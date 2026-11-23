# Tugas Peninjau

Diperbarui 23 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.16 Kelompok 5 PDF baru (23 November 2026, zip akses terbuka
  tambahan).** Apakah kelompok di bawah ini benar? Teks lengkapnya ada di
  `teks/<kunci>.txt`. Usul AI ditulis di
  [`../topik/penyaringan/teks_lengkap.txt`](../topik/penyaringan/teks_lengkap.txt)
  sesudah disetujui.

  | Kajian | Kelompok di tahap abstrak | Usul dari teks lengkap | Alasan dan tempat di teks |
  |---|---|---|---|
  | Lou dkk. 2024, pelacakan jeruk yang bergoyang saat dipetik (YOLOv5s dan DeepSORT) | C5 (depth atau 3D) | **C1, pelacakan (M3), video; buah tidak dicacah** | Kamera ponsel dan kamera depth di posisi tetap, 30–60 cm di depan jeruk yang digoyang tangan untuk meniru robot pemetik; 21 video (baris 208–229). DeepSORT menjaga identitas jeruk yang sama antarbingkai, dan pelacakannya dievaluasi: MOTA rata-rata naik dari 59,4% menjadi 68,6% dan pergantian identitas turun dari 78 menjadi 46 pada 3 video (Tabel 7). Depth hanya dipakai membuang jeruk di belakang. Sama dengan Li dkk. 2022 (lokasi buah untuk robot, dipindah ke C1). Alternatif: tetap C5 bila pelacakan untuk pemetikan, bukan untuk inventaris, dianggap di luar C1 |
  | Xiao dkk. 2024, deteksi buah *Camellia oleifera* tertutup (YOLO-DCL) | C2 (hitung dari satu foto) | **Dikeluarkan, E5 (deteksi tanpa hitung atau evaluasi)** | Hasil yang dilaporkan hanya mAP 92,7%, presisi, dan *recall*. Hitungan hanya ditampilkan pada citra contoh, misalnya "识别出1个混合遮挡（HO）果实、1个无遮挡（NO）" (baris 795–810, teks dari OCR), tanpa pembanding. Sama dengan Kiran dkk. 2025 |
  | Xu dkk. 2025, deteksi dan hitung tandan anggur dengan citra dan teks (GDCNet) | C2 | C2 tetap | "多模态" berarti citra dan teks, bukan depth. Hitungan per citra: MAE 1,65 dan RMSE 2,48 (abstrak) |
  | Cheng dkk. 2015, taksiran hasil awal apel Gala (pengolahan citra dan SVM) | C2 | C2 tetap | Satu citra tajuk sisi barat per pohon ("获取果树西面图像", baris 118); jumlah buah dan empat fitur lain menjadi masukan SVM; acuan hasil panen per pohon (15 pohon uji, MAPE 13%) |
  | Chen dkk. 2024, tinjauan persepsi robot pemetik di seluruh kebun | R (tinjauan terdahulu) | R tetap | Tinjauan |

  Dampak bila semua disetujui: peta naik dari 889 menjadi 893 kajian (C1
  248, C2 155, C5 108, R 113), yang dinilai dari teks lengkap 927, dan yang
  dikeluarkan 34.

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

