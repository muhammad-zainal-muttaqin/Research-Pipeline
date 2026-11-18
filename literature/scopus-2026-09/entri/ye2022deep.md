# Deep Learning for Person Re-Identification: A Survey and Outlook

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ye2022deep` |
| Judul asli | Deep Learning for Person Re-Identification: A Survey and Outlook |
| Penulis | Ye, Mang; Shen, Jianbing; Lin, Gaojie; Xiang, Tao; Shao, Ling; Hoi, Steven C. H. |
| Tahun | 2022 |
| Venue | IEEE Transactions on Pattern Analysis and Machine Intelligence |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [ye2022deep.pdf](../pdf/ye2022deep.pdf)
- DOI resmi: https://doi.org/10.1109/tpami.2021.3054775

## Gambaran Umum

Artikel ini adalah tinjauan pustaka sekaligus usulan model dasar untuk identifikasi ulang orang (*person re-identification*, Re-ID), yaitu pencarian orang yang sama lintas kamera yang tidak tumpang tindih. Masalah yang mendasari adalah banyaknya variasi yang menyulitkan, seperti sudut pandang, resolusi rendah, perubahan pencahayaan, pose, oklusi, modalitas heterogen, serta kotak pembatas yang tidak andal. Penulis membagi kajian menjadi dua keadaan: dunia tertutup (*closed-world*) yang beroperasi pada asumsi riset dengan data berlabel cukup, dan dunia terbuka (*open-world*) yang lebih dekat ke aplikasi nyata. Tinjauan ini membedakan diri dengan menganalisis kelebihan dan kekurangan metode, bukan hanya merangkum hasil.

Objek tinjauan adalah sistem Re-ID manusia, bukan tanaman. Penulis memetakan lima langkah perancangan sistem: pengumpulan data mentah, pembuatan kotak pembatas, anotasi data latih, pelatihan model, dan pengambilan kembali data. Keadaan dunia tertutup dianalisis dari tiga sudut: pembelajaran representasi fitur mendalam, pembelajaran metrik mendalam, dan optimasi peringkat. Keadaan dunia terbuka dianalisis dari lima aspek: data heterogen, citra atau video mentah, label yang tidak tersedia atau terbatas, anotasi bising, dan skenario uji tak terlihat (*open-set*).

Dua kontribusi teknis menjadi inti artikel. Pertama, metrik mINP (*mean Inverse Negative Penalty*) mengukur biaya untuk menemukan semua pencocokan yang benar. Metrik ini bertumpu pada posisi peringkat pencocokan benar yang paling sulit ditemukan; nilai yang lebih besar menandakan kinerja lebih baik dan perhitungannya dapat disisipkan dalam proses CMC atau mAP. Kedua, model dasar AGW dibangun di atas BagTricks dengan tulang punggung ResNet50 dan tiga komponen: blok atensi *non-local*, *generalized-mean pooling* (GeM), serta fungsi rugi triplet teregulasi berbobot (WRT). Untuk data video, varian AGW+ memakai rata-rata penyatuan tingkat frame untuk merepresentasikan urutan.

Angka hasil memakai metrik Rank-1, mAP, dan mINP. Pada kumpulan data Market-1501, AGW mencatat Rank-1 95,1%, mAP 87,8%, dan mINP 65,0%; pada DukeMTMC, AGW mencatat 89,0%, 79,6%, dan 45,7%, mengungguli ABD-Net yang mencatat mINP 42,1%. Secara keseluruhan, AGW mencapai kinerja terbaik atau setara pada dua belas kumpulan data untuk empat tugas Re-ID, meliputi Re-ID citra, video, sebagian (*partial*), dan lintas modalitas. Pada tugas lintas modalitas tampak-infrared, AGW mencatat Rank-1 70,05% dan mAP 66,37% pada RegDB serta 47,50% dan 47,65% pada SYSU-MM01 untuk pencarian menyeluruh.

Batasan yang dinyatakan penulis mencakup perbedaan nilai mINP yang menjadi lebih kecil ketika ukuran galeri besar, meski metrik ini tetap dapat menunjukkan kinerja relatif model. Percobaan juga menunjukkan bahwa penambahan pembelajaran fitur tingkat bagian tidak meningkatkan kinerja, sehingga penggabungannya dengan AGW masih perlu dikaji. Penulis mengakhiri dengan sejumlah isu terbuka yang belum banyak diteliti, antara lain pengumpulan data yang tidak terkendali, pengurangan kebutuhan anotasi manusia, rancangan arsitektur yang spesifik atau mudah digeneralisasi, pembaruan model secara dinamis, dan penerapan model yang efisien untuk menjembatani kesenjangan antara keadaan dunia tertutup dan dunia terbuka.

