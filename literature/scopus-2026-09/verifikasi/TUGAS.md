# Tugas Peninjau

Diperbarui 17 Oktober 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda. Arti kode ada di [ISTILAH.md](ISTILAH.md).

## Cara kerja

1. Kerjakan dari atas. Satu keputusan di tahap awal sering menyelesaikan banyak
   butir di bawahnya.
2. Jawab di lembar (kolom berlatar kuning di berkas `.xlsx`), atau tulis jawaban
   singkat ke agen, misalnya "1.1 ya, 2.2 tolak no 35".
3. Agen menerapkan jawaban ke data, menghitung ulang angka dan naskah, lalu
   menghapus butir yang selesai dari daftar ini.

Isian AI di lembar ditandai di kolom `catatan` dan belum sah sebelum Anda
setujui.

## Tahap 1. Aturan (sebaiknya bersama Bu Fatma)

- [ ] **1.1 Apakah artikel yang menyusun model 3D dari banyak foto, atau yang
  menggabungkan hitungan dengan cara statistik, termasuk C1?** AI menjawab "ya"
  karena aturannya belum ada.
  Buka [cek_C1.xlsx](cek-2-cek-tangan/cek_C1.xlsx), saring `catatan` yang memuat
  "aturan Fatma" (23 baris). Bila "tidak", sebagian keluar dari C1 dan angka
  naskah berubah.
- [ ] **1.2 Apakah artikel *dataset* yang tidak membawa metode hitung termasuk
  C1?** [cek_C1.xlsx](cek-2-cek-tangan/cek_C1.xlsx) no 167 (AI: ya) dan no 168
  (kosong).
- [ ] **1.3 Apakah artikel yang melacak buah antar-*frame* tetapi tidak
  melaporkan hitungan termasuk C1?** [cek_C1.xlsx](cek-2-cek-tangan/cek_C1.xlsx)
  no 129.
- [ ] **1.4 Apakah regresi kalibrasi (jumlah terlihat dikonversi ke jumlah
  sebenarnya) diberi label M1?** [cek_C1.xlsx](cek-2-cek-tangan/cek_C1.xlsx)
  no 163, 165, 184.
- [ ] **1.5 Artikel yang memotret dari banyak posisi lalu menyusun awan titik 3D
  diberi label akuisisi apa: D, S, atau V?** AI tidak seragam. Empat artikel:
  `xiao20243d`, `sun2020three`, `torressanchez2021grape`, `hobart2025fruit` di
  [kode_ulang_C1.csv](cek-5-kode-ulang/kode_ulang_C1.csv).
- [ ] **1.6 Artikel dari jurnal berbahasa Mandarin dengan abstrak Inggris:
  dikeluarkan karena bahasa (E7) atau dinilai menurut isinya?** Sepuluh artikel;
  empat artikel serupa sudah masuk tinjauan, jadi aturannya harus seragam. Lihat
  kolom `bahasa_artikel` di
  [sisa_perlu_peninjau_sonnet.csv](hasil-kerja-ai/menunggu-acc/cek-2/sisa_perlu_peninjau_sonnet.csv).

## Tahap 2. Keputusan yang mengubah jumlah artikel

- [ ] **2.1 Sembilan belas artikel yang dikeluarkan menurut AI layak masuk.
  Masukkan?** (C5 8, C2 4, C1 3, R 2, C3 1, C4 1.)
  [cek_eksklusi.xlsx](cek-2-cek-tangan/cek_eksklusi.xlsx), saring `catatan` yang
  memuat "layak masuk".
- [ ] **2.2 Lima artikel C1 yang menurut AI bukan C1. Keluarkan dari C1?**
  [cek_C1.xlsx](cek-2-cek-tangan/cek_C1.xlsx) no 35, 103, 140, 161, 194.
- [ ] **2.3 Tujuh artikel yang status C1-nya lemah menurut pembacaan PDF.
  Tetap C1?** `kutyrev2025uav`, `ahmad2024enabling`, `torressanchez2021grape`,
  `zineelabidine2021assigning`, `zaenker2021viewpoint`, `zaenker2023graph`,
  `marangoz2022fruit`. Alasan AI ada di
  [KEMAJUAN.md Cek 5](hasil-kerja-ai/menunggu-acc/cek-5/KEMAJUAN.md).
- [ ] **2.4 Empat artikel sawit yang menurut AI bukan C3. Setuju?** Tiga
  diusulkan pindah ke C1 karena aturan prioritas (no 15, 116, 126); satu
  dikeluarkan karena tidak memakai kamera (no 12).
  [cek_C3.xlsx](cek-2-cek-tangan/cek_C3.xlsx).
- [ ] **2.5 Empat artikel dari daftar pustaka artikel lain memenuhi kriteria.
  Tambahkan?** Payne 2014, Apolo-Apolo 2020, Kwon 2024, Choi 2015. AI
  menyarankan tidak, karena penelusuran daftar pustaka baru mencakup 57 dari 635
  judul. [usul_keputusan_cek3.md](hasil-kerja-ai/menunggu-acc/cek-3/usul_keputusan_cek3.md).
- [ ] **2.6 Hamdani 2026 menghitung buah di dalam tandan, bukan tandan; Hutapea
  2024 tidak melaporkan hitungan. Masih dihitung sebagai studi pencacahan
  sawit?** Ini menentukan kalimat "nine counting studies" di naskah.
- [ ] **2.7 Tujuh belas artikel dari penyaringan ulang AI yang belum
  diputuskan.** Tujuh diperdebatkan antar-AI dan sepuluh diserahkan ke manusia.
  [PERUBAHAN-AI2.md](hasil-kerja-ai/putaran-kedua/PERUBAHAN-AI2.md) bagian B
  dan C.

## Tahap 3. Usul koreksi label

- [ ] **3.1 Usul koreksi label C1.** Ada 42 usul dari Cek 2 dan 39 usul dari
  Cek 5; 26 artikel muncul di keduanya. Kerjakan per artikel, dua lembar
  berdampingan: [cek_C1.xlsx](cek-2-cek-tangan/cek_C1.xlsx) (saring
  `kode_benar` = N) dan [kode_ulang_C1.csv](cek-5-kode-ulang/kode_ulang_C1.csv)
  (saring `draf_ai_berubah` yang diawali "ya").
- [ ] **3.2 Lima label C1 yang AI sendiri ragukan.**
  [usul_kode_ulang_C1.csv](hasil-kerja-ai/menunggu-acc/cek-5/usul_kode_ulang_C1.csv),
  saring `keyakinan` = rendah.
- [ ] **3.3 Tiga pasang artikel yang memakai data atau hasil yang sama. Dihitung
  dua artikel atau satu?** `roy2019vision` dan `dong2020semantic`;
  `osman2021yield` dan `osman2021yieldb`; `nuske2014automated` dan
  `nuske2014modeling`.
- [ ] **3.4 Usul koreksi label C3.** 27 usul (saring `kode_benar` = N) dan 7
  baris yang label rincinya berbeda antarpenilai AI (no 33, 35, 46, 114, 131,
  132, 176). [cek_C3.xlsx](cek-2-cek-tangan/cek_C3.xlsx).
- [ ] **3.5 Lima label makalah terkenal yang diubah AI pada 1 Oktober 2026.**
  Stein, Zhang, Lee, Fusaro, Indriani.
  [usul_keputusan_cek3.md](hasil-kerja-ai/menunggu-acc/cek-3/usul_keputusan_cek3.md).
- [ ] **3.6 Empat artikel tetap dikeluarkan, tetapi AI mengusulkan alasan lain.**
  [cek_eksklusi.xlsx](cek-2-cek-tangan/cek_eksklusi.xlsx) no 7, 48, 101, 134;
  usulnya di kolom `catatan`.
- [ ] **3.7 Isian AI yang menyatakan "sudah benar": setujui semua atau periksa
  acak?** C1 146 baris, C3 134 baris, eksklusi 109 baris, kode ulang C1 147
  baris.

## Tahap 4. Yang harus dibaca dari PDF

- [ ] **4.1 Empat artikel sawit yang AI putuskan dari judul saja.**
  [cek_C3.xlsx](cek-2-cek-tangan/cek_C3.xlsx) no 7, 11, 21, 31.
- [ ] **4.2 Sebelas artikel yang dikeluarkan, tetapi buktinya kurang.**
  [cek_eksklusi.xlsx](cek-2-cek-tangan/cek_eksklusi.xlsx), baris dengan
  `konfirmasi_alasan` kosong.
- [ ] **4.3 Empat PDF berbahasa Mandarin yang teksnya tidak terbaca AI.**
  [kode_ulang_C1.csv](cek-5-kode-ulang/kode_ulang_C1.csv) no 29, 44, 48, 58.
- [ ] **4.4 PDF `kang2022accurate` berisi artikel lain dari penulis yang sama.**
  Unduh ulang PDF yang benar ke folder `pdf/` dengan nama yang sama.

## Tahap 5. Naskah

- [ ] **5.1 Sembilan kalimat naskah yang salah. Setujui kalimat penggantinya?**
  Usulnya ada di [KEMAJUAN.md Cek 6](hasil-kerja-ai/menunggu-acc/cek-6/KEMAJUAN.md).
  Nomor di sana memakai lembar lama; padanannya di
  [cek_fakta.csv](cek-6-cek-fakta/cek_fakta.csv): K006, K014, K021, K043-1,
  K136-2, K136-4, K136-5, K170, K200. Dua usul opsional: K136-6, K113-1.
- [ ] **5.2 Kalimat tentang penelusuran daftar pustaka** (`main6-body.tex`
  baris 75, "ten candidates ... none met the criteria") hanya benar untuk
  kriteria C1. Ubah?
- [ ] **5.3 Kueri Q9 ternyata tidak dibatasi bidang ilmu.** Kalimat metode dan
  `PROTOKOL.md` bagian 2 perlu disesuaikan. Setuju?
- [ ] **5.4 Sebanyak 223 kalimat naskah terbaru belum dicek ke sumbernya.
  Periksa sendiri, atau minta AI memeriksa dahulu?**
  [cek_fakta.csv](cek-6-cek-fakta/cek_fakta.csv), baris dengan `benar` kosong
  dan id tanpa awalan `L-`. Daftar
  [peta_klaim_kosong.csv](hasil-kerja-ai/menunggu-acc/cek-6/peta_klaim_kosong.csv)
  menunjukkan baris lama yang mirip.
- [ ] **5.5 Sepuluh klaim yang tidak dapat diperiksa AI.**
  [usul_cek_fakta.csv](hasil-kerja-ai/menunggu-acc/cek-6/usul_cek_fakta.csv),
  `usul_benar` kosong.
- [ ] **5.6 Tahun terbit Liu dan Ampatzidis: 2026 atau 2027?** Saat ini 2027.
- [ ] **5.7 Bagian yang hanya dapat diisi penulis:** CRediT, Funding,
  Declaration of competing interest, Acknowledgment, batas kata abstrak, dan
  kebijakan AI jurnal tujuan.

## Bagian Bu Fatma

- [ ] **F.1 118 perbedaan keputusan antara peninjau dan AI pada sampel acak.**
  [ketidaksepakatan.csv](cek-1-sampel-buta/ketidaksepakatan.csv), kolom
  `keputusan_final_fatma`.
- [ ] **F.2 Konfirmasi alasan E1 untuk idx 1338.**
- [ ] **F.3 Empat artikel C1 yang mungkin terkena aturan stereo:**
  `zhang2021method`, `xie2023fruit`, `hu2026calibration`, `vulpi2022rgb`.
- [ ] **F.4 Kode buta 20 artikel C1 acak.**
  [sampel_fatma_C1.csv](cek-5-kode-ulang/sampel_fatma_C1.csv), kolom `fatma_*`.
