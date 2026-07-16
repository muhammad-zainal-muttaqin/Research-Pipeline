# 007 - YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object Detectors

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 007 dari 154 |
| Kunci BibTeX | `wang2023yolov7` |
| Judul | YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object Detectors |
| Penulis | Wang, Chien-Yao; Bochkovskiy, Alexey; Liao, Hong-Yuan Mark |
| Tahun | 2023 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | YOLOv7, E-ELAN, reparameterisasi terencana, deep supervision, real-time |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLOv7%3A%20Trainable%20Bag-of-Freebies%20Sets%20New%20State-of-the-Art%20for%20Real-Time%20Object%20Detectors
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLOv7%3A%20Trainable%20Bag-of-Freebies%20Sets%20New%20State-of-the-Art%20for%20Real-Time%20Object%20Detectors&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 7464--7475 |

## Ringkasan Eksekutif
Detektor real-time terkuat pada masanya yang memperkenalkan E-ELAN dan strategi trainable Bag-of-Freebies termasuk reparameterisasi terencana serta penetapan label coarse-to-fine dengan lead/auxiliary head.

## Abstrak (Parafrase)
YOLOv7 berfokus pada 'trainable bag-of-freebies': teknik yang menaikkan akurasi tanpa menambah biaya inferensi. Inti arsitekturnya adalah E-ELAN (Extended Efficient Layer Aggregation Network) yang mengontrol panjang jalur gradien untuk pembelajaran fitur efisien, ditambah reparameterisasi terencana (planned re-parameterized convolution) dan penetapan label coarse-to-fine yang memakai lead head dan auxiliary head (deep supervision). Hasilnya mengungguli detektor real-time 5-160 FPS pada saat rilis.

## Latar Belakang & Konteks
Meningkatkan akurasi detektor real-time tanpa menaikkan latensi inferensi adalah tantangan utama. Reparameterisasi dan deep supervision menjanjikan namun penerapannya harus 'terencana' agar tidak merusak struktur atau gradien.

## Permasalahan yang Diangkat
- Menaikkan akurasi tanpa menambah biaya inferensi itu sulit.
- Reparameterisasi naif dapat merusak koneksi residual/konkatenasi.
- Deep supervision membutuhkan penetapan label yang tepat.
- Agregasi fitur perlu efisien dari sisi gradien.
- Skalabilitas model untuk beragam kebutuhan.

## Tujuan & Pertanyaan Penelitian
- Merancang agregasi fitur efisien (E-ELAN).
- Menerapkan reparameterisasi yang 'terencana' dan aman.
- Menyediakan penetapan label coarse-to-fine untuk lead/aux head.

## Tinjauan Terdahulu / Posisi Literatur
YOLOv7 mengembangkan ELAN dan model scaling, mengintegrasikan reparameterisasi (RepConv) secara terencana, serta memakai deep supervision melalui auxiliary head.

Karya/konsep pembanding yang relevan:

- ELAN — agregasi lapisan efisien.
- RepVGG/RepConv — reparameterisasi.
- Deep supervision — auxiliary head.
- Model scaling — penskalaan gabungan.

## Metodologi & Arsitektur
E-ELAN mengatur cardinality dan panjang jalur gradien; reparameterisasi terencana menyesuaikan RepConv agar kompatibel dengan koneksi identitas; penetapan label coarse-to-fine menghasilkan label lembut untuk auxiliary head dan label halus untuk lead head; penskalaan compound untuk model berbasis konkatenasi.

Komponen / langkah metodologis utama:

- E-ELAN untuk agregasi fitur dan aliran gradien efisien.
- Planned re-parameterized convolution.
- Coarse-to-fine lead/auxiliary head label assignment.
- Compound scaling untuk model konkatenasi.
- Bag-of-Freebies yang dapat dilatih.
- Head deteksi gaya YOLO multi-skala.

## Kontribusi Utama
1. E-ELAN sebagai blok agregasi efisien-gradien.
2. Reparameterisasi terencana yang aman terhadap residual.
3. Coarse-to-fine label assignment untuk deep supervision.
4. SOTA real-time 5-160 FPS saat rilis.

## Rincian Eksperimen
Diuji di COCO dengan pengukuran kecepatan pada V100, dibandingkan YOLOR, YOLOX, YOLOv5, dan detektor Transformer, disertai ablation E-ELAN dan reparameterisasi.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP | hingga ~56.8% AP untuk model besar |
| COCO | AP/FPS | mengungguli detektor real-time sezaman |
| Ablation | E-ELAN/RepConv | tiap komponen menyumbang gain |

## Temuan Kunci
- Trainable BoF menaikkan akurasi tanpa biaya inferensi.
- E-ELAN penting untuk efisiensi gradien.
- Reparameterisasi harus terencana agar tak merusak struktur.
- Deep supervision efektif dengan label coarse-to-fine.

## Keunggulan
- SOTA real-time pada masanya.
- Peningkatan tanpa menambah latensi.
- Desain agregasi & reparameterisasi yang matang.

## Keterbatasan
- Kompleksitas strategi pelatihan.
- Masih berbasis anchor pada rilis awal.
- Sensitif terhadap konfigurasi reparameterisasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
YOLOv7 menjadi tulang punggung banyak sistem deteksi 2023-an, termasuk yang dipadukan dengan depth; memahaminya penting untuk menilai pipeline YOLO+RGB-D mutakhir.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)
- [002 - 2017 - YOLO9000 (YOLOv2) - Fondasi RGB](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)
- [003 - 2018 - YOLOv3 - Fondasi RGB](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)
- [004 - 2020 - YOLOv4 - Fondasi RGB](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)
- [005 - 2021 - YOLOX - Fondasi RGB](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)
- [006 - 2022 - YOLOv6 - Fondasi RGB](./006%20-%202022%20-%20YOLOv6%20-%20Fondasi%20RGB.md)
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
YOLOv7 memperkuat peran reparameterisasi terencana dan agregasi efisien (E-ELAN), menjadikannya salah satu detektor real-time terkuat yang banyak diadopsi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wang2023yolov7` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 007/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
