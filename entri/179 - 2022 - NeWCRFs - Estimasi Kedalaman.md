# 179 - Neural Window Fully-Connected CRFs for Monocular Depth Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yuan2022newcrfs` |
| Judul asli | Neural Window Fully-connected CRFs for Monocular Depth Estimation |
| Penulis | Weihao Yuan, Xiaodong Gu, Zuozhuo Dai, Siyu Zhu, Ping Tan |
| Tahun | 2022 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2203.01502
- **Repositori kode resmi:** https://github.com/aliyun/NeWCRFs
- **Halaman proyek:** https://weihaosky.github.io/newcrfs/
- **Google Scholar:** https://scholar.google.com/scholar?q=Neural%20Window%20Fully-Connected%20CRFs%20for%20Monocular%20Depth%20Estimation

## Gambaran Umum

NeWCRFs (*Neural Window Fully-connected Conditional Random Fields*) merumuskan estimasi kedalaman monokular — memperkirakan jarak setiap piksel ke kamera dari satu citra RGB tunggal — sebagai masalah optimisasi *conditional random field* (CRF, model probabilistik yang menghubungkan variabel-variabel bertetangga agar prediksinya saling konsisten) yang dihitung secara lokal per jendela citra, bukan sebagai regresi langsung dari jaringan konvolusi dalam. Alih-alih menghubungkan seluruh piksel citra dalam satu graf CRF berukuran penuh — yang secara komputasi terlalu mahal — makalah ini membagi peta fitur menjadi jendela-jendela kecil dan menghitung CRF *fully-connected* (setiap simpul terhubung ke semua simpul lain dalam jendela yang sama) di dalam tiap jendela, lalu mengimplementasikan penghitungan itu sebagai mekanisme *multi-head attention* (perhatian bertingkat, cara jaringan memberi bobot berbeda pada tiap pasangan elemen fitur) sehingga seluruh proses dapat dilatih secara *end-to-end* bersama jaringan saraf. Arsitekturnya memakai Swin Transformer sebagai *encoder* (pengekstrak fitur) dan modul CRF berjendela ini sebagai *decoder* bertingkat, dari resolusi kasar ke resolusi halus. Pada saat rilis, metode ini mencapai kinerja *state-of-the-art* (kondisi terbaik yang tercatat) pada NYU Depth v2 dan KITTI, dua tolok ukur standar estimasi kedalaman indoor dan outdoor.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Estimasi kedalaman dari satu citra bersifat *ill-posed* (kurang terdefinisi secara matematis): satu citra RGB dapat berasal dari banyak konfigurasi 3D berbeda, sehingga model harus menyimpulkan petunjuk tidak langsung seperti tekstur, oklusi, dan ukuran relatif objek. Generasi metode sebelum NeWCRFs — misalnya BTS (*Big to Small*, memakai panduan planar lokal bertingkat) dan AdaBins (mengelompokkan kedalaman ke dalam sejumlah *bin* adaptif) — menyerang masalah ini dengan merancang arsitektur regresi yang semakin rumit, tanpa mekanisme eksplisit untuk memaksa konsistensi spasial antarpiksel bertetangga. DPT menunjukkan bahwa mengganti *backbone* konvolusi dengan Vision Transformer memperbaiki hasil, tetapi juga tanpa komponen konsistensi lokal semacam itu.

CRF adalah alat klasik untuk memperbaiki masalah ini: dengan menghubungkan piksel bertetangga dan mendorong nilai kedalaman yang berdekatan agar konsisten, CRF mempertajam batas objek dan mengurangi derau prediksi. Sebelum era pembelajaran dalam, CRF banyak dipakai sebagai lapisan pasca-pemrosesan pada tugas prediksi *dense* (padat per piksel) seperti segmentasi semantik. Masalahnya, CRF *fully-connected* pada graf sebesar citra penuh — di mana setiap piksel berpotensi terhubung ke semua piksel lain — memiliki kompleksitas komputasi yang tumbuh sangat cepat seiring jumlah piksel, sehingga dalam praktiknya CRF hanya dihitung antar-tetangga terdekat. Pembatasan ini mengurangi kemampuan CRF menangkap relasi jarak jauh dalam citra.

## Ide Utama

Gagasan inti NeWCRFs adalah membagi citra menjadi jendela-jendela kecil dan menghitung CRF *fully-connected* di dalam tiap jendela, alih-alih pada seluruh citra sekaligus. Karena tiap jendela hanya berisi sejumlah kecil simpul (piksel atau petak fitur), penghitungan hubungan antarsemua pasangan simpul di dalamnya tetap murah secara komputasi, sementara sifat "terhubung penuh" (setiap simpul saling memengaruhi) tetap terjaga secara lokal. Operasi ini kemudian direalisasikan bukan sebagai algoritme optimisasi CRF tradisional (misalnya *mean-field inference*, pendekatan iteratif untuk menaksir distribusi CRF), melainkan sebagai satu lapisan *neural network* yang meniru bentuk CRF: potensi hubungan antarsimpul dihitung memakai *multi-head attention*, mekanisme yang sama dipakai Transformer untuk menimbang relevansi antarelemen fitur. Dengan cara ini, langkah optimisasi CRF menyatu ke dalam arsitektur jaringan dan dapat dilatih bersama seluruh model memakai *backpropagation*, bukan dijalankan sebagai tahap terpisah setelah jaringan menghasilkan prediksi awal.

## Cara Kerja Langkah demi Langkah

### Encoder Swin Transformer

Citra masukan diproses oleh Swin Transformer, arsitektur Transformer citra yang membagi citra menjadi jendela-jendela lokal untuk menghitung *self-attention* (mekanisme di mana tiap elemen fitur menimbang relevansi elemen lain) secara efisien, lalu menggeser posisi jendela antar-lapis agar informasi tetap mengalir lintas batas jendela (dibahas rinci pada bab 025). *Encoder* ini menghasilkan fitur multiskala: peta fitur beresolusi kasar di lapis dalam dan beresolusi halus di lapis dangkal, pola umum arsitektur Transformer citra hierarkis.

### Struktur Bottom-Up-Top-Down dan Level Jendela

Dekoder NeWCRFs disusun dalam empat level, dari petak fitur berukuran 4×4 piksel pada level bawah hingga 32×32 piksel pada level atas. Pada tiap level, sejumlah petak digabung menjadi satu jendela berukuran tetap N×N (makalah menetapkan N = 7). Untuk citra berukuran H×W, jumlah jendela pada level bawah adalah (H/4N)×(W/4N), dan pada level atas (H/32N)×(W/32N) — level atas memiliki jendela lebih sedikit karena tiap petaknya mencakup wilayah citra yang lebih luas. Struktur ini disebut *bottom-up-top-down*: fitur diekstraksi dari resolusi tinggi ke rendah oleh *encoder* (arah *bottom-up*), kemudian prediksi kedalaman disempurnakan dari resolusi rendah ke tinggi oleh dekoder (arah *top-down*), dengan modul CRF berjendela dijalankan pada tiap level.

### Modul Neural Window FC-CRF

Pada tiap level, modul CRF menerima dua masukan: peta fitur dari *encoder* pada level tersebut, dan prediksi kedalaman kasar dari level di atasnya (level dengan resolusi lebih rendah). Modul menghitung dua jenis potensi CRF klasik dengan cara baru:

- **Potensi uner** (*unary potential*, mencerminkan kecocokan nilai kedalaman suatu simpul dengan fiturnya sendiri) dihitung oleh jaringan konvolusi.
- **Potensi pasangan** (*pairwise potential*, mencerminkan seberapa konsisten dua simpul bertetangga seharusnya) dihitung memakai *multi-head attention*: tiap simpul dalam jendela dibandingkan dengan semua simpul lain dalam jendela yang sama, menghasilkan bobot yang menentukan seberapa besar nilai kedalaman simpul tetangga memengaruhi simpul tersebut.

Karena mekanismenya memakai banyak *head* (kepala perhatian paralel, tiap kepala mempelajari pola hubungan berbeda), makalah menyebutnya sebagai "fungsi potensi multi-kepala". Keluaran modul pada tiap level adalah peta kedalaman yang telah disempurnakan, diteruskan ke level berikutnya yang resolusinya lebih tinggi.

### Modul Pyramid Pooling untuk Informasi Global

Karena CRF berjendela hanya menghubungkan simpul dalam jendela yang sama, informasi dari bagian citra yang jauh tidak langsung tersalur. Untuk mengompensasi ini, pada level teratas (resolusi terkasar) ditambahkan modul *pyramid pooling* yang menghimpun rata-rata fitur pada beberapa skala (1, 2, 3, dan 6 bagian citra), menyediakan konteks global sebelum informasi disempurnakan secara lokal di level-level berikutnya.

Diagram berikut merangkum alur bertingkat tersebut:

```
citra RGB
   │  Swin Transformer (encoder)
   ▼
fitur level-4 (kasar, petak 32x32) ── Pyramid Pooling (konteks global)
   │  Neural Window FC-CRF (jendela 7x7 petak)
   ▼  upsample
fitur level-3 (petak 16x16)
   │  Neural Window FC-CRF
   ▼  upsample
fitur level-2 (petak 8x8)
   │  Neural Window FC-CRF
   ▼  upsample
fitur level-1 (halus, petak 4x4)
   │  Neural Window FC-CRF
   ▼
peta kedalaman akhir
```

Tiap panah turun menandai penyempurnaan resolusi (*upsample*) sekaligus penerapan CRF berjendela baru pada level yang lebih halus; hasilnya adalah peta kedalaman yang secara bertahap makin tajam pada batas objek.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua tolok ukur utama: NYU Depth v2 (adegan indoor, kedalaman metrik hingga sekitar 10 meter) dan KITTI *Eigen split* (adegan jalan raya outdoor, pembagian data standar yang diperkenalkan Eigen dkk.). Metrik yang dilaporkan meliputi AbsRel (*Absolute Relative error*, rata-rata selisih absolut relatif terhadap kedalaman sebenarnya — makin kecil makin baik), RMSE (*Root Mean Square Error*, akar rata-rata kuadrat galat dalam satuan meter), log10 (galat pada skala logaritmik), dan δ<1,25 (persentase piksel dengan rasio prediksi-terhadap-kebenaran di bawah ambang 1,25 — makin besar makin baik).

Pada NYU Depth v2, NeWCRFs mencapai AbsRel 0,095, RMSE 0,334, log10 0,041, dan δ<1,25 sebesar 0,922. Sebagai perbandingan, BTS mencatat AbsRel 0,110 dan RMSE 0,392; AdaBins mencatat AbsRel 0,103 dan RMSE 0,364; DPT mencatat AbsRel 0,110 dan RMSE 0,357. Artinya, NeWCRFs menurunkan AbsRel sekitar 8–14% relatif terhadap ketiga metode tersebut sekaligus memperbaiki RMSE, menunjukkan prediksi yang secara konsisten lebih dekat ke kedalaman sebenarnya, bukan hanya unggul pada satu metrik.

Pada KITTI *Eigen split*, NeWCRFs mencapai AbsRel 0,052 dan RMSE 2,129 meter, dibandingkan BTS (AbsRel 0,059, RMSE 2,756), AdaBins (AbsRel 0,058, RMSE 2,360), dan DPT (AbsRel 0,062, RMSE 2,573). Selisih RMSE terhadap AdaBins, metode pembanding terbaik pada baris ini, sekitar 0,23 meter atau sekitar 10% relatif — cukup besar untuk adegan outdoor berskala puluhan meter. NeWCRFs juga tercatat menempati peringkat pertama pada papan peringkat daring (*online benchmark*) KITTI depth pada periode Oktober 2021–Maret 2022.

Selain dua tolok ukur utama tersebut, makalah menguji metode pada MatterPort3D, kumpulan data citra panorama indoor, dan melaporkan hasil yang melampaui metode estimasi kedalaman panorama sebelumnya — menunjukkan modul CRF berjendela dapat diadaptasi ke proyeksi citra yang berbeda dari citra perspektif standar.

## Kelebihan dan Keterbatasan

Kelebihan utama NeWCRFs adalah menyatukan prinsip klasik CRF — konsistensi spasial antarsimpul bertetangga — dengan efisiensi komputasi Transformer berjendela, sehingga optimisasi CRF dapat dilatih *end-to-end* tanpa tahap pasca-pemrosesan terpisah. Struktur bertingkat dari kasar ke halus memungkinkan model menangkap konteks luas pada level atas (dibantu *pyramid pooling*) sekaligus detail batas objek pada level bawah. Hasil pada tiga dataset berbeda (indoor, outdoor, panorama) menunjukkan mekanismenya cukup umum untuk beragam domain citra.

Dari sisi rekayasa, ketergantungan pada Swin Transformer sebagai *encoder* membuat model relatif berat dibandingkan arsitektur konvolusi murni seperti BTS, sehingga kebutuhan memori dan waktu inferensi lebih tinggi — makalah tidak menonjolkan perbandingan kecepatan sebagai kontribusi utamanya. Secara konseptual, metode ini tetap sepenuhnya tersupervisi: pelatihan membutuhkan label kedalaman padat dari sensor (LiDAR untuk KITTI, sensor Kinect untuk NYU Depth v2), berbeda dari pendekatan *self-supervised* yang belajar dari konsistensi antar-*frame* video atau pasangan stereo tanpa label kedalaman langsung. Fokus makalah juga murni pada estimasi kedalaman tunggal, tanpa menjadikan kedalaman sebagai bagian dari sistem multitugas.

## Kaitan dengan Bab Lain

NeWCRFs memakai Swin Transformer (bab 025) sebagai *encoder*, mewarisi mekanisme *window attention* Swin dan menerapkannya kembali dengan interpretasi baru sebagai penghitung potensi pasangan CRF — perluasan konseptual dari penggunaan Swin murni sebagai pengklasifikasi atau pendeteksi. Dibandingkan dengan metode estimasi kedalaman lain pada klaster yang sama, ZoeDepth (bab 176) dan Metric3D (bab 177) berfokus pada generalisasi metrik lintas domain memakai *backbone* dan strategi pelatihan berbeda, sedangkan Depth Anything V2 (bab 175) menekankan skala data pelatihan yang sangat besar dan distilasi dari model guru. Marigold (bab 178) mengambil pendekatan berbeda secara mendasar, memakai model difusi yang awalnya dilatih untuk sintesis citra. NeWCRFs berkontribusi pada garis penelitian ini dengan menunjukkan bahwa komponen klasik seperti CRF masih dapat memberi perbaikan terukur ketika diimplementasikan ulang sebagai lapisan *neural network* yang dapat dilatih, bukan sebagai tahap pasca-pemrosesan terpisah — gagasan yang relevan dibandingkan dengan pendekatan berbasis *backbone* besar atau difusi pada bab-bab lain di klaster Estimasi Kedalaman.

## Poin untuk Sitasi

Kutip dengan kunci `yuan2022newcrfs`. Ringkasan aman: "NeWCRFs merumuskan estimasi kedalaman monokular sebagai optimisasi CRF *fully-connected* yang dihitung per jendela citra memakai *multi-head attention*, dengan Swin Transformer sebagai *encoder* dan struktur dekoder *bottom-up-top-down* empat level, mencapai kinerja *state-of-the-art* pada NYU Depth v2 dan KITTI saat dipublikasikan pada CVPR 2022." Angka hasil (NYU: AbsRel 0,095, RMSE 0,334, log10 0,041, δ<1,25 0,922; KITTI: AbsRel 0,052, RMSE 2,129, δ<1,25 0,974) dan angka pembanding BTS/AdaBins/DPT diperoleh dari ringkasan tabel hasil makalah via sumber sekunder (bukan pembacaan langsung tabel PDF asli) — sebaiknya diverifikasi ulang terhadap Tabel 1 dan Tabel 2 naskah asli sebelum dikutip dalam karya formal. Ukuran varian Swin Transformer yang dipakai untuk hasil utama (Tiny/Base/Large) tidak berhasil dipastikan dari sumber yang diakses dan perlu dicek langsung ke naskah.
