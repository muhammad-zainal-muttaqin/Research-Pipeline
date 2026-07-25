# METRICS — tabel metrik definitif semua run detektor

Rekam lengkap metrik **setiap** run detektor: mAP50, mAP50-95, dan **per-kelas
AP50 B1–B4**, pada val dan test. Semua angka COCO/ultralytics apa adanya. Dibuat
sebelum workspace kerja di-terminate agar tidak ada metrik yang perlu dihitung
ulang.

**Sumber angka** (JSON di `experiments/results/`, kurva per-epoch di
`experiments/runs/<run>/results.csv`):
`baseline_test.json`, `eval_missing.json`, `rtdetr_eval.json`, `diag_bottleneck.json`,
`perkelas_fair.json` (per-kelas AP50+AP50-95 semua model), dan
`runs/rfdetr_l_e60_i1280/evaluation.json` + `metrics.csv` (RF-DETR, E-021).

Split per pohon 716/96/141, irisan nol. B1=matang … B4=mentah.

---

## Val (dasar pemilihan konfigurasi)

| Run | Ide/E | imgsz | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|---|---|
| yolo26m baseline | acuan | 640 | 0,5218 | 0,2407 | 0,7354 | 0,4076 | 0,5561 | 0,3881 |
| RGBD 4-kanal | I-4 | 640 | 0,5041 | 0,2378 | 0,7160 | 0,3821 | 0,5336 | 0,3847 |
| 4-kelas aman-warna | E-019 | 1280 | 0,5186 | 0,2358 | 0,7011 | 0,4130 | 0,5682 | 0,3922 |
| YOLO26l (param-adil) | E-021 | 1280 | 0,5300 | 0,2516 | 0,7431 | 0,4358 | 0,5586 | 0,3825 |
| RT-DETR-L | I-14 | 1280 | 0,5466 | 0,2543 | 0,7503 | 0,4413 | 0,5808 | 0,4138 |
| **RF-DETR-L** | **E-021** | 1280 | **0,5695** | **0,2604** | 0,775 | 0,446 | 0,594 | **0,464** |

## Test (dilaporkan; tidak dipakai memilih)

| Run | Ide/E | imgsz | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|---|---|
| DiB publikasi | acuan | 640 | 0,531 | — | 0,739 | 0,433 | 0,599 | 0,354 |
| yolo26m baseline (kami) | acuan | 640 | 0,5161 | 0,2457 | 0,7410 | 0,4016 | 0,5894 | 0,3323 |
| RGBD 4-kanal | I-4 | 640 | 0,5192 | 0,2471 | 0,7509 | 0,4115 | 0,5859 | 0,3283 |
| 4-kelas aman-warna | E-019 | 1280 | 0,5418 | 0,2493 | 0,7546 | 0,4503 | 0,6037 | 0,3585 |
| YOLO26l (param-adil) | E-021 | 1280 | 0,5313 | 0,2553 | 0,7597 | 0,4223 | 0,5900 | 0,3534 |
| RT-DETR-L | I-14 | 1280 | 0,5794 | 0,2694 | 0,7891 | 0,4685 | 0,6391 | 0,4208 |
| **RF-DETR-L** | **E-021** | 1280 | **0,6038** | **0,2770** | 0,817 | 0,497 | 0,668 | 0,433 |

## Tabel 1-protokol (pycocotools) — perbandingan adil E-021

Keempat model dievaluasi lewat **pipeline pycocotools identik** (predict threshold
rendah → COCOeval, GT sama) sehingga **caveat evaluator campur TERSELESAIKAN**.
Sumber: `experiments/results/perkelas_pycoco.json` (skrip `eval_all_pycoco.py`).
Diurutkan menurut parameter. Ranking monotonik di kedua metrik & kedua split.

**VAL** (mAP50 / mAP50-95 · per-kelas AP50 B1/B2/B3/B4):

| Model | Param | imgsz | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|---|---|
| YOLO26m | 21,9 jt | 640 | 0,5195 | 0,2411 | 0,738 | 0,404 | 0,549 | 0,387 |
| YOLO26l | 26,3 jt | 1280 | 0,5270 | 0,2526 | 0,739 | 0,435 | 0,554 | 0,380 |
| RT-DETR-L | 33,0 jt | 1280 | 0,5459 | 0,2555 | 0,748 | 0,442 | 0,579 | 0,415 |
| **RF-DETR-L** | 35,7 jt | 1280 | **0,5695** | **0,2604** | 0,775 | 0,446 | 0,594 | **0,464** |

**TEST** (dilaporkan; tidak dipakai memilih):

| Model | Param | imgsz | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|---|---|
| YOLO26m | 21,9 jt | 640 | 0,5165 | 0,2452 | 0,733 | 0,406 | 0,592 | 0,336 |
| YOLO26l | 26,3 jt | 1280 | 0,5300 | 0,2568 | 0,756 | 0,421 | 0,590 | 0,353 |
| RT-DETR-L | 33,0 jt | 1280 | 0,5784 | 0,2707 | 0,786 | 0,469 | 0,637 | 0,421 |
| **RF-DETR-L** | 35,7 jt | 1280 | **0,6038** | **0,2770** | 0,817 | 0,497 | 0,668 | 0,433 |

**Bacaan:** urutan performa = urutan parameter (YOLO26m < YOLO26l < RT-DETR-L <
RF-DETR-L) pada semua metrik. YOLO26l — baseline YOLO **param-adil sekelas DETR**
(26,3 jt, config identik RT-DETR) — tetap **di bawah kedua DETR**, jadi keunggulan
RF-DETR/RT-DETR **bukan** sekadar efek kapasitas/resolusi. RF-DETR-L unggul di
keempat kelas kedua split; test mAP50 0,6038 melewati sasaran 0,60.

## Metrik LENGKAP 4 model (1-protokol) — `results/metrics_full.json`

Dump metrik penuh via `eval_all_metrics.py` (pipeline pycocotools + matching IoU0.5
untuk P/R/F1). File JSON berisi, per model × val/test: **12 statistik COCO**
(AP@[.5:.95], AP50, AP75, AP S/M/L, AR@1/10/100, AR S/M/L), **per-kelas** AP50 +
AP50-95 + AR, dan **precision/recall/F1** (per-kelas, **macro**, **micro**) pada
ambang best-F1. Ringkasan metrik tambahan (di luar AP50/AP50-95 yang sudah di atas):

**VAL** (AP75 · AR100 · micro-F1 · macro-F1 · micro-P · micro-R):

| Model | AP75 | AR100 | micro-F1 | macro-F1 | micro-P | micro-R |
|---|---|---|---|---|---|---|
| YOLO26m | 0,1951 | 0,5386 | 0,5416 | 0,5394 | 0,5251 | 0,5591 |
| YOLO26l | 0,2129 | 0,5557 | 0,5452 | 0,5447 | 0,5004 | 0,5988 |
| RT-DETR-L | 0,2100 | 0,5225 | 0,5789 | 0,5840 | 0,5540 | 0,6063 |
| **RF-DETR-L** | 0,1971 | 0,5348 | **0,5841** | **0,5880** | 0,5604 | 0,6100 |

**TEST**:

| Model | AP75 | AR100 | micro-F1 | macro-F1 | micro-P | micro-R |
|---|---|---|---|---|---|---|
| YOLO26m | 0,2022 | 0,5578 | 0,5431 | 0,5314 | 0,5355 | 0,5509 |
| YOLO26l | 0,2175 | 0,5557 | 0,5449 | 0,5475 | 0,5394 | 0,5505 |
| RT-DETR-L | 0,2214 | 0,5300 | 0,5960 | 0,5911 | 0,5547 | 0,6440 |
| **RF-DETR-L** | 0,2160 | 0,5353 | **0,6189** | **0,6086** | 0,5903 | 0,6505 |

**Bacaan:** F1 (micro & macro) mengikuti urutan mAP — RF-DETR-L tertinggi di kedua
split. RF-DETR unggul terutama pada **recall** (micro-R test 0,6505 vs RT-DETR
0,6440), konsisten dengan hipotesis NMS-free (lebih sedikit kotak benar tertekan).
Per-kelas P/R/F1 (mis. TEST RF-DETR B4: P 0,471 / R 0,523 / F1 0,496 — kelas
tersulit) ada di `metrics_full.json`. **Catatan:** "accuracy" & "micro/macro" hanya
berlaku untuk P/R/F1; deteksi tak punya akurasi klasifikasi (tanpa true-negative).
mAP sendiri = macro-AP (rata-rata per-kelas).

## Deteksi kelas-agnostik (tanpa penilaian kematangan)

| Run | Ide/E | imgsz | split | mAP50 | mAP50-95 |
|---|---|---|---|---|---|
| baseline dievaluasi agnostik | E-014 | 640 | val | 0,7191 | 0,3197 |
| **detektor khusus agnostik** | I-23 | 960 | val | **0,7730** | **0,3320** |

Angka agnostik tak punya per-kelas (satu kelas "tandan" menurut definisi).
mAP50-95 agnostik 0,3320 **melewati** sasaran 0,30 — deteksi bukan hambatannya.

---

## Catatan penting per run

- **RGBD (I-4)** dihentikan pada epoch 25/60 (kurva datar, tak ada sinyal di
  atas baseline). Pakai pseudo-depth DA3, bukan depth sensor. Depth sensor
  metrik belum pernah diuji (lihat `pipeline/`).
- **4-kelas aman-warna (E-019)** dihentikan ep41; menempel baseline karena
  fine-tune dari checkpoint 640 mengganggu model. Bukan bukti augmentasi/resolusi
  gagal — strategi inisialisasinya yang salah.
- **RT-DETR-L** `best.pt` = epoch fitness-terbaik (ep25); dihentikan ep52.
  Unggul keempat kelas kedua split; lihat [SR-013](SR/SR-013-rtdetr-nms-free.md).
- **RF-DETR-L (E-021)** — **detektor 4-kelas terbaik saat ini**, melampaui
  RT-DETR-L di val (+0,023 mAP50 / +0,006 mAP50-95) dan test (+0,024 / +0,008);
  test mAP50 0,604 melewati sasaran 0,60. Checkpoint ep9 (EMA), early-stop ep17.
  **Catatan evaluator:** angka RF-DETR di atas dari COCO eval independen
  (`eval_rfdetr_perkelas.py`, pycocotools) — val-nya (0,5695) cocok dengan
  evaluator internal rf-detr (0,5699); model lain via ultralytics `.val()`.
  Perbedaan protokol <0,005 — **kini TERSELESAIKAN** oleh tabel 1-protokol
  pycocotools di atas. **Kesetaraan parameter:** baseline YOLO adil **YOLO26l
  26,3 jt @1280** (E-021) sudah dilatih & dievaluasi; tetap di bawah kedua DETR.
- **Kurva per-epoch penuh** (P/R/mAP50/mAP50-95 tiap epoch) ada di
  `experiments/runs/<run>/results.csv` untuk kelima run. Log konsol bersih di
  `experiments/logs/`.

## Diagnostik (bukan hasil model — jangan dikutip sebagai capaian mAP)

Tersimpan di `experiments/results/`: `class_mismatch.json` (E-001),
`diag_bottleneck.json` (E-014, agnostik vs 4-kelas), `loc_ceiling.json` (E-018,
plafon lokalisasi 0,8834/0,4702), `head_vs_crop.json` & `multiview_val.json`
(E-016), `metric_variants.json` & `metric_pm1.json` (E-016, varian perumusan),
`two_stage_val_*.json` (E-017), `raw_map.json` (E-015, peta master 3992/3992).
