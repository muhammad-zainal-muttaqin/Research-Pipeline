# An automatic and rapid system for grading palm bunch using a Kinect camera

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pamornnak2017automatic` |
| Judul asli | An automatic and rapid system for grading palm bunch using a Kinect camera |
| Penulis | Pamornnak, Burawich; Limsiroratana, Somchai; Khaorapapong, Thanate; Chongcheawchamnan, Mitchai; Ruckelshausen, Arno |
| Tahun | 2017 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [pamornnak2017automatic.pdf](../pdf/pamornnak2017automatic.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2017.10.020

## Gambaran Umum

Pamornnak dkk. (2017) membangun sistem penilaian mutu tandan buah segar (TBS) kelapa sawit di jalur konveyor. Sistem memakai satu kamera Kinect v2 yang menghasilkan citra RGB, inframerah dekat, dan *point cloud* (kumpulan titik tiga dimensi dari data kedalaman). Dari ketiga citra itu diambil tiga fitur: rona rata-rata (*average hue*) dari RGB, indeks volume relatif dari *point cloud*, dan intensitas inframerah rata-rata. Ketiga fitur dipakai untuk mengelompokkan tandan ke dalam tiga kelas kandungan minyak: L-Grade (kurang dari 4 kg), M-Grade (4–8 kg), dan H-Grade (lebih dari 8 kg). Hasil utama adalah akurasi 83% pada 200 tandan uji, dengan kecepatan sekitar 10 tandan per menit.

Tugas yang dikerjakan kajian ini adalah penilaian mutu per tandan, bukan pencacahan buah. Kajian tidak menghitung jumlah buah, tidak memakai deteksi buah per pandang, dan tidak membandingkan model deteksi. Penggunaan depth di sini berfungsi sebagai pengukur volume tandan, bukan sebagai kanal masukan detektor.

Kandungan minyak TBS biasanya diukur dengan metode Soxhlet, yaitu ekstraksi pelarut yang merusak sampel. Metode ini lambat dan tidak dapat dipakai pada setiap tandan di jalur produksi. Penulis menyebut bahwa penimbangan tandan di jalur konveyor rumit, sedangkan penimbangan sebelum tandan masuk jalur mengganggu alur kerja. Karena itu kajian mengusulkan volume sebagai pengganti berat. Kajian ini juga mengutip penelitian sebelumnya yang menghubungkan rona buah dengan tingkat kematangan dan kandungan minyak (Abdullah dkk., 2002; Makky dan Soni, 2014), tetapi hubungan itu tidak diuji sebagai satu sistem di jalur konveyor.

Sistem menghitung volume relatif tandan dengan skema integrasi sederhana, yang disebut *Simple Volume Integration Scheme* (SVIS). Skema ini menjumlahkan sel satuan volume dari *point cloud* setengah tandan, dengan asumsi tandan simetris terhadap bidang tengah. Volume satu sel satuan adalah 0,005 m³. Nilai volume kemudian dikombinasikan dengan rona dan intensitas inframerah ke dalam tiga fungsi kuadrat, yang rata-ratanya menjadi fungsi klasifikasi (*quality processing function*).

Konveyor bergerak dengan kecepatan 0,125 m/s. Pusat massa citra topeng (*mask*) dihitung terus-menerus, dan konveyor berhenti ketika pusat massa berada di garis tengah zona berhenti yang lebarnya 5% dari lebar bingkai. Setelah itu sistem mengambil citra RGB dan inframerah dalam waktu 5 detik. Citra topeng dibuat dari citra inframerah dengan ambang 10%, lalu dibersihkan dengan erosi dan dilasi.

Kalibrasi memakai papan catur 10×7 kotak berukuran 24 mm dengan 48 pasangan sudut. Jarak sensor-lensa rata-rata adalah 385 piksel pada jarak kerja 1 m.

Untuk menghubungkan volume dan berat, 90 tandan contoh dari tiga kelompok ukuran dipakai. Hubungan antara indeks volume dan berat menghasilkan R² = 0,911. Untuk klasifikasi, 200 tandan lain dipakai sebagai data uji. Kandungan minyak tiap tandan diukur dengan Soxhlet, lalu tiga fungsi regresi nonlinear dicocokkan. Koefisien determinasi (R²) tiap fungsi adalah 0,807 (volume dan rona), 0,522 (rona dan inframerah), dan 0,543 (volume dan inframerah). Pada fungsi pertama, koefisien volume relatif (a13) bernilai 1,937, sehingga tandan yang lebih besar menghasilkan lebih banyak minyak.

Pengujian volume memakai tiga benda dengan volume diketahui. Kinect memberi galat volume keseluruhan 2,36%, sedangkan ifm-O3D201 memberi 11,10% dan Nippon FX8 memberi 10,67%. Penulis menyebut bahwa kedua kamera pembanding beresolusi sekitar 36 kali lebih rendah dibanding Kinect. Pada bagian kesimpulan, galat 2,49% dilaporkan untuk benda 9.200 cm³. Waktu proses SVIS adalah 23 ms.

Untuk klasifikasi, 200 tandan uji menghasilkan akurasi keseluruhan 83%. Akurasi per kelas adalah 81% (L), 85% (M), dan 83% (H). Kesalahan terbesar terjadi pada tandan L yang diklasifikasikan sebagai M (19%) dan tandan H yang diklasifikasikan sebagai M (17%). Kesalahan batas M ke L dan M ke H masing-masing 11% dan 5%.

Kelebihan utama adalah satu kamera murah menghasilkan volume dan fitur citra sekaligus, pada kecepatan yang disebut cukup untuk 10 tandan per menit. Sistem ini juga menghitung tiga kelas dari fitur yang dapat diukur di jalur, sehingga tidak bergantung pada penimbangan.

Dari sisi evaluasi, beberapa batas perlu dicatat. Hasil klasifikasi berasal dari satu sesi uji 200 tandan di lingkungan cahaya terkendali. Kajian tidak melaporkan validasi silang atau uji pada tandan dari kebun lain. Label kelas berasal dari Soxhlet pada sampel yang sama, sehingga kesalahan pengukuran Soxhlet ikut memengaruhi label. Kajian juga tidak mengukur buah per tandan, sehingga kontribusinya untuk pencacahan buah terbatas. Secara konseptual, kajian ini menunjukkan volume dari depth dapat mengganti penimbangan, tetapi tidak menguji apakah depth menolong deteksi buah.
