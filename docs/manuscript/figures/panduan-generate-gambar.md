# Panduan Generate Ulang 10 Figur dengan GPT Image 2

Panduan ini menyimpan resep produksi untuk kesepuluh aset kanonis di folder
`figures/`. Prompt di bawah adalah prompt final yang dipakai sebagai dasar
versi saat ini; fakta, label, dan angka wajib selalu dibandingkan lagi dengan
brief `FNN-*.md` atau `CNN-*.md` yang bersangkutan.

## Prinsip yang tidak boleh berubah

1. Gambar adalah **figur inline jurnal**, bukan slide. Jangan buat judul
   global, subjudul, nomor gambar, caption, legenda dekoratif, atau footer di
   dalam gambar. Caption hanya berasal dari LaTeX.
2. Gunakan kanvas lanskap 16:9, latar hangat `#FAF9F6`, kartu bersudut
   membulat, ruang kosong longgar, dan panah arang tipis berkepala panah kecil.
3. Gunakan satu sans-serif yang jelas. Semua teks harus tepat ejaannya,
   tidak terpotong, tidak bertumpuk, dan tidak dilintasi garis.
4. Biru untuk RGB, emas-oker untuk Depth, merah bata untuk fusi/hasil/celah
   penting, dan arang untuk komponen netral atau YOLO.
5. Jangan memakai SVG atau PDF sebagai hasil produksi. Simpan hasil sebagai
   PNG dengan nama `FNN-slug-gpt-image-2.png` atau `CNN-slug-gpt-image-2.png`.

## Cara pakai

1. Buka brief terkait dan cek fakta sebelum membuat prompt.
2. Gunakan GPT Image 2 dengan satu gambar final yang sudah disetujui sebagai
   referensi gaya (misalnya `F04-strategi-fusi-gpt-image-2.png`). Referensi
   hanya untuk gaya visual, bukan untuk menyalin isi.
3. Gunakan **prompt dasar** berikut, lalu tambahkan prompt khusus figur.
4. Periksa PNG resolusi asli dan halaman `main.pdf` serta `main-elsarticle.pdf`.
   Ulangi generasi apabila ada satu saja angka, label, panah, atau ejaan salah.
5. Setelah lolos, salin ke nama aset kanonis dan pastikan `body.tex` menunjuk
   nama tersebut.

## Prompt dasar

Tambahkan teks ini di awal setiap prompt khusus:

```text
Use case: infographic-diagram. Create a single inline scientific journal
figure; its caption is outside the artwork. Use the provided reference image
only for clean sans-serif typography, warm off-white background #FAF9F6,
restrained colorful palette, rounded rectangular cards, generous whitespace,
and crisp publication quality. Landscape 16:9. Do NOT include an outer title,
subtitle, figure number, caption, legend, decorative icon, or footer. All
Indonesian text must be perfectly readable and exactly spelled. No text may
overlap, clip, touch, or be crossed by connector lines.
```

Untuk C01 dan C02, ganti `infographic-diagram` dengan
`scientific bar-chart infographic`, tetapi pertahankan semua larangan judul
internal dan semua aturan keterbacaan.

## Prompt khusus dan aset keluaran

### F01 — `F01-taksonomi-gpt-image-2.png`

```text
Create a balanced taxonomy map with no global title. The root node is a
functional node reading "Deteksi Objek RGB-D untuk Sawit". From it create four
clearly separated branches: "Evolusi YOLO", "Deteksi RGB", "Fusi RGB-D", and
"Integrasi YOLO+RGB-D". Under Evolusi YOLO place "Evolusi YOLO (14)" and
"Survei YOLO (9)". Under Deteksi RGB place "Fondasi RGB & Transformer (27)".
Under Fusi RGB-D place exactly: "Estimasi Kedalaman (20)", "RGB-D SOD (23)",
"Segmentasi RGB-D (16)", "Fusi RGB+Depth Deteksi (5)", "Pose 6D & Grasp
Robotik (19)", "Deteksi 3D LiDAR-Kamera (18)", "Pedestrian RGB-T (7)",
"RGB-D SLAM (7)", and "Dataset & Tolok Ukur (7)". Under Integrasi YOLO+RGB-D
place "YOLO+RGB-D (7)" and "Aplikasi (22)". Use blue, ochre, brick-red, and
charcoal branch headers, but use only parent-child connectors; do not imply
relationships between sibling clusters.
```

### F02 — `F02-timeline-yolo-gpt-image-2.png`

```text
Create one clean horizontal timeline without a global title. Use exactly these
year markers and cards: 2016 "YOLOv1 / regresi kisi"; 2017 "YOLOv2 / YOLO9000
/ anchor klaster"; 2018 "YOLOv3 / multiskala"; 2020 "YOLOv4 + PP-YOLO /
konsolidasi"; 2021 "YOLOX / anchor-free"; 2022 "YOLOv6 / efisiensi HW"; 2023
"YOLOv7 / agregasi lapisan"; 2024 four vertically stacked cards "YOLOv9 /
gradien terprogram", "YOLOv10 / bebas-NMS", "YOLOv11 / kerangka modular",
and "YOLO-World / kosakata terbuka"; 2025 "YOLO26 / real-time tanpa NMS".
Make the 2024 stack tall with generous spacing so no cards collide. Add only
two small brick-red milestone labels: "ANCHOR-FREE" at 2021 and "BEBAS-NMS"
at 2024. Keep all connectors attached cleanly to the timeline.
```

### F03 — `F03-silsilah-rgb-gpt-image-2.png`

```text
Create a clean five-lane detector lineage diagram with no global title. Use
only these functional lane headers: "Dua-tahap", "Satu-tahap", "Anchor-free",
"Transformer", and "Backbone". Draw these independent lineage chains:
R-CNN -> Fast R-CNN -> Faster R-CNN -> Mask R-CNN; SSD -> RetinaNet ->
EfficientDet; FCOS -> CenterNet; DETR -> Deformable DETR -> Conditional DETR
-> DN-DETR -> DINO -> Co-DETR; and RT-DETR -> RF-DETR -> Le-DETR. In the
Backbone lane place ResNet, ViT, Swin, Swin V2, PVT, ConvNeXt, and CBAM.
FPN and Sparse R-CNN are separate unconnected cards in the Dua-tahap lane.
Use subtle dotted support links only from ResNet to Dua-tahap and Satu-tahap,
and from ViT or Swin to Transformer; never cross text or create extra lineage
arrows. Make each lane spacious and visually independent.
```

### F04 — `F04-strategi-fusi-gpt-image-2.png`

```text
Show exactly three equal panels side by side with only these functional panel
headers: "Fusi Awal", "Fusi Menengah", and "Fusi Akhir". Panel 1 flow:
"RGB" and "Depth" -> "Masukan 4 kanal" -> "Encoder" -> "Prediksi".
Panel 2 flow: "RGB" -> "Encoder RGB" and "Depth" -> "Encoder Depth"; both
merge into "Atensi Lintas-Modal" -> "Prediksi". Panel 3 flow: "RGB" ->
"Encoder RGB" -> "Kepala RGB" and "Depth" -> "Encoder Depth" ->
"Kepala Depth"; both merge into "Gabung keluaran" -> "Prediksi". Use blue
for RGB, ochre for Depth, brick red for attention, and charcoal for neutral
blocks. Keep all connectors inside their panels.
```

### F05 — `F05-pola-yolorgbd-gpt-image-2.png`

```text
Show exactly two side-by-side, equally sized panels with only these functional
panel headers: "Pola 1 — Perluasan Kanal" and "Pola 2 — Deteksi-lalu-Proyeksi".
Left panel flow: "RGB (3 kanal)" plus "Depth (1 kanal)" merge into "Masukan
4 kanal", then "Backbone YOLO", then "Kepala Deteksi", then "Kotak + kelas".
Right panel flow: "RGB" -> "YOLO deteksi 2D" -> "Kotak 2D". Below it,
"Depth" and the nearby "Kotak 2D" merge into "Proyeksi / angkat 3D", then
"Lokasi 3D / jarak / awan titik". Use thin charcoal arrows with arrowheads;
RGB cards blue, Depth cards ochre, projection/output brick red, YOLO cards
charcoal. Keep all connectors inside their own panel.
```

### F06 — `F06-atensi-lintasmodal-gpt-image-2.png`

```text
Create one balanced cross-modal attention module. At the far left place two
vertically aligned source cards: top "F_rgb" in blue and bottom "F_depth" in
ochre. Each points horizontally to its own card: top "Peta bobot RGB", bottom
"Peta bobot Depth". The RGB weight map points diagonally down to "Timbang
F_depth"; the Depth weight map points diagonally up to "Timbang F_rgb". These
two cards merge cleanly into "Atensi Lintas-Modal", then "F_fusi", then
"ke lapisan berikut". Use only necessary arrows, visibly separated diagonal
paths, and small unobtrusive labels "saling menimbang" near both weighted
paths.
```

### F07 — `F07-funnel-sawit-gpt-image-2.png`

```text
Create a centered six-level research funnel, widest at the top and narrowest
at the bottom, with clear breathing room between rounded funnel bands. Label
the bands exactly: "1. Deteksi objek RGB matang / YOLO · transformer";
"2. Kedalaman monokular / fondasi"; "3. Fusi RGB-D + atensi / lintas-modal";
"4. YOLO + RGB-D / terbukti"; "5. Celah sawit / dataset · depth · oklusi";
and "6. Posisi riset / YOLO RGB-D sawit". Color the first four progressively
blue, teal, muted green, and ochre; the last two are brick red. Add only a
small downward side arrow labelled "spesifik dan belum terjawab".
```

### F08 — `F08-pipeline-sawit-gpt-image-2.png`

```text
Create an end-to-end palm-fruit RGB-D detection pipeline. At far left, place
one blue input card "Citra RGB kebun". It branches to top "Encoder RGB" and
bottom "Estimasi pseudo-depth monokular" -> "Encoder Depth". The two encoder
cards merge into "Fusi menengah + atensi lintas-modal + penimbangan adaptif".
Then arrow to "Kepala deteksi YOLO", then to "Penghitungan tandan + klasifikasi
kematangan". From the final result draw one subtle dotted optional arrow down
to "Proyeksi 3D / lokasi panen robotik". Use blue for RGB, ochre for depth,
brick red for fusion and final results, charcoal for YOLO, and keep each arrow
clearly separated.
```

### C01 — `C01-distribusi-tahun-gpt-image-2.png`

```text
Draw a clean annual vertical bar chart with no global title or legend.
Horizontal-axis label: "Tahun". Vertical-axis label: "Jumlah publikasi".
Use light horizontal grid lines only. Plot exactly these labelled bars, with
the integer above each bar: 2012=2, 2014=3, 2015=4, 2016=4, 2017=12,
2018=12, 2019=18, 2020=30, 2021=36, 2022=25, 2023=23, 2024=21, 2025=7,
2026=5. Do not draw a bar for 2013. Use blue for 2012–2020 and brick red for
2021–2026. Make the 2021 peak subtly emphasized. Exact data is essential.
```

### C02 — `C02-distribusi-tema-gpt-image-2.png`

```text
Draw a ranked horizontal bar chart, largest at the top, with no global title
or legend. Horizontal-axis label: "Jumlah publikasi". Use light vertical grid
lines only. Print values at bar ends. Plot exactly: Fondasi RGB 39; RGB-D SOD
22; Estimasi Kedalaman 21; Deteksi 3D 17; Segmentasi RGB-D 16; Pose 6D 10;
Survei YOLO 9; Grasp Robotik 9; YOLO+RGB-D 8; Pertanian 8; Pedestrian RGB-T 8;
Fusi Multimodal 8; RGB-D SLAM 7; Dataset 6; Remote Sensing 5; Medis 5;
Industri 4. Use blue for the first four bars and brick red for all remaining
bars. Exact spelling and data are essential.
```

## Pemeriksaan akhir

- Pastikan tidak ada judul ganda di area paling atas gambar.
- Cocokkan setiap label/angka dengan brief sebelum mengganti aset aktif.
- Render naskah dan periksa teks pada ukuran halaman, terutama C01 yang
  ditempatkan satu kolom pada varian IEEE.
- Jika satu detail salah, generate ulang gambar tersebut saja; jangan mengubah
  caption, nomor figur, atau fakta di `body.tex`.
