# Cek 5 — Pengodean Ulang Kajian Inti C1 dari Teks Lengkap

**Tenggat: 6 November 2026.** Disiapkan 29 September 2026.

## Tujuan

Kode 187 kajian inti C1 (`topik/bukti/mekanisme_C1.txt`) dibuat satu peninjau
dengan bantuan model bahasa besar, sebagian besar dari abstrak (145) atau judul
saja (42). Cek 5 memastikan setiap kode diperiksa manusia terhadap **teks
lengkap (PDF)** dan menambah enam kode baru yang hanya dapat dibaca dari teks
lengkap: sumber kode, lokasi hasil utama, acuan hitungan, tingkat metrik, cara
kelas ditetapkan, dan apakah kode berubah.

**Setiap nilai final adalah keputusan peninjau.** Kolom `draf_ai_*` hanya draf
model untuk mempercepat pencarian di PDF; jangan disalin tanpa membuka PDF.

## Berkas

| Berkas | Isi | Siapa yang mengisi |
|---|---|---|
| `verifikasi/kode_ulang_C1.csv` | Lembar kerja, satu baris per kajian C1 | skrip (kolom identitas, `kode_ai_*`, `draf_ai_*`, `catatan_skrip`) dan peninjau (`final_*`, `catatan_peninjau`) |
| `verifikasi/sampel_fatma_C1.csv` | 20 kajian C1 acak untuk cek buta Fatma | skrip (identitas) dan Fatma (`fatma_*`, `catatan_fatma`) |
| `verifikasi/log_perubahan.csv` | Log setiap sel yang berubah (dipakai bersama Cek 2) | skrip `--terapkan` |
| `tools/scopus/verifikasi_kode_ulang.py` | Pembuat lembar, pemindah nilai final, penarik sampel | — |
| `topik/bukti/mekanisme_C1.txt` | Sumber kode C1 (4 kolom lama + 6 kolom verifikasi opsional) | hanya lewat `--terapkan` |

Semua perintah dijalankan dari akar repo:

```bash
python3 tools/scopus/verifikasi_kode_ulang.py                 # buat/segarkan lembar
python3 tools/scopus/verifikasi_kode_ulang.py --terapkan --kering
python3 tools/scopus/verifikasi_kode_ulang.py --terapkan --oleh MZM
python3 tools/scopus/verifikasi_kode_ulang.py --sampel-fatma   # sudah dijalankan; lihat bawah
python3 tools/scopus/verifikasi_kode_ulang.py --banding-fatma
```

Menjalankan ulang skrip tanpa opsi aman: isian `final_*`, `catatan_peninjau`,
dan `draf_ai_*` dipertahankan (dicocokkan lewat `idx`); kolom lain dihitung ulang.

## Urutan kerja

Lembar sudah diurutkan menurut kolom `prioritas`, lalu kajian ber-PDF dahulu,
lalu tahun terbaru:

1. **Prioritas 1 (21 kajian)**: kajian yang angkanya dikutip di Tabel
   `tab:acq` (8) dan `tab:assoc` (13) naskah `main6`. Angka dan acuan di tabel
   itu harus cocok dengan PDF. Hanya 4 yang PDF-nya sudah ada; 17 lainnya ada di
   `unduhan/PRIORITAS-UNDUH-MANUAL.md` — unduh dahulu ke `pdf/<key>.pdf`, lalu
   jalankan ulang skrip agar `pdf_ada` dan `path_pdf` terisi.
2. **Prioritas 2 (42 kajian)**: C1 yang diputuskan dari judul saja
   (`dasar_keputusan = judul`). Periksa juga apakah kajian memang C1 (itu tugas
   Cek 2, `cek_C1.csv`); bila ternyata bukan C1, ubah keputusannya lewat Cek 2
   dan biarkan barisnya di sini tanpa `final_*`.
3. **Prioritas 3 (124 kajian)**: sisanya.

Untuk tiap baris: buka PDF → cari hasil utama (pakai `draf_ai_halaman` dan
cuplikan `draf_ai_bukti` dengan Ctrl+F) → isi kolom `final_*` → tulis alasan
singkat di `catatan_peninjau` bila ada kode yang berubah.

Lembar boleh dibuka di Excel. Simpan tetap sebagai CSV UTF-8; pemisah `,` atau
`;` (bawaan Excel berlokal Indonesia) sama-sama dibaca skrip.

## Kolom lembar

Kolom identitas (diisi skrip): `no`, `prioritas` (1/2/3; 9 = baris lama yang
kini bukan C1 tetapi sudah berisi isian peninjau), `alasan_prioritas`
(`tab:acq`, `tab:assoc`, `judul saja`), `idx`, `key`, `tahun`, `judul`, `doi`,
`dasar_keputusan` (`abstrak`/`judul`), `pdf_ada` (Y/N), `path_pdf`,
`teks_ada` (Y/N; ada `teks/<key>.txt`).

`kode_ai_mekanisme`, `kode_ai_akuisisi`, `kode_ai_per_kelas`,
`kode_ai_hasil_ringkas`: nilai yang **sekarang** ada di `mekanisme_C1.txt`
(kode model yang diminta dikonfirmasi).

Untuk setiap dari sepuluh kolom berikut ada pasangan `draf_ai_<kolom>` (draf
model) dan `final_<kolom>` (**kosong, milik peninjau**):

| Kolom | Arti | Nilai sah |
|---|---|---|
| `mekanisme` | Mekanisme asosiasi identitas | `M0`–`M5`, `DATA`, gabungan dengan `+` (mis. `M3+M4`) |
| `akuisisi` | Cara pengamatan berulang | `V` video lintasan, `D` beberapa pandang diskret, `S` pindaian 3D/awan titik, `T` kunjungan ulang antarwaktu, `1` satu pandang (satu nilai saja) |
| `per_kelas` | Jumlah **dilaporkan per kelas** (kematangan dsb.), bukan sekadar deteksi per kelas | `Y` / `N` |
| `hasil_ringkas` | Ringkasan hasil (bahasa Indonesia, tanpa TAB) | teks bebas |
| `sumber_kode` | Dasar kode final | `teks lengkap` / `abstrak` / `judul` |
| `halaman` | Tempat hasil utama di PDF | teks bebas, mis. `Tabel 4, h. 9` atau `Gbr. 7, h. 11`; nomor halaman = urutan halaman berkas PDF |
| `referensi_hitung` | Acuan pembanding jumlah | `pohon` (hitung tangan di pohon/tanaman), `panen` (hitungan atau bobot panen), `packhouse`, `anotasi` (citra/video beranotasi), `tidak ada`; gabungan dengan `;` |
| `tingkat_metrik` | Tingkat metrik yang dilaporkan | `hitung` (MAE, RMSE, R2, galat hitung), `identitas` (MOTA, IDF1, HOTA, ID switch), `deteksi` (mAP, AP, F1 deteksi), `tidak ada`; gabungan dengan `;` |
| `cara_kelas` | Hanya bila `per_kelas = Y`: kapan kelas ditetapkan pada buah yang dihitung | `saat pelacakan`, `sesudah pelacakan`, `voting antarpandang`, `tidak dinyatakan`; `-` atau kosong bila `per_kelas = N` |
| `berubah` | Apakah salah satu dari empat kode lama berubah | `tidak` / `ya (lama: kolom=nilai; ...)` |

Kolom lain: `draf_ai_bukti` (cuplikan verbatim ≤20 kata dari PDF untuk
dicari cepat; sudah dicek ada di teks), `draf_ai_catatan` (alasan draf dan hal
yang perlu dipastikan), `catatan_peninjau` (alasan perubahan; ikut ke kolom
`alasan` di log), `catatan_skrip` (peringatan, mis. kode sumber berubah sejak
lembar terakhir dibuat).

### Aturan pengisian `final_*`

- **Kosong** = tidak diubah (nilai di `mekanisme_C1.txt` dibiarkan).
- **`=`** = setuju: untuk empat kolom lama berarti mengonfirmasi `kode_ai_*`;
  untuk enam kolom baru berarti mengambil nilai `draf_ai_*` baris itu.
- Baris baru dianggap selesai dan diterapkan bila **`final_sumber_kode` terisi**.
  Baris dengan isian lain tetapi `final_sumber_kode` kosong dilewati.
- `final_berubah` boleh dikosongkan: skrip mengisinya sendiri (`tidak`, atau
  `ya (lama: ...)` berisi nilai lama). Bila diisi `tidak` padahal ada kode yang
  berubah, skrip berhenti.
- Bila PDF tidak dapat diperoleh, isi `final_sumber_kode` = `abstrak` atau
  `judul` dan tulis di `catatan_peninjau` sumber apa yang sudah dicoba.

## Draf model (dibuat 29 September 2026)

Semua 187 baris punya `draf_ai_sumber_kode`. Untuk **57 kajian** yang teks
lengkapnya ada (`teks/<key>.txt`), model membaca teks dengan pencarian kata kunci
dan pembacaan terarah per halaman PDF (`pdftotext`), lalu mengisi semua
`draf_ai_*`. Cakupan per prioritas: prioritas 1: 4 dari 21, prioritas 2: 1
dari 42, prioritas 3: 52 dari 124 (sisanya belum ber-PDF). Untuk 130 kajian
lain, `draf_ai_sumber_kode` hanya mencatat dasar kode saat ini (`abstrak`/`judul`).

Draf mengusulkan perubahan kode lama pada 8 kajian (lihat `draf_ai_berubah`):

| key | Usul | Alasan singkat (lihat `draf_ai_catatan`) |
|---|---|---|
| `arizasentis2025comparative` | akuisisi D → V | video UAV dilacak PointTrack (prioritas 1, `tab:acq`) |
| `tureckova2022slicing` | M3/V → M0/1 | satu citra lebar per baris, tanpa pelacakan; status C1 perlu Cek 2 |
| `lin2026tomato` | M3 → M2+M3 | StrongSORT memakai penampilan |
| `feng2024approach` | M3 → M2+M3 | DeepSORT + filter umur |
| `hu2023fruit` | M3 → M2+M3 | fitur penampilan SURF |
| `magalhaes2024monovisual3dfilter` | akuisisi V → D | pose kamera diskret |
| `hassan2025orange` | per_kelas Y → N | kelas diklasifikasi, tetapi jumlah hanya total |
| `ge2022tracking` | per_kelas Y → N | hitungan per kelas tidak dikuantifikasi |
Draf lain menandai hal yang perlu dicek tanpa mengusulkan perubahan, mis.
`torressanchez2021grape` (M4 dipertanyakan), `xia2022culling` (M2 atau M5),
`chen2026research` (status C1). Semua usul itu **draf**; peninjau memutuskan.

## Memindahkan nilai final ke `mekanisme_C1.txt`

`mekanisme_C1.txt` tidak disunting tangan untuk Cek 5. Pakai `--terapkan`:

1. `python3 tools/scopus/verifikasi_kode_ulang.py --terapkan --kering`
   menampilkan setiap sel yang akan berubah tanpa menulis apa pun.
2. `python3 tools/scopus/verifikasi_kode_ulang.py --terapkan --oleh MZM`
   (inisial peninjau) lalu:
   - memeriksa semua nilai terhadap kosakata di atas; bila ada satu galat,
     **tidak ada yang ditulis**;
   - menolak baris yang kodenya di `mekanisme_C1.txt` sudah berubah sejak lembar
     dibuat (mis. oleh Cek 2); jalankan ulang skrip tanpa opsi, periksa baris itu,
     lalu terapkan lagi;
   - menulis empat kolom lama dan enam kolom verifikasi ke baris `idx` yang
     sesuai di `mekanisme_C1.txt` (baris lain dan komentar tidak disentuh);
   - menambahkan satu baris per sel yang berubah ke `verifikasi/log_perubahan.csv`
     (`tanggal,berkas,idx_atau_key,kolom,nilai_lama,nilai_baru,alasan,oleh`;
     `berkas` = `topik/bukti/mekanisme_C1.txt`; `alasan` = `catatan_peninjau`
     atau "verifikasi teks lengkap (Cek 5)"). Pengisian pertama kolom verifikasi
     juga dicatat (nilai lama kosong). Header ditulis hanya bila berkas log belum ada;
   - menyegarkan lembar (`kode_ai_*` kini menunjukkan nilai baru).
   Menjalankan `--terapkan` dua kali tidak menulis apa pun untuk kedua kalinya.
3. Bangun ulang keluaran:

   ```bash
   python3 tools/scopus/kode_bukti.py
   python3 tools/scopus/gambar_tinjauan.py
   python3 tools/scopus/tabel_lampiran.py
   ```

   `kode_bukti.py` menambahkan kolom `sumber_kode`, `halaman`,
   `referensi_hitung`, `tingkat_metrik`, `cara_kelas`, `berubah` di ujung kanan
   `matriks_bukti.csv` begitu ada satu baris yang mengisinya (atau selalu,
   dengan `--kolom-verifikasi`). Sebelum itu matriks identik byte demi byte
   dengan versi sekarang. Gambar dan Lampiran A hanya membaca kolom lama.
4. Bila mekanisme, akuisisi, atau per_kelas berubah, angka di naskah `main6`
   (hitungan M0–M5, akuisisi, per kelas, Tabel `tab:acq`/`tab:assoc`),
   `PROTOKOL.md`, dan `AGENTS.md` §3 harus diperbarui (`AGENTS.md` §7).

Terapkan per kelompok (mis. setelah prioritas 1 selesai), jangan menunggu
seluruh 187 baris.

## Cek buta Fatma

`verifikasi/sampel_fatma_C1.csv` berisi 20 kajian C1 yang ditarik acak dengan
benih tetap 20261106 dari seluruh 187 C1, **tanpa** kode model maupun kode
peninjau. Sampel sudah ditarik sekarang agar tidak dipengaruhi urutan kerja;
jangan ditarik ulang (`--timpa` menghapus isian Fatma).

1. Fatma mengisi `fatma_*` dari PDF (atau DOI bila PDF tidak ada di repo) tanpa
   melihat `kode_ulang_C1.csv` maupun `mekanisme_C1.txt`.
2. Setelah peninjau menyelesaikan ke-20 baris itu, jalankan
   `--banding-fatma`. Yang dibandingkan: mekanisme (urutan gabungan diabaikan),
   akuisisi, per_kelas, referensi_hitung, tingkat_metrik, cara_kelas. Kajian
   yang belum diverifikasi peninjau dilaporkan terpisah.
3. **Bila lebih dari 3 dari 20 kajian berbeda**: cari penyebabnya (definisi
   kolom yang ditafsirkan berbeda, jenis kajian tertentu, sumber abstrak vs teks
   lengkap), perbaiki definisi di berkas ini bila perlu, lalu periksa ulang semua
   baris yang terkena pola yang sama, bukan hanya ke-20 sampel. Catat perubahan
   lewat `--terapkan` seperti biasa dan tulis ringkasan temuan di bawah.
4. Hasil (jumlah beda dari 20, per kolom) dilaporkan di naskah sebagai
   pemeriksaan antarpenilai pada sampel acak, sesuai `AGENTS.md` §7.

## Hubungan dengan Cek 2

`cek_C1.csv` (Cek 2) menanyakan apakah kajian benar C1 dan apakah kodenya benar.
Cek 5 memakai teks lengkap dan menambah kolom baru. Untuk kode yang sama,
keputusan Cek 5 (teks lengkap) menang. Bila Cek 2 mengubah `mekanisme_C1.txt`
lebih dulu, jalankan ulang skrip tanpa opsi; `catatan_skrip` menunjukkan kode
yang berubah dan `--terapkan` menolak baris itu sampai lembar disegarkan.

## Status

| Kelompok | Jumlah | Berdraf teks lengkap | Selesai (`final_sumber_kode` terisi) |
|---|---:|---:|---:|
| Prioritas 1 (`tab:acq`, `tab:assoc`) | 21 | 4 | 0 |
| Prioritas 2 (judul saja) | 42 | 1 | 0 |
| Prioritas 3 | 124 | 52 | 0 |
| **Total** | **187** | **57** | **0** |

Temuan cek Fatma: belum.
