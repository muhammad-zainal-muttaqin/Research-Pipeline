# Kode reproduksi eksperimen

Folder ini hanya menyimpan kode dan konfigurasi. Bukti yang dihasilkan atau
diaudit berada di [`results/`](results/).
Pemisahan ini membuat pembaca dapat membuka hasil tanpa perlu menelusuri skrip.

| Saya ingin | Buka |
|---|---|
| Melatih model | [`train/`](train/) dan [`config/`](config/) |
| Mengevaluasi checkpoint | [`eval/`](eval/) |
| Menyiapkan data turunan | [`build/`](build/) |
| Memeriksa diagnosis | [`analysis/`](analysis/) |
| Menemukan JSON, kurva, dan split | [bukti eksperimen](results/) |
| Mengulang E-021 | [`REPRODUCE.md`](REPRODUCE.md) dan [`CATATAN-TEKNIS-E021.md`](CATATAN-TEKNIS-E021.md) |

Metrik final yang boleh dikutip ada di
[`../METRICS.md`](../METRICS.md). Untuk
E-022, baca [audit](../AUDIT-E022.md) sebelum membuka
[arsip seed-42](../archive/E022-seed42-awal.md).

## Isi

| Lokasi | Fungsi |
|---|---|
| `train/` | Skrip pelatihan |
| `eval/` | Skrip pengukuran dan diagnosis metrik |
| `build/` | Penyiapan dataset turunan |
| `analysis/` | Uji hipotesis dan diagnosis |
| `shell/` | Orkestrasi antrean historis |
| `config/` | Konfigurasi dataset Ultralytics |
| [`PETA-SKRIP.md`](PETA-SKRIP.md) | Hubungan skrip, eksperimen, dan keluaran |

Untuk pipeline lapangan, gunakan
[`../pipeline/`](../pipeline/) dan bukan kode eksperimen ini.

```bash
pip install -r experiments/code/requirements.txt
python experiments/code/eval/eval_all_pycoco.py
```

Skrip utama memakai lokasi repo untuk membaca `experiments/results/`. Dataset
SawitMVC publik dan master mentah tetap perlu disediakan sesuai catatan di
[`REPRODUCE.md`](REPRODUCE.md).
