# 107 - ORB-SLAM2: An Open-Source SLAM System for Monocular, Stereo, and RGB-D Cameras

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 107 dari 154 |
| Kunci BibTeX | `murartal2017orbslam2` |
| Judul | ORB-SLAM2: An Open-Source SLAM System for Monocular, Stereo, and RGB-D Cameras |
| Penulis | Mur-Artal, Ra{\'u |
| Tahun | 2017 |
| Venue / Jurnal | IEEE Transactions on Robotics |
| Tema klaster | RGB-D SLAM |
| Kata kunci | RGB-D SLAM, open-source, stereo/mono/RGB-D, loop closure, ORB |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=ORB-SLAM2%3A%20An%20Open-Source%20SLAM%20System%20for%20Monocular%2C%20Stereo%2C%20and%20RGB-D%20Cameras
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=ORB-SLAM2%3A%20An%20Open-Source%20SLAM%20System%20for%20Monocular%2C%20Stereo%2C%20and%20RGB-D%20Cameras&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 33 |
| Nomor | 5 |
| Halaman | 1255--1262 |

## Ringkasan Eksekutif
Sistem SLAM lengkap sumber-terbuka untuk kamera monokular, stereo, dan RGB-D dengan tracking, mapping, relokalisasi, dan loop closing berbasis fitur ORB.

## Abstrak (Parafrase)
ORB-SLAM2 adalah sistem SLAM berbasis fitur yang lengkap dan andal untuk tiga jenis kamera (monokular, stereo, RGB-D). Ia mencakup tracking, local mapping, loop closing, dan relokalisasi, memakai fitur ORB yang cepat dan bundle adjustment untuk akurasi. Mode RGB-D memberi skala metrik langsung. Sistem berjalan real-time pada CPU dan menjadi baseline SLAM paling berpengaruh.

## Latar Belakang & Konteks
Dibutuhkan sistem SLAM yang andal, akurat, real-time, dan serbaguna lintas jenis kamera, dengan penanganan drift (loop closure) dan kegagalan tracking (relokalisasi).

## Permasalahan yang Diangkat
- Perlu SLAM andal & akurat lintas jenis kamera.
- Drift akumulatif memerlukan loop closure.
- Kegagalan tracking memerlukan relokalisasi.
- Real-time pada CPU diinginkan.
- Skala metrik penting (RGB-D/stereo).

## Tujuan & Pertanyaan Penelitian
- Menyediakan SLAM lengkap mono/stereo/RGB-D.
- Menangani drift via loop closing & BA.
- Menyediakan relokalisasi yang andal.

## Tinjauan Terdahulu / Posisi Literatur
ORB-SLAM2 menyempurnakan ORB-SLAM (monokular) ke stereo/RGB-D.

Karya/konsep pembanding yang relevan:

- ORB-SLAM (monokular) — pendahulu.
- Fitur ORB — cepat & rotasi-invarian.
- Bundle adjustment — akurasi.
- DBoW2 — loop closure/relokalisasi.

## Metodologi & Arsitektur
Tiga thread paralel: tracking (estimasi pose per-frame via fitur ORB), local mapping (menyempurnakan peta + local BA), dan loop closing (deteksi loop via bag-of-words + pose graph optimization + full BA); mode RGB-D memakai kedalaman untuk skala metrik dan inisialisasi cepat.

Komponen / langkah metodologis utama:

- Fitur ORB untuk tracking & pemetaan.
- Tiga thread: tracking, mapping, loop closing.
- Bundle adjustment (local & full).
- Loop closure + relokalisasi (DBoW2).
- Mode RGB-D (skala metrik langsung).
- Real-time pada CPU.

## Kontribusi Utama
1. Sistem SLAM lengkap & serbaguna (mono/stereo/RGB-D).
2. Loop closing + relokalisasi andal.
3. Akurasi tinggi (bundle adjustment).
4. Baseline SLAM paling berpengaruh, open-source.

## Rincian Eksperimen
Diuji pada KITTI, EuRoC, dan TUM RGB-D dengan metrik akurasi trajektori (ATE/RPE) dan kecepatan, dibandingkan sistem SLAM lain.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| TUM RGB-D | ATE | akurasi tinggi (statis) |
| KITTI/EuRoC | ATE/RPE | SOTA saat rilis |
| Kecepatan | real-time | CPU real-time |

## Temuan Kunci
- SLAM berbasis fitur andal & akurat.
- Loop closure krusial menekan drift.
- RGB-D memberi skala metrik langsung.
- Lemah pada lingkungan dinamis (motivasi turunan).

## Keunggulan
- Lengkap & serbaguna.
- Akurat & real-time (CPU).
- Open-source berpengaruh.

## Keterbatasan
- Rentan pada lingkungan dinamis.
- Berbasis fitur (gagal pada tekstur minim).
- Tak menangani objek bergerak.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
ORB-SLAM2 adalah fondasi klaster RGB-D SLAM dalam tinjauan dan basis banyak SLAM dinamis (DynaSLAM, DS-SLAM, CFP-SLAM) yang mengintegrasikan deteksi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SLAM** yang baik dibaca berdampingan:

- [108 - 2018 - DynaSLAM - RGB-D SLAM](./108%20-%202018%20-%20DynaSLAM%20-%20RGB-D%20SLAM.md)
- [109 - 2018 - DS-SLAM - RGB-D SLAM](./109%20-%202018%20-%20DS-SLAM%20-%20RGB-D%20SLAM.md)
- [110 - 2022 - CFP-SLAM - RGB-D SLAM](./110%20-%202022%20-%20CFP-SLAM%20-%20RGB-D%20SLAM.md)
- [111 - 2019 - Visual SLAM YOLO vs Mask R-CNN (Soares dkk.) - RGB-D SLAM](./111%20-%202019%20-%20Visual%20SLAM%20YOLO%20vs%20Mask%20R-CNN%20%28Soares%20dkk.%29%20-%20RGB-D%20SLAM.md)

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
ORB-SLAM2 menyediakan SLAM lengkap sumber-terbuka untuk mono/stereo/RGB-D dengan tracking, loop closing, dan relokalisasi berbasis ORB, menjadi baseline SLAM RGB-D paling berpengaruh.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `murartal2017orbslam2` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 107/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
