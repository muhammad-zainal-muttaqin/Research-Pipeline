# Tugas Peninjau

Diperbarui 24 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.23 Kelompok 3 PDF baru (24 November 2026).** Apakah kelompok di
  bawah ini benar? Teks lengkapnya ada di `teks/xia2023lightweight.txt`,
  `teks/dhonju2024harvest.txt`, dan `teks/yuchao2025review.txt`. Teks Xia
  dan Yuchao berbahasa Mandarin dengan abstrak berbahasa Inggris. Teks Dhonju
  adalah Bab 8 tesis penulis yang memuat makalah Acta Horticulturae itu.
  Usul AI ditulis di
  [`../topik/penyaringan/teks_lengkap.txt`](../topik/penyaringan/teks_lengkap.txt)
  dan [`../topik/bukti/mekanisme_C1.txt`](../topik/bukti/mekanisme_C1.txt)
  sesudah disetujui.

  | Kajian | Kelompok di tahap abstrak | Usul dari teks lengkap | Alasan dan tempat di teks |
  |---|---|---|---|
  | Xia dkk. 2023, *A Lightweight Fruit Load Estimation Model for Edge Computing Equipment* (*Smart Agriculture*) | Hitung dari satu foto (C2) | Pindah ke gabungan beberapa pengamatan (C1): penampilan dan pelacakan (M2+M3), video sepanjang baris (V), tanpa kelas; acuan hitung buah yang diperiksa tangan di video; metrik hitung dan deteksi | Jeruk di pohon direkam dengan ponsel genggam berjalan sepanjang baris, 40 video (baris 138–142). Detektor FairMOT dengan cabang fitur penampilan, dan asosiasinya diganti algoritme Byte. Buah dihitung sebagai ID yang bertahan lebih dari 5 bingkai (baris 200). Pasangan buah yang sama antarcitra berurutan dilabeli (baris 167). Pada 10 video uji (14 sampai 125 buah per pohon), akurasi hitung rata-rata 91,61%, R² 0,9858, RMSE 4,17 buah (baris 583; Tabel 5). Tabel 5 adalah perbandingan pada data yang sama: mengganti asosiasi FairMOT dengan Byte menaikkan akurasi hitung dari 85,67% ke 86,98% (ResNet34), 90,75% ke 91,53% (HRNet18), dan 85,76% ke 91,61% (CSPDarkNet53 dengan PAFPN) |
  | Dhonju dkk. 2024, *Harvest bin placement based on machine vision data in mango orchards* (Acta Horticulturae) | Hitung dari satu foto (C2) | C2 tetap | Hitungan mangga per 3,5 m sisi baris diambil dari sistem kamera kendaraan yang sudah ada (baris 139–142), lalu dijumlahkan sepanjang dua sisi baris untuk menempatkan bak panen 400 kg (baris 179–191). Kamera kiri dan kanan memotret dua baris pohon yang berbeda, jadi penjumlahan itu tidak menggabungkan dua pandang atas pohon yang sama. Jumlah bak 46 dan 53, yaitu 106% dan 112% dari kebutuhan menurut catatan *packhouse* (baris 219–223). Pelacakan dan hitung ganda tidak dibahas |
  | Yuchao dkk. 2025, *Review on lightweight deep learning networks for object detection in crops* (*Journal of Chinese Agricultural Mechanization*) | Tinjauan terdahulu (R) | R tetap | Tinjauan naratif tentang jaringan ringan (MobileNet, ShuffleNet, EfficientNet, GhostNet, dan versi ringan YOLO; baris 896–1012) untuk deteksi buah, malai serealia, dan hama penyakit. Teks menyebut penelusuran kajian 5 tahun terakhir tanpa basis data, kueri, atau kriteria (baris 889). Pencacahan disebut sekali, untuk satu kajian jeruk (baris 1289). Pelacakan, hitung ganda, dan penautan antarpandang tidak dibahas |

  Dampak bila disetujui: peta naik dari 899 menjadi 902 kajian (C1 249,
  C2 158, R 117), dan yang dinilai dari teks lengkap menjadi 938. Angka
  naskah berubah lewat makro. Xia dkk. 2023 dapat masuk naskah main7 sebagai
  perbandingan asosiasi pada data yang sama (seksi pelacakan).


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

