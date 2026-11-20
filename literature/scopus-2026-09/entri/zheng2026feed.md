# Feed-forward 3D reconstruction with point-cloud representations: From DUSt3R to VGGT and beyond

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zheng2026feed` |
| Judul asli | Feed-forward 3D reconstruction with point-cloud representations: From DUSt3R to VGGT and beyond |
| Penulis | Zheng, Zeyi; Yang, Xiong; Yi, Ran; Ma, Lizhuang |
| Tahun | 2026 |
| Venue | Virtual Reality and Intelligent Hardware |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [zheng2026feed.pdf](../pdf/zheng2026feed.pdf)
- DOI resmi: https://doi.org/10.1016/j.vrih.2026.03.005

## Gambaran Umum

Survei oleh Zheng dkk. (2026) dalam *Virtual Reality & Intelligent Hardware* ini bertujuan meninjau metode rekonstruksi 3D berbasis *point cloud* yang bersifat *feed-forward*, yakni metode yang menghasilkan geometri padat dan, bila relevan, pose kamera melalui inferensi jaringan saja tanpa optimasi per-adegan *Structure-from-Motion* (SfM) dan *Multi-View Stereo* (MVS) sebagai mekanisme utama. Penulis menempatkan rangkaian ini dari DUSt3R (CVPR 2024) hingga VGGT (CVPR 2025) dan varian turunannya yang terbit sampai Oktober 2025. Penulis merumuskan tugas rekonstruksi dalam dua setting, yaitu *pose-aware* (intrinsik dan ekstrinsik diberikan) dan *pose-free* (parameter kamera diestimasi saat uji), lalu membandingkan prediksi *point map* dengan pipeline klasik SfM dan MVS. Ruang lingkup survei mencakup model dua-tampilan maupun multi-tampilan. Metode yang hanya mengandalkan *Neural Radiance Fields* (NeRF) atau *3D Gaussian splatting* tidak masuk pembahasan utama.

Isi pokok survei disusun dalam tiga tahap. Tahap pertama adalah model pasangan awal seperti DUSt3R, yang meregresi *pointmap* dari pasangan citra tanpa pose dan memulihkan pose serta korespondensi dari geometri hasil prediksi. Tahap kedua adalah perluasan gaya DUSt3R yang memperkuat konsistensi multi-tampilan, pemrosesan *streaming*, efisiensi, dan adegan dinamis. Tahap ketiga adalah kerangka terpadu berbasis transformer besar seperti VGGT, yang memproses puluhan hingga ratusan tampilan secara bersamaan. Penulis membandingkan model-model tersebut menurut representasi adegan, penalaran korespondensi, regresi pose, strategi fusi, dan peran data latih berskala besar. Survei juga merangkum dataset 3D yang sering dipakai, termasuk MegaDepth, ScanNet, DTU, dan Waymo, beserta metrik evaluasinya. Metrik utama pada DTU adalah *accuracy* (Acc.), *completeness* (Comp.), dan rata-rata keduanya (Overall) yang berupa jarak Chamfer-L2 simetris. Untuk pose kamera pada ScanNet, digunakan AUC pada ambang sudut 5°, 10°, dan 20°.

Perbandingan kuantitatif dilakukan pada DTU dengan penyelarasan Sim(3) Umeyama. Pada tabel multi-tampilan, metode yang memakai kamera ground truth dibandingkan dengan metode yang mengestimasi kamera saat uji, dan angka sebagian dikutip dari makalah VGGT. Pada *point map*, VGGT mencapai rata-rata Acc. 1,338 dan π3 mencapai 1,198 dengan median 0,646, sedangkan Fast3R (3,340), CUT3R (4,742), dan FLARE (2,541) berada di bawahnya. Dari sisi waktu inferensi pada GPU NVIDIA L40 dengan citra 512 × 512, VGGT dan π3 tumbuh jauh lebih lambat seiring bertambahnya jumlah tampilan dibanding DUSt3R. Waktu DUSt3R naik dari 0,169 s pada 2 tampilan menjadi 4,826 s pada 8 tampilan, sedangkan VGGT hanya 0,184 s untuk satu tampilan dan π3 0,154 s. Pada estimasi pose ScanNet dengan 8 frame, π3 memperoleh hasil terbaik di semua ambang, diikuti dekat oleh VGGT, sementara DUSt3R dan FLARE tertinggal jauh. CUT3R menempati posisi terendah, yang menurut penulis disebabkan desainnya lebih cocok untuk inferensi streaming sekuens panjang.

Penulis menyatakan sejumlah batasan. Angka Acc. DUSt3R pada DTU harus ditafsirkan hati-hati karena dievaluasi dalam setting *pose-free* sehingga tidak sebanding langsung dengan baseline *pose-aware*, dan skala yang ambigu kemungkinan memperbesar selisih tersebut. Beberapa angka tabel juga dikutip dari makalah lain, sehingga keterbandingannya bergantung pada protokol asal. Penulis menilai bahwa pendekatan terpadu memerlukan memori yang besar untuk masukan berskala besar dan konteks panjang. Tantangan terbuka yang diakui meliputi keterbatasan data 3D, rekonstruksi dari tampilan jarang, material non-Lambertian, adegan dinamis, pemrosesan konteks panjang, serta efisiensi penerapan. Penulis juga menyarankan arah lanjutan yang memadukan arsitektur *feed-forward* dengan *differentiable rendering*, *generative priors*, dan mekanisme keamanan.
