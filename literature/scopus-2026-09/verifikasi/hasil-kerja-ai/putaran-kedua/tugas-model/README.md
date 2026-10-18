# Keputusan Model atas Butir Verifikasi (19 Oktober 2026)

Peninjau menyerahkan keputusan semua butir `TUGAS.md` kepada model, kecuali
F.4 (kode buta manusia) dan 5.7 (bagian yang hanya dapat diisi penulis). Folder
ini memuat bahan dan hasilnya. Semua perubahan data sudah diterapkan dan dicatat
di `../../../log_perubahan.csv` dengan oleh = `AI-Tugas`.

## Cara kerja

1. **Aturan (Tahap 1).** Tiga agen tanpa konteks repo menjawab enam pertanyaan
   aturan dari teks protokol dan contoh rekaman saja
   (`aturan_tahap1_brief.md`, jawaban di `aturan_tahap1.json`). Agen utama
   menetapkan aturan akhir. Aturannya dicatat di `PROTOKOL.md` §4 dan di bagian
   metode naskah.
2. **Rekaman yang diperdebatkan (Tahap 2).** Sebanyak 87 rekaman dibaca ulang
   buta oleh dua agen Haiku 5.5 *effort* high, dengan agen ketiga sebagai
   penengah. Agen utama memeriksa setiap perbedaan dengan keputusan lama
   terhadap abstrak atau teks lengkap. Keputusan akhir yang mengubah sesuatu, atau
   yang menolak usul, ada di `keputusan_tahap2.csv` (40 baris). Yang mengubah
   kode ditulis ke `topik/penyaringan/abstrak_W00.txt` (26 baris).
3. **Label C1 dan C3.** Semua kajian C1 dan C3 dikode ulang buta dengan cara
   yang sama: `label_c1.csv` (107 kajian; sisanya kontrol yang sudah berlabel
   Cek 5) dan `label_c3.csv` (169 kajian). Label C1 diterapkan lewat kolom
   `final_*` di `cek-5-kode-ulang/kode_ulang_C1.csv`; label C3 langsung ke
   `topik/bukti/kode_C3.txt`.
4. **Cek fakta naskah.** Dua agen Haiku 5.5 per kajian yang dikutip, penengah
   bila berbeda, lalu agen utama memeriksa putusan salah dan sebagian benar.
   Putusan mentah ada di `cek_fakta_buta.json`; hasil akhirnya diisikan ke
   `cek-6-cek-fakta/cek_fakta.csv` dengan oleh = model.

Pembaca buta dan penyaring awal sama-sama model bahasa. Kecocokan antara
keduanya mengukur konsistensi prosedur, bukan penilaian independen.

## Keputusan per butir

| Butir | Keputusan |
|---|---|
| 1.1 | Rekonstruksi 3D, panorama, atau ortomosaik tempat buah dicacah: C1, M4. Gabungan hitungan dua citra atau lebih dengan aturan yang dipasang atau dipelajari: C1, M1; penjumlahan biasa: M0. |
| 1.2 | Makalah set data berkode C1 (DATA) bila memuat dua pengamatan atau lebih atas buah yang sama beserta kebenaran dasar penghubungnya. |
| 1.3 | Pelacakan berkode C1 hanya bila pelacakan atau hitungannya dievaluasi; selain itu E5 (`johnson2025agtech` tetap E5). |
| 1.4 | Kalibrasi atas hitungan yang sudah unik bukan M1. |
| 1.5 | Akuisisi S bila buah dideteksi atau dicacah di awan titik atau model 3D. T hanya bila identitas buah ditautkan antarkunjungan. |
| 1.6 | E7 hanya bila tidak ada judul dan abstrak berbahasa Inggris; artikel jurnal Mandarin dinilai menurut isinya. |
| 2.1–2.4, 2.7, 3.6, 4.2, F.2 | Lihat `keputusan_tahap2.csv`: 25 usul diterima, 1 sebagian, 14 ditolak. Hasil: 1.013 kajian Scopus. |
| 2.5 | Empat kajian dari daftar pustaka ditambahkan sebagai rekaman metode lain (L2–L5 di `topik/tambahan_metode_lain.csv`). Naskah menyebut bahwa yang ditelusuri hanya daftar pustaka lima tinjauan terdekat, dan bahwa keempatnya tidak masuk statistik kode. |
| 2.6 | Hamdani 2026 tetap kajian pencacahan, tetapi ditulis sebagai pencacahan buah di dalam tandan. Hutapea 2024 dan Hidayat 2024 tidak dihitung sebagai kajian pencacahan. |
| 3.1, 3.2, 3.5, 3.7, 4.3 | Diganti oleh kode ulang buta seluruh C1 (`label_c1.csv`), diterapkan lewat Cek 5. PDF jurnal CSAM dibaca sebagai citra halaman. |
| 3.3 | Semua laporan dihitung terpisah. Naskah menyebut bahwa satuan hitungnya laporan, dengan contoh pasangan Osman 2021 dan Roy 2019 / Dong 2020. |
| 3.4, 4.1 | Diganti oleh kode ulang buta seluruh C3 (`label_c3.csv`). |
| 4.4 | PDF `kang2022accurate` diganti dengan artikel yang benar, lalu teksnya diekstrak ulang. |
| 5.1–5.3 | Kalimat naskah diperbaiki; Q9 dinyatakan tanpa batas bidang subjek. |
| 5.4, 5.5 | Cek fakta seluruh baris kosong (cara kerja langkah 4). |
| 5.6 | Liu dan Ampatzidis tetap bertahun 2027 sesuai volumenya. Naskah menyebut terbit daring sebelum tanggal pencarian. |
| F.3 | `xie2023fruit` dan `hu2026calibration` tetap C1 menurut kode ulang buta. |

## Koreksi agen utama atas label buta

Label buta tidak diterapkan apa adanya bila teks sumber menunjukkan lain.
Alasannya ditulis di kolom `catatan_peninjau` pada `kode_ulang_C1.csv` dan di
`log_perubahan.csv`. Contohnya:

- `nenavath2024tree`: M1 D, karena mangga di sudut citra dikurangi; SORT hanya disebut
  di metode umum.
- `zhao2026adapting`: M4+M5.
- `cara_kelas` untuk empat kajian dikembalikan ke "saat pelacakan".
- `huang2024automatic` dan `ahmad2024enabling` keluar dari C1 menjadi C2.
