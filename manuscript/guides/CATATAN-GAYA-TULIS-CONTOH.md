# Catatan Gaya Tulis Artikel Contoh dan Penerapannya pada main6

Catatan ini merekam cara artikel contoh (Xiao dkk., *Computers and Electronics in
Agriculture* 253 (2026) 112078; badan teks halaman 1–23, tabel lampiran halaman
23–29) menyampaikan isinya, dan cara penerapannya pada `main6`
(`manuscript/source/main6.tex` dan `main6-body.tex`). Kajian dilakukan pada
1 Oktober 2026 dari lima sudut: penamaan, arsitektur seksi, konstruksi paragraf,
pelaporan metode, serta bagian depan dan penutup. Tata letak dibahas terpisah di
`CATATAN-FORMAT-CONTOH.md`. Batasan pembimbing tetap berlaku: judul, empat
pertanyaan riset, tujuh kelompok kajian, klasifikasi enam mekanisme, urutan
seksi, tanggal pencarian, dan seluruh angka tidak berubah. Nomor baris merujuk
`main6-body.tex` kecuali disebut lain; kutipan contoh diberi nomor halaman (h.).

## 1. Jawaban singkat

Belum. Penanganan bukti pada `main6` sudah lebih kuat daripada contoh (tabel
perbandingan pada data yang sama, aturan penilaian bukti di baris 79, seksi
keterbatasan, kalimat pembuka paragraf berupa klaim, angka dan jenis referensi
untuk hampir setiap kajian). Yang belum sama adalah cara penyampaiannya.

1. **Kode menggantikan nama.** Contoh tidak memakai satu pun kode buatan; enam
   kategorinya selalu ditulis dengan kata. `main6` memuat 45 token M0–M5 pada 27
   baris, ditambah RQ1–RQ4, G1–G5, Q1–Q9, serta huruf V/D/S/T/1 dan GV/HH/LB/FX
   di Lampiran A. Abstrak `main6` (`main6.tex` baris 80) sudah tanpa kode, jadi
   perbaikannya adalah soal konsistensi.
2. **Kerangka tidak mengikat seksi.** Lima tahap di baris 107 sudah sepadan
   dengan Seksi 4–8, tetapi naskah tidak pernah menyatakannya. Sesudah baris 76
   tidak ada satu pun rujukan silang antarseksi.
3. **Seksi tanpa pembuka dan penutup.** Seksi 2 dan 3 langsung masuk ke
   subseksi; Seksi 3, 4, 5.1, 5.2, 5.4, dan 8 berakhir pada rincian satu kajian.
4. **Sitasi tercetak dua kali.** Nama diketik tangan 69 kali
   (`Name \textit{et al.}`) lalu disusul `\cite`, yang dipetakan ke `\citep`
   (`main6.tex` baris 16). Tahun tidak tampak di samping nama, sehingga
   "Wang et al." menunjuk tiga makalah berbeda (baris 229, 235, 263).
5. **Gambar dan tabel belum menjadi bagian argumen.** Gambar umumnya ditempel
   dalam kurung sesudah angka, panel (b) Fig. `fig:mek` tidak pernah dirujuk,
   judul gambar memuat temuan dan catatan cara hitung, dan Lampiran A hanya
   dirujuk sekali (baris 131).
6. **Metode tercampur.** Kriteria ditulis sebagai satu kalimat panjang (baris
   51), paragraf penyaringan memuat enam hal (baris 73), aturan keputusan
   pengodean tidak ada, dan metode peta istilah berada di subseksi hasil (baris
   96).
7. **Abstrak, pendahuluan, simpulan, dan penutup belum lengkap.** Abstrak tanpa
   kalimat celah, standar pelaporan, dan alur rekaman; pendahuluan tanpa
   paragraf peta isi; simpulan (baris 334) mengulang abstrak; empat pernyataan
   penutup belum ada.

## 2. Penamaan kategori dan singkatan

Praktik contoh:

- Enam kategori diberi nama dari kata biasa dan tidak pernah diberi kode:
  "Crossing these two dimensions yields six conceptual categories (static-single,
  static-multi, real-time-single, real-time-multi, hybrid-single, and
  hybrid-multi)" (h. 2).
- Nama yang sama dipakai dengan panjang bertingkat: bentuk panjang di definisi
  dan judul ("4.1. Static-information-based global path planning for
  single-vehicle systems", h. 11), bentuk sedang di prosa ("Static-information
  methods primarily rely on pre-acquired maps, field boundaries, or waypoints",
  h. 2), dan satu kata di judul gambar ("Fig. 5. Number of studies per year by
  information type (static, real-time, hybrid).", h. 8).
- Kategori didefinisikan dengan aturan keputusan: "To improve reproducibility,
  coding followed explicit decision rules." (h. 4).
- Pertanyaan dinomori di dalam kalimat tanpa awalan: "Accordingly, the review
  addresses three questions: (1) How are the static, real-time, and hybrid
  information sources used for path planning" (h. 2). Celah diberi angka Romawi
  dan judul deskriptif: "(i) Limited exploitation of hybrid information at the
  fleet level." (h. 21).
- Pencarian dilaporkan dengan satu kueri wakil tanpa pengenal: "A representative
  Web of Science query (Topic, TS) was" (h. 3).
- Tidak ada daftar singkatan; setiap akronim teknis dijabarkan saat pertama
  muncul, termasuk yang umum: "degraded Global Navigation Satellite System
  (GNSS) reception" (h. 1).
- Sel tabel lampiran berisi kata, bukan huruf sandi: "Satellite imagery;
  polygonal approximation" (h. 24).

Peta penamaan untuk `main6` (klasifikasi tetap; hanya labelnya yang berubah):

| Kode sekarang | Nama saat definisi dan di judul | Bentuk pendek dalam prosa | Label sel tabel atau gambar | Kode dipertahankan |
|---|---|---|---|---|
| M0 | No association | no association | No association | Tidak |
| M1 | Statistical correction | statistical correction; statistical-correction baseline | Statistical | Tidak |
| M2 | Appearance matching | appearance matching | Appearance | Tidak |
| M3 | Temporal tracking | tracking (sesudah nama lengkap muncul di paragraf itu) | Tracking | Tidak |
| M4 | Geometric or 3D association | geometric association | Geometric | Tidak |
| M5 | Learned association | learned association | Learned | Tidak |
| M2+M3, M3+M4, dan lainnya | tidak ada judul | appearance matching combined with temporal tracking | Appearance + tracking; Tracking + geometric (urutan tetap mengikuti klasifikasi) | Tidak |
| DATA | dataset paper | dataset paper | Dataset paper | Tidak |
| V, D, S, T, 1 | acquisition design | video along a path; discrete views; 3D scan; revisits over time; a single view | Video; Discrete views; 3D scan; Revisits; Single view | Tidak |
| GV, HH, LB, FX | platform | ground vehicle or robot; handheld device or smartphone; laboratory or conveyor | Ground vehicle; Handheld; Laboratory (FX dihapus, tidak ada baris yang memakainya) | Tidak |
| UAV | unmanned aerial vehicle (UAV), dijabarkan sekali | UAV | UAV | Ya (akronim baku) |
| count, det, track, none, n.a., -- | metric type | count agreement; detection quality; identity metric | Count; Detection; Identity; None; No abstract; Not stated | Tidak |
| RQ1–RQ4 | (1)–(4) dalam daftar | the first question; the question on class attributes | (1) Mechanisms and the conditions each assumes, dan seterusnya | Tidak |
| G1–G5 | (i)–(v) dengan judul miring yang sudah ada | dirujuk dengan judulnya | tidak ada | Tidak |
| Q1–Q9, Q8a–Q8e | nama sasaran kueri | oil-palm imaging query, dan seterusnya | Oil-palm imaging (Q3) | Ya, hanya sebagai kunci antara tabel kueri dan Lampiran B |
| C1–C5, R, T (internal) | tujuh nama kelompok | multi-observation studies; single-view counting studies; oil-palm studies; single-image class-wise counting studies; depth and 3D sensing studies; earlier reviews; methods papers from outside agriculture | sama | Tidak pernah tampil |

Catatan penerapan:

- Kode pada gambar dan lampiran adalah keluaran skrip. Perubahan label dilakukan
  di `tools/scopus/gambar_tinjauan.py` (kamus `NAMA_MEK`, baris 71–78, 243–245,
  266, 306, 359, 569–603), `tabel_lampiran.py`, dan `lampiran_kueri.py`; kunci
  di berkas data tetap.
- Satu istilah untuk satu konsep. Keluarga kategori selalu "association
  mechanism" (sekarang bercampur dengan "identity mechanism" di baris 76, 307,
  judul panel F04, dan sumbu F05). Mekanisme keempat selalu "geometric or 3D
  association" atau bentuk pendek "geometric association" (sekarang lima
  varian: baris 127, 134, 234, 318, dan legenda F04).
- Lampiran A memuat urutan kombinasi yang tidak tetap (M2+M3 24 baris dan
  M3+M2 4 baris; M3+M4 17 dan M4+M3 2), padahal teks dan F09 memperlakukannya
  sebagai satu kategori (28 dan 19).
- Akronim yang belum pernah dijabarkan di `main6`: SfM, SLAM, MOT, re-ID, RGB-D,
  LiDAR, UAV, MAE, MAPE, RMSE, MOTA, IDF1, HOTA, PRISMA. FFB dipakai di baris 37
  dan 66 sebelum dijabarkan di baris 73. Akronim yang hanya muncul sekali (mAP,
  IoU, GNSS) ditulis dengan kata.

## 3. Arsitektur seksi dan alur argumen

Praktik contoh:

- Kerangka diumumkan di pendahuluan, diberi aturan di metode, dihitung di
  subseksi lanskap, lalu dipakai untuk menata seksi bukti: "The framework
  underpins the quantitative synthesis, the scenario-based technical review, and
  the identification of research gaps." (h. 2).
- Pendahuluan ditutup dengan peta isi: "The remainder of this article is
  organised as follows." (h. 2).
- Setiap seksi dibuka dengan daftar tugasnya: "this section: (i) summarises
  major operational scenarios and navigation tasks; (ii) outlines typical
  machinery platforms" (h. 6). Seksi bukti dibuka dengan ukuran irisannya:
  "accounting for over 70% of the studies included in this review (Section
  3.4)" (h. 9).
- Subseksi yang padat kajian dipecah menjadi tren atau aliran berlabel: "Across
  the CCPP literature, five recurring algorithmic trends can be identified:"
  (h. 12); "A second research stream focuses on convoy- and formation-based
  cooperative navigation" (h. 19).
- Subseksi ditutup dengan sintesis, batas, dan penunjuk ke seksi berikutnya:
  "Collectively, these studies indicate that when accurate static maps are
  available, task allocation can be treated as a combinatorial optimisation
  problem" (h. 18); "This limitation motivates the subsequent multi-vehicle
  discussion in Section 5 and the cross-cutting analysis of evaluation protocols
  in Section 6." (h. 17).
- Diskusi adalah lapisan tersendiri yang tidak mengulang kajian: "This section
  synthesises the findings of Sections 3–5 from a system-level perspective"
  (h. 20), lalu celah lintas-topik: "Synthesising the three evolution lines
  reveals four major research gaps that cut across information sources,
  architectures, and operation modes." (h. 21).

Penerapan pada `main6` (urutan seksi tetap; tambahan sekitar 1.200–1.400 kata
berupa pembuka, penutup, label, dan rujukan silang):

- **Pemetaan tahap ke seksi dinyatakan tiga kali**: di peta isi pendahuluan, di
  kalimat serah-terima akhir Seksi 3 (sesudah baris 148), dan di kalimat pertama
  Seksi 4–8. Seksi 4 = tahap akuisisi, Seksi 5 = asosiasi, Seksi 6 = atribut,
  Seksi 7 = depth sebagai alat bantu observasi dan asosiasi, Seksi 8 = kasus.
- **Seksi 3.4** diganti judul menjadi "Quantitative landscape of the
  multi-observation studies" dan dipecah menjadi butir berlabel (i)–(v), satu
  gambar per butir, ditutup kalimat "Taken together".
- **Seksi 5** dibuka dengan pertanyaan yang dijawab, ukuran tiap mekanisme, dan
  alasan urutan subseksi. Subseksi pelacakan diberi empat label isu (baris
  225–229); subseksi geometri diberi lima aliran dan penutup "Where geometry
  fails" (baris 235–239).
- **Seksi 8** dipecah menjadi empat subseksi sesuai empat paragraf yang sudah
  ada (baris 277, 279, 281, 283).
- **Seksi 9** tetap di tempatnya, diberi pembuka yang menjelaskan alasan
  posisinya dan penutup yang mengantar ke Seksi 10.
- **Seksi 10** menjadi lapisan diskusi: lintasan mekanisme (dari baris 134,
  237, 241, dan hasil peta istilah baris 96), jawaban atas empat pertanyaan,
  lima celah (i)–(v) beserta seksi asalnya, dan daftar pelaporan minimum.
- Setiap subseksi bukti memuat minimal satu rujukan ke Seksi 3 dan setiap
  keterbatasan yang diangkat di Seksi 4–8 menunjuk ke Seksi 10. Subseksi diberi
  `\label` agar dapat dirujuk dengan nomor.

## 4. Konstruksi paragraf dan kalimat

Panjang kalimat kedua naskah setara (rerata contoh sekitar 27 kata; `main6`
20–31 kata), jadi kalimat `main6` tidak perlu dipanjangkan. Yang ditiru adalah
susunan paragrafnya. Paragraf bukti contoh mengikuti empat langkah: pembuka
tanpa kajian ("In CCPP, the planner generates trajectories that traverse all
reachable areas with minimal overlap and omission.", h. 11), dua sampai empat
kajian dengan nama dan tahun ("Mazzia et al. (2021) introduced
deep-learning-based waypoint extraction from aerial imagery, bridging the gap
between raw imagery and executable global routes.", h. 12), pernyataan lintas
kajian, lalu batasnya ("Despite these advances, most CCPP studies still rely on
idealised static maps and short-term experiments on single plots.", h. 14).

Aturan untuk `main6`, masing-masing dengan kalimat model dari isi yang sudah ada:

1. **Mekanisme disebut dengan nama.** "Discrete views taken around a tree have
   wide baselines and no temporal order, so temporal tracking does not apply and
   association must rely on appearance, geometry, or learning." (baris 188)
2. **Kajian yang diuraikan disitasi dengan `\citet`, satu kali, kata kerja
   lampau.** "`\citet{linker2015estimation}` photographed 42 apple trees from two
   sides at three heights, calibrated the summed counts against 14 trees, and
   obtained an orchard estimate within 10% of the actual yield." (baris 220)
3. **Pernyataan tentang beberapa kajian disitasi dengan `\citep` di akhir.**
   "In the two comparisons on the same apple and citrus data, DeepSORT did not
   outperform trackers that use motion alone and cost far more computation
   `\citep[Table~\ref{tab:assoc};][]{zhang2022deep,genemola2023video}`." (baris 227)
4. **Satu kajian per kalimat; kontras dengan "whereas"; rantai titik koma
   dipecah (baris 186, 222, 255, 263, 279, 281).** "`\citet{parico2021real}`
   found the unique-ID rule more reliable for pears (F1 87.85%), whereas
   `\citet{zhang2022deep}` counted citrus only when a track entered a fixed
   region." (baris 225)
5. **Subseksi mekanisme dibuka dengan nama, jumlah, dan penunjuk.** "Geometric
   association is used in 67 of the 182 multi-observation method studies (37%);
   they are listed in Appendix Table A1 and shown by crop in Fig. 6." (baris 134)
6. **Rangkaian kajian ditutup dengan pola dan batasnya, lalu penunjuk.** "Taken
   together, these studies show that tracking links fruit across consecutive
   frames but cannot, by itself, resolve the third source of double counting
   (Section 3.2); the studies that address it use geometric association
   (Section 5.4)." (baris 229)
7. **Temuan berjajar diberi label.** "(1) *A single image per side sees a
   minority of the fruit.* One image of one side counted 27% of the hand-counted
   fruit and one image of each side counted 54% on 16 mango trees." (baris 5, 186)
8. **Batas dinyatakan sebagai hitungan negatif, bukan kata penilaian.** "None of
   the 19 abstracts describes how a label is chosen when frames disagree, and
   none reports a class confusion matrix computed on unique fruit." (baris 259)
9. **Akronim dijabarkan saat pertama muncul.** "an identity metric such as
   multiple-object tracking accuracy (MOTA), the identification F1 score (IDF1),
   higher-order tracking accuracy (HOTA), or identity (ID) switches" (baris 245)
10. **Kala dan persona tetap**: lampau untuk kajian, kini untuk himpunan bukti,
    "this review" tanpa "we". Kontribusi diberi kata kerja: "First, the review
    provides a systematic map of 971 Scopus-indexed studies from 2012 to 2026."
    (baris 17)

Paragraf di atas kira-kira 150 kata atau lima kajian bernama dipecah pada
pergantian topik (baris 186, 235, 237, 263, 281).

## 5. Pelaporan metode dan lanskap kuantitatif

Praktik contoh:

- Seksi metode dibuka dengan tujuan dan alur kerja: "The review workflow
  comprised: (i) defining the research questions and scope; (ii) specifying
  inclusion and exclusion criteria" (h. 2).
- Kriteria berupa butir bernomor: "Studies were excluded if they: (i) were not
  related to agricultural contexts or to path planning for agricultural ground
  machinery" (h. 3).
- Tahap penyaringan disebut dan dikaitkan dengan diagram alur: "All retrieved
  records underwent three-stage screening: title screening, abstract screening,
  and full-text assessment." (h. 3).
- Subseksi pengodean menutup dengan kegunaan datanya: "The resulting dataset
  underpins the descriptive statistics in Section 3.4 and the comparative
  synthesis in Sections 4–6." (h. 4).
- Sintesis dilaporkan sebagai tiga prosedur, dan catatan per kajian dipindah ke
  lampiran: "To keep the main text focused on cross-study synthesis rather than
  study-by-study enumeration, the detailed coding records were organised in
  Appendix Tables A1-A9." (h. 5). Peta kata kunci dibatasi perannya: "This
  bibliometric analysis served for orientation only and did not affect study
  inclusion or quantitative conclusions." (h. 5).
- Lanskap dibuka dengan kaitan ke pengodean, lalu butir berlabel per gambar:
  "(i) Temporal trends and information sources. Fig. 5 shows that" (h. 7).
  Cara hitung dinyatakan di teks: "Because one study may include multiple
  algorithmic modules, the values in Fig. 8 represent category occurrences
  rather than mutually exclusive study counts." (h. 9).

Penerapan pada `main6`:

- **Seksi 2** mendapat pembuka (jenis tinjauan, tanpa penggabungan efek, PRISMA
  2020, alur kerja enam langkah) dan subseksi: *Data source*, *Search strategy*,
  *Inclusion and exclusion criteria*, *Study selection and screening*, *Data
  extraction and coding*, *Analytical framework*, *Evidence appraisal and
  synthesis*, *Search results and included studies*.
- **Kriteria** (baris 51) dinomori; tujuh alasan eksklusi ditulis dengan urutan
  dan kata yang sama dengan kotak diagram alur (21, 20, 26, 11, 71, 3, 1).
- **Penyaringan** (baris 73) dipecah menjadi tiga paragraf: tahap, penanganan
  rekaman, dan pelaksana. Pernyataan satu peninjau dengan model bahasa besar
  tanpa peninjau kedua tetap eksplisit.
- **Tujuh kelompok** didefinisikan sekali di subseksi pengodean dan diberi tabel
  kecil berisi jumlahnya (187, 231, 170, 49, 129, 119, 86; total 971) yang
  diambil dari keluaran skrip.
- **Aturan keputusan pengodean** ditambahkan dalam pola "A study was coded as X
  when ...". `PROTOKOL.md` bagian 5 hanya memuat nama mekanisme, jadi rumusannya
  harus dikonfirmasi penulis (bagian 8).
- **Metode peta istilah** (tiga kalimat pertama baris 96) pindah ke subseksi
  sintesis; frasa "As a check on the coding" diganti "As a supplementary
  perspective".
- **Seksi 3.4** menyatakan penyebut (182 kajian metode dari 187) dan catatan
  bahwa jumlah per mekanisme adalah kemunculan, bukan hitungan eksklusif (kini
  hanya di judul gambar baris 139). Dua hal yang perlu dilengkapi dari keluaran
  skrip: daftar akuisisi di baris 134 berjumlah 180 dari 182 (dua kajian
  *single view* tampil di F04 panel b), dan daftar platform di baris 148
  berjumlah 181 dari 182 (satu kajian *laboratory or conveyor* tampil di F09).
- **Aturan baca tabel** ("compared only within a row") dinyatakan saat Tabel
  `tab:acq` dan `tab:assoc` diperkenalkan (baris 164 dan 192), bukan hanya di
  keterbatasan (baris 330).

## 6. Abstrak, pendahuluan, tabel, gambar, simpulan, bagian penutup

**Abstrak.** Contoh memuat kalimat celah ("However, the evidence remains
fragmented across scenarios and information sources, and a scenario-aware
synthesis is still limited.", h. 1), alur rekaman ("564 records were screened
and 210 studies were included", h. 1), dan metode sintesis ("Descriptive
statistics, cross-tabulation, and keyword co-occurrence analysis were used to
synthesize the landscape.", h. 1). Abstrak `main6` ditambah kalimat celah,
PRISMA 2020, tanggal pencarian dan alur rekaman (6.491, 5.723, 971), variabel
pengodean, dan metode sintesis; semua angka sudah ada di baris 25 dan 82.

**Pendahuluan.** Contoh menyusun satu fungsi per paragraf: keterbatasan
tinjauan terdahulu ("prior reviews reveal four practical limitations", h. 2),
tujuan ("To address these issues, this article presents a scoping review",
h. 2), kontribusi ("This review makes three main contributions", h. 2),
kerangka, pertanyaan, peta isi. Baris 3–7 `main6` dipertahankan; baris 9–17
dibangun ulang dengan urutan itu, dan enam mekanisme disebut dengan nama satu
kali sebelum pertanyaan memakai kata "mechanisms".

**Gambar dan tabel.** Pada contoh, gambar atau tabel menjadi subjek kalimat
("The PRISMA-ScR flow diagram (Fig. 1) summarises the record counts at each
stage.", h. 3), judul hanya menyebut isi dan pengodean visualnya ("Fig. 3.
Keyword co-occurrence network (VOSviewer), where node size, edge width, and
colour represent keyword frequency, co-occurrence strength, and semantic
clusters, respectively.", h. 5), ukuran sampel ada di judul tabel ("(primary
studies, n = 185)", h. 5), dan keterangan berada di catatan bawah tabel ("Note:
NR indicates that the corresponding metric was not reported in the original
study.", h. 11). Untuk `main6`: temuan di judul F02 (baris 93) dan catatan cara
hitung di judul F04, F09, F10 (baris 139, 153, 159) pindah ke teks; judul
menjadi frasa benda dengan n; Tabel `tab:acq` dan `tab:assoc` mendapat catatan
(nilai seperti dilaporkan, dibandingkan hanya dalam satu baris, jabaran
akronim); kolom terakhir `tab:acq` menjadi "Count reference"; kolom terakhir
`tab:position` yang isinya seragam dihapus; Lampiran A memakai kata di setiap
sel dan judul satu kalimat; tabel lampiran dinomori A1.

**Simpulan.** Contoh menyusun simpulan sebagai ringkasan kerja, hal yang sudah
mapan, ketimpangan ("At the same time, the quantitative evidence reveals a
pronounced imbalance across the six conceptual categories defined by the
proposed framework.", h. 22), panduan desain ("three scenario-dependent
trajectories emerge that can serve as concrete design guidance", h. 22), dan
prioritas ("Looking forward, the synthesis supports five priorities that can
serve as a practical roadmap for the field:", h. 22). Seksi 12 `main6` disusun
ulang menjadi empat paragraf pendek (350–450 kata): yang dikerjakan; yang mapan
dan yang belum; panduan menurut desain akuisisi (dari baris 188, 229, 283);
lima prioritas (i)–(v). Kalimat yang sama dengan abstrak ditulis ulang.

**Bagian penutup.** Contoh memuat "CRediT authorship contribution statement"
(h. 23), pendanaan ("This research was funded by the National Natural Science
Foundation of China (Grant No. 32001412).", h. 23), pernyataan kepentingan
("The authors declare that they have no known competing financial interests or
personal relationships", h. 23), dan ucapan terima kasih. `main6` baru memuat
*Data availability* dan *Declaration of generative AI use* (baris 336–340);
empat pernyataan itu ditambahkan sesudah penulis memberi isinya.

## 7. Yang tidak ditiru dari contoh, dan alasannya

- **Pengulangan.** Peringatan yang sama muncul di h. 9 ("should be interpreted
  as representative KPI ranges rather than as a controlled benchmark or
  meta-analysis") dan lagi di h. 22 ("Therefore, Table 2 and Fig. 7 should be
  interpreted as a representative KPI synthesis rather than as a controlled
  benchmark or meta-analysis."). `main6` menyatakan setiap peringatan satu kali
  di tempat tabel diperkenalkan dan satu kali di keterbatasan.
- **Kata penilaian tanpa angka.** "SLAM has emerged as a core enabler for
  hybrid-single navigation" (h. 17); "remains an open research frontier"
  (h. 19). `main6` mempertahankan bentuk "N of M studies".
- **Besaran kabur.** "tend to report improved stability in cluttered or
  low-light conditions." (h. 16). `main6` mempertahankan nilai dan jenis
  referensinya.
- **Klaim pemeriksaan silang.** "Each study was coded by one author and
  cross-checked by another to ensure consistency." (h. 4). `main6` tidak dapat
  mengklaim ini; pernyataan satu peninjau tetap.
- **Persona bercampur.** "First, we propose a two-dimensional analytical
  framework" dan "This review followed PRISMA 2020" berada di halaman yang sama
  (h. 2). `main6` tetap memakai "this review".
- **Istilah tidak konsisten.** "information source × operation mode" (h. 2)
  menjadi "information type × operation mode" (h. 20); "MO-CCPP" (h. 11) menjadi
  "MO-CPP" ("In contrast to CCPP, MO-CPP studies exhibit a wider range of
  objectives", h. 15).
- **Simpulan panjang yang tumpang tindih dengan diskusi** (sekitar 1.100 kata,
  dengan lima prioritas berparagraf penuh mulai "(i) From isolated autonomy to
  cooperative fleets.", h. 23). Simpulan `main6` dibatasi 450 kata.
- **Tanpa seksi keterbatasan.** Contoh beralih dari "6.5. Implications for
  future research and deployment" (h. 22) langsung ke simpulan. Seksi 11 dan
  deklarasi AI `main6` dipertahankan.
- **Singkatan NR.** Praktik catatan bawah tabel ditiru, tetapi `main6` memakai
  kata "Not stated" (sudah dipakai di `tab:position` dan F09) agar tidak
  menambah singkatan baru.
- **Kelalaian sunting**, misalnya "The review Following the PRISMA 2020
  statement (Page et al., 2021)" (h. 2).

## 8. Yang memerlukan masukan penulis

1. Aturan keputusan pengodean mekanisme: dasar penetapan, perlakuan kombinasi,
   apakah urutan kode pada kombinasi (misalnya M3+M2 dan M2+M3) bermakna, cara
   menetapkan "counts per class", dan cakupan pemeriksaan acak.
2. Penyaringan: tindakan peninjau terhadap keputusan model, apakah teks lengkap
   dipakai pada tahap kelayakan, status uji kesepakatan pada sampel, dan apakah
   ada penelusuran sitasi (*snowballing*).
3. Isi *CRediT*, *Funding*, *Declaration of competing interest* (termasuk
   apakah peran penulis kedua sebagai penulis pertama makalah SawitMVC
   disebutkan), *Acknowledgment*, dan tautan bahan suplemen.
4. Label "RQ" pada Tabel `tab:rqmap`: dihapus mengikuti contoh, atau
   dipertahankan di tabel itu saja bila rencana verifikasi merujuknya.
5. Ejaan: `main6` memakai -ize dengan kosakata Inggris-Britania (satu
   pengecualian "summarised" di baris 25); contoh memakai -ise. Usulan: tetap
   -ize secara konsisten.
6. Ketidaksesuaian data: `nellithimaru2019rols` tercatat "apple" di Lampiran A,
   sedangkan baris 237 menyebut anggur.
7. "16% above NeRF-based methods" (baris 212, 237): persen atau poin persentase.
8. Deskripsi lima kajian tanpa asosiasi untuk subseksi 5.1 (judul menyebutnya,
   teks belum membahasnya).
9. Tambahan opsional yang memerlukan kerja skrip atau pembacaan ulang sumber:
   tabel silang desain akuisisi × mekanisme, pemisahan kolom metrik pada
   `tab:assoc`, dan tabel lampiran untuk 170 kajian kelapa sawit.
10. Batas kata abstrak dan jumlah kata kunci jurnal sasaran; kalimat implikasi
    di akhir abstrak; usulan enam kata kunci (*Fruit counting; Cross-view
    identity; Data association; Multi-object tracking; Class-wise inventory;
    Oil palm*).
11. Persetujuan pembimbing atas perubahan judul Seksi 10 ("Discussion: gaps and
    a measurement agenda") dan Seksi 12 ("Conclusions").
12. Versi perangkat lunak untuk peta istilah (NetworkX) dan kalimat tentang
    bidang yang dicari (judul saja atau judul, abstrak, dan kata kunci).
