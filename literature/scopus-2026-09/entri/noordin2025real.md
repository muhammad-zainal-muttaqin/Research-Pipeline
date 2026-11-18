# Real-time FFB ripeness detection using IoT-enabled YOLOv8n on Raspberry Pi 4 edge devices for precision agriculture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `noordin2025real` |
| Judul asli | Real-time FFB ripeness detection using IoT-enabled YOLOv8n on Raspberry Pi 4 edge devices for precision agriculture |
| Penulis | Noordin, Nurul Hazlina; Samad, Rosdiyana; Abdul Malek, Abdul Haikal |
| Tahun | 2025 |
| Venue | Journal of Mechatronics Electrical Power and Vehicular Technology |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm, other berries |

## Tautan Akses
- PDF: [noordin2025real.pdf](../pdf/noordin2025real.pdf)
- DOI resmi: https://doi.org/10.55981/j.mev.2025.1220

## Gambaran Umum

Penelitian ini bertujuan membangun sistem deteksi kematangan tandan buah segar (TBS) kelapa sawit secara langsung di perangkat tepi (*edge device*) dengan biaya rendah. Pemeriksaan kematangan manual dianggap memakan tenaga dan rentan terhadap kesalahan. Penulis memilih YOLOv8n karena ukurannya ringan, lalu menyesuaikannya agar berjalan pada Raspberry Pi 4 Model B di lingkungan perkebunan tropis. Sistem ini juga mencatat lokasi dan kondisi lingkungan setiap kali deteksi dilakukan.

Data berupa 4.194 citra TBS beranotasi yang diberi label tiga tingkat kematangan, yaitu kurang masak, masak, dan terlalu masak. Anotasi memakai Roboflow. Pembagian data adalah 3.681 citra latih (88%), 348 citra validasi (8%), dan 165 citra uji (4%). Pra-pemrosesan mencakup pelurusan otomatis, pengubahan ukuran dari 3024×4032 menjadi 640×640 piksel, pembalikan horizontal, rotasi 90°, pemotongan acak dengan zoom 0–20%, serta konversi ke abu-abu pada 15% citra. Augmentasi diterapkan untuk memperluas data dan mengurangi overfitting.

Mekanisme deteksi memakai model YOLOv8n terlatih (*pre-trained*) yang disetel ulang pada data tersebut. Model menghasilkan kotak pembatas di sekitar buah beserta label kematangannya. Perangkat memakai Raspberry Pi 4 dengan SoC Broadcom BCM2711, CPU ARM Cortex-A72 empat inti 1,5 GHz, RAM 4 GB, kamera Raspberry Pi V2 8 MP melalui antarmuka CSI, serta kipas yang diatur dalam sistem gelung tertutup. Modul GPS Neo 6M mencatat koordinat dan sensor BME280 mencatat suhu, kelembapan, dan tekanan. Data disimpan sementara dalam berkas JSON saat jaringan terputus, lalu dikirim melalui LoRaWAN ke gerbang dan dilanjutkan ke cloud memakai MQTT. Abstrak menyebut kuantisasi dan akselerasi perangkat keras, tetapi rincian kedua teknik itu tidak dinyatakan dalam teks. Sistem memiliki dua mode, yaitu mode kamera untuk deteksi dan mode GPS untuk pencatatan lokasi, dengan dasbor untuk menampilkan hasil.

Penulis melaporkan *average precision* (AP) 0,898 dan *mean average precision* (mAP) 0,952. Nilai *average recall* (AR) untuk ketiga kelas adalah 0,945. Tabel perbandingan mencantumkan presisi 0,952 dan recall 0,945 untuk metode yang diusulkan. Acuan hitung untuk ketiga angka itu tidak dinyatakan secara eksplisit, khususnya apakah dihitung pada cawat uji 165 citra atau pada cawat validasi. Pengujian lapangan dilakukan dengan dua kelompok yang memindai TBS di tanah dan di pohon. Sistem mendeteksi buah di pohon sampai ketinggian setara mata sekitar enam kaki; akurasi turun pada pohon lebih tinggi karena buah tertutup daun dan sudut kamera kurang sesuai.

Batasan yang dinyatakan penulis mencakup penurunan akurasi pada pohon tinggi, keterbatasan resolusi kamera, serta kondisi pencahayaan dan bayangan yang beragam. Penggunaan berkepanjangan di iklim tropis berisiko menaikkan suhu Raspberry Pi dan menurunkan kinerja. Penulis mengusulkan kamera beresolusi lebih tinggi, kamera teleskopik atau kalibrasi tinggi pohon, data latih yang lebih beragam, pendinginan tambahan, dan perluasan sistem ke pemantauan penyakit.

