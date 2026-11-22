# Detection, counting and maturity assessment of cherry tomatoes using multi-spectral images and machine learning techniques

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2020detection` |
| Judul asli | Detection, counting and maturity assessment of cherry tomatoes using multi-spectral images and machine learning techniques |
| Penulis | Chen, I-Tzu; Lin, Huei-Yung |
| Tahun | 2020 |
| Venue | Visigrapp 2020 Proceedings of the 15th International Joint Conference on Computer Vision Imaging and Computer Graphics Theory and Applications |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [chen2020detection.pdf](../pdf/chen2020detection.pdf)

## Gambaran Umum

Chen dkk. (2020) mengembangkan sistem penghitungan tomat ceri (*cherry tomato*) pada citra dari kamera yang bergerak di sepanjang tanaman. Sistem ini menggabungkan tiga bagian: deteksi tomat pada citra RGB dengan Faster R-CNN, klasifikasi tingkat kematangan dengan SVM (*support vector machine*) memakai fitur warna hijau dan NDVI dari kamera multispektral, dan pelacakan dengan DeepSORT agar setiap tomat hanya dihitung sekali. Penulis menyebut bahwa penghitungan yang hanya mengandalkan deteksi per bingkai akan menghitung tomat yang sama berulang kali ketika kamera bergerak. Pelacakan dengan ID unik ditempatkan sebagai solusi untuk masalah tersebut.

Penghitungan buah dari video kebun berbeda dengan penghitungan dari satu foto. Buah yang sama terlihat pada banyak bingkai saat kamera lewat, sehingga jumlah deteksi per bingkai tidak sama dengan jumlah buah. Penulis menyebut masalah penghitungan ganda (*double counting*) sebagai alasan utama memasukkan pelacakan ke dalam sistem. Dalam naskah, masalah ini muncul di Bagian 4.2 dan di simpulan.

Deteksi memberi kotak pembatas (*bounding box*) untuk setiap tomat pada setiap bingkai. DeepSORT mengaitkan kotak-kotak di bingkai berurutan menjadi satu lintasan dengan satu ID. Jumlah buah kemudian dihitung dari jumlah ID unik, bukan dari jumlah deteksi. Kematangan ditentukan pada tingkat tomat, sehingga setiap ID juga membawa label kelas kematangan.

Faster R-CNN dengan backbone ResNet-50 dan FPN (*feature pyramid network*) dipakai sebagai detektor. Pada Tabel 2, Faster R-CNN mencapai mAP 62,35%, sedangkan YOLO v3 mencapai 53,50% pada data yang sama. Penulis memakai Faster R-CNN sebagai detektor utama karena selisih ini.

Pada Tabel 3, mAP untuk deteksi dan klasifikasi kematangan bersama adalah 46,02% dengan histogram matching dan 45,14% tanpa histogram matching. Selisihnya kecil, sehingga pengaruh histogram matching pada deteksi tampak terbatas pada data ini.

Kamera multispektral Parrot SEQUOIA+ merekam pita NIR, merah, dan hijau. NDVI dihitung sebagai (NIR−RED)/(NIR+RED). Fitur hijau dan NDVI dipakai sebagai masukan SVM. Model dilatih dengan 42 sampel dan menghasilkan akurasi uji di atas 90%. Pada Tabel 4, mAP klasifikasi kematangan saja untuk Faster R-CNN dengan histogram matching adalah 99,67%. Angka ini mengukur klasifikasi pada tomat yang sudah terdeteksi, sehingga tidak sama dengan mAP deteksi pada Tabel 2 dan Tabel 3.

Pada Bagian 4.2, penulis menulis bahwa pendekatan ini melacak tomat yang sama dan memberinya ID unik untuk menghindari penghitungan ganda. Simpulan mengulang klaim yang sama: pelacakan multi-objek dipasang agar setiap tomat memperoleh ID unik selama kamera bergerak. Gambar 7 membandingkan SORT dengan DeepSORT pada evaluasi pelacakan.

Penulis melaporkan tiga jenis angka: mAP deteksi (Tabel 2), mAP deteksi dengan kematangan (Tabel 3), dan mAP klasifikasi kematangan (Tabel 4). Perbandingan detektor dilakukan pada data yang sama, yaitu Faster R-CNN dan YOLO v3. Perbandingan SORT dan DeepSORT dilaporkan secara visual pada Gambar 7.

Kelebihan utama studi ini adalah pemisahan yang jelas antara deteksi, kematangan, dan pelacakan, sehingga tiap komponen dapat diukur sendiri. Penggunaan kamera multispektral untuk NDVI juga memberi fitur yang tidak ada pada RGB saja.

Klasifikasi kematangan dilatih dengan 42 sampel, jumlah yang kecil untuk klaim akurasi di atas 90%. Secara konseptual, angka mAP deteksi tidak menunjukkan seberapa baik penghitungan akhir, karena penghitungan ganda dan buah yang terlewat tidak tercermin di mAP.
