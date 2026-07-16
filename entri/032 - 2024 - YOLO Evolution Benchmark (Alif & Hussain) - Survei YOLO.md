# 032 - YOLO Evolution: A Comprehensive Benchmark and Architectural Review of YOLOv12, YOLO11, and Their Previous Versions

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 032 dari 154 |
| Kunci BibTeX | `alif2024yoloevolution` |
| Judul | YOLO Evolution: A Comprehensive Benchmark and Architectural Review of YOLOv12, YOLO11, and Their Previous Versions |
| Penulis | Alif, Md Adnan Faisal; Hussain, Muhammad |
| Tahun | 2024 |
| Venue / Jurnal | arXiv preprint arXiv:2411.00201 |
| Tema klaster | Survei YOLO |
| Kata kunci | benchmark, YOLO, YOLOv12, YOLO11, perbandingan arsitektur |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2411.00201
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=YOLO%20Evolution%3A%20A%20Comprehensive%20Benchmark%20and%20Architectural%20Review%20of%20YOLOv12%2C%20YOLO11%2C%20and%20Their%20Previous%20Versions
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=YOLO%20Evolution%3A%20A%20Comprehensive%20Benchmark%20and%20Architectural%20Review%20of%20YOLOv12%2C%20YOLO11%2C%20and%20Their%20Previous%20Versions&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2411.00201 |

## Ringkasan Eksekutif
Benchmark dan tinjauan arsitektural YOLOv12, YOLO11, dan versi sebelumnya secara komparatif dengan pengukuran terstandar.

## Abstrak (Parafrase)
Makalah ini menyediakan benchmark seragam dan tinjauan arsitektural untuk versi YOLO terbaru (YOLOv12, YOLO11) bersama pendahulunya, membandingkan komponen arsitektur dan kinerja kecepatan-akurasi pada pengaturan yang sebisa mungkin setara. Ia memberi bukti komparatif untuk memilih versi YOLO terkini.

## Latar Belakang & Konteks
Klaim kinerja antar-versi YOLO sering diukur pada pengaturan berbeda, menyulitkan perbandingan adil; diperlukan benchmark seragam terutama untuk versi terbaru.

## Permasalahan yang Diangkat
- Klaim antar-versi diukur pada setup berbeda.
- Perbandingan adil versi terbaru belum tersedia.
- Perubahan arsitektur v11/v12 perlu dipetakan.
- Trade-off kecepatan-akurasi perlu diukur seragam.
- Praktisi butuh bukti pemilihan model.

## Tujuan & Pertanyaan Penelitian
- Menyediakan benchmark seragam versi YOLO terbaru.
- Meninjau perubahan arsitektural v11/v12.
- Memberi bukti komparatif untuk pemilihan model.

## Tinjauan Terdahulu / Posisi Literatur
Makalah meninjau lini YOLO mutakhir dengan pengukuran terstandar, membandingkan komponen dan kinerja.

Karya/konsep pembanding yang relevan:

- YOLO11 & YOLOv12 — fokus utama.
- Versi sebelumnya sebagai pembanding.
- Benchmark COCO.
- Metrik kecepatan-akurasi.

## Metodologi & Arsitektur
Metodologi: mendeskripsikan perubahan arsitektur v11/v12, lalu menjalankan/mengompilasi benchmark seragam untuk membandingkan kecepatan-akurasi antar-versi.

Komponen / langkah metodologis utama:

- Perbandingan arsitektur v11/v12 vs pendahulu.
- Benchmark kecepatan-akurasi seragam.
- Analisis komponen baru (attention/blok).
- Pengukuran parameter/FLOPs.
- Evaluasi lintas skala model.
- Rekomendasi pemilihan.

## Kontribusi Utama
1. Bukti komparatif versi YOLO terkini.
2. Benchmark seragam untuk perbandingan adil.
3. Analisis arsitektur v11/v12.
4. Panduan pemilihan model.

## Rincian Eksperimen
Evaluasi menggabungkan benchmark eksperimental dan tinjauan, membandingkan mAP/kecepatan/parameter antar-versi YOLO terbaru pada COCO.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| COCO | mAP/FPS | perbandingan seragam antar-versi |
| v11/v12 | parameter/FLOPs | analisis efisiensi |
| Skala model | trade-off | per skala |

## Temuan Kunci
- Benchmark seragam penting untuk perbandingan adil.
- v11/v12 membawa perubahan arsitektur bertahap.
- Trade-off kecepatan-akurasi terus membaik.
- Pemilihan model bergantung anggaran.

## Keunggulan
- Benchmark seragam & mutakhir.
- Analisis arsitektur terbaru.
- Panduan pemilihan praktis.

## Keterbatasan
- Fokus versi sangat baru (cepat usang).
- Setup benchmark memengaruhi hasil.
- Sebagian detail bergantung vendor.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Benchmark ini relevan untuk memilih backbone YOLO terkini pada sistem RGB-D mutakhir yang dibahas dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Survei YOLO** yang baik dibaca berdampingan:

- [026 - 2023 - Review YOLO (Terven dkk.) - Survei YOLO](./026%20-%202023%20-%20Review%20YOLO%20%28Terven%20dkk.%29%20-%20Survei%20YOLO.md)
- [027 - 2023 - Review YOLO Manufaktur (Hussain) - Survei YOLO](./027%20-%202023%20-%20Review%20YOLO%20Manufaktur%20%28Hussain%29%20-%20Survei%20YOLO.md)
- [028 - 2022 - Review Perkembangan YOLO (Jiang dkk.) - Survei YOLO](./028%20-%202022%20-%20Review%20Perkembangan%20YOLO%20%28Jiang%20dkk.%29%20-%20Survei%20YOLO.md)
- [029 - 2024 - Review YOLO Pertanian (Sapkota dkk.) - Survei YOLO](./029%20-%202024%20-%20Review%20YOLO%20Pertanian%20%28Sapkota%20dkk.%29%20-%20Survei%20YOLO.md)
- [030 - 2024 - Review Model & Aplikasi YOLO (Ali & Zhang) - Survei YOLO](./030%20-%202024%20-%20Review%20Model%20%26%20Aplikasi%20YOLO%20%28Ali%20%26%20Zhang%29%20-%20Survei%20YOLO.md)
- [031 - 2024 - Systematic Review YOLO (Vijayakumar & Vairavasundaram) - Survei YOLO](./031%20-%202024%20-%20Systematic%20Review%20YOLO%20%28Vijayakumar%20%26%20Vairavasundaram%29%20-%20Survei%20YOLO.md)
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
Alif & Hussain menyediakan benchmark seragam dan tinjauan arsitektural YOLO11/YOLOv12, memberi bukti komparatif untuk memilih versi YOLO terbaru.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `alif2024yoloevolution` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 032/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
