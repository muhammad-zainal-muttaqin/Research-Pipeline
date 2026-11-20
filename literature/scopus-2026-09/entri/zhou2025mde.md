# MDE-DETR: multi-domain enhanced feature fusion algorithm for bayberry detection and counting in complex orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2025mde` |
| Judul asli | MDE-DETR: multi-domain enhanced feature fusion algorithm for bayberry detection and counting in complex orchards |
| Penulis | Zhou, Cheng; Zhang, Yuyu; Fu, Wei; Yao, Lili; Yin, Chengliang |
| Tahun | 2025 |
| Venue | Frontiers in Plant Science |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [zhou2025mde.pdf](../pdf/zhou2025mde.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2025.1711545

## Gambaran Umum

Kajian ini bertujuan mendeteksi dan menghitung buah yang berukuran kecil di kebun kompleks guna mendukung perkiraan hasil. Buah yang dipelajari adalah bayberry (Myrica rubra). Penghitungan manual di kebun memakan tenaga dan waktu, sementara kondisi lapang menyulitkan deteksi: ukuran buah kecil, distribusi rapat, serta tertutup daun dan ranting. Penulis mengusulkan model Multi-Domain Enhanced DETR (MDE-DETR) sebagai penyelesaian ujung-ke-ujung (end-to-end) yang andal untuk kondisi tersebut.

Data dikumpulkan di Zhushan Bayberry Industry Park, Kabupaten Changxing, Kota Huzhou, Provinsi Zhejiang, pada awal Mei hingga akhir Juni. Citra diambil dengan ponsel iPhone 12, iPhone 14, dan Redmi K40S pada berbagai kondisi pencahayaan, sudut dekat, menengah, dan jauh, serta sudut elevasi dan depresi. Dari 2.512 citra awal, penyaringan menghasilkan 1.954 citra berkualitas tinggi yang dianotasi dengan LabelImg menggunakan kotak pembatas. Pembagian data mengikuti rasio 7:2:1, yaitu 1.367 citra latih, 391 validasi, dan 196 uji. Augmentasi pada himpunan latih menambah jumlahnya menjadi 5.468 citra. Model dilatih pada Windows 10, prosesor Intel Core i9-10900K, memori 32 GB, GPU NVIDIA GeForce RTX 3090, Python 3.9, dan PyTorch, dengan ukuran batch 8, 300 epoch, pengoptimal AdamW, dan laju pembelajaran awal 0,0001.

Mekanisme deteksi bertumpu pada tiga modul. EFENet sebagai jaringan ekstraksi fitur menggabungkan Multi-Path Feature Enhancement Module (MFEM), konvolusi reparameterisasi, koneksi cross-stage partial, dan perhatian lokal yang diperkuat. MDFFN sebagai jaringan fusi fitur memakai SPDConv untuk penataan ulang piksel spasial, CMKBlock dengan empat bentuk kernel kedalaman (1×1, 1×31, 31×1, 31×31), serta Dual-Domain Attention Module yang menggabungkan informasi domain spasial dan frekuensi melalui transformasi Fourier. ADSample sebagai modul downsampling menyesuaikan posisi sampling secara dinamis melalui prediksi offset spasial yang dipelajari dan interpolasi bilinear. Arsitektur RT-DETR mendeteksi secara ujung-ke-ujung tanpa Non-Maximum Suppression. Untuk penghitungan, penulis memilih 50 citra uji secara acak, menghitung buah manual lima kali per citra dan merata-ratkannya sebagai acuan, lalu meregresikan jumlah hasil mesin terhadap jumlah manual.

Pada himpunan uji bayberry, MDE-DETR mencapai mAP50 92,9 persen dan mAP50-95 67,9 persen, naik masing-masing 3,8 dan 5,1 poin persentase dibandingkan garis dasar RT-DETR-r18 (89,1 persen dan 62,8 persen). Presisi mencapai 90,5 persen, recall 85,8 persen, jumlah parameter 14,7 juta (turun 25,76 persen), penggunaan memori turun 25,14 persen, beban komputasi 55,5 GFLOPs, dan kecepatan 80,1 FPS pada RTX 3090 dengan masukan 640×640. Penghitungan memberi R² 0,9788, MAE 6,78 buah, dan RMSE 7,75 buah. Uji generalisasi pada VisDrone2019 menaikkan mAP50 dari 47,5 menjadi 50,5 persen dan mAP50-95 dari 29,1 menjadi 30,7 persen; pada TomatoPlantfactoryDataset, mAP50 naik dari 88,7 menjadi 90,5 persen dan mAP50-95 dari 68,5 menjadi 70,0 persen. Metrik mAP dihitung sebagai luas di bawah kurva presisi-recall pada berbagai ambang IoU; mAP50 memakai ambang 0,50 dan mAP50-95 dirata-ratakan atas ambang 0,50–0,95.

Penulis menyatakan beberapa batasan. Data berasal dari satu lokasi geografis dan terutama mencakup varietas Dongkui di Zhejiang, sehingga kinerja pada varietas, praktik budidaya, atau lingkungan daerah lain dapat berbeda. Skala data tergolong terbatas, dan pemrosesan lapisan P2 pada MDFFN masih menimbulkan beban komputasi tambahan. Penulis mengusulkan pengumpulan data lintas daerah dan varietas, teknik adaptasi domain, serta pengujian pada kebun komersial di lokasi lain sebagai kerja lanjutan.
