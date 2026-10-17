# Daftar Istilah

Arti kode yang muncul di lembar pemeriksaan dan di [TUGAS.md](TUGAS.md).
Definisi resmi ada di [`PROTOKOL.md`](../PROTOKOL.md) bagian 4 dan 5.

## Kelompok artikel

Setiap artikel yang masuk tinjauan diberi satu kelompok.

| Kode | Arti | Jumlah |
|---|---|---:|
| C1 | Menghitung buah dari beberapa pengamatan buah yang sama: video, beberapa sisi pohon, atau pindaian berulang. Kelompok inti tinjauan | 195 |
| C2 | Menghitung buah atau memperkirakan hasil panen dari satu foto | 238 |
| C3 | Pencitraan tandan sawit, termasuk penilaian mutu di pabrik dan brondolan | 176 |
| C4 | Menghitung buah per kelas (misalnya per tingkat kematangan) dari satu foto | 49 |
| C5 | Mendeteksi atau mengukur buah dengan kamera depth, 3D, atau sensor selain kamera biasa | 135 |
| R | Artikel tinjauan pustaka lain | 120 |
| T | Metode dari luar pertanian yang dapat dipakai untuk buah | 88 |

Dua aturan Bu Fatma (5 Oktober 2026):

- **Stereo.** Sepasang foto stereo dihitung satu pengamatan, jadi masuk C5,
  bukan C1. C1 hanya bila buah dihubungkan antarfoto atau antarposisi kamera.
- **Prioritas.** Bila artikel cocok untuk beberapa kelompok, C1 didahulukan.

## Alasan artikel dikeluarkan

| Kode | Artinya, artikel ini... |
|---|---|
| E1 | bukan tentang buah yang masih di tanaman |
| E2 | hanya pascapanen atau laboratorium |
| E3 | memperkirakan hasil panen tanpa mendeteksi buah satu per satu |
| E4 | hanya membahas pemetikan oleh robot |
| E5 | mendeteksi buah tanpa menghitung atau mengevaluasi hasilnya |
| E6 | memakai sensor yang bukan kamera |
| E7 | tidak berbahasa Inggris |

## Label artikel C1

Setiap artikel C1 diberi tiga label: mekanisme, akuisisi, dan per kelas.

**Mekanisme**, yaitu cara artikel memastikan buah yang sama tidak terhitung dua kali:

| Kode | Arti |
|---|---|
| M0 | Tidak ada usaha menghubungkan buah antarfoto |
| M1 | Koreksi statistik, misalnya faktor pengali atau regresi |
| M2 | Mencocokkan penampilan buah (*re-identification*) |
| M3 | Melacak buah dari *frame* ke *frame* video |
| M4 | Mencocokkan posisi buah dalam ruang 3D |
| M5 | Pencocokan yang dipelajari model |
| DATA | Artikel yang merilis *dataset* |

Gabungan ditulis dengan tanda tambah, misalnya M3+M4.

**Akuisisi**, yaitu cara foto diambil: V video sepanjang lintasan; D beberapa foto
dari posisi terpisah; S pindaian 3D atau awan titik; T kunjungan ulang pada
waktu berbeda; 1 satu foto.

**Per kelas**: Y bila hitungan dilaporkan per kelas, misalnya per tingkat kematangan.

## Label artikel C3

| Label | Pilihan |
|---|---|
| Tugas | KLS menilai kematangan; DET mendeteksi tandan; HIT menghitung; LF brondolan; MUTU cacat, minyak, massa, atau volume; SENSOR sensor non-RGB; DATA *dataset* |
| Lokasi | POHON; TANAH (tanah atau TPH); PABRIK (pabrik, konveyor, laboratorium); UAV; ? tidak jelas |
| Multipandang | Y bila tandan yang sama difoto lebih dari sekali |
| Per kelas | Y bila setiap tandan diberi kelas kematangan |

## Kolom lembar

| Kolom | Arti |
|---|---|
| Kolom berakhiran `_ai` | Keputusan AI. Dibekukan, jangan diubah |
| Kolom berlatar kuning di xlsx | Kolom Anda |
| `konfirmasi_C1`, `konfirmasi_C3`, `konfirmasi_alasan` | Y bila kelompok atau alasan keluarnya benar; N bila salah, lalu tulis yang benar di `catatan` |
| `kode_benar` | Y bila labelnya benar; N bila salah, lalu tulis koreksinya di `catatan` |
| `final_*` (Cek 5) | Label akhir setelah dibaca dari PDF |
| `catatan`, `catatan_peninjau` | Keterangan. Isian dari AI ditandai di sini, diawali "Diisi ... atas instruksi peninjau" atau "Penilaian buta ..." |
| `hanya_judul` | Y bila AI memutuskan dari judul saja, tanpa abstrak |
| `no`, `idx`, `key` | Nomor baris di lembar, nomor rekaman di korpus, dan kunci sitasi artikel |

## Istilah lain

| Istilah | Arti |
|---|---|
| Kappa | Ukuran kesepakatan dua penilai di luar kebetulan. 0,4–0,6 tergolong sedang |
| *Snowballing* | Mencari artikel tambahan dari daftar pustaka artikel yang sudah ada |
| Putaran kedua (AI-2) | Penyaringan ulang oleh AI pada 1–2 Oktober 2026 tanpa melihat putaran pertama |
| Penilaian buta | AI menilai dari nol, tanpa melihat keputusan sebelumnya |
