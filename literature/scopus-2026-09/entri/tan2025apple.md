# Apple Diameter Measurement from RGB Images Using ORCNN and Calibrated Monocular Depth

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `tan2025apple` |
| Judul asli | Apple Diameter Measurement from RGB Images Using ORCNN and Calibrated Monocular Depth |
| Penulis | Tan, Dian Gloria; Gitawardani, Stefani; Hadiprawira, Alexandra; Lucky, Henry |
| Tahun | 2025 |
| Venue | Proceedings 7th International Conference on Informatics Multimedia Cyber and Information System Icimcis 2025 |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [tan2025apple.pdf](../pdf/tan2025apple.pdf)
- DOI resmi: https://doi.org/10.1109/icimcis68501.2025.11327435

## Gambaran Umum

Penulis ingin mengukur diameter apel di pohon dari citra RGB saja, tanpa sensor kedalaman (*depth sensor*). Ukuran buah dipakai untuk estimasi hasil dan penilaian mutu. Mereka menyebut alat ukur manual seperti jangka sorong lambat dan rawan kesalahan operator. Mereka juga menyebut sistem RGB-D yang ada bergantung pada kedalaman acuan dan ukuran beranotasi yang sulit diperoleh dalam skala kebun.

Data adalah set data PApple RGB-D-Size v1: 4.017 citra RGB dengan peta kedalaman, masker modal (bagian terlihat) dan amodal (bentuk utuh termasuk bagian tertutup), serta diameter acuan yang diukur dengan jangka sorong. Citra diambil dengan Canon EOS 60D di kebun dengan variasi cahaya, oklusi, dan sudut pandang. Citra diubah ke 1.300×1.300 dengan panjang fokus efektif sekitar 2.180 piksel. Pembagian data 60:20:20 untuk latih, validasi, dan uji. Pembagian per pohon tidak disebut.

Metode memakai ORCNN, yaitu Mask R-CNN dengan cabang segmentasi amodal dan cabang regresi diameter, berpunggung ResNet-101 dengan FPN (*Feature Pyramid Network*). Diameter piksel dihitung dari luas masker amodal dengan anggapan siluet lingkaran. Depth Anything V2 memprediksi kedalaman dari satu citra. Kedalaman rerata dalam masker modal diubah ke skala metrik dengan regresi linear, lalu diameter milimeter dihitung dengan proyeksi lubang jarum (*pinhole*). Kalibrasi dilakukan secara global atau per citra.

Pada Depth Anything V2, Abs Rel 0,09 dan δ<1,25 sebesar 0,91, dibanding ZoeDepth-NK yang dilatih ulang: 0,26 dan 0,59. Pada ukuran apel, MAE 4,02 mm dengan kedalaman acuan. Dengan kedalaman prediksi, MAE 10,99 mm tanpa kalibrasi, 9,09 mm dengan kalibrasi global, dan 7,72 mm dengan kalibrasi per citra (R² 0,45). Presisi 0,91, recall 0,79, F1 0,83, AP 0,35, pada subset uji.

Keterbatasan dari teks: kalibrasi per citra memerlukan diameter acuan, sehingga tidak dapat dipakai di lapangan. Penulis sendiri menyebut kalibrasi global lebih realistis (MAE 9,09 mm). R² rendah dan RMSE 93,56. Bias rerata negatif pada semua varian. Variasi panjang fokus, cahaya latar kuat, dan oklusi berat tidak dievaluasi. Buah tidak dicacah dan hasil panen tidak diestimasi dengan angka. Hanya satu set data dan satu kamera.
