# 105 - Uncertainty-Guided Cross-Modal Learning for Robust Multispectral Pedestrian Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 105 dari 154 |
| Kunci BibTeX | `kim2022cmpd` |
| Judul | Uncertainty-Guided Cross-Modal Learning for Robust Multispectral Pedestrian Detection |
| Penulis | Kim, Jung Uk; Park, Sungjune; Ro, Yong Man |
| Tahun | 2022 |
| Venue / Jurnal | IEEE Transactions on Circuits and Systems for Video Technology |
| Tema klaster | Pedestrian RGB-T |
| Kata kunci | RGB-T, ketidakpastian, cross-modal learning, robust, pejalan |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-pedestrian-rgb-t)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Uncertainty-Guided%20Cross-Modal%20Learning%20for%20Robust%20Multispectral%20Pedestrian%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Uncertainty-Guided%20Cross-Modal%20Learning%20for%20Robust%20Multispectral%20Pedestrian%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 32 |
| Nomor | 3 |
| Halaman | 1510--1523 |

## Ringkasan Eksekutif
Metode deteksi pejalan multispektral yang memakai pembelajaran lintas-modal terpandu ketidakpastian untuk robustness, memodelkan keandalan prediksi antar-modal.

## Abstrak (Parafrase)
CMPD memakai uncertainty-aware cross-modal learning: memodelkan ketidakpastian prediksi tiap modal dan mentransfer pengetahuan antar-modal berdasarkan keandalan, sehingga modal yang tak andal (mis. thermal siang) ditekan. Ini meningkatkan robustness deteksi pejalan lintas kondisi pada KAIST dan CVC-14.

## Latar Belakang & Konteks
Modalitas dapat menjadi tidak andal tergantung kondisi (thermal siang, RGB malam), sehingga fusi harus sadar ketidakpastian untuk menghindari propagasi kesalahan.

## Permasalahan yang Diangkat
- Modalitas bisa tak andal tergantung kondisi.
- Fusi tanpa sadar-ketidakpastian rawan salah.
- Transfer pengetahuan antar-modal perlu selektif.
- Robustness lintas kondisi diperlukan.
- Keandalan prediksi belum dimodelkan.

## Tujuan & Pertanyaan Penelitian
- Memodelkan ketidakpastian prediksi tiap modal.
- Mentransfer pengetahuan antar-modal selektif.
- Meningkatkan robustness lintas kondisi.

## Tinjauan Terdahulu / Posisi Literatur
CMPD menyempurnakan fusi RGB-T dengan pemodelan ketidakpastian.

Karya/konsep pembanding yang relevan:

- KAIST/CVC-14 — dataset RGB-T.
- Uncertainty modeling.
- Cross-modal learning/distillation.
- Robust detection.

## Metodologi & Arsitektur
Jaringan memodelkan ketidakpastian prediksi per-modal; uncertainty-aware cross-modal learning mentransfer/menekan informasi antar-modal berdasarkan keandalan; deteksi pejalan yang robust dihasilkan dari fusi sadar-ketidakpastian.

Komponen / langkah metodologis utama:

- Uncertainty-aware cross-modal learning.
- Pemodelan ketidakpastian per-modal.
- Transfer/distilasi antar-modal selektif.
- Penekanan modal tak andal.
- Deteksi pejalan robust.
- Evaluasi KAIST & CVC-14.

## Kontribusi Utama
1. Pembelajaran lintas-modal sadar-ketidakpastian.
2. Menekan modal tak andal per kondisi.
3. Robust lintas kondisi cahaya.
4. Menurunkan miss rate.

## Rincian Eksperimen
Diuji pada KAIST dan CVC-14 dengan metrik miss rate lintas kondisi (siang/malam), dibandingkan metode fusi lain.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KAIST | miss rate | penurunan, robust lintas kondisi |
| CVC-14 | miss rate | kompetitif/unggul |
| Ablation | uncertainty | pemodelan ketidakpastian menyumbang gain |

## Temuan Kunci
- Pemodelan ketidakpastian memperkuat fusi.
- Transfer selektif mencegah propagasi kesalahan.
- Robustness lintas kondisi meningkat.
- Keandalan modal bergantung kondisi.

## Keunggulan
- Sadar-ketidakpastian.
- Robust lintas kondisi.
- Transfer selektif.

## Keterbatasan
- Pemodelan ketidakpastian menambah kompleksitas.
- Bergantung kualitas kedua modal.
- Fokus domain pejalan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
CMPD memperkuat tema keandalan modal via ketidakpastian — analog langsung dengan menimbang keandalan kedalaman pada fusi RGB+Depth dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pedestrian RGB-T** yang baik dibaca berdampingan:

- [100 - 2015 - KAIST Multispectral Pedestrian - Pedestrian RGB-T](./100%20-%202015%20-%20KAIST%20Multispectral%20Pedestrian%20-%20Pedestrian%20RGB-T.md)
- [101 - 2019 - IAF R-CNN (Illumination-Aware) - Pedestrian RGB-T](./101%20-%202019%20-%20IAF%20R-CNN%20%28Illumination-Aware%29%20-%20Pedestrian%20RGB-T.md)
- [102 - 2020 - MBNet - Pedestrian RGB-T](./102%20-%202020%20-%20MBNet%20-%20Pedestrian%20RGB-T.md)
- [103 - 2021 - GAFF - Pedestrian RGB-T](./103%20-%202021%20-%20GAFF%20-%20Pedestrian%20RGB-T.md)
- [104 - 2020 - Cyclic Fuse-and-Refine (CFR) - Pedestrian RGB-T](./104%20-%202020%20-%20Cyclic%20Fuse-and-Refine%20%28CFR%29%20-%20Pedestrian%20RGB-T.md)
- [106 - 2021 - RGB-D Fusion for Detection (Farahnakian & Heikkonen) - Pedestrian RGB-T](./106%20-%202021%20-%20RGB-D%20Fusion%20for%20Detection%20%28Farahnakian%20%26%20Heikkonen%29%20-%20Pedestrian%20RGB-T.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Pedestrian RGB-T** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Pedestrian RGB-T)
Istilah penting untuk memahami makalah ini:

- **Multispektral** — Citra beberapa pita (RGB + thermal).
- **RGB-T** — Pasangan citra warna dan termal.
- **Thermal/LWIR** — Inframerah panjang; andal saat gelap.
- **Illumination-aware** — Bobot modal menyesuaikan kondisi cahaya.
- **Modality imbalance** — Ketimpangan keandalan antar-modal.
- **Miss rate (MR)** — Metrik deteksi pejalan (makin kecil makin baik).
- **KAIST** — Dataset pejalan multispektral standar.
- **CVC-14** — Dataset pejalan siang-malam RGB-thermal.
- **Feature alignment** — Penyelarasan spasial fitur antar-modal.
- **Cross-modal attention** — Attention pemandu fusi RGB-thermal.

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
CMPD memakai pembelajaran lintas-modal terpandu ketidakpastian untuk menekan modal tak andal dan meningkatkan robustness deteksi pejalan multispektral lintas kondisi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `kim2022cmpd` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 105/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
