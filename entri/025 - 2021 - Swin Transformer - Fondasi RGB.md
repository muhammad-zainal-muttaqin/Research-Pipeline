# 025 - Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 025 dari 154 |
| Kunci BibTeX | `liu2021swin` |
| Judul | Swin Transformer: Hierarchical Vision Transformer Using Shifted Windows |
| Penulis | Liu, Ze; Lin, Yutong; Cao, Yue; Hu, Han; Wei, Yixuan; Zhang, Zheng; Lin, Stephen; Guo, Baining |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema klaster | Fondasi RGB |
| Kata kunci | Swin Transformer, shifted window, hierarkis, backbone, linear |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Swin%20Transformer%3A%20Hierarchical%20Vision%20Transformer%20Using%20Shifted%20Windows
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Swin%20Transformer%3A%20Hierarchical%20Vision%20Transformer%20Using%20Shifted%20Windows&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 10012--10022 |

## Ringkasan Eksekutif
Membangun representasi hierarkis dengan self-attention berjendela bergeser (shifted windows), memberi kompleksitas linear dan menjadikannya backbone tujuan umum untuk deteksi/segmentasi.

## Abstrak (Parafrase)
Swin Transformer menghitung self-attention di dalam jendela lokal non-overlap untuk kompleksitas linear terhadap ukuran citra, lalu menggeser partisi jendela antar-lapisan (shifted window) agar informasi mengalir antar-jendela. Peta fitur hierarkis multi-skala (via patch merging) menjadikannya backbone tujuan umum yang unggul pada klasifikasi, deteksi, dan segmentasi.

## Latar Belakang & Konteks
ViT global memiliki kompleksitas kuadratik terhadap jumlah token dan menghasilkan fitur single-scale, kurang ideal untuk prediksi padat (deteksi/segmentasi) yang membutuhkan multi-skala dan efisiensi.

## Permasalahan yang Diangkat
- Attention global ViT kuadratik terhadap ukuran citra.
- ViT menghasilkan fitur single-scale.
- Prediksi padat butuh fitur hierarkis multi-skala.
- Efisiensi diperlukan untuk resolusi tinggi.
- Backbone tujuan umum berbasis Transformer belum ada.

## Tujuan & Pertanyaan Penelitian
- Menurunkan kompleksitas attention menjadi linear.
- Membangun fitur hierarkis multi-skala.
- Menyediakan backbone Transformer tujuan umum.

## Tinjauan Terdahulu / Posisi Literatur
Swin menyatukan keunggulan CNN hierarkis dengan attention Transformer, sebagai backbone untuk berbagai tugas.

Karya/konsep pembanding yang relevan:

- ViT — Transformer global (pembanding).
- CNN hierarkis (ResNet) — inspirasi multi-skala.
- Window attention — kompleksitas linear.
- Patch merging — pengurangan resolusi bertahap.

## Metodologi & Arsitektur
Citra dipartisi menjadi jendela; W-MSA menghitung attention dalam jendela; lapisan berikutnya memakai SW-MSA (jendela digeser) untuk koneksi antar-jendela; patch merging mengurangi resolusi dan menaikkan dimensi (tahap hierarkis); relative position bias ditambahkan.

Komponen / langkah metodologis utama:

- Window-based MSA (W-MSA) — kompleksitas linear.
- Shifted window MSA (SW-MSA) — koneksi antar-jendela.
- Patch merging untuk fitur hierarkis multi-skala.
- Relative position bias.
- Empat tahap resolusi menurun.
- Backbone plug-in untuk deteksi/segmentasi.

## Kontribusi Utama
1. Attention berjendela bergeser (linear + koneksi antar-jendela).
2. Fitur hierarkis multi-skala.
3. Backbone tujuan umum yang unggul lintas tugas.
4. SOTA klasifikasi/deteksi/segmentasi saat rilis.

## Rincian Eksperimen
Diuji pada ImageNet (klasifikasi), COCO (deteksi/segmentasi), dan ADE20K (segmentasi) dengan perbandingan terhadap CNN dan ViT.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| ImageNet | top-1 | SOTA saat rilis |
| COCO | AP box/mask | SOTA sebagai backbone |
| ADE20K | mIoU | SOTA segmentasi semantik |

## Temuan Kunci
- Shifted window menyeimbangkan efisiensi dan koneksi global.
- Fitur hierarkis penting untuk prediksi padat.
- Backbone Transformer dapat menyaingi/mengungguli CNN.
- Serbaguna lintas tugas visi.

## Keunggulan
- Efisien (linear) dan hierarkis.
- Backbone serbaguna dan kuat.
- Banyak diadopsi luas.

## Keterbatasan
- Lebih kompleks dari CNN standar.
- Window attention membatasi konteks sangat jauh.
- Butuh implementasi khusus untuk shifting.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Swin Transformer adalah backbone yang dipakai pada RGB-D/RGB-T SOD (mis. SwinNet) dan segmentasi RGB-D dalam tinjauan ini; fundamental untuk memahami metode berbasis Transformer.

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
Swin Transformer menghadirkan attention berjendela bergeser yang linear dan hierarkis, menjadi backbone Transformer tujuan umum yang banyak dipakai pada tugas RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `liu2021swin` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 025/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
