# 038 - JL-DCF: Joint Learning and Densely-Cooperative Fusion Framework for RGB-D Salient Object Detection

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 038 dari 154 |
| Kunci BibTeX | `fu2020jldcf` |
| Judul | JL-DCF: Joint Learning and Densely-Cooperative Fusion Framework for RGB-D Salient Object Detection |
| Penulis | Fu, Keren; Fan, Deng-Ping; Ji, Ge-Peng; Zhao, Qijun |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, joint learning, siamese, densely-cooperative fusion, berbagi bobot |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=JL-DCF%3A%20Joint%20Learning%20and%20Densely-Cooperative%20Fusion%20Framework%20for%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=JL-DCF%3A%20Joint%20Learning%20and%20Densely-Cooperative%20Fusion%20Framework%20for%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 3052--3062 |

## Ringkasan Eksekutif
Kerangka RGB-D SOD yang memperlakukan RGB dan kedalaman via jaringan siamese berbagi bobot (joint learning) dengan densely-cooperative fusion, menunjukkan berbagi bobot lintas-modal layak dan kuat.

## Abstrak (Parafrase)
JL-DCF (Joint Learning and Densely-Cooperative Fusion) memproses RGB dan peta kedalaman melalui backbone siamese yang berbagi bobot (joint learning), memandang kedalaman sebagai 'citra khusus'. Densely-Cooperative Fusion menggabungkan fitur kedua cabang secara kooperatif di banyak level, menghasilkan peta saliency coarse-to-fine yang SOTA saat rilis.

## Latar Belakang & Konteks
RGB dan kedalaman memiliki perbedaan domain yang menyulitkan pelatihan bersama; banyak metode memakai cabang terpisah yang menambah parameter dan risiko overfitting, sehingga berbagi representasi dipertanyakan.

## Permasalahan yang Diangkat
- Perbedaan domain RGB vs depth menyulitkan pelatihan bersama.
- Cabang terpisah menambah parameter & risiko overfitting.
- Fusi lintas-modal satu-level kurang kaya.
- Kedalaman kurang dimanfaatkan sebagai 'citra'.
- Konsistensi fitur lintas-modal sulit dijaga.

## Tujuan & Pertanyaan Penelitian
- Memproses RGB & depth via backbone berbagi bobot.
- Menggabungkan fitur secara kooperatif di banyak level.
- Menghasilkan saliency coarse-to-fine berkualitas.

## Tinjauan Terdahulu / Posisi Literatur
JL-DCF menggabungkan joint learning (berbagi bobot) dan fusi kooperatif rapat sebagai kerangka umum RGB-D SOD.

Karya/konsep pembanding yang relevan:

- Siamese network — berbagi bobot.
- RGB-D SOD berbasis fusi — dasar.
- Dense fusion — penggabungan rapat.
- Coarse-to-fine decoding.

## Metodologi & Arsitektur
Backbone siamese berbagi bobot mengekstrak fitur dari RGB dan depth (diperlakukan seragam); Densely-Cooperative Fusion menggabungkan fitur kedua modal di banyak level; decoder coarse-to-fine menghasilkan saliency; supervisi multi-level.

Komponen / langkah metodologis utama:

- Backbone siamese berbagi bobot (joint learning).
- Kedalaman diperlakukan sebagai 'citra' input.
- Densely-Cooperative Fusion (DCF) multi-level.
- Decoder coarse-to-fine.
- Supervisi multi-level.
- Pelatihan end-to-end RGB-D.

## Kontribusi Utama
1. Berbagi bobot lintas-modal layak dan hemat parameter.
2. DCF menggabungkan fitur secara kooperatif.
3. Kerangka umum yang efektif untuk RGB-D SOD.
4. SOTA pada benchmark saat rilis.

## Rincian Eksperimen
Diuji pada benchmark RGB-D SOD standar (NJU2K, NLPR, STERE, SIP, DES, dll.) dengan metrik S/F/E-measure dan MAE.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NJU2K/NLPR | S/F/E, MAE | SOTA saat rilis |
| STERE/SIP | S/F/E, MAE | kompetitif/unggul |
| Ablation | joint learning/DCF | keduanya menyumbang gain |

## Temuan Kunci
- Berbagi bobot lintas-modal kuat dan efisien.
- Fusi kooperatif rapat meningkatkan kualitas.
- Memperlakukan depth sebagai citra bermanfaat.
- Kerangka umum dan mudah diadaptasi.

## Keunggulan
- Hemat parameter (berbagi bobot).
- Fusi kooperatif efektif.
- SOTA saat rilis.

## Keterbatasan
- Bergantung kualitas kedalaman.
- Backbone CNN (konteks global terbatas).
- Fusi rapat menambah komputasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
JL-DCF menunjukkan strategi berbagi bobot yang relevan sebagai prinsip efisiensi fusi RGB+Depth dalam tinjauan; berguna untuk memahami desain fusi lintas-modal.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [035 - 2019 - DMRA - RGB-D SOD](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)
- [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)
- [037 - 2021 - D3Net (Rethinking RGB-D SOD) - RGB-D SOD](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md)
- [039 - 2020 - S2MA - RGB-D SOD](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md)
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
JL-DCF membuktikan backbone siamese berbagi bobot dengan densely-cooperative fusion efektif untuk RGB-D SOD, menegaskan kelayakan berbagi representasi lintas-modal.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `fu2020jldcf` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 038/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
