# A case study on the integration of a snapshot hyperspectral field-portable imager solving fruit quality assessment

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cho2025case` |
| Judul asli | A case study on the integration of a snapshot hyperspectral field-portable imager solving fruit quality assessment |
| Penulis | Cho, SeongHyun; Sheppard, Eli; Castello, Elvira; Spanellis, Alexander; Pearce, Daniel; Chappell, Steve |
| Tahun | 2025 |
| Venue | Proceedings of SPIE the International Society for Optical Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [cho2025case.pdf](../pdf/cho2025case.pdf)
- DOI resmi: https://doi.org/10.1117/12.3042114

## Gambaran Umum

Makalah prosiding SPIE (Proc. SPIE Vol. 13373, 2025) ini merupakan studi kasus tentang integrasi kamera hiperspektral *snapshot* portabel (Living Optics) untuk penilaian mutu dan estimasi hasil buah kebun. Kerangka yang diusulkan mencakup segmentasi, pencacahan, pengukuran ukuran, dan estimasi kematangan buah dengan memadukan data spektral dan RGB. Tanaman yang diteliti adalah apel Royal Gala, pir, dan apel Cox di kebun buah milik produsen buah kebun terbesar di Inggris; pengujian kematangan dilakukan di laboratorium pada 40 sampel apel Royal Gala.

Hasil utama: kombinasi pengklasifikasi spektral 1D-ConvNet dengan segmentasi SAM2 dan penyaringan kemiripan spektral mencapai mAP@50 0,8210 dan *recall* 0,7030, sedangkan YOLOv8s berbasis RGB mencapai mAP@50 0,7535 dan *recall* 0,4586. Penulis menyebut peningkatan *recall* sekitar 25 persen (selisih sederhana 0,7030 dikurangi 0,4586 adalah 0,2444, dihitung oleh ringkasan ini). Pada estimasi kematangan, regresi *partial least squares* (PLSR) menghasilkan R² 0,71 dan RMSE 0,4385 terhadap nilai Brix.

Makalah juga memuat tahap pelacakan antarbingkai untuk menghitung buah unik pada satu sisi baris pohon. Tahap ini tidak memiliki acuan hitungan sebenarnya; "akurasi pencacahan" yang dilaporkan dibandingkan dengan perkiraan sekitar 7.500 pir per sisi baris dan berkisar 18,91% sampai 49,25%.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pencitraan hiperspektral (*hyperspectral imaging*, HSI) menangkap banyak pita panjang gelombang sehingga dapat membedakan bahan dan perubahan biokimia yang tidak tampak pada RGB. Penulis menyebut kendala penerapannya di pertanian: dimensi data spektral yang tinggi, data berlabel yang terbatas, serta variasi spektrum akibat oklusi, bayangan, dan keburaman gerak. Pada kebun buah, deteksi berbasis RGB kehilangan buah yang tertutup sebagian atau buah yang warnanya mirip dedaunan, misalnya pir hijau.

Penulis juga menyatakan perlunya kerangka terpadu dari satu sensor yang mencakup deteksi, pelacakan, ukuran, dan kematangan, serta perlunya dataset hiperspektral kebun yang terbuka. Tinjauan pustaka pada makalah merangkum metode klasifikasi HSI (k-NN, SVM, *random forest*, jaringan konvolusi), pencacahan buah, dan kendala estimasi hasil, tanpa angka baru yang diverifikasi di sini.

## Ide Utama

Gagasan utamanya adalah memanfaatkan spektrum kulit buah untuk mengklasifikasi titik-titik spektral, lalu menggabungkannya dengan segmentasi spasial pada citra RGB. Spektrum diklasifikasi per titik, kemudian segmen hasil model segmentasi (SAM2 atau FastSAM) diberi kelas berdasarkan kelas non-latar yang paling sering muncul di dalamnya. Dengan cara ini buah yang hanya tampak sebagian tetap dapat terdeteksi bila sebagian kecil permukaannya terlihat.

Untuk pencacahan antarbingkai video, setiap deteksi diberi koordinat 3D dari estimasi kedalaman monokular, lalu semua deteksi disatukan dalam satu sistem koordinat melalui registrasi awan titik antarbingkai, dan deteksi yang berdekatan dikelompokkan sebagai satu buah unik.

## Cara Kerja Langkah demi Langkah

```
 Citra RGB + 96 pita spektral (4.384 sampel spektral per bingkai)
        |                               |
 Klasifikasi spektrum            Segmentasi RGB (SAM2/FastSAM)
 (RF atau 1D-ConvNet)                   |
        |                               |
        +--------> penetapan kelas segmen <---+
                          |
            DAv2 -> awan titik -> ICP antarbingkai
                          |
          pengelompokan aglomeratif (Ward) -> buah unik
```

### 1. Akuisisi data

Data diambil dengan kamera hiperspektral Living Optics (VIS-NIR, 440 nm sampai 900 nm). Tiap sampel berisi citra RGB 2048 x 2432 x 3 dan data hiperspektral 96 pita dari 4.384 sampel spektral. Dataset dibuat bersama produsen buah kebun terbesar di Inggris dan mencakup lebih dari 1.000 pohon dari beberapa varietas, Maret sampai September. Subset beranotasi terdiri atas 44 berkas mentah dan 439 bingkai, dibagi 8:2 pada tingkat berkas mentah untuk mencegah kebocoran data. Tiga kelas beranotasi: Royal Gala Apple (3.785 instans), Pear (2.523), dan Cox Apple (73); kelas Cox hanya ada pada data latih. Sampel spektral di luar masker diberi kelas latar. Pada data latih terdapat 1.855.755 spektrum latar dan 51.285 spektrum latar depan. Jumlah pohon per video, kultivar pir, dan jumlah citra video tidak dilaporkan.

Kamera hanya mengumpulkan sampel spektral pada wilayah tengah 1920 x 1920, sehingga hanya objek di wilayah itu yang diberi label dan citra untuk model spasial-spektral serta YOLOv8s diubah menjadi 960 x 960.

### 2. Praproses spektrum

Dua normalisasi diterapkan: konversi ke pseudo-reflektansi (spektrum dibagi iluminan yang diestimasi dari rata-rata 5% piksel paling terang) dan normalisasi jumlah (tiap spektrum dibagi jumlah salurannya).

### 3. Pengklasifikasi spektral

*Random forest* (RF) memakai 400 estimator, minimum dua sampel per daun, dan lima sampel per pemisahan. 1D-ConvNet dipilih melalui pencarian grid atas 32 arsitektur; arsitektur terpilih berupa satu lapis konvolusi 64 neuron dan empat lapis terhubung penuh 512, 256, 128, 64, dioptimalkan dengan Adam dan penghentian dini pada F1 validasi. Ketidakseimbangan latar dan latar depan diatasi dengan enam skema (tanpa penyeimbangan, pembobotan kelas, dua skema subsampling latar, dua skema duplikasi data). Skema *Background subsampling 1* terbaik; tanpa penyeimbangan atau dengan pembobotan kelas, model hanya memprediksi latar (akurasi nominal 0,97).

### 4. Segmentasi spasial-spektral dan pascaproses

Empat kombinasi dievaluasi: RF + FastSAM, RF + SAM2, 1D-ConvNet + FastSAM, 1D-ConvNet + SAM2. Tiga hiperparameter pascaproses dioptimalkan dengan pencarian grid: *Spectral Classification Confidence* (SCC), *Spectral Angle Factor* (SA Factor), dan *Segmentation Confidence* (SC). Pembanding RGB adalah YOLOv8s untuk segmentasi yang dilatih dengan Ultralytics (960 x 960, Adam, *dropout* 40%, patience 200 epoch).

### 5. Pelacakan dan pencacahan buah unik

Kedalaman metrik diestimasi dengan DepthAnythingV2 (encoder `vitl`, bobot metrik VKitti 2), tanpa penyetelan halus pada kebun. Karena bobot itu berskala tidak terkalibrasi, penulis mengonversi dengan papan catur bersegi 2,5 cm yang diberi label manual pada dua adegan (Jx = 15,524 dan Jy = 15,863). Transformasi antarbingkai diestimasi dengan ICP *point-to-plane* (Open3D) lalu dikumulasikan sehingga semua pusat deteksi berada pada koordinat bingkai pertama. Deteksi duplikat dikelompokkan dengan pengelompokan aglomeratif (jarak Ward) dan `fcluster`. Penulis menyebut kumulasi galat ICP menimbulkan *drift* yang terlihat pada Gambar 8, dan asumsi tahap ini adalah adegan statis dengan kamera bergerak.

### 6. Pengukuran ukuran dan kematangan

Lebar dan tinggi buah dihitung dari masker dan awan titik DAv2 melalui empat titik terjauh; deteksi pir dengan tinggi kurang dari 1,7 kali lebar dianggap parsial. Kematangan diestimasi dengan PLSR linear pada 40 apel Royal Gala di laboratorium (iluminasi halogen dan LED pita lebar, geometri 45/0°), nilai Brix diukur dengan refraktometer genggam (akurasi plus minus 0,2 °Bx), dan pembagian data 50/50 dalam ruang radiansi.

## Eksperimen dan Hasil

Evaluasi deteksi memakai data uji 20% pada tingkat berkas mentah dari subset beranotasi. Metrik yang dipakai: mAP@50, F1, F2, *recall*, presisi, IoU spektral dan spasial, TNR, FNR, FPR, G-Mean, MCC, akurasi, dan GFLOPs.

Pengklasifikasi spektral (Tabel 3):

| Metrik | RF | 1D-ConvNet | 1D-ConvNet + penyaringan kemiripan |
|---|---|---|---|
| mAP@50 | 0,2266 | 0,3768 | 0,3254 |
| F1 | 0,1836 | 0,3653 | 0,3502 |
| *Recall* | 0,1569 | 0,7840 | 0,7276 |
| Presisi | 0,3059 | 0,2622 | 0,2649 |
| Akurasi | 0,5229 | 0,9082 | 0,9103 |

Pengklasifikasi spasial-spektral dan pembanding RGB (Tabel 4 dan 5):

| Model | mAP@50 | F1 | *Recall* | Presisi | IoU spasial |
|---|---|---|---|---|---|
| RF + FastSAM | 0,4572 | 0,3171 | 0,2893 | 0,4442 | 0,2531 |
| RF + SAM2 | 0,4238 | 0,2978 | 0,2813 | 0,3920 | 0,2315 |
| 1D-ConvNet + FastSAM | 0,5738 | 0,3619 | 0,3399 | 0,5170 | 0,2623 |
| 1D-ConvNet + SAM2 | 0,8192 | 0,6396 | 0,7004 | 0,6732 | 0,4866 |
| 1D-ConvNet + SAM2 + penyaringan kemiripan | 0,8210 | 0,6416 | 0,7030 | 0,6741 | 0,4886 |
| YOLOv8s (RGB) | 0,7535 | 0,5561 | 0,4586 | 0,7532 | 0,4098 |

Biaya komputasi: 1D-ConvNet + SAM2 sekitar 5.549,56 GFLOPs dibanding 6,28 GFLOPs untuk YOLOv8s. YOLOv8s unggul pada presisi dan FPR (0,0030 berbanding 0,0191), tetapi melewatkan lebih dari separuh buah (FNR 0,5414). Penulis menyatakan bahwa 1D-ConvNet + FastSAM lemah karena FastSAM tidak disetel halus, dan bahwa YOLOv8s menyamai atau melampaui model terbaik pada beberapa metrik.

Tingkat pencacahan per kelas (Tabel 6) berbeda dari teks. Tabel memuat Royal Gala Apple 0,4981 dan Pear 0,7948 untuk 1D-ConvNet + SAM2 + penyaringan kemiripan, serta 0,2541 dan 0,4802 untuk YOLOv8s. Teks pada seksi 6.1.2 menyebut 0,4597 dan 0,7926 untuk kombinasi 1D-ConvNet + SAM2. Penulis tidak menjelaskan perbedaan itu, dan definisi "counting rate" tidak dirinci.

Pelacakan pir pada dua blok (Tabel 7):

| Blok dan sisi | Total deteksi | Deteksi unik | "Akurasi pencacahan" |
|---|---|---|---|
| 7-157 kiri | 2.616 | 1.418 | 18,91% |
| 7-157 kanan | 6.589 | 2.725 | 36,33% |
| 7-160 kiri | 7.038 | 2.914 | 38,85% |
| 7-160 kanan | 19.376 | 3.694 | 49,25% |
| Gabungan | 35.619 | 10.751 | 35,84% |

Penulis menyatakan tidak ada hitungan sebenarnya per baris; tiap baris diperkirakan memuat sekitar 15.000 pir, dan karena hanya satu sisi dicitrakan per video, diasumsikan sekitar 7.500 pir per sisi.

Ukuran pir (Tabel 8, gabungan): lebar rerata 5,62 plus minus 2,05 cm dan panjang rerata 11,88 plus minus 4,08 cm; 41,59% pir berlebar kurang dari 5,1 cm. Ukuran acuan pir diambil dari sumber internet, tanpa pengukuran lapangan.

Kematangan: PLSR linear menghasilkan R² 0,71 dan RMSE 0,4385 pada 40 apel (pembagian 50/50).

## Kelebihan dan Keterbatasan

Kelebihan: perbandingan beberapa pengklasifikasi spektral dan segmentor pada data dan pembagian yang sama; penggunaan metrik selain akurasi sehingga mode kolaps ke kelas latar terdeteksi; pembagian data pada tingkat berkas mentah; dan dataset yang dinyatakan terbuka (Hugging Face, Living Optics). Seluruh rantai dari deteksi sampai kematangan dari satu sensor didemonstrasikan.

Keterbatasan yang dinyatakan penulis: kombinasi dengan SAM2 sangat mahal secara komputasi; FastSAM dan DAv2 tidak disetel halus; kalibrasi kedalaman memerlukan objek acuan dan intervensi manual luring serta mungkin tidak berlaku pada kedalaman lain; *drift* ICP merusak pengelompokan; tidak ada hitungan sebenarnya buah unik maupun ukuran sebenarnya; pelacakan mengasumsikan adegan statis; kelas Cox Apple sangat sedikit dan tampaknya membingungkan kelas Pear; eksperimen kematangan baru berupa uji awal berskala kecil di laboratorium.

Menurut pembacaan ringkasan ini: (a) klaim "pencacahan akurat" pada ringkasan makalah tidak didukung oleh angka, karena "akurasi pencacahan" 18,91% sampai 49,25% dihitung terhadap perkiraan, bukan hitungan sebenarnya; (b) perbandingan dengan YOLOv8s tidak setara dari sisi sumber daya (sekitar 5.550 GFLOPs berbanding 6,28 GFLOPs) dan YOLOv8s lebih unggul pada presisi; (c) hiperparameter pascaproses dan arsitektur dipilih dengan metrik pada data yang sama dengan evaluasi menurut uraian makalah, sehingga bias optimistis mungkin ada, meskipun makalah tidak menyatakan secara eksplisit; (d) subset beranotasi kecil (439 bingkai), tanpa ulangan atau selang kepercayaan; (e) data kematangan tidak berasal dari buah di pohon.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali pada bingkai video yang berurutan. Mekanismenya adalah pelacakan berbasis geometri: pusat deteksi diproyeksikan ke koordinat 3D dari estimasi kedalaman monokular, disatukan antarbingkai dengan ICP, lalu dikelompokkan secara aglomeratif untuk membentuk identitas buah unik. Pelacakan tidak memakai kemiripan penampilan atau pencocokan fitur. Hitungan per kelas tidak dilaporkan untuk tahap pelacakan; Tabel 7 hanya memuat pir. Hitungan sebenarnya tidak ada: acuannya adalah perkiraan sekitar 15.000 pir per baris (diasumsikan 7.500 per sisi), bukan panen atau hitung manual di lapangan, dan hasilnya jauh di bawah perkiraan itu (10.751 deteksi unik gabungan untuk empat sisi). Pada Tabel 6 terdapat "counting rate" per kelas untuk deteksi, tetapi definisinya tidak dijelaskan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: pola penyatuan koordinat lalu pengelompokan untuk menekan duplikasi, serta pelajaran negatifnya bahwa galat pose yang terakumulasi (*drift* ICP) langsung merusak identitas buah. Makalah tidak membahas penggabungan sisi pohon yang berbeda, tidak membahas atribut kelas seperti kematangan pada pencacahan, dan tidak memuat tandan kelapa sawit.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `cho2025case`.

Cho dkk. (2025) memaparkan studi kasus kamera hiperspektral *snapshot* portabel pada kebun apel dan pir, yang menggabungkan klasifikasi spektral 1D-ConvNet dengan segmentasi SAM2 dan menghasilkan mAP@50 0,8210 serta *recall* 0,7030 pada subset beranotasi 439 bingkai, dibandingkan YOLOv8s berbasis RGB dengan mAP@50 0,7535 dan *recall* 0,4586. Mereka juga melacak pir antarbingkai video dengan estimasi kedalaman monokular, ICP, dan pengelompokan aglomeratif, tetapi tanpa hitungan sebenarnya sehingga akurasi pencacahan tidak dapat dinilai. Estimasi Brix pada 40 apel di laboratorium dengan PLSR menghasilkan R² 0,71.

Catatan verifikasi data: angka deteksi spektral dan spasial-spektral diambil dari Tabel 3, 4, dan 5; hasil pelacakan dari Tabel 7; ukuran pir dari Tabel 8; R² 0,71 dan RMSE 0,4385 dari seksi 9.2; jumlah kelas dan bingkai dari seksi 4. Selisih *recall* 0,2444 dihitung oleh ringkasan ini. Tabel 2 (optimasi pascaproses) terbaca sebagian dari hasil ekstraksi teks sehingga nilai parameternya tidak dikutip. Kolom TNR pada Tabel 3 tampak identik dengan baris F2 untuk dua model, kemungkinan akibat galat ekstraksi atau cetak, sehingga nilai TNR tersebut tidak dikutip. Nilai Tabel 6 berbeda dari teks seksi 6.1.2 (lihat bagian hasil). Tidak tersedia dari teks: jumlah pohon pada video pelacakan, kultivar pir, hasil di luar satu pembagian data, dan hitungan sebenarnya buah unik. Teks makalah berbahasa Inggris.
