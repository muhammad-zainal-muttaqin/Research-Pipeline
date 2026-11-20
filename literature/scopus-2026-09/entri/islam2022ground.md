# A Ground-based Platform for Reliable Estimates of Fruit Number, Size, and Color in Stone Fruit Orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `islam2022ground` |
| Judul asli | A Ground-based Platform for Reliable Estimates of Fruit Number, Size, and Color in Stone Fruit Orchards |
| Penulis | Islam, Muhammad S.; Scalisi, Alessio; O'Connell, Mark Glenn; Morton, Peter; Scheding, Steve; Underwood, James; Goodwin, Ian |
| Tahun | 2022 |
| Venue | Horttechnology |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | peach/nectarine, plum/apricot |

## Tautan Akses
- PDF: [islam2022ground.pdf](../pdf/islam2022ground.pdf)
- DOI resmi: https://doi.org/10.21273/horttech05098-22

## Gambaran Umum

Studi ini menghitung buah batu (aprikot, persik, nektarin, dan plum) dari platform bergerak yang memakai kamera RGB-D dan LiDAR di kebun komersial dan kebun percobaan di Australia. Hitungan deteksi per citra dikalibrasi terhadap jumlah buah total per petak yang diukur dengan penyortir buah (*fruit grader*) saat panen. Dari hitungan itu dibuat peta kepadatan buah per pohon dan per meter baris, serta perkiraan hasil.

Selain jumlah buah, platform yang sama memperkirakan diameter buah (FD) dan warna kulit. Diameter diukur dengan kaliper dan dibandingkan dengan prediksi dari kotak pembatas (*bounding box*) hasil detektor. Warna dihitung dari sudut rona (*hue angle*) dalam ruang CIELab/LCh dan diringkas menjadi indeks perkembangan warna (*color development index*, CDI) dengan rentang 0 (hijau murni) sampai 1 (merah murni).

Studi ini tidak menghubungkan buah yang sama antar-pandang atau antar-kamera. Penyesuaian dilakukan pada tingkat citra dan pohon: buah yang tersembunyi di tajuk, deteksi dari pohon di baris tetangga, dan konversi dari jumlah per citra ke jumlah per pohon.

Untuk jumlah buah, faktor kalibrasi adalah kemiringan regresi linear tanpa intersep antara hitungan platform dan jumlah buah sebenarnya per petak. Pemindaian dilakukan dari dua sisi baris (barat dan timur), lalu hasilnya dirata-ratakan untuk mengurangi negatif palsu dan positif palsu. Zona pemindaian pendek berjarak 10 m dengan 30 sampai 45 pohon per kebun dipakai sebagai data kalibrasi.

Untuk diameter dan warna, data acuan diukur pada buah dari empat jenis buah, lima sistem penyanggaan, dan tiga ketinggian tajuk. Pengukuran dilakukan sebulan sebelum panen dan saat panen, lalu data digabung. Diameter diperkirakan dalam dua tahap: deteksi buah dengan jaringan yang sama dengan penghitungan, lalu lebar metrik kotak pembatas dari LiDAR dan citra.

Studi ini melaporkan keandalan prediksi diameter dan warna terhadap pengukuran manual, tetapi keandalan jumlah buah diukur terhadap penyortir panen di petak percobaan.
