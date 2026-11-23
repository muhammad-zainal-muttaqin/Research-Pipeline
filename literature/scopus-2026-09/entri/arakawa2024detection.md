# Detection of on-tree chestnut fruits using deep learning and RGB unmanned aerial vehicle imagery for estimation of yield and fruit load

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `arakawa2024detection` |
| Judul asli | Detection of on-tree chestnut fruits using deep learning and RGB unmanned aerial vehicle imagery for estimation of yield and fruit load |
| Penulis | Arakawa, Takumi; Tanaka, Takashi S. T.; Kamio, Shinji |
| Tahun | 2024 |
| Venue | Agronomy Journal |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [arakawa2024detection.pdf](../pdf/arakawa2024detection.pdf)
- DOI resmi: https://doi.org/10.1002/agj2.21330

## Gambaran Umum

Penelitian ini bertujuan menghitung buah kastanye (*bur*, kapsul berduri berisi biji) di pohon dari citra RGB yang direkam *unmanned aerial vehicle* (UAV, pesawat nirawak). Penulis menyatakan bahwa hitungan buah masih dilakukan manual atau berdasarkan perkiraan petani. Mereka juga menyatakan bahwa hubungan jumlah *bur* dengan hasil panen jarang dilaporkan. Tujuan lanjutannya adalah memakai hitungan itu untuk memprediksi hasil panen dan beban buah.

Penelitian dilakukan di kebun kastanye 0,4 ha di Gifu, Jepang, pada 2021. UAV DJI Mavic Mini terbang manual pada ketinggian 12 sampai 15 m dengan arah kamera tegak lurus ke bawah. Satu foto mencakup sekitar enam pohon. Foto dipotong menjadi 50 bagian (5 × 10) berukuran 416 × 416 piksel. Hasilnya 500 citra dengan 7.866 *bur* yang diberi kotak pembatas secara manual dengan LabelImg. Pembagian acak: 400 citra latih dan 100 citra validasi. Evaluasi hitungan memakai 53 pohon utuh (klon cangkok dari 9 kultivar, umur 3 sampai 7 tahun) dengan hitungan manual pada citra dan hitungan lapangan oleh teknisi ahli.

Metode memakai detektor satu tahap *You Only Look Once* (YOLO) versi 3 dan 4, yang memprediksi kotak dan kelas objek dalam satu lintasan jaringan. Bobot praterlatih disesuaikan pada semua lapisan (*transfer learning*). Jumlah *bur* per pohon diperoleh dengan menghitung kotak yang lolos ambang kepercayaan (0,3 untuk YOLOv4, 0,1 untuk YOLOv3). Hitungan itu dibandingkan dengan hitungan manual melalui regresi linear. Regresi linear lain menghubungkan hitungan dengan hasil panen. Hitungan dinormalkan dengan lingkar batang untuk menguji hubungannya dengan bobot biji pada kultivar "Ena hougetsu".

Pada data validasi, YOLOv4 mencapai presisi 0,84, *recall* 0,85, skor F1 0,84, dan AP pada IoU 50% sebesar 84,27, sedangkan YOLOv3 mencapai skor F1 0,77 dan AP 75,05. Terhadap hitungan manual pada citra yang sama (n = 53 pohon), YOLOv4 memberi R² 0,976, RMSE 6,3 *bur* per pohon, dan MAE 4,7. Terhadap hitungan lapangan, R² 0,828 dan RMSE 60,7. Hitungan YOLOv4 sebesar 42,9% sampai 103,6% (rerata 65,5%) dari hitungan lapangan. Terhadap hasil panen total, R² terkoreksi 0,76 dengan galat baku 1,08 kg per pohon (koefisien variasi 26,4%), setara hitungan lapangan (0,77). Hubungan hitungan ternormalisasi dengan bobot biji berkorelasi negatif (R = -0,90; p = 2,4 × 10⁻⁵; 13 pohon).

Keterbatasan yang tertulis: pandangan tegak lurus dari atas melewatkan sekitar sepertiga *bur* yang tertutup daun, dan hitungan YOLOv4 tidak menangkap buah tersembunyi. Pohon uji berumur 7 tahun atau kurang. Citra diambil pada satu hari, satu kebun, dan satu musim. Pembagian latih dan validasi acak per potongan citra, sehingga pemisahan per pohon tidak disebut. Penulis tidak memakai set uji terpisah untuk deteksi, dan tabel hasil deteksi disebut sebagai data uji padahal teks menyebutnya data validasi. Hubungan hasil panen diuji pada 53 pohon yang sama dengan evaluasi hitungan. Hitungan hanya dari satu pandang atas per pohon tanpa penggabungan pandang.
