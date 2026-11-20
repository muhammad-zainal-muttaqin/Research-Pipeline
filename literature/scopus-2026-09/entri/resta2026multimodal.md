# Multimodal Radar-Vision for Oil Palm Fresh Fruit Bunch Ripeness Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `resta2026multimodal` |
| Judul asli | Multimodal Radar-Vision for Oil Palm Fresh Fruit Bunch Ripeness Classification |
| Penulis | Resta, Firdausa Sonna Anggara; Setiawan, Rachmad; Rivai, Muhammad; Arif, Rezki El; Natawijaya, Azis; Hadad, Afan Ghafar Al |
| Tahun | 2026 |
| Venue | IEEE Access |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [resta2026multimodal.pdf](../pdf/resta2026multimodal.pdf)
- DOI resmi: https://doi.org/10.1109/access.2026.3675310

## Gambaran Umum

Penentuan tingkat kematangan tandan buah segar (TBS) kelapa sawit sebelum panen masih banyak dilakukan secara manual. Pekerja memeriksa warna buah dan menghitung brondolan yang jatuh ke tanah. Cara ini padat karya dan sangat bergantung pada pengalaman pekerja, sehingga penilaian sering tidak konsisten. Kondisi itu dapat menyebabkan waktu panen yang kurang tepat dan menurunkan efisiensi ekstraksi minyak. Kajian ini mengusulkan kerangka klasifikasi kematangan multimodal yang menggabungkan informasi radar dengan keluaran *computer vision*. Tujuannya adalah membuat penilaian kematangan lebih objektif, cepat, dan stabil di lingkungan perkebunan yang nyata.

Data dikumpulkan pada satu prototipe sistem sensing yang berisi radar gelombang kontinu 2,4 GHz, timbangan digital, dan kamera RGB. Pengukuran radar, berat, dan citra dilakukan berurutan dalam satu sesi penanganan yang sama agar kondisi lingkungan dan geometri tetap seragam. Data radar-berat diambil di sebuah *loading ramp* komersial dan berjumlah 255 sampel per kelas. Empat kelas kematangan yang digunakan adalah *Unripe*, *Underripe*, *Ripe*, dan *Overripe*. Pakar memberi label pada setiap citra berdasarkan warna brondolan dan jumlah buah lepas. Model deteksi YOLOv8-Nano dilatih dengan augmentasi geometris dan fotometrik, seperti pembalikan, rotasi, penskalaan, *shear*, serta perubahan kecerahan dan saturasi. Kajian tidak menyebutkan rincian pembagian data latih dan data uji pada bagian yang dibaca.

Metode terdiri dari dua cabang. Cabang radar-berat memakai XGBoost dengan tiga fitur per tandan: rata-rata daya hamburan radar (dB), berat tandan (kg), dan rasio daya terhadap berat (dB/kg). Cabang citra memakai YOLOv8-Nano yang menghasilkan *bounding box*, label kelas, dan probabilitas kelas. Kedua keluaran probabilitas digabung dengan *late fusion* pada tingkat keputusan melalui skema rata-rata, berbobot, dan *stacking*. Hasil pengujian menunjukkan model radar-berat mencapai akurasi 89,9%, sedangkan model citra mencapai akurasi 94,3%. YOLOv8-Nano memperoleh mAP@0,5 sebesar 0,99. Konfigurasi fusi terbaik, yaitu *stacking*, mencapai akurasi 96,9% dan F1-macro 97,3%. Penulis menyimpulkan bahwa informasi radar-berat memberi bukti pelengkap yang menstabilkan penilaian berbasis citra.

Penulis menyatakan bahwa ukuran data yang terbatas dan sifat kedua modalitas yang berbeda menjadi pertimbangan utama. Karena itu, mereka memilih *late fusion* dibanding *early fusion* atau *middle fusion*. Pendekatan yang lebih terpadu dinilai berisiko menimbulkan ketidakstabilan optimasi dan *overfitting*. Batasan ini menunjukkan bahwa hasil kajian berlaku pada kondisi data yang tercantum dan perlu diuji lebih lanjut pada skala data yang lebih besar.
