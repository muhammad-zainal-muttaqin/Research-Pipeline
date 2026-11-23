# Comparative Analysis of Series YOLO Models for Loose Fruits Palm Oil Detection: A Comprehensive Performance Evaluation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `warni2025comparative` |
| Judul asli | Comparative Analysis of Series YOLO Models for Loose Fruits Palm Oil Detection: A Comprehensive Performance Evaluation |
| Penulis | Warni, Elly; Indrabayu; Achmad, Andani |
| Tahun | 2025 |
| Venue | International Conference on Wireless Networks and Mobile Communications Wincom |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [warni2025comparative.pdf](../pdf/warni2025comparative.pdf)
- DOI resmi: https://doi.org/10.1109/wincom65874.2025.11313397

## Gambaran Umum

Penelitian ini membandingkan empat generasi YOLO (YOLOv5, YOLOv8, YOLOv9, YOLOv11) untuk mendeteksi brondolan sawit, dengan fokus pada akurasi dan waktu inferensi. Penulis menyebut kebanyakan studi sawit terdahulu hanya menguji satu versi YOLO sehingga *trade-off* kecepatan dan akurasi belum terpetakan. Hipotesisnya: varian s/m tiap generasi mencapai mAP50 minimal 0,85 dengan latensi paling lama 300 ms.

Data berupa 597 citra, dibagi 417 latih, 120 validasi, dan 60 uji. Data primer diambil di dua tinggi kamera (0,5 dan 1 m) dengan brondolan terlihat, tertutup daun, atau bertumpuk. Data sekunder dari Roboflow berisi daun kering dan batu. Tiga kelas dilabel: daun kering (dl), brondolan (lf), dan batu (r). Pemberi label tidak disebut. Model juga dicoba pada sembilan sampel video pada ketinggian 20 cm.

Metode melatih 20 skala model dengan satu pengaturan: 500 *epoch*, *batch* 32, *optimizer* SGD, laju awal 0,01, citra 640 x 640 piksel, dengan augmentasi pencerminan, kecerahan, saturasi, dan eksposur. Metrik adalah presisi, *recall*, mAP pada IoU 0,5 dan 0,5:0,95 (IoU adalah rasio tumpang tindih kotak prediksi dan kotak acuan), serta waktu inferensi dalam milidetik pada GPU dan perangkat tepi.

Hasil: YOLOv5s mAP50 0,83 (mAP50:95 0,636, 240 ms), YOLOv8s 0,853 (332,4 ms), YOLOv5n 0,828 (122,6 ms). Nilai tertinggi: YOLOv11l 0,877 (1234,5 ms), YOLOv5l 0,868 (1397,5 ms), YOLOv9e 0,872 (3310,1 ms). YOLOv9m 0,866 dan YOLOv11m 0,869 dengan 1159,5 dan 808,4 ms. Model terbesar tiap generasi hanya sedikit lebih akurat tetapi jauh lebih lambat. Abstrak menyebut mAP sekitar 0,83 untuk model ringan dan di atas 0,86 untuk YOLOv9m dan YOLOv11m.

Keterbatasan: data uji hanya 60 citra, dan teks tidak menyebut apakah tabel dihitung pada validasi atau uji. Tidak ada pengulangan *seed* atau uji statistik meski pendahuluan menjanjikan analisis signifikansi. Hasil video tidak dilaporkan secara kuantitatif. Tabel tidak memuat YOLOv7 padahal dibahas di teks, dan abstrak menyebut waktu di bawah 340 ms yang tidak sesuai dengan hipotesis 300 ms. Tidak ada pencacahan buah; hanya deteksi per citra.
