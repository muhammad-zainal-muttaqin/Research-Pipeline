# 169 - CAVER: Cross-Modal View-Mixed Transformer for Bi-Modal Salient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pang2023caver` |
| Judul asli | CAVER: Cross-Modal View-Mixed Transformer for Bi-Modal Salient Object Detection |
| Penulis | Youwei Pang, Xiaoqi Zhao, Lihe Zhang, Huchuan Lu |
| Tahun | 2023 |
| Venue | IEEE Transactions on Image Processing (TIP), vol. 32, hlm. 892–904 |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2112.02363
- **Kode sumber:** https://github.com/lartpang/CAVER
- **Google Scholar:** https://scholar.google.com/scholar?q=CAVER%3A%20Cross-Modal%20View-Mixed%20Transformer%20for%20Bi-Modal%20Salient%20Object%20Detection

## Gambaran Umum

Makalah ini mengusulkan CAVER (*Cross-Modal View-Mixed Transformer*), kerangka kerja untuk *salient object detection* (SOD) dwi-modal — tugas menandai piksel objek paling menonjol pada citra, dibantu satu modalitas kedua selain warna RGB (baik peta kedalaman/*depth* maupun citra termal). Alih-alih menyusun modul fusi konvolusi terpisah untuk RGB-D dan RGB-T seperti kebanyakan metode sebelumnya, CAVER memakai satu jalur dekoder berbasis *transformer* (arsitektur berbasis mekanisme *self-attention*, yang menghitung bobot relevansi antar seluruh pasangan elemen fitur, bukan hanya tetangga lokal) yang sama untuk kedua kombinasi modalitas.

Gagasan intinya adalah memandang penggabungan fitur multiskala dan multimodal sebagai proses propagasi konteks berurutan (*sequence-to-sequence*), dijalankan lewat mekanisme *view-mixed attention* (VMA) yang menggabungkan atensi spasial dan atensi kanal. Pada evaluasi rata-rata tujuh dataset benchmark RGB-D, varian CAVER dengan *backbone* ResNet-101 melaporkan S-measure 0,912, hasil yang menurut makalah lebih tinggi daripada TriTransNet — pembanding transformer sezaman — sekaligus menuntut biaya komputasi jauh lebih rendah, sekitar 44,4 GFLOPs berbanding 680 GFLOPs pada varian ResNet-50.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Metode RGB-D SOD berbasis jaringan konvolusi (CNN) yang mendominasi periode 2019–2021 — termasuk pendekatan fusi bercabang seperti pada bab 168 (SPNet) — mengandalkan operasi konvolusi untuk menyatukan fitur RGB dan *depth*. Konvolusi bersifat lokal: setiap unit keluaran hanya melihat wilayah kecil di sekitarnya (ditentukan ukuran kernel), sehingga jaringan perlu ditumpuk banyak lapis agar memperoleh konteks yang lebih luas. Keterbatasan ini menyulitkan model menangkap ketergantungan jarak jauh antar wilayah citra yang saling terpisah tetapi relevan bagi keputusan salien-tidaknya suatu objek.

Masalah kedua bersifat arsitektural: metode RGB-D dan metode RGB-T (menggunakan citra termal alih-alih *depth*) umumnya dirancang sebagai dua kerangka kerja terpisah, masing-masing dengan modul fusi khusus yang disesuaikan tangan untuk karakteristik modalitas keduanya. Padahal secara struktural kedua tugas serupa: keduanya menggabungkan RGB dengan satu kanal informasi tambahan bernilai tunggal per piksel. Kebutuhan merancang ulang modul fusi untuk setiap kombinasi modalitas membuat metode sulit digeneralisasi dan mahal dari sisi rekayasa.

Pada saat yang sama, model *transformer* penuh (tanpa komponen konvolusi) yang dipakai pada tugas visi lain memiliki kompleksitas komputasi yang tumbuh kuadratik terhadap jumlah token — pada citra beresolusi tinggi dengan token per piksel, biaya atensi menjadi sangat mahal. Metode transformer awal untuk SOD, seperti TriTransNet, mengatasi hal ini dengan menumpuk banyak lapis atensi penuh, sehingga biaya GFLOPs dan jumlah parameternya membengkak dibandingkan metode berbasis CNN.

## Ide Utama

CAVER memperlakukan integrasi fitur multiskala dan multimodal sebagai satu rangkaian pembaruan konteks berurutan yang dijalankan oleh unit-unit atensi yang sama, bukan modul fusi khusus per modalitas. Fitur RGB dan fitur modalitas kedua (*depth* atau termal) diekstraksi terpisah oleh *backbone* konvolusi (ResNet), kemudian keduanya dipertemukan pada dekoder melalui lapisan-lapisan atensi yang menukar informasi antar-modalitas dan antar-skala secara eksplisit.

Komponen penukar informasi itu adalah *view-mixed attention* (VMA): satu modul atensi yang menghitung dua jenis hubungan sekaligus dan menjumlahkannya dengan bobot yang dipelajari. Cabang pertama, atensi spasial, menghitung relevansi antar-lokasi pada peta fitur — mekanisme *self-attention* baku yang mencari lokasi mana yang saling memengaruhi. Cabang kedua, atensi kanal, memperlakukan setiap kanal fitur sebagai satu elemen urutan dan menghitung relevansi antar-kanal, menangkap hubungan yang tidak bergantung posisi spasial. Dua bobot terlatih, disebut α dan β pada makalah, menggabungkan keluaran kedua cabang secara adaptif alih-alih menjumlahkannya secara tetap.

Untuk menekan biaya komputasi atensi penuh pada peta fitur beresolusi tinggi, makalah menambahkan *patch-wise token re-embedding* (PTRE): sekumpulan token per piksel diagregasi menjadi token per tambalan (*patch*) berukuran p×p sebelum masuk ke lapisan atensi, menurunkan jumlah token — dan karenanya biaya atensi kuadratik — sebesar faktor p². Dengan p = 8, misalnya, peta fitur 64×64 (4.096 token per piksel) menyusut menjadi 8×8 (64 token per tambalan) sebelum dihitung atensinya, lalu dikembalikan ke resolusi asal setelah pembaruan konteks selesai.

## Cara Kerja Langkah demi Langkah

### Encoder Dua Aliran

CAVER memakai dua *backbone* ResNet (varian ResNet-50 atau ResNet-101, keduanya dilatih awal pada ImageNet-1K) yang berjalan paralel: satu menerima citra RGB tiga kanal, satu lagi menerima citra modalitas kedua (peta *depth* atau citra termal, direplikasi menjadi tiga kanal bila perlu). Setiap *backbone* menghasilkan fitur pada empat tingkat resolusi berbeda (dari resolusi tinggi/detail halus ke resolusi rendah/konteks luas), sehingga tersedia pasangan fitur RGB dan modalitas kedua pada tiap skala.

### Unit Interaksi Lintas-Modal (CMIU)

Empat skala fitur tersebut diproses oleh empat *Cross-Modal Interaction Unit* (CMIU) yang disusun berjenjang dari skala kasar ke skala halus, membentuk jalur propagasi informasi bernama *Transformer Information Propagation Path* (TIPP). Tiap CMIU terdiri atas tiga tahap atensi berurutan:

1. **Atensi mandiri intra-modal (IMSA)** — VMA diterapkan pada fitur RGB terhadap dirinya sendiri, dan pada fitur modalitas kedua terhadap dirinya sendiri, memperkuat konteks internal masing-masing modalitas sebelum digabung.
2. **Atensi silang antar-modal (IMCA)** — VMA diterapkan lintas-modal: fitur RGB dipakai sebagai kueri (*query*) terhadap fitur modalitas kedua sebagai kunci-nilai (*key-value*), dan sebaliknya, sehingga tiap modalitas dapat "bertanya" ke modalitas lain bagian mana yang relevan.
3. **Atensi mandiri lintas-skala (CSSA)** — fitur hasil tahap sebelumnya pada skala saat ini digabung dengan fitur terpropagasi dari skala yang lebih kasar (keluaran CMIU sebelumnya), sehingga informasi konteks global dari resolusi rendah ikut menyempurnakan detail pada resolusi lebih tinggi.

Keluaran tiap CMIU diteruskan ke jaringan umpan-maju konvolusional (*Conv-FFN*), yaitu blok umpan-maju yang biasanya berupa dua lapisan linear penuh pada transformer standar, di sini digantikan konvolusi kecil agar tetap menangkap detail tekstur lokal yang cenderung hilang pada atensi murni. Pada makalah, varian dengan Conv-FFN dilaporkan mengungguli varian umpan-maju linear biasa.

Diagram berikut merangkum alur satu CMIU pada satu tingkat skala:

```
fitur RGB skala-i        fitur modal-2 skala-i     fitur dari CMIU
      │                          │                  skala lebih kasar
      ▼                          ▼                          │
  ┌───────┐                 ┌───────┐                        │
  │ IMSA  │ (VMA-mandiri)   │ IMSA  │ (VMA-mandiri)           │
  └───┬───┘                 └───┬───┘                        │
      └───────────┬─────────────┘                            │
                   ▼                                          │
              ┌─────────┐                                     │
              │  IMCA   │  atensi silang RGB <-> modal-2       │
              └────┬────┘                                     │
                   ▼                                          │
              ┌─────────┐                                     │
              │  CSSA   │◄────────────────────────────────────┘
              └────┬────┘  gabung dgn konteks skala kasar
                   ▼
              ┌─────────┐
              │Conv-FFN │  penguat detail lokal
              └────┬────┘
                   ▼
         fitur tergabung skala-i
```

### Dekoder dan Prediksi Akhir

Keluaran CMIU pada skala paling halus, setelah menerima kontribusi seluruh skala di atasnya melalui CSSA, diteruskan ke kepala prediksi yang menghasilkan peta saliensi satu kanal berukuran sama dengan citra masukan. Pelatihan memakai fungsi *loss* gabungan piksel dan struktur, mengikuti praktik umum pada metode SOD terbaru, agar batas objek yang diprediksi selaras dengan batas objek pada label kebenaran.

## Eksperimen dan Hasil

Evaluasi RGB-D SOD memakai tujuh dataset benchmark standar bidang ini: NJUD, NLPR, SIP, STEREO1000, SSD, LFSD, dan DUT-RGBD, masing-masing berisi pasangan citra RGB dan peta *depth* dengan label saliensi piksel demi piksel. Evaluasi RGB-T SOD memakai tiga dataset citra termal: VT821, VT1000, dan VT5000-TE. Empat metrik dipakai secara konsisten: S-measure (kemiripan struktural antara peta prediksi dan kebenaran, memperhitungkan wilayah maupun objek), F-measure berbobot (harmonisasi presisi dan *recall* dengan pembobotan spasial), E-measure (kesesuaian pada tingkat piksel sekaligus citra secara keseluruhan), dan MAE (*mean absolute error*, selisih rata-rata absolut antara nilai piksel prediksi dan kebenaran, dengan nilai lebih rendah lebih baik).

Pada rata-rata tujuh dataset RGB-D, varian CAVER dengan *backbone* ResNet-101 melaporkan S-measure 0,912, F-measure berbobot 0,886, E-measure 0,947, dan MAE 0,035. Makalah menyatakan hasil ini mengungguli TriTransNet, pembanding berbasis transformer yang dirilis pada periode berdekatan, dengan selisih S-measure sekitar satu poin persentase. Pada dataset RGB-T VT821, varian ResNet-101 melaporkan S-measure 0,898, F-measure berbobot 0,845, dan MAE 0,027 — menunjukkan kerangka yang sama, tanpa modifikasi arsitektur, tetap kompetitif pada modalitas termal.

Dari sisi efisiensi, varian ResNet-50 (Ours50) dilaporkan membutuhkan 44,4 GFLOPs dan 55,8 juta parameter dengan kecepatan inferensi 35,2 *frame* per detik (FPS), dibandingkan TriTransNet yang membutuhkan 680 GFLOPs dan 139,5 juta parameter pada 10,2 FPS. Selisih ini menunjukkan PTRE dan desain atensi ganda VMA berhasil menekan biaya komputasi tanpa kehilangan akurasi terhadap pembanding transformer penuh — argumen inti makalah bahwa reduksi token per tambalan lebih efektif daripada menumpuk lapisan atensi murni.

Studi ablasi pada makalah menunjukkan setiap komponen berkontribusi: menonaktifkan IMCA menurunkan S-measure dari 0,909 menjadi 0,905 pada pengujian internal, mengindikasikan atensi silang antar-modal berperan signifikan dalam fusi; kombinasi IMSA dan CSSA bersama-sama diperlukan untuk mencapai S-measure puncak 0,909, lebih tinggi daripada memakai salah satunya; serta ukuran tambalan 8×8 dilaporkan sebagai titik seimbang terbaik antara efisiensi dan akurasi dibandingkan ukuran lain yang diuji.

## Kelebihan dan Keterbatasan

Kelebihan utama CAVER adalah kesatuan arsitektur: satu kerangka dekoder berbasis atensi menangani RGB-D maupun RGB-T tanpa modul fusi khusus per modalitas, mengurangi kebutuhan rekayasa ulang saat berpindah tugas. Desain VMA yang memisahkan atensi spasial dan kanal, dipadu PTRE, memberi efisiensi komputasi yang jauh lebih baik daripada transformer penuh sezaman sambil tetap unggul pada metrik akurasi standar bidang ini.

Dari sisi konseptual, kerangka ini tetap bergantung pada *backbone* CNN (ResNet) untuk ekstraksi fitur awal — bukan transformer murni dari awal hingga akhir — sehingga keterbatasan lokalitas konvolusi pada tahap awal ekstraksi fitur belum sepenuhnya teratasi, hanya dipindahkan tanggung jawabnya ke tahap fusi pada dekoder. Makalah sendiri melaporkan tiga kategori kegagalan: batas objek yang ambigu pada citra dengan tekstur kompleks, definisi saliensi yang tidak konsisten antar-dataset (objek yang dianggap salien pada satu dataset belum tentu demikian pada dataset lain), dan label kebenaran yang tidak selaras atau tidak lengkap pada sebagian data uji. Dari sisi rekayasa, dua aliran *backbone* paralel tetap menggandakan biaya ekstraksi fitur awal dibandingkan pendekatan satu aliran, dan kualitas keluaran tetap bergantung pada kualitas modalitas kedua — peta *depth* yang berderau atau citra termal bernoise berpotensi menurunkan hasil fusi, sekalipun mekanisme atensi memberi model peluang lebih besar untuk menekan kontribusi wilayah tidak andal dibandingkan fusi konvolusi tetap.

## Kaitan dengan Bab Lain

CAVER berada pada klaster RGB-D SOD bersama bab 166 (CoNet), bab 167 (DCF), bab 168 (SPNet), dan bab 170 (MobileSal); keempatnya mengatasi masalah fusi RGB-D dengan pendekatan berbeda — CoNet lewat pembelajaran kolaboratif, DCF lewat kalibrasi *depth*, SPNet lewat pemisahan cabang spesifik-modal (lihat bab 168) — sementara CAVER menjawabnya dengan mekanisme atensi lintas-modal yang eksplisit menggantikan konvolusi fusi. Perbandingan langsung dengan bab 168 relevan karena keduanya berangkat dari kritik yang sama terhadap fusi konvolusi tunggal, tetapi menempuh jalan berlawanan: SPNet menambah cabang arsitektural, CAVER mengganti mekanisme fusinya.

Dari sisi silsilah teknik, penggunaan *self-attention* dan struktur *encoder-decoder* berbasis atensi pada CAVER mewarisi prinsip yang sama dengan bab 165 (Co-DETR) dan keluarga *Vision Transformer* pada klaster fondasi transformer: kedua jalur menggantikan operasi lokal konvolusi dengan penghitungan relevansi global antar-token, hanya diterapkan pada tugas berbeda (deteksi objek kelas umum pada Co-DETR, segmentasi saliensi dwi-modal pada CAVER). Prinsip *patch-wise token re-embedding* pada CAVER juga sejalan dengan strategi reduksi token pada *backbone* transformer hierarkis seperti PVT, yang membagi citra menjadi tambalan bertahap untuk menekan biaya atensi pada resolusi tinggi.

## Poin untuk Sitasi

Kutip dengan kunci `pang2023caver`. Ringkasan yang aman dikutip: "CAVER mengusulkan *view-mixed attention* yang menggabungkan atensi spasial dan kanal untuk menyatukan penanganan RGB-D dan RGB-T SOD dalam satu kerangka dekoder berbasis transformer, melaporkan S-measure rata-rata 0,912 pada tujuh dataset RGB-D dengan biaya komputasi jauh lebih rendah daripada TriTransNet." Angka S-measure 0,912, F-measure berbobot 0,886, E-measure 0,947, MAE 0,035 (rata-rata RGB-D), hasil VT821 (S-measure 0,898), serta angka efisiensi 44,4 GFLOPs/55,8 juta parameter/35,2 FPS diambil dari pemrosesan naskah arXiv versi HTML (ar5iv) dan perlu dicocokkan ulang dengan tabel resmi pada versi IEEE TIP (vol. 32, hlm. 892–904, DOI 10.1109/TIP.2023.3234702) sebelum dikutip dalam karya formal. Rincian ablasi (S-measure 0,905 tanpa IMCA, 0,909 dengan IMSA+CSSA) juga berasal dari pemrosesan sumber sekunder dan memerlukan verifikasi ke tabel ablasi asli.
