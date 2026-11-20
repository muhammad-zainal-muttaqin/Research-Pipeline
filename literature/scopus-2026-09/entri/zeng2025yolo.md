# YOLO-FCAP: An improved lightweight object detection model based on YOLOv8n for citrus yield prediction in complex environments

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zeng2025yolo` |
| Judul asli | YOLO-FCAP: An improved lightweight object detection model based on YOLOv8n for citrus yield prediction in complex environments |
| Penulis | Zeng, Tiwei; Tong, Jintao; Sun, Xudong; Liu, Jiacheng; He, Xiangguo; Guan, Zhenzhen; Liu, Lingfeng; Jiang, Nan; wan, Tao |
| Tahun | 2025 |
| Venue | Smart Agricultural Technology |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [zeng2025yolo.pdf](../pdf/zeng2025yolo.pdf)
- DOI resmi: https://doi.org/10.1016/j.atech.2025.101590

## Gambaran Umum

Kajian ini membahas perkiraan hasil panen jeruk di kebun yang kompleks. Buah dan daun saling menutupi di kebun, sementara perangkat *edge* memiliki kemampuan komputasi yang terbatas. Menurut penulis, model deteksi yang akurat sekaligus ringan masih sulit dicapai. Karena itu, mereka mengusulkan YOLO-FCAP, model deteksi ringan berbasis YOLOv8n, untuk mencacah buah dan memperkirakan hasil panen kebun.

Penelitian dilakukan di kebun Ganzhou Citrus Scientific Research Institute, Provinsi Jiangxi, Tiongkok, dengan jeruk navel Gannan sebagai objek. Foto diambil dengan kamera belakang ponsel Redmi K60 dan iPhone 16 pada resolusi 3000 × 4000. Pengambilan gambar dilakukan dari sudut horizontal, sudut rendah, dan sudut atas, pada jarak 50 cm sampai 250 cm, dalam berbagai kondisi cahaya. Dua sampel pohon dipotret, yaitu buah jingga-kuning pada 9 Desember 2024 dan buah hijau pada 13 Oktober 2024. Setelah penyaringan citra duplikat dan citra buram, kedua set data berisi 5816 citra jeruk. Data diberi label tunggal NAO dengan *bounding box* menggunakan LabelImg. Setelah augmentasi pada citra buah hijau, jumlahnya menjadi 4616 citra tahap matang dan 2400 citra tahap muda, sehingga totalnya 7016 sampel. Setiap tahap kematangan dibagi dengan rasio 7:1:2 untuk data latih, validasi, dan uji. Augmentasi *mosaic* diterapkan pada data latih.

Model YOLO-FCAP memiliki empat modifikasi. Skala jaringan *pico* dipakai untuk mengurangi redundansi. Seluruh modul C2F diganti dengan FasterNetBlockWithCA. Tiga blok *downsampling* terakhir pada *backbone* diganti dengan modul ADown. Lapisan deteksi objek kecil ditambahkan untuk buah kecil dan tertutup. Hasil pada data jeruk menunjukkan parameter 0,81 M dan FLOPs 5,5 G, dengan ukuran penyimpanan 1,95 MB. Model mencapai *precision* 90,4 %, *recall* 84,3 %, dan *average precision* 92,5 %, serta kecepatan 168,42 bingkai per detik. Penulis juga membuat persamaan regresi linear yang memetakan jumlah buah hasil prediksi YOLO ke jumlah sebenarnya. Persamaan tersebut menghasilkan R² 0,983, MAE 0,95, dan RMSE 1,20. Menurut penulis, performa keseluruhan model lebih baik daripada model deteksi objek lain yang dibandingkan.

Penulis menyatakan beberapa batasan. Sebagian kesalahan deteksi berupa objek yang hilang akibat penutupan sebagian atau seluruh buah. Karena citra hanya diambil dengan kamera ponsel, sudut pandang yang tersedia terbatas. Pengujian juga dilakukan pada kondisi yang relatif ideal. Hujan dan kabut belum diuji, padahal keduanya dapat menurunkan kejelasan citra. Selain itu, data hanya mencakup sebagian varietas jeruk, sehingga cakupan seluruh varietas belum tercapai.

Penulis menutup dengan menyatakan bahwa YOLO-FCAP dapat diterapkan pada perangkat *edge* dan mendukung perencanaan kebun pada berbagai tahap. Penulis juga menyarankan pengambilan citra dari berbagai sudut untuk mengurangi deteksi yang terlewat.
