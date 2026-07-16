# 174 - Omnivore: A Single Model for Many Visual Modalities

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 174 dari 191 |
| Kunci BibTeX | `girdhar2022omnivore` |
| Judul | Omnivore: A Single Model for Many Visual Modalities |
| Penulis | Girdhar, Rohit; Singh, Mannat; Ravi, Nikhila; van der Maaten, Laurens; Joulin, Armand; Misra, Ishan |
| Tahun | 2022 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | multimodal, single model, images video RGB-D, modality-agnostic |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2201.08377
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Omnivore%3A%20A%20Single%20Model%20for%20Many%20Visual%20Modalities
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Omnivore%3A%20A%20Single%20Model%20for%20Many%20Visual%20Modalities&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2201.08377 |

## Ringkasan Eksekutif
Omnivore adalah satu model yang mengklasifikasikan citra, video, dan data RGB-D (single-view 3D) dengan bobot bersama, membuktikan satu Transformer dapat menangani banyak modalitas visual sekaligus.

## Abstrak (Parafrase)
Penulis melatih satu Vision Transformer untuk memproses gambar 2D, klip video, dan citra RGB-D dengan mengonversi tiap modalitas menjadi embedding patch spatio-temporal yang seragam. Tanpa arsitektur khusus per-modalitas, Omnivore mencapai kinerja kompetitif pada ImageNet, Kinetics, dan SUN RGB-D, serta menunjukkan transfer lintas-modal.

## Latar Belakang & Konteks
Model visi umumnya dilatih per-modalitas. Omnivore menguji apakah satu model dapat melayani banyak modalitas dan berbagi pengetahuan.

## Permasalahan yang Diangkat
- Model terpisah per-modalitas tidak efisien.
- Transfer lintas-modal sulit.
- Menyatukan format masukan beragam.

## Tujuan & Pertanyaan Penelitian
- Satu model untuk banyak modalitas visual.
- Berbagi representasi lintas-modal.
- Mendemonstrasikan transfer lintas-modal.

## Tinjauan Terdahulu / Posisi Literatur
Berdialog dengan ViT/Swin dan tren model generalis; berkaitan dengan segmentasi/klasifikasi RGB-D.

Karya/konsep pembanding yang relevan:

- ViT - Transformer citra.
- Swin - Transformer hierarkis.
- MultiMAE - pra-latih multimodal.
- Model generalis visual.

## Metodologi & Arsitektur
Tiap modalitas dipetakan ke patch embedding spatio-temporal seragam; satu Transformer memprosesnya dengan kepala klasifikasi per-dataset; dilatih bersama lintas modalitas.

Komponen / langkah metodologis utama:

- Embedding patch seragam lintas modalitas.
- Transformer tunggal berbagi bobot.
- Kepala klasifikasi per-dataset.
- Pelatihan gabungan multimodal.

## Kontribusi Utama
1. Model tunggal untuk citra/video/RGB-D.
2. Bukti transfer lintas-modal.
3. Kinerja kompetitif tiap modalitas.
4. Kesederhanaan arsitektur.

## Rincian Eksperimen
ImageNet-1K (citra), Kinetics-400 (video), SUN RGB-D (RGB-D) untuk akurasi klasifikasi, plus uji transfer lintas-modal.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| ImageNet | Top-1 | kompetitif |
| Kinetics-400 | akurasi | kompetitif |
| SUN RGB-D | akurasi | kuat sebagai model tunggal |

## Temuan Kunci
- Satu model bisa melayani banyak modalitas.
- Berbagi bobot memungkinkan transfer lintas-modal.
- Format masukan seragam kunci penyatuan.

## Keunggulan
- Generalis lintas-modal.
- Berbagi pengetahuan.
- Arsitektur sederhana.

## Keterbatasan
- Tugas klasifikasi (bukan dense) fokus utama.
- Butuh data besar.
- RGB-D terbatas single-view.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Menunjukkan penyatuan modalitas termasuk RGB-D dalam satu backbone, relevan untuk arsitektur persepsi multimodal terpadu.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [171 - 2021 - SegFormer - Segmentasi RGB-D](./171%20-%202021%20-%20SegFormer%20-%20Segmentasi%20RGB-D.md)
- [172 - 2022 - EMSANet - Segmentasi RGB-D](./172%20-%202022%20-%20EMSANet%20-%20Segmentasi%20RGB-D.md)
- [173 - 2024 - GeminiFusion - Segmentasi RGB-D](./173%20-%202024%20-%20GeminiFusion%20-%20Segmentasi%20RGB-D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Segmentasi RGB-D** dalam peta tinjauan (17 klaster, 191 entri total).
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
Omnivore membuktikan satu model dapat menangani beragam modalitas visual termasuk RGB-D, mendukung arah model generalis.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `girdhar2022omnivore` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 174/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
