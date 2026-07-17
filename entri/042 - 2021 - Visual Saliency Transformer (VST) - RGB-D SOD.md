# 042 - Visual Saliency Transformer

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2021vst` |
| Judul asli | Visual Saliency Transformer |
| Penulis | Nian Liu, Ni Zhang, Kaiyuan Wan, Ling Shao, Junwei Han |
| Tahun | 2021 |
| Venue | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV 2021), hal. 4722–4732 |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2104.12099
- **Repositori kode resmi:** https://github.com/nnizhang/VST
- **Google Scholar:** https://scholar.google.com/scholar?q=Visual%20Saliency%20Transformer
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Visual%20Saliency%20Transformer&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan VST (*Visual Saliency Transformer*), model pertama untuk deteksi objek salien (SOD, *salient object detection* — menandai objek yang paling menarik perhatian pengamat dalam citra sebagai peta biner per piksel) yang dibangun murni dari Transformer, tanpa satu pun lapis konvolusi. Satu kerangka yang sama dipakai untuk dua tugas: SOD pada citra RGB biasa dan SOD pada citra RGB-D, yaitu citra warna yang dilengkapi peta kedalaman (citra yang setiap pikselnya menyatakan jarak permukaan ke kamera).

Masalah yang dipecahkan adalah keterbatasan struktural metode SOD berbasis CNN (*convolutional neural network*): konvolusi hanya melihat jendela lokal, sedangkan menentukan objek salien memerlukan konteks dan kontras global. VST mengganti seluruh alur dengan pemodelan sekuens-ke-sekuens: citra dipotong menjadi *patch* (petak kecil) yang diperlakukan sebagai *token* (unit masukan berupa vektor), dan mekanisme *self-attention* (perhatian-diri: setiap token membobot hubungannya dengan semua token lain) menyebarkan konteks global di setiap lapis. Tiga komponen baru dikembangkan agar Transformer murni menghasilkan prediksi padat beresolusi penuh: *convertor* lintas-modal untuk fusi RGB dan kedalaman, *upsampling* token RT2T, dan *decoder* multi-tugas berbasis token. Hasilnya, VST mengalahkan seluruh metode CNN pembanding pada enam benchmark RGB dan sembilan benchmark RGB-D.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Hingga 2021, metode SOD terdepan — baik untuk RGB maupun RGB-D — sepenuhnya didominasi arsitektur *encoder-decoder* berbasis CNN: *encoder* memadatkan citra menjadi fitur multi-level, *decoder* menggabungkan fitur tersebut menjadi peta saliency. Perbaikan diperoleh dari modul perhatian, integrasi multi-skala, dan pembelajaran multi-tugas; untuk RGB-D ditambah berbagai skema fusi lintas-modal, misalnya strategi percabangan *backbone* pada BBS-Net (bab 036) atau fusi kooperatif pada JL-DCF (bab 038).

Kekurangan yang spesifik terletak pada jangkauan reseptif (*receptive field*) CNN yang lokal, padahal literatur saliency telah lama menunjukkan bahwa konteks dan kontras global menentukan objek mana yang dianggap menonjol. Konvolusi menyusun konteks luas hanya secara tidak langsung, lewat penumpukan banyak lapis; tambahan *global pooling* atau modul *non-local* hanya menyisipkan konteks global di beberapa titik. Masalah kedua bersifat teknis: ViT (*Vision Transformer*) yang mengadaptasi Transformer ke citra dirancang untuk klasifikasi — keluarannya satu label, bukan peta beresolusi tinggi — sehingga belum jelas bagaimana Transformer murni melakukan prediksi padat seperti SOD. Masalah ketiga khusus RGB-D: mekanisme fusi RGB dan kedalaman pada arsitektur Transformer belum pernah dirumuskan.

## Ide Utama

Gagasan inti VST adalah memformulasikan ulang SOD sebagai pemetaan sekuens-ke-sekuens. Citra dibagi menjadi petak-petak, setiap petak diubah menjadi token, dan Transformer menghubungkan semua token satu sama lain di setiap lapis. Dengan demikian ketergantungan jarak jauh — misalnya antara dua ujung objek besar yang terpisah ratusan piksel — dimodelkan secara langsung, sesuatu yang tidak dapat dilakukan konvolusi.

Dua hambatan diatasi dengan dua rancangan. Pertama, untuk prediksi padat diperkenalkan token terkait-tugas (*task-related token*): satu token saliency dan satu token batas disisipkan ke dalam sekuens token petak, dan peta keluaran diperoleh dengan mengukur kemiripan setiap token petak terhadap kedua token tugas tersebut. Kedua, resolusi dipulihkan dengan menaikkan panjang sekuens token secara bertahap memakai RT2T (*reverse token-to-token*), kebalikan dari operasi pemadatan token pada *backbone* T2T-ViT. Khusus RGB-D, satu *encoder* kedua memproses peta kedalaman dan fusi dilakukan lewat perhatian lintas-modal: token RGB dan token kedalaman saling membobot informasi satu sama lain.

## Cara Kerja Langkah demi Langkah

### Tokenisasi dan Encoder T2T-ViT

*Backbone* yang dipakai adalah T2T-ViT_t-14, varian ViT yang memodelkan struktur lokal lewat transformasi T2T (*tokens-to-token*): token-token tetangga digabung menjadi token baru sehingga panjang sekuens menyusut bertahap, dengan pemisahan petak tumpang tindih untuk membawa korespondensi lokal. Tiga langkah pemisahan (ukuran petak 7, 3, 3) menghasilkan token multi-level T1, T2, dan T3 dengan panjang H/4×W/4, H/8×W/8, dan H/16×W/16 untuk citra masukan H×W. Dimensi embedding token 64; T3 kemudian diproyeksikan ke 384 dan ditambah *position embedding* (penanda posisi) sinusoidal, lalu empat belas lapis Transformer memodelkan ketergantungan global di antara token T3. Pada masukan 224×224, T3 berisi 14×14 = 196 token, sehingga setiap token mewakili wilayah 16×16 piksel.

Untuk RGB, hanya satu *encoder* dipakai. Untuk RGB-D, arsitektur dua aliran dipakai: *encoder* kedua yang identik mengekstrak token dari peta kedalaman yang dinormalisasi ke [0,1] dan diduplikasi menjadi tiga kanal.

### Convertor dan Cross Modality Transformer

*Convertor* mengubah token dari ruang *encoder* ke ruang *decoder*. Pada model RGB, modul ini berisi empat lapis Transformer standar. Pada model RGB-D, dipakai CMT (*Cross Modality Transformer*): empat pasangan lapis yang bergantian antara *cross-modality-attention* dan *self-attention*. Pada *cross-modality-attention*, *query* (vektor pertanyaan) dari token RGB dihadapkan ke *key* (vektor indeks) dan *value* (vektor isi) dari token kedalaman, dan sebaliknya, sehingga setiap modalitas menyerap informasi pelengkap dari modalitas lainnya. Setelah empat kali pertukaran, token RGB dan token kedalaman digabungkan lewat konkatenasi (penyambungan) dan diproyeksikan menjadi token hasil konversi.

### RT2T: Upsampling Token

Panjang token 1/16 resolusi terlalu kasar untuk prediksi padat. Alih-alih *upsampling* bilinear seperti pada metode CNN, VST memperkenalkan RT2T: setiap token diproyeksikan dari dimensi 384 ke 64, lalu diperluas menjadi vektor berdimensi 64×k², ditafsirkan sebagai petak k×k dengan tumpang tindih, dan dilipat kembali menjadi peta yang lebih besar — kebalikan persis dari langkah *soft split* pada T2T. Tiga langkah RT2T (ukuran petak 3, 3, 7) mengembalikan panjang sekuens dari H/16×W/16 ke H×W penuh. Selama proses ini, token tingkat rendah T2 dan T1 dari *encoder* RGB difusikan lewat konkatenasi dan proyeksi linier diikuti satu lapis Transformer, untuk memasok detail tepi yang hilang pada token dalam.

### Decoder Multi-Tugas Berbasis Token

Pada setiap level *decoder*, dua token tugas — token saliency dan token batas — disisipkan pada sekuens token petak dan ikut diproses beberapa lapis Transformer (empat lapis di level terdalam, dua lapis di dua level berikutnya), lalu dibawa ke level berikutnya untuk diperbarui lagi. Keluaran diperoleh lewat *patch-task-attention*: token petak menjadi *query*, token tugas menjadi satu-satunya *key* dan *value*, dan karena hanya ada satu *key*, fungsi aktivasi *sigmoid* dipakai menggantikan *softmax*. Hasilnya dinaikkan ke resolusi penuh oleh RT2T ketiga dan diproyeksikan linier ke skalar [0,1], membentuk peta saliency dan peta batas objek. Kebenaran dasar (*ground truth*) batas dibuat dari peta saliency memakai operator Sobel (penapis deteksi tepi), dan supervisi dalam (*deep supervision*) diterapkan di setiap level *decoder*.

Alur lengkap model:

```
citra RGB 224x224                 peta depth 224x224 (khusus RGB-D)
      │                                  │
      ▼                                  ▼
┌───────────────┐                ┌───────────────┐
│ Encoder       │                │ Encoder depth │
│ T2T-ViT-14    │                │ T2T-ViT-14    │
│ T1 T2 T3      │                └──────┬────────┘
└─┬────┬────┬───┘                       │
  │    │    │ T3 (196 token)            │ T3 depth
  │    │    └────────┐    ┌─────────────┘
  │    │             ▼    ▼
  │    │      ┌─────────────────┐   RGB: convertor = 4 lapis
  │    │      │ Convertor / CMT │   Transformer biasa;
  │    │      │ attention RGB<->│   RGB-D: cross-modality
  │    │      │ depth, x4       │   attention, x4
  │    │      └───────┬─────────┘
  │    │              │ token terkonversi
  │    │   ┌──────────▼──────────────────────────┐
  │    │   │ Decoder multi-tugas:                │
  │    └───┤ RT2T upsampling x3, fusi T2 dan T1  │
  └────────┤ token saliency + token batas,       │
           │ patch-task-attention (sigmoid)      │
           └──────┬────────────────┬─────────────┘
                  ▼                ▼
        peta saliency HxW   peta batas objek HxW
```

Diagram di atas menunjukkan alur data VST: token multi-level dari *encoder* T2T-ViT (dengan cabang kedalaman untuk RGB-D) disatukan di *convertor*, lalu *decoder* memulihkan resolusi sekaligus memisahkan dua tugas prediksi.

## Eksperimen dan Hasil

Model RGB dilatih pada himpunan latih DUTS (10.553 citra); model RGB-D dilatih pada 2.985 pasangan citra gabungan NJUD, NLPR, dan DUTLF-Depth. Masukan di-*crop* acak 224×224; pelatihan memakai pengoptimal Adam dengan fungsi loss *binary cross entropy* untuk kedua tugas, pada satu GPU GTX 1080 Ti. Evaluasi memakai empat metrik baku SOD: S-measure (kemiripan struktur peta), F-measure maksimum (keseimbangan *precision-recall*), E-measure maksimum (keselarasan tingkat piksel dan citra), dan MAE (galat absolut rata-rata).

Pada RGB-D SOD, VST dibandingkan dengan 14 metode CNN terdepan di sembilan dataset. Pada NJUD, S-measure VST 0,922, mengungguli pembanding terbaik BBS-Net (0,921) dengan selisih tipis. Pada dataset yang lebih baru marginnya lebih besar: DUTLF-Depth 0,943 melawan 0,923 (CoNet, terbaik kedua), LFSD 0,882 melawan 0,856 (UC-Net), dan SIP 0,904 melawan 0,886 (HDFNet). Pada ReDWeb-S — dataset dengan kedalaman hasil estimasi, bukan sensor — VST mencapai 0,759 melawan 0,734 (JL-DCF). Artinya, keunggulan terbesar justru muncul pada data paling berderau, konsisten dengan klaim bahwa konteks global membantu ketika isyarat lokal tidak andal. Biaya komputasi VST 30,99 G MACs, sebanding dengan BBS-Net (31,2 G) dan jauh di bawah JL-DCF (211,06 G).

Pada RGB SOD, VST dibandingkan dengan 12 metode di enam dataset. Pada DUTS-TE, S-measure 0,896 dan MAE 0,037 melampaui pembanding terbaik (LDF 0,892). Pada ECSSD 0,932 melawan 0,931 (CSF), dan pada SOD 0,854 melawan 0,835 (ITSD) — selisih hampir dua poin. MACs VST 23,16 G, lebih kecil dari semua pembanding berbobot berat seperti GateNet (162,13 G), meski parameternya 44,48 M tidak paling ringan (ITSD 26,47 M).

Studi ablasi pada model RGB-D memisahkan kontribusi tiap komponen (S-measure pada NJUD): model dasar tanpa *convertor* dan *decoder* mencapai 0,869; menambah CMT menjadi 0,873; *upsampling* bilinear menaikkan ke 0,906; menggantinya dengan RT2T menjadi 0,915; fusi token multi-level menjadi 0,923; dan *decoder* multi-tugas mempertahankan 0,922 sambil menambah keluaran batas. Dua kesimpulan terbaca: pemulihan resolusi adalah penyumbang peningkatan terbesar, dan RT2T konsisten lebih baik dari *upsampling* bilinear. *Decoder* multi-tugas berbasis token juga lebih efisien daripada *decoder* dua aliran konvensional (C2D): 17,22 M parameter dan 17,70 G MACs melawan 20,35 M dan 28,27 G, dengan hasil lebih baik pada tiga dari empat dataset ablasi.

## Kelebihan dan Keterbatasan

Kelebihan utama VST adalah pemodelan konteks global di setiap lapis, bukan sebagai tambahan pada arsitektur lokal. Ketiga rancangannya — CMT, RT2T, dan *decoder* berbasis token — terbukti menyumbang kinerja dalam ablasi, dan paradigma *patch-task-attention* menunjukkan jalan bagi prediksi padat berbasis Transformer murni tanpa konvolusi maupun *upsampling* bilinear. Efisiensi MACs yang rendah relatif terhadap kualitasnya juga tercatat.

Keterbatasan berikut sebagian merupakan analisis penulis bab, bukan pernyataan penulis makalah. Pertama, dari sisi rekayasa, jumlah parameter model RGB-D (83,83 M) lebih besar daripada kebanyakan pembanding CNN, sehingga kebutuhan memori tetap tinggi meski MACs rendah. Kedua, model bergantung pada bobot pra-latih T2T-ViT dari ImageNet. Ketiga, pada dataset mapan seperti NJUD dan ECSSD selisih terhadap metode CNN terbaik sangat tipis (0,001 poin S-measure), sehingga klaim keunggulan universal perlu dibaca hati-hati. Keempat, kualitas peta kedalaman tetap memengaruhi hasil fusi; makalah tidak melaporkan analisis ketangguhan terhadap kedalaman berderau di luar ReDWeb-S.

## Kaitan dengan Bab Lain

VST menempati posisi peralihan dalam klaster RGB-D SOD: ia mewarisi agenda fusi lintas-modal dari generasi CNN — BBS-Net (bab 036), JL-DCF (bab 038), dan UC-Net (bab 041) — sekaligus mengganti fondasi komputasinya. Kaitan paling langsung adalah dengan S2MA (bab 039), karya penulis yang sama tahun 2020, yang memakai mekanisme *self-mutual attention* untuk interaksi RGB–kedalaman; CMT pada VST dapat dibaca sebagai reformulasi gagasan itu dalam kerangka Transformer murni. Prediksi batas sebagai tugas pendamping juga melanjutkan praktik yang dipopulerkan metode RGB seperti EGNet. Ke depan, VST membuka garis yang diteruskan SwinNet (bab 043), yang mengganti *backbone* T2T-ViT dengan Swin Transformer berjendela geser.

- [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)
- [038 - 2020 - JL-DCF - RGB-D SOD](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md)
- [039 - 2020 - S2MA - RGB-D SOD](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md)
- [041 - 2020 - UC-Net - RGB-D SOD](./041%20-%202020%20-%20UC-Net%20-%20RGB-D%20SOD.md)
- [043 - 2022 - SwinNet - RGB-D SOD](./043%20-%202022%20-%20SwinNet%20-%20RGB-D%20SOD.md)

## Poin untuk Sitasi

Kunci BibTeX: `liu2021vst`. Ringkasan yang aman dikutip: VST (Liu dkk., ICCV 2021) adalah model SOD pertama yang dibangun murni dari Transformer, dengan satu kerangka terpadu untuk RGB dan RGB-D. Model ini memakai *encoder* T2T-ViT, *convertor* lintas-modal (CMT), *upsampling* token RT2T, serta *decoder* multi-tugas berbasis token saliency dan token batas. Pada sembilan benchmark RGB-D dan enam benchmark RGB, VST melampaui metode CNN kontemporer dengan MACs yang sebanding atau lebih kecil.

Catatan verifikasi sebelum sitasi formal: seluruh angka pada bab ini diambil dari Tabel 1–3 naskah versi ICCV 2021 (hal. 4722–4732) dan telah dicocokkan dengan preprint arXiv:2104.12099; pembaca tetap dianjurkan memeriksa ulang angka yang dikutip ke tabel naskah asli.
