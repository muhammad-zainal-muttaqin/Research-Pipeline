# SR-016 — Konsistensi prediksi lintas-sisi: mengukur ambiguitas tanpa label manusia

**Ide:** pengganti `class_mismatch` yang dipalsukan E-001 · **Eksperimen:** E-024, E-026 · **Putusan: DIKONFIRMASI** (ukurannya bekerja) / **E-026 TIDAK KONKLUSIF** (denominator identitas berbeda) · 2026-07-31

---

## 1. Masalah

[SR-001](SR-001-ambiguitas-kematangan.md) mencoba mengukur plafon ambiguitas
kematangan lewat flag `class_mismatch`, dan **dipalsukan**: nol ketidaksepakatan
dari 7.328 bunch multi-sisi. Tafsir yang benar sudah dikunci di `CLAUDE.md` —
flag itu **pemeriksa integritas anotasi yang bersih**, bukan pengukur
ambiguitas, dan angka nolnya tidak mendukung maupun membantah klaim ambiguitas
B2/B3.

Tetapi pertanyaan aslinya tidak ikut mati. Diagnosis SR-007 dan SR-009
menyatakan kegagalan B2/B3 bersifat **fotometrik**, dan seluruh rencana depth
bersandar pada pembelahan itu. Yang hilang adalah **ukurannya**: mAP agregat
tidak bisa memberi tahu apakah detektor bingung pada objek fisik yang sama,
karena mAP menilai per-citra dan tidak tahu bahwa empat kotak di empat sisi
adalah satu tandan.

## 2. Ide

`CLAUDE.md` mencatat penggantinya sejak awal, lengkap dengan alasannya:

> Pakai graf `_confirmedLinks` sebagai **oracle identitas**, lalu ukur
> inkonsistensi **prediksi detektor** pada bunch fisik yang sama antar-sisi.
> Itu mengukur ambiguitas tanpa bergantung label manusia.

Kekuatannya justru pada apa yang **tidak** dibutuhkannya: tidak ada label
kebenaran kematangan yang dipakai, tidak ada asumsi tentang anotator. Kalau
detektor memberi kelas berbeda pada objek fisik yang sama dilihat dari sudut
berbeda, minimal satu di antaranya salah — dan itu terukur langsung.

Catatan asli menandai satu penghalang: **butuh detektor terlatih**. Sejak E-021
dan matriks E-022, penghalang itu hilang.

## 3. Solusi

`analysis/cross_side_consistency.py`. Oracle-nya ternyata **tidak perlu
dihitung**: `json/<tree>.json` sudah menyediakan `bunches[].appearances`, yaitu
hasil transitive closure graf `_confirmedLinks` — satu entri = satu tandan
fisik, dengan kotak piksel per sisi.

Prediksi dibuat lewat jalur evaluator E-022 yang sama supaya praproses dan
komposisi kanal tidak berbeda diam-diam. Kemunculan dicocokkan pada IoU ≥ 0,5,
conf ≥ 0,25.

Dua ukuran dilaporkan, dan yang kedua bukan pelengkap:

| Ukuran | Arti |
|---|---|
| `laju_inkonsisten` | fraksi tandan fisik yang mendapat ≥ 2 kelas berbeda |
| `laju_terlewat` | fraksi kemunculan yang tidak terdeteksi sama sekali |

`laju_terlewat` wajib dilaporkan terpisah karena tanpa itu **"konsisten karena
tidak terdeteksi" akan tersamar sebagai "konsisten"** — detektor yang buta
sempurna akan mencetak inkonsistensi nol.

## 4. Bukti

**E-024, YOLO26n RGB, split test SawitMVC-Depth (72 pohon):**

| | |
|---|---:|
| Tandan fisik | 310 |
| Tampak ≥ 2 sisi | 182 |
| Terukur (≥ 2 sisi terdeteksi) | 82 |
| **Tidak konsisten** | **16/82 = 19,5%** |
| Kemunculan terlewat | 137/376 = 36,4% |

Tabrakan: **B1↔B2 sebanyak 11**, **B2↔B3 sebanyak 6**, B1↔B3 nol.

**E-026, apakah depth menstabilkannya?**

| | RGB | RGB-D |
|---|---:|---:|
| Laju inkonsisten | 0,1951 (16/82) | 0,2000 (15/75) |
| Laju terlewat | 0,3644 | 0,3883 |

**selisih +0,0049 · CI95 [−0,1194; +0,1314] · P(depth membantu) = 0,457**

## 5. Putusan

**Ukurannya DIKONFIRMASI bekerja.** Ia memberi angka bermakna (19,5%) di tempat
`class_mismatch` memberi nol, dan strukturnya sesuai prediksi teori: tabrakan
terkonsentrasi pada **tetangga ordinal** B1↔B2 dan B2↔B3, tidak satu pun
melompati dua tingkat. Itu konsisten dengan ordinalitas kelas yang dikonfirmasi
E-012/SR-009, dan diperoleh tanpa memakai label kematangan sama sekali.

Pemisahannya bersih dan itu inti nilainya: **anotator manusia tidak pernah tidak
sepakat (0/7.328), detektor tidak sepakat pada 19,5% tandan fisik yang sama.**
Ambiguitas berada pada klasifikasi berbasis penampilan, bukan pada label.

**E-026 tidak konklusif pada subset terukur.** Titik estimasi bergerak ke arah
yang salah, CI lebar memuat nol, dan peluang depth membantu 0,457, tetapi
denominator identitas berbeda (82 RGB versus 75 RGB-D) sehingga hasil ini tidak
boleh dibaca sebagai ekuivalensi atau falsifikasi universal.

Hasil negatif itu **konfirmasi teori, bukan kegagalan eksperimen**: SR-007 dan
SR-009 mendiagnosis kegagalan B2/B3 sebagai fotometrik, dan `CLAUDE.md` mencatat
sejak awal bahwa depth tidak akan menolong di sana. Tabrakan yang terukur memang
jatuh persis di pasangan kelas yang kegagalannya fotometrik.

## 6. Keterbatasan yang menentukan arah

- **B4 NOL terwakili di kedua lengan.** Tidak satu pun tandan B4 terdeteksi di
  ≥ 2 sisi. B4 adalah kelas yang kegagalannya **geometris** dan karenanya paling
  mungkin dibantu depth — jadi untuk B4 hipotesis ini **belum diuji, bukan
  dipalsukan**. Ini batas terpenting SR ini.
- **n = 82 dan 75.** CI selebar ±0,12 memang wajar; uji ini tidak berdaya
  mendeteksi efek kecil.
- **Laju terlewat 36,4%** berarti lebih dari sepertiga kemunculan tidak masuk
  pengukuran sama sekali.
- Satu seed, satu arsitektur kecil (2,57 jt param). SR-015 menduga kandungan
  informasi depth baru terpakai pada kapasitas tinggi; ukuran ini belum
  dijalankan di sana.
- Ambang conf 0,25 belum disapu, padahal jumlah tandan terukur bergantung
  padanya.

## 7. Dampak

Dua konsekuensi yang sudah masuk rencana kerja:

1. **Instrumen tambahan untuk G4/G6.** Bila fusi menengah atau akhir benar
   bekerja, laju inkonsisten harus **turun**. Bila mAP naik tetapi laju
   inkonsisten datar, kenaikan itu patut dicurigai sebagai efek kapasitas —
   ukuran ini memberi pemeriksaan silang yang tidak dimiliki mAP.
2. **Diulang di SawitMVC (G8).** Dataset itu punya 18.540 kotak dan 7.328 bunch
   multi-sisi, ~40× daya uji SawitMVC-Depth, dan kemungkinan besar menyelesaikan
   masalah B4-nol. Skema JSON kedua dataset sudah diverifikasi identik, jadi
   ukuran yang sama berlaku langsung.

## 8. Reproduksi

```bash
python analysis/cross_side_consistency.py \
    --bobot runs/detect/runs_e022/yolo26n_rgb_seed42/weights/best.pt --modal rgb \
    --keluaran results/E-024/konsistensi_rgb_seed42.json
```

Ganti `--modal rgbd` dan checkpoint sepadan untuk lengan RGB-D. Untuk SawitMVC,
tambahkan `--data-root /workspace/SawitMVC/data --split-dir results/splits_rgb`.

Hasil: `experiments/results/E-024/konsistensi_{rgb,rgbd}_seed42.json`.
Log kronologis: [EKSPERIMEN.md](../EKSPERIMEN.md) §E-024, §E-026.
