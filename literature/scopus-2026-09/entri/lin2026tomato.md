# Tomato Maturity Classification and Fruit Counting Based on RGB and Multispectral Images †

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lin2026tomato` |
| Judul asli | Tomato Maturity Classification and Fruit Counting Based on RGB and Multispectral Images † |
| Penulis | Lin, Huei-Yung; Pai, Chu-An; Chang, Chin-Chen |
| Tahun | 2026 |
| Venue | Applied Sciences Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [lin2026tomato.pdf](../pdf/lin2026tomato.pdf)
- DOI resmi: https://doi.org/10.3390/app16073227

## Gambaran Umum
Makalah ini (Lin, Pai, dan Chang; *Applied Sciences* 2026, 16, 3227; versi perluasan makalah ICIT 2024) mengusulkan pendekatan terpadu untuk klasifikasi kematangan dan pencacahan buah tomat di rumah kaca dari urutan citra RGB dan citra multispektral. Pendekatan itu terdiri atas tiga tahap: deteksi tomat dengan YOLOv8 yang dipadukan dengan OSNet, pelacakan dan pencacahan dengan StrongSORT, serta klasifikasi kematangan ke tiga kelas (matang, hampir matang, mentah). Penulis menyatakan secara eksplisit bahwa makalah tidak memperkenalkan algoritma baru; kebaruannya terletak pada integrasi komponen yang sudah ada.

Data berasal dari tiga set pengambilan citra di dua rumah kaca (Farm Nineteen dan Lin Family Farm) dengan kamera Parrot Sequoia+ pada jarak sekitar 40 cm dari rak tanaman tomat. Klasifikasi kematangan diuji dengan *support vector machine* (SVM), *k-nearest neighbors* (KNN), dan *artificial neural network* (ANN) pada tiga konfigurasi fitur: R, G, B; indeks vegetasi NDVI, GNDVI, dan GRRI; serta gabungan keenamnya.

Hasil utama: akurasi klasifikasi kematangan maksimum 81% (KNN pada set 19th2_tomato dengan fitur R, G, B maupun gabungan), rerata akurasi lintas set dan lintas pengklasifikasi sebesar 66,8% untuk fitur gabungan, 64,9% untuk indeks vegetasi saja, dan 63,8% untuk RGB saja. Pencacahan berbasis pelacakan menunjukkan selisih terhadap acuan yang kecil pada beberapa urutan dan besar pada urutan lain (misalnya selisih -22 pada satu urutan set lin_tomato).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemantauan kematangan dan jumlah buah tomat di rumah kaca memengaruhi estimasi jumlah buah, penjadwalan panen, dan keputusan pengelolaan tanaman. Pemantauan manual disebut memerlukan banyak tenaga dan waktu serta rentan terhadap galat manusia. Variasi pencahayaan, oklusi, dan buah yang saling tumpang tindih menyulitkan klasifikasi kematangan dan pencacahan yang andal.

Penulis menunjuk dua kelemahan pada pendekatan terdahulu. Pertama, banyak metode menganalisis citra tunggal tanpa melacak buah individual sehingga menghasilkan penghitungan ganda dan prediksi kematangan yang tidak stabil. Kedua, metode yang bertumpu pada indeks spektral saja atau fitur visual saja dapat gagal membedakan tahap kematangan yang tampak serupa. Penulis juga mencatat bahwa metode berbasis RGB peka terhadap iluminasi, bayangan, dan kerumitan latar.

## Ide Utama
Gagasan utamanya adalah mengaitkan setiap tomat yang sama antarbingkai dalam urutan citra melalui pelacakan, sehingga (a) setiap buah dihitung berdasarkan identitas (ID) yang unik dan (b) prediksi kematangan dari banyak bingkai untuk satu buah dapat digabung melalui pemungutan suara mayoritas (*majority voting*). Fitur klasifikasi kematangan menggabungkan nilai warna RGB dengan indeks vegetasi dari kanal multispektral melalui penggabungan tingkat fitur (*feature-level fusion*, konkatenasi).

Kontribusi yang dinyatakan penulis ada tiga: kerangka terpadu deteksi, pelacakan multi-objek, dan klasifikasi kematangan; analisis efektivitas gabungan fitur RGB dan indeks vegetasi beserta kontribusi relatif tiap indikator; dan evaluasi pada beberapa set data tomat dengan beberapa model klasifikasi.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data
Perangkat yang dipakai adalah Parrot Sequoia+ yang memuat kamera RGB 16 MP (4608 × 3456 piksel), empat kamera multispektral satu pita (hijau, merah, *red-edge*, inframerah dekat) masing-masing 1280 × 960 piksel, dan sensor cahaya matahari untuk kalibrasi radiometrik. Jarak pemotretan sekitar 40 cm dari rak tomat. Terdapat tiga set data pada dua rumah kaca: 19th_tomato (September hingga Oktober), lin_tomato (November hingga Januari), dan 19th2_tomato (Maret hingga April). Dua set pertama dipotret sekali tiap tujuh hari, sedangkan set ketiga dua kali tiap tujuh hari. Pada tiap rumah kaca dipilih tiga baris tanaman: dua baris untuk latih dan satu baris untuk uji. Set 19th_tomato memuat tiga urutan latih dan dua urutan uji; lin_tomato lima urutan latih dan lima uji; 19th2_tomato lima urutan latih dan lima uji. Kultivar tomat tidak dilaporkan. Citra multispektral dikalibrasi dan diselaraskan terhadap citra RGB karena terdapat selisih spasial kecil.

Jumlah tomat beranotasi (Tabel 2): 19th_tomato 4.247 latih dan 1.775 uji; lin_tomato 4.554 latih dan 2.423 uji; 19th2_tomato 8.720 latih dan 4.338 uji. Jumlah citra tidak dilaporkan.

### 2. Pelabelan kematangan
Urutan citra diubah ke struktur set data IRIS yang menyimpan, per bingkai dan per tomat, ID unik, citra RGB, citra multispektral, dan label kematangan. Tomat dipantau tiap minggu dan label diberikan secara retrospektif berdasarkan jumlah minggu tersisa sebelum panen, dibantu ciri warna kulit (hijau ke merah). Label -1 berarti siap panen (matang), -2 berarti sekitar satu minggu menjelang panen (hampir matang), dan -3 berarti dua minggu atau lebih menjelang panen (mentah). Tomat yang membutuhkan tiga minggu atau lebih hampir tidak berubah tampilannya sehingga semuanya diberi label -3.

### 3. Deteksi tomat
Detektor adalah YOLOv8 yang diintegrasikan dengan OSNet (*omni-scale network*), jaringan konvolusi yang semula dikembangkan untuk identifikasi ulang orang dan dipakai di sini sebagai modul ekstraksi fitur multiskala. Pelatihan memakai Ultralytics dengan laju belajar awal 0,01, *optimizer* SGD (momentum 0,937, *weight decay* 0,001), 200 *epoch*, dan ukuran *batch* 8. Detektor dilatih pada citra RGB dengan satu kelas target, yaitu tomat.

### 4. Pelacakan dan pencacahan
Pelacak yang dipakai adalah StrongSORT (pengembangan DeepSORT dengan modul AFLink untuk menyambung potongan lintasan), dalam bentuk model prapelatihan. Tiap tomat yang terdeteksi memperoleh ID unik antarbingkai berurutan, dan jumlah ID dipakai sebagai hitungan buah. Penulis tidak merinci kriteria pencocokan selain bahwa gerak dan penampilan digabungkan.

### 5. Segmentasi pra-pemrosesan dan ekstraksi fitur
Untuk mengurangi gangguan dari ranting yang menutupi, citra diubah dari RGB ke YUV, lalu kanal V disegmentasi dengan ambang Otsu guna menekan derau latar dan pantulan spekular. Karena kepadatan buah dan oklusi, kotak persegi panjang hasil deteksi didekati dengan bentuk elips agar piksel latar berkurang. Nilai R, G, B, NDVI, GNDVI, dan GRRI dihitung sebagai rerata intensitas piksel pada area tak tertutup masker di dalam kotak tiap tomat. Rumusnya: NDVI = (NIR - RED)/(NIR + RED), GNDVI = (NIR - GRE)/(NIR + GRE), dan GRRI = RED/GRE. Indeks vegetasi ditransformasi dengan *principal component analysis* (PCA), lalu digabung dengan R, G, B melalui konkatenasi.

### 6. Klasifikasi kematangan
Tiga pengklasifikasi dievaluasi dengan validasi silang 10 lipatan. SVM memakai kernel RBF dengan C dari 10 sampai 40 (langkah 2) dan gamma pada pengaturan skala bawaan. KNN memakai K dari 2 sampai 30 (langkah 2). ANN berupa perceptron berlapis dengan satu lapis tersembunyi, 300 *epoch*, dan ukuran *batch* 40. Pembagian latih dan uji dilakukan pada tingkat urutan. Akurasi dihitung sebagai rasio kotak pembatas yang diprediksi benar setelah pemungutan suara antarbingkai terhadap seluruh kotak pada semua bingkai. Pada tahap klasifikasi ini informasi pelacakan tidak dipakai dan semua kotak pada data latih maupun uji diambil dari label acuan.

```
 Urutan citra RGB --> YOLOv8 + OSNet --> StrongSORT --> ID unik per tomat
                                                              |
 Citra multispektral --> kalibrasi/penyelarasan               v
        |                                              kotak per bingkai
        +--> NDVI, GNDVI, GRRI (PCA) --+                      |
 R, G, B (area elips, ambang Otsu) -----+--> konkatenasi --> SVM/KNN/ANN
                                                              |
                                          pemungutan suara antarbingkai
                                                              |
                                      hitungan buah per kelas kematangan
```

## Eksperimen dan Hasil
Evaluasi klasifikasi memakai tiga set data yang disebut di atas, dengan pembagian latih-uji menurut baris tanaman. Pembanding internal adalah tiga pengklasifikasi (SVM, KNN, ANN) dan tiga konfigurasi fitur. Tidak ada pembanding eksternal dengan metode orang lain secara kuantitatif; penulis hanya menyatakan secara naratif bahwa kinerjanya sebanding dengan metode terdahulu.

Tabel 3 melaporkan akurasi klasifikasi kematangan:

| Set data | Pengklasifikasi | R, G, B | NDVI, GNDVI, GRRI | R, G, B + indeks |
|---|---|---|---|---|
| 19th_tomato | SVM | 63% | 70% | 63% |
| 19th_tomato | KNN | 64% | 66% | 64% |
| 19th_tomato | ANN | 62% | 73% | 73% |
| lin_tomato | SVM | 64% | 55% | 65% |
| lin_tomato | KNN | 58% | 58% | 58% |
| lin_tomato | ANN | 38% | 75% | 46% |
| 19th2_tomato | SVM | 72% | 70% | 78% |
| 19th2_tomato | KNN | 81% | 59% | 81% |
| 19th2_tomato | ANN | 72% | 58% | 73% |

Penulis menyimpulkan bahwa, kecuali pada 19th_tomato, metode berbasis RGB mengungguli pendekatan multispektral pada dua set lain. Penjelasan yang diajukan untuk 19th_tomato adalah bahwa citra diambil awal musim tumbuh sehingga peralihan warna hijau ke merah belum berkembang. Analisis kontribusi fitur (Gambar 4) menunjukkan komponen hijau paling berkontribusi pada pembedaan kematangan, sedangkan pengaruh indeks multispektral, kanal merah, dan kanal biru bervariasi antarset. Tabel 4 membandingkan R + G + B, R + B saja, dan indeks saja; hasilnya menunjukkan bahwa pada hampir semua set penghapusan kanal hijau menurunkan akurasi di bawah akurasi indeks multispektral, dengan 19th_tomato sebagai pengecualian.

Tabel 5 melaporkan metrik tambahan (presisi, *recall*, dan F1 dirata-ratakan makro lintas tiga kelas) bersama akurasi:

| Set data | Presisi | *Recall* | F1 | Akurasi |
|---|---|---|---|---|
| 19th_tomato | 0,54 | 0,54 | 0,53 | 66,7% |
| lin_tomato | 0,80 | 0,83 | 0,80 | 79,8% |
| 19th2_tomato | 0,76 | 0,76 | 0,74 | 72,2% |

Matriks konfusi (Gambar 5) menunjukkan pembedaan yang relatif baik antara kelas -1 (matang) dan -2 (hampir matang), sedangkan kekeliruan besar terjadi antara -2 (hampir matang) dan -3 (mentah) karena warna kulit keduanya mirip. Berdasarkan pengamatan pada dua set pertama, warna tomat nyaris tidak berubah sampai sekitar satu setengah minggu sebelum matang penuh dan berubah cepat pada satu setengah minggu terakhir; karena itu frekuensi pengambilan citra set ketiga dinaikkan menjadi dua kali per minggu. Teks tidak menjelaskan konfigurasi dan pengklasifikasi yang menghasilkan angka Tabel 5, dan angka akurasinya tidak sama dengan nilai pada Tabel 3.

Pencacahan berbasis pelacakan yang digabung dengan klasifikasi kematangan dilaporkan pada Tabel 6, per urutan uji, dengan hitungan acuan dan prediksi untuk kelas -3, -2, -1 dan total, selisih total, serta RMSE. Sebagian baris:

| Urutan uji | Total acuan | Total prediksi | Selisih total | RMSE |
|---|---|---|---|---|
| 19th_tomato (6th), sekali seminggu | 35 | 34 | -1 | 4,65 |
| 19th_tomato (7th), sekali seminggu | 14 | 12 | -2 | 2,45 |
| lin_tomato (4th), sekali seminggu | 29 | 7 | -22 | 9,20 |
| lin_tomato (8th), sekali seminggu | 7 | 6 | -1 | 1,29 |
| 19th2_tomato (5th), sekali seminggu | 37 | 27 | -10 | 5,77 |
| 19th2_tomato (9th), sekali seminggu | 11 | 12 | 1 | 0,58 |
| 19th2_tomato (5th), dua kali seminggu | 37 | 27 | -10 | 5,83 |
| 19th2_tomato (8th), dua kali seminggu | 43 | 35 | -8 | 2,71 |

Hitungan prediksi lebih kecil daripada acuan pada hampir semua urutan. Penulis mengaitkan selisih besar pada lin_tomato dengan oklusi berat dan dedaunan rapat yang mengganggu deteksi dan pelacakan. Kata "konsisten" pada abstrak dan kesimpulan tidak disertai ukuran kuantitatif tunggal; penulis tidak melaporkan galat relatif terhadap hitungan acuan secara agregat.

## Kelebihan dan Keterbatasan
Kelebihan yang dapat dicatat dari teks: kerangka ini menyatukan deteksi, pelacakan, dan klasifikasi kematangan dalam satu alur; pembagian latih-uji dilakukan per baris tanaman dan per urutan sehingga kebocoran informasi antarbagian dikurangi; hasil dilaporkan menurut kelas kematangan; dan analisis kontribusi fitur menunjukkan bahwa kamera RGB berbiaya rendah mungkin cukup untuk banyak tugas penilaian kematangan. Pemungutan suara antarbingkai dinyatakan menstabilkan prediksi tingkat tomat, meskipun teks tidak menyajikan perbandingan dengan dan tanpa pemungutan suara.

Keterbatasan yang dinyatakan penulis: data berasal dari sedikit lingkungan rumah kaca sehingga variasi cahaya, bayangan, dan oklusi dapat memengaruhi ketangguhan; metode mengestimasi jumlah tomat, bukan hasil panen dalam massa atau volume per satuan luas; dan klasifikasi bergantung pada fitur visual dan spektral sehingga akurasi dapat menurun pada tomat yang tertutup daun atau buah lain. Penulis juga menyebut bahwa pencacahan menyimpang lebih besar pada urutan dengan oklusi berat dan menyarankan segmentasi yang lebih baik atau informasi *depth*.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan lain. Pertama, pelacakan dilakukan pada urutan dari satu sisi rak tanaman; teks tidak membahas buah yang terlihat dari sisi berbeda atau pandangan yang tidak berurutan. Kedua, evaluasi pencacahan hanya mencakup 10 sampai belasan urutan kecil (11 sampai 43 tomat per urutan) dan tidak ada ukuran agregat atau pembanding pelacak lain. Ketiga, pada evaluasi klasifikasi kotak acuan dipakai, sehingga akurasi 81% tidak mencerminkan galat deteksi dan pelacakan. Keempat, akurasi maksimum 81% dipilih dari sembilan kombinasi pengklasifikasi dan fitur pada satu set, dan nilai antarkombinasi sangat bervariasi (misalnya ANN pada lin_tomato berkisar 38% sampai 75%). Kelima, parameter C dan K dieksplorasi pada rentang tertentu tanpa dijelaskan nilai terpilih. Keenam, angka akurasi pada Tabel 3 dan Tabel 5 tidak dapat didamaikan dari teks.

## Kaitan dengan Tinjauan main6
Makalah ini menangani tomat yang terlihat pada banyak bingkai dalam urutan citra. Mekanismenya adalah pelacakan multi-objek: detektor YOLOv8 memberi kotak pada tiap bingkai, StrongSORT memberi ID unik yang memadukan gerak dan penampilan serta menyambung potongan lintasan (AFLink), dan jumlah ID menjadi hitungan buah. Pemungutan suara mayoritas atas prediksi kematangan antarbingkai untuk satu ID memberi satu label per buah. Hitungan dilaporkan per kelas kematangan (-3, -2, -1) pada Tabel 6 untuk tiap urutan uji, disertai selisih total dan RMSE per urutan. Acuan hitung adalah anotasi pada urutan citra (label tiap tomat dan hitungan acuan per urutan); teks tidak menyebut hitungan panen atau hitungan manual di lapangan sebagai acuan. Kelas kematangan ditentukan dari waktu tersisa sebelum panen, bukan dari tingkat kematangan visual semata.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola umum "deteksi, ID unik, label kelas pada tingkat identitas melalui pemungutan suara antar-observasi", sehingga satu buah memiliki satu kelas dan satu hitungan. Namun pelacakan di sini bertumpu pada kesinambungan gerak dan penampilan antarbingkai berurutan dari satu sisi; makalah tidak menangani pencocokan antarsisi pohon atau antarcitra tak berurutan. Hasil juga menunjukkan bahwa pelacakan kurang andal pada oklusi berat dan bahwa kelas antara (hampir matang dan mentah) paling sering tertukar, yang relevan bagi inventaris per kelas.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `lin2026tomato`.

Lin, Pai, dan Chang mengusulkan kerangka terpadu klasifikasi kematangan dan pencacahan tomat rumah kaca yang menggabungkan deteksi YOLOv8 dengan OSNet, pelacakan StrongSORT, dan klasifikasi kematangan tiga kelas (SVM, KNN, ANN) dengan fitur RGB dan indeks vegetasi multispektral, memakai pemungutan suara antarbingkai. Pada tiga set data rumah kaca, akurasi klasifikasi maksimum yang dilaporkan adalah 81%, rerata akurasi fitur gabungan 66,8%, dan kanal hijau paling berkontribusi. Pencacahan berbasis pelacakan menunjukkan selisih terhadap hitungan acuan yang kecil pada beberapa urutan dan besar pada urutan dengan oklusi berat.

Catatan verifikasi data: akurasi per kombinasi berasal dari Tabel 3; akurasi maksimum 81% dan rerata 66,8%, 64,9%, dan 63,8% dari Seksi 5.1 (rerata tidak dapat dihitung ulang dari Tabel 3 oleh ringkasan ini); presisi, *recall*, F1, dan akurasi 66,7%, 79,8%, 72,2% dari Tabel 5 (Seksi 5.2); jumlah tomat beranotasi dari Tabel 2; hitungan per urutan, selisih, dan RMSE dari Tabel 6 (Seksi 5.3). Tabel 6 pada ekstraksi teks terbaca baik, tetapi baris lin_tomato (7th) memuat acuan kelas 10, 0, 9 dengan total 18 (jumlah komponen 19), sehingga ada ketidakkonsistenan di sumber atau ekstraksi. Angka Tabel 5 tidak sama dengan nilai pada Tabel 3 dan teks tidak menjelaskan sebabnya. Jumlah citra, kultivar tomat, dan nilai C serta K terpilih tidak dilaporkan. Data tersedia atas permintaan kepada penulis. Teks makalah berbahasa Inggris dan terbaca penuh; gambar tidak terbaca dari ekstraksi.
