# 124 - Fruit Detection and 3D Location Using Instance Segmentation Neural Networks and Structure-from-Motion Photogrammetry

## Metadata Ringkas
| Atribut | Nilai |
|---|---|
| Kunci BibTeX | `genemola2020fruit3d` |
| Judul asli | Fruit Detection and 3D Location Using Instance Segmentation Neural Networks and Structure-from-Motion Photogrammetry |
| Penulis | Jordi Gené-Mola, Ricardo Sanz-Cortiella, Joan R. Rosell-Polo, Josep-Ramon Morera, Javier Ruiz-Carulla, Eduard Gregorio, Alexandre Escolà |
| Tahun | 2020 |
| Venue | Computers and Electronics in Agriculture |
| Tema | Pertanian |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Fruit%20Detection%20and%203D%20Location%20Using%20Instance%20Segmentation%20Neural%20Networks%20and%20Structure-from-Motion%20Photogrammetry
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Fruit%20Detection%20and%203D%20Location%20Using%20Instance%20Segmentation%20Neural%20Networks%20and%20Structure-from-Motion%20Photogrammetry&sort=relevance
- **DOI Resmi:** https://doi.org/10.1016/j.compag.2019.105165

## Gambaran Umum
Makalah ini menyajikan sebuah metodologi untuk deteksi buah dan lokalisasi koordinat spasial tiga dimensi (*3D location*) buah di kebun buah menggunakan sensor pasif. Masalah utama yang diselesaikan adalah ketidakakuratan lokalisasi akibat oklusi dedaunan dan gangguan radiasi solar pada sensor kedalaman aktif luar ruangan. Metode yang diusulkan mengintegrasikan segmentasi instan (*instance segmentation*) 2D berbasis *Mask R-CNN* dengan rekonstruksi awan titik (*point cloud*) 3D berbasis *Structure-from-Motion* (SfM) dari citra multi-sudut (*multi-view*).

Sistem ini memproyeksikan masker 2D buah ke dalam ruang 3D hasil SfM. Deteksi palsu (*false positive*) disaring menggunakan pengklasifikasi *Support Vector Machine* (SVM) biner yang menganalisis fitur geometris dan kerapatan klaster titik 3D. Uji coba eksperimental pada dataset Fuji-SfM menunjukkan peningkatan kinerja yang signifikan dengan pencapaian F1-score sebesar 0,881 pada pemetaan lokasi 3D dibandingkan dengan 0,816 pada tingkat deteksi 2D saja. Penelitian ini menyediakan solusi pemetaan buah non-destruktif yang akurat untuk manajemen hasil panen.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Otomatisasi pemantauan hasil kebun dan pemanenan buah memerlukan sistem penglihatan komputer yang tidak hanya mampu mendeteksi keberadaan buah, tetapi juga mengidentifikasi lokasi spasial 3D buah tersebut secara presisi. Informasi spasial 3D ini sangat penting bagi manipulator robotik untuk merencanakan lintasan gerak memetik buah tanpa merusak struktur tanaman. Sebelum penelitian ini, sebagian besar metode deteksi berbasis pembelajaran mendalam berfokus pada deteksi 2D pada citra RGB tunggal. Pendekatan 2D ini kehilangan informasi kedalaman sehingga tidak memadai untuk aplikasi pemanenan robotik langsung.

Untuk mendapatkan informasi 3D, pendekatan sebelumnya menggunakan sensor kedalaman aktif seperti kamera RGB-D berbasis *Time-of-Flight* (ToF) atau sensor LiDAR. Namun, sensor aktif ini memiliki keterbatasan serius di lingkungan pertanian luar ruangan. Spektrum inframerah dari radiasi sinar matahari langsung mengganggu sensor penerima inframerah pada kamera RGB-D aktif, menghasilkan data kedalaman yang bising atau tidak lengkap. Di sisi lain, biaya perangkat keras LiDAR sangat mahal untuk penerapan praktis. Metode fotogrametri pasif seperti stereo konvensional juga rentan gagal akibat oklusi daun yang padat dan variasi pencahayaan alami di kebun buah. Diperlukan metode lokalisasi 3D pasif yang tangguh terhadap gangguan luar ruangan dan oklusi.

## Ide Utama
Gagasan utama makalah ini adalah menggabungkan kemampuan representasi visual Mask R-CNN dengan konsistensi geometris multi-sudut yang disediakan oleh rekonstruksi SfM pasif. Informasi deteksi dikumpulkan dari berbagai sudut pandang kamera saat bergerak mengitari pohon apel untuk melengkapi data spasial yang hilang akibat oklusi.

Alur data dari sistem ini menerima masukan berupa urutan citra RGB dari pohon apel. Citra diproses secara paralel untuk menghasilkan masker piksel 2D buah melalui Mask R-CNN dan merekonstruksi awan titik 3D melalui SfM. Masker piksel 2D diproyeksikan kembali (*back-projected*) ke ruang 3D menggunakan parameter kamera hasil kalibrasi SfM untuk membentuk klaster titik 3D. Klaster titik dari berbagai citra yang saling tumpang tindih digabungkan untuk merepresentasikan satu buah apel fisik yang unik. Terakhir, fitur geometris dari klaster 3D ini diekstraksi dan diklasifikasikan menggunakan SVM biner guna menyaring deteksi palsu yang disebabkan oleh proyeksi menyimpang pada daun atau tanah.

## Cara Kerja Langkah demi Langkah
Metodologi lokalisasi 3D ini terdiri dari serangkaian langkah terintegrasi yang memindahkan representasi objek dari piksel 2D ke ruang metrik 3D:

```
  [ Citra RGB Multi-view ] ──┬──> [ SfM Photogrammetry ] ──> [ 3D Point Cloud ]
                             │                                       │
                             └──> [ Mask R-CNN (ResNet-101) ]        │
                                         │                           │
                                         ▼                           │
                                 [ 2D Pixel Masks ]                  │
                                         │                           │
                                         ▼                           │
                                 [ Proyeksi 2D-3D ] <────────────────┘
                                         │
                                         ▼
                             [ 3D Point Clusters ]
                                         │
                                         ▼
                              [ Klasterisasi 3D ]
                                         │
                                         ▼
                            [ Ekstraksi Fitur 3D ]
                            (P, V, delta, Psi)
                                         │
                                         ▼
                            [ Penapisan SVM Biner ]
                                         │
                                         ▼
                            [ Posisi 3D Buah Valid ]
```

### Segmentasi Instan 2D Berbasis Mask R-CNN
Deteksi biner 2D dilakukan menggunakan jaringan saraf tiruan Mask R-CNN dengan *backbone* ResNet-101 dan *Feature Pyramid Network* (FPN). Jaringan ini memprediksi kelas, kotak pembatas (*bounding box*), skor keyakinan (*confidence score*), dan masker biner tingkat piksel untuk setiap buah. Sebelum pemrosesan, citra beresolusi tinggi dipotong menjadi 24 sub-gambar berukuran $1024 \times 1024$ piksel. Langkah pemotongan ini krusial untuk mencegah degradasi detail buah berukuran kecil akibat kompresi ukuran input standar pada model. Jaringan dilatih melalui penyetelan halus (*fine-tuning*) pada 288 citra beranotasi dari dataset Fuji-SfM setelah diinisialisasi dengan bobot COCO. Hasil deteksi direpresentasikan sebagai masker piksel $M_{ij}$ untuk citra ke-$i$ dan objek buah ke-$j$.

### Rekonstruksi 3D dengan Structure-from-Motion (SfM)
Secara paralel, 582 citra gerak sekuensial dari 11 pohon apel Fuji diproses menggunakan perangkat lunak Agisoft Metashape Professional. Algoritma SfM mencocokkan titik fitur lintas gambar untuk mengestimasi matriks kalibrasi intrinsik dan pose ekstrinsik kamera untuk setiap citra. Selanjutnya, algoritma *Multi-View Stereo* (MVS) membangun awan titik padat yang merekonstruksi struktur geometri kanopi pohon dalam skala spasial dunia nyata. Setiap titik dalam awan titik memiliki koordinat global ($X, Y, Z$).

### Proyeksi Masker 2D ke Awan Titik 3D
Setiap masker piksel 2D hasil deteksi Mask R-CNN diproyeksikan ke ruang 3D. Dari pusat optik kamera untuk citra $i$, sinar proyeksi dihitung melewati setiap koordinat piksel di dalam masker $M_{ij}$. Titik-titik 3D pada awan titik padat yang terletak dalam batas jarak ambang tertentu dari garis sinar proyeksi ditandai sebagai titik milik buah tersebut. Proses ini menghasilkan awan titik terproyeksi untuk setiap objek buah yang terdeteksi pada citra.

### Klasterisasi Spasial dan Penggabungan Multi-Sudut
Karena satu buah apel fisik dipotret dari beberapa citra dengan sudut pandang berbeda, titik-titik proyeksi dari berbagai citra akan terakumulasi pada koordinat spasial 3D yang sama. Algoritma klasterisasi spasial berbasis jarak Euclidean diterapkan untuk menggabungkan titik-titik yang saling berdekatan menjadi satu klaster kandidat buah 3D tunggal. Untuk menjamin konsistensi visual, diterapkan aturan penyaringan ketat: suatu klaster 3D hanya dianggap sebagai kandidat buah valid jika didukung oleh deteksi Mask R-CNN pada minimal 2 citra yang berbeda. Klaster yang hanya didukung oleh satu citra langsung dibuang untuk mengeliminasi kesalahan deteksi acak.

### Ekstraksi Fitur Geometris 3D
Untuk setiap klaster kandidat buah 3D yang lolos penyaringan konsistensi, dihitung empat fitur geometris dari sebaran titik-titik pembentuknya:
1. Jumlah titik ($P$): Total titik 3D yang membentuk klaster.
2. Volume ($V$): Volume amplop cembung (*convex hull*) dari klaster titik 3D.
3. Kepadatan titik ($\delta$): Rasio kerapatan yang dihitung sebagai $\delta = P / V$.
4. Sferisitas ($\Psi$): Ukuran kebulatan klaster yang dihitung dari nilai eigen normalized ($\lambda_1, \lambda_2, \lambda_3$ dengan $\lambda_1 \ge \lambda_2 \ge \lambda_3$ dan $\lambda_1 + \lambda_2 + \lambda_3 = 1$) dari matriks kovarians klaster titik 3D:
   $$\Psi = 27 \cdot \lambda_1 \cdot \lambda_2 \cdot \lambda_3$$
   Klaster buah apel asli yang mendekati bentuk bola memiliki nilai eigen yang seimbang sehingga nilai sferisitas $\Psi$ mendekati 1. Klaster palsu dari dahan atau daun cenderung memiliki nilai eigen yang tidak seimbang (satu atau dua dimensi dominan), menghasilkan nilai $\Psi$ mendekati 0.

### Penapisan False Positive dengan SVM
Fitur empat dimensi ($P, V, \delta, \Psi$) diinput to model SVM biner dengan kernel *Radial Basis Function* (RBF). Model SVM mengklasifikasikan setiap klaster ke dalam kelas buah sejati (*true positive*) atau deteksi palsu (*false positive*). Klaster yang diklasifikasikan sebagai buah sejati dipertahankan, dan koordinat rata-rata dari seluruh titik dalam klaster dihitung sebagai koordinat pusat 3D final buah apel tersebut.

## Eksperimen dan Hasil
Eksperimen dilakukan di kebun apel komersial pada 11 pohon apel Fuji (Malus domestica Borkh. cv. Fuji) yang memiliki total 1.455 buah apel asli yang dihitung manual sebagai acuan (*ground truth*). Performa deteksi 2D Mask R-CNN dibandingkan secara langsung dengan performa sistem lokalisasi 3D terintegrasi (Mask R-CNN + SfM + SVM).

Hasil kuantitatif eksperimen dirangkum dalam tabel berikut:

| Pendekatan | Presisi (*Precision*) | Sensitivitas (*Recall*) | F1-Score |
|---|---|---|---|
| Deteksi 2D (Mask R-CNN saja) | 0,762 (76,2%) | 0,878 (87,8%) | 0,816 (81,6%) |
| Lokasi 3D (Mask R-CNN + SfM + SVM) | 0,857 (85,7%) | 0,906 (90,6%) | 0,881 (88,1%) |

Integrasi geometri 3D dan penapisan SVM memberikan peningkatan performa yang signifikan. Presisi sistem meningkat sebesar 9,5% (dari 0,762 menjadi 0,857), membuktikan bahwa fitur geometris 3D dan klasifikasi SVM sangat efektif dalam menyaring deteksi palsu tingkat piksel. Sensitivitas (*recall*) juga meningkat sebesar 2,8% (dari 0,878 menjadi 0,906) karena buah yang mengalami oklusi parsial pada satu citra tetap dapat dikenali dari citra lain lalu digabungkan dengan sukses di ruang 3D. Secara keseluruhan, F1-score sistem meningkat dari 0,816 menjadi 0,881.

## Kelebihan dan Keterbatasan
Kelebihan utama dari metodologi ini adalah kemampuannya melakukan lokalisasi 3D buah secara pasif tanpa bergantung pada sensor kedalaman aktif. Hal ini memberikan ketangguhan tinggi terhadap kebisingan data akibat gangguan radiasi matahari luar ruangan yang sering merusak performa sensor RGB-D aktif berbasis inframerah. Penggunaan informasi multi-sudut juga secara alami mengatasi masalah oklusi parsial pada buah. Selain itu, publikasi dataset Fuji-SfM menyediakan kontribusi berharga bagi komunitas riset pertanian presisi.

Dari sisi rekayasa komputasi, keterbatasan utama sistem ini adalah tingginya beban komputasi proses SfM. Pencocokan fitur dan rekonstruksi awan titik padat memerlukan waktu pemrosesan yang lama (beberapa menit hingga beberapa jam per pohon), sehingga metode ini tidak dapat dioperasikan secara waktu-nyata (*real-time*) untuk robot pemanen. Secara konseptual, keandalan SfM sangat rentan terhadap perubahan kondisi lingkungan fisik selama pengambilan citra. Hembusan angin yang menggerakkan daun atau pergeseran bayangan matahari dapat merusak konsistensi geometri antar-citra, sehingga menurunkan kualitas rekonstruksi 3D dan akurasi lokalisasi buah.

## Kaitan dengan Bab Lain
Metodologi dalam bab ini mewarisi kebutuhan deteksi objek buah 2D pada citra RGB yang dibahas pada [Bab 120 (MangoYOLO)](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md), [Bab 121 (Apple Detection Improved YOLOv3)](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md), dan [Bab 122 (Apple Flower Detection Pruned YOLOv4)](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md). Ketiga bab tersebut menggunakan varian YOLO untuk deteksi 2D pada tingkat piksel gambar. Namun, metode-metode tersebut tidak menyediakan koordinat spasial 3D yang mutlak diperlukan untuk operasi lengan robot pemenang.

Untuk mengatasi kehilangan informasi spasial tersebut, [Bab 123 (Apple Detection RGB+Depth Faster R-CNN)](./123%20-%202020%20-%20Apple%20Detection%20RGB+Depth%20%28Faster%20R-CNN%29%20-%20Pertanian.md) menggunakan sensor kedalaman aktif (RGB-D) untuk mendapatkan data kedalaman buah secara langsung. Bab 124 (metode Gené-Mola dkk. ini) hadir sebagai alternatif pasif yang menyelesaikan kelemahan sensor aktif di Bab 123 terhadap gangguan cahaya matahari luar ruangan dengan mengadopsi rekonstruksi geometri SfM dari citra multi-sudut.

Meskipun demikian, lambatnya komputasi rekonstruksi SfM di Bab 124 membuatnya kurang cocok untuk memandu robot panen instan secara *real-time* seperti pada [Bab 125 (Iceberg Lettuce Harvesting Robot)](./125%20-%202020%20-%20Iceberg%20Lettuce%20Harvesting%20Robot%20-%20Pertanian.md) dan [Bab 126 (Automated Fruit Harvesting Robot Onishi dkk.)](./126%20-%202019%20-%20Automated%20Fruit%20Harvesting%20Robot%20%28Onishi%20dkk.%29%20-%20Pertanian.md) yang membutuhkan keputusan pemetikan instan. Sebagai alternatif lain, [Bab 127 (Fruit Detection & 3D Visualisation Kang & Chen)](./127%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Visualisation%20%28Kang%20%26%20Chen%29%20-%20Pertanian.md) berupaya menjembatani celah kecepatan pemrosesan ini dengan memanfaatkan sensor RGB-D modern dan algoritma visualisasi 3D real-time.

## Poin untuk Sitasi
Kunci BibTeX untuk bab ini adalah `genemola2020fruit3d`. Ringkasan yang aman dikutip dalam tinjauan pustaka akademik adalah:
"Gené-Mola dkk. mengusulkan metode deteksi dan lokalisasi buah 3D pasif dengan mengintegrasikan segmentasi instan Mask R-CNN pada citra RGB 2D dengan awan titik hasil rekonstruksi fotogrametri *Structure-from-Motion* (SfM) multi-sudut. Penapisan klaster titik 3D menggunakan Support Vector Machine (SVM) biner berhasil meningkatkan F1-score deteksi dari 0,816 menjadi 0,881 serta mengeliminasi kesalahan deteksi palsu akibat oklusi dedaunan."

Catatan verifikasi data: Angka-angka hasil utama (F1-score 3D 0,881, presisi 0,857, recall 0,906) telah diverifikasi secara akurat dari naskah publikasi resmi. Pengujian dilakukan pada 11 pohon apel Fuji dengan total populasi 1.455 buah apel. Keterbatasan sistem berupa waktu komputasi yang tinggi untuk rekonstruksi SfM dikonfirmasi oleh penulis sebagai batasan utama untuk penerapan waktu-nyata (*real-time*).

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract

of agriculture management. Most of the current fruit detection systems are based on 2D image analysis. Although the use of 3D sensors

is emerging, precise 3D fruit location is still a pending issue. This work presents a new methodology for fruit detection and 3D location

(4) false positives removal using a trained support vector machine. This methodology was tested on 11 Fuji apple trees containing a total

of 1455 apples. Results showed that, by combining instance segmentation with SfM the system performance increased from an F1-score

of 0.816 (2D fruit detection) to 0.881 (3D fruit detection and location) with respect to the total amount of fruits. The main advantages of

processing time required for SfM, which makes it presently unsuitable for real-time work. From these results, it can be concluded that the

combination of instance segmentation and SfM provides high performance fruit detection with high 3D data precision. The dataset has

results

Introduction

that can ensure the increased efficiency, quality, and sustainability of agricultural activities. To achieve this goal, precision

spaceborne‒ to carry this instrumentation, are key to providing precise and detailed crop information. Such questions are

resolution ‒within a specific tree and at plot level‒ is of enormous interest in agriculture. Having this information allows

on. In addition, knowledge of the georeferenced distribution of fruits along the plot can be a starting point for robotized

process itself, with a resulting gain in speed and efficiency.

The characterization of the 3D spatial distribution of fruits, at both tree and plot scale, is a highly active research field.

strengths and weaknesses when used in real-field conditions, with the best choice depending on the specific application.

extraction of a rich set of parameters and vegetation indexes, but they are more expensive and time-consuming. In the case

background enables their differentiation. However, measurements are affected by the fruit size and the thermal evolution of

principles. Both systems allow the generation of high density 3D point clouds (coloured in the case of RGB-D sensors) of

plants and fruits. While LiDAR sensors are usually quite expensive and not user-friendly, RGB-D are commonly low-cost

al., 2014), although it may lead to some fruits being counted twice if a proper image registration methodology is not used.

To do so, Stein et al. (2016) proposed the use of epipolar geometry combined with the Hungarian algorithm (Kuhn, 2010).

Similarly, Liu et al. (2018) used the Hungarian Algorithm refined with SfM to track fruits in video fruit counting. In

neural networks and SfM photogrammetry. The Mask R-CNN (He et al., 2017) deep neural network was used to detect and

segment fruits in 2D RGB images. Then, SfM was used to generate an accurate 3D model and locate the detected fruits in

the space. The main advantages of using SfM are that: (1) it is a multi-view approach and, in consequence, presents a

counting of apples appearing in different images. The remainder of this paper is structured as follows: Section 2 presents

2.1. Data acquisition.

Tests were carried out in a commercial Fuji apple orchard (Malus domestica Borkh. cv. Fuji) located in the municipality

approximately 3.5 m and 1.5 m, respectively. The studied section was formed by 11 consecutive trees from the same row of

trees, containing a total of 1455 apples. Images were acquired at the end of September 2017, at BBCH phenological growth

In the choice of photographic equipment and its setup, the quality of the photographs was prioritized. An EOS 60D

A total of 582 photographs were taken, 291 images per row side. No artificial light was used. The photographs were

taken freehand, which allowed an average shooting frequency of 8 photographs per minute. Thus, the lighting conditions

between the first and last photograph were very similar. The east face was photographed in the morning (11:53 - 12:26h)

and the west face in the afternoon (15:27 - 16:05h), with a similar illumination obtained in both faces.

taken (Fig. 1a) from the lower part (soil-trunk) to the upper part of the trees. The separation between two consecutive

positions was 22 cm (Fig. 1b). These photographic positions defined a line parallel with respect to the apple tree row. The

ground was 1.7 m (Fig. 1a). With this configuration, the vertical and horizontal overlapping between neighbouring images

was higher than 30% and 90%, respectively (Fig. 2). This dataset has been made publicly available at

Fig. 1. a) Transversal scheme of the layout and distances of the photographic process. b) Isometric view of three scanned trees showing the separation between consecutive photographic positions.

Fig. 2. a) Vertical overlapping between two contiguous photographs. b) Horizontal displacement between two adjacent photographic positions.

2.2. Methodology pipeline

As shown in Fig. 3, the proposed fruit detection and location methodology includes the following processing steps: 1)

1024x1024 pixels. Then, the convolutional neural network Mask R-CNN (He et al., 2017) was used to detect and segment

the apples (Section 2.2.1). Apple detections and masks in the cropped images were translated to the original images. These

Fig. 3. Fruit detection and location methodology flowchart. Hexagons represent data preparation steps while rectangles define data processing steps.

2.2.1. Instance segmentation

segmentation) in acquired 2D RGB images. For an input image, this model provides 2D bounding boxes and semantic

masks for the objects in the scene. It is an extension of the Faster R-CNN (Ren et al., 2017) network that adds a branch for

The operation is depicted in Fig. 4. Two parts can be differentiated in the architecture: the backbone, used for feature

142 Fig. 4. Diagram of Mask R-CNN architecture.

provides RoI features from different levels of the feature pyramid according to their scale.

The Mask R-CNN network head is a small network that is slid over the feature map. Each sliding window is mapped to

a lower-dimensional feature. At each sliding-window location, multiple region proposals are simultaneously predicted. The

proposals are parameterized relative to a set of reference boxes, called anchors. An anchor is centred at the sliding window

in question, and is associated with a scale and aspect ratio. This anchor-based design improves computational efficiency

allowing features to be shared without an extra cost for addressing scales.

layer. The process can be described in two stages. The first stage employs a region proposal network (RPN) to scan the

contain objects. The RoIAlign layer shares the forward pass of a CNN for an image across its subregions. Then, the

features in each region are pooled using bilinear interpolation to maintain a precise alignment. The second stage classifies

provides a pixel level mask for the object. The predictions of the class, bounding box and binary mask for each RoI are

backbone. A model pre-trained in the COCO dataset (Lin et al., 2014) was adapted for Fuji apple detection by restricting

used to test the system was not used for training. In order to have a better relation between image size and fruit size, and

applied to avoid the partially split of fruits at the boundaries in different partitions. Thus, the dataset used to train and

flipping data augmentation was used to increase the number of training images. The learning rate was set to 0.001, with a

adjustment (Triggs et al., 2000) was employed in each row side. This approach aims to simultaneously determine the

LLC, St. Petersburg, Russia). The specific software configuration parameters set are detailed in Appendix A, Table A1.

Feature matching: where correspondences between points across different images are computed.

Camera estimation: using the previous correspondences, camera parameters and locations are estimated for each image.

Dense reconstruction: camera parameters are used to project 2D image points into their corresponding 3D locations.

The relationship between 2D image points and 3D locations is described following a pinhole camera model. Let 𝑥𝑥 be a

(no 𝑖𝑖 subindex in matrix 𝐾𝐾). Extrinsic parameters, on the other hand, are different for each image. Thus, rotation matrices

Fig. 5a represents the 3D point cloud generated using original RGB images. This point cloud was manually annotated,

placing rectangular bounding boxes around each apple (Fig. 5b). A total of 1455 apples were annotated in the point cloud,

counting. Annotated 3D bounding boxes were used as ground truth to evaluate the performance of the system in Section

apples (not the entire trees) are reconstructed in Fig. 5c. Using masked images was desirable to only reconstruct the 3D

model of the objects of interest (apples) and to reduce the computational time. As the 3D reconstruction stage is scale

invariant, a set of known markers (depicted in Fig. 5d) separated by 85 cm were used to scale the resulting 3D point cloud

Fig. 5. a) Illustration of the 3D point cloud obtained using original RGB images. Yellow rectangles show the positions where reference markers were placed. b) Annotated point cloud with 3D rectangular bounding boxes placed around each apple. c) Apples 3D point cloud obtained using masked images. d) Illustration of reference markers used to scale the resulting 3D point cloud.

2.2.3. Projection of 2D detections onto 3D point cloud

2D image detections were projected onto the 3D point cloud using the pinhole camera model (Eqs. (1) and (2)). The main

Fig. 6 illustrates the steps carried out to perform the 2D to 3D projection, showing an example with two images taken

from different positions. To assist visualization, Fig. 6a shows a small region of the scanned scene and Fig. 6b shows the

3D model obtained applying SfM photogrammetry with masked images. In Fig. 6c, detections from image 1 (img1) were

projected onto the 3D point cloud. Due to the position of the camera with respect to the scene, an apple was occluded

behind the green detection. In consequence, after projecting the 2D green detection, the detected and the occluded apples

were clustered within the same group of 3D points (plotted in green in the 3D model of Fig. 6c). To identify objects behind

DBSCAN (Ester et al., 1996). The minimum distance between connected points was set to 3 cm. If more than one group of

connected points were found in a 3D detection, only the nearest (to the camera) was selected. Comparing Fig. 6c and Fig.

detections of img1 in the 3D point cloud, the next image (img2) was processed. Detections from img2 that presented an

overlap higher than 50% (IoU > 0.5) with previously detected apples were identified and unified (Fig. 6e), and new

detections with no overlap with previous detections or with IoU < 0.5 were projected onto the 3D point cloud (Fig. 6f). The

process was repeated for all the images used to generate the 3D point cloud.

In order to reduce the number of false positives, a linear support-vector-machine (SVM) was trained to identify and remove false positive detections. This SVM was fed using 4 features per detection:

λ1𝑛𝑛 + λ2𝑛𝑛 + λ3𝑛𝑛 = 1), obtained applying singular value decomposition (SVD) on the 3D points of a detection.

of 11) containing a total of 434 apples were used as the training dataset. The result of identifying and removing false

positive detections can be observed in Fig. 6g, where the blue detection has been removed.

Fig. 6. Projection of 2D detections onto 3D point cloud. a) Data acquisition. b) 3D model obtained using structure-from-motion with segmented images. c) Projection of detections from image 1 (img1) onto the 3D point cloud. d) Identification of apples behind detections. e) Identification of apples appearing in a new image that were previously detected in other images. f) Projection of a new detection (coloured in purple) from image 2 (img2). g) False positive removal.

number of multi-detections produced when a single apple is detected multiple times.

Results

for the 3D point cloud generation. This is because an increase of false positives (lower precision) is not as critical as

decreasing the recall, since to build the 3D model an object has to be seen in, at least, two different images. Then, false

positive objects that are only detected in one image will be automatically removed when applying SfM photogrammetry.

Table 2. Instance segmentation results at different confidence levels. Best F1-score result is in bold type.

Fig. 7 shows 6 selected images from the validation dataset and the corresponding fruit detections, allowing a qualitative

evaluation of instance segmentation results. As can be observed, most of the apples were successfully detected, including

highly occluded or shadowed ones. In addition, Mask-RCNN masked correctly the pixels belonging to an apple, even when

human error when labeling (green rectangles in Fig. 7 b-d,f). Other false positives were wrong detections at the image

borders, in parts of the image presenting a similar pattern to apples (red rectangles in Fig. 7 b-d), or multi-detections (blue

rectangles in Fig. 7 a,e-f). As for the apples not detected, it can be seen that false negatives (yellow rectangles in Fig. 7 a-

b,e) were apples cut at the image borders, highly occluded and/or small apples. To overcome the increase of false positives

sub-images (Section 2.2.1). Thus, detection failures at image borders did not affect the performance of the 3D model.

Fig. 7. Selected examples of instance segmentation results to show correct detections (colour masks), false positives due to network failures (red rectangles), false positives due to miss-annotated apples (green rectangles), false positives due to multi-detections (blue rectangles), and false negatives (yellow rectangles). For each capture, the original sub-image (left) and the corresponding detections (right) are shown.

detection and location. Table 3 presents the detection rates achieved in the training (3 trees, 434 apples) and test (8 trees,

1021 apples) datasets. Results show a high detection rate (DR=0.991) with low false detections (FDR=0.037). However,

because some apples were clustered in a unique detection (as shown in Fig. 9) and due to the presence of multi-detections

Table 3. 3D fruit detection and location results from training and test datasets.

Fig. 8 illustrates the correspondence between 𝐷𝐷 and 𝑇𝑇 in all trees of the dataset (11 trees). Results show the existence of a

298 Fig. 8. Linear regression between the number of detections (D) and the actual number of fruits per tree (T).

http://www.grap.udl.cat/documents/photogrammetry_fruit_detection.html. Using the side menu, the reader can either

detections obtained after 2D-3D projection and false positive removal steps.

that belong to each apple. The presence of false positives is almost non-existent (FDR=0.037), while most of the multi-

sufficiently (they were not unified) with the detection from the other tree side. In contrast, as shown in Fig. 9, some groups

Fig. 9. Illustration of 3D fruit detection and location results from the test dataset: a) 3D visualisation of the scanned scene. b) Test scene with coloured fruit detections. A zoom view is shown to assist the visualization of the detections in the first tree of the dataset. Black circles show two examples where two apples were unified in a single detection. The reader is referred to the following link for an interactive 3D visualization of test fruit detection results: http://www.grap.udl.cat/documents/photogrammetry_fruit_detection.html

processing steps implied in the presented methodology. The most computational expensive was the SfM photogrammetry,

conventional CPU computer. However, this processing time could be significantly reduced by processing this step in a

expensive step, which required 260 min to process all images from the dataset. Since the code developed to project 2D

detections onto the 3D point cloud was not parallelized, this step could not be processed in the CPU+GPU machine.

Table 4. Computational cost of processing steps implied in the developed methodology. The reported processing time corresponds to the time required to process all the dataset (11 trees, 582 images).

Discussion

location. By projecting 2D segmentation masks onto the 3D point cloud, results showed an increase of 2.8% in recall (from

was evaluated with respect to the total number of fruits in the tree. The use of SfM helped to increase the detection rate

because of the multi-view approach of this technique. As stated by Hemming et al. (2014), due to the unstructured

increases fruit detectability. When using multi-view imaging, an image registration is necessary to not double-count apples

appearing in different images. In this work, this registration was automatically done by projecting 2D detections onto the

3D point cloud; even so, results showed a 10.6% multi-detection rate. Other authors have proposed similar approaches:

Gongal et al. (2016) reported an error of 21.1% when identifying duplicate apples by projecting 2D image detections onto

3D models from RGB-D sensors, while Stein et al. (2016) used the 3D point cloud acquired from LiDAR-based sensors to

identify multi-detections, although they did not assess the performance of this multi-detection identification. Using SfM not

two different images. Then, false positives only detected in one image were automatically removed. This fact, combined

proper 3D location when projecting 2D detections onto the 3D point cloud. As for the 3D apple location performance, few

works have provided 3D detection rates with respect to the total amount of fruits in trees. For instance, Stein et al. (2016)

smaller dataset of 59 apples. Finally, comparing the presented methodology with respect to other computer vision systems

used in fruit harvesting robots, our system performed well compared to most of those presented in Bac et al. (2014) and

Williams et al. (2019), which reported detection rates below 85%. However, the presented methodology is not suitable for

the development of efficient algorithms could overcome this limitation in the future.

issue, as data can be processed offline. However, in the tests carried out in this work, data was acquired manually, being a

labour and time consuming task when scanning larger areas. In order to automatize the data acquisition, some authors have

Conclusions

apple detection and 3D location. Due to the multi-view approach on which SfM is based, results showed a small number of

advantage of using SfM was the reduction of false positives. Since SfM only generates the 3D model of those objects

appearing in, at least, two different images, false positives only detected in one image were automatically discarded. This

methodology performs well compared to other state-of-the-art 3D fruit location systems. The main disadvantage of this

is an important limitation for its application in harvesting robots. However, the evolution of computing hardware and the

development of efficient algorithms could overcome this issue in the future. The dataset and the corresponding annotations

have been made publicly available, being the first dataset for 3D photogrammetric fruit detection and location. Due to the

Ministry of Education is thanked for Mr. J. Gené’s pre-doctoral fellowships (FPU15/03355). We would also like to thank

data acquisition, and Ernesto Membrillo and Roberto Maturino for their support in dataset labelling.

Appendix A. Parameter values used for 3D point cloud generation

Table A1. Configuration set to perform the 3D reconstruction using Agisoft Professional Photoscan (v1.4, Agisoft LLC, St. Petersburg, Russia). Step

Appendix B. False positive feature analysis

Fig. B 1 Graphical representation of apple detection features. The features analysed are the volume, number of points, the geometric parameter Ψ, and the detection point density δ. False positives are represented in red crosses; true positives are represented in blue diamonds. This analysis was performed on the training data set and was used to train the SVM for false positives identification (explained in Section 2.2.3).
