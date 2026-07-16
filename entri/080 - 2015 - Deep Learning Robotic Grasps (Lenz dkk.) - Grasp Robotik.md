# 080 - Deep Learning for Detecting Robotic Grasps

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 080 dari 154 |
| Kunci BibTeX | `lenz2015grasp` |
| Judul | Deep Learning for Detecting Robotic Grasps |
| Penulis | Lenz, Ian; Lee, Honglak; Saxena, Ashutosh |
| Tahun | 2015 |
| Venue / Jurnal | The International Journal of Robotics Research |
| Tema klaster | Grasp Robotik |
| Kata kunci | grasp, deep learning, RGB-D, Cornell dataset, dua-tahap |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Deep%20Learning%20for%20Detecting%20Robotic%20Grasps
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Deep%20Learning%20for%20Detecting%20Robotic%20Grasps&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 34 |
| Nomor | 4--5 |
| Halaman | 705--724 |

## Ringkasan Eksekutif
Karya pelopor deteksi grasp robotik dua-tahap dengan deep learning yang meranking kandidat kotak grasp dari citra RGB-D, memperkenalkan Cornell Grasp Dataset.

## Abstrak (Parafrase)
Lenz dkk. mempelopori deteksi grasp berbasis deep learning: sebuah kaskade dua jaringan pertama menyaring kandidat kotak grasp berorientasi lalu jaringan kedua mengevaluasi/meranking kualitasnya dari citra RGB-D. Representasi grasp sebagai oriented rectangle dan Cornell Grasp Dataset yang diperkenalkan menjadi standar awal bidang ini.

## Latar Belakang & Konteks
Perencanaan grasp analitik (berbasis model geometris) rapuh terhadap objek baru dan ketidakpastian sensor; dibutuhkan pendekatan pembelajaran dari data RGB-D.

## Permasalahan yang Diangkat
- Perencanaan grasp analitik rapuh terhadap objek baru.
- Ketidakpastian sensor menyulitkan grasp geometris.
- Representasi grasp perlu ringkas & dapat dipelajari.
- Dataset grasp berlabel masih kurang.
- Evaluasi grasp perlu standar.

## Tujuan & Pertanyaan Penelitian
- Mempelajari deteksi grasp dari RGB-D.
- Merepresentasikan grasp sebagai oriented rectangle.
- Menyediakan Cornell Grasp Dataset.

## Tinjauan Terdahulu / Posisi Literatur
Lenz dkk. pelopor grasp berbasis deep learning.

Karya/konsep pembanding yang relevan:

- Grasp analitik/geometris — pendahulu.
- Deep learning fitur — pendekatan baru.
- Oriented rectangle — representasi grasp.
- Cornell Grasp Dataset (diperkenalkan).

## Metodologi & Arsitektur
Kaskade dua jaringan: jaringan pertama (kecil) menyaring banyak kandidat kotak grasp berorientasi dengan cepat; jaringan kedua (lebih besar) mengevaluasi kandidat tersaring untuk memilih grasp terbaik; input fitur RGB-D; representasi grasp sebagai oriented rectangle.

Komponen / langkah metodologis utama:

- Kaskade dua jaringan (deteksi + evaluasi).
- Representasi grasp oriented rectangle.
- Input fitur RGB-D.
- Penyaringan cepat lalu evaluasi teliti.
- Pelatihan pada Cornell dataset.
- Evaluasi grasp berlabel.

## Kontribusi Utama
1. Pelopor deteksi grasp berbasis deep learning.
2. Representasi oriented rectangle yang ringkas.
3. Kaskade dua-tahap efisien.
4. Cornell Grasp Dataset sebagai standar awal.

## Rincian Eksperimen
Diuji pada Cornell Grasping Dataset dengan metrik akurasi deteksi grasp (rectangle metric), menetapkan baseline DL.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Cornell dataset | akurasi grasp | baseline DL grasp |
| Representasi | oriented rectangle | standar awal |
| Kaskade | efisiensi | penyaringan + evaluasi |

## Temuan Kunci
- Deep learning efektif untuk deteksi grasp.
- Oriented rectangle representasi grasp yang baik.
- Kaskade menyeimbangkan kecepatan-akurasi.
- RGB-D bermanfaat untuk grasp.

## Keunggulan
- Pelopor & berpengaruh.
- Representasi ringkas.
- Dataset standar.

## Keterbatasan
- Dataset kecil (Cornell) membatasi.
- Dua-tahap relatif lambat.
- Grasp 2D (bukan 6-DoF penuh).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Lenz dkk. meletakkan dasar deteksi grasp berbasis pembelajaran dari RGB-D — akar klaster Grasp Robotik dalam tinjauan yang menghubungkan deteksi dan manipulasi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Grasp Robotik** yang baik dibaca berdampingan:

- [081 - 2018 - GG-CNN - Grasp Robotik](./081%20-%202018%20-%20GG-CNN%20-%20Grasp%20Robotik.md)
- [082 - 2020 - GR-ConvNet - Grasp Robotik](./082%20-%202020%20-%20GR-ConvNet%20-%20Grasp%20Robotik.md)
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
Lenz dkk. mempelopori deteksi grasp robotik dua-tahap berbasis deep learning dari RGB-D dengan representasi oriented rectangle dan Cornell Grasp Dataset, meletakkan dasar bidang grasp pembelajaran.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `lenz2015grasp` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 080/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
