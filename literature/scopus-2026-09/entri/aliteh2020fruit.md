# Fruit battery method for oil palm fruit ripeness sensor and comparison with computer vision method

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `aliteh2020fruit` |
| Judul asli | Fruit battery method for oil palm fruit ripeness sensor and comparison with computer vision method |
| Penulis | Aliteh, Nor Aziana; Minakata, Kaiko; Tashiro, Kunihisa; Wakiwaka, Hiroyuki; Kobayashi, Kazuki; Nagata, Hirokazu; Misron, Norhisam |
| Tahun | 2020 |
| Venue | Sensors Switzerland |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [aliteh2020fruit.pdf](../pdf/aliteh2020fruit.pdf)
- DOI resmi: https://doi.org/10.3390/s20030637

## Gambaran Umum

Aliteh dan rekan (2020) menguji dua cara untuk menentukan tingkat kematangan tandan buah segar (TBS) kelapa sawit. Cara pertama adalah baterai buah: elektroda tembaga dan seng ditancapkan ke dalam buah, dengan tegangan pada beban resistor (VL) sebagai ukuran. Cara kedua adalah pengolahan citra warna dari foto tunggal menggunakan kamera iPhone 5S dengan klasifikasi *support vector machine* (SVM). Kedua cara digabungkan untuk melihat apakah hasilnya lebih baik daripada salah satunya. Hasil utamanya: akurasi baterai buah 90,4% (SD 0,0712), citra warna 86,5% (SD 0,0925), dan gabungan 94,2% (SD 0,0804).

Kajian ini berada di luar penghitungan buah. Yang diklasifikasikan adalah kematangan setiap buah. Penulis memakai ambang kadar air sebagai acuan: buah dengan kadar air di bawah 30% dianggap matang, 30 sampai 53% belum cukup matang, dan di atas 53% belum matang. Kadar air diukur dengan alat Kett FD-610 pada suhu 105 °C selama 60 menit. Sampel dikumpulkan pada 15 September sampai 15 Desember 2017 di Universiti Putra Malaysia (UPM). Kadar air dipakai sebagai acuan (*ground truth*) untuk melatih dan menguji kedua cara.

Bagian pertama, baterai buah, adalah sensor listrik. Kadar air buah berfungsi sebagai elektrolit, sehingga tegangan pada beban berubah seiring kematangan. Penulis melaporkan 52 buah untuk pengukuran kadar air dan 37 buah untuk pengukuran tegangan beban. Rentang beban terbaik adalah 10 Ω sampai 1 kΩ, dengan tingkat perubahan sekitar 76% pada bagian hasil. Pada simpulan, beban terbaik ditetapkan 1 kΩ dengan tingkat perubahan 74%, dan resolusi kadar air 0,517% per mV. Bagian kedua, citra warna, memakai kartu warna dengan penanda AR di 16 kotak untuk koreksi warna, lalu rasio warna merah terhadap hijau. Grid search diuji untuk parameter C (1, 10, 100), gamma (1, 0,1, 0,01), dan kernel (linear dan rbf), dengan validasi silang 8 lipatan.

Batas kajian ini jelas dan perlu dibaca bersama angka hasilnya. Jumlah sampel kecil: 52 dan 37 buah dari satu perkebunan dan satu musim. Akurasi gabungan dihitung pada sampel yang sama dengan kedua cara, sehingga angka gabungan tidak sebanding secara langsung dengan angka tunggal pada sampel yang lebih besar. Penulis sendiri menyebut perlunya lebih banyak sampel dan kalibrasi warna. Warna pada foto sensitif terhadap pencahayaan dan jenis kamera, dan kajian ini hanya memakai satu perangkat. Bagian citra juga hanya mengklasifikasikan buah yang sudah dipotret dari dekat, bukan menghitung buah pada pohon atau pada tumpukan.

Kajian ini menunjukkan bahwa sinyal non-citra dan citra warna saling melengkapi untuk pertanyaan kematangan. Kajian ini tidak menguji identitas buah lintas pandang dan tidak mengukur penghitungan.
