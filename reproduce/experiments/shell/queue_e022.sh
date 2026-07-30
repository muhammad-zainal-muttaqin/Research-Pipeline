#!/usr/bin/env bash
# E-022: antrean run setelah pasangan yolo26n selesai.
# Dijalankan berurutan supaya tidak memperebutkan VRAM L4 23 GB.
set -uo pipefail
cd reproduce/experiments
export YOLO_CONFIG_DIR=/tmp/Ultralytics
PY=./.venv/bin/python

# tunggu pasangan yolo26n beres
while pgrep -f "train_depth4ch.py --arch yolo26n" >/dev/null; do sleep 30; done
echo "[antrean] pasangan yolo26n selesai, lanjut RT-DETR-L $(date -Is)"

for modal in rgb rgbd; do
  echo "[antrean] mulai rtdetr-l $modal $(date -Is)"
  $PY train_depth4ch.py --arch rtdetr-l --modal $modal --epochs 60 --imgsz 640 \
      --batch 8 --workers 8 > logs-e022-rtdetrl-$modal.txt 2>&1
  echo "[antrean] selesai rtdetr-l $modal rc=$? $(date -Is)"
done

echo "[antrean] SELESAI $(date -Is)"
