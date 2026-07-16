# 198 - Depth Anything 3: Recovering the Visual Space from Any Views

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 198 dari 202 |
| Kunci BibTeX | `lin2025depthanything3` |
| Judul | Depth Anything 3: Recovering the Visual Space from Any Views |
| Penulis | Lin, Haotong; Chen, Sili; Liew, Junhao; Chen, Donny Y.; Li, Zhenyu; Shi, Guang; Feng, Jiashi; Kang, Bingyi |
| Tahun | 2025 |
| Venue / Jurnal | arXiv preprint arXiv:2511.10647 |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | Depth Anything 3, multi-view, geometry, DINOv2, novel view |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2511.10647
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Depth%20Anything%203%3A%20Recovering%20the%20Visual%20Space%20from%20Any%20Views
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Depth%20Anything%203%3A%20Recovering%20the%20Visual%20Space%20from%20Any%20Views&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2511.10647 |

## Ringkasan Eksekutif
Depth Anything 3 (Lin dkk., arXiv November 2025) memprediksi geometri yang konsisten secara spasial dari sejumlah pandangan sembarang (dengan atau tanpa pose kamera diketahui), memakai satu transformer polos dan target prediksi depth-ray tunggal, dan menetapkan SOTA baru melampaui VGGT.

## Abstrak (Parafrase)
Depth Anything 3 (DA3) memperluas paradigma Depth Anything dari depth monokular ke pemulihan ruang visual dari banyak pandangan. Cukup dengan satu transformer polos (mis. encoder DINOv2 vanilla) tanpa spesialisasi arsitektur, dan satu target prediksi depth-ray yang menghapus kebutuhan pembelajaran multi-tugas rumit. Mekanisme cross-view self-attention adaptif-masukan menata ulang token untuk pertukaran informasi antar-pandangan yang efisien. DA3 melakukan depth monokular, depth multi-view, depth berkondisi-pose, estimasi pose kamera, dan estimasi 3D Gaussian untuk sintesis pandangan baru - menetapkan SOTA di semua tugas, melampaui VGGT rata-rata 44.3% pada akurasi pose kamera dan 25.1% pada akurasi geometri.

## Latar Belakang & Konteks
Depth Anything V1/V2 unggul pada depth monokular. Namun aplikasi robotika/AR menuntut geometri konsisten lintas banyak pandangan. DA3 menyatukan estimasi geometri multi-view dalam satu model sederhana.

## Permasalahan yang Diangkat
- Depth monokular tidak menjamin konsistensi geometri lintas pandangan.
- Pipeline multi-view klasik butuh arsitektur/multi-tugas rumit.
- Pose kamera kadang tak diketahui.
- Pertukaran informasi antar-pandangan mahal.

## Tujuan & Pertanyaan Penelitian
- Memulihkan geometri konsisten dari sembarang jumlah pandangan.
- Menyederhanakan arsitektur menjadi transformer polos.
- Menyatukan depth, pose, dan 3D Gaussian dalam satu model.
- Menghadirkan cross-view attention yang efisien.

## Tinjauan Terdahulu / Posisi Literatur
DA3 melanjutkan Depth Anything V2 (entri 175) dan menandingi VGGT/DUSt3R pada geometri multi-view, tetapi dengan backbone polos dan target depth-ray tunggal.

Karya/konsep pembanding yang relevan:

- Depth Anything V2 - depth monokular SOTA (entri 175).
- VGGT - geometri multi-view (baseline yang dilampaui).
- DUSt3R/MASt3R - rekonstruksi 3D dari pasangan citra.
- DINOv2 - encoder self-supervised sebagai backbone.

## Metodologi & Arsitektur
Satu transformer polos berbasis DINOv2 memproses banyak pandangan; cross-view self-attention adaptif-masukan menata ulang token antar-view; target prediksi tunggal (depth-ray) menyatukan tugas tanpa cabang multi-tugas terpisah; keluaran mendukung depth, pose, dan 3D Gaussian.

Komponen / langkah metodologis utama:

- Backbone transformer polos (DINOv2 vanilla).
- Input-adaptive cross-view self-attention.
- Target prediksi depth-ray tunggal (bukan multi-tugas).
- Keluaran depth/pose/3D Gaussian untuk sintesis pandangan.

## Kontribusi Utama
1. Model tunggal geometri multi-view dari sembarang pandangan.
2. Penyederhanaan ke transformer polos + target depth-ray.
3. SOTA melampaui VGGT (+44.3% pose, +25.1% geometri).
4. Dukungan sintesis pandangan baru via 3D Gaussian.

## Rincian Eksperimen
Dievaluasi lintas tugas: depth monokular/multi-view, estimasi pose kamera, dan geometri; dibandingkan dengan VGGT dan metode multi-view terkini.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Pose kamera | Akurasi | +44.3% rata-rata vs VGGT |
| Geometri | Akurasi | +25.1% rata-rata vs VGGT |
| Multi-tugas | Depth/pose/3DGS | SOTA lintas tugas (lihat naskah) |

## Temuan Kunci
- Transformer polos cukup untuk geometri multi-view.
- Target depth-ray tunggal menyederhanakan pelatihan.
- Cross-view attention adaptif efisien dan akurat.
- Satu model melayani depth, pose, dan sintesis pandangan.

## Keunggulan
- SOTA geometri multi-view dengan arsitektur sederhana.
- Fleksibel: dengan/tanpa pose diketahui.
- Menyatukan banyak tugas 3D.

## Keterbatasan
- Kebutuhan komputasi multi-view besar.
- Angka perlu dikonfirmasi via naskah.
- Ketergantungan pada backbone DINOv2 skala besar.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Rujukan mutakhir estimasi kedalaman/geometri (2025), lanjutan langsung Depth Anything V2 (entri 175); relevan untuk RGB-D dan rekonstruksi 3D dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [199 - 2025 - Survei Estimasi Kedalaman Metrik Monokular - Estimasi Kedalaman](./199%20-%202025%20-%20Survei%20Estimasi%20Kedalaman%20Metrik%20Monokular%20-%20Estimasi%20Kedalaman.md)
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
Depth Anything 3 menyatukan geometri multi-view dalam satu transformer polos dengan target depth-ray tunggal, melampaui VGGT. Sebagai karya 2025, angka perlu diverifikasi via arXiv sebelum sitasi formal.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `lin2025depthanything3` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 198/202 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
