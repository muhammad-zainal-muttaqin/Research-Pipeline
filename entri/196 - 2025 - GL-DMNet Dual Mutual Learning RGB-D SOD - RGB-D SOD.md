# 196 - Dual Mutual Learning Network with Global-local Awareness for RGB-D Salient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yi2025gldmnet` |
| Judul asli | Dual Mutual Learning Network with Global-local Awareness for RGB-D Salient Object Detection |
| Penulis | Kang Yi, Haoran Tang, Yumeng Li, Jing Xu, Jun Zhang |
| Tahun | 2025 |
| Venue | arXiv preprint arXiv:2501.01648 |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2501.01648
- **Google Scholar:** https://scholar.google.com/scholar?q=Dual%20Mutual%20Learning%20Network%20with%20Global-local%20Awareness%20for%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Dual%20Mutual%20Learning%20Network%20with%20Global-local%20Awareness%20for%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Gambaran Umum

GL-DMNet (*Global-Local Dual Mutual Network*) adalah jaringan untuk *RGB-D salient object detection* (SOD, deteksi objek yang menonjol secara visual dalam suatu adegan), yang memanfaatkan citra warna (RGB) dan peta kedalaman (*depth map*, citra yang tiap pikselnya menyatakan jarak permukaan ke kamera) sekaligus. Masalah yang disasar makalah ini adalah cara kedua modalitas tersebut digabungkan: metode-metode sebelumnya cenderung memaksakan fusi searah tanpa memperhitungkan bahwa RGB dan depth memiliki karakteristik statistik yang berbeda, serta kurang menyeimbangkan konteks global dan detail lokal saat menggabungkan fitur bertingkat. GL-DMNet mengatasinya dengan dua modul fusi yang saling menyaling-belajar (*mutual learning*, kedua modalitas saling memengaruhi representasi satu sama lain, bukan satu modalitas mendominasi) pada dimensi posisi dan kanal fitur, ditambah dekoder berbasis *transformer* (jaringan berbasis mekanisme *attention* yang dapat menangkap ketergantungan jarak jauh antarposisi fitur) untuk merekonstruksi peta saliency secara bertahap. Pada enam tolok ukur RGB-D SOD standar, makalah melaporkan unggul dibanding 24 metode pembanding, dengan perbaikan rata-rata sekitar 3% pada empat metrik evaluasi dibanding model terbaik kedua, S3Net.

## Latar Belakang: Masalah yang Ingin Dipecahkan

*SOD* berupaya menghasilkan peta biner atau bernilai kontinu yang menandai wilayah citra paling menonjol secara visual, sebagai langkah awal bagi tugas hilir seperti segmentasi objek atau pengeditan citra otomatis. Menambahkan modalitas *depth* pada tugas ini memberi isyarat geometris (jarak, bentuk permukaan) yang tidak tersedia pada citra RGB murni, terutama berguna ketika objek menonjol memiliki warna atau tekstur mirip latar belakang. Namun, peta *depth* yang diperoleh dari sensor (mis. Kinect) atau estimasi *monocular* sering mengandung derau dan ketidakpastian pada tepi objek.

Pendekatan RGB-D SOD sebelumnya, termasuk yang berbasis *transformer* seperti SwinNet dan TriTransNet, umumnya menggabungkan fitur RGB dan *depth* lewat operasi fusi satu arah — misalnya penjumlahan elemen atau *concatenation* diikuti konvolusi — yang memperlakukan kedua modalitas secara simetris tanpa mekanisme eksplisit untuk menyaring kontribusi masing-masing pada setiap posisi atau kanal fitur. Akibatnya, ketika *depth* berkualitas rendah, kesalahan pada peta *depth* dapat ikut merusak fitur gabungan alih-alih ditekan. Masalah kedua adalah keseimbangan antara konteks global (hubungan antarwilayah citra yang berjauhan, penting untuk menentukan batas objek menonjol secara keseluruhan) dan detail lokal (tekstur dan tepi halus, penting untuk kehalusan kontur). Metode berbasis konvolusi murni unggul pada detail lokal tetapi lemah menangkap ketergantungan jarak jauh, sedangkan metode berbasis *transformer* murni cenderung sebaliknya.

## Ide Utama

Gagasan inti GL-DMNet adalah mengganti fusi searah dengan fusi dua arah yang eksplisit: fitur RGB dan fitur *depth* pada tingkat yang sama saling menyaring satu sama lain melalui dua modul terpisah, satu bekerja pada dimensi posisi spasial dan satu pada dimensi kanal. Kedua modul dijalankan paralel (bukan berurutan), sehingga interaksi posisi dan interaksi kanal tidak saling membatasi. Fitur gabungan dari tiap tingkat kemudian diproses lebih lanjut oleh komponen berbasis *transformer* yang menambahkan kesadaran konteks global sebelum direkonstruksi bertahap menjadi peta saliency akhir beresolusi penuh.

Secara mekanis: masukan berupa citra RGB dan peta *depth* berpasangan diproses oleh *backbone* (jaringan ekstraksi fitur dasar) ResNet-50 secara terpisah untuk masing-masing modalitas, menghasilkan empat tingkat fitur dengan resolusi menurun dan jumlah kanal meningkat, pola umum pada jaringan konvolusi bertingkat. Pada tiap tingkat, fitur RGB dan *depth* dilewatkan ke modul fusi posisi dan modul fusi kanal, keluarannya digabungkan, lalu diproses oleh tahap *transformer* dalam dekoder sebelum ditumpuk dengan fitur tingkat berikutnya secara berjenjang dari resolusi rendah ke tinggi.

## Cara Kerja Langkah demi Langkah

### Ekstraksi Fitur Dua Cabang

Citra RGB dan peta *depth* diproses oleh dua cabang ResNet-50 terpisah (tidak berbagi bobot), masing-masing menghasilkan fitur pada empat tingkat kedalaman jaringan. Tingkat awal memiliki resolusi spasial tinggi dan kanal sedikit (cocok untuk detail lokal seperti tepi), sedangkan tingkat akhir memiliki resolusi rendah dan kanal banyak (memuat informasi semantik/global). Pasangan fitur RGB-*depth* pada tiap tingkat diproses secara independen oleh modul fusi berikutnya, sehingga interaksi antarmodalitas terjadi pada empat skala berbeda, bukan hanya sekali di ujung jaringan.

### Position Mutual Fusion (PMF)

Modul *Position Mutual Fusion* menyelaraskan fitur RGB dan *depth* pada dimensi spasial. Fitur kedua modalitas pertama dijumlahkan secara elemen demi elemen untuk memperoleh representasi gabungan awal, lalu representasi ini diproses dengan *pooling* maksimum dan rata-rata untuk menghasilkan deskriptor perhatian spasial (*spatial attention*, bobot yang menandai posisi piksel mana pada peta fitur yang lebih relevan). Deskriptor gabungan ini kemudian dikalikan matriks (*matrix multiplication*) dengan fitur RGB tunggal dan fitur *depth* tunggal secara terpisah, menghasilkan dua peta perhatian posisi yang masing-masing menyatakan seberapa besar kontribusi tiap posisi dari modalitas lain semestinya diperkuat. Karena kedua peta dihitung dari basis gabungan yang sama tetapi diterapkan kembali pada tiap modalitas secara terpisah, informasi mengalir dua arah — RGB memengaruhi bobot yang diterapkan pada *depth*, dan sebaliknya. Normalisasi momen dan normalisasi L2 diterapkan pada tahap akhir modul untuk menstabilkan skala nilai sebelum digabungkan ke tahap berikutnya.

### Channel Mutual Fusion (CMF)

Modul *Channel Mutual Fusion* menjalankan mekanisme serupa PMF, tetapi pada dimensi kanal alih-alih posisi spasial. Fitur RGB dan *depth* digabungkan (*concatenation*), diproses lewat lapis terhubung penuh (*fully connected*) dengan *pooling* maksimum dan rata-rata untuk menghasilkan deskriptor perhatian kanal, lalu perkalian matriks menghasilkan bobot kanal yang diterapkan kembali ke masing-masing modalitas. Setiap kanal fitur biasanya berkorespondensi dengan satu jenis pola visual (mis. tepi vertikal, tekstur tertentu); modul ini menentukan kanal mana dari satu modalitas yang perlu diperkuat berdasarkan informasi dari modalitas lain. PMF dan CMF berjalan paralel pada tiap tingkat fitur, dan hasil ablasi pada makalah menunjukkan konfigurasi paralel ini mengungguli konfigurasi berurutan atau penggunaan salah satu modul saja.

### Dekoder Rekonstruksi Berbasis Transformer Berjenjang

Fitur gabungan dari PMF dan CMF pada tiap tingkat diproses lebih lanjut oleh komponen bernama *cascade transformer-infused reconstruction decoder* (dekoder rekonstruksi berjenjang yang disisipi *transformer*), yang memakai PVTv2-B2 — varian *Pyramid Vision Transformer* yang menghasilkan representasi fitur pada berbagai skala melalui mekanisme *attention*. Fitur pada tiap tingkat diberi *embedding transformer* secara independen agar tetap dapat diproses paralel dan mempertahankan ciri khas tiap skala, lalu keluaran *transformer* digabungkan kembali dengan fitur fusi aslinya. Perhatian kanal dipakai untuk mengintegrasikan fitur tingkat lebih dalam (semantik) ke tingkat lebih dangkal (detail), dan peta saliency direkonstruksi secara progresif lewat *upsampling* bertahap dari resolusi rendah menuju resolusi penuh citra masukan. Susunan inilah yang memberi "kesadaran global-lokal": komponen *transformer* menangani ketergantungan jarak jauh (global), sementara struktur berjenjang dan fitur konvolusi asli menjaga detail lokal tetap terjaga di tiap skala.

Diagram berikut merangkum aliran data utama jaringan:

```
RGB ──► ResNet-50 (cabang RGB) ──┐
                                  ├─► PMF ──┐
Depth ─► ResNet-50 (cabang D) ───┘         ├─► fitur fusi (4 tingkat)
                                  ├─► CMF ──┘        │
                                  (paralel)          ▼
                                          dekoder PVTv2-B2 berjenjang
                                          (transformer per tingkat +
                                           upsampling bertahap)
                                                      │
                                                      ▼
                                            peta saliency akhir
```

### Fungsi Loss

Pelatihan memakai kombinasi *binary cross-entropy* (BCE, galat klasifikasi piksel-per-piksel antara peta prediksi dan peta kebenaran biner) dan *IoU loss* (galat berbasis rasio irisan-gabungan antara wilayah prediksi dan wilayah kebenaran). Ablasi pada makalah melaporkan kombinasi BCE+IoU memberi hasil lebih baik dibanding alternatif fungsi loss lain yang diuji.

## Eksperimen dan Hasil

Data pelatihan diambil dari gabungan tiga dataset: 700 citra dari NLPR, 800 pasangan dari DUT-RGBD, dan 1.485 sampel dari NJUD, sehingga total sekitar 2.985 pasang citra RGB-*depth* dipakai untuk melatih model. Pengujian dilakukan pada enam dataset benchmark RGB-D SOD: SIP (929 citra pose manusia), DUT-RGBD (1.200 citra indoor dan outdoor), NJUD (2.003 pasang citra stereo), STEREO (797 citra), NLPR (1.000 citra stereo), dan SSD (80 citra alami); pada NLPR, DUT-RGBD, dan NJUD, hanya bagian di luar data latih yang dipakai untuk uji. Metrik evaluasi yang dipakai adalah S-measure (kemiripan struktural antara peta saliency prediksi dan kebenaran), F-measure (rata-rata harmonik presisi dan *recall*), E-measure (kesejajaran piksel yang memperhitungkan informasi global dan lokal sekaligus), dan MAE (*mean absolute error*, rata-rata selisih absolut nilai piksel antara prediksi dan kebenaran, semakin kecil semakin baik), dilengkapi kurva presisi-*recall* untuk perbandingan visual.

GL-DMNet dilaporkan mengungguli 24 metode pembanding RGB-D SOD pada enam dataset tersebut, dengan perbaikan rata-rata sekitar 3% lintas empat metrik dibanding model terbaik kedua, S3Net. Pada dataset NLPR, hasil ablasi konfigurasi terbaik (PMF+CMF paralel dengan dekoder PVTv2) mencatat E-measure 0,962, S-measure 0,927, F-measure 0,926, dan MAE 0,022. Nilai MAE 0,022 berarti rata-rata selisih absolut antara peta saliency prediksi dan kebenaran hanya 2,2% dari rentang nilai piksel, tergolong rendah untuk tolok ukur ini. Studi ablasi juga menunjukkan bahwa PVTv2 sebagai basis dekoder transformer mengungguli PVTv1, dan bahwa desain fusi mutual paralel (PMF dan CMF berjalan bersamaan) mengungguli konfigurasi serial atau penggunaan modul tunggal saja — mengonfirmasi bahwa interaksi posisi dan kanal memberi kontribusi yang saling melengkapi, bukan redundan.

Angka rinci per dataset uji individual (SIP, DUT-RGBD, NJUD, STEREO, SSD) di luar contoh NLPR di atas, serta tabel perbandingan lengkap terhadap seluruh 24 metode pembanding, tidak berhasil diekstrak secara pasti dari sumber yang diakses untuk bab ini dan perlu diverifikasi langsung ke tabel pada naskah asli sebelum dikutip dalam karya formal.

## Kelebihan dan Keterbatasan

Kelebihan utama GL-DMNet adalah mekanisme fusi eksplisit dua arah pada dua dimensi berbeda (posisi dan kanal) yang dijalankan paralel, sehingga interaksi RGB-*depth* tidak bergantung pada satu jenis operasi fusi tunggal. Penggabungan komponen *transformer* dalam dekoder secara berjenjang memberi jaringan akses ke konteks global tanpa mengorbankan detail lokal dari fitur konvolusi asli, dan hasil ablasi yang disertakan penulis (perbandingan paralel vs serial, PVTv2 vs PVTv1, berbagai kombinasi loss) memberi bukti bahwa tiap komponen memang berkontribusi, bukan sekadar penambahan modul tanpa dasar.

Dari sisi rekayasa, arsitektur ini menjalankan dua cabang *backbone* ResNet-50 penuh ditambah empat tahap *transformer* PVTv2-B2 dalam dekoder, sehingga biaya komputasi dan jumlah parameter kemungkinan besar lebih tinggi dibanding metode fusi RGB-D yang lebih ringan seperti MobileSal (bab 170); sumber yang diakses untuk bab ini tidak melaporkan angka FLOPs, jumlah parameter, atau kecepatan inferensi (FPS), sehingga kelayakan model untuk penerapan *real-time* atau perangkat terbatas sumber daya belum dapat dinilai. Secara konseptual, keandalan modul PMF dan CMF terhadap peta *depth* yang sangat berderau atau hilang sebagian belum diuji secara eksplisit dalam ringkasan yang tersedia.

## Kaitan dengan Bab Lain

GL-DMNet melanjutkan garis metode fusi RGB-D berbasis *attention* dan *transformer* yang juga dibahas pada [CAVER](./169%20-%202023%20-%20CAVER%20-%20RGB-D%20SOD.md) (bab 169, fusi lintas-modal dengan *transformer view-mixed*) dan [SPNet](./168%20-%202021%20-%20SPNet%20-%20RGB-D%20SOD.md) (bab 168, saliency yang mempertahankan spesifisitas modalitas). Perbedaan utamanya terletak pada penekanan eksplisit pada pembelajaran mutual dua arah pada dua dimensi fitur terpisah (posisi dan kanal), berbeda dari [DCF](./167%20-%202021%20-%20DCF%20-%20RGB-D%20SOD.md) (bab 167, fusi dinamis kalibrasi-terpandu) dan [CoNet](./166%20-%202020%20-%20CoNet%20-%20RGB-D%20SOD.md) (bab 166, jaringan kolaboratif tiga cabang) yang menata interaksi antarmodalitas dengan skema berbeda. Dibanding [MobileSal](./170%20-%202022%20-%20MobileSal%20-%20RGB-D%20SOD.md) (bab 170, RGB-D SOD ringan berorientasi perangkat mobile), GL-DMNet mengejar akurasi maksimum dengan menambah kompleksitas arsitektur alih-alih efisiensi komputasi, sehingga kedua bab dapat dibaca sebagai representasi dua ujung spektrum desain pada klaster RGB-D SOD: akurasi tinggi dengan biaya komputasi besar versus efisiensi dengan akurasi yang dikompromikan.

## Poin untuk Sitasi

Kutip dengan kunci `yi2025gldmnet`. Ringkasan yang aman dikutip: "GL-DMNet mengusulkan modul Position Mutual Fusion dan Channel Mutual Fusion yang berjalan paralel untuk menyaling-belajar fitur RGB dan *depth* pada dimensi posisi dan kanal, dipadukan dekoder rekonstruksi berjenjang berbasis PVTv2-B2, dan dilaporkan mengungguli 24 metode RGB-D SOD lain dengan perbaikan rata-rata sekitar 3% pada empat metrik di enam dataset benchmark (Yi dkk., arXiv 2501.01648, 2025)." Angka contoh pada NLPR (E-measure 0,962; S-measure 0,927; F-measure 0,926; MAE 0,022) diambil dari hasil ablasi yang diekstrak lewat alat bantu otomatis dari versi HTML arXiv, bukan pembacaan langsung tabel PDF asli — wajib diverifikasi ulang ke naskah sebelum dikutip secara formal. Angka hasil per dataset uji lain (SIP, DUT-RGBD, NJUD, STEREO, SSD) dan tabel perbandingan lengkap terhadap 24 metode pembanding belum berhasil diverifikasi untuk bab ini dan tidak dicantumkan. Status publikasi (preprint arXiv vs versi jurnal terbit) juga perlu dicek ulang sebelum sitasi formal.
