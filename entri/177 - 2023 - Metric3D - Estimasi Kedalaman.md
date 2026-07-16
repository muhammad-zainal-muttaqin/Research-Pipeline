# 177 - Metric3D: Towards Zero-Shot Metric 3D Prediction from a Single Image

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 177 dari 191 |
| Kunci BibTeX | `yin2023metric3d` |
| Judul | Metric3D: Towards Zero-Shot Metric 3D Prediction from a Single Image |
| Penulis | Yin, Wei; Zhang, Chi; Chen, Hao; Cai, Zhipeng; Yu, Gang; Wang, Kaixuan; Chen, Xiaozhi; Shen, Chunhua |
| Tahun | 2023 |
| Venue / Jurnal | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | metric depth, zero-shot, camera model, canonical space |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2307.10984
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Metric3D%3A%20Towards%20Zero-Shot%20Metric%203D%20Prediction%20from%20a%20Single%20Image
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Metric3D%3A%20Towards%20Zero-Shot%20Metric%203D%20Prediction%20from%20a%20Single%20Image&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2307.10984 |

## Ringkasan Eksekutif
Metric3D mengatasi ambiguitas skala pada depth monokular zero-shot dengan menormalkan citra ke ruang kamera kanonik, memungkinkan prediksi depth metrik akurat dari satu gambar lintas kamera dan domain.

## Abstrak (Parafrase)
Penulis mengidentifikasi bahwa perbedaan parameter intrinsik kamera adalah sumber utama ambiguitas skala pada depth metrik zero-shot. Dengan mentransformasikan citra/label ke ruang kamera kanonik selama pelatihan dan inferensi, Metric3D dapat memprediksi depth metrik yang konsisten untuk kamera arbitrer, memenangkan benchmark dan memungkinkan rekonstruksi metrik in-the-wild.

## Latar Belakang & Konteks
Depth metrik dari satu citra ambigu karena skala tergantung intrinsik kamera; solusi sebelumnya domain-spesifik.

## Permasalahan yang Diangkat
- Ambiguitas skala akibat intrinsik kamera beragam.
- Depth metrik zero-shot sulit.
- Rekonstruksi metrik in-the-wild belum andal.

## Tujuan & Pertanyaan Penelitian
- Menghapus ambiguitas skala via ruang kanonik.
- Depth metrik zero-shot lintas-kamera.
- Rekonstruksi 3D metrik general.

## Tinjauan Terdahulu / Posisi Literatur
Berbeda dari ZoeDepth (router domain) dengan pendekatan transformasi kamera kanonik yang eksplisit.

Karya/konsep pembanding yang relevan:

- ZoeDepth - relative-to-metric multi-domain.
- MiDaS - depth relatif.
- DPT - backbone dense.
- LeReS - depth 3D shape recovery.

## Metodologi & Arsitektur
Transformasi citra dan label depth ke ruang kamera kanonik berdasarkan intrinsik; latih model prediksi depth pada ruang ini; saat inferensi, prediksi ditransformasi balik ke kamera nyata untuk depth metrik.

Komponen / langkah metodologis utama:

- Canonical camera space transformation.
- Pelatihan pada data multi-kamera besar.
- Random proposal normalization.
- Rekonstruksi metrik balik ke kamera nyata.

## Kontribusi Utama
1. Solusi ambiguitas skala via ruang kanonik.
2. Depth metrik zero-shot lintas-kamera.
3. Pemenang benchmark depth.
4. Rekonstruksi metrik in-the-wild.

## Rincian Eksperimen
Berbagai dataset depth (NYU, KITTI, DDAD, dll.) untuk metrik zero-shot; uji rekonstruksi 3D metrik.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Zero-shot metrik | AbsRel | SOTA lintas-dataset |
| KITTI/NYU | RMSE/delta | akurat tanpa fine-tune domain |
| Rekonstruksi | kualitatif | skala metrik konsisten |

## Temuan Kunci
- Menormalkan kamera menghapus ambiguitas skala.
- Depth metrik zero-shot bisa akurat.
- Berlaku untuk kamera arbitrer.

## Keunggulan
- Metrik zero-shot lintas-kamera.
- Rekonstruksi 3D metrik.
- Generalisasi kuat.

## Keterbatasan
- Butuh intrinsik kamera diketahui.
- Data pelatihan multi-kamera besar.
- Kasus intrinsik ekstrem menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Depth metrik dari kamera arbitrer memperkuat pipeline RGB-D berbasis kamera untuk lokalisasi/rekonstruksi 3D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [175 - 2024 - Depth Anything V2 - Estimasi Kedalaman](./175%20-%202024%20-%20Depth%20Anything%20V2%20-%20Estimasi%20Kedalaman.md)
- [176 - 2023 - ZoeDepth - Estimasi Kedalaman](./176%20-%202023%20-%20ZoeDepth%20-%20Estimasi%20Kedalaman.md)
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
Metric3D memecahkan ambiguitas skala depth monokular via ruang kamera kanonik, memungkinkan depth metrik zero-shot yang akurat.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `yin2023metric3d` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 177/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
