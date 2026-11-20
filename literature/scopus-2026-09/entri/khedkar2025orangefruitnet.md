# OrangeFruitNet: A Dataset and On-device Real Time YOLO-based Framework for Orange Fruit Detection and Yield Estimation in Orchard Environments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `khedkar2025orangefruitnet` |
| Judul asli | OrangeFruitNet: A Dataset and On-device Real Time YOLO-based Framework for Orange Fruit Detection and Yield Estimation in Orchard Environments |
| Penulis | Khedkar, Mohan; Sambhe, Vijay; Dhore, Vaibhav; Khedkar, Shrinivas; Khandare, Nikhil |
| Tahun | 2025 |
| Venue | International Journal of Intelligent Engineering and Systems |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus, other berries |

## Tautan Akses
- PDF: [khedkar2025orangefruitnet.pdf](../pdf/khedkar2025orangefruitnet.pdf)
- DOI resmi: https://doi.org/10.22266/ijies2025.1231.67

## Gambaran Umum

Khedkar dkk. (2025) membandingkan lima detektor objek pada citra kebun jeruk: YOLOv4-Darknet53, YOLOv5-s, YOLOv8-n, Mask R-CNN, dan Faster R-CNN. Makalah ini juga mengusulkan taksonomi dataset OrangeFruitNet dan menghitung estimasi hasil panen per pohon serta per kebun. Penghitungan dilakukan per gambar, tanpa mekanisme identitas lintas-pandang.

Pada ringkasan abstrak, YOLOv8-n melaporkan mAP 91,2% dan F1 0,92. Hasil bagian deteksi menyebut YOLOv5-s dan YOLOv8-n dengan mAP di atas 93% pada dataset jeruk. Kedua model itu disebut lebih cepat daripada Faster R-CNN dan Mask R-CNN. Dataset dibagi 80:10:10, dan angka mAP@0,5 dilaporkan sebagai rerata ± simpangan baku dari tiga run.

Jumlah buah dihitung per gambar, lalu diskalakan dengan rasio luas kanopi pohon terhadap luas gambar (Persamaan 6). Hasil per pohon dijumlahkan menjadi hasil per kebun (Persamaan 7). Koefisien determinasi R² adalah 0,89 ± 0,03 untuk baseline berbasis luas dan 0,94 ± 0,02 untuk regresi linear berganda dengan kanopi, diameter buah, dan kerapatan sebagai prediktor. Regresi dikalibrasi memakai label ahli untuk 20 pohon dan divalidasi dengan lima lipatan. Validasi akhir memakai data survei lapangan ahli.

Model yang dilatih pada CitDet atau Green Citrus turun sekitar 6 sampai 10% saat diuji pada OrangeFruitNet. Penulis menafsirkan model yang dilatih pada OrangeFruitNet lebih tahan terhadap pergeseran domain, dengan penurunan sekitar 1 sampai 3%. Klaim ini tidak disertai uji kontrol lintas-pandang.
