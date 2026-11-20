# Human tracking over camera networks: a review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hou2017human` |
| Judul asli | Human tracking over camera networks: a review |
| Penulis | Hou, Li; Wan, Wanggen; Hwang, Jenq-Neng; Muhammad, Rizwan; Yang, Mingyang; Han, Kang |
| Tahun | 2017 |
| Venue | Eurasip Journal on Advances in Signal Processing |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [hou2017human.pdf](../pdf/hou2017human.pdf)
- DOI resmi: https://doi.org/10.1186/s13634-017-0482-z

## Gambaran Umum

Makalah ini adalah tinjauan (survei) tentang pelacakan manusia melalui jaringan kamera. Penulisnya membahas teknik yang paling banyak dipakai dan kemajuan terbarunya.

Pelacakan manusia dalam sistem pengawasan harus mempertahankan identitas satu orang saat ia bergerak di dalam satu kamera dan berpindah ke kamera lain. Masalah kedua ini lebih sulit karena pandangan antarkamera tidak selalu beririsan.

Pengelompokan ini menjadi kerangka utama tulisan.

Untuk pelacakan lintas kamera, re-identifikasi mencocokkan tampilan seseorang dengan kandidat dari kamera lain. Makalah membagi riset re-identifikasi menjadi dua arah: ekstraksi fitur dan pembelajaran metrik jarak. CLM memodelkan hubungan antarkamera, dan dapat dilatih secara terawasi maupun tidak terawasi. GM menyatakan seluruh jaringan kamera sebagai graf, dan penyelesaiannya dilakukan melalui estimasi MAP (*maximum a posteriori*).

Fitur yang dipakai untuk mencocokkan orang antarkamera mencakup warna, tekstur, bentuk, fitur global, fitur regional, fitur berbasis patch, dan fitur semantik. Makalah mencatat bahwa fitur warna relatif tahan terhadap perubahan sudut pandang, tetapi tidak tahan terhadap perubahan pencahayaan yang kuat. Fitur tekstur dan bentuk stabil terhadap perubahan cahaya, tetapi peka terhadap sudut pandang dan oklusi.

Angka yang dikutip berasal dari kajian yang ditinjau. Tabel 5 memuat skor pencocokan kumulatif (*cumulative matching score*) pada benchmark VIPeR untuk 12 metode re-identifikasi, pada peringkat 1, 10, dan 20. Contohnya FFN 51,1 / 91,4 / 96,9 dan SCSP 53,5 / 91,5 / 96,6. Bagian kesimpulan menyatakan bahwa akurasi peringkat-1 metode mutakhir re-identifikasi "kurang dari 60%" pada VIPeR.

Namun, data yang dibahas hanya pelacakan dan re-identifikasi manusia. Tidak ada hasil penghitungan objek, buah, atau tanaman dalam teks. Teknik ini belum diuji pada penghitungan buah. Ketergantungan pada fitur tampilan manusia perlu diuji ulang untuk objek yang bentuknya kurang bervariasi.
