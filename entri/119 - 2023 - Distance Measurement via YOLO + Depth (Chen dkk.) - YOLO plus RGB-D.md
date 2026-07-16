# 119 - Indoor Object Distance Measurement for Robots Based on YOLO and Depth Foreground Prediction

> **Lembar telaah jurnal** — bagian dari tinjauan pustaka *YOLO / RGB / RGB+Depth / YOLO+RGB-D (2019-2026)*. Berkas ini merangkum isi makalah agar dapat Anda baca dan verifikasi manual. Buka tautan akses untuk membaca/mengunduh naskah aslinya.

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Nomor entri | 119 dari 154 |
| Kunci BibTeX | `chen2023depthyolo` |
| Judul | Indoor Object Distance Measurement for Robots Based on YOLO and Depth Foreground Prediction |
| Penulis | Chen, Yu-Chen; others |
| Tahun | 2023 |
| Venue / Jurnal | Proceedings of the IEEE International Conference on Advanced Robotics and Intelligent Systems (ARIS) |
| Tema klaster | YOLO plus RGB-D |
| Kata kunci | YOLO+RGB-D, pengukuran jarak, depth foreground, robot indoor, ARIS |

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
18. [Glosarium Istilah](#glosarium-istilah-tema-yolo-plus-rgb-d)
19. [Checklist Verifikasi Manual](#checklist-verifikasi-manual)
20. [Kesimpulan](#kesimpulan)
21. [Cara Memverifikasi & Sitasi](#cara-memverifikasi--sitasi)

## Tautan Akses (klik untuk view/unduh)
- **Cari / unduh via Google Scholar:** https://scholar.google.com/scholar?q=Indoor%20Object%20Distance%20Measurement%20for%20Robots%20Based%20on%20YOLO%20and%20Depth%20Foreground%20Prediction
- **Semantic Scholar (metrik sitasi & PDF):** https://www.semanticscholar.org/search?q=Indoor%20Object%20Distance%20Measurement%20for%20Robots%20Based%20on%20YOLO%20and%20Depth%20Foreground%20Prediction&sort=relevance

## Identitas Publikasi
Rincian bibliografis tambahan (dari `references.bib`; kolom kosong berarti belum tercatat dan perlu dilengkapi dari sumber asli):

| Atribut | Nilai |
|---|---|
| — | — |

## Ringkasan Eksekutif
Metode pengukuran jarak objek indoor untuk robot dengan menggabungkan deteksi YOLO dan prediksi foreground kedalaman.

## Abstrak (Parafrase)
Chen dkk. mengembangkan metode pengukuran jarak objek untuk robot indoor: YOLO mendeteksi dan melokalisasi objek pada citra, lalu prediksi foreground kedalaman memberi estimasi jarak objek dari kamera. Kombinasi ini memberi robot informasi jarak yang andal, bukan sekadar kotak 2D. (ARIS 2023.)

## Latar Belakang & Konteks
Robot indoor membutuhkan jarak objek yang akurat (untuk navigasi/manipulasi), bukan hanya deteksi 2D; menggabungkan deteksi dan kedalaman menjawab kebutuhan ini.

## Permasalahan yang Diangkat
- Robot indoor butuh jarak objek, bukan hanya kotak 2D.
- Deteksi 2D saja tak memberi jarak.
- Kedalaman foreground perlu diprediksi/diproses.
- Objek harus dipisah dari latar untuk jarak akurat.
- Real-time diinginkan untuk robot.

## Tujuan & Pertanyaan Penelitian
- Mendeteksi objek via YOLO.
- Mengestimasi jarak via foreground kedalaman.
- Menyediakan informasi jarak untuk robot indoor.

## Tinjauan Terdahulu / Posisi Literatur
Metode menggabungkan YOLO dan pemrosesan depth foreground.

Karya/konsep pembanding yang relevan:

- YOLO — deteksi objek.
- Depth foreground prediction.
- Robot indoor (navigasi/manipulasi).
- Kamera RGB-D/depth.

## Metodologi & Arsitektur
YOLO mendeteksi objek pada citra RGB; prediksi foreground kedalaman memisahkan objek dari latar dan memberi nilai kedalaman objek; jarak objek dihitung dari kedalaman foreground di dalam kotak deteksi; dipakai robot indoor.

Komponen / langkah metodologis utama:

- Deteksi objek via YOLO (kotak).
- Depth foreground prediction (objek vs latar).
- Estimasi jarak dari kedalaman foreground.
- Integrasi deteksi + kedalaman.
- Orientasi robot indoor.
- Uji indoor.

## Kontribusi Utama
1. Pengukuran jarak objek via YOLO + depth.
2. Foreground kedalaman memisahkan objek dari latar.
3. Informasi jarak andal untuk robot.
4. Contoh praktis YOLO+depth indoor.

## Rincian Eksperimen
Diuji pada skenario indoor dengan metrik akurasi estimasi jarak objek untuk robot (ARIS 2023).

Ringkasan pengaturan & hasil (kualitatif bila angka pasti tak dikutip di sini — konfirmasi ke naskah):

| Dataset / Uji | Metrik | Catatan hasil |
|---|---|---|
| Indoor | akurasi jarak | estimasi jarak objek andal |
| Foreground depth | segmentasi | objek dipisah dari latar |
| Integrasi | YOLO+depth | deteksi + jarak |

## Temuan Kunci
- YOLO+depth memberi jarak objek untuk robot.
- Foreground kedalaman meningkatkan akurasi jarak.
- Deteksi + kedalaman saling melengkapi.
- Praktis untuk persepsi robot indoor.

## Keunggulan
- Praktis (jarak untuk robot).
- Integrasi YOLO+depth.
- Indoor.

## Keterbatasan
- Bergantung kualitas kedalaman.
- Fokus domain indoor.
- Detail bergantung implementasi.

> Sebagian butir keterbatasan merupakan **inferensi analitis**, bukan pernyataan eksplisit penulis. Tandai saat verifikasi.

## Relevansi terhadap Tema Tinjauan
Entri ini adalah contoh praktis YOLO+depth untuk persepsi jarak robot indoor dalam tinjauan, menautkan deteksi dengan pemanfaatan kedalaman langsung.

## Hubungan dengan Entri Lain
Entri lain pada klaster **YOLO plus RGB-D** yang baik dibaca berdampingan:

- [112 - 2020 - Expandable YOLO - YOLO plus RGB-D](./112%20-%202020%20-%20Expandable%20YOLO%20-%20YOLO%20plus%20RGB-D.md)
- [113 - 2024 - FusionVision - YOLO plus RGB-D](./113%20-%202024%20-%20FusionVision%20-%20YOLO%20plus%20RGB-D.md)
- [114 - 2024 - Pumpkin Pick-and-Place Robot (Ito dkk.) - YOLO plus RGB-D](./114%20-%202024%20-%20Pumpkin%20Pick-and-Place%20Robot%20%28Ito%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [115 - 2025 - YOLOv8-URE 2D+Point Cloud Grasping - YOLO plus RGB-D](./115%20-%202025%20-%20YOLOv8-URE%202D+Point%20Cloud%20Grasping%20-%20YOLO%20plus%20RGB-D.md)
- [116 - 2023 - Grasp via YOLO + RGB-D Fusion (Tian dkk.) - YOLO plus RGB-D](./116%20-%202023%20-%20Grasp%20via%20YOLO%20+%20RGB-D%20Fusion%20%28Tian%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [117 - 2024 - Onboard Dynamic-Object Detection (Xu dkk.) - YOLO plus RGB-D](./117%20-%202024%20-%20Onboard%20Dynamic-Object%20Detection%20%28Xu%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)
- [118 - 2019 - Exploring RGB+Depth Fusion (Ophoff dkk.) - YOLO plus RGB-D](./118%20-%202019%20-%20Exploring%20RGB+Depth%20Fusion%20%28Ophoff%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md)

## Konteks Klaster & Cara Membaca
- **Klaster:** entri ini termasuk tema **YOLO plus RGB-D** dalam peta tinjauan (17 klaster, 154 entri total).
- **Cara membaca:** mulai dari *Ringkasan Eksekutif* untuk gambaran cepat, lalu *Metodologi* dan *Rincian Eksperimen* untuk detail teknis, dan *Relevansi* untuk kaitan dengan fokus YOLO/RGB/RGB-D.
- **Untuk verifikasi:** bandingkan *Abstrak (Parafrase)* dan tabel hasil dengan naskah asli melalui *Tautan Akses*.
- **Untuk menulis:** kutip memakai kunci BibTeX pada tabel Metadata; lihat *Hubungan dengan Entri Lain* untuk membangun paragraf perbandingan.

## Glosarium Istilah (tema YOLO plus RGB-D)
Istilah penting untuk memahami makalah ini:

- **YOLO** — Detektor satu-tahap real-time regresi tunggal.
- **Kanal depth** — Peta kedalaman sebagai masukan tambahan.
- **Fusi RGB-D** — Penggabungan warna dan kedalaman pada deteksi.
- **Lokalisasi 3D** — Posisi objek dalam koordinat 3D via depth.
- **Point cloud** — Titik 3D dari depth untuk grasp/rekonstruksi.
- **Pick-and-place** — Tugas robot mengambil dan menempatkan objek.
- **RealSense/Kinect** — Kamera RGB-D konsumen umum.
- **Early/mid/late fusion** — Titik penggabungan depth pada arsitektur.
- **Segment Anything (SAM)** — Model segmentasi umum; FastSAM=versi cepat.
- **Real-time deployment** — Penerapan dengan kendala latensi.

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
Chen dkk. menggabungkan deteksi YOLO dan prediksi foreground kedalaman untuk mengukur jarak objek indoor bagi robot, memberi informasi jarak andal melampaui kotak 2D.

## Cara Memverifikasi & Sitasi
1. Buka salah satu **Tautan Akses** (arXiv untuk PDF gratis; DOI untuk versi penerbit; Scholar/Semantic Scholar untuk pencarian).
2. Cocokkan **judul, penulis, tahun, venue** dengan tabel Metadata & Identitas Publikasi.
3. Bandingkan bagian **Metodologi**, **Rincian Eksperimen**, dan **Kontribusi** dengan abstrak/isi makalah.
4. Untuk sitasi, gunakan kunci BibTeX `chen2023depthyolo` yang telah ada di `references.bib`.
5. Bila metadata (volume/halaman/DOI) keliru, perbaiki di `references.bib` lalu kompilasi ulang `tinjauan-pustaka.tex`.

## Catatan Penggunaan Berkas
- Berkas ini adalah **lembar telaah**, bukan pengganti naskah asli — selalu baca sumbernya untuk detail penuh.
- *Abstrak* dan *Ringkasan* adalah parafrase; angka/klaim spesifik wajib dikonfirmasi ke naskah.
- Untuk penulisan tinjauan pustaka, kutip memakai **kunci BibTeX** pada tabel Metadata.
- Untuk membangun paragraf perbandingan, lihat bagian *Hubungan dengan Entri Lain* dan *Glosarium*.
- Bila menemukan ketidaksesuaian metadata, perbarui `references.bib` agar sitasi tetap akurat.
- Tema dan penomoran berkas mengikuti peta 17 klaster pada `TEMUAN.md` dan `INDEX.md`.

---
*Lembar 119/154 — untuk telaah & verifikasi tinjauan pustaka. Abstrak = parafrase. Selalu rujuk naskah asli via tautan.*
