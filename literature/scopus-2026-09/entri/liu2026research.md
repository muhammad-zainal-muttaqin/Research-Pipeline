# RESEARCH ON A TOMATO RIPENESS DETECTION METHOD BASED ON CMLE-YOLO

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `liu2026research` |
| Judul asli | RESEARCH ON A TOMATO RIPENESS DETECTION METHOD BASED ON CMLE-YOLO |
| Penulis | Liu, Shuo; Hou, Pengzhi; Deng, Linqiang; Cheng, Lijun; Lv, Jia |
| Tahun | 2026 |
| Venue | Inmateh Agricultural Engineering |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | tomato |

## Tautan Akses
- PDF: [liu2026research.pdf](../pdf/liu2026research.pdf)
- DOI resmi: https://doi.org/10.35633/inmateh-78-62

## Gambaran Umum

Penentuan kematangan panen tomat yang tidak tepat menyebabkan pematangan tidak merata, kematangan berlebih, pembusukan, dan kerusakan akibat pelunakan selama transportasi, sehingga menimbulkan kerugian pascapanen yang besar. Penelitian ini bertujuan menyediakan dasar objektif untuk klasifikasi kematangan dan pencacahan buah melalui model ringan bernama CMLE-YOLO. Deteksi otomatis dalam lingkungan produksi nyata sulit karena buah tomat berukuran kecil, tersebar rapat, dan sering tertutup daun, batang, serta buah tetangga. Di rumah kaca, pencahayaan tidak merata, latar yang berantakan, dan pantulan spekular memperparah kesulitan. Tahap kematangan yang berdekatan memiliki perbedaan visual halus, sehingga tugas ini menjadi deteksi butir halus (*fine-grained*), bukan sekadar pelokalan buah.

Data dikumpulkan di lahan percobaan Universitas Pertanian Shanxi menggunakan kamera DSLR Canon EOS 70D dengan lensa EF-S 18–135 mm f/3,5–5,6 IS STM pada resolusi asli 5472×3648 piksel. Citra diambil pada cahaya siang alami, pagi dan sore, tanpa pengukuran intensitas cahaya secara kuantitatif; tidak ada citra malam maupun pencahayaan buatan. Dari 2.100 citra mentah, 2.000 citra lolos penyaringan setelah penghapusan citra kabur dan sampel dengan target hilang. Anotasi manual dengan LabelImg menghasilkan 8.593 buah dalam tiga kelas, yaitu *fully_ripened*, *half_ripened*, dan *green*, dalam format YOLO. Data dibagi untuk latih, validasi, dan uji dengan rasio 8:1:1. Augmentasi daring meliputi pembalikan citra, perubahan rona, saturasi, kecerahan, dan *mosaic*. Pelatihan memakai 200 epoch, ukuran batch 16, laju pembelajar awal 0,01 dengan optimisator SGD, ukuran masukan 640, ambang IoU 0,7, serta pemanasan laju pembelajar selama tiga epoch awal.

CMLE-YOLO dibangun di atas YOLOv11n dengan dua perubahan utama. Modul *Cross-Fusion and Multi-scale Attention* (CFMA) menggantikan blok C3k2 di *backbone* dan *neck*. Modul ini memakai FEM-Block yang terdiri dari PConv (*Partial Convolution*) pada sebagian saluran untuk menekan beban hitung, MLP berbasis konvolusi 1×1 untuk ekspansi dan kompresi saluran, serta perhatian EMA pada cabang residual, dengan koneksi residual dan DropPath. Mekanisme ini memperkuat interaksi lintas skala dan pemodelan konteks global agar model memusat perhatian pada buah dan menekan gangguan latar. Kepala deteksi *Lightweight Quality-Aware Detection Head* (LQAD) terdiri dari Conv_GN (konvolusi, GroupNorm, SiLU), struktur konvolusi bersama ringan (LSCS) yang menyatukan pemetaan lintas skala, serta *Localization Quality Estimator* (LQE). LQE memanfaatkan distribusi regresi dari *Distribution Focal Loss* untuk membentuk nilai kualitas yang mengoreksi skor klasifikasi, sehingga skor mencerminkan keyakinan kelas sekaligus kualitas pelokalan dan peringkat kotak pada NMS lebih andal. Model diuji pada GPU NVIDIA GeForce RTX 4080 dengan PyTorch 2.x dan CUDA 12,9.

Pada himpunan validasi, CMLE-YOLO mencapai mAP@50 0,8508 dan mAP50–95 0,6905, dengan presisi 0,7851, recall 0,7893, dan F1 0,7872. Angka itu mengungguli YOLOv5 (0,8291), YOLOv6 (0,8279), YOLOv8 (0,8172), YOLOv10 (0,8225), dan YOLOv11 (0,8219) pada mAP@50; nilai mAP50–95 sebanding dengan YOLOv6 (0,6905). Uji ablasi menunjukkan mAP@50 naik dari 0,8219 pada YOLOv11n menjadi 0,8320 dengan CFMA, 0,8410 dengan LQAD, dan 0,8508 dengan keduanya, sementara jumlah parameter turun dari 2,58 juta menjadi 2,13 juta dan beban hitung dari 6,2 menjadi 5,2 GFLOPs. Kecepatan inferensi tercatat 213,5 FPS. Metrik dihitung dengan P = TP/(TP+FP), R = TP/(TP+FN), dan mAP@0,5 sebagai rata-rata AP lintas kelas pada IoU 0,5; AP per kelas berturut-turut adalah 0,887 (*fully_ripened*), 0,800 (*half_ripened*), dan 0,885 (*green*), dengan ambang keyakinan 0,513 pada F1 0,80. Pada tugas pencacahan, selisih hitungan otomatis terhadap anotasi manual berturut-turut adalah 3, 5, dan 9 buah untuk *fully_ripened*, *half_ripened*, dan *green*.

Penulis menyatakan batasan berupa salah klasifikasi yang masih terjadi antar tahap kematangan berdekatan, terutama antara *half_ripened* dan *fully_ripened* atau *green*, karena transisi warna dan tekstur yang bertahap. Kinerja juga terpengaruh perubahan pencahayaan mendadak, oklusi parah, dan kemiripan buah dengan latar. Informasi RGB saja dianggap belum cukup pada sebagian skenario menantang. Penulis menyarankan kerja lanjutan berupa perluasan varietas, musim, kondisi pencahayaan, dan latar, representasi invarian iluminasi, pelatihan adaptasi domain, serta evaluasi lintas-domain dan uji penerapan perangkat keras jangka panjang.
