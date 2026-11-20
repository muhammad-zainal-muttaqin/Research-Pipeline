# Yield estimation in precision viticulture by combining deep segmentation and depth-based clustering

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `devanna2025yield` |
| Judul asli | Yield estimation in precision viticulture by combining deep segmentation and depth-based clustering |
| Penulis | Devanna, Rosa Pia; Romeo, Laura; Reina, Giulio; Milella, Annalisa |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | grape |

## Tautan Akses
- PDF: [devanna2025yield.pdf](../pdf/devanna2025yield.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2025.110025

## Gambaran Umum

Kajian ini membahas cara menghitung kelompok tandan (klaster) anggur dari citra yang diambil kamera pada robot yang bergerak di kebun. Penulis juga memperkirakan berat hasil dari volume tiap klaster yang direkonstruksi dalam tiga dimensi. Hasil utamanya: rata-rata galat penghitungan sekitar 12% terhadap ground truth visual, dan rata-rata galat kurang dari 30% terhadap pengukuran berat manual.

Data dan metode. Pengujian dilakukan pada satu varietas anggur dan pada satu tahap pertumbuhan, yaitu anggur matang. Jumlah tanaman uji disebut terbatas. Metode terdiri dari beberapa tahap. Pertama, segmentasi semantik dengan arsitektur *MANet* dan *backbone* *EfficientNetB3* memisahkan buah dari latar. Kedua, klaster dipisahkan dengan pengelompokan berbasis *gradien kedalaman*, yaitu perubahan jarak dari kamera yang menandai batas antar-tandan. Ketiga, tiap klaster direkonstruksi dalam 3D dengan *alpha-shape* dan bidang refleksi untuk memperoleh volume, yang kemudian diubah menjadi estimasi berat. Kamera yang dipakai adalah kamera RGB-D konsumen. Frame diambil setiap satu detik agar tiap frame bertumpang tindih secara minimal dan penghitungan ganda dikurangi. Penghitungan dilakukan per tanaman.

Hasil. Rata-rata penghitungan klaster meleset 1,5 klaster atau 12,2% terhadap ground truth visual. Terhadap ground truth lapangan, yaitu pengukuran berat manual, galatnya 6,7 dan 33,9%. Penulis menyimpulkan bahwa metode ini cukup akurat untuk penghitungan klaster pada anggur matang, dengan catatan bahwa galat terhadap berat manual jauh lebih besar daripada galat terhadap penghitungan visual.

Batasan. Penulis sendiri menyatakan bahwa teknik diuji pada satu tahap pertumbuhan, yaitu anggur matang, dan pada satu varietas. Jumlah tanaman uji juga terbatas. Dari sisi analisis, ringkasan ini mencatat bahwa metode bergantung pada kualitas kedalaman dari kamera konsumen, dan bahwa klaster yang tertutup daun atau saling menutupi belum tercatat sebagai kasus yang diuji secara terpisah. Karena objeknya anggur, hasil kajian ini tidak langsung berlaku untuk tandan kelapa sawit.
