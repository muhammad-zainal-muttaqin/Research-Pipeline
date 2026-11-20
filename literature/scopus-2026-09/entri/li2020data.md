# Data Association Methods via Video Signal Processing in Imperfect Tracking Scenarios: A Review and Evaluation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2020data` |
| Judul asli | Data Association Methods via Video Signal Processing in Imperfect Tracking Scenarios: A Review and Evaluation |
| Penulis | Li, Hui; Liu, Yapeng; Lin, Wenzhong; Xu, Lingwei; Wang, Junyin |
| Tahun | 2020 |
| Venue | Mathematical Problems in Engineering |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [li2020data.pdf](../pdf/li2020data.pdf)
- DOI resmi: https://doi.org/10.1155/2020/7549816

## Gambaran Umum

Kajian ini membahas *asosiasi data* (*data association*) dalam pelacakan multiobjek (*multiobject tracking*, MOT) pada video. Asosiasi data mencocokkan objek yang terdeteksi antarbingkai, sehingga kemajuannya menentukan kinerja pelacakan secara keseluruhan. Penulis menyatakan bahwa sebagian besar metode MOT masih dibangun untuk skenario ideal dengan kepadatan objek rendah dan oklusi yang jarang terjadi. Pada aplikasi nyata, kondisi tersebut sering tidak terpenuhi. Tinjauan terdahulu banyak membahas asosiasi data pada data sensor seperti radar dan sonar, sehingga belum ada ringkasan khusus untuk asosiasi data berbasis video. Kajian ini bertujuan mengisi celah tersebut.

Sebagai tinjauan, kajian ini menjelaskan cakupan literaturnya. Bagian metode tradisional meliputi asosiasi berbasis probabilitas, pencocokan fitur, asosiasi berbasis transformasi, dan asosiasi hierarkis. Bagian pembelajaran mendalam membagi metode menjadi tiga kelompok: asosiasi berbasis metode SOT, metode *end-to-end*, dan metode berbasis metrik *Wasserstein*. Penulis juga merangkum kumpulan data dan kriteria evaluasi MOT. Kumpulan data dibagi menjadi dua tahap, yaitu kumpulan data klasik berbasis metode tradisional dan kumpulan data populer berbasis pembelajaran mendalam. Kumpulan data yang disebut secara khusus antara lain MOT15, MOT17, dan UA-DETRAC. Kriteria evaluasi yang dibahas mencakup MOTA dan MOTP.

Penulis membandingkan kinerja metode tradisional dan metode pembelajaran mendalam. Metode tradisional relatif ringan dan dapat dijalankan pada CPU, tetapi kinerjanya kurang baik dan sebagian besar memerlukan intervensi manusia. Metode pembelajaran mendalam memberikan kinerja lebih baik dan jarang memerlukan intervensi manusia, tetapi membutuhkan data dan komputasi yang besar serta GPU saat pelatihan. Salah satu metode yang dibahas, DNA, membagi proses menjadi tahap ekstraksi fitur dan tahap estimasi afinitas. Menurut penulis, metode tersebut memberikan hasil terbaik pada masanya pada MOT15, MOT17, dan UA-DETRAC. Penulis juga menyinggung kebutuhan untuk menggabungkan keunggulan metode tradisional dengan pembelajaran mendalam.

Penulis menyatakan beberapa batasan dan tantangan. Oklusi dapat menyebabkan asosiasi keliru, pertukaran ID, atau hilangnya objek yang dilacak. Objek dalam satu kelas yang mirip juga sulit dibedakan jika fitur yang diekstraksi kurang kaya. Pada jaringan kembar, objek yang hilang atau tidak sejajar dapat membuat asosiasi gagal. Selain itu, metode pembelajaran mendalam masih memiliki parameter dan beban komputasi yang berlebihan, sementara kebutuhan waktu nyata, akurasi, dan generalitas harus terus diperbaiki. Penulis mencatat bahwa belum ada kumpulan data video dunia nyata yang umum dan lebih baik, serta anotasi data masih memakan waktu. Alat anotasi semiotomatis dan otomatis yang ada belum memberikan hasil yang memuaskan.
