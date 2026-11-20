# Unified Color Space Segmentation and Yolov5 Approach for Nutmeg Ripeness Detection and Quantity Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shrinivasacharya2026unified` |
| Judul asli | Unified Color Space Segmentation and Yolov5 Approach for Nutmeg Ripeness Detection and Quantity Estimation |
| Penulis | Shrinivasacharya, P.; others |
| Tahun | 2026 |
| Venue | 17th International Conference on Advances in Computing Control and Telecommunication Technologies Act 2026 |
| Kode | C4 (Atribut kelas dan pencacahan) |

## Tautan Akses
- PDF: [shrinivasacharya2026unified.pdf](../pdf/shrinivasacharya2026unified.pdf)

## Gambaran Umum

Penentuan tingkat kematangan dan estimasi hasil panen buah pala (*nutmeg*) selama ini dilakukan secara manual. Cara tersebut lambat, bergantung pada penilaian pengamat, dan hasilnya sering tidak konsisten. Penulis menyatakan bahwa kondisi ini menurunkan mutu dan menambah kehilangan pascapanen. Karena itu, penelitian ini mengusulkan sistem otomatis yang memadukan segmentasi ruang warna dengan model deteksi *YOLOv5*. Tujuannya adalah mengenali tiga tingkat kematangan buah sekaligus menghitung jumlah buah dalam citra secara *real-time*.

Objek penelitian adalah buah pala pada tanaman di kebun. Citra diambil dengan kamera diam dan *Unmanned Aerial Vehicle* (UAV) dari berbagai sudut pandang dan kondisi pencahayaan. Citra berwarna RGB kemudian diubah ke ruang warna HSV dan LAB. Anotasi dibuat dengan format YOLO yang berisi *bounding box* dan tiga kelas, yaitu tidak matang, setengah matang, dan matang. Data diperkaya dengan rotasi acak, pembalikan horizontal dan vertikal, serta penyesuaian kecerahan dan kontras. Pembagian data adalah 70% untuk latih, 20% untuk validasi, dan 10% untuk uji. Model dilatih dengan GPU seri NVIDIA RTX. Teks tidak mencantumkan jumlah citra atau jumlah buah dalam set data.

Model dilatih dengan *transfer learning* dari bobot *YOLOv5* pra-latih. Pada tahap praproses, citra diubah ke HSV, diratakan histogramnya, dan diberi filter Gaussian. Ambang warna kemudian membentuk *mask* untuk memisahkan buah dari latar. Hasil deteksi disaring dengan *non-maximum suppression* dan aturan ukuran serta bentuk untuk membuang *false positive*. Pada Tabel I, akurasi deteksi keseluruhan mencapai 98,5%, presisi 97,8%, recall 99,2%, dan *mean average precision* 98,7%. Pada Tabel II, akurasi deteksi dan klasifikasi per kelas adalah 97,5% dan 96,8% untuk tidak matang, 98,2% dan 97,6% untuk setengah matang, serta 99,1% dan 98,9% untuk matang. Pada Tabel III, *Mean Absolute Error* (MAE) penghitungan adalah 1,2 buah per citra dengan akurasi penghitungan 97,4%. Sistem mencapai 25 *frames per second* pada RTX 3080 lokal dan 20 *frames per second* pada Tesla T4 di cloud, dengan latensi 200 ms per citra. Abstrak dan kesimpulan melaporkan akurasi 95%, presisi 94%, dan recall 90%. Tabel IV menunjukkan akurasi klasifikasi SVM 80%, RF 85%, CNN 90%, dan YOLOv5 95%.

Penulis menyatakan bahwa penanganan buah yang saling tumpang tindih masih perlu ditingkatkan. Kondisi pencahayaan yang bervariasi, objek yang bertumpuk, dan latar belakang yang beragam juga disebut sebagai tantangan yang perlu diatasi melalui praproses dan augmentasi data yang lebih baik. Penulis juga menyebutkan bahwa teknik model pembelajaran mendalam yang lebih mutakhir dapat dieksplorasi untuk ekstraksi fitur. Sistem masih perlu dioptimalkan untuk penerapan *real-time* berskala besar.
