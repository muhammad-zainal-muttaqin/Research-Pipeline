# Tugas Peninjau

Diperbarui 27 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.30 Pencacahan nanas dari citra udara oleh Aguero Sandí dkk. (2026).**
  Apakah laporan Scopus nomor 912 masuk kelompok pencacahan dari beberapa
  pengamatan (C1), dengan asosiasi geometris (M4) dari beberapa pandang
  diskret (D)? Usul ini menggantikan kelompok pencacahan dari satu pandang
  (C2) pada tahap abstrak. Buka [metode, baris 204–233](../teks/sandi2026implementation.txt#L204-L233)
  dan [hasil, baris 380–445](../teks/sandi2026implementation.txt#L380-L445).
  Detektor YOLOv8 memproses petak ortomosaik, yaitu peta gabungan foto udara,
  lalu mengembalikan posisi setiap deteksi ke koordinat peta. Tabel II
  membandingkan prediksi dengan hitungan manual pada empat ortomosaik.
  Pada dua ortomosaik di luar pelatihan, galat model akhir adalah 8,78%
  (Lote Cerro) dan 38,54% (Lote Planta).

  Angka 36.852 deteksi untuk Lote Cerro pada [Tabel III, baris 530–534](../teks/sandi2026implementation.txt#L530-L534)
  juga menjadi angka dasar pada [Mejias-Hernandez dkk., baris 560–569](../teks/mejiashernandez2026automated.txt#L560-L569).
  Aguero Sandí dkk. melaporkan pembandingan dengan hitungan manual. Mejias-Hernandez
  dkk. menguji gabungan beberapa detektor. Usulnya mempertahankan kedua laporan
  dengan mencatat pemakaian ortomosaik dan angka dasar yang sama.

  Dampak bila disetujui: peta bertambah dari 924 menjadi 925 kajian dan
  kelompok pencacahan dari beberapa pengamatan bertambah dari 252 menjadi 253.

- [ ] **5.7 Bagian naskah yang hanya dapat diisi penulis.** Apakah sumber
  dana dan ucapan terima kasih sudah benar? Kerangkanya ada di akhir naskah,
  sebelum Data availability (`manuscript/source/main7-body.tex`, cari
  `\authorcheck`; di PDF tercetak merah). Peran CRediT dan penulis
  korespondensi (Fatma Indriani) sudah diisi. Hal yang masih harus diputuskan
  penulis:
  - Ada atau tidaknya dana hibah.
  - Isi ucapan terima kasih, atau hapus seksinya.
  - Tempat data. Jika keputusan penyaringan, matriks bukti, log, dan skrip
    diunggah ke repositori, cantumkan DOI atau tautannya di bagian Data
    availability.
  - Saat mengirim, periksa kembali dan unggah [lima butir *highlights*](../../../manuscript/output/papers/main6-highlights.txt)
    sebagai berkas terpisah dan periksa kebijakan AI di *Guide for Authors* jurnal
    *Computers and Electronics in Agriculture*.

  Hapus semua `\authorcheck` sebelum dikirim. Dampaknya: tanpa isian ini,
  naskah belum dapat dikirim.

