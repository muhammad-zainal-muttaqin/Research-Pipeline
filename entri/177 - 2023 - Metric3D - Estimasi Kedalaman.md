# 177 - Metric3D: Towards Zero-Shot Metric 3D Prediction from a Single Image

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yin2023metric3d` |
| Judul asli | Metric3D: Towards Zero-Shot Metric 3D Prediction from a Single Image |
| Penulis | Wei Yin, Chi Zhang, Hao Chen, Zhipeng Cai, Gang Yu, Kaixuan Wang, Xiaozhi Chen, Chunhua Shen |
| Tahun | 2023 |
| Venue | IEEE/CVF International Conference on Computer Vision (ICCV 2023) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2307.10984
- **Google Scholar:** https://scholar.google.com/scholar?q=Metric3D%3A%20Towards%20Zero-Shot%20Metric%203D%20Prediction%20from%20a%20Single%20Image
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Metric3D%3A%20Towards%20Zero-Shot%20Metric%203D%20Prediction%20from%20a%20Single%20Image&sort=relevance

## Gambaran Umum

Metric3D adalah metode estimasi *depth* (kedalaman) metrik dari satu citra RGB yang mampu menghasilkan jarak dalam satuan nyata (meter) untuk kamera dan domain apa pun tanpa penyesuaian ulang, disebut kemampuan *zero-shot* (generalisasi ke data yang tidak dilihat saat pelatihan). Masalah yang dipecahkan adalah ambiguitas skala: jaringan yang dilatih pada citra dari satu kamera cenderung gagal memprediksi kedalaman berskala benar ketika diuji pada citra dari kamera dengan parameter optik berbeda. Penulis menunjukkan bahwa sumber ambiguitas ini dapat diisolasi secara eksplisit melalui transformasi geometris pada tahap pelatihan, disebut *canonical camera space transformation* (transformasi ke ruang kamera kanonik/rujukan tunggal). Dengan menyelaraskan seluruh data pelatihan lintas-kamera ke satu ruang kamera rujukan sebelum dilatih, model dapat mempelajari kedalaman metrik yang konsisten, lalu ditransformasikan kembali ke skala kamera aslinya saat inferensi. Metode ini dilatih pada lebih dari delapan juta citra dari sebelas kumpulan data (dataset) berbeda dan mencapai performa terbaik (*state-of-the-art*) pada tujuh tolok ukur (*benchmark*) zero-shot, sekaligus memenangkan *2nd Monocular Depth Estimation Challenge*. Kegunaan praktisnya diuji pada rekonstruksi 3D metrik dan *Simultaneous Localization and Mapping* (SLAM) monokular, dua tugas yang selama ini terkendala oleh ketidaktahuan skala dari citra tunggal.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi *depth* monokular (dari satu citra, tanpa sensor jarak atau pasangan stereo) adalah masalah yang secara matematis kurang terbatas (*ill-posed*): satu citra dua dimensi dapat berasal dari tak terhingga banyak konfigurasi tiga dimensi yang berbeda. Sebagian besar metode sebelum Metric3D, seperti MiDaS dan DPT (*Dense Prediction Transformer*, arsitektur berbasis *transformer* untuk prediksi padat per piksel), mengatasi hal ini dengan memprediksi *depth* relatif — urutan jarak antar-titik, bukan jarak dalam satuan nyata. *Depth* relatif cukup untuk beberapa aplikasi visual, tetapi tidak dapat langsung dipakai untuk pengukuran fisik, navigasi robot, atau rekonstruksi bangunan berskala benar.

Metode yang mencoba memprediksi *depth* metrik langsung umumnya dilatih dan diuji pada satu domain kamera saja (misalnya hanya kamera mobil otonom pada KITTI atau hanya sensor RGB-D dalam ruangan pada NYU Depth V2), karena hubungan antara jarak sebenarnya dan ukuran objek pada citra bergantung pada panjang fokus (*focal length*) kamera. Citra yang sama dari objek pada jarak berbeda, difoto dengan kamera berpanjang fokus berbeda, dapat menghasilkan proyeksi piksel yang identik — inilah akar ambiguitas skala. ZoeDepth (bab 176), yang membahas gabungan berbagai domain lewat kepala prediksi khusus per domain, adalah salah satu upaya mengatasi hal ini secara tidak langsung dengan merutekan citra ke penaksir skala berbeda-beda bergantung domain yang dikenali. Metric3D mengambil arah berbeda: alih-alih merutekan citra ke penaksir berbeda, penulis menghilangkan sumber ambiguitas itu sendiri dengan menormalkan seluruh data pelatihan ke satu ruang kamera acuan sebelum pembelajaran berlangsung.

## Ide Utama

Gagasan inti Metric3D adalah bahwa ambiguitas skala akibat panjang fokus dapat dihilangkan dengan transformasi geometris sederhana sebelum data masuk ke jaringan, bukan dengan menambah kapasitas model untuk menebak-nebak kamera apa yang dipakai. Panjang fokus menentukan rasio antara ukuran piksel suatu objek pada citra dan jarak sebenarnya objek itu dari kamera. Jika seluruh citra pelatihan — yang berasal dari kamera berbeda-beda — diskalakan ulang seolah-olah diambil oleh satu kamera rujukan (kanonik) dengan panjang fokus tetap, hubungan antara piksel dan jarak metrik menjadi konsisten di seluruh dataset. Jaringan kemudian hanya perlu mempelajari satu pemetaan tunggal dari citra kanonik ke *depth* metrik, bukan mempelajari pemetaan berbeda untuk tiap kamera. Saat inferensi pada kamera baru yang panjang fokusnya diketahui, prediksi dalam ruang kanonik ditransformasikan balik (*de-canonicalization*) ke skala kamera nyata tersebut.

## Cara Kerja Langkah demi Langkah

### Transformasi ke Ruang Kamera Kanonik

Metric3D mendefinisikan sebuah kamera kanonik dengan panjang fokus rujukan f_c. Untuk setiap sampel pelatihan dengan panjang fokus asli f, rasio transformasi dihitung sebagai ω = f_c / f. Penulis mengusulkan dua cara menerapkan rasio ini, yang dapat dipilih bergantung pengaturan pelatihan:

- **CSTM-label**: label *ground-truth* (kedalaman rujukan/sebenarnya) diskalakan langsung dengan mengalikan peta kedalaman dengan ω, sementara citra masukan tidak diubah. Cara ini murah secara komputasi karena hanya mengubah label, tetapi citra tetap berasal dari geometri kamera aslinya.
- **CSTM-image**: citra masukan diubah ukurannya (*resize*) dengan rasio ω sehingga citra tampak seolah-olah difoto oleh kamera kanonik, sedangkan label kedalaman tidak diubah. Cara ini menyelaraskan geometri citra itu sendiri, sehingga jaringan konvolusi memproses pola tekstur-jarak yang konsisten, tetapi menuntut pengubahan ukuran citra pada setiap iterasi pelatihan.

Kedua varian menghasilkan pasangan citra-label yang konsisten dengan asumsi kamera tunggal, sehingga jaringan prediksi *depth* dapat dilatih sebagaimana jaringan biasa tanpa mekanisme kondisional tambahan untuk membedakan sumber kamera.

### Transformasi Balik saat Inferensi

Pada saat pemakaian, panjang fokus kamera nyata f_test diketahui atau diestimasi dari metadata citra. Jaringan tetap memprediksi *depth* dalam ruang kanonik, kemudian hasilnya dikalikan dengan kebalikan rasio transformasi (f_test / f_c) untuk memperoleh *depth* metrik dalam skala kamera nyata. Diagram berikut merangkum alur data dari pelatihan hingga inferensi:

```
PELATIHAN (banyak kamera, f berbeda-beda)
 citra_1 (f=800) --+                     +-- label_1 (kedalaman asli)
 citra_2 (f=1200) --+--> transformasi --> +-- label_2 (diskalakan w=fc/f)
 citra_3 (f=500)  --+   ke ruang kanonik  +-- label_3
                          |
                          v
                 jaringan prediksi depth
                 (satu pemetaan tunggal)
                          |
INFERENSI (kamera baru, f_test)          v
 citra_baru --> prediksi ruang kanonik --> de-kanonikalisasi (x f_test/fc)
                                           --> depth metrik skala nyata
```

Diagram ini menunjukkan bahwa keragaman kamera diserap pada tahap pra-pemrosesan (kiri) dan tahap pasca-pemrosesan (kanan), sementara inti jaringan di tengah hanya menangani satu ruang geometri tunggal.

### Random Proposal Normalization Loss

Selain transformasi kanonik, penulis menambahkan fungsi kerugian (*loss*) bernama *Random Proposal Normalization Loss* (RPNL). *Loss* ini mengambil 32 tambalan (*patch*) acak dari peta kedalaman, berukuran 12,5% hingga 50% dari citra penuh, lalu menormalkan nilai kedalaman pada tiap tambalan memakai *median absolute deviation* (MAD, ukuran sebaran data berbasis median, tahan terhadap nilai pencilan). Normalisasi lokal per tambalan — bukan pada citra penuh — memaksa jaringan mempertajam kontras geometris pada skala lokal, sehingga struktur permukaan dan tepian objek dalam wilayah kecil citra diprediksi lebih akurat, melengkapi konsistensi skala global yang sudah disediakan oleh transformasi kanonik.

### Arsitektur dan Data Pelatihan

Jaringan Metric3D memakai *backbone* (jaringan penyari fitur) ConvNeXt, sebuah arsitektur konvolusi modern, dengan varian *tiny* dan *large*, dipasangkan dengan dekoder bertipe *hourglass* (struktur menyempit lalu melebar kembali untuk menghasilkan peta kedalaman resolusi penuh). Model dilatih pada sebelas dataset gabungan berjumlah lebih dari delapan juta citra, mencakup adegan luar ruang dari kendaraan otonom, adegan dalam ruang dari sensor RGB-D, dan citra tangkapan stereo, dengan ribuan konfigurasi kamera berbeda. Skala data sebesar ini penting karena transformasi kanonik hanya efektif bila jaringan terpapar variasi panjang fokus yang luas selama pelatihan, bukan hanya satu atau dua domain kamera.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tujuh tolok ukur *zero-shot*, termasuk NYU Depth V2 (adegan dalam ruang) dan KITTI (adegan luar ruang dari kamera kendaraan), memakai metrik AbsRel (*Absolute Relative Error*, rata-rata selisih absolut antara kedalaman prediksi dan kebenaran dibagi kedalaman kebenaran — semakin kecil semakin baik) dan δ₁ (persentase piksel yang rasio prediksi-terhadap-kebenarannya berada dalam ambang 1,25 — semakin besar semakin baik). Pada NYU Depth V2, varian CSTM-label dilaporkan mencapai AbsRel 0,083 dengan δ₁ 0,944; pada KITTI, AbsRel 0,058 dengan δ₁ 0,964. Nilai AbsRel di bawah 0,1 pada kedua domain menunjukkan model mempertahankan akurasi metrik yang wajar meski diuji pada dataset yang tidak dipakai dalam pelatihan langsungnya — properti yang jarang dicapai metode *depth* metrik sebelum Metric3D, yang umumnya hanya akurat pada domain tempatnya dilatih.

Pada aplikasi SLAM monokular, *depth* metrik dari Metric3D diberikan sebagai masukan tambahan ke Droid-SLAM (sistem SLAM berbasis pembelajaran mendalam) pada rangkaian data KITTI *odometry*. Penulis melaporkan penurunan drastis galat drift translasi pada salah satu sekuens uji, dari sekitar 33,9% menjadi sekitar 1,44%. Penurunan sebesar ini mengindikasikan bahwa sumber utama *drift* skala pada SLAM monokular — yaitu tidak adanya rujukan metrik absolut sepanjang lintasan — dapat dikompensasi oleh *depth* metrik per-*frame* yang konsisten. Pada rekonstruksi 3D, model diuji pada sembilan adegan NYU Depth V2 yang tidak dilihat saat pelatihan, dengan hasil jarak Chamfer L1 (metrik kemiripan antar-permukaan 3D, mengukur jarak rata-rata titik-ke-titik terdekat) dan F-score yang lebih baik dibanding LeReS, DPT, dan baseline *multi-view stereo*. Penulis turut menunjukkan rekonstruksi metrik dari citra internet (Flickr) dengan ukuran struktur nyata yang mendekati ukuran sebenarnya, mendukung klaim kegunaan pada metrologi (pengukuran) skala benda dari citra tunggal tanpa kalibrasi lapangan.

## Kelebihan dan Keterbatasan

Kelebihan utama Metric3D adalah pemisahan yang jelas antara sumber ambiguitas (panjang fokus kamera) dan pembelajaran representasi kedalaman, sehingga solusi geometris sederhana — transformasi kanonik — dapat dipasangkan pada arsitektur jaringan prediksi kedalaman standar tanpa mekanisme kondisional yang rumit. Cakupan data pelatihan yang sangat luas (sebelas dataset, delapan juta citra) turut menjelaskan kemampuan generalisasi lintas domain yang kuat, dibuktikan pada tujuh tolok ukur berbeda dan pada aplikasi hilir seperti SLAM.

Dari sisi rekayasa, pendekatan ini menuntut panjang fokus kamera diketahui atau diestimasi dengan cukup akurat pada tahap inferensi; kesalahan estimasi panjang fokus akan langsung menerjemahkan menjadi kesalahan skala pada *depth* metrik keluaran, karena transformasi balik bergantung sepenuhnya pada rasio f_test terhadap f_c. Secara konseptual, transformasi kanonik mengasumsikan model kamera *pinhole* sederhana dengan distorsi lensa yang dapat diabaikan; kamera dengan distorsi ekstrem (lensa sudut sangat lebar atau *fisheye*) berpotensi tidak tercakup baik oleh asumsi ini. Pengumpulan dan penyelarasan sebelas dataset berskala metrik juga merupakan beban rekayasa data yang besar, sehingga replikasi penuh metode ini menuntut akses ke infrastruktur data yang setara.

## Kaitan dengan Bab Lain

Metric3D berada dalam klaster Estimasi Kedalaman bersama ZoeDepth (bab [176](./176%20-%202023%20-%20ZoeDepth%20-%20Estimasi%20Kedalaman.md)), yang mengatasi masalah lintas-domain serupa lewat kepala prediksi metrik yang dirutekan per domain, bukan lewat transformasi geometris eksplisit; kedua pendekatan dapat dibandingkan langsung sebagai dua strategi berbeda untuk masalah yang sama. Depth Anything V2 (bab [175](./175%20-%202024%20-%20Depth%20Anything%20V2%20-%20Estimasi%20Kedalaman.md)) berfokus pada kualitas *depth* relatif berbasis data sintetis berskala besar, sehingga saling melengkapi dengan Metric3D yang menyasar skala metrik absolut. Marigold (bab [178](./178%20-%202024%20-%20Marigold%20-%20Estimasi%20Kedalaman.md)) mendekati estimasi kedalaman lewat model difusi, jalur teknis berbeda dari jaringan regresi langsung yang dipakai Metric3D, namun berbagi tujuan generalisasi zero-shot yang sama. NeWCRFs (bab [179](./179%20-%202022%20-%20NeWCRFs%20-%20Estimasi%20Kedalaman.md)) mewakili generasi metode *depth* metrik domain-tunggal sebelum tren zero-shot lintas-kamera berkembang, sehingga menjadi rujukan kondisi bidang sebelum kontribusi Metric3D. Kemampuan Metric3D menghasilkan *depth* metrik yang stabil lintas-kamera relevan bagi bab-bab lain dalam tinjauan yang membahas gabungan RGB-D untuk lokalisasi dan rekonstruksi 3D, karena *depth* metrik yang andal adalah prasyarat bagi peta 3D berskala benar.

## Poin untuk Sitasi

Kutip dengan kunci `yin2023metric3d`. Ringkasan yang aman dikutip: "Metric3D mengusulkan transformasi ke ruang kamera kanonik untuk menghilangkan ambiguitas skala akibat panjang fokus kamera yang beragam, dilatih pada lebih dari delapan juta citra dari sebelas dataset, dan mencapai performa zero-shot terbaik pada tujuh tolok ukur sekaligus memenangkan 2nd Monocular Depth Estimation Challenge (Yin dkk., ICCV 2023)." Angka AbsRel 0,083/δ₁ 0,944 pada NYU Depth V2 dan AbsRel 0,058/δ₁ 0,964 pada KITTI, serta angka penurunan drift SLAM dari sekitar 33,9% menjadi 1,44% pada satu sekuens KITTI odometry, diperoleh dari ekstraksi otomatis naskah arXiv dan **wajib diverifikasi ulang terhadap tabel asli** (termasuk memastikan tabel yang tepat dan kondisi ujinya) sebelum dikutip dalam karya formal. Detail konfigurasi RPNL (32 tambalan, rentang ukuran 12,5–50%) dan hasil Chamfer L1/F-score pada sembilan adegan NYU juga perlu dicek ulang ke naskah karena belum diverifikasi silang dari sumber kedua.
