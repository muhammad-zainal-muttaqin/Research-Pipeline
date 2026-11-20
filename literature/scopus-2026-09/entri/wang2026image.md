# Image-Based, 3D reconstruction for smart farming Applications: A review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2026image` |
| Judul asli | Image-Based, 3D reconstruction for smart farming Applications: A review |
| Penulis | Wang, Haihua; Zhao, Jiayin; Zhang, Shulong; Yao, Mingyuan; Xue, Lin; Li, Daoliang |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [wang2026image.pdf](../pdf/wang2026image.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.111828

## Gambaran Umum

Tinjauan ini membahas rekonstruksi 3D berbasis citra untuk *smart farming*. Teknologi ini dinilai penting untuk persepsi lingkungan pertanian, operasi presisi, dan dukungan pengambilan keputusan. Penulis menyatakan bahwa rekonstruksi 3D berbasis citra menawarkan biaya rendah, portabilitas tinggi, dan fleksibilitas fusi data. Masalahnya, sebagian besar tinjauan terdahulu hanya membahas satu subbidang, misalnya fenotipe tanaman atau peternakan, atau hanya berfokus pada metode geometris konvensional. Karena itu, penulis ingin menyajikan gambaran terstruktur yang mencakup sistem tanaman, sistem ternak, dan persepsi robot sekaligus. Tinjauan ini juga memasukkan metode berbasis pembelajaran mendalam, *Neural Radiance Fields* (NeRF), dan *3D Gaussian Splatting* (3DGS).

Isi pokok tinjauan dimulai dari akuisisi citra. Metode akuisisi dibagi menjadi monokular, stereo, dan multi-view. Monokular murah tetapi mengalami ambiguitas skala. Stereo cocok untuk jarak pendek dalam kondisi terkendali. Multi-view memberikan batasan geometris yang lebih kaya, tetapi membutuhkan cakupan sudut pandang dan biaya komputasi yang lebih besar. Sensor RGB-D diperlakukan sebagai strategi berbantuan kedalaman, terpisah dari akuisisi pasif murni. Metode geometris tradisional yang dibahas meliputi *voxel carving*, *Structure from Motion* digabung *Multi-View Stereo* (SfM-MVS), dan *photometric stereo*. Metode pembelajaran mendalam, NeRF, dan 3DGS dibahas setelahnya. Tabel perbandingan menguraikan kekuatan, keterbatasan, masukan, dan area aplikasi tiap metode. Metode geometris umumnya mudah diinterpretasi dalam kondisi citra yang terkendali. Metode pembelajaran mendalam lebih fleksibel untuk struktur kompleks dan observasi yang tidak lengkap. NeRF dan 3DGS meningkatkan fidelitas rekonstruksi, tetapi menuntut komputasi yang lebih berat. Aplikasi dikelompokkan ke dalam fenotipe tanaman, persepsi dan operasi robot, serta pemantauan ternak. Di kebun dan ladang terbuka, penulis menyebut tantangan berupa variasi cahaya, oklusi, dan gerakan akibat angin.

Penulis menyatakan beberapa batasan utama. Kinerja *real-time*, ketahanan terhadap gangguan, dan integrasi sistem masih menjadi kendala. Metode berbasis NeRF dan 3DGS juga masih perlu peningkatan untuk gerakan, oklusi, dan deformasi biologis. Sensor RGB-D memiliki jangkauan terbatas dan rentan terhadap cahaya luar ruangan serta derau lingkungan. Penulis menguraikan arah penelitian lanjutan berupa model yang ringan, fusi data multimodal, dan penerapan pada perangkat tepi (*edge deployment*). Penulis juga menilai bahwa sistem pertanian pintar ke depan akan semakin mengandalkan pipeline adaptif yang menyeimbangkan akurasi, efisiensi komputasi, dan ketahanan adegan.
