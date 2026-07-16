# 084 - GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 084 dari 154 |
| Kunci BibTeX | `fang2020graspnet` |
| Judul | GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping |
| Penulis | Fang, Hao-Shu; Wang, Chenxi; Gou, Minghao; Lu, Cewu |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Grasp Robotik |
| Kata kunci | grasp, benchmark, 6-DoF, point cloud, dataset besar |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=GraspNet-1Billion%3A%20A%20Large-Scale%20Benchmark%20for%20General%20Object%20Grasping
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=GraspNet-1Billion%3A%20A%20Large-Scale%20Benchmark%20for%20General%20Object%20Grasping&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 11444--11453 |

## Ringkasan Eksekutif
Benchmark grasp umum berskala besar (1 miliar anotasi grasp) dengan jaringan baseline end-to-end dari point cloud RGB-D, menstandarkan evaluasi grasp 6-DoF.

## Abstrak (Parafrase)
GraspNet-1Billion menyediakan dataset grasp berskala masif: 190 scene tumpukan objek dengan ~1 miliar anotasi grasp 6-DoF terlabel dari point cloud RGB-D. Makalah juga menyediakan jaringan baseline end-to-end dan metrik evaluasi baru (berbasis analitik) yang menstandarkan penilaian grasp umum, menjadi infrastruktur kunci riset grasp modern.

## Latar Belakang & Konteks
Dataset grasp sebelumnya (Cornell/Jacquard) kecil dan terbatas grasp planar, membatasi generalisasi dan evaluasi adil untuk grasp 6-DoF umum.

## Permasalahan yang Diangkat
- Dataset grasp lama kecil (Cornell/Jacquard).
- Terbatas grasp planar (bukan 6-DoF).
- Generalisasi & evaluasi adil terbatas.
- Anotasi grasp mahal secara manual.
- Metrik evaluasi grasp belum seragam.

## Tujuan & Pertanyaan Penelitian
- Menyediakan dataset grasp 6-DoF berskala masif.
- Menyediakan baseline end-to-end & metrik baru.
- Menstandarkan evaluasi grasp umum.

## Tinjauan Terdahulu / Posisi Literatur
GraspNet menyediakan dataset & metrik grasp berskala.

Karya/konsep pembanding yang relevan:

- Cornell/Jacquard — dataset kecil (pembanding).
- Point cloud RGB-D — masukan.
- 6-DoF grasp — target.
- Metrik analitik grasp.

## Metodologi & Arsitektur
190 scene tumpukan objek difoto multi-view (RGB-D); anotasi ~1B grasp 6-DoF dihasilkan (analitik + verifikasi); baseline end-to-end memprediksi grasp dari point cloud; metrik evaluasi baru menilai kualitas grasp secara analitik.

Komponen / langkah metodologis utama:

- Dataset 190 scene, ~1B grasp 6-DoF.
- Anotasi dari point cloud RGB-D multi-view.
- Baseline end-to-end (point cloud -> grasp).
- Metrik evaluasi grasp analitik baru.
- Skenario tumpukan (clutter).
- Benchmark grasp umum.

## Kontribusi Utama
1. Dataset grasp 6-DoF berskala terbesar saat rilis.
2. Baseline end-to-end dari point cloud.
3. Metrik evaluasi grasp baru & seragam.
4. Infrastruktur kunci riset grasp modern.

## Rincian Eksperimen
Menyediakan benchmark GraspNet dengan metrik grasp analitik, dievaluasi oleh baseline dan banyak metode berikutnya.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| GraspNet benchmark | AP grasp | standar evaluasi 6-DoF |
| Dataset | skala | ~1B grasp, 190 scene |
| Baseline | end-to-end | point cloud -> grasp |

## Temuan Kunci
- Skala data besar penting untuk generalisasi grasp.
- Grasp 6-DoF lebih umum dari planar.
- Metrik seragam memungkinkan perbandingan adil.
- Point cloud RGB-D memadai untuk grasp umum.

## Keunggulan
- Dataset & metrik standar.
- Grasp 6-DoF berskala.
- Baseline end-to-end.

## Keterbatasan
- Anotasi analitik (bukan seluruhnya manual).
- Fokus setup tumpukan tertentu.
- Komputasi pemrosesan point cloud besar.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
GraspNet-1Billion adalah infrastruktur data-benchmark yang menopang riset grasp RGB-D modern dalam tinjauan (bandingkan YOLOv8-URE, BCMFNet).

## Hubungan dengan Entri Lain
Entri lain pada klaster **Grasp Robotik** yang baik dibaca berdampingan:

- [080 - 2015 - Deep Learning Robotic Grasps (Lenz dkk.) - Grasp Robotik](./080%20-%202015%20-%20Deep%20Learning%20Robotic%20Grasps%20%28Lenz%20dkk.%29%20-%20Grasp%20Robotik.md)
- [081 - 2018 - GG-CNN - Grasp Robotik](./081%20-%202018%20-%20GG-CNN%20-%20Grasp%20Robotik.md)
- [082 - 2020 - GR-ConvNet - Grasp Robotik](./082%20-%202020%20-%20GR-ConvNet%20-%20Grasp%20Robotik.md)
- [083 - 2022 - GR-ConvNet v2 - Grasp Robotik](./083%20-%202022%20-%20GR-ConvNet%20v2%20-%20Grasp%20Robotik.md)
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
GraspNet-1Billion menyediakan dataset grasp 6-DoF berskala miliaran anotasi dari point cloud RGB-D beserta baseline dan metrik, menstandarkan evaluasi grasp umum.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `fang2020graspnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 084/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
