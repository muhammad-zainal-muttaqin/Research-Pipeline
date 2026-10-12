# Kemajuan Cek 6 (draf model, menunggu persetujuan peninjau)

Keluaran: `usul_cek_fakta.csv`. Lembar `cek_fakta.csv` tidak diubah. Putusan memeriksa kalimat lembar dan, bila berbeda,
kalimat naskah terkini (`main6-body.tex`); kolom `catatan` menyebut mana yang salah.

## Ringkasan

- Klaim selesai: **273 dari 273** (117 baris lama dipertahankan; 156 baris baru). Satu baris lama dilengkapi: K022.
- Putusan: Y 206 · N 57 · kosong (tidak dapat diperiksa atau dipastikan) 10.
- Sumber yang dibaca: teks lengkap 166 · ANGKA-NASKAH.md dan berkas skrip 58 · abstrak 40 · judul saja 3 (K116, K128-1, K134-2; nilai baru `judul`, putusan Y dengan keyakinan rendah) · tidak tersedia 6.
- Perbandingan dengan `cek_fakta_ai2.csv` (dibuka setelah semua putusan selesai): sama 178 · beda 35 · tanpa pembanding 60 (baris abstrak dan angka korpus tidak dicakup AI-2). Alasan tiap beda ada di kolom `beda_dari_ai2`.
- Baris jenis angka korpus (K139-K187) tidak dicek ke makalah. Angkanya dicocokkan dengan `ANGKA-NASKAH.md` dan `main6-angka.tex`, lalu dihitung ulang (tanpa menjalankan skrip yang menulis berkas) dari `matriks_bukti.csv`, `kode_C3.txt`, `counts.csv`, `queries.json`, dan `gambar_tinjauan.py`.

## Klaim N yang masih salah di naskah terkini (9 wajib, 2 opsional)

| id | Masalah | Usul perbaikan |
|---|---|---|
| K006 | Tabel acq, kolom acuan Felip-Pomes: "Manual count" salah | "Harvest count per 5-m stretch (commercial sorting line)" |
| K014 | Tabel assoc, Qi 2025: 165.172 instans; penjumlahan Tabel 1 sumber 165.081 | Tulis 165.081 atau sebut "15 videos, 1,614 tomato clusters" |
| K020 | Tabel assoc, Xing 2026: 95,6% adalah terhadap pelacak tanpa kompensasi apa pun | "MAE 595.03 to 26.11 (95.6%) against tracking without compensation; 15% lower than single-view compensation" |
| K038-1 | Butir (1) Seksi Acquisition: "sees a minority" tidak berlaku untuk 54% (dua sisi) | "A single image per side counts about half of the fruit or fewer on a dense canopy: 27% for one side and 54% for two sides in mango, and 40% of harvest with one image per side" |
| K112-2 | Hamdani 2026 menghitung buah individual di dalam tandan, bukan tandan | Pisahkan dari kelompok "count bunches": "count individual fruits within bunches" |
| K112-4 | Prasetyo 2020: citra dikumpulkan dari internet, bukan diambil di kebun | "... or collected from the internet [prasetyo2020automatic]" |
| K112-5 | Hutapea 2024: tidak ada hasil pencacahan; hanya deteksi kematangan (kata "counting" hanya di judul) | Keluarkan dari kelompok pencacahan atau tulis "reports ripeness detection only"; tinjau angka "nine counting studies" |
| K142 | Kueri Q9 tidak memuat batas bidang subjek (SUBJAREA) | "All searches were limited to 2012-2026; all except Q9 were also limited to subject areas that publish engineering, computing, or agricultural work." (juga di PROTOKOL.md Seksi 2) |
| K184 | Hanya 6 dari 14 perbandingan membandingkan pelacak semata; "most within temporal tracking" tipis | "Table contains 14 such comparisons, six of which compare trackers only" |
| K112-6 (opsional) | Shiddiq 2023: konveyor ember buatan sendiri, bukan lini sortasi; sumber tidak memakai kata "laboratory" | "purpose-built test conveyor" |
| K094-1 (opsional) | Kelas matang terbaik menurut R2 dan MAE, tidak menurut MAPE dan RMSE; naskah terkini belum menyebut RMSE | Tambahkan "and RMSE" pada "though not the lowest MAPE" |

Peringatan pada baris berputusan Y: K043-1 dan K043-2 (kalimat sesudahnya, "do not report counts against a reference", tidak tepat untuk Roy & Isler 2017 dan Zaenker dkk. 2021); K106 ("largest study in the corpus" tidak diperiksa; `suharjito2025oil` merilis 14.503 citra); K112-9 (Narendran 2024 memakai sensor gerak dan tekanan untuk buah lepas, tanpa citra, sehingga tidak memenuhi kriteria "image-based").

## Klaim N yang hanya salah di lembar (naskah terkini sudah benar, tidak perlu perubahan naskah)

- Angka lama, naskah terkini memakai makro (36): K024, K025, K036, K037, K146-K148, K150-K154, K156, K157, K159-K170, K172, K177-K183, K186, K187. Penjelasan dan nilai benar ada di kolom `usul_perbaikan`. Kecuali K163: lembar menulis "before 2018, M1 and M4 were the only mechanisms"; kenyataannya satu kajian (Stein 2016) memakai pelacakan.
- Rumusan lembar yang sudah diperbaiki di naskah terkini (10): K027, K084-4, K093-2, K105-3, K106 (96,54% menjadi 94,66%), K112-3, K113-1, K129-3, K129-4, K136-2.

## Klaim yang tidak dapat diperiksa atau dipastikan (10)

K035-4 dan K035-6 (hanya judul, tidak ada abstrak atau PDF), K078-2 (NeRF), K104-1 (Depth Anything V2), K105-4 (Suharjito 2021), K109-4 (Junos 2022: apakah objeknya tandan atau buah lepas), K117-2 (Kipli 2023: abstrak tidak menyebut UAV maupun hitung ulang), K125 (Goh 2025: kata "self-described systematic" tidak ada di judul atau abstrak; perlu membuka artikel), K128-2 (Grant & Booth: "configurative synthesis" tidak dapat dikaitkan), K136-1 (Koirala 2019: hanya abstrak).

## Temuan sumber di luar baris lembar

- `teks/kang2022accurate.txt` dan `pdf/kang2022accurate.pdf` memuat makalah lain ("Semantic Segmentation of Fruits on Multi-sensor Fused Data in Natural Orchards"); makalah yang dikutip adalah DOI 10.1016/j.compag.2022.107450. Putusan K098-2 memakai abstrak. Perlu diperbaiki pada Cek 4.
- Wang dkk. 2019: abstrak dan Tabel 1 menulis 9,9% dan 7,3%, sedangkan teks Seksi 3.3 menulis 9,7% dan 7,1% (bersih tetap 2,6%).
- Lima dari sembilan kajian pencacahan sawit berbeda dari rumusan naskah: Hamdani (menghitung buah, bukan tandan), Hidayat (citra tandan hasil panen di TPH, bukan di pohon), Prasetyo (citra dari internet), Hutapea (tanpa hasil pencacahan), Narendran (sensor, bukan citra).
- Naskah menyebut "open-access full text" pada pengodean, sedangkan 41 PDF diperoleh lewat pembelian (SERAH-TERIMA.md).
- Jumlah per tanaman (apel 53, jeruk 21, dan seterusnya) memakai tanaman pertama dalam daftar tiap kajian (`angka_naskah.py` baris 66); hitungan kemunculan penuh lebih besar.

## Catatan proses

- Putusan awal K094-1, K105-3, dan K113-1 saya ubah dari Y menjadi N setelah membandingkan dengan AI-2 dan memeriksa ulang sumber; K112-2 dan K112-5 dari Y menjadi N setelah teks lengkap dibaca lebih jauh; K128-2 dari Y menjadi kosong.
- Satu kali, perintah penggabungan saya memuat skrip lama pada folder kerja bersama dan menulis ulang `usul_cek_fakta.csv` dengan 117 baris yang sama (ukuran dan jumlah baris identik); sesudah itu 117 baris lama dibandingkan dengan salinan dan tidak berubah, kecuali K022 yang sengaja dilengkapi.
