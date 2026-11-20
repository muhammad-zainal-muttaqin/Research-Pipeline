# Segment Anything

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kirillov2023segment` |
| Judul asli | Segment Anything |
| Penulis | Kirillov, Alexander; Mintun, Eric; Ravi, Nikhila; Mao, Hanzi; Rolland, Chloe; Gustafson, Laura; Xiao, Tete; Whitehead, Spencer; Berg, Alexander C.; Lo, Wan-Yen; Doll\'ar, Piotr; Girshick, Ross |
| Tahun | 2023 |
| Venue | Proceedings of the IEEE International Conference on Computer Vision |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [kirillov2023segment.pdf](../pdf/kirillov2023segment.pdf)
- DOI resmi: https://doi.org/10.1109/iccv51070.2023.00371

## Gambaran Umum

Penelitian ini membangun model dasar untuk segmentasi citra. Penulis berangkat dari keberhasilan model bahasa besar yang melakukan generalisasi tanpa pelatihan tambahan melalui rekayasa prompt, lalu menanyakan apabila hal yang sama dapat dilakukan untuk segmentasi. Masalah utamanya adalah setiap tugas segmentasi biasanya memerlukan data latih khusus, sementara tidak tersedia sumber data mask berskala web seperti halnya teks. Tujuan proyek ini terdiri dari tiga bagian yang saling terkait, yaitu merumuskan tugas segmentasi yang dapat diberi prompt, membangun model yang sesuai, serta mengumpulkan data dalam skala besar melalui sebuah mesin data. Tugas yang diusulkan bernama segmentasi dapat-diperintah, dengan ketentuan bahwa model harus menghasilkan mask yang valid untuk setiap prompt, termasuk prompt yang ambigu dan dapat merujuk pada lebih dari satu objek.

Model yang dihasilkan bernama Segment Anything Model (SAM) dan terdiri dari tiga komponen. Image encoder yang kuat menghitung representasi citra sekali saja, prompt encoder menyematkan prompt berupa titik, kotak, mask, atau teks, lalu decoder mask yang ringan menggabungkan keduanya untuk menghasilkan mask. Pemisahan ini membuat representasi citra dapat dipakai ulang untuk banyak prompt; setelah representasi dihitung, decoder menghasilkan mask dalam waktu sekitar 50 milidetik pada peramban web. Agar model sadar akan ambiguitas, SAM menghasilkan beberapa mask untuk satu prompt. Mesin data berjalan dalam tiga tahap, yaitu anotasi manual terbantu, anotasi semi-otomatis, dan anotasi otomatis penuh. Tahap akhir memberi prompt berupa kumpulan titik latar depan pada grid teratur, sehingga dihasilkan rata-rata sekitar 100 mask berkualitas per citra.

Data yang dikumpulkan bernama SA-1B dan memuat lebih dari 1 miliar mask pada 11 juta citra berlisensi yang menjaga privasi. Jumlah mask ini sekitar 400 kali lipat dari himpunan segmentasi terbesar sebelumnya, dengan jumlah citra 11 kali lebih banyak dan rata-rata 36 kali lebih banyak mask per citra. Penulis melakukan analisis keadilan dan menemukan bahwa Afrika serta negara berpenghasilan rendah tetap kurang terwakili, meskipun setiap wilayah memiliki sedikitnya 28 juta mask. Pengujian mencakup 23 himpunan data segmentasi, deteksi tepi pada BSDS500, pembangkitan usulan objek pada LVIS v1, segmentasi instance pada COCO dan LVIS, serta percobaan teks-ke-mask. Metrik yang dipakai antara lain mIoU, ODS, OIS, AP, AR@1000, dan penilaian kualitas oleh manusia pada skala 1 sampai 10.

Hasil menunjukkan kinerja tanpa pelatihan tambahan yang sering bersaing dengan metode terselia. Pada 23 himpunan data, SAM mengungguli RITM pada 16 himpunan dengan selisih mIoU hingga sekitar 47 poin; bila mask SAM yang paling sesuai dipilih dengan bantuan kebenaran, SAM mengungguli RITM pada seluruh himpunan. Penilai manusia memberi skor 7 sampai 9 untuk mask SAM. Pada deteksi tepi BSDS500, SAM mencatat ODS 0,768, OIS 0,786, AP 0,794, dan R50 0,928, sementara HED mencatat 0,788, 0,808, 0,840, dan 0,923. Pada usulan objek LVIS, SAM mencatat AR@1000 59,3 berbanding 63,0 untuk ViTDet-H, dengan keunggulan pada objek sedang (81,6 berbanding 80,8) dan kategori jarang (65,8 berbanding 58,3). Pada segmentasi instance, SAM mencatat AP 46,5 pada COCO dan 44,7 pada LVIS, sementara ViTDet-H mencatat 51,0 dan 46,6; namun dalam penilaian manusia pada LVIS, mask SAM mendapat rata-rata 8,1 berbanding 7,9 untuk ViTDet-H. Ablasi menunjukkan bahwa 1 juta citra, sekitar sepuluh persen SA-1B, memberikan hasil yang hampir sama dengan himpunan penuh, dan penggunaan hanya mask otomatis menurunkan mIoU hanya sekitar 0,5 poin.

Batasan dinyatakan penulis di bagian 8. SAM dapat melewatkan struktur halus, kadang menghasilkan komponen terputus kecil yang sebenarnya tidak ada, dan batas mask tidak setajam metode yang melakukan pemeriksaan lebih dekat. Metode interaksi khusus dengan banyak titik diharapkan mengungguli SAM karena SAM dirancang untuk keluasan penggunaan, bukan untuk mIoU tertinggi. Meskipun pemrosesan prompt berlangsung cepat, kinerja keseluruhan tidak termasuk waktu nyata bila memakai image encoder yang berat. Percobaan teks-ke-mask masih bersifat eksploratif dan belum sepenuhnya andal. Penulis juga menyatakan belum jelas bagaimana merancang prompt sederhana untuk segmentasi semantik dan panoptik, serta memperkirakan alat khusus untuk ranah tertentu akan mengungguli SAM pada ranahnya masing-masing.
