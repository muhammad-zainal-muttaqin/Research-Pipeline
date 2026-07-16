# 176 - ZoeDepth: Zero-Shot Transfer by Combining Relative and Metric Depth

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 176 dari 191 |
| Kunci BibTeX | `bhat2023zoedepth` |
| Judul | ZoeDepth: Zero-Shot Transfer by Combining Relative and Metric Depth |
| Penulis | Bhat, Shariq Farooq; Birkl, Reiner; Wofk, Diana; Wonka, Peter; M{\"u |
| Tahun | 2023 |
| Venue / Jurnal | arXiv preprint arXiv:2302.12288 |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | metric depth, zero-shot, relative-to-metric, monocular |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2302.12288
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=ZoeDepth%3A%20Zero-Shot%20Transfer%20by%20Combining%20Relative%20and%20Metric%20Depth
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=ZoeDepth%3A%20Zero-Shot%20Transfer%20by%20Combining%20Relative%20and%20Metric%20Depth&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2302.12288 |

## Ringkasan Eksekutif
ZoeDepth menjembatani depth relatif dan metrik: model dilatih untuk depth relatif zero-shot lintas-dataset lalu ditambah kepala metrik-bins per-domain, sehingga menghasilkan depth berskala metrik yang tetap general.

## Abstrak (Parafrase)
Penulis menggabungkan pra-pelatihan depth relatif pada banyak dataset (untuk generalisasi) dengan kepala metric bins (turunan AdaBins/LocalBins) yang diaktifkan per-domain via router ringan. Hasilnya satu model dapat menghasilkan depth metrik pada domain indoor/outdoor sekaligus mempertahankan kemampuan zero-shot, mengungguli baseline metrik pada beberapa benchmark.

## Latar Belakang & Konteks
Depth relatif general tapi tak berskala metrik; depth metrik akurat tapi domain-spesifik. ZoeDepth menyatukan keduanya.

## Permasalahan yang Diangkat
- Depth relatif tak punya skala metrik.
- Model metrik tak general lintas-domain.
- Butuh satu model serbaguna.

## Tujuan & Pertanyaan Penelitian
- Menghasilkan depth metrik yang tetap general.
- Menggabungkan pra-latih relatif dan kepala metrik.
- Menangani multi-domain via router.

## Tinjauan Terdahulu / Posisi Literatur
Berpijak pada MiDaS (relatif) dan AdaBins/LocalBins (metric bins); menekankan penggabungan keduanya.

Karya/konsep pembanding yang relevan:

- MiDaS - depth relatif lintas-dataset.
- AdaBins - metric bins adaptif.
- LocalBins - bins lokal.
- DPT - backbone prediksi dense.

## Metodologi & Arsitektur
Backbone terlatih relatif (MiDaS/DPT) di-fine-tune dengan kepala metric bins; router ringan memilih kepala domain (indoor/outdoor); dekoder menghasilkan depth metrik.

Komponen / langkah metodologis utama:

- Pra-latih depth relatif multi-dataset.
- Kepala metric bins per-domain.
- Router pemilih domain ringan.
- Fine-tune metrik indoor+outdoor.

## Kontribusi Utama
1. Kerangka relative-to-metric terpadu.
2. Depth metrik zero-shot yang general.
3. Router multi-domain.
4. Peningkatan pada benchmark metrik.

## Rincian Eksperimen
NYU Depth v2 (indoor) dan KITTI (outdoor) untuk metrik (AbsRel/RMSE/delta), plus uji zero-shot lintas-dataset.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYU v2 | AbsRel/delta | SOTA/kompetitif metrik indoor |
| KITTI | RMSE | kuat outdoor |
| Zero-shot | rank | generalisasi terjaga |

## Temuan Kunci
- Pra-latih relatif meningkatkan generalisasi metrik.
- Router memungkinkan multi-domain.
- Satu model melayani indoor+outdoor.

## Keunggulan
- Depth metrik + general.
- Multi-domain.
- Memanfaatkan pra-latih kuat.

## Keterbatasan
- Router menambah kompleksitas.
- Skala metrik bergantung kalibrasi domain.
- Domain baru mungkin butuh fine-tune.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Depth metrik dari satu kamera sangat berguna untuk lokalisasi 3D pada pipeline RGB-D tanpa sensor depth khusus.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [175 - 2024 - Depth Anything V2 - Estimasi Kedalaman](./175%20-%202024%20-%20Depth%20Anything%20V2%20-%20Estimasi%20Kedalaman.md)
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
ZoeDepth menyatukan keunggulan depth relatif dan metrik, menyediakan estimasi kedalaman metrik yang general lintas-domain.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `bhat2023zoedepth` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 176/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
