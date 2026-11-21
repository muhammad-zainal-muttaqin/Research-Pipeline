#!/usr/bin/env bash
# Antrian pelatihan berurutan. GPU L4 hanya muat satu pelatihan sekaligus,
# jadi tahap berikutnya menunggu tahap sebelumnya selesai daripada membiarkan
# GPU menganggur di antara giliran saya memeriksa.
set -u
cd experiments/code
PY=.venv/bin/python

log() { echo "[$(date +%H:%M:%S)] $*"; }

log "menunggu pelatihan RGB selesai..."
while pgrep -f "train_fusion.py --mode rgb" > /dev/null; do sleep 30; done
log "RGB selesai."

log "mulai RGBD 4-kanal"
$PY train_fusion.py --mode rgbd > logs-train-rgbd.txt 2>&1
log "RGBD selesai (exit $?)"

log "menunggu perakitan ubin..."
while pgrep -f "tiling.py --build" > /dev/null; do sleep 20; done
log "mulai pelatihan ubin"
$PY tiling.py --train --nx 2 --ny 2 --epochs 20 > logs-train-tile.txt 2>&1
log "ubin selesai (exit $?)"

log "ANTRIAN SELESAI"
