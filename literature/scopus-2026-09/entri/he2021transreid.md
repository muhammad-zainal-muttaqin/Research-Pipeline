# TransReID: Transformer-based Object Re-Identification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `he2021transreid` |
| Judul asli | TransReID: Transformer-based Object Re-Identification |
| Penulis | He, Shuting; Luo, Hao; Wang, Pichao; Wang, Fan; Li, Hao; Jiang, Wei |
| Tahun | 2021 |
| Venue | Proceedings of the IEEE International Conference on Computer Vision |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [he2021transreid.pdf](../pdf/he2021transreid.pdf)
- DOI resmi: https://doi.org/10.1109/iccv48922.2021.01474

## Gambaran Umum

Masalah utama adalah ekstraksi representasi fitur yang tangguh untuk identifikasi ulang objek (*object re-identification*, ReID), yaitu mengaitkan suatu objek lintas adegan dan pandang kamera. Metode berbasis jaringan saraf konvolusional (CNN) hanya memproses satu lingkungan lokal pada satu waktu dan kehilangan detail akibat operasi konvolusi serta penurunan sampel seperti *pooling* dan konvolusi berlangkah. CNN juga memiliki medan reseptif efektif berdistribusi Gauss sehingga lebih mengutamakan wilayah terus-menerus yang besar dan sulit mengekstrak beberapa bagian diskriminatif yang tersebar. Penelitian ini mengajukan TransReID, kerangka ReID murni berbasis *transformer* pertama sepanjang pengetahuan penulis. Tanaman tidak dibahas karena kajian ini berada di luar domain pertanian.

Data uji terdiri dari empat dataset ReID orang — Market-1501 (1.501 identitas, 32.668 citra, 6 kamera), DukeMTMC-reID (1.404 identitas, 36.441 citra, 8 kamera), MSMT17 (4.101 identitas, 126.441 citra, 15 kamera), dan Occluded-Duke (1.404 identitas, 36.441 citra, 8 kamera) — serta dua dataset ReID kendaraan, VeRi-776 (776 identitas, 49.357 citra, 20 kamera, 8 sudut pandang) dan VehicleID (26.328 identitas, 221.567 citra, 2 sudut pandang). Citra orang diubah ke ukuran 256×128 dan citra kendaraan ke 256×256. Bobot awal ViT dilatih awal pada ImageNet-21K lalu disempurnakan pada ImageNet-1K, sedangkan DeiT hanya pada ImageNet-1K. Pelatihan memakai satu GPU Nvidia Tesla V100 dengan PyTorch dan presisi FP16.

Mekanisme deteksi dan asosiasi berupa pembangkitan representasi fitur, bukan deteksi kotak. Citra dibagi menjadi deretan *patch* berukuran tetap, diberi token [cls] yang dapat dipelajari serta penyisipan posisi, lalu diproses oleh lapisan *transformer* dengan medan reseptif global dan tanpa penurunan sampel. Dua modul ditambahkan: *jigsaw patch module* (JPM) yang menggeser dan mengacak penyisipan *patch* lalu mengelompokkannya kembali agar fitur lokal mencakup bagian tubuh atau kendaraan yang beragam, dan *side information embedding* (SIE) yang menyisipkan penyisipan yang dapat dipelajari untuk informasi kamera dan sudut pandang guna mengurangi bias karena perbedaan pandang. Fitur global dari token [cls] dan fitur lokal dari JPM diawasi bersama oleh *ID loss* (entropi silang) dan *triplet loss* ber margin lunak; saat inferensi, keduanya dirangkai menjadi representasi akhir. Pengenalan tempat tidak dibahas; asosiasi dilakukan melalui kemiripan fitur ReID.

Hasil diukur dengan kurva *Cumulative Matching Characteristic* (CMC) dan *mean Average Precision* (mAP). Baselines ViT-B/16 memperoleh 61,0% mAP dan 81,8% Rank-1 pada MSMT17 serta 78,2% mAP dan 96,5% Rank-1 pada VeRi-776. Modul JPM menaikkan mAP masing-masing 2,6 dan 1,0 poin persentase; SIE menaikkan 1,4 poin persentase pada kedua dataset, dengan penyandian gabungan S(C,V) menghasilkan 79,6% mAP pada VeRi-776 berbanding 78,3% jika kedua penyisipan dijumlahkan. TransReID dengan kedua modul mencapai 64,9% mAP dan 83,3% Rank-1 pada MSMT17 serta 80,6% mAP dan 96,9% Rank-1 pada VeRi-776. Varian TransReID* memakai *patch* tumpang tindih dan pada MSMT17 serta DukeMTMC-reID mengungguli metode terbaik sebelumnya masing-masing 5,5 dan 2,1 poin persentase mAP; pada Occluded-Duke mencapai 58,1% mAP, pada VeRi-776 82,3% mAP, dan pada VehicleID 85,2% Rank-1. TransReID* juga 4,8% lebih cepat daripada MGN pada perangkat keras yang sama.

Batasan penulis tidak dinyatakan dalam bagian tersendiri. Penulis hanya mencatat bahwa penurunan langkah *sliding window* menaikkan kinerja sekaligus waktu inferensi, dan bahwa desain jaringan *transformer* yang lebih efisien dengan daya representasi lebih baik serta biaya komputasi lebih rendah masih menjadi prospek penelitian. Informasi sudut pandang hanya tersedia pada VeRi-776 dan VehicleID, sehingga modul SIE tidak dapat memakannya pada dataset orang; hasil VehicleID hanya memakai himpunan bagian kecil.
