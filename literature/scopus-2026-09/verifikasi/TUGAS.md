# Tugas Peninjau

Diperbarui 18 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **5.7 Bagian naskah yang hanya dapat diisi penulis.** Apakah peran
  penulis, sumber dana, deklarasi kepentingan, dan ucapan terima kasih sudah
  benar? Kerangkanya sudah ada di akhir naskah, sebelum Data availability
  (`manuscript/source/main6-body.tex`, cari `\authorcheck`; di PDF tercetak merah).
  Hal yang harus diputuskan penulis:
  - Peran CRediT kedua penulis (usulan sudah terisi).
  - Ada atau tidaknya dana hibah (teks bawaan menyatakan tidak ada).
  - Isi ucapan terima kasih, atau hapus seksinya.
  - Abstrak kini 288 kata. Periksa batas kata dan kebijakan AI di *Guide for
    Authors* jurnal *Computers and Electronics in Agriculture*.

  Hapus semua `\authorcheck` sebelum dikirim. Dampaknya: tanpa isian ini,
  naskah belum dapat dikirim.
- [ ] **A.1 Tanaman dan platform di Lampiran A dikode dari abstrak, dan
  sebagian keliru.** Apakah tanaman dan platform 215 kajian multi-pengamatan
  (C1) perlu dikode ulang dari teks lengkap? Saat ini keduanya diisi aturan
  kata kunci pada judul dan abstrak (`tools/scopus/kode_bukti.py`). Tiga
  kesalahan sudah terbukti dari teks lengkap:
  - Shimomoto dkk. 2025, *Predicting Sweet Pepper Yield*: tertulis "Tomato,
    pepper", padahal kajiannya hanya paprika. Kata "tomato" muncul karena
    abstrak menyebut sistem tomat mereka sebelumnya.
  - Liu dkk. 2018, *Robust fruit counting*: tanaman tertulis "Not stated",
    padahal kajiannya jeruk dan apel.
  - Stein dkk. 2016, *Image based mango fruit detection*: platform tertulis
    "Not stated", padahal mereka memakai kendaraan darat tak berawak
    ("Shrimp").

  Tinjauan independen atas lampiran menemukan pola kesalahan aturan yang
  sama:
  - Kata "vehicle" di dalam "unmanned aerial vehicle" membuat kajian UAV
    juga tercatat "Ground vehicle or robot", misalnya Piazolo dkk. 2026 dan
    Zheng dkk. 2023 (*Efficient*).
  - "Cherry tomato" tercatat sebagai dua tanaman, tomat dan ceri.
  - Kata "orange" sebagai warna kematangan tercatat sebagai jeruk (Awal dkk.
    2026, Viveros dkk. 2024).
  - "Laboratory" muncul dari "non-laboratory", dan pabrik sawit tercatat
    "Laboratory" (Aji dkk. 2021, Shiddiq dkk. 2023).

  Buka [matriks_bukti.csv](../topik/bukti/matriks_bukti.csv), saring kolom
  `kode` = C1, lalu lihat kolom `tanaman` dan `platform`. Dampak bila
  disetujui: Lampiran A, gambar tanaman dan sensor di bahan tambahan (S4),
  serta makro jumlah tanaman dan platform berubah.
- [ ] **A.3 Label 17 kajian C1 belum diperiksa peninjau.** Apakah label
  cara penghubungan, cara foto diambil, acuan hitungan, dan metrik untuk 17
  kajian yang masuk C1 pada tahap teks lengkap sudah benar? Kajian itu masuk
  setelah Cek 5 disetujui (19 Oktober 2026), sehingga labelnya diisi model
  dari teks lengkap tanpa pemeriksaan peninjau. Buka
  [kode_ulang_C1.csv](cek-5-kode-ulang/kode_ulang_C1.csv) dan saring kolom
  `diisi_oleh` = "AI dari teks lengkap, belum diperiksa peninjau". Dampak bila
  ada label yang diubah: angka mekanisme di naskah dan Lampiran A berubah.
