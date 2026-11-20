# ARIA: Augmented Reality and Artificial Intelligence enabled mobile application for Yield and grade prediction of tomato crops

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `balaji2024aria` |
| Judul asli | ARIA: Augmented Reality and Artificial Intelligence enabled mobile application for Yield and grade prediction of tomato crops |
| Penulis | B V, Balaji Prabhu; Shashank, R; Shreyas, B; Jois Narsipura, Omkar Subbaram |
| Tahun | 2024 |
| Venue | Procedia Computer Science |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [balaji2024aria.pdf](../pdf/balaji2024aria.pdf)
- DOI resmi: https://doi.org/10.1016/j.procs.2024.04.254

## Gambaran Umum

Makalah ARIA (Balaji dkk., 2024) membangun aplikasi seluler yang mencacah tomat dari satu citra kamera dan menilai kematangan serta kualitas tiap buah. Sistem memakai detektor *Faster R-CNN* dengan dua kelas dan dua pengklasifikasi ResNet-50 yang bekerja pada setiap buah yang terdeteksi. Hasil utamanya: akurasi uji deteksi 92%, pengklasifikasi kualitas 98,2%, dan pengklasifikasi kematangan 95,4% (rerata uji yang dilaporkan di bagian kesimpulan). Makalah ini mencacah dari citra tunggal, tanpa menggabungkan pengamatan dari beberapa pandang.

Penilaian tomat di lapangan dan di gudang sering dilakukan secara manual. Makalah ini mengusulkan aplikasi seluler dengan realitas tertambah tanpa penanda (*markerless augmented reality*) sebagai alat bantu pengguna. Kebutuhannya bersifat praktis: pengguna mengarahkan kamera ke sekumpulan tomat, lalu memperoleh jumlah buah dan penilaiannya.

Satu citra diproses dalam dua tahap. Detektor menemukan setiap tomat dan menentukan kotak pembatasnya. Dua pengklasifikasi kemudian memberi label kematangan dan kualitas pada setiap kotak. Jumlah tomat dihitung dari jumlah deteksi pada citra itu, bukan dari penggabungan dengan citra lain.

*Faster R-CNN* adalah detektor dua tahap: jaringan mengusulkan wilayah yang mungkin berisi objek, lalu wilayah itu diklasifikasi dan kotaknya diperhalus. Makalah ini melatihnya untuk dua kelas. Setiap kotak yang dihasilkan dipotong dan dikirim ke dua pengklasifikasi ResNet-50, satu untuk kematangan dan satu untuk kualitas. ResNet-50 adalah jaringan konvolusi dengan 50 lapisan yang menggunakan koneksi sisa (*residual connection*) agar pelatihan tetap stabil.

Data uji mencakup tomat dengan skala, pencahayaan, dan kontras yang beragam.

Hasil deteksi dilaporkan sebagai akurasi uji 92%. Angka klasifikasi di bagian hasil dan di bagian kesimpulan tidak cocok, dan makalah tidak menjelaskan sebabnya. Di bagian hasil, pengklasifikasi kematangan mencapai akurasi uji 97% dan pengklasifikasi kualitas 90%. Di bagian kesimpulan, rerata uji untuk kualitas 98,2% dan untuk kematangan 95,4%.

Makalah membandingkan kinerja dengan klaim "better, faster and more fruitful" tanpa tabel pembanding yang memuat mAP atau AP dari YOLOv5 pada data yang sama. Makalah tidak menyajikan angka pembanding untuk klaim tersebut.

Kelebihan makalah adalah sistem end-to-end yang dapat dijalankan di ponsel dan menghasilkan penilaian per buah. Dari sisi pencacahan, makalah tidak menangani buah yang sama dalam dua citra. Jika pengguna memotret pohon atau barisan dari beberapa sudut, jumlah yang dihasilkan dapat menghitung ganda. Makalah tidak menguji keadaan itu.

Secara konseptual, akurasi klasifikasi per buah tidak sama dengan akurasi jumlah total. Makalah tidak melaporkan galat hitungan terhadap jumlah tomat sebenarnya di lapangan.
