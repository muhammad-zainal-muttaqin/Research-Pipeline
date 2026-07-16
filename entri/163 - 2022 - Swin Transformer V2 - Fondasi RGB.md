# 163 - Swin Transformer V2: Scaling Up Capacity and Resolution

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 163 dari 191 |
| Kunci BibTeX | `liu2022swinv2` |
| Judul | Swin Transformer V2: Scaling Up Capacity and Resolution |
| Penulis | Liu, Ze; Hu, Han; Lin, Yutong; Yao, Zhuliang; Xie, Zhenda; Wei, Yixuan; Ning, Jia; Cao, Yue; Zhang, Zheng; Dong, Li; Wei, Furu; Guo, Baining |
| Tahun | 2022 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fondasi RGB |
| Kata kunci | vision transformer, scaling, high resolution, backbone |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2111.09883
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Swin%20Transformer%20V2%3A%20Scaling%20Up%20Capacity%20and%20Resolution
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Swin%20Transformer%20V2%3A%20Scaling%20Up%20Capacity%20and%20Resolution&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2111.09883 |

## Ringkasan Eksekutif
Swin Transformer V2 mengatasi ketidakstabilan saat menskalakan Vision Transformer ke kapasitas dan resolusi besar melalui residual-post-norm, scaled cosine attention, dan log-spaced continuous position bias.

## Abstrak (Parafrase)
Penulis mengidentifikasi masalah saat memperbesar Swin: aktivasi meledak di layer dalam dan bias posisi tak transfer antar-resolusi. Solusinya: post-normalization dengan residual, cosine attention yang diskalakan untuk menstabilkan logit, serta continuous log-spaced position bias agar model pra-latih resolusi rendah dapat fine-tune ke resolusi tinggi. Model diskalakan hingga 3 miliar parameter.

## Latar Belakang & Konteks
Menskalakan Transformer visi tak semulus NLP karena instabilitas pelatihan dan celah resolusi antara pra-latih dan hilir.

## Permasalahan yang Diangkat
- Instabilitas aktivasi pada model besar.
- Bias posisi tak transfer lintas resolusi.
- Kebutuhan data/labeled besar untuk skala.

## Tujuan & Pertanyaan Penelitian
- Menstabilkan pelatihan Transformer besar.
- Memungkinkan transfer resolusi rendah ke tinggi.
- Menskalakan kapasitas secara efektif.

## Tinjauan Terdahulu / Posisi Literatur
Kelanjutan Swin V1; berdialog dengan ViT-G dan tren penskalaan model besar.

Karya/konsep pembanding yang relevan:

- Swin Transformer V1 - Transformer hierarkis berjendela.
- ViT - Transformer citra murni.
- ViT-G - penskalaan besar.
- MAE - pra-pelatihan self-supervised.

## Metodologi & Arsitektur
Residual-post-norm menstabilkan, scaled cosine attention menggantikan dot-product, log-spaced continuous position bias (MLP kecil) untuk generalisasi resolusi; ditambah teknik hemat memori.

Komponen / langkah metodologis utama:

- Res-post-norm untuk stabilitas layer dalam.
- Scaled cosine attention.
- Log-spaced continuous position bias.
- Teknik hemat memori (activation checkpointing).

## Kontribusi Utama
1. Resep menskalakan Swin ke 3B parameter.
2. Transfer resolusi yang mulus.
3. Peningkatan SOTA di beberapa benchmark.
4. Efisiensi label lebih baik.

## Rincian Eksperimen
ImageNet klasifikasi, COCO deteksi, ADE20K segmentasi, Kinetics video - menunjukkan skala menaikkan kinerja.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| ImageNet | Top-1 | SOTA saat rilis |
| COCO | AP | backbone besar unggul |
| ADE20K | mIoU | segmentasi SOTA |

## Temuan Kunci
- Stabilisasi memungkinkan penskalaan besar.
- Bias posisi kontinu penting untuk resolusi tinggi.
- Model besar menaikkan tugas dense.

## Keunggulan
- Skalabel dan stabil.
- Kuat pada resolusi tinggi.
- Serbaguna lintas tugas.

## Keterbatasan
- Komputasi/memori sangat besar.
- Tak praktis untuk edge.
- Butuh infrastruktur pelatihan besar.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Backbone berkapasitas tinggi untuk tugas dense RGB (deteksi/segmentasi) yang dapat menjadi cabang RGB pada arsitektur RGB-D skala besar.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [155 - 2024 - RT-DETR - Fondasi RGB](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md)
- [156 - 2024 - YOLO-World - Fondasi RGB](./156%20-%202024%20-%20YOLO-World%20-%20Fondasi%20RGB.md)
- [157 - 2023 - Gold-YOLO - Fondasi RGB](./157%20-%202023%20-%20Gold-YOLO%20-%20Fondasi%20RGB.md)
- [158 - 2023 - DINO detector - Fondasi RGB](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md)
- [159 - 2022 - DN-DETR - Fondasi RGB](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md)
- [160 - 2021 - Conditional DETR - Fondasi RGB](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md)
- [161 - 2021 - Sparse R-CNN - Fondasi RGB](./161%20-%202021%20-%20Sparse%20R-CNN%20-%20Fondasi%20RGB.md)
- [162 - 2022 - ConvNeXt - Fondasi RGB](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Fondasi RGB** dalam peta tinjauan (17 klaster, 191 entri total).
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
Swin V2 memecahkan hambatan penskalaan Transformer visi, memperkuat opsi backbone kelas atas untuk persepsi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `liu2022swinv2` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 163/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
