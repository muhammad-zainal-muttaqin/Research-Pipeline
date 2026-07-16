# 033 - A Review on YOLOv8 and Its Advancements

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 033 dari 154 |
| Kunci BibTeX | `sohan2024yolov8review` |
| Judul | A Review on YOLOv8 and Its Advancements |
| Penulis | Sohan, Mupparaju; Sai Ram, Thotakura; Rami Reddy, Ch. Venkata |
| Tahun | 2024 |
| Venue / Jurnal | Data Intelligence and Cognitive Informatics |
| Tema klaster | Survei YOLO |
| Kata kunci | survei, YOLOv8, anchor-free, multi-tugas, C2f |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=A%20Review%20on%20YOLOv8%20and%20Its%20Advancements
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=A%20Review%20on%20YOLOv8%20and%20Its%20Advancements&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Penerbit | Springer |

## Ringkasan Eksekutif
Tinjauan arsitektur dan kemajuan YOLOv8 termasuk desain anchor-free, blok C2f, dan dukungan multi-tugas, sebagai acuan ringkas fitur YOLOv8.

## Abstrak (Parafrase)
Makalah ini mendokumentasikan arsitektur YOLOv8 (Ultralytics): backbone dengan blok C2f, head decoupled anchor-free, serta dukungan deteksi, segmentasi, pose, dan klasifikasi dalam satu kerangka. Ia menjelaskan perubahan relatif terhadap YOLOv5-v7 dan merangkum benchmark COCO, menjadi acuan praktis bagi pengguna YOLOv8.

## Latar Belakang & Konteks
YOLOv8 sangat populer di kalangan praktisi namun dokumentasi arsitekturalnya tersebar; dibutuhkan tinjauan yang menjelaskan komponen dan kemampuannya secara ringkas.

## Permasalahan yang Diangkat
- Dokumentasi arsitektur YOLOv8 tersebar.
- Perubahan relatif terhadap v5-v7 perlu dijelaskan.
- Kemampuan multi-tugas perlu dipetakan.
- Praktisi butuh acuan ringkas.
- Benchmark perlu dirangkum.

## Tujuan & Pertanyaan Penelitian
- Mendokumentasikan arsitektur YOLOv8.
- Menjelaskan desain anchor-free & C2f.
- Memetakan dukungan multi-tugas.

## Tinjauan Terdahulu / Posisi Literatur
Survei ini meninjau YOLOv8 relatif terhadap YOLOv5-v7 dan detektor sezaman.

Karya/konsep pembanding yang relevan:

- YOLOv5-v7 — pembanding langsung.
- Blok C2f — komponen backbone.
- Anchor-free head — desain deteksi.
- Ekosistem Ultralytics.

## Metodologi & Arsitektur
Metodologi survei: deskripsi arsitektur (backbone C2f, neck, head anchor-free), cakupan tugas, dan ringkasan benchmark COCO.

Komponen / langkah metodologis utama:

- Backbone dengan blok C2f.
- Head decoupled anchor-free.
- Dukungan deteksi/segmentasi/pose/klasifikasi.
- Perbandingan dengan v5-v7.
- Ringkasan benchmark COCO.
- Ikhtisar ekosistem/tooling.

## Kontribusi Utama
1. Acuan ringkas fitur YOLOv8.
2. Penjelasan desain anchor-free & C2f.
3. Pemetaan kemampuan multi-tugas.
4. Rangkuman benchmark praktis.

## Rincian Eksperimen
Sebagai survei, evaluasi berupa rangkuman benchmark COCO YOLOv8 lintas skala dari sumber resmi.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | mAP | rangkuman per skala model |
| Multi-tugas | cakupan | deteksi/seg/pose/klasifikasi |
| vs v5-v7 | perbandingan | perubahan arsitektur |

## Temuan Kunci
- YOLOv8 mengadopsi anchor-free & C2f.
- Satu kerangka menangani banyak tugas.
- Peningkatan atas v5 pada trade-off.
- Ekosistem mempermudah adopsi.

## Keunggulan
- Acuan ringkas & praktis.
- Menjelaskan multi-tugas.
- Populer di kalangan praktisi.

## Keterbatasan
- Bersifat survei satu-versi.
- Angka bergantung sumber vendor.
- Cepat usang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
YOLOv8 adalah backbone deteksi 2D yang banyak dipakai pada sistem RGB-D terbaru (mis. FusionVision, YOLOv8-URE) dalam tinjauan; acuan ini membantu memahaminya.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Survei YOLO** yang baik dibaca berdampingan:

- [026 - 2023 - Review YOLO (Terven dkk.) - Survei YOLO](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md)
- [027 - 2023 - Review YOLO Manufaktur (Hussain) - Survei YOLO](./027%20-%202023%20-%20Review%20YOLO%20Manufaktur%20%28Hussain%29%20-%20Survei%20YOLO.md)
- [028 - 2022 - Review Perkembangan YOLO (Jiang dkk.) - Survei YOLO](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md)
- [029 - 2024 - Review YOLO Pertanian (Sapkota dkk.) - Survei YOLO](./029%20-%202024%20-%20Review%20YOLO%20Pertanian%20%28Sapkota%20dkk.%29%20-%20Survei%20YOLO.md)
- [030 - 2024 - Review Model & Aplikasi YOLO (Ali & Zhang) - Survei YOLO](./030%20-%202024%20-%20Review%20Model%20%26%20Aplikasi%20YOLO%20%28Ali%20%26%20Zhang%29%20-%20Survei%20YOLO.md)
- [031 - 2024 - Systematic Review YOLO (Vijayakumar & Vairavasundaram) - Survei YOLO](./031%20-%202024%20-%20Systematic%20Review%20YOLO%20%28Vijayakumar%20%26%20Vairavasundaram%29%20-%20Survei%20YOLO.md)
- [032 - 2024 - YOLO Evolution Benchmark (Alif & Hussain) - Survei YOLO](./032%20-%202024%20-%20YOLO%20Evolution%20Benchmark%20%28Alif%20%26%20Hussain%29%20-%20Survei%20YOLO.md)
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
Sohan dkk. mendokumentasikan arsitektur dan kemampuan multi-tugas YOLOv8 secara ringkas, menjadi acuan praktis bagi pengguna yang banyak memakainya termasuk pada pipeline RGB-D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `sohan2024yolov8review` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 033/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
