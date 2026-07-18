# 188 - DETR3D: 3D Object Detection from Multi-View Images via 3D-to-2D Queries

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2022detr3d` |
| Judul asli | DETR3D: 3D Object Detection from Multi-View Images via 3D-to-2D Queries |
| Penulis | Yue Wang, Vitor Campagnolo Guizilini, Tianyuan Zhang, Yilun Wang, Hang Zhao, Justin Solomon |
| Tahun | 2022 |
| Venue | Conference on Robot Learning (CoRL 2021, dipublikasikan dalam prosiding 2022) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2110.06922
- **Google Scholar:** https://scholar.google.com/scholar?q=DETR3D%3A%203D%20Object%20Detection%20from%20Multi-View%20Images%20via%203D-to-2D%20Queries
- **Repositori kode resmi:** https://github.com/WangYueFt/detr3d

## Gambaran Umum

Makalah ini memperkenalkan DETR3D, metode deteksi objek 3D dari beberapa kamera sekaligus (*multi-view*) yang bekerja langsung dalam ruang 3D tanpa membangun representasi *bird's-eye view* (BEV, tampak-atas) yang padat dan tanpa memerlukan estimasi kedalaman (*depth*) per piksel. Gagasan intinya adalah membalik arah aliran informasi dibandingkan metode sebelumnya: alih-alih mengangkat setiap piksel citra ke ruang 3D lalu menyatukannya, DETR3D menempatkan sekumpulan kueri objek (*object query*) langsung di ruang 3D, memproyeksikan titik acuannya ke setiap citra kamera untuk mengambil fitur yang relevan, kemudian menyempurnakan posisi dan kelas objek lewat lapisan-lapisan *decoder Transformer*. Seluruh proses dilatih *end-to-end* (dari masukan ke keluaran tanpa tahap terpisah) dan prediksi akhir diperoleh lewat pencocokan himpunan (*set prediction*), sehingga tahap *Non-Maximum Suppression* (NMS, penekanan kotak tumpang tindih pasca-prediksi) tidak diperlukan.

Pada *benchmark* nuScenes, DETR3D dengan *backbone* (jaringan ekstraksi fitur dasar) ResNet-101 mencapai *NDS* (nuScenes Detection Score, metrik gabungan nuScenes) 0,425 dan *mAP* (*mean Average Precision*, rata-rata presisi seluruh kelas) 0,346 pada data validasi, mengungguli FCOS3D yang mencapai NDS 0,415 dan mAP 0,343 dengan NMS sebagai pasca-pemrosesan. Kontribusi utamanya bukan sekadar akurasi, melainkan arsitektur kamera-saja pertama yang menyatukan pandangan dari banyak kamera secara implisit lewat kueri 3D bersama, tanpa langkah penggabungan eksplisit di ruang BEV.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum DETR3D, deteksi 3D dari kamera tunggal maupun multi-kamera umumnya mengikuti pola *bottom-up*: setiap piksel atau setiap deteksi 2D pada citra terlebih dahulu diangkat ke ruang 3D, baru kemudian hasil-hasil per kamera digabungkan. FCOS3D, misalnya, memprediksi kotak 3D langsung dari setiap citra kamera secara independen, lalu menyatukan deteksi antar-kamera dengan NMS pada tahap pasca-pemrosesan. Pendekatan berbasis *pseudo-LiDAR* (titik 3D semu) memprediksi peta kedalaman per piksel, mengubahnya menjadi *point cloud* (kumpulan titik 3D), lalu menjalankan detektor 3D di atasnya seperti pada data LiDAR asli.

Pola *bottom-up* ini memiliki tiga kelemahan yang saling terkait. Pertama, estimasi kedalaman per piksel rawan galat, terutama pada objek jauh atau permukaan tanpa tekstur; galat ini merambat ke tahap-tahap berikutnya dan tidak dapat dikoreksi lagi. Kedua, karena setiap kamera diproses terpisah, objek yang terlihat pada dua kamera bertetangga (misalnya di sudut pandang tumpang tindih antara kamera depan dan kamera samping) dapat terdeteksi dua kali dengan posisi 3D yang sedikit berbeda; NMS antar-kamera yang menanganinya bersifat heuristik dan tidak ikut dilatih bersama jaringan. Ketiga, seluruh *pipeline* tidak dioptimalkan menyeluruh terhadap tujuan akhir deteksi 3D, sebab tahap estimasi kedalaman dan tahap deteksi sering dilatih dengan target yang berbeda. Metode berbasis BEV eksplisit, yang muncul kira-kira bersamaan dengan DETR3D, mengatasi sebagian masalah ini dengan memproyeksikan fitur seluruh kamera ke satu peta tampak-atas bersama, tetapi memerlukan pembangunan representasi padat yang berat secara komputasi.

## Ide Utama

Gagasan inti DETR3D adalah menjadikan kueri objek sebagai satu-satunya representasi yang dibagi antar-kamera, dan membiarkan kueri itu sendiri yang menentukan citra bagian mana yang relevan untuknya. Setiap kueri objek adalah vektor yang dipelajari selama pelatihan; jaringan kecil memetakan vektor ini menjadi satu titik acuan 3D di ruang koordinat kendaraan. Titik acuan tersebut diproyeksikan ke setiap citra kamera memakai matriks kalibrasi kamera (parameter intrinsik dan ekstrinsik yang menghubungkan koordinat 3D dunia dengan koordinat piksel 2D). Pada lokasi proyeksi itu, fitur citra diambil lewat interpolasi bilinear (pencampuran nilai empat piksel tetangga berdasarkan jarak) dari peta fitur multi-skala. Fitur dari kamera-kamera yang berhasil melihat titik tersebut dijumlahkan, lalu dipakai untuk menyempurnakan kueri: posisi 3D, dimensi kotak, orientasi, dan kelas objek diperbarui bertahap pada setiap lapisan *decoder*.

Dengan skema ini, penggabungan informasi antar-kamera terjadi di ruang kueri, bukan di ruang fitur citra maupun di ruang BEV. Tidak ada peta padat yang harus dibangun untuk seluruh area di sekitar kendaraan; hanya sejumlah kecil kueri (ratusan, bukan puluhan ribu sel BEV) yang diproses. Karena satu kueri dapat menarik fitur dari beberapa kamera sekaligus, masalah duplikasi deteksi pada sudut pandang tumpang tindih berkurang tanpa memerlukan NMS eksplisit.

## Cara Kerja Langkah demi Langkah

### Ekstraksi Fitur Multi-Kamera

Setiap citra dari enam kamera nuScenes (depan, depan-kiri, depan-kanan, belakang, belakang-kiri, belakang-kanan) diproses oleh *backbone* konvolusi bersama (ResNet-50/ResNet-101, atau VoVNet pada beberapa varian) dilengkapi *Feature Pyramid Network* (FPN, jaringan piramida fitur yang menghasilkan peta fitur pada beberapa resolusi). Keluarannya adalah empat tingkat peta fitur per kamera dengan resolusi menurun bertahap, sehingga objek besar dan objek kecil sama-sama terwakili pada skala yang sesuai.

### Kueri Objek dan Titik Acuan 3D

Model memakai sejumlah kueri objek yang dipelajari — makalah melaporkan bahwa 900 kueri memberi kinerja terbaik pada eksperimen ablasi mereka, dengan penambahan lebih lanjut tidak lagi memberi perbaikan berarti. Setiap kueri melewati jaringan umpan-maju kecil (Φ_ref) yang menghasilkan satu titik koordinat 3D (x, y, z) di ruang referensi kendaraan. Titik ini berperan sebagai hipotesis awal posisi objek yang diwakili kueri tersebut.

### Proyeksi 3D-ke-2D dan Sampling Fitur

Titik acuan 3D diproyeksikan ke bidang citra tiap-tiap kamera memakai matriks proyeksi kamera (hasil kali parameter intrinsik dan ekstrinsik yang sudah dikalibrasi). Karena satu titik 3D umumnya hanya terlihat dalam satu atau dua dari enam kamera akibat sudut pandang yang tidak saling tumpang tindih sepenuhnya, proyeksi yang jatuh di luar batas citra ditandai tidak valid lewat mask biner dan diabaikan. Pada proyeksi yang valid, fitur diambil dengan interpolasi bilinear dari peta fitur FPN pada level yang sesuai, kemudian fitur dari seluruh kamera valid dijumlahkan menjadi satu vektor fitur per kueri.

Diagram berikut meringkas alur dari kueri ke fitur teragregasi:

```
6 citra kamera --> backbone+FPN --> peta fitur multi-skala (per kamera)
                                            ^
kueri objek (900) --> titik acuan 3D (x,y,z)
                            |
                proyeksi ke tiap kamera (matriks kalibrasi)
                            |
                titik 2D valid pada kamera 1..k (mask biner)
                            |
                interpolasi bilinear -> fitur per kamera valid
                            |
                    penjumlahan fitur --> perbarui kueri
```

Diagram ini menegaskan bahwa jumlah kueri, bukan jumlah sel BEV, yang menentukan biaya komputasi tahap penggabungan; setiap kueri hanya menarik fitur dari kamera yang relevan, bukan dari seluruh area pemandangan.

### Decoder Transformer dan Penyempurnaan Bertahap

Fitur teragregasi dipakai memperbarui representasi kueri lewat lapisan *self-attention* (kueri saling bertukar informasi) dan umpan-maju, mengikuti struktur *decoder* DETR (*Detection Transformer*, model deteksi berbasis Transformer yang merumuskan deteksi sebagai prediksi himpunan langsung). Proses titik-acuan-ke-proyeksi-ke-fitur-ke-pembaruan-kueri diulang pada enam lapisan *decoder*; posisi 3D disempurnakan bertahap pada tiap lapisan, bukan diprediksi sekali. Kepala prediksi akhir pada tiap lapisan menghasilkan kelas objek, pusat 3D, dimensi kotak, dan orientasi (*yaw*).

### Fungsi Loss dan Pencocokan Himpunan

Pelatihan memakai pencocokan bipartit Hungaria (algoritme optimasi yang mencari pasangan satu-satu optimal) antara himpunan prediksi dan himpunan kotak kebenaran (*ground truth*), sehingga setiap objek nyata dipasangkan tepat dengan satu kueri prediksi tanpa memerlukan *anchor* (kotak jangkar bawaan) maupun NMS. Loss klasifikasi memakai *focal loss* (varian *cross-entropy* yang menekan bobot contoh mudah agar pelatihan fokus pada contoh sulit), sedangkan loss regresi kotak memakai L1 (jumlah selisih mutlak) pada parameter posisi, dimensi, dan orientasi. Karena pencocokan dan loss dihitung pada level himpunan, jaringan dilatih *end-to-end* dari citra mentah sampai kotak 3D akhir.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada nuScenes, *benchmark* deteksi 3D untuk kendaraan otonom yang berisi data dari enam kamera, radar, dan LiDAR, meski DETR3D hanya memakai citra kamera. Metrik utamanya adalah mAP dan NDS; NDS menggabungkan mAP dengan galat translasi, skala, orientasi, kecepatan, dan atribut menjadi satu skor tunggal.

Pada data validasi, DETR3D dengan *backbone* ResNet-101 mencapai NDS 0,425 dan mAP 0,346 tanpa NMS, sedangkan FCOS3D terbaik pada pengaturan sebanding mencapai NDS 0,415 dan mAP 0,343 dengan NMS. Interpretasinya: DETR3D mengungguli metode kamera-saja *bottom-up* sekaligus menghilangkan tahap pasca-pemrosesan heuristik, menunjukkan bahwa penggabungan lewat kueri 3D bersama mencukupi tanpa perlu NMS antar-kamera. Pada data uji (*test set*) tersembunyi nuScenes, DETR3D mencapai NDS 0,479 dan mAP 0,412, sebanding dengan metode kamera-saja terkuat lain pada masanya seperti DD3D.

Studi ablasi menunjukkan dua temuan penting. Pertama, penyempurnaan bertahap lewat enam lapisan *decoder* memberi kenaikan progresif — NDS lapisan pertama sekitar 0,380 naik menjadi 0,425 pada lapisan keenam — membuktikan bahwa proyeksi-dan-sampling berulang, bukan sekali jalan, yang mendorong akurasi. Kedua, jumlah kueri 900 memberi keseimbangan terbaik; menambah kueri lebih lanjut tidak memberi perbaikan berarti karena jumlah objek nyata per adegan pada nuScenes terbatas. Backbone yang lebih besar (ResNet-101 dibandingkan ResNet-50 atau DLA34) secara konsisten memberi skor lebih tinggi, sejalan dengan pola umum bahwa fitur citra yang lebih kaya mempermudah estimasi posisi 3D.

Penulis mencatat bahwa galat translasi (pergeseran posisi pusat objek dari nilai sebenarnya) tetap menjadi komponen galat terbesar meskipun DETR3D menghindari estimasi kedalaman eksplisit, menunjukkan bahwa kesulitan mendasar memperkirakan jarak dari citra 2D belum sepenuhnya teratasi oleh perubahan arsitektur.

## Kelebihan dan Keterbatasan

Kelebihan DETR3D meliputi: (1) penggabungan multi-kamera implisit lewat kueri bersama tanpa representasi BEV padat yang mahal secara komputasi; (2) pelatihan *end-to-end* penuh tanpa NMS, sehingga seluruh komponen dioptimalkan terhadap tujuan deteksi akhir; (3) jumlah kueri yang jauh lebih sedikit daripada jumlah sel pada peta BEV, sehingga biaya komputasi tahap penggabungan tetap rendah; (4) pemakaian langsung matriks kalibrasi kamera sebagai penghubung geometris antara ruang 3D dan ruang citra, tanpa jaringan tambahan untuk mempelajari hubungan ini.

Keterbatasan yang diakui penulis: galat translasi tetap dominan, menandakan estimasi jarak dari citra kamera tanpa depth eksplisit masih menjadi hambatan utama akurasi. Keterbatasan lain merupakan analisis penulis bab ini, bukan pernyataan eksplisit makalah. Dari sisi rekayasa, mekanisme proyeksi bergantung penuh pada kalibrasi kamera yang akurat; kesalahan kalibrasi ekstrinsik akan langsung menggeser titik sampling fitur dan menurunkan kualitas deteksi, tanpa mekanisme koreksi di dalam arsitektur. Secara konseptual, versi dasar DETR3D tidak memanfaatkan informasi temporal antar-*frame* video, sehingga objek yang sesaat tertutup (*occluded*) pada satu *frame* tidak mendapat bantuan konteks dari *frame* sebelumnya — keterbatasan yang menjadi arah pengembangan metode-metode kamera-saja berikutnya. Dibandingkan detektor berbasis LiDAR, akurasi kamera-saja seperti DETR3D pada umumnya masih di bawahnya untuk kelas objek kecil dan jarak jauh, konsekuensi wajar dari ketiadaan pengukuran jarak langsung yang dimiliki sensor laser.

## Kaitan dengan Bab Lain

DETR3D memperluas rumusan *set prediction* berbasis kueri milik DETR ke ruang 3D. Bab 165 (Co-DETR) membahas garis pengembangan arsitektur DETR di ranah 2D, termasuk perbaikan pencocokan label dan konvergensi pelatihan yang menjadi latar teknis bagi keluarga DETR yang diwarisi DETR3D. Dataset nuScenes yang dipakai untuk seluruh evaluasi dijelaskan lebih rinci pada bab 145 (nuScenes), termasuk struktur enam kamera, radar, LiDAR, dan definisi metrik NDS yang dipakai bersama oleh seluruh bab klaster Deteksi 3D.

Dalam klaster Deteksi 3D, DETR3D berdiri berseberangan secara arsitektural dengan bab 185 (CenterPoint) dan bab 186 (PV-RCNN), yang keduanya bekerja pada data LiDAR memakai representasi voxel atau titik padat, bukan kueri sparse berbasis kamera. Perbandingan paling langsung ada dengan bab 187 (BEVFormer), yang juga kamera-saja tetapi memilih membangun representasi BEV eksplisit lewat *attention* spatiotemporal, berlawanan dengan pilihan DETR3D menghindari representasi padat sama sekali. Kedua pendekatan — kueri sparse langsung ke 3D pada DETR3D versus BEV padat pada BEVFormer — mewakili dua cabang utama metode deteksi 3D kamera-saja yang berkembang paralel setelah kedua makalah ini terbit.

## Poin untuk Sitasi

Kutip dengan kunci `wang2022detr3d`. Ringkasan yang aman dikutip: "DETR3D memproyeksikan titik acuan 3D dari kueri objek yang dipelajari ke citra multi-kamera memakai matriks kalibrasi untuk mengambil fitur lewat interpolasi bilinear, lalu menyempurnakan kotak 3D lewat enam lapisan decoder Transformer tanpa NMS maupun representasi BEV eksplisit, mencapai NDS 0,425 dan mAP 0,346 pada data validasi nuScenes dengan backbone ResNet-101." Angka NDS/mAP validasi (0,425/0,346), angka data uji (NDS 0,479/mAP 0,412), jumlah kueri optimal (900), jumlah lapisan decoder (6), dan detail progresi ablasi per lapisan (NDS 0,380 pada lapisan pertama) diperoleh dari pembacaan naskah lewat alat pengambil konten otomatis, bukan dari tabel asli yang dibaca langsung baris per baris — sebaiknya diverifikasi ulang ke Tabel 1, Tabel 2, dan Tabel 6 pada naskah arXiv/CoRL sebelum dikutip dalam karya formal.
