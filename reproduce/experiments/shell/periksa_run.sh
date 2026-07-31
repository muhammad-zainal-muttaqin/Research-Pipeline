#!/usr/bin/env bash
# periksa_run.sh — penjaga kelengkapan run, di-source oleh skrip antrean.
#
# Latar: AUDIT-E022 mencatat tiga run yang mati di tengah tetapi dilaporkan
# "SELESAI", sehingga antrean melanjut tanpa peringatan dan angkanya sempat
# ikut masuk ringkasan. Penyebabnya dua hal terpisah:
#
#   1. `echo "[$(date)] rc=$?"` membaca status `date`, bukan status latihan,
#      karena substitusi perintah dieksekusi lebih dulu dan me-reset $?.
#      Pola di repo ini sudah aman (rc=$? selalu mendahului $(date)), tetapi
#      helper ini tetap menuntut rc ditangkap ke variabel lebih dulu.
#   2. Proses yang mati tanpa kode keluar bukan-nol (mis. dibunuh OOM killer)
#      tetap lolos butir 1. Karena itu kelengkapan diperiksa dari ARTEFAKNYA:
#      jumlah epoch yang benar-benar tercatat di results.csv / metrics.csv.
#
# Pemakaian:
#
#   source "$(dirname "$0")/periksa_run.sh"
#
#   $PY train_depth4ch.py ... > "$log" 2>&1
#   rc=$?                                   # WAJIB baris tersendiri
#   periksa_run "$rc" "$dir/results.csv" 60 "rtdetr-l rgbd seed42" || gagal=1
#
# Kolom pertama results.csv (ultralytics) dan metrics.csv (rfdetr) sama-sama
# `epoch`, jadi satu penghitung melayani keduanya. rfdetr menulis beberapa
# baris per epoch (per step), sehingga yang dihitung adalah epoch UNIK.
#
# Bila run memang boleh berhenti dini (early stopping aktif), berikan batas
# minimum yang masuk akal atau 0 untuk melewati pemeriksaan epoch.

periksa_run() {
  local rc=$1 csv=$2 harap=$3 nama=$4
  local pesan="" n

  [ "$rc" -ne 0 ] && pesan="rc=$rc"

  if [ ! -f "$csv" ]; then
    pesan="${pesan:+$pesan; }tidak ada $csv"
  elif [ "$harap" -gt 0 ]; then
    n=$(awk -F, 'NR>1 && $1 != "" {e[$1]=1} END {print length(e)+0}' "$csv")
    [ "$n" -lt "$harap" ] && pesan="${pesan:+$pesan; }epoch tercatat $n/$harap"
  fi

  if [ -n "$pesan" ]; then
    echo "[GAGAL] $nama — $pesan  $(date -Is)" >&2
    return 1
  fi
  echo "[ok] $nama — rc=0, artefak lengkap  $(date -Is)"
  return 0
}
