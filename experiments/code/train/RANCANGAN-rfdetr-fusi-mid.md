# Rancangan (ditangguhkan): fusi MENENGAH RGB+depth untuk RF-DETR

Status: **belum diimplementasikan, dengan sengaja.** Dokumen ini adalah keluaran
dari sesi pemetaan+implementasi E-023-untuk-RF-DETR (1 Agustus 2026), bukan janji
pengerjaan. Fusi AKHIR sudah diimplementasikan dan diuji CPU di
`train_rfdetr_fusion_late.py` — baca berkas itu dulu, termasuk KAVEAT 1–3 di
kepala docstring-nya, sebelum melanjutkan dokumen ini.

## Kenapa ditangguhkan

`train_fusion_2branch.py` (YOLO26) mendefinisikan fusi menengah sebagai "cabang
depth ringan berjalan sampai P2/4, lalu difusikan ke cabang RGB sebelum P3".
Definisi itu bertumpu pada CNN berjenjang: ada tahap spasial P2/P3/P4/P5 yang
downsampling-nya EKSPLISIT dan bertahap, jadi "sebelum P3" adalah titik yang
jelas dan murah untuk dipotong.

RF-DETR (`rfdetr` 1.8.3) tidak punya tahap spasial semacam itu. Backbone-nya
`WindowedDinov2WithRegistersEncoder` — SATU ViT 12-lapisan yang token gridnya
beresolusi KONSTAN sepanjang seluruh forward (hanya di-stride sekali oleh
patch-embed di awal). "P3/P4/P5" yang muncul di config (`projector_scale`)
adalah keluaran `MultiScaleProjector`: ia mengambil keluaran 4 LAPISAN
TRANSFORMER yang beresolusi SAMA (indeks token ke-3, 6, 9, 12 dari 12) lalu
meng-upsample/downsample masing-masing secara konvolusional untuk MENIRU
piramida — bukan piramida spasial yang nyata. Diverifikasi langsung dari source
`rfdetr/models/backbone/dinov2_with_windowed_attn.py:790-834` (loop
`WindowedDinov2WithRegistersEncoder.forward`) dan
`rfdetr/models/backbone/backbone.py:95-99` (`level2scalefactor`).

Konsekuensinya: **"fusi menengah" untuk RF-DETR tidak punya definisi yang bisa
ditransfer langsung dari YOLO26.** Ia harus didefinisikan ulang sebagai "fusi
TOKEN setelah blok transformer ke-k", dan definisi baru itu sendiri adalah
keputusan desain — bukan pekerjaan implementasi dari resep yang sudah ada.

## Apa yang perlu diputuskan sebelum menulis kode

Empat keputusan, masing-masing perlu verifikasi forward-pass sendiri (bukan
sekadar dipilih di atas kertas):

1. **Di lapisan transformer keberapa fusi terjadi (k).** `out_feature_indexes`
   RF-DETR-L adalah `[3, 6, 9, 12]` — jika fusi terjadi tepat di salah satu titik
   itu, proyektor bisa dipakai ulang; jika di antara dua titik, proyektor untuk
   cabang RGB dan depth sebelum fusi harus dibangun terpisah dari nol (tidak ada
   `out_feature_indexes` parsial yang siap pakai untuk k sembarang).

2. **Dua patch-embed terpisah, dua urutan token paralel.** Beda dari topeng
   E-023 (`_Topeng` di `train_fusion_2branch.py`) yang menutup kanal tapi tetap
   SATU conv/SATU graf: `Dinov2WithRegistersPatchEmbeddings.forward`
   (`dinov2_with_windowed_attn.py:307-311`) memvalidasi `num_channels` secara
   ketat PER INSTANCE conv. Tidak ada cara "menutup kanal lalu tetap lewat conv
   yang sama" pada level token ViT seperti pada conv spasial CNN — wajib dua
   modul patch-embed dan dua urutan `hidden_states` berjalan paralel sampai
   lapisan k.

3. **Token CLS/register tidak berkorespondensi spasial.** DINOv2-with-registers
   (dipakai bila `use_registers=True`) punya token CLS + N token register per
   cabang (`WindowedDinov2WithRegistersEmbeddings`,
   `dinov2_with_windowed_attn.py:317+`). RF-DETR-L (encoder
   `dinov2_windowed_small`, TANPA `registers` di nama) tidak memakainya, tapi
   varian lain (nano/small/medium: `dinov2_windowed_small` juga tanpa registers
   — periksa ulang per varian sebelum asumsi) mungkin beda. Kalau ada token
   CLS/register di kedua cabang, memutuskan cara menyatukannya saat fusi (pakai
   satu, buang satu, atau concat+proyeksi seperti token patch) adalah keputusan
   baru tanpa preseden di korpus atau di `train_fusion_2branch.py`.

4. **Jadwal windowed-attention harus disinkron antar cabang.**
   `window_block_indexes` (dipakai `run_full_attention` di
   `WindowedDinov2WithRegistersEncoder.forward:808`) dihitung SEKALI dari
   `out_feature_indexes` di `DinoV2.__init__`
   (`rfdetr/models/backbone/dinov2.py:97-99`). Kalau cabang depth punya
   `out_feature_indexes` berbeda dari RGB (misalnya karena depth "diperkecil" —
   lihat batasan di bawah), kedua cabang punya jadwal attention lokal-vs-global
   yang tidak sinkron pada lapisan k, dan efeknya terhadap fusi token belum
   diuji sama sekali.

## Batasan tambahan yang sudah diverifikasi (bukan spekulasi)

- **Tidak ada cara memperkecil cabang depth seperti `lebar_bagi` YOLO26.**
  Keluarga config DINOv2 di paket ini hanya punya JSON untuk
  `small` (384-d) / `base` (768-d) / `large` (1024-d)
  (`rfdetr/models/backbone/dinov2.py: size_to_config`) — tidak ada `tiny`.
  `Backbone.__init__` akan `KeyError` untuk `size='tiny'` (diverifikasi
  langsung, lihat riwayat sesi ini). Memperkecil cabang depth berarti menulis
  config `num_hidden_layers`/`hidden_size` kustom dari nol, kehilangan seluruh
  kompatibilitas dengan checkpoint pratlatih DINOv2 mana pun untuk cabang itu
  (masalah yang SUDAH ada untuk fusi akhir — lihat KAVEAT 1
  `train_rfdetr_fusion_late.py` — dan menjadi lebih rumit di sini karena
  potongan lapisan k harus tetap cocok antar dua config berbeda).
- Memotong ViT di tengah blok berarti seluruh sisa jaringan setelah lapisan k
  (blok k+1..11, projector, transformer LWDETR) mulai belajar dari representasi
  gabungan yang BELUM PERNAH dilihat DINOv2 pratlatih — beda dari fusi akhir,
  di mana hanya cabang depth yang acak dan cabang RGB tetap menjalankan seluruh
  DINOv2 pratlatih tanpa gangguan sampai titik fusi (setelah blok ke-12, bukan
  di tengah).

## Rekomendasi

Jangan kerjakan fusi menengah sampai:

1. Fusi akhir (`train_rfdetr_fusion_late.py`) sudah dilatih (bukan cuma
   dibangun) dan hasilnya memberi sinyal bahwa jalur RF-DETR RGB-D ini layak
   dikejar lebih jauh — tidak ada gunanya membedah encoder ViT untuk varian
   fusi yang lebih murah sebelum tahu varian yang lebih mahal dan lebih aman
   pun tidak menunjukkan sinyal.
2. Strategi pratlatihan (KAVEAT 1 di `train_rfdetr_fusion_late.py`) sudah
   diputuskan dan dicatat — keputusan itu berlaku untuk fusi menengah juga,
   dan lebih murah diputuskan sekali di titik fusi yang lebih sederhana.
3. Keempat keputusan desain di atas sudah dijawab EKSPLISIT dan dicatat di
   dokumen ini (revisi berikutnya), sebelum satu baris kode fusi menengah
   ditulis — mengikuti semangat "peta indeks eksplisit" `train_fusion_2branch.py`:
   petanya harus digambar dulu, baru dieksekusi.
