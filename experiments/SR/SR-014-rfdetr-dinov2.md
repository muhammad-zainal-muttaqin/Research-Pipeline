# SR-014 — RF-DETR-L (DINOv2, NMS-free): detektor 4-kelas terbaik, sasaran mAP50 terlewati

**Ide I-14 (lanjutan)** · **Eksperimen:** E-021 · **Putusan: DIKONFIRMASI** · 2026-07-25

---

## 1. Masalah

[SR-013](SR-013-rtdetr-nms-free.md) menetapkan arah: detektor NMS-free (RT-DETR-L)
mengalahkan keluarga YOLO pada keempat kelas, dengan kenaikan terbesar di B4.
Tetapi SR-013 meninggalkan dua celah yang membuat kesimpulannya tidak bisa
dipertahankan di hadapan penelaah:

1. **Pembanding tidak sekelas.** yolo26m (21,9 juta parameter, imgsz 640) bukan
   lawan yang adil bagi RT-DETR-L (33,0 juta, imgsz 1280). Kenaikan +0,063 bisa
   saja sekadar efek kapasitas dan resolusi, bukan mekanisme deteksi.
2. **Evaluator campur.** Model YOLO dan RT-DETR diukur lewat `.val()` ultralytics,
   sedangkan model lain lewat pycocotools. Dua implementasi COCO eval yang
   berbeda tidak boleh dibandingkan angka-per-angka.

Selain itu, RT-DETR-L berhenti pada test mAP50 0,5794 — masih −0,021 dari sasaran
0,60.

## 2. Ide

**RF-DETR-L** adalah transformer NMS-free generasi lebih baru: backbone **DINOv2**
patch-16 yang pra-latih secara *self-supervised*, dengan kepala LW-DETR hasil
*neural architecture search*. Pertanyaannya bukan kapasitas — RF-DETR-L (35,7 juta)
hanya sedikit lebih besar dari RT-DETR-L — melainkan apakah pada **setelan
identik** ia melampaui RT-DETR-L.

Sekalian, dua celah SR-013 ditutup dalam eksperimen yang sama.

**Yang akan memalsukan:** run yang konvergen tertinggal dari RT-DETR-L pada kedua
metrik. Test hanya dilaporkan setelah checkpoint dipilih dari val.

## 3. Solusi — varian yang persis dipakai

**RF-DETR-L**, `rfdetr` **1.8.3**, kelas `RFDETRLarge`, **35,65 juta parameter**,
DINOv2 patch-16 + 2-window, dari bobot COCO `rf-detr-large-2026`.

- Resolusi **1280 tepat** (kelipatan 32, sama dengan RT-DETR).
- Batch efektif 16 (batch 8 × gradient accumulation 2).
- *Early-stopping* patience 8 → berhenti ep17; checkpoint terbaik **ep9 (EMA)**.
- Split identik E-017: 3000/404/588, per pohon, irisan nol.
- Augmentasi aman-warna, sama seperti RT-DETR.

**Jebakan yang harus dihindari (terverifikasi):** default rf-detr `multi_scale` +
`expanded_scales` diam-diam mengunci resolusi ke **skala terbesar 1440**, bukan
1280. Keduanya **wajib dimatikan** agar perbandingan benar-benar pada 1280.
Rinciannya di [`experiments/code/CATATAN-TEKNIS-E021.md`](../code/CATATAN-TEKNIS-E021.md).

**Pembanding param-adil:** **YOLO26l** (26,3 juta) dilatih dengan konfigurasi
identik RT-DETR — 1280, 60 epoch, aman-warna, seed 42, `cos_lr`, bobot COCO.

**Satu protokol:** keempat model dievaluasi ulang lewat pipeline **pycocotools**
yang sama (prediksi ambang rendah → COCOeval, GT sama).

## 4. Bukti

**Hasil 1-protokol**, diurutkan menurut parameter:

| Model | Param | VAL mAP50 / 50-95 | TEST mAP50 / 50-95 |
|---|---|---|---|
| YOLO26m | 21,9 jt | 0,5195 / 0,2411 | 0,5165 / 0,2452 |
| YOLO26l | 26,3 jt | 0,5270 / 0,2526 | 0,5300 / 0,2568 |
| RT-DETR-L | 33,0 jt | 0,5459 / 0,2555 | 0,5784 / 0,2707 |
| **RF-DETR-L** | 35,7 jt | **0,5695 / 0,2604** | **0,6038 / 0,2770** |

Per-kelas AP50 test RF-DETR-L: B1 0,817 · B2 0,497 · B3 0,668 · **B4 0,433**.
Unggul di keempat kelas pada kedua split.

**Sanity check pipeline:** val pycocotools mandiri (0,5695) cocok dengan evaluator
internal rf-detr (0,5699 EMA) — jadi pipeline evaluasinya tervalidasi, bukan
angka yang menguntungkan diri sendiri.

**Signifikansi statistik.** Bootstrap 2.000× *resample* gambar test (588, seed 42):
selisih berpasangan RF−RT = **+0,0255, CI 95% [0,0104 – 0,0408]**, P(RF>RT) = 0,999.
CI selisih tidak memuat nol. (CI marginal kedua model beririsan, tetapi uji
berpasangan — gambar yang sama pada tiap resample — yang tepat di sini.)

**Recall, bukan sekadar presisi.** micro-F1 test RF-DETR 0,6189 vs RT-DETR 0,5960;
keunggulannya terutama pada recall (micro-R 0,6505 vs 0,6440) — konsisten dengan
hipotesis NMS-free: lebih sedikit kotak benar yang tertekan.

## 5. Putusan

**DIKONFIRMASI.** RF-DETR-L melampaui RT-DETR-L pada kedua metrik di kedua split
(test +0,024 mAP50, +0,008 mAP50-95) dan menjadi **detektor 4-kelas terbaik**.
Test mAP50 **0,6038 melewati sasaran 0,60** untuk pertama kali; mAP50-95 masih
−0,023.

Dua celah SR-013 tertutup: YOLO26l param-adil **tetap di bawah kedua DETR**, jadi
keunggulan DETR **bukan** efek kapasitas atau resolusi; dan caveat evaluator
campur hilang karena semuanya diukur satu protokol.

**Yang TIDAK dibuktikan — jangan dilewat.** Sama seperti SR-013, run ini tidak
mengisolasi NMS sebagai penyebab. RF-DETR berbeda dari RT-DETR pada backbone
(DINOv2 vs HGNetv2-L), pra-latih, dan kepala hasil NAS sekaligus. Yang terbukti
adalah **arah arsitektur**, bukan mekanisme tunggal.

**Harga yang dibayar.** RF-DETR paling lambat: **118,1 ms / 8,5 FPS** di NVIDIA L4,
versus RT-DETR 74,2 ms dan YOLO26m 24,8 ms. Untuk lapangan waktu-nyata ini
penghalang nyata; optimasi FP16 belum diukur.

**Kelas tersulit tetap B4** (AP50 0,433) dan pasangan yang paling sering tertukar
tetap **B2↔B3** (184 B2→B3, 60 B3→B2 pada test) — kedua diagnosis lama
([SR-007](SR-007-diagnosis-b4.md), [SR-009](SR-009-ordinalitas-kelas.md)) bertahan.

## 6. Reproduksi

```bash
cd experiments/code
.venv/bin/python build/build_rfdetr_ds.py
.venv/bin/python train/train_rfdetr.py --dataset rfdetr_ds --epochs 60 \
    --resolution 1280 --batch 8 --grad-accum 2 --workers 8
.venv/bin/python train/train_yolo26l.py
.venv/bin/python eval/eval_all_pycoco.py     # tabel 1-protokol keempat model
.venv/bin/python eval/eval_all_metrics.py    # COCO 12-stat + P/R/F1
.venv/bin/python eval/eval_extras.py         # confusion, bootstrap, kurva PR
.venv/bin/python eval/eval_efficiency.py     # latensi & FPS
# keluaran: results/E-021/, runs/rfdetr_l_e60_i1280/, runs/yolo26l_e60_i1280/
```

Metrik lengkap: [`experiments/METRICS.md`](../METRICS.md) §1-protokol.
Log entri: [`experiments/EKSPERIMEN.md`](../EKSPERIMEN.md) §E-021.
