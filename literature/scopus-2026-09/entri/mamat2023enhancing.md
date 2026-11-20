# Enhancing Image Annotation Technique of Fruit Classification Using a Deep Learning Approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mamat2023enhancing` |
| Judul asli | Enhancing Image Annotation Technique of Fruit Classification Using a Deep Learning Approach |
| Penulis | Mamat, Normaisharah; Othman, Mohd Fauzi; Abdulghafor, Rawad; Alwan, Ali A.; Gulzar, Yonis |
| Tahun | 2023 |
| Venue | Sustainability Switzerland |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [mamat2023enhancing.pdf](../pdf/mamat2023enhancing.pdf)
- DOI resmi: https://doi.org/10.3390/su15020901

## Gambaran Umum

Penelitian ini menangani anotasi citra yang dilakukan secara manual. Anotasi dianggap pekerjaan berulang yang memakan waktu dan tenaga, sementara volume data citra terus bertambah. Penulis mencatat bahwa klasifikasi kematangan tandan buah segar sawit penting untuk mutu minyak, dan penilaian manual rentan kesalahan manusia. Tujuan penelitian adalah mengembangkan teknik anotasi otomatis berbasis pembelajaran mendalam, khususnya metode anotasi berulang (*repetitive annotation task*), untuk mengklasifikasikan kematangan tandan sawit dan mengenali beberapa jenis buah pada himpunan data besar.

Citra tandan sawit dikumpulkan di kebun Felda Tenang, Jerteh, Terengganu, Malaysia, sebanyak 400 citra untuk empat kelas, yaitu unripe, underripe, ripe, dan overripe. Citra diperoleh dengan telepon genggam dan UAV DJI Phantom 4 beresolusi 3472×4640 serta 3840×2160 piksel, lalu diubah ke 416×416 piksel. Augmentasi memperbanyak data menjadi 600 citra. Anotasi awal dilakukan manual dengan LabelImg pada 152 citra, 38 per kelas. Himpunan data sawit terdiri atas 152 citra latih dan 600 citra uji (150 per kelas). Himpunan data buah lain mencakup rambutan, buah naga, nanas, dan manggis yang diunduh dari Google Image dan Kaggle, dengan 400 citra latih (100 per kelas) dan 3.500 citra uji (875 per kelas); teks juga menyebut angka 3.400 citra buah. Penulis menyatakan data tidak dipublikasikan karena pembatasan privasi.

Model yang dipakai adalah YOLOv5 dengan transfer learning, dibandingkan dengan YOLOv3 dan YOLOv4. Arsitektur YOLOv5 terdiri atas backbone dengan lapisan Focus, modul BottleneckCSP, dan SPP; neck berupa FPN dan PAN; serta head yang memakai anchor box untuk menghasilkan probabilitas kelas, skor, dan kotak pembatas. Fungsi rugi merupakan jumlah rugi regresi kotak, rugi kepercayaan, dan rugi klasifikasi. Mekanisme anotasi berulang bekerja dengan melatih model pada himpunan awal, memakai model itu untuk memberi anotasi otomatis pada citra baru, lalu menggabungkan citra hasil anotasi tersebut ke dalam himpunan latih; proses diulang sampai akurasi optimum. Metrik yang dipakai adalah presisi, recall, AP sebagai luas di bawah kurva presisi–recall, dan mAP@0.5 pada ambang IoU 0,5. Pelatihan memakai learning rate 0,01, batch 32, IoU 0,2, dan 100 epoch untuk data sawit serta 30 epoch untuk data buah lain, dengan Python di Google Colaboratory.

Perbandingan tiga versi YOLO pada data sawit menunjukkan YOLOv3 presisi 67%, recall 70%, mAP@50 78%, waktu latih 0,896 jam; YOLOv4 74%, 83%, 85%, 0,876 jam; YOLOv5 98%, 97%, 99%, 0,609 jam. Pada proses anotasi berulang untuk sawit, mAP@50 total naik dari 98% pada pelatihan awal menjadi 98,2% pada anotasi pertama dan 98,7% pada anotasi kedua. Presisi total berubah dari 98,2% menjadi 96,6% dan 96,7%, sedangkan recall total dari 93,6% menjadi 97% dan 97,5%. Waktu latih bertambah dari 0,187 menjadi 0,306 dan 0,412 jam, sedangkan waktu deteksi per citra turun dari 0,54 menjadi 0,43 dan 0,3 ms. Untuk campuran buah, mAP@50 total naik dari 99,0% menjadi 99,5% pada anotasi pertama dan tetap 99,5% pada anotasi kedua; presisi total menjadi 99,5% dan waktu deteksi turun dari 0,44 menjadi 0,25 ms. Abstrak melaporkan mAP 98,7% untuk tandan sawit dan 99,5% untuk beragam buah.

Batasan yang dinyatakan penulis mencakup ketidakmampuan anotasi otomatis untuk mengekstrak makna semantik secara lengkap dan tidak adanya kenaikan akurasi antara anotasi pertama dan kedua pada himpunan buah lain, yang dikaitkan dengan titik ketika penambahan data tidak lagi meningkatkan akurasi. Penulis juga mencatat nilai presisi dan recall yang tidak stabil, meskipun mAP dianggap lebih sesuai untuk deteksi karena memasukkan false positive dan false negative. Selain itu, himpunan data tidak tersedia untuk umum. Penulis mengusulkan metode anotasi berulang ini diterapkan pada teknik pembelajaran mendalam lain. Kajian ini berfokus pada anotasi dan klasifikasi kematangan per citra, bukan pada penghitungan jumlah tandan atau asosiasi lintas pandang.
