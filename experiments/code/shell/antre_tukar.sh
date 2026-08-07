#!/usr/bin/env bash
# Kontrol REGISTRASI berpasangan: depth benar vs depth milik citra lain.
# Titik estimasi sudah menunjukkan depth-tertukar (0,3771) MENGALAHKAN depth
# benar (0,3492) di yolo26n — CI menentukan apakah selisih itu nyata.
set -uo pipefail
cd experiments/code
PY=./.venv/bin/python
R=runs/detect/runs_e022
while pgrep -f antre_dvd.sh >/dev/null; do sleep 30; done
echo "[tukar] antrean dvd selesai $(date -Is)"
OUT=results/e022_paired_yolo26n_depth_vs_tukar.json
$PY -u eval_e022_paired.py --rgb $R/yolo26n_tukar_seed42 --modal-a tukar \
    --rgbd $R/yolo26n_rgbd_seed42 --modal-b rgbd --imgsz 640 --B 1000 \
    --keluaran "$OUT" > logs-e022-dvd-tukar.txt 2>&1
rc=$?
if [ "$rc" -ne 0 ] || [ ! -s "$OUT" ]; then
  echo "[GAGAL] tukar — rc=$rc, keluaran $OUT tidak ada/kosong  $(date -Is)" >&2
  exit 1
fi
echo "[tukar] ok rc=0 $(date -Is)"
