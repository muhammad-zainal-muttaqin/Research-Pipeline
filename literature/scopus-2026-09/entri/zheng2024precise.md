# A precise grape yield prediction method based on a modified DCNN model

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zheng2024precise` |
| Judul asli | A precise grape yield prediction method based on a modified DCNN model |
| Penulis | Zheng, Shaoxiong; Gao, Peng; Zhang, Jiahong; Ma, Zhexiang; Chen, Shihong |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [zheng2024precise.pdf](../pdf/zheng2024precise.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.109338

## Gambaran Umum

Penelitian ini bertujuan memprediksi hasil panen anggur secara lebih presisi. Penulis menyebut bahwa metode berbasis pengalaman petani dan statistik dasar memiliki rata-rata galat lebih dari 20 %. Regresi linier dan analisis deret waktu menurunkan galat menjadi 15 % sampai 20 %. Metode pembelajaran mesin seperti *support vector machine* dan *random forest* meningkatkan akurasi sekitar 10 % sampai 15 %, tetapi masih kesulitan dengan data berskala besar dan ekstraksi fitur yang kompleks. Karena itu, penulis mengusulkan model jaringan saraf konvolusional termodifikasi yang disebut M-DCNN.

Data dikumpulkan di kebun anggur seluas 60 acre di kampus Guangdong Ecological Engineering Vocational College, Tiongkok. Pengambilan citra berlangsung dari April 2023 sampai Juni 2024 dan menghasilkan 10.000 sampel citra. Data diambil dari tiga kebun yang mewakili tahap pertumbuhan awal, tengah, dan akhir. Kamera SONY Alpha 7R IV dengan resolusi 9504 × 6336 piksel dipasang pada traktor yang bergerak di sepanjang lahan. Citra yang buruk dibuang, dan total data yang tersisa sekitar 50 GB. Setiap citra diambil dari arah depan dan menghadap langsung ke tanaman anggur.

Penelitian ini membandingkan tiga arsitektur deteksi objek, yaitu *Single Shot MultiBox Detector* (SSD), DCNN, dan M-DCNN. Model dilatih awal pada *Common Objects in Context* (COCO) dan *Open Images Dataset* (OID), lalu dilatih lagi pada data kebun. Citra lapangan dianotasi dengan *bounding box* sebagai *ground truth*. Metrik utama adalah *mean average precision* (mAP), dan *intersection over union* (IoU) dihitung sebagai pelengkap. Untuk deteksi buah anggur individual, hanya DCNN dan M-DCNN yang diuji. Nilai mAP rata-rata berkisar 0,267 sampai 0,822 dengan citra resolusi sangat tinggi. Namun, penulis menilai akuisisi citra tersebut tidak ekonomis. Setelah citra dipecah menjadi struktur tanaman dan diuji pada IoU 75 %, nilai mAP berkisar 0,7576 sampai 0,9811. M-DCNN dinilai paling baik mendeteksi tanaman anggur. Pada tahap pelatihan, M-DCNN mencapai akurasi 97,35 %, atau 0,85 % lebih tinggi dibanding DCNN standar. Untuk deteksi buah anggur, rata-rata skor F1 sebesar 73,32 % dan koefisien determinasi di atas 0,98. Penulis menyatakan bahwa model ini mengungguli metode estimasi hasil tradisional dan model pembelajaran mesin lain.

Penulis menyebut beberapa tantangan umum pembelajaran mendalam dalam bidang ini. Tantangan tersebut meliputi kebutuhan data berlabel yang besar, keterbatasan interpretabilitas model, dan biaya komputasi yang tinggi. Pelabelan manual untuk buah individual juga disebut padat tenaga dan rawan kesalahan. Penulis menekankan bahwa tingkat resolusi citra menjadi kendala biaya dalam penerapan lapangan.
