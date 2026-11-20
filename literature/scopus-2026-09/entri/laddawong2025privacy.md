# Privacy-Preserving Federated Learning in Oil Palm Industry for Fresh Fruit Bunch Ripeness Grading

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `laddawong2025privacy` |
| Judul asli | Privacy-Preserving Federated Learning in Oil Palm Industry for Fresh Fruit Bunch Ripeness Grading |
| Penulis | Laddawong, Patchanee; Pianroj, Yutthapong; Chotikawanid, Piyanart; Punvichai, Teerasak; Jumrat, Saysunee; Muangprathub, Jirapond |
| Tahun | 2025 |
| Venue | Journal of Advances in Information Technology |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [laddawong2025privacy.pdf](../pdf/laddawong2025privacy.pdf)
- DOI resmi: https://doi.org/10.12720/jait.16.3.434-446

## Gambaran Umum

Penelitian ini bertujuan membangun model klasifikasi tingkat kematangan tandan buah segar (TBS) kelapa sawit yang menjaga kerahasiaan data antarpabrik. Latar belakangnya adalah kapasitas pabrik minyak sawit di Thailand yang hanya terpakai 43%, sementara kesalahan penilaian kematangan diduga menurunkan efisiensi ekstraksi minyak 10–20%. Penilaian kematangan oleh petugas pabrik bersifat visual dan rentan terhadap keterbatasan tenaga, waktu, serta subjektivitas. Penulis mengusulkan metode Privacy-Preserving Federated Learning with Federated Averaging (PP-FedAvg) untuk memprediksi tingkat kematangan dan hasil minyak tanpa mengirim data mentah ke server pusat.

Data berupa 5.209 citra TBS dari satu pabrik di Provinsi Surat Thani, Thailand, terdiri atas 2.571 citra tandan tunggal dan 2.638 citra tandan ganda. Empat kelas kematangan adalah raw (1.943 citra), semi-raw (1.107), semi-ripe (1.062), dan ripe (1.097), dengan empat kultivar, yaitu Searad 'Millennium', Spring Black, Surat Thani 2, dan Surat Thani 7. Citra diambil di dalam dan di luar ruangan dengan variasi pencahayaan serta pengaturan kamera. Pembagian data memakai stratified sampling 85% untuk latih dan 15% untuk uji, dengan 753 citra pengujian. Pra-pemrosesan meliputi pengubahan ukuran menjadi 224×224 piksel, peningkatan kontras, normalisasi nilai piksel ke rentang 0–1, serta augmentasi rotasi, pembalikan, dan zoom.

Mekanisme yang dipelajari model adalah klasifikasi tingkat kematangan citra, bukan penghitungan individu buah. Penulis membandingkan tiga pendekatan: CNN dengan pelatihan terpusat, FedAvg yang hanya mengirim bobot model ke server, dan PP-FedAvg. Pada PP-FedAvg, pembaruan model dienkripsi di sisi klien dengan kunci yang ditentukan, dikirim melalui HTTPS dengan token akses, lalu didekripsi dan diagregasi di server dengan rata-rata terbobot berdasarkan jumlah data tiap klien. Komunikasi real-time memakai Socket.io dan WebRTC. Model terpilih diterapkan pada aplikasi web yang menampilkan persentase tiap tingkat kematangan, waktu pemrosesan, dan perkiraan harga minyak.

Tabel IV melaporkan akurasi PP-FedAvg 97,9% dengan loss 0,0589, ROC 0,9, dan AUROC 0,9. FedAvg mencatat akurasi 98,7% dengan loss 0,0526, sedangkan CNN mencatat akurasi 86,58% dengan ROC dan AUROC 1,0. Abstrak dan simpulan menyebut akurasi 92,5%; nilai itu sesuai dengan hasil PP-FedAvg pada lokasi umum di Tabel V, sedangkan nilai pada empat lokasi industri berkisar 93,5–96,7%. Metrik dihitung pada cawat uji 15% dari 5.209 citra. Waktu pelatihan PP-FedAvg 8,51 menit, lebih lama daripada FedAvg (8,00 menit) dan CNN (5,07 menit).

Penulis menyatakan beberapa batasan. Generalisasi ke wilayah lain dengan kondisi lingkungan, spesies, dan praktik budidaya berbeda belum diperiksa. Set data diduga mengandung bias berupa ketidakseimbangan representasi tingkat kematangan dan variasi kualitas citra. Prediksi hasil minyak tidak memasukkan unsur hara, faktor lingkungan, dan pengukuran fisiologis. Pada penerapan, muncul latensi saat memproses data real-time dengan banyak klien serta kendala kompatibilitas antarserver, yang diatasi dengan pembagian beban kerja, pemrosesan asinkron, dan kontainerisasi Docker.
