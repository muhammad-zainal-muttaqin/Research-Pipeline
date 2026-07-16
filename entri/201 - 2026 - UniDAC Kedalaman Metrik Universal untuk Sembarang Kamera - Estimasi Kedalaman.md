# 201 - UniDAC: Universal Metric Depth Estimation for Any Camera

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 201 dari 202 |
| Kunci BibTeX | `ganesan2026unidac` |
| Judul | UniDAC: Universal Metric Depth Estimation for Any Camera |
| Penulis | Ganesan, Girish Chandar; Guo, Yuliang; Ren, Liu; Liu, Xiaoming |
| Tahun | 2026 |
| Venue / Jurnal | arXiv preprint arXiv:2603.27105 |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | UniDAC, universal depth, any camera, metric depth, intrinsics |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2603.27105
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=UniDAC%3A%20Universal%20Metric%20Depth%20Estimation%20for%20Any%20Camera
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=UniDAC%3A%20Universal%20Metric%20Depth%20Estimation%20for%20Any%20Camera&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2603.27105 |

## Ringkasan Eksekutif
UniDAC (Ganesan dkk., arXiv Maret 2026) mengusulkan estimasi kedalaman metrik universal yang bekerja untuk sembarang kamera, menargetkan generalisasi lintas intrinsik/FOV tanpa penyetelan per-kamera.

## Abstrak (Parafrase)
UniDAC (Universal Metric Depth Estimation for Any Camera) berfokus pada estimasi depth berskala metrik yang tidak bergantung pada model kamera tertentu. Dengan mengondisikan prediksi pada parameter intrinsik/geometri kamera, model menggeneralisasi lintas beragam FOV dan sensor tanpa kalibrasi per-kamera, mengatasi kegagalan umum metode metrik ketika intrinsik berubah. Pendekatan ini menyasar depth metrik zero-shot yang andal di berbagai perangkat.

## Latar Belakang & Konteks
Depth metrik sangat sensitif terhadap intrinsik kamera; model yang dilatih pada satu FOV kerap gagal di kamera lain. Estimasi universal lintas-kamera penting untuk penerapan luas.

## Permasalahan yang Diangkat
- Depth metrik gagal lintas intrinsik/FOV kamera berbeda.
- Kalibrasi per-kamera mahal dan tak selalu tersedia.
- Ambiguitas skala saat model kamera berubah.
- Generalisasi zero-shot lintas sensor sulit.

## Tujuan & Pertanyaan Penelitian
- Menghasilkan depth metrik universal lintas kamera.
- Mengondisikan prediksi pada intrinsik/geometri.
- Menggeneralisasi zero-shot tanpa kalibrasi per-kamera.
- Andal lintas FOV dan sensor.

## Tinjauan Terdahulu / Posisi Literatur
UniDAC melanjutkan Metric3D/UniDepth dan Depth Anything dengan penekanan eksplisit pada universalitas kamera (any camera) dan pengondisian intrinsik.

Karya/konsep pembanding yang relevan:

- Metric3D(v2) - depth metrik zero-shot via canonical camera (entri 177).
- ZoeDepth - depth metrik lintas domain (entri 176).
- UniDepth - depth metrik universal (pembanding).
- Depth Anything V2/3 - foundation depth (entri 175, 198).

## Metodologi & Arsitektur
Model mengondisikan estimasi depth pada representasi kamera (intrinsik/FOV), mentransformasi ke ruang kanonik agar konsisten lintas perangkat, lalu memulihkan skala metrik untuk kamera target.

Komponen / langkah metodologis utama:

- Pengondisian pada parameter intrinsik/geometri kamera.
- Transformasi ke ruang kamera kanonik.
- Pemulihan skala metrik untuk kamera target.
- Pelatihan lintas beragam sensor/FOV.

## Kontribusi Utama
1. Kerangka depth metrik universal lintas kamera.
2. Pengondisian intrinsik untuk generalisasi.
3. Depth metrik zero-shot tanpa kalibrasi per-kamera.
4. Evaluasi lintas beragam FOV/sensor.

## Rincian Eksperimen
Dievaluasi lintas dataset dengan kamera/intrinsik beragam (mis. KITTI, NYUv2, dan set zero-shot), memakai AbsRel/RMSE/delta<1.25 untuk menilai generalisasi metrik.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Zero-shot lintas kamera | AbsRel/delta<1.25 | Generalisasi membaik vs baseline (lihat naskah) |
| KITTI/NYUv2 | RMSE | Kompetitif; konfirmasi angka |
| FOV bervariasi | Konsistensi skala | Lebih stabil lintas intrinsik |

## Temuan Kunci
- Pengondisian intrinsik kunci generalisasi metrik lintas kamera.
- Ruang kanonik menstabilkan skala.
- Depth metrik universal layak tanpa kalibrasi per-kamera.

## Keunggulan
- Generalisasi lintas kamera/FOV.
- Depth metrik zero-shot.
- Tanpa kalibrasi per-kamera.

## Keterbatasan
- Karya 2026 sangat baru; validasi independen minim.
- Bergantung akurasi intrinsik yang tersedia.
- Angka perlu dikonfirmasi via naskah.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Relevan untuk depth metrik pada pipeline RGB-D lintas perangkat; melengkapi Metric3D (177) dan Depth Anything 3 (198) dalam bab kedalaman (2026).

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [198 - 2025 - Depth Anything 3 Geometri dari Sembarang Pandangan - Estimasi Kedalaman](./198%20-%202025%20-%20Depth%20Anything%203%20Geometri%20dari%20Sembarang%20Pandangan%20-%20Estimasi%20Kedalaman.md)
- [199 - 2025 - Survei Estimasi Kedalaman Metrik Monokular - Estimasi Kedalaman](./199%20-%202025%20-%20Survei%20Estimasi%20Kedalaman%20Metrik%20Monokular%20-%20Estimasi%20Kedalaman.md)
- [200 - 2026 - AsyncMDE Kedalaman Monokular Real-Time Memori Spasial - Estimasi Kedalaman](./200%20-%202026%20-%20AsyncMDE%20Kedalaman%20Monokular%20Real-Time%20Memori%20Spasial%20-%20Estimasi%20Kedalaman.md)
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
UniDAC menargetkan depth metrik universal lintas sembarang kamera melalui pengondisian intrinsik dan ruang kanonik. Sebagai karya 2026, verifikasi metrik/protokol via arXiv sebelum sitasi formal.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ganesan2026unidac` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 201/202 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
