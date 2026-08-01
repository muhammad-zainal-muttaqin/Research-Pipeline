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
| Matriks multi-seed YOLO26n | **Selesai (E-027).** Depth − RGB rerata **−0,0230**, dua dari tiga seed signifikan NEGATIF. Untuk YOLO26n depth **merugikan**, bukan netral. |
| Protokol evaluasi | **Mengikat (E-025):** `hasil.json` tidak boleh dipakai membandingkan antar lengan; celahnya menskala dengan jumlah deteksi. pycocotools protokol tunggal. |
| Ambiguitas lintas-sisi | Terukur 19,5% tanpa label manusia (E-024/SR-016). Depth tidak menstabilkannya (E-026). B4 belum terwakili. |

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
| Fusi menengah atau akhir E-023 | Ditangguhkan sampai protokol E-022 bersih dan evaluasi konsisten. | [arsip E-022](archive/E022-seed42-awal.md) |

## Lanjutkan sesuai tujuan

| Tujuan | Baca |
|---|---|
| Memahami status semua eksperimen | [README eksperimen](README.md) |
| Memeriksa riwayat bertanggal | [EKSPERIMEN.md](EKSPERIMEN.md) |
| Memeriksa koreksi E-022 | [AUDIT-E022.md](AUDIT-E022.md), lalu [arsip seed-42](archive/E022-seed42-awal.md) |
| Menjalankan ulang E-021 | [catatan teknis](../../reproduce/experiments/CATATAN-TEKNIS-E021.md), [reproduksi](../../reproduce/experiments/REPRODUCE.md), dan [peta skrip](../../reproduce/experiments/PETA-SKRIP.md) |
