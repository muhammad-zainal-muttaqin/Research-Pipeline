# Vision-Based 3D Fruit Localization for Robotic Harvesting Using Recursive State Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gao2026vision` |
| Judul asli | Vision-Based 3D Fruit Localization for Robotic Harvesting Using Recursive State Estimation |
| Penulis | Gao, Zhao; Wang, Yinglun; Liu, Kang; Yang, Wenyu; Jia, Chuanzhen; Wong, Ka-Hing |
| Tahun | 2026 |
| Venue | 2026 7th International Conference on Artificial Intelligence and Electromechanical Automation Aiea 2026 |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [gao2026vision.pdf](../pdf/gao2026vision.pdf)
- DOI resmi: https://doi.org/10.1109/aiea70743.2026.11633088

## Gambaran Umum
Makalah prosiding ini (AIEA 2026) mengusulkan kerangka lokalisasi 3D buah untuk pemanenan robotik dan estimasi hasil panen. Kerangka itu memanfaatkan asosiasi antarbingkai video berurutan dan penaksir *Recursive Least Squares* (RLS) untuk menghaluskan posisi 3D tiap buah yang mula-mula diperoleh kasar dari deteksi 2D dan pengukuran kedalaman. Dua konfigurasi sensor diperiksa, yaitu kamera RGB-D tunggal dan fusi kamera dengan LiDAR; fusi kamera-LiDAR dipakai sebagai pembanding dasar.

Validasi dilakukan pada lingkungan simulasi Gazebo: buah ditempatkan pada bedengan vertikal di kebun simulasi, dan wahana udara tanpa awak (UAV) berkamera kedalaman dan IMU memperkirakan posisi tanaman. Hasil dilaporkan hanya secara kualitatif melalui grafik lintasan posisi (Gambar 4) yang membandingkan metode usulan dengan metode rerata bergerak dua bingkai; penulis menyatakan varians metode usulan jauh lebih rendah. Makalah tidak melaporkan angka akurasi, galat, jumlah buah, maupun jumlah citra dalam bentuk numerik.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa lokalisasi 3D tanaman, terutama buah yang rapuh, sulit karena oklusi, pencahayaan yang berubah, dan kondisi lapangan yang dinamis. Pendekatan naif mendeteksi objek pada citra (misalnya dengan YOLO) lalu menggabungkannya dengan kedalaman untuk memperoleh posisi dalam kerangka dunia. Menurut makalah, posisi hasil pendekatan itu pada kerangka kamera berfluktuasi besar akibat galat komputasi, dan galat odometri kendaraan merambat pada posisi objek di kerangka dunia (Gambar 2).

Penulis juga menyatakan bahwa estimasi posisi buah tunggal tidak sepenuhnya sesuai kebutuhan produksi, dan bahwa penghitungan skala kebun mulai muncul. Galat sensor, lokalisasi, dan algoritma 3D menyebabkan deteksi ganda atau deteksi terlewat. Teknik seperti *loop closure* dan *scene graph* telah dipakai untuk mengurangi galat, tetapi menurut penulis belum ada pendekatan yang menganalisis secara sistematis porsi galat dari tiap modul.

## Ide Utama
Posisi buah yang sama diamati berulang kali pada bingkai berurutan, sehingga pengukuran per bingkai yang berisik dapat digabungkan secara rekursif menjadi taksiran posisi yang lebih stabil. Vektor keadaan objek adalah $x=[x,y,z,\phi,\theta,\psi]^T$, yaitu posisi 3D dan sudut Euler. Pengukuran dimodelkan linear, $z(k)=H(k)x+w(k)$, dengan derau Gaussian berkovarians $R(k)$ diagonal. Formulasi rekursif (identik dengan pembaruan filter Kalman linear) menggantikan penyelesaian kuadrat terkecil *batch* yang memerlukan semua bingkai sekaligus dan karena itu tidak cocok untuk sistem daring.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data dan platform
Percobaan memakai lingkungan Gazebo dengan buah berwarna dan berukuran serupa pada bedengan vertikal di kebun simulasi. UAV berkamera kedalaman dan IMU bergerak di dalam rumah kaca simulasi. Lintasan 6-DoF sebenarnya (*ground truth*) diambil langsung dari mesin simulasi dengan akurasi submilimeter. Jenis buah, jumlah buah, jumlah tanaman (grafik Gambar 4 menampilkan empat tanaman), dan jumlah bingkai tidak dilaporkan secara rinci. Abstrak menyebut platform robot bergerak otonom dengan fusi multisensor dan skenario dunia nyata, tetapi Bab V menyatakan bahwa pekerjaan ini baru divalidasi di lingkungan simulasi.

### 2. Bagian depan (*frontend*) per bingkai
Posisi objek relatif terhadap robot dihitung dari pembacaan sensor sesaat, lalu diubah ke kerangka dunia memakai pose odometri robot. Rekonstruksi 3D memproyeksikan balik deteksi 2D dengan geometri proyektif kamera, $[x_c,y_c,z_c]^T=K^{-1}[ud,vd,d]^T$. Pada kamera RGB-D, kedalaman diambil dari dalam kotak pembatas objek. Pada fusi kamera-LiDAR, kedalaman diperoleh dari awan titik LiDAR setelah kalibrasi ekstrinsik, baik berbasis target (papan catur dengan 7×5 sudut dalam dan ukuran kotak 5 cm) maupun tanpa target. Penulis menyatakan evaluasi kuantitatif kalibrasi tidak diberikan.

### 3. Optimasi bagian belakang (*backend*)
Formulasi *batch* diturunkan sebagai pembanding teoretis. Formulasi rekursif memperbarui matriks informasi, gain Kalman $W$, kovarians residu $S$, dan taksiran keadaan pada setiap bingkai baru (Algoritma 1). Matriks pengamatan posisi adalah $[I_{3\times3}\;0_{3\times3}]$ dan matriks pengamatan orientasi adalah $[0_{3\times3}\;I_{3\times3}]$. Varians derau ditentukan lewat kalibrasi sensor.

## Eksperimen dan Hasil
Eksperimen membandingkan metode usulan dengan pembanding rerata bergerak pada dua bingkai berurutan. Kedua metode memakai *frontend* RGB-D yang sama dan anotasi segmentasi semantik acuan yang dihasilkan lewat ambang HSV pada simulasi, sehingga derau sensor dari deteksi dikurangi. Tujuan tertulis Bab IV adalah menilai penghitungan buah dan lokalisasi terhadap *ground truth*, dengan akurasi hitungan dinyatakan dalam persen terhadap acuan, tetapi hasil penghitungan tidak disajikan pada teks.

| Aspek | Keterangan dalam makalah |
|---|---|
| Lingkungan uji | Simulasi Gazebo; UAV dengan kamera kedalaman dan IMU |
| Metode usulan | RLS rekursif pada posisi (dan orientasi) 3D tiap buah |
| Pembanding | Rerata bergerak dua bingkai berurutan |
| Ukuran hasil | Kurva posisi x, y, z empat tanaman terhadap waktu (Gambar 4) |
| Temuan | Kedua metode terpengaruh galat *frontend*; metode usulan bervarians jauh lebih rendah |
| Angka numerik | Tidak dilaporkan |

Konfigurasi kamera-LiDAR dijelaskan sebagai pembanding dasar, tetapi tidak ada hasilnya pada teks.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: pembaruan rekursif cukup ringan untuk sistem daring, dan metode menghasilkan lintasan posisi yang lebih koheren dibandingkan rerata bergerak. Penulis menyatakan keterbatasan: validasi baru dilakukan dalam simulasi, dan kerja lanjutan mencakup eksperimen lapangan nyata dengan fokus pada variasi pencahayaan dan oklusi, optimasi untuk UAV, serta perencanaan jalur. Penulis juga menyatakan bahwa sensor RGB-D memiliki jangkauan terbatas dan sensitif terhadap pencahayaan, dan bahwa resolusi LiDAR yang rendah dapat menimbulkan galat lebih besar pada objek kecil.

Menurut pembacaan ringkasan ini, evaluasi sangat terbatas: tidak ada metrik numerik, tidak ada uji pada data nyata, dan *frontend* memakai segmentasi acuan sehingga galat deteksi tidak diuji. Pembanding hanyalah rerata bergerak dua bingkai. Makalah juga tidak konsisten secara internal: kontribusi pada Bab I menyebut estimator RLS, Bab II menyebut *Extended Kalman Filter* (EKF), sedangkan formulasi Bab III adalah RLS linear. Abstrak menyebut validasi di skenario dunia nyata, sedangkan kesimpulan menyatakan hanya simulasi. Klaim kemampuan prediksi hasil panen non-invasif tidak didukung eksperimen penghitungan.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali pada bingkai video berurutan, dengan mekanisme asosiasi antarbingkai dan penggabungan posisi 3D secara rekursif (filter Kalman atau RLS). Teks tidak menjelaskan cara asosiasi dilakukan, yaitu bagaimana deteksi pada bingkai berbeda ditetapkan sebagai buah yang sama; algoritma hanya menyajikan pembaruan keadaan untuk satu objek. Penghitungan per kelas tidak dilaporkan, dan acuan hitung berupa *ground truth* simulasi, bukan panen atau hitungan lapangan. Hasil penghitungan tidak disajikan.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi hanya bersifat konseptual: penghalusan posisi 3D objek dari banyak pengamatan dengan model derau eksplisit, dan pemisahan galat odometri dari galat pengukuran kedalaman. Makalah ini tidak memberikan bukti empiris untuk skenario lapangan atau antarsisi pohon.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `gao2026vision`.

Gao dkk. mengusulkan kerangka lokalisasi 3D buah yang memakai asosiasi antarbingkai video dan penaksir *Recursive Least Squares* untuk menghaluskan posisi buah dari pengukuran RGB-D atau fusi kamera-LiDAR. Pada simulasi Gazebo dengan UAV, metode itu dilaporkan menghasilkan lintasan posisi dengan varians lebih rendah daripada rerata bergerak dua bingkai; makalah tidak melaporkan metrik numerik dan validasi lapangan masih menjadi pekerjaan lanjutan.

Catatan verifikasi data: Hasil utama hanya berupa kurva pada Gambar 4 (posisi x, y, z empat tanaman terhadap waktu); teks ekstraksi hanya memuat label sumbu dan tidak memuat nilai hasil, sehingga tidak ada angka yang dapat dikutip. Satu-satunya angka tertulis berkaitan dengan kalibrasi (papan catur 7×5 sudut dalam, kotak 5 cm, perekaman 15 detik per adegan) dan akurasi simulasi submilimeter. Jumlah buah, jenis buah, jumlah bingkai, dan hasil penghitungan tidak dilaporkan. Pembanding kamera-LiDAR dijelaskan tetapi tidak dilaporkan hasilnya. Ketidakkonsistenan RLS dan EKF serta klaim dunia nyata dalam abstrak dibahas pada bagian keterbatasan. Teks ekstraksi tampak lengkap untuk makalah enam halaman ini.
