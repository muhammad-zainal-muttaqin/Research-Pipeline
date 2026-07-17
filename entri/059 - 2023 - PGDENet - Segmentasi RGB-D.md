# 059 - PGDENet: Progressive Guided Fusion and Depth Enhancement Network for RGB-D Indoor Scene Parsing

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhou2022pgdenet` |
| Judul asli | PGDENet: Progressive Guided Fusion and Depth Enhancement Network for RGB-D Indoor Scene Parsing |
| Penulis | Wujie Zhou, Enquan Yang, Jingsheng Lei, Jian Wan, Lu Yu |
| Tahun | 2023 (daring 2022) |
| Venue | IEEE Transactions on Multimedia, vol. 25, hlm. 3483–3494 |
| Tema | Segmentasi RGB-D |

## Tautan Akses
- **DOI (halaman penerbit IEEE):** https://doi.org/10.1109/TMM.2022.3161852
- **Google Scholar:** https://scholar.google.com/scholar?q=PGDENet%3A%20Progressive%20Guided%20Fusion%20and%20Depth%20Enhancement%20Network%20for%20RGB-D%20Indoor%20Scene%20Parsing
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=PGDENet%3A%20Progressive%20Guided%20Fusion%20and%20Depth%20Enhancement%20Network%20for%20RGB-D%20Indoor%20Scene%20Parsing&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan PGDENet (*Progressive Guided Fusion and Depth Enhancement Network*), jaringan segmentasi semantik RGB-D untuk pemahaman adegan dalam ruangan (*indoor scene parsing*). Segmentasi semantik adalah tugas melabeli setiap piksel citra dengan kelas objeknya, misalnya dinding, lantai, atau kursi; masukan RGB-D berarti jaringan menerima citra warna (RGB) sekaligus peta kedalaman (*depth map*), yaitu citra yang setiap pikselnya menyimpan jarak permukaan ke kamera.

Makalah ini mengidentifikasi dua sumber galat pada metode fusi RGB-D yang ada: fitur cabang kedalaman lemah karena peta kedalaman mentah berkualitas rendah, dan penggabungan fitur antarmodalitas dilakukan tanpa memperhitungkan perbedaan tingkat abstraksi fitur. PGDENet menjawab keduanya dengan dua modul: modul penguatan kedalaman (*depth enhancement module*, DEM) yang memperbaiki fitur kedalaman dengan panduan RGB, dan modul fusi komplementer progresif (*progressive complementary fusion module*, PCFM) yang menggabungkan kedua modalitas bertingkat dari fitur semantik tertinggi ke fitur detail terendah. Dengan *backbone* ResNet-34, PGDENet mencapai 53,7% mIoU pada NYUv2 dan 51,0% mIoU pada SUN RGB-D — di atas metode konvolusional dua cabang sezamannya.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Metode segmentasi RGB-D umumnya memakai arsitektur dua cabang: satu *encoder* mengekstrak fitur dari citra RGB, satu *encoder* lain dari peta kedalaman, kemudian keduanya digabung dan diteruskan ke *decoder* yang menghasilkan peta kelas per piksel. Pola ini diletakkan oleh FuseNet (bab 051) dan diwarisi hampir semua metode sesudahnya. Perbedaan antarmetode terletak pada cara penggabungan (fusi) fitur kedua cabang.

Dua kelemahan spesifik menjadi sasaran makalah ini. Pertama, RGB dan kedalaman berbeda sifatnya: RGB kaya tekstur tetapi peka pencahayaan, sedangkan peta kedalaman dari sensor konsumen (misalnya Kinect) sering berderau dan berlubang — nilai hilang pada permukaan mengilap, gelap, atau terlalu jauh — sehingga fitur cabang kedalaman lemah dan representasi gabungannya ikut menurun. Kedua, fusi sekaligus pada satu titik tidak mengatur kerja sama fitur tingkat tinggi dan tingkat rendah: fitur tingkat rendah menyimpan detail spasial seperti tepi objek, fitur tingkat tinggi menyimpan makna semantik, dan menggabungkan keduanya tanpa panduan dapat memasukkan derau atau menghilangkan informasi kunci, sehingga peta segmentasi menjadi tidak akurat. Pendekatan sebelumnya menangani sebagian masalah ini: SA-Gate (bab 055) menyaring fitur antarmodalitas dengan mekanisme gerbang, dan ESANet (bab 056) mengejar efisiensi dengan fusi satu arah. Namun perbaikan fitur kedalaman sebelum fusi, serta pengaturan urutan fusi antar-tingkat, belum digarap secara eksplisit.

## Ide Utama

Gagasan inti PGDENet terdiri atas dua bagian yang saling melengkapi. Bagian pertama: jangan langsung memakai kedalaman mentah. Karena citra RGB berkualitas tinggi dan merekam struktur adegan yang sama, fitur RGB dipakai untuk memperkuat fitur kedalaman lebih dahulu — menekan bagian yang tidak dapat dipercaya dan menonjolkan struktur yang konsisten dengan citra warna. Bagian kedua: jangan menggabungkan semua tingkat fitur sekaligus. Fusi dimulai dari fitur tingkat tertinggi yang paling kaya makna semantik, lalu hasilnya dijadikan panduan saat menggabungkan fitur tingkat di bawahnya, dan seterusnya sampai tingkat paling dangkal. Dengan urutan ini, informasi semantik yang sudah tergabung mengarahkan fusi fitur detail, sehingga perbedaan sifat antar-tingkat menyusut di setiap langkah.

## Cara Kerja Langkah demi Langkah

### Garis Besar Arsitektur

PGDENet adalah jaringan *fully convolutional* (seluruhnya tersusun dari lapis konvolusi, sehingga dapat menerima citra berbagai ukuran) dengan pola *encoder-decoder*: *encoder* mengecilkan resolusi spasial sambil memperdalam makna fitur, *decoder* memulihkan resolusi untuk menghasilkan label per piksel. Dua *encoder* ResNet-34 — jaringan konvolusi residual 34 lapis dengan sambungan pintas (*skip connection*) antarblok — dipakai sebagai *backbone*: satu untuk RGB, satu untuk kedalaman. Keluaran setiap *encoder* dibagi menjadi empat tingkat sesuai tahapan ResNet; tingkat 1 beresolusi paling tinggi (detail), tingkat 4 paling rendah (semantik). Alur lengkapnya:

```
citra RGB                    peta kedalaman (mentah, berderau/berlubang)
   │                               │
   ▼                               ▼
┌────────────┐               ┌────────────┐
│ encoder    │               │ encoder    │
│ RGB        │               │ kedalaman  │
│ ResNet-34  │               │ ResNet-34  │
└─────┬──────┘               └─────┬──────┘
      │ R1 R2 R3 R4                │ D1 D2 D3 D4   (R4/D4 = semantik)
      │                            ▼
      │                    ┌───────────────┐
      │                    │ DEM per       │  penguatan korelasi kanal
      │                    │ tingkat       │  dan spasial, dipandu RGB
      │                    └─────┬─────────┘
      │                          │ D1' D2' D3' D4'
      │                          ▼
      │   fusi progresif: tingkat tinggi memandu tingkat di bawahnya
      │
      └─R4──┐
            ├──► PCFM ──► F4 ──┐ panduan
        D4'─┘                  ▼
      └─R3──┐
            ├──► PCFM ──► F3 ──┐
        D3'─┘                  ▼
      └─R2──┐
            ├──► PCFM ──► F2 ──┐
        D2'─┘                  ▼
      └─R1──┐
            ├──► PCFM ──► F1
        D1'─┘                  │
                               ▼
                          decoder ──► peta segmentasi per piksel
```

Diagram menunjukkan dua pembeda PGDENet dari fusi biasa: cabang kedalaman melewati DEM sebelum difusi, dan PCFM berjalan berantai dari tingkat 4 ke tingkat 1 dengan hasil fusi tingkat atas sebagai panduan.

### Modul Penguatan Kedalaman (DEM)

DEM ditempatkan pada cabang kedalaman sebelum fusi. Masukannya adalah fitur kedalaman pada suatu tingkat beserta fitur RGB yang bersesuaian; keluarannya adalah fitur kedalaman yang diperkuat. Penguatan dilakukan pada dua dimensi sebagaimana dinyatakan penulis. Pertama, korelasi kanal: sebuah peta fitur konvolusi tersusun atas banyak kanal, masing-masing menanggapi pola tertentu (misalnya tepi vertikal atau permukaan datar). Penguatan kanal berarti menimbang ulang setiap kanal — kanal yang konsisten dengan struktur pada citra RGB diperbesar bobotnya, kanal yang didominasi derau sensor ditekan. Kedua, korelasi spasial: setiap posisi pada peta fitur ditimbang berdasarkan hubungannya dengan posisi lain, sehingga wilayah kedalaman yang rusak (lubang) dapat diisi oleh konteks sekitarnya yang sejalan dengan tepi objek pada RGB. Citra RGB berperan sebagai sumber panduan karena resolusinya sama dan kualitasnya tinggi; kedalaman tidak diperbaiki sendirian, melainkan dikoreksi oleh modalitas yang lebih bersih.

### Modul Fusi Komplementer Progresif (PCFM)

Setelah fitur kedalaman diperkuat, penggabungan dengan RGB dilakukan bertingkat oleh PCFM. Istilah *progresif* berarti fusi tidak terjadi dalam satu operasi, melainkan empat langkah berurutan. Pada langkah pertama, fitur tingkat 4 (paling semantik) dari kedua cabang digabung menjadi fitur gabungan F4. Pada langkah kedua, F4 dibawa ke tingkat 3 dan dipakai sebagai panduan saat menggabungkan R3 dengan D3′ menjadi F3; pola yang sama berlanjut ke tingkat 2 dan tingkat 1. Sifat *komplementer* berarti kedua modalitas saling melengkapi: RGB menyumbang tekstur dan warna, kedalaman menyumbang geometri dan batas objek yang tegas.

Urutan dari atas ke bawah dipilih karena fitur tingkat tinggi sudah menyaring derau lokal dan memuat makna adegan. Ketika hasilnya turun sebagai panduan, fusi pada tingkat yang lebih dangkal tidak mencampur dua modalitas secara bebas, melainkan menempatkan detail spasial di bawah kendali konteks semantik; perbedaan abstraksi antar-tingkat pun diperkecil selapis demi selapis.

### Contoh Alur Numerik

Pada masukan NYUv2 480×640 piksel, keluaran empat tingkat ResNet-34 (dengan penurunan resolusi bertahap 4, 8, 16, dan 32 kali) kira-kira berukuran 120×160, 60×80, 30×40, dan 15×20 posisi. Misalkan peta kedalaman mentah kehilangan nilai pada permukaan layar televisi yang gelap. DEM pada tingkat 1–2 menekan bobot posisi berlubang itu dan memperkuat tepi layar yang terlihat jelas pada RGB. PCFM kemudian menggabungkan fitur tingkat 4 (15×20) lebih dahulu — pada skala ini, daerah televisi sudah terwakili sebagai satu konsep semantik — lalu F4 memandu fusi tingkat 3 (30×40), dan seterusnya sampai tingkat 1 (120×160). *Decoder* akhirnya menaikkan resolusi fitur gabungan kembali ke 480×640 dan mengeluarkan satu dari 40 kelas NYUv2 untuk setiap piksel.

## Eksperimen dan Hasil

Evaluasi dilakukan pada dua tolok ukur standar segmentasi dalam ruangan. NYUv2 memuat 1.449 pasangan RGB-D berlabel padat (795 untuk pelatihan, 654 untuk pengujian) dengan 40 kelas. SUN RGB-D lebih besar: 10.335 citra dengan 37 kelas. Metrik utama adalah mIoU (*mean Intersection over Union*): untuk setiap kelas dihitung rasio luas irisan terhadap luas gabungan antara piksel prediksi dan piksel kebenaran, lalu dirata-ratakan ke semua kelas; nilai maksimal 100%.

Angka utama PGDENet (dikutip dari tabel perbandingan DFormer dan DFormerv2 yang saling cocok):

| Dataset | Resolusi masukan | Komputasi | mIoU |
|---|---|---|---|
| NYUv2 (40 kelas) | 480×640 | 178,8 GFLOPs | 53,7% |
| SUN RGB-D (37 kelas) | 530×730 | 229,1 GFLOPs | 51,0% |

Interpretasi: pada NYUv2, PGDENet (53,7%) berada tepat di atas FRNet (53,6%) yang memakai *backbone* ResNet-34 yang sama, dan di atas ESANet (50,3%) serta EMSANet (51,0%); pada SUN RGB-D, 51,0% sejajar dengan TokenFusion MiT-B3 (51,0%) dan berada di bawah CMX MiT-B4 (52,1%). Dengan demikian klaim penulis terkonfirmasi untuk kelas metode konvolusional dua cabang; metode berbasis *transformer* yang muncul hampir bersamaan (CMX, bab 058) kemudian menyalipnya. Dua catatan biaya: PGDENet memuat 100,7 juta parameter — sekitar tiga kali ESANet (31,2 juta) — sehingga peningkatan akurasinya dibayar dengan model yang jauh lebih besar.

## Kelebihan dan Keterbatasan

Kelebihan PGDENet adalah menangani dua sumber galat sekaligus dalam satu rancangan: kualitas fitur kedalaman diperbaiki sebelum fusi (DEM), dan kerja sama antar-tingkat diatur lewat urutan fusi terpandu (PCFM). Kedua gagasan bersifat umum, tidak terikat pada satu *backbone* tertentu, dan peningkatannya terbukti pada dua dataset sekaligus.

Keterbatasannya, sebagian berupa analisis penulis bab. Dari sisi rekayasa, 100,7 juta parameter dan 178,8–229,1 GFLOPs per citra tergolong berat untuk pemakaian *real-time* pada robot atau kamera tertanam, terutama dibandingkan keluarga ESANet yang dirancang untuk efisiensi. Secara konseptual, penguatan kedalaman bergantung pada ketersediaan RGB berkualitas tinggi — pada adegan gelap di mana RGB ikut rusak, panduan untuk DEM melemah, dan makalah tidak menguji kondisi tersebut. Keterbatasan lain: evaluasi hanya mencakup adegan dalam ruangan, sehingga perilaku metode pada data luar ruangan tidak diketahui.

## Kaitan dengan Bab Lain

PGDENet meneruskan garis fusi dua cabang yang dibuka FuseNet (bab 051), yang menggabungkan fitur RGB dan kedalaman secara langsung. Gagasan menyaring informasi antarmodalitas sebelum fusi telah muncul pada SA-Gate (bab 055) lewat mekanisme gerbang; PGDENet mengalihkan penyaringan itu satu langkah lebih awal, ke perbaikan fitur kedalaman itu sendiri. Dibandingkan ESANet (bab 056) yang mengutamakan efisiensi, PGDENet memilih akurasi dengan biaya komputasi lebih besar. Pada tahun yang sama, CMX (bab 058) menempuh jalur berbeda dengan fusi berbasis *transformer* dan melampaui akurasi PGDENet pada kedua dataset.

- [051 - 2016 - FuseNet - Segmentasi RGB-D](./051%20-%202016%20-%20FuseNet%20-%20Segmentasi%20RGB-D.md)
- [055 - 2020 - SA-Gate - Segmentasi RGB-D](./055%20-%202020%20-%20SA-Gate%20-%20Segmentasi%20RGB-D.md)
- [056 - 2021 - ESANet - Segmentasi RGB-D](./056%20-%202021%20-%20ESANet%20-%20Segmentasi%20RGB-D.md)
- [058 - 2023 - CMX - Segmentasi RGB-D](./058%20-%202023%20-%20CMX%20-%20Segmentasi%20RGB-D.md)

## Poin untuk Sitasi

Kutip dengan kunci `zhou2022pgdenet`. Ringkasan yang aman dikutip: "PGDENet memperbaiki fitur peta kedalaman dengan modul penguatan kedalaman berpandu RGB, kemudian menggabungkan kedua modalitas secara progresif dari fitur semantik tingkat tinggi ke fitur detail tingkat rendah; dengan backbone ResNet-34, metode ini mencapai 53,7% mIoU pada NYUv2 dan 51,0% mIoU pada SUN RGB-D."

Catatan verifikasi sebelum sitasi formal:

1. Daftar penulis pada `references.bib` hanya memuat empat nama (Zhou, Yang, Lei, Yu); DBLP dan Semantic Scholar mencatat lima penulis, termasuk **Jian Wan**. Periksa naskah asli dan lengkapi `references.bib`.
2. Angka 53,7% / 51,0% mIoU, 100,7 juta parameter, dan 178,8 / 229,1 GFLOPs diambil dari tabel perbandingan DFormer (arXiv:2309.09668) dan DFormerv2 (arXiv:2504.04701) yang konsisten satu sama lain; naskah asli tertutup di IEEE, sehingga angka tersebut perlu dikonfirmasi ke tabel naskah.
3. Nilai *pixel accuracy* dan rincian hasil ablasi (kontribusi DEM dan PCFM secara terpisah) tidak berhasil diperoleh dari sumber terbuka dan sengaja tidak dicantumkan.
4. Deskripsi internal DEM dan PCFM pada bab ini dibatasi pada pernyataan abstrak (korelasi kanal dan spasial; fusi terpandu dari tingkat tinggi ke rendah); nama submodul dan persamaan rinci tidak diakses.
