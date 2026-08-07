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
| Membuat dek presentasi PPTX | [`presentation/`](presentation/) — sudah punya README sendiri |

## Isi folder

| Berkas / folder | Isi |
|---|---|
| `build_evidence_matrix.py` | Membangun matriks bukti dari `literature/entries/` dan PDF sumber |
| `build_synthesis_table.py` | Membangun tabel sintesis dari data korpus |
| `openalex_search.py` | Pencarian dan pengunduhan metadata pustaka lewat API OpenAlex |
| `presentation/` | Skrip pembuat dek PPTX: `build_charts.py`, `build_deck.py`, `build_panel.py`, `chart_rgb.py`, `verify_deck.py` |
