## Gambaran Umum
Makalah ini membahas perencanaan sudut pandang aktif (*active view planning*) untuk menghitung jumlah apel dalam satu gugus (*cluster*) pada kebun. Sebuah robot dengan kamera monokular pada lengan manipulator harus memilih sudut pandang kedua dan berikutnya agar jumlah apel dalam gugus dapat ditaksir dengan benar, karena satu pandangan sering menyesatkan akibat oklusi antarbuah (Gambar 1: tiga pandangan berbeda menunjukkan tiga, lima, dan enam apel pada gugus yang sama).

Metode menyajikan setiap hipotesis dunia (*world hypothesis*) sebagai sekumpulan elipsoid dan mengurangi ruang hipotesis dengan hanya menyebutkan model kombinatorial yang berbeda (jumlah apel terlihat dan terhalang). Perencana memilih pandangan berikutnya yang meminimalkan entropi distribusi posterior atas hipotesis. Dua perencana dibandingkan: satu langkah dan multi-langkah.

Evaluasi dilakukan pada simulasi MATLAB (gugus 1 sampai 10 apel, 20 contoh per ukuran) dan percobaan dalam ruangan dengan pohon apel tiruan, karena pada musim dingin tidak ada apel pada pohon sehingga percobaan lapangan tidak dilakukan. Perencana multi-langkah lebih baik daripada satu langkah untuk gugus berukuran 5 sampai 9. Pada percobaan dalam ruangan, gugus tiga apel yang tidak pernah tampak utuh pada satu pandangan ditaksir dengan benar dalam empat pandangan.

## Latar Belakang: Masalah yang Ingin Dipecahkan
Sistem pemetaan hasil panen umumnya memotret sepanjang lintasan yang sembarang atau telah ditentukan. Cara itu memadai untuk kebun komersial berdinding buah (*fruit-wall*) dengan gugus kecil, tetapi pada kondisi umum penghitungan tepat dari satu pandangan sulit. Pencacahan langsung dari sudut pandang tunggal tidak dapat melihat buah yang terhalang buah lain.

Enumerasi seluruh keadaan dunia tidak praktis: pada volume 1 m x 1 m x 1 m dengan grid 1 cm terdapat 10^6 sel, dan untuk gugus enam apel dengan diameter tetap terdapat 10^36 hipotesis (angka dari teks makalah).

## Ide Utama
Dua kontribusi utama: (1) teknik untuk menyebutkan hanya keadaan dunia yang berbeda secara kombinatorial, dan (2) metode menaksir kemungkinan (*likelihood*) tiap keadaan dari citra. Dua model dianggap setara secara kombinatorial bila jumlah apel terlihat dan terhalang dari pandangan frontal ortografik sama. Perencanaan memilih sudut pandang berikutnya agar entropi posterior berkurang sehingga hitungan dapat ditentukan.

## Cara Kerja Langkah demi Langkah

### 1. Sistem dan akuisisi
Sistem terdiri atas kamera monokular terkalibrasi pada manipulator di atas robot darat. Pose robot dan kamera diketahui terhadap kerangka dunia, dan jarak kerja ke gugus (d_est) diperkirakan secara kasar. Bola pandang (*viewing sphere*) berpusat di pusat gugus dengan jari-jari d_est; sebanyak m sudut pandang ditempatkan pada belahan depan bola yang terjangkau robot. Dalam simulasi, 25 sudut pandang dipakai.

### 2. Model dunia kombinatorial
Awalnya diasumsikan bahwa tiap apel terlihat menghalangi paling banyak satu apel lain, sehingga hanya ada dua lapisan (terlihat dan terhalang). Jumlah maksimum apel terhalang a_oc = ⌈n/L⌉ dan jumlah minimum apel terlihat a_vis = n − ⌈n/L⌉ untuk ukuran gugus n dan L lapisan. Perluasan ke lebih dari dua lapisan memakai strategi bagi-dan-selesaikan secara rekursif. Gambar 3 menunjukkan bahwa untuk gugus maksimum tiga apel terdapat enam model tanpa batas lapisan, dan satu model tereliminasi bila oklusi dibatasi satu lapisan.

### 3. Penginderaan dari citra tunggal dan pembentukan model fisik
Penginderaan memakai karya penulis sebelumnya: tiap apel dimodelkan sebagai fungsi kepadatan Gaussian dan gugus sebagai campuran Gaussian. Metode ini memberi lokasi dan ukuran piksel tiap apel serta kemungkinan ukuran gugus tertentu. Apel terlihat diproyeksikan balik ke 3D dengan kedalaman d_est; diameter sumbu z diasumsikan sama dengan rerata diameter x dan y. Apel terhalang ditempatkan tepat di belakang apel terlihat dari kiri ke kanan. Kemungkinan model beroklusi diperoleh dengan menambahkan penalti untuk apel terhalang pada kemungkinan apel terlihat.

### 4. Perencanaan pandangan berikutnya
Masalahnya dirumuskan sebagai meminimalkan entropi H(W | I_v1, I_vk). Posterior diperbarui dengan asumsi kebebasan bersyarat antar-pandangan untuk hipotesis tetap: P(w_i | I_v1,...,I_vk) sebanding dengan hasil kali P(I_vj | w_i) dan P(w_i). Karena citra berikutnya belum terlihat, utilitas sudut pandang dihitung dari jumlah apel terlihat dan terhalang yang diharapkan dengan memproyeksikan elipsoid sebagai kuadrik; elipsoid dianggap terlihat bila lebih dari 20% proyeksinya tidak terhalang. Utilitas didefinisikan sebagai visModel/(occModel + visModel). Perencana satu langkah memakai persamaan entropi langsung. Perencana multi-langkah merencanakan urutan sudut pandang yang menutupi seluruh konfigurasi apel terlihat dan terhalang; jumlah pandangan yang direncanakan bersama ditentukan oleh kardinalitas maksimum kelompok sudut pandang. Pada kedua perencana hanya satu gerakan dilakukan pada satu waktu, lalu posterior dihitung ulang. Kriteria berhenti memakai penurunan entropi posterior bersama selisih antara puncak posterior berturutan.

## Eksperimen dan Hasil
Deteksi buah diasumsikan sudah terselesaikan (gugus buah dapat dilokalisasi pada citra masukan). Karena tidak ada metode perencanaan pandangan aktif sebelumnya untuk menghitung apel, hasil dibandingkan dengan batas bawah dari kamera ortografik dengan enam pandangan kardinal (depan, belakang, atas, bawah, kanan, kiri), serta antara perencana satu langkah dan multi-langkah.

| Jumlah apel dalam gugus | Pandangan minimum (batas bawah ortografik) |
|---|---|
| 1 | 2 pandangan tegak lurus |
| 2 | 3 pandangan saling tegak lurus |
| 3 | 4 |
| 4 | 5 |
| 5 atau lebih | 6 |

Pada simulasi (kamera bidang pandang 40 derajat, derau Gaussian pada jarak dengan σ = 1 dan µ = 0, ukuran gugus 1 sampai 10, 20 contoh per ukuran), perencana multi-langkah mengungguli perencana satu langkah untuk gugus berukuran 5 sampai 9 (Gambar 6a). Untuk gugus besar, kedua perencana lebih sering konvergen ke ukuran gugus yang salah, yang dikaitkan penulis dengan model penginderaan; penulis menyatakan penanganan dengan konvergensi 90% dapat diterima karena gugus besar jarang. Angka rinci per ukuran gugus hanya tampak pada gambar dan tidak tertulis di teks. Pada percobaan dalam ruangan (pohon apel tiruan dan apel sintetis), gugus tiga apel yang tidak pernah tampak utuh dalam satu pandangan ditaksir benar setelah empat pandangan. Hasil simulasi dan dalam ruangan dinyatakan serupa.

## Kelebihan dan Keterbatasan
Kelebihan yang dinyatakan penulis: ruang hipotesis direduksi dari jumlah eksponensial menjadi model kombinatorial yang sedikit, dan metode dapat dipakai untuk benda bulat lain dalam pertanian.

Keterbatasan yang dinyatakan penulis: percobaan lapangan belum dilakukan karena tidak ada apel pada musim dingin; deteksi buah diasumsikan selesai; pada gugus besar konvergensi ke hitungan yang benar menurun; rencana ke depan mencakup evaluasi di kebun selama musim apel (Juli sampai September di Minnesota) dan perencanaan gerak basis robot.

Menurut pembacaan ringkasan ini, bukti numerik pada teks sangat terbatas (hampir seluruh hasil berupa gambar), dan percobaan dalam ruangan hanya dilaporkan pada satu gugus tiga apel tiruan. Makalah juga tidak menyebut galat hitungan terhadap data nyata.

## Kaitan dengan Tinjauan main6
Makalah ini menangani buah yang terlihat sebagian atau terhalang dari satu pandangan dan memakai pandangan tambahan yang direncanakan secara aktif. Mekanismenya bukan pelacakan atau pencocokan identitas antarcitra, melainkan inferensi probabilistik atas jumlah buah dalam gugus yang sama dari beberapa pandangan yang digabungkan melalui hipotesis dunia bersama. Hitungan tidak dilaporkan per kelas. Acuan hitung berupa jumlah apel buatan atau simulasi yang diketahui, bukan hitungan panen atau lapangan.

Yang dapat dipindahkan ke pencacahan tandan kelapa sawit multi-sisi: gagasan bahwa jumlah sisi pandang yang diperlukan bergantung pada derajat oklusi, serta penggunaan batas bawah geometris (enam pandangan kardinal) sebagai acuan jumlah sisi minimum. Makalah tidak menyelesaikan penentuan identitas antar-pandangan secara eksplisit, karena fokusnya pada satu gugus tunggal dengan pose kamera diketahui.

## Poin untuk Sitasi
Kunci BibTeX untuk entri ini adalah `roy2017active`.

Roy dan Isler (2017) mengusulkan perencanaan sudut pandang aktif untuk menghitung apel dalam gugus dengan merepresentasikan hipotesis dunia sebagai model kombinatorial buah terlihat dan terhalang, serta memilih pandangan yang meminimalkan entropi posterior. Perencana multi-langkah mengungguli perencana satu langkah untuk gugus berukuran 5 sampai 9 dalam simulasi, dan percobaan dalam ruangan pada pohon tiruan menaksir gugus tiga apel dengan benar dalam empat pandangan.

Catatan verifikasi data: angka 10^6 sel dan 10^36 hipotesis tertulis pada Bagian I; 25 sudut pandang, bidang pandang 40 derajat, σ = 1, µ = 0, 20 contoh per ukuran gugus tertulis pada Bagian VII-B; batas bawah pandangan ortografik pada Bagian VII-A; hasil dalam ruangan (tiga apel, empat pandangan) pada Bagian VII-C. Hasil kuantitatif per ukuran gugus (Gambar 6) tidak dapat diverifikasi karena hanya tersedia sebagai grafik. Tidak ada percobaan lapangan pada tanaman nyata.
