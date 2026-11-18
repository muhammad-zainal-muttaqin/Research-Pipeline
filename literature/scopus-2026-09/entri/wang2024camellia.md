# Camellia oleifera Fruit Static and Dynamic Detection Counting Based on Improved COF-YOLO v8n

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2024camellia` |
| Judul asli | Camellia oleifera Fruit Static and Dynamic Detection Counting Based on Improved COF-YOLO v8n |
| Penulis | Wang, J.; others |
| Tahun | 2024 |
| Venue | Nongye Jixie Xuebao Transactions of the Chinese Society for Agricultural Machinery |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | camellia |

## Tautan Akses
- PDF: [wang2024camellia.pdf](../pdf/wang2024camellia.pdf)
- DOI resmi: https://doi.org/10.6041/j.issn.1000-1298.2024.04.019

## Gambaran Umum

Makalah ini mengusulkan metode deteksi dan penghitungan buah Camellia oleifera untuk masukan citra statis maupun video. Fokus permasalahannya adalah okklusi parah, warna buah yang mirip dengan latar, dan ukuran target kecil. Penulis menyatakan bahwa YOLOv8n sebelum dimodifikasi menghasilkan akurasi rendah dan banyak deteksi yang terlewat pada kondisi tersebut.

Citra diambil di kebun Camellia oleifera di Jiangning, Nanjing, memakai kamera ZED-Mini pada cuaca cerah dan mendung antara pukul 07.00-11.00 serta 13.00-18.00. Pengambilan menghasilkan 788 citra. Augmentasi dengan OpenCV berupa derau Gaussian dan garam-merica, transformasi affine, translasi, dan pembalikan menghasilkan 3.566 citra yang diberi label memakai LabelImg. Label dibagi menjadi okklusi berat, yaitu bagian buah tertutup lebih dari seperempat, sebanyak 6.778 label, serta okklusi ringan atau tanpa okklusi sebanyak 6.989 label. Perbandingan kedua kelas sekitar 1:1 dengan pembagian data latih dan validasi 8:2.

Modifikasi terhadap YOLOv8n terdiri atas tiga bagian. MPDIOU dipakai sebagai fungsi rugi untuk mengatasi deteksi yang terlewat akibat buah saling menimpa. Sebuah lapisan deteksi target kecil ditambahkan agar buah berukuran kecil dan buah yang tertutup daun tetap terdeteksi. Modul SCConv menggantikan C2f supaya akurasi dan kecepatan tetap seimbang. Model hasil disebut COF-YOLOv8n. Untuk penghitungan dinamis, keluaran detector dijadikan masukan DeepSORT sehingga pelacakan multiobjek menghasilkan jumlah buah. Penulis juga menurunkan resolusi citra untuk mensimulasikan kondisi pengambilan di lapangan.

Abstrak melaporkan COF-YOLOv8n mencapai presisi 97,7%, recall 97%, dan mAP 99%, masing-masing naik 3,2; 4,8; dan 2,4 poin persentase dibanding YOLOv8n. Pada kondisi okklusi parah, ketiga angka menjadi 95,9%, 95%, dan 98,5%, naik 4,0; 9,1; dan 4,6 poin persentase. Model dinyatakan cukup sederhana untuk disematkan pada lengan robot dan dipakai dalam estimasi produksi kebun.

Ditinjau dari penghitungan lintas pandang, makalah ini menangani penghitungan ganda terutama melalui pelacakan video pada satu alur kamera. Pencocokan langsung antara pandangan yang berbeda tidak dijelaskan pada bagian OCR yang terbaca.

