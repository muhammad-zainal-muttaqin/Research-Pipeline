# 202 - Focusable Monocular Depth Estimation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `du2026focusabledepth` |
| Judul asli | Focusable Monocular Depth Estimation |
| Penulis | Yuxin Du, Tao Lin, Zile Zhong, Runting Li, Xiyao Chen, Jiting Liu, Chenglin Liu, Ying-Cong Chen, Yuqian Fu, Bo Zhao |
| Tahun | 2026 |
| Venue | arXiv preprint arXiv:2605.11756 (belum melalui peer review pada saat penulisan bab ini) |
| Tema | Estimasi Kedalaman |

## Tautan Akses
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2605.11756
- **Google Scholar:** https://scholar.google.com/scholar?q=Focusable%20Monocular%20Depth%20Estimation
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Focusable%20Monocular%20Depth%20Estimation&sort=relevance

## Gambaran Umum

Makalah ini mendefinisikan tugas baru bernama *Focusable Depth Estimation* (FDE, estimasi kedalaman yang dapat difokuskan): diberi sebuah citra RGB tunggal dan penanda wilayah target (berupa kotak pembatas atau deskripsi teks), model harus memprediksi peta kedalaman (*depth map*, citra yang setiap pikselnya menyatakan jarak permukaan ke kamera) yang secara khusus akurat pada wilayah target itu, mempertahankan batas objek yang tajam, tanpa merusak koherensi geometri seluruh citra. Untuk menjawab tugas ini, penulis mengusulkan **FocusDepth**, kerangka yang menggabungkan model fondasi segmentasi *Segment Anything Model 3* (SAM3) dengan model fondasi kedalaman keluarga *Depth Anything* melalui modul fusi bernama *Multi-Scale Spatial-Aligned Fusion* (MSSA). Sebagai alat ukur, makalah ini juga membangun **FDE-Bench**, kumpulan data evaluasi berisi 252.900 triplet (citra, wilayah target, kedalaman) untuk pelatihan dan 72.500 triplet untuk validasi, disusun dari lima kumpulan data RGB-D yang sudah ada. Hasil utama menunjukkan FocusDepth secara konsisten mengungguli model Depth Anything yang disetel halus (*fine-tuned*) pada metrik wilayah latar-depan dan batas objek, dengan penurunan akurasi global yang minimal.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Model estimasi kedalaman monokular modern, seperti Depth Anything V2 (bab 175) dan Depth Anything 3 (bab 198), dilatih dengan tujuan meminimalkan galat rata-rata pada seluruh piksel citra. Perlakuan seragam ini masuk akal untuk pemetaan ruangan atau navigasi umum, tetapi bermasalah pada aplikasi yang berpusat pada satu objek. Dalam manipulasi robotik, lengan robot perlu mengetahui kedalaman objek yang akan digenggam dengan presisi tinggi di sekitar batas objeknya, sementara galat kecil pada latar belakang jauh tidak berpengaruh terhadap keberhasilan tugas. Karena fungsi *loss* standar memberi bobot setara ke semua piksel, model semacam itu cenderung menghasilkan kedalaman yang baik secara rata-rata tetapi kabur tepat di batas objek — daerah yang justru paling menentukan bagi genggaman atau augmented reality (AR, penambahan objek virtual yang berinteraksi dengan geometri nyata).

Pendekatan lain, seperti model kedalaman metrik universal UniDAC (bab 201) atau kerangka *real-time* AsyncMDE (bab 200), memperbaiki aspek skala metrik dan kecepatan inferensi, tetapi tidak menyediakan mekanisme bagi pengguna untuk menyatakan wilayah mana yang penting saat itu. Survei estimasi kedalaman metrik monokular (bab 199) mencatat pola umum ini: hampir seluruh tolok ukur kedalaman menilai kinerja secara global, tanpa metrik yang secara eksplisit menilai wilayah target. Ketiadaan pengondisian wilayah dan ketiadaan tolok ukur yang menilainya menjadi dua kekosongan yang coba diisi oleh makalah ini.

## Ide Utama

Gagasan inti FocusDepth adalah memisahkan dua kebutuhan yang selama ini digabung dalam satu jaringan: kemampuan memahami geometri scene secara umum (disediakan oleh model kedalaman fondasi yang sudah terlatih) dan kemampuan memahami *ke mana* pengguna ingin model itu memperhatikan wilayah tertentu (disediakan oleh model segmentasi fondasi yang sudah terlatih untuk memahami prompt/penanda). Alih-alih melatih ulang model kedalaman dari nol dengan data berlabel wilayah, FocusDepth menyuntikkan sinyal fokus dari SAM3 ke dalam jalur fitur Depth Anything melalui modul fusi yang menjaga korespondensi posisi spasial antara kedua sumber fitur.

Secara mekanis, model menerima tiga masukan: citra RGB, dan prompt wilayah berupa kotak pembatas atau kalimat deskripsi objek (misalnya "cangkir merah di meja"). Cabang geometri (Depth Anything) mengekstrak fitur multi-skala dari citra seperti biasa, tanpa mengetahui prompt. Cabang prompt (SAM3) menghasilkan token yang menandai lokasi wilayah target. Modul MSSA kemudian menyelaraskan kedua kelompok fitur ini secara spasial pada tiap skala, lalu menyuntikkan informasi wilayah target ke fitur geometri hanya pada lokasi yang relevan, tanpa mengganggu representasi geometri di wilayah lain. Keluaran akhirnya tetap berupa satu peta kedalaman utuh untuk seluruh citra, tetapi bagian yang berkorespondensi dengan wilayah target diberi perhatian ekstra selama pelatihan dan inferensi.

## Cara Kerja Langkah demi Langkah

### Dua Cabang Ekstraksi Fitur

FocusDepth memakai dua model fondasi yang sudah terlatih sebagai tulang punggung (*backbone*, jaringan ekstraksi fitur dasar). Cabang geometri memakai *encoder* Depth Anything (varian DA2 atau DA3) untuk menghasilkan fitur multi-skala dari citra RGB — fitur pada beberapa resolusi berbeda, dari kasar (menangkap struktur scene) sampai halus (menangkap tekstur dan batas objek). Cabang prompt memakai SAM3, model segmentasi yang mampu menghasilkan token sadar-prompt (*prompt-aware token*) dari masukan berupa kotak pembatas atau teks, yaitu representasi vektor yang menandai lokasi dan bentuk kasar wilayah yang dimaksud pengguna.

### Multi-Scale Spatial-Aligned Fusion (MSSA)

MSSA adalah komponen yang menggabungkan dua cabang tersebut, terdiri atas tiga tahap pada setiap skala fitur geometri:

1. **Penyelarasan spasial per-skala**: token prompt dari SAM3 diproyeksikan ke ruang token geometri Depth Anything, dengan korespondensi satu-ke-satu terhadap grid patch (petak kecil citra yang menjadi unit dasar token) pada skala tersebut. Tanpa penyelarasan ini, informasi prompt bisa "bocor" ke lokasi yang salah pada peta kedalaman.
2. **Fusi kondisional beralur (routed conditional fusion)**: fitur yang sudah selaras diproses lewat lapisan *Mixture-of-Experts* (MoE, gabungan beberapa sub-jaringan "ahli" ringan yang masing-masing menspesialisasi diri) berisi empat *expert*, sehingga koreksi yang diterapkan dapat berbeda-beda bergantung lokasi spasial pada citra.
3. **Fusi bergerbang (gated fusion)**: hasil fusi digabungkan kembali dengan fitur geometri asli melalui gerbang sigmoid yang dapat dipelajari (*learnable sigmoid gate*, unit yang mengatur seberapa besar proporsi sinyal baru dicampur dengan sinyal lama). Mekanisme ini menjaga agar pengetahuan yang sudah dipelajari Depth Anything pada tahap pra-pelatihan tidak dirusak oleh sinyal prompt yang baru.

Berikut diagram alur data dari dua cabang masukan hingga peta kedalaman akhir:

```
citra RGB ──► Depth Anything (encoder) ──► fitur geometri multi-skala
                                                    │
prompt (kotak/teks) ──► SAM3 ──► token prompt       │
                                       │             │
                                       ▼             ▼
                              ┌─────────────────────────────┐
                              │   MSSA (per skala fitur)     │
                              │  1. penyelarasan spasial     │
                              │  2. fusi MoE (4 expert)      │
                              │  3. gerbang sigmoid          │
                              └─────────────────────────────┘
                                            │
                                            ▼
                                   decoder kedalaman
                                            │
                                            ▼
                              peta kedalaman (fokus tajam
                              pada wilayah target, global
                              tetap koheren)
```

### Strategi Pelatihan Dua Tahap

Pelatihan dilakukan dalam dua tahap. Pada tahap pertama, seluruh modul pralatih (Depth Anything dan SAM3) dibekukan (*frozen*, bobotnya tidak diperbarui), dan hanya modul penyelarasan MSSA yang dioptimalkan, sehingga proses belajar penyelarasan spasial tidak terganggu oleh perubahan representasi dasar. Pada tahap kedua, *encoder* tetap dibekukan, sementara MSSA, *decoder* kedalaman, dan cabang segmentasi bantu disetel halus bersama. Pemisahan dua tahap ini mencegah sinyal fokus yang masih kasar merusak fitur geometri yang sudah matang sejak awal pelatihan.

### Kerugian (Loss) Sadar-Wilayah

Fungsi *loss* pelatihan dipecah menjadi tiga komponen wilayah: galat pada wilayah latar-depan (bagian dalam target), galat pada pita batas objek (didefinisikan sebagai pita morfologis selebar 10 piksel di sekitar tepi target), dan galat global pada seluruh citra. Ketiganya diberi bobot terpisah sehingga model didorong memprioritaskan latar-depan dan batas tanpa mengabaikan konsistensi geometri di luar wilayah target.

## Eksperimen dan Hasil

Evaluasi utama memakai FDE-Bench, yang dibangun dari lima kumpulan data RGB-D: NYU v2 (adegan dalam ruangan), RLBench dan RoboTwin (simulasi tugas robotik/*embodied*), YCB-Video (objek meja), dan TUM RGB-D (sekuens SLAM — *Simultaneous Localization and Mapping*, pemetaan sekaligus penentuan posisi kamera). Metrik yang dilaporkan adalah AbsRel (*Absolute Relative error*, rata-rata selisih absolut relatif terhadap kedalaman sebenarnya — makin kecil makin baik) dan δ₁ (persentase piksel dengan galat di bawah ambang tertentu — makin besar makin baik), masing-masing dihitung terpisah untuk tiga wilayah: latar-depan, batas, dan global.

Pada pengujian dengan prompt kotak di RLBench, FocusDepth berbasis DA3 dilaporkan menurunkan AbsRel batas objek dari 0,073 (baseline DA3 yang disetel halus tanpa fokus wilayah) menjadi 0,049, AbsRel latar-depan dari 0,095 menjadi 0,056, dan AbsRel global dari 0,042 menjadi 0,030. Interpretasinya: perbaikan terbesar terjadi tepat pada dua wilayah yang menjadi sasaran utama makalah ini (batas dan latar-depan), sementara metrik global justru ikut sedikit membaik, bukan memburuk — menunjukkan bahwa penyuntikan sinyal fokus tidak mengorbankan pemahaman geometri keseluruhan. Model juga diuji dengan prompt berbasis teks; ketika teks yang diberikan tidak akurat atau dikosongkan, kinerja menurun dibandingkan prompt yang benar, tetapi tetap melampaui baseline tanpa fokus wilayah sama sekali, yang oleh penulis disebut sebagai kegunaan sisa (*residual usefulness*) dari arsitektur MSSA meski tanpa panduan prompt yang tepat.

Uji ablasi (pengujian dengan mencabut satu komponen untuk mengukur kontribusinya) menunjukkan penyelarasan spasial sebagai komponen paling kritis: mengacak urutan token prompt menaikkan AbsRel sekitar 13,8%. Menghilangkan fusi khusus per-skala menurunkan kinerja sekitar 10%, demikian pula mengganti fusi MoE beralur dengan satu lapisan *multilayer perceptron* (MLP) tunggal. Menghilangkan gerbang sigmoid menurunkan kinerja 2–5,4%. Melatih hanya dengan *loss* global tanpa pemecahan wilayah mengorbankan akurasi latar-depan sebesar 10,7–12%. Angka-angka ablasi ini konsisten menunjukkan bahwa setiap komponen MSSA memberi kontribusi terukur, dengan penyelarasan spasial sebagai fondasi yang paling menentukan.

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini terletak pada pemanfaatan dua model fondasi yang sudah matang (Depth Anything untuk geometri, SAM3 untuk pemahaman wilayah) tanpa melatih ulang keduanya dari nol, sehingga biaya pelatihan lebih rendah dibandingkan membangun model kedalaman sadar-wilayah dari awal. Pembangunan FDE-Bench juga mengisi kekosongan tolok ukur yang secara eksplisit menilai wilayah target, bukan hanya rata-rata seluruh citra, sehingga menyediakan alat ukur yang lebih relevan untuk aplikasi manipulasi robotik dan AR.

Dari sisi rekayasa, kerangka ini bergantung pada kualitas dua model fondasi eksternal; kesalahan SAM3 dalam memahami prompt atau Depth Anything dalam memahami geometri scene berpotensi merambat ke hasil akhir. Secara konseptual, definisi pita batas selebar 10 piksel adalah pilihan desain evaluasi, bukan properti yang melekat pada tugasnya, sehingga hasil kuantitatif metrik batas sensitif terhadap definisi ini. Penulis sendiri mengakui bahwa pelatihan gabungan berskala lebih besar dan integrasi dengan tugas hilir (misalnya keberhasilan genggaman robot nyata) belum dieksplorasi — evaluasi makalah ini berhenti pada kualitas peta kedalaman, bukan hasil tugas manipulasi sesungguhnya.

## Kaitan dengan Bab Lain

FocusDepth dibangun langsung di atas fondasi kedalaman monokular yang dibahas pada bab 175 ([Depth Anything V2](./175%20-%202024%20-%20Depth%20Anything%20V2%20-%20Estimasi%20Kedalaman.md)) dan bab 198 (Depth Anything 3), memakai keduanya sebagai *encoder* geometri tanpa pelatihan ulang penuh. Ia berbeda dari ZoeDepth (bab 176, [ZoeDepth](./176%20-%202023%20-%20ZoeDepth%20-%20Estimasi%20Kedalaman.md)) dan Metric3D (bab 177, [Metric3D](./177%20-%202023%20-%20Metric3D%20-%20Estimasi%20Kedalaman.md)) yang berfokus pada penskalaan metrik seragam, karena FocusDepth tidak menambahkan kemampuan metrik melainkan kemampuan pengondisian wilayah pada kedalaman relatif. Kesenjangan yang dicatat pada survei estimasi kedalaman metrik monokular (bab 199, [Survei Estimasi Kedalaman Metrik Monokular](./199%20-%202025%20-%20Survei%20Estimasi%20Kedalaman%20Metrik%20Monokular%20-%20Estimasi%20Kedalaman.md)) — ketiadaan tolok ukur yang menilai wilayah target secara eksplisit — langsung dijawab oleh FDE-Bench. Bab ini juga melengkapi dua bab sezaman: AsyncMDE (bab 200, [AsyncMDE Kedalaman Monokular Real-Time Memori Spasial](./200%20-%202026%20-%20AsyncMDE%20Kedalaman%20Monokular%20Real-Time%20Memori%20Spasial%20-%20Estimasi%20Kedalaman.md)) yang mengejar kecepatan inferensi, serta UniDAC (bab 201, [UniDAC Kedalaman Metrik Universal untuk Sembarang Kamera](./201%20-%202026%20-%20UniDAC%20Kedalaman%20Metrik%20Universal%20untuk%20Sembarang%20Kamera%20-%20Estimasi%20Kedalaman.md)) yang mengejar generalisasi lintas kamera; ketiganya menyerang dimensi berbeda dari masalah kedalaman monokular praktis tanpa saling tumpang tindih. Untuk klaster manipulasi robotik RGB-D, kemampuan memfokuskan kedalaman pada objek target relevan langsung terhadap perencanaan genggaman yang membutuhkan batas objek presisi.

## Poin untuk Sitasi

Kutip dengan kunci `du2026focusabledepth`. Ringkasan aman untuk dikutip: FocusDepth memperkenalkan tugas *Focusable Depth Estimation*, menggabungkan SAM3 dan Depth Anything melalui modul fusi MSSA untuk menghasilkan kedalaman monokular yang memprioritaskan akurasi latar-depan dan ketajaman batas pada wilayah target sesuai prompt pengguna, dievaluasi pada tolok ukur baru FDE-Bench (252,9 ribu triplet latih, 72,5 ribu triplet validasi dari lima kumpulan data). Karena makalah ini adalah preprint arXiv terbitan Mei 2026 yang belum melalui peer review, seluruh angka kuantitatif berikut wajib diverifikasi ulang terhadap tabel resmi pada naskah sebelum dikutip formal: angka AbsRel 0,073/0,049 (batas), 0,095/0,056 (latar-depan), dan 0,042/0,030 (global) pada pengujian RLBench prompt-kotak; persentase penurunan pada uji ablasi (13,8%; 10%; 2–5,4%; 10,7–12%); serta rincian jumlah kategori (972) dan komposisi lima kumpulan data penyusun FDE-Bench. Status publikasi (apakah diterima di venue tertentu setelah preprint) juga perlu dicek ulang karena tanggal penulisan bab ini mendekati tanggal terbit makalah.
