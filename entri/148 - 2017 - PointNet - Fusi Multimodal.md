# 148 - PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 148 dari 154 |
| Kunci BibTeX | `qi2017pointnet` |
| Judul | PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation |
| Penulis | Qi, Charles R.; Su, Hao; Mo, Kaichun; Guibas, Leonidas J. |
| Tahun | 2017 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Fusi Multimodal |
| Kata kunci | backbone 3D, point cloud, permutation invariant, klasifikasi/segmentasi, 3D |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-fusi-multimodal)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=PointNet%3A%20Deep%20Learning%20on%20Point%20Sets%20for%203D%20Classification%20and%20Segmentation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=PointNet%3A%20Deep%20Learning%20on%20Point%20Sets%20for%203D%20Classification%20and%20Segmentation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 652--660 |

## Ringkasan Eksekutif
Jaringan pelopor yang memproses point cloud mentah langsung dengan MLP per-titik dan symmetric pooling untuk invariansi permutasi, mendasari deep learning point cloud.

## Abstrak (Parafrase)
PointNet (Qi dkk.) memproses himpunan titik 3D mentah secara langsung: MLP diterapkan per-titik lalu max-pooling simetris mengagregasi fitur global, menjamin invariansi terhadap permutasi titik. T-Net menambah invariansi terhadap transformasi. PointNet mencapai SOTA klasifikasi/segmentasi 3D saat rilis dan menjadi fondasi banyak metode point cloud.

## Latar Belakang & Konteks
Point cloud tidak terstruktur dan tidak berurutan (permutasi bebas), sehingga CNN grid dan metode berurutan tidak langsung berlaku.

## Permasalahan yang Diangkat
- Point cloud tak terstruktur & tak berurutan.
- CNN grid tak langsung berlaku pada titik.
- Invariansi permutasi diperlukan.
- Voxelisasi kehilangan detail/mahal.
- Deep learning langsung pada titik belum ada.

## Tujuan & Pertanyaan Penelitian
- Memproses point cloud mentah langsung.
- Menjamin invariansi permutasi (symmetric pooling).
- Menyediakan fondasi deep learning 3D.

## Tinjauan Terdahulu / Posisi Literatur
PointNet pelopor deep learning langsung pada point set.

Karya/konsep pembanding yang relevan:

- Voxelisasi/multi-view — pendekatan sebelumnya.
- MLP per-titik — ekstraksi fitur.
- Symmetric function (max-pool) — invariansi.
- T-Net — invariansi transformasi.

## Metodologi & Arsitektur
MLP bersama diterapkan pada tiap titik untuk mengekstrak fitur; max-pooling simetris mengagregasi menjadi fitur global (invarian permutasi); T-Net memprediksi transformasi untuk menyelaraskan input/fitur; fitur global dipakai klasifikasi, fitur per-titik + global untuk segmentasi.

Komponen / langkah metodologis utama:

- MLP per-titik (fitur lokal).
- Max-pooling simetris (fitur global).
- Invariansi permutasi.
- T-Net untuk invariansi transformasi.
- Klasifikasi & segmentasi 3D.
- Pemrosesan point cloud mentah.

## Kontribusi Utama
1. Deep learning langsung pada point cloud mentah.
2. Invariansi permutasi via symmetric pooling.
3. SOTA klasifikasi/segmentasi 3D saat rilis.
4. Fondasi banyak metode point cloud.

## Rincian Eksperimen
Diuji pada ModelNet (klasifikasi) dan ShapeNet (segmentasi bagian) dengan metrik akurasi/mIoU, plus analisis robustness.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| ModelNet | akurasi | SOTA klasifikasi 3D saat rilis |
| ShapeNet | mIoU | SOTA segmentasi bagian |
| Robustness | perturbasi | tahan hilang/derau titik |

## Temuan Kunci
- Point cloud mentah dapat diproses langsung.
- Symmetric pooling menjamin invariansi permutasi.
- T-Net membantu invariansi transformasi.
- Fondasi deep learning 3D.

## Keunggulan
- Fondasi point cloud.
- Invariansi permutasi.
- Serbaguna 3D.

## Keterbatasan
- Tidak menangkap struktur lokal (PointNet++ memperbaiki).
- Fitur global tunggal terbatas.
- Bukan spesifik deteksi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
PointNet mendasari banyak metode pose 6D (DenseFusion/PVN3D) dan deteksi 3D (VoxelNet/Frustum) dalam tinjauan; fundamental untuk memproses geometri kedalaman.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Fusi Multimodal** yang baik dibaca berdampingan:

- [147 - 2016 - ResNet - Fusi Multimodal](./147%20-%202016%20-%20ResNet%20-%20Fusi%20Multimodal.md)
- [149 - 2018 - CBAM - Fusi Multimodal](./149%20-%202018%20-%20CBAM%20-%20Fusi%20Multimodal.md)
- [150 - 2021 - Survei Deteksi & Segmentasi Multimodal (Feng dkk.) - Fusi Multimodal](./150%20-%202021%20-%20Survei%20Deteksi%20%26%20Segmentasi%20Multimodal%20%28Feng%20dkk.%29%20-%20Fusi%20Multimodal.md)
- [151 - 2023 - Object Detection in 20 Years (Zou dkk.) - Fusi Multimodal](./151%20-%202023%20-%20Object%20Detection%20in%2020%20Years%20%28Zou%20dkk.%29%20-%20Fusi%20Multimodal.md)
- [152 - 2017 - Deep Multimodal Learning A Survey (Ramachandram & Taylor) - Fusi Multimodal](./152%20-%202017%20-%20Deep%20Multimodal%20Learning%20A%20Survey%20%28Ramachandram%20%26%20Taylor%29%20-%20Fusi%20Multimodal.md)
- [153 - 2021 - Survei RGB-D SOD (Zhou dkk.) - Fusi Multimodal](./153%20-%202021%20-%20Survei%20RGB-D%20SOD%20%28Zhou%20dkk.%29%20-%20Fusi%20Multimodal.md)
- [154 - 2022 - Survei Dataset RGB-D (Lopes dkk.) - Fusi Multimodal](./154%20-%202022%20-%20Survei%20Dataset%20RGB-D%20%28Lopes%20dkk.%29%20-%20Fusi%20Multimodal.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Fusi Multimodal** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Fusi Multimodal)
Istilah penting untuk memahami makalah ini:

- **Multimodal** — Menggabungkan >1 modalitas data.
- **Backbone** — Jaringan ekstraksi fitur fundamental.
- **Residual/skip** — Jalan pintas memudahkan pelatihan jaringan dalam.
- **Attention (CBAM/SE)** — Modul penimbang fitur kanal-spasial.
- **PointNet** — Jaringan pemroses point cloud mentah.
- **Early/late/deep fusion** — Tingkat penggabungan modalitas.
- **Survei** — Sintesis literatur lintas metode.
- **Generalisasi lintas-sensor** — Ketahanan terhadap kombinasi sensor.
- **Kalibrasi/penyelarasan** — Penyelarasan spasial-temporal antar-modal.
- **Representasi bersama** — Ruang fitur gabungan lintas-modal.

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
PointNet memproses point cloud mentah dengan MLP per-titik dan symmetric pooling untuk invariansi permutasi, menjadi fondasi deep learning 3D yang mendasari banyak metode pose dan deteksi 3D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `qi2017pointnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 148/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
