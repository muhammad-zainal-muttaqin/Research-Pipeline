#!/usr/bin/env bash
set -u
cd /workspace/experiments
PY=.venv/bin/python
log() { echo "[$(date +%H:%M:%S)] $*"; }
log "menunggu antrian 3 selesai..."
while pgrep -f "run_queue3.sh" > /dev/null; do sleep 60; done
log "mulai loss ordinal (I-22)"
$PY train_ordinal.py --alpha 0.2 --epochs 60 > logs-train-ordinal.txt 2>&1
log "ordinal selesai (exit $?)"
log "ANTRIAN 4 SELESAI"
