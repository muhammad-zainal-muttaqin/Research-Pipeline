# Scalable person re-identification: A benchmark

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zheng2015scalable` |
| Judul asli | Scalable person re-identification: A benchmark |
| Penulis | Zheng, Liang; Shen, Liyue; Tian, Lu; Wang, Shengjin; Wang, Jingdong; Tian, Qi |
| Tahun | 2015 |
| Venue | Proceedings of the IEEE International Conference on Computer Vision |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [zheng2015scalable.pdf](../pdf/zheng2015scalable.pdf)
- DOI resmi: https://doi.org/10.1109/iccv.2015.133

## Gambaran Umum

Kajian ini membahas *person re-identification*, yaitu mencari kembali orang yang sama di dalam kumpulan citra dari kamera yang berbeda. Penulis menilai dataset yang tersedia belum memadai. Skalanya kecil, anotasinya berupa *bounding box* gambar tangan yang tidak tersedia pada kondisi nyata, dan setiap identitas hanya memiliki satu kueri serta satu kebenaran dasar. Penulis lalu menawarkan dataset baru yang lebih besar dan lebih dekat dengan kondisi sebenarnya. Sebagai kontribusi kecil, mereka juga mengusulkan representasi *Bag-of-Words* (BoW) tanpa pengawasan. Pendekatan ini memandang re-identifikasi orang sebagai kasus khusus dari pencarian citra.

Dataset utama bernama Market-1501. Dataset ini memuat 1.501 identitas yang direkam oleh 6 kamera. Total 32.668 *bounding box* beranotasi lengkap dihasilkan dengan detektor pejalan kaki *Deformable Part Model* (DPM). Penulis menambahkan himpunan *distractor* berisi lebih dari 500.000 citra yang berisi alarm palsu pada latar belakang dan pejalan kaki di luar 1.501 identitas tersebut. Setiap *bounding box* diberi label "good", "distractor", atau "junk" berdasarkan rasio tumpang tindih dengan anotasi tangan. Rasio di atas 50 persen menjadi "good", rasio di bawah 20 persen menjadi "distractor", dan kasus lainnya menjadi "junk". Data kueri berjumlah 3.368 citra. Evaluasi utama memakai *mean average precision* (mAP), yang dinilai lebih menyeluruh daripada kurva CMC.

Metode BoW memakai codebook yang dibangun dari data latih. Teknik yang digunakan mencakup root descriptor, negative evidence, burstiness weighting, avgIDF, batasan geometri lemah, masker Gauss, multiple queries, dan *reranking*. Pada tabel pengaruh ukuran codebook, nilai terbaik tercapai pada k = 350 dengan mAP 14,10 persen dan r=1 sebesar 34,38 persen. Pada tabel pengaruh jumlah stripe horizontal, M = 16 juga menghasilkan mAP 14,10 persen dan r=1 34,38 persen. Nilai M = 1 hanya menghasilkan mAP 5,23 persen. Penulis menyatakan bahwa representasi ini memberikan akurasi yang kompetitif dengan waktu respons yang cepat, karena kemiripan dihitung cukup dengan hasil kali titik.

Penulis sendiri menyebutkan beberapa batasan. Jumlah identitas pada Market-1501 (1.501) lebih rendah daripada CUHK02, sehingga penulis berencana merilis versi 2.0 dengan lebih banyak identitas. Detektor DPM juga menghasilkan *misalignment* dan bagian tubuh yang hilang, yang dapat memengaruhi akurasi. Selain itu, metode BoW diklaim hanya kompetitif, bukan unggul, pada VIPeR, CUHK03, dan Market-1501. Penulis juga mencatat bahwa kebenaran dasar penautan tiap identitas bergantung pada anotasi tangan yang dibuat untuk setiap bounding box.
