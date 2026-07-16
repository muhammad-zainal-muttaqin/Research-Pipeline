# 138 - Hierarchical and Robust Convolutional Neural Network for Very High-Resolution Remote Sensing Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 138 dari 154 |
| Kunci BibTeX | `zhang2019remotesensing` |
| Judul | Hierarchical and Robust Convolutional Neural Network for Very High-Resolution Remote Sensing Object Detection |
| Penulis | Zhang, Yuanlin; Yuan, Yuan; Feng, Yachuang; Lu, Xiaoqiang |
| Tahun | 2019 |
| Venue / Jurnal | IEEE Transactions on Geoscience and Remote Sensing |
| Tema klaster | Remote Sensing |
| Kata kunci | remote sensing, VHR, CNN hierarkis, deteksi objek, TGRS |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Hierarchical%20and%20Robust%20Convolutional%20Neural%20Network%20for%20Very%20High-Resolution%20Remote%20Sensing%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Hierarchical%20and%20Robust%20Convolutional%20Neural%20Network%20for%20Very%20High-Resolution%20Remote%20Sensing%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Volume | 57 |
| Nomor | 8 |
| Halaman | 5535--5548 |

## Ringkasan Eksekutif
CNN hierarkis dan robust untuk deteksi objek pada citra remote sensing resolusi sangat tinggi.

## Abstrak (Parafrase)
Zhang dkk. mengusulkan CNN hierarkis yang robust untuk deteksi objek pada citra remote sensing beresolusi sangat tinggi (VHR). Arsitektur multi-skala menangani objek beragam skala/orientasi dan latar kompleks, mencapai akurasi tinggi pada dataset penginderaan jauh VHR.

## Latar Belakang & Konteks
Objek pada remote sensing VHR beragam skala dan orientasi dengan latar kompleks, menyulitkan detektor standar.

## Permasalahan yang Diangkat
- Objek VHR beragam skala & orientasi.
- Latar remote sensing kompleks.
- Detektor standar kurang robust.
- Resolusi sangat tinggi menantang.
- Fitur hierarkis diperlukan.

## Tujuan & Pertanyaan Penelitian
- Merancang CNN hierarkis multi-skala.
- Meningkatkan robustness terhadap variasi.
- Meningkatkan deteksi objek VHR.

## Tinjauan Terdahulu / Posisi Literatur
Makalah mengembangkan detektor khusus remote sensing.

Karya/konsep pembanding yang relevan:

- CNN deteksi objek — dasar.
- Arsitektur hierarkis multi-skala.
- Remote sensing VHR.
- Dataset penginderaan jauh.

## Metodologi & Arsitektur
Arsitektur CNN hierarkis mengekstrak fitur multi-skala yang robust terhadap variasi skala/orientasi; dirancang untuk citra VHR; dilatih dan dievaluasi pada dataset remote sensing untuk deteksi objek.

Komponen / langkah metodologis utama:

- Arsitektur CNN hierarkis multi-skala.
- Robust terhadap skala/orientasi/latar.
- Fokus citra VHR.
- Pelatihan pada remote sensing.
- Deteksi objek beragam.
- Evaluasi dataset VHR.

## Kontribusi Utama
1. CNN hierarkis robust untuk VHR.
2. Menangani variasi skala/orientasi.
3. Akurasi tinggi pada remote sensing.
4. Kontribusi deteksi penginderaan jauh.

## Rincian Eksperimen
Diuji pada dataset remote sensing VHR dengan metrik deteksi (IEEE TGRS 2019).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Remote sensing VHR | akurasi | tinggi |
| Skala/orientasi | robustness | ditingkatkan |
| Latar kompleks | robustness | ditangani |

## Temuan Kunci
- Fitur hierarkis penting untuk VHR.
- Robustness terhadap variasi krusial.
- Detektor khusus mengungguli umum.
- Remote sensing menuntut adaptasi.

## Keunggulan
- Robust untuk VHR.
- Hierarkis multi-skala.
- Akurasi tinggi.

## Keterbatasan
- Fokus domain remote sensing.
- RGB/citra saja.
- Generalisasi bervariasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini melengkapi klaster Remote Sensing tinjauan dengan detektor VHR yang robust terhadap variasi.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Remote Sensing** yang baik dibaca berdampingan:

- [137 - 2021 - TPH-YOLOv5 (Drone Detection) - Remote Sensing](./137%20-%202021%20-%20TPH-YOLOv5%20%28Drone%20Detection%29%20-%20Remote%20Sensing.md)
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
Zhang dkk. mengusulkan CNN hierarkis robust untuk deteksi objek pada citra remote sensing resolusi sangat tinggi, menangani variasi skala/orientasi dan latar kompleks.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhang2019remotesensing` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 138/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
