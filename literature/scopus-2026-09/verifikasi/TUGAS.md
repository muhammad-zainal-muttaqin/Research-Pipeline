# Tugas Peninjau

Diperbarui 27 November 2026. Ini satu-satunya daftar keputusan yang menunggu
Anda.

- [ ] **4.29 Kelompok 7 PDF terakhir dari folder Drive "dariemail" (27 November
  2026).** Apakah kelompok di bawah ini benar? Teks lengkapnya ada di
  `teks/<kunci>.txt`; nomor baris di kolom alasan merujuk berkas itu. Usul AI
  ditulis di
  [`../topik/penyaringan/teks_lengkap.txt`](../topik/penyaringan/teks_lengkap.txt)
  sesudah disetujui. Tiga baris yang perlu perhatian khusus: Mejias-Hernandez dkk.
  2026 pindah ke kelompok multi-observasi, Bakas dkk. 2026 pindah ke kelompok kelas
  pada citra tunggal, dan Golder dkk. 2026 dikeluarkan.

  | Kajian | Kelompok di tahap abstrak | Usul dari teks lengkap | Alasan dan tempat di teks |
  |---|---|---|---|
  | Kakisina dkk. 2024, deteksi dan urutan pungut brondolan (`kakisina2024detection`) | Pencitraan TBS kelapa sawit (C3) | C3 tetap; kode sawit tidak berubah (brondolan, di tanah) | Versi naskah tertelaah (*reviewed manuscript*), bukan PDF penerbit. 839 citra GoPro 5568×4872 piksel dari kebun di Mamuju, Sulawesi Barat, saat panen (baris 148–152). YOLOv7 mendeteksi brondolan di tanah untuk robot pemungut, dan urutan pungut ditentukan dari koordinat y kotak (baris 295–318). mAP50 0,866 dan 0,823 untuk dua set hiperparameter (baris 34). Tidak ada pencacahan |
  | Rosbi dan Omar 2025, segmentasi TBS dengan YOLO dan ambang warna (`rosbi2025segmentation`) | C3 | C3 tetap; lokasi diubah dari "tidak disebut" menjadi di kebun tanpa keterangan posisi tandan (KEBUN) | 124 citra TBS Tenera dari kebun di Malaysia, separuh matang dan separuh mentah (baris 92–93). YOLOv2 melokalisasi tandan (IoU rerata 0,77 pada 16 citra, baris 162), ambang Otsu pada kanal a\* dan S membuang daun dan tanah (baris 141–145), lalu warna diklasifikasikan dengan Gaussian Naive Bayes: akurasi sampai 93% pada 16 citra (baris 40–41) |
  | Goh dkk. 2024, data sintetis untuk kematangan TBS (`goh2024synthetic`) | C3 | C3 tetap; tugas diubah dari klasifikasi citra tandan (KLS) menjadi deteksi tandan dalam adegan (DET), lokasi diubah dari "tidak disebut" menjadi KEBUN | YOLOv8 dilatih terpisah dengan 150 citra nyata dari kebun dan dengan citra sintetis dari Unity Perception (baris 307–318). Dengan jumlah citra latih yang sama, mAP50 naik dari 0,533 (nyata) menjadi 0,96 (sintetis), tetapi teks tidak menyebut apakah data validasinya sama (baris 405–420). Tidak ada pencacahan |
  | Bakas dkk. 2026, kesehatan dan hasil jeruk dengan YOLO ringan (`bakas2026efficient`) | Pencacahan atau estimasi hasil dari satu pandang (C2) | **Pindah ke C4 (atribut kelas pada citra tunggal)**; pilihan lain: dikeluarkan, E5 (hitungan tidak dievaluasi) | 4.212 citra dari kebun jeruk di Sebt El Guerdane, Maroko, dua kelas: jeruk sehat dan jeruk sakit (baris 120–131). mAP50 terbaik 87,6% untuk YOLOv9t (baris 25–26). Aplikasi Android menampilkan jumlah per kelas (baris 226–229), tetapi jumlah itu tidak dibandingkan dengan hitungan lapangan, dan penulis menyatakan tidak ada pelacakan antarbingkai (baris 262–265). Usul C4 mengikuti keputusan Langpoklakpam dkk. 2025 di butir 4.28. Kajian ini bukan laporan ganda dari `bakas2025uav`, yang mencacah pohon jeruk dari UAV |
  | Golder dkk. 2026, deteksi daun dan buah pepaya dari gerombol (`golder2026automated`) | C2 | **Dikeluarkan, E5 (deteksi tanpa pencacahan)**; pilihan lain: C2 tetap | 1.840 citra gerombol pepaya dari kebun di Khulna, Bangladesh (baris 399–403), dilabeli terlihat penuh, terlihat sebagian, dan bukan buah (baris 490–493). Hasil hanya presisi 99,19%, *recall* 98,92%, dan mAP 99,43% (baris 31). Pencacahan disebut sebagai tujuan (baris 966–972), tetapi tidak dievaluasi. Kelas keterlihatan bukan atribut buah, sehingga syarat C4 tidak terpenuhi |
  | Mejias-Hernandez dkk. 2026, deteksi dan pencacahan nanas dari ortomosaik UAV (`mejiashernandez2026automated`) | C2 | **Pindah ke C1, asosiasi geometri (M4), beberapa pandang diskret (D)**; pilihan lain: dikeluarkan, E5 (hitungan tidak dievaluasi) | Buah dideteksi pada ortomosaik UAV yang dipotong per petak 1280×1280; deteksi ganda di batas petak dan antarmodel disaring, lalu kotak dipetakan kembali ke koordinat ortomosaik (baris 166–170, 263–265, 310–343). Menurut aturan rekonstruksi di PROTOKOL.md, deteksi pada ortomosaik berkode C1 M4. mAP@0,5 di atas 92% (baris 16). Jumlah deteksi di satu ortomosaik naik dari 36.852 menjadi 84.202 (baris 560–569), tetapi tidak dibandingkan dengan hitungan lapangan |
  | Xu dkk. 2022, posisi jeruk dari gabungan kamera dan LiDAR (`xu2022citrus`) | Deteksi buah dengan depth, 3D, atau non-RGB (C5) | C5 tetap | YOLOv3 dilatih pada 2.000 citra jeruk di lingkungan alami (baris 368–372). Depth pusat buah diambil dari awan titik LiDAR yang diproyeksikan ke citra setelah kalibrasi bersama (baris 88–92). Dari 50 pengukuran, galat posisi di bawah 0,01 m, dengan rerata 5,82 mm (Xc) dan 5,8 mm (Yc) (baris 545–549). Tempat percobaan posisi tidak dijelaskan. Tidak ada pencacahan |

  Dampak bila semua usul disetujui: peta naik dari 918 menjadi 924 kajian
  (multi-observasi 252, sawit 154, kelas pada citra tunggal 39, depth 111,
  satu pandang tetap 162), yang dinilai dari teks lengkap menjadi 962, yang
  dikeluarkan 38, dan yang tidak diperoleh 56. Angka naskah berubah lewat
  makro; isi naskah main7 tidak berubah.

- [ ] **5.7 Bagian naskah yang hanya dapat diisi penulis.** Apakah sumber
  dana dan ucapan terima kasih sudah benar? Kerangkanya ada di akhir naskah,
  sebelum Data availability (`manuscript/source/main7-body.tex`, cari
  `\authorcheck`; di PDF tercetak merah). Peran CRediT dan penulis
  korespondensi (Fatma Indriani) sudah diisi. Hal yang masih harus diputuskan
  penulis:
  - Ada atau tidaknya dana hibah.
  - Isi ucapan terima kasih, atau hapus seksinya.
  - Tempat data. Jika keputusan penyaringan, matriks bukti, log, dan skrip
    diunggah ke repositori, cantumkan DOI atau tautannya di bagian Data
    availability.
  - Saat mengirim, periksa kembali dan unggah [lima butir *highlights*](../../../manuscript/output/papers/main6-highlights.txt)
    sebagai berkas terpisah dan periksa kebijakan AI di *Guide for Authors* jurnal
    *Computers and Electronics in Agriculture*.

  Hapus semua `\authorcheck` sebelum dikirim. Dampaknya: tanpa isian ini,
  naskah belum dapat dikirim.

