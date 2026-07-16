# 023 - Deformable DETR: Deformable Transformers for End-to-End Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 023 dari 154 |
| Kunci BibTeX | `zhu2021deformabledetr` |
| Judul | Deformable DETR: Deformable Transformers for End-to-End Object Detection |
| Penulis | Zhu, Xizhou; Su, Weijie; Lu, Lewei; Li, Bin; Wang, Xiaogang; Dai, Jifeng |
| Tahun | 2021 |
| Venue / Jurnal | International Conference on Learning Representations (ICLR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | Deformable DETR, deformable attention, konvergensi cepat, multi-skala, objek kecil |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Deformable%20DETR%3A%20Deformable%20Transformers%20for%20End-to-End%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Deformable%20DETR%3A%20Deformable%20Transformers%20for%20End-to-End%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
Mempercepat konvergensi dan memperbaiki objek kecil DETR dengan deformable attention yang hanya memperhatikan sekumpulan titik sampling di sekitar referensi.

## Abstrak (Parafrase)
Deformable DETR mengganti attention global DETR dengan deformable attention: tiap query hanya memperhatikan sejumlah kecil titik sampling yang dipelajari di sekitar titik referensi, pada beberapa skala fitur. Ini menurunkan kompleksitas dari kuadratik menjadi linear terhadap ukuran fitur, mempercepat konvergensi ~10x, dan memperbaiki deteksi objek kecil lewat fitur multi-skala.

## Latar Belakang & Konteks
DETR menderita konvergensi sangat lambat (butuh ratusan epoch) dan lemah pada objek kecil karena attention global mahal dan sulit fokus pada wilayah relevan sejak awal pelatihan.

## Permasalahan yang Diangkat
- DETR konvergen sangat lambat (mahal dilatih).
- Attention global kuadratik terhadap ukuran fitur.
- Objek kecil lemah tanpa fitur multi-skala.
- Fokus attention sulit terbentuk di awal pelatihan.
- Biaya komputasi/memori tinggi.

## Tujuan & Pertanyaan Penelitian
- Mempercepat konvergensi DETR secara drastis.
- Menurunkan kompleksitas attention menjadi linear.
- Memperbaiki deteksi objek kecil via multi-skala.

## Tinjauan Terdahulu / Posisi Literatur
Deformable DETR menggabungkan deformable convolution (sampling adaptif) dan attention jarang pada kerangka DETR.

Karya/konsep pembanding yang relevan:

- DETR — kerangka dasar.
- Deformable Convolution — sampling adaptif.
- Attention jarang — kompleksitas linear.
- FPN/multi-skala — fitur multi-level.

## Metodologi & Arsitektur
Deformable attention module: tiap query memprediksi offset sampling dan bobot attention untuk K titik di sekitar referensi, dijumlahkan berbobot; diterapkan multi-skala (multi-scale deformable attention) tanpa FPN eksplisit; referensi query diperbarui iteratif (bounding box refinement).

Komponen / langkah metodologis utama:

- Deformable attention (K titik sampling adaptif).
- Multi-scale deformable attention (lintas level).
- Kompleksitas linear terhadap ukuran fitur.
- Reference point + iterative box refinement.
- Encoder-decoder gaya DETR.
- Konvergensi ~10x lebih cepat.

## Kontribusi Utama
1. Deformable attention menurunkan kompleksitas ke linear.
2. Konvergensi ~10x lebih cepat dari DETR.
3. Peningkatan signifikan pada objek kecil.
4. Fondasi banyak detektor Transformer efisien.

## Rincian Eksperimen
Diuji di COCO dengan perbandingan konvergensi (epoch) dan AP (khususnya objek kecil) terhadap DETR.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | AP | lebih tinggi dari DETR, epoch jauh lebih sedikit |
| COCO (objek kecil) | AP-S | peningkatan jelas |
| Konvergensi | epoch | ~50 epoch vs ~500 pada DETR |

## Temuan Kunci
- Attention jarang adaptif menyelesaikan konvergensi lambat.
- Multi-skala penting untuk objek kecil.
- Iterative refinement memperbaiki lokalisasi.
- Membuat DETR praktis untuk diadopsi.

## Keunggulan
- Konvergensi cepat & efisien.
- Kuat pada objek kecil.
- Fondasi detektor Transformer modern.

## Keterbatasan
- Implementasi deformable attention lebih kompleks.
- Masih lebih berat dari YOLO untuk real-time.
- Sensitif terhadap jumlah titik sampling.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Deformable DETR membuat detektor Transformer praktis dan mendasari RT-DETR; relevan untuk memahami evolusi menuju deteksi end-to-end yang memengaruhi YOLOv10.

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
Deformable DETR memperkenalkan deformable attention multi-skala yang membuat DETR konvergen cepat dan kuat pada objek kecil, menjadi fondasi detektor Transformer efisien.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhu2021deformabledetr` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 023/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
