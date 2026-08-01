# Status eksperimen

Dokumen ini adalah handoff singkat. Untuk peta lengkap, mulai dari
[README eksperimen](README.md).

## Fakta aktif

| Topik | Status |
|---|---|
| Hasil deteksi empat kelas | **RF-DETR-L E-021** adalah hasil final saat ini: test mAP50 **0,6038** dan mAP50-95 **0,2770**. |
| Dasar angka E-021 | Keempat model pembanding dinilai dengan satu protokol `pycocotools`; lihat [METRICS.md](METRICS.md). |
| Sasaran berikutnya | mAP50-95 0,30 masih kurang 0,023. |
| Data depth sensor E-022 | Parsing kalibrasi dan reproyeksi depth ke RGB tervalidasi. Klaim bahwa depth menaikkan deteksi belum boleh dibuat. |
| Varians split | **Terukur (E-031).** Lengan RGB berayun **0,0488** antar split — melampaui varians seed (0,0321) dan hampir 5× ambang H-022. **Setiap angka mAP wajib menyebut split.** |
| Matriks multi-seed YOLO26n | **Selesai (E-027).** Depth − RGB rerata **−0,0230**, dua dari tiga seed signifikan NEGATIF. Untuk YOLO26n depth **merugikan**, bukan netral. |
| Protokol evaluasi | **Mengikat (E-025):** `hasil.json` tidak boleh dipakai membandingkan antar lengan; celahnya menskala dengan jumlah deteksi. pycocotools protokol tunggal. |
| Ambiguitas lintas-sisi | Terukur tanpa label manusia: **0,2329 di SawitMVC** (511 tandan, E-028) dan 0,1951 di SawitMVC-Depth (82 tandan, E-024) — tidak dapat dibedakan. Depth tidak menstabilkannya (E-026). |
| Kelas paling ambigu | **B2 (0,434)**, bukan B4 (0,234 ≈ B1 0,235). AP50 rendah B4 adalah kegagalan DETEKSI, bukan kebingungan kelas (E-028). |

## Hasil yang boleh dikutip

Gunakan hanya [METRICS.md](METRICS.md) untuk mengutip performa final E-021.
Sumber angkanya adalah
[`evidence/experiments/results/E-021/perkelas_pycoco.json`](../../evidence/experiments/results/E-021/perkelas_pycoco.json).

## Pekerjaan yang dihentikan atau ditangguhkan

| Jalur | Keputusan | Rujukan |
|---|---|---|
| Pseudo-depth sebagai pemisah tandan | Dipalsukan. Hasil ini tidak menguji sensor depth fisik. | [SR-005](SR/SR-005-sinyal-depth-tandan.md) |
| Detektor dua tahap | Dipalsukan. | [SR-012](SR/SR-012-dua-tahap.md) |
| Klaim plafon kematangan E-016 | Ditarik karena bukti cacat. | [SR-011](SR/SR-011-plafon-kematangan.md) |
| Fusi awal E-022 | Tidak diteruskan sebagai bukti peningkatan deteksi. | [AUDIT-E022.md](AUDIT-E022.md) |
| Fusi menengah atau akhir E-023 | **SELESAI 1 Agustus 2026.** 15 run (5 lengan x 3 seed, 150 epoch, dari nol), 12 kontras berpasangan. Tidak ada lengan yang lolos ambang berbeda; seluruh 12 CI95 memuat nol. `mid` konsisten positif 3/3 seed (rerata +0,0139) tetapi berstatus INDIKASI, bukan temuan. Penjelasan "titik fusi salah" gugur. | [E-032](EKSPERIMEN.md#e-032--titik-fusi-rgb-d-awal-vs-menengah-vs-akhir-semua-dari-nol-2026-08-01--g4-g6) |

## Lanjutkan sesuai tujuan

| Tujuan | Baca |
|---|---|
| Memahami status semua eksperimen | [README eksperimen](README.md) |
| Memeriksa riwayat bertanggal | [EKSPERIMEN.md](EKSPERIMEN.md) |
| Memeriksa koreksi E-022 | [AUDIT-E022.md](AUDIT-E022.md), lalu [arsip seed-42](archive/E022-seed42-awal.md) |
| Menjalankan ulang E-021 | [catatan teknis](../../reproduce/experiments/CATATAN-TEKNIS-E021.md), [reproduksi](../../reproduce/experiments/REPRODUCE.md), dan [peta skrip](../../reproduce/experiments/PETA-SKRIP.md) |


## Rencana E-023 — SUDAH DIJALANKAN, lihat E-032

> Bagian di bawah adalah rancangan sebelum eksekusi, dipertahankan apa adanya
> sebagai rekam keputusan. Hasilnya di [E-032](EKSPERIMEN.md); yang berubah dari
> rancangan: opsi 2 (semua dari nol) dipilih, dan driver per-seed diganti
> penjadwal berbasis anggaran VRAM di tengah jalan karena barrier per-seed
> meninggalkan GPU menganggur belasan menit tiap pergantian seed.

### Rancangan awal

Arsitektur sudah dibangun dan diverifikasi
([`train_fusion_2branch.py`](../../reproduce/experiments/train/train_fusion_2branch.py)):
fusi menengah 2,51 jt param, fusi akhir 3,00 jt param, keduanya terbukti
tersambung (mengubah HANYA kanal kedalaman mengubah keluaran sebesar 6,8 dan
8,6 — sebanding dengan mengubah HANYA RGB). Yang belum dijalankan adalah
eksperimennya.

### Penghalang yang harus diputuskan lebih dulu

YAML dua cabang adalah arsitektur kustom, sehingga **tidak ada bobot COCO
pratlatih yang cocok dengan grafnya**. Seluruh lengan E-022 berangkat dari bobot
pratlatih — bahkan dengan callback khusus (`fourch.make_inflate_callback`) agar
lengan RGB-D tidak kalah karena inisialisasi. Melatih fusi dari nol lalu
membandingkannya dengan lengan E-022 yang pratlatih **bukan perbandingan sah**:
selisihnya akan didominasi ada-tidaknya pralatihan, bukan titik fusi.

| | Opsi 1 — muat sebagian | **Opsi 2 — semua dari nol** |
|---|---|---|
| Cara | Salin bobot pratlatih ke cabang RGB lewat kecocokan nama/bentuk; cabang depth dan lapisan fusi mulai acak | Latih ulang SELURUH lengan tanpa pralatihan, termasuk baseline RGB dan fusi awal |
| Biaya | ~4 run baru | ~15 run |
| Sebanding dengan E-022 | Ya, **bila** pemetaan bobotnya benar | Tidak — matriks terpisah, berdiri sendiri |
| Mode gagal | **Senyap.** Bobot tersalin sebagian, model tetap terlatih, tidak ada error, angkanya terlihat wajar | **Terlihat.** Angka absolut jatuh dan jelas tidak sebanding dengan E-021/E-022 |

**Opsi 2 dipilih**, dan alasannya bukan biaya — opsi 2 justru 3× lebih mahal.
Alasannya jenis risikonya. Sesi 31 Juli–1 Agustus menemukan tiga kegagalan senyap
berturut-turut (`alignedTo: "color"` yang bohong, `--skala` yang diabaikan
ultralytics, precision > 1 dari `evalImgs`); semuanya tidak menimbulkan error dan
hanya ketahuan karena ada yang mustahil secara definisi. Opsi 1 menambah satu
lagi risiko sejenis. Opsi 2 punya kelemahan yang **terlihat**, dan yang diuji
E-023 memang **selisih antar titik fusi**, bukan angka absolut.

### Konfigurasi yang direncanakan

| Parameter | Nilai | Alasan |
|---|---|---|
| Skala | **n** (fusi mid 2,51 jt / late 3,00 jt) | Yang diuji titik fusi, perbandingan internal antar lengan; skala l melipatkan biaya 4× untuk pertanyaan berbeda |
| Epoch | **150**, bukan 60 | 60 epoch cukup untuk model PRATLATIH. Dari nol dengan hanya 980 citra latih, 60 epoch hampir pasti *underfit* — dan hasil rendah akan salah dibaca sebagai "fusi menengah gagal" |
| Seed | **3** (42, 1337, 2024) | E-027/E-029/E-031 semuanya menunjukkan satu seed membalik tanda kesimpulan. Satu seed di sini = mengulang kesalahan yang menjatuhkan E-022 |
| Split | seed42 dulu | Varians split sudah terukur terpisah (E-031); prioritas replikasi = seed dulu, split kemudian |
| Lengan | RGB, fusi awal, fusi menengah, fusi akhir, derau | Kontrol derau WAJIB — SR-015 §6: tanpa itu kenaikan apa pun tidak dapat dibedakan dari efek kapasitas |

**5 lengan × 3 seed = 15 run, ~4,1 jam** pada RTX A4500 (dasar: laju terukur
1 Agustus, skala n 6,5 menit per run-ekuivalen pada 60 epoch, 4 paralel).

### Yang akan memalsukan, ditulis sebelum run pertama

- Fusi menengah/akhir **tidak** mengungguli fusi awal pada rerata 3 seed; atau
- Kenaikannya tidak melampaui kontrol derau pada lengan yang sama; atau
- Selisihnya lebih kecil daripada sebaran antar-seed pada lengan RGB sendiri.

### Instrumen tambahan yang sudah siap

`analysis/cross_side_consistency.py` memberi pemeriksaan silang yang tidak
dimiliki mAP: bila fusi benar bekerja, **laju inkonsisten lintas-sisi harus
turun** dari 0,2329 (baseline SawitMVC, E-028). Bila mAP naik tetapi laju
inkonsisten datar, kenaikan itu patut dicurigai sebagai efek kapasitas.
Penurunan yang terkonsentrasi di B2↔B3 menunjukkan mekanisme fotometrik; di
B3↔B4 menunjukkan geometris.

## Untuk sesi berikutnya — apa yang terbuka setelah 1 Agustus

Seluruh celah G0–G8 tertutup. Yang tersisa, berurut dari yang paling siap:

**1. Penjadwalan run — SUDAH DIPERBAIKI 1 Agustus.** Pustaka
`reproduce/experiments/shell/jadwal.sh` menutup ketiga bug di bawah; jalankan
`bash shell/jadwal.sh` untuk memverifikasi (empat pemeriksaan mandiri, semuanya
lulus saat ditulis). Driver lama BELUM dialihkan memakainya — itu pekerjaan
berikutnya, dan sebaiknya dilakukan sebelum antrean besar berikutnya dijalankan.
Ketiga bug yang ditutup, masing-masing menghabiskan waktu nyata:

- *Peluncuran ganda.* Penjaga "lewati bila berkas hasil sudah ada" tidak
  melindungi apa pun selama pekerjaan berjalan, karena hasil baru ditulis di
  akhir. Driver meluncurkan salinan kedua `awal_seed2024` 20 menit setelah yang
  pertama mulai. Perbaikan: `flock` pada berkas penanda saat MULAI.
- *Pekerja yatim.* Membunuh induk tidak membunuh 12 pekerja
  `ProcessPoolExecutor`-nya; mereka terus berjalan dengan ppid 1. Bunuh per grup
  proses, bukan per pid.
- *Ambang VRAM berbasis peluncuran.* Run tumbuh 2,35 → 4,04 GB; ambang yang
  mengukur pemakaian saat peluncuran menyebabkan dua OOM. Ambang 5500 MiB
  (puncak + margin) terbukti benar sepanjang 15 run.

**2. Oversubscription CPU pada evaluasi.** `eval_e022_paired.py` memakai
`min(32, cpu_count // 4)` = 12 proses. Menjalankan 8 kontras serentak berarti 96
pekerja pada 48 core dan justru MEMPERLAMBAT. Pembagian //4 masuk akal saat
latihan GPU berbagi mesin; setelah latihan selesai ia hanya menyisakan kapasitas.
Yang benar: satu penjadwal yang tahu total core, bukan tiap kontras memutuskan
sendiri.

**3. `mid` pada kapasitas lebih besar.** E-032 menempatkan fusi menengah sebagai
INDIKASI (3/3 seed positif, rerata +0,0139, semua CI memuat nol) pada yolo26n.
E-030 menunjukkan isi kanal ke-4 baru penting pada kapasitas besar. Uji `mid`
pada yolo26m/l adalah satu-satunya arah yang punya dasar dari dua entri sekaligus
— tetapi hanya kalau ada alasan lain untuk melanjutkan jalur depth.

**4. Backlog Blok 3 — sudah dipilah menurut biaya, bukan lagi satu blok.**
Diperiksa 1 Agustus; keempat ide pertama TIDAK dapat diselesaikan sebagai
perubahan kode, masing-masing adalah eksperimen tersendiri.

| Ide | Butuh latihan? | Perkiraan biaya | Catatan |
|---|---|---|---|
| **I-17** kalibrasi ambang per strata | **tidak** | ~20 menit | **Mulai dari sini.** Bekerja pada bobot yang sudah ada; hanya perlu pemilihan ambang pada split val lalu diuji di test. Satu-satunya yang memberi hasil tanpa GPU berjam-jam |
| I-13 loss berimbang / focal | ya, 3 seed x 150 epoch | ~4 jam | Ketimpangan nyata: B3 51,6% vs B1 9,7% |
| I-22 loss ordinal | ya, 3 seed | ~4 jam | Probe dihentikan di E-014; perlu dirancang ulang |
| I-15 neck BiFPN | ya, + arsitektur baru | ~5 jam | Menyasar B4 (objek kecil) |
| I-19 depth metrik | — | terblokir | Butuh Metric3D/ZoeDepth yang belum ada. Hanya relevan bila klaim jarak dilaporkan; DA3 saat ini menghasilkan depth RELATIF (`is_metric` kosong) |

**Tiga seed adalah syarat, bukan kemewahan.** E-032 mengukur rentang antar-seed
0,0354 pada lengan `awal` — lebih besar daripada SELURUH selisih antar-lengan
yang terukur. E-031 mengukur rentang antar-split 0,0488. Menjalankan I-13, I-15,
atau I-22 dengan satu seed akan menghasilkan angka yang tidak dapat ditafsirkan,
dan itu persis kesalahan yang menjatuhkan E-022. Perkiraan biaya di atas sudah
memasukkan 3 seed; memangkasnya berarti membuang seluruh runnya.

Protokol literatur Blok 5 juga masih terbuka.

## Mulai dari nol setelah jeda — apa yang hilang dan urutan membangunnya

Sesi 31 Juli–1 Agustus berjalan di workspace sementara. **8,8 GB state berada di
luar git dan akan hilang** bila workspace direset; yang tersisa hanyalah 770
berkas ter-track. Daftar ini menjawab "apa yang harus dibangun ulang, dalam
urutan apa" supaya tidak ditemukan ulang satu per satu.

| Hilang | Ukuran | Cara mendapatkan kembali |
|---|---:|---|
| `/workspace/SawitMVC/data` | 2,3 GB | HuggingFace `ULM-DS-Lab/SawitMVC` |
| `/workspace/SawitMVC-Depth/data` | 2,6 GB | HuggingFace `ULM-DS-Lab/SawitMVC-Depth` (**private**, butuh token baru) |
| `evidence/experiments/depth_png/` | 211 MB | `build/reproject_depth.py`, ~10 menit |
| `runs/detect/runs_e022/` (**35 checkpoint**) | 2,5 GB | latih ulang; tidak ada jalan pintas |
| `runs/detect/runs_e023/` (**15 checkpoint**) | ~1,1 GB | `shell/e023_fusi.sh` + `shell/e023_seed2024.sh`; ~4 jam pada satu A4500. Kurva latihan, `args.yaml`, dan SHA-256 tiap `best.pt` SUDAH diarsipkan di `evidence/experiments/results/E-023/` — cukup untuk memverifikasi apakah hasil latih-ulang menghasilkan checkpoint yang sama |
| `reproduce/experiments/.venv` | 1,2 GB | `python -m venv --system-site-packages` |

### Urutan, beserta jebakan yang sudah terverifikasi

**1. Dataset — layout wajib `data/`.** Unduhan HuggingFace mendarat dengan
`images/`, `labels/`, `json/` di **akar**, sedangkan seluruh skrip dan split
mengharapkan `<root>/data/…`. Pindahkan. Untuk SawitMVC-Depth, `MERGE_MAP.csv`
dan `MERGE_VERIFICATION.json` juga harus ada **di dalam** `data/`
(`build/make_splits_depth.py` membacanya dari sana) — sambungkan dengan symlink.
Verifikasi integritas sebelum dipakai: 6.336 artefak ber-SHA256 terhadap
`manifests/`.

**2. venv — pin opencv di `requirements.txt` tidak dapat dipasang apa adanya.**
Tertulis `opencv-python-headless==4.11.0`; versi itu tidak ada di PyPI (opencv
memakai versi 4 bagian) dan varian *headless* tidak mengekspor `cv2.imshow` yang
disentuh ultralytics saat impor. Pakai **`opencv-python==4.11.0.86`**. Pasang
juga `numpy==1.26.4` **setelah** ultralytics, karena ultralytics menariknya ke
numpy 2.x. torch diwarisi dari image sistem, jangan dipasang lewat pip.

**3. depth_png — rentang metrik dibekukan.** Jalankan
`build/reproject_depth.py --z-near 0.8 --z-far 15.0`, **bukan** nilai bawaan.
Pemeriksaan bahwa hasilnya benar: cakupan piksel valid rata-rata harus
**0,710** (nilai beku di `depth_meta.json` 0,71032). Jangan memakai
`pipeline/prepare_depth.py` untuk dataset ini.

**4. Split — sudah di git, tetapi path-nya absolut.** `splits_depth/seed{42,1,2}`
dan `splits_rgb/sawitmvc` memuat path absolut ke `/workspace/…`, baik di
`*.txt` maupun di `path:` tiap `data_*.yaml`. Bila repo di-clone ke lokasi lain,
keduanya harus disesuaikan. Path pada `data_*.yaml` **wajib absolut** —
ultralytics me-resolve entri relatif terhadap `DATASETS_DIR`, bukan terhadap
lokasi yaml.

**5. Checkpoint — tidak ada jalan pintas.** 35 bobot tidak diarsipkan (kebijakan
repo). Yang tersedia sebagai gantinya: `metrics_lengkap.json` memuat **SHA-256
dan ukuran byte** tiap `best.pt`. Setelah latih ulang, bandingkan hash-nya —
kalau angkanya berbeda, hash membedakan "checkpoint memang lain" dari "resep
tidak tereproduksi".

**6. Kredensial.** Token HuggingFace dan GitHub yang dipakai sesi ini sudah
seharusnya dicabut; siapkan yang baru.

### Yang TIDAK perlu dibangun ulang

Seluruh hasil sudah terarsip dan aman di git: 21 JSON berpasangan E-022,
`metrics_lengkap.json` (25 run, mAP50/mAP50-95/AP per kelas/P/R/F1/provenans),
hasil E-024/E-026/E-028, split, dan semua entri E-025 sampai E-031. **Membaca
kesimpulan tidak menuntut satu pun run diulang** — yang menuntut latih ulang
hanyalah melanjutkan ke E-023.
