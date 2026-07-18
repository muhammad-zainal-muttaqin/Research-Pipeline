# 115 - Research on a Fusion Technique of YOLOv8-URE-Based 2D Vision and Point Cloud for Robotic Grasping in Stacked Scenarios

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `yang2025yolov8ure` |
| Judul asli | Research on a Fusion Technique of YOLOv8-URE-Based 2D Vision and Point Cloud for Robotic Grasping in Stacked Scenarios |
| Penulis | Xuhui Ye, Xiaoyang Qin, Leming Zhan, Jun Wang, Yan Chen |
| Tahun | 2025 |
| Venue | Applied Sciences (MDPI), volume 15, nomor 12, artikel 6583 |
| Tema | YOLO plus RGB-D |

## Tautan Akses
- **DOI (penerbit, akses terbuka):** https://doi.org/10.3390/app15126583
- **Halaman naskah (MDPI):** https://www.mdpi.com/2076-3417/15/12/6583
- **Google Scholar:** https://scholar.google.com/scholar?q=Research%20on%20a%20Fusion%20Technique%20of%20YOLOv8-URE-Based%202D%20Vision%20and%20Point%20Cloud%20for%20Robotic%20Grasping%20in%20Stacked%20Scenarios
- **Semantic Scholar:** https://www.semanticscholar.org/search?q=Research%20on%20a%20Fusion%20Technique%20of%20YOLOv8-URE-Based%202D%20Vision%20and%20Point%20Cloud%20for%20Robotic%20Grasping%20in%20Stacked%20Scenarios&sort=relevance

## Gambaran Umum

Makalah ini, ditulis peneliti dari Hubei University of Technology, mengusulkan YOLOv8-URE: varian YOLOv8 dengan tiga modifikasi arsitektur, dipadukan dengan registrasi *point cloud* (kumpulan titik koordinat 3D hasil pemindaian kedalaman) untuk memperkirakan pose *grasp* (pose cengkeraman robot) pada objek yang saling bertumpuk. Deteksi 2D dari YOLOv8-URE dipakai lebih dulu untuk mempersempit wilayah pencarian pada citra; hanya *point cloud* di wilayah itu yang kemudian diregistrasi terhadap model acuan objek untuk memperoleh pose 3D yang dipakai lengan robot saat mencengkeram.

Hasil yang dilaporkan penulis: YOLOv8-URE meningkatkan akurasi deteksi 9,21% dibandingkan YOLOv8n (varian YOLOv8 terkecil) dan memangkas waktu registrasi *point cloud* sebesar 60,5%, dengan ukuran model hanya 4,46 MB. Kontribusi makalah ini bagi tinjauan pustaka adalah menunjukkan bahwa penyaringan wilayah oleh detektor 2D dapat memangkas biaya komputasi tahap 3D secara signifikan, menjadikannya salah satu bukti konkret pola integrasi YOLO dengan data kedalaman dalam klaster YOLO plus RGB-D.

## Latar Belakang: Masalah yang Ingin Dipecahkan

Pada tugas *bin picking* (pengambilan objek dari wadah atau tumpukan) di lini produksi, objek yang akan diambil sering saling menutupi dan bersinggungan. Metode registrasi *point cloud* klasik — menyelaraskan awan titik hasil pemindaian dengan model 3D acuan objek untuk menentukan posisi dan orientasinya — biasanya dijalankan pada seluruh *point cloud* adegan tanpa penyaringan awal. Pada skenario bertumpuk, hal ini menimbulkan dua masalah: pertama, jumlah titik yang harus dicocokkan sangat besar sehingga waktu registrasi memanjang; kedua, titik-titik dari objek tetangga yang saling menutupi ikut tercampur dalam pencarian korespondensi, sehingga akurasi pose yang dihasilkan menurun.

Pendekatan yang lebih efisien adalah mempersempit wilayah pencarian 3D lebih dahulu memakai deteksi 2D, sebagaimana sudah dieksplorasi pada bab-bab lain klaster YOLO plus RGB-D. FusionVision (bab 113), misalnya, memakai YOLO untuk deteksi awal sebelum segmentasi kedalaman. Namun demikian, detektor 2D dasar seperti YOLOv8n dilatih untuk objek yang umumnya terpisah jelas; pada citra objek logam identik yang bertumpuk rapat — kasus uji makalah ini — batas antarobjek kabur dan tekstur permukaan seragam, sehingga kotak pembatas (*bounding box*) yang dihasilkan kurang presisi dan sebagian objek kecil di celah tumpukan terlewat. Masalah inilah yang mendorong penulis memodifikasi arsitektur YOLOv8 sebelum menggabungkannya dengan registrasi 3D.

## Ide Utama

Gagasan inti makalah adalah dua lapis penyaringan berurutan: penyaringan kasar oleh deteksi 2D, diikuti penghalusan pose oleh registrasi 3D pada wilayah yang sudah dipersempit. YOLOv8-URE tidak dirancang untuk menggantikan registrasi *point cloud*, melainkan untuk membuatnya bekerja pada subset titik yang jauh lebih kecil dan lebih relevan, sehingga proses pencarian korespondensi 3D lebih cepat dan tidak terganggu titik dari objek tetangga.

Untuk mencapai penyaringan 2D yang cukup andal pada objek bertumpuk dan bertekstur seragam, penulis memodifikasi tiga bagian YOLOv8: tulang punggung (*backbone*, bagian jaringan yang mengekstraksi fitur dari citra masukan) diberi blok konvolusi bernama C2f_UniRepLKNetBlock yang memperluas *receptive field* (wilayah citra masukan yang memengaruhi satu nilai fitur keluaran) tanpa menambah banyak parameter; sebuah modul perhatian (*attention*) bernama *Efficient Local Attention* (ELA) disisipkan untuk menajamkan fokus fitur pada lokasi objek; serta bagian leher jaringan (*neck*, bagian yang menggabungkan fitur antar-skala) memakai strategi fusi multi-skala yang lebih efisien untuk memperbaiki regresi kotak pembatas. Ketiganya bekerja sama sebelum kotak deteksi diteruskan ke tahap registrasi 3D.

## Cara Kerja Langkah demi Langkah

### Modifikasi Tulang Punggung: C2f_UniRepLKNetBlock

Modul C2f pada YOLOv8 asli adalah blok konvolusi bertumpuk yang mengekstraksi fitur bertahap dari citra. Penulis mengganti sebagian isinya dengan blok bergaya UniRepLKNet: sedikit lapis konvolusi berkernel besar dipakai untuk menangkap konteks spasial luas dalam satu operasi, dikombinasikan dengan lapis konvolusi berkernel kecil untuk menangkap pola spasial yang lebih rinci. Kernel besar memungkinkan satu unit fitur "melihat" area citra yang lebih luas sekaligus — berguna ketika batas antarobjek pada tumpukan kabur dan konteks di sekitar objek diperlukan untuk memastikan lokasi sebenarnya.

### Modul Perhatian: Efficient Local Attention (ELA)

Setelah fitur diekstraksi, modul ELA memberi bobot lebih besar pada wilayah fitur yang relevan dengan keberadaan objek dan menekan bobot wilayah latar. Mekanisme perhatian semacam ini menghitung skor kepentingan untuk tiap lokasi fitur, kemudian mengalikan fitur asli dengan skor tersebut sehingga sinyal objek diperkuat relatif terhadap derau latar sebelum diteruskan ke lapis berikutnya.

### Fusi Multi-Skala pada Leher Jaringan

Bagian leher YOLOv8 standar menggabungkan peta fitur dari beberapa skala resolusi (fitur resolusi tinggi untuk objek kecil, resolusi rendah untuk objek besar). Makalah ini memakai strategi fusi yang lebih efisien pada tahap ini untuk memperbaiki akurasi regresi koordinat kotak pembatas, sehingga posisi dan ukuran kotak yang diprediksi lebih dekat dengan kotak kebenaran, khususnya untuk objek kecil yang terselip di celah tumpukan.

### Dari Kotak 2D ke Segmentasi Point Cloud

Kotak pembatas hasil YOLOv8-URE diproyeksikan ke citra kedalaman (*depth*) yang sejajar (*aligned*) dengan citra RGB — teknik yang sama dipakai bab-bab lain klaster ini, misalnya Expandable YOLO (bab 112). Hanya titik-titik *point cloud* yang berada di dalam proyeksi kotak itu yang diambil untuk tahap berikutnya, sehingga *point cloud* seluruh adegan (yang bisa memuat puluhan ribu titik dari banyak objek bertumpuk) dipangkas menjadi subset kecil milik satu objek target.

Alur data dari citra masukan sampai pose *grasp* dapat diringkas sebagai berikut.

```
citra RGB ---> YOLOv8-URE (backbone UniRepLKNet + ELA + neck fusi)
                    |
                    v
             kotak pembatas 2D per objek
                    |
                    v
citra depth --> proyeksi kotak ke depth --> segmentasi point cloud
                                                   |
                                                   v
                                   registrasi terhadap model acuan objek
                                                   |
                                                   v
                                        pose grasp 3D (posisi + orientasi)
```

### Registrasi Point Cloud dan Estimasi Pose

Titik-titik yang sudah tersegmentasi diselaraskan (diregistrasi) terhadap model 3D acuan objek untuk menghitung transformasi (translasi dan rotasi) yang menempatkan model acuan pada posisi objek nyata. Karena registrasi hanya bekerja pada subset titik milik satu objek — bukan seluruh adegan bertumpuk — jumlah titik yang harus dicocokkan berkurang drastis, dan kemungkinan pencocokan keliru dengan titik objek tetangga berkurang. Pose 3D hasil registrasi inilah yang dipakai lengan robot untuk menentukan posisi dan sudut pendekatan saat mencengkeram objek.

## Eksperimen dan Hasil

Penulis menguji YOLOv8-URE pada tugas deteksi objek dan membandingkannya dengan YOLOv8n serta detektor sejenis lain sebagai garis dasar (*baseline*). Pada pengujian ini, YOLOv8-URE mencapai *recall* (proporsi objek sebenarnya yang berhasil terdeteksi) sebesar 80,4% pada set uji, dilaporkan lebih tinggi daripada algoritme pembanding utama; akurasi deteksi keseluruhan meningkat 9,21% dibandingkan YOLOv8n. Ukuran model hasil akhir hanya 4,46 MB, jauh lebih ringkas daripada varian YOLOv8 yang lebih besar, sehingga sesuai untuk penempatan pada perangkat dengan sumber daya komputasi terbatas di lini produksi.

Pada tahap gabungan 2D-3D, penyaringan wilayah oleh YOLOv8-URE memangkas waktu registrasi *point cloud* sebesar 60,5% dibandingkan menjalankan registrasi pada *point cloud* adegan penuh tanpa penyaringan. Interpretasinya: sebagian besar penghematan waktu berasal dari berkurangnya jumlah titik yang harus dicocokkan, bukan dari perubahan algoritme registrasi itu sendiri — kontribusi YOLOv8-URE di sini adalah sebagai tahap penyaring, bukan pengganti registrasi. Penulis juga melaporkan bahwa fusi ini meningkatkan keberhasilan pengambilan objek pada skenario bertumpuk dibandingkan tanpa penyaringan 2D, meskipun angka pasti tingkat keberhasilan pengambilan (*grasp success rate*) pada uji lengan robot fisik tidak diperoleh secara pasti dari sumber sekunder yang diakses penulis bab ini dan perlu dicek langsung pada tabel eksperimen naskah asli.

## Kelebihan dan Keterbatasan

Kelebihan utama makalah ini adalah kombinasi tiga modifikasi arsitektur yang saling melengkapi — perluasan *receptive field* di *backbone*, penguatan fokus fitur lewat ELA, dan fusi multi-skala yang lebih rapi di *neck* — untuk mengatasi kasus spesifik objek identik yang bertumpuk rapat, ditambah model yang tetap ringkas (4,46 MB). Penyaringan wilayah oleh detektor 2D sebelum registrasi 3D terbukti memberi penghematan waktu registrasi yang besar (60,5%), sebuah hasil yang relevan bagi seluruh klaster YOLO plus RGB-D karena menunjukkan nilai praktis integrasi 2D-3D, bukan sekadar nilai akademik.

Dari sisi rekayasa, kombinasi tiga modifikasi (*backbone*, *attention*, *neck*) membuat kontribusi masing-masing komponen sulit dipisahkan tanpa studi ablasi (pengujian menghapus satu komponen untuk mengukur kontribusinya) yang rinci; makalah dilaporkan menyertakan sebagian pengujian semacam ini, tetapi rincian kuantitatifnya tidak terjangkau dari sumber sekunder yang diakses. Secara konseptual, keandalan metode masih bergantung pada ketersediaan model 3D acuan untuk setiap objek yang hendak diregistrasi — pendekatan ini kurang langsung berlaku untuk objek baru yang belum memiliki model acuan, berbeda dengan metode estimasi pose berbasis pembelajaran langsung dari data (*data-driven*) tanpa model CAD. Keterbatasan lain yang lazim pada metode berbasis registrasi adalah kepekaannya terhadap kualitas *point cloud*: derau atau titik hilang akibat permukaan objek yang mengilap atau saling menutupi dapat memengaruhi akurasi registrasi meski wilayah sudah dipersempit oleh YOLOv8-URE.

## Kaitan dengan Bab Lain

Bab ini melanjutkan pola integrasi 2D-3D yang juga muncul pada bab 112 (Expandable YOLO), yang memakai kotak deteksi YOLO untuk memandu segmentasi kedalaman, dan bab 113 (FusionVision), yang menggabungkan deteksi, segmentasi, dan estimasi pose 3D dalam satu *pipeline*. Perbedaannya, bab ini menempatkan registrasi *point cloud* klasik — bukan jaringan estimasi pose berbasis pembelajaran end-to-end — sebagai tahap akhir setelah penyaringan 2D, sehingga menjadi contoh jalur hibrida yang menggabungkan detektor CNN modern dengan geometri 3D klasik. Bab ini juga berkaitan dengan klaster Grasp Robotik, khususnya bab 084 (GraspNet-1Billion), yang membangun tolok ukur besar untuk estimasi pose *grasp* dari data RGB-D; makalah 115 dapat dibaca sebagai penerapan gagasan penyaringan wilayah berbasis deteksi pada konteks industri yang lebih sempit (objek identik bertumpuk) dibandingkan tolok ukur objek beragam pada GraspNet-1Billion. Pembaca yang tertarik pada varian lain penggabungan YOLO dan registrasi/fusi kedalaman untuk *grasp* dapat melanjutkan ke bab 116 (Tian dkk., Grasp via YOLO + RGB-D Fusion).

Tautan terkait: [112 - Expandable YOLO](./112%20-%202020%20-%20Expandable%20YOLO%20-%20YOLO%20plus%20RGB-D.md), [113 - FusionVision](./113%20-%202024%20-%20FusionVision%20-%20YOLO%20plus%20RGB-D.md), [116 - Grasp via YOLO + RGB-D Fusion (Tian dkk.)](./116%20-%202023%20-%20Grasp%20via%20YOLO%20+%20RGB-D%20Fusion%20%28Tian%20dkk.%29%20-%20YOLO%20plus%20RGB-D.md), [084 - GraspNet-1Billion](./084%20-%202020%20-%20GraspNet-1Billion%20-%20Grasp%20Robotik.md).

## Poin untuk Sitasi

Kutip dengan kunci `yang2025yolov8ure`. Ringkasan yang aman dikutip: "YOLOv8-URE memodifikasi *backbone*, modul perhatian, dan *neck* YOLOv8 untuk deteksi objek bertumpuk, lalu memakai kotak deteksinya untuk menyaring *point cloud* sebelum registrasi 3D pose *grasp*; penulis melaporkan peningkatan akurasi deteksi 9,21% atas YOLOv8n dan pemangkasan waktu registrasi 60,5%, dengan ukuran model 4,46 MB." Butir yang perlu diverifikasi langsung ke naskah sebelum sitasi formal: definisi metrik persis di balik angka "akurasi deteksi 9,21%" (apakah mAP@0,5 atau metrik lain), nama dataset/jumlah citra yang dipakai untuk melatih dan menguji YOLOv8-URE, nama algoritme registrasi *point cloud* yang dipakai pada tahap akhir, serta angka tingkat keberhasilan pengambilan objek (*grasp success rate*) pada uji lengan robot fisik, yang tidak diperoleh secara pasti dari sumber sekunder yang diakses penulis bab ini.
