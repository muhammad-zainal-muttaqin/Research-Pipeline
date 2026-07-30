#!/usr/bin/env bash
# Kontrol REGISTRASI berpasangan: depth benar vs depth milik citra lain.
# Titik estimasi sudah menunjukkan depth-tertukar (0,3771) MENGALAHKAN depth
# benar (0,3492) di yolo26n — CI menentukan apakah selisih itu nyata.
set -uo pipefail
cd reproduce/experiments
PY=./.venv/bin/python
R=runs/detect/runs_e022
while pgrep -f antre_dvd.sh >/dev/null; do sleep 30; done
echo "[tukar] antrean dvd selesai $(date -Is)"
$PY -u eval_e022_paired.py --rgb $R/yolo26n_tukar_seed42 --modal-a tukar \
    --rgbd $R/yolo26n_rgbd_seed42 --modal-b rgbd --imgsz 640 --B 1000 \
    --keluaran results/e022_paired_yolo26n_depth_vs_tukar.json > logs-e022-dvd-tukar.txt 2>&1
echo "[tukar] rc=$? $(date -Is)"
