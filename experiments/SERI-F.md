# Seri F — Formulasi

> **Berkas baru, seri baru.** Dibuka 6 Agustus 2026. Ini bukan kelanjutan seri E.
> Log kronologis tetap [`EKSPERIMEN.md`](EKSPERIMEN.md) (entri `F-0NN` masuk ke
> sana, append-only). Berkas ini adalah **laporan seri**: alasan keberadaannya,
> peta komponen, keadaan gerbang, dan catatan teknis yang berlaku untuk seluruh
> seri.

## 1. Kenapa seri terpisah

Seri E menjawab pertanyaan **diagnostik dan pembanding**: praproses mana yang
menaikkan keterpisahan (E-011), titik fusi mana yang terbaik (E-032), pada
kapasitas berapa kanal keempat mulai terpakai (E-030), seberapa besar varians
seed dan split (E-027, E-031). Seluruhnya menempatkan komponen yang sudah ada
pada konfigurasi yang berbeda.

Seri F mengubah **formulasi dan arsitekturnya**. Itu satu-satunya arah yang
tersisa menurut pernyataan pengguna 21 Juli 2026: teknik siap-pakai dari
literatur (termasuk SAHI) sudah dicoba sendiri dan tidak satu pun menaikkan mAP;
tuning sudah habis dijalankan dan ditegaskan dua kali. Yang diminta adalah
dekomposisi *first-principles* dan perubahan formulasi — bukan pencarian
hyperparameter lain (CLAUDE.md §"Pernyataan pengguna", §"Diagnosa yang sudah
disepakati").

Penomorannya juga tidak bisa menyambung: `E-033` sudah terpakai dua kali (rentang
metrik depth, 6 Agustus 2026). Seri F berjalan **paralel**, bukan sesudah.

## 2. Asal usul

Sintesis dua laporan *deep research* atas satu brief, keduanya diterima
5 Agustus 2026. Irisan keduanya sekitar tiga per empat: cabang frekuensi tinggi
di samping backbone beku, kepala ordinal kumulatif, loss peringkat berpasangan.

Peringatan mutu sumber yang wajib ikut dibawa:

- Laporan Gemini memuat **tabel hasil yang dikarang** (uji atas 12.500 citra,
  baseline "Co-DETR 0,6038", hasil akhir 0,7245). Yang diambil dari laporan itu
  **hanya rumusan loss**, tidak satu angka pun.
- Kedua laporan **sitasinya belum terverifikasi**. Gemini nol sitasi tersisa;
  Codex memakai token internal yang tidak dapat di-resolve.
- **"MF-RF-DETR" bukan algoritma yang ada** — nama karangan laporan Codex untuk
  usulannya sendiri. Tidak ada makalah, kode, maupun bobot. Jangan pernah ditulis
  seolah metode mapan.

## 3. Tiga komponen

Trunk tetap RF-DETR-L. Stem DINOv2 3-kanal tidak disentuh. Inferensi tetap satu
citra, satu tahap, NMS-free.

| Kode | Komponen | Sasaran | Gerbang | Status gerbang |
|---|---|---|---|---|
| **K1** | Cabang frekuensi tinggi ber-gate init-nol, disuntik sebelum projector | mekanisme (A) geometris, khususnya B4 | **P2** (F-002) | ✅ **LOLOS** |
| **K2** | Kepala ordinal kumulatif CORN, residu terpusat ber-clip ±ε | mekanisme (B) fotometrik, B2↔B3 | **P1** (F-005) | ✅ **LOLOS** |
| **K3** | Konsistensi query lintas-sisi dari graf `_confirmedLinks` | identitas tandan fisik | **P3** (F-003) | ❌ **GUGUR** |

Dua sifat yang wajib dijaga saat implementasi:

1. **γ = 0 saat inisialisasi** membuat K1 identik baseline secara persis. Cabang
   yang tak berguna mulai sebagai *no-op*, bukan sumber derau — ini yang menjawab
   keberatan E-030.
2. **Residu K2 di-clip ke ±ε.** Bila selisih logit > 2ε, urutan pasti terjaga.
   Hanya pasangan berskor rapat yang dapat ditukar. Inilah yang membedakannya
   dari LDL/EMD yang dilarang brief.

## 4. Peta eksperimen dan keadaannya

| Kode | Isi | Status | Hasil ringkas |
|---|---|---|---|
| **F-001** | Prasyarat + probe VRAM A4500 | ✅ selesai | Resep E-021 muat: puncak 10.331/20.470 MiB; 9,2 mnt/epoch; **paralelisme = 1** |
| **F-002** | P2 — frekuensi vs pelepah | ✅ **LOLOS** | dwt_hh +0,0731 pada B4 (ambang +0,02); Laplacian +0,0721 praktis seri |
| **F-003** | P3 — plafon lintas-sisi | ❌ **GUGUR** | 0,2794 < 0,30; 72% galat salah di semua sisi; B4 hanya 0,1038 |
| **F-004** | Baseline RF-DETR-L 3 seed | ✅ selesai | rerata test mAP50 0,5949; **SD seed 0,0049** — 6,5× lebih kecil dari asumsi rencana |
| **F-005** | P1 — massa selisih logit | ✅ **LOLOS** | 0,7113 (ambang 0,30); massa terbesar di **B3**, bukan B2 |
| **F-006** | K2 ordinal CORN | ⏹ **TIDAK DIJALANKAN** | kode siap + uji sambungan LULUS; dihentikan bersama seri |
| **F-007** | K1a cabang frekuensi | ⏹ **DIHENTIKAN** 2/12 run | **γ akhir ≈ 0** (dwt +0,0003, laplacian −6e-5) → mekanismenya tidak pernah aktif |
| ~~F-008~~ | ~~K3 lintas-sisi~~ | ❌ dibatalkan | digugurkan F-003; hemat ~13 jam GPU |
| **F-009** | Gabungan | ⏹ **TIDAK DIJALANKAN** | dihentikan bersama seri |

## 5. Catatan teknis yang berlaku untuk seluruh seri

Sejajar dengan `reproduce/experiments/CATATAN-TEKNIS-E021.md`. Semuanya
terverifikasi, bukan dugaan.

### 5.1 Kriteria klasifikasi RF-DETR adalah IA-BCE

Dibaca langsung dari `rfdetr/models/criterion.py:268-296` dan
`training_config.json` E-021 (`ia_bce_loss: true`):

- Bobot positif `t = σ(z)^α · IoU^(1−α)`, `α = 0,25`, di-`clamp(0,01)`, di-`detach`.
- **Bukan** softmax CE, bukan focal polos, bukan varifocal.
- Skor deteksi = `σ(z)` per kelas **independen**; top-k `num_select=300` atas
  grid **datar Q × C** (`postprocess.py:106`).
- **Tidak ada simpleks softmax.** Residu K2 karena itu = offset logit aditif
  ber-mean nol antar 4 kelas.
- Satu query dapat memancarkan sampai 4 deteksi (satu per kelas).

### 5.2 Kepala mengeluarkan **5** logit, bukan 4 — dan kanal ke-5 mati

Ditemukan saat memvalidasi dump logit, dan hampir menjadi kegagalan senyap.
`pred_logits` berbentuk `(B, 300, 5)` meski `num_classes: 4`. Kanal indeks 4:
logit maksimum **−2,424** dan **nol** skor di atas 0,25 pada seluruh 588 citra
test — kanal mati.

Namun `PostProcess` tetap memancarkannya sebagai label 4, sehingga
`eval_rfdetr_perkelas.py` (`category_id = class_id + 1`) menghasilkan kategori 5
yang tidak ada di GT. pycocotools membuangnya diam-diam, jadi **angka E-021 tidak
terpengaruh** — tetapi kode baru mana pun yang mengasumsikan 4 kanal akan salah
indeks tanpa error.

**Pemetaan yang berlaku, dibuktikan bukan ditebak:** kanal 0→B1, 1→B2, 2→B3,
3→B4, 4→mati. Buktinya di §5.3.

### 5.3 Deteksi dapat direkonstruksi PERSIS dari dump logit

`eval/dump_logits_rfdetr.py` menyimpan logit mentah dan kotak seluruh query.
Dari situ keluaran `PostProcess` direproduksi persis (top-k `sigmoid(z)` atas
grid datar): pada 4 citra uji, **kotak identik (maxdiff 0,0)** dan skor identik
sampai pembulatan float16.

Konsekuensinya satu inferensi melayani F-005 **dan** `eval/bootstrap_pohon.py` —
tidak ada jalur skor kedua yang bisa menyimpang diam-diam.

Uji ujung-ke-ujung: implementasi mandiri di `bootstrap_pohon.py` mereproduksi
evaluator rf-detr sendiri pada checkpoint probe 1-epoch —

| | evaluator rf-detr | implementasi seri F |
|---|---|---|
| test mAP50 | 0,5230 | **0,5223** |
| test mAP50-95 | 0,2354 | **0,2354** |

dan pola per-kelas (B1 0,7217 > B3 0,6079 > B2 0,4256 > B4 0,3339) mengulang
tanda tangan E-021 — itulah yang membuktikan pemetaan kanal §5.2.

### 5.4 Paralelisme run = 1, bukan pilihan tuning

VRAM puncak RF-DETR-L @1280 batch 8 = **10.331 MiB** dari 20.470. Dua run
serentak = 20.662 MiB > kapasitas → OOM. Ini persis jebakan yang dicatat
CLAUDE.md ("3 × 6,6 = 19,7 dari 19,7 GiB"). **Seluruh run seri F berurutan.**
Yang boleh diparalelkan hanya pekerjaan CPU (analisis, bootstrap, penulisan).

**Insiden 6 Agustus 2026, dicatat karena hampir merusak F-004.** Menjalankan
`shell/f007_frekuensi.sh` untuk "sekadar memeriksa prasyarat" langsung
**menyalakan run latihan sungguhan** di atas F-004 yang sedang berjalan. Run itu
dibunuh per **grup proses** (bukan per pid — pelajaran pekerja yatim CLAUDE.md)
sekitar satu menit kemudian; F-004 selamat, tidak ada OOM di lognya, dan
artefak parsialnya dihapus.

Dua penjaga ditambahkan supaya tidak terulang:

1. **`--periksa`** — memvalidasi prasyarat lalu keluar tanpa melatih apa pun.
2. **Penjaga proses** — driver MENOLAK start bila sudah ada `train_rfdetr*`
   berjalan. Anggaran VRAM saja tidak cukup: yang berbahaya adalah run KEDUA,
   bukan ukuran run pertama, dan itu hanya terlihat dari daftar proses.

Keduanya diuji: `--periksa` keluar 0 tanpa melatih; tanpa `--periksa` driver
keluar 1 selama F-004 masih hidup.

**Jangan menyunting berkas driver yang sedang dieksekusi.** bash membaca skrip
secara bertahap, jadi mengubahnya di tengah jalan dapat membuatnya mengeksekusi
potongan yang salah. `shell/f004_baseline.sh` karena itu **tidak** diberi penjaga
yang sama sampai runnya selesai.

### 5.5 Uji sambungan wajib — dan apa yang sudah lulus

Sebelum satu run 3-seed pun diantre, tiap komponen harus membuktikan **dua arah**:
(a) pada inisialisasi keluarannya IDENTIK baseline, dan (b) setelah gate dibuka
paksa keluarannya BERUBAH. Yang gagal senyap adalah (b): cabang yang tidak
tersambung tetap melatih tanpa error dan menghasilkan angka yang tampak wajar.

**K1 (F-007), keempat lengan — LULUS**

| | dwt | laplacian | freq_rendah | fase_diacak |
|---|---|---|---|---|
| (a) selisih saat γ = 0 | **0,0** | **0,0** | **0,0** | **0,0** |
| (b) selisih saat γ = 1 | 1,362 | 0,861 | 0,912 | 1,146 |
| param tambahan | **192.289** | **192.289** | **192.289** | **192.289** |

No-op-nya **eksak, bukan hampiran**. Parameter tambahan **identik di keempat
lengan** — syarat kontrol berparameter sama (§5.6) kini terbukti, bukan
diasumsikan. Tambahannya +0,54% atas 35,6 jt parameter.

**K2 (F-006) — LULUS lima pemeriksaan**

| Pemeriksaan | Hasil |
|---|---|
| (a) α = 0 → identik baseline | selisih **0,0** |
| (b) α = 1 → berubah | 0,3 |
| (c) residu ≤ ε | maks **0,3** = ε persis → penjaga peringkat bekerja |
| (d) kanal mati (indeks 4) tak tersentuh | **0,0** |
| (e) **gradien sampai ke kepala ordinal** | `ordinal.weight` norm 35,51 · `alpha` −3,91 · tembus ke backbone |

Pemeriksaan **(e) yang paling penting**. CORAL milik laporan Gemini dibuang
justru karena di-`stop_gradient` penuh sehingga **tidak dapat** menggerakkan
mAP50. Uji ini membuktikan K2 tidak mengulang cacat itu — bukan mengasumsikannya.

Suku loss juga diuji terpisah: `corn` 0,0001 pada label sempurna vs 0,7765 pada
acak; `pasangan` 0,0 saat kelas terpisah jauh (tidak ada pasangan sulit) vs
0,6685 saat rapat; `brs` 0,0 saat benar vs 0,9501 saat salah. Suku ordinal hanya
aktif di lapisan decoder terakhir, terverifikasi.

Kepala ordinal hanya menambah **772** parameter.

### 5.6 Membungkus `Backbone` MEMBUANG bobot pratlatih — bungkus jangan, turunkan

Kegagalan senyap terbesar seri ini sejauh ini, ditemukan 6 Agustus 2026 setelah
F-007 berjalan 12 menit.

Versi pertama `FrekuensiBackbone` **membungkus** `Backbone` sebagai `self.dasar`.
Itu mengubah nama parameter dari `backbone.0.encoder…` menjadi
`backbone.0.dasar.encoder…`, sehingga `load_pretrain_weights` gagal mencocokkan
**264 parameter** dan **seluruh backbone DINOv2 berangkat dari inisialisasi
acak**. rfdetr hanya mencetak WARNING; latihan tetap berjalan tanpa error.

Yang membuatnya ketahuan hanya perbandingan langsung dengan baseline:

| | baseline F-004 | F-007 versi pembungkus |
|---|---|---|
| param tak termuat | **1** | **264** |
| train/loss awal | 9,28 | **11,56** |
| val mAP50 epoch 0 | 0,4714 | **0,1308** |

Kalau lolos, 22 jam GPU akan menghasilkan perbandingan yang **tidak sah**: lengan
perlakuan berbackbone acak melawan baseline pratlatih. Selisihnya akan didominasi
ada-tidaknya pralatihan, bukan cabang frekuensi — mode gagal yang persis sama
dengan yang sudah dicatat untuk E-023 (`STATUS.md` §"Penghalang").

**Perbaikan: TURUNKAN, jangan bungkus.** `FrekuensiBackbone(Backbone)` membuat
nama parameter warisan tidak berubah, bobot pratlatih termuat penuh, dan
`get_named_param_lr_pairs` bawaan (yang mematok kunci `backbone.0.encoder`)
bekerja apa adanya sehingga peluruhan LR per lapisan tidak perlu ditulis ulang.

Setelah perbaikan: **14** parameter tak termuat, dan keempat belasnya terverifikasi
milik cabang samping — **nol** parameter encoder hilang.

**Dua pelajaran untuk uji sambungan**, keduanya sudah dipasang:

1. **Uji forward saja tidak cukup.** Versi pertama juga mati di
   `configure_optimizers` karena `get_named_param_lr_pairs` tidak ada — uji yang
   hanya menjalankan forward meloloskannya. Kaveat 3
   `train_rfdetr_fusion_late.py` sudah memperingatkan ini.
2. **Perbaikan naif untuk (1) menimbulkan kegagalan senyap kedua.**
   Mendelegasikan `get_named_param_lr_pairs` ke `self.dasar` mengembalikan dict
   **kosong tanpa error**, seluruh DINOv2 jatuh ke `other_params` dengan LR
   datar, dan peluruhan LR per lapisan hilang diam-diam.

Uji sambungan sekarang memeriksa **empat** hal: (a) no-op saat init, (b)
tersambung saat gate dibuka, (c) jalur optimizer hidup dengan **> 1 nilai LR
unik**, dan (d) **jumlah parameter tak termuat dari checkpoint pratlatih** berada
di ambang wajar. Pemeriksaan (c) dan (d) tidak ada pada versi pertama, dan
justru keduanya yang menangkap kedua cacat itu.

### 5.7 Gerbang P1 sensitif terhadap skala logit — jangan salah checkpoint

Pita `2ε = 0,6` dinyatakan dalam satuan **logit**, dan skala logit bergantung pada
kematangan latihan. Model yang belum konvergen punya logit rapat, sehingga
fraksi "di dalam pita" **bias TINGGI** dan gerbang bisa lolos secara palsu.

Terukur saat memvalidasi skripnya pada checkpoint probe F-001 (1 epoch):
fraksi dalam pita **0,7666** dengan median |Δ| hanya **0,3086**. Angka itu akan
"meloloskan" K2 tanpa arti apa pun.

**F-005 hanya sah dijalankan pada checkpoint terbaik-val F-004 yang konvergen.**
Keluarannya selalu mencatat `ckpt` supaya ini dapat diperiksa ulang.

Yang tetap informatif dari validasi itu: pasangan kelas yang tertukar didominasi
**kelas bertetangga** — B3→B4 (243), B2→B3 (199), B3→B2 (198), B4→B3 (126) —
yaitu persis struktur ordinal yang disasar K2. Dari 2.612 kotak GT, hanya 38
tidak tertangkap query mana pun, jadi analisis ini memang mengukur kesalahan
KELAS, bukan kegagalan deteksi.

### 5.8 Rezim pengukuran

- **Bootstrap tingkat POHON**, 10.000 replikat, persentil **dan** BCa.
  `eval_extras.py` me-resample citra dengan 2.000 replikat — unit yang salah,
  karena 4–8 citra satu pohon memuat tandan fisik yang sama (k ≈ 1,89) sehingga
  CI-nya terlalu sempit. Pengganti: `eval/bootstrap_pohon.py` (~1 menit per 200
  replikat, CPU; jalankan berdampingan dengan latihan GPU).
- **Tiga seed berpasangan**, seed dan urutan data sama antara baseline dan
  perlakuan.
- Satu protokol, split test beku (mengikat, E-025).
- **Setiap angka menyebut split** (`SawitMVC-val` / `SawitMVC-test`).
- **Kontrol berparameter sama wajib.** K1 harus mengalahkan cabang
  frekuensi-rendah dan fase-diacak. Tanpa itu, kenaikan signifikan pun tidak
  membuktikan bahwa *frekuensi* penyebabnya — disiplin lengan `derau`/`tukar`
  yang sama seperti E-027/E-032.
- CI yang memuat nol ditulis **TIDAK KONKLUSIF**, bukan dinaikkan jadi INDIKASI.

### 5.9 Ambang +0,05 belum tervalidasi untuk jalur ini

Varians seed 0,0321 (E-027) dan varians split 0,0488 (E-031) diukur pada
**SawitMVC-Depth dengan YOLO26n**, bukan SawitMVC dengan RF-DETR-L. F-004
memberi angka yang sebenarnya. Bila varians jalur RGB jauh lebih kecil, ambang
0,05 terlalu longgar dan harus diturunkan; bila jauh lebih besar, seri ini
kemungkinan tidak dapat diukur dan harus dihentikan.

## 6. Caveat yang tidak boleh dihaluskan

**Ukuran efek yang diprediksi 3–10× lebih besar daripada bukti eksternal mana pun
yang dikutip.** Align-DETR +0,6 AP COCO. ViT-Adapter +1,0 AP. Wave-ViT +1,3 box
AP. Semuanya jauh di bawah ambang +0,05 (= 5 poin). **Prior jujurnya: tiap
komponen memberi +0,01 sampai +0,03, yaitu di bawah lantai derau.** Gerbang
F-002/F-003/F-005 ada supaya kemungkinan itu terdeteksi murah — dan F-003 sudah
membuktikan gerbangnya bekerja.

**Bukti penjaga-peringkat K2 membuktikan keamanan, bukan potensi naik.** Ia
menjamin urutan tidak rusak; ia tidak menjamin ada cukup kerugian AP yang tinggal
di pasangan rapat untuk direbut. Itu yang dijawab F-005.

**Keterpisahan piksel bukan AP.** F-002 menutup satu mode gagal; ia tidak
meramalkan kenaikan mAP.

**Plafon anotasi tetap mengikat.** E-018: plafon **val** mAP50 0,8834 dan
mAP50-95 0,4702, median IoU terbaik 0,7303, hanya 3,76% kotak GT tercapai pada
IoU ≥ 0,90. Kenaikan mAP50 besar dapat berdampingan dengan kemajuan mAP50-95
kecil. **Plafon val tidak boleh diperlakukan sebagai plafon test.**

## 7. Peta skrip seri F

| Skrip | Kode | Keluaran |
|---|---|---|
| `build/build_rfdetr_ds.py` | F-001 | `rfdetr_ds/` (3000/404/588 symlink) |
| `train/train_rfdetr.py` (+`--seed`) | F-001, F-004 | `runs/detect/runs_f004/rfdetrl_rgb_seed*` |
| `analysis/freq_vs_pelepah.py` | F-002 | `results/F-002/freq_vs_pelepah.json` |
| `analysis/cross_side_consistency.py` (+`--dump-tandan`) | F-003 | rekam per-kemunculan |
| `analysis/plafon_lintas_sisi.py` | F-003 | `results/F-003/plafon_lintas_sisi.json` |
| `shell/f004_baseline.sh` | F-004 | driver 3 seed berurutan |
| `eval/dump_logits_rfdetr.py` | F-004 | `results/F-004/logits_test_seed*.npz` |
| `analysis/massa_selisih_logit.py` | F-005 | `results/F-005/massa_selisih_logit.json` |
| `eval/bootstrap_pohon.py` | rezim | CI pohon persentil + BCa |

---

## 8. Penutupan seri — 6 Agustus 2026

Seri F **dihentikan atas permintaan pengguna** pada 2 dari 12 run F-007, sebelum
F-006 dan F-009 dijalankan. Alasannya dinyatakan langsung: hanya hasil positif
yang bernilai, dan tidak ada yang menembus 0,60 pada split test.

### 8.1 Temuan yang berdiri sendiri

| # | Temuan | Angka | Berkas |
|---|---|---|---|
| 1 | **Varians seed jalur RGB RF-DETR akhirnya terukur** | SD test mAP50 **0,0049**, rentang 0,0097 | `results/F-004/` |
| 2 | Frekuensi tinggi memisahkan tandan dari **pelepah**, monoton B1<B2<B3<B4 | dwt_hh **+0,0731** pada B4 | `results/F-002/` |
| 3 | **Laplacian ≈ DWT** di tingkat piksel — mesin DWT tidak membeli apa pun | 0,0721 vs 0,0731 | `results/F-002/` |
| 4 | **72% galat kelas salah di SEMUA sisi**; B4 kasus terburuk | 0,2794 keseluruhan, **B4 0,1038** | `results/F-003/` |
| 5 | 71% galat kelas berada dalam pita 0,6 logit; massanya di **B3**, bukan B2 | 0,7113 / 0,6384 / 0,7147 | `results/F-005/` |
| 6 | **Gate init-nol adalah PERANGKAP, bukan hanya pengaman** | γ akhir +0,0003 / −6e-5 | `results/F-007/` |

Temuan 6 yang paling mahal dipelajari dan paling berguna ke depan: `γ = 0`
memberi *no-op* yang sempurna sekaligus **titik mati** yang sempurna — side
encoder tidak menerima gradien (dikali γ = 0), dan γ sendiri hanya menerima
derau karena proyeksi sampingnya masih acak. Setiap rancangan "cabang samping
ber-gate init-nol" di repo ini menabrak masalah yang sama kecuali gate-nya
diberi warmup, LR terpisah, inisialisasi kecil-taknol, atau tugas pendamping
untuk side encoder.

### 8.2 Yang tidak terjawab

- Apakah cabang frekuensi menolong **bila gate-nya terbuka** — tidak diuji.
- Atribusi frekuensi vs kapasitas — kedua lengan kontrol (`freq_rendah`,
  `fase_diacak`) **tidak pernah dijalankan**.
- K2 sama sekali — kodenya siap dan lulus lima pemeriksaan termasuk bukti
  gradien, tetapi **nol run**.
- Replikasi seed untuk F-007 — hanya seed 42.

### 8.3 Utang teknis yang tercatat

- **Evaluasi pycocotools belum dijalankan untuk seri F.** Seluruh angka mAP di
  sini berasal dari evaluator internal rf-detr, bukan `eval_all_pycoco.py`.
  Aturan mengikat E-025 menuntut satu protokol; ini **belum dipenuhi**.
- Angka 0,6038/0,2770 milik E-021 berasal dari evaluasi EMA-konsisten terpisah
  dan **belum** dihitung ulang untuk F-004. Pembanding like-for-like yang sah
  adalah 0,5837 (jalur `run_test`), dan F-004 memberi 0,5949.
- P3 definitif dengan RF-DETR-L belum dihitung; angka F-003 memakai proksi yolo26n.

### 8.4 Kenapa kontras bootstrap TIDAK dihitung

`eval/bootstrap_pohon.py` sempat dijalankan untuk dwt dan laplacian vs baseline
seed 42, lalu **dibatalkan sebelum selesai** — dan itu keputusan yang benar,
bukan pekerjaan yang tertunda.

Dengan γ akhir +0,0003 dan −6e-5, kontribusi cabang samping efektif nol,
sehingga model perlakuan **adalah** model baseline dengan derau latihan. CI
10.000 replikat atas selisih itu hanya akan mengukur ulang derau seed pada satu
seed — sementara penyebabnya sudah terdiagnosis langsung dari γ, jauh lebih
tajam daripada yang bisa diberikan interval kepercayaan.

Skripnya tetap ada dan tervalidasi (mereproduksi evaluator rf-detr: mAP50-95
0,2354 identik), siap dipakai bila seri ini dilanjutkan dengan gate yang
benar-benar terbuka.

### 8.5 Daftar tugas — selesai dan tidak

| # | Tugas | Status | Catatan |
|---|---|---|---|
| 1 | F-001 prasyarat + probe VRAM | ✅ SELESAI | dataset, bobot pratlatih, resep terkunci |
| 2 | F-002 gerbang K1 (P2) | ✅ SELESAI | LOLOS, +0,0731 B4 |
| 3 | F-003 gerbang K3 (P3) | ✅ SELESAI | GUGUR, 0,2794 < 0,30 |
| 4 | F-004 baseline 3 seed | ✅ SELESAI | SD seed 0,0049 |
| 5 | F-005 gerbang K2 (P1) | ✅ SELESAI | LOLOS 3 seed |
| 6 | Rezim pengukuran (`bootstrap_pohon.py`) | ✅ SELESAI | tervalidasi; adaptor RF-DETR untuk `cross_side_consistency.py` **BELUM** |
| 7 | F-006 K2 ordinal | ⏹ **TIDAK DIJALANKAN** | kode + uji sambungan lulus; **nol run GPU** |
| 8 | F-007 K1a frekuensi | ⏹ **DIHENTIKAN 2/12** | γ ≈ 0 → mekanisme tidak aktif |
| 9 | F-008 K3 lintas-sisi | ⏹ DIBATALKAN | digugurkan gerbang F-003 |
| 10 | F-009 gabungan | ⏹ **TIDAK DIJALANKAN** | syarat tidak terpenuhi |
| 11 | SR-017 + dokumen seri | ✅ SELESAI | `SERI-F.md`, `SR-017`, `PETA-SKRIP.md`, `STATUS.md`, `README.md` |

**Belum dikerjakan dan tercatat sebagai utang** (§8.3): evaluasi pycocotools
untuk seri F, angka EMA-konsisten pembanding 0,6038, P3 definitif dengan
RF-DETR-L, dan adaptor RF-DETR untuk `cross_side_consistency.py`.
