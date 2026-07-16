# 197 - DiffPixelFormer: Differential Pixel-Aware Transformer for RGB-D Indoor Scene Segmentation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 197 dari 202 |
| Kunci BibTeX | `gong2025diffpixelformer` |
| Judul | DiffPixelFormer: Differential Pixel-Aware Transformer for RGB-D Indoor Scene Segmentation |
| Penulis | Gong, Yan; Lu, Jianli; Gao, Yongsheng; Zhao, Jie; Zhang, Xiaojuan; Rahardja, Susanto |
| Tahun | 2025 |
| Venue / Jurnal | arXiv preprint arXiv:2511.13047 |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | DiffPixelFormer, RGB-D segmentation, transformer, indoor, NYUv2 |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-segmentasi-rgb-d)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2511.13047
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=DiffPixelFormer%3A%20Differential%20Pixel-Aware%20Transformer%20for%20RGB-D%20Indoor%20Scene%20Segmentation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=DiffPixelFormer%3A%20Differential%20Pixel-Aware%20Transformer%20for%20RGB-D%20Indoor%20Scene%20Segmentation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2511.13047 |

## Ringkasan Eksekutif
DiffPixelFormer (Gong dkk., arXiv November 2025) adalah transformer sadar-piksel diferensial untuk segmentasi scene indoor RGB-D, mengeksploitasi perbedaan antar-modal pada level piksel untuk fusi yang lebih tajam.

## Abstrak (Parafrase)
DiffPixelFormer mengusulkan modul differential pixel-aware untuk segmentasi semantik scene indoor RGB-D. Alih-alih menggabungkan RGB dan depth secara seragam, model memodelkan perbedaan (diferensial) antar-modal per piksel guna menonjolkan tepi objek dan struktur geometri, lalu memadukannya dalam kerangka transformer. Pendekatan ini menyasar peningkatan mIoU pada benchmark indoor seperti NYUv2/SUN RGB-D.

## Latar Belakang & Konteks
Segmentasi RGB-D indoor mengandalkan geometri depth untuk memisahkan objek berpenampilan mirip. Namun fusi seragam mengaburkan kontribusi khas tiap modal; pemodelan perbedaan piksel dapat mempertajam batas dan struktur.

## Permasalahan yang Diangkat
- Fusi RGB-D seragam mengabaikan komplementaritas per-piksel.
- Batas objek dan struktur geometri kerap kabur.
- Depth berderau menyulitkan fusi yang stabil.
- Kebutuhan representasi transformer yang sadar-perbedaan modal.

## Tujuan & Pertanyaan Penelitian
- Memodelkan perbedaan antar-modal per piksel.
- Mempertajam batas dan struktur pada segmentasi.
- Menaikkan mIoU pada benchmark indoor.
- Mengintegrasikan diferensial ke dalam transformer.

## Tinjauan Terdahulu / Posisi Literatur
DiffPixelFormer melanjutkan garis transformer RGB-D (SegFormer, Omnivore, GeminiFusion) dengan penekanan pada isyarat diferensial per-piksel alih-alih fusi additif/konkatenasi.

Karya/konsep pembanding yang relevan:

- SegFormer - transformer segmentasi efisien (entri 171).
- GeminiFusion - fusi pixel-wise multimodal (entri 173).
- EMSANet - analisis scene RGB-D multi-tugas (entri 172).
- AsymFormer/Sigma - fusi RGB-X terbaru.

## Metodologi & Arsitektur
Cabang RGB dan depth diproses lalu modul differential pixel-aware menghitung dan menimbang perbedaan antar-modal per piksel; hasilnya diintegrasikan dalam encoder-decoder transformer untuk prediksi label per-piksel.

Komponen / langkah metodologis utama:

- Modul Differential Pixel-Aware antar-modal.
- Encoder-decoder berbasis transformer.
- Penajaman batas via isyarat diferensial.
- Fusi RGB-D per-piksel yang adaptif.

## Kontribusi Utama
1. Konsep differential pixel-aware untuk fusi RGB-D.
2. Transformer segmentasi indoor yang lebih tajam di batas.
3. Peningkatan mIoU pada benchmark indoor.
4. Analisis kontribusi diferensial antar-modal.

## Rincian Eksperimen
Dievaluasi pada NYUv2 dan/atau SUN RGB-D dengan metrik mIoU dan pixel accuracy, dibandingkan metode fusi RGB-D transformer terkini.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | mIoU | Kompetitif/unggul; lihat naskah |
| SUN RGB-D | mIoU | Kompetitif; konfirmasi angka via naskah |
| Ablation | Diferensial | Modul diferensial menaikkan akurasi batas |

## Temuan Kunci
- Isyarat perbedaan per-piksel mempertajam segmentasi.
- Fusi diferensial mengalahkan konkatenasi seragam.
- Transformer cocok mengintegrasikan isyarat diferensial.

## Keunggulan
- Batas objek lebih tajam.
- Fusi RGB-D adaptif per-piksel.
- Kompetitif pada benchmark indoor.

## Keterbatasan
- Karya akhir 2025; validasi independen terbatas.
- Angka perlu dikonfirmasi via naskah.
- Biaya komputasi transformer perlu ditelaah untuk real-time.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Melengkapi klaster segmentasi RGB-D (entri 51-61, 171-174) dengan pendekatan diferensial terbaru (2025); relevan bagi fusi RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- (tidak ada entri lain pada tema ini)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Segmentasi RGB-D** dalam peta tinjauan (17 klaster, 202 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Segmentasi RGB-D)
Istilah penting untuk memahami makalah ini:

- **Segmentasi semantik** — Pelabelan kelas per-piksel.
- **Scene parsing** — Pemahaman menyeluruh isi scene via segmentasi.
- **Encoder-decoder** — Arsitektur mengecilkan lalu memulihkan resolusi.
- **Fusi RGB-D** — Penggabungan cabang warna dan kedalaman.
- **mIoU** — mean Intersection-over-Union; metrik segmentasi utama.
- **Gating** — Gerbang penyaring/penimbang fitur sebelum digabung.
- **Cross-modal** — Antar-modalitas (RGB dan depth/thermal/LiDAR).
- **NYUv2** — Dataset RGB-D indoor standar.
- **SUN RGB-D** — Dataset RGB-D indoor berskala.
- **Pixel accuracy** — Persentase piksel terlabel benar.

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
DiffPixelFormer menunjukkan pemodelan perbedaan antar-modal per-piksel mempertajam segmentasi scene RGB-D indoor. Sebagai karya 2025, verifikasi mIoU dan pengaturan via arXiv sebelum dikutip.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `gong2025diffpixelformer` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 197/202 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
