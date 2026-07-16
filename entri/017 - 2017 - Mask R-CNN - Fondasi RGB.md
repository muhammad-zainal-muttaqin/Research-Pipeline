# 017 - Mask R-CNN

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 017 dari 154 |
| Kunci BibTeX | `he2017maskrcnn` |
| Judul | Mask R-CNN |
| Penulis | He, Kaiming; Gkioxari, Georgia; Doll{\'a |
| Tahun | 2017 |
| Venue / Jurnal | Proceedings of the IEEE International Conference on Computer Vision (ICCV) |
| Tema klaster | Fondasi RGB |
| Kata kunci | Mask R-CNN, instance segmentation, RoIAlign, multi-task, Faster R-CNN |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Mask%20R-CNN
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Mask%20R-CNN&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 2961--2969 |

## Ringkasan Eksekutif
Memperluas Faster R-CNN dengan cabang prediksi mask per-RoI dan RoIAlign, memungkinkan instance segmentation akurat sekaligus deteksi dalam satu kerangka serbaguna.

## Abstrak (Parafrase)
Mask R-CNN menambahkan cabang FCN kecil yang memprediksi mask biner per-RoI secara paralel dengan cabang klasifikasi dan regresi box. Kunci akurasinya adalah RoIAlign yang menggantikan RoIPool untuk menghilangkan kuantisasi/misalignment. Kerangka ini serbaguna, dapat diperluas ke estimasi keypoint/pose, dan menjadi standar instance segmentation.

## Latar Belakang & Konteks
Deteksi kotak tidak cukup untuk aplikasi yang membutuhkan bentuk objek presisi (instance segmentation). Selain itu, RoIPool pada Faster R-CNN menimbulkan misalignment yang merusak prediksi mask halus.

## Permasalahan yang Diangkat
- Deteksi kotak tak cukup untuk segmentasi per-instance.
- RoIPool menimbulkan misalignment (kuantisasi).
- Perlu prediksi mask tanpa kompetisi antar-kelas.
- Kerangka harus tetap efisien dan serbaguna.
- Perluasan ke tugas lain (keypoint) diinginkan.

## Tujuan & Pertanyaan Penelitian
- Menambah kemampuan instance segmentation.
- Menghilangkan misalignment via RoIAlign.
- Menyediakan kerangka multi-task serbaguna.

## Tinjauan Terdahulu / Posisi Literatur
Mask R-CNN membangun di atas Faster R-CNN dan mengintegrasikan FCN untuk segmentasi per-RoI.

Karya/konsep pembanding yang relevan:

- Faster R-CNN — kerangka deteksi dasar.
- FCN — jaringan segmentasi penuh.
- RoIPool — operasi yang diperbaiki jadi RoIAlign.
- FPN — neck multi-skala.

## Metodologi & Arsitektur
Setiap RoI diproses tiga cabang: klasifikasi, regresi box, dan mask (FCN kecil menghasilkan mask biner per kelas, decoupled). RoIAlign memakai interpolasi bilinear tanpa kuantisasi untuk menjaga kesejajaran spasial. Loss = klasifikasi + box + mask.

Komponen / langkah metodologis utama:

- Cabang mask paralel (FCN kecil per-RoI).
- RoIAlign (interpolasi bilinear, tanpa kuantisasi).
- Mask per-kelas decoupled dari klasifikasi.
- Multi-task loss (kelas + box + mask).
- Backbone ResNet/ResNeXt + FPN.
- Perluasan ke keypoint/pose.

## Kontribusi Utama
1. Instance segmentation akurat dalam kerangka deteksi.
2. RoIAlign menghilangkan misalignment (peningkatan besar).
3. Mask decoupled meningkatkan kualitas.
4. Serbaguna: deteksi, segmentasi, keypoint.

## Rincian Eksperimen
Diuji di COCO (instance segmentation & deteksi & keypoint) dengan ablation RoIAlign vs RoIPool dan mask decoupled.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO instance seg | AP mask | SOTA saat rilis |
| COCO deteksi | AP box | meningkat berkat RoIAlign |
| COCO keypoint | AP | generalisasi ke pose keypoint |

## Temuan Kunci
- RoIAlign krusial untuk prediksi spasial presisi.
- Mask decoupled (per-kelas) lebih baik dari multi-kelas.
- Multi-task tak saling merugikan (bahkan membantu).
- Kerangka mudah diperluas ke tugas lain.

## Keunggulan
- Akurat untuk deteksi dan segmentasi.
- RoIAlign sederhana dan berdampak.
- Serbaguna dan banyak diadopsi.

## Keterbatasan
- Dua-tahap, lebih lambat dari YOLO.
- Mask menambah biaya komputasi.
- Butuh anotasi mask untuk pelatihan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Mask R-CNN sering dipakai memberi mask objek pada pipeline RGB-D dan SLAM dinamis (mis. DynaSLAM) dalam tinjauan ini, sehingga relevan untuk memahami komponen segmentasi.

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
Mask R-CNN memperluas Faster R-CNN ke instance segmentation via RoIAlign dan cabang mask, menjadi kerangka serbaguna yang banyak dipakai lintas tugas termasuk RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `he2017maskrcnn` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 017/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
