# In-field apple size estimation using photogrammetry-derived 3D point clouds: Comparison of 4 different methods considering fruit occlusions

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `genemola2021field` |
| Judul asli | In-field apple size estimation using photogrammetry-derived 3D point clouds: Comparison of 4 different methods considering fruit occlusions |
| Penulis | Gen\'e-Mola, Jordi; Sanz-Cortiella, Ricardo; Rosell-Polo, Joan R.; Escol\`a, Alexandre; Gregorio, Eduard |
| Tahun | 2021 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | apple |

## Tautan Akses
- PDF: [genemola2021field.pdf](../pdf/genemola2021field.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2021.106343

## Gambaran Umum

Gené-Mola dkk. (2021) menilai apakah diameter apel dapat diukur dari model 3D yang dibangun dengan *structure-from-motion* dan *multi-view stereo* (SfM-MVS) dari citra apel yang sudah tersegmentasi. Kajian ini mengukur ukuran buah, bukan jumlahnya. Empat estimator ukuran dibandingkan dengan diameter sebenarnya dari model bola acuan (*ground truth*). Estimator MSAC memberi MAPE 5,9% pada apel dengan visibilitas di atas 40%.

Ukuran buah berguna untuk pendugaan hasil dan penjadwalan panen. Pengukuran manual memakan waktu dan tidak mencakup seluruh pohon. Kajian ini membangun model 3D setiap apel dari beberapa foto yang diambil dari sudut berbeda, lalu mengestimasi diameternya dari titik-titik model tersebut. Kendalanya adalah bagian apel yang tertutup daun atau apel lain. Bagian yang tertutup membuat titik permukaan kurang lengkap dan estimasi ukuran dapat meleset.

Setiap apel direkonstruksi sebagai awan titik (*point cloud*, kumpulan titik koordinat 3D) dari citra yang sudah disegmentasi. Ukuran diestimasi dengan mencocokkan bentuk bola ke titik-titik tersebut. Kajian ini membandingkan beberapa cara pencocokan dan menguji pengaruh visibilitas apel terhadap galat.

Visibilitas V dihitung dengan V = SV / (SV + SO) × 100%. SV adalah jumlah titik model yang terlihat pada citra, dan SO adalah jumlah titik yang tertutup. Keduanya diperoleh dengan memproyeksikan titik-titik pada bola *ground truth* ke citra.

Citra apel diambil di lapangan dan di laboratorium. Pada citra lapangan, apel dipisahkan dari latar dengan Mask-RCNN (jaringan segmentasi objek per instans). Pada citra lab dipakai ambang warna HSV, dengan piksel latar didefinisikan sebagai S < 0,4 dan V > 0,55. Model 3D dibangun dengan Agisoft Metashape v1.6.4.

Sebelum estimasi ukuran, titik pencilan dibuang dengan aturan k = 50 dan α = 1.

- **Largest segment (Lar Seg):** memakai segmen terbesar.
- **Least squares sphere fit (LS):** mencocokkan bola dengan kuadrat terkecil.
- **MSAC:** mencocokkan bola dengan δ = 0,003 m, 10.000 iterasi, dan tingkat kepercayaan 99,9%.
- **Template matching dengan ICP_finite (TM):** mencocokkan templat bola.

Pengujian dilakukan pada 640 model apel 3D dari citra lapangan dan laboratorium. Galat dilaporkan sebagai MAE, MAPE, MBE, RMSE, dan R², dipisahkan menurut tiga ambang visibilitas (V > 0%, V > 20%, V > 40%).

Untuk MAPE pada ketiga ambang, Lar Seg berada pada 23,6%, 23,6%, dan 26,2%. LS berada pada 12,2%, 8,9%, dan 6,9%. MSAC berada pada 12,2%, 7,4%, dan 5,9%. TM berada pada 11,1%, 8,4%, dan 6,6%. Pada V > 40%, MSAC memberi MAE 3,7 mm, MAPE 6%, dan RMSE 5,1 mm, dengan R² di atas 0,9 pada 267 apel.

Lar Seg paling buruk pada semua ambang. LS, MSAC, dan TM relatif sejajar, dan perbedaan utamanya ada pada bias (MBE). MSAC memberi MBE +1,2 mm pada V > 0%, sedangkan Lar Seg memberi +11,4 mm sampai +16,2 mm. Waktu komputasi untuk 615 apel adalah 0,45 detik (LS), 2,64 detik (MSAC), dan 75,66 detik (Lar Seg).

Penulis menyimpulkan bahwa pendekatan SfM-MVS untuk apel yang sudah terdeteksi "is an interesting and promising technique for fruit size estimation".

Kajian ini melaporkan galat terpisah menurut visibilitas, sehingga terlihat bahwa galat turun ketika apel lebih terlihat. Perbandingan empat estimator dilakukan pada data yang sama.

Penulis menyebut waktu pemrosesan sebagai kelemahan utama, karena membatasi penggunaan untuk area besar (pada abstrak: 2.760 detik untuk 6 pohon). Hasil kajian mengukur satu sifat buah, yaitu diameter, dari satu rekonstruksi per apel. Kajian ini tidak menguji apakah identitas apel dipertahankan lintas pandang.
