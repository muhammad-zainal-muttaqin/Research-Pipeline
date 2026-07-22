#!/usr/bin/env bash
set -u
cd /workspace/experiments
CSV=runs/rtdetr_l_e60_i1280/weights/../results.csv
# tunggu sampai epoch >=52 terekam, atau proses mati sendiri
while :; do
  ep=$(tail -1 runs/rtdetr_l_e60_i1280/results.csv 2>/dev/null | cut -d, -f1)
  [ -n "$ep" ] && [ "$ep" -ge 52 ] 2>/dev/null && break
  pgrep -f train_rtdetr.py >/dev/null || break
  sleep 30
done
echo "[$(date +%H:%M:%S)] epoch tercapai: ${ep:-?} — menghentikan RT-DETR"
pkill -9 -f train_rtdetr.py; sleep 8
echo "[$(date +%H:%M:%S)] menjalankan evaluasi final best.pt (val + test + per-kelas)"
.venv/bin/python eval_rtdetr.py
echo "[$(date +%H:%M:%S)] EVAL SELESAI"
