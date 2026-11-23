# Tomato Fruit 3D Reconstruction Based on Improved YOLOv8 and MiDaS Depth Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ye2024tomato` |
| Judul asli | Tomato Fruit 3D Reconstruction Based on Improved YOLOv8 and MiDaS Depth Estimation |
| Penulis | Ye, Rong; Shao, Guoqi; Gao, Yanjun; Li, Tong; Gao, Quan |
| Tahun | 2024 |
| Venue | Proceedings 2024 International Conference on Advances in Electrical Engineering and Computer Applications Aeeca 2024 |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [ye2024tomato.pdf](../pdf/ye2024tomato.pdf)
- DOI resmi: https://doi.org/10.1109/aeeca62331.2024.00093

## Gambaran Umum

Kajian ini membahas rekonstruksi tiga dimensi buah tomat di rumah kaca dari citra yang diambil dari beberapa sudut. Penulis menyebut dua masalah, yaitu parameter fenotipe tanaman yang tidak akurat dan status pertumbuhan yang tidak jelas dalam prediksi hasil panen. Mereka juga menyebut buah, daun, dan batang yang saling menutupi pada latar yang rumit.

Citra dikumpulkan di kebun percobaan tanaman tomat Pusat Diantai, Universitas Pertanian Yunnan. Peneliti memakai telepon genggam untuk memotret buah dari tiga sudut berbeda. Adegan berisi satu tomat, dua tomat, atau banyak tomat. Jumlah citra, jumlah buah, pemberi label, dan pembagian latih/uji tidak disebut. Citra dinormalisasi dan ditingkatkan sebelum dipakai membangun set data deteksi.

Metode memakai YOLOv8n yang ditambah CBAM (*Convolutional Block Attention Module*), modul atensi pada dimensi kanal dan spasial, di dalam modul C2f pada tulang punggung jaringan. Kedalaman diperkirakan dari satu citra RGB dengan MiDaS, model estimasi kedalaman monokular yang dilatih pada 12 set data. Rekonstruksi 3D dari satu citra dikerjakan dengan Wonder3D, yang membangkitkan peta normal dan citra warna konsisten antar-pandang, lalu menyatukannya menjadi jaring bertekstur. Model YOLOv8 dilatih 100 putaran.

Hasil kuantitatif satu-satunya adalah mAP@0,5 deteksi sebesar 99,3%, naik 1,9% dari model asli. Set data uji dan galat rekonstruksi tidak disebut. Hasil estimasi kedalaman dan rekonstruksi 3D hanya disajikan sebagai gambar dan dinilai secara visual sebagai "memuaskan".

Keterbatasan yang dapat diperiksa: tidak ada pencacahan buah dan tidak ada acuan hitung. Pembagian data tidak disebut, sehingga tidak jelas apakah mAP dihitung pada data uji terpisah. Kedalaman diperkirakan, bukan diukur dengan sensor, dan tidak dibandingkan dengan nilai acuan. Rekonstruksi 3D tidak dievaluasi secara kuantitatif. Wonder3D dilatih untuk satu citra dan tidak menggabungkan beberapa citra buah yang sama.
