# Tomato Maturity Detection and Counting Model Based on MHSA-YOLOv8

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2023tomato` |
| Judul asli | Tomato Maturity Detection and Counting Model Based on MHSA-YOLOv8 |
| Penulis | Li, Ping; Zheng, Jishu; Li, Peiyuan; Long, Hanwei; Li, Mai; Gao, Lihong |
| Tahun | 2023 |
| Venue | Sensors |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [li2023tomato.pdf](../pdf/li2023tomato.pdf)
- DOI resmi: https://doi.org/10.3390/s23156701

## Gambaran Umum

Kajian ini mengatasi masalah penentuan tingkat kematangan dan pencacahan buah tomat yang masih dilakukan secara manual. Cara tersebut memakan waktu dan tenaga serta bergantung pada ketajaman penglihatan manusia. Penulis membangun model deteksi yang dapat membantu robot pemanen melakukan gradasi kematangan dan pencacahan secara daring maupun luring, sekaligus mendukung pengemasan terkelompok saat pemanenan mesin.

Data dikumpulkan di Taman Sains dan Teknologi Pertanian Cerdas Shouguang, Provinsi Shandong, China, dengan tomat Provence sebagai objek dan kamera RGB sebagai alat utama. Pengambilan citra sengaja memasukkan oklusi, bayangan, dan gangguan cahaya agar model tangguh terhadap kondisi lapang. Dataset terdiri atas 2.208 citra yang dibagi dengan rasio 7:1:2 untuk himpunan latih, validasi, dan uji. Anotasi memakai LabelImg 1.8.3. Model gradasi kematangan memakai tiga label, yaitu belum matang (IM), setengah matang (SM), dan matang (M), sedangkan model pencacahan memakai satu label "tomato" untuk seluruh buah. Pelatihan berjalan pada RTX 3090 24 GB dengan ukuran citra 640 × 640, 100 epoch, ukuran batch 8, learning rate 0,01, momentum 0,937, weight decay 0,0005, warmup 3 epoch, pengoptimal SGD, serta fungsi rugi VFL dan CIoU+DFL.

Mekanisme deteksi memakai YOLOv8 yang diperbaiki dengan mekanisme perhatian multi-kepala (MHSA). Modul MHSA ditempatkan di ujung jaringan ekstraksi fitur backbone, setelah SPPF, untuk memperkaya keragaman fitur yang diekstrak. Penulis lebih dulu membandingkan YOLOv8 dengan Faster R-CNN, YOLOv3, YOLOv4, YOLOv5, dan YOLOv7 pada dataset gradasi kematangan; YOLOv8 terpilih karena kinerjanya paling baik dengan ukuran model yang masih kecil. Arsitektur akhir memiliki 230 lapisan, 11.924.729 parameter, dan 29,3 GFLOPS. Dari metode yang sama dibangun dua model: gradasi tiga kelas dan pencacahan satu kelas. Kinerja diukur dengan presisi, recall, F1-score, dan mAP50.

YOLOv8 sebagai pembanding mencatat presisi 84,7%, recall 0,763, F1 0,803, mAP50 0,859, dengan ukuran 21,4 M. Setelah ditambah MHSA, model gradasi kematangan mencatat presisi 80,6%, recall 0,807, F1 0,806, dan mAP50 0,864, dengan ukuran 22,9 M; kenaikan berturut-turut adalah 0,044 pada recall, 0,003 pada F1, dan 0,004 pada mAP50. Menurut kelas, IM mencapai presisi 84,6%, recall 0,829, dan mAP50 0,880; SM mencapai 76,4%, 0,764, dan 0,824; M mencapai 80,7%, 0,828, dan 0,888. Model pencacahan mencatat presisi 0,990, recall 0,960, F1 0,975, dan mAP50 0,916. Kurva pelatihan dan validasi menunjukkan konvergensi tanpa tanda overfitting.

Batasan yang dinyatakan penulis mencakup oklusi buah, kaburnya latar, dan kemiripan ciri antara kelas SM dan M akibat gangguan cahaya, yang menjadi penghambat utama peningkatan kinerja. Model gradasi lebih lemah daripada model pencacahan karena merupakan masalah tiga kelas dengan jumlah instans yang tidak seimbang. Pada oklusi parah, kinerja menurun, terutama pada gradasi kematangan. Jika model dipasang pada robot, ruang gerak yang sempit antarbarisan tanam membatasi area yang dapat dipantau dan efisiensi operasi. Penulis menyatakan data tidak tersedia untuk umum dan mengarahkan pekerjaan lanjutan pada peredaman gangguan tersebut.

