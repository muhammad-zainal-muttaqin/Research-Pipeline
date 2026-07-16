# 110 - CFP-SLAM: A Real-Time Visual SLAM Based on Coarse-to-Fine Probability in Dynamic Environments

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 110 dari 154 |
| Kunci BibTeX | `hu2022cfpslam` |
| Judul | CFP-SLAM: A Real-Time Visual SLAM Based on Coarse-to-Fine Probability in Dynamic Environments |
| Penulis | Hu, Xinggang; Zhang, Yunzhou; Cao, Zhenzhong; Ma, Rong; Wu, Yanmin; Deng, Zhiqiang; Sun, Wenkai |
| Tahun | 2022 |
| Venue / Jurnal | Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) |
| Tema klaster | RGB-D SLAM |
| Kata kunci | RGB-D SLAM, dinamis, YOLO, probabilistik, real-time |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-rgb-d-slam)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=CFP-SLAM%3A%20A%20Real-Time%20Visual%20SLAM%20Based%20on%20Coarse-to-Fine%20Probability%20in%20Dynamic%20Environments
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=CFP-SLAM%3A%20A%20Real-Time%20Visual%20SLAM%20Based%20on%20Coarse-to-Fine%20Probability%20in%20Dynamic%20Environments&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 4399--4406 |

## Ringkasan Eksekutif
SLAM dinamis real-time yang memakai probabilitas coarse-to-fine (deteksi YOLO + geometri epipolar) untuk membobot titik dinamis secara probabilistik, bukan biner.

## Abstrak (Parafrase)
CFP-SLAM (Coarse-to-Fine Probability) memakai deteksi objek (YOLO) untuk prior kasar objek dinamis lalu model probabilistik coarse-to-fine (memanfaatkan geometri epipolar dan pengelompokan) untuk menetapkan probabilitas dinamis tiap titik. Titik diberi bobot dalam optimasi pose (bukan dibuang biner), sehingga fitur statis pada objek 'dinamis' tetap dimanfaatkan. Akurasi SOTA di antara SLAM dinamis, real-time.

## Latar Belakang & Konteks
Penghapusan biner objek dinamis (mis. seluruh area orang) membuang fitur statis berguna dan bergantung akurasi deteksi; pendekatan probabilistik lebih halus.

## Permasalahan yang Diangkat
- Penghapusan biner membuang fitur statis berguna.
- Bergantung akurasi deteksi (kotak kasar).
- Objek 'dinamis' bisa diam sebagian.
- Real-time perlu dijaga.
- Probabilitas dinamis belum dimanfaatkan penuh.

## Tujuan & Pertanyaan Penelitian
- Menetapkan probabilitas dinamis tiap titik.
- Membobot titik dalam optimasi (bukan biner).
- Menjaga real-time dan akurasi tinggi.

## Tinjauan Terdahulu / Posisi Literatur
CFP-SLAM menyempurnakan DynaSLAM/DS-SLAM dengan bobot probabilistik.

Karya/konsep pembanding yang relevan:

- ORB-SLAM2 — basis SLAM.
- YOLO — deteksi objek (prior kasar).
- Epipolar geometry — verifikasi gerak.
- Probabilistic weighting (coarse-to-fine).

## Metodologi & Arsitektur
YOLO memberi prior kasar objek dinamis; model coarse-to-fine memakai geometri epipolar dan pengelompokan untuk menghitung probabilitas dinamis tiap titik; probabilitas dipakai membobot titik dalam optimasi pose (weighted); berbasis ORB-SLAM2, real-time.

Komponen / langkah metodologis utama:

- Deteksi objek (YOLO) sebagai prior kasar.
- Probabilitas dinamis coarse-to-fine.
- Geometri epipolar untuk verifikasi.
- Pembobotan titik dalam optimasi pose.
- Real-time (deteksi cepat).
- Evaluasi TUM RGB-D dinamis.

## Kontribusi Utama
1. Penanganan dinamika probabilistik (bukan biner).
2. Memanfaatkan YOLO untuk prior cepat.
3. Menjaga fitur statis berguna.
4. SOTA SLAM dinamis, real-time.

## Rincian Eksperimen
Diuji pada TUM RGB-D dinamis dengan metrik ATE/RPE dan kecepatan, dibandingkan DynaSLAM/DS-SLAM.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| TUM RGB-D dinamis | ATE | SOTA di antara SLAM dinamis |
| Kecepatan | real-time | lebih cepat (YOLO) |
| Ablation | probabilistik | bobot > penghapusan biner |

## Temuan Kunci
- Bobot probabilistik unggul atas penghapusan biner.
- YOLO memberi prior cepat untuk real-time.
- Fitur statis dipertahankan.
- Geometri + deteksi saling melengkapi.

## Keunggulan
- Probabilistik & real-time.
- SOTA dinamis.
- Memakai YOLO.

## Keterbatasan
- Bergantung kualitas deteksi/geometri.
- Model probabilistik lebih kompleks.
- Fokus lingkungan indoor dinamis.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
CFP-SLAM menunjukkan integrasi YOLO ke SLAM dengan penanganan probabilistik — contoh langsung YOLO+RGB-D untuk SLAM dinamis dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SLAM** yang baik dibaca berdampingan:

- [107 - 2017 - ORB-SLAM2 - RGB-D SLAM](./107%20-%202017%20-%20ORB-SLAM2%20-%20RGB-D%20SLAM.md)
- [108 - 2018 - DynaSLAM - RGB-D SLAM](./108%20-%202018%20-%20DynaSLAM%20-%20RGB-D%20SLAM.md)
- [109 - 2018 - DS-SLAM - RGB-D SLAM](./109%20-%202018%20-%20DS-SLAM%20-%20RGB-D%20SLAM.md)
- [111 - 2019 - Visual SLAM YOLO vs Mask R-CNN (Soares dkk.) - RGB-D SLAM](./111%20-%202019%20-%20Visual%20SLAM%20YOLO%20vs%20Mask%20R-CNN%20%28Soares%20dkk.%29%20-%20RGB-D%20SLAM.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SLAM** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema RGB-D SLAM)
Istilah penting untuk memahami makalah ini:

- **SLAM** — Simultaneous Localization and Mapping.
- **RGB-D SLAM** — SLAM kamera warna+kedalaman (skala metrik).
- **Lingkungan dinamis** — Scene dengan objek bergerak.
- **Loop closure** — Pengenalan tempat untuk koreksi drift.
- **Bundle adjustment** — Optimasi bersama pose dan titik peta.
- **ATE/RPE** — Absolute/Relative Trajectory/Pose Error.
- **Semantic SLAM** — SLAM memanfaatkan label semantik.
- **Fitur ORB** — Fitur cepat rotasi-invarian.
- **TUM RGB-D** — Benchmark SLAM RGB-D standar.
- **Deteksi objek dinamis** — Menandai objek bergerak (YOLO/Mask R-CNN).

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
CFP-SLAM memakai deteksi YOLO dan probabilitas coarse-to-fine untuk membobot titik dinamis secara probabilistik, mencapai SLAM dinamis real-time SOTA yang menjaga fitur statis berguna.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `hu2022cfpslam` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 110/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
