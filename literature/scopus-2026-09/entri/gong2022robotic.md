# Robotic harvesting of the occluded fruits with a precise shape and position reconstruction approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gong2022robotic` |
| Judul asli | Robotic harvesting of the occluded fruits with a precise shape and position reconstruction approach |
| Penulis | Gong, Liang; Wang, Wenjie; Wang, Tao; Liu, Chengliang |
| Tahun | 2022 |
| Venue | Journal of Field Robotics |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [gong2022robotic.pdf](../pdf/gong2022robotic.pdf)
- DOI resmi: https://doi.org/10.1002/rob.22041

## Gambaran Umum

Penulis menangani oklusi (buah tertutup daun atau buah lain) yang menurunkan keberhasilan robot pemetik tomat. Kesulitan yang disebut ada tiga: tingkat deteksi rendah untuk tomat yang sangat tertutup, kontur tomat tertutup sulit ditentukan, dan posisi target meleset akibat oklusi parsial. Tujuannya adalah memperkirakan bentuk dan posisi tomat yang tertutup, bukan hanya memulihkan tampilan citra.

Data berasal dari rumah kaca tomat Venlo di Shanghai Sunqiao Modern Agriculture Base. Kamera Kinect-v2 menghasilkan citra RGB (1920 × 1080), kedalaman (*depth*), dan inframerah (512 × 424). Terkumpul 2.000 pasang citra RGB-D-I; tiap pasang berisi satu citra tomat utuh dan beberapa citra tomat yang sama saat tertutup. Set data Fruits-360 (49.561 citra, 74 jenis buah) dipakai sebagai data tambahan pralatih. Set uji deteksi berisi 500 sampel (371 tomat tunggal, 129 tomat bertumpuk). Pemberi label dan rasio latih/uji keseluruhan tidak disebut.

Metode pertama adalah Mask R-CNN yang diperluas (jaringan segmentasi instans) dengan masukan gabungan RGB, kedalaman, dan inframerah yang dipetakan piksel demi piksel lewat fungsi SDK Microsoft. Metode kedua adalah model pemulihan bentuk dan posisi (SPR), jaringan mirip UNet yang memperkirakan kedalaman bagian tomat yang tertutup. Dari kedalaman terpulihkan diambil jari-jari dan titik pusat (*centroid*). Sistem dipasang pada robot pemetik dua lengan.

Pada set uji 500 sampel, rerata IoU (*intersection over union*, tumpang tindih area) Mask R-CNN RGB adalah 0,851 dengan 195 ms per citra. Versi RGB-D-I mencapai 0,916 dengan 456 ms per citra. Pada oklusi di bawah 25% dan iluminasi 1 sampai 12 KLux, rerata IoU rekonstruksi adalah 0,895 dan galat titik pusat 0,62 mm. Pada oklusi 75% sampai 100%, galat titik pusat 12,94 mm dan rerata IoU 0,653. Pada uji petik di rumah kaca, waktu 11 detik per buah, akurasi cengkeram rerata 8,21 mm, dan keberhasilan petik rerata 73,04%.

Keterbatasan: oklusi pada uji lokalisasi dibuat dengan menutupkan topeng pada tomat utuh, bukan oklusi alami. Hanya satu spesies (tomat) di rumah kaca. Tidak ada pencacahan buah, tidak ada deduplikasi lintas pandang, dan pembagian latih/uji tidak dirinci per tanaman. Kegagalan petik terutama disebut berasal dari ruang kerja terbatas, batang tebal, dan gripper yang tergelincir.
