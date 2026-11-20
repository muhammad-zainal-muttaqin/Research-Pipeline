# OAFBC-Net: A Lightweight RGB-Depth Fusion Network for Occlusion-Aware Apple Detection in Complex Orchard Canopies

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `gao2026oafbc` |
| Judul asli | OAFBC-Net: A Lightweight RGB-Depth Fusion Network for Occlusion-Aware Apple Detection in Complex Orchard Canopies |
| Penulis | Gao, Long; Wang, Pengfei; Liu, Lixing; Liu, Hongjie; Li, Jianping; Yang, Xin |
| Tahun | 2026 |
| Venue | Agronomy |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | apple |

## Tautan Akses
- PDF: [gao2026oafbc.pdf](../pdf/gao2026oafbc.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy16141318

## Gambaran Umum

Penelitian ini mengatasi deteksi apel yang teroklusi di kanopi kebun, tempat penglihatan RGB saja sensitif terhadap oklusi daun, tumpang tindih buah, dan pencahayaan yang tidak stabil. Alih-alih hanya menemukan buah, penulis memodelkan tiga tingkat oklusi yang berorientasi pada pemanenan: tidak teroklusi (NO), teroklusi lunak (SO), dan teroklusi keras (HO). Pembagian ini memperluas deteksi menjadi penilaian kelayakan lintas dan genggaman bagi robot, karena model tidak hanya menghasilkan koordinat buah, tetapi juga kategori oklusi yang dipakai untuk perencanaan jalur lengan, pemilihan pose genggaman, dan penghindaran rintangan. OAFBC-Net diusulkan sebagai jaringan RGB-depth ringan yang menggabungkan fusi frekuensi lintas modal, pemodelan konteks, dan fusi multiskala.

Dataset dikumpulkan di Stasiun Pertama Jalan Taihang, Universitas Pertanian Hebei, Shunping, Baoding, menggunakan Intel RealSense D455 pada resolusi 1.280 × 720 piksel. Dataset berisi 3.000 pasangan citra RGB-peta kedalaman dengan 134.999 instan beranotasi: 57.285 SO, 31.006 NO, dan 46.708 HO. Peta kedalaman mengalami penyaringan bilateral, pengisian lubang, dan penyaringan median sebelum pelatihan. Pembagian latih, validasi, dan uji memakai rasio 7:1:2 dan dilakukan berdasarkan batch akuisisi, identitas pohon, serta grup citra, bukan pengacakan per citra, untuk mencegah kebocoran data. Stabilitas diuji dengan tiga seed (0, 42, 2026) dan validasi silang lima lipat dengan himpunan uji independen yang tetap. Pelatihan memakai 300 epoch, masukan 640 × 640, batch 8, optimisator SGD, dan fungsi rugi standar YOLOv11 yang terdiri atas DFL, klasifikasi, dan CIoU.

Mekanisme intinya adalah FAPEF, yang dipasang pada peta fitur P4 dan P5. Setiap alur distabilisasi dengan Dynamic Tanh, diubah ke ranah frekuensi memakai FFT ortogonal, lalu spektrum amplitudo dan fase nilai-principal dari RGB serta kedalaman digabungkan dengan bobot adaptif yang dapat dipelajari; spektrum kompleks hasil fusi direkonstruksi dan dikembalikan ke ranah spasial dengan IFFT ortogonal. Penulis membatasi FAPEF pada P4 dan P5 karena P3 beresolusi lebih tinggi dan lebih mahal; pada P3 fusi cukup memakai konkatenasi ringan dan kompresi konvolusi. Modul TCG menambahkan tiga jenis konteks: konteks lokal dari konvolusi depthwise 3 × 3, konteks sekitar dari konvolusi terdilasi dengan laju 2 yang memperluas reseptif field menjadi 5 × 5, serta konteks global dari perhatian kanal melalui pooling rata-rata dan MLP dengan rasio reduksi 16; ketiganya disusun dalam struktur CSP bergaya C3k2 hanya pada P4 dan P5. BiFPN pada neck mengintegrasikan fitur P3 sampai P5 dengan bobot yang dapat dipelajari serta jalur atas-bawah dan bawah-atas.

Pada himpunan uji, OAFBC-Net mencapai AP50 berturut-turut 72,1%, 87,3%, dan 57,9% untuk SO, NO, dan HO. Dengan ketiga modul aktif, presisi, recall, mAP50, dan mAP50-95 masing-masing mencapai 64,8%, 71,7%, 72,4%, dan 55,2%, dibandingkan mAP50 64,8% pada baseline dwimodal tanpa modul tersebut. Model memiliki 3,6 juta parameter dan 10,2 GFLOPs; latensi total per citra 11,3 ms dengan kecepatan 88,5 FPS pada NVIDIA GeForce RTX 4070 Laptop GPU pada batch 1 dan masukan 640 × 640. Metrik dihitung dengan mencocokkan kotak ikat prediksi dan kebenaran satu lawan satu serta menghitung TP ketika IoU minimal 0,50; AP50 adalah luas di bawah kurva presisi-recall per kelas, sedangkan mAP50 adalah rata-rata aritmetika dari tiga AP50 kelas.

Batasan yang dinyatakan penulis mencakup perlunya validasi lintas lokasi, varietas apel, struktur pohon, dan tahap pertumbuhan, karena data berasal dari satu kebun. Citra kedalaman dipengaruhi derau sensor, lubang, gangguan cahaya kuat, dan perubahan jarak akuisisi; ketika perbedaan kedalaman antara buah dan ranting kecil, model masih dapat meleset. Analisis berlapis pencahayaan menunjukkan cahaya matahari langsung menaikkan Invalid Depth Ratio pada kotak ikat HO dan menurunkan AP50 HO sebesar 7,3 poin persentase, sehingga sebagian kesenjangan HO berasal dari kegagalan sensor D455, bukan semata rancangan jaringan. Validasi pada platform tertanam berdaya rendah, terminal seluler, dan robot pemanen nyata belum dilakukan; ketahanan terhadap hujan, kabut, cahaya belakang kuat, malam, oklusi daun parah, dan tandan rapat juga masih perlu ditingkatkan. Penulis menyatakan data tersedia atas permintaan penulis korespondensi.
