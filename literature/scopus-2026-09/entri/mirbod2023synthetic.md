# Synthetic Data-Driven AI Using Mixture of Rendered and Real Imaging Data for Strawberry Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mirbod2023synthetic` |
| Judul asli | Synthetic Data-Driven AI Using Mixture of Rendered and Real Imaging Data for Strawberry Yield Estimation |
| Penulis | Mirbod, Omeed; Choi, Daeun |
| Tahun | 2023 |
| Venue | 2023 Asabe Annual International Meeting |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | strawberry |

## Tautan Akses
- PDF: [mirbod2023synthetic.pdf](../pdf/mirbod2023synthetic.pdf)
- DOI resmi: https://doi.org/10.13031/aim.202300548

## Gambaran Umum

Kajian ini menguji apakah citra sintetis dari simulasi dapat dipakai melatih detektor buah stroberi untuk estimasi hasil. Tujuannya mengurangi kebutuhan citra lapangan yang mahal dan memakan waktu. Studi sebelumnya sering memakai gambar contoh dari web atau adegan yang tidak mirip dengan kebun sasaran, sehingga hasilnya kurang representatif.

Data dikumpulkan pada Maret dan April 2023 di University of Florida Gulf Coast Research and Education Center, Wimauma, Florida, dari varietas 'Florida Brilliance' yang ditanam di bedengan beralas plastik. Platform darat buatan sendiri membawa tiga pasang kamera stereo Alvium 1800 U-240C, atau enam kamera, untuk merekam sisi dan permukaan atas bedengan. Platform berjalan 1 meter per detik dan merekam 3 citra per detik. Adegan simulasi dibuat di NVIDIA Isaac Sim dengan dua model tanaman 3D: M1 dari TurboSquid (lima variasi) dan M2 buatan penulis dengan beberapa tahap pertumbuhan. Citra sintetis diambil dari sisi dan atas bedengan simulasi. Data latih terdiri atas 75 citra sintetis M1 (189 label buah), 75 citra M1+M2 (201 label), 65 citra lapangan (278 label), dan 65 citra campuran lapangan dan M1 (306 label). Setiap model memakai 10 citra validasi dan 25 citra uji yang sama.

Model yang dipakai adalah *Faster R-CNN* (jaringan deteksi objek dua tahap) dengan arsitektur Inception ResNet V2 berukuran masukan 1024x1024 dari TensorFlow 2 Object Detection API. Setiap model dilatih 3.200 langkah dan deteksi diterima bila skor klasifikasi di atas 0,7. Penulis mengukur akurasi sebagai jumlah buah yang diprediksi dibagi jumlah buah aktual, bukan ketepatan klasifikasi per kotak. Model M1 mendeteksi 56 buah benar dengan 86 buah terlewat, presisi 0,96, recall 0,39, F1 0,56, dan akurasi 39,4%. Model M1+M2 mendeteksi 96 buah benar dengan 44 terlewat, presisi 0,97, recall 0,69, F1 0,80, dan akurasi 68,6%. Model lapangan mendeteksi 129 buah benar dengan 12 terlewat, presisi 0,98, recall 0,91, F1 0,95, dan akurasi 91,4%. Model campuran mendeteksi 127 buah benar dengan 14 terlewat, presisi 0,95, recall 0,90, F1 0,93, dan akurasi 90,0%. Penulis menyebut model sintetis M2 mengenali sekitar sepertiga buah muda dengan kelopak menghadap kamera, sedangkan M1 tidak mengenali satu pun. Penggantian M1 dengan M2 menaikkan akurasi 29 poin persentase.

Penulis menyatakan bahwa tanaman sintetis kurang variatif dalam tekstur dan warna, tetapi model tetap menemukan lebih dari sepertiga buah. Mereka juga menyatakan bahwa hasil ini belum cukup untuk menentukan fitur model sintetis mana yang paling menentukan. Penulis menyebut bahwa mengurangi jumlah citra M1 dari 75 menjadi 25 menaikkan deteksi dari 40% menjadi 50%, tetapi hipotesis ini belum diuji lebih lanjut. Batasannya, menurut penulis, adalah kebutuhan penelitian lanjutan untuk menyempurnakan model tanaman sintetis agar akurasi di lapangan naik. Kajian ini hanya menguji 25 citra dari satu plot dan satu varietas. Makalah ini berupa presentasi pertemuan ASABE yang tidak melalui tinjauan sejawat.

## Gambaran Umum

Kajian ini menguji apakah citra sintetis dari simulasi dapat dipakai melatih detektor buah stroberi untuk estimasi hasil. Tujuannya mengurangi kebutuhan citra lapangan yang mahal dan memakan waktu. Studi sebelumnya sering memakai gambar contoh dari web atau adegan yang tidak mirip dengan kebun sasaran, sehingga hasilnya kurang representatif.
