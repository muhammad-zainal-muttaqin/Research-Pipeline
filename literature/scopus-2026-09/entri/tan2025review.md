# A Review of Research on Fruit and Vegetable Picking Robots Based on Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tan2025review` |
| Judul asli | A Review of Research on Fruit and Vegetable Picking Robots Based on Deep Learning |
| Penulis | Tan, Yarong; Liu, Xin; Zhang, Jinmeng; Wang, Yigang; Hu, Yanxiang |
| Tahun | 2025 |
| Venue | Sensors |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [tan2025review.pdf](../pdf/tan2025review.pdf)
- DOI resmi: https://doi.org/10.3390/s25123677

## Gambaran Umum

Tinjauan ini menyusun secara sistematis aplikasi pembelajaran mendalam pada robot pemanen buah dan sayur. Latar belakangnya adalah pemanenan yang masih mengandalkan tenaga kerja, bersifat padat karya, efisiensinya rendah, dan semakin mahal, sehingga otomatisasi menjadi kebutuhan. Penulis menilai kajian yang ada masih tersebar pada satu bidang saja, seperti deteksi objek, klasifikasi, atau perencanaan lintasan, dan belum merangkum secara menyeluruh penggunaan inti pembelajaran mendalam, hambatan teknologi, maupun arah pengembangannya. Tinjauan ini mencakup tiga kelompok teknologi, yaitu persepsi visual dan pengenalan sasaran, perencanaan lintasan dan kendali gerak, serta kendali cerdas ujung efektor.

Sumber dikumpulkan dari basis data Web of Science dengan kata kunci pembelajaran mendalam, pertanian, dan robot pemanen. Lebih dari 325 makalah diperoleh, lalu disaring menjadi 122 makalah yang dikaji lebih dalam, dengan fokus pada hasil setelah tahun 2020. Berbagai tanaman menjadi contoh, antara lain apel, tomat, jeruk, stroberi, asparagus putih, anggur, pir, kiwi, tomat ceri, jambu biji, dan kamomila tea. Data citra berasal dari kamera RGB, kamera kedalaman RGB-D, LiDAR, dan sensor inframerah, dengan metode yang mencakup jaringan saraf konvolusional (CNN), deteksi objek, segmentasi semantik, pembelajaran penguatan mendalam (DRL), dan fusi multimodal.

Pada persepsi visual dan pengenalan sasaran, tinjauan membedakan deteksi dua tahap (R-CNN, Fast R-CNN, Faster R-CNN, FPN) yang akurat tetapi lambat, dan deteksi satu tahap (seri YOLO, SSD) yang lebih cepat. Mekanisme perbaikannya mencakup fusi fitur multiskala, mekanisme atensi, dan desain kepala deteksi ringan, misalnya YOLOv5s-BC untuk apel dan YOLOv4-Tiny dengan konvolusi berlubang serta strategi tanpa *anchor* untuk jeruk. Segmentasi semantik dan instan memisahkan buah, tangkai, dan daun yang bertumpang tindih melalui FCN, U-Net, DeepLab, atau YOLACT. Angka yang dikutip dari kajian sumber meliputi YOLO5-Spear untuk asparagus putih dengan akurasi 97,8%, TC-YOLO untuk kamomila 47,23 FPS pada akurasi rata-rata 92,49%, MiniNet dengan waktu inferensi 6,5 ms, DualSeg untuk tangkai anggur dengan IoU 72,1% (lebih tinggi 3,9% dari model lain), DRG untuk tandan anggur bertumpang tindih dengan recall 89,2% dan presisi 87,5%, serta robot pemanen tomat dengan waktu 9 s per tandan dan tingkat keberhasilan 95%. Metrik yang dipakai adalah F1, presisi, recall, mAP, IoU, akurasi, dan kecepatan inferensi; seluruh angka merupakan hasil yang dilaporkan kajian yang dikutip, bukan dihitung ulang oleh tinjauan ini.

Pada perencanaan lintasan dan kendali gerak, pembelajaran penguatan mendalam memetakan pengamatan langsung menjadi aksi tanpa aturan buatan, dengan algoritma seperti DQN, DDPG, SAC, dan recurrent DDPG yang dipadukan LSTM. Strategi lain memodelkan penjangkauan kebun sebagai masalah pedagang keliling (TSP) lalu mengoptimalkannya dengan DQN yang dimodifikasi. Angka yang dikutip mencakup keberhasilan perencanaan lintasan bebas tabrakan recurrent DDPG sebesar 90,90%, dibandingkan DDPG konvensional 19,32% dan bi-directional RRT 88,18%, serta model DRL-MPC-GNN dengan F1 92,91% dan akurasi 96,82%. Pada kendali ujung efektor, pembelajaran mendalam dipakai untuk persepsi sentuhan, prediksi gaya cengkeram, dan penentuan sikap cengkeram optimal melalui fusi visual dan taktil, antara lain dengan jaringan berbasis Transformer dan Mask R-CNN pada gripper murah untuk memotong tangkai tanpa menyentuh daging buah.

Penulis menyatakan sejumlah batasan. Bentuk buah dan sayur beragam, lingkungan pemanenan berubah-ubah karena cahaya, naungan, tumpang tindih, dan perbedaan kematangan, sehingga generalisasi dan ketahanan algoritma masih perlu ditingkatkan. Sebagian besar sistem masih berupa versi laboratorium atau validasi skala kecil, dan banyak kajian terlalu mengejar metrik algoritmik seperti mAP dan IoU tanpa menilai kinerja sistem secara keseluruhan, termasuk efisiensi sinergi, konsumsi energi, dan biaya. Penulis juga mencatat kurangnya solusi sistematis untuk fusi banyak sensor, rekonstruksi visual 3D, dan kendali presisi gerakan memetik; sinkronisasi dan fusi data multimodal belum matang, perencanaan lintasan lengan masih bergantung pada aturan atau model yang ditetapkan sebelumnya, dan kebutuhan daya komputasi serta data besar menyulitkan penerapan pada komputasi tepi. Arah pengembangan yang diusulkan adalah peningkatan akurasi persepsi, kolaborasi banyak sensor, fusi data multimodal, kendali adaptif, dan interaksi manusia-komputer.
