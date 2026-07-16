# 181 - ZebraPose: Coarse to Fine Surface Encoding for 6DoF Object Pose Estimation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 181 dari 191 |
| Kunci BibTeX | `su2022zebrapose` |
| Judul | ZebraPose: Coarse to Fine Surface Encoding for 6DoF Object Pose Estimation |
| Penulis | Su, Yongzhi; Saleh, Mahdi; Fetzer, Torben; Rambach, Jason; Navab, Nassir; Busam, Benjamin; Stricker, Didier; Tombari, Federico |
| Tahun | 2022 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Pose 6D |
| Kata kunci | 6D pose, surface encoding, coarse-to-fine, correspondence |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=ZebraPose%3A%20Coarse%20to%20Fine%20Surface%20Encoding%20for%206DoF%20Object%20Pose%20Estimation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=ZebraPose%3A%20Coarse%20to%20Fine%20Surface%20Encoding%20for%206DoF%20Object%20Pose%20Estimation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
ZebraPose mengodekan permukaan objek 3D dengan kode biner hierarkis (coarse-to-fine) sehingga jaringan memprediksi korespondensi permukaan padat secara bertahap-teliti, menghasilkan pose 6D yang sangat akurat.

## Abstrak (Parafrase)
Penulis merepresentasikan setiap verteks permukaan objek sebagai kode biner bertingkat (mirip pola zebra) yang membagi permukaan secara hierarkis. Jaringan memprediksi bit-bit kode per-piksel, membangun korespondensi 2D-3D padat dari kasar ke halus, lalu menyelesaikan pose via PnP. Pendekatan ini mencapai akurasi SOTA pada LineMOD, Occlusion, dan YCB-Video.

## Latar Belakang & Konteks
Kualitas korespondensi menentukan akurasi pose berbasis PnP. Pengodean permukaan yang efisien dan teliti meningkatkan korespondensi.

## Permasalahan yang Diangkat
- Korespondensi permukaan kurang teliti.
- Representasi permukaan padat mahal.
- Oklusi menurunkan korespondensi.

## Tujuan & Pertanyaan Penelitian
- Mengodekan permukaan secara hierarkis efisien.
- Membangun korespondensi coarse-to-fine.
- Meningkatkan akurasi pose.

## Tinjauan Terdahulu / Posisi Literatur
Melanjutkan DPOD/GDR-Net (korespondensi dense) dengan skema pengodean biner hierarkis baru.

Karya/konsep pembanding yang relevan:

- GDR-Net - geometry-guided regression.
- DPOD - dense correspondence.
- SurfEmb - embedding permukaan.
- PVNet - voting keypoint.

## Metodologi & Arsitektur
Bagi permukaan objek menjadi grup hierarkis, tiap verteks diberi kode biner bertingkat; jaringan memprediksi bit per-piksel untuk membentuk korespondensi 2D-3D; pose dihitung via PnP/RANSAC.

Komponen / langkah metodologis utama:

- Pengodean permukaan biner hierarkis.
- Prediksi bit per-piksel (coarse-to-fine).
- Korespondensi 2D-3D padat.
- PnP/RANSAC untuk pose.

## Kontribusi Utama
1. Surface encoding biner hierarkis.
2. Korespondensi padat teliti.
3. SOTA pose pada beberapa benchmark.
4. Robust terhadap oklusi.

## Rincian Eksperimen
LineMOD, Occlusion LineMOD, YCB-Video dengan ADD(-S) dan metrik korespondensi.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| LineMOD | ADD(-S) | SOTA saat rilis |
| Occlusion LM | ADD(-S) | unggul pada oklusi |
| YCB-Video | AUC | akurasi tinggi |

## Temuan Kunci
- Pengodean hierarkis meningkatkan ketelitian korespondensi.
- Coarse-to-fine efisien dan akurat.
- Robust terhadap oklusi parsial.

## Keunggulan
- Akurasi SOTA.
- Robust oklusi.
- Representasi efisien.

## Keterbatasan
- Butuh model CAD.
- Pelatihan per-objek/pengodean.
- Bergantung deteksi awal.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Metode pose 6D akurat melengkapi persepsi RGB-D untuk manipulasi robotik presisi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pose 6D** yang baik dibaca berdampingan:

- [180 - 2021 - GDR-Net - Pose 6D](./180%20-%202021%20-%20GDR-Net%20-%20Pose%206D.md)
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
ZebraPose menghadirkan pengodean permukaan hierarkis yang menghasilkan korespondensi padat dan pose 6D SOTA.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `su2022zebrapose` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 181/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
