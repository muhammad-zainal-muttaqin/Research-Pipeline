# 111 - Visual SLAM in Human Populated Environments: Exploring the Trade-off Between Accuracy and Speed of YOLO and Mask R-CNN

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 111 dari 154 |
| Kunci BibTeX | `soares2019visualslam` |
| Judul | Visual SLAM in Human Populated Environments: Exploring the Trade-off Between Accuracy and Speed of YOLO and Mask R-CNN |
| Penulis | Soares, Jo{\~a |
| Tahun | 2019 |
| Venue / Jurnal | Proceedings of the International Conference on Advanced Robotics (ICAR) |
| Tema klaster | RGB-D SLAM |
| Kata kunci | RGB-D SLAM, dinamis, YOLO, Mask R-CNN, trade-off |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-rgb-d-slam)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Visual%20SLAM%20in%20Human%20Populated%20Environments%3A%20Exploring%20the%20Trade-off%20Between%20Accuracy%20and%20Speed%20of%20YOLO%20and%20Mask%20R-CNN
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Visual%20SLAM%20in%20Human%20Populated%20Environments%3A%20Exploring%20the%20Trade-off%20Between%20Accuracy%20and%20Speed%20of%20YOLO%20and%20Mask%20R-CNN&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 135--140 |

## Ringkasan Eksekutif
Studi yang mengeksplorasi trade-off akurasi vs kecepatan memakai YOLO atau Mask R-CNN untuk menyaring objek dinamis pada visual SLAM di lingkungan berpenghuni.

## Abstrak (Parafrase)
Makalah ini membandingkan penggunaan YOLO (cepat, kotak) versus Mask R-CNN (akurat, mask) sebagai penyaring objek dinamis (manusia) dalam pipeline visual SLAM di lingkungan berpenghuni. Analisis menunjukkan trade-off: Mask R-CNN memberi mask presisi namun lambat, sedangkan YOLO menawarkan kompromi kecepatan-akurasi yang menarik untuk real-time.

## Latar Belakang & Konteks
Detektor akurat (Mask R-CNN) lambat sedangkan detektor cepat (YOLO) kurang detail (kotak, bukan mask); pilihan mana yang lebih baik untuk SLAM dinamis real-time belum jelas.

## Permasalahan yang Diangkat
- Mask R-CNN akurat namun lambat.
- YOLO cepat namun kotak (bukan mask presisi).
- SLAM dinamis real-time menuntut kecepatan.
- Pilihan detektor memengaruhi akurasi-kecepatan.
- Lingkungan berpenghuni penuh objek dinamis.

## Tujuan & Pertanyaan Penelitian
- Membandingkan YOLO vs Mask R-CNN sebagai penyaring.
- Menganalisis trade-off akurasi-kecepatan.
- Memberi panduan pemilihan detektor untuk SLAM.

## Tinjauan Terdahulu / Posisi Literatur
Studi ini membandingkan detektor dalam pipeline SLAM dinamis.

Karya/konsep pembanding yang relevan:

- ORB-SLAM2/DynaSLAM — basis SLAM dinamis.
- YOLO — detektor cepat (kotak).
- Mask R-CNN — detektor akurat (mask).
- Lingkungan berpenghuni (dinamis).

## Metodologi & Arsitektur
Pipeline SLAM dinamis memakai detektor (YOLO atau Mask R-CNN) untuk menandai/menyaring manusia; fitur pada objek dinamis dibuang; akurasi trajektori dan kecepatan dibandingkan antar-detektor pada lingkungan berpenghuni.

Komponen / langkah metodologis utama:

- Integrasi detektor sebagai penyaring dinamis.
- Konfigurasi YOLO (kotak, cepat).
- Konfigurasi Mask R-CNN (mask, akurat).
- Pembuangan fitur dinamis.
- Perbandingan akurasi-kecepatan.
- Evaluasi lingkungan berpenghuni.

## Kontribusi Utama
1. Analisis trade-off YOLO vs Mask R-CNN untuk SLAM.
2. YOLO menawarkan kompromi kecepatan-akurasi.
3. Mask R-CNN lebih presisi namun lambat.
4. Panduan pemilihan detektor untuk SLAM dinamis.

## Rincian Eksperimen
Diuji pada urutan/lingkungan berpenghuni dengan metrik akurasi trajektori dan kecepatan, membandingkan konfigurasi detektor.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Lingkungan berpenghuni | ATE/kecepatan | trade-off YOLO vs Mask R-CNN |
| YOLO | kecepatan | kompromi menarik untuk real-time |
| Mask R-CNN | akurasi | mask presisi namun lambat |

## Temuan Kunci
- Pilihan detektor menentukan trade-off SLAM dinamis.
- YOLO cukup baik dan jauh lebih cepat.
- Mask presisi belum tentu sepadan biayanya.
- Real-time memihak YOLO.

## Keunggulan
- Analisis trade-off praktis.
- Panduan pemilihan detektor.
- Fokus real-time.

## Keterbatasan
- Cakupan eksperimen terbatas.
- Bergantung implementasi detektor.
- Fokus objek manusia.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Studi ini langsung relevan bagi tema YOLO+RGB-D: mengukur peran YOLO (vs Mask R-CNN) dalam SLAM dinamis real-time pada tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SLAM** yang baik dibaca berdampingan:

- [107 - 2017 - ORB-SLAM2 - RGB-D SLAM](./107%20-%202017%20-%20ORB-SLAM2%20-%20RGB-D%20SLAM.md)
- [108 - 2018 - DynaSLAM - RGB-D SLAM](./108%20-%202018%20-%20DynaSLAM%20-%20RGB-D%20SLAM.md)
- [109 - 2018 - DS-SLAM - RGB-D SLAM](./109%20-%202018%20-%20DS-SLAM%20-%20RGB-D%20SLAM.md)
- [110 - 2022 - CFP-SLAM - RGB-D SLAM](./110%20-%202022%20-%20CFP-SLAM%20-%20RGB-D%20SLAM.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SLAM** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema RGB-D SLAM)
Istilah penting untuk memahami makalah ini:

- **SLAM** — Simultaneous Localization and Mapping.
- **RGB-D SLAM** — SLAM kamera warna+kedalaman (skala metrik).
- **Lingkungan dinamis** — Scene dengan objek bergerak.
- **Loop closure** — Pengenalan tempat untuk koreksi drift.
- **Bundle adjustment** — Optimasi bersama pose dan titik peta.
- **ATE/RPE** — Absolute/Relative Trajectory/Pose Error.
- **Semantic SLAM** — SLAM memanfaatkan label semantik.
- **Fitur ORB** — Fitur cepat rotasi-invarian.
- **TUM RGB-D** — Benchmark SLAM RGB-D standar.
- **Deteksi objek dinamis** — Menandai objek bergerak (YOLO/Mask R-CNN).

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
Soares dkk. membandingkan YOLO dan Mask R-CNN sebagai penyaring objek dinamis pada visual SLAM, menyimpulkan YOLO menawarkan kompromi kecepatan-akurasi menarik untuk lingkungan berpenghuni real-time.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `soares2019visualslam` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 111/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
