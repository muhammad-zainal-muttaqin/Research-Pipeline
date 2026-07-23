# Laporan Eksperimen — Deteksi & Penghitungan Tandan Sawit

**Cuplikan terkurasi (*curated snapshot*) per 22 Juli 2026.** Dokumen ini bukan
log dan bukan pengganti log. Ia merangkai satu cerita dari basis pustaka sampai
titik jeda hari ini, lalu menunjuk ke berkas kanonik untuk tiap angkanya.

Sumber kanonik yang dirangkum di sini:
[`EKSPERIMEN.md`](EKSPERIMEN.md) (log kronologis, *append-only*) ·
[`SR/README.md`](SR/README.md) (pandangan per-ide) ·
[`METRICS.md`](METRICS.md) (tabel metrik definitif) ·
[`STATUS.md`](STATUS.md) (titik jeda & jalur lanjutan) ·
[`../pipeline/README.md`](../pipeline/README.md) (deliverable produksi).

---

## 0. Cara membaca — label yang dipakai

**Label tahap (*stage labels*)** — empat tahap yang menyusun cerita di bawah:

| Label | Arti |
|---|---|
| **LIT-182** | *Literature base* — 182 entri terverifikasi yang memasok setiap hipotesis |
| **PILOT-SAWITMVC-RGB** | *Bounded RGB pilot* — seluruh eksperimen di bawah, dikerjakan pada SawitMVC 960×1280 + master 3024×4032, kamera RGB saja |
| **RESULT-RTDETR-RGB** | *Final RGB result* — detektor 4-kelas terbaik yang dihasilkan pilot ini |
| **GEMINI-PENDING** | *Pending depth-sensor phase* — menunggu data fisik Orbbec Gemini; belum ada satu angka pun |

**Label putusan (*verdict labels*)** — dipakai apa adanya dari log:

| Indonesia | English | Arti |
|---|---|---|
| DIKONFIRMASI | CONFIRMED | hipotesis bertahan terhadap uji yang bisa memalsukannya |
| DIPALSUKAN | FALSIFIED | hipotesis gugur; jalan ditutup |
| TIDAK KONKLUSIF | INCONCLUSIVE | uji tidak menjawab |
| DITARIK | WITHDRAWN | klaim pernah dibuat lalu dicabut karena buktinya cacat |
| MENEMPEL BASELINE | NULL RESULT | dijalankan penuh, angkanya tidak bergerak |

---

## 1. LIT-182 — dari mana hipotesisnya berasal

Repositori ini berangkat dari tinjauan pustaka: **182 entri terverifikasi** (ada
PDF lokal) dari 202 record BibTeX, 14 klaster tema, fokus 2019–2026. Tinjauan itu
sudah selesai ditulis; perannya di sini adalah memasok hipotesis yang *terlacak*,
bukan tebakan.

Yang diambil dari korpus dan benar-benar diuji:

- **Depth Anything 3** (entri 198) — geometri konsisten lintas-pandangan → E-003,
  E-004, E-005, E-006, E-007.
- **Fusi middle/late, bukan early** (sapuan 28 titik fusi Ophoff dkk.,
  `evidence-body.tex` §174) → dasar I-4/I-5.
- **Gerbang mutu depth** (SA-Gate entri 055; D3Net entri 037: depth buruk merusak
  prediksi) → I-8, masih menunggu GEMINI-PENDING.
- **Detektor NMS-free** sebagai prioritas 1 (`deep-research-report.md`) → E-020,
  yang akhirnya menjadi hasil terbaik.

Satu batas yang harus disebut sejak awal: **tidak ada satu pun benchmark RGB-D
pada FFB sawit di dalam 182 entri itu.** Karena itu setiap klaim "depth menaikkan
angka" berstatus hipotesis desain yang bisa dipalsukan, dan memang sebagian sudah
dipalsukan di bawah.

---

## 2. PILOT-SAWITMVC-RGB — batas ruang lingkupnya

Seluruh eksperimen 21–22 Juli 2026 dikerjakan dalam pilot yang **sengaja
dibatasi**:

| Dimensi | Isi pilot |
|---|---|
| Data | SawitMVC 960×1280 (953 pohon, 18.540 bbox, 9.823 *unique bunch*) + master mentah 3024×4032 |
| Split | per pohon 716/96/141, irisan train/val/test **nol** |
| Sensor | **RGB saja.** Semua "depth" di pilot ini adalah *pseudo-depth* dari model monokular |
| Pemilihan | konfigurasi dipilih di **val**, test hanya dilaporkan |
| Acuan | DiB 67 (2026) 112990 — YOLO26m test AP50 0,531; B4 0,354 |
| Sasaran | **mAP50 0,60 · mAP50-95 0,30 pada 4 kelas penuh**, angka COCO apa adanya |

Acuan DiB itu **sengaja tidak di-tuning** oleh penulisnya (`imgsz=640`, SVR
default) — ia titik acuan, bukan plafon.

---

## 3. Peta 19 eksperimen

Semua eksperimen yang tercatat di [`EKSPERIMEN.md`](EKSPERIMEN.md), dengan
putusan apa adanya. Empat dipalsukan dan satu ditarik — itu justru bagian yang
paling mempersempit arah kerja.

| E | Yang diuji | SR / ide | Putusan (ID / EN) |
|---|---|---|---|
| E-001 | `class_mismatch` sebagai ukuran ambiguitas kematangan | [SR-001](SR/SR-001-ambiguitas-kematangan.md) | DIPALSUKAN / FALSIFIED |
| E-002 | Master mentah 3024×4032 langsung pakai anotasi MVC | [SR-002](SR/SR-002-resolusi-master-mentah.md) | TIDAK KONKLUSIF / INCONCLUSIVE |
| E-003 | DA3 pada video orbit (n=1 video) | [SR-003](SR/SR-003-da3-video-orbit.md) | SEBAGIAN / PARTIAL |
| E-004 | DA3 pada 6 video, rotasi diperbaiki | [SR-003](SR/SR-003-da3-video-orbit.md) | DIKONFIRMASI / CONFIRMED |
| E-005 | DA3 pada 4 dan 8 sisi foto asli | [SR-004](SR/SR-004-da3-empat-sisi.md) | DIKONFIRMASI / CONFIRMED |
| E-006 | Kedalaman sebagai pemisah tandan (tingkat piksel) | [SR-005](SR/SR-005-sinyal-depth-tandan.md) | DIPALSUKAN / FALSIFIED |
| E-007 | Penautan tandan lintas-sisi secara geometris | [SR-006](SR/SR-006-penautan-geometris.md) | DIPALSUKAN / FALSIFIED |
| E-009 | Ukuran kotak GT pada resolusi latih | [SR-007](SR/SR-007-diagnosis-b4.md) | SEBAGIAN / PARTIAL |
| E-010 | Diagnosis penyebab kegagalan B4 | [SR-007](SR/SR-007-diagnosis-b4.md) | DIKONFIRMASI (kontras) / DIPALSUKAN (kepadatan) |
| E-011 | Praproses mana yang menaikkan keterpisahan B4 | [SR-008](SR/SR-008-kanal-tekstur.md) | DIKONFIRMASI (tekstur) / DIPALSUKAN (penajam kontras) |
| E-012 | Kematangan dari penampilan potongan GT | [SR-009](SR/SR-009-ordinalitas-kelas.md) | DIKONFIRMASI / CONFIRMED |
| E-013 | Pipeline produksi 4-kanal untuk sensor depth | [`pipeline/`](../pipeline/README.md) | SIAP PAKAI / DELIVERED |
| E-014 | Hambatan mAP: deteksi atau klasifikasi? | [SR-010](SR/SR-010-hambatan-klasifikasi.md) | DIKONFIRMASI / CONFIRMED |
| E-015 | Pemetaan master mentah lewat pencocokan isi | [SR-002](SR/SR-002-resolusi-master-mentah.md) | TERBLOKIR → DIBUKA / UNBLOCKED |
| E-016 | Plafon kematangan, diukur tiga kali | [SR-011](SR/SR-011-plafon-kematangan.md) | DITARIK / WITHDRAWN (lewat E-018) |
| E-017 | Detektor dua tahap (agnostik + kepala kematangan) | [SR-012](SR/SR-012-dua-tahap.md) | DIPALSUKAN / FALSIFIED |
| E-018 | Selubung lokalisasi empiris: 0,60/0,30 mungkin? | ide I-24 | DIKONFIRMASI / CONFIRMED |
| E-019 | Detektor 4-kelas 1280 + augmentasi aman-warna | ide I-24 | MENEMPEL BASELINE / NULL RESULT |
| E-020 | RT-DETR-L, detektor tanpa NMS | [SR-013](SR/SR-013-rtdetr-nms-free.md) | DIKONFIRMASI (arah) / CONFIRMED (direction) |

---

## 4. Temuan kunci

### 4.1 Geometri DA3 bekerja — tetapi bukan di tempat yang dibutuhkan

Depth Anything 3 memulihkan susunan kamera yang benar pada dua kondisi berbeda:

| Uji | Hasil |
|---|---|
| Video orbit, 6 video, 32 frame | **5 dari 6** video mencapai sapuan mulus ≥270°; `smooth_frac` median 100% |
| Foto 4 dan 8 sisi, 50 pohon | urutan sisi benar pada **50 dari 50 pohon (100%)**; RMSE sudut 17,3° (4 sisi) dan 8,5° (8 sisi) vs pembanding acak 57,5° dan 34,4° |

Rekonstruksi tingkat-pohon karena itu **DIKONFIRMASI**. Sebab kegagalan satu
video sisanya masih belum diketahui; tiga kandidat penjelasan sudah dipalsukan
dan tidak ada penjelasan pengganti yang dikarang.

Yang penting: keberhasilan ini **tingkat pohon**, bukan tingkat tandan.

### 4.2 Pseudo-depth tidak memisahkan tandan — 0,26× kendali acak

E-006 mengukur kontras kedalaman di dalam kotak tandan versus cincin
sekelilingnya, pada 40 pohon (780 kotak GT), dengan **kendali 2 kotak acak
seukuran per kotak asli** (1.560 kendali) — kendali ini wajib, karena peta
kedalaman apa pun punya struktur sehingga kotak apa pun menunjukkan kontras
tertentu.

| | kontras (res 504) | kontras (res 1008) |
|---|---|---|
| Kotak tandan asli | 0,0089 | 0,0096 |
| Kotak acak kendali | 0,0341 | 0,0364 |
| **Rasio** | **0,26×** | **0,26×** |

Tandan justru **kurang** menonjol dalam kedalaman daripada tambalan acak, dan
rasio 0,26× **identik** pada dua resolusi sehingga bukan artefak resolusi.
Selisih AUC +0,009 signifikan secara statistik pada n besar tetapi ukuran
efeknya dapat diabaikan. Per kelas, **B4 justru ber-AUC terendah (0,6022)**.

**Batas klaim yang wajib dibawa:** kedalaman ini **relatif**, bukan metrik
(`is_metric` kosong pada keluaran DA3), dan berasal dari **RGB yang sama**
sehingga galatnya berkorelasi dengan citranya. Ia prior struktural dari model
monokular, **bukan** pengukuran sensor. **Depth sensor Orbbec Gemini belum
pernah diuji sama sekali** — E-006 tidak berbicara tentangnya.

### 4.3 Tahap penghitungan sudah jenuh — koreksi k mencapai 95,57%

E-007 lebih dulu memvalidasi perangkatnya: jumlah mentah dan koreksi global
direproduksi **persis** dari Tabel 4 DiB. Lalu tangga ablasi §208 dijalankan pada
141 pohon split uji:

| Mode | Class ±1 | Tree ±1 | MAE |
|---|---|---|---|
| A. hanya penampilan | 77,13% | 32,62% | 0,876 |
| B. depth tanpa pose | 75,00% | 29,08% | 0,966 |
| C. sadar-pose (3D) | 69,50% | 22,70% | 1,367 |
| **D. koreksi global k = 1,8905** | **95,57%** | **86,52%** | **0,356** |

Penautan geometris **DIPALSUKAN**: ia kalah telak, dan justru yang paling
canggih yang paling buruk. Sapuan ambang (9 nilai untuk pose) menutup
kemungkinan salah setelan. Batas klaim: yang dipalsukan adalah **implementasi**
di atas kedalaman relatif; uji yang adil menuntut kedalaman metrik terkalibrasi.

Konsekuensi strategisnya tegas: **koreksi k sederhana sudah 95,57% bila diberi
deteksi bersih.** Ruang perbaikan di tahap counting tipis. Sisa perbaikan harus
datang dari detektor.

### 4.4 Kerugian mAP ada di klasifikasi kematangan, bukan di deteksi

E-014 mengambil **bobot yang identik** dan **val yang identik** (404 citra), lalu
mengubah satu bendera saja (`single_cls`):

| Evaluasi | mAP50 | mAP50-95 | P | R |
|---|---|---|---|---|
| 4 kelas | 0,5218 | 0,2407 | 0,5307 | 0,5484 |
| **Kelas-agnostik** | **0,7191** | **0,3197** | 0,6950 | 0,6365 |

38% mAP50 yang mungkin diraih hilang di penilaian kematangan; efektivitas
klasifikasi terukur 0,5218/0,7191 = **72,6%**. Detektor khusus agnostik pada
imgsz 960 bahkan mencapai **0,7730 / 0,3320** — mAP50-95 agnostik itu sudah
**melewati** sasaran 0,30.

Temuan pendukungnya konsisten:

- **B4 gagal karena tersamar, bukan bertumpuk.** Kontras CIELAB B4 (ΔE 11,55)
  **di bawah kotak acak** (12,92); tetangganya paling sedikit (2,58) dan IoU
  maksimumnya paling rendah (0,029).
- **Satu-satunya sinyal yang tersisa untuk B4 adalah tekstur.** Pada kanal
  Laplacian, peringkat kelas berbalik: B4 dari paling tidak terpisah (0,5573)
  menjadi **paling terpisah** (0,6153).
- **Kematangan itu kontinu.** Kebingungan hampir seluruhnya antar kelas
  bersebelahan pada rantai B1→B2→B3→B4; B3→B1 hanya 7 dari 375.

### 4.5 Selubung lokalisasi empiris — 0,8834 / 0,4702

Sebelum membakar jam GPU, E-018 memeriksa apakah kotak anotasinya sendiri
memungkinkan sasaran. Untuk tiap kotak GT val diambil IoU tertinggi dengan
deteksi mana pun (kelas diabaikan, conf 0,05):

| | Baseline 640 | Agnostik 960 |
|---|---|---|
| GT tercapai IoU≥0,50 | 0,8834 | 0,8786 |
| GT tercapai IoU≥0,75 | 0,4494 | 0,3975 |
| GT tercapai IoU≥0,90 | 0,0376 | 0,0254 |
| Median IoU terbaik | 0,7303 | 0,7110 |
| **Selubung mAP50 (kelas sempurna)** | **0,8834** | 0,8786 |
| **Selubung mAP50-95 (kelas sempurna)** | **0,4702** | 0,4448 |

Sasaran mAP50 0,60 = 68% dari 0,8834; mAP50-95 0,30 = 64% dari 0,4702. Posisi
saat ini 59% dan 51%. Artinya yang dituntut adalah menutup celah **klasifikasi
dan peringkat skor**.

**Apa yang angka ini BUKAN.** 0,8834/0,4702 adalah **selubung empiris** yang
diukur dari himpunan deteksi satu model tertentu pada satu split. Ia bukan
plafon ketelitian anotasi yang absolut, bukan batas fisik dataset, dan bukan
angka yang berlaku untuk detektor lain tanpa diukur ulang. Detektor yang
melokalisasi lebih baik akan menggeser selubungnya. Yang sah disimpulkan hanya:
sasaran **tidak** terhalang oleh kelonggaran kotak GT.

Peringatan yang menyertainya tetap berlaku: hanya 3,76% kotak GT tercapai pada
IoU≥0,90 dan median IoU terbaik 0,73 — batas tandan memang kabur, jadi mAP50-95
akan selalu jauh lebih berat daripada mAP50 di dataset ini.

Pada kesempatan yang sama, klaim "plafon kematangan 68%" dari E-016
**DITARIK**: dua dari tiga pengukurannya tidak bebas satu sama lain, dan
pembandingnya dilumpuhkan augmentasi `hsv_s=0.7`. Angka itu tidak boleh dikutip
sebagai plafon.

---

## 5. RESULT-RTDETR-RGB — hasil akhir pilot

### 5.1 Semua run detektor, berdampingan

Angka COCO/ultralytics apa adanya, dari [`METRICS.md`](METRICS.md).

**Val (dasar pemilihan konfigurasi):**

| Run | Ide/E | imgsz | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|---|---|
| yolo26m baseline | acuan | 640 | 0,5218 | 0,2407 | 0,7354 | 0,4076 | 0,5561 | 0,3881 |
| RGBD 4-kanal (*pseudo-depth*) | I-4 | 640 | 0,5041 | 0,2378 | 0,7160 | 0,3821 | 0,5336 | 0,3847 |
| 4-kelas aman-warna | E-019 | 1280 | 0,5186 | 0,2358 | 0,7011 | 0,4130 | 0,5682 | 0,3922 |
| **RT-DETR-L** | **I-14** | 1280 | **0,5466** | **0,2543** | 0,7503 | 0,4413 | 0,5808 | 0,4138 |

**Test (dilaporkan; tidak dipakai memilih):**

| Run | Ide/E | imgsz | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|---|---|
| DiB publikasi | acuan | 640 | 0,531 | — | 0,739 | 0,433 | 0,599 | 0,354 |
| yolo26m baseline (kami) | acuan | 640 | 0,5161 | 0,2457 | 0,7410 | 0,4016 | 0,5894 | 0,3323 |
| RGBD 4-kanal (*pseudo-depth*) | I-4 | 640 | 0,5192 | 0,2471 | 0,7509 | 0,4115 | 0,5859 | 0,3283 |
| 4-kelas aman-warna | E-019 | 1280 | 0,5418 | 0,2493 | 0,7546 | 0,4503 | 0,6037 | 0,3585 |
| **RT-DETR-L** | **I-14** | 1280 | **0,5794** | **0,2694** | 0,7891 | 0,4685 | 0,6391 | **0,4208** |

**Deteksi kelas-agnostik (tanpa penilaian kematangan):**

| Run | Ide/E | imgsz | split | mAP50 | mAP50-95 |
|---|---|---|---|---|---|
| baseline dievaluasi agnostik | E-014 | 640 | val | 0,7191 | 0,3197 |
| detektor khusus agnostik | I-23 | 960 | val | **0,7730** | **0,3320** |

Catatan run: RGBD 4-kanal dihentikan pada epoch 25/60 (kurva datar); E-019
dihentikan pada epoch 41 karena *fine-tune* dari checkpoint 640 mengganggu model
— itu bukti strategi inisialisasi yang salah, bukan bukti resolusi/augmentasi
gagal. RT-DETR-L dihentikan pada epoch 52; `best.pt` = epoch fitness-terbaik
(ep25).

### 5.2 RT-DETR-L: selisih terhadap baseline

RT-DETR-L (ultralytics 8.4.103, **32.970.476 parameter**, 103,4 GFLOPs, backbone
HGNetv2-L, encoder AIFI + RepC3, RTDETRDecoder), dilatih 1280 dari bobot COCO,
augmentasi aman-warna (`hsv_s=0.15`).

| TEST | mAP50 | mAP50-95 | B1 | B2 | B3 | **B4** |
|---|---|---|---|---|---|---|
| Baseline yolo26m | 0,5161 | 0,2457 | 0,7410 | 0,4016 | 0,5894 | 0,3323 |
| **RT-DETR-L** | **0,5794** | **0,2694** | 0,7891 | 0,4685 | 0,6391 | **0,4208** |
| selisih | **+0,0633** | +0,0237 | +0,0481 | +0,0669 | +0,0497 | **+0,0885** |

Ini **detektor 4-kelas terbaik yang dihasilkan pilot**: unggul pada keempat
kelas di kedua split, dengan kenaikan terbesar pada **B4 (+0,0885 test)** — kelas
yang paling tersamar.

**Batas atribusi — penting.** Pola "gain terbesar di kelas terpadat" **konsisten
dengan** hipotesis NMS-free, tetapi run ini **tidak** mengisolasi NMS sebagai
penyebab. Yang berubah sekaligus: keluarga arsitektur (transformer decoder vs
head YOLO), backbone (HGNetv2-L vs yolo26m), pencocokan Hungarian satu-ke-satu,
kapasitas (33,0 juta vs 21,9 juta parameter), bobot pratlatih COCO yang berbeda,
dan resolusi latih (1280 vs 640). Kenaikan +0,063 karena itu adalah **efek
gabungan seluruh perubahan tersebut**, bukan efek terukur dari menghapus NMS.
Menyatakan "NMS adalah penyebabnya" menuntut ablasi yang belum dijalankan —
misalnya RT-DETR pada 640, atau YOLO dengan pasca-pemrosesan diganti.

### 5.3 Jarak ke sasaran

| | mAP50 | ke 0,60 | mAP50-95 | ke 0,30 |
|---|---|---|---|---|
| val | 0,5466 | **−0,053** | 0,2543 | **−0,046** |
| test | **0,5794** | **−0,021** | **0,2694** | **−0,031** |

Terdekat yang pernah dicapai, dan **sasaran belum tembus**. Test tinggal −0,021
dari mAP50 0,60 dan −0,031 dari mAP50-95 0,30.

Bobot terbaik (`best.pt`, 264 MB) berada di luar repo dan dapat direproduksi dari
skrip arsip; pengarsipannya ke penyimpanan objek belum dilakukan.

---

## 6. GEMINI-PENDING — apa yang menunggu di depan

### 6.1 Yang sudah siap dan tidak hilang

- **[`pipeline/`](../pipeline/README.md)** — pipeline produksi YOLO 4-kanal
  (RGB + depth) untuk kamera **Orbbec Gemini**. Satu bobot melayani dua mode uji
  lewat *modality dropout*: RGB+depth saat sensor terpasang, RGB saja saat tidak.
  Kontrak kanal keempat sudah dibekukan (PNG uint8, `0` = tidak ada data,
  `1..255` = *inverse depth* pada rentang metrik tetap 0,3–8 m). Integrasi ke
  aplikasi lapangan yang sudah ada = tiga baris (`Sawit4CH`). **Belum ada bobot
  terlatih** — pipeline menunggu data fisik.
- **Dataset master 3024×4032** — dirakit dari peta isi E-015 (3.992/3.992 cocok,
  skor terendah 0,9985, nol ambigu), menunjuk ke piksel master penuh tanpa
  anotasi ulang karena rasio aspeknya identik (0,75). Belum dipakai melatih
  apa pun.
- **RT-DETR-L best.pt** — model terbaik (§5).

### 6.2 Jalur lanjutan, prioritas turun

1. **RT-DETR-L pada piksel master 3024×4032** (imgsz 1600–2048) — menyerang
   lokalisasi, penentu mAP50-95 yang sasarannya paling jauh. Taruhan terbaik
   menutup −0,021 terakhir.
2. **RT-DETR-X** (67,5 juta parameter) — menguji kapasitas di atas mekanisme yang
   sudah terbukti lebih baik.
3. **Loss ordinal / kepala regresi kematangan (I-22)** — menyerang ketidakcocokan
   objektif-vs-metrik dari §4.4, dan belum pernah diuji di atas detektor terbaik.
4. **Loss berimbang/focal (I-13), neck BiFPN (I-15)** — prioritas terendah.

### 6.3 Yang menunggu keputusan pengguna, bukan sekadar teknis

- **Depth sensor Gemini.** Depth **sensor** — pengukuran fisik yang independen
  dari RGB — **belum pernah diuji.** Yang dipalsukan di §4.2 adalah pseudo-depth
  monokular relatif. `pipeline/` ada justru supaya pertanyaan ini bisa dijawab
  begitu datanya terkumpul, dan gerbang mutu depth (I-8) baru relevan pada tahap
  itu.
- **Brondolan lepas** sebagai penanda kematangan — kriteria panen lapangan yang
  sesungguhnya, tidak terlihat dari kanopi pada jarak foto ini. Ini mengubah
  **perumusan tugas**, bukan tuning, dan perlu persetujuan sebelum disentuh.

---

## 7. Batas klaim — yang tidak boleh dibaca berlebihan

Diringkas dari peringatan yang tersebar di log; semuanya mengikat.

1. **Pseudo-depth ≠ depth sensor.** Semua angka depth di pilot ini berasal dari
   model monokular, bersifat **relatif** (bukan metrik), dan galatnya berkorelasi
   dengan RGB sumbernya. Tidak satu pun berbicara tentang Orbbec Gemini.
2. **Kenaikan RT-DETR bukan bukti kausal tentang NMS.** Lihat §5.2 — banyak hal
   berubah sekaligus.
3. **0,8834/0,4702 adalah selubung empiris, bukan plafon anotasi absolut.**
   Lihat §4.5.
4. **"Plafon kematangan 68%" sudah DITARIK.** Jangan dikutip.
5. **Nol `class_mismatch`** (E-001) adalah pemeriksa integritas data yang bersih;
   ia **tidak** mendukung maupun membantah klaim ambiguitas B2/B3, dan bukan
   "konsistensi anotator 100%".
6. **52,87%** dari E-012 adalah batas **bawah** keterpisahan dari fitur buatan
   tangan; yang transferable adalah struktur kebingungannya yang ordinal, bukan
   angkanya.
7. **Keberhasilan geometri DA3 bersifat tingkat-pohon.** Pemisahan tingkat-tandan
   tidak terbukti — justru dipalsukan (§4.2).
8. **mAP tidak dapat mewakili toleransi ordinal.** Kedua cara memaksakannya
   menurunkan angka; pelaporan yang jujur memisahkan AP deteksi kelas-agnostik
   dari akurasi kematangan.

---

## 8. Reproduksi

Kode eksperimen dijalankan di luar repo; snapshot kode, hasil JSON, dan split
diarsipkan di dalam repo bersama panduan reproduksi langkah demi langkah
(skrip → SR → keluaran, versi persis pustaka, dan celah yang diakui jujur).
Dataset: SawitMVC 960×1280 dan master 3024×4032, split per pohon 716/96/141
dengan irisan nol — invarian yang harus dijaga.

Untuk deliverable produksi, seluruh perintah latih/konversi/inferensi ada di
[`../pipeline/README.md`](../pipeline/README.md).

---

*Cuplikan ini dikurasi 22 Juli 2026. Angka apa adanya, hasil negatif ikut
dilaporkan. Bila ada selisih antara dokumen ini dan
[`EKSPERIMEN.md`](EKSPERIMEN.md) / [`METRICS.md`](METRICS.md), yang kanonik
adalah kedua berkas itu.*
