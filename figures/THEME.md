# THEME — Spesifikasi Gaya Visual Tunggal untuk Semua Figur

Berkas ini adalah **satu-satunya sumber kebenaran gaya** untuk seluruh figur di
`main.tex`. Setiap *brief* figur (`figures/FNN-*.md`, `figures/CNN-*.md`) wajib
merujuk berkas ini agar hasil generate (Gemini) seragam. Palet diselaraskan dengan
`PLAN.md` §13 (ruang baca web) supaya naskah dan situs memakai identitas visual sama.

---

## 1. Palet Warna

| Peran | Hex | Catatan |
|---|---|---|
| Kertas (latar) | `#FAF9F6` | latar semua figur; hangat, bukan putih murni |
| Tinta (garis & teks) | `#1A1D21` | garis utama, label, judul |
| Aksen (penekanan) | `#A03028` | merah bata; hanya untuk simpul/alur yang ditekankan |
| Hairline (pemisah) | `#E6E3DA` | garis bantu, kisi, batas halus |

**Jewel-tone per tema** (satu warna per klaster, dari `PLAN.md` §13) — dipakai untuk
mengode kelompok node pada figur taksonomi/silsilah:

| Tema | Hex |
|---|---|
| Fondasi RGB | `#2B6CB0` |
| Survei YOLO | `#0F766E` |
| Estimasi Kedalaman | `#A6740E` |
| Fusi RGB-D (SOD/Segmentasi) | `#8B5CB4` |
| Persepsi 3D & Geometri | `#4A5568` |
| Pedestrian/Multimodal | `#B45309` |
| YOLO + RGB-D | `#A03028` |
| Aplikasi | `#2F855A` |

## 2. Tipografi

- **Judul figur / heading node:** serif (Newsreader, Georgia, atau Source Serif).
- **Label node & sumbu:** sans-serif (Inter, Source Sans, atau Helvetica).
- **Angka, kode, nama model:** monospace (JetBrains Mono, IBM Plex Mono).
- Ukuran relatif konsisten antar-figur: judul > label kelompok > label node > anotasi.

## 3. Kaidah Bentuk

- Garis *hairline* 1–1,5 pt; tanpa bayangan berat, tanpa gradasi mencolok.
- Sudut node membulat halus (radius kecil, seragam).
- Latar kertas penuh; tanpa bingkai luar tebal.
- Orientasi **lanskap**; rasio, tebal garis, ukuran node, dan margin seragam antar-figur.
- Panah alur searah, kepala panah kecil dan konsisten.
- Tanpa emoji, tanpa ikon dekoratif; ikon hanya bila fungsional dan monokrom tinta.
- Kontras teks minimal setara WCAG AA terhadap kertas.

## 4. Ekspor

- Format utama: **PDF vektor** (untuk `\includegraphics` di LaTeX). Alternatif PNG ≥300 dpi.
- Penamaan berkas hasil: `figures/FNN-slug.pdf` (mis. `figures/F01-taksonomi.pdf`),
  sama dengan nama yang dirujuk di `main.tex`.
- Bidang aman (*safe margin*) ≥4% di tiap sisi agar tidak terpotong saat disisipkan.

## 5. Alur Pemakaian

1. Baca berkas ini.
2. Buka *brief* figur (`figures/FNN-*.md`): ambil konten faktual (node/edge atau data).
3. Tempel **Prompt Gemini** dari *brief* (sudah memuat kaidah tema ini) → generate.
4. Bandingkan hasil dengan **sumber mermaid** di *brief* (struktur harus identik; tidak
   ada node/relasi tambahan).
5. Simpan sebagai `figures/FNN-slug.pdf`; `main.tex` sudah merujuk nama itu.

## 6. Fallback

Bila figur Gemini belum siap, **sumber mermaid** di tiap *brief* dapat dirender langsung
(mis. via editor mermaid) dan diekspor sebagai gambar sementara dengan palet di atas.
Struktur mermaid adalah spesifikasi kebenaran; hasil Gemini hanya memperhalus tampilan.
