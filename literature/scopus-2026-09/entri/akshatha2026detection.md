# From detection to identity preservation: A pipeline–scenario–protocol–readiness review of datasets for visual multi-person tracking and re-identification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `akshatha2026detection` |
| Judul asli | From detection to identity preservation: A pipeline–scenario–protocol–readiness review of datasets for visual multi-person tracking and re-identification |
| Penulis | Bilakeri, Shavantrevva; Manisha; Akshatha, K. R. |
| Tahun | 2026 |
| Venue | Visual Computer |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [akshatha2026detection.pdf](../pdf/akshatha2026detection.pdf)
- DOI resmi: https://doi.org/10.1007/s00371-026-04700-x

## Gambaran Umum

Kajian ini meninjau dataset publik untuk *multi-person tracking* (MPT), yaitu pelacakan banyak orang dalam video dengan menjaga identitas tiap orang dari waktu ke waktu. Menurut penulis, tinjauan sebelumnya lebih banyak merangkum algoritma atau skor benchmark dan kurang menjelaskan peran tiap dataset dalam pipeline *tracking-by-detection*. Kajian ini mengelompokkan dataset menurut perannya dalam pipeline, lalu menilai apa yang dapat dan tidak dapat diuji oleh tiap dataset.

Kajian ini memuat 37 dataset yang diperkenalkan atau dipakai antara Januari 2005 dan April 2026. Dataset dibagi menjadi tiga kelompok: 8 dataset pendukung deteksi, 9 dataset *re-identification* (Re-ID) atau *person search*, dan 20 benchmark pelacakan inti. Benchmark pelacakan mencakup skenario kamera tunggal, multi-kamera, kerumunan padat, berkendara, olahraga, jangka panjang, dan sintetis. Contohnya MOT17 untuk pejalan kaki umum, MOT20 untuk kerumunan padat, DanceTrack untuk asosiasi di bawah gerak nonlinear dan tampilan yang mirip, SportsMOT untuk olahraga, BDD100K untuk kamera bergerak, dan TAO untuk pelacakan jangka panjang dan dunia terbuka. Metadata dataset, string pencarian, tabel penyaringan, dan anotasi PSPR tersedia secara publik di GitHub dan Zenodo.

Metode utama kajian adalah kerangka *Pipeline–Scenario–Protocol–Readiness* (PSPR). Setiap dataset dinilai menurut peran dalam pipeline, kompleksitas skenario visual, protokol evaluasi, kesiapan untuk penerapan, dan batasan benchmark. Penulis menyatakan bahwa pilihan dataset membentuk apa yang dapat diukur oleh sistem pelacakan. Dataset deteksi terutama menguji lokalisasi, dataset Re-ID mendukung pemodelan identitas berbasis tampilan, dan benchmark pelacakan berbeda dalam menguji ambiguitas asosiasi, kepadatan kerumunan, gerak kamera, kemunculan ulang lintas kamera, dan pelestarian identitas jangka panjang. Kajian juga mencatat bahwa metrik MOTA, IDF1, HOTA, DetA, dan AssA dilaporkan secara berbeda antar dataset, sehingga skor antarbenchmark sulit dibandingkan langsung.

Menurut penulis, kinerja Re-ID pada benchmark retrieval tidak menjamin pelacakan yang kuat ketika deteksi berderau, objek tertutup, atau lintasan terfragmentasi. Keterbatasan yang disebut penulis mencakup kurangnya evaluasi identitas jangka panjang, protokol metrik yang terfragmentasi, cakupan kondisi merugikan yang kurang, anotasi multimodal yang terbatas, dan dukungan yang lemah untuk pelacakan terbuka dan siap diterapkan.
