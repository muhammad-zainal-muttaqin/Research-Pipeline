#!/usr/bin/env bash
set -u
cd /workspace/experiments
PY=.venv/bin/python
log() { echo "[$(date +%H:%M:%S)] $*"; }

log "1/3 lanjutkan pelatihan RGB dari checkpoint"
$PY - <<'PYEOF' > logs-train-rgb-resume.txt 2>&1
from ultralytics import YOLO
YOLO("runs/rgb_e60_i640_s42/weights/last.pt").train(resume=True)
PYEOF
log "RGB selesai (exit $?)"

log "2/3 RGBD 4-kanal (susun saat pemuatan, tanpa salinan disk)"
$PY train_fusion.py --mode rgbd > logs-train-rgbd.txt 2>&1
log "RGBD selesai (exit $?)"

log "3/3 pelatihan ubin"
$PY tiling.py --train --nx 2 --ny 2 --epochs 20 > logs-train-tile.txt 2>&1
log "ubin selesai (exit $?)"
log "ANTRIAN SELESAI"
