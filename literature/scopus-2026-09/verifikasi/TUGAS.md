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

- [ ] **4.13 Kelompok 11 PDF baru (23 November 2026, dari zip unduhan).**
  Apakah kelompok di bawah ini benar? Teks lengkapnya ada di `teks/<kunci>.txt`.
  Usul AI ditulis di
  [`../topik/penyaringan/teks_lengkap.txt`](../topik/penyaringan/teks_lengkap.txt)
  sesudah disetujui. Dari 11 kajian, 4 berubah kelompok dan 7 tetap.

  | Kajian | Kelompok di tahap abstrak | Usul dari teks lengkap | Alasan dan tempat di teks |
  |---|---|---|---|
  | Wu dkk. 2025, hitung buah *Camellia oleifera* (YOLO-LGC) | C2 (hitung dari satu foto) | **C1, asosiasi geometris (M4), video** | Kamera OAK-D Pro merekam bingkai berurutan. Setiap buah diberi kubus 3D berjari-jari 20 mm. Kubus baru yang bertabrakan dengan kubus lama memakai identitas lama "从而确保同一个果实不会被多次计数" (baris 609–633). Hitungan per pohon dibandingkan dengan "实际数量" pada pohon uji, misalnya 193 lawan 200 dan 261 lawan 263 (Tabel 5, baris 1157–1200). Cara memperoleh jumlah sebenarnya tidak disebut |
  | Zhang dkk. 2024, hitung tomat per kematangan | C4 (kelas dari satu foto) | **C1, pelacakan (M3), video, per kelas** | Robot menyusuri baris dan merekam video. Pelacak BoT-SORT memberi identitas unik, lalu identitas dihitung per kelas (baris 728–845). Acuannya hitung tangan per video oleh pemeriksa yang menyusuri baris (baris 935–936). Ketepatan hitung 93,80% pada 70 video; tanpa penyaringan kedalaman 12,63 poin lebih rendah (abstrak). Cara menetapkan kelas satu identitas bila labelnya berganti tidak dinyatakan |
  | Wang dkk. 2024, awan titik paprika dari banyak sudut | C5 (depth atau 3D) | **C1, asosiasi geometris (M4), pandang diskret; buah tidak dicacah** | Lengan robot di rumah kaca memotret satu buah dari 6, 10, atau 15 sudut, dan awan titiknya disatukan menjadi satu model buah (baris 104–105, 203–205). Ini sama dengan Li dkk. 2022, yang dipindah ke C1 pada 23 November 2026. Alternatif: tetap C5 bila penyatuan pandang satu buah yang sudah dipilih dianggap bukan penautan identitas |
  | Yi dkk. 2021, deteksi jeruk Chunjian (FR-YOLOv4) | C2 (hitung dari satu foto) | **Dikeluarkan, E5 (deteksi tanpa hitung atau evaluasi)** | Hitungan didefinisikan sebagai jumlah deteksi dengan skor di atas 0,6 (baris 594–595), tetapi hasil yang dilaporkan hanya presisi, *recall*, mAP, dan laju bingkai (Tabel 2 dan 3). Tidak ada galat hitung terhadap hitung tangan. Sama dengan Kiran dkk. 2025 yang dikeluarkan dengan alasan ini |
  | Cheng dkk. 2015, jaringan saraf taksiran hasil apel | C2 | C2 tetap | Satu citra sisi barat per pohon ("获取果树西面图像"); jumlah apel dari citra menjadi salah satu masukan; acuan berat panen per pohon |
  | Zhang dkk. 2024, segmentasi tomat RGB dan depth | C5 | C5 tetap | Segmentasi buah dari RGB dan depth (baris 8); hanya mIoU dan akurasi piksel |
  | Liu dkk. 2022, lokasi dan ukuran jeruk navel | C5 | C5 tetap | Azure Kinect; posisi dan jari-jari dari bola yang dicocokkan ke awan titik; buah tidak dicacah |
  | Nordin dan Misro 2026, tinjauan kematangan sawit | R (tinjauan terdahulu) | R tetap | Tinjauan sistematis 15 kajian Scopus 2019–2025 |
  | Yang dkk. 2025, tinjauan stereo binokular di pertanian | R | R tetap | Tinjauan, termasuk lokalisasi buah untuk pemetikan |
  | Wang dkk. 2022, tinjauan LiDAR di pertanian | R | R tetap | Tinjauan; buah tidak dibahas per buah, jadi kaitannya dengan pencacahan lemah |
  | Cao dkk. 2024, survei *3D Gaussian splatting* | T (metode luar pertanian) | T tetap | Rekonstruksi 3D dari banyak pandang untuk SLAM dan mengemudi otonom |

  Dampak bila semua disetujui: peta naik dari 878 menjadi 888 kajian (C1
  247, C2 153, C5 108, R 112, T 86), yang dinilai dari teks lengkap 920, dan
  yang dikeluarkan 32. Angka naskah, Gambar F01–F12, Lampiran A, dan Ruang
  Baca dibuat ulang. Ketiga kajian C1 baru perlu ditambahkan ke prosa Seksi 5;
  Zhang dkk. 2024 juga relevan untuk Seksi 7 (kedalaman prediksi membuang buah
  baris belakang sebelum pelacakan).

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

