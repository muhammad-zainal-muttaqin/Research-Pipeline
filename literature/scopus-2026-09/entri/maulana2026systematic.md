# Systematic Review of Quantization-Optimized Lightweight Transformer Architectures for Real-Time Fruit Ripeness Detection on Edge Devices

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `maulana2026systematic` |
| Judul asli | Systematic Review of Quantization-Optimized Lightweight Transformer Architectures for Real-Time Fruit Ripeness Detection on Edge Devices |
| Penulis | Maulana, Donny; Ramasamy, R Kanesaraj |
| Tahun | 2026 |
| Venue | Computers |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | other berries |

## Tautan Akses
- PDF: [maulana2026systematic.pdf](../pdf/maulana2026systematic.pdf)
- DOI resmi: https://doi.org/10.3390/computers15010069

## Gambaran Umum

Tinjauan sistematis ini mengkaji inferensi visual waktu nyata pada perangkat keras berdaya rendah untuk deteksi kematangan buah. Vision Transformer dan Detection Transformer memiliki akurasi tinggi, tetapi menuntut daya hitung dan memori besar sehingga sulit dipasang pada platform tepi seperti NVIDIA Jetson dan Raspberry Pi. Penulis memusatkan perhatian pada tiga teknik pemampatan, yaitu kuantisasi, pemangkasan, dan distilasi pengetahuan, serta pada trade-off antara efisiensi dan akurasi. Khususnya, kuantisasi bit rendah menurunkan akurasi, terutama pada mekanisme perhatian Transformer, dan pelatihan sadar kuantisasi (*quantization-aware training*, QAT) secara konsisten mengungguli kuantisasi pascalatih (*post-training quantization*, PTQ). Asosiasi lintas pandang dan penghitungan buah unik tidak dibahas.

Data dan metode mengikuti pedoman PRISMA 2020. Pencarian dilakukan pada enam basis data, yaitu Scopus, Web of Science, IEEE Xplore, ScienceDirect, MDPI, dan SpringerLink, untuk periode Januari 2018 hingga Juni 2025. Kata kunci mencakup tiga tema, yakni arsitektur (RT-DETR, Q-DETR, lightweight Transformer), teknik optimasi (QAT, pemangkasan, distilasi pengetahuan), dan konteks aplikasi (deteksi buah, kematangan mangga, edge AI). Dari 160 rekaman awal, 32 duplikat dibuang sehingga tersisa 128; penyaringan judul dan abstrak menyingkirkan 89 rekaman; penilaian teks lengkap pada 39 rekaman berujung pada pengeluaran 17 kajian, sehingga 22 kajian dianalisis. Dua penulis menyaring secara mandiri dan perbedaan diselesaikan melalui konsensus atau penulis ketiga. Tanaman yang dikaji meliputi pisang, sawit, jeruk, tomat, delima, dan buah campuran.

Mekanisme yang dirangkum mencakup evolusi arsitektur dan pemampatan. DETR melakukan prediksi himpunan end-to-end sehingga menghilangkan *non-maximum suppression* (NMS); RT-DETR memakai encoder hibrida yang memisahkan pemrosesan intra-skala dan fusi lintas-skala guna menurunkan komputasi berulang; Deformable DETR hanya menghadiri sejumlah titik sampel kunci di sekitar titik acuan sehingga mempercepat konvergensi. Kuantisasi menurunkan presisi dari FP32 ke INT8 atau INT4 memakai parameter skala dan titik nol, dengan akselerasi 3,2–8 kali; pemangkasan terstruktur lebih cocok untuk tepi karena menjaga bentuk tensor ramah perangkat keras; distilasi pengetahuan memindahkan representasi dari model guru ke model murid. Q-DETR memakai *distribution rectification distillation* untuk mengatasi penurunan akurasi akibat kuantisasi.

Angka hasil dihimpun dari kajian-kajian dalam korpus dan bukan dari percobaan penulis sendiri, sehingga tinjauan ini tidak memiliki acuan hitung tunggal. MobileNetV2 pada pisang mencapai akurasi 97,0% pada 15 FPS di Raspberry Pi 4 dengan daya 5 W; EfficientNet-B0 pada sawit mencapai 89,3% dengan kuantisasi float16, ukuran model turun 50% dengan waktu inferensi 96 ms; YOLOv5-CS pada jeruk hijau mencapai mAP 98,23% dengan latensi 0,037 detik atau 28 FPS di Jetson Xavier NX. ORD-YOLO mencapai mAP 96,92% pada jeruk, naik 3% atas YOLOv8; RT-DETR meraih 53,1% AP pada COCO dengan 108 FPS di T4; Deformable DETR mencapai mAP 91,2% pada 45 FPS. Q-DETR dengan kuantisasi 4 bit mencapai 39,4% AP, hanya turun 2,6% dari model presisi penuh dengan akselerasi teoritis 6,6 kali; QAT memberi perbaikan 0,5–1,5% atas PTQ pada lebar bit sama. Metrik yang dipakai mencakup akurasi, mAP, AP, FPS, waktu inferensi, daya, ukuran model, dan MCC untuk data tidak seimbang.

Batasan yang dinyatakan penulis meliputi ketidakstabilan kuantisasi pada modul *multi-head attention*, yang 3–5 kali lebih sensitif daripada lapisan konvolusi dan memerlukan presisi sekurangnya 6 bit; data masih bias pada buah iklim sedang karena tomat, jeruk, dan apel menyusun 67% fokus penelitian, sementara durian, rambutan, dan manggis kurang terwakili; hanya 23% kajian menguji pada perangkat tepi fisik di lapangan, dengan penurunan FPS efektif 15–20% akibat pencahayaan dan latar belakang. Penulis juga mencatat biaya komputasi Transformer yang tinggi serta perlunya tolok ukur perangkat keras heterogen. Arah masa depan yang diusulkan adalah optimasi sadar perangkat keras, ketahanan terhadap data tidak seimbang, integrasi penginderaan multimodal, dan penggunaan MCC sebagai metrik utama.
