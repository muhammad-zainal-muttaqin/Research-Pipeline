# Oil palm fruit classifications by using near infrared images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kassim2014oil` |
| Judul asli | Oil palm fruit classifications by using near infrared images |
| Penulis | Kassim, Muhamad Saufi Mohd; Ismail, Wan Ishak Bin Wan; Teik, Lim Ho |
| Tahun | 2014 |
| Venue | Research Journal of Applied Sciences Engineering and Technology |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [kassim2014oil.pdf](../pdf/kassim2014oil.pdf)
- DOI resmi: https://doi.org/10.19026/rjaset.7.517

## Gambaran Umum

Kajian ini menilai apakah citra *multispektral* dapat menentukan tingkat kematangan tandan buah segar (TBS) kelapa sawit. Penulis menyebut bahwa panen pada waktu yang tepat menentukan mutu dan rendemen minyak. Kematangan saat ini dinilai dari jumlah brondolan (buah yang lepas dari tandan) dan penilaian mata manusia. Tujuan lain adalah membangun sistem informasi geografis (*GIS*) yang memetakan kematangan per pohon untuk menjadwalkan panen.

Data berasal dari 466 pohon sawit berumur lima tahun di kebun 8 ha Universiti Putra Malaysia. Satu tandan per pohon dipilih dan difoto dengan kamera *Tetracam* yang merekam pita merah, hijau, dan *near infrared* (NIR). Tingkat kematangan ditetapkan ahli manusia pada rentang 5 sampai 24 minggu setelah antesis. Analisis utama memakai 50 citra. Sepuluh pohon (P11 sampai P47) dipisahkan sebagai data uji. Teks tidak menyebut pembagian per pohon untuk seluruh citra.

Nilai *hue* NIR tiap citra dihitung. *Koefisien variasi* (CV, simpangan baku dibagi rata-rata) dihitung per minggu untuk memilih rentang nilai 235 sampai 241, yang dipakai menyusun bagan acuan. Dua cara klasifikasi dibandingkan: jarak *Euclidean* terhadap nilai acuan, dan pencocokan gradien pada bagan. Jumlah piksel dan *insertion loss* dipakai sebagai fitur pendukung. Kadar air metode oven dan sensor *microstrip* dipakai sebagai acuan kebenaran.

Hasil utama pada data uji: jarak Euclidean menempatkan 50% sampel dalam galat ±1 minggu, sedangkan pencocokan gradien menempatkan 60% dalam galat ±1 minggu. Kesimpulan penulis menyebut akurasi 50 sampai 60%. Teks tidak melaporkan akurasi per kelas minggu. Penulis sendiri menyatakan bahwa nilai hue NIR saja tidak cukup untuk berkorelasi dengan data sensor.

Keterbatasan yang dapat diperiksa: data uji hanya 10 pohon dan tidak ada ukuran ketidakpastian. Sudut kamera dan jarak pemotretan tidak dikendalikan, sebagaimana diakui penulis. Label minggu bergantung pada sensor yang dikalibrasi manusia. Tidak ada hitung buah.
