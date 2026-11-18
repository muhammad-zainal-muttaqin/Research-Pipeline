# Boosting RGB-D Pear Detection via Depth-Constraint Enhanced Gaussian Prior

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ling2026boosting` |
| Judul asli | Boosting RGB-D Pear Detection via Depth-Constraint Enhanced Gaussian Prior |
| Penulis | Ling, Feng; Lin, Yunfeng; Mao, Weijie; Xu, Weizhong; Xiao, Wenzheng |
| Tahun | 2026 |
| Venue | Plants |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple, pear |

## Tautan Akses
- PDF: [ling2026boosting.pdf](../pdf/ling2026boosting.pdf)
- DOI resmi: https://doi.org/10.3390/plants15121852

## Gambaran Umum

Penelitian ini mengatasi deteksi buah pir di kebun kompleks, tempat oklusi, tumpang tindih buah, latar yang berantakan, dan pencahayaan yang sangat berubah-ubah menyulitkan penglihatan RGB. Penulis mencatat dua kelemahan metode RGB-D yang ada: informasi kedalaman belum dimanfaatkan sepenuhnya dan bentuk elips buah pir jarang dimodelkan secara eksplisit. Kotak ikat persegi panjang konvensional tidak sesuai dengan kontur pir yang melengkung, sehingga menghasilkan pelokalan yang kurang tepat dan lebih banyak derau latar. Usulan yang diajukan adalah Multimodal Gaussian Former (MMGFormer), kerangka deteksi yang memodelkan RGB dan kedalaman secara bersama dengan backbone konvolusi Siamese dan arsitektur fusi berbasis Transformer.

Dataset utama berisi 1.500 pasangan citra RGB-D yang dikumpulkan dari tiga kebun di satu provinsi dan dua kultivar pir, dengan 300 citra digunakan sebagai himpunan uji; pengambilan memakai Intel RealSense D435i. Generalisasi diuji pada tiga kondisi: himpunan lapangan di Kebun Percontohan Snow Pear Yunhe, Zhejiang, yang berisi 200 pasangan RGB-D dan 743 instan beranotasi; dataset publik KFuji RGB-DS untuk apel Fuji dengan kanal RGB, kedalaman, dan inframerah, yang kanal inframerahnya dibuang; serta uji pemanenan robotik pada 75 buah pir yang terlihat dan dapat dipanen. Model diuji langsung pada data lapangan tanpa fine-tuning. Pelatihan memakai batch 32, optimisator Adam, 100 epoch, masukan 1.024 × 1.024, dan augmentasi berupa distorsi warna, pemotongan acak, penskalaan, dan pembalikan.

Mekanisme utama terdiri atas tiga bagian. PMPConv (Pear-Oriented Multimodal Pinwheel Convolution) memadukan kernel asimetris, gerbang lintas modal, dan prior topeng elips untuk menangkap pola geometris pir; ablasi menunjukkan ketiganya memberi kinerja terbaik jika digabungkan. Gaussian Prior Box memodelkan setiap pir sebagai distribusi Gaussian dua dimensi dengan standar deviasi σx dan σy, sehingga dapat mengikuti elips kultivar dengan rasio panjang terhadap lebar sekitar 1,0 sampai 1,5; faktor skala kovarian s = 1,0 memberikan AP50 0,966 pada analisis sensitivitas, sedangkan s = 0,5 atau 4,0 menurunkan kualitas pencocokan. Depth-Aware Constraint Loss memaksa konsistensi kedalaman di dalam region yang diprediksi; mask Gaussian lunak lebih baik daripada mask keras dan skala wilayah k = 3 paling efektif. Robust Cross-Modal Token Exchange menukar secara acak sebagian token antara modalitas RGB dan kedalaman selama pelatihan agar model tidak bertumpu pada satu modalitas; rasio 0,2 memberi hasil terbaik, sedangkan rasio berlebih merusak representasi spesifik modalitas.

Pada himpunan uji pir, MMGFormer mencapai AP50 0,961, presisi 0,941, recall 0,951, F1-score 0,942, dan 41,2 FPS pada GPU Tesla P100. Sebagai pembanding, YOLOv8-l berbasis RGB mencatat AP50 0,918 dan varian RGB-D 0,932, sehingga keunggulan model ini berturut-turut 4,3 dan 2,9 poin AP50. Pada dataset apel KFuji RGB-DS, MMGFormer mencapai AP50 0,927, melampaui baseline Faster R-CNN publik sebesar 0,901 dan YOLOv8-l RGB-D sebesar 0,908. Pada himpunan lapangan, AP50 sebesar 0,923 dengan presisi 0,907 dan recall 0,891, sedangkan uji robotik menghasilkan harvesting success rate 84,0%, fruit damage rate 4,8%, dan average picking time 8,7 detik per buah. AP50 dihitung sebagai luas di bawah kurva presisi-recall, dengan ambang kepercayaan 0,2 dan IoU 0,5; NMS dipakai untuk menghapus kotak duplikat dengan IoU di atas 0,3 atau skor kepercayaan di bawah 0,05.

Batasan yang dinyatakan penulis mencakup keterbatasan data pada satu provinsi, dua kultivar, dan satu musim tanam, sehingga generalisasi ke kultivar pir lain atau jenis buah lain masih memerlukan pengujian. Sensor kedalaman terstruktur D435i dapat menurun kinerjanya di bawah sinar matahari kuat maupun gangguan inframerah ambien. Kecepatan 41,2 FPS diukur pada server Tesla P100; varian tertanam pada Jetson Orin NX masih dikembangkan dan belum dilaporkan. Analisis kasus gagal menunjukkan tiga pola utama: oklusi lebih dari 80% menyebabkan 48% dari seluruh kelewatan deteksi karena sinyal kedalaman di dalam region Gaussian didominasi daun, cahaya belakang kuat pada sekitar 12% citra sore menyaturasi token RGB dan memicu kotak ikat palsu di sekitar kumpulan daun terang, serta buah pir sangat lonjong dengan rasio panjang terhadap lebar sekitar 1,5 memicu bias pelokalan ke ujung calyx. AP50 turun menjadi 0,892 pada subhimpunan oklusi berat dan 0,901 pada subhimpunan cahaya belakang kuat. Penulis juga menyebut generalisasi lintas genotipe, sistem pelatihan, dan jenis kamera serta integrasi dengan penentuan ukuran buah, estimasi kematangan, dan perencanaan genggaman sebagai hal yang belum terselesaikan.

