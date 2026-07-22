#!/usr/bin/env bash
set -u
cd /workspace/experiments
PY=.venv/bin/python
DET=runs/agn_e25_i960_s42/weights/best.pt
CLS=runs/maturity_raw/best.pt
while [ ! -f runs/maturity_raw/hasil.json ]; do sleep 15; done
echo "[$(date +%H:%M:%S)] v2 selesai, mulai evaluasi akhir"
echo "--- A. val: dua-tahap polos (tanpa TTA, satu pengklasifikasi) ---"
$PY two_stage.py --det $DET --cls $CLS --split val --crop-source raw --tag _A
echo "--- B. val: + TTA ---"
$PY two_stage.py --det $DET --cls $CLS --split val --crop-source raw --tta --tag _B
echo "--- C. val: + TTA + gabungan v1(MVC-res)+v2(master-res) ---"
$PY two_stage.py --det $DET --cls runs/maturity/best.pt,$CLS --split val --crop-source raw --tta --tag _C
echo "[$(date +%H:%M:%S)] EVALUASI VAL SELESAI"
