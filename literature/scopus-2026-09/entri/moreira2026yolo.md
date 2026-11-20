# A YOLO-based approach to grape berry detection and counting with ampelographic feature analysis for grapevine yield estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `moreira2026yolo` |
| Judul asli | A YOLO-based approach to grape berry detection and counting with ampelographic feature analysis for grapevine yield estimation |
| Penulis | Moreira, Germano; dos Santos, Filipe Neves; Cunha, M\'ario |
| Tahun | 2026 |
| Venue | Information Processing in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [moreira2026yolo.pdf](../pdf/moreira2026yolo.pdf)
- DOI resmi: https://doi.org/10.1016/j.inpa.2026.03.002

## Gambaran Umum

Kajian ini membandingkan empat varian detektor objek YOLO (v8n, v9t, v10n, dan v11n) untuk mendeteksi dan menghitung buah anggur yang terlihat pada satu citra. Tujuannya adalah memperkirakan hasil panen dari foto tunggal kebun anggur, dengan ampelografi (ciri varietas, fenologi, bentuk dan kepadatan tandan) sebagai konteks budidaya.

Penghitungan dilakukan per citra. Setiap citra menghasilkan jumlah buah terlihat, dan jumlah itu kemudian dihubungkan dengan total buah per tandan. Kajian tidak membahas bagaimana buah yang sama dihitung hanya sekali ketika muncul di beberapa foto dari sudut berbeda.

Estimasi hasil anggur masih bergantung pada pengamatan manual di lapangan. Kajian ini mengusulkan penghitungan otomatis dari citra, sehingga pekerjaan yang sebelumnya memakan waktu dapat dipercepat. Karena buah pada tandan sering tertutup daun dan buah lain, jumlah yang terlihat berbeda dari jumlah sebenarnya. Kajian ini mengukur seberapa besar selisih itu.

Detektor objek mencari kotak pembatas (*bounding box*) di sekitar setiap buah yang terlihat. Jumlah kotak pada satu citra dianggap sebagai jumlah buah terlihat. Dengan hubungan statistik antara jumlah terlihat dan total per tandan, jumlah terlihat dikonversi menjadi estimasi total.

Empat varian YOLO dilatih pada kumpulan citra anggur yang sama dan dievaluasi dengan protokol yang sama. Setiap varian menghasilkan kotak deteksi dengan skor kepercayaan. Ambang skor dipilih untuk setiap model, yaitu 0,503 untuk v8n, 0,455 untuk v9t, 0,405 untuk v10n, dan 0,504 untuk v11n.

Kinerja diukur dengan *precision* (proporsi deteksi yang benar), *recall* (proporsi buah yang berhasil ditemukan), F1-score (rata-rata harmonik keduanya), dan G-mAP (rata-rata presisi rata-rata pada kelompok kelas). Kecepatan inferensi semua varian di bawah 5 ms per citra.

Pada tabel hasil, YOLOv11n memberi nilai tertinggi: precision 0,988, recall 0,923, F1 0,954, dan G-mAP 0,962. YOLOv8n memiliki precision 0,974 dan recall 0,905 (F1 0,938, G-mAP 0,950). YOLOv9t memiliki precision 0,965 dan recall 0,920 (F1 0,942, G-mAP 0,958). YOLOv10n memiliki precision 0,959 dan recall 0,919 (F1 0,939, G-mAP 0,955). Selisih antarvarian kecil, sekitar satu hingga dua poin persentase pada F1.

Untuk estimasi jumlah, kajian melaporkan YOLOv10n dengan MAPE 4,764, MSE 12,203, dan RMSE 3,493. Hubungan antara buah terlihat per citra dan total buah per tandan mencapai R² 0,860. Kajian juga mencatat bahwa buah yang terlihat sekitar 50% dari total.

Dari sisi rekayasa, pendekatan ini ringan karena inferensi di bawah 5 ms per citra. Perbandingan empat varian dilakukan dengan protokol yang sama, sehingga selisihnya dapat dibaca langsung.

Secara konseptual, penghitungan per citra tidak mengatasi buah ganda. Jika satu tandan terlihat dari dua sudut, kedua citra menghasilkan hitungan terpisah.
