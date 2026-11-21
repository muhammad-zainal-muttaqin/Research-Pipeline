# Tugas Peninjau

Diperbarui 21 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **5.7 Bagian naskah yang hanya dapat diisi penulis.** Apakah peran
  penulis, sumber dana, deklarasi kepentingan, dan ucapan terima kasih sudah
  benar? Kerangkanya sudah ada di akhir naskah, sebelum Data availability
  (`manuscript/source/main6-body.tex`, cari `\authorcheck`; di PDF tercetak merah).
  Hal yang harus diputuskan penulis:
  - Peran CRediT kedua penulis (usulan sudah terisi).
  - Ada atau tidaknya dana hibah (teks bawaan menyatakan tidak ada).
  - Isi ucapan terima kasih, atau hapus seksinya.
  - Abstrak kini 290 kata. Periksa batas kata dan kebijakan AI di *Guide for
    Authors* jurnal *Computers and Electronics in Agriculture*.

  Hapus semua `\authorcheck` sebelum dikirim. Dampaknya: tanpa isian ini,
  naskah belum dapat dikirim.

- [ ] **5.8 Kajian buah blueberry Ni dkk. 2021 masuk kelompok mana?** Kajian
  "Three-dimensional photogrammetry with deep learning instance segmentation
  to extract berry fruit harvestability traits" kini tercatat sebagai kajian
  depth dan sensor 3D (C5). Isinya menggabungkan buah yang sama dari 120 foto
  satu tandan menjadi satu buah dalam model 3D, sama seperti kajian kembarnya
  Ni dkk. 2020 yang sudah tercatat sebagai kajian multi-pengamatan (C1).
  Apakah kelompoknya diubah menjadi C1? Buka
  [`../topik/penyaringan/teks_lengkap.txt`](../topik/penyaringan/teks_lengkap.txt)
  baris 652 (idx 621). Dampak: jumlah C1 naik satu dan C5 turun satu, angka
  naskah berubah.

- [ ] **5.9 Apakah tiga kajian menyatakan aturan kelas saat pengamatan
  berbeda?** Naskah kini menyebut aturan ini di Seksi 6, tetapi kodenya belum
  diubah. Buka [`../topik/bukti/mekanisme_C1.txt`](../topik/bukti/mekanisme_C1.txt),
  kolom `cara_kelas`:
  - baris 231 (idx 669, Ni dkk. 2020, blueberry): kini "per kelas: tidak".
    Setiap buah 3D diberi kelas matang bila potongan bertanda matang lebih
    banyak daripada yang mentah. Usul: per kelas ya, cara "voting
    antarpandang".
  - baris 234 (idx 955, Rong dkk. 2025, tomat ceri): kini "saat pelacakan".
    Kematangan diperbarui sebagai rata-rata bergerak antarbingkai dengan bobot
    0,5 bila tidak tertutup dan 0,1 bila tertutup. Usul: "voting
    antarpandang".
  - baris 241 (idx 593, Tenorio dan Caarls 2021, tomat ceri): kini "saat
    pelacakan". Kematangan dirata-ratakan atas bingkai yang cocok. Usul: tetap,
    atau "voting antarpandang".

  Dampak: angka "aturan dinyatakan" (kini 2) dan "studi per kelas" (kini 33)
  di naskah berubah; kalimat Seksi 6 dan Diskusi ikut diperbarui.
