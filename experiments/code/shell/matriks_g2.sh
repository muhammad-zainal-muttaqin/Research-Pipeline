#!/usr/bin/env bash
# G2 — matriks multi-seed E-022 dengan kode _fix.
#
# Melengkapi apa yang AUDIT-E022 sebut "sedang diproduksi" tetapi tidak pernah
# selesai maupun diarsipkan: 12 run YOLO26n (4 modal x 3 seed) + 9 RT-DETR-L
# (3 modal x 3 seed). Tiga run RT-DETR-L yang dulu mati senyap
# (rtdetr-l_tukar_seed1337, rtdetr-l_derau_seed2024, rtdetr-l_tukar_seed2024)
# ikut di sini dan kini dijaga periksa_run().
#
# Sifat penting:
#   - DAPAT DILANJUTKAN. Run yang results.csv-nya sudah lengkap dilewati, jadi
#     skrip boleh dijalankan ulang setelah mati listrik/timeout tanpa mengulang
#     pekerjaan yang sudah benar.
#   - BERHENTI PADA KEGAGALAN NYATA hanya di akhir; run lain tetap dicoba agar
#     satu crash tidak membatalkan semalam penuh komputasi. Ringkasan kegagalan
#     dicetak di akhir dan status keluar bukan-nol.
#
# Pemakaian:
#   bash shell/matriks_g2.sh            # seluruh matriks
#   ARCH=yolo26n bash shell/matriks_g2.sh   # satu arsitektur saja
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1
export YOLO_CONFIG_DIR=/tmp/Ultralytics
source shell/periksa_run.sh

PY=./.venv/bin/python
EPOCHS=${EPOCHS:-60}
SEEDS=${SEEDS:-"42 1337 2024"}
R=/workspace/research-pipeline/runs/detect/runs_e022

# Job berjalan di subshell latar, jadi variabel tidak bisa dipakai untuk
# mengumpulkan status — hasilnya ditulis ke direktori penanda dan dibaca lagi
# oleh induk setelah `wait`.
TANDA=${TANDA:-.g2-tanda}
rm -rf "$TANDA"; mkdir -p "$TANDA"

jalankan() {
  local arch=$1 modal=$2 seed=$3 batch=$4
  local nama="${arch}_${modal}_seed${seed}"
  local csv="$R/$nama/results.csv"

  # lanjutkan: lewati yang sudah lengkap
  if [ -f "$csv" ] && [ "$(awk -F, 'NR>1 && $1!="" {e[$1]=1} END{print length(e)+0}' "$csv")" -ge "$EPOCHS" ]; then
    echo "[lewati] $nama sudah lengkap"
    : > "$TANDA/lewati-$nama"
    return 0
  fi

  # modal 'derau' dan 'tukar' adalah kontrol negatif: keduanya memakai jalur
  # rgbd, dibedakan oleh flag. Lihat AUDIT-E022 cacat #3 dan #4 untuk mengapa
  # keduanya wajib memakai kode _fix (donor per-split, RNG deterministik).
  local flag=""
  case "$modal" in
    derau) flag="--depth-acak" ;;
    tukar) flag="--depth-tukar" ;;
  esac
  local modal_arg="$modal"
  [ -n "$flag" ] && modal_arg="rgbd"

  echo "=== $nama ($(date -Is)) ==="
  $PY train/train_depth4ch.py --arch "$arch" --modal "$modal_arg" $flag \
      --epochs "$EPOCHS" --imgsz 640 --batch "$batch" --workers 8 \
      --seed "$seed" --name "$nama" > "logs-g2-$nama.txt" 2>&1
  local rc=$?
  if periksa_run "$rc" "$csv" "$EPOCHS" "$nama"; then
    : > "$TANDA/ok-$nama"
  else
    : > "$TANDA/gagal-$nama"
  fi
}

# --- kolam slot paralel ---------------------------------------------------
# Satu run yolo26n batch16@640 memakai ~3 GB VRAM dari 20 GB, dan GPU hanya
# terpakai ~17% saat satu run jalan sendiri: menjalankannya berurutan membuang
# kapasitas. RT-DETR-L (33,0 jt param) jauh lebih berat, jadi kolamnya lebih
# sempit. Angka ini batas AMAN, bukan batas maksimum — biar ada ruang untuk
# lonjakan alokasi saat validasi akhir epoch.
PAR_YOLO=${PAR_YOLO:-4}
PAR_RTDETR=${PAR_RTDETR:-2}

tunggu_slot() {           # tunggu sampai job aktif < $1
  local batas=$1
  while [ "$(jobs -rp | wc -l)" -ge "$batas" ]; do wait -n; done
}

for seed in $SEEDS; do
  if [ "${ARCH:-yolo26n}" = "yolo26n" ] || [ -z "${ARCH:-}" ]; then
    for modal in rgb rgbd derau tukar; do
      tunggu_slot "$PAR_YOLO"
      jalankan yolo26n "$modal" "$seed" 16 &
    done
  fi
done
wait

if [ "${ARCH:-rtdetr-l}" = "rtdetr-l" ] || [ -z "${ARCH:-}" ]; then
  for seed in $SEEDS; do
    for modal in rgb rgbd derau; do
      tunggu_slot "$PAR_RTDETR"
      jalankan rtdetr-l "$modal" "$seed" 8 &
    done
  done
fi
wait

echo
echo "=== RINGKASAN G2 $(date -Is) ==="
n_ok=$(find "$TANDA" -name 'ok-*' | wc -l)
n_lewati=$(find "$TANDA" -name 'lewati-*' | wc -l)
mapfile -t daftar_gagal < <(find "$TANDA" -name 'gagal-*' -printf '%f\n' | sed 's/^gagal-//')
echo "selesai bersih          : $n_ok"
echo "dilewati (sudah lengkap): $n_lewati"
if [ ${#daftar_gagal[@]} -ne 0 ]; then
  echo "GAGAL ${#daftar_gagal[@]}:"
  printf '  %s\n' "${daftar_gagal[@]}"
  echo "jalankan ulang skrip ini — run yang sudah lengkap akan dilewati"
  exit 1
fi
echo "semua run lengkap"
