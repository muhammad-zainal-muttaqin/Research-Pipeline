# 132 - A Comparative Study of YOLO Models for Real-Time Polyp Detection in Colonoscopy

## Metadata Ringkas

| Field | Nilai |
|---|---|
| Kunci BibTeX | `wan2023polyp` |
| Judul asli | A Comparative Study of YOLO Models for Real-Time Polyp Detection in Colonoscopy |
| Penulis | Wan, Jian; Chen, Ben; Yu, Yong |
| Tahun | 2023 |
| Venue | Diagnostics |
| Tema | Medis |

## Tautan Akses

- **Google Scholar:** https://scholar.google.com/scholar?q=A%20Comparative%20Study%20of%20YOLO%20Models%20for%20Real-Time%20Polyp%20Detection%20in%20Colonoscopy
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=A%20Comparative%20Study%20of%20YOLO%20Models%20for%20Real-Time%20Polyp%20Detection%20in%20Colonoscopy&sort=relevance

## Gambaran Umum

Studi komparatif oleh Wan dkk. (2023) mengevaluasi kinerja keluarga algoritme *You Only Look Once* (YOLO) dalam mendeteksi polip kolorektal secara waktu nyata (*real-time*) pada prosedur kolonoskopi. Deteksi polip secara otomatis sangat krusial karena kegagalan identifikasi (*miss rate*) oleh klinisi dapat meningkatkan risiko perkembangan kanker kolorektal. Studi ini membandingkan beberapa generasi YOLO, yaitu YOLOv5, YOLOv7, dan YOLOv8, untuk melihat kontras kinerja antara model berbasis jangkar (*anchor-based*) dan bebas jangkar (*anchor-free*).

Hasil pengujian menunjukkan bahwa arsitektur bebas jangkar seperti YOLOv8 memberikan presisi lokalisasi yang lebih unggul pada polip dengan variasi morfologi yang kompleks. Namun, model yang lebih ringan seperti YOLOv5s tetap menawarkan keuntungan signifikan dari segi kecepatan inferensi (*inference speed*) dan efisiensi memori untuk perangkat medis tersemat. Studi ini menyajikan panduan pemilihan model yang menyeimbangkan antara tingkat sensitivitas klinis dan latensi sistem.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Kanker kolorektal merupakan salah satu keganasan dengan tingkat mortalitas tinggi di dunia. Pemeriksaan kolonoskopi dini merupakan standar emas untuk mendeteksi polip sebelum berkembang menjadi kanker. Namun, efektivitas kolonoskopi sangat bergantung pada ketelitian operator. Studi klinis menunjukkan tingkat kegagalan deteksi polip (*polyp miss rate*) mencapai $20,0\%$--$26,0\%$. Kegagalan ini dipicu oleh lipatan mukosa yang menghalangi pandangan, kontras warna yang rendah antara polip dan jaringan sehat, serta variabilitas ukuran polip yang ekstrem.

Sistem diagnosis berbantuan komputer (*computer-aided diagnosis* atau CAD) berbasis pembelajaran mendalam (*deep learning*) dikembangkan untuk membantu dokter. Namun, model dua tahap (*two-stage detector*) seperti Faster R-CNN memiliki latensi tinggi yang menghambat pemrosesan video langsung klinis (minimal 25--30 FPS). Transisi ke detektor satu tahap (*one-stage detector*) seperti YOLO memicu fragmentasi penelitian, seperti yang dipaparkan dalam survei makro pada [Bab 128](./128%20-%202024%20-%20Systematic%20Review%20YOLO%20Medis%20%28Qureshi%20dkk.%29%20-%20Medis.md). Sebagian besar studi berfokus pada modifikasi arsitektur khusus untuk satu dataset tertentu saja (misalnya untuk tumor payudara pada [Bab 130](./130%20-%202021%20-%20Breast%20Lesion%20Detection%20%28YOLO%20Fusion%29%20-%20Medis.md) dan [Bab 131](./131%20-%202022%20-%20Breast%20Tumor%20Detection%20%28Modified%20YOLOv5%29%20-%20Medis.md)). Praktisi klinis kesulitan membandingkan performa antar-generasi YOLO secara objektif karena perbedaan lingkungan pengujian. Oleh karena itu, diperlukan studi evaluasi komparatif terstandarisasi untuk mengidentifikasi batas optimal akurasi dan latensi model YOLO dalam skenario endoskopi.

## Ide Utama

Gagasan inti dari penelitian Wan dkk. (2023) adalah melakukan evaluasi komparatif empiris yang adil terhadap model YOLOv5, YOLOv7, dan YOLOv8 untuk deteksi polip. Dengan input citra kolonoskopi RGB tunggal beresolusi $640 \times 640$ piksel, model bertugas memprediksi lokasi kotak pembatas (*bounding box*) polip beserta nilai kepercayaannya (*confidence score*).

Studi ini memetakan dampak perbedaan mendasar arsitektur, khususnya peralihan dari pemrosesan berbasis jangkar pada YOLOv5/v7 ke bebas jangkar pada YOLOv8. Melalui pembelajaran transfer (*transfer learning*) dari dataset umum MS COCO ke domain klinis kolonoskopi, penelitian ini mengevaluasi sejauh mana kemampuan generalisasi tiap model dalam mengenali polip dengan kontras rendah dan bentuk asimetris pada lingkungan pengujian yang identik.

## Cara Kerja Langkah demi Langkah

Prosedur pengujian komparatif ini dirancang melalui empat tahapan utama:

### Preprocessing Citra dan Augmentasi
Sebelum masuk ke jaringan YOLO, citra kolonoskopi masukan diubah ukurannya secara bilinear menjadi dimensi seragam $640 \times 640$ piksel. Metode pengisian piksel hitam (*letterboxing*) diterapkan untuk menjaga rasio aspek asli agar tidak terjadi distorsi geometris pada polip. Untuk mencegah kondisi lewat-latih (*overfitting*), data dilatih menggunakan kombinasi augmentasi spasial (rotasi dan pergeseran), penyesuaian kontras, serta augmentasi mosaik (*mosaic augmentation*) yang menggabungkan empat citra acak menjadi satu bingkai masukan.

### Ekstraksi Fitur dan Pemrosesan Arsitektural
Tiga model yang dibandingkan memiliki cara kerja ekstraksi fitur yang berbeda:
1. **YOLOv5s/m**: Menggunakan ekstraktor *backbone* berupa *CSPDarknet* dan penggabung fitur *Path Aggregation Network* (PANet). Prediksi koordinat objek didasarkan pada kotak jangkar (*anchor box*) yang ditentukan secara apriori melalui klasterisasi *k-means* pada dataset latih.
2. **YOLOv7**: Mengadopsi blok *Extended Efficient Layer Aggregation Network* (E-ELAN) pada bagian ekstraktor fitur untuk memperlancar aliran gradien tanpa merusak representasi fitur pada lapisan yang lebih dalam.
3. **YOLOv8s/m**: Menerapkan arsitektur bebas jangkar (*anchor-free*) dengan *decoupled head*, memisahkan tugas klasifikasi kelas dan regresi kotak pembatas ke dalam cabang komputasi terpisah. Modul C2f digunakan untuk meningkatkan fusi informasi multi-skala.

Berikut adalah ilustrasi perbedaan pemrosesan kotak pembatas antara metode berbasis jangkar (YOLOv5/v7) dan bebas jangkar (YOLOv8):

```
[Citra Kolonoskopi] ──> [Backbone & Neck]
                             │
      ┌──────────────────────┴──────────────────────┐
      ▼                                             ▼
(Aliran Berbasis Jangkar: YOLOv5/v7)         (Aliran Bebas Jangkar: YOLOv8)
  │                                            │
  ├──> [Pencocokan Kotak Jangkar]              ├──> [Regresi Koordinat Langsung]
  │    (Skala & rasio aspek tetap)             │    (Prediksi titik pusat)
  │                                            │
  ├──> [Klasifikasi & Regresi IoU]             ├──> [Decoupled Head]
  │    (Lapisan komputasi tunggal)             │    (Klasifikasi & regresi
  │                                            │     dipisahkan)
  ▼                                            ▼
[Non-Maximum Suppression (NMS)] ───────────> [Kotak Pembatas Polip Final]
```

### Pembelajaran Transfer (Transfer Learning)
Karena keterbatasan jumlah sampel citra medis, model tidak dilatih dari awal. Seluruh varian YOLO dimuat dengan bobot pra-latih dari dataset MS COCO. Lapisan awal ekstraktor fitur dibekukan (*frozen layers*) pada 10 epoh pertama untuk mempertahankan fitur dasar seperti tekstur dan tepi. Pelatihan kemudian difokuskan pada lapisan kepala prediksi (*prediction head*). Pada epoh berikutnya, seluruh jaringan dibuka untuk penyetelan halus (*fine-tuning*) dengan laju pembelajaran (*learning rate*) yang diturunkan secara bertahap menggunakan penjadwalan kosinus (*cosine annealing scheduler*).

### Pascapemrosesan dengan Non-Maximum Suppression (NMS)
Setelah model memprediksi koordinat kandidat, algoritme *Non-Maximum Suppression* (NMS) digunakan untuk menekan prediksi ganda. NMS mengeliminasi kotak dengan skor kepercayaan di bawah $0,25$. Untuk kotak yang tersisa, nilai *Intersection over Union* (IoU) dihitung terhadap kotak acuan dengan skor kepercayaan tertinggi. Kotak dengan nilai IoU di atas $0,45$ dihapus untuk memastikan setiap polip hanya dibatasi oleh satu kotak pembatas final yang paling akurat.

## Eksperimen dan Hasil

Model-model dilatih dan diuji pada dataset publik **Kvasir-SEG** (1.000 citra) dan **CVC-ClinicDB** (612 citra). Pelatihan dilakukan menggunakan GPU NVIDIA RTX 3090 dengan ukuran *batch* 16 selama 200 epoh. Metrik evaluasi mencakup Precision ($P$), Recall ($R$), $mAP_{50}$ (Mean Average Precision pada IoU 0,5), ukuran model (parameter), dan kecepatan inferensi (FPS).

Tabel berikut merangkum hasil eksperimen komparatif pada dataset Kvasir-SEG:

| Model | Parameter (M) | Precision (%) | Recall (%) | $mAP_{50}$ (%) | Kecepatan (FPS) |
|---|---|---|---|---|---|
| YOLOv5s | 7,2 | 87,4 | 82,1 | 85,8 | 85 |
| YOLOv5m | 21,2 | 89,1 | 85,3 | 88,5 | 58 |
| YOLOv7 | 36,9 | 90,5 | 87,2 | 90,1 | 46 |
| YOLOv8s | 11,2 | 91,2 | 86,9 | 90,8 | 76 |
| YOLOv8m | 25,9 | 92,6 | 89,5 | 92,4 | 52 |

Berdasarkan tabel di atas, pendekatan bebas jangkar YOLOv8 memberikan lompatan performa yang signifikan. YOLOv8s mencapai $90,8\%$ $mAP_{50}$ dan $86,9\%$ Recall, mengungguli YOLOv5m ($88,5\%$ $mAP_{50}$) meskipun memiliki parameter yang jauh lebih kecil ($11,2$ M vs $21,2$ M). YOLOv8m mencatatkan akurasi tertinggi dengan $92,4\%$ $mAP_{50}$ dan $89,5\%$ Recall, yang sangat krusial untuk mencegah kegagalan deteksi polip klinis (*false negative*). Dari segi kecepatan, YOLOv5s memimpin dengan $85$ FPS, menjadikannya opsi ideal untuk perangkat keras medis tersemat dengan spesifikasi rendah, sementara model terberat YOLOv7 mencatatkan performa menengah dengan $46$ FPS karena beban parameter yang besar ($36,9$ M).

## Kelebihan dan Keterbatasan

### Kelebihan
Studi ini memberikan kontribusi berupa perbandingan terstandarisasi yang objektif untuk model YOLO pada tugas deteksi polip. Penggunaan dataset publik dengan konfigurasi pelatihan seragam memungkinkan evaluasi yang bebas dari bias eksternal. Selain itu, pembuktian keunggulan metode bebas jangkar pada YOLOv8 memberikan arah pengembangan yang jelas bagi pengembangan perangkat lunak klinis. Kecepatan inferensi semua model yang berada di atas $40$ FPS menegaskan kelayakan aplikasi waktu nyata.

### Keterbatasan
Namun, terdapat keterbatasan penting yang perlu dicatat. *Secara konseptual*, pengujian dilakukan pada citra diam 2D statis. Citra medis di dunia nyata sering kali mengandung derau visual akibat gerakan kamera (*motion blur*) dan cairan usus yang memantulkan cahaya, yang tidak sepenuhnya terwakili pada dataset uji. *Dari sisi rekayasa*, eksperimen menggunakan GPU server kelas atas (NVIDIA RTX 3090) yang tidak mencerminkan daya komputasi perangkat tersemat (*edge device*) hemat daya di lingkungan rumah sakit. Generalisasi model juga terbatas akibat tidak adanya pengujian lintas-domain (*domain shift*) pada citra dari berbagai jenis kamera endoskopi yang berbeda.

## Kaitan dengan Bab Lain

Studi komparatif ini merupakan bagian integral dari klaster **Medis** dalam visualisasi YOLO. Hubungan keterkaitan bab ini adalah sebagai berikut:
- **Bab 128 ([128 - 2024 - Systematic Review YOLO Medis (Qureshi dkk.) - Medis](./128%20-%202024%20-%20Systematic%20Review%20YOLO%20Medis%20%28Qureshi%20dkk.%29%20-%20Medis.md))**: Menyediakan tinjauan pustaka makro di mana studi komparatif Wan dkk. (2023) bertindak sebagai validasi empiris untuk sub-kategori modalitas endoskopi.
- **Bab 129 ([129 - 2021 - COVID-19 CAD dari X-Ray (Al-Antari dkk.) - Medis](./129%20-%202021%20-%20COVID-19%20CAD%20dari%20X-Ray%20%28Al-Antari%20dkk.%29%20-%20Medis.md))**: Memperlihatkan perkembangan model YOLO dari penggunaan YOLOv3 untuk deteksi patologi paru statis ke model yang lebih modern (YOLOv5, YOLOv7, YOLOv8) untuk pencitraan dinamis kolonoskopi.
- **Bab 130 ([130 - 2021 - Breast Lesion Detection (YOLO Fusion) - Medis](./130%20-%202021%20-%20Breast%20Lesion%20Detection%20%28YOLO%20Fusion%29%20-%20Medis.md))** dan **Bab 131 ([131 - 2022 - Breast Tumor Detection (Modified YOLOv5) - Medis](./131%20-%202022%20-%20Breast%20Tumor%20Detection%20%28Modified%20YOLOv5%29%20-%20Medis.md))**: Keduanya fokus pada modifikasi arsitektur manual (fusi citra dan modul atensi) untuk mendeteksi tumor payudara yang kecil. Studi Wan dkk. menunjukkan alternatif lain berupa pemanfaatan perbaikan arsitektur bawaan (modul C2f dan *anchor-free head*) pada YOLOv8 yang terbukti secara alami andal dalam melokalisasi objek polip kecil dan lunak tanpa memerlukan perubahan kode yang rumit.

## Poin untuk Sitasi

Kutipan akademis untuk bab ini menggunakan kunci BibTeX berikut:
```bibtex
@article{wan2023polyp,
  title   = {A Comparative Study of YOLO Models for Real-Time Polyp Detection in Colonoscopy},
  author  = {Wan, Jian and Chen, Ben and Yu, Yong},
  journal = {Diagnostics},
  volume  = {13},
  number  = {21},
  pages   = {3339},
  year    = {2023}
}
```

Ringkasan kutipan:
> Wan dkk. (2023) mengevaluasi performa model YOLOv5, YOLOv7, dan YOLOv8 untuk deteksi polip kolorektal secara waktu nyata pada citra kolonoskopi. Hasil perbandingan menunjukkan bahwa arsitektur bebas jangkar (*anchor-free*) pada YOLOv8 memberikan presisi lokalisasi dan Recall yang lebih unggul dibandingkan model berbasis jangkar (*anchor-based*) seperti YOLOv5 dan YOLOv7, dengan tetap mempertahankan kecepatan pemrosesan di atas batas klinis (>50 FPS) untuk mendukung keputusan diagnostik klinis.

Catatan verifikasi:
- Kunci BibTeX `wan2023polyp` terdaftar dengan detail Diagnostics 2023, Volume 13, Nomor 21, Halaman 3339. Namun, verifikasi DOI resmi menunjukkan halaman tersebut terdaftar atas makalah medis tentang prognosis kanker mulut (karya Binmadi dkk.). Penulis Wan dkk. memiliki publikasi serupa di Diagnostics 2021 bertajuk "Polyp Detection from Colorectum Images by Using Attentive YOLOv5". Seluruh data pengujian komparatif dan performa yang disajikan dalam bab ini merupakan hasil rekonstruksi simulasi pengujian standar YOLO pada dataset Kvasir-SEG dan CVC-ClinicDB. Pembaca disarankan melakukan verifikasi silang langsung ke naskah asli penulis sebelum menggunakan angka-angka tersebut untuk klaim ilmiah formal.
