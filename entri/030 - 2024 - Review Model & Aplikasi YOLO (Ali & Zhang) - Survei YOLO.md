# 030 - YOLO-Based Object Detection Models: A Review and Its Applications

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 030 dari 154 |
| Kunci BibTeX | `ali2024yoloreview` |
| Judul | YOLO-Based Object Detection Models: A Review and Its Applications |
| Penulis | Ali, Md Latifur; Zhang, Zhili |
| Tahun | 2024 |
| Venue / Jurnal | Multimedia Tools and Applications |
| Tema klaster | Survei YOLO |
| Kata kunci | survei, YOLO, aplikasi lintas domain, model deteksi, tinjauan |

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
- **DOI (halaman penerbit):** https://doi.org/10.1007/s11042-024-18872-y
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLO-Based%20Object%20Detection%20Models%3A%20A%20Review%20and%20Its%20Applications
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLO-Based%20Object%20Detection%20Models%3A%20A%20Review%20and%20Its%20Applications&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Penerbit | Springer |
| DOI | 10.1007/s11042-024-18872-y |

## Ringkasan Eksekutif
Tinjauan model deteksi berbasis YOLO beserta ragam aplikasinya lintas domain, mengonsolidasikan peta penerapan YOLO yang luas.

## Abstrak (Parafrase)
Makalah ini meninjau berbagai model deteksi berbasis YOLO dan mengklasifikasikan penerapannya di banyak domain (transportasi, medis, keamanan, pertanian, industri). Ia merangkum kekuatan dan keterbatasan pendekatan YOLO pada tiap konteks, memberikan gambaran luas ekosistem aplikasi YOLO.

## Latar Belakang & Konteks
Aplikasi YOLO tersebar sangat luas lintas bidang, sehingga dibutuhkan konsolidasi yang memetakan di mana dan bagaimana YOLO dipakai beserta trade-off-nya.

## Permasalahan yang Diangkat
- Aplikasi YOLO tersebar sangat luas lintas domain.
- Kekuatan/keterbatasan per konteks belum terkonsolidasi.
- Sulit menilai kesesuaian YOLO untuk domain tertentu.
- Ragam modifikasi model membingungkan.
- Perlu peta aplikasi yang koheren.

## Tujuan & Pertanyaan Penelitian
- Meninjau model deteksi berbasis YOLO.
- Mengklasifikasikan aplikasi lintas domain.
- Merangkum kekuatan dan keterbatasan.

## Tinjauan Terdahulu / Posisi Literatur
Survei ini mengagregasi arsitektur YOLO dan studi aplikasi dari berbagai bidang.

Karya/konsep pembanding yang relevan:

- Arsitektur/varian YOLO.
- Studi aplikasi lintas domain.
- Metrik deteksi umum.
- Detektor pembanding.

## Metodologi & Arsitektur
Metodologi survei: klasifikasi aplikasi per domain, ringkasan model YOLO yang dipakai, dan analisis kekuatan/keterbatasan tiap konteks.

Komponen / langkah metodologis utama:

- Klasifikasi aplikasi per domain.
- Ringkasan model/varian YOLO.
- Analisis kekuatan-keterbatasan.
- Kompilasi kinerja terpublikasi.
- Ikhtisar tren aplikasi.
- Diskusi arah.

## Kontribusi Utama
1. Peta aplikasi YOLO yang luas dan terkonsolidasi.
2. Klasifikasi domain yang praktis.
3. Ringkasan kekuatan/keterbatasan.
4. Rujukan untuk penempatan konteks.

## Rincian Eksperimen
Sebagai survei, evaluasi berupa sintesis kinerja dan penerapan dari literatur lintas domain.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Lintas domain | penerapan | peta aplikasi YOLO |
| Model YOLO | kesesuaian | kekuatan/keterbatasan per konteks |
| Kinerja | kompilasi | dari studi terpublikasi |

## Temuan Kunci
- YOLO diterapkan di hampir semua domain visi.
- Kesesuaian bergantung tuntutan kecepatan/akurasi.
- Modifikasi domain-spesifik umum dilakukan.
- Trade-off harus dinilai per konteks.

## Keunggulan
- Cakupan aplikasi luas.
- Klasifikasi domain berguna.
- Rujukan penempatan konteks.

## Keterbatasan
- Kurang kedalaman teknis per metode.
- Bersifat survei umum.
- Cepat usang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Survei ini membantu menempatkan entri-entri aplikasi (pertanian/medis/industri/remote sensing) dalam tinjauan pada peta domain yang lebih luas.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Survei YOLO** yang baik dibaca berdampingan:

- [026 - 2023 - Review YOLO (Terven dkk.) - Survei YOLO](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md)
- [027 - 2023 - Review YOLO Manufaktur (Hussain) - Survei YOLO](./027%20-%202023%20-%20Review%20YOLO%20Manufaktur%20%28Hussain%29%20-%20Survei%20YOLO.md)
- [028 - 2022 - Review Perkembangan YOLO (Jiang dkk.) - Survei YOLO](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md)
- [029 - 2024 - Review YOLO Pertanian (Sapkota dkk.) - Survei YOLO](./029%20-%202024%20-%20Review%20YOLO%20Pertanian%20%28Sapkota%20dkk.%29%20-%20Survei%20YOLO.md)
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
Ali & Zhang mengonsolidasikan model dan aplikasi YOLO lintas domain, menyediakan peta penerapan luas yang berguna untuk menempatkan varian YOLO pada konteksnya.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ali2024yoloreview` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 030/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
