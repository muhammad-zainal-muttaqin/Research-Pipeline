# NTrack: A Multiple-Object Tracker and Dataset for Infield Cotton Boll Counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `muzaddid2024ntrack` |
| Judul asli | NTrack: A Multiple-Object Tracker and Dataset for Infield Cotton Boll Counting |
| Penulis | Muzaddid, Md Ahmed Al; Beksi, William J. |
| Tahun | 2024 |
| Venue | IEEE Transactions on Automation Science and Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | cotton |

## Tautan Akses
- PDF: [muzaddid2024ntrack.pdf](../pdf/muzaddid2024ntrack.pdf)
- DOI resmi: https://doi.org/10.1109/tase.2023.3342791

## Gambaran Umum

Makalah ini mengusulkan NTrack, kerangka pelacakan multi-objek (*multiple object tracking*, MOT) untuk menghitung buah kapas (*cotton boll*, *Gossypium hirsutum* L.) langsung dari video lapangan. NTrack bersifat modular dan tidak bergantung pada detektor: kotak deteksi tiap bingkai dihasilkan lebih dahulu oleh detektor apa pun, lalu pelacak mengaitkan deteksi dengan lintasan. Kebaruan utamanya adalah penaksir lokasi relatif (*Relative Location Analyzer*, RLA), yang menaksir posisi lintasan yang tidak terdeteksi (tertutup) dari posisi lintasan tetangganya, sehingga identitas buah tetap terjaga tanpa mengandalkan kemiripan tampilan. Pergerakan lintasan diprediksi dengan aliran optik rapat (*dense optical flow*) dan penyaring partikel (*particle filter*).

Penulis juga merilis TexCot22, kumpulan data video buah kapas di lapangan yang diklaim sebagai yang pertama beranotasi untuk pelacakan. Data terdiri atas 30 urutan video, 17 untuk pelatihan dan 13 untuk pengujian, dengan sekitar 150.000 instans berlabel.

Pada 13 urutan uji, NTrack mencapai galat hitung rerata 4% terhadap hitungan manual, sedangkan pembanding pada protokol yang sama menghasilkan 8% (TrackFormer), 15% (ByteTrack), 55% (DeepSORT), dan 163% (Tracktor). Pada metrik pelacakan, NTrack mencapai IDF1 92,49% dan HOTA 73,56%.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penghitungan buah kapas di lapangan penting untuk prediksi hasil serat dan fenotipe tanaman. Cara baku yang disebut penulis adalah pencuplikan manual di lapangan, yang memakan tenaga dan biaya, dan hasilnya diekstrapolasi dari sedikit tanaman sehingga rawan bias. Metode berbasis citra tunggal sebelumnya memerlukan pencuplikan citra agar tidak saling tumpang tindih, misalnya pemilihan 25 citra yang berbeda pada setiap urutan video oleh salah satu pembanding.

Buah kapas sulit dilacak karena sering bergerombol, terbelah oleh cabang atau daun menjadi beberapa wilayah terpisah, berbentuk kompleks dengan ukuran beragam, serta bergerak tidak teratur akibat angin dan gerak kamera. Penulis menyatakan bahwa pelacak berbasis tampilan (*appearance-based re-identification*) gagal karena warna dan bentuk antarbuah kapas homogen dan tampilan satu buah berubah drastis akibat pergeseran sudut pandang setelah tertutup beberapa bingkai. Penulis menyatakan pula bahwa belum ada kumpulan data video beranotasi untuk kapas.

## Ide Utama

Posisi buah kapas yang berdekatan saling berkorelasi: jarak relatif antara dua buah bertetangga berubah secara linier terhadap posisinya pada bidang citra akibat pergeseran perspektif. Dari sini penulis menurunkan bahwa lokasi suatu lintasan yang sedang tidak terdeteksi (dorman) dapat ditaksir dari lokasi lintasan tetangga yang masih aktif. Taksiran ini dipakai sebagai pengamatan tidak langsung (*indirect observation*) untuk memperbarui penyaring partikel, sehingga lintasan yang tertutup lama dapat dikenali kembali dengan identitas yang sama tanpa membandingkan tampilan visual.

Prediksi gerak memakai model kecepatan aliran dinamis, bukan model kecepatan atau percepatan konstan, karena gerak kamera dan objek tidak teratur.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data (TexCot22)

Video diambil dari baris tanaman pada petak penelitian kapas di wilayah High Plains, Texas, dengan varietas berbeda antarbaris (satu kultivar per baris) dan perlakuan irigasi yang kontras. Setiap urutan berdurasi 10 sampai 20 detik, direkam pada resolusi 4K dengan laju bingkai berbeda (misalnya 10, 15, 30) dan pada waktu hari yang berbeda untuk memvariasikan pencahayaan. Terdapat 30 urutan (17 latih, 13 uji), kira-kira $30 \times 300$ bingkai dengan 150.000 instans berlabel, rata-rata 70 buah unik per urutan, dan 2 sampai 10 buah per gerombol. Rerata lebar dan tinggi kotak anotasi sekitar $230 \times 210$ piksel. Struktur berkas mengikuti format MOT17. Aturan anotasi (Tabel I): hanya buah terbuka pada tanaman, buah yang jatuh ke tanah dikecualikan; buah tetap diberi anotasi selama sebagian terlihat dan dapat dibedakan; identitas yang sama diberikan setelah tertutup lama selama masih dapat diidentifikasi. Jumlah jenis kultivar dan jumlah bidang atau baris tidak dilaporkan.

### 2. Detektor

Seluruh pelacak dibandingkan dengan kotak deteksi yang sama dari Cascade R-CNN berpunggung ResNet-50, dilatih 100 epoch pada data latih TexCot22 dengan GPU NVIDIA GeForce GTX 1080 Ti. Akurasi deteksi pada data uji dilaporkan 97%; definisi akurasi itu tidak dirinci dalam teks.

### 3. Prediksi lokasi

Untuk tiap bingkai, aliran optik rapat dihitung dengan algoritma Gunnar-Farneback (implementasi OpenCV) terhadap bingkai sebelumnya. Kecepatan aliran kotak diperoleh dari rerata kecepatan piksel pada jendela $3 \times 3$ di pusat kotak. Partikel penyaring partikel digerakkan sesuai kecepatan aliran itu untuk memprediksi pusat kotak. Ukuran dan lebar kotak berubah perlahan sehingga dilacak dengan penyaring Kalman berkecepatan konstan.

### 4. Asosiasi dan pembaruan

Modul asosiasi mencocokkan kotak prediksi dengan deteksi memakai prosedur asosiasi ByteTrack. Lintasan yang cocok menjadi aktif dan bobot partikelnya diperbarui dari deteksi langsung. Lintasan yang tidak cocok menjadi dorman dan diperbarui oleh RLA. Deteksi yang tidak cocok dan melampaui ambang keyakinan menjadi lintasan baru. Modul *Refiner* menghapus lintasan yang dorman selama 100 bingkai terakhir atau keluar dari batas bingkai.

### 5. Lokasi relatif (RLA)

Misalkan jarak relatif lintasan $\tau_i$ terhadap tetangga $\tau_j$ adalah $d = c_1 \rho_{\tau_j} + c_0$. Maka lokasi taksiran $\rho_{\tau_i,\tau_j} = (c_1 + 1)\rho_{\tau_j} + c_0$, dengan $c_0, c_1$ diperoleh dengan kuadrat terkecil dari $m$ bingkai sebelumnya tempat kedua lintasan aktif bersamaan. Taksiran dimodelkan sebagai variabel Gauss, dan taksiran dari $k$ tetangga digabung sebagai hasil kali densitas Gauss dengan bobot kebalikan varians. Tetangga dipilih dengan *k-nearest neighbors* pada jarak Euclid pusat kotak, dengan prioritas pada tetangga yang aktif bersamaan pada lebih banyak bingkai terakhir. Komponen x dan y dihitung terpisah. Jumlah tetangga yang dipakai ditetapkan secara empiris sebanyak tiga; satu tetangga memberi taksiran bising, sedangkan terlalu banyak tetangga memberi taksiran kasar.

## Eksperimen dan Hasil

Pengujian memakai 13 urutan uji TexCot22. Metrik pelacakan: IDP, IDR, IDF1, HOTA, MOTA, MOTP, IDsw (pergantian identitas), dan Frag (fragmentasi). Untuk menghindari ketidakkonsistenan anotasi di tepi bingkai, margin 200 piksel pada kedua sisi bingkai dikecualikan. Pembanding adalah DeepSORT, Tracktor, ByteTrack, dan TrackFormer. Metrik hitungan adalah MAPE dan RMSE terhadap jumlah buah unik yang dihitung manual per urutan video.

Tabel 1. Metrik pelacakan (Tabel II makalah).

| Metode | IDP | IDR | IDF1 | HOTA | MOTA | MOTP | IDsw | Frag |
|---|---|---|---|---|---|---|---|---|
| DeepSORT | 82,50% | 81,97% | 82,24% | 66,47% | 84,80% | 80,07% | 1751 | 633 |
| Tracktor | 82,47% | 81,01% | 81,74% | 66,28% | 86,56% | 79,03% | 2070 | 787 |
| ByteTrack | 90,88% | 88,76% | 89,80% | 71,19% | 88,60% | 80,32% | 1193 | 564 |
| TrackFormer | 89,94% | 70,40% | 78,98% | 54,90% | 69,58% | 70,86% | 652 | 311 |
| NTrack | 93,28% | 91,70% | 92,49% | 73,56% | 89,25% | 81,49% | 1062 | 508 |

TrackFormer memiliki IDsw dan Frag lebih rendah daripada NTrack, tetapi galat hitungnya dua kali lipat (8% terhadap 4%), sebagaimana dinyatakan penulis.

Tabel 2. Galat hitung rerata pada 13 urutan uji, protokol sama (Tabel IV makalah).

| Metode | Galat rerata (%) |
|---|---|
| NTrack | 4 |
| TrackFormer | 8 |
| ByteTrack | 15 |
| DeepSORT | 55 |
| Tracktor | 163 |

Tabel IV makalah juga memuat hitungan per urutan. Sebagai contoh, urutan vid09_01 memiliki acuan 66 buah dan NTrack menghitung 66 (galat 0%), sedangkan vid09_02 memiliki acuan 72 dan NTrack menghitung 80 (galat 11%). Uji-t berpasangan satu sisi terhadap pembanding menghasilkan nilai p 0,003945 (ByteTrack), 0,001769 (DeepSORT), 0,000027 (Tracktor), dan 0,033470 (TrackFormer); penulis menyimpulkan galat hitung NTrack lebih rendah pada $\alpha = 0{,}05$. Urutan kolom Tabel V pada teks ekstraksi tidak sepenuhnya jelas (lihat catatan verifikasi).

Tabel 3. Perbandingan dengan metode penghitungan kapas lain (Tabel III makalah; angka pembanding diambil dari makalah masing-masing, data dan kode tidak tersedia).

| Metode | MAPE | RMSE |
|---|---|---|
| Pembelajaran mendalam | 9,00% | 9,00 (kasus terbaik) |
| Berbasis fitur geometris | 15,04% | 7,40 |
| Berbasis awan titik 3D | 10,00% | 16,87 |
| NTrack | 4,00% | 4,73 |

Studi ablasi (Tabel VI) terhadap garis dasar ByteTrack (penyaring Kalman, gerak linier): IDF1 90,3, MOTA 88,9, IDsw 3682. Model gerak dinamis saja menghasilkan IDF1 92,2, MOTA 89,3, IDsw 264. Gerak dinamis ditambah RLA dengan 1, 3, dan 5 tetangga masing-masing menghasilkan IDF1 92,5, 92,8, dan 92,8; MOTA 89,5, 89,5, dan 89,4; IDsw 101, 85, dan 85. Evaluasi kualitatif (Gambar 7 dan 8) menunjukkan NTrack mempertahankan identitas buah yang tertutup lama, sedangkan DeepSORT dan ByteTrack memberi ID baru dan Tracktor serta TrackFormer tidak mendeteksinya. Pada Gambar 9, skor kemiripan kosinus tampilan buah yang sama sebelum dan sesudah tertutup bernilai 0,011 sampai 0,021, yang dipakai penulis untuk menunjukkan bahwa kemiripan visual tidak andal.

## Kelebihan dan Keterbatasan

Kelebihan yang dinyatakan penulis: pelacak tidak bergantung pada detektor tertentu; identitas dipertahankan pada oklusi panjang tanpa fitur tampilan; hitungan langsung dari video tanpa pencuplikan citra; serta kumpulan data dan kode dirilis ke publik dalam format MOT17. Menurut pembacaan ringkasan ini, ablasi memberi bukti tegas bahwa kenaikan IDF1 dari RLA kecil (0,6 poin persentase, sebagaimana diakui penulis), sedangkan penurunan IDsw dari 264 menjadi 85 lebih besar.

Keterbatasan yang dinyatakan penulis: kinerja pelacak terikat pada akurasi detektor; sistem mengandaikan perangkat perekam beresolusi tinggi dan pengambilan data pada pencahayaan ideal. Penulis berencana memperluas kerangka ke data pelacakan multi-pandang pada pekerjaan mendatang.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan tambahan. Pengujian hanya memakai 13 urutan pendek (10 sampai 20 detik) dari satu lokasi penelitian, tanpa bukti generalisasi ke lokasi lain. Perbandingan dengan metode kapas lain memakai angka dari makalah asal pada data yang berbeda, sehingga tidak sebanding secara langsung. Hitungan acuan adalah hitungan manual buah unik pada urutan video, bukan hitungan lapangan atau panen. Penaksir RLA bergantung pada tetangga yang aktif dan pada asumsi hubungan linier lokal, yang tidak diuji pada pohon berstruktur tiga dimensi kompleks.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali dalam satu urutan video dari satu pandang bergerak. Mekanismenya adalah pelacakan berbasis deteksi (*tracking-by-detection*) dengan asosiasi ByteTrack, prediksi gerak aliran optik dengan penyaring partikel, dan pemulihan identitas lewat taksiran lokasi relatif terhadap tetangga. Hitungan adalah jumlah ID unik per urutan; pelaporan per kelas tidak dilakukan karena objek hanya satu kelas (buah kapas terbuka). Acuan hitungan adalah hitungan manual buah unik pada video (anotasi dengan ID), bukan panen. Makalah tidak membahas pencocokan lintas sisi tanaman atau lintas lintasan kamera yang terpisah, dan penulis menyebut multi-pandang hanya sebagai pekerjaan mendatang.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan bahwa kemiripan tampilan tidak andal bagi objek yang homogen dan tampilannya berubah menurut sudut pandang, sehingga hubungan geometris dengan objek tetangga dapat menjadi isyarat identitas. Batasannya, RLA mengandaikan urutan kontinu dengan aliran optik dan perubahan perspektif gradual; hal itu tidak berlaku bagi gambar diam dari sisi pohon yang berjauhan, dan tandan sawit tidak berderet dalam gerombol serapat buah kapas.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `muzaddid2024ntrack`.

Muzaddid dan Beksi mengusulkan NTrack, pelacak multi-objek yang tidak bergantung pada detektor, untuk menghitung buah kapas dari video lapangan dengan memadukan aliran optik rapat, penyaring partikel, dan taksiran lokasi relatif terhadap lintasan tetangga untuk memulihkan identitas buah yang tertutup. Pada 13 urutan uji kumpulan data TexCot22 yang dirilis bersama makalah (30 urutan, sekitar 150.000 instans), galat hitung rerata NTrack 4% dibandingkan 8% pada TrackFormer, 15% pada ByteTrack, 55% pada DeepSORT, dan 163% pada Tracktor, dengan IDF1 92,49% dan HOTA 73,56%.

Catatan verifikasi data: Metrik pelacakan bersumber dari Tabel II, galat hitung dari Tabel III dan IV, ablasi dari Tabel VI, dan uraian data dari Bagian IV. Teks ekstraksi PDF terbaca utuh, tetapi tabel hasil terpecah menjadi satu nilai per baris. Tabel IV (hitungan per urutan) dibaca dengan urutan kolom GT, NTrack, DeepSORT, Tracktor, ByteTrack, TrackFormer, dan baris galat rerata (4, 55, 163, 15, 8) dicocokkan dengan teks yang menyatakan 4% dan 8% untuk NTrack dan TrackFormer. Judul kolom Tabel V tidak memuat kolom NTrack dan urutan p-value diasumsikan sama dengan urutan judul kolom (ByteTrack, DeepSORT, Tracktor, TrackFormer). Definisi "akurasi deteksi 97%", jumlah kultivar, serta jumlah citra atau bingkai pelatihan detektor tidak dilaporkan. Hitungan acuan 150.000 instans dan "sekitar $30 \times 300$" bingkai ditulis penulis secara pendekatan.
