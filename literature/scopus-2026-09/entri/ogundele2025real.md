# Real-Time Strawberry Ripeness Classification and Counting: An Optimized YOLOv8s Framework with Class-Aware Multi-Object Tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ogundele2025real` |
| Judul asli | Real-Time Strawberry Ripeness Classification and Counting: An Optimized YOLOv8s Framework with Class-Aware Multi-Object Tracking |
| Penulis | Ogundele, Oluwasegun Moses; Tamrakar, Niraj; Kook, Jung-Hoo; Kim, Sang-Min; Choi, Jeong-In; Karki, Sijan; Akpenpuun, Timothy Denen; Kim, Hyeon Tae |
| Tahun | 2025 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [ogundele2025real.pdf](../pdf/ogundele2025real.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture15181906

## Gambaran Umum
Makalah ini mengusulkan kerangka kerja terpadu untuk klasifikasi tingkat kematangan dan pencacahan buah stroberi (*Fragaria × ananassa*) di rumah kaca dari rekaman video. Kerangka itu terdiri atas detektor YOLOv8s yang dimodifikasi dan pelacak multi-objek (*multi-object tracking*, MOT) ByteTrack yang diberi informasi kelas pada vektor keadaan. Pencacahan dilakukan dengan garis virtual pada zona minat (*region of interest*, ROI), sehingga setiap identitas lintasan (*track ID*) dihitung satu kali pada kelasnya.

Data berasal dari satu rumah kaca di Gyeongsang National University, Jinju, Korea Selatan, dengan tiga kultivar (Seolhyang, Keumsil, dan Honghee) pada tiga musim tanam. Terkumpul 2.190 citra dan 37 video, dengan 13.228 kotak anotasi pada tiga kelas kematangan. Detektor akhir mencapai mAP@0,5 sebesar 92,5%, dengan 8,0 juta parameter (27,9% lebih sedikit daripada YOLOv8s). Pada 20 video validasi, sistem pencacahan menghasilkan R² = 0,914, MAE 8,55 buah, RMSE 9,63 buah, dan MAPE 9,52% terhadap hitungan manual.

Hasil per kelas menunjukkan R² tertinggi pada buah matang (0,950) dan terendah pada buah setengah matang (0,752; MAPE 16,25%). Penulis mengaitkan kelemahan kelas tengah dengan ambiguitas visual tahap transisi dan jumlah contoh latih yang lebih sedikit.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa pendugaan hasil panen stroberi yang akurat dibutuhkan karena kekurangan tenaga kerja akibat penuaan populasi petani dan karena buah mudah rusak. Mereka berpendapat bahwa pendugaan hasil harus membedakan kematangan: buah matang menunjukkan hasil siap panen, sedangkan buah mentah dan setengah matang menunjukkan potensi hasil berikutnya. Menghitung semua buah tanpa membedakan kelas dianggap tidak memadai.

Dua kesulitan utama yang dinyatakan adalah klasifikasi kematangan di bawah oklusi, bayangan, dan pencahayaan tidak seragam, serta penanganan oklusi dalam pencacahan video. Tanaman stroberi berbuah terus-menerus, sehingga beberapa tahap kematangan hadir bersamaan; penulis menyebut hal ini tidak sesuai dengan pendekatan yang dirancang untuk tanaman dengan pematangan seragam. Pada video dengan kamera yang bergerak terus, menghitung semua deteksi sepanjang video juga dapat menimbulkan galat.

Tabel 1 makalah membandingkan empat studi stroberi terdahulu dan mencatat celah masing-masing: detektor dua tahap yang tidak sesuai untuk waktu nyata dan hanya untuk buah matang, pelacak khusus oklusi tanpa pembedaan kematangan, serta dua detektor YOLO tanpa pelacakan dan tanpa validasi terhadap hitungan manual.

## Ide Utama
Ide utama adalah menyusun alur lengkap dari deteksi sampai hitungan per kelas. Detektor diperbaiki agar ringan dan lebih peka terhadap buah kecil, lalu dihubungkan dengan ByteTrack yang vektor keadaan filter Kalman-nya diperluas dengan variabel kelas. Pencocokan antara prediksi dan deteksi dilakukan per kelas, sehingga buah matang tidak dicocokkan dengan buah mentah.

Pengubahan identitas menjadi hitungan dilakukan dengan aturan sederhana: sebuah buah dihitung ketika titik pusat kotaknya masuk ke ROI vertikal di tengah bingkai, dan hanya bila ID lintasannya belum tercatat pada himpunan ID yang telah dihitung. Dengan demikian identitas dipertahankan hanya di dalam satu video yang bergerak menyusuri baris tanaman.

## Cara Kerja Langkah demi Langkah
Alur umum: citra dan video dikumpulkan, detektor YOLOv8s dimodifikasi dan dilatih pada citra, kemudian dipasang pada ByteTrack untuk memproses video, dan hasilnya divalidasi dengan regresi terhadap hitungan manual.

### 1. Akuisisi data
Citra diambil dengan kamera Sony Cyber-shot DSC-RX100 VII (sensor CMOS 1,0 inci, sekitar 20,1 megapiksel), dan video diambil dengan Apple iPhone 13 Pro Max. Perangkat dipasang pada platform bergerak setinggi 0,8 m dengan jarak ke buah 30 sampai 80 cm. Pengambilan dilakukan pada pagi (sekitar pukul 9), siang (sekitar tengah hari), dan sore (sekitar pukul 17) dalam cahaya alami. Tanaman ditanam pada lima bedeng tinggi dari September sampai Februari selama tiga musim (2022/2023, 2023/2024, 2024/2025), dan pengambilan data dilakukan pada periode panen utama, yaitu Desember dan Februari.

Kelas kematangan ditentukan dari luas permukaan merah: Kategori I (mentah; dominan hijau atau putih), Kategori II (setengah matang; sekitar 75% permukaan atau kurang berwarna merah), dan Kategori III (matang; permukaan merah penuh).

### 2. Anotasi dan pra-pemrosesan
Seluruh 2.190 citra dianotasi manual dengan Label Studio 1.16.0, menghasilkan 13.228 instans (rata-rata sekitar 6 buah per citra): 6.133 untuk Kategori I, 1.675 untuk Kategori II, dan 5.420 untuk Kategori III. Tiga augmentasi dipakai (rotasi sudut kecil, *Gaussian blur*, dan kecerahan serta kontras acak) sehingga dataset akhir berisi 4.250 citra dalam format YOLO. Dataset dibagi 8:1:1 untuk latih, validasi, dan uji. Teks tidak menyatakan apakah pembagian dilakukan sebelum atau sesudah augmentasi; urutan penulisannya menyiratkan augmentasi lebih dahulu.

Untuk validasi pencacahan, 20 dari 37 video dipilih dengan kriteria gerakan kamera yang lebih stabil. Hitungan acuan dibuat oleh dua operator independen yang menghitung semua buah per tingkat kematangan di setiap baris setelah pengambilan data. Selisih antaroperator rata-rata sekitar 2 buah per video.

### 3. Detektor YOLOv8s yang ditingkatkan
YOLOv8s dipilih sebagai garis dasar karena dinilai seimbang antara kecepatan dan akurasi. Tiga modifikasi dilakukan:

1. Modul C2f diganti modul C3x, yang memakai bottleneck dengan konvolusi 1 × 3 dan 3 × 1. Tabel 4 mencatat 11.126.745 parameter untuk C2f dan 8.607.705 untuk C3x.
2. Ditambahkan satu kepala deteksi objek kecil yang bekerja pada peta fitur beresolusi lebih tinggi (160 × 160).
3. Fungsi kerugian CIoU diganti Wise-IoU versi 3 (WIoU v3), yang memakai derajat pencilan (*outlier degree*) untuk memberi bobot dinamis pada kotak berkualitas rendah.

Pelatihan dan pengujian memakai CPU Intel Core i7-10700, GPU NVIDIA GeForce RTX 2060 (6 GB), PyTorch 2.4.1, CUDA 12.1, dan Python 3.8.2.

### 4. ByteTrack dengan keadaan sadar-kelas
ByteTrack memakai strategi BYTE: deteksi berkeyakinan tinggi dicocokkan lebih dahulu dengan lintasan yang ada memakai prediksi filter Kalman, lalu deteksi berkeyakinan rendah dicocokkan dengan lintasan yang tersisa agar buah yang tertutup sementara dapat ditemukan kembali. Vektor keadaan diperluas menjadi $x = [u, v, s, r, \dot{u}, \dot{v}, \dot{s}, \text{class}]^T$, dengan $(u, v)$ pusat kotak, $s$ rasio aspek, dan $r$ tinggi (sesuai penulisan makalah). Pencocokan dilakukan per kelas.

### 5. Pencacahan dengan garis virtual
ROI berukuran 500 × 1080 piksel diletakkan vertikal di tengah bingkai video 1920 × 1080. Pusat kotak yang masuk ke ROI memicu pemeriksaan keunikan: bila ID belum ada pada himpunan terdaftar, ID ditambahkan dan hitungan kelasnya naik; bila sudah ada, ID diabaikan.

```
  video --> detektor YOLOv8s (C3x + kepala kecil + WIoU)
        --> ByteTrack (keadaan memuat kelas)
        --> pusat kotak masuk ROI 500x1080 ?
        --> ID baru? --ya--> hitungan kelas + 1
```

## Eksperimen dan Hasil
Detektor dibandingkan dengan YOLOv3-tiny, YOLOv5s-p6, YOLOv6s, YOLOv8n, YOLOv8s, dan YOLOv8m pada dataset stroberi yang sama. Metrik deteksi adalah presisi, *recall*, F1, dan mAP@0,5. Metrik pencacahan adalah R², RMSE, MAE, dan MAPE terhadap hitungan manual pada 20 video.

Tabel 1. Perbandingan detektor (Tabel 6 makalah; makalah menyebut YOLOv8n memperoleh 90,5).

| Algoritma | P (%) | R (%) | F1 | mAP@50 (%) |
|---|---|---|---|---|
| YOLOv3-tiny | 84,4 | 86,2 | 85,3 | 90,1 |
| YOLOv5s-p6 | 84,6 | 86,9 | 85,7 | 91,0 |
| YOLOv6s | 85,0 | 87,2 | 86,1 | 90,5 |
| YOLOv8n | 81,7 | 88,7 | 85,1 | 90,5 |
| YOLOv8s | 86,7 | 86,2 | 86,5 | 92,1 |
| YOLOv8m | 86,4 | 89,3 | 87,8 | 92,6 |
| Model usulan | 87,0 | 89,6 | 88,3 | 92,5 |

YOLOv8m unggul 0,1 poin mAP, tetapi memerlukan 25,8 juta parameter dan 78,7 GFLOPs. Model usulan memerlukan 8,0 juta parameter, 27,1 GFLOPs, ukuran model 15,7 MB, dan waktu inferensi 9,7 ms per citra (sekitar 103 FPS menurut makalah). Untuk perbandingan, YOLOv8s memerlukan 11,1 juta parameter, 28,4 GFLOPs, dan 8,9 ms.

Tabel 2. Akurasi deteksi per kelas model usulan (Tabel 7 makalah).

| Kelas | P (%) | R (%) | AP@0,5 (%) |
|---|---|---|---|
| I (mentah) | 84,2 | 90,7 | 93,0 |
| II (setengah matang) | 79,1 | 82,6 | 86,3 |
| III (matang) | 93,4 | 95,6 | 98,0 |
| Keseluruhan | 87,0 | 89,6 | 92,5 |

Studi ablasi (Tabel 8) menunjukkan mAP@50 sebesar 92,1% untuk YOLOv8s (11,1 juta parameter), 91,4% setelah C3x (8,6 juta), 92,3% setelah penambahan kepala (8,05 juta), dan 92,5% setelah WIoU (8,0 juta). AP kelas II pada keempat konfigurasi berturut-turut 86,1; 85,3; 86,6; dan 86,3.

Tabel 3. Pencacahan pada 20 video terhadap hitungan manual (Tabel 10 makalah).

| Kategori | R² | MAE | RMSE | MAPE (%) |
|---|---|---|---|---|
| III (matang) | 0,950 | 2,65 | 3,37 | 11,63 |
| II (setengah matang) | 0,752 | 2,70 | 3,16 | 16,25 |
| I (mentah) | 0,910 | 4,20 | 5,07 | 9,62 |
| Total | 0,914 | 8,55 | 9,63 | 9,52 |

Akurasi pencacahan per video berkisar dari 84,51% sampai 95,24%; video 19 mengalami penghitungan kurang (akurasi 84,5%) dan video 4 penghitungan berlebih (akurasi 89,4%). Penulis mengaitkan variasi ini dengan kepadatan kelompok buah, tingkat oklusi daun, dan perubahan pencahayaan.

Perbandingan pelacak dilakukan dengan detektor yang sama dan pelacak SORT, DeepSORT, Norfair, dan MOTPY (Gambar 17). Teks menyebut ByteTrack memberi R² tertinggi dan galat terendah. DeepSORT memperoleh R² = 0,842 dengan penghitungan berlebih akibat kesalahan pencocokan fitur tampilan. SORT, Norfair, dan MOTPY dilaporkan mengalami lintasan terfragmentasi dan penghitungan kurang akibat oklusi; angka ketiganya hanya ada pada gambar dan tidak tertulis di teks.

## Kelebihan dan Keterbatasan
Kelebihan yang tampak dari makalah: hasil dilaporkan per kelas kematangan, bukan hanya total; hitungan divalidasi terhadap hitungan manual dua operator; dan pemilihan pelacak dibandingkan dengan empat alternatif pada detektor yang sama. Detektor juga ringan sehingga cocok untuk perangkat tepi menurut penulis.

Keterbatasan yang dinyatakan penulis: data berasal dari satu rumah kaca dengan tiga kultivar sehingga generalisasi ke kultivar atau sistem lahan terbuka belum teruji; skala kematangan tiga kelas menyederhanakan proses kematangan yang kontinu dan menimbulkan ambiguitas pada kelas setengah matang; dan sistem menghitung jumlah buah, bukan bobot, sehingga pendugaan hasil dalam kilogram memerlukan estimasi ukuran buah, misalnya dengan sensor kedalaman.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan lain. Validasi pencacahan hanya memakai 20 video yang dipilih karena gerakan kamera stabil, sehingga hasilnya belum mewakili kondisi gerakan tidak teratur. Data pencacahan hanya mencakup satu lintasan video per baris tanpa pandangan dari sisi lain tanaman, sehingga buah yang tersembunyi dari lintasan itu tidak terhitung. Ketiga pelacak pembanding selain DeepSORT tidak disertai angka di teks. Pembagian latih-uji yang dilakukan setelah augmentasi dapat menimbulkan tumpang tindih antarbagian bila citra hasil augmentasi tersebar ke bagian yang berbeda, tetapi teks tidak menjelaskan urutan ini. Selain itu, ambang keyakinan dan parameter ByteTrack tidak dilaporkan pada teks yang dibaca.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai, tetapi hanya dalam satu urutan video yang bergerak sepanjang baris tanaman. Mekanismenya adalah pelacakan berbasis deteksi (ByteTrack dengan filter Kalman), pencocokan per kelas, dan aturan hitung satu kali per ID pada ROI. Tidak ada pencocokan lintas sisi, lintas pandang yang terpisah, maupun rekonstruksi 3D; identitas tidak dipertahankan antarvideo.

Hitungan dilaporkan per kelas kematangan (tiga kelas) maupun total. Acuan hitungnya adalah hitungan manual di lapangan: dua operator menghitung semua buah per tingkat kematangan di setiap baris setelah pengambilan data, bukan panen dan bukan anotasi citra. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan memasukkan kelas ke dalam keadaan pelacak sehingga pencocokan berlangsung dalam kelas yang sama, aturan registrasi ID untuk mencegah penghitungan ganda, serta penyajian galat per kelas yang memperlihatkan bahwa kelas yang ambigu secara visual menurunkan akurasi hitungan per kelas meskipun total tetap stabil. Pendekatan garis virtual bergantung pada gerakan kamera yang linear sepanjang baris dan tidak otomatis berlaku untuk pengambilan dari beberapa sisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `ogundele2025real`.

Ogundele dkk. (2025) mengusulkan kerangka pencacahan stroberi per tingkat kematangan di rumah kaca yang memadukan detektor YOLOv8s yang dimodifikasi (modul C3x, kepala deteksi objek kecil, dan fungsi kerugian WIoU; mAP@0,5 92,5%, 8,0 juta parameter) dengan ByteTrack yang keadaan Kalman-nya memuat kelas dan pencacahan garis virtual berbasis ROI. Pada 20 video, hitungan sistem dibandingkan dengan hitungan manual dua operator dan menghasilkan R² = 0,914 dan MAPE 9,52% secara total, dengan R² 0,950 untuk buah matang dan 0,752 untuk buah setengah matang.

Catatan verifikasi data: Angka detektor dibaca dari Tabel 6 (perbandingan), Tabel 7 (per kelas), Tabel 8 (ablasi), dan Tabel 9 (efisiensi); angka pencacahan dibaca dari Tabel 10 dan teks Seksi 3.5. Jumlah citra, video, instans, dan pembagian data berasal dari Seksi 2.3. Teks ekstraksi terbaca baik, tetapi tabel hasil terpisah baris demi baris dan diinterpretasikan menurut urutan kolom; tabel ablasi memuat kolom AP kelas I, II, dan III dengan baris yang kolom kelasnya cukup jelas untuk dibaca. Hasil pelacak pembanding (Gambar 17) hanya tersedia sebagai gambar dan tidak dapat diverifikasi dari teks kecuali R² DeepSORT 0,842. Ukuran sampel pencacahan (jumlah total buah pada 20 video) tidak dilaporkan. Parameter ByteTrack dan ambang keyakinan tidak dilaporkan. Data tersedia atas permintaan kepada penulis korespondensi.
