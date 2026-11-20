# FGfuse-Net: A frequency guided dual-branch fusion model for multi-stage maturity tomato detection and counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tang2026fgfuse` |
| Judul asli | FGfuse-Net: A frequency guided dual-branch fusion model for multi-stage maturity tomato detection and counting |
| Penulis | Tang, Qiang; Chen, Siqi; Cao, Wenhao; Wei, Ye; Wang, Yuwei; Rao, Yuan; Liu, Lu; Hou, Wenhui |
| Tahun | 2026 |
| Venue | Smart Agricultural Technology |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [tang2026fgfuse.pdf](../pdf/tang2026fgfuse.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2026.102194

## Gambaran Umum

Deteksi dan pencacahan buah tomat di rumah kaca penting untuk prediksi hasil dan panen otomatis. Kondisi rumah kaca yang sebenarnya menimbulkan sejumlah kendala, antara lain variasi pencahayaan, daun yang menutupi buah, dan latar belakang yang kompleks. Penulis menyatakan bahwa model yang hanya memakai citra RGB menjadi tidak andal pada kondisi cahaya rendah, karena informasi warna berkurang dan akurasi deteksi turun. Tomat pada tahap kematangan yang berbeda juga memiliki gradasi warna yang kontinu, sementara warna buah yang belum matang sering mirip dengan daun. Penelitian ini bertujuan mengusulkan FGfuse-Net, model deteksi tomat multi-tahap kematangan yang dipandu oleh informasi frekuensi tinggi dan dapat menghitung buah pada setiap tahap.

Data dikumpulkan pada Juni 2024 di rumah kaca tomat Pusat Penelitian Ilmu Pertanian Shucheng, Provinsi Anhui, Tiongkok. Kendaraan roda empat diferensial yang dikendalikan jarak jauh bergerak dengan kecepatan konstan 1 m/s di sepanjang baris tanaman. Kamera Intel RealSense D455 dipasang pada ketinggian 0,75 m di atas tanah, dengan jarak pemotretan 0,1 hingga 1,5 m, resolusi 1280 × 720 piksel, dan 30 bingkai per detik. Sebanyak 800 citra dipotong menjadi 640 × 640 piksel, lalu dibagi secara acak dengan rasio 7:2:1 untuk latih, validasi, dan uji. Setelah augmentasi berupa perubahan kecerahan, pembalikan, dan penambahan derau *Gaussian*, jumlah citra menjadi 2142, yang terdiri atas 1500 citra latih, 428 citra uji, dan 214 citra validasi. Setiap buah dianotasi dengan *bounding box* menggunakan LabelImg. Tiga kelas kematangan yang digunakan adalah *ripe*, *halfripe*, dan *unripe*. Untuk pengujian pencacahan, 600 citra dipilih dari set uji dan validasi, lalu dihitung per kelompok lima citra agar galat relatif tidak tidak terdefinisi pada citra dengan nol atau satu buah per kelas.

Model menggabungkan dua cabang ekstraksi fitur, yaitu cabang RGB dan cabang fitur yang diperkaya frekuensi. Modul FGFF memakai transformasi Fourier dan filter *high-pass* Gaussian untuk menggabungkan fitur ruang yang telah diperkaya dengan informasi frekuensi tinggi. Modul MSWE memakai transformasi *wavelet* untuk menangkap kontur global dan detail lokal, sedangkan *Unified-IoU* dipakai untuk mengatasi ketidakseimbangan gradien pada adegan buah yang padat. Pada data asli, mAP@0,5 FGfuse-Net adalah 92,3% dan F1 adalah 90,6%. Setelah augmentasi, nilainya naik menjadi 96,4% dan 94,5%, masing-masing naik 4,1% dan 3,9%. Pada uji ablasi dengan YOLOv8n sebagai dasar, penambahan FGFF meningkatkan mAP@0,5 sebesar 1,7% dan *recall* sebesar 3,3%. Pada pencacahan, FGfuse-Net mengungguli YOLOv8n di setiap tahap kematangan. Untuk tomat *ripe*, R² naik menjadi 0,98, sedangkan RMSE, MAPE, dan RRMSE turun lebih dari 30%. YOLOv8n pada kelas *ripe* memiliki R² 0,94, RMSE 1,64, dan MAPE 9,4. Pada kelas *halfripe*, R² YOLOv8n adalah 0,89 dan RMSE-nya 1,71. Penulis menyimpulkan bahwa model ini mengungguli jaringan deteksi arus utama, meski angka lengkap untuk FGfuse-Net pada kelas *halfripe* dan *unripe* tidak tercantum dalam bagian yang dibaca.

Penulis menyatakan beberapa batasan. Hasil dapat berbeda antarvarietas tomat dan antarpola pengelolaan rumah kaca. Kinerja model juga dapat menurun pada kondisi ekstrem, seperti kelembapan tinggi dan debu. Penulis mencatat pula biaya energi untuk pelatihan model serta kemungkinan dampak otomatisasi terhadap tenaga kerja. Untuk penelitian lanjutan, penulis berencana mengembangkan model *transformer* yang lebih ringan, melakukan *pruning* atau kuantisasi, menguji model pada perangkat *edge* sungguhan, dan memperluas dataset dengan variasi varietas, struktur rumah kaca, dan musim tanam.
