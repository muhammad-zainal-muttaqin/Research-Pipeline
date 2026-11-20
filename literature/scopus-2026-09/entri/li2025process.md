# Process, challenges and solutions of fruit 3D reconstruction: A review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `li2025process` |
| Judul asli | Process, challenges and solutions of fruit 3D reconstruction: A review |
| Penulis | Li, Zetong; Xu, Xufeng; Xu, Tao; Gao, Yuan; Rao, Xiuqin |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | R (Tinjauan terdahulu) |

## Tautan Akses
- PDF: [li2025process.pdf](../pdf/li2025process.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2025.111068

## Gambaran Umum

Li dkk. (2025) adalah tinjauan sistematis tentang rekonstruksi tiga dimensi (3D) untuk buah, baik di kebun maupun di industri pascapanen, yang terbit di *Computers and Electronics in Agriculture* 239 (2025) 111068. Tinjauan ini tidak menghitung buah sendiri. Ia memetakan cara memperoleh model 3D buah dengan sensor aktif, seperti triangulasi laser, *time-of-flight*, dan *structured light*, serta dengan sensor pasif, seperti *stereo vision* dan *multi-view stereo*, lalu membahas rekonstruksi berbasis pembelajaran mesin.

Bagian klasik membahas dua tahap: akuisisi citra dan pemrosesan hingga menjadi model. Bagian pembelajaran dibagi menjadi rekonstruksi dari satu tampilan (*single-view*), yang menghasilkan keluaran berupa voksel, *point cloud*, atau mesh, dan rekonstruksi dari banyak tampilan (*multi-view*), termasuk *multi-view depth map*, NeRF (*neural radiance field*, model yang mempelajari warna dan kepadatan di setiap titik ruang dari kumpulan foto), dan *3D Gaussian splatting* (3DGS, yang memodelkan adegan sebagai kumpulan elipsoid Gaussian). Tinjauan membagi aplikasi menjadi dua kebutuhan: persepsi online real-time untuk pemanenan robotik, dan analisis offline presisi tinggi untuk fenomika, yaitu pengukuran sifat tanaman secara rinci.

Tabel ringkasan dalam tinjauan memuat beberapa kajian penghitungan buah berbasis NeRF. Kelly dkk. (2023) pada jeruk memakai instant-ngp dan YOLOv8 dengan MAE 1,5 dan akurasi 90,62%. Liu dkk. (2024) pada apel memakai FruitNeRF dengan F1 0,95 pada data sintetis yang memiliki mask ground-truth, dan tingkat deteksi di atas 89% pada data apel nyata. Zhou dkk. (2024) melaporkan kenaikan mAP50 sebesar 44,8% untuk AgriNeRF pada deteksi apel dan persik dalam pencahayaan ekstrem. Wang dkk. (2024f) melaporkan AP 76,3% untuk FF3D, dan Meyer dkk. (2024) memakai Tomato-NeRF. Angka-angka ini berasal dari data, metrik, dan protokol yang berbeda, sehingga tidak dapat langsung dibandingkan, dan tinjauan tidak menyatukannya.

Tinjauan juga mencatat peran sensor kedalaman untuk lokalisasi dan pengukuran. Neupane dkk. (2021) membandingkan delapan kamera kedalaman untuk lokalisasi mangga. Zhang dkk. (2020) melaporkan korelasi LS-SVM 0,90 untuk volume dan 0,86 untuk berat apel. Kesimpulan tinjauan menyebut dua agenda. Untuk persepsi online, tantangannya adalah rekonstruksi otonom yang kuat di kebun kompleks, integrasi multi-sensor, dan pengurangan beban komputasi (*lightweighting*) pada perangkat tertanam. Untuk analisis offline, fokusnya adalah fidelitas model dan efisiensi, dengan arah lanjutan berupa 4D, integrasi citra hiperspektral, termal, dan CT, serta biaya pelatihan NeRF yang tinggi.

Untuk kajian ini, kode R berarti tinjauan terdahulu tentang pencitraan dan rekonstruksi buah, bukan bukti penghitungan. Batasnya: bagian metode dan hasil asli penulis tidak dibaca penuh. Yang dibaca adalah pendahuluan, tabel ringkasan, dan kesimpulan. Angka dikutip sebagaimana dilaporkan tinjauan dan belum diverifikasi ke makalah asli.
