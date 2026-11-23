# Tugas Peninjau

Diperbarui 23 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.17 Kelompok 1 PDF baru (23 November 2026).** Apakah kelompok di
  bawah ini benar? Teks lengkapnya ada di `teks/li2021yield.txt`. PDF ini
  terjemahan mesin berbahasa Inggris dari *postprint* di ChinaXiv, bukan
  versi penerbit, dan tabelnya tidak ikut diterjemahkan. Usul AI ditulis di
  [`../topik/penyaringan/teks_lengkap.txt`](../topik/penyaringan/teks_lengkap.txt)
  sesudah disetujui.

  | Kajian | Kelompok di tahap abstrak | Usul dari teks lengkap | Alasan dan tempat di teks |
  |---|---|---|---|
  | Li dkk. 2021, taksiran hasil per pohon apel dengan YOLOv5 ringan dan jaringan saraf BP | C2 (hitung dari satu foto) | C2 tetap | Drone membawa kain putih di belakang pohon dan memotret pohon dari jarak 1,2 m (baris 146–149). Jumlah buah dan luas kotak dari citra menjadi masukan jaringan saraf BP. Acuannya hasil panen yang ditimbang per pohon (93 pohon, baris 193–202). Tidak ada penggabungan antarcitra pohon yang sama. Pada 13 pohon uji, RMSE 1,4021 kg dan MAPE 6,25% (baris 413–417). Galat relatif paling besar 7% dengan kain putih dan 13% tanpa kain putih, masing-masing pada 10 pohon (baris 423–443). Hitungan buah tidak dibandingkan dengan hitung tangan. Pola ini sama dengan Cheng dkk. 2015 |

  Dampak bila disetujui: peta naik dari 893 menjadi 894 kajian (C2 156),
  dan yang dinilai dari teks lengkap menjadi 928.

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

