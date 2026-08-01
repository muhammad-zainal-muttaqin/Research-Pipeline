#!/usr/bin/env bash
# G7 — sapuan kapasitas YOLO26 n -> m -> l pada SawitMVC-Depth.
#
# Menutup lubang dalam argumen SR-015. Temuan strukturalnya berbunyi "arah efek
# kanal ke-4 ditentukan KAPASITAS MODEL, bukan isi kanal": pada 2,57 jt param
# kanal ke-4 menaikkan dan isinya tidak penting (derau >= depth), pada 33,0 jt
# param ia menurunkan dan isinya penting (depth >> derau).
#
# Masalahnya, bukti itu melompat YOLO26n -> RT-DETR-L, yang mengubah KAPASITAS
# DAN ARSITEKTUR sekaligus. Klaim kapasitasnya belum terisolasi. YOLO26m
# (21,9 jt) dan YOLO26l (26,3 jt) mengisi celah di dalam SATU keluarga, sehingga
# kapasitas terpisah dari arsitektur:
#
#   - kalau pola derau-vs-depth berbalik di antara 2,57 dan 26,3 jt param,
#     klaim SR-015 diperkuat DAN titik baliknya terukur;
#   - kalau tidak berbalik sampai 26,3 jt, klaim itu harus dilemahkan menjadi
#     "arsitektur", bukan "kapasitas".
#
# Ketiga modal dijalankan, dan kontrol derau BUKAN opsional di sini: yang sedang
# diuji justru efek kapasitas, jadi tanpa pembanding kanal-tanpa-informasi
# kenaikan apa pun tidak dapat diatribusikan.
#
# Menunggu GPU longgar lebih dulu — yolo26m/l jauh lebih berat daripada n, dan
# dua RT-DETR-L saja sudah memakai ~16 GB dari 20,4 GB.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1
export YOLO_CONFIG_DIR=/tmp/Ultralytics
source shell/periksa_run.sh

PY=./.venv/bin/python
EPOCHS=${EPOCHS:-60}
SEEDS=${SEEDS:-42}
ARCHS=${ARCHS:-"yolo26m yolo26l"}
MODALS=${MODALS:-"rgb rgbd derau"}
BATCH=${BATCH:-8}
PAR=${PAR:-2}
R=/workspace/research-pipeline/runs/detect/runs_e022
TANDA=.g7-tanda
mkdir -p "$TANDA"

# --- tunggu antrean latihan lain selesai ---------------------------------
while pgrep -f "train_depth4ch.py|train_rfdetr_4ch.py" >/dev/null; do
  echo "[g7] menunggu antrean lain selesai... $(date -Is)"
  sleep 120
done
echo "[g7] GPU longgar, mulai sapuan $(date -Is)"

tunggu_slot() { while [ "$(jobs -rp | wc -l)" -ge "$1" ]; do wait -n; done; }

jalankan() {
  local arch=$1 modal=$2 seed=$3
  local nama="${arch}_${modal}_seed${seed}"
  local csv="$R/$nama/results.csv"
  if [ -f "$csv" ] && [ "$(awk -F, 'NR>1 && $1!="" {e[$1]=1} END{print length(e)+0}' "$csv")" -ge "$EPOCHS" ]; then
    echo "[lewati] $nama sudah lengkap"; : > "$TANDA/lewati-$nama"; return 0
  fi
  local flag="" modal_arg="$modal"
  [ "$modal" = "derau" ] && { flag="--depth-acak"; modal_arg="rgbd"; }
  [ "$modal" = "tukar" ] && { flag="--depth-tukar"; modal_arg="rgbd"; }

  echo "=== $nama ($(date -Is)) ==="
  $PY train/train_depth4ch.py --arch "$arch" --modal "$modal_arg" $flag \
      --epochs "$EPOCHS" --imgsz 640 --batch "$BATCH" --workers 8 \
      --seed "$seed" --name "$nama" > "logs-g7-$nama.txt" 2>&1
  local rc=$?
  if periksa_run "$rc" "$csv" "$EPOCHS" "$nama"; then : > "$TANDA/ok-$nama"
  else : > "$TANDA/gagal-$nama"; fi
}

for arch in $ARCHS; do
  for seed in $SEEDS; do
    for modal in $MODALS; do
      tunggu_slot "$PAR"
      jalankan "$arch" "$modal" "$seed" &
    done
  done
done
wait

echo
echo "=== RINGKASAN G7 $(date -Is) ==="
echo "selesai bersih : $(find "$TANDA" -name 'ok-*' | wc -l)"
echo "dilewati       : $(find "$TANDA" -name 'lewati-*' | wc -l)"
mapfile -t g < <(find "$TANDA" -name 'gagal-*' -printf '%f\n' | sed 's/^gagal-//')
if [ ${#g[@]} -ne 0 ]; then printf 'GAGAL: %s\n' "${g[@]}"; exit 1; fi
echo "semua run lengkap"
