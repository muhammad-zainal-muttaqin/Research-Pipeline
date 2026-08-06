# Laporan Eksperimen — Deteksi & Penghitungan Tandan Sawit

**Cuplikan terkurasi (*curated snapshot*) per 1 Agustus 2026.** Dokumen ini bukan
log dan bukan pengganti log. Ia merangkai satu cerita dari basis pustaka sampai
titik jeda hari ini, lalu menunjuk ke berkas kanonik untuk tiap angkanya.

Mencakup **E-001 sampai E-032**, dua dataset, dan dua fase yang berbeda sifatnya:
pilot RGB yang berujung pada hasil terbaik (E-021), lalu blok depth sensor yang
**tidak menghasilkan manfaat terkonfirmasi dalam rezim diuji** (E-022…E-032).
Keduanya diperlakukan sama —
angka apa adanya.

Sumber kanonik yang dirangkum di sini:
[`docs/experiments/EKSPERIMEN.md`](EKSPERIMEN.md) (log kronologis, *append-only*) ·
[`docs/experiments/SR/README.md`](SR/README.md) (pandangan per-ide) ·
[`docs/experiments/METRICS.md`](METRICS.md) (tabel metrik definitif E-021) ·
[`docs/experiments/METRIK-LENGKAP.md`](METRIK-LENGKAP.md) (metrik seluruh run blok depth) ·
[`docs/experiments/AUDIT-E022.md`](AUDIT-E022.md) (koreksi E-022) ·
[`docs/experiments/STATUS.md`](STATUS.md) (titik jeda & jalur lanjutan) ·
[`reproduce/pipeline/README.md`](../../reproduce/pipeline/README.md) (deliverable produksi).

> **Pembaruan audit 2 Agustus 2026.** Dokumen ini adalah snapshot kurasi
> historis. Untuk status klaim terbaru, gunakan `reports.tex` dan
> `REPORT_PLAN.md`. Khusus E-026, denominator identitas RGB dan RGB-D berbeda
> sehingga hasilnya tidak konklusif; khusus E-032, 12/12 CI memuat nol tetapi
> ekuivalensi belum dibuktikan. Status G0 tetap terbuka dan G4/G6 tidak ditutup
> secara universal.

---

## 0. Cara membaca — label yang dipakai

**Label tahap (*stage labels*)** — empat tahap yang menyusun cerita di bawah:

| Label | Arti |
|---|---|
| **LIT-182** | *Literature base* — 182 entri terverifikasi yang memasok setiap hipotesis |
| **PILOT-SAWITMVC-RGB** | *Bounded RGB pilot* — E-001…E-021, dikerjakan pada SawitMVC 960×1280 + master 3024×4032, kamera RGB saja |
| **RESULT-RFDETR-RGB** | *Final RGB result* — detektor 4-kelas terbaik yang dihasilkan pilot ini (E-021) |
| **DEPTH-SENSOR-MVCD** | *Physical depth-sensor phase* — E-022…E-032 pada SawitMVC-Depth (Orbbec, 352 pohon). **Sudah dijalankan**, dan hasilnya negatif di seluruh kontras |

Label **GEMINI-PENDING** yang dipakai versi 25 Juli sudah **tidak berlaku**:
sejak 29 Juli data depth sensor fisik tersedia dan diuji habis. Yang dulu
"menunggu satu angka pun" kini punya **54 run terarsip** (39 di E-022, 15 di
E-023) dan **49 kontras berpasangan** (37 + 12), seluruhnya dengan CI bootstrap.

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
- **Detektor NMS-free** sebagai prioritas 1 (`evidence/literature/references/deep-research-report.md`) → E-020,
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

## 3. Peta 30 eksperimen

Semua eksperimen yang tercatat di [`docs/experiments/EKSPERIMEN.md`](EKSPERIMEN.md), dengan
putusan apa adanya. Sepuluh dipalsukan, satu ditarik, satu dicabut — itu justru
bagian yang paling mempersempit arah kerja.

Nomor **E-008 tidak pernah dipakai** (tidak ada run), dan **E-023 dieksekusi di
bawah nomor E-032** karena rancangannya berubah sebelum dijalankan. Jadi 30
entri untuk rentang E-001…E-032, bukan 32.

### 3.1 Pilot RGB (E-001…E-021)

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
| E-013 | Pipeline produksi 4-kanal untuk sensor depth | [`reproduce/pipeline/`](../../reproduce/pipeline/README.md) | SIAP PAKAI / DELIVERED |
| E-014 | Hambatan mAP: deteksi atau klasifikasi? | [SR-010](SR/SR-010-hambatan-klasifikasi.md) | DIKONFIRMASI / CONFIRMED |
| E-015 | Pemetaan master mentah lewat pencocokan isi | [SR-002](SR/SR-002-resolusi-master-mentah.md) | TERBLOKIR → DIBUKA / UNBLOCKED |
| E-016 | Plafon kematangan, diukur tiga kali | [SR-011](SR/SR-011-plafon-kematangan.md) | DITARIK / WITHDRAWN (lewat E-018) |
| E-017 | Detektor dua tahap (agnostik + kepala kematangan) | [SR-012](SR/SR-012-dua-tahap.md) | DIPALSUKAN / FALSIFIED |
| E-018 | Selubung lokalisasi empiris: 0,60/0,30 mungkin? | ide I-24 | DIKONFIRMASI / CONFIRMED |
| E-019 | Detektor 4-kelas 1280 + augmentasi aman-warna | ide I-24 | MENEMPEL BASELINE / NULL RESULT |
| E-020 | RT-DETR-L, detektor tanpa NMS | [SR-013](SR/SR-013-rtdetr-nms-free.md) | DIKONFIRMASI (arah) / CONFIRMED (direction) |
| E-021 | RF-DETR-L (DINOv2) vs RT-DETR-L pada setelan identik | [SR-014](SR/SR-014-rfdetr-dinov2.md) | DIKONFIRMASI / CONFIRMED |

### 3.2 Blok depth sensor (E-022…E-032)

Dataset berganti ke **SawitMVC-Depth**. Angka di blok ini **tidak sebanding**
dengan blok pilot — lihat §6.1.

| E | Yang diuji | SR / gerbang | Putusan (ID / EN) |
|---|---|---|---|
| E-022a | Apakah depth sensor benar sudah tersejajar ke RGB? | [SR-015](SR/SR-015-depth-sensor-4kanal.md) | DIPALSUKAN / FALSIFIED (label sidecar bohong) |
| E-022b | Apakah depth sensor 4-kanal menaikkan mAP? | [SR-015](SR/SR-015-depth-sensor-4kanal.md) | DIPALSUKAN / FALSIFIED — **seluruh entri dicabut**, lihat [audit](AUDIT-E022.md) |
| E-024 | Inkonsistensi prediksi lintas-sisi sebagai ukuran ambiguitas | [SR-016](SR/SR-016-konsistensi-lintas-sisi.md) | DIKONFIRMASI / CONFIRMED (daya uji terbatas) |
| E-025 | Dari mana selisih evaluator E-022 berasal? | gerbang G1 | DIPALSUKAN (maxDets) / celah terlacak ke jumlah deteksi |
| E-026 | Apakah depth menstabilkan identitas lintas-sisi? | [SR-016](SR/SR-016-konsistensi-lintas-sisi.md) | TIDAK KONKLUSIF / INCONCLUSIVE — denominator identitas RGB/RGB-D berbeda |
| E-027 | Matriks multi-seed YOLO26n | gerbang G2 | DIPALSUKAN / FALSIFIED — depth **merugikan** |
| E-028 | Ukuran lintas-sisi pada SawitMVC (daya uji 6,2×) | [SR-016](SR/SR-016-konsistensi-lintas-sisi.md), G8 | DIKONFIRMASI / CONFIRMED |
| E-029 | Matriks multi-seed RT-DETR-L | gerbang G2, G3 | **DICABUT** / RETRACTED (klausa kapasitas SR-015) |
| E-030 | Sapuan kapasitas YOLO26 n→m→l | gerbang G7 | DIKONFIRMASI SEBAGIAN — klaim dipersempit |
| E-031 | Varians SPLIT vs varians SEED | gerbang G5 | DIKONFIRMASI / CONFIRMED (varians split nyata) |
| E-032 | Titik fusi: awal vs menengah vs akhir, semua dari nol | gerbang G4, G6 | TIDAK KONKLUSIF / INCONCLUSIVE dalam rezim diuji — 12/12 CI memuat nol; ekuivalensi belum dibuktikan |

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

## 5. RESULT-RFDETR-RGB — hasil akhir pilot

### 5.1 Semua run detektor, berdampingan

Angka COCO/ultralytics apa adanya, dari [`docs/experiments/METRICS.md`](METRICS.md).

**Val (dasar pemilihan konfigurasi):**

| Run | Ide/E | imgsz | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|---|---|
| yolo26m baseline | acuan | 640 | 0,5218 | 0,2407 | 0,7354 | 0,4076 | 0,5561 | 0,3881 |
| RGBD 4-kanal (*pseudo-depth*) | I-4 | 640 | 0,5041 | 0,2378 | 0,7160 | 0,3821 | 0,5336 | 0,3847 |
| 4-kelas aman-warna | E-019 | 1280 | 0,5186 | 0,2358 | 0,7011 | 0,4130 | 0,5682 | 0,3922 |
| YOLO26l (param-adil) | E-021 | 1280 | 0,5300 | 0,2516 | 0,7431 | 0,4358 | 0,5586 | 0,3825 |
| RT-DETR-L | I-14 | 1280 | 0,5466 | 0,2543 | 0,7503 | 0,4413 | 0,5808 | 0,4138 |
| **RF-DETR-L** | **E-021** | 1280 | **0,5695** | **0,2604** | 0,775 | 0,446 | 0,594 | **0,464** |

**Test (dilaporkan; tidak dipakai memilih):**

| Run | Ide/E | imgsz | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|---|---|
| DiB publikasi | acuan | 640 | 0,531 | — | 0,739 | 0,433 | 0,599 | 0,354 |
| yolo26m baseline (kami) | acuan | 640 | 0,5161 | 0,2457 | 0,7410 | 0,4016 | 0,5894 | 0,3323 |
| RGBD 4-kanal (*pseudo-depth*) | I-4 | 640 | 0,5192 | 0,2471 | 0,7509 | 0,4115 | 0,5859 | 0,3283 |
| 4-kelas aman-warna | E-019 | 1280 | 0,5418 | 0,2493 | 0,7546 | 0,4503 | 0,6037 | 0,3585 |
| YOLO26l (param-adil) | E-021 | 1280 | 0,5313 | 0,2553 | 0,7597 | 0,4223 | 0,5900 | 0,3534 |
| RT-DETR-L | I-14 | 1280 | 0,5794 | 0,2694 | 0,7891 | 0,4685 | 0,6391 | 0,4208 |
| **RF-DETR-L** | **E-021** | 1280 | **0,6038** | **0,2770** | 0,817 | 0,497 | 0,668 | 0,433 |

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

### 5.3 RF-DETR-L: sasaran mAP50 terlewati (E-021)

RF-DETR-L (rfdetr 1.8.3, **35.650.000 parameter**, backbone **DINOv2** patch-16
pra-latih + kepala LW-DETR hasil NAS), resolusi 1280 tepat, dari bobot COCO
`rf-detr-large-2026`. Checkpoint ep9 (EMA), *early-stop* ep17.

| TEST | mAP50 | mAP50-95 | B1 | B2 | B3 | **B4** |
|---|---|---|---|---|---|---|
| RT-DETR-L (E-020) | 0,5794 | 0,2694 | 0,7891 | 0,4685 | 0,6391 | 0,4208 |
| **RF-DETR-L (E-021)** | **0,6038** | **0,2770** | 0,817 | 0,497 | 0,668 | 0,433 |
| selisih | **+0,024** | +0,008 | +0,028 | +0,029 | +0,029 | +0,012 |

**Perbandingan adil, satu protokol.** Dua celah pada E-020 sudah ditutup: (1)
baseline YOLO **param-adil** YOLO26l (26,3 juta, konfigurasi identik RT-DETR)
dilatih penuh, dan (2) keempat model dievaluasi lewat **pipeline pycocotools yang
sama**, sehingga tidak ada lagi evaluator campur.

| Model | Param | VAL mAP50 / 50-95 | TEST mAP50 / 50-95 |
|---|---|---|---|
| YOLO26m | 21,9 jt | 0,5195 / 0,2411 | 0,5165 / 0,2452 |
| YOLO26l | 26,3 jt | 0,5270 / 0,2526 | 0,5300 / 0,2568 |
| RT-DETR-L | 33,0 jt | 0,5459 / 0,2555 | 0,5784 / 0,2707 |
| **RF-DETR-L** | 35,7 jt | **0,5695 / 0,2604** | **0,6038 / 0,2770** |

Urutan performa = urutan parameter di semua metrik dan kedua split. YOLO26l —
baseline YOLO sekelas DETR dari sisi kapasitas dan resolusi — **tetap di bawah
kedua DETR**. Artinya keunggulan RF-DETR/RT-DETR **bukan** efek kapasitas atau
resolusi.

**Signifikansi.** Bootstrap 2.000× *resample* gambar test (588, seed 42): selisih
berpasangan RF−RT = **+0,0255, CI 95% [0,0104 – 0,0408]**, P(RF>RT) = 0,999. CI
selisih tidak memuat nol.

**Harga yang dibayar — jangan dilewat.** RF-DETR paling akurat sekaligus paling
lambat: **118,1 ms / 8,5 FPS** di NVIDIA L4, versus RT-DETR 74,2 ms (13,5 FPS)
dan YOLO26m 24,8 ms (40,3 FPS). Untuk penerapan lapangan waktu-nyata ini
pertimbangan nyata; optimasi FP16 belum diukur.

**Confusion matrix (test, IoU 0,5, conf ≥ 0,25)** menguatkan dua diagnosis lama
secara kuantitatif: B2↔B3 adalah pasangan yang paling sering tertukar di semua
model (RF-DETR: 184 B2→B3, 60 B3→B2), dan B4 yang terlewat jadi latar jauh lebih
sedikit pada DETR (RT-DETR 91, RF-DETR 108) dibanding YOLO (YOLO26m 245,
YOLO26l 276) — sekitar 2,5× lebih baik.

### 5.4 Jarak ke sasaran

| | mAP50 | ke 0,60 | mAP50-95 | ke 0,30 |
|---|---|---|---|---|
| val | 0,5695 | **−0,031** | 0,2604 | **−0,040** |
| test | **0,6038** | **+0,004 (LEWAT)** | **0,2770** | **−0,023** |

**Sasaran mAP50 0,60 pada test terlewati untuk pertama kali.** mAP50-95 masih
kurang 0,023 — itu yang tersisa.

Bobot terbaik berada di luar repo dan dapat direproduksi dari skrip arsip:
RF-DETR `checkpoint_best_ema.pth` (142 MB), RT-DETR `best.pt` (264 MB), YOLO26l
`best.pt` (53 MB). Pengarsipannya ke penyimpanan objek belum dilakukan.

---

## 6. DEPTH-SENSOR-MVCD — blok E-022…E-032

Ini fase yang paling mahal dan **satu-satunya yang tidak menghasilkan perbaikan
apa pun**. Ia tetap ditulis penuh, karena hasil negatif yang tertutup rapat lebih
berharga daripada hasil positif yang goyah — dan karena separuh isi blok ini
adalah koreksi terhadap kesimpulan blok ini sendiri.

### 6.1 Dataset baru, dan mengapa angkanya tidak bisa dibandingkan

`ULM-DS-Lab/SawitMVC-Depth` — 352 pohon, 1.408 citra RGB **1280×800 lanskap**,
2.299 kotak B1–B4, plus **depth sensor Orbbec** Y16 848×480 uint16 milimeter per
citra. Integritas 6.336 artefak diverifikasi SHA-256: 0 hilang, 0 tidak cocok.

Inilah yang menutup lubang terbesar pilot: sampai E-021, **satu-satunya "depth"
yang pernah diuji adalah pseudo-depth monokular**, dan itu sudah dipalsukan
(§4.2). Depth sensor fisik belum pernah disentuh.

**Peringatan pembanding, mengikat.** Tidak satu pun angka di §6 sebanding dengan
test mAP50 0,6038 milik E-021:

| | SawitMVC (pilot) | SawitMVC-Depth |
|---|---|---|
| Anotasi | 18.540 kotak | 2.299 kotak |
| Orientasi | 960×1280 potret | 1280×800 lanskap |
| Prior kelas | B3 52,3% · B1 11,0% | B3 14,0% · B1 36,1% (**terbalik**) |
| Kepadatan | 4,64 kotak/citra | 1,63 kotak/citra |
| B4 | 148 kotak | **95 kotak** (38 di test) |

Satu-satunya klaim yang sah adalah **selisih antar lengan di dalam dataset ini
pada protokol identik**. Angka absolutnya tidak dapat dibawa keluar.

### 6.2 Tiga kegagalan senyap yang ditemukan lebih dulu

Sebelum satu pun klaim performa dibuat, tiga jebakan yang tidak menimbulkan error
sama sekali harus dibongkar. Ketiganya hanya ketahuan karena ada yang mustahil
secara definisi — bukan karena ada yang crash.

1. **Sidecar `"alignedTo": "color"` MENYESATKAN.** Buffer masih di grid kamera
   depth. Berkas yang sama membantah dirinya sendiri: ia mengirim ekstrinsik
   `mTrans ≈ −23,7 mm` yang mestinya nol bila benar sudah tersejajar. Tiga bukti
   independen (geometri intrinsik, tidak adanya pita kosong struktural yang
   diwajibkan selisih FOV, dan *mutual information* H3−H1 = **+0,0306 bit,
   CI95 [0,0260; 0,0354]**) mematahkan label itu. `cv2.resize` naif meleset
   **median 29,3 px, maksimum 61 px** — seukuran tandan B4 itu sendiri.
   Memakainya akan menghasilkan **hasil negatif palsu**, persis skenario D3Net
   (entri 037).
2. **Ada DUA unit kamera**, bukan satu (fx_depth 416,55 vs 414,38). Kalibrasi
   wajib dibaca **per berkas**; hardcode satu set = separuh dataset salah
   proses, dan biasnya berkorelasi dengan perangkat sehingga **bocor ke
   perbandingan antar-split**.
3. **Rentang metrik bawaan salah untuk sensor ini.** `fourch.py` memakai
   0,3–8,0 m; terukur 0,000% piksel di bawah 0,3 m dan 10,07% di atas 8 m.
   Dipilih ulang dari histogram **split train saja** (anti-kebocoran):
   **0,8 / 15,0 m**, entropi kanal naik 6,19 → **7,62 bit**.

Ditambah dua bug yang ditemukan audit *setelah* hasil pertama keluar: lengan
kontrol "depth pohon lain" mengambil donor **lintas split** (192 dari 980 citra
train memakai depth pohon **test**), dan lengan derau memakai satu RNG bersama
sehingga kanal ke-4 diacak ulang tiap epoch — ia diam-diam mendapat augmentasi.

**Pelajaran yang dibawa keluar:** pada blok ini, lima dari lima kesalahan serius
tidak menimbulkan satu pun pesan error. Itulah alasan E-032 memilih desain yang
kelemahannya **terlihat** (semua lengan dari nol) di atas desain yang lebih murah
tetapi gagal senyap.

### 6.3 Hasil pertama bertumpu pada satu seed — dan tidak bertahan

E-022 dilaporkan mula-mula pada seed 42 saja: Δ(RGB-D − RGB) = **+0,0252**,
melewati ambang +0,015 yang ditulis di depan. Tetapi CI95-nya
[−0,0215; +0,0632] memuat nol, sehingga H-022 sudah **DIPALSUKAN menurut
kriterianya sendiri** — kriteria yang ditulis sebelum hasil dibaca.

Replikasi multi-seed kemudian menunjukkan +0,0252 adalah **seed paling
menguntungkan dari tiga**:

| Kontras (YOLO26n, E-027) | seed 42 | seed 1337 | seed 2024 | rerata |
|---|---:|---:|---:|---:|
| depth − RGB | +0,0104 | **−0,0414** | **−0,0379** | **−0,0230** |
| derau − RGB | +0,0032 | +0,0011 | **−0,0443** | −0,0133 |
| depth − derau | +0,0072 | **−0,0425** | +0,0064 | −0,0096 |

Tebal = CI95 tidak memuat nol. **Untuk YOLO26n, depth bukan netral melainkan
merugikan** — dua dari tiga seed signifikan negatif.

Klausa penyelamat yang sempat ditulis SR-015 — *"depth terpakai pada kapasitas
tinggi"* — diuji terpisah pada RT-DETR-L (E-029) dan **DICABUT**: depth − derau
menyusut dari +0,0365 menjadi rerata +0,0124 dengan ketiga CI memuat nol, dan
B4 +0,1001 yang menjadi tulang punggungnya tidak direproduksi.

### 6.4 Yang bertahan justru temuan metodologis, bukan temuan depth

Tiga hasil di blok ini bertahan, dan ketiganya tentang **cara mengukur**, bukan
tentang kedalaman:

**(a) Protokol evaluasi (E-025).** `hasil.json` trainer dan `pycocotools` berbeda
hasil, dan celahnya **bukan offset tetap** — ia menskala dengan jumlah deteksi,
yang berbeda sistematis antar lengan. Hipotesis `maxDets` dipalsukan (identik
sampai lima desimal). Aturan yang kini mengikat: **`hasil.json` tidak boleh
dipakai membandingkan antar lengan.**

**(b) Varians split > varians seed (E-031).** Lengan RGB berayun **0,0488**
antar split — lebih lebar daripada 0,0321 antar seed, dan **hampir 5×** ambang
+0,015 yang dipakai H-022 sebagai kriteria keberhasilan. Konsekuensinya mengikat:
**tidak ada angka mAP absolut pada dataset ini yang bermakna tanpa menyebut
split-nya.** Yang berlawanan dengan dugaan wajar: *arah* Δ justru lebih stabil
terhadap split (3/3 positif) daripada terhadap seed (tanda berlawanan) — pola
yang konsisten dengan selisih berpasangan saling menghapus kesulitan split tetapi
tidak menghapus lintasan optimisasi. Itu **hipotesis dari n=3 lawan n=3**, bukan
temuan.

**(c) Ambiguitas terukur tanpa label manusia (E-024, E-026, E-028).** Memakai
identitas fisik tandan lintas-sisi sebagai oracle, detektor memberi kelas berbeda
pada objek yang sama sebesar **0,2329** di SawitMVC (511 tandan) dan 0,1951 di
SawitMVC-Depth (82 tandan) — sementara anotator manusia tidak pernah (0/7.328).
Tabrakannya meluruh rapi dengan jarak ordinal (79 → 32/25 → 12 → **0**) dan
**B2↔B3 dominan**, persis prediksi SR-007/SR-009 — diperoleh tanpa memakai label
kematangan sebagai kebenaran. Depth **tidak** menstabilkannya (E-026: +0,0049,
arah salah, P(depth membantu) = 0,457).

### 6.5 Kapasitas: klaimnya harus dipersempit (E-030)

SR-015 sempat menyimpulkan *"arah efek kanal ke-4 ditentukan kapasitas model"*.
Lompatan yang mendasarinya (YOLO26n 2,57 jt → RT-DETR-L 33,0 jt) mengubah
kapasitas **dan arsitektur sekaligus**, jadi kata "kapasitas" belum terisolasi.
Mengisi celahnya di dalam satu keluarga:

| Model | Param | depth − RGB | derau − RGB | depth − derau |
|---|---:|---:|---:|---:|
| YOLO26n | 2,57 jt | +0,0104 | +0,0032 | +0,0072 |
| YOLO26m | 21,9 jt | −0,0086 | +0,0184 | −0,0270 |
| YOLO26l | 26,3 jt | +0,0054 | **−0,0325** | +0,0379 |
| RT-DETR-L | 33,0 jt | −0,0350 | **−0,0533** | +0,0183 |

Yang **bertahan**: kolom derau − RGB berubah tanda secara monoton menurut
kapasitas, dengan titik balik terukur **antara 21,9 dan 26,3 jt parameter**.
Kanal ke-4 tanpa informasi membantu model kecil dan merugikan model besar.

Yang **tidak** bertahan: kolom depth − derau tidak monoton, dan tidak satu pun
dari keempatnya signifikan. Rumusan penggantinya:

> Kapasitas menentukan apakah **menambahkan kanal keempat** menolong atau
> merugikan. Kapasitas **tidak** menentukan apakah **mengisi kanal itu dengan
> kedalaman** lebih baik daripada mengisinya dengan derau.

### 6.6 Titik fusi: penjelasan terakhir yang diuji, tetapi belum menutup semua hipotesis (E-032)

Setelah fusi awal dipalsukan pada dua arsitektur dan tiga seed, satu penjelasan
tandingan masih berdiri: mungkin yang salah adalah **titik** fusinya — depth
dipaksa masuk sebelum jaringan sempat membentuk fitur. Ini hipotesis dengan dasar
pustaka yang kuat (sapuan 28 titik fusi Ophoff dkk., §174).

**5 lengan × 3 seed = 15 run, 150 epoch, semuanya dari nol.** Dari nol termasuk
baseline RGB — bukan penghematan, justru 3× lebih mahal — karena arsitektur dua
cabang tidak punya checkpoint COCO yang cocok, sehingga membandingkannya dengan
lengan pratlatih akan mengukur ada-tidaknya pralatihan, bukan titik fusi.

| lengan | seed 42 | seed 1337 | seed 2024 | rerata | rentang | putusan |
|---|---:|---:|---:|---:|---:|---|
| awal | −0,0120 | +0,0234 | −0,0017 | +0,0032 | 0,0354 | tidak berbeda |
| **mid** (P2/4) | +0,0096 | +0,0212 | +0,0110 | **+0,0139** | **0,0116** | **indikasi** |
| late (P3/P4/P5) | −0,0056 | +0,0070 | +0,0102 | +0,0039 | 0,0158 | tidak berbeda |
| derau | −0,0130 | +0,0025 | −0,0081 | −0,0062 | 0,0155 | tidak berbeda |

**Seluruh 12 CI95 memuat nol.** Kriterianya ditetapkan sebelum hasil dibaca.

Tiga pembacaan, berurut dari yang paling didukung bukti:

1. **Efek titik fusi lebih kecil daripada derau seed.** Rentang antar-seed pada
   lengan `awal` (0,0354) melampaui SELURUH selisih antar-titik yang terukur.
2. **Fusi akhir tidak menolong meski menambah parameter paling banyak** (3,00 jt
   vs 2,51 jt): dua backbone penuh, ~17% parameter tambahan, nol perbaikan.
3. **`mid` konsisten positif tetapi belum boleh disebut temuan.** Rentang
   tersempit, rerata tertinggi, unggul +0,0201 atas kontrol derau — pola yang
   diharapkan bila ia benar bekerja. Tetapi ketiga CI memuat nol, dan dengan
   4 lengan diuji, satu lengan bertanda sepakat 3/3 secara kebetulan **bukan
   kejadian langka**.

**Konsekuensi:** pada YOLO26n, satu split, 640 piksel, 150 epoch, dan
pelatihan dari nol, data tidak menunjukkan perbedaan yang dapat dibedakan
antar titik fusi. Itu mempersempit hipotesis dalam rezim ini, tetapi tidak
menutup pretrained middle/late fusion, kapasitas lain, split lain, atau data
lapangan. Kandidat yang tersisa meliputi kapasitas, kualitas depth itu sendiri,
dan ukuran data ([SR-015 §7b](SR/SR-015-depth-sensor-4kanal.md)).

### 6.7 Ringkasan blok: apa yang sebenarnya dibeli

| Pertanyaan | Jawaban setelah 11 entri |
|---|---|
| Apakah depth sensor fisik menaikkan deteksi? | **Belum terbukti** pada seluruh konfigurasi yang diuji |
| Apakah kegagalannya karena registrasi? | Tidak — registrasi divalidasi tiga cara |
| Apakah karena titik fusi? | E-032 tidak konklusif dalam rezim diuji; ekuivalensi belum dibuktikan |
| Apakah karena kapasitas model? | Sebagian, tetapi hanya untuk *ada-tidaknya* kanal ke-4, bukan untuk *isinya* |
| Apakah depth menstabilkan identitas lintas-sisi? | E-026 tidak konklusif karena denominator identitas berbeda |
| Apa yang tersisa sebagai kandidat penyebab? | Kualitas depth itu sendiri, ukuran data (980 citra latih), kapasitas |

Yang dibeli blok ini bukan perbaikan mAP, melainkan **penutupan jalur secara
meyakinkan** plus tiga instrumen yang bertahan: protokol evaluasi tunggal,
ukuran varians split, dan ukuran ambiguitas bebas-label.

---

## 7. Apa yang menunggu di depan

### 7.1 Yang sudah siap dan tidak hilang

- **[`reproduce/pipeline/`](../../reproduce/pipeline/README.md)** — pipeline produksi YOLO 4-kanal
  (RGB + depth) untuk kamera **Orbbec Gemini**. Satu bobot melayani dua mode uji
  lewat *modality dropout*: RGB+depth saat sensor terpasang, RGB saja saat tidak.
  Kontrak kanal keempat sudah dibekukan (PNG uint8, `0` = tidak ada data,
  `1..255` = *inverse depth* pada rentang metrik tetap 0,3–8 m). Integrasi ke
  aplikasi lapangan yang sudah ada = tiga baris (`Sawit4CH`). **Belum ada bobot
  terlatih.** Catatan penting setelah §6: rentang metrik bawaannya (0,3–8 m)
  **terbukti salah** untuk Orbbec Gemini pada kasus ini — pakai 0,8/15,0 m
  (§6.2), dan `prepare_depth.py` tidak boleh dipakai untuk data ber-sidecar
  seperti SawitMVC-Depth.
- **Dataset master 3024×4032** — dirakit dari peta isi E-015 (3.992/3.992 cocok,
  skor terendah 0,9985, nol ambigu), menunjuk ke piksel master penuh tanpa
  anotasi ulang karena rasio aspeknya identik (0,75). Belum dipakai melatih
  apa pun.
- **RF-DETR-L `checkpoint_best_ema.pth`** — model terbaik (§5.3), 142 MB.
  RT-DETR-L `best.pt` (264 MB) dan YOLO26l `best.pt` (53 MB) sebagai pembanding.

### 7.2 Register gerbang G0–G8 — dan satu yang masih terbuka

Blok depth sensor dikerjakan sebagai sembilan "gerbang" (celah yang harus
ditutup sebelum kesimpulan boleh dibuat). Daftar ini **belum pernah ditulis di
repo**; ia direkonstruksi dari judul entri dan pesan commit, dan dicatat di sini
supaya dapat diverifikasi.

| Gerbang | Isi | Ditutup oleh | Status |
|---|---|---|---|
| G0 | Penjaga kelengkapan run + tautan mati | `d58eae9` | **Terbuka pada snapshot kerja; manifest dan provenance perlu dirilis bersama source/PDF** |
| G1 | Selisih evaluator `hasil.json` vs pycocotools | E-025 | Asimetri terikat; mekanisme penuh belum terselesaikan |
| G2 | Matriks multi-seed, protokol tunggal | E-027 (YOLO26n) + E-029 (RT-DETR-L) | Tertutup untuk rezim diuji, bukan universal |
| G3 | Restrukturisasi E-022 + penyelarasan putusan SR-015 | `9c5d9dd`, `86f8e65` | Tertutup |
| G4 | Fusi menengah | E-032 | **Tidak konklusif; CI memuat nol, ekuivalensi belum dibuktikan** |
| G5 | Varians split | E-031 | Terukur pada tiga split; hukum populasi belum ditetapkan |
| G6 | Fusi akhir | E-032 | **Tidak konklusif; CI memuat nol, ekuivalensi belum dibuktikan** |
| G7 | Sapuan kapasitas dalam satu keluarga | E-030 | Eksploratori satu seed; tidak menutup klaim kapasitas |
| G8 | Ukuran lintas-sisi pada dataset berdaya uji layak | E-028 | Daya uji RGB meningkat; bukan perbandingan depth |
| **G7b** | **Monotonisitas kapasitas diuji multi-seed** | — | **TERBUKA** |

**G7b belum selesai dan tidak boleh dilupakan.** Commit `7afd274` membuka 12 run
tambahan (yolo26m/l × 3 modal × seed 1337, 2024) untuk menguji apakah
monotonisitas kolom derau − RGB (§6.5) bertahan multi-seed. Yang benar-benar
terjadi:

- **7 dari 12 run selesai dilatih** dan kurvanya terarsip (seed 1337 lengkap
  untuk yolo26m dan yolo26l; seed 2024 hanya `yolo26m_rgb`).
- **0 kontras berpasangan dihitung** — `paired_yolo26{m,l}_*` hanya ada untuk
  seed 42.
- **E-030 tidak pernah diperbarui**, sehingga keterbatasan "satu seed" yang
  ditulis di sana masih berlaku apa adanya.

Konsekuensinya jujur: klaim titik balik kapasitas **antara 21,9 dan 26,3 jt
parameter** tetap berstatus **pola satu-seed**, bukan temuan. Menyelesaikan G7b
menuntut 5 run sisa (~1 jam) plus evaluasi berpasangan — murah dibanding
nilainya, karena klaim inilah yang dipakai memilih arsitektur.

### 7.3 Jalur lanjutan, prioritas turun

1. **Selesaikan G7b** (§7.2) — 5 run + evaluasi. Termurah, dan menaikkan status
   satu klaim yang sudah dipakai mengambil keputusan.
2. **RF-DETR-L pada piksel master 3024×4032** (imgsz 1600–2048) — menyerang
   lokalisasi, penentu mAP50-95 yang sasarannya kini satu-satunya yang tersisa
   (−0,023). Taruhan terbaik menutup jarak itu.
3. **Kapasitas di atas mekanisme yang sudah terbukti** — RF-DETR pada varian
   lebih besar, atau RT-DETR-X (67,5 juta parameter).
4. **Optimasi latensi RF-DETR** (FP16 `optimize_for_inference`) — 8,5 FPS
   terlalu lambat untuk lapangan waktu-nyata; perlu diukur sebelum dipakai.
5. **Loss ordinal / kepala regresi kematangan (I-22)** — menyerang ketidakcocokan
   objektif-vs-metrik dari §4.4, dan belum pernah diuji di atas detektor terbaik.
6. **`mid` pada yolo26m/l** — satu-satunya arah depth yang masih punya dasar
   (§6.6 + §6.5), dan **hanya** kalau ada alasan lain melanjutkan jalur depth.
7. **Loss berimbang/focal (I-13), neck BiFPN (I-15)** — prioritas terendah.

### 7.4 Yang menunggu keputusan pengguna, bukan sekadar teknis

- **Apakah jalur depth diteruskan sama sekali.** Ini kini pertanyaan strategis,
  bukan teknis. Depth sensor fisik sudah diuji habis (§6) dan tidak membeli apa
  pun pada konfigurasi mana pun yang dicoba. Melanjutkan berarti bertaruh pada
  salah satu dari tiga kandidat penyebab yang tersisa — kualitas depth, ukuran
  data, kapasitas — dan masing-masing eksperimen tersendiri.
- **Brondolan lepas** sebagai penanda kematangan — kriteria panen lapangan yang
  sesungguhnya, tidak terlihat dari kanopi pada jarak foto ini. Ini mengubah
  **perumusan tugas**, bukan tuning, dan perlu persetujuan sebelum disentuh.

---

## 8. Batas klaim — yang tidak boleh dibaca berlebihan

Diringkas dari peringatan yang tersebar di log; semuanya mengikat.

1. **Pseudo-depth ≠ depth sensor.** Semua angka depth di **pilot** (§4.2) berasal
   dari model monokular, bersifat **relatif** (bukan metrik), dan galatnya
   berkorelasi dengan RGB sumbernya. Depth sensor fisik diuji terpisah di §6 —
   jangan mencampur kesimpulan keduanya.
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

Tambahan dari blok depth sensor — sama mengikatnya:

9. **Tidak ada angka E-022 yang boleh dikutip.** Seluruh entri bertumpu pada satu
   seed, dua lengan kontrol berkode cacat, dan evaluator yang kini terlarang
   untuk perbandingan antar lengan. Pakai E-027/E-029 sebagai gantinya.
10. **Angka SawitMVC-Depth tidak sebanding dengan SawitMVC.** Dataset, prior
    kelas, orientasi, dan kepadatan semuanya berbeda (§6.1). Yang sah hanya
    selisih antar lengan di dalam satu dataset.
11. **Setiap angka mAP pada SawitMVC-Depth wajib menyebut split.** Rentang
    antar-split 0,0488 melampaui hampir semua efek yang pernah diperdebatkan
    (§6.4b).
12. **`mid` (+0,0139) adalah INDIKASI, bukan temuan.** Ketiga CI memuat nol, dan
    dengan 4 lengan diuji satu tanda sepakat 3/3 bukan kejadian langka (§6.6).
13. **Titik balik kapasitas 21,9–26,3 jt masih satu seed.** G7b belum selesai
    (§7.2); jangan mengutipnya sebagai temuan multi-seed.
14. **"Depth tidak menolong" berlaku untuk yang diuji, bukan universal.** Yang
    diuji: fusi awal/menengah/akhir, YOLO26n/m/l + RT-DETR-L, 980 citra latih,
    satu sensor. Kualitas depth dan ukuran data belum terpisahkan sebagai
    penyebab.

---

## 9. Reproduksi

Kode eksperimen dijalankan di luar repo; snapshot kode, hasil JSON, dan split
diarsipkan di dalam repo bersama panduan reproduksi langkah demi langkah
(skrip → SR → keluaran, versi persis pustaka, dan celah yang diakui jujur).
Dataset: SawitMVC 960×1280 dan master 3024×4032, split per pohon 716/96/141
dengan irisan nol — invarian yang harus dijaga.

**Blok depth sensor** (§6) memakai SawitMVC-Depth, split per-pohon
terstratifikasi `(device × unit-kamera) × kelas-dominan`, 245/35/72 pohon,
irisan nol. Bukti terarsip: 39 kurva latihan + 37 kontras di
`evidence/experiments/results/E-022/`, 15 kurva latihan + 12 kontras di
`evidence/experiments/results/E-023/`. **Bobot tidak diarsipkan** (kebijakan
repo); sebagai gantinya tiap run menyimpan SHA-256 `best.pt`, sehingga hasil
latih-ulang dapat diverifikasi identik atau tidak.

Tiga jebakan yang wajib dibaca sebelum membangun ulang lingkungan — layout
`data/`, pin `opencv-python==4.11.0.86` dan `numpy==1.26.4` setelah ultralytics,
serta `reproject_depth.py --z-near 0.8 --z-far 15.0` — ada di
[STATUS.md](STATUS.md) §"Mulai dari nol setelah jeda".

Untuk deliverable produksi, seluruh perintah latih/konversi/inferensi ada di
[`reproduce/pipeline/README.md`](../../reproduce/pipeline/README.md).

---

*Cuplikan ini dikurasi 25 Juli 2026, diperluas ke E-032 pada 1 Agustus 2026.
Angka apa adanya, hasil negatif ikut dilaporkan — dan di blok §6, hasil negatif
adalah keseluruhan isinya. Bila ada selisih antara dokumen ini dan
[`docs/experiments/EKSPERIMEN.md`](EKSPERIMEN.md) / [`docs/experiments/METRICS.md`](METRICS.md), yang kanonik
adalah kedua berkas itu.*
