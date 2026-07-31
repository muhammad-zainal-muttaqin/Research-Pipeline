#!/usr/bin/env bash
# E-022 antrean lanjutan: kontrol negatif + pasangan RF-DETR Nano.
# Menunggu antrean pertama (rtdetr-l) selesai supaya tidak berebut VRAM.
set -uo pipefail
SKRIP_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd reproduce/experiments
export YOLO_CONFIG_DIR=/tmp/Ultralytics
PY=./.venv/bin/python
EPOCHS=60
source "$SKRIP_DIR/periksa_run.sh"
gagal=0

while pgrep -f "train_depth4ch.py --arch rtdetr-l" >/dev/null || pgrep -f queue_e022.sh >/dev/null; do sleep 30; done
echo "[antrean-b] mulai $(date -Is)"

# Kontrol negatif: kanal ke-4 = derau. Kalau ini menaikkan mAP sebanyak depth
# asli, kenaikan berasal dari kapasitas stem, bukan informasi kedalaman.
echo "[antrean-b] yolo26n kontrol-derau $(date -Is)"
$PY train_depth4ch.py --arch yolo26n --modal rgbd --depth-acak --epochs $EPOCHS --imgsz 640 \
    --batch 16 --name yolo26n_derau_seed42 > logs-e022-yolo26n-derau.txt 2>&1
rc=$?
periksa_run "$rc" "runs/detect/runs_e022/yolo26n_derau_seed42/results.csv" \
    "$EPOCHS" "yolo26n kontrol-derau" || gagal=1

for modal in rgb rgbd; do
  echo "[antrean-b] mulai rfdetr-nano $modal $(date -Is)"
  $PY train_rfdetr_4ch.py --varian nano --modal $modal --epochs $EPOCHS --resolution 640 \
      --batch 8 --grad-accum 2 --workers 8 \
      --output runs_e022/rfdetrnano_$modal > logs-e022-rfdetrnano-$modal.txt 2>&1
  rc=$?
  # rfdetr boleh berhenti dini (early stopping), jadi yang dijaga hanya rc dan
  # keberadaan artefaknya — bukan jumlah epoch penuh.
  periksa_run "$rc" "runs_e022/rfdetrnano_$modal/metrics.csv" 0 \
      "rfdetr-nano $modal" || gagal=1
done

if [ "$gagal" -ne 0 ]; then
  echo "[antrean-b] SELESAI DENGAN KEGAGALAN — jangan pakai angkanya $(date -Is)" >&2
  exit 1
fi
echo "[antrean-b] SELESAI $(date -Is)"
