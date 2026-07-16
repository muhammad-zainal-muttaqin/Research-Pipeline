# 009 - YOLOv10: Real-Time End-to-End Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 009 dari 154 |
| Kunci BibTeX | `wang2024yolov10` |
| Judul | YOLOv10: Real-Time End-to-End Object Detection |
| Penulis | Wang, Ao; Chen, Hui; Liu, Lihao; Chen, Kai; Lin, Zijia; Han, Jungong; Ding, Guiguang |
| Tahun | 2024 |
| Venue / Jurnal | Advances in Neural Information Processing Systems (NeurIPS) |
| Tema klaster | Fondasi RGB |
| Kata kunci | YOLOv10, NMS-free, dual assignment, end-to-end, efisiensi holistik |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLOv10%3A%20Real-Time%20End-to-End%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLOv10%3A%20Real-Time%20End-to-End%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
Merealisasikan YOLO end-to-end tanpa NMS melalui pelatihan consistent dual assignments dan desain ulang komponen secara holistik, menurunkan latensi pada akurasi setara.

## Abstrak (Parafrase)
YOLOv10 menghapus kebutuhan Non-Maximum Suppression (NMS) yang selama ini menjadi hambatan latensi dan penerapan end-to-end. Caranya adalah consistent dual label assignments: cabang one-to-many untuk supervisi kaya saat pelatihan dan cabang one-to-one untuk inferensi bebas-NMS, dengan metrik pencocokan yang konsisten. Selain itu, desain holistik efisiensi-akurasi (head ringan, downsampling terpisah spasial-kanal, rank-guided block) menekan redundansi. Hasilnya latensi lebih rendah pada akurasi setara dibanding YOLOv8/v9 dan RT-DETR.

## Latar Belakang & Konteks
NMS sebagai pasca-proses menambah latensi yang bervariasi dan menyulitkan penerapan end-to-end di perangkat. Upaya sebelumnya (one-to-one assignment) sering menurunkan akurasi atau memperlambat konvergensi.

## Permasalahan yang Diangkat
- NMS menambah latensi variabel dan menghambat end-to-end.
- One-to-one assignment naif menurunkan akurasi/konvergensi.
- Komponen YOLO menyimpan redundansi komputasi.
- Head konvensional mahal secara parameter.
- Trade-off latensi-akurasi belum optimal untuk deployment.

## Tujuan & Pertanyaan Penelitian
- Menghapus NMS lewat pelatihan dual assignment konsisten.
- Merancang ulang komponen untuk efisiensi holistik.
- Menurunkan latensi tanpa mengorbankan akurasi.

## Tinjauan Terdahulu / Posisi Literatur
YOLOv10 memadukan gagasan end-to-end (DETR/one-to-one) dengan efisiensi arsitektur YOLO, mengatasi kelemahan masing-masing.

Karya/konsep pembanding yang relevan:

- DETR — deteksi end-to-end bebas NMS.
- One-to-one/one-to-many assignment — supervisi label.
- YOLOv8 — basis arsitektur.
- Rank/efficiency design — kompresi komponen.

## Metodologi & Arsitektur
Dua head berbagi backbone: one-to-many (pelatihan) dan one-to-one (inferensi) dengan matching metric konsisten agar tak konflik. Desain efisiensi: lightweight classification head, spatial-channel decoupled downsampling, rank-guided block allocation; desain akurasi: large-kernel conv dan partial self-attention (PSA).

Komponen / langkah metodologis utama:

- Consistent dual label assignment (one-to-many + one-to-one).
- Inferensi bebas NMS via cabang one-to-one.
- Spatial-channel decoupled downsampling.
- Rank-guided block design (kurangi redundansi).
- Partial self-attention (PSA) untuk akurasi.
- Head klasifikasi ringan.

## Kontribusi Utama
1. YOLO end-to-end tanpa NMS yang praktis.
2. Consistent dual assignment menjaga akurasi.
3. Desain holistik menekan latensi & parameter.
4. Trade-off latensi-akurasi lebih baik dari v8/v9/RT-DETR.

## Rincian Eksperimen
Diuji di COCO lintas skala dengan pengukuran latensi end-to-end (tanpa NMS), dibandingkan YOLOv8, YOLOv9, RT-DETR, dan PP-YOLOE.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP / latensi | latensi lebih rendah pada AP setara |
| COCO | end-to-end | bebas NMS, latensi stabil |
| Perbandingan | vs RT-DETR | lebih efisien pada akurasi mirip |

## Temuan Kunci
- Dual assignment konsisten memungkinkan bebas-NMS tanpa rugi akurasi.
- Redundansi komponen YOLO dapat ditekan signifikan.
- Latensi end-to-end menjadi stabil/terprediksi.
- PSA menambah akurasi dengan biaya kecil.

## Keunggulan
- Deteksi end-to-end tanpa NMS.
- Latensi rendah dan stabil.
- Efisiensi parameter/komputasi tinggi.

## Keterbatasan
- Manfaat bervariasi menurut skala model.
- Kompleksitas pelatihan dual-head.
- Ekosistem/tooling masih berkembang saat rilis.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
YOLOv10 mendekatkan detektor satu-tahap ke inferensi bebas pasca-proses, menguntungkan pipeline RGB-D real-time yang sensitif latensi (robotika, navigasi).

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
YOLOv10 mewujudkan YOLO end-to-end tanpa NMS melalui dual assignment konsisten dan efisiensi holistik, memperbaiki trade-off latensi-akurasi untuk deployment nyata.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wang2024yolov10` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 009/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
