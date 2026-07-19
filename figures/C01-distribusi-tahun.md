# C01 — Distribusi Entri per Tahun (2012–2026)

## 1. Tujuan & tempat
Bar chart jumlah karya per tahun publikasi. Dirujuk di `\section{Aplikasi
YOLO Lintas Domain}` (`main.tex`, Gambar~\ref{fig:chart-tahun}). Sumber:
`entri/INDEX.md` (dihitung langsung; total 202).

## 2. Konten faktual (tahun : jumlah — jangan ubah angka)
| Tahun | Jumlah |
|---|---|
| 2012 | 2 |
| 2014 | 3 |
| 2015 | 4 |
| 2016 | 4 |
| 2017 | 12 |
| 2018 | 12 |
| 2019 | 18 |
| 2020 | 30 |
| 2021 | 36 |
| 2022 | 25 |
| 2023 | 23 |
| 2024 | 21 |
| 2025 | 7 |
| 2026 | 5 |

Total = 202. Catatan: 2013 tidak ada entri (batang kosong / dilewati).
Puncak pada 2021 (36) dan 2020 (30); ekor 2025–2026 (jurnal terbaru).

## 3. Rujukan tema
Ikuti `figures/THEME.md`. Batang tinta `#1A1D21`; rentang fokus 2019–2026
diberi aksen `#A03028`; sumbu & kisi hairline `#E6E3DA`.

## 4. Kontrak produksi GPT Image 2
```
Buat bar chart vertikal (lanskap) untuk jurnal IEEE. Tema WAJIB: latar
#FAF9F6; batang/teks #1A1D21; aksen #A03028; kisi hairline #E6E3DA; tanpa
bayangan/gradasi; label sans, angka mono; kontras AA. Sumbu-X tahun
2012..2026 (2013 kosong), sumbu-Y jumlah. Nilai persis: 2012=2, 2014=3,
2015=4, 2016=4, 2017=12, 2018=12, 2019=18, 2020=30, 2021=36, 2022=25,
2023=23, 2024=21, 2025=7, 2026=5. Warnai batang 2019-2026 dengan aksen
#A03028, sisanya tinta. Judul sumbu-Y "Jumlah karya". Angka pasti; jangan
ubah. Hasilkan PNG GPT Image 2 tanpa judul global, subjudul, nomor, atau caption internal.
```

## 5. Data referensi dan alternatif pgfplots
```latex
% \usepackage{pgfplots}\pgfplotsset{compat=1.18}
\begin{tikzpicture}
\begin{axis}[ybar, width=\linewidth, height=5cm, ylabel={Jumlah karya},
  symbolic x coords={2012,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026},
  xtick=data, x tick label style={rotate=45,anchor=east}, ymin=0,
  bar width=6pt]
\addplot coordinates {(2012,2)(2014,3)(2015,4)(2016,4)(2017,12)(2018,12)
  (2019,18)(2020,30)(2021,36)(2022,25)(2023,23)(2024,21)(2025,7)(2026,5)};
\end{axis}
\end{tikzpicture}
```
