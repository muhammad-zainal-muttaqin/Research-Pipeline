# Method of greenhouse tomato fruit identification and yield estimation based on improved YOLOv3

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cheng2021method` |
| Judul asli | Method of greenhouse tomato fruit identification and yield estimation based on improved YOLOv3 |
| Penulis | Cheng, W.; others |
| Tahun | 2021 |
| Venue | Journal of Chinese Agricultural Mechanization |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [cheng2021method.pdf](../pdf/cheng2021method.pdf)
- DOI resmi: https://doi.org/10.13733/j.jcam.issn.2095-5553.2021.04.25

## Gambaran Umum

Kajian ini bertujuan menaksir hasil tomat rumah kaca secara daring dengan mencacah buah merah dan buah hijau pada citra tanaman. Penulis menyebut tanaman tomat di rumah kaca tumbuh rapat, sehingga batang, daun, dan buah saling menutupi dan buah sulit dikenali. Mereka mengusulkan detektor YOLOv3 yang diperbaiki untuk dua kelas buah, yaitu merah (matang) dan hijau (belum matang).

Citra diambil di rumah kaca tomat budi daya industri dengan perangkat penaksir hasil yang bergerak di atas rel di antara baris tanaman. Kamera FL3-U3-13S2C berlensa 8 mm dipasang pada kepala putar dua sumbu, berjarak 800 mm dari tanaman, dengan bidang pandang 500 mm × 400 mm. Sebanyak 2.000 citra dikumpulkan pada berbagai waktu, lalu diperbanyak dengan putaran dan penskalaan menjadi 4.000 citra. Buah merah dan hijau ditandai kotak dengan LabelImg. Dari 4.000 citra itu, 3.200 dipakai melatih dan 800 menguji. Pemberi label tidak disebut.

Fungsi kerugian posisi YOLOv3 diganti dengan GIoU (*generalized intersection over union*), yaitu ukuran tumpang tindih kotak yang tetap memberi gradien ketika kotak prediksi dan kotak acuan tidak beririsan. Sembilan kotak acuan awal (*anchor*) ditentukan dengan pengelompokan *K-means* pada ukuran kotak berlabel, lalu dibagi ke tiga tingkat peta fitur. Hitungan buah adalah jumlah deteksi tiap kelas pada satu citra; buah tidak ditautkan antarcitra.

Pada citra uji, mAP naik dari 92,1% (YOLOv3) menjadi 95,7% (YOLOv3 yang diperbaiki), dengan waktu 15 ms per citra. Dalam uji lapangan, 200 bidang pandang dipilih acak, dan hitungan model dibandingkan dengan hitungan manual pada citra yang sama. Ketepatan taksiran, yaitu rasio jumlah deteksi terhadap jumlah hitungan manual, adalah 97,0% untuk buah merah, 95,5% untuk buah hijau, dan 96,3% untuk seluruh buah (YOLOv3: 96,2%, 91,8%, dan 93,6%) (Tabel 4). Pada 30 citra untuk setiap keadaan, kenaikan ketepatan buah merah dan hijau adalah 2,5% dan 1,4% untuk buah jarang, 5,5% dan 9,4% untuk buah rapat, serta 9,5% dan 11,3% untuk buah tertutup.

Keterbatasan yang dapat diperiksa dari teks adalah sebagai berikut. Perbanyakan data dilakukan sebelum pembagian latih dan uji, sehingga citra turunan dari citra yang sama dapat berada di kedua himpunan. Acuan hitung adalah hitungan manual pada citra, bukan hitungan di tanaman atau hasil panen. Ketepatan dinyatakan sebagai rasio jumlah total, sehingga deteksi berlebih dan buah terlewat dapat saling menutupi. Setiap bidang pandang dicacah sendiri, dan teks tidak menyebut cara menghindari hitungan ganda bila bidang pandang bertumpang tindih.
