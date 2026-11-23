# YOLO-Based Oil Palm FFB Ripeness Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `naghipour2024yolo` |
| Judul asli | YOLO-Based Oil Palm FFB Ripeness Detection |
| Penulis | Naghipour, Mohammadmahdi; Ling, Lew Sook; Connie, Tee |
| Tahun | 2024 |
| Venue | 5th International Conference on Electrical Communication and Computer Engineering Icecce 2024 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [naghipour2024yolo.pdf](../pdf/naghipour2024yolo.pdf)
- DOI resmi: https://doi.org/10.1109/icecce63537.2024.10823630

## Gambaran Umum

Penulis membangun detektor kematangan tandan buah segar (TBS) sawit dengan YOLOv10 untuk membedakan tandan matang dari mentah. Masalah yang disebut: penanganan buah secara manual memakan waktu, padat karya, dan subjektif. Hasilnya diekspor ke antarmuka web sederhana.

Data berupa himpunan pribadi 500 citra TBS pada berbagai tingkat kematangan. Sebanyak 321 citra berasal dari Multimedia University dan sisanya dari internet. Citra diberi kotak pembatas dengan aplikasi LabelImg. Pemberi label tidak disebut. Pembagian latih, validasi, dan uji tidak disebut. Tandan yang menjadi fokus berada di pohon.

Model yang diuji adalah YOLOv10 ukuran N, S, dan M dengan hiperparameter bawaan, 50 *epoch*, dan *batch* 32. YOLOv10 adalah detektor satu tahap tanpa langkah *non-maximum suppression* (penyaringan kotak ganda) pada inferensi. Pelatihan dijalankan di Google Colaboratory. Model terbaik dibungkus dengan pustaka Streamlit untuk antarmuka web.

Nilai mAP YOLOv10-N 0,946, YOLOv10-S 0,950, dan YOLOv10-M 0,924. Untuk YOLOv10-S, presisi 0,96 dan *recall* 0,87, serta mAP50-95 0,59. Teks tidak menyebut dengan jelas himpunan data yang dipakai menghitung angka ini.

Keterbatasan: hanya 500 citra, sebagian dari internet, tanpa pembagian data yang dinyatakan. Tidak ada himpunan uji terpisah yang disebut dan tidak ada ulangan. Jumlah dan nama kelas kematangan selain "matang" dan "mentah" tidak dirinci. Tidak ada pencacahan atau pembanding dengan kajian lain.
