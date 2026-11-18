# Deep Learning Based Apples Counting for Yield Forecast Using Proposed Flying Robotic System

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yldrm2023deep` |
| Judul asli | Deep Learning Based Apples Counting for Yield Forecast Using Proposed Flying Robotic System |
| Penulis | Y\ild\ir\im, \cSahin; Ulu, Burak |
| Tahun | 2023 |
| Venue | Sensors |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [yldrm2023deep.pdf](../pdf/yldrm2023deep.pdf)
- DOI resmi: https://doi.org/10.3390/s23136171

## Gambaran Umum

Penelitian ini bertujuan memperkirakan hasil panen apel secara otomatis agar produsen dapat membuat perkiraan hasil sebelum kesepakatan komersial dan perusahaan asuransi dapat menghitung premi secara lebih tepat. Pemeriksaan manual dianggap memakan waktu lama dan menimbulkan kerugian 20–30 persen. Penulis mengusulkan sistem robot terbang (Flying Robotic System, FRS) yang terbang mengikuti lintasan tetap di kebun apel, lalu mendeteksi dan menghitung apel dari citra video yang dikirim ke stasiun darat.

Tanaman yang diteliti adalah apel merah di kebun seluas 350 dekare di distrik Yeşilhisar, Kayseri, Türkiye, yang memiliki 90.000 pohon. Percobaan difokuskan pada bagian lorong sepanjang 50 m dengan 40 pohon. Data dikumpulkan setiap dua minggu antara September dan November 2021 memakai kamera GoPro Hero 9 beresolusi 5120×2160 piksel (20 MP), lalu dikecilkan menjadi 1728×1296 karena ukuran aslinya terlalu lama diproses. Citra diambil pada ketinggian 2 m dengan toleransi ±10 cm. Penandaan memakai LabelImg dalam format .xml yang kemudian diubah ke .record. Seratus foto dengan rata-rata 40 apel tiap foto menghasilkan 4.000 apel berlabel, yang dibagi 80 persen untuk latih dan 20 persen untuk uji dengan 3.000 iterasi.

Sistem FRS memakai kerangka X dengan empat motor sikat tanpa arus searah, pengontrol Pixhawk Cube 2, komputer Odroid XU4, dan baterai lithium polimer 4S 2500 mAh. Robot melintasi lorong sejauh 50 m dengan panduan GPS dan pustaka Dronekit; citra dikirim lewat tautan radio frekuensi dengan protokol MAVLink ke stasiun darat berbasis Intel i7-2600 dan GTX 1050 Ti, tempat inferensi CNN dijalankan. Dua arsitektur deteksi dibandingkan, yaitu SSD-Mobilenet dan Faster R-CNN, keduanya awalnya terlatih pada himpunan data COCO lalu disesuaikan dengan data khusus apel. Parameter latih adalah 3.000 langkah, ukuran kumpulan 4, dan laju pembelajaran 0,015–0,04. Setiap apel yang terdeteksi ditandai dengan kotak pembatas (bounding box); hitungan diakumulasi antara posisi pertama dan kedua sepanjang lintasan.

Hasil deteksi pada Tabel 4 menunjukkan SSD-Mobilenet versi usulan mencapai recall 0,72, presisi 0,83, skor F1 0,77, dan mAP@0,5 sebesar 71 persen, sedangkan Faster R-CNN versi usulan mencapai recall 0,87, presisi 0,96, skor F1 0,91, dan mAP@0,5 sebesar 93 persen. Model versi COCO tanpa penyesuaian memberikan hasil jauh lebih rendah. Pada uji penghitungan atas 140 apel dari delapan pohon, Faster R-CNN terlatih mendeteksi 129 apel dengan satu deteksi salah dan akurasi 93 persen; SSD-Mobilenet terlatih mendeteksi 65 apel dengan dua deteksi salah dan akurasi 46 persen; Faster R-CNN versi COCO mendeteksi 10 apel dengan dua belas deteksi salah dan akurasi 6 persen; SSD-Mobilenet versi COCO mendeteksi 32 apel dengan delapan deteksi salah dan akurasi 13 persen. Metrik dihitung dari true positive, true negative, false positive, dan false negative, dengan akurasi sebagai (TP + TN)/(TP + TN + FP + FN) dan IoU sebagai ukuran pelokalan. Penulis menyatakan peningkatan akurasi 10 persen dan penghematan waktu setidaknya enam kali lipat, dengan nilai loss model Faster R-CNN terlatih di bawah 0,1.

Batasan yang dinyatakan penulis: Faster R-CNN bekerja lebih lambat karena proses pemindaian ganda, sehingga kurang cocok untuk FRS meski akurasinya lebih tinggi. Sinyal satelit tidak efektif di bawah penutup kebun dan citra dinamis terpengaruh pembiasan cahaya. Penghitungan kumulatif masih dapat mencampur atau menghitung apel yang sama berkali-kali dari frame video yang berbeda. Penulis mengusulkan pemisahan frame unik, verifikasi posisi dengan SLAM, dan peningkatan efisiensi energi untuk menghitung seluruh kebun sebagai tindak lanjut.

