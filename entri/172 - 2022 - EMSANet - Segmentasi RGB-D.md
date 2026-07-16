# 172 - Efficient Multi-Task RGB-D Scene Analysis for Indoor Environments

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 172 dari 191 |
| Kunci BibTeX | `seichter2022emsanet` |
| Judul | Efficient Multi-Task RGB-D Scene Analysis for Indoor Environments |
| Penulis | Seichter, Daniel; Fischedick, S{\"o |
| Tahun | 2022 |
| Venue / Jurnal | International Joint Conference on Neural Networks (IJCNN) |
| Tema klaster | Segmentasi RGB-D |
| Kata kunci | RGB-D segmentation, multi-task, panoptic, real-time indoor |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2207.04526
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Efficient%20Multi-Task%20RGB-D%20Scene%20Analysis%20for%20Indoor%20Environments
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Efficient%20Multi-Task%20RGB-D%20Scene%20Analysis%20for%20Indoor%20Environments&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2207.04526 |

## Ringkasan Eksekutif
EMSANet melakukan analisis scene indoor RGB-D multitugas (segmentasi semantik + instance/panoptik dan tugas tambahan) secara efisien dan real-time dalam satu jaringan bersama.

## Abstrak (Parafrase)
Penulis memperluas ESANet menjadi jaringan multitugas yang berbagi encoder RGB-D untuk beberapa keluaran analisis scene - segmentasi semantik, segmentasi instance (panoptik), serta tugas tambahan - dengan biaya rendah. Dengan berbagi representasi, EMSANet mencapai kinerja kompetitif pada NYUv2/SUNRGB-D sambil tetap real-time, cocok untuk robotika.

## Latar Belakang & Konteks
Robot indoor butuh banyak keluaran persepsi; menjalankan model terpisah mahal. Berbagi encoder RGB-D multitugas lebih efisien.

## Permasalahan yang Diangkat
- Model per-tugas mahal untuk robot.
- Perlu real-time RGB-D indoor.
- Menggabungkan banyak tugas tanpa saling merusak.

## Tujuan & Pertanyaan Penelitian
- Analisis scene RGB-D multitugas efisien.
- Berbagi encoder untuk beberapa keluaran.
- Menjaga real-time.

## Tinjauan Terdahulu / Posisi Literatur
Kelanjutan ESANet (segmentasi RGB-D efisien); berdialog dengan panoptic segmentation multitugas.

Karya/konsep pembanding yang relevan:

- ESANet - segmentasi RGB-D efisien.
- Panoptic FPN - segmentasi panoptik.
- RedNet/ACNet - fusi RGB-D.
- Multi-task learning umum.

## Metodologi & Arsitektur
Encoder ganda RGB dan depth dengan fusi; dekoder bercabang untuk tiap tugas (semantik, instance/panoptik, orientasi); pelatihan multitugas dengan pembobotan kerugian.

Komponen / langkah metodologis utama:

- Encoder RGB-D berbagi + fusi.
- Dekoder multitugas (semantik + panoptik + lainnya).
- Optimasi real-time.
- Pembobotan kerugian multitugas.

## Kontribusi Utama
1. Jaringan analisis scene RGB-D multitugas efisien.
2. Berbagi representasi lintas-tugas.
3. Real-time pada perangkat robot.
4. Hasil kompetitif indoor.

## Rincian Eksperimen
NYUv2 dan SUNRGB-D untuk segmentasi (mIoU/PQ) plus pengukuran FPS pada perangkat embedded.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | mIoU | kompetitif |
| SUNRGB-D | mIoU/PQ | seimbang lintas tugas |
| Kecepatan | FPS | real-time pada GPU embedded |

## Temuan Kunci
- Berbagi encoder RGB-D menekan biaya multitugas.
- Real-time dapat dicapai untuk analisis scene lengkap.
- Tugas saling menguatkan bila diseimbangkan.

## Keunggulan
- Efisien multitugas.
- Real-time.
- Praktis untuk robot indoor.

## Keterbatasan
- Penyeimbangan kerugian rumit.
- Bergantung kualitas depth.
- Skala outdoor tak difokuskan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Contoh langsung persepsi RGB-D multitugas untuk robotika, sejalan dengan fokus aplikasi YOLO+RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Segmentasi RGB-D** yang baik dibaca berdampingan:

- [171 - 2021 - SegFormer - Segmentasi RGB-D](./171%20-%202021%20-%20SegFormer%20-%20Segmentasi%20RGB-D.md)
- [173 - 2024 - GeminiFusion - Segmentasi RGB-D](./173%20-%202024%20-%20GeminiFusion%20-%20Segmentasi%20RGB-D.md)
- [174 - 2022 - Omnivore - Segmentasi RGB-D](./174%20-%202022%20-%20Omnivore%20-%20Segmentasi%20RGB-D.md)

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
EMSANet menghadirkan analisis scene RGB-D multitugas yang efisien dan real-time, relevan untuk robot indoor.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `seichter2022emsanet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 172/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
