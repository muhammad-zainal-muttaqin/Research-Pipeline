# Precise Tomato Ripeness Estimation and Yield Prediction using Transformer Based Segmentation-SegLoRA

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `pisharody2025precise` |
| Judul asli | Precise Tomato Ripeness Estimation and Yield Prediction using Transformer Based Segmentation-SegLoRA |
| Penulis | Pisharody, Sidharth N; Duraisamy, Palmani; Rangarajan, Aravind Krishnaswamy; Whetton, Rebecca L.; Herrero-Langreo, Ana |
| Tahun | 2025 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [pisharody2025precise.pdf](../pdf/pisharody2025precise.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2025.110172

## Gambaran Umum

Penelitian ini membahas penilaian tingkat kematangan tomat (*Solanum lycopersicum*) yang akurat di lapangan. Kematangan menentukan mutu, nilai pasar, dan kepuasan konsumen. Metode berbasis warna dan jaringan konvolusi (CNN) sering tidak stabil ketika pencahayaan berubah, terutama di lahan terbuka. CNN juga membutuhkan pelatihan yang panjang karena seluruh parameter model harus disetel ulang, dan kurang baik dalam menangkap konteks global. Penulis mengusulkan kerangka segmentasi yang menggabungkan arsitektur *SegFormer* dengan modul *Low-Rank Adaptation* (SegLoRA). Tujuannya adalah segmentasi yang lebih akurat, lebih efisien, dan dapat dijalankan secara waktu nyata pada perangkat *edge computing* untuk mendukung panen selektif.

Data terdiri atas 4.206 citra tomat yang dikumpulkan dengan kamera ponsel pintar. Sebanyak 1.750 citra rumah kaca berasal dari kumpulan data publik "Real-world Tomato Image Dataset", dengan resolusi 1846 × 4000 piksel. Sebanyak 2.456 citra lain diambil di lahan pertanian terbuka dengan resolusi 4080 × 2296 piksel, dengan kondisi pencahayaan yang bervariasi. Standar USDA yang memuat enam tahap kematangan digabungkan menjadi empat kelas: ML-1 hingga ML-4. Kelas intermediat dibentuk dari tahap *breaker*, *turning*, dan *pink*, yang belum siap panen. Anotasi dibuat dengan alat Roboflow dan dikonsultasikan dengan petani serta pakar. Data dibagi secara acak menjadi 2.945 citra latih, 839 citra validasi, dan 422 citra uji, dengan rasio 7:2:1. Augmentasi hanya diterapkan pada data latih, sehingga jumlahnya menjadi 5.890 citra. Augmentasi mencakup rotasi 90 derajat, perubahan kecerahan ±15 %, dan *Gaussian blur* dengan radius hingga 2,5 piksel.

Model SegFormer varian MiT B0 hingga MiT B5 dilatih dan dibandingkan dengan UNET dan DeepLab V3. Varian MiT B4 memberikan hasil terbaik. Model dilatih selama 19 epoch, dan setelah itu performanya tidak lagi membaik. Pada hasil terbaik, mIoU mencapai 83,25 %, F1-score 90,07 %, akurasi uji 99,19 %, dan akurasi seimbang 93,88 %. Biaya komputasi turun 26,98 % dibandingkan model SegFormer yang ada. Parameter yang dapat dilatih hanya 5,75 % untuk varian B4. Pada data uji, nilai TP untuk ML-1, ML-3, dan ML-4 berturut-turut 0,929, 0,922, dan 0,972. Nilai TP untuk ML-2 hanya 0,627, dan 0,287 instans ML-2 salah diklasifikasikan sebagai ML-1. Pada perangkat *edge computing*, waktu prediksi rata-rata 0,065 detik per bingkai. Keluaran segmentasi ditumpangkan pada aliran video, dan jumlah tomat yang dapat dipanen dihitung dengan algoritma estimasi hasil. Penulis menyatakan bahwa metode ini memungkinkan penghitungan tomat yang tepat.

Penulis menyebut bahwa model paling sering keliru pada kelas ML-2, terutama dengan ML-1 dan ML-3, karena variasi warna yang halus. Pada citra uji tertentu, UNET juga keliru pada ML-1 karena warna daun yang mirip dengan tomat. Kumpulan data ini relatif kecil untuk model transformer, dan hasil di lahan terbuka bergantung pada kondisi pencahayaan dan oklusi. Penulis menekankan bahwa kinerja pada kelas ML-2 masih perlu diperbaiki. Pengujian dilakukan pada perangkat keras tertentu, sehingga hasil waktu prediksi berlaku untuk konfigurasi tersebut.
