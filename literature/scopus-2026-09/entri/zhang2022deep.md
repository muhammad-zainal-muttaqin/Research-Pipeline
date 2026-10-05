# Deep-learning-based in-field citrus fruit detection and tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2022deep` |
| Judul asli | Deep-learning-based in-field citrus fruit detection and tracking |
| Penulis | Zhang, Wenli; Wang, Jiaqi; Liu, Yuxin; Chen, Kaizhen; Li, Huibin; Duan, Yulin; Wu, Wenbin; Shi, Yun; Guo, Wei |
| Tahun | 2022 |
| Venue | Horticulture Research |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [zhang2022deep.pdf](../pdf/zhang2022deep.pdf)
- DOI resmi: https://doi.org/10.1093/hr/uhac003

## Gambaran Umum
Makalah ini mengusulkan algoritma pencacahan buah jeruk dari urutan video di kebun, yang terdiri atas dua submetode: OrangeYolo untuk deteksi buah dan OrangeSort untuk pelacakan. OrangeYolo adalah modifikasi YOLOv3 (*backbone* Darknet53) dengan tiga cabang deteksi yang dipilih menurut kesesuaian skala medan reseptif dengan ukuran buah, modul fusi multiskala berperhatian ganda (*dual-attention*, kanal dan spasial), serta augmentasi *mosaic*. OrangeSort adalah modifikasi algoritma SORT dengan estimasi perpindahan gerak untuk pelacak yang kehilangan target, dan strategi penghitungan pada wilayah tengah bingkai.

Data berasal dari dua kebun jeruk di Kota Meishan, Provinsi Sichuan, Tiongkok. Video direkam dengan kamera aksi DJI Osmo Action yang dipasang pada kendaraan lapangan (*field rover*) yang bergerak pada 2 m/s sepanjang baris pohon, tegak lurus terhadap baris. Pada set data deteksi, OrangeYolo mencapai AP 0,938 pada set uji (F1 0,897) dan AP 0,957 pada 182 citra standar (F1 0,916), dibandingkan 0,905, 0,911, dan 0,917 untuk YOLOv3, YOLOv4, dan YOLOv5 pada set uji. Pada enam urutan video dari 22 pohon, OrangeSort dengan strategi wilayah hitung (OrangeSort*) memperoleh galat absolut rerata (MAE) 0,081 terhadap hitungan manual pada video, dibandingkan 0,45 (Sort) dan 1,212 (DeepSort) menurut abstrak.

Acuan evaluasi pencacahan adalah hitungan manual pada video, bukan hitungan panen atau hitungan lapangan di pohon. Hanya satu kelas buah (jeruk) yang dicacah.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa pencacahan buah berbasis visi komputer memiliki dua keterbatasan: akurasi deteksi yang tidak konsisten dan penghitungan ganda buah yang sama. Pada deteksi, buah di kebun berukuran kecil dan beragam skala, sedangkan teknik yang ada cenderung mengabaikan buah kecil dan buah yang tumpang tindih berat; penulis mengutip temuan bahwa tomat kecil memperoleh skor rendah dan apel kecil sulit dideteksi.

Pada pelacakan, penghitungan dari citra statis dan dari video telah dicoba. Penulis menyatakan bahwa pencacahan berbasis video lebih akurat daripada berbasis citra statis dan lebih murah daripada metode 3D (yang memerlukan peralatan mahal dan sistem kompleks, misalnya GNSS, IMU, dan LiDAR). Namun SORT dan DeepSORT, yang memadukan filter Kalman dan algoritma Hungarian, dinyatakan kurang baik untuk pencacahan buah karena buah tumbuh padat dan saling menutupi. Pada tahap tertentu pelacak yang kehilangan target karena oklusi membuat pengenal (ID) baru ketika buah terlihat kembali, sehingga terjadi penghitungan ganda. Selain itu, keadaan oklusi buah berubah menurut sudut pandang kamera, sehingga oklusi kompleks pada seluruh urutan video menyebabkan target hilang.

## Ide Utama
Gagasan pertama adalah mencocokkan skala medan reseptif lapisan jaringan dengan skala buah. Analisis k-means pada kotak anotasi memberi enam klaster ukuran (11 × 12, 14 × 16, 18 × 19, 24 × 16, 30 × 17, 50 × 31 piksel), dan sebagian besar buah termasuk objek kecil menurut definisi COCO (kurang dari 32 × 32) atau kurang dari sepersepuluh ukuran citra. Cabang deteksi ditempatkan pada lapisan konvolusi yang medan reseptifnya sesuai dengan ukuran tersebut.

Gagasan kedua adalah memanfaatkan sifat buah yang diam: pada video dari kendaraan yang bergerak seragam, lintasan tiap buah kira-kira sama dengan jarak perpindahan kamera. Bila pelacak gagal mencocokkan suatu target, posisinya dalam bingkai berjalan diperkirakan dari perpindahan rata-rata target yang terlacak dengan benar. Gagasan ketiga adalah membatasi penghitungan pada wilayah tengah bingkai, karena buah paling jarang tertutup pada posisi itu sehingga penghitungan ganda akibat oklusi pada tepi bingkai dapat dikurangi.

## Cara Kerja Langkah demi Langkah

```
 video (2 m/s, tegak lurus baris) -> OrangeYolo per bingkai (3 cabang + fusi)
     -> NMS -> OrangeSort: Hungarian + Kalman + estimasi perpindahan gerak
     -> hitung ID unik pada wilayah tengah (3/5 lebar bingkai)
```

### 1. Akuisisi data
Kamera DJI Osmo Action (60 fps, 1920 × 1080, sensor 1/2,3 inci CMOS, bidang pandang 145 derajat, F2,8) dipasang pada kendaraan lapangan buatan sendiri (120 × 90 × 70 cm, penggerak motor dengan antarmuka ROS) yang melaju seragam 2 m/s sepanjang baris pohon dengan arah pandang tegak lurus baris. Bidang pandang vertikal mencakup puncak tajuk hingga pangkal batang. Dua kebun di Kota Meishan dijadikan lokasi. Kultivar jeruk tidak disebutkan secara spesifik pada teks ("oranges"). Dari video dibuat 1.465 sampel citra hasil pemotongan acak dengan skala dan sudut berbeda untuk melatih dan menguji deteksi; 182 citra di antaranya merupakan set standar yang direkam dengan jarak dan sudut tetap.

### 2. OrangeYolo
*Backbone* Darknet53 digunakan. Tiga cabang deteksi dipasang pada lapisan konvolusi ke-18, ke-26, dan ke-43 dengan keluaran 104 × 104, 52 × 52, dan 26 × 26 untuk objek kecil, sedang, dan besar. Analisis medan reseptif menurut persamaan $R_k = 1 + \sum_j (F_j - 1)\prod_{i<j} S_i$ memberi medan 29 × 29 pada keluaran Conv9 (cocok untuk buah 11 × 12, 14 × 16, 18 × 19), 165 × 165 pada Conv26 (cocok untuk 24 × 16, 30 × 17, 50 × 31), dan Conv43 dipertahankan dengan jangkar bawaan YOLOv3 untuk objek besar. Fitur Conv53 dinilai tidak cocok untuk deteksi langsung sehingga digabung dengan jaringan dangkal.

Modul fusi berperhatian ganda: fitur dangkal $X_1$ dan fitur dalam $X_2$ (di-*upsample* 2×) masing-masing diberi perhatian kanal (pengumpulan global, dua konvolusi 1 × 1, sigmoid), lalu digabung dan dikenai perhatian spasial (rerata dan maksimum pengumpulan, konvolusi 7 × 7, sigmoid). Augmentasi *mosaic* digunakan. Pelatihan memakai GPU GTX 1080 Ti dan CPU Intel i7 generasi ke-8, SGD dengan momentum 0,9, *weight decay* 0,0005, dan laju belajar awal 0,01. Pembagian latih dan uji 7:3 secara acak atas 1.465 sampel.

### 3. OrangeSort
Pada tiap bingkai, hasil deteksi dicocokkan dengan jalur dari bingkai sebelumnya memakai algoritma Hungarian, menghasilkan tiga kategori: deteksi tak cocok (ID baru), deteksi cocok (perpindahan rata-rata dihitung dan pelacak Kalman diperbarui), dan jalur tak cocok. Untuk jalur tak cocok, titik pusat diperkirakan dengan $(x', y') = (x + \bar{\Delta x},\, y + \bar{\Delta y})$ menurut perpindahan rata-rata target yang cocok, dan lebar serta tinggi dikalikan faktor peluruhan skala $\alpha$ (nilai $\alpha$ dan ambang skala tidak dilaporkan pada teks yang tersedia). Bila skala meluruh melampaui ambang, jalur dianggap tertutup penuh dan dihapus.

### 4. Strategi wilayah hitung
Posisi buah dibagi menjadi posisi awal, tengah, dan keluar. Tujuh keadaan oklusi (A sampai G, Tabel 1) dianalisis. Keadaan A sampai D (tengah tidak tertutup) mendominasi; pada keadaan E sampai G, buah tertutup di tengah tetapi tidak tertutup di posisi awal atau keluar. Wilayah hitung ditetapkan selebar 3/5 lebar urutan video, dengan 1/5 setelah posisi awal dan 1/5 sebelum posisi keluar sebagai wilayah tidak sah.

## Eksperimen dan Hasil
Deteksi dievaluasi dengan presisi, *recall*, F1, AP, dan FPS. Pencacahan dievaluasi dengan galat absolut rerata relatif $\mathrm{MAE} = \frac{1}{m}\sum_i \frac{|y_i - \hat{y}_i|}{\hat{y}_i}$ terhadap hitungan manual pada enam urutan video dari 22 pohon, dibandingkan dengan Sort dan DeepSort.

**Deteksi (Tabel 2).**

| Model | Presisi | *Recall* | F1 | AP | FPS | Jumlah acuan |
|---|---|---|---|---|---|---|
| YOLOv3 | 0,88 | 0,86 | 0,873 | 0,905 | 83,3 | 19.466 |
| YOLOv4 | 0,862 | 0,877 | 0,854 | 0,911 | 71,4 | 19.466 |
| YOLOv5 | 0,892 | 0,874 | 0,883 | 0,917 | 58,9 | 19.466 |
| OrangeYolo | 0,902 | 0,893 | 0,897 | 0,938 | 83,3 | 19.466 |
| OrangeYolo (182 citra standar) | 0,913 | 0,919 | 0,916 | 0,957 | 83,3 | 4.441 |

Ablasi (Tabel 3): garis dasar F1 0,873 dan AP 0,905; dengan pencocokan medan reseptif F1 0,887 dan AP 0,928; ditambah *mosaic* 0,89 dan 0,93; ditambah perhatian kanal 0,892 dan 0,933; dengan perhatian ganda 0,897 dan 0,938.

**Pencacahan (Tabel 4; hitungan manual per urutan 1 sampai 6 adalah 165, 64, 70, 183, 92, dan 248).** Nilai hitungan manual dibaca dari Tabel 4 dan diperiksa terhadap galat yang dilaporkan, karena sel hitungan manual tergabung dan bergeser pada hasil ekstraksi. Galat dihitung per urutan sebagai MAE satu urutan.

| Urutan | Sort | DeepSort | OrangeSort | OrangeSort* |
|---|---|---|---|---|
| 1 | 0,6788 | 0,5273 | 0,1455 | 0,0061 |
| 2 | 0,125 | 0,6406 | 0,0938 | 0,1094 |
| 3 | 0,6143 | 2,0286 | 0,3714 | 0,2429 |
| 4 | 0,4754 | 1,8142 | 0,1265 | 0,071 |
| 5 | 0,2717 | 0,8913 | 0,1522 | 0,0326 |
| 6 | 0,5363 | 1,371 | 0,3185 | 0,0242 |

Simpangan baku galat (Tabel 5): Sort 0,4741, DeepSort 1,3975, OrangeSort 0,2555, OrangeSort* 0,08. Rerata galat enam urutan OrangeSort* adalah 0,081 (nilai ini sesuai dengan rerata sederhana enam galat di tabel, yang dihitung dalam ringkasan ini sebagai pemeriksaan: 0,4862 dibagi 6). Penulis mencatat bahwa urutan 1 (pencahayaan standar) memiliki galat terkecil, urutan 2 sampai 4 kurang cahaya (urutan 3 terburuk karena buah dan daun hampir tak terbedakan), dan urutan 5 sampai 6 terpapar cahaya berlebih dengan guncangan kamera. Pada urutan 2, OrangeSort menghitung 70 buah (40 benar, 5 hitungan ganda, 25 hitungan salah), sedangkan OrangeSort* menghitung 57 (40 benar, 4 hitungan ganda, 13 hitungan salah).

## Kelebihan dan Keterbatasan
Kelebihan yang tampak: pencacahan dibandingkan langsung dengan dua pelacak baku pada video yang sama dengan rincian hitungan benar, salah, dan ganda; strategi wilayah hitung mengurangi hitungan ganda tanpa komponen 3D; kecepatan deteksi 83,3 FPS; dan set data dipublikasikan di GitHub.

Keterbatasan yang dinyatakan penulis atau tersirat dari teks: hanya buah yang tampak dari sisi kamera yang dihitung, dan penulis menyebut pekerjaan lanjutan perlu menghubungkan hitungan dengan jumlah buah sebenarnya dengan memperhitungkan bagian pohon yang tidak tampak; belokan di ujung baris belum ditangani; lokalisasi 3D dan model ringan untuk perangkat tepi dijadikan arah lanjutan; kondisi cahaya buruk dan berlebih meningkatkan galat.

Menurut pembacaan ringkasan ini, terdapat keterbatasan tambahan. Acuan hanya hitungan manual pada video (bukan panen atau hitungan lapangan), sehingga buah yang tidak tampak tidak termasuk dan galat terhadap jumlah buah di pohon tidak diketahui. Evaluasi pencacahan hanya pada enam urutan dan 22 pohon. Strategi wilayah hitung mengubah cakupan hitungan: OrangeSort* menghitung lebih sedikit buah (misalnya 166 terhadap 189 pada urutan 1) sehingga perbandingan dengan Sort dan DeepSort yang menghitung seluruh bingkai tidak sepenuhnya sebanding dalam hal wilayah acuan; teks tidak menjelaskan apakah hitungan manual juga dibatasi pada wilayah tengah. Strategi tersebut bergantung pada gerak translasi seragam dan arah kamera tegak lurus, sehingga tidak berlaku pada gerak tidak teratur seperti rekaman genggam. Kultivar, kondisi kematangan, dan jumlah total buah pada set data tidak dilaporkan, dan faktor $\alpha$ tidak diberi nilai pada teks. Tidak ada pengulangan atau ukuran ketidakpastian selain simpangan baku antarurutan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang tampak lebih dari satu kali pada video yang direkam dari kendaraan yang bergerak. Mekanismenya adalah pelacakan multi-objek berbasis SORT dengan asosiasi Hungarian dan filter Kalman, ditambah estimasi posisi dari perpindahan rata-rata target terlacak untuk jalur yang hilang, serta pembatasan penghitungan pada wilayah tengah bingkai. Identitas dipertahankan dalam satu video dari satu pass kamera; tidak ada pencocokan antarsisi pohon atau antar-video. Hitungan tidak dilaporkan per kelas karena hanya satu kelas (jeruk). Acuan hitungnya adalah hitungan manual pada video, bukan panen atau hitungan lapangan.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: gagasan bahwa objek diam dan kamera bergerak sehingga perpindahan rata-rata antarbingkai dapat memprediksi posisi target yang hilang; gagasan membatasi penghitungan pada zona bingkai yang kurang tertutup untuk mengurangi hitungan ganda; dan pengamatan bahwa oklusi berubah menurut sudut pandang. Pemindahan itu terbatas pada pengambilan video translasi seragam; pada pengambilan multi-sisi pohon dengan sudut berbeda, asumsi tersebut tidak berlaku.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zhang2022deep`.

Zhang dkk. (2022) mengusulkan algoritma pencacahan jeruk berbasis video yang terdiri atas OrangeYolo (modifikasi YOLOv3 dengan pencocokan medan reseptif dan fusi multiskala berperhatian ganda) dan OrangeSort (modifikasi SORT dengan estimasi perpindahan gerak dan strategi wilayah hitung tengah bingkai). OrangeYolo mencapai AP 0,938 pada set uji deteksi dan 0,957 pada 182 citra standar. Pada enam urutan video dari 22 pohon di dua kebun di Sichuan, OrangeSort dengan strategi wilayah hitung memiliki MAE 0,081 terhadap hitungan manual pada video, dibandingkan MAE 0,45 (Sort) dan 1,212 (DeepSort) menurut abstrak.

Catatan verifikasi data: Angka deteksi berasal dari Tabel 2 dan Tabel 3; angka pencacahan per urutan dari Tabel 4 dan simpangan baku dari Tabel 5. Ekstraksi Tabel 4 menggeser sel hitungan manual yang tergabung, sehingga hitungan manual (165, 64, 70, 183, 92, 248) disimpulkan dari posisi sel dan diperiksa dengan galat yang dilaporkan; semua galat cocok dengan hitungan manual tersebut kecuali OrangeSort pada urutan 4: galat yang dilaporkan 0,1265, sedangkan hitungan 211 terhadap manual 183 memberi selisih relatif sekitar 0,153 (dihitung); penyebab ketidakcocokan ini tidak dapat diverifikasi dari teks. Simpangan baku OrangeSort* tertulis 0,08 pada abstrak dan Tabel 5 tetapi 0,8 pada teks Bagian "Comparative analysis"; nilai 0,08 dipakai. Angka abstrak MAE Sort 0,45 dan DeepSort 1,212 sesuai dengan rerata sederhana enam galat pada Tabel 4 (dihitung: 0,4503 dan 1,2122). Gambar tidak dapat diperiksa dari teks. Tidak dapat diverifikasi: kultivar jeruk, nilai faktor peluruhan skala $\alpha$, dan apakah hitungan manual dibatasi pada wilayah tengah bingkai.
