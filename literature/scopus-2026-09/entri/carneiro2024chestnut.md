# Chestnut Burr Segmentation for Yield Estimation Using UAV-Based Imagery and Deep Learning

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `carneiro2024chestnut` |
| Judul asli | Chestnut Burr Segmentation for Yield Estimation Using UAV-Based Imagery and Deep Learning |
| Penulis | Carneiro, Gabriel A.; Santos, Joaquim; Sousa, Joaquim J.; Cunha, Ant\'onio; P\'adua, Lu\'\is |
| Tahun | 2024 |
| Venue | Drones |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [carneiro2024chestnut.pdf](../pdf/carneiro2024chestnut.pdf)
- DOI resmi: https://doi.org/10.3390/drones8100541

## Gambaran Umum

Kajian ini bertujuan mengurangi waktu dan tenaga yang diperlukan untuk menilai hasil kebun kastanye. Penulis mengusulkan metode segmentasi buah kastanye (bercak buah, burr) pada citra UAV yang diambil otomatis pada ketinggian pemotretan fotogrammetri umum dan dalam berbagai kondisi pencahayaan, lalu mengestimasi produktivitas dari data awan titik hasil pemrosesan fotogrammetri. Studi ini membatasi diri pada dua langkah awal, yaitu segmentasi bercak pada citra UAV dan penghitungan bercak; proyeksi ke awan titik untuk estimasi hasil direncanakan sebagai tahap lanjutan.

Data utama (Dataset 1) berasal dari perkebunan kastanye Castanea sativa seluas sekitar 0,55 hektar di Portugal timur laut. Pengambilan memakai UAV Phantom 4 Pro V2.0 dengan sensor CMOS 1 inci 20 MP pada ketinggian 30 m, sudut kamera −65°, tumpang tindih memanjang 90 persen dan melintang 80 persen, konfigurasi lintasan ganda, menghasilkan 601 citra pada 8 September 2020 saat awal pembentukan buah. Setiap citra dibagi menjadi 288 potongan 608×608 piksel. Anotasi dibantu ambang warna pada ruang CIELAB dengan rentang L*∈[50;100], a*∈[−40;0], dan b*∈[40;50], lalu dikoreksi di Label Studio pada 189 citra yang dipilih secara acak dan dibagi 66 persen latih, 17 persen validasi, dan 17 persen uji. Dataset 2 berasal dari Arakawa dkk., mencakup dua varietas (Castanea crenata dan Castanea mollissima) di Prefektur Gifu, Jepang, dengan UAV DJI Mavic Mini pada ketinggian 12–15 m, 500 citra 416×416 piksel, serta 53 citra 608×608 untuk penghitungan. Acuan manual Dataset 1 adalah 1.322 bercak hasil hitungan pakar pada 21 citra; Dataset 2 memiliki 4.234 bercak hitungan manual dan 6.753 bercak hitungan lapangan.

Metode yang diuji adalah tiga arsitektur segmentasi, yaitu U-Net, LinkNet, dan PSPNet, semuanya memakai backbone SE-ResNet-50, dengan YOLOv8m sebagai pembanding berbasis deteksi. U-Net dan LinkNet menerima masukan 320×320 piksel, PSPNet 336×336 piksel, dan ambang sigmoid ditetapkan 0,5. Pelatihan dilakukan dua fase masing-masing 50 epoch dengan AdamW, laju pembelajaran 1×10⁻³ lalu 1×10⁻⁴, serta augmentasi daring berupa pemotongan acak, pembalikan, derau Gauss, solarisasi, dan blur. Fungsi rugi menggabungkan Dice Loss dan Focal Loss. Penghitungan bercak memakai erosi dengan kernel elips 32 piksel untuk memisahkan wilayah yang menyatu, mengukur luas tiap wilayah dengan regionprops pada konektivitas 1, lalu membagi total piksel bercak dengan nilai modus, rata-rata, atau median luas wilayah.

U-Net memberi kinerja segmentasi terbaik. Pada Dataset 1, U-Net mencatat F1 0,56, IoU 0,39, presisi 0,51, dan recall 0,72; pada Dataset 2, F1 0,76 dan IoU 0,62; pada gabungan kedua data, F1 0,67 dan IoU 0,52. Akurasi penghitungan terbaik pada Dataset 1 adalah 0,71, dicapai oleh U-Net yang dilatih pada data gabungan dengan nilai modus, dengan galat 28,51 persen; model terbaik yang hanya dilatih pada Dataset 1 memberi galat 54,00 persen. YOLOv8m mencatat F1 0,52 pada Dataset 1, 0,78 pada Dataset 2, dan 0,77 pada data gabungan. Pada pengujian silang, model yang dilatih hanya pada Dataset 2 tidak mencapai IoU lebih dari 0,1 di Dataset 1, sedangkan U-Net yang dilatih pada Dataset 1 mencapai IoU 0,27 di uji Dataset 2. Untuk Dataset 2, PSPNet memberi RMSE 2,29 ketika jumlah wilayah digunakan; YOLOv8m memberi RMSE 4,62 pada citra 608×608 dengan data gabungan, dibandingkan RMSE 6,30 yang dilaporkan Arakawa dkk. Waktu pelatihan pada data gabungan adalah 96, 98, 40, dan 9 menit berturut-turut untuk U-Net, LinkNet, PSPNet, dan YOLOv8m.

Penulis menyatakan sejumlah batasan. Kastanye mudah tumbuh berkelompok, sehingga wilayah bercak yang berdekatan menyatu dalam mask dan menyebabkan hitungan kurang. Penggabungan kedua dataset menurunkan kualitas segmentasi pada Dataset 1 karena perbedaan penampilan bercak: bercak Dataset 2 berwarna hijau pada cuaca berawan, sedangkan bercak Dataset 1 hijau di tengah dan kuning di tepi pada cuaca cerah. Kesalahan juga muncul pada daun berpenyakit fitosanitasi dan bayangan, serta pada bercak kecil terisolasi. Hitungan manual pada Dataset 2 mengabaikan sebagian bercak tertutup, sehingga acuan lapangan 6.753 lebih besar daripada 4.234. Penulis mengusulkan penambahan ukuran dan keragaman data, pengujian ambang selain 0,50, resolusi citra lebih besar, dan pemanfaatan proyeksi awan titik untuk mengatasi duplikasi akibat citra yang tumpang tindih.

