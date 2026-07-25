# SR-009 — Kematangan itu kontinu, bukan empat kotak

**Ide I-18 → I-22** · **Eksperimen:** E-012 · **Putusan: DIKONFIRMASI** · 2026-07-21

---

## 1. Masalah

Dua kelas menyeret AP50 ke bawah, tetapi karena alasan yang berbeda —
dan SR-007 sudah membuktikan perbedaannya:

| Kelas | AP50 | Kontras latar (ΔE) | Tafsiran |
|---|---|---|---|
| B4 | 0,354 | **11,55** (di bawah kendali) | tidak terlihat |
| B2 | 0,433 | 18,48 (setara B1) | terlihat, tetapi **tertukar** |

B2 terlihat jelas dari latarnya, namun tetap gagal. Berarti kegagalannya ada di
tahap **membedakan kelas**, bukan menemukan objek.

SR-001 sudah mencoba mengukur ambiguitas ini lewat flag `class_mismatch` dan
gagal — nilainya nol karena ketidaksepakatan anotator sudah dikonsolidasikan
sebelum dataset dirilis. Pertanyaannya tetap terbuka: **seberapa besar
ambiguitas itu sebenarnya, dan bentuknya seperti apa?**

## 2. Ide

Hilangkan tahap deteksi sepenuhnya. Ambil potongan citra **tepat dari kotak
kebenaran-dasar**, hitung fitur penampilan, latih pengklasifikasi, lalu baca
matriks kebingungannya.

Kalau B2 dan B3 tetap tertukar meski kotaknya sudah diberikan secara sempurna,
maka ambiguitas itu melekat pada objeknya — bukan pada detektornya, dan bukan
sesuatu yang bisa diperbaiki dengan arsitektur deteksi apa pun.

Yang dicari bukan angka akurasinya, melainkan **bentuk kebingungannya**:

| Bentuk | Artinya |
|---|---|
| Kebingungan tersebar acak | fitur tidak memadai |
| Kebingungan antar kelas bersebelahan saja | variabel kontinu yang dipotong-potong |

## 3. Solusi

`experiments/class_separability.py`. Fitur sengaja **sederhana dan dapat
ditafsirkan** (37 dimensi: statistik LAB/HSV, varians Laplacian, besar gradien,
histogram hue) — tujuannya mengukur apakah sinyalnya ada dan bagaimana
bentuknya, bukan mengalahkan CNN. RandomForest 400 pohon berbobot seimbang,
6.000 potongan latih (1.500 per kelas), 1.377 potongan uji.

## 4. Hasil

Akurasi keseluruhan **52,87%** (tebak acak 25%).

| Sebenarnya \ Prediksi | B1 | B2 | B3 | B4 | Recall |
|---|---|---|---|---|---|
| **B1** | **177** | 44 | 15 | 16 | 70,2% |
| **B2** | 64 | **159** | 106 | 46 | **42,4%** |
| **B3** | 7 | 90 | **156** | 122 | **41,6%** |
| **B4** | 8 | 43 | 88 | **236** | 62,9% |

Kebingungan pasangan, sebagai persen dari kelas sebenarnya:

| Pasangan | % | Jarak ordinal |
|---|---|---|
| B3 → B4 | 32,5% | 1 |
| B2 → B3 | 28,3% | 1 |
| B3 → B2 | 24,0% | 1 |
| B4 → B3 | 23,5% | 1 |
| B1 → B2 | 17,5% | 1 |
| B2 → B1 | 17,1% | 1 |
| **B3 → B1** | **1,9%** (7/375) | **2** |

## 5. Putusan — DIKONFIRMASI

**Kebingungannya ordinal.** Enam kebingungan terbesar seluruhnya berjarak satu
langkah pada rantai B1→B2→B3→B4. Lompatan dua langkah nyaris tidak terjadi
(B3→B1 hanya 7 dari 375 kasus).

Ini tanda khas satu **variabel kontinu** — tingkat kematangan buah — yang
dipotong menjadi empat kotak. Batas antar kelas adalah garis buatan pada
rangkaian yang mulus, sehingga tandan yang kebetulan jatuh dekat garis itu
memang tidak punya jawaban benar yang tegas.

Ini juga menjelaskan kenapa kelas ujung (B1 recall 70,2%, B4 62,9%) jauh lebih
baik daripada kelas tengah (B2 42,4%, B3 41,6%): kelas ujung hanya punya satu
tetangga, kelas tengah punya dua.

### Batas klaim — jangan salah kutip

Angka 52,87% berasal dari fitur buatan tangan yang sengaja sederhana. Itu
**batas bawah** keterpisahan, bukan plafon sebenarnya; CNN hampir pasti lebih
baik. Yang transferable dari eksperimen ini adalah **struktur kebingungannya**,
bukan angka absolutnya. Menyajikan 52,87% sebagai "plafon akurasi kematangan"
akan menyesatkan.

## 6. Dampak

**I-22 — loss ordinal / kepala regresi kematangan.**

Ada ketidakcocokan yang belum tersentuh antara cara model dilatih dan cara ia
dinilai:

| | Perlakuan terhadap B2→B3 | Perlakuan terhadap B1→B4 |
|---|---|---|
| Pelatihan detektor (kategoris) | salah total | salah total |
| Metrik counting DiB (`Class ±1 Acc`) | **dianggap benar** | salah |

Metrik evaluasi DiB **sudah** mengakui sifat ordinal ini lewat toleransi ±1,
tetapi objektif pelatihannya belum: klasifikasi kategoris menghukum kesalahan
ke tetangga sama beratnya dengan lompatan jauh. Model karena itu menghabiskan
kapasitas untuk memisahkan hal yang metriknya sendiri tidak pedulikan.

Ini persis **"mismatch objective-ke-deployment"** yang disebut
`docs/deep-research-report.md` sebagai salah satu dari empat sumber plafon.

Bentuk konkret yang layak diuji:
1. Loss dengan bobot jarak ordinal (hukuman ∝ |kelas prediksi − kelas benar|).
2. Kepala regresi kematangan (keluaran kontinu 1–4), didiskretkan saat
   inferensi — cocok dengan sifat kontinu yang baru terukur.
3. Label smoothing yang hanya menyebar ke kelas tetangga.

**Catatan untuk B4:** SR-008 sudah menunjukkan B4 dapat dipisahkan lewat
tekstur. SR-009 menunjukkan B2/B3 tidak akan tertolong oleh tekstur maupun
kedalaman — masalahnya bukan keterlihatan. Dua kelas sulit ini menuntut dua
perbaikan yang berbeda, dan menggabungkannya sebagai "kelas sulit" akan
menyesatkan arah kerja.

## 7. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python class_separability.py --per-class 1500
# keluaran: results/e012/separability.json
```

Tanpa GPU. Beberapa menit.
