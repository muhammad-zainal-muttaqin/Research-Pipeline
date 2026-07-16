# 106 - RGB and Depth Image Fusion for Object Detection Using Deep Learning

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 106 dari 154 |
| Kunci BibTeX | `farahnakian2021fusion` |
| Judul | RGB and Depth Image Fusion for Object Detection Using Deep Learning |
| Penulis | Farahnakian, Fahimeh; Heikkonen, Jukka |
| Tahun | 2021 |
| Venue / Jurnal | Deep Learning Applications |
| Tema klaster | Pedestrian RGB-T |
| Kata kunci | RGB-D, deteksi objek, early/late fusion, deep learning, studi fusi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=RGB%20and%20Depth%20Image%20Fusion%20for%20Object%20Detection%20Using%20Deep%20Learning
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=RGB%20and%20Depth%20Image%20Fusion%20for%20Object%20Detection%20Using%20Deep%20Learning&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 73--93 |
| Penerbit | Springer |

## Ringkasan Eksekutif
Studi yang membandingkan strategi fusi (early/late) citra RGB dan kedalaman untuk deteksi objek berbasis deep learning, memberi panduan empiris pemilihan strategi.

## Abstrak (Parafrase)
Makalah ini mengevaluasi cara-cara menggabungkan citra RGB dan kedalaman untuk deteksi objek dengan deep learning, membandingkan early fusion (menggabungkan di input/awal) dan late fusion (menggabungkan skor/fitur akhir). Ia menganalisis kontribusi kanal kedalaman dan menunjukkan fusi meningkatkan deteksi dibanding RGB saja.

## Latar Belakang & Konteks
Cara terbaik menggabungkan RGB dan kedalaman untuk deteksi belum tuntas; early vs late fusion memiliki trade-off yang perlu dievaluasi empiris.

## Permasalahan yang Diangkat
- Cara terbaik fusi RGB-D untuk deteksi belum jelas.
- Early vs late fusion memiliki trade-off.
- Kontribusi kanal kedalaman perlu diukur.
- Deteksi berbasis DL menuntut strategi tepat.
- Panduan empiris masih kurang.

## Tujuan & Pertanyaan Penelitian
- Membandingkan strategi early vs late fusion.
- Menganalisis kontribusi kanal kedalaman.
- Memberi panduan pemilihan strategi fusi.

## Tinjauan Terdahulu / Posisi Literatur
Studi ini membandingkan skema fusi pada detektor CNN.

Karya/konsep pembanding yang relevan:

- Detektor CNN (mis. Faster R-CNN) — dasar.
- Early fusion — input/awal.
- Late fusion — skor/fitur akhir.
- Dataset RGB-D.

## Metodologi & Arsitektur
Beberapa konfigurasi fusi diimplementasikan pada detektor CNN: early fusion (RGB-D digabung di input/lapisan awal) dan late fusion (cabang terpisah digabung di akhir); dievaluasi pada dataset RGB-D untuk membandingkan akurasi.

Komponen / langkah metodologis utama:

- Implementasi early fusion (input/awal).
- Implementasi late fusion (skor/fitur akhir).
- Detektor CNN sebagai basis.
- Analisis kontribusi kedalaman.
- Perbandingan empiris strategi.
- Evaluasi dataset RGB-D.

## Kontribusi Utama
1. Perbandingan empiris early vs late fusion.
2. Analisis kontribusi kanal kedalaman.
3. Fusi meningkatkan deteksi vs RGB saja.
4. Panduan praktis pemilihan strategi.

## Rincian Eksperimen
Diuji pada dataset RGB-D dengan metrik deteksi (mAP), membandingkan RGB-only, early fusion, dan late fusion.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Dataset RGB-D | mAP | fusi > RGB saja |
| Early vs late | perbandingan | trade-off strategi |
| Kontribusi depth | analisis | kedalaman meningkatkan deteksi |

## Temuan Kunci
- Fusi RGB-D meningkatkan deteksi atas RGB saja.
- Early vs late memiliki trade-off kasuistis.
- Kanal kedalaman menyumbang informasi berguna.
- Pemilihan strategi bergantung skenario.

## Keunggulan
- Panduan empiris fusi.
- Analisis kontribusi kedalaman.
- Praktis.

## Keterbatasan
- Cakupan dataset/detektor terbatas.
- Bergantung kualitas kedalaman.
- Hasil dapat spesifik-skenario.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Studi ini langsung relevan bagi klaster YOLO+RGB-D: memberi bukti empiris manfaat dan strategi fusi RGB-D untuk deteksi dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Pedestrian RGB-T** yang baik dibaca berdampingan:

- [100 - 2015 - KAIST Multispectral Pedestrian - Pedestrian RGB-T](./100%20-%202015%20-%20KAIST%20Multispectral%20Pedestrian%20-%20Pedestrian%20RGB-T.md)
- [101 - 2019 - IAF R-CNN (Illumination-Aware) - Pedestrian RGB-T](./101%20-%202019%20-%20IAF%20R-CNN%20%28Illumination-Aware%29%20-%20Pedestrian%20RGB-T.md)
- [102 - 2020 - MBNet - Pedestrian RGB-T](./102%20-%202020%20-%20MBNet%20-%20Pedestrian%20RGB-T.md)
- [103 - 2021 - GAFF - Pedestrian RGB-T](./103%20-%202021%20-%20GAFF%20-%20Pedestrian%20RGB-T.md)
- [104 - 2020 - Cyclic Fuse-and-Refine (CFR) - Pedestrian RGB-T](./104%20-%202020%20-%20Cyclic%20Fuse-and-Refine%20%28CFR%29%20-%20Pedestrian%20RGB-T.md)
- [105 - 2022 - CMPD (Uncertainty-Guided Cross-Modal) - Pedestrian RGB-T](./105%20-%202022%20-%20CMPD%20%28Uncertainty-Guided%20Cross-Modal%29%20-%20Pedestrian%20RGB-T.md)

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
Farahnakian & Heikkonen membandingkan early dan late fusion RGB-D untuk deteksi objek berbasis deep learning, memberi panduan empiris bahwa fusi kedalaman meningkatkan deteksi dibanding RGB saja.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `farahnakian2021fusion` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 106/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
