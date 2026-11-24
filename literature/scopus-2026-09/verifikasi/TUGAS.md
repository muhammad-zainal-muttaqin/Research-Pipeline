# Tugas Peninjau

Diperbarui 24 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.21 Kelompok 2 PDF baru (24 November 2026).** Apakah kelompok dan
  kode di bawah ini benar? Teks lengkapnya ada di `teks/chowdhury2024oil.txt`
  dan `teks/dutta2025application.txt`. Usul AI ditulis di
  [`../topik/penyaringan/teks_lengkap.txt`](../topik/penyaringan/teks_lengkap.txt)
  dan [`../topik/bukti/kode_C3.txt`](../topik/bukti/kode_C3.txt) (baris idx
  1704) sesudah disetujui.

  | Kajian | Kelompok di tahap abstrak | Usul dari teks lengkap | Alasan dan tempat di teks |
  |---|---|---|---|
  | Chowdhury dkk. 2024, *Oil Palm Fresh Fruit Branch Ripeness Detection Using YOLOV6 Algorithm* (Lecture Notes in Mechanical Engineering) | C3 (kajian sawit); kode dari judul saja: deteksi tandan, lokasi tidak disebut, RGB, satu pandang, kelas kematangan per tandan | C3 tetap; lokasi berubah dari "tidak disebut" menjadi "di pohon dan di tanah" (CAMPUR); kode lain tetap | YOLOv6s dan YOLOv6m mendeteksi tandan dengan empat kelas kematangan (mentah, kurang matang, matang, lewat matang). Data 80 citra dari satu kebun di Selangor, dibagi 80:20 latih dan uji (baris 205–209). Teks hanya menyebut kebun, tetapi contoh citra menunjukkan satu tandan lewat matang di tanah dan tiga tandan di pohon (Fig. 3–6, halaman 193–194). YOLOv6m: presisi 0,369, *recall* 0,30, mAP50 0,369, mAP50-95 0,165 (Tabel 1, baris 393–415). Tandan tidak dicacah dan tidak ditautkan antarcitra |
  | Dutta dkk. 2025, *Application and Prospects of Artificial Intelligence (AI)-Based Technologies in Fruit Production Systems* (*Applied Fruit Science*) | R (tinjauan terdahulu) | R tetap | Tinjauan naratif tanpa metode pencarian (tidak ada basis data, kueri, atau kriteria inklusi di teks) atas lebih dari 110 penerapan AI pada produksi buah (baris 24–25). Seksinya: penyakit, alat digital, *grading*, identifikasi spesies, ukuran buah, jaringan saraf tiruan, mutu, dan status hara (baris 1110–1708). Pencacahan hanya muncul sebagai baris di Tabel 1 (taksiran hasil blueberry, deteksi dan pencacahan jeruk hijau; baris 190 dan 265). Hitung ganda antarcitra, pelacakan, dan penautan antarpandang tidak dibahas |

  Dampak bila disetujui: peta naik dari 898 menjadi 900 kajian (C3 149,
  R 116), dan yang dinilai dari teks lengkap menjadi 935. Angka naskah
  berubah lewat makro; isi naskah main7 belum tentu berubah (keduanya tidak
  memakai pengamatan ganda).

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

