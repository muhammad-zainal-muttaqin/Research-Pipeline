# Recent Research of Incremental Structure from Motion for Unmanned Aerial Vehicle Images

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `chen2022recent` |
| Judul asli | Recent Research of Incremental Structure from Motion for Unmanned Aerial Vehicle Images |
| Penulis | Chen, Wu; Jiang, San; Li, Qingquan; Jiang, Wanshou |
| Tahun | 2022 |
| Venue | Wuhan Daxue Xuebao Xinxi Kexue Ban Geomatics and Information Science of Wuhan University |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [chen2022recent.pdf](../pdf/chen2022recent.pdf)
- DOI resmi: https://doi.org/10.13203/j.whugis20220130

## Gambaran Umum

Artikel berbahasa Mandarin ini, dengan abstrak berbahasa Inggris, adalah tinjauan naratif tentang *structure from motion* (SfM) inkremental untuk aerotriangulasi citra drone. SfM menaksir posisi dan arah kamera serta struktur adegan dari citra yang bertumpang tindih; versi inkremental menambah citra satu per satu, mulai dari sepasang citra awal. Artikel ini tidak melaporkan basis data, kueri, atau kriteria pemilihan kajian.

Penulis menyebut dua ciri citra drone yang menyulitkan SfM. Pertama, resolusi, tumpang tindih, dan jumlah citra yang tinggi membuat pencocokan fitur mahal, sedangkan sudut miring yang besar dan tekstur berulang menimbulkan banyak pencocokan salah. Kedua, penyelesaian geometri memerlukan *bundle adjustment* berulang setiap kali citra ditambahkan, sehingga waktu hitung tumbuh dengan jumlah citra.

Bagian pencocokan fitur membahas fitur buatan tangan dan fitur pembelajaran mendalam, percepatan pencocokan (pemilihan pasangan citra dari data posisi drone atau pencarian citra berbasis isi), dan pembuangan pencocokan salah dengan metode parametrik, nonparametrik, dan pembelajaran mendalam. Bagian geometri membahas SfM inkremental, percepatan *bundle adjustment*, dan pembagian adegan besar menjadi bagian kecil yang kemudian digabung. Satu tabel mendaftar perangkat lunak SfM terbuka, antara lain COLMAP, OpenSfM, VisualSfM, dan MicMac.

Penutupnya menyebut tantangan dari perubahan cara pengambilan data, pemrosesan adegan besar, perkembangan perangkat keras dan komunikasi, serta penggabungan dengan pembelajaran mendalam. Pertanian hanya disebut sebagai salah satu bidang penerapan drone. Penautan buah antarcitra tidak dibahas, tetapi sebab pencocokan salah yang disebut (tekstur berulang dan perubahan sudut pandang) sama dengan kesulitan menautkan buah yang mirip satu sama lain.
