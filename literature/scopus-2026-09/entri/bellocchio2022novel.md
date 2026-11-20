# A novel vision-based weakly supervised framework for autonomous yield estimation in agricultural applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bellocchio2022novel` |
| Judul asli | A novel vision-based weakly supervised framework for autonomous yield estimation in agricultural applications |
| Penulis | Bellocchio, Enrico; Crocetti, Francesco; Costante, Gabriele; Fravolini, Mario Luca; Valigi, Paolo |
| Tahun | 2022 |
| Venue | Engineering Applications of Artificial Intelligence |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [bellocchio2022novel.pdf](../pdf/bellocchio2022novel.pdf)
- DOI resmi: https://doi.org/10.1016/j.engappai.2021.104615

## Gambaran Umum

Bellocchio dkk. (2022) di *Engineering Applications of Artificial Intelligence* mengusulkan estimasi hasil panen dari video satu kamera monokular. Kerangka ini menghubungkan buah yang sama lintas bingkai dan lintas pandangan, lalu menggabungkan observasinya ke dalam peta global, sehingga satu buah tidak dihitung berkali-kali. Penulis menyatakan bahwa sistem mampu melacak dan memetakan buah maupun pohon hanya dengan satu kamera. Detektor buah dilatih dengan label keberadaan atau ketiadaan (*weak supervision*), bukan dengan kotak batas penuh untuk setiap buah.

Cara kerjanya dibagi menjadi beberapa tahap. Detektor WS-FLNet memberi lokasi buah pada setiap bingkai. Aliran optik (*optical flow*) FlowNet2 memperkirakan gerak piksel antarbingkai, sehingga deteksi di bingkai berurutan dapat dicocokkan. Estimasi kedalaman DiverseDepth dan struktur dari gerak (*structure from motion*, SfM) memberi posisi relatif setiap buah dalam ruang tiga dimensi. Modul optimasi peta global kemudian menggabungkan observasi yang berasal dari buah yang sama. Hitungan akhir adalah jumlah entitas unik di peta, bukan jumlah deteksi per bingkai.

Hasil dilaporkan pada dua kumpulan data. Pada ACFR-mangoes, metode ini memberi MAE 58,61, RMSE 69,79, dan MAEP 33,80%. Pembanding monokular Liu dkk. (2019) dengan SfM memberi MAE 27,66, RMSE 35,16, dan MAEP 15,52%. Metode MVS dengan LIDAR dan GPS-RTK memberi galat terkecil, tetapi memerlukan perangkat yang lebih mahal. Penulis mencatat bahwa metode ini meremehkan jumlah pada buah yang berkelompok. Pada ISAR-almond, hasilnya setara YE-FasterRCNN pada sisi 1 dan lebih rendah pada sisi 2. Metode ini mengungguli YE-WSCOUNT dengan RMSE 97,79 melawan 124,07. Penulis menyebut strategi oklusi dan penghapusan hitungan ganda menentukan untuk total hasil.

Batas kajian ini terlihat dari sisi pengujian dan pelaporan. Dua kumpulan data (mangga dan almond) belum mencakup kebun sawit, dan penulis sendiri menyebut zaitun dan adaptasi domain sebagai pekerjaan lanjutan. Keunggulan atas Liu dkk. (2019) tidak berlaku pada ACFR-mangoes, sehingga klaim pelacakan lintas bingkai belum terbukti lebih baik daripada SfM monokular pada semua kondisi. Pada bagian yang telah dibaca, belum ditemukan ablasi yang memisahkan kontribusi tiap modul (pelacakan, kedalaman, optimasi peta) terhadap galat; pemeriksaan tabel ablasi lengkap belum dilakukan. Untuk peta tinjauan, kajian ini menjadi bukti bahwa de-duplikasi lintas pandang dapat dilakukan tanpa sensor kedalaman, dengan galat yang masih lebih besar dibanding metode multi-sensor.
