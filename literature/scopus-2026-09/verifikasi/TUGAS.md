# Tugas Peninjau

Diperbarui 23 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.10 Tiga puluh enam PDF yang baru diperoleh: masuk ke kelompok
  mana, atau keluar?** PDF-nya ada di folder `../pdf/` dengan nama di bawah.
  Usul model dibuat dari teks lengkap; buka PDF untuk memeriksa. Setelah
  disetujui, keputusan ditulis ke `../topik/penyaringan/teks_lengkap.txt`
  (satu baris per kajian), dan setiap kajian yang masuk mendapat ringkasan di
  `../entri/`. Dampaknya angka naskah berubah. Bila semua usul diterima,
  kajian yang dinilai dari teks lengkap naik dari 845 menjadi 881, yang
  dikeluarkan naik dari 26 menjadi 28, dan peta naik dari 819 menjadi 853
  kajian: C1 +3, C2 +9, C3 +9, C4 +1, C5 +10, dan R +2.

  **A. Pindah ke multi-pengamatan (C1).** Setiap
  kajian mendapat baris baru di `../topik/bukti/mekanisme_C1.txt` dan
  `../topik/bukti/tanaman_platform_C1.txt`.
  1. Vasconcelos dkk. 2024, *UAV-Based Optimization for Fruit Counting in
     Greenhouses* (`vasconcelos2024uav.pdf`, idx 1095). Usul: **C1**,
     asosiasi geometris (M4), dua pandang diskret (D), paprika, terong, dan
     tomat, UAV. Setiap bedeng dipotret dari depan dan belakang, lalu posisi
     kotak dipakai untuk mencocokkan buah kedua citra: "the correspondence
     between the fruits in the front and back images is checked to avoid
     double counting". Semua uji berupa simulasi Gazebo (kompetisi ICUAS
     2024). Kodenya mengikuti Szolc dkk. 2026, kajian ICUAS 2024 lain yang
     sudah berkode M4 dan D.
  2. De Narda dkk. 2024, *SHD-O2D: A Novel Image Dataset for Super-High-Density
     Olive Orchard Yield Estimation* (`denarda2024shd.pdf`, idx 1075). Usul:
     **C1**, koreksi statistik (M1), D, zaitun. Perlu keputusan Anda karena
     teksnya tidak tegas. Setiap pohon dipotret dari sisi timur dan barat.
     Faktor skala (3,18 cerah, 2,20 berawan) diturunkan dari hitung tangan
     lima pohon: "the east and west side counted fruits have been summed".
     RMSE lalu dihitung "for each tree" dari "the number of detected fruits
     per tree". Penulis tidak menulis bahwa deteksi kedua sisi dijumlahkan,
     tetapi faktor skala yang dibentuk dari jumlah dua sisi hanya cocok bila
     deteksinya juga dijumlahkan. Kasus ini sama dengan Koirala dkk. 2019
     (C1, M1). Pilihan lain: tetap C2 bila Anda menilai setiap citra diproses
     sendiri.
  3. Li dkk. 2022, *Multi-vision-based Localization and Pose Estimation of
     Occluded Apple Fruits for Harvesting Robots* (`li2022multi.pdf`,
     idx 3760). Usul: **C1** (dari C5), asosiasi geometris (M4), D, apel,
     robot pemetik. Dua kamera stereo memotret buah tertutup yang sama dari
     dekat dan jauh. Posisi dan pose buah dari kedua kamera diubah ke
     kerangka dasar robot lalu dirata-ratakan berbobot (λa = 0,7, λb = 0,3),
     dan hasilnya dibandingkan dengan satu kamera pada 50 bingkai. Aturan
     stereo di protokol memberi C1 bila buah dihubungkan antarposisi kamera,
     dan aturan prioritas mendahulukan C1. Buah tidak dicacah; yang diukur
     galat posisi (mm) dan pose (rad). Pilihan lain: tetap C5 bila
     pengukuran satu buah sasaran untuk pemetikan tidak Anda anggap
     penggabungan pengamatan dalam arti tinjauan ini.

  **B. Keluar.**
  4. Bazame dkk. 2022, *Mapping coffee yield with computer vision*
     (`bazame2022mapping.pdf`, idx 493). Usul: **keluar**, karena buah sudah
     dipanen saat dicitrakan (E2). Kamera dipasang "over the side loading
     spout of a coffee harvester", jadi yang dicacah adalah aliran buah di
     corong mesin panen, bukan buah di tanaman.
  5. Achraf dkk. 2024, *Segmentation of Fruits and Leaves in Olive Branch
     Image Using AI Based Approach: Toward Yield Estimation*
     (`achraf2024segmentation.pdf`, idx 1076). Usul: **keluar**, karena buah
     tidak dicacah (E5). Segmen citra hanya diklasifikasikan sebagai zaitun,
     daun, atau lainnya (akurasi kelas zaitun 99,17%, ResNet50 95,89%). Ini
     sama dengan alasan Cheng dkk. 2016 dikeluarkan.

  **C. Masuk sawit (C3), dengan perubahan kode lokasi di
  `../topik/bukti/kode_C3.txt`.** Lokasi diubah hanya bila teks lengkap
  menyatakannya.
  6. Arulnathan dkk. 2022 (`arulnathan2022background.pdf`, idx 1880):
     lokasi dari "tidak disebut" menjadi lab/pabrik, karena brondolan
     "quickly rushed to our laboratory for processing within 8 hours".
  7. Robi dkk. 2022 (`robi2022image.pdf`, idx 1891): lokasi dari "tidak
     disebut" menjadi "citra dari internet", karena "175 images are
     collected from internet sources".
  8. Priyadi dkk. 2023 (`priyadi2023comparison.pdf`, idx 1795): lokasi dari
     "tidak disebut" menjadi "di kebun, posisi tandan tidak disebut", karena
     "data collection took place in an oil palm plantation located in
     Kalimantan".
  9. Jailani dkk. 2024 (`jailani2024fresh.pdf`, idx 1698): lokasi dari
     "tidak disebut" menjadi "di kebun, posisi tandan tidak disebut", karena
     "5,042 images of oil palm fruits in plantation environment".
  10. Purba dkk. 2024 (`purba2024comparison.pdf`, idx 1702): lokasi dari
      "tidak disebut" menjadi "di kebun, posisi tandan tidak disebut", karena
      "The dataset was collected directly from the oil palm plantation area
      of PTPN IV Medan".
  11. Naghipour dkk. 2024 (`naghipour2024yolo.pdf`, idx 1687): lokasi dari
      "tidak disebut" menjadi "di pohon", karena "the FFB on the trees are
      our focus". Sebagian citra (179 dari 500) diambil dari internet.

  **D. Masuk tanpa perubahan kode.**
  - Sawit (C3), kode lokasi tetap: Gunawan dkk. 2023 (tandan diputar 360°
    di video, lokasi tidak disebut), Herman dkk. 2021 (klasifikasi tujuh
    tingkat kematangan, lokasi tidak disebut), Xiang dkk. 2021 (brondolan di
    tanah).
  - Hitung satu pandang (C2): Arakawa dkk. 2024 (kastanye, satu citra UAV
    per pohon), Behera dkk. 2021, Chakraborty dkk. 2023, Chanda dkk. 2024,
    Justam dkk. 2023, Li dkk. 2024, Pavithra dkk. 2022, Quan dkk. 2023, Tang
    dkk. 2022.
  - Atribut kelas dengan hitung (C4): Yan dkk. 2024, *An Integrated Target
    Recognition Method Based on Improved Faster-RCNN* (apel, empat tingkat
    kematangan, 200 citra dari Google).
  - Depth atau non-RGB (C5): da Silva dkk. 2024 (LiDAR, jeruk), Gong dkk.
    2022 (Kinect, tomat), Sato dkk. 2022 (RealSense, apel), Wang dkk. 2023
    (RGB-D, apel), Xie dkk. 2023 (stereo), Fukuda dkk. 2024 (diameter apel,
    RealSense), Hao dkk. 2024 (diameter tomat, kamera depth), Simini dkk.
    2024 (posisi 3D buah dari satu pasang RGB-D per pohon), Yan dkk. 2024,
    *Detection in Complex Scenes Using RGB and Depth Multimodal Feature
    Fusion* (pir), Ye dkk. 2024 (depth monokular MiDaS dan rekonstruksi 3D
    tomat; tetap C5 walaupun depth-nya diestimasi dari citra RGB).
  - Tinjauan terdahulu (R): Tang dkk. 2023, *Optimization strategies of
    fruit detection to overcome the challenge of unstructured background in
    field orchard environment*; Hidayat dkk. 2024, *Oil Palm Fruit Ripeness
    Detection Technique* (19 artikel sawit).

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

