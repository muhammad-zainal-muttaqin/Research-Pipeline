# 058 - CMX: Cross-Modal Fusion for RGB-X Semantic Segmentation with Transformers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2023cmx` |
| Judul asli | CMX: Cross-Modal Fusion for RGB-X Semantic Segmentation with Transformers |
| Penulis | Jiaming Zhang, Huayao Liu, Kailun Yang, Xinxin Hu, Ruiping Liu, Rainer Stiefelhagen |
| Tahun | 2023 |
| Venue | IEEE Transactions on Intelligent Transportation Systems (T-ITS) |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2203.04838
- **Repositori kode resmi:** https://github.com/huaaaliu/RGBX_Semantic_Segmentation
- **Google Scholar:** https://scholar.google.com/scholar?q=CMX%3A%20Cross-Modal%20Fusion%20for%20RGB-X%20Semantic%20Segmentation%20with%20Transformers
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=CMX%3A%20Cross-Modal%20Fusion%20for%20RGB-X%20Semantic%20Segmentation%20with%20Transformers&sort=relevance

## Gambaran Umum

CMX adalah kerangka fusi lintas-modal untuk segmentasi semantik RGB-X. Segmentasi semantik adalah pelabelan kelas objek pada setiap piksel citra, dan RGB-X berarti citra warna (RGB) digabungkan dengan satu modalitas pelengkap X, misalnya kedalaman (*depth*), termal, polarisasi, *event*, atau LiDAR. Berbeda dari metode sebelumnya yang dirancang khusus untuk satu pasangan modalitas, CMX memakai satu arsitektur untuk semua kombinasi. Kuncinya dua modul: *Cross-Modal Feature Rectification Module* (CM-FRM) yang saling mengoreksi fitur kedua modalitas, dan *Feature Fusion Module* (FFM) yang menukar konteks jarak jauh lewat *cross-attention* sebelum fitur digabung.

Kerangka ini diuji pada sembilan dataset lintas lima jenis kombinasi modalitas, dan mencapai hasil terbaik pada masanya di semuanya: 56,9% mIoU pada NYU Depth V2 (RGB-D), 59,7% pada MFNet (RGB-T), 92,6% pada ZJU-RGB-P (RGB-P), dan 64,3% pada KITTI-360 (RGB-L). Penulis juga membangun tolok ukur RGB-*Event* baru dari dataset EventScape, tempat CMX mengungguli lebih dari sepuluh model pembanding. Kode sumber dirilis terbuka.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pada sistem transportasi cerdas dan kendaraan otonom, segmentasi citra RGB sering gagal ketika dua objek berwarna atau bertekstur serupa, atau ketika pencahayaan buruk. Sensor pelengkap menutupi kelemahan itu: kedalaman memberi batas geometri, termal membedakan objek lewat radiasi inframerah, polarisasi membantu pada permukaan mengilap, dan LiDAR memberi informasi spasial. Masalahnya, karakteristik setiap sensor berbeda, sehingga selama ini setiap kombinasi modalitas memerlukan rancangan jaringan tersendiri.

Metode fusi sebelumnya terbagi dua golongan. Golongan pertama melebur kedua modalitas pada tahap masukan dengan operator khusus modalitas tertentu. Golongan kedua memakai dua *backbone* (jaringan pengekstrak fitur) terpisah, lalu menggabungkan fitur secara searah lewat perhatian kanal — misalnya ACNet (bab 054) dan SA-Gate (bab 055) yang dirancang untuk RGB-D. Penulis CMX mengamati bahwa keduanya tidak berpindah dengan baik: unggul di RGB-D, tetapi kurang memuaskan pada data RGB-T, karena interaksinya searah dan hanya menyentuh level kanal fitur. Selain itu, hampir semua metode memakai *backbone* CNN yang tidak memodelkan ketergantungan jarak jauh antarpiksel. Yang diperlukan adalah satu kerangka *modality-agnostic* (tidak terikat modalitas tertentu) dengan interaksi lintas-modal yang lebih lengkap.

## Ide Utama

Gagasan inti CMX adalah mengganti fusi searah menjadi **interaksi dua arah yang berlapis**. Sebelum digabung, fitur RGB dan fitur X saling mengoreksi: fitur satu modalitas dipakai mengkalibrasi fitur modalitas lainnya, karena modalitas yang satu sering memuat informasi yang dapat menekan derau pada pasangannya. Koreksi dilakukan pada dua dimensi sekaligus, yaitu kanal (fitur apa yang penting) dan spasial (lokasi mana yang penting). Setelah dikoreksi, kedua fitur bertukar konteks global melalui perhatian silang antarurutan piksel, barulah dilebur menjadi satu peta fitur.

Secara mekanis: masukan berupa sepasang citra RGB dan citra X; keluaran berupa peta segmentasi per piksel. Yang berubah dibanding pendahulunya adalah letak dan arah interaksinya — tidak lagi satu kali dan satu arah, melainkan di setiap tahap *backbone*, dua arah, pada level peta fitur maupun level urutan.

## Cara Kerja Langkah demi Langkah

### Arsitektur Dua Aliran

CMX memakai dua cabang *encoder* Transformer yang identik: cabang RGB dan cabang X. *Encoder*-nya adalah MiT (*Mix Transformer*) dari SegFormer, *backbone* Transformer hierarkis berfitur multi-resolusi dalam empat tahap; Transformer memroses citra sebagai urutan *patch* dan menghubungkan posisi berjauhan lewat *self-attention* (pembobotan tiap elemen urutan terhadap semua elemen lain). Di antara dua tahap berdekatan dipasang CM-FRM, dan pada setiap tahap dipasang FFM. Empat peta hasil fusi diteruskan ke *decoder* MLP ringan ala SegFormer (dimensi *embedding* 512) yang menghasilkan peta segmentasi akhir. Seluruhnya dilatih *end-to-end*. Karena tidak ada komponen spesifik modalitas, cabang X menerima kedalaman, termal, polarisasi, *event*, atau LiDAR tanpa perubahan arsitektur.

Alur data antarkomponen pada satu tahap backbone:

```
 RGB ─► MiT tahap i ─► fitur RGB ─┐
                                 ├─► CM-FRM ─► fitur terkoreksi
   X ─► MiT tahap i ─► fitur X ──┘      (dua arah, silang)
                                            │
                                            ▼
                                      MiT tahap i+1

 tiap tahap: fitur terkoreksi ─► FFM ─► peta gabungan Hi x Wi x Ci
                                                   │
     decoder MLP ◄── empat peta gabungan (4 skala) ◄┘
           │
           ▼
     peta segmentasi per piksel
```

Diagram menunjukkan dua hal: CM-FRM bekerja dua arah (fitur RGB mengoreksi fitur X dan sebaliknya) sebelum tahap backbone berikutnya, dan FFM menghasilkan satu peta gabungan per tahap untuk dikumpulkan decoder.

### Cross-Modal Feature Rectification Module (CM-FRM)

CM-FRM mengoreksi fitur pada dua dimensi. Pada **koreksi kanal**, fitur kedua modalitas (masing-masing H×W×C) diringkas lewat *global average pooling* (rata-rata seluruh posisi) dan *global max pooling* (nilai maksimum seluruh posisi) sekaligus, menghasilkan empat vektor yang digabung menjadi 4C angka. Sebuah MLP (jaringan *fully connected* berlapis) diikuti sigmoid (pemetaan ke rentang 0–1) mengubahnya menjadi 2C bobot kanal, yang dipecah dua. Bobot ini lalu menimbang fitur modalitas *pasangannya* per kanal: fitur X yang tertimbang menjadi koreksi bagi fitur RGB, dan sebaliknya.

Pada **koreksi spasial**, kedua fitur digabung lalu dilewatkan melalui dua konvolusi 1×1 (konvolusi titik per titik yang mencampur kanal tanpa menggeser piksel) dengan aktivasi ReLU di antaranya, diakhiri sigmoid, menghasilkan dua peta bobot H×W yang menimbang fitur pasangan per piksel. Keluaran CM-FRM bersifat residual: fitur asli ditambah 0,5 kali koreksi kanal dan 0,5 kali koreksi spasial (λ_C = λ_S = 0,5). Sebagai contoh, pada tahap pertama backbone fitur berukuran sekitar 160×160×64; koreksi kanal meringkasnya menjadi 64 bobot, koreksi spasial menghasilkan peta 160×160 bobot.

### Feature Fusion Module (FFM)

FFM bekerja dalam dua tahap. Tahap pertama, **pertukaran informasi**, mempertahankan kedua cabang tetapi saling menukar konteks. Fitur H×W×C diratakan menjadi urutan N×C dengan N = H×W, lalu diproyeksikan linier menjadi vektor residual dan vektor interaktif. Pada *self-attention* biasa, peta perhatian berukuran N×N — untuk N = 25.600 posisi berarti ratusan juta elemen. CMX memakai *cross-attention* efisien: setiap cabang menghitung konteks global G = KᵀV berukuran C_head×C_head (orde puluhan kali puluhan), lalu keluaran perhatian satu cabang dihitung dengan mengalikan vektor interaktifnya dengan konteks global *cabang lain*. Fitur RGB dengan demikian diperkaya ringkasan global fitur X, dan sebaliknya, tanpa matriks N×N. Hasil perhatian digabung dengan vektor residual dan diproyeksikan kembali ke H×W×C, dengan beberapa *head* perhatian mengikuti backbone.

Tahap kedua, **peleburan**, menggabungkan kedua jalur menjadi H×W×2C, lalu konvolusi 1×1 mereduksinya kembali ke H×W×C. Sebuah konvolusi *depth-wise* 3×3 (konvolusi per kanal terpisah, murah secara komputasi) ditambahkan sebagai sambungan pintas agar informasi tetangga lokal ikut terserap saat peleburan.

### Representasi Data per Modalitas

Agar dapat diproses backbone yang sama, setiap modalitas diubah ke format tiga kanal. Kedalaman dikodekan sebagai HHA: tiga kanal geometri berisi disparitas horizontal, tinggi di atas tanah, dan sudut normal permukaan. Citra termal satu kanal cukup disalin tiga kali. Polarisasi dihitung dari empat citra sudut polarisasi (0°, 45°, 90°, 135°) melalui vektor Stokes, menghasilkan DoLP (*Degree of Linear Polarization*, derajat polarisasi linier) atau AoLP (*Angle of Linear Polarization*, sudut polarisasi linier). Data *event* — aliran kejadian perubahan intensitas asinkron — dipadatkan menjadi *voxel grid* (kisi volum) H×W×B dengan resolusi waktu dinaikkan enam kali lalu ditumpuk, lebih halus daripada representasi EventScape asli. Awan titik LiDAR diproyeksikan ke citra *range-view* 1408×376 dengan sudut pandang 90° mengikuti proyeksi lubang jarum.

### Pelatihan

Kedua backbone diinisialisasi bobot MiT terlatih ImageNet. Optimizer AdamW (*weight decay* 0,01) dipakai dengan laju belajar awal 6×10⁻⁵ dan jadwal *poly* (laju menurun mengikuti pangkat iterasi). Fungsi loss adalah *cross-entropy* per piksel. Augmentasi terbatas pada pembalikan horizontal acak dan penskalaan acak 0,5–1,75. Pengujian multi-skala pada NYU Depth V2 dan SUN-RGBD memakai skala {0,75; 1; 1,25} dengan pembalikan horizontal.

## Eksperimen dan Hasil

Metrik utama adalah mIoU (*mean Intersection over Union*): rata-rata rasio irisan terhadap gabungan antara piksel prediksi dan piksel kebenaran, dihitung per kelas lalu dirata-ratakan; semakin tinggi semakin baik, maksimal 100%. CMX dievaluasi pada sembilan dataset: lima RGB-D (NYU Depth V2, 1.449 citra 40 kelas; SUN-RGBD, 10.335 citra 37 kelas; Stanford2D3D, 70.496 citra 13 kelas; ScanNetV2, 20 kelas; Cityscapes RGB-D, 19 kelas), plus MFNet (RGB-T, 1.569 citra siang-malam), ZJU-RGB-P (RGB-P), EventScape (RGB-E), dan KITTI-360 (RGB-L, 19 kelas).

Hasil utamanya:

- NYU Depth V2: 56,9% mIoU dengan backbone MiT-B5; bahkan varian MiT-B2 (54,4%) sudah melampaui metode-metode sebelumnya.
- Stanford2D3D: 62,1% mIoU (MiT-B4), mengungguli ShapeConv (bab 057) yang berbasis ResNet-101.
- SUN-RGBD: di atas 52,0% mIoU (MiT-B4/B5), melampaui metode fusi masukan maupun fusi fitur.
- ScanNetV2: 61,3% mIoU (MiT-B2), tertinggi di antara metode RGB-D murni 2D; metode dengan supervisi titik 3D seperti BPNet masih lebih tinggi karena informasi tambahannya.
- Cityscapes: 82,6% mIoU (MiT-B4), tetapi fusi kedalaman hanya menambah 0,6 poin atas baseline RGB — tanda kinerja RGB di dataset ini mulai jenuh.
- MFNet (RGB-T): 59,7% mIoU (MiT-B4), naik 4,9–5,0 poin atas baseline RGB; kelas *person* naik lebih dari 11 poin IoU, dan pada citra malam hari perbaikan melebihi 7 poin dibanding 2,7–3,1 poin pada siang hari — bukti langsung manfaat koreksi modalitas saat RGB bermutu buruk.
- ZJU-RGB-P: 92,6% mIoU, lebih dari 6 poin di atas metode RGB-P terbaik sebelumnya; kelas kaca naik lebih dari 8 poin IoU.
- EventScape (RGB-E): tolok ukur baru berisi 4.077 citra latih dan 749 citra uji resolusi 512×256 dengan 12 kelas; CMX mencapai 64,28% mIoU dan menetapkan hasil terbaik di antara lebih dari sepuluh model yang diujikan.
- KITTI-360 (RGB-L): 64,3% mIoU.

Rentang hasil ini penting dibaca sebagai satu kesatuan: arsitektur yang sama, tanpa penyesuaian per modalitas, unggul pada kelima tugas — sesuatu yang tidak dicapai metode spesifik-modalitas saat dipindahkan ke luar pasangan modalitas rancangannya.

## Kelebihan dan Keterbatasan

Kelebihan CMX tiga lapis. Pertama, generalisasi: satu kerangka melayani lima modalitas pelengkap, sehingga sensor baru dapat dipakai tanpa merancang ulang jaringan. Kedua, interaksinya lengkap — koreksi kanal dan spasial pada peta fitur ditambah perhatian silang pada urutan — dan terbukti mengungguli fusi searah. Ketiga, kerangka ini efektif di atas backbone Transformer maupun CNN, dan disertai tolok ukur RGB-*Event* baru serta kode terbuka.

Keterbatasannya: (1) dua backbone penuh menggandakan biaya komputasi dan memori; dari sisi rekayasa, ini menyulitkan pemakaian pada perangkat kendaraan yang terbatas. (2) Manfaat fusi mengecil pada dataset yang RGB-nya sudah jenuh, terbukti dari tambahan hanya 0,6 poin pada Cityscapes. (3) Kualitas modalitas kedua tetap menentukan; koreksi dua arah berarti modalitas yang sangat bising berpotensi mengoreksi pasangannya ke arah yang keliru. (4) Secara konseptual, CMX *modality-agnostic* hanya pada level arsitektur — pra-pemrosesan tiap modalitas (HHA, DoLP/AoLP, *voxel grid*, *range-view*) tetap dirancang khusus per sensor.

## Kaitan dengan Bab Lain

CMX meneruskan garis fusi dua aliran yang dimulai [FuseNet (bab 051)](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md) dan disempurnakan [RedNet (bab 052)](./052%20-%202018%20-%20RedNet%20-%20Segmentasi%20RGB-D.md) serta [RDFNet (bab 053)](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md). Terhadap fusi berbasis perhatian [ACNet (bab 054)](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md) dan gerbang selektif [SA-Gate (bab 055)](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md), CMX sekaligus menjadi koreksi: interaksi searah keduanya diganti koreksi dua arah, dan keduanya tertinggal ketika dipindah ke RGB-T. [ShapeConv (bab 057)](./057%20-%202021%20-%20ShapeConv%20-%20Segmentasi%20RGB-D.md), metode fusi masukan spesifik-kedalaman, dilampaui CMX pada Stanford2D3D dan SUN-RGBD. Sebagai karya 2023, CMX seangkatan dengan [PGDENet (bab 059)](./059%20-%202023%20-%20PGDENet%20-%20Segmentasi%20RGB-D.md), dan kerangkanya menjadi acuan fusi RGB-X generik pada literatur sesudahnya.

## Poin untuk Sitasi

Kutip dengan kunci `zhang2023cmx`. Ringkasan yang aman dikutip: "CMX adalah kerangka fusi lintas-modal berbasis Transformer untuk segmentasi semantik RGB-X yang memakai koreksi fitur dua arah (CM-FRM) dan fusi berbasis *cross-attention* (FFM); satu arsitektur yang sama mencapai hasil terbaik pada sembilan dataset lintas lima kombinasi modalitas, antara lain 56,9% mIoU pada NYU Depth V2 dan 59,7% pada MFNet." Angka-angka di atas bersumber dari naskah arXiv v5 (versi T-ITS) dan repositori resmi. Sebelum sitasi formal, verifikasi ulang ke naskah terbit: volume/nomor/halaman jurnal (tercatat 24/12/14679–14694), nilai ablasi bobot λ dan representasi polarisasi-*event*, serta angka 64,28% RGB-*Event* yang diambil dari repositori, bukan naskah.
