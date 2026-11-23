# Palm Fruit Ripeness Detection and Classification Using Various YOLOv8 Models

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gunawan2023palm` |
| Judul asli | Palm Fruit Ripeness Detection and Classification Using Various YOLOv8 Models |
| Penulis | Gunawan, Teddy Surya; Kartiwi, Mira; Mansor, Hasmah; Yusoff, Nelidya Md. |
| Tahun | 2023 |
| Venue | Icsima 2023 9th IEEE International Conference on Smart Instrumentation Measurement and Applications |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [gunawan2023palm.pdf](../pdf/gunawan2023palm.pdf)
- DOI resmi: https://doi.org/10.1109/icsima59853.2023.10373435

## Gambaran Umum

Kajian ini menguji varian YOLOv8 untuk mendeteksi dan mengklasifikasikan kematangan tandan buah segar (TBS) kelapa sawit. Penulis menyebut penilaian kematangan oleh penilai manusia memakan waktu dan rawan galat, sedangkan kematangan menentukan *oil extraction rate* (OER, rasio minyak yang diperoleh). Penulis menyebut penurunan OER 0,13% akibat buah mentah dapat menimbulkan kerugian RM 340 juta. Tujuannya adalah mencari varian YOLOv8 yang menyeimbangkan akurasi dan beban komputasi.

Data memakai set data terbitan lain yang digabungkan penulis, berisi 7.171 citra dengan 14.559 objek dalam enam kelas: mentah (*unripe*), kurang matang (*underripe*), matang (*ripe*), terlalu matang (*overripe*), tandan kosong, dan abnormal. Citra diambil dari video ponsel 1280×720 berisi putaran 360° satu TBS selama 10 sampai 15 detik. Bingkai diambil tiap detik dan diubah menjadi 416×416. Pelabelan memakai DarkLabel. Pembagian data 70% latih, 20% validasi, 10% uji. Lokasi pengambilan, jumlah pohon, dan pemberi label tidak disebut.

Metode melatih lima varian YOLOv8 (n, s, m, l, x), yaitu detektor satu tahap (*one-stage*) yang memprediksi kotak pembatas dan kelas dalam satu lintasan jaringan. Semua varian dilatih 100 *epoch* dengan laju belajar awal 0,01 dan ukuran *batch* 16 pada GPU RTX 4080. Model terbaik menurut mAP50-95 divalidasi ulang. mAP50 adalah rerata presisi pada ambang tumpang-tindih (IoU) 0,5, dan mAP50-95 merata-ratakan ambang 0,5 sampai 0,95.

Semua varian mencapai mAP50 0,995 pada Tabel II. mAP50-95 tertinggi dicapai YOLOv8m, 0,927, dengan waktu latih 0,899 jam, dibandingkan YOLOv8n 0,917, YOLOv8s 0,926, serta YOLOv8l dan YOLOv8x masing-masing 0,921. Pada pengujian model terbaik, presisi dan *recall* sekitar 0,9964, mAP50 0,9949, mAP50-95 0,9268, dan waktu inferensi 11,268 ms. AP per kelas berkisar 0,89 (abnormal) sampai 0,95 (mentah).

Keterbatasan yang dapat diperiksa dari teks: citra berasal dari bingkai video yang sama sehingga pembagian acak berpotensi menaruh bingkai satu TBS di data latih dan uji, dan pembagian per TBS tidak disebut. Angka hasil Tabel II tampak dihitung pada data validasi, sedangkan keterangan data uji pada tahap pengujian tidak jelas. Satu TBS dicitrakan sendiri, tanpa adegan pohon utuh. Tidak ada pencacahan buah atau penautan antarbingkai.
