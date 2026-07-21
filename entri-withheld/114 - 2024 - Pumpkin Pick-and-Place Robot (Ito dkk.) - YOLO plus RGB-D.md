# 114 - Development of a Pumpkin Fruits Pick-and-Place Robot Using an RGB-D Camera and a YOLO Based Object Detection AI Model

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ito2024pumpkin` |
| Judul asli | Development of a Pumpkin Fruits Pick-and-Place Robot Using an RGB-D Camera and a YOLO Based Object Detection AI Model |
| Penulis | Liangliang Yang, Tomoki Noguchi, Yohei Hoshino |
| Tahun | 2024 |
| Venue | Computers and Electronics in Agriculture, vol. 227, artikel 109625 |
| Tema | YOLO plus RGB-D |

## Tautan Akses
- **DOI (penerbit):** https://doi.org/10.1016/j.compag.2024.109625
- **ScienceDirect:** https://www.sciencedirect.com/science/article/pii/S0168169924010160
- **Google Scholar:** https://scholar.google.com/scholar?q=Development%20of%20a%20Pumpkin%20Fruits%20Pick-and-Place%20Robot%20Using%20an%20RGB-D%20Camera%20and%20a%20YOLO%20Based%20Object%20Detection%20AI%20Model
- **Semantic Scholar:** https://www.semanticscholar.org/paper/Development-of-a-pumpkin-fruits-pick-and-place-an-a-Yang-Noguchi/647c2a91c65d91a64f7d1f506039bdf319357ae1

## Gambaran Umum

Makalah ini melaporkan pengembangan robot pemanen buah labu yang bekerja secara *pick-and-place* (mengambil objek dari satu posisi dan meletakkannya di posisi lain) di ladang terbuka. Sistem menggabungkan tiga bagian: kamera RGB-D (kamera yang menghasilkan citra warna sekaligus peta kedalaman per piksel) untuk menangkap posisi buah, model deteksi YOLO untuk mengenali buah pada citra warna, dan lengan robot kolaboratif yang dipasang di atas kendaraan beroda rantai (*crawler*) untuk menjangkau dan mengangkat buah. Penulis membandingkan lima versi YOLO — v2, v3, v5, v7, dan v8 — pada tugas deteksi buah labu, kemudian memilih model dengan kinerja terbaik untuk dipakai pada sistem penuh.

Kontribusi utama makalah bukan arsitektur deteksi baru, melainkan integrasi sistem: metode kalibrasi satu langkah (*one-shot calibration*) yang memetakan posisi buah dari koordinat kamera ke koordinat lengan robot tanpa prosedur kalibrasi berulang, serta pengujian rangkaian penuh di ladang labu sungguhan, bukan hanya di laboratorium. Menurut penulis, sistem mencapai tingkat deteksi buah di atas 99% dan tingkat keberhasilan pengambilan (*grasp*) di atas 90%, dengan kegagalan utama terjadi pada buah yang tertutup rapat oleh sulur tanaman.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Panen buah labu adalah pekerjaan fisik berat: satu buah dapat berbobot belasan kilogram, permukaan ladang tidak rata, dan buah sering separuh tertutup daun atau sulur. Di Jepang, populasi petani yang menua membuat pekerjaan seberat ini semakin sulit dipenuhi tenaga manusia, sehingga otomasi panen menjadi kebutuhan praktis, bukan sekadar topik riset akademik.

Riset deteksi buah berbasis YOLO yang dibahas pada bab-bab lain klaster ini banyak berfokus pada buah ringan seperti pada studi fusi RGB dan kedalaman dasar (bab [118](./118%20-%202019%20-%20Exploring%20RGB+Depth%20Fusion%20%28Ophoff%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)), yang cukup diambil dengan pengisap atau jari penggenggam ringan. Buah labu menuntut platform mekanis yang berbeda: lengan berdaya angkat besar dan tangan penggenggam yang menahan bobot serta permukaan buah yang licin dan melengkung. Selain itu, sebagian besar sistem panen robotik yang dilaporkan sebelumnya diuji pada barisan tanaman yang rapi di rumah kaca atau kebun terstruktur; ladang labu tidak memiliki keteraturan spasial semacam itu, sehingga posisi buah relatif terhadap lengan robot bervariasi jauh lebih besar antar-percobaan.

Variasi posisi ini membuat kalibrasi kamera-lengan menjadi masalah tersendiri. Prosedur kalibrasi konvensional pada robotika umumnya menuntut penggerakan lengan ke banyak titik acuan untuk menghitung transformasi koordinat antara kamera dan lengan, sebuah proses yang memakan waktu dan harus diulang setiap kali platform dipindahkan ke petak ladang baru. Masalah gabungan — deteksi buah yang andal pada kondisi lapangan yang bervariasi, kalibrasi yang cepat diulang, dan manipulasi buah berat — belum banyak dipecahkan secara terintegrasi dalam satu sistem sebelum makalah ini.

## Ide Utama

Gagasan inti makalah adalah menyusun jalur pemrosesan (*pipeline*) tunggal yang mengubah citra RGB-D menjadi perintah gerak lengan robot, dengan dua keputusan desain penting. Pertama, deteksi dua dimensi (2D) dan lokalisasi tiga dimensi (3D) dipisahkan: YOLO hanya bertugas menemukan kotak pembatas (*bounding box*) buah pada citra warna datar, sedangkan jarak kedalamannya diambil langsung dari piksel peta kedalaman yang sudah sejajar dengan piksel warna pada koordinat kotak yang sama. Kedua, transformasi dari koordinat kamera ke koordinat lengan robot disederhanakan menjadi satu prosedur kalibrasi tunggal, bukan kalibrasi multi-titik berulang, karena posisi kamera tetap terhadap pangkal lengan sepanjang operasi.

Dengan pemisahan ini, penggantian versi YOLO tidak mengubah bagian kalibrasi maupun kendali lengan; hanya kotak pembatas yang berubah nilainya. Struktur modular semacam ini memudahkan penulis membandingkan lima versi YOLO tanpa merombak seluruh sistem untuk tiap perbandingan.

## Cara Kerja Langkah demi Langkah

### Platform dan Perangkat Keras

Dasar robot adalah kendaraan beroda rantai (*crawler*) tipe pertanian (NC16A, Yanmar) yang dipakai sebagai penopang bergerak di ladang tidak rata. Di atas kendaraan ini dipasang lengan robot kolaboratif enam sumbu (UR10, Universal Robots), dan pada pangkal lengan dipasang kamera RGB-D (RealSense D455, Intel) yang menghadap ke arah kerja lengan. Penempatan kamera di pangkal lengan, bukan di ujung efektor, membuat posisi kamera relatif terhadap dasar lengan tetap konstan selama pengoperasian, sehingga transformasi koordinat antara keduanya hanya perlu dihitung satu kali. Pada ujung lengan dipasang tangan robot rancangan khusus untuk mencengkeram buah labu.

### Deteksi Buah dengan YOLO

Citra warna dari kamera RGB-D dilewatkan ke model deteksi objek untuk menemukan kotak pembatas setiap buah labu yang tampak. Penulis melatih dan menguji lima versi YOLO — YOLOv2, YOLOv3, YOLOv5, YOLOv7, dan YOLOv8 — pada citra ladang labu, lalu membandingkan kinerjanya untuk memilih satu model yang dipakai pada sistem lapangan penuh. Perbandingan lintas generasi ini relevan karena tiap versi mewarisi rumusan dasar "grid dan regresi langsung" yang pertama diperkenalkan pada YOLO generasi awal (bab [002](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)), tetapi berbeda pada kedalaman jaringan, mekanisme *anchor*, dan strategi pelatihan, sehingga akurasi dan kecepatannya juga berbeda pada tugas khusus ini.

### Dari Kotak 2D ke Koordinat 3D

Setiap kotak pembatas yang dihasilkan YOLO memiliki titik pusat pada koordinat piksel (u, v) di citra warna. Karena kamera RGB-D menghasilkan peta kedalaman yang sejajar pikselnya dengan citra warna, nilai kedalaman pada piksel (u, v) yang sama memberi jarak buah dari kamera. Ketiga nilai ini — posisi horizontal, posisi vertikal, dan jarak — kemudian diubah menjadi satu titik koordinat tiga dimensi pada kerangka acuan kamera, memakai parameter internal kamera (panjang fokus dan titik pusat optik) yang sudah diketahui dari pabrikan.

### Kalibrasi Kamera-Lengan Satu Langkah

Titik 3D pada kerangka kamera belum dapat langsung dipakai lengan robot, karena lengan bergerak dalam kerangka koordinatnya sendiri. Makalah mengusulkan metode kalibrasi satu langkah: alih-alih menggerakkan lengan ke banyak titik acuan seperti kalibrasi konvensional, hubungan antara kerangka kamera dan kerangka lengan dihitung dari satu pengukuran acuan tunggal, memanfaatkan posisi kamera yang tetap terhadap pangkal lengan. Transformasi ini berupa perkalian matriks rotasi dan translasi yang, begitu dihitung sekali, dipakai berulang untuk setiap buah yang terdeteksi selama operasi berlangsung.

Alur data dari citra sampai gerak lengan dapat diringkas sebagai berikut:

```
kamera RGB-D di pangkal lengan UR10 (posisi kamera tetap)

  citra RGB               peta depth (piksel sejajar RGB)
      |                             |
      v                             |
 +-----------+                      |
 | YOLO      |  kotak buah          |
 | (v2..v8)  |------+               |
 +-----------+      |               |
                     v               v
              pusat kotak (u,v) -> ambil nilai depth di (u,v)
                     |
                     v
         titik 3D kerangka kamera (Xc, Yc, Zc)
                     |
                     v
      kalibrasi satu-langkah kamera -> lengan (rotasi+translasi)
                     |
                     v
         titik 3D kerangka robot (Xr, Yr, Zr)
                     |
                     v
      kinematika balik UR10 -> gerak lengan -> tangan menggenggam
```

### Perencanaan dan Eksekusi Pengambilan

Titik 3D pada kerangka robot menjadi target bagi perhitungan kinematika balik (*inverse kinematics*): proses menghitung sudut tiap sendi lengan yang membuat ujung efektor mencapai posisi target tertentu. Setelah sudut sendi dihitung, lengan bergerak menuju posisi buah, tangan penggenggam menutup untuk mencengkeram buah, lengan mengangkat dan memindahkannya ke titik peletakan (misalnya bak penampung pada kendaraan), lalu siklus berulang untuk buah berikutnya yang terdeteksi.

## Eksperimen dan Hasil

Pengujian dilakukan pada citra ladang labu untuk tahap pelatihan/pembandingan model deteksi, dan pada uji lapangan langsung di ladang terbuka untuk tahap pengambilan fisik oleh robot. Pada tahap deteksi, kelima versi YOLO (v2, v3, v5, v7, v8) diuji pada kumpulan citra yang sama dan dibandingkan kinerjanya; penulis melaporkan bahwa salah satu versi lebih baru (YOLOv8 pada sebagian rangkuman sekunder yang tersedia) memberi kinerja deteksi terbaik dan dipakai pada sistem akhir. Pada tahap uji lapangan penuh, penulis melaporkan tingkat deteksi buah di atas 99% dan tingkat keberhasilan pengambilan fisik (*grasp*) di atas 90%.

Interpretasi kedua angka ini penting dibedakan: tingkat deteksi mengukur seberapa sering YOLO benar mengenali buah pada citra, sedangkan tingkat keberhasilan pengambilan mengukur seberapa sering seluruh rantai (deteksi, lokalisasi 3D, kalibrasi, dan gerak lengan-tangan) berhasil memindahkan buah tanpa gagal secara fisik. Selisih sekitar 9 poin antara keduanya konsisten dengan sumber kegagalan yang dilaporkan penulis: buah yang terdeteksi dengan benar pada citra tetap dapat gagal diambil bila permukaannya tertutup rapat oleh sulur tanaman, karena tangan penggenggam tidak memiliki jalur bebas untuk mencengkeram buah secara aman. Dengan kata lain, kegagalan sistem pada percobaan ini lebih banyak berasal dari keterbatasan mekanis penggenggaman di lapangan, bukan dari kesalahan deteksi visual.

Beberapa angka rinci lain — nilai *precision* per versi YOLO, metrik *mean Average Precision* (mAP, rata-rata presisi di seluruh kelas dan ambang deteksi), skor F1, serta waktu siklus pengambilan per buah — disebutkan pada sejumlah rangkuman sekunder tetapi tidak seragam antar-sumber dan tidak berhasil diverifikasi langsung dari naskah lengkap (artikel berada di balik akses berbayar penerbit). Angka-angka tersebut ditandai di bagian Poin untuk Sitasi dan sebaiknya dicocokkan dengan tabel hasil pada naskah asli sebelum dikutip.

## Kelebihan dan Keterbatasan

Kelebihan utama makalah terletak pada cakupan pengujiannya: sistem diuji sebagai satu kesatuan (deteksi, lokalisasi 3D, kalibrasi, dan manipulasi fisik) di ladang labu sungguhan, bukan hanya komponen deteksi di laboratorium. Perbandingan lima versi YOLO pada tugas yang sama juga memberi dasar empiris untuk memilih model, alih-alih mengasumsikan versi terbaru otomatis paling sesuai. Metode kalibrasi satu langkah menyederhanakan penyiapan lapangan dibandingkan kalibrasi multi-titik konvensional, yang relevan untuk platform bergerak yang berpindah petak secara rutin.

Dari sisi rekayasa, keterbatasan yang tampak adalah ketergantungan keberhasilan pengambilan pada kondisi lapangan yang cukup spesifik: kepadatan sulur, arah pertumbuhan tanaman, dan pencahayaan pada saat pengujian belum tentu mewakili seluruh musim tanam atau varietas labu lain. Secara konseptual, pemisahan deteksi 2D dan lokalisasi 3D memudahkan integrasi tetapi juga berarti sistem tidak memiliki mekanisme eksplisit untuk menangani oklusi struktural (buah tertutup sulur); perbaikan pada bagian deteksi saja tidak akan menaikkan tingkat keberhasilan pengambilan jika masalahnya terletak pada akses fisik tangan penggenggam. Ketergantungan pada platform crawler dan lengan kolaboratif berukuran industri juga membatasi kemudahan penerapan pada operasi berskala kecil atau ladang dengan lorong antar-baris yang sempit.

## Kaitan dengan Bab Lain

Bab ini merupakan salah satu contoh penerapan paling konkret dari klaster YOLO plus RGB-D untuk tugas manipulasi fisik, sejalan dengan bab [115](./115%20-%202025%20-%20YOLOv8-URE%202D+Point%20Cloud%20Grasping%20-%20YOLO%20plus%20RGB-D.md) yang juga menggabungkan deteksi 2D dan data kedalaman untuk perencanaan penggenggaman, serta bab [116](./116%20-%202023%20-%20Grasp%20via%20YOLO%20+%20RGB-D%20Fusion%20%28Tian%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md) yang mengangkat masalah serupa dari sudut fusi fitur deteksi dan kedalaman. Dibandingkan keduanya, bab ini menonjol pada sisi rekayasa sistem lapangan penuh (kendaraan, lengan, kalibrasi) alih-alih perbaikan arsitektur model.

Ketergantungan makalah pada keluarga YOLO menautkannya ke bab-bab fondasi Fondasi RGB, khususnya bab [002](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md) sebagai versi paling awal yang diuji, hingga versi-versi lebih baru yang tidak memiliki bab tersendiri dalam tinjauan ini (YOLOv5 dan YOLOv8). Karena tugas akhirnya adalah penggenggaman fisik, bab ini juga berkaitan dengan klaster Grasp Robotik, misalnya bab [081](./081%20-%202018%20-%20GG-CNN%20-%20Grasp%20Robotik.md) yang membahas sintesis penggenggaman secara langsung dari citra kedalaman tanpa deteksi objek eksplisit — kontras metodologis yang berguna untuk membandingkan dua pendekatan berbeda dalam memutuskan titik cengkeram.

## Poin untuk Sitasi

Kutip dengan kunci `ito2024pumpkin`. Ringkasan yang aman dikutip: "Yang, Noguchi, dan Hoshino (2024) mengembangkan robot panen labu berbasis deteksi YOLO dan kamera RGB-D pada kendaraan crawler dan lengan kolaboratif, dengan metode kalibrasi kamera-lengan satu langkah, dan melaporkan tingkat deteksi buah di atas 99% serta tingkat keberhasilan pengambilan fisik di atas 90% pada uji lapangan."

Butir yang belum terverifikasi langsung dari naskah lengkap (akses berbayar) dan perlu dicocokkan sebelum dikutip formal: versi YOLO mana persis yang terpilih sebagai model terbaik pada sistem akhir; nilai *precision*, mAP, dan skor F1 per versi YOLO; waktu siklus pengambilan per buah; jumlah dan komposisi citra pada kumpulan data pelatihan; serta rincian desain tangan penggenggam (jumlah jari, rentang gaya cengkeram).
