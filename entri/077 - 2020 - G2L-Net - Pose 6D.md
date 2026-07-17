# 077 - G2L-Net: Global to Local Network for Real-Time 6D Pose Estimation with Embedding Vector Features

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2020g2lnet` |
| Judul asli | G2L-Net: Global to Local Network for Real-Time 6D Pose Estimation with Embedding Vector Features |
| Penulis | Wei Chen, Xi Jia, Hyung Jin Chang, Jinming Duan, Ales Leonardis |
| Tahun | 2020 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2020) |
| Tema | Pose 6D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2003.11089
- **CVF Open Access:** https://openaccess.thecvf.com/content_CVPR_2020/html/Chen_G2L-Net_Global_to_Local_Network_for_Real-Time_6D_Pose_Estimation_CVPR_2020_paper.html
- **Kode sumber:** https://github.com/DC1991/G2L_Net
- **Google Scholar:** https://scholar.google.com/scholar?q=G2L-Net%3A%20Global%20to%20Local%20Network%20for%20Real-Time%206D%20Pose%20Estimation

## Gambaran Umum

Makalah ini memperkenalkan G2L-Net (*Global to Local Network*), kerangka estimasi pose 6D *real-time* yang bekerja pada *point cloud* (himpunan titik 3D) hasil pindaian kamera RGB-D. Pose 6D adalah gabungan tiga parameter translasi dan tiga parameter rotasi yang menyatakan posisi dan orientasi objek relatif terhadap kamera; nilai ini diperlukan robot untuk mencengkeram atau memanipulasi benda. Masalah yang dipecahkan adalah bagaimana mengestimasi pose secara akurat sekaligus cukup cepat untuk penggunaan praktis, dua sifat yang sulit dicapai bersamaan karena memproses seluruh ruang 3D adegan mahal secara komputasi.

Gagasan intinya adalah strategi *divide-and-conquer* dari kasar ke halus: objek dilokalisasi secara global terlebih dahulu untuk memangkas ruang pencarian, kemudian *point cloud* objek dipindahkan ke sistem koordinat lokal dan pose halusnya diprediksi bertahap. Untuk rotasi, makalah mengusulkan *point-wise embedding vector features* (fitur vektor tanam per-titik) yang menangkap informasi sudut pandang, dan *rotation residual estimator* (penaksir sisa rotasi) yang mengoreksi rotasi awal. Pada tolok ukur LineMOD dan YCB-Video, G2L-Net melaporkan akurasi setara metode terbaik saat itu sambil berjalan di atas 20 *frame* per detik (FPS).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi pose 6D berbasis RGB-D pada saat makalah ini terbit didominasi dua garis pendekatan. Garis pertama, diwakili DenseFusion (bab 074), menggabungkan fitur warna dan geometri per-titik lalu meregresi pose secara padat; pendekatan ini akurat tetapi bergantung pada penyempurnaan iteratif yang menambah waktu komputasi. Garis kedua, diwakili PVN3D (bab 075), memakai *voting* keypoint 3D — setiap titik memberi suara untuk lokasi titik penanda objek — yang akurat tetapi berat karena setiap titik ikut memilih di seluruh adegan.

Masalah yang menyatukan kedua garis tersebut adalah biaya pemrosesan ruang 3D. Bila jaringan harus menilai seluruh titik adegan, sebagian besar komputasi terbuang pada latar belakang dan permukaan yang tidak relevan. Selain itu, rotasi jauh lebih sukar diprediksi daripada translasi: translasi cukup dinyatakan sebagai pergeseran tiga sumbu, sedangkan rotasi menempati ruang parameter yang tidak linear sehingga regresi langsung sering kurang tepat. Oklusi — objek yang terhalang sebagian oleh benda lain — memperburuk keduanya karena mengurangi jumlah titik yang teramati. G2L-Net menargetkan ketiga hambatan ini: mempersempit ruang pencarian, memisahkan translasi dari rotasi, dan memperkaya representasi rotasi.

## Ide Utama

Inti G2L-Net adalah memecah estimasi pose menjadi rangkaian submasalah yang masing-masing lebih mudah, alih-alih meregresi pose lengkap sekaligus. Alur berpindah dari lingkup global (seluruh adegan) ke lingkup lokal (kerangka koordinat objek), sehingga namanya *global to local*.

Pada lingkup global, detektor 2D pada citra RGB-D menandai wilayah objek, dan hanya *point cloud* di dalam wilayah itu yang diteruskan. Alih-alih memakai *frustum* (kerucut pandang yang memanjang searah kedalaman) seperti pendahulunya, G2L-Net membatasi titik objek di dalam sebuah bola 3D (*3D sphere*), yang menutup ruang pencarian menjadi lebih ringkas. Pada lingkup lokal, *point cloud* objek dipindahkan ke pusat koordinatnya sendiri, lalu translasi dan rotasi diprediksi terpisah. Untuk rotasi, setiap titik tidak hanya menyumbang fitur global, melainkan menghasilkan *embedding vector* yang mengkodekan sudut pandang objek, dan sebuah modul tambahan memperkirakan selisih antara rotasi awal dan rotasi sebenarnya.

## Cara Kerja Langkah demi Langkah

G2L-Net terdiri atas tiga subjaringan berurutan: lokalisasi global, lokalisasi translasi, dan lokalisasi rotasi. Diagram berikut merangkum aliran datanya.

```
citra RGB-D
     │
     ▼
┌──────────────────┐   deteksi 2D + bola 3D
│ lokalisasi global│──────────────────────►  point cloud objek (kasar)
└──────────────────┘
     │
     ▼
┌──────────────────┐   segmentasi 3D + translasi
│ lokalisasi       │──────────────────────►  titik objek terpilih,
│ translasi        │                          dipindah ke koordinat lokal
└──────────────────┘
     │
     ▼
┌──────────────────┐   embedding vector + sisa rotasi
│ lokalisasi rotasi│──────────────────────►  pose 6D (R, t)
└──────────────────┘
```

### Lokalisasi Global

Tahap ini mengubah citra RGB-D menjadi *point cloud* objek yang kasar. Detektor objek 2D memberi kotak pembatas pada citra warna; piksel di dalam kotak, dipadukan dengan peta kedalaman, diproyeksikan menjadi titik 3D. G2L-Net kemudian membatasi titik-titik ini dalam sebuah bola 3D alih-alih *frustum*. Bola membatasi jangkauan sepanjang sumbu kedalaman, yang pada *frustum* justru melebar semakin jauh dari kamera; ruang pencarian yang lebih ringkas berarti lebih sedikit titik latar yang harus diproses tahap berikutnya.

### Lokalisasi Translasi

*Point cloud* kasar masih memuat titik latar di sekitar objek. Subjaringan translasi melakukan dua hal sekaligus: segmentasi 3D, yaitu memilih titik mana yang benar milik objek, dan prediksi translasi, yaitu memperkirakan koordinat pusat objek. Arsitekturnya mengikuti gaya PointNet — jaringan yang memproses himpunan titik tak berurut dengan berbagi bobot antar-titik lalu menggabungkannya dengan operasi simetris seperti *max pooling*. Setelah pusat objek diketahui, seluruh titik objek dipindahkan sehingga pusatnya menjadi titik asal koordinat. Pemindahan ini melepaskan tahap rotasi dari pengaruh translasi: jaringan rotasi hanya perlu menilai bentuk dan orientasi, bukan lokasi.

### Lokalisasi Rotasi

Tahap ini adalah kontribusi utama makalah dan menyimpan dua komponen. Yang pertama, *point-wise embedding vector features*. Alih-alih meringkas seluruh objek menjadi satu vektor fitur global melalui *pooling* — yang membuang informasi per-titik — setiap titik menghasilkan vektor tanam yang mengodekan informasi sadar sudut pandang (*viewpoint-aware*), yaitu petunjuk dari sisi mana objek sedang dilihat. Representasi per-titik ini mempertahankan detail arah yang penting untuk rotasi dan lebih tahan terhadap oklusi karena tidak bergantung pada satu ringkasan tunggal.

Komponen kedua adalah *rotation residual estimator*. Dari fitur di atas, jaringan menghasilkan rotasi awal, lalu modul terpisah memperkirakan *residual* — selisih antara rotasi awal dan rotasi kebenaran — dan menambahkannya sebagai koreksi. Memprediksi selisih kecil lebih mudah dipelajari daripada memprediksi rotasi penuh dari nol, sehingga langkah ini menaikkan ketepatan tanpa penyempurnaan iteratif yang mahal. Gabungan rotasi terkoreksi dan translasi dari tahap sebelumnya membentuk pose 6D akhir.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua tolok ukur standar. LineMOD memuat 13 objek tunggal di atas latar berantakan, sedangkan YCB-Video memuat 21 objek dalam adegan dengan banyak benda dan oklusi. Metrik utamanya adalah ADD dan ADD-S: ADD (*Average Distance*) mengukur rata-rata jarak antara titik model pada pose prediksi dan pose kebenaran, sedangkan ADD-S adalah varian untuk objek simetris yang memakai jarak ke titik terdekat agar simetri tidak dihukum keliru. Pose dianggap benar bila jarak tersebut berada di bawah ambang tertentu (lazimnya 10% diameter objek); pada YCB-Video hasil juga dilaporkan sebagai AUC (*Area Under the Curve*), luas di bawah kurva akurasi terhadap ambang.

Pada LineMOD, G2L-Net melaporkan rata-rata ADD(-S) sekitar 98,7%, lebih tinggi daripada DenseFusion yang berbasis fusi padat iteratif. Interpretasinya: dari 13 objek, hampir seluruh estimasi jatuh dalam ambang benar, dan capaian ini diperoleh tanpa langkah penyempurnaan iteratif. Pada YCB-Video, G2L-Net melaporkan AUC ADD-S sekitar 92,3%, setara atau sedikit di atas DenseFusion versi non-iteratif pada metrik yang sama — bukti bahwa strategi global-ke-lokal tetap kompetitif pada adegan berantakan dengan oklusi. Dari sisi kecepatan, seluruh pipeline berjalan di atas 20 FPS (dilaporkan sekitar 23 FPS), yang memenuhi syarat *real-time* untuk banyak aplikasi robotika, berbeda dari metode akurat lain yang melambat akibat iterasi.

Makalah juga menyertakan *ablation study* (uji melepas komponen satu per satu) yang menambahkan bola 3D, *embedding vector features*, dan *rotation residual estimator* secara bertahap. Akurasi naik pada setiap penambahan hingga mencapai angka penuh, yang menunjukkan ketiga komponen berkontribusi nyata, bukan sekadar hiasan arsitektur.

## Kelebihan dan Keterbatasan

Kelebihan utama G2L-Net adalah keseimbangan akurasi dan kecepatan: akurasi setara metode terbaik saat itu pada laju *real-time*, dicapai lewat pemisahan tegas antara translasi dan rotasi serta perampingan ruang pencarian. Representasi *embedding vector* per-titik memberi ketahanan terhadap oklusi, dan penaksir sisa rotasi menaikkan ketepatan tanpa iterasi.

Keterbatasannya sebagian bersifat struktural. Karena tahap lokal bergantung penuh pada keluaran tahap global, galat pada deteksi 2D atau pembatasan bola 3D merambat ke bawah tanpa mekanisme koreksi balik; secara konseptual, arsitektur berantai seperti ini rentan terhadap kegagalan tahap awal. Dari sisi rekayasa, metode ini mensyaratkan masukan RGB-D berkualitas — *point cloud* yang tipis akibat permukaan mengilap atau kedalaman yang bising akan menurunkan kinerja tahap translasi dan rotasi. Metode ini juga berorientasi objek dengan model 3D yang diketahui pada level instans, sehingga generalisasi ke objek baru tanpa model tidak dibahas.

## Kaitan dengan Bab Lain

Bab ini berdiri dalam silsilah pose 6D RGB-D yang bermula dari PoseCNN (bab 073), yang meletakkan formulasi memisahkan estimasi translasi dan rotasi dari citra. G2L-Net mewarisi prinsip pemisahan itu dan membawanya ke ranah *point cloud*. Terhadap [DenseFusion (bab 074)](./074%20-%202019%20-%20DenseFusion%20-%20Pose%206D.md), yang menjadi pembanding langsung, G2L-Net menawarkan alternatif tanpa penyempurnaan iteratif: bila DenseFusion menggabungkan fitur warna-geometri secara padat lalu menyempurnakan pose berulang, G2L-Net justru mempersempit ruang lebih dahulu dan mengoreksi rotasi sekali lewat penaksir sisa. Terhadap [PVN3D (bab 075)](./075%20-%202020%20-%20PVN3D%20-%20Pose%206D.md) yang mengandalkan *voting* keypoint 3D, G2L-Net memilih regresi bertahap yang lebih ringan secara komputasi. Garis efisiensi ini berlanjut ke [FFB6D (bab 076)](./076%20-%202021%20-%20FFB6D%20-%20Pose%206D.md), yang menyatukan fusi dua arah RGB dan kedalaman, serta bermuara pada pergeseran paradigma di [FoundationPose (bab 078)](./078%20-%202024%20-%20FoundationPose%20-%20Pose%206D.md) yang menargetkan objek tanpa pelatihan ulang. Ringkasan lanskap ini tersedia pada [Review Pose 6D (bab 079)](./079%20-%202021%20-%20Review%20Pose%206D%20%26%20Deteksi%203D%20%28Hoque%20dkk.%29%20-%20Pose%206D.md).

## Poin untuk Sitasi

Kutip dengan kunci `chen2020g2lnet`. Ringkasan yang aman dikutip: "G2L-Net mengestimasi pose 6D dari RGB-D secara *real-time* melalui strategi global-ke-lokal — lokalisasi global dengan bola 3D, lokalisasi translasi, dan lokalisasi rotasi memakai *point-wise embedding vector features* serta *rotation residual estimator* — mencapai akurasi setara metode terbaik pada LineMOD dan YCB-Video di atas 20 FPS." Angka spesifik (LineMOD ADD(-S) ±98,7%, YCB-Video AUC ADD-S ±92,3%, laju ±23 FPS) berasal dari ringkasan sumber sekunder dan abstrak; nilai tepat, selisih terhadap DenseFusion, serta rincian waktu per-komponen sebaiknya diverifikasi ke tabel naskah CVF sebelum dikutip dalam karya formal. Jumlah objek LineMOD (13) dan YCB-Video (21) adalah properti dataset yang baku.
