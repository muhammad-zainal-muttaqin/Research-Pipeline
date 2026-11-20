# RTMFusion: An enhanced dual-stream architecture algorithm fusing RGB and depth features for instance segmentation of tomato organs

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rong2025rtmfusion` |
| Judul asli | RTMFusion: An enhanced dual-stream architecture algorithm fusing RGB and depth features for instance segmentation of tomato organs |
| Penulis | Rong, Jiacheng; Zheng, Wanli; Qi, Zhongxian; Yuan, Ting; Wang, Pengbo |
| Tahun | 2025 |
| Venue | Measurement Journal of the International Measurement Confederation |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [rong2025rtmfusion.pdf](../pdf/rong2025rtmfusion.pdf)
- DOI resmi: https://doi.org/10.1016/j.measurement.2024.115484

## Gambaran Umum

Kajian ini membahas penentuan posisi pemotongan pada robot pemanen tomat. Pemanen robot perlu mengenali buah, tangkai buah (*pedicel*), dan batang (*stem*) dari berbagai posisi. Tantangannya adalah latar belakang yang mirip dengan tangkai dan batang, pola tumbuh tandan yang beragam, serta tangkai yang tipis dan pendek. Penulis menilai bahwa pendekatan berbasis citra warna saja tidak cukup untuk menentukan titik potong secara akurat, sehingga mereka mengusulkan pemanfaatan citra kedalaman (*depth*) bersama citra warna.

Data penelitian berasal dari tanaman tomat di rumah kaca. Dataset segmentasi instance terdiri atas 714 sampel beranotasi. Pembagian data dilakukan menjadi data latih, validasi, dan uji dengan rasio 0,7 : 0,15 : 0,15. Pelatihan dilakukan pada server awan dengan GPU NVIDIA GeForce RTX 4090. Pengujian dilakukan pada komputer yang terpasang pada robot pemanen, dengan CPU AMD Ryzen 5800H dan GPU NVIDIA GeForce RTX 3070. Citra masukan berukuran 640 × 640 piksel. Sumber citra adalah pasangan citra warna dan citra kedalaman dari kamera RGB-D. Sampel pencocokan organ diuji pada 150 sampel rumah kaca.

Metode yang diusulkan bernama RTMFusion, yaitu model *instance segmentation* dengan dua aliran (*dual-stream*) yang menggabungkan fitur citra warna dan citra kedalaman. Modul utama bernama *Depth Enhanced Feature Fusion* (DEFF). Untuk pencocokan organ, penulis menggunakan batasan jarak dan pencarian bersyarat pada *point cloud* semantik. Hasil pada data uji menunjukkan peningkatan *mask mAP* sebesar 4,6 persen dibandingkan model dasar, dengan nilai akhir 72,1 persen dan waktu proses 17,1 milidetik. Metode pencocokan mencapai akurasi 99,2 persen untuk tangkai buah dan 97,3 persen untuk batang pada 150 sampel rumah kaca. Penulis juga menyatakan bahwa sistem visual ini meningkatkan tingkat keberhasilan identifikasi dan ketepatan lokalisasi posisi pemotongan.

Penulis menyebut dua sumber ketidakpastian. Yang pertama adalah ketelitian tepi hasil segmentasi model. Yang kedua adalah keterbatasan kinerja kamera RGB-D itu sendiri. Karena itu, pencarian titik potong pada *point cloud* dirancang untuk mengurangi pengaruh noise sehingga posisi pemotongan lebih stabil.
