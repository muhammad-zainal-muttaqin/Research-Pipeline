# Eksperimen: pintu masuk

Folder ini memisahkan hasil yang boleh dikutip dari riwayat, audit, dan
pekerjaan yang belum menjadi klaim ilmiah. Baca halaman ini sebelum membuka
log eksperimen yang panjang.

> **Seri F dibuka 6 Agustus 2026 — [SERI-F.md](SERI-F.md).** Seri terpisah untuk
> perubahan **formulasi dan arsitektur** (K1 cabang frekuensi, K2 kepala ordinal,
> K3 lintas-sisi), dengan gerbang penyaring tanpa GPU di depan tiap komponen.
> Berjalan paralel dengan seri E, bukan menggantikannya. Entri kronologisnya
> tetap di [EKSPERIMEN.md](EKSPERIMEN.md) dengan kode `F-0NN`.

## Status saat ini

**Final:** E-021 menetapkan RF-DETR-L sebagai hasil deteksi empat kelas terbaik
saat ini pada SawitMVC: test mAP50 **0,6038** dan mAP50-95 **0,2770** dengan
protokol `pycocotools` yang sama untuk seluruh pembanding.

**Batas E-022:** parser kalibrasi, reproyeksi depth ke RGB, dan pemeriksaan mutu
depth sudah divalidasi pada SawitMVC-Depth. Klaim bahwa kanal depth menaikkan
deteksi belum sah. Baca [audit](AUDIT-E022.md) sebelum melihat
[arsip seed-42](archive/E022-seed42-awal.md).

| Label | Arti |
|---|---|
| **Final** | Bukti dan metrik dibekukan; boleh dikutip sebagai hasil saat ini. |
| **Arsip** | Rekam eksperimen terdahulu; gunakan hanya sebagai konteks historis, bukan capaian final. |
| **Audit** | Bukti koreksi atau pemeriksaan; jangan mengutip skor lama sebagai hasil final. |
| **Ditangguhkan** | Kode, data, atau arah kerja sudah ada, tetapi belum mendukung klaim performa. |

> **Status audit terbaru (2 Agustus 2026).** Gunakan `reports.tex` dan
> `REPORT_PLAN.md` untuk putusan yang dibatasi bukti. Tabel ini adalah indeks
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
| E-013 | Apakah pipeline produksi 4 kanal siap untuk sensor? | Pipeline tersedia, belum ada bobot sensor | Ditangguhkan | [`reproduce/pipeline/`](../../reproduce/pipeline/) |
| E-014 | Apakah hambatan mAP ada di deteksi atau klasifikasi? | Klasifikasi kematangan menjadi hambatan | Arsip | [SR-010](SR/SR-010-hambatan-klasifikasi.md) |
| E-015 | Apakah piksel master mentah bisa dipetakan ke SawitMVC? | 3.992 dari 3.992 terpetakan | Arsip | [SR-002](SR/SR-002-resolusi-master-mentah.md) |
| E-016 | Apakah plafon kematangan dapat dibuktikan? | Ditarik karena bukti cacat | Audit | [SR-011](SR/SR-011-plafon-kematangan.md) |
| E-017 | Apakah detektor dua tahap lebih baik? | Dipalsukan | Arsip | [SR-012](SR/SR-012-dua-tahap.md) |
| E-018 | Apakah sasaran 0,60/0,30 mungkin secara geometris? | Mungkin secara geometri anotasi | Arsip | [log](EKSPERIMEN.md) |
| E-019 | Apakah resolusi tinggi dan augmentasi aman warna membantu? | Tidak konklusif | Arsip | [log](EKSPERIMEN.md) |
| E-020 | Apakah RT-DETR NMS-free melampaui baseline? | Dikonfirmasi, kemudian dilampaui E-021 | Arsip | [SR-013](SR/SR-013-rtdetr-nms-free.md) |
| E-021 | Apakah RF-DETR-L melampaui RT-DETR pada setelan identik? | Dikonfirmasi | **Final** | [METRICS](METRICS.md) dan [SR-014](SR/SR-014-rfdetr-dinov2.md) |
| E-022 | Apakah depth sensor terregistrasi menaikkan mAP? | Fusi awal tidak didukung; klaim kenaikan belum sah | **Audit** | [audit](AUDIT-E022.md) dan [arsip](archive/E022-seed42-awal.md) |
| E-023 | Fusi menengah/akhir dua cabang | **Dijalankan sebagai E-032**; nomor E-023 dipakai untuk direktori bukti | Arsip | [E-032](EKSPERIMEN.md), bukti `evidence/experiments/results/E-023/` |
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
| Pemeriksa bukti | Halaman ini, [AUDIT-E022.md](AUDIT-E022.md), [arsip E-022](archive/E022-seed42-awal.md), lalu [EKSPERIMEN.md](EKSPERIMEN.md). |
| Pelaksana reproduksi | Halaman ini, [PETA-SKRIP.md](../../reproduce/experiments/PETA-SKRIP.md), [catatan E-021](../../reproduce/experiments/CATATAN-TEKNIS-E021.md), lalu [REPRODUCE.md](../../reproduce/experiments/REPRODUCE.md). |
| Pihak luar yang diberi tugas riset | [BRIEF-DEEP-RESEARCH.md](BRIEF-DEEP-RESEARCH.md) — paket pengarahan berbahasa Inggris berisi larangan eksplisit atas jalur yang sudah dipalsukan. Bukan hasil dan tidak boleh dikutip sebagai bukti. |
| Perencana eksperimen berikutnya | [SINTESIS-DEEP-RESEARCH.md](SINTESIS-DEEP-RESEARCH.md) — rencana E-033…E-037 hasil sintesis dua jawaban deep research, beserta tiga pra-saring tanpa GPU. **Rencana, bukan hasil**; tidak ada run yang mendukungnya. |

`EKSPERIMEN.md` tetap menjadi catatan kronologis. `SR/` merangkai bukti per ide,
dan `experiments/` menyimpan skrip serta JSON sumber.
