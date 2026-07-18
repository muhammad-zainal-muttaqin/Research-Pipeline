# C02 — Distribusi Entri per Tema

## 1. Tujuan & tempat
Bar chart horizontal jumlah karya per tema (dari segmen tema pada nama berkas
`entri/`). Dirujuk di `\section{Aplikasi YOLO Lintas Domain}` (`main.tex`,
Gambar~\ref{fig:chart-tema}). Sumber: `entri/INDEX.md` (dihitung langsung;
total 202; 17 tema).

## 2. Konten faktual (tema : jumlah — urut menurun, jangan ubah angka)
| Tema | Jumlah |
|---|---|
| Fondasi RGB | 39 |
| RGB-D SOD | 22 |
| Estimasi Kedalaman | 21 |
| Deteksi 3D | 17 |
| Segmentasi RGB-D | 16 |
| Pose 6D | 10 |
| Survei YOLO | 9 |
| Grasp Robotik | 9 |
| YOLO+RGB-D | 8 |
| Pertanian | 8 |
| Pedestrian RGB-T | 8 |
| Fusi Multimodal | 8 |
| RGB-D SLAM | 7 |
| Dataset | 6 |
| Remote Sensing | 5 |
| Medis | 5 |
| Industri | 4 |

Total = 202. Catatan: `YOLO+RGB-D` adalah label tampilan untuk tema berkas
`YOLO plus RGB-D`. Pengelompokan tema berbasis nama berkas berbeda sedikit dari
14 klaster `TEMUAN.md` (yang menggabungkan beberapa tema); keduanya konsisten
pada total 202.

## 3. Rujukan tema
Ikuti `figures/THEME.md`. Batang tinta `#1A1D21`; tema inti **YOLO+RGB-D**
dan **Pertanian** diberi aksen `#A03028`; sumbu hairline `#E6E3DA`.

## 4. Prompt siap-tempel Gemini
```
Buat bar chart HORIZONTAL (lanskap), batang terurut dari terbanyak ke
tersedikit, untuk jurnal IEEE. Tema WAJIB: latar #FAF9F6; batang/teks
#1A1D21; aksen #A03028; kisi hairline #E6E3DA; tanpa bayangan/gradasi; label
sans, angka mono; kontras AA. Nilai persis (tema=jumlah): Fondasi RGB=39,
RGB-D SOD=22, Estimasi Kedalaman=21, Deteksi 3D=17, Segmentasi RGB-D=16,
Pose 6D=10, Survei YOLO=9, Grasp Robotik=9, YOLO+RGB-D=8, Pertanian=8,
Pedestrian RGB-T=8, Fusi Multimodal=8, RGB-D SLAM=7, Dataset=6, Remote
Sensing=5, Medis=5, Industri=4. Beri aksen #A03028 pada batang "YOLO +
RGB-D" dan "Pertanian", sisanya tinta. Angka pasti; jangan ubah. Ekspor
SVG/PDF vektor.
```

## 5. Sumber (fallback pgfplots — reproducible tanpa Gemini)
```latex
% \usepackage{pgfplots}\pgfplotsset{compat=1.18}
\begin{tikzpicture}
\begin{axis}[xbar, width=\linewidth, height=8cm, xlabel={Jumlah karya},
  symbolic y coords={Industri,Medis,Remote Sensing,Dataset,RGB-D SLAM,
    Fusi Multimodal,Pedestrian RGB-T,Pertanian,YOLO+RGB-D,Grasp Robotik,
    Survei YOLO,Pose 6D,Segmentasi RGB-D,Deteksi 3D,Estimasi Kedalaman,
    RGB-D SOD,Fondasi RGB},
  ytick=data, xmin=0, bar width=6pt, nodes near coords]
\addplot coordinates {(4,Industri)(5,Medis)(5,Remote Sensing)(6,Dataset)
  (7,RGB-D SLAM)(8,Fusi Multimodal)(8,Pedestrian RGB-T)(8,Pertanian)
  (8,YOLO+RGB-D)(9,Grasp Robotik)(9,Survei YOLO)(10,Pose 6D)
  (16,Segmentasi RGB-D)(17,Deteksi 3D)(21,Estimasi Kedalaman)(22,RGB-D SOD)
  (39,Fondasi RGB)};
\end{axis}
\end{tikzpicture}
```
