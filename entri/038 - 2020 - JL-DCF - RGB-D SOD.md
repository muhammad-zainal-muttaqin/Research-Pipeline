# 038 - JL-DCF: Joint Learning and Densely-Cooperative Fusion Framework for RGB-D Salient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `fu2020jldcf` |
| Judul asli | JL-DCF: Joint Learning and Densely-Cooperative Fusion Framework for RGB-D Salient Object Detection |
| Penulis | Keren Fu, Deng-Ping Fan, Ge-Peng Ji, Qijun Zhao |
| Tahun | 2020 |
| Venue | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2020), hal. 3052–3062 |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2004.08515
- **CVPR Open Access (versi penerbit):** https://openaccess.thecvf.com/content_CVPR_2020/html/Fu_JL-DCF_Joint_Learning_and_Densely-Cooperative_Fusion_Framework_for_RGB-D_Salient_CVPR_2020_paper.html
- **Kode sumber resmi:** https://github.com/kerenfu/JLDCF
- **Google Scholar:** https://scholar.google.com/scholar?q=JL-DCF%3A%20Joint%20Learning%20and%20Densely-Cooperative%20Fusion%20Framework%20for%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=JL-DCF%3A%20Joint%20Learning%20and%20Densely-Cooperative%20Fusion%20Framework%20for%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan JL-DCF, kerangka untuk deteksi objek menonjol (*salient object detection*, SOD) dari masukan RGB-D, yaitu pasangan citra berwarna dan peta kedalaman (citra yang setiap pikselnya menyatakan jarak permukaan ke kamera). Tugas SOD adalah menghasilkan *peta saliency*: citra keabuan seukuran masukan yang menandai piksel-piksel milik objek paling menonjol dalam pemandangan. Kerangka ini terdiri atas dua komponen. Komponen pertama, *joint learning* (JL), mengekstrak fitur RGB dan kedalaman memakai satu jaringan konvolusi yang sama dengan bobot yang dibagi penuh, alih-alih dua jaringan terpisah. Komponen kedua, *densely-cooperative fusion* (DCF), menggabungkan fitur kedua modalitas pada enam tingkat resolusi dengan operasi penjumlahan dan perkalian elemen-demi-elemen, lalu menyusun peta akhir secara kasar-ke-halus.

Hasil utamanya: pada enam *benchmark* RGB-D SOD, JL-DCF mengungguli model terbaik sebelumnya, D3Net, dengan rata-rata S-measure (metrik kemiripan struktur peta saliency) lebih tinggi sekitar 1,9%. Kerangka ini juga menunjukkan bahwa berbagi bobot lintas modalitas bukan hanya hemat parameter, tetapi justru membuat pelatihan lebih stabil dibandingkan dua cabang terpisah.

## Latar Belakang: Masalah yang Ingin Dipecahkan

SOD berbasis RGB saja sering gagal ketika objek menonjol memiliki warna dan tekstur yang mirip dengan latar belakang. Peta kedalaman dari kamera seperti Kinect atau RealSense menyediakan petunjuk geometri yang tidak bergantung pada penampilan, sehingga SOD RGB-D menjadi pilihan. Masalahnya adalah cara menggabungkan dua modalitas yang sifat statistiknya berbeda.

Strategi fusi yang ada terbagi tiga. *Early fusion* menggabungkan masukan di awal, misalnya menyambung RGB dan kedalaman menjadi citra empat kanal; strategi ini murah tetapi mencampur data mentah yang berbeda domain sebelum fitur terbentuk. *Late fusion* menggabungkan keluaran akhir tiap modalitas; interaksi lintas modalitas terjadi terlalu akhir. *Middle fusion* menggabungkan fitur kedua modalitas di tingkat fitur, seperti pada PCF, TANet, dan MMCI, tetapi memakai dua cabang CNN independen sehingga jumlah parameter hampir dua kali lipat dan pelatihannya menuntut rancangan hati-hati. Padahal data latih RGB-D berkualitas jumlahnya terbatas; akibatnya model besar rawan terjebak pada solusi suboptimal. Motivasi JL-DCF adalah pengamatan bahwa RGB dan kedalaman, meskipun berbeda domain, berbagi petunjuk saliency yang sama, misalnya kontras objek-latar yang kuat dan ketertutupan kontur objek. Kesamaan ini membuka peluang satu jaringan tunggal mempelajari representasi keduanya sekaligus.

## Ide Utama

Gagasan inti JL-DCF sederhana: perlakukan peta kedalaman sebagai citra biasa, lalu masukkan RGB dan kedalaman ke dalam satu jaringan yang sama. Karena bobot jaringan dibagi untuk kedua modalitas, informasi dari keduanya melebur ke dalam parameter yang sama melalui propagasi balik — inilah makna *joint learning*. Fusi eksplisit baru terjadi sesudahnya: fitur hierarkis dari kedua modalitas digabungkan pada setiap tingkat resolusi dengan operasi kooperatif (penjumlahan plus perkalian), dan sebuah *decoder* dengan koneksi rapat merakit fitur gabungan dari resolusi kasar ke halus hingga diperoleh peta saliency akhir. Dengan demikian, masukan kerangka adalah sepasang citra RGB dan peta kedalaman; keluarannya satu peta saliency seukuran masukan; dan seluruh sistem dilatih *end-to-end* (dari masukan ke keluaran dalam satu proses optimasi).

## Cara Kerja Langkah demi Langkah

### Pembentukan Batch Dua Modalitas

Masukan diubah ke ukuran tetap 320×320 piksel. Peta kedalaman dinormalisasi ke rentang [0, 255], lalu kanal tunggalnya direplikasi menjadi tiga kanal, sehingga secara bentuk ia setara citra RGB. Kedua citra kemudian digabungkan pada **dimensi batch**, bukan dimensi kanal: citra RGB 320×320×3 dan kedalaman 320×320×3 membentuk satu batch 320×320×3×2. Skema ini berbeda dari *early fusion* yang menyambung keduanya menjadi 320×320×6. Penggabungan pada dimensi batch memungkinkan satu backbone memproses kedua modalitas secara paralel dengan bobot yang sama persis.

### Backbone Siamese Berbagi Bobot

Ekstraksi fitur dilakukan oleh *backbone* (jaringan ekstraktor fitur utama) dalam konfigurasi *siamese*: satu arsitektur beserta bobotnya dipakai untuk dua masukan sekaligus. Makalah mengimplementasikan dua varian, VGG-16 dan ResNet-101, dua arsitektur CNN klasik untuk pengenalan citra. Backbone dibagi enam hierarki dengan ukuran spasial keluaran berturut-turut 320, 160, 80, 40, 20, dan 20 piksel. Agar peta terkasar tetap 20×20 tanpa kehilangan *receptive field* (wilayah masukan yang dilihat satu neuron), langkah (*stride*) lapisan pool5 diubah menjadi 1 dan dua lapisan tambahan memakai konvolusi terdilatasi (konvolusi dengan celah antar-titik penapisan, di sini laju 2) sehingga cakupan pandang tetap luas. Fitur dari tiap hierarki diambil sebagai *side output* (keluaran samping dari lapisan tengah), mengikuti praktik pada model SOD DSS.

### Kompresi Fitur dan Supervisi Global

Keluaran samping keenam tingkat memiliki jumlah kanal yang berbeda-beda. Modul CP (*compression*) berupa konvolusi 3×3 dengan k = 64 *filter* memampatkan semuanya ke 64 kanal agar seragam dan hemat komputasi. Pada tingkat terkasar (CP6), sebuah konvolusi 1×1 menghasilkan dua prediksi kasar — satu untuk bagian RGB, satu untuk bagian kedalaman — yang keduanya diawasi langsung oleh *ground truth* (peta kebenaran) yang diperkecil. Teknik pengawasan pada lapisan tengah ini disebut *deep supervision*; fungsi loss-nya dinamai loss pemandu global Lg. Tujuannya ganda: memberi lokalisasi kasar untuk pemrosesan selanjutnya, dan memaksa backbone belajar menemukan objek dari kedua modalitas secara bersamaan.

### Fusi Kooperatif Lintas Modal

Setiap pasangan fitur RGB dan kedalaman pada tingkat yang sama digabung oleh modul CM (*cross-modal fusion*). Bila Xrgb dan Xd adalah fitur 64 kanal dari kedua modalitas, keluaran CM adalah:

CM(Xrgb, Xd) = Xrgb ⊕ Xd ⊕ (Xrgb ⊗ Xd)

dengan ⊕ penjumlahan dan ⊗ perkalian elemen-demi-elemen; hasilnya tetap 64 kanal. Penjumlahan menangkap informasi yang saling melengkapi (fitur yang kuat di salah satu modalitas tetap bertahan), sedangkan perkalian menonjolkan kesamaan (respons hanya besar bila kedua modalitas sepakat). Penulis menguji alternatif berupa penyambungan kanal (menghasilkan 128 kanal) dan menemukan kinerjanya menurun: penyambungan membuat jaringan cenderung hanya memakai informasi RGB dan mengabaikan kedalaman, karena secara praktis ia melakukan seleksi fitur, bukan fusi eksplisit.

### Decoder Berkoneksi Rapat

Fitur hasil fusi dari keenam tingkat dirakit oleh modul FA (*feature aggregation*). Berbeda dengan decoder gaya U-Net (arsitektur penyandian-penguraian yang hanya menghubungkan tingkat yang bersebelahan), setiap FA di sini menerima masukan dari **semua** tingkat yang lebih dalam — pola koneksi rapat (*dense connection*) seperti pada DenseNet. Modul FA sendiri memakai struktur Inception: beberapa cabang konvolusi paralel berukuran 1×1, 3×3, dan 5×5 ditambah satu cabang *max-pooling* 3×3, yang hasilnya disambung dan dipetakan kembali ke 64 kanal; ukuran spasial tidak berubah karena semua langkah bernilai 1. Fitur dari tingkat lebih dalam diperbesar dengan interpolasi bilinear; pada kasus paling ekstrem, keluaran FA5 diperbesar dengan faktor 2, 4, 8, dan 16 untuk menjangkau empat tingkat di atasnya. Keluaran FA1 (tingkat terhalus, 320×320) dilewatkan ke konvolusi 1×1 untuk menghasilkan peta saliency akhir, yang diawasi oleh *ground truth* ukuran penuh melalui loss akhir Lf.

Alur lengkap kerangka ini dirangkum pada diagram berikut:

```
MASUKAN: RGB 320x320x3  +  depth 320x320x3 (kanal digandakan 3x)
                  |  digabung pada dimensi batch
                  v
          batch 320x320x3x2
+-------------------------------------------------------+
| JL: backbone siamese berbagi bobot (VGG-16/ResNet-101)|
|     enam hierarki, ukuran spasial 320..20             |
+-------------------------------------------------------+
   |     |     |     |     |     |     (side output)
   v     v     v     v     v     v
  CP1   CP2   CP3   CP4   CP5   CP6 -- konv 1x1 -- prediksi kasar
   |     |     |     |     |     |    RGB + depth -- loss global Lg
   v     v     v     v     v     v
  CM1   CM2   CM3   CM4   CM5   CM6   fusi: Xrgb + Xd + (Xrgb*Xd)
   |     |     |     |     |     |
   v     v     v     v     v     v
  FA1 <-- FA2 <-- FA3 <-- FA4 <-- FA5 <-- FA6   (koneksi rapat:
   |                                            tiap FA menerima
   v                                            semua tingkat lebih dalam)
 konv 1x1 -- peta saliency 320x320 -- loss akhir Lf
```

### Fungsi Loss dan Pelatihan

Loss total adalah Ltotal = Lf + λ·ΣLg, dengan Lg dihitung untuk prediksi kasar RGB dan kedalaman; ketiganya memakai *cross-entropy* per piksel. Bobot λ disetel 256 (= 16²) untuk mengimbangi skala loss antara prediksi beresolusi rendah dan tinggi. Implementasi memakai pustaka Caffe; bobot backbone diinisialisasi dari model DSS yang sudah terlatih, lalu disetel halus secara *end-to-end*. Pelatihan berjalan 40 *epoch* dengan laju belajar 10⁻⁹, momentum 0,99, peluruhan bobot 0,0005, dan augmentasi pencerminan citra, memakan waktu sekitar 18 jam (VGG-16) sampai 20 jam (ResNet-101) pada satu GPU NVIDIA 1080Ti.

## Eksperimen dan Hasil

Evaluasi dilakukan pada enam benchmark RGB-D SOD: NJU2K (2.000 citra), NLPR (1.000), STERE (1.000), RGBD135 (135), LFSD (100), dan SIP (929). Sesuai protokol CPFP, model dilatih hanya pada 1.500 sampel NJU2K dan 700 sampel NLPR, lalu model yang sama diuji pada keempat dataset lain — pengaturan ini sekaligus menguji generalisasi lintas dataset. Empat metrik dipakai: S-measure (kemiripan struktur peta, lebih tinggi lebih baik), F-measure maksimum (harmonik presisi-*recall* pada ambang terbaik), E-measure maksimum (keselarasan piksel dan citra secara menyeluruh), dan MAE (galat absolut rata-rata, lebih rendah lebih baik).

Hasil utama (varian ResNet-101) antara lain: S-measure 0,929 pada NLPR dan 0,854 pada NJU2K, dibandingkan 0,904 dan 0,824 untuk D3Net — selisih 2,5 dan 3,0 poin. Rata-rata pada enam dataset, JL-DCF mengungguli D3Net sekitar 1,9% S-measure, dan versi VGG-16-nya pun masih di atas CPFP maupun D3Net. Keunggulan yang konsisten pada keempat metrik dan keenam dataset, termasuk dataset di luar data latih, menunjukkan peningkatan ini bukan penyesuaian pada satu tolok ukur.

Studi ablasi (pelepasan komponen untuk mengukur kontribusinya) memberi tiga temuan. Pertama, mengganti *joint learning* dengan dua backbone terpisah (SL-DCF) menurunkan kinerja 1,1% (S-measure) sampai 1,76% (F-measure), dan pada laju belajar yang sama pelatihannya terjebak pada optimum lokal dengan loss tinggi — bukti langsung bahwa berbagi bobot mempermudah optimasi, bukan sekadar menghemat parameter. Kedua, mengganti modul CM dengan penyambungan kanal menurunkan kinerja, misalnya S-measure NJU2K turun dari 0,879 ke 0,870. Ketiga, pengujian satu modalitas menunjukkan RGB umumnya lebih informatif daripada kedalaman, tetapi kedalaman saja mengungguli RGB pada SIP dan RGBD135 yang peta kedalamannya berkualitas baik; sebaliknya pada STERE, yang peta kedalamannya kasar dan batas objeknya tidak tepat, kedalaman saja tertinggal 16–20% dari RGB dan fusi tidak memberi keuntungan berarti.

## Kelebihan dan Keterbatasan

Kelebihan kerangka ini: (1) satu backbone untuk dua modalitas memangkas jumlah parameter dibandingkan fusi tengah dua cabang; (2) berbagi bobot menstabilkan pelatihan, terbukti dari perbandingan kurva belajar terhadap varian dua backbone; (3) fusi kooperatif eksplisit mencegah model mengabaikan modalitas kedalaman; (4) kerangkanya umum — backbone dan modul agregasi dapat diganti — dan terbukti menggeneralisasi ke dataset di luar data latih.

Keterbatasannya: (1) kinerja bergantung pada kualitas peta kedalaman, sebagaimana ditunjukkan kasus STERE; (2) model dilatih dengan konvensi kedalaman tertentu — objek dekat bernilai gelap setelah normalisasi min-maks — dan menurut catatan resmi repositorinya, peta dengan konvensi terbalik (misalnya peta disparitas) menurunkan kinerja saat pengujian; (3) dari sisi rekayasa, decoder berkoneksi rapat menambah beban komputasi karena setiap modul agregasi memproses masukan dari banyak tingkat; (4) secara konseptual, backbone CNN memiliki cakupan konteks global terbatas dibandingkan arsitektur *transformer* yang muncul kemudian.

## Kaitan dengan Bab Lain

Bab ini berada pada garis lanjut fusi tengah RGB-D SOD yang dibahas pada bab-bab sebelumnya. [035 - 2019 - DMRA](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md) adalah salah satu baseline kuat yang dikalahkan JL-DCF pada seluruh dataset. Pembanding utamanya adalah [037 - 2021 - D3Net (Rethinking RGB-D SOD)](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md): D3Net adalah model peringkat pertama sebelum JL-DCF dan penyedia dataset SIP yang dipakai dalam evaluasi bab ini. Metode seangkatan seperti [036 - 2020 - BBS-Net](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md) dan [041 - 2020 - UC-Net](./041%20-%202020%20-%20UC-Net%20-%20RGB-D%20SOD.md) tetap memakai backbone dua cabang; prinsip berbagi bobot JL-DCF menjadi alternatif hemat terhadap keduanya. Gagasan ini kemudian diperluas penulisnya ke backbone *transformer* pada versi jurnal (TPAMI 2021), sejalan dengan peralihan klaster ini ke arsitektur transformer pada bab 042 dan 043.

## Poin untuk Sitasi

Kutip dengan kunci `fu2020jldcf`. Ringkasan yang aman dikutip: "JL-DCF (CVPR 2020) memproses citra RGB dan peta kedalaman melalui satu backbone siamese berbagi bobot (*joint learning*) dan menggabungkan fitur hierarkis keduanya dengan fusi kooperatif penjumlahan-plus-perkalian pada decoder berkoneksi rapat (*densely-cooperative fusion*). Pada enam benchmark RGB-D SOD, kerangka ini mengungguli D3Net dengan rata-rata S-measure lebih tinggi sekitar 1,9%." Catatan verifikasi sebelum sitasi formal: (1) seluruh angka hasil di bab ini diambil dari Tabel 1 dan 2 arXiv v1 (2004.08515); (2) makalah menyebut NJU2K berisi 2.000 sampel, tetapi catatan resmi repositori mengoreksinya menjadi 1.985 sampel yang benar-benar dipakai; (3) klaim abstrak menyebut peningkatan "±1,9% S-measure", sedangkan bagian kontribusi menyebut "±2% F-measure" — keduanya konsisten dengan tabel tetapi merujuk metrik berbeda.
