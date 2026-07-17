# 069 - 3D Packing for Self-Supervised Monocular Depth Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `guizilini2020packnet` |
| Judul asli | 3D Packing for Self-Supervised Monocular Depth Estimation |
| Penulis | Vitor Guizilini, Rares Ambrus, Sudeep Pillai, Allan Raventos, Adrien Gaidon (Toyota Research Institute) |
| Tahun | 2020 |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2020), hal. 2485–2494 |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1905.02693
- **CVPR Open Access (versi penerbit):** https://openaccess.thecvf.com/content_CVPR_2020/html/Guizilini_3D_Packing_for_Self-Supervised_Monocular_Depth_Estimation_CVPR_2020_paper.html
- **Repositori kode resmi (TRI-ML):** https://github.com/TRI-ML/packnet-sfm
- **Google Scholar:** https://scholar.google.com/scholar?q=3D%20Packing%20for%20Self-Supervised%20Monocular%20Depth%20Estimation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=3D%20Packing%20for%20Self-Supervised%20Monocular%20Depth%20Estimation&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan PackNet, jaringan untuk estimasi kedalaman monokular — memprediksi jarak setiap piksel dari satu citra RGB saja — yang dilatih secara swa-awas (*self-supervised*), yaitu hanya dari video monokular tanpa label kedalaman dan tanpa pra-pelatihan tersupervisi di ImageNet. Kontribusi utamanya ada dua. Pertama, arsitektur *encoder-decoder* baru yang mengganti *downsampling* (penurunan resolusi) dan *upsampling* (penaikan resolusi) standar dengan blok *packing* dan *unpacking* simetris berbasis konvolusi 3D, sehingga detail spasial yang biasanya hilang saat kompresi fitur dapat dipertahankan dan dipulihkan. Kedua, skema supervisi kecepatan lemah (*weak velocity supervision*): besaran translasi ego-gerak kendaraan yang diprediksi jaringan pose dicocokkan dengan pengukuran kecepatan kamera, sehingga peta kedalaman yang dihasilkan berskala metrik (satuan meter nyata), bukan sekadar skala relatif.

Hasil utamanya: meskipun hanya dilatih dari video mentah, PackNet mengungguli metode swa-awas, semi-supervisi, dan bahkan beberapa metode tersupervisi penuh pada tolok ukur KITTI; performanya membaik ketika resolusi masukan dan jumlah parameter dinaikkan tanpa *overfitting*; serta berjalan *real-time*. Makalah ini juga merilis DDAD (*Dense Depth for Automated Driving*), dataset berkendara baru dengan ground truth LiDAR berjangkauan hingga 250 m.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman dari satu citra adalah masalah *ill-posed*: satu piksel pada citra berkorespondensi dengan tak berhingga titik di sepanjang sinar pandang kamera. Metode tersupervisi awal, misalnya Eigen dkk. (bab 062), memecahkannya dengan melatih jaringan pada pasangan citra dan peta kedalaman dari sensor, tetapi label semacam itu mahal dan jarang. Jalur swa-awas dibuka oleh Monodepth (bab 063), yang memakai konsistensi kiri-kanan pada pasangan stereo, lalu disempurnakan Monodepth2 (bab 064), yang melatih kedalaman dan ego-gerak bersamaan dari video monokular dengan *loss* fotometrik.

Dua kelemahan spesifik masih melekat pada jalur swa-awas itu. Pertama, arsitektur *encoder-decoder* konvensional menurunkan resolusi fitur dengan *max-pooling* atau konvolusi berlangkah (*strided convolution*). Kedua operasi itu membuang informasi spasial frekuensi tinggi, sehingga objek tipis dan jauh — tiang, pejalan kaki — menjadi kabur pada peta kedalaman keluaran. Kedua, kedalaman monokular swa-awas hanya terdefinisi sampai faktor skala yang tidak diketahui: video yang sama direkonstruksi sama baiknya pada dunia berukuran dua kali lipat dengan kamera bergerak dua kali lebih cepat. Akibatnya, evaluasi standar harus menyamakan skala prediksi dengan ground truth menggunakan median, dan hasilnya tidak langsung dapat dipakai untuk navigasi kendaraan yang menuntut jarak dalam meter.

## Ide Utama

Gagasan inti PackNet adalah mengganti pembuangan informasi dengan pemadatan informasi. Alih-alih menurunkan resolusi dengan membuang piksel, blok *packing* memindahkan detail spasial ke dimensi kanal secara utuh melalui operasi *space-to-depth*, lalu memadatkannya dengan konvolusi 3D yang dipelajari. Di sisi dekoder, blok *unpacking* melakukan proses cermin: konvolusi 3D menyiarkan kembali informasi kanal ke ruang spasial melalui operasi *depth-to-space*. Karena pemadatan dan pemulihan sama-sama dipelajari dan simetris, jaringan dapat memutuskan sendiri detail mana yang disimpan pada setiap tingkat resolusi.

Gagasan kedua bersifat geometris. Ketidakpastian skala monokular dapat dihapus dengan satu pengukuran eksternal yang murah: kecepatan kamera, yang pada kendaraan tersedia dari odometri. Dengan menambahkan *loss* yang mencocokkan besaran translasi prediksi jaringan pose terhadap kecepatan terukur, seluruh sistem — kedalaman dan gerak — terkunci pada skala metrik tanpa satu pun label kedalaman.

## Cara Kerja Langkah demi Langkah

### Pelatihan Swa-awas dengan Loss Fotometrik

Kerangka pelatihan mewarisi Monodepth2 (bab 064). Dua jaringan dilatih bersama: jaringan kedalaman (PackNet) yang menerima satu *frame* target dan mengeluarkan peta kedalaman per piksel, serta jaringan pose yang menerima pasangan *frame* dan mengeluarkan satu transformasi kaku (rotasi dan translasi) di antara keduanya. Dengan kedalaman target, pose relatif, dan intrinsik kamera yang diketahui, piksel dari *frame* tetangga dapat diproyeksikan ulang ke *frame* target. Selisih fotometrik antara citra target asli dan citra hasil pelengkungan (*warping*) — diukur dengan kombinasi L1 dan SSIM (*Structural Similarity*, ukuran kemiripan struktur citra) — menjadi sinyal pelatihan. Kedalaman yang salah menghasilkan rekonstruksi yang buruk, sehingga meminimalkan selisih ini sama artinya dengan mempelajari geometri adegan, tanpa label kedalaman.

### Blok Packing: Space-to-Depth dan Konvolusi 3D

Komponen pertama blok packing adalah *space-to-depth* (diperkenalkan pada SuperDepth, ICRA 2019): piksel disusun ulang tanpa ada yang dibuang. Secara konkret, fitur berukuran H×W×C dipartisi menjadi blok 2×2 piksel; keempat piksel setiap blok ditumpuk menjadi empat kanal pada satu posisi, menghasilkan H/2×W/2×4C. Resolusi spasial berkurang separuh pada tiap sumbu, tetapi seluruh informasi tetap ada — berbeda dengan *max-pooling* yang membuang tiga dari empat nilai.

Komponen kedua adalah konvolusi 3D, yaitu konvolusi yang kaidahnya sama dengan konvolusi 2D tetapi kernel-nya membentang pada tiga dimensi. Pada PackNet, tumpukan kanal hasil *space-to-depth* diperlakukan sebagai volume dengan dimensi kedalaman buatan, sehingga kernel 3D dapat mencampur informasi antar-piksel yang semula bertetangga sekaligus antar-kanal fitur. Hasilnya adalah representasi termampatkan yang mempertahankan detail halus; penulis menyebutnya *3D inductive bias* (bias struktural yang cocok dengan sifat 3D adegan). *Encoder* PackNet menyusun beberapa blok packing bertingkat hingga fitur mencapai resolusi terkecil.

### Blok Unpacking: Proses Cermin di Dekoder

Dekoder membalik urutan tersebut dengan blok *unpacking*: konvolusi 3D terlebih dahulu memperluas informasi kanal, kemudian *depth-to-space* menyusun ulang kanal menjadi piksel spasial — kebalikan persis dari *space-to-depth* — sehingga resolusi naik dua kali per blok tanpa interpolasi. Pada *upsampling* konvensional (misalnya *nearest-neighbor* lalu konvolusi), nilai piksel baru dihasilkan dengan menebak dari tetangganya; pada *unpacking*, nilai piksel baru direkonstruksi dari informasi yang memang disimpan saat *packing*. Dekoder juga menerapkan super-resolusi kedalaman ala SuperDepth: kedalaman diprediksi pada beberapa resolusi dan dihaluskan hingga resolusi penuh.

Diagram alur satu pasang blok simetris:

```
ENCODER (packing)                  DECODER (unpacking)
H x W x C                          H/2 x W/2 x C'
   | space-to-depth                    | konvolusi 3D
   v (blok 2x2 -> kanal)               v
H/2 x W/2 x 4C  ---------------->  H x W x C''  (keluaran)
   | konvolusi 3D                  ^ depth-to-space
   v (padatkan kanal)              | (kanal -> blok 2x2)
H/2 x W/2 x C'  ------------------ +
```

Panah mendatar menyatakan hubungan simetris: apa yang dipadatkan *encoder* pada resolusi tertentu dipulihkan dekoder pada resolusi yang sama, ditambah koneksi lintas (*skip connection*) seperti pada U-Net pada umumnya.

### Supervisi Kecepatan untuk Skala Metrik

Jaringan pose memprediksi vektor translasi antar-*frame*. Tanpa pengikat eksternal, norma vektor ini bebas berskala. Supervisi kecepatan menambahkan *loss* sederhana: norma translasi prediksi pada interval waktu antar-*frame* harus cocok dengan jarak tempuh yang dihitung dari kecepatan kendaraan terukur. Karena kedalaman dan pose dilatih bersama dan saling terkait melalui proyeksi geometris, penguncian skala pada pose merambat ke peta kedalaman. Hasilnya, model (disebut PackNet-SfM, *structure-from-motion*) mengeluarkan kedalaman dalam meter dan tidak lagi memerlukan penyamaan skala median terhadap ground truth saat pengujian — pada tolok ukur odometri KITTI, varian ini tetap kompetitif terhadap metode monokular lain yang justru masih memerlukan penskalaan ground truth.

### Inferensi

Saat inferensi hanya jaringan kedalaman yang dipakai: satu citra masuk, peta kedalaman per piksel keluar dalam satu lintasan maju. Karena tidak bergantung pada pra-pelatihan ImageNet, seluruh bobot dipelajari untuk tugas geometris ini; dengan optimasi TensorRT, model berjalan *real-time*.

## Eksperimen dan Hasil

Evaluasi mengikuti protokol Eigen dengan praproses Zhou dkk. (membuang *frame* statis dari data latih) pada KITTI. Metrik utama: AbsRel (*absolute relative error*, rata-rata selisih relatif terhadap ground truth, makin kecil makin baik), RMSE (akar rata-rata kuadrat galat dalam meter), dan δ<1,25 (persentase piksel dengan rasio prediksi/ground truth di bawah 1,25, makin besar makin baik). Angka berikut dari repositori resmi TRI-ML (resolusi masukan 192×640, kecuali disebut lain):

- *Baseline* ResNet18 swa-awas (pra-latih ImageNet): AbsRel 0,116; RMSE 4,902; δ<1,25 = 0,865.
- PackNet swa-awas (tanpa pra-latih ImageNet): AbsRel 0,111; RMSE 4,576; δ<1,25 = 0,880.
- PackNet sadar-skala (CS→K, dilatih awal di Cityscapes lalu KITTI): AbsRel 0,108; δ<1,25 = 0,887; pada resolusi 384×1280 membaik menjadi AbsRel 0,106 dan δ<1,25 = 0,895.

Interpretasinya tiga hal. Pertama, pada arsitektur dan data yang sama, mengganti *downsampling* standar dengan blok packing mengurangi AbsRel dari 0,116 ke 0,111 dan mengungguli Monodepth2 (sekitar 0,115 pada pengaturan setara), padahal tanpa bantuan bobot ImageNet. Kedua, kenaikan resolusi masukan dua kali lipat memperbaiki semua metrik — perilaku yang jarang pada arsitektur 2D, yang cenderung jenuh atau *overfitting* — dan dijadikan bukti *3D inductive bias*. Ketiga, makalah melaporkan bahwa pada tolok ukur daring KITTI (dengan ground truth yang diperbaiki) PackNet-SfM mengungguli metode swa-awas, semi-supervisi, dan tersupervisi penuh saat rilis.

Pada DDAD (384×640), PackNet swa-awas mencapai AbsRel 0,162 dan δ<1,25 = 0,823, dibandingkan baseline ResNet18 0,213 dan 0,761. Nilai AbsRel DDAD jauh lebih besar daripada di KITTI bukan karena model memburuk, melainkan karena ground truth DDAD menjangkau jarak jauh (hingga 250 m), sehingga galat pada jarak yang sulit ikut dihitung — celah antarmetode justru melebar pada rentang jauh. Generalisasi lintas domain diuji dengan mengevaluasi model terlatih langsung pada NuScenes tanpa penyetelan, dan PackNet dilaporkan menggeneralisasi lebih baik dari pembanding.

DDAD sendiri adalah kontribusi data: 194 adegan latih (17.050 sampel) dan 60 adegan validasi (4.150 sampel) dari Amerika Serikat (San Francisco, Detroit, Ann Arbor) dan Jepang (Tokyo, Odaiba); enam kamera *global-shutter* 2,4 MP (1936×1216) tersinkron 10 Hz dengan cakupan 360°; ground truth dari LiDAR Luminar berjangkauan 250 m dengan presisi di bawah 1 cm. Pada makalah ini hanya kamera depan yang dipakai.

## Kelebihan dan Keterbatasan

Kelebihan: (1) detail spasial terjaga berkat pemadatan tanpa pembuangan informasi, terlihat dari perbaikan konsisten atas baseline ber-pooling; (2) skala metrik dari isyarat kecepatan menghapus kebutuhan penskalaan ground truth saat pengujian; (3) membaik dengan resolusi dan parameter, sehingga pengguna dapat menukar komputasi dengan akurasi; (4) tidak memerlukan pra-pelatihan ImageNet dan berjalan *real-time*; (5) DDAD menyediakan evaluasi jarak jauh yang lebih rapat daripada KITTI.

Keterbatasan: (1) konvolusi 3D dan penyimpanan kanal hasil *packing* menambah beban komputasi dan memori dibanding *encoder* 2D setara, sehingga mode *real-time* memerlukan optimasi khusus seperti TensorRT; (2) skala metrik bergantung pada ketersediaan pengukuran kecepatan kamera — pada video umum tanpa odometri, keunggulan sadar-skala tidak berlaku; (3) seluruh evaluasi berada pada domain berkendara dengan gerak kamera dominan maju, sehingga klaim pada adegan umum belum teruji; (4) dari sisi rekayasa, *loss* fotometrik tetap mewarisi kelemahan Monodepth2 terhadap objek bergerak dan permukaan tak bertekstur, karena mekanisme pelatihannya tidak diubah pada makalah ini.

## Kaitan dengan Bab Lain

Bab ini meneruskan garis swa-awas yang dibangun pada bab-bab sebelumnya: formulasi kedalaman-dari-video beserta *loss* fotometrik dan jaringan pose diwarisi langsung dari [Monodepth2](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md) (bab 064), yang sendiri melanjutkan konsistensi fotometrik [Monodepth](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md) (bab 063) dan tradisi regresi kedalaman monokular [Eigen dkk.](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md) (bab 062). Kontribusi PackNet bersifat ortogonal: bukan mengubah sumber supervisi, melainkan mengganti mekanisme kompresi fitur. Posisinya berseberangan dengan [MiDaS](./068%20-%202022%20-%20MiDaS%20%28Robust%20Monocular%20Depth%29%20-%20Estimasi%20Kedalaman.md) (bab 068) yang mengejar ketangguhan lintas dataset dengan kedalaman relatif — PackNet justru mengejar skala metrik pada satu domain berkendara. Bagi tinjauan RGB-D, PackNet memperlihatkan bahwa pseudo-kedalaman dari kamera tunggal dapat mencapai kualitas dan skala metrik yang layak menjadi pengganti atau pelengkap sensor kedalaman aktif.

## Poin untuk Sitasi

Kutip dengan kunci `guizilini2020packnet`. Ringkasan yang aman dikutip: "PackNet melatih estimasi kedalaman monokular secara swa-awas dari video dengan blok packing/unpacking simetris berbasis konvolusi 3D yang mempertahankan detail spasial, serta supervisi kecepatan lemah yang memulihkan skala metrik; pada KITTI model ini mengungguli metode swa-awas dan sejumlah metode tersupervisi saat rilis, dan ikut merilis dataset DDAD dengan ground truth LiDAR berjangkauan 250 m."

Catatan verifikasi: angka AbsRel/RMSE/δ pada bagian Eksperimen dikutip dari tabel model pada repositori resmi TRI-ML, bukan dari tabel naskah; angka naskah sedikit berbeda karena DDAD diperbarui setelah CVPR 2020. Klaim "mengungguli metode tersupervisi penuh" merujuk pada tolok ukur daring KITTI sebagaimana dinyatakan abstrak — angka persisnya pada tabel naskah perlu dicek sebelum sitasi formal. Detail internal konvolusi 3D (jumlah blok, jumlah kanal per tingkat) tidak diperinci dalam bab ini dan perlu dirujuk ke naskah atau kode sumber.
