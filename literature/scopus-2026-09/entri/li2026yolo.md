# YOLO-MSRF: A Multimodal Segmentation and Refinement Framework for Tomato Fruit Detection and Segmentation with Count and Size Estimation Under Complex Illumination

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2026yolo` |
| Judul asli | YOLO-MSRF: A Multimodal Segmentation and Refinement Framework for Tomato Fruit Detection and Segmentation with Count and Size Estimation Under Complex Illumination |
| Penulis | Li, Ao; Wang, Chunrui; Wang, Aichen; Sun, Jianpeng; Gu, Fengwei; Zhang, Tianxue |
| Tahun | 2026 |
| Venue | Agriculture Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [li2026yolo.pdf](../pdf/li2026yolo.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture16020277

## Gambaran Umum

Penelitian ini mengatasi kesulitan segmentasi semantik buah tomat di bawah pencahayaan kompleks, khususnya cahaya rendah dan paparan berlebih, yang membuat metode berbasis RGB saja menghasilkan batas objek kabur dan melewatkan buah kecil atau tertutup. Penulis juga menilai bahwa fusi multimodal sederhana belum memanfaatkan isyarat saling melengkapi dari tiap modalitas secara optimal. Tujuan penelitian adalah membangun kerangka segmentasi dan penyempurnaan multimodal RGB–near-infrared (NIR) yang ringan untuk persepsi tomat di pertanian fasilitas, sekaligus mendukung penghitungan, estimasi ukuran, analisis kematangan, dan prediksi hasil panen.

Tanaman yang dipakai adalah tomat satu kultivar dalam satu rumah kaca. Data berasal dari Multimodal Image Dataset of Tomato Fruits with Different Maturity, yang memuat 4.000 himpunan citra multimodal di bawah empat kondisi pencahayaan, yaitu alami, buatan, rendah, dan kuning natrium, dengan anotasi deteksi dan segmentasi untuk tiga tahap kematangan: mentah, setengah matang, dan matang. Penulis memilih 1.389 citra dan membaginya sekitar 70% latih, 15% uji, dan 15% validasi, dengan pembagian identik untuk citra RGB dan NIR. Model dibangun di atas Ultralytics YOLO11 dan dilatih 150 epoch dengan masukan 640 × 640, ukuran batch 32, segmentasi satu kelas, pengoptimal SGD, dan presisi campuran pada satu GPU NVIDIA RTX 3090 24 GB.

Mekanisme deteksi memakai jaringan tulang punggung dua cabang, RGB dan NIR, dengan modul C-MDCF (Cross-Modality Difference Complement Fusion) yang menguraikan fitur menjadi komponen umum dan diferensial, lalu memberi bobot selisih antarkanal melalui *global average pooling* dan sigmoid agar tiap modalitas melengkapi modalitas lain secara selektif. Modul ringan C2f-DCB menggabungkan konvolusi grup 3 × 3 dan konvolusi titik 1 × 1. MS-CPAM menggabungkan konvolusi 3D lintas skala dengan perhatian kanal dan posisi untuk target kecil atau tertutup, sedangkan MSF-SRNet memakai Scale-Concat dan injeksi detail semantik (SDI) berbasis produk Hadamard. Untuk penghitungan, penulis memakai pelacak DeepSORT dengan mekanisme penyambungan kembali lintasan: lintasan yang hilang disimpan dalam daftar kandidat dan dicocokkan ulang berdasarkan konsistensi kelas, kemiripan tampilan, jarak spasial, dan selang waktu. Estimasi ukuran memakai fitting elips transformasi Hough pada mask yang tertutup sebagian, dengan diameter ekuivalen 2√(ab) dan agregasi median lintas frame.

Pada himpunan validasi campuran empat pencahayaan, model lengkap mencapai mAP50 97,8%, mAP50–95 79,1%, dan mIoU 77,53 dengan 4,10 juta parameter, 14,6 GFLOPs, dan 105,07 FPS; model dasar YOLO11 mencatat 95,5%, 76,7%, dan 73,93. Setiap varian ablasi diulang lima kali dengan benih acak berbeda dan diuji dengan uji-t berpasangan pada α = 0,05. Tabel 6 melaporkan akurasi penghitungan rata-rata di atas 90% dan mAP50 kotak maksimum 98,90% pada empat video: video1 mencatat 37 deteksi DeepSORT berbanding 35 anotasi manual (88,96%) dan video3 mencatat 75 berbanding 79 (94,87%). Angka FPS diukur pada RTX 3090 dan tidak memasukkan beban pelacakan DeepSORT.

Batasan yang dinyatakan penulis meliputi penggunaan satu rumah kaca dan satu kultivar tomat tanpa pemandangan lapangan terbuka maupun beberapa kultivar; generalisasi ke rumah kaca, sistem kamera, dan varietas lain dapat terpengaruh oleh pergeseran domain. Kerangka bergantung pada masukan RGB–NIR, sehingga kinerja menurun bila sensor NIR tidak tersedia dan sistem beralih ke konfigurasi RGB saja (mAP50 turun menjadi 95,5%). DeepSORT berisiko mengalami pertukaran identitas pada oklusi panjang atau tumpang tindih parah. Penulis belum mengatasi kabur gerak antarsensor akibat getaran kendaraan tanpa *global shutter*, belum menguji latensi pada platform tertanam seperti Jetson atau Edge TPU, dan belum melakukan pembelajaran lintas tanaman, pembelajaran tanpa pengawasan, pemodelan temporal, maupun kuantisasi model.

