# 147 - Deep Residual Learning for Image Recognition

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `he2016resnet` |
| Judul asli | Deep Residual Learning for Image Recognition |
| Penulis | He, Kaiming; Zhang, Xiangyu; Ren, Shaoqing; Sun, Jian |
| Tahun | 2016 |
| Venue | IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2016) |
| Tema | Fusi Multimodal |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1512.03385
- **Google Scholar:** https://scholar.google.com/scholar?q=Deep%20Residual%20Learning%20for%20Image%20Recognition
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Deep%20Residual%20Learning%20for%20Image%20Recognition&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan ResNet (*Residual Networks*), sebuah arsitektur jaringan saraf konvolusi yang dirancang untuk mengatasi masalah degradasi akurasi pada jaringan sangat dalam. Dengan memperkenalkan koneksi jalan pintas (*shortcut connection* atau *skip connection*), ResNet memformulasikan ulang lapisan-lapisan konvolusi agar mempelajari fungsi residual terhadap input identitas. Pendekatan ini memungkinkan pelatihan arsitektur jaringan yang jauh lebih dalam tanpa mengalami penurunan akurasi akibat sulitnya optimasi.

Model ResNet dengan kedalaman hingga 152 lapisan berhasil dilatih pada dataset ImageNet, mencapai tingkat kesalahan klasifikasi *top-5 error* sebesar 3,57% menggunakan metode ansambel (*ensemble*). Keberhasilan ini mengantarkan ResNet memenangi berbagai kategori dalam kompetisi ILSVRC and MS COCO 2015. Dalam konteks fusi multimodal, ResNet memainkan peran penting sebagai ekstraktor fitur visual atau tulang punggung (*backbone*) berkinerja tinggi sebelum fiturnya dipadukan dengan modalitas sensor lain.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum diperkenalkannya ResNet, peningkatan kinerja model visi komputer berbasis pembelajaran mendalam sangat bergantung pada penambahan kedalaman jaringan. Model seperti AlexNet, VGG, dan GoogLeNet membuktikan bahwa representasi fitur yang lebih kaya diekstrak dengan menumpuk lebih banyak lapisan konvolusi. Namun, melatih jaringan yang sangat dalam menimbulkan tantangan optimasi berat.

Hambatan pertama adalah gradien menghilang atau meledak (*vanishing or exploding gradient*), yang menghambat aliran gradien saat penyebaran balik (*backpropagation*). Masalah ini sebagian besar diatasi dengan inisialisasi bobot terstandardisasi dan normalisasi *batch* (*batch normalization*), tetapi muncul hambatan lain yang dikenal sebagai masalah degradasi (*degradation problem*).

Masalah degradasi ditandai dengan saturasi akurasi saat kedalaman jaringan meningkat, diikuti penurunan akurasi yang tajam pada model yang lebih dalam. Berbeda dengan kelebihan kecocokan (*overfitting*), galat pelatihan (*training error*) juga meningkat secara signifikan. Sebagai contoh, jaringan polos (*plain network*) dengan 34 lapisan menunjukkan galat pelatihan dan validasi yang lebih buruk dibanding versi 18 lapisan. Secara teoretis, jaringan lebih dalam seharusnya dapat menduplikasi kinerja model dangkal dengan mempelajari pemetaan identitas (*identity mapping*). Namun, optimasi berbasis gradien terbukti kesulitan mengarahkan lapisan non-linear dalam mempelajari pemetaan identitas secara langsung.

## Ide Utama

Gagasan inti ResNet adalah pembelajaran residual (*residual learning*). Alih-alih membiarkan tumpukan lapisan konvolusi non-linear memetakan fungsi target $H(x)$ (dengan $x$ sebagai masukan), lapisan-lapisan tersebut diarahkan mempelajari fungsi residual $F(x) := H(x) - x$. Dengan demikian, pemetaan target didefinisikan sebagai $H(x) = F(x) + x$.

Secara mekanis, formulasi ini diimplementasikan melalui koneksi jalan pintas yang melewati satu atau beberapa lapisan. Koneksi ini melakukan penjumlahan elemen demi elemen (*element-wise addition*) antara masukan identitas $x$ dan keluaran blok konvolusi $F(x)$ tanpa menambah parameter tambahan atau beban komputasi. Intuisinya adalah jika pemetaan identitas optimal, mengarahkan bobot-bobot lapisan non-linear mendekati nol (sehingga $F(x) = 0$) lebih mudah dicapai dibanding memaksa lapisan konvolusi biasa mempelajari pemetaan identitas dari awal melalui transformasi non-linear kompleks.

## Cara Kerja Langkah demi Langkah

### Struktur Blok Residual: BasicBlock dan Bottleneck
Dua jenis blok residual digunakan berdasarkan kedalaman arsitektur:
- **Blok Dasar (*BasicBlock*)**: Digunakan pada ResNet-18 dan ResNet-34. Blok ini terdiri atas dua lapisan konvolusi $3\times3$ berturut-turut. Setiap lapisan diikuti normalisasi *batch* dan fungsi aktivasi unit linear terarah (*rectified linear unit* atau ReLU). Koneksi jalan pintas menghubungkan masukan awal langsung ke hasil sebelum ReLU kedua.
- **Blok Penyempitan (*Bottleneck Block*)**: Dirancang untuk ResNet-50, ResNet-101, dan ResNet-152 guna menekan parameter. Blok ini menggunakan tiga lapisan: konvolusi $1\times1$ untuk mereduksi dimensi saluran (*channel dimension*), konvolusi $3\times3$ untuk ekstraksi fitur spasial, dan konvolusi $1\times1$ untuk mengembalikan jumlah saluran ke dimensi semula. Operasi $3\times3$ yang mahal dilakukan pada dimensi saluran yang diperkecil.

Struktur arsitektur ini digambarkan dalam diagram ASCII berikut:

```
       [ BasicBlock ]                     [ Bottleneck Block ]
       
            Masukan x                           Masukan x
               │                                   │
         ┌─────┴─────┐                       ┌─────┴─────┐
         │           ▼                       │           ▼
         │      Conv 3x3 (F)                 │      Conv 1x1 (Reduksi)
         │           │                       │           │
         │         ReLU                      │         ReLU
         │           │                       │           │
         │      Conv 3x3                     │      Conv 3x3
         │           │                       │           │
         │           │                       │         ReLU
         │           │                       │           │
         │           │                       │      Conv 1x1 (Restorasi)
         │           ▼                       │           ▼
    Identity ────────►+                 Identity ────────►+
                     │                                   │
                    ReLU                                ReLU
                     │                                   │
                  Keluaran                            Keluaran
```

### Penyelarasan Dimensi Spasial dan Saluran
Penjumlahan $y = F(x) + x$ mensyaratkan dimensi spasial dan jumlah saluran $F(x)$ and $x$ sama persis. Namun, resolusi spasial sering kali dikurangi setengahnya (lewat *stride* = 2) sedangkan jumlah saluran dilipatgandakan. Untuk mengatasi ketidakcocokan ini, dirumuskan tiga opsi koneksi jalan pintas:
- **Opsi A (*Zero-Padding*)**: Menggunakan pengisian nol (*zero-padding*) untuk meningkatkan dimensi saluran tanpa parameter latih baru, serta pencocokan resolusi spasial menggunakan *stride*.
- **Opsi B (Proyeksi Parameter Parsial)**: Menggunakan konvolusi proyeksi $1\times1$ hanya saat dimensi berubah, sedangkan blok dengan dimensi tetap menggunakan jalan pintas identitas murni.
- **Opsi C (Proyeksi Parameter Penuh)**: Menggunakan konvolusi proyeksi $1\times1$ untuk seluruh jalan pintas di jaringan. Opsi C memberikan hasil terbaik secara marjinal namun menambah beban parameter, sehingga opsi B dipilih sebagai kompromi terbaik.

### Normalisasi Batch dan Skema Pelatihan
Stabilitas pelatihan pada kedalaman ekstrem dijamin dengan menerapkan normalisasi *batch* segera setelah konvolusi dan sebelum aktivasi ReLU. Optimasi menggunakan penurunan gradien stokastik (*stochastic gradient descent* atau SGD) dengan ukuran *batch* 256. Laju pembelajaran awal diatur 0,1 dan diturunkan dengan faktor 10 setiap galat mengalami saturasi. Inisialisasi bobot menerapkan metode He (*He initialization*). Model dilatih dengan peluruhan bobot (*weight decay*) 0,0001 dan momentum 0,9.

## Eksperimen dan Hasil

Evaluasi kinerja dilakukan pada dataset ImageNet 2012 yang mencakup tugas klasifikasi dengan 1.000 kelas. Perbandingan kuantitatif dilakukan antara jaringan polos (*plain*) dan jaringan residual (ResNet) pada varian 18 dan 34 lapisan.

Hasil evaluasi *10-crop* pada set validasi menunjukkan:
- **Plain-18 vs ResNet-18**: Jaringan polos mencapai *top-1 error* 27,94%, sedangkan ResNet-18 mencapai 27,88%. Pada kedalaman dangkal ini, akurasi keduanya sebanding, tetapi ResNet-18 mengalami konvergensi awal yang jauh lebih cepat.
- **Plain-34 vs ResNet-34**: Versi polos menunjukkan degradasi dengan galat naik menjadi 28,54%. Sebaliknya, ResNet-34 berhasil membalikkan tren degradasi dengan menekan galat menjadi 25,03% (penurunan galat sebesar 3,51%).

Evaluasi model yang lebih dalam dengan blok *bottleneck* pada set validasi ImageNet menunjukkan:
- **ResNet-50**: *Top-1 error* 22,85%, *top-5 error* 6,71%.
- **ResNet-101**: *Top-1 error* 21,75%, *top-5 error* 6,05%.
- **ResNet-152**: *Top-1 error* 21,43%, *top-5 error* 5,71%.

Pada pengujian model tunggal (*single-model*), ResNet-152 mencapai *top-5 error* 4,49% melalui evaluasi multi-skala. Ansambel model ResNet memenangi ILSVRC 2015 dengan *top-5 error* 3,57% pada set pengujian. Pada dataset MS COCO, ResNet sebagai tulang punggung deteksi objek meningkatkan nilai *mean Average Precision* (mAP) sebesar 28% secara relatif dibanding model berbasis VGG.

## Kelebihan dan Keterbatasan

- **Kelebihan**: Keunggulan utama ResNet adalah pemecahan masalah degradasi akurasi, sehingga memungkinkan pelatihan jaringan hingga ratusan lapisan. Secara teoretis, penjumlahan jalan pintas menjamin aliran gradien langsung tanpa reduksi eksponensial. Penggunaan blok *bottleneck* memberikan efisiensi komputasi tinggi; FLOPs ResNet-152 lebih rendah dibanding VGG-16/19 yang jauh lebih dangkal. ResNet juga memiliki kemampuan generalisasi tinggi, menjadikannya tulang punggung transfer pembelajaran (*transfer learning*) standar untuk tugas penalaan halus.
- **Keterbatasan**: Dari sisi rekayasa, kebutuhan memori aktivasi (*activation memory*) saat pelatihan meningkat secara linear sesuai kedalaman lapisan, membatasi ukuran *batch* pada perangkat keras dengan memori terbatas. Secara konseptual, terdapat redundansi representasi (*representation redundancy*) pada model yang sangat dalam, di mana banyak lapisan hanya mempelajari perubahan fitur kecil tanpa kontribusi representasi baru. Terakhir, model ini dirancang untuk data unimodal (RGB), sehingga memerlukan modul fusi eksternal untuk digabungkan dengan sensor lain (seperti sensor kedalaman).

## Kaitan dengan Bab Lain

Sebagai salah satu karya paling berpengaruh dalam sejarah pembelajaran mendalam, ResNet meletakkan dasar arsitektur yang diwarisi oleh hampir semua model visi modern, khususnya dalam klaster **Fusi Multimodal** (bab 148-154) dan klaster YOLO lainnya.

Hubungan konseptual dan implementatif ResNet dengan bab-bab terkait meliputi:
- **[148 - PointNet](./148%20-%202017%20-%20PointNet%20-%20Fusi%20Multimodal.md)**: Memperkenalkan pemrosesan awan titik (*point cloud*) 3D langsung. Pada sistem fusi multimodal 2D-3D, ResNet mengekstrak fitur visual RGB (2D), sedangkan PointNet mengekstrak fitur geometris 3D, sebelum keduanya dilebur dalam ruang laten bersama.
- **[149 - CBAM](./149%20-%202018%20-%20CBAM%20-%20Fusi%20Multimodal.md)**: Modul perhatian (*attention module*) yang disisipkan ke dalam blok residual ResNet sebelum penjumlahan jalan pintas untuk memperkaya fitur melalui pembobotan saluran dan spasial dinamis.
- **[150 - Survei Deteksi & Segmentasi Multimodal (Feng dkk.)](./150%20-%202021%20-%20Survei%20Deteksi%20%26%20Segmentasi%20Multimodal%20%28Feng%20dkk.%29%20-%20Fusi%20Multimodal.md)**: Menyebutkan ResNet sebagai *standard baseline backbone* yang dominan untuk mengekstrak fitur visual pada arsitektur fusi awal (*early fusion*), akhir (*late fusion*), maupun mendalam (*deep fusion*).
- **[151 - Object Detection in 20 Years (Zou dkk.)](./151%20-%202023%20-%20Object%20Detection%20in%2020%20Years%20%28Zou%20dkk.%29%20-%20Fusi%20Multimodal.md)**: Memetakan evolusi deteksi objek dari metode konvensional ke pembelajaran mendalam, di mana koneksi residual ResNet menjadi pilar utama yang menggantikan dominasi VGG pada detektor modern seperti Faster R-CNN dan menginspirasi arsitektur DarkNet pada YOLOv3.
- **[152 - Deep Multimodal Learning A Survey (Ramachandram & Taylor)](./152%20-%202017%20-%20Deep%20Multimodal%20Learning%20A%20Survey%20%28Ramachandram%20%26%20Taylor%29%20-%20Fusi%20Multimodal.md)**: Menyediakan fondasi teori penggabungan representasi lintas modal. ResNet di sini berfungsi sebagai pilar penting untuk ekstraksi fitur citra representasional (modalitas visual) sebelum dipadukan dengan modalitas suara atau teks.
- **[153 - Survei RGB-D SOD (Zhou dkk.)](./153%20-%202021%20-%20Survei%20RGB-D%20SOD%20%28Zhou%20dkk.%29%20-%20Fusi%20Multimodal.md)**: Mengulas deteksi objek menonjol berbasis RGB-D, di mana arsitektur berbasis ResNet sering kali diduplikasi menjadi struktur dua aliran (*two-stream architecture*) untuk mengekstrak fitur spasial multi-level baik dari aliran warna (RGB) maupun kedalaman (depth).
- **[154 - Survei Dataset RGB-D (Lopes dkk.)](./154%20-%202022%20-%20Survei%20Dataset%20RGB-D%20%28Lopes%20dkk.%29%20-%20Fusi%20Multimodal.md)**: Mengkatalogkan dataset RGB-D yang sering digunakan untuk mengevaluasi model fusi berbasis ResNet pada domain pengenalan adegan.

## Poin untuk Sitasi

Kunci BibTeX untuk sitasi formal adalah `he2016resnet`. Ringkasan deskriptif yang aman dikutip:
"ResNet memperkenalkan kerangka kerja pembelajaran residual menggunakan koneksi jalan pintas (*skip connection*) untuk mengatasi masalah degradasi akurasi pada jaringan sangat dalam. Pendekatan ini memungkinkan pelatihan model hingga kedalaman 152 lapisan pada ImageNet, menghasilkan tingkat kesalahan *top-5* sebesar 3,57% dan memenangi kompetisi ILSVRC serta COCO 2015."
Catatan verifikasi data: Angka kesalahan validasi 25,03% (ResNet-34) dan 21,43% (ResNet-152) diperoleh menggunakan pengujian *10-crop* pada set validasi ImageNet 2012, sedangkan nilai kesalahan ansambel 3,57% diperoleh pada set pengujian ImageNet. Pengguna disarankan memverifikasi jenis evaluasi (single-crop vs multi-crop) saat membandingkan metrik secara formal.
