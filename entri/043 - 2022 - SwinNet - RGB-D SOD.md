# 043 - SwinNet: Swin Transformer Drives Edge-Aware RGB-D and RGB-T Salient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2021swinnet` |
| Judul asli | SwinNet: Swin Transformer Drives Edge-Aware RGB-D and RGB-T Salient Object Detection |
| Penulis | Zhengyi Liu, Yacheng Tan, Qian He, Yun Xiao |
| Tahun | 2022 |
| Venue | IEEE Transactions on Circuits and Systems for Video Technology (TCSVT), vol. 32, no. 7, hlm. 4486–4497 |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2204.05585
- **DOI (versi penerbit):** https://doi.org/10.1109/TCSVT.2021.3127149
- **Kode sumber (GitHub):** https://github.com/liuzywen/SwinNet
- **Google Scholar:** https://scholar.google.com/scholar?q=SwinNet%3A%20Swin%20Transformer%20Drives%20Edge-Aware%20RGB-D%20and%20RGB-T%20Salient%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=SwinNet%3A%20Swin%20Transformer%20Drives%20Edge-Aware%20RGB-D%20and%20RGB-T%20Salient%20Object%20Detection&sort=relevance

## Gambaran Umum

SwinNet adalah model fusi lintas-modalitas untuk *salient object detection* (SOD), yaitu tugas memetakan piksel pembentuk objek paling menonjol dalam citra. Satu desain yang sama dipakai untuk dua tugas: SOD pada pasangan citra RGB dan peta kedalaman (RGB-D), serta SOD pada pasangan citra RGB dan citra termal (RGB-T). Tiga komponen menyusun model ini: *backbone* Swin Transformer dua aliran untuk mengekstrak fitur hierarkis kedua modalitas, modul penyelarasan spasial dan rekalibrasi kanal untuk fusi fitur per tingkat, serta dekoder terpandu tepi yang mempertajam kontur objek.

Model ini melaporkan kinerja terbaik pada enam tolok ukur RGB-D dan tiga tolok ukur RGB-T. Pada dataset NLPR, S-measure mencapai 0,941, melampaui Visual Saliency Transformer (0,931) sebagai pembanding *transformer* terdekat. Biaya yang harus dibayar adalah kompleksitas tinggi, sebagaimana dibahas pada bagian Keterbatasan.

## Latar Belakang: Masalah yang Ingin Dipecahkan

SOD pada citra RGB tunggal menurun ketika pencahayaan kurang atau latar belakang rumit. Dua modalitas pelengkap terbukti membantu: peta kedalaman menyediakan informasi geometri yang tidak peka terhadap perubahan cahaya, sedangkan citra termal menangkap radiasi panas objek sehingga tetap bekerja dalam gelap atau cuaca buruk. Informasi pelengkap ini hanya berguna bila fusi lintas-modalitas dilakukan dengan tepat.

Sebelum SwinNet, metode RGB-D dan RGB-T SOD hampir seluruhnya dibangun di atas jaringan saraf konvolusi (CNN), misalnya BBS-Net (bab 036). CNN mengumpulkan informasi dari piksel tetangga dalam *receptive field* (wilayah pandang) terbatas dan kehilangan informasi spasial akibat operasi *pooling*, sehingga ketergantungan semantik jarak jauh sulit dipelajari. Visual Saliency Transformer atau VST (bab 042) menjadi pelopor penggunaan *transformer* untuk tugas ini; SwinNet mengambil langkah berikutnya dengan Swin Transformer (bab 025) yang memadukan lokalitas dan hierarki ala CNN dengan pemodelan ketergantungan global. Makalah ini sekaligus menjawab dua masalah lain: metode sebelumnya umumnya khusus untuk kedalaman saja atau termal saja, dan batas objek cenderung kabur karena fitur dangkal pembawa detail tepi bercampur derau latar.

## Ide Utama

Gagasan intinya terdiri atas tiga keputusan. Pertama, dua *backbone* Swin Transformer mengekstrak fitur RGB dan modalitas pelengkap sehingga fitur hierarkis keduanya berkonteks global. Kedua, fusi lintas-modalitas pada setiap tingkat fitur dilakukan dalam dua langkah: penyelarasan spasial terlebih dahulu, karena posisi objek menonjol harus sama pada kedua modalitas; kemudian rekalibrasi kanal, karena tiap modalitas menonjolkan isi yang berbeda — RGB kaya tekstur, kedalaman kaya struktur. Ketiga, kontur dipertajam oleh fitur tepi dari lapisan dangkal *backbone* kedalaman yang memandu dekoder. Karena kedalaman dan termal berperan sama sebagai modalitas pelengkap, desain yang identik berlaku untuk kedua tugas tanpa perubahan.

## Cara Kerja Langkah demi Langkah

### Backbone Swin Transformer Dua Aliran

Swin Transformer adalah *backbone* berbasis *self-attention* (mekanisme di mana tiap elemen fitur menimbang hubungannya dengan elemen lain) yang bekerja di dalam jendela lokal dan memindahkan jendela itu antarlapisan (*shifted window*), sehingga informasi menyebar lintas jendela dengan biaya linear terhadap ukuran citra. SwinNet memakai varian Swin-B yang digandakan menjadi dua aliran. Setiap aliran memecah citra masukan 384×384 menjadi *patch* (petak) tak bertumpang-tindih, kemudian memperkecil jumlah token secara bertahap melalui *patch merging* menjadi empat tingkat fitur hierarkis {STic} (warna) dan {STid} (kedalaman), i = 1 sampai 4. Karena peta kedalaman hanya berisi satu kanal, nilainya disalin menjadi tiga kanal agar cocok dengan bobot Swin-B terlatih. Alur lengkap model tergambar pada diagram berikut.

```
masukan: citra RGB + peta kedalaman (atau citra termal), masing-masing 384x384

 RGB --> [Swin-B aliran warna] --> STic (i=1..4) --+
                                                   |
 D/T --> [Swin-B aliran depth] --> STid (i=1..4) --+
            |                                      |
            | STid (i=1,2,3)                       v
            v                        [penyelarasan spasial +
   [modul sadar-tepi]                 rekalibrasi kanal]
   konv 1x1, upsampling,                         |
   penggabungan, atensi kanal                    v
            |                            Fic, Fid per tingkat
            v                                      |
      fitur tepi Fe                    fusi Fi = gabungan(Fid+Fic, Fid*Fic)
            |                                      |
            |                                      v
            |                    dekoder progresif gaya U-Net:
            |                    FF4 = F4
            |                    FFi = Fi + konv3(naik2(FFi+1)), i=1..3
            |                                      |
            +---------> gabungan(Fe, FF1) <--------+
                                  |
                                  v
                  konv 3x3 + upsampling 4x --> peta saliens S
```

Fusi terjadi dua kali: intra-tingkat pada setiap keluaran *backbone*, dan antar-tingkat di dalam dekoder.

### Penyelarasan Spasial dan Rekalibrasi Kanal

Modul ini bekerja terpisah pada setiap tingkat i. Pada penyelarasan spasial, fitur warna STic dan fitur kedalaman STid dikalikan elemen demi elemen; hasilnya diringkas dengan *global max pooling* sepanjang arah kanal, dilewatkan ke konvolusi 3×3, lalu diaktivasi sigmoid menjadi peta atensi spasial bersama SAi. Karena perkalian elemen hanya bernilai besar di posisi yang aktif pada kedua modalitas, SAi menyorot posisi menonjol yang disepakati keduanya; peta ini dikalikan kembali ke STic dan STid sehingga keduanya selaras. Pada rekalibrasi kanal, fitur yang telah selaras diringkas dengan *global max pooling*, dilewatkan ke konvolusi 1×1 dan sigmoid menjadi bobot atensi kanal yang berbeda untuk tiap modalitas. Bobot ini dikalikan ke fitur asal, menghasilkan fitur akhir Fic dan Fid yang selaras secara posisi dan tertimbang secara isi.

### Modul Sadar-Tepi

Fitur tingkat tinggi membawa makna semantik, sedangkan fitur dangkal membawa detail batas; objek menonjol juga cenderung *pop-out* pada peta kedalaman sehingga kontras kedalamannya memudahkan penggambaran kontur. Karena itu modul ini mengambil tiga fitur dangkal aliran kedalaman (STid untuk i = 1, 2, 3), memproyeksikan masing-masing dengan konvolusi 1×1, menyamakan ukurannya dengan *upsampling*, lalu menggabungkan ketiganya melalui konkatenasi (penyusunan fitur sepanjang dimensi kanal). Hasilnya dilewatkan ke atensi kanal dan koneksi residual — keluaran modul ditambahkan kembali ke masukannya — untuk menghasilkan fitur tepi Fe yang lebih bersih.

### Dekoder Terpandu Tepi

Pada setiap tingkat, Fic dan Fid dipadukan dengan penjumlahan, perkalian elemen, dan konkatenasi sekaligus: Fi = gabungan((Fid + Fic), (Fid × Fic)). Dekoder mengikuti pola U-Net, yaitu skema yang mengalirkan fitur tingkat tinggi ke tingkat yang lebih dangkal melalui *upsampling*: dimulai dari FF4 = F4, kemudian FFi = Fi + konv3(naik2(FFi+1)) untuk i = 1 sampai 3 (naik2 = pembesaran dua kali; konv3 = konvolusi 3×3). Terakhir, fitur tepi Fe digabungkan dengan FF1 menjadi fitur saliens terpandu tepi, yang dikonvolusi 3×3 dan diperbesar empat kali menjadi peta saliens akhir S. Peran Fe ganda: menekan derau latar yang terbawa fitur dangkal sekaligus mempertajam kontur.

### Fungsi Loss dan Pelatihan

Pelatihan diawasi dua fungsi *cross-entropy*: loss tepi dan loss saliens. Peta tepi dihasilkan dari fitur tepi Fe, dan targetnya diperoleh otomatis dengan menjalankan detektor tepi Canny pada peta saliens kebenaran, tanpa anotasi tepi tambahan. Masukan dilatih pada 384×384 dengan augmentasi pembalikan, rotasi, dan pemotongan tepi acak. Pengoptimal Adam dipakai dengan ukuran *batch* 3 dan laju pembelajaran awal 5×10⁻⁵ yang dibagi sepuluh setiap 100 *epoch*. Model konvergen dalam 200 *epoch*, sekitar 26 jam pada satu GPU NVIDIA RTX 2080Ti.

## Eksperimen dan Hasil

Evaluasi RGB-D dilakukan pada enam dataset: NLPR (1.000 citra), NJU2K (2.003 pasang citra stereo), STERE (1.000 pasang), DES (135 citra Kinect dalam ruang), SIP (1.000 citra manusia beresolusi tinggi), dan DUT (1.200 citra kamera Lytro). Data latih RGB-D berisi 2.185 pasang dari NJU2K dan NLPR, ditambah 800 pasang DUT bila pengujian dilakukan pada DUT. Evaluasi RGB-T dilakukan pada VT821 (821 pasang), VT1000 (1.000 pasang), dan VT5000 (5.000 pasang), dengan 2.500 pasang dari VT5000 sebagai data latih. Empat metrik dipakai: S-measure (kemiripan struktur antara prediksi dan kebenaran), F-measure (rata-rata harmonik berbobot *precision* dan *recall*), E-measure (kesejajaran global dan kecocokan piksel), serta MAE (rata-rata selisih absolut per piksel; semakin kecil semakin baik).

Hasil RGB-D: pada NLPR, S-measure 0,941 — naik 0,010 atas VST (0,931) dan 0,029 atas D3Net (0,912). Pada NJU2K, S-measure 0,935 dengan MAE 0,027; pada STERE 0,919; pada SIP 0,911 dengan MAE 0,035. Pengecualiannya DES: SwinNet hanya unggul tipis atas VST (0,945 lawan 0,943) karena dataset ini berisi 135 citra dalam ruang yang relatif mudah. Dibandingkan VST secara rata-rata lintas dataset, SwinNet memperbaiki keempat metrik sekitar 0,007 (S), 0,017 (F), 0,010 (E), dan 0,005 (MAE). Pada RGB-T marginnya lebih lebar: S-measure 0,904 pada VT821 (pembanding terbaik 0,885), 0,938 pada VT1000 (0,923), dan 0,912 pada VT5000 (0,883). Selisih hampir tiga poin pada dataset terbesar itu menunjukkan fusi yang tahan terhadap data beragam.

Ablasi memisahkan kontribusi tiap komponen. Pengujian *backbone* menempatkan Swin-B di atas semua alternatif: pada NLPR, S-measure 0,941 melawan 0,924 (ResNet-101), 0,932 (ResNet-50+ViT16), dan 0,925 (PVT-M). Mengganti modul penyelarasan dan rekalibrasi dengan *Depth-enhanced Module* dari BBS-Net (bab 036) menurunkan S-measure sekitar 0,006; penyelarasan posisi terbukti bernilai tambah di luar atensi biasa. Tanpa panduan tepi, S-measure turun sekitar 0,004 dan F-measure 0,009 (pada NJU2K dari 0,935 menjadi 0,928), sehingga kontribusi tepi nyata tetapi lebih kecil daripada *backbone*. Ablasi modalitas menunjukkan kedalaman saja (0,896 pada NLPR) kalah dari RGB saja (0,932), dan fusi (0,941) mengungguli keduanya; pada STERE, kedalaman saja anjlok ke 0,768 karena sebagian peta kedalamannya bermutu rendah.

## Kelebihan dan Keterbatasan

Kelebihan utama SwinNet adalah generalitas desain: satu arsitektur identik menangani kedalaman dan termal tanpa rekayasa khusus per modalitas. Panduan tepi menghasilkan kontur lebih tajam dengan biaya komputasi nyaris nol menurut analisis penulis, dan kode sumber tersedia publik sehingga hasil mudah direproduksi.

Keterbatasannya diakui penulis: 198,7 juta parameter, beban komputasi sekitar 124,3 GFLOPs, dan inferensi hanya sekitar 10 FPS termasuk prapemrosesan, dengan sebagian besar biaya pada dua *backbone* Swin-B; penulis menjadwalkan desain ringan sebagai pekerjaan lanjutan. Keunggulan pada DES juga sangat tipis, sehingga klaim keunggulan tidak seragam di semua kondisi. Dari sisi rekayasa, model bergantung pada mutu modalitas pelengkap: anjloknya hasil kedalaman saja pada STERE (0,768) menunjukkan fusi terbebani modalitas berderau, dan tidak ada mekanisme eksplisit untuk menilai keandalannya.

## Kaitan dengan Bab Lain

SwinNet berdiri langsung di atas [025 - 2021 - Swin Transformer - Fondasi RGB](./025%20-%202021%20-%20Swin%20Transformer%20-%20Fondasi%20RGB.md): *backbone* Swin-B beserta bobot terlatihnya dipakai apa adanya; kontribusinya terletak pada cara memadukan dua aliran. Dalam klaster RGB-D SOD, posisinya melanjutkan [042 - 2021 - Visual Saliency Transformer (VST) - RGB-D SOD](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md): keduanya menggantikan CNN dengan *transformer*, tetapi SwinNet memindahkan fusi lintas-modalitas ke mekanisme atensi spasial-kanal yang lebih sederhana daripada *cross-attention* VST, sekaligus mewarisi supervisi tepi. Terhadap metode CNN seperti [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md) dan [037 - 2021 - D3Net (Rethinking RGB-D SOD) - RGB-D SOD](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md), SwinNet menunjukkan lewat ablasi bahwa keunggulannya bukan sekadar *backbone*, melainkan juga strategi penyelarasan lintas modalitas.

## Poin untuk Sitasi

Kunci BibTeX: `liu2021swinnet`.

Ringkasan aman untuk dikutip: SwinNet (Liu dkk., TCSVT 2022) adalah model fusi lintas-modalitas berbasis *backbone* Swin Transformer dua aliran untuk deteksi objek menonjol RGB-D dan RGB-T dalam satu desain. Model ini menyelaraskan fitur kedua modalitas secara spasial dan menimbang ulang kanalnya pada setiap tingkat, lalu memadukannya antar-tingkat melalui dekoder yang dipandu fitur tepi dari lapisan dangkal modalitas pelengkap. Pada enam tolok ukur RGB-D dan tiga tolok ukur RGB-T, model melaporkan kinerja terbaik pada hampir semua metrik, dengan S-measure 0,941 pada NLPR dan 0,912 pada VT5000.

Catatan verifikasi sebelum sitasi formal: (1) seluruh angka pada bab ini diambil dari preprint arXiv:2204.05585v1; penulis menyatakan versi ini identik dengan artikel TCSVT, tetapi cocokkan kembali dengan Tabel I–VII versi penerbit. (2) Hasil pada dataset DUT tidak dikutip di sini karena kolomnya tidak terbaca utuh pada preprint. (3) Pada F-measure VT1000, CGFNet (0,906) tercatat di atas SwinNet (0,896), sehingga klaim "terbaik pada semua metrik" tidak tepat untuk sel tunggal tersebut. (4) Volume, nomor, dan halaman (32(7):4486–4497) berasal dari metadata repositori ini dan belum dicocokkan dengan sitasi IEEE.
