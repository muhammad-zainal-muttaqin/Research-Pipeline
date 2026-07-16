# 168 - Specificity-Preserving RGB-D Saliency Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 168 dari 191 |
| Kunci BibTeX | `zhou2021spnet` |
| Judul | Specificity-Preserving RGB-D Saliency Detection |
| Penulis | Zhou, Tao; Fu, Huazhu; Chen, Geng; Zhou, Yi; Fan, Deng-Ping; Shao, Ling |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, specificity-preserving, shared-specific, saliency |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-rgb-d-sod)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Specificity-Preserving%20RGB-D%20Saliency%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Specificity-Preserving%20RGB-D%20Saliency%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
SPNet (Specificity-Preserving Network) menjaga informasi khas tiap modalitas RGB dan depth di samping representasi bersama, sehingga fusi tidak menghapus isyarat spesifik-modal yang berguna untuk saliency.

## Abstrak (Parafrase)
Penulis mengamati bahwa fusi yang terlalu menyatukan dapat menghilangkan ciri unik modalitas. SPNet mempertahankan cabang spesifik RGB dan depth sekaligus membentuk cabang bersama, lalu mengagregasi ketiganya melalui cross-enhanced integration dan multi-modal feature aggregation. Hasilnya SOTA pada beberapa benchmark RGB-D SOD.

## Latar Belakang & Konteks
Fusi lintas-modal harus menyeimbangkan berbagi informasi dan mempertahankan spesifisitas modalitas; banyak metode mengabaikan yang kedua.

## Permasalahan yang Diangkat
- Fusi menghapus ciri spesifik modalitas.
- Keseimbangan shared vs specific sulit.
- Agregasi multiskala belum optimal.

## Tujuan & Pertanyaan Penelitian
- Mempertahankan fitur spesifik-modal.
- Menggabungkan cabang shared dan specific.
- Meningkatkan akurasi SOD.

## Tinjauan Terdahulu / Posisi Literatur
Kontras dengan fusi tunggal (BBS-Net, JL-DCF); menekankan cabang spesifik-modal eksplisit.

Karya/konsep pembanding yang relevan:

- BBS-Net - fusi bercabang.
- JL-DCF - fusi kooperatif padat.
- CoNet - depth kolaboratif.
- S2MA - self-mutual attention.

## Metodologi & Arsitektur
Tiga aliran: RGB-specific, depth-specific, shared; cross-enhanced integration module (CIM) memperkaya cabang, multi-modal feature aggregation (MFA) menggabungkan lintas skala untuk peta saliency.

Komponen / langkah metodologis utama:

- Cabang spesifik RGB & depth + cabang bersama.
- Cross-enhanced integration module.
- Multi-modal feature aggregation.
- Dekoder saliency multiskala.

## Kontribusi Utama
1. Prinsip specificity-preserving pada RGB-D SOD.
2. Modul CIM dan MFA.
3. Peningkatan SOTA di beberapa dataset.
4. Analisis peran fitur spesifik-modal.

## Rincian Eksperimen
Benchmark RGB-D SOD (NJU2K, NLPR, STERE, SIP, DES, DUT-RGBD) dengan S/F/E-measure dan MAE.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NJU2K/NLPR | S-measure | SOTA/kompetitif saat rilis |
| DUT-RGBD/SIP | F/E-measure | peningkatan konsisten |
| Ablation cabang | metrik | cabang spesifik menaikkan hasil |

## Temuan Kunci
- Mempertahankan spesifisitas modal meningkatkan akurasi.
- Kombinasi shared+specific optimal.
- Agregasi multiskala penting.

## Keunggulan
- Memanfaatkan ciri unik tiap modal.
- Akurasi tinggi.
- Modul dapat diadaptasi.

## Keterbatasan
- Tiga aliran menambah parameter.
- Kompleksitas fusi meningkat.
- Bergantung kualitas depth.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Prinsip menjaga informasi spesifik-modal berguna untuk desain fusi RGB-D pada deteksi/segmentasi selain SOD.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [166 - 2020 - CoNet - RGB-D SOD](./166%20-%202020%20-%20CoNet%20-%20RGB-D%20SOD.md)
- [167 - 2021 - DCF - RGB-D SOD](./167%20-%202021%20-%20DCF%20-%20RGB-D%20SOD.md)
- [169 - 2023 - CAVER - RGB-D SOD](./169%20-%202023%20-%20CAVER%20-%20RGB-D%20SOD.md)
- [170 - 2022 - MobileSal - RGB-D SOD](./170%20-%202022%20-%20MobileSal%20-%20RGB-D%20SOD.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SOD** dalam peta tinjauan (17 klaster, 191 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema RGB-D SOD)
Istilah penting untuk memahami makalah ini:

- **SOD** — Salient Object Detection; menyorot objek paling menonjol.
- **Peta kedalaman** — Citra yang tiap pikselnya menyatakan jarak ke kamera.
- **Fusi lintas-modal** — Penggabungan fitur RGB dan depth.
- **Early/middle/late fusion** — Fusi di input, fitur tengah, atau keputusan akhir.
- **Attention lintas-modal** — Membobot kontribusi RGB vs depth secara adaptif.
- **S-measure** — Structure-measure; kemiripan struktur peta saliency.
- **E-measure** — Enhanced-alignment measure; kesejajaran piksel-global.
- **F-measure** — Harmonik precision-recall pada peta saliency.
- **MAE** — Mean Absolute Error peta saliency vs ground truth.
- **Depth berkualitas rendah** — Depth berderau yang dapat merusak fusi.
- **Backbone Transformer** — Encoder attention (mis. Swin) untuk konteks global.

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
SPNet menegaskan pentingnya mempertahankan ciri khas tiap modalitas dalam fusi RGB-D, menghasilkan SOD yang lebih akurat.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhou2021spnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 168/191 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
