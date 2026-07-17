# 085 - Bilateral Cross-Modal Fusion Network for Robot Grasp Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2023bcmfnet` |
| Judul asli | Bilateral Cross-Modal Fusion Network for Robot Grasp Detection |
| Penulis | Qiang Zhang, Xueying Sun |
| Tahun | 2023 |
| Venue | Sensors, vol. 23, no. 6, artikel 3340 |
| Tema | Grasp Robotik |

## Tautan Akses
- **DOI (versi penerbit, akses terbuka):** https://doi.org/10.3390/s23063340
- **PMC (teks penuh gratis):** https://pmc.ncbi.nlm.nih.gov/articles/PMC10057080/
- **Google Scholar:** https://scholar.google.com/scholar?q=Bilateral%20Cross-Modal%20Fusion%20Network%20for%20Robot%20Grasp%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Bilateral%20Cross-Modal%20Fusion%20Network%20for%20Robot%20Grasp%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan BCMFNet (*Bilateral Cross-Modal Fusion Network*), sebuah jaringan deteksi cengkeraman robotik yang mengolah citra RGB dan kedalaman melalui tiga aliran paralel — aliran RGB, aliran kedalaman, dan aliran gabungan — sehingga kedua modal saling memandu satu sama lain, bukan hanya digabungkan searah. Masalah yang disasar adalah cengkeraman visual dua derajat kebebasan (2-DoF, posisi dan sudut penjepit pada bidang citra): bagaimana memanfaatkan informasi warna (tekstur permukaan) dan kedalaman (geometri jarak) secara serentak agar posisi dan orientasi cengkeraman diprediksi lebih akurat daripada bila kedua modal digabung secara statis di awal.

Inti kontribusinya adalah modul interaksi modal (*Modal Interaction Module*, MIM) yang memakai perhatian silang (*cross-attention*) spasial dua arah, sehingga fitur RGB ikut menimbang fitur kedalaman dan sebaliknya, dilengkapi modul interaksi kanal (*Channel Interaction Module*, CIM) yang menyaring fitur gabungan sebelum diteruskan ke kepala prediksi. Pada dataset baku Cornell dan Jacquard, BCMFNet mencapai akurasi *object-wise* 97,8% dan 94,6%, mengungguli sejumlah metode RGB-D sezaman, dan tervalidasi pada lengan robot fisik dengan tingkat keberhasilan 94,5% dari 200 percobaan cengkeraman pada 30 objek rumah tangga yang belum pernah dilihat model. Bab ini melanjutkan garis GR-ConvNet (bab 082) dengan mengganti fusi kanal statis dengan mekanisme interaksi yang dapat dilatih.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi cengkeraman berbasis RGB-D umumnya menggabungkan kedua modal dengan salah satu dari tiga strategi: fusi dini (menumpuk kanal warna dan kedalaman sebagai satu masukan sebelum diproses jaringan), fusi lanjut (memproses kedua modal terpisah lalu menjumlahkan/mengonkatenasi keluarannya), atau fusi menengah pada beberapa titik tetap di dalam jaringan. GR-ConvNet (bab 082), misalnya, menumpuk kanal RGB dan kedalaman menjadi satu masukan *n*-kanal di awal jaringan — pendekatan yang sederhana dan cepat, tetapi bobot relatif antara warna dan kedalaman ditentukan oleh pelatihan konvolusi biasa, bukan disesuaikan secara adaptif per lokasi citra.

Makalah ini beralasan bahwa strategi semacam itu memanfaatkan komplementaritas RGB-kedalaman secara tidak menyeluruh: kedua modal diperlakukan setara di semua wilayah citra, padahal pada kenyataannya kontribusi masing-masing modal berbeda-beda tergantung kondisi permukaan. Pada permukaan datar dan bertekstur jelas, warna lebih informatif untuk menentukan tepi objek; pada permukaan mengilap atau nyaris tanpa tekstur, kedalaman lebih dapat diandalkan untuk menentukan bentuk. Fusi statis tidak dapat menyesuaikan bobot ini per piksel, sehingga akurasi berpotensi tersandera oleh modal yang lebih lemah pada wilayah tertentu. Masalah ini menjadi lebih penting seiring makin banyaknya penerapan lengan robot pada objek rumah tangga yang permukaannya beragam dan kondisi pencahayaannya tidak terkendali.

## Ide Utama

Gagasan inti BCMFNet adalah membuat kedua modal saling menanyai satu sama lain lewat mekanisme perhatian (*attention*) sebelum digabungkan, bukan sekadar ditumpuk atau dijumlahkan. Fitur RGB pada suatu lokasi citra dipakai sebagai kueri untuk "bertanya" ke seluruh peta fitur kedalaman, mencari lokasi kedalaman yang relevan untuk memperkaya pemahaman tentang lokasi RGB itu; pada saat yang sama, fitur kedalaman melakukan hal yang sama terhadap fitur RGB. Karena kedua arah pertanyaan ini berjalan bersamaan, mekanismenya disebut bilateral (dua arah) — berbeda dari fusi searah yang hanya membiarkan satu modal memandu modal lainnya.

Selain interaksi antar-modal secara spasial, jaringan juga membutuhkan penyaringan antar-kanal: setelah fitur RGB, kedalaman, dan gabungan ketiganya disatukan, tidak semua kanal fitur sama pentingnya untuk prediksi akhir. Modul interaksi kanal memberi bobot pada tiap kanal berdasarkan kontribusinya, meredam kanal yang kurang informatif. Kombinasi interaksi spasial (antar-piksel, antar-modal) dan interaksi kanal (antar-fitur) inilah yang membedakan BCMFNet dari pendekatan fusi RGB-D sebelumnya.

## Cara Kerja Langkah demi Langkah

### Arsitektur Tiga Aliran

Jaringan menerima citra RGB dan citra kedalaman sebagai dua masukan terpisah, masing-masing diolah oleh aliran konvolusi tersendiri berpola *encoder–decoder* (menyandikan citra ke fitur padat berresolusi rendah, lalu menyandikannya kembali ke resolusi tinggi). Bagian penyandi kedua aliran memakai modul batang berbasis koneksi residual (*Residual Stem Module*, RSM) yang menurunkan resolusi spasial bertahap sambil menghasilkan fitur multi-skala — dilambangkan cf0 hingga cf4 untuk aliran RGB dan df0 hingga df4 untuk aliran kedalaman, dengan indeks yang lebih besar menandakan fitur beresolusi lebih rendah namun lebih kaya makna. Fitur-fitur ini kemudian disandikan kembali ke resolusi tinggi lewat penaikan skala dengan koneksi pintas (*skip connection* — menyalurkan langsung fitur dari tahap penyandi ke tahap penyandi ulang pada resolusi yang sama, mengurangi hilangnya detail spasial), menghasilkan fitur akhir cf7 dan df7. Aliran ketiga, aliran gabungan, dibangun paralel dengan fitur ff7 yang menyerap hasil interaksi kedua modal pada tiap tingkat skala.

### Modul Interaksi Modal (MIM)

Pada beberapa titik di antara tahap penyandi, fitur RGB dan kedalaman dilewatkan ke MIM. Modul ini terlebih dahulu memecah peta fitur menjadi kepingan kecil (*patch embedding* — membagi peta fitur menjadi blok-blok kecil yang masing-masing diperlakukan sebagai satu unit token), lalu menerapkan perhatian mandiri ringan (*Lightweight Multi-Head Self-Attention*, LMHSA) yang menghubungkan kepingan-kepingan dalam satu modal, dan perhatian silang ringan (*Lightweight Multi-Head Cross-Attention*, LMHCA) yang menghubungkan kepingan RGB dengan kepingan kedalaman secara dua arah. LMHCA inilah mekanisme cross-attention spasial yang menjadi inti bilateral: setiap kepingan RGB memperoleh kueri terhadap seluruh kepingan kedalaman, dan sebaliknya, sehingga bobot penggabungan ditentukan berdasarkan kemiripan fitur pada tiap pasangan lokasi, bukan bobot tetap yang sama untuk seluruh citra.

### Modul Interaksi Kanal (CIM)

Setelah fitur RGB (cf7), kedalaman (df7), dan gabungan (ff7) mencapai resolusi penuh, ketiganya dikonkatenasi (ditumpuk sepanjang dimensi kanal) dan diproses oleh CIM. Modul ini menerapkan mekanisme mirip blok *squeeze-and-excitation* (SE): setiap kanal fitur gabungan diberi bobot skalar hasil pembelajaran, sehingga kanal yang membawa informasi berguna dipertahankan dan kanal yang kurang relevan diredam sebelum diteruskan ke kepala prediksi.

Alur data dari dua citra masukan hingga peta cengkeraman dapat diringkas sebagai berikut.

```
RGB  --> aliran RGB (RSM, turun-skala)  --> cf0..cf4 --> cf7
                    \                                    |
                     \--- MIM: LMHSA + LMHCA (dua arah) --+--> ff7
                    /                                    |
Depth --> aliran Depth (RSM, turun-skala) --> df0..df4 --> df7
                                                          |
                    CIM: konkatenasi [cf7, df7, ff7]
                         + bobot kanal ala SE-block
                                                          |
              peta grasp: Q (mutu) | sin2phi, cos2phi (sudut) | W (lebar)
```

### Representasi Cengkeraman dan Fungsi Loss

Mengikuti rumusan yang sama dengan GG-CNN (bab 081) dan GR-ConvNet (bab 082), keluaran jaringan berupa empat peta seukuran citra: peta mutu cengkeraman Q̃ (skor kelayakan tiap piksel sebagai pusat cengkeraman), dua peta sudut sin(2φ̃) dan cos(2φ̃) (penggandaan sudut menghindari ambiguitas orientasi antipodal 180°), dan peta lebar bukaan penjepit W̃. Pelatihan memakai *smooth L1 loss* (fungsi galat yang kuadratik untuk selisih kecil dan linear untuk selisih besar, sehingga tidak terlalu sensitif terhadap pencilan) dengan parameter ambang β = 1, dihitung sebagai jumlah galat pada seluruh piksel keempat peta terhadap kebenaran anotasi.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua tolok ukur baku deteksi cengkeraman. Dataset Cornell berisi 885 sampel dari 240 objek nyata, dipecah 90% latih dan 10% uji, diperbesar lewat augmentasi (pemotongan dan rotasi acak) karena ukurannya kecil. Dataset Jacquard (bab 086) jauh lebih besar, tersusun dari puluhan ribu citra sintetis hasil simulasi fisika dengan jutaan anotasi cengkeraman, juga dipecah 90:10. Kedua dataset diuji dengan dua skema pemisahan data: *image-wise* (IW, membagi berdasarkan citra sehingga objek yang sama dapat muncul di data latih dan uji) dan *object-wise* (OW, memisahkan berdasarkan objek sehingga model diuji pada objek yang benar-benar baru — skema yang lebih ketat menilai generalisasi). Sebuah prediksi cengkeraman dinyatakan benar bila IoU (*Intersection over Union*, rasio luas irisan terhadap luas gabungan kotak) terhadap anotasi lebih dari 25% dan selisih sudut kurang dari 30°, definisi yang sama dipakai GR-ConvNet.

BCMFNet mencapai akurasi 99,4% (IW) dan 97,8% (OW) pada Cornell, serta 96,7% (IW) dan 94,6% (OW) pada Jacquard, dengan waktu inferensi 17,7 milidetik per citra. Dibandingkan GR-ConvNet (97,7% IW / 96,6% OW pada Cornell, ~20 milidetik), BCMFNet unggul tipis pada akurasi Cornell dengan kecepatan yang sebanding; pada Jacquard, angka akurasi objek-wise BCMFNet (94,6%) setara dengan yang dilaporkan GR-ConvNet. Studi ablasi menunjukkan kontribusi tiap modul: tanpa MIM, akurasi *object-wise* turun tajam ke 89,7% (Cornell) dan 84,6% (Jacquard); tanpa CIM, akurasi turun lebih kecil ke 96,4% dan 92,6%. Selisih penurunan ini mengindikasikan interaksi silang spasial (MIM) menyumbang porsi akurasi yang jauh lebih besar daripada penyaringan kanal (CIM), meski keduanya tetap saling melengkapi karena model penuh (97,8% / 94,6%) mengungguli kedua varian tanpa modul.

Validasi fisik dilakukan pada lengan robot kolaboratif Elite EC-66 berpenjepit paralel dengan kamera RGB-D Orbbec Femto-W. Dari 200 percobaan cengkeraman pada 30 objek rumah tangga yang tidak termasuk data latih, 189 berhasil (94,5%). Angka ini konsisten dengan pola pada bab 082: akurasi tinggi pada tolok ukur akademik diikuti tingkat keberhasilan yang tetap tinggi ketika dipindahkan ke perangkat keras nyata pada objek baru. Penulis makalah mencatat inferensi 17,7 milidetik masih lebih lambat daripada sejumlah metode pembanding lain yang dilaporkan berjalan sekitar 12 milidetik, dan menyebutnya sebagai arah perbaikan pada kerja mendatang.

## Kelebihan dan Keterbatasan

Kelebihan utama BCMFNet terletak pada mekanisme interaksi lintas-modal yang dapat menyesuaikan bobot RGB dan kedalaman secara adaptif per lokasi citra, alih-alih memakai bobot tetap seperti fusi kanal statis pada GR-ConvNet. Studi ablasi mengonfirmasi bahwa interaksi ini — bukan sekadar menambah parameter jaringan — yang menyumbang kenaikan akurasi paling besar. Validasi pada robot fisik dengan objek di luar data latih juga memperkuat klaim generalisasi model.

Dari sisi rekayasa, arsitektur tiga aliran plus modul perhatian silang menambah kompleksitas komputasi dibandingkan jaringan konvolusi murni seperti GR-ConvNet, tercermin pada waktu inferensi yang lebih lambat daripada sejumlah metode pembanding sezaman meski masih tergolong dekat waktu nyata. Secara konseptual, BCMFNet tetap terbatas pada cengkeraman planar 2-DoF: posisi dan sudut penjepit ditentukan pada bidang citra, bukan pada ruang tiga dimensi penuh seperti pendekatan 6-DoF pada bab 084. Keberhasilan model juga tetap bergantung pada kualitas kanal kedalaman; sensor RGB-D konsumen rentan menghasilkan derau atau lubang data pada permukaan mengilap, kondisi yang tidak diuji secara eksplisit pada evaluasi robot 30 objek di atas.

## Kaitan dengan Bab Lain

Bab ini melanjutkan garis fusi RGB-D untuk cengkeraman planar yang dimulai GG-CNN (bab 081) dan diperkuat GR-ConvNet ([082 - GR-ConvNet](./082%20-%202020%20-%20GR-ConvNet%20-%20Grasp%20Robotik.md)): representasi keluaran Q/sudut/lebar dan definisi validitas IoU>25%/sudut<30° diwarisi langsung, sedangkan strategi fusi diganti dari penumpukan kanal statis menjadi interaksi lintas-modal yang dapat dilatih. Dataset Jacquard yang dipakai untuk salah satu evaluasi utama diuraikan pada [086 - Jacquard Dataset](./086%20-%202018%20-%20Jacquard%20Dataset%20-%20Grasp%20Robotik.md). Penyempurnaan arsitektur generatif lain pada garis yang sama dibahas pada [083 - GR-ConvNet v2](./083%20-%202022%20-%20GR-ConvNet%20v2%20-%20Grasp%20Robotik.md), sementara batasan 2-DoF pada bab ini berkontraskan dengan pendekatan cengkeraman 6-DoF berskala besar pada [084 - GraspNet-1Billion](./084%20-%202020%20-%20GraspNet-1Billion%20-%20Grasp%20Robotik.md). Kontribusi bab ini bagi tinjauan adalah menunjukkan bahwa mekanisme perhatian lintas-modal dapat menaikkan akurasi fusi RGB-D untuk grasp tanpa mengorbankan kelayakan waktu nyata secara signifikan.

## Poin untuk Sitasi

Kutip dengan kunci `zhang2023bcmfnet`. Ringkasan yang aman dikutip: "BCMFNet memakai arsitektur tiga aliran dengan modul interaksi modal berbasis perhatian silang dua arah dan modul interaksi kanal untuk menggabungkan fitur RGB dan kedalaman, mencapai akurasi *object-wise* 97,8% pada Cornell dan 94,6% pada Jacquard, serta keberhasilan 94,5% pada 200 percobaan cengkeraman robot fisik." Angka akurasi (99,4%/97,8% Cornell; 96,7%/94,6% Jacquard), waktu inferensi (17,7 ms), dan hasil robot (189/200, 30 objek) diperoleh dari abstrak dan isi artikel versi PMC; angka rinci tabel pembanding metode lain (mis. Kumra dkk., Tian dkk.) dan angka ablasi per modul (89,7%/84,6% tanpa MIM; 96,4%/92,6% tanpa CIM) sebaiknya diverifikasi ulang terhadap tabel PDF resmi sebelum dikutip dalam karya formal, karena diekstraksi lewat alat baca otomatis, bukan pembacaan tabel langsung.
