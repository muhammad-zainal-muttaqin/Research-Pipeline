# Citrus yield estimation based on multi- object tracking in video streams using an improved YOLOv8n model

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `si2026citrus` |
| Judul asli | Citrus yield estimation based on multi- object tracking in video streams using an improved YOLOv8n model |
| Penulis | Si, N.; others |
| Tahun | 2026 |
| Venue | Journal of Fruit Science |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [si2026citrus.pdf](../pdf/si2026citrus.pdf)
- DOI resmi: https://doi.org/10.13925/j.cnki.gsxb.20250487

## Gambaran Umum
Makalah ini membangun sistem estimasi hasil jeruk dari aliran video yang direkam dengan mengelilingi setiap pohon (rekaman rotasi 360°). Sistem terdiri atas detektor YOLOv8n yang dimodifikasi (YOLOv8n-SC) dan pelacak multi-objek (*multi-object tracking*, MOT) DeepSORT yang memberi nomor identitas (ID) pada setiap buah sehingga buah yang sama pada bingkai berbeda dihitung satu kali. Naskah ini adalah *preprint* SSRN yang belum ditelaah sejawat.

Data berasal dari 20 pohon jeruk pada fase pembesaran buah di rumah kaca Zhenjiang, Provinsi Jiangsu, Tiongkok. Tiap pohon direkam dalam sembilan kombinasi tiga kondisi pencahayaan (cerah, mendung, penerangan buatan) dan tiga sudut pengambilan (atas, horizontal, bawah), sehingga terkumpul 180 video dan 9.000 citra.

Hasil utama: YOLOv8n-SC mencapai *recall* 97,6% dan mAP50 93,7% pada seluruh data, masing-masing 2,0 dan 3,5 poin persentase di atas YOLOv8n asli (nilai selisih sesuai pernyataan makalah). Pada pencahayaan buatan dan pengambilan horizontal, MOTA mencapai 90,8%, MOTP 94,0%, dan akurasi hitungan rerata (*average counting precision*, ACP) 89,46% dengan galat absolut rerata (MAE) 9,98.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Estimasi hasil jeruk saat ini umumnya dilakukan dengan pengambilan sampel manual yang melelahkan dan lambat. Metode berbasis citra tunggal dinilai penulis tidak cukup presisi untuk menghitung buah, karena oklusi dan variasi cahaya. Pelacakan tradisional (aliran optik, selisih bingkai) dibatasi oleh variasi iluminasi dan gangguan latar, sedangkan pelacakan berbasis LiDAR rentan terhadap oklusi dan derau.

Pengambilan video yang lazim dilakukan sejajar antarbaris, yang cocok bagi pohon berpenopang atau espalier. Pohon jeruk modern ditanam pada jarak seragam dengan cabang menyebar radial, sehingga buah tersebar pada berbagai ketinggian dan arah. Penulis berargumen bahwa perekaman mengelilingi pohon memberi citra permukaan menyeluruh dan mengurangi galat akibat oklusi.

## Ide Utama
Gagasannya adalah menghitung buah sebagai jumlah ID unik pada video rotasi: detektor menemukan buah pada tiap bingkai, DeepSORT mempertahankan identitas buah yang sama saat kamera berputar, dan ID tertinggi (MAX ID) menjadi hitungan. Detektor diperkuat untuk objek kecil karena buah jeruk hijau yang kecil dan mirip daun menempati kurang dari 0,1% luas citra. Penulis juga menyelidiki pengaruh kondisi pencahayaan dan sudut pengambilan terhadap akurasi.

## Cara Kerja Langkah demi Langkah

```
 Video rotasi 360 per pohon -> ekstraksi bingkai -> YOLOv8n-SC -> DeepSORT -> MAX ID
```

### 1. Akuisisi data
Perekaman memakai kamera olahraga DJI OSMO Action4 dan lampu LED pada tongkat teleskopik (maksimum 1,5 m), diputar 360° mengelilingi pohon dengan radius sekitar 1,2–1,5 m. Pohon berjarak antarbaris 2,5–3 m, antartanaman 2–2,5 m, dan tinggi sekitar 2 m. Sudut atas berarti menunduk 30°, sudut bawah mendongak 30°, dan horizontal setinggi rerata kanopi $H$. Tiap video berformat MP4 3840×2880, 30 bingkai per detik, berdurasi sekitar 30 detik. Satu citra diambil tiap 18 bingkai, menghasilkan 9.000 citra (3.000 citra per kondisi pencahayaan). Anotasi memakai AnyLabeling dalam format YOLO; hanya buah hijau yang kontur terlihat atau dapat disimpulkan pada pohon tersebut yang dianotasi (buah jatuh, buah baris belakang, buah di tepi citra, dan buah retak tidak). Data dibagi acak 4:1 menjadi latih dan uji. Varietas atau kultivar tidak dilaporkan selain lokasi "Hongmeiren".

### 2. Detektor YOLOv8n-SC
Tiga modifikasi atas YOLOv8n: (a) kepala deteksi tambahan untuk objek kecil dengan peta fitur 160×160; (b) modul perhatian *Convolutional Block Attention Module* (CBAM) pada modul C2f tulang punggung (C2f_CBAM); (c) fungsi kerugian *Weighted Intersection over Union* (WIoU) menggantikan CIoU. Pelatihan 400 *epoch* dengan laju belajar awal 0,01 pada RTX 2080 Ti 11 GB (PyTorch, CUDA 11.2).

### 3. Pelacakan dan penghitungan dengan DeepSORT
Gerak buah antarbingkai dianggap seragam dan diestimasi dengan filter Kalman. Asosiasi memakai algoritma Hungaria dengan pencocokan bertingkat (*cascade*) yang menggabungkan jarak Mahalanobis dan jarak kosinus fitur penampakan, lalu pencocokan IoU. Setiap lintasan memiliki *age*; lintasan dihapus bila tidak cocok kembali dalam `max_age` = 90 bingkai. ID bernomor mulai 1 diberikan menurut urutan kemunculan, dan nilai ID maksimum menjadi hasil hitungan (MAX ID). Ambang keyakinan deteksi 0,7.

### 4. Acuan hitungan
Lima peneliti menghitung manual buah pada tiap pohon sambil merekam; rerata dipakai sebagai nilai kebenaran kebun (*orchard ground truth*). Buah pada video juga dihitung dan dirata-ratakan sebagai kebenaran video. Perhitungan galat dilakukan terhadap kebenaran video; kebenaran kebun hanya sebagai referensi.

## Eksperimen dan Hasil
Metrik deteksi: P, R, mAP50, mAP50-95, FLOPs. Metrik pelacakan: MOTA, MOTP, FPS, dan laju pergantian ID (*ID Switch Rate*, IDSR). Metrik hitungan: RMSE, MAE, dan ACP.

Perbandingan detektor pada seluruh data (Tabel 1):

| Model | P (%) | R (%) | mAP50 (%) | mAP50-95 (%) | Ukuran (M) | FLOPs (G) |
|---|---|---|---|---|---|---|
| YOLOv8n | 93,7 | 95,6 | 90,2 | 59,1 | 14,5 | 8,1 |
| Faster RCNN | 88,1 | 79,3 | 84,7 | 56,5 | 100,3 | 65,2 |
| YOLOv8n-SC | 97,2 | 97,6 | 93,7 | 60,6 | 14,8 | 7,9 |
| YOLOv10n | 94,5 | 96,9 | 90,8 | 59,9 | 8,7 | 6,8 |

Ablasi (Tabel 2): kepala deteksi tambahan menaikkan R dari 95,6 ke 96,2 dan mAP50 dari 90,2 ke 92,6; dengan CBAM, R 96,5 dan mAP50 93,3; dengan ketiganya, R 97,6 dan mAP50 93,7. Teks ekstraksi menampilkan baris ablasi tanpa kolom yang jelas sehingga kombinasi tepat tiap baris diambil dari urutan tanda centang dan sebaiknya diperiksa pada PDF.

Pencahayaan (Tabel 3, mAP50/mAP50-95): cerah 83,5/45,1; mendung 96,1/61,4; penerangan buatan 98,2/66,9.

Sudut pengambilan, pada penerangan buatan (Tabel 4):

| Sudut | MOTA (%) | MOTP (%) | FPS | IDSR (%) |
|---|---|---|---|---|
| Atas | 84,9 | 95,7 | 21,74 | 5,6 |
| Horizontal | 90,8 | 94,0 | 21,74 | 11,8 |
| Bawah | 85,8 | 87,9 | 21,74 | 27,4 |

Hitungan (Tabel 5): ACP, RMSE, dan MAE untuk sudut atas 88,87, 11,35, dan 9,97; horizontal 89,46, 10,83, dan 9,98; bawah 81,03, 22,16, dan 20,01. Jumlah buah per kolom (kebenaran kebun, kebenaran video, prediksi algoritma) tidak terbaca andal dari teks ekstraksi sehingga tidak dilaporkan di sini.

Perbandingan pelacak (Tabel 6, YOLOv8n-SC sebagai detektor):

| Pelacak | RMSE | MAE | FPS | ACP (%) |
|---|---|---|---|---|
| SORT | 17,50 | 16,33 | 31,84 | 84,81 |
| Tracktor | 11,21 | 10,67 | 25,25 | 86,37 |
| DeepSORT | 10,83 | 9,98 | 21,74 | 89,46 |

Penulis menyatakan DeepSORT unggul 4,65 dan 3,09 poin persentase atas SORT dan Tracktor, tetapi paling lambat karena menghitung fitur penampakan tiap bingkai.

## Kelebihan dan Keterbatasan
Kelebihan: perekaman rotasi menjawab kebutuhan pohon berbentuk bebas; ada ablasi, perbandingan pelacak, dan analisis pencahayaan serta sudut; ID dipertahankan lintas bingkai dengan jendela hilang 90 bingkai.

Keterbatasan yang dinyatakan penulis: pengambilan sudut atas kehilangan banyak buah akibat oklusi daun sehingga hitungannya tidak layak dipakai; sudut bawah menimbulkan pergantian ID yang berat; pada pengambilan horizontal sumber galat utama adalah laju pergantian ID 11,8% akibat oklusi timbal balik; cahaya matahari menurunkan deteksi karena pantulan dan bayangan. Contoh dalam makalah menunjukkan buah yang hilang lebih dari 90 bingkai mendapat ID baru (ID 92, 93, 94 untuk buah yang sebelumnya ID 16, 17, 30).

Menurut pembacaan ringkasan ini, kesimpulan terbaik diperoleh pada penerangan buatan, sehingga penerapan di kebun terbuka belum teruji. Data berasal dari 20 pohon pada satu lokasi rumah kaca dan hanya buah hijau fase pembesaran; hanya satu kelas buah. Pembagian latih-uji 4:1 dilakukan secara acak pada citra yang diambil dari video yang sama, sehingga citra latih dan uji dapat berasal dari pohon yang sama (kemungkinan kebocoran data, tidak dibahas penulis). Jumlah pohon untuk evaluasi hitungan per sudut tidak jelas dari teks. Makalah berstatus *preprint*.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat lebih dari sekali dengan mekanisme pelacakan temporal: DeepSORT memberi ID pada buah yang sama pada bingkai berurutan selama kamera mengelilingi pohon, dan hitungan adalah ID maksimum. Dengan kata lain, identitas lintas pandang dijaga lewat kontinuitas video, tanpa pencocokan antarsisi pohon atau rekonstruksi 3D. Kesalahan pelacakan (pergantian ID, ID baru setelah hilang lebih dari 90 bingkai) dilaporkan melalui IDSR dan contoh kualitatif.

Hitungan tidak dilaporkan per kelas; hanya satu kelas buah (jeruk hijau). Acuan hitungnya ada dua: hitungan manual lima peneliti di kebun (kebenaran kebun) dan hitungan manual pada video (kebenaran video); galat dihitung terhadap yang kedua. Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi: pola pengambilan rotasi mengelilingi pohon, penggunaan ID tertinggi sebagai hitungan, dan pelaporan IDSR untuk mengukur kegagalan identitas. Keterbatasan penerapannya adalah pelacakan bergantung pada kontinuitas video, sedangkan citra sawit diambil per sisi diskret.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `si2026citrus`.

Si dkk. (2026, *preprint*) mengusulkan estimasi hasil jeruk dari video rotasi 360° per pohon dengan detektor YOLOv8n-SC (kepala deteksi tambahan, CBAM, WIoU) dan pelacak DeepSORT. Pada 20 pohon (180 video, 9.000 citra), detektor mencapai mAP50 93,7% dan *recall* 97,6%; pada penerangan buatan dengan pengambilan horizontal, MOTA 90,8% dan ACP 89,46% dengan MAE 9,98, lebih tinggi daripada SORT dan Tracktor.

Catatan verifikasi data: Angka detektor ada pada Tabel 1 dan 2, pencahayaan pada Tabel 3, pelacakan pada Tabel 4, hitungan pada Tabel 5, dan pembanding pelacak pada Tabel 6; angka abstrak (R 97,6%, mAP50 93,7%, MOTA 90,8%, ACP 89,46%, MAE 9,98) sesuai tabel. Ekstraksi PDF memecah tabel menjadi satu nilai per baris. Kolom jumlah buah Tabel 5 tidak dapat dipetakan dan tidak dikutip. Teks menyebut RMSE dan MAE horizontal lebih rendah 11,33 dan 10,03 daripada sudut bawah, sedangkan angka tabel (10,83 dan 9,98 versus 22,16 dan 20,01) memberi selisih 11,33 dan 10,03, sehingga konsisten. Teks menyebut MOTP 94,0% sebagai "tracking precision", sesuai Tabel 4. Rumus kerugian dan metrik tidak terbaca karena ekstraksi. Judul pada berkas (*Citrus Yield Estimation Method Based on Video Stream and YOLOv8n Object Tracking*) berbeda dari judul pada daftar tugas.
