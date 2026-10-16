# A method for organs classification and fruit counting on pomegranate trees based on multi-features fusion and support vector machine by 3D point cloud

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2021method` |
| Judul asli | A method for organs classification and fruit counting on pomegranate trees based on multi-features fusion and support vector machine by 3D point cloud |
| Penulis | Zhang, Chunlong; Zhang, Kaifei; Ge, Luzhen; Zou, Kunlin; Wang, Song; Zhang, Junxiong; Li, Wei |
| Tahun | 2021 |
| Venue | Scientia Horticulturae |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | pomegranate |

## Tautan Akses
- PDF: [zhang2021method.pdf](../pdf/zhang2021method.pdf)
- DOI resmi: https://doi.org/10.1016/j.scienta.2020.109791

## Gambaran Umum
Makalah ini mengusulkan metode klasifikasi organ dan penghitungan buah pada pohon delima (*pomegranate*) dari awan titik 3D seluruh pohon. Awan titik diperoleh dengan kamera RGB-D Intel RealSense D435, dipra-olah, lalu setiap titik diklasifikasikan menjadi buah, cabang, atau daun oleh *Support Vector Machine* (SVM) dengan kernel RBF berdasarkan fitur warna (R, G, B) dan fitur bentuk dari nilai eigen matriks kovarians tetangga. Label disehaluskan dengan *K-nearest neighbor* (KNN) berbobot jarak Euklides, kemudian buah dihitung dengan pengelompokan hierarkis aglomeratif-divisif.

Data berasal dari enam pohon delima fase matang di China Agricultural University, Beijing, 20 Juli sampai 26 Agustus 2019. Klasifikasi SVM dengan warna dan bentuk dua skala menghasilkan AUC kurva presisi-*recall* 0,75307 untuk buah, 0,99701 untuk non-buah, 0,34601 untuk cabang, dan 0,97985 untuk daun. Pada penghitungan buah, hasil akhir adalah *recall* 87,74%, presisi 78,15%, dan skor F1 82,67% terhadap 106 buah acuan; metode ini memperoleh *recall* lebih tinggi daripada pengelompokan aglomeratif saja (80,19%).

Penghitungan dilakukan pada awan titik satu rekonstruksi, sehingga buah yang terlihat dari banyak sudut sudah menyatu pada ruang 3D yang sama sebelum dihitung.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Klasifikasi organ dan penghitungan buah penting untuk pekerjaan hortikultura (pengenalan tahap tumbuh, estimasi hasil, pemetikan robotik, penyemprotan presisi, pemangkasan). Metode berbasis citra 2D terbatas oleh pencahayaan yang tidak terkendali di alam terbuka, fitur bentuk yang tidak lengkap, dan oklusi buah. Metode berbasis pembelajaran mendalam, menurut penulis, memerlukan banyak data dan waktu pelatihan.

Awan titik 3D memuat informasi bentuk yang lebih lengkap. Penulis mencatat tiga cara memperolehnya: pemindai laser atau LiDAR yang mahal, kamera RGB-D berbiaya rendah dengan jangkauan kurang dari sepuluh meter, dan rekonstruksi dari banyak citra. Penulis menyatakan bahwa metode 3D sebelumnya umumnya menyasar sebagian pohon, sedangkan makalah ini menyasar seluruh pohon.

## Ide Utama
Fitur warna digabung dengan fitur bentuk multi-skala yang menganggap buah sebagai "bola", cabang sebagai "silinder", dan daun sebagai "datar". Hasil klasifikasi per titik yang masih bising dihaluskan dengan KNN berbobot, lalu klaster titik berlabel buah dihitung sebagai buah. Pengelompokan dua tahap (bawah-atas lalu pemecahan) dipakai agar klaster besar yang memuat beberapa buah dipecah.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data
Awan titik tiga dimensi enam pohon delima fase matang direkonstruksi dengan RealSense D435 menggunakan perangkat lunak Dot3D, dan algoritma dijalankan di MATLAB R2019a pada PC Windows 10 dengan RAM 16 GB dan Intel Core i7-8750. Posisi dan jumlah sudut pengambilan, serta jumlah bingkai RGB-D, tidak dilaporkan.

### 2. Pra-pengolahan awan titik
Tiga langkah: (1) latar belakang dihapus manual dengan MeshLab, (2) penurunan sampel (*downsampling*) dengan *voxel grid filter* berukuran langkah seragam 8 mm, dan (3) penyaringan pencilan. Awan titik asli berisi 13.244.046 titik, menjadi 7.116.143 titik setelah latar dihapus, dan 961.003 titik setelah pra-pengolahan.

### 3. Ekstraksi fitur warna dan bentuk
Fitur warna adalah kanal R, G, dan B. Fitur bentuk dihitung dari matriks kovarians koordinat tetangga tiap titik (diindeks dengan *k-d tree*), dengan tiga nilai eigen $d_1, d_2, d_3$:

$$\epsilon_1 = \frac{d_1-d_2}{d_1+d_2+d_3},\quad \epsilon_2 = \frac{2(d_2-d_3)}{d_1+d_2+d_3},\quad \epsilon_3 = \frac{3 d_3}{d_1+d_2+d_3}.$$

Tiga skala tetangga dipakai: $k_1=200$, $k_2=400$, $k_3=800$. Gabungan warna dan fitur bentuk membentuk vektor fitur 12 dimensi pada konfigurasi tiga skala.

### 4. Klasifikasi organ dengan SVM
Digunakan libsvm 3.2.3 dengan kernel RBF. Set data berisi 961.003 titik yang dilabeli manual menjadi buah, cabang, dan daun. Sebanyak 159.613 titik dipakai sebagai data latih dan 801.390 titik sebagai data uji. Penulis membandingkan fitur warna saja, serta warna dengan bentuk satu, dua, dan tiga skala.

### 5. Penghalusan KNN berbobot jarak
Label tiap titik dikoreksi berdasarkan tetangganya dengan bobot yang bergantung pada jarak (Persamaan 5). Nilai $k = 20$, 50, dan 100 dibandingkan; $k = 50$ dipilih.

### 6. Penghitungan dengan pengelompokan aglomeratif-divisif
Pengelompokan hierarkis aglomeratif dengan ambang jarak Euklides menggabungkan titik menjadi klaster, dengan ambang yang bergantung pada jumlah titik klaster. Klaster yang jumlah titiknya melebihi ambang dipecah oleh pengelompokan divisif menjadi klaster yang lebih kecil. Pengelompokan aglomeratif saja dijadikan pembanding.

## Eksperimen dan Hasil
Penilaian klasifikasi memakai kurva presisi-*recall* dan luas di bawah kurva (AUC), sedangkan penghitungan memakai presisi, *recall*, dan skor F1.

Klasifikasi organ (Tabel 1, AUC kurva PR):

| Organ | Warna saja | Bentuk 1 skala + warna | Bentuk 2 skala + warna | Bentuk 3 skala + warna |
|---|---|---|---|---|
| Buah | 0,72134 | 0,64221 | 0,75307 | 0,57647 |
| Cabang | 0,21849 | 0,28185 | 0,34601 | 0,29705 |
| Daun | 0,96920 | 0,97044 | 0,97985 | 0,96705 |
| Non-buah | 0,99516 | 0,99543 | 0,99701 | 0,99335 |

Konfigurasi warna dengan bentuk dua skala ($k_1=200$, $k_2=400$) terbaik pada semua kategori. Cabang merupakan kelas terlemah, yang dikaitkan penulis dengan ketimpangan jumlah titik cabang dan non-cabang serta fitur warna cabang yang lemah. Dibandingkan dengan metode Color-FPFH pada pohon apel dari penelitian lain, metode ini lebih tinggi untuk daun dan lebih rendah untuk buah dan cabang.

Penghitungan buah dengan penghalusan (Tabel 2), dengan 106 buah acuan:

| Kondisi | Positif | Negatif | *Recall* (%) | Presisi (%) | F1 (%) |
|---|---|---|---|---|---|
| Sebelum penghalusan | 85 | 35 | 80,19 | 70,83 | 75,23 |
| Setelah, $k=20$ | 87 | 33 | 82,08 | 72,50 | 76,99 |
| Setelah, $k=50$ | 93 | 26 | 87,74 | 78,15 | 82,67 |
| Setelah, $k=100$ | 90 | 31 | 84,91 | 74,38 | 79,30 |

Perbandingan metode pengelompokan (Tabel 3): pengelompokan aglomeratif saja memberikan 85 positif dan 39 negatif dengan *recall* 80,19%, presisi 68,55%, dan F1 73,91%; aglomeratif-divisif memberikan 93 positif dan 26 negatif dengan *recall* 87,74%, presisi 78,15%, dan F1 82,67%. Penulis menyatakan peningkatan *recall* 7,55 poin persentase. Dibandingkan DBSCAN pada deteksi tunas anggur oleh peneliti lain (presisi 100%, *recall* 45%), metode ini memiliki presisi lebih rendah tetapi *recall* lebih tinggi; kedua tugas dan data berbeda.

## Kelebihan dan Keterbatasan
Kelebihan menurut penulis: menyasar seluruh pohon sehingga informasi lebih lengkap, memakai kamera RGB-D berbiaya rendah, fitur bentuk yang tidak peka terhadap pencahayaan, dan *recall* penghitungan yang tinggi.

Keterbatasan yang dinyatakan penulis: hasil klasifikasi cabang buruk (AUC 0,34601) karena ketimpangan jumlah titik dan warna cabang yang mirip sebagian buah; ukuran daun yang mirip sebagian buah menyebabkan kesalahan klasifikasi bentuk; skala tetangga penghalusan yang besar menghilangkan buah kecil atau tertutup, sedangkan skala kecil kurang menghaluskan; dan akurasi awan titik perlu ditingkatkan pada penelitian mendatang.

Menurut pembacaan ringkasan ini, sampel hanya enam pohon pada satu lokasi dan satu musim, tanpa ulangan atau validasi silang antarpohon, dan asal angka acuan 106 buah tidak dijelaskan (misalnya apakah dari hitung manual di pohon). Pembagian latih-uji dilakukan pada titik dari awan yang sama dan tidak dinyatakan terpisah per pohon. Pra-pengolahan menghapus latar secara manual, sehingga alur tidak sepenuhnya otomatis. Abstrak menyebut "akurasi" 0,75 untuk buah, padahal isi makalah menyebut nilai tersebut sebagai AUC.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat dari banyak sudut hanya melalui rekonstruksi 3D tunggal: awan titik dibangun dari rekaman yang mengelilingi pohon, dan penghitungan dilakukan sebagai pengelompokan titik buah pada ruang 3D. Dengan demikian identitas lintas pandang dijamin oleh koordinat 3D bersama, bukan oleh pencocokan antarcitra. Langkah penggabungan klaster yang terlalu besar dan pemecahannya adalah mekanisme untuk buah yang saling menempel, bukan untuk buah yang sama pada beberapa sisi.

Hitungan tidak dilaporkan per kelas kematangan; semua pohon berada pada fase matang. Acuan hitung berupa 106 buah ("Fruit" pada Tabel 2 dan 3); sumbernya (panen, hitung manual, atau anotasi awan titik) tidak dinyatakan pada teks. Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan menyatukan seluruh sisi pohon dalam satu awan titik lalu menghitung klaster tandan. Kendalanya adalah tinggi pohon sawit, jangkauan RealSense D435, dan lamanya rekonstruksi, yang tidak dibahas pada makalah ini.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `zhang2021method`.

Zhang dkk. mengusulkan klasifikasi organ pohon delima dari awan titik RGB-D dengan SVM berfitur warna dan bentuk multi-skala, penghalusan KNN berbobot jarak, dan penghitungan buah dengan pengelompokan hierarkis aglomeratif-divisif. Pada enam pohon dengan 106 buah acuan, penghitungan memperoleh *recall* 87,74%, presisi 78,15%, dan F1 82,67%, lebih tinggi daripada pengelompokan aglomeratif saja (*recall* 80,19%, presisi 68,55%).

Catatan verifikasi data: AUC klasifikasi berasal dari Tabel 1; hasil penghitungan dari Tabel 2 dan Tabel 3; jumlah titik dari bagian 3.1 dan bagian 2.2.3; jumlah pohon dan periode akuisisi dari bagian 2.1. Kolom "Positive" dan "Negative" pada Tabel 2 dan 3 tidak didefinisikan secara eksplisit; dari angka yang tertulis (93 positif dan 26 negatif dengan presisi 78,15%) dapat dilihat bahwa "Negative" tampak berarti jumlah deteksi palsu, tetapi ini adalah penafsiran. Pembagian titik antarpohon pada data latih dan uji, serta cara memperoleh angka 106 buah, tidak dapat diverifikasi dari teks. Teks ekstraksi terbaca dengan baik, kecuali rumus yang tersusun per baris.
