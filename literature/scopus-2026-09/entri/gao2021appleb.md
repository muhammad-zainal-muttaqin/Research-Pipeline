# Apple fruit detection and counting based on deep learning and trunk tracking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gao2021appleb` |
| Judul asli | Apple fruit detection and counting based on deep learning and trunk tracking |
| Penulis | Gao, Fangfang; Yang, Tingyi; Fu, Longsheng |
| Tahun | 2021 |
| Venue | American Society of Agricultural and Biological Engineers Annual International Meeting Asabe 2021 |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [gao2021appleb.pdf](../pdf/gao2021appleb.pdf)
- DOI resmi: https://doi.org/10.13031/aim.202100193

## Gambaran Umum
Makalah prosiding ASABE 2021 ini mengembangkan metode otomatis untuk mendeteksi dan menghitung apel dari video kebun dengan arsitektur dinding buah vertikal (*vertical fruiting-wall*). Alih-alih melacak setiap buah, penulis melacak satu batang pohon dan memakai perpindahan batang antarbingkai sebagai perpindahan acuan (*reference displacement*) untuk mencocokkan buah yang sama pada bingkai berurutan. Deteksi apel dan batang memakai YOLOv4-tiny, dan pelacak batang memakai CSR-DCF (*channel and spatial reliability discriminative correlation filter*, implementasi CSRT di OpenCV).

Data berasal dari kebun apel komersial vertikal kultivar Scifresh di Prosser, Washington, AS: 800 citra RGB (Kinect V2, 1920 × 1080) dan 10 video yang diambil pada dua musim panen (2017 dan 2018). Pada data uji deteksi, AP apel 99,59%, AP batang 99,10%, dan mAP 99,35%. Pada video, hitungan algoritma dibandingkan dengan hitungan manual: R² regresi 0,9875 dari 15 video dan rerata akurasi hitung Pc 91,30%.

Penulis menyatakan bahwa metode ini mencatat buah dari satu sisi barisan pohon; penggabungan hitungan dari kedua sisi barisan, termasuk apel yang terlihat dari kedua sisi, disebut sebagai pekerjaan mendatang. Makalah ini adalah presentasi pertemuan yang tidak melalui tinjauan sejawat formal komite editorial ASABE.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil apel diperlukan untuk menjadwalkan panen, mengalokasikan tenaga kerja, dan menaksir volume stok. Penghitungan manual memerlukan banyak tenaga, mahal, dan sering merusak, sehingga sulit dipakai pada kebun luas. Metode berbasis citra pohon tunggal memakan waktu dan sulit diterapkan di kebun apel. Video beberapa pohon yang direkam dari kereta dorong dipandang sebagai alternatif, tetapi memerlukan cara menghubungkan buah yang sama antarbingkai agar tidak terhitung berulang.

Penelitian video terdahulu melacak semua buah yang terdeteksi. Penulis menilai bahwa buah berukuran kecil, berjumlah banyak, dan serupa antarindividu sehingga sulit dilacak, dan pelacakan semua buah memakan banyak sumber daya komputasi. Penulis mengajukan pelacakan satu target sebagai alternatif hemat sumber daya.

## Ide Utama
Semua objek yang relatif diam dalam video (batang, cabang, daun, buah) mengalami lintasan perpindahan yang sama akibat gerak kamera. Batang pohon berukuran besar dan berciri jelas sehingga lebih mudah dilacak daripada apel. Pada arsitektur dinding buah, pohon ditanam rapat (jarak antartanaman 0,3 sampai 1,5 m, jarak antarbaris 2,5 sampai 4,0 m menurut makalah). Perpindahan batang antarbingkai dipakai untuk memprediksi posisi tiap apel pada bingkai berikutnya. Apel hasil prediksi dicocokkan dengan apel terdeteksi yang berjarak Euklides terdekat, dan pasangan itu diberi ID yang sama. Jumlah buah pada video adalah ID maksimum pada bingkai terakhir.

## Cara Kerja Langkah demi Langkah

```
 [Video satu sisi baris] -> [YOLOv4-tiny: apel + batang per bingkai]
      -> [CSR-DCF melacak batang -> perpindahan acuan s]
      -> [posisi apel + s ~ apel terdekat di bingkai berikut -> ID sama]
      -> [jumlah = ID maksimum pada bingkai terakhir]
```

### 1. Akuisisi data
Perangkat portabel berisi sensor Microsoft Kinect V2, penjepit kamera, dan rangka penyangga di atas kereta dorong; troli kendali jarak jauh dipakai untuk merekam video. Jarak antartanaman 1,5 m, jarak antarbaris 2,7 m, tinggi pohon sekitar 4,0 m. Diperoleh 800 citra RGB (JPEG, 1920 × 1080) dan 10 video selama dua musim panen 2017 dan 2018; kereta dijaga pada kecepatan hampir tetap, dan waktu perekaman acak sehingga jumlah pohon dan buah per video berbeda. Jumlah buah dan pohon pada tiap video dihitung manual (buah latar belakang tidak dihitung). RMSE hitungan manual oleh tiga operator pada himpunan video adalah 2,7 buah per video (rerata 43 buah per citra).

### 2. Penyusunan data dan augmentasi
Citra dibagi acak menjadi 80% data latih dan 20% data uji. Apel dan batang dianotasi sebagai dua kelas dengan kotak persegi panjang (XML). Seluruh video dipakai untuk menguji algoritma penghitungan. Augmentasi mencakup perubahan kecerahan, pemerataan histogram adaptif, kekaburan gerak, dan pencerminan horizontal, sehingga 800 citra menjadi 6.400 citra. Rotasi sengaja tidak dipakai karena tidak sesuai dengan sudut pohon sebenarnya.

### 3. Deteksi dengan YOLOv4-tiny
YOLOv4-tiny memiliki 37 lapisan (mulai dari 0), masukan 416 × 416, dan dua peta fitur untuk deteksi. Pelatihan memakai kerangka Darknet pada GTX 1080 8 GB, ukuran *batch* 64, SGD dengan momentum 0,9 dan peluruhan bobot 0,0005, laju belajar awal 0,001, 50.000 iterasi, dan transfer dari bobot COCO.

### 4. Pelacakan batang dengan CSR-DCF
Batang pertama menurut arah gerak video dipilih sebagai target pelacakan. Pelacak melatih templat DCF dengan fitur HoG dan Colornames serta peta keandalan spasial. Selisih posisi antarbingkai menjadi perpindahan acuan $s$.

### 5. Algoritma penghitungan
Pada bingkai pertama, ID apel diberikan berurutan menurut arah gerak video. Pada bingkai berikutnya: (a) posisi kotak batang dari pelacak dibandingkan dengan semua deteksi batang memakai tingkat tumpang tindih (IoU); bila tumpang tindih maksimum kurang dari 30% (ambang dipilih dari uji 10%, 20%, 30%, 40%, 50%), kotak deteksi dengan tumpang tindih terbesar menggantikan kotak pelacak untuk memperbarui pelacak; (b) perpindahan acuan dihitung dari posisi batang; (c) apel bingkai sebelumnya yang digeser dengan $s$ dicocokkan dengan apel terdeteksi berjarak Euklides terkecil; (d) ID apel pasangan disamakan. Bila batang yang dilacak tidak lagi utuh di bidang pandang, batang lain dijadikan target pelacakan. Pelacak diganti lebih awal untuk menghindari kegagalan pelacakan.

### 6. Metrik
mAP rerata dari AP apel dan AP batang. Untuk penghitungan: MIDE (*mean ID calculation error*) berbasis jumlah apel yang berganti ID antarbingkai, RMSE hitungan per bingkai terhadap rerata hitungan manual tiga operator, dan Pc = $[1-|P_t-N_t|/N_t]\times100\%$ untuk hitungan per video.

## Eksperimen dan Hasil
Data uji deteksi berisi 1.280 citra dengan 37.642 target (teks tidak menjelaskan bahwa angka ini berasal dari himpunan teruji yang telah diaugmentasi; 20% dari 6.400 adalah 1.280, yang dihitung dalam ringkasan ini). Pengujian penghitungan memakai video kebun dengan hitungan manual rerata tiga operator sebagai acuan.

Tabel 1 (deteksi pada data uji):

| Objek | TP | FP | FN | P (%) | R (%) | AP (%) | mAP (%) |
|---|---|---|---|---|---|---|---|
| Apel | 37.376 | 4.035 | 266 | 90,26 | 99,29 | 99,59 | 99,35 |
| Batang | tidak terbaca | tidak terbaca | tidak terbaca | tidak terbaca | tidak terbaca | 99,10 | |

Waktu deteksi rerata YOLOv4-tiny adalah 0,022 detik per citra 1920 × 1080. Seluruh batang pada data uji terdeteksi menurut penulis.

Hasil penghitungan pada video:

| Indikator | Nilai |
|---|---|
| Jumlah video pada regresi | 15 video (10 sampai 104 bingkai; 76 sampai 478 buah) |
| R² (hitungan algoritma vs hitungan manual) | 0,9875 |
| Pc rerata | 91,30% |
| Rerata buah terdeteksi per bingkai | 38 (sekitar 0,01 *false positive* dan 0,19 *false negative* per bingkai) |
| MIDE (10 bingkai berurutan, Tabel 2) | 0,199 |
| RMSE (10 bingkai berurutan, Tabel 2) | 2,387 |
| Kecepatan | 2 sampai 5 fps pada CPU (laptop i7-8565U) |

Pada sepuluh bingkai berurutan (bingkai 37 sampai 46), paling banyak empat ID berganti pada satu bingkai. Penyebab pergantian ID menurut penulis adalah buah yang tidak terdeteksi berkesinambungan, serta buah berjarak Euklides dekat saat salah satunya tidak terdeteksi.

Pembandingan dengan *deep sort* (kerangka pelacakan-berbasis-deteksi dengan filter Kalman dan algoritma Hungarian), memakai detektor yang sama pada lima video yang sama: metode usulan memperoleh akurasi hitung rerata 91,60%, sedangkan *deep sort* mengalami penghitungan berlebih yang serius (angka *deep sort* hanya tampak pada Gambar 9a dan tidak terbaca dari teks). Kecepatan *deep sort* 0 sampai 2 fps. Penulis menyatakan bahwa perbandingan dengan studi lain sulit karena data dan lingkungan berbeda.

## Kelebihan dan Keterbatasan
Kelebihan: hanya satu target (batang) yang dilacak sehingga beban komputasi lebih ringan daripada pelacakan semua buah, hitungan berjalan pada CPU dengan 2 sampai 5 fps, dan hasil dibandingkan dengan hitungan manual tiga operator pada video nyata. Hasil metode lebih baik daripada *deep sort* pada data yang sama menurut penulis.

Keterbatasan yang dinyatakan penulis: hitungan hanya mencakup satu sisi barisan pohon; sebagian apel terlihat dari kedua sisi dinding buah sehingga penjumlahan kedua sisi akan menghitung ganda buah itu, dan penulis berencana mengembangkan algoritma yang mengenali buah yang terlihat dari kedua sisi. Pergantian ID akibat deteksi yang tidak berkesinambungan dan jarak buah yang dekat juga dinyatakan sebagai sumber galat. Penulis berencana mengukur diameter dan volume buah dengan kamera kedalaman.

Menurut pembacaan ringkasan ini: (a) pelacakan memakai asumsi bahwa semua objek diam mengalami perpindahan yang sama pada bidang citra, sehingga pada pohon dengan kedalaman yang berbeda (paralaks) asumsi ini hanya mendekati; (b) acuan hitungan berupa hitungan manual pada video, bukan hasil panen; (c) 10 video diakui di bagian data, tetapi regresi memakai 15 video, dan teks tidak menjelaskan selisih itu; (d) hanya satu kultivar dan satu kebun yang diuji; (e) hanya dua kelas (apel dan batang) tanpa kelas kematangan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai video dari satu sisi baris pohon. Mekanismenya adalah pencocokan antarbingkai berbasis gerak: perpindahan batang yang dilacak dipakai memprediksi posisi buah, lalu buah dicocokkan dengan jarak Euklides terdekat dan ID dipertahankan. Hitungan dilaporkan per video (total), bukan per kelas; satu-satunya kelas selain apel adalah batang pohon sebagai penanda gerak. Acuan hitungnya adalah hitungan manual pada video (rerata tiga operator), bukan panen. Identitas lintas sisi tidak ditangani; penulis secara eksplisit menyebutnya sebagai pekerjaan mendatang karena buah yang terlihat dari kedua sisi akan terhitung ganda.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: penggunaan objek struktural berukuran besar sebagai penanda gerak (dalam hal ini batang) untuk mencocokkan buah antarbingkai tanpa melacak seluruh buah, dan pelaporan RMSE serta tingkat pergantian ID. Makalah ini juga menyatakan bahwa masalah penghitungan ganda lintas sisi baris belum terselesaikan, yang sejalan dengan kebutuhan identitas lintas pandang pada tandan sawit.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `gao2021appleb`.

Gao, Yang, dan Fu (2021) mengembangkan penghitungan apel dari video kebun dinding buah vertikal dengan mendeteksi apel dan batang menggunakan YOLOv4-tiny (mAP 99,35% pada data uji citra), melacak satu batang dengan CSR-DCF, dan memakai perpindahan batang untuk mencocokkan apel yang sama antarbingkai. Pada video, hitungan algoritma berkorelasi dengan hitungan manual (R² 0,9875; 15 video) dengan akurasi hitung rerata 91,30%. Hitungan terbatas pada satu sisi barisan, dan penggabungan kedua sisi disebut sebagai pekerjaan mendatang.

Catatan verifikasi data: AP apel 99,59%, AP batang 99,10%, mAP 99,35%, dan 37.642 target pada 1.280 citra uji bersumber dari Tabel 1 dan teks bagian "Performance of the detection network"; R² 0,9875 dan Pc 91,30% dari Gambar 6 dan teksnya; MIDE 0,199 dan RMSE 2,387 dari Tabel 2 dan teksnya; 91,60% dan perbandingan *deep sort* dari bagian "Comparison with other methods" (Gambar 9a, angka per video tidak terbaca). Ekstraksi Tabel 1 tidak lengkap: nilai TP, FP, FN, P, dan R untuk kelas batang tidak terbaca dan tidak ditebak, dan kolom "Detection time/s" tertulis 28 yang tidak konsisten dengan teks (0,022 detik per citra). Rumus 2 sampai 4 pada ekstraksi rusak sebagian. Jumlah video yang disebut berbeda (10 video pada data, 15 video pada regresi) dan selisihnya tidak dijelaskan. Makalah ini bukan terbitan jurnal bertinjauan sejawat (prosiding presentasi ASABE).
