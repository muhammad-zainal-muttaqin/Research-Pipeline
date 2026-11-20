# Intact detection of highly occluded immature tomatoes on plants using deep learning techniques

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `mu2020intact` |
| Judul asli | Intact detection of highly occluded immature tomatoes on plants using deep learning techniques |
| Penulis | Mu, Yue; Chen, Tai-Shen; Ninomiya, Seishi; Guo, Wei |
| Tahun | 2020 |
| Venue | Sensors Switzerland |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [mu2020intact.pdf](../pdf/mu2020intact.pdf)
- DOI resmi: https://doi.org/10.3390/s20102984

## Gambaran Umum

Makalah ini menghitung buah tomat dari citra kamera tunggal yang diambil berurutan sepanjang satu baris tanaman di rumah kaca. Tujuannya ada dua: mendeteksi tiap tomat dengan Faster R-CNN, lalu menghitung jumlah tomat per tanaman dan per baris. Pertanyaan utamanya adalah apakah hasil deteksi dari citra tunggal dapat dipercaya sebagai pengganti hitungan manual.

Data berupa foto baris tanaman yang diambil dengan satu kamera. Foto berurutan dijahit (stitching) menjadi peta satu baris, sehingga tomat yang terpotong di tepi satu foto dapat muncul utuh di foto berikutnya. Enam citra hasil jahitan dipakai sebagai set uji. Tiga arsitektur backbone dibandingkan, yaitu ResNet-50, ResNet-101, dan Inception-ResNet-v2, semuanya diawali bobot pralatih COCO. ResNet-101 dipilih karena memberi AP validasi 0,82 dan AP uji 0,87. Deteksi dianggap benar bila intersection over union (IoU) minimal 0,5. Hasil deteksi disaring dengan ambang skor 0,5, dan kotak yang tumpang tindih di sambungan jahitan digabung agar tomat tidak terhitung dua kali.

Hasil utama adalah AP uji 87,83% pada ambang IoU 0,5 dan R2 = 0,87 untuk jumlah tomat dibanding hitungan acuan. Peta baris gabungan memuat 1.422 tomat. Penulis melaporkan laju kesalahan (miss rate) hingga 16%, dan jumlah yang kurang terhitung meningkat bila satu sub-citra memuat lebih dari 20 tomat. Dalam Tabel 4, makalah ini mencatat F1 83,67% dan AP 87,83%, sedangkan Yolo-tomato mencapai F1 93,91% dan AP 96,40%. Waktu inferensi 0,37 detik per citra pada GPU GTX 1060. Penulis juga mencatat tanda overfitting selama pelatihan. Angka-angka ini berasal dari set uji yang kecil, sehingga selisihnya dengan pembanding perlu dibaca bersama kondisi pengambilan citranya.

Makalah ini menghitung dari satu kamera. Penjahitan dipakai untuk memetakan lokasi dan menggabungkan kotak di sambungan, bukan untuk menggabungkan pengamatan tomat yang sama dari sisi berlawanan. Karena itu, hanya tomat yang terlihat dari kamera yang terhitung, dan tomat di sisi belakang tanaman tidak tercakup. Penulis menyebut pengambilan dua sisi sebagai pekerjaan lanjutan. Sistem juga tidak mengonversi jumlah tomat ke satuan area tetap, sehingga hasilnya belum dapat langsung dibandingkan dengan lintasan atau kebun lain.

Dari sisi bukti, makalah ini memberi contoh penghitungan pada satu pandang yang ditopang penjahitan lokal. Prediksi kematangan dan hasil panen hanya dibahas sebagai perspektif di bagian diskusi dan belum diukur. Keterbatasan utama yang tercatat adalah sisi tanaman yang tertutup, kepadatan tomat per sub-citra, dan ketergantungan pada satu kamera di satu lingkungan rumah kaca.
