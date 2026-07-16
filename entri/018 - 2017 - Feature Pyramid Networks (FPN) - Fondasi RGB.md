# 018 - Feature Pyramid Networks for Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 018 dari 154 |
| Kunci BibTeX | `lin2017fpn` |
| Judul | Feature Pyramid Networks for Object Detection |
| Penulis | Lin, Tsung-Yi; Doll{\'a |
| Tahun | 2017 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | FPN, piramida fitur, top-down, koneksi lateral, multi-skala |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Feature%20Pyramid%20Networks%20for%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Feature%20Pyramid%20Networks%20for%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 2117--2125 |

## Ringkasan Eksekutif
Membangun piramida fitur bermakna semantik di semua skala melalui jalur top-down dan koneksi lateral, meningkatkan deteksi objek multi-skala secara hemat komputasi.

## Abstrak (Parafrase)
FPN mengatasi dilema bahwa fitur beresolusi tinggi minim semantik sedangkan fitur dalam kaya semantik namun beresolusi rendah. Dengan menambahkan jalur top-down yang menyalurkan semantik dari level tinggi ke rendah dan koneksi lateral yang menggabungkannya dengan fitur beresolusi tinggi, FPN menghasilkan piramida fitur kaya-semantik di semua level dengan tambahan biaya minimal.

## Latar Belakang & Konteks
Deteksi objek multi-skala, khususnya objek kecil, sulit karena tidak ada representasi yang sekaligus beresolusi tinggi dan kaya semantik. Piramida citra mahal, sedangkan prediksi multi-skala terpisah kurang optimal.

## Permasalahan yang Diangkat
- Fitur resolusi tinggi minim semantik.
- Fitur dalam minim resolusi untuk objek kecil.
- Piramida citra mahal secara komputasi.
- Prediksi multi-skala terpisah tak berbagi semantik.
- Objek kecil sulit dideteksi.

## Tujuan & Pertanyaan Penelitian
- Membangun piramida fitur kaya-semantik di semua skala.
- Menyalurkan semantik top-down secara hemat.
- Meningkatkan deteksi objek multi-skala.

## Tinjauan Terdahulu / Posisi Literatur
FPN memperbaiki piramida citra dan prediksi multi-skala terpisah dengan arsitektur top-down + lateral yang dapat dipasang pada RPN/Fast R-CNN.

Karya/konsep pembanding yang relevan:

- Piramida citra — pendekatan mahal sebelumnya.
- Prediksi multi-skala (SSD) — tanpa berbagi semantik.
- U-Net/hourglass — arsitektur top-down terkait.
- Faster R-CNN — kerangka yang ditingkatkan.

## Metodologi & Arsitektur
Jalur bottom-up (backbone) menghasilkan fitur multi-level; jalur top-down mengupsample fitur semantik tinggi; koneksi lateral (1x1 conv) menggabungkan dengan fitur bottom-up beresolusi sama; hasilnya piramida P2-P6 untuk prediksi. Dipasang sebagai neck ke RPN dan head.

Komponen / langkah metodologis utama:

- Jalur bottom-up (backbone standar).
- Jalur top-down (upsample semantik).
- Koneksi lateral (1x1 conv) menggabungkan level.
- Prediksi pada tiap level piramida.
- Plug-in ke RPN/Fast R-CNN.
- Biaya tambahan minimal.

## Kontribusi Utama
1. Piramida fitur kaya-semantik di semua skala.
2. Peningkatan konsisten, terutama objek kecil.
3. Hemat komputasi (tambahan minimal).
4. Menjadi neck standar detektor modern.

## Rincian Eksperimen
Diuji di COCO sebagai neck untuk RPN dan Fast R-CNN, dengan analisis peningkatan per ukuran objek (terutama kecil).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP | peningkatan konsisten sebagai neck |
| COCO (objek kecil) | AP-S | peningkatan terbesar |
| Proposal (RPN) | recall | recall multi-skala meningkat |

## Temuan Kunci
- Top-down + lateral menghasilkan semantik multi-skala.
- Objek kecil paling diuntungkan.
- Biaya komputasi kecil untuk gain besar.
- Menjadi komponen standar (PAN/BiFPN turunannya).

## Keunggulan
- Sederhana dan hemat.
- Peningkatan multi-skala konsisten.
- Mudah dipasang ke banyak detektor.

## Keterbatasan
- Menambah sedikit memori/komputasi.
- Fusi penjumlahan sederhana (turunan memperbaiki).
- Desain koneksi perlu penyesuaian per-arsitektur.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Konsep piramida fitur FPN mendasari neck (PANet, BiFPN) pada hampir semua YOLO modern; fundamental untuk memahami arsitektur detektor pada tinjauan YOLO+RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)
- [002 - 2017 - YOLO9000 (YOLOv2) - Fondasi RGB](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)
- [003 - 2018 - YOLOv3 - Fondasi RGB](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)
- [004 - 2020 - YOLOv4 - Fondasi RGB](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)
- [005 - 2021 - YOLOX - Fondasi RGB](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)
- [006 - 2022 - YOLOv6 - Fondasi RGB](./006%20-%202022%20-%20YOLOv6%20-%20Fondasi%20RGB.md)
- [007 - 2023 - YOLOv7 - Fondasi RGB](./007%20-%202023%20-%20YOLOv7%20-%20Fondasi%20RGB.md)
- [008 - 2024 - YOLOv9 - Fondasi RGB](./008%20-%202024%20-%20YOLOv9%20-%20Fondasi%20RGB.md)

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
FPN menyediakan piramida fitur kaya-semantik multi-skala secara hemat, menjadi neck standar yang mendasari desain PAN/BiFPN pada detektor modern termasuk YOLO.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `lin2017fpn` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 018/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
