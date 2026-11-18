# CIAFNet: An RGB-D Cross-Modal Interaction and Adaptive Fusion Network for Camellia oleifera Fruit Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2026ciafnet` |
| Judul asli | CIAFNet: An RGB-D Cross-Modal Interaction and Adaptive Fusion Network for Camellia oleifera Fruit Detection |
| Penulis | Chen, Yan; Yang, Chengxin; Yuan, Chao; Lu, Yiming; Fu, Dandan; Fang, Yinghui; Liu, Shuman; Ai, Hui |
| Tahun | 2026 |
| Venue | Agriculture Switzerland |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | camellia |

## Tautan Akses
- PDF: [chen2026ciafnet.pdf](../pdf/chen2026ciafnet.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture16171884

## Gambaran Umum

Studi ini mengatasi hambatan akurasi deteksi buah *Camellia oleifera* hanya dengan citra RGB di kebun alami. Oklusi daun yang parah, variasi skala yang besar, dan struktur latar yang kompleks menyebabkan fitur tampilan RGB saja sulit membedakan buah dari daun, latar, dan buah yang bertumpang tindih. Penelitian sebelumnya banyak mengandalkan reorganisasi fitur tampilan, sehingga tetap terbatas ketika RGB tidak cukup memisahkan target. Penulis mengusulkan CIAFNet, jaringan deteksi dwialur RGB-D, untuk memanfaatkan informasi struktural dari peta kedalaman sebagai pelengkap tampilan. Tiga tujuan dinyatakan: menguji apakah pseudo-depth dari Depth Anything V2 memberi informasi struktural tambahan, menilai kinerja CIAFNet pada data RGB–pseudo-depth serta adaptasinya ke kedalaman terukur D435i, dan mengevaluasi potensi deteksi CIAFNet sebagai antarmuka visual untuk pelokalan 3D relatif.

Dua himpunan data dibangun. Himpunan kebun alami berisi 1.758 citra RGB yang diambil dengan iPhone 13 pada musim panen 2024 di Xianning, Hubei, China, dengan 12.496 instan buah yang diberi anotasi kotak ikat manual dalam format YOLO; pembagiannya adalah 1.231 citra latih, 264 validasi, dan 263 uji. Karena tidak ada sensor kedalaman saat pengambilan di lapangan, setiap citra dipasangkan dengan peta pseudo-depth yang dihasilkan offline oleh Depth Anything V2 dengan encoder ViT-L, lalu dipangkas pada persentil ke-1 sampai ke-99 dan dinormalisasi ke [0, 1] sebagai citra grayscale 8-bit. Himpunan terkontrol diperoleh dengan Intel RealSense D435i dan terdiri atas 352 pasangan RGB-D tersinkron dari buah tiruan dan ranting potong, bukan tanaman hidup, dengan pembagian 211/70/71. Arsitektur CIAFNet menggabungkan tiga komponen: C3k2_PartialNetBlock untuk ekstraksi fitur intra-modal yang ringan pada kedua cabang, modul CIDAF untuk interaksi dan fusi adaptif lintas modal, serta BiFPN yang diperkuat SC-EUCB pada neck untuk agregasi fitur multiskala.

Mekanisme utamanya terletak pada cara fusi memanfaatkan kesepakatan dan perbedaan lokal antara RGB dan kedalaman. C3k2_PartialNetBlock membagi kanal menjadi cabang konvolusi spasial dan cabang konteks mengikuti strategi PartialNetBlockV1, dengan rasio kanal parsial rp = 1/4 yang dipilih sebagai kompromi akurasi–efisiensi, bukan pengaturan yang memaksimalkan setiap metrik. CIDAF menyelaraskan fitur RGB dan kedalaman, secara eksplisit membangun representasi perbedaan dan kesepakatan untuk menghasilkan gerbang spasial adaptif bagi kedua alur, lalu menambahkan cabang residual untuk memulihkan informasi yang lemah akibat fusi tergerbang. Penulis menegaskan bahwa pseudo-depth DA-V2 bukan kedalaman metrik terukur, melainkan prior struktural relatif, dan karena setiap peta diturunkan secara deterministik dari citra RGB pasangannya, RGB dan pseudo-depth bukan dua modalitas yang independen secara statistik. Tahap fine-tuning kedua menyesuaikan model dengan kedalaman terukur D435i. Untuk pelokalan, pusat kotak ikat dipetakan ke piksel, kedalaman robust diambil sebagai median nilai valid di dalam ROI melingkar dengan faktor radius 0,5–0,8 yang bersifat empiris, lalu direproyeksikan dengan parameter intrinsik kamera menjadi koordinat kamera.

Pada himpunan uji kebun alami, CIAFNet mencapai 93,33% mAP@0,5 dengan 10,49 GFLOPs dan 3,80 juta parameter. Pada uji konsistensi perpindahan relatif dalam kondisi terkontrol, rata-rata galat absolut konsistensi sumbu X, Y, dan Z berturut-turut adalah 3,10 mm, 3,15 mm, dan 3,27 mm, dengan galat Euclidean 3D rata-rata 5,60 mm; angka ini dihitung dari 50 pengukuran tingkat target dalam 10 kelompok percobaan yang membandingkan perubahan koordinat dengan translasi kamera sebesar 100 mm per sumbu. Batasan yang dinyatakan penulis mencakup sifat pseudo-depth yang relatif dan bukan pengukuran absolut, ketidakindependenan statistik kedua alur, serta fakta bahwa evaluasi 3D hanya menguji konsistensi perubahan koordinat dalam kondisi terkontrol dan bukan akurasi penempatan absolut di kebun alami. Selain itu, data D435i memakai model buatan dan ranting potong, pilihan rp = 1/4 dan rentang radius ROI 0,5–0,8 bersifat empiris dan tidak diklaim universal, dan penulis tidak menyatakan perbandingan langsung dengan detektor lain pada angka mAP tersebut dalam ringkasan ini.

