# 200 - AsyncMDE: Real-Time Monocular Depth Estimation via Asynchronous Spatial Memory

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 200 dari 202 |
| Kunci BibTeX | `ma2026asyncmde` |
| Judul | AsyncMDE: Real-Time Monocular Depth Estimation via Asynchronous Spatial Memory |
| Penulis | Ma, Lianjie; Li, Yuquan; Jiang, Bingzheng; Zhong, Ziming; Ding, Han; Zhu, Lijun |
| Tahun | 2026 |
| Venue / Jurnal | arXiv preprint arXiv:2603.10438 |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | AsyncMDE, real-time depth, asynchronous, spatial memory, video |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2603.10438
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=AsyncMDE%3A%20Real-Time%20Monocular%20Depth%20Estimation%20via%20Asynchronous%20Spatial%20Memory
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=AsyncMDE%3A%20Real-Time%20Monocular%20Depth%20Estimation%20via%20Asynchronous%20Spatial%20Memory&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2603.10438 |

## Ringkasan Eksekutif
AsyncMDE (Ma dkk., arXiv Maret 2026, revisi Juni 2026) mengusulkan estimasi kedalaman monokular real-time via memori spasial asinkron, menargetkan depth video yang konsisten temporal dengan latensi rendah untuk robotika.

## Abstrak (Parafrase)
AsyncMDE menghadirkan estimasi kedalaman monokular real-time yang memanfaatkan memori spasial asinkron untuk menjaga konsistensi temporal antar-frame tanpa memproses ulang seluruh konteks di tiap langkah. Dengan memperbarui memori secara asinkron, model memangkas komputasi berulang dan mempertahankan latensi rendah, cocok untuk aplikasi robotika dan navigasi yang menuntut depth streaming stabil.

## Latar Belakang & Konteks
Depth monokular per-frame rentan kedip temporal (flicker); metode video konsisten sering mahal. Memori spasial yang diperbarui asinkron dapat menyeimbangkan konsistensi dan kecepatan.

## Permasalahan yang Diangkat
- Depth per-frame tak konsisten temporal (flicker).
- Metode video konsisten mahal untuk real-time.
- Pemrosesan ulang konteks penuh boros komputasi.
- Robotika menuntut depth streaming latensi rendah.

## Tujuan & Pertanyaan Penelitian
- Menjaga konsistensi temporal depth video.
- Menekan komputasi via memori asinkron.
- Mempertahankan latensi real-time.
- Menyediakan depth streaming stabil untuk robotika.

## Tinjauan Terdahulu / Posisi Literatur
AsyncMDE berdiri di atas depth video konsisten dan foundation depth (Depth Anything), tetapi menambah mekanisme memori spasial asinkron untuk efisiensi.

Karya/konsep pembanding yang relevan:

- Depth Anything V2 - foundation depth (entri 175).
- NVDS/consistent video depth - konsistensi temporal.
- ZoeDepth - depth metrik (entri 176).
- Streaming/online depth - inferensi bertahap.

## Metodologi & Arsitektur
Fitur spasial disimpan dalam memori yang diperbarui secara asinkron; frame baru meng-query memori untuk konteks temporal tanpa rekomputasi penuh, menghasilkan depth konsisten dengan biaya rendah.

Komponen / langkah metodologis utama:

- Memori spasial (spatial memory) antar-frame.
- Pembaruan memori asinkron (asynchronous update).
- Query konteks temporal tanpa rekomputasi penuh.
- Desain sadar-latensi untuk real-time.

## Kontribusi Utama
1. Mekanisme memori spasial asinkron untuk depth video.
2. Konsistensi temporal pada latensi real-time.
3. Pengurangan komputasi berulang.
4. Kesesuaian untuk robotika/navigasi streaming.

## Rincian Eksperimen
Dievaluasi pada benchmark depth video/streaming untuk konsistensi temporal, akurasi (AbsRel/RMSE), dan latensi/FPS; detail pada naskah.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Depth video | Konsistensi temporal | Membaik vs per-frame (lihat naskah) |
| Akurasi | AbsRel/RMSE | Kompetitif; konfirmasi angka |
| Latensi | FPS | Real-time via memori asinkron |

## Temuan Kunci
- Memori asinkron menyeimbangkan konsistensi dan kecepatan.
- Konteks temporal mengurangi flicker depth.
- Rekomputasi penuh tidak diperlukan untuk konsistensi.

## Keunggulan
- Depth video real-time dan konsisten.
- Efisien secara komputasi.
- Cocok untuk robotika streaming.

## Keterbatasan
- Karya 2026 sangat baru; validasi independen minim.
- Angka perlu dikonfirmasi via naskah.
- Ketahanan pada gerak cepat/oklusi perlu diperiksa.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Relevan untuk estimasi kedalaman real-time pada pipeline RGB-D/robotika; melengkapi entri depth (175-179, 198-202) dengan sudut temporal/streaming (2026).

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [198 - 2025 - Depth Anything 3 Geometri dari Sembarang Pandangan - Estimasi Kedalaman](./198%20-%202025%20-%20Depth%20Anything%203%20Geometri%20dari%20Sembarang%20Pandangan%20-%20Estimasi%20Kedalaman.md)
- [199 - 2025 - Survei Estimasi Kedalaman Metrik Monokular - Estimasi Kedalaman](./199%20-%202025%20-%20Survei%20Estimasi%20Kedalaman%20Metrik%20Monokular%20-%20Estimasi%20Kedalaman.md)
- [201 - 2026 - UniDAC Kedalaman Metrik Universal untuk Sembarang Kamera - Estimasi Kedalaman](./201%20-%202026%20-%20UniDAC%20Kedalaman%20Metrik%20Universal%20untuk%20Sembarang%20Kamera%20-%20Estimasi%20Kedalaman.md)
- [202 - 2026 - Focusable Monocular Depth Estimation - Estimasi Kedalaman](./202%20-%202026%20-%20Focusable%20Monocular%20Depth%20Estimation%20-%20Estimasi%20Kedalaman.md)

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
AsyncMDE menawarkan depth monokular real-time yang konsisten temporal lewat memori spasial asinkron. Sebagai karya 2026, verifikasi metrik dan protokol via arXiv sebelum sitasi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ma2026asyncmde` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 200/202 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
