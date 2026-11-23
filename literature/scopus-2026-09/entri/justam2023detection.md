# Detection and Counting of the Number of Cocoa Fruits on Trees Using UAV

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `justam2023detection` |
| Judul asli | Detection and Counting of the Number of Cocoa Fruits on Trees Using UAV |
| Penulis | Justam; Indrabayu; Zainuddin, Zahir; Basri |
| Tahun | 2023 |
| Venue | Proceedings of the 2023 IEEE International Conference on Industry 4 0 Artificial Intelligence and Communications Technology Iaict 2023 |
| Kode | C2 (Pencacahan satu pandang) |

## Tautan Akses
- PDF: [justam2023detection.pdf](../pdf/justam2023detection.pdf)
- DOI resmi: https://doi.org/10.1109/iaict59002.2023.10205752

## Gambaran Umum

Penelitian ini bertujuan mengenali dan mencacah buah kakao pada pohon dengan citra dari *Unmanned Aerial Vehicle* (UAV, pesawat tanpa awak). Masalah utama yang disebut penulis adalah memperkirakan hasil panen dari buah kakao yang saling menumpuk. Penulis mengusulkan algoritme yang memisahkan buah tunggal, buah tertutup sebagian, dan buah yang saling tumpang tindih sebelum dicacah.

Data berupa rekaman video dari UAV yang terbang di antara barisan pohon kakao dengan jarak antarpohon rata-rata 3 meter, pada cuaca cerah. Citra diambil dari kebun rakyat dengan posisi, jarak, dan sumber cahaya yang berbeda. Jumlah video, citra, pohon, dan buah tidak disebut. Pemberi label dan pembagian latih/uji tidak disebut, karena metode tidak dilatih.

Metodenya berupa rangkaian pengolahan citra klasik. Citra diperhalus dengan tapis Gaussian 3x3, lalu dipisahkan dari latar dengan *thresholding* (pemisahan piksel berdasarkan ambang kecerahan) otomatis metode Otsu pada ruang warna YCbCr. Kontur objek dicari dengan `findContours()` OpenCV. Kebulatan (*roundness*) 0,7 sampai 0,9 dianggap buah tunggal, dan 0,4 sampai 0,7 dianggap area tumpang tindih atau tertutup. Area tumpang tindih dipisahkan dengan transformasi jarak (*distance transform*, peta jarak tiap piksel ke tepi objek) dan ambang adaptif berdasarkan jumlah tepi.

Abstrak menyebut akurasi deteksi 94,5% setelah analisis tumpang tindih. Angka itu tidak muncul di bagian hasil. Hasil yang dilaporkan hanya satu citra dengan 20 buah menurut hitung tangan. Empat ambang menghasilkan 15, 16, 17, dan 20 buah terdeteksi, dengan *recall* 0,75; 0,80; 0,85; dan 1,0. *Precision* bernilai 1 pada semua ambang karena tidak ada *false positive*.

Keterbatasan yang dapat diperiksa: evaluasi hanya satu citra, ambang keempat dipilih setelah hasil hitung tangan diketahui, dan tidak ada data uji terpisah. Pembagian per pohon tidak ada. Penulis menyebut sistem gagal pada buah yang terlalu buram atau terlalu kecil. Citra tidak digabung antarpandang, sehingga tiap citra dicacah sendiri.
