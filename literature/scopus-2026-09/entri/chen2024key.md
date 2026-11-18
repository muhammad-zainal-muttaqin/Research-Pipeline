# Key Technologies for Autonomous Fruit- and Vegetable-Picking Robots: A Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2024key` |
| Judul asli | Key Technologies for Autonomous Fruit- and Vegetable-Picking Robots: A Review |
| Penulis | Chen, Zhiqiang; Lei, Xiaohui; Yuan, Quanchun; Qi, Yannan; Ma, Zhengbao; Qian, Shicheng; Lyu, Xiaolan |
| Tahun | 2024 |
| Venue | Agronomy |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [chen2024key.pdf](../pdf/chen2024key.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy14102233

## Gambaran Umum

Tinjauan ini merangkum teknologi utama robot pemanen buah dan sayur otonom, yaitu sistem visi, deteksi dan penentuan posisi sasaran, serta rancangan ujung efektor. Latar belakangnya adalah berkurangnya tenaga kerja pertanian akibat urbanisasi dan meningkatnya biaya tenaga kerja. Menurut Kementerian Pertanian dan Pembangunan Pedesaan Tiongkok, upah bulanan rata-rata pekerja migran naik dari sekitar CNY 2609 pada 2013 menjadi sekitar CNY 4780 pada 2023, atau lebih dari 150%. Penulis menegaskan bahwa keberhasilan pemanenan bertumpu pada dua teknologi kritis, yaitu sistem visi untuk mengenali dan menentukan posisi buah serta mekanisme pemisah pada ujung efektor. Tinjauan ini juga menyoroti tanaman yang sudah dikomersialkan, seperti tomat, stroberi, dan apel, serta contoh robot dari berbagai negara.

Sistem visi terdiri atas kamera, modul pengolahan citra, penentu posisi, dan unit pemroses pusat. Sensor yang dipakai mencakup kamera warna, kamera inframerah dekat dan multispektral, susunan monokular atau binokular, kamera RGB-D, serta sensor laser dan ultrasonik. Penulis membandingkan kelima jenis sensor tersebut: kamera monokular murah dan sederhana tetapi tidak memperoleh ukuran sejati serta akurasinya 81–91%, pencocokan stereo binokular memberi informasi kedalaman kaya dengan akurasi 83–95% tetapi memerlukan algoritma dan daya komputasi besar, kamera RGB-D berakurasi 86–94% dengan keterbatasan resolusi dan kedalaman medan, dan pencari jangkau laser berakurasi 87–90% yang terhambat oleh daun serta ranting.

Untuk pengenalan, tinjauan membedakan tiga golongan metode. Pengolahan citra tradisional memakai ciri warna, bentuk, dan tekstur dengan akurasi berturut-turut 80–85%, 80–87%, dan 75–90%, serta mudah terganggu cahaya dan naungan. Segmentasi berbasis pembelajaran mesin memakai ambang batas, K-means, pertumbuhan wilayah, SVM, Bayes, dan Random Forest; akurasi yang dikutip meliputi Bayes 81%, SVM 90–93%, KNN 90%, K-means 90%, dan Random Forest 96%. Metode pembelajaran mendalam memakai Faster R-CNN, Mask R-CNN, SSD, dan YOLO; akurasi yang dikutip meliputi jaringan residual 85–87%, Mask R-CNN 89%, SSD 90%, dan YOLO 89–95%. Contoh spesifik mencakup Mask R-CNN dengan ResNet-50 dan FPN untuk stroberi berakurasi rata-rata 95,78% pada 100 citra uji, SSD berbasis ResNet-101 sebesar 89,53%, YOLOv3 apel dengan waktu 19 ms per apel disertai salah kenal 7,8% dan terlewat 9,2%, serta I-Yolov8 yang menaikkan akurasi 16,33% saat cerah dan 14,63% saat mendung dibandingkan YOLOv8. Untuk penentuan posisi, stereo, RGB-D, dan laser dipakai dengan tantangan berupa angin, getaran mesin, dan buah yang bertumpang tindih; salah satu metode pencocokan citra apel menurunkan galat koordinat 3D menjadi kurang dari 10 mm. Seluruh angka berasal dari tabel dan kajian yang dikutip tinjauan ini, bukan dihitung ulang.

Ujung efektor dikelompokkan menjadi tiga jenis, yaitu penjepit, hisap, dan pisau potong. Penjepit paling luas pemakaiannya karena dapat menyesuaikan berbagai bentuk dan ukuran, tetapi banyak sendi dan sensor menaikkan biaya serta dapat merusak buah lunak pada kecepatan tinggi. Ujung hisap memakai tekanan negatif sehingga mengurangi kontak fisik, namun kurang cocok untuk permukaan tidak beraturan; pada 400 uji coba jamur cokelat, metode ini mencapai tingkat keberhasilan 90,5% dengan kerusakan buah 6%. Pisau potong cocok untuk tangkai keras seperti anggur, kesemek, dan leci, tetapi menuntut akurasi penentuan posisi lebih tinggi; pada buah naga, tekanan udara 0,5 MPa memberi tingkat keberhasilan 90% dengan waktu 0,46 s per buah, sedangkan alat pemanen leci memotong tangkai berdiameter 3–7 mm dalam waktu rata-rata 2 s. Tabel tinjauan mencatat tingkat keberhasilan sejumlah robot, misalnya apel 77% dan 84%, kiwi 51%, paprika manis 61%, serta jamur 86,8%.

Penulis menyatakan sejumlah kekurangan. Tingkat pengenalan masih rendah karena cahaya, bayang, pantulan, latar yang kompleks, serta buah yang tertutup daun atau saling bertumpang. Akurasi penentuan posisi terganggu oleh galat deteksi, getaran mekanis, pengukur jarak yang tidak tepat, dan buah yang berayun karena angin. Kerusakan buah dapat terjadi karena kontak yang tidak diinginkan dan kesulitan mengatur gaya cengkeram. Efisiensi dan kecepatan robot masih jauh di bawah manusia, apalagi pada penanaman rapat, sementara baterai membatasi daya tahan operasi dan komponen mudah aus. Biaya pengadaan serta pemeliharaan menjadi hambatan utama komersialisasi. Arah pengembangan yang diusulkan adalah pengoptimalan algoritma pengenalan yang ringan dan adaptif, penataan kebun dengan jarak dan pola tanam teratur, penghitungan kelayakan biaya dibanding tenaga kerja, peningkatan daya tahan terhadap cuaca serta keragaman fungsi, dan integrasi teknologi seperti drone dan 5G.

