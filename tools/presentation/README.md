# Pembangun dek `reports-simple-id.pptx`

Skrip perakit dek 16 slide Bahasa Indonesia dari `reports-simple-id.tex`.
Keluarannya `output/presentation/reports-simple-id.pptx`.

## Urutan jalan

```bash
python build_charts.py    # chart_fusi.png, chart_derau.png, chart_dataset.png
python chart_rgb.py       # chart_rgb.png  (perbandingan detektor RGB, E-021)
python build_panel.py     # panel_mvc.png, panel_depth.png (contoh citra + potongan)
python build_deck.py      # rakit pptx
python verify_deck.py     # periksa geometri: luar kanvas, tumpang tindih, luapan
```

Seluruh skrip menulis PNG ke direktorinya sendiri, dan `build_deck.py` membaca
PNG dari direktori yang sama. `fig_hipotesis.png` adalah salinan
`manuscript/figures/N02-rgbd-hypothesis-gpt-image-2.png`.

## Ketergantungan data

`build_panel.py` membaca dua dataset yang **tidak ada di repo ini**:

| Dataset | Lokasi yang dipakai | Citra terpilih |
|---|---|---|
| SawitMVC lama | `Baseline-SawitMVC/SawitMVC-YOLO` | `DAMIMAS_A21B_0641_3.jpg` |
| SawitMVC-Depth | `PalmAnnotate-Kotlin/Dataset-28-29July2026` | `DAMIMAS_A21B_0023_2.jpg` |

Aturan pemilihan citra sama untuk keduanya: dari seluruh citra yang memuat
keempat kelas, diambil yang kotak terkecilnya paling besar, lalu diperiksa
manual agar keempat potongan benar memperlihatkan tandan. SawitMVC punya 573
citra semacam itu, SawitMVC-Depth hanya 8.

Tanpa kedua dataset, `build_panel.py` gagal. Itu perilaku normal, bukan bug.

## Verifikasi tata letak

`verify_deck.py` tidak merender slide. Ia menaksir tinggi teks dari panjang
karakter, ukuran font, dan lebar kotak, lalu memeriksa tiga hal: kotak di luar
kanvas, kotak teks yang beririsan, dan teks yang melebihi kotaknya. Jalankan
juga dengan `AVG_EM = 0.56` sebagai uji ketat.

Angka pada dek bersumber dari `reports-simple-id.tex`,
`experiments/EKSPERIMEN.md`, dan
`experiments/results/E-021/perkelas_pycoco.json`.
