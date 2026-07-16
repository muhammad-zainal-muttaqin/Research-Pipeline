# 085 - Bilateral Cross-Modal Fusion Network for Robot Grasp Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 085 dari 154 |
| Kunci BibTeX | `zhang2023bcmfnet` |
| Judul | Bilateral Cross-Modal Fusion Network for Robot Grasp Detection |
| Penulis | Zhang, Qiang; Sun, Xueying |
| Tahun | 2023 |
| Venue / Jurnal | Sensors |
| Tema klaster | Grasp Robotik |
| Kata kunci | grasp, bilateral fusion, cross-modal, RGB-D, Cornell/Jacquard |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Bilateral%20Cross-Modal%20Fusion%20Network%20for%20Robot%20Grasp%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Bilateral%20Cross-Modal%20Fusion%20Network%20for%20Robot%20Grasp%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 23 |
| Nomor | 6 |
| Halaman | 3340 |

## Ringkasan Eksekutif
Jaringan deteksi grasp yang memakai fusi lintas-modal bilateral untuk menggabungkan fitur RGB dan kedalaman secara dua-arah.

## Abstrak (Parafrase)
BCMFNet (Bilateral Cross-Modal Fusion Network) menggabungkan fitur RGB dan kedalaman melalui modul fusi lintas-modal bilateral (dua-arah), sehingga kedua modal saling memandu, lalu memprediksi grasp. Fusi bilateral melampaui fusi searah/dangkal dan mencapai akurasi kompetitif/SOTA pada Cornell/Jacquard.

## Latar Belakang & Konteks
Fusi RGB-D untuk grasp sering searah atau dangkal, membatasi pemanfaatan komplementaritas warna (tekstur) dan kedalaman (geometri).

## Permasalahan yang Diangkat
- Fusi RGB-D untuk grasp sering searah/dangkal.
- Komplementaritas warna-geometri kurang dimanfaatkan.
- Aliran informasi lintas-modal terbatas.
- Akurasi grasp perlu ditingkatkan.
- Fusi statis kurang adaptif.

## Tujuan & Pertanyaan Penelitian
- Menggabungkan RGB & kedalaman secara bilateral.
- Membuat kedua modal saling memandu.
- Meningkatkan akurasi deteksi grasp.

## Tinjauan Terdahulu / Posisi Literatur
BCMFNet mengembangkan fusi lintas-modal dua-arah untuk grasp.

Karya/konsep pembanding yang relevan:

- GR-ConvNet — grasp RGB-D (pembanding).
- Bilateral/bidirectional fusion.
- Cross-modal interaction.
- Cornell/Jacquard dataset.

## Metodologi & Arsitektur
Cabang RGB dan cabang kedalaman mengekstrak fitur; bilateral cross-modal fusion module mempertukarkan informasi dua-arah antar-modal di beberapa level; fitur tergabung memprediksi peta grasp (quality/angle/width).

Komponen / langkah metodologis utama:

- Cabang RGB & cabang kedalaman.
- Bilateral cross-modal fusion module (dua-arah).
- Pertukaran informasi antar-modal multi-level.
- Prediksi peta grasp dari fitur tergabung.
- Input RGB-D.
- Evaluasi Cornell/Jacquard.

## Kontribusi Utama
1. Fusi lintas-modal bilateral untuk grasp.
2. Kedua modal saling memandu.
3. Akurasi kompetitif/SOTA.
4. Memanfaatkan komplementaritas RGB-D.

## Rincian Eksperimen
Diuji pada Cornell dan Jacquard dengan metrik akurasi grasp, plus ablation fusi bilateral.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Cornell | akurasi grasp | kompetitif/SOTA |
| Jacquard | akurasi grasp | kompetitif/SOTA |
| Ablation | bilateral fusion | fusi dua-arah menyumbang gain |

## Temuan Kunci
- Fusi bilateral mengungguli fusi searah.
- Komplementaritas RGB-D dimanfaatkan.
- Aliran informasi dua-arah bermanfaat.
- Akurasi grasp meningkat.

## Keunggulan
- Fusi bilateral efektif.
- Memanfaatkan komplementaritas.
- Akurasi tinggi.

## Keterbatasan
- Grasp planar (bukan 6-DoF penuh).
- Bergantung kualitas RGB-D.
- Fusi dua-arah menambah komputasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
BCMFNet menegaskan fusi RGB-D bilateral bermanfaat untuk grasp — sejalan dengan tema fusi dua-arah (FFB6D) dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Grasp Robotik** yang baik dibaca berdampingan:

- [080 - 2015 - Deep Learning Robotic Grasps (Lenz dkk.) - Grasp Robotik](./080%20-%202015%20-%20Deep%20Learning%20Robotic%20Grasps%20%28Lenz%20dkk.%29%20-%20Grasp%20Robotik.md)
- [081 - 2018 - GG-CNN - Grasp Robotik](./081%20-%202018%20-%20GG-CNN%20-%20Grasp%20Robotik.md)
- [082 - 2020 - GR-ConvNet - Grasp Robotik](./082%20-%202020%20-%20GR-ConvNet%20-%20Grasp%20Robotik.md)
- [083 - 2022 - GR-ConvNet v2 - Grasp Robotik](./083%20-%202022%20-%20GR-ConvNet%20v2%20-%20Grasp%20Robotik.md)
- [084 - 2020 - GraspNet-1Billion - Grasp Robotik](./084%20-%202020%20-%20GraspNet-1Billion%20-%20Grasp%20Robotik.md)
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
BCMFNet memakai fusi lintas-modal bilateral yang membuat RGB dan kedalaman saling memandu untuk deteksi grasp, mencapai akurasi kompetitif/SOTA pada Cornell/Jacquard.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhang2023bcmfnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 085/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
