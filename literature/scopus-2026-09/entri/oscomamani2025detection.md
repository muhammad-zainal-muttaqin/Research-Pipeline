# The Detection and Counting of Olive Tree Fruits Using Deep Learning Models in Tacna, Perú

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `oscomamani2025detection` |
| Judul asli | The Detection and Counting of Olive Tree Fruits Using Deep Learning Models in Tacna, Perú |
| Penulis | Osco-Mamani, Erbert; Santana-Carbajal, Oliver; Chaparro-Cruz, Israel; Ochoa-Donoso, Daniel; Alcazar-Alay, Sylvia |
| Tahun | 2025 |
| Venue | AI Switzerland |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | olive |

## Tautan Akses
- PDF: [oscomamani2025detection.pdf](../pdf/oscomamani2025detection.pdf)
- DOI resmi: https://doi.org/10.3390/ai6020025

## Gambaran Umum

Kajian ini bertujuan menilai kinerja model deteksi untuk menghitung buah zaitun pada kebun alami di Tacna, Peru, guna mendukung perkiraan hasil panen. Tacna menyumbang 95 persen produksi zaitun nasional dengan hasil rata-rata 6,4 t/ha dan varietas utama Sevillana. Produksi antara tahun 2022 dan 2023 turun 27 persen akibat El Niño–Southern Oscillation, sehingga perkiraan hasil otomatis diperlukan untuk memilih strategi produksi, menekan biaya tenaga kerja, dan meningkatkan ketepatan ramalan.

Tanaman yang dipelajari adalah zaitun varietas Sevillana di La Yarada Los Palos, Tacna (18°15′16,1″ S, 70°26′30,7″ W). Citra diambil dengan kamera Canon EOS Rebel T6i 24,2 MP pada jarak sekitar 5 m dari batang pohon, bukaan f/4,5, pukul 10.00–17.00, delapan foto per pohon pada langkah 45 derajat. Dari 100 pohon diperoleh 815 citra CR2; 503 citra dipilih lalu dipotong menjadi 24 wilayah setiap citra sehingga terbentuk 19.560 citra berukuran 1000×1000 piksel. Sebanyak 12.072 citra dipilih untuk pelabelan dan 10.728 citra diberi kotak pembatas melalui lima iterasi yang melibatkan pakar dan tim peneliti. Pembagian data adalah 8.549 citra (70,82 persen) untuk latih, 2.179 (18,05 persen) untuk validasi, dan 1.344 (11,13 persen) untuk uji. Enam model dibandingkan, yaitu YOLOv8m, YOLOv8s, Faster R-CNN 101, Faster R-CNN 50, RetinaNet 101, dan RetinaNet 50. Setiap model dilatih sepuluh kali selama 100 epoch dengan ukuran batch 4, laju pembelajaran 0,001, dan bobot awal COCO pada GPU NVIDIA A5000 24 GB.

Mekanisme penghitungan menjumlahkan semua buah yang diprediksi model pada potongan citra, mengelompokkan kembali hasilnya per citra utuh, lalu menggabungkan delapan citra per pohon untuk memperoleh jumlah buah per pohon. Penghitungan memakai ambang keyakinan 0,5; inferensi terpotong (SAHI) juga diterapkan pada citra pohon utuh. Metrik deteksi terdiri atas IoU, mAP, mAP50 pada ambang IoU 0,50, serta mAP50-95 yang dirata-ratakan atas sepuluh ambang IoU 0,50–0,95 dengan langkah 0,05. Akurasi penghitungan dinilai dengan RMSE dan koefisien determinasi R² terhadap jumlah label manual per pohon.

YOLOv8m memberi kinerja tertinggi. Pada himpunan validasi, mAP50 mencapai 0,9496 (94,960) pada epoch 77 dan mAP50-95 mencapai 0,77533 (77,533) pada epoch 80; YOLOv8s mencapai 0,94685 dan 0,7707. Pada himpunan uji, YOLOv8m mencatat mAP50 maksimum 0,98273 (rerata 0,98142) dan mAP50-95 maksimum 0,96060 (rerata 0,95365). Untuk penghitungan pada 447 citra yang dikelompokkan menjadi 55 kelompok delapan citra per pohon, YOLOv8m menghasilkan RMSE 402,46 dan R² 0,94, lebih baik daripada YOLOv8s (RMSE 452,98; R² 0,93) dan keempat model lainnya. Uji ANOVA menunjukkan perbedaan kinerja antarmodel signifikan (p < 0,05). YOLOv8s memiliki waktu inferensi rata-rata tercepat, 7,183 ms.

Penulis menyebut sejumlah faktor yang memengaruhi hasil, yaitu posisi kamera, jarak pengambilan, pencahayaan, bayangan, jenis perangkat, dan variabel tak terkontrol lain. Kesulitan utama berupa buah yang saling menumpang, kondisi pencahayaan, kemiripan antara zaitun hijau dan daun, serta buah di tepi citra. Penulis menyarankan pengujian arsitektur ringan seperti YOLOv8n dan penerapan model pada perangkat tepi sebagai kerja lanjutan.

