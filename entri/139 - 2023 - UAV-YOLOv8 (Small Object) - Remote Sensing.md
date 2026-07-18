# 139 - UAV-YOLOv8: A Small-Object-Detection Model Based on Improved YOLOv8 for UAV Aerial Photography Scenarios

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2023uavyolo` |
| Judul asli | UAV-YOLOv8: A Small-Object-Detection Model Based on Improved YOLOv8 for UAV Aerial Photography Scenarios |
| Penulis | Wang, Gang; Chen, Yanfei; An, Pei; Hong, Hanyu; Hu, Jinghu; Huang, Tiange |
| Tahun | 2023 |
| Venue | Sensors |
| Tema | Remote Sensing |

## Tautan Akses
- Cari / unduh via Google Scholar: https://scholar.google.com/scholar?q=UAV-YOLOv8%3A%20A%20Small-Object-Detection%20Model%20Based%20on%20Improved%20YOLOv8%20for%20UAV%20Aerial%20Photography%20Scenarios
- Semantic Scholar (metrik sitasi & PDF): https://www.semanticscholar.org/search?q=UAV-YOLOv8%3A%20A%20Small-Object-Detection%20Model%20Based%20on%20Improved%20YOLOv8%20for%20UAV%20Aerial%20Photography%20Scenarios&sort=relevance
- DOI Resmi: https://doi.org/10.3390/s23167190

## Gambaran Umum
UAV-YOLOv8 merupakan varian arsitektur deteksi objek satu-tahap (*single-stage detector*) yang dikembangkan untuk mengatasi rendahnya akurasi pendeteksian objek kecil pada citra udara yang diambil oleh wahana tanpa awak (*unmanned aerial vehicle* atau UAV). Model ini dimodifikasi langsung dari kerangka kerja YOLOv8s baseline dengan mengintegrasikan komponen ekstraksi fitur yang efisien dan fungsi kerugian terlokalisasi. Model ini dirancang untuk menyeimbangkan kebutuhan akurasi tinggi pada objek-objek kecil dengan efisiensi parameter agar dapat diimplementasikan pada perangkat komputasi tepi (*edge computing*).

Tiga kontribusi utama model ini meliputi penerapan mekanisme atensi *bi-level routing attention* melalui modul BiFormer, pengembangan blok pemrosesan fitur fokal bernama *Focal FasterNet block* (FFNB), serta integrasi fungsi kerugian regresi kotak pembatas *Wise-IoU* (WIoU) v3. Hasil pengujian menunjukkan peningkatan akurasi deteksi keseluruhan (*mean average precision* atau mAP) sebesar 7,7% absolut dibandingkan dengan model pembanding YOLOv8s pada dataset benchmark VisDrone2019.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Fotografi udara menggunakan UAV menghasilkan citra dengan karakteristik yang sangat berbeda dari citra horizontal standar. Objek target seperti pejalan kaki, sepeda, dan kendaraan bermotor seringkali hanya menempati area beberapa piksel saja (objek mikro di bawah 16×16 piksel) karena diambil dari ketinggian vertikal yang signifikan. Pendekatan deteksi objek standar seperti YOLOv8s sering melewatkan objek-objek kecil ini karena hilangnya resolusi spasial dan detail semantik akibat operasi konvolusi berulang di lapisan terdalam jaringan.

Selain masalah skala objek, citra udara dicirikan oleh latar belakang yang sangat padat dan kompleks, seperti vegetasi, bayangan gedung, dan pola jalan raya. Struktur tulang punggung (*backbone*) konvensional cenderung memproses seluruh area citra secara merata, sehingga menghabiskan sumber daya komputasi pada wilayah latar belakang yang tidak informatif. Di sisi lain, perangkat keras yang terpasang pada UAV (*onboard computing devices*) memiliki keterbatasan daya dan memori, sehingga metode peningkatan deteksi tidak boleh menambah beban parameter secara berlebihan. Oleh karena itu, diperlukan model yang mampu memfokuskan ekstraksi fitur pada area target kecil secara dinamis tanpa meningkatkan memori komputasi secara ekstrem.

## Ide Utama
Ide dasar UAV-YOLOv8 adalah memadukan mekanisme atensi spasial yang selektif dengan struktur konvolusi parsial yang efisien untuk memperkuat representasi spasial objek berukuran mikro. Pertama, model menyaring informasi latar belakang yang tidak relevan di dalam tulang punggung menggunakan modul atensi dinamis yang membatasi operasi pencarian kunci-nilai (*query-key*) hanya pada wilayah yang menjanjikan. Kedua, jaringan menggunakan konvolusi parsial untuk menghemat operasi komputasi mubazir di bagian leher (*neck*), serta menambahkan cabang deteksi resolusi tinggi khusus untuk memproses peta fitur beresolusi tinggi (subsampling 4x). Terakhir, untuk menangani ketidakakuratan pelabelan spasial pada objek kecil, model dilatih dengan fungsi kerugian regresi yang secara adaptif menyesuaikan gradien pembaruan berdasarkan kualitas sampel prediksi.

## Cara Kerja Langkah demi Langkah
UAV-YOLOv8 memodifikasi arsitektur YOLOv8s standar pada tiga komponen utama: tulang punggung untuk penyaringan atensi, leher untuk fusi fitur multiskala, dan kepala deteksi untuk pemrosesan skala resolusi tinggi. Alur kerja dan mekanisme dari setiap modifikasi tersebut dijabarkan sebagai berikut:

### 1. Struktur Modul BiFormer Attention
Mekanisme *bi-level routing attention* (BRA) diintegrasikan ke dalam tulang punggung YOLOv8s untuk menyaring gangguan latar belakang. BRA membagi peta fitur berukuran $H \times W$ menjadi grid wilayah yang berisi $S \times S$ sel. Pertama, modul ini menghitung nilai rata-rata dari setiap wilayah untuk membangun graf relasi wilayah. Relasi ini digunakan untuk menyaring wilayah yang tidak relevan, sehingga hanya wilayah-wilayah dengan nilai keterkaitan tertinggi (top-$k$) yang akan dialirkan (*routed*) untuk perhitungan atensi detail pada tingkat piksel. 

Untuk citra input beresolusi 640×640 piksel, pembagian wilayah ini mengurangi kompleksitas komputasi dari $O((HW)^2)$ pada self-attention standar menjadi $O(HW \cdot S^2)$ yang bersifat linear terhadap ukuran citra. Mekanisme ini membatasi operasi pemrosesan fitur hanya pada area yang berpotensi memuat objek kecil.

### 2. Desain Focal FasterNet Block (FFNB)
Untuk meningkatkan efisiensi pemrosesan fitur pada leher jaringan, modul C2f standar digantikan oleh *Focal FasterNet block* (FFNB). Blok ini mengadopsi konsep *partial convolution* (PConv) dari arsitektur FasterNet. PConv hanya menerapkan konvolusi standar 3×3 pada sebagian kecil saluran input ($c_p = 1/4$ dari total saluran $c$), sementara saluran sisanya ($3/4 \cdot c$) dilewatkan langsung tanpa melalui komputasi konvolusi. 

Hal ini meminimalkan akses memori dan operasi floating-point yang mubazir. FFNB memodifikasi struktur ini dengan menambahkan operasi pembobotan fokal (*focal weighting*) pada luaran PConv untuk menonjolkan fitur tepi dan detail objek kecil sebelum digabungkan kembali dengan saluran yang dilewatkan langsung.

### 3. Penambahan Skala Deteksi Resolusi Tinggi (P2 Head)
YOLOv8 standar menghasilkan prediksi pada tiga skala (subsampling 8x, 16x, dan 32x). Pada citra input 640×640 piksel, resolusi spasial terkecil pada kepala deteksi adalah 20×20 piksel (P5), yang tidak lagi memuat detail geometris objek berukuran di bawah 10 piksel. UAV-YOLOv8 menambahkan kepala deteksi keempat (P2) dengan subsampling 4x, menghasilkan peta fitur beresolusi 160×160 piksel. Kepala prediksi P2 ini digabungkan secara lateral dengan fitur dangkal dari tulang punggung menggunakan jaringan fusi fitur dua-arah (*bidirectional feature pyramid network* atau BiFPN) untuk meminimalkan hilangnya resolusi spasial objek mikro.

```
       [ Citra Input ]
              │
              ▼
   ┌─────────────────────┐
   │ Backbone (YOLOv8)   │
   │  - P1, P2           │
   │  - BiFormer Attn    ├────────┐ (Fitur Dangkal/Mikro)
   │  - P3, P4, P5       │        │
   └──────────┬──────────┘        │
              │                   ▼
              │        ┌─────────────────────┐
              │        │  Neck (FFNB Fusi)   │
              │        │   - Integrasi P2    │
              │        │   - Modul FFNB      │
              ▼        └──────────┬──────────┘
   ┌─────────────────────┐        │
   │    PANet (Neck)     │◄───────┘
   │   (Fusi Fitur)      │
   └──────────┬──────────┘
              ▼
   ┌─────────────────────────────────────────────────────────┐
   │                 Multi-Scale Detect Head                 │
   │  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐  │
   │  │ Head (P2) │ │ Head (P3) │ │ Head (P4) │ │ Head (P5) │  │
   │  └─────┬─────┘ └─────┬─────┘ └─────┬─────┘ └─────┬─────┘  │
   └────────┼─────────────┼─────────────┼─────────────┼──────┘
            ▼             ▼             ▼             ▼
        [Objek Mikro] [Objek Kecil] [Objek Sedang] [Objek Besar]
                     (Loss Regresi: WIoU v3)
```

### 4. Optimalisasi dengan Wise-IoU (WIoU) v3
Kotak pembatas (*bounding box*) objek kecil sangat rentan terhadap bias pelabelan manual (*ground truth labeling noise*) pada citra udara. Fungsi kerugian regresi biasa seperti CIoU memberikan penalti gradien yang besar untuk prediksi yang sangat menyimpang, sekalipun penyimpangan tersebut disebabkan oleh kesalahan label luar (*outlier*). WIoU v3 memperkenalkan faktor gain non-monotonik dinamis yang menghitung rasio deviasi relatif (*outlierness*) dari sampel prediksi. 

Untuk prediksi dengan kualitas rata-rata, model memberikan gain gradien yang tinggi. Namun, untuk kotak prediksi yang menyimpang ekstrem (sampel berkualitas sangat buruk), gain diturunkan untuk melindungi stabilitas konvergensi model selama pelatihan.

## Eksperimen dan Hasil
Model UAV-YOLOv8 dievaluasi pada dataset udara VisDrone2019-DET yang mencakup skenario lalu lintas perkotaan dan jalan raya padat yang ditangkap oleh drone di berbagai wilayah. Perbandingan hasil mAP@0.5 antara model baseline YOLOv8s dengan model usulan (Ours) disajikan dalam tabel berikut:

| Model | Pedestrian | People | Bicycle | Car | Van | Truck | Tricycle | Awning-Tricycle | Bus | Motor | mAP@0.5 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **YOLOv8s** | 42,7 | 32,0 | 12,4 | 79,1 | 44,0 | 36,5 | 28,1 | 15,9 | 57,0 | 44,9 | 39,3 |
| **Ours** | **56,8** | **44,9** | **18,8** | **85,8** | **50,8** | **39,0** | **33,3** | **19,7** | **64,3** | **56,2** | **47,0** |

Penggantian modul ekstraksi fitur dan penambahan kepala P2 meningkatkan performa deteksi mAP@0.5 secara keseluruhan dari 39,3% menjadi 47,0% (+7,7%). Keuntungan terbesar tercatat pada objek-objek kecil dengan aspek rasio yang ramping seperti pejalan kaki (*pedestrian*, meningkat +14,1%), orang (*people*, meningkat +12,9%), dan sepeda motor (*motor*, meningkat +11,3%). Kategori kendaraan besar seperti truk (*truck*) hanya meningkat sebesar 2,5% karena fitur kendaraan besar sudah terwakili dengan cukup baik oleh kepala prediksi standar P4 dan P5.

Selain itu, model Ours (UAV-YOLOv8s) dibandingkan dengan model YOLOv8l yang memiliki struktur jauh lebih berat di tingkat parameter. YOLOv8l menghasilkan Precision sebesar 57,5%, Recall 44,3%, mAP@0.5 46,5%, dan mAP@0.5:0.95 28,7%. Sebagai perbandingan, Ours (UAV-YOLOv8s) mencapai Precision 54,4%, Recall 45,6%, mAP@0.5 47,0%, dan mAP@0.5:0.95 29,2%. Hasil ini membuktikan bahwa modifikasi arsitektur yang dirancang khusus untuk domain udara mampu memberikan performa deteksi objek kecil yang lebih unggul dibandingkan dengan meningkatkan kapasitas model secara naif.

## Kelebihan dan Keterbatasan
Dari sisi rekayasa arsitektur, keunggulan utama UAV-YOLOv8s terletak pada kemampuannya meningkatkan sensitivitas terhadap objek mikro tanpa mengalami pembengkakan parameter model yang signifikan. Integrasi *Partial Convolution* pada blok FFNB terbukti menjaga efisiensi akses memori, sementara fungsi kerugian WIoU v3 mencegah ketidakstabilan latih akibat noise label yang jamak ditemui pada dataset UAV resolusi rendah. Peningkatan akurasi pada kategori dengan skala terkecil seperti pejalan kaki membuktikan bahwa model ini cocok untuk diimplementasikan pada sistem pengawasan lalu lintas udara real-time.

Namun demikian, secara konseptual, model ini masih memiliki beberapa keterbatasan. Penambahan kepala deteksi keempat (P2) pada resolusi 160×160 piksel menuntut alokasi memori grafis yang lebih tinggi pada tahap leher jaringan selama fase inferensi. Hal ini dapat menurunkan laju bingkai per detik (*frame rate*) jika diimplementasikan pada komputer tepi (*edge device*) berdaya sangat rendah tanpa optimasi kuantisasi bobot tambahan. Selain itu, model ini hanya dievaluasi pada citra RGB standar dan belum teruji pada domain citra inframerah (*thermal imagery*) yang sering digunakan pada misi penyelamatan malam hari oleh drone.

## Kaitan dengan Bab Lain
UAV-YOLOv8s merupakan kelanjutan evolusioner dari teknik penginderaan jauh berbasis pembelajaran mendalam (*deep learning*) yang dibahas pada bab-bab sebelumnya. Kerangka kerja ini secara langsung mewarisi gagasan adaptasi arsitektur deteksi untuk wahana udara yang dipelopori oleh model [137 - 2021 - TPH-YOLOv5 (Drone Detection) - Remote Sensing](./137%20-%202021%20-%20TPH-YOLOv5%20%28Drone%20Detection%29%20-%20Remote%20Sensing.md). Perbedaannya, jika TPH-YOLOv5 menambahkan kepala prediksi berbasis *Transformer* yang mahal secara komputasi, UAV-YOLOv8s memilih pendekatan atensi dinamis sparse (*dynamic sparse attention*) lewat BiFormer dan konvolusi parsial.

Selain itu, masalah variabilitas skala besar yang diselesaikan oleh model ini berkaitan erat dengan penelitian [138 - 2019 - Robust CNN High-Res Remote Sensing (Zhang dkk.) - Remote Sensing](./138%20-%202019%20-%20Robust%20CNN%20High-Res%20Remote%20Sensing%20%28Zhang%20dkk.%29%20-%20Remote%20Sensing.md) yang berfokus pada ketahanan ekstraksi fitur CNN di bawah variasi resolusi spasial citra satelit. Dari sudut pandang penanganan objek mikro tanpa menurunkan kecepatan deteksi secara ekstrem, model ini menawarkan alternatif arsitektur yang lebih terpadu dibandingkan dengan pendekatan pemotongan citra dinamis yang diperkenalkan dalam [140 - 2018 - YOLT (Satellite Imagery) - Remote Sensing](./140%20-%202018%20-%20YOLT%20%28Satellite%20Imagery%29%20-%20Remote%20Sensing.md), di mana YOLT mengandalkan pemrosesan ubin gambar (*tiling*) secara serial yang membutuhkan waktu komputasi linier terhadap jumlah ubin.

## Poin untuk Sitasi
Kunci BibTeX: `wang2023uavyolo`

Kutipan Tinjauan Pustaka:
> Wang dkk. (2023) memperkenalkan UAV-YOLOv8, sebuah model deteksi objek mikro untuk citra udara UAV yang mengintegrasikan mekanisme atensi dinamis BiFormer dan blok konvolusi parsial Focal FasterNet Block (FFNB). Model ini memperluas kepala prediksi menjadi empat skala (termasuk cabang P2) dan dioptimalkan dengan fungsi kerugian Wise-IoU (WIoU) v3, mencapai peningkatan mAP@0.5 sebesar 7,7% absolut dibandingkan baseline YOLOv8s pada dataset VisDrone2019.

Catatan untuk Verifikasi:
Klaim performa mAP@0.5 sebesar 47,0% dan peningkatan kategori pejalan kaki di atas 10% telah diperoleh dari data eksperimen primer pada dataset VisDrone2019-DET dalam naskah asli (Sensors 2023, Vol. 23, No. 16, Halaman 7190).
