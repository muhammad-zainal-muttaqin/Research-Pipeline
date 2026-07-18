# 160 - Conditional DETR for Fast Training Convergence

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `meng2021conditionaldetr` |
| Judul asli | Conditional DETR for Fast Training Convergence |
| Penulis | Meng, Depu; Chen, Xiaokang; Fan, Zejia; Zeng, Gang; Li, Houqiang; Yuan, Yuhui; Sun, Lei; Wang, Jingdong |
| Tahun | 2021 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2108.06152
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Conditional%20DETR%20for%20Fast%20Training%20Convergence
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Conditional%20DETR%20for%20Fast%20Training%20Convergence&sort=relevance

## Gambaran Umum
Conditional DETR memperkenalkan mekanisme perhatian silang kondisional (*conditional cross-attention*) untuk mengatasi masalah lambatnya konvergensi pelatihan pada model *Detection Transformer* (DETR) standar. Makalah ini menunjukkan bahwa lambatnya konvergensi DETR disebabkan oleh ketergantungan yang tinggi pada representasi konten (*content embeddings*) dalam melokalisasi ekstremitas (*extremities*) objek serta memprediksi kotak pembatas (*bounding box*). Hal ini membuat model membutuhkan proses pencarian spasial yang panjang dan tidak efisien pada tahap awal pelatihan.

Untuk menyelesaikan permasalahan tersebut, Conditional DETR memisahkan perhatian konten dan perhatian spasial dalam modul perhatian silang secara eksplisit. Jaringan ini memproyeksikan kueri spasial kondisional (*conditional spatial query*) dari keluaran dekoder layer sebelumnya yang dikombinasikan dengan titik acuan (*reference point*) 2D. Pendekatan ini mempersempit ruang pencarian spasial sehingga setiap kepala perhatian (*attention head*) dapat langsung berfokus pada wilayah spesifik di sekitar objek. Hasil eksperimen menunjukkan bahwa model ini mencapai konvergensi pelatihan hingga 6,7 kali lebih cepat pada tulang punggung (*backbone*) ResNet-50 dan ResNet-101, serta hingga 10 kali lebih cepat pada varian *dilated* DC5-ResNet-50 dan DC5-ResNet-101 jika dibandingkan dengan DETR asli.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Arsitektur DETR memelopori pendekatan deteksi objek berbasis transformer yang bersifat ujung-ke-ujung (*end-to-end*). Namun, kelemahan utama dari model DETR standar adalah lambatnya konvergensi pelatihan, di mana model memerlukan sekitar 500 *epoch* untuk mencapai performa optimal pada dataset COCO. Lambatnya konvergensi ini menjadi hambatan besar bagi penelitian dan penerapan praktis model berbasis transformer.

Secara teknis, keterlambatan ini berakar pada formulasi perhatian silang di dalam dekoder. Pada DETR asli, kueri objek (*object query*) dibentuk dengan menjumlahkan kueri konten dan kueri posisi (spasial). Key yang dicocokkan juga dibentuk dengan cara serupa dari fitur citra dan koordinat piksel spasial. Ketika operasi perkalian titik (*dot product*) dilakukan antara kueri dan kunci, muncul komponen perkalian silang (*cross-terms*) antara konten dan posisi. Komponen silang ini membingungkan model karena konten kueri dipaksa mencocokkan diri dengan posisi kunci, dan sebaliknya.

Silang-pencocokan ini memperlambat proses belajar. Selain itu, penyusupan posisi kueri (*query positional embedding*) pada DETR asli bersifat statis dan dipelajari secara global untuk seluruh dataset. Kueri posisi statis ini hanya mampu memprediksi wilayah objek secara umum tanpa memperhatikan variasi konten citra masukan secara dinamis. Akibatnya, dekoder harus sangat bergantung pada fitur konten untuk memandu lokalisasi ekstremitas objek. Di awal pelatihan, karena fitur konten belum terbentuk dengan baik, proses lokalisasi ini berjalan lambat dan tidak stabil, yang memperlambat konvergensi model secara keseluruhan.

## Ide Utama
Ide utama dari Conditional DETR adalah melakukan dekopling (*decoupling*) atau pemisahan eksplisit antara kueri konten dan kueri spasial dalam proses komputasi perhatian silang. Alih-alih menjumlahkan kedua representasi tersebut, model ini menggabungkan keduanya melalui operasi konkatenasi (*concatenation*), sehingga menghilangkan interaksi silang yang membingungkan antara konten dan posisi pada modul perhatian.

Untuk memberikan panduan spasial yang dinamis, Conditional DETR memperkenalkan mekanisme kueri spasial kondisional. Setiap kueri objek diasosiasikan dengan sebuah titik acuan 2D yang dapat diperbarui dari satu lapisan dekoder ke lapisan berikutnya. Titik acuan ini kemudian dipetakan menjadi representasi posisi sinusoidal. Fitur konten dari lapisan dekoder sebelumnya digunakan untuk memprediksi matriks transformasi linier (skala). Representasi posisi sinusoidal kemudian dimodulasi secara multiplikatif oleh skala tersebut untuk menghasilkan kueri spasial kondisional. Modulasi ini memungkinkan kueri spasial untuk menyesuaikan jangkauan pencariannya secara dinamis berdasarkan konten objek yang sedang diprediksi, sehingga perhatian silang dapat langsung terfokus pada wilayah spasial yang relevan seperti batas-batas fisik objek.

## Cara Kerja Langkah demi Langkah
Mekanisme Conditional DETR beroperasi secara berurutan mulai dari ekstraksi fitur oleh enkoder hingga proses pembaruan titik acuan di dekoder. Berikut adalah rincian tahapan kerja model:

### Formulasi Perhatian Silang Konvensional vs Kondisional
Pada DETR standar, perkalian titik antara kueri $q$ dan kunci $k$ didefinisikan sebagai:
$$q^\top k = (f_q + p_q)^\top (f_k + p_k) = f_q^\top f_k + f_q^\top p_k + p_q^\top f_k + p_q^\top p_k$$
Di mana $f_q$ dan $f_k$ adalah fitur konten, sedangkan $p_q$ and $p_k$ adalah fitur posisi spasial. Suku $f_q^\top p_k$ dan $p_q^\top f_k$ merupakan interaksi silang yang menurunkan efisiensi pembelajaran.

Conditional DETR mengubah formulasi ini dengan memisahkan pencocokan konten dan spasial secara eksplisit menggunakan konkatenasi:
$$q = [f_q; q_s], \quad k = [f_k; p_k]$$
Sehingga hasil perkalian titiknya menjadi:
$$q^\top k = f_q^\top f_k + q_s^\top p_k$$
Di mana $q_s$ adalah kueri spasial kondisional dan $p_k$ adalah penyusupan posisi kunci spasial (*key spatial positional embedding*) yang diturunkan dari koordinat piksel enkoder. Formulasi ini menjamin tidak ada suku silang yang membingungkan jaringan.

### Penentuan Titik Acuan 2D
Setiap kueri objek dikaitkan dengan sebuah titik acuan 2D $s = [x_s, y_s]^\top$ yang merepresentasikan tebakan awal lokasi pusat objek. Pada lapisan dekoder pertama, titik-titik acuan ini merupakan parameter yang dapat dipelajari secara bebas oleh model (*learnable parameters*). Pada lapisan-lapisan berikutnya, titik acuan diperbarui menggunakan prediksi pergeseran (*offset*) yang dihasilkan oleh lapisan dekoder sebelumnya.

### Pemetaan Sinusoidal dan Modulasi Spasial
Titik acuan $s$ yang memiliki nilai dalam rentang $[0, 1]$ dinormalisasi dan dipetakan ke dalam ruang dimensi tinggi menggunakan fungsi penyusupan posisi sinusoidal:
$$p_s = \text{sinusoidal}(s)$$
Di mana $p_s \in \mathbb{R}^d$ terdiri dari penggabungan komponen sinus dan kosinus untuk koordinat $x$ dan $y$.

Untuk menyesuaikan arah dan skala pencarian spasial berdasarkan karakteristik objek (misalnya, memperlebar jangkauan perhatian untuk objek berukuran besar), fitur konten dekoder $f_q$ diproyeksikan melalui sebuah lapisan linier untuk menghasilkan vektor skala $\lambda_q \in \mathbb{R}^d$:
$$\lambda_q = \text{Linear}(f_q)$$
Kueri spasial kondisional $q_s$ kemudian diperoleh melalui operasi perkalian elemen demi elemen (*element-wise multiplication*):
$$q_s = \lambda_q \odot p_s$$
Operasi modulasi ini memungkinkan kueri spasial untuk meregangkan atau menyusutkan koordinat spasial masukan, memfokuskan kepala perhatian pada tepi-tepi batas objek (*object extremities*).

### Proses Multi-Head Cross-Attention
Dalam mekanisme perhatian multi-kepala (*multi-head attention*), kunci spasial $p_k$ dipetakan ke setiap kepala perhatian menggunakan proyeksi linier yang berbeda. Demikian pula, kueri spasial kondisional $q_s$ diproyeksikan ke setiap kepala perhatian. Hal ini memberikan kebebasan bagi setiap kepala perhatian untuk mencari koordinat ekstremitas objek yang berbeda (misalnya, kepala pertama fokus pada tepi atas, kepala kedua pada tepi kanan).

### Diagram Aliran Data
Mekanisme pembentukan kueri spasial kondisional dan interaksinya dalam modul perhatian silang dapat digambarkan pada diagram berikut:

```
[Fitur Enkoder]                   [Decoder Output f_q (Layer l-1)]
       |                                       |
       | (Content & Position)                  +---------------+
       v                                       |               |
  Key: [f_k ; p_k]                             v               v
       |                              Pembaruan Titik    Lapisan Linier
       |                                 Acuan 2D              |
       |                                       |               v
       |                                  Titik s     Skala \lambda_q
       |                                       |               |
       |                                       v               |
       |                                  Sinusoidal           |
       |                                   Encoding            |
       |                                       |               |
       |                                       v               |
       |                                   Vektor p_s          |
       |                                       |               |
       |                                       +-------+-------+
       |                                               |
       |                                               v (Modulasi \odot)
       |                                            Kueri q_s
       |                                               |
       +-----------------------+-----------------------+
                               |
                               v
                     Perhatian Silang (q^T k)
                    = (f_q^T f_k + q_s^T p_k)
                               |
                               v
                      [Keluaran Dekoder]
```

## Eksperimen dan Hasil
Conditional DETR dievaluasi pada dataset COCO 2017 menggunakan arsitektur ResNet-50 (R50) dan ResNet-101 (R101) sebagai tulang punggung, termasuk varian dengan konvolusi terdilasi pada tahap kelima (DC5-R50 dan DC5-R101) untuk mempertahankan resolusi spasial tinggi pada peta fitur akhir.

Pada pelatihan jangka pendek sebanyak 50 *epoch*, Conditional DETR dengan tulang punggung R50 mencapai akurasi sebesar $40,9\%$ Average Precision (AP). Hasil ini sangat kompetitif jika dibandingkan dengan model DETR asli yang hanya mendapatkan $42,0\%$ AP setelah melalui pelatihan sepanjang 500 *epoch*. Hal ini menunjukkan percepatan konvergensi pelatihan sekitar 10 kali lipat untuk mencapai tingkat performa yang setara. Ketika pelatihan diperpanjang menjadi 108 *epoch*, akurasi Conditional DETR-R50 meningkat menjadi $43,0\%$ AP, melampaui performa puncak DETR asli.

Untuk varian tulang punggung yang lebih kuat pada pengujian 50 *epoch*, performa model tercatat sebagai berikut:
- **Conditional DETR-R101 (50 epoch):** Mencapai $42,8\%$ AP.
- **Conditional DETR-R101 (108 epoch):** Meningkat menjadi $44,6\%$ AP.
- **Conditional DETR-DC5-R50 (50 epoch):** Mencapai $43,8\%$ AP.
- **Conditional DETR-DC5-R101 (50 epoch):** Mencapai $45,0\%$ AP.

Analisis peta perhatian menunjukkan bahwa Conditional DETR berhasil mengurangi area aktivasi yang tidak perlu pada awal pelatihan. Kepala perhatian membatasi fokus pencariannya secara lokal di sekitar titik acuan spasial, yang secara drastis menyederhanakan masalah optimasi parameter dibandingkan dengan DETR asli yang harus mencari seluruh area citra secara global tanpa panduan spasial awal.

## Kelebihan dan Keterbatasan
Dari analisis struktural dan hasil eksperimen, Conditional DETR menunjukkan beberapa karakteristik keunggulan serta keterbatasan spesifik:

### Keunggulan
- **Konvergensi Pelatihan yang Sangat Cepat:** Mampu memotong waktu pelatihan yang dibutuhkan dari 500 *epoch* menjadi hanya 50 *epoch* untuk mencapai tingkat performa yang sebanding dengan DETR asli.
- **Formulasi Matematika yang Bersih:** Dekopling konten dan posisi menghilangkan interaksi silang yang tidak perlu pada operasi perhatian silang, membuat representasi fitur lebih mudah dioptimalkan.
- **Interpretabilitas yang Tinggi:** Setiap kepala perhatian secara konsisten melokalisasi wilayah ekstremitas objek tertentu, memberikan penjelasan visual yang logis mengenai cara model memprediksi kotak pembatas.
- **Kompatibilitas Komponen:** Mekanisme ini dapat diintegrasikan dengan mudah ke dalam struktur dekoder DETR standar tanpa memerlukan modifikasi arsitektur yang besar pada enkoder.

### Keterbatasan
- **Beban Komputasi Enkoder Tetap Tinggi:** Perbaikan konvergensi hanya difokuskan pada bagian dekoder. Model ini tetap mempertahankan enkoder transformer standar yang memiliki kompleksitas waktu dan memori kuadratik terhadap ukuran peta fitur citra masukan.
- **Ketergantungan pada Titik Acuan Awal:** Performa model sensitif terhadap kualitas titik acuan spasial yang dipelajari. Jika titik acuan gagal melokalisasi area sekitar objek pada lapisan awal, proses regresi offset pada lapisan berikutnya akan kesulitan mengoreksi prediksi kotak pembatas.
- **Akurasi di Bawah Model Detektor Modern:** Meskipun jauh lebih cepat daripada DETR asli, akurasi puncak Conditional DETR masih berada di bawah model-model berbasis transformer generasi berikutnya (seperti DINO atau Co-DETR) yang menggunakan kueri berbentuk kotak (*anchor box*) secara langsung.

## Kaitan dengan Bab Lain
Conditional DETR merupakan tonggak penting dalam perkembangan detektor berbasis transformer, bertindak sebagai jembatan antara model DETR klasik dan model detektor modern.

Model ini secara langsung mewarisi arsitektur dasar dari [DETR](./022%20-%202020%20-%20DETR%20-%20Fondasi%20RGB.md), namun secara khusus memperbaiki masalah konvergensi lambat yang ada pada model tersebut. Dalam hal percepatan konvergensi, model ini berdiri sejajar dengan [Deformable DETR](./023%20-%202021%20-%20Deformable%20DETR%20-%20Fondasi%20RGB.md). Perbedaannya, Deformable DETR menggunakan perhatian lokal terdeformasi yang membatasi komputasi pada beberapa titik sampling terpilih, sedangkan Conditional DETR tetap mempertahankan perhatian global penuh dengan panduan kueri spasial dinamis.

Konsep dekopling konten-posisi dan penggunaan koordinat 2D sebagai referensi dalam Conditional DETR memengaruhi lahirnya model-model berikutnya:
1. [DN-DETR](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md) mengadopsi struktur kueri yang terdekopel dan menambahkan metode *denoising training* untuk menghilangkan ketidakstabilan pencocokan bipartit.
2. [DINO detector](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md) menggabungkan konsep kueri spasial kondisional dengan representasi kotak pembatas 4D (DAB-DETR) serta skema denoising ganda untuk mencapai performa deteksi tingkat tinggi yang konvergen dengan sangat cepat.
3. [RT-DETR](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md) memanfaatkan efisiensi dari evolusi kueri kondisional ini untuk mewujudkan detektor transformer waktu nyata (*real-time*) pertama yang mengungguli keluarga YOLO.
4. [Co-DETR](./165%20-%202023%20-%20Co-DETR%20-%20Fondasi%20RGB.md) memperluas arsitektur ini dengan memperkenalkan kepala pengawasan kolaboratif untuk memperkuat representasi fitur enkoder.

Hubungan dengan representasi tulang punggung yang efisien dan tangguh juga dapat dipelajari pada [Sparse R-CNN](./161%20-%202021%20-%20Sparse%20R-CNN%20-%20Fondasi%20RGB.md), [ConvNeXt](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md), [Swin Transformer V2](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md), dan [Pyramid Vision Transformer](./164%20-%202021%20-%20Pyramid%20Vision%20Transformer%20-%20Fondasi%20RGB.md).

## Poin untuk Sitasi
- **Kunci BibTeX:** `meng2021conditionaldetr`
- **Kutipan Ringkas:** Conditional DETR mempercepat konvergensi pelatihan detektor transformer dengan memperkenalkan mekanisme perhatian silang kondisional. Mekanisme ini memisahkan pencocokan konten dan spasial secara eksplisit melalui operasi konkatenasi kueri dan kunci, serta memodulasi posisi referensi 2D secara dinamis berdasarkan fitur konten dekoder. Pada dataset COCO, model ini mencapai akurasi sebesar 40,9% AP hanya dalam 50 epoch pelatihan menggunakan backbone ResNet-50.
- **Catatan Verifikasi:** Nilai akurasi yang dilaporkan sebesar 40,9% AP (50 epoch, R50) dan 43,0% AP (108 epoch, R50) telah diverifikasi sesuai dengan Tabel 1 dan Tabel 2 pada naskah asli publikasi ICCV 2021. Peningkatan konvergensi sebesar 6,7 kali lipat dilaporkan pada konfigurasi tulang punggung standar, sedangkan peningkatan hingga 10 kali lipat diamati pada varian DC5 yang mempertahankan resolusi spasial tinggi.
