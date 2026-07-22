# METRICS — tabel metrik definitif semua run detektor

Rekam lengkap metrik **setiap** run detektor: mAP50, mAP50-95, dan **per-kelas
AP50 B1–B4**, pada val dan test. Semua angka COCO/ultralytics apa adanya. Dibuat
sebelum workspace kerja di-terminate agar tidak ada metrik yang perlu dihitung
ulang.

**Sumber angka** (JSON di `experiments/results/`, kurva per-epoch di
`experiments/runs/<run>/results.csv`):
`baseline_test.json`, `eval_missing.json`, `rtdetr_eval.json`, `diag_bottleneck.json`.

Split per pohon 716/96/141, irisan nol. B1=matang … B4=mentah.

---

## Val (dasar pemilihan konfigurasi)

| Run | Ide/E | imgsz | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|---|---|
| yolo26m baseline | acuan | 640 | 0,5218 | 0,2407 | 0,7354 | 0,4076 | 0,5561 | 0,3881 |
| RGBD 4-kanal | I-4 | 640 | 0,5041 | 0,2378 | 0,7160 | 0,3821 | 0,5336 | 0,3847 |
| 4-kelas aman-warna | E-019 | 1280 | 0,5186 | 0,2358 | 0,7011 | 0,4130 | 0,5682 | 0,3922 |
| **RT-DETR-L** | **I-14** | 1280 | **0,5466** | **0,2543** | 0,7503 | 0,4413 | 0,5808 | 0,4138 |

## Test (dilaporkan; tidak dipakai memilih)

| Run | Ide/E | imgsz | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|---|---|
| DiB publikasi | acuan | 640 | 0,531 | — | 0,739 | 0,433 | 0,599 | 0,354 |
| yolo26m baseline (kami) | acuan | 640 | 0,5161 | 0,2457 | 0,7410 | 0,4016 | 0,5894 | 0,3323 |
| RGBD 4-kanal | I-4 | 640 | 0,5192 | 0,2471 | 0,7509 | 0,4115 | 0,5859 | 0,3283 |
| 4-kelas aman-warna | E-019 | 1280 | 0,5418 | 0,2493 | 0,7546 | 0,4503 | 0,6037 | 0,3585 |
| **RT-DETR-L** | **I-14** | 1280 | **0,5794** | **0,2694** | 0,7891 | 0,4685 | 0,6391 | 0,4208 |

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
  **Detektor terbaik**, unggul keempat kelas kedua split; lihat [SR-013](SR/SR-013-rtdetr-nms-free.md).
- **Kurva per-epoch penuh** (P/R/mAP50/mAP50-95 tiap epoch) ada di
  `experiments/runs/<run>/results.csv` untuk kelima run. Log konsol bersih di
  `experiments/logs/`.

## Diagnostik (bukan hasil model — jangan dikutip sebagai capaian mAP)

Tersimpan di `experiments/results/`: `class_mismatch.json` (E-001),
`diag_bottleneck.json` (E-014, agnostik vs 4-kelas), `loc_ceiling.json` (E-018,
plafon lokalisasi 0,8834/0,4702), `head_vs_crop.json` & `multiview_val.json`
(E-016), `metric_variants.json` & `metric_pm1.json` (E-016, varian perumusan),
`two_stage_val_*.json` (E-017), `raw_map.json` (E-015, peta master 3992/3992).
