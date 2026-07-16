# 143 - ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 143 dari 154 |
| Kunci BibTeX | `dai2017scannet` |
| Judul | ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes |
| Penulis | Dai, Angela; Chang, Angel X.; Savva, Manolis; Halber, Maciej; Funkhouser, Thomas; Nie{\ss |
| Tahun | 2017 |
| Venue / Jurnal | Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | Dataset |
| Kata kunci | dataset, 3D indoor, rekonstruksi, segmentasi 3D, RGB-D |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-dataset)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=ScanNet%3A%20Richly-Annotated%203D%20Reconstructions%20of%20Indoor%20Scenes
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=ScanNet%3A%20Richly-Annotated%203D%20Reconstructions%20of%20Indoor%20Scenes&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 5828--5839 |

## Ringkasan Eksekutif
Dataset rekonstruksi 3D indoor beranotasi kaya (2.5 juta view RGB-D dari 1500+ scan) dengan label semantik 3D.

## Abstrak (Parafrase)
ScanNet (Dai dkk.) menyediakan 1513 scan indoor (2.5 juta view RGB-D) dengan rekonstruksi mesh 3D dan anotasi instance/semantik 3D. Pipeline akuisisi dan anotasi berskala membuatnya benchmark kunci untuk segmentasi 3D, deteksi, dan rekonstruksi indoor.

## Latar Belakang & Konteks
Pembelajaran 3D indoor (segmentasi/deteksi 3D) membutuhkan data 3D beranotasi berskala yang sebelumnya sulit diperoleh.

## Permasalahan yang Diangkat
- Pembelajaran 3D indoor butuh data 3D berskala.
- Anotasi 3D (mesh/instance) mahal.
- Akuisisi 3D indoor sulit diskalakan.
- Benchmark 3D indoor kurang.
- Segmentasi/deteksi 3D menuntut label kaya.

## Tujuan & Pertanyaan Penelitian
- Menyediakan scan RGB-D indoor berskala.
- Merekonstruksi mesh 3D + anotasi semantik.
- Menyediakan benchmark 3D indoor.

## Tinjauan Terdahulu / Posisi Literatur
ScanNet menyediakan pipeline akuisisi + anotasi 3D masif.

Karya/konsep pembanding yang relevan:

- RGB-D scanning — akuisisi.
- Rekonstruksi mesh 3D.
- Anotasi instance/semantik 3D.
- Benchmark segmentasi/deteksi 3D.

## Metodologi & Arsitektur
1513 scan indoor direkam (2.5M view RGB-D); rekonstruksi mesh 3D dihasilkan; anotasi instance dan semantik 3D dilakukan lewat crowdsourcing; menyediakan tugas segmentasi 3D, deteksi, dan rekonstruksi.

Komponen / langkah metodologis utama:

- 1513 scan, 2.5M view RGB-D.
- Rekonstruksi mesh 3D.
- Anotasi instance/semantik 3D.
- Pipeline akuisisi+anotasi berskala.
- Tugas segmentasi/deteksi/rekonstruksi 3D.
- Lingkungan indoor.

## Kontribusi Utama
1. Dataset 3D indoor beranotasi berskala.
2. Rekonstruksi mesh + label semantik 3D.
3. Pipeline akuisisi/anotasi masif.
4. Benchmark kunci pembelajaran 3D indoor.

## Rincian Eksperimen
Menyediakan benchmark ScanNet untuk segmentasi 3D (mIoU), deteksi 3D, dan rekonstruksi.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| ScanNet segmentasi 3D | mIoU | benchmark standar 3D indoor |
| Deteksi 3D | mAP | benchmark deteksi indoor |
| Skala | view/scan | 2.5M view / 1513 scan |

## Temuan Kunci
- Data 3D berskala memungkinkan deep learning 3D.
- Rekonstruksi + label semantik penting.
- Crowdsourcing mempercepat anotasi.
- Benchmark memacu riset 3D indoor.

## Keunggulan
- Benchmark 3D indoor berpengaruh.
- Berskala & kaya.
- Rekonstruksi + anotasi.

## Keterbatasan
- Akuisisi/anotasi mahal.
- Domain indoor saja.
- Kualitas scan bervariasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
ScanNet adalah dataset 3D indoor berpengaruh untuk deep learning 3D (segmentasi/deteksi) yang relevan bagi pemahaman scene RGB-D dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Dataset** yang baik dibaca berdampingan:

- [141 - 2012 - NYU Depth v2 - Dataset](./141%20-%202012%20-%20NYU%20Depth%20v2%20-%20Dataset.md)
- [142 - 2015 - SUN RGB-D - Dataset](./142%20-%202015%20-%20SUN%20RGB-D%20-%20Dataset.md)
- [144 - 2012 - KITTI - Dataset](./144%20-%202012%20-%20KITTI%20-%20Dataset.md)
- [145 - 2020 - nuScenes - Dataset](./145%20-%202020%20-%20nuScenes%20-%20Dataset.md)
- [146 - 2014 - Microsoft COCO - Dataset](./146%20-%202014%20-%20Microsoft%20COCO%20-%20Dataset.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Dataset** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Dataset)
Istilah penting untuk memahami makalah ini:

- **Benchmark** — Dataset+metrik standar untuk evaluasi adil.
- **Anotasi** — Label ground-truth (box, mask, pose, depth).
- **RGB-D** — Data warna berpasangan kedalaman.
- **Split train/val/test** — Pembagian data pelatihan/evaluasi.
- **Metrik** — Ukuran kinerja (mAP, mIoU, AbsRel).
- **Sensor** — Perangkat akuisisi (Kinect, LiDAR, stereo).
- **Skala** — Jumlah citra/instance.
- **Kelas/kategori** — Jenis objek yang dilabeli.
- **Kalibrasi** — Parameter intrinsik/ekstrinsik sensor.
- **Generalisasi** — Kemampuan lintas domain.

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
ScanNet menyediakan 1513 scan RGB-D indoor (2.5M view) dengan rekonstruksi mesh dan anotasi semantik 3D, menjadi benchmark kunci untuk segmentasi, deteksi, dan rekonstruksi 3D indoor.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `dai2017scannet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 143/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
