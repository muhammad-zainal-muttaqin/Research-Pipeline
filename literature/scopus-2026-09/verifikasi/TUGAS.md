# Tugas Peninjau

Diperbarui 23 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.20 Kelompok 2 PDF baru (23 November 2026).** Apakah kelompok di
  bawah ini benar? Teks lengkapnya ada di `teks/kadir2022analysis.txt` dan
  `teks/gunawan2026drone.txt`. Usul AI ditulis di
  [`../topik/penyaringan/teks_lengkap.txt`](../topik/penyaringan/teks_lengkap.txt)
  sesudah disetujui.

  | Kajian | Kelompok di tahap abstrak | Usul dari teks lengkap | Alasan dan tempat di teks |
  |---|---|---|---|
  | Kadir dkk. 2022, *Analysis of Ground FFB Detection via RealSense Camera* (ICSIMA 2022) | C3 (kajian sawit) | C3 tetap; kode sawit tetap "deteksi tandan, di tanah, RGB dan depth, satu pandang, tanpa kelas kematangan" | YOLOv4 dan YOLOv4-tiny mendeteksi tandan di tanah untuk mesin pengumpul tandan otomatis. Kamera RealSense D435i memberi jarak tandan untuk lengan mesin. Data 1.104 citra latih, 105 validasi, 47 uji, satu kelas (baris 296–298). Hasil dievaluasi dengan mAP, IoU, dan F1; F1 kedua model 0,96 (baris 379–381). Tandan tidak dicacah dan tidak ditautkan antarcitra |
  | Gunawan dkk. 2026, *Drone and Deep Learning-Based Instrumentation for Palm Fruit Detection and Yield Measurement: A Southeast Asian Roadmap* (*IEEE Instrumentation & Measurement Magazine*) | R (tinjauan terdahulu) | R tetap | Tinjauan naratif tanpa metode pencarian tentang drone dan pembelajaran mendalam untuk deteksi tandan dan taksiran hasil di Malaysia, Indonesia, dan Thailand. Isinya menyusun anggaran ketidakpastian taksiran hasil dari drone; galat hitung detektor dinilai terhadap hitungan petak contoh. Hitung ganda antarcitra, pelacakan, dan penautan antarpandang tidak dibahas (tidak ada di teks) |

  Dampak bila disetujui: peta naik dari 896 menjadi 898 kajian (C3 148,
  R 115), dan yang dinilai dari teks lengkap menjadi 933.

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

