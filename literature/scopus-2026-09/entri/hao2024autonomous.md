# AUTONOMOUS HARVESTING ROBOT FOR OIL PALM PLANTATION: A REVIEW

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hao2024autonomous` |
| Judul asli | AUTONOMOUS HARVESTING ROBOT FOR OIL PALM PLANTATION: A REVIEW |
| Penulis | Hao, Teoh Kean |
| Tahun | 2024 |
| Venue | Journal of Oil Palm Research |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [hao2024autonomous.pdf](../pdf/hao2024autonomous.pdf)
- DOI resmi: https://doi.org/10.21894/jopr.2024.0008

## Gambaran Umum

Tinjauan ini merespons krisis tenaga kerja pada perkebunan kelapa sawit Malaysia. Kekurangan 28.940 pekerja pada 2022, dengan pekerja asing lebih dari 75% dari total tenaga kerja, menyebabkan tandan buah segar (FFB) senilai RM10,46 miliar tidak terpanen pada Januari hingga Mei 2022. Pekerjaan panen tergolong kotor, sulit, berbahaya, dan rendah martabat (4-D); 88% pekerja panen mengalami gangguan muskuloskeletal pada 2020. Pohon sawit tua dapat mencapai 20,0 m, sementara medan perkebunan beragam, mulai dari datar, perbukitan, gambut, hingga pasir, sehingga pemanenan manual masih dianggap paling efektif. Penulis mengusulkan robot pemanen otonom dan meninjau enam teknologi kunci: deteksi kematangan, mekanisme pemotongan, mekanisme pemanjatan, perencanaan lintasan manipulator, lokalisasi, serta navigasi dan penghindaran rintangan.

Sebagai latar, tinjauan ini membandingkan tiga tahapan teknologi panen. Pahat dipakai untuk pohon di bawah 3 m dan sabit dengan galah panjang untuk pohon lebih tinggi. Alat semi-mekanis Cantas dari Malaysian Palm Oil Board menjangkau 4,5-6,0 m, memotong 37% lebih cepat, dan menaikkan produktivitas dari 4,19 menjadi 11,60 t FFB/hari, tetapi masih memerlukan operator dan menimbulkan getaran yang berisiko menyebabkan Hand-Arm Vibration Syndrome. Mesin mekanis penuh memakai boom berdaya 31,5 hp dengan muatan 500 kg dan mencapai 4-6 t FFB/hari, namun ukurannya menyulitkan akses pada medan sempit, berat 10-30 t sehingga memadatkan tanah, dan jangkauannya terbatas. Robot pemanjat dapat mencapai puncak pohon tanpa batas tinggi, tetapi mekanisme yang ada baru cocok untuk batang berpermukaan halus dan berdiameter seragam, sedangkan batang sawit penuh sisa pelepah dan berdiameter beragam.

Pada deteksi kematangan, tandan dibedakan menjadi lima kelas, yaitu belum matang, hampir matang, matang, terlalu matang, dan busuk; kandungan minyak tertinggi ada pada tahap matang. Spektroskopi Raman dengan klasifier fine k-nearest neighbours (KNN) mencapai akurasi 100%, tetapi pengujiannya dilakukan di lingkungan terkendali dan sampel buah harus diiris, sehingga tidak praktis di lapang. Analisis citra dengan fitur warna dan bag of visual words (BOVW) memakai segmentasi K-means, fitur hue, speeded up robust features (SURF), dan support vector machine (SVM), menghasilkan akurasi rata-rata 57% dan 70%; Model ResAtt DenseNet dengan mekanisme residual attention dan Ten Crop mencapai skor F1 0,6929, lebih baik tetapi lebih berat secara komputasi. Sensor induktif dengan discriminant analysis mencapai akurasi 100% dan RMSE 13,45 hari untuk memperkirakan umur kematangan, namun harus menyentuh buah. Sensor optik berbasis LED dan spektrometer menghasilkan akurasi 63% dengan Lazy KStar serta 88,2% dengan KNN dan discriminant analysis bila acuannya kandungan minyak, tetapi hasilnya dipengaruhi cahaya luar. Untuk teknologi lain, lokalisasi memakai GNSS, odometri, dan estimasi pose visual dengan galat rata-rata 0,2865 m atau RFID dengan presisi 5,9 cm dan akurasi orientasi 2,1°; navigasi memakai pencarian lintasan, algoritma Hybrid PSO-MFB, convolutional neural network (CNN), serta deep reinforcement learning berbasis duelling deep Q-network.

Penulis menyatakan sejumlah batasan dan syarat penerapan. Mekanisme pemanjat yang ada belum tangguh untuk batang sawit yang tidak beraturan, teknik lokalisasi dari wilayah perkotaan, UAV, atau kapal perlu disesuaikan sebelum dipakai di perkebunan, dan modul robot yang dapat mendeteksi sekaligus memanen tandan secara otonom belum tersedia. Klasifikasi kematangan di lapang masih mengandalkan penilaian manusia yang tidak konsisten, sementara metode berbasis citra sensitif terhadap cahaya sekitar dan metode deep learning sulit diterapkan pada perangkat berdaya rendah. Navigasi berbasis pembelajaran hanya bekerja pada lingkungan yang dikenal dan mudah mengalami overfitting saat dipindah dari simulasi ke lapang. Tinjauan ini menyimpulkan bahwa keenam teknologi belum terintegrasi menjadi sistem lengkap; penulis menganjurkan penggunaan Robot Operating System (ROS) sebagai perantara, kombinasi beberapa teknik lokalisasi, serta navigasi hibrida karena pohon sawit ditanam dalam pola kisi.
