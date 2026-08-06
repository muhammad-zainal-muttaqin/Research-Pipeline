# Seri F — Keadaan dan Sisa Pekerjaan

> **Diperbarui 7 Agustus 2026.**
>
> Berkas ini menggantikan versi sebelumnya yang salah pada dua hal: penomoran
> bentrok dengan E-033/E-033b yang sudah ada, dan ambang pemalsuannya dikalibrasi
> ke lantai derau yang keliru.
>
> Seri F berjalan paralel dengan seri E dan memakai penomoran sendiri. Tidak ada
> pemetaan F ke E.
>
> Rancangan K1 dan K2 berasal dari jawaban deep research atas
> [`BRIEF-DEEP-RESEARCH.md`](BRIEF-DEEP-RESEARCH.md) v1 (5 Agustus). Jalur
> RGB+D (§4) **bukan** dari sumber itu — brief v1 tidak memuat arahan depth,
> sehingga kedua laporan tidak mengusulkan apa pun tentang RGB-D. Brief v2
> sudah diperbaiki tetapi belum dijalankan.
>
> Laporan lengkap: [`SERI-F.md`](SERI-F.md) ·
> [`SR-017`](SR/SR-017-sintesis-deep-research.md).
> Log eksperimen: [`EKSPERIMEN.md`](EKSPERIMEN.md) baris 2353–2646 (F-001…F-005).

---

## 1. Keadaan per 7 Agustus 2026

| ID | Apa yang diuji | Status | Temuan utama |
|---|---|---|---|
| F-001 | Cek prasyarat dan probe VRAM | **Selesai** | Puncak 10.331 dari 20.470 MiB, 9,2 mnt/epoch, hanya bisa 1 run sekaligus |
| F-002 | Gerbang K1: apakah informasi frekuensi tinggi membedakan tandan dari pelepah? | **Lolos** | Sinyal ada — selisih B4 vs kendali: dwt_hh +0,073, laplacian +0,072 (ambang lolos: +0,02) |
| F-003 | Gerbang K3: seberapa besar galat deteksi terjadi karena *lintas-sisi* (tandan dihitung ganda)? | **Dipalsukan (lemah)** | Proporsi 0,279, ambang 0,30, tetapi interval kepercayaan [0,235; 0,324] masih memuat ambang. 72% galat terjadi di semua sisi, bukan hanya lintas-sisi. B4 hanya 0,104 |
| F-004 | Baseline RF-DETR-L tanpa modifikasi, 3 seed | **Selesai** | Test mAP50 rerata **0,5949**, simpangan baku **0,0049**, rentang 0,0097 |
| F-005 | Gerbang K2: apakah ada cukup banyak pasangan tandan yang skornya berdekatan sehingga kepala ordinal bisa merebut? | **Lolos** | Massa 0,711 / 0,638 / 0,715 (ambang lolos: 0,30) — artinya banyak pasangan B2↔B3 yang skor modelnya hampir sama |
| F-006 | Melatih kepala ordinal CORN (K2) | Baru uji sambungan kode | 6 run tersisa, perkiraan 11 jam GPU |
| F-007 | Melatih cabang frekuensi (K1) | **Berjalan, 1 dari 12 run selesai** | Hasil pertama justru negatif — lihat §2.2 |
| F-008 | Eksperimen lintas-sisi (K3) | **Dibatalkan** karena F-003 | Menghemat sekitar 13 jam GPU |
| F-009 | Gabungan komponen yang lolos | Belum mulai | Dilakukan hanya bila minimal 2 komponen berhasil |

Baseline RF-DETR-L per seed pada split test SawitMVC (141 pohon, 588 citra, 2.612 kotak):

| Seed | VAL mAP50 | TEST mAP50 | TEST mAP50-95 |
|---|---|---|---|
| 42 | 0,5708 | **0,5997** | **0,2738** |
| 1337 | 0,5708 | 0,5900 | 0,2700 |
| 2024 | 0,5796 | 0,5951 | 0,2677 |

---

## 2. Dua temuan yang mengubah rencana

### 2.1 Derau antar-seed ternyata jauh lebih kecil dari perkiraan

Simpangan baku antar-seed RF-DETR-L di SawitMVC hanya **0,0049** (rentang 0,0097).
Angka yang selama ini dipakai sebagai acuan — 0,0321 (E-027) dan 0,0488 (E-031) —
berasal dari YOLO26n di SawitMVC-Depth, dataset yang jauh lebih kecil. Angka itu
**terlalu longgar** untuk jalur ini; lantai derau sebenarnya 6,5 kali lebih kecil.

Apa artinya:

1. **Ambang +0,05 tidak berlaku lagi sebagai syarat deteksi.** Angka +0,05 setara
   dengan 10 kali simpangan baku — syarat seketat itu akan membuang efek yang
   sebenarnya nyata. Gantinya: uji bootstrap tingkat pohon secara berpasangan;
   hasilnya sah bila interval kepercayaan tidak memuat nol. Skrip `bootstrap_pohon.py`
   sudah ditulis dan divalidasi, tetapi belum dijalankan untuk satu kontras pun.

2. **Efek kecil dari pustaka kini terdeteksi.** Efek +0,01 setara 2 SD, +0,03
   setara 6 SD — keduanya terukur. Ukuran efek dari pustaka (Align-DETR +0,6 AP,
   ViT-Adapter +1,0 AP, Wave-ViT +1,3 AP) berada dalam jangkauan pengukuran,
   bukan di bawahnya seperti dugaan awal.

3. **Seluruh kondisi pemalsuan di versi lama berkas ini tidak berlaku lagi** dan
   diganti oleh §3.

### 2.2 Run pertama cabang frekuensi (K1) justru negatif

Agent sebelumnya melaporkan dwt seed 42 sebagai 0,5956 terhadap rerata 0,5949 dan
menyimpulkannya netral. Perbandingan yang benar adalah **seed yang sama** (bukan
rerata), dan hasilnya menurun di ketiga metrik:

| | Baseline seed 42 | DWT seed 42 | Selisih |
|---|---|---|---|
| VAL mAP50 | 0,5708 | 0,5667 | **−0,0041** |
| TEST mAP50 | 0,5997 | 0,5956 | **−0,0041** |
| TEST mAP50-95 | 0,2738 | 0,2711 | **−0,0027** |

Penurunan sekitar 0,8 SD, konsisten di tiga metrik. **Ini belum memalsukan K1** —
baru satu seed, dan kedua kontrol (`freq_rendah` serta `fase_diacak`) belum
dijalankan. Tetapi prediksi sebelumnya yang memperkirakan kenaikan +0,06 sampai
+0,10 harus dianggap kemungkinan besar salah.

Catatan penting: **selisih berpasangan tetap sah** meskipun evaluator bukan
pycocotools, karena protokolnya identik di kedua sisi. Yang **tidak sah** adalah
membandingkan langsung 0,5949 dengan 0,6038 (E-021) — penjelasan ada di §5.

Singkatnya: gerbang piksel F-002 lolos, tetapi run pertama datar-sampai-negatif.
Ini persis celah yang diperingatkan brief: sinyal di tingkat piksel belum tentu
bisa dimanfaatkan oleh detektor.

---

## 3. Sisa pekerjaan jalur RGB

### Prioritas: K1 ditunda, K2 dilanjutkan

Dua komponen ini menyasar mekanisme kegagalan yang berbeda. Perbedaan itu
menentukan urutan pengerjaan:

| Komponen | Menyasar masalah apa | Hubungan dengan jalur depth |
|---|---|---|
| **K1** (frekuensi) | Masalah **(A) geometris** — B4 kecil, tertutup pelepah, kamuflase | **Bersaing** dengan depth. Keduanya menargetkan masalah yang sama. Mengerjakan keduanya sekaligus berarti membelanjakan dua kali untuk satu masalah |
| **K2** (ordinal) | Masalah **(B) fotometrik** — kelas B2 dan B3 sulit dibedakan secara warna | **Melengkapi** depth. Depth tidak mungkin memperbaiki ambiguitas kematangan. Hanya K2 yang bisa |

Konsekuensinya:

- **8 run sisa K1 tidak dijadwalkan sampai pra-saring depth (D0) selesai.** K1 dan
  depth berebut masalah yang sama, titik data pertama K1 negatif (§2.2), dan D0
  tidak memerlukan GPU. Menjalankan K1 lebih dulu berarti menghabiskan sekitar 14
  jam GPU pada jalur yang sedang menunjukkan tanda minus, sementara jalur
  alternatif untuk masalah yang sama belum diuji sama sekali.

- **K2 tidak terkena aturan ini.** K2 satu-satunya komponen yang menyasar masalah
  B, gerbangnya lolos telak, dan tidak ada jalur depth yang bisa menggantikannya.

### F-007 — K1, dihentikan di 4 dari 12 run

Dihentikan setelah `fase_diacak` seed 42, bukan di 2/12 (tanpa kontrol, tidak bisa
disimpulkan — kesalahan yang menjatuhkan E-022) dan bukan lanjut ke 12/12 (buang
GPU). Empat lengan pada satu seed memberikan gambaran lengkap karena kedua kontrol
sudah ada, dan dengan SD 0,0049, pembacaan satu seed jauh lebih informatif daripada
perkiraan sebelumnya.

Aturan keputusan setelah 4 run selesai:

| Pola hasil | Artinya | Tindakan |
|---|---|---|
| DWT ≈ freq_rendah ≈ fase_diacak (semua mirip) | Yang bekerja kapasitas tambahan, bukan konten frekuensi | K1 mati, 8 run sisa dibatalkan |
| Keempatnya ≈ baseline (tidak ada yang bergerak) | Cabang samping tidak berdampak | K1 mati |
| DWT/laplacian jelas di atas kedua kontrol | Konten frekuensi yang bekerja | Lanjut 8 run, verifikasi 3 seed |

Kontrol arsitektur sudah bersih: keempat lengan punya parameter identik (192.289),
gate init nol terverifikasi (γ=0 menghasilkan selisih tepat 0,0 terhadap backbone;
γ=1 menghasilkan 0,807–1,089), 14 parameter tak-termuat semuanya milik cabang
samping, nol parameter encoder hilang. Yang diuji memang benar isi kanalnya,
bukan artefak arsitektur.

Catatan: dari F-002, laplacian (0,072) dan DWT-HH (0,073) praktis setara di
tingkat piksel. Bila anggaran GPU menyempit, dua lengan tekstur bisa diringkas
menjadi satu.

### F-006 — K2 (kepala ordinal), 6 run, perkiraan 11 jam

Gerbang F-005 lolos telak (0,71 / 0,64 / 0,71 terhadap ambang 0,30) — artinya
banyak pasangan tandan yang skornya berdekatan dan tersedia untuk direbut oleh
kepala ordinal. Kode dan uji sambungan sudah ada; shell driver belum ditulis. Ini
kandidat dengan rasio informasi-per-jam-GPU terbaik yang tersisa.

Kondisi pemalsuan: interval kepercayaan bootstrap pohon berpasangan pada mAP50
memuat nol; atau B2/B3 tidak naik sementara B1/B4 turun; atau akurasi ±1 naik
tetapi mAP50 eksak justru turun.

### K3 — Ditutup, dengan satu tindak lanjut tanpa GPU

F-003 menggugurkan K3 dan membatalkan F-008. Tetapi pemalsuannya **lemah** (CI
memuat ambang) dan dihitung dari **proksi yolo26n**, bukan RF-DETR-L. Dump logit
F-004 (`logits_test_seed*.npz`) sudah tersedia, sehingga angka definitif untuk
RF-DETR-L bisa dihitung **tanpa GPU**. Ini harus dijalankan sebelum K3 dinyatakan
tertutup di naskah — bila angka RF-DETR-L melewati 0,30, pembatalan F-008 harus
ditinjau ulang.

---

## 4. Jalur RGB+D — Belum Dimulai

**Tidak ada pekerjaan depth di seri F.** RF-DETR-L belum pernah dilatih pada
SawitMVC-Depth; yang pernah hanya RF-DETR nano (E-033).

Yang sudah tersedia: `/workspace/SawitMVC-Depth-YOLO` (dibuat 6 Agustus, oleh
`build/materialize_yolo_split.py`) — tata letak YOLO dari SawitMVC-Depth v1.1.0
berisi train 980, valid 208, test 220 citra, split per pohon 245/52/53, plus
berkas depth (`.raw`, `.json`). Byte-identik dengan rilis kanonik.

### 4.1 Yang gagal adalah cara memasukkan depth, bukan depth-nya sendiri

Kesimpulan penutup E-022: *"Kegagalan ada pada cara memasukkan depth (konkatenasi
di kanal masukan), bukan pada kandungan depth-nya."*

Buktinya sudah terakumulasi dari tiga eksperimen:

| Eksperimen | Yang diuji | Hasil |
|---|---|---|
| E-027 | Depth sebagai kanal ke-4, fusi awal, YOLO26n, 3 seed | Depth justru menurunkan mAP sebesar 0,023 |
| E-029 | Sama seperti di atas, RT-DETR-L, 3 seed | Klaim "depth bermanfaat di kapasitas tinggi" dicabut |
| E-030 | Kanal ke-4 diisi **derau acak** | Kanal masukan ke-4 merugikan di atas 21,9–26,3 juta parameter, apa pun isinya |
| E-032 | Tiga titik fusi (awal/menengah/akhir), YOLO26n | Semua CI memuat nol; fusi menengah positif 3/3 seed (+0,014) tetapi masih **indikasi**, belum diuji pada skala lebih besar |

Tiga eksperimen menghantam satu pintu masuk yang sama (kanal masukan ke-4). Yang
**belum pernah** diuji: fusi menengah di atas model yang lebih besar dari yolo26n,
depth pada RF-DETR-L, dan admisi lewat side encoder dengan gate init nol.

### 4.2 Rancangan: pakai slot side encoder yang sama dengan K1

Cabang samping F-007 sudah terbukti bersih secara arsitektur (lihat §3): 192.289
parameter, gate init nol dengan selisih tepat 0,0, jalur optimizer hidup. **Masukan
side encoder itu berupa slot 3 kanal.** Isinya bisa diganti dari sub-band DWT
menjadi depth + peta validitas, dan seluruh instrumentasi F-007 berlaku apa adanya.
Stem DINOv2 tidak disentuh, sehingga keberatan E-030 tidak berlaku — kerugian di
E-030 berasal dari kanal masukan yang mengganggu stem sejak langkah pertama.

**Gating kualitas wajib.** 29% piksel tidak punya depth valid, dan korpus mencatat
bahwa depth berkualitas buruk justru **merusak** prediksi (D3Net, entri 037)
sementara mekanisme filter-before-fuse meredamnya (SA-Gate, entri 055). Peta
validitas harus masuk sebagai masukan eksplisit, bukan diisi nol diam-diam. Kontrol
derau dan kontrol tukar wajib ada.

### 4.3 Pra-saring tanpa GPU (D0) — semuanya belum dikerjakan

Sebelum melatih model apa pun dengan depth, tiga pertanyaan harus dijawab lebih
dulu. Ketiganya bisa dihitung tanpa GPU:

| Kode | Pertanyaan | Gagal bila | Catatan |
|---|---|---|---|
| **D-P1** | Berapa persen piksel depth yang valid **di dalam kotak tandan**, khususnya B4? | Cakupan B4 jauh di bawah 0,71 (angka agregat seluruh citra) | Yang ada baru angka agregat dari `E-022/depth_meta.json` = 0,7103. Belum pernah dihitung per kelas di dalam kotak GT |
| **D-P2** | Apakah depth sensor bisa membedakan isi tandan dari latar belakangnya? | AUC setara pseudo-depth E-006 (0,602, yang sudah dipalsukan) | Depth sensor belum pernah diuji dengan ukuran ini |
| **D-P3** | Apakah ada lompatan depth di batas tandan, di tempat kontras warna RGB gagal? | Gradien depth di batas kotak GT tidak lebih besar dari gradien di kotak acak | Bisa memakai mesin yang sama dengan F-002, dengan statistik batas menggantikan statistik interior |

Mesin analisis F-002 sudah terbukti bekerja pada pertanyaan berbentuk serupa,
sehingga D-P1 sampai D-P3 adalah adaptasi, bukan pembangunan dari nol.

### 4.4 Urutan bila D0 lolos

1. **Baseline RGB RF-DETR-L di SawitMVC-Depth, 3 seed** — belum pernah ada, dan
   tanpa ini, lengan depth tidak punya pembanding yang sah.
2. **Fusi menengah yolo26l (RGB / mid / derau, 3 seed)** — 26,3 juta parameter
   berada tepat di atas titik balik E-030. Di situlah jalur admisi alternatif harus
   membuktikan diri.
3. **Admisi depth ber-gate pada RF-DETR-L (RGB / depth / derau / tukar, 3 seed)** —
   hanya dilakukan bila butir 2 tidak memalsukan arah.

**Batasan yang tidak bisa dihindari.** Depth hanya tersedia di SawitMVC-Depth (352
pohon, 2.299 kotak, B4 hanya **148 kotak** di seluruh dataset). Jalur ini tidak
bisa menggerakkan angka 0,5949 atau 0,6038 dan harus dilaporkan di tabel terpisah.
Derau antar-seed di dataset ini jauh lebih buruk: lengan RGB berayun **0,0759**
antar seed (E-029) — 15 kali lebih besar dari SD jalur utama.

---

## 5. Blokir evaluasi — selesaikan sebelum run berikutnya

Semua angka seri F berasal dari **evaluator internal rf-detr** (torchmetrics via
Lightning, dari berkas `metrics.csv`), bukan dari pycocotools. Skrip
`eval_all_pycoco.py` belum pernah dijalankan untuk seri F.

| Klaim | Sah atau tidak? |
|---|---|
| Selisih berpasangan antar-lengan di dalam seri F | **Sah** — evaluator sama di kedua sisi |
| Simpangan baku antar-seed 0,0049 | **Sah** — sumber tunggal |
| Membandingkan 0,5949 dengan 0,6038 | **Tidak sah** — evaluator berbeda, harus melewati protokol E-025 dulu |

Masalah tambahan: bobot E-021 **hilang**. Pada jalur evaluasi yang sama
(`run_test/best_total`), E-021 mencatat 0,5837 sementara F-004 menghasilkan
0,5949 — lebih tinggi. Angka **0,6038 dari E-021 berasal dari `eval_all_pycoco.py`
dengan pengaturan EMA yang berbeda dan belum pernah dihitung ulang untuk F-004.**

Artinya: **proyek saat ini tidak punya satu angka acuan pun yang bisa dibandingkan
secara adil antar-seri.** Setiap klaim "menembus plafon" tidak berdasar sampai
evaluasi pycocotools dijalankan.

Biaya: nol GPU. **Prioritas: di atas semua hal lain di berkas ini.**

---

## 6. Catatan yang tetap berlaku

**Plafon anotasi.** E-018 menunjukkan val mAP50 maksimal 0,8834 dan mAP50-95
0,4702. Median IoU terbaik 0,7303; hanya 3,76% kotak GT tercapai pada IoU ≥ 0,90.
Kenaikan mAP50 besar bisa berdampingan dengan kemajuan mAP50-95 yang kecil. Plafon
val bukan plafon test.

**F-005 membuktikan keamanan K2, bukan potensi kenaikan.** Massa yang cukup (0,64–
0,71 terhadap ambang 0,30) berarti ada ruang untuk direbut, tetapi bukan jaminan
bahwa kepala ordinal akan berhasil merebutnya.

**Sitasi dari kedua laporan deep research belum diverifikasi.** Laporan Gemini: nol
sitasi tersisa setelah dicek, dan tabel hasilnya **dikarang** (mengklaim uji 12.500
citra dan baseline "Co-DETR 0,6038" dengan hasil 0,7245 yang tidak ada dasarnya).
Laporan Codex: memakai token internal `citeturn…` yang tidak bisa di-resolve;
rujukan "MVDet, DOI 10.1007/s10044-023-01168-6" patut dicurigai karena nama itu
biasanya merujuk makalah ECCV 2020 (Hou dkk.) yang berbeda. Verifikasi sebelum
satu pun dimasukkan ke naskah.

**MF-RF-DETR bukan algoritma yang ada.** Nama itu dikarang oleh laporan Codex
untuk usulannya sendiri. Tidak ada makalah, kode, maupun bobot publik.

**Brief v2 belum dijalankan.** Arahan G (admisi depth) sudah ditambahkan dan
ditandai wajib; jawaban v1 tidak memuat RGB-D karena memang tidak ditanya.
