# MLP-based multimodal tomato detection in complex scenarios: Insights from task-specific analysis of feature fusion architectures

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2024mlp` |
| Judul asli | MLP-based multimodal tomato detection in complex scenarios: Insights from task-specific analysis of feature fusion architectures |
| Penulis | Chen, Wenjun; Rao, Yuan; Wang, Fengyi; Zhang, Yu; Wang, Tan; Jin, Xiu; Hou, Wenhui; Jiang, Zhaohui; Zhang, Wu |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [chen2024mlp.pdf](../pdf/chen2024mlp.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.108951

## Gambaran Umum

Deteksi tomat yang akurat dan efisien penting bagi robot pemetik di lapangan. Namun, deteksi berbasis RGB saja sulit pada kondisi kompleks, seperti cahaya yang berubah-ubah, buah yang saling tumpang tindih, dan oklusi oleh cabang serta daun. Kajian ini menilai kontribusi tugas spesifik dari arsitektur penggabungan fitur berbasis *Multi-Layer Perceptron* (MLP), *Vision Transformer* (ViT), dan *Convolutional Neural Network* (CNN). Penulis juga mengusulkan model deteksi ringan yang memanfaatkan data kedalaman dan inframerah dekat selain citra RGB.

Data dikumpulkan di Institut Ilmu Pertanian Kabupaten Shucheng, Kota Lu'an, Provinsi Anhui, Tiongkok, pada Juni 2022 dan April 2023. Sensor yang digunakan adalah kamera kedalaman Azure Kinect yang menghasilkan citra RGB, kedalaman, dan inframerah dekat. Ketiga modalitas diselaraskan memakai API produsen kamera dan disimpan pada resolusi 1280x720. Kamera diposisikan 0,3 sampai 2,0 m dari tomat dan 1,0 sampai 2,0 m di atas tanah, meniru sudut pandang lengan robot yang dipasang pada tangan. Kumpulan data terdiri atas 1.342 sampel dengan rata-rata dua puluh buah tomat per sampel, pada berbagai tingkat kematangan dan kondisi pencahayaan. Data latih dan validasi dipilih secara acak dengan rasio 9:1.

Metode yang diusulkan adalah YOLO-DNA, yaitu kerangka deteksi ringan berbasis YOLOv7-tiny yang diintegrasikan dengan *encoder* fusi multimodal. Encoder ini mengekstraksi fitur dari modalitas kedalaman dan inframerah dekat, lalu menggabungkannya dengan fitur dari citra RGB. Varian MLP dipilih karena memberi keseimbangan performa yang baik. Hasil utamanya, YOLO-DNA mencapai mAP0,5 sebesar 98,13% dan mAP0,5:0,95 sebesar 74,0%. Rata-rata peningkatannya terhadap model ringan utama adalah 5,01% pada mAP0,5 dan 14,55% pada mAP0,5:0,95. Kecepatan deteksinya mencapai 37,12 *frame per second* (FPS), yang dinilai memenuhi kebutuhan deteksi tomat secara *real-time*. Pada pengujian ketahanan, arsitektur CNN bergantung kuat pada kualitas citra RGB, sedangkan ViT tidak stabil dan membutuhkan biaya inferensi tinggi.

Penulis menyatakan bahwa nilai mAP hanya menggambarkan performa pada kumpulan data dan anotasi yang digunakan, sehingga penerapan di lingkungan praktis dan kemampuan generalisasi model masih menjadi tantangan. Arsitektur MLP menunjukkan potensi, tetapi teknik untuk mencegah *overfitting* perlu dikaji lebih lanjut karena parameter MLP yang besar dan data latih yang relatif kecil. Penulis juga menyebut bahwa stabilitas model masih perlu ditingkatkan agar hasil deteksi tidak berubah-ubah antarbingkai.
