# Advanced Machine Learning Method for Watermelon Identification and Yield Estimation †

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `farooq2025advanced` |
| Judul asli | Advanced Machine Learning Method for Watermelon Identification and Yield Estimation † |
| Penulis | Farooq, Memoona; Chen, Chih-Yuan; Wang, Cheng-Pin |
| Tahun | 2025 |
| Venue | Engineering Proceedings |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | melon |

## Tautan Akses
- PDF: [farooq2025advanced.pdf](../pdf/farooq2025advanced.pdf)
- DOI resmi: https://doi.org/10.3390/engproc2025108010

## Gambaran Umum

Kajian ini menguji deteksi dan penghitungan semangka (*watermelon*) dari video dengan YOLOv8 dan YOLOv8-OBB. YOLOv8 adalah keluarga detektor objek yang memprediksi kotak pembatas (*bounding box*) sumbu-tegak untuk setiap objek dalam satu citra. YOLOv8-OBB memprediksi kotak yang dapat diputar (*oriented bounding box*), sehingga bentuk buah yang miring lebih pas terlingkupi. Pelacak SORT (*Simple Online and Realtime Tracking*) memberi ID unik pada setiap buah dari frame ke frame, dan penghitungan dilakukan dengan mencatat buah yang pusat kotaknya melewati garis hitung.

Penelitian memakai video dengan resolusi 1280×746. Garis hitung ditulis sebagai koordinat [0, 550, 1920, 550]; garis ini mendatar pada y = 550. Dalam teks, ukuran piksel dikonversi ke sentimeter dengan rasio 7,88 piksel per cm untuk memperkirakan ukuran buah.

Model YOLOv8 dengan varian n, s, m, l, dan x dilatih 20 epoch dengan ukuran batch 16 dan laju pembelajaran 0,01 (untuk YOLOv8n). Model OBB dilatih 100 epoch dengan waktu pelatihan 0,112 jam. Metrik yang dilaporkan adalah mAP50, mAP50-95, dan presisi.

Hasil pada tabel YOLOv8 menunjukkan varian n memiliki mAP50-95 tertinggi (0,526) dan presisi tertinggi (0,915). Varian l memiliki mAP50 tertinggi (0,964). Pada tabel OBB, varian l memiliki mAP50-95 tertinggi (0,702), varian s memiliki presisi tertinggi (0,938), dan varian n memiliki mAP50 tertinggi (0,933). Kesimpulan teks menyebut presisi tertinggi dicapai oleh YOLOv8s-OBB dengan nilai 0,938. Tidak ada varian tunggal yang unggul pada semua metrik.

Kedua judul tabel memuat huruf "l" dua kali dalam daftar varian, yaitu "(m, n, l, s, x, and l)", sehingga daftar varian yang diuji perlu dicocokkan dengan isi tabel. Kajian ini juga tidak memisahkan galat deteksi dari galat pelacakan, karena metrik deteksi dan hasil hitung disajikan terpisah.

Dalam peta tinjauan, kajian ini termasuk kelompok penghitungan tanaman tunggal berbasis citra karena objeknya dihitung per buah dari video. Mekanisme asosiasinya adalah pelacakan temporal (SORT), bukan asosiasi lintas pandang yang menggabungkan beberapa kamera pada satu waktu.
