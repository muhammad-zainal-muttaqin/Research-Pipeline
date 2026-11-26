# Automated pineapple detection, ripeness classification, and weight prediction using YOLOv8 and drone imagery

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `langpoklakpam2025automated` |
| Judul asli | Automated pineapple detection, ripeness classification, and weight prediction using YOLOv8 and drone imagery |
| Penulis | Langpoklakpam, Bidyarani; Murry, Lithungo K.; Kumar, R. |
| Tahun | 2025 |
| Venue | Journal of Food Measurement and Characterization |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | pineapple |

## Tautan Akses
- PDF: [langpoklakpam2025automated.pdf](../pdf/langpoklakpam2025automated.pdf)
- DOI resmi: https://doi.org/10.1007/s11694-025-03565-3

## Gambaran Umum

Kajian ini (Journal of Food Measurement and Characterization, 2025) menggabungkan deteksi nanas, klasifikasi kematangan, perkiraan ukuran, dan perkiraan bobot dari citra drone.

Video diambil dengan DJI Mini 4 Pro pada ketinggian 2 m di atas barisan nanas varietas Kew di dua kebun di Nagaland, India. Pengambilan dilakukan pada beberapa hari, pagi dan sore. Bingkai video menghasilkan 2.057 citra 1920×1080 piksel yang dibagi 1.528 latih, 354 validasi, dan 175 uji. Kotak dilabeli dengan LabelImg dalam tiga kelas: mentah, setengah matang, dan matang.

Untuk deteksi, YOLOv8 memberi presisi 99,8%, mAP 97,7%, dan *recall* 93,1%, lebih tinggi daripada YOLOv7, YOLOv11, dan RT-DETR. Presisi per kelas kematangan adalah 98%, 92%, dan 98%. Ukuran buah dihitung dari kotak dan topeng biner, dengan konversi piksel ke milimeter, dan dibandingkan dengan ukuran jangka sorong pada 100 buah yang dibawa ke laboratorium. MAPE ukuran di bawah 6% untuk buah tidak tertutup dan 8% untuk buah tertutup. Bobot diperkirakan dari jumlah piksel, dan KNN memberi R2 0,978 dan RMSE 4,12 g.

Buah tidak dicacah per petak atau per baris. Citra berasal dari bingkai video, dan teks tidak menyebut bahwa bingkai dari video yang sama dipisahkan antara data latih dan data uji.
