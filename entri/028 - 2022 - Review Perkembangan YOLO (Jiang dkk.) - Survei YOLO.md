# 028 - A Review of YOLO Algorithm Developments

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 028 dari 154 |
| Kunci BibTeX | `jiang2022yoloreview` |
| Judul | A Review of YOLO Algorithm Developments |
| Penulis | Jiang, Peiyuan; Ergu, Daji; Liu, Fangyao; Cai, Ying; Ma, Bo |
| Tahun | 2022 |
| Venue / Jurnal | Procedia Computer Science |
| Tema klaster | Survei YOLO |
| Kata kunci | survei, YOLO, perkembangan algoritma, perbandingan versi, pengantar |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=A%20Review%20of%20YOLO%20Algorithm%20Developments
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=A%20Review%20of%20YOLO%20Algorithm%20Developments&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 199 |
| Halaman | 1066--1073 |

## Ringkasan Eksekutif
Ulasan ringkas perkembangan algoritma YOLO dan perbandingan antar-versi awal yang berfungsi sebagai pengantar padat bagi praktisi.

## Abstrak (Parafrase)
Makalah ini merangkum prinsip kerja dan perbedaan utama antar-versi YOLO awal (terutama v1-v4 dan turunan), membandingkan kecepatan-akurasi serta perubahan arsitektural inti. Sebagai ulasan ringkas, ia sering dijadikan referensi awal untuk memahami dasar YOLO.

## Latar Belakang & Konteks
Praktisi baru membutuhkan ringkasan aksesibel yang menjelaskan perbedaan antar-versi YOLO tanpa harus membaca banyak makalah teknis terpisah.

## Permasalahan yang Diangkat
- Perbedaan antar-versi YOLO membingungkan pemula.
- Makalah teknis tersebar dan padat.
- Perlu ringkasan aksesibel dan ringkas.
- Trade-off kecepatan-akurasi perlu dijelaskan sederhana.
- Konteks aplikasi perlu diberikan.

## Tujuan & Pertanyaan Penelitian
- Menyediakan pengantar padat evolusi YOLO.
- Membandingkan prinsip dan kinerja antar-versi.
- Memudahkan pemahaman dasar bagi praktisi.

## Tinjauan Terdahulu / Posisi Literatur
Survei ini meninjau YOLOv1-v4 dan turunannya sebagai pengantar.

Karya/konsep pembanding yang relevan:

- YOLOv1-v4 — fokus utama.
- Detektor pembanding (R-CNN, SSD).
- Metrik kecepatan-akurasi.
- Aplikasi umum YOLO.

## Metodologi & Arsitektur
Metodologi survei ringkas: menjelaskan prinsip tiap versi, membandingkan arsitektur dan kinerja, serta menyoroti aplikasi umum.

Komponen / langkah metodologis utama:

- Ringkasan prinsip tiap versi YOLO awal.
- Perbandingan kecepatan-akurasi.
- Ikhtisar perubahan arsitektural inti.
- Diskusi aplikasi umum.
- Format ringkas dan aksesibel.
- Referensi untuk pemula.

## Kontribusi Utama
1. Pengantar padat evolusi YOLO yang mudah dipahami.
2. Perbandingan antar-versi yang ringkas.
3. Sering dikutip sebagai referensi awal.
4. Aksesibel bagi praktisi baru.

## Rincian Eksperimen
Sebagai survei ringkas, evaluasi berupa kompilasi kinerja terpublikasi antar-versi, bukan eksperimen baru.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| YOLOv1-v4 | kecepatan/akurasi | kompilasi ringkas |
| Perbandingan | versi | perubahan inti antar-versi |
| Aplikasi | cakupan | ikhtisar umum |

## Temuan Kunci
- Evolusi YOLO awal meningkatkan kecepatan & akurasi bertahap.
- Tiap versi menambah komponen kunci (anchor, multi-skala, dll.).
- Trade-off kecepatan-akurasi menjadi tema sentral.
- YOLO cocok untuk beragam aplikasi real-time.

## Keunggulan
- Ringkas dan aksesibel.
- Cocok sebagai pengantar.
- Banyak dikutip.

## Keterbatasan
- Cakupan terbatas (versi awal).
- Kedalaman teknis rendah.
- Cepat usang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Ulasan ini berguna sebagai pengantar cepat evolusi YOLO yang menaungi entri-entri YOLO dalam tinjauan, terutama untuk pembaca yang baru mengenal bidang.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Survei YOLO** yang baik dibaca berdampingan:

- [026 - 2023 - Review YOLO (Terven dkk.) - Survei YOLO](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md)
- [027 - 2023 - Review YOLO Manufaktur (Hussain) - Survei YOLO](./027%20-%202023%20-%20Review%20YOLO%20Manufaktur%20%28Hussain%29%20-%20Survei%20YOLO.md)
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
Jiang dkk. menyajikan pengantar padat perkembangan YOLO awal dan perbandingan antar-versi, menjadi referensi awal yang aksesibel bagi praktisi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `jiang2022yoloreview` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 028/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
