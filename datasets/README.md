# Datasets

Wadah dataset lokal yang dipakai untuk eksperimen. Isi folder ini **tidak
masuk Git** karena ukurannya terlalu besar — hanya metadata dan README
dataset yang dilacak.

## Isi folder

| Lokasi | Isi |
|---|---|
| `SawitMVC-Depth/` | Dataset depth sensor Orbbec: 352 pohon, 1.408 citra RGB 1280x800, depth Y16 848x480 uint16 milimeter. Sudah punya [README sendiri](SawitMVC-Depth/README.md). Sumber: [Hugging Face](https://huggingface.co/datasets/ULM-DS-Lab/SawitMVC-Depth), CC BY-NC 4.0 |

## Dataset lain yang dipakai tetapi tidak ada di repo

| Dataset | Lokasi di workspace | Isi |
|---|---|---|
| SawitMVC | `/workspace/SawitMVC/data` | 953 pohon, 3.992 citra 960x1280, label YOLO empat kelas (B1–B4) |
| Sawit (master mentah) | `/workspace/Sawit/data` | 3.992 citra 3024x4032 resolusi penuh, tanpa anotasi |
