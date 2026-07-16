# 006 - YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 006 dari 154 |
| Kunci BibTeX | `li2022yolov6` |
| Judul | YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications |
| Penulis | Li, Chuyi; Li, Lulu; Jiang, Hongliang; Weng, Kaiheng; Geng, Yifei; Li, Liang; Ke, Zaidan; Li, Qingyuan; Cheng, Meng; Nie, Weiqiang; others |
| Tahun | 2022 |
| Venue / Jurnal | arXiv preprint arXiv:2209.02976 |
| Tema klaster | Fondasi RGB |
| Kata kunci | YOLOv6, EfficientRep, reparameterisasi, kuantisasi, industri |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2209.02976
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLOv6%3A%20A%20Single-Stage%20Object%20Detection%20Framework%20for%20Industrial%20Applications
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLOv6%3A%20A%20Single-Stage%20Object%20Detection%20Framework%20for%20Industrial%20Applications&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2209.02976 |

## Ringkasan Eksekutif
Detektor YOLO berorientasi industri dengan backbone reparameterisasi (EfficientRep), head decoupled efisien, serta dukungan distilasi dan kuantisasi untuk penerapan pada perangkat nyata.

## Abstrak (Parafrase)
YOLOv6 (Meituan) dirancang khusus untuk aplikasi industri, menekankan keseimbangan latensi-akurasi dan kemudahan deployment. Ia memakai backbone EfficientRep berbasis RepVGG (reparameterisasi struktural), neck Rep-PAN, head decoupled anchor-free yang efisien, fungsi loss SIoU/GIoU, self-distillation, serta jalur kuantisasi (quantization-aware training) agar model dapat berjalan cepat di GPU maupun perangkat tepi.

## Latar Belakang & Konteks
Kebutuhan industri berbeda dari akademik: latensi harus rendah pada perangkat spesifik, model harus mudah dikuantisasi dan diterapkan, serta stabil dilatih. Detektor akademik tak selalu optimal untuk kendala-kendala ini.

## Permasalahan yang Diangkat
- Latensi-akurasi belum optimal untuk deployment industri.
- Kuantisasi sering menurunkan akurasi drastis.
- Kompleksitas arsitektur menyulitkan penerapan tepi.
- Head/loss belum efisien untuk perangkat terbatas.
- Kebutuhan skala model beragam (N/S/M/L).

## Tujuan & Pertanyaan Penelitian
- Mengoptimalkan latensi-akurasi untuk industri.
- Menyediakan jalur kuantisasi tanpa rugi akurasi besar.
- Menawarkan keluarga skala model untuk beragam perangkat.

## Tinjauan Terdahulu / Posisi Literatur
YOLOv6 mengadopsi reparameterisasi RepVGG dan desain anchor-free modern, menempatkan diri sebagai penerus praktis lini YOLOv5 untuk industri.

Karya/konsep pembanding yang relevan:

- RepVGG — reparameterisasi struktural inferensi.
- YOLOX/anchor-free — desain head.
- Knowledge distillation — self-distillation.
- Quantization-aware training — deployment efisien.

## Metodologi & Arsitektur
EfficientRep (RepBlock) melatih dengan cabang ganda lalu meleburnya ke konvolusi tunggal saat inferensi; Rep-PAN sebagai neck; head decoupled anchor-free memprediksi kelas dan box; SIoU loss mempercepat konvergensi; self-distillation dan QAT menjaga akurasi pasca-kuantisasi.

Komponen / langkah metodologis utama:

- Backbone EfficientRep (RepVGG-style, reparameterisasi).
- Neck Rep-PAN.
- Head decoupled anchor-free efisien.
- SIoU/GIoU loss.
- Self-distillation.
- Quantization-aware training untuk INT8.

## Kontribusi Utama
1. Detektor YOLO yang dioptimalkan penuh untuk industri.
2. Reparameterisasi menyeimbangkan pelatihan-inferensi.
3. Dukungan kuantisasi INT8 dengan rugi akurasi minimal.
4. Keluarga skala N/S/M/L untuk beragam perangkat.

## Rincian Eksperimen
Diuji di COCO lintas skala model dengan pengukuran latensi pada GPU (T4) dan analisis akurasi pasca-kuantisasi, dibandingkan YOLOv5/YOLOX/PP-YOLOE.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP / latensi | trade-off latensi-akurasi kompetitif per skala |
| COCO (INT8) | AP | rugi akurasi kecil setelah kuantisasi |
| Perangkat tepi | FPS | dioptimalkan untuk deployment nyata |

## Temuan Kunci
- Reparameterisasi kunci untuk kecepatan inferensi.
- QAT memungkinkan INT8 tanpa penurunan besar.
- Head/loss efisien menaikkan trade-off.
- Orientasi industri terbukti pada latensi nyata.

## Keunggulan
- Fokus deployment dan kuantisasi yang matang.
- Skalabilitas perangkat luas.
- Pelatihan stabil dan praktis.

## Keterbatasan
- Peningkatan bersifat rekayasa/deployment, bukan paradigma.
- Bergantung dukungan pustaka reparameterisasi/kuantisasi.
- Perbandingan adil antar-versi sensitif terhadap setup.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
YOLOv6 relevan untuk aplikasi industri RGB (deteksi cacat) pada tinjauan ini dan menjadi contoh bagaimana YOLO dioptimalkan untuk deployment tepi yang juga penting bagi sistem RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [001 - 2016 - You Only Look Once (YOLOv1) - Fondasi RGB](./001%20-%202016%20-%20You%20Only%20Look%20Once%20%28YOLOv1%29%20-%20Fondasi%20RGB.md)
- [002 - 2017 - YOLO9000 (YOLOv2) - Fondasi RGB](./002%20-%202017%20-%20YOLO9000%20%28YOLOv2%29%20-%20Fondasi%20RGB.md)
- [003 - 2018 - YOLOv3 - Fondasi RGB](./003%20-%202018%20-%20YOLOv3%20-%20Fondasi%20RGB.md)
- [004 - 2020 - YOLOv4 - Fondasi RGB](./004%20-%202020%20-%20YOLOv4%20-%20Fondasi%20RGB.md)
- [005 - 2021 - YOLOX - Fondasi RGB](./005%20-%202021%20-%20YOLOX%20-%20Fondasi%20RGB.md)
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
YOLOv6 menegaskan orientasi deployment industri pada silsilah YOLO melalui reparameterisasi, head/loss efisien, dan kuantisasi, memperluas kepraktisan YOLO ke perangkat nyata.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `li2022yolov6` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 006/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
