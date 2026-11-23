# Harnessing YOLO for Loose Fruits Detection: Boosting Productivity in Palm Oil Plantations

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `warni2025harnessing` |
| Judul asli | Harnessing YOLO for Loose Fruits Detection: Boosting Productivity in Palm Oil Plantations |
| Penulis | Warni, Elly; Indrabayu; Achmad, Andani; Syahsir, Aldilah Rezki Rhamadani |
| Tahun | 2025 |
| Venue | Icadeis 2025 2025 International Conference on Advancement in Data Science E Learning and Information System Integrating Data Science and Information System Proceeding |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [warni2025harnessing.pdf](../pdf/warni2025harnessing.pdf)
- DOI resmi: https://doi.org/10.1109/icadeis65852.2025.10933352

## Gambaran Umum

Penelitian ini bertujuan mendeteksi brondolan (buah sawit lepas) di perkebunan dengan YOLOv5. Penulis menyebut brondolan bernilai ekonomi tinggi karena kandungan minyaknya, tetapi sering tidak terkumpul sehingga merugikan dan memicu pertumbuhan gulma. Pengumpulan manual dinilai tidak efisien, subjektif, dan lambat. Studi ini bagian dari proyek robot pengumpul brondolan.

Data berupa 525 citra brondolan di lingkungan kebun, dibagi 461 latih, 32 validasi, dan 32 uji. Data primer diambil langsung dengan tinggi kamera 0,5 dan 1 m, dengan brondolan terlihat jelas, tertutup sebagian oleh daun, atau bertumpuk. Data sekunder dari Roboflow berisi daun kering dan batu agar kelas dan objek serupa terwakili. Pemberi label tidak disebut. Jumlah pohon dan jumlah buah tidak disebut.

Metode memakai YOLOv5, detektor satu tahap dengan *backbone* CSPDarknet (pengekstrak fitur), *neck* PAFPN (penggabung fitur antarskala), dan *head* yang memprediksi kotak pembatas, skor keyakinan, dan kelas. Citra diubah ke 640 x 640 piksel dan diaugmentasi dengan pencerminan serta perubahan kecerahan, saturasi, dan eksposur. Penulis menyetel ukuran *batch* (4 sampai 64, 500 *epoch*), *optimizer*, laju pembelajaran, *weight decay*, dan *momentum*. Pengujian memakai dua skenario: brondolan terlihat jelas, dan brondolan tertutup sebagian daun atau rumput.

Pada penyetelan, kombinasi terbaik adalah SGD, laju 0,01, *weight decay* 0,0005, dan *momentum* 0,9, dengan mAP50 0,884 dan mAP50:95 0,638. Pada pengujian skenario 1, kelas brondolan mencapai mAP50 0,916 dan mAP50:95 0,622, dan semua kelas 0,738 dan 0,547. Pada skenario 2, brondolan mencapai mAP50 0,940 dan mAP50:95 0,632, semua kelas 0,574 dan 0,408, kelas batu hanya 0,208 dan 0,187. Matriks konfusi skenario 1 mencatat 225 positif benar, 21 negatif palsu, dan 50 positif palsu untuk brondolan.

Keterbatasan: data uji hanya 32 citra, dan teks tidak menyebut apakah angka penyetelan dihitung pada validasi atau uji. Pembagian per lokasi atau pohon tidak disebut. Daun kering sengaja tidak dilabel bila mirip tanah, sehingga positif palsu kelas itu tinggi. Tidak ada pencacahan buah atau penggabungan pandang; hanya deteksi per citra. Teks tidak memuat uji pada pohon atau video untuk studi ini.
