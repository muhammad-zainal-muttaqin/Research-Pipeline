# Enhancing citrus fruit yield investigations through flight height optimization with UAV imaging

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kwon2024enhancing` |
| Judul asli | Enhancing citrus fruit yield investigations through flight height optimization with UAV imaging |
| Penulis | Kwon, Soon-Hwa; Ku, Ki Bon; Le, Anh Tuan; Han, Gyung Deok; Park, Yosup; Kim, Jaehong; Tuan, Thai Thanh; Chung, Yong Suk; Mansoor, Sheikh |
| Tahun | 2024 |
| Venue | Scientific Reports |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [kwon2024enhancing.pdf](../pdf/kwon2024enhancing.pdf)
- DOI resmi: https://doi.org/10.1038/s41598-023-50921-8

## Gambaran Umum

Kajian kwon2024enhancing (Scientific Reports 14:322, 2024) menguji apakah jumlah buah jeruk (*Citrus unshiu*) dapat diestimasi dari citra RGB yang diambil UAV dari satu sudut pandang. Setiap pohon difoto pada lima ketinggian terbang, yaitu 30, 50, 70, 90, dan 110 m. Buah dipisahkan dari daun dengan ambang warna, lalu jumlah piksel buah dikonversi menjadi estimasi jumlah buah. Hasilnya dibandingkan dengan panen aktual.

Penelitian memakai tiga pohon per ketinggian. Dua kondisi citra diuji: citra RGB asli dan citra yang diberi *histogram equalization* (penyetaraan histogram, yaitu peregangan kontras agar buah yang gelap lebih mudah terlihat). Untuk pemisahan buah dari latar, penulis menguji tiga indeks vegetasi: IPCA, CIVE, dan I1. Indeks vegetasi adalah rumus aritmetika pada nilai kanal warna yang menonjolkan objek hijau atau kuning. Jumlah piksel buah kemudian dihitung dengan Persamaan 6 di naskah untuk menghasilkan estimasi jumlah buah.

Jumlah piksel buah turun tajam seiring ketinggian. Pada citra asli, rata-rata piksel buah adalah 33.208 pada 30 m dan 14 pada 110 m (Tabel 4). Equalization menaikkan jumlah piksel buah pada semua ketinggian. Perbedaan signifikan hanya pada 50 m (p = 0,03). Pada 30 m, perbedaannya tidak signifikan (p = 0,31).

Estimasi jumlah buah pada 30 m dengan equalization adalah 88, 71, dan 105 untuk tiga pohon, dengan panen aktual 124, 88, dan 141 (Tabel 3 dan 5). Citra asli pada 30 m memberi 73, 55, dan 88. Pada 110 m, citra asli tidak mendeteksi buah pada dua dari tiga pohon. Indeks IPCA memberi hasil yang mirip dengan equalization. Indeks I1 disimpulkan tidak cocok untuk jeruk.

Penulis menyimpulkan bahwa citra 30 m lebih tepat daripada 110 m, dan equalization mungkin lebih akurat daripada citra asli. Mereka juga menulis bahwa kepekaan deteksi bergantung pada jenis indeks vegetasi. Jumlah buah yang tersembunyi dapat diperkirakan secara kasar dengan koefisien koreksi, tetapi akurasinya bergantung pada pascapemrosesan.

Dari sisi desain, jumlah pohon sangat kecil (tiga per ketinggian), sehingga uji signifikansi pada 50 m dan 70 m hanya didasarkan pada sedikit sampel. Estimasi dihitung dari satu pandang per pohon, sehingga buah yang tertutup daun tidak terdeteksi. Penulis menyebut kondisi ini sebagai alasan koreksi koefisien. Basis data pembanding (panen Agustus 2021, rata-rata 842 buah per pohon) tidak dirinci per pohon dalam bagian yang dibaca.

Kunci BibTeX: kwon2024enhancing.
