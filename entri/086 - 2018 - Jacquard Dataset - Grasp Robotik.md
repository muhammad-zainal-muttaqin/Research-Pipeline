# 086 - Jacquard: A Large Scale Dataset for Robotic Grasp Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `depierre2018jacquard` |
| Judul asli | Jacquard: A Large Scale Dataset for Robotic Grasp Detection |
| Penulis | Amaury Depierre, Emmanuel Dellandréa, Liming Chen |
| Tahun | 2018 |
| Venue | IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2018), hlm. 3511–3516 |
| Tema | Grasp Robotik |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1803.11469
- **Google Scholar:** https://scholar.google.com/scholar?q=Jacquard%3A%20A%20Large%20Scale%20Dataset%20for%20Robotic%20Grasp%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Jacquard%3A%20A%20Large%20Scale%20Dataset%20for%20Robotic%20Grasp%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan Jacquard, sebuah *dataset* (kumpulan data) sintetis berskala besar untuk deteksi *grasp* (posisi cengkeraman) pada citra RGB-D. Alih-alih mengumpulkan anotasi lewat pelabelan manusia atau percobaan fisik dengan robot, penulis membangun seluruh isi *dataset* melalui simulasi: model CAD (*Computer-Aided Design*) tiga dimensi dari ShapeNet dijatuhkan ke sebuah bidang dalam lingkungan fisika buatan, dirender menjadi citra, dan diuji secara otomatis untuk menemukan posisi cengkeraman yang berhasil menurut simulator fisika. Hasilnya adalah 54.000 citra dari lebih dari 11.000 objek berbeda, dengan lebih dari 1,1 juta anotasi *grasp* — lebih dari 50 kali lipat jumlah anotasi *dataset* Cornell yang sebelumnya menjadi acuan utama pada tugas ini.

Selain skala, makalah ini mengusulkan kriteria evaluasi baru bernama *Simulated Grasp Trial* (SGT, uji cengkeraman tersimulasi): alih-alih membandingkan geometri kotak prediksi dengan kotak anotasi, SGT menjalankan ulang percobaan cengkeraman di dalam simulator dan menilai keberhasilan berdasarkan apakah objek benar-benar terangkat dan berpindah. Eksperimen dengan jaringan AlexNet menunjukkan bahwa model yang dilatih pada Jacquard menggeneralisasi jauh lebih baik ke objek yang tidak pernah dilihat dibandingkan model yang dilatih pada Cornell, termasuk pada uji coba dengan lengan robot nyata (78,43% dibandingkan 60,46% tingkat keberhasilan).

## Latar Belakang: Masalah yang Ingin Dipecahkan

Deteksi *grasp* memprediksi posisi, ukuran, dan orientasi cengkeraman yang aman bagi *gripper* (penjepit) dua-rahang dari citra sebuah objek. Metode berbasis jaringan saraf dalam untuk tugas ini membutuhkan data berlabel dalam jumlah besar, sedangkan sumber data yang tersedia sebelum Jacquard saling bertolak belakang kelemahannya. Pelabelan manusia menghasilkan anotasi akurat tetapi sangat lambat: *dataset* Cornell, acuan utama pada masanya, hanya memuat 885 citra dari 240 objek dengan 8.019 kotak *grasp* berlabel tangan — terlalu kecil untuk melatih jaringan dalam agar menggeneralisasi ke objek baru, dan bias terhadap cengkeraman yang nyaman bagi tangan manusia, belum tentu sesuai untuk *gripper* dua-rahang paralel.

Percobaan fisik dengan robot nyata — misalnya pengumpulan 50.000 percobaan oleh satu lengan Baxter, atau lebih dari 800.000 titik data oleh 14 lengan robot yang berjalan selama dua bulan — menghasilkan data lebih banyak, tetapi memerlukan waktu, perangkat keras, dan campur tangan manusia untuk menata ulang objek di depan robot pada setiap percobaan. Pendekatan lain, Dex-Net 2.0, membuat 6,7 juta citra kedalaman sintetis berlabel keberhasilan sebuah kandidat *grasp* tunggal di tengah citra; jaringan yang dilatih di atasnya hanya bisa menilai (*ranking*) kandidat yang dihasilkan metode lain, bukan memprediksi posisi *grasp* secara langsung dari citra. Ada pula percobaan simulasi pada 1.000 objek oleh peneliti lain yang datanya tidak pernah dirilis untuk umum. Belum ada *dataset* yang sekaligus berskala besar, otomatis dihasilkan, memuat citra RGB-D realistis, dan dirilis terbuka untuk publik.

## Ide Utama

Gagasan inti Jacquard adalah mengganti seluruh proses pelabelan manusia dengan simulasi fisika tertutup: model CAD tiga dimensi dijatuhkan ke sebuah bidang, dirender menjadi citra layaknya kamera nyata, lalu diuji langsung oleh sebuah *gripper* virtual untuk menentukan kandidat cengkeraman mana yang benar-benar berhasil mengangkat objek. Karena keberhasilan diuji oleh fisika simulasi dan bukan diberi label oleh manusia, proses ini dapat diulang jutaan kali tanpa biaya tenaga kerja tambahan, dan hasilnya langsung memuat kebenaran fisik, bukan sekadar kemiripan geometris dengan anotasi rujukan.

Representasi *grasp* yang dipakai mengikuti format yang sudah dipakai *dataset* Cornell: sebuah cengkeraman dinyatakan sebagai vektor lima dimensi g = {x, y, h, w, θ}, yaitu posisi pusat kotak (x, y), ukuran kotak (h, w), dan sudut orientasi θ terhadap sumbu horizontal citra. Representasi ini menyatakan *grasp* sepenuhnya dalam koordinat citra dua dimensi; posisi rahang pada sumbu kedalaman dan arah pendekatan lengan ditentukan kemudian dari citra kedalaman saat *grasp* dieksekusi.

## Cara Kerja Langkah demi Langkah

Diagram berikut merangkum alur pembuatan satu adegan Jacquard, dari model CAD sampai citra dan anotasi jadi:

```
        Model CAD (subset ShapeNetSem)
                    |
                    v
   Pembuatan adegan: objek dijatuhkan ke bidang,
        posisi dan orientasi awal acak
                    |
        +-----------+-----------+
        v                       v
   Rendering (Blender)    Simulasi grasp (pyBullet)
   - citra RGB             - ribuan kandidat grasp acak
   - depth asli            - uji rigid-body, jaw 2 cm
   - depth stereo (noise)  - kandidat sukses diuji ulang
   - mask objek              pada 5 ukuran jaw lain
                            - buang kandidat berdekatan
        +-----------+-----------+
                    v
     Jacquard: 54.000 citra, 11.000 objek,
             1,1 juta anotasi grasp
```

### Pembuatan Adegan

Setiap adegan dibangun dengan pola yang sama. Sebuah bidang bertekstur putih dijadikan alas, dengan tekstur yang dirotasi dan digeser secara acak agar latar belakang tidak selalu identik. Satu objek dipilih dari kumpulan model CAD ShapeNetSem — subset ShapeNet yang memuat anotasi semantik — lalu diskalakan ulang sehingga sisi terpanjang kotak pembatasnya berada antara 8 dan 90 sentimeter, dengan massa yang mengikuti ukurannya (80 gram untuk objek 8 cm, 900 gram untuk objek 90 cm). Objek dijatuhkan dari posisi dan orientasi acak di atas bidang; begitu mencapai posisi diam yang stabil, konfigurasi adegan disimpan dan diteruskan ke dua modul independen: rendering citra dan simulasi *grasp*. Untuk setiap objek dibuat hingga lima adegan berbeda agar tersedia beberapa sudut pandang.

### Rendering Citra

Citra RGB dan citra kedalaman (*depth*) sebenarnya dirender dengan Blender memakai *Cycles Renderer*. Untuk kedalaman yang lebih realistis, penulis tidak menambahkan derau Gaussian buatan pada citra kedalaman sempurna, melainkan merender dua citra RGB tambahan dengan pola cahaya terproyeksi lalu menerapkan algoritme *stereo-vision* (visi stereo) *semiglobal matching* pada keduanya, menghasilkan citra kedalaman berderau yang menyerupai keluaran sensor sungguhan. Sebuah *mask* biner yang memisahkan objek dari latar belakang turut dihasilkan pada tahap ini.

### Pembuatan Anotasi Grasp

Anotasi dihasilkan dengan pustaka fisika waktu-nyata pyBullet. Untuk mempercepat perhitungan, tumbukan (*collision*) tidak dihitung pada *mesh* asli objek, melainkan pada dekomposisi cembung hierarkis (*approximate convex decomposition*) yang menyederhanakan bentuknya. *Gripper* dua-rahang paralel disimulasikan dengan bukaan maksimum 10 cm dan lebar rahang (*jaw*) yang bervariasi pada nilai {1, 2, 3, 4, 6} cm; variasi ini, digabung dengan variasi skala objek, membuat simulator menjajaki cengkeraman pada rentang konfigurasi yang luas.

Proses anotasi berjalan tiga tahap. Pertama, ribuan kandidat *grasp* acak dibangkitkan di seluruh area di bawah kamera dengan distribusi probabilitas tidak seragam — lebih sering pada area yang diperkirakan menjanjikan, memakai heuristik kepadatan tepi (*edge*) sejajar pada citra, sehingga kandidat tidak terbuang pada area kosong. Kedua, seluruh kandidat diuji lewat simulasi benda tegar (*rigid body*) memakai *gripper* berlebar rahang 2 cm; sebuah percobaan dinyatakan berhasil bila objek terangkat, berpindah, dan diletakkan kembali pada lokasi tertentu. Ketiga, posisi yang lolos tahap kedua diuji ulang dengan seluruh ukuran rahang lain, sehingga setiap posisi *grasp* akhir memiliki catatan satu sampai lima ukuran rahang yang berhasil untuknya. Kandidat berhasil yang letaknya terlalu berdekatan kemudian disaring agar setiap posisi cengkeraman hanya dianotasikan sekali.

### Kriteria Evaluasi: Simulated Grasp Trial

*Dataset* Cornell mengevaluasi prediksi *grasp* dengan metrik geometris berbasis kotak: sebuah prediksi dianggap benar bila sudutnya berselisih kurang dari 30 derajat dari kotak anotasi **dan** rasio *Intersection over Union* (IoU — luas irisan dibagi luas gabungan dua kotak) melampaui 25%. Metrik ini dapat keliru menilai: prediksi yang secara visual tampak baik bisa dinyatakan salah karena kebetulan tidak cocok dengan anotasi yang ada, padahal satu objek biasanya punya banyak posisi cengkeraman valid yang tidak semuanya teranotasi.

Sebagai koreksi, penulis mengusulkan SGT: ketika sebuah prediksi *grasp* perlu dinilai, adegan yang bersangkutan dibangun ulang di simulator, dan *gripper* virtual mencoba melakukan cengkeraman pada koordinat prediksi tersebut, dalam kondisi identik dengan saat anotasi awal dibuat. Prediksi dinyatakan berhasil bila objek terangkat dan berpindah, terlepas dari kecocokannya dengan anotasi mana pun. Penulis juga merilis antarmuka web bagi peneliti lain untuk mengirim kandidat *grasp* ke simulator dan menerima hasil evaluasi SGT tanpa perlu menjalankan simulator sendiri.

## Eksperimen dan Hasil

Efektivitas Jacquard diuji lewat dua rangkaian eksperimen memakai jaringan AlexNet siap-pakai (bobot konvolusi dipralatih pada ImageNet, lapisan terhubung penuh dilatih dari awal; citra kedalaman dinormalkan dan disisipkan menggantikan salah satu kanal warna agar sesuai format masukan AlexNet).

Eksperimen pertama adalah evaluasi lintas-*dataset*. Untuk perbandingan yang setara, dipakai subset Jacquard berisi 15.000 citra dari 3.000 objek terpilih dengan 316.000 posisi *grasp*, dibandingkan dengan seluruh Cornell (885 citra, 240 objek, 8.019 *grasp*). Jaringan yang dilatih pada Cornell dan diuji pada dirinya sendiri (validasi silang 5-lipat) mencapai 86,88% akurasi metrik kotak; saat diuji pada Jacquard, akurasinya turun menjadi 54,28% metrik kotak (selisih 32,6 poin) dan hanya 42,76% menurut metrik SGT — bukti bahwa jaringan tersebut gagal menggeneralisasi ke objek yang lebih beragam. Sebaliknya, jaringan yang dilatih pada Jacquard mencapai 74,21% metrik kotak dan 72,42% metrik SGT saat diuji pada Jacquard sendiri, dan tetap mencapai 81,92% metrik kotak saat diuji pada Cornell — mendekati kinerja dasar Cornell (86,88%) walaupun jaringan itu tidak pernah dilatih pada satu pun citra Cornell. Interpretasinya: keragaman objek dan posisi *grasp* pada Jacquard membuat jaringan menggeneralisasi jauh lebih baik ke domain data lain, sementara jaringan yang dilatih pada Cornell yang kecil dan seragam tidak mampu melakukan hal yang sama.

Eksperimen kedua menguji prediksi *grasp* dengan lengan robot Fanuc M-20iA bergripper dua-rahang, pada 28 objek nyata (15 mainan/perabot dan 13 komponen industri). Jaringan yang dilatih pada subset 2.000 objek Jacquard mencapai tingkat keberhasilan 78,43%, sedangkan jaringan yang dilatih pada Cornell hanya 60,46% — selisih 18 poin yang mengonfirmasi keunggulan generalisasi yang sama dengan evaluasi lintas-*dataset*, kali ini pada robot fisik sungguhan. Sebagian besar kegagalan pada jaringan berbasis Jacquard bukan karena kotak prediksi keliru, melainkan karena cengkeraman kurang stabil: objek terangkat pada awalnya tetapi terjatuh selama lengan bergerak.

## Kelebihan dan Keterbatasan

Kelebihan utama Jacquard terletak pada kombinasi skala dan otomatisasi: simulasi menghasilkan 1,1 juta anotasi tanpa pelabelan manusia, jauh melampaui Cornell, sekaligus mempertahankan modalitas RGB-D dan beragam ukuran *gripper* yang tidak dimiliki *dataset* otomatis lain seperti Dex-Net 2.0. Metrik SGT juga menjadi kontribusi tersendiri karena menilai keberhasilan fungsional cengkeraman, bukan sekadar kecocokan geometris, sehingga lebih dekat dengan kondisi nyata di mana satu objek dapat memiliki banyak posisi cengkeraman valid yang tidak semuanya teranotasi. Eksperimen lintas-*dataset* dan uji robot nyata memberi bukti langsung bahwa data sintetis berskala besar bisa mengungguli data hasil pelabelan manusia yang kecil dalam hal generalisasi ke objek baru.

Dari sisi keterbatasan, penulis sendiri mencatat bahwa metode ini hanya mencakup skenario satu objek tunggal di atas bidang datar, dan menyebutkan perluasan ke adegan lebih kompleks dengan banyak objek sebagai kerja mendatang. Secara konseptual, keberhasilan *grasp* di sini hanya diverifikasi terhadap simulator fisika yang menyederhanakan gesekan, deformasi, dan sifat material objek nyata; kesenjangan simulasi-ke-nyata (*sim-to-real gap*) ini tampak pada uji robot, ketika sebagian kegagalan Jacquard-terlatih disebabkan ketidakstabilan saat objek berpindah, bukan kesalahan lokasi cengkeraman. Dari sisi rekayasa, representasi *grasp* lima dimensi yang dipakai juga terbatas pada cengkeraman planar dua-rahang paralel, belum mencakup orientasi pendekatan tiga dimensi penuh (*6-DoF grasp*) yang dibutuhkan untuk objek dengan geometri lebih rumit.

## Kaitan dengan Bab Lain

Jacquard dibangun langsung sebagai jawaban atas keterbatasan skala *dataset* Cornell, yang mendasari metode deteksi *grasp* berbasis citra tunggal pada bab [080 - 2015 - Deep Learning Robotic Grasps (Lenz dkk.) - Grasp Robotik](./080%20-%202015%20-%20Deep%20Learning%20Robotic%20Grasps%20%28Lenz%20dkk.%29%20-%20Grasp%20Robotik.md), yang memperkenalkan representasi kotak *grasp* lima dimensi yang tetap dipakai Jacquard. Skala dan format RGB-D Jacquard kemudian menjadi salah satu data pelatihan standar bagi arsitektur konvolusi generasi berikutnya, termasuk [082 - 2020 - GR-ConvNet - Grasp Robotik](./082%20-%202020%20-%20GR-ConvNet%20-%20Grasp%20Robotik.md) dan turunannya [083 - 2022 - GR-ConvNet v2 - Grasp Robotik](./083%20-%202022%20-%20GR-ConvNet%20v2%20-%20Grasp%20Robotik.md), serta metode fusi RGB-D pada [085 - 2023 - BCMFNet (Bilateral Cross-Modal Fusion) - Grasp Robotik](./085%20-%202023%20-%20BCMFNet%20%28Bilateral%20Cross-Modal%20Fusion%29%20-%20Grasp%20Robotik.md). Pendekatan pembuatan data lewat simulasi fisika yang dipelopori Jacquard juga sejalan dengan gagasan yang diperluas ke skenario multi-objek dan penggenggaman 3D penuh pada [084 - 2020 - GraspNet-1Billion - Grasp Robotik](./084%20-%202020%20-%20GraspNet-1Billion%20-%20Grasp%20Robotik.md), yang menaikkan lagi skala anotasi *grasp* sintetis-realistis ke tingkat lebih tinggi.

## Poin untuk Sitasi

Kutip dengan kunci `depierre2018jacquard`. Ringkasan yang aman dikutip: "Jacquard adalah *dataset* deteksi *grasp* sintetis yang dihasilkan sepenuhnya lewat simulasi fisika terhadap model CAD ShapeNetSem, memuat 54.000 citra RGB-D dari lebih dari 11.000 objek dengan 1,1 juta anotasi cengkeraman, dan memperkenalkan metrik evaluasi *Simulated Grasp Trial* yang menilai keberhasilan fungsional alih-alih kecocokan geometris semata." Angka hasil AlexNet (86,88%; 81,92%; 54,28%; 74,21%; 42,76%; 72,42%; 78,43%; 60,46%) diambil langsung dari Tabel II dan bagian eksperimen naskah asli. Catatan: naskah menyebut jumlah citra Cornell sebagai 885 pada bagian narasi tetapi 1.035 pada tabel ringkasan *dataset* (Table I) — perbedaan ini ada pada sumber asli, perlu diverifikasi ulang bila dikutip untuk perbandingan presisi jumlah citra Cornell.
