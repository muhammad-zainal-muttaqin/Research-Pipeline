# 039 - Learning Selective Self-Mutual Attention for RGB-D Saliency Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2020s2ma` |
| Judul asli | Learning Selective Self-Mutual Attention for RGB-D Saliency Detection |
| Penulis | Nian Liu, Ni Zhang, Junwei Han |
| Tahun | 2020 |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2020), hlm. 13756–13765 |
| Tema | RGB-D SOD |

## Tautan Akses
- **CVF Open Access (PDF gratis):** https://openaccess.thecvf.com/content_CVPR_2020/html/Liu_Learning_Selective_Self-Mutual_Attention_for_RGB-D_Saliency_Detection_CVPR_2020_paper.html
- **Kode sumber (GitHub):** https://github.com/nnizhang/S2MA
- **Google Scholar:** https://scholar.google.com/scholar?q=Learning%20Selective%20Self-Mutual%20Attention%20for%20RGB-D%20Saliency%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Learning%20Selective%20Self-Mutual%20Attention%20for%20RGB-D%20Saliency%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan S2MA (*Selective Self-Mutual Attention*), model deteksi objek menonjol (*salient object detection*, SOD) pada data RGB-D. SOD memisahkan objek yang paling menarik perhatian dari latar belakangnya ke dalam peta saliency per piksel. Data RGB-D terdiri atas citra RGB dan peta kedalaman (*depth map*), citra yang setiap pikselnya menyimpan jarak ke kamera. Kedalaman memberi petunjuk geometri, tetapi sering berderau, sehingga fusi kedua modalitas memerlukan mekanisme yang memilah informasi yang dapat dipercaya.

Gagasan utamanya adalah memfusikan atensi, bukan fitur. Setiap aliran menghitung peta atensi *non-local* (kemiripan setiap posisi terhadap semua posisi lain), lalu atensi milik modalitas lain ditambahkan dengan bobot seleksi per piksel yang memperkirakan keandalannya. Modul ini dipasang pada jaringan dua aliran berbasis VGG-16. Pada tujuh tolok ukur RGB-D SOD, model ini mengungguli 11 pembanding pada lima dataset; pada RGBD135, S-measure mencapai 0,941 dibandingkan 0,900 dari pesaing terdekat, DMRA.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Model SOD pada masanya umumnya bekerja pada citra RGB semata. Pada adegan berlatar kompleks atau objek yang mirip latar, petunjuk penampakan tidak mencukupi; kedalaman menjadi pelengkap karena objek menonjol umumnya berjarak berbeda dari latar. Masalahnya adalah cara menggabungkan kedua modalitas.

Sebelum makalah ini ada tiga skema fusi. Fusi awal (*early fusion*) menggabung RGB dan kedalaman di tingkat masukan, tetapi terbebani kesenjangan distribusi antara data warna dan data jarak. Fusi hasil (*result fusion*) menggabungkan dua peta saliency dari dua model terpisah, tetapi informasi sudah terkompresi sebelum interaksi terjadi. Fusi fitur (*feature fusion*) menjumlahkan atau menyambungkan fitur tingkat menengah dari dua aliran CNN, seperti pada CTMF, PCF, TANet, dan DMRA (bab [035 - 2019 - DMRA - RGB-D SOD](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)); skema ini hanya membentuk interaksi linear. Modul *Non-local* (Wang dkk., 2018) membuka jalan lain: setiap posisi dapat memperhatikan seluruh posisi lain. Namun memindahkan atensi lintas modalitas tanpa penyaring berisiko menyebarkan kesalahan dari peta kedalaman yang buruk; celah inilah yang diisi makalah ini.

## Ide Utama

Atensi kedalaman menyatakan posisi-posisi yang saling berkaitan menurut geometri; atensi RGB menyatakan keterkaitan menurut penampakan. S2MA memfusikan keduanya: matriks afinitas (tabel kemiripan antarposisi) dari modalitas sendiri dijumlahkan dengan matriks afinitas modalitas lain, dan hasilnya dipakai kedua aliran untuk mengumpulkan konteks global. Atensi sendiri disebut *self-attention*; atensi pinjaman dari modalitas lain disebut *mutual attention*.

Karena atensi pinjaman tidak selalu benar, S2MA menambahkan atensi seleksi: dua peta bobot per piksel, dihitung dari gabungan kedua fitur, yang menentukan seberapa besar atensi pinjaman berperan di setiap posisi. Atensi diri selalu dipakai penuh; atensi silang hanya masuk pada posisi yang dinilai andal, sehingga kedalaman yang buruk tidak ikut merusak fitur RGB.

## Cara Kerja Langkah demi Langkah

### Modul Non-local sebagai Titik Tolak

Modul *Non-local* menerima peta fitur X berukuran H×W×C (tinggi, lebar, jumlah kanal). Tiga konvolusi 1×1 memproyeksikan X ke tiga ruang embedding: θ(X), φ(X), dan g(X). Matriks afinitas f(X) = θ(X)ᵀ φ(X) berukuran HW×HW; elemen f_ij menyatakan kemiripan posisi i dan posisi j. Fungsi *softmax* (normalisasi eksponensial agar tiap baris berjumlah satu) mengubah afinitas menjadi bobot atensi A. Fitur baru tiap posisi adalah jumlah berbobot fitur seluruh posisi: Y = A · g(X); keluaran Z = W_Z · Y + X menambahkannya ke fitur semula melalui koneksi residual. Sebagai gambaran skala, pada peta fitur 32×32 matriks afinitas berukuran 1024×1024.

### Atensi Diri-Silang (SMA)

Untuk dua modalitas terdapat dua peta fitur, Xr (RGB) dan Xd (kedalaman), dengan afinitasnya masing-masing, f_r dan f_d. Modul SMA menjumlahkan keduanya lalu menormalkan: A_f = softmax(f_r + f_d). Atensi gabungan ini dipakai kedua aliran untuk mengagregasi konteks: Y_r = A_f · g_r(Xr) dan Y_d = A_f · g_d(Xd). Karena A_f memuat bukti kemiripan dari dua modalitas, penentuan posisi yang saling berkaitan menjadi lebih akurat daripada atensi satu modalitas.

### Atensi Seleksi: dari SMA menjadi S2MA

SMA memperlakukan atensi pinjaman seolah selalu dapat dipercaya, padahal sebagian peta kedalaman berderau. S2MA menghitung atensi seleksi: Xr dan Xd disambungkan sepanjang kanal, dilewatkan ke konvolusi 1×1, lalu dinormalkan dengan softmax menjadi Ω berukuran H×W×2, yang dipecah menjadi dua peta H×W×1: ω_r dan ω_d (keandalan atensi RGB dan kedalaman, berjumlah satu per piksel). Atensi selektif adalah A_r = softmax(f_r + ω_d ⊙ f_d) untuk aliran RGB dan A_d = softmax(f_d + ω_r ⊙ f_r) untuk aliran kedalaman; ⊙ adalah perkalian per elemen (produk Hadamard). Bobot hanya dikenakan pada suku pinjaman; menimbang suku atensi diri dilaporkan justru menurunkan hasil. Struktur modul diringkas pada diagram berikut.

```
Xr (fitur RGB)                              Xd (fitur depth)
    |                                          |
    | afinitas diri:  fr = th_r(Xr)' ph_r(Xr)  |  fd = th_d(Xd)' ph_d(Xd)
    |                                          |
    +--> [Xr; Xd] -> konvolusi 1x1 -> softmax -> omega_r, omega_d
    |                       (peta keandalan per piksel tiap modalitas)
    v                                          v
Ar = softmax(fr + omega_d * fd)    Ad = softmax(fd + omega_r * fr)
    |                                          |
    v                                          v
Yr = Ar . g_r(Xr)                  Yd = Ad . g_d(Xd)
    |                                          |
    +-> Zr = Wz Yr + Xr            +-> Zd = Wz Yd + Xd
```

Hanya peta afinitas yang bertukar antaraliran; fitur g(X) tetap dari modalitas masing-masing, sehingga setiap aliran hanya meminjam pola perhatian modalitas lain.

### Jaringan Dua Aliran dan DenseASPP

Modul S2MA disisipkan ke CNN dua aliran yang identik, satu untuk RGB dan satu untuk kedalaman. Setiap aliran memakai pola UNet, yaitu arsitektur enkoder–dekoder dengan koneksi *skip* (loncatan) yang menyalurkan fitur enkoder ke dekoder pada resolusi yang sama. Enkodernya adalah VGG-16 (CNN 16 lapis klasik) yang dimodifikasi: *stride* *pooling* dua lapis terakhir menjadi 1, konvolusi blok kelima berdilatasi 2, dan dua lapis akhir diganti konvolusi berdilatasi 12 dengan 1024 kanal. Konvolusi berdilatasi menautkan piksel berjarak tertentu sehingga jangkauan penglihatan membesar tanpa menurunkan resolusi; hasilnya enkoder konvolusional penuh dengan *output stride* 8 (peta fitur akhir 1/8 ukuran masukan).

Di atas enkoder dipasang DenseASPP: beberapa konvolusi berdilatasi paralel untuk konteks multi-skala, di sini tiga cabang berdilatasi 2, 4, dan 8 (masing-masing 176 kanal) ditambah satu cabang *average pooling* global. S2MA ditempatkan setelah DenseASPP pada resolusi terkecil; pada peta yang lebih besar modul ini terlalu mahal karena afinitas tumbuh kuadratik terhadap jumlah posisi. Alurnya: kedua masukan melewati VGG-16 dan DenseASPP menjadi Xr dan Xd, dipetakan S2MA ke Zr dan Zd, lalu diteruskan ke dekoder masing-masing aliran; peta saliency akhir diambil dari dekoder RGB.

### Dekoder dan Modul Fusi Residual

Dekoder kedalaman memakai modul F: fitur *skip* dan fitur dekoder sebelumnya disambungkan lalu dilewatkan ke dua konvolusi 3×3. Dekoder RGB memakai modul R (*residual fusion*): setelah konvolusi pertama, fitur hasil konvolusi pertama milik modul kedalaman yang sejajar turut disambungkan, lalu konvolusi kedua mempelajari sinyal fusi residual — petunjuk kedalaman masuk sebagai koreksi tambahan di setiap tingkat resolusi. Setiap aliran diakhiri konvolusi berkanal satu dan fungsi sigmoid (pemetaan ke rentang 0–1); saat pengujian hanya keluaran aliran RGB yang dipakai.

### Pelatihan

Himpunan latih berisi 2.050 pasang citra (1.400 dari NJUD dan 650 dari NLPR), mengikuti protokol karya sebelumnya. Citra diubah ke 288×288 piksel, dipotong acak menjadi 256×256, dan dibalik horizontal secara acak. Peta kedalaman disalin menjadi tiga kanal, diseragamkan (nilai kecil berarti dekat ke kamera), dan dinormalisasi ke 0–255. Fungsi loss adalah *cross-entropy* per piksel terhadap mask kebenaran pada kedua aliran, ditambah pengawasan dalam (*deep supervision*): tiap modul dekoder menghasilkan peta saliency sementara yang ikut dihitung loss-nya dengan bobot 0,5 dan 0,8. Optimisasi memakai SGD momentum 0,9, *batch* 8, 40.000 iterasi, laju pembelajaran awal 0,01, pada satu GPU GTX 1080 Ti.

## Eksperimen dan Hasil

Evaluasi memakai tujuh tolok ukur: NJUD (1.985 citra), NLPR (1.000 citra Kinect), RGBD135 (135 citra Kinect), LFSD (100 citra kamera medan cahaya Lytro), STERE (1.000 citra binokular), SSD (80 bingkai stereo), dan DUT-RGBD (1.200 citra Lytro2). Metriknya: S-measure (kemiripan struktural dengan peta kebenaran), F-measure maksimum (rerata harmonik presisi–recall pada ambang terbaik), E-measure (kesejajaran global dan lokal), serta MAE (rerata selisih absolut per piksel, makin rendah makin baik).

Dibandingkan 11 metode terdahulu dengan DMRA sebagai pesaing terkuat, S2MA memperoleh S-measure terbaik pada lima dataset: NJUD 0,894 lawan 0,886; NLPR 0,915 lawan 0,899; RGBD135 0,941 lawan 0,900 (selisih 4,1 poin persentase, margin terbesar); SSD 0,868 lawan 0,857; dan DUT-RGBD 0,903 lawan 0,889. Pada dua dataset lain S2MA di posisi kedua: LFSD 0,837 lawan 0,847, dan STERE 0,890 lawan 0,886 pada S-measure tetapi tertinggal tipis pada tiga metrik lain. Keunggulan S2MA paling konsisten pada kedalaman hasil sensor; pada kedalaman estimasi manfaatnya menyusut.

Studi ablasi pada NJUD memerinci sumbangan komponen (S-measure / MAE): UNet dasar hanya-RGB 0,865 / 0,072; ditambah DenseASPP 0,877 / 0,057; ditambah modul Non-local biasa tetap 0,877 / 0,057 — atensi satu modalitas tidak menambah apa pun; diganti SMA 0,890 / 0,058; ditambah atensi seleksi MAE turun ke 0,056; dan modul fusi residual menutup konfigurasi penuh pada 0,894 / 0,053. Pada RGBD135 urutan yang sama naik dari 0,875 ke 0,941. Keuntungan dengan demikian datang dari fusi atensi lintas modalitas, bukan dari modul atensi itu sendiri. Visualisasi bobot seleksi memperkuat hal ini: ω_d kecil pada piksel jauh yang kedalamannya kasar, besar pada piksel dekat, dan sekitar 0,5 di dalam objek menonjol. Kecepatan pengujian 0,107 detik per citra (sekitar 9,3 citra per detik).

## Kelebihan dan Keterbatasan

Kelebihan utama S2MA adalah fusi lintas modalitas non-linear tanpa mengubah representasi fitur: modul hanya menukar pola atensi sehingga dapat disisipkan ke arsitektur dua aliran mana pun. Mekanisme seleksi menangani keandalan modalitas secara eksplisit per piksel, dan kode beserta peta saliency dirilis terbuka.

Keterbatasannya, sebagaimana diakui penulis, afinitas berukuran kuadratik terhadap jumlah posisi sehingga S2MA hanya dipasang sekali pada resolusi terkecil. Dari sisi rekayasa, dua aliran VGG-16 menggandakan parameter dan kecepatan 9,3 citra per detik jauh dari kebutuhan waktu nyata. Secara konseptual, hasil pada LFSD dan STERE yang tidak melampaui DMRA mengindikasikan manfaat seleksi mengecil ketika kedalaman bukan hasil sensor; bobot seleksi dipelajari dari data latih, sehingga perilakunya terhadap jenis derau kedalaman yang tak dikenal tidak terjamin.

## Kaitan dengan Bab Lain

S2MA mewarisi dua garis pemikiran. Dari sisi fusi RGB-D, ia melanjutkan skema fusi fitur dua aliran yang dipakai DMRA (bab [035](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)) dan menggantikan gerbang atensi terpandu kedalaman DMRA dengan fusi atensi dua arah yang selektif. Sepantarannya adalah JL-DCF (bab [038](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md)) dan UC-Net (bab [041](./041%20-%202020%20-%20UC-Net%20-%20RGB-D%20SOD.md)). Gagasan bahwa kedalaman tidak selalu dapat dipercaya dikembangkan lebih jauh oleh D3Net (bab [037](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md)). Dari sisi mekanisme atensi, modul Non-local berbasis CNN kemudian digantikan backbone transformer: Visual Saliency Transformer (bab [042](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md)) dan SwinNet (bab [043](./043%20-%202022%20-%20SwinNet%20-%20RGB-D%20SOD.md)) menjadikan atensi global sebagai operasi bawaan jaringan.

## Poin untuk Sitasi

Kunci BibTeX: `liu2020s2ma`. Ringkasan yang aman dikutip: S2MA (Liu, Zhang, Han; CVPR 2020) melakukan fusi RGB-D untuk deteksi objek menonjol dengan memfusikan atensi *non-local* kedua modalitas, bukan fiturnya; suku atensi lintas modalitas ditimbang per piksel oleh atensi seleksi yang memperkirakan keandalan modalitas, sehingga kedalaman berderau tidak menyebarkan kesalahan. Model dua aliran berbasis VGG-16 ini melaporkan kinerja terbaik pada lima dari tujuh tolok ukur RGB-D SOD saat itu. Catatan verifikasi: seluruh angka pada bab ini diambil dari Tabel 1 dan Tabel 2 naskah CVPR 2020 versi *open access* (hlm. 13756–13765); makalah ini tidak memiliki versi arXiv; entri lama yang menyebut dataset SIP tidak sesuai dengan naskah asli.
