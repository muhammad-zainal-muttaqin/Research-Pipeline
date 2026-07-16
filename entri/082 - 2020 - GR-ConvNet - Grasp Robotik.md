# 082 - Antipodal Robotic Grasping Using Generative Residual Convolutional Neural Network

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 082 dari 154 |
| Kunci BibTeX | `kumra2020grconvnet` |
| Judul | Antipodal Robotic Grasping Using Generative Residual Convolutional Neural Network |
| Penulis | Kumra, Sulabh; Joshi, Shirin; Sahin, Ferat |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) |
| Tema klaster | Grasp Robotik |
| Kata kunci | grasp, generative residual, RGB-D, antipodal, Cornell/Jacquard |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Antipodal%20Robotic%20Grasping%20Using%20Generative%20Residual%20Convolutional%20Neural%20Network
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Antipodal%20Robotic%20Grasping%20Using%20Generative%20Residual%20Convolutional%20Neural%20Network&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 9626--9633 |

## Ringkasan Eksekutif
Jaringan grasp generatif residual yang memprediksi grasp antipodal per-piksel dari input RGB-D n-kanal untuk grasp multi-objek dengan akurasi tinggi.

## Abstrak (Parafrase)
GR-ConvNet (Generative Residual Convolutional Network) memprediksi peta grasp antipodal per-piksel (quality, angle, width) dari input RGB-D (n-kanal). Dengan blok residual, ia lebih akurat dari GG-CNN, mendukung grasp multi-objek, mencapai akurasi ~97%/95% pada Cornell/Jacquard, dan divalidasi pada robot nyata.

## Latar Belakang & Konteks
Grasp perlu akurat, cepat, dan general untuk banyak objek/multi-objek; pendekatan sebelumnya (GG-CNN) ringan namun akurasinya dapat ditingkatkan.

## Permasalahan yang Diangkat
- Grasp perlu akurat sekaligus cepat.
- Generalisasi ke banyak objek/multi-objek.
- GG-CNN ringan namun akurasi bisa ditingkatkan.
- Fusi RGB dan kedalaman perlu dimanfaatkan.
- Validasi robot nyata diperlukan.

## Tujuan & Pertanyaan Penelitian
- Memprediksi grasp antipodal per-piksel dari RGB-D.
- Meningkatkan akurasi via blok residual.
- Mendukung grasp multi-objek & robot nyata.

## Tinjauan Terdahulu / Posisi Literatur
GR-ConvNet menyempurnakan grasp generatif (GG-CNN) dengan arsitektur residual.

Karya/konsep pembanding yang relevan:

- GG-CNN — pendahulu generatif.
- Residual blocks (ResNet).
- RGB-D input (n-channel).
- Cornell/Jacquard dataset.

## Metodologi & Arsitektur
Arsitektur generative residual (encoder konvolusi + blok residual + decoder) menerima input RGB-D n-kanal dan menghasilkan tiga peta per-piksel (quality/angle/width); grasp terbaik dipilih dari peta quality; divalidasi pada robot.

Komponen / langkah metodologis utama:

- Generative residual architecture.
- Input RGB-D (n-channel).
- Output peta grasp per-piksel (quality/angle/width).
- Blok residual untuk akurasi.
- Grasp multi-objek.
- Validasi robot nyata.

## Kontribusi Utama
1. Grasp generatif residual akurat dari RGB-D.
2. Mendukung multi-objek.
3. Akurasi ~97%/95% (Cornell/Jacquard).
4. Divalidasi pada robot nyata.

## Rincian Eksperimen
Diuji pada Cornell dan Jacquard dengan metrik akurasi grasp, plus eksperimen robot fisik.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Cornell | akurasi grasp | ~97% |
| Jacquard | akurasi grasp | ~95% |
| Robot nyata | success rate | tinggi |

## Temuan Kunci
- Blok residual meningkatkan akurasi grasp.
- RGB-D lebih baik dari depth saja pada kasus tertentu.
- Grasp generatif per-piksel efektif multi-objek.
- Validasi robot memperkuat kepraktisan.

## Keunggulan
- Akurasi tinggi.
- Multi-objek.
- Divalidasi robot.

## Keterbatasan
- Grasp planar (bukan 6-DoF penuh).
- Bergantung kualitas RGB-D.
- Objek berhimpitan tetap menantang.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
GR-ConvNet adalah baseline kuat grasp berbasis RGB-D dalam tinjauan; menegaskan manfaat fusi RGB+Depth untuk manipulasi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Grasp Robotik** yang baik dibaca berdampingan:

- [080 - 2015 - Deep Learning Robotic Grasps (Lenz dkk.) - Grasp Robotik](./080%20-%202015%20-%20Deep%20Learning%20Robotic%20Grasps%20%28Lenz%20dkk.%29%20-%20Grasp%20Robotik.md)
- [081 - 2018 - GG-CNN - Grasp Robotik](./081%20-%202018%20-%20GG-CNN%20-%20Grasp%20Robotik.md)
- [083 - 2022 - GR-ConvNet v2 - Grasp Robotik](./083%20-%202022%20-%20GR-ConvNet%20v2%20-%20Grasp%20Robotik.md)
- [084 - 2020 - GraspNet-1Billion - Grasp Robotik](./084%20-%202020%20-%20GraspNet-1Billion%20-%20Grasp%20Robotik.md)
- [085 - 2023 - BCMFNet (Bilateral Cross-Modal Fusion) - Grasp Robotik](./085%20-%202023%20-%20BCMFNet%20%28Bilateral%20Cross-Modal%20Fusion%29%20-%20Grasp%20Robotik.md)
- [086 - 2018 - Jacquard Dataset - Grasp Robotik](./086%20-%202018%20-%20Jacquard%20Dataset%20-%20Grasp%20Robotik.md)

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
GR-ConvNet memprediksi grasp antipodal per-piksel dari RGB-D dengan arsitektur generative residual, mencapai akurasi tinggi pada Cornell/Jacquard dan validasi robot nyata.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `kumra2020grconvnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 082/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
