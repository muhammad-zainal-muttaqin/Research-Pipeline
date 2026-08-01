#!/usr/bin/env bash
# G8 — ulangi ukuran inkonsistensi lintas-sisi di SawitMVC (daya uji ~40x).
#
# E-026 menandai dua batas yang keduanya soal DAYA UJI, bukan teori: hanya 82
# tandan terukur, dan B4 NOL terwakili karena tidak pernah terdeteksi di >= 2
# sisi — padahal B4 kelas paling geometris dan yang paling mungkin dibantu depth.
#
# SawitMVC jauh lebih besar: 18.540 kotak vs 2.299, 953 pohon vs 352, 4-8 sisi
# per pohon vs 4, dan 7.328 bunch multi-sisi vs 182. Skema JSON kedua dataset
# sudah diverifikasi IDENTIK (bunches[].appearances dengan side_index dan
# bbox_pixel), jadi ukuran yang sama berlaku langsung.
#
# Resep latihan sengaja dibuat IDENTIK dengan lengan RGB SawitMVC-Depth
# (yolo26n, 60 epoch, imgsz 640, batch 16, seed 42, HSV mati) supaya laju
# inkonsistensi kedua dataset dapat diperbandingkan. imgsz 640 dipilih pengguna.
#
# BATAS YANG TIDAK BOLEH DIHALUSKAN: SawitMVC tidak punya depth. G8 hanya
# memberi laju BASELINE dengan CI yang jauh lebih sempit dan pemecahan per
# kelas. Pertanyaan "apakah depth menstabilkan identitas lintas-sisi" tetap
# hanya terjawab di SawitMVC-Depth (E-026).
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1
export YOLO_CONFIG_DIR=/tmp/Ultralytics
source shell/periksa_run.sh

PY=./.venv/bin/python
EPOCHS=${EPOCHS:-60}
IMGSZ=${IMGSZ:-640}
SEED=${SEED:-42}
NAMA="yolo26n_sawitmvc_rgb_seed${SEED}"
R=/workspace/research-pipeline/runs/detect/runs_e022
SPLIT_ROOT=/workspace/research-pipeline/evidence/experiments/splits_rgb
OUT=/workspace/research-pipeline/evidence/experiments/results/E-028

# --- tunggu GPU longgar ---------------------------------------------------
while pgrep -f "train_depth4ch.py|train_rfdetr_4ch.py" >/dev/null; do
  echo "[g8] menunggu antrean latihan lain... $(date -Is)"
  sleep 120
done

# --- 1. latih baseline RGB di SawitMVC ------------------------------------
if [ -f "$R/$NAMA/results.csv" ] && \
   [ "$(awk -F, 'NR>1 && $1!="" {e[$1]=1} END{print length(e)+0}' "$R/$NAMA/results.csv")" -ge "$EPOCHS" ]; then
  echo "[g8] $NAMA sudah lengkap, lewati latihan"
else
  echo "[g8] latih $NAMA $(date -Is)"
  $PY train/train_depth4ch.py --arch yolo26n --modal rgb \
      --split-root "$SPLIT_ROOT" --split sawitmvc \
      --epochs "$EPOCHS" --imgsz "$IMGSZ" --batch 16 --workers 8 \
      --seed "$SEED" --name "$NAMA" > "logs-g8-$NAMA.txt" 2>&1
  rc=$?
  periksa_run "$rc" "$R/$NAMA/results.csv" "$EPOCHS" "$NAMA" || exit 1
fi

# --- 2. ukur inkonsistensi lintas-sisi ------------------------------------
mkdir -p "$OUT"
echo "[g8] ukur konsistensi lintas-sisi $(date -Is)"
$PY analysis/cross_side_consistency.py \
    --bobot "$R/$NAMA/weights/best.pt" --modal rgb \
    --data-root /workspace/SawitMVC/data \
    --split-dir "$SPLIT_ROOT/sawitmvc" --split test \
    --imgsz "$IMGSZ" \
    --keluaran "$OUT/konsistensi_sawitmvc_rgb_seed${SEED}.json" \
    > "logs-g8-konsistensi.txt" 2>&1
rc=$?
[ "$rc" -ne 0 ] && { echo "[GAGAL] pengukuran konsistensi rc=$rc" >&2; exit 1; }

echo "=== G8 SELESAI $(date -Is) ==="
tail -30 "logs-g8-konsistensi.txt"
