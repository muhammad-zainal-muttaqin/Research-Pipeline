# Deep learning techniques for Video Instance Segmentation: A survey

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xu2025deep` |
| Judul asli | Deep learning techniques for Video Instance Segmentation: A survey |
| Penulis | Xu, Chenhao; Li, Chang-Tsun; Hu, Yongjian; Lim, Chee Peng; Creighton, Douglas |
| Tahun | 2025 |
| Venue | Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [xu2025deep.pdf](../pdf/xu2025deep.pdf)
- DOI resmi: https://doi.org/10.1016/j.patcog.2025.111763

## Gambaran Umum

Kajian ini membahas *Video Instance Segmentation* (VIS), yaitu tugas yang menggabungkan deteksi, segmentasi, dan pelacakan instance objek secara serentak di sepanjang frame video. Tugas ini juga dikenal sebagai *multi-object tracking and segmentation*. Penulis menyebut VIS telah dipakai di berbagai bidang, mulai dari pengawasan dan kendaraan otonom hingga kesehatan dan pertanian. Meski demikian, tinjauan literatur yang menyeluruh tentang VIS masih jarang. Survei yang ada umumnya membahas segmentasi citra, Transformer, atau pelacakan objek video, dengan cakupan VIS yang terbatas.

Penulis melakukan tinjauan sistematis atas metode VIS berbasis *deep learning* yang terbit sejak tahun 2019, saat VIS pertama kali diperkenalkan. Pencarian literatur dilakukan melalui Google Scholar dengan kata kunci "video instance segmentation" dan "multi-object tracking and segmentation". Prioritas diberikan kepada publikasi di konferensi dan jurnal kelas atas bidang *computer vision*. Preprint arXiv yang berdampak juga dipertimbangkan. Tabel 1 membandingkan survei ini dengan 11 survei terdahulu yang terbit tahun 2020 sampai 2023. Untuk evaluasi kuantitatif, penulis memakai tiga dataset benchmark, yaitu YouTube-VIS 2019, YouTube-VIS 2021, dan OVIS. YouTube-VIS disebut sebagai dataset berskala besar pertama dan paling banyak dipakai. OVIS memuat persentase instance yang tertutup (*occlusion*) tinggi sehingga menjadi tantangan bagi model VIS.

Penulis mengelompokkan metode VIS ke dalam empat kategori menurut strategi pemodelan temporal: *frame-by-frame*, berbasis klip (*clip-based*), propagasi fitur dalam memori (*in-memory feature propagation*), dan propagasi query objek dalam memori (*in-memory object query propagation*). Penulis menilai kategori ini menunjukkan perbedaan arsitektur yang mendasar beserta implikasinya terhadap performa. Performa metode VIS sangat bergantung pada *backbone* untuk ekstraksi fitur. ResNet, yang memperkenalkan *residual learning*, disebut sebagai salah satu arsitektur yang umum digunakan. Hasil kuantitatif disajikan pada Tabel 3 berupa perbandingan mAP berbagai metode pada tiga dataset tersebut.

Penulis menyatakan bahwa tantangan utama VIS terletak pada keseimbangan antara efisiensi komputasi dan akurasi pelacakan. Sejumlah metode meningkatkan akurasi segmentasi, tetapi dengan beban komputasi yang tinggi. Metode lain berjalan secara *real-time* dengan mengorbankan akurasi. Penulis juga menyoroti hubungan antara akurasi model dan *overhead* komputasi sebagai isu yang masih terbuka. Penulis menyebut survei ini menyoroti beberapa tantangan utama dan arah riset yang menjanjikan.

Kontribusi survei ini terdiri atas tiga bagian. Pertama, kategorisasi sistematis pendekatan VIS berdasarkan strategi pemodelan temporal. Kedua, perbandingan kuantitatif metode VIS yang ada. Ketiga, analisis tantangan dan arah riset di bidang ini. Penulis berharap uraian tersebut dapat memberi wawasan bagi peneliti dan praktisi yang ingin memajukan teknik segmentasi video.
