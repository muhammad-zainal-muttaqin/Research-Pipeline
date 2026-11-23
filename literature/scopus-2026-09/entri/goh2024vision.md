# Vision Language Models for Oil Palm Fresh Fruit Bunch Ripeness Classification

## Metadata Ringkas
| Field | Nilai |
|---|---|
| Kunci BibTeX | `goh2024vision` |
| Judul asli | Vision Language Models for Oil Palm Fresh Fruit Bunch Ripeness Classification |
| Penulis | Goh, Jin Yu; Yunos, Yusri Md; Sheikh, Usman Ullah; Mohamed Ali, Mohamed Sultan |
| Tahun | 2024 |
| Venue | 2024 IEEE 8th International Conference on Signal and Image Processing Applications Icsipa 2024 |
| Kode | C3 (Pencitraan TBS kelapa sawit) |
| Tanaman | oil palm |

## Tautan Akses
- PDF: [goh2024vision.pdf](../pdf/goh2024vision.pdf)
- DOI resmi: https://doi.org/10.1109/icsipa62061.2024.10686009

## Gambaran Umum

Kajian ini menguji apakah model bahasa-visual (*vision language model*, VLM) dapat mengklasifikasikan kematangan tandan buah segar (TBS) kelapa sawit sekaligus menghasilkan deskripsi teksnya. Penulis menyebut inspeksi manual padat karya, subjektif, dan rawan kesalahan. Tiga model dibandingkan: LLaVA 1.5, Yi-VL, dan PaliGemma. Kajian menilai kualitas deskripsi teks dan kecepatan, bukan pencacahan buah.

Data berupa 100 citra TBS yang diambil secara manual di kebun (*orchard*), terbagi rata antara matang dan mentah. Setiap citra diberi kotak pembatas dan teks keterangan kematangan. Pembagian data dinyatakan 8:1:1 untuk latih, validasi, dan uji. Teks juga menyebut 100 citra sebagai set uji. Kedua pernyataan tidak sejalan, dan jumlah total citra, jumlah pohon, serta pemberi label tidak disebut.

Ketiga model di-*fine-tune* dengan *Low-Rank Adaptation* (LoRA), yaitu teknik yang hanya melatih sedikit parameter tambahan agar muat di GPU RTX 3080 Ti. Hanya proyeksi multimodal yang dilatih, dengan *batch* 1 per perangkat, akumulasi gradien 8 langkah, laju belajar 0,0001, dan 10 *epoch*. Keluaran dinilai dengan BLEU dan ROUGE, yaitu ukuran tumpang-tindih n-gram dan urutan kata terpanjang antara teks model dan teks acuan manusia.

Yi-VL mencapai BLEU 92,24, ROUGE-1 94,00, ROUGE-2 91,59, dan ROUGE-L 93,14. LLaVA 1.5 mencapai BLEU 87,02 dan ROUGE-L 82,16. PaliGemma mencapai BLEU 38,91 dan ROUGE-L 26,15. Waktu prediksi per citra 5,48 detik (Yi-VL, 0,18 sampel/detik), 4,52 detik (LLaVA 1.5, 0,22), dan 1,90 detik (PaliGemma, 0,53). Skor dihitung pada set uji tentang kemiripan teks.

Keterbatasan: akurasi klasifikasi (benar atau salah per citra) tidak dilaporkan, hanya kemiripan teks. Hanya dua kelas (matang, mentah) dipakai. Ukuran set uji kecil dan pembagian per pohon tidak disebut. Pengujian lapangan, LiDAR, dan interpretabilitas disebut penulis sebagai pekerjaan lanjutan.
