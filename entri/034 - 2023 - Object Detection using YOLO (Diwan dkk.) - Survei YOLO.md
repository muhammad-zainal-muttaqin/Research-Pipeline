# 034 - Object Detection Using YOLO: Challenges, Architectural Successors, Datasets and Applications

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 034 dari 154 |
| Kunci BibTeX | `diwan2023yolo` |
| Judul | Object Detection Using YOLO: Challenges, Architectural Successors, Datasets and Applications |
| Penulis | Diwan, Tausif; Anirudh, G.; Tembhurne, Jitendra V. |
| Tahun | 2023 |
| Venue / Jurnal | Multimedia Tools and Applications |
| Tema klaster | Survei YOLO |
| Kata kunci | survei, YOLO, tantangan, dataset, aplikasi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Object%20Detection%20Using%20YOLO%3A%20Challenges%2C%20Architectural%20Successors%2C%20Datasets%20and%20Applications
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Object%20Detection%20Using%20YOLO%3A%20Challenges%2C%20Architectural%20Successors%2C%20Datasets%20and%20Applications&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 82 |
| Nomor | 6 |
| Halaman | 9243--9275 |

## Ringkasan Eksekutif
Tinjauan tantangan, penerus arsitektur, dataset, dan aplikasi deteksi objek berbasis YOLO yang memetakan ekosistem dan isu terbuka secara menyeluruh.

## Abstrak (Parafrase)
Makalah survei ini membahas deteksi objek dengan YOLO secara menyeluruh: tantangan inti (objek kecil, oklusi, real-time), penerus arsitektur, dataset dan metrik, serta aplikasi lintas domain. Ia memberikan peta tantangan-dan-arah yang berguna untuk merumuskan masalah riset.

## Latar Belakang & Konteks
Deteksi berbasis YOLO menghadapi tantangan berulang (objek kecil, oklusi, kecepatan) dan memiliki ekosistem dataset/aplikasi yang luas; dibutuhkan peta menyeluruh atas tantangan dan arah.

## Permasalahan yang Diangkat
- Objek kecil dan oklusi tetap menantang.
- Kebutuhan real-time membatasi kompleksitas.
- Dataset/metrik beragam dan tersebar.
- Ekosistem aplikasi luas sulit dipetakan.
- Isu terbuka perlu diidentifikasi.

## Tujuan & Pertanyaan Penelitian
- Memetakan tantangan inti deteksi YOLO.
- Meninjau dataset, metrik, dan aplikasi.
- Mengidentifikasi arah pengembangan.

## Tinjauan Terdahulu / Posisi Literatur
Survei ini mengagregasi silsilah YOLO, dataset, dan tantangan terbuka.

Karya/konsep pembanding yang relevan:

- Silsilah YOLO & penerus arsitektur.
- Dataset deteksi (COCO, VOC, dll.).
- Metrik evaluasi.
- Aplikasi lintas domain.

## Metodologi & Arsitektur
Metodologi survei: identifikasi tantangan, ikhtisar arsitektur penerus, tinjauan dataset/metrik, dan pemetaan aplikasi serta arah.

Komponen / langkah metodologis utama:

- Diskusi tantangan (objek kecil/oklusi/real-time).
- Ikhtisar penerus arsitektur YOLO.
- Tinjauan dataset & metrik.
- Pemetaan aplikasi lintas domain.
- Identifikasi isu terbuka.
- Rekomendasi arah pengembangan.

## Kontribusi Utama
1. Peta tantangan-dan-arah deteksi YOLO.
2. Ikhtisar dataset/metrik yang praktis.
3. Pemetaan aplikasi lintas domain.
4. Berguna merumuskan masalah riset.

## Rincian Eksperimen
Sebagai survei, evaluasi berupa sintesis tantangan, dataset, dan kinerja dari literatur.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Tantangan | peta | objek kecil, oklusi, real-time |
| Dataset/metrik | ikhtisar | COCO/VOC & mAP |
| Aplikasi | pemetaan | lintas domain |

## Temuan Kunci
- Objek kecil/oklusi adalah tantangan berulang.
- Trade-off kecepatan-akurasi sentral.
- Ekosistem dataset/aplikasi sangat luas.
- Banyak arah riset terbuka.

## Keunggulan
- Menyeluruh (tantangan+dataset+aplikasi).
- Berguna merumuskan riset.
- Ikhtisar dataset/metrik praktis.

## Keterbatasan
- Bersifat survei umum.
- Kedalaman per topik terbatas.
- Cepat usang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Survei ini menyediakan kerangka tantangan-dan-arah yang berguna untuk memposisikan kontribusi entri-entri YOLO+RGB-D dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Survei YOLO** yang baik dibaca berdampingan:

- [026 - 2023 - Review YOLO (Terven dkk.) - Survei YOLO](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md)
- [027 - 2023 - Review YOLO Manufaktur (Hussain) - Survei YOLO](./027%20-%202023%20-%20Review%20YOLO%20Manufaktur%20%28Hussain%29%20-%20Survei%20YOLO.md)
- [028 - 2022 - Review Perkembangan YOLO (Jiang dkk.) - Survei YOLO](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md)
- [029 - 2024 - Review YOLO Pertanian (Sapkota dkk.) - Survei YOLO](./029%20-%202024%20-%20Review%20YOLO%20Pertanian%20%28Sapkota%20dkk.%29%20-%20Survei%20YOLO.md)
- [030 - 2024 - Review Model & Aplikasi YOLO (Ali & Zhang) - Survei YOLO](./030%20-%202024%20-%20Review%20Model%20%26%20Aplikasi%20YOLO%20%28Ali%20%26%20Zhang%29%20-%20Survei%20YOLO.md)
- [031 - 2024 - Systematic Review YOLO (Vijayakumar & Vairavasundaram) - Survei YOLO](./031%20-%202024%20-%20Systematic%20Review%20YOLO%20%28Vijayakumar%20%26%20Vairavasundaram%29%20-%20Survei%20YOLO.md)
- [032 - 2024 - YOLO Evolution Benchmark (Alif & Hussain) - Survei YOLO](./032%20-%202024%20-%20YOLO%20Evolution%20Benchmark%20%28Alif%20%26%20Hussain%29%20-%20Survei%20YOLO.md)
- [033 - 2024 - Review YOLOv8 (Sohan dkk.) - Survei YOLO](./033%20-%202024%20-%20Review%20YOLOv8%20%28Sohan%20dkk.%29%20-%20Survei%20YOLO.md)

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
Diwan dkk. meninjau tantangan, penerus arsitektur, dataset, dan aplikasi deteksi YOLO secara menyeluruh, menyediakan peta yang membantu merumuskan masalah dan arah riset.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `diwan2023yolo` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 034/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
