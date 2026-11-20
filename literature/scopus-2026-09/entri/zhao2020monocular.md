# Monocular depth estimation based on deep learning: An overview

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhao2020monocular` |
| Judul asli | Monocular depth estimation based on deep learning: An overview |
| Penulis | Zhao, ChaoQiang; Sun, QiYu; Zhang, ChongZhen; Tang, Yang; Qian, Feng |
| Tahun | 2020 |
| Venue | Science China Technological Sciences |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [zhao2020monocular.pdf](../pdf/zhao2020monocular.pdf)
- DOI resmi: https://doi.org/10.1007/s11431-020-1582-8

## Gambaran Umum

Tinjauan ini membahas estimasi kedalaman monokular berbasis pembelajaran mendalam, yaitu memperkirakan peta kedalaman padat dari satu citra. Penulis menyatakan masalah ini bersifat *ill-posed* karena satu citra tidak menyediakan korespondensi antarpandang. Metode geometris seperti *structure from motion* dan pencocokan stereo menghasilkan kedalaman hanya pada titik fitur yang jarang, bergantung pada citra berpasangan atau sekuens, serta mengalami ambiguitas skala pada SfM. Sensor kedalaman seperti kamera RGB-D dan LiDAR memang memberi kedalaman langsung, tetapi memiliki jangkauan terbatas, sensitivitas terhadap cahaya matahari, ukuran besar, dan konsumsi daya tinggi, sehingga kurang cocok untuk robot berukuran kecil.

Karena berupa tinjauan, makalah ini tidak memakai satu tanaman atau data percobaan sendiri, melainkan merangkum dataset dan metode yang umum dipakai. Empat dataset dibahas: KITTI (56 adegan, 28 untuk latih dan 28 untuk uji, pasangan stereo 1224×368, kebenaran dasar kedalaman jarang dari LiDAR), NYU Depth (464 adegan dalam ruangan, 249 untuk latih dan 215 untuk uji, RGB 640×480 dari kamera RGB-D), Cityscapes (5.000 citra beranotasi halus, 20.000 beranotasi kasar, 22.973 pasangan stereo 1024×2048, tanpa kebenaran dasar kedalaman), dan Make3D (citra RGB serta kedalaman monokular tanpa stereo atau sekuens). Metode dikelompokkan menjadi tiga berdasarkan sumber sinyal pengawas, yaitu *supervised*, *unsupervised*, dan *semi-supervised*.

Mekanisme utamanya bukan deteksi atau asosiasi objek, melainkan cara jaringan memperoleh kedalaman. Metode *supervised* meregresikan peta kedalaman terhadap kebenaran dasar dengan fungsi rugi L2, Berhu, regresi ordinal berbasis *spacing-increasing discretization*, *conditional random field*, pembelajaran adversarial, dan pelatihan bersama dengan segmentasi semantik. Metode *unsupervised* memakai kendala geometri antarframe, pn−1 ∼ K Tn→n−1 Dn(pn) K−1 pn, lalu menghitung galat fotometrik antara citra asli dan citra yang disintesis ulang dengan SSIM serta rugi kehalusan, dengan topeng penjelas atau topeng geometris untuk objek dinamis dan oklusi. Metode *semi-supervised* memakai pasangan stereo, memprediksi peta disparitas atau kedalaman invers, merekonstruksi citra kiri dari citra kanan, menerapkan rugi konsistensi kiri-kanan, dan mengubah disparitas menjadi kedalaman dengan d = fB/Dis; beberapa kerja menambahkan kebenaran dasar jarang dari LiDAR atau distilasi pengetahuan.

Penulis memakai lima metrik evaluasi sesuai Eigen dkk., yaitu RMSE, RMSE log, Abs Rel, Sq Rel, dan akurasi δ < thr dengan ambang 1,25, 1,25², dan 1,25³. Pada Tabel II untuk KITTI dengan batas kedalaman 80 m (kecuali Garg dkk., 50 m) dan tanpa penyempurnaan daring atau pralatihan, metode *semi-supervised* terbaik adalah Pilzer dkk. (2019) dengan Abs Rel 0,098; Sq Rel 0,831; RMSE 4,656; RMSE log 0,202; serta δ sebesar 0,882, 0,948, dan 0,973. Metode *unsupervised* terbaik adalah Godard dkk. (2019) dengan Abs Rel 0,132; Sq Rel 1,044; RMSE 5,142; RMSE log 0,210; serta δ sebesar 0,845, 0,948, dan 0,977. Sebagai pembanding, Zhou dkk. (2017) mencatat Abs Rel 0,208 dan RMSE 6,865.

Batasan yang dinyatakan penulis mencakup ketergantungan metode *supervised* pada data berlabel yang mahal dan sulit diperoleh; ambiguitas skala, ketidakkonsistenan skala, dan oklusi pada metode *unsupervised*; ketergantungan metode *semi-supervised* pada data pose dan LiDAR; penurunan kinerja yang parah saat data latih dan uji berasal dari kamera atau domain berbeda; biaya komputasi jaringan dalam sehingga sulit berjalan waktu nyata pada perangkat tertanam; serta sedikitnya kajian tentang petunjuk kedalaman yang sebenarnya dipelajari jaringan. Penulis juga mencatat bahwa akurasi metode *unsupervised* masih jauh di bawah metode *semi-supervised* dan bahwa penambahan banyak fungsi rugi menyulitkan pemilihan hiperparameter.
