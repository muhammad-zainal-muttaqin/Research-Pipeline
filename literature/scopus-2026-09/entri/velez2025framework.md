# Framework for smartphone-based grape detection and vineyard management using UAV-trained AI

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `velez2025framework` |
| Judul asli | Framework for smartphone-based grape detection and vineyard management using UAV-trained AI |
| Penulis | V\'elez, Sergio; Ariza-Sent\'\is, Mar; Trivi\~no, Mario; Cob-Parro, Antonio Carlos; Mila, Miquel; Valente, Jo\~ao |
| Tahun | 2025 |
| Venue | Heliyon |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [velez2025framework.pdf](../pdf/velez2025framework.pdf)
- DOI resmi: https://doi.org/10.1016/j.heliyon.2025.e42525

## Gambaran Umum

Kajian ini membahas pencacahan tandan anggur dengan ponsel pintar di kebun anggur komersial. Estimasi hasil panen pada tingkat tanaman dan lahan biasanya memerlukan penghitungan visual yang lambat dan mahal. Pemantauan dengan drone sudah banyak dipakai, tetapi petani kecil sering tidak memiliki drone atau robot darat. Penulis mengusulkan kerangka lima tahap. Model deteksi dilatih dengan citra drone, lalu dipakai untuk menganalisis foto yang diambil petani dengan ponsel biasa. Hasil deteksi kemudian digabungkan dengan posisi batang tanaman dari GNSS untuk menghasilkan peta hasil. Tujuannya adalah alat yang murah, mudah diakses, dan dapat diterapkan dalam pemantauan kebun secara nyata.

Penelitian dilakukan pada dua kebun komersial di Tomiño, Spanyol, dengan tanaman *Vitis vinifera* kultivar Loureiro pada fase BBCH77 sampai BBCH79. Sistem pembinaan memakai tiang vertikal, dan tanaman tidak diberi perlakuan seperti pembuangan daun. Video diambil dengan drone DJI M210v2 yang dilengkapi sensor Zenmuse X5S. Penerbangan dilakukan pada 28 Juni 2021 pada ketinggian 3 m, dengan kamera dimiringkan 60 derajat. Sebanyak 40 video RGB direkam dari empat penerbangan, dengan total 7,49 gigabita. Pakar agronomi memberi anotasi pada 29 urutan video, menghasilkan 679 bingkai dengan label per piksel. Video kemudian dibagi kira-kira 70/30 untuk pelatihan dan pengujian. Foto ponsel berjumlah 253 citra tandan anggur dari dua kebun. Foto diambil dengan Xiaomi Poco X3 Pro dan iPhone X pada siang dan sore hari. Posisi batang diukur dengan Trimble R2 yang memberi akurasi tingkat sentimeter. Data video dan label MOTS tersedia untuk umum.

Metode memakai X-Decoder untuk *referring segmentation* yang memisahkan tanaman dari latar belakang. Zona yang mungkin berisi tandan kemudian diekstraksi. Model YOLOv8x-seg untuk *instance segmentation* dilatih selama 150 epoch dengan ukuran batch 8, ukuran citra 640 piksel, dan pengoptimal SGD. Pelatihan berjalan pada satu GPU Nvidia A5500 selama lebih dari 25 jam. Hasil pada data uji menunjukkan presisi 0,92, recall 0,735, dan skor F1 0,82. *Average Precision* (AP) sebesar 0,802 setara dengan mAP karena hanya satu kelas, yaitu "grape-bunch". Pada perbandingan dengan *ground truth* di lapangan, jumlah tandan hasil model memiliki R2 0,84 dengan kemiringan 0,8843 terhadap hitungan visual. Hitungan visual terhadap *ground truth* memiliki R2 0,93 dengan kemiringan 0,7715. Penulis memperkirakan tingkat tertutup daun rata-rata sekitar 20 %.

Penulis mencatat beberapa batasan. Model cenderung meremehkan jumlah tandan dibandingkan hitungan visual. Penyebab utamanya adalah kesulitan mengenali tandan yang tertutup sebagian oleh daun. Peta hasil dari metode usulan juga sedikit lebih rendah daripada peta visual, terutama di bagian tengah dan atas kebun. Kondisi pencahayaan yang buruk pada sore hari juga menjadi tantangan bagi deteksi. Penulis menekankan bahwa kebun yang diteliti tidak diberi perlakuan pembuangan daun, sehingga oklusi alami tetap ada. Hasil ini perlu diuji lebih lanjut pada kebun dan varietas lain.
