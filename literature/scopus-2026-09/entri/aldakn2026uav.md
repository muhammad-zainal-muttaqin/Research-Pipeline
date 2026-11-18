# UAV-Based Computer Vision Approach for Melon Fruit Detection and Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `aldakn2026uav` |
| Judul asli | UAV-Based Computer Vision Approach for Melon Fruit Detection and Yield Estimation |
| Penulis | Aldakn, Hassan; Dragonetti, Giovanna; Khadra, Roula; Abdelmoneim, Ahmed Ali Ayoub; Derardja, Bilal |
| Tahun | 2026 |
| Venue | Agriengineering |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | melon |

## Tautan Akses
- PDF: [aldakn2026uav.pdf](../pdf/aldakn2026uav.pdf)
- DOI resmi: https://doi.org/10.3390/agriengineering8020053

## Gambaran Umum

Penelitian ini bertujuan membangun alur kerja berbasis citra UAV untuk mendeteksi buah melon dan mengestimasi hasil panen. Cara konvensional mengandalkan pengalaman petani dan sampel destruktif yang mahal serta tidak cocok untuk skala luas. Penulis mencatat bahwa melon masih jarang diteliti dan data untuk estimasi hasil masih sedikit. Alur kerja yang diusulkan menggabungkan deteksi buah dengan regresi berbasis volume untuk menaksir berat buah dan total hasil.

Tanaman yang diamati adalah melon kuning (*Cucumis melo* L.). Eksperimen berlangsung pada musim tanam Mei–Agustus 2025 di lahan percobaan Mediterranean Agronomic Institute of Bari di Apulia, Italia selatan (41°03'16" LU, 16°52'32" BT, ketinggian 77 m), dengan luas 1.408 m² (0,14 ha). UAV DJI Mavic 3M membawa kamera RGB 20 megapiksel dan kamera multispektral 5 megapiksel, dilengkapi GNSS, modul RTK, dan sensor cahaya matahari. Penerbangan dilakukan mendekati tengah hari dengan interval dua minggu; enam penerbangan menjelang panen dipakai dalam kajian. Tumpang tindih citra diatur 80% lateral dan 80% depan, ketinggian 65 m dan 21 m menghasilkan GSD masing-masing 3 cm dan 1 cm, kecepatan 0,9 m/s, dan lama penerbangan sekitar 4 dan 13 menit.

Citra diolah dengan Pix4D 4,5,6 menjadi ortomosaik tergereferensi. Sebanyak 79 melon dipilih secara acak dan ditandai di lapang dengan papan penanda tegak; ukuran dan massanya diukur sebagai kebenaran. Ortomosaik dipotong menjadi 95 subcitra. Penulisan label memakai GSD 1 cm; citra 3 cm dikeluarkan karena buah sulit dibedakan. Penandaan memakai Roboflow dengan satu kelas buah tanpa pembedaan tahap kematangan, lalu diekspor ke format YOLOv12. Data dibagi menjadi 67 citra latih (70%), 19 citra validasi (20%), dan 9 citra uji (10%). Model YOLOv12 dilatih 100 epoch pada sasaran 1280 piksel dengan ambang kepercayaan 0,25 dan NMS IoU 0,50, memakai Python 3.12 dan GPU NVIDIA T4 16 GB di Google Colab.

Deteksi menghasilkan kotak pembatas, lalu setiap kotak diproses menjadi ROI, diubah ke skala abu-abu, dinormalisasi ke [0, 1], dan disegmen dengan model kontur aktif Chan–Vese (µ = 0,25, λ1 = 1, λ2 = 1, toleransi 10⁻³, maksimum 200 iterasi). Kontur terbesar diambil; jika memiliki sekurang-kurangnya lima titik, elips terbaik dihitung dan sumbu-sumbunya dikonversi ke sentimeter memakai GSD 1 cm/px. Volume dihitung dengan pendekatan elipsoid dari sumbu A, B, dan C. Jika suatu citra memiliki sekurang-kurangnya lima kegagalan dan satu keberhasilan, sumbu rata-rata citra dipakai untuk mengisi deteksi yang gagal dengan sudut 0°. Nilai presisi dan recall stabil di atas 0,85 setelah 20 epoch, mAP50 melebihi 0,9, dan mAP50–95 sekitar 0,7 setelah 100 epoch. Perbandingan dengan hitungan manual pada tiga panen memberi selisih 7% (521 berbanding 560), 4% (1673 berbanding 1735), dan 3% (114 berbanding 117); secara keseluruhan R² = 0,99, RMSE 5,68, dan MAPE 5%. Pada tahap berat, regresi volume terukur terhadap berat memberi R² = 0,89; volume hasil citra terhadap volume ukuran lapang memberi R² = 0,86; dan berat taksiran terhadap berat aktual memberi R² = 0,79 dengan RMSE 0,26 kg, MAE 0,19 kg, dan MAPE 9,77%. Abstrak dan simpulan menyebut galat hasil panen total 2,9%; bagian pembahasan juga mencantumkan angka 2,9% untuk kajian pembanding yang memakai GSD 0,4 cm dengan R² tersesuaikan 0,87.

Penulis menyatakan beberapa batasan. Buah melon nyata sering menyimpang dari elipsoid ideal karena keragaman biologis, ketidakteraturan permukaan, serta deformasi akibat kontak dengan tanah atau tumpukan buah; penyimpangan ini menimbulkan bias sistematis pada volume dan merambat ke taksiran berat. Citra 3 cm menurunkan kejernihan batas buah sehingga buah menyatu dengan vegetasi dan pelabelan gagal. Kumpulan data hanya memuat satu kelas tanpa anotasi kematangan. Data tidak tersedia untuk umum karena pembatasan institusi. Penulis menganjurkan perluasan data ke lebih banyak kultivar dan struktur tajuk, rekonstruksi tiga dimensi seperti LiDAR untuk volume pada kondisi tumpang tindih atau tertutup, serta penggabungan deteksi RGB dengan pencitraan multispektral atau termal.

