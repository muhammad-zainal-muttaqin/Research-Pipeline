# 039 - Learning Selective Self-Mutual Attention for RGB-D Saliency Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 039 dari 154 |
| Kunci BibTeX | `liu2020s2ma` |
| Judul | Learning Selective Self-Mutual Attention for RGB-D Saliency Detection |
| Penulis | Liu, Nian; Zhang, Ni; Han, Junwei |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, self-mutual attention, seleksi, depth tak andal, fusi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Learning%20Selective%20Self-Mutual%20Attention%20for%20RGB-D%20Saliency%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Learning%20Selective%20Self-Mutual%20Attention%20for%20RGB-D%20Saliency%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 13756--13765 |

## Ringkasan Eksekutif
Metode RGB-D SOD yang mempelajari self-mutual attention selektif untuk saling menyempurnakan fitur RGB dan kedalaman sambil menyaring kedalaman tak andal.

## Abstrak (Parafrase)
S2MA (Selective Self-Mutual Attention) memperkenalkan attention yang menggabungkan self-attention dalam-modal dan mutual-attention lintas-modal, dengan mekanisme seleksi yang menekan kontribusi kedalaman menyesatkan. Ini mencegah penyebaran kesalahan dari peta kedalaman berkualitas rendah dan meningkatkan konsistensi saliency.

## Latar Belakang & Konteks
Attention lintas-modal dapat menyebarkan kesalahan bila salah satu modal (kedalaman) tidak andal, sehingga fusi memerlukan mekanisme seleksi keandalan.

## Permasalahan yang Diangkat
- Attention lintas-modal menyebarkan kesalahan depth buruk.
- Kedalaman tak andal menurunkan fusi.
- Self- dan mutual-attention perlu diseimbangkan.
- Konsistensi saliency lintas-modal sulit.
- Seleksi keandalan belum ada pada attention klasik.

## Tujuan & Pertanyaan Penelitian
- Menggabungkan self- dan mutual-attention untuk fusi.
- Menyaring kontribusi kedalaman menyesatkan.
- Meningkatkan konsistensi saliency RGB-D.

## Tinjauan Terdahulu / Posisi Literatur
S2MA mengembangkan non-local/self-attention untuk fusi RGB-D dengan seleksi keandalan.

Karya/konsep pembanding yang relevan:

- Non-local/self-attention — dasar mekanisme.
- Mutual attention lintas-modal.
- RGB-D SOD berbasis fusi.
- Reliability gating — seleksi keandalan.

## Metodologi & Arsitektur
Modul self-mutual attention menghitung attention dalam-modal (RGB, depth) dan lintas-modal, lalu menerapkan seleksi (selection) untuk menekan fitur depth tak andal sebelum digabung; jaringan menghasilkan saliency yang lebih konsisten.

Komponen / langkah metodologis utama:

- Self-attention dalam-modal (RGB & depth).
- Mutual-attention lintas-modal.
- Selection mechanism menekan depth menyesatkan.
- Fusi terpandu attention selektif.
- Decoder saliency.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Self-mutual attention selektif untuk fusi RGB-D.
2. Seleksi keandalan mencegah penyebaran kesalahan.
3. Peningkatan konsistensi saliency.
4. Hasil kompetitif pada benchmark.

## Rincian Eksperimen
Diuji pada benchmark RGB-D SOD standar dengan metrik S/F/E-measure dan MAE, plus ablation mekanisme seleksi.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NJU2K/NLPR | S/F/E, MAE | peningkatan konsisten |
| STERE/SIP | S/F/E, MAE | kompetitif |
| Ablation | selection | seleksi keandalan menyumbang gain |

## Temuan Kunci
- Seleksi keandalan penting pada attention lintas-modal.
- Self+mutual attention saling melengkapi.
- Depth buruk dapat ditekan efektif.
- Konsistensi saliency meningkat.

## Keunggulan
- Menangani keandalan depth eksplisit.
- Attention lintas-modal efektif.
- Peningkatan konsisten.

## Keterbatasan
- Attention non-local mahal komputasi.
- Bergantung metrik seleksi.
- Backbone CNN (konteks terbatas).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
S2MA memperkuat tema penting tinjauan: fusi RGB+Depth harus menyaring keandalan modal — prinsip yang berlaku juga untuk YOLO+RGB-D.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [035 - 2019 - DMRA - RGB-D SOD](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)
- [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)
- [037 - 2021 - D3Net (Rethinking RGB-D SOD) - RGB-D SOD](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md)
- [038 - 2020 - JL-DCF - RGB-D SOD](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md)
- [040 - 2020 - HDFNet - RGB-D SOD](./040%20-%202020%20-%20HDFNet%20-%20RGB-D%20SOD.md)
- [041 - 2020 - UC-Net - RGB-D SOD](./041%20-%202020%20-%20UC-Net%20-%20RGB-D%20SOD.md)
- [042 - 2021 - Visual Saliency Transformer (VST) - RGB-D SOD](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md)
- [043 - 2022 - SwinNet - RGB-D SOD](./043%20-%202022%20-%20SwinNet%20-%20RGB-D%20SOD.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **RGB-D SOD** dalam peta tinjauan (17 klaster, 154 entri total).
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
S2MA memperkenalkan self-mutual attention selektif yang menyaring kedalaman tak andal, mencegah penyebaran kesalahan dan meningkatkan konsistensi fusi RGB-D SOD.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `liu2020s2ma` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 039/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
