# 180 - GDR-Net: Geometry-Guided Direct Regression Network for Monocular 6D Object Pose Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2021gdrnet` |
| Judul asli | GDR-Net: Geometry-Guided Direct Regression Network for Monocular 6D Object Pose Estimation |
| Penulis | Gu Wang, Fabian Manhardt, Federico Tombari, Xiangyang Ji |
| Tahun | 2021 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2021) |
| Tema | Pose 6D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2102.12145
- **Google Scholar:** https://scholar.google.com/scholar?q=GDR-Net%3A%20Geometry-Guided%20Direct%20Regression%20Network%20for%20Monocular%206D%20Object%20Pose%20Estimation
- **Kode sumber resmi:** https://github.com/THU-DA-6D-Pose-Group/GDR-Net

## Gambaran Umum

GDR-Net (*Geometry-Guided Direct Regression Network*) adalah metode estimasi pose 6D (tiga parameter translasi dan tiga parameter rotasi objek relatif terhadap kamera) dari satu citra RGB tunggal, tanpa memerlukan data kedalaman (*depth*). Makalah ini memecahkan konflik antara dua keluarga metode: metode berbasis korespondensi geometris yang akurat tetapi tidak dapat dilatih *end-to-end* (dari masukan ke keluaran dalam satu proses pelatihan tanpa tahap terpisah), dan metode regresi langsung yang dapat dilatih *end-to-end* tetapi kurang akurat. GDR-Net menggabungkan keduanya: jaringan memprediksi peta korespondensi geometris antara (representasi 2D-3D dense) dari RoI (*Region of Interest*, wilayah citra yang memuat objek) yang telah di-*zoom-in*, kemudian sebuah modul bernama Patch-PnP meregresi pose 6D langsung dari peta tersebut secara *differentiable* (dapat diturunkan gradiennya). Pada evaluasi di dataset LineMOD (LM), LineMOD-Occlusion (LM-O), dan YCB-Video (YCB-V), GDR-Net dilaporkan mengungguli metode-metode RGB-only sebelumnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum GDR-Net, metode estimasi pose 6D dari RGB tunggal dengan performa terbaik memakai strategi tak langsung (*indirect*): jaringan terlebih dahulu memprediksi korespondensi 2D-3D — pasangan antara titik pada bidang citra dan titik pada sistem koordinat objek — kemudian pose dihitung dari korespondensi itu memakai algoritme PnP (*Perspective-n-Point*, metode geometris untuk menghitung pose kamera dari sejumlah pasangan titik 2D-3D yang diketahui) yang biasanya dikombinasikan dengan RANSAC (*Random Sample Consensus*, teknik penyaringan iteratif untuk membuang korespondensi yang salah/*outlier*). Metode seperti PVNet (memvoting lokasi *keypoint* dari peta arah piksel) dan DPOD (memprediksi peta korespondensi objek dense) termasuk kelompok ini.

Masalah utamanya adalah tahap PnP/RANSAC tersebut tidak dapat diturunkan gradiennya, sehingga jaringan dan solver pose dilatih terpisah: jaringan dioptimalkan untuk memprediksi korespondensi yang akurat, bukan langsung untuk pose yang akurat, dan gradien galat pose tidak dapat mengalir balik ke pelatihan jaringan. Ini menyulitkan sistem yang membutuhkan pose *differentiable*, misalnya jaringan yang menggabungkan estimasi pose dengan tugas hilir lain dalam satu pelatihan menyeluruh.

Kelompok metode lain, regresi langsung, memprediksi pose secara langsung dari fitur citra tanpa representasi geometris perantara — misalnya PoseCNN yang meregresi rotasi dan translasi langsung dari fitur CNN. Pendekatan ini dapat dilatih penuh secara *end-to-end*, tetapi akurasinya di bawah metode berbasis korespondensi karena tidak memanfaatkan struktur geometris eksplisit objek. Makalah ini berangkat dari pengamatan bahwa kedua kelompok metode memiliki kelebihan yang saling melengkapi, dan mempertanyakan apakah keduanya dapat disatukan dalam satu jaringan yang tetap *end-to-end*.

## Ide Utama

Gagasan inti GDR-Net adalah memisahkan proses estimasi pose menjadi dua tahap yang tetap terhubung secara *differentiable*. Tahap pertama memprediksi representasi geometris perantara dense (nilai per piksel, bukan sekumpulan titik jarang) berupa peta korespondensi 2D-3D beserta informasi bantu terkait. Tahap kedua adalah modul regresi kecil, Patch-PnP, yang membaca peta-peta tersebut dan langsung mengeluarkan pose 6D — menggantikan solver PnP/RANSAC klasik dengan jaringan saraf yang dapat dilatih bersama tahap pertama memakai *backpropagation* (algoritme perambatan gradien balik standar pada pelatihan jaringan saraf).

Dengan susunan ini, jaringan tetap memanfaatkan struktur geometris eksplisit — sama seperti metode berbasis korespondensi — tetapi seluruh proses, dari citra masukan hingga pose keluaran, dapat dioptimalkan sebagai satu fungsi tunggal. Galat pose akhir dapat langsung memberi sinyal koreksi ke prediksi peta korespondensi, sesuatu yang tidak mungkin dilakukan ketika PnP/RANSAC dipakai sebagai solver terpisah di luar jaringan.

## Cara Kerja Langkah demi Langkah

### Deteksi dan Dynamic Zoom-In

GDR-Net tidak melakukan deteksi objek sendiri; ia menerima kotak deteksi dari detektor luar (mis. Faster R-CNN atau YOLOv3, tergantung *setup* percobaan), lalu memotong wilayah tersebut menjadi RoI. Selama pelatihan, prosedur *Dynamic Zoom-In* menambah variasi posisi dan skala RoI secara acak di sekitar kotak kebenaran (*ground truth*), sehingga jaringan tidak bergantung pada karakteristik detektor tertentu dan lebih tahan terhadap kotak deteksi yang kurang presisi saat pengujian.

### Prediksi Peta Geometris Dense

RoI yang telah di-*zoom-in* dilewatkan ke jaringan konvolusi (dibangun di atas arsitektur yang serupa dengan CDPN, metode korespondensi dense sebelumnya) yang mengeluarkan tiga peta beresolusi spasial 64×64:

1. **Peta korespondensi 2D-3D dense (M2D-3D).** Untuk tiap piksel dalam RoI yang termasuk objek, peta ini memberi koordinat 3D pada sistem koordinat objek yang berkorespondensi dengan piksel itu — perluasan dense dari korespondensi jarang yang dipakai PVNet/DPOD.
2. **Peta atensi wilayah permukaan (surface region attention, MSRA).** Permukaan objek dibagi menjadi sejumlah wilayah (*region*) berdasarkan pembagian model 3D-nya; peta ini memberi distribusi probabilitas per piksel atas wilayah-wilayah tersebut. Peta ini berguna terutama untuk objek simetris, karena mengurangi ambiguitas korespondensi ketika beberapa bagian permukaan terlihat identik dari satu sudut pandang.
3. **Mask objek tampak (Mvis).** Peta biner yang menandai piksel dalam RoI yang benar-benar merupakan bagian objek yang terlihat (tidak terhalang objek lain).

### Patch-PnP: Regresi Pose yang Dapat Dilatih

Ketiga peta di atas ditumpuk sebagai kanal masukan bagi Patch-PnP, sebuah jaringan konvolusi kecil yang langsung meregresi enam parameter pose: rotasi (direpresentasikan dalam bentuk yang kontinu secara numerik, bukan kuaternion langsung, untuk menghindari diskontinuitas saat pelatihan) dan translasi. Berbeda dari PnP/RANSAC klasik yang mengiterasi mencari solusi geometris optimal di luar jaringan, Patch-Pnp adalah fungsi *feed-forward* murni sehingga waktu inferensinya konstan dan gradiennya dapat dirambatkan balik ke tahap prediksi peta geometris. Translasi diregresi memakai parameterisasi *disentangled* — komponen kedalaman (*depth*) dipisahkan dari komponen posisi pada bidang citra — supaya galat pada satu komponen tidak mendominasi galat komponen lain selama pelatihan.

Alur data dari citra hingga pose dapat diringkas sebagai berikut.

```
citra RGB + kotak deteksi
        |
   Dynamic Zoom-In -> RoI (mis. 256x256)
        |
   backbone konvolusi (mirip CDPN)
        |
   tiga peta 64x64:
     M2D-3D (korespondensi)  MSRA (region)  Mvis (mask)
        |
   Patch-PnP (jaringan feed-forward kecil)
        |
   pose 6D: rotasi R, translasi t
```

### Fungsi Loss dan Pelatihan

Pelatihan memakai kombinasi loss pada peta-peta perantara (galat prediksi korespondensi, region, dan mask terhadap label yang dirender dari model CAD objek) dan loss langsung pada pose keluaran Patch-PnP. Karena seluruh alur bersifat *differentiable*, kedua jenis loss ini dioptimalkan bersamaan dalam satu proses pelatihan, bukan dalam dua tahap terpisah. Label peta geometris diperoleh dengan me-*render* model 3D objek pada pose kebenaran, sehingga pelatihan memerlukan model CAD atau rekonstruksi 3D objek yang diketahui.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tiga dataset standar estimasi pose 6D. LineMOD (LM) berisi 13 objek tunggal dengan latar relatif bersih. LineMOD-Occlusion (LM-O) memakai subset citra dari LM yang sama tetapi dengan banyak objek saling menutupi sebagian (oklusi), sehingga lebih menantang. YCB-Video (YCB-V) berisi 21 objek rumah tangga dalam adegan meja yang berantakan dengan variasi pencahayaan dan oklusi. Metrik utama adalah ADD(-S): rata-rata jarak titik permukaan model 3D antara pose prediksi dan pose kebenaran, dengan varian ADD-S (memakai jarak titik terdekat, bukan titik berpasangan) khusus dipakai untuk objek simetris karena pose simetris berbeda dapat menghasilkan permukaan yang identik secara visual.

Berdasarkan tabel hasil pada makalah, GDR-Net dilaporkan mencapai recall ADD(-S) rata-rata sekitar 62,2% pada LM-O, mengungguli PVNet yang mencapai sekitar 40,8% pada metrik yang sama — selisih lebih dari 20 poin persentase yang menunjukkan manfaat menggabungkan representasi geometris dense dengan regresi pose yang dapat dilatih penuh. Pada YCB-V, makalah melaporkan GDR-Net unggul dibandingkan metode RGB-only sebelumnya seperti PoseCNN dan CDPN pada metrik AUC (*Area Under Curve*) dari ADD-S dan ADD(-S). Angka-angka LM-O di atas diperoleh dari sumber sekunder yang merujuk tabel makalah, bukan dari pembacaan langsung tabel asli, sehingga wajib diverifikasi ulang ke naskah sebelum dikutip secara formal (lihat bagian *Poin untuk Sitasi*).

Selain perbandingan lintas metode, makalah menyertakan uji ablasi yang membandingkan Patch-PnP dengan varian PnP lain (RANSAC/EPnP klasik dan metode PnP berbasis pembelajaran lain) pada data sintetis berbentuk bola, menunjukkan Patch-PnP memberi kombinasi akurasi dan kecepatan yang lebih baik dalam pengaturan terkendali tersebut.

## Kelebihan dan Keterbatasan

Kelebihan GDR-Net terletak pada penyatuan dua paradigma yang sebelumnya terpisah: akurasi dari representasi geometris dense dan kemampuan pelatihan *end-to-end* dari regresi langsung. Karena Patch-PnP adalah jaringan *feed-forward*, waktu inferensinya konstan dan dapat diprediksi, berbeda dari RANSAC yang jumlah iterasinya bervariasi tergantung kualitas data. Peta atensi wilayah permukaan juga memberi mekanisme eksplisit untuk menangani objek simetris, sebuah sumber kesalahan umum pada metode pose 6D lain.

Dari sisi rekayasa, GDR-Net tetap bergantung pada model CAD objek atau data geometris permukaan yang diketahui untuk menghasilkan label peta korespondensi saat pelatihan, sehingga metode ini kurang langsung diterapkan pada objek baru tanpa model 3D siap pakai. Secara konseptual, performa sistem juga bergantung pada kualitas kotak deteksi dari detektor eksternal tahap awal — meskipun Dynamic Zoom-In mengurangi sensitivitas ini saat pelatihan, kesalahan deteksi besar pada saat pengujian tetap dapat menurunkan akurasi pose akhir. Objek dengan simetri kompleks atau oklusi berat, meskipun ditangani lebih baik dibandingkan metode sebelumnya, tetap menjadi kasus yang lebih sulit dibandingkan objek tunggal tanpa halangan.

## Kaitan dengan Bab Lain

GDR-Net berada pada klaster Pose 6D bersama [181 - ZebraPose](./181%20-%202022%20-%20ZebraPose%20-%20Pose%206D.md) dan [182 - OnePose](./182%20-%202022%20-%20OnePose%20-%20Pose%206D.md). ZebraPose melanjutkan gagasan representasi korespondensi dense GDR-Net dengan pengkodean permukaan berjenjang yang lebih presisi, sedangkan tahap regresi pose *differentiable* yang diperkenalkan GDR-Net melalui Patch-PnP menjadi rujukan bagi metode pose lanjutan yang ingin menghindari solver PnP/RANSAC klasik. OnePose, sebaliknya, mengangkat masalah berbeda: estimasi pose tanpa model CAD sama sekali, sesuatu yang menjadi keterbatasan eksplisit GDR-Net karena metode ini memerlukan model 3D objek untuk pelatihan. GDR-Net juga bergantung pada detektor objek RGB tahap awal untuk menghasilkan kotak wilayah objek, sehingga secara tidak langsung mewarisi kualitas dari bab-bab fondasi deteksi objek RGB pada klaster awal tinjauan ini.

## Poin untuk Sitasi

Kutip dengan kunci `wang2021gdrnet`. Ringkasan yang aman dikutip: "GDR-Net menyatukan estimasi pose 6D berbasis korespondensi geometris dense dengan regresi langsung yang dapat dilatih *end-to-end*, memakai modul Patch-PnP sebagai pengganti PnP/RANSAC klasik yang tidak *differentiable*, dan dievaluasi pada dataset LineMOD, LineMOD-Occlusion, dan YCB-Video dengan metrik ADD(-S)." Angka recall ADD(-S) sekitar 62,2% pada LM-O dan perbandingan sekitar 40,8% untuk PVNet diperoleh dari ringkasan sumber sekunder (hasil pencarian web atas isi tabel makalah), bukan dari pembacaan langsung tabel PDF asli — angka ini wajib diverifikasi ke Tabel 2 dan Tabel 3 pada naskah CVPR/arXiv (2102.12145) sebelum dikutip dalam karya formal. Angka hasil pada YCB-V (AUC ADD-S/ADD(-S)) belum terverifikasi secara numerik dan tidak dicantumkan di badan bab ini karena alasan yang sama.
