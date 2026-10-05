# IoT-Based Precision Litchi Tracking and Counting Method Using Gated Metrics

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lu2025iot` |
| Judul asli | IoT-Based Precision Litchi Tracking and Counting Method Using Gated Metrics |
| Penulis | Lu, Jianqiang; Bao, Guoqing; Deng, Xiaoling; Han, Xiongzhe; Lan, Yubin; Wu, Haiwei |
| Tahun | 2025 |
| Venue | IEEE Internet of Things Journal |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | litchi/longan |

## Tautan Akses
- PDF: [lu2025iot.pdf](../pdf/lu2025iot.pdf)
- DOI resmi: https://doi.org/10.1109/jiot.2025.3561130

## Gambaran Umum

Makalah ini mengusulkan LitchiCount, metode pelacakan dan penghitungan buah leci dari video lapangan yang direkam dari beberapa sisi pohon. LitchiCount menggabungkan detektor ringan LitchiDet dengan modul pelacakan dan penghitungan yang memakai metrik asosiasi baru DG-GM (*distance-generalized IoU with gating mechanism*) dan strategi penghitungan area AreaC. Rancangannya dipandu oleh Grad-CAM++ dan uji validasi berbasis fitur penting. Sistem dipindahkan ke platform tepi (*edge*) Jetson AGX Xavier dan dipercepat dengan TensorRT.

Data berupa kumpulan data baru dari Conghua dan Zengcheng, Guangzhou, Tiongkok, pada Juni sampai Juli 2022 sampai 2023, mencakup varietas Huai Zhi, Guiwei, dan Xianjinfeng. Kumpulan data memuat 475 citra RGB dengan lebih dari 23.000 buah leci serta video berdurasi total 933 detik.

Hasil utama menurut penulis: LitchiCount mencapai *mean absolute percentage error* (MAPE) penghitungan 3,29% dan unggul atas metode berbasis DeepSORT, yang memiliki MAPE 49,79% (dengan Cross Line) dan 46,95% (dengan AreaC) pada pembanding, serta kecepatan bingkai delapan kali lebih tinggi. Pada deteksi, mAP LitchiDet naik 5,97% terhadap model awal dan ukuran model berkurang 33,56%. Angka-angka sel tabel tidak terbaca pada teks ekstraksi sehingga nilai absolut mAP tidak tersedia.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi hasil panen memerlukan penghitungan yang akurat, tetapi pada lapangan nyata deteksi buah menghasilkan banyak deteksi terlewat dan positif palsu. Penghitungan berbasis regresi memberi hitungan perkiraan tetapi kehilangan posisi tiap buah, sehingga tidak dapat mengaitkan target yang sama dan menyebabkan penghitungan terlewat dan berulang. Metode pelacakan multi-objek (*multi-object tracking*, MOT) masih mengalami pergantian ID, penghitungan berulang, dan deteksi terlewat, terutama ketika leci berada di tepi bidang pandang (*field of view*, FOV) kamera.

Penulis juga menyebut dua masalah lain. Model pembelajaran mendalam bersifat kompleks dan kurang dapat ditafsirkan, dan banyak model terlalu berat untuk dijalankan waktu-nyata pada perangkat tepi IoT. Selain itu, pohon leci besar sehingga FOV harus disesuaikan dan buah di satu sisi pohon dapat muncul kembali dari sudut lain, yang menyebabkan penghitungan berulang.

## Ide Utama

Gagasan utamanya adalah penghitungan melalui pelacakan (*counting by tracking*) berbasis paradigma pelacakan-berdasarkan-deteksi (*tracking-by-detection*), dengan tiga penyesuaian. Pertama, detektor dibuat sensitif terhadap objek kecil dan padat. Kedua, metrik asosiasi diganti agar jangkauan pencocokan diperluas saat oklusi tetapi dibatasi jaraknya agar ID tidak berpindah ke buah lain (*ID drift*). Ketiga, hanya buah yang berada di area tengah bingkai yang dihitung, tempat keadaan buah lebih stabil, sehingga hitungan berulang di tepi bingkai berkurang.

Penulis memakai Grad-CAM++ untuk mendiagnosis penyebab kinerja deteksi yang buruk, dan menguji secara eksperimen fitur mana (gerak atau tampilan) yang paling berkontribusi pada keputusan asosiasi. Hasil pengujian itu mengarahkan pemilihan DG-GM dibanding penambahan fitur tampilan.

## Cara Kerja Langkah demi Langkah

### 1. Akuisisi data

Data diambil dengan Huawei Mate40 (12 MP, f/1,9), iPhone 13 (12 MP, f/1,6), dan gimbal tiga sumbu, dari berbagai sudut dengan jarak 0,5 sampai 2 m. Kecepatan gerak pengambilan 0,1 sampai 0,3 m/s, laju bingkai 30 FPS, resolusi 1080p. Citra dianotasi manual dengan LabelImg dan dibagi menjadi 334 citra latih dan 141 citra uji (rasio 7:3). Augmentasi (pembalikan horizontal, kecerahan, *motion blur*, hujan simulasi, derau *salt-and-pepper*) menambah set latih menjadi 2.004 citra. Hitungan acuan untuk tiap video diperoleh dengan menghitung manual lebih dulu; metrik menyebut hitungan manual adalah rerata dari lima orang yang menghitung dari video.

### 2. Detektor LitchiDet

LitchiDet memiliki tiga komponen. Lapisan deteksi objek kecil ditambahkan dengan skala fitur baru 160 × 160, 80 × 80, dan 40 × 40, sedangkan kepala deteksi objek besar dihapus. Modul DFC-C3Ghost (GhostNetV2 dengan atensi *decoupled fully connected*) menggantikan sebagian modul C3 pada tulang punggung dan *neck* untuk menangkap dependensi jarak jauh dengan biaya komputasi rendah (kompleksitas atensi turun dari $O(H^2W^2)$ menjadi $O(H^2W + HW^2)$). Modul ELANB (*efficient layer aggregation network block*) menggantikan modul C3 asli untuk memperkaya aliran gradien. Pelatihan: masukan 640 × 640, laju belajar 0,01, *batch* 8, 200 *epoch*, pada RTX 2080 (8 GB), CUDA 11.3, PyTorch 1.10.0.

### 3. Pelacakan

Mengacu pada ByteTrack, kotak deteksi dibagi menjadi skor tinggi dan rendah. Trajektori awal dibuat pada bingkai pertama, lalu tiga tahap asosiasi dilakukan: pencocokan kotak skor tinggi dengan semua trajektori, pencocokan kotak skor rendah dengan trajektori yang belum cocok, dan pembuatan trajektori baru untuk kotak skor tinggi yang tidak cocok. Trajektori yang tidak cocok dipertahankan selama 60 bingkai agar dapat dicocokkan saat muncul kembali. Prediksi keadaan memakai filter Kalman dan pencocokan memakai algoritme Hungarian.

### 4. Metrik asosiasi DG-GM

DIoU dipakai sebagai gerbang: bila DIoU kurang dari ambang $\alpha = 0{,}34$ (dua kotak berjauhan), nilai IoU dipakai sebagai skor pencocokan, bila tidak, nilai GIoU dipakai. GIoU tetap memberi nilai ketika kotak tidak bertumpuk (misalnya akibat oklusi), sedangkan gerbang DIoU membatasi jarak sehingga dua leci yang berjauhan tidak diberi ID yang sama.

### 5. Strategi penghitungan AreaC

Penghitungan dilakukan dalam area di tengah bingkai yang mencakup 60% lebar horizontal dan 95% tinggi vertikal. Buah dihitung berdasarkan ID unik saat memasuki area itu. Strategi pembanding adalah *Cross Line* (garis hitung), yang menyebabkan banyak hitungan terlewat saat buah tertutup sebelum melintasi garis, dan *Full Count* (seluruh bingkai), yang menyebabkan penghitungan berulang karena buah di tepi bingkai berganti ID.

### 6. Penerapan pada perangkat tepi

Jetson AGX Xavier (CPU Carmel ARMv8.2 8 inti, GPU 32 TOPS) dipakai dengan kuantisasi TensorRT pada LitchiDet untuk membangun model format TRT.

## Eksperimen dan Hasil

Metrik deteksi: presisi, *recall*, AP, mAP (satu kelas), jumlah parameter, ukuran model, dan FPS. Metrik penghitungan: MAPE, *mean error* (ME, bertanda sehingga menunjukkan hitungan terlewat atau berulang), dan FPS, terhadap hitungan manual rerata lima orang.

Hasil yang terbaca pada narasi (isi Tabel I sampai VI tidak terbaca pada teks ekstraksi):

| Aspek | Hasil yang dilaporkan |
|---|---|
| Ablasi deteksi | Lapisan objek kecil meningkatkan kinerja secara substansial; ELANB menaikkan mAP 5,42% dan DFC-C3Ghost 5,11%; model akhir mAP naik 5,97% dan ukuran model berkurang 33,56% (FPS sedikit turun) |
| TensorRT | Kehilangan akurasi deteksi 0,25%; FPS deteksi citra naik sekitar 50,29% dan FPS penghitungan video naik sekitar 29,69% |
| Perbandingan detektor | mAP LitchiDet lebih tinggi 118,91% dan 122,13% dibanding Faster R-CNN dan Nanodet, dan melampaui YOLOv6, YOLOv7, dan YOLOv8; lebih cepat dari Faster R-CNN dan seri YOLO |
| Parameter gerbang | $\alpha = 0{,}34$ memberi hasil terbaik pada sepuluh kelompok bingkai kunci (lima oklusi, lima pergeseran ID) dan MAPE terendah |
| DG-GM dan FastReID | FastReID kurang lebih setara IoU; satu leci dengan ID awal 1023 mengalami 7 pergantian ID dalam 40 bingkai pada guncangan kamera; DG-GM lebih baik |
| Strategi hitung | MAPE Cross Line dan Full Count lebih tinggi daripada AreaC (terlewat vs berulang) |
| Pembanding DeepSORT | DeepSORT dengan Cross Line MAPE 49,79%; dengan AreaC 46,95%; LitchiCount MAPE 3,29% dengan kecepatan bingkai delapan kali lipat |

Metrik IoU, DIoU, CIoU, EIoU, dan GIoU diuji tanpa gerbang. Hasilnya menurut penulis: IoU memberi hitungan berulang, GIoU memberi hasil lebih akurat, dan metrik lain umumnya memberi hitungan lebih rendah karena rentang pencocokan melebar yang memicu pergeseran ID antarbuah.

## Kelebihan dan Keterbatasan

Keterbatasan yang dinyatakan penulis: metode efektif untuk oklusi jangka pendek tetapi masih bermasalah pada oklusi jangka panjang dan pada buah yang muncul kembali setelah keluar dari bingkai. Pada pohon dengan cabang dan daun jarang, buah di sisi seberang dapat sering masuk FOV sehingga terjadi penghitungan berulang. Penulis berencana menambahkan informasi kedalaman (*depth*) untuk memperbaiki identifikasi pada berbagai jarak.

Menurut pembacaan ringkasan ini, evaluasi penghitungan memakai video dengan durasi total 933 detik dari satu wilayah dan musim, dan jumlah video uji serta hitungan acuan per video tidak terbaca pada teks ekstraksi sehingga kemantapan statistik MAPE 3,29% tidak dapat dinilai. Pembandingan dengan DeepSORT memakai detektor dan strategi yang disebut berbeda dari sistem sendiri, sehingga selisih MAPE bercampur antara pengaruh detektor dan asosiasi. Pengaruh sudut pandang sisi pohon yang berbeda tidak dipisahkan dari pengaruh perpindahan kamera, dan identitas antar-sisi pohon hanya ditangani melalui pembatasan area hitung, bukan pencocokan eksplisit.

## Kaitan dengan Tinjauan main6

Makalah ini menangani buah yang terlihat lebih dari sekali pada video yang mengelilingi pohon dari beberapa sisi. Mekanismenya adalah pelacakan berdasarkan deteksi (Kalman, metrik DG-GM, Hungarian, penyimpanan trajektori 60 bingkai) dengan hitungan ID unik di area tengah bingkai (AreaC). Penulis menyebut masalah yang relevan secara langsung: buah di satu sisi pohon muncul kembali di tepi bingkai pada sudut lain dan menerima ID baru sehingga terhitung ulang. Masalah itu diredam, bukan diselesaikan, dan penulis mengakui hitungan berulang tetap muncul bila buah sisi seberang tampak melalui cabang yang jarang. Hitungan tidak dilaporkan per kelas (satu kelas leci). Acuan hitung adalah hitung manual dari video (rerata lima orang), bukan panen.

Yang dapat dipindahkan ke pencacahan tandan sawit multi-sisi: perancangan area hitung yang mengabaikan tepi bingkai, metrik asosiasi yang menahan pergeseran ID dengan gerbang jarak, dan evaluasi dengan ME bertanda untuk memisahkan hitungan terlewat dari hitungan berulang. Keterbatasannya adalah identitas antar-sisi tidak ditangani secara geometris, sehingga untuk sawit perlu mekanisme tambahan (misalnya informasi kedalaman, seperti yang direncanakan penulis).

## Poin untuk Sitasi

Kunci BibTeX untuk entri ini adalah `lu2025iot`.

Lu dkk. mengusulkan LitchiCount, metode pelacakan dan penghitungan leci dari video multi-sisi yang menggabungkan detektor ringan LitchiDet, metrik asosiasi DG-GM berbasis GIoU dengan gerbang DIoU ($\alpha = 0{,}34$), dan strategi penghitungan area AreaC, serta berjalan pada Jetson AGX Xavier dengan TensorRT. Penulis melaporkan MAPE penghitungan 3,29% terhadap hitungan manual, dibanding 49,79% dan 46,95% untuk metode berbasis DeepSORT dengan Cross Line dan AreaC.

Catatan verifikasi data: Angka MAPE 3,29% berasal dari kesimpulan, MAPE DeepSORT 49,79% dan 46,95% dari seksi VII-B-3, angka ablasi dan TensorRT dari seksi VII-A, dan data akuisisi dari seksi II. Isi Tabel I sampai VI tidak terbaca pada teks ekstraksi sehingga nilai absolut mAP, parameter, FPS, ME, dan MAPE per strategi tidak dapat diverifikasi; MAPE 3,29% tidak dapat dicocokkan dengan tabel. Jumlah video uji dan hitungan acuan per video tidak dilaporkan pada teks yang terbaca. Peningkatan 118,91% dan 122,13% dinyatakan sebagai peningkatan relatif oleh penulis dan tidak dihitung ulang. Makalah berbahasa Inggris. Teks daftar pustaka dan biografi penulis tidak dipakai.
