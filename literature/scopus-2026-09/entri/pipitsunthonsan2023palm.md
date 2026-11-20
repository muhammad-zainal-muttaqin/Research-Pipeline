# Palm bunch grading technique using a multi-input and multi-label convolutional neural network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pipitsunthonsan2023palm` |
| Judul asli | Palm bunch grading technique using a multi-input and multi-label convolutional neural network |
| Penulis | Pipitsunthonsan, Pronthep; Pan, Liangrui; Peng, Shaoliang; Khaorapapong, Thanate; Nakasathien, Sutkhet; Channumsin, Sittiporn; Chongcheawchamnan, Mitchai |
| Tahun | 2023 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C3 (Pencitraan TBS kelapa sawit) |

## Tautan Akses
- PDF: [pipitsunthonsan2023palm.pdf](../pdf/pipitsunthonsan2023palm.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2023.107864

## Gambaran Umum

Tandan buah segar (TBS) kelapa sawit merupakan bahan baku minyak sawit mentah (CPO). Mutu TBS ditentukan oleh rendemen minyak atau *oil extraction rate* (OER), tetapi penentuan harga beli di pabrik dan tengkulak masih bergantung pada penilaian pakar. Penilaian manual ini dinilai bias dan tidak andal. Metode standar pengukuran OER, yaitu ekstraksi Soxhlet, memakan waktu dan bersifat merusak, sehingga tidak sesuai untuk pengujian cepat di lokasi perdagangan. Penulis mengusulkan sistem penggolongan TBS berbasis pembelajaran mendalam yang memadukan citra dan data fisik agar penilaian menjadi lebih cepat dan konsisten.

Data dikumpulkan dari empat lokasi perdagangan. Jumlah citra seluruhnya 1.575 dan mencakup 14 varietas TBS. Sistem sensor terdiri atas kamera RGB, sensor inframerah (IR), dan *load cell* untuk menimbang tandan. Data kemudian dibagi menjadi tiga bagian: 70% untuk pelatihan, 20% untuk validasi, dan 10% untuk pengujian. Citra RGB dan IR berukuran 227 × 227 piksel, sedangkan bobot tandan dimasukkan sebagai data tambahan. Empat kelas keluaran adalah *overripe*, *ripe*, *under ripe*, dan *unripe*.

Model yang diusulkan bersifat *multi-input*, yaitu citra RGB dan IR diproses melalui blok konvolusi, lalu digabungkan dengan data bobot pada blok konkatenasi. Arsitektur ini menggunakan AlexNet dan VGG sebagai tulang punggung. Blok konvolusi terdiri atas lima sub-blok dengan jumlah filter 32, 64, 128, 256, dan 512. Lapisan terhubung penuh memiliki 1.000 kanal dengan *dropout* 50%. Keluaran *softmax* bersifat *multi-label* untuk empat kelas. Fungsi galat yang digunakan adalah *cross-entropy*. Penulis juga memakai *Gradient-weighted Class Activation Mapping* (*Grad-CAM*) untuk membandingkan area yang menjadi perhatian model pada citra asli dan citra hasil pra-pemrosesan.

Pada data uji, model mencapai akurasi 90,26%, presisi 89,86%, perolehan kembali (*recall*) 89,54%, dan skor F1 89,68%. Penulis menekankan bahwa penelitian sebelumnya umumnya hanya menguji satu varietas, sedangkan studi ini menguji 14 varietas dari empat lokasi. Angka hasil di atas merupakan ukuran kinerja penggolongan pada data uji, bukan pengukuran rendemen minyak secara langsung.

Penulis menyebutkan bahwa bobot dan citra dari berbagai varietas menjadi tantangan utama bagi metode sebelumnya, dan model ini dirancang untuk mengatasi keterbatasan tersebut. Kajian ini hanya menilai ketepatan penggolongan tingkat TBS dari satu sisi pandang kamera per tandan. Pengukuran jumlah buah, penautan antarpengamatan, dan pengukuran berbasis kedalaman tidak menjadi bagian dari studi ini.
