# Enhancing tomato fruit detection and counting through ai-enabled agricultural innovations

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `usha2023enhancing` |
| Judul asli | Enhancing tomato fruit detection and counting through ai-enabled agricultural innovations |
| Penulis | Usha, S Gandhimathi Alias |
| Tahun | 2023 |
| Venue | Machine Learning and Deep Learning for Smart Agriculture and Applications |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [usha2023enhancing.pdf](../pdf/usha2023enhancing.pdf)
- DOI resmi: https://doi.org/10.4018/978-1-6684-9975-7.ch005

## Gambaran Umum

Bab ini membahas cara meningkatkan deteksi dan pencacahan buah tomat di lapangan dengan kecerdasan buatan. Penulis menilai pencacahan manual padat karya, memakan waktu, dan mudah menghasilkan kesalahan karena dipengaruhi penilaian manusia yang subjektif. Pengamatan visual juga sering gagal menangkap seluruh buah, terutama bila buah tertutup atau tersebar di antara dedaunan yang rimbun, sehingga estimasi hasil panen menjadi kurang akurat. Tomat dipilih karena merupakan sayuran komersial penting di India, dengan peran ekonomi dan ketahanan pangan yang besar.

Bab ini membahas akuisisi dan anotasi data secara umum. Data yang baik perlu mencakup variasi varietas, tahap pertumbuhan, kondisi cahaya, dan orientasi buah. Anotasi kebenaran dasar (*ground truth*) dibuat oleh anotator ahli dalam bentuk *bounding box* atau masker segmentasi tingkat instans. Citra tomat yang dipakai dalam eksperimen ditampilkan pada Gambar 2. Bab ini juga menyebut sumber dataset publik yang dikelola lembaga penelitian dan universitas. Penulis menyinggung tantangan konsistensi anotasi serta perlunya kolaborasi lintas wilayah untuk memperluas keragaman data.

Metode yang diusulkan adalah Mask R-CNN, perluasan dari Faster R-CNN, yang menghasilkan *bounding box* dan masker piksel untuk setiap buah. Jumlah buah dihitung dari banyaknya wilayah masker yang terpisah. Evaluasi memakai presisi, recall, dan F1-score. Hasil eksperimen ditampilkan sebagai kurva konvergensi berbagai fungsi kerugian (*loss*) selama beberapa epoch pada Gambar 3. Penulis menyatakan bahwa Mask R-CNN menghasilkan jauh lebih sedikit false positive dan false negative dibandingkan segmentasi tradisional berbasis fitur buatan tangan, serta memiliki presisi dan recall yang lebih tinggi. Sebagai pembanding, penulis mengutip rata-rata presisi 0,82 dari Zhou dkk. (2017), dan presisi 0,88 serta recall 0,8 dari Yamamoto dkk. (2014). Penulis menyatakan bahwa akurasi dan recall Mask R-CNN pada data mereka lebih tinggi daripada angka-angka tersebut. Teks tidak mencantumkan nilai presisi dan recall tunggal untuk sistem penulis.

Penulis menegaskan bahwa pemilihan teknik pencacahan harus disesuaikan dengan kebutuhan dan kendala aplikasi. Efisiensi komputasi, akurasi, dan kemampuan pemrosesan waktu nyata menentukan kelayakan suatu metode untuk skenario tertentu. Bab ini juga menyatakan bahwa otomatisasi dapat menghemat waktu dan tenaga dibandingkan penghitungan manual, terutama untuk estimasi hasil panen dan pemantauan kebun. Kesimpulan penulis bersifat umum. Inovasi berbasis kecerdasan buatan dinilai meningkatkan produktivitas, menekan biaya tenaga kerja dan kehilangan panen, serta mendukung praktik pertanian berkelanjutan.
