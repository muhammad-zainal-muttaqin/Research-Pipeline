#!/usr/bin/env bash
# watcher.sh — pengawas kesehatan antrean latihan.
#
# Menjawab kegagalan yang justru paling merepotkan di E-022: run yang MATI
# TANPA SUARA. periksa_run() menangkapnya SETELAH run selesai; watcher ini
# menangkapnya SELAGI berjalan, sehingga slot yang mati tidak dibiarkan kosong
# berjam-jam dan penyebabnya (OOM CUDA, OOM host, proses hilang) tercatat saat
# kejadian, bukan direkonstruksi dari log terpotong.
#
# Yang diawasi tiap siklus:
#   - tekanan VRAM & RAM host
#   - log run aktif untuk penanda OOM/CUDA error
#   - run yang log-nya berhenti tumbuh padahal prosesnya masih ada (hang)
#
# Watcher TIDAK membunuh dan TIDAK me-restart apa pun. Ia hanya mengamati dan
# mencatat: keputusan menjalankan ulang ada di matriks_g2.sh yang memang sudah
# dapat dilanjutkan. Pengawas yang ikut bertindak akan menyulitkan pelacakan
# sebab-akibat, dan itu persis masalah yang sedang kita bereskan.
#
# Pemakaian:
#   bash shell/watcher.sh                 # awasi sampai tak ada latihan aktif
#   INTERVAL=60 bash shell/watcher.sh
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

INTERVAL=${INTERVAL:-60}
STATUS=${STATUS:-status_watcher.txt}
HANG_SIKLUS=${HANG_SIKLUS:-10}    # siklus tanpa pertumbuhan log = dicurigai hang

declare -A ukuran_lama siklus_diam
siklus=0

catat() { echo "[$(date -Is)] $*" | tee -a "$STATUS"; }

catat "watcher mulai (interval ${INTERVAL}s)"

while true; do
  siklus=$((siklus + 1))
  aktif=$(pgrep -cf "train_depth4ch.py|train_rfdetr_4ch.py" || true)

  # Berhenti hanya kalau memang sudah tidak ada latihan DAN bukan siklus awal
  # (memberi jeda agar antrean sempat menyalakan job pertamanya).
  if [ "$aktif" -eq 0 ] && [ "$siklus" -gt 2 ]; then
    catat "tidak ada proses latihan aktif — watcher berhenti"
    break
  fi

  vram=$(nvidia-smi --query-gpu=memory.used,memory.total,utilization.gpu \
         --format=csv,noheader,nounits | tr -d ' ')
  ram_bebas=$(free -g | awk '/^Mem:/ {print $7}')
  catat "siklus $siklus · proses=$aktif · vram=${vram} · ram_bebas=${ram_bebas}G"

  # --- penanda OOM / error CUDA pada log yang sedang ditulis ----------------
  for log in logs-g2-*.txt logs-a4500-*.txt; do
    [ -f "$log" ] || continue
    if grep -qiE "out of memory|CUDA error|CUBLAS_STATUS|device-side assert" "$log"; then
      if ! grep -q "OOM_TERCATAT:$log" "$STATUS" 2>/dev/null; then
        catat "OOM_TERCATAT:$log — $(grep -iom1 -E 'out of memory|CUDA error[^\"]*' "$log")"
      fi
    fi

    # --- deteksi hang: log tidak tumbuh padahal proses masih hidup ----------
    nama=${log#logs-g2-}; nama=${nama%.txt}
    if pgrep -f -- "--name $nama" >/dev/null 2>&1; then
      baru=$(stat -c %s "$log" 2>/dev/null || echo 0)
      if [ "${ukuran_lama[$log]:-0}" -eq "$baru" ]; then
        siklus_diam[$log]=$(( ${siklus_diam[$log]:-0} + 1 ))
        if [ "${siklus_diam[$log]}" -eq "$HANG_SIKLUS" ]; then
          catat "DICURIGAI HANG: $nama — log diam ${HANG_SIKLUS} siklus (~$((HANG_SIKLUS*INTERVAL))s)"
        fi
      else
        siklus_diam[$log]=0
      fi
      ukuran_lama[$log]=$baru
    fi
  done

  sleep "$INTERVAL"
done

catat "watcher selesai"
