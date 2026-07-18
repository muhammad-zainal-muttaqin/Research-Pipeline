# 130 - Breast Lesions Detection and Classification via YOLO-Based Fusion Models

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `baccouche2021breast` |
| Judul Asli | Breast Lesions Detection and Classification via YOLO-Based Fusion Models |
| Penulis | Asma Baccouche, Begonya Garcia-Zapirain, Cristian Castillo Olea, Adel S. Elmaghraby |
| Tahun | 2021 |
| Venue | Computers, Materials \& Continua |
| Tema | Medis |

## Tautan Akses
*   **DOI (Tech Science Press):** https://doi.org/10.32604/cmc.2021.018461
*   **Google Scholar:** https://scholar.google.com/scholar?q=Breast%20Lesions%20Detection%20and%20Classification%20via%20YOLO-Based%20Fusion%20Models
*   **Semantic Scholar:** https://www.semanticscholar.org/search?q=Breast%20Lesions%20Detection%20and%20Classification%20via%20YOLO-Based%20Fusion%20Models&sort=relevance

## Gambaran Umum
Makalah ini mengusulkan sistem diagnosis berbantuan komputer (*computer-aided diagnosis* atau CAD) berbasis model *You Only Look Once* versi 3 (YOLOv3) yang terintegrasi dengan pendekatan fusi tingkat keputusan (*decision-level fusion*) untuk mendeteksi dan mengklasifikasikan lesi payudara secara simultan pada citra mamografi. Masalah utama yang diselesaikan adalah kesulitan melokalisasi lesi massa (*mass*) yang cenderung besar berbatas kabur, dan kalsifikasi (*calcification*) yang berukuran sangat kecil (*microcalcification*) secara bersamaan. Detektor tunggal standar sering kali gagal mengidentifikasi kedua tipe lesi ini akibat ketidakseimbangan skala objek yang ekstrem.

Untuk mengatasinya, penulis merancang skema fusi yang menggabungkan prediksi dari dua konfigurasi model YOLOv3: model kelas tunggal (*single-class model*) yang dilatih khusus untuk masing-masing kelas lesi, dan model multi-kelas (*multi-class model*) yang mendeteksi kedua kelas secara bersamaan. Evaluasi dilakukan pada tiga dataset mamografi, yaitu Curated Breast Imaging Subset of Digital Database for Screening Mammography (CBIS-DDSM), INbreast, dan sebuah dataset privat dari National Institute of Cancerology (INCAN) Meksiko. Hasil pengujian menunjukkan bahwa model fusi ini meningkatkan akurasi deteksi massa hingga 95,7% (CBIS-DDSM), 98,1% (INbreast), dan 98,0% (privat), serta deteksi kalsifikasi sebesar 74,4% (CBIS-DDSM), 71,8% (INbreast), dan 73,2% (privat), melampaui performa detektor tunggal secara signifikan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Kanker payudara merupakan penyebab utama kematian akibat keganasan pada populasi wanita secara global. Penapisan dini menggunakan mamografi efektif menekan mortalitas, namun interpretasi citra mamogram secara manual sangat menantang dan rentan terhadap kesalahan diagnosis (*human error*). Kendala utamanya adalah rendahnya kontras visual antara jaringan lesi abnormal dengan jaringan kelenjar payudara yang padat, serta keberadaan otot pektoral (*pectoral muscle*) yang memiliki intensitas piksel mirip dengan lesi massa.

Sebelum penerapan detektor satu-tahap (*one-stage detector*) terpadu, sistem CAD medis konvensional memisahkan proses lokalisasi lesi dan klasifikasi patologi menjadi beberapa modul indeks (misalnya diawali segmentasi payudara, dilanjutkan ekstraksi fitur tekstur manual, dan klasifikasi akhir menggunakan SVM). Seperti dibahas pada [Bab 129](./129%20-%202021%20-%20COVID-19%20CAD%20dari%20X-Ray%20%28Al-Antari%20dkk.%29%20-%20Medis.md), pemisahan modul ini memicu akumulasi kesalahan (*error propagation*) di mana kegagalan segmentasi langsung menurunkan akurasi diagnosis akhir.

Meskipun model satu-tahap seperti YOLOv2 telah diterapkan (misalnya model CAD berbasis YOLO oleh Al-Masni dkk. [45]), detektor tunggal standar kesulitan mendeteksi lesi massa dan kalsifikasi secara simultan. Hal ini disebabkan oleh perbedaan dimensi spasial yang kontras antara massa (sentimeter) dan kalsifikasi (milimeter). Ketika dilatih secara multi-kelas, fitur model cenderung didominasi oleh kelas dengan kontras atau ukuran spasial yang lebih menonjol (massa), sehingga memicu tingkat negatif palsu yang tinggi pada kelas minoritas (kalsifikasi). Masalah ketidakseimbangan skala ini melatarbelakangi kebutuhan akan integrasi fusi multi-model.

## Ide Utama
Gagasan inti makalah ini adalah menerapkan fusi tingkat keputusan (*decision-level fusion*) pada beberapa model YOLOv3 yang dilatih dengan spesialisasi kelas berbeda. Pendekatan ini menggabungkan sensitivitas tinggi dari model kelas tunggal dengan fleksibilitas model multi-kelas untuk meminimalisasi tingkat kesalahan prediksi (*miss-prediction error*).

Sistem ini melatih dua jenis model YOLOv3 secara terpisah:
1.  **Model Kelas Tunggal (Model1 / M1):** Terdiri atas model $M^1\text{ (Mass)}$ yang khusus mendeteksi massa dan $M^1\text{ (Calcification)}$ khusus untuk kalsifikasi.
2.  **Model Multi-Kelas (Model2 / M2):** Satu model $M^2\text{ (Mass and Calcification)}$ yang dilatih untuk mendeteksi kedua kelas sekaligus sebagai jangkar pembanding.

Secara mekanis, citra mamogram masukan dilewatkan pada ketiga model tersebut untuk menghasilkan koordinat kotak pembatas (*bounding box*) dan skor kepercayaan (*confidence score*). Fusi keputusan dilakukan dengan menerapkan logika threshold ganda (*dual-threshold logic*). Prediksi awal diambil dari model khusus $M^1$ dengan ambang batas tinggi (threshold1 = 0,5) demi menjaga presisi. Prediksi tambahan dari model multi-kelas $M^2$ disaring dengan ambang batas lebih rendah (threshold2 = 0,35) untuk menangkap lesi samar yang terlewat oleh $M^1$. Hasil dari model multi-kelas ini divalidasi silang untuk mengeliminasi positif palsu sebelum digabungkan menjadi output prediksi akhir.

## Cara Kerja Langkah demi Langkah
Mekanisme kerja sistem YOLO Fusion terbagi menjadi empat tahapan utama:

### Pra-pemrosesan Citra Mamogram
1.  **Ekstraksi Anotasi:** Koordinat lesi payudara diekstraksi ke dalam format nilai tengah spasial ($x, y$), lebar ($w$), dan tinggi ($h$) kotak pembatas beserta label kelasnya.
2.  **Histogram Equalization:** Citra mamogram dari dataset CBIS-DDSM and dataset privat diproses dengan perataan histogram (*histogram equalization*) untuk merentang kontras lokal dan memperjelas lesi. Dataset INbreast tidak melewati tahap ini karena kualitas akuisisinya sudah optimal sejak awal.
3.  **Resize Interpolasi Bikubik:** Citra mamogram diubah dimensinya menjadi resolusi seragam $448 \times 448$ piksel menggunakan interpolasi bikubik (*bi-cubic interpolation*) pada lingkungan tetangga $4 \times 4$ piksel. Ukuran ini dipilih agar habis dibagi oleh 32 sesuai karakteristik reduksi spasial YOLOv3 dan menghemat memori GPU.

### Augmentasi Data Medis
Untuk mengatasi keterbatasan jumlah citra medis, diterapkan augmentasi data geometris secara dinamis yang meliputi rotasi citra ($90^\circ, 180^\circ, 270^\circ$), pergeseran spasial (*translation*), dan pencerminan (*flipping*). Augmentasi ini meningkatkan performa akurasi sebesar 10% untuk CBIS-DDSM dan menstabilkan konvergensi pelatihan model.

### Ekstraksi Fitur Multiskala YOLOv3
Model YOLOv3 menggunakan tulang punggung (*backbone*) Darknet-53 yang mengadopsi sambungan residu (*skip connections*) untuk mencegah hilangnya gradien (*vanishing gradient*). Citra masukan $448 \times 448$ piksel direduksi secara spasial untuk menghasilkan deteksi pada tiga skala grid:
*   Skala Kasar ($14 \times 14$): Untuk melokalisasi lesi massa berukuran besar.
*   Skala Menengah ($28 \times 28$): Untuk lesi berukuran sedang.
*   Skala Halus ($56 \times 56$): Untuk mendeteksi mikro-kalsifikasi yang sangat kecil.
Jangkar kotak pembatas (*anchor boxes*) pada setiap skala disesuaikan khusus dengan karakteristik dimensi lesi mamogram.

### Fusi Keputusan Threshold Ganda
Prediksi akhir diperoleh dengan menggabungkan output model kelas tunggal dan multi-kelas melalui langkah berikut:
1.  Prediksi awal ($P_1$) diperoleh dari model khusus $M^1$ dengan ambang batas IoU $\ge 0,5$.
2.  Prediksi pembanding ($P_2$) diekstrak dari model multi-kelas $M^2$ dengan ambang batas IoU $\ge 0,35$.
3.  Prediksi dari $P_2$ disaring untuk menyisakan kotak pembatas baru ($P_{2\text{\_new}}$) yang tidak terdeteksi dalam $P_1$ (tidak memiliki tumpang-tindih IoU $\ge 0,5$ dengan kotak pembatas di $P_1$).
4.  Prediksi final diperoleh dari gabungan $P_1 \cup P_{2\text{\_new}}$.

Berikut visualisasi diagram alir proses fusi keputusan YOLO Fusion:

```
                  ┌───────────────────────────────┐
                  │ Citra Mamogram Masukan (448)  │
                  └──────┬─────────────────┬──────┘
                         │                 │
                         ▼                 ▼
                 ┌──────────────┐   ┌──────────────┐
                 │ Model M1     │   │ Model M2     │
                 │ (Kelas Tungg)│   │ (Multi-Kelas)│
                 └──────┬───────┘   └──────┬───────┘
                        │                  │
           Threshold1 = 0,5           Threshold2 = 0,35
                        │                  │
                        ▼                  ▼
                 ┌──────────────┐   ┌──────────────┐
                 │ Prediksi M1  │   │ Prediksi M2  │
                 │    (P1)      │   │    (P2)      │
                 └──────┬───────┘   └──────┬───────┘
                        │                  │
                        │        ┌─────────┴────────┐
                        │        │ Filter: Simpan   │
                        │        │ jika TIDAK ada   │
                        │        │ dalam P1 (P2_new)│
                        │        └─────────┬────────┘
                        │                  │
                        ▼                  ▼
                     ┌────────────────────────┐
                     │  Penggabungan (P1+P2)  │
                     └───────────┬────────────┘
                                 ▼
                     ┌────────────────────────┐
                     │ Prediksi Akhir Fusi    │
                     └────────────────────────┘
```

## Eksperimen dan Hasil
Eksperimen menggunakan pembagian data 70% pelatihan, 20% pengujian, dan 10% validasi. Model dilatih menggunakan pengoptimasi Adam (*Adam optimizer*) dengan laju pembelajaran (*learning rate*) awal 0,001. Jika loss tidak turun dalam 10 epoch berturut-turut pada paruh kedua iterasi, diterapkan penurunan laju pembelajaran adaptif (*learning rate decay*) sebesar 10%. Pelatihan dibatasi hingga 100 epoch dengan batch size 16.

Performa diukur menggunakan akurasi deteksi (*detection accuracy rate*) dengan batas IoU $\ge 0,5$ terhadap anotasi ground truth. Hasil evaluasi pada tiga dataset menunjukkan performa sebagai berikut:
1.  **CBIS-DDSM (2.907 mamogram):** Akurasi deteksi massa meningkat dari 85,1% (model tunggal) menjadi **95,7%** (model fusi). Akurasi deteksi kalsifikasi mengalami peningkatan sebesar **12,2%** hingga mencapai **74,4%**.
2.  **INbreast (235 mamogram FFDM):** Pendekatan fusi menghasilkan akurasi deteksi massa sebesar **98,1%** and deteksi kalsifikasi sebesar **71,8%** (atau dibulatkan menjadi 72% pada analisis teks).
3.  **Dataset Privat INCAN Meksiko (487 mamogram):** Mencapai akurasi deteksi massa sebesar **98,0%** dan kalsifikasi sebesar **73,2%**.

Sistem YOLO Fusion dengan akurasi massa **98,1%** pada INbreast terbukti mengungguli model *Single Shot Multibox Detector* (SSD) yang mencatat akurasi 89,4% dan *Faster R-CNN* (91,2%). Waktu inferensi rata-rata model fusi ini adalah 0,028 detik per citra pada GPU, menjadikannya cukup cepat untuk aplikasi diagnostik klinis instan.

## Kelebihan dan Keterbatasan
Kelebihan utama sistem YOLO Fusion terletak pada efisiensi komputasi yang tinggi sebagai detektor terpadu satu-tahap (*one-stage detector*) yang mampu melokalisasi sekaligus mengklasifikasikan lesi payudara secara langsung. Waktu inferensi yang sangat cepat (28 milidetik per citra) sangat ideal untuk diintegrasikan pada stasiun kerja klinis guna mendukung penapisan massal kanker payudara secara waktu nyata. Desain fusi keputusan threshold ganda (0,5 dan 0,35) juga merupakan solusi praktis untuk menangani perbedaan ukuran spasial antara massa dan kalsifikasi tanpa perlu merancang ulang arsitektur dasar model YOLOv3.

Namun, dari sisi rekayasa, model ini memiliki ketergantungan penuh pada penyediaan label koordinat kotak pembatas pada data pelatihan, sehingga tidak dapat mempelajari fitur secara mandiri hanya dari label diagnosis tingkat citra (*image-level label*). Secara konseptual, sistem ini terbatas sebagai alat pendeteksi keberadaan objek abnormal dan belum mencakup modul segmentasi kontur lesi secara halus serta bi-klasifikasi tingkat histopatologi (jinak vs. ganas). Keterbatasan lain terlihat pada rendahnya akurasi deteksi kalsifikasi yang berada pada kisaran 71% hingga 74% akibat dimensi mikro-kalsifikasi yang sangat halus dan mudah tersamarkan oleh noise citra.

## Kaitan dengan Bab Lain
Bab ini memiliki hubungan silsilah yang sangat erat dengan perkembangan aplikasi detektor satu-tahap berbasis YOLO dalam domain medis. Metode pelokalisasian-klasifikasi terpadu pada bab ini mewarisi kerangka berpikir sistem CAD yang dirancang oleh Al-Antari dkk. pada [Bab 129](./129%20-%202021%20-%20COVID-19%20CAD%20dari%20X-Ray%20%28Al-Antari%20dkk.%29%20-%20Medis.md) untuk deteksi lesi paru akibat infeksi COVID-19 pada citra rontgen dada digital. Perbedaannya, Al-Antari dkk. menggunakan YOLOv2 (Darknet-19) dengan skala deteksi tunggal, sedangkan bab ini menggunakan YOLOv3 (Darknet-53) yang mengekstrak fitur pada tiga skala grid berbeda untuk menangani variasi spasial yang ekstrem pada mamogram.

Di sisi lain, bab ini terhubung langsung dengan [Bab 131](./131%20-%202022%20-%20Breast%20Tumor%20Detection%20%28Modified%20YOLOv5%29%20-%20Medis.md) (Mohiyuddin dkk., 2022) yang menguji deteksi tumor payudara pada dataset publik CBIS-DDSM yang sama. Jika bab ini menggunakan pendekatan fusi keputusan multi-model YOLOv3, Mohiyuddin dkk. pada [Bab 131](./131%20-%202022%20-%20Breast%20Tumor%20Detection%20%28Modified%20YOLOv5%29%20-%20Medis.md) memilih modifikasi struktural dengan menyederhanakan arsitektur *BottleneckCSP* YOLOv5 menjadi *BottleneckCSP-new* untuk memotong beban parameter. Perlu dicatat juga bahwa penelitian di Bab 130 ini datanya terverifikasi secara sahih, sedangkan artikel pada [Bab 131](./131%20-%202022%20-%20Breast%20Tumor%20Detection%20%28Modified%20YOLOv5%29%20-%20Medis.md) telah resmi mengalami retraksi pada tahun 2023 akibat manipulasi penelaahan sejawat.

Konteks klinis yang lebih luas dari integrasi YOLO pada deteksi lesi organ tubuh lainnya, seperti polip kolorektal pada video kolonoskopi di [Bab 132](./132%20-%202023%20-%20YOLO%20untuk%20Deteksi%20Polip%20%28Wan%20dkk.%29%20-%20Medis.md), dirangkum dalam tinjauan komprehensif pada [Bab 128](./128%20-%202024%20-%20Systematic%20Review%20YOLO%20Medis%20%28Qureshi%20dkk.%29%20-%20Medis.md).

## Poin untuk Sitasi
*   **Kunci BibTeX:** `baccouche2021breast`
*   **Ringkasan untuk Tinjauan Pustaka:** Baccouche dkk. (2021) mengusulkan sistem diagnosis kanker payudara berbantuan komputer (CAD) menggunakan pendekatan fusi keputusan tingkat model YOLOv3. Metode ini mampu mendeteksi lesi massa dan kalsifikasi secara simultan dengan akurasi deteksi massa sebesar 95,7% pada CBIS-DDSM dan 98,1% pada INbreast dengan waktu inferensi 28 milidetik per citra.
*   **Catatan Verifikasi:** Hasil akurasi kalsifikasi (71,8%-74,4%) telah diverifikasi dari tabel performa naskah asli. Pengukuran waktu inferensi diuji pada konfigurasi GPU tunggal yang tercantum di bagian rincian eksperimen.
