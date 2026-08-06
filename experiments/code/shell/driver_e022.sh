#!/usr/bin/env bash
# E-022 driver: jalankan sisa pekerjaan berurutan, bersihkan checkpoint sambil
# jalan, dan tulis progres ke logs-e022-driver.txt supaya bisa di-poll.
#
# Pelajaran dari kematian senyap run RF-DETR RGB-D: rfdetr menulis snapshot
# 490 MB tiap 10 epoch. Dua run = 5,8 GB, cukup untuk menghabiskan sisa kuota
# 50 GB dan mematikan proses TANPA pesan apa pun (checkpoint terpotong tepat
# 256 MB). Karena itu pembersihan dilakukan segera setelah tiap run, bukan di
# akhir.
set -uo pipefail
cd reproduce/experiments
export YOLO_CONFIG_DIR=/tmp/Ultralytics
PY=./.venv/bin/python

lapor() { echo "[driver $(date +%H:%M:%S)] $*"; }
bersihkan() {
  rm -f runs_e022/*/checkpoint_[0-9]*.ckpt runs_e022/*/last.ckpt 2>/dev/null
  lapor "disk /workspace: $(du -sm /workspace 2>/dev/null | cut -f1) MB"
}

# tunggu evaluasi yang sedang jalan
while pgrep -f "eval_rfdetr_e022|modal-b derau" >/dev/null; do sleep 30; done
lapor "evaluasi yang tertunda selesai"
bersihkan

# TODO #10: kontrol derau pada RT-DETR-L. Menjawab langsung kenapa arah efek
# depth berlawanan antar arsitektur: kalau derau JUGA menurunkan mAP di RT-DETR,
# polanya "model besar tak butuh kanal ke-4, model kecil terbantu apa pun
# isinya" — menjelaskan kedua arsitektur tanpa teori soal HGStem.
if [ ! -f runs/detect/runs_e022/rtdetr-l_derau_seed42/hasil.json ]; then
  lapor "mulai kontrol derau RT-DETR-L (~50 mnt)"
  $PY -u train_depth4ch.py --arch rtdetr-l --modal rgbd --depth-acak \
      --epochs 60 --imgsz 640 --batch 8 --workers 8 \
      --name rtdetr-l_derau_seed42 > logs-e022-rtdetrl-derau.txt 2>&1
  lapor "kontrol derau RT-DETR-L rc=$?"
  bersihkan
fi

# uji berpasangan untuk kontrol derau RT-DETR
if [ ! -f results/e022_paired_rtdetrl_derau.json ]; then
  lapor "uji berpasangan derau RT-DETR-L"
  $PY -u eval_e022_paired.py --rgb runs/detect/runs_e022/rtdetr-l_rgb_seed42 \
      --rgbd runs/detect/runs_e022/rtdetr-l_derau_seed42 --modal-b derau \
      --imgsz 640 --B 2000 --keluaran results/e022_paired_rtdetrl_derau.json \
      > logs-e022-paired-rtdetrl-derau.txt 2>&1
  lapor "uji berpasangan derau RT-DETR-L rc=$?"
fi

bersihkan
lapor "DRIVER SELESAI"
