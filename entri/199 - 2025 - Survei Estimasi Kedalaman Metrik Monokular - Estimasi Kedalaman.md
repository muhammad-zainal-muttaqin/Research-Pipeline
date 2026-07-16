# 199 - Survey on Monocular Metric Depth Estimation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 199 dari 202 |
| Kunci BibTeX | `zhang2025metricdepthsurvey` |
| Judul | Survey on Monocular Metric Depth Estimation |
| Penulis | Zhang, Jiuling |
| Tahun | 2025 |
| Venue / Jurnal | arXiv preprint arXiv:2501.11841 |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | survei, monocular metric depth, zero-shot, scale-agnostic, MMDE |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2501.11841
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Survey%20on%20Monocular%20Metric%20Depth%20Estimation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Survey%20on%20Monocular%20Metric%20Depth%20Estimation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2501.11841 |

## Ringkasan Eksekutif
Survei ini (Zhang, arXiv Januari 2025) mensintesis kemajuan Monocular Metric Depth Estimation (MMDE), menyoroti metode scale-agnostic untuk generalisasi zero-shot serta tantangan generalisasi model dan hilangnya detail pada batas scene.

## Abstrak (Parafrase)
Makalah adalah survei atas estimasi kedalaman metrik monokular (MMDE) - memprediksi depth berskala nyata dari satu citra. Ia menaksonomikan pendekatan supervised, self-supervised, dan foundation model (mis. Metric3D, ZoeDepth, Depth Anything, UniDepth), menekankan metode scale-agnostic untuk generalisasi zero-shot lintas kamera/domain. Survei membahas tantangan utama: generalisasi model, hilangnya detail pada batas scene, serta peran model difusi generatif (Marigold, GeoWizard) dalam memulihkan detail frekuensi-tinggi.

## Latar Belakang & Konteks
MMDE penting untuk robotika/AR karena memberi skala metrik, bukan sekadar depth relatif. Namun generalisasi lintas kamera dan pelestarian detail masih menantang, memicu banyak pendekatan yang perlu disintesis.

## Permasalahan yang Diangkat
- Depth relatif tak cukup untuk aplikasi berskala metrik.
- Generalisasi lintas kamera/domain (intrinsik berbeda) sulit.
- Detail pada batas scene sering hilang.
- Beragamnya metode menuntut taksonomi terpadu.

## Tujuan & Pertanyaan Penelitian
- Menaksonomikan metode MMDE secara sistematis.
- Menyoroti pendekatan scale-agnostic zero-shot.
- Merangkum tantangan generalisasi dan detail.
- Memetakan arah riset (foundation & difusi).

## Tinjauan Terdahulu / Posisi Literatur
Survei merangkum foundation model depth (Metric3D entri 177, ZoeDepth entri 176, Depth Anything V2 entri 175) dan difusi (Marigold entri 178), memberi peta menyeluruh MMDE.

Karya/konsep pembanding yang relevan:

- ZoeDepth - gabungan depth relatif+metrik (entri 176).
- Metric3D - depth metrik zero-shot (entri 177).
- Marigold - difusi untuk depth (entri 178).
- Depth Anything V2 - foundation depth (entri 175).

## Metodologi & Arsitektur
Sebagai survei, metodenya adalah tinjauan sistematis: mengklasifikasikan metode (supervised/self-supervised/foundation/difusi), membandingkan strategi penanganan skala kamera, dan mengidentifikasi celah riset.

Komponen / langkah metodologis utama:

- Taksonomi metode MMDE.
- Analisis strategi scale-agnostic (canonical camera, intrinsik).
- Perbandingan benchmark dan metrik (AbsRel, RMSE, delta<1.25).
- Identifikasi celah dan arah riset.

## Kontribusi Utama
1. Taksonomi terpadu MMDE.
2. Sintesis metode scale-agnostic zero-shot.
3. Ringkasan tantangan generalisasi & detail.
4. Peta arah riset (foundation & difusi generatif).

## Rincian Eksperimen
Bukan eksperimen baru; survei membandingkan hasil terlapor lintas benchmark depth (KITTI, NYUv2, dll.) dan metrik standar untuk memetakan lanskap.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KITTI/NYUv2 (dari literatur) | AbsRel, RMSE, delta<1.25 | Perbandingan lintas metode (rangkuman) |
| Zero-shot | Generalisasi | Fokus pada metode scale-agnostic |
| Arah riset | Celah | Detail batas & generalisasi kamera |

## Temuan Kunci
- Scale-agnostic adalah kunci generalisasi zero-shot MMDE.
- Foundation model mendorong lompatan generalisasi.
- Difusi generatif membantu detail frekuensi-tinggi.
- Detail batas dan intrinsik kamera tetap menantang.

## Keunggulan
- Peta menyeluruh dan mutakhir (2025) bidang MMDE.
- Taksonomi jelas untuk orientasi pembaca.
- Menautkan foundation & difusi.

## Keterbatasan
- Sebagai survei, tak menyumbang metode baru.
- Cakupan bergantung tanggal tinjau (revisi Agu 2025).
- Tak semua metode terbaru bisa tercakup.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Sangat relevan sebagai rujukan pengantar/sitasi payung untuk bab estimasi kedalaman (2025); memberi konteks bagi entri 175-179 dan 198-202.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [198 - 2025 - Depth Anything 3 Geometri dari Sembarang Pandangan - Estimasi Kedalaman](./198%20-%202025%20-%20Depth%20Anything%203%20Geometri%20dari%20Sembarang%20Pandangan%20-%20Estimasi%20Kedalaman.md)
- [200 - 2026 - AsyncMDE Kedalaman Monokular Real-Time Memori Spasial - Estimasi Kedalaman](./200%20-%202026%20-%20AsyncMDE%20Kedalaman%20Monokular%20Real-Time%20Memori%20Spasial%20-%20Estimasi%20Kedalaman.md)
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
Survei ini memberi kerangka mutakhir untuk memahami MMDE, menekankan scale-agnostic dan foundation model. Sebagai rujukan payung 2025, cocok dikutip untuk konteks; klaim spesifik metode individual tetap dicek ke sumber primernya.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhang2025metricdepthsurvey` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 199/202 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
