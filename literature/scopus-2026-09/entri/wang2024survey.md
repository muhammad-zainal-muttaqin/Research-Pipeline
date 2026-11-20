# A survey on person and vehicle re-identification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2024survey` |
| Judul asli | A survey on person and vehicle re-identification |
| Penulis | Wang, Zhaofa; Wang, Liyang; Shi, Zhiping; Zhang, Miaomiao; Geng, Qichuan; Jiang, Na |
| Tahun | 2024 |
| Venue | Iet Computer Vision |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [wang2024survey.pdf](../pdf/wang2024survey.pdf)
- DOI resmi: https://doi.org/10.1049/cvi2.12316

## Gambaran Umum

Kajian ini membahas *re-identification* (Re-ID) orang dan kendaraan. Tujuannya adalah mencocokkan orang atau kendaraan yang sama pada citra atau video dari kamera, lokasi, dan waktu yang berbeda. Teknik ini dipakai untuk pencarian orang, pelacakan lintas kamera, pengawasan lalu lintas, dan penyelidikan kriminal. Masalah utamanya adalah fitur buatan tangan (*handcrafted features*) mudah terpengaruh sudut pandang tetap, resolusi rendah, dan pencahayaan yang tidak sesuai. Warna objek yang sama dapat berubah jauh pada kondisi cahaya berbeda sehingga sistem salah menganggapnya sebagai identitas yang berbeda.

Kajian ini berupa tinjauan pustaka, bukan eksperimen baru, sehingga tidak memiliki data citra sendiri. Cakupannya meliputi tugas Re-ID untuk orang dan kendaraan. Penulis merangkum empat bidang penelitian yang sedang populer, yaitu pembelajaran multitugas, pembelajaran generalisasi, pembelajaran lintas modalitas, dan pembelajaran optimisasi. Lampiran memuat tautan kode sumber sejumlah metode, misalnya CAP, TransReID-SSL, HHCL, ICE, dan PPLR untuk orang, serta TransReID, RPTM, MSINet, dan UFDN untuk kendaraan. Lampiran juga menyebut sejumlah himpunan data kendaraan dan multimodal, antara lain VeRi, VehicleID, VeRi-wild, CityFlow, dan MSVR310.

Isi pokok tinjauan dibagi menjadi dua fase perkembangan. Fase pertama mengandalkan fitur buatan tangan dengan dua komponen, yaitu ekstraksi fitur dan pengukuran kemiripan. Contohnya adalah SDALF yang memadukan tiga fitur warna, serta *Sparse Re-ID* yang memandang Re-ID sebagai masalah pemulihan sparse blok pada ruang embedding bersama. Fase kedua memakai jaringan saraf konvolusional (*Convolutional Neural Networks*, CNN). Sejak 2014, metode berbasis CNN menggantikan fitur buatan tangan. Penulis menyatakan bahwa fitur hasil pembelajaran mendalam lebih stabil di lingkungan nyata karena tidak hanya bergantung pada warna. Tinjauan ini juga membandingkan tugas Re-ID dari berbagai sudut klasifikasi dan menyajikan arah perkembangan ke depan.

Penulis menyatakan bahwa Re-ID berbasis pembelajaran mendalam sudah mencapai akurasi yang lebih tinggi pada himpunan data acuan yang umum digunakan. Namun, teks ini tidak menyajikan angka hasil eksperimen tunggal dalam bentuk tabel kuantitatif. Tinjauan ini membahas tantangan yang muncul di keempat bidang tersebut serta kerangka dan jaringan pembelajaran mendalam yang dipakai untuk mengatasinya. Pembahasan difokuskan pada perkembangan metode, bukan pada perbandingan performa baru yang diukur penulis sendiri.
