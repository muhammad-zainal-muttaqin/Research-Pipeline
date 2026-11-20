# Development of monitoring robot system for tomato fruits in hydroponic greenhouses

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `seo2021development` |
| Judul asli | Development of monitoring robot system for tomato fruits in hydroponic greenhouses |
| Penulis | Seo, Dasom; Cho, Byeong-Hyo; Kim, Kyoung-Chul |
| Tahun | 2021 |
| Venue | Agronomy |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [seo2021development.pdf](../pdf/seo2021development.pdf)
- DOI resmi: https://doi.org/10.3390/agronomy11112211

## Gambaran Umum

Penelitian ini mengembangkan sistem robot pemantau pertumbuhan generatif tomat secara real-time di rumah kaca hidroponik. Penulis menyatakan sebagian besar robot pertanian difokuskan pada pemanenan, sehingga aplikasi robot monitoring yang memakai pembelajaran mendalam masih sedikit. Tujuan sistem ini adalah mendeteksi buah tomat, mengklasifikasikan kematangan ke dalam enam tingkat, dan menghitung jumlah buah pada setiap tingkat tanpa hitungan ganda.

Tanaman yang dipakai adalah tomat (*Solanum lycopersicum* L.) di rumah kaca hidroponik di Korea. Model deteksi dilatih dengan himpunan data terbuka Tomato yang memuat 895 citra beranotasi kotak pembatas satu kelas dalam format PASCAL VOC, dibagi acak menjadi 805 citra latih dan 90 citra validasi. Faster R-CNN dengan tulang punggung ResNet-101 dilatih pada GPU RTX Titan menggunakan TensorFlow, laju pembelajaran 0,04, 10.000 epoch, optimizer momentum 0,9, dan penurunan laju pembelajaran cosine. Rugi yang diperoleh adalah 0,0149 untuk klasifikasi, 0,005 untuk deteksi, dan 0,0299 total. Perangkat lapangan memakai komputer industri Nuvo-8108 dengan GPU NVIDIA GTX 2080 ti dan webcam USB ELP 4K.

Mekanisme sistem terdiri atas tiga tahap. Faster R-CNN menghasilkan kotak pembatas buah; algoritme k-means dengan k = 2 memisahkan daerah buah dari latar karena kotak pembatas masih memuat latar. Citra diubah dari RGB ke HSV dan nilai hue rata-rata daerah buah dipakai untuk menetapkan enam tingkat kematangan menurut standar USDA, yaitu Green, Breakers, Turning, Pink, Light Red, dan Red. Penulis memilih hue karena nilai ini paling kebal terhadap perubahan cahaya, dengan simpangan baku 1,23 pada tiga tingkat kecerahan dan hubungan linear terhadap suhu terakumulasi dengan R² = 0,96. Penghitungan memakai pelacakan berbasis sentroid: titik pusat setiap kotak diberi identitas unik dan dicocokkan dengan jarak Euclidean minimum pada frame berikutnya; titik tanpa pasangan menerima identitas baru.

Uji lapangan dilakukan sepuluh kali pada area yang sama dengan 53 buah tomat sebagai acuan. Sistem mencapai akurasi deteksi 88,6% ketika buah yang tertutup penuh dan tidak terekam kamera ikut dihitung, serta 90,2% ketika buah tertutup dikecualikan. Rata-rata sepuluh prediksi adalah 54,4 buah; dua kali prediksi di bawah 53, empat kali tepat 53, dan lebih dari empat kali 54. Duplikat terjadi pada empat sampai enam objek. Waktu inferensi deteksi 0,16 s dan waktu pemrosesan total 0,18 s, setara hingga 5,5 frame per sementara robot bergerak 0,16 m/s. Standar kematangan dividasi dengan klasifikasi tiga pakar terhadap 20 buah; nilai a* yang dihitung dari citra berada dalam rentang tingkat kematangan yang ditetapkan pakar.

Penulis menyatakan standar kematangan di lapangan dapat berbeda menurut pakar dan kebun, sehingga diperlukan lebih banyak data klasifikasi dari pakar. Akurasi deteksi dan penghitungan perlu ditingkatkan karena masalah oklusi dan duplikasi belum terselesaikan. Data penelitian tidak dipublikasikan karena alasan privasi, melainkan tersedia atas permintaan penulis korespondensi.
