# NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mildenhall2020nerf` |
| Judul asli | NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis |
| Penulis | Mildenhall, Ben; Srinivasan, Pratul P.; Tancik, Matthew; Barron, Jonathan T.; Ramamoorthi, Ravi; Ng, Ren |
| Tahun | 2020 |
| Venue | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [mildenhall2020nerf.pdf](../pdf/mildenhall2020nerf.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-030-58452-8_24

## Gambaran Umum

Makalah ini memperkenalkan *neural radiance field* (NeRF), yaitu cara merepresentasikan adegan 3D sebagai jaringan saraf sederhana yang dilatih dari sekumpulan citra 2D. Jaringan *multilayer perceptron* (MLP) menerima koordinat 5D, yaitu posisi (x, y, z) dan arah pandang (θ, φ), lalu menghasilkan kepadatan volume dan warna yang bergantung pada arah pandang. Warna setiap piksel dihitung dengan *volume rendering*, yakni penjumlahan berbobot sepanjang sinar kamera. Karena seluruh proses itu dapat diturunkan, jaringan dilatih dengan galat rendering terhadap citra asli.

Masalah yang dipecahkan adalah sintesis pandangan baru (*novel view synthesis*): menghasilkan gambar dari sudut yang belum pernah dipotret, berdasarkan sekumpulan foto yang posisi kameranya diketahui. Menurut penulis, pendekatan sebelumnya memakai voksel diskret yang membatasi resolusi, atau permukaan implisit yang hanya menyimpan satu kedalaman dan satu warna per sinar. Makalah ini menambahkan dua perbaikan agar detail halus dapat ditangkap. Yang pertama adalah *positional encoding* pada koordinat dan arah pandang. Yang kedua adalah *hierarchical sampling*, yang tidak diuraikan di naskah dan dirujuk ke makalah asli. Optimasi satu adegan memerlukan sekitar 1 sampai 2 hari pada satu GPU, dan bobot jaringan berukuran sekitar 5 MB.

Hasil utama diukur dengan PSNR, SSIM, dan LPIPS pada tiga kumpulan data. Pada "Diffuse Synthetic 360°", yang berisi empat objek Lambertian sederhana, NeRF mencapai PSNR 40,15, SSIM 0,991, dan LPIPS 0,023. Nilai itu lebih baik daripada LLFF (PSNR 34,38) dan NV (PSNR 29,62). Pada "Realistic Synthetic 360°", yang berisi delapan objek dengan material non-Lambertian, PSNR NeRF 31,01 dibandingkan 24,88 milik LLFF. Pada "Real Forward-Facing", yang berisi delapan adegan nyata yang difoto dengan ponsel, PSNR NeRF 26,50 melampaui LLFF 24,13. Namun LPIPS NeRF 0,250 lebih buruk daripada LLFF 0,212, sehingga penulis hanya mengklaim unggul secara menyeluruh dengan pengecualian satu metrik pada data nyata. Waktu latih menjadi pertukaran utama: metode pembanding per adegan membutuhkan paling sedikit 12 jam, sedangkan LLFF memproses masukan kecil dalam kurang dari 10 menit tetapi menyimpan grid voksel yang sangat besar.

Objek uji dalam makalah ini berupa benda sintetis seperti kapal, lego, dan mikrofon, serta adegan nyata seperti daun pakis, kerangka dinosaurus, dan anggrek. Tidak ada data pertanian, tanaman, atau penghitungan objek di dalam makalah. Pengukuran yang dilaporkan hanya berupa kualitas gambar hasil rendering terhadap citra uji yang ditahan.

Keterbatasan yang tercantum di naskah adalah satu model dilatih untuk satu adegan, sehingga setiap adegan baru memerlukan optimasi ulang. Naskah tidak membahas adegan dengan banyak objek yang bergerak atau tertutup satu sama lain dalam skala besar.
