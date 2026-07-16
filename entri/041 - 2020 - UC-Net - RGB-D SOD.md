# 041 - UC-Net: Uncertainty Inspired RGB-D Saliency Detection via Conditional Variational Autoencoders

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 041 dari 154 |
| Kunci BibTeX | `zhang2020ucnet` |
| Judul | UC-Net: Uncertainty Inspired RGB-D Saliency Detection via Conditional Variational Autoencoders |
| Penulis | Zhang, Jing; Fan, Deng-Ping; Dai, Yuchao; Anwar, Saeed; Saleh, Fatemeh Sadat; Zhang, Tong; Barnes, Nick |
| Tahun | 2020 |
| Venue / Jurnal | Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) |
| Tema klaster | RGB-D SOD |
| Kata kunci | RGB-D SOD, ketidakpastian, conditional VAE, probabilistik, kalibrasi |

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
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=UC-Net%3A%20Uncertainty%20Inspired%20RGB-D%20Saliency%20Detection%20via%20Conditional%20Variational%20Autoencoders
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=UC-Net%3A%20Uncertainty%20Inspired%20RGB-D%20Saliency%20Detection%20via%20Conditional%20Variational%20Autoencoders&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| Halaman | 8582--8591 |

## Ringkasan Eksekutif
Metode RGB-D SOD pertama yang memodelkan ketidakpastian anotasi manusia via conditional VAE untuk menghasilkan beragam prediksi saliency yang lebih kalibratif.

## Abstrak (Parafrase)
UC-Net (Uncertainty inspired RGB-D saliency) memodelkan ambiguitas dan variasi anotasi manusia dengan conditional variational autoencoder (CVAE). Alih-alih satu peta deterministik, jaringan menghasilkan distribusi prediksi saliency; sampling menghasilkan ensembel yang menangkap ketidakpastian, meningkatkan kalibrasi dan robustness.

## Latar Belakang & Konteks
SOD deterministik menghasilkan satu peta 'benar', mengabaikan fakta bahwa anotasi manusia bervariasi (subjektif/ambigu), sehingga model tak menangkap ketidakpastian.

## Permasalahan yang Diangkat
- SOD deterministik mengabaikan ambiguitas anotasi.
- Anotasi manusia bervariasi/subjektif.
- Ketidakpastian prediksi tidak dimodelkan.
- Kalibrasi output kurang.
- Robustness terhadap ambiguitas rendah.

## Tujuan & Pertanyaan Penelitian
- Memodelkan ketidakpastian anotasi via CVAE.
- Menghasilkan beragam prediksi saliency.
- Meningkatkan kalibrasi dan robustness.

## Tinjauan Terdahulu / Posisi Literatur
UC-Net membawa VAE/probabilistic modeling ke RGB-D SOD.

Karya/konsep pembanding yang relevan:

- Conditional VAE — pemodelan distribusi.
- RGB-D SOD berbasis fusi.
- Probabilistic prediction.
- Ensembling via sampling.

## Metodologi & Arsitektur
CVAE mengondisikan pada fitur RGB-D dan variabel laten; saat inferensi, sampling variabel laten menghasilkan beragam peta saliency (ensembel) yang menangkap ketidakpastian; peta akhir dapat diagregasi.

Komponen / langkah metodologis utama:

- Conditional VAE memodelkan distribusi saliency.
- Variabel laten menangkap ambiguitas anotasi.
- Sampling menghasilkan ensembel prediksi.
- Fusi fitur RGB-D sebagai kondisi.
- Agregasi ensembel untuk peta akhir.
- Estimasi ketidakpastian per-piksel.

## Kontribusi Utama
1. Pemodelan ketidakpastian pertama pada RGB-D SOD.
2. CVAE menghasilkan beragam prediksi kalibratif.
3. Menangkap variasi anotasi manusia.
4. Hasil kompetitif dengan estimasi ketidakpastian.

## Rincian Eksperimen
Diuji pada benchmark RGB-D SOD standar dengan metrik S/F/E-measure dan MAE, plus analisis kualitas ketidakpastian/ensembel.

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| NJU2K/NLPR | S/F/E, MAE | kompetitif saat rilis |
| Uncertainty | kalibrasi | estimasi ketidakpastian per-piksel |
| Ablation | CVAE | sampling meningkatkan robustness |

## Temuan Kunci
- Ketidakpastian anotasi dapat dimodelkan CVAE.
- Ensembel prediksi lebih kalibratif.
- Robustness meningkat terhadap ambiguitas.
- Membuka arah probabilistik RGB-D SOD.

## Keunggulan
- Pelopor pemodelan ketidakpastian.
- Output kalibratif.
- Robust terhadap ambiguitas.

## Keterbatasan
- Sampling menambah biaya inferensi.
- Bergantung kualitas kedalaman.
- Interpretasi ketidakpastian perlu hati-hati.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
UC-Net memperkenalkan dimensi ketidakpastian yang relevan bagi keandalan fusi RGB+Depth secara umum — penting saat kedalaman/anotasi tak pasti.

## Hubungan dengan Entri Lain
Entri lain pada klaster **RGB-D SOD** yang baik dibaca berdampingan:

- [035 - 2019 - DMRA - RGB-D SOD](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)
- [036 - 2020 - BBS-Net - RGB-D SOD](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)
- [037 - 2021 - D3Net (Rethinking RGB-D SOD) - RGB-D SOD](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md)
- [038 - 2020 - JL-DCF - RGB-D SOD](./038%20-%202020%20-%20JL-DCF%20-%20RGB-D%20SOD.md)
- [039 - 2020 - S2MA - RGB-D SOD](./039%20-%202020%20-%20S2MA%20-%20RGB-D%20SOD.md)
- [040 - 2020 - HDFNet - RGB-D SOD](./040%20-%202020%20-%20HDFNet%20-%20RGB-D%20SOD.md)
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
UC-Net memodelkan ketidakpastian anotasi manusia via conditional VAE untuk menghasilkan prediksi RGB-D SOD yang beragam dan kalibratif, menjadi pelopor pendekatan probabilistik di bidang ini.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `zhang2020ucnet` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

---
*Lembar 041/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
