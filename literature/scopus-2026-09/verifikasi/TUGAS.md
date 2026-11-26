# Tugas Peninjau

Diperbarui 27 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.28 Kelompok 12 PDF baru dari folder Drive "dariemail" (27 November
  2026).** Apakah kelompok di bawah ini benar? Teks lengkapnya ada di
  `teks/<kunci>.txt`; nomor baris di kolom alasan merujuk berkas itu. Teks
  `santhi2026streamlined` adalah hasil OCR karena PDF-nya berupa pindaian. Usul AI
  ditulis di
  [`../topik/penyaringan/teks_lengkap.txt`](../topik/penyaringan/teks_lengkap.txt)
  sesudah disetujui. Tiga baris yang perlu perhatian khusus: Sarron dkk. 2023 dan
  Maheswari dkk. 2025 pindah ke kelompok multi-observasi, dan Scalisi dkk. 2023
  dikeluarkan.

  | Kajian | Kelompok di tahap abstrak | Usul dari teks lengkap | Alasan dan tempat di teks |
  |---|---|---|---|
  | Dahlan dkk. 2026, deteksi kematangan TBS dengan YOLO (`dahlan2026detecting`) | Pencitraan TBS kelapa sawit (C3) | C3 tetap; tugas deteksi tandan dalam adegan (DET), lokasi diubah dari "tidak disebut" menjadi citra dari set data publik (WEB) | 2.672 citra TBS empat kelas dari Mendeley, Kaggle, dan Roboflow, sebagian dari bingkai video (baris 227–250). mAP50 validasi 88% untuk YOLO11n dan 87,1% untuk YOLOv9c (baris 289–291). Tidak ada pencacahan |
  | Sari dkk. 2023, kematangan TBS dengan K-means (`sari2023ripeness`) | Pencitraan TBS kelapa sawit (C3) | C3 tetap; tugas klasifikasi kematangan citra tandan (KLS), lokasi diubah dari "tidak disebut" menjadi di kebun tanpa keterangan posisi tandan (KEBUN), modalitas RGB | 120 foto ponsel 4000×3000 piksel atas TBS hasil panen 2021 dari kebun di Kalimantan Timur dan Utara, dipotong ke tandan (baris 78–79, 98–99, 243–247). Uji pada 40 citra: 36 benar (baris 630–633) |
  | Deng dkk. 2020, TSGYE, estimasi hasil anggur dua tahap (`deng2020tsgye`) | Pencacahan atau estimasi hasil dari satu pandang (C2) | C2 tetap | Tandan anggur dideteksi YOLOv4 di WGISD (300 citra), lalu buah anggur di dalam kotak dicacah dengan transformasi Hough (baris 159–161, 229–232). Acuan hitung dari anotasi tangan 58 citra uji; galat per kultivar dalam Tabel 1 (baris 225–236). Setiap citra dicacah sendiri |
  | Shao dkk. 2024, pencacahan buah dengan fitur konteks dan pemasangan titik (`shao2024plant`) | C2 | C2 tetap | Jaringan titik (turunan P2PNet) pada 1.120 citra apel berlabel titik, 112 citra uji (baris 179–185). MAE 0,67 dan RMSE 0,98 per citra (baris 228–232) |
  | Goes dkk. 2026, deteksi dan pencacahan pisang (`goes2026detection`) | C2 | C2 tetap | 938 foto ponsel dari kebun dan pasar di Goa, satu kelas "buah pisang" (baris 302–330). RF-DETR: MAE 0,17 dan hitungan tepat pada 87,23% citra uji (baris 760–762). Citra pasar tidak membuat kajian keluar karena sebagian citra diambil di kebun |
  | Santhi dkk. 2026, kerangka ringkas estimasi hasil anggur (`santhi2026streamlined`) | C2 | C2 tetap; pilihan lain: dikeluarkan, E5 (tanpa evaluasi hitungan) | Deteksi tandan dengan Faster R-CNN pada citra tunggal WGISD, lalu hitungan buah anggur per tandan diperkirakan dengan regresi CNN (baris 160–161, 205–211, 227–238). SORT disebut untuk mencegah hitung ganda (baris 212–217), tetapi WGISD berupa citra lepas dan pelacakan tidak dievaluasi. MAE didefinisikan (baris 327–336), tetapi nilainya tidak dilaporkan. Hasil yang dilaporkan hanya akurasi 95,8% MINN untuk kelas hasil rendah, sedang, dan tinggi (baris 380–389, Gambar 7) |
  | Maheswari dkk. 2025, MangoYieldNet (`maheswari2025mangoyieldnet`) | C2 | **Pindah ke C1, penjumlahan tanpa koreksi (M0), beberapa pandang diskret (D)**; pilihan lain: C2 tetap | Setiap pohon difoto dari dua sisi, 5 m dari pohon; 556 citra dari 278 pohon (baris 18, 252–254). Hitungan per pohon dari kedua citra dibandingkan dengan hitungan petani: total 26.929 terhadap 28.345, R² 0,98 (baris 631–639). Penulis menyebut hitung ganda karena dua sisi sebagai sumber galat (baris 661–665), sehingga kedua sisi dijumlahkan tanpa koreksi. Kalimat yang menyatakan penjumlahan secara langsung tidak ada |
  | Sarron dkk. 2023, koreksi jumlah deteksi mangga (`sarron2023fruit`) | C2 | **Pindah ke C1, koreksi statistik (M1), beberapa pandang diskret (D)** | Dua citra dari sisi berlawanan untuk setiap pohon; "detected count" adalah jumlah deteksi pada kedua citra (baris 184–187, 206). Jumlah itu dikoreksi dengan regresi terhadap hitungan dua pakar di 325 pohon dari 27 kebun: R² 0,66 dan NRMSE 11% dengan kovariat wilayah dan sistem tanam, dibandingkan dengan R² 0,34 untuk regresi sederhana (baris 25–32). Sarron dkk. 2020, dengan cara yang sama, sudah berkode C1 M1 |
  | Scalisi dkk. 2023, Green Atlas Cartographer pada apel dan pir (`scalisi2023green`) | C2 | **Dikeluarkan, E5 (tanpa evaluasi hitungan)**; pilihan lain: C1 bila pemakaian platform tanpa validasi dianggap cukup | Jumlah buah per pohon, ukuran, dan warna diambil dari keluaran platform komersial (dua kamera RGB dan LiDAR), lalu dikorelasikan dengan geometri tajuk per petak (baris 96–117). Jumlah buah tidak dibandingkan dengan hitungan lapangan. Validasinya dirujuk ke Scalisi dkk. 2021 (baris 107–108), yang sudah masuk korpus sebagai C1 |
  | Khiem dkk. 2026, klasifikasi dan pencacahan tomat dengan YOLOv11 dan SAHI (`khiem2026approach`) | Atribut kelas disertai pencacahan dari citra tunggal (C4) | C4 tetap | 904 citra dari Kaggle, VegNet, dan sumber lain, tiga kelas kematangan (baris 137–143). Pada 135 citra uji (1.996 tomat), hitungan per kelas tepat 95% dengan SAHI dan 84% tanpa SAHI (baris 306–359, Tabel 2) |
  | Langpoklakpam dkk. 2025, nanas dari drone: deteksi, kematangan, dan bobot (`langpoklakpam2025automated`) | C4 | C4 tetap; pilihan lain: dikeluarkan, E5 (deteksi tanpa pencacahan) | Video drone 2 m di atas barisan nanas di Nagaland, 2.057 citra, uji 175 citra (baris 342–355, 410–412). Deteksi dengan kelas kematangan (presisi 98%, 92%, dan 98%), ukuran buah, dan bobot dari 100 buah yang ditimbang di laboratorium (baris 31–49, 403–409). Buah tidak dicacah. Usul C4 karena kriteria inklusi menerima deteksi dengan atribut kelas pada buah di tanaman |
  | Piani dkk. 2025, ukuran dan warna apel dari kamera stereo dan monokular (`piani2025evaluating`) | Deteksi buah dengan depth, 3D, atau non-RGB (C5) | C5 tetap | Kamera stereo RealSense D435i dan kamera monokular dengan depth dari Depth Anything V2, dipasang diam 2,5 m dari empat pohon apel; 17 bingkai per kamera (baris 128–138). Dari 66 buah, RealSense mencacah 56 dan kamera monokular rata-rata 19 (baris 243–252). Bias ukuran 0,59 mm untuk stereo (baris 23–25). Buah tidak ditautkan antarbingkai |

  Dampak bila semua usul disetujui: peta naik dari 907 menjadi 918 kajian
  (multi-observasi 251, satu pandang 162, sawit 151, kelas pada citra tunggal 38,
  depth 110), yang dinilai dari teks lengkap menjadi 955, yang dikeluarkan
  37, dan yang tidak diperoleh 63. Angka naskah berubah lewat makro. Dua kajian
  baru di kelompok multi-observasi dapat menambah contoh penjumlahan dua sisi
  di naskah main7, tetapi teksnya tidak diubah tanpa persetujuan.

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

