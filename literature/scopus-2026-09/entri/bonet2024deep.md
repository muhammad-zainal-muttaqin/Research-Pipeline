# Deep Learning Model to Predict the Ripeness of Oil Palm Fruit

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `bonet2024deep` |
| Judul asli | Deep Learning Model to Predict the Ripeness of Oil Palm Fruit |
| Penulis | Bonet, Isis; Gongora, Mario; Acevedo, Fernando; Ochoa, Ivan |
| Tahun | 2024 |
| Venue | International Conference on Agents and Artificial Intelligence |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [bonet2024deep.pdf](../pdf/bonet2024deep.pdf)
- DOI resmi: https://doi.org/10.5220/0012434600003636

## Gambaran Umum

Kajian ini melatih YOLOv8 untuk mendeteksi tandan buah segar (TBS) kelapa sawit dan mengklasifikasikannya menurut tingkat kematangan. Data diambil dari video dan foto di rampa pemuatan area produksi. Hasil utama: precision 96,5%, recall 95%, mAP50 98%, dan mAP50-95 80% pada data yang dilaporkan teks.

Data yang dianotasi berjumlah 390 tandan dari 65 citra video, terdiri atas 65 tandan mentah (unripe), 203 matang (ripe), dan 122 terlalu matang (overripe). Setelah augmentasi tersedia 165 citra latih, dengan 156 label immature, 642 label mature, dan 309 label overripe. Teks tidak menjelaskan hubungan antara 390 tandan teranotasi dan 165 citra latih, serta tidak menjelaskan mengapa nama kelas berganti dari unripe ke green dan dari ripe ke mature. Pelatihan memakai transfer learning selama 300 epoch dengan batch size 16.

Hasil pada data validasi: precision 96,5%, recall 95%, mAP50 98%, mAP50-95 80%, dan mAP validasi 94,3%. Tabel 1 melaporkan precision per kelas: unripe 92, ripe 85, dan overripe 93. Kelas ripe memiliki precision terendah, sehingga kesimpulan teks yang menyebut model "more accurate in unripe and ripe stages" tidak sejalan dengan tabel tersebut. Teks hanya melaporkan data validasi; pemisahan data uji (test) belum ditemukan dalam bacaan.

Dari sisi pencacahan, kajian ini tidak menautkan tandan yang sama antarframe video atau antarpandang.

Jumlah video dan durasinya juga tidak dijelaskan secara terpisah dari 65 citra yang dianotasi.
