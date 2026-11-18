# A PICTURE OF RIPENESS: INVESTIGATING IMAGE-BASED TECHNIQUES FOR OIL PALM FRUIT GRADING

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rosbi2025picture` |
| Judul asli | A PICTURE OF RIPENESS: INVESTIGATING IMAGE-BASED TECHNIQUES FOR OIL PALM FRUIT GRADING |
| Penulis | Rosbi, Munirah |
| Tahun | 2025 |
| Venue | Journal of Oil Palm Research |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [rosbi2025picture.pdf](../pdf/rosbi2025picture.pdf)
- DOI resmi: https://doi.org/10.21894/jopr.2024.0015

## Gambaran Umum

Tinjauan ini mengkaji teknik berbasis citra untuk menilai kematangan tandan buah segar (FFB) sawit. Di Malaysia, sektor sawit menyerap sekitar 18,0% luas lahan dan menyumbang 66,1% pendapatan ekspor, tetapi sekitar 30,0% hasil hilang akibat pemanenan buah mentah, tandan matang yang tidak dipanen, dan buah lepas yang tidak dikumpulkan. Penentuan kematangan secara manual lambat, subjektif, dan memerlukan pegawai berpengalaman, sehingga keterbatasan tenaga kerja pascapandemi COVID-19 mendorong otomatisasi.

Badan Minyak Sawit Malaysia membagi kematangan menjadi empat kelas, yaitu mentah, belum matang, matang, dan terlalu matang, yang dibedakan lewat warna: ungu kehitaman, ungu kemerahan, jingga kemerahan, dan merah gelap. Penulis meninjau alur klasifikasi yang terdiri dari prapemrosesan, segmentasi, ekstraksi ciri, dan klasifikasi, serta menelusuri evolusi metode dari rentang warna dan nilai digital intensitas (DN), klasifikasi fuzzy, jarak tetangga histogram, pembelajaran mesin (ANN, KNN, CNN, SVM, LDA), hingga YOLO. Prapemrosesan memakai pelabelan, pengubahan ukuran, filter median, dan Gaussian blur. Segmentasi memakai ambang batas pada HSV atau Otsu, pertumbuhan wilayah n-SRG, pengelompokan k-means dan fuzzy c-means, analisis tekstur, deteksi tepi Canny, GrabCut, pemilihan daerah menarik (ROI), dan deteksi objek YOLO-P.

Ekstraksi ciri memakai warna RGB, rasio R/G dan R/B, histogram, dan momen warna, serta ruang warna HSV, HSI, YIQ, YCbCr, dan CIELAB untuk mengurangi pengaruh cahaya luar. Ciri tekstur memakai Gabor wavelet, *grey-level co-occurrence matrix* (GLCM), *basic grey-level aura matrix* (BGLAM), HOG, BOVW, dan SURF; ciri tepi Canny dan Sobel dipakai untuk mengenali duri dan soket kosong pada buah terlalu matang. Seleksi ciri memakai PCA, *correlation-based feature selection* (CFS), regresi mundur, dan metode fuzzy untuk mengurangi overfitting. Klasifikasi memakai LDA, ANN/MLP, SVM, KNN, CNN (AlexNet, DenseNet, ResNet), dan YOLO.

Angka hasil yang dikumpulkan penulis mencakup BGLAM 93% pada citra dalam ruang tertutup, tetapi ciri tekstur pada citra luar ruang hanya mencapai 70% dan 75%; kombinasi warna dan tepi Canny memberi 79%. LDA mencapai 98,88% untuk tiga tingkat kematangan, seleksi dua ciri memberi lebih dari 90%, dan seleksi lima ciri memberi 98,2%. Deteksi YOLO-P memakai 5.350 citra latih mencapai 98,96% mAP, sedangkan YOLOv4 dengan 490 citra mencapai 87,90% mAP; penulis mencatat YOLO memerlukan lebih dari 5.000 sampel untuk mencapai mAP 98%. Beberapa kajian dalam ruang terkontrol melaporkan 100% (Ghazali 2009; Fahmi 2018), sementara kajian luar ruang dengan SVM mencapai 98,9% (Sabri 2018) dan 98,3% (Septiarini 2021); ponsel berbiaya rendah dapat mencapai lebih dari 78% dengan pengklasifikasi yang andal.

Penulis menyatakan teknik ini belum banyak dipakai: dari 36 kajian yang dibandingkan, hanya 26 yang memperkenalkan pendekatan baru, sisanya menyempurnakan kerja sebelumnya, dan sistem komersial masih terbatas. Segmentasi citra luar ruang terganggu oleh pencahayaan tidak merata, oklusi, bayangan, dan cahaya belakang yang menggelapkan warna; pengelompokan k-means menghasilkan under-segmentasi, sedangkan fuzzy c-means menghasilkan over-segmentasi; ROI manual memakan waktu dan ROI otomatis sering tidak tepat. Metode koreksi warna masih jarang dipakai, dan segmentasi semantik belum populer karena bentuk tandan tidak tetap serta pelabelan citra sulit. Penulis menyarankan penggabungan koreksi warna dengan pengelompokan dan YOLO, penggunaan ciri tekstur duri dan soket kosong, serta pencitraan multispektral, termal, dan kedalaman dari Kinect, dengan seleksi ciri untuk mencegah overfitting.

