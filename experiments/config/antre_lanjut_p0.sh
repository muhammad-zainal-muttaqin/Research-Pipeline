#!/usr/bin/env bash
# Rantai penutup P0 — dibuat supaya seluruh deliverable MENDARAT TANPA AGEN.
#
# Urutan:
#   1. tunggu driver tambal (3 run RT-DETR-L) selesai
#   2. tunggu driver eval putaran pertama selesai
#   3. jalankan ulang antre_eval_p0.sh -> mengisi 3 sel RT-DETR-L yang tadi
#      belum ada run-nya (skrip itu melewati JSON yang sudah ada, jadi aman)
#   4. tulis results/p0_multiseed/RINGKASAN.{md,json}
#
# rc ditangkap SEBELUM substitusi perintah apa pun — lihat catatan bug di
# antre_tambal_p0.sh.
set -u
cd /workspace/experiments
source .venv/bin/activate

for pid in "$@"; do
  echo "[$(date +%H:%M:%S)] menunggu PID $pid ..."
  while [ -d "/proc/$pid" ]; do sleep 30; done
  echo "[$(date +%H:%M:%S)] PID $pid selesai"
done

echo "[$(date +%H:%M:%S)] === EVAL PUTARAN 2: isi sel RT-DETR-L yang baru ==="
./antre_eval_p0.sh > logs_eval_p0_putaran2.log 2>&1
rc=$?
echo "[$(date +%H:%M:%S)] eval putaran 2 rc=${rc}"

echo "[$(date +%H:%M:%S)] === RINGKASAN AKHIR ==="
python ringkas_p0.py > logs_ringkas_p0.log 2>&1
rc=$?
echo "[$(date +%H:%M:%S)] ringkas_p0 rc=${rc} -> results/p0_multiseed/RINGKASAN.md"

# Laporan kelengkapan terakhir, supaya lubang tidak lolos tanpa terlihat.
python3 - <<'PY'
import os, csv, glob
bolong = []
for arch in ("yolo26n", "rtdetr-l"):
    for a in ("rgb", "rgbd", "derau", "tukar"):
        for s in (42, 1337, 2024):
            n = f"{arch}_{a}_seed{s}" + ("_fix" if a in ("derau", "tukar") else "")
            c = f"runs/detect/runs_e022/{n}/results.csv"
            ep = len(list(csv.reader(open(c)))) - 1 if os.path.isfile(c) else 0
            if ep < 60:
                bolong.append(f"{n} (ep={ep})")
j = len(glob.glob("results/p0_multiseed/*_seed*.json"))
print(f"JSON berpasangan: {j}/18 (2 arsitektur x 3 seed x 3 pembanding)")
print("MATRIKS LENGKAP" if not bolong else "MASIH BOLONG:\n  " + "\n  ".join(bolong))
PY

echo "[$(date +%H:%M:%S)] === P0 TUNTAS ==="
