# 172 - Efficient Multi-Task RGB-D Scene Analysis for Indoor Environments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `seichter2022emsanet` |
| Judul asli | Efficient Multi-Task RGB-D Scene Analysis for Indoor Environments |
| Penulis | Daniel Seichter, Söhnke Benedikt Fischedick, Mona Köhler, Horst-Michael Gross |
| Tahun | 2022 |
| Venue | International Joint Conference on Neural Networks (IJCNN 2022) |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2207.04526
- **Kode sumber resmi:** https://github.com/TUI-NICR/EMSANet
- **Google Scholar:** https://scholar.google.com/scholar?q=Efficient%20Multi-Task%20RGB-D%20Scene%20Analysis%20for%20Indoor%20Environments

## Gambaran Umum

Makalah ini memperkenalkan EMSANet (*Efficient Multi-Task Scene Analysis Network*), satu jaringan saraf yang menyelesaikan lima tugas analisis *scene* (pemahaman ruangan) indoor sekaligus dari masukan RGB-D (citra warna disertai peta kedalaman): segmentasi semantik, segmentasi instans, segmentasi panoptik, estimasi orientasi instans, dan klasifikasi *scene*. Kelima keluaran dihasilkan dalam satu kali lintasan maju (*forward pass*) melalui *encoder* (bagian jaringan yang mengekstrak fitur) RGB-D yang dibagi bersama, bukan oleh lima jaringan terpisah.

Klaim utama makalah adalah bahwa penggabungan tugas ini tidak mengorbankan akurasi dibandingkan model satu-tugas sejenis, sementara kecepatan tetap layak untuk agen bergerak berdaya baterai terbatas. Pada perangkat *embedded* NVIDIA Jetson AGX Xavier dengan TensorRT dan presisi *float16*, EMSANet dilaporkan berjalan pada 24,5 *frame* per detik (FPS) tanpa pascapemrosesan. Makalah ini adalah perluasan langsung dari ESANet (Seichter dkk., 2021), pendahulunya yang hanya menangani segmentasi semantik.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Agen bergerak — misalnya robot layanan indoor — membutuhkan pemahaman *scene* yang lebih kaya daripada sekadar label kelas per piksel. Untuk menavigasi dan berinteraksi dengan aman, robot perlu mengetahui batas antarobjek individual (bukan hanya kelasnya), arah hadap objek tersebut (misalnya ke arah mana seseorang menghadap), dan kategori ruangan yang sedang dimasuki. Ketiga jenis informasi ini secara konvensional dihasilkan oleh jaringan terpisah: satu untuk segmentasi semantik, satu untuk deteksi/segmentasi instans, satu lagi untuk estimasi orientasi, dan satu lagi untuk klasifikasi *scene*.

Menjalankan empat atau lima jaringan terpisah pada satu perangkat mahal secara komputasi. Setiap jaringan memiliki *encoder*-nya sendiri yang mengekstrak fitur dari citra masukan, padahal fitur tingkat rendah dan menengah (tepi, tekstur, bentuk kasar) sebagian besar sama-sama berguna untuk semua tugas tersebut. Duplikasi ini memboroskan memori dan waktu komputasi, sesuatu yang tidak dapat ditoleransi pada platform bergerak dengan anggaran daya dan kalkulasi terbatas. Masalah kedua adalah interferensi antartugas: menggabungkan tugas dalam satu jaringan tanpa desain yang tepat dapat membuat kinerja tiap tugas justru menurun dibandingkan model khusus tugas tunggal. Pendahulu langsung pekerjaan ini, ESANet, sudah menunjukkan bahwa segmentasi semantik RGB-D dapat dibuat efisien dan *real-time* lewat *encoder* ganda yang ringan dan mekanisme fusi berbasis atensi, tetapi ESANet hanya menyelesaikan satu tugas.

## Ide Utama

Gagasan inti EMSANet adalah membagi satu pasang *encoder* RGB-D untuk seluruh tugas, lalu mencabangkan hasilnya ke beberapa kepala (*head*) dekoder khusus tugas. Fitur tingkat rendah dan menengah yang diekstrak dari citra warna dan peta kedalaman bersifat umum: tepi objek, tekstur permukaan, dan bentuk kasar berguna baik untuk menentukan kelas piksel maupun untuk memisahkan instans individual atau mengenali kategori ruangan. Dengan membagi fitur ini, biaya komputasi *encoder* dikeluarkan satu kali, sedangkan setiap kepala tugas hanya menambah beban komputasi kecil di lapisan dekoder.

Konsekuensinya, jaringan menerima satu pasang citra RGB dan peta kedalaman sebagai masukan, lalu mengeluarkan lima jenis keluaran sekaligus: peta label kelas per piksel (segmentasi semantik), pemisahan tiap objek individual (segmentasi instans), gabungan keduanya menjadi satu peta yang melabeli setiap piksel dengan kelas sekaligus identitas instansnya (segmentasi panoptik), sudut hadap tiap instans yang terdeteksi (estimasi orientasi), dan satu label kategori untuk seluruh *scene* (misalnya "dapur" atau "ruang tamu").

## Cara Kerja Langkah demi Langkah

### Encoder Ganda RGB dan Depth

EMSANet memakai dua *encoder* terpisah dengan arsitektur dasar ResNet34, satu menerima citra RGB dan satu lagi menerima peta kedalaman (dinormalisasi menjadi citra satu kanal). Blok konvolusi standar ResNet diganti dengan blok *Non-Bottleneck-1D* (NBt1D), warisan dari ESANet: konvolusi 3×3 difaktorkan secara spasial menjadi dua konvolusi berurutan 3×1 dan 1×3. Faktorisasi ini menurunkan jumlah parameter dan operasi hitung per lapisan tanpa mengubah ukuran wilayah reseptif (area citra masukan yang memengaruhi satu unit fitur keluaran), sehingga *encoder* tetap ringan untuk perangkat *embedded*.

### Fusi RGB-Depth Berbasis Atensi

Pada setiap tahap resolusi di dalam kedua *encoder*, fitur dari cabang *depth* digabungkan ke cabang RGB memakai mekanisme atensi bergaya *Squeeze-and-Excitation* (SE): fitur dipadatkan menjadi vektor ringkasan per kanal, vektor itu dipetakan menjadi bobot kepentingan per kanal, lalu fitur asli dikalikan dengan bobot tersebut sebelum dijumlahkan ke cabang RGB. Dengan cara ini, kanal fitur kedalaman yang informatif untuk konteks tertentu diperkuat, sedangkan kanal yang kurang relevan ditekan. Fusi dilakukan berulang pada tiap tahap resolusi, bukan hanya sekali di akhir *encoder*, sehingga informasi geometris dari peta kedalaman ikut membentuk representasi RGB pada semua skala fitur.

### Modul Konteks dan Dekoder Bersama

Keluaran gabungan dari *encoder* diteruskan ke modul konteks yang memperluas wilayah reseptif sebelum masuk ke dekoder — komponen yang memulihkan resolusi spasial dari fitur terkompresi. Dekoder inti ini dipakai bersama sebagai tulang punggung sebelum bercabang ke kepala-kepala khusus tugas.

### Percabangan ke Lima Kepala Tugas

Dari titik percabangan tersebut, jaringan memiliki jalur terpisah untuk tiap tugas: satu jalur memprediksi label kelas per piksel (segmentasi semantik); satu jalur memprediksi peta pusat instans dan vektor offset untuk mengelompokkan piksel menjadi instans individual (segmentasi instans, mengikuti pendekatan berbasis pusat mirip Panoptic-DeepLab); satu jalur menambahkan estimasi sudut orientasi untuk tiap instans yang ditemukan; satu jalur lagi memakai fitur global (hasil *pooling* menyeluruh) untuk memprediksi satu label kategori *scene*. Segmentasi panoptik diperoleh dengan menggabungkan keluaran segmentasi semantik dan segmentasi instans secara langsung, tanpa jaringan tambahan.

Diagram berikut merangkum alur data dari masukan hingga lima keluaran:

```
RGB ──► encoder RGB (ResNet34-NBt1D) ─┐
                                       ├─ fusi SE per-tahap ─► modul konteks
Depth ─► encoder depth (ResNet34-NBt1D)┘                         │
                                                                   ▼
                                                          dekoder bersama
                                                                   │
                      ┌───────────────┬───────────────┬───────────┼──────────────┐
                      ▼               ▼               ▼           ▼              ▼
                 segmentasi      segmentasi       orientasi   segmentasi    klasifikasi
                 semantik        instans          instans     panoptik*     scene
                                                               (*gabungan semantik+instans)
```

### Pelatihan Multitugas

Karena kelima kepala tugas dilatih bersamaan, fungsi *loss* total merupakan jumlah tertimbang dari *loss* tiap tugas (galat klasifikasi piksel, galat regresi pusat/offset instans, galat sudut orientasi, galat klasifikasi *scene*). Pembobotan ini menentukan seberapa besar tiap tugas memengaruhi arah pembaruan bobot bersama di *encoder*; bila salah satu tugas diberi bobot terlalu besar, tugas lain cenderung dirugikan.

## Eksperimen dan Hasil

Evaluasi dilakukan pada NYUv2 dan SUNRGB-D, dua tolok ukur standar untuk segmentasi *scene* indoor RGB-D, yang diperluas oleh penulis dengan anotasi instans dan orientasi tambahan karena anotasi bawaan kedua dataset itu tidak mencakup tugas-tugas tersebut. Pada NYUv2, EMSANet mencapai mIoU (*mean Intersection over Union*, metrik rata-rata kesesuaian area prediksi terhadap area kebenaran untuk segmentasi semantik) sebesar 50,97% tanpa praperlatihan tambahan, meningkat menjadi 53,34% ketika model dipraperlatih pada dataset sintetis Hypersim sebelum disetel halus (*fine-tuning*) pada NYUv2. Untuk segmentasi panoptik, model mencapai *Panoptic Quality* (PQ, metrik gabungan yang menilai ketepatan segmentasi dan pengenalan instans sekaligus) sebesar 43,56%. Estimasi orientasi diukur dengan *Mean Absolute Angle Error* (MAAE, rata-rata selisih sudut mutlak antara orientasi prediksi dan kebenaran) sebesar 16,38 derajat, sedangkan klasifikasi *scene* mencapai akurasi seimbang (*balanced accuracy*) 76,46%.

Interpretasinya: angka mIoU 50,97–53,34% berada pada kisaran yang sebanding dengan ESANet (mIoU 50,30% pada NYUv2), pendahulunya yang hanya menangani satu tugas — menunjukkan bahwa penambahan empat tugas lain tidak menurunkan kualitas segmentasi semantik secara berarti. Kecepatan 24,5 FPS pada Jetson AGX Xavier dengan TensorRT presisi *float16* berada sedikit di bawah 29,7 FPS yang dicapai ESANet pada perangkat yang sama untuk segmentasi tunggal, konsisten dengan tambahan beban komputasi dari empat kepala tugas ekstra, tetapi masih berada pada rentang yang dapat disebut *real-time* untuk aplikasi robotika indoor.

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini adalah pembuktian bahwa lima tugas analisis *scene* dapat digabungkan dalam satu jaringan dengan satu *encoder* bersama tanpa penurunan akurasi berarti dibandingkan model satu-tugas, sambil tetap mempertahankan kecepatan mendekati *real-time* pada perangkat *embedded*. Desain fusi berbasis atensi yang diwarisi dari ESANet menghindari pencampuran fitur RGB dan *depth* secara naif (misalnya penjumlahan langsung tanpa pembobotan), sehingga kontribusi tiap modalitas dapat disesuaikan menurut konteks. Ketersediaan kode sumber resmi di repositori TUI-NICR memudahkan reproduksi dan perbandingan oleh kelompok riset lain.

Dari sisi rekayasa, pembobotan *loss* multitugas tetap merupakan hiperparameter yang harus disetel secara empiris; makalah tidak menjelaskan aturan umum untuk menentukan bobot optimal pada dataset atau kombinasi tugas lain di luar NYUv2/SUNRGB-D. Secara konseptual, ketergantungan pada peta kedalaman berarti kinerja jaringan berkurang pada kondisi sensor kedalaman kurang andal, misalnya di bawah cahaya matahari langsung yang mengganggu sensor kedalaman aktif berbasis inframerah. Evaluasi juga terbatas pada *scene* indoor; generalisasi ke lingkungan luar ruangan tidak dieksplorasi dalam makalah ini.

## Kaitan dengan Bab Lain

EMSANet adalah kelanjutan langsung ESANet (Seichter dkk., 2021), yang memperkenalkan *encoder* ganda NBt1D dan fusi berbasis atensi untuk segmentasi semantik RGB-D tunggal; bab ini mewarisi seluruh mekanisme *encoder-fusi* tersebut dan menambahkan empat tugas baru di atasnya. Dalam klaster Segmentasi RGB-D pada tinjauan ini, bab ini berdampingan dengan [171 - SegFormer](./171%20-%202021%20-%20SegFormer%20-%20Segmentasi%20RGB-D.md), yang menyelesaikan segmentasi semantik memakai arsitektur *transformer* tanpa modalitas kedalaman eksplisit — berbeda dari EMSANet yang secara khusus memakai dua *encoder* RGB dan *depth* terpisah. Bab [173 - GeminiFusion](./173%20-%202024%20-%20GeminiFusion%20-%20Segmentasi%20RGB-D.md) mengangkat tema fusi RGB-D lanjutan berbasis *transformer*, dapat dibandingkan langsung dengan mekanisme fusi SE pada bab ini. Bab [174 - Omnivore](./174%20-%202022%20-%20Omnivore%20-%20Segmentasi%20RGB-D.md) mengangkat pendekatan satu jaringan untuk banyak modalitas visual sekaligus, sejalan secara konseptual dengan prinsip berbagi representasi yang dipakai EMSANet untuk banyak tugas.

Kedua dataset yang dipakai untuk evaluasi memiliki bab tersendiri dalam tinjauan ini: [141 - NYU Depth v2](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md), dataset indoor RGB-D klasik yang menjadi tolok ukur utama, dan [142 - SUN RGB-D](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md), dataset indoor berskala lebih besar yang juga dipakai untuk validasi silang hasil segmentasi.

## Poin untuk Sitasi

Kutip dengan kunci `seichter2022emsanet`. Ringkasan yang aman dikutip: "EMSANet menyelesaikan segmentasi semantik, segmentasi instans, segmentasi panoptik, estimasi orientasi instans, dan klasifikasi *scene* dalam satu jaringan RGB-D yang berbagi *encoder*, mencapai mIoU 50,97–53,34% pada NYUv2 dan kecepatan 24,5 FPS pada Jetson AGX Xavier dengan TensorRT *float16*." Angka PQ 43,56%, MAAE 16,38°, dan akurasi seimbang klasifikasi *scene* 76,46% diperoleh dari halaman proyek dan ringkasan pihak ketiga, bukan dari pembacaan langsung tabel PDF resmi — sebaiknya diverifikasi ulang ke naskah IJCNN/arXiv sebelum dikutip dalam karya formal. Perbandingan kecepatan dengan ESANet (29,7 FPS pada perangkat sama) juga sebaiknya dicek ulang ke kedua makalah aslinya.
