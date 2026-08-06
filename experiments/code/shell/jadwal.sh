#!/usr/bin/env bash
# Pustaka penjadwalan run — memperbaiki tiga bug yang terverifikasi 1 Agustus.
#
# Sumberkan, jangan jalankan:  source shell/jadwal.sh
#
# ## Bug 1 — peluncuran ganda
#
# Pola lama menjaga dengan "lewati bila berkas hasil sudah ada". Itu tidak
# melindungi apa pun SELAMA pekerjaan berjalan, karena hasil baru ditulis di
# akhir. Nyatanya driver E-023 meluncurkan salinan kedua `awal_seed2024` 20
# menit setelah yang pertama mulai; keduanya menulis ke berkas yang sama.
#
# Perbaikannya kunci berbasis proses: `flock` non-blocking pada berkas penanda,
# diambil saat MULAI dan dilepas otomatis oleh kernel saat proses mati — termasuk
# saat mati karena SIGKILL, sehingga kunci tidak pernah tertinggal basi.
#
# ## Bug 2 — pekerja yatim
#
# Membunuh induk TIDAK membunuh 12 pekerja ProcessPoolExecutor-nya; mereka
# berpindah ke ppid 1 dan terus membakar CPU. Perbaikannya menjalankan tiap run
# di grup proses sendiri (`setsid`) lalu membunuh seluruh grup (`kill -TERM --`
# dengan PID negatif), bukan satu pid.
#
# ## Bug 3 — ambang VRAM berbasis peluncuran
#
# Run yolo26n tumbuh 2,35 -> 4,04 GB selama latihan. Ambang yang mengukur
# pemakaian SAAT PELUNCURAN menyebabkan dua OOM pada 1 Agustus. Ambang di sini
# wajib puncak-plus-margin, dan `tunggu_vram` menolak angka yang mencurigakan
# rendah supaya kesalahan yang sama tidak terulang diam-diam.
set -uo pipefail

JADWAL_KUNCI_DIR=${JADWAL_KUNCI_DIR:-/tmp/jadwal-kunci}
mkdir -p "$JADWAL_KUNCI_DIR"

# --- kunci ----------------------------------------------------------------
# ambil_kunci <nama>
#   rc 0 = kunci didapat (fd tetap terbuka selama proses hidup)
#   rc 1 = pekerjaan dengan nama sama SEDANG berjalan
ambil_kunci() {
  local nama=$1 fd
  exec {fd}>"$JADWAL_KUNCI_DIR/$nama.lock" || return 2
  if flock -n "$fd"; then
    printf '%s' "$fd" > "$JADWAL_KUNCI_DIR/$nama.fd"
    return 0
  fi
  exec {fd}>&-
  return 1
}

# --- VRAM -----------------------------------------------------------------
# tunggu_vram <ambang_mib> [jeda_detik]
#
# Ambang WAJIB puncak-plus-margin, bukan pemakaian saat peluncuran. Nilai di
# bawah 4500 MiB ditolak: puncak terukur yolo26n saja 4,04 GB, jadi angka lebih
# rendah hampir pasti berarti seseorang mengukur di saat yang salah.
tunggu_vram() {
  local ambang=$1 jeda=${2:-30} bebas
  if [ "$ambang" -lt 4500 ]; then
    echo "[jadwal] TOLAK ambang ${ambang} MiB — di bawah puncak terukur yolo26n (4,04 GB)." >&2
    echo "[jadwal] Ambang harus puncak + margin, bukan pemakaian saat peluncuran." >&2
    return 2
  fi
  while true; do
    bebas=$(nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits)
    [ "$bebas" -ge "$ambang" ] && { echo "$bebas"; return 0; }
    sleep "$jeda"
  done
}

# --- peluncuran & penghentian --------------------------------------------
# luncurkan <nama> <perintah...>
#   Menjalankan perintah di grup proses sendiri. Mencetak PGID ke stdout.
luncurkan() {
  local nama=$1; shift
  setsid "$@" &
  local pid=$!
  echo "$pid" > "$JADWAL_KUNCI_DIR/$nama.pgid"
  echo "$pid"
}

# hentikan <nama> [sinyal]
#   Membunuh SELURUH grup proses, bukan hanya induknya. Tanpa ini, pekerja
#   ProcessPoolExecutor menjadi yatim dan terus berjalan.
hentikan() {
  local nama=$1 sinyal=${2:-TERM}
  local f="$JADWAL_KUNCI_DIR/$nama.pgid"
  [ -f "$f" ] || { echo "[jadwal] tidak ada pgid untuk $nama" >&2; return 1; }
  local pgid; pgid=$(cat "$f")
  kill -"$sinyal" -- "-$pgid" 2>/dev/null
  return 0
}

# --- pemeriksaan mandiri --------------------------------------------------
# Jalankan langsung untuk memverifikasi ketiga perbaikan:  bash shell/jadwal.sh
_periksa_mandiri() {
  local gagal=0
  export JADWAL_KUNCI_DIR=/tmp/jadwal-uji-$$
  mkdir -p "$JADWAL_KUNCI_DIR"

  # 1. kunci menolak peluncuran kedua dengan nama sama
  ( ambil_kunci uji && sleep 3 ) &
  sleep 0.5
  if ambil_kunci uji 2>/dev/null; then
    echo "GAGAL: kunci kedua berhasil diambil padahal yang pertama masih hidup"; gagal=1
  else
    echo "ok  kunci menolak peluncuran ganda"
  fi
  wait

  # 2. kunci dilepas setelah pemegangnya mati
  if ambil_kunci uji; then echo "ok  kunci dilepas setelah proses selesai"
  else echo "GAGAL: kunci tertinggal basi"; gagal=1; fi

  # 3. ambang VRAM rendah ditolak
  if tunggu_vram 3400 2>/dev/null; then
    echo "GAGAL: ambang 3400 MiB diterima — inilah yang menyebabkan OOM"; gagal=1
  else
    echo "ok  ambang di bawah puncak terukur ditolak"
  fi

  # 4. hentikan membunuh anak, bukan cuma induk
  luncurkan uji2 bash -c 'sleep 30 & sleep 30 & wait' >/dev/null
  sleep 0.5
  local pgid; pgid=$(cat "$JADWAL_KUNCI_DIR/uji2.pgid")
  local sebelum; sebelum=$(pgrep -g "$pgid" 2>/dev/null | wc -l)
  hentikan uji2 KILL; sleep 0.5
  local sesudah; sesudah=$(pgrep -g "$pgid" 2>/dev/null | wc -l)
  if [ "$sebelum" -ge 2 ] && [ "$sesudah" -eq 0 ]; then
    echo "ok  seluruh grup proses mati ($sebelum -> 0), tidak ada yatim"
  else
    echo "GAGAL: $sebelum proses sebelum, $sesudah sesudah — ada yang yatim"; gagal=1
  fi

  rm -rf "$JADWAL_KUNCI_DIR"
  [ "$gagal" -eq 0 ] && echo "SEMUA PEMERIKSAAN LULUS" || echo "ADA YANG GAGAL"
  return "$gagal"
}

[ "${BASH_SOURCE[0]}" = "$0" ] && _periksa_mandiri
