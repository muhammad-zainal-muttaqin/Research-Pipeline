# End-to-End Object Detection with Transformers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `carion2020end` |
| Judul asli | End-to-End Object Detection with Transformers |
| Penulis | Carion, Nicolas; Massa, Francisco; Synnaeve, Gabriel; Usunier, Nicolas; Kirillov, Alexander; Zagoruyko, Sergey |
| Tahun | 2020 |
| Venue | Lecture Notes in Computer Science Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [carion2020end.pdf](../pdf/carion2020end.pdf)
- DOI resmi: https://doi.org/10.1007/978-3-030-58452-8_13

## Gambaran Umum

Kajian ini mengubah deteksi objek menjadi masalah prediksi himpunan langsung (*direct set prediction*). Detektor modern memprediksi secara tidak langsung melalui usulan, *anchor*, atau pusat jendela, lalu bergantung pada pascaproses seperti *non-maximum suppression* (NMS) untuk menghilangkan duplikat serta pada aturan heuristik penetapan kotak ke *anchor*. Penulis menghilangkan komponen buatan tersebut dan mengusulkan DETR (*DEtection TRansformer*) yang memprediksi seluruh objek sekaligus, dilatih dari ujung ke ujung dengan rugi himpunan berbasis pencocokan bipartit. Dua unsur utamanya adalah rugi pencocokan yang memaksa prediksi unik dan arsitektur *transformer* penyandi–pengode dengan dekode paralel, bukan dekode autoregresif seperti upaya sebelumnya.

Kajian ini bukan tentang tanaman; ia termasuk metode dari luar pertanian yang dapat ditransfer ke deteksi instance. Percobaan memakai dataset COCO 2017 untuk deteksi dan segmentasi panoptik, dengan 118.000 citra latih dan 5.000 citra validasi; rata-rata tujuh instance per citra dan maksimal 63 instance pada satu citra latih. Metrik utama adalah AP untuk kotak (bbox AP), dengan rincian AP50, AP75, APS, APM, dan APL; untuk segmentasi panoptik dipakai Panoptic Quality (PQ) beserta komponen SQ dan RQ. Perbandingan dilakukan terhadap Faster R-CNN yang diperkuat dengan GIoU, augmenasi *random crop*, dan jadwal latih panjang.

Mekanisme DETR terdiri dari tiga bagian: *backbone* CNN untuk mengekstrak peta fitur, *transformer encoder*, serta *decoder* dengan FFN prediksi. Peta fitur dari ResNet-50 atau ResNet-101 diratakan dan diberi penyandian posisi sebelum masuk ke *encoder* yang memakai *self-attention* global. *Decoder* menerima sejumlah kecil penyematan posisi terlatih tetap yang disebut *object queries*, lalu memperhatikan keluaran *encoder* secara paralel. Setiap keluaran diterjemahkan oleh FFN tiga lapis menjadi kelas, termasuk kelas khusus ∅ untuk slot kosong, serta koordinat pusat, tinggi, dan lebar kotak secara absolut. Pelatihan mencari permutasi pencocokan optimal dengan algoritma Hungaria antara N prediksi dan kotak benar yang ditambahi ∅, lalu menghitung rugi Hungaria berupa kombinasi negatif log-probabilitas kelas dan rugi kotak; rugi kotak menggabungkan ℓ1 dan GIoU yang invarian skala. Rugi bantu diterapkan setelah setiap lapisan *decoder* untuk membantu model menghasilkan jumlah objek yang tepat.

Hasil utama menunjukkan DETR sebanding dengan Faster R-CNN yang telah dioptimasi. Pada COCO validation, DETR dengan ResNet-50 mencapai AP 42,0 dengan 41 juta parameter dan 28 FPS, sedangkan Faster R-CNN-FPN+ mencatat AP 42,0 dengan 42 juta parameter dan 26 FPS; keunggulan DETR ada pada objek besar (APL 61,1 berbanding 53,4), tetapi tertinggal pada objek kecil (APS 20,5 berbanding 26,6) (Tabel 1). DETR-DC5-R101 mencapai AP 44,9 dan AP50 64,7. Ablasi menunjukkan penghapusan seluruh lapisan *encoder* menurunkan AP dari 41,6 menjadi 36,7 (Tabel 2), penghapusan penyandian posisi spatial menurunkan AP menjadi 32,8 (Tabel 3), dan penggunaan ℓ1 tanpa GIoU menghasilkan AP 35,8 dibanding 40,6 pada konfigurasi lengkap (Tabel 4). Untuk segmentasi panoptik, DETR-R101 memperoleh PQ 45,1 dan PQ untuk kelas *stuff* 37,0, mengungguli PanopticFPN++ dengan PQ 44,1 (Tabel 5); pada COCO test, model mencatat PQ 46. Seluruh angka bersumber dari tabel naskah.

Batasan yang dinyatakan penulis mencakup kinerja yang lebih rendah pada objek kecil dan kebutuhan jadwal latih yang jauh lebih lama dibanding detektor standar, yakni 300 epoch untuk ablasi dan 500 epoch untuk perbandingan, dengan pelatihan tiga hari pada 16 GPU V100. Varian DC5 menaikkan biaya *self-attention encoder* enam belas kali dan total biaya komputasi dua kali. Penulis juga mengakui tantangan pada optimalisasi dan pelatihan, serta menyebut bahwa pada segmentasi panoptik mask AP untuk kelas *thing* masih kalah hingga delapan poin dari baseline meski PQ-nya kompetitif. Selain itu, mekanisme *attention* menyebabkan setiap slot *object query* mengkhususkan diri pada area dan ukuran tertentu, yang diuji tidak menjadi ketergantungan kelas melalui percobaan generalisasi pada 24 jerapah dalam satu citra sintetis.
