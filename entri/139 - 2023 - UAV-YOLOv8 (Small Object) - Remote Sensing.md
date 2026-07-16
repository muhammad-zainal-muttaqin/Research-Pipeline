# 139 - UAV-YOLOv8: A Small-Object-Detection Model Based on Improved YOLOv8 for UAV Aerial Photography Scenarios

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 139 dari 154 |
| Kunci BibTeX | `wang2023uavyolo` |
| Judul | UAV-YOLOv8: A Small-Object-Detection Model Based on Improved YOLOv8 for UAV Aerial Photography Scenarios |
| Penulis | Wang, Gang; Chen, Yanfei; An, Pei; Hong, Hanyu; Hu, Jinghu; Huang, Tiange |
| Tahun | 2023 |
| Venue / Jurnal | Sensors |
| Tema klaster | Remote Sensing |
| Kata kunci | remote sensing, UAV, YOLOv8, objek kecil, Sensors |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=UAV-YOLOv8%3A%20A%20Small-Object-Detection%20Model%20Based%20on%20Improved%20YOLOv8%20for%20UAV%20Aerial%20Photography%20Scenarios
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=UAV-YOLOv8%3A%20A%20Small-Object-Detection%20Model%20Based%20on%20Improved%20YOLOv8%20for%20UAV%20Aerial%20Photography%20Scenarios&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 23 |
| Nomor | 16 |
| Halaman | 7190 |

## Ringkasan Eksekutif
Modifikasi YOLOv8 untuk deteksi objek kecil pada skenario fotografi udara UAV.

## Abstrak (Parafrase)
Wang dkk. mengembangkan UAV-YOLOv8, memodifikasi YOLOv8 dengan mekanisme atensi dan penyempurnaan fitur serta optimasi head skala kecil untuk mendeteksi objek kecil pada citra fotografi udara UAV. Model meningkatkan mAP objek kecil atas baseline pada dataset UAV (mis. VisDrone).

## Latar Belakang & Konteks
Objek kecil pada citra UAV mudah terlewat oleh detektor umum karena resolusi efektif rendah dan latar padat.

## Permasalahan yang Diangkat
- Objek kecil UAV mudah terlewat.
- Resolusi efektif rendah untuk objek kecil.
- Latar udara padat/kompleks.
- YOLOv8 baseline dapat ditingkatkan.
- Skala kecil menuntut head khusus.

## Tujuan & Pertanyaan Penelitian
- Menambahkan atensi/penyempurnaan fitur.
- Mengoptimalkan head skala kecil.
- Meningkatkan mAP objek kecil UAV.

## Tinjauan Terdahulu / Posisi Literatur
Makalah menyempurnakan YOLOv8 untuk objek kecil UAV.

Karya/konsep pembanding yang relevan:

- YOLOv8 — detektor dasar.
- Attention/feature refinement.
- Head skala kecil.
- Dataset UAV (VisDrone).

## Metodologi & Arsitektur
UAV-YOLOv8 menambahkan mekanisme atensi dan penyempurnaan fitur pada YOLOv8, dengan head skala kecil untuk objek kecil; dilatih pada dataset UAV; dievaluasi terhadap baseline untuk mAP objek kecil.

Komponen / langkah metodologis utama:

- Mekanisme atensi/penyempurnaan fitur.
- Optimasi head skala kecil.
- Basis YOLOv8.
- Pelatihan dataset UAV.
- Fokus objek kecil.
- Perbandingan dengan baseline.

## Kontribusi Utama
1. Adaptasi YOLOv8 untuk objek kecil UAV.
2. Peningkatan mAP objek kecil.
3. Contoh YOLOv8 mutakhir untuk UAV.
4. Optimasi skala kecil.

## Rincian Eksperimen
Diuji pada dataset UAV (mis. VisDrone) dengan metrik deteksi objek kecil (Sensors 2023).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| UAV (VisDrone) | mAP | peningkatan objek kecil |
| Objek kecil | AP-S | ditingkatkan |
| vs YOLOv8 | perbandingan | modifikasi menyumbang gain |

## Temuan Kunci
- Atensi/penyempurnaan meningkatkan objek kecil.
- Head skala kecil penting untuk UAV.
- Adaptasi domain bermanfaat.
- YOLOv8 dapat dioptimalkan untuk UAV.

## Keunggulan
- Objek kecil.
- YOLOv8 mutakhir.
- Peningkatan mAP.

## Keterbatasan
- Fokus domain UAV.
- RGB saja.
- Peningkatan inkremental.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini melengkapi klaster Remote Sensing tinjauan dengan adaptasi YOLOv8 untuk objek kecil UAV.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Remote Sensing** yang baik dibaca berdampingan:

- [137 - 2021 - TPH-YOLOv5 (Drone Detection) - Remote Sensing](./137%20-%202021%20-%20TPH-YOLOv5%20%28Drone%20Detection%29%20-%20Remote%20Sensing.md)
- [138 - 2019 - Robust CNN High-Res Remote Sensing (Zhang dkk.) - Remote Sensing](./138%20-%202019%20-%20Robust%20CNN%20High-Res%20Remote%20Sensing%20%28Zhang%20dkk.%29%20-%20Remote%20Sensing.md)
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
UAV-YOLOv8 memodifikasi YOLOv8 dengan atensi/penyempurnaan fitur dan head skala kecil untuk deteksi objek kecil pada fotografi udara UAV, meningkatkan mAP atas baseline.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `wang2023uavyolo` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 139/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
