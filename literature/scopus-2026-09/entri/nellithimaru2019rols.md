# ROLS : Robust object-level SLAM for grape counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `nellithimaru2019rols` |
| Judul asli | ROLS : Robust object-level SLAM for grape counting |
| Penulis | Nellithimaru, Anjana K.; Kantor, George A. |
| Tahun | 2019 |
| Venue | IEEE Computer Society Conference on Computer Vision and Pattern Recognition Workshops |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple, citrus, grape |

## Tautan Akses
- PDF: [nellithimaru2019rols.pdf](../pdf/nellithimaru2019rols.pdf)
- DOI resmi: https://doi.org/10.1109/cvprw.2019.00321

## Gambaran Umum
Makalah ini (Nellithimaru dan Kantor, Carnegie Mellon University) mengusulkan ROLS, saluran SLAM (*Simultaneous Localization and Mapping*) tingkat objek untuk menghitung buah anggur di kebun anggur dari citra stereo. Saluran ini memadukan segmentasi instans Mask R-CNN pada citra 2D dengan pemrosesan 3D klasik: awan titik berbasis disparitas, klasifikasi lingkungan lokal titik dengan *Singular Value Decomposition* (SVD), pencocokan bola pada buah anggur, dan pencocokan antarbingkai berbasis bola-bola tersebut untuk membangun peta 3D padat serta lintasan kamera.

Data diambil dari kebun anggur di Delano, California, pada Juli 2018 dengan dua kamera PointGrey 9 MP berjarak dasar 0,22 m pada kendaraan lapangan, dilengkapi peniup udara untuk menyingkap daun. Hitungan anggur hasil peta 3D diproyeksikan ulang ke citra dan dibandingkan dengan hitungan manual dari citra. Hasilnya: presisi rerata 0,9662, *recall* 0,9881, skor F1 0,977, dan korelasi R2 0,9989 pada 20 citra berurutan. Galat lokalisasi, berupa simpangan model dari garis lurus baris tanaman, adalah 20 cm (galat kuadrat rerata, sesuai teks) pada lintasan 187 m.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pengukuran manual karakteristik tanaman pada kebun anggur skala luas lambat dan tidak akurat; pada praktiknya dilakukan dengan interpolasi dari sebagian kecil sampel. Pemodelan 3D kebun dengan kamera sulit karena gerakan daun akibat angin atau peniup udara, perubahan iluminasi, tekstur yang terbatas, dan struktur berulang. Metode klasik seperti *Structure from Motion* (SfM), *Multi-View Stereo* (MVS), dan ORB-SLAM sering gagal bila dipakai sendiri pada kondisi ini.

Metode SLAM yang ada juga tidak memakai informasi semantik, dan metode tingkat objek yang ada (misalnya Fusion++, SLAM++, QuadricSLAM) dinilai penulis tidak cocok untuk adegan padat dengan kotak pembatas anggur yang saling tumpang tindih, atau memerlukan basis data model 3D objek. Jaringan 3D membutuhkan data berlabel 3D dalam jumlah besar yang tidak tersedia untuk kebun anggur.

## Ide Utama
Penulis menggunakan objek yang dipasang bentuk parametriknya, yaitu bola yang dicocokkan pada buah anggur, sebagai fitur tingkat objek untuk SLAM. Dibanding titik fitur atau ICP pada awan titik mentah, bentuk terparameterisasi (a) tahan terhadap dinamika adegan akibat peniup daun dan (b) membatasi jumlah landmark sehingga mempercepat optimisasi. Bola juga memberi solusi bentuk tertutup untuk asosiasi data.

Akurasi klasifikasi titik ditingkatkan dengan menggabungkan topeng instans 2D dengan kesan geometri lokal 3D (SVD pada tiga skala lingkungan), yang juga memisahkan daun dari cabang. Hitungan anggur diambil dari model 3D hasil SLAM, sehingga satu butir anggur yang tampak pada beberapa bingkai berurutan diwakili oleh satu bola pada peta 3D dan dihitung satu kali.

## Cara Kerja Langkah demi Langkah
```
 [ Citra stereo ] -> [ Rekonstruksi 3D (SGM) ] ----\
       |                                             v
       +-> [ Mask R-CNN (citra kiri) ] -> [ proyeksi topeng ke 3D ]
              -> [ SVD + TSVM ] -> [ pencocokan bola (MSAC) ]
              -> [ SLAM (ICP titik-ke-bidang) ] -> [ peta 3D, hitungan ]
```

### 1. Akuisisi data
Kebun anggur di Delano, California, Juli 2018. Dua kamera PointGrey 9 MP (jarak dasar 0,22 m) dipasang pada kendaraan lapangan, dengan peniup udara di bawah kamera untuk menggerakkan daun. Bingkai berurutan tumpang tindih paling sedikit 50%, dan lebih dari 85% saat peniup menyala. Citra dikumpulkan dari lebih dari 20 baris, tiap baris sepanjang 187 m dengan 70 sampai 80 tanaman dan sekitar 750 citra. Percobaan dilakukan dengan dan tanpa peniup, hasilnya dilaporkan terpisah (nilai terpisah tidak tertulis pada Bagian 4.2). Kultivar tidak dilaporkan.

### 2. Rekonstruksi 3D
Awan titik padat dihitung dengan *Semi-Global Matching* (SGM) dengan biaya kecocokan berbasis *Mutual Information* yang tidak peka terhadap perubahan iluminasi, dipilih penulis dibanding pencocokan fitur SIFT atau SURF.

### 3. Segmentasi instans
Mask R-CNN (tulang punggung ResNet 50, kepala Faster R-CNN) dengan bobot pralatih MS-COCO dilatih ulang pada anggur. Citra 9 MP dipotong menjadi petak berukuran 256 x 338 yang masing-masing memuat 0 sampai 20 buah anggur, karena jaringan bekerja baik bila objek menempati paling sedikit 5% citra. Data latih berjumlah 62 segmen citra dan data validasi 7 segmen, dengan augmentasi balik kiri-kanan dan atas-bawah (Tabel 1). Anggur dekat kamera dilabeli, anggur kecil dari baris latar diabaikan.

### 4. SVD dan klasifikasi titik
Topeng diproyeksikan ke 3D dan di tiap pusat topeng, tetangga dalam jarak d dikumpulkan lewat pohon k-d. Matriks kovarians dan SVD memberi nilai singular yang menentukan sebaran isotropik (buah anggur), linear (cabang), atau planar (daun). Vektor ciri 9 dimensi (tiga skala) dipakai melatih *Transductive Support Vector Machine* (TSVM) semi-terawasi dengan 20% data berlabel dan 80% tak berlabel: titik diklasifikasikan sebagai anggur atau bukan, lalu bukan-anggur dipisah menjadi daun atau cabang.

### 5. Pencocokan bola
Bola (pusat dan jari-jari) dicocokkan pada titik berkelas anggur dengan MSAC (varian RANSAC); rentang jari-jari dan wilayah pencarian berasal dari ROI proyeksi topeng yang telah disempurnakan SVD. Titik anggota bola dihapus setelah pencocokan agar tidak dipakai dua bola.

### 6. SLAM dan penghitungan
Masukan SLAM adalah awan titik bola hasil pencocokan. Pose kamera 6 derajat kebebasan diestimasi dengan ICP titik-ke-bidang (bidang singgung dari 50 titik tetangga), dipilih karena konvergen dalam iterasi lebih sedikit dibanding titik-ke-titik. Bingkai awan titik digabung menjadi peta padat dan lintasan kamera. Hitungan anggur diambil dari model 3D lalu diproyeksikan ulang ke tiap citra memakai pose kamera dunia untuk memperoleh hitungan per citra.

## Eksperimen dan Hasil
Hitungan hasil proyeksi ulang dibandingkan dengan hitungan anggur manual dari citra. Lokalisasi dinilai dengan mengasumsikan tanaman ditanam lurus: garis lurus dibuat dari interpolasi koordinat GPS awal dan akhir baris, dan simpangan model gabungan dari garis itu dihitung per bingkai. Pembanding SLAM: ICP titik-ke-bidang pada awan titik mentah, SfM berbasis fitur (SIFT, SURF, sudut), dan ORB-SLAM2; hasil pembanding hanya disajikan secara visual dan deskriptif (Gambar 9), bukan sebagai angka.

| Hasil (Bagian 4.2) | Nilai |
|---|---|
| Presisi rerata | 0,9662 |
| *Recall* | 0,9881 |
| Skor F1 | 0,977 |
| R2 untuk 20 citra berurutan terpilih acak | 0,9989 |
| Galat kuadrat rerata lokalisasi (lintasan 187 m) | 20 cm |

Waktu per modul (Tabel 2): tetangga terdekat 0,02 ms per ROI, SVD 0,15 ms per ROI, klasifikasi TSVM 1 ms per bingkai, pencocokan bola 0,1 ms per bola, SLAM 1 ms per bingkai; pelatihan Mask R-CNN 10 jam dan TSVM 2 menit. Ablasi menunjukkan secara kualitatif bahwa tanpa Mask R-CNN hanya sebagian anggur terpilih sebagai ROI sehingga peta buruk; tanpa SVD satu anggur dapat terisi beberapa bola atau satu bola menutupi beberapa anggur; tanpa pencocokan bola iteratif positif palsu bertahan dan anggur tertutup terlewat. ICP pada awan titik mentah menunjukkan pergeseran tanaman dari garis harapan, SfM berfitur terjebak pada sudut daun, dan ORB-SLAM2 menghasilkan peta yang terlalu jarang.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: tidak mengandaikan iluminasi konstan atau adegan statis, lokalisasi dalam sentimeter, representasi ringkas, dan seluruh saluran selain segmentasi instans tidak bergantung pada sensor dan jenis buah sehingga dapat digeneralisasi ke apel dan jeruk dengan melatih ulang segmentasi.

Keterbatasan yang dinyatakan penulis: pendekatan end-to-end berbasis jaringan 3D membutuhkan data 3D berlabel besar dan dibiarkan untuk pekerjaan mendatang; generalisasi ke buah dan sensor lain belum diuji; pembuatan peta berbasis GPS di atas citra satelit adalah arah lanjutan.

Menurut pembacaan ringkasan ini, evaluasi hitungan terhadap hitungan manual dari citra (bukan panen) dilaporkan pada dasarnya sebagai satu set angka rerata, dan R2 diperoleh dari hanya 20 citra berurutan; jumlah citra total yang dievaluasi tidak dilaporkan. Data latih sangat kecil (62 segmen). Galat lokalisasi 20 cm pada 187 m diukur terhadap garis lurus dari GPS yang diasumsikan, bukan terhadap acuan posisi sebenarnya, sementara abstrak menyebut akurasi "dalam sentimeter" dan teks menyebut kebutuhan akurasi sub-sentimeter; kedua klaim tidak serasi dengan angka 20 cm. Penghitungan memakai bola dengan anggur sebagai butiran, yang berbeda dari tandan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang tampak pada banyak citra berurutan dengan mekanisme rekonstruksi 3D dan SLAM tingkat objek: tiap anggur diwakili satu bola pada peta 3D gabungan, yang diperoleh dengan penyelarasan antarbingkai (ICP titik-ke-bidang pada bola-bola), lalu hitungan diambil dari model 3D dan diproyeksikan ulang ke citra. Identitas ditegakkan secara geometris pada ruang 3D bersama, bukan dengan pelacak tampilan. Cakupan hanya satu sisi baris kebun yang dilalui kendaraan; lintas sisi tanaman tidak dibahas.

Hitungan tidak dilaporkan per kelas (hanya satu kelas, anggur, dan kelas daun serta cabang dipakai sebagai klasifikasi titik, bukan sebagai hitungan). Acuan hitung adalah hitungan manual dari citra, bukan panen. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah gagasan menyatukan identitas lewat ruang 3D bersama dengan landmark berbentuk parametrik. Syarat yang perlu dicatat: pendekatan ini memerlukan stereo atau depth, pose kamera yang andal, dan objek yang cocok dengan bentuk parametrik sederhana; kecocokan bola untuk tandan sawit yang besar dan tidak bulat belum dibuktikan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `nellithimaru2019rols`.

Nellithimaru dan Kantor mengusulkan ROLS, saluran SLAM tingkat objek untuk menghitung anggur dari citra stereo dengan menggabungkan segmentasi instans Mask R-CNN, klasifikasi struktur tanaman berbasis SVD, pencocokan bola, dan penyelarasan antarbingkai. Terhadap hitungan manual dari citra, metode ini mencapai presisi 0,9662, *recall* 0,9881, dan skor F1 0,977 pada data kebun anggur di Delano, California, dengan galat lokalisasi 20 cm pada baris sepanjang 187 m.

Catatan verifikasi data: presisi, *recall*, F1, R2, dan galat 20 cm tertulis pada Bagian 4.2; parameter jaringan pada Tabel 1; waktu pada Tabel 2; rincian akuisisi pada Bagian 4.1. Teks ekstraksi terbaca baik, tetapi gambar dan grafik (Gambar 6 sampai 9) tidak terbaca. Pembanding SLAM tidak disertai angka. Jumlah total citra evaluasi, hasil terpisah dengan dan tanpa peniup, kultivar, dan jumlah anggur sebenarnya tidak dilaporkan. Teks menyebut label Tabel 3 pada teks tetapi tabel diberi nomor Tabel 2; ringkasan ini mengikuti nomor pada tabel.
