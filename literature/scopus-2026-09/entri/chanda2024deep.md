# Deep learning-based Mango Fruit Detection and Counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chanda2024deep` |
| Judul asli | Deep learning-based Mango Fruit Detection and Counting |
| Penulis | Chanda, Apisak; Voraseyanont, Parameth; Siricharoen, Punnarai |
| Tahun | 2024 |
| Venue | 2024 21st International Conference on Electrical Engineering Electronics Computer Telecommunications and Information Technology Ecti Con 2024 |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | mango |

## Tautan Akses
- PDF: [chanda2024deep.pdf](../pdf/chanda2024deep.pdf)
- DOI resmi: https://doi.org/10.1109/ecti-con60892.2024.10594843

## Gambaran Umum

Penelitian ini bertujuan mendeteksi dan menghitung buah mangga pada tajuk pohon dari citra RGB untuk mendukung estimasi hasil panen di Thailand. Penulis menyebut oklusi sebagian oleh daun dan buah yang saling tumpang tindih sebagai masalah utama. Mereka mengusulkan augmentasi *Random Erasing* untuk menangani oklusi.

Citra diambil di kebun mangga kultivar "Nam Dok Mai" di Provinsi Chainat dengan kamera digital dan telepon pintar, resolusi 4032 × 3021, sebanyak 308 citra. Buah berada pada tahap belum matang, sekitar 50 hari setelah berbunga. Anotasi berupa poligon. Pembagian 70:15:15 menghasilkan 40 citra validasi dengan 224 anotasi dan 47 citra uji dengan 260 anotasi. Teks juga menulis "221 images for testing with 1339 annotations", yang tampaknya merujuk citra latih. Pemberi label tidak disebut. Jumlah pohon tidak disebut.

Penulis membandingkan dua model segmentasi instans (deteksi disertai mask piksel): *Mask R-CNN* dan *Cascade R-CNN*. *Mask R-CNN* memperluas *Faster R-CNN* dengan cabang mask. *Cascade R-CNN* menambah beberapa kepala deteksi berurutan agar kotak lebih tepat. Keduanya memakai tulang punggung (*backbone*, penyaring fitur) ResNeXt-101 dengan *Feature Pyramid Network* (FPN, penggabung fitur berbagai skala), varian 32x4d dan 32x8d. *Random Erasing* menutup acak 3 sampai 10 kotak (rasio luas 0,1 sampai 0,5, nilai 128) pada citra latih. Ambang kepercayaan dipilih dari F1 tertinggi pada data validasi (0,5 untuk *Mask R-CNN*, 0,4 untuk *Cascade R-CNN*).

Pada 47 citra uji, *Mask R-CNN* dengan ResNeXt-101-32x8d-FPN dan *Random Erasing* memberi presisi 0,922, *recall* 0,786, skor F1 0,849, mAP@50 0,883, dan MAE hitungan 1,106 buah per citra. Tanpa *Random Erasing* (augmentasi dasar), *Mask R-CNN* mencapai mAP@50 0,870 dan MAE 1,170. *Cascade R-CNN* dengan *Random Erasing* mencapai skor F1 0,830, mAP@50 0,874, dan MAE 1,298. Backbone 32x8d lebih baik daripada 32x4d untuk *Mask R-CNN* (mAP@50 0,870 berbanding 0,818).

Keterbatasan yang dapat diperiksa: hitungan dinilai per citra, bukan per pohon, dan tidak dibandingkan dengan hasil panen. MAE dihitung antara hitungan manual dan prediksi positif benar (*true positive*), bukan semua prediksi. Selisih antarmodel kecil (misalnya 0,9% pada mAP@50) dan tanpa pengulangan atau uji signifikansi. Pembagian dilakukan pada tingkat citra, sehingga pemisahan per pohon tidak disebut. Kebun tunggal, satu kultivar, satu tahap buah. Setiap citra dihitung sendiri tanpa penggabungan pandang.
