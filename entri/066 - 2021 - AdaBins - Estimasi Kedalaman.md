# 066 - AdaBins: Depth Estimation Using Adaptive Bins

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 066 dari 154 |
| Kunci BibTeX | `bhat2021adabins` |
| Judul | AdaBins: Depth Estimation Using Adaptive Bins |
| Penulis | Bhat, Shariq Farooq; Alhashim, Ibraheem; Wonka, Peter |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | depth monokular, adaptive bins, Transformer, diskretisasi, NYUv2/KITTI |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=AdaBins%3A%20Depth%20Estimation%20Using%20Adaptive%20Bins
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=AdaBins%3A%20Depth%20Estimation%20Using%20Adaptive%20Bins&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 4009--4018 |

## Ringkasan Eksekutif
Metode depth monokular yang memprediksi kedalaman sebagai kombinasi linear bin adaptif per-citra yang diputuskan modul Transformer, bukan regresi kontinu langsung.

## Abstrak (Parafrase)
AdaBins mengubah estimasi kedalaman menjadi klasifikasi-regresi hibrida: modul mini-ViT memutuskan pusat bin kedalaman yang adaptif per-citra, lalu kedalaman tiap piksel diprediksi sebagai kombinasi linear (softmax) dari pusat bin tersebut. Adaptasi bin ke distribusi kedalaman spesifik citra meningkatkan akurasi, mencapai SOTA saat rilis.

## Latar Belakang & Konteks
Regresi kedalaman kontinu global mengabaikan bahwa distribusi kedalaman berbeda antar-citra (mis. ruangan sempit vs koridor panjang), sehingga suboptimal.

## Permasalahan yang Diangkat
- Regresi kontinu global mengabaikan distribusi per-citra.
- Distribusi kedalaman berbeda antar-adegan.
- Diskretisasi tetap (bin seragam) suboptimal.
- Konteks global kurang dimanfaatkan.
- Akurasi depth perlu ditingkatkan.

## Tujuan & Pertanyaan Penelitian
- Menentukan bin kedalaman adaptif per-citra.
- Memprediksi kedalaman sebagai kombinasi bin.
- Memanfaatkan konteks global (Transformer).

## Tinjauan Terdahulu / Posisi Literatur
AdaBins menggabungkan diskretisasi adaptif dan Transformer untuk depth.

Karya/konsep pembanding yang relevan:

- Depth supervised (encoder-decoder) — dasar.
- Ordinal regression/diskretisasi depth.
- Mini-ViT — modul global.
- Dataset NYUv2/KITTI.

## Metodologi & Arsitektur
Encoder-decoder menghasilkan fitur; modul AdaBins (mini-ViT) memproses fitur global untuk menghasilkan pusat bin adaptif per-citra; tiap piksel diprediksi sebagai kombinasi linear (bobot softmax) dari pusat bin; loss depth + bin-center regularization.

Komponen / langkah metodologis utama:

- Encoder-decoder depth.
- Modul AdaBins berbasis mini-ViT (global).
- Adaptive bin centers per-citra.
- Prediksi = kombinasi linear pusat bin.
- Pelatihan supervised.
- Evaluasi NYUv2 & KITTI.

## Kontribusi Utama
1. Diskretisasi depth adaptif per-citra.
2. Modul Transformer untuk konteks global.
3. Prediksi sebagai kombinasi bin (hibrida).
4. SOTA saat rilis.

## Rincian Eksperimen
Diuji pada NYUv2 dan KITTI dengan metrik depth standar, dibandingkan BTS dan metode supervised lain, plus ablation adaptive bins.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | AbsRel/RMSE | SOTA saat rilis |
| KITTI | AbsRel/RMSE | SOTA/kompetitif |
| Ablation | adaptive bins | adaptasi per-citra menyumbang gain |

## Temuan Kunci
- Adaptasi bin per-citra meningkatkan akurasi.
- Konteks global (Transformer) bermanfaat.
- Hibrida klasifikasi-regresi efektif.
- Distribusi kedalaman spesifik citra penting.

## Keunggulan
- Diskretisasi adaptif efektif.
- Konteks global via Transformer.
- SOTA saat rilis.

## Keterbatasan
- Butuh ground-truth depth.
- Modul global menambah komputasi.
- Jumlah bin perlu penyetelan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
AdaBins memperkaya klaster Estimasi Kedalaman dengan ide diskretisasi adaptif + Transformer; relevan bagi kualitas pseudo-depth untuk RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [062 - 2014 - Depth dari Citra Tunggal (Eigen dkk.) - Estimasi Kedalaman](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md)
- [063 - 2017 - Monodepth (Left-Right Consistency) - Estimasi Kedalaman](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md)
- [064 - 2019 - Monodepth2 - Estimasi Kedalaman](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md)
- [065 - 2019 - BTS (Local Planar Guidance) - Estimasi Kedalaman](./065%20-%202019%20-%20BTS%20%28Local%20Planar%20Guidance%29%20-%20Estimasi%20Kedalaman.md)
- [067 - 2021 - DPT (Dense Prediction Transformer) - Estimasi Kedalaman](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md)
- [068 - 2022 - MiDaS (Robust Monocular Depth) - Estimasi Kedalaman](./068%20-%202022%20-%20MiDaS%20%28Robust%20Monocular%20Depth%29%20-%20Estimasi%20Kedalaman.md)
- [069 - 2020 - PackNet - Estimasi Kedalaman](./069%20-%202020%20-%20PackNet%20-%20Estimasi%20Kedalaman.md)
- [070 - 2021 - MonoIndoor - Estimasi Kedalaman](./070%20-%202021%20-%20MonoIndoor%20-%20Estimasi%20Kedalaman.md)

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
AdaBins memprediksi kedalaman sebagai kombinasi bin adaptif per-citra yang diputuskan modul Transformer, memanfaatkan distribusi kedalaman spesifik citra untuk akurasi SOTA.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `bhat2021adabins` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 066/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
