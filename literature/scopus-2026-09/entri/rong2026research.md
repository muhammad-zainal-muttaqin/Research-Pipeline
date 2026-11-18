# Research progress on precision orchard yield estimation based on multi-source information perception sensors

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `rong2026research` |
| Judul asli | Research progress on precision orchard yield estimation based on multi-source information perception sensors |
| Penulis | Rong, Zifan; Ru, Yu; Zhang, Xiao; Fang, Shuping; Zhou, Hongping; Jiang, Xuesong |
| Tahun | 2026 |
| Venue | Frontiers in Plant Science |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [rong2026research.pdf](../pdf/rong2026research.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2026.1759956

## Gambaran Umum

Tinjauan sistematis ini mengkaji estimasi hasil kebun presisi berbasis penginderaan multi-sumber. Penulis berangkat dari kelemahan estimasi manual yang memakan tenaga dan waktu serta mengabaikan perbedaan antarpohon dan pengaruh topografi dan pencahayaan, sehingga menghasilkan galat besar. Peninjauan bertujuan membandingkan metode penglihatan mesin, penginderaan jarak jauh, dan fusi data multi-sumber dari sisi metode dan aplikasi, serta menganalisis hambatan fusi sensor untuk prediksi hasil. Cakupan tanaman difokuskan pada apel, jeruk, dan anggur. Penghitungan buah unik lintas pandang tidak dibahas sebagai mekanisme tersendiri.

Data dan metode mengikuti prinsip inti PRISMA. Pencarian memakai Web of Science, Scopus, Google Scholar, IEEE Xplore, ScienceDirect, dan SpringerLink dengan kata kunci bahasa Cina dan Inggris, seperti "fruit tree", "yield estimation", "remote sensing", "UAV", "machine learning", dan "deep learning", serta metode bola salju dari daftar pustaka. Kriteria inklusi mencakup kajian estimasi hasil buah yang diterbitkan di jurnal bereputasi atau konferensi berkualitas dan memuat inovasi metode, aplikasi, atau evaluasi kinerja; rentang waktu dibatasi 15 tahun terakhir. Kolam awal berjumlah sekitar 436 rekaman, lalu disaring melalui judul, abstrak, dan teks lengkap. Kajian yang tidak terkait buah, tanpa validasi praktis, atau tanpa teks lengkap dikecualikan.

Mekanisme estimasi dibedakan menjadi langsung dan tidak langsung. Estimasi langsung mendeteksi dan menghitung buah per pohon lalu menjumlahkannya untuk seluruh kebun; estimasi tidak langsung menambah langkah regresi untuk menyimpulkan muatan buah per pohon dari sampel citra sebelum dijumlahkan. Penghitungan buah memakai segmentasi citra atau deteksi objek. Fusi multi-sumber menggabungkan informasi deteksi buah dengan ciri fisiologis dan struktural kanopi dari pencitraan RGB, LiDAR, hyperspektral, dan inframerah termal. Pendekatan lain mencakup deteksi buah muda, estimasi ukuran buah, fotogrametri SfM, dan model seperti YOLO, Faster R-CNN, Mask R-CNN, serta LSTM.

Angka hasil dikutip dari kajian dalam korpus tinjauan, bukan dari percobaan penulis, sehingga tidak ada acuan hitung milik tinjauan ini. Penggantian backbone YOLOv5 dengan BiFPN pada leci meningkatkan AP@0,5 dari 50,6 menjadi 64,1, atau naik 13,5 poin persentase (26,7%). Penggantian backbone dengan GhostNet pada YOLOv5 meningkatkan kecepatan deteksi sebesar 81%. Kombinasi Faster R-CNN dan LSTM menurunkan galat estimasi hasil dari 13,74% menjadi 7,22%, atau turun 47,5% dibandingkan baseline. Metrik yang dipakai meliputi AP@0,5, kecepatan deteksi, dan galat estimasi hasil.

Batasan yang dinyatakan penulis meliputi oklusi buah, deteksi yang terlewat, variabilitas lingkungan, generalisasi lintas musim yang terbatas, dan heterogenitas data tinggi. Pada tahap berbunga dan buah muda, penyerbukan alami, cuaca ekstrem, serta hama dan penyakit menyebabkan rontok buah sehingga estimasi cenderung berlebih; buah yang kecil dan pucat juga menyerupai daun dan ranting sehingga sering salah atau terlewat terdeteksi. Penginderaan multispektral terbatas oleh jumlah pita dan resolusi spasial, sementara integrasi LiDAR dan pencitraan inframerah termal untuk kebun masih jarang. Penulis mengusulkan kerangka penginderaan terpadu dengan fusi data darat, udara, dan satelit, deteksi nol dan sedikit contoh berbasis model bahasa-visi, serta platform otonom dengan komputasi tepi dan awan.

