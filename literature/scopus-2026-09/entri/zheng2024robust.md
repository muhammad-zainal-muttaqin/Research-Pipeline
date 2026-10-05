# A robust and efficient citrus counting approach for large-scale unstructured orchards

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zheng2024robust` |
| Judul asli | A robust and efficient citrus counting approach for large-scale unstructured orchards |
| Penulis | Zheng, Zhenhui; Wu, Meng; Chen, Ling; Wang, Chenglin; Xiong, Juntao; Wei, Lijiao; Huang, Xiaoman; Wang, Shuo; Huang, Weihua; Du, Dongjie |
| Tahun | 2024 |
| Venue | Agricultural Systems |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [zheng2024robust.pdf](../pdf/zheng2024robust.pdf)
- DOI resmi: https://doi.org/10.1016/j.agsy.2024.103867

## Gambaran Umum

Makalah ini mengusulkan alur pencacahan buah jeruk (*citrus*) secara daring (*online*) dari video pesawat nirawak (*unmanned aerial vehicle*, UAV) di kebun skala besar yang tidak terstruktur. Alur terdiri atas empat tahap: platform siaran video dan aplikasi kendali penerbangan bernama FlyCounter; peningkatan citra cahaya rendah dengan jaringan *Illumination-Adaptive-Transformer* (IAT); detektor baru bernama Fruit-YOLO (modifikasi YOLOv5 dengan modul SPD-Conv); dan pelacakan serta pencacahan dengan DeepSORT. Data berasal dari kebun jeruk di Distrik Baiyun, Guangzhou, Tiongkok, yang diambil pada April dan Juni 2023 memakai DJI PHANTOM 4 pada jarak pemotretan 1,5 m. Dua kelas dianotasi, yaitu *mature* (matang) dan *immature* (belum matang).

Hasil utama menurut ringkasan makalah: nilai P, R, dan mAP Fruit-YOLO dengan masukan citra yang ditingkatkan adalah 0,898, 0,854, dan 0,929, yaitu 1,7%, 4,6%, dan 3,5% lebih tinggi daripada citra asli. Pada pencacahan siang dan malam, rerata *ID switch*, MOTA, dan *Error Mean* adalah 63,7, 0,86, dan 9,81%. MAPE operasi luring dan daring masing-masing 4,36% dan 12,66%. Terdapat ketidakkonsistenan angka P dan mAP antara abstrak, teks Bagian 4.3.3, dan Tabel 1; hal ini dirinci pada catatan verifikasi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Penulis menyatakan dua kelemahan pada algoritma pencacahan jeruk yang ada. Pertama, ketahanan terhadap perubahan pencahayaan dan oklusi padat masih kurang. Kedua, efisiensi operasional sistem rendah, karena pengambilan data dilakukan terpisah dan luring, dan hasil diperoleh melalui pemrosesan video yang sudah direkam. Penelitian terdahulu juga lebih banyak memakai sensor yang dipegang orang atau dipasang pada kendaraan, sedangkan UAV dinilai lebih murah, fleksibel, dan kaya sudut pandang.

Pada sisi pencahayaan, kondisi berlawanan cahaya (*backlight*) siang hari dan cahaya rendah sore hari menurunkan kualitas citra dan kinerja detektor. Penelitian terdahulu sering memakai sumber cahaya tambahan atau membangun dataset per kondisi cahaya yang sulit dianotasi. Penulis juga membahas metode yang memanfaatkan informasi 3D (rekonstruksi, *Structure-from-Motion*, SLAM) yang akurat tetapi, menurut makalah, memerlukan perangkat mahal dan prosedur rumit, dengan rekonstruksi yang memakan beberapa jam hingga lebih dari sepuluh jam.

## Ide Utama

Gagasan utama adalah satu alur ujung ke ujung yang menyatukan akuisisi UAV daring, peningkatan citra cahaya rendah, deteksi yang peka terhadap buah kecil, dan pelacakan multi-objek, sehingga hasil hitung dapat diperoleh pada musim yang sama. Pelacakan lintas bingkai dipakai agar buah yang tertutup pada satu sudut dapat teramati dari sudut lain saat UAV bergerak. Penulis menyatakan bahwa alur ini mengutamakan pencacahan murah berbasis pelacakan-melalui-deteksi dibandingkan rekonstruksi 3D.

Untuk menghindari pembuatan data anotasi cahaya rendah, penulis membangun tiga kumpulan data cahaya rendah sintetis dengan gradien koefisien 0,6 (T1), 0,35 (T2), dan 0,1 (T3), lalu melatih IAT pada masing-masing.

## Cara Kerja Langkah demi Langkah

```
  UAV --> FlyCounter --> Nginx (RTMP) --> IAT --> Fruit-YOLO --> DeepSORT
  (video)   (kendali)    (siaran)       (cahaya)   (deteksi)    (hitung)
```

### 1. Akuisisi data

Terkumpul 23 video UAV; tiap video mencakup 7 sampai 17 pohon, tiap pohon memiliki 80 sampai 100 buah, dan durasi video 4 sampai 8 menit. Video dibagi acak: 13 video untuk pelatihan dan validasi, 10 video untuk pengujian. Dari 13 video pelatihan diekstrak bingkai pada interval tertentu hingga diperoleh 3.954 citra, dibagi 7:3 untuk pelatihan dan validasi. Anotasi memakai perangkat lunak DarkLabel. Varietas disebut jeruk (*orange*) dengan kulit kuning-hijau dan hijau. Citra diambil pada resolusi 5472 × 3078 piksel dari berbagai sudut dan waktu dalam sehari.

### 2. Platform transmisi UAV dan FlyCounter

Aplikasi FlyCounter menggantikan kendali manual agar UAV terbang stabil dengan kecepatan tetap; pengguna dapat mengatur ketinggian, arah, kecepatan, dan waktu terbang, serta sistem penghindar rintangan dimatikan agar UAV dapat terbang di kebun yang sempit. Video dikirim melalui protokol OcuSync ke perangkat Android, didorong ke server Nginx dengan protokol RTMP, lalu ditarik oleh komputer berkinerja tinggi untuk diproses.

### 3. Peningkatan citra dengan IAT

IAT adalah jaringan ringan dengan sekitar 90 ribu parameter, berisi cabang lokal (tiga modul PEM) dan cabang global (modul atensi yang menghasilkan matriks warna 3 × 3 dan nilai gamma, total sepuluh parameter). Pelatihan dilakukan 30 epoch pada tiga kumpulan data cahaya rendah sintetis, menghasilkan model MT1, MT2, dan MT3. Model MT2 dipilih.

### 4. Detektor Fruit-YOLO

Fruit-YOLO mengganti tujuh lapisan konvolusi langkah-2 pada YOLOv5 dengan modul SPD-Conv: lima pada *backbone* dan dua pada *neck*. Tujuannya mengurangi hilangnya informasi detail untuk buah kecil dan buah yang bertumpuk.

### 5. Pelacakan dan pencacahan

DeepSORT dipakai dengan filter Kalman (video 24 bingkai per detik, buah dianggap bergerak seragam), algoritma Hungarian pada pencocokan bertingkat (*cascade*) dan IoU, jarak Mahalanobis untuk gerak, dan jarak kosinus untuk penampilan. Jumlah akhir buah adalah banyaknya lintasan di seluruh kebun.

## Eksperimen dan Hasil

Perangkat keras: CPU Intel Xeon Gold 6256 dan GPU NVIDIA RTX A6000 48 GB. Detektor dievaluasi dengan P, R, mAP, dan FPS; peningkatan citra dengan PSNR dan SSIM; pencacahan dengan MOTA, *ID switch*, *L1 Loss*, *Error Mean* (galat per pohon), dan MAPE. Pembanding pencacahan adalah YOLOv5 dengan DeepSORT (disebut YOLO_DSORT). Acuan hitung adalah hitungan manual buah.

Deteksi (Tabel 1):

| Kelas | P YOLOv5 | P Fruit-YOLO | R YOLOv5 | R Fruit-YOLO | mAP YOLOv5 | mAP Fruit-YOLO |
|---|---|---|---|---|---|---|
| Mature | 0,874 | 0,879 | 0,878 | 0,889 | 0,910 | 0,921 |
| Immature | 0,821 | 0,842 | 0,715 | 0,727 | 0,794 | 0,806 |
| Rerata | 0,848 | 0,861 | 0,797 | 0,808 | 0,852 | 0,864 |

Kecepatan deteksi tercatat 69 FPS (YOLOv5) dan 65 FPS (Fruit-YOLO). Penulis menyebut peningkatan mAP rerata 1,20%, yang sesuai dengan selisih 0,864 dan 0,852.

Peningkatan citra: PSNR dan SSIM model MT2 adalah 26,571 dan 0,795, yaitu 2,189 dan 1,0% lebih tinggi daripada MT1 serta 5,612 dan 2,7% lebih tinggi daripada MT3. Pengujian memakai 188 citra cahaya cukup dan cahaya rendah yang diambil dengan UAV pada posisi tetap. Masukan citra yang ditingkatkan menaikkan P, R, mAP Fruit-YOLO sebesar 1,7%, 4,6%, dan 3,5%.

Pencacahan lokal (Tabel 2, rerata sepuluh video; lima siang dengan pencahayaan di atas 15 kLux dan lima sore di bawah 10 kLux):

| Metrik | YOLO_DSORT | Fruit-YOLO + IAT + DeepSORT |
|---|---|---|
| FN rerata | 32,9 | 21,2 |
| FP rerata | 138,5 | 99,3 |
| ID switch rerata | 79,1 | 63,7 |
| MOTA rerata | 0,80 | 0,86 |
| GT rerata | 1.302,2 | 1.302,2 |

Pencacahan keseluruhan (Tabel 3):

| Skenario | Metode | Hitungan / acuan | L1 Loss | Error Mean |
|---|---|---|---|---|
| Siang (77 pohon) | YOLO_DSORT | 6.991 / 6.065 | 926 | 12,03 |
| Siang (77 pohon) | Metode usulan | 6.726 / 6.065 | 661 | 8,58 |
| Sore (69 pohon) | YOLO_DSORT | 7.877 / 6.957 | 920 | 13,33 |
| Sore (69 pohon) | Metode usulan | 7.719 / 6.957 | 762 | 11,04 |

Luring versus daring (tiga baris pohon, 54 pohon, Tabel 5 pada Bahan Tambahan): tunda 7 sampai 10 detik, tingkat distorsi data 2,8%; luring memiliki rerata *ID switch* 26 dan MAPE 4,36%, daring 65,53 dan 12,66%. Pada operasi multi-UAV, waktu pemrosesan satu citra sekitar 0,18 s, 0,33 s, dan 0,44 s untuk satu, dua, dan tiga UAV, dan VRAM sekitar 4,95 g, 9,90 g, dan 14,85 g.

## Kelebihan dan Keterbatasan

Kelebihan menurut penulis: sistem ujung ke ujung dengan siaran daring; ketahanan pada cahaya rendah tanpa anotasi data cahaya rendah baru; biaya lebih rendah dan prosedur lebih sederhana daripada metode rekonstruksi 3D; dukungan beberapa UAV paralel.

Keterbatasan yang dinyatakan penulis: platform transmisi tidak bekerja baik pada jaringan buruk dan menyebabkan kegagalan pelacakan; setelah IAT, Fruit-YOLO dapat melewatkan atau keliru mendeteksi buah (misalnya tepi citra yang terlalu terang); pencacahan hanya dari satu sisi pohon sehingga terjadi *ID switch* dan buah terlewat, dan pencacahan lintas kamera dengan UAV kolaboratif diusulkan sebagai penelitian lanjutan. Kegagalan lain yang diuraikan: daun terdeteksi sebagai buah, serta rintangan (orang lewat, pilar batu) yang memutus pelacakan.

Menurut pembacaan ringkasan ini, kinerja per kelas (matang dan belum matang) hanya dilaporkan untuk deteksi, tidak untuk hitungan. Menurut pembacaan ringkasan ini, pengujian hanya pada satu kebun dan dua musim pengambilan data, dan angka P dan mAP pada ringkasan makalah tidak konsisten dengan tabel di badan teks sehingga perlu dikonfirmasi pada sumber asli.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali melalui pelacakan video: UAV bergerak di sepanjang baris pohon dan DeepSORT mempertahankan identitas buah antarbingkai (filter Kalman, algoritma Hungarian, fitur penampilan). Penulis menyatakan bahwa buah yang tertutup pada satu sudut dapat teramati dari sudut lain saat UAV bergerak. Penulis juga menyebut bahwa pencacahan hanya dari satu sisi pohon menimbulkan *ID switch* dan buah terlewat, dan pencocokan lintas kamera dari beberapa UAV hanya diusulkan sebagai pekerjaan mendatang, bukan diuji.

Hitungan total dilaporkan; hitungan per kelas tidak dilaporkan (kelas matang dan belum matang hanya muncul pada hasil deteksi). Acuan hitungnya adalah hitungan manual buah (*ground truth*) per pohon atau per video, bukan hasil panen. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi adalah pelaporan kegagalan pelacakan akibat penghalang dan *ID switch* yang menyebabkan hitungan berlebih atau tidak berlebih, serta pemisahan galat lokal (MOTA, *ID switch*) dan galat total (MAPE). Mekanisme pelacakan sendiri mengandaikan video kontinu dan tidak menangani identitas lintas sisi pohon.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `zheng2024robust`.

Ringkasan yang aman dikutip: Zheng dkk. (2024) mengusulkan alur pencacahan jeruk daring berbasis UAV yang menggabungkan peningkatan citra cahaya rendah (IAT), detektor Fruit-YOLO, dan pelacakan DeepSORT. Pada pengujian dengan 77 pohon siang hari dan 69 pohon sore hari, *Error Mean* per pohon adalah 8,58 dan 11,04, lebih rendah daripada 12,03 dan 13,33 pada YOLOv5 dengan DeepSORT. Penulis juga melaporkan MAPE 4,36% untuk operasi luring dan 12,66% untuk operasi daring pada 54 pohon, serta menyatakan bahwa pencacahan hanya dari satu sisi pohon menimbulkan *ID switch* dan buah terlewat.

Catatan verifikasi data: Angka deteksi per kelas ada pada Tabel 1; pencacahan lokal pada Tabel 2; pencacahan keseluruhan pada Tabel 3. Angka luring dan daring, kualitas peningkatan citra, dan tabel pembagian data berada pada Bahan Tambahan (Tabel 1, 3, 4, 5) yang tidak termasuk dalam teks ekstraksi; angka itu hanya diverifikasi dari kalimat badan teks. Terdapat ketidakkonsistenan: abstrak menulis P, R, mAP masukan citra ditingkatkan sebagai 0,898, 0,854, 0,929, sedangkan Bagian 4.3.3 menulis 0,878, 0,854, 0,899, dan Tabel 1 melaporkan rerata Fruit-YOLO (citra asli) 0,861, 0,808, 0,864. Angka *Error Mean* 9,81% pada abstrak tidak dinyatakan pada tabel; nilai itu sama dengan rerata sederhana 8,58 dan 11,04 (dihitung). Jumlah kolom tabel 2 pada ekstraksi bergeser sehingga hanya baris rerata dan beberapa baris yang diverifikasi. Data dinyatakan tersedia atas permintaan.
