#!/usr/bin/env bash
# F-004 — Baseline RF-DETR-L 3 seed pada SawitMVC (jalur RGB).
#
# Resep dikunci PERSIS ke training_config.json E-021 (resolusi 1280, batch 8,
# grad-accum 2, workers 8, epochs 60, early stopping patience 8 min-delta 0,001,
# EMA, multi_scale/expanded_scales dimatikan). Yang berbeda dari E-021 hanya:
#   - tiga seed, bukan satu  -> memberi varians seed jalur RGB yang sampai kini
#     NOL TERUKUR pada RF-DETR (ambang +0,05 seri F bergantung pada angka ini)
#   - logit mentah per query di-dump  -> masukan wajib F-005 (P1)
#
# BERURUTAN, bukan paralel. VRAM puncak terukur F-001 = 9.853 MiB dari 20.470;
# dua run serentak = 19.706 MiB (96%), yaitu persis jebakan OOM yang dicatat
# CLAUDE.md ("3 x 6,6 = 19,7 dari 19,7"). Jangan diparalelkan.
#
# Perkiraan: ~9,2 menit/epoch (terukur F-001 di RTX A4500), berhenti sekitar
# epoch 18 seperti E-021 -> ~3 jam per seed, ~9 jam total.
set -euo pipefail

cd "$(dirname "$0")/.."
PY=.venv/bin/python
RUNS=../../runs/detect/runs_f004
HASIL=results/F-004
mkdir -p "$RUNS" "$HASIL"

for SEED in 42 1337 2024; do
  OUT="$RUNS/rfdetrl_rgb_seed${SEED}"
  TANDA="$OUT/.selesai"
  if [ -f "$TANDA" ]; then
    echo "[F-004] seed $SEED sudah selesai, dilewati"
    continue
  fi
  echo "[F-004] === seed $SEED mulai $(date -Is) ==="
  $PY train/train_rfdetr.py \
      --dataset rfdetr_ds \
      --output "$OUT" \
      --epochs 60 \
      --resolution 1280 \
      --batch 8 \
      --grad-accum 2 \
      --workers 8 \
      --seed "$SEED" \
      2>&1 | tee "logs-f004-seed${SEED}.txt"

  # Logit mentah per query, split test -> masukan F-005 (P1).
  $PY eval/dump_logits_rfdetr.py \
      --ckpt "$OUT/checkpoint_best_ema.pth" \
      --split test \
      --resolution 1280 \
      --keluaran "$HASIL/logits_test_seed${SEED}.npz" \
      2>&1 | tee "logs-f004-dump-seed${SEED}.txt"

  # Bobot tidak diarsipkan (kebijakan repo), tetapi hash-nya dicatat supaya
  # latih-ulang dapat dibedakan dari "resep tidak tereproduksi" -- pelajaran
  # yang sama seperti metrics_lengkap.json E-022.
  sha256sum "$OUT"/checkpoint_best_*.pth > "$HASIL/sha256_seed${SEED}.txt" || true
  cp "$OUT/evaluation.json" "$HASIL/evaluation_seed${SEED}.json"
  cp "$OUT/metrics.csv" "$HASIL/metrics_seed${SEED}.csv"
  touch "$TANDA"
  echo "[F-004] === seed $SEED selesai $(date -Is) ==="
done

echo "[F-004] seluruh seed selesai $(date -Is)"
