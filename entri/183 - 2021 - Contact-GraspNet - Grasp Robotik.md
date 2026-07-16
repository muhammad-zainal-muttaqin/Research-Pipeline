# 183 - Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 183 dari 191 |
| Kunci BibTeX | `sundermeyer2021contactgraspnet` |
| Judul | Contact-GraspNet: Efficient 6-DoF Grasp Generation in Cluttered Scenes |
| Penulis | Sundermeyer, Martin; Mousavian, Arsalan; Triebel, Rudolph; Fox, Dieter |
| Tahun | 2021 |
| Venue / Jurnal | IEEE International Conference on Robotics and Automation (ICRA) |
| Tema klaster | Grasp Robotik |
| Kata kunci | 6-DoF grasp, cluttered scenes, point cloud, contact points |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/2103.14127
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Contact-GraspNet%3A%20Efficient%206-DoF%20Grasp%20Generation%20in%20Cluttered%20Scenes
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Contact-GraspNet%3A%20Efficient%206-DoF%20Grasp%20Generation%20in%20Cluttered%20Scenes&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 2103.14127 |

## Ringkasan Eksekutif
Contact-GraspNet menghasilkan grasp 6-DoF langsung dari point cloud scene berantakan dengan merepresentasikan grasp sebagai berlabuh pada titik kontak yang teramati, menyederhanakan ruang pencarian dan mencapai keberhasilan tinggi.

## Abstrak (Parafrase)
Penulis mengurangi dimensi ruang grasp dengan menautkan setiap grasp 6-DoF ke titik kontak pada point cloud teramati; jaringan memprediksi grasp per-titik beserta skor. Karena grasp berakar pada titik nyata, representasi menjadi lebih ringkas dan generalizable. Dilatih pada data sintetis, metode ini menggeneralisasi ke scene nyata berantakan dengan tingkat keberhasilan grasp tinggi.

## Latar Belakang & Konteks
Grasp 6-DoF di scene berantakan memerlukan pencarian ruang besar. Menautkan grasp ke titik kontak mengurangi kompleksitas.

## Permasalahan yang Diangkat
- Ruang grasp 6-DoF sangat besar.
- Scene berantakan menyulitkan.
- Generalisasi sintetis ke nyata.

## Tujuan & Pertanyaan Penelitian
- Menyederhanakan representasi grasp via titik kontak.
- Menghasilkan grasp 6-DoF dari point cloud.
- Generalisasi ke scene nyata.

## Tinjauan Terdahulu / Posisi Literatur
Melanjutkan GraspNet-1Billion dan 6-DOF GraspNet; kebaruan pada penautan grasp ke titik kontak teramati.

Karya/konsep pembanding yang relevan:

- GraspNet-1Billion - benchmark grasp besar.
- 6-DOF GraspNet - sampling+evaluasi grasp.
- VGN - grasp volumetrik.
- PointNet++ - encoder point cloud.

## Metodologi & Arsitektur
Encoder point cloud (PointNet++) memproses scene; untuk tiap titik kontak, prediksi arah/baseline/lebar grasp dan skor; representasi contact-based mengurangi parameter grasp; filter collision menyeleksi grasp final.

Komponen / langkah metodologis utama:

- Grasp berakar pada titik kontak teramati.
- Prediksi grasp per-titik + skor.
- Pelatihan pada data sintetis.
- Penyaringan tabrakan untuk seleksi.

## Kontribusi Utama
1. Representasi grasp berbasis titik kontak.
2. Grasp 6-DoF efisien di clutter.
3. Generalisasi sintetis ke nyata.
4. Keberhasilan grasp tinggi.

## Rincian Eksperimen
Scene berantakan sintetis dan robot nyata (bin-picking) dengan metrik success rate dan clearance rate.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Sintetis clutter | precision | grasp berkualitas tinggi |
| Robot nyata | success rate | tinggi pada bin-picking |
| Generalisasi | - | sintetis ke nyata efektif |

## Temuan Kunci
- Menautkan grasp ke titik kontak menyederhanakan masalah.
- Data sintetis cukup untuk generalisasi.
- Efektif di scene berantakan.

## Keunggulan
- Grasp 6-DoF efisien.
- Robust di clutter.
- Generalisasi baik.

## Keterbatasan
- Bergantung kualitas point cloud/depth.
- Objek transparan/mengkilap sulit.
- Perlu penyaringan tabrakan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Langsung relevan untuk manipulasi robotik RGB-D (bin-picking), inti aplikasi YOLO+RGB-D + grasp.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Grasp Robotik** yang baik dibaca berdampingan:

- [184 - 2020 - VGN - Grasp Robotik](./184%20-%202020%20-%20VGN%20-%20Grasp%20Robotik.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Grasp Robotik** dalam peta tinjauan (17 klaster, 191 entri total).
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
Contact-GraspNet menyederhanakan grasp 6-DoF via titik kontak, memberi generasi grasp efisien dan andal untuk scene berantakan.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `sundermeyer2021contactgraspnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 183/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
