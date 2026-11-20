# Real-Time Pear Fruit Detection and Counting Using YOLOv4 Models and Deep SORT

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `parico2023real` |
| Judul asli | Real-Time Pear Fruit Detection and Counting Using YOLOv4 Models and Deep SORT |
| Penulis | Parico, Addie Ira Borja; Ahamed, Tofael |
| Tahun | 2023 |
| Venue | Iot and AI in Agriculture Self Sufficiency in Food Production to Achieve Society 5 0 and Sdgs Globally |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | pear |

## Tautan Akses
- PDF: [parico2023real.pdf](../pdf/parico2023real.pdf)
- DOI resmi: https://doi.org/10.1007/978-981-19-8113-5_11

## Gambaran Umum

Studi ini membandingkan beberapa varian detektor objek YOLOv4 untuk mengenali buah pir pada video kebun, lalu menghitung jumlah buah dengan cara menghubungkan buah yang sama antarbingkai (frame). Data dikumpulkan di kebun pir gabungan (joint-tree) seluas 0,15 ha menggunakan kamera ponsel, dan hanya memakai citra RGB. Hasil utama: YOLOv4-CSP dinilai model paling baik untuk akurasi deteksi, dengan AP@0,50 sebesar 98%. YOLOv4-tiny dinilai model paling ideal untuk kecepatan, dengan lebih dari 50 FPS. Untuk penghitungan, metode ID unik memberi F1count 87,85%.

Kamera ponsel 16 MP merekam video 1920 × 1080 selama 32 detik pada 30 FPS. Untuk video 30 FPS, satu bingkai diambil setiap 15 bingkai. Studi ini memakai 314 citra beresolusi 4K. Karena kebun hanya 0,15 ha, jumlah pohon dan buah dalam satu rekaman terbatas, sehingga angka penghitungan belum tentu berlaku untuk kebun yang lebih luas atau kondisi pencahayaan lain.

Pembanding utamanya adalah YOLOv4, YOLOv4-tiny, dan YOLOv4-CSP. Kriteria yang dipakai penulis ada dua: akurasi deteksi dan kecepatan mendekati waktu nyata, yaitu minimal 24 FPS. YOLOv4-608 mencapai 26,4 FPS dan memenuhi syarat tersebut, sehingga model ini disebut paling baik dalam hal akurasi dan kecepatan pada tahap itu. Kesimpulan studi menyebut model terpilih dengan AP di atas 96% dan kecepatan 37,3 FPS.

Studi membandingkan beberapa cara penghitungan. Metode ID unik dinyatakan lebih andal dengan F1count 87,85%. Penulis menjelaskan bahwa metode ini bersifat kurang membatasi (less restrictive) dibanding metode lain, sehingga buah yang sama di bingkai berbeda lebih mudah dikenali sebagai satu buah. Mekanisme pelacakan yang dipakai adalah Deep SORT, yang memberi ID pada setiap buah dan mempertahankannya antarbingkai.

Penulis menyebut dua keterbatasan. Pertama, buah yang baru terdeteksi setelah melewati garis ROI tidak ikut terhitung. Kedua, pelacakan bergantung pada informasi tampilan (appearance), sehingga perubahan tampilan buah antarbingkai dapat memutus ID. Keterbatasan ini langsung memengaruhi angka penghitungan, dan studi tidak mengukur besarnya dampak pada kebun yang lebih luas. Studi lain yang dikutip dalam pendahuluan melaporkan Deep SORT berjalan 25 sampai 50 FPS pada GPU konvensional, dan satu studi buah pir berbasis video mencapai AP 97% pada deteksi. Angka-angka itu berasal dari studi lain dan tidak dibandingkan dengan data studi ini.
