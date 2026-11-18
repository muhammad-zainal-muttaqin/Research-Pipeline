# Automated Detection and Counting of Gossypium barbadense Fruits in Peruvian Crops Using Convolutional Neural Networks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ballenaruiz2025automated` |
| Judul asli | Automated Detection and Counting of Gossypium barbadense Fruits in Peruvian Crops Using Convolutional Neural Networks |
| Penulis | Ballena-Ruiz, Juan; Arcila-Diaz, Juan; Tuesta-Monteza, Victor |
| Tahun | 2025 |
| Venue | Agriengineering |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | cotton |

## Tautan Akses
- PDF: [ballenaruiz2025automated.pdf](../pdf/ballenaruiz2025automated.pdf)
- DOI resmi: https://doi.org/10.3390/agriengineering7050152

## Gambaran Umum

Kajian ini mengembangkan sistem deteksi dan penghitungan otomatis buah kapas *Gossypium barbadense* varietas IPA pada tahap pemasakan yang disebut "mota" di wilayah Lambayeque, Peru utara. Penghitungan manual memerlukan banyak waktu dan tenaga, sehingga tidak praktis untuk produksi skala besar; kondisi lingkungan yang berubah juga menyulitkan penentuan luas tanam dan estimasi hasil. Tujuannya adalah membangun model convolutional neural network untuk mendeteksi dan menghitung buah kapas, lalu mengintegrasikannya ke dalam aplikasi web agar petani dan teknisi lapang dapat memperkirakan hasil panen dari citra.

Tanaman yang dikaji adalah kapas IPA berusia 5–6 bulan pada tahap produksi. Penelitian dilakukan di dua petak di distrik, provinsi, dan region Lambayeque, Peru (6°40′20″ LS, 79°53′17″ BB), dengan luas gabungan 8.458,37 m² atau sekitar 0,85 hektare. Citra dikumpulkan dengan jalur berjalan jarak 1 m antarbaris dan kamera pada ketinggian 2,5 m dari tanah, karena tinggi tanaman 1,00–1,20 m. Perangkat Samsung A12 (SM-A127M) dipasang pada statif dan tongkat teleskopik dengan dudukan 180°, menghasilkan 370 citra JPG beresolusi 640 × 640 piksel dengan ISO 20, jarak fokus 5 mm, dan setara 25 mm pada format 35 mm. Dari 370 citra, 100 citra pertama dianotasi manual dengan LabelImg 1.8.6 pada kelas "cotton", menghasilkan 3.062 anotasi format YOLO dengan rata-rata 30 anotasi per citra. Augmentasi berupa rotasi bertahap −5° sampai +5° menghasilkan rata-rata 21–22 citra baru per citra asli, sehingga himpunan akhir memuat 2.186 citra dan 70.348 buah berlabel.

Lima model dilatih, yaitu YOLOv8n, YOLOv8x, YOLOv11n, YOLOv11x, dan Faster R-CNN. YOLOv8 dan YOLOv11 memakai skema anchor-free, dengan masukan 640 × 640 dan prediksi langsung koordinat kotak serta skor keyakinan; Faster R-CNN memakai ResNet50 untuk ekstraksi fitur, Region Proposal Network, dan RoI Pooling atau RoI Align. Himpunan dibagi 70% latih, 15% validasi, dan 15% uji, dengan 100 epoch dan batch 8. Evaluasi memakai presisi TP/(TP+FP), recall TP/(TP+FN), dan F1 sebagai harmonic mean keduanya, dihitung dari matriks konfusi pada split uji. Jumlah absolut citra uji tidak dinyatakan.

Hasil pada split uji menunjukkan YOLOv8x dan YOLOv11x sebagai model terbaik. YOLOv8x mencatat 10.794 true positive dengan 26 false positive, presisi 99,81%, recall 99,54%, dan F1 99,68%; YOLOv11x mencatat 10.621 true positive dengan 35 false positive, presisi 99,78%, recall 99,44%, dan F1 99,61%. YOLOv8n memperoleh presisi 98,80%, recall 97,40%, dan F1 98,10%; YOLOv11n 97,91%, 97,33%, dan 97,62%; Faster R-CNN 99,10%, 97,22%, dan 98,15%, dengan false negative 551 dan false positive 575, jumlah tertinggi di antara kelima model. Nilai pada Tabel 4 merupakan rata-rata epoch akhir. Model terbaik, yaitu YOLOv8x, diintegrasikan ke aplikasi web berbasis arsitektur Model-View-Controller dengan framework Django untuk menghitung buah pada citra yang diunggah; metrik mAP tidak dinyatakan.

Penulis menyatakan keterbatasan utama berupa model belum diuji pada citra lapang yang berbeda dari himpunan latih. Pengujian lanjutan diperlukan pada kondisi pencahayaan, sudut akuisisi, dan variabilitas tanaman yang belum tercakup. Rencana berikutnya adalah penerapan model pada aplikasi seluler untuk memproses video secara real time dan memperluas pengujian ke kondisi lapang serta jenis tanaman lain.

