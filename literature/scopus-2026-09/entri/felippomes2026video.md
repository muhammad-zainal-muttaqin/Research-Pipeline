# Video-based fruit detection and tracking: effects of scanning conditions on fruit load estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `felippomes2026video` |
| Judul asli | Video-based fruit detection and tracking: effects of scanning conditions on fruit load estimation |
| Penulis | Felip-Pom\'es, Marc; Gen\'e-Mola, Jordi; Arn\'o, Jaume; Lordan, Jaume; Ruiz-Hidalgo, Javier; Morros, Josep-Ramon; Arasanz-Malo, Miguel; Net-Barn\'es, Francesc; Gregorio, Eduard |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [felippomes2026video.pdf](../pdf/felippomes2026video.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.112330

## Gambaran Umum
Makalah ini mengusulkan dan mengevaluasi sistem penglihatan komputer untuk estimasi beban buah (*fruit load*) apel berbasis pelacakan multi-objek pada video (*multi-object tracking*, MOT). Sistem mencakup deteksi buah, pelacakan, penentuan lokasi buah di dalam kebun, dan pembuatan peta beban buah per segmen baris. Fokus utama makalah adalah analisis pengaruh kondisi pemindaian, yaitu jenis sensor, jarak pemindaian, tanggal akuisisi, dan sisi baris yang dipindai, terhadap akurasi hitungan.

Eksperimen dilakukan di kebun apel eksperimental (kultivar Story Inoredcov, sistem *fruiting wall*) di Mollerussa, Catalonia, Spanyol, dengan empat baris berisi total 420 pohon yang dibagi menjadi 84 segmen sepanjang 5 m. Data direkam dengan dua kamera RGB-D (Azure Kinect DK dan ZED 2) pada tiga jarak (125 cm, 175 cm, 225 cm) dan dua tanggal (6 September 2021, empat minggu sebelum panen; 28 September 2021, satu minggu sebelum panen). Acuan hitungan berasal dari panen per segmen yang dihitung dengan mesin sortir apel komersial.

Hasil terbaik dicapai oleh ZED 2 pada jarak 225 cm pada 28 September 2021 dengan *mean absolute percentage error* (MAPE) 6,91 % dan koefisien determinasi $R^2$ 0,733. Azure Kinect lebih stabil antartanggal ($R^2$ sekitar 0,68; MAPE 7,48 % sampai 7,67 % pada 225 cm). Pemindaian dari kedua sisi baris menurunkan RMSE secara signifikan (p = 0,024), tetapi tidak mengubah MAE, MAPE, dan $R^2$ secara signifikan. Makalah menyatakan bahwa pemindaian timur dan barat diproses terpisah tanpa pencocokan identitas lintas pandang.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penghitungan buah otomatis dan estimasi hasil diperlukan untuk perencanaan panen, tenaga kerja, dan penyimpanan. Kesulitan utama adalah oklusi oleh daun, ranting, atau buah lain, yang menyebabkan buah terdeteksi sebagian, terlewat, atau muncul secara terputus-putus sehingga hitungan cenderung terlalu rendah. Pengambilan data dari beberapa sudut pandang dapat membuka buah yang tertutup dari satu sisi, tetapi berisiko menghitung ganda buah yang sama dari perspektif yang tumpang tindih.

Metode berbasis 3D (fotogrametri dan lokalisasi 3D) yang dirujuk penulis dapat menghilangkan hitungan ganda, tetapi memerlukan fotogrametri dan kalibrasi kamera yang rumit serta kompleksitas komputasi yang tinggi, sehingga sulit diterapkan pada kebun komersial besar. Alternatifnya adalah pipeline berbasis video yang mendeteksi buah pada setiap bingkai dan memakai algoritma pelacakan untuk memberi identitas unik antarbingkai. Penulis mencatat bahwa banyak studi MOT buah hanya dinilai dengan metrik pelacakan seperti MOTA atau HOTA, sedangkan selisih antara hitungan dan data panen sebenarnya jarang dikaji.

Hipotesis yang diajukan: jarak pemindaian yang lebih dekat memperbaiki deteksi tetapi dapat menurunkan akurasi hitungan keseluruhan karena cakupan pohon pada bidang pandang terbatas. Karena itu diperlukan keseimbangan antara pemindaian dekat (deteksi lebih baik) dan jauh (cakupan pohon lebih luas).

## Ide Utama
Gagasan utama adalah memakai hasil pelacakan video (jumlah ID unik per segmen) sebagai pengamatan parsial beban buah, lalu mengoreksinya dengan model regresi linear terhadap hitungan panen sebenarnya. Penulis menyatakan bahwa hitungan mentah adalah proksi beban buah, bukan hitungan eksak, dan regresi berperan sebagai koreksi bias sistematis akibat oklusi, buah yang terlihat dari kedua sisi baris, dan galat pelacakan (jejak terputus atau pertukaran identitas).

Penulis menekankan bahwa kontribusi makalah bukan inovasi algoritmik, melainkan evaluasi sistematis pipeline penghitungan berbasis MOT yang divalidasi terhadap acuan tingkat panen pada berbagai kondisi akuisisi yang realistis. Makalah ini memperluas karya sebelumnya penulis yang membandingkan SORT, DeepSORT, dan ByteTrack, dengan menambahkan algoritma penghitungan dari keluaran pelacakan serta analisis kondisi pemindaian.

## Cara Kerja Langkah demi Langkah

```
 Video RGB-D (2 sensor x 3 jarak x 2 tanggal x sisi timur/barat)
        |
        v
 Deteksi apel per bingkai (YOLOv5x)
        |
        v
 Pelacakan (ByteTrack): ID unik per apel antarbingkai
        |
        v
 Penetapan segmen 5 m (tanda pembatas + suara mayoritas)
        |
        v
 Hitungan mentah per segmen --> regresi linear --> hitungan terkoreksi
        |
        v
 Peta beban buah tingkat blok kebun
```

### 1. Akuisisi data
Kebun berisi empat baris sepanjang 105 m dengan total 420 pohon, ditanam dengan jarak 3,6 m x 1 m dan tinggi kanopi maksimum 3,5 m. Baris dibagi menjadi 21 segmen berukuran 5 m (total 84 segmen). Acuan hitungan diperoleh dari panen 5 Oktober 2021 per segmen dengan mesin sortir Maf Roda Agrobotic. Segmen 4, 5, dan 6 pada baris 2 serta segmen 5 pada baris 4 tidak memiliki acuan.

Peralatan terdiri atas kamera stereo ZED 2 dan kamera *time-of-flight* Azure Kinect DK, keduanya pada ketinggian 162 cm, ditambah GNSS Ardusimple simpleRTK2B pada ketinggian 207 cm, dipasang pada tiang di kendaraan listrik segala medan. Resolusi RGB kedua kamera 1920 x 1080; bidang pandang RGB ZED 2 110 x 70 derajat dan Azure Kinect 90 x 59 derajat. Kendaraan bergerak dengan kecepatan konstan 2 km/jam. Setiap baris dipindai dua kali, dari sisi timur dan barat, pada tiga jarak sensor ke sumbu baris, yaitu 1,25 m, 1,75 m, dan 2,25 m. Pada tanggal pertama apel berwarna dua-nada merah muda dan hijau; pada tanggal kedua apel sudah merah penuh.

### 2. Detektor
YOLOv5x diinisialisasi dari bobot COCO lalu disetel halus (*fine-tuning*) dengan SGD (laju belajar 0,01, *weight decay* 0,0001, ukuran *batch* 4) pada 1.723 bingkai beranotasi dari segmen 4, 5, dan 6 baris 2, dibagi menjadi 1.295 latih, 203 validasi, dan 225 uji. Data mencakup semua kondisi sensor, jarak, dan tanggal. Identitas apel diberikan secara manual pada kotak pembatas melalui platform Supervisely. Pelatihan berlangsung 273 epoch pada dua GPU RTX 2080 Ti. Segmen 4, 5, dan 6 baris 2 dikeluarkan dari percobaan penghitungan untuk mencegah kebocoran data.

### 3. Pelacakan
Tiga pelacak berpola *tracking-by-detection* dibandingkan: SORT (filter Kalman dan algoritma Hungarian), DeepSORT (menambah fitur penampilan dari jaringan Re-ID), dan ByteTrack (menambah tahap asosiasi kedua untuk deteksi berkeyakinan rendah). Evaluasi dilakukan pada sembilan urutan video berisi 1.723 bingkai dari segmen 5 dan 6 baris 2.

### 4. Penetapan segmen
Untuk validasi, pita merah-putih dipasang pada tiap pergantian segmen dan bingkai pergantian dianotasi manual. Algoritma 1 memperkirakan posisi tanda pembatas pada seluruh bingkai tempat tanda terlihat dengan memakai rerata perpindahan piksel apel antarbingkai. Algoritma 2 menetapkan tiap apel yang terlacak ke segmen tempat apel itu paling sering muncul relatif terhadap tanda (suara mayoritas). Penulis menyatakan bahwa tanda fisik dan anotasi manual hanya untuk validasi dan tidak diperlukan pada penerapan operasional.

### 5. Koreksi regresi dan validasi silang
Hitungan ID unik per segmen diregresikan terhadap hitungan panen. Deteksi dari pemindaian timur dan barat diproses terpisah, tanpa fusi tingkat objek atau pencocokan lintas pandang; buah yang terlihat dari kedua sisi dapat terhitung dua kali pada pengamatan antara dan dikompensasi secara statistik oleh regresi. Evaluasi memakai validasi silang *leave-one-row-out*. Penulis menyatakan bahwa koefisien regresi spesifik terhadap kebun dan konfigurasi akuisisi, sehingga kalibrasi ulang diperlukan untuk kebun atau kondisi lain, misalnya dengan menghitung manual buah pada sejumlah segmen atau pohon acuan saat panen.

### 6. Metrik
Deteksi dinilai dengan *precision*, *recall*, F1, dan mAP; pelacakan dengan MOTA, IDF1, dan HOTA; penghitungan dengan MAE, MAPE, RMSE, dan $R^2$ pada tingkat segmen. Pengaruh tanggal dan sisi pemindaian diuji dengan ANOVA.

## Eksperimen dan Hasil
### Deteksi dan pelacakan
YOLOv5x mencapai F1 0,834 dan mAP@0,5 0,871. Perbandingan pelacak pada data validasi segmen 5 dan 6 baris 2 ditunjukkan pada tabel berikut (Tabel 3 makalah).

| Pelacak | MOTA | IDF1 | HOTA | Waktu (ms/citra) |
|---|---|---|---|---|
| SORT | 0,6401 | 0,8091 | 0,6804 | 15,3 |
| DeepSORT | 0,5735 | 0,7646 | 0,6824 | 128,0 |
| ByteTrack | 0,6817 | 0,8369 | 0,6894 | 15,4 |

Pada bagian diskusi, penulis melaporkan bahwa YOLO26 yang disetel halus pada data yang sama sedikit lebih rendah dari YOLOv5 (F1 0,819 berbanding 0,834; mAP@0,5 0,865 berbanding 0,871). BoT-SORT memberi perbaikan sekitar 4 % pada MOTA, 3 % pada IDF1, dan 6 % pada HOTA dibandingkan ByteTrack, dengan waktu pemrosesan sekitar lima kali lebih lama; StrongSORT tidak melampaui ByteTrack. ByteTrack dipertahankan karena dinilai memberi keseimbangan akurasi dan efisiensi terbaik. Angka rinci BoT-SORT dan StrongSORT tidak ditampilkan dalam tabel pada teks yang tersedia.

### Akurasi penghitungan menurut sensor, tanggal, dan jarak
Hitungan mentah berkorelasi positif dengan hitungan panen (Azure Kinect $R^2$ = 0,702; ZED 2 $R^2$ = 0,744) sebelum koreksi regresi. Seluruh hasil berikutnya memakai prediksi terkoreksi regresi (Tabel 4 makalah).

| Sensor | Tanggal | Jarak (cm) | MAE (apel) | MAPE (%) | RMSE (apel) |
|---|---|---|---|---|---|
| Azure Kinect | 06/09/2021 | 225 | 35,28 | 7,67 | 46,64 |
| Azure Kinect | 06/09/2021 | 175 | 38,33 | 8,24 | 52,37 |
| Azure Kinect | 06/09/2021 | 125 | 47,37 | 10,10 | 62,80 |
| Azure Kinect | 28/09/2021 | 225 | 35,07 | 7,48 | 46,98 |
| Azure Kinect | 28/09/2021 | 175 | 36,97 | 7,69 | 50,40 |
| Azure Kinect | 28/09/2021 | 125 | 46,68 | 10,00 | 61,90 |
| ZED 2 | 06/09/2021 | 225 | 42,98 | 9,44 | 57,86 |
| ZED 2 | 06/09/2021 | 175 | 46,51 | 10,00 | 61,85 |
| ZED 2 | 06/09/2021 | 125 | 52,76 | 11,82 | 70,21 |
| ZED 2 | 28/09/2021 | 225 | 31,71 | 6,91 | 43,04 |
| ZED 2 | 28/09/2021 | 175 | 36,76 | 7,71 | 50,10 |
| ZED 2 | 28/09/2021 | 125 | 43,42 | 9,29 | 55,46 |

Pada kedua sensor, galat terendah diperoleh pada jarak 225 cm. Penulis menduga galat lebih besar pada jarak dekat disebabkan bidang pandang yang sempit, yang membatasi cakupan bagian atas dan bawah pohon sehingga ada buah yang tidak terdeteksi dan jumlah potongan jejak (*tracklet*) bertambah. Nilai $R^2$ pada 225 cm: Azure Kinect 0,686 (06/09) dan 0,682 (28/09); ZED 2 0,519 (06/09) dan 0,733 (28/09). Penulis mengaitkan peningkatan ZED 2 menjelang panen dengan perubahan warna apel dari hijau ke merah yang menambah kontras terhadap kanopi. Perbaikan MAPE ZED 2 dari 9,44 % ke 6,91 % adalah selisih 2,53 poin persentase (sesuai pernyataan makalah "2,53 %"). Garis regresi antartanggal untuk kedua sensor dinyatakan tidak berbeda signifikan.

Pada peta beban buah, rerata hitungan panen mendekati 450 apel per segmen (konsentrasi pada kisaran 400 sampai 500). Prediksi mengikuti pola spasial acuan, tetapi daerah berkepadatan tertinggi kurang terwakili, terutama pada ZED 2, sehingga puncak lokal cenderung diperhalus.

### Pemindaian satu sisi dan dua sisi (Azure Kinect, 225 cm)
ANOVA terhadap faktor tanggal dan sisi (timur, barat, kedua sisi) tidak menemukan efek signifikan pada MAE, MAPE, dan $R^2$ (semua p > 0,05; untuk sisi: MAE p = 0,062, MAPE p = 0,082, $R^2$ p = 0,797). Pada RMSE, faktor sisi signifikan (p = 0,024; di bagian lain ditulis 0,0249). RMSE terkoreksi (*least squares mean*) untuk pemindaian dua sisi adalah 46,73 apel, dibandingkan 59,36 apel (hanya barat) dan 58,69 apel (hanya timur).

## Kelebihan dan Keterbatasan
Kelebihan: validasi dilakukan terhadap hitungan panen sebenarnya per segmen, bukan terhadap anotasi citra, sehingga lebih mewakili sudut pandang pengguna akhir. Rancangan eksperimen memvariasikan sensor, jarak, tanggal, dan sisi pemindaian. Kode dan dataset dinyatakan tersedia publik pada repositori GitHub yang disebut makalah. Pipeline tidak memerlukan rekonstruksi 3D.

Keterbatasan yang dinyatakan penulis: (1) seluruh eksperimen berlangsung di satu kebun dengan arsitektur pohon, kepadatan tanam, dan manajemen yang relatif homogen, dan variasi antarbaris kemungkinan lebih kecil daripada variasi antarkebun; (2) koefisien regresi spesifik terhadap kebun dan konfigurasi akuisisi sehingga perlu kalibrasi ulang; (3) tanda fisik dan anotasi bingkai manual diperlukan untuk validasi tingkat segmen dan tidak ditujukan bagi penerapan komersial; (4) tidak ada pencocokan identitas atau penghapusan duplikat lintas pandang antara pemindaian timur dan barat; (5) kontribusi terpisah dari oklusi, observasi ganda, dan galat pelacakan tidak dapat dipisahkan karena dikompensasi bersama oleh regresi; (6) jarak optimum dipengaruhi arsitektur kanopi *fruiting wall*; (7) tidak ada pengulangan lapangan yang sepenuhnya independen.

Menurut pembacaan ringkasan ini, hasil 6,91 % dan $R^2$ 0,733 diperoleh dari model yang dikalibrasi terhadap panen pada kebun yang sama (validasi silang antarbaris), sehingga kinerja pada kebun baru tanpa kalibrasi tidak terbukti. Menurut pembacaan ringkasan ini, pemilihan konfigurasi terbaik (ZED 2, 225 cm, 28/09) dan sensor yang dianalisis lebih lanjut dilakukan berdasarkan hasil pada data yang sama, dan teks tidak melaporkan uji signifikansi untuk perbedaan antarsensor selain pernyataan bahwa kedua model tidak berbeda secara statistik pada 225 cm satu minggu sebelum panen. Menurut pembacaan ringkasan ini, kesimpulan tentang manfaat pemindaian dua sisi bertumpu pada satu metrik (RMSE) dan tidak menunjukkan peningkatan pada MAE, MAPE, dan $R^2$.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali melalui dua mekanisme yang berbeda. Dalam satu pass pemindaian, identitas buah antarbingkai dijaga oleh pelacakan MOT (ByteTrack, tracking-by-detection berbasis filter Kalman dan asosiasi Hungarian), dan penghitungan memakai jumlah ID unik per segmen. Untuk dua sisi baris (timur dan barat), makalah secara eksplisit tidak melakukan pencocokan lintas pandang: duplikat dari kedua sisi tidak dihapus di tingkat instans, melainkan dikompensasi secara statistik oleh regresi linear terhadap hitungan panen. Penulis menyatakan peningkatan dari pemindaian dua sisi dikaitkan dengan visibilitas kanopi yang saling melengkapi, bukan dengan peningkatan akurasi tingkat instans, dan mereka menyebut fusi multi-pandang berbasis lokalisasi 3D atau pencocokan lintas pandang sebagai pekerjaan lanjutan.

Hitungan dilaporkan untuk satu kelas buah (N = 1), tanpa pemisahan per kelas kematangan; tanggal pertama dan kedua dibedakan menurut warna buah, bukan menurut kelas. Acuan hitungan adalah hitungan panen per segmen 5 m dengan mesin sortir, bukan anotasi citra; penulis menegaskan bahwa hasil ini tidak dapat dibandingkan langsung dengan studi yang diukur terhadap anotasi citra. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah rancangan validasi terhadap hitungan panen, penggunaan regresi sebagai koreksi bias untuk duplikat lintas sisi dan oklusi, serta bukti bahwa pemindaian dua sisi tanpa pencocokan identitas memperkecil galat besar tetapi tidak menyelesaikan masalah identitas lintas pandang. Makalah ini tidak membahas sawit atau hitungan per kelas.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `felippomes2026video`.

Ringkasan yang aman dikutip: Felip-Pomés dkk. (2026) mengembangkan sistem estimasi beban buah apel berbasis deteksi YOLOv5x dan pelacakan ByteTrack pada video RGB-D (Azure Kinect DK dan ZED 2) dari kebun eksperimental berisi 420 pohon, dengan koreksi regresi linear terhadap hitungan panen per segmen 5 m dan validasi silang *leave-one-row-out*. Jarak pemindaian 225 cm memberi galat terendah pada kedua sensor, dengan MAPE terbaik 6,91 % dan $R^2$ 0,733 (ZED 2, satu minggu sebelum panen). Pemindaian dari kedua sisi baris menurunkan RMSE secara signifikan, tetapi pemindaian timur dan barat diproses tanpa pencocokan identitas lintas pandang sehingga duplikat dikompensasi secara statistik oleh regresi.

Catatan verifikasi data: Angka deteksi (F1 0,834; mAP@0,5 0,871) dan perbandingan pelacak terdapat pada seksi 3.1 dan Tabel 3. Angka MAE, MAPE, dan RMSE per sensor, tanggal, dan jarak terdapat pada Tabel 4; nilai $R^2$ pada seksi 3.2 (teks). Hasil ANOVA berada pada Tabel 5 (seksi 3.3) dan RMSE terkoreksi 46,73, 59,36, dan 58,69 apel pada akhir seksi 3.3. Angka YOLO26 (F1 0,819; mAP@0,5 0,865) dan peningkatan BoT-SORT (sekitar 4 %, 3 %, 6 %) berasal dari seksi 4.1; tabel rinci pembandingan tersebut tidak tersedia dalam teks. Nilai p untuk sisi pada RMSE tertulis 0,024 pada Tabel 5 dan seksi 3.3, serta 0,0249 pada satu kalimat di seksi 3.3. Nilai $R^2$ penggunaan regresi terkoreksi untuk semua konfigurasi tidak tercantum dalam teks ekstraksi karena berada pada Gambar 8; tabel ANOVA untuk MAPE ditampilkan dengan skala pecahan, dan teks ekstraksi tabel tersebut sempat terpotong pada bagian awal. Jumlah total bingkai atau jam video untuk penghitungan seluruh kebun, serta jumlah apel total, tidak dilaporkan dalam teks; kedalaman angka rerata panen hanya dinyatakan "mendekati 450". Selisih 2,53 % pada MAPE ZED 2 adalah selisih poin persentase (9,44 dikurangi 6,91) yang cocok dengan pernyataan makalah. Teks makalah berbahasa Inggris dan tidak rusak secara berarti.
