# UAV-based monocular 3D panoptic mapping for fruit shape completion in orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2026uav` |
| Judul asli | UAV-based monocular 3D panoptic mapping for fruit shape completion in orchard |
| Penulis | Wang, Kaiwen; Pan, Yue; Magistri, Federico; Kooistra, Lammert; Stachniss, Cyrill; Wang, Wensheng; Valente, Jo\~ao |
| Tahun | 2026 |
| Venue | ISPRS Journal of Photogrammetry and Remote Sensing |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [wang2026uav.pdf](../pdf/wang2026uav.pdf)
- DOI resmi: https://doi.org/10.1016/j.isprsjprs.2025.11.013

## Gambaran Umum
Makalah ini mengusulkan kerangka pemetaan panoptik 3D monokular berbasis UAV (*unmanned aerial vehicle*) untuk melengkapi bentuk apel yang tertutup sebagian (*fruit shape completion*) di kebun apel. Kerangka menggabungkan tiga komponen: Grounded-SAM2 untuk pelacakan dan segmentasi multi-objek (*multi-object tracking and segmentation*, MOTS), rekonstruksi *structure-from-motion* (SfM) dengan Agisoft Metashape untuk adegan 3D, dan DeepSDF (representasi implisit berbasis jaringan saraf) untuk melengkapi geometri apel yang tertutup. Penulis juga mengusulkan protokol evaluasi MOTS yang tidak memerlukan anotasi kebenaran dasar.

Data lapangan diambil di kebun apel Elstar di Randwijk, Overbetuwe, Belanda, pada 24 Juli 2024 dengan UAV DJI Phantom 4 RTK (video 3840 × 2160, 29,98 fps, ketinggian sekitar 2 sampai 4 m). Data laboratorium berupa pindaian 3D 100 apel Elstar. Hasil utama: pada MOTS, Grounded-SAM2 pada mode terbang A mencapai MOTSA 34,84% dan sMOTSA 14,95%; pada uji laboratorium, jarak Chamfer DeepSDF 0,98 ± 0,05 dibandingkan 1,67 ± 0,08 untuk pendekatan bola (*sphere approximation*, SA); di kebun, 2.729 apel pada baris 1 terdeteksi dan direkonstruksi, dan RMSE diameter maksimum terhadap pengukuran jangka sorong untuk 120 apel adalah 1,85 cm.

Penulis menyimpulkan bahwa apel dengan visibilitas lebih dari 10% dapat direkonstruksi lengkap. Tujuan akhirnya adalah fenotipe fruit-level (bentuk dan ukuran), bukan penghitungan hasil panen.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Bentuk dan ukuran buah penting bagi nilai pasar, penilaian pertumbuhan, dan estimasi hasil di tingkat buah. Fenotipe manual sulit diperluas. Pemindai laser terestrial (TLS) mahal dan peka terhadap oklusi, sedangkan rekonstruksi SfM dari UAV lebih murah (kurang dari 1.000 euro dibandingkan LiDAR lebih dari 10.000 euro, menurut makalah) tetapi bergantung pada fitur permukaan yang tampak sehingga tidak merekonstruksi area bayangan atau tertutup. Penelitian terdahulu pada UAV umumnya berfokus pada sifat tingkat pohon seperti volume kanopi.

Banyak apel tertutup daun, ranting, atau apel lain, sehingga metode geometri konvensional tidak dapat memulihkan bentuk lengkap buah. Pelacakan buah pada video UAV juga sulit karena buah kecil, mirip satu sama lain, padat, dan hampir diam sehingga gerakannya berkorelasi dengan kanopi; penulis mencatat bahwa studi terdahulu melaporkan MOTSA dan sMOTSA yang bahkan negatif.

## Ide Utama
Ide utama adalah menghubungkan pelacakan 2D dengan geometri 3D: ID instans apel dari MOTS dipakai untuk memotong titik 3D dari peta SfM per apel, sehingga setiap apel memiliki awan titik parsial sendiri. Awan titik parsial itu lalu dicocokkan dengan prior bentuk DeepSDF yang dilatih pada pindaian apel utuh di laboratorium, sehingga bentuk lengkap dapat diperkirakan dari permukaan yang sebagian tampak.

Latar (kebun) dan latar depan (apel) dipisahkan dalam peta panoptik. Resolusi latar diturunkan (voxel 0,01) untuk menghemat memori, sedangkan resolusi apel dipertahankan. Penulis juga membandingkan empat pola terbang (mode A sampai D) dan mengusulkan evaluasi MOTS tanpa anotasi yang memakai rasio kecepatan pusat massa apel terhadap kecepatan kamera: bila pelacakan benar, rasio mendekati 1.

## Cara Kerja Langkah demi Langkah

```
  Video UAV (3 fps) -> Grounded-SAM2 -> ID + topeng apel
  Video UAV (3 fps) -> SfM (Metashape) -> pose + kedalaman + titik
  topeng + kedalaman + pose -> awan titik parsial per apel
  awan titik parsial -> optimasi DeepSDF -> mesh apel lengkap
```

### 1. Akuisisi data
Lapangan: area 0,083 ha dengan empat baris apel Elstar (*Malus pumila* 'Elstar'), jarak pohon 1,1 m dan jarak baris 3,0 m, sekitar 80 pohon per baris. Apel berada pada tahap pembesaran dan dipanen satu bulan kemudian. UAV DJI Phantom 4 RTK dengan sensor RGB FC6310R (CMOS, 3840 × 2160, fokus 8,8 mm), ketinggian sekitar 2 sampai 4 m, kecepatan sekitar 0,1 sampai 1,5 m/s, cuaca cerah, angin 2,8 m/s, suhu 20 °C. Empat mode terbang: A (lurus di tepi baris, kamera dari samping), B (naik-turun lebih dekat dengan pohon), C (di antara baris pada ketinggian lebih tinggi, pandangan samping), dan D (di antara baris, pandangan depan). Dari video 29,98 fps hanya 3 fps yang dipakai.

Acuan lapangan: 14 tiang kayu per baris setinggi 2,7 m untuk skala metrik, dan diameter maksimum apel diukur dengan jangka sorong pada 135 apel (24 pohon di baris 1, sekitar enam apel per pohon) yang diberi pita berwarna pada tangkai. Laboratorium: 100 apel Elstar dipindai dengan CR-Scan Ferret (Creality, akurasi 0,1 mm), dinormalisasi ke sistem koordinat kanonik (sumbu z searah tangkai, pusat di titik asal); 88 apel untuk pelatihan dan 12 untuk uji. Diameter apel laboratorium terutama 70 sampai 85 mm, sedangkan apel lapangan terutama 55 sampai 65 mm.

### 2. MOTS dengan Grounded-SAM2
Grounding DINO dengan perintah teks "apple" menghasilkan kotak yang menjadi prompt untuk prediktor video SAM2, sehingga diperoleh topeng instans dengan ID yang konsisten antarbingkai. Dipakai model SAM2 besar dan Grounding DINO tiny pada GPU NVIDIA Quadro RTX A6000. Pembanding adalah AppleMOTS dengan TrackRCNN dan PointTrack.

### 3. Rekonstruksi SfM
Bingkai 3 fps diimpor ke Agisoft Metashape Pro dengan penanda pada puncak dan dasar tiang (jarak 2,7 m) sebagai skala; penyelarasan akurasi tertinggi dengan batas 40.000 titik kunci dan 4.000 titik ikat; galat reproyeksi akhir 0,691 piksel. Peta kedalaman dan pose kamera berskala metrik diekspor.

### 4. Pemetaan panoptik dan penyelesaian bentuk
Titik latar depan diperoleh dari piksel kedalaman di dalam topeng tiap apel, ditransformasi ke koordinat dunia dengan pose kamera, dan diakumulasi dari banyak bingkai menjadi submap per apel. DeepSDF (decoder MLP delapan lapis dengan 512 dimensi per lapis, kode laten ukuran $C = 32$, 200.000 titik sampel per apel, 3.000 epoch, laju belajar awal 0,001 yang turun 0,0005 tiap 300 epoch) dilatih pada pindaian laboratorium. Saat inferensi, pose sim(3) dan kode laten dioptimalkan dengan Levenberg-Marquardt untuk meminimalkan kehilangan permukaan $\mathcal{L}_s$ ditambah regularisasi $\mathcal{L}_r = \|z\|^2$, dengan inisialisasi kode laten nol; mesh lengkap dihasilkan dengan *marching cubes*.

### 5. Evaluasi
MOTS dievaluasi dengan MOTSA, sMOTSA, dan MOTSP pada anotasi manual 10 bingkai berurutan per mode terbang (1.890, 756, 470, dan 1.015 instans apel untuk mode A, B, C, D). Evaluasi tanpa anotasi memakai 10 jendela acak berisi 5 bingkai berurutan dengan 10 apel acak per jendela. Rekonstruksi diukur dengan jarak Chamfer di laboratorium dan RMSE diameter maksimum di lapangan. Tingkat oklusi dikelompokkan lima tingkat berdasarkan rasio area terlihat: A (≥90%), B (70% sampai 89%), C (40% sampai 69%), D (10% sampai 39%), E (<10%).

## Eksperimen dan Hasil
Tabel 2 makalah (pelacakan dan segmentasi apel pada empat mode terbang):

| Model | Mode | MOTSA (%) | sMOTSA (%) | MOTSP (%) |
|---|---|---|---|---|
| TrackRCNN | A | -2,69 | -2,73 | 58,71 |
| TrackRCNN | B | -6,70 | -7,04 | 57,74 |
| TrackRCNN | C | -8,30 | -8,30 | 0,00 |
| TrackRCNN | D | -4,43 | -4,43 | 0,00 |
| PointTrack | A | 8,47 | 6,38 | 64,98 |
| PointTrack | B | 1,03 | -3,79 | 62,19 |
| PointTrack | C | -2,03 | -3,85 | 14,21 |
| PointTrack | D | -1,38 | -2,43 | 6,98 |
| Grounded-SAM2 | A | 34,84 | 14,95 | 71,98 |
| Grounded-SAM2 | B | 2,72 | -1,20 | 72,13 |
| Grounded-SAM2 | C | -40,18 | -57,05 | 66,96 |
| Grounded-SAM2 | D | 1,99 | 1,25 | 73,29 |

Kecepatan rerata: TrackRCNN 0,15 fps, PointTrack 3,24 fps, Grounded-SAM2 1,31 fps. Grounded-SAM2 terbaik pada mode A. Pada mode D, MOTSP tertinggi (73,29%) tetapi tingkat deteksi apel rendah. Pada mode C kinerjanya turun nyata (MOTSA -40,18%). Evaluasi tanpa anotasi pada mode A menunjukkan sebagian besar rasio kecepatan mendekati 1,0, dengan beberapa nilai ekstrem yang menurut penulis dapat berasal dari pertukaran ID, oklusi, atau UAV yang melayang (rasio nol).

Rekonstruksi di laboratorium (Tabel 3; 12 apel uji; satuan galat tidak ditulis pada tabel utama, tetapi Tabel A.6 memberi satuan mm): SA 1,67 ± 0,08 dan DeepSDF 0,98 ± 0,05. Contoh Tabel A.6: Apple10 SA 1,59 mm dan DeepSDF 0,93 mm; Apple12 SA 1,70 dan DeepSDF 0,97.

Di kebun, 2.729 apel terdeteksi dan direkonstruksi pada baris 1 mode A. Dari 135 apel bersampel: 12,6% tingkat A, 19,3% B, 27,4% C, 30,4% D, dan 10,4% E (tidak terdeteksi atau tidak terlacak); 120 dari 135 apel berhasil dideteksi dan direkonstruksi, dengan RMSE diameter 1,85 cm. Galat berkorelasi positif dengan tingkat oklusi kecuali turun pada tingkat D. Biaya komputasi: SfM sekitar 24 menit rerata untuk empat mode (Tabel 4: mode A dengan 210 citra, pembangunan awan titik 33 menit 8 detik), rekonstruksi DeepSDF 0,58 detik per apel parsial, dan memori submap latar turun 31,9% dari 1,75 GB menjadi 571 MB.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: kerangka mengatasi oklusi dengan prior bentuk, memakai kamera RGB monokular berbiaya rendah, dapat merekonstruksi apel dengan visibilitas di atas 10% (dibandingkan metode amodal 2D yang hanya mengukur apel dengan visibilitas di atas 60%), tidak memerlukan pelabelan massal untuk melatih model amodal, dan menyediakan protokol evaluasi MOTS tanpa anotasi. Penulis juga menyediakan dataset apel 3D laboratorium dan video UAV lapangan, serta kode.

Keterbatasan yang dinyatakan penulis: DeepSDF dilatih pada apel matang di laboratorium, sedangkan apel lapangan pada tahap pembesaran, sehingga ada deviasi diameter sistematis rata-rata 1,6 cm; kinerja seluruh sistem bergantung pada MOTS yang masih mengalami pertukaran ID dan deteksi salah; hanya kebun berbaris yang diuji; angin kuat dan sinar matahari rendah dapat menurunkan kualitas; jejak data besar (sekitar 1.800 bingkai atau 700 MB video mentah dan 1,27 GB citra kedalaman untuk satu baris); ukuran apel terkecil yang terdeteksi sekitar 45 mm; satu varietas dan satu waktu pengambilan data.

Menurut pembacaan ringkasan ini, keterbatasan tambahan adalah sebagai berikut. Hasil pelacakan tidak dievaluasi sebagai penghitungan jumlah buah unik; tidak ada hitungan buah, hanya diameter. Nilai MOTSA yang tinggi hanya terjadi pada satu mode terbang (A) dan nilai MOTSA mode B sampai D mendekati nol atau negatif, sehingga ketahanan lintas pola terbang terbatas. Anotasi MOTS hanya mencakup 10 bingkai per mode. Makalah memakai istilah RMSE dan MAE untuk nilai 1,85 cm secara bergantian (seksi 4.3 dan 5.3).

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat dari banyak bingkai: ID instans apel dari Grounded-SAM2 menghubungkan topeng apel yang sama antarbingkai, dan topeng itu diproyeksikan ke ruang 3D bersama lewat kedalaman dan pose SfM sehingga awan titik apel yang sama dikumpulkan dalam satu submap. Mekanismenya gabungan pelacakan video (MOTS) dan rekonstruksi 3D. Makalah tidak melaporkan hitungan buah unik; keluarannya adalah diameter dan bentuk. Jumlah 2.729 apel pada baris 1 adalah jumlah instans yang direkonstruksi, tidak dibandingkan dengan hitungan panen atau hitungan lapangan dalam teks.

Hitungan tidak dilaporkan per kelas. Acuan adalah pengukuran diameter dengan jangka sorong (135 apel) dan anotasi topeng pada 10 bingkai per mode terbang untuk MOTS. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: pemakaian ID pelacakan untuk menautkan topeng 2D ke instans 3D, serta protokol evaluasi pelacakan tanpa anotasi berbasis rasio kecepatan instans terhadap kecepatan kamera (memerlukan gerak kamera yang diketahui). Hasilnya juga menunjukkan bahwa pelacakan objek sejenis yang padat dan diam, mirip tandan pada tajuk, sangat peka terhadap pola terbang (MOTSA dari 34,84% turun hingga -40,18% untuk model yang sama).

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `wang2026uav`.

Wang dkk. mengusulkan kerangka pemetaan panoptik 3D monokular berbasis UAV yang menggabungkan Grounded-SAM2 untuk pelacakan dan segmentasi multi-objek, SfM fotogrametri, dan DeepSDF untuk melengkapi bentuk apel yang tertutup. Pada kebun apel Elstar dengan empat pola terbang, pelacakan terbaik pada mode terbang A (MOTSA 34,84%, sMOTSA 14,95%); jarak Chamfer DeepSDF 0,98 dibandingkan 1,67 untuk pendekatan bola pada apel uji laboratorium; dan 120 dari 135 apel bersampel direkonstruksi di lapangan dengan RMSE diameter 1,85 cm. Makalah tidak melaporkan hitungan buah.

Catatan verifikasi data: Angka MOTS diambil dari Tabel 2 dan seksi 4.1; jarak Chamfer dari Tabel 3 dan Tabel A.6; angka 2.729 apel, distribusi tingkat oklusi (12,6%, 19,3%, 27,4%, 30,4%, 10,4%), 120 dari 135 apel, dan RMSE 1,85 cm dari seksi 4.3; biaya komputasi dari Tabel 4 dan seksi 4.3 serta 5.3. Satuan Tabel 3 tidak tertulis pada teks ekstraksi (hanya Tabel A.6 yang bersatuan mm); satuan milimeter dalam ringkasan ini mengikuti Tabel A.6 dan abstrak. Seksi 5.2 merujuk "Table 4, and Fig. 9(a)" untuk distribusi visibilitas, sedangkan tingkat oklusi didefinisikan pada Tabel 5; teks juga menyebut "Chamfer distance (Eq. (9))" walaupun rumusnya Eq. (10). Hasil Gambar 8 dan 9 tidak dapat dibaca dari teks ekstraksi. Berkas teks hanya diperiksa sampai awal Tabel A.6 (apel ke-15); daftar tabel lampiran selanjutnya tidak dipakai.
