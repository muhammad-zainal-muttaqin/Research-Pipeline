# 103 - Guided Attentive Feature Fusion for Multispectral Pedestrian Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 103 dari 154 |
| Kunci BibTeX | `zhang2021gaff` |
| Judul | Guided Attentive Feature Fusion for Multispectral Pedestrian Detection |
| Penulis | Zhang, Heng; Fromont, Elisa; Lefevre, S{\'e |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) |
| Tema klaster | Pedestrian RGB-T |
| Kata kunci | RGB-T, guided attention, fusi, intra/inter-modal, pejalan |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-pedestrian-rgb-t)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Guided%20Attentive%20Feature%20Fusion%20for%20Multispectral%20Pedestrian%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Guided%20Attentive%20Feature%20Fusion%20for%20Multispectral%20Pedestrian%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 72--80 |

## Ringkasan Eksekutif
Detektor pejalan multispektral yang memakai guided attentive feature fusion untuk memandu fusi RGB-thermal via attention intra- dan inter-modal.

## Abstrak (Parafrase)
GAFF (Guided Attentive Feature Fusion) memakai attention intra-modal (menyoroti wilayah penting dalam tiap modal) dan inter-modal (memandu pertukaran antar-modal) untuk menggabungkan fitur RGB dan thermal secara selektif. Panduan attention ini menekan fitur tak relevan dan mencapai SOTA pada KAIST/CVC-14 saat rilis.

## Latar Belakang & Konteks
Fusi tanpa panduan menyertakan fitur tak relevan/berderau dari kedua modal, menurunkan deteksi.

## Permasalahan yang Diangkat
- Fusi tanpa panduan menyertakan fitur tak relevan.
- Wilayah penting per-modal perlu disoroti.
- Pertukaran antar-modal perlu dipandu.
- Derau modal menurunkan deteksi.
- Attention lintas-modal belum matang untuk RGB-T.

## Tujuan & Pertanyaan Penelitian
- Memandu fusi via attention intra-modal.
- Memandu pertukaran via attention inter-modal.
- Menekan fitur tak relevan.

## Tinjauan Terdahulu / Posisi Literatur
GAFF mengembangkan fusi terpandu attention untuk RGB-T.

Karya/konsep pembanding yang relevan:

- KAIST/CVC-14 — dataset RGB-T.
- Attention (intra/inter-modal).
- Guided fusion.
- Deteksi pejalan.

## Metodologi & Arsitektur
Intra-modality attention menyoroti wilayah penting dalam RGB dan thermal; inter-modality attention memandu pertukaran/penggabungan fitur antar-modal; guided fusion module menggabungkan fitur terpandu; deteksi pejalan dari fitur tergabung.

Komponen / langkah metodologis utama:

- Intra-modality attention (per-modal).
- Inter-modality attention (antar-modal).
- Guided feature fusion module.
- Penekanan fitur tak relevan.
- Deteksi pejalan.
- Evaluasi KAIST & CVC-14.

## Kontribusi Utama
1. Fusi terpandu attention (intra + inter).
2. Menekan fitur tak relevan.
3. SOTA KAIST/CVC-14 saat rilis.
4. Panduan attention efektif untuk RGB-T.

## Rincian Eksperimen
Diuji pada KAIST dan CVC-14 dengan metrik miss rate, dibandingkan metode fusi RGB-T lain.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| KAIST | miss rate | SOTA saat rilis |
| CVC-14 | miss rate | SOTA saat rilis |
| Ablation | intra/inter attention | keduanya menyumbang gain |

## Temuan Kunci
- Attention terpandu memperbaiki fusi RGB-T.
- Intra + inter attention saling melengkapi.
- Penekanan fitur tak relevan penting.
- Panduan meningkatkan deteksi.

## Keunggulan
- Fusi terpandu attention.
- Menekan derau.
- SOTA.

## Keterbatasan
- Attention menambah komputasi.
- Bergantung kualitas kedua modal.
- Fokus domain pejalan.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
GAFF menegaskan attention terpandu untuk fusi lintas-modal — mekanisme yang berulang di fusi RGB+Depth (bandingkan attention lintas-modal SOD) dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pedestrian RGB-T** yang baik dibaca berdampingan:

- [100 - 2015 - KAIST Multispectral Pedestrian - Pedestrian RGB-T](./100%20-%202015%20-%20KAIST%20Multispectral%20Pedestrian%20-%20Pedestrian%20RGB-T.md)
- [101 - 2019 - IAF R-CNN (Illumination-Aware) - Pedestrian RGB-T](./101%20-%202019%20-%20IAF%20R-CNN%20%28Illumination-Aware%29%20-%20Pedestrian%20RGB-T.md)
- [102 - 2020 - MBNet - Pedestrian RGB-T](./102%20-%202020%20-%20MBNet%20-%20Pedestrian%20RGB-T.md)
- [104 - 2020 - Cyclic Fuse-and-Refine (CFR) - Pedestrian RGB-T](./104%20-%202020%20-%20Cyclic%20Fuse-and-Refine%20%28CFR%29%20-%20Pedestrian%20RGB-T.md)
- [105 - 2022 - CMPD (Uncertainty-Guided Cross-Modal) - Pedestrian RGB-T](./105%20-%202022%20-%20CMPD%20%28Uncertainty-Guided%20Cross-Modal%29%20-%20Pedestrian%20RGB-T.md)
- [106 - 2021 - RGB-D Fusion for Detection (Farahnakian & Heikkonen) - Pedestrian RGB-T](./106%20-%202021%20-%20RGB-D%20Fusion%20for%20Detection%20%28Farahnakian%20%26%20Heikkonen%29%20-%20Pedestrian%20RGB-T.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Pedestrian RGB-T** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Pedestrian RGB-T)
Istilah penting untuk memahami makalah ini:

- **Multispektral** — Citra beberapa pita (RGB + thermal).
- **RGB-T** — Pasangan citra warna dan termal.
- **Thermal/LWIR** — Inframerah panjang; andal saat gelap.
- **Illumination-aware** — Bobot modal menyesuaikan kondisi cahaya.
- **Modality imbalance** — Ketimpangan keandalan antar-modal.
- **Miss rate (MR)** — Metrik deteksi pejalan (makin kecil makin baik).
- **KAIST** — Dataset pejalan multispektral standar.
- **CVC-14** — Dataset pejalan siang-malam RGB-thermal.
- **Feature alignment** — Penyelarasan spasial fitur antar-modal.
- **Cross-modal attention** — Attention pemandu fusi RGB-thermal.

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
GAFF memakai guided attentive feature fusion dengan attention intra- dan inter-modal untuk menggabungkan RGB dan thermal secara selektif, mencapai SOTA deteksi pejalan multispektral.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhang2021gaff` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 103/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
