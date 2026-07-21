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

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract

Point cloud is an important type of geometric data structure. Due to its irregular format, most researchers transform such data to regular 3D voxel grids or collections of images. This, however, renders data unnecessarily voluminous and causes issues. In this paper, we design a novel type of neural network that directly consumes point clouds, which well respects the permutation invariance of points in the input. Our network, named PointNet, provides a unified architecture for applications ranging from object classification, part segmentation, to scene semantic parsing. Though simple, PointNet is highly efficient and effective. Empirically, it shows strong performance on par or even better than state of the art. Theoretically, we provide analysis towards understanding of what the network has learnt and why the network is robust with respect to input perturbation and corruption.

Figure 1. Applications of PointNet. We propose a novel deep net architecture that consumes raw point cloud (set of points) without voxelization or rendering. It is a unified architecture that learns both global and local point features, providing a simple, efficient and effective approach for a number of 3D recognition tasks.

still has to respect the fact that a point cloud is just a set of points and therefore invariant to permutations of its members, necessitating certain symmetrizations in the net computation. Further invariances to rigid motions also need to be considered. Our PointNet is a unified architecture that directly takes point clouds as input and outputs either class labels for the entire input or per point segment/part labels for each point of the input. The basic architecture of our network is surprisingly simple as in the initial stages each point is processed identically and independently. In the basic setting each point is represented by just its three coordinates (x, y, z). Additional dimensions may be added by computing normals and other local or global features. Key to our approach is the use of a single symmetric function, max pooling. Effectively the network learns a set of optimization functions/criteria that select interesting or informative points of the point cloud and encode the reason for their selection. The final fully connected layers of the network aggregate these learnt optimal values into the global descriptor for the entire shape as mentioned above (shape classification) or are used to predict per point labels (shape segmentation). Our input format is easy to apply rigid or affine transformations to, as each point transforms independently. Thus we can add a data-dependent spatial transformer network that attempts to canonicalize the data before the PointNet processes them, so as to further improve the results.

1. Introduction In this paper we explore deep learning architectures capable of reasoning about 3D geometric data such as point clouds or meshes. Typical convolutional architectures require highly regular input data formats, like those of image grids or 3D voxels, in order to perform weight sharing and other kernel optimizations. Since point clouds or meshes are not in a regular format, most researchers typically transform such data to regular 3D voxel grids or collections of images (e.g, views) before feeding them to a deep net architecture. This data representation transformation, however, renders the resulting data unnecessarily voluminous — while also introducing quantization artifacts that can obscure natural invariances of the data. For this reason we focus on a different input representation for 3D geometry using simply point clouds – and name our resulting deep nets PointNets. Point clouds are simple and unified structures that avoid the combinatorial irregularities and complexities of meshes, and thus are easier to learn from. The PointNet, however, * indicates equal contributions.

We provide both a theoretical analysis and an experimental evaluation of our approach. We show that our network can approximate any set function that is continuous. More interestingly, it turns out that our network learns to summarize an input point cloud by a sparse set of key points, which roughly corresponds to the skeleton of objects according to visualization. The theoretical analysis provides an understanding why our PointNet is highly robust to small perturbation of input points as well as to corruption through point insertion (outliers) or deletion (missing data). On a number of benchmark datasets ranging from shape classification, part segmentation to scene segmentation, we experimentally compare our PointNet with state-ofthe-art approaches based upon multi-view and volumetric representations. Under a unified architecture, not only is our PointNet much faster in speed, but it also exhibits strong performance on par or even better than state of the art. The key contributions of our work are as follows: • We design a novel deep net architecture suitable for consuming unordered point sets in 3D; • We show how such a net can be trained to perform 3D shape classification, shape part segmentation and scene semantic parsing tasks; • We provide thorough empirical and theoretical analysis on the stability and efficiency of our method; • We illustrate the 3D features computed by the selected neurons in the net and develop intuitive explanations for its performance. The problem of processing unordered sets by neural nets is a very general and fundamental problem – we expect that our ideas can be transferred to other domains as well.

2. Related Work

their operations are still on sparse volumes, it’s challenging for them to process very large point clouds. Multiview CNNs: [23, 18] have tried to render 3D point cloud or shapes into 2D images and then apply 2D conv nets to classify them. With well engineered image CNNs, this line of methods have achieved dominating performance on shape classification and retrieval tasks [21]. However, it’s nontrivial to extend them to scene understanding or other 3D tasks such as point classification and shape completion. Spectral CNNs: Some latest works [4, 16] use spectral CNNs on meshes. However, these methods are currently constrained on manifold meshes such as organic objects and it’s not obvious how to extend them to non-isometric shapes such as furniture. Feature-based DNNs: [6, 8] firstly convert the 3D data into a vector, by extracting traditional shape features and then use a fully connected net to classify the shape. We think they are constrained by the representation power of the features extracted.

Deep Learning on Unordered Sets From a data structure point of view, a point cloud is an unordered set of vectors. While most works in deep learning focus on regular input representations like sequences (in speech and language processing), images and volumes (video or 3D data), not much work has been done in deep learning on point sets. One recent work from Oriol Vinyals et al [25] looks into this problem. They use a read-process-write network with attention mechanism to consume unordered input sets and show that their network has the ability to sort numbers. However, since their work focuses on generic sets and NLP applications, there lacks the role of geometry in the sets.

3. Problem Statement

Point Cloud Features Most existing features for point cloud are handcrafted towards specific tasks. Point features often encode certain statistical properties of points and are designed to be invariant to certain transformations, which are typically classified as intrinsic [2, 24, 3] or extrinsic [20, 19, 14, 10, 5]. They can also be categorized as local features and global features. For a specific task, it is not trivial to find the optimal feature combination.

We design a deep learning framework that directly consumes unordered point sets as inputs. A point cloud is represented as a set of 3D points {Pi | i = 1, ..., n}, where each point Pi is a vector of its (x, y, z) coordinate plus extra feature channels such as color, normal etc. For simplicity and clarity, unless otherwise noted, we only use the (x, y, z) coordinate as our point’s channels.

Deep Learning on 3D Data 3D data has multiple popular representations, leading to various approaches for learning. Volumetric CNNs: [28, 17, 18] are the pioneers applying 3D convolutional neural networks on voxelized shapes. However, volumetric representation is constrained by its resolution due to data sparsity and computation cost of 3D convolution. FPNN [13] and Vote3D [26] proposed special methods to deal with the sparsity problem; however,

For the object classification task, the input point cloud is either directly sampled from a shape or pre-segmented from a scene point cloud. Our proposed deep network outputs k scores for all the k candidate classes. For semantic segmentation, the input can be a single object for part region segmentation, or a sub-volume from a 3D scene for object region segmentation. Our model will output n × m scores for each of the n points and each of the m semantic subcategories.

Figure 2. PointNet Architecture. The classification network takes n points as input, applies input and feature transformations, and then aggregates point features by max pooling. The output is classification scores for k classes. The segmentation network is an extension to the classification net. It concatenates global and local features and outputs per point scores. “mlp” stands for multi-layer perceptron, numbers in bracket are layer sizes. Batchnorm is used for all layers with ReLU. Dropout layers are used for the last mlp in classification net.

4.1. Properties of Point Sets in Rn Our input is a subset of points from an Euclidean space. It has three main properties: • Unordered. Unlike pixel arrays in images or voxel arrays in volumetric grids, point cloud is a set of points without specific order. In other words, a network that consumes N 3D point sets needs to be invariant to N ! permutations of the input set in data feeding order. • Interaction among points. The points are from a space with a distance metric. It means that points are not isolated, and neighboring points form a meaningful subset. Therefore, the model needs to be able to capture local structures from nearby points, and the combinatorial interactions among local structures. • Invariance under transformations. As a geometric object, the learned representation of the point set should be invariant to certain transformations. For example, rotating and translating points all together should not modify the global point cloud category nor the segmentation of the points.

4.2. PointNet Architecture Our full network architecture is visualized in Fig 2, where the classification network and the segmentation network share a great portion of structures. Please read the caption of Fig 2 for the pipeline. Our network has three key modules: the max pooling layer as a symmetric function to aggregate information from

all the points, a local and global information combination structure, and two joint alignment networks that align both input points and point features. We will discuss our reason behind these design choices in separate paragraphs below. Symmetry Function for Unordered Input In order to make a model invariant to input permutation, three strategies exist: 1) sort input into a canonical order; 2) treat the input as a sequence to train an RNN, but augment the training data by all kinds of permutations; 3) use a simple symmetric function to aggregate the information from each point. Here, a symmetric function takes n vectors as input and outputs a new vector that is invariant to the input order. For example, + and ∗ operators are symmetric binary functions. While sorting sounds like a simple solution, in high dimensional space there in fact does not exist an ordering that is stable w.r.t. point perturbations in the general sense. This can be easily shown by contradiction. If such an ordering strategy exists, it defines a bijection map between a high-dimensional space and a 1d real line. It is not hard to see, to require an ordering to be stable w.r.t point perturbations is equivalent to requiring that this map preserves spatial proximity as the dimension reduces, a task that cannot be achieved in the general case. Therefore, sorting does not fully resolve the ordering issue, and it’s hard for a network to learn a consistent mapping from input to output as the ordering issue persists. As shown in experiments (Fig 5), we find that applying a MLP directly on the sorted point set performs poorly, though slightly better than directly processing an unsorted input. The idea to use RNN considers the point set as a sequential signal and hopes that by training the RNN

with randomly permuted sequences, the RNN will become invariant to input order. However in “OrderMatters” [25] the authors have shown that order does matter and cannot be totally omitted. While RNN has relatively good robustness to input ordering for sequences with small length (dozens), it’s hard to scale to thousands of input elements, which is the common size for point sets. Empirically, we have also shown that model based on RNN does not perform as well as our proposed method (Fig 5). Our idea is to approximate a general function defined on a point set by applying a symmetric function on transformed elements in the set: f ({x1 , . . . , xn }) ≈ g(h(x1 ), . . . , h(xn )),

Empirically, our basic module is very simple: we approximate h by a multi-layer perceptron network and g by a composition of a single variable function and a max pooling function. This is found to work well by experiments. Through a collection of h, we can learn a number of f ’s to capture different properties of the set. While our key module seems simple, it has interesting properties (see Sec 5.3) and can achieve strong performace (see Sec 5.1) in a few different applications. Due to the simplicity of our module, we are also able to provide theoretical analysis as in Sec 4.3. Local and Global Information Aggregation The output from the above section forms a vector [f1 , . . . , fK ], which is a global signature of the input set. We can easily train a SVM or multi-layer perceptron classifier on the shape global features for classification. However, point segmentation requires a combination of local and global knowledge. We can achieve this by a simple yet highly effective manner. Our solution can be seen in Fig 2 (Segmentation Network). After computing the global point cloud feature vector, we feed it back to per point features by concatenating the global feature with each of the point features. Then we extract new per point features based on the combined point features - this time the per point feature is aware of both the local and global information. With this modification our network is able to predict per point quantities that rely on both local geometry and global semantics. For example we can accurately predict per-point normals (fig in supplementary), validating that the network is able to summarize information from the point’s local neighborhood. In experiment session, we also show that our model can achieve state-of-the-art performance on shape part segmentation and scene segmentation.

Joint Alignment Network The semantic labeling of a point cloud has to be invariant if the point cloud undergoes certain geometric transformations, such as rigid transformation. We therefore expect that the learnt representation by our point set is invariant to these transformations. A natural solution is to align all input set to a canonical space before feature extraction. Jaderberg et al. [9] introduces the idea of spatial transformer to align 2D images through sampling and interpolation, achieved by a specifically tailored layer implemented on GPU. Our input form of point clouds allows us to achieve this goal in a much simpler way compared with [9]. We do not need to invent any new layers and no alias is introduced as in the image case. We predict an affine transformation matrix by a mini-network (T-net in Fig 2) and directly apply this transformation to the coordinates of input points. The mininetwork itself resembles the big network and is composed by basic modules of point independent feature extraction, max pooling and fully connected layers. More details about the T-net are in the supplementary. This idea can be further extended to the alignment of feature space, as well. We can insert another alignment network on point features and predict a feature transformation matrix to align features from different input point clouds. However, transformation matrix in the feature space has much higher dimension than the spatial transform matrix, which greatly increases the difficulty of optimization. We therefore add a regularization term to our softmax training loss. We constrain the feature transformation matrix to be close to orthogonal matrix: Lreg = kI − AAT k2F ,

where A is the feature alignment matrix predicted by a mini-network. An orthogonal transformation will not lose information in the input, thus is desired. We find that by adding the regularization term, the optimization becomes more stable and our model achieves better performance.

Figure 3. Qualitative results for part segmentation. We visualize the CAD part segmentation results across all 16 object categories. We show both results for partial simulated Kinect scans (left block) and complete ShapeNet CAD models (right block).

where x1 , . . . , xn is the full list of elements in S ordered arbitrarily, γ is a continuous function, and MAX is a vector max operator that takes n vectors as input and returns a new vector of the element-wise maximum. The proof to this theorem can be found in our supplementary material. The key idea is that in the worst case the network can learn to convert a point cloud into a volumetric representation, by partitioning the space into equal-sized voxels. In practice, however, the network learns a much smarter strategy to probe the space, as we shall see in point function visualizations. Bottleneck dimension and stability Theoretically and experimentally we find that the expressiveness of our network is strongly affected by the dimension of the max pooling layer, i.e., K in (1). Here we provide an analysis, which also reveals properties related to the stability of our model. We define u = MAX{h(xi )} to be the sub-network of f xi ∈S

5. Experiment Experiments are divided into four parts. First, we show PointNets can be applied to multiple 3D recognition tasks (Sec 5.1). Second, we provide detailed experiments to validate our network design (Sec 5.2). At last we visualize what the network learns (Sec 5.3) and analyze time and space complexity (Sec 5.4).

5.1. Applications In this section we show how our network can be trained to perform 3D object classification, object part segmentation and semantic scene segmentation 1 . Even though we are working on a brand new data representation (point sets), we are able to achieve comparable or even better performance on benchmarks for several tasks. 3D Object Classification Our network learns global point cloud feature that can be used for object classification. We evaluate our model on the ModelNet40 [28] shape classification benchmark. There are 12,311 CAD models from 40 man-made object categories, split into 9,843 for 1 More application examples such as correspondence and point cloud based CAD model retrieval are included in supplementary material.

per point class in each block. Each point is represented by a 9-dim vector of XYZ, RGB and normalized location as to the room (from 0 to 1). At training time, we randomly sample 4096 points in each block on-the-fly. At test time, we test on all the points. We follow the same protocol as [1] to use k-fold strategy for train and test. We compare our method with a baseline using handcrafted point features. The baseline extracts the same 9dim local features and three additional ones: local point density, local curvature and normal. We use standard MLP as the classifier. Results are shown in Table 3, where our PointNet method significantly outperforms the baseline method. In Fig 4, we show qualitative segmentation results. Our network is able to output smooth predictions and is robust to missing points and occlusions. Based on the semantic segmentation output from our network, we further build a 3D object detection system using connected component for object proposal (see supplementary for details). We compare with previous stateof-the-art method in Table 4. The previous method is based on a sliding shape method (with CRF post processing) with SVMs trained on local geometric features and global room context feature in voxel grids. Our method outperforms it by a large margin on the furniture categories reported.

Figure 4. Qualitative results for semantic segmentation. Top row is input point cloud with color. Bottom row is output semantic segmentation result (on points) displayed in the same camera viewpoint as input.

Figure 5. Three approaches to achieve order invariance. Multilayer perceptron (MLP) applied on points consists of 5 hidden layers with neuron sizes 64,64,64,128,1024, all points share a single copy of MLP. The MLP close to the output consists of two layers with sizes 512,256.

points as n×3 arrays, RNN model that considers input point as a sequence, and a model based on symmetry functions. The symmetry operation we experimented include max pooling, average pooling and an attention based weighted sum. The attention method is similar to that in [25], where a scalar score is predicted from each point feature, then the score is normalized across points by computing a softmax. The weighted sum is then computed on the normalized scores and the point features. As shown in Fig 5, maxpooling operation achieves the best performance by a large winning margin, which validates our choice. Effectiveness of Input and Feature Transformations In Table 5 we demonstrate the positive effects of our input and feature transformations (for alignment). It’s interesting to see that the most basic architecture already achieves quite reasonable results. Using input transformation gives a 0.8% performance boost. The regularization loss is necessary for the higher dimension transform to work. By combining both transformations and the regularization term, we achieve the best performance.

In this section we validate our design choices by control experiments. We also show the effects of our network’s hyperparameters.

Robustness Test We show our PointNet, while simple and effective, is robust to various kinds of input corruptions. We use the same architecture as in Fig 5’s max pooling network. Input points are normalized into a unit sphere. Results are in Fig 6. As to missing points, when there are 50% points missing, the accuracy only drops by 2.4% and 3.8% w.r.t. furthest and random input sampling. Our net is also robust to outlier

Comparison with Alternative Order-invariant Methods As mentioned in Sec 4.2, there are at least three options for consuming unordered set inputs. We use the ModelNet40 shape classification problem as a test bed for comparisons of those options, the following two control experiment will also use this task. The baselines (illustrated in Fig 5) we compared with include multi-layer perceptron on unsorted and sorted

5.2. Architecture Design Analysis

90 Accuracy (%)

5.4. Time and Space Complexity Analysis

Figure 6. PointNet robustness test. The metric is overall classification accuracy on ModelNet40 test set. Left: Delete points. Furthest means the original 1024 points are sampled with furthest sampling. Middle: Insertion. Outliers uniformly scattered in the unit sphere. Right: Perturbation. Add Gaussian noise to each point independently.

points, if it has seen those during training. We evaluate two models: one trained on points with (x, y, z) coordinates; the other on (x, y, z) plus point density. The net has more than 80% accuracy even when 20% of the points are outliers. Fig 6 right shows the net is robust to point perturbations.

5.3. Visualizing PointNet

In Fig 7, we visualize critical point sets CS and upperbound shapes NS (as discussed in Thm 2) for some sample shapes S. The point sets between the two shapes will give exactly the same global shape feature f (S). We can see clearly from Fig 7 that the critical point sets CS , those contributed to the max pooled feature, summarizes the skeleton of the shape. The upper-bound shapes NS illustrates the largest possible point cloud that give the same global shape feature f (S) as the input point cloud S. CS and NS reflect the robustness of PointNet, meaning that losing some non-critical points does not change the global shape signature f (S) at all. The NS is constructed by forwarding all the points in a edge-length-2 cube through the network and select points p whose point function values (h1 (p), h2 (p), · · · , hK (p)) are no larger than the global shape descriptor.

Figure 7. Critical points and upper bound shape. While critical points jointly determine the global shape feature for a given shape, any point cloud that falls between the critical points set and the upper bound shape gives exactly the same feature. We color-code all figures to show the depth information.

Table 6 summarizes space (number of parameters in the network) and time (floating-point operations/sample) complexity of our classification PointNet. We also compare PointNet to a representative set of volumetric and multiview based architectures in previous works. While MVCNN [23] and Subvolume (3D CNN) [18] achieve high performance, PointNet is orders more efficient in computational cost (measured in FLOPs/sample: 141x and 8x more efficient, respectively). Besides, PointNet is much more space efficient than MVCNN in terms of #param in the network (17x less parameters). Moreover, PointNet is much more scalable – it’s space and time complexity is O(N ) – linear in the number of input points. However, since convolution dominates computing time, multi-view method’s time complexity grows squarely on image resolution and volumetric convolution based method grows cubically with the volume size. Empirically, PointNet is able to process more than one million points per second for point cloud classification (around 1K objects/second) or semantic segmentation (around 2 rooms/second) with a 1080X GPU on TensorFlow, showing great potential for real-time applications.

Table 6. Time and space complexity of deep architectures for 3D data classification. PointNet (vanilla) is the classification PointNet without input and feature transformations. FLOP stands for floating-point operation. The “M” stands for million. Subvolume and MVCNN used pooling on input data from multiple rotations or views, without which they have much inferior performance.

6. Conclusion In this work, we propose a novel deep neural network PointNet that directly consumes point cloud. Our network provides a unified approach to a number of 3D recognition tasks including object classification, part segmentation and semantic segmentation, while obtaining on par or better results than state of the arts on standard benchmarks. We also provide theoretical analysis and visualizations towards understanding of our network. Acknowledgement. The authors gratefully acknowledge the support of a Samsung GRO grant, ONR MURI N0001413-1-0341 grant, NSF grant IIS-1528025, a Google Focused Research Award, a gift from the Adobe corporation and hardware donations by NVIDIA.
