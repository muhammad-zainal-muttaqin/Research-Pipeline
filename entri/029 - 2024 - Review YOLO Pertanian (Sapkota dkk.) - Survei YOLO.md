# 029 - YOLOv1 to YOLOv10: A Comprehensive Review of YOLO Variants and Their Application in the Agricultural Domain

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 029 dari 154 |
| Kunci BibTeX | `sapkota2024yoloagri` |
| Judul | YOLOv1 to YOLOv10: A Comprehensive Review of YOLO Variants and Their Application in the Agricultural Domain |
| Penulis | Sapkota, Ranjan; Meng, Zhichao; Churuvija, Manoj; Du, Xiaoming; Ma, Zhenghao; Karkee, Manoj |
| Tahun | 2024 |
| Venue / Jurnal | arXiv preprint arXiv:2406.10139 |
| Tema klaster | Survei YOLO |
| Kata kunci | survei, YOLO, pertanian, deteksi buah, YOLOv1-v10 |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2406.10139
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLOv1%20to%20YOLOv10%3A%20A%20Comprehensive%20Review%20of%20YOLO%20Variants%20and%20Their%20Application%20in%20the%20Agricultural%20Domain
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLOv1%20to%20YOLOv10%3A%20A%20Comprehensive%20Review%20of%20YOLO%20Variants%20and%20Their%20Application%20in%20the%20Agricultural%20Domain&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2406.10139 |

## Ringkasan Eksekutif
Tinjauan komprehensif YOLOv1-v10 dan penerapannya di domain pertanian (deteksi buah, gulma, hama, ternak), memetakan versi ke tugas dan tantangan lapangan.

## Abstrak (Parafrase)
Makalah survei ini memetakan seluruh silsilah YOLO (v1-v10) ke beragam tugas pertanian: deteksi dan penghitungan buah, identifikasi gulma/hama, pemantauan ternak, dan estimasi hasil. Ia membahas dataset pertanian, tantangan lapangan (oklusi, pencahayaan, angin), serta merekomendasikan arah riset, menjadikannya panduan pemilihan varian YOLO untuk agrikultur.

## Latar Belakang & Konteks
Adopsi YOLO di pertanian tumbuh pesat namun terfragmentasi antar-tugas, versi, dan kondisi lapangan, sehingga sulit menentukan pendekatan yang tepat untuk suatu masalah pertanian.

## Permasalahan yang Diangkat
- Adopsi YOLO di pertanian terfragmentasi antar-tugas/versi.
- Tantangan lapangan (oklusi, cahaya, angin) beragam.
- Dataset pertanian tersebar dan tak seragam.
- Sulit memilih versi YOLO yang tepat per tugas.
- Kebutuhan sintesis dan rekomendasi arah.

## Tujuan & Pertanyaan Penelitian
- Memetakan versi YOLO ke tugas-tugas pertanian.
- Mensintesis dataset dan tantangan lapangan.
- Merekomendasikan arah riset agrikultur.

## Tinjauan Terdahulu / Posisi Literatur
Survei ini mengagregasi silsilah YOLO dan literatur agrikultur berbasis penglihatan.

Karya/konsep pembanding yang relevan:

- Seluruh silsilah YOLO (v1-v10).
- Studi deteksi buah/gulma/hama/ternak.
- Dataset pertanian.
- Sensor RGB & RGB-D di lapangan.

## Metodologi & Arsitektur
Metodologi survei: klasifikasi aplikasi pertanian, pemetaan versi YOLO ke tugas, tinjauan dataset, analisis tantangan lapangan, dan rekomendasi arah.

Komponen / langkah metodologis utama:

- Pemetaan versi YOLO ke tugas pertanian.
- Klasifikasi aplikasi (buah/gulma/hama/ternak).
- Tinjauan dataset agrikultur.
- Analisis tantangan lapangan (oklusi/cahaya).
- Kompilasi metrik dari banyak studi.
- Rekomendasi arah riset.

## Kontribusi Utama
1. Panduan pemilihan varian YOLO untuk pertanian.
2. Pemetaan versi->tugas yang praktis.
3. Sintesis tantangan lapangan.
4. Rekomendasi arah yang berguna.

## Rincian Eksperimen
Sebagai survei, evaluasi berupa agregasi metrik dari banyak studi pertanian dan analisis komparatif, bukan eksperimen baru.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Studi pertanian | mAP/PR | agregasi lintas studi |
| Versi YOLO | kesesuaian | pemetaan ke tugas agrikultur |
| Tantangan | lapangan | oklusi, cahaya, dataset |

## Temuan Kunci
- YOLO diadopsi luas lintas tugas pertanian.
- Kondisi lapangan menuntut adaptasi model.
- RGB-D membantu lokalisasi 3D buah.
- Standarisasi dataset masih kurang.

## Keunggulan
- Komprehensif untuk domain pertanian.
- Pemetaan versi->tugas praktis.
- Mencakup hingga v10.

## Keterbatasan
- Bersifat survei domain-spesifik.
- Perbandingan antar-studi tak setara.
- Cepat usang seiring rilis versi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Survei ini langsung relevan dengan klaster Pertanian dan YOLO+RGB-D dalam tinjauan (deteksi buah, panen robotik), menyediakan konteks untuk entri-entri tersebut.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Survei YOLO** yang baik dibaca berdampingan:

- [026 - 2023 - Review YOLO (Terven dkk.) - Survei YOLO](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md)
- [027 - 2023 - Review YOLO Manufaktur (Hussain) - Survei YOLO](./027%20-%202023%20-%20Review%20YOLO%20Manufaktur%20%28Hussain%29%20-%20Survei%20YOLO.md)
- [028 - 2022 - Review Perkembangan YOLO (Jiang dkk.) - Survei YOLO](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md)
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
Sapkota dkk. memetakan penerapan YOLOv1-v10 di pertanian secara komprehensif, menjadi panduan pemilihan varian dan pemahaman tantangan lapangan termasuk untuk sistem RGB-D panen.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `sapkota2024yoloagri` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 029/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
