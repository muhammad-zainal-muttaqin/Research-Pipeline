# 148 - PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation

## Metadata Ringkas
| Atribut | Nilai |
| --- | --- |
| Kunci BibTeX | `qi2017pointnet` |
| Judul asli | PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation |
| Penulis | Qi, Charles R.; Su, Hao; Mo, Kaichun; Guibas, Leonidas J. |
| Tahun | 2017 |
| Venue | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema | Fusi Multimodal |

## Tautan Akses
*   **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=PointNet%3A%20Deep%20Learning%20on%20Point%20Sets%20for%203D%20Classification%20and%20Segmentation
*   **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=PointNet%3A%20Deep%20Learning%20on%20Point%20Sets%20for%203D%20Classification%20and%20Segmentation&sort=relevance
*   **ArXiv (PDF gratis):** https://arxiv.org/abs/1612.00593

## Gambaran Umum
PointNet memperkenalkan arsitektur jaringan saraf dalam perintis yang dirancang untuk memproses *point cloud* (himpunan titik 3D) mentah secara langsung tanpa transformasi perantara seperti voxelisasi atau proyeksi gambar multi-sudut (*multi-view*). Pendekatan ini mengatasi sifat data *point cloud* yang tidak terstruktur, tidak terurut (permutasi bebas), dan sensitif terhadap rotasi atau translasi. Dengan menerapkan *multi-layer perceptron* (MLP) independen per titik dan operasi penimbunan maksimum (*max pooling*) sebagai fungsi simetris, PointNet mengekstrak fitur global yang invarian terhadap urutan input.

Eksperimen pada ModelNet40 menghasilkan akurasi keseluruhan sebesar 89,2%, menyamai kinerja metode berbasis voxel dengan efisiensi komputasi yang jauh lebih tinggi. Pada segmentasi bagian ShapeNet, model ini memperoleh *instance* mean Intersection over Union (mIoU) sebesar 83,7% dan *class* mIoU sebesar 80,4%. Sebagai komponen *backbone* geometris dasar, PointNet berperan penting dalam sistem fusi multimodal modern untuk mengintegrasikan citra RGB dan geometri kedalaman.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sebelum PointNet, jaringan saraf konvensional kesulitan memproses data 3D secara langsung. Citra 2D memiliki struktur grid teratur yang memudahkan penerapan operasi konvolusi. Sebaliknya, *point cloud* dari sensor LiDAR atau kamera RGB-D merupakan himpunan titik tak teratur dengan koordinat $(x, y, z)$. Ketiadaan urutan indeks membuat urutan titik bersifat bebas, sehingga model harus menghasilkan keluaran yang sama terlepas dari permutasi input (invariansi permutasi).

Pendekatan terdahulu umumnya mengonversi *point cloud* menjadi representasi lain:
1. **Voxelisasi:** Mengonversi data ke grid voxel 3D teratur. Pendekatan ini terhambat oleh kebutuhan komputasi dan memori yang sangat besar karena tumbuh secara kubik terhadap resolusi. Akibatnya, resolusi grid sering dibatasi, yang memicu hilangnya detail geometris akibat efek kuantisasi (*quantization artifacts*).
2. **Proyeksi Multi-View:** Merender objek 3D menjadi kumpulan citra 2D dari berbagai sudut pandang, lalu memprosesnya dengan 2D CNN. Meskipun memberikan akurasi klasifikasi yang tinggi, metode ini sulit diperluas ke tugas prediksi per titik seperti segmentasi bagian atau pemahaman adegan yang kompleks.

Selain masalah representasi, representasi 3D harus tangguh terhadap transformasi kaku (*rigid transformation*) seperti rotasi dan translasi. Rotasi mengubah nilai koordinat secara drastis, tetapi makna semantik objek tetap sama. Penanganan transformasi ini secara manual melalui augmentasi data tidak menjamin invariansi yang kuat. Oleh karena itu, diperlukan metode pemrosesan langsung yang secara matematis mempertahankan invariansi permutasi dan transformasi spasial.

## Ide Utama
Ide utama PointNet adalah memproses koordinat *point cloud* secara independen pada tahap awal menggunakan MLP bersama per titik, lalu mengagregasi fitur-fiturnya menggunakan fungsi simetris. Secara matematis, untuk himpunan titik $S = \{x_1, \dots, x_n\}$ dengan $x_i \in \mathbb{R}^3$, PointNet memodelkan fungsi set kontinu $f(S)$ melalui:

$$f(S) \approx g(h(x_1), \dots, h(x_n))$$

Di mana $h$ adalah fungsi pemetaan fitur non-linear (MLP bersama) yang memetakan koordinat ke fitur berdimensi tinggi ($K$), dan $g$ adalah fungsi simetris (operasi *max pooling*) untuk mereduksi matriks fitur berdimensi $N \times K$ menjadi vektor representasi global berdimensi $1 \times K$. Untuk menjamin invariansi transformasi spasial, PointNet mengintegrasikan **T-Net**, yaitu jaringan mini yang memprediksi matriks transformasi secara dinamis dari fitur input untuk menyejajarkan titik ke ruang referensi kanonis.

## Cara Kerja Langkah demi Langkah
Aliran data PointNet memproses koordinat $N$ titik dengan format awal $N \times 3$ menjadi prediksi klasifikasi tingkat objek atau segmentasi tingkat titik. Struktur diagram berikut menggambarkan detail arsitekturnya:

```
                  ┌──────────────────────────────┐
                  │    Input Point Cloud (N x 3) │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                         ┌──────────────┐
                         │ T-Net (3x3)  │
                         └───────┬──────┘
                                 │ (Matriks 3x3)
                                 ▼
                         ┌──────────────┐
                         │ Transformasi │◄── Kalikan koordinat
                         └───────┬──────┘
                                 │ (N x 3)
                                 ▼
                        ┌────────────────┐
                        │ MLP (64, 64)   │
                        └───────┬────────┘
                                 │ (N x 64)
                                 ▼
                         ┌──────────────┐
                         │ T-Net (64x64)│
                         └───────┬──────┘
                                 │ (Matriks 64x64)
                                 ▼
                         ┌──────────────┐
                         │ Transformasi │◄── Kalikan fitur
                         └───────┬──────┘
                                 │ (N x 64) ────┐ (Simpan untuk segmentasi)
                                 ▼              │
                      ┌─────────────────────┐   │
                      │ MLP (64, 128, 1024) │   │
                      └──────────┬──────────┘   │
                                 │ (N x 1024)   │
                                 ▼              │
                        ┌────────────────┐      │
                        │ Max Pooling    │      │
                        └───────┬────────┘      │
                                 │ (1 x 1024)   │
                                 ├──────────────┼──────────────┐
                                 │              │              │
              (Jalur Klasifikasi)│              │(Jalur Segmentasi)
                                 ▼              │              ▼
                         ┌──────────────┐       │      ┌───────────────┐
                         │ MLP (512,256)│       │      │ Duplikasi     │
                         └───────┬──────┘       │      │  (N x 1024)   │
                                 │ (256)        │      └───────┬───────┘
                                 ▼              │              │
                         ┌──────────────┐       │              ▼
                         │ FC (k)       │       │      ┌───────────────┐
                         └───────┬──────┘       │      │  Konkatenasi  │◄───┘
                                 │          ┌───┘      │  (N x 1088)   │
                                 ▼          │          └───────┬───────┘
                           [ k Kelas ]      │                  │
                                            │                  ▼
                                            │         ┌────────────────┐
                                            │         │ MLP (512, 256) │
                                            │         └────────┬───────┘
                                            │                  │ (N x 256)
                                            │                  ▼
                                            │         ┌────────────────┐
                                            │         │ MLP (128, m)   │
                                            │         └────────┬───────┘
                                            │                  │
                                            │                  ▼
                                            └────────────► [ N x m Skor ]
```

### Jaringan Penjajaran Spasial (T-Net)
Langkah awal PointNet adalah menyelaraskan koordinat input ke orientasi yang seragam. Jaringan mini **T-Net** memprediksi matriks transformasi afinitas 3D ($3 \times 3$) dari koordinat input $N \times 3$. T-Net terdiri dari MLP bersama per titik (dengan dimensions output 64, 128, 1024), diikuti operasi *max pooling* untuk mengekstrak fitur global, dan beberapa lapisan terhubung penuh (*fully connected*) yang menghasilkan matriks $3 \times 3$. Matriks ini dikalikan langsung dengan koordinat input $N \times 3$ untuk menyejajarkan titik ke ruang referensi kanonis.

Proses serupa diterapkan pada ruang fitur menengah berdimensi 64 menggunakan T-Net kedua untuk memprediksi matriks transformasi fitur $64 \times 64$. Karena dimensi matriks fitur ini besar ($64 \times 64 = 4096$ parameter), optimasi distabilkan dengan menambahkan suku regularisasi ortogonalitas pada fungsi kerugian (*loss function*):

$$L_{reg} = \|I - A A^T\|_F^2$$

Di mana $I$ melambangkan matriks identitas dan $A$ adalah matriks transformasi fitur. Suku ini memastikan tidak ada informasi geometris yang hilang selama transformasi.

### Ekstraksi Fitur dan Operasi Pooling Simetris
Setelah penjajaran fitur pertama, matriks fitur $N \times 64$ diproses melalui MLP bersama dengan filter berdimensi 64, 128, dan 1024 secara independen pada setiap titik. Operasi ini mengubah dimensi tensor menjadi $N \times 1024$, yang mewakili fitur geometris lokal setiap titik.

Untuk mereduksi matriks fitur tersebut menjadi representasi global yang invarian terhadap urutan input, PointNet menerapkan operasi *max pooling* elemen-demi-elemen pada dimensi jumlah titik ($N$). Hasil akhirnya adalah vektor fitur global berdimensi $1 \times 1024$. Untuk setiap kanal fitur ke-$j$, nilai global diambil dari nilai maksimum dari semua $N$ titik:

$$g_j = \max(h_{1, j}, \dots, h_{N, j})$$

Operasi ini memastikan representasi fitur global tetap sama meskipun urutan titik diubah.

### Penggabungan Fitur Lokal-Global untuk Segmentasi
Untuk tugas klasifikasi, fitur global $1 \times 1024$ diproses oleh MLP akhir (berukuran 512 dan 256) dengan *dropout* (rasio 0,3) untuk mencegah *overfitting*, dan diakhiri dengan lapisan linear untuk memprediksi skor probabilitas $k$ kelas objek.

Untuk tugas segmentasi bagian objek atau segmentasi semantik pemandangan, keputusan harus diambil pada tingkat titik individual (*per-point*). Hal ini memerlukan perpaduan antara fitur geometris lokal titik dan fitur semantik global objek. PointNet menyalin fitur global $1 \times 1024$ sebanyak $N$ kali menjadi matriks $N \times 1024$, lalu menggabungkannya (*concatenate*) secara spasial dengan fitur lokal $N \times 64$ (diperoleh setelah transformasi fitur tahap awal) menjadi matriks fitur hibrida berdimensi $N \times 1088$. Matriks ini diproses oleh MLP per titik (ukuran filter 512, 256, 128) dan diakhiri dengan proyeksi linear untuk memprediksi skor dari $m$ kelas segmentasi pada setiap titik.

## Eksperimen dan Hasil
PointNet diuji pada tiga benchmark utama: klasifikasi 3D (ModelNet40), segmentasi bagian objek (ShapeNet), dan segmentasi semantik pemandangan (S3DIS).

Tabel 1: Perbandingan Performa Klasifikasi 3D pada ModelNet40
| Metode | Representasi Input | Akurasi Kelas Rata-rata (%) | Akurasi Keseluruhan (%) |
| :--- | :--- | :---: | :---: |
| 3DShapeNets (Wu dkk.) | Voxel ($30^3$) | 77,3 | 84,7 |
| VoxNet (Maturana & Scherer) | Voxel ($32^3$) | 83,0 | 85,9 |
| Subvolume (Qi dkk.) | Voxel ($32^3$) | 86,0 | 89,2 |
| MVCNN (Su dkk.) | Citra Multi-View | **90,1** | **90,1** |
| **PointNet (Ours)** | **Point Cloud** | **86,2** | **89,2** |

Tabel 2: Perbandingan Performa Segmentasi Bagian pada ShapeNet (mIoU %)
| Metode | Instance mIoU (%) | Class mIoU (%) |
| :--- | :---: | :---: |
| Yi dkk. | 81,4 | 80,4 |
| Loop-Reg (Psar dkk.) | 82,8 | - |
| 3D CNN Baseline | 79,4 | 77,8 |
| **PointNet (Ours)** | **83,7** | **80,4** |

Pada ModelNet40 (Tabel 1), PointNet mencapai akurasi keseluruhan sebesar 89,2%, menyamai kinerja metode berbasis voxel (Subvolume) dengan efisiensi komputasi yang jauh lebih tinggi. MVCNN yang berbasis citra 2D multi-view memimpin dengan akurasi 90,1% karena mampu mengeksrak fitur tekstur halus, namun sulit diterapkan pada klasifikasi tingkat titik.

Pada ShapeNet (Tabel 2), PointNet mencatat *instance* mIoU sebesar 83,7% dan *class* mIoU sebesar 80,4%. Kinerja ini mengungguli baseline 3D CNN (79,4%) sebesar 4,3%. Pada S3DIS, PointNet mencapai mIoU 47,6% melalui validasi silang 6 area (*6-fold cross validation*). Uji ketahanan menunjukkan bahwa ketika 50% titik dibuang, akurasi hanya menurun sebesar 2,4% (jika menggunakan *furthest point sampling*) dan 3,8% (jika menggunakan pengambilan acak). PointNet mampu memproses 1 juta titik per detik pada GPU NVIDIA GTX 1080 (TensorFlow), menunjukkan potensi implementasi waktu nyata (*real-time*).

## Kelebihan dan Keterbatasan
Kelebihan utama PointNet adalah kemampuan memproses data *point cloud* mentah secara langsung dengan kompleksitas ruang dan waktu linear $O(N)$ terhadap jumlah titik. Skalabilitas ini jauh lebih baik dibanding 3D CNN berbasis voxel yang tumbuh secara kubik. Penggunaan *max pooling* secara matematis menjamin invariansi permutasi titik. Selain itu, visualisasi *critical point set* membuktikan ketangguhan model terhadap hilangnya sebagian data atau adanya pencilan (*outliers*).

Keterbatasan utama PointNet adalah ketiadaan pemrosesan fitur lokal yang bersifat hierarkis. Karena MLP bekerja secara independen pada setiap titik sebelum diintegrasikan secara global, model ini tidak mampu menangkap hubungan spasial atau informasi geometri antara titik-titik bertetangga dalam jarak dekat (*local neighborhood*). Hal ini membatasi kemampuannya dalam memahami hubungan spasial pada pemandangan berskala besar atau membedakan detail geometris halus. Selain itu, ketergantungan pada koordinat absolut $(x, y, z)$ membuat model sensitif terhadap perubahan skala dan translasi global jika data input tidak dinormalisasi dengan ketat.

## Kaitan dengan Bab Lain
PointNet merupakan komponen fundamental dalam klaster fusi multimodal untuk memproses data kedalaman 3D secara langsung. Model ini bertindak sebagai ekstraktor fitur geometris 3D yang melengkapi ekstraktor fitur visual 2D berbasis CNN seperti [ResNet (Bab 147)](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md) pada arsitektur hibrida.

Penggabungan fitur lintas modalitas RGB dan 3D dibahas dalam studi tinjauan [Deep Multimodal Learning A Survey (Bab 152)](./152%20-%202017%20-%20Deep%20Multimodal%20Learning%20A%20Survey%20%28Ramachandram%20%26%20Taylor%29%20-%20Fusi%20Multimodal.md) melalui konsep representasi bersama (*joint representation*). Selain itu, [Survei Deteksi & Segmentasi Multimodal (Bab 150)](./150%20-%202021%20-%20Survei%20Deteksi%20%26%20Segmentasi%20Multimodal%20%28Feng%20dkk.%29%20-%20Fusi%20Multimodal.md) mendokumentasikan peran PointNet sebagai *backbone* geometris untuk menghasilkan proposal wilayah 3D pada sistem fusi awal (*early fusion*) maupun fusi lanjut (*late fusion*). Perkembangan ini juga diulas secara historis dalam [Object Detection in 20 Years (Bab 151)](./151%20-%202023%20-%20Object%20Detection%20in%2020%20Years%20%28Zou%20dkk.%29%20-%20Fusi%20Multimodal.md).

Untuk mengintegrasikan representasi fitur PointNet dan ResNet secara dinamis, mekanisme atensi seperti [CBAM (Bab 149)](./149%20-%202018%20-%20CBAM%20-%20Fusi%20Multimodal.md) dapat diterapkan untuk menimbang fitur spasial dan kanal. Konsep fusi geometri dan warna ini juga mendasari pencarian objek berbasis kedalaman dalam [Survei RGB-D SOD (Bab 153)](./153%20-%202021%20-%20Survei%20RGB-D%20SOD%20%28Zhou%20dkk.%29%20-%20Fusi%20Multimodal.md) dan pengelolaan data spasial yang diulas pada [Survei Dataset RGB-D (Bab 154)](./154%20-%202022%20-%20Survei%20Dataset%20RGB-D%20%28Lopes%20dkk.%29%20-%20Fusi%20Multimodal.md).

## Poin untuk Sitasi
Kunci BibTeX: `qi2017pointnet`

Ringkasan sitasi:
PointNet memperkenalkan arsitektur jaringan saraf dalam pertama yang memproses data *point cloud* mentah secara langsung dengan mempertahankan invariansi permutasi melalui operasi *symmetric pooling*. Model ini menjadi fondasi utama dalam ekstraksi fitur geometris 3D yang sangat efisien untuk tugas klasifikasi, segmentasi bagian, dan deteksi objek 3D.

Catatan verifikasi:
- Nilai akurasi klasifikasi keseluruhan sebesar 89,2% dan akurasi kelas rata-rata sebesar 86,2% diperoleh pada dataset ModelNet40 dengan koordinat input $(x, y, z)$ tanpa fitur normal.
- Performa segmentasi bagian pada ShapeNet menghasilkan *instance* mIoU 83,7% dan *class* mIoU 80,4%.
- Kompleksitas waktu dan ruang linear $O(N)$ terbukti secara teoretis dan empiris dengan kecepatan pemrosesan 1 juta titik per detik menggunakan GPU NVIDIA GTX 1080 pada kerangka kerja TensorFlow.
