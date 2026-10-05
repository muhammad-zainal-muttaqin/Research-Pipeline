# Row-based kiwifruit counting pipeline for smartphone-captured videos using fruit tracking and detection region adaptation guided by support-post

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2025row` |
| Judul asli | Row-based kiwifruit counting pipeline for smartphone-captured videos using fruit tracking and detection region adaptation guided by support-post |
| Penulis | Zhang, Jiwei; Jiang, Liguo; He, Leilei; Wu, Zhenchao; Li, Rui; Chen, Jinyong; Sun, Xiaoxu; Xue, Yunfei; Grecheneva, Anastasia; Fountas, Spyros; Fu, Longsheng |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | kiwifruit |

## Tautan Akses
- PDF: [zhang2025row.pdf](../pdf/zhang2025row.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2025.110476

## Gambaran Umum
Makalah ini mengusulkan alur kerja (*pipeline*) pencacahan buah kiwi per baris kebun dari video yang direkam dengan telepon pintar. Alur kerja terdiri atas tiga komponen: deteksi buah kiwi dan tiang penyangga (*support-post*) dengan model YOLO, pencacahan berbasis video dengan pelacakan buah yang diikuti metode verifikasi dua wadah (*two-containers verification*, TCV), dan adaptasi wilayah deteksi (*detection region adaptation*) yang memakai tiang penyangga untuk mengeluarkan buah dari baris tetangga. Video direkam dari sudut pandang menengadah yang menempuh seluruh panjang satu baris.

Data berupa 1.353 citra beranotasi dan 11 urutan video uji untuk pencacahan, dari kebun kiwi dengan tinggi tandan sekitar 1,7 m dan jarak antarbaris 3,0 m. Detektor YOLOv5m dan YOLOv8m mencapai AP0,5:0,95 buah kiwi masing-masing 0,864 dan 0,878. Akurasi hitungan dengan TCV naik dari 40,12% menjadi 94,20% pada ByteTrack dan dari 37,59% menjadi 96,65% pada DeepSORT. Koefisien determinasi (R²) hitungan per baris terhadap acuan bernilai 0,9791.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil kiwi memerlukan hitungan buah yang akurat dan tepat waktu. Penulis menyatakan bahwa metode pencacahan kiwi sebelumnya umumnya berfokus pada bagian kecil baris kebun sehingga kurang memadai untuk penerapan praktis akibat kondisi tumbuh yang tidak merata. Hitungan dari citra tunggal tidak memberi data rinci karena kepadatan buah berbeda di tiap bagian baris, sehingga pencacahan berbasis video dipandang lebih masuk akal.

Pencacahan video dengan pendekatan *tracking-by-detection* mengasosiasikan instans antarbingkai, tetapi penulis mencatat bahwa metode demikian peka terhadap kondisi lingkungan dan menghasilkan penaksiran berlebih (*over-estimation*) karena galat penetapan ID menumpuk. Deteksi positif palsu yang sporadis juga didaftarkan pelacak sebagai buah normal. Selain itu, karena baris kiwi ditanam rapat, citra dari telepon pintar sering memuat buah dari baris tetangga yang ikut terlacak dan terhitung sehingga hitungan salah atribusi baris.

## Ide Utama
Dua gagasan memisahkan masalah. Pertama, hitungan tidak diambil dari ID terakhir yang ditetapkan pelacak, melainkan dari buah yang berhasil melewati dua wadah virtual berurutan dengan lintasan stabil dan konsisten; deteksi sporadis tidak memenuhi syarat itu sehingga tersaring. Gagasan ini diadaptasi dari pencacahan kendaraan dengan garis virtual ganda. Kedua, batas baris diperkirakan dari tiang penyangga beton yang mudah dideteksi, lalu masker area minat (*region of interest*, RoI) diadaptasi secara dinamis sehingga buah di luar baris tidak terlihat oleh detektor.

## Cara Kerja Langkah demi Langkah

```
  [ Video telepon pintar ] --> [ YOLO: buah kiwi + tiang ]
                                     |            |
                                     v            v
                          [ ByteTrack / DeepSORT ] [ Batas baris + masker RoI ]
                                     |            |
                                     v            |
                            [ TCV: dua wadah ] <--+
                                     |
                                     v
                              [ Hitungan per baris ]
```

### 1. Akuisisi data
Video direkam dengan penstabil gimbal tiga sumbu AOCHUAN Smart XE dan tongkat ekstensi 73 cm. Kamera yang dipakai adalah OnePlus 7 Pro, iPhone 11, dan iPhone 14 Pro Max pada resolusi 1920 × 1080 dan 60 FPS, serta Canon EOS Kiss X3 untuk citra 2352 × 1568. Sebagian citra diekstraksi dari video di berbagai kebun. Total 1.353 citra dianotasi dan 11 urutan video dicadangkan untuk uji pencacahan. Pada citra dari jarak dekat, tiap buah menempati lebih dari 1,0% piksel; pada citra baris lebar, tiap buah menempati kurang dari 0,2% piksel. Citra dibagi acak menjadi set latih, validasi, dan uji dengan rasio 8:1:1. Anotasi memakai program pelabelan otomatis dengan verifikasi manual LabelImg. Kultivar kiwi tidak dilaporkan; jumlah kebun tidak dilaporkan.

### 2. Deteksi buah dan tiang penyangga
Beberapa model YOLO dilatih pada data yang sama dengan hiperparameter awal identik: laju belajar awal $1{,}0\times10^{-3}$, SGD, penjadwal CosineAnnealingLR, ukuran masukan 768 × 768, *batch* 4, 300 epoch, probabilitas *mosaic* 1,0. Dua percobaan dilakukan: skala model YOLOv5 (nano, small, medium, large) dan perbandingan kerangka YOLOv5m, YOLOv6m, YOLOv7, serta YOLOv8m.

### 3. Pelacakan buah
DeepSORT (menggabungkan jarak gerak dan jarak cosinus fitur) dan ByteTrack (memakai juga kotak berkeyakinan rendah untuk menjaga kontinuitas) dibandingkan pada deteksi YOLOv5m. Pencacahan dasar memakai ID terakhir yang ditetapkan pada keadaan stabil sebagai hitungan; penulis menunjukkan bahwa ID kerap berlebih dan berpindah.

### 4. Verifikasi dua wadah (TCV)
Buah dilacak ketika melewati dua wadah virtual yang ditetapkan sebelumnya. Buah masuk wadah pertama, berpindah ke wadah kedua, lalu diverifikasi dan dihitung bila lintasannya stabil dan konsisten. Kasus yang digambarkan mencakup buah stabil, buah yang tidak terlacak stabil karena positif palsu pada sebagian bingkai, buah yang semula tertutup daun, dan positif palsu sporadis yang dieliminasi. Antrean koordinat terbaru yang disimpan dibatasi panjangnya sehingga TCV tidak banyak menambah waktu.

### 5. Adaptasi wilayah deteksi per baris
Metode ini memanfaatkan umpan balik bingkai sebelumnya. Bila tiang penyangga terdeteksi, kotak buah dibagi menjadi dua kelompok menurut koordinat horizontal dan dibuat batas paralel virtual untuk RoI; sudut batas ditentukan dari rerata arah gerak relatif buah, yang dinilai lebih andal daripada orientasi tiang. Bila tiang tidak terlihat, masker RoI menyempit secara horizontal secara bertahap sambil menjaga jarak dari batas perkiraan sampai tiang muncul kembali.

### 6. Aplikasi
Sistem klien-server (Vue pada klien, Flask pada server) beroperasi dalam jaringan lokal melalui HTTP; pengguna mengunggah video dan server mengembalikan video terproses serta hitungan.

## Eksperimen dan Hasil
Metrik deteksi adalah AP dan AP0,5:0,95 serta waktu inferensi. Metrik pencacahan adalah akurasi $Acc = 1 - |\hat{y}-y|/(\hat{y}+y)$ terhadap seluruh buah terlihat pada 11 video uji, akurasi per baris $Acc_r$ terhadap acuan baris $y_r$ yang mengecualikan buah baris tetangga, dan R². Acuan hitungan adalah hitung manual buah pada video uji; hitungan lapangan atau panen tidak dilaporkan.

Tabel 3 makalah (skala YOLOv5):

| Skala | Parameter (M) | Ukuran (MB) | Waktu (ms) | Kiwi AP0,5 | Kiwi AP0,5:0,95 | Tiang AP0,5 | Tiang AP0,5:0,95 |
|---|---|---|---|---|---|---|---|
| Nano | 1,9 | 15,7 | 5,4 | 0,991 | 0,833 | 0,864 | 0,659 |
| Small | 7,2 | 58,6 | 6,2 | 0,993 | 0,828 | 0,879 | 0,633 |
| Medium | 21,2 | 170,5 | 12,3 | 0,991 | 0,864 | 0,895 | 0,727 |
| Large | 46,5 | 373,7 | 19,1 | 0,993 | 0,846 | 0,929 | 0,787 |

Tabel 4 makalah (kerangka skala menengah):

| Model | Parameter (M) | Ukuran (MB) | Waktu (ms) | Kiwi AP0,5 | Kiwi AP0,5:0,95 | Tiang AP0,5 | Tiang AP0,5:0,95 |
|---|---|---|---|---|---|---|---|
| YOLOv5m | 21,2 | 170,5 | 12,3 | 0,991 | 0,864 | 0,895 | 0,727 |
| YOLOv6m | 34,3 | 304,8 | 21,0 | 0,909 | 0,730 | 0,995 | 0,790 |
| YOLOv7 | 36,9 | 301,8 | 11,9 | 0,996 | 0,853 | 0,928 | 0,750 |
| YOLOv8m | 25,9 | 207,9 | 16,1 | 0,983 | 0,878 | 0,942 | 0,786 |

Penulis memilih YOLOv5m karena keseimbangan AP, ukuran, dan waktu inferensi. YOLOv8m lebih tinggi 1,6% pada AP0,5:0,95 kiwi dan 8,1% pada tiang, tetapi waktu inferensinya 30,9% lebih lama (angka persentase dari makalah).

Tabel 5 makalah (pencacahan pada 11 video uji):

| Pelacak | Metode | Kecepatan (FPS) | Acc |
|---|---|---|---|
| DeepSORT | ID terakhir | 5,80 | 37,59% |
| DeepSORT | ID terakhir + TCV | 5,32 | 96,65% |
| ByteTrack | ID terakhir | 23,67 | 40,12% |
| ByteTrack | ID terakhir + TCV | 22,39 | 94,20% |

ID maksimum dengan hitung ID langsung adalah 2,17 kali (DeepSORT) dan 2,39 kali (ByteTrack) acuan. TCV menaikkan akurasi sebesar 59,06% (ByteTrack) dan 54,08% (DeepSORT) menurut makalah. ByteTrack sekitar 3,14 kali lebih cepat daripada DeepSORT dan akurasi TCV berbasis ByteTrack 2,45% lebih rendah daripada DeepSORT. Penulis menyatakan R² naik 2,44% dengan TCV, tanpa angka R² mentah dalam teks untuk kondisi tanpa TCV.

Untuk hitungan per baris, $Acc_r$ melebihi 90% pada 11 video uji dan R² 0,9791 (ByteTrack dengan TCV, Gambar 12). Penulis mencatat bahwa akurasi menurun ketika acuan hitungan membesar, yang dikaitkan dengan akumulasi galat dari TCV dan adaptasi wilayah deteksi.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: pencacahan menempuh seluruh baris dengan telepon pintar berbiaya rendah; TCV menekan penaksiran berlebih secara besar tanpa menurunkan kecepatan secara berarti; batas baris dari tiang penyangga mengurangi buah baris tetangga; dan kumpulan data tersedia di repositori GitHub (menurut makalah) meskipun pernyataan ketersediaan data menyebut "tersedia atas permintaan".

Keterbatasan yang dinyatakan penulis: perubahan lingkungan mendadak dan penyesuaian parameter citra yang terlambat menyebabkan kehilangan informasi; buram gerak karena waktu pajanan panjang; ketidakseimbangan instans buah dan tiang; pergeseran pusat kotak tiang karena tertutup masker; kesulitan menghitung pada kepadatan tinggi; TCV dipengaruhi kualitas pelacakan; sebagian buah tersaring TCV karena hilang dari pandangan atau buram; kontainer TCV perlu dikonfigurasi lebih tepat; batas baris mungkin konservatif atau kasar dan bergantung pada tiang yang terlihat berkala; dan studi tidak mempertimbangkan pergeseran rute atau guncangan keras.

Menurut pembacaan ringkasan ini, terdapat keterbatasan tambahan. Evaluasi pencacahan hanya memakai 11 video sehingga estimasi variasi antarvideo terbatas dan R² dihitung dari 11 titik. Acuan baris bersifat subjektif karena batas baris tidak terlihat (diakui penulis sebagian). Tidak ada perbandingan langsung dengan metode pencacahan lain pada data yang sama. Pembandingan dengan penelitian terdahulu dinyatakan sulit oleh penulis sendiri. Hitungan tidak dibedakan per kelas karena hanya ada satu kelas buah.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai dengan pelacakan multi-objek (ByteTrack atau DeepSORT pada deteksi YOLOv5m), kemudian memadatkan hitungan melalui TCV, yaitu validasi lintasan melalui dua wadah virtual. Mekanisme TCV bukan penentuan identitas lintas pandang, melainkan penyaringan ID tak stabil dari satu aliran video yang bergerak sepanjang baris. Makalah juga membatasi hitungan pada satu baris melalui masker RoI berbasis tiang, yang merupakan kendali atas buah yang tampak dari baris tetangga.

Hitungan hanya satu kelas buah, jadi tidak dilaporkan per kelas. Acuan hitungnya adalah hitung manual buah pada video uji (seluruh buah terlihat dan buah per baris), bukan panen. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan memverifikasi lintasan sebelum menambah hitungan, sehingga ID yang tidak stabil tidak menggelembungkan hitungan, serta pembatasan area hitung dengan penanda struktural tetap untuk menolak objek di luar unit yang dihitung. Pengaturan data makalah bersifat satu lintasan kontinu, sehingga tidak langsung berlaku untuk sisi pohon yang diambil terpisah.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zhang2025row`.

Zhang dkk. (2025) mengusulkan alur kerja pencacahan kiwi per baris dari video telepon pintar yang menggabungkan deteksi YOLO, pelacakan ByteTrack atau DeepSORT, verifikasi dua wadah (TCV) untuk menekan penaksiran berlebih, dan adaptasi wilayah deteksi berbasis tiang penyangga untuk mengeluarkan buah baris tetangga. Pada 11 video uji, TCV menaikkan akurasi hitungan dari 40,12% menjadi 94,20% (ByteTrack) dan dari 37,59% menjadi 96,65% (DeepSORT), dan R² hitungan per baris terhadap acuan manual adalah 0,9791.

Catatan verifikasi data: AP0,5:0,95 YOLOv5m 0,864 dan YOLOv8m 0,878 berasal dari Tabel 4; skala model dari Tabel 3; akurasi dan kecepatan pelacakan dari Tabel 5; R² 0,9791 dan $Acc_r$ di atas 90% dari Bagian 3.3 dan Gambar 12 (nilai per video hanya ada pada gambar sehingga tidak dibaca dari teks). Rasio 2,17 dan 2,39 kali serta kenaikan R² 2,44% dari Bagian 3.2; R² mentah tanpa TCV tidak tertera dalam teks. Jumlah buah acuan per video, jumlah kebun, dan kultivar tidak dilaporkan dalam teks. Makalah berbahasa Inggris dan teksnya terbaca baik.
