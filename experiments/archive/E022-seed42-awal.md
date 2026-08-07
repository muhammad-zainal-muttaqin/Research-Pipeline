# E-022: snapshot metrik seed-42 awal

**Status: arsip historis, sebagian tercemar, tidak layak dikutip sebagai hasil
peningkatan deteksi.** Dokumen ini memindahkan tabel E-022 dari `METRICS.md`
tanpa mengubah angka yang dicatat pada commit `e8a0866`.

Audit pada commit `f0901de` menemukan cacat pada kontrol depth pohon lain,
kontrol derau, seed RF-DETR, dan perbedaan evaluator. Karena itu, tabel di
bawah mempertahankan rekam awal E-022, bukan metrik final. Untuk koreksi dan
status setiap cacat, baca [AUDIT-E022.md](../AUDIT-E022.md) terlebih dahulu.

Pipeline sensor dan reproyeksi intrinsik-ekstrinsik tetap merupakan hasil
teknis yang tervalidasi. Tabel performa deteksi seed-42 tidak membuktikan
kenaikan mAP.

## Konteks data dan protokol

SawitMVC-Depth berbeda dari SawitMVC E-001 sampai E-021: 352 pohon, 1.408
citra 1280x800, dan 2.299 kotak. Split per pohon 245/35/72 memiliki irisan nol
dan stratifikasi perangkat, unit kamera, serta kelas dominan. Semua model
dilatih 60 epoch pada seed 42 dan resolusi 640. Kanal depth direproyeksi penuh
ke bidang color dengan z-buffer; rentang depth memakai Z_NEAR 0,8 dan Z_FAR
15,0 m.

## Run awal dengan evaluator Ultralytics

**Status tabel: historis.** Kontrol derau dan depth pohon lain dalam snapshot
ini terdampak cacat yang dijelaskan oleh audit.

| Run | Kanal ke-4 | mAP50 | mAP50-95 | B1 | B2 | B3 | B4 |
|---|---|---:|---:|---:|---:|---:|---:|
| yolo26n_rgb_seed42 | RGB | 0,3219 | 0,1072 | 0,6559 | 0,3851 | 0,1168 | 0,1296 |
| yolo26n_rgbd_seed42 | depth | 0,3492 | 0,1230 | 0,6245 | 0,4431 | 0,1861 | 0,1429 |
| yolo26n_derau_seed42 | derau | 0,3523 | 0,1170 | 0,6802 | 0,4180 | 0,2170 | 0,0940 |
| yolo26n_tukar_seed42 | depth pohon lain | **0,3771** | **0,1405** | 0,6704 | 0,4557 | 0,2298 | 0,1526 |
| rtdetr-l_rgb_seed42 | RGB | **0,4070** | **0,1376** | 0,7383 | 0,4662 | 0,1763 | **0,2472** |
| rtdetr-l_rgbd_seed42 | depth | 0,3882 | 0,1347 | 0,7647 | 0,4400 | 0,1884 | 0,1595 |
| rtdetr-l_derau_seed42 | derau | 0,3552 | 0,1142 | 0,6743 | 0,4249 | 0,2323 | 0,0892 |

RF-DETR Nano memakai paket terpisah. Val EMA terbaik yang tercatat: RGB
0,4555/0,1600 pada epoch 13, depth 0,4911/0,1786 pada epoch 10, dan derau
0,5093/0,1815 pada epoch 11.

| Kanal ke-4 | YOLO26n (2,57 jt) | RT-DETR-L (33,0 jt) |
|---|---:|---:|
| RGB, 3 kanal | 0,3219 | **0,4070** |
| depth sensor terregistrasi | 0,3492 | 0,3882 |
| derau acak | 0,3523 | 0,3552 |
| depth pohon lain | **0,3771** | - |

## Selisih berpasangan `pycocotools`

**Status tabel: historis.** CI memakai bootstrap 2.000 kali per pohon. Audit
menetapkan bahwa angka ini tidak boleh menjadi dasar klaim akhir tentang
peningkatan deteksi.

| Model | RGB | RGB-D | Delta | CI95 | P(>0) |
|---|---:|---:|---:|---|---:|
| YOLO26n | 0,3249 | 0,3501 | +0,0252 | [−0,0215; +0,0632] | 0,851 |
| RF-DETR Nano | 0,4196 | 0,4635 | +0,0439 | [+0,0000; +0,0918] | 0,975 |
| RT-DETR-L | 0,4076 | 0,3900 | −0,0177 | [−0,0669; +0,0203] | 0,225 |
| YOLO26n derau | 0,3249 | 0,3686 | **+0,0437** | **[+0,0051; +0,0875]** | 0,991 |

| Model | Derau | Depth | Delta | CI95 | P(>0) |
|---|---:|---:|---:|---|---:|
| YOLO26n (2,57 jt) | 0,3686 | 0,3501 | −0,0186 | [−0,0694; +0,0191] | 0,194 |
| RF-DETR Nano | 0,4547 | 0,4635 | +0,0087 | [−0,0372; +0,0538] | 0,649 |
| RT-DETR-L (33,0 jt) | 0,3535 | 0,3900 | **+0,0365** | [−0,0014; +0,0668] | 0,971 |

Catatan awal per kelas mencatat depth minus derau: YOLO26n B1 −0,0734
[−0,1156; −0,0297], RF-DETR Nano B1 −0,0446 [−0,0876; −0,0008], RT-DETR-L
B1 +0,0698 [+0,0306; +0,1100], dan B4 +0,1001 [+0,0062; +0,1618]. Angka ini
historis dan tidak mengubah status pencabutan di atas.

Kontrol registrasi awal, depth benar minus depth pohon lain pada YOLO26n,
mencatat −0,0220 [−0,0506; +0,0085] dan B1 −0,0662 [−0,1089; −0,0199].

## AP50 per kelas pada snapshot awal

**Status tabel: historis.** Tabel ini mempertahankan AP50 seed-42 yang semula
berada di `METRICS.md`.

| Model | Kanal ke-4 | mAP50 | B1 | B2 | B3 | B4 |
|---|---|---:|---:|---:|---:|---:|
| YOLO26n | RGB | 0,3249 | 0,6598 | 0,4342 | 0,0889 | 0,1166 |
| YOLO26n | depth | 0,3501 | 0,6102 | 0,4394 | 0,2001 | 0,1506 |
| YOLO26n | derau | 0,3686 | 0,6836 | 0,4300 | 0,2215 | 0,1393 |
| YOLO26n | depth pohon lain | 0,3721 | 0,6765 | 0,4392 | 0,2057 | 0,1671 |
| RT-DETR-L | RGB | 0,4076 | 0,7360 | 0,4678 | 0,1770 | **0,2497** |
| RT-DETR-L | depth | 0,3900 | **0,7621** | 0,4456 | 0,1891 | 0,1631 |
| RT-DETR-L | derau | 0,3535 | 0,6923 | 0,4287 | 0,2300 | 0,0630 |
| RF-DETR Nano | RGB | 0,4196 | 0,7335 | 0,4504 | 0,2738 | 0,2207 |
| RF-DETR Nano | depth | **0,4635** | 0,7038 | **0,5569** | **0,3717** | 0,2214 |
| RF-DETR Nano | derau | 0,4547 | 0,7484 | 0,5425 | 0,3376 | 0,1903 |

## Registrasi depth E-022a

**Status: hasil teknis.** Reproyeksi penuh mengungguli resize langsung pada
mutual information, tetapi hasil ini tidak membuktikan kenaikan mAP.

| Pemetaan | MI (bit) |
|---|---:|
| H1 resize langsung | 0,2546 |
| H2 affine-intrinsik | 0,2591 |
| H3 reproyeksi penuh | **0,2852** |
| H3 digeser +24 px | 0,2385 |
| H3 digeser −24 px | 0,2320 |

H3 minus H1 adalah **+0,0306 bit, CI95 [+0,0260; +0,0354]**. H3 unggul pada
84% dari 150 citra. Sidecar `alignedTo: "color"` tidak berarti buffer sudah
berada pada grid kamera color.

## Sumber angka

Semua angka berasal dari `experiments/results/E-022/`: `mi.json`,
`pycoco_yolo26n.json`, `paired_yolo26n.json`, `paired_rtdetrl.json`,
`paired_rfdetrnano.json`, `paired_derau.json`,
`paired_*_depth_vs_derau.json`, `paired_yolo26n_depth_vs_tukar.json`, dan
`depth_meta.json`. Indeks artefaknya ada di
[`experiments/results/README.md`](../results/README.md).
