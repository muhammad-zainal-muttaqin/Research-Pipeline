# Research progress and prospect of key technologies of fruit target recognition for robotic fruit picking

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2024research` |
| Judul asli | Research progress and prospect of key technologies of fruit target recognition for robotic fruit picking |
| Penulis | Liu, Shaohua; Xue, Jinlin; Zhang, Tianyu; Lv, Pengfei; Qin, Huanhuan; Zhao, Tianxing |
| Tahun | 2024 |
| Venue | Frontiers in Plant Science |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [liu2024research.pdf](../pdf/liu2024research.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2024.1423338

## Gambaran Umum

Tinjauan sistematis ini mengkaji pengenalan target buah untuk pemanenan robotik, dengan fokus pada visi mesin. Pemanenan manual masih dominan di kebun dan memiliki intensitas tenaga kerja tinggi serta efisiensi rendah, sementara kelangkaan tenaga kerja pertanian semakin parah. Lingkungan kebun yang tidak terstruktur menyulitkan pengenalan buah karena bayangan, pencahayaan tidak merata, oklusi, kondisi malam, tumpang tindih buah, serta buah yang warnanya menyerupai daun dan ranting. Penulis membedakan dua pendekatan, yaitu metode tradisional yang merancang ciri buatan dan metode pembelajaran mendalam berbasis convolutional neural network (CNN). Tinjauan memakai 181 referensi dari rentang 2006-2023 yang diperoleh melalui Web of Science, Elsevier ScienceDirect, dan sumber daring, serta merangkum 23 jenis buah.

Metode tradisional membangun ciri warna, bentuk, dan tekstur secara manual, lalu memakai perbedaan kroma, ambang batas, region growing, support vector machine (SVM), atau K-means untuk segmentasi. Berbagai penyesuaian dilakukan terhadap faktor gangguan, antara lain pencahayaan buatan dan koreksi gamma untuk bayangan serta kondisi malam, citra kedalaman dan point cloud untuk oklusi serta tumpang tindih, dan ciri gabungan untuk buah sewarnanya dengan lingkungan. Pendekatan pembelajaran mendalam bersifat end-to-end dan mempelajari ciri secara otomatis. Alurnya mencakup persiapan dataset, pemilihan detektor, perubahan struktur model, pelatihan transfer, pengujian, dan perbaikan berkelanjutan. Model diklasifikasikan menjadi deteksi dua tahap (R-CNN, Fast R-CNN, Faster R-CNN, Mask R-CNN), deteksi satu tahap (YOLO, SSD), deteksi tanpa anchor box, segmentasi (FCN, U-Net, SegNet, DeepLab, PSPNet, ENet), serta kompresi dan akselerasi jaringan melalui pemangkasan parameter, kuantisasi, dekomposisi peringkat rendah, distilasi pengetahuan, dan jaringan ringkas seperti MobileNet dan SqueezeNet.

Tabel hasil yang disajikan memperlihatkan kinerja pada berbagai buah dengan metrik mAP, AP, presisi, recall, F1, dan waktu deteksi. Pada metode tradisional, pengenalan tomat muda mencapai tingkat keberhasilan 77,6%, sedangkan jaringan GA-Elman untuk buah yang bertumpang tindih mencapai 88,67%. Deteksi dua tahap memberi mAP 98,5%, presisi 97,71%, recall 94,58%, dan F1 96,12% untuk jujube dan kenari hijau, dengan waktu 227 ms; Mask R-CNN pada apel menghasilkan presisi 97,31% dan recall 95,70%. Deteksi satu tahap memberi mAP 97,13%, presisi 96,36%, dan recall 96,03% dengan waktu 7,72 ms pada tomat memakai IMS-YOLO, serta mAP 96,30%, F1 91,80%, dan 27,8 gambar per detik pada apel memakai YOLOv3. Model ringkas berbasis MobileNet mencapai mAP 89,73%, waktu 68 ms, dan ukuran 46,5 MB pada longan. Angka rujukan pada dataset umum juga dicantumkan: YOLOv1 mencapai AP 63,4% pada PASCAL VOC2007, YOLOv2 78,6%, YOLOv3-spp 36,2% AP dan 60,6% AP50 pada 20 FPS, serta YOLOv4 43,5% AP dan 65,7% AP50 pada lebih dari 50 FPS di MS COCO.

Penulis menyatakan lima keterbatasan utama. Dataset kebun berskala besar dan terbuka belum tersedia; kajian yang ada memakai data kecil milik sendiri yang tidak mencakup seluruh kondisi gangguan, sehingga kinerja algoritma belum teruji secara memadai. Model tersedia umumnya berbasis pembelajaran terselia dan menjadi semakin kompleks, sehingga waktu hitung meningkat dan real-time menurun. Algoritma belum bersifat universal karena perlu menyiapkan dan melatih ulang dataset ketika jenis buah atau lingkungan berubah. Tumpang tindih dan oklusi buah belum memiliki solusi yang efektif. Stabilitas, generalisasi, dan ketahanan model terhadap faktor lingkungan yang acak masih rendah. Penulis mengarahkan penelitian berikutnya pada pembelajaran dengan pengawasan lemah atau tanpa pengawasan, kompresi model untuk perangkat tertanam, pengenalan tanpa anchor box untuk target kecil dan bertumpang tindih, perbaikan tata tanam kebun, serta peningkatan ketahanan model.

