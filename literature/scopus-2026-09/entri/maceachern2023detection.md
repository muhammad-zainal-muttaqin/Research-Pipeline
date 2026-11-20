# Detection of fruit maturity stage and yield estimation in wild blueberry using deep learning convolutional neural networks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `maceachern2023detection` |
| Judul asli | Detection of fruit maturity stage and yield estimation in wild blueberry using deep learning convolutional neural networks |
| Penulis | MacEachern, Craig B.; Esau, Travis J.; Schumann, Arnold W.; Hennessy, Patrick J.; Zaman, Qamar U. |
| Tahun | 2023 |
| Venue | Smart Agricultural Technology |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | blueberry |

## Tautan Akses
- PDF: [maceachern2023detection.pdf](../pdf/maceachern2023detection.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2022.100099

## Gambaran Umum

Kajian ini menguji apakah model deteksi objek YOLO (*You Only Look Once*, arsitektur deteksi satu tahap) dapat mendeteksi buah dan mengklasifikasikan tingkat kematangannya dari foto kuadrat lapangan, lalu memakai jumlah buah tersebut untuk memperkirakan hasil per hektare. Data berasal dari 864 citra yang diambil pada musim 2018 dan 2019 di kuadrat berukuran 0,5 × 0,5 m, dengan 54 titik pengambilan per lapangan. Citra asli dari kamera Canon Rebel T6 (6000 × 4000 piksel) dipotong menjadi 17.280 citra berukuran 1280 × 720 piksel, dan 6.766 citra dipilih untuk pelabelan. Pembagian data menjadi 4.736 citra latih, 1.015 citra validasi, dan 1.015 citra uji.

Model terbaik, YOLOv4 dengan tiga kelas kematangan, mencapai mAP50 (*mean average precision* pada ambang IoU 0,5, yaitu rata-rata presisi di seluruh kelas) sebesar 79,79%. Ketika tiga kelas digabung menjadi dua kelas, mAP50 naik menjadi 88,12%, dengan F1 tertinggi 0,82, recall 0,86, dan precision 0,79. Penulis melaporkan bahwa penggabungan kelas merah dan hijau menaikkan mAP50 sebesar 9,73%. Angka ini menunjukkan bahwa sebagian galat berasal dari pembedaan antarkelas kematangan, bukan dari pendeteksian buah itu sendiri.

Untuk regresi hasil, model YOLOv4-Small menghasilkan galat absolut rata-rata 578,4 kg/ha, atau 24,1%, dengan R² 89,67 pada tabel regresi. Rata-rata waktu inferensi 7,8 ms dan memori rata-rata 1,63 GB. Penulis merekomendasikan YOLOv4-Tiny untuk kecepatan dan kebutuhan memori, serta menyebut rencana pengembangan aplikasi telepon pintar sebagai langkah berikutnya.

Kajian tidak melaporkan penautan buah antarcitra atau kebenaran dasar (*ground truth*) lintas pandang, sehingga tidak dihitung sebagai asosiasi lintas pandang. Keterbatasan yang dinyatakan penulis mencakup variasi klon dan dedaunan yang menutupi buah, serta bias pelabelan manual yang dibahas pada bagian metode. Model dan kuadrat yang sama menjadi dasar seluruh hitungan, sehingga generalisasi ke lapangan lain belum diuji dalam kajian ini.
