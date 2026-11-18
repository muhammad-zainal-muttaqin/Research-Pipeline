# FruitNeRF++: A Generalized Multi-Fruit Counting Method Utilizing Contrastive Learning and Neural Radiance Fields

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `meyer2025fruitnerf` |
| Judul asli | FruitNeRF++: A Generalized Multi-Fruit Counting Method Utilizing Contrastive Learning and Neural Radiance Fields |
| Penulis | Meyer, Lukas; Ardelean, Andrei-Timotei; Weyrich, Tim; Stamminger, Marc |
| Tahun | 2025 |
| Venue | IEEE International Conference on Intelligent Robots and Systems |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple, citrus, mango, peach/nectarine, pear, plum/apricot |

## Tautan Akses
- PDF: [meyer2025fruitnerf.pdf](../pdf/meyer2025fruitnerf.pdf)
- DOI resmi: https://doi.org/10.1109/iros60139.2025.11247341

## Gambaran Umum

Penelitian ini bertujuan menghitung buah dari kumpulan foto kebun yang tidak
teratur dengan satu kerangka kerja yang berlaku untuk banyak jenis buah.
Permasalahan utama adalah kebanyakan metode hanya dioptimalkan untuk satu
jenis buah. Pendahulunya, FruitNeRF, memakai template bentuk buah tertentu dan
pemadanan bertahap, sehingga perlu penyesuaian untuk setiap jenis dan tahap
tumbuh. Penulis mengusulkan FruitNeRF++ yang menghilangkan ketergantungan
pada bentuk buah dengan menyandikan identitas setiap buah ke dalam medan
instance neural memakai pembelajaran kontrastif.

Data terdiri dari dua himpunan. Himpunan sintetis mewarisi model pohon
FruitNeRF untuk apel, plum, lemon, pir, persik, dan mangga; setiap model
dirender 300 citra berukuran 1024 × 1024 piksel dari belahan bumi atas dan
dilengkapi mask instance sebenarnya. Himpunan dunia nyata FUJI memuat 582
citra dari 12 pohon apel di kebun komersial, diturunkan menjadi 1296 × 864
piksel. Pose kamera diperoleh dengan COLMAP dan didaftarkan manual untuk
kedua sisi pohon. Mask semantik dan instance diprediksi memakai model dasar
penglihatan Grounded-SAM dan Detic tanpa melatih model khusus.

Mekanisme penghitungan dimulai dari mask instance dua dimensi yang tidak
konsisten antarpandang. Medan instance memetakan koordinat tiga dimensi ke
vektor penyematan sehingga titik dalam satu buah berdekatan dan titik dari
buah berbeda terpisah. Penulis mengadaptasi rugi InfoNCE dengan prototipe buah
sebagai pasangan positif dan prototipe buah lain sebagai negatif, serta
menambang negatif lokal berupa buah tetangga terdekat. Pelatihan dilakukan
bertahap: kerapatan dan warna, lalu medan semantik, kemudian medan instance
saja dengan dua medan pertama dibekukan. Setelah pelatihan, seluruh medan
disampel secara volumetrik menjadi awan titik buah berfitur, lalu dikelompokkan
dengan k-Means untuk partisi ruang dan HDBSCAN memakai jarak gabungan cosine
dengan bobot λc = 1 dan Euclidean dengan bobot λe = 5. Jumlah klaster menjadi
jumlah buah. Pada data sintetis dipakai D = 32, τ = 0,2, λc = 1, dan λe = 1;
pada FUJI dipakai D = 32, τ = 0,35, λe = 5, 600.000 titik, dan 40 partisi.

Hasil pada data sintetis dengan mask sebenarnya memberi F1-score rata-rata
0,925, lebih tinggi daripada FruitNeRF; mask Grounded-SAM memberi 0,832 dan
mask Detic memberi 0,776. Per jenis buah dengan mask sebenarnya, F1-score
apel 0,996 (285/283), plum 0,859 (572/745), lemon 0,978 (312/326), pir 0,996
(252/250), persik 0,996 (153/152), dan mangga 0,713 (649/1150). Acuan
penghitungan adalah pusat buah hasil klaster yang dekat dengan pusat buah
sebenarnya. Pengujian tambahan pada himpunan Messy Rooms yang memuat 100 benda
rumah tangga menghasilkan 99 benda terdeteksi.

Batasan yang dinyatakan penulis mencakup waktu latih sekitar delapan jam pada
NVIDIA A5000 24 GB untuk adegan besar seperti FUJI, sehingga metode ini tidak
sesuai untuk penggunaan langsung (real time); konvergensi medan instance
menyumbang lebih dari separuh waktu latih. Akurasi sangat bergantung pada
cakupan pohon yang baik dan menurun karena data bernoise, terutama pose tidak
tepat yang mencemari penyematan buah tetangga. Segmen instance juga memisahkan
satu buah menjadi dua ketika daun atau cabang menutupnya. Buah yang tumbuh
dalam gugus, seperti pisang, beri, dan kurma, masih menjadi tantangan tersendiri.

