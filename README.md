# Research-Pipeline — Tinjauan Pustaka YOLO / RGB-D + Eksperimen Deteksi Sawit

Repositori ini menampung **dua pekerjaan** yang saling menopang: sebuah tinjauan
pustaka terverifikasi tentang deteksi objek berbasis YOLO dan fusi RGB-D, dan
eksperimen deteksi tandan buah sawit (SawitMVC) yang dijalankan di atas landasan
pustaka itu.

| Jalur | Status | Mulai dari |
|---|---|---|
| **Tinjauan pustaka** | Selesai ditulis | [`evidence-body.tex`](./evidence-body.tex) · [`TEMUAN.md`](./TEMUAN.md) |
| **Eksperimen deteksi** | Aktif | [`docs/eksperimen/STATUS.md`](./docs/eksperimen/STATUS.md) |

Hasil terbaik saat ini: **RF-DETR-L, test mAP50 0,6038 / mAP50-95 0,2770** (E-021)
— melewati sasaran mAP50 0,60. Rinciannya di
[`docs/eksperimen/METRICS.md`](./docs/eksperimen/METRICS.md).

## Angka korpus

| | |
|---|---|
| Entri di ledger ([`references.bib`](./references.bib)) | 202 |
| Entri terverifikasi (ada PDF lokal) = korpus naskah | **182** ([`entri/`](./entri)) |
| Entri ditahan (PDF sumber tak tersedia) | 20 ([`entri-withheld/`](./entri-withheld)) |
| Klaster tema taksonomi naskah | 14 |
| Rentang fokus | 2019–2026 (+ fondasi 2012–2018) |

## Peta repositori

| Folder / berkas | Isi |
|---|---|
| [`docs/`](./docs) | Seluruh dokumen, dipecah per fungsi — **peta lengkapnya di [`docs/README.md`](./docs/README.md)** |
| [`entri/`](./entri) | 182 ringkasan makalah. Indeks: [urut nomor](./entri/INDEX.md) · [per tahun & tema](./entri/INDEX-TAHUN.md) |
| [`entri-withheld/`](./entri-withheld) | 20 entri ditahan; **tidak dipakai naskah** |
| [`experiments/`](./experiments) | Kode, JSON hasil, dan log eksperimen — peta: [`PETA-SKRIP.md`](./experiments/PETA-SKRIP.md) |
| [`pipeline/`](./pipeline) | Deliverable produksi: pipeline YOLO 4 kanal (RGB+depth) untuk kamera Gemini |
| [`figures/`](./figures) | Figur final F01–F08, C01, C02, beserta brief-nya |
| [`tools/`](./tools) | Utilitas pembangun matriks bukti |

### Naskah

| Berkas | Isi |
|---|---|
| [`evidence-body.tex`](./evidence-body.tex) | **Isi naskah aktif.** Semua penyuntingan masuk ke sini. |
| [`main.tex`](./main.tex) · [`main-elsarticle.tex`](./main-elsarticle.tex) | Driver IEEEtran dan Elsevier; keduanya `\input` berkas di atas |
| [`references.bib`](./references.bib) | Basis data sitasi, 202 record |
| [`TEMUAN.md`](./TEMUAN.md) | Sintesis lintas makalah |

Draf lama `tinjauan-pustaka.tex` sudah **tidak dipakai** dan diarsipkan ke
[`docs/archive/`](./docs/archive).

### Situs

[`index.html`](./index.html) adalah Ruang Baca Riset — aplikasi statis mandiri
berisi seluruh korpus. Berkas itu **hasil build, jangan disunting tangan.**

## Perintah

```bash
node build.js --dry      # laporan saja, tidak menulis
node build.js            # rakit ulang index.html
latexmk -pdf main.tex    # kompilasi naskah
```

Jalankan `build.js` setiap kali `entri/*.md`, `TEMUAN.md`, atau
`docs/eksperimen/LAPORAN-EKSPERIMEN.md` berubah, lalu commit `index.html`
bersamaan.

## Konvensi

- **Bahasa:** seluruh isi repo memakai Bahasa Indonesia.
- **Nama berkas entri:** `NNN - YYYY - Judul singkat - Tema.md`. Kontrak yang
  diparse `build.js` — jangan diubah. Aturan lengkap di
  [`docs/naskah/PANDUAN-PENULISAN.md`](./docs/naskah/PANDUAN-PENULISAN.md).
- **Keterlacakan:** setiap klaim numerik harus dapat dilacak ke sumber primer.
  Itu prinsip yang menopang seluruh nilai repo ini.
