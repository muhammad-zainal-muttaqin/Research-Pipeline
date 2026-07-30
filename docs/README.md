# Dokumen pembaca

Folder ini adalah pintu masuk untuk pembaca. Bukti mentah dan kode berada di
luar `docs/`, sehingga urutan baca tidak tertutup oleh log, JSON, atau output
build.

| Saya ingin | Mulai dari |
|---|---|
| Mengetahui hasil riset yang sah | [Eksperimen](experiments/README.md), lalu [metrik final](experiments/METRICS.md) |
| Memeriksa E-022 | [Audit E-022](experiments/AUDIT-E022.md) |
| Membaca tinjauan pustaka | [Sintesis](literature/synthesis.md) dan [korpus](literature/entries/) |
| Memakai protokol pencarian | [Dokumen pencarian](literature/search/) |
| Menyunting atau membangun naskah | [Panduan](manuscript/guides/) dan [sumber LaTeX](manuscript/source/) |
| Memeriksa keterlacakan klaim | [Audit](audit/) |

## Batas antarbagian

- `docs/experiments/` menjelaskan status, metrik, audit, riwayat, dan keputusan eksperimen.
- `docs/literature/` berisi sintesis, ringkasan 182 sumber, entri yang ditahan, dan protokol pencarian.
- `docs/manuscript/` memisahkan panduan penulisan dari sumber naskah dan figur final.
- `docs/audit/` memuat pemeriksaan klaim dan matriks bukti.

Untuk data sumber, PDF, hasil JSON, log, split, dan dataset, buka
[`../evidence/`](../evidence/). Untuk skrip reproduksi, buka
[`../reproduce/`](../reproduce/). Keduanya dipisahkan agar dokumen pembaca
tetap ringkas, tetapi tautan dari dokumen terkait tetap mengarah ke bukti dan
kode yang tepat.
