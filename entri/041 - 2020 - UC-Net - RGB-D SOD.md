# 041 - UC-Net: Uncertainty Inspired RGB-D Saliency Detection via Conditional Variational Autoencoders

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2020ucnet` |
| Judul asli | UC-Net: Uncertainty Inspired RGB-D Saliency Detection via Conditional Variational Autoencoders |
| Penulis | Jing Zhang, Deng-Ping Fan, Yuchao Dai, Saeed Anwar, Fatemeh Sadat Saleh, Tong Zhang, Nick Barnes |
| Tahun | 2020 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2020, presentasi oral), halaman 8582–8591 |
| Tema | RGB-D SOD |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2004.05763
- **Kode sumber resmi:** https://github.com/JingZhang617/UCNet
- **Google Scholar:** https://scholar.google.com/scholar?q=UC-Net%3A%20Uncertainty%20Inspired%20RGB-D%20Saliency%20Detection%20via%20Conditional%20Variational%20Autoencoders

## Gambaran Umum

Makalah ini memperkenalkan UC-Net, model deteksi objek salien RGB-D pertama yang memperlakukan tugas tersebut sebagai estimasi distribusi, bukan estimasi titik. Deteksi objek salien (*salient object detection*, SOD) adalah tugas memisahkan objek yang paling menarik perhatian manusia dari latar belakang; varian RGB-D memakai pasangan citra warna dan peta kedalaman (*depth map*, citra yang tiap pikselnya menyatakan jarak ke kamera). Semua metode sebelumnya menghasilkan tepat satu peta saliensi deterministik per masukan, padahal anotasi peta kebenaran (*ground truth*) dibuat manusia yang penilaiannya subjektif dan bervariasi.

Gagasan intinya adalah memakai *conditional variational autoencoder* (CVAE) untuk memodelkan variasi anotasi sebagai distribusi atas peta saliensi. Mengambil sampel pada ruang laten menghasilkan beberapa peta prediksi yang berbeda namun sama-sama sahih; modul *saliency consensus* merangkumnya menjadi satu peta akhir. Sebuah jaringan koreksi kedalaman melengkapi model untuk meredam derau data *depth*. Evaluasi pada enam dataset tolok ukur melawan 18 algoritme pembanding menempatkan UC-Net sebagai yang terbaik pada keenamnya menurut empat metrik standar.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Sebelum 2020, metode SOD RGB-D berbasis pembelajaran dalam dikelompokkan menurut cara memfusi informasi RGB dan kedalaman: fusi awal (penggabungan di tingkat masukan), fusi akhir (penggabungan prediksi dari cabang RGB dan kedalaman yang terpisah), serta fusi lintas-tingkat (pertukaran fitur antar-modalitas pada beberapa tingkat jaringan, misalnya DMRA pada [bab 035](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)). Apa pun strategi fusinya, semuanya memakai satu asumsi: untuk setiap pasangan RGB-D ada satu peta saliensi benar yang tunggal, dan tugas jaringan adalah meregresi peta itu. Inilah formulasi estimasi titik.

Asumsi itu bertentangan dengan cara peta *ground truth* diperoleh. Penilaian saliensi bersifat subjektif; karena itu dataset saliensi lazim dilabeli beberapa anotator dan peta akhirnya diambil lewat mekanisme semacam voting mayoritas. Variasi antar-anotator — ketidakpastian anotasi — nyata ada, tetapi dibuang saat dataset dirilis dengan satu peta tunggal. Model yang dilatih pada peta tunggal tidak dapat menyatakan keraguan: pada citra dengan beberapa objek yang sama-sama mencolok, model deterministik terpaksa memilih satu jawaban dan mengabaikan jawaban lain yang sama sahnya.

Masalah kedua bersifat teknis: data kedalaman selalu mengandung derau, baik dari sensor kedalaman (misalnya Microsoft Kinect pada dataset DES dan NLPR) maupun dari perhitungan stereo (misalnya dataset SSB dan NJU2K). Fusi langsung RGB dengan kedalaman berderau dapat membuat jaringan ikut mempelajari deraunya. UC-Net menangani keduanya: ketidakpastian anotasi lewat CVAE, derau kedalaman lewat jaringan koreksi.

## Ide Utama

Ide utama UC-Net adalah meniru proses pelabelan dataset ke dalam arsitektur jaringan. Alih-alih mempelajari pemetaan deterministik dari citra ke satu peta, jaringan mempelajari distribusi bersyarat: diberikan pasangan RGB-D, seperti apa sebaran peta saliensi yang mungkin ditulis anotator. Distribusi ini dimodelkan dengan CVAE, model generatif yang menghasilkan keluaran dari dua sumber: fitur deterministik citra masukan dan variabel laten acak berdimensi rendah yang mewakili variasi anotasi. Sampel laten yang berbeda menghasilkan peta yang berbeda.

Karena dataset hanya menyediakan satu anotasi per citra, variasi sintetis dibangkitkan dengan penyembunyian iteratif: objek salien pada citra latih disembunyikan berulang kali sehingga objek lain muncul sebagai anotasi alternatif. Pada pengujian, beberapa sampel prediksi dirangkum dengan modul *saliency consensus* yang meniru voting mayoritas antar-anotator — persis mekanisme pembuatan *ground truth*.

## Cara Kerja Langkah demi Langkah

UC-Net terdiri atas lima modul: LatentNet (PriorNet dan PosteriorNet), DepthCorrectionNet, SaliencyNet, PredictionNet, dan modul *saliency consensus* yang hanya aktif saat pengujian. Alur datanya dirangkum pada diagram berikut.

```
I + D ──> DepthCorrectionNet ──> D' ──┐
I ──────┐                             ▼
        └─────> SaliencyNet (VGG16 + DenseASPP) ─> S^d (M = 32 kanal)
                                                          │
X = (I,D) ──> PriorNet ─> (mu, sigma)   [latihan: PosteriorNet
              │                          melihat GT Y; loss KL
              ▼                          mendekatkan prior]
        z ~ N(mu, sigma^2), K = 8 ─> Feature Expanding ─> S^s (8 kanal)
                                                          │
                              S^d + S^s ─> campur kanal (urutan r)
                                                          ▼
                              PredictionNet (konv 1x1: 8 > 4 > 1)
                                                          ▼
                              peta saliensi P; pengujian: sampling C kali
                              -> saliency consensus (voting mayoritas)
                              -> peta akhir
```

Diagram menunjukkan dua jalur fitur yang bertemu di PredictionNet: jalur deterministik S^d yang menyaring isi citra, dan jalur stokastik S^s yang menyuntikkan variasi anotasi lewat sampling variabel laten z.

### LatentNet: Memodelkan Variasi Anotasi

*Variational autoencoder* (VAE) adalah model generatif yang memetakan data ke distribusi Gaussian pada ruang laten berdimensi rendah, lalu membangkitkan data dari sampel ruang itu; CVAE mengondisikan distribusi tersebut pada data masukan. LatentNet berisi dua jaringan berstruktur sama, masing-masing lima lapis konvolusi diakhiri *global average pooling* (perataan peta fitur menjadi satu vektor) dan konvolusi 1×1. PriorNet memetakan pasangan RGB-D (X) ke parameter Gaussian (mu_prior, sigma_prior); PosteriorNet melihat juga peta *ground truth* Y dan menghasilkan (mu_post, sigma_post). PosteriorNet hanya dipakai saat pelatihan: loss CVAE memakai *KL divergence* — ukuran jarak antar-distribusi — untuk mendekatkan PriorNet ke PosteriorNet, sehingga saat pengujian PriorNet menghasilkan sampel yang seolah tahu variasi anotasi. Dimensi ruang laten disetel K = 8.

Sampel z diperoleh dengan trik reparameterisasi: z = sigma ⊙ epsilon + mu, dengan epsilon noise Gaussian standar. Vektor z diekspansi menjadi peta fitur stokastik S^s seukuran spasial S^d dengan menjadikan epsilon peta noise dua dimensi.

### Membangkitkan Variasi Anotasi (AugedGT)

CVAE lazim dilatih dengan beberapa versi anotasi per citra, sedangkan dataset RGB-D hanya punya satu. Solusinya: objek salien pada citra RGB disembunyikan (ditimpa nilai rata-rata dataset), lalu citra hasilnya dilewatkan ke model SOD RGB yang sudah ada (BASNet) untuk menghasilkan peta saliensi baru sebagai anotasi alternatif. Penyembunyian diulang tiga kali per citra — setelah itu biasanya tidak ada objek mencolok tersisa — sehingga setiap citra latih memiliki empat versi anotasi termasuk *ground truth* asli. Dataset latih hasil prosedur ini diberi nama AugedGT.

### SaliencyNet dan DepthCorrectionNet

SaliencyNet menghasilkan fitur saliensi deterministik S^d. Enkodernya VGG16 (jaringan konvolusi 16 lapis yang dilatih awal pada ImageNet) yang dipotong setelah lapis *pooling* kelima; setiap tingkat dilengkapi modul DenseASPP — konvolusi *atrous* (berlubang, memperluas *receptive field* tanpa menurunkan resolusi) yang tersambung rapat — agar peta fitur tiap tingkat memiliki *receptive field* seluas citra penuh. Peta-peta itu digabung dan diringkas menjadi S^d dengan M = 32 kanal.

DepthCorrectionNet memperbaiki kedalaman mentah sebelum dipakai SaliencyNet; enkodernya berbagi struktur dengan SaliencyNet, dekodernya empat lapis konvolusi dengan *upsampling* bilinear. Loss-nya dua: *smooth L1* antara kedalaman terkoreksi dan mentah (agar koreksi tidak menyimpang jauh), serta *boundary IOU loss* yang memaksa tepian kedalaman sejajar dengan tepian intensitas citra RGB, berdasarkan asumsi bahwa batas objek konsisten pada kedua modalitas.

### PredictionNet: Pencampuran Kanal

PredictionNet menggabungkan S^s dan S^d. Penggabungan naif sebagai blok kanal terpisah berisiko membuat jaringan hanya memakai jalur deterministik. Solusinya, kedua peta disatukan menjadi K + M = 40 kanal, lalu urutan kanalnya diacak menurut variabel r berdimensi 40 yang dipelajari selama pelatihan, sehingga jaringan tidak dapat membedakan asal kanal. Tiga konvolusi 1×1 berukuran kanal berturut-turut K, K/2, dan 1 (yaitu 8, 4, 1) memetakan fitur campuran menjadi peta saliensi satu kanal P.

### Saliency Consensus saat Pengujian

Saat pengujian, PriorNet disampling C kali menghasilkan C prediksi. Setiap prediksi dibinerkan dengan ambang adaptif; untuk setiap piksel dihitung voting mayoritas di antara C prediksi biner. Peta akhir dihitung hanya dari prediksi yang sesuai voting mayoritas, sehingga prediksi minoritas yang menyimpang tidak menentukan hasil.

### Pelatihan

Loss total terdiri atas loss CVAE (rekonstruksi peta ditambah regularisasi KL), loss kedalaman, dan *smoothness loss* sadar-tepian yang menekan perubahan saliensi pada daerah citra yang intensitasnya rata; bobotnya lambda_1 = lambda_2 = 0,3. Model dilatih dengan PyTorch, pengoptimal Adam (laju awal 10^-4, turun 10% per epoch), *batch* 6, maksimal 30 epoch, sekitar 13 jam pada satu GPU NVIDIA GeForce RTX. Pada masukan 352×352, inferensi rata-rata 0,06 detik per citra — sekitar 16 citra per detik, di bawah kecepatan *real-time* tetapi layak untuk pemrosesan luring.

## Eksperimen dan Hasil

Pengujian dilakukan pada enam dataset RGB-D: NJU2K, NLPR, SSB, LFSD, DES, dan SIP (dataset baru yang dirilis bersama D3Net). Pembandingnya 18 algoritme: sepuluh metode fitur rancangan tangan dan delapan model deep learning. Empat metrik dipakai: MAE (*Mean Absolute Error*, rata-rata selisih absolut prediksi terhadap *ground truth*; makin kecil makin baik), F-measure (rata harmonik presisi–recall), E-measure (keselarasan piksel sekaligus statistik global), dan S-measure (kemiripan struktur regional peta).

Hasil utamanya: UC-Net terbaik pada keenam dataset untuk seluruh metrik, dengan peningkatan paling besar pada SSB dan SIP. Angka pasti per dataset tercantum pada Tabel 1 naskah dan tidak dikutip di sini. Studi ablasi (uji dengan mencabut atau mengganti komponen) memberi bukti per komponen:

- Mencabut DepthCorrectionNet menurunkan kinerja; pada DES, kehadirannya menambah sekitar 4 poin persen pada S-measure, E-measure, dan F-measure — bukti kuantitatif bahwa koreksi kedalaman berderau berdampak.
- Mengganti CVAE dengan VAE biasa, model multi-kepala, atau *MC-dropout* tetap menghasilkan kinerja setara atau di atas metode mutakhir saat itu, tetapi semuanya di bawah CVAE penuh; secara kualitatif, hanya CVAE yang menghasilkan prediksi beragam pada citra ambigu, sedangkan kedua alternatif menghasilkan prediksi yang hampir sama.
- Dimensi laten K = 8 terpilih terbaik; K = 32 menurunkan kinerja, dan rentang K antara 6 sampai 10 relatif stabil.
- Pelatihan dengan AugedGT mengalahkan dataset asli, mengonfirmasi manfaat anotasi alternatif.
- Mengganti *depth* mentah dengan representasi HHA (pengkodean kedalaman tiga kanal) memberi kinerja serupa; model tidak peka terhadap representasi kedalaman.

Interpretasi keseluruhan: keunggulan UC-Net bukan hanya pada angka, melainkan pada kemampuan menghasilkan beberapa prediksi sahih untuk citra bermakna ganda — sesuatu yang secara struktural mustahil bagi model estimasi titik.

## Kelebihan dan Keterbatasan

Kelebihan: (1) pelopor formulasi probabilistik pada SOD RGB-D, menghasilkan distribusi prediksi bukan satu titik; (2) *saliency consensus* menyelaraskan inferensi dengan cara dataset dibuat; (3) koreksi kedalaman memberi keuntungan terukur (sekitar 4 poin pada DES); (4) keberagaman prediksi terbukti melebihi alternatif stokastik yang lebih sederhana.

Keterbatasan: (1) inferensi memerlukan C kali sampling dan konsensus, sehingga biayanya kelipatan model satu-jalan; dengan 0,06 detik per citra model tidak *real-time*; (2) pembangkitan anotasi alternatif bergantung pada model SOD RGB eksternal (BASNet), sehingga kualitas AugedGT dibatasi kualitas model itu; (3) dari sisi rekayasa, arsitektur berbasis VGG16 berat dibanding *backbone* modern, dan metrik tolok ukur hanya menilai peta konsensus — keragaman prediksi itu sendiri hanya ditunjukkan kualitatif; (4) secara konseptual, ketidakpastian yang dimodelkan adalah ketidakpastian anotasi, bukan ketidakpastian model terhadap data di luar distribusi latih.

## Kaitan dengan Bab Lain

UC-Net berdiri di tengah gelombang SOD RGB-D 2019–2021. Ia mewarisi *backbone* VGG16 dan fusi lintas-modal dari generasi sebelumnya, khususnya DMRA ([bab 035](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)) yang menjadi pembanding utama evaluasi kualitatifnya. Kontemporernya setahun itu — BBS-Net ([bab 036](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)), JL-DCF ([bab 038](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md)), S2MA ([bab 039](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md)), dan HDFNet ([bab 040](./040%20-%202020%20-%20HDFNet%20-%20RGB-D%20SOD.md)) — tetap deterministik dan berlomba pada angka metrik, sedangkan UC-Net mengubah pertanyaannya: bukan "peta apa yang benar" melainkan "peta-peta apa yang mungkin". Dataset SIP yang dipakai menguji UC-Net berasal dari karya D3Net ([bab 037](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md)). Masalah anotasi tunggal yang diangkatnya tetap relevan bagi arsitektur penerus, termasuk pendekatan Transformer pada VST ([bab 042](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md)) dan SwinNet ([bab 043](./043%20-%202022%20-%20SwinNet%20-%20RGB-D%20SOD.md)).

## Poin untuk Sitasi

Kutip dengan kunci `zhang2020ucnet`. Ringkasan yang aman dikutip: "UC-Net adalah kerangka SOD RGB-D pertama yang memodelkan ketidakpastian anotasi manusia dengan *conditional variational autoencoder*, menghasilkan beragam peta saliensi lewat sampling ruang laten dan merangkumnya lewat modul *saliency consensus*; model ini mencapai kinerja terbaik pada enam dataset tolok ukur RGB-D." Catatan verifikasi: angka pasti per dataset pada Tabel 1 naskah tidak dikutip dalam bab ini dan wajib diperiksa ke naskah asli sebelum sitasi formal; klaim peningkatan sekitar 4 poin pada DES, inferensi 0,06 detik pada 352×352, dan hiperparameter (K = 8, M = 32, lambda = 0,3) berasal dari teks naskah arXiv:2004.05763.
