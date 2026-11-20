# Estimation of mango crop yield using image analysis - Segmentation method

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `payne2013estimation` |
| Judul asli | Estimation of mango crop yield using image analysis - Segmentation method |
| Penulis | Payne, A.B.; Walsh, K.B.; Subedi, P.P.; Jarvis, D. |
| Tahun | 2013 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | mango |

## Tautan Akses
- PDF: [payne2013estimation.pdf](../pdf/payne2013estimation.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2012.11.009

## Gambaran Umum

Payne dkk. (2013) menguji apakah penghitungan buah mangga (*Mangifera indica*) per pohon dapat dilakukan dari citra kebun. Tujuannya adalah memperkirakan beban panen (*crop load*) sebelum panen, agar pengelola kebun dapat merencanakan tenaga kerja dan pemasaran. Penghitungan dilakukan per citra. Buah tidak dikaitkan antarsisi pohon, sehingga kajian ini menghitung buah dari satu pandang atau dari dua sisi secara terpisah.

Data dikumpulkan dengan kamera Canon 50D beresolusi 4752 × 3168 piksel. Kamera diletakkan sekitar 2 m dari barisan pohon dan memotret dari sela antarbaris. Dari sekitar 56.000 pohon di kebun, 593 pohon difoto, atau sekitar 1%. Sebagai acuan kebenaran, satu operator menghitung manual seluruh buah yang terlihat di setiap citra. Buah yang jatuh atau rusak tidak dihitung. Citra dibagi menurut kondisi cahaya: terang, sedang, dan difus. Pemrosesan citra memakai segmentasi warna (RGB dan YCbCr) serta tekstur untuk memisahkan buah dari daun dan latar, lalu setiap area buah dihitung sebagai satu blob.

Hasil utama pada 555 citra adalah regresi y = 0,582x − 0,20 dengan R2 0,74 dan RMSEP 7,7 setelah koreksi bias. Nilai R2 0,91 untuk dua sisi pohon disebut dalam abstrak. Kemiringan (*slope*) di bawah 1 berarti sistem cenderung meremehkan jumlah buah, terutama pada pohon berbuah banyak. Rata-rata hitungan manual adalah 32,3 ± 14,3 buah per pohon. Cahaya matahari langsung menurunkan kemiringan regresi, sedangkan kondisi difus memberi hasil yang lebih baik. Pada kelas beban buah tinggi, R2 turun hingga 0,06. Pada subset 60 citra, hanya 51% buah yang terdeteksi dengan benar, dan tingkat positif palsu 2,4%. Penulis menyimpulkan bahwa estimasi beban panen berbasis penglihatan mesin mungkin dilakukan, tetapi pengembangan yang diperlukan masih besar, terutama untuk buah yang belum matang.

Keterbatasannya cukup jelas. Studi ini hanya menguji satu spesies (mangga) dan satu bentuk tajuk. Acuannya adalah hitungan satu operator, bukan hasil panen. Sampel hanya sekitar 1% dari populasi pohon. Studi ini tidak mengukur apakah buah yang sama dihitung dua kali pada dua sisi pohon, dan karena itu tidak dapat dijadikan bukti deduplikasi lintas pandang.
