# FG-LCNet: A two-stage foreground-guided network for whole-tree litchi counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhuang2026fg` |
| Judul asli | FG-LCNet: A two-stage foreground-guided network for whole-tree litchi counting |
| Penulis | Zhuang, Yitao; Yang, Mingchao; Ke, Zhikeng; Chen, Riyao; Gao, Yuefang; Wang, Xianghe; Hu, Fuchu |
| Tahun | 2026 |
| Venue | Plant Phenomics |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | litchi/longan |

## Tautan Akses
- PDF: [zhuang2026fg.pdf](../pdf/zhuang2026fg.pdf)
- DOI resmi: https://doi.org/10.1016/j.plaphe.2026.100268

## Gambaran Umum

Penghitungan buah leci yang akurat dari citra seluruh pohon penting untuk estimasi hasil, pengelolaan kebun, dan fenotipe tanaman. Di kebun nyata, tugas ini tetap sulit karena buah tumbuh dalam tandan padat yang sering tertutup daun. Pada tahap hijau, buah juga mudah tertukar dengan dedaunan di sekitarnya. Metode yang ada bergantung pada *instance segmentation* atau deteksi objek, dan kinerjanya menurun ketika tumpang-tindih dan gangguan latar sangat kuat. Penulis menilai bahwa penghitungan seluruh pohon yang andal di bawah kerapatan tinggi, oklusi berat, dan perubahan penampilan antarfase fenologi belum banyak diteliti. Karena itu, mereka mengusulkan FG-LCNet untuk memisahkan pelokalan kluster buah dari penghitungan di dalam kluster.

Data dikumpulkan dari Februari 2023 hingga Agustus 2024 di lima kebun, yaitu Haikou, Chengmai, Qionghai, Zhanjiang, dan Maoming. Dataset mencakup hampir 50 kultivar leci dan tiga tahap pematangan, yaitu hijau, mulai merah, dan merah penuh. Citra diambil dengan *unmanned aerial vehicle* (UAV), kamera *digital single-lens reflex* (DSLR), dan ponsel pintar, dengan resolusi dari 512 × 515 hingga 2048 × 4846 piksel. Dataset berisi 1126 citra seluruh pohon. Anotasi terdiri atas *bounding box* tingkat kluster, yang diberi label sesuai tahap kematangan dominan, dan anotasi titik tingkat buah. Total anotasi titik sekitar 120.000 dan kotak kluster lebih dari 20.000. Tabel 1 memuat rincian per kebun, tetapi angka per kebun dalam tabel tidak dikutip di sini. Setiap kebun menunjukkan perbedaan jumlah buah dan kluster yang signifikan.

FG-LCNet bekerja dalam dua tahap. Tahap pertama adalah YOLOv11 yang ditingkatkan dengan kepala P2 beresolusi tinggi dan modul *Global-to-Local Spatial Aggregation* (GLSA). Tahap ini mendeteksi kluster buah dan menekan latar belakang tajuk. Tahap kedua adalah jaringan regresi kepadatan dengan *hybrid attention* yang dilatih menggunakan strategi konsistensi (*consistency disturbance*). Jaringan ini menghitung buah pada citra yang latar belakangnya sudah ditekan. Hasil utama pada dataset ini adalah MAE 7,44 dan RMSE 11,01, dengan kinerja terbaik secara keseluruhan. Penulis melaporkan keunggulan jelas pada skenario kluster padat dan validasi lintas kebun. Hasil pada subset wilayah kebun dan tahap kematangan tetap kompetitif. Efisiensi inferensi juga dinyatakan cukup untuk penerapan praktis.

Penulis menyatakan beberapa batasan. Angka kebenaran dasar hanya merujuk pada buah yang terlihat dari sudut pandang citra tersebut, bukan seluruh beban buah tiga dimensi pada pohon. Karena itu, hasil penghitungan tidak sama dengan total panen pohon. Dataset ini mencakup lima kebun dan tiga tahap kematangan, sehingga generalisasi ke kondisi lain perlu diuji lebih lanjut. Penulis juga menyebut bahwa metode ini diharapkan dapat dipakai untuk tugas penghitungan buah berkelompok lainnya, tetapi klaim tersebut belum diuji pada komoditas lain.
