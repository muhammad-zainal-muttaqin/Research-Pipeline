# Geometry-Driven Triangulation and Differentiable Semantic Gaussian Refinement for 3D Grape Bunch Model Reconstruction in the Field

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `woo2026geometry` |
| Judul asli | Geometry-Driven Triangulation and Differentiable Semantic Gaussian Refinement for 3D Grape Bunch Model Reconstruction in the Field |
| Penulis | Woo, Yan San; Yok-In, Kabin; Buayai, Prawit; Nishizaki, Hiromitsu; Kamarudin, Latifah Munirah; Mao, Xiaoyang |
| Tahun | 2026 |
| Venue | Icict 2026 Proceedings of 2026 the 9th International Conference on Information and Computer Technologies |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | grape |

## Tautan Akses
- PDF: [woo2026geometry.pdf](../pdf/woo2026geometry.pdf)
- DOI resmi: https://doi.org/10.1145/3803291.3803356

## Gambaran Umum

Penelitian ini mengatasi kebutuhan memperkirakan jumlah dan susunan buah anggur meja di bawah oklusi parah untuk penipisan buah (*berry thinning*). Penulis menilai bahwa alur rekonstruksi 3D dan *neural rendering* yang ada menghasilkan geometri rapat atau sintesis pandangan baru, tetapi jarang menghasilkan model ringkas bertingkat instans untuk tandan yang rapat. Tujuan penelitian adalah merekonstruksi model 3D semantik per buah dari rekaman video genggam di kebun nyata, dengan representasi yang dapat dihitung dan ditafsirkan.

Tanaman yang dipakai adalah anggur meja di kebun nyata. Data berupa 30 sekuens tandan yang direkam dengan ponsel genggam sambil mengelilingi tandan untuk membentuk cincin pandangan, pada resolusi 1080 × 1920; seluruh frame diproses pada resolusi asli. Detektor dan segmentor buah dari kajian [4] menghasilkan mask dan kotak per buah. Landasan kebenaran berupa awan titik berlabel dengan nomor buah per titik, yang diubah menjadi elipsoid Gaussian melalui PCA dengan faktor penskalaan global γ = 1,45. Penulis tidak menyebut split latih/uji karena tiap tandan direkonstruksi terpisah melalui optimasi. Tahap 3 dijalankan dengan PyTorch pada satu GPU NVIDIA RTX 4080 SUPER 16 GB memakai SGD, laju belajar 10⁻³ untuk parameter buah dan 10⁻⁵ untuk parameter kamera saat pemanasan.

Mekanisme rekonstruksi terdiri atas tiga tahap. Tahap 1 mengekstrak atribut 2D per pandangan (pusat, jari-jari lingkaran atau sumbu elips, mask, kotak, dan label keterlihatan) serta pose kamera awal memakai SfM ringan COLMAP dengan model kamera OPENCV tunggal dan penyesuaian bundle global dinonaktifkan. Tahap 2 membangun lintasan lintas pandangan tanpa deskriptor tampilan, hanya memakai empat petunjuk geometri: pembatasan tetangga berdasarkan azimut (selisih indeks paling banyak 4), gerbang epipolar (ambang 3 piksel), konsistensi sudut (selisih azimut di bawah 25°), dan konsistensi skala jari-jari. Penugasan Hungarian per pasangan pandangan dan union–find menghasilkan lintasan; lintasan yang tampak di kurang dari tiga pandangan dibuang. Triangulasi DLT diverifikasi dengan sudut baseline minimum 1,5°, galat reproyeksi median 3 piksel, dan kedalaman positif, lalu duplikat digabung dengan penghambatan nonmaksimum 3D berjari-jari 8–10 mm. Tahap 3 menyempurnakan elipsoid Gaussian melalui render diferensial berpenyangga kedalaman dengan rugi gabungan untuk pusat, jari-jari, mask (Dice dan *focal BCE*), serta kotak (IoU), dengan penugasan Hungarian antara hasil render dan deteksi 2D. Penjadwalan tiga fase terdiri atas pemanasan pose sampai laju pencocokan mencapai 0,40, pembaruan topologi konservatif berupa penambahan buah setelah tiga epoch tak tercocok dan penghapusan buah yang terus tak tercocok, serta penyempurnaan skala; orientasi quaternion dibekukan selama optimasi.

Hasil utama diukur pada 30 tandan dengan tiga metrik: galat absolut rata-rata jumlah buah, presisi/recall/F1 pada ambang OBB-IoU τ = 0,10; 0,25; dan 0,45, serta waktu Tahap 3. Galat jumlah buah keseluruhan turun dari 3,7 pada inisialisasi Tahap 2 menjadi 3,1 (10 pandangan), 3,2 (20 pandangan), dan 2,5 (30 pandangan); pada tandan padat dengan sedikitnya 60 buah, galat turun dari 10,5 menjadi 8,0; 8,2; dan 4,8. Nilai F1 OBB-IoU naik dari 35,6 menjadi 78,7; 87,8; dan 88,5 pada τ = 0,10, serta dari 10,3 menjadi 64,5; 74,1; dan 74,9 pada τ = 0,25. Waktu Tahap 3 rata-rata 1,8; 3,8; dan 5,1 menit per tandan untuk 10; 20; dan 30 pandangan, tidak termasuk biaya Tahap 1 dan 2 yang sama untuk semua pengaturan.

Batasan yang dinyatakan penulis tidak dikumpulkan dalam bagian tersendiri. Orientasi buah dibekukan untuk menghindari degenerasi antara pose, skala, dan orientasi di bawah pengawasan 2D. Kinerja pada τ = 0,45 tetap rendah karena oklusi dan derau pada landasan kebenaran elipsoid. Lintasan yang teramati kurang dari tiga pandangan dibuang, pose kamera SfM diperlakukan sebagai inisialisasi perkiraan, dan penyesuaian bundle global dinonaktifkan. Waktu pemrosesan tidak mencakup Tahap 1 dan 2, sehingga angka 1,8–5,1 menit hanya mengukur penyempurnaan dari model awal. Penulis juga tidak menyebut uji lintas kebun, kultivar, atau sistem kamera lain.

