# Transferability and Robustness in Proximal and UAV Crop Imaging

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `barbedo2026transferability` |
| Judul asli | Transferability and Robustness in Proximal and UAV Crop Imaging |
| Penulis | Barbedo, Jayme Garcia Arnal |
| Tahun | 2026 |
| Venue | Agronomy |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [barbedo2026transferability.pdf](../pdf/barbedo2026transferability.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy16030364

## Gambaran Umum

Tinjauan ini membahas ketahanan model pencitraan tanaman pada platform
proksimal dan pesawat tanpa awak (UAV). Pencitraan berbasis kecerdasan
buatan digunakan untuk deteksi penyakit dan stres, estimasi hasil, struktur
kanopi, dan pencacahan buah. Penulis berpendapat bahwa hambatan utama bukan
lagi akurasi mentah, melainkan ketahanan terhadap pergeseran distribusi:
model yang dilatih pada satu lahan, musim, kultivar, atau sensor sering
gagal ketika adegan, sensor, protokol, atau waktu akuisisi berubah secara
wajar. Tinjauan ini menyusun bukti tentang ketahanan dan keterpindahan
serta memetakan kapan citra RGB saja memadai dan kapan moda multispektral,
hiperspektral, atau termal berpotensi membantu.

Bahan tinjauan adalah 42 kajian inti yang diperoleh melalui pencarian
terstruktur pada 8 Oktober 2025 tanpa batas tahun terbit. Kueri Scopus
menghasilkan 98 rekaman dan Web of Science 62 rekaman, dengan 54 rekaman
tumpang tindih, sehingga terkumpul 106 artikel unik setelah deduplikasi.
Penyaringan menghasilkan 42 artikel inti berdasarkan kriteria: berbahasa
Inggris, secara teks membahas pergeseran distribusi dalam pencitraan
tanaman, serta memakai pencitraan proksimal atau UAV. Kajian yang hanya
menyinggung ketahanan secara tidak langsung, memakai citra satelit murni,
atau tidak memiliki komponen visi komputer dikeluarkan. Penelusuran mundur
dari daftar pustaka ke-42 artikel tidak menambah kajian baru. Tanaman yang
dicakup adalah gandum, padi, jagung, kedelai, apel, jeruk, mangga, tomat,
anggur, dan pir, ditambah konteks rumah kaca serta pencitraan akar dan
tanah. Setiap artikel dikodekan menurut tanaman, tugas, sensor, platform,
dan sumbu pergeseran. Sintesisnya bersifat deskriptif, bukan statistik,
sehingga tidak dilaporkan satu metrik akurasi gabungan; metrik dan angka
dinyatakan tidak dinyatakan secara terpadu dalam tinjauan ini.

Mekanisme penyusunan tinjauan bertumpu pada empat sumbu pergeseran, yaitu
adegan, sensor, protokol, dan waktu. Pergeseran adegan mengubah geometri
kanopi, latar, dan pengelolaan; pergeseran sensor membawa perbedaan respons
spektral, resolusi, dan derau; pergeseran protokol mengubah geometri pandang,
iluminasi, dan radiometri; sedangkan pergeseran waktu mencakup fenologi,
musim, dan tahun. Penulis memetakan bukti bahwa garis dasar RGB yang
diperoleh dan dievaluasi secara cermat sering cukup, sedangkan moda
tambahan paling membantu untuk sifat fisiologis seperti nitrogen,
klorofil, dan stres air atau ketika pencahayaan dan latar tidak stabil.
Adaptasi disusun bertahap sesuai gejala: normalisasi dan augmentasi,
penyesuaian halus dengan 10–30% sampel sasaran, penyejajaran fitur dangkal
seperti transfer component analysis, adaptasi domain tanpa label,
terjemahan gaya, serta pembaruan saat uji dan kalibrasi. Penulis menegaskan
bahwa pembagian data acak pada tingkat piksel atau keping menaikkan angka
secara palsu karena kebocoran konteks, sehingga diperlukan pembagian
leave-one-field-out dan leave-one-season-out. Tolok ukur yang disarankan
mencakup minimal tiga lahan dan satu musim yang disisihkan, kartu protokol,
serta paket percobaan E0–E5 dengan anggaran label sasaran 0%, 5%, 10%,
dan 20%.

Penulis menyatakan lima batasan. Pertama, korpus inti dibatasi oleh kueri
tertentu, daftar tanaman tertentu, dan hanya artikel berbahasa Inggris,
sehingga kajian dalam bahasa lain, tanaman di luar daftar, atau artikel
dengan istilah berbeda dapat terlewat. Kedua, pembatasan pada istilah
ketahanan di judul secara sengaja memusatkan perhatian pada kajian yang
menjadikan pergeseran distribusi sebagai pokok, tetapi dengan sendirinya
menyingkirkan banyak artikel bermutu yang tidak menonjolkan konsep tersebut.
Ketiga, heterogenitas tugas, sensor, dan protokol menghalangi meta-analisis
besaran efek, sehingga sintesis bersifat deskriptif dan konseptual. Keempat,
kajian satelit murni, jaringan sensor noncitra, dan sistem pertanian digital
yang lebih luas hanya disinggung bila relevan, sehingga simpulan tidak
langsung dapat dipindahkan ke bidang tersebut. Kelima, pencarian dan
pengodean dilakukan oleh penilai yang jumlahnya terbatas dan mengandung
keputusan subjektif pada kasus tepi.
