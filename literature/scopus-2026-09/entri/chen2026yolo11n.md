# YOLO11n-DRE: A METHOD FOR MATURITY DETECTION AND ACCURATE COUNTING OF SINGLE TRUSS TOMATO FRUITS IN COMPLEX UNSTRUCTURED ENVIRONMENTS

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2026yolo11n` |
| Judul asli | YOLO11n-DRE: A METHOD FOR MATURITY DETECTION AND ACCURATE COUNTING OF SINGLE TRUSS TOMATO FRUITS IN COMPLEX UNSTRUCTURED ENVIRONMENTS |
| Penulis | Chen, Baofan; Hao, Yuhao; Chen, Bingjun; Cui, Shuaishuai; Yan, Yaqi; Song, Guozhu |
| Tahun | 2026 |
| Venue | Inmateh Agricultural Engineering |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [chen2026yolo11n.pdf](../pdf/chen2026yolo11n.pdf)
- DOI resmi: https://doi.org/10.35633/inmateh-78-03

## Gambaran Umum

Penelitian ini mengatasi deteksi kematangan dan penghitungan buah tomat tandan (*truss tomato*) secara langsung di lingkungan rumah kaca yang tidak terstruktur. Informasi jumlah buah dan sebaran kematangan menjadi dasar penjadwalan panen, prediksi hasil, dan pengambilan keputusan otomatis. Buah pada satu tandan masak tidak bersamaan, sehingga panen terlalu awal meningkatkan bagian buah mentah dan menurunkan nilai jual, sedangkan panen terlambat menyebabkan kerusakan mekanis dan risiko penyakit pascapanen. Penghitungan manual memakan tenaga, tidak efisien, dan rawan kesalahan subjektif. Penulis menyatakan detektor yang ada cenderung mengenali seluruh tandan, sehingga pada area padat mudah terjadi deteksi terlewat maupun ganda karena buah berukuran kecil, rapat, saling menempel, dan saling menutupi. Tujuan penelitian ini adalah meningkatkan kemampuan model ringan YOLO11n dalam membedakan buah individual pada kelas kematangan yang padat dan terhalang, lalu mengubah keluaran deteksi menjadi data hasil panen.

Data dikumpulkan di Nonggu Tomato Town, Distrik Taigu, Kota Jinzhong, Provinsi Shanxi, Tiongkok, dari Januari 2024 sampai Oktober 2025. Citra diambil dengan kamera belakang ponsel beresolusi 2778 × 1284 piksel dan 12 megapiksel serta lensa telefoto 77 mm, pada berbagai sudut, jarak, dan kondisi cahaya, termasuk cuaca cerah, berawan, mendung, oklusi, dan tandan rapat. Dataset berisi 2.785 citra yang dibagi menjadi 1.948 citra latih, 558 citra validasi, dan 279 citra uji dengan rasio 7:2:1. Anotasi kotak pembatas dilakukan dengan LabelImg dan menghasilkan 62.673 buah, terdiri atas 18.373 hijau (mentah), 9.173 oranye (transisi), dan 35.127 merah (matang). Setiap anotasi ditulis sebagai L = (c, x, y, w, h), dengan c sebagai kelas kematangan serta x, y, w, h sebagai koordinat dan ukuran kotak yang ternormalisasi. Pelatihan memakai Xeon Platinum 8470Q 25 vCPU, NVIDIA RTX 5090 32 GB, Ubuntu 22.04.3, Python 3.11.14, dan CUDA 12.8.

Mekanisme deteksi memodifikasi YOLO11n menjadi YOLO11n-DRE melalui lima perubahan yang saling melengkapi. Pada *backbone*, modul C3k2 diganti dengan C3k2_EMA yang menyisipkan *Efficient Multi-Scale Attention* pada tahap dangkal dan menengah untuk menekan derau latar tanpa mengubah resolusi fitur. *Neck* diperluas hingga lapisan P2 dengan langkah 4, membentuk rantai transfer P5→P4→P3→P2 agar detail geometri target sangat kecil tidak hilang akibat penurunan sampel berulang. Pada jalur P3→P2, operator *nearest-neighbor* diganti dengan DySample yang melakukan interpolasi dan penyusunan ulang fitur secara dinamis sesuai kandungan lokal citra. Modul *Pre-Head Refinement* berbasis EMA dipasang pada cabang P2 dan P3 untuk menyaring ulang fitur sebelum memasuki kepala deteksi. Terakhir, kepala deteksi tiga skala diganti dengan kepala empat skala yang efisien untuk P2–P5 dengan pembagian parameter yang lebih ringan. Penghitungan buah memakai tiga tahap deteksi, penyaringan, dan kuantifikasi: kotak dengan skor kepercayaan di bawah ambang τ = 0,5 dibuang, lalu jumlah buah per kelas dihitung dari kotak yang tersisa dan dibagi dengan total untuk memperoleh persentase kematangan.

Kinerja dinilai dengan presisi P = TP/(TP+FP), recall R = TP/(TP+FN), F1 = 2PR/(P+R), AP sebagai luas di bawah kurva presisi-recall, mAP, GFLOPs, jumlah parameter, dan FPS yang diukur dari rata-rata waktu selama 500 iterasi pada data uji. Tabel hasil menunjukkan YOLO11n memperoleh P 77,5%, R 79,7%, mAP@0,5 83,8%, mAP@0,5:0,95 59,4%, F1 78,6%, 6,5 GFLOPs, dan 2,6 juta parameter. YOLO11n-DRE memperoleh P 78,0%, R 80,2%, mAP@0,5 84,7%, mAP@0,5:0,95 59,2%, F1 79,2%, 6,8 GFLOPs, dan 2,38 juta parameter, dengan kecepatan 370 FPS. Dengan demikian, mAP@0,5 naik 0,9 poin persentase, mAP@0,5:0,95 turun 0,2 poin, dan parameter berkurang sekitar 8,5%. Abstrak menyebutkan kenaikan P, R, dan mAP@0,5 berturut-turut 0,65%, 0,63%, dan 1,07% serta penurunan parameter 8,5%, sehingga angka kenaikan mAP@0,5 di sana tidak sama dengan selisih pada tabel. Penulis menjelaskan penurunan kecil mAP@0,5:0,95 sebagai akibat sensitivitas IoU@0,95 terhadap pergeseran satu atau dua piksel pada target sangat kecil, dan menyatakan angka akurasi penghitungan tidak dinyatakan selain pernyataan bahwa hasilnya sangat sesuai dengan anotasi manual.

Penulis menyebutkan beberapa batasan. Cakupan dataset masih terbatas pada perbedaan varietas, struktur rumah kaca, dan kondisi pencahayaan, sehingga perlu penambahan sampel, keragaman adegan, dan strategi augmentasi yang sesuai dengan mekanisme pencitraan rumah kaca. Pada kondisi ekstrem seperti buah yang sangat menempel, oklusi parah, dan batas yang kabur, deteksi terlewat atau penyimpangan lokasi masih mungkin terjadi dan berdampak kumulatif pada hasil penghitungan. Sistem evaluasi juga masih bertumpu pada metrik deteksi; penulis menyarankan evaluasi untuk seluruh rantai deteksi, penghitungan, estimasi hasil, dan keputusan panen, serta uji penerapan dan pengukuran latensi pada platform komputasi dengan daya berbeda.

