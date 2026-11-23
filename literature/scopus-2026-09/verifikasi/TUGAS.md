# Tugas Peninjau

Diperbarui 23 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.8 Empat PDF kajian sawit yang baru diperoleh: masuk atau keluar?**
  PDF-nya ada di folder `../pdf/` dengan nama di bawah. Usul model ditulis per
  kajian; buka PDF untuk memeriksa. Setelah disetujui, keputusan ditulis ke
  `../topik/penyaringan/teks_lengkap.txt` (satu baris per kajian). Dampaknya
  angka naskah berubah: laporan yang tidak diperoleh turun dari 208 menjadi
  204. Kelompok sawit (C3) dan jumlah kajian di peta bertambah 2 bila usul
  diterima, atau 4 bila semuanya dimasukkan.
  1. Junos dkk. 2024, *Improved hybrid feature extractor in lightweight
     convolutional neural network for postharvesting technology*
     (`junos2024improved.pdf`). Usul: **masuk** sebagai kajian sawit (C3).
     Model YOLO mendeteksi tandan dan memberi empat kelas kematangan. Ada 1.281
     citra yang diambil di kebun Sime Darby, Selangor, dan hasilnya mAP 94,37%
     (halaman 1 dan 4). Lokasi tandan diubah dari "tidak disebut" menjadi "di
     kebun, posisi tandan tidak disebut" di `../topik/bukti/kode_C3.txt` baris
     idx 1619.
  2. Septiarini dkk. 2020, *Maturity grading of oil palm fresh fruit bunches
     based on a machine learning approach* (`septiarini2020maturity.pdf`).
     Usul: **masuk** sebagai kajian sawit (C3). Penelitian ini
     mengklasifikasikan kematangan dari 150 foto ponsel berjarak sekitar
     10 cm, dengan tiga kelas. Akurasi uji pada 90 citra adalah 98,89%
     (halaman 1). Tempat pengambilan tidak disebut, sehingga kodenya
     tetap.
  3. Fadilah dkk. 2012, *Oil palm fresh fruit bunch ripeness classification
     using artificial neural network*, konferensi ICIAS (`fadilah2012oil.pdf`).
     Usul: **keluar** karena merupakan laporan kedua dari kajian yang sudah
     masuk (E8). Kajian itu adalah Fadilah dkk. 2012 di jurnal *Sensors*
     (`fadilah2012intelligent.pdf`). Kedua laporan memakai 80 tandan DxP
     Yangambi dari FASSB, dengan penilai kematangan dan metode jaringan saraf
     yang sama. Pembagian citranya berbeda, dan akurasinya 86,67% dibanding
     93,33%. Ini mengikuti preseden Silwal dkk. 2015, yang dikeluarkan karena
     artikel jurnalnya sudah tercatat.
  4. Husin dkk. 2021, *Distribution map of oil palm fresh fruit bunch using
     LiDAR* (`husin2021distribution.pdf`). Usul: **keluar** karena tidak ada
     evaluasi kuantitatif (E5). Tandan contoh di MPOB Bangi dipindai dengan
     LiDAR Lite V3, yaitu pengukur jarak laser satu berkas. Rentang intensitas
     per kelas kematangan ditetapkan dari data yang sama, dan tidak ada
     akurasi yang dilaporkan (halaman 2–5). Bila Anda memilih memasukkannya,
     tugasnya di `kode_C3.txt` idx 1974 diubah dari deteksi tandan (DET)
     menjadi kajian modalitas non-RGB (SENSOR).

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

