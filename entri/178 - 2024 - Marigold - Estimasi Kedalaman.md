# 178 - Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 178 dari 191 |
| Kunci BibTeX | `ke2024marigold` |
| Judul | Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation |
| Penulis | Ke, Bingxin; Obukhov, Anton; Huang, Shengyu; Metzger, Nando; Daudt, Rodrigo Caye; Schindler, Konrad |
| Tahun | 2024 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | monocular depth, diffusion, generative prior, affine-invariant |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2312.02145
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Repurposing%20Diffusion-Based%20Image%20Generators%20for%20Monocular%20Depth%20Estimation
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Repurposing%20Diffusion-Based%20Image%20Generators%20for%20Monocular%20Depth%20Estimation&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2312.02145 |

## Ringkasan Eksekutif
Marigold menata ulang generator citra difusi (Stable Diffusion) menjadi estimator kedalaman monokular yang, walau di-fine-tune hanya pada data sintetis, menghasilkan depth affine-invariant yang sangat detail dan general.

## Abstrak (Parafrase)
Penulis memanfaatkan prior visual kaya dari model difusi laten pra-latih. Dengan protokol fine-tuning ringan pada dataset sintetis (Hypersim/Virtual KITTI), U-Net difusi diubah menjadi prediktor depth yang dijalankan sebagai proses denoising terkondisi citra. Marigold menghasilkan detail depth mengesankan dan generalisasi zero-shot yang kuat ke citra nyata meski tak melihat data nyata saat pelatihan.

## Latar Belakang & Konteks
Model difusi menyimpan prior scene yang kaya; memanfaatkannya untuk depth menjanjikan detail dan generalisasi tanpa data nyata masif.

## Permasalahan yang Diangkat
- Depth diskriminatif butuh data nyata besar.
- Detail halus sulit direproduksi.
- Generalisasi zero-shot terbatas.

## Tujuan & Pertanyaan Penelitian
- Mengubah difusi jadi estimator depth.
- Fine-tune hemat pada data sintetis.
- Mencapai depth detail dan general.

## Tinjauan Terdahulu / Posisi Literatur
Berbeda dari pendekatan diskriminatif (MiDaS/DPT/Depth Anything) dengan memanfaatkan prior generatif difusi.

Karya/konsep pembanding yang relevan:

- Stable Diffusion - model difusi laten.
- MiDaS/DPT - depth diskriminatif.
- Depth Anything - data tak berlabel besar.
- Metode depth generatif lain.

## Metodologi & Arsitektur
Encoder VAE memetakan citra ke laten; U-Net difusi dikondisikan pada laten citra untuk mendenoise laten depth; fine-tune pada pasangan citra-depth sintetis; inferensi multi-langkah dengan agregasi (ensembling).

Komponen / langkah metodologis utama:

- Backbone U-Net difusi laten pra-latih.
- Kondisi pada laten citra.
- Fine-tune pada data sintetis saja.
- Inferensi denoising + ensembling.

## Kontribusi Utama
1. Estimator depth berbasis difusi.
2. Detail dan generalisasi tinggi hanya dari data sintetis.
3. Protokol fine-tuning efisien.
4. Zero-shot kuat ke citra nyata.

## Rincian Eksperimen
Zero-shot pada NYU, KITTI, ETH3D, ScanNet, DIODE untuk depth affine-invariant (AbsRel/delta).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Zero-shot (NYU/KITTI) | AbsRel/delta | SOTA/kompetitif lintas-dataset |
| Detail | kualitatif | struktur halus sangat baik |
| Data latih | - | hanya sintetis |

## Temuan Kunci
- Prior difusi menghasilkan depth detail dan general.
- Data sintetis cukup berkat prior kuat.
- Ensembling menstabilkan hasil.

## Keunggulan
- Detail tinggi.
- Generalisasi zero-shot.
- Hemat data nyata.

## Keterbatasan
- Inferensi multi-langkah lebih lambat.
- Depth affine-invariant (bukan metrik).
- Bergantung kualitas model difusi dasar.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Menyediakan depth detail dari satu citra, berguna untuk rekonstruksi/lokalisasi 3D pada pipeline berbasis kamera RGB.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [175 - 2024 - Depth Anything V2 - Estimasi Kedalaman](./175%20-%202024%20-%20Depth%20Anything%20V2%20-%20Estimasi%20Kedalaman.md)
- [176 - 2023 - ZoeDepth - Estimasi Kedalaman](./176%20-%202023%20-%20ZoeDepth%20-%20Estimasi%20Kedalaman.md)
- [177 - 2023 - Metric3D - Estimasi Kedalaman](./177%20-%202023%20-%20Metric3D%20-%20Estimasi%20Kedalaman.md)
- [179 - 2022 - NeWCRFs - Estimasi Kedalaman](./179%20-%202022%20-%20NeWCRFs%20-%20Estimasi%20Kedalaman.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Estimasi Kedalaman** dalam peta tinjauan (17 klaster, 191 entri total).
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
Marigold menunjukkan prior generatif difusi dapat menjadi estimator depth monokular yang detail dan general, arah baru estimasi kedalaman.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ke2024marigold` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 178/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
