# Measurement of the ripening rate on coffee branches by using 3D images in outdoor environments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ramos2018measurement` |
| Judul asli | Measurement of the ripening rate on coffee branches by using 3D images in outdoor environments |
| Penulis | Ramos, Paula J.; Avenda\~no, Jonathan; Prieto, Flavio A. |
| Tahun | 2018 |
| Venue | Computers in Industry |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | coffee |

## Tautan Akses
- PDF: [ramos2018measurement.pdf](../pdf/ramos2018measurement.pdf)
- DOI resmi: https://doi.org/10.1016/j.compind.2018.03.024

## Gambaran Umum

Panen kopi dilakukan berulang kali dalam satu musim karena buah tidak matang pada waktu yang sama. Kondisi ini membuat biaya tenaga kerja dan pemetikan tinggi. Pengetahuan tentang persentase buah matang pada cabang, pohon, dan lahan membantu penjadwalan tenaga kerja serta menentukan strategi panen tiap lot. Penelitian ini bertujuan menentukan indeks kematangan cabang kopi secara nondestruktif, sehingga keputusan panen dapat didasarkan pada ketersediaan buah matang di cabang.

Data dikumpulkan di kebun kopi berumur tiga tahun di Kolombia pada semester kedua 2015. Sebanyak 30 cabang ditandai di awal musim panen dan dipantau pada sembilan waktu pengumpulan. Sebanyak 90 cabang digunakan dalam klasifikasi. Video direkam dengan kamera utama ponsel *Samsung Galaxy S5* yang bersifat monokular, dengan resolusi HD dan 30 fps. Setiap video berdurasi rata-rata 15 detik, dan satu gambar diambil dari setiap lima frame. Rata-rata diperoleh 90 gambar per cabang untuk gerakan linear dan 180 gambar untuk gerakan zig-zag. Kecepatan perekaman sekitar 5 cm per detik. Akuisisi dilakukan pukul 07.30 sampai 17.00, dengan pengukuran cahaya langsung dan difus menggunakan luxmeter. Jumlah buah pada tiap tahap kematangan dihitung secara manual sebelum setiap waktu pengumpulan.

Metode mengambil frame yang tajam dengan indeks ketajaman berbasis filter Sobel, Laplacian, dan Canny. Frame tersebut kemudian direkonstruksi menjadi *point cloud* 3D dengan *Bundle Structure from Motion*. Sebanyak 17 fitur dihitung untuk tiga tahap kematangan, daun, dan batang. Delapan model klasifikasi dilatih dengan ukuran subregion kelengkungan yang berbeda. Model terbaik memakai subregion sebesar 6,5% dari ukuran total awan titik. Akurasi klasifikasi berada pada rentang 42% sampai 92%, dengan rata-rata spesifisitas 86%. Model estimasi statistik untuk tiap tahap kematangan menunjukkan bahwa persentase buah matang cenderung terlalu tinggi, persentase buah setengah matang cenderung terlalu rendah, dan persentase buah mentah sebanding satu banding satu. Galat estimasi berada pada rentang 3,7% sampai 8,7%, dengan korelasi 0,64 sampai 0,98. Indeks kematangan yang dihitung dari hasil pemantauan musim panen menentukan apakah cabang siap panen dengan efisiensi 83%.

Penulis menyatakan beberapa batasan. Jarak antara kamera dan cabang tidak dapat dijamin karena sistem akuisisi bergantung pada pergerakan tangan. Akibatnya, awan titik tidak dapat diskalakan ke satuan metrik. Pencahayaan yang tidak terkendali juga menimbulkan *overexposure* yang langsung memengaruhi hasil klasifikasi. Kecepatan perekaman sekitar 5 cm per detik harus dijaga agar gambar tetap jelas. Sistem ini juga bekerja di bawah hujan dan bayangan daun, sehingga kinerjanya bergantung pada kondisi lapangan saat akuisisi.
