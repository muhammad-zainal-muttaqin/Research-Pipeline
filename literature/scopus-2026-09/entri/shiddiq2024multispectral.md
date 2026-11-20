# Multispectral imaging and deep learning for oil palm fruit bunch ripeness detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `shiddiq2024multispectral` |
| Judul asli | Multispectral imaging and deep learning for oil palm fruit bunch ripeness detection |
| Penulis | Shiddiq, Minarni; Saktioto, Saktioto; Salambue, Roni; Wardana, Fiqra; Dasta, Vicky Vernando; Harmailil, Ihsan Okta; Rabin, Mohammed Fisal; Arpyanti, Nisa; Wahyudi, Dilham |
| Tahun | 2024 |
| Venue | Bulletin of Electrical Engineering and Informatics |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [shiddiq2024multispectral.pdf](../pdf/shiddiq2024multispectral.pdf)
- DOI resmi: https://doi.org/10.11591/eei.v13i6.8120

## Gambaran Umum

Sortir dan penilaian mutu tandan buah segar (TBS) di pabrik masih mengandalkan grader berpengalaman, sehingga rentan terhadap subjektivitas, kerusakan buah, dan waktu kerja panjang. Kajian pencitraan sebelumnya memakai kamera warna pada panjang gelombang tampak dan tandan diam, baik di pohon maupun di tanah. Penelitian ini bertujuan membangun sistem pencitraan multispektral berbasis LED yang dikombinasikan dengan pembelajaran mendalam untuk mendeteksi kematangan TBS secara cepat dan real time pada konveyor yang bergerak.

Sampel adalah TBS kelapa sawit Tenera dari dua perkebunan, yaitu PTPN V Pekanbaru, Riau, dan perkebunan swasta atau petani kecil, dengan dua kelas kematangan, unripe dan ripe; tingkat overripe (fraksi F4) dimasukkan ke dalam kelas ripe karena warnanya serupa. Grader bersertifikat memvalidasi kematangan berdasarkan warna kulit dan mesokarp serta jumlah buah lepas. Sistem terdiri atas konveyor berantai, portal optik dengan perisai hitam, pemisah pneumatik, Arduino UNO, sensor kedekatan, dan kamera monokrom Sentech NIR CMOS 2,2 MP (2048×1088 piksel, 167 FPS) dengan lensa Navitar 12 mm F/1.4. Larik LED berbentuk donat memuat 32 LED pita sempit pada delapan panjang gelombang, yaitu 680, 700, 750, 780, 810, 850, 880, dan 900 nm, yang dapat dinyalakan satu per satu atau seluruhnya. Percobaan pertama mengukur intensitas reflektansi pada 15 tandan unripe dan 15 tandan ripe, menghasilkan 60 citra dari dua sisi dan delapan panjang gelombang, dengan kalibrasi referensi putih dan gelap serta ROI 614×326 piksel; kandungan minyak (OC) dan asam lemak bebas (FFA) diukur dengan ekstraksi Soxhlet. Percobaan kedua membangun dataset 2000 citra multispektral, terdiri atas 1000 unripe dan 1000 ripe, yang berasal dari 356 citra ripe dan 176 citra unripe dengan larik LED serta 644 citra ripe dan 824 citra unripe dari percobaan lensa filter halogen sebelumnya.

Mekanisme deteksi memakai YOLOv4-tiny dua kelas. Anotasi dengan LabelImg menghasilkan kotak pembatas dan label kelas, dengan kelas 0 untuk ripe dan 1 untuk unripe. Konfigurasi model memakai 6000 iterasi, batch 64, subdivisi 16, ukuran 416×416, dua kelas, dan 21 filter; pelatihan memakai bobot awalYOLOv4-tiny melalui transfer learning di Google Colab Pro. Dataset dibagi menjadi 1520 citra latih, 380 citra uji, dan 100 citra validasi. Kotak pembatas pada hasil deteksi menampilkan kelas kematangan dan nilai kepercayaan. Pengujian real time memakai dua video berisi 30 tandan yang bergerak di konveyor, 15 per kelas, dengan seluruh LED menyala. Secara fisik, tandan ripe memantulkan cahaya 7,75% lebih tinggi daripada tandan unripe pada setiap panjang gelombang, dengan kenaikan tajam pada 750–900 nm kecuali 780 nm dan 880 nm; OC ripe berkisar 16–28% dan unripe 0,5–15%.

Metrik yang dihitung adalah confusion matrix, presisi, recall, F1-score, AP, mAP pada IoU 0,50 dan 0,70, serta IoU, memakai paket scikit-learn pada Python. Pelatihan mencapai mAP 99,7% pada iterasi ke-6000 dengan loss rata-rata 0,0479. Pada 380 citra uji (190 per kelas), AP ripe 99,55% dan unripe 99,40%, mAP@0,50 99,47%, mAP@0,70 81,01%, presisi 0,92 dan 0,88, recall 0,99 untuk kedua kelas, serta F1 0,95 dan 0,93. Validasi pada 100 citra diam menghasilkan mAP@0,50 98,60% dan mAP@0,70 81,71%; validasi pada video 30 tandan menghasilkan AP 99,69% untuk ripe dan 99,62% untuk unripe, IoU 79,59%, mAP@0,50 99,66%, laju 2,99–3,88 FPS, dan durasi rata-rata 2 detik per tandan. Abstrak penulis menyebut akurasi rata-rata 99,66% dan kecepatan 3,32–3,62 FPS.

Penulis menyatakan sejumlah batasan. Kinerja kelas unripe lebih rendah daripada ripe, terutama presisi 0,88 karena FP sebanyak 26, yang dikaitkan dengan perbedaan tekstur citra sisi depan dan belakang. Variasi akurasi pada kelas ripe lebih besar karena variasi warna under-ripe, ripe, dan overripe, ukuran tandan, serta pencahayaan; hal ini memengaruhi ambang NMS, sedangkan ketidakkonsistenan anotasi memengaruhi IoU. Pada video muncul FP dan FN yang penulis kaitkan dengan overfitting serta pencahayaan LED yang tidak merata akibat pantulan pelat konveyor, sehingga presisi, recall, dan F1 turun dibandingkan citra diam. Beberapa citra validasi berakurasi rendah, misalnya ripe 0,49 karena intensitasnya menyerupai unripe dan unripe 0,74 karena bagian pangkal lebih terang. Nilai FFA sedikit di atas baku 5%, kemungkinan karena jeda waktu antara pemanenan, pemindaian, dan ekstraksi Soxhlet. Penulis mengarahkan pekerjaan berikutnya pada deteksi TBS cacat dan klasifikasi dengan sistem LED yang diperbaiki serta ANN.
