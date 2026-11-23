# Image Detection and Classification of Oil Palm Fruit Bunches

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `robi2022image` |
| Judul asli | Image Detection and Classification of Oil Palm Fruit Bunches |
| Penulis | Robi, Siti Nur Aisyah Binti Mohd; Izhar, Mohd Azri Bin Mohd; Sahrim, Mus'Ab Bin; Ahmad, Norulhusna Binti |
| Tahun | 2022 |
| Venue | 4th International Conference on Smart Sensors and Application Digitalization for Societal Well Being Icssa 2022 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [robi2022image.pdf](../pdf/robi2022image.pdf)
- DOI resmi: https://doi.org/10.1109/icssa54161.2022.9870945

## Gambaran Umum

Kajian ini membangun sistem deteksi dan klasifikasi kematangan tandan buah segar (TBS) kelapa sawit dengan model YOLO (*You Only Look Once*, detektor objek satu tahap yang memprediksi kotak pembatas dan kelas dalam satu langkah). Penulis menyebut pemanen menilai kematangan secara manual lewat warna dan jumlah brondolan di tanah, cara yang menurut mereka dapat tidak akurat. Empat tingkat kematangan dipakai: mentah, kurang matang, matang, dan terlalu matang. Dua tugas diuji: deteksi satu kelas (hanya TBS) dan klasifikasi empat kelas.

Data berupa 175 citra dari internet (Google Images). Tiap citra asli menghasilkan satu citra tambahan lewat rotasi, pergeseran lebar, penskalaan, dan pembalikan horizontal, sehingga totalnya 350 citra. Kotak pembatas digambar pada TBS, tetapi pemberi label tidak disebut. Pembagian data adalah 70% latih, 20% verifikasi, dan 10% uji. Ukuran masukan 416 x 416 piksel. Varietas disebut sebagai hibrida dura dan pisifera yang umum di Malaysia, tanpa rincian lokasi atau sensor.

Empat model dibandingkan: YOLOv3, YOLOv3-tiny, YOLOv4, dan YOLOv4-tiny. Versi *tiny* adalah varian ringan dengan jaringan lebih kecil untuk perangkat tertanam. Semua model diinisialisasi dari bobot terlatih (*transfer learning*, yaitu penyesuaian bobot yang sudah dilatih pada data lain) lalu dilatih ulang dengan 2.000 iterasi (satu kelas) atau 4.000 iterasi (empat kelas), *batch* 32. Metrik yang dipakai: *average precision* (AP, luas di bawah kurva presisi-*recall*), mAP (rerata AP antarkelas), presisi, *recall*, F1, dan *intersection over union* (IoU, tumpang tindih kotak prediksi dengan kotak acuan).

Pada deteksi satu kelas, YOLOv4 mencapai mAP 98,97% dengan 350 citra, F1 0,96, dan rerata IoU 68,80%. Dengan 150 citra, mAP YOLOv3-tiny 45,91%, YOLOv3 64,7%, YOLOv4-tiny 71,10%, dan YOLOv4 76,86%. Pada empat kelas, YOLOv4 mencapai mAP 77,20%, presisi 0,70, *recall* 0,71, F1 0,7, dan IoU 51,68%. YOLOv3 hanya 55,70%. Abstrak menyebut 98,70%, sedangkan isi teks menyebut 98,97%. Teks tidak menyatakan data uji tempat angka itu dihitung selain bahwa 10% data dipakai untuk uji.

Keterbatasan yang dapat diperiksa: set data kecil (175 citra asli), berasal dari internet, dan pembagian per pohon atau per sumber tidak disebut. Citra augmentasi dari citra asli yang sama dapat jatuh pada bagian latih dan uji, karena urutan augmentasi dan pembagian tidak dijelaskan. Penulis sendiri menyebut jumlah citra sedikit dan kelas tidak seimbang. Angka mAP 150 citra pada Tabel II dan III disebut diperoleh saat pelatihan. Tidak ada pencacahan buah dan tidak ada acuan hitung.
