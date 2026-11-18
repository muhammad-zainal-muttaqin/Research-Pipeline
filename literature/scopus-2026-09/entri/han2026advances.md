# Advances in Recognition Methods for Fruit and Vegetable Harvesting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `han2026advances` |
| Judul asli | Advances in Recognition Methods for Fruit and Vegetable Harvesting |
| Penulis | Han, Dianlei; Xu, Shixing; Zhou, Siyu; Zhu, Qingzhen; Chen, Xuegeng |
| Tahun | 2026 |
| Venue | Agriculture Switzerland |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [han2026advances.pdf](../pdf/han2026advances.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture16171924

## Gambaran Umum

Tinjauan ini mengangkat masalah biaya tenaga kerja tinggi, efisiensi panen rendah, dan tingkat kerusakan buah tinggi pada pemanenan buah dan sayur. Pengenalan target merupakan prasyarat robot pemanen: sistem harus memisahkan tanaman dari latar belakang, memperoleh pose tiga dimensi, dan menilai kematangan. Penulis menilai bahwa sistem yang ada masih lemah dalam ketahanan terhadap lingkungan kompleks, generalisasi, dan biaya penerapan, sehingga menghalangi pemakaian skala besar. Tujuan tinjauan adalah menganalisis prinsip, evolusi, dan tantangan pengenalan target, dengan tolok ukur kebutuhan operasional pemanenan, bukan sekadar metrik deteksi umum. Proses di hilir, seperti perencanaan gerak, berada di luar cakupan.

Data dan metode bersifat tinjauan sistematis, bukan percobaan tunggal. Pencarian memakai Web of Science dan Google Scholar untuk periode 2017–2026, dengan kata kunci yang mencakup tanaman target, metode pengenalan, dan strategi tertentu. Cakupan dibatasi pada jurnal Q1/Q2 dan makalah konferensi bereputasi; kriteria inklusi meliputi objek buah atau sayur, tugas pengenalan visual dalam pemanenan, serta metode berupa pemrosesan citra digital, pembelajaran mesin tradisional, atau pembelajaran mendalam. Dari hasil penyaringan, 131 makalah dimasukkan, terdiri atas 85 kajian langsung tentang pengenalan target panen dan 46 kajian pendukung tidak langsung. Satu pun nama tanaman, dataset tunggal, atau metrik milik tinjauan ini tidak dinyatakan karena tidak ada percobaan baru yang dijalankan.

Mekanisme pengenalan dibahas dalam tiga generasi. Pemrosesan citra digital memakai operator buatan untuk mengekstrak fitur warna, bentuk, dan tekstur, lalu melakukan segmentasi dan pengenalan; pembelajaran mesin tradisional (SVM, K-means, hutan acak) beralih ke fitur yang dipelajari dari data; pembelajaran mendalam memakai jaringan konvolusional end-to-end (YOLO, Faster R-CNN) dan arsitektur Transformer (DETR, Deformable-DETR, RT-DETRv2) yang menangkap konteks global lewat mekanisme perhatian diri. Penulis merangkum strategi perbaikan berupa augmentasi data dan transfer learning, penggantian backbone dan operator konvolusi efisien, reparameterisasi serta kompresi parameter untuk perangkat tepi, dan deteksi multiskala untuk mengatasi oklusi, objek kecil, dan pencahayaan ekstrem. Asosiasi lintas pandang dan penghitungan unik tidak dibahas sebagai mekanisme tersendiri.

Angka hasil yang dikutip berasal dari kajian-kajian dalam korpus tinjauan, bukan dari percobaan penulis sendiri, sehingga tidak ada acuan hitung milik tinjauan ini. Contoh yang dilaporkan: segmentasi apel pada kanal a CIE L*a*b* mencapai akurasi 76%, prasaringan stroberi dalam HSV lebih dari 98%, deteksi bayberry dengan YUV dan CLAHE 97,4%, dan apel hijau dengan perbedaan G-B adaptif 93,13% pada 108 citra. Pendekatan bentuk memberi akurasi 86% pada 38,9 FPS untuk mentimun dan peningkatan 15,03% serta 16,41% pada kondisi cahaya depan dan belakang; tekstur GLCM memberi 96,667% untuk klasifikasi jeruk dan 93,7% serta 94,2% untuk cacat dan parut apel. YOLO26 meningkatkan kecepatan inferensi CPU sebesar 43%. Metrik yang dipakai mencakup akurasi, FPS, dan mAP, tetapi penulis menegaskan bahwa metrik umum tersebut tidak langsung menggambarkan keberhasilan panen.

Batasan yang dinyatakan penulis meliputi biaya anotasi data tinggi, kesulitan menyeimbangkan akurasi dengan ukuran model, keterbatasan daya komputasi dan memori perangkat tepi, serta ketahanan yang belum cukup terhadap oklusi parah dan perubahan pencahayaan drastis. Pemrosesan citra digital memiliki daya pindah lintas skenario rendah dan plafon kinerja karena fitur dirancang manual; pembelajaran mesin tradisional dibatasi oleh rekayasa fitur, kutukan dimensionalitas, dan overfitting. Arah masa depan yang diusulkan adalah fusi fitur multimodal (inframerah dekat, kedalaman, termal, LiDAR), penerapan model pada perangkat tertanam lewat kuantisasi dan pemangkasan, pembelajaran mandiri dan lemah pengawasan, serta integrasi pengenalan buah dengan penentuan titik pemanenan.

