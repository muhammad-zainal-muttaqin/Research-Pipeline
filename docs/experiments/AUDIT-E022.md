# AUDIT-E022 — audit trainer & evaluator E-022 (2026-07-30)

> **Ruang lingkup:** dokumen ini adalah sumber koreksi E-022, bukan tempat
> metrik final. Tabel seed-42 awal ada di
> [arsip E-022](archive/E022-seed42-awal.md); hasil final yang boleh dikutip
> tetap ada di [METRICS.md](METRICS.md).

Audit ini dijalankan **sebelum** matriks run E-022 diperbesar ke multi-seed, dan
itu keputusan yang benar: tiga dari empat temuan nyata, dan dua di antaranya
membatalkan kesimpulan yang sudah dipublikasikan di
[EKSPERIMEN.md](EKSPERIMEN.md) §E-022 dan
[SR-015](SR/SR-015-depth-sensor-4kanal.md).

Setiap temuan diverifikasi ulang secara independen, tidak diterima apa adanya.
Satu temuan yang diajukan sebagai pemblokir justru **diturunkan lewat
pengukuran**, bukan lewat argumen — menghindari rerun penuh yang tidak perlu.

---

## Cacat #3 — kebocoran lengan kontrol "depth pohon LAIN"

**Nyata, material, membatalkan satu kesimpulan.**

Pemasangan donor depth dilakukan atas daftar citra global tanpa memperhatikan
split. Akibatnya **192 dari 980 citra train memakai peta depth milik pohon di
split TEST** — kontrol registrasi yang seharusnya bersih justru melihat data
test selama backprop.

Perbaikan: pemasangan donor dilakukan per split, dengan pergeseran indeks
`max(4, n//2)` sehingga dijamin melompat ke pohon lain, lalu diperiksa
`assert` bahwa nol pasangan memakai pohon sendiri.

Dampak terukur (YOLO26n seed42, test mAP50):

| | lama (bocor) | `_fix` | selisih |
|---|---:|---:|---:|
| depth pohon LAIN | 0,3771 | 0,3301 | **−0,0470** |

Angka 0,3771 adalah dasar klaim "registrasi tidak memberi apa pun" — dan angka
itu tercemar. Setelah bersih, kontrol tukar (0,3301) berada **di bawah** lengan
depth (0,3501) pada seed42, yang arahnya justru pro-registrasi. **Klaim lama
dicabut**; klaim baru belum boleh dibuat karena baru satu seed satu arsitektur.

---

## Cacat #4 — RNG bersama pada lengan derau

**Nyata, tetapi hipotesis dampaknya GUGUR.**

Versi lama membuat satu `np.random.default_rng` bersama di luar hook lalu
memanggilnya di dalam `imread`. Akibatnya kanal ke-4 diacak ulang **setiap epoch
dan setiap pekerja dataloader** — lengan derau diam-diam mendapat augmentasi
kuat, sementara lengan depth mendapat kanal yang tetap. Itu bukan kontrol
setara.

Perbaikan: penyemaian deterministik per berkas,
`zlib.crc32(stem) ^ seed` (bukan `hash()`, yang dirandomisasi
`PYTHONHASHSEED`). Kanal derau kini tetap sepanjang latihan, sepadan dengan
kanal depth.

Hipotesis saat temuan diajukan: augmentasi tak sengaja itu **menaikkan** derau,
sehingga +0,0437 (satu-satunya delta signifikan di seluruh E-022) adalah
artefak. **Hipotesis itu salah.** Setelah diperbaiki, derau **naik**:

| | lama (cacat) | `_fix` | selisih |
|---|---:|---:|---:|
| YOLO26n derau | 0,3523 | 0,3576 | +0,0053 |
| RT-DETR-L derau | 0,3552 | 0,3894 | **+0,0343** |

Jadi temuan "kanal derau mengalahkan kanal depth" **bukan** artefak bug — ia
bertahan dan diperkuat. Konsekuensinya untuk SR-015: klausa putusan "mekanisme
depth terkonfirmasi pada model besar" kehilangan pijakan, karena pembanding
derau-nya kini lebih kuat.

---

## Cacat #1 — nilai padding letterbox pada kanal ke-4

**Nyata, diukur, TIDAK berdampak. Tidak perlu rerun.**

`ultralytics` 8.4.103 `data/augment.py` `LetterBox.apply_image` cabang
multispectral mengisi **seluruh** kanal dengan `padding_value` (114), termasuk
kanal depth — padahal konvensi encoding kita adalah 0 = "tidak ada data".
Citra 1280×800 → 640×640 memberi skala 0,5, jadi 240 dari 640 baris
(**37,5% tinggi citra**) berisi depth palsu bernilai 114.

Temuan ini diajukan sebagai **pemblokir**. Alih-alih menerima atau menolaknya
secara argumentatif, dampaknya **diukur**: checkpoint 4-kanal yang sudah ada
dievaluasi dua kali pada split test — apa adanya, lalu dengan padding kanal
ke-4 dipaksa 0 (hanya bingkai padding, area citra tidak disentuh).

| | mAP50 | mAP50-95 |
|---|---:|---:|
| padding 114 (apa adanya) | 0,3492 | 0,1230 |
| padding kanal-4 = 0 | 0,3494 | 0,1230 |
| **selisih** | **+0,0002** | **+0,00002** |

Cacatnya nyata tetapi tak berdampak pada kesimpulan. Status: **diturunkan dari
pemblokir**, didokumentasikan, tidak diperbaiki di jalur produksi.
Skrip: `analysis/diag_letterbox_pad.py`. Hasil:
`results/E-022/diag_letterbox_pad.json`.

---

## Cacat #2 — seed RF-DETR di-hardcode

Seed di-hardcode 42 di dalam `model.train()` pada `train/train_rfdetr_4ch.py`,
sehingga setiap "seed berbeda" pada matriks multi-seed akan memakai RNG yang
identik. Diperbaiki: `--seed` kini diteruskan. Belum terpakai karena RF-DETR
belum direplikasi multi-seed.

---

## Cacat operasional — `rc=$?` yang selalu 0

Bukan cacat ilmiah, tetapi ia menyembunyikan tiga run gagal dan karena itu
dicatat di sini.

Pola yang dipakai di seluruh skrip driver antrean:

```bash
python train_depth4ch.py ... > "$log" 2>&1
echo "[$(date +%H:%M:%S)] SELESAI $nama rc=$?"     # SALAH
```

Substitusi perintah `$(date)` **dieksekusi lebih dulu** dan me-reset `$?`,
sehingga `$?` yang terbaca adalah status `date` — **selalu 0**. Run yang crash
dilaporkan sukses dan antrean melanjut tanpa peringatan.

Bukti:

```
$ false; echo "[$(date +%T)] rc=$?"   ->  rc=0     (salah)
$ false; rc=$?; echo "rc=$rc"          ->  rc=1     (benar)
```

Perbaikan: tangkap `rc=$?` di baris terpisah **sebelum** substitusi perintah
apa pun, lalu bandingkan juga jumlah baris `results.csv` terhadap jumlah epoch
yang diharapkan — sehingga run yang mati di tengah tidak bisa lolos sebagai
"selesai".

Tiga run yang lolos gara-gara ini: `rtdetr-l_tukar_seed1337_fix` (mati epoch
27/60 tanpa error dan tanpa OOM), `rtdetr-l_derau_seed2024_fix` (crash, log
terpotong 108 byte, tidak ada direktori run), `rtdetr-l_tukar_seed2024_fix`
(belum pernah selesai).

---

## Selisih evaluator — TERLACAK 2026-07-31, lihat [E-025](EKSPERIMEN.md)

> **Status: selesai.** Celahnya **menskala dengan jumlah deteksi**, bukan
> berasal dari pemilihan checkpoint, ambang confidence, `max_det`, `maxDets`,
> maupun perbedaan daftar citra — keempat kandidat di bawah plus satu kandidat
> tambahan sudah diuji dan digugurkan oleh pengukuran. Lengan RGB-D memancarkan
> 2,44× lebih banyak deteksi, dan evaluator internal ultralytics menaikkan
> lengan yang deteksinya jarang (+0,0133) jauh lebih besar daripada yang padat
> (−0,0023); asimetri 0,0156 itu cukup untuk membalik tanda Δ.
>
> **Aturan yang mengikat:** `hasil.json` tidak boleh dipakai membandingkan antar
> lengan — celahnya bukan offset tetap. pycocotools adalah protokol tunggal.
> Rincian, angka, dan batas klaimnya ada di [E-025](EKSPERIMEN.md).

Catatan asli saat temuan diajukan, dipertahankan sebagai rekam:

Ditemukan saat memvalidasi ringkasan multi-seed, **belum terlacak**, dan dicatat
di sini karena ia memengaruhi arah kesimpulan.

`hasil.json` per-run (jalur evaluasi internal trainer) dan
`eval/eval_e022_paired.py` (pycocotools, protokol beku) berselisih sampai
**0,028** — dan selisihnya **tidak simetris antar lengan**:

| seed | RGB pyc − hasil | RGB+D pyc − hasil |
|---|---:|---:|
| 42 | +0,0030 | +0,0009 |
| 1337 | +0,0005 | **+0,0184** |
| 2024 | +0,0083 | **+0,0282** |

`hasil.json` merugikan lengan RGB+D secara sistematis, sehingga rerata Δ YOLO26n
berubah tanda: −0,0060 (hasil.json) versus **+0,0059** (pycocotools). Kandidat
penyebab: pemilihan checkpoint (best vs last), ambang confidence, `max_det`,
atau perbedaan daftar citra. **Tidak ada angka E-022 yang berstatus hasil
final.** Angka pycocotools hanya dipakai untuk menelusuri audit sampai
perbedaan ini terlacak.
