#!/usr/bin/env bash
# E-023 seed 2024 — penjadwal berbasis anggaran VRAM, tanpa barrier.
#
# `e023_fusi.sh` menahan seed berikutnya di balik `wait`: seluruh lima lengan
# seed sebelumnya harus tuntas sebelum satu pun lengan seed berikutnya mulai.
# Karena lengan tidak selesai bersamaan (rgb 150 epoch lebih cepat daripada
# late yang punya dua backbone penuh), barrier itu meninggalkan VRAM menganggur
# belasan menit di tiap pergantian seed. Driver seed42/seed1337 sudah dihentikan
# setelah seed1337 mulai; skrip ini menggantikan sisa kerjanya.
#
# Ambang 5500 MiB, bukan 3400: 3400 mengukur pemakaian SAAT PELUNCURAN,
# sedangkan run tumbuh 2,35 -> 4,04 GB selama latihan. Ambang saat-peluncuran
# itulah yang menyebabkan OOM 1 Agustus.
#
# Penjadwal TUNGGAL. Dua penjadwal yang saling buta terhadap alokasi masing-
# masing adalah separuh kedua dari OOM yang sama.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1
export YOLO_CONFIG_DIR=/tmp/Ultralytics
source shell/periksa_run.sh

PY=./.venv/bin/python
EPOCHS=${EPOCHS:-150}
SEED=${SEED:-2024}
BATCH=${BATCH:-16}
AMBANG=${AMBANG:-5500}
R=/workspace/research-pipeline/runs/detect/runs_e023

for lengan in rgb awal mid late derau; do
  nama="e023_${lengan}_seed${SEED}"
  csv="$R/$nama/results.csv"
  if [ -f "$csv" ] && [ "$(awk -F, 'NR>1 && $1!="" {e[$1]=1} END{print length(e)+0}' "$csv")" -ge "$EPOCHS" ]; then
    echo "[lewati] $nama sudah lengkap"; continue
  fi
  # Direktori run yang ada tapi belum lengkap akan membuat ultralytics memakai
  # nama bersuffiks (nama2), sehingga hasilnya tidak terbaca oleh evaluasi yang
  # mencari nama aslinya. Lebih baik gagal keras.
  if [ -d "$R/$nama" ]; then
    echo "[GAGAL] $R/$nama sudah ada tapi belum lengkap — periksa manual" >&2
    continue
  fi
  while true; do
    bebas=$(nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits)
    [ "$bebas" -ge "$AMBANG" ] && break
    sleep 60
  done
  echo "=== $nama, VRAM bebas ${bebas} MiB, $(date -Is) ==="
  case "$lengan" in
    rgb)   $PY train/train_depth4ch.py --arch yolo26n --modal rgb  --dari-nol \
             --epochs "$EPOCHS" --imgsz 640 --batch "$BATCH" --workers 5 --seed "$SEED" \
             --project runs_e023 --name "$nama" > "logs-$nama.txt" 2>&1 & ;;
    awal)  $PY train/train_depth4ch.py --arch yolo26n --modal rgbd --dari-nol \
             --epochs "$EPOCHS" --imgsz 640 --batch "$BATCH" --workers 5 --seed "$SEED" \
             --project runs_e023 --name "$nama" > "logs-$nama.txt" 2>&1 & ;;
    derau) $PY train/train_depth4ch.py --arch yolo26n --modal rgbd --depth-acak --dari-nol \
             --epochs "$EPOCHS" --imgsz 640 --batch "$BATCH" --workers 5 --seed "$SEED" \
             --project runs_e023 --name "$nama" > "logs-$nama.txt" 2>&1 & ;;
    mid|late)
           $PY train/train_fusion_2branch.py --fusi "$lengan" --skala n --modal rgbd \
             --epochs "$EPOCHS" --imgsz 640 --batch "$BATCH" --workers 5 --seed "$SEED" \
             --project runs_e023 --name "$nama" > "logs-$nama.txt" 2>&1 & ;;
  esac
  sleep 90    # beri waktu run baru mencapai alokasi mantapnya sebelum
              # pembacaan memory.free berikutnya, agar tidak terhitung longgar
              # dua kali dan meluncurkan lengan berikutnya terlalu cepat
done
wait
echo "=== seed $SEED selesai $(date -Is) ==="
