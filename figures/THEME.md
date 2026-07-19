# THEME — Spesifikasi Visual Figur GPT Image 2

Berkas ini adalah sumber kebenaran gaya untuk seluruh figur di `main.tex`.
Setiap brief di `figures/` tetap menjadi sumber fakta: node, edge, urutan,
angka, dan label di dalamnya tidak boleh berubah ketika aset dibuat ulang.

## 1. Prinsip editorial

- Figur adalah **ilustrasi inline** untuk jurnal, bukan slide presentasi.
- Dilarang menaruh judul global, subjudul, nomor gambar, caption, legenda
  dekoratif, atau footer di dalam artboard. Semua itu sudah disediakan oleh
  lingkungan `figure` dan caption LaTeX.
- Heading panel hanya boleh dipakai bila membedakan bagian yang benar-benar
  berbeda (misalnya dua pola arsitektur); heading tersebut harus pendek dan
  fungsional.
- Teks dibuat singkat, dengan ruang aman yang cukup; tidak boleh menyentuh,
  bertumpuk, terpotong, atau dilintasi panah.

## 2. Palet dan bentuk

| Peran | Warna | Pemakaian |
|---|---|---|
| Latar | `#FAF9F6` | kertas hangat penuh |
| Tinta | `#1A1D21` | teks, garis, dan panah |
| RGB | biru | sumber/alur RGB |
| Depth | emas-oker | sumber/alur kedalaman |
| Fusi dan hasil penting | merah bata | fusi, celah, atau hasil akhir |
| Bantuan | abu muda | kisi dan relasi opsional |

- Artboard lanskap 16:9 dengan ruang aman minimal 4% pada semua sisi.
- Node berupa kartu persegi panjang bersudut membulat; garis konsisten,
  panah kecil, dan tanpa garis yang tidak bermakna.
- Tampilan berwarna namun hemat: tanpa ilustrasi dekoratif, emoji, atau efek
  yang menurunkan keterbacaan.

## 3. Tipografi dan keterbacaan

- Gunakan satu keluarga sans-serif yang jelas dan konsisten pada seluruh
  label; istilah model dan angka diberi bobot yang cukup, bukan font berbeda
  yang sulit dibaca.
- Kontras teks harus tinggi terhadap latar, ukuran harus tetap terbaca ketika
  figur ditempatkan selebar kolom/judul jurnal.
- Teks wajib dicek secara visual pada PNG asli dan pada halaman PDF naskah.

## 4. Produksi dan aset kanonis

- Produksi final menggunakan **GPT Image 2** sebagai PNG lanskap, bukan SVG
  atau PDF buatan generator.
- Nama aset final yang dirujuk LaTeX: `figures/FNN-slug-gpt-image-2.png` dan
  `figures/CNN-slug-gpt-image-2.png`.
- Hasil generasi harus diperiksa sebelum dipakai: tidak ada salah eja,
  informasi yang hilang, label keluar artboard, panah bertabrakan, atau angka
  chart yang meleset dari brief.

## 5. Alur pemakaian

1. Baca berkas ini dan brief figur terkait.
2. Buat kandidat GPT Image 2 dengan fakta dari brief serta larangan judul
   internal.
3. Inspeksi gambar pada resolusi asli, lalu render kedua naskah LaTeX.
4. Pakai hanya aset yang lolos inspeksi; caption dan penomoran tetap dikelola
   LaTeX di luar gambar.
