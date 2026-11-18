# Grape berry detection and size measurement based on edge image processing and geometric morphology

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `luo2021grape` |
| Judul asli | Grape berry detection and size measurement based on edge image processing and geometric morphology |
| Penulis | Luo, Lufeng; Liu, Wentao; Lu, Qinghua; Wang, Jinhai; Wen, Weichang; Yan, De; Tang, Yunchao |
| Tahun | 2021 |
| Venue | Machines |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [luo2021grape.pdf](../pdf/luo2021grape.pdf)
- DOI resmi: https://doi.org/10.3390/machines9100233

## Gambaran Umum

Penelitian ini bertujuan menghitung jumlah buah anggur dan mengukur diametersnya dari citra dua dimensi untuk menunjang keputusan pemanen robot, estimasi hasil, dan penilaian kualitas. Penulis menyatakan penghitungan manual memakan waktu dan rawan salah, metode berbasis awan titik tiga dimensi bergantung pada alat pemindai laboratorium sehingga sulit digeneralisasi, dan algoritma dua dimensi konvensional memiliki ketahanan rendah serta kesulitan mengukur ukuran buah pada citra yang padat. Usulan ini ditujukan pada buah anggur bulat atau hampir bulat dalam keadaan saling menumpuk di lingkungan kebun.

Datanya berasal dari Guangdong Luonan Ecological Park. Peneliti memotret anggur Niagara, anggur hitam, dan anggur merah pada cuaca cerah dengan kamera dan tripod beresolusi maksimum 1.280 × 480 piksel, pada berbagai sudut dan jarak tanam serta tingkat kepenuhan yang berbeda. Setiap jenis dipotret 100 kali sehingga total 300 citra. Tidak ada pembagian data latih dan data uji yang dinyatakan; evaluasi memakai ketiga ratus citra itu. Kode ditulis dengan MATLAB 2020b dan perbandingan memakai pustaka Hough transform.

Alurnya dimulai dengan penghapusan latar, bilateral filtering untuk menekan derau tanpa menghilangkan tepi, konversi ke citra keabuan, dan deteksi tepi Canny. Titik menarik pada buah dicari memakai fast radial symmetry transform. Urutan piksel tepi ditelusuri dengan topeng 3 × 3, lalu titik cekung pada batas antarbuah ditentukan melalui deteksi sudut curvature scale space dengan ambang adaptif dan area pendukung dinamis; selisih kelengkungan lebih besar dari 0,015 ditandai sebagai titik singular. Pusat tiap segmen kontur dihitung dengan random sampling consensus, lalu segmen yang berasal dari buah yang sama dikelompokkan dengan strategi pencarian klaster lokal dan penentuan arah rotasi; nilai R1 antara 25 dan 35 piksel memberi pengelompokan terbaik. Bagian buah yang tertutup direkonstruksi dengan least squares fitting sebelum jumlah buah dihitung dan diameter diukur. Diameter dalam piksel diubah ke milimeter memakai koefisien kalibrasi papan kalibrasi; pengujian ulang sistem memberi kesalahan kalibrasi kurang dari 0,1 mm. Metrik evaluasinya adalah PPV = TP/(TP+FP), TPR = TP/(TP+FN), rata-rata jarak piksel (AD) antara titik cekung hasil deteksi dan titik sebenarnya dengan ambang 2 piksel, serta average Jaccard similarity coefficient (AJSC) dengan ambang tumpang tindih 0,5.

Pada deteksi titik cekung, TPR anggur merah mencapai 90,47 persen dengan PPV 82,97 persen dan AD 3,47 piksel; anggur hitam memberi TPR 85,21 persen, PPV 94,23 persen, dan AD 3,01 piksel; anggur Niagara memberi TPR 87,61 persen, PPV 92,92 persen, dan AD 3,34 piksel. Penulis melaporkan rata-rata presisi 87,76 persen dan rata-rata recall 90,04 persen untuk pencarian titik cekung. Untuk penghitungan jumlah buah, metode usulan memberi TPR 92,15 persen, PPV 87,59 persen, AJSC 88,33 persen pada anggur merah; 90,63 persen, 84,61 persen, 90,46 persen pada anggur hitam; serta 91,48 persen, 86,23 persen, 86,29 persen pada anggur Niagara. Hough transform memberi TPR berturut-turut 84,71 persen, 87,49 persen, dan 87,80 persen. Penulis menyatakan kenaikan TPR 7,44 persen dan PPV 11,13 persen pada anggur merah, kenaikan AJSC 2,29 persen pada anggur hitam, serta rata-rata akurasi penghitungan 91,42 persen atau 4,75 persen lebih tinggi daripada Hough transform. Waktu pemrosesan metode usulan adalah 17,848 detik, 36,651 detik, dan 42,433 detik, lebih lama daripada Hough transform yang memerlukan 7,389 detik, 5,796 detik, dan 7,067 detik. Pengukuran diameter pada 10 sampel memberi kesalahan rata-rata 2,30 mm dan kesalahan maksimum 5,62 mm terhadap pengukuran manual.

Batasan yang dinyatakan penulis mencakup kecepatan, jenis buah, dan kondisi tepi. Metode ini lebih lambat daripada Hough transform karena melakukan banyak perhitungan pada setiap piksel tepi. Pada buah lonjong seperti ARRA, kinerja melemah karena tepi buah bukan busur lingkaran, kelengkungan maksimal pada daerah persilangan tidak jelas sehingga titik cekung tidak terdeteksi, dan kondisi arah rotasi tidak dapat menggabungkan segmen kontur secara tepat. Sumber kesalahan lain adalah derau tepi yang dianggap kontur buah, pusat segmen busur pada buah yang sama yang terlalu berjauhan disertai perbedaan radius yang besar, serta area buah yang tertutup terlalu luas sehingga fitting menjadi tidak tepat. Buah juga tidak terdeteksi bila segmen konturnya terlalu pendek sehingga dibuang sebagai derau atau bila titik cekung tidak terbentuk. Penulis menyatakan data tidak tersedia (Data Availability Statement: Not applicable).
