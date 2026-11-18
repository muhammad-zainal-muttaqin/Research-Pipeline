# Instance Segmentation and Number Counting of Grape Berry Images Based on Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2023instance` |
| Judul asli | Instance Segmentation and Number Counting of Grape Berry Images Based on Deep Learning |
| Penulis | Chen, Yanmin; Li, Xiu; Jia, Mei; Li, Jiuliang; Hu, Tianyang; Luo, Jun |
| Tahun | 2023 |
| Venue | Applied Sciences Switzerland |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [chen2023instance.pdf](../pdf/chen2023instance.pdf)
- DOI resmi: https://doi.org/10.3390/app13116751

## Gambaran Umum

Kajian ini bertujuan melakukan segmentasi instansi dan menghitung jumlah setiap buah anggur secara terpisah, bukan hanya satu tandan utuh. Latar belakangnya adalah ukuran buah anggur menentukan mutu, pengkelasan, dan harga, sehingga penghitungan pada tingkat buah diperlukan untuk kebutuhan produksi. Kesulitan utama adalah bentuk buah yang tumbuh dalam tandan yang kompleks, saling menutupi, serta memiliki perbedaan ukuran dan warna yang besar. Penulis menguji apakah model segmentasi instansi dapat memisahkan setiap buah dan menghitung jumlahnya, termasuk pada buah yang tertutup.

Objek kajian adalah anggur *red globe*. Data terdiri atas 73 citra asli: 48 citra dari adegan peralatan otomatis di laboratorium dan 25 citra dari kebun alami. Kamera industri JAI AD-080 digunakan di laboratorium dengan jarak 50 cm dan sudut pandang 30 cm × 40 cm, sedangkan citra kebun diambil dengan iPhone 6s pada cahaya siang hari. Ukuran citra asli 1024 × 768 piksel untuk laboratorium dan 3024 × 4032 piksel untuk kebun, lalu diisi dengan latar hitam menjadi bujur sangkar dan diubah menjadi 512 × 512 piksel. Augmentasi berupa pembalikan horizontal, rotasi ±5°, dan penapisan Gaussian memperbanyak data menjadi 648 citra (438 laboratorium dan 210 kebun). Pembagian 8:1:1 menghasilkan 570 citra latih (380 laboratorium dan 190 kebun), 78 citra validasi (50 dan 28), serta 8 citra uji (5 laboratorium dan 3 kebun). Penulis membandingkan tiga model: Mask R-CNN dua tahap serta YOLACT dan SOLO satu tahap, dan memilih Mask R-CNN karena kinerjanya tertinggi.

Mekanismenya adalah sebagai berikut. Mask R-CNN memakai region proposal network (RPN) untuk menghasilkan kotak kandidat dan region of interest (ROI) untuk memetakan fitur, lalu tiga cabang memprediksi kelas, kotak pembatas, dan topeng segmentasi. Aresta dengan lapisan ResNet101 dan feature pyramid network (FPN) mengekstraksi fitur. Untuk mengatasi buah yang terlewat akibat kotak kandidat yang saling bertumpang tindih, penulis mengganti non-maximum suppression (NMS) dengan Soft-NMS berbobot linear: kotak bertumpang tindih tidak dibuang, melainkan skornya diturunkan, sehingga model Soft-MRBS mempertahankan buah yang tertutup. Penghitungan jumlah buah dilakukan dengan menghitung banyaknya kotak prediksi. Pelatihan memakai transfer learning dari bobot COCO, pengoptimal SGD, ukuran 512 × 512, batch 2, dan momentum 0,9; perangkatnya dua kartu NVIDIA GTX2080Ti dengan TensorFlow 2.1.0, Keras 2.1.6, Python 3.5.2, CUDA 10.1, OpenCV 3.4.2, dan PIL 8.1.2.

Pada percobaan awal, Mask R-CNN mencapai mIoU 85,98%, AP0,50 88,08%, AP0,75 82,04%, dan mAP 69,93% pada himpunan uji, lebih tinggi daripada SOLO (mIoU 83,47%, mAP 67,25%) dan YOLACT (mIoU 82,91%, mAP 66,59%). Setelah perbaikan Soft-MRBS, pada himpunan uji campuran nilainya menjadi mIoU 89,53%, AP0,50 90,06%, AP0,75 84,76%, dan mAP 74,23%, naik masing-masing 3,55%, 1,98%, 2,72%, dan 4,30% dibanding Mask R-CNN tanpa perbaikan. Skor mAP dihitung sebagai rata-rata AP pada ambang IoU 0,50 sampai 0,95 dengan langkah 0,05. Koefisien korelasi penghitungan buah naik dari 93,59% menjadi 96,13% (naik 2,54%). Uji generalisasi pada tiga varietas yang tidak dilatih, yaitu Kyoho, Xiahei, dan Red Rose, memberi mIoU 87,24% dan mAP 69,57%.

Batasan yang dinyatakan penulis: hasil pada adegan kebun alami lebih rendah daripada laboratorium karena latar belakang lebih kompleks; kegagalan deteksi terkonsentrasi pada daerah dengan buah yang tertutup dalam skala besar; dan data hanya tersedia atas permintaan penulis korespondensi. Kajian memakai hanya citra RGB dan sejumlah kecil sampel beranotasi rinci.

