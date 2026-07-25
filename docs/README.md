# docs/ — Peta Dokumen

Satu pintu masuk ke seluruh dokumen repositori. Folder dipecah menurut **fungsi**,
bukan menurut waktu penulisan.

| Folder | Untuk apa |
|---|---|
| [`eksperimen/`](eksperimen/) | Riset deteksi yang **masih berjalan** — status, log, metrik, laporan solusi |
| [`naskah/`](naskah/) | Tinjauan pustaka & naskah LaTeX yang **sudah selesai ditulis** — panduan, rencana, keputusan revisi |
| [`audit/`](audit/) | Pemeriksaan keterlacakan klaim terhadap 182 sumber terverifikasi |
| [`referensi/`](referensi/) | Bahan dari luar — makalah baseline, laporan riset, masukan dosen |
| [`search/`](search/) | Protokol pencarian sistematis + hasil mentah OpenAlex/Scopus |
| [`extracted/`](extracted/) | Teks lengkap 182 PDF hasil ekstraksi (dipakai audit; di-exclude dari situs) |
| [`archive/`](archive/) | Draf dan figur yang sudah tidak dipakai |

## eksperimen/ — mulai dari sini kalau melanjutkan riset

Urutan baca: **STATUS → EKSPERIMEN → METRICS → SR**.

| Berkas | Isi | Sifat |
|---|---|---|
| [`STATUS.md`](eksperimen/STATUS.md) | Titik berhenti, hasil terbaik saat ini, jalur lanjutan yang siap jalan | **Baca pertama** |
| [`EKSPERIMEN.md`](eksperimen/EKSPERIMEN.md) | Log kronologis E-001…E-021, satu entri = satu hipotesis falsifiable | **Append-only** |
| [`METRICS.md`](eksperimen/METRICS.md) | Tabel metrik definitif semua run: per-kelas B1–B4, val + test | Sumber angka |
| [`LAPORAN-EKSPERIMEN.md`](eksperimen/LAPORAN-EKSPERIMEN.md) | Cuplikan terkurasi yang merangkai satu cerita utuh | **Tayang di situs publik** |
| [`SR/`](eksperimen/SR/) | Satu berkas per ide solusi: masalah → hipotesis → bukti → putusan | SR-001…SR-014 |

Kode, JSON mentah, dan log yang menghasilkan angka-angka itu ada di
[`../experiments/`](../experiments/) — lihat
[`PETA-SKRIP.md`](../experiments/PETA-SKRIP.md) untuk peta skripnya.

## naskah/ — tinjauan pustaka

| Berkas | Isi |
|---|---|
| [`PANDUAN-PENULISAN.md`](naskah/PANDUAN-PENULISAN.md) | Aturan gaya + **kontrak teknis berkas entri**. Wajib dibaca sebelum menulis entri. |
| [`PLAN-TINJAUAN-PUSTAKA.md`](naskah/PLAN-TINJAUAN-PUSTAKA.md) | Rencana penulisan naskah LaTeX (`main.tex`, IEEEtran) |
| [`PLAN-SITUS.md`](naskah/PLAN-SITUS.md) | Rencana teknis `index.html` (Ruang Baca Riset) — dahulu bernama `PLAN.md` |
| [`REFRAME-DECISIONS.md`](naskah/REFRAME-DECISIONS.md) | Keputusan atas revisi dosen 23 Juli 2026. **Append-only.** |
| [`figure-english-labels.md`](naskah/figure-english-labels.md) | Prompt relabel figur F01–F08 ke bahasa Inggris |

## search/ — protokol pencarian sistematis

| Berkas | Isi |
|---|---|
| [`PROTOCOL.md`](search/PROTOCOL.md) | Protokol pencarian: 6 set query, kriteria inklusi/eksklusi, dua register asal-usul |
| [`scopus-queries.md`](search/scopus-queries.md) | Query Scopus final, siap tempel |
| [`openalex-counts.csv`](search/openalex-counts.csv) | Rekap jumlah hasil per query |
| [`CEK-SAYA.md`](search/CEK-SAYA.md) | Daftar periksa sesi otonom 23 Juli 2026 — apa yang wajib diverifikasi sendiri |
| `raw/` | 8 CSV hasil mentah OpenAlex Q1–Q7 + known-item test (29 MB, di-exclude dari situs) |

Skrip pengambilannya: [`tools/openalex_search.py`](../tools/openalex_search.py).

## audit/ — keterlacakan klaim

| Berkas | Isi |
|---|---|
| [`AUDIT-PRA-SUBMISI.md`](audit/AUDIT-PRA-SUBMISI.md) | Checklist mekanis sebelum naskah diajukan |
| [`claim-audit-182.md`](audit/claim-audit-182.md) | Verifikasi klaim naskah terhadap teks 182 PDF |
| [`core-claim-register.md`](audit/core-claim-register.md) | Register klaim numerik inti yang dikutip naskah |
| [`entri-accuracy-check.md`](audit/entri-accuracy-check.md) | Konsistensi rangkuman `entri/*.md` vs teks lengkap |
| [`evidence-matrix-182.md`](audit/evidence-matrix-182.md) · [`.csv`](audit/evidence-matrix-182.csv) | Matriks bukti per sumber (ledger baris-per-baris) |

## referensi/ — bahan dari luar

| Berkas | Isi |
|---|---|
| [`SawitMVC-DiB-2026.pdf`](referensi/SawitMVC-DiB-2026.pdf) | Makalah dataset baseline, Data in Brief 67 (2026) 112990 |
| [`deep-research-report.md`](referensi/deep-research-report.md) | Laporan strategi menembus plafon performa setelah tuning |
| [`revisi-dosen-2026-07-23/`](referensi/revisi-dosen-2026-07-23/) | Transkrip masukan dosen + bedah konvensi CEA |
