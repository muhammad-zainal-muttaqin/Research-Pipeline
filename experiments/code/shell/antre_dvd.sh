#!/usr/bin/env bash
# depth vs derau berpasangan — uji yang mengisolasi KANDUNGAN INFORMASI depth.
# Kedua lengan punya jumlah parameter, statistik masukan, dan perlakuan
# augmentasi identik; yang berbeda hanya isi kanal ke-4 bermakna atau tidak.
set -uo pipefail
cd experiments/code
PY=./.venv/bin/python
R=runs/detect/runs_e022

for pas in "yolo26n:$R/yolo26n_derau_seed42:$R/yolo26n_rgbd_seed42" \
           "rtdetrl:$R/rtdetr-l_derau_seed42:$R/rtdetr-l_rgbd_seed42"; do
  nama=${pas%%:*}; sisa=${pas#*:}; a=${sisa%%:*}; b=${sisa#*:}
  out=results/e022_paired_${nama}_depth_vs_derau.json
  [ -f "$out" ] && { echo "[dvd] $nama sudah ada, lewati"; continue; }
  echo "[dvd] mulai $nama $(date -Is)"
  $PY -u eval_e022_paired.py --rgb "$a" --modal-a derau --rgbd "$b" --modal-b rgbd \
      --imgsz 640 --B 1000 --keluaran "$out" > logs-e022-dvd-$nama.txt 2>&1
  rc=$?
  if [ "$rc" -ne 0 ] || [ ! -s "$out" ]; then
    echo "[GAGAL] dvd $nama — rc=$rc, keluaran $out tidak ada/kosong  $(date -Is)" >&2
    gagal=1
  else
    echo "[dvd] selesai $nama rc=0 $(date -Is)"
  fi
done
if [ "${gagal:-0}" -ne 0 ]; then
  echo "[dvd] SELESAI DENGAN KEGAGALAN — jangan pakai angkanya $(date -Is)" >&2
  exit 1
fi
echo "[dvd] SEMUA SELESAI $(date -Is)"

