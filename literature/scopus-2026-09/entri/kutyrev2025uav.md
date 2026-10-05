# UAV-based sustainable orchard management: deep learning for apple detection and yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kutyrev2025uav` |
| Judul asli | UAV-based sustainable orchard management: deep learning for apple detection and yield estimation |
| Penulis | Kutyrev, Alexey; Khort, Dmitry; Smirnov, Igor; Zubina, Valeria |
| Tahun | 2025 |
| Venue | E3s Web of Conferences |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [kutyrev2025uav.pdf](../pdf/kutyrev2025uav.pdf)
- DOI resmi: https://doi.org/10.1051/e3sconf/202561403021

## Gambaran Umum
Makalah prosiding ini (E3S Web of Conferences 614, ICAW 2024) mengusulkan metode penghitungan apel otomatis dari citra beresolusi tinggi hasil pesawat nirawak (*unmanned aerial vehicle*, UAV). Citra direkam dengan kamera RGB 20 MP pada DJI Mavic 3 Multispectral di kebun apel industri, diubah menjadi ortofoto dengan Agisoft Metashape, dipotong menjadi petak (*tile*) 200×200 piksel, dideteksi dengan model YOLO11 (varian n, s, m, l, x), lalu hasilnya digabung kembali ke ortofoto dengan koordinat spasial yang terjaga. Dua kelas dideteksi: `apple` (apel pada pohon) dan `fallen_apple` (apel jatuh).

Data awal berupa 11 citra beresolusi 5280×3956 piksel yang diperbanyak dengan augmentasi menjadi 2.000 citra berisi 51.797 objek (34.383 `apple` dan 17.414 `fallen_apple`). Model terbaik, YOLO11x, mencapai mAP50 0,81602, mAP50-95 0,54721, *precision* 0,85193, dan *recall* 0,76625. Evaluasi terbatas pada akurasi deteksi; makalah tidak melaporkan galat hitungan terhadap hitungan lapangan atau panen.

Makalah juga mengusulkan koefisien koreksi untuk buah yang tersembunyi dari kamera, tetapi koefisien itu belum ditentukan dan menjadi pekerjaan lanjutan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penilaian hasil kebun secara tradisional bergantung pada pengamatan visual agronom yang subjektif sehingga menimbulkan galat besar pada prakiraan hasil. Sensor darat dan kamera tetap terbatas cakupannya, pencitraan hiperspektral dan termal memerlukan peralatan serta pengolahan khusus, dan pemindai laser (LiDAR) mahal serta sulit ditafsirkan. UAV dinilai mampu mengumpulkan data dengan cepat, tetapi menurut penulis kebanyakan pendekatan pemantauan berbasis UAV dioptimalkan untuk tanaman lapangan atau hutan, bukan kebun intensif berkepadatan tanam tinggi.

Kebun apel intensif menyulitkan deteksi karena interaksi cahaya dengan kanopi, buah dan daun yang saling menutupi, tekstur tanaman yang rumit, serta variasi pencahayaan dan bayangan. Penulis menyatakan perlunya metode yang disesuaikan dengan citra kebun beresolusi tinggi dari UAV.

## Ide Utama
Gagasan utamanya adalah memisahkan citra ortofoto besar menjadi petak kecil berukuran tetap agar detektor YOLO11 dapat melihat buah kecil secara rinci dengan beban komputasi terkendali, kemudian menyatukan hasil deteksi per petak menjadi satu peta kebun berkoordinat. Jumlah apel total dihitung sebagai jumlah deteksi per petak. Nama berkas setiap petak memuat posisinya pada sumbu X dan Y sehingga hasil dapat dikembalikan ke geometri ortofoto asli.

Gagasan tambahan, yang baru diusulkan, adalah koefisien koreksi $K_{corr}$ per petak untuk buah yang tidak terlihat dari atas, ditentukan secara eksperimental dari perbandingan citra dengan hitungan manual pada sampel pohon.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Citra diambil dengan DJI Mavic 3 Multispectral; hanya kamera RGB yang dipakai (sensor CMOS 4/3 inci, 20 MP, panjang fokus 24 mm, apertur f/2.8, sudut pandang 84°, resolusi maksimum 5280×3956 piksel). Penerbangan dilakukan pada ketinggian 30–60 m, cuaca cerah, siang hari. Lokasi dan kultivar tidak dilaporkan; makalah hanya menyebut kebun industri dengan apel yang telah masak. Jumlah pohon tidak dilaporkan.

### 2. Pembuatan ortofoto
Foto udara diproses dengan Agisoft Metashape: penyelarasan citra, pembuatan awan titik padat, dan pembuatan ortomosaik dalam format GeoTIFF.

### 3. Pemotongan menjadi petak
Ortofoto dipotong dengan skrip Python (pustaka PIL) menjadi petak 200×200 piksel. Setiap petak diberi nama unik yang memuat posisi X dan Y.

### 4. Anotasi dan augmentasi
Anotasi kotak pembatas dilakukan manual dengan layanan Roboflow untuk dua kelas. Augmentasi meliputi transformasi *Tile* 8×8, pembalikan horizontal dan vertikal, penyesuaian rona (*hue*) hingga 15%, dan pengaburan (*blur*) dengan koefisien 1%. Data awal 11 citra menjadi 2.000 citra.

### 5. Pelatihan detektor
Model YOLO11n, s, m, l, dan x berbobot terlatih (*transfer learning*) dilatih dengan batch 12, laju belajar 0,1, dan 1.500 epoch, dengan penghentian dini bila metrik validasi tidak membaik. *Non-Maximum Suppression* (NMS) menyingkirkan kotak tumpang tindih berkeyakinan rendah. Pelatihan memakai komputer dengan Intel Core i9-10900X dan dua GPU GeForce RTX 2080Ti (masing-masing 11 GB). Pembagian data latih, validasi, dan uji tidak dilaporkan.

### 6. Penggabungan dan penghitungan
Hasil deteksi per petak digabung kembali berdasarkan koordinat pada nama berkas. Makalah menyebut bahwa tumpang tindih antarpetak diperhitungkan dan algoritma penghapusan irisan dipakai untuk mencegah penghitungan ganda, tetapi tidak menjelaskan prosedurnya. Jumlah total apel dihitung sebagai $N_{total}=\sum_{i=1}^{n} n_i$, dengan $n_i$ jumlah buah terdeteksi pada petak ke-$i$.

### 7. Koefisien koreksi (usulan)
Rumus yang diusulkan menjumlahkan deteksi yang keyakinannya mencapai ambang $T$ (misalnya 0,5), masing-masing dikalikan koefisien koreksi $K_{corr,ij}$ per petak. Sebagai contoh, pada area berdaun lebat $K_{corr}$ dapat bernilai 1,5 sampai 2 dan pada area berdaun jarang mendekati 1. Nilai ini belum ditentukan secara empiris di makalah. Penulis juga mengusulkan citra miring dan model 3D untuk menjangkau buah tersembunyi.

### 8. Antarmuka
Antarmuka grafis berbasis Tkinter menampilkan hasil deteksi pada citra gabungan, ringkasan jumlah apel per bagian kebun dari berkas teks, dan ekspor data.

## Eksperimen dan Hasil
Evaluasi memakai *precision*, *recall*, mAP50, dan mAP50-95 pada kelima varian YOLO11. Tabel 1 makalah melaporkan nilai berikut (dibulatkan dua desimal oleh penulis; urutan kolom pada tabel asli adalah n, s, l, m, x).

| Metrik | YOLO11n | YOLO11s | YOLO11m | YOLO11l | YOLO11x |
|---|---|---|---|---|---|
| mAP50 | 0,73 | 0,77 | 0,77 | 0,80 | 0,81 |
| mAP50-95 | 0,38 | 0,46 | 0,51 | 0,52 | 0,54 |
| Precision | 0,78 | 0,81 | 0,83 | 0,84 | 0,85 |
| Recall | 0,71 | 0,73 | 0,74 | 0,77 | 0,76 |

Dalam teks, nilai tidak dibulatkan dilaporkan untuk YOLO11x: mAP50 0,81602, mAP50-95 0,54721, *precision* 0,85193, *recall* 0,76625; untuk YOLO11l mAP50 0,80041 dan untuk YOLO11m mAP50 0,77836. Penulis menyatakan YOLO11l dan YOLO11x unggul, YOLO11l menawarkan keseimbangan antara kinerja dan biaya komputasi, sedangkan YOLO11n dan YOLO11s cocok untuk lingkungan berdaya komputasi terbatas. Titik stabilisasi pelatihan dinyatakan berada pada kisaran 600 sampai 800 iterasi. Makalah juga memuat nilai *loss* validasi dan latih pada Tabel 1.

Tidak ada hasil per kelas (`apple` terhadap `fallen_apple`), tidak ada perbandingan dengan hitungan manual atau panen, dan tidak ada galat hitungan total yang dilaporkan.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: pemrosesan per petak menurunkan beban komputasi sambil mempertahankan akurasi deteksi; penggabungan hasil menjaga informasi geospasial sehingga sebaran buah dapat divisualisasikan; metode dinyatakan mengurangi biaya tenaga kerja dan meningkatkan skalabilitas pemantauan.

Keterbatasan yang dinyatakan penulis: pemotretan vertikal tidak mencakup seluruh buah sehingga buah tersembunyi tidak terhitung; karena itu diusulkan koefisien koreksi dan citra miring untuk model 3D, serta integrasi data multispektral sebagai pekerjaan lanjutan.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan tambahan. Hanya 11 citra asli yang dipakai, dan makalah tidak menjelaskan apakah pembagian latih, validasi, dan uji dilakukan sebelum atau sesudah augmentasi, sehingga kebocoran data tidak dapat dikesampingkan. Tidak ada validasi hitungan terhadap acuan lapangan. Prosedur penghapusan penghitungan ganda pada petak yang tumpang tindih tidak dirinci. Selisih nilai antara tabel dan teks untuk YOLO11m dan YOLO11l (urutan kolom l dan m tertukar pada tabel) perlu dicermati saat mengutip.

## Kaitan dengan Tinjauan main6
Makalah ini tidak menangani buah yang terlihat lebih dari sekali sebagai masalah identitas. Satu-satunya mekanisme yang menyerupai pengelolaan duplikasi adalah penghapusan irisan antarpetak pada ortofoto (tanpa rincian), yaitu duplikasi spasial pada satu mosaik, bukan pencocokan antarpandang atau antarsisi pohon. Penghitungan berupa penjumlahan deteksi per petak dari satu pandang atas. Hitungan tidak dilaporkan per kelas kematangan; dua kelas yang ada (apel pada pohon dan apel jatuh) hanya membedakan posisi buah, dan hasil metrik tidak dirinci per kelas. Acuan yang dipakai hanyalah anotasi citra; hitungan manual lapangan baru diusulkan untuk menentukan koefisien koreksi.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah gagasan koefisien koreksi untuk buah tersembunyi yang dikalibrasi terhadap hitungan manual pada sampel pohon, serta usulan citra miring untuk menjangkau buah yang tertutup. Nilai koefisien yang disebut (1,5 sampai 2) hanya contoh dan tidak diturunkan dari data.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `kutyrev2025uav`.

Kutyrev dkk. mengusulkan penghitungan apel otomatis dari ortofoto hasil UAV dengan memotong ortofoto menjadi petak 200×200 piksel, mendeteksi apel dengan YOLO11 (n sampai x), dan menggabungkan hasilnya secara geospasial. Pada kumpulan data 2.000 citra hasil augmentasi dari 11 citra asli (51.797 objek), YOLO11x mencapai mAP50 0,816 dan mAP50-95 0,547. Koefisien koreksi untuk buah tersembunyi diusulkan sebagai pekerjaan lanjutan dan tidak divalidasi.

Catatan verifikasi data: Angka metrik YOLO11x (mAP50 0,81602, mAP50-95 0,54721, *precision* 0,85193, *recall* 0,76625) tertulis di teks Bagian 3 dan di abstrak; nilai pembulatan semua varian ada pada Tabel 1. Jumlah citra dan objek (11, 2.000, 51.797, 34.383, 17.414) ada pada Bagian 2 dan abstrak. Ekstraksi tabel terbaca sebagai daftar sel sehingga pemetaan kolom mengikuti urutan n, s, l, m, x pada tabel asli. Tidak dapat diverifikasi dari teks: lokasi, kultivar, jumlah pohon, pembagian data, hitungan manual, dan galat hitungan total. Rumus (4) terekstraksi sebagian rusak; isinya dibaca dari uraian di teks.
