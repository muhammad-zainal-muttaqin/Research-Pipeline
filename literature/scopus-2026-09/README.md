# Korpus Scopus September 2026

Bahan tinjauan pustaka `main6` yang ditulis ulang dari awal. Semua literatur
dicari melalui Scopus Search API pada 28 September 2026. Semua angka di naskah
`manuscript/source/main6*.tex` dapat dihitung ulang dari berkas di folder ini
dengan skrip di `tools/scopus/`.

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Melihat string kueri, waktu eksekusi, dan jumlah hasil | [`QUERY.md`](QUERY.md) |
| Membaca protokol penyaringan dan pengodean | [`PROTOKOL.md`](PROTOKOL.md) |
| Melihat keputusan per rekaman | `topik/penyaringan/` |
| Membuka matriks bukti (satu baris per kajian) | `topik/bukti/matriks_bukti.csv` |
| Membaca PDF korpus | `pdf/` (968 berkas, semuanya sudah diperkecil gambarnya dan punya teks di `teks/`; 325 berkas yang ditambahkan 20 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 3 tinjauan terdahulu yang ditambahkan 21 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 4 kajian sawit yang ditambahkan 23 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 95 berkas berikutnya yang ditambahkan 23 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 11 berkas berikutnya yang ditambahkan 23 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 2 berkas berikutnya yang ditambahkan 23 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 5 berkas berikutnya yang ditambahkan 23 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 1 berkas berikutnya yang ditambahkan 23 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 2 berkas berikutnya yang ditambahkan 23 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 1 berkas berikutnya yang ditambahkan 23 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 2 berkas berikutnya yang ditambahkan 23 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 2 berkas yang ditambahkan 24 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 8 berkas berikutnya yang ditambahkan 24 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 12 berkas yang ditambahkan 27 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau; 7 berkas berikutnya yang ditambahkan 27 November 2026 sudah dinilai dari teks lengkap dan disetujui peninjau); daftar menurut kode di [`KATALOG-PDF.md`](KATALOG-PDF.md) |
| Mengetahui PDF yang belum ada | `unduhan/pdf_belum_ada.csv` (55 laporan per 27 November 2026, semuanya dari Scopus, dengan alasan gagal unduh dan status permintaan PDF ke penulis per 26 November 2026); untuk kajian inti lihat `verifikasi/cek-4-teks-lengkap/teks_lengkap.csv` (kolom `pdf_ada`) |
| Melihat kajian metodologi tinjauan pustaka | `metodologi/`; pola tinjauan yang disarikan darinya di `AGENTS.md` §13 |

## Isi folder

| Lokasi | Isi |
|---|---|
| `QUERY.md` | String kueri verbatim MA1–MA7 (metodologi) dan Q1–Q9 (topik) |
| `PROTOKOL.md` | Kriteria inklusi dan eksklusi, kode, alur, keterbatasan |
| `metodologi/` | Kueri MA1–MA7, 60 artikel terpilih, PDF dan teks 25 artikel |
| `topik/queries.json`, `topik/counts.csv`, `topik/raw/` | Kueri Q1–Q9, jumlah hasil, respons mentah API |
| `topik/records_*.csv` | Rekaman per kueri dan gabungan unik (`records_all.csv`, 5.889 rekaman) |
| `topik/enrich.jsonl` | Abstrak dan tautan akses terbuka dari OpenAlex, Semantic Scholar, Crossref, Europe PMC |
| `topik/penyaringan/` | Keputusan tahap judul (`tahap_judul.csv`) dan tahap kelayakan (`abstrak_*.txt`) |
| `topik/bukti/` | Kode manual C1 (`mekanisme_C1.txt`), kode manual C3 (`kode_C3.txt`), hasil yang dilaporkan kajian untuk gambar F12 beserta kutipan sumbernya (`nilai_terlapor.csv`), galat per kelas kematangan (`galat_kelas.tsv`), perbandingan dasar tingkat kepastian temuan (`kepastian_klaim.tsv`), matriks bukti |
| `crossref.jsonl` | Metadata Crossref untuk daftar pustaka `references6.bib` |
| `pdf/`, `teks/` | PDF akses terbuka kajian yang lolos dan teks hasil ekstraksinya |
| `entri/` | 924 ringkasan per kajian `main6`, satu berkas per kunci BibTeX; isi ringkasan dibaca Ruang Baca, teks lengkapnya di `teks/` |
| `unduhan/` | Log unduhan per rekaman dan daftar PDF yang belum diperoleh |

## Menjalankan ulang

```bash
export ELSEVIER_API_KEY_FILE=/path/ke/kunci.txt   # kunci tidak disimpan di repo
python3 tools/scopus/scopus_search.py --queries literature/scopus-2026-09/topik/queries.json --out literature/scopus-2026-09/topik
python3 tools/scopus/enrich_records.py --records literature/scopus-2026-09/topik/records_all.csv --cache literature/scopus-2026-09/topik/enrich.jsonl
python3 tools/scopus/kode_bukti.py          # matriks bukti dari keputusan dan kode manual
python3 tools/scopus/gambar_tinjauan.py     # gambar F01–F13 di manuscript/figures/main6
python3 tools/scopus/tabel_lampiran.py      # tabel lampiran C1 dan daftar kajian bahan tambahan (CSV)
python3 tools/scopus/buat_bib.py --rekaman literature/scopus-2026-09/topik/records_all.csv \
  literature/scopus-2026-09/topik/tambahan_metode_lain.csv \
  literature/scopus-2026-09/metodologi/records_MA*.csv \
  --kunci literature/scopus-2026-09/topik/bukti/matriks_bukti.csv literature/scopus-2026-09/metodologi/terpilih.csv \
  --cache literature/scopus-2026-09/crossref.jsonl --cache-openalex literature/scopus-2026-09/openalex.jsonl \
  --penulis-pdf literature/scopus-2026-09/penulis_pdf.tsv \
  --keluar manuscript/source/references6.bib
```

Jumlah hasil Scopus dapat bertambah bila kueri dijalankan ulang karena terbitan
baru terus diindeks, terutama untuk tahun 2025–2026.
