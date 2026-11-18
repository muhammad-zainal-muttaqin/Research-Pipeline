# Automated Systems Based on Machine Vision for Inspecting Citrus Fruits from the Field to Postharvest—a Review

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `cubero2016automated` |
| Judul asli | Automated Systems Based on Machine Vision for Inspecting Citrus Fruits from the Field to Postharvest—a Review |
| Penulis | Cubero, Sergio; Lee, Won Suk; Aleixos, Nuria; Albert, Francisco; Blasco, Jose |
| Tahun | 2016 |
| Venue | Food and Bioprocess Technology |
| Kode | R (Tinjauan terdahulu) |
| Tanaman | citrus |

## Tautan Akses
- PDF: [cubero2016automated.pdf](../pdf/cubero2016automated.pdf)
- DOI resmi: https://doi.org/10.1007/s11947-016-1767-1

## Gambaran Umum

Artikel ini adalah tinjauan pustaka tentang sistem otomatis berbasis penglihatan mesin untuk memeriksa buah sitrus mulai dari kebun hingga pascapanen. Masalah utamanya adalah kebutuhan akan pemeriksaan mutu yang cepat, non-destruktif, dan andal, baik untuk memperkirakan hasil panen dan mendeteksi penyakit di pohon maupun untuk mengurutkan buah di fasilitas pengemasan. Penulis menyoroti bahwa sistem yang hanya memakai informasi warna memiliki keterbatasan serius: warna cacat pada satu buah dapat menyerupai kulit sehat buah lain, padahal warna kulit sehat kedua buah itu berbeda. Karena berupa tinjauan, artikel ini tidak menyajikan eksperimen baru; seluruh angka hasil berasal dari kajian yang ditinjau.

Tanaman yang dibahas adalah sitrus, terutama jeruk dan mandarin, serta limau gedang (grapefruit). Data berupa citra buah di kebun, citra udara dan satelit, serta citra pada lini pemilahan pascapanen. Teknologi akuisisi yang ditinjau mencakup kamera warna, pencitraan multispektral dan hiperspektral (MIS/HIS), pencitraan termal, fluoresensi yang diinduksi sinar ultraviolet (UV), spektrometer near-inframerah (NIR), pencitraan hambur-balik laser (LBI), dan telepon pintar. Pengolahan memakai segmentasi berbasis warna, tekstur, dan wilayah, pemilihan panjang gelombang, serta pengklasifikasi seperti analisis diskriminan linier (LDA), jaringan saraf tiruan, mesin vektor pendukung (SVM), *spectral angle mapper* (SAM), dan *spectral information divergence* (SID).

Mekanisme deteksi dan asosiasi bersifat dua jalur. Di kebun, buah dan penyakit dikenali dari warna, tekstur, atau tanda spektral—misalnya perbedaan pantulan antara buah dan daun, panjang gelombang 815 nm dan 1190 nm untuk membedakan buah hijau muda dari daun, serta akumulasi pati pada daun bergejala *Huanglongbing* (HLB). Di pascapanen, warna kulit diukur dengan *Citrus Colour Index* (CCI) yang dihitung dari koordinat HunterLab L, a, b; nilai negatif berarti hijau tua, nilai sekitar nol berarti transisi hijau ke jingga, dan nilai positif tinggi berarti buah matang. Indeks ini dipakai untuk menentukan tanggal panen dan lama perlakuan penghilangan warna hijau (*degreening*). Untuk cacat berbahaya seperti busuk dan kanker sitrus, mekanismenya memakai kontras spektral pada panjang gelombang tertentu, fluoresensi UV, atau profil hambur-balik laser yang direduksi menjadi profil intensitas radial satu dimensi.

Angka hasil yang dikutip mencakup beragam metrik dengan acuan hitung yang berbeda-beda, semuanya dari kajian yang ditinjau, bukan dari eksperimen penulis. Untuk deteksi di kebun, algoritme kromatisitas merah mencapai akurasi 90% dengan tingkat positif palsu 4% (Hannan dkk.); algoritme *extended spectral angle mapping* mencapai 86% untuk HLB (Li dkk. 2014); sistem genggam HLB mencapai 95,5% di laboratorium dan 98,5% di lapangan (Pourreza dkk. 2015a); dan deteksi buah rontok akibat HLB mencapai 83–88% (Choi dkk. 2015). Untuk perkiraan hasil, hubungan antara jumlah buah dari citra dan hitungan manual menghasilkan R² = 0,76 dengan waktu olah 283 ms per citra pada prosesor 750 MHz (Annamalai & Lee 2003), sedangkan model yang menggabungkan indeks vegetasi dua pita dan ukuran kanopi menghasilkan akurasi 76% (Ye dkk. 2008). Di lini pemilahan, sistem pada kendaraan pertanian mampu mengurutkan buah ke dalam tiga kategori pada laju 8 buah per detik (Cubero dkk. 2014a), sementara sistem dengan spektrometer NIR membutuhkan 12–20 s per buah sehingga tidak praktis secara komersial (Kohno dkk. 2011). Untuk klasifikasi cacat, penggunaan ruang warna HSI menghasilkan tingkat keberhasilan 43% untuk serangan kutu sisik hingga 100% untuk kerusakan akibat dingin dan ujung tangkai (Blasco dkk. 2007b), meningkat menjadi rata-rata 85% setelah informasi morfologi dimasukkan (Blasco dkk. 2009); deteksi kanker sitrus mencapai 97,6% dengan SID (Qin dkk. 2009); dan bintik hitam sitrus mencapai akurasi keseluruhan 92% dengan diskriminasi 100% untuk kelas tersebut (Bulanon dkk. 2013), naik menjadi sekitar 98% dengan SAM dan SID (Kim dkk. 2014).

Batasan yang dikemukakan penulis mencakup kondisi pencahayaan yang berubah-ubah dan oklusi buah sebagai hambatan utama deteksi langsung di kebun secara waktu nyata; keterbatasan sistem berbasis warna ketika warna cacat mirip kulit sehat; kebutuhan pelatihan ulang yang sering pada segmentasi terselia; redundansi data hiperspektral dan harga peralatan yang tinggi; serta belum tercapainya penilaian mutu internal buah secara langsung pada lini produksi. Penulis juga mencatat ketidaksesuaian panjang gelombang yang dilaporkan antarkajian, bahkan untuk jenis cacat yang sama, karena pemilihan panjang gelombang lebih ditentukan oleh metode statistik yang dipakai daripada oleh cacatnya sendiri. Sistem yang mampu mendeteksi semua jenis cacat sekaligus masih menjadi tantangan, dan mesin komersial saat ini baru mengurutkan buah berdasarkan ukuran dan berat, sehingga presisi deteksi busuk masih perlu ditingkatkan.

