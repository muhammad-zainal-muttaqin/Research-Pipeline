# 168 - Specificity-Preserving RGB-D Saliency Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2021spnet` |
| Judul asli | Specificity-preserving RGB-D Saliency Detection |
| Penulis | Tao Zhou, Huazhu Fu, Geng Chen, Yi Zhou, Deng-Ping Fan, Ling Shao |
| Tahun | 2021 |
| Venue | IEEE/CVF International Conference on Computer Vision (ICCV 2021) |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2108.08162
- **Kode sumber (GitHub):** https://github.com/taozh2017/SPNet
- **Google Scholar:** https://scholar.google.com/scholar?q=Specificity-preserving%20RGB-D%20Saliency%20Detection

## Gambaran Umum

Makalah ini memperkenalkan SPNet (*Specificity-Preserving Network*), jaringan untuk *salient object detection* (SOD) berbasis RGB-D — tugas menandai piksel objek paling menonjol pada citra dengan bantuan peta kedalaman (*depth map*, citra yang tiap pikselnya menyatakan jarak permukaan ke kamera). Masalah yang disasar adalah kecenderungan metode fusi RGB-D sebelumnya menyatukan kedua modalitas terlalu dini sehingga ciri yang hanya muncul pada salah satu modalitas ikut hilang. SPNet menambahkan dua jaringan khusus modalitas (*modality-specific*) di samping jaringan bersama (*shared*), lalu menggabungkan ketiganya melalui dua modul baru: *Cross-Enhanced Integration Module* (CIM) dan *Multi-Modal Feature Aggregation* (MFA). Pada enam tolok ukur RGB-D SOD standar, SPNet dengan *backbone* (jaringan tulang punggung ekstraksi fitur) Res2Net-50 mencapai *S-measure* 0,925–0,945 dan MAE serendah 0,014–0,044 tergantung dataset, unggul dari rangkaian metode berbasis CNN sebelumnya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

SOD RGB tunggal kesulitan pada kasus objek yang warnanya menyatu dengan latar belakang atau tekstur latarnya rumit. Peta kedalaman membantu karena batas objek sering bersesuaian dengan lompatan jarak kamera, sehingga banyak metode SOD generasi 2018–2020 (di antaranya CoNet pada bab 166 dan DCF pada bab 167) menambahkan cabang depth dan menggabungkannya dengan cabang RGB melalui berbagai skema fusi — di tahap awal (*early fusion*), tahap fitur tengah (*middle fusion*), atau tahap keputusan akhir (*late fusion*). Sebagian besar skema ini memakai satu jaringan gabungan atau satu titik pertemuan fitur untuk mempelajari representasi bersama kedua modalitas.

Masalahnya, proses menyatukan fitur RGB dan depth ke satu representasi bersama cenderung menghilangkan informasi yang hanya berguna untuk satu modalitas. Sebagai misal, tekstur warna hanya bermakna pada cabang RGB dan tidak punya padanan pada peta kedalaman; sebaliknya, kontinuitas jarak hanya bermakna pada cabang depth. Bila kedua fitur ini dipaksa berbagi satu ruang representasi sejak awal, sinyal yang spesifik pada satu modalitas dapat teredam oleh sinyal modalitas lain yang lebih dominan pada lokasi tertentu. Makalah ini berangkat dari pengamatan bahwa metode-metode sebelumnya jarang secara eksplisit menjaga fitur spesifik-modal ini tetap tersedia untuk prediksi akhir.

## Ide Utama

Gagasan inti SPNet adalah memisahkan pembelajaran fitur menjadi tiga aliran paralel, bukan satu: satu aliran khusus RGB, satu aliran khusus depth, dan satu aliran bersama yang mempelajari representasi gabungan. Ketiga aliran berbagi *encoder* (bagian jaringan yang mengekstrak fitur dari citra masukan) yang sama, tetapi masing-masing memiliki *decoder* (bagian yang merekonstruksi peta saliency dari fitur) sendiri. Dengan begitu, aliran RGB tetap dapat mempelajari isyarat warna dan tekstur tanpa gangguan depth, aliran depth tetap mempelajari isyarat jarak tanpa gangguan warna, sedangkan aliran bersama tetap menangkap korelasi lintas-modal.

Ketiga aliran ini tidak berjalan terisolasi. CIM menyuntikkan informasi silang antar-modalitas ke aliran bersama pada tiap tingkat *encoder*, sementara MFA mengambil fitur dari kedua *decoder* spesifik-modal dan menggabungkannya ke dalam *decoder* bersama sebelum peta saliency akhir diproduksi. Prediksi akhir yang dipakai sebagai keluaran sistem berasal dari *decoder* bersama, yang pada tahap ini sudah diperkaya oleh informasi spesifik dari kedua modalitas melalui MFA.

## Cara Kerja Langkah demi Langkah

### Backbone dan ekstraksi fitur multiskala

SPNet memakai Res2Net-50 yang telah dilatih awal (*pretrained*) pada ImageNet sebagai *backbone* untuk kedua modalitas. Res2Net adalah varian ResNet yang memecah setiap blok residual menjadi beberapa kelompok kanal yang saling terhubung bertingkat, sehingga satu blok dapat menangkap fitur pada beberapa skala reseptif sekaligus. Citra RGB dan peta kedalaman masing-masing dilewatkan melalui *backbone* terpisah, menghasilkan lima tingkat fitur dengan resolusi spasial menurun dari H/8×W/8 hingga H/32×W/32 dan jumlah kanal 64, 256, 512, 1024, dan 2048 berturut-turut (H dan W adalah tinggi dan lebar citra masukan).

### Tiga aliran paralel

Dari fitur *backbone* tersebut, jaringan membangun tiga cabang: cabang khusus RGB memproses fitur RGB saja menuju *decoder*-nya sendiri; cabang khusus depth memproses fitur depth saja menuju *decoder* terpisah; cabang bersama memproses gabungan fitur RGB dan depth pada tiap tingkat menuju *decoder* ketiga. Ketiga *decoder* memakai koneksi lompat (*skip connection*) standar arsitektur *encoder-decoder*: fitur tingkat rendah beresolusi tinggi digabung dengan fitur tingkat tinggi yang telah diperbesar (*upsampling*), sehingga detail tepi objek tidak hilang di tengah proses.

### Cross-Enhanced Integration Module (CIM)

CIM ditempatkan pada tiap tingkat *encoder* untuk memperkaya fitur yang mengalir ke cabang bersama. Modul ini mengambil fitur RGB dan fitur depth pada tingkat yang sama, saling memperkuat keduanya melalui operasi perkalian dan penjumlahan berbobot, lalu meneruskan hasilnya ke tingkat berikutnya dalam cabang bersama. Dengan cara ini, informasi lintas-modal dipropagasikan secara bertahap dari tingkat fitur rendah ke tinggi, bukan digabung sekaligus di satu titik seperti pada skema fusi lama.

### Multi-Modal Feature Aggregation (MFA)

MFA bekerja pada sisi *decoder*. Modul ini mengambil fitur dari *decoder* khusus RGB dan *decoder* khusus depth pada tingkat yang bersesuaian, kemudian menggabungkannya ke dalam *decoder* bersama sebagai informasi pelengkap. Karena fitur yang digabung berasal dari *decoder* yang sudah terspesialisasi per modalitas — bukan dari *encoder* mentah — MFA membawa isyarat spesifik-modal yang sudah relevan dengan tugas saliency, bukan sekadar fitur visual umum.

Skema alur data dari dua modalitas masukan hingga peta saliency akhir:

```
RGB  ──► encoder-RGB ─┬─────────────► decoder-RGB ─┐
                       │  (CIM per level)           │
Depth ──► encoder-D ──┴─────────────► decoder-D ────┤
                       │                             │ (MFA)
                       └──► fitur gabungan ──► decoder-shared ──► peta saliency
```

Diagram ini menunjukkan bahwa cabang RGB dan depth tetap menghasilkan peta saliency sendiri-sendiri (dipakai sebagai sinyal pelatihan tambahan), sementara cabang bersama — yang menerima suntikan CIM di sisi *encoder* dan suntikan MFA di sisi *decoder* — menghasilkan peta saliency yang dipakai sebagai keluaran akhir sistem.

### Fungsi pelatihan

Ketiga *decoder* (RGB, depth, bersama) masing-masing diawasi (*supervised*) oleh peta *ground truth* yang sama menggunakan kombinasi *binary cross-entropy loss* dan *IoU loss* (*Intersection-over-Union loss*, mengukur tumpang tindih wilayah prediksi dan wilayah sebenarnya). Pengawasan pada ketiga cabang memaksa cabang RGB dan cabang depth tetap mampu memprediksi saliency secara mandiri, bukan menjadi penampung fitur pasif untuk cabang bersama.

## Eksperimen dan Hasil

Model dilatih pada gabungan 1.485 citra dari NJU2K dan 700 citra dari NLPR (total 2.195 pasangan RGB-depth), lalu diuji pada enam tolok ukur RGB-D SOD: NJU2K (500 citra uji), NLPR (300 citra), STERE (1.000 citra), DES (135 citra), SSD (80 citra), dan SIP (929 citra). Empat metrik dipakai: *S-measure* (Sα, mengukur kemiripan struktural peta saliency dengan *ground truth* pada tingkat wilayah dan objek), *F-measure* maksimum (Fβ, rata-rata harmonik presisi dan *recall* pada ambang optimal), *E-measure* (Eξ, mengukur kesesuaian peta prediksi dengan *ground truth* secara piksel sekaligus global), dan MAE (*Mean Absolute Error*, rata-rata selisih absolut nilai piksel prediksi terhadap *ground truth*, semakin kecil semakin baik).

Hasil pada varian Res2Net-50: Sα 0,925/Fβ 0,935/Eξ 0,954/MAE 0,028 pada NJU2K; Sα 0,907/Fβ 0,915/Eξ 0,944/MAE 0,037 pada STERE; Sα 0,945/Fβ 0,950/Eξ 0,980/MAE 0,014 pada DES; Sα 0,927/Fβ 0,925/Eξ 0,959/MAE 0,021 pada NLPR; Sα 0,871/Fβ 0,883/Eξ 0,915/MAE 0,044 pada SSD; dan Sα 0,894/Fβ 0,916/Eξ 0,930/MAE 0,043 pada SIP. Dibandingkan dengan sekitar dua puluh metode pembanding yang dilatih pada rezim data sama — termasuk JL-DCF, S2MA, UCNet, CoNet, dan D3Net — SPNet mencatat hasil terbaik atau mendekati terbaik pada mayoritas dataset, dengan keunggulan paling jelas pada DES (MAE 0,014, jauh di bawah rata-rata metode pembanding pada rentang 0,02–0,05).

Studi ablasi menunjukkan tiap komponen memberi kontribusi terukur. Menghapus MFA dan menggantinya dengan konkatenasi sederhana menaikkan MAE pada NJU2K dari 0,028 menjadi 0,034 — penurunan akurasi yang berarti untuk metrik bernilai kecil. Menghapus CIM (memakai konkatenasi fitur langsung tanpa penguatan silang) juga menurunkan kinerja pada seluruh dataset uji. Menghapus *decoder* spesifik-modal sepenuhnya — sehingga hanya tersisa cabang bersama — menurunkan akurasi paling signifikan di antara semua varian ablasi, mengonfirmasi klaim inti makalah bahwa mempertahankan cabang spesifik-modal memberi manfaat yang tidak tergantikan oleh cabang bersama saja.

## Kelebihan dan Keterbatasan

Kelebihan utama SPNet adalah pemisahan eksplisit antara pembelajaran fitur spesifik-modal dan fitur bersama, yang terbukti melalui ablasi memberi kontribusi nyata pada akurasi, bukan sekadar penambahan kapasitas jaringan tanpa dasar. Desain CIM dan MFA juga bersifat modular — keduanya dapat dipasang pada *backbone* dan arsitektur *encoder-decoder* lain tanpa perubahan struktural besar. Dari sisi hasil, keunggulan SPNet konsisten pada mayoritas dari enam tolok ukur, bukan hanya satu dataset tunggal, yang menunjukkan generalisasi yang wajar.

Dari sisi rekayasa, tiga aliran paralel dengan tiga *decoder* menambah jumlah parameter dan biaya komputasi dibandingkan arsitektur satu aliran tunggal, meski makalah tidak menonjolkan efisiensi sebagai kontribusi utamanya. Secara konseptual, kinerja SPNet tetap bergantung pada kualitas peta kedalaman masukan; pada dataset dengan depth berderau atau tidak akurat, penguatan silang oleh CIM berisiko menyebarkan kesalahan depth ke cabang bersama alih-alih menyaringnya. Keterbatasan lain adalah pelatihan hanya memakai 2.195 pasangan citra dari dua dataset (NJU2K dan NLPR), jumlah yang relatif kecil untuk jaringan tiga aliran, sehingga generalisasi ke domain di luar enam tolok ukur yang diuji belum tentu terjamin.

## Kaitan dengan Bab Lain

SPNet melanjutkan garis metode fusi RGB-D yang dibahas pada bab 166 (CoNet, fusi kolaboratif RGB-depth) dan bab 167 (DCF, fusi terkalibrasi kedalaman), tetapi mengambil arah berbeda: alih-alih mencari skema fusi tunggal yang lebih baik, SPNet menambahkan jalur pembelajaran terpisah untuk tiap modalitas di samping jalur fusi. Prinsip menjaga fitur spesifik-modal ini relevan untuk dibandingkan dengan bab 169 (CAVER, yang memakai mekanisme *attention* lintas-modal berbasis Transformer) dan bab 170 (MobileSal, yang menekankan efisiensi komputasi pada arsitektur RGB-D ringan) — dua arah pengembangan lanjutan yang menghadapi trade-off berbeda antara akurasi, kompleksitas fusi, dan biaya komputasi yang mulai tampak pada SPNet.

Tautan bab terkait:
- [166 - 2020 - CoNet - RGB-D SOD](./166%20-%202020%20-%20CoNet%20-%20RGB-D%20SOD.md)
- [167 - 2021 - DCF - RGB-D SOD](./167%20-%202021%20-%20DCF%20-%20RGB-D%20SOD.md)
- [169 - 2023 - CAVER - RGB-D SOD](./169%20-%202023%20-%20CAVER%20-%20RGB-D%20SOD.md)
- [170 - 2022 - MobileSal - RGB-D SOD](./170%20-%202022%20-%20MobileSal%20-%20RGB-D%20SOD.md)

## Poin untuk Sitasi

Kutip dengan kunci `zhou2021spnet`. Ringkasan yang aman dikutip: "SPNet mempertahankan cabang pembelajaran khusus RGB dan khusus depth di samping cabang bersama, digabungkan melalui Cross-Enhanced Integration Module dan Multi-Modal Feature Aggregation, dan mencapai S-measure hingga 0,945 serta MAE serendah 0,014 pada enam tolok ukur RGB-D SOD standar dengan backbone Res2Net-50." Angka hasil per dataset (Sα, Fβ, Eξ, MAE pada NJU2K, STERE, DES, NLPR, SSD, SIP) dan angka ablasi (MAE 0,028 → 0,034 tanpa MFA) diambil dari versi teks makalah yang diperoleh melalui ar5iv; kesesuaiannya dengan versi PDF resmi ICCV/CVF sebaiknya dicocokkan ulang sebelum dikutip dalam karya formal, karena laman CVF tidak dapat diakses langsung saat penyusunan bab ini. Daftar lengkap metode pembanding (23 metode) dan detail rumus *loss* sebaiknya juga diverifikasi ke naskah asli.
