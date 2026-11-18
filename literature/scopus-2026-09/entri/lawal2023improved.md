# An improved YOLOv5s model using feature concatenation with attention mechanism for real-time fruit detection and counting

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `lawal2023improved` |
| Judul asli | An improved YOLOv5s model using feature concatenation with attention mechanism for real-time fruit detection and counting |
| Penulis | Lawal, Olarewaju Mubashiru; Zhu, Shengyan; Cheng, Kui |
| Tahun | 2023 |
| Venue | Frontiers in Plant Science |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [lawal2023improved.pdf](../pdf/lawal2023improved.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2023.1153505

## Gambaran Umum

Kajian ini bertujuan membangun model deteksi buah yang ringan, cepat, dan dapat dijalankan pada perangkat berdaya rendah untuk robot pemanen. Permasalahan yang diangkat adalah deteksi buah di lingkungan kompleks yang dipengaruhi pencahayaan tidak merata, penutupan oleh daun, serta buah yang tampilan visualnya mirip latar belakang. Penulis menambahkan penggabungan fitur dan mekanisme perhatian pada YOLOv5s untuk meningkatkan akurasi sekaligus menekan jumlah parameter dan biaya komputasi.

Objek kajian adalah stroberi (*Fragaria ananassa*) dan jujube (*Ziziphus jujuba*). Citra diambil di rumah kaca wanghaizhuang, Houcheng, Jinzhong, dan Kebun Pemetikan Kurma Gaolang, Linxian, Luliang, Provinsi Shanxi, Tiongkok, dengan kamera digital Huawei mate30pro dan mate40pro beresolusi 3968 × 2976, 1904 × 4096, serta 2736 × 3648 piksel. Pengambilan dilakukan pagi, siang, dan sore dengan jarak serta sudut yang berubah-ubah, sehingga citra memuat penutupan daun, tumpang tindih buah, penutupan cabang, kemiripan dengan latar, sasaran rapat, dan berbagai arah cahaya. Total citra adalah 1.350 stroberi dan 1.959 jujube. Pembagian acak 80% latih, 15% validasi, dan 5% uji menghasilkan 2.651, 491, dan 167 citra. Kotak anotasi berjumlah 9.321 untuk stroberi dan 13.470 untuk jujube, dengan rincian 18.496 pada latih, 3.232 pada validasi, dan 1.063 pada uji. Anotasi dibuat dengan labelImg dan disimpan dalam format teks YOLO. Video mp4 juga direkam untuk menguji kecepatan deteksi, ketahanan, dan penghitungan.

Mekanisme utama adalah modifikasi arsitektur YOLOv5s. Skala adaptif dinaikkan menjadi 1,0 untuk kedalaman dan lebar; anchor dihitung dengan k-means clustering; jumlah peta fitur downsampling dikurangi dari lima menjadi empat. Jaringan Stem menggantikan lapisan konvolusi pertama, jaringan AC yang menggabungkan CBS 1 × 1, CBS 3 × 3, dan coordinate attention mechanism (CAM) menggantikan lapisan 1, 3, dan 5, Maxpool menggantikan lapisan 2, 4, dan 6, serta CBS, SPPF, dan CAM menggantikan lapisan 7, 8, dan 9. Modul C3 pada PANet diganti CBS 1 × 1 dan jumlahnya dipangkas menjadi satu. Kepala model menghasilkan peta fitur 160 × 160, 80 × 80, dan 40 × 40, dibandingkan 80 × 80, 40 × 40, dan 20 × 20 pada model awal. Deteksi memakai NMS untuk membuang kotak ganda dan fungsi rugi CIoU. Pelatihan memakai citra 640 × 640, batch 16, momentum 0,937, weight decay 0,0005, IoU 0,2, dan 300 epoch dari inisialisasi acak pada Ubuntu 22.04, Intel Core i7-12700, RTX 3060, Python 3.9.12, dan PyTorch 1.11.0+cu113. Penghitungan buah dilakukan dengan melacak setiap kelas buah terlebih dahulu, lalu menghitung kotak hasil deteksi.

Hasil utama membandingkan model yang diperbaiki terhadap YOLOv5s awal. Model yang diperbaiki memiliki 122 lapisan, 4,4 × 10⁶ parameter, 12,8 GFLOPs, dan ukuran bobot 8,8 MB, masing-masing 45,5%, 30,2%, 14,1%, dan 31,3% lebih kecil. Nilai mAP pada himpunan validasi naik dari 92,8% menjadi 93,4% dan pada himpunan uji dari 95,5% menjadi 96,0%, sedangkan kecepatan naik dari 67 fps menjadi 74 fps, atau 10,4%. F1 validasi naik dari 89,7% menjadi 90,2% dan F1 uji dari 91,4% menjadi 92,5%. Pada penghitungan, model yang diperbaiki mencatat 419 kotak stroberi dan 693 kotak jujube pada himpunan uji, dengan deteksi terlewat 1,64% berbanding 3,52% dan deteksi salah 8,79% berbanding 11,62% pada model awal. Pada video, jumlah stroberi terhitung 6.292 berbanding 6.098. Studi ablasi menunjukkan kombinasi penggabungan fitur, mekanisme perhatian, dan PANet memberi kinerja tertinggi; perbandingan lain menunjukkan model ini mengungguli GhostYOLOv5s, YOLOv4-tiny, dan YOLOv7-tiny.

Batasan yang dinyatakan penulis adalah masih adanya deteksi terlewat dan deteksi salah, serta kondisi jujube yang lebih kompleks daripada stroberi sehingga kurva presisi-recallnya lebih rendah. Penulis juga menyatakan bahwa penurunan skala adaptif lebih lanjut dapat mengurangi parameter dan biaya komputasi, tetapi kemungkinan menurunkan akurasi, dan menganjurkan pengujian pada jaringan leher serta fungsi rugi lain pada penelitian berikutnya.

