# 131 - Breast Tumor Detection and Classification in Mammogram Images Using Modified YOLOv5 Network

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 131 dari 154 |
| Kunci BibTeX | `mohiyuddin2022breast` |
| Judul | Breast Tumor Detection and Classification in Mammogram Images Using Modified YOLOv5 Network |
| Penulis | Mohiyuddin, Aqsa; Basharat, Asma; Ghani, Usman; Peter, Vaclav; Abbas, Sidra; Naeem, Osama Bin; Rizwan, Muhammad |
| Tahun | 2022 |
| Venue / Jurnal | Computational and Mathematical Methods in Medicine |
| Tema klaster | Medis |
| Kata kunci | medis, payudara, YOLOv5, mamogram, tumor |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-medis)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Breast%20Tumor%20Detection%20and%20Classification%20in%20Mammogram%20Images%20Using%20Modified%20YOLOv5%20Network
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Breast%20Tumor%20Detection%20and%20Classification%20in%20Mammogram%20Images%20Using%20Modified%20YOLOv5%20Network&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 2022 |
| Halaman | 1359019 |

## Ringkasan Eksekutif
YOLOv5 termodifikasi untuk deteksi dan klasifikasi tumor payudara pada citra mamogram.

## Abstrak (Parafrase)
Mohiyuddin dkk. memodifikasi arsitektur YOLOv5 untuk mendeteksi dan mengklasifikasikan tumor payudara pada mamogram secara akurat dan efisien. Modifikasi meningkatkan deteksi tumor dibanding YOLOv5 baseline, mendukung diagnosis payudara.

## Latar Belakang & Konteks
Deteksi tumor payudara akurat dan efisien pada mamogram diperlukan untuk skrining; YOLOv5 baseline dapat ditingkatkan untuk domain ini.

## Permasalahan yang Diangkat
- Deteksi tumor payudara perlu akurat & efisien.
- Tumor bervariasi dan mudah terlewat.
- YOLOv5 baseline dapat ditingkatkan.
- Skrining menuntut keandalan.
- Data mamogram terbatas.

## Tujuan & Pertanyaan Penelitian
- Memodifikasi YOLOv5 untuk domain mamografi.
- Mendeteksi & mengklasifikasikan tumor.
- Meningkatkan akurasi atas baseline.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menyempurnakan YOLOv5 untuk pencitraan payudara.

Karya/konsep pembanding yang relevan:

- YOLOv5 — detektor dasar.
- Modifikasi arsitektur.
- Mamogram.
- Deteksi/klasifikasi tumor.

## Metodologi & Arsitektur
YOLOv5 dimodifikasi (arsitektur/komponen) untuk deteksi tumor payudara; dilatih pada citra mamogram; dievaluasi untuk deteksi dan klasifikasi tumor, dibandingkan YOLOv5 baseline.

Komponen / langkah metodologis utama:

- Modifikasi arsitektur YOLOv5.
- Deteksi tumor payudara.
- Klasifikasi tumor.
- Pelatihan pada mamogram.
- Perbandingan dengan baseline.
- Dukungan diagnosis.

## Kontribusi Utama
1. Adaptasi YOLOv5 untuk mamografi.
2. Deteksi & klasifikasi tumor akurat.
3. Peningkatan atas baseline.
4. Contoh YOLOv5 untuk pencitraan payudara.

## Rincian Eksperimen
Diuji pada dataset mamogram dengan metrik deteksi/klasifikasi tumor (Computational and Mathematical Methods in Medicine 2022).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Mamogram | deteksi/klasifikasi | tinggi |
| Tumor | akurasi | peningkatan atas baseline |
| vs YOLOv5 | perbandingan | modifikasi menyumbang gain |

## Temuan Kunci
- Modifikasi YOLOv5 meningkatkan deteksi tumor.
- Adaptasi domain bermanfaat.
- Deteksi+klasifikasi mendukung diagnosis.
- Validasi klinis diperlukan.

## Keunggulan
- Adaptasi YOLOv5.
- Deteksi+klasifikasi.
- Peningkatan.

## Keterbatasan
- Data terbatas.
- Validasi klinis diperlukan.
- Bias dataset mungkin.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini melengkapi klaster Medis tinjauan dengan adaptasi YOLOv5 untuk pencitraan payudara.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Medis** yang baik dibaca berdampingan:

- [128 - 2024 - Systematic Review YOLO Medis (Qureshi dkk.) - Medis](./128%20-%202024%20-%20Systematic%20Review%20YOLO%20Medis%20%28Qureshi%20dkk.%29%20-%20Medis.md)
- [129 - 2021 - COVID-19 CAD dari X-Ray (Al-Antari dkk.) - Medis](./129%20-%202021%20-%20COVID-19%20CAD%20dari%20X-Ray%20%28Al-Antari%20dkk.%29%20-%20Medis.md)
- [130 - 2021 - Breast Lesion Detection (YOLO Fusion) - Medis](./130%20-%202021%20-%20Breast%20Lesion%20Detection%20%28YOLO%20Fusion%29%20-%20Medis.md)
- [132 - 2023 - YOLO untuk Deteksi Polip (Wan dkk.) - Medis](./132%20-%202023%20-%20YOLO%20untuk%20Deteksi%20Polip%20%28Wan%20dkk.%29%20-%20Medis.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Medis** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Medis)
Istilah penting untuk memahami makalah ini:

- **CAD** — Computer-Aided Diagnosis.
- **Deteksi lesi** — Melokalisasi kelainan (tumor, polip).
- **Mamografi** — Rontgen payudara untuk skrining.
- **Kolonoskopi** — Pencitraan usus untuk polip.
- **X-ray dada** — Rontgen toraks (COVID/pneumonia).
- **Sensitivitas/spesifisitas** — Benar-positif / benar-negatif.
- **Real-time** — Deteksi seketika saat prosedur.
- **Kelas tak seimbang** — Kasus abnormal jauh lebih sedikit.
- **Transfer learning** — Bobot pra-latih untuk data terbatas.
- **Validasi klinis** — Uji pada data pasien nyata.

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
Mohiyuddin dkk. memodifikasi YOLOv5 untuk deteksi dan klasifikasi tumor payudara pada mamogram, meningkatkan akurasi atas baseline untuk mendukung diagnosis.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `mohiyuddin2022breast` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 131/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
