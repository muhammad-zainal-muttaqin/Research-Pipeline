# Catatan Teknis E-021 — RF-DETR / RT-DETR / YOLO26 (2026-07-24/25)

Konsolidasi **semua jebakan teknis, keputusan, dan analisis** dari run E-021 agar
tidak perlu diulang. Log mentah di `logs/` (lihat daftar di bawah). Log konsol
di-bersihkan dari spam progress-bar (carriage-return) tetapi isi bermakna utuh.

## Ringkasan hasil (1-protokol pycocotools)

| Model | Param | imgsz | VAL mAP50/50-95 | TEST mAP50/50-95 |
|---|---|---|---|---|
| YOLO26m | 21,9 jt | 640 | 0,5195 / 0,2411 | 0,5165 / 0,2452 |
| YOLO26l | 26,3 jt | 1280 | 0,5270 / 0,2526 | 0,5300 / 0,2568 |
| RT-DETR-L | 33,0 jt | 1280 | 0,5459 / 0,2555 | 0,5784 / 0,2707 |
| **RF-DETR-L** | 35,7 jt | 1280 | **0,5695 / 0,2604** | **0,6038 / 0,2770** |

Ranking = urutan parameter di semua metrik & split. RF-DETR-L test mAP50 0,6038
melewati sasaran 0,60. Sumber: `results/perkelas_pycoco.json` (per-kelas lengkap
di `docs/METRICS.md` §1-protokol).

## Jebakan RF-DETR (rfdetr 1.8.3) — WAJIB tahu sebelum run ulang

1. **Resolusi harus kelipatan 32**, BUKAN 56. Constraint = patch_size(16) ×
   num_windows(2) = 32. Jadi 1280 valid (1280/32=40) dan cocok persis dengan
   RT-DETR. (Awalnya diduga 56 → salah; error: "resolution=1288 is not divisible
   by patch_size (16) * num_windows (2) = 32".)

2. **`multi_scale`/`expanded_scales` default melatih di 1440, BUKAN resolusi yang
   diminta.** Default `multi_scale=True`+`expanded_scales=True`, dan karena
   `do_random_resize_via_padding=False`, ia mengunci ke skala TERBESAR =
   resolusi×45/40 = 1440. **Untuk fairness @1280 WAJIB set
   `multi_scale=False, expanded_scales=False`.** Tanpa ini RF-DETR diam-diam dapat
   keunggulan resolusi. Cek log: baris "Using multi-scale training ... scales:
   [1440]" TIDAK boleh muncul.

3. **Tidak ada `.evaluate()` di rfdetr 1.8.3.** Pakai `run_test=True` di `.train()`
   → metrik test masuk `metrics.csv` (kolom `test/*`). Val dicatat tiap epoch
   (`val/mAP_50`, `val/mAP_50_95`, `val/AP/Bx`, plus varian `val/ema_*`).

4. **Per-kelas `val/AP/Bx` di metrics.csv & evaluation.json = AP50-95, BUKAN AP50.**
   Untuk AP50 per-kelas harus COCO-eval terpisah (`eval_rfdetr_perkelas.py`).

5. **Checkpoint: `run_test` memakai `checkpoint_best_total.pth` untuk test**
   (memberi test 0,5837/0,2653), sedangkan checkpoint terbaik-val = EMA
   (`checkpoint_best_ema.pth`). Eval EMA konsisten val↔test memberi test
   0,6038/0,2770. Val pycocotools EMA (0,5695) cocok dengan evaluator internal
   rf-detr (0,5699) → pipeline tervalidasi. **Pakai EMA konsisten.**

6. **Resume:** `RFDETRLarge(..., resume="runs/.../last.ckpt")` (PTL ckpt_path).
   `train_rfdetr.py --resume` sudah mendukung.

## Jebakan performa GPU (NVIDIA L4, 23 GB, TDP 72 W)

7. **GPU kelaparan data dengan `num_workers` default 2** → util loncat 5%↔100%
   (rata-rata rendah), ~5 jam untuk 60 epoch. Naikkan ke 8. (128 core tersedia,
   tapi lihat #8.)

8. **JANGAN maksimalkan worker/batch membabi-buta.** batch16 × workers32 →
   **`/dev/shm` (26 GB) penuh → DataLoader worker di-SIGKILL** ("DataLoader worker
   (pid …) is killed by signal: Killed"). RAM host 503 GB tak relevan; batasnya
   shared-memory. **Sweet spot: batch 8 / grad-accum 2 (effective 16) / workers 8**
   → shm ~2-3 GB, GPU util ~67-100%, tanpa crash.

9. **L4 power-limited.** Pada beban penuh: util 100%, **power 70/72 W (~97%)**,
   P-State P0. "100% util tapi 70 W" itu NORMAL — L4 memang GPU hemat daya; 70 W =
   sudah mentok. **~10 mnt/epoch adalah lantai** untuk RF-DETR-L @1280 di L4;
   lebih cepat hanya dengan GPU lebih kuat atau resolusi lebih rendah (merusak
   fairness).

## Keputusan fairness (dijaga ketat)

- **Resolusi 1280 identik** untuk RT-DETR & RF-DETR & YOLO26l (YOLO26m 640 = acuan
  ringan, bukan pembanding sekelas).
- **Split identik** 3000/404/588 (E-017), augmentasi aman-warna (hsv kecil, E-019),
  seed 42, dari bobot COCO. `build_rfdetr_ds.py` = adaptor dataset YOLO→RF-DETR via
  symlink (tanpa salin citra).
- **Effective batch 16** untuk RF-DETR; RT-DETR/YOLO26l pakai batch 4 default
  ultralytics (perbedaan batch antar-framework kurang kritis dibanding resolusi).
- **Patience beda tapi adil:** RF-DETR patience 8 (stop ep17), RT-DETR & YOLO26l
  patience 60 (penuh). SEMUA melaporkan checkpoint **terbaik-val** — patience hanya
  soal kapan berhenti melatih, bukan checkpoint mana yang dilaporkan.
- **Baseline YOLO param-adil = YOLO26l** (26,3 jt, config IDENTIK RT-DETR). Tetap
  di bawah kedua DETR → keunggulan DETR **bukan** efek kapasitas/resolusi.
- **Evaluator campur diselesaikan:** semua 4 model dievaluasi ulang lewat
  **1-protokol pycocotools** (`eval_all_pycoco.py`) — perbedaan protokol vs
  ultralytics `.val()` <0,005 (terkonfirmasi silang).

## Peta berkas run ini (di repo)

- **Skrip:** `train_rfdetr.py`, `build_rfdetr_ds.py`, `train_yolo26l.py`,
  `eval_perkelas.py`, `eval_rfdetr_perkelas.py`, `eval_all_pycoco.py`
- **Hasil JSON:** `results/perkelas_fair.json` (native), `results/perkelas_pycoco.json`
  (1-protokol), `results/yolo26l_eval.json`
- **Metadata run:** `runs/rfdetr_l_e60_i1280/{evaluation.json,metrics.csv,training_config.json}`,
  `runs/yolo26l_e60_i1280/{args.yaml,results.csv}` (tanpa bobot — bisa dibuat ulang)
- **Log konsol:** `logs/logs-rfdetr-e60.txt` (training), `logs/logs-rfdetr-smoke.txt`
  (smoke), `logs/logs-rfdetr-install.txt` + `-install2.txt` (instalasi),
  `logs/logs-rfdetr-perkelas.txt` (COCO eval), `logs/logs-yolo26l.txt` (training),
  `logs/logs-pycoco-all.txt` (eval 4-model)
- **Log naratif:** [`docs/EKSPERIMEN.md`](../docs/EKSPERIMEN.md) E-021,
  [`docs/METRICS.md`](../docs/METRICS.md), [`docs/STATUS.md`](../docs/STATUS.md)

Bobot model (.pth/.pt/.ckpt) TIDAK diarsipkan (terlalu besar) — dibuat ulang dari
skrip di atas.
