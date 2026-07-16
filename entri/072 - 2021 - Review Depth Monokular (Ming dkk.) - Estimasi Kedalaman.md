# 072 - Deep Learning for Monocular Depth Estimation: A Review

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 072 dari 154 |
| Kunci BibTeX | `ming2021depthsurvey` |
| Judul | Deep Learning for Monocular Depth Estimation: A Review |
| Penulis | Ming, Yue; Meng, Xuyang; Fan, Chunxiao; Yu, Hui |
| Tahun | 2021 |
| Venue / Jurnal | Neurocomputing |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | survei, depth monokular, supervised, self-supervised, review |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-estimasi-kedalaman)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Deep%20Learning%20for%20Monocular%20Depth%20Estimation%3A%20A%20Review
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Deep%20Learning%20for%20Monocular%20Depth%20Estimation%3A%20A%20Review&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 438 |
| Halaman | 14--33 |

## Ringkasan Eksekutif
Tinjauan metode deep learning untuk estimasi kedalaman monokular yang memetakan pendekatan supervised/self-supervised, arsitektur, loss, dan dataset.

## Abstrak (Parafrase)
Makalah survei ini mengkaji perkembangan estimasi kedalaman monokular berbasis deep learning: taksonomi supervised, self-supervised, dan semi-supervised; ragam arsitektur (encoder-decoder, multi-skala); fungsi loss; serta dataset dan metrik (AbsRel, RMSE, akurasi ambang). Ia menyediakan peta bidang yang berguna untuk memilih pendekatan.

## Latar Belakang & Konteks
Bidang depth monokular berkembang pesat dengan banyak pendekatan dan tolok ukur, sehingga dibutuhkan sintesis terstruktur.

## Permasalahan yang Diangkat
- Bidang depth monokular berkembang pesat.
- Banyak pendekatan (supervised/self/semi).
- Ragam arsitektur & loss membingungkan.
- Dataset & metrik beragam.
- Perlu peta bidang yang koheren.

## Tujuan & Pertanyaan Penelitian
- Mengklasifikasikan metode depth monokular.
- Meninjau arsitektur, loss, dan dataset.
- Mendiskusikan tantangan dan arah.

## Tinjauan Terdahulu / Posisi Literatur
Survei ini mengagregasi metode depth monokular 2014-2020.

Karya/konsep pembanding yang relevan:

- Metode supervised (Eigen, BTS).
- Metode self-supervised (Monodepth2).
- Arsitektur & loss depth.
- Dataset (NYUv2, KITTI).

## Metodologi & Arsitektur
Metodologi survei: taksonomi supervised/self/semi, tinjauan arsitektur dan fungsi loss, ikhtisar dataset/metrik, dan diskusi tantangan (skala, generalisasi, objek dinamis).

Komponen / langkah metodologis utama:

- Taksonomi supervised/self/semi-supervised.
- Tinjauan arsitektur (encoder-decoder/multi-skala).
- Ikhtisar fungsi loss depth.
- Ikhtisar dataset & metrik (AbsRel/RMSE).
- Diskusi tantangan & arah.
- Sintesis literatur.

## Kontribusi Utama
1. Peta bidang depth monokular yang terstruktur.
2. Taksonomi pendekatan yang jelas.
3. Ikhtisar loss/dataset/metrik praktis.
4. Rujukan untuk memilih pendekatan.

## Rincian Eksperimen
Sebagai survei, evaluasi berupa kompilasi & analisis komparatif metode depth dari literatur, bukan eksperimen baru.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Metode depth | AbsRel/RMSE | kompilasi komparatif |
| Pendekatan | taksonomi | supervised/self/semi |
| Tantangan | peta | skala/generalisasi/dinamis |

## Temuan Kunci
- Ada spektrum supervised hingga self-supervised.
- Trade-off label vs generalisasi penting.
- Skala metrik & generalisasi tantangan utama.
- Dataset/metrik terstandar memudahkan perbandingan.

## Keunggulan
- Peta bidang terstruktur.
- Taksonomi jelas.
- Rujukan pemilihan pendekatan.

## Keterbatasan
- Bersifat survei.
- Cakupan hingga ~2020.
- Kurang metode terbaru (foundation).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Survei ini menaungi entri-entri depth dalam tinjauan dan membantu memahami trade-off pendekatan untuk menyediakan depth pada pipeline RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [062 - 2014 - Depth dari Citra Tunggal (Eigen dkk.) - Estimasi Kedalaman](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md)
- [063 - 2017 - Monodepth (Left-Right Consistency) - Estimasi Kedalaman](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md)
- [064 - 2019 - Monodepth2 - Estimasi Kedalaman](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md)
- [065 - 2019 - BTS (Local Planar Guidance) - Estimasi Kedalaman](./065%20-%202019%20-%20BTS%20%28Local%20Planar%20Guidance%29%20-%20Estimasi%20Kedalaman.md)
- [066 - 2021 - AdaBins - Estimasi Kedalaman](./066%20-%202021%20-%20AdaBins%20-%20Estimasi%20Kedalaman.md)
- [067 - 2021 - DPT (Dense Prediction Transformer) - Estimasi Kedalaman](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md)
- [068 - 2022 - MiDaS (Robust Monocular Depth) - Estimasi Kedalaman](./068%20-%202022%20-%20MiDaS%20%28Robust%20Monocular%20Depth%29%20-%20Estimasi%20Kedalaman.md)
- [069 - 2020 - PackNet - Estimasi Kedalaman](./069%20-%202020%20-%20PackNet%20-%20Estimasi%20Kedalaman.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Estimasi Kedalaman** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Estimasi Kedalaman)
Istilah penting untuk memahami makalah ini:

- **Depth monokular** — Estimasi kedalaman dari satu citra RGB (ill-posed).
- **Supervised** — Dilatih dengan ground-truth depth.
- **Self-supervised** — Dilatih tanpa label depth via konsistensi stereo/video.
- **Disparitas** — Pergeseran piksel antar-pandangan stereo.
- **Skala metrik vs relatif** — Depth satuan nyata vs hanya urutan relatif.
- **AbsRel** — Absolute Relative error (makin kecil makin baik).
- **RMSE** — Root Mean Square Error peta depth.
- **delta<1.25** — Persentase piksel dengan error di bawah ambang.
- **Zero-shot** — Generalisasi ke dataset tak dilihat saat pelatihan.
- **Pseudo-depth** — Depth prediksi model, pengganti sensor depth.

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
Ming dkk. meninjau metode deep learning untuk depth monokular dengan taksonomi supervised/self-supervised, ikhtisar arsitektur/loss/dataset, menjadi peta bidang yang berguna untuk memilih pendekatan.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ming2021depthsurvey` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 072/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
