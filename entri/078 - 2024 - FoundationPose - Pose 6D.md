# 078 - FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wen2024foundationpose` |
| Judul asli | FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects |
| Penulis | Bowen Wen, Wei Yang, Jan Kautz, Stan Birchfield |
| Tahun | 2024 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2024) |
| Tema | Pose 6D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2312.08344
- **Halaman proyek (kode & data):** https://nvlabs.github.io/FoundationPose/
- **Google Scholar:** https://scholar.google.com/scholar?q=FoundationPose%3A%20Unified%206D%20Pose%20Estimation%20and%20Tracking%20of%20Novel%20Objects
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=FoundationPose%3A%20Unified%206D%20Pose%20Estimation%20and%20Tracking%20of%20Novel%20Objects&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan FoundationPose, satu model terpadu untuk estimasi pose 6D — posisi (tiga translasi) dan orientasi (tiga rotasi) sebuah objek relatif terhadap kamera — sekaligus pelacakan pose (*tracking*) pada objek yang belum pernah dilihat selama pelatihan (*novel object*). Masukan sistem adalah citra RGB-D (citra warna berpasangan peta kedalaman) ditambah salah satu dari dua bentuk pengetahuan objek: model CAD (*computer-aided design*, yaitu model 3D objek dari perangkat lunak desain) pada setup *model-based*, atau sekitar 16 citra referensi objek pada setup *model-free*. Kedua setup dijembatani oleh representasi implisit saraf yang mampu me-render objek dari sudut pandang baru, sehingga modul estimasi pose di hilir identik untuk keduanya.

Model ini dipakai langsung pada objek baru tanpa penyetelan halus (*fine-tuning*) sama sekali. Pada lima tolok ukur publik, FoundationPose mengungguli metode yang dirancang khusus untuk masing-masing dari empat tugas (estimasi/pelacakan × model-based/model-free), bahkan menyamai metode tingkat *instance* yang dilatih khusus per objek. Generalisasi tersebut diperoleh dari pelatihan pada data sintetis berskala besar yang teksturnya diperkaya secara otomatis oleh model bahasa besar (LLM) dan model difusi.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum FoundationPose, metode pose 6D terbagi dalam tingkatan asumsi pengetahuan objek. Metode tingkat *instance* — PoseCNN (bab 073), DenseFusion (bab 074), PVN3D (bab 075), dan FFB6D (bab 076) — dilatih dan diuji pada objek yang persis sama, dan umumnya memerlukan model CAD bertekstur untuk membangkitkan data latih. Metode tingkat kategori melonggarkan asumsi ini, tetapi hanya berlaku pada kategori terdefinisi (misalnya hanya botol atau hanya mangkuk), dan data latih tingkat kategori sulit diperoleh karena setiap objek harus melalui proses kanonikalisasi pose.

Untuk objek sembarang, dua setup berkembang terpisah. Pada setup model-based, model CAD objek tersedia saat pengujian; contohnya MegaPose, metode render-and-compare untuk objek baru. Pada setup model-free, yang tersedia hanya sejumlah citra referensi objek; contohnya Gen6D (pipeline deteksi–penelusuran–penghalusan pada RGB), OnePose (korespondensi 2D–3D dari rekonstruksi *structure-from-motion*), dan FS6D (metode RGB-D *few-shot*). Aplikasi nyata menyediakan salah satu dari dua bentuk informasi itu, sehingga praktisi harus memakai metode yang berbeda untuk kasus yang berbeda. Di sisi lain, metode pelacakan pose pada video (DeepIM, se(3)-TrackNet) membentuk garis penelitian ketiga yang sebagian besar juga tingkat *instance*. Akar masalah yang sama melintasi ketiganya: data nyata beranotasi pose 6D sangat mahal, sehingga setiap metode mengikat diri pada himpunan objek yang sempit agar pelatihan tetap mungkin.

## Ide Utama

Gagasan inti FoundationPose adalah menyeragamkan seluruh variasi tugas menjadi satu skema *render-and-compare*: objek di-render pada banyak kandidat pose, setiap hasil render dibandingkan dengan citra amatan, dan kandidat yang paling cocok dipilih. Agar skema ini tetap berlaku tanpa model CAD, objek direpresentasikan sebagai *medan saraf* (*neural field*) yang dilatih dari belasan citra referensi dan dapat me-render tampilan RGB-D dari sudut pandang mana pun. Dengan demikian, baik CAD maupun citra referensi dikonversi ke satu kemampuan yang sama — me-render objek — sehingga satu jaringan penghalusan pose dan satu jaringan seleksi pose melayani keempat tugas sekaligus.

Kunci kedua adalah sumber pelatihan. Karena data pose nyata langka, seluruh pelatihan memakai data sintetis yang keragamannya diperbesar dua lapis: puluhan ribu model 3D dari basis data publik, dan augmentasi tekstur otomatis yang dirancang oleh LLM lalu direalisasikan oleh model difusi (model generatif yang mensintesis data melalui penghilangan derau bertahap). Arsitektur jaringan berbasis *transformer* dan fungsi loss kontrastif membuat jaringan yang hanya dilatih pada data sintetis tetap menggeneralisasi ke objek dan kamera nyata.

## Cara Kerja Langkah demi Langkah

Alur kerja sistem secara keseluruhan:

```
MASUKAN: citra RGB-D amatan  +  pengetahuan objek (salah satu)
                                  |
              model CAD        ~16 citra referensi
                  |                   v
                  |        medan saraf objek (SDF), dilatih
                  |        beberapa detik, sekali per objek
                  |                   v
                  |        marching cubes -> mesh bertekstur
                  v                   v
              +---------------------------------------+
              |  renderer RGB-D: render objek         |
              |  pada pose sembarang                  |
              +---------------------------------------+
                                  |
   deteksi 2D (Mask R-CNN/CNOS) -> translasi awal (kedalaman median)
                               -> rotasi awal: Ns x Ni hipotesis
                                  v
              +---------------------------------------+
              | JARINGAN PENGHALUSAN (iteratif):      |
              | bandingkan render(pose kasar) dengan  |
              | amatan -> pembaruan translasi, rotasi |
              +---------------------------------------+
                                  v
              +---------------------------------------+
              | SELEKSI HIERARKIS: K embedding ->     |
              | self-attention lintas hipotesis ->    |
              | K skor -> pose berskor tertinggi      |
              +---------------------------------------+
                                  v
                    KELUARAN: pose 6D (R, t)
           mode tracking: pose frame sebelumnya -> jalur cepat
```

Diagram di atas menunjukkan konvergensi dua jalur pengetahuan objek ke satu renderer, diikuti tiga tahap inti: inisialisasi hipotesis, penghalusan iteratif, dan seleksi. Setiap tahap diuraikan berikut ini.

### Pembangkitan Data Sintetis Berbantuan LLM

Aset 3D pelatihan diambil dari Objaverse-LVIS (lebih dari 40.000 objek dalam 1.156 kategori menurut taksonomi LVIS, sebuah dataset deteksi objek bervariasi tinggi) dan GSO (*Google Scanned Objects*). Kualitas bentuk umumnya baik, tetapi ketepatan teksturnya bervariasi. Metode sebelumnya (FS6D) menambal tekstur dengan citra acak dari ImageNet atau MS-COCO, yang menimbulkan artefak berupa jahitan pada permukaan. FoundationPose menggantinya dengan strategi *prompt* hierarkis dua tingkat: pertama, ChatGPT diminta mendeskripsikan penampakan yang mungkin dari suatu kategori objek; jawabannya menjadi prompt teks bagi TexFusion, model difusi yang mensintesis tekstur baru pada permukaan model 3D. Karena otomatis penuh, satu objek dapat diperkaya menjadi banyak gaya penampakan.

Adegan latih dirender dengan NVIDIA Isaac Sim memakai *path tracing* (teknik rendering yang menelusuri lintasan cahaya untuk hasil fotorealistis) serta simulasi fisika gravitasi agar susunan objek wajar. Ukuran, material, pose kamera, dan pencahayaan diacak. Akurasi pada YCB-Video jenuh pada sekitar satu juta citra latih; di atas titik itu penambahan data tidak lagi menaikkan akurasi.

### Medan Saraf Objek untuk Setup Model-Free

Bila CAD tidak tersedia, objek dimodelkan oleh dua fungsi saraf. Fungsi geometri Ω memetakan titik 3D x ke *signed distance* (jarak bertanda ke permukaan objek: nol tepat di permukaan, positif di luar, negatif di dalam). Fungsi penampakan Φ memetakan fitur geometri, normal permukaan, dan arah pandang ke warna. Koordinat x dikodekan dengan *multi-resolution hash encoding* (pengkodean posisi berjenjang yang mempercepat pelatihan medan saraf), sedangkan normal dan arah pandang disisipkan sebagai koefisien harmonik bola (*spherical harmonics*). Permukaan objek adalah himpunan titik dengan Ω(x) = 0.

Medan ini dilatih per objek dari sekitar 16 citra referensi dalam hitungan detik, satu kali per objek. Setelah itu, algoritme *marching cubes* (pengekstraksi permukaan dari medan skalar 3D) mengekstrak mesh bertekstur satu kali, sehingga rendering selanjutnya berlangsung sebagai rasterisasi biasa — cepat dan dapat diparalelkan untuk banyak hipotesis pose sekaligus. Dibanding NeRF (*Neural Radiance Field*, medan saraf berbasis densitas volume), representasi *signed distance field* (SDF) memberi kedalaman lebih akurat tanpa pemilihan ambang densitas manual.

### Inisialisasi Hipotesis Pose

Objek dideteksi lebih dahulu oleh detektor siap pakai: Mask R-CNN (detektor dan pensegmen instans dua tahap) atau CNOS (detektor objek baru berbasis kemiripan dengan model dasar). Translasi awal diambil dari titik 3D pada kedalaman median di dalam kotak deteksi. Rotasi awal dicuplik seragam: Ns sudut pandang pada *icosphere* (bola yang dipartisi menjadi titik-titik yang berjarak hampir sama) yang menghadap pusat objek, dikalikan Ni rotasi dalam-bidang terdiskritisasi, menghasilkan Ns·Ni hipotesis pose global.

### Jaringan Penghalusan Pose

Masukan jaringan penghalusan adalah render objek pada pose kasar dan potongan citra amatan; keluarannya adalah pembaruan translasi Δt dan pembaruan rotasi ΔR. Pemotongan citra dikondisikan oleh pose: pusat potongan adalah proyeksi titik asal objek ke citra, dan ukurannya ditentukan dari proyeksi diameter objek yang sedikit diperbesar. Bila pose kasar meleset, potongan ikut bergeser, sehingga jaringan memperoleh umpan balik visual untuk mengoreksi translasi. Pembaruan dipisahkan (*disentangled*): t+ = t + Δt dan R+ = ΔR ⊗ R, keduanya dinyatakan dalam kerangka kamera; rotasi diparameterkan sebagai *axis-angle* (sumbu putar dan sudut putar). Proses dapat diulang dengan memasukkan pose hasil sebagai masukan iterasi berikutnya.

Secara arsitektur, satu encoder CNN bersama mengekstrak fitur dari kedua cabang RGB-D (render dan amatan). Fitur digabungkan, dilewatkan blok CNN residual, dipecah menjadi *patch* dengan penyisipan posisi, lalu diproses oleh *transformer encoder* — modul perhatian-diri (*self-attention*) yang menimbang hubungan antar-patch — yang terpisah untuk translasi dan rotasi. Pelatihan diawasi loss L2 terhadap pembaruan pose kebenaran.

### Seleksi Pose Hierarkis dengan Loss Kontrastif

Setiap hipotesis yang telah dihaluskan diberi skor oleh jaringan peringkat dua tingkat. Tingkat pertama membandingkan render tiap hipotesis dengan amatan dan menghasilkan *embedding* (vektor representasi) 512 dimensi. Tingkat kedua menerapkan *self-attention* pada seluruh K embedding sekaligus — tanpa penyisipan posisi agar hasil tidak bergantung urutan — lalu memproyeksikannya menjadi K skor; pose berskor tertinggi menjadi keluaran. Perbandingan lintas-hipotesis ini membuat skor bersifat relatif terhadap kandidat lain, bukan penilaian absolut per kandidat, sehingga lebih mudah dipelajari.

Jaringan dilatih dengan *triplet loss* terkondisi pose: skor pose buruk harus lebih rendah dari skor pose baik dengan margin tertentu. Label baik/buruk ditentukan metrik ADD (jarak rata-rata titik-titik model objek antara pose prediksi dan pose kebenaran) terhadap anotasi. Hanya pasangan yang pose baiknya cukup dekat dengan kebenaran (jarak geodesik rotasi di bawah ambang) yang dipakai, karena membandingkan dua pose yang sama-sama jauh dari kebenaran bersifat ambigu.

### Pelacakan Pose pada Video

Pada mode pelacakan, pose dari *frame* sebelumnya menjadi inisialisasi, dan hanya modul penghalusan yang dijalankan — tanpa pencuplikan hipotesis ganda dan tanpa seleksi. Pemangkasan inilah yang membuat pelacakan berjalan jauh lebih cepat daripada estimasi pose penuh; angka kecepatannya dilaporkan pada bagian Eksperimen.

## Eksperimen dan Hasil

Evaluasi memakai lima dataset: LINEMOD, Occluded LINEMOD, YCB-Video, T-LESS, dan YCBInEOAT, yang mencakup objek tanpa tekstur, mengilap, simetris, adegan padat, dan manipulasi robot. Metriknya antara lain AUC dari ADD dan ADD-S (luas area di bawah kurva akurasi terhadap ambang galat; ADD-S memakai jarak ke titik model terdekat agar adil bagi objek simetris), recall ADD-0.1d (proporsi pose dengan galat di bawah 10% diameter objek), dan skor AR tolok ukur BOP (rata-rata recall dari tiga metrik: VSD, MSSD, MSPD).

Hasil utama pada tiap tugas:

- **Estimasi model-free, YCB-Video (16 referensi):** AUC ADD-S 97,4 dan ADD 91,5, dibanding FS6D 88,4/42,1 — padahal FS6D disetel halus pada dataset target. Lonjakan ADD hampir 50 poin menunjukkan metode berbasis korespondensi tertinggal jauh pada objek minim tekstur.
- **Estimasi model-free, LINEMOD:** ADD-0.1d 99,9 dari 16 referensi, melampaui FS6D+ICP (91,5) dan metode RGB OnePose++ (76,9) yang memakai 200 referensi. Artinya, kedalaman dan render-and-compare menutup defisit jumlah referensi dua belas kali lipat.
- **Estimasi model-based (BOP):** skor AR rata-rata 83,3 pada tiga dataset inti, melampaui MegaPose-RGBD (58,6) dan SurfEmb+ICP (79,7) — yang terakhir adalah metode tingkat *instance*. Model dengan asumsi lebih longgar ternyata sekaligus lebih akurat.
- **Pelacakan, YCBInEOAT:** ADD-S 96,4, di atas se(3)-TrackNet (95,5) yang dilatih per objek dan diberi pose awal kebenaran.
- **Pelacakan, YCB-Video:** ADD-S 97,9, di atas ICG (96,5) yang juga berbasis render-and-compare; varian model-free murni tetap mencapai 97,5.

Studi ablasi pada YCB-Video menunjukkan kontribusi tiap komponen. Menghapus perbandingan hierarkis menurunkan ADD dari 91,52 ke 89,05 — penurunan terbesar di antara komponen yang diuji. Mengganti transformer dengan lapisan konvolusi biasa memberi 90,77; tanpa augmentasi tekstur LLM 90,83; mengganti triplet loss dengan InfoNCE 89,39. Semua varian berada di bawah model penuh, sehingga setiap pilihan desain terbukti berkontribusi. Model juga tahan terhadap sedikitnya referensi: akurasi jenuh pada 12 citra, dan dengan hanya 4 citra pun masih melampaui FS6D yang memakai 16 citra.

Waktu berjalan diukur pada CPU Intel i9-10980XE dan GPU RTX 3090. Estimasi pose satu objek memakan ±1,3 detik (penghalusan 0,88 detik, seleksi 0,42 detik), sedangkan pelacakan berjalan ±32 Hz. Kesenjangan dua orde kecepatan ini mendasari pola pemakaian praktis: estimasi penuh dijalankan sekali untuk inisialisasi, lalu sistem beralih ke mode pelacakan.

## Kelebihan dan Keterbatasan

Kelebihan utama adalah cakupan: satu bobot terlatih menangani empat tugas tanpa penyetelan per objek maupun per dataset, dan tetap unggul atas metode spesialis. Strategi render-and-compare tidak bergantung pada tekstur kuat atau korespondensi titik, sehingga kokoh pada objek polos dan simetris. Rendering dari mesh hasil marching cubes membuat banyak hipotesis dapat dinilai secara paralel.

Keterbatasan pertama, masukan wajib berupa RGB-D; makalah tidak menyediakan varian RGB murni. Kedua, setup model-free masih memerlukan citra referensi dengan anotasi pose kebenaran (pada eksperimen diambil dari split latih dataset), sehingga asumsinya belum sepenuhnya bebas pengetahuan objek. Ketiga, estimasi pose penuh ±1,3 detik per objek bukan *real-time*; penggunaan langsung menuntut peralihan ke mode pelacakan. Keempat, rantai kerja bergantung pada detektor 2D eksternal, sehingga kegagalan deteksi merambat ke seluruh tahap. Dari sisi rekayasa, biaya di muka tidak ringan: pelatihan memerlukan sekitar satu juta citra sintetis berkualitas *path tracing*, dan pembangkitan tekstur memerlukan akses LLM serta model difusi.

## Kaitan dengan Bab Lain

Bab ini mewarisi tolok ukur dan metrik dari silsilah pose 6D sebelumnya: dataset YCB-Video dan metrik ADD/ADD-S diperkenalkan oleh PoseCNN (bab 073), estimator pose berbasis CNN yang meregresikan translasi dan memilih titik kunci. DenseFusion (bab 074), PVN3D (bab 075), FFB6D (bab 076), dan G2L-Net (bab 077) merepresentasikan paradigma tingkat *instance* — fusi fitur RGB dan geometri per objek — yang justru dilampaui FoundationPose tanpa pelatihan per objek sama sekali. Peta konseptual bidang ini secara keseluruhan dibahas pada bab 079 (review Hoque dkk.). Dalam tinjauan ini, bab 078 menandai peralihan pose 6D dari model per-objek menuju model fondasi yang dilatih pada data sintetis berskala besar.

- [073 - 2018 - PoseCNN - Pose 6D](./073%20-%202018%20-%20PoseCNN%20-%20Pose%206D.md)
- [074 - 2019 - DenseFusion - Pose 6D](./074%20-%202019%20-%20DenseFusion%20-%20Pose%206D.md)
- [075 - 2020 - PVN3D - Pose 6D](./075%20-%202020%20-%20PVN3D%20-%20Pose%206D.md)
- [076 - 2021 - FFB6D - Pose 6D](./076%20-%202021%20-%20FFB6D%20-%20Pose%206D.md)
- [077 - 2020 - G2L-Net - Pose 6D](./077%20-%202020%20-%20G2L-Net%20-%20Pose%206D.md)
- [079 - 2021 - Review Pose 6D & Deteksi 3D (Hoque dkk.) - Pose 6D](./079%20-%202021%20-%20Review%20Pose%206D%20%26%20Deteksi%203D%20%28Hoque%20dkk.%29%20-%20Pose%206D.md)

## Poin untuk Sitasi

Kutip dengan kunci `wen2024foundationpose`. Ringkasan yang aman dikutip: "FoundationPose adalah model fondasi terpadu untuk estimasi dan pelacakan pose 6D objek baru pada citra RGB-D; representasi implisit saraf menjembatani setup model-based dan model-free, dan pelatihan sintetis berskala besar berbantuan LLM memberi generalisasi tanpa penyetelan halus, melampaui metode spesialis pada lima tolok ukur publik." Seluruh angka hasil pada bab ini diambil dari tabel naskah arXiv v2 (2312.08344); nomor halaman CVPR (17868–17879) berasal dari berkas tinjauan lama dan sebaiknya diverifikasi ke prosiding resmi. Rincian implementasi yang tidak dibahas di sini — nilai pasti Ns dan Ni, jumlah iterasi penghalusan, serta anggaran GPU pelatihan — perlu dicek ke naskah dan lampirannya sebelum dikutip dalam karya formal.
