# Cek 1: Sampel Buta Penyaringan Korpus `main6`

Folder ini memuat bahan untuk memeriksa penyaringan yang dilakukan satu
peninjau dengan bantuan model bahasa besar (`../../PROTOKOL.md` §6). Berkas ini
menjelaskan **Cek 1: sampel buta penyaringan**. Cek 2 (pemeriksaan tangan
semua C1, C3, dan eksklusi) dijelaskan di [`CEK-TANGAN.md`](../cek-2-cek-tangan/CEK-TANGAN.md).

Rencana induknya, *Literature Review Verification Plan* dari Bu Fatma
(29 September 2026), disalin di [`rencana/index.html`](../rencana/index.html).

| Cek | Panduan | Lembar kerja |
|---|---|---|
| 1 Sampel buta | berkas ini | `sampel_judul`, `sampel_abstrak`, `kesepakatan.md` (keluaran skrip) |
| 2 Cek tangan | [`CEK-TANGAN.md`](../cek-2-cek-tangan/CEK-TANGAN.md) | `cek_C1`, `cek_C3`, `cek_eksklusi` |
| 3 Makalah dikenal | [`cek_makalah_dikenal.md`](../cek-3-makalah-dikenal/cek_makalah_dikenal.md) | `kandidat_snowballing.csv` |
| 4 Teks lengkap | [`PERMINTAAN-PDF.md`](../cek-4-teks-lengkap/PERMINTAAN-PDF.md) | `teks_lengkap.csv` |
| 5 Kode ulang C1 | [`KODE-ULANG.md`](../cek-5-kode-ulang/KODE-ULANG.md) | `kode_ulang_C1.csv`, `sampel_fatma_C1.csv` |
| 6 Cek fakta | [`CEK-FAKTA.md`](../cek-6-cek-fakta/CEK-FAKTA.md) | `cek_fakta.csv` |
| Semua | - | `../log_perubahan.csv` |

## 1. Tujuan dan urutan kerja

Cek 1 mengukur kesepakatan antara peninjau manusia dan penyaring AI
(persentase kesepakatan dan kappa Cohen) pada sampel acak, lalu mencari
rekaman penting yang terlewat. Angka kesepakatan akan dilaporkan di naskah,
sehingga **kolom keputusan manusia hanya boleh diisi manusia**. Skrip tidak
pernah mengisinya dan tidak boleh ada yang menebak isinya.

> **Kerjakan Cek 1 lebih dulu, sebelum membuka lembar Cek 2.** Lembar
> `cek_C1`, `cek_C3`, dan `cek_eksklusi` menampilkan keputusan AI untuk semua
> rekaman C1, C3, dan semua eksklusi tahap kelayakan. Setelah melihatnya,
> peninjau tidak lagi buta terhadap sampel abstrak. Bila Cek 2 sudah dibuka,
> catat hal itu di `kesepakatan.md` dan di naskah, atau serahkan Cek 1 kepada
> peninjau yang belum melihatnya.

Selama mengisi, **jangan membuka** berkas yang memuat keputusan AI:
`.kunci/`, `terbuka/`, `../../topik/penyaringan/` (`tahap_judul.csv`,
`kandidat_abstrak.csv`, `abstrak_*.txt`, `judul_*.txt`),
`../../topik/bukti/matriks_bukti.csv`, lembar `cek_*`, dan lampiran naskah
`main6`. Folder `.kunci` tidak otomatis tersembunyi di Windows.

## 2. Berkas

| Berkas | Isi |
|---|---|
| `sampel_judul.xlsx` / `.csv` | 300 rekaman acak dari populasi tahap judul (5.723) |
| `sampel_abstrak.csv` | 165 rekaman tahap abstrak yang dinilai peninjau, dari sampel acak 300 atas 1.143 rekaman (benih acak 20261004), beserta keputusan AI. Dua sampel yang tidak dipakai disimpan di `cadangan_sampel_abstrak_bersarang/` (62 rekaman yang bersarang di dalam 300 judul) dan `cadangan_sampel_abstrak_terpisah/` (100 dari 1.124) |
| `sampel_judul_manusia.xlsx` | Lembar isian asli peninjau untuk tahap judul; isinya sudah disalin ke `sampel_judul.csv` |
| `.kunci/kunci_judul.csv`, `.kunci/kunci_abstrak.csv` | Keputusan AI per `idx` (jangan dibuka sebelum selesai) |
| `.kunci/riwayat_sampel.csv` | Catatan setiap penarikan sampel: waktu, benih, n, populasi |
| `kesepakatan.md` | Kesepakatan, kappa, matriks, dan status lulus, dihitung 4 Oktober 2026. Keluaran `verifikasi_kappa.py --tulis`, yang membaca `sampel_judul.csv` dan `sampel_abstrak.csv` |
| `ketidaksepakatan.csv` | Semua rekaman yang berbeda keputusan, untuk diputuskan Fatma |
| `terbuka/` | Salinan lembar dengan kolom `keputusan_ai` terisi (dibuat skrip kappa) |
| `../log_perubahan.csv` | Log setiap perubahan pada berkas keputusan sumber |

Sampel ditarik oleh `tools/scopus/verifikasi_sampel.py` dengan **benih
20260929**: satu generator `random.Random(20260929)` menarik 300 judul lebih
dulu, lalu 100 abstrak. Menjalankan ulang skrip dengan benih yang sama
menghasilkan sampel yang persis sama. Urutan baris adalah urutan acak, bukan
urutan kueri.

Populasi:

- **Tahap judul (5.723)**: semua baris `tahap_judul.csv` (5.889 rekaman unik)
  dikurangi 166 baris `X0` yang dikeluarkan menurut tipe dokumen sebelum judul
  dibaca. Keputusan AI `I`, `M`, `R`, `T` berarti lanjut ke abstrak (1.124);
  `X` berarti eksklusi (4.599).
- **Tahap kelayakan (1.124)**: semua baris `kandidat_abstrak.csv`. Keputusan AI
  diambil dari `abstrak_*.txt` yang dibaca urut nama (00–08, B00–B03, T00);
  bila satu `idx` muncul lebih dari sekali, baris terakhir yang berlaku (aturan
  yang sama dengan `kode_bukti.py`). Per 29 September 2026 setiap `idx` hanya
  muncul sekali, jadi aturan itu belum pernah terpakai.

## 3. Cara mengisi

Isi berkas **`.xlsx`** (ada daftar pilihan dan teks terbungkus). CSV
disediakan sebagai cadangan. Jangan mengisi keduanya; bila keduanya berisi
keputusan, skrip kappa berhenti dan meminta `--sumber csv` atau `--sumber xlsx`.

Kolom yang diisi peninjau (berlatar kuning):

- `keputusan_manusia`: keputusan Anda sendiri, dari informasi di lembar.
- `catatan`: alasan singkat bila ragu, bila lebih dari satu kode cocok, atau
  bila abstrak tidak tersedia.
- `keputusan_final_fatma`: **biarkan kosong**; diisi Fatma hanya untuk
  ketidaksepakatan (lihat bagian 5).

Kolom `keputusan_ai` sengaja kosong di lembar isian.

### 3.1 Tahap judul (`sampel_judul`)

Putuskan **hanya dari judul, sumber, dan tahun**, seperti penyaringan aslinya.
Pertanyaannya: apakah judul ini layak dibaca abstraknya karena mungkin memenuhi
salah satu kode inklusi (bagian 3.3)? Bila ragu, pilih lanjut.

| Nilai | Arti |
|---|---|
| `Yes` (atau `L`) | Lanjut ke abstrak |
| `Yes-C1` (atau `L-C1`) | Lanjut, dan judul menunjukkan beberapa pengamatan buah yang sama (video, beberapa pandang, pindaian berulang) |
| `Yes-C3` (atau `L-C3`) | Lanjut, dan judul menyangkut pencitraan TBS kelapa sawit |
| `No` (atau `X`) | Eksklusi pada tahap judul |

`Yes-C1` dan `Yes-C3` dihitung sebagai "lanjut" dalam kappa. Keduanya dipakai
untuk aturan lulus (bagian 5), jadi tandai bila judul jelas mengarah ke C1 atau C3.

### 3.2 Tahap kelayakan (`sampel_abstrak`)

Putuskan dari judul, sumber, dan abstrak. Bila abstrak tidak tersedia, sel
`abstrak` berisi keterangan; putuskan dari judul dan sumber, lalu tulis
`tanpa abstrak` di `catatan`. Isi satu kode: `C1`–`C5`, `T`, `R`, atau
`X-E1` … `X-E7`. Penulisan `X E5` atau `XE5` diterima skrip, tetapi pakai
daftar pilihan bila bisa.

### 3.3 Kode inklusi (`PROTOKOL.md` §4)

| Kode | Arti |
|---|---|
| C1 | Metode yang menggabungkan beberapa pengamatan buah yang sama (video, beberapa pandang, pindaian berulang) |
| C2 | Pencacahan atau estimasi hasil dari satu pandang |
| C3 | Pencitraan TBS kelapa sawit, termasuk grading di pabrik dan brondolan |
| C4 | Atribut kelas (misalnya kematangan) disertai pencacahan dari citra tunggal |
| C5 | Deteksi, lokalisasi, atau pengukuran buah dengan depth, 3D, atau modalitas non-RGB (NIR, termal, LiDAR) |
| R | Tinjauan terdahulu |
| T | Metode yang dapat dipindahkan dari luar pertanian |

Protokol tidak menetapkan urutan prioritas bila lebih dari satu kode cocok.
Pilih kode yang paling menggambarkan kontribusi utama kajian dan tulis kode
lain yang juga cocok di `catatan` (misalnya `juga C3`).

### 3.4 Alasan eksklusi

| Nilai | Alasan |
|---|---|
| `X-E1` | Bukan buah pada tanaman |
| `X-E2` | Hanya pascapanen atau laboratorium |
| `X-E3` | Hasil panen dimodelkan tanpa mendeteksi buah |
| `X-E4` | Hanya pemetikan atau manipulasi (titik petik, pose genggam, manipulator) |
| `X-E5` | Buah dideteksi, tetapi tidak dicacah atau dievaluasi lebih lanjut |
| `X-E6` | Sensor bukan pencitraan (spektroskopi titik, e-nose, dielektrik, radar tunggal) |
| `X-E7` | Bukan bahasa Inggris |

Pedoman tambahan dari berkas penyaringan: SLAM atau navigasi kebun tanpa buah,
geometri tajuk atau batang, penyakit, dan suhu buah dikeluarkan; fusi RGB-D
untuk deteksi buah, lokalisasi atau pemetaan 3D buah yang dievaluasi, dan
estimasi ukuran buah di lapangan dengan depth, stereo, atau LiDAR dimasukkan.

## 4. Menghitung kesepakatan

Setelah **semua** baris terisi:

```bash
python3 tools/scopus/verifikasi_kappa.py            # membaca .xlsx bila terisi, selain itu .csv
python3 tools/scopus/verifikasi_kappa.py --sumber xlsx
```

Skrip menolak berjalan bila masih ada baris kosong, agar keputusan AI tidak
terbuka sebelum waktunya (`--izinkan-belum-lengkap` mematikan penjaga ini;
hindari). Keluaran:

- `kesepakatan.md`: n, persentase kesepakatan, kappa Cohen dengan selang 95%
  indikatif, matriks kebingungan, dan status Cek 1. Tahap judul dihitung biner
  (lanjut/eksklusi) beserta PABAK. Tahap kelayakan dihitung tiga kali: kode
  penuh (14 kategori), kode dengan semua X digabung (8 kategori), dan biner
  masuk/eksklusi.
- `ketidaksepakatan.csv`: setiap rekaman yang berbeda keputusan (tahap judul:
  berbeda lanjut/eksklusi; tahap kelayakan: berbeda kode atau alasan), rekaman
  kritis di atas. Isian `keputusan_final_fatma` dan `alasan_fatma` yang sudah
  ada dipertahankan saat skrip dijalankan ulang.
- `terbuka/`: salinan lembar dengan `keputusan_ai`. Lembar isian asli tidak diubah.

Kappa dihitung sendiri: κ = (p_o − p_e) / (1 − p_e), dengan p_o kesepakatan
teramati dan p_e kesepakatan harapan dari proporsi marginal kedua penilai.

## 5. Aturan lulus dan langkah bila gagal

**Lulus** bila sampel tidak memuat satu pun rekaman yang dikeluarkan AI tetapi
dinilai manusia C1 atau C3 (tahap judul: `L-C1` atau `L-C3` pada rekaman yang
dikeluarkan AI). Rekaman seperti ini ditandai `kritis = ya` di
`ketidaksepakatan.csv`.

Bila **gagal**:

1. Cari polanya: kueri asal, kata kunci judul, alasan eksklusi AI, dan apakah
   keputusan AI dibuat dari judul saja.
2. Periksa ulang **semua** rekaman berjenis sama di seluruh korpus, bukan hanya
   yang masuk sampel. Setiap keputusan yang berubah diubah di berkas sumbernya
   dan dicatat di `log_perubahan.csv`.
3. Tarik 300 judul tambahan dengan benih baru, tanpa `idx` yang sudah pernah
   disampel:

   ```bash
   python3 tools/scopus/verifikasi_sampel.py --tambah 300 --benih 20261006
   ```

   Skrip menulis `sampel_judul_tambah_<benih>.csv`/`.xlsx` dan kuncinya, serta
   menolak benih yang sudah dipakai. Isi lembar itu dengan cara yang sama, lalu
   jalankan ulang skrip kappa (semua lembar `sampel_judul*` dihitung).
   `--tahap abstrak` menarik tambahan dari tahap kelayakan dengan cara yang sama.

## 6. Tenggat

**6 Oktober 2026**: kirim ke Fatma angka kesepakatan (`kesepakatan.md`) dan
**semua** ketidaksepakatan (`ketidaksepakatan.csv`). Fatma mengisi
`keputusan_final_fatma` dan `alasan_fatma`. Bila keputusan final mengubah
keputusan korpus, ubah berkas sumbernya, catat di `log_perubahan.csv`,
jalankan ulang skrip `tools/scopus/`, lalu perbarui angka naskah dan
`PROTOKOL.md`.

## 7. Mencatat perubahan

`log_perubahan.csv` memakai kolom `tanggal, berkas, idx_atau_key, kolom,
nilai_lama, nilai_baru, alasan, oleh`. Satu baris untuk setiap nilai yang
diubah. Lembar sampel dan kunci tidak disunting setelah kappa dihitung; bila
ada salah isi, perbaiki lalu catat perbaikannya di log.
