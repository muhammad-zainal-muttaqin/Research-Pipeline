# 3D Gaussian Splatting for Real-Time Radiance Field Rendering

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kerbl20233d` |
| Judul asli | 3D Gaussian Splatting for Real-Time Radiance Field Rendering |
| Penulis | Kerbl, Bernhard; Kopanas, Georgios; Leimkuehler, Thomas; Drettakis, George |
| Tahun | 2023 |
| Venue | ACM Transactions on Graphics |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [kerbl20233d.pdf](../pdf/kerbl20233d.pdf)
- DOI resmi: https://doi.org/10.1145/3592433

## Gambaran Umum

Penelitian ini mengatasi keterbatasan sintesis pandangan baru pada rekonstruksi adegan dari banyak foto atau video. Metode medan radiansi seperti NeRF menghasilkan mutu tinggi, tetapi pelatihan dan perenderannya memakan biaya besar. Metode yang lebih cepat mengorbankan mutu, dan pada resolusi 1080p untuk adegan utuh dan tidak terikat, belum ada metode yang mencapai laju waktu nyata. Tujuan penulis adalah menghasilkan mutu setara metode terbaik dengan waktu latih yang bersaing dengan metode tercepat, sekaligus merender pandangan baru pada resolusi 1080p dengan laju sekurang-kurangnya 30 bingkai per detik.

Objek yang dipelajari bukan tanaman, melainkan adegan nyata dan sintetis. Pengujian memakai 13 adegan nyata dari himpunan Mip-NeRF360, Tanks and Temples, dan Deep Blending, ditambah delapan adegan sintetis dari himpunan Blender NeRF. Adegan nyata mencakup ruang dalam yang terbatas maupun lingkungan luar yang tidak terikat. Masukan berupa kamera yang terkalibrasi dengan Struktur-dari-Gerak dan awan titik jarang yang dihasilkan bersamaan dengan kalibrasi tersebut. Pembagian latih dan uji mengikuti aturan Mip-NeRF360, yaitu setiap foto kedelapan dipakai untuk pengujian. Metrik yang dipakai adalah PSNR, SSIM, dan LPIPS untuk mutu, serta waktu latih, laju bingkai per detik, dan memori. Seluruh hasil diukur pada GPU A6000, kecuali beberapa angka Mip-NeRF360 yang diambil dari publikasi aslinya.

Mekanisme inti terdiri dari tiga bagian. Pertama, adegan direpresentasikan sebagai sekumpulan Gaussian tiga dimensi yang diawali dari awan titik SfM. Sifat setiap Gaussian meliputi posisi tiga dimensi, opacitas, kovarians anisotropik, dan koefisien harmonik bola. Kedua, sifat-sifat itu dioptimalkan secara bergantian dengan pengendalian kepadatan adaptif. Gaussian kecil yang belum mencakup geometri diduplikasi, sedangkan Gaussian besar yang mewakili geometri berlebih dibelah dua; Gaussian dengan opacitas sangat rendah atau jejak sangat besar dibuang. Ketiga, rasterizer differensial berbasis ubin berukuran 16 kali 16 piksel menyortir seluruh primitive layar dengan Radix sort pada GPU dan melakukan pelapisan alfa sesuai urutan kedalaman. Perenderan berhenti bila akumulasi opacitas mencapai jenuh, dan lintasan mundur menelusuri ulang daftar ubin tanpa menyimpan daftar titik per piksel.

Hasil kuantitatif pada Tabel 1 menunjukkan bahwa konfigurasi 30.000 iterasi mencapai mutu setara atau sedikit lebih baik dari Mip-NeRF360. Pada himpunan Mip-NeRF360, metode ini mencatat SSIM 0,815, PSNR 27,21, dan LPIPS 0,214 dengan waktu latih 41 menit 33 detik serta laju 134 bingkai per detik, sementara Mip-NeRF360 mencatat SSIM 0,792, PSNR 27,69, dan LPIPS 0,237 dengan waktu latih 48 jam serta laju 0,06 bingkai per detik. Pada Tanks and Temples, metode ini mencatat SSIM 0,841, PSNR 23,14, dan 154 bingkai per detik; pada Deep Blending, SSIM 0,903, PSNR 29,41, dan 137 bingkai per detik. Konfigurasi 7.000 iterasi mencapai PSNR 25,60 setelah 6 menit 25 detik pada Mip-NeRF360 dengan laju 160 bingkai per detik. Pada himpunan sintetis Blender (Tabel 2), rata-rata PSNR 33,32 mengungguli Point-NeRF 33,30 dan InstantNGP 33,18; adegan sintetis dirender pada 180–300 bingkai per detik. Untuk adegan nyata, waktu latih berkisar 35–45 menit dibandingkan 48 jam bagi Mip-NeRF360. Uji kekompakan menghasilkan ukuran model rata-rata 3,8 MB dengan sekitar seperempat jumlah titik dari metode pembanding yang berukuran 9 MB.

Batasan yang dinyatakan penulis termuat di bagian 7.4. Artefak muncul pada wilayah yang kurang teramati selama pelatihan, meskipun metode pembanding juga mengalami hal serupa. Gaussian anisotropik dapat membentuk artefak memanjang atau bercak, dan terdapat artefak muncul-tiba ketika optimasi membentuk Gaussian besar, terutama pada wilayah dengan tampilan bergantung sudut pandang. Penulis menyebut penyebabnya adalah penolakan sederhana oleh guard band pada rasterizer dan algoritma visibilitas yang masih sederhana. Optimasi belum memakai regularisasi, dan laju pembelajaran posisi perlu diturunkan untuk adegan sangat besar. Konsumsi memori lebih tinggi daripada solusi berbasis NeRF; saat melatih adegan besar, memori puncak dapat melebihi 20 GB pada prototipe yang belum dioptimalkan, dengan model tersimpan berukuran ratusan megabita ditambah 30–500 MB untuk rasterizer. Penulis memperkirakan sekitar 80 persen waktu latih masih dihabiskan pada kode Python karena hanya rasterisasi yang ditulis sebagai kernel CUDA.

