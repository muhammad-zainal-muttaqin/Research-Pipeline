# NDMFCS: An automatic fruit counting system in modern apple orchard using abatement of abnormal fruit detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wu2023ndmfcs` |
| Judul asli | NDMFCS: An automatic fruit counting system in modern apple orchard using abatement of abnormal fruit detection |
| Penulis | Wu, Zhenchao; Sun, Xiaoming; Jiang, Hanhui; Mao, Wulan; Li, Rui; Andriyanov, Nikita; Soloviev, Vladimir; Fu, Longsheng |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [wu2023ndmfcs.pdf](../pdf/wu2023ndmfcs.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.108036

## Gambaran Umum

Pencacahan buah apel di kebun modern penting bagi petani untuk memperkirakan hasil panen dan mengatur kebun. Banyak sistem pencacahan berbasis video memakai algoritme deteksi buah berbasis pembelajaran mendalam. Namun, algoritme ini sering ikut mendeteksi buah yang bukan target, yaitu buah di baris belakang pohon dan buah yang jatuh di tanah. Kedua jenis deteksi itu membuat jumlah hitungan lebih besar daripada jumlah sebenarnya. Penulis mengusulkan sistem bernama NDMFCS (*Normal Detection Matched Fruit Counting System*) untuk mengurangi masalah tersebut dan meningkatkan akurasi pencacahan buah apel.

Penelitian dilakukan di kebun apel varietas 'Fuji' dengan tanaman kerdil di Famen, Baoji, Provinsi Shaanxi, Tiongkok. Jarak antartanaman 1,5 m dan jarak antarbaris 4,0 m. Sensor yang dipakai adalah kamera Intel RealSense D435 yang dipasang pada kendaraan kendali jarak jauh. Kamera berada sekitar 1,4 m di atas tanah dan berjarak 2,0 m dari baris pohon. Kendaraan bergerak sekitar 1,0 m/s di sepanjang baris. Data terdiri atas 1.600 citra asli dan 10 set video asli (V1 sampai V10) berukuran 720 × 1280 piksel, yang direkam pada musim panen 2020 dan 2021. Setiap set video memiliki video RGB dan video kedalaman (*depth*) yang sudah diselaraskan. Citra dibagi acak menjadi 1.280 citra latih (80 persen) dan 320 citra uji (20 persen). Setiap buah dan batang diberi label kotak pembatas (*bounding box*), dengan total 93.050 label, yang terdiri atas 90.798 label buah dan 2.252 label batang. Data latih kemudian diperluas dengan augmentasi menjadi 11.520 citra. Kinerja sistem diuji pada 10 set video.

Sistem terdiri atas tiga bagian. Pertama, YOLOv4-tiny mendeteksi buah dan batang pada setiap bingkai video RGB, lalu menghasilkan tingkat keyakinan dan koordinat piksel setiap objek. Kedua, buah di baris belakang dibuang bila jaraknya dari kamera lebih jauh daripada ambang jarak yang diambil dari peta kedalaman. Buah di tanah dibuang bila tingkat keyakinan deteksinya berada di bawah ambang keyakinan. Ketiga, pencacahan dilakukan dengan pelacakan batang dan penugasan ID. Setiap buah memperoleh ID pelacakan yang unik, dan buah yang sama pada bingkai berurutan tidak dihitung dua kali.

Pada 10 set video, rata-rata presisi deteksi buah naik dari 89,1 persen menjadi 93,3 persen setelah penghapusan deteksi abnormal. Rata-rata *Multiple Object Tracking Accuracy* naik 4,2 persen, dan rata-rata *Multiple Object Tracking Precision* naik 3,3 persen. Rata-rata *ID Switch Rate* turun 1,1 persen. Akurasi pencacahan buah rata-rata naik menjadi 95,0 persen, atau naik 4,2 persen. Koefisien determinasi (R2) sebesar 0,97 menunjukkan bahwa jumlah buah yang dihitung sistem mendekati jumlah sebenarnya.

Penulis menyimpulkan bahwa penghapusan deteksi abnormal meningkatkan kinerja deteksi, pelacakan, dan pencacahan buah. Penulis juga menyatakan bahwa buah di baris belakang menurunkan kinerja pelacakan, sedangkan buah di baris belakang dan buah di tanah sama-sama menurunkan kinerja pencacahan. Batasan utama terletak pada perangkat keras. NDMFCS dikembangkan dengan kamera Intel RealSense D435 dan memerlukan perangkat komputasi, sehingga sulit digunakan secara luas. Penulis menyarankan pengembangan sistem serupa berbasis video dari ponsel pintar yang memiliki kamera RGB beresolusi tinggi dan *system on chip*.
