# Computer vision algorithm development for classification of palm fruit ripeness

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wong2020computer` |
| Judul asli | Computer vision algorithm development for classification of palm fruit ripeness |
| Penulis | Wong, Zhin Yue; Chew, Wei Jen; Phang, Swee King |
| Tahun | 2020 |
| Venue | Aip Conference Proceedings |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [wong2020computer.pdf](../pdf/wong2020computer.pdf)
- DOI resmi: https://doi.org/10.1063/5.0002188

## Gambaran Umum

Penulis menyatakan bahwa penilaian kematangan *fresh fruit bunch* (FFB) sawit secara manual tidak konsisten dan rawan kesalahan. Penelitian ini mengembangkan algoritme klasifikasi kematangan berbasis citra dan menjalankannya pada papan tunggal *Tinker Board* dengan kamera. Kematangan dibagi menjadi dua kelas: matang dan mentah.

Data berupa 200 citra buah sawit dari kebun di Batu Pahat, Johor, yang disediakan tim Sabri dari UiTM. Sebanyak 100 citra dipakai untuk mengembangkan algoritme, dengan 50 citra per kelas. Sisa 100 citra dipakai untuk verifikasi. Untuk pelatihan AlexNet, citra kebun dipotong manual menjadi 50 bagian per kelas. Teks tidak menyebut siapa yang memberi label kematangan.

Metode memakai AlexNet yang dilatih ulang dengan *sliding window* untuk menemukan pohon, dengan ukuran jendela 863 × 230 piksel. Untuk kematangan, citra diubah ke ruang warna HSV dan dihitung nilai rerata kanal *hue*. Buah dengan nilai 0,7 sampai 0,8 diklasifikasikan matang, dan nilai di bawah itu mentah.

Hasil utama adalah akurasi 85%, yaitu 85 dari 100 citra benar. Teks menyebut nilai hue matang berada pada rentang 0,7 sampai 0,8, dengan contoh enam citra pada Tabel 1. Teks tidak melaporkan matriks kebingungan, presisi, atau recall.

Keterbatasan yang dapat diperiksa dari teks: hanya dua kelas dan satu lokasi. Tidak ada pembagian per pohon dan tidak ada matriks kebingungan. Tabel 1 hanya memuat enam citra per kelas. Kondisi cahaya saat pengambilan citra tidak dirinci.
