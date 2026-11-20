# Apple estimation and recognition in complex scenes using YOLO v8

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `geng2025apple` |
| Judul asli | Apple estimation and recognition in complex scenes using YOLO v8 |
| Penulis | Geng, Hui; Pan, Jun-Zhang; Cao, Yu-Chuan; Yin, Zhi-Ben; Wang, Jichuan; Shi, Ming-Deng; Si, Chunjing; Qi, Li-Mei |
| Tahun | 2025 |
| Venue | Peerj Computer Science |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [geng2025apple.pdf](../pdf/geng2025apple.pdf)
- DOI resmi: https://doi.org/10.7717/peerj-cs.3116

## Gambaran Umum

Robot pemanen apel dirancang untuk mengenali buah yang sudah matang, memanennya secara efisien, dan dapat diterapkan pada berbagai jenis buah. Namun, metode yang ada masih memiliki akurasi deteksi yang terbatas di lingkungan kompleks. Penyebabnya antara lain *shading* (bayangan dan tertutup daun atau buah lain) di alam, perubahan pencahayaan, serta keragaman warna, bentuk, dan ukuran buah. Kajian ini mengintegrasikan transformasi ruang warna *Hue–Saturation–Value* (HSV) dengan model *YOLO v8* untuk menghitung jumlah dan lokasi apel, serta menilai tingkat kematangan dan memperkirakan bobotnya. Latar belakangnya adalah Tiongkok sebagai produsen dan eksportir apel terbesar dunia, dengan produksi tahunan sekitar 35 juta ton. Mekanisasi panen dinilai penting untuk menekan biaya tenaga kerja, mengurangi kerusakan buah, dan meningkatkan efisiensi panen. Penulis membandingkan YOLO v8 dengan varian YOLO v9 hingga v12. Menurut penulis, varian-varian tersebut memiliki kelemahan untuk penerapan pada perangkat tepi di kebun, misalnya beban komputasi yang lebih besar, konvergensi yang tidak stabil, atau kebutuhan memori yang lebih tinggi.

Data yang digunakan berupa citra apel yang dikumpulkan di lingkungan alami kebun. Dalam pembahasan, penulis juga menguji model pada citra beberapa jenis buah yang memiliki bentuk dan warna mirip, dengan variasi sudut, pencahayaan, dan latar belakang. Penulis menyebut ada lima jenis buah dalam percobaan tersebut, dengan fokus pada lokasi dan tingkat kematangan apel. Kajian ini tidak menyebutkan jumlah citra atau jumlah buah dalam *dataset* secara spesifik pada bagian yang dibaca. Tahapan pengolahan citra meliputi konversi keabuan dan penyaringan Gaussian untuk mereduksi derau. Deteksi tepi dilakukan dengan algoritma *Canny* dan *Sobel*. Kematangan dinilai dari nilai HSV dan *Red–Green–Blue* (RGB), sedangkan bobot diperkirakan melalui pembentukan model 3D buah.

Hasil kuantitatif utama menunjukkan bahwa YOLO v8 mencapai *average precision* 95% dan *F1-score* 93,45%. Pada bagian pembahasan, *mean average precision* (mAP) dilaporkan sebesar 95,0%. Dibandingkan algoritma pembanding, YOLO v8 meningkatkan mAP sebesar 0,14% dibandingkan VGG dan 8% dibandingkan ResNet. Pada bagian kesimpulan, penulis mencatat peningkatan mAP 0,14%, akurasi 2,6%, dan *F1-score* 0,58 poin dibandingkan VGG, yang merupakan algoritma terbaik kedua dalam perbandingan. Penulis juga mengutip tolok ukur lain dalam tinjauan pustakanya, yaitu deteksi objek tunggal di lingkungan terkendali yang sering melampaui 95%, serta akurasi yang dapat turun di bawah 80% ketika banyak objek dan tekstur kompleks hadir. Dari sisi sumber daya, penulis menyebut YOLO v9 memiliki beban komputasi 112 GFLOPs dibandingkan 85 GFLOPs pada v8, serta YOLO v12 membutuhkan VRAM 8 GB dibandingkan 4 GB pada v8. Penulis juga menyatakan bahwa peningkatan akurasi dicapai melalui penetapan *anchor* dinamis, fusi *feature pyramid* yang diperbaiki, dan augmentasi data berupa *HSV jitter*, simulasi oklusi acak, serta *mosaic* multi-skala.

Penulis secara eksplisit menyatakan bahwa sistem belum diterapkan di lapangan. Kemungkinan penerapannya dibahas untuk tiga skenario, yaitu platform panen otomatis dengan NVIDIA Jetson, jalur sortir pascapanen dengan kamera RGB-D, dan pemantauan skala kebun melalui UAV atau menara kamera tetap. Penulis mengakui bahwa kinerja dapat menurun dalam cuaca ekstrem seperti hujan lebat atau kabut tebal tanpa sensor tambahan. Kebutuhan komputasi model, meskipun lebih ringan dibanding versi YOLO sebelumnya, tetap memerlukan pemilihan perangkat keras yang cermat untuk robot mobile otonom. Penulis juga menyebut bahwa kegagalan deteksi terjadi pada kondisi oklusi, pencahayaan bervariasi, dan citra buram, yang diduga berasal dari kurangnya data latih yang cukup dan beragam. Terakhir, penulis mencatat bahwa generalisasi model ke varietas dan kondisi lingkungan apel yang lebih beragam masih perlu diuji lebih lanjut, dan penerapan skala besar memerlukan sumber daya komputasi yang signifikan.
