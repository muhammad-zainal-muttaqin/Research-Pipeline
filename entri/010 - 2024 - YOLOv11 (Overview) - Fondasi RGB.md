# 010 - YOLOv11: An Overview of the Key Architectural Enhancements

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 010 dari 154 |
| Kunci BibTeX | `khanam2024yolov11` |
| Judul | YOLOv11: An Overview of the Key Architectural Enhancements |
| Penulis | Khanam, Rahima; Hussain, Muhammad |
| Tahun | 2024 |
| Venue / Jurnal | arXiv preprint arXiv:2410.17725 |
| Tema klaster | Fondasi RGB |
| Kata kunci | YOLOv11, C3k2, C2PSA, multi-tugas, Ultralytics |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2410.17725
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLOv11%3A%20An%20Overview%20of%20the%20Key%20Architectural%20Enhancements
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLOv11%3A%20An%20Overview%20of%20the%20Key%20Architectural%20Enhancements&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2410.17725 |

## Ringkasan Eksekutif
Tinjauan ringkas peningkatan arsitektural YOLOv11 (Ultralytics) yang memperkenalkan blok C3k2 dan modul attention C2PSA serta dukungan multi-tugas dalam satu kerangka.

## Abstrak (Parafrase)
Makalah ini merangkum peningkatan kunci YOLOv11: penggantian blok C2f dengan C3k2 yang lebih efisien, penambahan modul C2PSA (Cross Stage Partial with Spatial Attention) untuk memperkuat fitur secara spasial, serta head yang dioptimalkan. YOLOv11 mendukung deteksi, segmentasi instance, estimasi pose, klasifikasi, dan oriented bounding box (OBB) dalam satu kerangka, dengan klaim peningkatan mAP pada parameter lebih sedikit dibanding YOLOv8.

## Latar Belakang & Konteks
Perkembangan YOLO sangat cepat sehingga praktisi memerlukan peta ringkas perubahan arsitektural tiap versi. YOLOv11 sebagai rilis Ultralytics membawa sejumlah blok baru yang perlu dipahami relatif terhadap YOLOv8-v10.

## Permasalahan yang Diangkat
- Perubahan antar-versi YOLO cepat dan sulit dilacak.
- Perlu ringkasan arsitektural yang jelas untuk praktisi.
- Integrasi attention pada YOLO perlu dipetakan.
- Kebutuhan satu kerangka multi-tugas.
- Klaim efisiensi perlu konteks pembanding.

## Tujuan & Pertanyaan Penelitian
- Merangkum perubahan arsitektural kunci YOLOv11.
- Menjelaskan peran blok C3k2 dan C2PSA.
- Memetakan dukungan multi-tugas.

## Tinjauan Terdahulu / Posisi Literatur
Sebagai tinjauan, makalah ini merangkum lini YOLOv8-v10 dan komponen attention/efisiensi terkini untuk memposisikan YOLOv11.

Karya/konsep pembanding yang relevan:

- YOLOv8 — basis (blok C2f).
- Attention spasial/PSA — komponen C2PSA.
- CSP design — dasar C3k2.
- Ultralytics framework — implementasi multi-tugas.

## Metodologi & Arsitektur
Ulasan menjelaskan penggantian C2f->C3k2 (kernel lebih kecil, efisiensi), penambahan C2PSA untuk attention spasial, serta head yang disempurnakan; menampilkan konfigurasi skala model (n/s/m/l/x) dan cakupan tugas.

Komponen / langkah metodologis utama:

- Blok C3k2 menggantikan C2f (efisiensi).
- Modul C2PSA (spatial attention) memperkuat fitur.
- Head deteksi yang dioptimalkan.
- Dukungan deteksi/segmentasi/pose/klasifikasi/OBB.
- Skala model n hingga x.
- Kompatibilitas ekosistem Ultralytics.

## Kontribusi Utama
1. Meringkas peningkatan arsitektural YOLOv11 secara sistematis.
2. Menyoroti integrasi attention (C2PSA).
3. Menegaskan cakupan multi-tugas satu kerangka.
4. Menyediakan acuan cepat bagi praktisi.

## Rincian Eksperimen
Berbasis rilis dan benchmark Ultralytics di COCO, ulasan melaporkan peningkatan mAP dengan parameter lebih sedikit dibanding YOLOv8 (angka mengacu dokumentasi resmi).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | mAP / parameter | peningkatan mAP dengan parameter lebih sedikit vs YOLOv8 |
| Multi-tugas | cakupan | deteksi/segmentasi/pose/klasifikasi/OBB |
| Skala model | n-x | trade-off kecepatan-akurasi per skala |

## Temuan Kunci
- C3k2 dan C2PSA adalah perubahan inti YOLOv11.
- Attention spasial meningkatkan kualitas fitur.
- Satu kerangka menangani banyak tugas visi.
- Efisiensi parameter membaik dibanding YOLOv8.

## Keunggulan
- Ringkasan arsitektural yang jelas.
- Menyoroti tren integrasi attention.
- Berguna sebagai rujukan cepat.

## Keterbatasan
- Bersifat tinjauan (bukan kontribusi metode baru).
- Angka bergantung dokumentasi vendor.
- Detail teknis sebagian belum dipublikasi formal.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
YOLOv11 sebagai rilis terbaru sering dijadikan backbone deteksi 2D pada sistem RGB-D mutakhir; tinjauan ini membantu memahami fitur yang relevan untuk integrasi tersebut.

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
Tinjauan ini menyediakan peta cepat peningkatan YOLOv11 (C3k2, C2PSA, multi-tugas), menegaskan tren integrasi attention pada YOLO modern.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `khanam2024yolov11` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 010/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
