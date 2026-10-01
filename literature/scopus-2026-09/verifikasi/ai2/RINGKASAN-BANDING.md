# Ringkasan Banding Putaran Kedua (AI-2) terhadap Putaran Pertama

Berkas ini dibuat `tools/scopus/verifikasi_ai2_gabung.py`; jangan disunting tangan. Kedua putaran dikerjakan model bahasa besar. Tidak ada angka di sini yang berasal dari peninjau manusia.

## 1. Rekaman kunci tahap kelayakan (C1, C3, dan eksklusi)

Putaran kedua menilai 510 dari 510 rekaman tanpa melihat keputusan putaran pertama.

Kesepakatan kelompok (C1, C3, X, lain): 83,7%; kappa Cohen 0,768.

| Putaran 1 | n | sama | AI-2: kode lain, tetapi kode putaran 1 juga cocok | berbeda |
|---|---:|---:|---:|---:|
| C1 | 187 | 173 | 7 | 7 |
| C3 | 170 | 166 | 2 | 2 |
| X | 153 | 88 | 0 | 65 |

Arah perbedaan kelompok (putaran 1 -> putaran 2):

- X -> C4: 31
- X -> C2: 12
- X -> C1: 8
- X -> C5: 8
- C1 -> X: 7
- C1 -> C2: 4
- C1 -> C5: 3
- X -> R: 3
- C3 -> C1: 2
- X -> C3: 2
- C3 -> X: 2
- X -> T: 1

Kesepakatan kode pada rekaman yang kelompoknya sama:

| Kolom | n dibandingkan | sama | % |
|---|---:|---:|---:|
| C1 mekanisme | 180 | 131 | 72,8% |
| C1 akuisisi | 180 | 166 | 92,2% |
| C1 per kelas | 180 | 172 | 95,6% |
| C3 tugas | 168 | 141 | 83,9% |
| C3 lokasi | 168 | 124 | 73,8% |
| C3 modalitas | 168 | 162 | 96,4% |
| C3 multipandang | 168 | 154 | 91,7% |
| C3 per kelas | 168 | 147 | 87,5% |
| X alasan | 88 | 69 | 78,4% |

Dasar bukti putaran kedua: {'abstrak': 292, 'abstrak (web)': 84, 'teks lengkap (web)': 13, 'teks lengkap': 103, 'judul': 18}.

Rekaman yang masuk ajudikasi (ada perbedaan apa pun): **227**.

## 2. Sampel buta Cek 1 (putaran kedua oleh model, bukan manusia)

Angka di bawah adalah kesepakatan antara dua putaran model. Angka ini **bukan** kesepakatan manusia-model yang diminta Cek 1 dan tidak boleh ditulis di `kesepakatan.md`.

Tahap judul: n = 300; kesepakatan lanjut/eksklusi 85,3%; kappa 0,646; AI-1 eksklusi tetapi AI-2 lanjut: 44; AI-1 lanjut tetapi AI-2 eksklusi: 0; kritis (AI-1 eksklusi, AI-2 menandai C1 atau C3): **2**.

Tahap kelayakan, kode penuh: n = 100; kesepakatan 83,0%; kappa 0,802.
Tahap kelayakan, kode dengan semua X digabung: n = 100; kesepakatan 83,0%; kappa 0,801.
Tahap kelayakan, masuk/eksklusi: n = 100; kesepakatan 90,0%; kappa 0,324.

Kritis tahap kelayakan (AI-1 eksklusi, AI-2 C1 atau C3): **2**.

## 3. Cek fakta naskah (Cek 6, oleh model)

Baris klaim dinilai: 213 dari 213. Y 171, SEBAGIAN 29, N 2, TAK-TERPERIKSA 11.

Dasar bukti: {'teks lengkap': 87, 'abstrak': 88, 'teks lengkap (web)': 23, 'judul': 5, 'abstrak (web)': 10}.

