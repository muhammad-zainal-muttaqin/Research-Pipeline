# Oil palm fresh fruit bunches (FFB) growth determination system to support harvesting operation

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `kassim2012oil` |
| Judul asli | Oil palm fresh fruit bunches (FFB) growth determination system to support harvesting operation |
| Penulis | Kassim, Muhamad Saufi Mohd; Ismail, Wan Ishak Wan; Ramli, Abdul Rahman; Bejo, Siti Khairunniza |
| Tahun | 2012 |
| Venue | Journal of Food Agriculture and Environment |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [kassim2012oil.pdf](../pdf/kassim2012oil.pdf)

## Gambaran Umum

Penelitian ini bertujuan membangun sistem pemantauan pertumbuhan tandan buah segar (TBS) untuk menentukan tanggal panen tandan tertentu pada pohon tertentu serta memproyeksikan hasil TBS pohon itu sepanjang umur ekonominya. Latar belakangnya adalah penentuan kematangan oleh pemanen secara manual memakai warna tandan dan jumlah buah lepas di bawah pohon, yang menghasilkan penilaian tidak konsisten karena tugas panen bersifat melelahkan. Buah lepas yang tidak dikumpulkan menyebabkan kerugian; penulis mengutip laporan Sime Darby Plantation tentang potensi kehilangan pendapatan tahunan sekitar RM11 juta.

Tanaman yang diamati adalah kelapa sawit (*Elaeis guineensis* var. Tenera). Pengambilan citra dilakukan di kebun Universiti Putra Malaysia pada koordinat 2°58'47,97" LU dan 101°43'44,77" BT terhadap 60 pohon berusia lima tahun. Kamera Panasonic DMC-TZ10 yang dilengkapi penerima GPS dipakai dengan interval tiga hari dari pertengahan Mei hingga akhir Desember 2010. Setiap pohon, bunga betina, dan TBS diberi penanda dan identitas unik. Pada akhir pengamatan, 809 TBS pada berbagai tahap kematangan terpantau dan menghasilkan hampir 30.000 citra. Penulis mengutip hasil Razali dkk. yang mengorelasikan nilai *hue* citra TBS dengan kandungan minyak sebesar R² = 0,884 sebagai dasar penggunaan warna.

Mekanisme utama berupa perangkat lunak *Maturity Table*, yaitu tabel yang menyimpan informasi citra dan memuat persamaan untuk menghitung umur TBS dalam minggu sejak anthesis (minggu 0) serta tanggal panen. Citra dikelompokkan menjadi empat kelas: *Full Set* (dari anthesis sampai panen), *Non-Full Set* tipe A (dari setelah anthesis sampai panen), *Non-Full Set* tipe B (dari anthesis sampai sebelum panen), dan TBS tidak berkembang. Untuk tipe A, tahap kematangan ditentukan oleh pemanen lalu dibetulkan dengan membandingkan tampilan warna citra terhadap *Full Set* dari pohon yang sama; untuk tipe B, tahap kematangan dihitung langsung dari *Maturity Table*. Sebagai pemeriksaan, penulis memakai penggabungan *K-means* untuk mengekstrak citra TBS dan nilai *hue*. Pada contoh TBS 14A, citra 14A(32) mula-mula dinilai minggu ke-21, lalu dibetulkan menjadi minggu ke-23 setelah rentang *hue*-nya dicocokkan dengan *Full Set* 14F pada minggu ke-21 (kisaran *hue* 0,82–0,92).

Dari 809 TBS, jumlah per kelas berturut-turut 217 (24%), 351 (44%), 237 (31%), dan 4 (1%). Proyeksi hasil untuk Januari–September 2011 menurun dari 82 tandan pada Januari menjadi 5 tandan pada Juni 2011, sehingga *Maturity Table* menghasilkan proyeksi enam bulan ke depan. Peta hasil yang dibuat dengan perangkat lunak sistem informasi geografis menunjukkan pola penurunan dari utara ke selatan lahan. Jadwal panen Mei 2011 memuat 15 TBS beserta tanggal, koordinat GPS, identitas pohon, dan minggu kematangan; contohnya pohon P1 memiliki tahap kematangan optimum minggu ke-21, yang dihitung dari pembukaan bunga trilobus hingga minggu tersebut. Tahap optimum ditetapkan sebagai rata-rata umur TBS *Full Set* yang dipanen. Akurasi klasifikasi kematangan, metrik deteksi, dan split latih/uji tidak dinyatakan.

Penulis menyatakan beberapa batasan. Rincian pemrosesan citra untuk menentukan tahap kematangan tidak dilaporkan dalam makalah ini, dan keluaran pemrosesan itu masih harus diverifikasi terhadap hasil *Maturity Table*. Keandalan sistem bergantung pada ketersediaan data yang terus-menerus; karena perkembangan sampai kematangan memakan waktu sekitar enam bulan, sistem memerlukan data dalam satu siklus enam bulan. Beban pengumpulan data meningkat untuk perkebunan yang lebih luas, sehingga penulis mengarahkan pengembangan berikutnya pada pengumpulan data otomatis memakai peralatan robot. Fluktuasi hasil bulanan yang teramati berkemungkinan berkaitan dengan cuaca, tetapi penulis menyatakan faktor itu di luar ruang lingkup kajian.
