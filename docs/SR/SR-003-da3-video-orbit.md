# SR-003 — DA3 multi-view pada video orbit pohon

**Ide I-1** · **Eksperimen:** E-003, E-004 · **Putusan: DIKONFIRMASI** · 2026-07-21

---

## 1. Masalah

Tim sudah menghabiskan seluruh ruang tuning (batch, hyperparameter, ukuran
input) dan angkanya tetap. Yang dibutuhkan perubahan arsitektur, bukan pencarian
hyperparameter. Kandidat terkuat dari korpus: menambahkan **kedalaman**.

Tetapi kedalaman monokular biasa (entri 175, DA V2) punya kelemahan yang
tercatat di entri 198: *"tidak menjamin konsistensi lintas pandangan — dua foto
dari sudut berbeda bisa memperoleh kedalaman yang saling bertentangan pada titik
3D yang sama."* Untuk dataset 4–8 sisi per pohon, ketidakkonsistenan itu fatal.

## 2. Ide

**Depth Anything 3** (entri 198, `lin2025depthanything3`, arXiv 2511.10647)
menerima sembarang jumlah pandangan dan menghasilkan geometri **konsisten
lintas-pandangan** plus pose kamera.

Uji pertama sengaja dilakukan pada **video**, bukan foto 4-sisi. Alasannya:
risiko terbesar rencana ini adalah *baseline* ~90° yang terlalu lebar untuk
rekonstruksi multi-view. Video orbit memberi ratusan frame dengan *baseline*
antar-frame kecil — kondisi paling menguntungkan. Kalau di sini pun gagal,
seluruh jalur geometris gugur lebih awal tanpa membakar jam GPU.

**Yang akan memalsukan:** rekonstruksi gagal, pusat kamera tidak membentuk orbit
masuk akal, atau peta kedalaman kanopi datar.

## 3. Solusi

Dua tahap.

**E-003** (`experiments/da3_video_test.py`) — satu video, 16 dan 48 frame.
Diagnosa: PCA pusat kamera → kecocokan lingkaran pada bidang orbit; rentang
dinamis kedalaman; pratinjau RGB|depth|conf untuk inspeksi mata.

**E-004** (`experiments/da3_video_multi.py`) — menuntaskan tiga keterbatasan
E-003: 6 video (bukan 1), ekstraksi frame lewat **ffmpeg** yang menerapkan
display matrix (`cv2` mengabaikannya; video terkonfirmasi memuat
`displaymatrix: rotation of -90.00 degrees`), dan pengukuran **di mana** orbit
berhenti mulus berikut korelasinya dengan mutu frame.

Metrik utama: `smooth_frac` = pecahan frame di dalam sapuan orbit searah
terpanjang (langkah searah, besar ≤40°).

## 4. Hasil

### E-003 — satu video, frame miring

Cepat: 16 frame dalam **2,2 detik** (0,14 dtk/frame, GPU L4). Keluaran
`Prediction` memuat `depth`, **`conf` per piksel**, `extrinsics` (N,3,4),
`intrinsics`. `is_metric` kosong → kedalaman **relatif**, bukan metrik.

Orbit: cakupan 319,7°, residual lingkaran 8,2%. Tetapi langkah sudut mulus hanya
pada indeks 0–30, lalu kacau (−77°, +54°, +89°, −76°).

Dua sub-hipotesis penyebab diuji dan **keduanya dipalsukan**:

| Dugaan | Uji | Hasil |
|---|---|---|
| Operator berhenti → *baseline* kecil | Ukur perpindahan pusat kamera | **Salah** — ekor justru 2,2× lebih besar |
| Sampling terlalu jarang | Rapatkan 16 → 48 frame | **Salah** — batas kegagalan tidak bergeser |

### E-004 — enam video, rotasi diperbaiki

| Video | `smooth_frac` | Sapuan mulus | Residual lingkaran | Kerataan |
|---|---|---|---|---|
| 090556 | 41% | 149° | 2,4% | 0,098 |
| 091514 | **100%** | 331° | 3,6% | 0,020 |
| 092017 | 97% | 335° | 3,3% | 0,049 |
| 092548 | **100%** | 362° | 4,1% | 0,041 |
| 093119 | **100%** | 379° | 5,7% | 0,025 |
| 094046 | **100%** | 385° | 7,0% | 0,034 |

`smooth_frac` rata-rata **90%**, median **100%**; **5 dari 6** video mencapai
sapuan ≥270°.

Uji sebab pada frame di luar segmen mulus: **ketajaman justru lebih tinggi**
(7.725 vs 6.526), kecerahan dan gerak hampir sama. Jadi blur, pencahayaan, dan
gerak **bukan** penyebabnya.

## 5. Putusan — DIKONFIRMASI

DA3 merekonstruksi orbit pohon sawit secara andal pada 5 dari 6 video, dengan
sapuan mendekati lingkaran penuh dan pusat kamera yang hampir sebidang.
Kedalaman memisahkan pelepah satu per satu dari latar, dan **tandan buah terlihat**
(gugusan B1 merah pada frame 8 E-003).

E-003 mengukur satu video yang kebetulan bermasalah. Koreksi oleh E-004 persis
alasan keterbatasan `n=1` dicatat sejak awal, bukan disembunyikan.

**Sebab kegagalan video 090556 masih belum diketahui** — tiga kandidat sudah
dipalsukan. Tidak dikarang penjelasan untuk sisa satu video ini.

## 6. Dampak

- Fondasi untuk **I-6** (penautan geometris) dan **I-7** (asosiasi sadar-pose)
  tersedia dan terverifikasi.
- Keandalan **tidak universal** (1 dari 6 gagal) → **I-8** (gerbang mutu depth)
  bukan hiasan melainkan syarat.
- Peta `conf` yang dikembalikan DA3 adalah sinyal gating yang diminta SA-Gate
  (entri 055) dan D3Net (entri 037), tersedia tanpa perlu dibangun sendiri.
- Berlanjut ke **SR-004**: apakah ini bertahan pada foto 4-sisi berbaseline
  lebar? Keberhasilan pada video **tidak** menjawab itu.

## 7. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python da3_video_test.py --frames 16          # E-003
.venv/bin/python da3_video_test.py --frames 48 --out results/e003b
.venv/bin/python da3_video_multi.py --videos 6 --frames 32              # E-004
.venv/bin/python da3_video_multi.py --videos 6 --frames 32 --no-rotate  # pembanding
```

Lingkungan: GPU NVIDIA L4, `depth-anything/da3-large`, `process_res=504`,
torch 2.8.0+cu128. Waktu jalan E-004: beberapa menit.
