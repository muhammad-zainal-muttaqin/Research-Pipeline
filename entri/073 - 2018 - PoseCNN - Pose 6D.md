# 073 - PoseCNN: A Convolutional Neural Network for 6D Object Pose Estimation in Cluttered Scenes

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 073 dari 154 |
| Kunci BibTeX | `xiang2018posecnn` |
| Judul | PoseCNN: A Convolutional Neural Network for 6D Object Pose Estimation in Cluttered Scenes |
| Penulis | Xiang, Yu; Schmidt, Tanner; Narayanan, Venkatraman; Fox, Dieter |
| Tahun | 2018 |
| Venue / Jurnal | Robotics: Science and Systems (RSS) |
| Tema klaster | Pose 6D |
| Kata kunci | pose 6D, RGB-D, decoupling, Hough voting, YCB-Video |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=PoseCNN%3A%20A%20Convolutional%20Neural%20Network%20for%206D%20Object%20Pose%20Estimation%20in%20Cluttered%20Scenes
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=PoseCNN%3A%20A%20Convolutional%20Neural%20Network%20for%206D%20Object%20Pose%20Estimation%20in%20Cluttered%20Scenes&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
Jaringan pelopor estimasi pose 6D objek yang memisahkan prediksi label semantik, translasi (voting arah pusat + kedalaman), dan rotasi (kuaternion), serta memperkenalkan dataset YCB-Video.

## Abstrak (Parafrase)
PoseCNN mengestimasi pose 6D dengan mendekomposisi masalah: cabang segmentasi semantik, cabang translasi yang memvoting arah ke pusat objek lalu mengestimasi kedalaman, dan cabang rotasi yang meregresi kuaternion. ShapeMatch loss menangani objek simetris. Makalah juga memperkenalkan dataset YCB-Video yang menjadi benchmark penting.

## Latar Belakang & Konteks
Estimasi pose 6D pada scene berantakan dengan oklusi dan objek simetris sangat sulit; regresi pose langsung tidak stabil dan objek simetris menimbulkan ambiguitas rotasi.

## Permasalahan yang Diangkat
- Scene berantakan & oklusi menyulitkan pose 6D.
- Regresi pose langsung tidak stabil.
- Objek simetris menimbulkan ambiguitas rotasi.
- Translasi & rotasi memerlukan perlakuan berbeda.
- Benchmark pose 6D masih terbatas.

## Tujuan & Pertanyaan Penelitian
- Mendekomposisi estimasi pose 6D.
- Menangani objek simetris (ShapeMatch loss).
- Menyediakan benchmark YCB-Video.

## Tinjauan Terdahulu / Posisi Literatur
PoseCNN pelopor pose 6D berbasis CNN dengan dekomposisi tugas.

Karya/konsep pembanding yang relevan:

- Deteksi/segmentasi CNN — dasar.
- Hough voting — estimasi pusat.
- Kuaternion — representasi rotasi.
- ShapeMatch loss — objek simetris.

## Metodologi & Arsitektur
Jaringan menghasilkan segmentasi semantik; cabang translasi memvoting arah menuju pusat objek per-piksel lalu mengestimasi kedalaman pusat; cabang rotasi meregresi kuaternion per-objek; ShapeMatch loss menangani simetri; RGB (dan opsional depth) sebagai input.

Komponen / langkah metodologis utama:

- Cabang segmentasi semantik.
- Cabang translasi (Hough voting pusat + kedalaman).
- Cabang rotasi (regresi kuaternion).
- Decoupling translasi & rotasi.
- ShapeMatch loss untuk simetri.
- Dataset YCB-Video baru.

## Kontribusi Utama
1. Dekomposisi translasi/rotasi menstabilkan pose.
2. Hough voting robust terhadap oklusi.
3. ShapeMatch loss menangani objek simetris.
4. Dataset YCB-Video sebagai benchmark penting.

## Rincian Eksperimen
Diuji pada YCB-Video dan OccludedLINEMOD dengan metrik ADD/ADD-S, menjadi baseline pose 6D.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| YCB-Video | ADD-S | baseline pose 6D penting |
| OccludedLINEMOD | ADD | robust terhadap oklusi |
| Ablation | decoupling/ShapeMatch | keduanya menyumbang gain |

## Temuan Kunci
- Decoupling translasi-rotasi efektif.
- Voting pusat robust terhadap oklusi.
- Simetri objek harus ditangani eksplisit.
- Meletakkan dasar pose 6D CNN modern.

## Keunggulan
- Pelopor pose 6D CNN.
- Menangani simetri & oklusi.
- Dataset YCB-Video.

## Keterbatasan
- Akurasi di bawah metode fusi RGB-D berikutnya.
- Rotasi via regresi langsung terbatas.
- Butuh refinement (ICP) untuk presisi tinggi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
PoseCNN adalah fondasi klaster Pose 6D dalam tinjauan dan sumber benchmark YCB-Video; menegaskan peran kedalaman/geometri untuk lokalisasi 3D objek.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pose 6D** yang baik dibaca berdampingan:

- [074 - 2019 - DenseFusion - Pose 6D](./074%20-%202019%20-%20DenseFusion%20-%20Pose%206D.md)
- [075 - 2020 - PVN3D - Pose 6D](./075%20-%202020%20-%20PVN3D%20-%20Pose%206D.md)
- [076 - 2021 - FFB6D - Pose 6D](./076%20-%202021%20-%20FFB6D%20-%20Pose%206D.md)
- [077 - 2020 - G2L-Net - Pose 6D](./077%20-%202020%20-%20G2L-Net%20-%20Pose%206D.md)
- [078 - 2024 - FoundationPose - Pose 6D](./078%20-%202024%20-%20FoundationPose%20-%20Pose%206D.md)
- [079 - 2021 - Review Pose 6D & Deteksi 3D (Hoque dkk.) - Pose 6D](./079%20-%202021%20-%20Review%20Pose%206D%20%26%20Deteksi%203D%20%28Hoque%20dkk.%29%20-%20Pose%206D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Pose 6D** dalam peta tinjauan (17 klaster, 154 entri total).
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
PoseCNN mempelopori pose 6D berbasis CNN dengan dekomposisi translasi-rotasi, Hough voting, dan ShapeMatch loss, serta memperkenalkan benchmark YCB-Video.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `xiang2018posecnn` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 073/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
