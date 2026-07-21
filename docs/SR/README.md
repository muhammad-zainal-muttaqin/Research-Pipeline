# Solution Report (SR) — Indeks

Satu berkas SR untuk satu **ide solusi**. Tiap SR menjawab rantai yang sama:

```
1. Masalah      apa yang ingin diselesaikan, dan kenapa itu masalah
2. Ide          gagasan solusinya, berikut rujukan korpus yang mendasarinya
3. Solusi       apa yang benar-benar dibangun/dijalankan (skrip, konfigurasi)
4. Hasil        angka apa adanya, termasuk yang tidak menyenangkan
5. Putusan      DIKONFIRMASI / DIPALSUKAN / TIDAK KONKLUSIF, plus alasan
6. Reproduksi   perintah persis untuk mengulang
```

`docs/EKSPERIMEN.md` adalah **log kronologis** semua eksperimen (E-NNN); berkas
SR di sini adalah **pandangan per-ide** yang merangkum satu atau beberapa E-NNN
menjadi satu cerita utuh dari masalah sampai putusan.

Kode ada di `/workspace/experiments/` (di luar repo).

## Daftar

| SR | Ide | Eksperimen | Putusan |
|---|---|---|---|
| [SR-001](SR-001-ambiguitas-kematangan.md) | Ukur plafon ambiguitas B2/B3 dari `class_mismatch` | E-001 | **DIPALSUKAN** |
| [SR-002](SR-002-resolusi-master-mentah.md) | Pakai master mentah 3024×4032 untuk B4 | E-002 | **TIDAK KONKLUSIF** (terblokir) |
| [SR-003](SR-003-da3-video-orbit.md) | DA3 multi-view pada video orbit | E-003, E-004 | **DIKONFIRMASI** |
| [SR-004](SR-004-da3-empat-sisi.md) | DA3 multi-view pada 4/8 sisi foto | E-005 | **DIKONFIRMASI** |
| [SR-005](SR-005-sinyal-depth-tandan.md) | Kedalaman sebagai pemisah tandan (piksel) | E-006 | **DIPALSUKAN** |

## Ide yang belum dikerjakan

| Ide | Isi | Sumber |
|---|---|---|
| I-3 | Bangkitkan pseudo-depth untuk 3.992 gambar | entri 175/198 |
| I-4 | YOLO 4-kanal (early fusion) vs baseline RGB | Expandable YOLO, §174 |
| I-5 | Fusi middle/late dua cabang | Ophoff dkk., §174 |
| I-6 | Penautan bunch lintas-sisi secara geometris | §208 |
| I-7 | Asosiasi sadar-pose berjenjang | §208 |
| I-8 | Gerbang mutu depth + fallback RGB | §174, §265 |
| I-10 | Kaskade deteksi-lalu-proyeksi | §174 |
| I-11 | Analisis terstratifikasi ukuran/oklusi/iluminasi | §234–262 |
