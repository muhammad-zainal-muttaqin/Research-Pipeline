# 202 - Focusable Monocular Depth Estimation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 202 dari 202 |
| Kunci BibTeX | `du2026focusabledepth` |
| Judul | Focusable Monocular Depth Estimation |
| Penulis | Du, Yuxin; others |
| Tahun | 2026 |
| Venue / Jurnal | arXiv preprint arXiv:2605.11756 |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | focusable, monocular depth, region prior, boundary, foreground |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2605.11756
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Focusable%20Monocular%20Depth%20Estimation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Focusable%20Monocular%20Depth%20Estimation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2605.11756 |

## Ringkasan Eksekutif
Focusable Monocular Depth Estimation (Du dkk., arXiv Mei 2026) memperkenalkan kerangka yang, diberi wilayah target, memprioritaskan akurasi depth latar-depan, menjaga transisi batas tajam, dan mempertahankan geometri global yang koheren.

## Abstrak (Parafrase)
Focusable Monocular Depth Estimation mengusulkan model yang dapat 'difokuskan' pada wilayah target: ketika diberi region of interest, model memprioritaskan akurasi kedalaman objek latar-depan, mempertahankan transisi batas yang tajam, sekaligus menjaga koherensi geometri scene secara global. Pendekatan ini mengatasi kelemahan depth monokular yang memperlakukan seluruh piksel seragam, sehingga detail objek penting sering kabur di batas.

## Latar Belakang & Konteks
Depth monokular umum memperlakukan semua wilayah sama, sehingga objek fokus (mis. yang akan digenggam robot) bisa kehilangan ketajaman batas. Kemampuan memfokuskan estimasi pada wilayah target berguna untuk manipulasi dan AR.

## Permasalahan yang Diangkat
- Depth seragam mengaburkan batas objek fokus.
- Akurasi latar-depan penting untuk manipulasi/grasp.
- Menjaga koherensi global sambil fokus lokal sulit.
- Kebutuhan kontrol wilayah pada estimasi depth.

## Tujuan & Pertanyaan Penelitian
- Memprioritaskan akurasi depth wilayah target.
- Mempertahankan transisi batas yang tajam.
- Menjaga geometri global tetap koheren.
- Memberi kontrol 'fokus' pada estimasi depth.

## Tinjauan Terdahulu / Posisi Literatur
Karya ini melanjutkan foundation depth (Depth Anything, Marigold) dengan menambah mekanisme fokus wilayah, berbeda dari estimasi seragam pada literatur sebelumnya.

Karya/konsep pembanding yang relevan:

- Depth Anything V2 - depth monokular seragam (entri 175).
- Marigold - difusi depth berdetail (entri 178).
- NeWCRFs - perbaikan struktur depth (entri 179).
- Depth Anything 3 - geometri multi-view (entri 198).

## Metodologi & Arsitektur
Diberi prior wilayah/region target, model menimbang objektif agar galat depth latar-depan diminimalkan dan batas dipertajam, sambil regularisasi menjaga konsistensi geometri global.

Komponen / langkah metodologis utama:

- Pengondisian pada wilayah target (focus prior).
- Objektif prioritas latar-depan.
- Penajaman transisi batas.
- Regularisasi koherensi geometri global.

## Kontribusi Utama
1. Konsep depth monokular yang dapat difokuskan.
2. Prioritas akurasi latar-depan + batas tajam.
3. Keseimbangan fokus lokal dan koherensi global.
4. Kegunaan untuk manipulasi/AR berbasis wilayah.

## Rincian Eksperimen
Dievaluasi pada benchmark depth dengan penekanan pada akurasi wilayah/latar-depan dan ketajaman batas, di samping metrik global (AbsRel/RMSE); detail pada naskah.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Wilayah fokus | Akurasi latar-depan | Membaik vs estimasi seragam (lihat naskah) |
| Batas objek | Ketajaman | Transisi lebih tajam |
| Global | AbsRel/RMSE | Koherensi geometri terjaga |

## Temuan Kunci
- Memfokuskan estimasi menaikkan akurasi wilayah target.
- Batas objek dapat dipertajam tanpa merusak global.
- Kontrol wilayah berguna untuk aplikasi manipulasi/AR.

## Keunggulan
- Depth wilayah-fokus dengan batas tajam.
- Koherensi global tetap terjaga.
- Relevan untuk grasp/manipulasi.

## Keterbatasan
- Karya 2026 sangat baru; validasi independen minim.
- Perlu definisi wilayah target saat inferensi.
- Angka perlu dikonfirmasi via naskah.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Relevan untuk depth pada manipulasi robotik RGB-D (fokus objek yang akan digenggam); melengkapi bab kedalaman (175-179, 198-202) dengan sudut fokus-wilayah (2026).

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [198 - 2025 - Depth Anything 3 Geometri dari Sembarang Pandangan - Estimasi Kedalaman](./198%20-%202025%20-%20Depth%20Anything%203%20Geometri%20dari%20Sembarang%20Pandangan%20-%20Estimasi%20Kedalaman.md)
- [199 - 2025 - Survei Estimasi Kedalaman Metrik Monokular - Estimasi Kedalaman](./199%20-%202025%20-%20Survei%20Estimasi%20Kedalaman%20Metrik%20Monokular%20-%20Estimasi%20Kedalaman.md)
- [200 - 2026 - AsyncMDE Kedalaman Monokular Real-Time Memori Spasial - Estimasi Kedalaman](./200%20-%202026%20-%20AsyncMDE%20Kedalaman%20Monokular%20Real-Time%20Memori%20Spasial%20-%20Estimasi%20Kedalaman.md)
- [201 - 2026 - UniDAC Kedalaman Metrik Universal untuk Sembarang Kamera - Estimasi Kedalaman](./201%20-%202026%20-%20UniDAC%20Kedalaman%20Metrik%20Universal%20untuk%20Sembarang%20Kamera%20-%20Estimasi%20Kedalaman.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Estimasi Kedalaman** dalam peta tinjauan (17 klaster, 202 entri total).
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
Focusable Monocular Depth Estimation menambahkan kontrol fokus wilayah pada depth monokular, menajamkan batas objek target tanpa mengorbankan geometri global. Sebagai karya 2026, verifikasi metrik/protokol via arXiv sebelum sitasi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `du2026focusabledepth` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 202/202 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
