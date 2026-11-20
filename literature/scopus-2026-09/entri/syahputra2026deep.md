# Deep Learning for Ripeness Grading of Oil Palm Fresh Fruit Bunches: A Comprehensive Review of Convolutional Neural Network Approaches

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `syahputra2026deep` |
| Judul asli | Deep Learning for Ripeness Grading of Oil Palm Fresh Fruit Bunches: A Comprehensive Review of Convolutional Neural Network Approaches |
| Penulis | Syahputra, Wahyu Nurkholis Hadi; Chaichana, Chatchawan; Bundhurat, Damorn; Wuttisarnwattana, Patiwet; Putra, Bayu Taruna Widjaja |
| Tahun | 2026 |
| Venue | Trends in Sciences |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [syahputra2026deep.pdf](../pdf/syahputra2026deep.pdf)
- DOI resmi: https://doi.org/10.48048/tis.2026.13227

## Gambaran Umum

Tinjauan ini mengkaji penggunaan jaringan saraf konvolusional (*convolutional neural network*, CNN) untuk penilaian kematangan tandan buah segar (TBS) kelapa sawit. Penulis berangkat dari peran kematangan terhadap kandungan asam lemak bebas, rendemen minyak, dan mutu produk: kesalahan penilaian saat panen atau penerimaan di pabrik menaikkan asam lemak bebas, menurunkan rendemen, dan menyebabkan kerugian ekonomi. Kajian bertujuan memetakan tren publikasi dan kemajuan teknik CNN, sekaligus mengidentifikasi kesenjangan menuju penerapan skala besar. Asosiasi lintas pandang dan penghitungan buah unik tidak dibahas.

Data dan metode memadukan analisis bibliometrik dan tinjauan literatur. Sumber data adalah Scopus dengan kueri terstruktur pada judul, abstrak, dan kata kunci penulis yang menggabungkan istilah sawit dan TBS, istilah CNN atau pembelajaran mendalam, serta istilah pengelompokan, kematangan, dan klasifikasi, dibatasi pada publikasi berbahasa Inggris. Pencarian awal menghasilkan 143 dokumen, lalu penyaringan isi mengeluarkan kajian yang memakai CNN untuk tujuan di luar penilaian kematangan, seperti deteksi pohon dan pemetaan perkebunan, sehingga tersisa 126 kajian. Analisis kemunculan kata kunci memakai VOSviewer. Publikasi terbanyak berasal dari Malaysia, diikuti Indonesia, dengan tren dimulai sekitar 2017 dan meningkat kuat setelah 2021.

Mekanisme deteksi dan klasifikasi bertumpu pada CNN, baik untuk klasifikasi citra maupun deteksi objek. Penulis mencatat dominasi detektor satu tahap, khususnya keluarga YOLO, karena kemampuan waktu nyata dan kinerja yang relatif tinggi; pendekatan lain mencakup AlexNet, DenseNet, EfficientNet, Faster R-CNN, dan Mask R-CNN. Ciri kematangan bersumber dari perubahan morfologi luar yang mudah diamati pada tandan. Kajian terkini mengarah pada penerapan perangkat seluler, sistem tertanam, dan komputasi tepi agar penilaian dapat dilakukan di lokasi tanpa server berdaya tinggi, dengan arah masa depan berupa penginderaan multimodal yang menggabungkan RGB dengan berat, respon near-infrared, data termal, atau kedalaman.

Angka hasil dikutip dari kajian dalam korpus tinjauan, bukan dari percobaan penulis, sehingga tidak ada metrik atau acuan hitung milik tinjauan ini. Anotasi citra berbasis YOLO mencapai mAP 98,7%; EfficientNetB0 pada TensorFlow Lite meraih akurasi 0,893 dengan waktu inferensi 96 ms per citra; YOLOv4 pada sistem pemanen mencapai mAP 87,9% dan recall 82% pada IoU di atas 0,5 setelah 2.000 iterasi dengan kecepatan sekitar 21 FPS. DenseNet mengungguli AlexNet sebesar 8,5% dalam akurasi dan 8% dalam skor F1 pada dataset tujuh tingkat kematangan dengan 400 citra. YOLOv4 dengan kuantisasi 16 bit memberi mAP 12% lebih tinggi daripada YOLOv4-Tiny, sementara AlexNet yang dilatih ulang dengan analisis warna HSV mencapai akurasi 85% pada 100 citra. Metrik yang dipakai meliputi akurasi, mAP, recall, skor F1, IoU, dan waktu inferensi.

Batasan yang dinyatakan penulis meliputi keragaman dataset yang rendah, karena setiap kajian memakai dataset dan kondisi pengumpulan sendiri dengan definisi kematangan, format anotasi, resolusi citra, dan pembagian data yang tidak seragam sehingga metrik tidak dapat dibandingkan langsung. Kajian juga terkendala kebutuhan daya hitung tinggi, integrasi yang kurang dengan sistem manajemen perkebunan dan pabrik berbasis Internet of Things, serta belum adanya estimasi waktu nyata untuk indikator mutu seperti asam lemak bebas dan atribut kernel. Banyak kajian tidak melaporkan waktu inferensi, penggunaan memori, atau konsumsi energi. Penulis mengusulkan dataset bersama bernama PalmNet, metrik kinerja terstandar, serta kerangka pembelajaran multitugas yang menggabungkan penilaian kematangan dengan estimasi rendemen minyak.
