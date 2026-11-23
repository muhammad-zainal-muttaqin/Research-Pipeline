# Tugas Peninjau

Diperbarui 23 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.14 Kelompok 2 PDF baru (23 November 2026).** Apakah kelompok di
  bawah ini benar? Teks lengkapnya ada di `teks/<kunci>.txt`. Usul AI
  ditulis di
  [`../topik/penyaringan/teks_lengkap.txt`](../topik/penyaringan/teks_lengkap.txt)
  sesudah disetujui.

  | Kajian | Kelompok di tahap abstrak | Usul dari teks lengkap | Alasan dan tempat di teks |
  |---|---|---|---|
  | Cheng dkk. 2021, taksiran hasil tomat rumah kaca (YOLOv3 diperbaiki) | C2 (hitung dari satu foto) | **C4 (kelas dari satu foto)** | Buah merah dan buah hijau dicacah terpisah pada satu citra per bidang pandang. Pada 200 bidang pandang, rasio hitungan model terhadap hitungan manual pada citra adalah 97,0% (merah), 95,5% (hijau), dan 96,3% (semua) (Tabel 4; baris 385–412 di `teks/cheng2021method.txt`, hasil OCR). Buah tidak ditautkan antarcitra |
  | Chauhan dan Singh 2022, robot deteksi tandan anggur (OpenCV dan *random forest*) | C2 | **Dikeluarkan, E5 (deteksi tanpa hitung atau evaluasi)** | Yang dievaluasi hanya klasifikasi piksel anggur dan bukan anggur (akurasi 97,5%, F1 90,7%). Jumlah tandan hanya ditampilkan pada satu gambar contoh (Gambar 9) tanpa pembanding, dan sebagian citra uji diambil dari Google (baris 387–391, 452–453). Sama dengan Kiran dkk. 2025 yang dikeluarkan dengan alasan ini |

  Dampak bila disetujui: peta naik dari 888 menjadi 889 kajian (C4 36), yang
  dinilai dari teks lengkap 922, dan yang dikeluarkan 33. Angka naskah,
  gambar, lampiran, dan Ruang Baca dibuat ulang.

- [ ] **5.7 Bagian naskah yang hanya dapat diisi penulis.** Apakah sumber
  dana dan ucapan terima kasih sudah benar? Kerangkanya ada di akhir naskah,
  sebelum Data availability (`manuscript/source/main6-body.tex`, cari
  `\authorcheck`; di PDF tercetak merah). Peran CRediT dan penulis
  korespondensi (Fatma Indriani) sudah diisi. Hal yang masih harus diputuskan
  penulis:
  - Ada atau tidaknya dana hibah (teks bawaan menyatakan tidak ada).
  - Isi ucapan terima kasih, atau hapus seksinya.
  - Tempat data. Seksi Data availability menulis bahwa keputusan
    penyaringan, matriks bukti, log perubahan, dan skrip "are provided with
    it". Bila berkas itu diunggah ke repositori (misalnya Zenodo), tulis DOI
    atau tautannya di kalimat itu.
  - Saat mengirim: unggah lima butir *highlights* (di `main6.tex`) sebagai
    berkas terpisah, dan periksa kebijakan AI di *Guide for Authors* jurnal
    *Computers and Electronics in Agriculture*. Abstrak kini 249 kata.

  Hapus semua `\authorcheck` sebelum dikirim. Dampaknya: tanpa isian ini,
  naskah belum dapat dikirim.

