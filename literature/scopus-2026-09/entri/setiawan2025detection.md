# Detection of Oil Palm Fruit Ripeness through Image Feature Optimization using Convolutional Neural Network Algorithm

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `setiawan2025detection` |
| Judul asli | Detection of Oil Palm Fruit Ripeness through Image Feature Optimization using Convolutional Neural Network Algorithm |
| Penulis | Setiawan, Dedy; Eko Prasetyo Utomo, Pradita; Alfalah, Muksin |
| Tahun | 2025 |
| Venue | International Journal on Informatics Visualization |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [setiawan2025detection.pdf](../pdf/setiawan2025detection.pdf)
- DOI resmi: https://doi.org/10.62527/joiv.9.2.2687

## Gambaran Umum

Kajian ini bertujuan mengidentifikasi tingkat kematangan buah kelapa sawit dari citra. Penulis berangkat dari kebutuhan akan pemilahan buah yang lebih cepat dan akurat. Di Indonesia, pemilahan buah untuk produksi minyak sawit umumnya masih bergantung pada keputusan manusia. Penulis menyebut bahwa proses manual memakan waktu, sehingga diperlukan bantuan mekanis pada skala industri besar. Penulis juga menyebut bahwa sekitar 5 persen buah yang disortir oleh pabrik dinilai tidak layak olah. Karena itu, penelitian ini menerapkan *deep learning* dengan *Convolutional Neural Network* (CNN) untuk mengklasifikasikan buah ke dalam tiga kelas, yaitu mentah, matang, dan busuk.

Data penelitian berupa citra buah kelapa sawit. Sebagian citra diambil dari berbagai sumber internet, dan sebagian lain difoto langsung menggunakan kamera ponsel sesuai kelas yang ditentukan. Sumber sensornya berupa kamera RGB pada ponsel, dan pengujian akhir dijalankan melalui situs web berbasis *Streamlit*. Bagian abstrak menyebut 400 citra, sedangkan bagian metode menyebut 1.000 citra yang dibagi 80 persen untuk latih dan 20 persen untuk uji dengan metode *Train Test Split* dari Sklearn. Bagian hasil menyebut 400 citra latih dan 80 citra uji. Latar belakang setiap citra dihapus dan diganti warna putih menggunakan Photoshop. Augmentasi yang dipakai meliputi rescaling 1/255, shearing dengan skala 0,2, zoom 0,2, dan flip horizontal. Pada bagian hasil, penulis juga menyebut rotasi hingga 15 derajat. Ukuran input pada tahap pelatihan adalah 64 x 64 piksel dengan *batch size* 16.

Model CNN terdiri atas dua lapisan konvolusi dengan jumlah filter dan ukuran kernel yang berbeda. Setelah itu terdapat *dropout*, lapisan *flatten*, dan lapisan *fully connected* untuk klasifikasi. Pelatihan memakai *learning rate* 0,001 selama 10 *epoch* dan memakan waktu sekitar 30 menit. Pada akhir pelatihan, akurasi latih mencapai 0,9911 dengan *loss* 0,0261. Akurasi validasi mencapai 1,000 dengan *loss* 0,0028. Pada pengujian dengan 200 sampel, penulis melaporkan 66 citra per kelas. Dari matriks kebingungan, 60 citra mentah diprediksi benar, 62 citra matang diprediksi benar, dan 55 citra busuk diprediksi benar. Enam citra mentah salah diklasifikasikan sebagai busuk. Empat citra matang salah sebagai busuk dan satu citra sebagai mentah. Enam citra busuk salah sebagai mentah dan lima sebagai matang. Akurasi keseluruhan matriks tercatat 88,5 persen, yang dibulatkan penulis menjadi 88 persen. Pada tahap klasifikasi citra, penulis menguji enam citra dan memperoleh akurasi 100 persen. Penulis menyimpulkan bahwa akurasi latih mencapai 99,11 persen dan akurasi validasi mencapai 100 persen.

Penulis menyatakan bahwa dataset perlu diperkaya dengan sampel yang lebih rinci dari tiap kelas. Fokus penambahan itu adalah ciri khas buah mentah dan buah busuk. Penulis juga menyarankan percobaan dengan berbagai arsitektur CNN untuk meningkatkan akurasi model. Selain itu, pengujian dengan dataset yang lebih luas dan lebih beragam perlu dilakukan pada penelitian lanjutan. Pengujian pada tahap klasifikasi citra hanya memakai enam citra, sehingga hasil 100 persen pada tahap itu perlu dibaca dengan hati-hati. Penulis menilai bahwa teknologi ini menawarkan alternatif yang lebih cepat dan akurat dibandingkan metode manual, tetapi klaim tersebut didasarkan pada dataset yang masih terbatas.
