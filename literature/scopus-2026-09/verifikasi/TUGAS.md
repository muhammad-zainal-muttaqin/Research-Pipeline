# Tugas Peninjau

Diperbarui 19 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.5 Empat PDF berisi versi lain dari dokumen yang tercatat di
  Scopus.** Apakah versi ini diterima sebagai teks lengkap kajian yang sama,
  atau versi terbitnya dicari dulu? Isi dan penulisnya sama, tetapi
  dokumennya berbeda:
  - Bolouri dkk. 2024, *CottonSense* (C1): PDF adalah tesis magister Texas
    Tech 2023, bukan artikel *Computers and Electronics in Agriculture*.
    Buka [bolouri2024cottonsense.pdf](../pdf/bolouri2024cottonsense.pdf).
  - Si dkk. 2026, *Citrus yield estimation ... video streams* (C1): PDF
    adalah pracetak SSRN berbahasa Inggris dengan judul lain, bukan artikel
    *Journal of Fruit Science*. Buka [si2026citrus.pdf](../pdf/si2026citrus.pdf).
  - Yamamoto dkk. 2013, *Detection and counting of intact tomato fruits*
    (calon C2): Scopus mencatat makalah konferensi 2013; PDF adalah artikel
    *Sensors* 2014 berjudul *On Plant Detection of Intact Tomato Fruits*.
    Buka [yamamoto2013detection.pdf](../pdf/yamamoto2013detection.pdf).
  - Silwal dkk. 2015, *A hierarchical approach of apple identification*
    (calon C2): Scopus mencatat makalah konferensi ASABE 2015; PDF adalah
    artikel *Trans. ASABE* 2016. Buka
    [silwal2015hierarchical.pdf](../pdf/silwal2015hierarchical.pdf).

  Dampak bila versi ini ditolak: Bolouri dan Si keluar dari 214 kajian C1
  sampai versi terbitnya diperoleh, sehingga angka naskah berubah; Yamamoto
  dan Silwal kembali ke daftar
  [pdf_belum_ada.csv](../unduhan/pdf_belum_ada.csv).

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
  sebagian keliru.** Apakah tanaman dan platform 214 kajian multi-pengamatan
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
