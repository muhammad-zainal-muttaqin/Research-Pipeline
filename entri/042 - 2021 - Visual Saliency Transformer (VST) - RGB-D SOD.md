# 042 - Visual Saliency Transformer

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 042 dari 154 |
| Kunci BibTeX | `liu2021vst` |
| Judul | Visual Saliency Transformer |
| Penulis | Liu, Nian; Zhang, Ni; Wan, Kaiyuan; Shao, Ling; Han, Junwei |
| Tahun | 2021 |
| Venue / Jurnal | Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) |
| Tema klaster | RGB-D SOD |
| Kata kunci | SOD, Transformer, token-based, multi-task decoder, RGB-D |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Visual%20Saliency%20Transformer
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Visual%20Saliency%20Transformer&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 4722--4732 |

## Ringkasan Eksekutif
Kerangka SOD berbasis Transformer murni untuk RGB dan RGB-D, dengan token-based multi-task decoder dan reverse token-to-token upsampling.

## Abstrak (Parafrase)
VST (Visual Saliency Transformer) menerapkan Transformer murni untuk salient object detection pada RGB maupun RGB-D. Encoder Transformer menangkap konteks global; multi-task token decoder memprediksi saliency dan batas objek bersama; reverse token-to-token (RT2T) upsampling memulihkan resolusi. VST mencapai SOTA pada RGB dan RGB-D SOD saat rilis.

## Latar Belakang & Konteks
SOD berbasis CNN terbatas dalam menangkap konteks global (receptive field lokal), sementara Transformer murni belum tereksplorasi untuk SOD dan prediksi padatnya.

## Permasalahan yang Diangkat
- SOD berbasis CNN terbatas konteks global.
- Transformer murni belum dieksplorasi untuk SOD.
- Prediksi padat butuh pemulihan resolusi dari token.
- Saliency & batas objek perlu diprediksi bersama.
- Fusi RGB-D pada Transformer belum matang.

## Tujuan & Pertanyaan Penelitian
- Menerapkan Transformer murni untuk SOD.
- Memprediksi saliency & batas via token decoder.
- Memulihkan resolusi dengan RT2T upsampling.

## Tinjauan Terdahulu / Posisi Literatur
VST mengadaptasi ViT/T2T-ViT ke SOD untuk RGB dan RGB-D.

Karya/konsep pembanding yang relevan:

- ViT/T2T-ViT — backbone Transformer.
- SOD berbasis CNN — pembanding.
- Token-based decoding.
- Boundary-aware saliency.

## Metodologi & Arsitektur
Encoder Transformer (T2T) memproses token citra (dan kedalaman untuk RGB-D); multi-task token decoder memprediksi saliency dan batas objek; reverse token-to-token (RT2T) upsampling memulihkan resolusi peta; token task-related mengarahkan prediksi.

Komponen / langkah metodologis utama:

- Encoder Transformer (T2T) untuk RGB(-D).
- Multi-task token decoder (saliency + boundary).
- Reverse token-to-token (RT2T) upsampling.
- Task-related tokens.
- Fusi token RGB-D.
- Pelatihan end-to-end.

## Kontribusi Utama
1. SOD berbasis Transformer murni lintas modalitas.
2. Multi-task decoder (saliency + boundary).
3. RT2T upsampling untuk prediksi padat.
4. SOTA RGB & RGB-D SOD saat rilis.

## Rincian Eksperimen
Diuji pada benchmark RGB SOD dan RGB-D SOD dengan metrik S/F/E-measure dan MAE, dibandingkan metode berbasis CNN.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| RGB SOD | S/F/E, MAE | SOTA saat rilis |
| RGB-D SOD | S/F/E, MAE | SOTA saat rilis |
| Ablation | RT2T/multi-task | keduanya menyumbang gain |

## Temuan Kunci
- Transformer murni efektif untuk SOD.
- Konteks global meningkatkan saliency.
- Multi-task (boundary) memperbaiki tepi.
- RT2T memulihkan resolusi dari token.

## Keunggulan
- Transformer murni lintas modalitas.
- Multi-task decoder efektif.
- SOTA saat rilis.

## Keterbatasan
- Transformer mahal komputasi.
- Butuh data pra-latih memadai.
- Bergantung kualitas kedalaman (RGB-D).

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
VST membuka SOD berbasis Transformer murni yang relevan bagi tren backbone Transformer pada fusi RGB+Depth dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [035 - 2019 - DMRA - RGB-D SOD](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)
- [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)
- [037 - 2021 - D3Net (Rethinking RGB-D SOD) - RGB-D SOD](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md)
- [038 - 2020 - JL-DCF - RGB-D SOD](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md)
- [039 - 2020 - S2MA - RGB-D SOD](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md)
- [040 - 2020 - HDFNet - RGB-D SOD](./040%20-%202020%20-%20HDFNet%20-%20RGB-D%20SOD.md)
- [041 - 2020 - UC-Net - RGB-D SOD](./041%20-%202020%20-%20UC-Net%20-%20RGB-D%20SOD.md)
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
VST menghadirkan SOD berbasis Transformer murni untuk RGB dan RGB-D dengan multi-task token decoder dan RT2T upsampling, mencapai SOTA dan membuka arah Transformer untuk saliency.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `liu2021vst` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 042/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
