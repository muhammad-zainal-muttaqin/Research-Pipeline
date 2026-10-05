## Gambaran Umum
Makalah prosiding (IEEE WF-IoT 2021) ini membangun alur dua tahap untuk mencacah buah pada video: detektor YOLOv3 (varian dengan *spatial pyramid pooling*, YOLOv3-SPP) menghasilkan kotak pembatas, lalu pelacak DeepSORT yang dimodifikasi mengaitkan deteksi antarbingkai sehingga setiap apel dihitung satu kali. Penyesuaian utama adalah mengganti pengekstraksi fitur penampilan DeepSORT, yang semula dilatih untuk identifikasi ulang pejalan kaki, dengan ResNet18 berbobot pralatih ImageNet, serta memakai kecocokan penampilan dan kecocokan IoU.

Data uji berupa video barisan pohon apel dari kebun apel pada cahaya matahari. Pada satu klip video dengan 342 apel sebagai acuan hitung manual, bobot YOLO pralatih (COCO) menghasilkan 523 apel terhitung (akurasi 47,06%), bobot pralatih dengan mekanisme koreksi ukuran menghasilkan 299 (87,43%), dan bobot yang disetel halus dengan 150 citra apel menghasilkan 313 (91,5%).

Penulis menyatakan bahwa pendekatan ini dapat dipakai pada jenis buah dan sayur lain tanpa mengubah algoritme pelacakan. Pernyataan itu belum diuji pada buah lain dalam makalah ini.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Pencacahan buah (estimasi hasil panen) membantu petani mengalokasikan sumber daya panen, menyiapkan penyimpanan, dan merencanakan rute panen, sedangkan hitung manual di lapangan melelahkan. Penulis mencatat bahwa metode pengolahan citra klasik berbasis warna atau tekstur bergantung pada jenis buah serta rentan terhadap perubahan iluminasi dan penutupan, dan bahwa banyak pustaka pembelajaran mendalam sebelumnya bekerja pada citra diam, bukan video.

Pada video, deteksi saja tidak dapat dipakai untuk mencacah karena tidak ada cara mengetahui apakah apel yang terdeteksi pada bingkai pertama sama dengan apel pada bingkai berikutnya, sehingga apel yang sama akan dihitung berkali-kali. Video juga memberi beberapa sudut pandang sehingga buah yang tertutup atau teduh pada satu bingkai dapat terlihat jelas pada bingkai lain. Masalah tambahan yang ditemukan adalah apel dari barisan pohon di belakang ikut terdeteksi dan terhitung padahal pencacahan dilakukan satu baris per penerbangan.

## Ide Utama
Penghitungan dilakukan pada objek hasil pelacakan, bukan pada deteksi per bingkai. Setiap lintasan yang telah terkonfirmasi dihitung satu kali. Penampilan buah direpresentasikan oleh vektor fitur dari ResNet18 (keluaran lapisan *average pooling* berdimensi 512), sehingga pelacak umum untuk berbagai buah karena ResNet18 berbobot ImageNet tidak perlu dilatih ulang. Kecocokan IoU berfungsi sebagai cadangan ketika kecocokan penampilan gagal sesaat.

Untuk apel pada barisan belakang, kotak yang lebar dan tingginya kurang dari 30 piksel dibuang. Setelah detektor disetel halus tanpa menganotasi apel jauh, mekanisme koreksi ini tidak diperlukan lagi.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Video diambil dari kebun apel pada cahaya matahari, dengan peronda (dalam teks disebut *drone*) yang terbang di antara barisan pohon dan menyediakan umpan video. Satu baris pohon dicacah pada satu waktu. Kultivar, lokasi, resolusi, jumlah bingkai, dan panjang video tidak dilaporkan. Untuk penyetelan halus dipakai 150 citra apel: setengah citra jarak dekat buah dan setengah citra pohon apel. Anotasi manual mencakup lima kasus (Tabel III makalah): apel tertutup sebagian oleh daun, setengah tertutup, sangat tertutup (hanya bagian terlihat yang dianotasi), apel yang saling tumpang tindih, dan apel pada pencahayaan berbeda. Apel yang jauh sengaja tidak dianotasi.

### 2. Deteksi dengan YOLOv3-SPP
YOLOv3-SPP dipilih berdasarkan perbandingan pada Tabel I makalah (bukan hasil eksperimen penulis pada data apel kecuali nilai bertanda khusus) karena memberi kompromi akurasi dan kecepatan; penulis tidak memakai TensorRT karena dianggap masih eksperimental dan menuntut perangkat keras tertentu. YOLOv3 memakai tulang punggung Darknet-53 dengan koneksi residu dan prediksi pada tiga skala. *Non-max suppression* memakai ambang IoU 0,6, yang sengaja longgar karena apel sering saling tumpang tindih. Bobot awal adalah COCO; pada konfigurasi akhir, model dikonfigurasi hanya untuk kelas apel dan dilatih 5.000 epoch dengan konfigurasi pelatihan bawaan.

### 3. Koreksi deteksi apel latar
Bobot pralatih mendeteksi apel dari baris pohon lain. Ambang tinggi keyakinan tidak membantu karena apel tertutup atau kabur akibat gerak kamera juga berkeyakinan rendah. Penulis menganalisis ukuran rata-rata apel jauh dari keluaran detektor dan menetapkan ambang 30 piksel untuk lebar dan tinggi kotak; kotak lebih kecil dari itu dibuang.

### 4. Pelacakan DeepSORT dimodifikasi
Keadaan Kalman berdimensi 8 $(x, y, a, h, \dot{x}, \dot{y}, \dot{a}, \dot{h})$ dengan model kecepatan konstan. Hanya jarak penampilan yang dipakai (tanpa jarak gerak), dengan kemiripan kosinus pada fitur ResNet18 dan biaya $C(i,j) = 1 - D(j)^T T(i)$. Pencocokan memakai algoritme Hungarian. Jarak maksimum yang diterima 0,15. Lintasan baru berstatus *tentative* dan menjadi *confirmed* setelah lebih dari 2 pencocokan (*hits*). Umur maksimum lintasan tanpa pencocokan adalah 30 bingkai (sekitar 1 detik pada 30 bingkai per detik). Sebelum deteksi tak terkait dijadikan lintasan baru, dilakukan pencocokan IoU dengan ambang 0,3. Keyakinan minimum deteksi adalah 0,3; nilai di bawahnya mulai memasukkan daun yang salah dikenali sebagai apel. Seluruh ambang dipilih dari implementasi DeepSORT bawaan dan percobaan informal.

### 5. Pencacahan
ID lintasan tidak langsung dipakai sebagai hitungan karena sebagian lintasan tentatif dihapus. Apel dihitung ketika lintasannya menjadi terkonfirmasi.

## Eksperimen dan Hasil
Evaluasi dilakukan pada satu klip video apel dengan acuan hitung manual oleh manusia (342 apel). Akurasi dihitung sebagai $(GT - L)/GT \times 100$ dengan $L$ galat absolut $L_1$ antara hitungan prediksi dan hitungan acuan.

| Konfigurasi | Prediksi / acuan | Galat L1 | Akurasi |
|---|---|---|---|
| Bobot pralatih (COCO) | 523 / 342 | 181 | 47,06% |
| Bobot pralatih + koreksi ukuran | 299 / 342 | 43 | 87,43% |
| Bobot disetel halus | 313 / 342 | 29 | 91,5% |

Bobot pralatih menghitung berlebih karena mendeteksi apel dari barisan belakang. Koreksi ukuran mengubah hasil menjadi penghitungan kurang (299 dari 342), karena apel jauh tidak lagi terdeteksi, tetapi detektor masih kesulitan dengan apel tertutup. Setelah penyetelan halus, lebih banyak apel tertutup terdeteksi dengan benar dan pelacak mempertahankan identitasnya, sedangkan apel yang hampir seluruhnya tertutup tetap tidak terdeteksi pada semua bingkai. Gambar 5 sampai 7 menunjukkan kasus ID 589 yang tidak terdeteksi pada satu bingkai lalu diidentifikasi ulang ketika terdeteksi kembali, serta apel ID 598 yang terdeteksi setelah sudut pandang berubah.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: alur sepenuhnya berbasis pembelajaran mendalam, pelacak tidak perlu dilatih ulang untuk buah lain karena memakai ResNet18 ImageNet, dan penyetelan halus dengan data kecil (150 citra) sudah memperbaiki hitungan. Penulis menyebut hasil tinggi pada umpan video waktu nyata, tetapi kecepatan (bingkai per detik) tidak dilaporkan.

Keterbatasan yang dinyatakan penulis: apel yang hampir seluruhnya tertutup tidak terdeteksi walaupun sudut pandang atau cahaya berubah, dan tantangan utama ada pada tahap deteksi. Rencana ke depan mencakup uji pada buah lain (jeruk) dan detektor lain.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan lain. Evaluasi hanya memakai satu klip video dari satu baris pohon, sehingga hasil 91,5% tidak memberi gambaran sebaran galat. Detektor disetel halus pada citra dari kebun yang sama dan kemungkinan satu sumber video; pemisahan data latih dan uji tidak diuraikan, jadi kebocoran data tidak dapat dikesampingkan. Klaim bahwa pendekatan berlaku untuk buah lain tidak diuji. Ambang ditetapkan lewat percobaan informal pada video yang sama. Tidak ada penanganan buah yang sama pada pelintasan berbeda atau sisi pohon berbeda, dan tidak ada hitungan per kelas.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dengan pelacakan berbasis deteksi dalam satu video: fitur penampilan ResNet18 dengan kemiripan kosinus, Kalman, Hungarian, kecocokan IoU cadangan, dan konfirmasi lintasan setelah beberapa pencocokan. Hitungan dilaporkan sebagai total apel, bukan per kelas. Acuan hitungnya adalah hitung manual oleh manusia pada klip video (bukan panen); apakah acuan dihitung dari video atau di lapangan tidak dirinci.

Untuk pencacahan tandan sawit multi-sisi, gagasan memakai fitur penampilan umum dari jaringan pralatih sebagai pencocok identitas dapat dipindahkan, demikian pula aturan konfirmasi lintasan sebelum dihitung. Namun, pelacakan ini mengandalkan kontinuitas antarbingkai, dan pencocokan penampilan antar-sisi pohon pada sudut pandang berbeda belum diuji. Pada pencacahan sawit multi-sisi, kendala tambahan adalah tandan bersebelahan yang tampak serupa pada kelas yang sama.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `osman2021yieldb`.

Osman dkk. (2021) menyajikan alur pencacahan buah pada video yang terdiri atas YOLOv3-SPP dan DeepSORT yang dimodifikasi dengan ResNet18 berbobot ImageNet sebagai pengekstraksi fitur penampilan, serta pencocokan IoU cadangan. Pada satu klip video apel dengan 342 apel acuan, detektor yang disetel halus dengan 150 citra menghitung 313 apel (akurasi 91,5%), sedangkan bobot pralatih tanpa koreksi menghitung 523 apel (47,06%).

Catatan verifikasi data: Angka hasil ada pada Tabel II dan Seksi IV-C; ambang (0,15; 0,3; 0,3 keyakinan; umur maksimum 30; ambang ukuran 30 piksel; NMS 0,6; 5.000 epoch; 150 citra) ada pada Seksi III dan IV. Angka pada Tabel I (AP dan FPS beberapa detektor) berasal dari makalah lain, kecuali nilai bertanda asterisk yang diperoleh dari pengujian penulis. Akurasi 47,06% dikutip sebagaimana tertulis; hitungan dari $(342 - 181)/342$ memberi sekitar 47,08%, selisih kecil yang tidak dibahas penulis. Resolusi video, panjang klip, kecepatan pemrosesan, kultivar, lokasi, dan pemisahan data latih dan uji tidak dilaporkan.
