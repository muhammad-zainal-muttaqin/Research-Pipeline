# Tugas Peninjau

Diperbarui 23 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.9 Tiga puluh satu PDF yang baru diperoleh: masuk ke kelompok mana,
  atau keluar?** PDF-nya ada di folder `../pdf/` dengan nama di bawah. Usul
  model dibuat dari teks lengkap; buka PDF untuk memeriksa. Setelah disetujui,
  keputusan ditulis ke `../topik/penyaringan/teks_lengkap.txt` (satu baris per
  kajian), dan setiap kajian yang masuk mendapat ringkasan di `../entri/`.
  Dampaknya angka naskah berubah. Bila semua usul diterima, kajian yang dinilai
  dari teks lengkap naik dari 814 menjadi 845, yang dikeluarkan naik dari 25
  menjadi 26, dan peta naik dari 789 menjadi 819 kajian: C1 +4, C2 +10,
  C3 +12, C5 +3, dan T +1.

  **A. Pindah dari hitung satu pandang (C2) ke multi-pengamatan (C1).** Ketiga
  kajian pertama menggabungkan hitungan beberapa citra pohon yang sama tanpa
  menautkan buah, lalu mengoreksinya dengan faktor atau regresi. Aturan
  "gabungan statistik" di protokol menetapkan kasus ini sebagai C1 dengan
  mekanisme koreksi statistik (M1). Kajian keempat melacak buah antarcitra.
  Setiap kajian mendapat baris baru di `../topik/bukti/mekanisme_C1.txt` dan
  `../topik/bukti/tanaman_platform_C1.txt`.
  1. Koirala dkk. 2019, *Deep learning for real-time fruit detection and
     orchard fruit load estimation* (`koirala2019deep.pdf`, idx 685). Usul:
     **C1**, koreksi statistik (M1), dua pandang diskret (D), mangga.
     Hitungan dari dua sisi pohon dijumlahkan lalu dikali faktor koreksi dari
     panen tangan pohon contoh.
  2. Sarron dkk. 2020, *Is machine learning efficient for mango yield
     estimation when used under heterogeneous field conditions?*
     (`sarron2020machine.pdf`, idx 1269). Usul: **C1**, M1, D, mangga.
     Penulis menulis: "The automatic count, was calculated as the sum of the
     number of detection from both images of the tree." Jumlah itu lalu
     diregresikan per kultivar terhadap hitungan lapangan pada 104 pohon.
  3. Linker 2017, *A procedure for estimating the number of green mature
     apples in night-time orchard images* (`linker2017procedure.pdf`,
     idx 1358). Usul: **C1**, M1, D, apel. Hitungan dari dua sampai enam citra
     per pohon (tiga ketinggian kamera, satu atau dua sisi) digabung dengan
     regresi linear berganda terhadap hasil panen per pohon.
  4. Anderson dkk. 2019, *Estimation of fruit load in mango orchards: tree
     sampling considerations and use of machine vision and satellite imagery*
     (`anderson2019estimation.pdf`, idx 697). Usul: **C1**, pelacakan dan
     asosiasi geometris (M3+M4), video (V), mangga. Kajian ini memakai metode
     Stein dkk. 2016, yaitu buah dilacak pada 25 citra per sisi pohon dan
     deteksi dikaitkan ke pohon dengan proyeksi LiDAR. Kodenya mengikuti
     kode Stein dkk. 2016 yang sudah ada.

  **B. Keluar.**
  5. Cheng dkk. 2016, *Detection of apple fruit in an orchard for early yield
     prediction as affected by crop load management* (`cheng2016detection.pdf`,
     idx 1370). Usul: **keluar**, karena tidak ada pencacahan atau evaluasi
     terhadap acuan (E5). "Efisiensi pengenalan buah" yang dilaporkan adalah
     rasio luas buah terdeteksi antara dua tanggal pemotretan, tanpa hitung
     tangan, panen, atau anotasi.

  **C. Perlu keputusan Anda.**
  6. Hung dkk. 2013, *Orchard fruit segmentation using multi-spectral feature
     learning* (`hung2013orchard.pdf`, idx 2740). Usul: **tetap C5** (deteksi
     buah dengan modalitas non-RGB). Setiap piksel citra warna dan inframerah
     diberi label buah atau bukan buah, dengan akurasi 88% terhadap label
     piksel manual. Penulis menyatakan metodenya "does not provide the actual
     fruit count". Pilihan lain: keluar sebagai E5 karena buah tidak dicacah.

  **D. Masuk sawit (C3), dengan perubahan kode lokasi di
  `../topik/bukti/kode_C3.txt`.** Lokasi diubah hanya bila teks lengkap
  menyatakannya. Lab/pabrik dipakai untuk pencitraan di dalam ruangan atau di
  laboratorium.
  7. Wong dkk. 2020 (`wong2020computer.pdf`, idx 2055): lokasi dari "di
     pohon" menjadi "citra dari internet", karena citra kematangan berasal
     dari "available palm fruit datasets online".
  8. Kassim dkk. 2014 (`kassim2014oil.pdf`, idx 2410): lokasi dari "di tanah"
     menjadi "di kebun, posisi tandan tidak disebut", karena tandan dipotret
     saat survei kebun ("one FFB from each tree was selected").
  9. Alfatni dkk. 2014, *Oil palm fruit maturity classification based on
     texture feature extraction* (`alfatni2014oil.pdf`, idx 2388): lokasi dari
     "tidak disebut" menjadi lab/pabrik, karena citra diambil dengan
     penerangan terkendali di ruang tandan sistem grading.
  10. Gro dkk. 2017 (`gro2017maturity.pdf`, idx 2275): lokasi dari "tidak
      disebut" menjadi lab/pabrik, karena buah lepas dipotret di ruang gelap.
      Tugas dari klasifikasi (KLS) menjadi kajian sensor (SENSOR), karena
      indeks NDVI dan NRI dibandingkan dengan kadar pigmen pada 18 sampel,
      tanpa klasifikasi.
  11. Septiarini dkk. 2019 (`septiarini2019image.pdf`, idx 2112): lokasi
      lab/pabrik, karena dipotret "in the room".
  12. Setiawan dkk. 2019 (`setiawan2019estimation.pdf`, idx 2125): lokasi
      lab/pabrik, karena dipotret "in a closed room" dengan LED 680 nm.
  13. Setiawan dkk. 2020 (`setiawan2020palm.pdf`, idx 2076): lokasi
      lab/pabrik, karena dipotret "in closed and dark conditions".
  14. Shiddiq dkk. 2017 (`shiddiq2017ripeness.pdf`, idx 2282): lokasi
      lab/pabrik, karena percobaan "was done indoor" dengan tandan di platform
      aluminium setinggi 1,5 sampai 3 m.
  15. Zolfagharnassab dkk. 2017 (`zolfagharnassab2017emissivity.pdf`,
      idx 2274): lokasi lab/pabrik, karena tandan dipanaskan sampai 100°C
      sebelum dicitrakan dengan kamera termal.

  **E. Masuk tanpa perubahan kode.**
  - Sawit (C3), kode lokasi tetap: Sae-Tang dkk. 2020 (`saetang2020estimation`,
    kadar minyak, lokasi tidak disebut), Siddesha dkk. 2018
    (`siddesha2018segmentation`, tandan di pohon), Sukemi dkk. 2019
    (`sukemi2019identification`, lokasi tidak disebut).
  - Hitung satu pandang (C2): Gayathri dkk. 2018, Hung dkk. 2016, Hutagalung
    dkk. 2018, Li dkk. 2016, Neethi dkk. 2021, Payne dkk. 2016, Prabhu dkk.
    2021, Qureshi dkk. 2017, Sathesh dkk. 2019, Wang dkk. 2018. Hung dkk.
    2016 menjumlahkan lingkaran dari citra yang diambil setiap 0,5 m sepanjang
    baris. Penulis menyebut jarak itu "arbitrary 0.5 m image spacing to avoid
    overlapping detections", jadi tidak ada penggabungan pengamatan buah yang
    sama. Karena itu kajian ini tetap C2.
  - Depth atau non-RGB (C5): Tsoulias dkk. 2020 (LiDAR 2D, apel), Tu dkk. 2020
    (RGB-D, markisa).
  - Luar pertanian (T): Timofte dkk. 2014 (rambu lalu lintas dari beberapa
    pandang, dilokalisasi dalam 3D).

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

