#!/usr/bin/env bash
# eval_g2.sh — evaluasi matriks multi-seed G2, protokol tunggal pycocotools.
#
# Terikat aturan yang ditetapkan E-025: `hasil.json` TIDAK BOLEH dipakai
# membandingkan antar lengan, karena celah evaluatornya menskala dengan jumlah
# deteksi dan jumlah deteksi berbeda sistematis antar lengan (RGB-D 2,44x lebih
# banyak pada seed 42). Semua angka di sini datang dari eval_e022_paired.py.
#
# Empat perbandingan per seed, mengikuti rancangan kontrol E-022:
#   rgbd - rgb      hipotesis utama
#   derau - rgb     kontrol negatif kapasitas (kanal ke-4 tanpa informasi)
#   rgbd - derau    isolasi kandungan informasi depth
#   rgbd - tukar    kontrol registrasi (depth pohon lain)
#
# `--seed` diteruskan ke evaluator karena lengan derau dan tukar membangkitkan
# kanal ke-4 secara deterministik dari seed; memakai seed yang salah saat
# evaluasi berarti mengevaluasi kanal yang berbeda dari yang dilatih.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1
export YOLO_CONFIG_DIR=/tmp/Ultralytics
PY=./.venv/bin/python
R=/workspace/research-pipeline/runs/detect/runs_e022
OUT=/workspace/research-pipeline/experiments/results/E-022
B=${B:-2000}
ARCH=${ARCH:-yolo26n}
SEEDS=${SEEDS:-"42 1337 2024"}
mkdir -p "$OUT"
gagal=0

banding() {                # arch seed modal_a modal_b label
  local arch=$1 seed=$2 a=$3 b=$4 label=$5
  local ra="$R/${arch}_${a}_seed${seed}" rb="$R/${arch}_${b}_seed${seed}"
  local keluaran="$OUT/paired_${arch}_${label}_seed${seed}.json"

  if [ ! -d "$ra" ] || [ ! -d "$rb" ]; then
    echo "[lewati] $arch $label seed$seed — run belum ada"
    return 0
  fi
  if [ -s "$keluaran" ]; then
    echo "[lewati] $arch $label seed$seed — hasil sudah ada"
    return 0
  fi

  echo "=== $arch $label seed$seed $(date -Is) ==="
  $PY eval/eval_e022_paired.py --rgb "$ra" --modal-a "$a" --rgbd "$rb" --modal-b "$b" \
      --seed "$seed" --B "$B" --keluaran "$keluaran" \
      > "logs-evalg2-${arch}-${label}-seed${seed}.txt" 2>&1
  local rc=$?
  if [ "$rc" -ne 0 ] || [ ! -s "$keluaran" ]; then
    echo "[GAGAL] $arch $label seed$seed rc=$rc" >&2
    gagal=1
  fi
}

for seed in $SEEDS; do
  banding "$ARCH" "$seed" rgb   rgbd  depth_vs_rgb
  banding "$ARCH" "$seed" rgb   derau derau_vs_rgb
  banding "$ARCH" "$seed" derau rgbd  depth_vs_derau
  banding "$ARCH" "$seed" tukar rgbd  depth_vs_tukar
done

echo
echo "=== SELESAI eval G2 ($ARCH) $(date -Is) ==="
exit "$gagal"
