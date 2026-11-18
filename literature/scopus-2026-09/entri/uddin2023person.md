# Person Re-Identification with RGB–D and RGB–IR Sensors: A Comprehensive Survey

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `uddin2023person` |
| Judul asli | Person Re-Identification with RGB–D and RGB–IR Sensors: A Comprehensive Survey |
| Penulis | Uddin, Md Kamal; Bhuiyan, Amran; Bappee, Fateha Khanam; Islam, Md Matiqul; Hasan, Mahmudul |
| Tahun | 2023 |
| Venue | Sensors |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [uddin2023person.pdf](../pdf/uddin2023person.pdf)
- DOI resmi: https://doi.org/10.3390/s23031504

## Gambaran Umum

Artikel ini adalah tinjauan pustaka tentang identifikasi ulang orang (*person re-identification*, Re-ID) menggunakan sensor RGB-D dan RGB-IR. Masalah utamanya adalah mencocokkan individu lintas kamera yang tidak tumpang tindih. Pendekatan RGB-RGB berbasis pembelajaran mendalam bekerja baik pada kondisi normal, tetapi tidak konsisten ketika resolusi rendah dan pencahayaan gelap. Sensor tambahan, yaitu kedalaman (D) dan inframerah (IR), mampu menangkap penampilan dalam gelap, sehingga menjadi alternatif bagi pengawasan siang-malam. Tinjauan lain biasanya membahas hanya RGB-RGB atau hanya RGB-IR; artikel ini menyatakan sebagai tinjauan pertama yang membahas RGB-D dan RGB-IR sekaligus.

Objek tinjauan bukan tanaman, melainkan publikasi Re-ID manusia dari literatur visi komputer. Penulis mengklasifikasikan metode menjadi tiga golongan: multi-modal, cross-modal, dan single-modal. Golongan multi-modal dibagi lagi menjadi kombinasi RGB-depth, RGB-rangka, depth-rangka, RGB-depth-rangka, dan RGB-depth-termal. Golongan cross-modal membahas pencocokan RGB-depth, RGB-sketsa, dan RGB-IR. Golongan single-modal membahas IR-IR dan depth-depth. Kumpulan data yang diulas meliputi RGBD-ID, KinectREID, BIWI RGBD-ID, RobotPKU RGBD-ID, DPI-T, TVPR, OPR, RGB-D-T, SYSU-MM01 (491 orang, 287.628 citra RGB, 15.792 citra IR), dan RegDB (412 orang).

Mekanisme yang menopang asosiasi adalah penggabungan fitur atau skor dari beberapa modalitas, baik pada tingkat fitur maupun tingkat skor. Fitur penampilan RGB digabung dengan fitur antropometrik kebal cahaya dari citra kedalaman, fitur rangka, atau citra termal. Contoh metode yang diulas meliputi MMUDL yang membentuk variabel latent seragam dengan bagian khusus kedalaman, bersama, dan khusus RGB; UVDL yang memakai *auto-encoder* seragam dan variasional; serta *multi-modal attention network* (MAT) yang menggabungkan fitur lokal dan global. Pada pencocokan cross-modal RGB-IR, model non-generatif menangani jurang modalitas pada tingkat fitur, sedangkan model generatif menangannya pada tingkat piksel.

Angka hasil berasal dari metrik CMC yang dilaporkan sebagai akurasi *rank-1* (sebagian juga nAUC), bukan dari eksperimen baru penulis. MMUDL mencatat 100% *rank-1* pada RGBD-ID tanpa perubahan pakaian dan 76,7% pada RGBD-ID lengkap, serta 97% pada KinectREID. UVDL mencatat 99,4% pada KinectREID dan 76,7% pada RGBD-ID, sehingga kenaikan 2,4% pada KinectREID tidak diikuti perbaikan pada RGBD-ID. Lejbolle dkk. memperoleh 90,36%, 63,83%, dan 45,63% berturut-turut pada DPI-T, TVPR, dan OPR; MAT menaikkan angka itu sebesar 2,01%, 19,15%, dan 3,43%. Metode gabungan skor ketidaksamaan mencatat 93,33% pada RobotPKU, 82,05% pada RGBD-ID, dan 87,65% pada SUCVL.

Batasan yang dinyatakan penulis mencakup ketidakcukupan kumpulan data untuk melatih model mendalam karena jumlah frame per orang terlalu sedikit untuk menangkap keragaman. Kamera Kinect hanya menjangkau objek sampai 4 m sehingga tidak cocok untuk pengawasan jarak jauh; penulis menyarankan Intel RealSense hingga 10 m. Beberapa kumpulan data tidak merekam informasi rangka dengan benar dan tidak menyinkronkan citra RGB dengan kedalaman. Model generatif berisiko memasukkan derau meski menghindari pengaruh warna. Penulis juga menyatakan bahwa setting eksperimen yang berbeda-beda menghalangi perbandingan adil antarmetode, sehingga mereka merencanakan prosedur eksperimen baku untuk evaluasi ulang.

