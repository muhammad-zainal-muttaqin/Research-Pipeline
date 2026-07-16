# 191 - DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 191 dari 191 |
| Kunci BibTeX | `teed2021droidslam` |
| Judul | DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras |
| Penulis | Teed, Zachary; Deng, Jia |
| Tahun | 2021 |
| Venue / Jurnal | Advances in Neural Information Processing Systems (NeurIPS) |
| Tema klaster | RGB-D SLAM |
| Kata kunci | deep SLAM, dense bundle adjustment, optical flow, RGB-D |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2108.10869
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=DROID-SLAM%3A%20Deep%20Visual%20SLAM%20for%20Monocular%2C%20Stereo%2C%20and%20RGB-D%20Cameras
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=DROID-SLAM%3A%20Deep%20Visual%20SLAM%20for%20Monocular%2C%20Stereo%2C%20and%20RGB-D%20Cameras&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2108.10869 |

## Ringkasan Eksekutif
DROID-SLAM adalah sistem SLAM berbasis deep learning yang memperbarui pose kamera dan depth secara iteratif melalui Dense Bundle Adjustment (DBA) yang dapat dilatih, mencapai akurasi dan robustnes tinggi untuk kamera monokular, stereo, dan RGB-D.

## Abstrak (Parafrase)
Penulis membangun SLAM di sekitar operator DBA layer yang dapat didiferensialkan: jaringan (mirip RAFT) memprediksi koreksi aliran optik antar-frame, lalu DBA memperbarui pose dan depth per-piksel secara konsisten geometris. Diulang dalam struktur rekuren, DROID-SLAM jauh mengungguli SLAM klasik dan deep sebelumnya dalam akurasi dan robustnes, dengan sedikit kegagalan tracking, dan mendukung mono/stereo/RGB-D.

## Latar Belakang & Konteks
SLAM klasik akurat tetapi rapuh pada kondisi sulit; metode deep sebelumnya sering kurang akurat. DROID-SLAM menyatukan pembelajaran dan optimasi geometris.

## Permasalahan yang Diangkat
- SLAM klasik rapuh (gerak cepat, tekstur miskin).
- Metode deep kurang akurat/geometris.
- Butuh pembaruan pose+depth yang konsisten.

## Tujuan & Pertanyaan Penelitian
- Menyatukan deep flow dan bundle adjustment.
- Pembaruan pose+depth iteratif terlatih.
- Akurasi dan robustnes tinggi lintas modalitas.

## Tinjauan Terdahulu / Posisi Literatur
Menggabungkan RAFT (optical flow) dan bundle adjustment; berdialog dengan ORB-SLAM3 dan DeepV2D.

Karya/konsep pembanding yang relevan:

- RAFT - optical flow rekuren.
- ORB-SLAM3 - SLAM fitur klasik.
- BA-Net/DeepV2D - deep SfM/SLAM.
- Bundle adjustment diferensiabel.

## Metodologi & Arsitektur
Graf frame; update operator memprediksi revisi korespondensi/flow dengan confidence; Dense Bundle Adjustment layer menyelesaikan pose kamera dan depth per-piksel; iterasi rekuren memperbaiki estimasi; mendukung mono/stereo/RGB-D.

Komponen / langkah metodologis utama:

- Update operator gaya RAFT (flow + bobot).
- Dense Bundle Adjustment layer diferensiabel.
- Pembaruan pose + depth per-piksel iteratif.
- Dukungan mono/stereo/RGB-D.

## Kontribusi Utama
1. SLAM dengan DBA layer terlatih end-to-end.
2. Akurasi/robustnes jauh di atas baseline.
3. Sedikit kegagalan tracking.
4. Generalisasi lintas modalitas kamera.

## Rincian Eksperimen
TartanAir, EuRoC, TUM-RGBD, dan ETH3D untuk ATE dan tingkat keberhasilan tracking.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| EuRoC | ATE | jauh lebih akurat dari baseline |
| TUM-RGBD | ATE | robust & akurat |
| TartanAir | ATE/success | sedikit kegagalan |

## Temuan Kunci
- Menyatukan deep flow + BA memberi akurasi tinggi.
- DBA diferensiabel menstabilkan geometri.
- Robust lintas kondisi sulit.

## Keunggulan
- Akurat & sangat robust.
- Serbaguna (mono/stereo/RGB-D).
- Sedikit kegagalan tracking.

## Keterbatasan
- Komputasi GPU besar.
- Memori tumbuh dengan graf frame.
- Objek dinamis tak ditangani eksplisit.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
SLAM RGB-D deep yang akurat, relevan untuk navigasi robot berbasis kamera+depth dan sistem persepsi 3D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SLAM** yang baik dibaca berdampingan:

- [190 - 2021 - ORB-SLAM3 - RGB-D SLAM](./190%20-%202021%20-%20ORB-SLAM3%20-%20RGB-D%20SLAM.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SLAM** dalam peta tinjauan (17 klaster, 191 entri total).
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
DROID-SLAM menyatukan deep learning dan bundle adjustment untuk SLAM yang akurat dan robust lintas modalitas, tonggak SLAM modern.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `teed2021droidslam` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 191/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
