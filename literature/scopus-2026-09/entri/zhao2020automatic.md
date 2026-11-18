# Automatic sweet pepper detection based on point cloud images using subtractive clustering

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhao2020automatic` |
| Judul asli | Automatic sweet pepper detection based on point cloud images using subtractive clustering |
| Penulis | Zhao, Xiaokang; Li, Hao; Zhu, Qibing; Huang, Min; Guo, Ya; Qin, Jianwei; 2. USDA/ARS Environmental Microbial; Food Safety Laboratory, Beltsville Agricultural Research Center, Bldg., 303, BARC-East, 10300 Baltimore Ave., MD 20705-2350, USA |
| Tahun | 2020 |
| Venue | International Journal of Agricultural and Biological Engineering |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | sweet pepper |

## Tautan Akses
- PDF: [zhao2020automatic.pdf](../pdf/zhao2020automatic.pdf)
- DOI resmi: https://doi.org/10.25165/j.ijabe.20201303.5460

## Gambaran Umum

Penelitian ini mengusulkan metode deteksi buah berbasis citra awan titik tiga dimensi untuk mengatasi oklusi oleh cabang, daun, dan buah lain. Penulis menyatakan identifikasi buah yang tepat dari citra kanopi menjadi dasar robot pemanen, sementara metode berbasis citra RGB konvensional sulit ketika warna buah mendekati latar dan bentuk buah tidak beraturan. Tujuan penelitian adalah mendeteksi dan menghitung buah paprika merah dalam adegan awan titik tanpa harus mengetahui jumlah buah lebih dahulu, serta membandingkan hasilnya dengan metode RANSAC.

Data memakai himpunan data terbuka sweet pepper yang direkam dengan kamera RGB-D Intel RealSense F200 yang dipasang pada lengan robot selama sepuluh hari di sistem pertanian terlindung. Awan titik padat dibangun dari banyak pandang dengan Kinect Fusion, lalu denoising dan penyaringan voxel grid dilakukan memakai PCL. Acuan hitung adalah penghitungan manual visual atas seluruh citra oleh pemeriksa manusia. Himpunan data terdiri atas lima pohon dengan total 86 buah, terdiri atas 51 buah dengan luas oklusi di bawah 50% dan 35 buah dengan oklusi di atas 50%. Artikel ini tidak menyatakan pembagian latih dan uji; seluruh awan titik dipakai untuk pengujian.

Metode terdiri atas tiga tahap. Segmentasi warna memakai selisih R-G, dengan titik dinyatakan sebagai buah jika Rs − Gs lebih besar daripada ambang δ; untuk paprika merah dengan latar hijau, δ ditetapkan antara 20 dan 50 karena nilai di atas 50 mulai menyaring titik buah normal. Penghapusan pencilan jarang menghitung jarak rata-rata setiap titik terhadap tetangganya, lalu membuang titik di luar rentang μ ± ασ dengan α = 0,6. Deteksi dan penghitungan memakai subtractive clustering: setiap titik diperlakukan sebagai kandidat pusat cluster dengan densitas fungsi Gaussian, radius lingkungan Ra = 0,02 m, radius pengurangan Rb = 1,5 Ra, dan jarak minimum antarpusat r = 0,04 m agar buah yang sama tidak terhitung dua kali. Iterasi berhenti ketika densitas kandidat tidak melebihi kelipatan Tmin dari densitas pusat sebelumnya.

Terhadap 86 buah, metode yang diusulkan menghasilkan TPR 90,69% (78 benar positif), FPR 6,97% (6 positif palsu), dan FNR 9,31% (8 salah negatif). RANSAC sebagai pembanding menghasilkan TPR 86,05% (74), FPR 3,49% (3), dan FNR 13,95% (12); penulis menyatakan FPR RANSAC lebih rendah karena metode itu menggabungkan dua buah berdekatan yang saling menutupi menjadi satu. Pada satu contoh adegan yang memuat 12 buah dengan delapan buah beroklusi lebih dari 50%, metode yang diusulkan mengenali 11 buah. Penulis menyatakan buah yang terlewat umumnya berada di tepi citra dengan hanya sebagian kecil permukaan tampak.

Keterbatasan yang dinyatakan penulis mencakup parameter radius yang tetap, sehingga buah berukuran besar dapat menghasilkan dua pusat cluster dan menaikkan FPR; penulis merencanakan penyesuaian parameter otomatis. Segmentasi warna membatasi metode pada buah merah dan dwiwarna, sehingga apel hijau memerlukan strategi Filtering lain, misalnya klasifikasi warna dengan pembelajaran mesin atau ciri spektral. Penulis juga menyatakan metode ini sulit untuk buah yang tumbuh berjambak seperti anggur, dan menyatakan positif palsu lebih mengganggu estimasi hasil daripada proses pemanenan.

