# 047 - C2DFNet: Criss-Cross Dynamic Filter Network for RGB-D Salient Object Detection

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `zhang2022c2dfnet` |
| Judul asli | C2DFNet: Criss-Cross Dynamic Filter Network for RGB-D Salient Object Detection |
| Penulis | Miao Zhang, Shunyu Yao, Beiqi Hu, Yongri Piao, Wei Ji |
| Tahun | 2023 (versi awal daring 2022) |
| Venue | IEEE Transactions on Multimedia, vol. 25, hlm. 5142–5154 |
| Tema | RGB-D SOD |

## Tautan Akses
- **DOI (versi penerbit):** https://doi.org/10.1109/TMM.2022.3187856
- **Kode dan hasil (GitHub):** https://github.com/OIPLab-DUT/C2DFNet
- **Google Scholar:** https://scholar.google.com/scholar?q=C2DFNet%3A%20Criss-Cross%20Dynamic%20Filter%20Network%20for%20RGB-D%20Salient%20Object%20Detection
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=C2DFNet%3A%20Criss-Cross%20Dynamic%20Filter%20Network%20for%20RGB-D%20Salient%20Object%20Detection&sort=relevance

## Gambaran Umum

Makalah ini memperkenalkan C2DFNet (*Criss-Cross Dynamic Filter Network*), sebuah metode deteksi objek menonjol dwimodal RGB-D. Deteksi objek menonjol (*Salient Object Detection*, SOD) adalah tugas menandai piksel objek yang paling menarik perhatian pada sebuah citra dan memisahkannya dari latar; varian RGB-D menambahkan peta kedalaman (*depth map* — citra yang tiap pikselnya menyatakan jarak permukaan ke kamera) sebagai masukan kedua di samping citra warna RGB. Persoalan yang diserang C2DFNet adalah cara menggabungkan (memfusi) dua modalitas yang sifatnya berbeda ini tanpa memakai konvolusi berparameter tetap yang, menurut penulis, tidak peka terhadap perbedaan bawaan antara data RGB dan kedalaman.

Gagasan intinya adalah mengganti konvolusi statis dengan *dynamic filter* (tapis dinamis) yang bobotnya dibangkitkan mengikuti isi citra, lalu menerapkannya sepanjang pola *criss-cross* (silang mendatar-menegak) agar biaya komputasinya rendah. Model ini disusun dari dua modul: satu untuk memperkuat fitur di dalam tiap modalitas, satu lagi untuk memilih fitur lintas-modalitas secara adaptif. Menurut naskah, C2DFNet memperoleh kinerja yang bersaing terhadap 28 metode RGB-D SOD mutakhir pada 7 set data publik.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Bab-bab RGB-D SOD sebelumnya menegakkan gagasan bahwa peta kedalaman memberi isyarat geometri yang memisahkan objek dari latar ketika warna saja ambigu, dan bahwa cara fusi menentukan kualitas hasil. DMRA (bab [035](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)) memakai *attention* untuk menyaring kedalaman, dan BBS-Net (bab [036](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)) memisahkan fitur beraras rendah dan tinggi sebelum menggabungkannya. Sebagian besar metode ini dibangun di atas konvolusi konvensional, yaitu operasi yang bobot tapisnya dipelajari saat pelatihan lalu dibekukan: satu set bobot yang sama dipakai untuk semua citra saat inferensi, tanpa memandang isi adegan.

Penulis menilai pemakaian bobot tetap ini sebagai keterbatasan mendasar untuk data dwimodal. RGB membawa tekstur dan warna, sedangkan kedalaman membawa struktur jarak; keduanya memiliki statistik dan tingkat keandalan yang berbeda, dan keandalan itu berubah antar-adegan. Peta kedalaman dari sebuah adegan bisa tajam, tetapi pada adegan lain berderau atau salah pada bidang tembus pandang. Tapis berparameter tetap memperlakukan semua masukan seragam, sehingga tidak dapat menyesuaikan pemrosesan menurut kondisi modalitas pada tiap citra. Masalah inilah yang ingin dipecahkan: memberi jaringan kemampuan menyesuaikan operasinya terhadap adegan, sambil menjaga biaya komputasi tetap terkendali.

## Ide Utama

Solusi C2DFNet berpijak pada *dynamic filter network*, yaitu jaringan yang tidak menyimpan satu set bobot tapis tetap, melainkan membangkitkan bobot tapis secara langsung dari fitur masukan melalui subjaringan kecil. Dengan cara ini, operasi konvolusi menjadi bergantung pada isi citra: adegan yang berbeda menghasilkan tapis yang berbeda pula. Kelemahan pendekatan ini adalah biayanya — membangkitkan tapis dua dimensi penuh untuk tiap posisi spasial sangat mahal.

C2DFNet menekan biaya itu dengan menguraikan (*decoupling*) konvolusi dinamis menjadi pola *criss-cross*. Alih-alih membangkitkan dan menerapkan tapis atas seluruh bidang dua dimensi sekaligus, model menyalurkan panduan hanya sepanjang jalur mendatar dan menegak yang melewati tiap posisi. Dua modul dibangun di atas prinsip ini: *Model-specific Dynamic Enhanced Module* (MDEM) yang memperkuat fitur di dalam satu modalitas dengan panduan konteks global, dan *Scene-aware Dynamic Fusion Module* (SDFM) yang memilih fitur antar-modalitas secara adaptif terhadap adegan. Yang masuk adalah dua aliran fitur (RGB dan kedalaman); yang keluar adalah peta saliensi; yang berubah dibanding pendahulunya adalah tapis penggabung yang kini dibangkitkan per adegan, bukan dibekukan.

## Cara Kerja Langkah demi Langkah

### Tapis Statis versus Tapis Dinamis

Pada konvolusi biasa, sebuah tapis 3×3 memiliki sembilan bobot yang ditetapkan saat pelatihan dan dipakai identik untuk setiap citra uji. Pada tapis dinamis, kesembilan bobot itu tidak disimpan; sebuah subjaringan membacanya dari fitur masukan sehingga menghasilkan bobot yang berbeda untuk masukan yang berbeda. Konsekuensinya, operasi yang sama dapat menonjolkan tepi pada satu adegan dan meratakan derau pada adegan lain, sesuai isi masing-masing. Untuk fusi RGB-D hal ini berguna karena bobot penggabung dapat mengecil ketika kedalaman berkualitas rendah dan membesar ketika kedalaman informatif.

### Pola Criss-Cross untuk Menekan Biaya

Pola *criss-cross* diambil dari gagasan agregasi konteks sepanjang baris dan kolom. Setiap posisi hanya mengumpulkan informasi dari posisi lain yang sebaris (mendatar) dan sekolom (menegak) dengannya, bukan dari seluruh bidang. Perbedaan biayanya besar. Pada peta fitur berukuran 80×80 = 6.400 posisi, operasi konteks padat (*non-local*) yang menghubungkan tiap posisi ke semua posisi lain memerlukan sekitar 6.400 × 6.400 ≈ 41 juta pasangan keterhubungan. Pola criss-cross hanya menghubungkan tiap posisi ke 80 + 80 − 1 = 159 posisi pada silangnya, sehingga menjadi sekitar 6.400 × 159 ≈ 1 juta pasangan — turun sekitar 40 kali lipat. Dengan menerapkan operasi criss-cross dua kali berurutan, informasi dari satu posisi tetap dapat menjangkau seluruh peta melalui perpotongan jalur, sehingga konteks global tercapai tanpa biaya penuh. C2DFNet memindahkan prinsip ini ke ranah tapis dinamis: tapis dibangkitkan dan diterapkan sepanjang jalur criss-cross, bukan atas kernel dua dimensi penuh.

Alur data ringkas kedua modul terhadap dua aliran masukan:

```
   RGB  ──►┌──────────────┐        ┌──────────────┐
           │    MDEM       │──feat─►│              │
           │ (perkuat fitur│  RGB   │    SDFM       │──► decoder ──► peta
           │  intra-modal, │        │ (fusi lintas- │        saliensi
   depth ─►│  panduan      │──feat─►│  modal,       │
           │  global)      │  depth │  sadar-adegan)│
           └──────────────┘        └──────────────┘
             tapis criss-cross        tapis criss-cross
             dibangkitkan per         memilih RGB vs
             modalitas                depth per adegan
```

### Model-specific Dynamic Enhanced Module (MDEM)

MDEM bekerja di dalam satu modalitas, terpisah untuk aliran RGB dan aliran kedalaman. Modul ini membangkitkan tapis dinamis yang dikondisikan oleh konteks global fitur, lalu memakainya untuk memperkuat fitur intra-modalitas tersebut. Istilah "konteks global" merujuk pada ringkasan informasi dari seluruh peta fitur, bukan hanya tetangga lokal; dengan menyertakannya, penonjolan sebuah objek dinilai relatif terhadap keseluruhan adegan. Karena tapisnya criss-cross, konteks global itu disalurkan melalui jalur baris-kolom, sehingga penguatan tetap peka posisi tanpa biaya operasi padat.

### Scene-aware Dynamic Fusion Module (SDFM)

SDFM bekerja antar-modalitas. Setelah RGB dan kedalaman diperkuat secara mandiri, modul ini melakukan pemilihan fitur dinamis di antara keduanya: bobot penggabung dibangkitkan menurut adegan sehingga kontribusi RGB dan kedalaman dapat ditimbang berbeda dari satu citra ke citra lain. Frasa "sadar-adegan" (*scene-aware*) menandai bahwa keputusan fusi bergantung pada isi adegan tertentu, bukan aturan tetap. Rancangan ini menjawab langsung masalah keandalan kedalaman yang berubah-ubah: pada adegan dengan kedalaman buruk, SDFM dapat menekan kontribusi kedalaman, dan sebaliknya.

### Prediksi Peta Saliensi

Fitur hasil fusi dari SDFM diteruskan ke sebuah *decoder*, yaitu bagian jaringan yang secara bertahap menaikkan resolusi fitur kembali ke ukuran citra untuk menghasilkan peta saliensi akhir. Peta ini bernilai kontinu per piksel dan menyatakan derajat penonjolan; nilai tinggi menandai piksel objek menonjol. Seluruh jaringan dilatih *end-to-end*, yakni dari masukan sampai keluaran dalam satu proses optimasi tanpa tahap terpisah.

## Eksperimen dan Hasil

Evaluasi dilakukan pada 7 set data publik RGB-D SOD dan membandingkan C2DFNet terhadap 28 metode mutakhir, angka yang keduanya dinyatakan pada abstrak makalah. Set data yang lazim dipakai pada evaluasi seperti ini mencakup NJU2K, NLPR, STERE, DES, LFSD, SSD, dan SIP; daftar tepat ketujuh set data yang dipakai perlu dipastikan ke naskah.

Metrik penilaian standar untuk tugas ini ada empat. *S-measure* (*Structure-measure*) menilai kemiripan struktur antara peta prediksi dan kebenaran acuan, menggabungkan kesamaan berorientasi objek dan berorientasi wilayah. *F-measure* adalah rata-rata harmonik presisi dan *recall* pada peta saliensi yang diambangkan. *E-measure* (*Enhanced-alignment measure*) menilai kesejajaran pada aras piksel sekaligus aras citra global. *MAE* (*Mean Absolute Error*) mengukur selisih rata-rata absolut antara peta prediksi dan acuan; berbeda dari tiga metrik sebelumnya, nilai MAE yang lebih rendah menandakan hasil lebih baik. Klaim inti makalah adalah bahwa C2DFNet mencapai kinerja yang bersaing pada gabungan metrik ini terhadap sederet metode pembanding, sekaligus mempertahankan biaya komputasi yang terkendali berkat penguraian criss-cross. Nilai numerik per set data serta biaya komputasi (jumlah parameter, FLOPs, dan kecepatan inferensi) tidak dikutip di sini dan harus dibaca langsung dari tabel naskah.

## Kelebihan dan Keterbatasan

Kelebihan utama C2DFNet adalah pemakaian tapis dinamis yang menyesuaikan pemrosesan terhadap tiap adegan, sehingga fusi dapat menimbang RGB dan kedalaman menurut keandalannya, bukan menurut aturan tetap. Penguraian criss-cross membuat kemampuan adaptif ini dapat diperoleh dengan biaya jauh lebih rendah daripada operasi konteks padat. Pemisahan tugas antara MDEM (penguatan intra-modalitas) dan SDFM (fusi antar-modalitas) juga membuat peran tiap modul jelas dan dapat diuji secara terpisah melalui *ablation*.

Keterbatasan berikut merupakan analisis penulis bab, bukan pernyataan eksplisit penulis makalah. Secara konseptual, pola criss-cross membatasi jalur agregasi pada arah mendatar dan menegak; konteks di arah diagonal hanya terjangkau tidak langsung melalui dua langkah, sehingga pola ini merupakan pendekatan terhadap konteks penuh, bukan penggantinya. Dari sisi rekayasa, ketergantungan SDFM pada peta kedalaman tetap ada: modul dapat menekan kedalaman yang buruk, tetapi tidak dapat memulihkan informasi yang tidak tersedia di dalamnya. Selain itu, C2DFNet memakai *backbone* konvolusi (dilaporkan ResNet-50 pada praktik umum bidang ini, perlu dipastikan ke naskah), sehingga penangkapan konteks global bertumpu pada modul tambahan, berbeda dari pendekatan berbasis *Transformer* seperti VST (bab [042](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md)) yang menyatukan konteks global ke dalam encoder.

## Kaitan dengan Bab Lain

C2DFNet berada pada silsilah RGB-D SOD yang dibuka DMRA (bab [035](./035%20-%202019%20-%20DMRA%20-%20RGB-D%20SOD.md)) dan diperkuat BBS-Net (bab [036](./036%20-%202020%20-%20BBS-Net%20-%20RGB-D%20SOD.md)). Ia mewarisi persoalan pusat klaster ini, yakni cara memfusi RGB dan kedalaman, tetapi menggeser jawabannya dari *attention* berbobot tetap ke tapis yang dibangkitkan per adegan. Kekhawatiran tentang kedalaman berkualitas rendah yang menonjol pada D3Net (bab [037](./037%20-%202021%20-%20D3Net%20%28Rethinking%20RGB-D%20SOD%29%20-%20RGB-D%20SOD.md)) dan HDFNet (bab [040](./040%20-%202020%20-%20HDFNet%20-%20RGB-D%20SOD.md)) dijawab C2DFNet melalui pemilihan fitur adaptif pada SDFM. Terhadap VST (bab [042](./042%20-%202021%20-%20Visual%20Saliency%20Transformer%20%28VST%29%20-%20RGB-D%20SOD.md)) yang mengejar konteks global lewat *Transformer*, C2DFNet menempuh jalur berbeda: mempertahankan *backbone* konvolusi tetapi menambahkan konteks global murah melalui pola criss-cross. Penekanan pada keseimbangan akurasi dan efisiensi inilah yang menghubungkan bab ini dengan minat tinjauan pada penerapan waktu nyata, termasuk turunan YOLO plus RGB-D.

## Poin untuk Sitasi

Kutip dengan kunci `zhang2022c2dfnet`. Ringkasan yang aman dikutip: "C2DFNet mengganti konvolusi berparameter tetap pada fusi RGB-D dengan tapis dinamis berpola criss-cross, disusun dari modul penguatan intra-modalitas (MDEM) dan modul fusi antar-modalitas sadar-adegan (SDFM), dan dilaporkan bersaing terhadap 28 metode mutakhir pada 7 set data publik." Fakta terverifikasi dari sumber primer (abstrak dan halaman resmi): identitas modul MDEM dan SDFM, konsep penguraian konvolusi dinamis menjadi pola criss-cross, jumlah 28 metode pembanding dan 7 set data, serta venue IEEE Transactions on Multimedia (vol. 25, hlm. 5142–5154, DOI 10.1109/TMM.2022.3187856). Klaim yang **belum** dapat diverifikasi dari sumber primer dan harus dicek ke naskah sebelum sitasi formal: nilai numerik S-/F-/E-measure dan MAE per set data; jumlah parameter, FLOPs, dan kecepatan inferensi; daftar tepat ketujuh set data; serta identitas *backbone* (ResNet-50 disebut berdasarkan praktik umum bidang, bukan konfirmasi naskah).
