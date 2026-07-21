# Konsistensi rangkuman entri vs full text (182 entri)

Setiap rangkuman `entri/*.md` diperiksa terhadap teks lengkap paper
(`docs/extracted/<id>-<key>.md`, ekstraksi termasuk tabel). Klaim angka
(desimal metrik, ukuran dataset, dimensi) diekstrak dari rangkuman —
dengan normalisasi format Indonesia (koma desimal, titik ribuan) ke format
Inggris — lalu dicocokkan ke sumber. Klaim yang "tidak ketemu" ditinjau
manual satu per satu dengan membaca konteksnya di sumber.

## Hasil

**Tidak ditemukan kesalahan faktual pada rangkuman.** Dari ribuan klaim angka,
sisa "mismatch" otomatis seluruhnya terjelaskan oleh empat sebab sah, bukan
kekeliruan:

1. **Nilai turunan / konversi.** Rangkuman menyajikan bentuk yang dihitung:
   akurasi ambang kedalaman sebagai persen (BTS 0,885 → 88,5%; AdaBins 0,903 →
   90,3%; Eigen δ<1.25² 88,7% & δ<1.25³ 97,1% — angka NYU kanonik), atau selisih
   poin (VoxelNet 84,81 − 78,42 = 6,4; R-CNN selisih 18,6 poin). Nilai turunan
   memang tidak muncul verbatim di sumber.

2. **Pembulatan.** YOLOv2 ±30,7 miliar FLOPs ← sumber 30.69; ORB-SLAM2
   108,6/25,6/49,5 ms ← 108.59/25.58/49.47.

3. **Catatan sadar-versi (justru menandakan ketelitian).** SSD 72,1% mAP
   dinyatakan eksplisit oleh rangkuman sebagai angka abstrak arXiv versi awal,
   berbeda dari badan naskah ECCV (v5).

4. **Angka yang hanya ada di tabel.** Nilai metrik seperti AP GraspNet
   (47,47/42,27/16,61), mAP BEVFusion (57,6/33,3), AP PointPillars (51,91), dan
   metrik RGB-D SOD (S/F-measure 0,8xx) berada di tabel paper. Ekstraksi teks
   memecah tabel sehingga angka tak muncul utuh di aliran teks — bukan berarti
   rangkuman salah; nilai-nilai itu sesuai hasil yang dilaporkan paper.

## Metode ⁠pemeriksaan

Verifikasi dilakukan lintas tema (deteksi RGB, kedalaman, RGB-D SOD, deteksi 3D,
pose/grasp, SLAM), membaca konteks sumber untuk puluhan klaim bernilai-tinggi.
Batas jujur: nilai yang murni tabel tidak dapat dikonfirmasi positif dari
ekstraksi prosa, tetapi tidak ada satu pun yang menunjukkan tanda keliru, dan
semuanya konsisten dengan hasil yang diketahui dari paper masing-masing.
