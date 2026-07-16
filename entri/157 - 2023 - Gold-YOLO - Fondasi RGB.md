# 157 - Gold-YOLO: Efficient Object Detector via Gather-and-Distribute Mechanism

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 157 dari 191 |
| Kunci BibTeX | `wang2023goldyolo` |
| Judul | Gold-YOLO: Efficient Object Detector via Gather-and-Distribute Mechanism |
| Penulis | Wang, Chengcheng; He, Wei; Nie, Ying; Guo, Jianyuan; Liu, Chuanjian; Han, Kai; Wang, Yunhe |
| Tahun | 2023 |
| Venue / Jurnal | Advances in Neural Information Processing Systems (NeurIPS) |
| Tema klaster | Fondasi RGB |
| Kata kunci | gather-and-distribute, neck, feature fusion, real-time detection |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2309.11331
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Gold-YOLO%3A%20Efficient%20Object%20Detector%20via%20Gather-and-Distribute%20Mechanism
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Gold-YOLO%3A%20Efficient%20Object%20Detector%20via%20Gather-and-Distribute%20Mechanism&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2309.11331 |

## Ringkasan Eksekutif
Gold-YOLO memperkenalkan mekanisme Gather-and-Distribute (GD) pada neck detektor untuk memperbaiki fusi fitur multiskala yang selama ini bocor informasi pada FPN/PAN konvensional, menaikkan akurasi tanpa mengorbankan kecepatan.

## Abstrak (Parafrase)
Penulis menganalisis bahwa fusi bertingkat FPN/PAN kehilangan informasi karena penggabungan hanya antar-level bertetangga. Mekanisme GD mengumpulkan (gather) fitur seluruh level ke representasi global lalu mendistribusikannya (distribute) kembali ke tiap level, sehingga setiap skala mengakses konteks penuh. Ditambah blok berbasis attention dan pra-pelatihan MAE-style, Gold-YOLO mengungguli YOLO sebanding pada COCO.

## Latar Belakang & Konteks
Neck (FPN/PAN) menentukan kualitas fitur multiskala pada detektor real-time, tetapi fusi tetangga-ke-tetangga membatasi aliran informasi lintas-skala yang jauh.

## Permasalahan yang Diangkat
- Fusi FPN/PAN kehilangan informasi antar-level yang berjauhan.
- Perlu fusi global tanpa menambah latensi signifikan.
- Menjaga trade-off akurasi-kecepatan YOLO.

## Tujuan & Pertanyaan Penelitian
- Merancang neck dengan fusi fitur global.
- Meningkatkan mAP pada anggaran kecepatan sama.
- Mengintegrasikan attention secara efisien.

## Tinjauan Terdahulu / Posisi Literatur
Membandingkan diri dengan neck FPN, PAN, dan BiFPN, serta seri YOLOv6/YOLOv7/YOLOv8; kebaruan pada aliran informasi global gather-and-distribute.

Karya/konsep pembanding yang relevan:

- FPN - piramida fitur top-down.
- PAN - jalur agregasi bottom-up tambahan.
- BiFPN - fusi berbobot dua-arah.
- YOLOv6/7/8 - baseline real-time.

## Metodologi & Arsitektur
Modul Gather-and-Distribute low-stage dan high-stage mengumpulkan fitur multiskala ke token global via attention lalu menyuntikkannya kembali; ditambah information injection module dan pra-pelatihan self-supervised.

Komponen / langkah metodologis utama:

- Gather: agregasi fitur semua level ke representasi bersama.
- Distribute: injeksi konteks global ke tiap level.
- Blok attention efisien untuk fusi.
- Pra-pelatihan MAE-style pada backbone.

## Kontribusi Utama
1. Mekanisme Gather-and-Distribute untuk neck.
2. Peningkatan mAP tanpa memperlambat inferensi.
3. Integrasi pra-pelatihan self-supervised.
4. SOTA di antara YOLO sebanding saat rilis.

## Rincian Eksperimen
COCO dengan varian N/S/M/L, melaporkan AP dan latensi; ablation memisahkan kontribusi GD dan pra-pelatihan.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| MS COCO | AP | naik konsisten vs YOLOv6/8 pada FLOPs setara |
| Latensi | ms | tetap real-time |
| Ablation GD | AP | GD menyumbang kenaikan utama |

## Temuan Kunci
- Fusi global mengungguli fusi tetangga bertingkat.
- Konteks penuh membantu objek multiskala.
- Pra-pelatihan menambah akurasi tambahan.

## Keunggulan
- Akurasi lebih tinggi pada kecepatan setara.
- Neck dapat dipasang pada berbagai YOLO.
- Skalabel.

## Keterbatasan
- Kompleksitas neck meningkat.
- Manfaat attention bergantung implementasi efisien.
- Pra-pelatihan menambah biaya latih.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Menyediakan komponen neck yang bisa diadopsi detektor RGB/RGB-D untuk memperbaiki fusi fitur objek berbagai ukuran.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fondasi RGB** yang baik dibaca berdampingan:

- [155 - 2024 - RT-DETR - Fondasi RGB](./155%20-%202024%20-%20RT-DETR%20-%20Fondasi%20RGB.md)
- [156 - 2024 - YOLO-World - Fondasi RGB](./156%20-%202024%20-%20YOLO-World%20-%20Fondasi%20RGB.md)
- [158 - 2023 - DINO detector - Fondasi RGB](./158%20-%202023%20-%20DINO%20detector%20-%20Fondasi%20RGB.md)
- [159 - 2022 - DN-DETR - Fondasi RGB](./159%20-%202022%20-%20DN-DETR%20-%20Fondasi%20RGB.md)
- [160 - 2021 - Conditional DETR - Fondasi RGB](./160%20-%202021%20-%20Conditional%20DETR%20-%20Fondasi%20RGB.md)
- [161 - 2021 - Sparse R-CNN - Fondasi RGB](./161%20-%202021%20-%20Sparse%20R-CNN%20-%20Fondasi%20RGB.md)
- [162 - 2022 - ConvNeXt - Fondasi RGB](./162%20-%202022%20-%20ConvNeXt%20-%20Fondasi%20RGB.md)
- [163 - 2022 - Swin Transformer V2 - Fondasi RGB](./163%20-%202022%20-%20Swin%20Transformer%20V2%20-%20Fondasi%20RGB.md)

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
Gold-YOLO membuktikan perbaikan aliran informasi pada neck memberi kenaikan akurasi gratis, relevan sebagai referensi desain detektor.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wang2023goldyolo` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 157/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
