# A low-cost and unsupervised image recognition methodology for yield estimation in a vineyard

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `di2019low` |
| Judul asli | A low-cost and unsupervised image recognition methodology for yield estimation in a vineyard |
| Penulis | Di Gennaro, Salvatore Filippo; Toscano, Piero; Cinat, Paolo; Berton, Andrea; Matese, Alessandro |
| Tahun | 2019 |
| Venue | Frontiers in Plant Science |
| Kode | C2 (Pencacahan satu pandang) |
| Tanaman | grape |

## Tautan Akses
- PDF: [di2019low.pdf](../pdf/di2019low.pdf)
- DOI resmi: https://doi.org/10.3389/fpls.2019.00559

## Gambaran Umum

Penelitian ini bertujuan mengembangkan metode cepat dan otomatis untuk memperkirakan hasil panen kebun anggur sebelum panen. Cara konvensional berupa pengambilan contoh manual pada sejumlah tanaman terbatas memakan waktu, sering tidak representatif, dan bersifat subjektif karena hasilnya berbeda antarpengamat. Penulis menguji penglihatan mesin tanpa perusak untuk memperoleh perkiraan hasil dari jumlah dan ukuran tandan. Penulis menyatakan ini sebagai kajian pertama yang menerapkan teknologi tersebut pada kebun anggur yang dipangkas daun sebagian dengan sistem teralis *vertical shoot positioning* (VPS).

Kajian berlangsung pada musim 2017 dan 2018 di kebun anggur seluas 1,4 ha di Castellina in Chianti, Italia tengah, dengan kultivar Sangiovese (*Vitis vinifera*) dan jarak tanam 2,2 m × 0,75 m. Platform UAV berupa Mikrokopter termodifikasi membawa kamera multispektral ADC-Snap (1280 × 1024 piksel, pita hijau, merah, dan inframerah dekat) pada ketinggian 50 m untuk memetakan variabilitas vigor melalui NDVI, serta kamera RGB Sony Cyber-shot DSC-QX100 20,2 MP pada ketinggian 10 m dengan kemiringan 45° yang menghasilkan resolusi 0,002 m/piksel pada zona buah. Pada 2017, lima pohon dipilih di setiap zona vigor tinggi (HV) dan rendah (LV), lalu dicitrakan dalam dua kondisi: kondisi terburuk (W) dengan tandan tertutup daun dan berada di bayang pukul 10.00, serta kondisi terbaik (B) setelah defoliasi sebagian dengan tandan tersinari matahari pukul 14.00. Pada 2018, desain diperluas menjadi dua blok per zona vigor dengan delapan tanaman per blok (32 tanaman) dan hanya memakai kondisi B. Pengukuran lapang yang menjadi acuan hitung meliputi massa segar tunas, jumlah tandan matang dan belum matang, serta berat hasil per pohon.

Deteksi tandan memakai alur kerja tanpa pengawasan di ImageJ. Citra RGB diubah ke ruang warna Lab; komponen b* dipilih karena berkorelasi dengan warna tandan, lalu filter Gauss berjari-jari 2 diterapkan. Ambang Otsu pertama memisahkan piksel vegetasi yang kemudian dibuang, dan ambang Otsu kedua menghasilkan piksel tandan yang diubah menjadi mask setelah skala dikalibrasi dengan target berpanjang diketahui. Rutin *Analyze Particles* menghitung jumlah dan ukuran tandan dengan batas luas 200 piksel hingga tak terhingga serta sirkularitas 0,25–1,00. Kinerja deteksi dihitung dengan indeks *true positive rate* (TPR), yaitu rasio tandan yang terklasifikasi benar terhadap total tandan yang diamati; akurasi dihitung sebagai (nilai terukur − nilai taksiran)/nilai terukur × 100. Pendugaan hasil memakai regresi linier antara luas tandan (cm²) dari citra dan berat buah (g) dari ukuran lapang pada 2017 (R² = 0,90). Parameter regresi itu diterapkan pada data 2018 sebagai cawat uji dan divalidasi terhadap pengukuran lapang.

Pada 2017, TPR untuk tandan matang mencapai 100,0% pada HV_B dan LV_B, tetapi turun menjadi 54,9% pada HV_W dan 26,4% pada LV_W; pada 2018, TPR tandan matang sebesar 84,8% (HV_B) dan 97,7% (LV_B). Luas tandan 2017 sebesar 168,6 ± 84,0 cm² di HV dan 69,2 ± 35,6 cm² di LV. Akurasi pendugaan hasil pada kondisi B berturut-turut 84,9% dan 86,9% pada 2017 serta 91,7% dan 84,4% pada 2018; pada kondisi W akurasinya hanya 40,1% dan 22,2%. Penulis menyatakan metode ini memerlukan garis pandang langsung ke tandan, sulit membedakan tandan hijau yang belum matang, dan cenderung meremehkan hasil sebesar sekitar 12% pada 2018. Analisis biaya menunjukkan pendekatan UAV menghemat waktu tetapi menaikkan biaya total karena pembelian peralatan, sehingga lahan minimal 60 ha diperlukan untuk mengganti investasi tetap; untuk lahan lebih kecil penulis mengusulkan jasa UAV bersama atau koperasi. Kinerja juga bergantung pada perencanaan penerbangan dan kondisi cahaya matahari, dan penulis meminta uji lanjutan untuk pengaturan kamera, sudut gimbal, parameter penerbangan, varietas, dan tahap fenologis.
