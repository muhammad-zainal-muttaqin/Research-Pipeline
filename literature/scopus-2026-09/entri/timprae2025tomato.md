# Tomato Growth Monitoring and Phenological Analysis Using Deep Learning-Based Instance Segmentation and 3D Point Cloud Reconstruction

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `timprae2025tomato` |
| Judul asli | Tomato Growth Monitoring and Phenological Analysis Using Deep Learning-Based Instance Segmentation and 3D Point Cloud Reconstruction |
| Penulis | Timprae, Warut; Sagawa, Tatsuki; Baar, Stefan; Kondo, Satoshi; Okada, Yoshifumi; Sato, Kazuhiko; Rumahorbo, Poltak Sandro; Lyu, Yan; Shibuya, Kyuki; Gama, Yoshiki; Hatanaka, Yoshiki; Watanabe, Shinya |
| Tahun | 2025 |
| Venue | Sustainability Switzerland |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato, cherry |

## Tautan Akses
- PDF: [timprae2025tomato.pdf](../pdf/timprae2025tomato.pdf)
- DOI resmi: https://doi.org/10.3390/su172210120

## Gambaran Umum

Penelitian ini bertujuan memantau pertumbuhan tomat secara nondestruktif di
rumah kaca, dengan fokus pada kultivar buah kecil (cherry tomato) yang sulit
diukur memakai analisis citra dua dimensi. Permasalahan yang diangkat adalah
cara citra 2D sering gagal menangkap ciri morfologi yang tepat, sehingga
membatasi pemodelan pertumbuhan dan estimasi hasil. Penulis mengusulkan kerangka
fenotiping yang menggabungkan segmentasi instance, rekonstruksi awan titik
tiga dimensi beresolusi tinggi, dan pemasangan elipsoid untuk mengestimasi
ukuran dan kematangan buah dari rekaman video harian, lalu memodelkan dinamika
pertumbuhannya.

Data berupa video harian tomat cherry di Asai Nursery, Tsu, Prefektur Mie,
Jepang, selama sekitar 30–40 hari dari pembentukan buah hingga matang penuh.
Rekaman MP4 beresolusi 1920 × 1080 diambil dengan kamera ponsel biasa
(Lenovo Tab M9, 8 megapiksel) pada jarak hingga sekitar 60 cm dan sudut
sekitar 180°, bukan pandangan penuh 360°; kamera tidak tetap dan tidak
dikalibrasi, sehingga posisi dan sudut berubah tiap hari. Model segmentasi
YOLOv8x-seg dilatih pada himpunan Laboro Tomato yang memuat 804 citra dalam
tiga kelas kematangan, dengan ukuran 3024 × 4032 dan 3120 × 4160 piksel;
pembagian latih dan uji tidak dinyatakan. Pelatihan memakai ukuran masukan
640 × 640, batch 16, 10 epoch, laju pembelajaran 0,01, serta augmentasi
pembalikan, rotasi, dan geser. Rekonstruksi tiga dimensi memakai COLMAP untuk
SfM dan MVS, lalu Nerfacto dari Nerfstudio untuk menyempurnakan permukaan.
Segmentasi buah pada awan titik memakai DBSCAN terbantu pewarnaan dalam ruang
HSV.

Mekanisme pengukuran memasangkan elipsoid ke setiap gugus titik memakai
kuadrat-terkecil, dengan sumbu utama turunan nilai eigen dan volume
V = 4/3 πabc. Kalibrasi metrik memakai bola referensi berdiameter 40 mm,
sehingga ukuran buah dihitung sebagai perbandingan panjang buah dan bola di
awan titik dikali 40. Kematangan dinilai dari ruang warna CIELAB: nilai a* dan
b* per piksel diplot, lalu kemiringan interpolasi linier dipakai sebagai
indikator dan dipetakan ke kelas kematangan menurut acuan warna petani.
Dinamika ukuran dan kematangan dicocokkan dengan fungsi logistik
f(x) = A/(1 + e^(−d(x−x0))) yang dioptimalkan memakai metode GRG; laju
pertumbuhan maksimum gmax dipakai untuk membandingkan musim. Fokus kerja ini
adalah pemantauan pertumbuhan per buah, bukan penghitungan atau penghapusan
duplikat lintas pandang.

Hasil utama menunjukkan YOLOv8x-seg mencapai segmentasi mAP@0,5 sebesar 0,881,
presisi 0,806, dan recall 0,818, mengungguli Mask R-CNN yang mencatat mAP 0,523;
mAP per kelas adalah 0,886 untuk buah matang penuh, 0,919 untuk hijau, dan
0,839 untuk setengah matang. Estimasi ukuran memberi galat rata-rata 8,01%
terhadap pengukuran jangka sorong manual, dengan kecenderungan sedikit
berlebih. Kemiringan warna pada 1, 2, 4, dan 12 Juli berturut-turut −0,3,
0,03, 0,83, dan 1,31, yang diklasifikasikan sebagai kelas 1, 2, 5, dan 8.
Ukuran buah meningkat cepat dalam 40 hari pertama dan stabil setelah hari
ke-45, sedangkan perubahan warna dimulai sekitar hari ke-20 dan berjalan dari
buah atas ke bawah dalam satu tandan. Nilai gmax ukuran musim panas 1,08
berbanding 0,87 pada musim dingin (24,14% lebih tinggi); gmax kematangan 0,41
berbanding 0,21 (95,24% lebih cepat), dengan buah musim dingin matang
sekitar 10 hari lebih lambat.

Batasan yang dinyatakan penulis mencakup okklusi oleh daun dan buah yang
saling menimpa, yang mengganggu deteksi dan pemasangan elipsoid sehingga
rekonstruksi bisa keliru pada buah yang hanya tampak sebagian. Perubahan posisi
kamera dan pencahayaan pada rekaman genggaman memicu ketidakkonsistenan
pemodelan dan penilaian kematangan. Beberapa tahap seperti pemilihan objek,
pemeriksaan bentuk, dan pelacakan masih memerlukan campur tangan manual. Penulis
juga menyatakan galat dapat berasal dari pengukuran jangka sorong karena buah
berkulit lunak dapat penyok, dan mengusulkan perbandingan dengan LiDAR serta
penguatan sistem terhadap kondisi lapang.
