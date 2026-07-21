# SR-006 — Penautan tandan lintas-sisi secara geometris

**Ide I-6 / I-7** · **Eksperimen:** E-007 · **Putusan: DIPALSUKAN** · 2026-07-21

---

## 1. Masalah

Satu tandan fisik terlihat dari beberapa sisi, sehingga menjumlahkan deteksi
seluruh sisi menghasilkan hitungan yang terlalu besar. Rasio duplikasinya
k = 1,8905 (14.041 kotak ÷ 7.427 tandan pada split latih).

DiB menangani ini secara **statistik**: bagi dengan k, atau taksir dengan SVR.
Keduanya menebak rata-rata populasi; keduanya **tidak tahu tandan mana yang sama
dengan tandan mana**. Naskah §208 menyebut kelemahan ini langsung: asosiasi
adalah "mekanisme yang mengubah deteksi per-frame yang baik menjadi hitungan
yang benar", dan penampilan saja rapuh di perkebunan tempat tandan bertetangga
terlihat serupa.

## 2. Ide

SR-004 sudah membuktikan DA3 memulihkan pose kamera 4/8 sisi dengan benar
(urutan melingkar benar 50/50). Kalau pose tersedia, dua deteksi dapat diuji
kesesuaian spasialnya di kerangka koordinat bersama: **tandan fisik yang sama
harus menempati titik 3D yang sama dari sisi mana pun ia dilihat.**

Penautan menjadi **geometris, bukan statistik** — dan identitas tandan
diturunkan sebagai komponen terhubung, persis cara dataset menurunkan
kebenaran-dasarnya.

Diuji sebagai **tangga ablasi** sesuai resep §208:

| Mode | Cara mencocokkan |
|---|---|
| A. hanya penampilan | kelas + kemiripan ukuran kotak |
| B. depth tanpa pose | kedalaman + posisi vertikal pada citra |
| C. sadar-pose (3D) | proyeksi balik ke 3D memakai pose & intrinsik DA3 |
| D. koreksi global k | pembanding publikasi |

**Yang akan memalsukan:** C tidak lebih baik daripada A/B/D.

## 3. Solusi

`experiments/geometric_linking.py`, 141 pohon split uji (140 punya pose).
Untuk tiap kotak: ambil median kedalaman di sekitar pusatnya, proyeksikan balik
ke 3D dengan `Xw = Rᵀ(d·K⁻¹[u,v,1] − t)`, lalu tautkan pasangan lintas-sisi yang
berjarak di bawah ambang. Identitas akhir = komponen terhubung (union-find).
Metrik identik dengan Tabel 4 DiB.

Ambang **disapu**, bukan dipilih sekali — karena kegagalan pada satu ambang
tidak boleh dianggap kegagalan ide.

## 4. Hasil

### Validasi perangkat — penting

Dua baris pembanding direproduksi **persis** dari publikasi:

| | Class±1 | Tree±1 | MAE | Bias |
|---|---|---|---|---|
| Jumlah mentah — skrip ini | 50,00% | 6,38% | 2,142 | +2,142 |
| Jumlah mentah — DiB Tabel 4 | 50,00% | 6,38% | 2,142 | +2,142 |
| Koreksi k — skrip ini | 95,57% | 86,52% | 0,356 | +0,009 |
| Koreksi k — DiB Tabel 4 | 95,57% | 86,52% | 0,356 | +0,009 |

Kecocokan digit-per-digit ini menetapkan bahwa pipeline evaluasinya benar,
sehingga angka di bawah adalah perbandingan yang sah.

### Sapuan ambang

| Mode | Ambang terbaik | Class±1 | Tree±1 | MAE |
|---|---|---|---|---|
| A. penampilan | 0,1 | **77,13%** | 32,62% | 0,876 |
| B. depth tanpa pose | 0,01 | 75,00% | 29,08% | 0,966 |
| **C. sadar-pose (3D)** | 1,0 | **69,50%** | 22,70% | 1,367 |
| D. koreksi global k | — | **95,57%** | 86,52% | 0,356 |

## 5. Putusan — DIPALSUKAN

Ketiga metode penautan **kalah telak** dari koreksi global yang sederhana, dan
metode geometris justru **paling buruk** di antara ketiganya (69,50% vs 77,13%
penampilan). Sapuan ambang menutup kemungkinan bahwa ini sekadar salah setelan:
pose diuji pada sembilan ambang dari 0,05 sampai 10,0.

### Kenapa gagal — dan batas dari klaim ini

Dua penjelasan yang tidak dapat dipisahkan oleh eksperimen ini:

1. **Kedalaman DA3 bersifat relatif, bukan metrik** (`is_metric` kosong), dan
   dinormalisasi per pohon. Proyeksi balik `d·K⁻¹[u,v,1]` mengasumsikan `d`
   adalah jarak sebenarnya. Dengan kedalaman relatif, titik 3D yang dihasilkan
   terdistorsi secara non-linear, sehingga jarak Euclidean antar titik tidak
   lagi bermakna. Skala intrinsik yang saya asumsikan (dari resolusi pemrosesan
   DA3) juga belum diverifikasi.
2. **Idenya memang tidak cocok di sini.**

Kejujurannya: eksperimen ini **memalsukan implementasi**, dan hanya melemahkan
— bukan menggugurkan — idenya. Untuk mengujinya dengan adil diperlukan
kedalaman **metrik** terkalibrasi (ide I-19: Metric3D entri 177 / ZoeDepth) dan
verifikasi intrinsik. Itu dicatat sebagai pekerjaan terbuka, bukan diklaim
sebagai sudah dijawab.

### Pelajaran yang lebih penting

Koreksi k = 1,8905 itu **sangat kuat** (95,57% / 86,52%). Penyebabnya struktural:
tandan per pohon sedikit (median 10) dan duplikasinya sangat teratur (1,887
rata-rata kemunculan). Metode penautan apa pun harus nyaris sempurna untuk
mengalahkannya.

**Konsekuensi strategis:** ruang perbaikan di tahap counting sudah tipis.
Bersama SR-005, ini mempersempit arah secara tegas — sisa perbaikan harus datang
dari **detektor**, persis kesimpulan DiB sendiri dan prioritas pertama
`docs/deep-research-report.md`.

## 6. Dampak

- I-6 dan I-7 dihentikan pada bentuk sekarang; dibuka kembali hanya bila
  kedalaman metrik tersedia (I-19).
- Prioritas bergeser ke ide yang menyerang detektor pada tandan kecil:
  **I-12 (pelatihan berbasis ubin)**, I-13 (loss berimbang kelas),
  I-15 (neck multiskala).

## 7. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python geometric_linking.py --split test           # tabel utama
.venv/bin/python geometric_linking.py --split test --sweep   # sapuan ambang
# keluaran: results/e007/report_test.json, results/e007/sweep.json
```

Prasyarat: `depth_da3/depth/*.png` dan `depth_da3/cameras_all.json` (dihasilkan
`gen_depth_dataset.py`). Tanpa GPU; beberapa menit.
