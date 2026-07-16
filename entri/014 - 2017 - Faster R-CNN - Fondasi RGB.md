# 014 - Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 014 dari 154 |
| Kunci BibTeX | `ren2017fasterrcnn` |
| Judul | Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks |
| Penulis | Ren, Shaoqing; He, Kaiming; Girshick, Ross; Sun, Jian |
| Tahun | 2017 |
| Venue / Jurnal | IEEE Transactions on Pattern Analysis and Machine Intelligence |
| Tema klaster | Fondasi RGB |
| Kata kunci | Faster R-CNN, RPN, anchor, dua-tahap, region proposal |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Faster%20R-CNN%3A%20Towards%20Real-Time%20Object%20Detection%20with%20Region%20Proposal%20Networks
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Faster%20R-CNN%3A%20Towards%20Real-Time%20Object%20Detection%20with%20Region%20Proposal%20Networks&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 39 |
| Nomor | 6 |
| Halaman | 1137--1149 |

## Ringkasan Eksekutif
Memperkenalkan Region Proposal Network yang berbagi fitur dengan detektor sehingga proposal nyaris gratis, menjadikan deteksi dua-tahap mendekati real-time dan menetapkan paradigma anchor.

## Abstrak (Parafrase)
Faster R-CNN menyatukan proposal ke dalam jaringan lewat Region Proposal Network (RPN) yang berbagi backbone dengan detektor Fast R-CNN. RPN memprediksi objectness dan offset box dari sekumpulan anchor berukuran/rasio tetap di tiap lokasi feature map. Proposal berkualitas dihasilkan hampir tanpa biaya tambahan, menjadikan sistem akurat dan jauh lebih cepat.

## Latar Belakang & Konteks
Fast R-CNN masih memakai selective search yang menjadi bottleneck kecepatan. Diperlukan mekanisme proposal yang cepat, dapat dilatih, dan berbagi komputasi dengan detektor.

## Permasalahan yang Diangkat
- Selective search menjadi bottleneck kecepatan Fast R-CNN.
- Proposal eksternal tak dapat dioptimalkan bersama detektor.
- Perlu proposal berkualitas dengan biaya minimal.
- Objek multi-skala/rasio perlu ditangani proposal.
- Pelatihan berbagi fitur antara proposal dan deteksi.

## Tujuan & Pertanyaan Penelitian
- Mengintegrasikan proposal ke dalam jaringan (RPN).
- Berbagi fitur antara proposal dan deteksi.
- Mencapai deteksi dua-tahap mendekati real-time.

## Tinjauan Terdahulu / Posisi Literatur
Faster R-CNN menggantikan selective search dengan RPN berbasis anchor terintegrasi, membangun di atas Fast R-CNN.

Karya/konsep pembanding yang relevan:

- Fast R-CNN — detektor dasar.
- Selective search — proposal yang digantikan.
- Anchor box — konsep yang diperkenalkan.
- Multi-task loss — klasifikasi+regresi.

## Metodologi & Arsitektur
RPN meluncur di atas feature map bersama, memprediksi objectness dan offset untuk k anchor per lokasi (beragam skala/rasio); proposal teratas diteruskan ke RoI pooling + head Fast R-CNN. Pelatihan memakai skema bergantian atau approximate joint training.

Komponen / langkah metodologis utama:

- RPN memprediksi objectness + offset dari anchor.
- Anchor multi-skala/rasio di tiap lokasi.
- Berbagi backbone antara RPN dan detektor.
- RoI pooling + head klasifikasi/regresi.
- Pelatihan alternating / approximate joint.
- NMS pada proposal dan deteksi akhir.

## Kontribusi Utama
1. RPN menghasilkan proposal cepat dan berbagi fitur.
2. Menetapkan paradigma anchor yang berpengaruh luas.
3. Deteksi dua-tahap mendekati real-time (~5-17 FPS).
4. Menjadi standar detektor dua-tahap.

## Rincian Eksperimen
Diuji pada PASCAL VOC dan COCO dengan analisis kualitas proposal (recall) dan mAP/kecepatan terhadap Fast R-CNN + selective search.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| PASCAL VOC 2007 | mAP | ~73-76% dengan VGG/ResNet |
| COCO | mAP | baseline dua-tahap kuat |
| Kecepatan | FPS | ~5-17 FPS (jauh > selective search) |

## Temuan Kunci
- RPN membuat proposal nyaris gratis dan dapat dilatih.
- Anchor menangani objek multi-skala/rasio.
- Berbagi fitur kunci untuk kecepatan.
- Kualitas proposal (recall) tinggi menaikkan mAP.

## Keunggulan
- Akurat dan menjadi standar dua-tahap.
- Proposal terintegrasi dan cepat.
- Fleksibel dengan berbagai backbone.

## Keterbatasan
- Masih lebih lambat dari detektor satu-tahap.
- Anchor menambah hyperparameter.
- Dua-tahap lebih kompleks dari YOLO.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Faster R-CNN adalah baseline dua-tahap utama pembanding YOLO dan sering dipakai (dengan RGB-D) pada aplikasi seperti deteksi apel berdaun lebat dalam tinjauan ini.

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
Faster R-CNN menetapkan RPN dan paradigma anchor, menjadikan deteksi dua-tahap akurat dan mendekati real-time serta baseline pembanding utama bagi detektor satu-tahap.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ren2017fasterrcnn` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 014/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
