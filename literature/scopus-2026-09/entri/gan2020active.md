# Active thermal imaging for immature citrus fruit detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gan2020active` |
| Judul asli | Active thermal imaging for immature citrus fruit detection |
| Penulis | Gan, Hao; Lee, Won S.; Alchanatis, Victor; Abd-Elrahman, A. |
| Tahun | 2020 |
| Venue | Biosystems Engineering |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [gan2020active.pdf](../pdf/gan2020active.pdf)
- DOI resmi: https://doi.org/10.1016/j.biosystemseng.2020.08.015

## Gambaran Umum

Makalah ini meneliti deteksi buah jeruk muda (*immature citrus fruit*) memakai kamera termal aktif. Berbeda dengan kebanyakan studi penghitungan buah yang memakai citra RGB, penulis memasang kamera termal FLIR pada platform kereta golf yang bergerak di sela baris pohon, lalu menyemprotkan air ke tajuk sebelum pengambilan gambar. Semprotan itu membuat suhu permukaan daun turun, sehingga buah yang suhunya tetap tinggi dapat dibedakan dari daun. Studi ini melaporkan rerata *average precision* (AP, ukuran ketepatan deteksi yang merangkum presisi dan recall) sebesar 87,2% untuk Faster R-CNN dan 85,5% untuk SSD pada citra uji, serta akurasi penghitungan 96% ketika Faster R-CNN dipasangkan dengan pelacakan video.

Latar belakangnya adalah keterbatasan citra warna pada buah hijau yang tertutup daun. Buah muda jeruk memiliki warna yang mirip dengan daun, sehingga pendekatan RGB saja sering gagal memisahkan keduanya di bawah tajuk yang rapat. Penulis memilih pencitraan termal karena selisih suhu antara buah dan daun dapat diukur tanpa bergantung pada warna. Video direkam dengan kecepatan 25 FPS dari 20 baris pohon. Sebanyak 289 citra diberi label dan dibagi dengan rasio 4:1 untuk pelatihan dan pengujian. Pelatihan model membutuhkan sekitar 50 jam. Detektor yang dibandingkan adalah Faster R-CNN dengan backbone VGG16 dan SSD, keduanya diimplementasikan di Caffe.

Untuk penghitungan, sistem memakai pelacakan optik aliran Lucas-Kanade agar objek yang sama di beberapa bingkai tidak dihitung dua kali. Algoritma penghitungan mengaitkan hasil deteksi antarbingkai menurut posisi dan gerakan objek. Pada pengujian video, Faster R-CNN menghasilkan 899 dan 1.180 deteksi pada dua video uji, sedangkan SSD menghasilkan 775 dan 1.449. Pada tabel penghitungan pohon 1 sampai 25, jumlah hitung manual 747 buah dibandingkan dengan 719 buah dari algoritma, yang setara dengan akurasi 96%. Angka video dan angka pohon berasal dari rangkaian uji yang berbeda, sehingga keduanya tidak dibandingkan langsung.

Penulis juga menguji pengaruh kondisi lingkungan terhadap selisih suhu (Tmax, selisih suhu maksimum antara buah dan daun) dengan regresi linear berganda memakai IBM SPSS. Peubah bebasnya adalah ln(Wunit), kelembapan relatif (RH), dan suhu ambien. Hasilnya menunjukkan Tmax berkorelasi negatif dengan RH dan positif dengan suhu ambien. Uji hipotesis dilakukan pada 86 video. Keterbatasan yang diakui penulis adalah sifat studi yang masih tahap awal. Di wilayah lembap, perubahan kelembapan yang mendadak dapat menimbulkan risiko penyakit pada tanaman akibat penyemprotan air, sehingga penilaian risiko diperlukan sebelum sistem dipakai secara komersial.
