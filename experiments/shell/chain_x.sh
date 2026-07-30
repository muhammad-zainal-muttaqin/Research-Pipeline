#!/usr/bin/env bash
set -u
cd /workspace/experiments
# tunggu berdasarkan BERKAS, bukan pgrep — pgrep -f mencocoki baris perintah
# skrip ini sendiri dan membuatnya menunggu dirinya sendiri selamanya.
while [ ! -f runs/c4_e50_i1280_warna/hasil_selesai ]; do
  if ! ps -o pid= -C python 2>/dev/null | xargs -r ps -o args= -p 2>/dev/null | grep -q train_4cls_hi; then
    touch runs/c4_e50_i1280_warna/hasil_selesai; break
  fi
  sleep 60
done
echo "[$(date +%H:%M:%S)] run 1280 selesai, mulai yolo26x"
.venv/bin/python train_x.py > logs-x.txt 2>&1
echo "[$(date +%H:%M:%S)] yolo26x selesai (exit $?)"
