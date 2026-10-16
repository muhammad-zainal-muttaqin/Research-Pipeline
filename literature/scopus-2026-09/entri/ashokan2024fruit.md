# Fruit yield estimation and forecasting for precision agriculture

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ashokan2024fruit` |
| Judul asli | Fruit yield estimation and forecasting for precision agriculture |
| Penulis | Ashokan, Anju; Akbar, N. Ali |
| Tahun | 2024 |
| Venue | Aip Conference Proceedings |
| Kode | C1 (Gabungan beberapa pengamatan) |

## Tautan Akses
- PDF: [ashokan2024fruit.pdf](../pdf/ashokan2024fruit.pdf)
- DOI resmi: https://doi.org/10.1063/5.0196960

## Gambaran Umum
Makalah prosiding (AIP Conf. Proc. 3037, 020036, RIST2022) ini mengusulkan sistem estimasi dan peramalan hasil buah untuk pertanian presisi, dengan mangga sebagai buah yang dikerjakan. Estimasi dilakukan pada rekaman video: buah dideteksi dengan YOLOv5, dilacak antarbingkai dengan DeepSORT (dengan OSNet sebagai penyandi tampilan), dan jumlah buah diambil dari nilai pengenal jalur (*track ID*) tertinggi. Peramalan hasil nasional dilakukan terpisah dengan model ARIMA pada data produksi mangga India dari Indiastat.

Detektor dilatih pada kumpulan data 101 citra pohon mangga satu kelas (`mango`). Metrik deteksi yang dilaporkan adalah *precision* 82,4, *recall* 87,2, F1-score 71,9, dan mAP 89,6 (satuan persen tidak dinyatakan eksplisit). Makalah tidak melaporkan galat hitungan total hasil pelacakan terhadap hitungan sebenarnya, sehingga ketepatan penghitungan berbasis pelacakan tidak dapat dinilai dari teks.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Penulis menyatakan bahwa penghitungan manual memerlukan pengamat terampil, memakan waktu, mahal, dan berakurasi rendah, sehingga menyulitkan keputusan petani tentang panen, pemasaran, biaya produksi, dan alokasi sumber daya. Kebutuhan yang dirumuskan adalah sistem cerdas yang memperkirakan hasil buah saat ini dan meramalkan hasil mendatang.

Pada bagian karya terkait, makalah mengutip pendekatan terdahulu (Faster R-CNN dengan fusi pengklasifikasi, jaringan kaskade multitugas, kerangka penghitungan terawasi lemah WSCOUNT, serta YOLOv3 dan YOLOv4) sebagai latar deteksi buah. Makalah ini memilih YOLOv5 karena dinilai sesuai untuk deteksi dengan citra berkualitas tinggi.

## Ide Utama
Deteksi per bingkai dikombinasikan dengan pelacakan sehingga buah yang sama pada bingkai berbeda mendapat pengenal yang sama dan dihitung sekali. Jumlah buah pada video diambil dari nilai pengenal jalur tertinggi pada berkas keluaran pelacakan. Komponen peramalan bersifat terpisah: deret waktu produksi tahunan dimodelkan dengan ARIMA untuk memperkirakan produksi lima tahun ke depan.

## Cara Kerja Langkah demi Langkah
### 1. Akuisisi data
Kumpulan data mangga berupa citra jpeg buah mangga pada pohon, dengan kondisi tertutup daun, buah bertumpuk, dan pencahayaan beragam. Sumber, lokasi, kultivar, sensor, serta resolusi tidak dilaporkan. Teks menyebut pelatihan dengan 101 citra pohon mangga. Sumber dan sifat video uji untuk pelacakan tidak dijelaskan.

### 2. Pelabelan
Anotasi dibuat dengan LabelImg dalam format YOLO. Hanya satu kelas, `mango` (ID 0).

### 3. Pelatihan YOLOv5
YOLOv5s (CSPDarknet53 sebagai *backbone*, lapisan *neck* piramida fitur, dan kepala deteksi) dilatih di Google Colab dari bobot `yolov5s.pt` selama 100 epoch dengan batch 16 dan ukuran citra 224. Data dibagi 70% latih dan 30% uji. Ringkasan model: 213 lapisan, 7.012.822 parameter, 15,8 GFLOPs; pelatihan 100 epoch memakan 0,041 jam. NMS dipakai untuk menghindari deteksi ganda.

### 4. Pelacakan dengan DeepSORT
DeepSORT memakai filter Kalman untuk memprediksi posisi buah dari lokasi sebelumnya, dan mengasosiasikan deteksi antarbingkai dengan metrik jarak berdasarkan gerak dan tampilan. Setiap jalur memiliki ID, matriks fitur dari OSNet, status jalur, serta rerata dan kovarians untuk filter Kalman. Model yang dipakai adalah Yolov5-DeepSort-OSNet.

### 5. Penghitungan buah
Berkas `out.txt` berisi nomor bingkai, ID jalur, koordinat kotak, dan kelas. Kolom ID diambil dan nilai ID tertinggi dianggap sebagai jumlah mangga pada video.

### 6. Peramalan dengan ARIMA
Data luas, produksi, dan produktivitas mangga India dari Indiastat (tahun 1987–1998 dan 1991–1992 sampai 2021–2022) dibersihkan dari nilai kosong; kolom persentase yang sebagian besar kosong dibuang. Uji Augmented Dickey-Fuller menunjukkan data tidak stasioner, dan setelah diferensiasi orde pertama menjadi stasioner. Auto ARIMA memilih orde (p,d,q) berdasarkan AIC dan BIC; model musiman ARIMA dipakai untuk meramalkan produksi lima tahun, 2022 sampai 2026. Nilai parameter terpilih dan galat peramalan tidak ditulis dalam teks.

## Eksperimen dan Hasil
Evaluasi deteksi memakai *precision*, *recall*, F1, dan mAP pada bobot YOLOv5 hasil penyetelan halus.

| Metrik | Nilai dilaporkan |
|---|---|
| Precision | 82,4 |
| Recall | 87,2 |
| F1-score | 71,9 |
| mAP | 89,6 |

Menurut pembacaan ringkasan ini, F1-score 71,9 tidak konsisten dengan *precision* 82,4 dan *recall* 87,2, karena rumus F1 pada makalah akan memberi nilai sekitar 84,7 dari kedua angka itu (selisih sederhana dihitung ringkasan ini dan tidak tertulis di makalah). Penyebabnya tidak dijelaskan.

Hasil pelacakan dan penghitungan hanya ditampilkan sebagai gambar (Gambar 11 sampai 13), tanpa angka hitungan, acuan, atau galat dalam teks. Hasil peramalan (Gambar 16 sampai 18) juga disajikan sebagai grafik tanpa angka galat; penulis hanya menyatakan model "mencocokkan data secara mendekati".

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: sistem bekerja dengan kecepatan dan efisiensi tinggi, menggabungkan estimasi hasil saat ini dengan peramalan, dan dimaksudkan membantu petani.

Keterbatasan yang dinyatakan penulis tidak dibahas secara eksplisit; makalah tidak memuat bagian keterbatasan.

Menurut pembacaan ringkasan ini, terdapat beberapa keterbatasan. Validasi penghitungan berbasis pelacakan tidak dilaporkan secara kuantitatif. Kumpulan data pelatihan kecil (101 citra) dan ukuran masukan 224 sangat kecil untuk buah kecil. Klaim pengenal tertinggi sebagai hitungan mengandaikan tidak ada pergantian ID, sehingga pergantian ID atau buah yang hilang lalu muncul kembali akan membiaskan hitungan, dan hal ini tidak dianalisis. Peramalan ARIMA bekerja pada produksi nasional tahunan dan tidak terkait dengan hitungan buah dari video. Angka F1 tidak konsisten dengan komponennya.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat pada banyak bingkai dengan mekanisme pelacakan video: DeepSORT dengan filter Kalman dan asosiasi gerak serta tampilan (OSNet), dan hitungan diambil dari ID jalur tertinggi. Penghitungan tidak dilaporkan per kelas karena hanya ada satu kelas. Acuan hitungan (panen, hitungan lapangan, atau anotasi citra) untuk video tidak dilaporkan; hanya anotasi kotak pada citra latih yang dijelaskan. Penanganan buah yang terlihat dari sisi atau pohon berbeda tidak dibahas.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi adalah pola umum deteksi lalu asosiasi berbasis gerak dan tampilan dengan hitungan dari ID unik. Namun tanpa evaluasi hitungan dan tanpa penanganan sisi pohon, makalah ini hanya menjadi contoh pola dan bukan bukti efektivitas.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `ashokan2024fruit`.

Ashokan dan Akbar mengusulkan sistem estimasi hasil mangga pada rekaman video dengan YOLOv5s sebagai detektor dan DeepSORT (dengan OSNet) sebagai pelacak, dengan jumlah buah diambil dari ID jalur tertinggi, serta peramalan produksi mangga India lima tahun dengan ARIMA. Detektor dilatih pada 101 citra dan melaporkan *precision* 82,4, *recall* 87,2, F1 71,9, dan mAP 89,6; akurasi hitungan hasil pelacakan tidak dilaporkan secara kuantitatif.

Catatan verifikasi data: Metrik deteksi tertulis pada teks di bagian "Evaluation Criteria and Results"; satuan (persen atau pecahan) tidak dinyatakan. Angka 101 citra, 100 epoch, batch 16, ukuran citra 224, pembagian 70/30, dan ringkasan model ada pada bagian "Building YOLO V5 Model". Hasil pelacakan, penghitungan, dan peramalan hanya ada pada gambar yang tidak terbaca dari teks ekstraksi; kekonsistenan F1 dengan komponennya tidak dapat dijelaskan dari teks. Jumlah video, durasi, dan hitungan acuan tidak dilaporkan.
