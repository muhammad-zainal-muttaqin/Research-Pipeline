# Volumetric 3D Reconstruction and parametric shape modeling from RGB-D Sequences

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `nakaguro2015volumetric` |
| Judul asli | Volumetric 3D Reconstruction and parametric shape modeling from RGB-D Sequences |
| Penulis | Nakaguro, Yoichi; Qureshi, Waqar S.; Dailey, Matthew N.; Ekpanyapong, Mongkol; Bunnun, Pished; Tungpimolrut, Kanokvate |
| Tahun | 2015 |
| Venue | Lecture Notes in Computer Science |
| Kode | C5 (Depth, 3D, dan non-RGB) |

## Tautan Akses
- PDF: [nakaguro2015volumetric.pdf](../pdf/nakaguro2015volumetric.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-319-23231-7_45

## Gambaran Umum

Kajian Nakaguro dan kawan-kawan (2015) membangun model volumetrik dari urutan RGB-D kamera Primesense Carmine untuk mengukur bentuk dan volume buah nanas. Buah diukur sebagai elipsoid dengan tiga metode fitting pada dua jenis titik: titik mentah sensor dan titik hasil render model volumetrik. Pengujian dilakukan pada kebun nanas tiruan skala kecil dengan dua buah.

Urutan dasarnya: 400 bingkai RGB-D direkam dengan kamera digerakkan secara manual di atas dua buah. DVO-SLAM memperkirakan lintasan kamera. FastFusion membangun model volumetrik inkremental yang diekspor sebagai mesh bertekstur.

Dari mesh, 100 pasang citra RGB dan depth sintetis dirender pada posisi kamera tiap empat bingkai. Masker buah dari segmentasi dense diterapkan, lalu 100 awan titik sintetis dan 100 awan titik mentah dibandingkan. Tiga metode fitting elipsoid dibandingkan: Direct least squares, MSAC, dan selisih SIFT yang dioptimasi dengan Levenberg-Marquardt.

Ground truth diukur manual. Pada titik mentah, metode MSAC memberi galat volume buah A 3,3% (Tabel 1, kolom MSAC, Raw). Pada titik model, metode Direct untuk buah B gagal konvergen dengan galat volume 7423,3%. Penulis menyatakan bahwa keunggulan titik model terjadi "except for the divergence of the direct method", sehingga klaim keunggulan tidak berlaku untuk seluruh sel tabel. Perbandingan MSAC dan selisih SIFT tidak menunjukkan selisih jelas (teks bagian 3.2).

Penulis mencantumkan lima keterbatasan: skala kecil (4 m × 2 m × 0,5 m, dua buah), jangkauan sensor 0,35 m sampai 1,4 m, resolusi 640 × 480, syarat cahaya difus, dan syarat visibilitas permukaan buah. Dari sisi bukti, jumlah sampel buah sangat kecil, hanya dua buah dengan dua kunci bingkai per buah, dan parameter penalti disetel secara eksperimen. Hasil tidak mengukur penghitungan buah atau identitas lintas pandang.
