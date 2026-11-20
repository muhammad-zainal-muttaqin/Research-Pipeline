# DEVELOPMENT AND PRELIMINARY EVALUATION OF A YOLO-BASED FRUIT COUNTING AND MATURITY EVALUATION MOBILE APPLICATION FOR BLUEBERRIES

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `deng2025development` |
| Judul asli | DEVELOPMENT AND PRELIMINARY EVALUATION OF A YOLO-BASED FRUIT COUNTING AND MATURITY EVALUATION MOBILE APPLICATION FOR BLUEBERRIES |
| Penulis | Deng, Boyang; Lu, Yuzhen; Vander Weide, Josh |
| Tahun | 2025 |
| Venue | Applied Engineering in Agriculture |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | blueberry |

## Tautan Akses
- PDF: [deng2025development.pdf](../pdf/deng2025development.pdf)
- DOI resmi: https://doi.org/10.13031/aea.16247

## Gambaran Umum

Studi Deng dkk. (2025) membangun sistem penghitungan buah blueberry dari video yang berjalan di aplikasi iOS. Sistem ini memakai detektor objek YOLOv8 untuk menemukan setiap buah dan menggolongkannya menjadi "Blue" (matang dan siap panen) atau "Unblue" (belum matang). Pengukuran utama adalah mAP@50, yaitu ketepatan deteksi pada ambang *intersection over union* 50%, serta R² dan RMSE untuk persentase buah "Blue" per citra.

Data dikumpulkan pada dua musim. Pada musim 2022, mAP@50 YOLOv8m untuk seluruh kelas ("All") tercatat 88,8% dengan R² 0,985 dan RMSE 4,1. YOLOv8l mencapai 95,0% dengan R² 0,990 dan RMSE 3,2. Pada musim 2024, YOLOv8m turun menjadi 81,5% (R² 0,911; RMSE 10,1) dan YOLOv8l menjadi 88,7% (R² 0,947; RMSE 9,7). Teks menyebut selisih YOLOv8m antara kedua musim sebesar 7,3 poin mAP@50 dan 0,074 pada R². Penulis menafsirkan penurunan ini sebagai akibat pergeseran domain antarmusim, dan membandingkannya dengan MacEachern (2023) yang melaporkan mAP@50 di bawah 90% serta Li (2023) di bawah 80% pada pengujian dalam musim.

Ada ketidakkonsistenan di dalam naskah yang perlu diperiksa sebelum dikutip. Bagian hasil menyebut data uji sebagai musim 2022, sedangkan kesimpulan menyebut model "trained on 2023 data". Teks juga menyatakan RMSE YOLOv8m turun "6.0%", padahal Tabel 1 memberi 4,1 dan 10,1 untuk model dan kelas yang sama, dan angka 6,0% tidak dapat diturunkan dari tabel tersebut.

Dari sisi desain, studi ini menguji penghitungan buah per citra dan klasifikasi kematangan. Setiap buah dihitung pada citra tunggal. Penulis juga mengusulkan kombinasi detektor cepat (YOLOv8m, sekitar 9 FPS di iPhone 15) dan detektor akurat (YOLOv8l, 0,6 FPS), tetapi kombinasi itu tidak dievaluasi secara eksperimental.

Dengan demikian, studi ini menunjukkan bahwa detektor YOLOv8 dapat mencapai mAP@50 di atas 88% pada pengujian dalam musim yang sama, dengan penurunan yang tercatat ketika diuji pada musim lain. Angka itu berasal dari satu kelompok data dan satu perangkat, sehingga generalisasinya ke kebun lain belum dapat dinilai.
