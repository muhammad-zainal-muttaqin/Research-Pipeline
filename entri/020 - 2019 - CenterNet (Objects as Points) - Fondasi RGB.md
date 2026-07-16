# 020 - Objects as Points

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 020 dari 154 |
| Kunci BibTeX | `zhou2019objects` |
| Judul | Objects as Points |
| Penulis | Zhou, Xingyi; Wang, Dequan; Kr{\"a |
| Tahun | 2019 |
| Venue / Jurnal | arXiv preprint arXiv:1904.07850 |
| Tema klaster | Fondasi RGB |
| Kata kunci | CenterNet, point-based, heatmap, anchor-free, NMS-free |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/1904.07850
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Objects%20as%20Points
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Objects%20as%20Points&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 1904.07850 |

## Ringkasan Eksekutif
Merepresentasikan objek sebagai titik pusat via heatmap lalu meregresi atribut (ukuran, offset, bahkan 3D/pose) langsung dari fitur pusat, tanpa anchor maupun NMS.

## Abstrak (Parafrase)
CenterNet (Objects as Points) memandang objek sebagai satu titik: pusat kotaknya. Jaringan menghasilkan heatmap puncak untuk pusat objek tiap kelas, lalu meregresi ukuran box, offset sub-piksel, dan atribut lain (kedalaman, orientasi 3D, pose) langsung dari fitur di lokasi puncak. Karena puncak lokal unik, NMS tidak diperlukan, menghasilkan pipeline sederhana, cepat, dan serbaguna.

## Latar Belakang & Konteks
Pipeline berbasis box/anchor memerlukan enumerasi banyak kandidat dan NMS pasca-proses yang rumit. Representasi objek sebagai titik menjanjikan penyederhanaan besar.

## Permasalahan yang Diangkat
- Enumerasi anchor/box banyak dan boros.
- NMS pasca-proses menambah kompleksitas/latensi.
- Perluasan ke 3D/pose sulit pada kerangka box.
- Ketidakseimbangan positif-negatif pada anchor.
- Perlu representasi objek yang ringkas dan serbaguna.

## Tujuan & Pertanyaan Penelitian
- Merepresentasikan objek sebagai titik pusat (heatmap).
- Menghapus anchor dan NMS.
- Menyediakan kerangka serbaguna (2D/3D/pose).

## Tinjauan Terdahulu / Posisi Literatur
CenterNet terinspirasi estimasi keypoint (CornerNet) dan deteksi anchor-free, memakai backbone penghasil heatmap resolusi tinggi.

Karya/konsep pembanding yang relevan:

- CornerNet — deteksi berbasis keypoint sudut.
- Hourglass/DLA — backbone heatmap.
- Estimasi pose keypoint — inspirasi representasi titik.
- Anchor-free — paradigma umum.

## Metodologi & Arsitektur
Backbone (Hourglass/DLA/ResNet) menghasilkan heatmap pusat per kelas; puncak lokal (via max-pooling 3x3) menjadi deteksi; cabang regresi memprediksi ukuran box dan offset sub-piksel dari fitur pusat; perluasan menambah cabang kedalaman/orientasi/pose. Tanpa NMS.

Komponen / langkah metodologis utama:

- Heatmap puncak untuk pusat objek per-kelas.
- Ekstraksi puncak via max-pooling (pengganti NMS).
- Regresi ukuran box & offset dari fitur pusat.
- Cabang tambahan untuk 3D/orientasi/pose.
- Backbone resolusi tinggi (Hourglass/DLA).
- Focal-style loss pada heatmap.

## Kontribusi Utama
1. Representasi point-based sederhana dan cepat.
2. Menghapus anchor dan NMS.
3. Serbaguna: 2D, 3D, pose keypoint dalam satu kerangka.
4. Trade-off kecepatan-akurasi kuat.

## Rincian Eksperimen
Diuji di COCO (deteksi 2D & pose) dan KITTI/nuScenes (3D) dengan berbagai backbone, dibandingkan detektor anchor-based dan CornerNet.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP / FPS | hingga ~45.1% AP; trade-off cepat-akurat |
| COCO keypoint | AP | estimasi pose multi-orang |
| KITTI/3D | AP | perluasan deteksi 3D monokular |

## Temuan Kunci
- Objek sebagai titik menyederhanakan deteksi.
- Tanpa NMS mempercepat & menyederhanakan pipeline.
- Serbaguna lintas tugas (2D/3D/pose).
- Backbone resolusi tinggi penting untuk heatmap.

## Keunggulan
- Sederhana dan cepat.
- Tanpa anchor/NMS.
- Sangat serbaguna.

## Keterbatasan
- Objek sangat berdekatan bisa berbagi puncak.
- Butuh backbone resolusi tinggi (mahal).
- Akurasi puncak sensitif terhadap resolusi heatmap.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Paradigma point-based CenterNet relevan untuk deteksi 3D berbasis kamera (RGB-D) dan estimasi pose; menghubungkan deteksi 2D dengan atribut 3D dari fitur pusat.

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
CenterNet merepresentasikan objek sebagai titik pusat pada heatmap, menghapus anchor/NMS dan menawarkan kerangka deteksi 2D/3D/pose yang sederhana, cepat, dan serbaguna.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhou2019objects` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 020/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
