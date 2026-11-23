# Tugas Peninjau

Diperbarui 23 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.18 Kelompok 2 PDF baru (23 November 2026).** Apakah kelompok di
  bawah ini benar? Teks lengkapnya ada di `teks/<kunci>.txt`. Usul AI ditulis
  di [`../topik/penyaringan/teks_lengkap.txt`](../topik/penyaringan/teks_lengkap.txt)
  sesudah disetujui.

  | Kajian | Kelompok di tahap abstrak | Usul dari teks lengkap | Alasan dan tempat di teks |
  |---|---|---|---|
  | Zhang dkk. 2019, hitung jeruk matang dengan komponen "a" ruang warna Lab dan transformasi Hough | C2 (hitung dari satu foto) | C2 tetap | Ponsel di tripod, 2,13 m dari pohon; dua sisi pohon difoto (baris 281), tetapi hitungan kedua sisi tidak dijumlahkan per pohon. Grafik regresi memuat lebih dari 100 titik, bukan 10 pohon atau 20 citra (Gambar 4). Akurasi 94,01% dan 96,58% hanya dari satu citra: 113 terdeteksi terhadap 117 hitung tangan (baris 266–274). R² ditulis 0,9879 di teks, 0,982 di grafik, dan 0,83 di abstrak bahasa Inggris |
  | Li dkk. 2014, ukur diameter apel muda dengan *watershed* dan *convex hull* | C5 (depth atau 3D) | **Dikeluarkan, E5 (deteksi tanpa pencacahan)** | Kamera RGB tetap 1–2 m dari buah, dengan bola pingpong sebagai acuan skala (baris 80–87). Tidak ada depth atau 3D, jadi syarat C5 tidak terpenuhi. Hanya 4 buah pilihan pada 2 pohon yang diukur diameternya (96 citra), dan acuannya penggaris Photoshop pada citra yang sama (baris 612–620). Buah tidak dicacah. Pilihan lain: tetap C5 bila pengukuran ukuran buah dari RGB dianggap masuk, seperti Fukuda dkk. 2024 yang memakai kamera depth |

  Dampak bila semua disetujui: peta naik dari 894 menjadi 895 kajian (C2
  157, C5 tetap 108), yang dinilai dari teks lengkap 930, dan yang
  dikeluarkan 35.

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

