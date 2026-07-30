#!/usr/bin/env bash
# Tambal 3 lubang matriks P0 RT-DETR-L (task #27).
#
# PENTING — bug yang diperbaiki di skrip ini (task #26):
#   Pola LAMA di antre_p0a/p0b/p0b_controls.sh:
#       echo "[$(date +%H:%M:%S)] SELESAI $nama rc=$?"
#   Substitusi $(date) DIEKSEKUSI LEBIH DULU dan me-reset $?, jadi $? yang
#   terbaca adalah status `date` -> SELALU 0. Run yang crash dilaporkan sukses
#   dan antrean melanjut tanpa peringatan. Itulah sebab tiga lubang ini lolos.
#   Di bawah, rc ditangkap ke variabel SEBELUM ada substitusi perintah apa pun.
#
# Dijalankan dengan setsid supaya proses latih TIDAK ikut mati saat terminal
# atau sesi agen mana pun ditutup (dugaan penyebab tukar_seed1337 mati di
# epoch 27 — waktunya bertepatan dengan Codex distop).
set -u
cd /workspace/experiments
source .venv/bin/activate
mkdir -p logs_gap

jalankan() {  # nama arch seed imgsz batch flag
  local nama="$1" arch="$2" seed="$3" imgsz="$4" batch="$5" flag="$6"
  local csv="runs/detect/runs_e022/${nama}/results.csv"
  local n=0
  [ -f "$csv" ] && n=$(wc -l < "$csv")
  if [ "$n" -gt 60 ]; then
    echo "[$(date +%H:%M:%S)] LEWAT ${nama} (sudah ${n} baris)"
    return 0
  fi
  echo "[$(date +%H:%M:%S)] MULAI ${nama}"
  python train_depth4ch.py --name "${nama}" --arch "$arch" --modal rgbd \
      --seed "$seed" --imgsz "$imgsz" --batch "$batch" --workers 16 "$flag" \
      > "logs_gap/${nama}.log" 2>&1
  local rc=$?                      # <-- ditangkap SEBELUM $(date), ini kuncinya
  local akhir=0
  [ -f "$csv" ] && akhir=$(wc -l < "$csv")
  if [ "$rc" -ne 0 ] || [ "$akhir" -le 60 ]; then
    echo "[$(date +%H:%M:%S)] *** GAGAL ${nama} rc=${rc} baris=${akhir} — lihat logs_gap/${nama}.log"
  else
    echo "[$(date +%H:%M:%S)] SELESAI ${nama} rc=${rc} baris=${akhir}"
  fi
  return 0                          # jangan hentikan antrean; lubang dicatat
}

echo "[$(date +%H:%M:%S)] === TAMBAL P0 RT-DETR-L: 3 run, ~50 mnt/run ==="
jalankan rtdetr-l_tukar_seed1337_fix rtdetr-l 1337 640 8 --depth-tukar
jalankan rtdetr-l_derau_seed2024_fix rtdetr-l 2024 640 8 --depth-acak
jalankan rtdetr-l_tukar_seed2024_fix rtdetr-l 2024 640 8 --depth-tukar
echo "[$(date +%H:%M:%S)] === TAMBAL P0 SELESAI ==="

# Ringkasan kelengkapan matriks di akhir, supaya lubang tidak lolos lagi.
python3 - <<'PY'
import os, csv
for arch in ("yolo26n", "rtdetr-l"):
    for a in ("rgb", "rgbd", "derau", "tukar"):
        for s in (42, 1337, 2024):
            n = f"{arch}_{a}_seed{s}" + ("_fix" if a in ("derau", "tukar") else "")
            c = f"runs/detect/runs_e022/{n}/results.csv"
            ep = len(list(csv.reader(open(c)))) - 1 if os.path.isfile(c) else 0
            if ep < 60:
                print(f"MASIH BOLONG: {n} (ep={ep})")
print("cek kelengkapan matriks selesai")
PY
