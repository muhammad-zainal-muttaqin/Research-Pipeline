# UAV imagery coupled deep learning approach for the development of an adaptive in-house web-based application for yield estimation in citrus orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `subeesh2024uav` |
| Judul asli | UAV imagery coupled deep learning approach for the development of an adaptive in-house web-based application for yield estimation in citrus orchard |
| Penulis | Subeesh, A.; Prakash Kumar, Satya; Kumar Chakraborty, Subir; Upendar, Konga; Singh Chandel, Narendra; Jat, Dilip; Dubey, Kumkum; Modi, Rajesh U.; Mazhar Khan, Mohammad |
| Tahun | 2024 |
| Venue | Measurement Journal of the International Measurement Confederation |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [subeesh2024uav.pdf](../pdf/subeesh2024uav.pdf)
- DOI resmi: https://doi.org/10.1016/j.measurement.2024.114786

## Gambaran Umum

Estimasi hasil panen sebelum panen sangat penting bagi petani dalam mengambil keputusan. Metode konvensional berbasis sampel dan penimbangan dinilai mahal, memakan waktu, dan rentan bias. Kajian ini bertujuan mengembangkan dan mengevaluasi model deteksi objek *deep learning* pada citra *unmanned aerial vehicle* (UAV) untuk mendeteksi buah jeruk, lalu menggabungkannya dengan estimasi ukuran buah dan regresi menjadi aplikasi berbasis web bernama DeepYield.

Data terdiri atas citra pohon jeruk mandarin (*Citrus reticulata*) yang diambil dengan quadcopter DJI Phantom 4 Pro V2.0. Kamera berada pada jarak horizontal 2,5 hingga 3 m dan tinggi 1 hingga 1,25 m dari tajuk pohon, dan citra diambil dari sisi kanan dan kiri. Pengambilan dilakukan selama dua musim di dua lokasi, yaitu lahan terkelola di Budni dan lahan petani di Khamkheda, Bhopal, Madhya Pradesh. Total 800 citra beresolusi tinggi dikumpulkan. Sebagian citra dibuang karena kurang layak. Citra kemudian diperbanyak dengan pemotongan, rotasi, dan pembalikan. Pembagian data untuk pelatihan, validasi, dan pengujian adalah 70:15:15. Setiap buah dianotasi ke dalam dua kelas, yaitu *harvest* (siap panen) dan *unripe* (belum matang), menggunakan alat LabelImg dengan kotak pembatas yang digambar manual. Evaluasi akhir dilakukan pada 25 pohon yang dipilih secara acak di kebun.

Metode yang dibandingkan mencakup SSD, Faster RCNN, YOLOv4, YOLOv5, dan YOLOv7. Setiap model dilatih selama 100 dan 200 epoch dengan ukuran batch 16, 32, dan 64. YOLOv7 memberikan hasil terbaik, yaitu mAP 86,48 % pada 200 epoch dan batch 32. Presisi, *recall*, dan skor F1 model tersebut masing-masing 88,54 %, 83,66 %, dan 86,03 %. SSD mencapai mAP paling tinggi 75,3 %. YOLOv4 dan YOLOv5 memperoleh mAP 84,43 % dan 84,97 %. Untuk ukuran buah, metode segmentasi tradisional YCrCb-Otsu-*watershed* hanya baik pada citra dengan kontras tinggi, dengan presisi 88,21 %, *recall* 86,75 %, dan F1 87,47 %. Segmentasi berbasis *deep learning* dinilai jauh lebih baik. Hubungan panjang sumbu utama dengan berat buah menghasilkan R² = 0,92. Pada tahap validasi lapangan, selisih hitungan buah siap panen terhadap hitungan manual rata-rata sekitar 6 ± 3 buah. Galat rata-rata estimasi hasil siap panen adalah 1,014 ± 0,2889 kg. Untuk total buah siap panen dan belum matang, galatnya meningkat menjadi 1,920 ± 0,604 kg. Keseluruhan estimasi hasil memiliki linearitas R² = 0,98 terhadap hasil aktual.

Penulis menyatakan beberapa batasan. Algoritma masih gagal mendeteksi buah yang tertutup daun, dedaunan, atau buah lain. Buah belum matang lebih sering terlewat dibanding buah siap panen karena warna hijaunya kurang kontras dengan daun dan dahan. Segmentasi tradisional tidak andal di kondisi kebun nyata. Dalam pengujian DeepYield, galat estimasi lebih dari 20 % terjadi ketika jumlah citra yang diunggah sedikit. Perbaikan lebih lanjut tidak terlalu besar setelah lebih dari 10 citra pohon. Penulis juga menyebut bahwa buah dengan segmentasi tidak presisi diberi berat default 150 g, dengan batas 50 g hingga 300 g. Penulis menyarankan pengoptimalan jalur UAV dan penggunaan perangkat pencitraan dengan bidang pandang yang berbeda untuk penelitian selanjutnya.
