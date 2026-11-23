# Tugas Peninjau

Diperbarui 23 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.15 Zhang dkk. 2024 masuk tabel kepastian?** Tabel kepastian di
  naskah (Table "Certainty of the main findings") dihitung dari
  [`../topik/bukti/kepastian_klaim.tsv`](../topik/bukti/kepastian_klaim.tsv).
  Usul AI: tambah satu baris untuk temuan "depth untuk membuang latar atau
  buah baris belakang membawa hitungan lebih dekat ke acuan". Zhang dkk. 2024
  membuang deteksi tomat yang lebih jauh dari ambang kedalaman prediksi
  (Depth Anything), dengan detektor dan pelacak yang sama. Pada 70 video,
  ketepatan hitung terhadap hitung tangan naik dari 81,17% tanpa langkah itu
  menjadi 83,87–93,80% pada tujuh ambang yang diuji (Tabel 3, baris
  1258–1341 di `teks/zhang2024counting.txt`). Arah: mendukung temuan. Catatan:
  kedalamannya hasil prediksi dari citra, bukan dari sensor, dan ambang dipilih
  pada video yang sama. Dampak: baris temuan itu berubah dari 6 menjadi 7
  perbandingan; tingkat kepastiannya dihitung ulang oleh skrip.

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

