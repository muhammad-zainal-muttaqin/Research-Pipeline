# 077 - G2L-Net: Global to Local Network for Real-Time 6D Pose Estimation with Embedding Vector Features

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 077 dari 154 |
| Kunci BibTeX | `chen2020g2lnet` |
| Judul | G2L-Net: Global to Local Network for Real-Time 6D Pose Estimation with Embedding Vector Features |
| Penulis | Chen, Wei; Jia, Xi; Chang, Hyung Jin; Duan, Jinming; Leonardis, Ales |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Pose 6D |
| Kata kunci | pose 6D, RGB-D, global-to-local, real-time, embedding vector |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=G2L-Net%3A%20Global%20to%20Local%20Network%20for%20Real-Time%206D%20Pose%20Estimation%20with%20Embedding%20Vector%20Features
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=G2L-Net%3A%20Global%20to%20Local%20Network%20for%20Real-Time%206D%20Pose%20Estimation%20with%20Embedding%20Vector%20Features&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 4233--4242 |

## Ringkasan Eksekutif
Jaringan pose 6D real-time yang memakai pendekatan global-ke-lokal: deteksi 3D kasar, transformasi ke koordinat objek, lalu embedding vektor untuk rotasi.

## Abstrak (Parafrase)
G2L-Net (Global to Local) mengestimasi pose 6D secara real-time melalui tahapan: melokalisasi objek kasar dalam 3D (global), mentransformasi point cloud ke koordinat objek, lalu memprediksi rotasi via point-wise embedding vector features. Pendekatan bertahap ini efisien dan akurat pada LineMOD dan YCB-Video.

## Latar Belakang & Konteks
Estimasi pose 6D yang sekaligus akurat dan real-time pada RGB-D sulit; pemrosesan seluruh ruang 3D mahal.

## Permasalahan yang Diangkat
- Pose 6D akurat + real-time sulit dicapai.
- Pemrosesan seluruh ruang 3D mahal.
- Rotasi sulit diprediksi langsung.
- Oklusi menyulitkan pose.
- Efisiensi penting untuk robotika.

## Tujuan & Pertanyaan Penelitian
- Melokalisasi objek kasar (global) lebih dulu.
- Mentransformasi ke koordinat objek (lokal).
- Memprediksi rotasi via embedding vector.

## Tinjauan Terdahulu / Posisi Literatur
G2L-Net mengembangkan pose berbasis point cloud yang efisien.

Karya/konsep pembanding yang relevan:

- DenseFusion/PVN3D — pose RGB-D (pembanding).
- PointNet — fitur point cloud.
- Global localization + local refinement.
- Embedding vector features.

## Metodologi & Arsitektur
Tahap global melokalisasi objek dan mengekstrak point cloud objek; transformasi ke koordinat objek; jaringan point-wise memprediksi translasi residual dan rotasi via embedding vector features; pipeline dioptimasi untuk real-time.

Komponen / langkah metodologis utama:

- Global localization (deteksi 3D kasar).
- Transformasi ke koordinat objek.
- Point-wise embedding vector features.
- Prediksi rotasi via embedding.
- Refinement translasi residual.
- Real-time RGB-D.

## Kontribusi Utama
1. Pendekatan global-ke-lokal yang efisien.
2. Embedding vector features untuk rotasi.
3. Akurat dan real-time.
4. Pose 6D RGB-D praktis.

## Rincian Eksperimen
Diuji pada LineMOD dan YCB-Video dengan metrik ADD/ADD-S dan pengukuran kecepatan, dibandingkan DenseFusion dan PVN3D.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| LineMOD | ADD | akurat dan real-time |
| YCB-Video | ADD-S | kompetitif |
| Kecepatan | FPS | real-time |

## Temuan Kunci
- Strategi global-lokal efisien untuk pose.
- Embedding vector efektif untuk rotasi.
- Real-time tercapai tanpa mengorbankan akurasi.
- Transformasi koordinat objek membantu.

## Keunggulan
- Efisien & real-time.
- Global-ke-lokal.
- Embedding rotasi.

## Keterbatasan
- Bergantung kualitas point cloud.
- Lokalisasi kasar memengaruhi tahap lokal.
- Butuh model objek.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
G2L-Net menawarkan pose 6D RGB-D efisien yang relevan bagi robotika real-time (grasp) dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pose 6D** yang baik dibaca berdampingan:

- [073 - 2018 - PoseCNN - Pose 6D](./073%20-%202018%20-%20PoseCNN%20-%20Pose%206D.md)
- [074 - 2019 - DenseFusion - Pose 6D](./074%20-%202019%20-%20DenseFusion%20-%20Pose%206D.md)
- [075 - 2020 - PVN3D - Pose 6D](./075%20-%202020%20-%20PVN3D%20-%20Pose%206D.md)
- [076 - 2021 - FFB6D - Pose 6D](./076%20-%202021%20-%20FFB6D%20-%20Pose%206D.md)
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
G2L-Net mengestimasi pose 6D RGB-D secara real-time dengan strategi global-ke-lokal dan point-wise embedding vector features untuk rotasi, menyeimbangkan akurasi dan efisiensi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `chen2020g2lnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 077/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
