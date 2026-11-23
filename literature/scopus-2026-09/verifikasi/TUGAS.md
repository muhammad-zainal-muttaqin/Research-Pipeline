# Tugas Peninjau

Diperbarui 23 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.11 Dua puluh delapan PDF yang baru diperoleh: masuk ke kelompok
  mana, atau keluar?** PDF-nya ada di folder `../pdf/` dengan nama di bawah.
  Usul model dibuat dari teks lengkap; buka PDF untuk memeriksa. Setelah
  disetujui, keputusan ditulis ke `../topik/penyaringan/teks_lengkap.txt`
  (satu baris per kajian), dan setiap kajian yang masuk mendapat ringkasan di
  `../entri/`. Dampaknya angka naskah berubah. Bila semua usul diterima,
  kajian yang dinilai dari teks lengkap naik dari 881 menjadi 909, yang
  dikeluarkan naik dari 28 menjadi 31, dan peta naik dari 853 menjadi 878
  kajian: C1 +1, C2 +1, C3 +16, C4 +1, C5 +2, R +2, dan T +2.

  **A. Pindah dari hitung satu pandang (C2) ke multi-pengamatan (C1).**
  1. Chandra dkk. 2025, *Fruit Detection and Counting Using Deep Learning*
     (`chandra2025fruit.pdf`, idx 212). Usul: **C1**, pelacakan (M3), video
     (V), apel, drone. Drone memutari pohon apel sambil merekam video, dan
     ByteTrack menjaga identitas buah antarbingkai "to reduce the risk of
     counting the same fruit more than once". Pelacakannya dievaluasi pada 300
     bingkai: rata-rata 93,4% identitas bertahan, serta jumlah identitas
     hilang dan tertukar. Tidak ada acuan hitung tangan atau panen. Baris baru
     ditambahkan di `../topik/bukti/mekanisme_C1.txt` dan
     `../topik/bukti/tanaman_platform_C1.txt`.

  **B. Keluar.**
  2. Pragatheesh dkk. 2025, *A Deep Learning application for Accurate Oil
     Palm Counting by Eliminating Re-counting* (`pragatheesh2025deep.pdf`,
     idx 233). Usul: **keluar**, karena yang dicacah pohon sawit dari video
     UAV, bukan buah atau tandan (E1). Pelacakannya juga hanya dinilai
     secara kualitatif.
  3. Kiran dkk. 2025, *Automated Fruit Counting with YOLOv5 Model for
     Harvest Management in Orchards* (`kiran2025automated.pdf`, idx 1012).
     Usul: **keluar**, karena buah tidak dicacah dalam hasil (E5). Yang
     dilaporkan hanya presisi, *recall*, F1, dan mAP deteksi. DeepSORT
     disebut sebagai pascapemrosesan tetapi tidak dievaluasi.
  4. Prabhu dkk. 2025, *On Tree Grading of Sapota and Yield Prediction with
     Computer Vision* (`prabhu2025tree.pdf`, idx 2557). Usul: **keluar**,
     karena buah tidak dicacah dan hasil tidak diestimasi dengan angka (E5).
     Yang dilaporkan hanya mAP deteksi dua kelas ukuran (0,983).

  **C. Masuk sawit (C3), dengan perubahan kode di
  `../topik/bukti/kode_C3.txt`.** Lokasi diubah hanya bila teks lengkap
  menyatakannya. "Set data publik" mengikuti kode WEB (citra dari internet
  atau set data publik tanpa keterangan tempat).
  5. Chowdhury dkk. 2025 (`chowdhury2025comparative.pdf`, idx 1560): lokasi
     "di kebun", karena "obtained from a palm oil plantation in Selangor,
     Malaysia".
  6. Cindra dkk. 2025 (`cindra2025utilization.pdf`, idx 1554): lokasi "di
     kebun", karena citra "sourced from plantations in Johor, Negeri
     Sembilan, and Perak, Malaysia".
  7. Izzatina dkk. 2025 (`izzatina2025knowledge.pdf`, idx 1558): lokasi "di
     kebun", karena citra "captured on field conditions representative of
     Indonesian palm oil plantations".
  8. Santoso dkk. 2025 (`santoso2025se.pdf`, idx 1597): lokasi "di kebun",
     karena citra "collected from a plantation in Kalimantan"; modalitas dari
     "tidak disebut" menjadi RGB.
  9. Goh dkk. 2024 (`goh2024vision.pdf`, idx 1684): lokasi "di kebun",
     karena set uji 100 citra "captured manually from the orchard". Asal
     data latih tidak disebut.
  10. Warni dkk. 2025, *Comparative Analysis of Series YOLO Models*
      (`warni2025comparative.pdf`, idx 1587): lokasi "di kebun", karena
      citra brondolan "collected from field sources". Isinya berbeda dari
      laporan Warni dkk. 2025 yang lain (597 citra, empat generasi YOLO),
      jadi bukan laporan ganda.
  11. Kiet dkk. 2025 (`kiet2025study.pdf`, idx 1572): lokasi lab/pabrik,
      karena memakai set data Suharjito dkk. yang "collected from several
      palm oil mills in South Kalimantan".
  12. Desandros dkk. 2025 (`desandros2025interpretable.pdf`, idx 1574):
      lokasi "citra dari internet atau set data publik", karena memakai "a
      publicly available oil palm images dataset" di Zenodo.
  13. Fadillah dkk. 2025 (`fadillah2025enhanced.pdf`, idx 1583): lokasi set
      data publik, karena memakai set data Kaggle "Ripeness of oil palm
      fruit".
  14. Srithai dkk. 2025 (`srithai2025ripeness.pdf`, idx 1570): lokasi set
      data publik, karena citra "obtained from the Science Data Bank".
  15. Bakar dkk. 2024 (`bakar2024color.pdf`, idx 1685): lokasi "citra dari
      internet", karena citra "collected from various internet sources such
      as Kaggle, along with self-taken photos".

  **D. Masuk tanpa perubahan kode.**
  - Sawit (C3), kode tetap: Hakim dkk. 2025 dan Hamzah dkk. 2025
    (brondolan, lokasi tidak disebut), Sukma dkk. 2025 (tandan di pohon,
    drone), Zaman dkk. 2025 (tandan di pohon dari UAV), Warni dkk. 2025,
    *Harnessing YOLO for Loose Fruits Detection* (brondolan di tanah).
  - Hitung satu pandang (C2): Li dkk. 2025, SYL-YOLOv8n (persik, satu citra
    UAV per pohon, dibandingkan dengan hitung tangan 80 pohon).
  - Atribut kelas dengan hitung (C4): Carandang dkk. 2025 (murbei, empat
    tahap buah dicacah per kelas).
  - Depth atau non-RGB (C5): Tan dkk. 2025 (diameter apel dari depth
    monokular yang dikalibrasi, diuji pada set data RGB-D), Yang dkk. 2025
    (segmentasi apel RGB-D).
  - Tinjauan terdahulu (R): Gong dkk. 2025 (86 kajian deteksi buah), Sutriani
    dkk. 2025 (10 kajian YOLO sawit).
  - Luar pertanian (T): Das dkk. 2026 (tinjauan pelacakan banyak objek),
    Song dkk. 2025 (tinjauan rekonstruksi 3D multi-pandang).

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

