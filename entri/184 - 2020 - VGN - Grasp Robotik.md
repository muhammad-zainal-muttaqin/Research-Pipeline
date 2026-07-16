# 184 - Volumetric Grasping Network: Real-Time 6 DOF Grasp Detection in Clutter

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 184 dari 191 |
| Kunci BibTeX | `breyer2021vgn` |
| Judul | Volumetric Grasping Network: Real-Time 6 DOF Grasp Detection in Clutter |
| Penulis | Breyer, Michel; Chung, Jen Jen; Ott, Lionel; Siegwart, Roland; Nieto, Juan |
| Tahun | 2020 |
| Venue / Jurnal | Conference on Robot Learning (CoRL) |
| Tema klaster | Grasp Robotik |
| Kata kunci | volumetric grasping, TSDF, real-time, 6-DoF grasp |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-grasp-robotik)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2101.01132
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Volumetric%20Grasping%20Network%3A%20Real-Time%206%20DOF%20Grasp%20Detection%20in%20Clutter
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Volumetric%20Grasping%20Network%3A%20Real-Time%206%20DOF%20Grasp%20Detection%20in%20Clutter&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2101.01132 |

## Ringkasan Eksekutif
VGN (Volumetric Grasping Network) memprediksi grasp 6-DoF secara real-time dari volume TSDF scene, menghasilkan peta kualitas grasp 3D dalam satu forward pass untuk decluttering cepat.

## Abstrak (Parafrase)
Penulis merepresentasikan scene sebagai Truncated Signed Distance Function (TSDF) volumetrik dari citra depth, lalu jaringan 3D-konvolusi memprediksi kualitas grasp, orientasi, dan lebar untuk setiap voxel sekaligus. Karena keluaran padat dihitung dalam satu pass, VGN menghasilkan grasp 6-DoF real-time dan berhasil membersihkan tumpukan objek pada eksperimen robot nyata.

## Latar Belakang & Konteks
Banyak metode grasp mengevaluasi kandidat satu per satu (lambat). Prediksi volumetrik padat memungkinkan grasp real-time.

## Permasalahan yang Diangkat
- Evaluasi grasp kandidat-per-kandidat lambat.
- Butuh grasp 6-DoF real-time.
- Integrasi geometri scene 3D.

## Tujuan & Pertanyaan Penelitian
- Prediksi grasp padat dari volume TSDF.
- Grasp 6-DoF real-time.
- Decluttering andal pada robot nyata.

## Tinjauan Terdahulu / Posisi Literatur
Berbeda dari sampling-evaluate (6-DOF GraspNet) dengan prediksi volumetrik satu-pass; berkaitan dengan GG-CNN (2D) yang diangkat ke 3D.

Karya/konsep pembanding yang relevan:

- GG-CNN - grasp generatif 2D real-time.
- 6-DOF GraspNet - sampling grasp.
- TSDF fusion - representasi volumetrik.
- 3D CNN untuk voxel.

## Metodologi & Arsitektur
Integrasikan beberapa citra depth ke TSDF; 3D CNN memprediksi peta kualitas grasp, orientasi (quaternion), dan lebar per-voxel; seleksi grasp terbaik lalu eksekusi robot.

Komponen / langkah metodologis utama:

- Representasi scene TSDF volumetrik.
- 3D CNN prediksi grasp padat.
- Keluaran kualitas+orientasi+lebar per-voxel.
- Inferensi satu-pass real-time.

## Kontribusi Utama
1. Jaringan grasp volumetrik real-time.
2. Prediksi grasp padat satu-pass.
3. Validasi robot nyata (declutter).
4. Dataset/simulasi grasp.

## Rincian Eksperimen
Simulasi (pile/packed scenes) dan robot nyata dengan metrik grasp/clearance success rate dan waktu inferensi.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Simulasi pile/packed | success rate | tinggi |
| Robot nyata | clearance rate | efektif declutter |
| Kecepatan | ms | real-time (satu pass) |

## Temuan Kunci
- Prediksi volumetrik padat memungkinkan grasp real-time.
- TSDF menyediakan geometri scene berguna.
- Satu-pass mengungguli sampling lambat.

## Keunggulan
- Real-time.
- Grasp 6-DoF padat.
- Tervalidasi robot nyata.

## Keterbatasan
- Resolusi voxel membatasi detail.
- Bergantung kualitas depth/TSDF.
- Volume besar mahal memori.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Metode grasp real-time berbasis depth, komponen praktis untuk sistem manipulasi RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Grasp Robotik** yang baik dibaca berdampingan:

- [183 - 2021 - Contact-GraspNet - Grasp Robotik](./183%20-%202021%20-%20Contact-GraspNet%20-%20Grasp%20Robotik.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Grasp Robotik** dalam peta tinjauan (17 klaster, 191 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Grasp Robotik)
Istilah penting untuk memahami makalah ini:

- **Grasp detection** — Prediksi cengkeraman stabil untuk objek.
- **Grasp rectangle** — Grasp sebagai kotak beorientasi (posisi, sudut, lebar).
- **Antipodal grasp** — Cengkeraman dua-jari berlawanan.
- **RGB-D** — Warna + kedalaman untuk geometri grasp.
- **6-DoF grasp** — Grasp enam derajat kebebasan di ruang 3D.
- **Cornell dataset** — Dataset grasp kecil klasik.
- **Jacquard** — Dataset grasp sintetis berskala besar.
- **Closed-loop** — Kontrol grasp real-time berbasis umpan-balik.
- **Success rate** — Persentase percobaan grasp berhasil.
- **Point cloud fusion** — Penggabungan geometri titik 3D.

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
VGN menghasilkan grasp 6-DoF real-time dari volume TSDF, mendukung decluttering robotik yang cepat dan andal.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `breyer2021vgn` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 184/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
