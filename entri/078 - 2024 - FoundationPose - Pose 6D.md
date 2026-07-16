# 078 - FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 078 dari 154 |
| Kunci BibTeX | `wen2024foundationpose` |
| Judul | FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects |
| Penulis | Wen, Bowen; Yang, Wei; Kautz, Jan; Birchfield, Stan |
| Tahun | 2024 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Pose 6D |
| Kata kunci | pose 6D, objek baru, foundation model, sintetis, zero-shot |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=FoundationPose%3A%20Unified%206D%20Pose%20Estimation%20and%20Tracking%20of%20Novel%20Objects
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=FoundationPose%3A%20Unified%206D%20Pose%20Estimation%20and%20Tracking%20of%20Novel%20Objects&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 17868--17879 |

## Ringkasan Eksekutif
Model fondasi yang menyatukan estimasi dan pelacakan pose 6D objek baru (model-based & model-free) via pelatihan sintetis skala besar, tanpa fine-tuning per-objek.

## Abstrak (Parafrase)
FoundationPose adalah model fondasi untuk pose 6D dan tracking objek novel yang bekerja dalam dua setup: model-based (punya CAD) dan model-free (hanya beberapa citra referensi), disatukan lewat neural implicit representation. Dilatih dengan sintesis data berskala besar (LLM-aided, kontras), ia melakukan generalisasi zero-shot ke objek baru tanpa pelatihan ulang, mengungguli metode instance-specific.

## Latar Belakang & Konteks
Metode pose 6D lama membutuhkan CAD dan/atau pelatihan per-objek, sehingga tidak general ke objek baru — penghambat utama penerapan luas.

## Permasalahan yang Diangkat
- Metode lama butuh CAD dan/atau latih per-objek.
- Tidak general ke objek baru (novel).
- Setup model-based & model-free terpisah.
- Data pose nyata terbatas.
- Generalisasi zero-shot diperlukan.

## Tujuan & Pertanyaan Penelitian
- Menyatukan pose model-based & model-free.
- Generalisasi zero-shot ke objek baru.
- Menghilangkan fine-tuning per-objek.

## Tinjauan Terdahulu / Posisi Literatur
FoundationPose menggabungkan neural implicit representation dan pelatihan sintetis masif.

Karya/konsep pembanding yang relevan:

- Metode pose instance-specific — pembanding.
- Neural implicit representation.
- Sintesis data berskala (LLM-aided).
- Contrastive learning.

## Metodologi & Arsitektur
Neural implicit representation menjembatani setup model-based/free; render-and-compare untuk hipotesis pose; jaringan refinement dan seleksi (scoring) memilih pose terbaik; dilatih pada data sintetis berskala besar dengan augmentasi/kontras; mendukung tracking temporal.

Komponen / langkah metodologis utama:

- Neural implicit object representation.
- Unifikasi model-based & model-free.
- Render-and-compare + pose refinement.
- Pose selection/scoring network.
- Pelatihan sintetis berskala (LLM-aided).
- Estimasi + tracking pose novel.

## Kontribusi Utama
1. Model fondasi pose 6D generalis (zero-shot).
2. Menyatukan setup model-based & model-free.
3. Sintesis data berskala + kontras.
4. Mengungguli metode instance-specific.

## Rincian Eksperimen
Diuji pada banyak benchmark pose (YCB-Video, LineMOD, dan objek novel) dengan metrik ADD/ADD-S, dibandingkan metode instance-specific.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| YCB-Video/LineMOD | ADD-S | SOTA |
| Objek novel | zero-shot | unggul tanpa latih ulang |
| Tracking | temporal | estimasi + pelacakan pose |

## Temuan Kunci
- Pose objek baru dapat diestimasi tanpa latih ulang.
- Unifikasi model-based/free layak.
- Sintesis data berskala kunci generalisasi.
- Lompatan menuju pose generalis.

## Keunggulan
- Generalis (zero-shot objek baru).
- Menyatukan dua setup.
- SOTA & tracking.

## Keterbatasan
- Pelatihan sintetis berskala mahal.
- Model-free butuh citra referensi.
- Komputasi render-and-compare tinggi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
FoundationPose mewakili arah mutakhir pose 6D generalis yang relevan bagi robotika/manipulasi RGB-D masa depan dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pose 6D** yang baik dibaca berdampingan:

- [073 - 2018 - PoseCNN - Pose 6D](./073%20-%202018%20-%20PoseCNN%20-%20Pose%206D.md)
- [074 - 2019 - DenseFusion - Pose 6D](./074%20-%202019%20-%20DenseFusion%20-%20Pose%206D.md)
- [075 - 2020 - PVN3D - Pose 6D](./075%20-%202020%20-%20PVN3D%20-%20Pose%206D.md)
- [076 - 2021 - FFB6D - Pose 6D](./076%20-%202021%20-%20FFB6D%20-%20Pose%206D.md)
- [077 - 2020 - G2L-Net - Pose 6D](./077%20-%202020%20-%20G2L-Net%20-%20Pose%206D.md)
- [079 - 2021 - Review Pose 6D & Deteksi 3D (Hoque dkk.) - Pose 6D](./079%20-%202021%20-%20Review%20Pose%206D%20%26%20Deteksi%203D%20%28Hoque%20dkk.%29%20-%20Pose%206D.md)

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
FoundationPose menyatukan estimasi dan tracking pose 6D objek baru (model-based & free) via neural implicit representation dan pelatihan sintetis masif, mencapai generalisasi zero-shot yang mengungguli metode instance-specific.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wen2024foundationpose` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 078/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
