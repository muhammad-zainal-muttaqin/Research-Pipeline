# Enhancing Outdoor Fruit Localization Accuracy: A Stereo Network Approach with Parallax Attention

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xie2023enhancing` |
| Judul asli | Enhancing Outdoor Fruit Localization Accuracy: A Stereo Network Approach with Parallax Attention |
| Penulis | Xie, Feng; Li, Tao |
| Tahun | 2023 |
| Venue | Proceedings 2023 38th Youth Academic Annual Conference of Chinese Association of Automation Yac 2023 |
| Kode | C5 (Depth, 3D, dan non-RGB) |

## Tautan Akses
- PDF: [xie2023enhancing.pdf](../pdf/xie2023enhancing.pdf)
- DOI resmi: https://doi.org/10.1109/yac59482.2023.10401448

## Gambaran Umum

Penulis menyebut bahwa lokalisasi buah yang akurat diperlukan untuk panen otomatis di kebun. Kedalaman (*depth*) dari kamera stereo memiliki tingkat pengisian yang kurang dan derau, sehingga memengaruhi akurasi lokalisasi. Penulis mengusulkan jaringan pencocokan stereo (*stereo matching*) berbasis mekanisme atensi untuk memperbaiki mutu kedalaman, lalu memakainya untuk memperkirakan titik pusat (*centroid*) buah.

Data berupa 1000 citra yang dikumpulkan di kebun buah di Haidian dan Changping, Beijing, dengan kamera Intel RealSense D435 pada kondisi cahaya dan jarak yang bervariasi. Setiap sampel memuat citra inframerah kiri dan kanan yang tersinkron serta citra warna. Jenis tanaman tidak disebut dalam teks. Pemberi label kebenaran dasar disparitas tidak disebut. Pembagian latih dan uji 9:1, dengan pemangkasan acak (*random crop*) dan 500 epoch.

Jaringan mengekstrak fitur multiskala dari citra kiri dan kanan dengan *feature pyramid network* (FPN), yaitu modul yang menggabungkan fitur beberapa resolusi. Biaya pencocokan (*matching cost*) dihitung dengan perkalian tensor pada baris horizontal yang sama (*parallax attention module*, PAM), sebagai pengganti konvolusi 3D pada *cost volume*. Disparitas diperhalus menjadi resolusi asli, diubah menjadi kedalaman dengan baseline dan panjang fokus, lalu diselaraskan ke kamera warna. Posisi 3D buah diperoleh dengan metode *frustum*: kotak deteksi dan segmentasi dari jaringan berbasis YOLOX menentukan garis tengah, dan kedalaman pusat buah diambil dari garis itu.

Pada tabel ablasi, model umum dengan 4 blok memberi EPE (*end-point error*, selisih disparitas prediksi dan acuan per piksel) 4,52 dengan waktu 100,47 ms. Model ringan dengan 2 blok memberi EPE 5,49 pada 81,71 ms. PAM dibandingkan dengan *cost volume*: EPE 4,68 berbanding 6,27, dengan memori 0,48 kali. Pada 50 pasang citra dari set validasi, galat lokalisasi median 6,87 mm, rerata 9,27 mm, dan galat baku 8,42 mm, dibandingkan 7,25, 11,22, dan 12,25 mm untuk algoritma bawaan kamera.

Keterbatasan yang dapat diperiksa dari teks: tidak ada pencacahan buah, tidak ada pengamatan ganda atas buah yang sama, dan evaluasi lokalisasi hanya memakai 50 pasang citra dari set validasi. Asal acuan posisi 3D buah untuk menghitung galat tidak disebut. Tidak ada pembagian per pohon atau kebun, dan tidak ada set uji terpisah dari set validasi.
