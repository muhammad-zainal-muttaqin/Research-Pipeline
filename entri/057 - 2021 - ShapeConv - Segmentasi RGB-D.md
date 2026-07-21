# 057 - ShapeConv: Shape-Aware Convolutional Layer for Indoor RGB-D Semantic Segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cao2021shapeconv` |
| Judul asli | ShapeConv: Shape-aware Convolutional Layer for Indoor RGB-D Semantic Segmentation |
| Penulis | Jinming Cao, Hanchao Leng, Dani Lischinski, Danny Cohen-Or, Changhe Tu, Yangyan Li |
| Tahun | 2021 |
| Venue | IEEE/CVF International Conference on Computer Vision (ICCV 2021), hal. 7088–7097 |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2108.10528
- **Repositori kode resmi (PyTorch):** https://github.com/hanchaoleng/ShapeConv
- **Google Scholar:** https://scholar.google.com/scholar?q=ShapeConv%3A%20Shape-Aware%20Convolutional%20Layer%20for%20Indoor%20RGB-D%20Semantic%20Segmentation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=ShapeConv%3A%20Shape-Aware%20Convolutional%20Layer%20for%20Indoor%20RGB-D%20Semantic%20Segmentation&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan ShapeConv (*Shape-aware Convolutional layer*), lapisan konvolusi yang dirancang khusus untuk memproses fitur kedalaman pada segmentasi semantik RGB-D. Segmentasi semantik adalah pelabelan kelas objek untuk setiap piksel citra; pada varian RGB-D, masukannya berupa citra warna (RGB) yang dipasangkan dengan peta kedalaman, yaitu citra yang setiap pikselnya menyimpan jarak permukaan ke kamera. Dasar gagasannya: nilai kedalaman sebuah *patch* — jendela kecil seluas ukuran *kernel* konvolusi — memuat dua informasi berbeda, yaitu posisi dasar *patch* itu dalam ruang dan bentuk geometri lokalnya (variasi relatif antarpiksel). Konvolusi biasa mencampur keduanya, padahal bentuk memiliki hubungan lebih kuat dengan kelas semantik daripada posisi absolut.

ShapeConv memisahkan kedua komponen tersebut, menimbangnya dengan dua bobot terlatih yang berbeda, lalu menggabungkannya kembali sebelum konvolusi diterapkan. Karena bobot itu menjadi konstanta setelah pelatihan, keduanya dapat dilebur ke dalam *kernel* konvolusi, sehingga jaringan saat inferensi identik dengan jaringan konvolusi biasa — tanpa tambahan komputasi maupun memori. Diuji pada tiga *benchmark* dalam-ruang (NYUDv2, SUN RGB-D, SID) dan lima arsitektur segmentasi, ShapeConv menaikkan mean IoU antara 0,7 hingga 6,0 poin.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum 2021, metode segmentasi RGB-D umumnya menempuh dua jalur. Jalur pertama memakai dua jaringan paralel yang fiturnya digabung pada titik-titik tertentu: FuseNet (bab 051) menjumlahkan fitur kedalaman ke cabang RGB, RDFNet (bab 053) memperluas fusi ke banyak tingkat jaringan, dan ACNet (bab 054) menimbang fitur kedua modalitas dengan modul atensi. Jalur ini menyisakan dua masalah: sulit menentukan pada tahap mana fusi paling tepat dilakukan, dan arsitektur dua cabang menaikkan biaya komputasi secara signifikan.

Jalur kedua merancang lapisan baru yang sadar geometri. Konvolusi sadar-kedalaman (*depth-aware convolution*, Wang dan Neumann 2018) menimbang kontribusi piksel berdasarkan kesamaan kedalamannya melalui fungsi Gaussian yang dirancang manual. Konvolusi 2,5D *malleable* (Xing dkk. 2020) mempelajari luas reseptif sepanjang sumbu kedalaman. S-Conv pada SGNet (Chen dkk. 2021) memprediksi pergeseran titik *sampling* konvolusi dari informasi spasial tiga dimensi. Ketiganya sejalan: konvolusi standar bukan alat yang tepat untuk data kedalaman.

Kekurangan spesifik yang disasar ShapeConv adalah ketiadaan pembedaan informasi di dalam *patch* kedalaman. Dua kursi berbentuk sama tetapi berjarak berbeda menghasilkan *patch* bernilai berbeda, sehingga konvolusi biasa mengekstrak fitur berbeda untuk keduanya — padahal bentuk keduanya identik. Sebaliknya, komponen dasar juga tidak dapat dibuang begitu saja: pada lapisan berikutnya yang konteksnya lebih luas, komponen dasar inilah yang menyusun informasi bentuk berskala lebih besar.

## Ide Utama

Setiap *patch* kedalaman didekomposisi menjadi dua bagian. Komponen dasar (*base-component*) adalah rata-rata nilai *patch*, yang menyatakan di mana *patch* itu berada relatif terhadap kamera. Komponen bentuk (*shape-component*) adalah sisa setelah rata-rata dikurangkan, yang menyatakan perubahan relatif kedalaman di dalam *patch*, yaitu bentuk geometrinya. Dua bobot terlatih yang terpisah — satu skalar untuk komponen dasar, satu matriks untuk komponen bentuk — menimbang ulang keduanya sebelum dijumlahkan kembali menjadi *patch* sadar-bentuk yang kemudian dikonvolusi seperti biasa. Dengan cara ini, jaringan belajar menekan atau menonjolkan informasi bentuk sesuai kebutuhan.

## Cara Kerja Langkah demi Langkah

### Dekomposisi Patch

Konvolusi standar menghitung F = Conv(K, P): setiap elemen keluaran adalah jumlah hasil kali elemen *patch* P (berukuran Kh×Kw×Cin; Kh dan Kw ukuran spasial *kernel*, Cin jumlah kanal masukan) dengan bobot *kernel* K yang bersesuaian. Karena perhitungan ini linear terhadap nilai *patch*, dua *patch* berbentuk sama yang seluruh nilainya berbeda satu meter menghasilkan fitur berbeda.

ShapeConv memecah P menjadi P_B = m(P), yaitu rata-rata seluruh nilai *patch* per kanal (berukuran 1×1×Cin), dan P_S = P − m(P), yaitu komponen bentuk yang berukuran sama dengan P. Contoh numerik: *patch* 2×2 bernilai [[2,0; 2,0]; [2,2; 2,4]] meter memiliki rata-rata 2,15, sehingga komponen dasarnya 2,15 dan komponen bentuknya [[−0,15; −0,15]; [+0,05; +0,25]]. *Patch* lain dengan bentuk sama pada jarak satu meter lebih jauh, [[3,0; 3,0]; [3,2; 3,4]], memiliki komponen bentuk yang persis sama — hanya komponen dasarnya berbeda. Pemisahan inilah sumber invariansi yang dicari.

### Dua Bobot Terpisah: Base-Product dan Shape-Product

Komponen dasar ditimbang oleh *base-kernel* W_B, satu skalar terlatih yang mengalikannya (operasi *base-product*). Komponen bentuk diproses oleh *shape-kernel* W_S, matriks terlatih berukuran (Kh×Kw)×(Kh×Kw) untuk setiap kanal masukan (operasi *shape-product*): setiap posisi keluaran merupakan kombinasi terboboti dari seluruh posisi komponen bentuk, sehingga pola relatif antarpiksel — bukan nilai absolut — yang dipetakan. Untuk *kernel* 3×3 dan 256 kanal masukan, W_S berisi 9×9×256, atau sekitar 20.700 bobot per lapisan. Kedua hasil penimbangan dijumlahkan elemen demi elemen menjadi *patch* sadar-bentuk P_BS yang berukuran sama dengan P, lalu keluaran lapisan dihitung sebagai F = Conv(K, P_BS).

### Ekivalensi Dua Rumusan

Menghitung dua operasi produk pada setiap *patch* menambah biaya pelatihan. Penulis membuktikan bahwa operasi yang sama dapat dipindahkan dari *patch* ke *kernel*: *kernel* K didekomposisi menjadi K_B = m(K) dan K_S = K − m(K), lalu digabung menjadi K_BS = W_B⋄K_B + W_S∗K_S. Berlaku Conv(K, P_BS) = Conv(K_BS, P); kedua rumusan identik secara matematis, tetapi rumusan *kernel* tidak mengubah data masukan. Implementasi resmi memakai rumusan kedua ini.

### Inisialisasi Identitas dan Fusi Saat Inferensi

W_B diinisialisasi 1 dan W_S diinisialisasi matriks identitas, sehingga pada awal pelatihan berlaku K_BS = K: ShapeConv persis merupakan konvolusi biasa. Inisialisasi ini memberi dua keuntungan: fitur RGB diproses sama seperti jaringan asalnya, dan bobot pralatih ImageNet dapat dipakai ulang apa adanya. Setelah pelatihan, W_B dan W_S menjadi konstanta dan dilebur permanen ke dalam K_BS, yang berukuran persis sama dengan K. Jaringan inferensi yang dihasilkan identik dengan jaringan konvolusi biasa; tambahan waktu komputasi dan memori saat inferensi adalah nol.

### Penempatan dalam Jaringan Segmentasi

ShapeConv menggantikan seluruh lapisan konvolusi, baik pada *backbone* (jaringan pengekstrak fitur, misalnya ResNet) maupun pada tahap segmentasi. Masukan jaringan adalah penggabungan kanal RGB dengan kanal kedalaman; kedalaman dapat berupa nilai mentah atau pengkodean HHA — tiga kanal turunan kedalaman yang terdiri atas disparitas horizontal, tinggi di atas lantai, dan sudut normal permukaan terhadap sumbu vertikal (diperkenalkan Gupta dkk. 2014). Alur pemrosesan satu *patch* pada satu lapisan:

```
        patch kedalaman P (Kh x Kw x Cin)
        |
        +-------------------+--------------------+
        v                   v                    |
  P_B = rata-rata(P)   P_S = P - rata-rata(P)    |
  (1x1xCin)            (Kh x Kw x Cin)           |
  "di mana"            "bentuk apa"              |
        |                   |                    |
        v                   v                    |
  base-product         shape-product             |
  W_B . P_B            W_S * P_S                 |
  (1 skalar terlatih)  (matriks terlatih)        |
        |                   |                    |
        +------->(+)--------+                    |
                  v                              |
        patch sadar-bentuk P_BS                  |
                  v                              |
        F = Conv(K, P_BS)                        |
                                                 |
  inferensi: W_B, W_S konstan, dilebur ke kernel |
  K_BS = W_B.K_B + W_S*K_S  ->  F = Conv(K_BS, P)|
  (jaringan identik konvolusi biasa, biaya +0)   |
```

Satu-satunya perbedaan terhadap konvolusi biasa terletak pada cabang dekomposisi dan penimbangan; cabang itu hilang saat inferensi karena bobotnya menyatu ke dalam *kernel*.

## Eksperimen dan Hasil

Pengujian dilakukan pada tiga *benchmark* segmentasi dalam-ruang. NYUDv2 memuat 1.449 citra RGB-D (795 latih, 654 uji) dengan dua pengaturan: 13 kelas dan 40 kelas. SUN RGB-D memuat 10.355 citra dari 37 kelas (5.285 latih, 5.050 uji). SID (*Stanford Indoor Dataset*) jauh lebih besar, yaitu 70.496 citra dari 13 kelas, dengan pengujian pada area gedung yang tidak muncul saat pelatihan. Metrik yang dilaporkan mencakup akurasi piksel, akurasi rata-rata kelas, mean IoU (mIoU — rata-rata rasio irisan terhadap gabungan per kelas, metrik utama segmentasi), dan *frequency-weighted* IoU. *Baseline* dan versi ShapeConv hanya berbeda pada lapisan konvolusinya; seluruh pengaturan lain sama, sehingga selisih kinerja murni berasal dari ShapeConv.

Hasil mIoU utama (pengujian skala tunggal, arsitektur DeepLabv3+):

| Dataset | *Backbone* | *Baseline* | +ShapeConv | Selisih |
|---|---|---|---|---|
| NYUDv2-13 | ResNeXt-101 | 63,2 | 65,1 | +1,9 |
| NYUDv2-40 | ResNet-101 | 45,9 | 47,4 | +1,5 |
| SUN RGB-D | ResNet-101 | 46,9 | 47,6 | +0,7 |
| SID | ResNet-101 | 54,6 | 60,6 | +6,0 |

Lonjakan terbesar pada SID (+6,0 poin mIoU, akurasi piksel 78,7 menjadi 82,7) konsisten dengan ukuran datasetnya yang puluhan kali lebih besar: W_S memuat banyak bobot, dan 70 ribu citra menyediakan cukup data untuk mempelajarinya. Sebaliknya, kenaikan pada SUN RGB-D hanya +0,7 poin, menunjukkan manfaat yang bergantung pada karakteristik dataset.

Terhadap metode lain pada NYUDv2-40 dengan pengujian multi-skala (citra diuji pada beberapa skala lalu hasilnya digabung), ShapeConv mencapai 51,3% mIoU, di atas SGNet (51,1), konvolusi 2,5D *malleable* (50,9), RDFNet (50,1), dan ACNet (48,3). Pada NYUDv2-13, skornya 65,6 dibandingkan 59,3 milik PVNet, selisih 6,3 poin. Uji generalisasi pada lima arsitektur — DeepLabv3+, DeepLabv3, UNet, PSPNet, dan FPN — dengan *backbone* ResNet-50/101 pada NYUDv2-40 menunjukkan kenaikan mIoU 1,2 hingga 2,3 poin pada seluruh sepuluh kombinasi, membuktikan sifat *plug-and-play* (dapat disisipkan tanpa mengubah arsitektur).

Pada ablasi NYUDv2-40, tanpa kedua bobot (konvolusi biasa) mIoU 45,9; hanya W_B menghasilkan 47,0; hanya W_S menghasilkan 46,3; keduanya bersama menghasilkan 47,4. Kedua bobot terbukti saling melengkapi, dan W_B yang hanya satu skalar memberi sumbangan terbesar sendirian. Masukan HHA mengungguli kedalaman mentah (47,4 berbanding 46,2 dengan ShapeConv). Analisis *trimap* — penghitungan piksel salah-kelas dalam pita sempit di sekitar batas objek, mengikuti metode Kohli dkk. — menunjukkan ShapeConv unggul pada semua lebar pita, artinya perbaikannya terkonsentrasi pada tepi objek, sesuai tujuan pemodelan bentuk.

## Kelebihan dan Keterbatasan

Kelebihan utama ShapeConv adalah biaya inferensi nol: seluruh mekanisme tambahan menyatu ke dalam *kernel* setelah pelatihan, sehingga tidak ada penalti kecepatan maupun memori saat model dipakai. Sifatnya yang *model-agnostic* memungkinkannya menggantikan konvolusi pada hampir semua CNN, dan inisialisasi identitas membuat bobot pralatih tetap dapat dipakai apa adanya.

Keterbatasannya, penulis sendiri menyatakan bahwa dekomposisi berbasis rata-rata hanya menangani perbedaan translasi kedalaman; transformasi rotasi akibat sudut pandang kamera tidak teratasi. Dari sisi rekayasa, W_S menambah sekitar 20.700 parameter per lapisan 3×3 berkanal 256, sehingga biaya pelatihan dan kebutuhan data naik — gejala ini terlihat dari kecilnya peningkatan pada dataset yang lebih kecil. Secara konseptual, manfaatnya bergantung pada kualitas peta kedalaman dan, untuk hasil terbaik, pada prapemrosesan HHA; selain itu penerapannya menuntut pelatihan ulang jaringan secara penuh, bukan penyetelan ringan.

## Kaitan dengan Bab Lain

ShapeConv mengambil arah berlawanan dari jalur fusi dua cabang pada bab-bab sebelumnya. [FuseNet](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md) (bab 051), [RDFNet](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md) (bab 053), dan [ACNet](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md) menggabungkan fitur dua modalitas melalui arsitektur; ShapeConv justru menggabungkan masukan sejak awal lalu memodifikasi operator konvolusinya — dan pada NYUDv2-40 dilaporkan melampaui RDFNet (50,1 berbanding 51,3) serta ACNet (48,3). Ia seangkatan dengan [ESANet](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md) (bab 056), yang juga terbit 2021 tetapi mengejar efisiensi lewat arsitektur ringan. Gagasan memanfaatkan perbedaan sifat RGB dan kedalaman kemudian dilanjutkan pada arsitektur *transformer* oleh [CMX](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md) (bab 058), yang menukar fusi konvolusi dengan mekanisme *cross-attention* antarmodalitas.

## Poin untuk Sitasi

Kunci BibTeX: `cao2021shapeconv`. Ringkasan aman kutip: ShapeConv (Cao dkk., ICCV 2021) adalah lapisan konvolusi untuk fitur kedalaman yang mendekomposisi *patch* menjadi komponen dasar (rata-rata) dan komponen bentuk (residu), menimbang keduanya dengan bobot terlatih terpisah, lalu menggabungkannya kembali sebelum konvolusi. Bobot tersebut dapat dilebur ke *kernel* saat inferensi sehingga tidak menambah komputasi, dan penggantian konvolusi biasa dengan ShapeConv menaikkan mIoU pada NYUDv2, SUN RGB-D, dan SID lintas lima arsitektur segmentasi.

Catatan verifikasi sebelum sitasi formal: seluruh angka pada bab ini diambil dari arXiv v1 (Agustus 2021) dan README repositori resmi; cocokkan dengan versi kamera-siap ICCV 2021 (hal. 7088–7097) karena angka tabel dapat berbeda tipis antarversi. Klaim "biaya inferensi nol" hanya berlaku setelah fusi bobot — pada fase pelatihan tetap ada tambahan parameter dan komputasi. Klaim analisis *trimap* bersifat grafis (kurva pada Gambar 5 makalah), tanpa tabel angka.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Abstract RGB-D semantic segmentation has attracted increasing attention over the past few years. Existing methods mostly employ homogeneous convolution operators to consume the RGB and depth features, ignoring their intrinsic differences. In fact, the RGB values capture the photometric appearance properties in the projected image space, while the depth feature encodes both the shape of a local geometry as well as the base (whereabout) of it in a larger context. Compared with the base, the shape probably is more inherent and has a stronger connection to the semantics, and thus is more critical for segmentation accuracy. Inspired by this observation, we introduce a Shape-aware Convolutional layer (ShapeConv) for processing the depth feature, where the depth feature is firstly decomposed into a shape-component and a base-component, next two learnable weights are introduced to cooperate with them independently, and finally a convolution is applied on the re-weighted combination of these two components. ShapeConv is model-agnostic and can be easily integrated into most CNNs to replace vanilla convolutional layers for semantic segmentation. Extensive experiments on three challenging indoor RGB-D semantic segmentation benchmarks, i.e., NYU-Dv2(-13,-40), SUN RGB-D, and SID, demonstrate the effectiveness of our ShapeConv when employing it over five popular architectures. Moreover, the performance of CNNs with ShapeConv is boosted without introducing any computation and memory increase in the inference phase. The reason is that the learnt weights for balancing the importance between the shape and base components in ShapeConv become constants in the inference phase, and thus can be fused into the following convolution, resulting in a network that is identical to one with vanilla convolutional layers.

!"# $%&'ℎ Figure 1. Visual demonstration of why the shape of an RGB-D image matters. Regarding the images on the top, lines with the same color share a same shape, yet with different base. The corresponding patches are shown on the bottom.

1. Introduction With the widespread use of depth sensors (such as Microsoft Kinect [31]), the availability of RGB-D data has boosted the advancement of RGB-D semantic segmentation, which contributes to an indispensable task in the computer vision community. Thanks to the flourishing of Convolutional Neural Networks (CNNs), recent studies mostly resort to CNNs for tackling this problem. Convolutional layers, deemed as the core building blocks of CNNs, are accordingly the key elements in RGB-D semantic segmentation models [6, 13, 15, 17, 21]. However, RGB and depth information are inherently different from each other. In particular, RGB values capture the photometric appearance properties in the projected image space, while the depth feature encodes both the shape of a local geometry as well as the base (whereabout) of it in a larger context. As a result, the convolution operator that is widely adopted for consuming RGB data might not be

the optimal for processing the depth data. Taking Figure 1 as an example, we would expect the corresponding patches of the same chairs to have the same features, as they share the same shape. The shape is a more inherent property of the underlying object and has stronger connection to the semantics. We would expect to achieve shape invariance in the learning process. When a vanilla convolution operator is applied on these corresponding patches, the resulting features are different due to the differences in their base component, hindering the learning from achieving shape invariance. On the other hand, the base components cannot be simply discarded for pursuing the shape invariance in the current layer, as they form the shape in a followup layer with a larger context. To address these problems, we propose a Shape-aware Convlutional layer (ShapeConv), to learn the adaptive balance between the importance of shape and base information, giving the network the chance to focus more on the shape information whenever necessary for benefiting the RGB-D semantic segmentation task. We firstly decompose a patch1 into two separate components, i.e., a basecomponent and a shape-component. The mean of patch values depicts the whereabout of the patch in a larger context, thus constitutes the base component, while the residual is the relative changes in the patch, which depicts the shape of the underlying geometry, thus constitutes to the shape component. Specifically, for an input patch (such as P1 in Figure 1), the base describes where the patch is, i.e., the distance from the observation point; while the shape expresses what the patch is, e.g., a chair corner. We then employ two operations, namely, base-product and shape-product, to respectively process these two components with two learnable weights, i.e., base-kernel and shape-kernel. The output from these two is then combined in an addition manner to form a shape-aware patch, which is further convolved with a normal convolutional kernel. In contrast to the original patch, the shape-aware one is capable of adaptively learning the shape characteristic with the shape-kernel, and the base-kernel serves to balance the contributions of the shape and the base for the final prediction. In addition, since the base-kernel and shape-kernel become constants in the inference phase, we can fuse them into the following convolution kernel, resulting in a network that is identical to the one with vanilla convolutional layers. The proposed ShapeConv can be easily plugged into most CNNs as a replacement of the vanilla convolution in semantic segmentation without introducing any computation and memory increase in the inference phase. This simple replacement transforms CNNs designed for RGB data into ones better suited for consuming RGB-D data. To validate the effectiveness of the proposed method, 1 The operation unit of input features for the convolutional layer, whose spatial size is the same as the convolution kernel.

we conduct extensive experiments on three challenging RGB-D indoor semantic segmentation benchmarks: NYUDv2 [25](-13,-40), SUN RGBD [26], and SID [1]. We apply our ShapeConv to five popular semantic segmentation architectures and can observe promising performance improvements compared with baseline models. We found that ShapeConv can significantly improve the segmentation accuracy around the object boundaries (see Figure 5), which demonstrates the effective leveraging of the depth information2 .

2. Related Work CNNs have been widely used for semantic segmentation on RGB images [3, 4, 19, 18, 23, 33]. In general, existing segmentation architectures usually involve two stages: the backbone and the segmentation stage. The former stage is leveraged to extract features from RGB images, wherein popular models are ResNet [12], ResNeXt [29] which are pre-trained on the ImageNet dataset [24]. The latter stage aims to generate predictions based on the extracted features. Methods in this stage include Upsample [19], PPM [33] and ASPP [3, 4], etc. It is worth noting that both stages adopt the convolutional layers as the core building blocks. As RGB semantic segmentation has been extensively studied in literature, a straightforward solution for RGB-D semantic segmentation is to adapt the well-developed architectures from the ones designed for RGB data. However, implementing such a idea is non-trivial due to the asymmetric modality problem between the RGB and the depth information. To tackle this, researchers have devoted efforts into two directions: designing dedicated architectures for RGB-D data [6, 8, 13, 15, 17, 21, 28], and presenting novel layers to enhance or replace the convolutional layers in RGB semantic segmentation [5, 27, 30]. Our method falls into the second category. Methods in the first category propose to feed RGB and depth channels to two parallel CNNs streams, where the output features are fused with specific strategies. For example, [6] presents a gate-fusion method, [8, 13, 21] fuse the features in multi-levels of the backbone stages. Nevertheless, these methods mostly leverage separate networks to consume RGB and depth features, they are yet faced with two limitations: 1) it is hard to decide when is the best stage for the fusion to happen; and 2) the two-stream or multilevel way often results in large increase of computation. In contrast, methods along the second direction target at designing novel layers based on the geometric characteristics of RGB-D data, which are more flexible and timeefficient. For instance, Wang et al. [27] proposed the depthaware convolution to weight pixels based on a hand-crafted Gaussian function by leveraging the depth similarity between pixels. [30] presents a novel operator called mal2 Our code is released through https://github.com/hanchaoleng/ShapeConv.

leable 2.5D convolution, to learn the receptive field along the depth-axis. [5] devises a S-Conv to infer the sampling offset of the convolution kernel guided by the 3D spatial information, enabling the convolutional layer to adjust the receptive field and geometric transformations. ShapeConv proposed a novel view of the content in each patch and a mechanism to leverage them adaptively with learnt weights. Moreover, ShapeConv can be converted into vanilla convolution in the inference phase, resulting in ZERO increase of memory and computation compared with the models with vanilla convolution.

3. Method In this section, we first provide the basic formulation of the Shape-aware convolutional layer (ShapeConv) for RGB-D data, followed by its application in the training and inference phase. We end this section with the method architectures.

3.1. ShapeConv for RGB-D Data Method Intuition. Given an input patch P ∈ RKh ×Kw ×Cin , Kh and Kw are the spatial dimensions of the kernel; Cin represents the channel numbers in the input feature map, the output features from the vanilla convolution layer are obtained by, F = Conv(K, P),

where K ∈ RKh ×Kw ×Cin ×Cout denotes the learnable weights of kernels in a convolutional layer (The bias terms are not included for simplicity.); Cout represents the channel numbers in the output feature map. Each element of F ∈ RCout is calculated as, Fcout =

ShapeConv Formulation. Based on the aforementioned analysis, in this paper, we offer to decompose an input patch into two components: a base-component PB describing where the patch is, and a shape-component PS expressing what the patch is. Therefore, we refer the mean3 of patch values to be PB , and its relative values to be as PS :

It can be easily recognized that F usually changes with respect to different values of P. Take the two patches in the Figure 1, P1 and P2 , as an example. The corresponding output features, F1 and F2 from the vanilla convolution layer are learned by: F1 = Conv(K, P1 ), F2 = Conv(K, P2 ). Since P1 and P2 are not identical (different distances from the observation points), accordingly, their features are usually different, and this may lead to distinct prediction results. Nevertheless, P1 and P2 , corresponding to the red regions in Figure 1, actually belong to the same class - chair. And vanilla convolutional layers cannot well handle such situations. In fact, there exists some invariants of these two patches, namely, the shape. It refers to the relative depth correlation under local features, which is however, unexpectedly ignored by the existing methods. In view of this, we propose to fill this gap via effectively modeling the shape for RGB-D semantic segmentation.

(4) where cin , kh , kw are the indices of the elements in Cin , Kh , Kw dimensions, respectively. We reconstruct the shape-aware patch PBS from the addition of PB and PS , and PBS ∈ RKh ×Kw ×Cin , which enables it to be smoothly convolved by the kernel K of vanilla convolutional layer. Nevertheless, the PBS is equipped with the important shape information which is learned by the two additional weights, making the convolutional layer to focus on the situations when merely using depth values fails.

3.2. ShapeConv in Training and Inference Training phase. The proposed ShapeConv in Section 3.1 can effective leverage the shape information of 3 As the depth values are obtained from a fixed observation point, we

notice that the rotational transformations cannot be addressed due to the angle of view limitation. As a result, we focus more on the translational transformations in this paper.

please refer to the Supp. for detailed proof. In this way, we utilize the ShapeConv in Equation 5 in our implementation as illustrated in Figure 2(b) and (c). Inference phase. During inference, since the two additional weights i.e. WB and WS , become constants, we can fuse them into KBS as shown in Figure 2(c) with KBS = WB KB + WS ∗ KS . And KBS shares the same tensor size with K in Equation 1, thus, our ShapeConv is actually the same as the vanilla convolutional layer in Figure 2(a). In other words, when replacing vanilla convolution with ShapeConv, there would introduce zero additional inference time.

3.3. ShapeConv-enhanced Network Architecture Different from devising specially dedicated architectures for RGB-D segmentation [21, 22, 17], the proposed ShapeConv is a more generalized approach that can be easily plugged into most CNNs as a replacement for the vanilla convolution in semantic segmentation, which is then transformed for adapting the RGB-D data. Figure 3 depicts an example of the overall method architecture. In order to leverage the advanced backbones in semantic segmentation, we firstly require to convert the input features from RGB images to RGB-D data via the concatenation of the RGB and D information. In practice, D can be depth values [11, 20] or HHA4 images [10, 19, 16, 6]. We then replace the vanilla convolution layer with the ShapeConv in both the backbone and segmentation stages. It is worth noting that, WB is initialized to one, WS can be viewed as Cin square (Kh × Kw ) × (Kh × Kw ) matrices, which are initialized to the identity matrix. In this way, ShapeConv is equivalent to the vanilla convolution at the beginning of training since KBS = K. This initialization approach offers two advantages: 1) It makes the ShapeConvenhanced networks do not interfere with the RGB data, i.e., the RGB features are processed in the same way as before. 2) It facilitates ShapeConv to reuse the parameters from pretrained models. 4 Horizontal disparity, Height above ground and normal Angle to the vertical axis.

Figure 3. The overall semantic segmentation network architecture. In this figure, yellow and orange cube denote the RGB and D inputs; “C” denotes channel-wise concatenation; Green and blue boxes denote architectures consisting of vanilla convolutional layers and ShapeConv layers, respectively.

Thus, with this approach, future advances in RGB semantic segmentation architectures can be easily transferred to consuming the RGB-D data, greatly reducing the effort that would otherwise be spent on designing dedicated networks for RGB-D semantic segmentation. We have shown the results of building RGB-D segmentation networks with this style using several popular architectures [3, 4, 18, 23, 33] in Sec 4.2.

4. Experiments Datasets and metrics. Among the existing RGB-D segmentation problems, the indoor semantic segmentation is rather challenging, as the objects are often complex and with severe occlusions [5]. Thus, in order to validate the effectiveness of the proposed method, we conducted experiments on three indoor RGB-D benchmarks: NYU-DepthV2 (NYUDv2-13 and -40) [25], SUN-RGBD [26] and Stanford Indoor Dataset (SID) [1]. NYUDv2 contains 1,449 RGB-D scene images, where 795 images are split for training and 654 images for testing. We adopted two popular settings for this dataset, i.e., 13-class [25] and 40-class [9], where all pixels are labeled with 13 and 40 classes, respectively. SUN-RGBD is composed of 10,355 RGB-D indoor images with 37 categories for each pixel label. We followed the widely used setting in [26] to split the dataset into a training set of 5285 images and a testing set of 5050 images. SID contains 70, 496 RGB-D images with 13 object categories. In particular, areas 1, 2, 3, 4, and 6 used for the training and Area 5 is for testing following [27]. We reported the results using the same evaluation protocol and metrics as FCN [19], i.e., Pixel Accuracy (Pixel Acc.), Mean Accuracy (Mean Acc.), Mean Region Intersection Over Union (Mean IoU), and Frequency Weighted Intersection Over Union (f.w. IoU). Comparison protocol. We adopted several popular architectures with different backbones as our baseline methods to

demonstrate the effectiveness and generalization capability of ShapeConv. For all the baseline methods, we only replaced the vanilla convolutional layers with our ShapeConv, without any change to other settings. This guarantees that the obtained performance improvements is due to the application of ShapeConv, but not other factors. Table 1. Performance comparison with baselines on NYUDv2-13 dataset. Deeplabv3+ is the adopted architecture. Back bone

Implementation Details. We used the ResNet [12] and ResNeXt [29] initialized with the pre-trained model on ImageNet [24] in the backbone stage. If not otherwise noted, the inputs of both the baseline and ours are the concatenation of RGB and HHA images. We adopted both singlescale and multi-scale testing strategies during inference. For the latter one, left-right flipped images and five scales are exploited: [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]. F in tables of this section denotes the multi-scale strategy. Note that, no

post-processing tricks like CRF [2] is used in our experiments.

Table 4. Performance comparison with other methods on NYUDv2-40 dataset. Method

Table 2. Performance comparison with baselines on NYUDv2-40 dataset. Deeplabv3+ is the adopted architecture. Back bone

4.1. Experiments on Different Datasets

Table 3. Performance comparison with other methods on NYUDv2-13 dataset. Method Eigen [7] MVCNet [20] Ours MVCNet [20]F PVNet [32]F OursF

SUN-RGBD Dataset. The comparison results between baseline and ours with SUN-RGBD dataset are reported in

Table 5. Performance comparison with baselines on SUN-RGBD dataset. The architectures adopted in this table is deeplabv3+ with different backbones.

NYUDv2 Dataset. We adopted two popular settings for this dataset, i.e., 13-class [25] and 40-class [9], and show the results of baseline and our method with different backbones on NYUDv2-13 and NYUDv2-40 in Table 1 and Table 2, respectively. It can be seen that architectures with ShapeConv outperform the baselines with a large margin under all settings. We also compare the performance of our ShapeConv with several recently developed methods in Table 3 and Table 4. As illustrated in Table 3, ShapeConv achieves the best over all the four metrics on NYUDv2-13. Compared to the recently proposed method [32], our approach yields around 6.3% improvements on Mean IOU which is the most commonly used metric for semantic segmentation. In addition, our method also achieves a competitive performance on NYUDv2-40 in Table 4.

SID Dataset. Note that SID dataset is much larger than the other two datasets, contributing to a better testbed for

Figure 4. Visualization results from NYUDv2 dataset. Input column denotes RGB, Depth, HHA images from top to bottom; the black regions in the GT, Baseline and Ours indicate the ignored category. The upper and lower cases are from NYUDv2-40 and NYUDv2-13, respectively.

evaluating RGB-D semantic segmentation model capabilities. The results on SID dataset between the baseline with ours and the state-of-the-art methods are reported in Table 7. We can observe that our ShapeConv surpasses these methods with a large margin. Note that even though we utilized a strong baseline (ResNet-101 backbone) which surpasses MMAF-Net-152 (ResNet-152 backbone) with 1.7% Mean IoU, our ShapeConv can still achieves a 6% Mean IoU improvement. This highlights the effectiveness of our method. Table 7. Performance comparison on SID dataset. The architectures of baseline and ours adopted in this table is deeplabv3+ with ResNet-101 backbone and the “+” denote the deltas relative to the baseline method. Method D-CNN [27] MMAF-Net-152 [8] Baseline-101 Ours-101 +

4.2. Experiments on Different Architectures Our proposed ShapeConv is a general layer for RGBD semantic segmentation which can be easily plugged into most CNNs as a replacement for the vanilla convolution in semantic segmentation. To verify its generalization properties, we also evaluated the effectiveness of our method in several representative semantic segmentation architectures: Deeplabv3+ [4], Deeplabv3 [3], UNet [23], PSPNet [33] and FPN [18] with different backbones (ResNet-50 [12], ResNet-101 [12]) on NYUDv2-40 dataset, and reported the performance in Table 8. We can see that ShapeConv brings significant performance improvements under all settings, demonstrating the generalization capability of our method.

Table 8. Performance comparison with different baseline methods on NYUDv2-40 dataset. Architecture

4.3. Visualization Figure 4 illustrates the qualitative results on NYUDv213 and -40, more results can be found in the Supp. As shown in this figure, the depth information, especially the detailed one, can be well utilized by ShapeConv to extract the object features. For instance, the chair and table regions in the top example of Figure 4(a) are with gradually changed colors, making it hard to predict accurate segmentation boundaries of the baseline method. The shape fea-

Figure 5. Segmentation accuracy around object boundaries. In this figure, the left is the visualization of the “trimap” measure; The right is the percent of misclassified pixels within trimaps of different widths.

tures learned by ShapeConv makes the accurate cut following the geometric hints compare with the conventional convolutional layer. For other two cases, i.e., the chair in the bottom example of Figure 4(a) and the desk in the top example of Figure 4(b), the ShapeConv can also significantly improve the segmentation results in edge areas compared with the baseline. It is worth noting that for the multiple bookshelves in the bottom example of Figure 4(b), ShapeConv achieves more consistent predictions. This is because our ShapeConv yields a positive tendency for smoothing neighborhood regions within same classes. To validate the effectiveness of our method on modeling the depth information, we adopted the comparison strategy proposed by Kohli et al. [14]. Specifically, we counted the relative number of misclassified pixels within a narrow band (“trimap”) surrounding ground-truth object boundaries. As shown in Figure 5, our method outperforms the baseline across all trimap widths. This further demonstrates the segmentation effectiveness of our method on edge areas, where the shape information matters.

4.4. Ablation Study We conducted ablation experiments to validate the indispensability of the two introduced weights in Equation 5. As can be observed in Table 9, the model performance degrades when removing either WB or WS , or both. This proves that both the base-kernel and shape-kernel are essential for the final performance improvement, and combing these two achieves the best results. Table 9. Performance comparison with and without WB and WS in ShapeConv on NYUDv2-40. The architecture adopted in this table is deeplabv3+ with ResNet-101 as backbone. WB

To provide a more in-depth analysis of ShapeConv, we conducted detailed ablation studies on the NYUDv2-40 dataset with deeplabv3+ and ResNet-101 as baseline and backbone, respectively. Results on more datasets can be found at the Supp. Table 10 illustrates the results and the

Table 10. Ablation study of the proposed ShapeConv on the NYUDv2-40 dataset. RGB, Detph and HHA denote the inputs consisting of RGB images, depth images and HHA images. Setting a.RGB b.RGB+Depth c.RGB+DepthF d.RGB+HHA e.RGB+HHAF f.RGB+Depth+ShapeConv g.RGB+Depth+ShapeConvF h.RGB+HHA+ShapeConv i.RGB+HHA+ShapeConvF

key observations from this table are as follows: 1) The input features with HHA outperform the Depth images for the baseline and ours; 2) Replacing the vanilla convolution with ShapeConv leads to considerable performance improvements on both Depth and HHA; 3) The multi-scale setting in testing phase brings more performance gains; 4) Cascading the ShapeConv with HHA and multi-scale testing can achieve the best result.

5. Conclusion In this paper, we propose a ShapeConv layer to effectively leverage the depth information for RGB-D semantic segmentation. In particular, an input patch is firstly decomposed into two components, i.e., shape and base, which are then decorated with two corresponding learnable weights before the convolution is applied. We have conducted extensive experiments on several challenging indoor RGB-D semantic segmentation benchmarks and promising experimental results can be observed. Moreover, it is worth noting that our ShapeConv introducing no additional computation or memory in comparison with the vanilla convolution during inference, yet with superior performance. In fact, the shape-component is inherent in the local geometry and highly relevant to the semantics in images. In the future, we plan to expand the application scope to other geometry entities, such as point clouds, where the shapebase decomposition is more challenging due to the additional degree of freedom.

Acknowledgments. This work is supported by the National Key Research and Development Program of China grant No.2017YFB1002603, the National Science Foundation of China General Program grant No.61772317, 61772318 and 62072284, “Qilu” Young Talent Program of Shandong University, and the Research Intern Program of Alibaba Group.
