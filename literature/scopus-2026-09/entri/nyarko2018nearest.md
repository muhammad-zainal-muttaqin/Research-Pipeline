# A nearest neighbor approach for fruit recognition in RGB-D images based on detection of convex surfaces

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `nyarko2018nearest` |
| Judul asli | A nearest neighbor approach for fruit recognition in RGB-D images based on detection of convex surfaces |
| Penulis | Nyarko, Emmanuel Karlo; Vidovi\'c, Ivan; Rado\vcaj, Kristijan; Cupec, Robert |
| Tahun | 2018 |
| Venue | Expert Systems with Applications |
| Kode | C5 (Depth, 3D, dan non-RGB) |

## Tautan Akses
- PDF: [nyarko2018nearest.pdf](../pdf/nyarko2018nearest.pdf)
- DOI resmi: https://doi.org/10.1016/j.eswa.2018.07.048

## Gambaran Umum

Pemanenan buah otomatis merupakan masalah yang sulit dalam robotika. Agar robot pemanen dapat bekerja, sistem harus mampu mendeteksi buah di antara daun dan cabang pada kondisi tidak terkendali, ketika buah terhalang atau berada dalam bayangan. Kajian ini mengusulkan pendekatan baru untuk pengenalan buah pada citra *RGB-D*. Pendekatannya berbasis deteksi dan klasifikasi permukaan cembung. Penulis juga ingin mengetahui apakah satu sistem yang dilatih dengan berbagai jenis buah dapat dipakai untuk mengenali buah yang berbeda-beda tanpa pelatihan ulang untuk tiap jenis.

Data dikumpulkan dengan sensor *RGB-D* genggam PrimeSense Carmine 1.09 yang bekerja pada mode 100 mm. Citra direkam di kebun buah pada kondisi alami di luar ruangan, dengan resolusi 320 × 240 piksel. Setiap urutan citra memuat satu dari empat jenis buah, yaitu tomat, nectarine, pir, atau plum. Penulis hanya memilih citra yang tidak kabur akibat gerakan dan tidak berada dalam bayangan dalam. Setiap citra dibagi menjadi permukaan hampir cembung, lalu setiap segmen diberi label manual oleh evaluator manusia. Segmen buah diberi label *fruit*, sedangkan segmen daun dan cabang diberi label *other*. Data dibagi menjadi dataset referensi untuk pelatihan dan dataset uji untuk penilaian. Hanya sekitar 4,4% dari seluruh segmen konveks pada kedua dataset yang berlabel buah, sehingga data sangat tidak seimbang. Dataset ini juga dipublikasikan untuk pembanding metode pengenalan buah di masa depan.

Metode ini menyegmentasi citra menjadi permukaan cembung dan mengklasifikasikannya dengan *k-nearest neighbor*. Nilai k ditentukan dengan *10-fold cross validation* dan diperoleh k = 5. Penulis membandingkan descriptor *Convex Template Instance* (CTI) yang diusulkan dengan descriptor *SHOT*, dan masing-masing dalam varian dengan dan tanpa warna. Pada dataset uji, *SHOT* dan *SHOTColor* memiliki akurasi 98,5% hingga 99,6%, presisi 82,4% hingga 87,5%, recall 85,4% hingga 91,3%, dan F1 85,1% hingga 88,8%. Descriptor CTI memiliki akurasi 98,1% hingga 99,8%, presisi 82% hingga 92,4%, recall 78,1% hingga 92,6%, dan F1 80,1% hingga 91,5%. Penambahan informasi warna memperbaiki hasil CTI. Secara umum CTI sedikit lebih rendah dari SHOT, kecuali untuk tomat dan plum. Keunggulan utama CTI adalah kecepatan komputasinya. Pembuatan descriptor CTI jauh lebih cepat daripada SHOT, dan klasifikasinya juga lebih cepat karena komponen descriptor-nya lebih sedikit. Sistem yang dilatih dengan semua jenis buah sekaligus hanya sedikit lebih rendah daripada sistem yang dilatih per jenis buah.

Penulis menyatakan beberapa batasan. Pertama, hasil diperoleh dengan kondisi rekaman sore hari yang berawan. Pada tengah hari yang cerah, penulis memperkirakan hasilnya jauh lebih buruk. Kedua, presisi sensor menurun seiring jarak, sehingga segmentasi hanya memakai titik dalam jarak 0,6 m dari kamera. Ketiga, buah dan daun yang berdekatan kadang membentuk satu permukaan hampir cembung, sehingga satu segmen dapat mewakili beberapa objek. Keempat, warna beberapa jenis buah sulit dibedakan dari warna daun, dan bayangan daun atau buah lain dapat mengurangi saturasi warna buah yang berada lebih dalam di tajuk. Akibatnya, informasi warna tidak selalu membantu. Penulis juga mencatat bahwa metode ini diuji pada satu dataset dengan empat jenis buah, sehingga generalisasinya ke kondisi lain belum dibuktikan.
