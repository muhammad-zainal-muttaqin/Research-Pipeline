# Establishing a Standard Operating Procedure (SOP) for Palm Oil Plantation FFB Image Capture: Utilizing YOLOv8 for Counting and Ripeness Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hidayat2024establishing` |
| Judul asli | Establishing a Standard Operating Procedure (SOP) for Palm Oil Plantation FFB Image Capture: Utilizing YOLOv8 for Counting and Ripeness Classification |
| Penulis | Rizky Hidayat, Muhammad; Azarya Sulistyo, Pavel; Oktario, Hansen; Gunawan, Alexander A S; Mimboro, Prasetyo |
| Tahun | 2024 |
| Venue | 2024 6th International Conference on Cybernetics and Intelligent System Icoris 2024 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [hidayat2024establishing.pdf](../pdf/hidayat2024establishing.pdf)
- DOI resmi: https://doi.org/10.1109/icoris63540.2024.10903724

## Gambaran Umum

Penelitian ini bertujuan menyusun prosedur baku pengambilan citra tandan buah segar (TBS) di titik pengumpulan (TPH) agar sistem otomatis dapat mendeteksi, menghitung, dan mengklasifikasikan kematangan secara optimal. Pemeriksaan kematangan di TPH masih dilakukan manual oleh mandor panen dan asisten afdeling. Pemeriksaan yang lambat dapat menunda seluruh alur panen, menyebabkan truk menunggu, merusak jalan, dan menurunkan kapasitas pabrik. Penulis memilih YOLOv8n karena ringan dan dapat berjalan pada perangkat dengan spesifikasi terbatas di lapangan.

Data berupa 4.257 citra kumpulan TBS di TPH yang berasal dari perkebunan PTPN IV. Pra-pemrosesan mencakup pembersihan, pengubahan ukuran, pemberian kotak pembatas pada setiap objek, dan augmentasi berupa rotasi, pembalikan, serta perubahan pencahayaan. Kelas tandan mentah dan cacat jumlahnya sedikit karena kebijakan panen hanya memotong tandan matang. Rasio pembagian data ditunjukkan dalam gambar tetapi tidak dinyatakan dalam teks.

Model dibangun dengan transfer learning dari bobot terlatih Ultralytics dan penyetelan lanjutan. Konfigurasi pelatihan memakai `yolov8n.pt`, 200 epoch, 16 pekerja, ukuran masukan 800×800 piksel, ukuran batch otomatis, dan cache di memori. Penghitungan objek dilakukan dari kotak pembatas hasil deteksi dan ditampilkan melalui aplikasi web berbasis Streamlit. Mekanisme utama mencakup deteksi, klasifikasi kematangan per kotak, dan penghitungan jumlah tandan per kelas.

Akurasi yang dilaporkan adalah 96,56%, dihitung sebagai jumlah prediksi benar dibagi seluruh prediksi pada matriks konfusi. Cawat penghitungan angka ini tidak dinyatakan secara eksplisit. Penulis juga menyebut metrik mAP50 dan mAP50-95 mengalami kenaikan selama pelatihan, tetapi tidak mencantumkan nilainya. Prosedur baku yang diusulkan meminta pencahayaan cukup, sudut pengambilan 45°–90°, jumlah tandan di bawah 30, serta jarak pengambilan yang tidak terlalu dekat sehingga tidak memotong objek. Ambang keyakinan ditetapkan 40% untuk citra dengan banyak objek dan 60% untuk citra dengan sedikit objek.

Penulis menyatakan bahwa jarak pengambilan, pencahayaan, dan sudut kamera memengaruhi hasil deteksi, terutama pada citra dengan banyak tandan. Citra yang diambil lebih dekat menghasilkan deteksi lebih tepat daripada citra yang sama dari jarak lebih jauh. Penelitian lanjutan yang diusulkan mencakup data lebih besar dan beragam, fitur fisiologis dan kontekstual tambahan, penyetelan hyperparameter, serta versi YOLO yang lebih baru.

