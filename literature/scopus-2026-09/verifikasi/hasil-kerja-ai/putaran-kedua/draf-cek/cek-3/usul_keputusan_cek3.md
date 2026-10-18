Draf model tertanggal 12 Oktober 2026 dan belum diperiksa peninjau. Isinya usul, bukan keputusan; tidak ada berkas data, skrip, `.bib`, atau naskah yang diubah.

# Usul Keputusan Cek 3 (makalah dikenal dan penelusuran rujukan)

Sumber keadaan terkini: `topik/bukti/matriks_bukti.csv`, `topik/records_all.csv`, `topik/tambahan_metode_lain.csv`, `main6-body.tex`, `main6-appendix-c1.tex`, `references6.bib`, `verifikasi/log_perubahan.csv`, `PROTOKOL.md`. Rincian per kandidat: `usul_keputusan_cek3.csv`.

## Ringkasan

1. Semua 16 makalah dikenal (18 kunci) berada di peta dan dikutip di badan naskah. Perbedaan utama dari laporan 29 September: Häni dkk. 2020 kini C1 (M4, V, teks lengkap), dikutip 2 kali, dan ada di Lampiran A; Liu dan Ampatzidis kini rekaman metode lain (L1) yang dikutip 3 kali.
2. Lima mekanisme berubah sejak laporan lama (Stein, Zhang, Lee, Fusaro, Indriani). Semuanya diubah putaran kedua model pada 1 Oktober 2026 dan belum diperiksa manusia.
3. Dari 10 kandidat penelusuran rujukan, tidak ada yang tercatat di korpus. Tidak ada yang jelas C1. Tiga berada di luar rentang tahun, satu E1, satu E5, satu duplikat tesis dari idx 777, tiga memenuhi kriteria sebagai C2, dan satu sebagai C5.
4. Kalimat di subseksi Study selection and screening (baris 75 `main6-body.tex`: "ten candidates were examined and none met the criteria within the date range") benar hanya bila "criteria" dibaca sebagai kriteria multipengamatan (C1), dan satu kandidat (Apolo-Apolo dkk. 2020) berada di batas itu.

## A. Enam belas makalah dikenal

Kolom "Badan" adalah jumlah kemunculan kunci di `main6-body.tex` (termasuk sel tabel). Kunci tidak muncul di `main6.tex`. Semua kunci ada di `references6.bib`.

| No | Makalah | Kunci | idx | Kode | Mekanisme, akuisisi, sumber kode | Badan | Lamp. A | Beda dari 29 Sep |
|---|---|---|---:|---|---|---:|---|---|
| 1 | Stein 2016 | `stein2016image` | 766 | C1 | M3+M4, V, teks lengkap | 6 | ya | Mekanisme M4 menjadi M3+M4 |
| 2 | Liu 2018 | `liu2018robust` | 723 | C1 | M3+M4, V, abstrak | 2 | ya | Tidak ada |
| 3 | Liu 2019 | `liu2019monocular` | 699 | C1 | M3+M4, V, teks lengkap | 4 | ya | Tidak ada |
| 4a | Gené-Mola 2020 (LiDAR, aliran udara) | `genemola2020fruit` | 672 | C1 | M4, S, abstrak | 1 | ya | Tidak ada pada data; usul Cek 2 belum diterapkan (lihat D) |
| 4b | Gené-Mola 2020 (Mask R-CNN, SfM) | `genemola2020fruitb` | 4032 | C1 | M4, D, abstrak | 3 | ya | Tidak ada |
| 5 | Gené-Mola 2023 | `genemola2023video` | 449 | C1 | M3+M2, V, abstrak | 3 | ya | Tidak ada |
| 6 | Zhang 2022 (jeruk) | `zhang2022deep` | 535 | C1 | M3, V, teks lengkap | 4 | ya | Mekanisme M3+M2 menjadi M3 |
| 7 | Lee 2026 | `lee2026lidarcamera` | 53 | C1 | M4, V, teks lengkap | 1 | ya | Mekanisme M3+M4 menjadi M4 |
| 8 | Rapado-Rincón 2023 | `rapadorincon2023development` | 421 | C1 | M4+M3, V, teks lengkap | 3 | ya | Tidak ada pada data; usul Cek 2 belum diterapkan (lihat D) |
| 9 | Fusaro 2026 | `fusaro2026horticultural` | 37 | C1 | M2+M4+M5, T, teks lengkap | 1 | ya | Mekanisme M5 menjadi M2+M4+M5 |
| 10 | Indriani 2026 (SawitMVC) | `indriani2026sawitmvc` | 24 | C1 | M1, D, per kelas Y, teks lengkap | 6 | ya | Mekanisme DATA menjadi M1; usul Cek 2 buta kembali ke DATA (lihat D) |
| 11 | Lai 2022 | `lai2022real` | 1883 | C3 | modalitas RGB (sebelumnya RGB+DEPTH) | 1 | tidak (bukan C1) | Kode C3 sama; modalitas diubah putaran kedua |
| 12 | Shiddiq 2023 | `shiddiq2023counting` | 434 | C3 | - | 1 | tidak (bukan C1) | Tidak ada |
| 13 | Goh 2025 (set data RGB-D) | `goh2025outdoor` | 1509 | C3 | - | 1 | tidak (bukan C1) | Tidak ada |
| 14 | Suharjito 2025 (set data) | `suharjito2025oil` | 117 | C3 | - | 1 | tidak (bukan C1) | Tidak ada |
| 15a | Lai 2023 (tinjauan) | `lai2023oil` | 1796 | R | - | 4 | tidak | Tidak ada |
| 15b | Goh 2025 (tinjauan) | `goh2025fresh` | 1563 | R | - | 4 | tidak | Tidak ada |
| 16 | Häni 2020 | `hani2020comparative` | 1278 | C1 | M4, V, teks lengkap | 2 | ya | Kode C2 menjadi C1; dikutip 0 menjadi 2 kali; Lampiran A tidak menjadi ya |
| - | Liu dan Ampatzidis | `liu2026shaping` | tidak di matriks | R (metode lain, L1) | - | 3 | tidak berlaku | Dari usulan menjadi terpasang: `tambahan_metode_lain.csv`, `references6.bib` (tahun 2027, `scopuseid` lain-0001), kotak F01, Tabel `tab:position` |

Perubahan kode pada baris 1, 6, 7, 9, 10, 16 dan modalitas baris 11 tercatat di `verifikasi/log_perubahan.csv` (tanggal 2026-10-01, oleh AI-2) dengan alasan dari teks lengkap. Contoh: Stein, "pelacakan antarbingkai ... ditriangulasi ke 3D"; Lee, asosiasi hanya lewat tetangga terdekat 3D di peta SLAM.

Butir rencana tentang Häni (apakah pemetaan hasilnya menggabungkan pandangan): ya. Teks lengkap (`teks/hani2020comparative.txt`, Gambar 1) memuat langkah "Merge front/backside in 3D Remove double counted fruit, visible from front & backside". Hasil gabungan 95,56-97,83% dari hitungan panen (Tabel 4, h. 21 menurut log) terhadap 103,86-147,81% untuk penjumlahan dua sisi, sesuai baris Tabel `tab:assoc` di naskah. Pemindahan ke C1 sudah terjadi; yang tersisa adalah konfirmasi peninjau pada Cek 5.

Makalah dikenal yang tidak dikutip di badan naskah: tidak ada saat ini (Häni, satu-satunya kasus pada laporan lama, sudah dikutip).

## B. Sepuluh kandidat penelusuran rujukan

Pencocokan ke `records_all.csv` dan `matriks_bukti.csv` dilakukan lewat DOI (bila ada), lalu kemiripan judul (difflib) dan pencarian kata kunci judul. Tidak ada kandidat yang tercatat. Aturan stereo tidak mengubah keputusan apa pun; prioritas C1 hanya relevan pada Apolo-Apolo.

| # | Kandidat | Tahun | Usul | Kode atau alasan | Keyakinan |
|---|---|---:|---|---|---|
| 1 | Payne dkk., *Estimating mango crop yield ... night time imaging* (10.1016/j.compag.2013.11.011) | 2014 | MASUK | C2. Abstrak: deteksi 78,3%, R^2 0,63 terhadap hitungan manual; tidak menyebut dua sisi atau beberapa pandang. Klaim lama "kedua sisi pohon" tidak terbukti dari abstrak | sedang |
| 2 | Apolo-Apolo dkk., *Deep learning techniques ... citrus fruits using a UAV* (10.1016/j.eja.2020.126030) | 2020 | MASUK | C2, batas C1 (M1, D). Teks lengkap: dua citra per pohon (kiri, kanan); hitungan per sisi menjadi masukan LSTM tanpa asosiasi antar-sisi | sedang |
| 3 | Gongal, *Over-the-row machine vision system ...* (tesis MSc, WSU) | 2014 | TIDAK MASUK | Tesis; isinya terbit sebagai Gongal dkk. 2016 (idx 777, C1). Abstrak tidak diperoleh | sedang |
| 4 | Silwal dkk., *Apple identification in field environment with over-the-row machine vision system* (CIGR J. 16(4)) | 2014 | TIDAK MASUK | E5. Hanya akurasi identifikasi (90% pada 60 citra), tanpa hitungan | tinggi |
| 5 | Choi dkk., *Machine vision system for early yield estimation of citrus ...* (10.13031/aim.20152181863) | 2015 | MASUK | C5. Deteksi dengan informasi depth, dievaluasi hanya dengan laju identifikasi (72,1%); mengikuti preseden C5 idx 1360, 3451, 541, tetapi idx 3689 berkode E5 | sedang |
| 6 | Kwon dkk., *Enhancing citrus fruit yield investigations through flight height optimization ...* (10.1038/s41598-023-50921-8) | 2024 | MASUK | C2. Estimasi jumlah buah dari citra UAV tegak per ketinggian, terpisah, tiga pohon; risiko E3 karena hitungan berbasis piksel warna | sedang |
| 7 | Sapkota dkk., *3D reconstruction and information fusion between dormant and canopy seasons ...* (arXiv:2507.01912) | 2025 | TIDAK MASUK | E1. Objek batang dan cabang, bukan buah; praprint | tinggi |
| 8 | Swanson dkk., *A multi-modal system for yield prediction in citrus trees* (10.13031/2013.29916) | 2010 | TIDAK MASUK | Di luar rentang tahun | tinggi |
| 9 | Moonrinta dkk., *Fruit detection, tracking, and 3D reconstruction ...* (10.1109/ICARCV.2010.5707436) | 2010 | TIDAK MASUK | Di luar rentang tahun (nanas; isinya C1 menurut definisi) | tinggi |
| 10 | Chinchuluun dkk., *Machine vision-based citrus yield mapping system* (Proc. Fla. State Hort. Soc. 119) | 2006/2007 | TIDAK MASUK | Di luar rentang tahun (rujukan Gongal 2015 menulis 2007; OpenAlex 2006) | tinggi |

Hasil terhadap tujuan langkah opsional (C1 yang terlewat): nol kandidat C1 yang jelas. Dari abstrak yang terbaca, kandidat 9 satu-satunya yang menggabungkan pengamatan (pelacakan dan rekonstruksi 3D), tetapi terbit 2010.

Batas bukti: teks lengkap hanya dibaca sebagian untuk kandidat 2 (bagian 2.1 sampai 2.8) dan 6 (kutipan bagian metode dan diskusi). Kandidat 1 tidak memiliki berkas pada entri figshare akses terbukanya; kandidat 3, 4, 5, dan 10 hanya dinilai dari abstrak atau rujukan. Status indeks Scopus kandidat yang MASUK tidak diperiksa.

## C. Keputusan yang perlu diambil penulis

1. **Lingkup penambahan (kandidat 1, 2, 5, 6).** Keempatnya memenuhi kriteria inklusi umum, tetapi bukan C1, sedangkan langkah opsional Bu Fatma hanya meminta C1. Dua pilihan:
   - (A) Usul model: tidak menambahkan, dan mengubah kalimat di subseksi Study selection and screening menjadi "none was a multi-observation study". Alasannya, penelusuran ini hanya memeriksa judul yang tampak multipengamatan (57 dari 635 rujukan), sehingga penambahan sebagian C2 dan C5 membuat cakupan tidak seragam. Pemeriksaan DOI tambahan saya menemukan enam rujukan berentang 2012-2020 yang juga tidak ada di korpus dan tampak C2 atau E5 dari judulnya saja: *Deep count: fruit counting based on deep simulated learning* (10.3390/s17040905), *Using colour features of cv. Gala apple fruits ... to predict yield* (10.1007/s11119-012-9269-2), *Application of neural networks and image visualization for early forecast of apple yield* (10.1007/s10341-012-0162-y), *Multi-class fruit-on-plant detection for apple in SNAP system using Faster R-CNN* (10.1016/j.compag.2020.105634), *3DBunch* (10.1109/access.2020.3003415), dan *Detection of citrus fruit and tree trunks ... multi-elliptical boundary model* (10.1016/j.compind.2018.03.007). Abstrak keenam item itu tidak dibaca. Celah ini perlu disebut di keterbatasan; laporan lama sudah mencatat celah frasa kueri ("Estimating ... yield").
   - (B) Menambahkan keempatnya sebagai rekaman metode lain (C2 tiga, C5 satu): ubah `tambahan_metode_lain.csv`, jalankan ulang `gambar_tinjauan.py`, `angka_naskah.py`, `buat_bib.py`, dan perbarui kalimat di subseksi Study selection and screening serta angka PRISMA (metode lain 1 menjadi 5).
2. **Batas C1 untuk Apolo-Apolo dkk. 2020.** Dua citra per pohon yang hitungannya dijumlahkan oleh regresi mirip pola `linker2015estimation` dan `vijayakumar2023tree` (C1, M1, D), tetapi Cek 2 mengusulkan `vijayakumar2023tree` bukan C1. Selama aturan "beberapa pandang tanpa asosiasi buah" belum diputuskan Bu Fatma, kandidat ini tidak dapat dipastikan; bila dikodekan C1, kalimat itu salah dan pilihan A tidak berlaku tanpa mengubah isi kalimat.
3. **Tahun `liu2026shaping`.** `.bib` dan Tabel `tab:position` memakai 2027 (volume 256 bertanggal Januari 2027); rencana menulis 2026. Butir ini sudah tercantum di `SERAH-TERIMA.md` bagian 2 nomor 5.
4. **Isi Liu dan Ampatzidis tentang pelacakan.** Baris `tab:position` hanya bersandar pada abstrak. Klaim rencana bahwa tinjauan itu membahas pelacakan, ID switch, dan hitung ganda belum diverifikasi; laporan lama juga mencatat status akses terbukanya belum pasti. Masukkan ke permintaan PDF Cek 4 bila tertutup.
5. **Usul mekanisme yang masih tergantung** (butir D) memengaruhi apa yang dikatakan Tabel dan Lampiran A tentang makalah dikenal.

## D. Hal lain yang relevan

- **Usul Cek 2 yang belum diterapkan pada makalah dikenal** (`verifikasi/cek-2-cek-tangan/cek_C1.csv`, kolom `catatan`, belum dibaca peninjau): `indriani2026sawitmvc` penilai buta mengusulkan DATA (nilai kini M1, hasil putaran kedua); `rapadorincon2023development` penilai buta mengusulkan mekanisme DATA dan akuisisi D (nilai kini M4+M3 dan V), yang tampak janggal untuk makalah pelacakan tomat dan perlu dibaca peninjau; `genemola2020fruit` dinilai C1 dari definisi, dengan C5 sebagai alternatif bila rekonstruksi 3D tidak dihitung C1 dan usul mekanisme M1+M4.
- **Aturan yang belum ada**: pencacahan dari rekonstruksi 3D tanpa pelacakan dan penggabungan statistik antar-pandang. Keduanya memengaruhi kode Gené-Mola 2020 (LiDAR, rekonstruksi) dan Apolo-Apolo (gabungan statistik).
- **Rekaman yang ditandai laporan lama**, status 12 Oktober: Underwood dkk. 2016 (idx 4294) dan Zhou dkk. 2025 Agrosense (idx 3058) masih X pada tahap judul dan belum dibaca ulang; Payne 2013, Koirala 2019 (MangoYOLO), Anderson 2019, Qureshi 2017, Koirala 2021, Linker 2017 dan 2018, Bellocchio 2020, dan Vasconez 2020 masih C2. Payne 2014 yang diusulkan C2 konsisten dengan Payne 2013 (idx 841).
- **Angka naskah yang terkait**: kalimat "ten candidates" (baris 75) sama dengan jumlah baris `kandidat_snowballing.csv`. Bila pilihan B diambil, angka itu dan makro `\nOther` (kini 1) perlu diperbarui.
