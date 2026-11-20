# MIoP-NMS: Perfecting crops target detection and counting in dense occlusion from high-resolution UAV imagery

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `jiang2023miop` |
| Judul asli | MIoP-NMS: Perfecting crops target detection and counting in dense occlusion from high-resolution UAV imagery |
| Penulis | Jiang, Quan; Huang, Zichen; Xu, Gang; Su, Yingying |
| Tahun | 2023 |
| Venue | Smart Agricultural Technology |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | banana |

## Tautan Akses
- PDF: [jiang2023miop.pdf](../pdf/jiang2023miop.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2023.100226

## Gambaran Umum

Jiang dkk. (2023) melaporkan metode penghitungan pohon pisang dari citra UAV RGB di kebun yang rapat dan saling menutup. Masalah utamanya adalah pohon yang sama tampak pada beberapa potongan citra. Jika setiap potongan dihitung sendiri, satu pohon dapat tercatat lebih dari sekali. Metode ini memotong ortomosaik beresolusi tinggi menjadi potongan berukuran 832 piksel dengan tumpang tindih 20% sampai 50%, lalu mendeteksi pohon di setiap potongan dengan YOLOv4. Deteksi dari potongan yang berdekatan digabung dengan varian non-maximum suppression (NMS) yang diusulkan penulis, yaitu MIoP-NMS, yang memakai rasio maksimum irisan terhadap porsi (*maximum intersection over portion*). Hasil utamanya adalah mAP sekitar 85%, galat penghitungan sekitar 1,3%, dan akurasi turunan sekitar 98,7% pada hutan pisang padat.

Data terdiri atas 552 citra UAV dengan resolusi 4864×3648 piksel yang dipotret pada ketinggian 30 m. Citra dibagi menjadi 442 untuk latih, 38 untuk validasi, dan 72 untuk uji. Ortomosaik area sampel berukuran 4104×14.505 piksel dan memuat dua plot: plot jarang dengan 214 pohon dan plot padat dengan 244 pohon. Ukuran data ini kecil dibanding korpus deteksi objek umum, dan seluruh citra berasal dari satu lokasi dan satu sensor. Kajian ini tidak melaporkan variasi musim, varietas pisang, atau kondisi pencahayaan yang berbeda. Akibatnya, angka akurasi berlaku untuk kebun yang mirip dengan lokasi pengambilan data.

Pelatihan dijalankan pada beberapa jumlah epoch, yaitu 250, 300, 350, dan 400. Untuk plot jarang, Tabel 2 membandingkan keempat varian NMS pada setiap jumlah epoch. Galat penghitungan NMS standar berada pada 9,81% sampai 11,21%, CIoU-NMS pada 14,95% sampai 16,36%, dan soft-NMS pada 22,43% sampai 23,83%. Nilai mAP pada plot jarang berkisar 85% sampai 89% untuk semua varian, sehingga mAP yang tinggi tidak menjamin galat penghitungan yang rendah. Pada plot padat, galat MIoP-NMS dilaporkan sebesar 1,29%, 1,43%, dan 1,31% pada tiga konfigurasi yang diuji di bagian 4. Perbandingan ini berasal dari dua plot dengan kerapatan berbeda, sehingga selisih galat antara plot jarang dan padat tidak dapat dibaca sebagai selisih metode saja.

Mekanisme asosiasi yang dipakai adalah penggabungan kotak deteksi berdasarkan tumpang tindih, bukan identitas tetap antarpandang. Kajian ini tidak memakai beberapa pandang untuk mengidentifikasi pohon yang sama, dan tidak melacak pohon antarwaktu. Batas lain yang perlu dicatat adalah tidak adanya pengukuran penghitungan pada data uji yang benar-benar terpisah dari kebun pelatihan.
