# Apple Yield Estimation Method Based on CBAM-ECA-Deeplabv3+ Image Segmentation and Multi-Source Feature Fusion

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cui2025apple` |
| Judul asli | Apple Yield Estimation Method Based on CBAM-ECA-Deeplabv3+ Image Segmentation and Multi-Source Feature Fusion |
| Penulis | Cui, Wenhao; Lan, Yubin; Li, Jingqian; Yang, Lei; Zhou, Qi; Han, Guotao; Xiao, Xiao; Zhao, Jing; Qiao, Yongliang |
| Tahun | 2025 |
| Venue | Sensors |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [cui2025apple.pdf](../pdf/cui2025apple.pdf)
- DOI resmi: https://doi.org/10.3390/s25103140

## Gambaran Umum

Kajian ini membahas estimasi hasil panen apel dari citra kebun dengan segmentasi semantik dan regresi. Citra dipisahkan menjadi empat kelas, yaitu bunga, buah, daun, dan cabang, memakai DeepLabv3+ yang dilengkapi modul perhatian CBAM dan ECA. Dari hasil segmentasi dihitung rasio struktural, indeks vegetasi, dan nilai SPAD (klorofil relatif), lalu dipakai sebagai masukan model regresi untuk memperkirakan hasil panen per plot dalam kilogram.

Metode segmentasi diukur dengan IoU per kelas. Pada Tabel 7, CBAM-ECA-DeepLabv3+ mencapai IoU 0,86 untuk bunga, 0,90 untuk buah, 0,94 untuk daun, dan 0,83 untuk cabang, dengan rata-rata 0,89. Teks melaporkan bahwa DeepLabv3+ memperoleh MIoU 0,11 lebih tinggi dari U2Net dan 0,03 lebih tinggi dari PSPNet. Jumlah sampel tercatat 240 (80 untuk SPAD, 80 untuk indeks vegetasi, dan 80 untuk rasio struktural), dibagi 7:3 untuk latih dan uji.

Pada Tabel 8, korelasi Pearson terhadap hasil panen adalah 0,792 untuk f1 dan 0,800 untuk f4, dengan f2 0,750 dan f3 0,740. Indeks VARI (0,755) memiliki korelasi tertinggi di antara indeks vegetasi, sedangkan DVI, GDVI, dan GEVI berada di bawah 0,7. Rasio f1 sampai f4 dipilih sebagai masukan model hasil panen. Tabel 9 membandingkan tiga kelompok masukan: A (s1, s2), B (f1 sampai f4), dan C (d1, d2, d3, k1).

Abstrak melaporkan R2 0,942 dan RMSE 12,980 kg untuk model hasil panen. Pencarian kata kunci (grep) pada tahap ini mengembalikan keluaran kosong dan tidak dipakai sebagai bukti bahwa istilah tertentu tidak ada.

Batasnya adalah sampel kecil (240 total) dan keluaran berupa berat hasil panen per plot, bukan jumlah buah per pohon.
