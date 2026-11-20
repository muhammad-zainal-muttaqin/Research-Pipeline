# StrongSORT: Make DeepSORT Great Again

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `du2023strongsort` |
| Judul asli | StrongSORT: Make DeepSORT Great Again |
| Penulis | Du, Yunhao; Zhao, Zhicheng; Song, Yang; Zhao, Yanyun; Su, Fei; Gong, Tao; Meng, Hongying |
| Tahun | 2023 |
| Venue | IEEE Transactions on Multimedia |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [du2023strongsort.pdf](../pdf/du2023strongsort.pdf)
- DOI resmi: https://doi.org/10.1109/tmm.2023.3240881

## Gambaran Umum

Penelitian ini mengatasi kesulitan membandingkan metode pelacakan banyak objek secara adil. Penulis menilai bahwa penelitian terkini memakai detektor, model penyematan, data latih, dan trik inferensi yang berbeda, sehingga perbandingan progres menjadi tidak seimbang. Tujuan utamanya adalah menghidupkan kembali pelacak klasik DeepSORT sebagai tolok ukur yang kuat dan adil. Penulis berpendapat bahwa kinerja DeepSORT yang rendah bukan berasal dari kerangka pelacakannya, melainkan dari teknik yang sudah usang. Oleh karena itu, DeepSORT diperkaya dengan komponen mutakhir pada sisi deteksi, penyematan penampilan, dan asosiasi tanpa mengganti paradigma dasarnya.

Objek yang dilacak bukan tanaman, melainkan pedestrian, mobil, dan kepala manusia. Percobaan memakai MOT17 (tujuh urutan latih dengan 5.316 bingkai dan tujuh urutan uji dengan 5.919 bingkai), MOT20 (empat urutan latih dengan 8.931 bingkai dan empat urutan uji dengan 4.479 bingkai pada adegan sangat padat), KITTI (21 urutan latih dan 29 urutan uji pada laju 10 bingkai per detik), serta DanceTrack (100 video tari dengan penampilan manusia yang mirip dan gerak beragam). Detektor yang dipakai adalah YOLOX-X terlatih pada COCO, dengan ambang keyakinan deteksi 0,6 dan ambang NMS 0,8. Penyariat penampilan memakai model BoT dan dilatih awal pada DukeMTMC, sedangkan detektor dilatih pada CrowdHuman dan bagian setengah data latih MOT17. Metrik yang dipakai adalah MOTA, IDF1, HOTA, AssA, DetA, jumlah peralihan identitas (IDs), dan kecepatan bingkai per detik.

Mekanisme utama dibangun bertahap dari DeepSORT menjadi StrongSORT. Empat perbaikan inti adalah penggantian penyariat penampilan dengan BoT, kompensasi gerak kamera memakai ECC, filter Kalman NSA yang menyesuaikan derau ukuran dengan skor keyakinan deteksi, dan pembaruan ciri memakai EMA. Pada tahap asosiasi, biaya pencocokan merupakan jumlah berbobot biaya penampilan dan biaya gerak dengan faktor 0,98, dan algoritma matching cascade diganti dengan penugasan linear global biasa. Penulis menyatakan cascading justru membatasi pelacak yang sudah kuat. StrongSORT++ menambahkan dua modul ringan yang dapat dipasang pada pelacak lain. AFLink menyambung tracklet yang terputus tanpa informasi penampilan, memakai dua cabang konvolusi temporal dan fusi atas 30 bingkai terakhir serta MLP untuk memprediksi skor konektivitas. GSI mengganti interpolasi linier dengan regresi proses Gaussian berbasis kernel radial, dengan kehalusan yang menyesuaikan panjang lintasan, untuk mengisi deteksi yang hilang sekaligus meredam derau lokalisasi.

Hasil ablation pada himpunan validasi MOT17 (Tabel I) menunjukkan kontribusi masing-masing komponen. DeepSORT dasar mencatat IDF1 77,3, MOTA 76,7, dan HOTA 66,3; setelah keenam perbaikan, StrongSORTv6 mencatat IDF1 82,3, MOTA 77,1, dan HOTA 69,6, dengan kecepatan turun dari 13,8 menjadi 7,5 bingkai per detik. Pada himpunan uji MOT17 (Tabel IV), StrongSORT mencatat HOTA 63,5, IDF1 78,5, MOTA 78,3, AssA 63,7, DetA 63,6, dan 1.446 peralihan identitas. Setelah kedua modul tambahan diterapkan, StrongSORT++ mencatat HOTA 64,4, IDF1 79,5, MOTA 79,6, AssA 64,4, DetA 64,6, dan 1.194 peralihan identitas pada kecepatan 7,1 bingkai per detik. Sebagai acuan, ByteTrack pada tabel yang sama mencatat HOTA 63,1, IDF1 77,3, dan MOTA 80,3. Penulis menyatakan StrongSORT++ menduduki peringkat pertama pada HOTA, IDF1, AssA, dan DetA di MOT17 maupun MOT20, serta mencapai hasil terbaik pada DanceTrack dan KITTI.

Batasan yang dinyatakan penulis mencakup beberapa hal. Perbandingan kecepatan sulit dilakukan secara adil karena kecepatan tiap metode bergantung pada perangkat dan waktu deteksi umumnya tidak dihitung dalam pelacakan berbasis deteksi. StrongSORT++ memakai satu tumpuan parameter yang sama dengan ablasi dan tidak disetel khusus tiap urutan. GSI lebih cocok untuk pelacak yang kuat; pada pelacak yang lemah, modul ini justru terbingung oleh banyaknya asosiasi salah.AFLink dan GSI menambah biaya masing-masing 1,7 milidetik dan 7,1 milidetik per citra pada MOT17, sehingga peningkatan akurasi mengorbankan kecepatan keseluruhan. Penulis juga tidak mengklaim keunggulan MOTA mutlak karena ByteTrack tetap mencatat MOTA lebih tinggi pada MOT17.
