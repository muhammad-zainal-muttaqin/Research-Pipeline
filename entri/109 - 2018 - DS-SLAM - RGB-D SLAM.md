# 109 - DS-SLAM: A Semantic Visual SLAM towards Dynamic Environments

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 109 dari 154 |
| Kunci BibTeX | `yu2018dsslam` |
| Judul | DS-SLAM: A Semantic Visual SLAM towards Dynamic Environments |
| Penulis | Yu, Chao; Liu, Zuxin; Liu, Xin-Jun; Xie, Fugui; Yang, Yi; Wei, Qi; Fei, Qiao |
| Tahun | 2018 |
| Venue / Jurnal | Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) |
| Tema klaster | RGB-D SLAM |
| Kata kunci | RGB-D SLAM, semantik, SegNet, dinamis, oktomap |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=DS-SLAM%3A%20A%20Semantic%20Visual%20SLAM%20towards%20Dynamic%20Environments
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=DS-SLAM%3A%20A%20Semantic%20Visual%20SLAM%20towards%20Dynamic%20Environments&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 1168--1174 |

## Ringkasan Eksekutif
SLAM semantik untuk lingkungan dinamis yang menggabungkan segmentasi (SegNet) dan pemeriksaan konsistensi gerak, membangun peta semantik oktomap.

## Abstrak (Parafrase)
DS-SLAM menggabungkan segmentasi semantik real-time (SegNet) dengan moving consistency check (berbasis optical flow/geometri) untuk mengidentifikasi dan membuang titik dinamis, sehingga akurasi pose meningkat pada scene dinamis. Ia juga membangun peta semantik oktomap. Dibangun di atas ORB-SLAM2.

## Latar Belakang & Konteks
Objek dinamis menurunkan akurasi pose SLAM; menggabungkan isyarat semantik (kelas berpotensi bergerak) dan geometri (gerak nyata) dapat menyaringnya.

## Permasalahan yang Diangkat
- Objek dinamis menurunkan akurasi pose.
- Semantik saja tak cukup (objek statis salah dibuang).
- Geometri saja rawan noise.
- Peta perlu informasi semantik.
- Real-time diinginkan.

## Tujuan & Pertanyaan Penelitian
- Menggabungkan semantik & konsistensi gerak.
- Membuang titik dinamis untuk pose akurat.
- Membangun peta semantik oktomap.

## Tinjauan Terdahulu / Posisi Literatur
DS-SLAM menggabungkan semantik dan geometri di atas ORB-SLAM2.

Karya/konsep pembanding yang relevan:

- ORB-SLAM2 — basis SLAM.
- SegNet — segmentasi semantik real-time.
- Moving consistency check — geometri.
- Octomap — peta semantik.

## Metodologi & Arsitektur
SegNet mensegmentasi kelas (mis. orang) secara real-time di thread terpisah; moving consistency check memverifikasi gerak titik; titik dinamis (kelas bergerak + gerak terverifikasi) dibuang; peta semantik oktomap dibangun; berbasis ORB-SLAM2.

Komponen / langkah metodologis utama:

- SegNet segmentasi semantik (thread terpisah).
- Moving consistency check (gerak nyata).
- Pembuangan titik dinamis.
- Peta semantik oktomap.
- Berbasis ORB-SLAM2 (RGB-D).
- Evaluasi TUM RGB-D dinamis.

## Kontribusi Utama
1. SLAM semantik dinamis (semantik + geometri).
2. Pembuangan titik dinamis menurunkan galat.
3. Peta semantik oktomap.
4. Contoh awal integrasi semantik-SLAM.

## Rincian Eksperimen
Diuji pada TUM RGB-D dinamis dengan metrik ATE/RPE, dibandingkan ORB-SLAM2.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| TUM RGB-D dinamis | ATE/RPE | penurunan galat signifikan |
| Peta | semantik | oktomap dibangun |
| Ablation | semantik+geometri | keduanya menyumbang gain |

## Temuan Kunci
- Semantik + geometri lebih baik dari salah satu saja.
- Titik dinamis efektif dibuang.
- Peta semantik bermanfaat.
- Real-time layak dengan thread terpisah.

## Keunggulan
- Semantik + geometri.
- Peta semantik.
- Menurunkan galat dinamis.

## Keterbatasan
- Bergantung kualitas segmentasi.
- Kelas terbatas (SegNet).
- Overhead segmentasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
DS-SLAM adalah contoh awal SLAM semantik dinamis dalam tinjauan; relevan bagi integrasi deteksi/segmentasi (termasuk YOLO) ke SLAM RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SLAM** yang baik dibaca berdampingan:

- [107 - 2017 - ORB-SLAM2 - RGB-D SLAM](./107%20-%202017%20-%20ORB-SLAM2%20-%20RGB-D%20SLAM.md)
- [108 - 2018 - DynaSLAM - RGB-D SLAM](./108%20-%202018%20-%20DynaSLAM%20-%20RGB-D%20SLAM.md)
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
DS-SLAM menggabungkan segmentasi SegNet dan pemeriksaan konsistensi gerak untuk SLAM robust di lingkungan dinamis, membangun peta semantik oktomap di atas ORB-SLAM2.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `yu2018dsslam` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 109/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
