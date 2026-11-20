# A precise berry counting method for in-cluster grapes to guide berry thinning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `du2026precise` |
| Judul asli | A precise berry counting method for in-cluster grapes to guide berry thinning |
| Penulis | Du, Wensheng; Qin, Weishuai; Cui, Xiao; Zhu, Yanjun; Jia, Yonghao; Wang, Ruihan; Du, Yuanpeng |
| Tahun | 2026 |
| Venue | Frontiers in Plant Science |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [du2026precise.pdf](../pdf/du2026precise.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2025.1739688

## Gambaran Umum

Penelitian ini bertujuan menghasilkan cara menghitung buah secara tepat di dalam tandan anggur meja untuk memandu penjarangan buah. Penjarangan memerlukan jumlah buah awal per tandan, sementara hitungan manual bersifat padat karya, lambat, dan rentan galat. Penulis mengusulkan jaringan dua cabang bernama MVDNet yang melakukan regresi peta kerapatan buah dan segmentasi tandan secara bersamaan, dilengkapi algoritme pasca-olahan untuk menghitung buah per tandan.

Tanaman yang dipakai adalah anggur meja kultivar Shine Muscat yang telah diberi perlakuan tanpa biji dan dibudidayakan dengan sistem teralis atas. Pengambilan citra dilakukan pukul 08.00–15.00 pada tiga hari cerah, 28–30 Mei 2021, di stasiun percobaan hortikultura Universitas Pertanian Shandong, Distrik Daiyue, Tai'an, Provinsi Shandong, Cina (117°9'38,92" BT, 36°9'47,4" LU). Kamera iPhone SE menghasilkan citra 3024 × 4032 piksel yang kemudian diskalakan menjadi 1024 × 1365. Dari 779 citra yang diseleksi manual, 545 masuk himpunan latih (49.960 buah, 1.102 tandan), 155 validasi (14.650 buah, 315 tandan), dan 79 uji (7.671 buah, 132 tandan). Anotasi memakai Labelme: buah ditandai sebagai titik dan tandan sebagai poligon; peta kerapatan dibentuk secara daring dengan konvolusi kernel Gaussian terhadap peta titik.

MVDNet mengadopsi arsitektur penyandi–penyandi ulang dua cabang yang terinspirasi U-Net. Bagian depan memakai encoder bersama dengan tiga tahap penurunan sampel dan modul Universal Inverted Bottleneck dari MobileV4, ditambah fusi fitur multiskala dan mekanisme perhatian SimAM tanpa parameter. Bagian belakang melakukan tiga tahap penaikan sampel dengan sambungan lewati. Cabang regresi merekonstruksi peta kerapatan buah, sedangkan cabang segmentasi membatasi tandan. Fungsi rugi total menjumlahkan rugi peta kerapatan (MSE) dan rugi segmentasi (entropi silang biner plus rugi Dice) dengan penjadwal bobot adaptif; bobot awal berturut-turut 1 dan 0,01, sedangkan bobot komponen segmentasi awalnya 1 dan 1. Pelatihan berlangsung 300 epoch dengan laju pembelajaran 1e-4, pengoptimal Adam, peluruhan bobot 1e-4, potongan citra 512 × 512, ukuran kelompok 4, dan penghentian awal setelah 50 epoch tanpa perbaikan, memakai GPU NVIDIA GeForce RTX 3090 24 GB dan PyTorch 1,9,0 dalam kerangka NWPU-Crowd. Pasca-olahan membaca peta segmentasi dan peta kerapatan. Peta segmentasi dibinerkan pada ambang 0,5, lalu diberi operasi morfologis penutupan dan pembukaan. Kontur diekstrak dan disaring berdasarkan luas minimum, titik pusatnya dihitung dari momen citra, lalu dikelompokkan dengan DBSCAN untuk memisahkan tandan. Jumlah buah per tandan dihitung dengan mengintegralkan peta kerapatan pada topeng hasil segmentasi. Uji sensitivitas menunjukkan nilai minPts = 1 memberi kinerja terbaik dan nilai ε dalam rentang 10–20 tidak berpengaruh.

Pada himpunan uji, MVDNet mencapai MAE 7,7, RMSE 12,6, dan MIoU 0,90 dengan 3,372 juta parameter. Pengujian ablasi menunjukkan kinerja naik dari 9,0/13,4/0,85 pada bagian depan saja menjadi 8,5/13,2/0,86 setelah bagian belakang ditambahkan, 8,2/12,9/0,88 setelah fusi multis skala, dan 7,7/12,6/0,90 setelah SimAM ditambahkan. Tabel perbandingan mencantumkan MCNN 14,2/21,2/0,73, CSRNet 9,3/16,9/0,80, CANNet 10,3/14,8/0,80, dan SCAR 9,0/16,8/0,87. Hitungan buah per tandan menghasilkan R² = 0,886 dengan galat rata-rata −0,83 dan simpangan baku 12,00; sebagian besar galat berada dalam rentang wajar dan sedikit pencilan melebihi ±20. Kinerja cabang regresi dan segmentasi pada model dua tugas sama dengan kinerja model yang dilatih terpisah.

Penulis menyatakan beberapa batasan. Akurasi hitungan per tandan bergantung pada kedua cabang; pada tandan yang sangat rapat dan tumpang tindih, galat segmentasi merambat ke tahap hitungan, sementara model kerapatan kesulitan menangkap oklusi dan distorsi perspektif yang kompleks. Penulis menunjukkan dua kasus gagal: tandan yang terlalu longgar terdeteksi sebagai dua tandan, dan dua tandan yang saling menempel terdeteksi sebagai satu. Model dilatih dan divalidasi pada satu himpunan data, sehingga kemampuan generalisasi pada kultivar, sistem teralis, dan kondisi pencahayaan lain belum diuji. Himpunan data hanya berisi 779 citra; penulis membandingkannya dengan kajian lain yang memakai 26.230 citra dan hanya satu tandan per citra. Data tersedia atas permintaan penulis. Kajian lanjutan yang diusulkan mencakup arsitektur Vision Transformer, data tiga dimensi, deteksi titik pusat bersamaan, himpunan data lintas kultivar, adaptasi ranah, dan pembelajaran sedikit contoh.
