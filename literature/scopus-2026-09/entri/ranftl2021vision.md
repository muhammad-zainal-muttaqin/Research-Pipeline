# Vision Transformers for Dense Prediction

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `ranftl2021vision` |
| Judul asli | Vision Transformers for Dense Prediction |
| Penulis | Ranftl, Rene; Bochkovskiy, Alexey; Koltun, Vladlen |
| Tahun | 2021 |
| Venue | Proceedings of the IEEE International Conference on Computer Vision |
| Kode | T (Metode dari luar pertanian) |

## Tautan Akses
- PDF: [ranftl2021vision.pdf](../pdf/ranftl2021vision.pdf)
- DOI resmi: https://doi.org/10.1109/iccv48922.2021.01196

## Gambaran Umum

Kajian ini mengatasi keterbatasan arsitektur jaringan konvolusional untuk tugas prediksi padat (*dense prediction*), seperti estimasi kedalaman monokuler dan segmentasi semantik. Arsitektur konvolusional melakukan *downsampling* bertahap untuk memperluas *receptive field*, tetapi proses itu menghilangkan resolusi dan butiran fitur pada tahap dalam yang sulit dipulihkan kembali oleh dekoder. Selain itu, konvolusi bersifat lokal dan memiliki *receptive field* terbatas, sehingga harus ditumpuk secara sangat dalam untuk memperoleh konteks global. Penulis berpendapat bahwa informasi yang hilang di encoder tidak dapat dikembalikan oleh dekoder, sehingga pilihan *backbone* menentukan batas kemampuan model.

Kajian ini bukan tentang tanaman; ia termasuk metode dari luar pertanian yang dapat ditransfer. Data yang dipakai mencakup meta-dataset MIX 6 untuk estimasi kedalaman, yang terdiri dari sekitar 1,4 juta gambar dan merupakan kumpulan data terbesar yang pernah disusun untuk tugas itu, serta perluasan dari MIX 5 dengan tambahan lima dataset. Untuk segmentasi semantik, penulis memakai ADE20K dan menyetel lanjut model pada Pascal Context. Penyetelan lanjut untuk kedalaman dilakukan pada NYUv2 dan KITTI. Arsitekturnya, bernama *dense prediction transformer* (DPT), memakai *encoder*–*dekoder* dengan *vision transformer* (ViT) sebagai *backbone*: ViT-Base dan ViT-Large memakai *patch embedding*, sedangkan ViT-Hybrid memakai ResNet50 sebagai pengekstrak fitur awal.

Mekanisme intinya memanfaatkan sifat transformer yang mempertahankan jumlah token dan memiliki *receptive field* global pada setiap tahap setelah *embedding* awal. Token-token dari berbagai tahap encoder disusun kembali menjadi representasi menyerupai gambar pada empat resolusi melalui operasi *Reassemble* yang terdiri dari *Read*, *Concatenate*, dan *Resample*. Penulis menguji tiga cara menangani token pembaca (*readout token*), yaitu mengabaikannya, menjumlahkannya ke token lain, dan memproyeksikannya; proyeksi dipakai sebagai bawaan. Peta fitur hasil penyusunan kemudian digabungkan dan di-*upsample* secara progresif oleh blok fusi berbasis RefineNet hingga resolusi setengah gambar, lalu kepala khusus tugas menghasilkan prediksi akhir. Dengan demikian, prediksi menjadi lebih butir dan lebih koheren secara global dibanding jaringan konvolusional.

Hasil yang dilaporkan menunjukkan peningkatan relatif rata-rata lebih dari 23% untuk DPT-Hybrid dan 28% untuk DPT-Large dibanding MiDaS pada pengujian transfer lintas dataset tanpa penyetelan ulang (*zero-shot*), dengan metrik AbsRel dan δ>1,25 yang dihitung menurut protokol Ranftl dkk. (Tabel 1). Pada ADE20K, DPT-Hybrid mencapai mIoU 49,02% dan akurasi piksel 83,11%, mengungguli arsitektur konvolusional sebanding (Tabel 4). Penyetelan lanjut pada Pascal Context memberi mIoU 60,46% (Tabel 5), sedangkan pada NYUv2 DPT-Hybrid memperoleh AbsRel 0,110 dan pada KITTI AbsRel 0,062 (Tabel 2 dan Tabel 3). Penulis juga melaporkan waktu inferensi 38 ms untuk DPT-Hybrid dan 35 ms untuk DPT-Large pada GPU RTX 2080, dibanding 32 ms untuk MiDaS (Tabel 9).

Batasan yang dinyatakan penulis adalah DPT mencapai potensi penuhnya hanya bila dilatih pada dataset berskala besar. Pada ADE20K, DPT-Large justru sedikit lebih rendah daripada DPT-Hybrid karena ukuran dataset jauh lebih kecil daripada percobaan sebelumnya. Penulis juga mencatat bahwa kinerja jaringan konvolusional menurun tajam bila inferensi dilakukan pada resolusi yang berbeda jauh dari resolusi latih, sementara DPT menurun lebih perlahan; hal ini dinyatakan sebagai dugaan yang diuji lewat plot penurunan kinerja, bukan klaim tanpa syarat. Selain itu, penulis menyatakan peningkatan per kelas pada ADE20K tidak menunjukkan pola yang kuat, dan perbaikan yang terjadi terutama berupa butiran yang lebih halus serta pengaturan kedalaman global yang lebih baik.

