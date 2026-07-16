# 074 - DenseFusion: 6D Object Pose Estimation by Iterative Dense Fusion

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 074 dari 154 |
| Kunci BibTeX | `wang2019densefusion` |
| Judul | DenseFusion: 6D Object Pose Estimation by Iterative Dense Fusion |
| Penulis | Wang, Chen; Xu, Danfei; Zhu, Yuke; Mart{\'i |
| Tahun | 2019 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Pose 6D |
| Kata kunci | pose 6D, RGB-D, dense fusion, iterative refinement, per-pixel |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=DenseFusion%3A%206D%20Object%20Pose%20Estimation%20by%20Iterative%20Dense%20Fusion
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=DenseFusion%3A%206D%20Object%20Pose%20Estimation%20by%20Iterative%20Dense%20Fusion&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 3343--3352 |

## Ringkasan Eksekutif
Metode estimasi pose 6D RGB-D yang menyatukan fitur RGB dan point cloud kedalaman secara per-piksel (dense) lalu memurnikan pose secara iteratif.

## Abstrak (Parafrase)
DenseFusion mengekstrak fitur RGB (CNN) dan geometri dari point cloud kedalaman (PointNet-like) lalu menggabungkannya secara per-piksel (dense fusion), sehingga tiap titik memiliki embedding warna+geometri. Pose diestimasi per-titik lalu diagregasi, dan sebuah jaringan refinement iteratif menyempurnakannya. Hasilnya SOTA real-time saat rilis.

## Latar Belakang & Konteks
Fusi RGB-D tingkat-global kehilangan detail lokal penting untuk pose presisi, dan pendekatan yang mengandalkan ICP mahal secara komputasi.

## Permasalahan yang Diangkat
- Fusi RGB-D tingkat-global kehilangan detail lokal.
- ICP untuk refinement mahal secara komputasi.
- Pose presisi butuh fusi warna+geometri lokal.
- Oklusi menyulitkan estimasi pose.
- Real-time diperlukan untuk robotika.

## Tujuan & Pertanyaan Penelitian
- Menyatukan RGB & geometri secara per-piksel.
- Mengestimasi pose per-titik lalu agregasi.
- Memurnikan pose via refinement iteratif (bukan ICP).

## Tinjauan Terdahulu / Posisi Literatur
DenseFusion mengembangkan fusi RGB-D dense untuk pose.

Karya/konsep pembanding yang relevan:

- PoseCNN — pose 6D (pembanding).
- PointNet — fitur point cloud.
- Dense fusion per-pixel.
- Iterative refinement network.

## Metodologi & Arsitektur
CNN mengekstrak embedding warna per-piksel; PointNet-like mengekstrak geometri per-titik dari point cloud (depth); dense fusion menggabungkan keduanya per-titik; jaringan memprediksi pose per-titik + confidence, diagregasi; refinement network menyempurnakan pose iteratif.

Komponen / langkah metodologis utama:

- Ekstraksi embedding RGB per-piksel (CNN).
- Ekstraksi geometri per-titik (PointNet-like).
- Dense fusion per-pixel (warna+geometri).
- Prediksi pose per-titik + confidence.
- Iterative refinement network.
- Input RGB-D, real-time.

## Kontribusi Utama
1. Fusi RGB-D dense per-titik untuk pose.
2. Estimasi pose per-titik + agregasi confidence.
3. Refinement iteratif menggantikan ICP.
4. SOTA real-time saat rilis.

## Rincian Eksperimen
Diuji pada YCB-Video dan LineMOD dengan metrik ADD/ADD-S dan pengukuran kecepatan, dibandingkan PoseCNN(+ICP).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| YCB-Video | ADD-S | SOTA real-time saat rilis |
| LineMOD | ADD | SOTA/kompetitif |
| Kecepatan | FPS | real-time (tanpa ICP mahal) |

## Temuan Kunci
- Fusi dense per-titik unggul untuk pose 6D.
- Refinement iteratif menggantikan ICP.
- Confidence per-titik menangani oklusi.
- Real-time tercapai.

## Keunggulan
- Fusi dense per-titik.
- Real-time tanpa ICP.
- SOTA saat rilis.

## Keterbatasan
- Bergantung kualitas kedalaman/point cloud.
- Butuh model objek untuk evaluasi ADD.
- Oklusi berat tetap menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
DenseFusion menegaskan fusi RGB-D dense per-titik untuk pose 6D — contoh kuat pemanfaatan kedalaman geometris dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pose 6D** yang baik dibaca berdampingan:

- [073 - 2018 - PoseCNN - Pose 6D](./073%20-%202018%20-%20PoseCNN%20-%20Pose%206D.md)
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
DenseFusion menyatukan fitur RGB dan geometri point cloud secara per-piksel dengan refinement iteratif untuk pose 6D RGB-D, mencapai SOTA real-time tanpa ICP mahal.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wang2019densefusion` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 074/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
