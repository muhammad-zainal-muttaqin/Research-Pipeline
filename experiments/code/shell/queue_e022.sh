#!/usr/bin/env bash
# E-022: antrean run setelah pasangan yolo26n selesai.
# Dijalankan berurutan supaya tidak memperebutkan VRAM L4 23 GB.
set -uo pipefail
SKRIP_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd reproduce/experiments
export YOLO_CONFIG_DIR=/tmp/Ultralytics
PY=./.venv/bin/python
EPOCHS=60
source "$SKRIP_DIR/periksa_run.sh"
gagal=0

# tunggu pasangan yolo26n beres
while pgrep -f "train_depth4ch.py --arch yolo26n" >/dev/null; do sleep 30; done
echo "[antrean] pasangan yolo26n selesai, lanjut RT-DETR-L $(date -Is)"

for modal in rgb rgbd; do
  echo "[antrean] mulai rtdetr-l $modal $(date -Is)"
  $PY train_depth4ch.py --arch rtdetr-l --modal $modal --epochs $EPOCHS --imgsz 640 \
      --batch 8 --workers 8 > logs-e022-rtdetrl-$modal.txt 2>&1
  rc=$?   # WAJIB baris tersendiri, sebelum substitusi perintah apa pun
  periksa_run "$rc" "runs/detect/runs_e022/rtdetr-l_${modal}_seed42/results.csv" \
      "$EPOCHS" "rtdetr-l $modal" || gagal=1
done

if [ "$gagal" -ne 0 ]; then
  echo "[antrean] SELESAI DENGAN KEGAGALAN — jangan pakai angkanya $(date -Is)" >&2
  exit 1
fi
echo "[antrean] SELESAI $(date -Is)"
