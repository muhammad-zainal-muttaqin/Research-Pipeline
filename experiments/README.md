# Eksperimen: pintu masuk

Folder ini memisahkan hasil yang boleh dikutip dari riwayat, audit, dan
pekerjaan yang belum menjadi klaim ilmiah. Baca halaman ini sebelum membuka
log eksperimen yang panjang.

> **Seri F dibuka dan ditutup 6 Agustus 2026 — [SERI-F.md](SERI-F.md).** Seri
> terpisah untuk perubahan **formulasi dan arsitektur** (K1 cabang frekuensi, K2
> kepala ordinal, K3 lintas-sisi), dengan gerbang penyaring tanpa GPU di depan
> tiap komponen. Hasilnya: F-002 dan F-005 lolos gerbang, F-003 gugur, F-007
> dihentikan (gate γ ≈ 0), F-006 dan F-009 tidak dijalankan. Entri kronologisnya
> di [EKSPERIMEN.md](EKSPERIMEN.md) dengan kode `F-0NN`.

## Posisi sekarang

Tidak ada eksperimen yang berjalan. Seri F ditutup 6 Agustus 2026.

**Final:** E-021 menetapkan RF-DETR-L sebagai hasil deteksi empat kelas terbaik
saat ini pada SawitMVC: test mAP50 **0,6038** dan mAP50-95 **0,2770** dengan
protokol `pycocotools` yang sama untuk seluruh pembanding. Replikasi tiga seed
(F-004): rerata test mAP50 0,5949, SD seed 0,0049.

**Batas E-022:** parser kalibrasi, reproyeksi depth ke RGB, dan pemeriksaan mutu
depth sudah divalidasi pada SawitMVC-Depth. Klaim bahwa kanal depth menaikkan
deteksi belum sah. Rinciannya di [audit](AUDIT-E022.md).

| Topik | Status |
|---|---|
| Hasil deteksi empat kelas | **RF-DETR-L E-021** adalah hasil final saat ini: test mAP50 **0,6038** dan mAP50-95 **0,2770**. |
| Dasar angka E-021 | Keempat model pembanding dinilai dengan satu protokol `pycocotools`; lihat [METRICS.md](METRICS.md). |
| Sasaran berikutnya | mAP50-95 0,30 masih kurang 0,023. |
| Data depth sensor E-022 | Parsing kalibrasi dan reproyeksi depth ke RGB tervalidasi. Klaim bahwa depth menaikkan deteksi belum boleh dibuat. |
| Varians split | **Terukur (E-031).** Lengan RGB berayun **0,0488** antar split — melampaui varians seed (0,0321) dan hampir 5× ambang H-022. **Setiap angka mAP wajib menyebut split.** |
| Matriks multi-seed YOLO26n | **Selesai (E-027).** Depth − RGB rerata **−0,0230**, dua dari tiga seed signifikan NEGATIF. Untuk YOLO26n depth **merugikan**, bukan netral. |
| Protokol evaluasi | **Mengikat (E-025):** `hasil.json` tidak boleh dipakai membandingkan antar lengan; celahnya menskala dengan jumlah deteksi. pycocotools protokol tunggal. |
| Ambiguitas lintas-sisi | Terukur tanpa label manusia: **0,2329 di SawitMVC** (511 tandan, E-028) dan 0,1951 di SawitMVC-Depth (82 tandan, E-024). E-026 **tidak konklusif** pada subset terukur karena denominator identitas RGB dan RGB-D tidak sama (82 vs 75); tidak ada klaim ekuivalensi. |
| Kelas paling ambigu | **B2 (0,434)**, bukan B4 (0,234 ≈ B1 0,235). AP50 rendah B4 adalah kegagalan DETEKSI, bukan kebingungan kelas (E-028). |

| Label | Arti |
|---|---|
| **Final** | Bukti dan metrik dibekukan; boleh dikutip sebagai hasil saat ini. |
| **Arsip** | Rekam eksperimen terdahulu; gunakan hanya sebagai konteks historis, bukan capaian final. |
| **Audit** | Bukti koreksi atau pemeriksaan; jangan mengutip skor lama sebagai hasil final. |
| **Ditangguhkan** | Kode, data, atau arah kerja sudah ada, tetapi belum mendukung klaim performa. |

> **Status audit terbaru (2 Agustus 2026).** Gunakan laporan hasil
> `manuscript/reports/reports.tex` untuk putusan yang dibatasi bukti. Tabel ini adalah indeks
> handoff dan dapat memuat label historis; khususnya E-026 harus dibaca sebagai
> tidak konklusif karena denominator identitas berbeda, dan E-032 sebagai tidak
> konklusif dalam rezim diuji, bukan sebagai ekuivalensi.

## Register E-001 sampai E-032

| Eksperimen | Pertanyaan dan data | Putusan | Status kutip | Detail |
|---|---|---|---|---|
| E-001 | Apakah `class_mismatch` mengukur ambiguitas kematangan pada SawitMVC? | Dipalsukan | Arsip | [SR-001](SR/SR-001-ambiguitas-kematangan.md) |
| E-002 | Apakah master mentah Sawit dapat diinventarisasi? | Inventaris selesai | Arsip | [log](EKSPERIMEN.md) |
| E-003 | Apakah DA3 menjaga geometri video orbit? | Dikonfirmasi untuk pose | Arsip | [SR-003](SR/SR-003-da3-video-orbit.md) |
| E-004 | Apakah DA3 konsisten pada banyak video orbit? | Dikonfirmasi | Arsip | [SR-003](SR/SR-003-da3-video-orbit.md) |
| E-005 | Apakah DA3 dapat mengaitkan empat atau delapan sisi foto? | Dikonfirmasi | Arsip | [SR-004](SR/SR-004-da3-empat-sisi.md) |
| E-006 | Apakah pseudo-depth memisahkan tandan dari latar? | Dipalsukan | Arsip | [SR-005](SR/SR-005-sinyal-depth-tandan.md) |
| E-007 | Apakah penautan geometri lintas sisi membantu? | Dipalsukan | Arsip | [SR-006](SR/SR-006-penautan-geometris.md) |
| E-008 | Nomor tidak digunakan | Tidak ada run | - | [log](EKSPERIMEN.md) |
| E-009 | Apakah ukuran kotak menjelaskan kesulitan B4? | Diagnosis tersedia | Arsip | [SR-007](SR/SR-007-diagnosis-b4.md) |
| E-010 | Apakah B4 gagal karena kepadatan atau kontras? | Kontras dikonfirmasi, kepadatan dipalsukan | Arsip | [SR-007](SR/SR-007-diagnosis-b4.md) |
| E-011 | Praproses apa yang membantu B4? | Tekstur dikonfirmasi, penajam kontras dipalsukan | Arsip | [SR-008](SR/SR-008-kanal-tekstur.md) |
| E-012 | Apakah kelas kematangan bersifat ordinal? | Dikonfirmasi | Arsip | [SR-009](SR/SR-009-ordinalitas-kelas.md) |
| E-013 | Apakah pipeline produksi 4 kanal siap untuk sensor? | Pipeline tersedia, belum ada bobot sensor | Ditangguhkan | [`pipeline/`](../pipeline/) |
| E-014 | Apakah hambatan mAP ada di deteksi atau klasifikasi? | Klasifikasi kematangan menjadi hambatan | Arsip | [SR-010](SR/SR-010-hambatan-klasifikasi.md) |
| E-015 | Apakah piksel master mentah bisa dipetakan ke SawitMVC? | 3.992 dari 3.992 terpetakan | Arsip | [SR-002](SR/SR-002-resolusi-master-mentah.md) |
| E-016 | Apakah plafon kematangan dapat dibuktikan? | Ditarik karena bukti cacat | Audit | [SR-011](SR/SR-011-plafon-kematangan.md) |
| E-017 | Apakah detektor dua tahap lebih baik? | Dipalsukan | Arsip | [SR-012](SR/SR-012-dua-tahap.md) |
| E-018 | Apakah sasaran 0,60/0,30 mungkin secara geometris? | Mungkin secara geometri anotasi | Arsip | [log](EKSPERIMEN.md) |
| E-019 | Apakah resolusi tinggi dan augmentasi aman warna membantu? | Tidak konklusif | Arsip | [log](EKSPERIMEN.md) |
| E-020 | Apakah RT-DETR NMS-free melampaui baseline? | Dikonfirmasi, kemudian dilampaui E-021 | Arsip | [SR-013](SR/SR-013-rtdetr-nms-free.md) |
| E-021 | Apakah RF-DETR-L melampaui RT-DETR pada setelan identik? | Dikonfirmasi | **Final** | [METRICS](METRICS.md) dan [SR-014](SR/SR-014-rfdetr-dinov2.md) |
| E-022 | Apakah depth sensor terregistrasi menaikkan mAP? | Fusi awal tidak didukung; klaim kenaikan belum sah | **Audit** | [audit](AUDIT-E022.md) |
| E-023 | Fusi menengah/akhir dua cabang | **Dijalankan sebagai E-032**; nomor E-023 dipakai untuk direktori bukti | Arsip | [E-032](EKSPERIMEN.md), bukti `experiments/results/E-023/` |
| E-024 | Apakah inkonsistensi prediksi lintas-sisi terukur? | Terukur 19,5% | Arsip | [SR-016](SR/SR-016-konsistensi-lintas-sisi.md) |
| E-025 | Dari mana selisih evaluator E-022 berasal? | Menskala dengan jumlah deteksi | **Audit** | [audit](AUDIT-E022.md) dan [log](EKSPERIMEN.md) |
| E-026 | Apakah depth menstabilkan identitas lintas-sisi? | Tidak konklusif pada subset terukur; denominator RGB/RGB-D berbeda | Audit | [SR-016](SR/SR-016-konsistensi-lintas-sisi.md) |
| E-027 | Apakah kenaikan depth E-022 bertahan multi-seed? | Dipalsukan; depth merugikan pada YOLO26n | Arsip | [log](EKSPERIMEN.md) |
| E-028 | Apakah ukuran lintas-sisi bertahan pada dataset 6x lebih besar? | Dikonfirmasi; B2 kelas paling ambigu | Arsip | [SR-016](SR/SR-016-konsistensi-lintas-sisi.md) |
| E-029 | Apakah klausa "depth terpakai pada kapasitas tinggi" bertahan multi-seed? | Dicabut | **Audit** | [log](EKSPERIMEN.md), [SR-015](SR/SR-015-depth-sensor-4kanal.md) |
| E-030 | Apakah arah efek kanal ke-4 ditentukan kapasitas? | Dikonfirmasi sebagian; klaim dipersempit | Arsip | [log](EKSPERIMEN.md) |
| E-031 | Seberapa besar kesimpulan bergantung pada split? | Varians split nyata; arah Δ justru lebih stabil | Arsip | [log](EKSPERIMEN.md) |
| E-032 | Apakah memindahkan titik fusi (awal/menengah/akhir) menolong? | Tidak konklusif dalam rezim diuji; 12/12 CI memuat nol. `mid` indikasi saja; ekuivalensi belum dibuktikan | Audit | [log](EKSPERIMEN.md), [SR-015 §7b](SR/SR-015-depth-sensor-4kanal.md) |

## Urutan baca menurut kebutuhan

| Pembaca | Urutan |
|---|---|
| Pembaca hasil | Halaman ini, [METRICS.md](METRICS.md), lalu [SR-014](SR/SR-014-rfdetr-dinov2.md). |
| Pemeriksa bukti | Halaman ini, [AUDIT-E022.md](AUDIT-E022.md), lalu [EKSPERIMEN.md](EKSPERIMEN.md). |
| Pelaksana reproduksi | Halaman ini, [peta skrip](code/README.md), lalu [REPRODUCE.md](code/REPRODUCE.md). |

`EKSPERIMEN.md` tetap menjadi catatan kronologis. `SR/` merangkai bukti per ide,
dan `experiments/` menyimpan skrip serta JSON sumber.

## Langkah berikutnya

Butir terbuka dari sesi 1 dan 6 Agustus 2026, diurutkan dari yang paling murah.
Tidak ada yang dijalankan tanpa permintaan.

1. **G7b, monotonisitas kapasitas multi-seed.** Dari 12 run yolo26m/l × 3 modal
   × seed 1337 dan 2024, hanya 3 yang lengkap (`yolo26m_{rgb,rgbd,derau}_seed1337`,
   60 epoch dan `hasil.json`). Empat terputus (`yolo26m_rgb_seed2024` 15 epoch,
   `yolo26l_rgb_seed1337` dan `yolo26l_derau_seed1337` 18 epoch,
   `yolo26l_rgbd_seed1337` 2 epoch); lima belum ada. Tidak ada kontras
   berpasangan yang dihitung, sehingga titik balik kapasitas 21,9–26,3 jt
   parameter di E-030 masih pola satu seed. Periksa `runs/detect/` sebelum
   melatih ulang: 55 `best.pt` ditemukan di sana pada 6 Agustus 2026.
2. **Driver lama belum memakai `code/shell/jadwal.sh`.** Pustaka itu menutup
   peluncuran ganda (`flock` saat mulai), pekerja yatim (bunuh per grup proses),
   dan ambang VRAM (5.500 MiB). Jalankan `bash code/shell/jadwal.sh` untuk empat
   pemeriksaan mandirinya.
3. **Oversubscription CPU pada evaluasi.** `eval/eval_e022_paired.py` memakai
   `min(32, cpu_count // 4)` proses per kontras; delapan kontras serentak berarti
   96 pekerja pada 48 core.
4. **Fusi menengah pada yolo26m/l.** E-032 memberi indikasi pada yolo26n (3/3
   seed positif, rerata +0,0139, semua CI memuat nol), dan E-030 menunjukkan isi
   kanal ke-4 baru penting pada kapasitas besar. Hanya relevan bila jalur depth
   dilanjutkan.
5. **Ide yang belum diuji.** I-17 kalibrasi ambang per strata tidak butuh
   latihan (sekitar 20 menit, pada bobot yang ada). I-13 loss berimbang, I-22
   loss ordinal, dan I-15 neck BiFPN masing-masing butuh 3 seed (4–5 jam). I-19
   depth metrik terblokir karena Metric3D atau ZoeDepth belum ada. Tiga seed
   wajib: rentang antar-seed E-032 (0,0354) lebih besar daripada seluruh selisih
   antar-lengan, dan rentang antar-split E-031 0,0488.
