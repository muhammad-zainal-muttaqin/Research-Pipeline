# Blueberry harvestability trait extraction from 2D images and 3D point clouds based on deep learning and photogrammetric reconstruction

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ni2020blueberry` |
| Judul asli | Blueberry harvestability trait extraction from 2D images and 3D point clouds based on deep learning and photogrammetric reconstruction |
| Penulis | Ni, Xueping; Li, Changying; Jiang, Huanyu |
| Tahun | 2020 |
| Venue | Asabe 2020 Annual International Meeting |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape, blueberry |

## Tautan Akses
- PDF: [ni2020blueberry.pdf](../pdf/ni2020blueberry.pdf)
- DOI resmi: https://doi.org/10.13031/aim.202001338

## Gambaran Umum

Blueberry tipe *southern highbush* dipanen bertahap karena kematangan buah berbeda, baik dalam satu tandan, antartandan, maupun antarcabang. Makalah ini menilai kematangan buah secara individu, lalu menghitung kepadatan tandan (*compactness*), jumlah buah, dan kematangan per tandan. Ketiga sifat itu dipakai untuk memperkirakan kemudahan panen (*harvestability*) dan hasil. Penulis menyebut metode berbasis spektrum hanya dapat dipakai di dalam ruangan dengan pencahayaan buatan. Tujuan studi adalah memisahkan buah individual dari citra 2D dan awan titik 3D (*point cloud*), lalu menghitung sifat panen dan hasil dari masing-masing data.

Data dikumpulkan di Alma, Georgia, Amerika Serikat, pada April 2019. Empat kultivar diteliti: Emerald, Farthing, Meadowlark, dan Star. Untuk melatih model, 669 citra 2D dianotasi dan dibagi menjadi 524 citra latih dan 145 citra validasi; 137 citra pertama dianotasi manual, dan model diuji pada 55 citra. Untuk ekstraksi sifat, ada 26 sampel per kultivar dengan lima sudut pandang per sampel, sehingga totalnya 520 citra. Untuk 3D, 10 tandan per kultivar disimpan dua hari di lemari pendingin, lalu tiga kamera digital (X-A10, Fujifilm) memotret tandan yang diputar motor langkah setiap 9 derajat. Setiap tandan menghasilkan 120 citra, yang direkonstruksi dengan Agisoft Metashape.

Metode 2D memakai Mask R-CNN dengan *backbone* resnet101 dan bobot awal COCO. Model dilatih 600 epoch dengan citra 1024 × 1024 piksel. Anotasi iteratif menghemat dua pertiga waktu anotasi: model awal menebak segmentasi citra berikutnya, lalu hasilnya dikoreksi manual. Untuk 3D, masker 2D dari 120 citra diproyeksikan ke awan titik. Dua masker dianggap buah yang sama jika tumpang tindih proyeksinya lebih dari 30%. Kematangan buah 3D ditentukan dari patch terbanyak: bila patch matang lebih banyak, buah dianggap matang. Volume buah diperkirakan dengan pencocokan bola (*sphere fitting*).

Hasil segmentasi 2D menunjukkan mAP 0,72 pada ambang IoU 0,5 (71,6% di abstrak) dan akurasi masker 90,4%. Pada IoU 0,95, mAP mendekati nol. Akurasi hitungan dari awan titik 3D di atas 97%, menurut abstrak. Pada hitungan 2D, RMSE 1,484 berarti hitungan kurang sekitar 1,5 buah per tandan. Rata-rata jumlah buah Emerald tertinggi, 13,812, dan Star terendah, 8,534. Meadowlark memiliki kematangan tertinggi, 0,651. Analisis varians (ANOVA) menunjukkan hasil kematangan yang konsisten antara 2D dan 3D. Menurut abstrak, hasil jumlah buah dan kepadatan tidak konsisten antara keduanya.

Penulis mencatat empat jenis kesalahan deteksi 2D: satu buah terbagi menjadi dua, buah tidak terdeteksi karena tertutup tangkai, daun, atau buah lain, dua buah yang berdekatan terdeteksi sebagai satu, dan deteksi parsial. Daun kadang terdeteksi sebagai buah mentah. Penulis menduga penyebabnya adalah banyak buah yang saling menutupi, sehingga hanya sebagian kecil buah terlihat; keterbatasan ini melekat pada citra 2D. Hitungan 2D kurang karena satu sudut pandang tidak melihat seluruh tandan. Rekonstruksi 3D memakan waktu beberapa jam per tandan. Menurut keterangan di halaman pertama, makalah ini adalah presentasi pertemuan ASABE dan tidak melalui tinjauan sejawat seperti jurnal.
