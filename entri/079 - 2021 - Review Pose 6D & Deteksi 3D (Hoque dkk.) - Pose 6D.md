# 079 - A Comprehensive Review on 3D Object Detection and 6D Pose Estimation with Deep Learning

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 079 dari 154 |
| Kunci BibTeX | `hoque2021posesurvey` |
| Judul | A Comprehensive Review on 3D Object Detection and 6D Pose Estimation with Deep Learning |
| Penulis | Hoque, Sabera; Arafat, Md Yasin; Xu, Shuxiang; Maiti, Ananda; Wei, Yuchen |
| Tahun | 2021 |
| Venue / Jurnal | IEEE Access |
| Tema klaster | Pose 6D |
| Kata kunci | survei, pose 6D, deteksi 3D, deep learning, review |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-pose-6d)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=A%20Comprehensive%20Review%20on%203D%20Object%20Detection%20and%206D%20Pose%20Estimation%20with%20Deep%20Learning
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=A%20Comprehensive%20Review%20on%203D%20Object%20Detection%20and%206D%20Pose%20Estimation%20with%20Deep%20Learning&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 9 |
| Halaman | 143746--143770 |

## Ringkasan Eksekutif
Tinjauan komprehensif deteksi objek 3D dan estimasi pose 6D berbasis deep learning yang memetakan metode, dataset, dan metrik.

## Abstrak (Parafrase)
Makalah survei ini mengkaji secara menyeluruh deteksi objek 3D dan estimasi pose 6D dengan deep learning: taksonomi metode berbasis RGB, kedalaman, dan point cloud; ikhtisar dataset dan metrik (ADD, ADD-S, AP 3D); serta tantangan terbuka. Ia menyediakan peta bidang pose 6D dan deteksi 3D.

## Latar Belakang & Konteks
Bidang pose 6D dan deteksi 3D luas dengan beragam modalitas sensor dan pendekatan, sehingga dibutuhkan sintesis terstruktur.

## Permasalahan yang Diangkat
- Bidang pose 6D & deteksi 3D sangat luas.
- Beragam modalitas (RGB/depth/point cloud).
- Metode & metrik heterogen.
- Dataset tersebar.
- Perlu peta bidang koheren.

## Tujuan & Pertanyaan Penelitian
- Mengklasifikasikan metode pose 6D & deteksi 3D.
- Meninjau dataset dan metrik.
- Mengidentifikasi tantangan terbuka.

## Tinjauan Terdahulu / Posisi Literatur
Survei ini mengagregasi metode berbasis RGB, depth, dan point cloud.

Karya/konsep pembanding yang relevan:

- Metode pose 6D (PoseCNN/DenseFusion/PVN3D).
- Deteksi 3D (point cloud/fusi).
- Dataset (YCB/LineMOD/KITTI).
- Metrik (ADD/ADD-S/AP).

## Metodologi & Arsitektur
Metodologi survei: taksonomi metode berdasarkan modalitas/representasi, ikhtisar dataset & metrik, dan diskusi tantangan (oklusi, simetri, generalisasi).

Komponen / langkah metodologis utama:

- Taksonomi metode pose 6D & deteksi 3D.
- Klasifikasi berdasarkan modalitas/representasi.
- Ikhtisar dataset (YCB/LineMOD/KITTI).
- Ikhtisar metrik (ADD/ADD-S/AP 3D).
- Diskusi tantangan (oklusi/simetri).
- Sintesis literatur.

## Kontribusi Utama
1. Peta bidang pose 6D & deteksi 3D terstruktur.
2. Taksonomi metode yang jelas.
3. Ikhtisar dataset/metrik praktis.
4. Identifikasi tantangan terbuka.

## Rincian Eksperimen
Sebagai survei, evaluasi berupa kompilasi & analisis komparatif metode dari literatur.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Metode pose/3D | ADD/AP | kompilasi komparatif |
| Modalitas | taksonomi | RGB/depth/point cloud |
| Tantangan | peta | oklusi/simetri/generalisasi |

## Temuan Kunci
- Modalitas kedalaman/geometri krusial untuk pose/3D.
- Oklusi & simetri tantangan berulang.
- Fusi RGB-D dominan untuk pose presisi.
- Generalisasi objek baru arah penting.

## Keunggulan
- Peta bidang terstruktur.
- Taksonomi jelas.
- Rujukan pose 6D & 3D.

## Keterbatasan
- Bersifat survei.
- Cepat usang.
- Perbandingan antar-sumber tak setara.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Survei ini menaungi klaster Pose 6D dan Deteksi 3D dalam tinjauan, membantu memposisikan entri-entri terkait pemanfaatan kedalaman.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pose 6D** yang baik dibaca berdampingan:

- [073 - 2018 - PoseCNN - Pose 6D](./073%20-%202018%20-%20PoseCNN%20-%20Pose%206D.md)
- [074 - 2019 - DenseFusion - Pose 6D](./074%20-%202019%20-%20DenseFusion%20-%20Pose%206D.md)
- [075 - 2020 - PVN3D - Pose 6D](./075%20-%202020%20-%20PVN3D%20-%20Pose%206D.md)
- [076 - 2021 - FFB6D - Pose 6D](./076%20-%202021%20-%20FFB6D%20-%20Pose%206D.md)
- [077 - 2020 - G2L-Net - Pose 6D](./077%20-%202020%20-%20G2L-Net%20-%20Pose%206D.md)
- [078 - 2024 - FoundationPose - Pose 6D](./078%20-%202024%20-%20FoundationPose%20-%20Pose%206D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Pose 6D** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Pose 6D)
Istilah penting untuk memahami makalah ini:

- **Pose 6D** — Tiga translasi + tiga rotasi objek relatif kamera.
- **RGB-D** — Citra warna berpasangan peta kedalaman.
- **Point cloud** — Himpunan titik 3D dari depth/LiDAR.
- **Keypoint voting** — Titik memilih lokasi keypoint 3D untuk pose.
- **ADD/ADD-S** — Metrik pose: rata-rata jarak titik model (S=simetris).
- **Fusi dense** — Penggabungan fitur RGB dan geometri per-titik.
- **YCB-Video** — Dataset pose 6D scene berantakan.
- **LineMOD** — Dataset pose 6D objek tunggal klasik.
- **Refinement iteratif** — Penyempurnaan pose bertahap (ICP/jaringan).
- **Oklusi** — Objek terhalang sebagian.

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
Hoque dkk. meninjau deteksi 3D dan pose 6D berbasis deep learning secara komprehensif, memetakan metode lintas modalitas, dataset, metrik, dan tantangan sebagai peta bidang.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `hoque2021posesurvey` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 079/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
