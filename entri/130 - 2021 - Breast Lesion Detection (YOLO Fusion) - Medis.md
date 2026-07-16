# 130 - Breast Lesions Detection and Classification via YOLO-Based Fusion Models

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 130 dari 154 |
| Kunci BibTeX | `baccouche2021breast` |
| Judul | Breast Lesions Detection and Classification via YOLO-Based Fusion Models |
| Penulis | Baccouche, Asma; Garcia-Zapirain, Begonya; Castillo Olea, Cristian; Elmaghraby, Adel S. |
| Tahun | 2021 |
| Venue / Jurnal | Computers, Materials \& Continua |
| Tema klaster | Medis |
| Kata kunci | medis, payudara, mamografi, YOLO fusion, deteksi lesi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Breast%20Lesions%20Detection%20and%20Classification%20via%20YOLO-Based%20Fusion%20Models
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Breast%20Lesions%20Detection%20and%20Classification%20via%20YOLO-Based%20Fusion%20Models&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 69 |
| Nomor | 1 |
| Halaman | 1407--1425 |

## Ringkasan Eksekutif
Model fusi berbasis YOLO untuk deteksi dan klasifikasi lesi payudara pada mamografi.

## Abstrak (Parafrase)
Baccouche dkk. mengusulkan model fusi berbasis YOLO untuk mendeteksi dan mengklasifikasikan lesi payudara pada citra mamografi. YOLO melokalisasi lesi dan model fusi mengklasifikasikan jinak/ganas, membantu skrining kanker payudara dini.

## Latar Belakang & Konteks
Deteksi lesi payudara dini krusial namun menantang pada mamogram karena lesi bervariasi bentuk/kontras dan mudah terlewat.

## Permasalahan yang Diangkat
- Lesi payudara bervariasi bentuk/kontras.
- Lesi mudah terlewat pada mamogram.
- Deteksi + klasifikasi diperlukan.
- Skrining dini krusial.
- Data medis terbatas.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi lesi payudara via YOLO.
- Mengklasifikasikan jinak/ganas via fusi.
- Mendukung skrining kanker dini.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menggabungkan YOLO dan model fusi/klasifikasi.

Karya/konsep pembanding yang relevan:

- YOLO — deteksi lesi.
- Model fusi — klasifikasi.
- Mamografi.
- Skrining payudara.

## Metodologi & Arsitektur
YOLO melokalisasi lesi pada mamogram; model fusi menggabungkan fitur/keputusan untuk klasifikasi jinak/ganas; pipeline dievaluasi pada dataset mamografi untuk deteksi dan klasifikasi.

Komponen / langkah metodologis utama:

- Deteksi lesi via YOLO.
- Model fusi untuk klasifikasi.
- Klasifikasi jinak/ganas.
- Pipeline deteksi+klasifikasi.
- Evaluasi mamografi.
- Dukungan skrining.

## Kontribusi Utama
1. YOLO efektif melokalisasi lesi mamografi.
2. Model fusi meningkatkan klasifikasi.
3. Deteksi+klasifikasi terpadu.
4. Dukungan skrining kanker dini.

## Rincian Eksperimen
Diuji pada dataset mamografi dengan metrik deteksi dan klasifikasi (Computers, Materials & Continua 2021).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Mamografi | deteksi/klasifikasi | akurat |
| Jinak/ganas | klasifikasi | fusi meningkatkan |
| Skrining | dukungan | deteksi lesi dini |

## Temuan Kunci
- YOLO cocok untuk lokalisasi lesi mamografi.
- Fusi meningkatkan klasifikasi.
- Deteksi+klasifikasi bermanfaat klinis.
- Validasi klinis diperlukan.

## Keunggulan
- Deteksi+klasifikasi lesi.
- Model fusi.
- Dukungan skrining.

## Keterbatasan
- Data terbatas.
- Validasi klinis diperlukan.
- Bias dataset mungkin.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini menunjukkan YOLO untuk lokalisasi lesi mamografi dalam klaster Medis tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Medis** yang baik dibaca berdampingan:

- [128 - 2024 - Systematic Review YOLO Medis (Qureshi dkk.) - Medis](./128%20-%202024%20-%20Systematic%20Review%20YOLO%20Medis%20%28Qureshi%20dkk.%29%20-%20Medis.md)
- [129 - 2021 - COVID-19 CAD dari X-Ray (Al-Antari dkk.) - Medis](./129%20-%202021%20-%20COVID-19%20CAD%20dari%20X-Ray%20%28Al-Antari%20dkk.%29%20-%20Medis.md)
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
Baccouche dkk. mengusulkan model fusi berbasis YOLO untuk deteksi dan klasifikasi lesi payudara pada mamografi, mendukung skrining kanker dini.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `baccouche2021breast` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 130/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
