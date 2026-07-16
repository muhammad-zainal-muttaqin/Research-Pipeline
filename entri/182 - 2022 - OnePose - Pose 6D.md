# 182 - OnePose: One-Shot Object Pose Estimation without CAD Models

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 182 dari 191 |
| Kunci BibTeX | `sun2022onepose` |
| Judul | OnePose: One-Shot Object Pose Estimation without CAD Models |
| Penulis | Sun, Jiaming; Wang, Zihao; Zhang, Siyu; He, Xingyi; Zhao, Hongcheng; Zhang, Guofeng; Zhou, Xiaowei |
| Tahun | 2022 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Pose 6D |
| Kata kunci | 6D pose, CAD-free, one-shot, feature matching |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=OnePose%3A%20One-Shot%20Object%20Pose%20Estimation%20without%20CAD%20Models
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=OnePose%3A%20One-Shot%20Object%20Pose%20Estimation%20without%20CAD%20Models&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
OnePose mengestimasi pose 6D objek tanpa model CAD dan tanpa pelatihan per-objek: dari sekumpulan citra referensi, ia membangun model titik dengan struktur-dari-gerak lalu mencocokkan fitur untuk pose objek baru secara one-shot.

## Abstrak (Parafrase)
Terinspirasi visual localization, OnePose merekonstruksi point cloud jarang objek dari video/citra referensi via SfM, membangun deskriptor 2D-3D, lalu untuk citra kueri mencocokkan fitur 2D-3D dan menyelesaikan pose via PnP. Tanpa CAD dan tanpa pelatihan ulang per-objek, OnePose menangani objek sehari-hari dan diperkuat penerusnya (OnePose++) untuk objek bertekstur rendah.

## Latar Belakang & Konteks
Metode pose umumnya butuh CAD dan pelatihan per-objek, membatasi skalabilitas ke objek arbitrer di dunia nyata.

## Permasalahan yang Diangkat
- Ketergantungan pada model CAD.
- Pelatihan per-objek mahal.
- Skala ke objek baru terbatas.

## Tujuan & Pertanyaan Penelitian
- Estimasi pose tanpa CAD.
- One-shot untuk objek baru.
- Memanfaatkan pencocokan fitur 2D-3D.

## Tinjauan Terdahulu / Posisi Literatur
Menjembatani pose estimation dan visual localization (structure-based); berbeda dari GDR-Net/ZebraPose yang butuh CAD.

Karya/konsep pembanding yang relevan:

- Visual localization berbasis SfM.
- GDR-Net - pose berbasis CAD.
- SuperGlue - pencocokan fitur.
- OnePose++ - penerus tekstur-rendah.

## Metodologi & Arsitektur
Bangun model titik jarang objek via SfM dari citra referensi; agregasi deskriptor 2D-3D; untuk kueri, cocokkan fitur 2D-3D (graph attention) dan selesaikan pose via PnP+RANSAC.

Komponen / langkah metodologis utama:

- Rekonstruksi SfM objek dari referensi.
- Deskriptor 2D-3D teragregasi.
- Pencocokan fitur 2D-3D (attention).
- PnP+RANSAC untuk pose one-shot.

## Kontribusi Utama
1. Estimasi pose 6D bebas-CAD.
2. One-shot untuk objek baru.
3. Dataset OnePose.
4. Kerangka berbasis pencocokan fitur.

## Rincian Eksperimen
Dataset OnePose (objek sehari-hari) dengan metrik cm-degree accuracy; pembandingan terhadap metode berbasis CAD.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| OnePose dataset | cm-degree acc | akurat tanpa CAD |
| Objek baru | one-shot | tanpa retraining |
| Tekstur rendah | - | ditingkatkan oleh OnePose++ |

## Temuan Kunci
- Pose akurat mungkin tanpa CAD.
- SfM + matching cukup untuk objek baru.
- Tekstur rendah adalah tantangan utama.

## Keunggulan
- Bebas-CAD.
- Skalabel ke objek baru.
- One-shot.

## Keterbatasan
- Butuh citra referensi + SfM.
- Objek tekstur-rendah sulit (v1).
- Bergantung kualitas pencocokan fitur.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Pose tanpa CAD sangat praktis untuk robot yang menghadapi objek arbitrer, melengkapi grasp/manipulasi berbasis RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pose 6D** yang baik dibaca berdampingan:

- [180 - 2021 - GDR-Net - Pose 6D](./180%20-%202021%20-%20GDR-Net%20-%20Pose%206D.md)
- [181 - 2022 - ZebraPose - Pose 6D](./181%20-%202022%20-%20ZebraPose%20-%20Pose%206D.md)

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
OnePose memungkinkan estimasi pose 6D bebas-CAD dan one-shot melalui pencocokan fitur 2D-3D, memperluas skalabilitas ke objek dunia nyata.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `sun2022onepose` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 182/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
