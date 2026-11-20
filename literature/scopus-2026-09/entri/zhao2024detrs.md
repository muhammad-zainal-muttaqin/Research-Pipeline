# DETRs Beat YOLOs on Real-time Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhao2024detrs` |
| Judul asli | DETRs Beat YOLOs on Real-time Object Detection |
| Penulis | Zhao, Yian; Lv, Wenyu; Xu, Shangliang; Wei, Jinman; Wang, Guanzhong; Dang, Qingqing; Liu, Yi; Chen, Jie |
| Tahun | 2024 |
| Venue | Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [zhao2024detrs.pdf](../pdf/zhao2024detrs.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr52733.2024.01605

## Gambaran Umum

Artikel ini mengusulkan RT-DETR, detektor objek *end-to-end* berbasis Transformer yang bekerja secara waktu nyata. Masalah utamanya adalah detektor YOLO bergantung pada *Non-Maximum Suppression* (NMS), yang memperlambat inferensi dan memperkenalkan dua ambang batas—ambang kepercayaan dan ambang IoU—sehingga kecepatan dan akurasi menjadi tidak stabil. Di sisi lain, detektor berbasis DETR menghilangkan NMS tetapi biaya komputasinya tinggi sehingga belum memenuhi kebutuhan waktu nyata. Penulis menganalisis pengaruh NMS dan menunjukkan bahwa waktu eksekusinya bergantung pada jumlah kotak prediksi dan kedua ambang batas tersebut. Kebaruan yang diklaim terdiri atas detektor *end-to-end* waktu nyata pertama, analisis kuantitatif dampak NMS beserta tolok ukur kecepatan *end-to-end*, serta kemampuan penyesuaian kecepatan tanpa pelatihan ulang.

Tanaman dan data pertanian tidak dinyatakan; data yang dipakai adalah dataset deteksi objek umum MS COCO val2017 untuk evaluasi dan Objects365 untuk prapelatihan. Mekanisme deteksi yang dibangun terdiri atas tiga bagian, yaitu *backbone*, encoder hibrida efisien, dan decoder Transformer dengan kepala prediksi bantu. Fitur dari tiga tahap terakhir *backbone* (S3, S4, S5) dimasukkan ke encoder. Encoder hibrida memisahkan interaksi intra-skala dan fusi lintas-skala melalui dua modul: AIFI (*Attention-based Intra-scale Feature Interaction*) yang melakukan interaksi hanya pada S5 memakai *self-attention*, serta CCFF (*CNN-based Cross-scale Feature Fusion*) yang menyatukan S3, S4, dan F5 lewat blok fusion berbasis RepConv. Seleksi kueri dengan ketidakpastian minimum mendefinisikan ketidakpastian sebagai selisih antara distribusi lokalisasi dan klasifikasi, lalu memasukkannya ke fungsi rugi agar kueri awal decoder memiliki kualitas tinggi. Kecepatan dapat diatur dengan mengurangi jumlah lapisan decoder tanpa pelatihan ulang.

Penulis membangun tolok ukur kecepatan *end-to-end* dengan menambahkan plugin NMS TensorRT pada detektor YOLO dan menguji pada COCO val2017 dengan T4 GPU dan TensorRT FP16. Pada Tabel 1, YOLOv8 dengan ambang IoU 0,5; 0,6; dan 0,8 menghasilkan AP 52,1%; 52,6%; dan 52,8% dengan waktu NMS 2,24; 2,29; dan 2,46 ms. Dengan ambang kepercayaan 0,001; 0,01; dan 0,05 pada IoU 0,7, AP berturut-turut 52,9%; 52,4%; dan 51,2%, sedangkan waktu NMS 2,36; 1,73; dan 1,06 ms.

Hasil utama pada Tabel 2 menunjukkan RT-DETR-R50 mencapai AP 53,1% dengan 108 FPS pada T4 GPU, 42 juta parameter, dan 136 GFLOPs; RT-DETR-R101 mencapai AP 54,3% dengan 74 FPS, 76 juta parameter, dan 259 GFLOPs. Sebagai perbandingan, YOLOv8-L mencatat 52,9% AP dan 71 FPS, YOLOv8-X 53,9% AP dan 50 FPS, serta DINO-Deformable-DETR-R50 50,9% AP dan 5 FPS. RT-DETR-R50 mengungguli DINO-R50 sebesar 2,2% AP dan sekitar 21 kali kecepatan. Setelah prapelatihan dengan Objects365, RT-DETR-R50 dan R101 mencapai 55,3% dan 56,2% AP. Penulis juga melaporkan varian yang lebih ringan dengan backbone ResNet18/34 atau CSPResNet yang mengungguli model YOLO ukuran S dan M.

Batasan yang dinyatakan penulis adalah kinerja pada objek kecil masih lebih rendah daripada detektor waktu nyata kuat lainnya, sebagaimana umum pada DETR. RT-DETR-R50 mencatat AP untuk objek kecil 0,5% lebih rendah daripada YOLOv8-L, sedangkan RT-DETR-R101 mencatat 0,9% lebih rendah daripada YOLOv7-X. Arah lanjutan yang disebutkan adalah melakukan distilasi detektor ringan memakai model DETR besar yang telah dilatih dengan akurasi tinggi, karena decoder RT-DETR bersifat homogen dengan decoder DETR lain.
