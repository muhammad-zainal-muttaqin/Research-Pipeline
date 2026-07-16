# 002 - YOLO9000: Better, Faster, Stronger

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 002 dari 154 |
| Kunci BibTeX | `redmon2017yolo9000` |
| Judul | YOLO9000: Better, Faster, Stronger |
| Penulis | Redmon, Joseph; Farhadi, Ali |
| Tahun | 2017 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | YOLOv2, anchor box, multi-skala, WordTree, 9000 kelas |

> **Catatan integritas.** Ringkasan disusun dari pemahaman atas makalah ini; bagian *Abstrak* adalah **parafrase**, bukan kutipan verbatim. Angka/klaim spesifik dapat berbeda dari naskah asli — **verifikasi lewat tautan akses** sebelum dikutip dalam karya formal.

## Daftar Isi
1. [Metadata Ringkas](#metadata-ringkas)
2. [Tautan Akses](#tautan-akses-klik-untuk-viewunduh)
3. [Identitas Publikasi](#identitas-publikasi)
4. [Ringkasan Eksekutif](#ringkasan-eksekutif)
5. [Abstrak (Parafrase)](#abstrak-parafrase)
6. [Latar Belakang & Konteks](#latar-belakang--konteks)
7. [Permasalahan yang Diangkat](#permasalahan-yang-diangkat)
8. [Tujuan & Pertanyaan Penelitian](#tujuan--pertanyaan-penelitian)
9. [Tinjauan Terdahulu / Posisi Literatur](#tinjauan-terdahulu--posisi-literatur)
10. [Metodologi & Arsitektur](#metodologi--arsitektur)
11. [Kontribusi Utama](#kontribusi-utama)
12. [Rincian Eksperimen](#rincian-eksperimen)
13. [Temuan Kunci](#temuan-kunci)
14. [Keunggulan](#keunggulan)
15. [Keterbatasan](#keterbatasan)
16. [Relevansi terhadap Tema Tinjauan](#relevansi-terhadap-tema-tinjauan)
17. [Hubungan dengan Entri Lain](#hubungan-dengan-entri-lain)
18. [Glosarium Istilah](#glosarium-istilah-tema-fondasi-rgb)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLO9000%3A%20Better%2C%20Faster%2C%20Stronger
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLO9000%3A%20Better%2C%20Faster%2C%20Stronger&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 7263--7271 |

## Ringkasan Eksekutif
Generasi kedua YOLO yang menaikkan akurasi dan recall melalui anchor box, batch normalization, dan pelatihan multi-skala, sekaligus memperkenalkan pelatihan gabungan deteksi-klasifikasi untuk mengenali lebih dari 9000 kategori.

## Abstrak (Parafrase)
YOLOv2 memperbaiki YOLOv1 pada tiga poros: 'Better' (batch normalization, klasifier resolusi tinggi, anchor box dengan dimension clusters, pelatihan multi-skala), 'Faster' (backbone Darknet-19 yang efisien), dan 'Stronger' (mekanisme WordTree yang menggabungkan dataset deteksi COCO dan klasifikasi ImageNet). Hasilnya, YOLO9000 mampu mendeteksi lebih dari 9000 kategori objek meski hanya sebagian kecil memiliki label kotak, dengan mentransfer pengetahuan dari klasifikasi ke deteksi lewat hierarki label.

## Latar Belakang & Konteks
YOLOv1 unggul dalam kecepatan namun tertinggal dalam recall dan presisi lokalisasi dibanding metode berbasis region. Selain itu, jumlah kategori yang bisa dideteksi dibatasi oleh mahalnya anotasi kotak, sehingga skala kosakata deteksi jauh lebih kecil daripada klasifikasi.

## Permasalahan yang Diangkat
- Recall dan presisi lokalisasi YOLOv1 masih kalah dari dua-tahap.
- Jumlah kelas deteksi terbatas oleh mahalnya label kotak.
- Ketidakstabilan pelatihan tanpa normalisasi.
- Resolusi klasifier pra-latih tak cocok dengan deteksi.
- Anchor manual pada metode lain tak optimal untuk dataset tertentu.

## Tujuan & Pertanyaan Penelitian
- Meningkatkan akurasi/recall tanpa mengorbankan kecepatan.
- Memperluas skala kategori deteksi hingga ribuan.
- Menyediakan mekanisme penggabungan dataset heterogen.

## Tinjauan Terdahulu / Posisi Literatur
YOLOv2 mengadopsi anchor dari Faster R-CNN namun menentukannya via k-means (dimension clusters), meminjam prediksi multi-skala, dan memperkenalkan WordTree berbasis WordNet untuk menyatukan label deteksi dan klasifikasi.

Karya/konsep pembanding yang relevan:

- Faster R-CNN — sumber gagasan anchor box.
- SSD — prediksi multi-skala.
- WordNet — hierarki label untuk WordTree.
- Batch Normalization — stabilisasi pelatihan.

## Metodologi & Arsitektur
Darknet-19 (19 lapis konvolusi) menjadi backbone; anchor box ditentukan lewat k-means pada kotak ground truth; koordinat diprediksi relatif terhadap sel (direct location prediction) agar stabil; pelatihan multi-skala mengganti resolusi input tiap beberapa iterasi. WordTree memungkinkan softmax hierarkis atas gabungan ImageNet+COCO.

Komponen / langkah metodologis utama:

- Batch normalization di semua konvolusi (+mAP, regularisasi).
- High-resolution classifier (fine-tune 448x448).
- Anchor box via dimension clusters (k-means, jarak IoU).
- Direct location prediction (sigmoid pada offset sel).
- Pelatihan multi-skala (input 320-608) untuk ketahanan skala.
- WordTree + joint training deteksi/klasifikasi (9000+ kelas).

## Kontribusi Utama
1. Anchor berbasis clustering + prediksi lokasi langsung yang stabil.
2. Darknet-19 sebagai backbone cepat dan akurat.
3. Pelatihan multi-skala dalam satu model.
4. WordTree untuk deteksi 9000+ kategori.

## Rincian Eksperimen
Diuji pada PASCAL VOC dan COCO untuk deteksi, serta ImageNet untuk evaluasi YOLO9000 pada kategori tanpa label kotak, dengan analisis kontribusi tiap peningkatan (ablation).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| PASCAL VOC 2007 | mAP / FPS | 76.8% mAP @67 FPS (fleksibel via multi-skala) |
| COCO | mAP | kompetitif untuk detektor real-time |
| ImageNet (9000) | deteksi | YOLO9000 mendeteksi 9418 kategori |

## Temuan Kunci
- Anchor via clustering lebih baik daripada anchor manual.
- Pelatihan multi-skala memberi trade-off kecepatan-akurasi fleksibel.
- Joint training memperluas kosakata deteksi drastis.
- Batch norm + resolusi tinggi menaikkan mAP signifikan.

## Keunggulan
- Akurasi dan recall jauh lebih baik dari YOLOv1.
- Fleksibel skala (satu model banyak resolusi).
- Skalabilitas kelas ekstrem via WordTree.

## Keterbatasan
- Deteksi 9000 kelas masih jauh di bawah akurasi kelas berlabel penuh.
- Objek kecil tetap menantang.
- WordTree bergantung kualitas hierarki label.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Menetapkan anchor box dan pelatihan multi-skala sebagai komponen standar YOLO yang diwarisi versi-versi berikutnya; relevan sebagai batu loncatan evolusi arsitektur yang dipakai pada pipeline RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)
- [003 - 2018 - YOLOv3 - Fondasi RGB](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)
- [004 - 2020 - YOLOv4 - Fondasi RGB](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)
- [005 - 2021 - YOLOX - Fondasi RGB](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)
- [006 - 2022 - YOLOv6 - Fondasi RGB](./006%20-%202022%20-%20YOLOv6%20-%20Fondasi%20RGB.md)
- [007 - 2023 - YOLOv7 - Fondasi RGB](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md)
- [008 - 2024 - YOLOv9 - Fondasi RGB](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md)
- [009 - 2024 - YOLOv10 - Fondasi RGB](./009%20-%202024%20-%20YOLOv10%20-%20Fondasi%20RGB.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Fondasi RGB** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Fondasi RGB)
Istilah penting untuk memahami makalah ini:

- **Bounding box** — Kotak pembatas yang melingkupi objek; (x,y,w,h) atau (x1,y1,x2,y2).
- **Anchor box** — Kotak acuan berukuran/rasio tetap tempat jaringan meregresi offset objek.
- **Anchor-free** — Deteksi tanpa anchor; memprediksi pusat/keypoint atau jarak ke sisi box.
- **mAP** — mean Average Precision; rata-rata AP lintas kelas/ambang IoU.
- **IoU** — Intersection over Union; rasio irisan/gabungan dua box.
- **NMS** — Non-Maximum Suppression; membuang deteksi berlebih yang tumpang tindih.
- **Backbone** — Jaringan ekstraksi fitur (ResNet, CSPDarknet) di awal detektor.
- **Neck** — Modul agregasi fitur multi-skala (FPN, PAN, BiFPN).
- **Head** — Bagian akhir yang menghasilkan prediksi kelas dan box.
- **One-stage vs two-stage** — Satu-tahap (YOLO/SSD) langsung; dua-tahap (Faster R-CNN) pakai proposal.
- **FLOPs** — Floating-point operations; ukuran biaya komputasi.
- **Attention/Transformer** — Mekanisme membobot relasi antar-token/fitur secara global.

## Checklist Verifikasi Manual
Centang saat memeriksa berkas ini terhadap makalah asli:

- [ ] Judul, tahun, dan venue di berkas ini cocok dengan makalah asli (buka tautan).
- [ ] Nama penulis sesuai (perhatikan entri yang memakai 'others'/dkk.).
- [ ] Klaim metode/arsitektur di bagian Metodologi sesuai isi makalah.
- [ ] Dataset yang disebut pada bagian Eksperimen benar dipakai makalah.
- [ ] Metrik & angka hasil (bila tercantum) sesuai tabel makalah asli.
- [ ] Daftar Kontribusi mencerminkan klaim penulis, bukan tafsir berlebih.
- [ ] Bagian Keterbatasan wajar (sebagian dapat berupa inferensi, bukan pernyataan penulis).
- [ ] Tautan arXiv/DOI/Scholar benar mengarah ke makalah yang dimaksud.
- [ ] Relevansi terhadap tema (YOLO/RGB/RGB-D) masuk akal untuk kebutuhan Anda.
- [ ] Jenis publikasi (jurnal/konferensi/preprint) sesuai kebutuhan sitasi Anda.
- [ ] Tahun publikasi berada pada rentang fokus tinjauan (2019-2026) atau merupakan karya fondasi yang dirujuk.
- [ ] Kode/sumber terbuka (bila ada) tersedia dan dapat direproduksi.

## Pertanyaan Telaah Kritis
Gunakan pertanyaan berikut untuk menilai kualitas dan kecocokan makalah bagi riset Anda:

- Apa gap/celah spesifik yang membedakan makalah ini dari karya sebelumnya?
- Apakah klaim kinerja didukung ablation study (uji komponen) yang memadai?
- Seberapa adil baseline pembanding (dataset, resolusi, dan anggaran komputasi setara)?
- Apakah metrik yang dipakai tepat untuk tugasnya (mis. mAP untuk deteksi, mIoU untuk segmentasi, AbsRel untuk depth)?
- Bagaimana generalisasi metode ke domain/dataset lain di luar yang diuji?
- Apakah biaya komputasi (parameter, FLOPs, FPS) dilaporkan dan realistis untuk penerapan Anda?

## Kesimpulan
YOLOv2/YOLO9000 menaikkan akurasi dan skala kosakata deteksi secara bersamaan, menegaskan anchor berbasis data dan pelatihan multi-skala sebagai praktik baku yang bertahan pada generasi YOLO selanjutnya.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `redmon2017yolo9000` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 002/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
