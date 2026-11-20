# Combining Domain Adaptation and Spatial Consistency for Unseen Fruits Counting: A Quasi-Unsupervised Approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bellocchio2020combining` |
| Judul asli | Combining Domain Adaptation and Spatial Consistency for Unseen Fruits Counting: A Quasi-Unsupervised Approach |
| Penulis | Bellocchio, Enrico; Costante, Gabriele; Cascianelli, Silvia; Fravolini, Mario Luca; Valigi, Paolo |
| Tahun | 2020 |
| Venue | IEEE Robotics and Automation Letters |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [bellocchio2020combining.pdf](../pdf/bellocchio2020combining.pdf)
- DOI resmi: https://doi.org/10.1109/lra.2020.2966398

## Gambaran Umum

Bellocchio dkk. (2020) mengusulkan QU-COUNT, metode pencacahan buah yang dilatih tanpa anotasi lokasi buah. Metode ini bekerja pada citra tunggal per pandang. Sinyal pelatihannya berupa label lemah: ada atau tidak adanya buah pada citra, dan jumlah total buah per citra. Penghitungan dilakukan per citra lalu dijumlahkan, tanpa penggabungan identitas buah antarpandang.

Pencacahan berbasis deteksi memerlukan kotak pembatas atau titik untuk setiap buah. Anotasi semacam itu mahal, dan penulis menyebut biayanya sebagai hambatan utama penerapan di kebun. Metode yang hanya memakai jumlah per citra menghemat anotasi, tetapi jumlah saja tidak menunjukkan di mana buah berada, sehingga galatnya sulit ditelusuri.

QU-COUNT melatih penghitung kepadatan pada citra yang hanya diberi label jumlah dan keberadaan buah. Adaptasi domain dilakukan dengan *CycleGAN*, jaringan yang menerjemahkan gaya citra antardomain tanpa pasangan citra, sehingga citra sumber mirip citra target. Keluarannya adalah peta kepadatan yang diintegralkan menjadi jumlah buah per citra.

MBC-CNN memakai tiga cabang dengan skala 1, 4, dan 16. Setiap cabang menghasilkan peta kepadatan, dan jumlah buah diperoleh dari integral peta tersebut.

*Presence-Absence Classifier* (PAC), pengklasifikasi ada atau tidaknya buah, memberi sinyal ada atau tidaknya buah pada citra. Sinyal ini dipakai sebagai pengawas tambahan pada citra yang jumlahnya nol atau sangat kecil, sehingga penghitung tidak menghasilkan kepadatan pada latar belakang.

CycleGAN dilatih untuk menerjemahkan citra sumber ke gaya citra target dan sebaliknya. Fungsi galat mencakup galat adversarial (LGAN), galat siklus (Lcyc), galat adaptasi (Ladapt), dan galat total (Ltot). Persamaan 3 sampai 6 pada makalah memuat fungsi ini.

Penulis membandingkan QU-COUNT dengan Bargoti dkk., WS-COUNT, MBC-CNN+PACS, dan MBC-CNN+GAN. Hasil dilaporkan dalam Tabel I sebagai rerata galat (µ), simpangan baku (σ), dan p-value per skenario. Untuk domain Almonds dengan sumber AL, QU-COUNT mencatat µ 3,69, σ 0,13, p 0,99. MBC-CNN+GAN dengan sumber AL pada target yang sama mencatat µ 4,93, σ 0,26, p 0,96. Penulis menyatakan QU-COUNT memberi galat lebih rendah daripada MBC-CNN+GAN pada seluruh eksperimen. Angka dibaca per baris tabel dan tidak dirata-ratakan.

Estimasi hasil kebun (bagian IV.E) memakai FasterRCNN berbasis ResNet101 yang dilatih pada COCO untuk mendeteksi kanopi. Citra dipotong menjadi tile 300×300 piksel, lalu jumlah buah tiap tile dijumlahkan per pohon.

Kelebihan utama adalah tidak diperlukannya anotasi lokasi buah. Keterbatasannya: setiap estimasi tetap bergantung pada satu citra per pandang, sehingga buah yang sama dari pandang berbeda dapat terhitung lebih dari sekali. Dalam bagian yang dibaca untuk kajian ini, tidak ditemukan mekanisme deduplikasi lintas pandang.
