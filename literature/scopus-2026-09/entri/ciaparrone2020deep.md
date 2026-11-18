# Deep learning in video multi-object tracking: A survey

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ciaparrone2020deep` |
| Judul asli | Deep learning in video multi-object tracking: A survey |
| Penulis | Ciaparrone, Gioele; Luque S\'anchez, Francisco; Tabik, Siham; Troiano, Luigi; Tagliaferri, Roberto; Herrera, Francisco |
| Tahun | 2020 |
| Venue | Neurocomputing |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [ciaparrone2020deep.pdf](../pdf/ciaparrone2020deep.pdf)
- DOI resmi: https://doi.org/10.1016/j.neucom.2019.11.023

## Gambaran Umum

Kajian ini adalah tinjauan pustaka tentang penggunaan pembelajaran mendalam untuk pelacakan banyak objek (*multiple object tracking*, MOT) pada video satu kamera. Berbeda dengan deteksi objek yang hanya menghasilkan kotak, MOT juga memberikan identitas pada setiap kotak agar objek sejenis dapat dibedakan. Penulis menyatakan kesulitan utama berasal dari oklusi, interaksi antarobjek, dan penampilan yang mirip, sehingga penerapan langsung model pelacakan objek tunggal menghasilkan pergeseran target dan banyak kesalahan identitas. Tinjauan ini memetakan cara kerja model deep learning pada empat tahap umum algoritma MOT, yaitu deteksi, ekstraksi fitur atau prediksi gerak, penghitungan afinitas, dan asosiasi.

Kajian ini bukan tentang tanaman; ia termasuk metode dari luar pertanian yang dapat ditransfer ke asosiasi lintas pandang. Ruang lingkupnya dibatasi pada data 2D dari video satu kamera, bukan data 3D atau banyak kamera. Dataset yang diulas mencakup MOT15 (22 video, 11.283 frame, 1.221 identitas, 101.345 kotak), MOT16 dan MOT17 (14 video, 11.235 frame, 1.342 identitas, 292.733 kotak), tantangan CVPR 2019 dengan kepadatan sangat tinggi (8 video, 13.410 frame, 6.869 lintasan, 2.259.143 kotak, hingga 245 pejalan kaki per frame), serta KITTI untuk pejalan kaki dan kendaraan. Metrik yang dijelaskan mencakup MOTA, MOTP, MT, ML, ID switches, dan IDF1; MOTA dihitung sebagai 1 − (FN + FP + IDSW)/GT, sedangkan pencocokan kotak memakai ambang IoU 0,5. IDF1 dihitung dari IDP dan IDR yang berasal dari IDTP, IDFP, dan IDFN pada pencocokan bipartit global.

Mekanisme yang dirangkum mencakup pemakaian CNN pada keempat tahap tersebut. Pada tahap deteksi, mayoritas kerja memakai Faster R-CNN dan variannya, SSD, atau YOLO, baik sebagai deteksi kustom maupun deteksi publik yang disediakan benchmark. Pada tahap fitur, CNN dipakai sebagai ekstraktor penampilan, sering kali dilatih sebagai jaringan siam dengan rugi kontrastif atau *triplet loss* agar fitur antarobjek berbeda dapat dibedakan. DeepSORT menambahkan vektor 128 fitur dari CNN residual dan jarak kosinus ke skor afinitas SORT. Tahap afinitas memanfaatkan kemiripan penampilan, gerak dari Kalman Filter, dan informasi posisi, sedangkan asosiasi memakai algoritma Hungaria, pemrograman linear, *greedy*, atau pemodelan graf. Penulis juga mencatat penggunaan autoencoder, LSTM, dan pembelajaran penguatan dalam sistem yang lebih kompleks.

Angka hasil yang dikutip tinjauan berasal dari publikasi yang dirangkum, bukan percobaan baru penulis. SORT melaporkan kenaikan MOTA absolut 18,9% pada MOT15 ketika deteksi ACF diganti dengan Faster R-CNN. Yu dkk. memperbaiki MOTA lebih dari 30% secara absolut pada MOT16 memakai Faster R-CNN termodifikasi dengan *skip pooling* dan fitur multiregion. Kim dkk. menambahkan 4.096 fitur visual dari CNN yang direduksi menjadi 256 dengan PCA dan menaikkan MOTA lebih dari tiga poin pada MOT15. Penulis menyimpulkan bahwa deteksi yang lebih akurat mengurangi kebutuhan akan algoritma pelacakan kompleks karena MOTA sangat dipengaruhi jumlah positif dan negatif palsu. Semua angka tersebut bersumber dari ringkasan naskah dan mengacu pada metrik MOTA sebagaimana didefinisikan pada bagian metrik tinjauan.

Batasan yang dinyatakan penulis mencakup fokus pada video satu kamera dan data 2D saja, sehingga tidak mencakup pelacakan 3D maupun multicamera. Metode daring hanya memakai informasi masa kini dan masa lalu sehingga umumnya lebih rendah mutunya daripada metode batch yang memakai informasi masa depan, dan sebagian besar tetap terlalu lambat untuk lingkungan waktu nyata. Penulis juga menilai metrik FPS sulit dibandingkan karena sebagian metode memasukkan tahap deteksi dan sebagian tidak, selain ketergantungan pada perangkat keras. Kategorisasi empat tahap tidak dianggap kaku karena satu model sering dipakai untuk beberapa tujuan. Selain itu, pendekatan deep learning pertama pada MOT yang memakai autoencoder diuji pada dataset yang tidak umum sehingga hasilnya sulit dibandingkan dengan metode lain, dan tinjauan ini tidak menyajikan pelatihan model baru melainkan mengumpulkan dan membandingkan hasil yang sudah dipublikasikan.

