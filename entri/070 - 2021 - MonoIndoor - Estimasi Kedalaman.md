# 070 - MonoIndoor: Towards Good Practice of Self-Supervised Monocular Depth Estimation for Indoor Environments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ji2021monoindoor` |
| Judul asli | MonoIndoor: Towards Good Practice of Self-Supervised Monocular Depth Estimation for Indoor Environments |
| Penulis | Pan Ji, Runze Li, Bir Bhanu, Yi Xu |
| Tahun | 2021 |
| Venue | IEEE/CVF International Conference on Computer Vision (ICCV 2021) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2107.12429
- **DOI (arXiv):** https://doi.org/10.48550/arXiv.2107.12429
- **Google Scholar:** https://scholar.google.com/scholar?q=MonoIndoor%3A%20Towards%20Good%20Practice%20of%20Self-Supervised%20Monocular%20Depth%20Estimation%20for%20Indoor%20Environments
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=MonoIndoor%3A%20Towards%20Good%20Practice%20of%20Self-Supervised%20Monocular%20Depth%20Estimation%20for%20Indoor%20Environments&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan MonoIndoor, metode estimasi kedalaman monokular — memprediksi peta kedalaman (jarak setiap piksel ke kamera) dari satu citra RGB — yang dilatih secara swa-awas (*self-supervised*) khusus untuk lingkungan dalam ruangan. Pelatihan swa-awas berarti model belajar tanpa data kedalaman acuan dari sensor; sinyal pelatihannya diperoleh dari konsistensi fotometrik antarbingkai video. Metode semacam ini sebelumnya berhasil pada data luar ruangan (berkendara), tetapi kinerjanya menurun tajam di dalam ruangan.

Penulis mengidentifikasi dua penyebab penurunan itu: rentang kedalaman ruangan berubah-ubah antarbingkai, dan gerak kamera dalam ruangan didominasi rotasi besar yang sulit diprediksi jaringan pose. Sebagai jawabannya, makalah ini mengusulkan dua modul: *faktorisasi kedalaman* yang memisahkan peta kedalaman menjadi skala global per citra dan kedalaman relatif, serta *estimasi pose residual* yang menguraikan pose besar menjadi pose awal ditambah rangkaian koreksi kecil. Pada tiga tolok ukur dalam ruangan (EuRoC, NYUv2, 7-Scenes), MonoIndoor mencapai hasil terbaik di antara metode swa-awas saat itu; pada NYUv2 galat AbsRel turun dari 16,0% (Monodepth2) menjadi 13,4%.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman monokular swa-awas dirumuskan sebagai masalah *sintesis tampilan baru* (*novel view synthesis*): diberikan satu bingkai target dan satu bingkai sumber dari video yang sama, model memprediksi peta kedalaman bingkai target dan pose relatif kamera di antara keduanya, lalu bingkai sumber "ditekuk" (*warping*) ke sudut pandang target. Selisih warna antara hasil tekukan dan bingkai target asli menjadi sinyal pelatihan — inilah yang disebut *loss* fotometrik. Kerangka ini dipopulerkan oleh Zhou dkk. (2017) dan disempurnakan oleh Monodepth2 (bab 064), yang pada dataset berkendara KITTI mencapai galat AbsRel 10,6%, tidak jauh dari 7,2% milik metode tersupervisi DORN.

Kondisi itu berubah di dalam ruangan. Sebagai gambaran kesenjangan, metode swa-awas Zhao dkk. pada dataset indoor NYUv2 hanya mencapai AbsRel 18,9%. Penulis MonoIndoor menunjuk dua sebab spesifik. Pertama, **rentang kedalaman tidak konsisten**. Pada pemandangan berkendara, jarak terjauh hampir selalu sama karena kamera melihat langit; pada ruangan, rentang kedalaman kamar mandi (0,1–3 m) sangat berbeda dari lobi (0,1–10 m), dan dapat berubah antarbingkai dalam satu video. Jaringan kedalaman konvensional memetakan keluaran aktivasi *sigmoid* σ ke kedalaman melalui d = 1/(a·σ + b) dengan batas a dan b yang ditetapkan tetap; batas tetap ini menjadi panduan yang keliru ketika skala kedalaman berubah cepat.

Kedua, **rotasi kamera besar**. Video luar ruangan (mobil) didominasi translasi ke depan, sedangkan video dalam ruangan direkam dengan kamera genggam (Kinect) atau wahana udara kecil (*micro aerial vehicle*, MAV) yang sering berputar. Jaringan pose — jaringan kedua dalam kerangka swa-awas yang memprediksi gerak kamera 6 derajat kebebasan (3 translasi, 3 rotasi) — dikenal lemah pada rotasi: temuan Zou dkk. yang dikutip makalah ini menunjukkan galat rotasi jaringan pose dapat sepuluh kali lebih besar daripada metode SLAM geometris (SLAM = *Simultaneous Localization and Mapping*, pemetaan dan pelokalan serentak berbasis geometri). Pose yang salah membuat piksel sumber dipasangkan ke piksel target yang keliru, sehingga loss fotometrik memberi sinyal pelatihan yang menyesatkan. Pekerjaan indoor sebelumnya menghindari masalah ini dengan membuang data: Zhou dkk. membuang pasangan bingkai berotasi murni, dan Bian dkk. menghilangkan komponen rotasi antarbingkai lewat rektifikasi. Makalah ini mengambil jalan berlawanan: rotasi tidak dibuang, melainkan diestimasi secara bertahap.

## Ide Utama

Gagasan pertama adalah **faktorisasi kedalaman**: peta kedalaman satu citra diuraikan menjadi dua faktor — satu skala global (satu angka untuk seluruh citra, misalnya "ruangan ini berjarak maksimum 8 m") dan satu peta kedalaman relatif (bentuk geometri ruangan tanpa skala absolut). Skala global diprediksi oleh cabang jaringan tersendiri, sehingga jaringan kedalaman utama tidak lagi dipaksa menebak skala absolut yang berubah-ubah; ia cukup mempelajari bentuk relatif yang lebih konsisten antarbingkai.

Gagasan kedua adalah **estimasi pose residual**: pose besar antara dua bingkai tidak diprediksi sekaligus, melainkan diurai menjadi pose awal ditambah satu atau beberapa pose residual (koreksi sisa) yang diestimasi berulang. Setelah pose awal dipakai menekuk citra sumber, jaringan kedua melihat selisih antara hasil tekukan dan citra target, lalu memprediksi koreksi kecil berikutnya. Setiap tahap hanya perlu memprediksi gerak kecil, tugas yang jauh lebih mudah dipelajari daripada rotasi besar dalam satu langkah.

## Cara Kerja Langkah demi Langkah

### Kerangka Swa-awas: Kedalaman, Pose, dan Loss Fotometrik

MonoIndoor dibangun di atas kerangka Monodepth2. Sistemnya memuat tiga jaringan: jaringan kedalaman (berstruktur *encoder-decoder* dengan sambungan loncat/*skip connection* — *encoder* memampatkan citra menjadi fitur, *decoder* memulihkannya menjadi peta kedalaman beresolusi penuh), jaringan pose, dan jaringan pose residual. Saat pelatihan, diberikan bingkai target I_t dan bingkai sumber I_t′. Jaringan kedalaman menghasilkan peta kedalaman D_t, jaringan pose menghasilkan transformasi T. Setiap piksel target diproyeksikan ke citra sumber memakai kedalaman, pose, dan matriks intrinsik kamera K (parameter fokus dan titik pusat lensa), lalu warnanya diambil dengan pencuplikan bilinear. Selisih antara citra hasil tekukan dan citra target diukur dengan gabungan selisih absolut (L1) dan SSIM (*Structural Similarity Index*, ukuran kemiripan struktur dua citra). Loss totalnya adalah L = L_A + τ·L_s + γ·L_c, dengan L_s perataan tepi-sadar (*edge-aware smoothness*), L_c loss konsistensi kedalaman antarbingkai (diadopsi dari Bian dkk. 2019), τ = 0,001, dan γ = 0,05. Mekanisme *auto-masking* dari Monodepth2 dipakai untuk menonaktifkan piksel statis yang melanggar asumsi gerak kamera.

### Modul Faktorisasi Kedalaman

Modul ini mengganti prediksi kedalaman absolut dengan dua keluaran. Jaringan kedalaman Monodepth2 tetap dipakai, tetapi hanya memprediksi kedalaman relatif. Skala global S diprediksi oleh **jaringan skala** yang menerima fitur dari *encoder* kedalaman (fitur dipakai bersama, bukan diekstrak ulang) dan mengolahnya melalui tiga tahap.

Tahap pertama adalah blok *self-attention* (perhatian-diri): setiap posisi fitur diproyeksikan menjadi tiga vektor — *query*, *key*, dan *value* — lalu skor kemiripan *query-key* dinormalisasi dengan *softmax* (fungsi yang mengubah skor menjadi bobot berjumlah satu) dan dipakai menimbang *value*. Hasilnya, fitur dari daerah yang informatif bagi skala — misalnya titik terjauh ruangan — mendapat bobot lebih besar. Tahap kedua adalah dua blok residual (lapisan konvolusi dengan sambungan pintas) yang memampatkan fitur. Tahap ketiga adalah tiga lapis terhubung penuh dengan *dropout* 0,5.

Keluaran akhir bukan regresi satu angka langsung — cara itu menurut pengamatan penulis membuat pelatihan tidak stabil — melainkan **kepala regresi probabilistik**: rentang skala yang mungkin didiskritisasi menjadi sejumlah nilai kandidat, jaringan mengeluarkan distribusi probabilitas atas kandidat itu lewat *softmax*, dan skala akhir dihitung sebagai nilai harapannya (jumlah setiap kandidat dikali probabilitasnya). Kedalaman akhir adalah kedalaman relatif dikali S.

### Modul Estimasi Pose Residual

Jaringan pose mula-mula memprediksi pose awal T₀ antara bingkai target dan sumber. Dengan T₀ dan peta kedalaman D_t, citra sumber ditekuk menghasilkan tampilan sintesis; bila pose benar, tampilan ini identik dengan citra target. Kenyataannya tidak, karena pose awal keliru. Jaringan pose residual kemudian menerima citra target dan tampilan sintesis itu, lalu memprediksi pose residual — koreksi kecil yang masih diperlukan. Tampilan sintesis diperbarui dengan koreksi tersebut, dan proses dapat diulang. Pose akhir adalah perkalian berantai seluruh pose: pose awal dikali semua pose residual. Kedua jaringan pose berbagi bobot pada bagian *encoder*, tetapi kepala regresi posenya independen.

Alur data lengkap kedua modul saat pelatihan:

```
bingkai target It        bingkai sumber It'
     │                        │
     ▼                        │
┌─────────────┐               │
│ Depth       │──► peta kedalaman relatif ─┐
│ Encoder-    │                            │  kedalaman akhir
│ Decoder     │                            ▼  D = relatif × S
│ (Monodepth2)│   ┌────────────────┐   ┌───────┐
└──────┬──────┘   │ jaringan skala:│──►│ skala │
       │ fitur ──►│ self-attention │   │ global│
       │ bersama  │ + 2 blok res.  │   │   S   │
       │          │ + kepala prob. │   └───────┘
       │          └────────────────┘
       │
       │     ┌──────────┐ pose awal T0   warp (D, T0)
       └────►│ PoseNet  │────────────────► tampilan sintesis #1
             └──────────┘                      │
                  ▲                            ▼
             ┌───────────────┐ residual  warp  tampilan sintesis #2
             │ ResidualPose- │─────────► (ulangi i kali)
             │ Net           │
             └───────────────┘
        pose akhir T = T0 × T_res,1 × ... × T_res,i
        loss fotometrik: bandingkan It dengan sintesis akhir
```

Diagram di atas menunjukkan dua jalur yang bertemu pada loss fotometrik: jalur kedalaman (atas) menghasilkan D, jalur pose (bawah) menghasilkan T lewat penyempurnaan bertahap. Catatan penting dari hasil ablasi makalah: satu blok pose residual sudah memberi hampir seluruh perbaikan; menambah blok lebih banyak tidak menambah akurasi.

### Pelatihan

Model diimplementasikan dalam PyTorch dan dilatih 40 *epoch* dengan pengoptimal Adam; laju pembelajaran 10⁻⁴ pada 20 *epoch* pertama, lalu 10⁻⁵. Resolusi citra pelatihan 512×256 pada EuRoC dan 320×256 pada NYUv2.

## Eksperimen dan Hasil

Evaluasi dilakukan pada tiga dataset dalam ruangan. EuRoC MAV berisi video wahana udara kecil di aula mesin dan ruang Vicon; pelatihan memakai lima sekuens (MH_01, MH_02, MH_04, V1_01, V1_02), pengujian pada sekuens V2_01. NYUv2 berisi 464 video ruangan dari kamera Kinect genggam; dipakai 302 sekuens latih (±20 ribu citra setelah penipisan bingkai) dan 654 citra uji resmi. 7-Scenes berisi tujuh ruangan; model dipra-latih pada NYUv2 lalu disetel halus. Metrik yang dipakai: AbsRel (rata-rata galat relatif |d − d*|/d*, makin kecil makin baik), RMSE (akar kuadrat rata-rata galat kuadrat), dan akurasi δ₁ (persentase piksel dengan rasio prediksi terhadap acuan di bawah 1,25; makin besar makin baik).

Hasil utama pada EuRoC: AbsRel Monodepth2 15,7% turun menjadi 14,9% dengan faktorisasi kedalaman saja, 14,1% dengan pose residual saja, dan 12,5% dengan keduanya; δ₁ naik dari 78,6% menjadi 84,0%. Pada NYUv2 polanya sama: 16,0% menjadi 15,2% (faktorisasi saja), 14,2% (pose residual saja), dan 13,4% (keduanya), dengan δ₁ dari 76,7% menjadi 82,3%. Kedua modul terbukti menyumbang perbaikan secara terpisah, dan kombinasinya memberi perbaikan terbesar — penurunan AbsRel sekitar seperlima dari garis dasar pada kedua dataset.

Dibandingkan metode swa-awas indoor terbaik sebelumnya (Bian dkk., yang menghilangkan rotasi lewat rektifikasi), MonoIndoor pada NYUv2 menurunkan AbsRel 1,3 poin dan menaikkan δ₁ 1,9 poin. Pada 7-Scenes, pada scene "Fire" dicapai AbsRel 7,7% dan δ₁ 93,9%, pada scene "Heads" AbsRel 10,6% dan δ₁ 88,9% — keduanya lebih baik 1,2–1,8 poin AbsRel dari pembanding tersebut, baik sebelum maupun sesudah penyetelan halus, yang menunjukkan kemampuan generalisasi lintas dataset. Akurasi ini juga melampaui sebagian metode tersupervisi yang lebih tua, sehingga kesenjangan antara swa-awas dan supervisi penuh di dalam ruangan menyempit.

Evaluasi odometri pada EuRoC mengukur kualitas pose secara langsung: pada sekuens V1_03, galat lintasan absolut (ATE) turun dari 0,0681 m menjadi 0,052 m, dan galat pose relatif rotasi turun dari 1,3237° menjadi 0,7179° — hampir separuhnya. Angka ini mengonfirmasi klaim bahwa estimasi pose residual memang memperbaiki prediksi rotasi, bukan sekadar menaikkan metrik kedalaman.

## Kelebihan dan Keterbatasan

Kelebihannya: kedua modul menyerang penyebab kegagalan yang teridentifikasi jelas dan efektivitasnya dibuktikan ablasi terpisah; tidak ada data rotasi yang dibuang, berbeda dengan pendekatan rektifikasi; modul faktorisasi kedalaman menurut penulis bersifat agnostik terhadap jenis supervisi sehingga berpotensi dipakai pada metode tersupervisi; dan generalisasi lintas dataset terbukti pada 7-Scenes.

Keterbatasannya: fenomena bahwa blok pose residual tambahan tidak memperbaiki hasil tidak dijelaskan dan diakui penulis sebagai pekerjaan lanjutan. Dari sisi metode, seluruh pelatihan masih bertumpu pada asumsi fotometrik — pencahayaan konstan dan permukaan difus — sehingga daerah reflektif atau minim tekstur (dinding polos, kaca) berpotensi menghasilkan kedalaman keliru. Dari sisi rekayasa, iterasi *warping* dan jaringan pose tambahan menambah biaya pelatihan dibandingkan Monodepth2 polos, dan kedalaman yang dihasilkan tetap berskala per-video sehingga tidak otomatis konsisten metrik lintas video.

## Kaitan dengan Bab Lain

Bab ini meneruskan garis klaster Estimasi Kedalaman. Fondasi estimasi kedalaman dari citra tunggal diletakkan pada [bab 062 (Eigen dkk.)](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md), yang juga memperkenalkan metrik AbsRel dan δ yang dipakai di sini. Paradigma swa-awas stereo dibuka oleh [bab 063 (Monodepth)](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md), dan MonoIndoor secara eksplisit memakai [bab 064 (Monodepth2)](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md) sebagai tulang punggung: jaringan kedalaman, loss fotometrik L1+SSIM, *auto-masking*, dan arsitektur pose semuanya diwarisi, lalu dua modul ditambahkan di atasnya. Arah yang berbeda untuk ruangan dalam ditempuh metode tersupervisi seperti [bab 065 (BTS)](./065%20-%202019%20-%20BTS%20%28Local%20Planar%20Guidance%29%20-%20Estimasi%20Kedalaman.md) dan [bab 066 (AdaBins)](./066%20-%202021%20-%20AdaBins%20-%20Estimasi%20Kedalaman.md); keluarga ini kemudian dilanjutkan oleh MonoIndoor++ (2023) yang menyempurnakan praktik yang sama. Bagi tinjauan YOLO/RGB-D, bab ini relevan sebagai penyedia *pseudo-depth* dalam ruangan: kedalaman hasil prediksi dapat menggantikan sensor kedalaman pada skenario robotik dalam ruangan.

## Poin untuk Sitasi

Kutip dengan kunci `ji2021monoindoor`. Ringkasan yang aman dikutip: "MonoIndoor mengadaptasi estimasi kedalaman monokular swa-awas ke lingkungan dalam ruangan melalui dua modul — faktorisasi kedalaman yang memisahkan skala global dari kedalaman relatif, dan estimasi pose residual iteratif untuk rotasi besar — sehingga menurunkan AbsRel terhadap Monodepth2 dari 15,7% menjadi 12,5% pada EuRoC dan dari 16,0% menjadi 13,4% pada NYUv2." Seluruh angka di bab ini diambil dari naskah arXiv:2107.12429v2; khusus untuk angka per-scene pada 7-Scenes ("Fire", "Heads") dan rincian tabel ablasi (mis. RMSE 0,466), verifikasi ulang ke tabel naskah asli disarankan sebelum sitasi formal, karena sebagian hanya dibaca dari teks ar5iv hasil konversi.
