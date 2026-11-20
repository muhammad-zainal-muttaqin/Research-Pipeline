# Real-Time Detection of Ripe Oil Palm Fresh Fruit Bunch Based on YOLOv4

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lai2022real` |
| Judul asli | Real-Time Detection of Ripe Oil Palm Fresh Fruit Bunch Based on YOLOv4 |
| Penulis | Lai, Jin Wern; Ramli, Hafiz Rashidi; Ismail, Luthffi Idzhar; Hasan, Wan Zuha Wan |
| Tahun | 2022 |
| Venue | IEEE Access |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [lai2022real.pdf](../pdf/lai2022real.pdf)
- DOI resmi: https://doi.org/10.1109/access.2022.3204762

## Gambaran Umum

Lai dkk. (2022) membangun sistem deteksi tandan buah segar (TBS) matang pada pohon kelapa sawit secara real-time, memakai detektor YOLOv4 dan kamera RGB Intel RealSense D435. Sistem berjalan pada Nvidia Jetson NX, dan posisi buah dikirim ke robot melalui ROS. Model dilatih pada 490 citra dari 49 pohon di Selangor, Malaysia, dan diuji lapangan pada 20 pohon di Carey Island. Pada uji lapangan, model mencapai mAP 87,9%, average IoU 70,19%, dan kecepatan rata-rata 21 bingkai per detik.

Kajian ini hanya mendeteksi buah matang. Ia tidak mengukur jumlah tandan per pohon atau per tanaman, dan tidak membahas identitas buah lintas sudut pandang.

Penentuan waktu panen TBS di kebun sawit masih dilakukan dengan pengamatan manusia. Penulis menyebut bahwa sistem deteksi otomatis diperlukan untuk robot pemanen yang harus menemukan buah matang pada pohon. Sebelum kajian ini, pendekatan yang tersedia belum dinilai pada buah sawit yang diambil langsung di kebun (Lai dkk. 2022, bagian Pendahuluan).

Gagasan utama adalah menerapkan YOLOv4 apa adanya pada citra TBS matang, tanpa mengubah arsitektur. Penulis menyatakan bahwa hasil yang layak diperoleh dari metodologi dan hiperparameter yang dipilih untuk pelatihan (Lai dkk. 2022, Kesimpulan). Dengan kata lain, kontribusinya ada pada data, pelabelan, dan pemilihan iterasi, bukan pada desain detektor.

Citra direkam dengan kamera pada ketinggian buah, sekitar 3 meter dari tandan, dengan resolusi 1920 × 1080 piksel. Dari 49 pohon, 24 memiliki setidaknya satu tandan matang dan 25 tidak memiliki tandan matang. Dari video, dipilih 10 citra per pohon agar tidak redundan. Total 240 citra positif dan 250 citra negatif dipakai, lalu dibagi menjadi 210 dan 30 citra positif untuk pelatihan dan validasi, serta 220 dan 30 citra negatif. Pelabelan dilakukan manual dengan labelImg. Citra dari satu pohon tidak boleh muncul di pelatihan dan validasi sekaligus.

Parameter memakai nilai bawaan YOLOv4. Augmentasi meliputi exposure dan saturation 1,5, hue 0,1, dan Mosaic. Penulis menilai performa setiap 1.000 iterasi. Presisi validasi mencapai 86% pada 1.000 iterasi dan 100% pada 2.000 iterasi ke atas, tetapi penulis menganggap hasil 3.000 iterasi sebagai tanda overfitting. Model 2.000 iterasi dipilih.

Empat varian dibandingkan: YOLOv4, YOLOv4-CSP, YOLOv4-tiny, dan YOLOv4-tiny dengan dua ukuran masukan (512 dan 608). YOLOv4 dan YOLOv4-CSP memberi mAP tertinggi. YOLOv4-tiny memberi 48,89% (512) dan 55,60% (608) (Lai dkk. 2022, Tabel 5). Pada validasi, presisi, recall, dan F1 YOLOv4 disebut sekitar 97%. Angka ini berasal dari set validasi yang sama dengan tahap pemilihan iterasi, sehingga tidak independen.

Uji lapangan dilakukan pada 20 pohon: 10 pohon hanya berisi tandan belum matang dan 10 pohon memiliki minimal satu tandan matang. Hasil uji lapangan YOLOv4 adalah mAP 87,9%, average IoU 70,19%, recall 82%, dan F1 88% (Lai dkk. 2022, Tabel 6 dan Kesimpulan). Kecepatan rata-rata 21 bingkai per detik dilaporkan sebagai bukti deteksi real-time.

Kajian ini menyediakan angka uji lapangan terpisah dari data pelatihan, dan membandingkan empat varian YOLOv4 pada data yang sama. Pelaporan kecepatan dan ukuran berkas bobot juga memungkinkan penilaian kebutuhan perangkat di kebun.

Pertama, data hanya dari satu kebun, satu periode perekaman, dan satu jenis kamera. Kedua, pelabelan dan pelatihan hanya memakai buah matang, sehingga kelas belum matang tidak dilatih. Ketiga, tidak ada evaluasi jumlah tandan per pohon. Dari sisi rekayasa, angka uji lapangan dihitung pada 20 pohon, sehingga variasinya belum dapat diukur.
