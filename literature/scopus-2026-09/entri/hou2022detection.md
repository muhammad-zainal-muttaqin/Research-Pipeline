# Detection and localization of citrus fruit based on improved You Only Look Once v5s and binocular vision in the orchard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `hou2022detection` |
| Judul asli | Detection and localization of citrus fruit based on improved You Only Look Once v5s and binocular vision in the orchard |
| Penulis | Hou, Chaojun; Zhang, Xiaodi; Tang, Yu; Zhuang, Jiajun; Tan, Zhiping; Huang, Huasheng; Chen, Weilin; Wei, Sheng; He, Yong; Luo, Shaoming |
| Tahun | 2022 |
| Venue | Frontiers in Plant Science |
| Kode | C5 (Depth, 3D, dan non-RGB) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [hou2022detection.pdf](../pdf/hou2022detection.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2022.972445

## Gambaran Umum

Penelitian ini mengatasi deteksi dan pelokalan buah jeruk matang untuk robot pemanen otomatis. Dua hambatan utama adalah pencahayaan yang berubah dan beragam kondisi penutupan buah, yang menurunkan akurasi deteksi maupun pelokalan. Penulis mencatat bahwa deteksi berbasis pembelajaran mendalam sering memburuk pada lingkungan tumbuh tidak terstruktur, sementara peta kedalaman dari kamera stereo bersifat jarang karena keterbatasan kamera, sudut pengambilan, dan penutupan oleh daun, ranting, atau buah tetangga. Tujuan penelitian ini adalah menghapus nilai kedalaman yang hilang agar posisi tiga dimensi buah dapat diperoleh secara akurat di kebun alami.

Data dikumpulkan dari jeruk kultivar Shantanju di kebun bukit Guangzhou Conghua Hualong Fruit and Vegetable Freshness Co. Ltd., Guangzhou, Tiongkok (113°39′2,38″ BT, 23°33′12,48″ LU). Sebanyak 4.485 kelompok citra diambil pada Desember 2020 dan Desember 2021 sebelum panen memakai kamera binokular ZED 2 beresolusi 1920 × 1080 pada kondisi cerah dan berawan, dengan jarak kamera ke buah sekitar 30–150 cm. Setiap kelompok memuat tampilan kiri (RGB) dan peta kedalaman; tampilan kanan hanya dipakai untuk membentuk peta kedalaman. Citra dibagi menjadi tiga kelas pencahayaan, yaitu tidak seragam, lemah, dan baik, dengan rincian 2.913 citra latih (11.088 sampel), 971 citra validasi (3.880 sampel), dan 971 citra uji (2.599 sampel). Buah di dekat tengah citra diberi kotak pembatas secara manual dengan Labelme.

Mekanisme terdiri atas tiga tahap. Pertama, YOLO v5s dimodifikasi dengan fungsi rugi *polarity binary cross-entropy with logit loss* (LossPB) untuk menghitung rugi probabilitas kelas dan skor keberadaan objek. Fungsi penalti fp mempeluas selisih antara probabilitas kelas benar dan salah sehingga memberi hukuman besar pada deteksi yang terlewat maupun deteksi palsu; parameter λ ditetapkan 20, laju pembelajaran 0,0032, ukuran kumpulan 32, ambang IoU 0,5, 200 epoch, dan masukan diubah menjadi 640 × 640 dengan bobot awal dari COCO. Kedua, dari kotak pembatas hasil deteksi, daerah buah diekstrak memakai pemetaan kromatik Cr-Cb, ambang batas Otsu, serta operasi morfologi erosi, dilatasi, pengisian lubang, dan *convex hull* untuk menutup bagian yang tersembunyi. Nilai kedalaman yang hilang dipulihkan dengan metode kriging, yang merupakan penaksir linier tak bias terbaik berdasarkan kedekatan spasial dan susunan nilai teramati. Ketiga, posisi tiga dimensi dihitung dari model pencitraan kamera dan ciri geometri buah, menghasilkan diameter dx, dy, dz, koordinat pusat Q0, jarak ke kamera d, serta kotak pembatas tiga dimensi berdelapan titik; dz ditaksir dari regresi polinomial kuadrat terhadap dx dan dy karena buah jeruk menyerupai elipsoid.

Metrik deteksi adalah recall, presisi, dan skor-F1 dihitung dari matriks kebingungan. Pada himpunan uji, LossPB menghasilkan recall 99,55% untuk pencahayaan tidak seragam, 98,47% untuk pencahayaan lemah, dan 98,48% untuk pencahayaan baik, dengan presisi berturut-turut 95,79%, 96,13%, dan 96,64% serta F1 mendekati 0,98. Secara keseluruhan recall 98,85%, presisi 96,22%, F1 0,98, dan waktu deteksi rata-rata 78,96 ms per citra, lebih tinggi sekitar 2–9 poin persentase daripada YOLO v5s awal. Uji pemulihan kedalaman dengan sekitar 50% piksel sengaja dihilangkan memberi galat pemulihan rata-rata 2,21 mm dan galat relatif 1,36%; bagian artikel simpulan mencantumkan angka sedikit berbeda, 2,02 mm dan 1,26%. Model regresi dz berdasarkan 137 buah yang diukur dengan jangka sorong menghasilkan RMSE 4,51 mm dan R² 0,940. Pada 22 citra yang diukur dengan penggaris laser dan jangka sorong, galat rata-rata jarak ke kamera 3,98 mm serta galat diameter dx, dy, dz berturut-turut 2,75 mm, 2,52 mm, dan 2,11 mm.

Batasan yang dinyatakan penulis mencakup ketergantungan metode pada kualitas kamera stereo dan kondisi pencahayaan, karena peta kedalaman dapat kosong pada lebih dari separuh luas daerah buah. Deteksi difokuskan pada buah yang berada di dekat tengah citra, sehingga pelokalan untuk buah di tepi citra tidak dievaluasi. Fungsi rugi diuji hanya pada YOLO v5s dan tiga kondisi pencahayaan dalam satu kultivar jeruk; penulis menyatakan generalisasi ke kebun lain belum diperiksa. Pemulihan kedalaman memberi galat lebih besar pada bagian peta yang paling tidak kontinu. Penelitian lanjutan yang diusulkan adalah pembelajaran sedikit contoh (*few-shot learning*) untuk mengurangi jumlah citra latih. Data dan kode tersedia di repositori publik yang disebutkan penulis.

