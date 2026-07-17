# 036 - BBS-Net: RGB-D Salient Object Detection with a Bifurcated Backbone Strategy Network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fan2020bbsnet` |
| Judul asli | BBS-Net: RGB-D Salient Object Detection with a Bifurcated Backbone Strategy Network |
| Penulis | Deng-Ping Fan; Yingjie Zhai; Ali Borji; Jufeng Yang; Ling Shao |
| Tahun | 2020 |
| Venue | European Conference on Computer Vision (ECCV), hlm. 275–292 |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (teks lengkap):** https://arxiv.org/abs/2007.02713
- **DOI versi jurnal (IEEE TIP 2021):** https://doi.org/10.1109/TIP.2021.3116793
- **Repositori kode resmi:** https://github.com/DengPingFan/BBS-Net
- **Google Scholar:** https://scholar.google.com/scholar?q=BBS-Net%3A%20RGB-D%20Salient%20Object%20Detection%20with%20a%20Bifurcated%20Backbone%20Strategy%20Network
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=BBS-Net%3A%20RGB-D%20Salient%20Object%20Detection%20with%20a%20Bifurcated%20Backbone%20Strategy%20Network&sort=relevance

## Gambaran Umum
BBS-Net adalah jaringan saraf untuk deteksi objek menonjol (*salient object detection*, SOD) pada masukan RGB-D, yaitu pasangan citra warna dan peta kedalaman yang setiap pikselnya menyatakan jarak ke kamera. Makalah ini menangani dua kelemahan metode RGB-D SOD sebelumnya: penggabungan fitur multi-level yang tidak membedakan karakter tiap level, dan pemanfaatan peta kedalaman yang dangkal. Solusinya dua. Pertama, *bifurcated backbone strategy* (BBS) membagi fitur multi-level menjadi kelompok fitur guru (level tinggi) dan fitur murid (level rendah), lalu memakai peta saliens dari fitur guru untuk membersihkan derau pada fitur murid. Kedua, *depth-enhanced module* (DEM) memperkuat fitur kedalaman dengan perhatian kanal dan spasial sebelum digabung dengan fitur RGB. Pada delapan dataset benchmark dan lima metrik evaluasi, BBS-Net mengungguli 18 model pembanding, dengan peningkatan S-measure sekitar 4% terhadap model peringkat teratas saat itu, DMRA (ICCV 2019).

## Latar Belakang: Masalah yang Ingin Dipecahkan
SOD bertujuan menemukan dan mensegmentasi objek yang paling menonjol secara visual dalam sebuah citra, dan hasilnya berupa peta saliens biner. Model SOD yang hanya memakai citra RGB mengalami penurunan kinerja pada skenario sulit: latar belakang kompleks, objek ganda, dan pencahayaan bervariasi. Peta kedalaman membantu karena memuat struktur spasial dan tata letak objek, dan kini mudah diperoleh dari kamera stereo, Kinect, maupun telepon pintar.

Masalah pertama adalah agregasi fitur multi-level. *Backbone* konvolusi menghasilkan fitur pada beberapa level: fitur level rendah memuat detail tepi tetapi juga derau dari latar belakang, sedangkan fitur level tinggi memuat informasi semantik tetapi kehilangan detail spasial. Metode seperti DMRA (dibahas pada [bab 035](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)) menggabungkan semua level secara langsung, sehingga derau fitur rendah ikut masuk ke prediksi.

Masalah kedua adalah ekstraksi informasi dari modalitas kedalaman. Pendekatan yang lazim sebelumnya hanya menjadikan peta kedalaman sebagai kanal masukan keempat, atau menggabungkan fitur RGB dan kedalaman dengan penjumlahan atau perkalian sederhana. Perlakuan ini mengabaikan perbedaan modalitas: citra RGB merekam warna dan tekstur, sedangkan peta kedalaman merekam relasi spasial. Selain itu, peta kedalaman dari sensor konsumen sering kabur dan berderau, sehingga fusi yang naif justru memasukkan galat ke dalam jaringan.

## Ide Utama
Gagasan inti BBS-Net adalah memperlakukan fitur multi-level secara berbeda sesuai karakternya, alih-alih menggabungkannya sekaligus. Fitur level tinggi (disebut fitur guru, *teacher features*) diproses lebih dahulu untuk menghasilkan peta saliens awal S1. Peta bernilai [0,1] ini berfungsi sebagai penapis: fitur level rendah (fitur murid, *student features*) dikalikan elemen-demi-elemen dengan S1, sehingga respons pada daerah latar ditekan sedangkan respons pada daerah objek dipertahankan. Fitur murid yang telah dibersihkan kemudian diproses menjadi peta saliens akhir S2. Modalitas kedalaman pun tidak digabung mentah-mentah; fitur kedalaman diperkuat dahulu oleh DEM melalui dua operasi perhatian berurutan, baru kemudian dijumlahkan dengan fitur RGB. Masukan jaringan adalah sepasang citra RGB dan peta kedalaman; keluarannya adalah dua peta saliens, S1 dan S2, dengan S2 sebagai hasil akhir.

## Cara Kerja Langkah demi Langkah
Alur data BBS-Net digambarkan pada diagram berikut.

```
 RGB 352×352×3  ┌───────────────┐
 ──────────────►│ ResNet-50     │──► f1..f5 (RGB) ────────────────┐
                │ (cabang RGB)  │                                 │
                └───────────────┘                                 ▼
                                                  f_cm = f_rgb + DEM(f_d)
 Depth 352×352×1┌───────────────┐   f1..f5 (D)  ┌───────┐         │
 ──────────────►│ ResNet-50     │──────────────►│  DEM  │─────────┘
                │ (cabang D)    │               └───────┘
                └───────────────┘

 Fitur lintas-modal f1..f5 (cm), titik belah pada Conv3:

  guru  {f3,f4,f5} ─► CD1 (GCM + agregasi) ─► T1 ─► S1 ─────────┐
                                                                │ perkalian
  murid {f1,f2,f3} ─► f'(i) = f(i) + f(i)⊙S1 ◄──────────────────┘
                      ─► CD2 ─► PTM ──► S2 (peta saliens akhir)
```

Diagram di atas merangkum dua cabang ekstraksi fitur, penggabungan lintas-modal setelah DEM, dan pemrosesan berurutan kelompok guru-murid oleh dua dekoder bertingkat (CD1, CD2). Rincian tiap tahap diuraikan di bawah.

### Ekstraksi fitur dua cabang
Masukan RGB dan kedalaman masing-masing diubah ukurannya menjadi 352×352 piksel dan diproses oleh dua backbone ResNet-50 yang terpisah tanpa berbagi bobot. ResNet-50 adalah jaringan konvolusi 50 lapis dengan sambungan residual (jalan pintas yang menjumlahkan masukan dan keluaran blok), yang bobot awalnya diambil dari pelatihan klasifikasi ImageNet. Kedua cabang identik kecuali jumlah kanal masukan: tiga untuk RGB, satu untuk kedalaman. Lima blok konvolusi (Conv1 sampai Conv5) menghasilkan fitur multi-level dengan ukuran spasial menurun dan kanal meningkat: Conv1 menghasilkan 88×88×64, Conv3 menghasilkan 44×44×512, dan Conv5 menghasilkan 11×11×2048. Fitur Conv1 yang beresolusi tinggi memuat detail tepi; fitur Conv5 yang beresolusi rendah memuat rangkuman semantik posisi objek.

### Depth-Enhanced Module (DEM)
DEM ditempatkan pada setiap keluaran samping (*side-out*) cabang kedalaman sebelum penggabungan. Fungsinya meningkatkan kompatibilitas dengan fitur RGB sekaligus meredam derau kedalaman. DEM terdiri dari dua operasi perhatian berurutan. Operasi pertama, perhatian kanal (*channel attention*), menerapkan penyatuan maksimum global (*global max pooling*) pada setiap kanal peta fitur, meneruskan vektor hasilnya ke perceptron dua lapis, dan mengalikan kembali bobot yang diperoleh ke tiap kanal untuk menonjolkan kanal informatif. Operasi kedua, perhatian spasial (*spatial attention*), mengambil nilai maksimum sepanjang sumbu kanal pada setiap posisi piksel, menerapkan satu lapis konvolusi, dan mengalikan peta bobot spasial hasilnya ke fitur untuk menonjolkan lokasi informatif. Fitur lintas-modal kemudian dibentuk dengan penjumlahan elemen-demi-elemen: f(i,cm) = f(i,rgb) + DEM(f(i,d)). DEM hanya memakai penyatuan maksimum global tanpa penyatuan rata-rata, karena SOD hanya memerlukan isyarat paling menonjol; pilihan ini menekan kompleksitas modul.

### Strategi bifurkasi dan penyempurnaan bertingkat
Lima fitur lintas-modal dibagi menjadi dua kelompok yang tumpang tindih pada Conv3 sebagai titik belah: kelompok murid G1 = {f1, f2, f3} dan kelompok guru G2 = {f3, f4, f5}. Tahap pertama, dekoder bertingkat CD1 mengagregasi ketiga fitur guru, dan dua lapis konvolusi sederhana (T1) mengubah kanal menjadi satu untuk menghasilkan peta awal S1. Karena fitur guru kaya semantik, S1 menandai posisi objek dengan andal tetapi bertepi kasar. Tahap kedua, setiap fitur murid diperbarui dengan aturan residual: f'(i) = f(i) + f(i)⊙S1, dengan ⊙ menyatakan perkalian elemen-demi-elemen. Perkalian menekan aktivasi latar, dan penjumlahan menjaga detail objek tetap utuh. Fitur murid hasil pembaruan diagregasi oleh dekoder kedua CD2 menjadi peta akhir S2.

### Dekoder bertingkat: GCM dan agregasi piramidal
Setiap dekoder bertingkat terdiri dari tiga *global context module* (GCM) dan satu strategi agregasi. GCM adalah penyempurnaan dari *receptive field block* (RFB), modul multi-cabang yang memperluas lapang reseptif (wilayah citra yang memengaruhi satu unit fitur). Setiap GCM memiliki empat cabang paralel: semua cabang diawali konvolusi 1×1 yang mereduksi kanal menjadi 32; cabang ke-k (k = 2, 3, 4) menerapkan konvolusi berkernel 2k−1 (3, 5, dan 7) berdilatasi 1, diikuti konvolusi 3×3 berdilatasi 2k−1. Dilatasi, yaitu jarak antar-titik sampel kernel, membuat kernel kecil mencakup wilayah luas tanpa tambahan parameter. Keluaran keempat cabang digabungkan, direduksi kembali menjadi 32 kanal oleh konvolusi 3×3, dan dijumlahkan dengan masukan melalui sambungan residual. Setelah GCM, agregasi piramidal dilakukan: setiap fitur dikalikan dengan versi tercuplik-naik (*upsampling*, peningkatan resolusi spasial melalui interpolasi) dari semua fitur level lebih tinggi, kemudian hasilnya digabungkan dengan konkatenasi progresif.

### Modul peluas bertahap dan pelatihan
Keluaran CD2 berukuran 88×88, yaitu seperempat resolusi masukan 352×352. Pencuplikan naik langsung empat kali akan menghilangkan detail, sehingga dipakai *progressively transposed module* (PTM): dua blok residual berbasis konvolusi tertransposisi (konvolusi yang menaikkan resolusi) dan tiga konvolusi 1×1, yang memperbesar peta secara bertahap hingga ukuran penuh. Pelatihan mengoptimalkan rugi entropi silang biner (ukuran selisih antara peta prediksi dan acuan piksel demi piksel) pada S1 dan S2 dengan bobot sama (λ = 0,5). Optimisasi memakai Adam dengan laju pembelajaran awal 10⁻⁴ yang dibagi sepuluh setiap 60 epoch, ukuran batch 10, selama 150 epoch (±10 jam pada satu GPU GTX 1080 Ti), dengan augmentasi pembalikan, rotasi, dan pemotongan batas acak.

## Eksperimen dan Hasil
Evaluasi dilakukan pada tujuh dataset benchmark RGB-D SOD: NJU2K (1.985 pasangan), NLPR (1.000 pasangan, Kinect 640×480), STERE (1.000 pasangan), DES (135 pasangan dalam ruang), LFSD (100 pasangan), SSD (80 pasangan), dan SIP (1.000 pasangan dari telepon pintar, 992×744); versi jurnal menambahkan dataset DUT sehingga menjadi delapan. Sesuai protokol DMRA, pelatihan memakai 1.485 sampel NJU2K dan 700 sampel NLPR; sisanya menjadi data uji. Lima metrik dipakai: S-measure (kesamaan struktur peta dengan acuan), F-measure maksimum (rata-rata harmonik presisi dan *recall*), E-measure maksimum (keselarasan piksel dan global), MAE (galat absolut rata-rata; makin kecil makin baik), dan kurva presisi-recall.

Tabel berikut membandingkan S-measure BBS-Net (backbone ResNet-50) dengan DMRA, pembanding terkuat, pada tujuh dataset.

| Dataset | S-measure DMRA | S-measure BBS-Net |
|---|---|---|
| NJU2K | 0,886 | 0,921 |
| NLPR | 0,899 | 0,930 |
| STERE | 0,886 | 0,908 |
| DES | 0,900 | 0,933 |
| LFSD | 0,839 | 0,864 |
| SSD | 0,857 | 0,882 |
| SIP | 0,806 | 0,879 |

BBS-Net unggul pada seluruh dataset, dengan selisih 2,1 sampai 7,3 poin S-measure. Keunggulan terbesar terjadi pada SIP, dataset dengan latar paling bervariasi, yang menunjukkan bahwa penekanan derau fitur murid paling berdampak pada skenario sulit. Pada NJU2K, MAE turun dari 0,051 menjadi 0,035 (sekitar sepertiga lebih kecil). Secara keseluruhan, peningkatan terhadap pembanding terbaik berkisar 2,5–3,5% untuk S-measure dan 0,009–0,016 untuk MAE, konsisten dengan klaim abstrak berupa perbaikan S-measure ±4% terhadap DMRA. Kecepatan inferensi mencapai 24,32 fps pada GTX 1080 Ti dengan 49,77 juta parameter dan 31,40 GFLOPs, cukup untuk pemrosesan mendekati waktu nyata. Versi jurnal menambahkan varian efisien yang berbagi bobot antar-cabang dengan modul adaptasi kedalaman: parameternya tinggal 25,96 juta (±50%) dengan kinerja hampir sama.

## Kelebihan dan Keterbatasan
Kelebihan utama BBS-Net adalah kesederhanaan konsepnya: strategi bifurkasi dan DEM tidak terikat pada backbone tertentu, dan keunggulan tetap diperoleh dengan backbone VGG-16 maupun VGG-19, bukan hanya ResNet-50. Penyempurnaan hanya memerlukan satu putaran, tidak berulang seperti metode pemurnian sebelumnya, sehingga biaya komputasi terkendali.

Keterbatasan pertama adalah ukuran model: dua backbone tanpa berbagi bobot menghasilkan 49,77 juta parameter. Dari sisi rekayasa, angka ini berat untuk perangkat tepi, dan penulis sendiri mengusulkan varian efisien pada versi jurnal. Keterbatasan kedua, secara konseptual DEM meredam tetapi tidak menghilangkan ketergantungan pada kualitas peta kedalaman; pada kedalaman yang sangat rusak, isyarat spasial yang diekstrak tetap terbatas. Keterbatasan ketiga, backbone konvolusi memiliki lapang reseptif terbatas; GCM memperluasnya, tetapi konteks global tetap tidak ditangkap sebaik pada arsitektur berbasis *transformer* yang muncul kemudian.

## Kaitan dengan Bab Lain
BBS-Net melanjutkan garis karya RGB-D SOD berbasis CNN: DMRA pada [bab 035](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md) adalah pembanding utama sekaligus sumber protokol pelatihan yang dipakai ulang, sedangkan dekoder bertingkatnya dikembangkan dari CPD (Wu dkk., CVPR 2019) yang kodenya menjadi dasar implementasi resmi. Gagasan memilah fitur sebelum diagregasi menjadi acuan karya berikutnya; D3Net pada [bab 037](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md) mempertanyakan ulang desain fusi RGB-D, dan strategi pemisahan fitur guru-murid banyak diadopsi arsitektur RGB-D SOD setelahnya.

## Poin untuk Sitasi
Kunci BibTeX: `fan2020bbsnet`. Ringkasan yang aman dikutip: BBS-Net (Fan dkk., ECCV 2020) mengusulkan strategi backbone bercabang yang memisahkan fitur multi-level menjadi fitur guru dan murid, modul penguat kedalaman berbasis perhatian kanal-spasial, serta penyempurnaan bertingkat satu putaran untuk RGB-D SOD; model ini mengungguli 18 metode pada delapan dataset dengan peningkatan S-measure sekitar 4% terhadap DMRA. Catatan verifikasi: angka S-measure dan MAE per dataset, parameter, FLOPs, dan kecepatan diambil dari tabel versi jurnal IEEE TIP 2021 (arXiv v3); tabel versi prosiding ECCV 2020 dapat sedikit berbeda dan perlu dicocokkan sebelum sitasi formal. Varian efisien dengan modul adaptasi kedalaman hanya ada pada versi jurnal, bukan versi konferensi.
