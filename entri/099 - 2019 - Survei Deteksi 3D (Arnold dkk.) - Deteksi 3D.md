# 099 - A Survey on 3D Object Detection Methods for Autonomous Driving Applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `arnold2019survey3d` |
| Judul asli | A Survey on 3D Object Detection Methods for Autonomous Driving Applications |
| Penulis | Eduardo Arnold, Omar Y. Al-Jarrah, Mehrdad Dianati, Saber Fallah, David Oxtoby, Alexandros Mouzakitis |
| Tahun | 2019 |
| Venue | IEEE Transactions on Intelligent Transportation Systems, vol. 20, no. 10, hlm. 3782–3795 |
| Tema | Deteksi 3D |

## Tautan Akses
- **Naskah diterima (PDF gratis, repositori Universitas Warwick):** https://wrap.warwick.ac.uk/id/eprint/114314/1/WRAP-survey-3D-object-detection-methods-autonomous-driving-applications-Arnold-2019.pdf
- **DOI (versi penerbit IEEE):** https://doi.org/10.1109/TITS.2019.2892405
- **Google Scholar:** https://scholar.google.com/scholar?q=A%20Survey%20on%203D%20Object%20Detection%20Methods%20for%20Autonomous%20Driving%20Applications

## Gambaran Umum

Makalah ini adalah survei yang memetakan metode deteksi objek 3D untuk kendaraan otonom, yaitu tugas memprediksi kotak pembatas berorientasi dalam ruang tiga dimensi (posisi x, y, z; ukuran panjang, lebar, tinggi; dan sudut hadap/*yaw*) alih-alih kotak dua dimensi pada bidang citra. Arnold dkk. mengklaim ini sebagai survei pertama yang secara khusus menata bidang deteksi 3D untuk aplikasi berkendara otonom, dengan menyusun taksonomi berdasarkan modalitas sensor yang dipakai: metode monokular (satu kamera RGB), metode berbasis *point cloud* (himpunan titik 3D dari sensor LiDAR), dan metode fusi multi-sensor yang menggabungkan keduanya.

Sebagai survei, kontribusinya bukan model baru, melainkan peta bidang: menata metode-metode yang sudah ada ke dalam kerangka yang sama, meninjau sensor dan kumpulan data (*dataset*) yang lazim dipakai, serta mengidentifikasi celah riset dan arah pengembangan. Bab ini berguna sebagai titik masuk bagi pembaca yang ingin memahami mengapa klaster Deteksi 3D dalam tinjauan pustaka ini terbagi menjadi pendekatan berbasis *voxel* (bab 087), berbasis kolom titik/*pillar* (bab 088), berbasis *region proposal* langsung dari titik (bab 089), berbasis frustum (bab 090), dan berbagai skema fusi kamera-LiDAR (bab 091–094) — seluruhnya adalah instansiasi dari tiga kategori yang disusun Arnold dkk.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum makalah ini terbit, riset deteksi objek pada citra sudah matang: detektor dua dimensi seperti keluarga R-CNN (bab 012–014) dan keluarga YOLO (bab 001–004) memprediksi kotak pembatas pada bidang gambar dengan akurasi tinggi. Namun keluaran dua dimensi tidak cukup untuk kendaraan otonom. Perencanaan lintasan (*path planning*) dan penghindaran tabrakan memerlukan informasi jarak, ukuran fisik, dan orientasi objek di dunia nyata — bukan sekadar posisi piksel pada citra. Kotak 2D pada citra tidak memberi tahu seberapa jauh sebuah mobil berada atau ke arah mana ia menghadap; informasi ini hanya dapat diperoleh bila kedalaman (*depth*) turut diprediksi atau diukur.

Kebutuhan ini mendorong munculnya beragam pendekatan deteksi 3D yang memakai sensor dan representasi data yang sangat berbeda satu sama lain: sebagian memakai kamera tunggal dengan asumsi geometris tambahan, sebagian memakai sensor LiDAR (*Light Detection and Ranging*, sensor laser yang mengukur jarak dengan memantulkan pulsa cahaya dan mencatat waktu pantulnya) yang menghasilkan *point cloud* — himpunan titik 3D akurat namun jarang (*sparse*) dan tidak berstruktur kisi seperti citra — dan sebagian lain menggabungkan kamera dengan LiDAR. Karena setiap kelompok metode memakai representasi masukan, arsitektur jaringan, kumpulan data, dan bahkan metrik evaluasi yang berbeda, membandingkan satu metode dengan metode lain menjadi sulit tanpa kerangka penyatuan. Inilah kekosongan yang ingin diisi oleh survei ini: sebelum 2019, belum ada rujukan tunggal yang menata seluruh pendekatan deteksi 3D khusus untuk konteks berkendara otonom ke dalam satu taksonomi yang konsisten.

## Ide Utama

Gagasan pengorganisasian survei ini adalah mengelompokkan metode deteksi 3D berdasarkan satu sumbu utama: modalitas sensor dan representasi data yang menjadi masukan jaringan. Sumbu ini dipilih karena secara langsung mencerminkan trade-off yang paling relevan bagi perancang sistem persepsi kendaraan otonom — biaya sensor, ketersediaan informasi geometris, dan ketahanan terhadap kondisi lingkungan saling terkait dengan pilihan modalitas.

Tiga kategori yang dihasilkan adalah metode monokular (bergantung pada kamera tunggal yang murah tetapi tidak mengukur kedalaman secara langsung, sehingga kedalaman harus disimpulkan dari isyarat visual), metode berbasis *point cloud* (bergantung pada LiDAR yang mengukur geometri 3D secara langsung dan akurat, tetapi mahal dan menghasilkan data jarang terutama pada jarak jauh), dan metode fusi (menggabungkan tekstur kaya dari kamera dengan geometri presisi dari LiDAR untuk saling menutupi kelemahan masing-masing sensor). Dengan kerangka ini, pembaca dapat memposisikan metode baru mana pun ke dalam salah satu dari tiga kelompok tersebut hanya dengan mengetahui sensor apa yang dipakainya.

## Cara Kerja Langkah demi Langkah

Karena berbentuk survei, bagian ini menguraikan metodologi peninjauan Arnold dkk., yaitu bagaimana taksonomi disusun dan apa yang dibahas pada tiap kategori — bukan pipeline satu model.

Peta taksonomi yang disusun survei ini:

```
Deteksi objek 3D untuk berkendara otonom
   |
   +-- Monokular (satu kamera RGB)
   |     citra 2D + asumsi geometris -> kotak 3D
   |
   +-- Berbasis point cloud (LiDAR)
   |     |-- proyeksi ke tampak-atas / tampak-depan
   |     |-- volumetrik (pembagian ruang jadi voxel)
   |     `-- langsung dari titik mentah (mis. PointNet)
   |
   `-- Fusi multi-sensor
         kamera (tekstur) + LiDAR (geometri)
         -> digabung pada tahap dini, lanjut, atau dalam
```

### Metode Monokular

Kelompok pertama memprediksi kotak 3D hanya dari satu citra RGB. Karena citra tunggal secara matematis tidak memuat informasi kedalaman, metode-metode ini menambahkan asumsi geometris sebagai pengganti, misalnya asumsi bahwa objek bertumpu pada bidang tanah datar atau pemakaian templat bentuk 3D generik (mobil sedan, misalnya, memiliki proporsi panjang/lebar/tinggi yang relatif konsisten) yang dicocokkan dengan siluet objek pada citra. Survei menjelaskan bahwa keakuratan pendekatan ini pada dasarnya dibatasi oleh ambiguitas kedalaman dari citra tunggal, sehingga performanya secara konsisten berada di bawah metode yang memakai LiDAR, khususnya untuk objek jauh atau kecil.

### Metode Berbasis Point Cloud

Kelompok kedua bekerja langsung pada *point cloud* dari LiDAR. Data ini tidak berbentuk kisi teratur seperti piksel citra, sehingga jaringan konvolusi standar tidak dapat langsung diterapkan. Survei menandai tiga strategi umum untuk mengatasi hal ini: pertama, memproyeksikan titik 3D ke bidang 2D (tampak-atas/*bird's-eye view* atau tampak-depan) sehingga konvolusi 2D biasa dapat dipakai, dengan konsekuensi sebagian informasi 3D hilang saat proyeksi; kedua, membagi ruang 3D menjadi sel volumetrik (*voxel*) berukuran tetap dan menerapkan konvolusi 3D pada kisi voxel tersebut, seperti yang dilakukan VoxelNet (dibahas pada bab 087); ketiga, memproses titik mentah secara langsung tanpa voksel atau proyeksi memakai arsitektur bergaya PointNet, yang menjamin invariansi terhadap urutan titik. Pendekatan berbasis frustum (bab 090) dan berbasis *region proposal* dari titik (bab 089) merupakan variasi dari strategi ketiga ini.

### Metode Fusi Multi-Sensor

Kelompok ketiga menggabungkan kamera dan LiDAR agar kekurangan satu sensor ditutupi sensor lain: kamera memberi tekstur dan warna yang kaya untuk membedakan kelas objek, LiDAR memberi geometri dan jarak yang presisi. Survei membedakan skema fusi menurut tahap penggabungannya di dalam jaringan — penggabungan dini (menggabungkan data mentah sebelum diproses), penggabungan lanjut (menggabungkan hasil akhir dari dua jaringan terpisah), dan penggabungan pada lapisan tersembunyi jaringan (fitur kedua modalitas digabung di tengah proses, bukan di awal atau akhir). Metode fusi yang menggabungkan tampilan kamera, tampak-atas, dan tampak-depan LiDAR seperti MV3D (bab 091) dan AVOD (bab 092) menjadi contoh representatif kategori ini pada masa survei ditulis.

### Kumpulan Data dan Metrik Evaluasi

Survei juga meninjau sensor dan kumpulan data yang lazim dipakai untuk melatih dan menguji metode-metode di atas. KITTI menjadi tolok ukur (*benchmark*) dominan yang dibahas: kumpulan data ini menyediakan citra kamera, *point cloud* LiDAR, dan kalibrasi antar-sensor yang telah diselaraskan, dengan anotasi kotak 3D untuk tiga kelas objek jalan raya (mobil, pejalan kaki, pesepeda) dan tiga tingkat kesulitan (mudah, sedang, sulit) yang ditentukan dari derajat oklusi, pemotongan objek di tepi citra, dan tinggi kotak pada piksel. Metrik utama yang dipakai adalah *Average Precision* (AP, presisi rata-rata di berbagai ambang) yang dihitung terpisah untuk deteksi tampak-atas (*bird's-eye view*) dan deteksi 3D penuh, biasanya pada ambang IOU tertentu per kelas.

## Eksperimen dan Hasil

Sebagai survei, makalah ini tidak menjalankan eksperimen baru; ia mengumpulkan dan membandingkan hasil yang telah dilaporkan oleh metode-metode yang ditinjau pada tolok ukur yang sama, terutama KITTI. Pembandingan semacam ini menempatkan metode monokular, berbasis *point cloud*, dan fusi pada satu tabel yang sama sehingga selisih akurasi antar-kategori dapat dilihat langsung.

Pola yang ditekankan survei bersifat kualitatif namun konsisten dengan penjelasan mekanistik di atas: metode berbasis LiDAR dan metode fusi secara umum jauh melampaui metode monokular dalam akurasi lokalisasi 3D, karena keduanya mengakses geometri langsung dari sensor jarak, sedangkan metode monokular harus menyimpulkan kedalaman dari isyarat visual yang secara inheren ambigu. Namun keunggulan akurasi ini berhadapan dengan biaya perangkat keras — LiDAR jauh lebih mahal daripada kamera — dan dengan kebutuhan komputasi tambahan pada metode fusi karena harus memproses dua aliran data sekaligus. Survei juga mencatat bahwa performa hampir seluruh metode menurun tajam pada objek jauh dan kecil, konsisten di semua kategori, karena kepadatan titik LiDAR menurun seiring jarak dan resolusi efektif objek pada citra kamera juga mengecil.

Angka AP spesifik per metode pada tabel perbandingan survei tidak dapat diverifikasi ulang secara langsung dalam penulisan bab ini; pembaca yang membutuhkan angka pasti sebaiknya merujuk tabel komparatif pada naskah asli (lihat Tautan Akses) sebelum mengutipnya dalam karya formal.

## Kelebihan dan Keterbatasan

Kelebihan utama survei ini terletak pada kejelasan taksonominya: pengelompokan berdasarkan modalitas sensor memberi kerangka yang mudah dipakai untuk memposisikan metode baru, dan peninjauan atas kumpulan data serta metrik membantu pembaca yang baru memasuki bidang deteksi 3D memahami bagaimana metode-metode itu diuji dan dibandingkan secara adil. Identifikasi celah riset dan arah pengembangan juga memberi konteks bagi metode-metode yang muncul setelahnya.

Dari sisi keterbatasan, survei bidang deteksi 3D untuk berkendara otonom cepat menjadi usang karena lajunya publikasi yang sangat tinggi pada periode 2018–2021; metode-metode yang muncul setelah 2019, termasuk beberapa yang dibahas pada bab-bab berikutnya dalam klaster ini (bab 093, PointPainting; bab 094, 3D-CVF), berada di luar cakupan survei ini dan hanya dapat dipahami dengan membaca survei yang lebih baru sebagai pelengkap. Secara konseptual, fokus survei yang sangat spesifik pada domain berkendara otonom juga berarti taksonominya kurang langsung berlaku untuk kasus penggunaan deteksi 3D lain, seperti robotika indoor atau pemetaan dengan wahana udara nirawak, yang memiliki karakteristik sensor dan objek berbeda. Terakhir, karena berbentuk survei, makalah ini tidak memberikan kontribusi arsitektur baru; nilai akademisnya terletak pada penataan dan sintesis, bukan pada peningkatan akurasi tolok ukur.

## Kaitan dengan Bab Lain

Bab ini berfungsi sebagai peta bagi seluruh klaster Deteksi 3D dalam tinjauan pustaka ini. Kategori berbasis *point cloud* yang dijelaskan di sini mencakup pendekatan volumetrik pada [087 - 2018 - VoxelNet - Deteksi 3D](./087%20-%202018%20-%20VoxelNet%20-%20Deteksi%203D.md), pendekatan kolom titik pada [088 - 2019 - PointPillars - Deteksi 3D](./088%20-%202019%20-%20PointPillars%20-%20Deteksi%203D.md), dan pendekatan langsung dari titik mentah pada [089 - 2019 - PointRCNN - Deteksi 3D](./089%20-%202019%20-%20PointRCNN%20-%20Deteksi%203D.md) serta [090 - 2018 - Frustum PointNets - Deteksi 3D](./090%20-%202018%20-%20Frustum%20PointNets%20-%20Deteksi%203D.md). Kategori fusi mencakup [091 - 2017 - MV3D - Deteksi 3D](./091%20-%202017%20-%20MV3D%20-%20Deteksi%203D.md) dan [092 - 2018 - AVOD - Deteksi 3D](./092%20-%202018%20-%20AVOD%20-%20Deteksi%203D.md), dengan kelanjutan fusi yang lebih baru pada [093 - 2020 - PointPainting - Deteksi 3D](./093%20-%202020%20-%20PointPainting%20-%20Deteksi%203D.md) dan [094 - 2020 - 3D-CVF - Deteksi 3D](./094%20-%202020%20-%203D-CVF%20-%20Deteksi%203D.md), yang keduanya terbit setelah survei ini dan karenanya tidak tercakup di dalamnya. Bagi pembaca tinjauan ini, urutan yang disarankan adalah membaca bab 099 terlebih dahulu untuk memperoleh kerangka klasifikasi, baru kemudian mendalami tiap metode pada bab 087–094 dan 098 (jika ada bab lain di luar rentang ini pada klaster yang sama) untuk detail mekanisme masing-masing.

## Poin untuk Sitasi

Kutip dengan kunci `arnold2019survey3d`. Ringkasan yang aman dikutip: "Arnold dkk. (2019) menyusun survei deteksi objek 3D untuk berkendara otonom yang mengklasifikasikan metode ke dalam tiga kategori berdasarkan modalitas sensor — monokular, berbasis *point cloud*, dan fusi — serta meninjau kumpulan data dan metrik evaluasi yang lazim dipakai, khususnya KITTI." Klaim taksonomi tiga kategori dan status "survei pertama" untuk domain berkendara otonom diverifikasi dari abstrak naskah (repositori Universitas Warwick). Detail berikut belum terverifikasi langsung dari isi lengkap naskah dan perlu dicek ulang sebelum dikutip formal: nama metode spesifik yang dicontohkan pada tiap kategori (VoxelNet, MV3D, AVOD, dan sejenisnya), rincian pasti pembagian data latih/uji KITTI, ambang IOU per kelas yang dipakai dalam tabel perbandingan, serta angka AP pada tabel komparatif metode.
