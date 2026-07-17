# 012 - Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `girshick2014rcnn` |
| Judul asli | Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation |
| Penulis | Ross Girshick, Jeff Donahue, Trevor Darrell, Jitendra Malik |
| Tahun | 2014 |
| Venue | IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2014) |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis, versi tech report v5):** https://arxiv.org/abs/1311.2524
- **Google Scholar:** https://scholar.google.com/scholar?q=Rich%20Feature%20Hierarchies%20for%20Accurate%20Object%20Detection%20and%20Semantic%20Segmentation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Rich%20Feature%20Hierarchies%20for%20Accurate%20Object%20Detection%20and%20Semantic%20Segmentation&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan R-CNN (*Regions with CNN features*), detektor objek pertama yang menunjukkan secara telak bahwa fitur jaringan saraf konvolusi (CNN) mengungguli fitur rancangan tangan untuk deteksi objek. Sistemnya bekerja tiga tahap: sekitar 2.000 kandidat wilayah dihasilkan oleh *selective search*, setiap wilayah diekstrak fiturnya oleh CNN, diklasifikasikan oleh SVM linear per kelas, lalu posisi kotak dikoreksi sebuah regresor. Pada PASCAL VOC 2012, R-CNN mencapai 53,3% mAP, yaitu perbaikan relatif lebih dari 30% terhadap hasil terbaik sebelumnya.

Kontribusi kedua bersifat metodologis: saat data deteksi terbatas, CNN dilatih dengan pra-latih terbimbing pada klasifikasi ILSVRC yang berlimpah data, lalu disetel halus untuk deteksi. Paradigma dan arsitektur tiga tahap ini menjadi titik awal keluarga detektor dua tahap yang dirujuk hampir semua bab lain.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi objek adalah tugas menemukan posisi semua objek dalam citra — dinyatakan sebagai *bounding box* (kotak pembatas berisi koordinat dan ukuran objek) — sekaligus menentukan kelas setiap objek. Pada rentang 2010–2012, akurasi deteksi pada tolok ukur standar PASCAL VOC praktis stagnan. Metode terbaik saat itu berupa sistem *ensemble* (gabungan banyak komponen) yang memadukan fitur rancangan tangan, terutama SIFT dan HOG (*Histogram of Oriented Gradients*: histogram arah gradien intensitas pada blok-blok kecil citra), dengan konteks tingkat tinggi. Detektor yang paling banyak dipakai adalah DPM (*Deformable Part Model*), yang memandang objek sebagai susunan bagian-bagian yang dapat bergeser relatif satu sama lain dan dievaluasi dengan pola *sliding window*: pengklasifikasi dijalankan berulang pada jendela-jendela yang digeser menutupi seluruh citra pada beberapa skala.

Tahun 2012, CNN bernama AlexNet memenangkan kompetisi klasifikasi ImageNet setelah dilatih pada 1,2 juta citra berlabel. Keberhasilan itu memunculkan pertanyaan terbuka: seberapa jauh akurasi klasifikasi CNN dapat dialihkan ke deteksi objek? Dua halangan teknis muncul. Pertama, unit lapis atas AlexNet memiliki *receptive field* (wilayah masukan yang memengaruhi satu unit) 195×195 piksel dengan *stride* (jarak langkah antar-unit) 32×32 piksel, sehingga lokalisasi presisi dalam paradigma *sliding window* sulit. Kedua, data deteksi berlabel kotak terlalu sedikit untuk melatih CNN besar dari nol.

## Ide Utama

Gagasan inti R-CNN terdiri atas dua bagian. Bagian pertama: jangan jalankan CNN sebagai *sliding window*; jalankan CNN pada *region proposal* — kandidat wilayah citra yang berpeluang memuat objek, dihasilkan oleh algoritme bawah-atas tanpa mengetahui kelas objeknya. Dengan cara ini, masalah lokalisasi diserahkan kepada pengusul wilayah, dan CNN cukup mengenali isi setiap wilayah. Masukan sistem satu citra; keluarannya daftar kotak objek, kelas, dan skor; yang berubah dari pendekatan sebelumnya adalah fitur HOG digantikan fitur CNN yang dipelajari dari data.

Bagian kedua: atasi kelangkaan data deteksi dengan *transfer learning*. CNN dilatih terlebih dahulu secara terbimbing untuk klasifikasi citra pada data ILSVRC yang melimpah, lalu bobotnya disetel halus (*fine-tuning*) — dilatih lanjut dengan laju pembelajaran kecil — pada data deteksi yang sedikit.

## Cara Kerja Langkah demi Langkah

Sistem R-CNN terdiri atas tiga modul: pengusul wilayah, CNN pengekstrak fitur, dan himpunan SVM per kelas, ditambah satu regresor koreksi kotak. Alur datanya:

```
citra masukan
     │
     ▼
┌──────────────────────┐
│ selective search     │  ±2.000 proposal wilayah per citra,
│ (mode "fast")        │  independen terhadap kelas objek
└──────────────────────┘
     │ ±2.000 kotak kandidat
     ▼
┌──────────────────────┐
│ warping ke 227x227   │  setiap wilayah diregangkan ke ukuran
│ + konteks 16 piksel  │  tetap masukan CNN
└──────────────────────┘
     │
     ▼
┌──────────────────────┐
│ CNN (AlexNet)        │  5 lapis konvolusi + 2 lapis fully
│ 2.000 kali forward   │  connected -> fitur fc7: 4.096 dimensi
└──────────────────────┘
     │ matriks fitur 2.000 x 4.096
     ▼
┌──────────────────────┐
│ SVM linear per kelas │  matriks bobot 4.096 x N (N = jumlah
│ + NMS per kelas      │  kelas); NMS merampingkan kotak ganda
└──────────────────────┘
     │
     ▼
┌──────────────────────┐
│ regresi bounding box │  koreksi posisi kotak dari fitur pool5
└──────────────────────┘
     │
     ▼
deteksi akhir: kotak + kelas + skor
```

### Tahap 1: Pengusulan Wilayah dengan Selective Search

*Selective search* adalah algoritme segmentasi hierarkis: piksel citra dikelompokkan berangsur-angsur berdasarkan kemiripan warna, tekstur, ukuran, dan kesesuaian bentuk antar wilayah, lalu kotak pembatas diambil dari wilayah hasil pengelompokan pada semua tingkatan. Hasilnya sekitar 2.000 proposal per citra (mode "fast"). R-CNN bebas memakai pengusul wilayah apa pun; selective search dipilih agar perbandingan dengan pendahulu berproposal sama berlangsung adil.

### Tahap 2: Warping dan Ekstraksi Fitur CNN

CNN yang dipakai (implementasi Caffe dari AlexNet: lima lapis konvolusi diikuti dua lapis *fully connected* — lapis yang setiap unitnya terhubung ke seluruh unit sebelumnya) menuntut masukan tetap 227×227 piksel, sedangkan proposal berbentuk sembarang persegi panjang. Solusinya adalah *warping*: seluruh piksel dalam kotak pembatas proposal diregangkan anisotropik (skala horizontal dan vertikal boleh berbeda) menjadi 227×227. Sebelum diregangkan, kotak diperlebar dahulu sehingga tersisa konteks 16 piksel di sekeliling objek. Sebagai contoh, proposal berukuran 300×80 piksel dipaksa menjadi citra persegi 227×227, sehingga rasio aspeknya berubah. Setiap citra hasil warping dilewatkan ke CNN, dan keluaran lapis fc7 (lapis *fully connected* terakhir) diambil sebagai vektor fitur 4.096 dimensi per wilayah.

### Tahap 3: Klasifikasi SVM dan NMS

Fitur setiap wilayah dinilai oleh satu SVM (*support vector machine*: pengklasifikasi linear yang mencari bidang pemisah dengan margin selebar mungkin) biner per kelas — 20 SVM untuk PASCAL VOC. Karena bobot CNN dipakai bersama semua kelas, satu-satunya komputasi spesifik kelas adalah perkalian matriks fitur 2.000×4.096 dengan bobot SVM 4.096×N. Setelah semua wilayah berskor, *Non-Maximum Suppression* (NMS) dijalankan per kelas: dari sekumpulan kotak yang saling tumpang tindih, hanya kotak berskor tertinggi yang dipertahankan, dan kotak lain dibuang bila IoU-nya (*Intersection over Union*: rasio luas irisan terhadap luas gabungan dua kotak) melebihi ambang.

### Tahap 4: Regresi Bounding Box

Analisis galat pada makalah menunjukkan bahwa kesalahan dominan R-CNN adalah mislokalisasi (kotak kurang tepat posisinya), bukan salah kelas. Untuk memperbaikinya, sebuah model regresi linear per kelas dilatih memprediksi jendela deteksi baru dari fitur pool5 proposal — pool5 adalah keluaran lapis konvolusi kelima setelah penggabungan maksimum (*max-pooling*), berukuran 6×6×256 = 9.216 dimensi.

### Pelatihan: Pra-latih, Penyetelan Halus, dan SVM

Mula-mula CNN dilatih untuk klasifikasi pada ILSVRC2012 (1.000 kelas, tanpa label kotak). Untuk penyetelan halus ke deteksi, lapis klasifikasi 1.000 arah diganti lapis (N+1) arah — N kelas objek ditambah satu kelas latar belakang — lalu pelatihan dilanjutkan hanya pada proposal hasil warping. Proposal dengan IoU ≥ 0,5 terhadap kotak *ground truth* (anotasi kebenaran) dianggap positif, sisanya negatif. Setiap *mini-batch* berisi 128 jendela: 32 positif dan 96 latar, dengan laju pembelajaran 0,001. Untuk ILSVRC2013, penyetelan halus berjalan 50.000 iterasi selama 13 jam pada satu GPU NVIDIA Tesla K20. Terakhir, SVM per kelas dilatih dengan definisi label berbeda: kotak *ground truth* menjadi contoh positif, sedangkan proposal dengan IoU di bawah 0,3 menjadi negatif — ambang 0,3 hasil pencarian grid ini penting, karena ambang 0,5 menurunkan mAP sekitar 5 poin. Pelatihannya memakai *hard negative mining*: contoh negatif yang paling sulit diklasifikasikan ditambang berulang untuk memperbarui pemisah.

## Eksperimen dan Hasil

Evaluasi dilakukan pada PASCAL VOC 2007/2010/2012 (20 kelas) dan ILSVRC2013 detection (200 kelas), dengan metrik mAP (*mean Average Precision*: rata-rata presisi pada berbagai tingkat *recall*, dirata-ratakan lintas kelas; maksimal 100%). Pada VOC 2010, R-CNN memperoleh 53,7% mAP. Pembanding paling adil adalah sistem UVA, yang memakai proposal selective search identik tetapi fitur SIFT berpiramida: 35,1% — selisih 18,6 poin pada proposal yang sama membuktikan peningkatan berasal dari fitur CNN. DPM hanya mencapai 33,4%. Pada VOC 2012, R-CNN mencapai 53,3% mAP — perbaikan relatif lebih dari 30% atas hasil terbaik sebelumnya.

Ablasi pada VOC 2007: penyetelan halus menambah 8,0 poin mAP menjadi 54,2% — representasi pra-latih ImageNet bersifat umum, dan adaptasi domain memberi lompatan besar. Regresi *bounding box* menambah 3–4 poin menjadi 58,5%; dibandingkan DPM berbasis HOG (33,7%), ini setara perbaikan relatif 61%. Versi lanjutan laporan menguji arsitektur VGG-16 (16 lapis): mAP naik menjadi 66,0%, tetapi *forward pass*-nya tujuh kali lebih lambat.

Pada ILSVRC2013, R-CNN mencapai 31,4% mAP, jauh di atas OverFeat (detektor CNN berbasis *sliding window*) dengan 24,3%. Rantai ablasinya: tanpa penyetelan halus dengan data validasi terbatas, 20,9%; menambah data positif menjadi 24,1%; penyetelan halus pada data terbatas 26,5%; penyetelan halus dengan data diperluas 29,7%; regresi kotak menutupnya menjadi 31,0%. Selisih 7 poin ini menunjukkan paradigma proposal-plus-klasifikasi lebih efektif untuk lokalisasi, sekalipun OverFeat sembilan kali lebih cepat (2 detik per citra). Kelemahan terukurnya: *recall* proposal selective search (proporsi kotak kebenaran yang tertutup proposal pada IoU 0,5) hanya 91,6% pada ILSVRC versus sekitar 98% pada PASCAL — tahap proposal menjadi plafon akurasi.

Untuk segmentasi semantik, fitur R-CNN mencapai akurasi rata-rata 47,9% pada VOC 2011 test, sebanding dengan sistem O2P yang memimpin tolok ukur. Kecepatan deteksi: 13 detik per citra pada GPU atau 53 detik pada CPU untuk proposal dan ekstraksi fitur — jauh dari *real-time*.

## Kelebihan dan Keterbatasan

Kelebihan R-CNN: (1) lompatan akurasi sangat besar terhadap fitur rancangan tangan, dibuktikan oleh perbandingan dengan proposal identik; (2) fitur 4.096 dimensi dipakai bersama semua kelas dan jauh lebih ringkas daripada fitur wilayah sebelumnya (360.000 dimensi pada sistem UVA), sehingga penambahan kelas hanya menambah kolom bobot SVM; (3) paradigma pra-latih terbimbing plus penyetelan halus menjawab kelangkaan data dan berlaku umum ke tugas visi lain.

Keterbatasannya: (1) lambat, karena sekitar 2.000 *forward pass* CNN per citra tanpa berbagi komputasi; dari sisi rekayasa, kecepatan ini menutup pemakaian waktu nyata; (2) pelatihan multi-tahap — CNN, SVM, dan regresor kotak dilatih terpisah dengan definisi label berbeda-beda, sehingga tidak dioptimalkan menyeluruh; (3) dari sisi rekayasa, fitur 2.000×4.096 per citra harus disimpan ke diska untuk melatih SVM dan regresor, menuntut ruang penyimpanan besar; (4) secara konseptual, tahap proposal tidak dipelajari dari data: selective search tetap algoritme rancangan tangan yang lambat dan *recall*-nya membatasi akurasi akhir; (5) warping mengubah rasio aspek objek, distorsi yang dianalisis penulis pada lampiran makalah.

## Kaitan dengan Bab Lain

Bab ini titik awal silsilah detektor dua tahap, sehingga tidak ada bab pendahulu dalam garis keturunannya; warisannya terlihat pada bab-bab sesudahnya. Bab 013 ([Fast R-CNN](./013%20-%202015%20-%20Fast%20R-CNN%20-%20Fondasi%20RGB.md)) menyerang langsung keterbatasan (1) dan (2): konvolusi dijalankan satu kali per citra dan fitur setiap proposal dipetik dari peta fitur bersama. Bab 014 ([Faster R-CNN](./014%20-%202017%20-%20Faster%20R-CNN%20-%20Fondasi%20RGB.md)) mengganti selective search dengan jaringan pengusul wilayah yang dipelajari, menjawab keterbatasan (4). Sebaliknya, bab 001 ([YOLOv1](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)) mengambil jalan berlawanan — membuang tahap proposal sama sekali demi kecepatan — dan menjadikan R-CNN pembanding utama. Regresi *bounding box* dan skema pra-latih-plus-penyetelan-halus yang diperkenalkan di sini diwarisi oleh ketiganya.

## Poin untuk Sitasi

Kutip dengan kunci `girshick2014rcnn`. Ringkasan yang aman dikutip: "R-CNN menggabungkan *region proposal* bottom-up dari selective search dengan fitur CNN untuk deteksi objek, mencapai 53,3% mAP pada PASCAL VOC 2012 — perbaikan relatif lebih dari 30% terhadap hasil terbaik sebelumnya — dan 31,4% mAP pada ILSVRC2013, mengungguli OverFeat (24,3%). Makalah ini juga menetapkan paradigma pra-latih terbimbing pada klasifikasi berdata besar diikuti penyetelan halus pada data deteksi yang terbatas." Angka 53,3%, 31,4%, dan 24,3% berasal dari abstrak kedua versi naskah. Catatan verifikasi: angka VOC 2007 (58,5% dengan AlexNet; 66,0% dengan VGG-16), ablasi ILSVRC (20,9% hingga 31,0%), hasil segmentasi 47,9%, dan waktu 13 detik per citra dikutip dari tech report arXiv v5 yang diperluas; cocokkan dengan tabel versi konferensi bila mensitasi makalah CVPR 2014 versi pendek.
