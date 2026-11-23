# Ruang Baca Riset

Katalog ini memuat kajian penghitungan buah berbasis citra serta kajian deteksi
objek dan sensor kedalaman. Cari judul, nama penulis, metode, DOI, atau kunci
BibTeX. Hasil muncul di bawah kolom pencarian. Di ponsel, buka Filter
untuk menyaring menurut koleksi, tema, atau tahun.

Buka judul kajian untuk mulai membaca Gambaran Umum. Pilih nama penulis untuk
mencari kajiannya, atau buka daftar penulis lain jika tersedia. Daftar isi
melompat ke bagian bacaan. Kajian terkait melompat ke saran lanjutan yang
menyertakan alasan berdasarkan rujukan atau kemiripan isi. Opsi PDF, sumber
asli, dan penyalinan ada di Sumber. Naskah, bahan tambahan, dan jalur baca
tersedia di Dokumen riset.

## Membuka situs dari salinan repo

Jalankan perintah berikut dari akar repositori.

```sh
node site/build.js
python3 -m http.server 8000 --bind 127.0.0.1
```

Buka [Ruang Baca Riset](http://127.0.0.1:8000/) di peramban. Server lokal
menyediakan ringkasan lengkap dan teks sumber Scopus saat pembaca membukanya.

## Memperbarui situs

Sunting susunan katalog, halaman kajian, dan dokumen di `app.js`. Warna dan
ukuran untuk tema terang dan gelap ada di `style.css`. Warna kuning kehijauan
menandai teks yang cocok dengan pencarian, bagian navigasi yang aktif, dan
kemajuan baca. Nomor di awal hasil menunjukkan posisi pada urutan saat ini.

Aturan pencarian dan saran kajian ada di `discovery.js`. `build.js` membaca
metadata dan isi dari korpus serta dokumen riset. Jalankan
`node site/build.js --dry` untuk memeriksa jumlah kajian dan tautan tanpa
menulis keluaran.

Rakit ulang [index.html](../index.html) dengan `node site/build.js` setiap
kali sumber situs, entri korpus, sintesis, laporan eksperimen, atau katalog PDF
berubah. GitHub Pages memakai berkas hasil rakitan di akar repositori.
