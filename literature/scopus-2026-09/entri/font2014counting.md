# Counting red grapes in vineyards by detecting specular spherical reflection peaks in RGB images obtained at night with artificial illumination

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `font2014counting` |
| Judul asli | Counting red grapes in vineyards by detecting specular spherical reflection peaks in RGB images obtained at night with artificial illumination |
| Penulis | Font, D.; Pallej\`a, T.; Tresanchez, M.; Teixid\'o, M.; Martinez, D.; Moreno, J.; Palac\'\in, J. |
| Tahun | 2014 |
| Venue | Computers and Electronics in Agriculture |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [font2014counting.pdf](../pdf/font2014counting.pdf)
- DOI resmi: https://doi.org/10.1016/j.compag.2014.07.006

## Gambaran Umum

Kajian ini menghitung anggur merah (*red grapes*) dari citra yang diambil di kebun pada malam hari. Penulis memakai kamera Nikon D300s dengan lensa 20 mm, lampu cincin (*ring flash*) sebagai sumber cahaya buatan, dan kendaraan yang bergerak 0,25 m/s pada jarak sekitar 2 m dari tanaman. Setiap gambar diproses sebagai satu pandang tunggal, sehingga hitungan dilakukan per citra tanpa menggabungkan hasil antargambar.

Segmentasi memakai ambang Otsu pada lapisan *hue* yang sudah ditransformasi, dengan filter rata-rata radius 10 piksel. Tahap deteksi memakai detektor morfologi: sebuah titik pusat dihitung sebagai buah hanya jika lebih terang daripada semua titik pada lingkaran di sekitarnya. Konfigurasi akhir memakai radius 30 piksel dan 15 titik radial. Detektor diterapkan pada lapisan R dan masker segmentasi.

Pemilihan parameter dilakukan pada gambar kebun. Pada radius 20 piksel, konfigurasi dengan 15 sampai 35 titik mendekati hitungan manual. Konfigurasi akhir menangkap sekitar 85% kelompok dengan 10% positif palsu. Penulis mengulang analisis pada gambar lain yang dipilih acak dan memperoleh hasil yang sangat mirip.

Hasil diukur pada 10 gambar terhadap hitungan manual. Rata-rata galat hitung berada pada rentang +5,4% sampai 26%, dengan nilai rata-rata 14%. Positif palsu rata-rata 7%. Galat tidak merata menurut tingkat oklusi: 18% buah tidak tertutup, 49% tertutup sebagian, dan 33% tertutup berat (75 sampai 99%). Abstrak mencatat proporsi buah tertutup berat yang sama, yaitu 33%.

Batasan kajian ini jelas. Data hanya 10 gambar dari satu varietas dan satu kondisi cahaya malam. Kematangan tidak diukur, meskipun penulis menyebutnya sebagai pekerjaan lanjutan bersama varietas dan buah lain. Karena setiap gambar dihitung terpisah, kajian ini tidak menyelesaikan masalah buah yang sama terlihat dari beberapa pandang.
