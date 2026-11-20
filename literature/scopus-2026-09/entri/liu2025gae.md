# GAE-YOLO: a lightweight multimodal detection framework for tomato smart agriculture with edge computing

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2025gae` |
| Judul asli | GAE-YOLO: a lightweight multimodal detection framework for tomato smart agriculture with edge computing |
| Penulis | Liu, Xiaoke; Teng, Wenjie; Yu, Haoran; Yao, Zhuoyi; Wang, Chengzhen; Peng, Yuzhong; Han, Xiaoqing; Liu, Jianming |
| Tahun | 2025 |
| Venue | Frontiers in Plant Science |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [liu2025gae.pdf](../pdf/liu2025gae.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2025.1712432

## Gambaran Umum

Kajian ini mengusulkan GAE-YOLO, sebuah kerangka deteksi multimodal ringan untuk pengelolaan tanaman tomat berbasis *edge computing*. Penulis menyoroti tiga persoalan pada produksi tomat konvensional: panen yang tidak efisien karena masih bergantung pada tenaga manusia, pengendalian hama dan penyakit yang kurang tepat karena pemeriksaan lapangan manual lambat dan sering salah identifikasi, serta keterbatasan pengetahuan budidaya di wilayah yang kekurangan tenaga teknis. Penulis berargumen bahwa model *deep learning* yang sudah ada umumnya berat secara komputasi, kurang mampu bekerja secara *real-time*, dan kurang baik dalam mengoordinasikan beberapa tugas sekaligus.

Data dihimpun dari dua sumber. Sumber pertama adalah 895 citra tomat beresolusi tinggi dari Kaggle yang dianotasi dalam format PASCAL VOC. Sumber kedua adalah data lapangan dari rumah kaca di Shouguang, Provinsi Shandong, yang direkam dengan kamera binokular ZED pada berbagai tahap pertumbuhan, kondisi pencahayaan, dan sudut pandang. Untuk deteksi penyakit daun, penulis memakai lebih dari 700 citra daun tomat dari Kaggle dengan enam kategori penyakit dan satu kelas sehat, yaitu *bacterial spot*, *early blight*, *late blight*, *leaf mold*, *target spot*, dan *black spot*. Citra daun tersebut diperkaya dengan pembalikan, koreksi gamma, injeksi derau, augmentasi warna PCA, rotasi, dan penskalaan. Perangkat keras yang digunakan terdiri atas kamera ZED, platform roda omnidireksional, dan modul komputasi tepi Jetson TX2.

Metode utamanya mengganti sebagian konvolusi standar dengan modul *Ghost Convolution* (GhostConv) agar model lebih ringan, lalu menambahkan fungsi aktivasi AReLU dan fungsi kerugian *Effective Intersection over Union* (E-IoU) untuk meningkatkan akurasi. Pada Jetson TX2, sistem mencapai *mean Average Precision* pada ambang IoU 50 persen (mAP@50) sebesar 93,5 persen dengan kecepatan 10,2 *frame* per detik (FPS). Abstrak menyebut angka ini, sedangkan bagian simpulan menulis 93,3 persen mAP@50, sehingga terdapat ketidakkonsistenan kecil dalam naskah. Dengan optimasi *TensorRT* dan resolusi 720p, kecepatan dapat ditingkatkan hingga 27 FPS. Dalam tinjauan perbandingan arsitektur ringan, penulis melaporkan bahwa GhostNet sekitar 0,5 persen lebih akurat pada top-1 dibandingkan MobileNetV3 dengan latensi yang setara. Sistem tersebut juga memuat modul penilaian kematangan dan prediksi hasil per tanaman, modul diagnosis penyakit, dan konsultasi berbasis model bahasa besar untuk pertanian.

Penulis menyatakan dua batasan secara eksplisit. Pertama, ukuran dataset yang terbatas membuat model hanya terpapar sebagian kecil variasi lingkungan pertanian yang sebenarnya. Akibatnya, kinerja model dapat menurun pada kondisi yang tidak terwakili dalam data latih, misalnya manifestasi penyakit yang belum pernah terlihat, cekaman abiotik yang ekstrem, atau karakteristik kultivar yang unik. Kedua, penulis mengakui bahwa mencapai generalisasi yang kokoh tetap menjadi tantangan terbuka di bidang pertanian. Penulis mengurangi risiko *overfitting* melalui regularisasi dan augmentasi data, tetapi tidak menguji secara lebih luas di luar kondisi rumah kaca yang dipelajari.
