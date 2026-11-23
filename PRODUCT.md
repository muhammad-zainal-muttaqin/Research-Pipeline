# Produk: Ruang Baca Riset

<!-- impeccable:product-schema 1 -->

## Platform

web

## Pengguna

Pembaca yang mencari rujukan tertentu atau menelusuri topik dapat memakai
katalog dari ponsel maupun komputer. Kelompok pembaca utama belum ditetapkan.

## Tujuan produk

Ruang Baca Riset menyediakan ringkasan kajian penghitungan buah berbasis
citra, deteksi objek, dan sensor kedalaman. Pembaca dapat mencari rujukan,
menilai relevansinya dari ringkasan, lalu membuka sumber atau kajian terkait.

## Cara penelusuran

Katalog menyediakan pencarian judul, nama penulis, topik, dan DOI, serta
penyaringan menurut koleksi, tema, dan tahun. Tautan nama penulis membuka
hasil pencarian atas nama itu. Saran kajian terkait menyertakan alasan dari
rujukan dalam ringkasan atau kemiripan isi. Naskah, bahan tambahan, dan jalur
baca tersedia di Dokumen riset.

## Kebutuhan di ponsel

Kolom pencarian dan hasil pertama terlihat saat katalog dibuka. Kalimat awal
ringkasan mulai terbaca saat halaman kajian dibuka. Daftar isi, daftar nama
penulis, dan kajian terkait tetap mudah dijangkau.

## Sumber isi

Ringkasan berasal dari `literature/entries/` dan
`literature/scopus-2026-09/entri/`. `node site/build.js --dry` melaporkan
jumlah kajian berdasarkan isi kedua koleksi. GitHub Pages menyajikan
`index.html` yang dirakit dari sumber di `site/`.
