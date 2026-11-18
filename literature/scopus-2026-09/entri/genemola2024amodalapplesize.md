# AmodalAppleSize_RGB-D dataset: RGB-D images of apple trees annotated with modal and amodal segmentation masks for fruit detection, visibility and size estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `genemola2024amodalapplesize` |
| Judul asli | AmodalAppleSize_RGB-D dataset: RGB-D images of apple trees annotated with modal and amodal segmentation masks for fruit detection, visibility and size estimation |
| Penulis | Gen\'e-Mola, Jordi; Ferrer-Ferrer, Mar; Hemming, Jochen; van Dalfsen, Pieter; de Hoog, Dirk; Sanz-Cortiella, Ricardo; Rosell-Polo, Joan R.; Morros, Josep-Ramon; Vilaplana, Ver\'onica; Ruiz-Hidalgo, Javier; Gregorio, Eduard |
| Tahun | 2024 |
| Venue | Data in Brief |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [genemola2024amodalapplesize.pdf](../pdf/genemola2024amodalapplesize.pdf)
- DOI resmi: https://doi.org/10.1016/j.dib.2023.110000

## Gambaran Umum

Artikel data ini menyajikan kumpulan citra RGB-D pohon apel untuk melatih dan menguji metode deteksi serta pengukuran ukuran buah berbasis visi komputer. Masalah yang mendasarinya adalah pengukuran diameter apel dengan jangka sorong memiliki keterbatasan ketelitian dan efisiensi, sedangkan metode berbasis citra yang ada menggunakan segmentasi instans modal hanya pada bagian buah yang terlihat sehingga kesulitan menangani buah yang sebagian tertutup. Penulis menyatakan bahwa dataset publik untuk deteksi dan pengukuran apel di pohon belum ada yang menyertakan mask amodal, yaitu mask yang mencakup bagian buah yang terlihat maupun yang tertutup. Kesenjangan ini menghambat pengembangan metode pengukuran ukuran buah dan estimasi visibilitas yang tangguh terhadap oklusi.

Dataset terdiri dari dua himpunan. Himpunan Fuji memuat 3.925 citra RGB-D dengan total 15.335 buah apel; setiap buah diberi mask segmentasi modal dan amodal serta nilai diameter hasil pengukuran lapangan memakai jangka sorong. Citra diambil di kebun Fuji di Agramunt, Catalonia, Spanyol, pada dua tanggal, yaitu 3 Oktober 2018 (tahap pertumbuhan BBCH85) dan 16 Juli 2020 (BBCH77), dengan kamera Canon EOS 60D. Himpunan Elstar memuat 2.731 citra RGB-D dari lima pohon pada empat tahap pertumbuhan (BBCH75, BBCH77, BBCH79, dan BBCH85) di Randwijk, Belanda, dengan kamera Nikon Z6; himpunan ini menyediakan diameter rata-rata apel per pohon pada setiap tahap sebagai bahan evaluasi. Citra anotasi berukuran 1300 × 1300 piksel dan dapat diunduh melalui DOI 10.34810/data916.

Peta kedalaman dibangkitkan dengan Structure-from-Motion dan Multi-View-Stereo memakai Agisoft Metashape dari citra yang memiliki tumpang tindih lebih dari 75%, sehingga dihasilkan parameter kamera, peta kedalaman, dan awan titik tiga dimensi. Mask modal dibuat secara semi-otomatis dengan Mask R-CNN yang telah dilatih pada dataset Fuji-SfM, lalu dikoreksi manual memakai perangkat lunak VIA. Mask amodal dibentuk dengan mencocokkan bola berdiameter sama dengan diameter apel terukur pada awan titik memakai CloudCompare, lalu memproyeksikannya ke bidang citra mengikuti model kamera pinhole; karena bola dipandang sebagai representasi buah yang lengkap, proyeksinya menghasilkan mask amodal. Citra diberi padding 100 piksel untuk mengakomodasi mask yang melampaui tepi citra. Himpunan Fuji dibagi menjadi 2.304 citra latih dari sisi barat barisan pohon, 814 citra validasi dan 807 citra uji dari sisi timur, dengan tujuan menghindari tumpang tindih antarhimpunan.

Karena artikel ini merupakan artikel data, metrik kinerja deteksi tidak dinyatakan di dalamnya; penulis mengarahkan pembaca ke makalah riset terkait untuk hasil estimasi ukuran berbasis segmentasi amodal. Angka yang tersedia bersifat deskriptif, meliputi 3.925 citra Fuji dengan 15.335 apel, 615 apel Fuji yang diukur manual, 2.731 citra Elstar, dan 10 kelompok buah terukur per pohon Elstar. Distribusi diameter apel Fuji memiliki dua puncak pada rentang [50:55) mm dan [80:85) mm, yang sesuai dengan diameter rata-rata pada tahap BBCH77 dan BBCH85. Nilai diameter rata-rata apel Elstar tercantum pada Tabel 1, misalnya 36,05 mm pada pohon 27 tanggal 21 Juni 2019 dan 75,49 mm pada pohon 78 tanggal 23 Agustus 2019; nilai untuk tahap BBCH75 dan BBCH85 diperoleh dengan interpolasi karena tanggal pengukurannya tidak bertepatan dengan akuisisi citra.

Penulis menyatakan tidak ada keterbatasan pada bagian Limitations naskah. Penulis hanya menjelaskan bahwa nilai diameter rata-rata Elstar untuk dua tahap pertumbuhan diinterpolasi dari tanggal pengukuran terdekat, dan bahwa data dihasilkan dari dua varietas apel serta beberapa tahap pertumbuhan agar dapat dipakai untuk studi perbandingan. Penulis juga menyebut penggunaan ChatGPT-3.5 untuk meningkatkan keterbacaan bahasa naskah, dengan penjelasan bahwa isi tetap menjadi tanggung jawab penulis.

