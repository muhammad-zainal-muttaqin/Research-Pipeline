# Enhanced Palm Oil Image Quality Using RGF-ESRGAN Architecture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fadillah2025enhanced` |
| Judul asli | Enhanced Palm Oil Image Quality Using RGF-ESRGAN Architecture |
| Penulis | Fadillah, Arif; Desiani, Anita; Rini, Dian Palupi; Kesuma, Lucky Indra; Gofar, Nuni; Ramadhan, Faishal Fitra; Kurniawan, Rifki |
| Tahun | 2025 |
| Venue | Proceedings 7th International Conference on Informatics Multimedia Cyber and Information System Icimcis 2025 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [fadillah2025enhanced.pdf](../pdf/fadillah2025enhanced.pdf)
- DOI resmi: https://doi.org/10.1109/icimcis68501.2025.11327377

## Gambaran Umum

Penelitian ini bertujuan memperbaiki kualitas citra tandan kelapa sawit sebelum klasifikasi kematangan. Penulis menyebut kualitas citra turun akibat derau, pencahayaan tidak merata, dan perbedaan kondisi pengambilan di lapangan. Mereka mengusulkan gabungan dua tahap peningkatan citra: *Rolling Guidance Filter* (RGF) dan *Enhanced Super-Resolution Generative Adversarial Network* (ESRGAN).

Data adalah set data publik "Ripeness of oil palm fruit" dengan tiga kelas (mentah, matang, terlalu matang), masing-masing 460 citra, total 1.380 citra. Sensor, tempat pengambilan, pemberi label, dan jumlah pohon tidak disebut. Pembagian data latih dan uji untuk peningkatan citra tidak disebut. Untuk uji klasifikasi, pembagian data juga tidak disebut.

RGF adalah tapis iteratif yang membobot piksel menurut jarak spasial dan selisih intensitas untuk meredam derau sambil menjaga tepi. RGF dapat mengaburkan detail halus. ESRGAN adalah jaringan generatif yang menaikkan resolusi dengan generator berblok residual dan diskriminator, dan dipakai untuk memulihkan detail itu. Mutu citra diukur dengan *Peak Signal-to-Noise Ratio* (PSNR, kedekatan nilai piksel), *Structural Similarity Index Measure* (SSIM, kemiripan struktur), dan *Fréchet Inception Distance* (FID, jarak sebaran fitur). Klasifikasi memakai *convolutional neural network* (CNN) yang arsitekturnya tidak dirinci.

Gabungan RGF-ESRGAN memperoleh PSNR 32,26 dB, SSIM 0,94, dan FID 6,78. RGF saja atau ESRGAN saja disebut memperoleh PSNR di bawah 30, SSIM di bawah 0,9, dan FID di atas 10. Akurasi klasifikasi CNN pada citra asli 77%, RGF 82%, ESRGAN 81%, dan RGF-ESRGAN 95%, dengan sensitivitas 95% dan spesifisitas 99% untuk gabungan.

Keterbatasan yang dapat diperiksa: tidak ada pembagian per pohon atau data uji terpisah yang dinyatakan, CNN tidak dirinci, dan PSNR serta SSIM dihitung terhadap citra asli sehingga tidak menunjukkan keunggulan pada tugas lain. Tidak ada deteksi tandan atau pencacahan. Penulis menyebut perlunya data lebih besar dan beragam serta integrasi dengan model klasifikasi.
