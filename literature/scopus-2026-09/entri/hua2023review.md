# A Review of Target Recognition Technology for Fruit Picking Robots: From Digital Image Processing to Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hua2023review` |
| Judul asli | A Review of Target Recognition Technology for Fruit Picking Robots: From Digital Image Processing to Deep Learning |
| Penulis | Hua, Xuehui; Li, Haoxin; Zeng, Jinbin; Han, Chongyang; Chen, Tianci; Tang, Luxin; Luo, Yuanqiang |
| Tahun | 2023 |
| Venue | Applied Sciences Switzerland |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [hua2023review.pdf](../pdf/hua2023review.pdf)
- DOI resmi: https://doi.org/10.3390/app13074160

## Gambaran Umum

Tinjauan ini membahas teknologi pengenalan target untuk robot pemanen buah, mulai dari pengolahan citra digital hingga pembelajaran dalam. Pemanenan buah menyerap lebih dari 60% tenaga kerja, sehingga penuaan penduduk dan urbanisasi meningkatkan biaya panen. Robot pemanen memerlukan sistem visi yang mengenali buah secara cepat dan tepat. Pengolahan citra digital memakai ciri buatan berupa warna, bentuk geometris, dan tekstur; cara ini sulit mengatasi kebun yang kompleks karena perubahan pencahayaan mengubah ciri warna dan halangan dari ranting serta daun merusak ciri geometris. Pembelajaran dalam mengekstraksi ciri dari data latih dan memberikan akurasi serta ketahanan yang lebih tinggi. Rekonstruksi tiga dimensi juga diperlukan agar ujung efektor tidak bertabrakan dengan ranting.

Tinjauan ini merangkum literatur, bukan percobaan baru; pernyataan ketersediaan data menyatakan tidak ada data yang dilaporkan. Penulis menelusuri perkembangan sejak pengenalan visi mesin pada 1968, sistem visi pertama untuk apel pada 1977, hingga AlexNet pada 2012. Metode dikelompokkan menjadi pengolahan citra digital tradisional, deteksi pembelajaran dalam dua tahap dan satu tahap, segmentasi, serta rekonstruksi tiga dimensi. Buah yang dikaji mencakup nanas, apel, tomat, jeruk, limau, melon pahit, mangga, leci, kiwi, pisang, ceri, stroberi, jambu biji, jujube, teh minyak, dan markisa.

Mekanisme pengolahan citra tradisional memakai segmentasi ruang warna RGB, HSI, atau HSV, ciri geometris berupa tepi dan keliling, ciri tekstur seperti Gabor dan matriks kookurensi, serta gabungan beberapa ciri. Deteksi dua tahap memakai R-CNN dengan pencarian selektif sekitar 2.000 kandidat wilayah, AlexNet, dan SVM; Fast R-CNN memakai VGG16 dan SoftMax; Faster R-CNN memakai jaringan usulan wilayah. Deteksi satu tahap memakai YOLO dengan sel kisi dan kotak jangkar, FPN untuk prediksi banyak skala, serta SSD dengan filter konvolusi kecil. Segmentasi memakai FCN, DeepLab, SegNet, dan Mask R-CNN yang terdiri atas ResNet-FPN, jaringan usulan wilayah, serta cabang klasifikasi dan segmentasi instance. Rekonstruksi tiga dimensi memakai pencocokan stereo dua kamera atau sensor RGB-D melalui cahaya terstruktur maupun waktu tempuh, lalu memproses awan titik.

Angka hasil berikut berasal dari kajian primer yang dirangkum dan dihitung dengan metrik masing-masing, karena tinjauan ini tidak menghasilkan data baru. Pada metode tradisional, pengenalan nanas mencapai 90% saat cerah dan 60% saat mendung, segmentasi apel lebih dari 80% dengan galat 18% pada cahaya belakang, pengenalan jeruk berbasis tepi 90%, dan pengenalan jeruk hijau berbasis tekstur 75,3%. R-CNN mencatat mAP 53,3% pada VOC 2012; deteksi tiga organ tomat dengan Fast R-CNN mencatat AP 70,33%, 63,99%, dan 44,95%; Faster R-CNN mencatat 87,9% pada empat kelas apel dan 87,16% pada kiwi. YOLOv2 pada mangga hijau mencatat mAP 86,4%; YOLOv3 pada leci mencatat AP terendah 89,3% dengan waktu 0,026 detik; DY3TNet pada kiwi mencatat AP 90,05%. Pemangkasan kanal pada YOLOv4 mengurangi parameter 96,74% dengan mAP 97,31%. YOLOv5 dengan ResNet34 mencatat 95,07% pada jeruk, dan YOLOv5 yang dioptimasi CBAM mencatat mAP 98,23% pada jeruk hijau. SSD mencatat mAP 89,53% pada empat jenis buah dan 96,6% pada jujube. Mask R-CNN dengan ResNet-50 mencatat MIoU 89,85%, sedangkan varian dengan DenseNet mencatat akurasi 97,31% dan recall 95,70%. Rekonstruksi RGB-D pada apel mencatat akurasi 92,3%, 88,03%, dan 80,34% untuk apel, ranting, dan daun.

Penulis menyatakan sejumlah batasan. Ciri warna peka terhadap pencahayaan, ciri geometris rusak oleh halangan dan tumpang tindih, ciri tekstur peka terhadap derau kebun, dan gabungan ciri masih belum memenuhi kebutuhan lingkungan alami. Pembelajaran dalam belum sepenuhnya mengatasi tabrakan antara ujung efektor dan ranting. Faster R-CNN kurang baik untuk objek kecil, YOLO kurang tepat untuk objek rapat dan kecil atau yang ukurannya jauh berbeda dari data latih, dan SSD sulit memadukan ciri pada banyak skala. Segmentasi semantik kurang akurat pada lingkungan kompleks, sedangkan segmentasi instance memerlukan waktu komputasi lama sehingga sulit memenuhi kebutuhan waktu nyata. Rekonstruksi stereo peka terhadap pencahayaan dan halangan, sedangkan RGB-D memiliki akurasi rendah pada tepi objek, resolusi rendah, dan pengisian awan titik yang kurang pada ranting ramping. Penulis juga mencatat perlunya data berskala besar, model yang lebih umum, pengenalan pada buah yang berayun, serta model ringan untuk perangkat tepi.

