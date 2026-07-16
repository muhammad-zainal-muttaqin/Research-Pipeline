# 086 - Jacquard: A Large Scale Dataset for Robotic Grasp Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 086 dari 154 |
| Kunci BibTeX | `depierre2018jacquard` |
| Judul | Jacquard: A Large Scale Dataset for Robotic Grasp Detection |
| Penulis | Depierre, Amaury; Dellandr{\'e |
| Tahun | 2018 |
| Venue / Jurnal | Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) |
| Tema klaster | Grasp Robotik |
| Kata kunci | grasp, dataset sintetis, simulasi, berskala, benchmark |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-grasp-robotik)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Jacquard%3A%20A%20Large%20Scale%20Dataset%20for%20Robotic%20Grasp%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Jacquard%3A%20A%20Large%20Scale%20Dataset%20for%20Robotic%20Grasp%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 3511--3516 |

## Ringkasan Eksekutif
Dataset grasp robotik berskala besar yang dibangun secara sintetis lewat simulasi, jauh lebih besar dari Cornell, menjadi standar pelatihan model grasp dalam.

## Abstrak (Parafrase)
Jacquard adalah dataset grasp yang dibangun otomatis melalui simulasi fisika: objek 3D di-render dan grasp yang berhasil (simulated grasp trial) dianotasi, menghasilkan ~54 ribu citra dengan ~1.1 juta anotasi grasp. Skalanya jauh melampaui Cornell, memungkinkan pelatihan model grasp dalam, dan menyediakan metrik SGT (simulated grasp trial).

## Latar Belakang & Konteks
Cornell Grasp Dataset terlalu kecil untuk melatih model grasp dalam modern, membatasi generalisasi; anotasi manual grasp mahal dan lambat.

## Permasalahan yang Diangkat
- Cornell terlalu kecil untuk model grasp dalam.
- Anotasi grasp manual mahal & lambat.
- Generalisasi terbatas oleh data kecil.
- Evaluasi grasp perlu metrik terverifikasi.
- Ragam objek/grasp perlu diperbanyak.

## Tujuan & Pertanyaan Penelitian
- Membangun dataset grasp berskala via simulasi.
- Menyediakan anotasi grasp masif otomatis.
- Menyediakan metrik evaluasi (SGT).

## Tinjauan Terdahulu / Posisi Literatur
Jacquard menyediakan dataset grasp sintetis berskala.

Karya/konsep pembanding yang relevan:

- Cornell — dataset kecil (pembanding).
- Simulasi fisika grasp.
- Oriented rectangle grasp.
- Simulated Grasp Trial (SGT) metric.

## Metodologi & Arsitektur
Objek 3D dari basis data di-render dalam simulasi; grasp candidate diuji secara fisika; grasp yang berhasil dianotasi sebagai oriented rectangle; menghasilkan ~54k citra & ~1.1M grasp; metrik SGT mengevaluasi keberhasilan grasp tersimulasi.

Komponen / langkah metodologis utama:

- Pembangunan dataset via simulasi fisika.
- ~54k citra, ~1.1M anotasi grasp.
- Representasi oriented rectangle.
- Metrik SGT (simulated grasp trial).
- Ragam objek 3D besar.
- Anotasi otomatis berskala.

## Kontribusi Utama
1. Dataset grasp sintetis berskala besar.
2. Anotasi otomatis masif via simulasi.
3. Metrik SGT untuk evaluasi.
4. Memungkinkan pelatihan model grasp dalam.

## Rincian Eksperimen
Dipakai untuk melatih/menguji model grasp (mis. GR-ConvNet) dengan metrik akurasi grasp dan SGT.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Jacquard | akurasi/SGT | standar pelatihan/uji grasp |
| Skala | citra/grasp | ~54k / ~1.1M |
| Metrik | SGT | evaluasi grasp tersimulasi |

## Temuan Kunci
- Data sintetis berskala memungkinkan model grasp dalam.
- Simulasi mengurangi biaya anotasi.
- Metrik SGT melengkapi metrik rectangle.
- Generalisasi membaik dengan data besar.

## Keunggulan
- Dataset besar & sintetis.
- Anotasi otomatis.
- Metrik SGT.

## Keterbatasan
- Domain gap simulasi-ke-nyata.
- Grasp planar (oriented rectangle).
- Kualitas bergantung realisme simulasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Jacquard adalah dataset grasp standar yang dipakai luas dalam tinjauan (mis. GR-ConvNet, BCMFNet), menopang pelatihan model grasp RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Grasp Robotik** yang baik dibaca berdampingan:

- [080 - 2015 - Deep Learning Robotic Grasps (Lenz dkk.) - Grasp Robotik](./080%20-%202015%20-%20Deep%20Learning%20Robotic%20Grasps%20%28Lenz%20dkk.%29%20-%20Grasp%20Robotik.md)
- [081 - 2018 - GG-CNN - Grasp Robotik](./081%20-%202018%20-%20GG-CNN%20-%20Grasp%20Robotik.md)
- [082 - 2020 - GR-ConvNet - Grasp Robotik](./082%20-%202020%20-%20GR-ConvNet%20-%20Grasp%20Robotik.md)
- [083 - 2022 - GR-ConvNet v2 - Grasp Robotik](./083%20-%202022%20-%20GR-ConvNet%20v2%20-%20Grasp%20Robotik.md)
- [084 - 2020 - GraspNet-1Billion - Grasp Robotik](./084%20-%202020%20-%20GraspNet-1Billion%20-%20Grasp%20Robotik.md)
- [085 - 2023 - BCMFNet (Bilateral Cross-Modal Fusion) - Grasp Robotik](./085%20-%202023%20-%20BCMFNet%20%28Bilateral%20Cross-Modal%20Fusion%29%20-%20Grasp%20Robotik.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Grasp Robotik** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Grasp Robotik)
Istilah penting untuk memahami makalah ini:

- **Grasp detection** — Prediksi cengkeraman stabil untuk objek.
- **Grasp rectangle** — Grasp sebagai kotak beorientasi (posisi, sudut, lebar).
- **Antipodal grasp** — Cengkeraman dua-jari berlawanan.
- **RGB-D** — Warna + kedalaman untuk geometri grasp.
- **6-DoF grasp** — Grasp enam derajat kebebasan di ruang 3D.
- **Cornell dataset** — Dataset grasp kecil klasik.
- **Jacquard** — Dataset grasp sintetis berskala besar.
- **Closed-loop** — Kontrol grasp real-time berbasis umpan-balik.
- **Success rate** — Persentase percobaan grasp berhasil.
- **Point cloud fusion** — Penggabungan geometri titik 3D.

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
Jacquard menyediakan dataset grasp sintetis berskala besar (~1.1M anotasi) via simulasi dengan metrik SGT, memungkinkan pelatihan model grasp dalam melampaui keterbatasan Cornell.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `depierre2018jacquard` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 086/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
