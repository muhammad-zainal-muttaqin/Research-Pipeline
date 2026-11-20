# Field-grown tomato yield estimation using point cloud segmentation with 3D shaping and RGB pictures from a field robot and digital single lens reflex cameras

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ambrus2024field` |
| Judul asli | Field-grown tomato yield estimation using point cloud segmentation with 3D shaping and RGB pictures from a field robot and digital single lens reflex cameras |
| Penulis | Ambrus, B.; Teschner, G.; Kov\'acs, A.J.; Nem\'enyi, M.; Helyes, L.; P\'ek, Z.; Tak\'acs, S.; Alahmad, T.; Ny\'eki, A. |
| Tahun | 2024 |
| Venue | Heliyon |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [ambrus2024field.pdf](../pdf/ambrus2024field.pdf)
- DOI resmi: https://doi.org/10.1016/j.heliyon.2024.e37997

## Gambaran Umum

Ambrus dkk. (2024) menguji sistem robot untuk menghitung dan mengukur tomat di kebun, dengan pengambilan gambar dari sisi tanaman dalam barisan. Kajian ini menggabungkan deteksi berbasis citra RGB dengan pemindaian 3D untuk memperkirakan volume dan massa buah.

Deteksi buah memakai segmentasi warna HSV dengan OpenCV, pemisahan buah berdempetan dengan *watershed*, dan pencocokan lingkaran. Klasifikasi memakai MobileNetV2 yang dilatih di Edge Impulse. Pada pelatihan terakhir, performa pada set validasi menghasilkan F1-score 59,3%. Tomat merah dikenali dengan akurasi rata-rata 65,3%, sedangkan tomat hijau lebih lemah karena warnanya sama dengan latar belakang daun.

Untuk pengukuran volume, buah dipindai dengan pemindai 3D Ciclop yang memakai dua laser garis 650 nm, lalu *point cloud* dibentuk dari pemindaian itu. Gambar rekonstruksi *multi-view* diambil secara manual dengan mengelilingi buah. Model 3D dan model bola (*sphere*) dibandingkan. Menurut kajian, kedua pendekatan tidak berbeda dalam korelasi terhadap perlakuan irigasi, dengan R² 0,77 sampai 0,95 (Tabel 4).

Keterbatasan utama dinyatakan penulis: berat dan jumlah buah diremehkan karena robot sulit memotret buah di belakang daun tanaman dalam barisan. Akibatnya, hitungan dari satu sisi tanaman tidak mencakup seluruh buah. Dari sisi rekayasa, kajian ini menunjukkan bahwa penghitungan dengan citra RGB saja kehilangan buah yang tertutup, dan pemindaian 3D dipakai untuk mengukur ukuran, bukan untuk menghitung ulang buah lintas pandang.

Percobaan dilakukan pada musim tanam 2022 di kebun percobaan Universitas Pertanian dan Ilmu Hayati Hongaria di Gödöllő, dengan hibrida tomat H1015. Ada lima perlakuan irigasi (T0 sampai T4) dengan empat ulangan, dan data dikumpulkan dari 20 lokasi sampel. Dalam abstrak, penulis melaporkan galat relatif berat 21,90% untuk model 3D, akurasi klasifikasi berbasis objek 55,33% di atas tingkat tanaman atau barisan, dan selisih rata-rata 3,42 kg untuk estimasi dari citra DSLR.
