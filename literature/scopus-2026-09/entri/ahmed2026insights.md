# Insights into recent developments and obstacles in automated fruit ripeness classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ahmed2026insights` |
| Judul asli | Insights into recent developments and obstacles in automated fruit ripeness classification |
| Penulis | Ahmed, Zienab F.R.; Abdalla, Abdelmoneim K.; Kaur, Navjot; Wu, Falin |
| Tahun | 2026 |
| Venue | Green Technologies and Sustainability |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [ahmed2026insights.pdf](../pdf/ahmed2026insights.pdf)
- DOI resmi: https://doi.org/10.1016/j.grets.2025.100302

## Gambaran Umum

Tinjauan ini membahas klasifikasi tingkat kematangan buah secara otomatis, dengan sensor yang tidak merusak buah dan kecerdasan buatan (AI). Kajian ini diterbitkan di *Green Technologies and Sustainability* 4 (2026) 100302 dan memuat tiga kelompok metode: spektroskopi, sensor aroma (*electronic nose*), dan sensor taktil atau kekerasan buah, serta bagian khusus untuk warna dan citra. Cakupan waktu tabel utama adalah 2020 sampai 2024.

Tinjauan ini tidak membahas penghitungan buah di kebun atau kelapa sawit. Fokusnya adalah satu buah pada satu waktu, bukan jumlah buah dalam pohon atau tanaman.

Menurut abstrak, pendekatan yang paling efektif didominasi strategi AI, yaitu pembelajaran mesin (ML), pembelajaran mendalam (DL), dan kecerdasan buatan yang dapat dijelaskan (XAI). Tantangan utama yang disebut adalah variabilitas lingkungan, kemampuan generalisasi, dan kualitas data, serta penulis menganjurkan metodologi standar agar hasil dapat direproduksi dan dibandingkan.

Bagian spektroskopi (Tabel 1) memuat contoh dengan angka yang dilaporkan penulisnya. Pada durian, klasifikasi tingkat kematangan dengan LDA dan sensor NIR 900 sampai 1600 nm mencapai 100% akurasi. Pada blackberry, CNN VGG16 multi-masukan dengan citra stereo mencapai 95,1% pada data uji dan 90,2% pada kondisi lapangan. Pada tomat, R-CNN dengan ResNet-101 mencapai rerata presisi deteksi 87,83%. Angka ini berasal dari data dan protokol masing-masing kajian, sehingga tidak dapat dibandingkan langsung satu sama lain.

Bagian sensor aroma dan taktil (Tabel 2) memuat hasil yang lebih rendah dan lebih beragam. Pada durian, e-nose dengan jaringan saraf mencapai 91%. Pada apel Golden Delicious, KNN dengan empat sensor MOS mencapai akurasi di atas 75%, dengan 100% pada subset tertentu. Pada tomat dan nektarin, sensor taktil dengan ResNet-LSTM mencapai 84,6% dan 81,5%. Pada alpukat, ResNet-34 dengan data taktil dan citra mencapai tingkat keberhasilan 96,0%. Penulis tinjauan sendiri mencatat bahwa sensor aroma kesulitan membedakan campuran senyawa, dan sensor taktil tidak menangkap warna serta rasa.
