# AI-driven 3D point cloud analysis in plant phenotyping: A Systematic Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chang2026ai` |
| Judul asli | AI-driven 3D point cloud analysis in plant phenotyping: A Systematic Review |
| Penulis | Chang, Jianye; Walsh, Jason John; Mangina, Eleni; Ruan, Jue; Negr\~ao, S\'onia |
| Tahun | 2026 |
| Venue | Smart Agricultural Technology |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [chang2026ai.pdf](../pdf/chang2026ai.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2026.101869

## Gambaran Umum

Kajian ini memetakan penggunaan *kecerdasan buatan* (*artificial intelligence*, AI) pada *awan titik tiga dimensi* (*3D point cloud*, 3DPC), yaitu kumpulan titik koordinat yang merekam bentuk permukaan objek, untuk mengukur fenotipe tanaman. Fenotipe tanaman adalah sifat yang dapat diukur dari tanaman, seperti struktur daun, ukuran batang, dan tinggi tanaman. Penulis berpendapat bahwa citra dua dimensi belum cukup untuk menangkap detail geometri tersebut. Menurut penulis, tinjauan sebelumnya hanya membahas satu metode akuisisi atau satu aplikasi. Karena itu, kajian ini menyatukan metode akuisisi, kelompok tanaman, algoritma, dan dataset dalam satu tinjauan kuantitatif.

Cakupannya adalah 381 makalah yang terbit antara Januari 2017 dan Oktober 2025. Sebanyak 342 makalah (89,8%) berupa artikel jurnal dan 39 makalah (10,2%) berupa prosiding konferensi. Jumlah makalah per tahun naik dari 3 (2017) dan 9 (2018) menjadi 17 (2019), 21 (2020), 26 (2021), 41 (2022), 72 (2023), 88 (2024), dan 104 (2025 hingga Oktober). Lebih dari separuh makalah terbit sejak 2022.

Pada algoritma, 256 studi (66,7%) menerapkan algoritma langsung pada 3DPC. Masukan yang dipakai berupa titik mentah, voksel, atau beberapa pandangan. Pada 2017 hingga 2020 pembelajaran mesin tradisional dominan, dengan porsi di atas 80% pada 2019. Sejak 2021 pembelajaran mendalam (*deep learning*) dominan. Arsitektur yang muncul meliputi jaringan berbasis MLP per titik seperti PointNet dan PointNet++, model *Transformer*, model berbasis graf, dan model hibrida. *Neural Radiance Fields* (NeRF) dan *3D Gaussian Splatting* (3DGS) dipakai untuk rekonstruksi 3D dan sintesis adegan. Di lingkungan terkontrol, pembelajaran mendalam lebih sering dipakai. Di lapangan, pembelajaran mesin tradisional masih kuat.

Teknologi akuisisi yang paling sering dipakai adalah *Time-of-Flight* (ToF) dengan 163 studi dan *Structure from Motion and Multi-View Stereo* (SfM-MVS) dengan 117 studi. Lima metode lain tercatat lebih sedikit: pembelajaran (36), stereo (34), lainnya (33), triangulasi laser (24), dan cahaya terstruktur (23). ToF tumbuh tajam sekitar 2022 dan menjadi metode dominan pada 2025.

Fokus objek tanaman adalah pohon dan semak (132 studi) serta serealia (112 studi). Kelompok lain adalah Solanaceae (76), Fabaceae (36), dan Brassicaceae (28), sedangkan 73 studi mencakup tanaman lain. Sebanyak 329 studi (86,4%) meneliti satu spesies. Dataset publik dipakai pada 18,9% studi. Tidak ada studi yang memakainya pada 2017 dan 2018, dan proporsinya naik sejak 2020 dengan puncak pada 2025. Tabel 1 dalam kajian memuat dataset publik yang disebut, yaitu ModelNet, ShapeNet, ROSE-X, Pheno4D, dan Soybean-MVS.

Penulis menyebut empat keterbatasan utama. Pertama, belum ada standar pengumpulan data dan format. Kedua, ketahanan dan generalisasi model dari laboratorium ke lapangan masih rendah. Ketiga, kebutuhan komputasi tinggi. Keempat, model masih bergantung pada spesies tertentu. Penulis menyebut empat prioritas berikutnya: model yang efisien dan dapat dipakai di lapangan, pemanfaatan model fondasi, dataset publik yang beragam dan terstandar, serta integrasi fenomika 3D dengan genomika.
