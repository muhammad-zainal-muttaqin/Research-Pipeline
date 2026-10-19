# Angka Naskah `main6`

Dibuat `tools/scopus/angka_naskah.py`; jangan disunting tangan. Teks naskah memakai angka ini melalui makro di `manuscript/source/main6-angka.tex`.

## Seksi 2: alur rekaman

- Rekaman diambil 6,491; unik 5,889; duplikat 602
- Dibuang menurut tipe dokumen 166; judul disaring 5,723; dikeluarkan di tahap judul 4,578
- Dinilai kelayakannya 1,145 (dengan abstrak 891; judul dan sumber saja 254)
- Dikeluarkan di tahap kelayakan 132: E1 23, E2 18, E3 25, E4 1, E5 60, E6 4, E7 1
- Masuk peta dari Scopus 1013: C1 199, C2 243, C3 171, C4 52, C5 138, R 122, T 88
- Metode lain 5: liu2026shaping (R), payne2014estimating (C2), apoloapolo2020deep (C1), choi2015machine (C5), kwon2024enhancing (C2)
- Total kajian masuk 1018
- Kajian per tahun: 2012: 9, 2013: 14, 2014: 13, 2015: 16, 2016: 22, 2017: 25, 2018: 29, 2019: 39, 2020: 67, 2021: 73, 2022: 90, 2023: 117, 2024: 166, 2025: 196, 2026: 137
- Multi-pengamatan per tahun: 2012: 1, 2013: 2, 2014: 4, 2015: 1, 2016: 3, 2017: 2, 2018: 1, 2019: 5, 2020: 10, 2021: 14, 2022: 13, 2023: 27, 2024: 36, 2025: 48, 2026: 32
- Dengan abstrak 787 dari 1013; PDF teks lengkap 476 (teks terekstrak 472); multi-pengamatan dengan PDF 197 dari 199
- Peta istilah: 43 istilah, 317 tautan; istilah identitas 24-37 kajian; detection 621; counting 431

## Seksi 3: kajian multi-pengamatan

- Multi-pengamatan 199; makalah dataset 4; kajian metode 195
- Kemunculan mekanisme: temporal tracking 126 dari 195 (65%); geometric or 3D association 79 dari 195 (41%); appearance matching 57 dari 195 (29%); statistical correction 13 dari 195 (7%); no association 1 dari 195 (1%); learned association 8 dari 195 (4%)
- Kajian yang menggabungkan mekanisme: 84
- Kategori eksklusif: M2+M3 52, M4 52, M3 47, M3+M4 19, M1 12, M4+M5 3, M2+M3+M4 3, M3+M5 2, M2+M4+M5 1, M3+M4+M5 1, M0+M3 1, M2+M5 1, M1+M3 1
- Akuisisi (V video, D diskret, S pindaian 3D, T kunjungan ulang, 1 satu pandang): V 138, D 20, S 33, T 4, 1 0
- Periode 2012-2017 (n = 13): M1 2 (15%), M3 3 (23%), M4 10 (77%)
- Periode 2018-2020 (n = 14): M3 6 (43%), M4 12 (86%)
- Periode 2021-2022 (n = 27): M0 1 (4%), M1 3 (11%), M2 8 (30%), M3 18 (67%), M4 7 (26%), M5 1 (4%)
- Periode 2023-2024 (n = 61): M1 5 (8%), M2 24 (39%), M3 45 (74%), M4 17 (28%), M5 2 (3%)
- Periode 2025-2026 (n = 80): M1 3 (4%), M2 25 (31%), M3 54 (68%), M4 33 (41%), M5 5 (6%)
- Periode sejak 2023 (n = 141): M1 8 (6%), M2 49 (35%), M3 99 (70%), M4 50 (35%), M5 7 (5%)
- Tanaman: apple 52, (tanaman tidak disebut) 23, citrus 21, grape 21, tomato 19, strawberry 11, mango 7, oil palm 6, sweet pepper 6, cotton 5, pear 4, passion fruit 3
- Melaporkan hitungan per kelas: 25 dari 195
- Akuisisi x kategori mekanisme: V: M2+M3 52, M3 46, M4 17, M3+M4 12, M1 4; D: M4 11, M1 8, M4+M5 1; S: M4 23, M3+M4 7, M4+M5 2, M2+M3+M4 1; T: M2+M4+M5 1, M4 1, M2+M3+M4 1, M3 1
- Pandangan diskret: dengan asosiasi geometris 12, dengan koreksi statistik 8
- Platform (satu kategori per kajian): tidak disebut 118, ground vehicle/robot 39, lebih dari satu 17, UAV 11, handheld/smartphone 6, conveyor/lab 4
- Modalitas (kemunculan): RGB 162, RGB-D 14, LiDAR 7, stereo 6, multispectral 4, monocular depth 2, hyperspectral 1
- Pencocokan penampilan: satu-satunya mekanisme pada 0, digabung pada 57
- Kajian no association: daud2022loose
- Kajian learned association: arizasentis2023object, arizasentis2025comparative, fusaro2026horticultural, meyer2025fruitnerf, santos2026multi, xia2022culling, zhao2026adapting, zheng2023object
- Makalah dataset: arizasentis2023dataset, arizasentis2024grapemots, genemola2020fuji, genemola2020lfuji
- Dasar pengodean kajian multi-pengamatan: teks lengkap 195, abstrak 4
- Referensi hitung (kemunculan): anotasi 125, pohon 43, panen 28, tidak ada 19, packhouse 1
- Tingkat metrik menurut pengodean kajian (kemunculan): hitung 157, deteksi 135, identitas 70, tidak ada 4
- Cara pemberian kelas pada kajian per kelas: tidak dinyatakan 12, saat pelacakan 10, voting antarpandang 2, sesudah pelacakan 1

## Seksi 5: metrik di abstrak kajian metode multi-pengamatan

- Dengan abstrak 149 dari 195: hitung 64 dari 149 (43%); deteksi 58 dari 149 (39%); identitas 18 dari 149 (12%); tanpa metrik 53 dari 149 (36%)

## Seksi 6: pencacahan per kelas pada citra tunggal

- Kajian 52; tanaman: tomato 18, (tanaman tidak disebut) 7, blueberry 7, apple 5, coffee 4, strawberry 2
- Atribut kelas kematangan: 46

## Seksi 7: kedalaman dan sensor lain

- Kajian 138; modalitas (kemunculan): RGB-D 81, RGB 32, stereo 20, LiDAR 13, monocular depth 3, NIR 3, hyperspectral 2, thermal 2, multispectral 1
- Tanaman: apple 48, (tanaman tidak disebut) 16, grape 14, tomato 14, citrus 13

## Seksi 8: kelapa sawit

- Kajian 171 (matriks: 171)
- Tugas: KLS 76, DET 42, MUTU 18, SENSOR 16, LF 12, DATA 4, HIT 3
- Lokasi: ? 136, POHON 13, PABRIK 11, TANAH 8, UAV 3
- Modalitas: RGB 139, ? 5, MSI 5, TERMAL 5, RGB+DEPTH 3, HSI 2, LASER 2, LIDAR 2, RGB+LASER 2, RGB+NIR 1, RGB+RADAR 1, MSI+NIR 1, STEREO 1, MSI+TERMAL 1, RGB+NIR+DEPTH 1
- Multipandang Y: 17; kelas per instans Y: 131
- Kajian pencacahan (HIT): hamdani2026automated, naftali2024palm, prasetyo2020automatic
- Kajian multipandang: arief2026machine, cherie2015advance, cherie2015optical, cherie2020optical, cherie2021non, fadilah2012intelligent, hidayat2024establishing, junior2023video, naftali2024palm, omar2024outdoor, salambue2018investigation, shiddiq2024multispectral, shiddiq2024neural, suharjito2023annotated, suharjito2023real, suharjito2025oil, wang2024novel

## Seksi 9: tinjauan terdahulu dan metode luar pertanian

- Tinjauan terdahulu 122 (+ 1 metode lain); metode luar pertanian 88

## Pemeriksaan ulang tahap judul

- Sampel judul 300: eksklusi judul yang layak setelah abstrak dibaca 11
- Eksklusi judul kueri Q1 dan Q3 dibaca abstraknya: 1325; dimasukkan kembali 19

## Cek 1: sampel buta peninjau terhadap keputusan model

- Judul: sepakat 256 dari 300 (85%); kappa 0.57
- Kelayakan (kode penuh): sepakat 86 dari 165 (52%); kappa 0.45
