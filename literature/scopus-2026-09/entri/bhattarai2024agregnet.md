# AgRegNet: A deep regression network for flower and fruit density estimation, localization, and counting in orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bhattarai2024agregnet` |
| Judul asli | AgRegNet: A deep regression network for flower and fruit density estimation, localization, and counting in orchards |
| Penulis | Bhattarai, Uddhav; Bhusal, Santosh; Zhang, Qin; Karkee, Manoj |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [bhattarai2024agregnet.pdf](../pdf/bhattarai2024agregnet.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.109534

## Gambaran Umum

Kajian ini bertujuan mengestimasi kepadatan, jumlah, dan lokasi bunga serta buah pada kanopi pohon buah tanpa deteksi objek eksplisit. Latar belakangnya adalah ketidakpastian tenaga kerja manual dan biayanya, yang mendorong otomatisasi estimasi hasil, pengelolaan beban tanaman, dan penipisan bunga atau buah muda. Pendekatan berbasis deteksi menjadi tidak praktis ketika objek berjumlah banyak, berukuran kecil, dan saling menutupi, seperti bunga apel pada fase penuh mekar. Penulis mengusulkan AgRegNet, jaringan regresi berbasis anotasi titik yang lebih sederhana dan ringan daripada deteksi dengan kotak pembatas atau poligon.

Data terdiri atas dua himpunan apel. Himpunan bunga berisi 325 citra dari tiga kebun komersial di Washington, Amerika Serikat, yang dikumpulkan pada musim tanam 2018 dan 2019 dengan sensor ZED2, Kinect V2 (1920×1080), dan Sony RX100 (5472×3648). Varietasnya adalah Scifresh (dinding buah vertikal), Envi, dan HoneyCrisp (keduanya teralis V), dengan 43.031 objek, kisaran 4–434 objek per citra, dan rata-rata 132. Himpunan buah berasal dari data publik Gao dkk., setelah penghapusan citra kembar dengan SSIM lebih dari 95 persen menjadi 630 citra unik dari sensor Kinect V2 (1920×1080), memuat 34.404 objek, kisaran 10–121, dan rata-rata 55. Setiap himpunan dibagi menjadi 75 persen latih dan 25 persen uji; himpunan validasi diperoleh dengan memotong citra uji secara acak. Pelatihan memakai Adam dengan laju pembelajaran 0,0004, peluruhan 0,995 per epoch, hingga 200 epoch pada dua GPU NVIDIA Titan X 12 GB, dengan citra latih dan uji diubah ke 1024×768 serta potongan validasi 768×576.

Mekanisme inti adalah regresi peta kepadatan. Anotasi titik berupa titik pusat (centroid) setiap bunga atau buah diubah menjadi peta kepadatan melalui konvolusi kernel Gauss dengan simpangan batas adaptif yang dihitung dengan KNN, yaitu 15 persen jarak tetangga terdekat untuk bunga dan 25 persen untuk buah. Peta segmentasi dibentuk dengan elemen struktur cakram berjari-jari 2σ dan berfungsi sebagai gerbang penyaring fitur latar. Arsitektur AgRegNet berbentuk U dengan encoder ConvNeXt-T yang dimodifikasi, koneksi skip, modul perhatian CBAM pada ranah spasial dan kanal, serta cabang segmentasi. Jumlah parameter yang dilatih 9,45 juta, lebih kecil daripada 29 juta pada ConvNeXt-T awal. Jumlah objek dihitung dari jumlah intensitas piksel peta kepadatan. Lokasi diperkirakan dengan mencari puncak lokal (peak local max, jarak minimum 2 piksel) lalu mencocokkan puncak hasil prediksi dan acuan satu-satu menggunakan algoritme Hungarian dengan jarak Euclidean sebagai biaya. Metrik mAP dan mAR dihitung dengan ambang jarak T dari σf hingga 2,2σf, yang berperan seperti ambang IoU pada deteksi.

Pada data bunga, AgRegNet menghasilkan SSIM 0,938, PSNR 31,2, MAE 18,1, RMSE 23,8, dan pMAE 13,7 persen. Pada data buah, nilainya berturut-turut 0,910, 24,1, 3,1, 4,0, dan 5,6 persen. Pelokalan memberi mAP 0,81 dan mAR 0,79 untuk bunga serta 0,93 dan 0,89 untuk buah. Waktu inferensi 14,2 ms, lebih singkat daripada 238 ms pada Mask R-CNN yang dipakai untuk deteksi dan segmentasi gugus bunga dalam sistem yang sama. Uji ablasi menunjukkan penambahan cabang segmentasi menurunkan MAE dan RMSE masing-masing 27,1 persen dan 21,2 persen serta menaikkan SSIM 10,7 persen; penambahan CBAM memberi perbaikan lebih kecil. Penulis menyatakan pula bahwa pada data bunga AgRegNet mengungguli CSRNet, SFCN, SCAR, dan DRN, sedangkan pada data buah DRN tetap mencatat MAE 2,4 dan RMSE 3,2.

Batasan yang dinyatakan penulis mencakup penggunaan citra tampak depan tunggal, sehingga tidak semua bunga atau buah terlihat akibat oklusi dan bidang pandang kamera yang terbatas. Pada sistem teralis V, bunga latar juga kadang masuk ke peta kepadatan, dan sebagian bunga mekar penuh dekat batang tidak terdeteksi. Sebuah ranting yang membelah satu apel menjadi tiga bagian pernah memicu tiga peta kepadatan terpisah, meski penulis menyebut kasus tersebut jarang. Penulis mengusulkan citra multi-pandang, pencahayaan aktif yang invarian terhadap iluminasi, penyaringan latar berbasis kedalaman, serta penambahan citra beranotasi untuk meningkatkan keandalan pada berbagai kondisi kebun.

