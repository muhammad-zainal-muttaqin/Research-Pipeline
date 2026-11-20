# Neural network for identifying apple fruits on the crown of a tree

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `smirnov2021neural` |
| Judul asli | Neural network for identifying apple fruits on the crown of a tree |
| Penulis | Smirnov, Igor; Kutyrev, Alexey; Kiktev, Nikolay |
| Tahun | 2021 |
| Venue | E3s Web of Conferences |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | apple |

## Tautan Akses
- PDF: [smirnov2021neural.pdf](../pdf/smirnov2021neural.pdf)
- DOI resmi: https://doi.org/10.1051/e3sconf/202127001021

## Gambaran Umum

Menghitung jumlah buah pada tajuk pohon secara otomatis masih menjadi masalah yang belum terselesaikan dalam hortikultura. Penulis menilai perhitungan manual memakan waktu dan tenaga, sehingga efisiensi produksi kebun ikut terdampak. Metode yang hanya mengandalkan warna buah dinilai kurang memadai karena warna apel sangat beragam dan sensitivitas cahaya kamera berubah-ubah. Kondisi iklim dan pencahayaan di lapangan juga menyulitkan pengenalan tanaman yang serupa. Karena itu, penulis mengusulkan kompleks perangkat keras dan lunak (*PAC*) yang memakai sistem visi teknis dan jaringan saraf dalam untuk mengenali buah apel pada tajuk pohon, sekaligus menghitung jumlahnya.

Objek kajian adalah pohon apel varietas Northern Synap. Untuk data pelatihan, penulis memotret buah dengan beberapa kamera Nikon D3500 dan lensa Nikkor AF-P DX 18-55 mm pada jarak 0,2 m, 0,5 m, dan 1,0 m, dari sudut yang saling tumpang tindih. Jumlah foto lebih dari 3.000 citra. Kelas buah dibagi menjadi dua kelompok. Kelompok pertama adalah buah sehat, yaitu merah dan hijau. Kelompok kedua adalah buah berpenyakit atau cacat, yaitu busuk, bitter pitiness, hail, mekanis, kudis, sawfly, dan ngengat buah, sehingga totalnya dua kelas sehat dan tujuh kelas berpenyakit. Anotasi dibuat dengan perangkat terbuka VGG Image Annotator dan disimpan dalam berkas JSON, lalu dikonversi menjadi masker. Kumpulan data dibagi menjadi data latih dan data uji dengan pembagian merata per kelas. Untuk pengujian lapangan, kamera Basler ace 1920-155uc dengan antarmuka GigE dan sensor CMOS Sony IMX174 dipakai dengan resolusi hingga 1920 × 1200 piksel, atau 2,3 megapiksel. Intensitas cahaya diukur dengan luxmeter Radex Lupin.

Metode yang dipilih adalah arsitektur *Mask R-CNN* yang diimplementasikan dengan PyTorch. Pada tahap pertama, algoritma *YOLO* mendeteksi objek apel dalam bingkai. Pada tahap kedua, jaringan menentukan batas tepat setiap objek dan membuat masker piksel demi piksel. Sebuah objek dianggap termasuk kelas tertentu jika probabilitasnya lebih dari 0,9. Dalam pengujian lapangan, sistem diulang lima kali pada pohon yang sama dengan 150 buah, termasuk buah yang tidak tertutup sebagian. Rata-rata jumlah buah yang terhitung adalah 134 buah, dengan nilai minimum 131 dan maksimum 136. Akurasi estimasi jumlah buah terhadap hitungan manual minimal 89,3 persen. Kesalahan absolut persentase rata-rata adalah 11,9 persen. Penulis menyatakan bahwa jaringan konvolusional rekuren ini paling cocok untuk identifikasi buah apel, karena mampu mengenali kontur buah dengan akurasi tinggi pada kondisi iklim yang berubah.

Penulis mencatat beberapa batasan. Kesalahan penghitungan utama berasal dari segmentasi citra beresolusi rendah. Akibatnya, sebagian area buah hanya terdeteksi sebagian, atau latar belakang dan lingkungan keliru dikenali sebagai buah. Penulis menduga kesalahan ini dapat dikurangi dengan menaikkan resolusi kamera menjadi 3840 × 2160 piksel. Penulis juga menyebut bahwa kemampuan sistem beroperasi stabil di kebun industri, terlepas dari ukuran dan gangguan daun, serta mengukur warna dan ukuran buah, belum sepenuhnya diuji di teks ini. Pernyataan bahwa sistem akan mengidentifikasi penyakit dan cacat buah dengan probabilitas minimal 99 persen tercantum sebagai kemampuan yang diharapkan dari perluasan kumpulan data selama operasi. Pernyataan tersebut merupakan target penulis dan bukan hasil eksperimen yang dilaporkan dalam teks.
