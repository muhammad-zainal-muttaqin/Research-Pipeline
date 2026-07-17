# 014 - Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ren2017fasterrcnn` |
| Judul asli | Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks |
| Penulis | Shaoqing Ren, Kaiming He, Ross Girshick, Jian Sun |
| Tahun | 2017 |
| Venue | IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), vol. 39 no. 6, hal. 1137–1149 |
| Tema | Fondasi RGB |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1506.01497
- **Google Scholar:** https://scholar.google.com/scholar?q=Faster%20R-CNN%3A%20Towards%20Real-Time%20Object%20Detection%20with%20Region%20Proposal%20Networks
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Faster%20R-CNN%3A%20Towards%20Real-Time%20Object%20Detection%20with%20Region%20Proposal%20Networks&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Faster R-CNN, detektor objek dua tahap yang menghilangkan ketergantungan pada algoritme *region proposal* (kandidat wilayah objek) eksternal. Komponen barunya adalah *Region Proposal Network* (RPN): jaringan konvolusi yang memprediksi kandidat wilayah beserta skor keobjekan (*objectness*) langsung dari peta fitur — larik keluaran lapisan konvolusi yang mempertahankan susunan spasial citra — yang sama dengan yang dipakai detektor. Karena perhitungan konvolusi dibagi antara pengusul wilayah dan detektor, biaya tambahan untuk menghasilkan proposal turun menjadi sekitar 10 milidetik per citra.

Hasilnya, dengan model VGG-16, sistem lengkap berjalan 5 *frame* per detik (FPS) di GPU dengan hanya 300 proposal per citra, sambil mencapai akurasi tertinggi pada masanya: 73,2% mAP pada PASCAL VOC 2007 dan 70,4% pada VOC 2012. Mekanisme *anchor* yang diperkenalkan di sini menjadi komponen standar detektor sesudahnya, termasuk YOLO sejak YOLOv2.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Detektor berbasis wilayah bekerja dalam dua tahap: pertama mengusulkan kandidat wilayah, kemudian mengklasifikasikan setiap wilayah. Pada R-CNN (bab 012), kedua tahap ini mahal karena setiap wilayah diproses terpisah oleh CNN. Fast R-CNN (bab 013) memangkas biaya tahap kedua dengan menghitung konvolusi satu kali untuk seluruh citra, sehingga tahap deteksinya mendekati *real-time*. Namun tahap pertama tetap diserahkan pada algoritme eksternal, terutama *selective search* — metode yang menggabungkan superpiksel (kelompok piksel homogen) secara bertahap berdasarkan fitur tingkat rendah rancangan manual.

Selepas Fast R-CNN, tahap proposal itulah yang menjadi penghambat. *Selective search* memerlukan sekitar 1,5–2 detik per citra di CPU, satu orde lebih lambat daripada jaringan deteksinya; alternatif tercepat saat itu, EdgeBoxes, masih memerlukan 0,2 detik per citra. Ada dua masalah yang lebih mendasar. Pertama, proposal dihasilkan oleh algoritme tetap yang tidak dapat dilatih, sehingga kualitasnya tidak ikut membaik ketika detektor membaik. Kedua, proposal dan deteksi dihitung oleh dua sistem terpisah, sehingga tidak ada perhitungan yang dibagi. Makalah ini menyerang kedua masalah tersebut sekaligus.

## Ide Utama

Gagasan intinya: peta fitur yang sudah dihitung detektor ternyata cukup untuk menghasilkan proposal; proposal tidak perlu dihitung algoritme lain. RPN ditempatkan di atas peta fitur akhir detektor sebagai jaringan *fully convolutional* (jaringan yang seluruh lapisnya berupa konvolusi, sehingga dapat menerima citra berukuran berapa pun). Di setiap lokasi peta fitur, RPN memprediksi dua hal sekaligus: skor *objectness* (peluang wilayah itu berisi objek, tanpa memedulikan kelasnya) dan koreksi posisi kotak.

Prediksi tidak dilakukan terhadap satu kotak per lokasi, melainkan terhadap sekumpulan kotak acuan berukuran dan berrasio tetap yang disebut *anchor*. Jaringan tidak menebak koordinat kotak dari nol; ia cukup menjawab dua pertanyaan per *anchor*: "apakah *anchor* ini menutupi objek?" dan "bagaimana kotak ini harus digeser dan diubah ukurannya agar pas?". Dengan desain ini, objek aneka ukuran dan bentuk dapat ditangani pada satu skala citra tanpa piramida citra yang mahal.

## Cara Kerja Langkah demi Langkah

### Arsitektur Keseluruhan

Sistem Faster R-CNN terdiri atas dua modul di atas satu tumpukan lapisan konvolusi bersama. Makalah menguji dua tumpukan: ZF (5 lapis konvolusi) dan VGG-16 (13 lapis konvolusi). Citra diskalakan sehingga sisi pendeknya 600 piksel, dan stride total (rasio pengecilan resolusi) kedua jaringan adalah 16 piksel, sehingga peta fitur akhir berukuran sekitar 1/16 dari citra masukan.

Alur data sistem lengkapnya:

```
citra (sisi pendek diskala 600 piksel)
        │
        ▼
┌───────────────────────────────┐
│ konvolusi bersama (VGG-16,    │  peta fitur keluaran:
│ 13 lapis konv, stride 16)     │  W x H x 512
└───────────────┬───────────────┘
                │
   ┌────────────┴────────────┐
   ▼                         │
┌──────────────────────┐     │
│ RPN                  │     │
│ konv 3x3 -> 512-d    │     │
│ ├─ cls: 2k skor      │     │
│ └─ reg: 4k offset    │     │
│ k = 9 anchor/lokasi  │     │
└──────────┬───────────┘     │
           │ ±20.000 anchor  │
           │ NMS (IoU 0,7)   │
           │ 300 teratas     │
           ▼                 ▼
┌───────────────────────────────────────┐
│ RoI pooling pada peta fitur bersama   │
│ -> lapisan terhubung penuh            │
│ -> kelas (20 + latar) + koreksi kotak │
└───────────────────────────────────────┘
```

Diagram di atas menunjukkan pembagian perhitungan: peta fitur dihitung sekali, lalu dipakai dua kali — oleh RPN untuk mengusulkan wilayah, dan oleh tahap deteksi untuk menilainya.

### Region Proposal Network dan Anchor

RPN menggeser jendela konvolusi 3×3 di atas peta fitur akhir. Setiap jendela dipetakan menjadi vektor fitur 256 dimensi (ZF) atau 512 dimensi (VGG), kemudian diumpankan ke dua lapisan saudara: lapisan klasifikasi (cls) yang mengeluarkan 2k skor — objek atau bukan, untuk k kotak — dan lapisan regresi (reg) yang mengeluarkan 4k angka koreksi koordinat. Karena berbentuk konvolusi, kedua lapisan ini terbagi di seluruh lokasi.

Di setiap lokasi dipasang k = 9 *anchor*: kombinasi 3 luas kotak (128², 256², dan 512² piksel) dan 3 rasio aspek (1:1, 1:2, 2:1). Untuk citra sekitar 1000×600 piksel, peta fitur berukuran ±60×40, sehingga terdapat ±60×40×9 ≈ 20.000 *anchor* per citra. Ukuran *anchor* tidak harus pas dengan objek; regresi kotak yang akan mengoreksinya. Selama pelatihan, *anchor* yang melintasi batas citra diabaikan, menyisakan sekitar 6.000 *anchor* per citra.

### Penetapan Label dan Fungsi Loss

Setiap *anchor* diberi label biner berdasarkan IoU (*Intersection over Union* — rasio luas irisan terhadap luas gabungan antara *anchor* dan kotak kebenaran, yaitu kotak anotasi posisi objek yang sebenarnya). *Anchor* berlabel positif bila memiliki IoU di atas 0,7 dengan suatu kotak kebenaran, atau bila ia adalah *anchor* dengan IoU tertinggi untuk suatu kotak kebenaran (kondisi cadangan agar setiap objek terwakili). *Anchor* berlabel negatif bila IoU-nya di bawah 0,3 terhadap semua kotak kebenaran; sisanya tidak ikut dihitung.

Fungsi loss mengikuti pola *multi-task* Fast R-CNN: loss klasifikasi berupa *log loss* dua kelas (negatif logaritma peluang prediksi pada kelas yang benar) ditambah loss regresi berupa *smooth L1* (fungsi yang kuadratik di sekitar nol dan linear untuk galat besar, sehingga tidak peka terhadap pencilan). Loss regresi hanya aktif untuk *anchor* positif. Karena *anchor* negatif jauh lebih banyak, setiap mini-batch — kelompok contoh yang diproses dalam satu langkah pembaruan bobot — dibatasi 256 *anchor* terpilih acak dari satu citra dengan rasio positif:negatif maksimal 1:1.

### Parameterisasi Regresi Kotak

Regresi memprediksi transformasi dari *anchor* ke kotak objek, bukan koordinat absolut. Untuk pusat kotak dipakai selisih ternormalisasi, t_x = (x − x_a)/w_a, sedangkan untuk ukuran dipakai skala logaritmik, t_w = log(w/w_a), dan setara untuk t_y dan t_h. Bentuk logaritmik membuat koreksi bersifat relatif: memperbesar kotak 2 kali lipat bernilai sama di mana pun ukuran awalnya. Setiap *anchor* memiliki regresornya sendiri, sehingga 9 regresor belajar koreksi khas untuk skala dan rasionya masing-masing.

### Dari Proposal ke Deteksi

Setelah skor dan offset dihitung, *anchor* diubah menjadi kotak proposal, lalu dirampingkan dengan *Non-Maximum Suppression* (NMS): dari sekumpulan kotak yang saling tumpang tindih dengan IoU di atas 0,7, hanya yang berskor *objectness* tertinggi yang dipertahankan. NMS menyisakan sekitar 2.000 proposal; 300 teratas dipakai pada saat pengujian. Setiap proposal dinilai tahap Fast R-CNN: *RoI pooling* (operasi yang memotong wilayah berukuran bebas dari peta fitur menjadi fitur berukuran tetap) mengekstrak fiturnya, lalu lapisan terhubung penuh mengeluarkan kelas akhir (20 kelas VOC ditambah latar) beserta koreksi kotak per kelas.

### Pelatihan Bersama

RPN dan Fast R-CNN yang dilatih terpisah akan mengubah lapisan konvolusi ke arah berbeda. Makalah memakai pelatihan bergantian empat langkah: (1) latih RPN dari bobot hasil pralatih klasifikasi ImageNet; (2) latih Fast R-CNN memakai proposal RPN tersebut; (3) pakai bobot detektor untuk menginisialisasi RPN, bekukan lapisan bersama, dan setel hanya lapisan khas RPN; (4) setel lapisan khas Fast R-CNN dengan lapisan bersama tetap beku. Hasilnya satu jaringan dengan lapisan konvolusi yang melayani dua tugas. Makalah juga melaporkan pelatihan gabungan aproksimatif yang mengabaikan gradien terhadap koordinat proposal; hasilnya hampir sama dengan waktu latih 25–50% lebih singkat.

## Eksperimen dan Hasil

Evaluasi dilakukan pada PASCAL VOC 2007 dan 2012 (20 kelas) serta MS COCO (80 kelas), dengan metrik mAP (*mean Average Precision*: rata-rata presisi lintas kelas, maksimal 100%). Pada VOC 2007, detektor Fast R-CNN berbasis ZF dengan proposal *selective search* memperoleh 58,7% mAP; mengganti proposalnya dengan RPN (jaringan ZF yang sama, 300 proposal) menaikkan mAP menjadi 59,9% sekaligus memangkas waktu proposal dari ±1,5 detik menjadi 10 milidetik. Dengan VGG-16 dan fitur bersama, mAP mencapai 69,9% saat dilatih pada VOC 2007 dan 73,2% saat dilatih pada gabungan VOC 2007+2012; pada VOC 2012 hasilnya 70,4%, dan bertambah menjadi 75,9% bila data COCO ikut dipakai untuk pelatihan. Angka terakhir menunjukkan data tambahan berdampak lebih besar daripada perubahan metode.

Pada MS COCO, Faster R-CNN memperoleh 42,1% mAP@0,5 dan 21,5% mAP@[.5,.95] (rata-rata mAP pada sepuluh ambang IoU dari 0,5 hingga 0,95, metrik yang lebih menuntut ketepatan lokalisasi), naik 2,8 poin dan 2,2 poin dari pembanding Fast R-CNN pada protokol yang sama; melatihkan data validasi menaikkannya menjadi 42,7% dan 21,9%. Peningkatan pada ambang IoU tinggi menandakan proposal RPN memang lebih tepat posisinya.

Dua ablasi penting memperkuat klaim desain. Pertama, mengganti tahap proposal dengan jendela geser padat satu tahap menurunkan mAP dari 58,7% menjadi 53,9% (jaringan ZF), sehingga kaskade dua tahap terbukti berkontribusi langsung terhadap akurasi. Kedua, memakai hanya satu *anchor* per lokasi menurunkan mAP 3–4 poin, sehingga *anchor* multi-skala dan multi-rasio terbukti berfungsi. Kecepatan akhir: 198 milidetik per citra (±5 FPS) dengan VGG-16 dan 17 FPS dengan ZF, dibandingkan ±2 detik bila proposal masih dihitung *selective search*. Kerangka ini menjadi dasar entri juara pertama beberapa jalur kompetisi ILSVRC dan COCO 2015.

## Kelebihan dan Keterbatasan

Kelebihannya: proposal menjadi nyaris gratis karena berbagi konvolusi; kualitas proposal ikut terlatih dan meningkat bersama jaringan yang lebih baik; desain *anchor* menangani multi-skala pada satu skala citra; dan seluruh sistem dapat dilatih menyeluruh.

Keterbatasannya: kecepatan 5 FPS dengan VGG-16 masih jauh dari *real-time* ketat, dan detektor satu tahap seperti YOLO (bab 001) tetap satu orde lebih cepat dengan akurasi sedikit lebih rendah. Desain *anchor* memperkenalkan parameter rancangan baru — skala, rasio, dan ambang IoU label — yang harus disesuaikan per dataset; makalah sendiri menambah skala 64² khusus untuk objek kecil di COCO. Dari sisi rekayasa, pelatihan empat langkah lebih rumit daripada pelatihan satu jaringan tunggal, dan tahap NMS pada ±20.000 kandidat tetap menyisakan biaya dan ambang rancangan. Secara konseptual, ketergantungan pada *anchor* rancangan tangan menjadi titik yang diserang generasi detektor *anchor-free*.

## Kaitan dengan Bab Lain

Bab ini meneruskan garis keluarga R-CNN: [bab 012](./012%20-%202014%20-%20R-CNN%20-%20Fondasi%20RGB.md) memperkenalkan deteksi berbasis proposal, [bab 013](./013%20-%202015%20-%20Fast%20R-CNN%20-%20Fondasi%20RGB.md) mempercepat tahap deteksi, dan bab ini menghapus hambatan terakhirnya dengan mengintegrasikan proposal ke dalam jaringan. Warisannya melintasi paradigma: [bab 002](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md) meminjam konsep *anchor* untuk detektor satu tahap YOLO; [bab 017](./017%20-%202017%20-%20Mask%20R-CNN%20-%20Fondasi%20RGB.md) memperluas Faster R-CNN menjadi segmentasi instans; dan [bab 018](./018%20-%202017%20-%20Feature%20Pyramid%20Networks%20%28FPN%29%20-%20Fondasi%20RGB.md) menyempurnakan penanganan multi-skala di atasnya. Sebagai pembanding, [bab 016](./016%20-%202017%20-%20RetinaNet%20%28Focal%20Loss%29%20-%20Fondasi%20RGB.md) menunjukkan detektor satu tahap dapat menyaingi akurasi dua tahap yang diletakkan di sini.

## Poin untuk Sitasi

Kutip dengan kunci `ren2017fasterrcnn`. Ringkasan yang aman dikutip: "Faster R-CNN memperkenalkan Region Proposal Network yang berbagi fitur konvolusi dengan detektor Fast R-CNN melalui mekanisme *anchor*, sehingga proposal berkualitas diperoleh dengan biaya sekitar 10 milidetik per citra; sistem mencapai 73,2% mAP pada PASCAL VOC 2007 dengan kecepatan 5 FPS menggunakan VGG-16." Seluruh angka pada bab ini dikutip dari naskah versi jurnal (TPAMI 2017) di arXiv; untuk sitasi formal, cocokkan angka mAP per konfigurasi data latih (misalnya 69,9% untuk latih VOC 2007 saja) dengan tabel naskah asli.
