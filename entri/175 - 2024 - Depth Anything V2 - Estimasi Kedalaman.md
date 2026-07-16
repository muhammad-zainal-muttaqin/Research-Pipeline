# 175 - Depth Anything V2

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 175 dari 191 |
| Kunci BibTeX | `yang2024depthanythingv2` |
| Judul | Depth Anything V2 |
| Penulis | Yang, Lihe; Kang, Bingyi; Huang, Zilong; Zhao, Zhen; Xu, Xiaogang; Feng, Jiashi; Zhao, Hengshuang |
| Tahun | 2024 |
| Venue / Jurnal | Advances in Neural Information Processing Systems (NeurIPS) |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | monocular depth, foundation model, synthetic data, zero-shot |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2406.09414
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Depth%20Anything%20V2
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Depth%20Anything%20V2&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2406.09414 |

## Ringkasan Eksekutif
Depth Anything V2 menyempurnakan model fondasi estimasi kedalaman monokular dengan melatih pada data sintetis berlabel presisi lalu mendistilasi ke data nyata skala besar, menghasilkan depth relatif yang tajam, robust, dan efisien.

## Abstrak (Parafrase)
Penulis berargumen label depth nyata sering kasar/berderau. Mereka melatih model guru pada citra sintetis berlabel akurat, menghasilkan pseudo-label untuk jutaan citra nyata tak berlabel, lalu melatih model siswa pada pseudo-label tersebut. Hasilnya prediksi depth relatif lebih detail dan robust dari V1, dengan varian ringan hingga besar dan kemampuan zero-shot yang kuat.

## Latar Belakang & Konteks
Depth Anything (V1) menunjukkan kekuatan data tak berlabel skala besar; V2 memperbaiki ketajaman dan robustnes lewat strategi data sintetis + distilasi.

## Permasalahan yang Diangkat
- Label depth nyata kasar/berderau.
- Detail halus (tepi tipis) sulit.
- Robustnes lintas-domain.

## Tujuan & Pertanyaan Penelitian
- Meningkatkan ketajaman/robustnes depth monokular.
- Memanfaatkan data sintetis presisi + distilasi.
- Menyediakan model efisien berskala.

## Tinjauan Terdahulu / Posisi Literatur
Melanjutkan MiDaS/DPT dan Depth Anything V1; menekankan pipeline data guru-siswa.

Karya/konsep pembanding yang relevan:

- MiDaS - depth relatif lintas-dataset.
- DPT - Transformer prediksi dense.
- Depth Anything V1 - data tak berlabel skala besar.
- Marigold - depth berbasis difusi.

## Metodologi & Arsitektur
Latih guru pada data sintetis akurat; hasilkan pseudo-label untuk citra nyata tak berlabel; latih siswa pada pseudo-label; gunakan backbone DINOv2 dan varian ukuran berbeda.

Komponen / langkah metodologis utama:

- Guru pada citra sintetis berlabel presisi.
- Pseudo-label jutaan citra nyata.
- Distilasi guru ke siswa.
- Varian S/B/L efisien.

## Kontribusi Utama
1. Pipeline sintetis + distilasi untuk depth fondasi.
2. Depth lebih tajam/robust dari V1.
3. Model efisien berskala.
4. Zero-shot kuat.

## Rincian Eksperimen
Benchmark zero-shot depth relatif lintas-dataset, uji ketajaman tepi dan kecepatan; varian metrik via fine-tuning.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Zero-shot relatif | AbsRel/rank | unggul atas V1/MiDaS |
| Ketajaman tepi | kualitatif | detail halus lebih baik |
| Kecepatan | FPS | varian ringan real-time |

## Temuan Kunci
- Data sintetis presisi + distilasi mengalahkan label nyata kasar.
- Skala data tak berlabel tetap krusial.
- Robustnes lintas-domain meningkat.

## Keunggulan
- Tajam dan robust.
- Efisien berskala.
- Zero-shot kuat.

## Keterbatasan
- Depth relatif (metrik perlu fine-tune).
- Bergantung kualitas guru sintetis.
- Domain sangat berbeda tetap menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Sumber pseudo-depth berkualitas untuk pipeline RGB-D tanpa sensor, mendukung deteksi/lokalisasi 3D berbasis kamera.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [176 - 2023 - ZoeDepth - Estimasi Kedalaman](./176%20-%202023%20-%20ZoeDepth%20-%20Estimasi%20Kedalaman.md)
- [177 - 2023 - Metric3D - Estimasi Kedalaman](./177%20-%202023%20-%20Metric3D%20-%20Estimasi%20Kedalaman.md)
- [178 - 2024 - Marigold - Estimasi Kedalaman](./178%20-%202024%20-%20Marigold%20-%20Estimasi%20Kedalaman.md)
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
Depth Anything V2 memperkuat model fondasi depth monokular via data sintetis dan distilasi, memberi depth tajam dan robust untuk berbagai aplikasi.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `yang2024depthanythingv2` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 175/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
