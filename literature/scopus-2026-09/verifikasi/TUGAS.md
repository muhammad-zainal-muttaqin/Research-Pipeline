# Tugas Peninjau

Diperbarui 24 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.22 Laporan ganda Chowdhury dkk. (24 November 2026).** Apakah
  Chowdhury dkk. 2024 dikeluarkan sebagai laporan kedua dari kajian yang
  sudah masuk (E8), dengan Chowdhury dkk. 2025 sebagai laporan yang dihitung?
  Bandingkan Tabel 1 di `teks/chowdhury2024oil.txt` (baris 393–439) dengan
  Tabel I di `teks/chowdhury2025comparative.txt` (baris 433–483).

  | Kajian | Isi | Keadaan sekarang | Usul |
  |---|---|---|---|
  | Chowdhury dkk. 2024, *Oil Palm Fresh Fruit Branch Ripeness Detection Using YOLOV6 Algorithm* (Lecture Notes in Mechanical Engineering) | YOLOv6s dan YOLOv6m, empat kelas kematangan, 80 citra dari kebun di Selangor (baris 205–209) | Masuk peta, kelompok sawit (C3) | Dikeluarkan, E8 (laporan kedua dari kajian yang sudah masuk) |
  | Chowdhury dkk. 2025, *Comparative Study of Different YOLO Variants for Ripeness Detection of Palm Oil Fresh Fruit Bunches* (IEEE ROMA 2025) | YOLOv5s, YOLOv5m, YOLOv6s, YOLOv6m, dan YOLOv7 dengan pengaturan latih yang sama (416, *batch* 16, 100 *epoch*), 2.000 citra dari kebun di Selangor (baris 330–336) | Masuk peta, kelompok sawit (C3) | Tetap; laporan yang lebih lengkap |

  Alasan: ke-14 nilai YOLOv6 di kedua tabel sama persis (presisi, *recall*,
  F1, FPS, dan nilai per kelas untuk dua model). Akurasi per kelas pada citra
  uji di laporan 2024 disebut AP di laporan 2025. Penulis pertama dan kedua
  sama, dan laporan 2025 tidak mengutip laporan 2024. Ukuran data yang
  dinyatakan berbeda (80 dan 2.000 citra), sehingga salah satu deskripsi data
  tidak sesuai dengan hasilnya; kajian tetap dihitung sekali. Pilihan lain:
  keduanya tetap masuk, dan tumpang tindihnya hanya dicatat di ringkasan
  (keadaan sekarang).

  Dampak bila disetujui: peta turun dari 900 menjadi 899 kajian (C3 148),
  laporan yang dikeluarkan pada tahap teks lengkap naik dari 35 menjadi 36
  (E8 2 menjadi 3), dan kajian sawit di pohon dan di tanah kembali 5. Angka
  naskah berubah lewat makro.

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

