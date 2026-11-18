# Industrial Object Counting from Traditional Machine Vision to Open-World Foundation Models: A Systematic Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2026industrial` |
| Judul asli | Industrial Object Counting from Traditional Machine Vision to Open-World Foundation Models: A Systematic Review |
| Penulis | Wang, Wei; Zhang, Shengjie; He, Jin; Liu, Lanhui; Du, Wu; Zhang, Le |
| Tahun | 2026 |
| Venue | Sensors |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [wang2026industrial.pdf](../pdf/wang2026industrial.pdf)
- DOI resmi: https://doi.org/10.3390/s26144494

## Gambaran Umum

Artikel ini adalah tinjauan sistematis tentang penghitungan objek industri, mulai dari penglihatan mesin tradisional hingga model dasar dunia terbuka. Masalah utamanya adalah memperkirakan jumlah benda kerja, komponen, atau produk dari citra atau video secara otomatis sebagai pengganti hitungan manual. Tiga kesulitan khas industri adalah penampilan yang sangat serupa dengan penumpukan rapat sehingga terjadi oklusi dan pelekatan, kondisi lingkungan yang berubah seperti pencahayaan dan debu, serta rentang skala target yang sangat luas. Penulis menggunakan definisi industri yang luas, mencakup produksi manufaktur, gudang dan logistik, penginderaan jauh industri, industrialisasi pertanian seperti penghitungan buah dan tanaman, serta lalu lintas dan perparkiran, karena tantangan teknisnya serupa dan metodenya dapat dipindahkan antarranah.

Data dan metode mengikuti PRISMA 2020. Pencarian dilakukan pada IEEE Xplore, ACM Digital Library, Web of Science, dan arXiv hingga 28 Mei 2026, menghasilkan 1.474 rekaman, terdiri atas 1.427 dari pencarian basis data dan 47 dari penelusuran daftar pustaka. Setelah penghapusan 525 duplikat, tersisa 949 rekaman untuk penyaringan judul dan abstrak; 715 dikeluarkan, sehingga 234 dinilai teks lengkap. Dari jumlah itu, 78 dikeluarkan karena bukan kajian industri, berupa tinjauan, abstrak konferensi, atau tidak memuat metrik kuantitatif, sehingga 156 kajian dimasukkan. Kajian dikelompokkan atas tiga fase, yaitu penglihatan mesin tradisional sebelum 2014, pembelajaran mendalam 2014–2020, dan model besar serta penghitungan dunia terbuka 2021–2025.

Mekanisme penghitungan berubah dari pencocokan templat dan ciri buatan, seperti ambang batas, deteksi tepi, watershed, SIFT, SURF, HOG dengan SVM, serta model komponen deformabel, menjadi regresi peta kerapatan dan deteksi berbasis jaringan saraf konvolusional. Peta kerapatan mengabaikan segmentasi per objek dan mengintegrasikan nilai kerapatan untuk memperoleh jumlah, sehingga tahan terhadap oklusi. Pendekatan berikutnya memakai Transformer, model ruang keadaan Mamba, dan model dasar. Paradigma bergeser dari penghitungan spesifik kelas ke penghitungan agnostik kelas, penghitungan tanpa contoh, penghitungan tanpa contoh visual, dan penghitungan tanpa latih, yang mengurangi ketergantungan pada anotasi berskala besar.

Angka hasil memakai metrik MAE, RMSE, NAE, SRE, presisi, recall, F1, AP50, serta sistem PrACo untuk penghitungan agnostik kelas berbasis prompt. Penulis mengutip perkembangan MAE dari 181,8 pada R-CNN tahun 2014 menjadi 68,2 pada CSRNet tahun 2018, 37,7 pada Swin Transformer tahun 2021, dan 8,6 pada Mamba-MOC tahun 2024. YOLOv1 tahun 2016 menurunkan MAE dari 110,2 menjadi 26,4, sedangkan Mamba-MOC tahun 2024 mencatat perbaikan 69,6% dibandingkan MAE 28,3 milik CountingDINO tahun 2023. Kecepatan naik dari kurang dari 5 citra per detik pada R-CNN menjadi lebih dari 60 pada YOLOv8 dan 100 pada Mamba-MOC. Penulis secara tegas menyatakan bahwa penurunan MAE keseluruhan sebesar 95,3% hanya bersifat ilustratif, bukan perbandingan langsung, karena dataset dan pengaturan percobaan berbeda antarkajian. Pada uji oklusi, kenaikan MAE relatif dari oklusi ringan 10–30% ke berat 60–90% adalah 27,4% untuk jaringan sadar oklusi, 38,2% untuk fusi banyak pandang, dan 82,7% untuk estimasi peta kerapatan. CSRNet memiliki 16,2 juta parameter dan 68,7 G FLOPs pada masukan 512 × 512; anotasi titik mengurangi biaya pelabelan lebih dari 70% dibandingkan anotasi kotak, sedangkan kuantisasi INT8 menurunkan latensi dari 42 ms menjadi di bawah 25 ms dengan kehilangan MAE di bawah 3%.

Batasan yang dikemukakan penulis mencakup biaya anotasi, kesulitan adaptasi domain, dan keharusan penerapan waktu nyata pada perangkat tepi. Terdapat kesenjangan antara FLOPs teoretis dan latensi nyata: pengurangan FLOPs sebesar 50% hanya menurunkan latensi ujung-ke-ujung 20–30% karena transmisi data, praproses, pascaproses, dan penjadwalan sistem tidak menyusut sebanding. Sistem industri juga menuntut kestabilan operasi 7 × 24 jam, ketahanan terhadap suhu, debu, dan getaran, integrasi dengan pengendali logika terprogram, serta sertifikasi keselamatan. Penulis tidak melakukan meta-analisis kuantitatif karena heterogenitas dataset, metrik, dan pengaturan percobaan, sehingga sintesis bersifat naratif. Arah masa depan yang diusulkan adalah arsitektur ringan dengan kompleksitas linear, penghitungan dunia terbuka berbasis model bahasa-visi, fusi multimodal, serta pembelajaran tanpa pengawasan dan swa-pengawasan.

