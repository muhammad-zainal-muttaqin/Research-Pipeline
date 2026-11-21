# Fresh Fruit Bunch Ripeness Classification Methods: A Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `goh2025fresh` |
| Judul asli | Fresh Fruit Bunch Ripeness Classification Methods: A Review |
| Penulis | Goh, Jin Yu; Md Yunos, Yusri; Mohamed Ali, Mohamed Sultan |
| Tahun | 2025 |
| Venue | Food and Bioprocess Technology |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [goh2025fresh.pdf](../pdf/goh2025fresh.pdf)
- DOI resmi: https://doi.org/10.1007/s11947-024-03483-0

## Gambaran Umum

Tinjauan ini membandingkan metode tak merusak untuk mengklasifikasikan kematangan tandan buah segar (TBS) kelapa sawit. Enam kelompok teknik dibahas: spektroskopi, penginderaan induktif, pencitraan termal, *light detection and ranging* (LiDAR), pencitraan hamburan balik sinar laser (*laser-light backscattering imaging*, LLBI), dan visi komputer. Pertanyaan yang diajukan penulis adalah teknik mana yang dapat mengklasifikasikan kematangan secara akurat dan seketika di lingkungan kebun yang tidak terstruktur, sebagai bagian dari pemanenan otomatis. Penulis menyebut tinjauannya sistematis ("rigorous systematic review"), tetapi teks lengkapnya tidak menyebut basis data, string pencarian, atau kriteria seleksi.

Tabel pembanding (Tabel 2) mengumpulkan akurasi atau R² yang dilaporkan kajian asal. Spektroskopi inframerah dekat (NIRS) mencapai R² 0,93 (Iqbal dkk. 2019), tetapi sampelnya dari satu perkebunan karena kalibrasi alat. Pencitraan hiperspektral mencapai 98,67% (Bensaeed dkk. 2014) dengan peralatan yang dipasang tetap. Spektroskopi Raman mencapai 90,90% sampai 100% pada empat kajian, sedangkan penginderaan induktif 100% (Sinambela dkk. 2020). Pencitraan termal mencapai 99,10% (Zolfagharnassab dkk. 2022). Gabungan LiDAR dan LLBI mencapai 85% (Mohd Ali dkk. 2020). Visi komputer berbasis warna berkisar dari 57% (Aslamiah dkk. 2019) sampai 98,70% (Robi dkk. 2022). Angka-angka ini berasal dari data dan protokol yang berbeda, sehingga tidak dapat dibandingkan langsung antarbaris.

Penulis menyimpulkan bahwa visi komputer paling cocok untuk penerapan di lapangan, dan LiDAR menjadi pendukung karena memberi struktur 3D dan lebih tahan terhadap perubahan cahaya. Fusi LiDAR dan visi komputer diusulkan karena dapat sekaligus melokalisasi dan memetakan tandan. Tantangan yang disebut adalah latar yang padat pelepah, oklusi antartandan, dan tandan yang tampak kecil bila dipotret dari jauh atau dari wahana udara (UAV). Penulis juga menganjurkan data sintetis untuk menambah ukuran dataset, dan RT-DETR untuk mendeteksi objek kecil.

Untuk korpus `main6`, kajian ini termasuk tinjauan terdahulu tentang sawit (R). Satuan analisisnya adalah satu tandan atau satu citra, bukan satu pohon. Pencacahan tandan dan identitas tandan di antara beberapa pandang pohon tidak dibahas.
