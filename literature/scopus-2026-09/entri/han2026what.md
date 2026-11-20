# What's next in agri-vision: A review of Vision Transformers and Vision Mamba in crop management

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `han2026what` |
| Judul asli | What's next in agri-vision: A review of Vision Transformers and Vision Mamba in crop management |
| Penulis | Han, Kangrui; Hua, Weiyun; He, Long |
| Tahun | 2026 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [han2026what.pdf](../pdf/han2026what.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2026.111551

## Gambaran Umum

CNN memiliki *receptive field* lokal, sehingga sulit menangkap hubungan spasial berjarak jauh, oklusi berat, dan variasi skala yang lazim di kebun. ViT menambahkan konteks global lewat *self-attention*. ViM menggantikan *self-attention* dengan *state-space model* selektif yang kompleksitasnya linear terhadap panjang urutan, sehingga lebih ringan untuk citra beresolusi tinggi. Penulis mengajukan dua pertanyaan: arsitektur mana yang cocok untuk dipakai di lapangan, dan bagaimana desain baru menangani kelangkaan data, variasi lingkungan, dan batas perangkat *edge*.

Pencarian dilakukan di Google Scholar, ScienceDirect, MDPI, dan IEEE Xplore, dengan periode mulai Januari 2020. Pencarian awal menghasilkan 5.577 hasil, yaitu Google Scholar 4.706, ScienceDirect 576, MDPI 247, dan IEEE Xplore 48. Penyaringan judul, abstrak, dan kata kunci menyisakan 207 rekaman. Penilaian mendalam menghasilkan 112 makalah, lalu 11 makalah ilmu komputer ditambahkan sehingga total 123 makalah. Dari 123 makalah, 91 membahas manajemen tanaman: 30 tentang deteksi penyakit, 25 tentang serangga dan gulma, 24 tentang deteksi tanaman dan prediksi hasil, dan 13 tentang lahan, tanah, serta air.

Sintesis menghasilkan tiga pola. Pertama, ViT cenderung melampaui baseline CNN pada kondisi lapangan yang berantakan dan bervariasi, dengan syarat data cukup dan pelatihannya tepat. Kedua, ViM memberi keseimbangan akurasi dan efisiensi yang baik untuk perangkat *edge* dan UAV. Ketiga, desain hibrida, misalnya CNN yang digabung dengan kepala ViT atau ViM, atau ViM sebagai leher detektor, lebih andal pada cahaya rendah dan kanopi yang rapat. Pencacahan buah dan estimasi hasil menjadi salah satu dari empat bidang yang disintesis, bersama penyakit, hama dan gulma, serta lahan, tanah, dan air. Bagian pembahasan ini memakai ringkasan abstrak; angka kuantitatif per studi tidak diulang di sini.

Penulis menyebut empat tantangan yang masih ada. Keragaman data lintas lokasi terbatas. Model peka terhadap perubahan cahaya dan oklusi. Energi dan latensi perangkat *edge* membatasi penerapan. Interpretabilitas model juga terbatas. Sebagai arah ke depan, penulis mengusulkan uji pergeseran domain yang distandarkan, pelaporan energi dan latensi, kuantisasi atau distilasi untuk *edge*, keluaran yang memuat ketidakpastian, dan fusi multimodal yang berprinsip. Penulis menyatakan bahwa arah ini dapat membawa pipeline berbasis ViM atau hibrida ke tahap praktis untuk pertanian lapangan.
