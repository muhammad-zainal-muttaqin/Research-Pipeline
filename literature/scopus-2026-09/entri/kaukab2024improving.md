# Improving real-time apple fruit detection: Multi-modal data and depth fusion with non-targeted background removal

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kaukab2024improving` |
| Judul asli | Improving real-time apple fruit detection: Multi-modal data and depth fusion with non-targeted background removal |
| Penulis | Kaukab, Shaghaf; Komal; Ghodki, Bhupendra M; Ray, Hena; Kalnar, Yogesh B.; Narsaiah, Kairam; Brar, Jaskaran S. |
| Tahun | 2024 |
| Venue | Ecological Informatics |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [kaukab2024improving.pdf](../pdf/kaukab2024improving.pdf)
- DOI resmi: https://doi.org/10.1016/j.ecoinf.2024.102691

## Gambaran Umum

Kajian ini (Kaukab dkk., 2024) mengusulkan NBR-DF, yaitu pendekatan deteksi buah berbasis RGB-D untuk kebun dengan tajuk pohon yang rapat. Pendekatan ini memakai detektor YOLOv5 yang diperkaya modul depth-attention. Sebelum masuk jaringan, citra depth diproses dengan non-targeted background removal dan pengisian lubang depth. Penulis melaporkan average precision 0,964 pada AP0,5 dalam pengujian real-time, angka tertinggi di antara varian yang diuji dalam tabel perbandingan mereka.

Masalah yang diangkat adalah deteksi buah pada kebun yang padat, ketika daun dan cabang menutupi buah dan latar belakangnya mirip warna buah. Pada citra RGB saja, pemisahan buah dari latar tersebut bergantung pada warna dan tekstur. Depth dari kamera stereo memberi informasi jarak yang dapat membantu memisahkan buah yang berada di depan dari latar yang lebih jauh. Kajian ini menguji apakah informasi itu, bila dimasukkan lewat mekanisme atensi, menaikkan akurasi deteksi.

Perangkat yang dipakai adalah kamera stereo Intel RealSense D455. Data berisi 39.894 buah yang diberi label pada keseluruhan citra RGB-D, termasuk 1.000 citra. Tabel 3 melaporkan AP0,5 untuk beberapa varian: A 0,915; B 0,363; C 0,925; D 0,964; dan E 0,931. Angka 0,964 pada abstrak dikaitkan dengan NBR-DF. Varian B yang jauh lebih rendah menunjukkan bahwa penambahan atau pilihan komponen tertentu dapat merusak deteksi.

Hasil pengujian dilaporkan dengan GPU RTX 2050, sedangkan kesimpulan menyebut RTX 2060. Ketidakkonsistenan ini belum diselesaikan. Kajian juga tidak menyebut hasil pada data publik lain, dan data hanya tersedia atas permintaan (Data availability: "Data will be made available on request."), sehingga pengulangan oleh pihak lain bergantung pada penulis.
