# 105 - Uncertainty-Guided Cross-Modal Learning for Robust Multispectral Pedestrian Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kim2022cmpd` |
| Judul asli | Uncertainty-Guided Cross-Modal Learning for Robust Multispectral Pedestrian Detection |
| Penulis | Jung Uk Kim, Sungjune Park, Yong Man Ro |
| Tahun | 2022 |
| Venue | IEEE Transactions on Circuits and Systems for Video Technology (TCSVT), vol. 32, no. 3, hlm. 1510–1523 |
| Tema | Pedestrian RGB-T |

## Tautan Akses
- **DOI (versi penerbit):** https://doi.org/10.1109/TCSVT.2021.3076466
- **Google Scholar:** https://scholar.google.com/scholar?q=Uncertainty-Guided%20Cross-Modal%20Learning%20for%20Robust%20Multispectral%20Pedestrian%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Uncertainty-Guided%20Cross-Modal%20Learning%20for%20Robust%20Multispectral%20Pedestrian%20Detection&sort=relevance
- **Versi pendahulu (konferensi MMM 2021):** https://doi.org/10.1007/978-3-030-67832-6_32

## Gambaran Umum

Makalah ini mengusulkan CMPD (disingkat dari isi makalah, bukan akronim resmi penulis), sebuah kerangka deteksi pejalan multispektral yang memakai dua warna cahaya berbeda — citra warna (RGB) dan citra termal (*thermal*, inframerah gelombang panjang) — dengan memodelkan secara eksplisit seberapa dapat diandalkan fitur dari tiap modal pada tiap kasus. Alih-alih menggabungkan kedua modal dengan bobot tetap atau bobot yang hanya bergantung pada kondisi pencahayaan global, penulis mengukur dua jenis ketidakpastian (*uncertainty*) pada level wilayah dan level prediksi, lalu memakai keduanya untuk mengendalikan proses fusi dan pelatihan pengklasifikasi.

Dua masalah spesifik yang disasar adalah *miscalibration* (kotak wilayah dari kedua kamera tidak sejajar sempurna karena sudut pandang, *field-of-view*, yang berbeda) dan *modality discrepancy* (perbedaan keandalan sinyal antar-modal akibat panjang gelombang yang berbeda, sehingga muncul masalah *overconfidence* — jaringan tetap memberi skor keyakinan tinggi meski fitur sumbernya sebenarnya tidak dapat diandalkan). Kerangka yang diusulkan terdiri atas dua modul: *Uncertainty-aware Feature Fusion* (UFF) yang menekan pengaruh fitur wilayah tak andal saat fusi, dan *Uncertainty-aware Cross-Modal Guiding* (UCG) yang mengarahkan distribusi fitur modal kurang andal menuju distribusi modal yang lebih andal. Metode ini diuji pada KAIST Multispectral Pedestrian Benchmark dan CVC-14, dua tolok ukur standar deteksi pejalan RGB-T (RGB-*thermal*), dan penulis melaporkan metode ini melampaui sejumlah pembanding sezaman.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi pejalan berbasis RGB-T lahir dari kebutuhan mengatasi kegagalan kamera tunggal pada kondisi tertentu: kamera RGB kehilangan kontras dalam gelap, sedangkan kamera termal kurang informatif saat suhu latar dan suhu tubuh berdekatan (misalnya siang hari yang terik). Dataset KAIST Multispectral Pedestrian (bab 100), yang menyediakan pasangan citra RGB dan termal yang telah diselaraskan waktu dan sudut pandang secara kasar, menjadi tolok ukur standar untuk klaster ini. Generasi metode fusi pertama, seperti IAF R-CNN (bab 101), menangani ketidaksetaraan keandalan modal dengan pendekatan *illumination-aware*: sebuah subjaringan menaksir tingkat pencahayaan citra secara keseluruhan (siang/malam), lalu bobot fusi antar-modal diatur berdasarkan taksiran itu. MBNet (bab 102) dan GAFF (bab 103) memperhalus mekanisme fusi dengan modul kesadaran ilumninasi dan *attention* (mekanisme pembobotan fitur berbasis relevansi) lintas-modal, sedangkan CFR (bab 104) menambahkan siklus penghalusan fitur bertahap.

Pendekatan berbasis iluminasi global memiliki keterbatasan mendasar: iluminasi citra secara keseluruhan bukan indikator langsung dari keandalan fitur pada wilayah kandidat (*Region of Interest*, RoI — bagian citra yang diduga memuat objek) tertentu. Sebuah wilayah bisa saja tidak andal bukan karena kondisi cahaya, melainkan karena kotak wilayah dari dua kamera tidak sejajar akibat *field-of-view* yang berbeda, sehingga fitur RGB dan termal yang digabungkan sebetulnya menunjuk ke bagian citra yang sedikit bergeser. Masalah kedua adalah bahwa jaringan saraf konvolusi dalam sering bersifat *overconfident*: skor keyakinan keluaran cenderung tinggi meski fitur masukannya sebenarnya kurang informatif, sehingga metode fusi yang hanya mengandalkan bobot iluminasi tidak punya mekanisme untuk mendeteksi dan mengoreksi kepercayaan berlebih semacam itu. Kedua celah inilah yang menjadi target makalah ini: mengganti proksi kasar (iluminasi global) dengan taksiran ketidakpastian yang diestimasi langsung dari fitur wilayah dan fitur prediksi itu sendiri.

## Ide Utama

Gagasan inti makalah adalah membedakan dua sumber ketidakandalan sinyal secara eksplisit, masing-masing diberi taksiran ketidakpastian tersendiri. **Ketidakpastian RoI** (*RoI uncertainty*) mengukur seberapa dapat diandalkan fitur pada satu wilayah kandidat tertentu, dan dipakai untuk mengatasi dampak miskalibrasi antar-kamera: wilayah yang fiturnya tidak konsisten antar-modal diberi bobot lebih rendah saat digabung. **Ketidakpastian prediktif** (*predictive uncertainty*) mengukur seberapa dapat diandalkan keluaran prediksi kelas dari satu modal, dan dipakai untuk mengatasi diskrepansi modal serta *overconfidence*: modal yang taksiran ketidakpastian prediktifnya tinggi (kurang andal pada kondisi tersebut) diarahkan untuk menyerupai distribusi fitur modal yang taksiran ketidakpastiannya rendah (lebih andal).

Dengan kata lain, alih-alih memutuskan bobot fusi dari satu sinyal global (iluminasi), jaringan menghasilkan dua taksiran ketidakpastian yang berbeda level (wilayah dan prediksi), lalu memakai keduanya sebagai sinyal kendali: taksiran pertama mengendalikan bagaimana fitur digabung (modul UFF), taksiran kedua mengendalikan bagaimana pengklasifikasi dilatih agar tidak terlalu percaya pada modal yang sedang tidak andal (modul UCG).

## Cara Kerja Langkah demi Langkah

### Ekstraksi Fitur Wilayah Dua Modal

Citra RGB dan citra termal yang berpasangan masing-masing dilewatkan melalui cabang jaringan konvolusi terpisah untuk menghasilkan peta fitur. Dari peta fitur ini, kandidat wilayah pejalan (RoI) diusulkan dan fitur tiap RoI diekstrak untuk kedua modal, mengikuti kerangka umum detektor berbasis wilayah (*region-based detector*, seperti keluarga R-CNN pada bab 012–014).

### Estimasi Ketidakpastian RoI

Untuk setiap pasangan RoI RGB-termal, jaringan menaksir ketidakpastian RoI: sebuah nilai yang menyatakan seberapa besar keraguan bahwa fitur wilayah tersebut, pada kedua modal, benar-benar menunjuk ke objek yang sama dan selaras secara spasial. Taksiran ini secara langsung menyasar masalah miskalibrasi: bila kotak RGB dan termal sedikit bergeser akibat perbedaan *field-of-view* kamera, fitur pada wilayah itu menjadi kurang konsisten dan ketidakpastian RoI-nya meningkat.

### Uncertainty-aware Feature Fusion (UFF)

Modul UFF menggabungkan fitur RoI dari kedua modal dengan memakai taksiran ketidakpastian RoI sebagai pengendali bobot: wilayah dengan ketidakpastian tinggi diberi pengaruh lebih kecil terhadap fitur gabungan, sedangkan wilayah dengan ketidakpastian rendah (fitur kedua modal konsisten dan selaras) diberi pengaruh lebih besar. Mekanisme ini membuat fusi tahan terhadap wilayah yang miskalibrasi tanpa perlu penyelarasan geometris eksplisit antar-kamera.

### Estimasi Ketidakpastian Prediktif

Setelah fitur RoI gabungan diteruskan menuju tahap klasifikasi, jaringan juga menaksir ketidakpastian prediktif untuk tiap modal secara terpisah — nilai yang menyatakan seberapa dapat diandalkan prediksi kelas (pejalan/bukan pejalan) yang dihasilkan modal tersebut pada kasus itu. Taksiran ini menangkap kondisi seperti termal yang kurang informatif pada siang panas atau RGB yang kurang informatif pada malam gelap, tanpa memerlukan label eksplisit "siang" atau "malam": nilai ketidakpastian dipelajari dari pola fitur itu sendiri.

### Uncertainty-aware Cross-Modal Guiding (UCG)

Modul UCG memakai selisih ketidakpastian prediktif antar-modal untuk mengarahkan pelatihan pengklasifikasi. Modal dengan ketidakpastian prediktif lebih tinggi (kurang andal pada kasus tersebut) diarahkan agar distribusi fiturnya menyerupai distribusi fitur modal dengan ketidakpastian lebih rendah (lebih andal), memakai label sasaran lunak (*soft target label* — target pelatihan berupa distribusi probabilitas, bukan label satu-kelas keras) yang sadar akan tingkat ketidakpastian tersebut. Dengan begitu, kesalahan dari modal yang sedang tidak andal tidak diteruskan begitu saja ke prediksi akhir, dan masalah *overconfidence* pada modal yang lemah ditekan.

Alur keseluruhan pipeline dapat diringkas sebagai berikut:

```
citra RGB --> fitur RoI RGB   \
                                >-- ketidakpastian RoI --> UFF --+
citra termal --> fitur RoI termal /                              |
                                                                   v
                                                          fitur gabungan RoI
                                                                   |
                              ketidakpastian prediktif per-modal   |
                              (RGB vs termal)                     v
                                        \                 klasifikasi awal
                                         >------ UCG -----(soft target
                                        /                  sadar-ketidakpastian)
                              modal kurang andal diarahkan        |
                              menuju modal lebih andal            v
                                                          prediksi akhir pejalan
```

### Pelatihan

Kerangka dilatih secara *end-to-end* (dari citra masukan sampai prediksi akhir dalam satu proses optimisasi tanpa tahap terpisah): taksiran ketidakpastian RoI, taksiran ketidakpastian prediktif, modul UFF, dan modul UCG dioptimalkan bersama dengan tujuan akhir deteksi pejalan, sehingga kedua taksiran ketidakpastian belajar mencerminkan kegunaannya bagi tugas deteksi, bukan diestimasi sebagai tahap terpisah yang berdiri sendiri.

## Eksperimen dan Hasil

Evaluasi utama dilakukan pada KAIST Multispectral Pedestrian Benchmark (bab 100), memakai protokol pengujian standar klaster ini: metrik *log-average miss rate* (MR⁻², rata-rata logaritmik dari *miss rate* — proporsi pejalan yang gagal terdeteksi — pada rentang *false positive per image* tertentu) di bawah pengaturan "*reasonable*" yang mengecualikan pejalan yang sangat kecil atau tertutup berat; semakin rendah nilainya semakin baik. Pengujian dipecah menurut kondisi siang dan malam untuk menilai konsistensi lintas iluminasi, karena itulah tujuan utama metode ini. CVC-14, tolok ukur pejalan RGB-termal siang-malam kedua, dipakai sebagai pengujian tambahan atas kemampuan generalisasi metode ke pasangan sensor dan protokol anotasi yang berbeda dari KAIST.

Penulis melaporkan bahwa kerangka ini melampaui sejumlah metode pembanding sezaman yang memakai fusi berbasis iluminasi atau *attention* tanpa pemodelan ketidakpastian eksplisit, dengan perbaikan yang konsisten pada kedua kondisi siang dan malam, bukan hanya pada satu kondisi tertentu. Studi ablasi pada makalah menunjukkan bahwa modul UFF dan modul UCG masing-masing memberi kontribusi yang terpisah: UFF menyumbang ketahanan terhadap miskalibrasi wilayah, sedangkan UCG menyumbang ketahanan terhadap diskrepansi modal antar-kondisi. Nilai *miss rate* persis untuk tiap kondisi (siang, malam, keseluruhan) pada KAIST dan CVC-14, serta rincian arsitektur cabang penaksir ketidakpastian, tidak berhasil diverifikasi penuh dari sumber sekunder yang tersedia dalam riset ini dan perlu diperiksa langsung pada tabel naskah asli sebelum dikutip sebagai angka pasti (lihat *Poin untuk Sitasi*).

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini adalah mengganti proksi kasar berbasis iluminasi global — yang dipakai metode pendahulunya seperti IAF R-CNN — dengan taksiran ketidakpastian yang dipelajari langsung dari fitur wilayah dan fitur prediksi, sehingga mekanisme fusi dapat bereaksi terhadap sumber ketidakandalan yang lebih beragam daripada sekadar siang/malam, termasuk miskalibrasi antar-kamera pada level wilayah individual. Pemisahan dua jenis ketidakpastian (RoI dan prediktif) juga memberi kerangka konseptual yang jelas: satu menyasar masalah geometris (penyelarasan), satu lagi menyasar masalah statistik (keandalan sinyal per-modal), sehingga tiap modul (UFF dan UCG) memiliki tanggung jawab yang tidak tumpang tindih.

Dari sisi rekayasa, penambahan dua cabang penaksir ketidakpastian menambah parameter dan kompleksitas pelatihan dibandingkan detektor fusi yang lebih sederhana, dan kualitas seluruh sistem bergantung pada seberapa baik kedua taksiran ketidakpastian itu terkalibrasi terhadap kegagalan yang sesungguhnya terjadi pada data. Secara konseptual, metode ini tetap mengasumsikan tersedianya pasangan citra RGB dan termal yang sudah terhubung kasar (sebagaimana pada KAIST dan CVC-14); makalah ini tidak dirancang untuk kasus salah satu modal hilang sepenuhnya saat inferensi. Fokus makalah juga terbatas pada deteksi pejalan sebagai satu kelas objek, sehingga generalisasi kerangka ketidakpastian ganda ini ke deteksi multi-kelas RGB-T tidak dibahas.

## Kaitan dengan Bab Lain

Makalah ini berdiri pada garis kerja yang sama dengan bab 100 (KAIST), sumber data uji utamanya, dan merupakan kelanjutan langsung dari pendekatan berbasis iluminasi pada bab 101 (IAF R-CNN): bila bab 101 memakai iluminasi global sebagai proksi keandalan modal, bab ini mengusulkan proksi yang lebih halus berupa ketidakpastian RoI dan ketidakpastian prediktif per-kasus. Dibandingkan bab 102 (MBNet) dan bab 103 (GAFF), yang memakai kesadaran-iluminasi dan *attention* lintas-modal untuk memandu fusi, bab ini menawarkan jalur berbeda menuju tujuan yang sama — ketahanan lintas kondisi — dengan mengukur ketidakandalan secara langsung dari statistik fitur, bukan dari sinyal iluminasi atau relevansi *attention*. Bab ini juga melengkapi bab 104 (CFR), yang menyempurnakan fusi lewat siklus penghalusan fitur bertahap tanpa pemodelan ketidakpastian eksplisit. Untuk pembaca yang menelusuri klaster Pedestrian RGB-T secara berurutan, bab ini dan [bab 106](./106%20-%202021%20-%20RGB-D%20Fusion%20for%20Detection%20%28Farahnakian%20%26%20Heikkonen%29%20-%20Pedestrian%20RGB-T.md) sama-sama menyoroti bahwa keandalan satu modal tidak bisa diasumsikan tetap, baik pada pasangan RGB-termal maupun RGB-*depth*.

## Poin untuk Sitasi

Kutip dengan kunci `kim2022cmpd`. Ringkasan yang aman dikutip: "Makalah ini mengusulkan pemodelan ketidakpastian RoI dan ketidakpastian prediktif secara terpisah untuk deteksi pejalan RGB-termal, memakainya melalui modul UFF (fusi sadar-ketidakpastian) dan UCG (pemanduan lintas-modal sadar-ketidakpastian) untuk mengatasi miskalibrasi antar-kamera dan diskrepansi keandalan antar-modal, diuji pada KAIST Multispectral Pedestrian Benchmark dan CVC-14." Definisi UFF, UCG, ketidakpastian RoI, dan ketidakpastian prediktif diverifikasi dari ringkasan resmi metadata publikasi (Kyung Hee University) dan abstrak versi pendahulu konferensi (MMM 2021, DOI 10.1007/978-3-030-67832-6_32). Nilai *miss rate* numerik per kondisi (siang/malam/keseluruhan) pada KAIST maupun CVC-14, serta hasil ablasi kuantitatif UFF versus UCG, **belum terverifikasi langsung dari tabel naskah asli** dalam riset ini — sumber sekunder yang ditemukan (tabel perbandingan pada makalah pihak ketiga) menyebut angka berbeda-beda dan berpotensi tertukar dengan versi konferensi 2021 dari tim penulis yang sama; angka-angka ini harus diperiksa ulang pada PDF resmi IEEE Xplore sebelum dikutip dalam karya formal.
