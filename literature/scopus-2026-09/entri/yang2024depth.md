# Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2024depth` |
| Judul asli | Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data |
| Penulis | Yang, Lihe; Kang, Bingyi; Huang, Zilong; Xu, Xiaogang; Feng, Jiashi; Zhao, Hengshuang |
| Tahun | 2024 |
| Venue | Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [yang2024depth.pdf](../pdf/yang2024depth.pdf)
- DOI resmi: https://doi.org/10.1109/cvpr52733.2024.00987

## Gambaran Umum

Artikel ini memperkenalkan Depth Anything, model dasar untuk estimasi kedalaman monokular yang tangguh pada beragam citra. Masalah utamanya adalah estimasi kedalaman monokular belum memiliki model dasar karena membangun dataset berskala jutaan label kedalaman mahal, memakan waktu, atau tidak memungkinkan. Model sebelumnya seperti MiDaS memiliki kemampuan *zero-shot*, tetapi cakupan datanya terbatas sehingga kinerjanya menurun drastis pada beberapa skenario. Penulis tidak mengejar modul teknis baru; mereka memperbesar cakupan data dengan merancang mesin data yang mengumpulkan dan memberi anotasi otomatis pada citra tanpa label dalam skala besar. Kontribusi yang diklaim terdiri atas pemanfaatan citra tanpa label yang murah dan beragam, target optimasi yang lebih sulit saat mempelajari citra tanpa label, serta pewarisan prior semantik dari encoder terlatih.

Tanaman dan data pertanian tidak dinyatakan; data yang dipakai adalah citra dari delapan dataset publik tanpa label dan enam dataset berlabel. Mekanisme yang dibangun adalah estimasi kedalaman relatif, bukan deteksi atau asosiasi identitas, sehingga mekanisme deteksi atau asosiasi tidak dinyatakan. Dataset berlabel mencakup BlendedMVS, DIML, HRWSI, IRS, MegaDepth, dan TartanAir, dengan total 1,5 juta citra; dataset tanpa label mencakup BDD100K, Google Landmarks, ImageNet-21K, LSUN, Objects365, Open Images V7, Places365, dan SA-1B, dengan total 62 juta citra. Alur kerja terdiri atas pelatihan model guru pada data berlabel, pemberian label semu pada data tanpa label, lalu pelatihan model siswa pada gabungan keduanya. Untuk memanfaatkan data tanpa label, penulis menyuntikkan distorsi warna kuat dan CutMix dengan probabilitas 50% agar siswa mencari pengetahuan visual tambahan. Untuk mempertahankan kemampuan semantik, diterapkan *feature alignment loss* terhadap encoder DINOv2 yang dibekukan dengan margin toleransi α sebesar 0,85. Arsitektur memakai encoder DINOv2 dan decoder DPT, dengan tiga ukuran model, yaitu ViT-S (24,8 juta parameter), ViT-B (97,5 juta), dan ViT-L (335,3 juta). Fungsi rugi utama memakai *affine-invariant loss* pada ruang disparitas.

Hasil kuantitatif pada Tabel 2 memperlihatkan kinerja *zero-shot* estimasi kedalaman relatif pada enam dataset yang tidak terlihat saat pelatihan, dengan metrik AbsRel yang lebih rendah lebih baik dan δ1 yang lebih tinggi lebih baik. Dengan encoder ViT-L, model mencatat AbsRel 0,076 dan δ1 0,947 pada KITTI berbanding 0,127 dan 0,850 untuk MiDaS v3.1; 0,043 dan 0,981 pada NYUv2 berbanding 0,048 dan 0,980; 0,458 dan 0,760 pada Sintel berbanding 0,587 dan 0,699; 0,230 dan 0,789 pada DDAD berbanding 0,251 dan 0,766; 0,127 dan 0,882 pada ETH3D berbanding 0,139 dan 0,867; serta 0,066 dan 0,952 pada DIODE berbanding 0,075 dan 0,942. Setelah penyetelan halus pada data kedalaman metrik NYUv2 (Tabel 3), model mencatat δ1 0,984 dan AbsRel 0,056, mengungguli VPD yang mencatat 0,964 dan 0,069. Encoder yang dihasilkan juga lebih baik daripada encoder MiDaS pada segmentasi semantik ADE20K, dengan mIoU 59,4 berbanding 52,4 (Tabel 10).

Batasan yang dinyatakan penulis terutama berkaitan dengan skala model dan resolusi. Ukuran model terbesar masih dibatasi pada ViT-Large, sehingga pekerjaan lanjutan direncanakan memperbesar menjadi ViT-Giant untuk menghasilkan label semu yang lebih akurat bagi model kecil. Resolusi pelatihan 512×512 yang umum dipakai dinilai belum memadai untuk aplikasi dunia nyata, sehingga penulis merencanakan pelatihan ulang pada resolusi 700+ atau 1000+. Selain itu, penulis mencatat bahwa penambahan tugas segmentasi semantik diskrit tidak meningkatkan kinerja ketika model kedalaman sudah kuat, sehingga prior semantik dipertahankan lewat alignment fitur, bukan lewat kelas diskrit.

