# A Transfer Learning-Based Multimodal Model for Grape Detection and Counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `xu2025transfer` |
| Judul asli | A Transfer Learning-Based Multimodal Model for Grape Detection and Counting |
| Penulis | Wenwen, XU; Yu, KeJian; Dai, ZeXu; Yunzhi, WU |
| Tahun | 2025 |
| Venue | Smart Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [xu2025transfer.pdf](../pdf/xu2025transfer.pdf)
- DOI resmi: https://doi.org/10.12133/j.smartag.sa202504005

## Gambaran Umum

Penulis menyatakan bahwa estimasi hasil panen anggur sulit dan mahal. Deteksi anggur hijau, yang warna butirnya mirip daun, memiliki keterbatasan. Deteksi tandan dengan butir kecil juga tidak efektif. Untuk mengatasinya, penulis mengusulkan kerangka deteksi multimodal berbasis pembelajaran transfer (*transfer learning*) bernama GDCNet. Kerangka ini mendeteksi dan menghitung tandan anggur dari berbagai varietas sebagai dukungan bagi prediksi hasil panen dan pengelolaan kebun.

Data utama adalah set data publik WGISD (*Wine Grape Instance Segmentation Dataset*), berisi 300 citra berwarna beresolusi 2.048×1.365 piksel dari lima varietas, dengan 4.432 kotak tandan. Dari kotak itu, 3.582 dipakai untuk latih, 850 untuk validasi, dan 850 untuk uji. Penulis menambah 280 citra lapangan dari kebun anggur di Hefei, Tiongkok, dengan empat varietas dan 2.411 kotak. Gabungan 6.843 kotak dibagi menjadi 5.503 latih, 1.340 validasi, dan 1.340 uji. Pemberi label untuk data lapangan tidak disebut.

GDCNet memakai struktur dua pengode, satu pendekode. Pengode citra (misalnya *Swin Transformer*) dan pengode teks (misalnya BERT) mengekstrak fitur. Modul penguat fitur memakai atensi silang (*cross-attention*) agar fitur citra dan teks saling memengaruhi. Modul pemilihan kueri berpemandu bahasa memilih fitur citra yang paling cocok dengan teks sebagai kueri pendekode. Pendekode lintas modalitas lalu menghasilkan kotak tandan. Bobot awal berasal dari model terlatih pada data publik, lalu disetel ulang dengan sedikit citra anggur.

Pada WGISD, GDCNet mencapai mAP50 80,3%, mAP 53,2%, mAP75 58,2%, dan mAR 76,5% pada data uji. Nilai mAP50 itu 2,7 poin persentase di atas model terbaik kedua. Galat hitung tandan adalah MAE 1,65 tandan dan RMSE 2,48 tandan, sedangkan NAS-FPN memperoleh MAE 2,10 dan RMSE 2,72. Pada sembilan varietas gabungan, hasilnya mAP50 82,5%, mAP 58,5%, MAE 1,44, dan RMSE 2,19. Pada tandan kecil, mAP_s mencapai 74,2%.

Keterbatasan yang dapat diperiksa dari teks: pembagian latih, validasi, dan uji dilakukan per kotak pembatas, bukan per citra atau per tanaman, sehingga kotak dari citra yang sama dapat berada di lebih dari satu bagian. Satuan sampel untuk MAE dan RMSE tidak dijelaskan, dan acuan hitung adalah label kotak, bukan hitung tangan di kebun. Hasil Grounding DINO memakai bobot terlatih publik. Penulis menyebut galat terkonsentrasi pada tandan hijau yang tertutup daun.
