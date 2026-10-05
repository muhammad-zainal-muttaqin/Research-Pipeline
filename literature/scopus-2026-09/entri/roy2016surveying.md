# Surveying apple orchards with a monocular vision system

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `roy2016surveying` |
| Judul asli | Surveying apple orchards with a monocular vision system |
| Penulis | Roy, Pravakar; Isler, Volkan |
| Tahun | 2016 |
| Venue | IEEE International Conference on Automation Science and Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [roy2016surveying.pdf](../pdf/roy2016surveying.pdf)
- DOI resmi: https://doi.org/10.1109/coase.2016.7743500

## Gambaran Umum
Makalah ini (Roy dan Isler) menyajikan algoritma *computer vision* untuk mengumpulkan informasi terkait hasil panen di kebun apel dari citra satu kamera monokular, misalnya ponsel atau kamera digital. Keluarannya adalah jumlah apel dan diameter apel. Kontribusi teknis utama adalah saluran *structure from motion* (SfM) baru yang memakai kontur apel untuk menghasilkan pencocokan padat, sehingga apel yang sama pada bingkai berbeda terdaftar sebagai satu apel dan tidak terdaftar berulang kali.

Evaluasi memakai dua kumpulan data lapangan: Dataset1 berisi apel merah (965 citra, satu baris penuh kebun) dan Dataset2 berisi campuran apel merah dan hijau (464 citra, satu blok dengan enam pohon). Makalah melaporkan akurasi hitung 85,87% pada Dataset1 dan 81,3492% pada Dataset2. Untuk diameter, perbedaan rerata antara estimasi monokular dan stereo pada seratus apel tunggal adalah +0,90 cm dengan simpangan baku ±2,9 cm.

Makalah ini adalah naskah konferensi (disebut sebagai *preprint* yang diajukan ke konferensi otomasi) dan menyebut hasilnya sebagai hasil awal. Metode hitung dan estimasi diameter yang dipakai berasal dari laporan teknis terdahulu penulis yang sama, sehingga makalah ini berfokus pada tahap registrasi dan rekonstruksi.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil panen sebelum panen membantu petani menentukan jumlah pemetik, jumlah tempat penyimpanan, dan kontrak penjualan sejak awal musim. Sistem yang ada umumnya bekerja pada kondisi pencahayaan dan pencitraan terkendali (misalnya pada malam hari dengan pencahayaan buatan), atau memakai penglihatan stereo dan sensor aktif seperti pemindai laser. Menurut penulis, sistem demikian mahal dan kurang praktis.

Penulis menyebut dua kendala bagi SfM baku pada pengaturan ini. Pertama, fitur titik seperti SURF dan SIFT sering tidak terdeteksi pada apel; bila terdeteksi, adanya oklusi dan pantulan spekular menghasilkan kecocokan nol atau salah, dan kecocokan benar yang tersisa terlalu jarang untuk mengestimasi diameter. Kedua, metode SfM dasar gagal menyelaraskan gugusan apel padat lintas bingkai sehingga apel yang sama terdaftar berkali-kali (Gambar 4). Penulis juga menyebut bahwa metode berbasis satu citra tidak dapat dipakai untuk menaksir hasil seluruh kebun karena beberapa citra dapat memuat buah yang saling tumpang tindih.

## Ide Utama
Kontur apel dipakai langsung sebagai sumber pencocokan padat. Pada kebun, umumnya hanya tampak muka depan gugusan apel, dan perubahan kedalaman pada bagian apel yang terlihat dapat diabaikan, sehingga apel didekati sebagai lingkaran pada bidang datar. Dengan asumsi itu, kontur apel yang sama pada bingkai berurutan dihubungkan oleh transformasi afin.

Gagasan kedua adalah saluran SfM inkremental sepotong demi sepotong (*piecewise incremental*). Alih-alih menyelaraskan seluruh bingkai, penulis menyelaraskan tiap gugusan apel yang cocok secara terpisah, lalu merata-ratakan faktor skala lokal untuk menyelaraskan gugusan yang tidak punya pasangan pada rekonstruksi sebelumnya. Karena kamera tunggal memiliki ambiguitas skala global, ukuran dinormalisasi terhadap satu apel acuan yang diukur pengguna.

## Cara Kerja Langkah demi Langkah
```
  [ Citra monokular ] -> [ Segmentasi kontur apel ]
          -> [ Pencocokan kontur (transformasi afin) ]
          -> [ SfM sepotong demi sepotong ]
          -> [ Skala oleh pengguna (opsional) ]
          -> [ Hitung apel dan estimasi diameter ]
```

### 1. Akuisisi data dan asumsi
Kamera diasumsikan telah terkalibrasi secara intrinsik dan berfokus tetap (kamera dengan fokus otomatis yang mengubah panjang fokus sebenarnya tidak kompatibel). Kalibrasi memakai *calibration toolbox* dan pola papan catur. Citra berasal dari tablet dan kamera monokular pada beberapa uji lapangan; data stereo dipakai sebagai acuan diameter. Tidak ada asumsi tentang pencahayaan. Jumlah pohon dilaporkan hanya untuk Dataset2 (enam pohon). Lokasi, kultivar, dan perangkat tepat tidak dilaporkan pada teks selain bahwa Dataset1 berisi apel merah dan Dataset2 campuran merah dan hijau.

### 2. Praproses dan pencocokan padat
Citra disegmentasi untuk memperoleh kontur yang memuat gugusan apel. Gugusan apel pada citra berurutan dicocokkan dengan menghitung transformasi afin yang menyelaraskan dua kontur. Pada karya terdahulu, penulis memakai pencarian menyeluruh; di sini diganti dengan optimisasi nonlinear berbasis penurunan gradien Gauss-Newton (algoritma komposisional invers). Langkah galat citra diubah agar menghukum berat warp yang memetakan titik keluar dari templat. Setiap kontur memiliki transformasi afinnya sendiri, dan hierarki afin menghubungkan kontur yang sama dari bingkai I1 ke I3 melalui komposisi transformasi pasangan.

### 3. Pemilihan bingkai kunci dan rekonstruksi berpasangan
Pasangan bingkai dipilih agar memenuhi kendala epipolar dan memiliki paralaks cukup. Matriks esensial dan homografi dihitung lalu diperiksa dengan *Geometric Robust Information Criterion* (GRIC). Matriks esensial ditolak bila determinannya tidak mendekati nol (ambang $<10^{-10}$) atau dua nilai singularnya tidak identik (rasio $\le 0{,}9$). Dekomposisi memberi empat kombinasi R dan t; triangulasi diperiksa dengan kondisi *cheirality* (99% titik di depan kamera) dan galat reproyeksi rerata rendah (ambang 1,00 piksel). Titik dengan sudut triangulasi di antara lima dan enam puluh derajat dipertahankan.

### 4. Penyelarasan awan titik per gugusan
Rekonstruksi berpasangan berada pada kerangka acuan berbeda dan hanya berbeda oleh transformasi kemiripan. Transformasi dihitung antara gugusan apel yang cocok pada dua kerangka, dan faktor skala $\lambda_j$ diselesaikan dari korespondensi dalam gugusan. Rata-rata skala lokal memberikan skala yang konsisten pada seluruh awan titik dan dipakai untuk gugusan tanpa pasangan. Penyetelan berkas (*bundle adjustment*) dapat dilewati karena penyelarasan sepotong demi sepotong cukup kokoh, tetapi tetap dijalankan sebagai langkah akhir untuk menghilangkan penyimpangan kecil gerak kamera.

### 5. Hitung dan estimasi diameter
Untuk menghitung apel, dipakai metode dari laporan teknis penulis terdahulu (rujukan [13]) yang menerima citra apel tersegmentasi yang sudah terdaftar. Karena apel telah terdaftar di ruang 3D, citra terdaftar 2D dibangkitkan dengan memproyeksikan awan titik gugusan ke bingkai kamera tempat gugusan tampak. Diameter hanya diestimasi untuk apel tunggal: diameter piksel diproyeksikan ke kedalaman rerata piksel apel. Skala metrik diperoleh dari satu apel acuan yang diukur pengguna.

## Eksperimen dan Hasil
Evaluasi saluran SfM memakai lebih dari 200 bingkai dari Dataset2. Hanya bingkai kunci yang dipilih saluran yang ditampilkan. Pembanding adalah dua metode dasar: SfM inkremental dan SfM berbasis PnP, keduanya dengan penyetelan berkas penuh setelah tiap bingkai baru. Hasilnya dilaporkan secara visual (Gambar 4, 7, dan 8) tanpa angka galat dalam teks: galat reproyeksi metode penulis, bahkan tanpa penyetelan berkas, dinyatakan jauh lebih rendah daripada kedua metode dasar.

| Evaluasi | Data | Hasil |
|---|---|---|
| Akurasi hitung apel | Dataset1 (apel merah, 965 citra) | 85,87% |
| Akurasi hitung apel | Dataset2 (merah dan hijau, 464 citra) | 81,3492% |
| Selisih diameter monokular terhadap stereo | 100 apel tunggal | rerata +0,90 cm, simpangan baku ±2,9 cm |
| Jarak *earth mover* antara dua distribusi diameter | monokular dan stereo | 0,65 |

Penulis menyatakan bahwa dengan empat atau lebih apel acuan untuk menaksir skala, galat diameter turun di bawah satu sentimeter (Gambar 9). Definisi tepat akurasi hitung (rumus, serta apakah dihitung terhadap hitung manual atau acuan lain) tidak dijelaskan pada makalah ini; pembaca diarahkan ke laporan teknis terdahulu.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: hanya memerlukan satu kamera murah, tidak bergantung pada waktu hari atau posisi matahari, dan mengatasi pendaftaran ganda apel yang sama pada metode SfM dasar. Penulis juga menyatakan metodenya yang pertama memperoleh informasi diameter buah dari kamera monokular.

Keterbatasan yang dinyatakan penulis: kamera harus terkalibrasi dan berfokus tetap; pemrosesan dijalankan luring setelah pengambilan data; skala memerlukan pengukuran satu apel (estimasi dari satu apel rentan terhadap derau); implementasi waktu nyata dan kamera tak terkalibrasi merupakan pekerjaan lanjutan; hasil disebut sebagai hasil awal.

Menurut pembacaan ringkasan ini, evaluasi hitung hanya menyajikan dua angka akurasi tanpa rincian acuan, jumlah apel sebenarnya, atau galat per pohon, sehingga tidak dapat diverifikasi dari makalah ini. Asumsi apel sebagai lingkaran pada bidang datar dengan muka depan saja membatasi kasus yang diwakilinya. Perbandingan dengan metode dasar tidak disertai angka dalam teks.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali pada bingkai berurutan. Mekanismenya adalah registrasi 3D: kontur apel dicocokkan dengan transformasi afin per gugusan, rekonstruksi SfM sepotong demi sepotong menyelaraskan gugusan, dan apel dihitung setelah terdaftar pada ruang 3D yang sama, sehingga satu apel tidak terhitung berulang. Apel yang sama terdaftar berkali-kali pada metode SfM dasar, dan inilah masalah identitas lintas bingkai yang ditangani. Pencacahan berasal dari satu rangkaian bingkai pada satu sisi kebun; lintas sisi pohon tidak dibahas.

Hitungan tidak dilaporkan per kelas (tidak ada atribut kematangan atau kelas lain; dua kumpulan data dibedakan hanya menurut warna apel). Acuan hitung tidak dijelaskan pada makalah ini; hanya diameter yang diacukan ke data stereo. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah gagasan menyelaraskan objek per gugusan (bukan seluruh bingkai) dengan korespondensi dari kontur objek, serta penggunaan skala lokal yang dirata-ratakan. Perlu dicatat bahwa pendekatan ini mengandalkan segmentasi kontur dan asumsi muka depan yang mendekati bidang, yang belum diuji pada tandan sawit.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `roy2016surveying`.

Roy dan Isler mengusulkan saluran *structure from motion* baru yang memakai kontur apel untuk menghasilkan pencocokan padat dari citra satu kamera monokular, sehingga apel yang sama terdaftar satu kali dan dapat dihitung serta diukur diameternya. Pada dua kumpulan data lapangan, akurasi hitung dilaporkan 85,87% (apel merah) dan 81,3492% (apel merah dan hijau), dan perbedaan rerata diameter terhadap stereo adalah +0,90 cm dengan simpangan baku ±2,9 cm pada seratus apel.

Catatan verifikasi data: Jumlah citra (965 dan 464), akurasi hitung (85,87% dan 81,3492%), serta statistik diameter (+0,90 cm, ±2,9 cm, jarak *earth mover* 0,65, seratus apel) tertulis pada Seksi VIII, bagian A dan B. Ambang algoritmik tertulis pada Seksi VI-A. Teks ekstraksi baik, tetapi gambar dan grafik (Gambar 4 sampai 9) tidak terbaca sehingga galat reproyeksi numerik tidak dapat diverifikasi. Definisi akurasi hitung, jumlah apel acuan, lokasi, dan kultivar tidak dilaporkan. Teks mencantumkan penanda *preprint* konferensi (diajukan ke konferensi otomasi, Maret 2016).
