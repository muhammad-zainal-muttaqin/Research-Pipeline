# 141 - Indoor Segmentation and Support Inference from RGBD Images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `silberman2012nyu` |
| Judul asli | Indoor Segmentation and Support Inference from RGBD Images |
| Penulis | Nathan Silberman, Derek Hoiem, Pushmeet Kohli, Rob Fergus |
| Tahun | 2012 |
| Venue | European Conference on Computer Vision (ECCV 2012), LNCS 7576, hlm. 746–760 |
| Tema | Dataset |

## Tautan Akses
- **DOI (Springer, PDF akses terbuka):** https://doi.org/10.1007/978-3-642-33715-4_54
- **Halaman proyek dataset (unduhan data beranotasi, data mentah, dan perangkat pengolah):** https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html
- **Google Scholar:** https://scholar.google.com/scholar?q=Indoor%20Segmentation%20and%20Support%20Inference%20from%20RGBD%20Images
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Indoor%20Segmentation%20and%20Support%20Inference%20from%20RGBD%20Images&sort=relevance

## Gambaran Umum

Makalah ini memiliki dua kontribusi. Pertama, NYU Depth v2: dataset citra RGB-D (citra warna yang tiap pikselnya berpasangan dengan nilai kedalaman) untuk adegan dalam ruang — 1.449 citra 640×480 beranotasi padat per piksel dari 464 adegan di tiga kota Amerika Serikat, memuat 35.064 objek dari 894 kelas, dengan label instans dan anotasi relasi dukungan fisik. Kedua, metode yang menguraikan adegan menjadi lantai, dinding, permukaan penyangga, dan region objek, sekaligus menginferensi objek mana yang menyangga objek lain.

Dataset ini menjadi tolok ukur standar untuk segmentasi semantik RGB-D dan estimasi kedalaman dalam ruang.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum 2012, pemahaman adegan dalam ruang dikerjakan dari satu citra RGB. Metode *geometric context* (Hoiem dkk., 2005) mengklasifikasikan region ke kategori geometris; metode tata letak ruangan mencari batas dinding dan lantai. Pendekatan satu citra tersandung geometri: orientasi lantai dan bidang besar sulit ditentukan dari warna saja. Selain itu, label objek tidak menyatakan hubungan fisik antarobjek, padahal hubungan semacam "cangkir ditopang buku" diperlukan robotika. Karya terdekat (Gupta dkk., ECCV 2010) menginferensi dukungan dengan heuristik fisika untuk adegan luar ruang, bukan ruangan dalam yang penuh objek kecil dan oklusi (tutup-menutup antarobjek).

Microsoft Kinect (2010) membuat citra RGB-D murah, tetapi dataset awalnya belum memadai sebagai tolok ukur: NYU indoor generasi pertama (Silberman dan Fergus, 2011) hanya memuat 67 adegan, dan dataset Berkeley (Karayev dkk., 2011) hanya melabeli beberapa objek per adegan. Belum ada dataset dalam ruang dengan anotasi padat per piksel untuk ribuan citra beserta relasi fisiknya; domain luar ruang pada tahun yang sama justru memperoleh tolok ukur berkendara (bab 144, KITTI).

## Ide Utama

Gagasan pertama: bangun dataset yang jauh lebih besar dan lebih beragam, rekam dengan Kinect, lalu anotasi secara padat — bukan hanya kelas objek per piksel, tetapi juga nomor instans dan relasi dukungan antarregion. Anotasi ini membuat dukungan fisik pertama kalinya dapat dipelajari dan dievaluasi dari data.

Gagasan kedua: dalam ruang, kedalaman menyelesaikan soal geometri, warna menyelesaikan soal penampilan. Metode yang diusulkan memakai kedalaman untuk memperoleh struktur 3D ruangan, memakai struktur itu bersama fitur warna untuk menyegmentasi objek, lalu menginferensi relasi dukungan secara global dengan pemrograman integer. Dukungan tidak dimodelkan per kelas objek, melainkan lewat empat *kelas struktur* — Ground (lantai), Structure (dinding, langit-langit, kolom), Furniture (perabot besar), dan Prop (objek kecil yang mudah dibawa) — karena peran fisik region lebih menentukan pola dukungannya daripada nama objeknya.

## Cara Kerja Langkah demi Langkah

### Akuisisi dan Anotasi Dataset

Data direkam dengan kamera RGB dan kedalaman Kinect pada 464 adegan rumah tinggal dan komersial, mencakup 26 jenis adegan (kamar tidur, dapur, kantor). Dari 435.103 bingkai video, 1.449 bingkai dipilih manual agar beragam dan tidak mirip; tiap bingkai berupa pasangan citra RGB dan peta kedalaman teregistrasi 640×480. Anotasi padat per piksel dikerjakan lewat platform kerja kerumunan Amazon Mechanical Turk: tiap piksel diberi label kelas, dan objek sejenis dibedakan dengan nomor instans (*cup 1*, *cup 2*). Relasi dukungan ditandai sebagai triplet [Ri, Rj, tipe]: Ri region yang ditopang, Rj region penopang, dan tipe menyatakan dukungan dari bawah (cangkir di atas meja) atau dari belakang (gambar pada dinding). Peta kedalaman mentah Kinect berlubang pada bayangan inframerah dan permukaan mengilap atau gelap; lubang diisi dengan skema *colorization* Levin dkk. (2004). Dirilis pula data mentah (407.024 bingkai tanpa label) dan *toolbox* MATLAB.

### Menemukan Struktur Geometri Ruangan

Normal permukaan (vektor tegak lurus permukaan) dihitung per piksel dengan memasang bidang *least squares* pada piksel tetangga. Ruangan lalu diluruskan ke koordinatnya berdasarkan asumsi *Manhattan world*: sebagian besar permukaan searah salah satu dari tiga arah yang saling tegak lurus. Kandidat arah utama diperoleh dari garis lurus citra RGB dan modus *mean-shift* (puncak kepadatan) normal; tripel ortogonal berskor tertinggi dipilih, lalu seluruh titik 3D diputar agar lantai menghadap ke atas. Prosedur ini membawa 80% lantai ke dalam rentang 5° dari vertikal, dibandingkan 5% tanpa pelurusan.

Bidang besar (lantai, dinding, permukaan meja) diusulkan dengan RANSAC, algoritme yang memasang model pada sampel acak titik dan menghitung piksel yang cocok (*inlier*); hanya bidang dengan sedikitnya 2.500 *inlier* yang dipertahankan. Keanggotaan piksel ditentukan dengan *graph cut alpha expansion*: energinya mengukur kecocokan posisi 3D dan normal terhadap bidang (rasio log probabilitas *inlier* terhadap *outlier*), ditambah pemulusan sensitif gradien warna. Piksel berkedalaman terukur diberi bobot 1, hasil pengisian lubang 0,25, dan tanpa kedalaman 0.

### Segmentasi Hierarkis

Citra dipecah secara berlebihan (*oversegmentation*) menjadi 1.000–2.000 *superpixel* dengan algoritme *watershed* di atas peta batas Pb (peta kekuatan batas probabilistik), dipaksa konsisten dengan bidang 3D agar region tidak melintasi batas dinding. Region digabung berpasangan secara iteratif oleh *classifier boosted decision tree* yang memprediksi peluang dua region berasal dari instans yang sama, memakai fitur warna-posisi 2D ditambah fitur 3D (perbedaan bidang, orientasi permukaan, beda kedalaman). Penggabungan berhenti ketika tidak ada pasangan dengan peluang satu-instans di atas 50%.

### Inferensi Dukungan dengan Pemrograman Integer

Untuk tiap region i dicari tiga hal: Si (penopangnya — region lain, region tersembunyi di luar bingkai, atau lantai), Ti (tipe dukungan: dari bawah atau dari belakang), dan Mi (kelas strukturnya). Energi gabungan memuat dua suku *likelihood* dari classifier regresi logistik — classifier dukungan memakai fitur kedekatan 3D, bentuk, dan lokasi 3D, sedangkan classifier kelas struktur memakai fitur SIFT (deskriptor penampilan lokal), histogram normal, dimensi *bounding box* (kotak pembatas) 2D/3D, histogram warna, dan kedalaman relatif — serta empat prior: prior transisi dari frekuensi dukungan antarkelas struktur, konsistensi dukungan (penopang harus dekat secara 3D), konsistensi lantai (region non-lantai wajib ditopang), dan konsistensi lantai global (region lantai harus terendah).

Penugasan terbaik diformulasikan sebagai program integer dengan variabel biner untuk setiap kombinasi region, penopang, tipe, dan kelas struktur. Karena persoalan ini NP-hard (sukar dipecahkan tepat), kendala kebulatan direlaksasi menjadi program linear yang dipecahkan solver Gurobi; solusi pecahan dibulatkan ke penugasan berpeluang terbesar. Pada 1.394 dari 1.449 citra, *duality gap* relaksasi ini nol — solusinya praktis optimal.

Alur lengkap dari masukan ke keluaran diringkas pada diagram berikut.

```
masukan: citra RGB 640x480 + peta kedalaman (mentah dan hasil inpainting)
   |                                   |
   v                                   v
garis lurus RGB               normal permukaan per piksel
   |                                   |
   +----> 3 arah dominan ortogonal (asumsi Manhattan world)
             |
             v
      rotasi ke koordinat ruangan (lantai menghadap atas)
             |
             v
      RANSAC: proposal bidang besar (>= 2.500 piksel inlier)
             |
             v
      graph cut: label bidang tiap piksel -----> struktur 3D ruangan
             |
             v
watershed pada batas Pb: 1.000-2.000 superpiksel (konsisten dgn bidang)
             |
             v
penggabungan hierarkis (classifier: fitur RGB/posisi + fitur 3D)
             |
             v
      region objek R1..Rn
             |
             v
inferensi dukungan (program integer -> relaksasi LP, solver Gurobi)
  Si = penopang; Ti = {dari bawah, dari belakang};
  Mi = {Ground, Furniture, Prop, Structure}
  prior: transisi, konsistensi dukungan, lantai, lantai global
             |
             v
keluaran: segmentasi objek + relasi dukungan antarregion
```

Diagram menunjukkan dua jalur masukan bertemu pada pelurusan ruangan; tiap tahap bergantung pada tahap sebelumnya, sehingga galat awal diteruskan ke hilir.

## Eksperimen dan Hasil

Kualitas segmentasi diukur dengan *overlap* rata-rata: untuk tiap region kebenaran dicari region hasil paling tumpang tindih, lalu skor dirata-rata, dalam versi berbobot luas piksel dan tanpa bobot. Tabel berikut memuat angka naskah tercetak dan koreksi resminya; angka tercetak sekitar 2 poin terlalu tinggi akibat *bug* evaluasi.

| Fitur | Tercetak (berbobot/tanpa bobot) | Koreksi resmi (berbobot/tanpa bobot) |
|---|---|---|
| RGB saja | 52,5 / 48,7 | 50,3 / 44,0 |
| Kedalaman saja | 55,9 / 47,3 | 53,7 / 43,0 |
| RGB-D | 62,7 / 52,7 | 60,1 / 47,9 |
| RGB-D + dukungan | 63,4 / 53,7 | 60,7 / 48,8 |
| RGB-D + dukungan + kelas struktur | 63,9 / 54,1 | 61,1 / 49,1 |

Interpretasinya konsisten pada kedua versi: RGB-D mengungguli modalitas tunggal dengan margin sekitar 10 poin terhadap RGB saja dan 7 poin terhadap kedalaman saja (versi koreksi), sedangkan dukungan dan kelas struktur menambah sekitar 1 poin — penalaran fisik memperbaiki segmentasi sekalipun kecil.

Inferensi dukungan dibandingkan dengan tiga *baseline*: aturan bidang citra (penopang = region tepat di bawahnya), aturan kelas struktur, dan classifier dukungan saja. Metriknya proporsi region yang penopangnya benar, dalam varian *type agnostic* (tipe boleh salah) dan *type aware* (tipe harus benar). Pada region kebenaran, model energi penuh (LP) mencapai 75,9% *agnostic* dan 72,6% *aware*, mengungguli baseline terkuat (aturan kelas struktur, 72,0/57,7) terutama pada varian *aware* dengan margin 15 poin — penalaran global menentukan jenis dukungan, bukan hanya pasangannya. Pada region segmentasi otomatis, selisihnya lebih tajam: LP 55,1/54,5 melawan 45,8/41,4 dan 22,1/19,4; aturan sederhana kehilangan sebagian besar kinerjanya ketika region tidak ideal.

Akurasi kelas struktur 79,9% pada region kebenaran dan 58,7% pada region segmentasi; LP hanya mengubahnya tipis (80,3% dan 58,6%). Analisis kegagalan menemukan dua galat berantai: karpet yang dikenali sebagai lantai membuat dinding dan tempat tidur seolah ditopang karpet, dan kelas struktur yang salah menyeret inferensi dukungan ikut salah.

## Kelebihan dan Keterbatasan

Kelebihan utama ada pada data: NYU Depth v2 adalah dataset RGB-D dalam ruang pertama dengan anotasi padat per piksel, label instans, dan relasi dukungan pada skala ribuan citra. Dari sisi metode, pelurusan ruangan dan kelas struktur memasukkan pengetahuan fisik ke segmentasi secara terukur, dan formulasi program integernya praktis diselesaikan karena relaksasinya terbukti ketat.

Keterbatasan yang diakui penulis: metode bergantung pada kualitas segmentasi awal (akurasi dukungan turun dari 75,9% menjadi 55,1% pada region otomatis), kegagalan deteksi lantai merambat ke seluruh inferensi, dan kedalaman Kinect yang berderau menurunkan kualitas normal permukaan. Secara konseptual, asumsi *Manhattan world* membatasi metode pada tata letak ortogonal. Dari sisi rekayasa, 1.449 citra terbukti kecil untuk melatih model pembelajaran mendalam satu dekade kemudian, dan domainnya murni dalam ruang.

## Kaitan dengan Bab Lain

Dalam klaster Dataset, bab 144 ([KITTI](./144%20-%202012%20-%20KITTI%20-%20Dataset.md)) adalah tolok ukur sezaman untuk domain berlawanan — luar ruang, LiDAR, kendaraan — sedangkan bab ini menutup sisi dalam ruang. Bab ini diwarisi dua penerus langsung: bab 142 ([SUN RGB-D](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md)) yang memperluas skala dan ragam sensor, dan bab 143 ([ScanNet](./143%20-%202017%20-%20ScanNet%20-%20Dataset.md)) yang menaikkan skala ke rekonstruksi 3D; bab 145 ([nuScenes](./145%20-%202020%20-%20nuScenes%20-%20Dataset.md)) dan bab 146 ([Microsoft COCO](./146%20-%202014%20-%20Microsoft%20COCO%20-%20Dataset.md)) meneruskan gagasan tolok ukur beranotasi padat ke domain mengemudi otonom dan deteksi umum.

Di luar klaster Dataset, NYU Depth v2 menjadi data evaluasi de facto: bab 051 ([FuseNet](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)) dan hampir seluruh klaster Segmentasi RGB-D (052–061) melaporkan akurasi pada 1.449 citra ini, sedangkan bab 062 ([Eigen dkk.](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20(Eigen%20dkk.)%20-%20Estimasi%20Kedalaman.md)) dan klaster Estimasi Kedalaman menjadikannya tolok ukur kedalaman monokular dalam ruang.

## Poin untuk Sitasi

Kutip dengan kunci `silberman2012nyu`. Ringkasan yang aman dikutip: "Silberman dkk. (ECCV 2012) memperkenalkan NYU Depth v2, 1.449 citra RGB-D dalam ruang beranotasi padat dari 464 adegan, dengan label instans untuk 35.064 objek dari 894 kelas dan anotasi relasi dukungan fisik; makalah yang sama mengusulkan penguraian adegan berbasis struktur 3D dan inferensi dukungan yang diformulasikan sebagai program integer."

Catatan verifikasi: (1) angka segmentasi tercetak sekitar 2 poin terlalu tinggi akibat bug evaluasi; gunakan koreksi resmi dari halaman proyek. (2) Angka dukungan (75,9/72,6 dan 55,1/54,5) berasal dari Tabel 2 naskah. (3) Naskah menyebut 1.449 citra dipilih dari 435.103 bingkai; halaman proyek menyebut 407.024 bingkai mentah tanpa label — keduanya berbeda cakupan.

---

## Teks Sumber Lengkap (ekstraksi PDF, dirapikan)

Teks isi paper direkonstruksi dari PDF: baris terbungkus disatukan menjadi paragraf; tabel angka, label gambar, rumus lepas, nomor halaman, dan daftar pustaka dihilangkan. Rangkuman terkurasi di atas tetap acuan utama.

<!--SRC-->
Courant Institute, New York University Department of Computer Science, University of Illinois at Urbana-Champaign 3 Microsoft Research, Cambridge Abstract. We present an approach to interpret the major surfaces, objects, and support relations of an indoor scene from an RGBD image. Most existing work ignores physical interactions or is applied only to tidy rooms and hallways. Our goal is to parse typical, often messy, indoor scenes into floor, walls, supporting surfaces, and object regions, and to recover support relationships. One of our main interests is to better understand how 3D cues can best inform a structured 3D interpretation. We also contribute a novel integer programming formulation to infer physical support relations. We offer a new dataset of 1449 RGBD images, capturing 464 diverse indoor scenes, with detailed annotations. Our experiments demonstrate our ability to infer support relations in complex scenes and verify that our 3D scene cues and inferred support lead to better object segmentation.

Introduction

Traditional approaches to scene understanding aim to provide labels for each object in the image. However, this is an impoverished description since labels tell us little about the physical relationships between objects, possible actions that can be performed, or the geometric structure of the scene. Many robotics and scene understanding applications require a physical parse of the scene into objects, surfaces, and their relations. A person walking into a room, for example, might want to find his coffee cup and favorite book, grab them, find a place to sit down, walk over, and sit down. These tasks require parsing the scene into different objects and surfaces – the coffee cup must be distinguished from surrounding objects and the supporting surface for example. Some tasks also require understanding the interactions of scene elements: if the coffee cup is supported by the book, then the cup must be lifted first. In this paper, our goal is to provide such a physical scene parse: to segment visible regions into surfaces and objects and to infer their support relations. In particular, we are interested in indoor scenes that reflect typical living conditions. Challenges include the well-known difficulty of object segmentation, prevalence of small objects, and heavy occlusion, which are all compounded by the mess and disorder that are common in lived-in rooms. What makes interpretation possible at all is the rich geometric structure: most rooms are composed of large planar surfaces, such as the floor, walls, and table tops, and objects can often A. Fitzgibbon et al. (Eds.): ECCV 2012, Part V, LNCS 7576, pp. 746–760, 2012. c Springer-Verlag Berlin Heidelberg 2012

be interpreted in relation to those surfaces. We can better interpret the room by rectifying our visual data with the room’s geometric structure. Our approach, illustrated in Fig. 1, is to first infer the overall 3D structure of the scene and then jointly parse the image into separate objects and estimate their support relations. Some tasks, such as estimating the floor orientation or finding large planar surfaces are much easier with depth information, which is easy to acquire indoors. But other tasks, such as segmenting and classifying objects require appearance based cues. Thus, we use depth cues to sidestep the common geometric challenges that bog down single-view image-based approaches, enabling a more detailed and accurate geometric structure. We are then able to focus on properly leveraging this structure to jointly segment the objects and infer support relations, using both image and depth cues. One of our innovations is to classify objects into structural classes that reflect their physical role in the scene: “ground”; “permanent structures” such as walls, ceilings, and columns; large “furniture” such as tables, dressers, and counters; and “props” which are easily movable objects. We show that these structural classes aid both segmentation and support estimation. To reason about support, we introduce a principled approach that integrates physical constraints (e.g. is the object close to its putative supporting object?) and statistical priors on support relationships (e.g. mugs are often supported by tables, but rarely by walls). Our method is designed for real-world scenes that contain tens or hundred of objects with heavy occlusion and clutter. In this setting, interfaces between objects are often not visible and thus must be inferred. Even without occlusion, limited image resolution can make support ambiguous, necessitating global reasoning between image regions. Real-world images also contain significant variation in focal length. While wide-angle shots contain many objects, narrow-angle views can also be challenging as important structural elements of the scene, such as the floor, are not observed. Our scheme is able to handle these situations by inferring the location of invisible elements and how they interact with the visible components of the scene. 1.1

Related Work

Our overall approach of incorporating geometric priors to improve scene interpretation is most related to a set of image-based single-view methods (e.g. [1–7]). Our use of “structural classes”, such as “furniture” and “prop”, to improve segmentation and support inference relates to the use of “geometric classes” [1] to segment objects [8] or volumetric scene parses [3, 5–7]. Our goal of inferring support relations is most closely related to Gupta et al. [6], who apply heuristics inspired by physical reasoning to infer volumetric shapes, occlusion, and support in outdoor scenes. Our 3D cues provide a much stronger basis for inference of support, and our dataset enables us to train and evaluate support predictors that can cope with scene clutter and invisible supporting regions. Russell and Torralba [9] show how a dataset of user-annotated scenes can be used to infer 3D structure and support; our approach, in contrast, is fully automatic.

1. Major Surfaces 2. Surface Normals 3. Align Point Cloud

Fig. 1. Overview of algorithm. Our algorithm flows from left to right. Given an input image with raw and inpainted depth maps, we compute surface normals and align them to the room by finding three dominant orthogonal directions. We then fit planes to the points using RANSAC and segment them based on depth and color gradients. Given the 3D scene structure and initial estimates of physical support, we then create a hierarchical segmentation and infer the support structure. In the surface normal images, the absolute value of the three normal directions is stored in the R, G, and B channels. The 3D planes are indicated by separate colors. Segmentation is indicated by red boundaries. Arrows point from the supported object to the surface that supports it.

Our approach to estimate geometric structure from depth cues is most closely related to Zhang et al. [10]. After estimating depth from a camera on a moving vehicle, Zhang et al. use RANSAC to fit a ground plane and represent 3D scene points relative to the ground and direction of the moving vehicle. We use RANSAC on 3D points to initialize plane fitting but also infer a segmentation and improved plane parameters using a graph cut segmentation that accounts for 3D position, 3D normal, and intensity gradients. Their application is pixel labeling, but ours is parsing into regions and support relations. Others, such as Silberman et al. [11] and Karayev et al. [12] use RGBD images from the Kinect for object recognition, but do not consider tasks beyond category labeling. To summarize, the most original of our contributions is the inference of support relations in complex indoor scenes. We incorporate geometric structure inferred from depth, object properties encoded in our structural classes, and data-driven scene priors, and our approach is robust to clutter, stacked objects, and invisible supporting surfaces. We also contribute ideas for interpreting geometric structure from a depth image, such as graph cut segmentation of planar surfaces and ways to use the structure to improve segmentation. Finally, we offer a new large dataset with registered RGBD images, detailed object labels, and annotated physical relations.

Several Kinect scene datasets have recently been introduced. However, the NYU indoor scene dataset [11] has limited diversity (only 67 scenes); in the Berkeley Scenes dataset [12] only a few objects per scene are labeled; and others such as [13, 14] are designed for robotics applications. We therefore introduce a new Kinect dataset1 , significantly larger and more diverse than existing ones. The dataset consists of 1449 RGBD images2 , gathered from a wide range of commercial and residential buildings in three different US cities, comprising 464 different indoor scenes across 26 scene classes.A dense per-pixel labeling was obtained for each image using Amazon Mechanical Turk. If a scene contained multiple instances of an object class, each instance received a unique instance label, e.g. two different cups in the same image would be labeled: cup 1 and cup 2, to uniquely identify them. The dataset contains 35,064 distinct objects, spanning 894 different classes. For each of the 1449 images, support annotations were manually added. Each image’s support annotations consists of a set of 3tuples: [Ri , Rj , type] where Ri is the region ID of the supported object, Rj is the region ID of the supporting object and type indicates whether the support is from below (e.g. cup on a table) or from behind (e.g. picture on a wall). Examples of the dataset are found in Fig 7 (object category labels not shown).

Indoor scenes are usually arranged with respect to the orthogonal orientations of the floor and walls and the major planar surfaces such as supporting surfaces, floor, walls, and blocky furnishings. We treat initial inference of scene surfaces as an alignment and segmentation problem. We first compute surface normals from the depth image. Then, based on surface normals and straight lines, we find three dominant and orthogonal scene directions and rotate the 3D coordinates to be axis aligned with the principal directions. Finally, we propose 3D planes using RANSAC on the 3D points and segment the visible regions into one of these planes or background using graph cuts based on surface normals, 3D points, and RGB gradients. Several examples are shown in Fig. 2. We now describe each stage of this procedure in more detail. 3.1

We are provided with registered RGB and depth images, with in-painted depth pixels [15]. We compute 3D surface normals at each pixel by sampling surrounding pixels within a depth threshold and fitting a least squares plane. For each pixel we have an image coordinate (u, v), 3D coordinate (X, Y , Z), and surface normal (NX , NY , NZ ). Our first step is to align our 3D measurements to room coordinates, so that the floor points upwards (NY =1) and each wall’s normal 1 2

http://cs.nyu.edu/~ silberman/datasets/nyu_depth_v2.html 640 × 480 resolution. The images were hand selected from 435, 103 video frames, to ensure diverse scene content and lack of similarity to other frames.

Fig. 2. Scene Structure Estimation. Given an input image (a), we compute surface normals (b) and align the normals (c) to the room. We then use RANSAC to generate several plane candidates which are sorted by number of inliers (d). Finally, we segment the visible portions of the planes using graph cuts (e). Top row: a typical indoor scene with a rectangular layout. Bottom row: an scene with many oblique angles; floor orientation is correctly recovered.

is in the X or Z direction. Our alignment is based on the Manhattan world assumption[16], that many visible surfaces will be along one of three orthogonal directions. To obtain candidates for the principal directions, we extract straight lines from the image and compute mean-shift modes of surface normals. Straight line segments are extracted from the RGB image using the method described by Kosecka et al. [17] and the 3D coordinates along each line are recorded. We compute the 3D direction of each line using SVD to find the direction of maximum variance. Typically, we have 100-200 candidates of principal directions. For each candidate that is approximately in the Y direction, we sample two orthogonal candidates and compute the score of the triple as follows: S(v1 , v2 , v3 ) =

We generate potential wall, floor, support, and ceiling planes using a RANSAC procedure. Several hundred points along the grid of pixel coordinates are sampled, together with nearby points at a fixed distance (e.g., 20 pixels) in the horizontal and vertical directions. While thousands of planes are proposed, only planes above a threshold (2500) of inlier pixels after RANSAC and non-maximal suppression are retained. To determine which image pixels correspond to each plane, we solve a segmentation using graph cuts with alpha expansion based on the 3D points X, the surface normals N and the RGB intensities I of each pixel. Each pixel i is assigned a plane label yi = 0..Np for Np planes (yi = 0 signifies no plane) to minimize the following energy:

The unary terms f3d and fnorm encode whether the 3D values and normals r(dist|inlier) , at a pixel match those of the plane. Each term is defined as log PPr(dist|outlier) the log ratio of the probability of the distance between the pixel’s 3D position or normal compared to that of the plane, given that the pixel is an inlier or outlier. The probabilities are computed using histograms with 100 bins using the RANSAC inlier/outlier estimates to initialize. The unary terms are weighted by αi , according to whether we have directly recorded depth measurements (αi = 1), inpainted depth measurements (αi = 0.25), or no depth measurements (αi = 0) at each pixel. 1(.) is an indicator function. The pairwise term fpair (yi , yj , I) = 2 β1 + β2 ||Ii − Ij || enforces gradient-sensitive smoothing. In our experiments, β1 = 1 and β2 = 45/μg , where μg is the average squared difference of intensity values for pixels connected within N8 , the 8-connected neighborhood.

In order to classify objects and interpret their relations, we must first segment the image into regions that correspond to individual object or surface instances. Starting from an oversegmentation, pairs of regions are iteratively merged based on learned similarities. The key element is a set of classifiers trained to predict whether two regions correspond to the same object instance based on cues from the RGB image, the depth image, and the estimated scene structure (Sec. 3). To create an initial set of regions, we use the watershed algorithm applied to Pb boundaries, as first suggested by Arbeleaz [18]. We force this oversegmentation to be consistent with the 3D plane regions described in Sec. 3, which primarily helps to avoid regions that span wall boundaries with faint intensity edges. We also experimented with incorporating edges from depth or surface orientation maps, but found them unhelpful, mostly because discontinuities in depth or surface orientation are usually manifest as intensity discontinuities.

Fig. 4. Segmentation Examples. We show two examples of hierarchical segmentation. Starting with roughly 1500 superpixels (not shown), our algorithm iteratively merges regions based on the likelihood of two regions belonging to the same object instance. For the final segmentation, no two regions have greater than 50% chance of being part of the same object.

Our oversegmentation typically provides 1000-2000 regions, such that very few regions overlap more than one object instance. For hierarchical segmentation, we adapt the algorithm and code of Hoiem et al. [8]. Regions with minimum boundary strength are iteratively merged until the minimum cost reaches a given threshold. Boundary strengths are predicted by a trained boosted decision tree classifier as P(yi = yj |xsij ), where yi is the instance label of the ith region and xsij are paired region features. The classifier is trained using similar RGB and position features 3 to Hoiem et al. [8], but the “geometric context” features are replaced with ones using more reliable depthbased cues. These proposed 3D features encode regions corresponding to different planes or having different surface orientations or depth differences are likely to belong to different objects. Both types of features are important: 3D features help differentiate between texture and objects edges, and standard 2D features are crucial for nearby or touching objects.

Given an image split into R regions, we denote by Si : i = 1..R the hidden variable representing a region’s physical support relation. The basic assumption made by our model is that every region is either (a) supported by a region visible in the image plane, in which case Si ∈ {1..R}, (b) supported by an object not visible in the image plane, Si = h, or (c) requires no support indicating that the region is the ground itself, Si = g. Additionally, let Ti encode whether region i is supported from below (Ti = 0) or supported from behind (Ti = 1). When inferring support, prior knowledge of object types can be reliable predictors of the likelihoods of support relations. For example, it is unlikely that a piece of fruit is supporting a couch. However, rather that attempt to model 3

A full list of features can be found in the supplementary material.

support in terms of object classes, we model each region’s structure class Mi , where Mi can take on one of the following values: Ground (Mi = 1), Furniture (Mi = 2), Prop (Mi = 3) or Structure (Mi = 4). We map each object in our densely labeled dataset to one of these four structure classes. Props are small objects that can be easily carried; furniture are large objects that cannot. Structure refers to non-floor parts of a room (walls, ceiling, columns). We map each object in our labeled dataset to one of these structure classes. We want to infer the most probable joint assignment of support regions S = {S1 , ...SR }, support types T ∈ {0, 1}R and structure classes M ∈ {1..4}R. More formally, {S∗ , T∗ , M∗ } = arg max P (S, T, M|I) = arg min E(S, T, M|I), S,T,M

where E(S, T, M|I) = − log P (S, T, M|I) is the energy of the labeling. The posterior distribution of our model factorizes into likelihood and prior terms as P (S, T, M|I) ∝

i=1 S where Fi,S are the support features for regions i and Si , and Ds is a Support i S Relation classifier trained to maximize P (Fi,S |Si , Ti ). FiM are the structure feai tures for region i and Dm is a Structure classifier trained to maximize P (FiM |Mi ). The specifics regarding training and choice of features for both classifiers are found in sections 5.3 and 5.4, respectively. The prior EP is composed of a number of different terms, and is formally defined as: R

(6) The transition prior, ψT C , encodes the probability of regions belonging to different structure classes supporting each other. It takes the following form:

where Hib and HSt i are the lowest and highest points in 3D of region i and Si respectively, as measured from the ground, and V (i, Si ) is the minimum horizontal distance between regions i and Si . The ground consistency term ψGC (Si , Mi ) has infinite cost if Si = g ∧ Mi = 1 and 0 cost otherwise, enforcing that all non-ground regions must be supported. The global ground consistency term ψGGC (M) ensures that the region taking the floor label is lower than other regions in the scene. Formally, it is defined as: R R

The support likelihood Ds (eq. 5) and the support consistency ψSC (eq. 8) s terms of the energy are encoded in the IP objective though coefficients θi,j . The structure class likelihood Dm (eq. 5) and the global ground consistency ψGGC m (eq. 9) terms are encoded in the objective through coefficients θi,u . The transition w prior ψT C (eq. 7) is encoded using the parameters θi,j,u,v . Constraints 11 and 12 ensure that each region is assigned a single support, type and structure label. Constraint 13 satisfies the Ground Consistency φGC term. Constraints 14 and 15 are marginalization and consistency constraints.

Finally, constraint 16 ensure that all indicator variables take integral values. It is NP-hard to solve the integer program defined in equations 10-16. We reformulate the constraints as a linear program, which we solve using Gurobi’s LP solver, by relaxing the integrality constraints 16 to: u,v si,j , mi,u , wi,j ∈ [0, 1],

Fractional solutions are resolved by setting the most likely support, type and structure class to 1 and the remaining values to zero. In our experiments, we found this relation to be tight in that the duality gap was 0 in 1394/1449 images. 5.3

Our support features capture individual and pairwise characteristics of regions. s Such characteristics are not symmetric: feature vector Fi,j would be used to determine whether i supports j but not vice versa. Geometrical features encode proximity and containment, e.g. whether one region contains another when projected onto the ground plane. Shape features are important for capturing characteristics of different supporting objects: objects that support others from below have large horizontal components and those that support from behind have large vertical components. Finally, location features capture the absolute 3d locations of the candidate objects.4 S To train Ds , a logistic regression classifier, each feature vector Fi,j is paired S with a label Y ∈ {1..4} which indicates whether (1) i is supported from below by j, (2) i is supported from behind by j, (3) j represents the ground or (4) no relationship exists between the two regions. Predicting whether j S ) such that is the ground is necessary for computing Ds (Si = g, Ti = 0; Fi,g

Experiments

To evaluate our segmentation algorithm, we use the overlap criteria from [8]. As shown in Table 1, the combination of RGB and Depth features outperform each set of features individually by margins of 10% and 7%, respectively, using the area-weighted score. We also performed two additional segmentation experiments 4

A full list of features can be found in the supplementary material.

in which at each stage of the segmentation, we extracted and classified support and structure class features from the intermediate segmentations and used the support and structure classifier output as features for boundary classification. The addition of these features both improve segmentation performance with Support providing a slightly larger gain. 6.2

Because the support labels are defined in terms of ground truth regions, we must map the relationships onto the segmented regions. To avoid penalizing the support inference for errors in the bottom up segmentation, the mapping is performed as follows: each support label from the ground truth region [RiGT , RjGT , T ] is replaced with a set of labels [RaS1 , RbS1 , T ]...[RaSw , RbSw , T ] where the overlap between supported regions (RiGT ,RaSw ) and supporting regions, (RjGT ,RbSw ) exceeds a threshold (.25). We evaluate our support inference model against several baselines: – Image Plane Rules: A Floor Classifier is trained in order to assign Si = g properly. For the remaining regions: if a region is completely surrounded by another region in the image plane, then a support-from-behind relationship is assigned to the pair with the smaller region as the supported region. Otherwise, for each candidate region, choose the region directly below it as its support from below. – Structure Class Rules: A classifier is trained to predict each region’s structure class. If a region is predicted to be a floor, Si = g is assigned. Regions predicted to be of Structure class Furniture or Structure are assigned the support of the nearest floor region. Finally, Props are assigned support from below by the region directly beneath them in the image plane. – Support Classifier: For each region in the image, we infer the likelihood of support between it and every other region in the image using Ds and assign each region the most likely support relation indicated by the support classifier score. The metric used for evaluation is the number of regions for which we predict a correct support divided by the total number of regions which have a support

label. We also differentiate between Type Agnostic accuracy, in which we consider a predicted support relation correct regardless of whether the support type (below or from behind) matched the label and Type Aware accuracy in which only a prediction of the correct type is considered a correct support prediction. We also evaluate each method on both the ground truth regions and regions generated by the bottom up segmentation. Results for support classification are listed in Table 2. When using the ground truth regions, the Image Plane Rules and Structure Class Rules perform well Table 2. Results of the various approaches to support inference. Accuracy is measured by total regions whose support is correctly inferred divided by the number of labeled regions. Type Aware accuracy penalized incorrect support type and Type Agnostic does not. Predicting Support Relationships Region Source Ground Truth Segmentation Algorithm Type Agnostic Type Aware Type Agnostic Type Aware Image Plane Rules 63.9 50.7 22.1 19.4 Structure Class Rules 72.0 57.7 45.8 41.4 Support Classifier 70.1 63.4 45.8 37.1 Energy Min (LP) 75.9 72.6 55.1 54.5

Fig. 5. Comparison of support algorithms. Image Plane Rules incorrectly assigns many support relationships. Structure Class Rules corrects several support relationships for Furniture objects but struggles with Props. The Support classifier corrects several of the Props but infers an implausible Furniture support. Finally, our LP solution correctly assigns most of the support relationships. (→ : support from below, : support from behind, + : support from hidden region. Correct support predictions in green, incorrect in red. Ground in pink, Furniture in Purple, Props in Blue, Structure in Yellow, Grey indicates missing structure class label. Incorrect structure predictions are striped.) Ground

Fig. 7. Examples of support and structure class inference with the LP solution. → : support from below, : support from behind, + : support from hidden region. Correct support predictions in green, incorrect in red. Ground in pink, Furniture in Purple, Props in Blue, Structure in Yellow, Grey indicates missing structure class label. Incorrect structure predictions are striped.

given their simplicity. Indeed, when using ground truth regions, the Structure Class Rules prove superior to the support classifier alone, demonstrating the usefulness of the Structure categories. However, both rule-based approaches cannot handle occlusion well nor are they particularly good at inferring the type of support involved. When considering the support type, our energy based model improves on the Structure Class Rules by 9% and 17% when using the ground truth and segmented regions, respectively, demonstrating the need to take into account a combination of global reasoning and discriminative inference. Visual examples are shown in Fig 7. They demonstrate that many objects, such as the right dresser in the row3, column 3 and the chairs in row 5, column 1, are supported by regions that are far from them in the image plane, necessitating non-local inference. One of the main stumbling blocks of the algorithm is incorrect floor classification as show in the 3rd image of the last row. Incorrectly labeling the rug as the floor creates a cascade of errors since the walls and bed rely on this as support rather than using the true floor. Additionally, incorrect structure class prediction can lead to incorrect support inference, such as the objects on the table in row 4, column 1. 6.3

To evaluate the structure class prediction, we calculate both the overall accuracy and the mean diagonal of the confusion matrix. As 6 indicates, the LP solution makes a small improvement over the local structure class prediction. Structure class accuracy often struggles when the depth values are noisy or when the segmentation incorrectly merges two regions of different structure class.

Conclusion

We have introduced a new dataset useful for various tasks including recognition, segmentation and inference of physical support relationships. Our dataset is unique in the diversity and complexity of depicted indoor scenes, and we provide an approach to parse such complex environments through appearance cues, room-aligned 3D cues, surface fitting, and scene priors. Our experiments show that we can reliably infer the supporting region and the type of support, especially when segmentations are accurate. We also show that initial estimates of support and major surfaces lead to better segmentation. Future work could include inferring the full extent of objects and surfaces and categorizing objects. Acknowledgements. This work was supported in part by NSF Awards 0904209, 09-16014 and IIS-1116923. The authors would also like to thank Microsoft for their support. Part of this work was conducted while Rob Fergus and Derek Hoiem were visiting researchers at Microsoft Research Cambridge.
