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
