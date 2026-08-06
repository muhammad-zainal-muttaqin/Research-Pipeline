# SR-017 — Sintesis dua laporan deep research: K1 frekuensi, K2 ordinal, K3 lintas-sisi

**Ide:** perubahan formulasi/arsitektur di atas RF-DETR-L, bukan tuning · **Eksperimen:** F-001…F-009 ([seri F](../SERI-F.md)) · **Putusan sementara: K1 LOLOS gerbang · K3 DIPALSUKAN · K2 menunggu** · 2026-08-06

---

## 1. Masalah

Setelah E-021 menempatkan RF-DETR-L pada test mAP50 0,6038, jalur yang tersisa
menyempit tajam. Pengguna menyatakan 21 Juli 2026 bahwa teknik siap-pakai dari
literatur — termasuk SAHI — sudah dicoba sendiri dan **tidak satu pun** menaikkan
mAP, dan bahwa tuning sudah habis dijalankan (ditegaskan dua kali). Jalur depth
juga tidak memberi kenaikan: E-027 menemukan depth **merugikan** untuk YOLO26n,
E-032 tidak konklusif untuk titik fusi, E-033b mencabut indikasi rentang metrik.

Yang tersisa adalah pertanyaan yang belum pernah diserang langsung: **apakah
formulasi keluaran detektornya sendiri yang membatasi?** Dua diagnosis lama
menunjuk ke sana:

- **(A) geometris** — B4 kecil, tertanam, menyatu dengan pelepah. E-011 sudah
  menunjukkan B4 **tak terlihat dalam intensitas tetapi terlihat dalam tekstur**
  (Laplacian +0,0458 di atas kendali, membalik urutan kelas).
- **(B) fotometrik** — ambiguitas B2↔B3. E-028 mengukurnya tanpa label manusia:
  inkonsistensi lintas-sisi 0,2329, dan **B2 adalah kelas paling ambigu (0,434)**,
  bukan B4.

Keduanya tetap ditangani detektor yang memperlakukan B1…B4 sebagai **empat kelas
nominal yang saling asing** — padahal kematangan itu **ordinal** (B1 = matang →
B4 = mentah) — dan yang membuang informasi bahwa 4–8 citra dalam satu pohon
memuat tandan fisik yang sama.

## 2. Ide

Sintesis dua laporan *deep research* atas satu brief (keduanya 5 Agustus 2026),
disaring menjadi tiga komponen di atas trunk RF-DETR-L yang **tidak disentuh**:

| | Komponen | Menyerang |
|---|---|---|
| **K1** | Cabang frekuensi tinggi ber-gate init-nol, disuntik sebelum projector | (A), khususnya B4 |
| **K2** | Kepala ordinal kumulatif CORN, residu terpusat ber-clip ±ε | (B), B2↔B3 |
| **K3** | Konsistensi query lintas-sisi dari graf `_confirmedLinks` | identitas tandan |

**Yang membuat rencana ini berbeda dari daftar ide sebelumnya adalah gerbangnya.**
Tiga penyaring (P1/P2/P3) dirancang untuk menggugurkan komponen **tanpa melatih
apa pun**. Itu jawaban langsung atas caveat terpenting dari brief: ukuran efek
yang diprediksi 3–10× lebih besar daripada bukti eksternal mana pun yang dikutip
(Align-DETR +0,6 AP, ViT-Adapter +1,0 AP, Wave-ViT +1,3 AP — semuanya jauh di
bawah ambang +0,05). Prior jujurnya adalah tiap komponen memberi +0,01…+0,03,
yaitu **di bawah lantai derau**.

Mutu sumber juga ditandai sejak awal, bukan belakangan: laporan Gemini memuat
**tabel hasil yang dikarang**, kedua laporan sitasinya belum dapat di-resolve,
dan "MF-RF-DETR" adalah **nama karangan** tanpa makalah, kode, maupun bobot.
Yang diambil dari laporan Gemini hanya rumusan loss — tidak satu angka pun.

## 3. Solusi

Seri F dibuka sebagai **seri terpisah** (kode `F-0NN`), bukan lanjutan seri E:
seri E adalah eksperimen diagnostik dan pembanding, seri F mengubah formulasi.
Nomor `E-033` juga sudah terpakai dua kali.

Urutan yang dijalankan berbeda dari rancangan aslinya, dan alasannya empiris.
Rancangan menaruh seluruh Gerbang 0 **di belakang** reproduksi baseline karena
mengira seluruh bobot hilang. Pemeriksaan disk menemukan itu hanya separuh
benar:

- Bobot RF-DETR-L E-021 memang **hilang**, begitu pula bobot pratlatihnya, dan
  `rfdetr_ds` kosong — semuanya dipulihkan di F-001.
- Tetapi `konsistensi_sawitmvc_rgb_seed42.json` hanya menyimpan **laju agregat**
  (tidak ada prediksi per-sisi) **sementara bobot yolo26n yang menghasilkannya
  MASIH ADA**.

Akibatnya **P2 dan P3 dapat dipindahkan ke depan baseline** dan dijalankan lebih
dulu — keduanya mampu menggugurkan komponen sebelum 9 jam GPU terbakar.

## 4. Hasil

### F-002 (P2) → K1 **LOLOS**

E-011 mengukur tandan vs **cincin sekeliling**; yang dikhawatirkan adalah tandan
vs **pelepah** — struktur berfrekuensi sangat tinggi yang justru paling menyatu
dengan B4. Wilayah pembanding didefinisikan ulang: cincin **dikurangi** seluruh
kotak GT tandan lain.

| Lengan | B4 − kendali |
|---|---|
| asli (luminans) | +0,0155 |
| gradmag (Sobel) | +0,0608 |
| **laplacian** | **+0,0721** |
| **dwt_hh** | **+0,0731** |

Mode gagal yang dikhawatirkan **tidak terjadi** — pemisahan terhadap pelepah
justru LEBIH BESAR daripada terhadap cincin generik di E-011 (0,0721 vs 0,0458).
Urutan kelas **monoton B1 < B2 < B3 < B4 pada setiap lengan frekuensi tinggi**,
dan terbalik pada luminans: makin mentah, makin menyatu dalam intensitas, makin
terpisah dalam tekstur.

**Laplacian dan DWT-HH praktis seri** (selisih 0,0010). Pada dataset ini sub-band
DWT tidak membeli apa pun di atas Laplacian yang jauh lebih murah — sehingga
lengan Laplacian di F-007 bukan formalitas melainkan pesaing sesungguhnya, dan
**DWT wajib mengalahkannya** untuk membenarkan mesin tambahannya.

### F-003 (P3) → K3 **DIPALSUKAN**

Plafon keras distilasi lintas-sisi: dari kemunculan yang salah kelas, berapa yang
punya kemunculan **benar** di sisi lain tandan fisik yang sama?

| Plafon | fraksi | CI95 |
|---|---|---|
| Kelas | **0,2794** | [0,2353; 0,3235] |
| Kehadiran | 0,4946 | [0,4583; 0,5309] |

Titik estimasi 0,2794 di bawah ambang pra-daftar 0,30 → **K3 tidak diteruskan,
F-008 dibatalkan, ~13 jam GPU dihemat.** Tetapi CI memuat 0,30, jadi **pemalsuannya
LEMAH, bukan tegas**, dan wajib dibaca demikian.

Yang justru tegas adalah dua hal lain:

1. **72% galat kelas salah di SEMUA sisi** (294 dari 408); 194 tandan bergalat
   punya nol sisi benar. Galat kelas bukan kecelakaan per pandangan — ia sifat
   tandannya. Konsisten dengan E-028 (B2 paling ambigu) dan dengan diagnosis (B):
   ambiguitas B2↔B3 tidak diselesaikan dengan melihat dari sisi lain.
2. **B4 adalah kasus terburuk: 0,1038** (11 dari 106). Harapan bahwa K3 menolong
   B4 tertutup — dan itu kebetulan kelas yang paling ingin ditolong.

Plafon **kehadiran** 0,4946 tegas di atas ambang, tetapi itu **mekanisme berbeda
dengan plafon berbeda**, bukan penyelamat gerbang yang gagal. Bila mau dikejar,
ia harus didaftarkan sebagai hipotesis tersendiri dengan ambangnya sendiri.

**Kaveat proksi:** bobot yang tersedia yolo26n, bukan RF-DETR-L. Menjawab "ada
ruang?", bukan "berapa besar ruangnya". P3 definitif menunggu F-004.

### Implementasi K1 dan K2 — uji sambungan LULUS

Keduanya menambal `rfdetr` saat runtime, tidak mem-fork paket (pola
`train_rfdetr_4ch.py` / `train_rfdetr_fusion_late.py`).

- **K1**, keempat lengan: γ = 0 → selisih **tepat 0,0** (no-op eksak); γ = 1 →
  0,86–1,36 (tersambung); parameter tambahan **identik 192.289** di semua lengan,
  sehingga syarat kontrol berparameter sama terbukti, bukan diasumsikan.
- **K2**, lima pemeriksaan: α = 0 → 0,0; α = 1 → berubah; residu maks **0,3 = ε
  persis** (penjaga peringkat bekerja); kanal mati tak tersentuh; dan yang
  terpenting **gradien sampai ke kepala ordinal** (`ordinal.weight` norm 35,51,
  `alpha` −3,91, tembus ke backbone). Pemeriksaan terakhir itu yang membedakan K2
  dari CORAL laporan Gemini, yang dibuang justru karena di-`stop_gradient` penuh
  sehingga **tidak dapat** menggerakkan mAP50.

## 5. Putusan

| Komponen | Putusan | Dasar |
|---|---|---|
| **K1** | **LOLOS gerbang**, lanjut ke F-007 | F-002: +0,0731 pada B4, 3× ambang |
| **K2** | **menunggu** gerbang F-005 | butuh dump logit F-004 |
| **K3** | **DIPALSUKAN (lemah)**, dibatalkan | F-003: 0,2794 < 0,30; B4 0,1038 |

Karena tinggal dua komponen, syarat F-009 ("≥ 2 lolos") sekarang menuntut
**keduanya** lolos.

**Yang belum boleh diklaim.** Tidak satu pun angka di atas adalah kenaikan mAP.
F-002 menutup satu mode gagal; ia tidak meramalkan kenaikan. Keterpisahan piksel
bukan AP. Bukti penjaga-peringkat K2 membuktikan **keamanan, bukan potensi naik**
— ia menjamin urutan tidak rusak, bukan bahwa ada cukup kerugian AP yang tinggal
di pasangan rapat untuk direbut. Itu yang dijawab F-005.

**Ambang +0,05 sendiri belum tervalidasi untuk jalur ini** (varians 0,0321 E-027
dan 0,0488 E-031 diukur pada SawitMVC-Depth dengan YOLO26n). F-004 memberi
varians seed jalur RGB RF-DETR yang sampai kini **nol terukur** — dan angka itu
yang menentukan apakah ambangnya diturunkan, dipertahankan, atau seri ini
dihentikan karena tidak dapat diukur.

## 6. Rujukan

- Laporan seri, catatan teknis, dan peta skrip: [SERI-F.md](../SERI-F.md)
- Entri kronologis: [EKSPERIMEN.md](../EKSPERIMEN.md) F-001, F-002, F-003
- Diagnosis yang menopang: [SR-007](SR-007-diagnosis-b4.md) (B4 tekstur),
  [SR-008](SR-008-kanal-tekstur.md) (kanal tekstur),
  [SR-009](SR-009-ordinalitas-kelas.md) (ordinalitas kelas),
  [SR-016](SR-016-konsistensi-lintas-sisi.md) (konsistensi lintas-sisi)
- Bukti: `evidence/experiments/results/F-001…F-007/`
