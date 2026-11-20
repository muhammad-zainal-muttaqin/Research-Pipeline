# Developing Machine Vision in Tree-Fruit Applications—Fruit Count, Fruit Size and Branch Avoidance in Automated Harvesting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `neupane2024developing` |
| Judul asli | Developing Machine Vision in Tree-Fruit Applications—Fruit Count, Fruit Size and Branch Avoidance in Automated Harvesting |
| Penulis | Neupane, Chiranjivi; Walsh, Kerry B.; Goulart, Rafael; Koirala, Anand |
| Tahun | 2024 |
| Venue | Sensors |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | mango |

## Tautan Akses
- PDF: [neupane2024developing.pdf](../pdf/neupane2024developing.pdf)
- DOI resmi: https://doi.org/10.3390/s24175593

## Gambaran Umum

Penelitian ini membandingkan model arsitektur utama, khususnya YOLOv8 dan YOLOv9, dengan model yang dirancang khusus untuk tiga aplikasi buah pohon, yaitu penghitungan buah, pengukuran ukuran buah, dan penghindaran cabang pada pemanen otomatis. Penulis berpendapat bahwa perbandingan model harus memakai himpunan latih dan uji yang sama, kinerja pelatihan ulang perlu didokumentasikan karena proses pelatihan bersifat stokastik, dan himpunan data perlu dirilis agar hasil dapat dievaluasi kembali. Tujuannya adalah menilai kinerja model generasi terbaru secara spesifik per aplikasi, bukan menerima begitu saja nilai kinerja yang dilaporkan pada dataset umum.

Studi memakai tiga himpunan data kebun mangga di Central Queensland, Australia. Dataset-A memuat citra RGB kanopi dengan label kotak buah untuk penghitungan; Dataset-B memuat citra RGB dengan label segmentasi instans buah untuk pengukuran; Dataset-C dibuat baru memakai kamera RGB-D Azure Kinect yang dipasang pada kendaraan berkecepatan sekitar 7 km/jam dengan pencahayaan LED saat malam hari, menghasilkan 200 ubin citra berukuran 640 × 540 piksel untuk latih dan 50 untuk uji dengan dua kelas, yaitu buah dan cabang. Model yang diuji mencakup lima ukuran YOLOv8 untuk deteksi dan segmentasi, YOLOv9 (gelan-c), serta Mask R-CNN berbasis ResNet-50 dan ResNet-101 sebagai acuan. Pelatihan memakai masukan 640 piksel, ukuran batch 16, laju pembelajaran 0,01, momentum 0,937, dan 100 epoch dengan transfer learning dari COCO; sepuluh seed berbeda dipakai untuk mengukur variasi akibat proses stokastik. Metrik yang dipakai adalah presisi, recall, skor F1, mAP50, dan mAP50-95.

Pada penghitungan buah, model deteksi menghasilkan lokasi buah yang kemudian dihitung; penulis mengutip kajian sebelumnya yang menyatakan bahwa faktor koreksi dari hitungan manual masih diperlukan untuk buah yang benar-benar tertutup. Pada pengukuran, model segmentasi menghasilkan topeng buah, lalu tinggi dan lebar topeng dalam piksel dikonversi ke milimeter memakai jarak kamera ke buah dari citra kedalaman; filter elips dipakai untuk menyingkirkan buah yang tertutup atau tersegmentasi secara buruk. Pada penghindaran cabang, YOLOv8m-seg memisahkan buah dan cabang, piksel kedalaman pada cabang tersegmentasi diubah menjadi awan titik tiga dimensi, lalu setiap titik diuji terhadap ruang kerja lengan pemanen. Ruang kerja berbentuk prisma segi empat ketika platform pemanen berhenti dan prisma trapesium ketika platform bergerak vertikal; pengujian memakai pertidaksamaan rentang koordinat untuk prisma pertama dan persamaan bidang dari tiga titik sudut untuk prisma kedua.

Koefisien variasi mAP50 dari sepuluh pelatihan ulang YOLOv8m sekitar 0,2% untuk deteksi buah, 1% untuk segmentasi buah, dan 2% untuk segmentasi cabang; penulis memakai nilai ini sebagai penimbang apakah selisih antarmodel bermakna. YOLOv8m mencapai mAP50 99,29% dengan waktu inferensi 14,1 ms pada deteksi buah, mengungguli MangoYOLO yang mencapai 98,55% dengan 15 ms, sedangkan YOLOv8s mencapai 99,31% dengan 7,7 ms. Pada segmentasi dengan data buah dan cabang, YOLOv8m-seg mencapai mAP50 80,5% untuk buah dan 63,2% untuk cabang, sedangkan Mask R-CNN dengan ResNet-101 masing-masing mencapai 67,8% dan 67,2%; dengan data buah saja, YOLOv8s-seg mencapai mAP50 98,7%. Pada pengukuran panjang buah, Mask R-CNN menghasilkan galat RMSE 4,7 mm untuk kultivar Honey Gold dan 5,1 mm untuk Keitt, sedangkan YOLOv8m-seg menghasilkan 4,4 mm dan 7,5 mm sebelum koreksi bias. Penyaringan awan titik sekitar 4,2 juta titik untuk penghindaran cabang memakan waktu kurang dari 2,1 ms pada Jetson AGX Orin dengan CUDA.

Penulis mencatat sejumlah keterbatasan. Pendekatan penghindaran cabang secara teori benar, tetapi waktu komputasi dapat menjadi hambatan karena sistem menargetkan 25 frame per detik sehingga setiap frame hanya memiliki waktu kurang dari 40 ms; desain robot dengan banyak lengan memperkuat kebutuhan akan penyaringan prisma segi empat dan penggunaan CUDA. TensorRT dapat mempercepat inferensi, tetapi terikat pada perangkat keras NVIDIA modern dan konversi ke FP-16 dapat menurunkan akurasi secara kecil. Pelabelan cabang lebih bergantung pada interpretasi operator daripada pelabelan buah karena cabang bertekstur, berwarna gelap, dan sering berada di bawah bayangan. Penulis juga menyatakan bahwa penyebab ketidaksesuaian nilai bias pada kultivar Keitt tidak jelas. Selain itu, penulis menganjurkan perilisan himpunan latih dan uji serta pendokumentasian variasi pelatihan ulang pada setiap studi perbandingan model.
