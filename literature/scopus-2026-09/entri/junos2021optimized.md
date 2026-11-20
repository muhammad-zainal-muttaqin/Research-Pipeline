# An optimized YOLO-based object detection model for crop harvesting system

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `junos2021optimized` |
| Judul asli | An optimized YOLO-based object detection model for crop harvesting system |
| Penulis | Junos, Mohamad Haniff; Mohd Khairuddin, Anis Salwa; Thannirmalai, Subbiah; Dahari, Mahidzal |
| Tahun | 2021 |
| Venue | Iet Image Processing |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [junos2021optimized.pdf](../pdf/junos2021optimized.pdf)
- DOI resmi: https://doi.org/10.1049/ipr2.12181

## Gambaran Umum

Kajian ini (Junos dkk., 2021) membangun detektor objek bernama YOLO-P untuk tandan buah segar (TBS) kelapa sawit. YOLO-P adalah turunan YOLOv3 tiny dengan backbone DenseNet-201, empat skala deteksi, dan anchor box hasil pengelompokan (clustering) dari data latih. Detektor mengenali tandan dalam tiga kelas tingkat kematangan: matang, kurang matang, dan lewat matang.

Data dikumpulkan dengan kamera EKEN H9R 12 MP yang dipasang pada traktor di kebun Sime Darby, Selangor. Sebanyak 5.000 citra diambil dari video. Data dibagi 70/30 untuk latih dan uji, dengan 350 citra uji.

Hasil utama dilaporkan pada abstrak: mAP 98,68%, F1 0,97, dan ukuran model 76 MB. Tabel 8 pada naskah memuat mAP 98,91% untuk YOLO-P, dengan AP 98,65% (matang), 98,18% (kurang matang), dan 99,91% (lewat matang). Kedua nilai mAP itu berbeda.

Panen sawit masih bergantung pada penilaian manual terhadap kematangan tandan. Penulis menyebut bahwa sistem panen otomatis memerlukan deteksi tandan di lapangan yang dapat membedakan tingkat kematangan. Kajian ini tidak membandingkan detektor dengan metode sebelumnya pada data yang sama, sehingga klaim keunggulan atas metode lain tidak dapat dinilai dari isi kajian.

Gagasan utamanya adalah memakai detektor satu tahap berbasis YOLO dengan backbone yang lebih dalam dan anchor yang disesuaikan dengan ukuran tandan di citra traktor. Keluaran berupa kotak pembatas (bounding box) dan label kelas kematangan untuk setiap tandan pada satu citra. Kajian ini tidak menghitung tandan lintas beberapa pandang atau antarframe.

Citra dari video diberi anotasi kotak dan kelas kematangan. Data dibagi 70/30 menjadi data latih dan data uji. Detektor dilatih dengan backbone DenseNet-201, yang menyambungkan setiap lapisan dengan lapisan-lapisan sebelumnya. Empat skala deteksi menangkap tandan dari ukuran besar sampai kecil. Anchor box diperoleh dengan clustering pada kotak-kotak anotasi.

Evaluasi memakai precision, recall, F1, average IoU (irisan atas gabungan, ukuran kecocokan kotak prediksi dengan kotak anotasi), dan AP per kelas. Tabel 2 memuat YOLO-P dengan precision 96,60%, recall 98,12%, F1 0,97, dan average IoU 83,34%.

Eksperimen menguji YOLO-P pada 350 citra uji dari kebun Sime Darby. Pada Tabel 8, rata-rata IoU YOLO-P tercatat 83,69%. Kelas lewat matang memiliki AP tertinggi, sedangkan kurang matang memiliki AP terendah di antara ketiga kelas. Penulis menyimpulkan model layak untuk deteksi di perkebunan sawit dan dapat diterapkan pada sistem panen otomatis.

Kajian ini tidak menyebut apakah angka mAP dihitung pada data uji atau data validasi, dan tidak menyebut protokol perhitungan mAP yang dipakai. Angka mAP per baris Tabel 2 tidak tercantum dalam kajian ini.

Kelebihan kajian ini adalah cakupan kelas kematangan yang lengkap dan pelaporan metrik per kelas. Data diambil dari kebun sungguhan dengan kamera pada traktor, bukan dari citra yang dikurasi.

Dari sisi rekayasa, data hanya berasal dari satu kebun dan satu jenis kamera. Ukuran data 5.000 citra dan 350 citra uji tergolong kecil untuk klaim generalisasi. Kajian ini belum melaporkan deteksi video real-time, yang disebut penulis sebagai kerja lanjut. Algoritma penghitungan untuk prediksi hasil juga belum ada dalam kajian ini.
