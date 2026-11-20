# Application of Machine Vision Technology in Citrus Production

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `peng2023application` |
| Judul asli | Application of Machine Vision Technology in Citrus Production |
| Penulis | Peng, Kaiqian; Ma, Wei; Lu, Jinzhu; Tian, Zhiwei; Yang, Zhiming |
| Tahun | 2023 |
| Venue | Applied Sciences Switzerland |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [peng2023application.pdf](../pdf/peng2023application.pdf)
- DOI resmi: https://doi.org/10.3390/app13169334

## Gambaran Umum

Tinjauan ini merangkum penerapan visi mesin dalam tiga tahap produksi jeruk: deteksi hama dan penyakit, pengenalan dan penentuan posisi buah untuk pemanenan, serta pengelompokan mutu buah. Latar belakangnya adalah produksi jeruk global yang terus meningkat, dengan total lebih dari 130 juta ton pada 2010–2023 atau pertumbuhan sekitar 125%, sementara efisiensi dan ketepatan produksi terbatas oleh kekurangan tenaga ahli, waktu, dan upaya. Visi mesin mencakup perangkat keras berupa sumber cahaya, kartu pemroses citra, dan aktuator, serta perangkat lunak berupa algoritma pemrosesan citra. Penulis membandingkan kelebihan dan kekurangan tiap pendekatan, lalu menguraikan masalah yang tersisa dan arah penelitian berikutnya.

Data berupa citra RGB dari kamera atau telepon genggam, citra hiperspektral dari kamera spektral, dan citra tiga dimensi yang jumlahnya masih sedikit. Pada pendekatan tradisional, citra daun sakit melewati praproses untuk membuang latar, fitur dibuat manual dari ruang warna, tekstur, dan bentuk, lalu diklasifikasikan dengan naive Bayes, SVM, AdaBoost, atau ensemble pohon. Pendekatan pembelajaran mendalam memakai jaringan seperti ResNet34, VGG-16, E-Res2Net, YOLOv4, Faster R-CNN, EfficientNet, serta penggabungan fitur dari DenseNet dan Xception. Citra hiperspektral direkam pada rentang seperti 480–900 nm dengan 81 pita, 478–900 nm, 380–1080 nm, dan 325–1098 nm, lalu direduksi dengan PCA atau seleksi pita sebelum klasifikasi dengan SVM, random forest, PLS-DA, atau jaringan berulang.

Mekanisme utama memanfaatkan perubahan warna, tekstur, dan bentuk daun atau buah, serta perubahan spektral akibat infeksi. Hasil yang dikutip penulis mencakup akurasi 99%, luas di bawah kurva 1,0, dan sensitivitas 99,7% untuk klasifikasi penyakit dengan deskriptor Delta E, RGB, HSV, dan LBP pada pengklasifikasi ensemble pohon. Segmentasi naive Bayes pada canker memberikan laju salah segmentasi terendah meski memakan waktu lebih lama, dan kuantisasi HSV takseragam 16:4:4 lebih jelas daripada skema 8:3:3. Model VGG-16 atas 81 pita hiperspektral mencapai akurasi rata-rata 98,75%; E-Res2Net mencapai 86,04% atau 3,91% lebih tinggi daripada Res2Net-50; YOLOv4-Tiny yang dimodifikasi mengenali kutu psyllid dengan presisi rata-rata 96,16%; dan R-CNN berbasis ResNet 33 lapis menghasilkan 95,31%, 90,23%, dan 99,20% untuk tiga penyakit. Deteksi dan klasifikasi dengan YOLO-V4 dan EfficientNet mencapai 89% di lapang, lebih rendah daripada di laboratorium, sementara model gabungan DenseNet-Xception menghasilkan mAP deteksi 85,10% dan akurasi klasifikasi 96,69%. Pada citra hiperspektral, model Att-BiGRU-RNN mencapai akurasi keseluruhan 98,21% dan model PLS-DA untuk huanglongbing menghasilkan laju salah keputusan hanya 5,6%. Untuk pengelompokan mutu, konversi RGB ke HSV dengan analisis interval tonal menghasilkan empat kelas warna dengan akurasi 93,75%, dan YOLOv5 dengan sistem dua cahaya serta mekanisme perhatian CBAM meningkatkan presisi rata-rata 5,8% terhadap model awal. Pada pemanenan, YOLOv3-tiny yang dimodifikasi mencapai akurasi pengenalan rata-rata 96,52%, dan algoritma Informed RRT* dengan titik pandu sebelum memetik memangkas waktu perencanaan 46%.

Batasan yang dinyatakan penulis mencakup ketiadaan himpunan data terbuka jeruk yang memadai, karena sebagian besar citra berupa RGB dan hanya sedikit citra 3-D, dengan jenis penyakit yang terfokus pada huanglongbing dan canker. Lingkungan lapang yang berubah-ubah, antara lain pertumbuhan tidak beraturan, intensitas cahaya, dan penutupan daun, menimbulkan gangguan yang membuat robot salah mengenali atau salah menentukan posisi buah; akurasi di luar ruangan juga lebih rendah daripada di laboratorium. Beberapa model hanya mengenali satu daun atau sedikit jenis penyakit, dan kelangkaan citra black spot serta scab memicu overfitting. Metode tradisional lambat dan subjektif dalam mengekstrak fitur, sedangkan model mendalam memerlukan komputasi besar, memori besar, dan perangkat keras berkualitas tinggi; algoritma yang dipakai masih terutama serial dan sering hanya berlaku untuk tanaman tertentu. Penelitian tentang buah dalam keadaan bergerak juga belum matang dan umumnya dilakukan dalam kondisi ideal. Penulis mengarahkan penelitian berikutnya pada keragaman himpunan data, penggunaan kamera RGB-D, robot untuk lingkungan kompleks, perangkat keras dan algoritma paralel yang lebih baik, serta penambahan pemantauan dinamis.
