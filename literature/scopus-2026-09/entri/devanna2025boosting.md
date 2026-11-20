# Boosting grape bunch detection in RGB-D images using zero-shot annotation with Segment Anything and GroundingDINO

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `devanna2025boosting` |
| Judul asli | Boosting grape bunch detection in RGB-D images using zero-shot annotation with Segment Anything and GroundingDINO |
| Penulis | Devanna, Rosa Pia; Reina, Giulio; Cheein, Fernando Auat; Milella, Annalisa |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | grape |

## Tautan Akses
- PDF: [devanna2025boosting.pdf](../pdf/devanna2025boosting.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2024.109611

## Gambaran Umum

Penelitian ini membahas pendeteksian dan pemisahan tandan anggur (*grape bunch*) di kebun nyata. Dalam *precision agriculture*, informasi jumlah dan bentuk buah dibutuhkan untuk pemantauan pertumbuhan serta estimasi hasil panen. Metode pembelajaran mendalam (*deep learning*) yang akurat biasanya memerlukan data latih yang besar dan anotasi manual yang melelahkan, sehingga penulis menguji apakah model *zero-shot* dapat mengurangi kebutuhan tersebut. Dua model yang diuji adalah *Segment Anything* (SAM) dari Meta dan *GroundingDINO*, dengan *DepthSeg*, metode yang sebelumnya dikembangkan penulis, sebagai pembanding.

Data berasal dari robot petani berpenggerak darat yang dilengkapi kamera RGB-D. Citra diambil di kebun anggur komersial di Italia selatan. Setiap citra disertai peta kedalaman (*depth map*), dan citra tersebut dibandingkan dengan data *ground truth* yang dilabeli secara manual. Dataset ini dipublikasikan di GitHub. Penulis mengajukan tiga metode baru: SAM-Refine (SAM-R), yang memperbaiki DepthSeg dengan SAM; SAM-Segmentation (SAM-S), yang menggabungkan SAM dengan model segmentasi semantik terlatih untuk memisahkan kelompok buah; dan AutoSAM-Dino (ASD), yang menggabungkan GroundingDINO dan SAM tanpa pelabelan manual maupun *transfer learning*. Penelitian ini mengklaim sebagai yang pertama menggunakan SAM dan GroundingDINO untuk pengenalan anggur di lapangan.

Evaluasi dilakukan pada dua aspek, yakni penghitungan objek dan akurasi segmentasi piksel. Metrik yang digunakan adalah *mean Average Precision* (mAP), *Intersection over Union* (IoU), *precision*, dan *recall*. Dibandingkan DepthSeg, SAM-R sedikit meningkatkan penghitungan objek dengan mAP naik 0,5% dan meningkatkan segmentasi piksel dengan IoU naik 17,0%. SAM-S menurunkan mAP, tetapi meningkatkan IoU sebesar 13,9%, *precision* sebesar 9,2%, dan *recall* sebesar 11,7%. ASD juga menurunkan mAP, namun meningkatkan IoU sebesar 7,8%, *precision* sebesar 4,2%, dan *recall* sebesar 4,9%. DepthSeg sendiri mencapai mAP 0,590. Penulis juga mencatat bahwa pelatihan model segmentasi instans jauh lebih singkat dibandingkan pelabelan manual.

Temuan penelitian menunjukkan adanya pertukaran (*trade-off*) antara ketepatan penghitungan dan kualitas segmentasi. DepthSeg dan SAM-R bekerja baik dalam kondisi pencahayaan yang kurang ideal, karena memanfaatkan data kedalaman. Meskipun demikian, DepthSeg belum optimal dalam segmentasi instans, sehingga kurang cocok untuk fenotipe yang memerlukan informasi bentuk buah yang akurat. Penurunan mAP pada SAM-S dan ASD menunjukkan bahwa peningkatan kualitas segmentasi belum tentu sejalan dengan peningkatan kemampuan deteksi objek. Dengan demikian, pilihan metode bergantung pada kebutuhan aplikasinya, apakah penghitungan buah atau analisis bentuk.

Batasan utama yang dinyatakan penulis berkaitan dengan cakupan evaluasi. Hasil berlaku untuk satu dataset dari satu kebun komersial, dan penulis sendiri menegaskan bahwa pengaruh faktor eksternal seperti pencahayaan dan kualitas data hanya ditelaah sebagian. Penurunan mAP pada dua metode berbasis SAM juga belum dapat diselesaikan dalam kerangka penelitian ini. Penulis menyebut arah penelitian lanjutan, tetapi tidak merinci keterbatasan lain secara terpisah.
