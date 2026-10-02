# Pertanyaan untuk Bu Fatma tentang Rencana Verifikasi

Disiapkan 29 September 2026 untuk ditempel sebagai komentar pada dokumen
rencana (tenggat 1 Oktober 2026). Setiap pertanyaan diikuti satu baris alasan.
Rincian pendukung ada di `cek_makalah_dikenal.md` dan `kandidat_snowballing.csv`.

## 1. Peninjau kedua dan Cek 1–2

1. **Siapa peninjau kedua, dan bagaimana ia disebut di naskah?** Apakah Ibu
   sendiri (penulis kedua), atau orang lain yang perlu disebut di
   *Acknowledgements*?
   *Alasan:* kalimat "No second, independent reviewer checked the decisions"
   akan diganti, dan naskah tidak boleh mengklaim lebih dari yang dikerjakan.
2. **Apakah sampel Cek 1 perlu distratifikasi?** Sampel sekarang acak sederhana:
   300 dari 5.723 judul dan 100 dari 1.124 abstrak (benih 20260929).
   *Alasan:* kelompok kecil (C4 49, T 86) bisa hanya muncul beberapa kali,
   sehingga kappa per kelompok tidak stabil; stratifikasi menurut keputusan AI
   (lolos/eksklusi) atau menurut kelompok memperbaikinya.
   **2a. Apakah 100 abstrak diambil dari seluruh tahap abstrak atau dari 300 judul?**
   Rencana menulis "300 records from the title stage; 100 records from the
   abstract stage". Kami menafsirkannya sebagai dua sampel terpisah: 300 dari
   5.723 judul dan 100 dari 1.124 rekaman tahap abstrak.
   *Alasan:* hanya sekitar 20% judul lolos ke abstrak, sehingga 300 judul
   menghasilkan sekitar 59 abstrak, kurang dari 100. Mohon konfirmasi sebelum
   lembar abstrak diisi.
3. **Kappa dihitung pada keputusan apa, dan berapa batas lulusnya?**
   Dua kelas (lolos/eksklusi), atau tujuh kode kelompok? Bila di bawah batas
   (misalnya κ < 0,6), apa tindak lanjutnya?
   *Alasan:* kriteria perlu ditetapkan sebelum hasil dilihat agar tidak bias.
4. **Siapa yang mengisi Cek 1?** Lembar Cek 2 memperlihatkan keputusan AI,
   jadi saya akan mengisi Cek 1 lebih dulu sebelum membuka lembar Cek 2.
   Apakah cukup saya yang mengisi, atau perlu orang lain yang belum pernah
   melihat keputusan AI sama sekali?
   *Alasan:* Cek 1 hanya sah bila pengisinya buta terhadap keputusan AI.
5. **Pada Cek 5, bila PDF sebuah kajian C1 tidak bisa diperoleh (Cek 4), apakah
   cukup dikode ulang dari abstrak dan ditandai "abstrak saja"?**
   *Alasan:* kalimat naskah "a person recoded C1 from full text" harus sesuai
   jumlah yang benar-benar dibaca penuh.
6. **Bagaimana aturan C1 untuk studi yang menjumlahkan hitungan dua sisi pohon
   lalu mengalibrasinya?** Linker 2015 dikode C1 (M1), tetapi Linker 2017/2018,
   Payne 2013, MangoYOLO 2019, dan Anderson 2019 dikode C2. Häni 2020 (salah
   satu dari 16 makalah dikenal) juga C2 dan belum dikutip di naskah.
   *Alasan:* aturan ini bisa mengubah angka 187 dan perlu diputuskan sebelum
   Cek 5.

## 2. Cek 3: Liu dan Ampatzidis

7. **Apakah makalah ini dihitung dalam total peta (971 + 1 = 972; R 119 → 120),
   atau hanya muncul di kotak PRISMA "metode lain" dan Tabel IV, sementara
   gambar kuantitatif tetap berbasis Scopus (971)?**
   *Alasan:* pilihan kedua menjaga semua angka dapat dihitung ulang dari
   Scopus; pilihan pertama sesuai templat PRISMA 2020 tetapi mengubah beberapa
   angka di teks.
8. **Tahun sitasi 2026 atau 2027?** Artikel terbit daring 14 September 2026,
   tetapi masuk CEA volume 256 bertanggal Januari 2027.
   *Alasan:* justru karena itu kueri `PUBYEAR < 2027` tidak akan menemukannya
   walau dijalankan ulang; naskah perlu menjelaskannya dalam satu kalimat.
9. **Status akses terbuka belum pasti** (OpenAlex: hybrid CC BY-NC-ND; Crossref
   dan ScienceDirect tidak menunjukkan lisensi terbuka). Bolehkah saya
   memasukkannya ke daftar permintaan PDF Cek 4?
   *Alasan:* klaim bahwa review ini membahas pelacakan dan hitung ganda belum
   terlihat di abstrak dan harus dicek ke teks lengkap.
10. **Apakah *backward snowballing* satu putaran dari lima review terdekat
    dijadikan bagian resmi "metode lain"?** Persiapannya sudah ada: dari 57
    judul relevan, 45 sudah tertangkap Scopus; hanya tiga kandidat kuat dalam
    rentang tahun (Payne 2014, Apolo-Apolo 2020, Gongal 2014).
    *Alasan:* contoh review CEA memakai *snowballing*; hasil ini juga menjadi
    bukti bahwa kueri Scopus cukup lengkap.

## 3. Sumber, jurnal, dan kebijakan

11. **Apakah keterbatasan "Scopus saja" dapat diterima?** Contoh review
    (Xiao dkk. 2026) memakai Web of Science ditambah *snowballing* dua arah.
    *Alasan:* menambah WoS berarti tanggal dan angka pencarian berubah
    (bertentangan dengan rencana); *snowballing* (butir 10) lebih murah dan
    menjawab kritik yang sama.
12. **Perlukah celah frasa kueri disebut di keterbatasan?** Dua kandidat kuat
    lolos karena judulnya "Estimating ... yield" atau "estimation of the
    yield", tidak cocok dengan `"yield estimat*"`.
    *Alasan:* lebih jujur daripada diam, dan tidak mengubah tanggal pencarian.
13. **Jurnal sasaran *Computers and Electronics in Agriculture* (CEA)?** Dokumen
    repo mengarah ke CEA (pola review CEA 2026, rencana `elsarticle`, contoh
    review dari CEA).
    *Alasan:* panduan CEA menentukan pernyataan AI, data, *highlights*, dan
    format.
14. **Pernyataan AI:** panduan penulis CEA meminta seksi baru sebelum daftar
    pustaka berjudul *Declaration of generative AI and AI-assisted technologies
    in the manuscript preparation process*, penggunaan hanya dengan pengawasan
    manusia, dan AI tidak boleh dicantumkan sebagai penulis. Naskah sekarang
    menulis bahwa model bahasa ikut menyaring, mengode, menulis skrip, dan
    menyusun draf. Apakah Ibu setuju dengan cakupan pengakuan itu, dan apakah
    peran AI dalam penyaringan cukup dijelaskan di Metode?
    *Alasan:* peran AI dalam proses riset (penyaringan) berbeda dari bantuan
    menulis, dan editor akan menilai keduanya.
15. **Ketersediaan data:** CEA memakai "Option C" (data wajib disimpan di
    repositori dan dikutip, atau diberi alasan bila tidak bisa). Repositori mana
    yang dipakai (mis. Zenodo atau Mendeley Data), dan atas nama siapa?
    *Alasan:* naskah sekarang hanya menulis "provided as supplementary
    material".
16. **Pernyataan lain untuk `elsarticle`:** CRediT, pendanaan, konflik
    kepentingan, 3–5 *highlights* (≤85 karakter), dan *graphical abstract*.
    Mohon informasi pendanaan dan pembagian peran.
    *Alasan:* bagian ini belum ada di `main6` dan dibutuhkan saat 25 November.

## 4. Usulan tambahan dari contoh review (mohon diputuskan)

17. **Tabel silang mekanisme × akuisisi** (meniru Tabel 1 contoh review). Angka
    awal dari matriks sekarang (182 studi metode; satu studi bisa dihitung di
    beberapa mekanisme): video — M3 112, M4 35, M2 31, M1 7; pandangan diskret
    (37) — M4 24, M1 10, M3 1, **M2 0**. Perlukah juga kode "mekanisme dominan"
    (yang benar-benar menghapus duplikat) pada Cek 5 agar tabel saling lepas?
    *Alasan:* murah (data sudah ada), langsung menopang G4, dan tidak mengubah
    judul, RQ, kelompok, maupun struktur.
18. **Gambar lintasan teknis per tahun** (M1 kalibrasi → M3 pelacakan → M4 3D
    dan representasi implisit → M5 terlatih), sebagai pengganti atau pelengkap
    Gambar 4a.
    *Alasan:* contoh review menyusun sintesisnya sebagai lintasan; data per
    tahun sudah tersedia.
19. **Perlukah pembandingan dengan sistem penghitung buah komersial?**
    *Alasan:* contoh review melakukannya untuk navigasi, tetapi sumbernya
    literatur abu-abu di luar Scopus; bila diinginkan, sebaiknya satu paragraf
    "konteks, bukan bukti".
20. **Perlukah peta kata kunci VOSviewer dan daftar periksa PRISMA-ScR?**
    Usul saya: PRISMA-ScR ya (lampiran tambahan, murah), VOSviewer tidak
    (contoh review sendiri menyatakan analisis itu hanya orientasi).
    *Alasan:* menjaga naskah tetap ringkas tanpa kehilangan kepatuhan
    pelaporan.

## 5. Pola dari contoh review (Xiao dkk. 2026) dan usulan untuk main6

Contoh: Xiao dkk. (2026), *Research progress of autonomous navigation path
planning methods for agricultural ground machinery: a review*, CEA 253:112078.
Kolom terakhir menjawab apakah usulan bertentangan dengan pernyataan rencana
bahwa "hanya sedikit suntingan; judul, RQ, kelompok, mekanisme, struktur, dan
tanggal pencarian tetap".

| Aspek | Xiao dkk. 2026 | main6 sekarang | Yang kurang di main6 | Biaya | Bertentangan? |
|---|---|---|---|---|---|
| Struktur | Pendahuluan → Metode → masalah, platform, kerangka, lanskap kuantitatif, sistem komersial → sintesis per kategori (4, 5) → diskusi, celah, implikasi → kesimpulan → Lampiran A1–A10 | Pendahuluan → Metode → ruang desain → akuisisi → bukti per mekanisme → atribut kelas → depth → sawit → posisi → celah dan agenda → keterbatasan → kesimpulan; Lampiran A, B | Tidak ada | — | Tidak |
| Pedoman pelaporan | PRISMA 2020 + PRISMA-ScR, diagram alir PRISMA-ScR | PRISMA 2020 "where the items apply" | Daftar periksa PRISMA-ScR sebagai bahan tambahan | Rendah | Tidak |
| Sumber | WoS Core Collection + *snowballing* mundur dan maju | Scopus saja, 13 kueri, tanggal 28 Sep 2026 | *Snowballing*; kotak "metode lain" | Sedang (persiapan sudah ada) | Tidak, bila hanya sebagai "metode lain"; ya bila menambah WoS |
| String kueri | Satu kueri "representatif" | 13 string lengkap di Lampiran B | Tidak ada (main6 lebih lengkap) | — | Tidak |
| Kriteria kelayakan | Artikel jurnal, bahasa Inggris, 2019–2025 | E1–E7, termasuk prosiding, 2012–2026 | Tidak ada | — | Tidak |
| Kerangka analitis | Dua dimensi: sumber informasi × mode operasi → 6 kategori | Lima tahap + mekanisme M0–M5 (satu dimensi); akuisisi dikode terpisah | Menampilkan mekanisme × akuisisi sebagai kerangka dua dimensi | Rendah | Tidak (memakai kode yang ada; mekanisme tidak berubah) |
| Tabel silang | Tabel 1, 185 studi primer, aturan penyaringan eksplisit | Gambar 4 (proporsi per periode; akuisisi terpisah), Gambar 5 (tanaman × mekanisme) | Tabel mekanisme × akuisisi dengan angka pasti dan aturan multi-label/dominan | Rendah | Tidak |
| Statistik deskriptif | Studi per tahun per kategori, skenario × mode, sensor × skenario | Gambar 2, 4, 5, 6, 7 | Hitungan per tahun per mekanisme (bukan hanya proporsi per periode) | Rendah | Tidak |
| VOSviewer | Jaringan dan peta kerapatan kata kunci, "orientation only" | Tidak ada | Opsional; nilai rendah | Rendah–sedang (kata kunci pengarang belum diunduh) | Tidak, tetapi menambah gambar tanpa menjawab RQ |
| Lintasan teknis | Statis → waktu nyata → hibrida, dipakai sebagai benang sintesis dan kesimpulan | Tersirat ("before 2018 M1 and M4 only; since 2023 tracking in about 70%"; M4 bergerak ke 3D dan representasi implisit) | Satu paragraf dan satu gambar lintasan yang eksplisit | Rendah | Tidak |
| Pembandingan komersial | Gambar 10, sistem John Deere, Case IH, dsb. | Tidak ada | Paragraf konteks sistem penghitung buah komersial | Sedang–tinggi (literatur abu-abu) | Ya, bila dijadikan bukti; tidak, bila hanya konteks |
| Pengodean | "Coded by one author and cross-checked by another"; ketidaksepakatan diselesaikan lewat diskusi; tanpa kappa | Satu peninjau + model bahasa; diakui di Metode dan Keterbatasan | Hasil Cek 1 (kappa), Cek 2 (cek tangan C1/C3/eksklusi), Cek 5 (kode ulang teks lengkap) | Sesuai rencana | Tidak (memang rencana) |
| Tabel lampiran | A1–A9 rekaman pengodean per kategori, A10 KPI | Lampiran A: matriks 187 C1; keputusan dan kode sebagai bahan tambahan | Opsional: lampiran kode C3 (170 studi sawit) | Rendah (skrip lampiran sudah ada) | Tidak |
| Tabel kinerja | Tabel 2 KPI + Gambar 7, dengan peringatan "not a controlled benchmark" | Tabel II dan III (perbandingan pada data yang sama, acuan, tingkat metrik) + Gambar 7 | Tidak ada (main6 lebih ketat) | — | Tidak |
| Tantangan dan arah | Empat celah lintas-kategori, implikasi, protokol pelaporan minimum, lima prioritas | G1–G5 dengan ukuran, himpunan pelaporan minimum | Tidak ada | — | Tidak |
| Keterbatasan tinjauan | Tidak ada seksi khusus | Ada (Scopus saja, abstrak, satu peninjau, OA) | Perbarui dengan hasil Cek 1–5; tetap "Scopus only" | Rendah | Tidak |
| Pernyataan akhir | CRediT, pendanaan, konflik kepentingan, data "on request" | Ketersediaan data, pernyataan AI | CRediT, pendanaan, konflik kepentingan, *highlights*, judul pernyataan AI sesuai CEA | Rendah | Tidak |

Ringkasan usulan: tambahan yang murah dan tidak bertentangan adalah tabel
silang mekanisme × akuisisi, gambar lintasan per tahun, daftar periksa
PRISMA-ScR, satu putaran *snowballing* sebagai "metode lain", dan pernyataan
akhir `elsarticle`. Yang bertentangan dengan rencana adalah menambah WoS atau
menyusun ulang seksi menurut kategori dua dimensi; keduanya tidak saya usulkan.
