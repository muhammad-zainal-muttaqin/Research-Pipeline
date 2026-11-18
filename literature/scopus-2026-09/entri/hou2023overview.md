# An Overview of the Application of Machine Vision in Recognition and Localization of Fruit and Vegetable Harvesting Robots

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hou2023overview` |
| Judul asli | An Overview of the Application of Machine Vision in Recognition and Localization of Fruit and Vegetable Harvesting Robots |
| Penulis | Hou, Guangyu; Chen, Haihua; Jiang, Mingkun; Niu, Runxin |
| Tahun | 2023 |
| Venue | Agriculture Switzerland |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [hou2023overview.pdf](../pdf/hou2023overview.pdf)
- DOI resmi: https://doi.org/10.3390/agriculture13091814

## Gambaran Umum

Tinjauan ini membahas penggunaan visi mesin dalam pengenalan dan penentuan posisi robot pemanen buah dan sayur. Biaya tenaga kerja untuk pemanenan yang kompleks terus naik, sehingga peralatan pertanian bergerak ke arah sistem tanpa operator. Visi mesin dipilih karena memberi informasi visual dengan biaya perangkat keras yang relatif rendah. Robot pemanen menghadapi lingkungan kerja yang kompleks dan banyak ketidakpastian, sehingga sistem pengenalan dan penentuan posisi harus memenuhi persyaratan ketepatan, kecepatan, dan kestabilan. Penulis merangkum sensor, algoritma, tantangan, dan arah penelitian berikutnya.

Tinjauan ini menyusun hasil literatur, bukan percobaan baru; pernyataan ketersediaan data menyatakan tidak ada data baru. Penulis menganalisis 49 publikasi untuk jenis sensor visual. Sensor dibedakan menjadi sensor citra dua dimensi dan tiga dimensi, yaitu kamera monokuler, kamera stereo, kamera cahaya terstruktur, dan kamera multispektral; kamera cahaya terstruktur paling banyak digunakan. Algoritma dibagi menjadi segmentasi citra, deteksi objek, dan rekonstruksi tiga dimensi. Buah dan sayur yang dibahas mencakup apel, jeruk, kiwi, leci, stroberi, anggur, mangga, tomat, timun, pir, persik, pisang, dan teh.

Mekanisme pengenalan memakai prinsip berbeda pada tiap sensor. Kamera monokuler mengekstraksi warna, bentuk, dan tekstur, tetapi kehilangan informasi kedalaman sehingga dipasangkan dengan algoritma atau LiDAR. Kamera stereo menghitung kedalaman dari perbedaan posisi citra kiri dan kanan melalui triangulasi. Kamera cahaya terstruktur memproyeksikan pola yang diketahui ke pemandangan dan menyimpulkan kedalaman dari derajat deformasi pola. Kamera multispektral membedakan target berdasarkan sifat radiasi pada beberapa panjang gelombang. Segmentasi memisahkan buah dari latar dengan ambang kedalaman, kemiripan, binarisasi Otsu, bentuk lingkaran Hough, serta segmentasi semantik PSP-Net dan U-Net atau segmentasi instance Mask R-CNN dan YOLACT. Deteksi objek memakai varian YOLO yang diperbaiki melalui klaster anchor K-means, modul perhatian SE dan CBAM, atau perubahan fungsi aktivasi. Rekonstruksi tiga dimensi mengubah citra atau awan titik menjadi model tiga dimensi dengan klaster titik, iterasi titik terdekat, Delaunay, atau ICP. Pengenalan dan penentuan posisi lintas pandang untuk penghitungan objek unik tidak dinyatakan.

Angka hasil berikut diambil dari kajian primer yang ditinjau dan dihitung dengan metrik masing-masing, karena tinjauan ini tidak menghasilkan data baru. Kamera monokuler pada apel mencatat tingkat keberhasilan lebih dari 90% dan akurasi 90% berdasarkan warna dan tekstur. Penentuan posisi titik panen tomat dengan kamera terstruktur mencapai 93,83%, sedangkan pemanenan jeruk dengan Kinect V2 mencapai 80,51%. Kamera multispektral mengidentifikasi 80–89% jeruk, mendeteksi 69,2% paprika lapangan, dan mencapai 83,3% pada timun. Segmentasi semantik mencatat akurasi 92,5–98%, segmentasi instance 89,7–95,78%, dan segmentasi berbasis pembelajaran mesin lebih tinggi sekitar lima poin persentase daripada segmentasi tradisional. Deteksi YOLO yang diperbaiki mencatat 94,29% pada tomat ceri dengan waktu 0,058 detik, 96,76% pada apel dengan 0,015 detik, dan 97,5% pada tomat dengan 0,227 detik. Model dengan residual ResNet mencatat akurasi 94,44–97,07% dengan waktu 0,017–0,093 detik. Rekonstruksi tiga dimensi berkisar antara 74,1% pada stroberi dan 97,5% pada apel. Pada kondisi cahaya alami, akurasi turun sampai 59,2%, dan tingkat keberhasilan pemanenan berkisar antara 38% dan 78%.

Penulis menyatakan sejumlah batasan. Kamera monokuler tidak dapat dipakai pada kondisi gelap atau cahaya rendah dan peka terhadap pencahayaan. Kamera stereo memerlukan kalibrasi presisi tinggi, waktu komputasi lama, dan kehilangan kedalaman pada tepi objek. Cahaya matahari mengalahkan sebagian besar citra inframerah pada kamera terstruktur di luar ruang, serta biayanya tinggi. Kamera multispektral memerlukan pengolahan berat sehingga tidak cocok untuk pemanenan waktu nyata. Segmentasi tradisional peka terhadap perubahan cahaya, dan rekonstruksi tiga dimensi memerlukan komputasi besar. Pengenalan dengan tumpang tindih atau halangan sangat bergantung pada informasi awal. Ujung efektor hanya dapat mengompensasi kesalahan awal perangkat keras visual, bukan kesalahan acak yang tidak diketahui. Penulis juga mencatat kurangnya dataset yang mencakup berbagai tahap pertumbuhan dan perbedaan antarobjek. Arah yang diusulkan mencakup fusi banyak sensor, pengumpulan citra pada berbagai tahap pertumbuhan, pengaturan kebun seperti pemangkasan untuk mengurangi halangan, serta pemanfaatan model besar melalui antarmuka API.

