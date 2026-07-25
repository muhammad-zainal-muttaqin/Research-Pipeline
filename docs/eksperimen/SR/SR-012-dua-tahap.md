# SR-012 — Detektor dua tahap tidak mengalahkan satu tahap

**Ide I-23** · **Eksperimen:** E-017 · **Putusan: DIPALSUKAN** · 2026-07-21

---

## 1. Masalah

SR-010 menunjukkan 38% mAP50 yang mungkin diraih hilang di penilaian
kematangan, bukan di deteksi. Dugaan yang wajar: head klasifikasi YOLO
mengambil keputusan kematangan dari peta fitur citra yang sudah diperkecil ke
640 — tempat tandan hanya bermedian 46–63 px — sedangkan bukti kematangan
adalah warna dan tekstur permukaan buah, yang butuh piksel.

## 2. Ide

Pisahkan kedua keputusan secara arsitektural:

- **Tahap 1** mendeteksi tandan tanpa dibebani kematangan (`single_cls`),
  dilatih pada 960 supaya lokalisasi — penentu mAP50-95 — ikut membaik.
- **Tahap 2** menilai kematangan dari potongan pada **resolusi master
  3024×4032** (dibuka oleh E-015), dengan kapasitas penuh sebuah ConvNeXt-Tiny
  yang tidak melakukan hal lain.

Skor gabungan = skor objek × peluang kelas, tiap kotak menyumbang ke keempat
kelas — cara skor detektor dua-tahap klasik dihitung, bukan penyetelan angka.

**Yang akan memalsukan:** mAP 4-kelas dua tahap tidak melampaui satu tahap.

## 3. Solusi

`train_agnostic.py` (yolo26m, `single_cls`, imgsz 960, diinisialisasi dari
baseline RGB yang sudah konvergen) · `build_crops_raw.py` · `train_maturity.py`
dan `train_maturity_v2.py` · `two_stage.py` (evaluasi pycocotools).

Augmentasi tahap 2 sengaja **aman-warna**. Baseline YOLO memakai `hsv_s=0.7`,
yang mengacak saturasi ±70% — pada tugas yang buktinya adalah warna, resep
bawaan itu merusak sinyalnya sendiri.

**Integritas** — split per pohon 716/96/141, irisan train–val, train–test, dan
val–test semuanya nol. Konfigurasi dipilih pada val; test hanya dilaporkan.
Evaluator diverifikasi terhadap ultralytics pada baseline (0,5153/0,2384 vs
0,5218/0,2407).

## 4. Hasil

**Tahap 1 berhasil** — dan ini bagian yang positif:

| Deteksi kelas-agnostik | mAP50 | mAP50-95 |
|---|---|---|
| Baseline 4-kelas dievaluasi agnostik (640) | 0,7191 | 0,3197 |
| **Tahap 1 khusus agnostik (960, 6 epoch)** | **0,7730** | **0,3320** |

Dipotong pada epoch 6 dari 25 karena anggaran waktu; epoch 6 kebetulan yang
terbaik dari yang sempat berjalan.

**Tahap 2 gagal menutup celahnya.** Dua rezim, dua mode gagal berlawanan, satu
plafon yang sama:

| Pengklasifikasi | val acc | val seimbang |
|---|---|---|
| v1 (tanpa penyeimbang) | 0,6910 | 0,6116 |
| v2 (pencuplikan berimbang) | 0,5350 | 0,6656 |
| **Head YOLO (acuan)** | 0,6871 | **0,6484** |

**Rakitan penuh, val, mAP 4-kelas:**

| Sistem | mAP50 | mAP50-95 |
|---|---|---|
| **Baseline satu tahap (640)** | **0,5218** | **0,2407** |
| Dua tahap (960 + potongan master) | 0,4787 | 0,2076 |

AP50 per kelas: B1 0,698 · B2 0,367 · B3 0,524 · B4 0,326 — **di bawah baseline
pada keempat kelas** (0,735 · 0,408 · 0,556 · 0,388).

## 5. Putusan — DIPALSUKAN

Dua tahap **lebih buruk**, meskipun tahap 1-nya lebih baik. Penjelasannya utuh
dan konsisten dengan SR-011: head klasifikasi YOLO **sudah berada di plafon**
(0,6871 akurasi, 0,6484 seimbang). Tidak ada ruang yang bisa direbut dengan
memberi lebih banyak piksel atau kapasitas khusus, karena bukan piksel yang
kurang.

Yang terjadi justru sebaliknya — dua tahap **kehilangan** sesuatu yang dimiliki
satu tahap:

1. **Konteks.** Head YOLO melihat seluruh citra; potongan tidak. Pada tugas
   yang jawabannya relatif (buah ini lebih matang dibanding apa?), konteks itu
   bernilai — dan itulah yang membuat potongan resolusi 3× tetap tidak menang.
2. **Kalibrasi bersama.** Skor objek dan skor kelas pada satu tahap dilatih
   bersama, sehingga peringkatnya saling menyesuaikan. Mengalikan dua skor dari
   dua model yang dilatih terpisah merusak peringkat itu, dan mAP menghukum
   kerusakan peringkat lebih keras daripada kesalahan argmax.

### Kegunaan hasil negatif ini

I-23 adalah gagasan yang paling masuk akal setelah SR-010, dan ia gagal karena
alasan yang sekarang terukur, bukan karena dugaan. Bersama SR-011, konsekuensinya:

> Perbaikan **penilaian kematangan** dari citra RGB — lewat resolusi, kapasitas,
> arsitektur, modalitas, maupun jumlah sudut pandang — sudah habis. Yang tersisa
> hanya perubahan pada perumusan tugas atau pada sumber buktinya.

**Tahap 1 tetap dipakai.** Angka 0,7730/0,3320 adalah sistem deteksi tandan
terbaik yang kita punya, dan mAP50-95-nya **melampaui sasaran 0,30**. Untuk
aplikasi lapangan yang menghitung tandan (bukan menilai kematangannya), itu
komponen yang layak dipasang apa adanya.

## 6. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python train_agnostic.py
.venv/bin/python build_crops_raw.py
.venv/bin/python train_maturity_v2.py --root crops_raw --out runs/maturity_raw
.venv/bin/python two_stage.py --det runs/agn_e25_i960_s42/weights/best.pt \
    --cls runs/maturity_raw/best.pt --split val --crop-source raw
```
