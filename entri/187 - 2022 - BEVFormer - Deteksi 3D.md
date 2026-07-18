# 187 - BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2022bevformer` |
| Judul asli | BEVFormer: Learning Bird's-Eye-View Representation from Multi-Camera Images via Spatiotemporal Transformers |
| Penulis | Zhiqi Li, Wenhai Wang, Hongyang Li, Enze Xie, Chonghao Sima, Tong Lu, Yu Qiao, Jifeng Dai |
| Tahun | 2022 |
| Venue | European Conference on Computer Vision (ECCV 2022) |
| Tema | Deteksi 3D |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2203.17270
- **Kode resmi (GitHub):** https://github.com/fundamentalvision/BEVFormer
- **Google Scholar:** https://scholar.google.com/scholar?q=BEVFormer%3A%20Learning%20Bird%27s-Eye-View%20Representation%20from%20Multi-Camera%20Images

## Gambaran Umum

BEVFormer adalah kerangka kerja persepsi 3D yang membangun representasi *bird's-eye-view* (BEV, tampak-atas) terpadu dari citra beberapa kamera saja, tanpa memerlukan sensor *LiDAR* (sensor laser penghasil titik-titik jarak/*point cloud*). Representasi BEV dibangun oleh sekumpulan *query* (vektor kueri yang dapat dipelajari, berfungsi sebagai "sel" pada peta tampak-atas) yang mengambil fitur dari citra multi-kamera melalui *spatial cross-attention* (mekanisme atensi silang yang menghubungkan setiap kueri BEV dengan wilayah citra kamera yang relevan) dan menggabungkan informasi dari *frame* (bingkai) waktu sebelumnya melalui *temporal self-attention* (atensi diri yang menghubungkan kueri BEV pada waktu sekarang dengan kueri BEV pada waktu lampau). Representasi BEV yang dihasilkan bersifat umum: dapat dipakai baik untuk kepala deteksi 3D maupun kepala segmentasi peta semantik tanpa mengubah tulang punggung (*backbone*, jaringan ekstraksi fitur dasar) BEV itu sendiri.

Pada benchmark nuScenes, varian BEVFormer-base mencapai 51,7% NDS (*nuScenes Detection Score*, metrik gabungan kualitas deteksi 3D) dan 41,6% mAP (*mean Average Precision*, rata-rata presisi deteksi) pada set validasi. Pada set uji (*test set*), model ini mencapai 56,9% NDS, unggul 9,0 poin dari metode kamera-saja terbaik sebelumnya, dan mendekati kinerja beberapa metode berbasis LiDAR pada metrik tertentu. Kontribusi utamanya adalah menunjukkan bahwa informasi temporal, yang sebelumnya jarang dimanfaatkan secara eksplisit pada deteksi 3D berbasis kamera, dapat meningkatkan akurasi deteksi objek bergerak dan estimasi kecepatan secara signifikan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sistem persepsi kendaraan otonom umumnya mengandalkan LiDAR karena data titik 3D yang dihasilkannya langsung memberi informasi jarak yang akurat, seperti dimanfaatkan pada CenterPoint (bab 185) dan PV-RCNN (bab 186). Sensor LiDAR mahal dan rentan terhadap kondisi cuaca tertentu, sehingga persepsi berbasis kamera saja menjadi alternatif yang lebih murah dan lebih mudah dipasang secara masal. Masalahnya, citra kamera adalah proyeksi 2D dari dunia 3D — informasi kedalaman hilang pada satu citra tunggal, dan kendaraan otonom biasanya memakai enam kamera atau lebih yang memandang arah berbeda, sehingga sistem harus menyatukan pandangan-pandangan terpisah itu menjadi satu representasi 3D yang konsisten secara geometris.

Pendekatan sebelumnya seperti *Lift-Splat-Shoot* (LSS) dan BEVDet memproyeksikan fitur citra ke ruang BEV dengan memprediksi distribusi kedalaman per piksel, lalu menyebarkan (*splat*) fitur ke sel BEV sesuai kedalaman itu. Pendekatan ini bergantung pada estimasi kedalaman eksplisit yang cenderung tidak akurat pada kamera murni, sehingga kesalahan kedalaman menjalar menjadi kesalahan posisi objek pada BEV. DETR3D (bab 188), pendekatan lain yang sezaman, memakai kueri objek 3D yang diproyeksikan kembali ke citra 2D untuk mengambil fitur, tetapi tidak menghasilkan representasi BEV yang padat dan tidak memanfaatkan informasi antar-*frame* waktu. Akibatnya, model-model kamera-saja pada masa itu kesulitan mendeteksi objek yang tertutup sebagian (*occlusion*) dan kesulitan mengestimasi kecepatan objek, karena kecepatan hanya dapat disimpulkan dari perubahan posisi antar-waktu, sedangkan kebanyakan metode hanya memproses satu *frame* per prediksi.

## Ide Utama

Gagasan inti BEVFormer adalah membangun satu grid kueri BEV yang dapat dipelajari, lalu mengisi kueri tersebut dengan dua jenis atensi berurutan: atensi spasial yang mengambil fitur dari kamera pada waktu sekarang, dan atensi temporal yang mengambil fitur dari representasi BEV pada waktu sebelumnya. Grid kueri ini berbentuk H×W posisi tetap pada bidang tampak-atas di sekitar kendaraan, misalnya grid berukuran 200×200 yang mencakup area 102,4×102,4 meter — setiap sel grid berukuran sekitar 0,512×0,512 meter dan berkaitan dengan satu lokasi tetap di dunia nyata, terlepas dari susunan kamera.

Setiap kueri BEV, alih-alih menyorot seluruh piksel citra dari semua kamera (yang mahal secara komputasi karena jumlah piksel dari enam kamera sangat besar), hanya menyorot sejumlah kecil titik acuan (*reference point*) pada citra kamera yang relevan secara geometris — hasil proyeksi lokasi 3D kueri itu ke bidang gambar kamera memakai kalibrasi kamera yang diketahui. Mekanisme penyorotan titik acuan yang jarang (bukan seluruh citra) ini disebut *deformable attention* (atensi yang dapat berubah bentuk, memilih sendiri titik-titik penting alih-alih memproses seluruh masukan secara merata), yang sebelumnya diperkenalkan pada Deformable DETR (bab 023) untuk mempercepat atensi pada deteksi 2D. BEVFormer memperluas gagasan itu ke ruang 3D dan ke banyak kamera sekaligus.

## Cara Kerja Langkah demi Langkah

### Kueri BEV dan Posisi 3D

Grid kueri BEV berukuran H×W (misalnya 200×150 pada konfigurasi dasar) diinisialisasi sebagai parameter yang dapat dipelajari, masing-masing ditambah *embedding* posisi (representasi vektor dari lokasi) yang menandai koordinat (x, y) pada bidang BEV. Setiap sel BEV mewakili wilayah nyata seluas beberapa puluh sentimeter persegi di sekitar kendaraan. Karena BEV adalah tampak-atas, sumbu tinggi (z) tidak diwakili langsung oleh grid; ketinggian ditangani dengan mengambil sampel pada beberapa titik acuan di sepanjang sumbu z untuk setiap sel sebelum diproyeksikan ke kamera.

### Spatial Cross-Attention

Untuk mengisi setiap kueri BEV dengan informasi visual, sistem memproyeksikan titik-titik acuan 3D milik kueri itu (pada beberapa ketinggian z) ke bidang gambar setiap kamera memakai parameter kalibrasi ekstrinsik dan intrinsik kamera. Sebagian titik acuan jatuh di dalam bidang pandang satu atau dua kamera yang bertetangga (karena kamera-kamera pada kendaraan saling tumpang tindih di tepi), sedangkan titik yang jatuh di luar bidang pandang kamera tertentu diabaikan untuk kamera itu. Pada titik-titik yang valid, *deformable attention* mengambil fitur dari sekitar titik proyeksi tersebut pada peta fitur citra kamera, lalu menjumlahkan fitur dari seluruh kamera yang relevan menjadi satu vektor pembaruan untuk kueri BEV bersangkutan. Dengan cara ini, satu kueri BEV dapat menggabungkan informasi dari lebih dari satu kamera tanpa harus memproses citra secara penuh.

### Temporal Self-Attention

Selain fitur spasial dari kamera saat ini, setiap kueri BEV juga menyorot representasi BEV historis dari *frame* sebelumnya (BEV lampau, hasil dari langkah waktu t−1) pada lokasi yang sama secara geometris, setelah posisi BEV lampau disejajarkan ulang (*warp*, transformasi koordinat) sesuai pergerakan kendaraan (*ego-motion*) antara dua *frame*. Penyejajaran ini penting karena kendaraan bergerak, sehingga grid BEV pada waktu t dan t−1 tidak menunjuk ke titik dunia nyata yang sama tanpa dikoreksi. Setelah disejajarkan, atensi diri menggabungkan fitur BEV sekarang dengan fitur BEV lampau, sehingga model memperoleh isyarat gerak: objek yang berpindah antar-*frame* menghasilkan perbedaan fitur yang dapat dipakai kepala deteksi untuk mengestimasi kecepatan dan mengenali objek yang sedang tertutup sebagian pada *frame* saat ini tetapi terlihat pada *frame* sebelumnya. Proses ini berjalan berulang (rekursif) dari satu *frame* ke *frame* berikutnya, sehingga BEV pada waktu t membawa jejak informasi dari banyak *frame* sebelumnya, bukan hanya satu langkah ke belakang.

Diagram berikut merangkum alur satu langkah waktu pemrosesan BEVFormer:

```
enam citra kamera (t)          BEV historis (t-1, disejajarkan)
   │  ekstraksi fitur (backbone)         │
   ▼                                     ▼
peta fitur multi-kamera         grid kueri BEV (H x W)
   │                                     │
   └──── spatial cross-attention ───►[kueri BEV]◄─── temporal self-attention
              (titik acuan 3D)            │
                                          ▼
                                  BEV terbarukan (t)
                                    │            │
                              kepala deteksi   kepala segmentasi
                              (kotak 3D)       (peta semantik)
```

### Kepala Deteksi dan Segmentasi

Representasi BEV yang telah diperbarui pada tiap langkah waktu berfungsi sebagai fitur bersama untuk dua kepala tugas. Kepala deteksi 3D, mengikuti desain berbasis kueri dari DETR3D, memprediksi kotak 3D beserta orientasi dan kecepatan objek langsung dari fitur BEV. Kepala segmentasi memprediksi peta semantik BEV, misalnya batas jalan dan lokasi kendaraan lain, dari representasi BEV yang sama. Karena kedua kepala memakai fitur BEV yang identik, BEVFormer dapat dilatih untuk kedua tugas sekaligus tanpa membangun dua jalur ekstraksi fitur terpisah.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada nuScenes (bab 145), *benchmark* deteksi 3D berkendara berisi data dari enam kamera, radar, dan LiDAR yang direkam di area perkotaan, dengan metrik NDS (skor gabungan yang menimbang akurasi posisi, ukuran, orientasi, kecepatan, dan atribut kotak 3D) dan mAP (presisi rata-rata deteksi diukur pada beberapa ambang jarak). Tiga konfigurasi model diuji pada set validasi: BEVFormer-tiny dengan tulang punggung ResNet-50 mencapai 35,4% NDS dan 25,2% mAP; BEVFormer-small dengan tulang punggung ResNet-101-DCN mencapai 47,9% NDS dan 37,0% mAP; BEVFormer-base, juga dengan ResNet-101-DCN tetapi resolusi dan jumlah kueri lebih besar, mencapai 51,7% NDS dan 41,6% mAP. Kenaikan bertahap dari *tiny* ke *base* menunjukkan bahwa kapasitas tulang punggung dan resolusi fitur berkontribusi langsung pada akurasi, sejalan dengan pola umum pada detektor berbasis Transformer.

Pada set uji nuScenes, BEVFormer mencapai 56,9% NDS, unggul 9,0 poin di atas metode kamera-saja terbaik sebelumnya pada saat publikasi. Selisih 9,0 poin ini tergolong besar untuk metrik gabungan seperti NDS, yang biasanya bergerak dalam kenaikan satu-dua poin antar-generasi metode; besarnya selisih ini terutama berasal dari kontribusi *temporal self-attention* terhadap estimasi kecepatan dan deteksi objek yang tertutup sebagian, dua aspek yang sulit ditangani metode kamera tunggal per-*frame*. Studi ablasi pada makalah menunjukkan bahwa menghapus *temporal self-attention* menurunkan NDS secara jelas dibandingkan model penuh, mengonfirmasi bahwa konteks temporal, bukan hanya spasial, adalah sumber utama peningkatan akurasi dibandingkan pendekatan kamera-saja berbasis satu *frame* seperti DETR3D.

## Kelebihan dan Keterbatasan

Kelebihan utama BEVFormer adalah representasi BEV tunggal yang dapat dipakai untuk banyak tugas persepsi (deteksi dan segmentasi) tanpa perubahan arsitektur besar, serta pemanfaatan eksplisit informasi temporal yang terbukti meningkatkan akurasi kecepatan dan ketahanan terhadap oklusi. *Deformable attention* pada kueri BEV membuat komputasi atensi tidak meledak sebanding jumlah piksel citra dari enam kamera, sehingga metode tetap dapat dilatih dengan sumber daya yang wajar dibandingkan atensi penuh (*full attention*) pada seluruh piksel.

Dari sisi rekayasa, ketergantungan pada kalibrasi kamera yang akurat merupakan kelemahan struktural: proyeksi titik acuan 3D ke bidang gambar memerlukan parameter ekstrinsik dan intrinsik kamera yang presisi, sehingga kesalahan kalibrasi menjalar langsung menjadi kesalahan penyorotan fitur. Secara konseptual, komputasi Transformer pada grid BEV berukuran besar (misalnya 200×200 sel) dan enam kamera sekaligus tetap lebih berat dibandingkan detektor konvolusi konvensional, sehingga penerapan pada perangkat keras berdaya rendah memerlukan optimisasi tambahan. Selain itu, sebagai metode kamera-saja, BEVFormer masih berada di bawah metode berbasis LiDAR pada metrik akurasi posisi murni, terutama pada jarak jauh, karena kamera tidak memberi ukuran jarak langsung seperti titik LiDAR.

## Kaitan dengan Bab Lain

BEVFormer berada pada klaster Deteksi 3D bersama CenterPoint (bab 185, deteksi berbasis titik pusat pada data LiDAR) dan PV-RCNN (bab 186, penggabungan fitur titik dan *voxel* pada LiDAR); kedua bab itu menjadi pembanding berbasis LiDAR yang coba didekati kinerjanya oleh BEVFormer tanpa LiDAR. Bab ini juga berhubungan erat dengan bab 188 (DETR3D), karena kepala deteksi BEVFormer mewarisi desain kueri objek 3D dari DETR3D, sementara BEVFormer menambahkan lapisan representasi BEV terpadu dan atensi temporal yang tidak dimiliki DETR3D. Mekanisme *deformable attention* yang dipakai pada *spatial cross-attention* diwarisi langsung dari Deformable DETR (bab 023), yang aslinya dirancang untuk mempercepat atensi pada deteksi 2D; BEVFormer memperluasnya ke pengambilan fitur lintas-kamera dan lintas-waktu. Dataset nuScenes (bab 145) menjadi tolok ukur evaluasi tunggal pada bab ini, sekaligus sumber data multi-kamera dan multi-*frame* yang membuat mekanisme temporal BEVFormer relevan untuk diuji.

## Poin untuk Sitasi

Kutip dengan kunci `li2022bevformer`. Ringkasan aman untuk dikutip: BEVFormer membangun representasi *bird's-eye-view* terpadu dari citra multi-kamera memakai kueri BEV yang dapat dipelajari, dipadukan lewat *spatial cross-attention* antar-kamera dan *temporal self-attention* antar-*frame*, mencapai 56,9% NDS pada set uji nuScenes (unggul 9,0 poin dari metode kamera-saja terbaik sebelumnya) dan 51,7% NDS/41,6% mAP untuk konfigurasi BEVFormer-base pada set validasi. Angka NDS/mAP untuk varian *tiny* (35,4%/25,2%) dan *small* (47,9%/37,0%) diambil dari repositori kode resmi, bukan langsung dari tabel abstrak makalah, sehingga sebaiknya dicocokkan ulang dengan tabel eksperimen lengkap pada naskah sebelum dikutip dalam karya formal. Rincian hasil segmentasi peta semantik (IoU) dan hasil studi ablasi temporal secara numerik tidak diverifikasi dalam penulisan bab ini dan perlu dicek langsung ke naskah asli.
