# 060 - Multimodal Token Fusion for Vision Transformers

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `wang2022tokenfusion` |
| Judul asli | Multimodal Token Fusion for Vision Transformers |
| Penulis | Yikai Wang, Xinghao Chen, Lele Cao, Wenbing Huang, Fuchun Sun, Yunhe Wang |
| Tahun | 2022 |
| Venue | IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022) |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **arXiv (PDF gratis):** https://arxiv.org/abs/2204.08721
- **DOI (arXiv):** https://doi.org/10.48550/arXiv.2204.08721
- **Kode sumber resmi:** https://github.com/yikaiw/TokenFusion
- **Google Scholar:** https://scholar.google.com/scholar?q=Multimodal%20Token%20Fusion%20for%20Vision%20Transformers
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Multimodal%20Token%20Fusion%20for%20Vision%20Transformers&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan TokenFusion, metode fusi multimodal untuk *vision transformer* — arsitektur jaringan saraf yang memproses citra sebagai urutan token. Masalah yang dipecahkan adalah cara menggabungkan beberapa transformer satu modal (misalnya satu untuk citra warna RGB dan satu untuk peta kedalaman) tanpa merusak struktur atensi yang telah dipelajari masing-masing model. Alih-alih menggabungkan seluruh token dari semua modalitas, TokenFusion mendeteksi token yang tidak informatif pada satu modalitas, lalu menggantinya dengan token dari modalitas lain pada posisi yang bersesuaian.

Metode ini diuji pada tiga tugas: translasi citra multimodal (dataset Taskonomy), segmentasi semantik RGB-D (NYUDv2 dan SUN RGB-D), serta deteksi objek 3D dari awan titik dan citra (SUN RGB-D dan ScanNetV2). Pada tugas yang paling relevan dengan bab ini, TokenFusion mencapai 54,2% mIoU pada NYUDv2, melampaui metode fusi CNN terbaik saat itu (CEN, 52,5%), dengan *backbone* transformer ringan. Kode sumbernya dirilis terbuka.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Segmentasi semantik RGB-D adalah pelabelan kelas untuk setiap piksel citra dengan memakai dua masukan: citra warna (RGB) dan peta kedalaman (D) yang menyimpan jarak setiap piksel ke kamera. Silsilah metode pada klaster ini — dari FuseNet (bab 051) yang memadukan dua aliran CNN, hingga ESANet (bab 056) dan CMX (bab 058) — menunjukkan bahwa kedalaman konsisten menambah akurasi, karena bentuk geometri objek tetap terbaca ketika penampilan warna ambigu. Hampir semua berbasis CNN; fusi dilakukan lewat penjumlahan fitur, penyambungan kanal, atau gerbang perhatian.

Sementara itu, *vision transformer* (ViT) menjadi pilihan arsitektur baru. Pada ViT, citra dipotong menjadi *patch* (potongan berukuran tetap, misalnya 16×16 piksel), setiap potongan diproyeksikan linier menjadi sebuah vektor yang disebut token, dan urutan token diproses oleh lapis *self-attention* — mekanisme yang menghitung bobot interaksi untuk setiap pasangan token sehingga representasi tiap token memuat konteks seluruh citra. Ketika dua modalitas hendak dipadukan pada arsitektur ini, muncul pertanyaan desain: di mana dan bagaimana interaksi antar-modal harus terjadi.

Dua jawaban intuitif tidak memuaskan. Pertama, fusi *tanpa penyelarasan* (*alignment-agnostic*): seluruh token dari kedua modalitas disambung menjadi satu urutan, seperti pada model bahasa-visi semacam ViLT. Cara ini menggandakan panjang urutan dan, menurut penulis, melemahkan bobot atensi dalam satu modal; eksperimen makalah menunjukkan keuntungannya kecil. Kedua, fusi *sadar penyelarasan* (*alignment-aware*) secara langsung: token diproyeksikan antar-modal mengikuti korespondensi posisi piksel. Cara ini memaksa perancang memilih lapis dan token yang diproyeksikan, serta berisiko mengubah alur data asli sehingga bobot pralatih tidak lagi optimal.

## Ide Utama

Gagasan inti TokenFusion: jangan menambah token, melainkan memakai kembali slot token yang tidak informatif. Setiap lapis transformer dilengkapi penilaian skor yang menandai token-token berkontribusi kecil; token yang tertandai kemudian diganti oleh token dari modalitas pasangan pada posisi yang bersesuaian, sedangkan token penting dibiarkan utuh. Dengan cara ini, relasi atensi antar token penting dalam satu modal tidak berubah, dan informasi antar-modal masuk melalui slot yang memang kurang berguna.

Agar token pengganti tetap membawa informasi posisi, dipakai *residual positional alignment* (RPA): embedding posisi asli token yang diganti tetap ditambahkan pada fitur hasil substitusi. Hasilnya fusi yang selektif, dinamis, dan hemat: struktur transformer satu modal praktis utuh sehingga bobot pralatih tetap diwarisi.

## Cara Kerja Langkah demi Langkah

### Representasi Token dan Lapis Transformer

Setiap modalitas diolah menjadi *N* token berdimensi seragam. Satu lapis transformer terdiri atas dua blok: MSA (*multi-head self-attention*, yaitu *self-attention* dengan beberapa kepala yang dihitung paralel) diikuti MLP (*multi-layer perceptron*, jaringan dua lapis penuh per token), dan masing-masing blok didahului LN (*layer normalization*, normalisasi rata-rata dan varians fitur per token). Untuk masukan dua modalitas dipakai dua urutan token, misalnya token RGB dan token kedalaman, yang keduanya melewati struktur lapis yang sama.

### Skor Kepentingan Token

Kepentingan setiap token diukur fungsi skor s(e) = MLP(e) yang menghasilkan satu nilai dalam rentang [0,1] per token per lapis. Skor dilatih bersama jaringan utama; agar gradien mengalir, skor dikalikan ke fitur token sebelum blok MSA. Selain rugi tugas utama (misalnya rugi segmentasi), ditambahkan rugi sparsitas berupa norma *l1* — jumlah nilai absolut seluruh skor — dengan bobot λ. Rugi ini mendorong sebagian skor turun mendekati nol, sehingga sebagian token secara eksplisit ditandai tidak penting. Karena dihitung dari isi fitur, penandaan bersifat dinamis per citra.

### Substitusi Token Antar-Modal

Substitusi diterapkan sebelum setiap lapis dengan ambang θ. Token dengan skor ≥ θ dipertahankan; token dengan skor < θ diganti token dari modalitas pasangan pada posisi yang bersesuaian. Sebagai ilustrasi, pada citra 480×640 dengan *patch* 16×16 terbentuk 30×40 = 1.200 token per modalitas; bila 200 token RGB memperoleh skor di bawah θ, tepat 200 slot itu diisi token kedalaman pada posisi piksel yang sama, sedangkan 1.000 token lain tidak berubah. Untuk RGB-D yang pikselnya teregistrasi, proyeksi antar-modal cukup fungsi identitas: token ke-*n* kedua modal menunjuk piksel yang sama. Untuk segmentasi, makalah memakai θ = 2×10⁻².

Alur fusi untuk dua modalitas homogen (RGB dan kedalaman):

```
RGB (citra warna)                    D (peta kedalaman)
     |                                    |
     v potong patch + proyeksi linier     v potong patch + proyeksi linier
 N token e_RGB + embedding posisi    N token e_D + embedding posisi
     |                                    |
     v skor s = MLP(e) dalam [0,1]        v skor s = MLP(e) dalam [0,1]
┌────────────── transformer berbagi bobot, per lapis ──────────────┐
│  s >= theta : token asli dipertahankan                           │
│  s <  theta : token diganti token pada posisi sama dari modal    │
│               pasangannya; embedding posisi asli tetap (RPA)     │
└──────────────────────────────────────────────────────────────────┘
     |                                    |
     +-----------------+------------------+
                       v
        kepala segmentasi -> peta kelas per piksel
```

Diagram menekankan dua hal: bobot transformer dibagi sehingga parameter tidak berlipat, dan jumlah token konstan *N* per modalitas sehingga biaya *self-attention* tidak bertambah seperti pada fusi penyambungan.

### Residual Positional Alignment

*Positional embedding* (embedding posisi) adalah vektor yang ditambahkan ke setiap token untuk menyandi posisi *patch*-nya dalam kisi citra; tanpanya, *self-attention* tidak dapat membedakan urutan spasial token. Substitusi menimbulkan masalah: token kedalaman yang ditempatkan pada slot RGB tidak otomatis membawa posisi slot tersebut. RPA mengatasinya dengan tetap menambahkan embedding posisi asli slot pada token hasil substitusi. Gradien embedding posisi juga dihentikan setelah lapis pertama, sehingga korespondensi posisi antar-modal tetap stabil selama pelatihan.

### Penyetelan untuk Modalitas Homogen

Untuk modalitas yang teregistrasi per piksel (RGB, kedalaman, normal, tekstur), seluruh parameter MSA dan MLP dibagi antar-modalitas, tetapi LN dibuat terpisah per modalitas karena statistik masing-masing modal berbeda jauh. Substitusi berjalan dua arah: token RGB yang lemah diisi token kedalaman, dan sebaliknya. Untuk lebih dari dua modalitas, *N* token dibagi acak menjadi *M*−1 kelompok berukuran sama sebelum pelatihan; setiap kelompok diikat ke satu modalitas lain sebagai sumber pengganti, dan pembagian ini dibekukan selama pelatihan.

### Penyetelan untuk Modalitas Heterogen

Untuk modalitas dengan struktur berbeda — deteksi objek 3D dari awan titik dan deteksi 2D dari citra — dipakai dua transformer terpisah tanpa berbagi bobot. Cabang 3D mengikuti Group-Free (detektor 3D berbasis transformer yang memperlakukan titik contoh dan titik usulan sebagai token), cabang 2D mengikuti YOLOS (detektor 2D yang meneruskan *patch* citra langsung ke ViT). Karena dimensi kedua cabang berbeda, proyeksi antar-modal diganti dari identitas menjadi MLP dangkal. Korespondensi posisi memakai geometri kamera: titik 3D diproyeksikan ke piksel citra dengan matriks intrinsik dan ekstrinsik kamera, lalu piksel itu dipetakan ke indeks *patch*. Token titik 3D yang terpangkas diganti oleh token *patch* citra pada lokasi proyeksinya.

### Fungsi Rugi Gabungan

Rugi total adalah jumlah rugi tugas setiap modalitas ditambah rugi sparsitas skor di seluruh lapis, dengan bobot λ = 10⁻³ untuk segmentasi dan 10⁻⁴ untuk translasi citra. Seluruh sistem dilatih *end-to-end* (satu proses pelatihan menyatu dari masukan ke keluaran), dengan bobot awal dari pralatih ImageNet.

## Eksperimen dan Hasil

Evaluasi mencakup tiga tugas dengan tujuh modalitas pada empat dataset. Metrik utama segmentasi adalah mIoU (*mean Intersection over Union*: rata-rata rasio irisan terhadap gabungan antara piksel prediksi dan kebenaran, dihitung per kelas; maksimal 100%).

**Segmentasi RGB-D.** Pada NYUDv2 (795 citra latih, 654 uji, 40 kelas) dengan *backbone* SegFormer ringan: model satu modal RGB saja memperoleh 49,7% mIoU (versi kecil) dan 50,6% (versi besar); fusi penyambungan token hanya menambah menjadi 50,8% dan 51,4%; TokenFusion mencapai 53,3% dan 54,2%. Angka terakhir melampaui CEN, metode fusi CNN terbaik pembanding, yang memperoleh 52,5%. Pada SUN RGB-D (5.285 latih, 5.050 uji, 37 kelas) polanya sama: TokenFusion versi besar mencapai 53,0% mIoU dibanding CEN 51,1% dan penyambungan 49,0%. Interpretasinya: penyambungan naif hanya bernilai sekitar satu poin, sedangkan substitusi selektif menambah 3,6 poin di atas model satu modal — keuntungan datang dari *cara* fusi, bukan sekadar dari keberadaan modal kedua.

**Deteksi objek 3D.** Metriknya mAP@0,25 (*mean Average Precision* dengan ambang IoU 3D 0,25). Pada SUN RGB-D, TokenFusion mencapai 64,9 dibanding *backbone* Group-Free 63,0; menempelkan warna RGB langsung ke titik justru menurunkan kinerja menjadi 62,1. Pada ScanNetV2, TokenFusion mencapai 70,8 dibanding 69,1 milik pembanding terkuat. Artinya, fusi heterogen yang keliru dapat merugikan, sedangkan substitusi terpandu skor menguntungkan.

**Translasi citra.** Pada Taskonomy (1.000 citra latih, 500 validasi), tugas Shade+Texture→RGB, TokenFusion mencapai FID 43,92 — FID (*Fréchet Inception Distance*) mengukur jarak distribusi citra hasil terhadap citra asli, makin kecil makin baik — dibanding CEN 62,63, atau penurunan relatif 29,8%.

**Ablasi.** Norma *l1* sendirian tanpa substitusi praktis tidak mengubah hasil (49,5% vs 49,7% mIoU). Substitusi acak 10% token hanya mencapai 50,1%, dan 30% justru menurunkan ke 48,2% — bukti bahwa pemilihan token berbasis skor, bukan substitusi itu sendiri, yang menyumbang keuntungan. RPA menambah 0,4 poin mIoU pada segmentasi (52,9% menjadi 53,3%) dan 1,3 poin mAP pada deteksi 3D (63,6 menjadi 64,9).

## Kelebihan dan Keterbatasan

Kelebihan utama adalah generalitas: satu mekanisme berlaku untuk modalitas homogen maupun heterogen pada tiga tugas, tanpa merancang ulang arsitektur dasar. Struktur transformer satu modal praktis utuh sehingga bobot pralatih ImageNet terwarisi, jumlah token konstan sehingga biaya atensi tidak bertambah, dan berbagi parameter menekan ukuran model.

Keterbatasannya sebagai berikut. Ambang θ dan bobot λ disetel berbeda per tugas (10⁻³ versus 10⁻⁴), sehingga dari sisi rekayasa metode ini menambah hiperparameter yang peka terhadap penyetelan. Fusi menuntut penyelarasan antar-modal: pasangan RGB-D harus teregistrasi, dan fusi titik-citra memerlukan parameter kamera; pada data tanpa korespondensi eksplisit mekanisme ini tidak berlaku langsung. Rasio token yang dipangkas tidak dikendalikan eksplisit melainkan mengikuti data dan kekuatan rugi sparsitas. Terakhir, makalah tidak melaporkan latensi atau FLOPs untuk tugas segmentasi, sehingga klaim efisiensi bersifat struktural — jumlah token konstan — bukan hasil pengukuran waktu nyata.

## Kaitan dengan Bab Lain

Bab ini meneruskan garis fusi RGB-D yang diletakkan [bab 051 (FuseNet)](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md) — pemaduan dua aliran CNN pertama untuk segmentasi RGB-D — tetapi mengganti medium fusinya: bukan lagi penggabungan peta fitur konvolusi, melainkan pertukaran token di dalam transformer. Dibanding [bab 058 (CMX)](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md) yang memadukan modalitas lewat pertukaran fitur dan rektifikasi antar-*backbone* transformer, TokenFusion mengambil jalan berbeda: arsitektur satu modal dibiarkan utuh dan fusi hanya mengisi slot token tak informatif. [Bab 061 (DFormer)](./061%20-%202024%20-%20DFormer%20-%20Segmentasi%20RGB-D.md) kemudian memperlihatkan rancangan *backbone* transformer RGB-D terpadu yang lebih baru; keduanya layak dibaca berdampingan sebagai dua strategi fusi era transformer.

## Poin untuk Sitasi

Kutip dengan kunci `wang2022tokenfusion`. Ringkasan yang aman dikutip: "TokenFusion memadukan beberapa *vision transformer* satu modal dengan mendeteksi token tak informatif lewat skor terlatih, menggantinya dengan token modalitas lain pada posisi bersesuaian, dan mempertahankan embedding posisi asli melalui *residual positional alignment*; metode ini melampaui fusi berbasis CNN pada segmentasi RGB-D (54,2% mIoU di NYUDv2) serta pada deteksi objek 3D (64,9 mAP@0,25 di SUN RGB-D)."

Catatan verifikasi sebelum sitasi formal: (1) seluruh angka di bab ini diambil dari tabel naskah arXiv v2, sebaiknya dicocokkan ulang dengan versi prosiding CVPR; (2) naskah tidak konsisten menyebut ambang θ (10⁻² di bagian metode, 2×10⁻² di bagian eksperimen) dan pengaturan *backbone* (B2/B3 di bagian eksperimen, tetapi B1/B2 di paragraf hasil); (3) angka FID 43,92 dan klaim penurunan relatif 29,8% berasal dari Tabel 1 naskah.
