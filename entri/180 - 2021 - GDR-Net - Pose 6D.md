# 180 - GDR-Net: Geometry-Guided Direct Regression Network for Monocular 6D Object Pose Estimation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 180 dari 191 |
| Kunci BibTeX | `wang2021gdrnet` |
| Judul | GDR-Net: Geometry-Guided Direct Regression Network for Monocular 6D Object Pose Estimation |
| Penulis | Wang, Gu; Manhardt, Fabian; Tombari, Federico; Ji, Xiangyang |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Pose 6D |
| Kata kunci | 6D pose, monocular RGB, geometry-guided, direct regression |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-pose-6d)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=GDR-Net%3A%20Geometry-Guided%20Direct%20Regression%20Network%20for%20Monocular%206D%20Object%20Pose%20Estimation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=GDR-Net%3A%20Geometry-Guided%20Direct%20Regression%20Network%20for%20Monocular%206D%20Object%20Pose%20Estimation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
GDR-Net memadukan keunggulan metode berbasis korespondensi (Geometry) dan regresi langsung untuk estimasi pose 6D dari RGB tunggal, meregresi pose secara end-to-end dari representasi geometris perantara yang dipelajari.

## Abstrak (Parafrase)
Penulis berargumen regresi pose langsung dan metode PnP berbasis korespondensi memiliki kelebihan komplementer. GDR-Net memprediksi peta koordinat objek dense (dan region) sebagai representasi geometris, lalu meregresi pose 6D langsung melalui Patch-PnP yang dapat dilatih end-to-end. Ini menghasilkan pose akurat dari RGB tanpa depth, mengungguli metode sebelumnya pada LineMOD dan YCB-V.

## Latar Belakang & Konteks
Metode pose RGB-only umumnya memakai PnP tak-terlatih atas korespondensi, memutus aliran gradien. GDR-Net menyatukannya secara end-to-end.

## Permasalahan yang Diangkat
- PnP tak-terlatih memutus end-to-end.
- Regresi langsung kurang akurat sendirian.
- Pose dari RGB tunggal sulit (oklusi/simetri).

## Tujuan & Pertanyaan Penelitian
- Menyatukan geometri dan regresi langsung.
- Membuat PnP dapat dilatih (Patch-PnP).
- Meningkatkan akurasi pose RGB-only.

## Tinjauan Terdahulu / Posisi Literatur
Berpijak pada PVNet/DPOD (korespondensi) dan PoseCNN (regresi); kebaruan pada Patch-PnP terlatih.

Karya/konsep pembanding yang relevan:

- PoseCNN - regresi pose langsung.
- PVNet - voting keypoint.
- DPOD - dense correspondence.
- CDPN - decoupled pose.

## Metodologi & Arsitektur
Deteksi + zoom-in ROI; jaringan memprediksi dense correspondence map (koordinat objek) dan mask/region; Patch-PnP meregresi pose 6D dari peta ini secara end-to-end.

Komponen / langkah metodologis utama:

- Peta koordinat objek dense (geometri).
- Prediksi region/mask objek.
- Patch-PnP terlatih end-to-end.
- Zoom-in ROI untuk detail.

## Kontribusi Utama
1. Kerangka geometry-guided direct regression.
2. Patch-PnP yang dapat dilatih.
3. SOTA pose RGB-only saat rilis.
4. Menyatukan dua paradigma pose.

## Rincian Eksperimen
LineMOD, Occlusion LineMOD, dan YCB-Video dengan metrik ADD(-S), evaluasi ketahanan terhadap oklusi.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| LineMOD | ADD(-S) | SOTA RGB-only saat rilis |
| Occlusion LM | ADD(-S) | robust terhadap oklusi |
| YCB-Video | AUC ADD-S | akurat tanpa depth |

## Temuan Kunci
- Menyatukan geometri+regresi meningkatkan akurasi.
- PnP terlatih menjaga aliran gradien.
- Representasi koordinat dense efektif.

## Keunggulan
- RGB-only (tanpa depth).
- Akurat dan robust oklusi.
- End-to-end.

## Keterbatasan
- Butuh model CAD/koordinat objek.
- Objek simetris tetap menantang.
- Perlu deteksi/ROI yang baik.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Estimasi pose 6D dari RGB memperluas kemampuan sistem yang tak selalu punya depth andal, melengkapi pendekatan RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pose 6D** yang baik dibaca berdampingan:

- [181 - 2022 - ZebraPose - Pose 6D](./181%20-%202022%20-%20ZebraPose%20-%20Pose%206D.md)
- [182 - 2022 - OnePose - Pose 6D](./182%20-%202022%20-%20OnePose%20-%20Pose%206D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Pose 6D** dalam peta tinjauan (17 klaster, 191 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Pose 6D)
Istilah penting untuk memahami makalah ini:

- **Pose 6D** — Tiga translasi + tiga rotasi objek relatif kamera.
- **RGB-D** — Citra warna berpasangan peta kedalaman.
- **Point cloud** — Himpunan titik 3D dari depth/LiDAR.
- **Keypoint voting** — Titik memilih lokasi keypoint 3D untuk pose.
- **ADD/ADD-S** — Metrik pose: rata-rata jarak titik model (S=simetris).
- **Fusi dense** — Penggabungan fitur RGB dan geometri per-titik.
- **YCB-Video** — Dataset pose 6D scene berantakan.
- **LineMOD** — Dataset pose 6D objek tunggal klasik.
- **Refinement iteratif** — Penyempurnaan pose bertahap (ICP/jaringan).
- **Oklusi** — Objek terhalang sebagian.

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
GDR-Net menyatukan geometri dan regresi langsung dengan Patch-PnP terlatih, menghasilkan pose 6D RGB-only yang akurat.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wang2021gdrnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 180/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
