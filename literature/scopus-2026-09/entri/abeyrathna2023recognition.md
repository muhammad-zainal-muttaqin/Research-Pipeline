# Recognition and Counting of Apples in a Dynamic State Using a 3D Camera and Deep Learning Algorithms for Robotic Harvesting Systems

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `abeyrathna2023recognition` |
| Judul asli | Recognition and Counting of Apples in a Dynamic State Using a 3D Camera and Deep Learning Algorithms for Robotic Harvesting Systems |
| Penulis | Abeyrathna, R. M. Rasika D.; Nakaguchi, Victor Massaki; Minn, Arkar; Ahamed, Tofael |
| Tahun | 2023 |
| Venue | Sensors |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [abeyrathna2023recognition.pdf](../pdf/abeyrathna2023recognition.pdf)
- DOI resmi: https://doi.org/10.3390/s23083810

## Gambaran Umum
Makalah ini mengembangkan sistem pengenalan, pelacakan, dan pencacahan apel dari kamera RGB-D yang dipasang pada kendaraan bergerak, dengan tujuan mendukung lengan robot pemanen. Detektor satu tahap (*one-stage detector*) YOLOv4, YOLOv5, YOLOv7, dan EfficientDet dilatih pada citra apel hasil augmentasi, lalu dijalankan bersama algoritma pelacakan Deep SORT pada kamera Realsense D455. Sistem diuji pada pohon apel tiruan (*artificial trees*) yang ditata sebagai kebun berstruktur khusus, pada tiga sudut kamera (90° atau tegak lurus, 15°, dan 30°) dan tiga kecepatan maju kendaraan (0,052 m/s, 0,069 m/s, dan 0,098 m/s).

Data latih berasal dari video apel di kebun penelitian di Prefektur Aomori, Jepang, sedangkan uji dinamis dilakukan di Universitas Tsukuba dengan 30 apel nyata yang ditempelkan pada 10 pohon tiruan. Nilai mAP@0,5 pada data uji adalah 0,84 (YOLOv4), 0,861 (YOLOv5), 0,905 (YOLOv7), dan 0,775 (EfficientDet). Galat akar rerata kuadrat (*root mean square error*, RMSE) jarak terendah, 1,54 cm, dicapai EfficientDet pada sudut 15° dan kecepatan 0,098 m/s.

Untuk pencacahan, YOLOv5 dan YOLOv7 menghasilkan jumlah deteksi tertinggi dengan akurasi hitung maksimum 86,6%. Penulis menyimpulkan bahwa EfficientDet pada sudut 15° layak dipakai untuk pengembangan lengan robot lebih lanjut.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pemanenan apel bergantung pada tenaga kerja musiman yang terampil, sehingga robot pemanen dipandang sebagai solusi. Namun, bentuk kebun konvensional yang tidak beraturan, kanopi padat, oklusi oleh daun dan cabang, serta variasi cahaya menyulitkan sistem penglihatan memberikan posisi apel yang tepat. Lokalisasi yang salah dapat merusak apel maupun manipulator, karena lintasan penghindar tabrakan dan arah genggam dihitung setelah lokalisasi.

Penulis berargumen bahwa kebun yang dirancang khusus (misalnya tipe *tall spindle* atau V-shape) dapat membantu pengenalan dan pencacahan. Penulis juga menyebut bahwa galat hitung memengaruhi estimasi hasil panen. Studi terdahulu yang dikutip mencakup deteksi apel dengan fitur tekstur citra multispektral, lokalisasi dengan RANSAC, serta penghitungan apel pada dinding buah vertikal dengan pelacakan batang pohon (mAP@0,5 batang 99,35% dan akurasi hitung 91,49% menurut makalah yang dikutip). Tujuan makalah ini adalah membangun sistem pengenalan dan pencacahan apel berbasis pembelajaran mendalam dengan kamera RGB-D D455 pada data kebun yang dirancang khusus.

## Ide Utama
Gagasan utama adalah memadukan detektor satu tahap dengan pelacakan Deep SORT agar setiap apel yang bergerak melintasi bingkai video mendapat identitas tunggal, lalu menghitungnya sekali ketika apel melewati garis acuan vertikal di tengah bingkai. Pada saat yang sama, tengah kotak pembatas apel dipetakan ke aliran *depth* yang telah disejajarkan dengan RGB sehingga koordinat 3D apel diperoleh. Dengan cara ini, pencacahan dan lokalisasi 3D dikerjakan oleh satu alur.

Kontribusi yang dinyatakan penulis ada dua. Pertama, kombinasi detektor mutakhir dan Deep SORT pada tiga kecepatan dan tiga orientasi kamera untuk mencari orientasi optimal bagi pencengkeraman. Kedua, pemakaian aliran *depth* yang ditumpangkan pada RGB untuk membandingkan akurasi nilai kedalaman pada kondisi dinamis dan memilih model yang paling cocok untuk lengan robot.

## Cara Kerja Langkah demi Langkah
```
 Video GoPro --> bingkai --> augmentasi --> anotasi YOLO --> latih 4 detektor
                                                                   |
 Realsense D455 (RGB + depth selaras) --> detektor --> Deep SORT --+
                                                                   v
                       garis ROI di tengah bingkai --> hitung + koordinat 3D
```

### 1. Akuisisi data latih
Video direkam dengan GoPro Hero 10 beresolusi 3840 × 2160 piksel pada 27 dan 28 September 2022 di institut penelitian apel di Kuroishi, Prefektur Aomori, pada pagi, siang, dan sore hari. Kamera berada pada ketinggian 1 sampai 1,5 m dari tanah dan berjarak 1 sampai 2 m dari pohon. Kultivar apel tidak dilaporkan.

### 2. Penyiapan dan augmentasi citra
Video diubah menjadi citra yang dipotong. Citra dirotasi 180°, 90° searah jarum jam, dan 90° berlawanan arah jarum jam, kemudian semua citra diubah menjadi skala abu-abu. Jumlah citra asli 800 menjadi 6.511 setelah augmentasi. Anotasi memakai program Python buatan sendiri dengan format YOLO. Pembagian data: 4.500 citra latih, 1.500 validasi, dan 511 uji. Detektor hanya memiliki satu kelas, yaitu apel.

### 3. Detektor yang dilatih
YOLOv4 dilatih pada kerangka Darknet (CSPDarknet-53, 12.000 iterasi *batch*, 72 jam). YOLOv5s dilatih pada PyTorch di Google Colab selama 50 epoch (4,57 jam). YOLOv7 dilatih 20 epoch di Colab (2,549 jam). EfficientDet dilatih pada TensorFlow di komputer lokal dengan ukuran masukan 512 × 512 selama 60.000 langkah. Seluruh model memakai himpunan data yang sama.

### 4. Lokalisasi 3D dinamis
Pusat geometri kotak pembatas dihitung dari koordinat sudut kiri atas dan ukuran kotak. Koordinat piksel diselaraskan dengan aliran *depth*, lalu koordinat kamera $X_a$, $Y_a$, dan $Z_a$ dihitung dengan model kamera lubang jarum (*pinhole*) memakai parameter intrinsik dari SDK Realsense. Ukuran bingkai kamera 3D diatur 1280 × 720 piksel.

### 5. Pelacakan dan pencacahan
Deep SORT dipakai sebagai perluasan SORT: filter Kalman dengan model kecepatan konstan, algoritma Hungarian untuk asosiasi data dengan ambang IoU 50%, dan CNN MobileNetV2 untuk fitur penampakan guna mempertahankan identitas apel saat terjadi oklusi. Apel dihitung setelah melewati garis vertikal pada 50% bingkai.

### 6. Rancangan uji lapangan
Uji dilakukan di Tsukuba-Plant Innovation Research Center. Kamera dipasang di bagian belakang traktor roda empat Kubota KL21. Sebanyak 30 apel nyata dipasang pada 10 pohon tiruan dengan jarak antarbaris 80 cm, dan traktor dijalankan 1 m sejajar pohon. Sudut kamera adalah 0° (tegak lurus baris), 15°, dan 30°, dengan tiga kecepatan sesuai gigi 3, 5, dan 6 pada putaran mesin 1000 rpm. Jarak acuan diukur manual dengan pita ukur untuk 30 apel, tiga kali dari tiga sudut. Perangkat komputasi: GPU NVIDIA GTX 1650 4 GB, RAM 32 GB.

## Eksperimen dan Hasil
Evaluasi pelatihan memakai presisi, *recall*, F1, dan mAP@0,5 (mengikuti PASCAL VOC). Evaluasi dinamis memakai RMSE jarak terhadap pengukuran pita dan jumlah apel terdeteksi dari 30 apel.

| Model | Presisi | Recall | F1 | mAP@0,5 |
|---|---|---|---|---|
| YOLOv4 | 0,840 | 0,790 | 0,810 | 0,840 |
| YOLOv5 | 0,874 | 0,783 | 0,830 | 0,861 |
| YOLOv7 | 0,892 | 0,828 | 0,860 | 0,905 |
| EfficientDet | 0,950 | 0,950 | tidak dilaporkan | 0,775 |

Pada uji dinamis, EfficientDet pada orientasi 15° dan kecepatan 0,098 m/s memberi jarak paling akurat (RMSE 1,54 cm). Penulis menyatakan bahwa EfficientDet memiliki RMSE kurang dari 3 cm pada ketiga orientasi dan ketiga kecepatan, sedangkan YOLOv4 paling tidak akurat saat kamera tegak lurus. Untuk pencacahan, YOLOv5 dan YOLOv7 menghasilkan deteksi terbanyak dari 30 apel, dengan akurasi hitung maksimum 86,6%. Nilai RMSE dan jumlah deteksi untuk tiap kombinasi sudut dan kecepatan hanya tersaji dalam grafik (Gambar 19 dan 20) yang tidak terbaca dari teks ekstraksi.

## Kelebihan dan Keterbatasan
Penulis menyatakan bahwa oklusi oleh daun, variasi cahaya, bayangan, dan gerakan daun akibat angin menyebabkan deteksi yang terlewat serta galat nilai kedalaman. Penulis menyarankan penerangan tambahan, dua kamera (satu di dasar manipulator dan satu dekat penjepit), sensor kedalaman tambahan, dan deteksi ulang apel yang sama saat manipulator berada di tengah siklus geraknya. Penulis juga menyebut bahwa data tidak dibuka bebas (tersedia atas permintaan dengan pembatasan).

Menurut pembacaan ringkasan ini, uji dinamis hanya memakai 30 apel pada pohon tiruan yang disusun khusus sehingga tidak mewakili kebun nyata, dan akurasi hitung 86,6% hanya didasarkan pada satu skenario berukuran kecil. Perbandingan antardetektor juga tidak seimbang: kerangka, jumlah epoch, dan ukuran masukan berbeda antarmodel, serta tidak ada ulangan atau selang kepercayaan yang dilaporkan. Data latih berupa citra skala abu-abu dari video yang berbeda dari kamera uji (GoPro versus Realsense). Pernyataan bahwa EfficientDet paling cocok didasarkan pada RMSE jarak, padahal mAP@0,5 model itu terendah.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai dengan mekanisme pelacakan video: detektor lalu Deep SORT (filter Kalman, asosiasi IoU Hungarian, dan penanda penampakan MobileNetV2), serta penghitungan sekali saat apel melewati garis vertikal di tengah bingkai. Identitas dipertahankan dalam satu lintasan video menyamping; makalah tidak menangani pencocokan apel yang sama antara lintasan atau sisi pohon yang berbeda. Hitungan tidak dilaporkan per kelas karena hanya ada satu kelas (apel). Acuan hitung adalah jumlah apel nyata yang dipasang pada pohon tiruan (30 apel), yang diketahui oleh penulis, bukan hasil panen atau hitung lapangan pada kebun nyata.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola detektor, pelacak, lalu garis hitung; temuan bahwa sudut kamera memengaruhi galat kedalaman; serta pemakaian *depth* terselaras untuk koordinat 3D. Makalah tidak membahas penggabungan identitas lintas sisi pohon, sehingga bagian itu tidak dapat diambil darinya.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `abeyrathna2023recognition`.

Ringkasan yang aman dikutip: Abeyrathna dkk. (2023) membandingkan YOLOv4, YOLOv5, YOLOv7, dan EfficientDet yang dikombinasikan dengan pelacak Deep SORT dan kamera RGB-D Realsense D455 untuk mengenali, menghitung, dan melokalisasi apel dari kendaraan bergerak pada pohon apel tiruan. mAP@0,5 pelatihan adalah 0,84, 0,861, 0,905, dan 0,775; RMSE jarak terendah 1,54 cm dicapai EfficientDet pada sudut 15° dan kecepatan 0,098 m/s, sedangkan akurasi hitung maksimum 86,6% dicapai YOLOv5 dan YOLOv7.

Catatan verifikasi data: nilai mAP@0,5 dan presisi, recall, serta F1 terdapat pada Tabel 1; nilai mAP juga tertulis di Abstrak dan Bagian 4.1. RMSE 1,54 cm dan akurasi hitung 86,6% tertulis di Abstrak dan Bagian 5. Jumlah citra (800, 6.511; pembagian 4.500, 1.500, 511) tertulis di Bagian 3.2. Nilai RMSE per kombinasi sudut dan kecepatan serta jumlah apel terdeteksi per model hanya tersaji pada Gambar 19, 20, dan A1 yang tidak terbaca dalam teks ekstraksi, sehingga tidak dikutip. Jumlah apel yang setara dengan 86,6% tidak dinyatakan dalam teks. F1 EfficientDet tidak dilaporkan pada Tabel 1.
