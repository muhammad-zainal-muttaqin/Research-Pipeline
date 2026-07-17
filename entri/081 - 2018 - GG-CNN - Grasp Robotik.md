# 081 - Closing the Loop for Robotic Grasping: A Real-Time, Generative Grasp Synthesis Approach

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `morrison2018ggcnn` |
| Judul asli | Closing the Loop for Robotic Grasping: A Real-Time, Generative Grasp Synthesis Approach |
| Penulis | Douglas Morrison, Peter Corke, Jürgen Leitner |
| Tahun | 2018 |
| Venue | Robotics: Science and Systems (RSS 2018) |
| Tema | Grasp Robotik |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/1804.05172
- **Google Scholar:** https://scholar.google.com/scholar?q=Closing%20the%20Loop%20for%20Robotic%20Grasping%3A%20A%20Real-Time%2C%20Generative%20Grasp%20Synthesis%20Approach
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Closing%20the%20Loop%20for%20Robotic%20Grasping%3A%20A%20Real-Time%2C%20Generative%20Grasp%20Synthesis%20Approach&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan GG-CNN (*Generative Grasping Convolutional Neural Network*), sebuah jaringan konvolusi yang memetakan citra kedalaman menjadi prediksi cengkeraman (*grasp*) untuk setiap piksel dalam satu lintasan jaringan. Tugas cengkeraman robotik adalah menentukan posisi dan orientasi penjepit (*gripper*) dua jari agar dapat mengangkat objek secara stabil. GG-CNN menyelesaikan tugas ini bukan dengan menilai ribuan kandidat cengkeraman satu per satu, melainkan dengan langsung menghasilkan tiga peta beresolusi sama dengan citra masukan: peta mutu cengkeraman, peta sudut, dan peta lebar bukaan penjepit.

Karena jaringannya sangat kecil — hanya 62.420 parameter, beberapa orde lebih kecil daripada jaringan pembanding yang berukuran puluhan juta parameter — inferensinya cukup ringan untuk berjalan berulang-ulang selama lengan robot bergerak. Waktu komputasi jaringan sekitar 6 milidetik dan seluruh alur pemrosesan sekitar 19 milidetik, sehingga cengkeraman dapat diperbarui sampai 50 kali per detik. Kecepatan inilah yang memungkinkan kontrol *closed-loop*: prediksi cengkeraman dihitung ulang terus-menerus dan lengan robot mengoreksi sasarannya secara *real-time*, sehingga tetap berhasil ketika objek digeser saat percobaan berlangsung. Pada objek rumah tangga yang dipindahkan selama percobaan, sistem mencapai keberhasilan 88%, dan 81% pada objek yang tersusun berantakan (*clutter*) yang dinamis.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum makalah ini, pendekatan cengkeraman berbasis pembelajaran mendalam yang dominan bekerja dengan menyampel kandidat. Metode Lenz dkk. (bab 080) menghasilkan banyak kotak cengkeraman kandidat, lalu mengevaluasi setiap kandidat dengan jaringan pengklasifikasi untuk memilih yang terbaik. Pendekatan ini memiliki dua kelemahan yang saling berkaitan. Pertama, biaya komputasinya tinggi: mengevaluasi banyak kandidat satu per satu memakan waktu dari ratusan milidetik hingga beberapa detik per citra. Kedua, karena lambat, cengkeraman hanya dapat dihitung sekali di awal, lalu dieksekusi secara *open-loop* — yaitu lengan robot menjalankan rencana yang dihitung di muka tanpa mengoreksinya di tengah jalan.

Eksekusi *open-loop* mengandaikan tiga hal yang sering tidak terpenuhi di dunia nyata: kalibrasi kamera-ke-robot yang presisi, kendali lengan yang akurat, dan objek yang diam sempurna. Bila objek bergeser, tersenggol, atau posisi awalnya salah diukur, cengkeraman yang sudah direncanakan menjadi meleset dan tidak ada mekanisme untuk memperbaikinya. Selain itu, banyak metode terdahulu mendiskretkan ruang cengkeraman menjadi kisi posisi dan sudut yang terbatas, sehingga membuang informasi kontinu tentang di mana cengkeraman terbaik sesungguhnya berada. Makalah ini menargetkan ketiga kelemahan tersebut sekaligus: kecepatan, kemampuan koreksi, dan representasi yang kontinu.

## Ide Utama

Gagasan inti GG-CNN adalah memperlakukan pendeteksian cengkeraman seperti pekerjaan segmentasi per-piksel, bukan pemilihan kandidat. Alih-alih bertanya "manakah dari sekian kandidat yang terbaik", jaringan langsung menjawab, untuk setiap piksel citra kedalaman, "seberapa baik cengkeraman yang berpusat di sini, pada sudut berapa, dan selebar apa". Keluaran jaringan berupa peta yang setiap pikselnya memuat jawaban itu; cengkeraman terbaik dipilih belakangan cukup dengan mencari piksel bernilai mutu tertinggi.

Karena satu lintasan jaringan konvolusi penuh (*fully convolutional*, yaitu jaringan tanpa lapis terhubung penuh sehingga keluarannya berbentuk peta spasial) menghasilkan seluruh peta sekaligus, biaya komputasi tidak lagi bergantung pada jumlah kandidat. Ini membuat prediksi cukup cepat untuk diulang di setiap langkah gerak lengan. Dengan begitu, cengkeraman berubah dari rencana statis menjadi sasaran yang diperbarui terus-menerus — inti dari "menutup gelung" (*closing the loop*) pada judul makalah.

## Cara Kerja Langkah demi Langkah

### Representasi Cengkeraman

Sebuah cengkeraman di ruang nyata dinyatakan sebagai g = (p, φ, w, q): p = (x, y, z) adalah posisi pusat penjepit, φ adalah rotasi penjepit terhadap sumbu tegak, w adalah lebar bukaan yang diperlukan, dan q adalah skor mutu antara 0 dan 1 yang menyatakan perkiraan peluang keberhasilan. Di ruang citra, cengkeraman yang sama dinyatakan sebagai g̃ = (s, φ̃, w̃, q), dengan s = (u, v) titik pusat dalam koordinat piksel, φ̃ sudut dalam kerangka kamera, dan w̃ lebar dalam satuan piksel (rentang 0–150). Konversi dari ruang citra ke ruang nyata dilakukan dengan transformasi geometri kamera yang sudah diketahui, sehingga jaringan cukup bekerja sepenuhnya dalam ruang citra.

### Peta Cengkeraman sebagai Keluaran

Untuk seluruh citra, GG-CNN memprediksi peta cengkeraman G = (Q, Φ, W), yaitu tiga peta beresolusi sama dengan citra masukan. Q adalah peta mutu: nilai tiap piksel antara 0 dan 1 menyatakan sebaik apa cengkeraman yang berpusat di piksel itu. Φ adalah peta sudut dengan nilai pada rentang [−π/2, π/2]. W adalah peta lebar dalam piksel (0–150), yang kemudian diskalakan ke lebar fisik penjepit.

Sudut cengkeraman tidak diprediksi langsung sebagai satu angka, karena sudut memiliki diskontinuitas: cengkeraman antipodal (dua jari berlawanan) bersifat simetris, sehingga sudut −π/2 dan +π/2 sebenarnya setara, dan regresi angka tunggal akan tersendat di titik lompatan itu. Solusinya, jaringan memprediksi dua komponen, cos 2φ dan sin 2φ. Kelipatan dua membuat rentang [−π/2, π/2] terpetakan penuh satu putaran, dan sudut dipulihkan dengan φ = ½ arctan(sin 2φ / cos 2φ). Cara ini menghilangkan diskontinuitas tanpa mengubah tugasnya menjadi klasifikasi sudut diskret.

Diagram berikut merangkum alur dari citra kedalaman ke satu cengkeraman terpilih.

```
citra kedalaman           GG-CNN            tiga peta keluaran (300 x 300)
   300 x 300      ->   62.420 parameter  ->  ┌─ Q  : mutu cengkeraman (0..1)
  (satu kanal)         fully-conv, ~6 ms     ├─ Phi: sudut, via cos2phi & sin2phi
                                             └─ W  : lebar bukaan (0..150 piksel)
                                                       │
                          argmax pada Q  <────────────┘
                                │
                                ▼
                cengkeraman terpilih g~ = (s, phi~, w~, q)
```

### Arsitektur dan Pelatihan

Jaringannya kecil dan sepenuhnya konvolusional, berjumlah 62.420 parameter — dibandingkan puluhan juta parameter pada jaringan pembanding. Masukannya citra kedalaman 300×300 piksel satu kanal; keluarannya empat peta (Q, cos 2φ, sin 2φ, W) beresolusi sama.

Data pelatihan berasal dari *Cornell Grasping Dataset*, yaitu himpunan 885 citra RGB-D objek nyata yang dilengkapi 5.110 anotasi cengkeraman positif. Data ini diperbanyak (*augmentasi*) menjadi 8.840 citra melalui pemotongan, penyekalaan, dan rotasi acak, sehingga secara efektif memberi puluhan ribu contoh cengkeraman. Anotasi kotak cengkeraman diubah menjadi label per-piksel: piksel di sekitar pusat setiap cengkeraman positif diberi mutu 1, dan nilai sudut serta lebar cengkeraman itu ditanamkan pada peta Φ dan W di wilayah tersebut. Jaringan dilatih untuk mereproduksi peta-peta ini dengan galat kuadrat.

### Kontrol Closed-Loop

Saat eksekusi, kamera *Intel RealSense SR300* dipasang di pergelangan lengan *Kinova Mico* 6 derajat kebebasan yang memakai penjepit dua jari KG-2. Selama lengan mendekati objek, GG-CNN dijalankan berulang pada aliran citra kedalaman. Pada setiap iterasi, piksel bermutu tertinggi pada peta Q menjadi sasaran cengkeraman baru, dan lengan mengoreksi lintasannya ke sasaran itu. Karena satu siklus prediksi hanya sekitar 19 milidetik (termasuk pra-pemrosesan citra dan pemilihan cengkeraman), pembaruan dapat terjadi sampai 50 kali per detik — jauh lebih cepat daripada gerak objek yang lazim, sehingga sasaran selalu mengikuti posisi objek terkini.

## Eksperimen dan Hasil

Pengujian dilakukan pada robot fisik, bukan hanya pada dataset. Objek uji terdiri atas dua himpunan: 8 objek "adversarial" hasil cetak 3D dengan geometri sulit, dan sekumpulan objek rumah tangga dari benda sehari-hari. Metrik utamanya adalah *success rate*, yaitu persentase percobaan cengkeraman yang berhasil mengangkat objek.

Pada cengkeraman objek statis (*open-loop*, objek diam), GG-CNN mencapai 84% pada objek adversarial dan 92% pada objek rumah tangga. Angka ini setara atau lebih baik daripada metode terdahulu yang berukuran puluhan juta parameter dan memerlukan waktu 0,2 hingga 13,5 detik per cengkeraman, padahal GG-CNN hanya butuh sekitar 19 milidetik. Perbandingan ini menunjukkan bahwa jaringan kecil per-piksel tidak mengorbankan akurasi demi kecepatan.

Keunggulan sebenarnya muncul pada kondisi dinamis. Ketika objek digeser tangan manusia selama lengan mendekat, mode *closed-loop* mempertahankan keberhasilan 83% pada objek adversarial dan 88% pada objek rumah tangga — kondisi yang akan menggagalkan eksekusi *open-loop* karena rencana awal menjadi usang. Pada tumpukan objek berantakan yang juga diganggu selama percobaan, keberhasilannya 81%. Interpretasinya: manfaat koreksi *real-time* paling terasa persis pada situasi yang selama ini menjadi titik lemah metode sampling lambat, yakni objek yang bergerak dan penempatan yang tidak presisi.

## Kelebihan dan Keterbatasan

Kelebihan utama GG-CNN adalah ukurannya yang ringkas dan kecepatannya, yang secara langsung membuka kontrol *closed-loop* pada perangkat robot tanpa komputasi berat. Prediksi per-piksel yang kontinu menghindari diskretisasi ruang cengkeraman, dan pelatihan dari dataset publik berukuran kecil membuktikan bahwa jaringan mungil pun cukup untuk generalisasi ke objek tak dikenal.

Keterbatasannya berakar pada representasinya. GG-CNN memprediksi cengkeraman planar — posisi pada bidang citra, sudut satu putaran, dan lebar — bukan cengkeraman 6 derajat kebebasan penuh di ruang tiga dimensi, sehingga cengkeraman dari arah menyamping atau miring tidak terwakili. Dari sisi rekayasa, kinerjanya bergantung pada mutu citra kedalaman; permukaan yang memantul atau menyerap sinar inframerah dapat menghasilkan kedalaman yang buruk dan menurunkan prediksi. Secara konseptual, karena masukannya hanya kedalaman tanpa warna, isyarat visual seperti tekstur dan batas objek yang tampak pada kanal RGB tidak dimanfaatkan — celah yang kelak diisi metode fusi warna-kedalaman.

## Kaitan dengan Bab Lain

Bab ini berdiri sebagai jawaban langsung atas keterbatasan pendekatan sampling yang dibahas pada [080 - Deep Learning Robotic Grasps (Lenz dkk.)](./080%20-%202015%20-%20Deep%20Learning%20Robotic%20Grasps%20%28Lenz%20dkk.%29%20-%20Grasp%20Robotik.md): dari mengevaluasi banyak kandidat secara lambat menjadi menghasilkan peta cengkeraman sekali jalan. Representasi cengkeraman per-piksel yang diperkenalkan di sini diwarisi dan diperluas oleh [082 - GR-ConvNet](./082%20-%202020%20-%20GR-ConvNet%20-%20Grasp%20Robotik.md), yang menambahkan kanal warna dan jaringan lebih dalam, serta lanjutannya [083 - GR-ConvNet v2](./083%20-%202022%20-%20GR-ConvNet%20v2%20-%20Grasp%20Robotik.md). Dataset *Cornell* yang dipakai di sini kelak dilengkapi oleh dataset sintetis berskala besar pada [086 - Jacquard Dataset](./086%20-%202018%20-%20Jacquard%20Dataset%20-%20Grasp%20Robotik.md), sedangkan lompatan ke cengkeraman 6 derajat kebebasan yang menjadi keterbatasan bab ini diangkat pada [084 - GraspNet-1Billion](./084%20-%202020%20-%20GraspNet-1Billion%20-%20Grasp%20Robotik.md).

## Poin untuk Sitasi

Kutip dengan kunci `morrison2018ggcnn`. Ringkasan yang aman dikutip: "GG-CNN memprediksi peta cengkeraman per-piksel (mutu, sudut, lebar) dari citra kedalaman dalam satu lintasan jaringan berukuran 62.420 parameter dengan inferensi sekitar 19 milidetik, memungkinkan cengkeraman *closed-loop* *real-time* yang tetap berhasil pada objek yang bergerak."

Angka yang berasal langsung dari naskah dan aman dirujuk: 62.420 parameter, masukan 300×300, waktu jaringan ±6 ms dan alur penuh ±19 ms, laju sampai 50 Hz, serta *Cornell Grasping Dataset* (885 citra, 5.110 anotasi, diaugmentasi menjadi 8.840 citra). Angka keberhasilan perlu dicermati karena bergantung kondisi uji: statis *open-loop* 84% (adversarial) dan 92% (rumah tangga); dinamis *closed-loop* 83% (adversarial) dan 88% (rumah tangga); *clutter* dinamis 81%. Pasangan angka statis 84%/92% dan rincian jumlah percobaan per objek sebaiknya diverifikasi ulang ke tabel naskah asli sebelum sitasi formal, karena abstrak menonjolkan 83%/88%/81% sementara tabel hasil melaporkan angka statis yang terpisah.
