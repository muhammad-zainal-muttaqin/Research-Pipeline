#!/usr/bin/env bash
set -u
cd /workspace/experiments
PY=.venv/bin/python
log() { echo "[$(date +%H:%M:%S)] $*"; }
log "menunggu antrian sebelumnya selesai..."
while pgrep -f "run_queue2.sh" > /dev/null; do sleep 60; done
log "mulai RGB+tekstur (I-21)"
$PY train_fusion.py --mode rgbt > logs-train-rgbt.txt 2>&1
log "RGB+tekstur selesai (exit $?)"
log "ANTRIAN 3 SELESAI"
