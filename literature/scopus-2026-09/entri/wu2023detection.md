# Detection and counting of banana bunches by integrating deep learning and classic image-processing algorithms

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wu2023detection` |
| Judul asli | Detection and counting of banana bunches by integrating deep learning and classic image-processing algorithms |
| Penulis | Wu, Fengyun; Yang, Zhou; Mo, Xingkang; Wu, Zihao; Tang, Wei; Duan, Jieli; Zou, Xiangjun |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | banana |

## Tautan Akses
- PDF: [wu2023detection.pdf](../pdf/wu2023detection.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.107827

## Gambaran Umum

Kajian ini membahas pendeteksian dan pencacahan tandan pisang pada kebun yang kompleks. Penghitungan tandan penting untuk dua keputusan di lapangan. Pertama, waktu pembuangan tunas steril (*sterile bud removal*) yang dilakukan robot. Kedua, estimasi berat tandan saat panen. Penulis menyebut bahwa tandan pisang sulit dihitung karena bentuknya kompleks, tersusun heliks di sepanjang tangkai, dan warnanya mirip dengan latar belakang daun dan cabang.

Data dikumpulkan dalam dua gelombang. Pada Desember 2021 pengambilan sampel dilakukan di kebun Guangdong Academy of Agricultural Sciences. Pada Maret 2022 pengambilan sampel dilakukan di Caojiang Town. Pengambilan gambar memakai cahaya alami tanpa sumber cahaya tambahan. Sensor yang digunakan adalah kamera ponsel pintar beresolusi tinggi (48 juta piksel, 2316 × 1080) dan kamera kedalaman Kinect 2.0 (1920 × 1080). Keduanya dipasang pada platform robot pembuangan tunas. Total 1500 citra asli diperoleh, terdiri atas 575 sampel dari periode pembuangan tunas dan 925 sampel dari periode panen. Jumlah sampel kemudian ditingkatkan melalui augmentasi data menjadi 2000 untuk periode pembuangan tunas dan 1500 untuk periode panen. Pada periode panen, tandan tersusun rapat. Pada periode pembuangan tunas, tandan tersebar lebih jarang.

Metode dibagi sesuai periode pertumbuhan. Pada periode pembuangan tunas, jaringan konvolusi DeepLab V3+ dipakai untuk segmentasi kasar, lalu algoritma pengolahan citra klasik dipakai untuk segmentasi halus dan penghitungan. Hasilnya adalah nilai MIoU segmentasi target sebesar 0,878, akurasi piksel rata-rata 0,936, dan akurasi deteksi tandan 86%. Pada periode panen, YOLOv5-Banana dipakai untuk mengenali kluster buah. Deteksi tepi kemudian mengekstrak titik pusat (*centroid*) setiap jari buah. Algoritma *K-means* dan koefisien siluet menentukan jumlah tandan yang terlihat pada permukaan deteksi. Model estimasi berbasis pola susunan heliks kemudian menghitung tandan yang tersembunyi. Pada periode panen, akurasi deteksi tandan tercatat 76%, dengan 38 dari 50 sampel benar dan 12 sampel salah. Akurasi pencacahan total untuk seluruh sampel uji mencapai 93,2%. Penulis juga merancang perangkat lunak untuk memperkirakan berat buah pisang pada periode panen.

Penulis menyatakan beberapa batasan. Jaringan segmentasi berukuran besar, sehingga pemrosesan citra beresolusi tinggi menjadi lambat. Hasil pengenalan juga masih peka terhadap kondisi pencahayaan. Penulis menilai algoritma pendeteksian batang pisang sudah memiliki tingkat keberhasilan yang dapat diterima, tetapi kompleksitasnya masih perlu diperbaiki. Penelitian lanjutan diharapkan meningkatkan ketahanan algoritma terhadap perubahan cahaya, membangun jaringan segmentasi yang lebih ringan, serta meningkatkan kestabilan dan kecepatan kinerja sistem.
