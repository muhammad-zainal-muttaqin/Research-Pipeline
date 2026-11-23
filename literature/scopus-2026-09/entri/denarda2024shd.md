# SHD-O2D: A Novel Image Dataset for Super-High-Density Olive Orchard Yield Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `denarda2024shd` |
| Judul asli | SHD-O2D: A Novel Image Dataset for Super-High-Density Olive Orchard Yield Estimation |
| Penulis | Denarda, Alessandro Rocco; Marchionni, Damiano; Crocetti, Francesco; Costante, Gabriele; Valigi, Paolo; Famiani, Franco; Fravolini, Mario Luca |
| Tahun | 2024 |
| Venue | 2024 IEEE International Workshop on Metrology for Agriculture and Forestry Metroagrifor 2024 Proceedings |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | olive |

## Tautan Akses
- PDF: [denarda2024shd.pdf](../pdf/denarda2024shd.pdf)
- DOI resmi: https://doi.org/10.1109/metroagrifor63043.2024.10948806

## Gambaran Umum

Penulis menyajikan SHD-O2D, set data citra kebun zaitun berkepadatan sangat tinggi (*super-high-density*, SHD) untuk estimasi hasil panen. Masalah yang disebut adalah kurangnya set data khusus buah yang diperlukan untuk melatih sistem *computer vision*, serta mahalnya pelabelan manual dengan kotak pembatas atau label piksel. Karena itu penulis mengevaluasi paradigma *weakly supervised* (pelatihan dengan label tingkat citra, bukan label per buah) sebagai penerapan pertama set data ini.

Data dikumpulkan dari satu baris pohon zaitun kultivar Piantone di Mogliano, berumur tujuh tahun, di Wilayah Umbria, Italia. Baris itu terdiri atas 100 pohon dengan jarak tanam 5,0 x 1,8 m. Pengambilan citra dilakukan empat sesi pada Oktober sampai November 2023: dua sesi sebelum panen (cerah dan berawan) dan dua sesi sesudah panen. Tiap sesi memotret sisi timur dan barat setiap pohon, sehingga tiap pohon memiliki delapan citra dan set data memuat 800 citra beresolusi 4608 x 2592 dari kamera Panasonic Lumix DMC-CH4 pada mode otomatis. Berat zaitun hasil panen ditimbang per pohon, dan berat rata-rata satu buah ditentukan dari sampel 50 buah. Dari keduanya dihitung jumlah buah per pohon sebagai acuan (*ground truth*) estimasi. Pada lima pohon (nomor 2, 28, 38, 49, dan 64), empat citra sebelum panen dipotong menjadi 256 petak dan buah dihitung manual.

Metode memakai jaringan *encoder-decoder* dengan blok residual ResNet yang dilatih dengan label ada atau tidaknya buah. Jaringan dioptimalkan dengan modul perhatian (*attention*) dan menghasilkan peta aktivasi delapan kanal yang dijumlahkan menjadi satu peta panas (*heatmap*). Posisi buah diambil sebagai maksimum lokal peta panas dengan detektor TC-LMD dengan ambang skor isi 18,99. Pelatihan tahap pertama memakai set data OliveISAR (1.402 petak, 1.298 latih dan 104 validasi). Tahap kedua menyetel ulang (*fine-tuning*) model dengan petak dari delapan citra satu pohon (pohon 2): 1.768 petak latih dan 280 validasi. Pengujian dilakukan pada seluruh 800 citra, tiap citra dipotong 256 petak lalu peta panasnya disusun kembali. Optimizer yang dipakai SGD dengan laju belajar awal 0,1, dikali 0,5 tiap 10 *epoch*, ukuran *batch* 24.

Karena jumlah buah panen tidak sama dengan buah yang tampak pada satu citra, penulis menetapkan faktor skala dari hitung manual lima pohon. Faktor itu 3,18 untuk citra cerah dan 2,20 untuk citra berawan. Acuan RMSE adalah jumlah buah panen dibagi faktor skala. RMSE jumlah buah pada citra sebelum panen adalah 462,32 (cerah) dan 875,90 (berawan), setara 1,11 kg dan 2,13 kg. Pada citra sesudah panen RMSE hanya 7,86 (cerah) dan 1,42 (berawan), setara 0,02 kg dan 0,01 kg. Penulis menyimpulkan kondisi cerah lebih sesuai untuk estimasi, walaupun hitung manual menunjukkan lebih banyak buah tampak saat berawan.

Keterbatasan yang dapat diperiksa dari teks: faktor skala diturunkan dari hanya lima pohon, dan pohon 2 yang dipakai untuk *fine-tuning* juga termasuk dalam set uji 800 citra, tanpa pembagian per pohon yang terpisah. Acuan hitung berasal dari berat panen dan berat rata-rata buah, bukan hitung tangan di pohon. Faktor skala dibentuk dari jumlah hitungan sisi timur dan barat, tetapi teks tidak menulis tegas bahwa deteksi kedua sisi juga dijumlahkan per pohon. Tidak ada penautan buah antarcitra. Kesalahan hasil uji hanya dilaporkan sebagai RMSE tanpa MAE atau galat relatif, dan hanya satu baris kebun serta satu kultivar yang dicakup.
