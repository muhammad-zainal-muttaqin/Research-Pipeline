# Computational Models in Precision Fruit Growing: Reviewing the Impact of Temporal Variability on Perennial Crop Yield Assessment

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `magro2023computational` |
| Judul asli | Computational Models in Precision Fruit Growing: Reviewing the Impact of Temporal Variability on Perennial Crop Yield Assessment |
| Penulis | Magro, Renata Bulling; Alves, Silvio Andr\'e Meirelles; Gebler, Luciano |
| Tahun | 2023 |
| Venue | SN Computer Science |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [magro2023computational.pdf](../pdf/magro2023computational.pdf)
- DOI resmi: https://doi.org/10.1007/s42979-023-02103-6

## Gambaran Umum

Tinjauan ini mengkaji model komputasional untuk menilai hasil panen tanaman tahunan dalam pertanian presisi buah. Masalah utamanya adalah hasil panen tahun berjalan merupakan akumulasi pengaruh iklim, pengelolaan, dan fisiologi dari siklus sebelumnya, sehingga penilaian yang hanya memakai variabel tahunan tidak memadai. Tanaman tahunan juga menunjukkan produksi bergantian antara tahun tinggi dan tahun rendah (alternate bearing), yang makin kuat pada skala lokal seperti zona pengelolaan atau pohon tunggal, tetapi cenderung saling mengimbangi pada skala wilayah atau nasional. Penulis meninjau 49 artikel yang diterbitkan antara 1978 dan April 2022, dicari melalui Google Scholar, Science Direct, dan Scopus dengan kata kunci terkait pemodelan hasil panen, pembelajaran mesin, dan pertanian presisi. Artikel dikelompokkan menurut strategi penilaian, kelas model, dan karakteristik variabel masukan.

Strategi dibedakan menjadi model estimasi yang memakai data dari musim berjalan (n) dan model prakira yang memakai data musim sebelumnya (n−1) atau sebelum buah matang. Model estimasi umumnya memakai variabel langsung seperti jumlah bunga dan buah, berat buah rata-rata, serta diameter penampang batang; model prakira lebih banyak memakai variabel tidak langsung seperti indeks vegetasi, data iklim, dan hasil panen masa lalu. Berdasarkan kelas model, estimasi didominasi model nonlinear sederhana (42%), diikuti model linier (32%) dan model nonlinear dalam seperti pembelajaran mendalam (26%). Untuk prakira, porsinya berturut-turut 41%, 35%, dan 24% untuk model mekanistik. Citra RGB dari kamera, sensor proksimal, satelit, dan pesawat tanpa awak dipakai untuk menghitung bunga dan buah, mengekstrak indeks vegetasi, serta mendeteksi buah pada berbagai tahap perkembangan.

Mekanisme pemodelan berubah dari regresi linier menjadi pembelajaran mesin ketika hubungan bersifat nonlinear dan bersifat stokastik. Pada estimasi, model ANN dengan citra satelit resolusi tinggi dan indeks vegetasi menghasilkan akurasi di atas 93% untuk kebun mangga; Faster R-CNN pada citra RGB UAV beresolusi 2 m menghasilkan akurasi 0,76–0,91 untuk deteksi bunga dan buah stroberi, tetapi salah mengklasifikasikan buah muda sebagai daun mati dan terkendala oklusi daun. Pendekatan CNN dengan geometri multitinjau melakukan pelacakan buah untuk menghindari penghitungan ganda sekaligus menempatkan buah dalam ruang 3-D, sehingga mendukung estimasi hasil panen. YOLO-V3 dilaporkan mengenali apel muda, sedang, dan matang meski saling bertumpang tindih atau tertutup daun dan ranting. Pada prakira, ANN dengan masukan NDVI menghasilkan galat mutlak rata-rata (MAE) 1,4 ton/ha untuk kebun anggur, lebih rendah daripada 2 ton/ha pada regresi konvensional; model pohon keputusan kabur pada kebun apel mengklasifikasikan hasil panen dengan benar pada 42 dari 56 kasus atau akurasi 75%, namun hanya dihitung pada data latih tanpa himpunan uji. Model WOFOST yang dimodifikasi memprediksi buah matang 2–3 hari lebih awal daripada pengamatan lapang, dan data cuaca historis 2014–2019 dipakai untuk memprakirakan hasil panen makadamia. Seluruh angka ini berasal dari kajian yang ditinjau, bukan percobaan penulis.

Batasan yang ditegaskan penulis adalah minimnya himpunan data jangka panjang yang representatif: hanya 11% kajian memakai catatan lebih dari 10 musim, sedangkan 47% memakai paling banyak tiga musim sebelumnya, sehingga variabilitas antartahun belum tertangkap. Hasil estimasi sulit diekstrapolasi lintas tahun karena pembungaan, oklusi, pencahayaan, dan perubahan kanopi bersifat spesifik lokasi serta belum ada konsensus penentuan tahap fenologi. Model mekanistik memerlukan banyak parameter kalibrasi dan dibatasi pengetahuan yang ada, sehingga kurang tanggap terhadap interaksi spesifik kultivar dan lokasi. Indeks vegetasi saja tidak menangkap campur tangan manusia, korelasinya berubah sesuai waktu akuisisi citra, dan variabel tanah baru diteliti dalam dua publikasi. Model nonlinear sederhana sangat bergantung pada mutu dan jumlah data serta peka terhadap derau, data tidak lengkap, dan pencilan; penulis juga mencatat belum ada kajian mengenai prakira hasil panen jangka panjang yang benar-benar tanpa variabel tahun berjalan.

