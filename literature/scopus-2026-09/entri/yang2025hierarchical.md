# Hierarchical 3D Scene Graph based Semantic-Metric SLAM for Plant Inspection and Fruit Counting in Intelligent Hydroponics System

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2025hierarchical` |
| Judul asli | Hierarchical 3D Scene Graph based Semantic-Metric SLAM for Plant Inspection and Fruit Counting in Intelligent Hydroponics System |
| Penulis | Yang, Wenyu; Liu, Kang; Tan, Zheng; Lo, Li-Yu; Wang, Yinglun; Wong, Ka-Hing; Wen, Chih-Yung |
| Tahun | 2025 |
| Venue | IEEE Internet of Things Journal |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [yang2025hierarchical.pdf](../pdf/yang2025hierarchical.pdf)
- DOI resmi: https://doi.org/10.1109/jiot.2025.3600531

## Gambaran Umum

Makalah ini mengusulkan kerangka SLAM metrik-semantik (*metric-semantic SLAM*) berbasis graf adegan 3D hierarkis (*3-D scene graph*, 3DSG) untuk inspeksi tanaman dan penghitungan buah pada sistem pertanian vertikal hidroponik yang memakai pesawat nirawak (UAV). Graf adegan disusun dalam lapisan: titik geometris tanpa semantik, buah, tanaman, dan kebun. Buah dideteksi hanya di dalam kotak pembatas tanaman, ditambahkan sebagai simpul anak dari tanaman, dan digabung dengan simpul buah yang sudah ada bila jaraknya di bawah ambang. Penulis juga menurunkan analisis rambatan galat (*error propagation*) untuk konfigurasi stereo/RGB-D dan kamera-LiDAR.

Validasi dilakukan pada empat skenario: simulasi Gazebo (terong ungu, tomat merah, paprika kuning), dataset TUM RGB-D (dalam ruangan, untuk objek umum), dataset kompetisi ICUAS'24 (kebun dengan buah kuning dan merah, UAV dengan kamera dan LiDAR), serta laboratorium hidroponik stroberi di The Hong Kong Polytechnic University. Teks makalah menyebut hasil kuantitatif tertentu: kecocokan 100% terhadap acuan pada sebagian besar kasus simulasi (satu kasus 102%), pengurangan galat lokalisasi buah 40% dibandingkan metode Liu pada kebun luar ruangan ICUAS'24, dan akurasi hitungan stroberi 92% pada penerbangan dinamis di laboratorium. Isi Tabel I–V tidak terbaca dari teks ekstraksi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penulis menyatakan bahwa pemantauan pertumbuhan tanaman pada sistem pertanian vertikal otonom membutuhkan persepsi yang memberi informasi struktur dan semantik. Tiga keterbatasan disebutkan: (1) SLAM visual dan LiDAR umumnya menghasilkan peta awan titik tanpa semantik; (2) algoritma deteksi dan segmentasi 2D yang dikembangkan pada data ideal tidak membangun model pertumbuhan 3D yang berkorelasi secara ekologis; (3) metode yang ada mengurai organ tanaman menjadi elemen spasial terpisah. Metode estimasi objek 3D dari pengendaraan otonom disebut tetap menghasilkan galat tinggi pada penghitungan buah dan estimasi pose di kebun yang bertekstur kompleks dengan target berskala kecil.

Penulis juga mencatat bahwa sistem graf adegan terdahulu (Kimera dan Hydra) terutama diuji pada simulasi dengan segmentasi semantik yang akurat, sedangkan segmentasi sempurna tidak realistis di dunia nyata.

## Ide Utama

Hierarki objek dipakai untuk menekan galat. Alasannya dua: (1) deteksi berderau pada objek kecil (misalnya buah) terbatas pada tingkat abstraksi rendah sehingga galat tidak merambat ke tingkat tanaman atau kebun; (2) objek tingkat lebih tinggi (tanaman) mengumpulkan pengamatan dari banyak simpul anak sehingga pencilan tertekan. Objek besar berasosiasi dengan lebih banyak piksel kedalaman sehingga nilai kedalamannya lebih tahan terhadap pencilan. Asosiasi data dilakukan dari atas ke bawah: objek besar diasosiasikan lebih dulu, lalu objek kecil di dalamnya, dengan ambang jarak yang bergantung pada ukuran objek. Pembaruan pose simpul induk ikut memperbarui pose anaknya, yang menurut penulis mengurangi galat pencocokan saat penutupan loop.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Empat set data dipakai (Tabel I tidak terbaca dari teks). Simulasi Gazebo dari fase simulasi ICUAS'24 berisi buah pada petak tanam vertikal dengan UAV bersensor kamera kedalaman dan IMU, dengan odometri acuan (*ground truth*) sebagai pose. Dataset ICUAS'24 dikumpulkan dengan UAV yang diterbangkan manual dengan kamera menghadap depan, LiDAR 3D, penerima GPS, IMU, dan pengendali Pixhawk; kebun berisi dua jenis tanaman dengan buah kuning dan merah. Laboratorium hidroponik (suhu 22 ± 1 °C, kelembapan relatif 50%–60%) memiliki 32 unit hidroponik cerdas; UAV dilengkapi kamera RGB-D dan Livox MID-360. Lebih dari 1200 citra stroberi dianotasi hanya untuk stroberi dengan kelopak gugur penuh. Jumlah pohon atau tanaman per set data tidak dilaporkan pada teks.

### 2. Model galat

Koordinat dunia dipulihkan dari deteksi piksel $(u, v)$ dan kedalaman $d$ dengan matriks intrinsik $K$ dan transformasi $T_{wc}$, dengan derau deteksi, derau kedalaman, dan galat pose. Pada stereo, galat kedalaman sebanding dengan kuadrat kedalaman: $\sigma_Z = \frac{m}{fb}\frac{\sigma_\rho}{Z^2}$ menurut ungkapan penulis (Persamaan 8, teks ekstraksi memuat tata letak yang rusak). Pada kamera-LiDAR, suku dominan galat kedalaman tumbuh kuadratik terhadap jarak. Ukuran objek di citra mengikuti $\text{obj\_image\_size} = \text{obj\_size} \cdot f / \text{distance}$.

### 3. Graf adegan hierarkis

Graf berlapis dengan aturan induk tunggal, atribut posisi diwarisi dari induk, lokalitas antarlapis, dan anak-anak yang saling lepas. Lapisan yang dipakai: titik, buah, tanaman, kebun. Algoritma 1 menambahkan anak; bila jarak simpul baru ke anak lama kurang dari ambang, keduanya digabung dengan filter respons impuls tak hingga (*infinite impulse response*, IIR), dan pose semua anak simpul itu diperbarui. Segmentasi pohon pada peta awan titik memakai DBSCAN.

### 4. Fusi sensor

Untuk RGB-D, deteksi 2D dibatasi di dalam kotak objek tingkat atas. Untuk kamera-LiDAR, kotak pembatas diproyeksikan ke ruang 3D lalu gugus titik disaring, dengan peta LiDAR yang dibangun terlebih dahulu melalui odometri LiDAR dan fusi dilakukan pada peta tersebut. Deteksi stroberi memakai YOLOv8 dengan dua kelas: matang bila permukaan merah lebih dari 60%, mentah bila kurang dari 60%.

## Eksperimen dan Hasil

Pembanding untuk data RGB-D: OA-SLAM, QuadricSLAM, VOOM, QISO-SLAM, Kimera, dan Hydra. Untuk kamera-LiDAR: metode Kang dkk. dan Liu dkk. (ORB-Livox, diimplementasikan ulang karena kode tidak terbuka). Metrik hitungan dinyatakan sebagai persentase kedekatan terhadap acuan, dengan 100% berarti sesuai.

| Skenario | Pembanding | Hasil yang tertulis dalam teks |
|---|---|---|
| Simulasi Gazebo (Tabel II) | Kimera, Hydra | Metode penulis mencapai 100% pada sebagian besar kasus uji dan 102% pada satu kasus; angka pembanding tidak terbaca |
| TUM RGB-D dan DIAMOND (Tabel III) | OA-SLAM, QISO-SLAM, VOOM | Penulis menyatakan metodenya unggul pada semua sekuens; angka tidak terbaca |
| ICUAS'24 (Tabel IV) | Liu dkk. | Galat lokalisasi buah berkurang 40% (Kesimpulan); angka hitungan tidak terbaca |
| Hidroponik stroberi (Tabel V) | Liu dkk. | Akurasi hitungan 92% pada penerbangan dinamis; galat lokalisasi 2 cm |

Selain itu, teks melaporkan bahwa sekalipun lintasan acuan dipakai, tidak ada metode yang mencapai 100% pada "% Found" dan "% Correct" dan bahwa terdapat galat lokalisasi tingkat sentimeter pada ketiga metode di simulasi. Penulis mengaitkan ini dengan Hydra yang cenderung kurang-segmentasi objek berdekatan sekelas, serta peta Voxblox yang kadang memproyeksikan label ke permukaan di belakang objek. Pada ICUAS'24, buah pada metode Liu banyak jatuh pada area kosong di antara dua baris kebun akibat derau kedalaman latar belakang, sedangkan pada metode penulis buah selaras dengan pohon. Hanya stroberi matang yang dihitung karena stroberi mentah sulit dideteksi.

## Kelebihan dan Keterbatasan

Kelebihan menurut makalah: pengurangan galat melalui asosiasi hierarkis dari atas ke bawah, analisis galat untuk beberapa kombinasi sensor, kode terbuka, pengujian pada simulasi dan data nyata, serta penggunaan pada UAV bergerak (bukan hanya platform statis).

Keterbatasan yang dinyatakan penulis: kinerja RGB-D menurun pada skenario sulit (diatasi dengan fusi LiDAR), beban komputasi berat pada perangkat tertanam, kepekaan terhadap kerapatan daun ekstrem pada kebun luar ruangan, kesulitan mendeteksi stroberi mentah, dan masih adanya galat pada lingkungan berantakan.

Menurut pembacaan ringkasan ini: acuan hitungan pada kebun dan hidroponik tidak dijelaskan cara pembuatannya selain pengukuran manual posisi stroberi, sehingga dasar persentase 92% dan 40% tidak dapat dinilai dari teks. Baseline Liu diimplementasikan ulang oleh penulis sendiri. Skenario hidroponik adalah ruang terkendali dengan stroberi saja, sehingga generalisasi ke tandan besar di pohon tinggi belum teruji. Hitungan hanya dilaporkan untuk satu kelas (stroberi matang).

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali melalui asosiasi data berbasis geometri pada peta 3D yang dibangun SLAM. Pengamatan dari banyak bingkai digabung bila posisi 3D simpul baru berada dalam ambang jarak (yang bergantung pada ukuran dan kelas objek) terhadap simpul lama, kemudian posisinya diperbarui dengan filter IIR; satu simpul mewakili satu buah. Lapisan induk (tanaman) membatasi ruang pencarian: buah hanya dicari dan dicocokkan di dalam tanaman yang sama. Mekanisme ini tergolong rekonstruksi 3D dan asosiasi hierarkis, bukan pelacakan visual per bingkai.

Hitungan dilaporkan sebagai jumlah per kategori buah (misalnya jenis sayur dan stroberi matang) pada beberapa skenario, tetapi hanya stroberi matang yang dihitung pada hidroponik; tidak ada inventaris per kelas kematangan. Acuan hitung adalah hitungan acuan pada simulasi dan hasil pelabelan manual pada TUM RGB-D; untuk kebun dan hidroponik, asal acuan tidak dijelaskan dengan rinci. Yang dapat dipindahkan ke tandan sawit multi-sisi adalah penguncian pencarian buah ke dalam objek induk (pohon) dan ambang asosiasi yang bergantung pada ukuran objek, ditambah penghalusan pose dengan filter berulang. Kebutuhan pose kamera akurat dan kedalaman andal pada jarak jauh tetap menjadi syarat, dan analisis galat makalah menunjukkan kedalaman memburuk secara kuadratik terhadap jarak.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `yang2025hierarchical`.

Yang dkk. mengusulkan SLAM metrik-semantik berbasis graf adegan 3D hierarkis (titik, buah, tanaman, kebun) untuk penghitungan buah pada sistem hidroponik berbasis UAV, dengan asosiasi data dari atas ke bawah dan penggabungan pengamatan buah memakai filter IIR. Makalah melaporkan kecocokan hitungan 100% pada sebagian besar kasus simulasi, pengurangan galat lokalisasi buah 40% terhadap metode Liu pada ICUAS'24, dan akurasi hitungan stroberi 92% pada penerbangan dinamis di laboratorium hidroponik.

Catatan verifikasi data: Tabel I–V dan Gambar 3 serta Gambar 11 tidak terbaca pada teks ekstraksi, sehingga angka hitungan per metode, jumlah buah acuan, dan jumlah pohon tidak dapat diverifikasi. Angka yang dikutip berasal dari narasi: 100% dan 102% (Seksi V-A), 40% dan 92% (Kesimpulan), galat 2 cm (Seksi V-D), lebih dari 1200 citra dan ambang 60% merah (Seksi V-D), 32 unit hidroponik dan kondisi lingkungan (Seksi V-D). Pernyataan "40%" pada Kesimpulan dirumuskan sebagai pengurangan galat lokalisasi buah terhadap metode Liu, sedangkan Seksi V-C tidak menyebut angka itu secara eksplisit. Persamaan di teks ekstraksi terpotong sebagian.
