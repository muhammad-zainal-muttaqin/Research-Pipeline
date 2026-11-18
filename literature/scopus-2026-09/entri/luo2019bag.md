# Bag of tricks and a strong baseline for deep person re-identification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `luo2019bag` |
| Judul asli | Bag of tricks and a strong baseline for deep person re-identification |
| Penulis | Luo, Hao; Gu, Youzhi; Liao, Xingyu; Lai, Shenqi; Jiang, Wei |
| Tahun | 2019 |
| Venue | IEEE Computer Society Conference on Computer Vision and Pattern Recognition Workshops |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [luo2019bag.pdf](../pdf/luo2019bag.pdf)
- DOI resmi: https://doi.org/10.1109/cvprw.2019.00190

## Gambaran Umum

Makalah ini membahas *person re-identification* (ReID), yaitu mencocokkan citra orang yang sama di antara kamera dengan identitas berbeda. Penulis mengamati bahwa banyak metode unggulan membangun struktur jaringan yang kompleks dan menggabungkan banyak fitur lokal, serta sering diuji di atas baseline yang lemah. Perbaikan yang dilaporkan sebagian berasal dari trik latih yang tidak dijelaskan secara memadai, sehingga perbandingan menjadi tidak adil. Penulis juga mencatat bahwa industri lebih membutuhkan model sederhana yang hanya memakai fitur global karena fitur lokal yang panjang memperlambat pencarian. Tujuan makalah ini adalah mengumpulkan dan menguji trik latih yang efektif, menyediakan baseline yang kuat, serta memberi acuan bagi penelaah saat membandingkan metode.

Eksperimen memakai dataset Market1501 dan DukeMTMC-reID dengan metrik *rank-1 accuracy* dan *mean Average Precision* (mAP). Baseline memakai ResNet50 berbobot awal ImageNet; satu batch terdiri dari P = 16 identitas dan K = 4 citra per identitas, citra diubah ke 256×128 dengan padding 10 piksel lalu dipotong secara acak, dibalik horizontal dengan probabilitas 0,5, dan dinormalisasi per kanal RGB. Pelatihan memakai *triplet loss* dengan margin 0,3 dan *ID loss* berupa *cross entropy*, dioptimalkan dengan Adam pada laju awal 0,00035 yang diturunkan 0,1 kali pada epoch ke-40 dan ke-70 selama 120 epoch. Enam trik ditambahkan secara berurutan: *warmup* laju belajar (10 epoch pertama naik linier dari 3,5×10⁻⁵ ke 3,5×10⁻⁴), *random erasing augmentation* (probabilitas 0,5, rasio luas 0,02–0,4, rasio aspek 0,3–3,33), *label smoothing* (ε = 0,1), perubahan *last stride* dari 2 menjadi 1 sehingga peta fitur membesar dari 8×4 menjadi 16×8, BNNeck, dan *center loss* dengan bobot β = 0,0005.

Mekanisme asosiasinya terletak pada cara fitur dipelajari dan dicocokkan. BNNeck menambahkan satu lapisan *batch normalization* setelah fitur ft dan sebelum lapisan FC tanpa bias, lalu memakai fi hasil normalisasi untuk *ID loss* dan ft untuk *triplet loss*. Penulis beralasan *ID loss* mengoptimalkan jarak cosine karena memisahkan ruang dengan hyperplane, sedangkan *triplet loss* mengoptimalkan jarak Euclidean untuk kompaksi intra-kelas dan pemisahan antarkelas; mengoptimalkan satu vektor dengan kedua rugi tersebut menimbulkan tujuan yang bertentangan. Normalisasi BN membuat fitur berdistribusi di sekitar permukaan hipersfera, memudahkan konvergensi *ID loss*, mengurangi kendalanya terhadap ft, dan menjaga kekompakan fitur satu orang. Saat inferensi, model memakai fi dengan metrik cosine. *Center loss* melengkapi *triplet loss* yang hanya membandingkan jarak pasangan positif dan negatif dengan menghukum jarak fitur ke pusat kelas.

Tabel 1 melaporkan ablasi pada domain yang sama. Baseline standar memperoleh 87,7% *rank-1* dan 74,0% mAP pada Market1501 serta 79,7% dan 63,7% pada DukeMTMC-reID. Penambahan berurutan menghasilkan 88,7/75,2 dan 80,6/65,1 (*warmup*), 91,3/79,3 dan 81,5/68,3 (REA), 91,4/80,3 dan 82,4/69,3 (*label smoothing*), 92,0/81,7 dan 82,6/70,6 (*stride* = 1), 94,1/85,7 dan 86,2/75,9 (BNNeck), serta 94,5/85,9 dan 86,4/76,4 (*center loss*). Pada uji lintas domain (Tabel 3), baseline mencatat 24,4/12,9 untuk Market1501 ke Duke dan 34,2/14,5 untuk sebaliknya; dengan menghilangkan REA, hasil menjadi 41,4/25,7 dan 54,3/25,5. Tabel 4 menunjukkan bahwa dengan *k-reciprocal re-ranking*, model mencapai 95,4/94,2 pada Market1501 dan 90,3/89,1 pada Duke. Angka-angka tersebut adalah *rank-1*/mAP pada kedua dataset; penulis tidak menyatakan pengulangan dengan beberapa seed.

Batasan yang dinyatakan penulis mencakup REA yang justru merugikan kinerja lintas domain karena menutup area citra latih dan membuat model terlalu menyesuaikannya dengan domain sumber; ukuran citra yang tidak memberi perbedaan besar; serta ukuran batch yang tidak menghasilkan kesimpulan pasti, hanya kecenderungan bahwa batch lebih besar membantu penambangan pasangan sulit. Percobaan dibatasi oleh memori satu GPU yang hanya menampung 128 citra sehingga kombinasi P = 32 dengan K = 6 atau 8 tidak diuji. Penulis juga menyatakan bahwa tujuan makalah ini bukan sekadar menaikkan angka, bahwa masih banyak trik yang belum ditemukan, dan bahwa prinsip di balik trik tersebut belum dianalisis lebih jauh, misalnya penggantian BNNeck dengan normalisasi L2 serta penerapan metode lain di atas baseline ini.

