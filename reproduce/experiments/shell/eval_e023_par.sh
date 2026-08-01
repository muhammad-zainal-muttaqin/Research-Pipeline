#!/usr/bin/env bash
# E-023 — 12 kontras berpasangan, DIJALANKAN PARALEL.
#
# Versi berurutan (eval_e023.sh) memakai mesin ini seperempatnya saja: tiap
# kontras memanggil ProcessPoolExecutor dengan `min(32, cpu_count//4)` = 12
# proses, dan kontras dijalankan satu per satu. Di mesin 48 core hasilnya 36
# core menganggur selama ~36 menit. Rumus //4 itu masuk akal ketika beberapa
# LATIHAN GPU berbagi mesin dan butuh core untuk dataloader-nya; setelah
# latihan selesai, ia hanya menyisakan kapasitas.
#
# Empat kontras x 12 proses = 48, tepat mengisi mesin. Bukan pekerjaan baru:
# 12 kontras yang sama, hanya diselesaikan ~4x lebih cepat.
#
# Kontras yang hasilnya sudah ada DILEWATI, jadi skrip ini aman dijalankan
# ulang setelah gangguan.
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1
export YOLO_CONFIG_DIR=/tmp/Ultralytics

PY=./.venv/bin/python
R=/workspace/research-pipeline/runs/detect/runs_e023
OUT=/workspace/research-pipeline/evidence/experiments/results/E-023
SPLIT_DIR=/workspace/research-pipeline/evidence/experiments/splits_depth/seed42
B=${B:-2000}
PAR=${PAR:-4}
mkdir -p "$OUT"

modal_dari() { case "$1" in derau) echo derau ;; *) echo rgbd ;; esac; }

tunggu_slot() { while [ "$(jobs -rp | wc -l)" -ge "$PAR" ]; do wait -n; done; }

satu() {
  local lengan=$1 seed=$2
  local keluaran="$OUT/paired_${lengan}_vs_rgb_seed${seed}.json"
  echo "=== ${lengan} vs rgb seed${seed} mulai $(date -Is) ==="
  $PY eval/eval_e022_paired.py \
      --rgb "$R/e023_rgb_seed${seed}" --rgbd "$R/e023_${lengan}_seed${seed}" \
      --modal-a rgb --modal-b "$(modal_dari "$lengan")" \
      --split-dir "$SPLIT_DIR" --split test \
      --seed "$seed" --B "$B" --keluaran "$keluaran" \
      > "logs-eval-${lengan}-seed${seed}.txt" 2>&1
  local rc=$?
  if [ "$rc" -eq 0 ] && [ -f "$keluaran" ]; then
    echo "[ok] ${lengan} seed${seed} $(date -Is)"
  else
    echo "[GAGAL] ${lengan} seed${seed} rc=$rc $(date -Is)" >&2
  fi
}

for seed in 42 1337 2024; do
  for lengan in awal mid late derau; do
    keluaran="$OUT/paired_${lengan}_vs_rgb_seed${seed}.json"
    [ -f "$keluaran" ] && { echo "[lewati] ${lengan} seed${seed}"; continue; }
    tunggu_slot
    satu "$lengan" "$seed" &
  done
done
wait

n=$(find "$OUT" -name 'paired_*_vs_rgb_seed*.json' | wc -l)
echo
echo "=== RINGKASAN $(date -Is) — $n/12 kontras ==="
[ "$n" -lt 12 ] && exit 1
echo "12 kontras lengkap"
