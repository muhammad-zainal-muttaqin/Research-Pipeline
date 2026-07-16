# 026 - A Comprehensive Review of YOLO Architectures in Computer Vision: From YOLOv1 to YOLOv8 and YOLO-NAS

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 026 dari 154 |
| Kunci BibTeX | `terven2023yolo` |
| Judul | A Comprehensive Review of YOLO Architectures in Computer Vision: From YOLOv1 to YOLOv8 and YOLO-NAS |
| Penulis | Terven, Juan; Cordova-Esparza, Diana-Margarita; Romero-Gonzalez, Julio-Alejandro |
| Tahun | 2023 |
| Venue / Jurnal | Machine Learning and Knowledge Extraction |
| Tema klaster | Survei YOLO |
| Kata kunci | survei, YOLO, YOLOv1-v8, YOLO-NAS, evolusi arsitektur |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-survei-yolo)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=A%20Comprehensive%20Review%20of%20YOLO%20Architectures%20in%20Computer%20Vision%3A%20From%20YOLOv1%20to%20YOLOv8%20and%20YOLO-NAS
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=A%20Comprehensive%20Review%20of%20YOLO%20Architectures%20in%20Computer%20Vision%3A%20From%20YOLOv1%20to%20YOLOv8%20and%20YOLO-NAS&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 5 |
| Nomor | 4 |
| Halaman | 1680--1716 |

## Ringkasan Eksekutif
Tinjauan komprehensif arsitektur YOLO dari v1 hingga v8 dan YOLO-NAS yang mensintesis evolusi backbone/neck/head, metrik, dan tren desain menjadi peta jalan terstruktur.

## Abstrak (Parafrase)
Makalah survei ini menelusuri seluruh silsilah YOLO (v1-v8, PP-YOLO, YOLOX, YOLO-NAS), menjelaskan komponen arsitektural tiap versi (backbone, neck, head), perubahan strategi (anchor->anchor-free, label assignment), serta metrik dan dataset evaluasi. Ia menyediakan kerangka pemahaman evolusi YOLO yang banyak disitasi.

## Latar Belakang & Konteks
Perkembangan YOLO sangat cepat dan tersebar di banyak makalah/repos, sehingga praktisi dan peneliti membutuhkan sintesis terstruktur yang menautkan perubahan antar-versi.

## Permasalahan yang Diangkat
- Evolusi YOLO cepat dan tersebar di banyak sumber.
- Sulit membandingkan komponen antar-versi secara sistematis.
- Perubahan paradigma (anchor-free, label assignment) perlu dipetakan.
- Metrik/dataset evaluasi beragam.
- Praktisi butuh peta jalan yang koheren.

## Tujuan & Pertanyaan Penelitian
- Mensintesis evolusi arsitektur YOLO v1-v8 + turunan.
- Memetakan komponen backbone/neck/head tiap versi.
- Menyediakan acuan metrik dan dataset.

## Tinjauan Terdahulu / Posisi Literatur
Sebagai survei, makalah ini mengagregasi dan mengklasifikasikan seluruh literatur YOLO dan detektor terkait.

Karya/konsep pembanding yang relevan:

- Seluruh silsilah YOLO (v1-v8, PP-YOLO, YOLOX, YOLO-NAS).
- Detektor pembanding (R-CNN, SSD, RetinaNet).
- Metrik deteksi (mAP, IoU) & dataset (COCO, VOC).
- Tren label assignment & anchor-free.

## Metodologi & Arsitektur
Metodologi survei: menelusuri kronologi versi, mendekomposisi arsitektur (backbone/neck/head), membandingkan strategi pelatihan/label assignment, dan merangkum kinerja terpublikasi pada benchmark standar.

Komponen / langkah metodologis utama:

- Kronologi evolusi v1 hingga v8 + YOLO-NAS.
- Dekomposisi backbone/neck/head per versi.
- Analisis anchor vs anchor-free.
- Ringkasan label assignment (statis vs dinamis).
- Kompilasi metrik/kecepatan dari literatur.
- Diskusi aplikasi & arah.

## Kontribusi Utama
1. Peta jalan evolusi YOLO yang koheren dan terstruktur.
2. Dekomposisi arsitektur yang memudahkan perbandingan.
3. Ringkasan metrik/dataset yang praktis.
4. Rujukan survei YOLO yang banyak disitasi.

## Rincian Eksperimen
Sebagai survei, evaluasi berupa kompilasi dan analisis komparatif mAP/kecepatan lintas versi dari makalah asli, bukan eksperimen baru.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Lintas versi YOLO | mAP/FPS | kompilasi hasil terpublikasi |
| COCO | perbandingan | tren peningkatan antar-versi |
| Analisis | komponen | dampak backbone/neck/head |

## Temuan Kunci
- Evolusi YOLO menuju anchor-free dan label assignment dinamis.
- Peningkatan konsisten backbone/neck memacu akurasi.
- Trade-off kecepatan-akurasi terus membaik.
- Ekosistem/tooling mempercepat adopsi.

## Keunggulan
- Komprehensif dan terstruktur.
- Rujukan cepat evolusi YOLO.
- Banyak disitasi.

## Keterbatasan
- Bersifat survei (tanpa metode/eksperimen baru).
- Cepat usang seiring rilis versi baru.
- Perbandingan antar-sumber tak selalu setara.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Survei ini menyediakan kerangka klasifikasi yang menaungi banyak entri YOLO dalam tinjauan ini; berguna untuk menempatkan tiap varian pada peta evolusi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Survei YOLO** yang baik dibaca berdampingan:

- [027 - 2023 - Review YOLO Manufaktur (Hussain) - Survei YOLO](./027%20-%202023%20-%20Review%20YOLO%20Manufaktur%20%28Hussain%29%20-%20Survei%20YOLO.md)
- [028 - 2022 - Review Perkembangan YOLO (Jiang dkk.) - Survei YOLO](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md)
- [029 - 2024 - Review YOLO Pertanian (Sapkota dkk.) - Survei YOLO](./029%20-%202024%20-%20Review%20YOLO%20Pertanian%20%28Sapkota%20dkk.%29%20-%20Survei%20YOLO.md)
- [030 - 2024 - Review Model & Aplikasi YOLO (Ali & Zhang) - Survei YOLO](./030%20-%202024%20-%20Review%20Model%20%26%20Aplikasi%20YOLO%20%28Ali%20%26%20Zhang%29%20-%20Survei%20YOLO.md)
- [031 - 2024 - Systematic Review YOLO (Vijayakumar & Vairavasundaram) - Survei YOLO](./031%20-%202024%20-%20Systematic%20Review%20YOLO%20%28Vijayakumar%20%26%20Vairavasundaram%29%20-%20Survei%20YOLO.md)
- [032 - 2024 - YOLO Evolution Benchmark (Alif & Hussain) - Survei YOLO](./032%20-%202024%20-%20YOLO%20Evolution%20Benchmark%20%28Alif%20%26%20Hussain%29%20-%20Survei%20YOLO.md)
- [033 - 2024 - Review YOLOv8 (Sohan dkk.) - Survei YOLO](./033%20-%202024%20-%20Review%20YOLOv8%20%28Sohan%20dkk.%29%20-%20Survei%20YOLO.md)
- [034 - 2023 - Object Detection using YOLO (Diwan dkk.) - Survei YOLO](./034%20-%202023%20-%20Object%20Detection%20using%20YOLO%20%28Diwan%20dkk.%29%20-%20Survei%20YOLO.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Survei YOLO** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Survei YOLO)
Istilah penting untuk memahami makalah ini:

- **Survei/tinjauan** — Makalah yang mensintesis banyak studi, bukan metode baru.
- **Taksonomi** — Skema klasifikasi metode ke kategori terstruktur.
- **Silsilah YOLO** — Rangkaian versi YOLO (v1..v12, PP-YOLO, YOLOX).
- **Benchmark** — Evaluasi terstandar untuk perbandingan adil.
- **mAP** — mean Average Precision; metrik deteksi utama.
- **Bag-of-Freebies** — Teknik menaikkan akurasi tanpa menambah biaya inferensi.
- **Celah riset** — Isu terbuka yang diidentifikasi sebagai arah lanjutan.
- **PRISMA** — Protokol tinjauan sistematis (identifikasi-seleksi-inklusi).
- **Real-time** — Kemampuan berjalan pada laju tinggi (>=30 FPS).
- **Domain aplikasi** — Bidang penerapan yang dipetakan survei.

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
Terven dkk. memberikan tinjauan komprehensif dan terstruktur atas arsitektur YOLO v1-v8 dan YOLO-NAS, menjadi peta jalan rujukan yang banyak dipakai untuk memahami evolusi YOLO.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `terven2023yolo` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 026/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
