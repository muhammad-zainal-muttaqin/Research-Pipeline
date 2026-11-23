# Surveillance to self-driving: a comprehensive review of object detection and tracking paradigms

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `das2026surveillance` |
| Judul asli | Surveillance to self-driving: a comprehensive review of object detection and tracking paradigms |
| Penulis | Das, Puja; Jain, Chitra; Gola, Kamal Kumar |
| Tahun | 2026 |
| Venue | Iran Journal of Computer Science |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [das2026surveillance.pdf](../pdf/das2026surveillance.pdf)
- DOI resmi: https://doi.org/10.1007/s42044-025-00387-w

## Gambaran Umum

Tinjauan ini membahas pelacakan banyak objek (*multi-object tracking*, MOT) untuk pengawasan, kendaraan otonom, robotika, dan sistem transportasi cerdas. Penulis menyebut tantangan utama berupa oklusi, kabur gerak, pemeliharaan identitas jangka panjang, dan kendala waktu nyata. Kajian ini bukan kajian pertanian dan tidak membahas buah.

Data kajian berupa literatur, bukan data primer. Abstrak menyebut 152 model dan kerangka MOT yang dibandingkan pada set data acuan MOTChallenge, KITTI, Waymo Open Dataset, dan nuScenes. Strategi pencarian literatur, basis data yang dicari, dan kriteria inklusi tidak disebut dalam bagian yang dibaca. Pemberi label dan pembagian latih/uji mengikuti set data acuan masing-masing.

Metode yang ditinjau mencakup pelacak berbasis jaringan saraf konvolusi (*CNN*), jaringan saraf berulang (*RNN*), graf, dan *transformer*. Pelacak satu tahap seperti FairMOT menggabungkan deteksi dan pelacakan dalam satu model. Pelacak dua tahap seperti DeepSORT mendeteksi objek lebih dahulu lalu menautkannya dengan model gerak atau fitur tampilan (*appearance embedding*). Pendekatan hibrida menggabungkan model gerak probabilistik dengan fitur dalam.

Hasil utama bersifat kualitatif pada bagian yang dibaca. Penulis menyimpulkan bahwa pendekatan hibrida memberi ketahanan lebih baik tetapi skalabilitas lebih rendah. Metrik yang dipakai adalah MOTA, MOTP, pergantian identitas (*IDSW*), dan fragmen (*FRAG*). Angka per metode tidak dibaca dari teks ini.

Keterbatasan yang dapat diperiksa: cakupan domain hanya lalu lintas, pengawasan, dan robotika. Tidak ada evaluasi pada buah atau tanaman. Hanya satu tabel set data memuat entri pemantauan tanaman, tanpa pembahasan lebih lanjut. Sebagian teks juga memuat kalimat yang tampak sisa catatan penulis, sehingga mutu penyuntingan perlu dicermati. Bagian setelah baris 250 tidak dibaca seluruhnya.
