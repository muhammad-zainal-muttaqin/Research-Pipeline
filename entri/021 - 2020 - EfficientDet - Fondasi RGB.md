# 021 - EfficientDet: Scalable and Efficient Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 021 dari 154 |
| Kunci BibTeX | `tan2020efficientdet` |
| Judul | EfficientDet: Scalable and Efficient Object Detection |
| Penulis | Tan, Mingxing; Pang, Ruoming; Le, Quoc V. |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | EfficientDet, BiFPN, compound scaling, EfficientNet, efisiensi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=EfficientDet%3A%20Scalable%20and%20Efficient%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=EfficientDet%3A%20Scalable%20and%20Efficient%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 10781--10790 |

## Ringkasan Eksekutif
Menggabungkan backbone EfficientNet, neck BiFPN berbobot, dan compound scaling terpadu untuk menghasilkan keluarga detektor efisien D0-D7 yang skalabel.

## Abstrak (Parafrase)
EfficientDet mengejar efisiensi tinggi melalui tiga inovasi: BiFPN (weighted Bi-directional FPN) yang menggabungkan fitur multi-skala dua-arah dengan bobot terlatih; compound scaling yang menskalakan resolusi, kedalaman, dan lebar backbone/neck/head secara terkoordinasi; serta backbone EfficientNet. Hasilnya keluarga D0-D7 mencapai akurasi tinggi dengan parameter/FLOPs jauh lebih rendah dari pesaing.

## Latar Belakang & Konteks
Detektor sulit menyeimbangkan akurasi dan efisiensi; penskalaan komponen yang tidak terkoordinasi (hanya backbone atau hanya resolusi) memberi hasil suboptimal, dan fusi FPN standar memperlakukan semua skala setara.

## Permasalahan yang Diangkat
- Penskalaan komponen tak terkoordinasi memberi hasil suboptimal.
- Fusi FPN standar memperlakukan semua input skala setara.
- Detektor akurat sering boros parameter/FLOPs.
- Kebutuhan keluarga model untuk beragam anggaran.
- Efisiensi penting untuk perangkat terbatas.

## Tujuan & Pertanyaan Penelitian
- Merancang fusi multi-skala berbobot dua-arah (BiFPN).
- Menskalakan seluruh detektor secara terkoordinasi.
- Menghasilkan keluarga detektor efisien D0-D7.

## Tinjauan Terdahulu / Posisi Literatur
EfficientDet membangun di atas EfficientNet, FPN/PANet, dan prinsip compound scaling dari EfficientNet.

Karya/konsep pembanding yang relevan:

- EfficientNet — backbone & compound scaling.
- FPN/PANet — dasar BiFPN.
- NAS-FPN — pencarian fusi (pembanding).
- Weighted fusion — bobot fitur terlatih.

## Metodologi & Arsitektur
BiFPN menambah koneksi dua-arah dan bobot terlatih (fast normalized fusion) untuk menggabungkan fitur multi-skala berulang; compound scaling memakai satu koefisien untuk menskalakan resolusi input, kedalaman BiFPN/head, dan lebar; backbone EfficientNet-B0..B6 untuk D0..D7.

Komponen / langkah metodologis utama:

- BiFPN: fusi multi-skala dua-arah berbobot, berulang.
- Fast normalized weighted fusion.
- Compound scaling (resolusi/kedalaman/lebar serentak).
- Backbone EfficientNet.
- Keluarga D0-D7 untuk beragam anggaran.
- Head klasifikasi/box bersama antar-skala.

## Kontribusi Utama
1. BiFPN sebagai fusi multi-skala berbobot efektif.
2. Compound scaling terpadu untuk detektor.
3. Keluarga D0-D7 skalabel.
4. Akurasi tinggi dengan parameter/FLOPs rendah.

## Rincian Eksperimen
Diuji di COCO lintas D0-D7 dengan analisis parameter/FLOPs vs AP, dibandingkan detektor anchor-based/free dan NAS-FPN.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP | D7 ~52-53% AP dengan FLOPs jauh lebih rendah |
| COCO | efisiensi | parameter/FLOPs jauh di bawah pesaing |
| Ablation | BiFPN/scaling | keduanya menyumbang gain |

## Temuan Kunci
- BiFPN berbobot lebih baik dari fusi setara.
- Compound scaling mengungguli penskalaan tunggal.
- Efisiensi tinggi lintas skala model.
- BiFPN diadopsi luas termasuk varian YOLO.

## Keunggulan
- Efisiensi parameter/FLOPs terbaik pada kelasnya.
- Skalabel D0-D7.
- Fusi multi-skala superior.

## Keterbatasan
- Model besar (D7) tetap berat.
- Compound scaling perlu penyetelan koefisien.
- Latensi nyata bisa berbeda dari FLOPs.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
EfficientDet menetapkan tolok ukur efisiensi dan BiFPN yang diadopsi pada beberapa neck YOLO; relevan untuk memahami trade-off efisiensi pada detektor RGB-D.

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
EfficientDet memadukan BiFPN berbobot dan compound scaling terpadu untuk keluarga detektor efisien, menetapkan tolok ukur akurasi-efisiensi dan menyumbang BiFPN ke desain detektor modern.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `tan2020efficientdet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 021/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
