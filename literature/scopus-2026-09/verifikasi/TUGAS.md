# Tugas Peninjau

Diperbarui 18 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **Teks lengkap: apakah 32 perubahan kelompok dari pembacaan PDF sudah
  benar?** Korpus kini hanya memuat artikel yang PDF-nya ada (480 dinilai,
  468 masuk peta). Buka [log_perubahan.csv](log_perubahan.csv) dan saring
  kolom `diubah_oleh` = "AI, belum disetujui peninjau" (baris paling atas,
  bertanggal 2026-11-18). Setiap baris memuat artikel, kelompok sebelum dan
  sesudah, dan alasan dari teks lengkap: 17 artikel pindah ke C1 (hitung dari
  banyak pengamatan buah yang sama), 3 pindah ke kelompok lain, dan 12
  dikeluarkan (4 pascapanen atau laboratorium, 1 tanpa deteksi tingkat buah,
  7 hanya deteksi tanpa evaluasi hitungan). Dampaknya: bila ada yang
  dibatalkan, angka naskah berubah (jumlah kajian, kelompok, dan statistik
  C1). Setelah disetujui, ubah kode `AI-TL` menjadi `AI-Tugas` di
  `.teknis/log_perubahan.csv`, jalankan `tools/scopus/verifikasi_log_manusia.py`,
  dan hapus `\authorcheck` pada kalimat persetujuan di Metode
  (`manuscript/source/main6-body.tex`, subseksi *Study selection and
  screening*).

- [ ] **5.7 Bagian naskah yang hanya dapat diisi penulis.** Apakah peran
  penulis, sumber dana, deklarasi kepentingan, dan ucapan terima kasih sudah
  benar? Kerangkanya sudah ada di akhir naskah, sebelum Data availability
  (`manuscript/source/main6-body.tex`, cari `\authorcheck`; di PDF tercetak merah).
  Hal yang harus diputuskan penulis:
  - Peran CRediT kedua penulis (usulan sudah terisi).
  - Ada atau tidaknya dana hibah (teks bawaan menyatakan tidak ada).
  - Apakah keikutsertaan kedua penulis dalam makalah SawitMVC yang dikutip
    perlu diungkapkan.
  - Isi ucapan terima kasih, atau hapus seksinya.
  - Abstrak kini 288 kata. Periksa batas kata dan kebijakan AI di *Guide for
    Authors* jurnal *Computers and Electronics in Agriculture*.

  Hapus semua `\authorcheck` sebelum dikirim. Dampaknya: tanpa isian ini,
  naskah belum dapat dikirim.
- [ ] **F.4 Kode buta 20 artikel C1 acak oleh Bu Fatma.**
  Buka [sampel_fatma_C1.xlsx](cek-5-kode-ulang/sampel_fatma_C1.xlsx) dan isi
  kolom berlatar kuning. Arti setiap pilihan ada di lembar `pilihan`. Hasilnya
  menjadi satu-satunya ukuran kesepakatan manusia untuk label C1. Naskah saat
  ini menyatakan bahwa label C1 dikode ulang oleh model.
