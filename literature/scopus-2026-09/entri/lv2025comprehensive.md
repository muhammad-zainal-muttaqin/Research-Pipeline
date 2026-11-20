# A Comprehensive Review of Deep Learning in Computer Vision for Monitoring Apple Tree Growth and Fruit Production

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lv2025comprehensive` |
| Judul asli | A Comprehensive Review of Deep Learning in Computer Vision for Monitoring Apple Tree Growth and Fruit Production |
| Penulis | Lv, Meng; Xu, Yi-Xiao; Miao, Yu-Hang; Su, Wen-Hao |
| Tahun | 2025 |
| Venue | Sensors |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | apple |

## Tautan Akses
- PDF: [lv2025comprehensive.pdf](../pdf/lv2025comprehensive.pdf)
- DOI resmi: https://doi.org/10.3390/s25082433

## Gambaran Umum

Tinjauan ini mengkaji penggunaan pembelajaran mendalam (*deep learning*) bersama visi komputer untuk memantau pertumbuhan pohon apel dan produksi buah. Apel memiliki nilai gizi dan ekonomi tinggi; produksi tahunan mencapai 87,2 juta ton dan menempati urutan ketiga setelah pisang dan semangka. Masalahnya, sebagian besar kegiatan kebun masih dikerjakan manual sehingga membutuhkan tenaga kerja dan biaya pembelajaran besar. Algoritma pembelajaran mesin konvensional memiliki kompleksitas komputasi tinggi dan kecepatan rendah, sehingga sukar memenuhi kebutuhan deteksi waktu nyata. Penulis meninjau lebih dari 100 literatur dalam tujuh tahun terakhir dan membagi aplikasinya menjadi lima bidang: hama, penyakit pada daun, buah, dan batang, pertumbuhan organ, prediksi hasil, serta cacat pascapanen.

Literatur yang ditinjau memakai citra RGB, termal inframerah, spektral, dan pencitraan 3D, dengan tiga kelas model: deteksi (YOLO dan Faster R-CNN), klasifikasi (AlexNet dan ResNet), serta segmentasi (SegNet dan Mask R-CNN). Pembelajaran mendalam mengekstrak fitur secara otomatis dari data skala besar melalui jaringan saraf konvolusional (CNN) dan arsitektur berbasis *transformer*, sehingga mengatasi keterbatasan fitur buatan yang sensitif terhadap cahaya, latar, dan oklusi. Mekanisme asosiasi lintas pandang penting pada penghitungan buah: YOLOV7-CA menggabungkan mekanisme *self-attention* dari *vision transformer* (ViT) dengan YOLOV7 dan memakai filter Kalman untuk mencocokkan buah antarframe; model lain memakai ByteTrack atau Deep OC-SORT untuk pelacakan guna menghindari penghitungan ganda. Untuk dahan, informasi kedalaman dari sensor Kinect V2 dipakai memisahkan latar sebelum segmentasi SegNet; untuk cacat awal, pencitraan *structured-illumination reflectance imaging* (SIRI) menghasilkan citra arus searah (DC), arus bolak-balik (AC), dan rasio (RT), sementara citra inframerah dekat (NIR) dipakai untuk memar yang tersembunyi di bawah kulit.

Berbagai angka dilaporkan dari kajian yang ditinjau. Pada deteksi hama, AlexNet mencapai akurasi 99,53%, EfficientDet 98,00%, dan kombinasi *density curvature weighted Gaussian mixture model* (GMM-DC) dengan Mask R-CNN yang diperbaiki mencapai 96,75% untuk hama yang menempel; PestLite berbasis YOLOv5 menaikkan mAP sebesar 2,80% dengan jumlah parameter turun dari 7,03 juta menjadi 6,09 juta. Pada penyakit, DCGAN-DCNN mencapai akurasi 99,99%, DMCNN dengan dua ruang warna RGB-HSV mencapai 99,50%, YOLOX-ASSANano mencapai mAP 91,08%, dan ELM-YOLOv8n mencapai mAP 96,70% dengan parameter serta beban komputasi turun masing-masing 44,80% dan 39,50%. Metode semi-terarah PSPNet-SA mempertahankan mIoU 97,50%, 97,40%, dan 96,50% hanya dengan 1/2, 1/4, dan 1/8 data berlabel.

Pada organ tanaman, model CNN deteksi bunga apel mencapai akurasi 92,70%, YOLOv5s-ShuffleNetv2-Ghost mencapai mAP 91,80%, model SegNet dengan data kedalaman dari Kinect V2 mencapai akurasi 92,00–94,00% untuk dahan, dan arsitektur ResNet-18 mencapai mAP rata-rata 97,00%. Untuk prediksi hasil, kombinasi MS-MLP, CNN, segmentasi *watershed*, dan *circular Hough transform* menghasilkan skor F1 86,10%, model CNN mencapai 97,83%, YOLOV7-CA mencapai mAP 91,30% dengan skor F1 0,85, dan AppleYOLO yang menggabungkan YOLOv8 dengan Deep OC-SORT mencapai mAP 98,50%. Pada cacat pascapanen, CNN mencapai akurasi 99,00%, ASDINet mencapai AP 98,80% dengan skor F1 97,75%, YOLOv8n pada citra SIRI mencapai 99,12%, dan klasifikasi berbasis NIR mencapai 99,33–100,00% dibandingkan 74,66–86,00% untuk RGB.

Batasan yang dinyatakan penulis mencakup biaya dan waktu anotasi dataset yang besar, terutama untuk segmentasi yang menandai setiap piksel; kecenderungan model mengalami overfitting pada dataset kecil atau satu varietas sehingga generalisasi rendah di lapangan; serta kualitas citra yang dipengaruhi resolusi kamera dan perangkat keras. Penghitungan buah masih terganggu oleh tumpang tindih dan penghitungan ganda, dan prediksi hasil skala besar terkendala perlunya hitungan manual sebagai acuan. Sebagian besar kajian masih memakai citra RGB dan berhenti di laboratorium, dengan sedikit bukti penerapan nyata; penulis menyerukan penggunaan pembelajaran semi-terarah, dataset multivarietas, pencitraan multispektral, UAV, serta optimasi ringan seperti kuantisasi, pemangkasan, dan distilasi pengetahuan untuk perangkat seluler. Penulis menyatakan tidak ada konflik kepentingan; pendanaan berasal dari Yayasan Ilmu Pengetahuan Alam Nasional Tiongkok dan program pengembangan bakat Universitas Pertanian Tiongkok.
