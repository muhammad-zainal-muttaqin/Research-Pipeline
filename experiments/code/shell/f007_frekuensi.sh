#!/usr/bin/env bash
# F-007 (K1a) — Cabang frekuensi samping, 4 lengan x 3 seed = 12 run.
#
# Gerbangnya sudah lolos (F-002: dwt_hh +0,0731 pada B4, tiga kali ambang).
#
# Dua dari empat lengan adalah KONTROL WAJIB dan tidak boleh dipangkas:
#   dwt          sub-band Haar frekuensi tinggi        <- yang diusulkan
#   laplacian    |Laplacian| tiga skala                <- pesaing E-011/F-002
#   freq_rendah  sub-band LL             [KONTROL]     <- frekuensi RENDAH
#   fase_diacak  fase diacak di Fourier  [KONTROL]     <- spektrum sama, struktur hancur
#
# Tanpa kedua kontrol, kenaikan signifikan pun tidak membuktikan bahwa
# FREKUENSI penyebabnya — bisa saja sekadar 192.289 parameter tambahan. Ini
# disiplin lengan `derau`/`tukar` yang sama seperti E-027 dan E-032.
# Uji sambungan sudah membuktikan keempat lengan berparameter IDENTIK.
#
# BERURUTAN. VRAM puncak 10.331 MiB dari 20.470 (F-001); dua run serentak = OOM.
# Perkiraan ~3 jam per run -> ~36 jam total. Urutan seed di dalam lengan supaya
# bila anggaran habis di tengah, tiap lengan tetap punya seed 42 lebih dulu.
#
# MODE PERIKSA: `bash shell/f007_frekuensi.sh --periksa` hanya memvalidasi
# prasyarat lalu keluar TANPA melatih apa pun. Wajib ada karena menjalankan
# skrip ini "sekadar untuk melihat" pernah menyalakan run sungguhan di atas
# latihan yang sedang berjalan — dua run RF-DETR-L serentak = OOM (F-001 §5.4).
set -euo pipefail

PERIKSA=0
[ "${1:-}" = "--periksa" ] && PERIKSA=1

cd "$(dirname "$0")/.."
PY=.venv/bin/python
RUNS=../../runs/detect/runs_f007
HASIL=results/F-007
mkdir -p "$RUNS" "$HASIL"

# Penjaga GPU: menolak start bila sudah ada latihan lain berjalan. Anggaran
# VRAM saja tidak cukup — yang menyebabkan bahaya adalah run KEDUA, bukan
# ukuran run pertama.
if [ "$PERIKSA" = "0" ] && pgrep -f "train_rfdetr" | grep -qv "^$$\$"; then
  if pgrep -af "train_rfdetr" | grep -qv "f007_frekuensi"; then
    echo "[F-007] TOLAK: sudah ada proses train_rfdetr* berjalan."
    pgrep -af "train_rfdetr" | grep -v "bash -c" | head -3
    echo "        Dua run RF-DETR-L serentak = 20.662 MiB > 20.470 MiB (OOM)."
    echo "        Tunggu run itu selesai, atau jalankan dengan --periksa untuk validasi saja."
    exit 1
  fi
fi

# Prasyarat: uji sambungan tiap lengan harus LULUS sebelum runnya diantre.
for L in dwt laplacian freq_rendah fase_diacak; do
  U="$HASIL/uji_sambungan_${L}.json"
  if ! grep -q '"PUTUSAN": "LULUS"' "$U" 2>/dev/null; then
    echo "[F-007] uji sambungan $L BELUM LULUS ($U) — jalankan dulu:"
    echo "        $PY train/train_rfdetr_freq.py --uji-sambungan --lengan $L"
    exit 1
  fi
done
echo "[F-007] uji sambungan keempat lengan LULUS"

if [ "$PERIKSA" = "1" ]; then
  echo "[F-007] mode --periksa: prasyarat lengkap, TIDAK ada yang dilatih."
  exit 0
fi

for SEED in 42 1337 2024; do
  for L in dwt laplacian freq_rendah fase_diacak; do
    OUT="$RUNS/${L}_seed${SEED}"
    TANDA="$OUT/.selesai"
    if [ -f "$TANDA" ]; then
      echo "[F-007] $L seed $SEED sudah selesai, dilewati"
      continue
    fi
    echo "[F-007] === $L seed $SEED mulai $(date -Is) ==="
    $PY train/train_rfdetr_freq.py \
        --lengan "$L" \
        --dataset rfdetr_ds \
        --output "$OUT" \
        --epochs 60 --resolution 1280 --batch 8 --grad-accum 2 --workers 8 \
        --seed "$SEED" \
        2>&1 | tee "logs-f007-${L}-seed${SEED}.txt"

    $PY eval/dump_logits_rfdetr.py \
        --ckpt "$OUT/checkpoint_best_ema.pth" --split test --resolution 1280 \
        --keluaran "$HASIL/logits_test_${L}_seed${SEED}.npz" \
        2>&1 | tee "logs-f007-dump-${L}-seed${SEED}.txt"

    sha256sum "$OUT"/checkpoint_best_*.pth > "$HASIL/sha256_${L}_seed${SEED}.txt" || true
    cp "$OUT/evaluation.json" "$HASIL/evaluation_${L}_seed${SEED}.json" 2>/dev/null || true
    touch "$TANDA"
    echo "[F-007] === $L seed $SEED selesai $(date -Is) ==="
  done
done

echo "[F-007] seluruh lengan x seed selesai $(date -Is)"
echo "[F-007] langkah berikut: kontras berpasangan terhadap baseline F-004"
echo "  for L in dwt laplacian freq_rendah fase_diacak; do for S in 42 1337 2024; do"
echo "    $PY eval/bootstrap_pohon.py --npz-a $HASIL/../F-004/logits_test_seed\$S.npz \\"
echo "        --npz-b $HASIL/logits_test_\${L}_seed\$S.npz --label-a baseline --label-b \$L \\"
echo "        --keluaran $HASIL/kontras_\${L}_seed\$S.json; done; done"
