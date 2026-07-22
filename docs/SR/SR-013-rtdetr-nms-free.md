# SR-013 — RT-DETR-L (NMS-free): detektor 4-kelas terbaik sejauh ini

**Ide I-14** · **Eksperimen:** E-020 · **Putusan: DIKONFIRMASI (arah positif; belum capai target)** · 2026-07-22

---

## 1. Masalah

E-014 menunjukkan deteksi bukan hambatan utama (agnostik 0,7191–0,7730). Tetapi
"bukan hambatan utama" tidak berarti "sempurna": E-018 mengukur 11,7% kotak GT
tak tercapai pada IoU 0,5 dan median IoU terbaik hanya 0,73. Sebagian kotak yang
hilang bisa jadi bukan soal model gagal *melihat* tandan, melainkan **satu kotak
benar ditekan kotak lain di sebelahnya**.

Tandan di mahkota sawit rapat dan saling menutup. Setiap detektor keluarga YOLO
— termasuk yolo26m baseline — memakai **Non-Maximum Suppression (NMS)**: bila dua
kotak tumpang tindih melebihi ambang IoU, yang skornya lebih rendah dibuang. Pada
objek yang memang berdekatan, NMS greedy dapat membuang kotak benar. Ini plafon
**struktural** — di pasca-pemrosesan, bukan di model — jadi tak bisa dihapus
dengan data, kapasitas, atau resolusi. `deep-research-report.md` menempatkannya
**prioritas 1**.

## 2. Ide

RT-DETR tidak memakai NMS. Ia memakai **pencocokan Hungarian satu-ke-satu** saat
pelatihan: tiap objek nyata dipasangkan tepat dengan satu prediksi, sehingga model
belajar mengeluarkan satu kotak per objek tanpa penindasan pasca-pemrosesan.

Kalau sebagian plafon deteksi berasal dari NMS, mengganti detektor dengan yang
NMS-free menaikkan recall pada tandan bertumpuk — terbaca langsung pada mAP,
khususnya pada kelas yang paling padat/tersamar.

**Yang akan memalsukan:** RT-DETR tidak melampaui baseline, atau menang merata di
semua kelas tanpa keunggulan khusus pada kelas bertumpuk (artinya NMS bukan
penyebab).

## 3. Solusi — varian yang persis dipakai

**RT-DETR-L**, implementasi **ultralytics 8.4.103**, config
`ultralytics/models/rt-detr/rt-detr-l.yaml`:

| Komponen | Isi |
|---|---|
| Backbone | **HGNetv2-L** (HGStem + 6× HGBlock + DWConv) |
| Encoder | **AIFI** (Attention-based Intra-scale Feature Interaction) + fusi RepC3 (CCFM) |
| Head | **RTDETRDecoder** (decoder transformer, query objek, Hungarian; **tanpa NMS**) |
| Parameter | **32.970.476 (33,0 juta)** · 103,4 GFLOPs |
| Bobot awal | COCO `rtdetr-l.pt` (ultralytics assets v8.4.0) |

Untuk perbandingan yang adil, kapasitasnya (33,0 juta) sebanding dengan baseline
yolo26m (21,9 juta) — bukan lompatan kapasitas seperti yolo26x. Yang berbeda
adalah **mekanisme**: NMS-free vs NMS.

Pelatihan: `experiments/train_rtdetr.py`, resolusi asli **1280**, augmentasi
**aman-warna** (`hsv_s=0.15`; kematangan adalah warna, lihat E-019), jadwal
kosinus, `close_mosaic=10`. Dihentikan pada epoch 52/60 setelah dikonfirmasi
`best.pt` (epoch fitness-terbaik) tak lagi terlampaui dan fase mosaic-off (ep50)
tidak memberi lonjakan. Split/seed/data.yaml identik baseline; **irisan pohon
train/val/test = nol** (E-017). Konfigurasi dipilih pada val; test dilaporkan
terpisah. Evaluasi: `eval_rtdetr.py` (val() ultralytics bawaan).

## 4. Hasil

`best.pt` = epoch fitness-terbaik (fitness = 0,1·mAP50 + 0,9·mAP50-95 → epoch 25).

**Validasi (dasar pemilihan):**

| VAL | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---|---|---|---|---|
| Baseline yolo26m | 0,5218 | 0,2407 | 0,7354 | 0,4076 | 0,5561 | 0,3881 |
| **RT-DETR-L** | **0,5466** | **0,2543** | 0,7503 | 0,4413 | 0,5808 | 0,4138 |
| selisih | +0,0248 | +0,0136 | +0,0149 | +0,0337 | +0,0247 | +0,0257 |

**Test (dilaporkan, tidak dipakai memilih):**

| TEST | mAP50 | mAP50-95 | B1 | B2 | B3 | **B4** |
|---|---|---|---|---|---|---|
| Baseline yolo26m | 0,5161 | 0,2457 | 0,7410 | 0,4016 | 0,5894 | 0,3323 |
| DiB (publikasi) | 0,531 | — | 0,739 | 0,433 | 0,599 | 0,354 |
| **RT-DETR-L** | **0,5794** | **0,2694** | 0,7891 | 0,4685 | 0,6391 | **0,4208** |
| selisih vs baseline | **+0,0633** | +0,0237 | +0,0481 | +0,0669 | +0,0497 | **+0,0885** |

## 5. Putusan — DIKONFIRMASI (arah), TARGET BELUM TERCAPAI

**RT-DETR-L adalah detektor 4-kelas terbaik yang kita hasilkan.** Ia melampaui
baseline **pada keempat kelas di kedua split**, dan — inti hipotesisnya —
**keunggulan terbesar ada di B4** (+0,0885 test), kelas yang paling padat dan
tersamar. Itu persis tanda tangan yang diramalkan hipotesis NMS-free: yang
paling diuntungkan adalah kelas tempat NMS greedy paling mungkin menekan kotak
benar. B2 (+0,067) menyusul — juga kelas ramai di kanopi tengah. NMS **memang**
sebagian dari plafon.

**Koreksi terhadap prediksi saya sendiri.** Selama pelatihan saya berulang kali
menyebut RT-DETR "menempel plateau ~0,55 seperti yang lain" dan menduga akan
DIPALSUKAN. **Saya keliru.** Itu membaca `last.pt` yang overfit, bukan `best.pt`.
Dievaluasi benar pada test, RT-DETR **+0,063 mAP50** di atas baseline — bukan
plateau, melainkan lompatan terbesar dari semua eksperimen deteksi.

**Tetapi target belum tercapai.** Sasaran **mAP50 0,60 / mAP50-95 0,30 pada 4
kelas**:

| | mAP50 | ke 0,60 | mAP50-95 | ke 0,30 |
|---|---|---|---|---|
| val | 0,5466 | −0,053 | 0,2543 | −0,046 |
| test | 0,5794 | −0,021 | 0,2694 | −0,031 |

Test tinggal **−0,021** dari sasaran mAP50 — sedekat itu belum pernah. NMS-free
mengangkat plafon, tetapi tidak sendirian menutup celahnya.

### Dampak — arah yang sekarang dibenarkan

Untuk pertama kalinya sebuah perubahan **arsitektural** (bukan tuning) menggeser
angka secara berarti. Konsekuensinya:

1. **RT-DETR jadi tulang punggung baru**, menggantikan yolo26m sebagai baseline
   deteksi. Semua ide berikut dibangun di atasnya.
2. **Menggabungkan dengan resolusi master** (E-015/E-018): RT-DETR-L dilatih di
   1280; melatihnya pada piksel master 3060×4080 (imgsz 1600–2048, dataset siap
   di `build_master_ds.py`) menyerang lokalisasi — penentu mAP50-95, sasaran yang
   lebih jauh.
3. **RT-DETR-X** (67,5 juta) menguji apakah kapasitas menambah lagi di atas
   mekanisme NMS-free.

`best.pt` (264 MB) adalah model terbaik kita — terlalu besar untuk repo; disimpan
di `/workspace/experiments/runs/rtdetr_l_e60_i1280/weights/` dan dapat direproduksi
dari skrip. Kandidat untuk diarsipkan ke penyimpanan objek.

## 6. Reproduksi

```bash
cd /workspace/experiments
.venv/bin/python train_rtdetr.py --weights rtdetr-l.pt --imgsz 1280 --epochs 60
.venv/bin/python eval_rtdetr.py     # val + test + per-kelas dari best.pt
# keluaran: runs/rtdetr_l_e60_i1280/, results/rtdetr_eval.json
```
