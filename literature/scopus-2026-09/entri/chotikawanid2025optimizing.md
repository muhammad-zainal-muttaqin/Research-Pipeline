# Optimizing an Object Detection Algorithm for Detecting Oil Palm Fruit Bunches and Their Ripeness

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chotikawanid2025optimizing` |
| Judul asli | Optimizing an Object Detection Algorithm for Detecting Oil Palm Fruit Bunches and Their Ripeness |
| Penulis | Chotikawanid, Piyanart; Saeleung, Pattanapong; Pianroj, Yutthapong; Jumrat, Saysunee; Punvichai, Teerasak; Muangprathub, Jirapond |
| Tahun | 2025 |
| Venue | Applied Computational Intelligence and Soft Computing |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [chotikawanid2025optimizing.pdf](../pdf/chotikawanid2025optimizing.pdf)
- DOI resmi: https://doi.org/10.1155/acis/6263757

## Gambaran Umum

Kajian ini mengembangkan detektor tandan buah segar (TBS) kelapa sawit berbasis YOLOv7 yang mengklasifikasikan tandan menurut tingkat kematangan: mentah (*raw*), setengah matang (*half ripe*), dan matang (*ripe*). Model dilatih dan diuji pada 427 citra. Penulis melaporkan bahwa pembekuan lapisan (*layer freezing*) pada 80% lapisan memperbaiki hasil dibanding pelatihan 500 epoch tanpa pembekuan.

Citra dibagi menjadi 146 citra mentah, 157 setengah matang, dan 124 matang. Pembagian data adalah 297 citra latih, 84 validasi, dan 46 uji, dan augmentasi menaikkan jumlah citra latih menjadi 891. Model dasar dilatih selama 500 epoch. Varian yang dioptimasi membekukan 50% sampai 90% lapisan, dan pembekuan 80% dipilih sebagai konfigurasi terbaik.

Model dasar YOLOv7 selama 500 epoch mencapai mAP@0,5 sebesar 86,90%, presisi 72,50%, recall 90,20%, dan F1 80,38%. Pada konfigurasi pembekuan 80%, presisi naik 4,92 poin, F1 naik 3,36 poin, recall naik 0,98 poin, dan mAP@0,5 naik 0,7 poin. Tabel 9 melaporkan presisi 77,42% (p = 0,00021), F1 83,74% (p = 0,00015), recall 91,18%, dan mAP@0,5 87,60%, dengan uji Wilcoxon signed-rank untuk perbedaan berpasangan.

Angka di abstrak tidak sama dengan angka di Tabel 9 dan simpulan. Abstrak menyebut akurasi klasifikasi 92,55% dan mAP 95,08%, sedangkan Tabel 9 dan simpulan menyebut 77,42% dan 87,60%.

Penulis sendiri menyebut tiga keterbatasan: dataset kecil (427 citra), tidak ada validasi silang k-fold, dan uji lapangan yang belum dilakukan. Kajian ini mengklasifikasikan tandan per citra dan menyatakan penghitungan pada antarmuka web, tetapi tidak mengasosiasikan tandan yang sama lintas beberapa citra atau pandang. Karena itu jumlah tandan yang dilaporkan tidak menjamin bahwa setiap buah hanya dihitung sekali.
