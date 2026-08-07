#!/usr/bin/env bash
# E-023 — evaluasi berpasangan 12 kontras: tiap lengan fusi vs baseline RGB.
#
# Protokol tunggal pycocotools [E-025]. `hasil.json` milik trainer TIDAK dipakai
# membandingkan antar lengan: pada E-022 ia membalik TANDA selisih (-0,00515 vs
# +0,01041), dan seluruh titik E-023 justru soal tanda dan besar selisih.
#
# Berpasangan per POHON, bukan per citra: empat sisi satu pohon tidak
# independen, resample per citra membuat CI terlalu sempit.
#
# CPU, bukan GPU-bound: prediksi memakai GPU sebentar lalu 2000x bootstrap
# berjalan di 32 proses. Karena itu kontras dijalankan BERURUTAN — menumpuknya
# hanya membuat mereka berebut core yang sama.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1
export YOLO_CONFIG_DIR=/tmp/Ultralytics

PY=./.venv/bin/python
R=/workspace/research-pipeline/runs/detect/runs_e023
OUT=/workspace/research-pipeline/experiments/results/E-023
SPLIT_DIR=/workspace/research-pipeline/experiments/splits/depth/seed42
B=${B:-2000}
mkdir -p "$OUT"

# lengan -> modalitas yang dipakai saat memuat citra.
#   awal/mid/late = rgbd (kanal ke-4 berisi depth asli)
#   derau         = kanal ke-4 berisi derau; WAJIB agar kontrol negatif dinilai
#                   dengan masukan yang sama seperti saat dilatih
modal_dari() {
  case "$1" in
    derau) echo derau ;;
    *)     echo rgbd ;;
  esac
}

gagal=0
for seed in 42 1337 2024; do
  for lengan in awal mid late derau; do
    rgb="$R/e023_rgb_seed${seed}"
    arm="$R/e023_${lengan}_seed${seed}"
    keluaran="$OUT/paired_${lengan}_vs_rgb_seed${seed}.json"
    if [ -f "$keluaran" ]; then echo "[lewati] $keluaran sudah ada"; continue; fi
    [ -f "$arm/weights/best.pt" ] || { echo "[GAGAL] bobot $arm tidak ada" >&2; gagal=1; continue; }
    echo "=== ${lengan} vs rgb, seed ${seed} — $(date -Is) ==="
    $PY eval/eval_e022_paired.py \
        --rgb "$rgb" --rgbd "$arm" \
        --modal-a rgb --modal-b "$(modal_dari "$lengan")" \
        --split-dir "$SPLIT_DIR" --split test \
        --seed "$seed" --B "$B" \
        --keluaran "$keluaran" || { echo "[GAGAL] $lengan seed$seed rc=$?" >&2; gagal=1; }
  done
done

echo
echo "=== RINGKASAN EVALUASI E-023 $(date -Is) ==="
echo "berkas hasil: $(find "$OUT" -name 'paired_*_seed*.json' | wc -l)/12"
[ "$gagal" -ne 0 ] && { echo "ADA KONTRAS YANG GAGAL" >&2; exit 1; }
echo "12 kontras lengkap"
