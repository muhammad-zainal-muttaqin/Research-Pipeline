# 070 - MonoIndoor: Towards Good Practice of Self-Supervised Monocular Depth Estimation for Indoor Environments

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 070 dari 154 |
| Kunci BibTeX | `ji2021monoindoor` |
| Judul | MonoIndoor: Towards Good Practice of Self-Supervised Monocular Depth Estimation for Indoor Environments |
| Penulis | Ji, Pan; Li, Runze; Bhanu, Bir; Xu, Yi |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema klaster | Estimasi Kedalaman |
| Kata kunci | depth monokular, self-supervised, indoor, depth factorization, residual pose |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-estimasi-kedalaman)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=MonoIndoor%3A%20Towards%20Good%20Practice%20of%20Self-Supervised%20Monocular%20Depth%20Estimation%20for%20Indoor%20Environments
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=MonoIndoor%3A%20Towards%20Good%20Practice%20of%20Self-Supervised%20Monocular%20Depth%20Estimation%20for%20Indoor%20Environments&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 12787--12796 |

## Ringkasan Eksekutif
Metode depth swa-awas untuk lingkungan indoor yang mengatasi variasi rentang kedalaman dan gerak rotasi besar melalui faktorisasi kedalaman dan estimasi pose residual.

## Abstrak (Parafrase)
MonoIndoor menangani tantangan spesifik depth swa-awas indoor: rentang kedalaman sangat bervariasi antar-scene dan gerak kamera indoor sering melibatkan rotasi besar. Ia memakai depth factorization (memisahkan skala global dan depth relatif) dan residual pose estimation iteratif untuk memperbaiki estimasi pose. Hasilnya meningkatkan depth swa-awas pada dataset indoor.

## Latar Belakang & Konteks
Depth swa-awas yang sukses di outdoor (berkendara) gagal di indoor karena rentang kedalaman bervariasi dan rotasi kamera besar melanggar asumsi gerak halus.

## Permasalahan yang Diangkat
- Rentang kedalaman indoor sangat bervariasi antar-scene.
- Gerak kamera indoor sering rotasi besar.
- Asumsi gerak halus (outdoor) tak berlaku.
- Estimasi pose sulit pada rotasi besar.
- Depth swa-awas outdoor gagal di indoor.

## Tujuan & Pertanyaan Penelitian
- Memfaktorkan skala global dan depth relatif.
- Memperbaiki pose via estimasi residual iteratif.
- Meningkatkan depth swa-awas indoor.

## Tinjauan Terdahulu / Posisi Literatur
MonoIndoor mengadaptasi pipeline swa-awas ke domain indoor.

Karya/konsep pembanding yang relevan:

- Monodepth2 — swa-awas (pembanding outdoor).
- Depth factorization — pemisahan skala.
- Residual pose estimation.
- Dataset NYUv2/7-Scenes/EuRoC.

## Metodologi & Arsitektur
Depth factorization module memisahkan estimasi skala global (yang bervariasi antar-scene) dari depth relatif; residual pose estimation memperbaiki pose secara iteratif untuk menangani rotasi besar; pelatihan swa-awas photometric pada video indoor.

Komponen / langkah metodologis utama:

- Depth factorization (skala global + relatif).
- Residual pose estimation iteratif.
- Penanganan rotasi kamera besar.
- Photometric self-supervision (video indoor).
- Backbone encoder-decoder.
- Evaluasi NYUv2/7-Scenes/EuRoC.

## Kontribusi Utama
1. Faktorisasi kedalaman untuk variasi skala indoor.
2. Residual pose menangani rotasi besar.
3. Peningkatan depth swa-awas indoor.
4. Adaptasi swa-awas ke domain indoor.

## Rincian Eksperimen
Diuji pada dataset indoor (NYUv2, 7-Scenes, EuRoC) dengan metrik depth, dibandingkan metode swa-awas outdoor-oriented.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NYUv2 | AbsRel/RMSE | peningkatan depth swa-awas indoor |
| 7-Scenes/EuRoC | AbsRel | generalisasi indoor |
| Ablation | factorization/pose | keduanya menyumbang gain |

## Temuan Kunci
- Domain indoor menuntut penanganan skala & rotasi khusus.
- Depth factorization menangani variasi skala.
- Residual pose penting untuk rotasi besar.
- Swa-awas dapat diadaptasi ke indoor.

## Keunggulan
- Adaptasi indoor efektif.
- Menangani rotasi besar.
- Faktorisasi skala.

## Keterbatasan
- Fokus domain indoor.
- Skala metrik tetap menantang.
- Bergantung asumsi photometric.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
MonoIndoor relevan bagi tinjauan karena indoor adalah domain utama RGB-D (robot, SLAM); menyediakan depth swa-awas untuk pseudo-RGB-D indoor.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Estimasi Kedalaman** yang baik dibaca berdampingan:

- [062 - 2014 - Depth dari Citra Tunggal (Eigen dkk.) - Estimasi Kedalaman](./062%20-%202014%20-%20Depth%20dari%20Citra%20Tunggal%20%28Eigen%20dkk.%29%20-%20Estimasi%20Kedalaman.md)
- [063 - 2017 - Monodepth (Left-Right Consistency) - Estimasi Kedalaman](./063%20-%202017%20-%20Monodepth%20%28Left-Right%20Consistency%29%20-%20Estimasi%20Kedalaman.md)
- [064 - 2019 - Monodepth2 - Estimasi Kedalaman](./064%20-%202019%20-%20Monodepth2%20-%20Estimasi%20Kedalaman.md)
- [065 - 2019 - BTS (Local Planar Guidance) - Estimasi Kedalaman](./065%20-%202019%20-%20BTS%20%28Local%20Planar%20Guidance%29%20-%20Estimasi%20Kedalaman.md)
- [066 - 2021 - AdaBins - Estimasi Kedalaman](./066%20-%202021%20-%20AdaBins%20-%20Estimasi%20Kedalaman.md)
- [067 - 2021 - DPT (Dense Prediction Transformer) - Estimasi Kedalaman](./067%20-%202021%20-%20DPT%20%28Dense%20Prediction%20Transformer%29%20-%20Estimasi%20Kedalaman.md)
- [068 - 2022 - MiDaS (Robust Monocular Depth) - Estimasi Kedalaman](./068%20-%202022%20-%20MiDaS%20%28Robust%20Monocular%20Depth%29%20-%20Estimasi%20Kedalaman.md)
- [069 - 2020 - PackNet - Estimasi Kedalaman](./069%20-%202020%20-%20PackNet%20-%20Estimasi%20Kedalaman.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Estimasi Kedalaman** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Estimasi Kedalaman)
Istilah penting untuk memahami makalah ini:

- **Depth monokular** — Estimasi kedalaman dari satu citra RGB (ill-posed).
- **Supervised** — Dilatih dengan ground-truth depth.
- **Self-supervised** — Dilatih tanpa label depth via konsistensi stereo/video.
- **Disparitas** — Pergeseran piksel antar-pandangan stereo.
- **Skala metrik vs relatif** — Depth satuan nyata vs hanya urutan relatif.
- **AbsRel** — Absolute Relative error (makin kecil makin baik).
- **RMSE** — Root Mean Square Error peta depth.
- **delta<1.25** — Persentase piksel dengan error di bawah ambang.
- **Zero-shot** — Generalisasi ke dataset tak dilihat saat pelatihan.
- **Pseudo-depth** — Depth prediksi model, pengganti sensor depth.

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
MonoIndoor mengadaptasi depth swa-awas ke indoor dengan depth factorization dan residual pose estimation, mengatasi variasi rentang kedalaman dan rotasi besar khas lingkungan dalam ruangan.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `ji2021monoindoor` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 070/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
