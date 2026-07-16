# 140 - You Only Look Twice: Rapid Multi-Scale Object Detection in Satellite Imagery

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 140 dari 154 |
| Kunci BibTeX | `vanetten2018yolt` |
| Judul | You Only Look Twice: Rapid Multi-Scale Object Detection in Satellite Imagery |
| Penulis | Van Etten, Adam |
| Tahun | 2018 |
| Venue / Jurnal | arXiv preprint arXiv:1805.09512 |
| Tema klaster | Remote Sensing |
| Kata kunci | remote sensing, satelit, YOLO, tiling, objek kecil |

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
- **arXiv (PDF/HTML gratis):** https://arxiv.org/abs/1805.09512
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=You%20Only%20Look%20Twice%3A%20Rapid%20Multi-Scale%20Object%20Detection%20in%20Satellite%20Imagery
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=You%20Only%20Look%20Twice%3A%20Rapid%20Multi-Scale%20Object%20Detection%20in%20Satellite%20Imagery&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| arXiv | 1805.09512 |

## Ringkasan Eksekutif
Adaptasi YOLO ('You Only Look Twice') untuk deteksi multi-skala cepat pada citra satelit beresolusi/berukuran besar.

## Abstrak (Parafrase)
Van Etten mengembangkan YOLT (You Only Look Twice), mengadaptasi YOLO untuk citra satelit yang sangat besar dengan memproses tile dan dua lintasan skala untuk menangani objek kecil (kendaraan, bangunan, pesawat). YOLT mendeteksi objek pada skala satelit secara cepat, menjadi adaptasi awal YOLO berpengaruh untuk remote sensing.

## Latar Belakang & Konteks
Citra satelit sangat besar (jutaan piksel) dengan objek kecil menyulitkan detektor standar yang dirancang untuk citra kecil.

## Permasalahan yang Diangkat
- Citra satelit sangat besar (jutaan piksel).
- Objek satelit kecil (kendaraan/bangunan).
- Detektor standar untuk citra kecil.
- Skala bervariasi lebar.
- Kecepatan diperlukan untuk area luas.

## Tujuan & Pertanyaan Penelitian
- Memproses citra satelit besar via tiling.
- Menangani objek kecil multi-skala (dua lintasan).
- Mendeteksi objek satelit secara cepat.

## Tinjauan Terdahulu / Posisi Literatur
YOLT mengadaptasi YOLO untuk skala satelit.

Karya/konsep pembanding yang relevan:

- YOLO — detektor dasar.
- Tiling — pemecahan citra besar.
- Multi-skala (dua lintasan).
- Citra satelit.

## Metodologi & Arsitektur
Citra satelit besar dipecah menjadi tile; YOLO dijalankan pada tile dengan dua lintasan skala (untuk objek besar & kecil); deteksi digabung kembali ke citra penuh; dioptimalkan untuk objek kecil satelit.

Komponen / langkah metodologis utama:

- Tiling citra satelit besar.
- Dua lintasan skala (objek besar & kecil).
- YOLO pada tiap tile.
- Penggabungan deteksi ke citra penuh.
- Optimasi objek kecil.
- Evaluasi citra satelit.

## Kontribusi Utama
1. Adaptasi YOLO untuk skala satelit.
2. Tiling + dua lintasan skala.
3. Deteksi objek kecil satelit cepat.
4. Adaptasi awal berpengaruh remote sensing.

## Rincian Eksperimen
Diuji pada citra satelit dengan metrik deteksi objek (kendaraan/bangunan/pesawat) (arXiv 2018).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Citra satelit | deteksi | objek kecil terdeteksi cepat |
| Tiling | skala besar | citra jutaan piksel |
| Dua lintasan | multi-skala | objek besar & kecil |

## Temuan Kunci
- Tiling memungkinkan deteksi pada citra besar.
- Dua lintasan skala menangani objek kecil.
- YOLO dapat diadaptasi untuk satelit.
- Kecepatan penting untuk area luas.

## Keunggulan
- Adaptasi satelit awal.
- Tiling + multi-skala.
- Cepat.

## Keterbatasan
- Tiling menambah overhead penggabungan.
- Objek sangat kecil tetap menantang.
- RGB/citra saja.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini adalah adaptasi awal YOLO yang berpengaruh untuk remote sensing satelit dalam tinjauan.

## Hubungan dengan Entri Lain
Entri lain pada klaster **Remote Sensing** yang baik dibaca berdampingan:

- [137 - 2021 - TPH-YOLOv5 (Drone Detection) - Remote Sensing](./137%20-%202021%20-%20TPH-YOLOv5%20%28Drone%20Detection%29%20-%20Remote%20Sensing.md)
- [138 - 2019 - Robust CNN High-Res Remote Sensing (Zhang dkk.) - Remote Sensing](./138%20-%202019%20-%20Robust%20CNN%20High-Res%20Remote%20Sensing%20%28Zhang%20dkk.%29%20-%20Remote%20Sensing.md)
- [139 - 2023 - UAV-YOLOv8 (Small Object) - Remote Sensing](./139%20-%202023%20-%20UAV-YOLOv8%20%28Small%20Object%29%20-%20Remote%20Sensing.md)

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
YOLT mengadaptasi YOLO untuk citra satelit besar dengan tiling dan dua lintasan skala, mendeteksi objek kecil pada skala satelit secara cepat sebagai adaptasi awal yang berpengaruh.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `vanetten2018yolt` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 140/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
