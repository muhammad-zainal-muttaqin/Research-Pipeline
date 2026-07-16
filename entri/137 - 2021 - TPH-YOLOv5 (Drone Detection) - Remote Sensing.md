# 137 - TPH-YOLOv5: Improved YOLOv5 Based on Transformer Prediction Head for Object Detection on Drone-Captured Scenarios

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 137 dari 154 |
| Kunci BibTeX | `zhu2021tphyolov5` |
| Judul | TPH-YOLOv5: Improved YOLOv5 Based on Transformer Prediction Head for Object Detection on Drone-Captured Scenarios |
| Penulis | Zhu, Xingkui; Lyu, Shuchang; Wang, Xu; Zhao, Qi |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops (ICCVW) |
| Tema klaster | Remote Sensing |
| Kata kunci | remote sensing, UAV, YOLOv5, Transformer head, objek kecil |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-remote-sensing)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=TPH-YOLOv5%3A%20Improved%20YOLOv5%20Based%20on%20Transformer%20Prediction%20Head%20for%20Object%20Detection%20on%20Drone-Captured%20Scenarios
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=TPH-YOLOv5%3A%20Improved%20YOLOv5%20Based%20on%20Transformer%20Prediction%20Head%20for%20Object%20Detection%20on%20Drone-Captured%20Scenarios&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 2778--2788 |

## Ringkasan Eksekutif
YOLOv5 yang menambahkan Transformer Prediction Head dan CBAM untuk deteksi objek pada citra drone yang padat objek kecil.

## Abstrak (Parafrase)
Zhu dkk. mengembangkan TPH-YOLOv5: YOLOv5 dengan Transformer Prediction Head (TPH) dan modul CBAM serta head skala tambahan untuk menangani objek sangat kecil dan skala bervariasi ekstrem pada citra drone (VisDrone). Model mencapai SOTA/juara kompetisi saat rilis untuk deteksi objek UAV.

## Latar Belakang & Konteks
Citra drone penuh objek sangat kecil dengan skala bervariasi ekstrem dan latar kompleks, menyulitkan detektor umum.

## Permasalahan yang Diangkat
- Citra drone penuh objek sangat kecil.
- Skala objek bervariasi ekstrem.
- Latar kompleks & padat.
- Detektor umum lemah untuk UAV.
- Konteks global diperlukan.

## Tujuan & Pertanyaan Penelitian
- Menambahkan Transformer Prediction Head.
- Menambahkan CBAM & head skala kecil.
- Meningkatkan deteksi objek kecil UAV.

## Tinjauan Terdahulu / Posisi Literatur
TPH-YOLOv5 menggabungkan Transformer head dan attention pada YOLOv5.

Karya/konsep pembanding yang relevan:

- YOLOv5 — detektor dasar.
- Transformer Prediction Head (TPH).
- CBAM — attention.
- VisDrone — dataset UAV.

## Metodologi & Arsitektur
TPH mengganti head prediksi dengan Transformer untuk konteks global; CBAM menambah attention kanal-spasial; head skala tambahan menangkap objek sangat kecil; dilatih pada VisDrone; dievaluasi untuk deteksi objek UAV.

Komponen / langkah metodologis utama:

- Transformer Prediction Head (konteks global).
- CBAM attention (kanal-spasial).
- Head skala tambahan (objek kecil).
- Basis YOLOv5.
- Pelatihan VisDrone.
- Evaluasi deteksi UAV.

## Kontribusi Utama
1. Transformer head efektif untuk objek kecil UAV.
2. CBAM + head skala tambahan meningkatkan deteksi.
3. SOTA/juara kompetisi saat rilis.
4. Contoh integrasi Transformer ke YOLO.

## Rincian Eksperimen
Diuji pada VisDrone dengan metrik deteksi (mAP), memenangi/juara kompetisi drone (ICCVW 2021).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| VisDrone | mAP | SOTA/juara saat rilis |
| Objek kecil | AP-S | ditingkatkan signifikan |
| Ablation | TPH/CBAM | keduanya menyumbang gain |

## Temuan Kunci
- Transformer head menangkap konteks untuk objek kecil.
- Attention memperkuat fitur.
- Head skala tambahan penting untuk UAV.
- Integrasi Transformer ke YOLO bermanfaat.

## Keunggulan
- SOTA UAV saat rilis.
- Transformer head.
- Objek kecil.

## Keterbatasan
- Transformer head menambah komputasi.
- Fokus domain UAV.
- RGB saja.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini menegaskan integrasi Transformer/attention pada YOLO untuk objek kecil dalam klaster Remote Sensing tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Remote Sensing** yang baik dibaca berdampingan:

- [138 - 2019 - Robust CNN High-Res Remote Sensing (Zhang dkk.) - Remote Sensing](./138%20-%202019%20-%20Robust%20CNN%20High-Res%20Remote%20Sensing%20%28Zhang%20dkk.%29%20-%20Remote%20Sensing.md)
- [139 - 2023 - UAV-YOLOv8 (Small Object) - Remote Sensing](./139%20-%202023%20-%20UAV-YOLOv8%20%28Small%20Object%29%20-%20Remote%20Sensing.md)
- [140 - 2018 - YOLT (Satellite Imagery) - Remote Sensing](./140%20-%202018%20-%20YOLT%20%28Satellite%20Imagery%29%20-%20Remote%20Sensing.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **Remote Sensing** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema Remote Sensing)
Istilah penting untuk memahami makalah ini:

- **Remote sensing** — Penginderaan jauh satelit/UAV.
- **UAV/drone** — Wahana udara citra resolusi tinggi.
- **Objek kecil** — Objek sangat kecil khas citra udara.
- **Tiling** — Pemecahan citra besar menjadi ubin.
- **Oriented bounding box** — Kotak beorientasi untuk objek berputar.
- **Transformer head** — Kepala prediksi attention untuk objek kecil.
- **VisDrone/DOTA** — Benchmark deteksi udara/remote sensing.
- **mAP** — Metrik deteksi remote sensing.
- **Skala bervariasi** — Rentang ukuran objek sangat lebar.
- **Latar kompleks** — Latar beragam dan padat.

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
TPH-YOLOv5 menambahkan Transformer Prediction Head dan CBAM ke YOLOv5 untuk deteksi objek pada citra drone padat objek kecil, mencapai SOTA/juara kompetisi UAV.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhu2021tphyolov5` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 137/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
