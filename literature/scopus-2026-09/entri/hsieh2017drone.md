# Drone-Based Object Counting by Spatially Regularized Regional Proposal Network

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hsieh2017drone` |
| Judul asli | Drone-Based Object Counting by Spatially Regularized Regional Proposal Network |
| Penulis | Hsieh, Meng-Ru; Lin, Yen-Liang; Hsu, Winston H. |
| Tahun | 2017 |
| Venue | Proceedings of the IEEE International Conference on Computer Vision |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [hsieh2017drone.pdf](../pdf/hsieh2017drone.pdf)
- DOI resmi: https://doi.org/10.1109/iccv.2017.446

## Gambaran Umum

Penelitian ini mengatasi penghitungan objek pada video yang direkam drone, dengan mobil sebagai objek contoh. Penulis menyatakan metode penghitungan yang ada umumnya bersifat regresi dan tidak dapat menentukan lokasi objek secara tepat, sehingga menghambat analisis lanjutan seperti pemahaman tingkat tinggi dan klasifikasi halus. Selain itu, penelitian sebelumnya mengasumsikan kamera tetap dan lokasi objek sudah diketahui, sehingga tidak langsung dapat dipakai pada video drone yang dinamis. Tujuannya adalah menghitung sekaligus melokalisasi objek memakai informasi tata letak antarobjek, karena mobil umumnya diparkir berjajar dan objek lain juga membentuk pola tertentu.

Data yang dipakai berupa kumpulan data CARPK yang dibuat penulis, berisi 89.777 mobil dari empat tempat parkir dengan citra drone beresolusi tinggi dan anotasi kotak pembatas (bounding box) per mobil. Penulis juga melengkapi anotasi sub-kumpulan PUCPR dari PKLot menjadi PUCPR+ yang memuat hampir 17.000 mobil; sebelumnya PUCPR hanya menganotasi sebagian tempat parkir dan hanya mendukung tugas klasifikasi, bukan penghitungan. Kumpulan data pembanding memiliki jumlah mobil lebih sedikit atau resolusi lebih rendah, yaitu OIRDS (180), VEDAI (2.950), dan COWC (32.716 dengan hanya 24–48 piksel per mobil). Seluruh model dibangun di atas VGG-16 dengan bobot terlatih ImageNet 2012, diimplementasikan dengan Caffe, dan disetel ulang pada CARPK atau PUCPR+; pelatihan bersama memakan waktu sekitar satu hari pada satu GPU NVIDIA Tesla K80.

Mekanisme intinya adalah Layout Proposal Network (LPN), yaitu jaringan konvolusional penuh yang menerima citra berukuran sembarang dan menghasilkan usulan region (region proposal) yang tidak bergantung pada kelas objek. Strukturnya mengikuti Region Proposal Network, dengan jendela 3×3 pada peta fitur konvolusional dan dua lapisan konvolusional 1×1 saudara untuk lokalisasi serta klasifikasi latar depan/latar belakang. Perbedaan utamanya ada pada loss yang memberi bobot spasial pada usulan latar depan: bobot dihitung dari kernel Gaussian dua dimensi pada posisi pusat kotak prediksi, yang menjumlahkan kontribusi pusat kotak kebenaran di sekitarnya dalam jendela spasial S = 255 dengan empat arah rotasi dan amplitudo α = 1. Dengan demikian, posisi yang dikelilingi lebih banyak objek sejenis memperoleh skor keyakinan lebih tinggi. Penulis memakai fitur conv4-3 dan ukuran kotak default yang lebih kecil (16×16, 40×40, 100×100) agar objek kecil terdeteksi, serta menetapkan γ = λ = 1. Pembobotan ini dapat disisipkan ke sistem detektor lain dan mengurangi jumlah usulan pada inference, yang penting karena baterai drone hanya memberi waktu terbang sekitar 20 menit.

Hasil diukur dengan Average Recall (AR), yaitu rata-rata recall untuk ambang IoU dari 0,5 sampai 1, serta metrik MAE dan RMSE yang didefinisikan sebagai rata-rata selisih absolut dan akar rata-rata selisih kuadrat antara jumlah sebenarnya dan jumlah prediksi. Pada PUCPR+, LPN mencapai AR 62,5 persen untuk 1.000 usulan, naik dari 59,9 persen pada RPN yang sudah disesuaikan; untuk 300 usulan, AR naik dari 43,2 persen menjadi 49,3 persen, dan untuk 500 usulan dari 53,4 persen menjadi 57,9 persen. Penulis melaporkan pula peningkatan relatif 16,30 persen pada kasus padat berbanding 8,27 persen pada kasus kurang padat. Untuk penghitungan dengan 400 usulan pada PUCPR+, model penulis memperoleh MAE 22,76 dan RMSE 34,46, sedangkan One-Look Regression memperoleh 21,88 dan 36,73 serta Faster R-CNN tersetel ulang dengan kotak kecil 39,88 dan 47,67. Pada CARPK dengan 200 usulan, model penulis memperoleh MAE 23,80 dan RMSE 36,79, mengungguli One-Look Regression (59,46 dan 66,84) dan Faster R-CNN tersetel ulang dengan kotak kecil (24,32 dan 37,62). Dengan 1.000 usulan, angkanya menjadi 8,04 dan 12,06 pada PUCPR+ serta 13,72 dan 21,77 pada CARPK.

Batasan yang dinyatakan penulis mencakup ketergantungan metode pada pola tata letak objek yang berulang, karena usulan dibobot dari kemiripan posisi tetangga. Penulis juga mencatat bahwa YOLO dan Faster R-CNN yang dilatih pada PASCAL VOC dan MS COCO memberi hasil lebih buruk karena perbedaan sudut pandang, sehingga penyesuaian pada kumpulan data target diperlukan. Penelitian lanjutan yang diusulkan mencakup penggunaan informasi global seperti konteks, adegan jalan, dan objek lain untuk membedakan objek menyerupai mobil dari mobil sungguhan. Penulis tidak menyatakan batasan lain secara eksplisit.
