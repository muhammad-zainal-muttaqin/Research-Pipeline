# An In-Field Dynamic Vision-Based Analysis for Vineyard Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ahmedtaristizabal2024field` |
| Judul asli | An In-Field Dynamic Vision-Based Analysis for Vineyard Yield Estimation |
| Penulis | Ahmedt-Aristizabal, David; Smith, Daniel; Khokher, Muhammad Rizwan; Li, Xun; Smith, Adam L.; Petersson, Lars; Rolland, Vivien; Edwards, Everard J. |
| Tahun | 2024 |
| Venue | IEEE Access |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [ahmedtaristizabal2024field.pdf](../pdf/ahmedtaristizabal2024field.pdf)
- DOI resmi: https://doi.org/10.1109/access.2024.3431244

## Gambaran Umum
Makalah ini mengusulkan sistem estimasi hasil panen anggur (*yield estimation*) dari video yang direkam di kebun anggur pada tahap prapanen. Sistem menggabungkan lima komponen: deteksi dan segmentasi tandan anggur dengan Mask R-CNN berbasis Swin Transformer, pelacakan tandan antarbingkai dengan *K-Shortest Path Siamese Network* (KSP-SiamFC) untuk menghitung jumlah tandan unik per panel, penghitungan buah beri (*berry*) per tandan dengan pendekatan peta kepadatan (*multitask point supervision*, MPS), regresi bobot tandan dari luas piksel dan jumlah beri, serta penjumlahan sampel acak dari distribusi bobot tandan untuk memperoleh hasil panen satu panel. Tanaman yang diteliti adalah anggur (kultivar Mataro) di kebun komersial Australia; data video direkam dengan kamera Blackmagic yang dipasang pada kendaraan Kubota RTV 500.

Data pelatihan berasal dari set data CSIRO Pre-harvest (300 citra beresolusi 6.144 × 3.456) dan set data publik Embrapa WGISD. Validasi sistem utuh memakai tiga panel kebun anggur yang direkam pada hari panen, dengan jumlah dan bobot tandan hasil panen sebagai acuan.

Hasil utama: mAP@50 deteksi kotak 77,3% dan segmentasi masker 77,1% pada subset uji; galat jumlah tandan rerata 11,3% pada kombinasi Swin-T Mask R-CNN dengan KSP-SiamFC; regresi Huber dengan rerata luas dan rerata jumlah beri menghasilkan MAE 22,1 gram dan R2 0,68. Galat bobot panen panel berkisar antara 1% dan 19,3%; pada dua dari tiga panel galat kurang dari 5%, sedangkan satu panel mencapai sekitar 15% atau lebih akibat kesalahan pelacakan pada tandan yang rapat.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil anggur dipakai untuk logistik panen, penyimpanan, pengolahan, dan penetapan harga. Buah anggur tidak dapat disimpan sebelum diolah menjadi anggur minuman dan mutunya menurun bila dibiarkan di pokok, sehingga prakiraan yang akurat penting bagi industri. Praktik yang berlaku umumnya berupa penilaian visual oleh pengelola kebun atau penghitungan tandan pada sebagian kecil kebun yang dikombinasikan dengan sedikit pengukuran bobot tandan. Praktik ini padat karya, mahal, dan menimbulkan galat; makalah menyebut galat praktik terkini mencapai 30%. Makalah juga mengutip perkiraan bahwa penurunan galat dari 33% menjadi 20% dapat menghemat sekitar AU$85 juta per tahun bagi industri.

Menurut penulis, sebagian besar metode pembelajaran mendalam di bidang viticultur dikembangkan untuk analisis pada satu titik waktu (citra statis). Solusi yang memanfaatkan informasi temporal pada bingkai berurutan masih sedikit. Pada video, tandan atau beri yang sama terdeteksi berkali-kali sehingga penghitungan langsung per bingkai menghasilkan hitungan ganda. Metode terdahulu mengatasinya dengan asumsi penyederhanaan, misalnya sebaran tandan yang seragam pada pokok, yang menurut penulis sering tidak terpenuhi karena tandan tersebar sangat heterogen.

## Ide Utama
Gagasan utama adalah mengestimasi hasil dengan cara berbeda dari praktik lazim (jumlah tandan dikali bobot rerata historis). Sistem mengestimasi bobot tandan secara langsung melalui kalibrasi empiris, yaitu regresi dari fitur visual tandan tersegmentasi ke bobot sebenarnya, lalu membangun distribusi bobot tandan untuk area yang direkam. Hasil panen area diperoleh dengan menjumlahkan sampel acak dari distribusi itu, dengan jumlah sampel sama dengan jumlah tandan unik hasil pelacakan.

Identitas tandan antarbingkai dijaga dengan pelacakan berbasis deteksi (*tracking-by-detection*). Jumlah lintasan (*track*) yang terbentuk dipakai sebagai jumlah tandan, dan beberapa pandangan atas tandan yang sama pada satu lintasan digabungkan untuk menghasilkan fitur yang lebih kuat bagi regresi bobot.

## Cara Kerja Langkah demi Langkah

```
 Video RGB -> Deteksi + segmentasi tandan (Swin-T Mask R-CNN)
                 |-> Pelacakan (KSP-SiamFC) -> jumlah tandan unik / panel
                 |-> Hitung beri per tandan (MPS, peta kepadatan)
 Fitur lintasan (rerata luas, rerata jumlah beri) -> regresi Huber -> bobot tandan
 Distribusi bobot (tandan "penuh") -> sampel acak sejumlah tandan -> hasil panel
```

### 1. Akuisisi data
Platform sensor dipasang pada Kubota RTV 500 dengan rangka aluminium. Kamera Blackmagic 50 fps dipasang pada kendaraan yang bergerak sekitar 4 km/jam; durasi video biasanya 10 sampai 15 menit. Set data CSIRO Pre-harvest direkam pada kebun kultivar Mataro selama musim 2021–2022 dalam berbagai kondisi cahaya (cerah dan berawan). Sebanyak 300 citra beresolusi 6.144 × 3.456 dipilih untuk pelatihan; topeng tandan dianotasi dengan poligon dan beri dianotasi dengan titik. Set data publik Embrapa WGISD (lima varietas: Chardonnay, Cabernet Franc, Cabernet Sauvignon, Sauvignon Blanc, Syrah) dipakai pula karena set data video publik langka. Bobot tandan Mataro dicatat saat panen. Pokok hanya direkam dari satu sisi.

### 2. Deteksi dan segmentasi tandan
Kerangka terdiri atas *backbone* Swin Transformer, *neck* berupa *feature pyramid network* (FPN), dan *head* Mask R-CNN yang menghasilkan kotak, label kelas, dan masker. Hanya ada satu kelas, yaitu tandan. Anotasi tandan lebih kecil dari 250 × 250 piksel (biasanya berisi 3 sampai 5 beri) dikeluarkan saat prapemrosesan, dengan alasan tandan kecil menjadi cukup besar pada bingkai lain karena sudut pandang berubah. Citra dibagi 80% pelatihan dan 20% pengujian, dilatih dari bobot awal COCO selama 50 epoch dengan *learning rate* 0,0001, ukuran *batch* 1, optimiser AdamW, augmentasi pembalikan horizontal, dan citra diubah menjadi 1.536 × 864. Ambang IoU 0,5 dan keyakinan kotak minimum 0,3 dipakai saat uji. Pelatihan memakai satu GPU 16 GB.

### 3. Pelacakan dan penghitungan tandan
Dua pelacak dari kelompok *separate detection and embedding* (SDE) dipakai. DeepSORT memakai filter Kalman untuk memprediksi posisi lintasan dan jaringan *embedding* untuk membandingkan penampakan. KSP-SiamFC menggunakan penampakan objek untuk menyambung potongan lintasan pendek (*tracklet*) menjadi lintasan panjang; algoritma *K-shortest path* berbasis pemrograman linear menghasilkan himpunan lintasan optimal pada satu rangkaian bingkai, dan jaringan Siamese (SiamFC) membandingkan penampakan kotak antarbingkai. Pelacak disesuaikan (*fine-tune*) dengan 1.000 pasangan kotak yang dipilih acak dari 38 lintasan tandan Mataro yang ditandai dan dianotasi manual pada beberapa bingkai. Jumlah lintasan dipakai sebagai jumlah tandan.

### 4. Penghitungan beri
Setelah tandan terdeteksi, kotak tandan dipotong dan diubah ukurannya menjadi 1.024 × 512. Penulis mengadopsi MPS (awalnya dikembangkan untuk penghitungan kerumunan) dengan modifikasi: memakai satu peta fitur gabungan untuk penghitungan dan lokalisasi, serta mempertahankan hanya fungsi rugi cabang gabungan, karena skala beri dalam citra relatif seragam. Jumlah beri diperoleh dengan menjumlahkan peta kepadatan; lokasi beri diperoleh dengan algoritma komponen terhubung. Fungsi rugi memakai *mean squared error*. Penulis mencatat bahwa oklusi mengganggu akurasi penghitungan dan bingkai tengah urutan tandan memberikan estimasi terbaik. Dua eksperimen dilakukan: hanya data CSIRO (110 kotak tandan, pembagian 3:1:1 untuk latih, validasi, uji, *batch* 512, Adam, *learning rate* awal 0,0001, konvergen dalam 20 epoch) dan gabungan CSIRO dengan Embrapa (4.404 citra kotak tandan).

### 5. Regresi bobot tandan
Variabel bebas adalah luas piksel masker dan jumlah beri. Fitur lintasan diestimasi dengan rerata, median, maksimum, atau maksimum gabungan (*max-jnt*, yaitu jumlah dua fitur yang diskalakan ke 0–1). Empat model dibandingkan: regresi linear, Huber, *Random Forest*, dan *Support Vector Regression* (SVR), dengan validasi silang tiga lipatan pada 38 lintasan Mataro yang bobot panennya dicatat. Metrik adalah R2 dan *mean absolute error* (MAE).

### 6. Estimasi hasil panel
Tandan yang tersegmentasi dibagi menjadi tandan "penuh" dan "parsial" berdasarkan ambang luas (diuji pada kisaran 2,5 × 10^5 sampai 3,5 × 10^5 piksel). Hanya tandan penuh yang dipakai untuk menyesuaikan distribusi beta bagi bobot tandan, agar tidak bias ke tandan kecil yang terokluasi. Jumlah sampel acak sama dengan jumlah tandan, dan proses diulang 300 kali untuk mendapatkan rerata. Karena pokok hanya direkam dari satu sisi, hitungan tandan visual dan hitungan SiamFC dilipatgandakan dengan asumsi jumlah tandan di sisi seberang sama.

## Eksperimen dan Hasil
Tiga panel kebun anggur Mataro dipakai untuk validasi hitungan tandan dan hasil panen. Jumlah tandan acuan dihitung manual dari video oleh dua pengamat independen, dan hasilnya dirata-ratakan. Bobot dan jumlah tandan panen dicatat pada hari panen.

| Tahap | Konfigurasi | Hasil |
|---|---|---|
| Deteksi tandan | Swin-T Mask R-CNN, subset uji | mAP@50 kotak 77,3%; mAP@50 masker 77,1% |
| Hitungan tandan, galat rerata tiga panel | Swin-T Mask R-CNN + KSP-SiamFC | 11,3% |
| Hitungan tandan | YOLOv4 + KSP-SiamFC | 23,6% |
| Hitungan tandan | YOLOv4 + DeepSORT | 28,3% (hitungan panel 2 tepat) |
| Regresi bobot, rerata seluruh konfigurasi | Huber | MAE 27,0 g; R2 0,44 |
| Regresi bobot terbaik | Huber, rerata luas + rerata jumlah beri | MAE 22,1 g; R2 0,68 |

Linear mengungguli nonlinear dengan perbaikan MAE rerata 16,9% dan R2 72,9% (angka dari teks makalah). Model Huber lebih baik 4,2% (MAE) dan 12,8% (R2) daripada regresi linear standar. Model fitur gabungan memperbaiki MAE 6,6% dan R2 28,6% dibanding model luas saja, serta MAE 18,3% dan R2 171,4% dibanding model jumlah beri saja. Rerata unggul atas median dengan perbaikan MAE 3,4% dan R2 4,8%. Hasil penghitungan beri dirangkum pada Tabel 5 makalah (MAE dan presisi lokalisasi); penulis menyatakan bahwa akurasi penghitungan meningkat dengan data lebih banyak (gabungan CSIRO dan Embrapa), sedangkan akurasi lokalisasi menurun karena variasi citra, dan model eksperimen 2 dipilih untuk aplikasi.

Galat hasil panen (bobot) per panel, menurut teks makalah:

| Panel | Basis hitungan tandan | Galat |
|---|---|---|
| 1 | Hitungan sebenarnya (*actual count*) | minimum 10,4%; rerata 18,9% (selalu *underestimate*) |
| 1 | Hitungan visual | minimum 3,1% |
| 1 | Hitungan SiamFC | minimum 19,1% |
| 2 | Hitungan sebenarnya | minimum 2,7%; rerata 8,3% |
| 2 | Hitungan visual | minimum 12,3% (selalu *underestimate*) |
| 2 | Hitungan SiamFC | minimum 3,0% |
| 3 | Hitungan sebenarnya | minimum 2,5%; rerata 6,0% |
| 3 | Hitungan visual / SiamFC | minimum 1,0% / 1,3% |

Penulis menyatakan galat panel pada sistem utuh berkisar antara 1% dan 19,3%, dan membandingkannya dengan hasil terdahulu yang disitir makalah: 5,9%–14,8% (penginderaan jauh NDVI, dilaporkan pada data latih), 6,48%–11,47% (pendeteksian beri tanpa pengawasan dengan sistem pencitraan khusus malam hari), dan 15%–27,1% (model *end-to-end*). Penulis menekankan bahwa perbandingan langsung tidak mungkin karena kondisi evaluasi berbeda. Penulis juga menyimpulkan bahwa pelacakan tandan merupakan sumber galat utama: hasil panen dengan hitungan tandan sebenarnya lebih konsisten daripada hasil dengan hitungan hasil pelacakan. Kecilnya galat pada hitungan visual panel 1 dijelaskan penulis sebagai akibat hitungan visual yang sangat *underestimate* terhadap hitungan sebenarnya, bukan akurasi yang sesungguhnya.

## Kelebihan dan Keterbatasan
Kelebihan: sistem utuh dari video tanpa penyesuaian manual atau pengumpulan data tambahan; perangkat akuisisi murah berbasis kamera konsumen; tidak memerlukan latar belakang buatan atau pencahayaan khusus; pemakaian banyak pandangan tandan sepanjang lintasan untuk memperhalus fitur; dan evaluasi pada hasil panen nyata di tiga panel. Penulis juga menyediakan tinjauan ringkas literatur 2020 sampai awal 2024.

Keterbatasan yang dinyatakan penulis: tandan yang padat, oklusi, dan penampakan tandan yang serupa membuat pelacakan salah menetapkan kotak ke lintasan tandan di dekatnya, sehingga hitungan tandan keliru; distribusi bobot hasil visi komputer pada panel 1 bias ke tandan ringan; geometri tandan bergantung pada jarak pengambilan citra; dan pokok hanya direkam dari satu sisi sehingga jumlah tandan dikalikan dua dengan asumsi sebaran seragam. Penulis mengusulkan pelacakan multi-objek 3D berbantuan *depth* dan penghitungan serta pengukuran beri individual sebagai arah lanjutan.

Menurut pembacaan ringkasan ini, regresi bobot hanya dilatih dan diuji pada 38 lintasan Mataro dengan validasi silang tiga lipatan, dan evaluasi hasil panen hanya pada tiga panel dari satu kebun dan satu kultivar, sehingga generalisasi tidak dapat dinilai. Menurut pembacaan ringkasan ini, ambang tandan "penuh" dipilih dari kisaran dan galat minimum dilaporkan pada beberapa hasil, sehingga galat minimum tidak setara dengan galat pada pengaturan yang ditetapkan sebelumnya. Menurut pembacaan ringkasan ini, galat panel yang rendah pada satu sumber hitungan dapat disebabkan oleh galat hitungan dan galat bobot yang saling meniadakan, seperti yang diakui penulis untuk panel 1.

## Kaitan dengan Tinjauan main6
Makalah ini menangani tandan yang terlihat berkali-kali pada bingkai video berurutan. Mekanismenya adalah pelacakan berbasis deteksi: deteksi tandan dihubungkan antarbingkai oleh KSP-SiamFC (atau DeepSORT sebagai pembanding), dan jumlah lintasan dipakai sebagai jumlah tandan unik per panel. Perbandingan tiga kombinasi detektor-pelacak menunjukkan bahwa pelacakan merupakan sumber galat utama pada tandan yang rapat. Makalah juga meninjau secara singkat pendekatan berbasis SfM (COLMAP) untuk memberi identitas unik melalui posisi 3D, tetapi tidak memakainya; pendekatan stereo, kamera *depth*, dan SLAM dinyatakan di luar cakupan tinjauan, dan pelacakan 3D diusulkan sebagai pekerjaan lanjutan. Hitungan tidak dilaporkan per kelas, karena hanya ada satu kelas (tandan). Hitungan antarsisi pokok tidak dilakukan: hanya satu sisi pokok yang direkam dan hitungan digandakan dengan asumsi simetri, tanpa mekanisme pencocokan identitas antar sisi.

Acuan hitung adalah hitungan manual dari video oleh dua pengamat (dirata-ratakan) serta jumlah dan bobot tandan hasil panen pada tiap panel. Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah rancangan evaluasi yang membandingkan hitungan otomatis dengan hitungan visual dan hitungan panen sebenarnya, serta temuan bahwa galat pelacakan pada objek rapat dan serupa mendominasi galat total. Penggandaan hitungan satu sisi dengan asumsi sebaran seragam adalah praktik yang penulis sendiri nilai lemah, sehingga tidak layak dijadikan acuan untuk inventaris per kelas dari beberapa sisi.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `ahmedtaristizabal2024field`.

Ahmedt-Aristizabal dkk. mengusulkan sistem estimasi hasil panen anggur dari video yang menggabungkan segmentasi tandan dengan Swin Transformer Mask R-CNN, pelacakan tandan KSP-SiamFC untuk memperoleh jumlah tandan unik, penghitungan beri dengan peta kepadatan, dan regresi bobot tandan Huber. Pada tiga panel kebun anggur Mataro, galat jumlah tandan rerata 11,3% untuk kombinasi terbaik, dan galat bobot panen panel berkisar antara 1% dan 19,3%; galat di bawah 5% tercapai pada dua dari tiga panel. Penulis menyatakan pelacakan tandan pada tandan yang rapat sebagai sumber galat utama.

Catatan verifikasi data: angka mAP (77,3% dan 77,1%) tertulis di Bagian V-A2; galat hitungan tandan 11,3%, 23,6%, dan 28,3% di Bagian V-B2; MAE 27,0 g, R2 0,44, MAE 22,1 g, dan R2 0,68 di Bagian V-D2 dan keterangan Tabel 7; galat panel di Bagian V-E2. Isi Tabel 4 (hitungan tandan per panel), Tabel 5 (hasil penghitungan beri), Tabel 6, dan Tabel 7, serta grafik Gambar 13, tidak terbaca pada teks ekstraksi, sehingga jumlah tandan pengamatan per panel dan nilai MAE penghitungan beri tidak dapat dilaporkan di sini. Nilai "galat maksimum 19,3%" berasal dari kalimat perbandingan dengan karya terdahulu dan tidak dapat dicocokkan dengan satu sel tertentu. Persentase perbaikan (misalnya 16,9% dan 72,9%) dikutip dari teks, tidak dihitung ulang.
