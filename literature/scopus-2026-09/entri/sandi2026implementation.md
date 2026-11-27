# Implementation and Optimization of a Machine Learning Model for Pineapple Fruit Counting in Aerial Imagery

## Metadata Ringkas

| Bidang | Nilai |
|---|---|
| Kunci BibTeX | `sandi2026implementation` |
| Judul asli | Implementation and Optimization of a Machine Learning Model for Pineapple Fruit Counting in Aerial Imagery |
| Penulis | Johnny Zaet Aguero Sandí, Jason Leitón Jiménez, dan Luis Diego Noguera Mena |
| Tahun | 2026 |
| Prosiding | 6th International Conference on Innovative Research in Applied Science, Engineering and Technology (IRASET) |
| Kode | C1 (gabungan beberapa pengamatan) |
| Tanaman | Nanas |

## Tautan Akses

- [Naskah yang diterima](../pdf/sandi2026implementation.pdf)
- [DOI](https://doi.org/10.1109/iraset68627.2026.11538886)

## Gambaran Umum

Kajian ini mencacah nanas pada ortomosaik, yaitu peta yang dibentuk dengan menyatukan beberapa citra udara. Sistem membagi peta menjadi petak 640 × 640 piksel, memperbesar dan memperjelas tiap petak dengan Real-ESRGAN+, lalu mendeteksi buah pada ukuran 1280 × 1280 piksel dengan YOLOv8s. Posisi deteksi dikembalikan ke koordinat peta dan disimpan sebagai titik berkoordinat geografis (Bagian III.B).

Pada dua ortomosaik di luar pelatihan, model akhir menghasilkan galat cacah 8,78% di Lote Cerro (644 deteksi terhadap 706 buah yang dihitung manual) dan 38,54% di Lote Planta (177 terhadap 288). Pembanding yang dilatih dengan 616 citra menghasilkan galat masing-masing 41,08% dan 75,00%. Model akhir dilatih dengan 1.640 citra yang dihimpun lewat pelabelan ulang contoh sulit (*active learning*). Perbandingan dua model itu menilai perubahan gabungan dalam pelatihan (Bagian IV.C, Tabel II).

Tabel III melaporkan 36.852 deteksi untuk Lote Cerro pada skala ortomosaik. Angka itu menjadi pembanding awal untuk gabungan beberapa detektor dalam [Mejias-Hernandez dkk. (2026)](mejiashernandez2026automated.md). Tabel II menyediakan acuan hitung manual bagi perbandingan model dalam kajian ini. Tabel III menyediakan jumlah deteksi pada skala peta.
