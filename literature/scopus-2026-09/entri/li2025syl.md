# SYL-YOLOv8n: A lightweight and robust detector for peach recognition and yield estimation in complex orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2025syl` |
| Judul asli | SYL-YOLOv8n: A lightweight and robust detector for peach recognition and yield estimation in complex orchards |
| Penulis | Li, Xinlong; Liu, Haiteng; Lan, Yubin; Chen, Guanglong; Shan, Changfeng; Jiao, Lening; Liu, Jiatian; Wang, Huizheng |
| Tahun | 2025 |
| Venue | Journal of Food Measurement and Characterization |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | peach/nectarine |

## Tautan Akses
- PDF: [li2025syl.pdf](../pdf/li2025syl.pdf)
- DOI resmi: https://doi.org/10.1007/s11694-025-03664-1

## Gambaran Umum

Kajian ini bertujuan mendeteksi buah persik (*peach*) dari citra tanah dan citra pesawat nirawak (*unmanned aerial vehicle*, UAV), lalu memperkirakan jumlah buah per pohon. Penulis menyebut tiga masalah: sebagian besar kajian memakai sudut pandang darat, kinerja turun pada buah yang tertutup daun atau saling tumpang tindih, dan keseimbangan antara akurasi dan kecepatan belum terpecahkan. Hasil deteksi kemudian dipakai untuk menaksir hasil panen.

Data dikumpulkan pada 25 sampai 27 Agustus 2024 di satu kebun di Kabupaten Yiyuan, Kota Zibo, Provinsi Shandong, Tiongkok. Perangkatnya Canon m6, iPhone 13, IQOO 3, dan DJI Phantom 4. Terkumpul 2.200 citra, diperluas dengan augmentasi menjadi 9.450 citra dan 53.857 buah berlabel. Pembagian latih, uji, dan validasi 8:1:1 (7.560, 945, 945 citra). Pemberi label tidak disebut. Untuk taksiran hasil, 80 pohon dipilih acak, buahnya dihitung tangan per pohon, dan tiap pohon difoto UAV. Citra dipangkas ke tajuk pohon sasaran. Nilai indeks luas daun (*leaf area index*, LAI) diukur dengan LI-COR LAI-2200C, rata-rata tiga pengukuran per pohon.

Model SYL-YOLOv8n memodifikasi YOLOv8n (detektor satu tahap). Modul PE-C2f menggabungkan konvolusi parsial (PConv, menghitung konvolusi hanya pada sebagian kanal) dan perhatian EMA (*efficient multi-scale attention*). Fungsi kerugian kotak diganti MPDIoU, yaitu IoU yang menambahkan jarak titik sudut kotak prediksi dan kotak acuan. BiFPN adalah piramida fitur dua arah dengan bobot belajar. Lapisan deteksi P2 (peta fitur 160 × 160) ditambahkan untuk objek kecil. Taksiran hasil memakai regresi linear dari jumlah buah terlihat di tajuk dan LAI ke jumlah buah seluruh pohon.

Pada data uji, SYL-YOLOv8n mencapai presisi 92,7%, *recall* 85,0%, mAP 94,3%, dan F1 88,7%. Nilai itu 1,4, 1,9, 0,7, dan 1,7 poin persentase di atas YOLOv8n asli. Ukuran model 5,1 MB. Pada 80 pohon, regresi tanpa LAI dari YOLOv8n asli memberi R² 0,73 dan RMSE 16,94. Dengan SYL-YOLOv8n dan LAI, R² menjadi 0,88 dengan RMSE 11,16 pada gambar 15, sedangkan simpulan menyebut RMSE 14,17 dan teks lain menyebut 11,71.

Keterbatasan yang dapat diperiksa: pembagian latih, uji, dan validasi dilakukan pada citra setelah augmentasi dan tidak disebut per pohon, sehingga kebocoran antarcitra belum dapat disingkirkan. Taksiran hasil memakai satu citra tajuk per pohon dari atas, jadi buah di bagian bawah tajuk tidak terlihat dan dikoreksi lewat LAI. Pembagian pemodelan dan validasi 3:1 hanya pada 80 pohon dari satu kebun. Angka RMSE di dalam naskah tidak konsisten.
