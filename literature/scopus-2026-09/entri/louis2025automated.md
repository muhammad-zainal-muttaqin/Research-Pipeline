# Automated Muskmelon Counting in Real Farm Environment using YOLOv11n

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `louis2025automated` |
| Judul asli | Automated Muskmelon Counting in Real Farm Environment using YOLOv11n |
| Penulis | Louis, Fourr\'e; Ooi, Boon-Yaik; Savita, K. Sugathan |
| Tahun | 2025 |
| Venue | Proceeding of the IEEE International Conference on Smart Instrumentation Measurement and Applications Icsima |
| Kode | C1 (Gabungan beberapa pengamatan) |
| Tanaman | melon |

## Tautan Akses
- PDF: [louis2025automated.pdf](../pdf/louis2025automated.pdf)
- DOI resmi: https://doi.org/10.1109/icsima66552.2025.11233648

## Gambaran Umum

Penelitian ini bertujuan membangun alur kerja penglihatan komputer untuk
mendeteksi, melacak, dan menghitung melon di lingkungan pertanian nyata.
Permasalahan yang diangkat adalah deteksi dan penghitungan buah di lapang
terganggu oleh okklusi, pencahayaan yang berubah, dan latar belakang yang
padat. Di rumah kaca, tanaman pada barisan belakang sering terdeteksi bersama
barisan depan, sementara daun menutupi buah. Penulis menguji pengaruh strategi
anotasi dan metode pemrosesan terhadap akurasi penghitungan dengan model
YOLOv11n.

Data berupa rekaman video dari kendaraan berpandu otomatis di sebuah rumah
kaca melon. Hanya dua video yang dianggap relevan: satu untuk membangun
dataset dan satu untuk pengujian. Video uji berdurasi 85 detik dan memuat 73
melon pada barisan depan; jumlah ini menjadi acuan hitungan manual. Dari video
sumber diekstrak 187 citra relevan. Penulis membuat tiga versi anotasi: V1D
menandai semua melon tampak dengan minimal 75% bagian terlihat; V2D hanya
menandai melon barisan depan yang jelas dan tidak tertutup daun; V3D memisahkan
melon depan dan belakang dengan ambang minimal 50% tampak. Citra dibagi 70%
latih (131), 20% validasi (37), dan 10% uji (19). Augmentasi kecerahan dan
eksposur ±10% dengan tiga keluaran per contoh menambah jumlah citra latih
menjadi 392 dari total 448. Eksperimen lokal memakai GPU NVIDIA RTX 4060m
8 GB dan prosesor Intel i5-12450HX.

Mekanisme penghitungan diuji dalam empat versi pemrosesan. V1R menjalankan
model yang dihosting di Roboflow dan mengirim setiap frame melalui API,
sehingga memerlukan koneksi internet. V2R memakai metode `predict` Ultralytics
per frame tanpa penyimpanan identitas, sehingga satu melon dapat dihitung
berkali-kali. V3R memakai metode `track` yang menjaga identitas melon antarframe
tetapi dapat kehilangan jejak saat buah tertutup terlalu lama, sehingga
muncul ID baru. V4R memakai penghitung garis dari pustaka Solutions
Ultralytics: sebuah melon dihitung sekali ketika melintasi garis, selama buah
terlihat dan terdeteksi saat melintas. Tingkat galat dihitung terhadap 73 melon
hasil hitungan manual.

Hasil terbaik diperoleh dari kombinasi anotasi V2D dan metode V4R, dengan 71
melon terhitung, tingkat galat 2,74%, dan waktu pemrosesan 153,09 detik untuk
video 85 detik. Kombinasi V2D dengan V3R menghasilkan 89 melon dan galat
21,92%; V3D dengan V3R menghasilkan 68 melon dan galat 6,85%; V3D dengan V4R
menghasilkan 59 melon dan galat 19,18%. Anotasi V1D dengan V4R mencatat galat
56,16%, sedangkan V1R paling lambat dengan 3157,44 detik. Sebagai acuan,
model YOLOv11n dasar tanpa dataset khusus mencatat galat 53,425% pada V3R dan
49,315% pada V4R.

Batasan yang dinyatakan penulis mencakup waktu pemrosesan hampir dua kali
durasi video sehingga sistem belum dapat dipakai secara langsung (real time),
kehilangan jejak pada okklusi sementara yang memicu penghitungan ganda, dan
ukuran dataset yang kecil (392 citra latih). Penghitung garis dapat melewatkan
melon yang tertutup saat melintasi garis. Penulis juga mencatat pertanyaan
penerapan pemrosesan di perangkat, server, atau cloud, serta mengusulkan
perbaikan pelacakan dan dataset yang lebih besar.
