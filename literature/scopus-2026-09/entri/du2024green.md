# Green pepper fruits counting based on improved DeepSort and optimized Yolov5s

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `du2024green` |
| Judul asli | Green pepper fruits counting based on improved DeepSort and optimized Yolov5s |
| Penulis | Du, Pengcheng; Chen, Shang; Li, Xu; Hu, Wenwu; Lan, Nan; Lei, Xiangming; Xiang, Yang |
| Tahun | 2024 |
| Venue | Frontiers in Plant Science |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | sweet pepper |

## Tautan Akses
- PDF: [du2024green.pdf](../pdf/du2024green.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2024.1417682

## Gambaran Umum

Makalah ini mengusulkan metode pencacahan otomatis buah cabai hijau (*green pepper*) pada video lapangan dengan menggabungkan detektor objek dan pelacakan multi-objek (*multi-object tracking*, MOT). Detektornya adalah CS_YOLOv5s, yaitu YOLOv5s yang diubah dengan struktur Slim-Neck berbasis GSConv dan modul perhatian CBAM. Pelacaknya adalah DeepSort yang diperbaiki dengan pencocokan fitur tampilan tambahan dan optimasi lintasan yang diadaptasi dari SportsTrack. Jumlah buah diperoleh dengan menghitung identitas (ID) unik yang diberikan pelacak.

Data berupa 1.200 citra (diperluas menjadi 4.800 dengan augmentasi) dan tujuh video dari kultivar 'Xiangyan 15' di lahan percobaan Hunan Agricultural University, Changsha. Pengambilan data memakai mobil kendali jarak jauh yang membawa telepon seluler pada penstabil genggam.

Hasil utama: dalam abstrak, CS_YOLOv5s dilaporkan mencapai mAP 98,96%, presisi 95%, *recall* 97,3%, dan waktu deteksi 6,3 ms per citra, meskipun angka pada Tabel 3 dan 4 berbeda (lihat catatan verifikasi). Optimasi DeepSort mengurangi pertukaran ID sebesar 29,41%. Pada pencacahan tiga video uji, ACP (*Average Counting Precision*) 95,33%, MAE 3,33, dan RMSE 3,74; dibandingkan DeepSort asli, ACP naik 7,2%, sedangkan MAE dan RMSE turun masing-masing 6,67 dan 6,94.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi hasil cabai hijau masih bergantung pada pencuplikan manual yang memakan waktu dan tenaga. Pencacahan pada citra tunggal tidak mewakili jumlah buah seluruh kebun, sehingga banyak penelitian memakai pencuplikan citra berinterval, tetapi cara ini menimbulkan hitungan ganda karena buah yang sama muncul pada citra yang berdekatan. Penulis mengutip upaya pencocokan antarcitra (misalnya pencocokan *patch* dengan waktu rata-rata 5,33 menit per urutan citra) sebagai solusi yang lambat.

Pelacakan pada video memberi satu ID per buah sehingga hitungan sama dengan jumlah ID, tetapi pada kebun yang rapat buah tertutup daun dan buah lain, lalu hilang dan muncul kembali. Cabai hijau mempunyai warna mirip daun, tersebar rapat, dan tertutup ranting, sehingga deteksi sulit. Perubahan ciri gerak akibat gerakan kamera, tumpang tindih buah, dan oklusi menyebabkan pertukaran ID (*ID switch*), yang pada akhirnya menggandakan hitungan.

## Ide Utama

Penulis menyatakan bahwa deteksi yang baik dan pelacakan yang tepat sama-sama menentukan akurasi hitungan. Idenya ada tiga: detektor yang ringan dan tetap peka (Slim-Neck dengan GSConv ditambah CBAM), penambahan pencocokan fitur tampilan setelah pencocokan bertingkat (*cascade matching*) DeepSort agar buah yang ciri geraknya berubah tiba-tiba tetap dikaitkan dengan lintasan lamanya, dan pascapemrosesan lintasan yang menggabungkan dua segmen lintasan stabil yang ternyata milik buah yang sama.

Mekanisme identitas yang dipakai adalah kontinuitas dalam satu urutan video, dengan penyatuan lintasan terfragmentasi berdasarkan kemiripan tampilan, posisi, dan bentuk.

## Cara Kerja Langkah demi Langkah

```
 Video -> CS_YOLOv5s -> deteksi -> DeepSort (Kalman + ReID + cascade)
                                     -> pencocokan tampilan tambahan
                                     -> optimasi lintasan (gabung segmen)
                                     -> hitung ID unik = jumlah buah
```

### 1. Akuisisi data

Kultivar 'Xiangyan 15' ditanam di lahan percobaan Hunan Agricultural University, Distrik Furong, Changsha, Provinsi Hunan. Mobil kendali jarak jauh (penggerak empat roda, rentang kecepatan 0 sampai 2 m/s, beban 0 sampai 5 kg) membawa telepon OPPO Reno6 Pro+ pada penstabil DJI Osmo Mobile SE. Pengambilan data dilakukan pada pukul 08.00 (intensitas cahaya rendah), 12.00 (tinggi), dan 16.00 (sedang) dengan kecepatan 0,2 m/s. Dataset memuat 1.200 citra 1920 × 1080 (JPG) dan tujuh video 1920 × 1080 (MP4) pada 30 fps. Augmentasi (rotasi, *Gaussian blur*, pencerminan, perubahan kecerahan) memperbesar set citra dari 1.200 menjadi 4.800, dibagi latih dan uji dengan rasio 7:3. Video dibagi latih dan uji dengan rasio 4:3 (empat latih, tiga uji). Tiga video uji berdurasi 12, 17, dan 20 detik (Video001 sampai Video003), sedangkan empat video latih berdurasi 6, 11, 17, dan 27 detik.

### 2. Detektor CS_YOLOv5s

Pada YOLOv5s, modul C3 pada *Neck* diganti VoV-GSCSP dan konvolusi biasa diganti GSConv (gabungan konvolusi standar dan konvolusi terpisah-kedalaman dengan pengacakan kanal), sehingga parameter berkurang. CBAM (perhatian kanal dan spasial) dipasang pada sambungan antara *Neck* dan kepala prediksi. Pelatihan: citra 640 × 640, SGD, *weight decay* 0,005, momentum 0,937, ukuran *batch* 4, 300 *epoch*.

### 3. DeepSort dan perbaikannya

DeepSort memakai filter Kalman, algoritma Hungaria, model ReID, dan pencocokan bertingkat (jarak Mahalanobis untuk gerak, jarak kosinus untuk tampilan, lalu IoU untuk sisa). Penulis membedakan dua jenis pertukaran ID: permanen (ID berganti dan tidak kembali) dan reversibel (ID berganti sesaat lalu kembali, tetapi ID sementara sempat tercatat dalam hitungan). Perbaikan pertama menambahkan pencocokan fitur tampilan setelah pencocokan bertingkat. Perbaikan kedua mengadaptasi optimasi lintasan SportsTrack untuk lintasan berkesinambungan dan lintasan terfragmentasi: lintasan tidak stabil dan setengah stabil dibuang berdasarkan varians kemiripan tampilan; untuk dua segmen stabil yang panjang dan cukup lama, matriks kemiripan dihitung, dan bila jumlah nilai kemiripan memenuhi syarat (melebihi setengah dari hasil kali panjang kedua segmen), posisi dan bentuk dicocokkan; bila semua syarat terpenuhi, kedua lintasan digabung menjadi satu ID. Model ReID memakai ResNet dengan bobot awal Market, citra 128 × 256, SGD, momentum 0,9, ukuran *batch* 64, 300 *epoch*.

### 4. Evaluasi

Metrik deteksi: presisi, *recall*, mAP, waktu deteksi per citra, GFLOPs. Metrik pelacakan: ID Switch (IDs), MOTA, MOTP. Metrik hitungan: ACP, MAE, RMSE yang dihitung antarvideo (N adalah jumlah video). Perangkat: workstation dengan Xeon W2155, RAM 32 GB, RTX 2080Ti 12 GB, PyTorch 1.8, Windows 10.

## Eksperimen dan Hasil

Ablasi detektor pada set uji (Tabel 3):

| Model | P (%) | R (%) | mAP (%) | Waktu per citra (ms) | GFLOPs |
|---|---|---|---|---|---|
| YOLOv5s | 99 | 93,9 | 96,8 | 9,4 | 16,3 |
| + Slim-Neck + GSConv | 98,7 | 94,5 | 96,9 | 6,0 | 15,3 |
| + Slim-Neck + GSConv + CBAM (CS_YOLOv5s) | 98,6 | 95 | 97,3 | 6,1 | 15,4 |

Perbandingan detektor (Tabel 4): RT-DETR memperoleh P 95,80%, R 96,80%, mAP 97,90% dengan 108,30 GFLOPs; YOLOv3-tiny P 99,00%, R 78,00%, mAP 88,00%, 19,00 GFLOPs; YOLOv6s P 99,00%, R 90,80%, mAP 95,20%, 44,20 GFLOPs; YOLOv8s P 99,20%, R 91,40%, mAP 95,50%, 28,40 GFLOPs.

Pelacakan pada tiga video uji, gabungan (Tabel 6; GT 247 sasaran): DeepSort asli MOTA 90,9%, MOTP 87,1%, IDs 68; dengan pencocokan tampilan MOTA 91,3%, MOTP 86,9%, IDs 51; dengan optimasi lintasan saja MOTA 90,9%, MOTP 87,1%, IDs 65; dengan keduanya MOTA 91,3%, MOTP 86,9%, IDs 48. Pengurangan ID switch tersendiri adalah 25% (pencocokan tampilan) dan 4,41% (optimasi lintasan), dan 29,41% untuk gabungan, sesuai teks.

Pencacahan per video (Tabel 7; hanya hitungan DeepSort dan gabungan keduanya yang dikutip):

| Video | GT | DeepSort (hitungan, ACP, MAE) | DeepSort + tampilan + optimasi (hitungan, ACP, MAE) |
|---|---|---|---|
| 001 (cahaya sedang, kerapatan rendah) | 57 | 63, 89,47%, 6 | 62, 91,23%, 5 |
| 002 (cahaya sedang, kerapatan tinggi) | 95 | 104, 90,52%, 9 | 96, 98,95%, 1 |
| 003 (cahaya rendah, kerapatan tinggi) | 96 | 111, 84,38%, 15 | 100, 95,83%, 4 |

Ringkasan hitungan (Tabel 8): DeepSort asli ACP 88,13%, MAE 10, RMSE 10,68; dengan pencocokan tampilan 93,59%, 5, 5,07; dengan optimasi lintasan 90,57%, 7,67, 8,27; dengan keduanya 95,33%, 3,33, 3,74. Pengaruh detektor (Tabel 9) dengan DeepSort yang diperbaiki: YOLOv5s ACP 93,29%, MAE 5,33, RMSE 5,58, 15,9 FPS; CS_YOLOv5s ACP 95,33%, MAE 3,33, RMSE 3,74, 16,2 FPS. Penulis menyatakan kecepatan pemrosesan video sekitar 17 FPS, yang belum cukup untuk video 30 FPS secara waktu-nyata.

## Kelebihan dan Keterbatasan

Kelebihan: metode memisahkan pengaruh tiap komponen (detektor, pencocokan tampilan, optimasi lintasan) melalui ablasi, menguji tiga kondisi cahaya dan kerapatan buah, serta menunjukkan bahwa detektor yang lebih baik menurunkan galat hitungan.

Keterbatasan yang dinyatakan penulis: kecepatan baru sekitar 17 FPS dan proses pencocokan menyita banyak komputasi, sehingga pemrosesan waktu-nyata video 30 FPS memerlukan penurunan laju bingkai menjadi 15 FPS dan kecepatan mobil dikurangi setengah; dataset dari satu kultivar dan satu lokasi perlu diperluas ke varietas dan kondisi tumbuh lain; pencocokan perlu disederhanakan.

Menurut pembacaan ringkasan ini, jumlah video uji hanya tiga dengan GT 57, 95, dan 96 buah, sehingga metrik hitungan bersandar pada sampel kecil. Perbaikan MOTA dan MOTP kecil, dan beberapa kolom Tabel 7 menunjukkan hitungan yang lebih tinggi dari GT pada semua metode (hitungan berlebih), yang menandakan duplikasi belum sepenuhnya hilang. Hitungan diacu pada jumlah buah beranotasi pada video, bukan hasil panen. Hasil tidak dilaporkan per kelas kematangan, dan kerangka bergantung pada kontinuitas gerak dalam satu urutan video.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali pada bingkai-bingkai berurutan video yang direkam dengan kamera bergerak sepanjang barisan. Mekanismenya adalah pelacakan (DeepSort dengan Kalman, ReID, dan pencocokan bertingkat) disertai pencocokan tampilan tambahan dan penggabungan lintasan terfragmentasi; hitungan adalah jumlah ID unik. Hitungan tidak dilaporkan per kelas, dan acuan hitungnya adalah jumlah sasaran beranotasi pada video (kolom GT), bukan panen atau hitung manual di lapangan.

Hal yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: gagasan menambahkan pencocokan tampilan setelah pencocokan gerak serta penggabungan lintasan terfragmentasi yang memakai kemiripan tampilan, posisi, dan bentuk. Makalah tidak membahas pencocokan antarsisi pohon yang tidak berurutan, sehingga ketergantungannya pada kontinuitas gerak membatasi pemindahan langsung.

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `du2024green`.

Du dkk. mengusulkan pencacahan cabai hijau pada video dengan detektor CS_YOLOv5s (Slim-Neck GSConv dan CBAM) dan DeepSort yang diperbaiki dengan pencocokan fitur tampilan serta optimasi lintasan ala SportsTrack. Pada tiga video uji, ACP mencapai 95,33% dengan MAE 3,33 dan RMSE 3,74, dan pertukaran ID turun 29,41% dibandingkan DeepSort asli.

Catatan verifikasi data: angka hitungan dikutip dari Tabel 7, 8, dan 9; angka pelacakan dari Tabel 5 dan 6; angka detektor dari Tabel 3 dan 4. Terdapat ketidakkonsistenan internal pada makalah. Abstrak dan kesimpulan menyebut mAP 98,96%, presisi 95%, dan *recall* 97,3%, sedangkan Tabel 3 dan 4 mencatat P 98,6%, R 95%, mAP 97,3% untuk CS_YOLOv5s; urutan angka pada abstrak tampak tertukar dengan tabel dan mAP 98,96% tidak ditemukan pada tabel. Waktu deteksi 6,3 ms (abstrak) berbeda dari 6,1 ms (Tabel 3), dan abstrak menyebut pengurangan waktu 34,4% sedangkan teks hasil menyebut pengurangan 3,3 ms. Kesimpulan menyatakan IDs turun dari 68 menjadi 28, sedangkan Tabel 6 mencatat 48 (68 ke 48 sesuai dengan 29,41%). Rentang tabel diekstraksi satu sel per baris dan kolom "Count" pada beberapa baris Tabel 7 tidak muncul sehingga hanya baris yang terbaca yang dikutip; kolom hitungan baris DeepSort + pencocokan tampilan pada Tabel 7 terbaca dari urutan sel. Jumlah pohon atau barisan tidak dilaporkan, dan angka pada Gambar 9 sampai 11 tidak dapat diverifikasi dari teks.
