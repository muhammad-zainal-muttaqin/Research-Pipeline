# 129 - Fast Deep Learning Computer-Aided Diagnosis of COVID-19 Based on Digital Chest X-Ray Images

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 129 dari 154 |
| Kunci BibTeX | `alantari2020covid` |
| Judul | Fast Deep Learning Computer-Aided Diagnosis of COVID-19 Based on Digital Chest X-Ray Images |
| Penulis | Al-Antari, Mugahed A.; Hua, Cam-Hao; Bang, Jaehun; Lee, Sungyoung |
| Tahun | 2021 |
| Venue / Jurnal | Applied Intelligence |
| Tema klaster | Medis |
| Kata kunci | medis, COVID-19, X-ray, deteksi+klasifikasi, CAD |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Fast%20Deep%20Learning%20Computer-Aided%20Diagnosis%20of%20COVID-19%20Based%20on%20Digital%20Chest%20X-Ray%20Images
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Fast%20Deep%20Learning%20Computer-Aided%20Diagnosis%20of%20COVID-19%20Based%20on%20Digital%20Chest%20X-Ray%20Images&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 51 |
| Nomor | 5 |
| Halaman | 2890--2907 |

## Ringkasan Eksekutif
Sistem diagnosis berbantuan komputer cepat berbasis deep learning (deteksi gaya YOLO + klasifikasi) untuk COVID-19 dari citra rontgen dada digital.

## Abstrak (Parafrase)
Al-Antari dkk. mengembangkan pipeline CAD cepat untuk COVID-19 dari X-ray dada: deteksi region relevan (gaya YOLO) diikuti klasifikasi multi-kelas (COVID-19/pneumonia/normal) memakai deep learning. Sistem dirancang cepat dan akurat untuk membantu diagnosis saat pandemi.

## Latar Belakang & Konteks
Diagnosis COVID-19 dari X-ray perlu cepat dan akurat saat pandemi untuk triase, namun interpretasi manual lambat dan bervariasi.

## Permasalahan yang Diangkat
- Diagnosis COVID-19 dari X-ray perlu cepat & akurat.
- Interpretasi manual lambat & bervariasi.
- Triase pandemi menuntut otomasi.
- Kelas (COVID/pneumonia/normal) perlu dibedakan.
- Data medis terbatas.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi region relevan pada X-ray (gaya YOLO).
- Mengklasifikasikan multi-kelas penyakit.
- Menyediakan CAD cepat untuk COVID-19.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menggabungkan deteksi dan klasifikasi CNN untuk X-ray.

Karya/konsep pembanding yang relevan:

- Detektor gaya YOLO — deteksi region.
- Klasifikasi CNN multi-kelas.
- X-ray dada digital.
- CAD (diagnosis berbantuan komputer).

## Metodologi & Arsitektur
Tahap deteksi (gaya YOLO) melokalisasi region paru/relevan pada X-ray; tahap klasifikasi CNN mengklasifikasikan ke COVID-19/pneumonia/normal; pipeline dioptimalkan untuk kecepatan diagnosis; dievaluasi pada dataset X-ray dada.

Komponen / langkah metodologis utama:

- Deteksi region relevan (gaya YOLO).
- Klasifikasi CNN multi-kelas.
- Pipeline deteksi+klasifikasi.
- Optimasi kecepatan diagnosis.
- Evaluasi X-ray dada.
- Kelas COVID/pneumonia/normal.

## Kontribusi Utama
1. Pipeline CAD deteksi+klasifikasi cepat.
2. Klasifikasi multi-kelas akurat.
3. Dukungan diagnosis COVID-19.
4. Contoh deteksi+klasifikasi medis.

## Rincian Eksperimen
Diuji pada dataset X-ray dada dengan metrik klasifikasi (akurasi/sensitivitas/spesifisitas) (Applied Intelligence 2021).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| X-ray dada | akurasi | klasifikasi tinggi |
| Multi-kelas | sensitivitas/spesifisitas | COVID/pneumonia/normal |
| Kecepatan | diagnosis | cepat |

## Temuan Kunci
- Deteksi+klasifikasi mempercepat diagnosis.
- Deep learning akurat untuk X-ray COVID.
- Multi-kelas membedakan penyakit.
- Validasi klinis tetap diperlukan.

## Keunggulan
- CAD cepat.
- Deteksi+klasifikasi.
- Multi-kelas.

## Keterbatasan
- Data terbatas (generalisasi).
- Validasi klinis nyata diperlukan.
- Bias dataset mungkin.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini mencontohkan pipeline deteksi+klasifikasi medis cepat dalam klaster Medis tinjauan, menegaskan peran deteksi gaya YOLO di citra klinis.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Medis** yang baik dibaca berdampingan:

- [128 - 2024 - Systematic Review YOLO Medis (Qureshi dkk.) - Medis](./128%20-%202024%20-%20Systematic%20Review%20YOLO%20Medis%20%28Qureshi%20dkk.%29%20-%20Medis.md)
- [130 - 2021 - Breast Lesion Detection (YOLO Fusion) - Medis](./130%20-%202021%20-%20Breast%20Lesion%20Detection%20%28YOLO%20Fusion%29%20-%20Medis.md)
- [131 - 2022 - Breast Tumor Detection (Modified YOLOv5) - Medis](./131%20-%202022%20-%20Breast%20Tumor%20Detection%20%28Modified%20YOLOv5%29%20-%20Medis.md)
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
Al-Antari dkk. mengembangkan CAD cepat berbasis deep learning (deteksi gaya YOLO + klasifikasi) untuk COVID-19 dari X-ray dada, membedakan COVID/pneumonia/normal untuk dukungan diagnosis.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `alantari2020covid` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 129/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
