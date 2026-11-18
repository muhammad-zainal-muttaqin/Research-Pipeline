# Machine vision for ripeness estimation in viticulture automation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `vrochidou2021machine` |
| Judul asli | Machine vision for ripeness estimation in viticulture automation |
| Penulis | Vrochidou, Eleni; Bazinas, Christos; Manios, Michail; Papakostas, George A.; Pachidis, Theodore P.; Kaburlasos, Vassilis G. |
| Tahun | 2021 |
| Venue | Horticulturae |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | grape |

## Tautan Akses
- PDF: [vrochidou2021machine.pdf](../pdf/vrochidou2021machine.pdf)
- DOI resmi: https://doi.org/10.3390/horticulturae7090282

## Gambaran Umum

Tinjauan ini menyurvei aplikasi penglihatan mesin untuk estimasi kematangan buah anggur dalam otomasi perkebunan anggur. Penulis menyatakan penentuan waktu panen merupakan keputusan penting karena menentukan mutu hasil, khususnya pada anggur wine yang kualitasnya terkait konsentrasi senyawa seperti antosianin. Waktu panen bergantung pada lokasi, lama musim tumbuh, kultivar, beban tanaman, dan penggunaan buah, serta kondisi lingkungan. Cara tradisional memadukan penilaian indrawi warna dan rasa oleh ahli dengan pengambilan contoh berulang dan analisis kimia; cara ini subjektif, destruktif, memakan waktu, mahal, dan hanya menguji sejumlah contoh terbatas sehingga menurunkan presisi. Karena anggur termasuk buah non-klimakterik yang tidak terus matang setelah dipetik, pemetikan harus dilakukan setelah kematangan merata.

Penulis menguraikan indikator kematangan kimia dan indrawi. Indikator kimia mencakup kandungan padatan terlarut atau SSC dalam satuan °Brix, keasaman tertitrasi TA, rasio SSC/TA, pH, senyawa volatil, polifenol, antosianin, tanin, terpen, klorofil, antioksidan, dan flavanol. Batas indikatif untuk anggur wine matang adalah 3,2 < pH < 3,5, 20 < SSC < 23, dan 4 < TA < 7; anggur meja dianggap matang pada 16 °Brix, Sauvignon Blanc pada 20–22 °Brix, serta Merlot dan Cabernet pada 21–23 °Brix. Indikator indrawi meliputi warna, ukuran, dan rasa, dengan warna sebagai penanda paling penting, meskipun banyak kultivar berubah warna sebelum matang sehingga warna biji yang berubah dari hijau ke cokelat dianggap lebih diskritif namun bersifat invasif.

Mekanisme deteksi yang ditinjau dibagi atas pencitraan warna RGB, pencitraan hiperspektral, dan spektroskopi inframerah dekat. Pencitraan RGB memakai ruang warna CIELAB, HSI, dan HSV serta ciri kolorimetri, morfologi, dan tekstur, dengan model seperti regresi bertahap, analisis diskriminan, SVM, SVR, random forest, CNN, jaringan saraf, PLSR, dan Dirichlet Mixture Model. Pencitraan hiperspektral merekam pantulan pada banyak pita bersebelahan untuk memperoleh informasi spektral dan spasial, sedangkan spektroskopi NIR mengukur radiasi yang ditransmisikan atau dipantulkan tanpa preparasi kimia. Penulis memetakan pita serapan yang terkait senyawa, antara lain sekitar 1.200 nm untuk gula, 950 dan 1.460 nm untuk air, 990 nm untuk gula dan asam organik, 1.690 dan 1.750 nm untuk glukosa dan etanol, 2.260 nm untuk glukosa, 2.302 nm untuk etanol dan karbohidrat, 280 nm untuk polifenol total, serta 420, 520, dan 620 nm untuk hijau, merah, dan biru.

Berikut angka hasil beserta metrik dan acuan hitungnya. Pada pencitraan warna, analisis 15.000 citra dan 21 polifenol menghasilkan R² hingga 0,97; klasifikasi menghasilkan tingkat 100% untuk Syrah merah, 87,50% untuk Tempranillo merah, 71,43% untuk Zalema putih pada tanah pasir, dan 57,14% pada tanah lempung; SVM mencapai 96,88%; SVR menghasilkan MSE 22,64; regresi MLR dan PLSR menghasilkan MSE pH 0,0987 dan 0,1257 serta MSE SSC 0,7982 dan 0,9252; CNN mencapai 79% pada anggur putih dan 93,41% pada Syrah, sedangkan SVM 69%. Pada pencitraan hiperspektral, PLSR menghasilkan R² 0,95 untuk TA dan 0,94 untuk SSC pada anggur putih; jaringan saraf menghasilkan R² 0,92 untuk SSC dan 0,95 untuk antosianin; dan regresi PLS menghasilkan R² 0,99 untuk TA, 0,95 untuk TF, dan 0,94 untuk TSS. Spektroskopi NIR menghasilkan R² 0,86 untuk antosianin. Metrik yang dipakai adalah R², tingkat klasifikasi, MSE, dan average error, dengan acuan berupa analisis kimia atau penilaian visual.

Penulis menyatakan sejumlah batasan. Belum ada kajian yang membandingkan secara menyeluruh ciri dari berbagai ruang warna, sehingga tidak ada kesimpulan pasti mengenai ciri optimal. pH sering kurang dapat diandalkan, dan hubungan antarindikator kematangan belum dipahami sepenuhnya. Pencitraan hiperspektral mahal dan kompleks serta menghasilkan jumlah citra terbatas, sehingga menghambat penggunaan pembelajaran mendalam; hanya dua kajian memakai CNN dan kinerjanya tidak selalu lebih tinggi daripada metode lain. Tidak tersedia himpunan data publik berskala besar untuk kematangan anggur, dan metode pencitraan warna memakai akurasi klasifikasi sementara metode hiperspektral memakai R², sehingga sulit dibandingkan langsung. Anggur merah lebih mudah dinilai daripada anggur putih karena perubahan warnanya jelas, sedangkan anggur putih memiliki variasi warna kecil dan mirip daun. Sebagian besar metode diuji di lingkungan terkontrol dengan pencahayaan buatan; dari 20 metode yang ditinjau, hanya sembilan yang membiarkan tandan tetap utuh dan hanya enam yang dapat diterapkan di lapangan. Integrasi ke robot pemanen masih pada tahap awal, dan model pertumbuhan tanaman belum memasukkan ciri warna dan morfologi dari citra.

