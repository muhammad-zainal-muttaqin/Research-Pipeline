# SR-005 — Apakah kedalaman memisahkan tandan dari sekitarnya?

**Ide I-9 (sampel depth terkendala instans)** · **Eksperimen:** E-006
**Putusan: DIPALSUKAN** · 2026-07-21

---

## 1. Masalah

Seluruh tesis "depth sebagai terobosan" bersandar pada satu asumsi yang belum
pernah diuji: bahwa tandan yang bertumpuk atau tertanam berada pada **lapisan
kedalaman yang berbeda** dari sekitarnya, sehingga kedalaman dapat memisahkan
apa yang warna tidak bisa. Naskah merumuskannya di §14: *"When two similarly
coloured regions occupy different spatial layers, depth can help separate them."*

Kalau asumsi itu salah untuk tandan sawit, maka **tidak ada arsitektur fusi
yang akan menolong B4** — early, middle, maupun late. Menguji ini lebih dulu
menghemat berjam-jam GPU dan mencegah kesimpulan yang salah arah.

SR-004 sudah memberi sinyal peringatan: secara visual, area mahkota tampak
menyatu pada peta kedalaman.

## 2. Ide

Jangan menilai dengan mata. Ukur langsung, memakai **kotak kebenaran-dasar** yang
sudah tersedia: untuk tiap kotak tandan, bandingkan statistik kedalaman di
**dalam** kotak terhadap **cincin** di sekelilingnya.

**Kendali sangat penting di sini.** Peta kedalaman mana pun punya struktur —
atas jauh, bawah dekat, tepi pelepah tajam — sehingga **kotak apa pun** akan
menunjukkan "kontras" tertentu. Karena itu prosedur yang sama dijalankan pada
**kotak acak berukuran sama di posisi acak** pada citra yang sama. Yang bermakna
adalah **selisih terhadap kendali**, bukan angka mentahnya.

Metrik:

| Metrik | Arti |
|---|---|
| `contrast` | \|median dalam − median cincin\| ÷ rentang kedalaman citra |
| `cohen_d` | ukuran efek (beda rata-rata ÷ simpangan baku gabungan) |
| `auc` | peluang piksel dalam-kotak lebih dekat daripada piksel cincin; **0,5 = tidak informatif** |

**Yang akan memalsukan:** kotak tandan tidak menunjukkan kontras/AUC yang lebih
besar daripada kotak acak.

## 3. Solusi

`experiments/depth_bunch_signal.py` atas **40 pohon** (780 kotak tandan),
kedalaman dari DA3 multi-view per pohon, dengan **2 kotak kendali per kotak
asli** (1.560 kendali). AUC dihitung lewat statistik-U Mann–Whitney, dan
signifikansi selisih AUC diuji dengan **2.000 permutasi**.

Dijalankan pada dua resolusi pemrosesan untuk memisahkan efek nyata dari
artefak resolusi: `process_res` 504 dan 1008.

## 4. Hasil

### process_res = 504

| | kontras | AUC | \|d\| | n |
|---|---|---|---|---|
| Kotak tandan asli | **0,0089** | 0,6078 | 0,226 | 780 |
| Kotak acak (kendali) | **0,0341** | 0,5998 | 0,378 | 1.560 |
| **Selisih** | **−0,0252 (rasio 0,26×)** | +0,0080 | | |

Uji permutasi selisih AUC: p = 0,0245.

### process_res = 1008 (resolusi digandakan)

| | kontras | AUC | \|d\| | n |
|---|---|---|---|---|
| Kotak tandan asli | 0,0096 | 0,6079 | 0,213 | 780 |
| Kotak acak (kendali) | 0,0364 | 0,5991 | 0,375 | 1.560 |
| **Selisih** | **−0,0268 (rasio 0,26×)** | +0,0088 | | |

Uji permutasi: p = 0,0110. **Rasio identik (0,26×) pada kedua resolusi.**

### Per kelas (process_res = 1008)

| Kelas | kontras | AUC | \|d\| | piksel median | n |
|---|---|---|---|---|---|
| B1 | 0,0107 | 0,6236 | 0,156 | 10.044 | 92 |
| B2 | 0,0092 | 0,6111 | 0,147 | 8.160 | 111 |
| B3 | 0,0090 | 0,6056 | 0,232 | 6.789 | 431 |
| **B4** | 0,0108 | **0,6022** | 0,246 | **4.515** | 146 |

## 5. Putusan — DIPALSUKAN

Tandan **tidak menonjol** dalam kedalaman. Kontrasnya justru **0,26×** kotak
acak — artinya kotak acak lebih sering memotong batas kedalaman nyata (langit,
tanah, tepi pelepah) daripada kotak tandan.

Penjelasan fisiknya konsisten dengan data: tandan tumbuh **tertanam di ketiak
pelepah**, pada jarak yang praktis sama dengan mahkota di sekitarnya. Tidak ada
lapisan kedalaman yang memisahkannya.

AUC 0,608 vs kendali 0,600 memang signifikan secara statistik (p = 0,011)
karena n besar, tetapi **ukuran efeknya dapat diabaikan**: +0,009 AUC, sementara
0,5 berarti tidak informatif sama sekali. Signifikansi statistik di sini bukan
signifikansi praktis, dan menyajikannya sebagai "depth membawa sinyal" akan
menyesatkan.

**Yang paling menentukan:** B4 — kelas yang paling diharapkan tertolong —
justru punya **AUC terendah (0,6022)**.

Penggandaan resolusi tidak mengubah apa pun (rasio tetap 0,26×), sehingga ini
**bukan artefak resolusi** melainkan sifat nyata objeknya.

## 6. Dampak

**Yang dipalsukan:** versi hipotesis "kedalaman sebagai pemisah tandan di
tingkat piksel". Karena itu fusi RGB-D naif — terutama **I-4 (4-kanal early
fusion)** — tidak diharapkan menaikkan AP50 B4 secara berarti. Prediksi ini
sejalan dengan Ophoff dkk. (§174) yang justru memperkirakan early fusion
berkinerja rendah, dan sekarang kita punya alasan mekanistik **spesifik untuk
sawit**, bukan sekadar analogi dari domain lain.

**Yang TIDAK dipalsukan** — penting untuk tidak berlebihan menyimpulkan:

1. **Geometri tingkat-pohon** (SR-003, SR-004) tetap berdiri kokoh: RMSE sudut
   19% relatif, urutan sisi benar 50/50. Nilai DA3 ada di **pose dan struktur
   antar-pandangan**, bukan di kontras kedalaman lokal.
2. Karena itu **I-6/I-7 (penautan dan asosiasi geometris)** justru menjadi jalur
   yang paling menjanjikan: ia memakai apa yang terbukti (pose lintas-pandangan)
   dan tidak bergantung pada apa yang baru saja dipalsukan (kontras lokal).
3. Ingat pembagian masalah: kegagalan **(A) geometris** vs **(B) fotometrik**.
   SR-005 mempersempit klaim (A) dari "depth memisahkan tandan bertumpuk" menjadi
   "depth memberi kerangka geometris antar-pandangan".

**Konsekuensi rencana:** I-4 tetap dijalankan sebagai **pembanding yang
diprediksi gagal** — nilainya justru sebagai kontrol, dan prediksinya sudah
dicatat di sini *sebelum* dijalankan sehingga tidak bisa dirasionalisasi
belakangan.

## 7. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python depth_bunch_signal.py --trees 40                     # res 504
.venv/bin/python depth_bunch_signal.py --trees 40 --process-res 1008  # res 1008
# keluaran: results/e006/report_res504.json, report_res1008.json
```

Lingkungan: GPU NVIDIA L4, `depth-anything/da3-large`, `seed=42`.
