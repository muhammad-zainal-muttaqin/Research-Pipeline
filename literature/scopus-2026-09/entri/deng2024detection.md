# Detection, counting, and maturity assessment of blueberries in canopy images using YOLOv8 and YOLOv9

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `deng2024detection` |
| Judul asli | Detection, counting, and maturity assessment of blueberries in canopy images using YOLOv8 and YOLOv9 |
| Penulis | Deng, Boyang; Lu, Yuzhen; Li, Zhaojian |
| Tahun | 2024 |
| Venue | Smart Agricultural Technology |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | blueberry |

## Tautan Akses
- PDF: [deng2024detection.pdf](../pdf/deng2024detection.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2024.100620

## Gambaran Umum

Kajian Deng dkk. (2024) menguji dua detektor objek, YOLOv8l dan YOLOv9-c, untuk mendeteksi buah blueberry pada citra kanopi. Tujuannya adalah menghitung buah per gambar dan menaksir persentase buah matang per gambar. Citra diambil dengan kamera genggam. Detektor dilatih dengan dua kelas: buah matang (ripe) dan buah belum matang (unripe). YOLOv8l dan YOLOv9-c dipakai dengan bobot awal pretrained COCO. YOLOv9-c juga dilatih dari awal sebagai pembanding.

Pada resolusi masukan 2560 px, YOLOv8l dan YOLOv9-c mencapai mAP@50 masing-masing sekitar 91,0% dan 91,7%. YOLOv9-c unggul 0,9% dari YOLOv8l, tetapi selisih itu tidak signifikan menurut paired t-test. Pada resolusi 3520 px, YOLOv8l mencapai mAP@50 92,7% (Tabel 3 memuat 92,1% untuk buah matang dan 93,2% untuk buah belum matang; teks menulis 93,3% untuk belum matang). Evaluasi memakai Monte Carlo cross-validation dengan tiga replikasi dan alfa 0,05.

Penghitungan buah per gambar didasarkan pada jumlah bounding box prediksi, tanpa membedakan kelas. Hasilnya dibandingkan dengan hitungan manual. Regresi penghitungan memberi R² 0,996, RMSE 10,39, dan galat relatif 6,67%. Untuk fraksi buah matang, R² 0,973, RMSE 3,62%, dan galat relatif 9,65%. Abstrak menyebut RMSE penghitungan 10,4 dan galat persentase matang 3,62%, sesuai dengan angka di bagian hasil.

Tidak ada langkah yang menentukan apakah buah yang sama muncul di beberapa pandang. Penulis sendiri menyebut stitching multi-pandang sebagai tantangan terbuka. Pada keterbatasan, mereka mencatat bahwa akuisisi masih handheld dan belum ada stitching multi-pandang yang berhasil. Li dkk. dikutip memakai tiga pandang, tetapi stitching gagal karena overlap antarpandang kurang. Pekerjaan lanjutan menyebut aplikasi smartphone yang sedang dibangun, tetapi belum diuji di lapangan dengan sistem bergerak.

Ada ketidakcocokan jumlah dataset di dalam naskah. Abstrak dan Pendahuluan menyebut 17.955 instance, sedangkan Kesimpulan menulis 17.809.

Dari sisi tinjauan, kajian ini termasuk studi per gambar. Deteksi dan penghitungan dilaporkan per citra, dan tidak ada deduplikasi lintas pandang. Kajian ini relevan sebagai pembanding deteksi blueberry dengan kamera genggam, tetapi tidak menjawab pertanyaan identitas lintas pandang.
