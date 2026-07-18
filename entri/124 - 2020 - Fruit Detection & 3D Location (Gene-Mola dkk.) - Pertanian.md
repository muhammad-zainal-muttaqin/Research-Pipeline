# 124 - Fruit Detection and 3D Location Using Instance Segmentation Neural Networks and Structure-from-Motion Photogrammetry

## Metadata Ringkas
| Atribut | Nilai |
|---|---|
| Kunci BibTeX | `genemola2020fruit3d` |
| Judul asli | Fruit Detection and 3D Location Using Instance Segmentation Neural Networks and Structure-from-Motion Photogrammetry |
| Penulis | Jordi Gené-Mola, Ricardo Sanz-Cortiella, Joan R. Rosell-Polo, Josep-Ramon Morera, Javier Ruiz-Carulla, Eduard Gregorio, Alexandre Escolà |
| Tahun | 2020 |
| Venue | Computers and Electronics in Agriculture |
| Tema | Pertanian |

## Tautan Akses
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Fruit%20Detection%20and%203D%20Location%20Using%20Instance%20Segmentation%20Neural%20Networks%20and%20Structure-from-Motion%20Photogrammetry
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Fruit%20Detection%20and%203D%20Location%20Using%20Instance%20Segmentation%20Neural%20Networks%20and%20Structure-from-Motion%20Photogrammetry&sort=relevance
- **DOI Resmi:** https://doi.org/10.1016/j.compag.2019.105165

## Gambaran Umum
Makalah ini menyajikan sebuah metodologi untuk deteksi buah dan lokalisasi koordinat spasial tiga dimensi (*3D location*) buah di kebun buah menggunakan sensor pasif. Masalah utama yang diselesaikan adalah ketidakakuratan lokalisasi akibat oklusi dedaunan dan gangguan radiasi solar pada sensor kedalaman aktif luar ruangan. Metode yang diusulkan mengintegrasikan segmentasi instan (*instance segmentation*) 2D berbasis *Mask R-CNN* dengan rekonstruksi awan titik (*point cloud*) 3D berbasis *Structure-from-Motion* (SfM) dari citra multi-sudut (*multi-view*).

Sistem ini memproyeksikan masker 2D buah ke dalam ruang 3D hasil SfM. Deteksi palsu (*false positive*) disaring menggunakan pengklasifikasi *Support Vector Machine* (SVM) biner yang menganalisis fitur geometris dan kerapatan klaster titik 3D. Uji coba eksperimental pada dataset Fuji-SfM menunjukkan peningkatan kinerja yang signifikan dengan pencapaian F1-score sebesar 0,881 pada pemetaan lokasi 3D dibandingkan dengan 0,816 pada tingkat deteksi 2D saja. Penelitian ini menyediakan solusi pemetaan buah non-destruktif yang akurat untuk manajemen hasil panen.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Otomatisasi pemantauan hasil kebun dan pemanenan buah memerlukan sistem penglihatan komputer yang tidak hanya mampu mendeteksi keberadaan buah, tetapi juga mengidentifikasi lokasi spasial 3D buah tersebut secara presisi. Informasi spasial 3D ini sangat penting bagi manipulator robotik untuk merencanakan lintasan gerak memetik buah tanpa merusak struktur tanaman. Sebelum penelitian ini, sebagian besar metode deteksi berbasis pembelajaran mendalam berfokus pada deteksi 2D pada citra RGB tunggal. Pendekatan 2D ini kehilangan informasi kedalaman sehingga tidak memadai untuk aplikasi pemanenan robotik langsung.

Untuk mendapatkan informasi 3D, pendekatan sebelumnya menggunakan sensor kedalaman aktif seperti kamera RGB-D berbasis *Time-of-Flight* (ToF) atau sensor LiDAR. Namun, sensor aktif ini memiliki keterbatasan serius di lingkungan pertanian luar ruangan. Spektrum inframerah dari radiasi sinar matahari langsung mengganggu sensor penerima inframerah pada kamera RGB-D aktif, menghasilkan data kedalaman yang bising atau tidak lengkap. Di sisi lain, biaya perangkat keras LiDAR sangat mahal untuk penerapan praktis. Metode fotogrametri pasif seperti stereo konvensional juga rentan gagal akibat oklusi daun yang padat dan variasi pencahayaan alami di kebun buah. Diperlukan metode lokalisasi 3D pasif yang tangguh terhadap gangguan luar ruangan dan oklusi.

## Ide Utama
Gagasan utama makalah ini adalah menggabungkan kemampuan representasi visual Mask R-CNN dengan konsistensi geometris multi-sudut yang disediakan oleh rekonstruksi SfM pasif. Informasi deteksi dikumpulkan dari berbagai sudut pandang kamera saat bergerak mengitari pohon apel untuk melengkapi data spasial yang hilang akibat oklusi.

Alur data dari sistem ini menerima masukan berupa urutan citra RGB dari pohon apel. Citra diproses secara paralel untuk menghasilkan masker piksel 2D buah melalui Mask R-CNN dan merekonstruksi awan titik 3D melalui SfM. Masker piksel 2D diproyeksikan kembali (*back-projected*) ke ruang 3D menggunakan parameter kamera hasil kalibrasi SfM untuk membentuk klaster titik 3D. Klaster titik dari berbagai citra yang saling tumpang tindih digabungkan untuk merepresentasikan satu buah apel fisik yang unik. Terakhir, fitur geometris dari klaster 3D ini diekstraksi dan diklasifikasikan menggunakan SVM biner guna menyaring deteksi palsu yang disebabkan oleh proyeksi menyimpang pada daun atau tanah.

## Cara Kerja Langkah demi Langkah
Metodologi lokalisasi 3D ini terdiri dari serangkaian langkah terintegrasi yang memindahkan representasi objek dari piksel 2D ke ruang metrik 3D:

```
  [ Citra RGB Multi-view ] ──┬──> [ SfM Photogrammetry ] ──> [ 3D Point Cloud ]
                             │                                       │
                             └──> [ Mask R-CNN (ResNet-101) ]        │
                                         │                           │
                                         ▼                           │
                                 [ 2D Pixel Masks ]                  │
                                         │                           │
                                         ▼                           │
                                 [ Proyeksi 2D-3D ] <────────────────┘
                                         │
                                         ▼
                             [ 3D Point Clusters ]
                                         │
                                         ▼
                              [ Klasterisasi 3D ]
                                         │
                                         ▼
                            [ Ekstraksi Fitur 3D ]
                            (P, V, delta, Psi)
                                         │
                                         ▼
                            [ Penapisan SVM Biner ]
                                         │
                                         ▼
                            [ Posisi 3D Buah Valid ]
```

### Segmentasi Instan 2D Berbasis Mask R-CNN
Deteksi biner 2D dilakukan menggunakan jaringan saraf tiruan Mask R-CNN dengan *backbone* ResNet-101 dan *Feature Pyramid Network* (FPN). Jaringan ini memprediksi kelas, kotak pembatas (*bounding box*), skor keyakinan (*confidence score*), dan masker biner tingkat piksel untuk setiap buah. Sebelum pemrosesan, citra beresolusi tinggi dipotong menjadi 24 sub-gambar berukuran $1024 \times 1024$ piksel. Langkah pemotongan ini krusial untuk mencegah degradasi detail buah berukuran kecil akibat kompresi ukuran input standar pada model. Jaringan dilatih melalui penyetelan halus (*fine-tuning*) pada 288 citra beranotasi dari dataset Fuji-SfM setelah diinisialisasi dengan bobot COCO. Hasil deteksi direpresentasikan sebagai masker piksel $M_{ij}$ untuk citra ke-$i$ dan objek buah ke-$j$.

### Rekonstruksi 3D dengan Structure-from-Motion (SfM)
Secara paralel, 582 citra gerak sekuensial dari 11 pohon apel Fuji diproses menggunakan perangkat lunak Agisoft Metashape Professional. Algoritma SfM mencocokkan titik fitur lintas gambar untuk mengestimasi matriks kalibrasi intrinsik dan pose ekstrinsik kamera untuk setiap citra. Selanjutnya, algoritma *Multi-View Stereo* (MVS) membangun awan titik padat yang merekonstruksi struktur geometri kanopi pohon dalam skala spasial dunia nyata. Setiap titik dalam awan titik memiliki koordinat global ($X, Y, Z$).

### Proyeksi Masker 2D ke Awan Titik 3D
Setiap masker piksel 2D hasil deteksi Mask R-CNN diproyeksikan ke ruang 3D. Dari pusat optik kamera untuk citra $i$, sinar proyeksi dihitung melewati setiap koordinat piksel di dalam masker $M_{ij}$. Titik-titik 3D pada awan titik padat yang terletak dalam batas jarak ambang tertentu dari garis sinar proyeksi ditandai sebagai titik milik buah tersebut. Proses ini menghasilkan awan titik terproyeksi untuk setiap objek buah yang terdeteksi pada citra.

### Klasterisasi Spasial dan Penggabungan Multi-Sudut
Karena satu buah apel fisik dipotret dari beberapa citra dengan sudut pandang berbeda, titik-titik proyeksi dari berbagai citra akan terakumulasi pada koordinat spasial 3D yang sama. Algoritma klasterisasi spasial berbasis jarak Euclidean diterapkan untuk menggabungkan titik-titik yang saling berdekatan menjadi satu klaster kandidat buah 3D tunggal. Untuk menjamin konsistensi visual, diterapkan aturan penyaringan ketat: suatu klaster 3D hanya dianggap sebagai kandidat buah valid jika didukung oleh deteksi Mask R-CNN pada minimal 2 citra yang berbeda. Klaster yang hanya didukung oleh satu citra langsung dibuang untuk mengeliminasi kesalahan deteksi acak.

### Ekstraksi Fitur Geometris 3D
Untuk setiap klaster kandidat buah 3D yang lolos penyaringan konsistensi, dihitung empat fitur geometris dari sebaran titik-titik pembentuknya:
1. Jumlah titik ($P$): Total titik 3D yang membentuk klaster.
2. Volume ($V$): Volume amplop cembung (*convex hull*) dari klaster titik 3D.
3. Kepadatan titik ($\delta$): Rasio kerapatan yang dihitung sebagai $\delta = P / V$.
4. Sferisitas ($\Psi$): Ukuran kebulatan klaster yang dihitung dari nilai eigen normalized ($\lambda_1, \lambda_2, \lambda_3$ dengan $\lambda_1 \ge \lambda_2 \ge \lambda_3$ dan $\lambda_1 + \lambda_2 + \lambda_3 = 1$) dari matriks kovarians klaster titik 3D:
   $$\Psi = 27 \cdot \lambda_1 \cdot \lambda_2 \cdot \lambda_3$$
   Klaster buah apel asli yang mendekati bentuk bola memiliki nilai eigen yang seimbang sehingga nilai sferisitas $\Psi$ mendekati 1. Klaster palsu dari dahan atau daun cenderung memiliki nilai eigen yang tidak seimbang (satu atau dua dimensi dominan), menghasilkan nilai $\Psi$ mendekati 0.

### Penapisan False Positive dengan SVM
Fitur empat dimensi ($P, V, \delta, \Psi$) diinput to model SVM biner dengan kernel *Radial Basis Function* (RBF). Model SVM mengklasifikasikan setiap klaster ke dalam kelas buah sejati (*true positive*) atau deteksi palsu (*false positive*). Klaster yang diklasifikasikan sebagai buah sejati dipertahankan, dan koordinat rata-rata dari seluruh titik dalam klaster dihitung sebagai koordinat pusat 3D final buah apel tersebut.

## Eksperimen dan Hasil
Eksperimen dilakukan di kebun apel komersial pada 11 pohon apel Fuji (Malus domestica Borkh. cv. Fuji) yang memiliki total 1.455 buah apel asli yang dihitung manual sebagai acuan (*ground truth*). Performa deteksi 2D Mask R-CNN dibandingkan secara langsung dengan performa sistem lokalisasi 3D terintegrasi (Mask R-CNN + SfM + SVM).

Hasil kuantitatif eksperimen dirangkum dalam tabel berikut:

| Pendekatan | Presisi (*Precision*) | Sensitivitas (*Recall*) | F1-Score |
|---|---|---|---|
| Deteksi 2D (Mask R-CNN saja) | 0,762 (76,2%) | 0,878 (87,8%) | 0,816 (81,6%) |
| Lokasi 3D (Mask R-CNN + SfM + SVM) | 0,857 (85,7%) | 0,906 (90,6%) | 0,881 (88,1%) |

Integrasi geometri 3D dan penapisan SVM memberikan peningkatan performa yang signifikan. Presisi sistem meningkat sebesar 9,5% (dari 0,762 menjadi 0,857), membuktikan bahwa fitur geometris 3D dan klasifikasi SVM sangat efektif dalam menyaring deteksi palsu tingkat piksel. Sensitivitas (*recall*) juga meningkat sebesar 2,8% (dari 0,878 menjadi 0,906) karena buah yang mengalami oklusi parsial pada satu citra tetap dapat dikenali dari citra lain lalu digabungkan dengan sukses di ruang 3D. Secara keseluruhan, F1-score sistem meningkat dari 0,816 menjadi 0,881.

## Kelebihan dan Keterbatasan
Kelebihan utama dari metodologi ini adalah kemampuannya melakukan lokalisasi 3D buah secara pasif tanpa bergantung pada sensor kedalaman aktif. Hal ini memberikan ketangguhan tinggi terhadap kebisingan data akibat gangguan radiasi matahari luar ruangan yang sering merusak performa sensor RGB-D aktif berbasis inframerah. Penggunaan informasi multi-sudut juga secara alami mengatasi masalah oklusi parsial pada buah. Selain itu, publikasi dataset Fuji-SfM menyediakan kontribusi berharga bagi komunitas riset pertanian presisi.

Dari sisi rekayasa komputasi, keterbatasan utama sistem ini adalah tingginya beban komputasi proses SfM. Pencocokan fitur dan rekonstruksi awan titik padat memerlukan waktu pemrosesan yang lama (beberapa menit hingga beberapa jam per pohon), sehingga metode ini tidak dapat dioperasikan secara waktu-nyata (*real-time*) untuk robot pemanen. Secara konseptual, keandalan SfM sangat rentan terhadap perubahan kondisi lingkungan fisik selama pengambilan citra. Hembusan angin yang menggerakkan daun atau pergeseran bayangan matahari dapat merusak konsistensi geometri antar-citra, sehingga menurunkan kualitas rekonstruksi 3D dan akurasi lokalisasi buah.

## Kaitan dengan Bab Lain
Metodologi dalam bab ini mewarisi kebutuhan deteksi objek buah 2D pada citra RGB yang dibahas pada [Bab 120 (MangoYOLO)](./120%20-%202019%20-%20MangoYOLO%20-%20Pertanian.md), [Bab 121 (Apple Detection Improved YOLOv3)](./121%20-%202019%20-%20Apple%20Detection%20%28Improved%20YOLOv3%29%20-%20Pertanian.md), dan [Bab 122 (Apple Flower Detection Pruned YOLOv4)](./122%20-%202020%20-%20Apple%20Flower%20Detection%20%28Pruned%20YOLOv4%29%20-%20Pertanian.md). Ketiga bab tersebut menggunakan varian YOLO untuk deteksi 2D pada tingkat piksel gambar. Namun, metode-metode tersebut tidak menyediakan koordinat spasial 3D yang mutlak diperlukan untuk operasi lengan robot pemenang.

Untuk mengatasi kehilangan informasi spasial tersebut, [Bab 123 (Apple Detection RGB+Depth Faster R-CNN)](./123%20-%202020%20-%20Apple%20Detection%20RGB+Depth%20%28Faster%20R-CNN%29%20-%20Pertanian.md) menggunakan sensor kedalaman aktif (RGB-D) untuk mendapatkan data kedalaman buah secara langsung. Bab 124 (metode Gené-Mola dkk. ini) hadir sebagai alternatif pasif yang menyelesaikan kelemahan sensor aktif di Bab 123 terhadap gangguan cahaya matahari luar ruangan dengan mengadopsi rekonstruksi geometri SfM dari citra multi-sudut.

Meskipun demikian, lambatnya komputasi rekonstruksi SfM di Bab 124 membuatnya kurang cocok untuk memandu robot panen instan secara *real-time* seperti pada [Bab 125 (Iceberg Lettuce Harvesting Robot)](./125%20-%202020%20-%20Iceberg%20Lettuce%20Harvesting%20Robot%20-%20Pertanian.md) dan [Bab 126 (Automated Fruit Harvesting Robot Onishi dkk.)](./126%20-%202019%20-%20Automated%20Fruit%20Harvesting%20Robot%20%28Onishi%20dkk.%29%20-%20Pertanian.md) yang membutuhkan keputusan pemetikan instan. Sebagai alternatif lain, [Bab 127 (Fruit Detection & 3D Visualisation Kang & Chen)](./127%20-%202020%20-%20Fruit%20Detection%20%26%203D%20Visualisation%20%28Kang%20%26%20Chen%29%20-%20Pertanian.md) berupaya menjembatani celah kecepatan pemrosesan ini dengan memanfaatkan sensor RGB-D modern dan algoritma visualisasi 3D real-time.

## Poin untuk Sitasi
Kunci BibTeX untuk bab ini adalah `genemola2020fruit3d`. Ringkasan yang aman dikutip dalam tinjauan pustaka akademik adalah:
"Gené-Mola dkk. mengusulkan metode deteksi dan lokalisasi buah 3D pasif dengan mengintegrasikan segmentasi instan Mask R-CNN pada citra RGB 2D dengan awan titik hasil rekonstruksi fotogrametri *Structure-from-Motion* (SfM) multi-sudut. Penapisan klaster titik 3D menggunakan Support Vector Machine (SVM) biner berhasil meningkatkan F1-score deteksi dari 0,816 menjadi 0,881 serta mengeliminasi kesalahan deteksi palsu akibat oklusi dedaunan."

Catatan verifikasi data: Angka-angka hasil utama (F1-score 3D 0,881, presisi 0,857, recall 0,906) telah diverifikasi secara akurat dari naskah publikasi resmi. Pengujian dilakukan pada 11 pohon apel Fuji dengan total populasi 1.455 buah apel. Keterbatasan sistem berupa waktu komputasi yang tinggi untuk rekonstruksi SfM dikonfirmasi oleh penulis sebagai batasan utama untuk penerapan waktu-nyata (*real-time*).
