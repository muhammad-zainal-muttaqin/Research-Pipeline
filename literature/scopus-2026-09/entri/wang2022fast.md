# Fast and precise detection of litchi fruits for yield estimation based on the improved YOLOv5 model

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2022fast` |
| Judul asli | Fast and precise detection of litchi fruits for yield estimation based on the improved YOLOv5 model |
| Penulis | Wang, Lele; Zhao, Yingjie; Xiong, Zhangjun; Wang, Shizhou; Li, Yuanhong; Lan, Yubin |
| Tahun | 2022 |
| Venue | Frontiers in Plant Science |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | litchi/longan |

## Tautan Akses
- PDF: [wang2022fast.pdf](../pdf/wang2022fast.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2022.965425

## Gambaran Umum

Penelitian ini bertujuan mendeteksi buah leci yang tumbuh rapat dan menentukan tingkat kematangannya secara cepat dan tepat untuk estimasi hasil di kebun dan pemanenan robotik. Lingkungan tumbuh yang kompleks, sebaran buah yang rapat, serta penutupan oleh daun, ranting, dan buah lain membuat keluaran metode visual menyimpang dari nilai aktual. Penulis mengusulkan model YOLOv5 yang dimodifikasi beserta aplikasi Android untuk penghitungan buah dan estimasi hasil.

Tanaman yang diteliti adalah leci (*Litchi chinensis*). Citra RGB diambil di Taman Pameran Leci, Distrik Conghua, Guangzhou, Guangdong, Tiongkok, antara pukul 09.00 dan 18.00 pada 17 Mei, 11 Juni, dan 30 Juni 2021. Kamera utama ponsel 40 megapiksel (sensor Sony IMX600) dipakai dengan resolusi 3648×2736 piksel, jarak 2–5 m, dan sudut acak. Sejumlah 1.375 citra asli dikumpulkan, masing-masing memuat 10–100 buah, dengan total 53.855 label. Buah dibagi menjadi dua kelas, yaitu matang (`litchi`, merah) dan belum matang (`raw_litchi`, hijau kebiruan), dengan rasio antarkelas sekitar 1,28. Anotasi memakai LabelImg. Pembagian data 7:1:2 menghasilkan 962 citra latih, 138 validasi, dan 275 uji; setelah augmentasi, jumlah citra latih menjadi 5.772 dan total data 6.175.

Mekanisme deteksi memakai YOLOv5s versi 6.0 yang dimodifikasi. Tulang punggung CSP-Darknet53 diganti dengan ShuffleNet v2 yang disetel ulang: konvolusi pertama diubah dari 3×3 menjadi 6×6, blok ShuBlock ditumpuk, dan modul SPPF dipertahankan pada lapisan terakhir. Modul CBAM yang menggabungkan perhatian kanal dan spasial ditambahkan sebelum neck untuk memperkuat ciri buah dan menekan latar. Ukuran masukan diubah dari 640×640 menjadi 1280×1280 agar buah kecil lebih dikenali. Lapisan ke-21 sampai ke-23 serta kepala deteksi skala besar (20,20,512) dihapus, sehingga model hanya memiliki dua kepala deteksi. Pelatihan memakai PyTorch dengan laju pembelajaran awal 0,01, eta_min 2×10⁻³, momentum 0,937, peluruhan 5×10⁻³, ukuran kumpulan 8, T_max 250, pengoptimal AdamW, delapan pekerja, dan augmentasi Mosaic; pelatihan memakan waktu sekitar 28 jam pada RTX 2060 SUPER. Metrik yang dipakai adalah presisi, recall, skor F1, AP, mAP dengan IoU 0,5, jumlah parameter, ukuran model, dan FPS.

Hasil utama pada 275 citra uji adalah mAP@0,5 sebesar 92,4 persen dan skor F1 0,87 untuk kedua kelas gabungan, dengan presisi 87,6 persen dan recall 85,6 persen. Kelas matang mencapai presisi 88,1 persen, recall 88,4 persen, dan mAP 93,9 persen; kelas belum matang mencapai 87,1 persen, 82,7 persen, dan 90,8 persen. Ukuran model 5,1 MB dengan kecepatan 78,13 frame per detik pada keyakinan 0,5. Dibandingkan YOLOv5s awal yang mencatat mAP 88,9 persen, 7.015.519 parameter, 13,7 MB, dan 104,17 FPS, model akhir meningkatkan mAP 3,5 persen dan mengecilkan ukuran model 62,77 persen dengan 2.251.496 parameter. Model lain yang diuji ulang memberi mAP 88,9 persen (YOLOv5s), 74,7 persen (YOLOv4-tiny), 82,87 persen (MobileNetv3-YOLOv4), dan 69,13 persen (SSD dengan VGG). Pada uji kepadatan, satu buah terlewat pada citra ringan dan sedang, delapan pada citra padat, dengan laju terlewat di bawah 3 persen. Aplikasi Android yang dibangun dengan konversi PyTorch ke ONNX, lalu NCNN dan kuantisasi Fp16, diuji pada 30 citra uji yang masing-masing dijalankan tiga kali; korelasi R² terhadap jumlah buah aktual 0,9879, dengan waktu deteksi rata-rata 182 ms pada ponsel Kirin990.

Batasan yang dinyatakan penulis: buah pada masa transisi kematangan memiliki perbedaan warna yang tidak jelas sehingga klasifikasi berpindah antara matang dan belum matang. Pada kondisi cahaya belakang, daun leci yang menggulung dapat terdeteksi salah sebagai buah belum matang, dan kontur buah sulit diekstraksi. Buah dengan tumpang tindih atau penutupan berat dapat dianggap satu buah atau terlewat sehingga perkiraan hasil menjadi lebih rendah; sebaliknya, bagian yang teduh dan daun kering yang menyerupai buah dapat menaikkan perkiraan. Penulis juga menyebut himpunan data yang masih terbatas, distorsi dan kabur pada buah berjarak jauh, serta perlunya penyempurnaan kategori kematangan, perluasan data, dan perbaikan struktur tanaman untuk pemanenan mekanis.
