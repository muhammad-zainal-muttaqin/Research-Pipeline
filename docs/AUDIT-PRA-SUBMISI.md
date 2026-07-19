# Audit Pra-Submisi Naskah

**Tanggal audit:** 19 Juli 2026  
**Cakupan:** `main.tex`, `main-elsarticle.tex`, `body.tex`, `references.bib`,
artefak PDF, dan spesifikasi figur pada `figures/`.

Dokumen ini mencatat pemeriksaan mekanis yang dapat dilakukan pada lingkungan
lokal saat ini. Dokumen ini bukan pengganti verifikasi ilmiah terhadap makalah
sumber atau pedoman jurnal tujuan.

## Ringkasan status

| Area | Status | Bukti / tindak lanjut |
|---|---|---|
| Dua driver naskah | Siap ditinjau | `main.tex` (IEEEtran) dan `main-elsarticle.tex` (elsarticle) sama-sama memuat `body.tex`, sehingga isi utama tidak bercabang. |
| Artefak PDF | Perlu dibuat ulang | `main.pdf` (22 halaman) dan `main-elsarticle.pdf` (71 halaman) ada di root repositori, tetapi masih merender placeholder figur. Metadata pembuatannya juga perlu divalidasi ulang setelah kompilasi bersih. |
| Pemeriksaan objek Git | Lulus | `git fsck --no-reflogs --no-dangling` selesai tanpa temuan. |
| Kompilasi lokal | Belum dapat dijalankan | `pdflatex` tidak tersedia pada lingkungan audit ini. Kompilasi bersih perlu dilakukan di Overleaf atau instalasi TeX yang lengkap. |
| Figur final | Menghalangi submisi | `figures/` hanya memuat 10 brief Markdown; tidak ada `*.pdf`/`*.png` hasil render. Semua 10 panggilan `\figplace` memakai placeholder pada PDF saat ini. |
| Metadata penulis | Menghalangi submisi | Nama penulis, pembimbing, afiliasi, alamat, kota, dan email pada kedua driver masih berupa placeholder. |
| Sitasi dan BibTeX | Lulus pemeriksaan struktural | 202 kunci sitasi unik di `body.tex` persis cocok dengan 202 entri BibTeX unik: tidak ada kunci hilang, entri tak tersitasi, atau label duplikat. Verifikasi metadata terhadap sumber primer tetap manual. |

## Temuan yang sudah diperbaiki otomatis

- `figures/F01-taksonomi.md` sekarang menegaskan bahwa angka pada klaster
  **tidak boleh dijumlahkan**: satu karya dapat muncul pada lebih dari satu
  klaster. Instruksi prompt figurnya juga meminta catatan kaki yang sama.
  Penjelasan ini mencegah pembaca menafsirkan total badge sebagai jumlah
  korpus.

## Validasi struktural naskah

Pemeriksaan statis menemukan 247 kelompok perintah sitasi yang mereferensikan
202 kunci unik. Semua kunci tersebut ada pada `references.bib`, dan tidak ada
entri BibTeX yang tidak dipakai oleh isi naskah. Struktur float juga seimbang:
6 `figure`, 4 `figure*`, 2 `table`, dan 1 `table*`. Dari 24 label unik, seluruh
22 kunci `\ref` dapat diurai dan tidak ada label ganda.

Kedua driver juga memakai judul dan abstrak identik (abstrak: 1.519 karakter),
sehingga pilihan template tidak menimbulkan perbedaan isi. Pemeriksaan indeks
korpus dengan `node build.js --dry` lulus: 202 entri, 17 tema, rentang
2012–2026, dan 14 tahun terisi, tanpa peringatan serta tanpa menulis
`index.html`.

## Temuan penghalang sebelum pengajuan

### 1. Render seluruh figur ke PDF vektor

Spesifikasi figur tersedia pada `figures/F01-taksonomi.md` sampai
`figures/F08-pipeline-sawit.md` serta `figures/C01-distribusi-tahun.md` dan
`figures/C02-distribusi-tema.md`. Namun, driver LaTeX hanya memasukkan berkas
`figures/<label>.pdf`; jika berkas tersebut tidak ada, makro `\figplace`
menampilkan kotak placeholder. Buat dan simpan berkas berikut sebelum
kompilasi final:

```text
figures/F01-taksonomi.pdf            figures/F06-atensi-lintasmodal.pdf
figures/F02-timeline-yolo.pdf        figures/F07-funnel-sawit.pdf
figures/F03-silsilah-rgb.pdf         figures/F08-pipeline-sawit.pdf
figures/F04-strategi-fusi.pdf        figures/C01-distribusi-tahun.pdf
figures/F05-pola-yolorgbd.pdf        figures/C02-distribusi-tema.pdf
```

Semua placeholder telah terverifikasi pada PDF yang dilacak: `main.pdf` halaman
2, 5, 7, 9, 13, 14, 16, dan 17; `main-elsarticle.pdf` halaman 5, 11, 15, 23,
24, 35, 39, 40, 43, dan 44. Static check tidak menemukan marker literal `??`
atau label/referensi figur yang tidak cocok. Setiap artefak harus tetap ditinjau
secara visual: keterbacaan ukuran teks, kontras, ejaan label, nomor gambar, dan
kesesuaian dengan caption di `body.tex`.

### 2. Ganti seluruh placeholder identitas

Sebelum pengajuan, ganti setidaknya:

- `Nama Penulis`, `Nama Pembimbing`, program studi, dan email pada `main.tex`;
- nama, afiliasi, alamat institusi, kota, serta negara pada
  `main-elsarticle.tex`.

### 3. Lakukan kompilasi bersih empat langkah

Setelah figur dan metadata final tersedia, jalankan dari root repositori:

```text
pdflatex main
bibtex main
pdflatex main
pdflatex main

pdflatex main-elsarticle
bibtex main-elsarticle
pdflatex main-elsarticle
pdflatex main-elsarticle
```

Audit log harus memastikan tidak ada `Undefined references`, `Citation ...
undefined`, `Overfull \\hbox` yang mengganggu, atau kegagalan pemuatan figur.

## Pemeriksaan manual yang masih wajib

1. Baca ulang abstrak, simpulan, dan semua klaim komparatif untuk memastikan
   setiap generalisasi benar-benar ditopang sitasi primer.
2. Pilih satu target jurnal sebelum mengubah format akhir; driver IEEEtran dan
   elsarticle tidak boleh dikirim bersamaan.
3. Cocokkan judul, abstrak, kata kunci, batas kata, gaya referensi, deklarasi
   konflik kepentingan, kontribusi penulis, dan pernyataan data dengan panduan
   jurnal yang dipilih.
4. Buka PDF final per halaman dan periksa pemenggalan tabel, orientasi figur,
   placeholder, sitasi, serta nomor halaman.
5. Putuskan status `tinjauan-pustaka.tex`: berkas tersebut adalah draf mandiri
   lama dan tidak diinput oleh `main.tex` maupun `main-elsarticle.tex`. Isinya
   tidak identik dengan `body.tex`, sehingga jangan gunakan sebagai sumber
   pengajuan tanpa rekonsiliasi atau pengarsipan yang disengaja.
6. Tinjau ulang kalibrasi klaim abstrak terhadap isi: naskah membatasi ketiadaan
   dataset sawit RGB--D pada korpus yang ditinjau dan memosisikan fusi tingkat
   menengah yang sadar kualitas sebagai hipotesis teruji, bukan superioritas
   universal. Terminologi kedalaman monokular juga perlu membedakan
   *pseudo-depth* dari kedalaman metrik/fisik.
7. Samakan unit objek utama (`buah` atau `tandan buah`) pada judul, abstrak,
   kata kunci, dan isi. Bila naskah diposisikan sebagai *systematic review*,
   lengkapi tanggal pencarian, kueri, kriteria seleksi/eksklusi, alur
   penyaringan, serta penilaian kualitas sumber.
8. Rekonsiliasi taksonomi empat poros pada Gambar F01 dengan enam kelompok pada
   `tab:taksonomi`. Jika tabel adalah pengelompokan tingkat kedua, ubah nama
   kolom atau tambahkan kalimat yang menjelaskan hubungan hierarkisnya agar
   pembaca tidak menafsirkannya sebagai dua taksonomi yang saling bertentangan.
9. Perjelas kolom `\approx Entri` pada `tab:taksonomi`. Isi selnya berupa nomor
   atau rentang nomor entri, bukan jumlah perkiraan; ganti judul kolom menjadi
   nomor/rentang entri atau hitung jumlah sebenarnya secara konsisten.
10. Seragamkan tahun YOLOv7. Indeks, C01, dan `body.tex` memakai 2023, sementara
    `TEMUAN.md` serta draf lama memakai 2022. Tetapkan apakah konvensi naskah
    mengikuti tahun pracetak atau publikasi konferensi, lalu dokumentasikan dan
    terapkan secara konsisten.

## Catatan reproduksibilitas

Repositori tidak menyimpan instalasi TeX, `latexmk`, skrip build, lockfile
lingkungan, maupun log kompilasi. Kelas dan gaya bibliografi juga dipasok oleh
distribusi TeX eksternal. Selain itu, PDF yang dilacak menunjukkan produser
XeTeX/dvipdfmx, sedangkan komentar driver mendokumentasikan alur `pdflatex` dan
BibTeX; provenance PDF saat ini karenanya tidak dapat dibuktikan dari
repositori. Setelah target jurnal dan lingkungan TeX disepakati, tambahkan
perintah build kanonis serta CI yang menjalankan kompilasi bersih dan gagal
apabila placeholder figur atau referensi tak terselesaikan masih ada.
