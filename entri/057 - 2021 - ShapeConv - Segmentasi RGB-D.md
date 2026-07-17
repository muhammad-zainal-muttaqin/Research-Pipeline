# 057 - ShapeConv: Shape-Aware Convolutional Layer for Indoor RGB-D Semantic Segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cao2021shapeconv` |
| Judul asli | ShapeConv: Shape-aware Convolutional Layer for Indoor RGB-D Semantic Segmentation |
| Penulis | Jinming Cao, Hanchao Leng, Dani Lischinski, Danny Cohen-Or, Changhe Tu, Yangyan Li |
| Tahun | 2021 |
| Venue | IEEE/CVF International Conference on Computer Vision (ICCV 2021), hal. 7088–7097 |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2108.10528
- **Repositori kode resmi (PyTorch):** https://github.com/hanchaoleng/ShapeConv
- **Google Scholar:** https://scholar.google.com/scholar?q=ShapeConv%3A%20Shape-Aware%20Convolutional%20Layer%20for%20Indoor%20RGB-D%20Semantic%20Segmentation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=ShapeConv%3A%20Shape-Aware%20Convolutional%20Layer%20for%20Indoor%20RGB-D%20Semantic%20Segmentation&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan ShapeConv (*Shape-aware Convolutional layer*), lapisan konvolusi yang dirancang khusus untuk memproses fitur kedalaman pada segmentasi semantik RGB-D. Segmentasi semantik adalah pelabelan kelas objek untuk setiap piksel citra; pada varian RGB-D, masukannya berupa citra warna (RGB) yang dipasangkan dengan peta kedalaman, yaitu citra yang setiap pikselnya menyimpan jarak permukaan ke kamera. Dasar gagasannya: nilai kedalaman sebuah *patch* — jendela kecil seluas ukuran *kernel* konvolusi — memuat dua informasi berbeda, yaitu posisi dasar *patch* itu dalam ruang dan bentuk geometri lokalnya (variasi relatif antarpiksel). Konvolusi biasa mencampur keduanya, padahal bentuk memiliki hubungan lebih kuat dengan kelas semantik daripada posisi absolut.

ShapeConv memisahkan kedua komponen tersebut, menimbangnya dengan dua bobot terlatih yang berbeda, lalu menggabungkannya kembali sebelum konvolusi diterapkan. Karena bobot itu menjadi konstanta setelah pelatihan, keduanya dapat dilebur ke dalam *kernel* konvolusi, sehingga jaringan saat inferensi identik dengan jaringan konvolusi biasa — tanpa tambahan komputasi maupun memori. Diuji pada tiga *benchmark* dalam-ruang (NYUDv2, SUN RGB-D, SID) dan lima arsitektur segmentasi, ShapeConv menaikkan mean IoU antara 0,7 hingga 6,0 poin.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum 2021, metode segmentasi RGB-D umumnya menempuh dua jalur. Jalur pertama memakai dua jaringan paralel yang fiturnya digabung pada titik-titik tertentu: FuseNet (bab 051) menjumlahkan fitur kedalaman ke cabang RGB, RDFNet (bab 053) memperluas fusi ke banyak tingkat jaringan, dan ACNet (bab 054) menimbang fitur kedua modalitas dengan modul atensi. Jalur ini menyisakan dua masalah: sulit menentukan pada tahap mana fusi paling tepat dilakukan, dan arsitektur dua cabang menaikkan biaya komputasi secara signifikan.

Jalur kedua merancang lapisan baru yang sadar geometri. Konvolusi sadar-kedalaman (*depth-aware convolution*, Wang dan Neumann 2018) menimbang kontribusi piksel berdasarkan kesamaan kedalamannya melalui fungsi Gaussian yang dirancang manual. Konvolusi 2,5D *malleable* (Xing dkk. 2020) mempelajari luas reseptif sepanjang sumbu kedalaman. S-Conv pada SGNet (Chen dkk. 2021) memprediksi pergeseran titik *sampling* konvolusi dari informasi spasial tiga dimensi. Ketiganya sejalan: konvolusi standar bukan alat yang tepat untuk data kedalaman.

Kekurangan spesifik yang disasar ShapeConv adalah ketiadaan pembedaan informasi di dalam *patch* kedalaman. Dua kursi berbentuk sama tetapi berjarak berbeda menghasilkan *patch* bernilai berbeda, sehingga konvolusi biasa mengekstrak fitur berbeda untuk keduanya — padahal bentuk keduanya identik. Sebaliknya, komponen dasar juga tidak dapat dibuang begitu saja: pada lapisan berikutnya yang konteksnya lebih luas, komponen dasar inilah yang menyusun informasi bentuk berskala lebih besar.

## Ide Utama

Setiap *patch* kedalaman didekomposisi menjadi dua bagian. Komponen dasar (*base-component*) adalah rata-rata nilai *patch*, yang menyatakan di mana *patch* itu berada relatif terhadap kamera. Komponen bentuk (*shape-component*) adalah sisa setelah rata-rata dikurangkan, yang menyatakan perubahan relatif kedalaman di dalam *patch*, yaitu bentuk geometrinya. Dua bobot terlatih yang terpisah — satu skalar untuk komponen dasar, satu matriks untuk komponen bentuk — menimbang ulang keduanya sebelum dijumlahkan kembali menjadi *patch* sadar-bentuk yang kemudian dikonvolusi seperti biasa. Dengan cara ini, jaringan belajar menekan atau menonjolkan informasi bentuk sesuai kebutuhan.

## Cara Kerja Langkah demi Langkah

### Dekomposisi Patch

Konvolusi standar menghitung F = Conv(K, P): setiap elemen keluaran adalah jumlah hasil kali elemen *patch* P (berukuran Kh×Kw×Cin; Kh dan Kw ukuran spasial *kernel*, Cin jumlah kanal masukan) dengan bobot *kernel* K yang bersesuaian. Karena perhitungan ini linear terhadap nilai *patch*, dua *patch* berbentuk sama yang seluruh nilainya berbeda satu meter menghasilkan fitur berbeda.

ShapeConv memecah P menjadi P_B = m(P), yaitu rata-rata seluruh nilai *patch* per kanal (berukuran 1×1×Cin), dan P_S = P − m(P), yaitu komponen bentuk yang berukuran sama dengan P. Contoh numerik: *patch* 2×2 bernilai [[2,0; 2,0]; [2,2; 2,4]] meter memiliki rata-rata 2,15, sehingga komponen dasarnya 2,15 dan komponen bentuknya [[−0,15; −0,15]; [+0,05; +0,25]]. *Patch* lain dengan bentuk sama pada jarak satu meter lebih jauh, [[3,0; 3,0]; [3,2; 3,4]], memiliki komponen bentuk yang persis sama — hanya komponen dasarnya berbeda. Pemisahan inilah sumber invariansi yang dicari.

### Dua Bobot Terpisah: Base-Product dan Shape-Product

Komponen dasar ditimbang oleh *base-kernel* W_B, satu skalar terlatih yang mengalikannya (operasi *base-product*). Komponen bentuk diproses oleh *shape-kernel* W_S, matriks terlatih berukuran (Kh×Kw)×(Kh×Kw) untuk setiap kanal masukan (operasi *shape-product*): setiap posisi keluaran merupakan kombinasi terboboti dari seluruh posisi komponen bentuk, sehingga pola relatif antarpiksel — bukan nilai absolut — yang dipetakan. Untuk *kernel* 3×3 dan 256 kanal masukan, W_S berisi 9×9×256, atau sekitar 20.700 bobot per lapisan. Kedua hasil penimbangan dijumlahkan elemen demi elemen menjadi *patch* sadar-bentuk P_BS yang berukuran sama dengan P, lalu keluaran lapisan dihitung sebagai F = Conv(K, P_BS).

### Ekivalensi Dua Rumusan

Menghitung dua operasi produk pada setiap *patch* menambah biaya pelatihan. Penulis membuktikan bahwa operasi yang sama dapat dipindahkan dari *patch* ke *kernel*: *kernel* K didekomposisi menjadi K_B = m(K) dan K_S = K − m(K), lalu digabung menjadi K_BS = W_B⋄K_B + W_S∗K_S. Berlaku Conv(K, P_BS) = Conv(K_BS, P); kedua rumusan identik secara matematis, tetapi rumusan *kernel* tidak mengubah data masukan. Implementasi resmi memakai rumusan kedua ini.

### Inisialisasi Identitas dan Fusi Saat Inferensi

W_B diinisialisasi 1 dan W_S diinisialisasi matriks identitas, sehingga pada awal pelatihan berlaku K_BS = K: ShapeConv persis merupakan konvolusi biasa. Inisialisasi ini memberi dua keuntungan: fitur RGB diproses sama seperti jaringan asalnya, dan bobot pralatih ImageNet dapat dipakai ulang apa adanya. Setelah pelatihan, W_B dan W_S menjadi konstanta dan dilebur permanen ke dalam K_BS, yang berukuran persis sama dengan K. Jaringan inferensi yang dihasilkan identik dengan jaringan konvolusi biasa; tambahan waktu komputasi dan memori saat inferensi adalah nol.

### Penempatan dalam Jaringan Segmentasi

ShapeConv menggantikan seluruh lapisan konvolusi, baik pada *backbone* (jaringan pengekstrak fitur, misalnya ResNet) maupun pada tahap segmentasi. Masukan jaringan adalah penggabungan kanal RGB dengan kanal kedalaman; kedalaman dapat berupa nilai mentah atau pengkodean HHA — tiga kanal turunan kedalaman yang terdiri atas disparitas horizontal, tinggi di atas lantai, dan sudut normal permukaan terhadap sumbu vertikal (diperkenalkan Gupta dkk. 2014). Alur pemrosesan satu *patch* pada satu lapisan:

```
        patch kedalaman P (Kh x Kw x Cin)
        |
        +-------------------+--------------------+
        v                   v                    |
  P_B = rata-rata(P)   P_S = P - rata-rata(P)    |
  (1x1xCin)            (Kh x Kw x Cin)           |
  "di mana"            "bentuk apa"              |
        |                   |                    |
        v                   v                    |
  base-product         shape-product             |
  W_B . P_B            W_S * P_S                 |
  (1 skalar terlatih)  (matriks terlatih)        |
        |                   |                    |
        +------->(+)--------+                    |
                  v                              |
        patch sadar-bentuk P_BS                  |
                  v                              |
        F = Conv(K, P_BS)                        |
                                                 |
  inferensi: W_B, W_S konstan, dilebur ke kernel |
  K_BS = W_B.K_B + W_S*K_S  ->  F = Conv(K_BS, P)|
  (jaringan identik konvolusi biasa, biaya +0)   |
```

Satu-satunya perbedaan terhadap konvolusi biasa terletak pada cabang dekomposisi dan penimbangan; cabang itu hilang saat inferensi karena bobotnya menyatu ke dalam *kernel*.

## Eksperimen dan Hasil

Pengujian dilakukan pada tiga *benchmark* segmentasi dalam-ruang. NYUDv2 memuat 1.449 citra RGB-D (795 latih, 654 uji) dengan dua pengaturan: 13 kelas dan 40 kelas. SUN RGB-D memuat 10.355 citra dari 37 kelas (5.285 latih, 5.050 uji). SID (*Stanford Indoor Dataset*) jauh lebih besar, yaitu 70.496 citra dari 13 kelas, dengan pengujian pada area gedung yang tidak muncul saat pelatihan. Metrik yang dilaporkan mencakup akurasi piksel, akurasi rata-rata kelas, mean IoU (mIoU — rata-rata rasio irisan terhadap gabungan per kelas, metrik utama segmentasi), dan *frequency-weighted* IoU. *Baseline* dan versi ShapeConv hanya berbeda pada lapisan konvolusinya; seluruh pengaturan lain sama, sehingga selisih kinerja murni berasal dari ShapeConv.

Hasil mIoU utama (pengujian skala tunggal, arsitektur DeepLabv3+):

| Dataset | *Backbone* | *Baseline* | +ShapeConv | Selisih |
|---|---|---|---|---|
| NYUDv2-13 | ResNeXt-101 | 63,2 | 65,1 | +1,9 |
| NYUDv2-40 | ResNet-101 | 45,9 | 47,4 | +1,5 |
| SUN RGB-D | ResNet-101 | 46,9 | 47,6 | +0,7 |
| SID | ResNet-101 | 54,6 | 60,6 | +6,0 |

Lonjakan terbesar pada SID (+6,0 poin mIoU, akurasi piksel 78,7 menjadi 82,7) konsisten dengan ukuran datasetnya yang puluhan kali lebih besar: W_S memuat banyak bobot, dan 70 ribu citra menyediakan cukup data untuk mempelajarinya. Sebaliknya, kenaikan pada SUN RGB-D hanya +0,7 poin, menunjukkan manfaat yang bergantung pada karakteristik dataset.

Terhadap metode lain pada NYUDv2-40 dengan pengujian multi-skala (citra diuji pada beberapa skala lalu hasilnya digabung), ShapeConv mencapai 51,3% mIoU, di atas SGNet (51,1), konvolusi 2,5D *malleable* (50,9), RDFNet (50,1), dan ACNet (48,3). Pada NYUDv2-13, skornya 65,6 dibandingkan 59,3 milik PVNet, selisih 6,3 poin. Uji generalisasi pada lima arsitektur — DeepLabv3+, DeepLabv3, UNet, PSPNet, dan FPN — dengan *backbone* ResNet-50/101 pada NYUDv2-40 menunjukkan kenaikan mIoU 1,2 hingga 2,3 poin pada seluruh sepuluh kombinasi, membuktikan sifat *plug-and-play* (dapat disisipkan tanpa mengubah arsitektur).

Pada ablasi NYUDv2-40, tanpa kedua bobot (konvolusi biasa) mIoU 45,9; hanya W_B menghasilkan 47,0; hanya W_S menghasilkan 46,3; keduanya bersama menghasilkan 47,4. Kedua bobot terbukti saling melengkapi, dan W_B yang hanya satu skalar memberi sumbangan terbesar sendirian. Masukan HHA mengungguli kedalaman mentah (47,4 berbanding 46,2 dengan ShapeConv). Analisis *trimap* — penghitungan piksel salah-kelas dalam pita sempit di sekitar batas objek, mengikuti metode Kohli dkk. — menunjukkan ShapeConv unggul pada semua lebar pita, artinya perbaikannya terkonsentrasi pada tepi objek, sesuai tujuan pemodelan bentuk.

## Kelebihan dan Keterbatasan

Kelebihan utama ShapeConv adalah biaya inferensi nol: seluruh mekanisme tambahan menyatu ke dalam *kernel* setelah pelatihan, sehingga tidak ada penalti kecepatan maupun memori saat model dipakai. Sifatnya yang *model-agnostic* memungkinkannya menggantikan konvolusi pada hampir semua CNN, dan inisialisasi identitas membuat bobot pralatih tetap dapat dipakai apa adanya.

Keterbatasannya, penulis sendiri menyatakan bahwa dekomposisi berbasis rata-rata hanya menangani perbedaan translasi kedalaman; transformasi rotasi akibat sudut pandang kamera tidak teratasi. Dari sisi rekayasa, W_S menambah sekitar 20.700 parameter per lapisan 3×3 berkanal 256, sehingga biaya pelatihan dan kebutuhan data naik — gejala ini terlihat dari kecilnya peningkatan pada dataset yang lebih kecil. Secara konseptual, manfaatnya bergantung pada kualitas peta kedalaman dan, untuk hasil terbaik, pada prapemrosesan HHA; selain itu penerapannya menuntut pelatihan ulang jaringan secara penuh, bukan penyetelan ringan.

## Kaitan dengan Bab Lain

ShapeConv mengambil arah berlawanan dari jalur fusi dua cabang pada bab-bab sebelumnya. [FuseNet](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md) (bab 051), [RDFNet](./053%20-%202017%20-%20RDFNet%20-%20Segmentasi%20RGB-D.md) (bab 053), dan [ACNet](./054%20-%202019%20-%20ACNet%20-%20Segmentasi%20RGB-D.md) menggabungkan fitur dua modalitas melalui arsitektur; ShapeConv justru menggabungkan masukan sejak awal lalu memodifikasi operator konvolusinya — dan pada NYUDv2-40 dilaporkan melampaui RDFNet (50,1 berbanding 51,3) serta ACNet (48,3). Ia seangkatan dengan [ESANet](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md) (bab 056), yang juga terbit 2021 tetapi mengejar efisiensi lewat arsitektur ringan. Gagasan memanfaatkan perbedaan sifat RGB dan kedalaman kemudian dilanjutkan pada arsitektur *transformer* oleh [CMX](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md) (bab 058), yang menukar fusi konvolusi dengan mekanisme *cross-attention* antarmodalitas.

## Poin untuk Sitasi

Kunci BibTeX: `cao2021shapeconv`. Ringkasan aman kutip: ShapeConv (Cao dkk., ICCV 2021) adalah lapisan konvolusi untuk fitur kedalaman yang mendekomposisi *patch* menjadi komponen dasar (rata-rata) dan komponen bentuk (residu), menimbang keduanya dengan bobot terlatih terpisah, lalu menggabungkannya kembali sebelum konvolusi. Bobot tersebut dapat dilebur ke *kernel* saat inferensi sehingga tidak menambah komputasi, dan penggantian konvolusi biasa dengan ShapeConv menaikkan mIoU pada NYUDv2, SUN RGB-D, dan SID lintas lima arsitektur segmentasi.

Catatan verifikasi sebelum sitasi formal: seluruh angka pada bab ini diambil dari arXiv v1 (Agustus 2021) dan README repositori resmi; cocokkan dengan versi kamera-siap ICCV 2021 (hal. 7088–7097) karena angka tabel dapat berbeda tipis antarversi. Klaim "biaya inferensi nol" hanya berlaku setelah fusi bobot — pada fase pelatihan tetap ada tambahan parameter dan komputasi. Klaim analisis *trimap* bersifat grafis (kurva pada Gambar 5 makalah), tanpa tabel angka.
