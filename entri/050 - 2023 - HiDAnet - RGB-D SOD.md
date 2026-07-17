# 050 - HiDAnet: RGB-D Salient Object Detection via Hierarchical Depth Awareness

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wu2023hidanet` |
| Judul asli | HiDAnet: RGB-D Salient Object Detection via Hierarchical Depth Awareness |
| Penulis | Zongwei Wu, Guillaume Allibert, Fabrice Meriaudeau, Chao Ma, Cédric Demonceaux |
| Tahun | 2023 |
| Venue | IEEE Transactions on Image Processing (TIP), vol. 32, hlm. 2160–2173 |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2301.07405
- **Kode sumber (GitHub):** https://github.com/Zongwei97/HIDANet
- **Google Scholar:** https://scholar.google.com/scholar?q=HiDAnet%3A%20RGB-D%20Salient%20Object%20Detection%20via%20Hierarchical%20Depth%20Awareness
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=HiDAnet%3A%20RGB-D%20Salient%20Object%20Detection%20via%20Hierarchical%20Depth%20Awareness&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan HiDAnet (*Hierarchical Depth Awareness network*), jaringan untuk *salient object detection* (SOD) RGB-D: tugas memetakan objek paling menonjol secara visual pada citra, dibantu peta kedalaman (*depth map*) — citra yang tiap pikselnya menyatakan jarak ke kamera. Sasaran perbaikannya adalah pemanfaatan kedalaman yang dangkal: *channel attention* (pembobotan kanal fitur menurut kepentingannya) pada metode sebelumnya dihitung dari *global average pooling* (perata-rataan seluruh piksel menjadi satu nilai per kanal), sehingga latar dan objek berkontribusi sama besar; akibatnya, objek yang mirip latar tetapi berbeda jarak dari kamera sulit dipisahkan.

Solusinya adalah *hierarchical depth awareness*: histogram kedalaman didiskretisasi menjadi wilayah granularitas jarak dengan *multi-thresholding* Otsu (ambang yang memaksimalkan perbedaan antarkelompok nilai), tiap wilayah menjadi maska untuk attention kanal lokal di setiap level *encoder*, dan satu modul attention silang menangani fusi antarmodalitas sekaligus antarlevel. Model dilatih *end-to-end* (tanpa tahap terpisah), melampaui metode sebelumnya pada lima tolok ukur RGB-D SOD dengan tiga *backbone* (pengekstrak fitur dasar), dan paling stabil ketika peta kedalaman diberi derau.

## Latar Belakang: Masalah yang Ingin Dipecahkan

SOD berbasis citra warna rapuh pada pencahayaan kontras rendah dan oklusi (objek tertutup sebagian). Sensor RGB-D murah menyediakan petunjuk geometri, dan literatur mengembangkan dua keluarga fusi: *single-stream* menggabungkan RGB dan depth sejak masukan (DANet dengan masukan empat kanal; JL-DCF pada bab 038 dengan desain siamese), sedangkan *multi-stream* memakai dua *encoder* paralel yang fiturnya digabung pada tingkat semantik (DMRA pada bab 035; BBS-Net pada bab 036).

Dua kelemahan tersisa. Pertama, attention kanal yang umum dipakai merata-ratakan peta fitur secara global; kedalaman tidak dipakai memisahkan statistik objek dari latar, sehingga detail berbutir halus (*fine-grained*) jarang dieksploitasi eksplisit. Kedua, pemanfaatan prior kedalaman secara langsung masih terbatas: DSA2F (bab 045), karya sezaman terdekat, memakai ambang tetap pada histogram kedalaman — tidak adaptif antarcitra — dan attention-nya hanya konvolusi 1×1. Sebagian peta kedalaman dataset juga berkualitas rendah karena bias pengukuran atau estimasi, sehingga ketahanan terhadap derau menjadi syarat praktis.

## Ide Utama

Pengamatan awalnya: objek salien biasanya menempati rentang jarak tertentu — satu *granularitas* (tingkat kebutiran) histogram kedalaman — sedangkan latar menempati granularitas lain. Struktur kedalaman yang berlapis ini sejajar dengan hirarki jaringan: level awal *encoder* memuat detail halus, level dalam memuat abstraksi semantik.

Gagasan inti HiDAnet adalah mengubah granularitas kedalaman menjadi mekanisme attention. Histogram kedalaman dibagi statis menjadi beberapa wilayah — tanpa parameter yang dipelajari — dan tiap wilayah menjadi maska: attention kanal dihitung lokal di dalam tiap wilayah, bukan dari seluruh peta fitur, sehingga statistik latar tidak ikut menentukan bobot fitur objek. Bila seluruh piksel berkedalaman sama, maska menutupi citra penuh dan modul tereduksi menjadi attention kanal konvensional. Gagasan kedua: fusi antarmodalitas (RGB–depth) dan antarlevel (encoder–decoder) adalah satu masalah yang sama — dua sumber fitur heterogen yang saling mempertegas — sehingga satu modul attention silang dipakai untuk keduanya.

## Cara Kerja Langkah demi Langkah

Arsitektur HiDAnet mengikuti pola U-Net: dua *encoder* paralel, satu *decoder* bersama lima level, serta *skip connection* (jalur pintas yang menyalin fitur encoder ke decoder pada resolusi yang sama). Alur datanya, dengan tiga komponen utama GBA (encoder), CDA (fusi), dan EMI (decoder):

```
masukan: citra RGB 352x352  +  peta depth 352x352

[pra-proses] histogram depth ─► multi-Otsu (T=2) ─► 3 maska wilayah
             (dekat / tengah / jauh); dihitung sekali per citra,
             lalu di-resize ke 5 resolusi peta fitur

[encoder]    RGB   ─► fR1..fR5, tiap level ditegas GBA ─┐
             depth ─► fD1..fD5, tiap level ditegas GBA ─┤
   GBA = attention kanal lokal per maska (pooling lokal + ECA)
                                                        ▼
[fusi]   CDA tiap level: attention kanal+spasial dari RGB mempertegas
         fitur depth, dan sebaliknya; concat + konvolusi 3x3;
         hasil digabung keluaran level sebelumnya (kasar ► halus)
                                                        │
[decoder]  decoder RGB ─┐                               │ skip via CDA
           decoder depth ├─► EMI ─► DECODER BERSAMA ◄───┘
                        ─┘   (concat + konvolusi 3x3 + ECA + residual)
                             5 level, tiap level ─► RFB ─► peta saliency

[keluaran]  5 peta x 3 cabang (RGB, depth, bersama)
            loss tiap level = BCE + IoU, bobot {1; 0,8; 0,6; 0,4; 0,2}
            inferensi: hanya cabang bersama
```

### Diskretisasi Kedalaman dengan Multi-Otsu

Dari peta kedalaman dibentuk histogram nilai jarak. Algoritme Otsu mencari ambang pembagi histogram yang memaksimalkan varians antarkelas: kelompok nilai kedalaman dibuat seberbeda mungkin satu sama lain. HiDAnet memakai perluasan multi-level (multi-Otsu) dengan T ambang yang membagi kedalaman menjadi T+1 wilayah; ablasi menetapkan T = 2, menghasilkan tiga wilayah yang dapat dibaca sebagai "dekat", "tengah", dan "jauh". Ambang dihitung satu kali per citra pada pra-pemrosesan — menjadikannya adaptif terhadap isi citra — lalu maska wilayah di-resize mengikuti resolusi peta fitur tiap level.

### GBA: Attention Kanal Berbasis Granularitas

GBA (*granularity-based attention*) dipasang pada setiap level kedua encoder. Diberikan peta fitur f_in berukuran C×h×w (C kanal, tinggi h, lebar w) dan maska wilayah m_i (i = 1..T+1), langkahnya: (1) fitur diseleksi per wilayah lewat perkalian elemen demi elemen f_in ⊗ m_i; (2) *local average pooling* merata-ratakan hanya piksel di dalam wilayah menjadi vektor 1×1×C; (3) vektor ini dilewatkan ke ECA (*Efficient Channel Attention*: attention kanal ringan berbasis konvolusi satu dimensi antarkanal) dan fungsi sigmoid (pemetaan ke rentang 0–1) menjadi bobot kanal; (4) bobot dikalikan kembali ke fitur wilayah. Keluaran seluruh wilayah dijumlahkan, lalu ditambah f_in lewat koneksi residual (penjumlahan identitas yang menjaga informasi asal).

Contoh numerik: pada peta fitur 44×44 (1.936 piksel) dan wilayah seluas 30%, pooling lokal merangkum ±580 piksel, bukan seluruh 1.936 piksel; statistik latar tidak lagi mengencerkan bobot kanal objek. Pada level awal, GBA mempertajam batas objek; pada level dalam, GBA memperkuat diskriminasi semantik antarobjek yang mirip penampilannya.

### CDA: Attention Silang untuk Fusi Encoder

Fusi fitur RGB (f_x) dan depth (f_y) per level diawali konvolusi 1×1 yang memparuhkan kanal, diikuti konvolusi 3×3 untuk respons tepi. Dari tiap fitur dihitung dua attention: attention kanal M_c (vektor C×1×1) dari *average* dan *max pooling* global yang dilewatkan ke MLP (*multi-layer perceptron*, jaringan terhubung penuh kecil), dan attention spasial M_s (peta 1×h×w) dari konvolusi 7×7 atas rata-rata dan maksimum antarkanal; keduanya diaktifkan sigmoid. Fusi dilakukan menyilang: fitur RGB dikalikan attention milik depth, dan fitur depth dikalikan attention milik RGB, sehingga tiap modalitas mempertegas modalitas lain pada kanal dan lokasi yang relevan; ketika kedalaman gagal memisahkan objek dari permukaan sejarak, penampilan memberi pembeda. Hasil kedua arah digabung lewat konkatenasi dan konvolusi 3×3; mulai level kedua, keluaran fusi digabung pula dengan keluaran level sebelumnya, mengalir dari kasar ke halus (*coarse-to-fine*). Modul CDA (*cross dual-attention*) yang sama dipakai ulang pada *skip connection*: fitur encoder dan decoder diperlakukan sebagai pasangan "multi-modal".

### EMI: Agregasi Decoder Bersama

Fitur hasil fusi encoder diteruskan ke tiga cabang decoder: decoder RGB, decoder depth, dan decoder bersama. Pada tiap level, EMI (*efficient multi-input fusion*) menggabungkan fitur decoder RGB, fitur decoder depth, dan keluaran bersama level sebelumnya: ketiganya dikonkatenasi, dirampingkan konvolusi 3×3, diseleksi dengan G-ECA (ECA dengan pooling global), lalu ditambah koneksi residual dari level sebelumnya. Berbeda dengan CDA, EMI hanya memakai attention kanal karena petunjuk spasial telah terkikis pada fitur dalam. Setiap level decoder bersama diakhiri RFB (*Receptive Field Block*: modul multi-cabang dengan konvolusi berdilasi yang memperluas daerah tangkapan fitur) sebelum menghasilkan peta saliency.

### Supervisi Multi-Skala

Kelima level pada ketiga cabang menghasilkan peta prediksi yang disamakan ukurannya dengan *ground truth* (maska kebenaran) dan dinilai dua fungsi *loss*: BCE (*binary cross-entropy*, galat per piksel) dan *IoU loss* (galat global berbasis rasio irisan terhadap gabungan prediksi dan kebenaran). *Loss* total menjumlahkan kelima level dengan bobot menurun {1; 0,8; 0,6; 0,4; 0,2}, sehingga tiap level dipaksa belajar representasi yang berguna. Saat inferensi, hanya keluaran cabang bersama yang dipakai.

## Eksperimen dan Hasil

Pelatihan mengikuti protokol standar: 2.195 sampel (1.485 dari NJU2K-train dan 700 dari NLPR-train), dengan pengujian pada DES (135 citra), NLPR-test (300), NJU2K-test (500), STERE (1.000), dan SIP (929), ditambah COME15K (dilatih pada 8.025 sampel, diuji pada himpunan "Difficult" berisi 3.000 citra). Metriknya: MAE (*mean absolute error*; lebih kecil lebih baik), F-measure maksimum (rata-rata harmonik presisi dan *recall*, β² = 0,3), S-measure (kemiripan struktur objek dan wilayah), dan E-measure maksimum (kesejajaran tingkat citra dan piksel). Model dilatih pada GPU V100 dengan masukan 352×352, pengoptimal Adam berlaju awal 0,0001, selama 100 *epoch* (±6 jam).

Dengan *backbone* Res2Net50 (525 MB, ±11 FPS), HiDAnet mencapai MAE 0,013 dan F-measure 0,952 pada DES — di atas SPNet (0,014 dan 0,950) dengan model 25% lebih kecil (SPNet 702 MB). Pada NJU2K dan STERE, F-measure 0,939 dan 0,921 melawan 0,935 dan 0,915 milik SPNet: keunggulan konsisten tetapi berorde persepuluh poin. Dengan ResNet50 (523 MB, ±12 FPS) ia mencetak nilai terbaik pada DES, NLPR, dan NJU2K; dengan VGG16 (269 MB, ±6 FPS) unggul terutama pada NLPR dan SIP. Pada COME15K "Difficult", MAE 0,062 adalah yang terkecil di antara tujuh pembanding (SPNet 0,065; CMINet 0,064) dengan E-measure 0,893 yang setara CMINet.

Ketika peta kedalaman uji diberi derau Gaussian (RMSE 0,261), penurunan S-measure HiDAnet pada DES hanya 0,3%, dibandingkan 1,0% pada SPNet dan 2,0% pada CMINet; pada NJU2K penurunannya 0,1% (SPNet 0,5%; CMINet 0,7%). Wilayah Otsu statis terbukti lebih stabil daripada fusi berbasis informasi-mutual milik CMINet.

Ablasi mengonfirmasi tiap komponen. Memasang GBA pada alur RGB saja menurunkan MAE DES dari 0,015 ke 0,014, dan pada kedua alur menjadi 0,013; mengganti pooling lokal dengan pooling global menaikkan MAE kembali ke 0,019. T = 2 adalah titik terbaik: T = 1 membelah kedalaman terlalu kasar, T = 3 menghasilkan diskretisasi berlebih dengan F-measure turun dan kecepatan turun dari 13,3 FPS (tanpa GBA) menjadi 10,5 FPS. Mengganti modul fusi HiDAnet dengan fusi milik BBS-Net, CDINet, DCF, atau SPNet pada pengaturan identik menurunkan kinerja: sumbangan utama datang dari desain fusi, bukan *backbone* atau decoder.

## Kelebihan dan Keterbatasan

Kelebihan utama HiDAnet adalah pemanfaatan prior geometri tanpa parameter tambahan yang dipelajari: maska granularitas dihitung statis, sehingga murah dan stabil, dengan ketahanan derau terbaik di antara pembanding. Satu desain attention untuk tiga kebutuhan (fusi modalitas, fusi level, *skip connection*) menjaga arsitektur koheren; keunggulannya konsisten lintas tiga *backbone*.

Keterbatasannya: (1) kecepatan ±11 FPS dengan model 525 MB masih jauh dari *real-time*; dari sisi rekayasa, tiga cabang decoder dan fusi di setiap level menambah konsumsi memori pelatihan. (2) Manfaat granularitas menyusut ketika objek salien berada di latar: pada NLPR yang banyak memuat kasus demikian, sensitivitas terhadap T rendah dan keunggulan menipis. (3) Secara konseptual, metode ini tetap bergantung pada kualitas kedalaman — derau besar dapat merusak diskretisasi Otsu itu sendiri — sedangkan makalah hanya menguji derau Gaussian tersimulasi. (4) Seluruh eksperimen memakai *backbone* konvolusional; arsitektur *transformer* yang sezaman tidak dieksplorasi.

## Kaitan dengan Bab Lain

HiDAnet melanjutkan garis fusi *multi-stream* RGB-D SOD: [DMRA (bab 035)](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md) sebagai pelopor attention kedalaman multi-skala, [BBS-Net (bab 036)](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md) dengan CBAM pada fitur depth, dan [JL-DCF (bab 038)](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md) yang mewakili keluarga *single-stream*. Attention kanal yang dipakai pendahulunya dibuat sadar kedalaman lewat pooling lokal per wilayah Otsu. Karya sezaman terdekat adalah [DSA2F (bab 045)](./045%20-%202021%20-%20DSA2F%20-%20RGB-D%20SOD.md): keduanya membelah histogram kedalaman, tetapi DSA2F memakai ambang tetap dan konvolusi 1×1, sedangkan HiDAnet mengoptimalkan ambang dengan multi-Otsu dan memadukan wilayah dengan attention kanal. Jalur alternatif pada periode yang sama dibawa [VST (bab 042)](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md) dan [TriTransNet (bab 044)](./044%20-%202021%20-%20TriTransNet%20-%20RGB-D%20SOD.md) yang mengganti *backbone* konvolusional dengan transformer. Tolok ukurnya dibakukan antara lain oleh [D3Net (bab 037)](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md).

## Poin untuk Sitasi

Kutip dengan kunci `wu2023hidanet`. Ringkasan yang aman dikutip: "HiDAnet memanfaatkan prior geometri kedalaman secara berlapis: histogram kedalaman didiskretisasi dengan multi-Otsu menjadi beberapa wilayah granularitas yang dipakai sebagai maska untuk attention kanal lokal (GBA), lalu fusi multimodal-multilevel dilakukan satu modul *cross dual-attention* (CDA) dengan supervisi multi-skala. Model ini melampaui metode RGB-D SOD sebelumnya pada lima tolok ukur dengan tiga backbone berbeda dan menunjukkan ketahanan terbaik terhadap derau kedalaman."

Catatan verifikasi: seluruh angka pada bab ini dikutip dari preprint arXiv v1 (Januari 2023); sebelum sitasi formal, cocokkan dengan versi terbit IEEE TIP vol. 32 hlm. 2160–2173. Arah urutan bobot *loss* multi-skala {1; 0,8; 0,6; 0,4; 0,2} terhadap level tidak dirinci pada preprint.
