# Tugas Peninjau

Diperbarui 23 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.12 Perbandingan pada data yang sama dari PDF baru: masukkan ke tabel
  kepastian?** Tabel kepastian di naskah (Table "Certainty of the main
  findings") dihitung dari
  [`../topik/bukti/kepastian_klaim.tsv`](../topik/bukti/kepastian_klaim.tsv).
  Gambar hasil terlapor (Gambar F12) dihitung dari
  [`../topik/bukti/nilai_terlapor.csv`](../topik/bukti/nilai_terlapor.csv).
  Usul AI, sudah dicocokkan dengan teks lengkap:
  - **Linker 2017 (apel, hasil panen per pohon): tambah satu baris ke
    temuan "menambah pandang atau bingkai tidak selalu menurunkan galat
    hitung".** Hitungan dari dua sampai enam citra malam per pohon
    digabung dengan regresi, tanpa menautkan buah antarcitra. Simpangan
    baku galat per pohon (buah per pohon) pada data 2013 (Tabel 4, baris
    606–626 di `teks/linker2017procedure.txt`):

    | Kamera | Satu sisi | Dua sisi |
    |---|---:|---:|
    | Tiga kamera | 78 | 78 |
    | Bawah dan tengah | 97 | 86 |
    | Bawah dan atas | 95 | 105 |
    | Tengah dan atas | 80 | 79 |

    Pada 23 pohon validasi Juli 2014 (Tabel 5 dan 6, sepuluh model),
    tiga kamera memberi 132–180 buah per pohon dengan dua sisi dan 137–185
    dengan satu sisi; dua kamera bawah dan atas memberi 135–175. Penulis
    menulis bahwa tiga kamera "only slightly better" daripada dua, dan satu
    sisi tidak memperburuk hasil secara nyata (baris 445–456). Arah:
    mendukung temuan. Dampak (sudah dicoba lalu dikembalikan): baris temuan
    itu di tabel kepastian berubah dari 8 menjadi 9 perbandingan, 9 kajian,
    dan 9 kelompok riset; tingkatnya tetap "Low".
  - **Kalimat naskah untuk Linker 2017.** Linker belum dikutip di badan
    naskah. Usul satu kalimat di Seksi 4, butir *(3) An unlinked extra view
    helps only when something absorbs its duplicates*, sesudah kalimat
    Isobe: "\citet{linker2017procedure} combined counts from two to six night
    images of each apple tree in regression models; on 23 validation trees,
    the standard deviation of the per-tree error was 132--180 apples with
    three cameras on both sides and 137--185 with one side, and two cameras
    did almost as well as three." Dampak: paragraf itu bertambah sekitar 45
    kata.
  - **Li 2022 (apel, dua kamera stereo dekat dan jauh): usul tidak
    dimasukkan.** Yang diukur adalah galat posisi satu buah (median 5,73 mm
    kamera dekat, 8,25 mm kamera jauh, 6,43 mm gabungan berbobot; Tabel III),
    bukan galat hitung. Tidak ada temuan di tabel kepastian yang membahas
    galat posisi. Kajian ini sudah diuraikan di Seksi 5 (asosiasi
    geometris).
  - **Gambar F12: usul tidak ada yang ditambahkan.** Panel (a) membandingkan
    hitungan yang ditautkan dengan yang tidak ditautkan, dan panel (b)
    membandingkan aturan hitung sesudah pelacakan. Semua lengan Linker tidak
    menautkan buah, dan Li 2022 tidak melaporkan hitungan, jadi keduanya
    tidak punya pasangan pembanding di gambar itu.

  Jawab "ya" untuk menerapkan semua usul di butir ini, atau sebutkan bagian
  yang ditolak.

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

