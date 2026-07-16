# 013 - Fast R-CNN

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 013 dari 154 |
| Kunci BibTeX | `girshick2015fastrcnn` |
| Judul | Fast R-CNN |
| Penulis | Girshick, Ross |
| Tahun | 2015 |
| Venue / Jurnal | Proceedings of the IEEE International Conference on Computer Vision (ICCV) |
| Tema klaster | Fondasi RGB |
| Kata kunci | Fast R-CNN, RoI pooling, multi-task loss, deteksi, end-to-end |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Fast%20R-CNN
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Fast%20R-CNN&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 1440--1448 |

## Ringkasan Eksekutif
Mempercepat R-CNN dengan berbagi komputasi konvolusi seluruh citra dan RoI pooling, serta menyatukan klasifikasi dan regresi box dalam satu pelatihan multi-task.

## Abstrak (Parafrase)
Fast R-CNN menghitung feature map konvolusi sekali untuk seluruh citra, lalu mengekstrak fitur tiap region proposal melalui RoI pooling ke ukuran tetap. Satu jaringan dengan dua keluaran (softmax klasifikasi dan regresi box) dilatih bersama memakai multi-task loss, menghasilkan pelatihan single-stage yang jauh lebih cepat dan lebih akurat dari R-CNN.

## Latar Belakang & Konteks
R-CNN sangat lambat karena menjalankan CNN untuk tiap region secara terpisah dan melatih CNN, SVM, serta regressor dalam tahap-tahap terpisah yang mahal dan rumit.

## Permasalahan yang Diangkat
- R-CNN menjalankan CNN per-region (sangat lambat).
- Pelatihan bertingkat (CNN/SVM/regressor) rumit dan mahal.
- Penyimpanan fitur besar diperlukan.
- Optimasi tidak end-to-end.
- Region tumpang tindih menghitung ulang konvolusi.

## Tujuan & Pertanyaan Penelitian
- Berbagi komputasi konvolusi untuk semua region.
- Menyatukan klasifikasi dan regresi dalam satu pelatihan.
- Mempercepat pelatihan dan inferensi drastis.

## Tinjauan Terdahulu / Posisi Literatur
Fast R-CNN memperbaiki R-CNN dan SPP-Net dengan RoI pooling yang dapat di-backprop dan pelatihan end-to-end (kecuali proposal).

Karya/konsep pembanding yang relevan:

- R-CNN — pendahulu langsung.
- SPP-Net — berbagi fitur via spatial pyramid pooling.
- Selective search — proposal (masih eksternal).
- Multi-task learning — gabungan klasifikasi+regresi.

## Metodologi & Arsitektur
Feature map dihitung sekali; RoI pooling memetakan tiap proposal ke fitur berukuran tetap (mis. 7x7); dua fully-connected head menghasilkan skor kelas (softmax) dan offset box (smooth L1). Loss multi-task menggabungkan keduanya; seluruh jaringan (selain proposal) dilatih end-to-end.

Komponen / langkah metodologis utama:

- Konvolusi seluruh citra dihitung sekali (berbagi fitur).
- RoI pooling ke ukuran tetap, dapat di-backprop.
- Head ganda: softmax klasifikasi + regresi box.
- Multi-task loss (klasifikasi + smooth L1).
- Pelatihan single-stage end-to-end.
- Truncated SVD untuk mempercepat FC (opsional).

## Kontribusi Utama
1. RoI pooling memungkinkan berbagi fitur dan backprop.
2. Pelatihan single-stage menggantikan pipeline bertingkat.
3. Kecepatan pelatihan/inferensi jauh meningkat.
4. Akurasi lebih tinggi dari R-CNN/SPP-Net.

## Rincian Eksperimen
Diuji pada PASCAL VOC 2007/2010/2012 dengan perbandingan kecepatan pelatihan/inferensi dan mAP terhadap R-CNN dan SPP-Net.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| PASCAL VOC 2007 | mAP | ~66-70% (naik dari R-CNN) |
| Kecepatan latih | x | ~9x lebih cepat dari R-CNN |
| Kecepatan uji | x | ratusan kali lebih cepat (tanpa proposal) |

## Temuan Kunci
- RoI pooling kunci untuk berbagi komputasi.
- Multi-task loss menyatukan tugas dan menaikkan akurasi.
- Proposal (selective search) tersisa sebagai bottleneck.
- Pelatihan end-to-end menyederhanakan pipeline.

## Keunggulan
- Jauh lebih cepat dan akurat dari R-CNN.
- Pelatihan single-stage.
- Berbagi fitur efisien.

## Keterbatasan
- Masih bergantung proposal eksternal (lambat).
- Belum sepenuhnya end-to-end (proposal terpisah).
- Belum real-time.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Fast R-CNN memperkenalkan RoI pooling dan multi-task loss yang mendasari detektor dua-tahap modern; pembanding penting bagi kecepatan YOLO pada konteks RGB-D.

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
Fast R-CNN menyederhanakan R-CNN menjadi pelatihan single-stage dengan RoI pooling dan multi-task loss, menyisakan proposal sebagai hambatan yang kemudian dijawab Faster R-CNN.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `girshick2015fastrcnn` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 013/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
