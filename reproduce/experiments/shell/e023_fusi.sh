#!/usr/bin/env bash
# E-023 (G4+G6) — fusi MENENGAH vs AKHIR vs AWAL, semua dari nol.
#
# Opsi 2 dari dua yang didaftar di STATUS.md: seluruh lengan dilatih TANPA bobot
# pratlatih. Bukan karena lebih murah — justru 3x lebih mahal — melainkan karena
# arsitektur fusi dua cabang lahir dari YAML kustom dan tidak punya checkpoint
# COCO yang cocok. Membandingkan fusi-dari-nol dengan lengan pratlatih akan
# didominasi ada-tidaknya pralatihan, bukan titik fusi.
#
# LIMA LENGAN, semuanya skala n, 150 epoch, split seed42:
#   rgb    baseline 3-kanal
#   awal   konkatenasi 4-kanal di masukan (replikasi E-022 tanpa pralatihan)
#   mid    cabang depth ringan sampai P2/4, fusi sebelum P3
#   late   dua backbone penuh, fusi pada P3/P4/P5
#   derau  kontrol negatif: kanal ke-4 berisi derau. WAJIB — SR-015 §6: tanpa
#          kontrol ini kenaikan apa pun tidak dapat dibedakan dari efek kapasitas
#
# 150 epoch, bukan 60. Dari nol dengan hanya 980 citra latih, 60 epoch hampir
# pasti underfit — dan hasil rendah akan salah dibaca sebagai "fusi gagal".
#
# 3 seed. E-027/E-029/E-031 semuanya menunjukkan satu seed membalik tanda
# kesimpulan; satu seed di sini = mengulang kesalahan yang menjatuhkan E-022.
#
# PARALELISME DARI ANGGARAN VRAM, bukan slot tetap (aturan CLAUDE.md, lahir dari
# OOM 1 Agustus): skala n ~3,0 GB, jadi 5 paralel = ~15 GB dari 20,4 GB.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1
export YOLO_CONFIG_DIR=/tmp/Ultralytics
source shell/periksa_run.sh

PY=./.venv/bin/python
EPOCHS=${EPOCHS:-150}
SEEDS=${SEEDS:-"42 1337 2024"}
BATCH=${BATCH:-16}
VRAM_PER_RUN=${VRAM_PER_RUN:-3400}     # MiB, skala n + margin
R=/workspace/research-pipeline/runs/detect/runs_e023
TANDA=.e023-tanda
mkdir -p "$TANDA"

tunggu_vram() {
  while true; do
    bebas=$(nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits)
    [ "$bebas" -ge "$VRAM_PER_RUN" ] && break
    sleep 30
  done
}

jalankan() {
  local lengan=$1 seed=$2
  local nama="e023_${lengan}_seed${seed}"
  local csv="$R/$nama/results.csv"
  if [ -f "$csv" ] && [ "$(awk -F, 'NR>1 && $1!="" {e[$1]=1} END{print length(e)+0}' "$csv")" -ge "$EPOCHS" ]; then
    echo "[lewati] $nama"; : > "$TANDA/lewati-$nama"; return 0
  fi
  echo "=== $nama $(date -Is) ==="
  case "$lengan" in
    rgb)   $PY train/train_depth4ch.py --arch yolo26n --modal rgb  --dari-nol \
             --epochs "$EPOCHS" --imgsz 640 --batch "$BATCH" --workers 5 --seed "$seed" \
             --project runs_e023 --name "$nama" > "logs-$nama.txt" 2>&1 ;;
    awal)  $PY train/train_depth4ch.py --arch yolo26n --modal rgbd --dari-nol \
             --epochs "$EPOCHS" --imgsz 640 --batch "$BATCH" --workers 5 --seed "$seed" \
             --project runs_e023 --name "$nama" > "logs-$nama.txt" 2>&1 ;;
    derau) $PY train/train_depth4ch.py --arch yolo26n --modal rgbd --depth-acak --dari-nol \
             --epochs "$EPOCHS" --imgsz 640 --batch "$BATCH" --workers 5 --seed "$seed" \
             --project runs_e023 --name "$nama" > "logs-$nama.txt" 2>&1 ;;
    mid|late)
           $PY train/train_fusion_2branch.py --fusi "$lengan" --skala n --modal rgbd \
             --epochs "$EPOCHS" --imgsz 640 --batch "$BATCH" --workers 5 --seed "$seed" \
             --project runs_e023 --name "$nama" > "logs-$nama.txt" 2>&1 ;;
  esac
  local rc=$?
  if periksa_run "$rc" "$csv" "$EPOCHS" "$nama"; then : > "$TANDA/ok-$nama"
  else : > "$TANDA/gagal-$nama"; fi
}

for seed in $SEEDS; do
  for lengan in rgb awal mid late derau; do
    tunggu_vram
    jalankan "$lengan" "$seed" &
    sleep 20                      # jeda agar pemuatan model tidak bertabrakan
  done
  wait
  echo "--- seed $seed selesai $(date -Is) ---"
done

echo
echo "=== RINGKASAN E-023 $(date -Is) ==="
echo "selesai bersih : $(find "$TANDA" -name 'ok-*' | wc -l)"
echo "dilewati       : $(find "$TANDA" -name 'lewati-*' | wc -l)"
mapfile -t g < <(find "$TANDA" -name 'gagal-*' -printf '%f\n' | sed 's/^gagal-//')
if [ ${#g[@]} -ne 0 ]; then printf 'GAGAL: %s\n' "${g[@]}"; exit 1; fi
echo "semua run lengkap"
