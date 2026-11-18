# Accurate fruit localisation using high resolution LiDAR-camera fusion and instance segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kang2022accurate` |
| Judul asli | Accurate fruit localisation using high resolution LiDAR-camera fusion and instance segmentation |
| Penulis | Kang, Hanwen; Wang, Xing; Chen, Chao |
| Tahun | 2022 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [kang2022accurate.pdf](../pdf/kang2022accurate.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2022.107450

## Gambaran Umum

Penelitian ini mengatasi penginderaan kedalaman untuk menentukan lokasi buah apel secara akurat bagi robot pemanen di kebun alami. Penulis mencatat bahwa penginderaan kedalaman menentukan keberhasilan pemanenan, sementara kamera monokular tidak dapat menentukan kedalaman absolut, kamera stereo kehilangan akurasi pada permukaan tanpa tekstur atau tekstur berulang, dan kamera cahaya terstruktur maupun stereo kurang tangguh terhadap pencahayaan kompleks. LiDAR tahan terhadap kondisi cahaya dan memberi geometri tiga dimensi yang tepat, tetapi awan titik dari LiDAR mekanik beresolusi rendah. LiDAR padat (*solid-state*) mengatasi kelemahan itu dengan mengakumulasi awan titik dari pola pemindaian tidak beraturan, namun tidak memiliki informasi semantik. Penulis menggabungkan LiDAR padat dan kamera warna, dengan prasyarat kalibrasi ekstrinsik yang akurat antarkedua sensor.

Sistem memakai Livox Mid-70 sebagai LiDAR padat dan kamera Intel RealSense D455 yang dipasang bersama dalam konfigurasi tetap memakai komponen cetakan tiga dimensi, dengan Nvidia Jetson TX2 sebagai pengontrol dan ROS Melodic untuk komunikasi. Kalibrasi intrinsik kamera dilakukan dengan papan catur 10 × 7 lebih dari 20 citra memakai MATLAB Camera Calibrator; galat reprojeksi maksimum kurang dari 0,09 piksel. Kalibrasi ekstrinsik membandingkan dua metode mutakhir, yaitu berbasis target memakai ASAC dengan papan catur 7 × 5 berukuran kotak 5 cm, serta tanpa target memakai fitur tepi dari detektor Canny pada citra dan bidang hasil RANSAC pada awan titik. Kalibrasi memerlukan akuisisi 15 detik agar awan titik cukup rapat, sedangkan penginderaan visual lazimnya kurang dari 2 detik.

Mekanisme penggabungan memproyeksikan setiap titik LiDAR ke piksel citra melalui matriks intrinsik kamera dan matriks ekstrinsik hasil kalibrasi, lalu menyusun awan titik berwarna. Tahap persepsi memakai jaringan segmentasi instans satu tahap YOLACT yang dimodifikasi, dengan *backbone* ResNet-50, cabang deteksi berbasis PANet yang menggabungkan fitur C3, C4, dan C5, serta cabang ProtoNet untuk topeng instans. Pelatihan memakai pengoptimal Adam selama 100 epoch dengan bobot *backbone* yang dibekukan pada 70 epoch pertama, laju pembelajaran 0,001, peluruhan 0,9, dan bobot rugi λobj 2,5 serta λnobj, λbbox, λmask masing-masing 1,0. Topeng buah hasil deteksi dipetakan ke peta kedalaman, titik-titik tiga dimensi yang bersesuaian dikumpulkan, pencilan dibuang dengan algoritme Z-score, dan pusat awan titik dipakai sebagai lokasi buah sebelum diubah ke kerangka robot.

Metrik kalibrasi berupa galat reprojeksi rata-rata dan galat reprojeksi ternormalisasi (NRE). Metode berbasis target menghasilkan 2,03 dan 0,78 piksel, sedangkan metode tanpa target menghasilkan 1,91 dan 0,66 piksel, sehingga metode tanpa target dipilih karena tidak memerlukan target khusus dan menyebarkan fitur secara merata. Pengujian lokalisasi dilakukan di kebun apel Fankhauser, Melbourne, pada jarak 0,5; 0,8; 1,2; 1,5; dan 1,8 m dengan menyamakan sudut pandang kedua sensor. Simpangan baku ketidakpastian lokasi buah untuk LiDAR-kamera berturut-turut 0,245; 0,236; 0,227; 0,204; dan 0,275 cm, dibandingkan RealSense D455 sebesar 1,006; 1,051; 1,175; 1,238; dan 1,360 cm. Dengan demikian galat LiDAR-kamera sekitar seperlima galat D455 dan hampir tidak berubah dengan jarak, sedangkan galat D455 meningkat seiring jarak.

Batasan yang dinyatakan penulis mencakup akurasi awan titik LiDAR yang lebih rendah di tepi wilayah pemindaian akibat *bleeding points* dari divergensi sudut berkas laser; solusi yang diusulkan adalah menggabungkan beberapa LiDAR dan hanya memakai bagian tengah awan titik masing-masing. Kalibrasi tanpa target memiliki syarat pemandangan, tidak cocok untuk objek silindris murni karena penyesuaian bidang, serta memerlukan tepi yang tersebar merata dan dalam berbagai arah. Penulis menyatakan lokasi buah diwakili oleh pusat awan titik dan estimasi sikap cengkeraman belum dikerjakan, karena fokus penelitian pada akurasi lokalisasi. Penelitian lanjutan yang diusulkan adalah meningkatkan akurasi kalibrasi ekstrinsik dan penggabungan LiDAR dari beberapa sudut pandang. Angka deteksi berupa presisi, recall, atau AP tidak dinyatakan.

