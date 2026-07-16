# 108 - DynaSLAM: Tracking, Mapping, and Inpainting in Dynamic Scenes

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 108 dari 154 |
| Kunci BibTeX | `bescos2018dynaslam` |
| Judul | DynaSLAM: Tracking, Mapping, and Inpainting in Dynamic Scenes |
| Penulis | Bescos, Berta; F{\'a |
| Tahun | 2018 |
| Venue / Jurnal | IEEE Robotics and Automation Letters |
| Tema klaster | RGB-D SLAM |
| Kata kunci | RGB-D SLAM, dinamis, Mask R-CNN, inpainting, ORB-SLAM2 |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=DynaSLAM%3A%20Tracking%2C%20Mapping%2C%20and%20Inpainting%20in%20Dynamic%20Scenes
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=DynaSLAM%3A%20Tracking%2C%20Mapping%2C%20and%20Inpainting%20in%20Dynamic%20Scenes&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 3 |
| Nomor | 4 |
| Halaman | 4076--4083 |

## Ringkasan Eksekutif
Perluasan ORB-SLAM2 yang menangani lingkungan dinamis dengan deteksi objek bergerak (Mask R-CNN + geometri multi-view) dan inpainting latar.

## Abstrak (Parafrase)
DynaSLAM memperluas ORB-SLAM2 untuk lingkungan dinamis: Mask R-CNN mensegmentasi objek berpotensi bergerak (orang, kendaraan) dan pemeriksaan geometri multi-view mendeteksi gerak nyata, lalu fitur pada objek dinamis dibuang dari SLAM. Background inpainting mengisi area yang tertutup objek bergerak untuk peta statis yang bersih. Akurasi pose meningkat drastis pada scene dinamis.

## Latar Belakang & Konteks
SLAM klasik (ORB-SLAM2) mengasumsikan scene statis dan gagal ketika banyak objek bergerak merusak asosiasi fitur dan estimasi pose.

## Permasalahan yang Diangkat
- SLAM klasik mengasumsikan scene statis.
- Objek bergerak merusak asosiasi fitur & pose.
- Fitur dinamis harus dibuang.
- Peta statis perlu bersih dari objek bergerak.
- Deteksi objek bergerak diperlukan.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi & membuang objek bergerak.
- Membersihkan peta via background inpainting.
- Meningkatkan akurasi pose pada scene dinamis.

## Tinjauan Terdahulu / Posisi Literatur
DynaSLAM menggabungkan segmentasi instan dan geometri untuk menyaring dinamika.

Karya/konsep pembanding yang relevan:

- ORB-SLAM2 — basis SLAM.
- Mask R-CNN — segmentasi objek bergerak.
- Multi-view geometry — deteksi gerak.
- Background inpainting — peta bersih.

## Metodologi & Arsitektur
Mask R-CNN mendeteksi objek berpotensi bergerak (prior kelas); multi-view geometry memverifikasi gerak nyata (kedalaman/reprojeksi); fitur pada objek dinamis dibuang sebelum tracking/mapping; background inpainting mengisi area tertutup untuk peta statis.

Komponen / langkah metodologis utama:

- Mask R-CNN untuk objek berpotensi bergerak.
- Multi-view geometry mendeteksi gerak nyata.
- Pembuangan fitur dinamis dari SLAM.
- Background inpainting (peta statis bersih).
- Berbasis ORB-SLAM2 (RGB-D).
- Evaluasi TUM RGB-D dinamis.

## Kontribusi Utama
1. Penyaringan objek dinamis (segmentasi + geometri).
2. Peta statis bersih via inpainting.
3. Peningkatan akurasi pose besar pada scene dinamis.
4. Contoh integrasi deteksi + SLAM.

## Rincian Eksperimen
Diuji pada TUM RGB-D (urutan dinamis) dengan metrik ATE/RPE, dibandingkan ORB-SLAM2.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| TUM RGB-D dinamis | ATE | jauh lebih baik dari ORB-SLAM2 |
| Peta statis | kualitas | bersih via inpainting |
| Ablation | geometry+CNN | keduanya menyumbang gain |

## Temuan Kunci
- Penyaringan objek dinamis penting untuk pose.
- Segmentasi + geometri saling melengkapi.
- Inpainting menghasilkan peta statis bersih.
- Deteksi objek meningkatkan SLAM dinamis.

## Keunggulan
- Akurasi tinggi pada scene dinamis.
- Peta statis bersih.
- Integrasi deteksi+SLAM.

## Keterbatasan
- Mask R-CNN lambat (bukan real-time penuh).
- Bergantung kualitas segmentasi.
- Inpainting menambah komputasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
DynaSLAM adalah contoh kunci integrasi deteksi/segmentasi ke SLAM RGB-D dalam tinjauan, menegaskan peran deteksi objek bagi robustness SLAM dinamis.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SLAM** yang baik dibaca berdampingan:

- [107 - 2017 - ORB-SLAM2 - RGB-D SLAM](./107%20-%202017%20-%20ORB-SLAM2%20-%20RGB-D%20SLAM.md)
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
DynaSLAM memperluas ORB-SLAM2 dengan Mask R-CNN, geometri multi-view, dan background inpainting untuk menangani lingkungan dinamis, meningkatkan akurasi pose secara drastis.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `bescos2018dynaslam` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 108/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
