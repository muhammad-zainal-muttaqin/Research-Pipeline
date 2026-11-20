# Deep Learning Methods for Multi-Species Animal Re-identification and Tracking a Survey

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ravoor2020deep` |
| Judul asli | Deep Learning Methods for Multi-Species Animal Re-identification and Tracking a Survey |
| Penulis | Ravoor, Prashanth C.; Sudarshan, T.S.B. |
| Tahun | 2020 |
| Venue | Computer Science Review |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [ravoor2020deep.pdf](../pdf/ravoor2020deep.pdf)
- DOI resmi: https://doi.org/10.1016/j.cosrev.2020.100289

## Gambaran Umum

Survei ini membahas pemanfaatan teknik *re-identification* (re-ID) hewan untuk meningkatkan kinerja pelacakan hewan antarkamera. Latar belakangnya adalah konservasi satwa liar dan upaya mencegah konflik antara hewan dan manusia. Sistem pemantauan otomatis perlu mengenali kembali individu yang sama ketika ia berpindah dari satu kamera ke kamera lain. Penulis menyatakan bahwa identitas individu tidak perlu diingat dalam jangka panjang, tetapi harus dipertahankan selama hewan masih berada dalam jangkauan sistem, yang bisa berlangsung beberapa menit hingga beberapa jam. Masalah utama yang diangkat adalah bagaimana membedakan individu dari spesies yang sama secara andal dan secara *real time* atau mendekati *real time*.

Survei ini tidak menggunakan data baru. Cakupannya adalah studi-studi *re-identification* hewan dan beberapa metode pelacakan objek serta *re-identification* manusia yang berkinerja baik. Studi hewan tunggal yang ditinjau mencakup paus minke dengan 76 individu dan 1.320 citra, lumba-lumba dengan sekitar 4.750 citra dari sekitar 185 individu, sapi dengan sekitar 13.600 citra dari 60 individu, serta panda merah dengan 2.877 citra dari 51 individu. Studi lain memakai wajah simpanse, gorila, dan gajah, serta harimau Amur dari tantangan ATRW. Survei juga meninjau studi multi-spesies dan *re-identification* manusia. Teks tidak merinci pembagian data latih, validasi, dan uji untuk setiap studi di luar angka yang disebutkan di atas.

Metode yang ditinjau antara lain jaringan konvolusi seperti FCN-8 berbasis VGG-16, ResNet50 dengan fungsi kerugian *triplet loss*, CNN tiga lapis khusus, dan VGG-16 untuk ekstraksi fitur wajah panda. Penulis membandingkan pendekatan klasifikasi *softmax* dengan pendekatan yang membandingkan fitur memakai kemiripan kosinus. Hasil kuantitatif yang dilaporkan adalah akurasi uji 93,5% pada paus minke (Konovalov et al.), akurasi top-1 90,6% pada lumba-lumba (Bouma et al.), akurasi *closed-set* top-1 96,3% pada sapi (Phyo et al.), dan akurasi top-1 *closed-set* 93,3% pada panda merah (He et al.). Akurasi validasi pada studi paus minke tercatat 92,3%. Untuk studi lumba-lumba, akurasi *open-set* dipertimbangkan tetapi tidak dilaporkan secara eksplisit. Dua studi lain tidak melaporkan akurasi *open-set*. Penulis juga mencatat bahwa metode yang dibahas memungkinkan pengenalan individu baru melalui pengelompokan fitur, sehingga *open-set* lebih mudah diterapkan.

Penulis menyatakan beberapa batasan. Pertama, klasifikasi *softmax* menyulitkan implementasi pada skenario *open-set*. Kedua, pendekatan berbasis bagian tubuh bergantung pada detektor objek yang melokalisasi bagian tertentu, seperti sirip, sehingga detektor harus diganti jika metode diterapkan pada spesies lain. Ketiga, sebagian besar studi yang ditinjau belum melaporkan akurasi *open-set* secara jelas. Penulis juga menyebut tantangan pada tahap lain dalam pipeline pelacakan, termasuk asosiasi identitas dan kecepatan inferensi, dan mengusulkan sejumlah solusi untuk masing-masing tahap. Kesimpulan penulis menyatakan bahwa survei ini diharapkan menjadi dasar bagi penelitian selanjutnya di bidang pelacakan hewan.
