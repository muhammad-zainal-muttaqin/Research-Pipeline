# Towards a Real-Time Oil Palm Fruit Maturity System Using Supervised Classifiers Based on Feature Analysis

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `alfatni2022real` |
| Judul asli | Towards a Real-Time Oil Palm Fruit Maturity System Using Supervised Classifiers Based on Feature Analysis |
| Penulis | Alfatni, Meftah Salem M.; Khairunniza-Bejo, Siti; Marhaban, Mohammad Hamiruce B.; Saaed, Osama M. Ben; Mustapha, Aouache; Shariff, Abdul Rashid Mohamed |
| Tahun | 2022 |
| Venue | Agriculture Switzerland |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [alfatni2022real.pdf](../pdf/alfatni2022real.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture12091461

## Gambaran Umum
Makalah ini menyajikan rancangan dan pengujian sistem klasifikasi kematangan tandan buah segar (TBS) kelapa sawit secara non-destruktif dengan kamera CCD dan pengolahan citra. Sistem mengekstraksi fitur warna (statistik dan histogram) serta fitur tekstur (*Gabor wavelet*, *gray level co-occurrence matrix* atau GLCM, dan *basic gray level aura matrix* yang ditulis penulis sebagai BGLAM) dari citra tandan. Fitur itu diklasifikasikan dengan tiga pengklasifikasi terawasi: *support vector machine* (SVM), *K-nearest neighbor* (KNN), dan jaringan saraf tiruan (*artificial neural network*, ANN) berjenis *multilayer perceptron* (MLP). Kinerja dinilai dengan kurva ROC (*receiver operating characteristic*) dan luas di bawahnya (AUC), serta akurasi uji dan waktu pemrosesan citra.

Data berupa citra tandan dari tiga varietas kulit buah kelapa sawit, yaitu Nigrescens, Oleifera, dan Virescens, dengan tiga kelas kematangan (*under-ripe*, *ripe*, *over-ripe*) yang ditetapkan oleh seorang pakar. Citra diambil di laboratorium dalam kotak tertutup dengan pencahayaan LED terkendali, bukan di kebun. Makalah tidak menangani pencacahan.

Hasil utama: kombinasi BGLAM dan ANN pada wilayah minat ROI3 (100 × 100 piksel) mencapai akurasi uji 93,00% dengan waktu 0,44 detik untuk klasifikasi jenis TBS. Untuk kematangan, BGLAM dengan ANN mencapai 92,00% (Nigrescens, ROI3, 0,43 detik) dan 93,00% (Oleifera dan Virescens, ROI2, 0,40 detik). Histogram warna dengan ANN pada ROI3 mencapai 94,00% pada Tabel 6 (1,6 detik).

## Latar Belakang: Masalah yang Ingin Dipecahkan
Mutu minyak sawit mentah bergantung pada pemanenan TBS pada tahap kematangan optimal. Penulis menyatakan bahwa cara penentuan saat ini bertumpu pada pengamatan warna dan brondolan (buah lepas) oleh manusia, tidak mudah diulang, dan rentan terhadap kesalahan manusia. Mereka menginginkan metode yang murah, cepat, non-invasif, andal, dan presisi, terutama bagi wilayah perdesaan dengan fasilitas otomasi terbatas.

Tinjauan singkat pada Bagian 2 (Tabel 1) memuat kinerja berbagai sistem penglihatan komputer pada banyak komoditas, dan penulis menyimpulkan bahwa ruang warna RGB dan pengklasifikasi SVM paling sering dipakai. Penulis menilai bahwa untuk TBS sawit diperlukan sistem yang menggabungkan perangkat lunak (pengolahan citra, data, keputusan berbasis AI) dan perangkat keras (pencahayaan, penyortir).

## Ide Utama
Gagasan makalah ini adalah membandingkan secara sistematis lima teknik ekstraksi fitur (statistik warna, histogram warna, Gabor, GLCM, BGLAM) dengan tiga pengklasifikasi (ANN, KNN, SVM) pada tiga ukuran wilayah minat (ROI1 300 × 300, ROI2 50 × 50, ROI3 100 × 100 piksel), lalu memilih kombinasi dengan AUC dan akurasi tertinggi serta waktu pemrosesan terpendek. Tiga model fitur diuji: model warna, model tekstur, dan model duri (*thorn*) pada permukaan tandan.

Penulis menyimpulkan bahwa ANN memberi akurasi tertinggi, diikuti KNN dan SVM. Menurut penulis, SVM memang pengklasifikasi yang umumnya kokoh, tetapi ANN lebih baik karena derau alami pada data.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Kegiatan dimulai dengan kunjungan lapangan ke kebun MPOB Kluang, Malaysia, bersama tim Universiti Putra Malaysia dan Lembaga Minyak Sawit Malaysia (MPOB). Terkumpul 270 citra buah untuk setiap tipe dari tiga tipe (Nigrescens, Oleifera, Virescens). Seorang pakar mengklasifikasikan buah menjadi *under-ripe*, *ripe*, dan *over-ripe*. Pengumpulan dilakukan 15 sampai 20 buah per hari sesuai kapasitas laboratorium. Perangkat berupa kotak tertutup berisi tabung pencahayaan LED, kamera warna CCD DFK 41BF02.H FireWire di bagian atas, alat pengumpan sampel, dan unit pengolah. Makalah tidak melaporkan jumlah pohon, kultivar spesifik di luar tiga tipe tersebut, atau resolusi citra mentah.

### 2. Praproses dan ekstraksi fitur
Citra diproses melalui akuisisi, praproses, segmentasi, dan ekstraksi fitur. Tiga wilayah minat dipakai: ROI1 (300 × 300), ROI2 (50 × 50), dan ROI3 (100 × 100). Fitur warna meliputi rerata, simpangan baku, dan histogram warna. Fitur tekstur meliputi Gabor, GLCM, dan BGLAM. Penulis juga menguji model fitur duri.

### 3. Klasifikasi
- ANN-MLP: propagasi balik dengan masukan dinormalisasi pada rentang [0, 1]; keluaran target 0,5, 0, dan 1 untuk *under-ripe*, *ripe*, dan *over-ripe*. Jumlah neuron tersembunyi dipilih secara eksperimental (Tabel 3, misalnya arsitektur [45 × 22 × 1] untuk BGLAM).
- KNN: k = 1, 3, 5, 7, 9 dan jarak Euclidean, *city-block*, cosine, korelasi. Konfigurasi terbaik adalah k = 1 dengan jarak *city-block*.
- SVM: strategi satu-lawan-semua; kernel linear, polinomial, dan RBF; sigma RBF 1 sampai 100, derajat polinomial 1 sampai 4, parameter C 1 sampai 1000. Konfigurasi terbaik yang dilaporkan adalah sigma 10 dan C 500 pada BGLAM (Tabel 4).

### 4. Pembagian data dan evaluasi
Dua pertiga data dipakai untuk pelatihan dan sisanya untuk penilaian. Teks menyebut 90 sampel per kelas untuk pengujian. Evaluasi memakai kurva ROC, AUC, akurasi, galat kuadrat rerata (MSE), efisiensi, dan waktu pemrosesan citra.

## Eksperimen dan Hasil
Empat eksperimen dijalankan: klasifikasi jenis TBS dengan tekstur (eksperimen 1), serta klasifikasi kematangan per jenis dengan model warna, tekstur, dan duri (eksperimen 2 sampai 4). Acuan label adalah penilaian pakar pada buah yang dipanen; tidak ada hitung panen atau hitung lapangan.

Tabel 5 (klasifikasi jenis TBS, akurasi uji %, waktu detik):

| Fitur dan ROI | ANN | KNN | SVM |
|---|---|---|---|
| BGLAM, ROI1 | 91,00 (1,02 s) | 75,00 (0,98 s) | 90,00 (1,74 s) |
| BGLAM, ROI2 | 89,00 (0,43 s) | 76,00 (0,38 s) | 77,00 (1,14 s) |
| BGLAM, ROI3 | 93,00 (0,44 s) | 89,00 (0,40 s) | 82,00 (1,32 s) |
| GLCM, ROI3 | 86,00 (0,56 s) | 77,00 (0,51 s) | 69,00 (1,22 s) |

Hasil terbaik per jenis untuk kematangan (Tabel 6 dan 7, akurasi uji %):

| Model fitur | Nigrescens | Oleifera | Virescens |
|---|---|---|---|
| Histogram warna dengan ANN | 94,00 (ROI3, 1,6 s) | 94,00 (ROI3, 1,6 s) | 93,00 (ROI2, 1,4 s) |
| BGLAM dengan ANN | 92,00 (ROI3, 0,43 s) | 93,00 (ROI2, 0,40 s) | 93,00 (ROI2, 0,40 s) |

Pada Tabel 6, statistik warna dengan ANN untuk Virescens mencapai 93,00% menurut teks. Model duri (Tabel 8) memberi hasil lebih rendah: terbaik 87,00% (GLCM dengan ANN, ROI1) untuk Nigrescens, 91,00% (BGLAM dengan SVM, ROI3, 1,20 s) untuk Oleifera, dan 87,00% (BGLAM dengan ANN, ROI3) untuk Virescens. Penulis mengaitkan hasil rendah itu dengan derau data.

Perbandingan AUC pada ANN (Gambar 13): statistik ROI1 93,1413%, histogram ROI3 93,8765%, GLCM ROI3 92,4842%, BGLAM ROI3 92,9067%, Gabor ROI1 82,9945%. KNN terbaik dengan k = 1 dan jarak *city-block* mencapai AUC 93,00%, 92,00%, 91,00%, 92,00%, dan 80% untuk statistik, histogram, GLCM, BGLAM, dan Gabor. Akurasi SVM terbaik 92% (BGLAM, ROI3; Tabel 4).

Pada Tabel 3 (MSE dan efisiensi ANN), efisiensi pelatihan mendekati 0,999 pada GLCM, BGLAM, histogram, dan Gabor, sedangkan efisiensi uji berkisar dari 0,2048 (Gabor, [40 × 30 × 1]) sampai 0,9189 (histogram, [25 × 10 × 1]). Selisih besar antara efisiensi pelatihan dan uji menunjukkan kecocokan berlebih pada data latih, tetapi makalah tidak membahasnya secara eksplisit.

## Kelebihan dan Keterbatasan
Kelebihan: perbandingan luas atas fitur, pengklasifikasi, dan ukuran ROI dengan metrik AUC dan waktu; waktu pemrosesan di bawah satu detik untuk kombinasi terbaik; pengujian tiga varietas kulit buah.

Keterbatasan yang dinyatakan penulis: lingkup penelitian terbatas pada hubungan antara tingkat kematangan dan pendekatan pengolahan citra serta AI; pencahayaan perlu dikendalikan (disarankan filter polarisator linier); perlu sensor lain seperti kamera termal; perlu korelasi dengan analisis kimia internal (kandungan minyak dan asam lemak bebas); metode temu kembali berbasis kemiripan masih berupa pekerjaan lanjutan; sistem perlu digeneralisasi untuk komoditas lain. Penulis juga menyebut hasil model duri buruk akibat derau data dan kinerja SVM yang peka terhadap derau.

Menurut pembacaan ringkasan ini: (1) citra diambil dari buah yang telah dipanen dalam kotak berpencahayaan terkendali, sehingga hasil belum mewakili tandan di pohon dengan oklusi dan cahaya alami; (2) hanya satu pakar yang melabeli data, dan tidak ada uji kesepakatan antarpelabel; (3) angka 270 citra per tipe, pembagian dua pertiga untuk pelatihan, dan 90 sampel uji per kelas tidak sepenuhnya konsisten satu sama lain pada teks; (4) tidak dilaporkan ulangan, validasi silang, atau interval kepercayaan, sehingga selisih satu sampai dua poin antarkombinasi sulit ditafsirkan; (5) tidak ada matriks konfusi per kelas kematangan.

## Kaitan dengan Tinjauan main6
Makalah ini tidak menangani buah yang terlihat lebih dari sekali. Tidak ada mekanisme asosiasi lintas citra, pelacakan, atau pencocokan multi-pandang. Unit analisis adalah citra satu tandan. Hitungan tidak dilaporkan; keluarannya adalah label jenis dan label kematangan per citra, sehingga tidak ada acuan hitung panen, hitung manual lapangan, atau anotasi jumlah.

Yang dapat dipindahkan ke pencacahan tandan multi-sisi adalah komponen penentuan kelas kematangan: fitur warna dan tekstur dari wilayah tandan dapat memberi atribut kelas bagi tiap deteksi, sedangkan pencacahan identitas harus dikerjakan oleh komponen lain. Hasilnya menunjukkan bahwa kelas kematangan sawit dapat dipisahkan dengan fitur sederhana dalam kondisi terkendali; hal itu belum menjamin kinerja pada citra lapangan.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `alfatni2022real`.

Alfatni dkk. merancang sistem klasifikasi kematangan dan jenis TBS kelapa sawit dengan kamera CCD pada kotak berpencahayaan terkendali, memakai fitur warna dan tekstur (Gabor, GLCM, BGLAM) dan pengklasifikasi ANN, KNN, serta SVM. Kombinasi BGLAM dengan ANN mencapai akurasi uji 93,00% dalam 0,44 detik untuk klasifikasi jenis TBS, dan ANN umumnya mengungguli KNN dan SVM pada data berukuran 270 citra per tipe.

Catatan verifikasi data: akurasi 93,00% dan 0,44 detik berasal dari Tabel 5 serta abstrak; hasil kematangan dari Tabel 6 dan 7; hasil model duri dari Tabel 8; MSE dan efisiensi dari Tabel 3; konfigurasi SVM dari Tabel 4 (nilai sigma dan C terbaca dari teks, kolom ROI tabel terpotong sebagian); nilai AUC dari legenda Gambar 13 dan 14 pada teks ekstraksi. Angka 270 citra per tipe dan 90 sampel uji per kelas dari Bagian 2.1 dan 2.5. Teks ekstraksi memuat sebagian tabel dengan susunan kolom terpisah sehingga pembacaan Tabel 6 dan 8 mengikuti urutan baris dan dapat keliru bila urutan bergeser. Jumlah pohon, lokasi kebun per tandan, dan resolusi citra tidak dilaporkan. Ejaan nama varietas pada keterangan Gambar 2 berbeda dari teks utama; entri ini memakai Nigrescens, Oleifera, dan Virescens.
