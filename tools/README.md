# Tools

Skrip utilitas yang bukan bagian eksperimen maupun naskah. Dipakai untuk
membangun artefak pendukung seperti matriks bukti, tabel sintesis, dan
dek presentasi.

## Saya ingin...

| Tujuan | Buka ini |
|---|---|
| Membangun matriks bukti | [`build_evidence_matrix.py`](build_evidence_matrix.py) — butuh `pypdf` dan folder `literature/pdf/benar/` |
| Membangun tabel sintesis | [`build_synthesis_table.py`](build_synthesis_table.py) |
| Mencari pustaka lewat OpenAlex | [`openalex_search.py`](openalex_search.py) |
| Membangun register deduplikasi dan screening | [`build_literature_screening_master.py`](build_literature_screening_master.py) |
| Menyelesaikan review konflik deduplikasi | [`resolve_literature_dedup.py`](resolve_literature_dedup.py) |
| Membuat laporan review deduplikasi yang mudah dibaca | [`build_dedup_review_report.py`](build_dedup_review_report.py) |
| Menjalankan triage judul berkepercayaan tinggi | [`build_title_screening.py`](build_title_screening.py) |
| Menjalankan triage abstrak berkepercayaan tinggi | [`build_abstract_screening.py`](build_abstract_screening.py) |
| Mengaudit full text lokal terhadap master pencarian | [`audit_local_fulltext.py`](audit_local_fulltext.py) |
| Membuat dek presentasi PPTX | [`presentation/`](presentation/) — sudah punya README sendiri |

## Isi folder

| Berkas / folder | Isi |
|---|---|
| `build_evidence_matrix.py` | Membangun matriks bukti dari `literature/entries/` dan PDF sumber |
| `build_synthesis_table.py` | Membangun tabel sintesis dari data korpus |
| `openalex_search.py` | Pencarian dan pengunduhan metadata pustaka lewat API OpenAlex |
| `build_literature_screening_master.py` | Deduplikasi raw Scopus/OpenAlex dan pembuatan audit, review manual, master screening, serta rekap PRISMA |
| `resolve_literature_dedup.py` | Resolusi konservatif konflik DOI berbeda dengan bukti judul, tahun, penulis, venue, dan provenance |
| `build_dedup_review_report.py` | Membuat laporan Markdown, HTML, dan CSV ringkas untuk kelompok deduplikasi yang tersisa |
| `build_title_screening.py` | Menandai EC5/EC6 yang jelas dari judul dan meneruskan judul lain ke screening abstrak |
| `build_abstract_screening.py` | Menandai EC1/EC5/EC6 yang sangat jelas dari abstrak dan meneruskan record lain ke pemeriksaan teks penuh |
| `audit_local_fulltext.py` | Mencocokkan PDF terverifikasi lokal dengan master pencarian dan mengekstrak bukti full text untuk kecocokan yang ditemukan |
| `presentation/` | Skrip pembuat dek PPTX: `build_charts.py`, `build_deck.py`, `build_panel.py`, `chart_rgb.py`, `verify_deck.py` |
