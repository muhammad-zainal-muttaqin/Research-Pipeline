# Occluded person re-identification with deep learning: A survey and perspectives

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ning2024occluded` |
| Judul asli | Occluded person re-identification with deep learning: A survey and perspectives |
| Penulis | Ning, Enhao; Wang, Changshuo; Zhang, Huang; Ning, Xin; Tiwari, Prayag |
| Tahun | 2024 |
| Venue | Expert Systems with Applications |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [ning2024occluded.pdf](../pdf/ning2024occluded.pdf)
- DOI resmi: https://doi.org/10.1016/j.eswa.2023.122419

## Gambaran Umum

Artikel tinjauan ini mengkaji *person re-identification* (Re-ID) pada kondisi teroklusi, yaitu pencocokan pedestrian ketika sebagian tubuh tertutup objek. Masalah utamanya adalah oklusi yang meluas menurunkan kinerja Re-ID karena hilangnya informasi, gangguan noise, dan ketidaksejajaran pandang. Penulis membagi masalah oklusi menjadi tiga bagian: masalah noise berupa campuran informasi dari ciri lingkungan yang kompleks, masalah hilangnya ciri karena hanya sebagian tubuh yang terekam, serta masalah penyelarasan karena perubahan pose, perspektif, dan posisi sehingga ciri tidak berkorespondensi satu-ke-satu. Kebaruan tinjauan ini adalah cakupan metode berbasis *vision transformer* (ViT) dan varian hibridanya, yang belum banyak dibahas tinjauan terdahulu, serta dimasukannya Re-ID 3D dan multimodal yang memakai informasi kedalaman atau modalitas tambahan.

Tanaman dan data pertanian tidak dinyatakan; objek yang dicocokkan adalah pedestrian. Mekanisme asosiasi yang dibahas adalah pencocokan identitas lintas kamera, bukan deteksi tanaman. Metode dikelompokkan menurut arsitektur (CNN, Transformer, hibrida), cara ekstraksi ciri (unimodal dan multimodal), dan struktur ciri (2D dan 3D). Kelas utama mencakup pembelajaran ciri lokal—berupa segmentasi tubuh, estimasi pose, segmentasi semantik, anotasi atribut, dan metode campuran—serta representasi relasional berupa area bersama, klaster, konvolusi graf, dan perhatian. Contoh mekanismenya adalah CBDB-Net yang membuang satu per satu potongan pita fitur untuk memaksa model belajar representasi tangguh, DPPR yang menetapkan tiga belas kotak pembatas dengan perhatian pada bagian tubuh yang sama, HOReID yang memakai titik kunci pose sebagai simpul graf topologi, dan DSA-reID yang memetakan komponen semantik 3D dari model DensePose. Pendekatan 3D memakai SMPL untuk menghasilkan enam kanal data awan titik, sedangkan pendekatan multimodal memakai citra inframerah dan peta kedalaman sebagai kanal tambahan.

Dataset dibedakan menjadi dataset oklusi, yang citranya mengandung gangguan oklusi dan tidak dipangkas, serta dataset parsial, yang bagian tubuhnya dipangkas secara buatan. Occluded-DukeMTMC memuat 15.618 citra latih dari 708 identitas, 2.210 citra kueri dari 519 identitas, dan 17.661 citra galeri dari 1.110 identitas, dengan 100% kueri dan 10% galeri beroklusi. Occluded-REID memuat 2.000 citra dari 200 pedestrian, masing-masing lima citra teroklusi dan lima citra tubuh utuh. Dataset parsial mencakup Partial-ReID (600 citra, 60 identitas), Partial-iLIDS (238 citra, 119 identitas), Partial-CAVIAR (142 citra, 72 identitas), P-ETHZ (3.897 citra, 85 identitas), dan P-DukeMTMC-reID (24.143 citra, 1.299 identitas). Metrik evaluasi adalah kurva CMC dan mAP; CMC berperingkat Rank-k hanya memeriksa hitungan pangkat teratas, sedangkan mAP memperhitungkan semua sampel, sehingga keduanya saling melengkapi.

Perbandingan hasil pada Tabel 2 hingga Tabel 4, dinyatakan dalam persen, menunjukkan bahwa tidak ada satu metode pun yang terbaik pada semua dataset. OCNet mencatat Rank-1 64,30 dan mAP 54,40 pada Occluded-DukeMTMC serta 95,00 dan 89,30 pada Market1501. CBDB-Net mencatat 50,09 dan 38,90 pada Occluded-DukeMTMC serta 94,40 dan 85,00 pada Market1501. Metode berbasis Transformer FRT mencatat 70,70 dan 61,30 pada Occluded-DukeMTMC serta 80,40 dan 71,00 pada Occluded-REID; PFD mencatat 69,50 dan 61,80 pada Occluded-DukeMTMC serta 81,50 dan 83,00 pada Occluded-REID. Penulis menyimpulkan bahwa kinerja pada dataset oklusi mencerminkan ketahanan terhadap noise, kinerja pada dataset parsial mencerminkan pengenalan dengan informasi yang hilang, dan kinerja pada dataset umum mencerminkan kemampuan menyeluruh; perhatian dan estimasi pose merupakan pendekatan yang paling umum dipakai.

Batasan yang dikemukakan penulis terutama bersumber pada data dan sistem. Sebagian besar model diuji pada dataset yang dikumpulkan di lingkungan terkontrol, padahal data dunia nyata tidak terkendali. Dataset yang ada belum memadukan beragam modalitas seperti teks, inframerah, dan peta kedalaman, belum mencakup domain dan resolusi yang lebih luas, serta masih terbatas untuk Re-ID 3D. Arah masa depan yang diusulkan mencakup dataset multimodal berkualitas tinggi, ekstraksi ciri 3D dan lintas-modal, penanganan perbedaan resolusi, model yang lebih kecil dan cepat, metode tersupervisi sebagian dan tanpa supervisi yang masih tertinggal dari metode tersupervisi, serta sistem end-to-end yang menggabungkan deteksi objek dengan Re-ID teroklusi.

