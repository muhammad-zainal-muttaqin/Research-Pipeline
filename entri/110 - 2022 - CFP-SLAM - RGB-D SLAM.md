# 110 - CFP-SLAM: A Real-Time Visual SLAM Based on Coarse-to-Fine Probability in Dynamic Environments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hu2022cfpslam` |
| Judul asli | CFP-SLAM: A Real-Time Visual SLAM Based on Coarse-to-Fine Probability in Dynamic Environments |
| Penulis | Xinggang Hu, Yunzhou Zhang, Zhenzhong Cao, Rong Ma, Yanmin Wu, Zhiqiang Deng, Wenkai Sun |
| Tahun | 2022 |
| Venue | IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2022), Kyoto, hlm. 4399–4406 |
| Tema | RGB-D SLAM |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2202.01938
- **DOI (IEEE Xplore):** https://ieeexplore.ieee.org/document/9981826/
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=CFP-SLAM%3A%20A%20Real-Time%20Visual%20SLAM%20Based%20on%20Coarse-to-Fine%20Probability%20in%20Dynamic%20Environments&sort=relevance

## Gambaran Umum

CFP-SLAM (*Coarse-to-Fine Probability SLAM*) adalah sistem *visual SLAM* (*Simultaneous Localization and Mapping* — pelokalan kamera dan pemetaan lingkungan yang dilakukan serentak) untuk lingkungan dengan objek bergerak. Masalah yang dipecahkan adalah bagaimana menilai keandalan titik-titik fitur di tengah adegan dinamis tanpa membuang seluruhnya secara biner (statis atau dinamis, tanpa nilai antara). Gagasan utamanya adalah menghitung sebuah "probabilitas statis" bertingkat, dimulai dari objek yang dideteksi jaringan saraf, diturunkan ke setiap titik kunci (*keypoint* — titik citra yang khas dan mudah dicocokkan antar-*frame*) di dalam kotak objek tersebut, lalu ke titik peta 3D yang bersangkutan. Nilai probabilitas ini dipakai sebagai bobot pada optimasi pose kamera, bukan sebagai penyaring biner.

Pada rangkaian uji dinamis-tinggi TUM RGB-D `fr3/walking_xyz`, makalah melaporkan galat trayektori absolut (ATE) sekitar 0,014 m, jauh di bawah ORB-SLAM2 (basis sistem ini) yang mencapai 0,72 m pada urutan yang sama, dan lebih baik daripada DS-SLAM (sekitar 0,025 m). Sistem berjalan mendekati *real-time*, dilaporkan sekitar 42,7 milidetik per *frame* (setara 23 *frame per second*/FPS) untuk versi penuh, dengan varian ringkas yang lebih cepat. Bab ini melanjutkan garis SLAM dinamis berbasis deteksi objek yang dirintis DynaSLAM (bab 108) dan DS-SLAM (bab 109), dengan penekanan pada pembobotan probabilistik bertahap alih-alih penghapusan area dinamis secara langsung.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Algoritme SLAM klasik seperti ORB-SLAM2 (bab 107) mengasumsikan lingkungan statis: seluruh titik fitur yang teramati dianggap tetap posisinya di dunia nyata, sehingga pergerakannya di citra murni disebabkan gerak kamera. Ketika ada objek bergerak — orang berjalan, kursi didorong — asumsi ini dilanggar, dan titik fitur pada objek tersebut menyesatkan estimasi pose kamera karena pergerakannya bercampur antara gerak kamera dan gerak objek.

Generasi SLAM dinamis sebelumnya menangani masalah ini dengan menghapus seluruh wilayah yang dicurigai dinamis. DynaSLAM memakai segmentasi Mask R-CNN untuk menandai piksel manusia dan menghilangkan seluruh titik fitur di dalamnya sebelum estimasi pose berjalan. DS-SLAM menandai objek berpotensi dinamis dengan SegNet lalu memverifikasinya dengan kendala geometri sebelum membuang titik yang lolos verifikasi. Pendekatan penghapusan biner semacam ini memiliki dua kelemahan. Pertama, objek yang berpotensi bergerak tidak selalu benar-benar bergerak pada saat pengambilan citra — seseorang yang sedang duduk diam tetap ditandai "manusia" dan seluruh fitur di tubuhnya terbuang, padahal fitur tersebut statis dan berguna untuk pelokalan. Kedua, keputusan biner sepenuhnya bergantung pada akurasi kotak atau masker deteksi; kesalahan deteksi (kotak terlalu besar, mencakup latar belakang statis di sekitarnya) ikut membuang fitur statis yang seharusnya dipertahankan. Masalah yang belum terpecahkan pada generasi ini adalah bagaimana memanfaatkan derajat keyakinan dinamis secara bertingkat, bukan sekadar ya/tidak.

## Ide Utama

Gagasan inti CFP-SLAM adalah mengganti keputusan biner "dinamis vs statis" dengan sebuah nilai probabilitas kontinu antara 0 dan 1 untuk setiap titik fitur, dihitung melalui dua tahap berurutan: tahap kasar (*coarse*) pada tingkat objek, dan tahap halus (*fine*) pada tingkat titik kunci individual. Objek yang dideteksi jaringan saraf memberi perkiraan awal yang murah secara komputasi tetapi kasar resolusinya (satu kotak mencakup banyak titik dengan sifat gerak yang mungkin berbeda-beda). Tahap halus kemudian mengoreksi perkiraan itu titik demi titik memakai kendala geometri, sehingga titik statis di dalam kotak objek dinamis (misalnya latar di belakang orang yang tercakup kotak deteksi) tidak ikut terbuang, dan titik yang benar-benar bergerak tetap diberi bobot rendah. Probabilitas akhir dipakai sebagai bobot pada fungsi galat optimasi pose: titik berprobabilitas statis tinggi memengaruhi estimasi pose lebih besar, titik berprobabilitas rendah nyaris diabaikan tanpa perlu dihapus secara eksplisit.

## Cara Kerja Langkah demi Langkah

### Modul Deteksi dan Kompensasi

CFP-SLAM dibangun di atas kerangka ORB-SLAM2, dengan modul semantik tambahan berbasis YOLOv5s (varian ringkas dari keluarga detektor YOLO, dijelaskan pada bab 001 dan penerusnya) yang mendeteksi objek berpotensi dinamis pada tiap *frame* RGB. Karena detektor tidak selalu berhasil mendeteksi objek pada setiap *frame* (misalnya saat objek sebagian tertutup), sistem menambahkan kompensasi memakai *Extended Kalman Filter* (EKF — penduga keadaan rekursif yang memprediksi posisi kotak deteksi pada *frame* berikutnya berdasarkan riwayat gerak, lalu mengoreksinya bila deteksi baru tersedia) dan algoritme Hungarian (metode optimasi kombinatorial yang mencari pemasangan satu-ke-satu optimal) untuk mencocokkan kotak deteksi antar-*frame* yang berurutan. Dengan kompensasi ini, kotak objek tetap tersedia meski deteksi sesaat gagal, sehingga probabilitas dinamis tidak terputus di tengah lintasan objek.

### Tahap Kasar: Probabilitas Tingkat Objek

Untuk tiap objek yang terdeteksi, sistem menghitung galat konsistensi geometris memakai kombinasi *optical flow* (estimasi pergerakan piksel antar dua *frame* berurutan) dan galat epipolar (ukuran seberapa jauh sebuah titik menyimpang dari batasan geometris yang berlaku bila titik itu statis dan hanya kamera yang bergerak). Galat ini diuji terhadap distribusi *chi-square* (distribusi statistik yang dipakai di sini untuk menilai apakah besar galat tersebut wajar bagi titik statis atau menandakan gerak independen) untuk menghasilkan satu nilai probabilitas statis per objek. Objek dengan probabilitas ≤ 0,9 diklasifikasikan "dinamis tinggi", sedangkan yang di atas ambang itu diklasifikasikan "dinamis rendah". Untuk memisahkan piksel objek dari latar di sekitarnya pada peta kedalaman, tahap ini memakai DBSCAN (*Density-Based Spatial Clustering of Applications with Noise* — algoritme pengelompokan berbasis kepadatan titik yang tidak memerlukan jumlah kelompok ditentukan di muka) sehingga batas objek pada citra kedalaman lebih presisi daripada sekadar kotak persegi hasil deteksi. Probabilitas objek ini menjadi nilai awal bagi seluruh titik kunci yang berada di dalamnya.

### Tahap Halus: Probabilitas Tingkat Titik Kunci

Nilai awal dari tahap kasar kemudian disempurnakan per titik kunci memakai dua kendala geometris tambahan. Kendala proyeksi mengukur galat reproyeksi (selisih posisi sebuah titik peta 3D yang diproyeksikan ke citra dibandingkan posisi pengamatan sebenarnya) dan mengubahnya menjadi nilai probabilitas lewat fungsi sigmoid (fungsi berbentuk S yang memetakan bilangan real ke rentang 0–1 secara mulus). Kendala epipolar memverifikasi ulang konsistensi geometris tiap titik secara individual, lebih rinci daripada verifikasi tingkat objek pada tahap kasar. Kedua kendala digabungkan dengan strategi berbeda bergantung status objek induknya (dinamis tinggi atau rendah), lalu probabilitas titik kunci diperbarui secara kumulatif seiring waktu ketika titik yang sama teramati pada beberapa *frame* berturut-turut.

Alur keseluruhan dari citra masukan hingga pose kamera dapat diringkas sebagai berikut.

```
citra RGB-D masuk
        |
        v
deteksi objek (YOLOv5s) -- kompensasi (EKF + Hungarian)
        |  kotak objek berpotensi dinamis
        v
TAHAP KASAR (tingkat objek)
  optical flow + galat epipolar (uji chi-square)
  -> probabilitas objek; <=0,9 dinamis tinggi, >0,9 dinamis rendah
  -> DBSCAN memisahkan batas objek pada peta kedalaman
        |  probabilitas awal tiap titik kunci di dalam objek
        v
TAHAP HALUS (tingkat titik kunci)
  kendala proyeksi (sigmoid atas galat reproyeksi)
  kendala epipolar per titik, digabung sesuai status objek induk
        |  probabilitas titik kunci diperbarui
        v
pembobotan titik dalam optimasi pose (bundle adjustment)
        |
        v
   pose kamera + peta titik berbobot probabilitas statis
```

Titik kunci dan titik peta yang telah memiliki bobot ini kemudian dimasukkan ke *bundle adjustment* (optimasi bersama pose kamera dan posisi titik peta yang meminimalkan total galat reproyeksi) mengikuti kerangka ORB-SLAM2, tetapi dengan kontribusi tiap titik pada fungsi galat dikalikan bobot probabilitas statisnya, bukan dengan opsi hadir/tidak hadir.

## Eksperimen dan Hasil

Evaluasi dilakukan pada TUM RGB-D, kumpulan data benchmark standar untuk SLAM RGB-D yang menyediakan lintasan kebenaran (*ground truth*) dari sistem penangkap gerak eksternal. Makalah menguji pada delapan rangkaian: empat rangkaian dinamis rendah (kategori "sitting", subjek duduk dengan gerakan terbatas) dan empat rangkaian dinamis tinggi (kategori "walking", subjek berjalan penuh di dalam ruang). Metrik utamanya adalah ATE (*Absolute Trajectory Error* — galat antara lintasan kamera yang diestimasi dan lintasan kebenaran setelah keduanya disejajarkan, dilaporkan sebagai *root mean square error*/RMSE dalam meter) dan RPE (*Relative Pose Error* — galat pose relatif pada interval waktu tetap, mengukur drift lokal).

Pada rangkaian dinamis tinggi `fr3/walking_xyz`, ATE CFP-SLAM tercatat sekitar 0,014 m, dibandingkan ORB-SLAM2 tanpa penanganan dinamis sebesar 0,72 m dan DS-SLAM sekitar 0,025 m. Selisih terhadap ORB-SLAM2 menegaskan bahwa penanganan objek dinamis memang diperlukan pada adegan ini — tanpa penanganan itu, galat membesar puluhan kali lipat karena titik fitur pada tubuh yang bergerak ikut dipakai seolah statis. Selisih terhadap DS-SLAM, meski lebih kecil, tetap menunjukkan keuntungan dari pembobotan bertingkat dibandingkan skema penghapusan objek DS-SLAM yang lebih sederhana. Pada rangkaian dinamis rendah `fr3/sitting_xyz`, ATE CFP-SLAM (sekitar 0,009 m) dan ORB-SLAM2 (sekitar 0,009 m) nyaris setara — masuk akal karena gerak subjek pada rangkaian ini minim, sehingga keuntungan penanganan dinamis tidak banyak berperan dan sistem dasar sudah memadai.

Dari sisi kecepatan, makalah melaporkan sistem penuh berjalan sekitar 42,7 milidetik per *frame*, setara 23 FPS, dengan varian ringkas (disebut CFP-SLAM tanpa modul tertentu) mencapai sekitar 24,8 milidetik per *frame* atau 40 FPS. Angka ini mengindikasikan sistem tetap berada pada kisaran mendekati *real-time* untuk aplikasi robotika, meski di bawah kecepatan ORB-SLAM2 murni yang tidak memiliki beban komputasi modul deteksi dan probabilitas tambahan. Studi ablasi pada makalah menunjukkan bahwa menghilangkan kompensasi deteksi hilang menyebabkan kegagalan berat pada adegan dinamis tinggi, dan menghilangkan pembaruan probabilitas titik kunci pada tahap halus membuat kinerja tidak konsisten antar-rangkaian — keduanya menunjukkan bahwa kedua tahap saling melengkapi, bukan berdiri sendiri.

## Kelebihan dan Keterbatasan

Kelebihan utama CFP-SLAM adalah pembobotan probabilistik bertingkat yang mempertahankan fitur statis di dalam kotak objek yang tertandai dinamis, sesuatu yang tidak dapat dilakukan skema penghapusan biner DynaSLAM maupun DS-SLAM. Sistem juga menunjukkan akurasi tinggi pada adegan dinamis tinggi tanpa mengorbankan akurasi pada adegan dinamis rendah, dan tetap berjalan pada kisaran mendekati *real-time*.

Dari sisi rekayasa, sistem ini menambahkan beberapa komponen berurutan — deteksi, kompensasi EKF/Hungarian, klasifikasi *chi-square*, klasterisasi DBSCAN, dan dua lapis kendala geometri — sehingga jumlah parameter ambang batas dan bobot fusi yang perlu disetel lebih banyak dibandingkan ORB-SLAM2 dasar. Secara konseptual, keandalan tahap kasar tetap bergantung pada kualitas deteksi YOLOv5s; bila objek gagal terdeteksi berkepanjangan meski sudah dikompensasi EKF, probabilitas awal yang diwariskan ke titik kunci berpotensi keliru. Evaluasi juga difokuskan pada rangkaian TUM RGB-D dalam ruangan; generalisasi ke lingkungan luar ruangan atau kondisi pencahayaan yang berbeda tidak dibahas pada makalah ini.

## Kaitan dengan Bab Lain

CFP-SLAM dibangun langsung di atas kerangka ORB-SLAM2 (bab [107](./107%20-%202017%20-%20ORB-SLAM2%20-%20RGB-D%20SLAM.md)), yang menyediakan struktur pelacakan fitur ORB dan *bundle adjustment* yang tetap dipakai sebagai inti optimasi pose. Terhadap DynaSLAM (bab [108](./108%20-%202018%20-%20DynaSLAM%20-%20RGB-D%20SLAM.md)) dan DS-SLAM (bab [109](./109%20-%202018%20-%20DS-SLAM%20-%20RGB-D%20SLAM.md)), bab ini menawarkan alternatif terhadap skema penghapusan biner objek dinamis keduanya, dengan menggantinya menjadi pembobotan probabilistik bertingkat. Perbandingan lebih lanjut dengan pendekatan berbasis deteksi objek untuk SLAM dapat dibaca pada bab [111](./111%20-%202019%20-%20Visual%20SLAM%20YOLO%20vs%20Mask%20R-CNN%20%28Soares%20dkk.%29%20-%20RGB-D%20SLAM.md), yang membandingkan langsung pilihan detektor objek (YOLO versus Mask R-CNN) sebagai modul semantik dalam SLAM dinamis, tema yang sejalan dengan penggunaan YOLOv5s pada makalah ini.

## Poin untuk Sitasi

Kutip dengan kunci `hu2022cfpslam`. Ringkasan yang aman dikutip: "CFP-SLAM menghitung probabilitas statis bertingkat (dari objek hasil deteksi YOLOv5s ke titik kunci individual) memakai kendala *optical flow*, epipolar, dan reproyeksi, lalu memakainya sebagai bobot pada optimasi pose ORB-SLAM2, mencapai ATE jauh lebih rendah daripada ORB-SLAM2 dasar pada rangkaian dinamis tinggi TUM RGB-D." Angka ATE (sekitar 0,014 m pada `fr3/walking_xyz`, sekitar 0,72 m untuk ORB-SLAM2, sekitar 0,025 m untuk DS-SLAM; sekitar 0,009 m pada `fr3/sitting_xyz`) dan angka kecepatan (42,7 ms/23 FPS untuk versi penuh, 24,8 ms/40 FPS untuk versi ringkas) diambil dari ekstraksi otomatis naskah dan sumber sekunder yang saling sedikit berbeda pada digit desimal (satu sumber melaporkan sekitar 1,5 cm dan 27 FPS untuk rangkaian yang sama) — **wajib diverifikasi ulang terhadap tabel asli pada PDF makalah** sebelum dikutip presisi dalam karya formal. Ambang klasifikasi "dinamis tinggi" (probabilitas ≤ 0,9) juga sebaiknya dicocokkan ke naskah asli.
