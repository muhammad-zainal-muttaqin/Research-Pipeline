#!/usr/bin/env bash
# Kontrol derau RF-DETR Nano — uji paling menentukan yang belum ada:
# RF-DETR menunjukkan kenaikan depth TERBESAR (+0,0439), jadi kalau derau juga
# memberi kenaikan setara, maka kenaikan terbesar di E-022 pun bukan dari
# kandungan informasi kedalaman.
set -uo pipefail
cd /workspace/experiments
while pgrep -f "train_depth4ch.py --arch yolo26n --modal rgbd --depth-tukar" >/dev/null; do sleep 30; done
echo "[antre] depth-tukar selesai $(date -Is)"
rm -f runs_e022/*/checkpoint_[0-9]*.ckpt runs_e022/*/last.ckpt 2>/dev/null
./.venv/bin/python -u train_rfdetr_4ch.py --varian nano --modal rgbd --depth-acak \
    --epochs 60 --resolution 640 --batch 8 --grad-accum 2 --workers 8 \
    --output runs_e022/rfdetrnano_derau > logs-e022-rfdetrnano-derau.txt 2>&1
echo "[antre] rfdetr derau rc=$? $(date -Is)"
rm -f runs_e022/*/checkpoint_[0-9]*.ckpt runs_e022/*/last.ckpt 2>/dev/null
echo "[antre] disk: $(du -sm /workspace | cut -f1) MB"
