# Coffee and cashew nut dataset: A dataset for detection, classification, and yield estimation for machine learning applications

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `sanya2024coffee` |
| Judul asli | Coffee and cashew nut dataset: A dataset for detection, classification, and yield estimation for machine learning applications |
| Penulis | Sanya, Rahman; Nabiryo, Ann Lisa; Tusubira, Jeremy Francis; Murindanyi, Sudi; Katumba, Andrew; Nakatumba-Nabende, Joyce |
| Tahun | 2024 |
| Venue | Data in Brief |
| Kode | C4 (Atribut kelas dan pencacahan) |
| Tanaman | coffee |

## Tautan Akses
- PDF: [sanya2024coffee.pdf](../pdf/sanya2024coffee.pdf)
- DOI resmi: https://doi.org/10.1016/j.dib.2023.109952

## Gambaran Umum

Kajian ini memperkenalkan kumpulan data citra kopi dan jambu mete yang dikumpulkan di Uganda. Latar belakangnya adalah metode estimasi hasil panen konvensional yang mahal, tidak efisien, dan rawan galat. Akibatnya, petani sulit merencanakan produksi dan pemasaran. Pengembangan metode pembelajaran mesin untuk estimasi hasil membutuhkan data yang sesuai, sedangkan data seperti ini masih langka, terutama di Afrika Sub-Sahara. Penulis ingin menyediakan data yang dapat dipakai untuk deteksi objek, klasifikasi, dan estimasi hasil.

Data dikumpulkan selama sembilan bulan, dari September 2022 hingga Mei 2023, pada dua musim panen. Sensor yang digunakan adalah kamera beresolusi tinggi pada *drone* DJI Mini 3 Pro dengan sensor CMOS 1/1.3 inci dan resolusi 20 hingga 48 megapiksel. Kamera dipasang pada *Unmanned Aerial Vehicle* (UAV) dan terbang pada ketinggian rendah, sekitar 1 meter dari pohon. Jumlah keseluruhan adalah 3000 citra kopi dan 3086 citra jambu mete, sehingga totalnya 6086 citra. Tanaman kopi mencakup varietas Robusta dan Arabika. Pengumpulan kopi dilakukan di Kabupaten Bukomansimbi, Kyotera, Mukono, Buikwe, Masaka, Luuka, Jinja, Mbale, dan Sironko. Pengumpulan jambu mete dilakukan di Lira, Abim, dan Nakasongola. Data kopi berasal dari Robusta dan Arabika, dan data jambu mete dari wilayah utara dan tengah Uganda.

Setiap citra dianotasi dengan beberapa *bounding box* untuk objek yang diminati. Anotasi jambu mete dibuat dengan Makesense AI, sedangkan anotasi kopi dibuat dengan VGG Image Annotator oleh spesialis kopi dari lembaga penelitian. Format keluarannya adalah YOLO. Kelas kopi terdiri atas *unripe*, *ripening*, *ripe*, *spoilt*, dan *coffee_tree*. Kelas jambu mete terdiri atas *tree*, *flower*, *premature*, *unripe*, *ripe*, dan *spoilt*. Hasil kuantitatif yang tercantum adalah 121.761 instans kopi kelas *unripe* pada Tabel 1. Penulis juga menyebut bahwa setiap citra memiliki metadata waktu dan lokasi geografis. Nilai instans kelas lain tidak dibahas di sini.

Penulis menyatakan bahwa sebagian besar citra kopi berasal dari dua kebun demonstrasi di Kituza, Kabupaten Mukono, sehingga cakupan lokasi kopi cenderung terpusat. Pengumpulan dilakukan saat puncak musim panen, dan citra ditangkap dari beberapa sudut pandang untuk setiap pohon. Keseimbangan jumlah citra antarwilayah dan antarkelas tidak dijelaskan lebih lanjut dalam bagian yang dibaca. Kumpulan data ini ditujukan untuk penelitian lanjutan dan bukan untuk evaluasi model tertentu.
