# Brief deep research — menembus plafon 0,6038 mAP50

> **Catatan bahasa.** Isi brief di bawah ditulis dalam bahasa Inggris karena
> sasarannya adalah penelusuran pustaka berbahasa Inggris oleh agen riset
> eksternal. Ini pengecualian yang disengaja terhadap aturan bahasa repo, dan
> hanya berlaku untuk berkas ini.

**Fungsi berkas ini.** Paket pengarahan untuk mendelegasikan pencarian pustaka ke
agen deep research eksternal, tanpa agen tersebut mengulang 30 eksperimen yang
sudah dijalankan di sini. Setiap angka empiris di dalamnya bertanda ID
eksperimen, split, dan model — periksa balik ke [EKSPERIMEN.md](EKSPERIMEN.md)
dan [METRICS.md](METRICS.md) sebelum mengutipnya ke luar.

**Statusnya bukan hasil.** Berkas ini tidak memuat temuan baru dan tidak boleh
dikutip sebagai bukti. Ia hanya merangkum keadaan bukti per 5 Agustus 2026 dalam
bentuk yang dapat dibaca pihak luar. Bila hasil eksperimen berubah, §3 dan §5 di
bawah ikut usang — perbarui atau tandai.

> **Koreksi 7 Agustus 2026 — versi ini v2, jangan pakai v1.** Versi pertama brief
> ini memuat daftar Research Directions A–F **tanpa satu pun direction untuk
> depth**, sehingga kedua agen deep research (5 Agustus) mengembalikan nol usulan
> RGB-D. Itu cacat penyusunan brief, bukan temuan: sasaran O2 — cara memasukkan
> depth yang benar — justru pertanyaan yang paling terbuka dan menjadi dasar
> keputusan perangkat keras proyek. Yang diperbaiki di v2: §1 kini menyatakan dua
> objektif eksplisit, §5.5 dipersempit agar tidak terbaca sebagai larangan atas
> modalitas depth, **§8 Direction G ditambahkan dan ditandai wajib**, dan §10
> memuat pemeriksaan mandiri untuknya. **Deep research wajib dijalankan ulang
> dengan v2.** Hasil v1 tetap berlaku untuk jalur RGB dan tidak perlu dibuang.

---

## 0. HOW TO READ THIS BRIEF

This is not a blank-slate question. Thirty logged experiments already ran on this
exact problem (IDs E-001 … E-032; **E-008 was never used**, and the experiment
planned as **E-023 was executed as E-032** — the E-023 number survives only as an
evidence-directory name). Most of the obvious ideas are **already falsified with
numbers**. Your value is *not* in re-deriving the diagnosis — it is in finding
what nobody here has tried.

Every empirical number below is tagged with its experiment ID, the split it was
measured on, and the model it was measured with. **Preserve that discipline in
your answer.** A recommendation that cannot state which failure mode it targets,
on which split, at what cost, is not usable.

Two datasets are involved and **their numbers are not comparable**. Do not mix them:

| | SawitMVC (RGB) | SawitMVC-Depth |
|---|---|---|
| Role | Where the 0,6038 ceiling lives | Where all depth / variance work lives |
| Size | 953 trees, 3.992 images 960×1280, 18.540 boxes | 352 trees, 1.408 images 1280×800, 2.299 boxes |
| Density | 4,64 boxes/image | 1,63 boxes/image |
| Class balance | **B3-heavy: B3 51,6 % / B1 9,7 %** (test split measured: B3 1.409 · B2 496 · B4 455 · B1 252 of 2.612 boxes) | B2 43,5 % / B1 36,1 % / B3 14,0 % / B4 6,4 % |
| Absolute mAP50 scale | ~0,52–0,60 | ~0,35 |
| Extra modality | none | Orbbec active-IR depth, Y16 848×480 |

---

## 1. ROLE, OBJECTIVE, AND THE NOVELTY BAR

Act as a Senior Computer Vision Research Scientist specializing in **fine-grained
agricultural object detection**, **ordinal classification**, **RGB-D / multimodal
fusion**, and **camouflaged / low-contrast object detection**. Search CVPR, ICCV,
ECCV, WACV, NeurIPS, ICLR, IEEE T-PAMI, IEEE T-IP, *Computers and Electronics in
Agriculture*, *Plant Phenomics*, and arXiv preprints, **2022–2026**.

**Two objectives, and the second is the one with an open engineering question.**

| | Objective | State |
|---|---|---|
| **O1** | Push the RGB detector past 0,6038 mAP50 on SawitMVC | RF-DETR-L already reached it (E-021); further RGB gains are welcome but the track is mature |
| **O2** | **Determine the correct way to integrate sensor depth into a high-capacity pretrained detector** | **Open.** Three attempts falsified the *entry point* (input-channel concatenation), never the modality. This is the question the project's hardware decision rests on |

O2 is not optional or secondary. The deployed hardware is an Orbbec Gemini depth
camera and the field application already exists; what is missing is the
architecture that makes the fourth modality earn its place. **An answer that
returns nothing on O2 does not satisfy this brief**, regardless of how strong its
RGB recommendations are.

**The novelty bar is explicit and non-negotiable.** The research team has spent
months implementing standard off-the-shelf techniques from the literature — SAHI,
tiling, augmentation sweeps, hyperparameter search, batch/image-size tuning,
model scaling within the YOLO family — and **not one of them moved mAP**. A gain
of 2–5 % relative is considered **insufficient**. What is being asked for is a
change in **problem formulation, loss geometry, or architecture** — not a recipe.

Therefore:

> **If your recommendation could be implemented by reading a library's README and
> flipping a flag, it is out of scope.** If it has already been applied to oil
> palm FFB detection in a published paper, say so and explain what it left on the
> table — do not present it as new.

---

## 2. THE PROBLEM, STATED PRECISELY

Detect and grade oil palm Fresh Fruit Bunches inside a dense canopy from
smartphone photos taken from 4–8 sides of each tree. Four ordinal ripeness
grades, **B1 = ripe (orange-red)** declining monotonically to **B4 = unripe (dark
greenish)**. B2 and B3 are intermediate ordinal steps; the annotation guide does
not give them independent visual definitions beyond their position on the
ripeness continuum.

**The failure splits into two mechanisms, and they are NOT the same problem.**
This separation is the single most important fact in this brief:

| Mechanism | What fails | Evidence | Which class |
|---|---|---|---|
| **(A) Geometric / camouflage** | The bunch is never *found*. Dark green fruit against green fronds; small, embedded, self-occluded. | E-010/SR-007: B4 background contrast ΔE **11,55**, *below* the random-box control **12,92**. E-028: B4 cross-side prediction inconsistency 0,234 ≈ B1 0,235 → B4's low AP is a **detection** failure, not class confusion. | **B4** |
| **(B) Photometric / ordinal** | The bunch is found but *graded wrong*, always to an adjacent grade. | E-012/SR-009: the six largest confusions are all ordinal distance 1; the distance-2 jump B3→B1 occurs in only 1,9 % (7/375). E-028: the most ambiguous class is **B2 (0,434)**, not B4. | **B2 ↔ B3** |

**A proposal that claims to fix both mechanisms with one mechanism is suspect and
must justify itself.** Depth, texture, and resolution address (A). Loss geometry
and calibration address (B). They do not substitute for each other.

**Downstream task.** The deployed application is *counting*, not grading per se.
The published baseline (Data in Brief 67 (2026) 112990, DOI
`10.1016/j.dib.2026.112990`) shows counting accuracy collapsing from **96,81 %**
(ground-truth boxes + SVR) to **75,35 %** (YOLO26m boxes + SVR). The counter is
already near-perfect given clean detections. **The detector is the bottleneck.**
Note that the counting metric uses a **±1 grade tolerance** while mAP50 does not —
this asymmetry matters for Direction A below.

---

## 3. WHAT IS ALREADY ESTABLISHED — DO NOT RE-DERIVE

### 3.1 Confirmed findings (treat as given)

| ID | Finding | Numbers |
|---|---|---|
| **E-014** | The bottleneck is classification, not localization. | Identical weights (yolo26m), identical val: 4-class **0,5218** mAP50 vs class-agnostic **0,7191**. Classification efficiency 72,6 %. |
| **E-020 / E-021** | The gain comes from **NMS-free architecture**, not capacity. Single-protocol pycocotools, test mAP50: YOLO26m (21,9 M) 0,5165 · YOLO26l (26,3 M, param-fair @1280, identical config) 0,5300 · RT-DETR-L (33,0 M) 0,5784 · **RF-DETR-L (35,7 M, DINOv2) 0,6038 / 0,2770 mAP50-95**. The param-fair YOLO still loses to both DETRs. | Current SOTA of this project. |
| **E-012 / SR-009** | Maturity is a **continuous variable cut into four boxes**. End classes (B1 70,2 %, B4 62,9 % recall) beat middle classes (B2 42,4 %, B3 41,6 %) because middle classes have two neighbours. | Confusion is ordinal. |
| **E-011 / SR-008** | **High-frequency texture separates B4; contrast enhancement does not.** Pixel-level AUC over a random-box control: Laplacian **+0,0458**, Sobel **+0,0367**, CLAHE **−0,0080**, unsharp **−0,0066**. Rank reversal: B4 goes from *least* separable in luminance (0,5573) to *most* separable in Laplacian (0,6153). | Motivates Direction B. |
| **E-018** | **Annotation tightness caps the metric.** val: median best-IoU 0,7303; only 3,76 % of GT boxes reachable at IoU ≥ 0,90. Ceiling mAP50 **0,8834**, ceiling mAP50-95 **0,4702**. Current 0,6038/0,2770 = 68 % / 59 % of ceiling. | mAP50-95 will always be much harder here. |
| **E-028 / SR-016** | Cross-side prediction inconsistency, measured **without human labels** using the dataset's `_confirmedLinks` identity graph: **0,2329** over 511 physical bunches. A second, orthogonal metric that mAP does not capture. | Useful as a mechanism probe. |
| **E-001** | The dataset's `class_mismatch` flag is **zero** across 7.328 multi-side bunches. Annotator disagreement was consolidated before release. | **No measurement of annotator disagreement exists.** Do not build an argument on "annotators disagree" — it is unmeasured here. |

### 3.2 Falsified — never propose these again

| ID | What was falsified | The killing number |
|---|---|---|
| **E-017 / SR-012** | **Two-stage decoupled pipeline** (class-agnostic detector → crop → dedicated fine-grained classifier). Tested in its *strongest* form: stage-1 trained agnostic @960 reaching **0,7730/0,3320** (better than the 0,7191 baseline), stage-2 = ConvNeXt-Tiny on **native 3024×4032 master-resolution crops** with colour-safe augmentation. | Assembled system **0,4787** vs single-stage **0,5218** val mAP50 — worse on **all four classes**. Two documented causes: (i) crops destroy global canopy context, and ripeness is judged *relative* to its surroundings; (ii) multiplying independently-trained `p_box × p_cls` destroys joint score ranking, and AP punishes ranking damage harder than argmax error. |
| **E-011** | CLAHE, unsharp masking, naive spatial contrast enhancement. | Both *below* the unprocessed baseline. |
| **E-019** | Fine-tuning a converged 640 px checkpoint up to 1280 px. | Peak 0,5263 val, only touching the baseline, then declining. Verdict: cross-resolution fine-tuning from a converged checkpoint is the wrong strategy — train clean from COCO weights instead. This is **not** evidence that resolution fails. |
| **E-006 / SR-005** | Monocular pseudo-depth as a bunch separator. | Bunch-vs-surround AUC 0,602; contrast 0,26× the control. |
| **E-027** | Registered **sensor** depth as a 4th input channel, early fusion, YOLO26n, 3 seeds. | depth − RGB mean **−0,0230**; two of three seeds significantly NEGATIVE. Depth **harms** small models — not merely neutral. |
| **E-029** | The claim "depth is used at high capacity" (RT-DETR-L). | **Withdrawn.** The comparison rested on a noise-control arm built with faulty code. |
| **E-016 / SR-011** | The claim of a hard "maturity ceiling". | **Withdrawn** as flawed evidence. Do not cite any maturity accuracy number as a ceiling. |

### 3.3 Inconclusive or never run — this is where the room is

| ID / Idea | Status |
|---|---|
| **E-032** (gates G4/G6) | Fusion-point sweep: early vs **mid** vs late vs noise-control vs RGB, 5 arms × 3 seeds, 150 epochs from scratch, YOLO26n. All 12 paired CI95 **contain zero**. `mid` is positive on 3/3 seeds (mean +0,0139) → **INDICATION, not a finding**. Mid/late fusion is therefore **untested at scale**, not refuted. |
| **E-030** (gate G7) | Capacity sweep, **one seed only**. The `noise − RGB` column flips sign monotonically with capacity (+0,0032 → +0,0184 → −0,0325 → −0,0533), turning point between **21,9 and 26,3 M parameters**. The `depth − noise` column is **not** monotonic. Multi-seed replication (G7b) is **OPEN**. |
| **I-22 — ordinal loss / maturity regression head** | Designed, **never run**. |
| **I-21 — high-frequency texture as an extra channel** | Queued, then dropped at E-014 for GPU reallocation. **Never falsified.** |
| **I-13 — class-balanced / focal loss** | **Never run.** The imbalance is real: B3 51,6 % vs B1 9,7 %. |
| **I-15 — BiFPN-style neck** | **Never run.** |
| **I-17 — per-stratum score threshold calibration** | **Never run**, estimated ~20 minutes on existing weights, no GPU training. |
| **Master-resolution 4-class detector** | E-015 unlocked the raw 3024×4032 master via content-based matching (min score 0,9985). Crops from it were used in E-017, but a **4-class detector has never been trained on master pixels**. |
| **Camouflaged Object Detection (COD) literature** | The 182-entry local corpus contains RGB-D salient-object-detection work but **no dedicated COD entries**. B4 is literally green-on-green camouflage. This body of literature is **unsearched**. |
| **Surface normals / HHA encoding** | **Never tested here.** Do not describe it as falsified. See §6. |

---

## 4. THE MEASUREMENT REGIME — WHAT COUNTS AS A RESULT

Any proposal must survive this regime, and you must state how it will:

1. **Noise floor.** Seed-to-seed range on an identical configuration: **0,0321**
   (E-027). Split-to-split range: **0,0488** (E-031). *Caveat: both were measured
   on SawitMVC-Depth with YOLO26n, not on SawitMVC with RF-DETR-L. They are used
   here as a conservative proxy; the RGB-track noise floor is unmeasured.*
   → **A proposal whose expected gain is below ~0,05 mAP50 cannot be
   distinguished from noise on this setup.** State your expected effect size.
2. **Minimum 3 seeds.** Single-seed results have reversed conclusions three times
   in this project (E-022, E-027, E-029). Single-seed evidence will be rejected.
3. **One evaluation protocol.** `pycocotools` only, on the frozen test split.
   Mixing evaluators is a binding prohibition (E-025) — the gap scales with
   detection count.
4. **Every mAP number must name its split.** val and test differ materially here.
5. **Compute budget.** One RTX A4500, 20,4 GB VRAM. A proposal requiring more
   than roughly 3 seeds × 6 GPU-hours, or multi-GPU training, must say so
   explicitly and justify the cost.
6. **Data budget.** No re-annotation, no new field collection, no external
   dataset. Both datasets are CC BY-NC 4.0.
7. **Falsification written first.** State, before any run, what result would
   refute the proposal.
8. **Report the auxiliary probe.** If a proposal claims to fix mechanism (A) or
   (B), predict its effect on cross-side inconsistency (baseline 0,2329). A mAP
   gain with a flat inconsistency rate is a suspected capacity effect, not a
   mechanism.

---

## 5. HARD DON'Ts — falsified or out of scope

1. **DO NOT propose a two-stage crop classifier** in any form (RPN → ROI crop →
   fine-grained head, cascade classifiers, crop-and-refine). Falsified in E-017
   at native master resolution with a dedicated backbone. See §3.2 for the two
   structural causes.
2. **DO NOT propose spatial colour/contrast enhancement** — CLAHE, unsharp,
   histogram equalisation, colour-space shifts, retinex-style normalisation as a
   preprocessing step. Falsified in E-011.
3. **DO NOT propose cross-resolution fine-tuning from a converged checkpoint.**
   Falsified in E-019.
4. **DO NOT propose monocular pseudo-depth as a bunch separator.** Falsified in
   E-006. Its error is correlated with the RGB it was estimated from — it is a
   structural prior, not an independent sensor.
5. **DO NOT propose early fusion of a 4th input channel into a small detector.**
   Falsified in E-027 (depth actively harms). **Read this narrowly:** it bans one
   *entry point*, not the depth modality. Depth admitted at intermediate stages,
   through a side branch, or through any operator that leaves the pretrained stem
   intact is **explicitly in scope** — see Direction G, which is objective O2.
6. **DO NOT re-propose off-the-shelf recipes already exhausted:** SAHI, sliced
   inference, tiling, TTA, mosaic/copy-paste augmentation sweeps, hyperparameter
   search, batch-size or image-size tuning, scaling up within the YOLO family,
   swapping to a bigger COCO-pretrained backbone.
7. **DO NOT invoke "active IR depth fails under tropical solar irradiance."**
   This mechanism was asserted in a prior review and **has no measurement behind
   it** in this project. What *is* measured: valid depth pixel coverage 0,71032,
   no always-invalid rows or columns, and a noise-control arm whose behaviour is
   statistically indistinguishable from depth in most contrasts. The measured
   effect concerns **where the 4th channel enters the network**, not sensor SNR.
   Do not build on the solar story.
8. **DO NOT propose anything requiring re-annotation, new data collection, a
   different dataset, or multi-GPU training.**
9. **DO NOT propose a method whose expected gain is < 0,05 mAP50**, or whose
   effect size you cannot estimate at all.
10. **DO NOT present a published oil-palm FFB paper's method as novel.** If it
    exists in the FFB literature, cite it and state what it failed to solve.

---

## 6. SOFT DON'Ts — admissible only if your mechanism defeats the stated objection

These are not forbidden. They are **deprioritised with a specific reason**. If
you propose one, you must address the objection head-on; if you cannot, drop it.

| Direction | The objection you must defeat |
|---|---|
| Adding a 4th input channel to a **pretrained 3-channel stem** at > 21,9 M params | E-030: a channel containing *pure noise* significantly **harms** models above the 21,9–26,3 M turning point. Content does not rescue it. Also, RF-DETR's advantage is attributed to DINOv2 pretraining (E-021) — modifying `PatchEmbeddings` destroys exactly the asset that produced 0,6038. *Caveat, stated for fairness: E-030 ran on YOLO26n/m/l and RT-DETR-L on SawitMVC-Depth, never on RF-DETR-L. Extending it to DINOv2 is an inference, not a measured result.* Admissible if your mechanism **leaves the stem untouched**. |
| **HHA encoding / surface normals** | HHA's third channel *is* the surface-normal angle. The local corpus (entry 052, RedNet) records Hazirbas et al.'s finding that *"the HHA encoding does not hold more information than the depth itself."* Additionally, the available monocular depth (Depth-Anything-3) is currently **relative, not metric** (`is_metric` empty), so normals derived from it are ill-scaled; and normals are spatial derivatives, which amplify noise on boxes of median size 46–63 px. |
| **Plain LDL / EMD label smoothing** | Softening targets toward neighbouring grades raises the neighbour class's confidence on true positives. Under COCO AP that produces **high-scoring false positives in the neighbour class**, lowering its AP. LDL almost certainly raises the counting metric's `±1 accuracy` by construction while *lowering* mAP50. Admissible only in a **ranking-preserving** formulation — see Direction A. |
| Any method that trades mAP50 for `±1` counting accuracy | Admissible, but you must state the trade explicitly and quantify both sides. Do not present it as a pure win. |

---

## 7. DOs — what a usable answer looks like

1. **Name the insertion point.** For every recommendation, specify where it
   attaches in a DETR-family graph (RF-DETR-L: DINOv2 patch-16 backbone,
   LW-DETR-style NAS head, one-to-one Hungarian assignment, no NMS). "Add an
   attention module" is not an answer; "replace the classification branch of the
   decoder's last N layers with X, keeping the box branch untouched" is.
2. **Name the mechanism it targets** — (A) geometric/camouflage B4, or (B)
   photometric ordinal B2↔B3 — and **predict the per-class effect** on
   B1/B2/B3/B4 separately. A flat prediction across all four classes signals that
   the author has not engaged with §2.
3. **Give the mathematics.** Loss equations, gradient behaviour, and specifically
   **what happens to the score ranking that COCO AP consumes**. This project has
   been burned once by a method that improved argmax accuracy and destroyed
   ranking (E-017).
4. **Write the falsification condition** for each recommendation, before the
   experimental protocol.
5. **Cite primary sources** with arXiv ID or DOI, and give the reported gain
   *with its original benchmark*. No number without provenance.
6. **Report negative literature.** If a direction was tried in fine-grained or
   agricultural detection and failed, that is as valuable as a success — say so.
7. **Flag domain-transfer risk explicitly.** Methods validated on indoor scenes,
   autonomous driving, or medical imaging carry a transfer assumption to a dense
   outdoor canopy under uncontrolled illumination. Name the assumption.
8. **Rank by expected gain ÷ GPU cost**, and be honest when a promising method is
   simply too expensive for one A4500.
9. **Distinguish "not tried here" from "known to work here."** Given §3, the
   prior on any single idea working is low. Calibrate your confidence language
   accordingly — hedged claims are preferred over confident ones.

---

## 8. RESEARCH DIRECTIONS

**Direction G is objective O2 and is mandatory** — an answer that omits it is
incomplete no matter what else it contains. Among the remaining directions, E and
F are the least explored and carry the most novelty potential.

### Direction A — Ordinal loss geometry that preserves AP ranking

The confusion is ordinal (E-012), and the deployment metric already tolerates ±1
while mAP50 does not. Modern detector heads do **not** use one-hot categorical
cross-entropy over 4 classes — they use per-class BCE with IoU-weighted soft
targets (task-aligned assignment) or varifocal/focal loss. **Verify this against
the actual implementation before formulating.**

*Question:* what 2022–2026 loss functions, target-assignment schemes, or
calibration-aware heads impose an ordinal penalty **without** flattening the
intra-class score ranking that COCO AP consumes? Look at ordinal regression with
monotonic constraints, unimodal output distributions, rank-consistent
classification (the CORAL/CORN family and successors), and any work explicitly
analysing label smoothing's effect on AP rather than on accuracy.

### Direction B — High-frequency texture injection *without* touching the stem

E-011 measured a real, class-rank-reversing signal for B4 in the Laplacian /
Sobel bands. The stem is off-limits (§6).

*Question:* how can DWT sub-bands, Laplacian pyramids, or learned high-pass
features be injected via **side-tuning networks, adapters, LoRA-style branches,
cross-attention from a frozen auxiliary encoder, or feature-space modulation** at
intermediate backbone stages, leaving the pretrained 3-channel input path intact?
Include the frequency-domain-in-transformer literature (wavelet attention,
Fourier-domain token mixing) and assess whether any of it has been used for
*detection* rather than classification or restoration.

### Direction C — Fine-grained feature preservation in single-stage DETRs

P4/P5 strides (16×, 32×) discard fruitlet-scale surface detail before it reaches
the classification queries. ROI cropping to recover it is forbidden (§5.1).

*Question:* what mechanisms preserve or recover high-resolution evidence *inside*
a DETR — high-resolution query initialisation, deformable multi-scale sampling
tuned for small objects, feature-pyramid designs that carry P2, dense query
refinement, masked feature reconstruction as an auxiliary task? Prioritise
methods reporting gains on **small and low-contrast objects specifically**,
not overall mAP.

### Direction D — Post-hoc stratified score calibration

Note: this is already scheduled locally as I-17 (~20 minutes, no retraining).
Your contribution is valuable only if it points to **specific published methods**
rather than the general idea.

*Question:* what non-parametric or post-hoc calibration methods (per-class
isotonic regression on detection logits, stratified threshold mapping,
conformal / risk-controlling prediction for detection, AP-aware score
recalibration) recover AP ranking without retraining? Prioritise work that
calibrates **for AP** rather than for expected calibration error, since the two
objectives differ.

### Direction E — Exploiting the multi-view structure (least explored)

Each tree is photographed from 4–8 sides. 63,8 % of bunches appear in exactly 2
views. The published baseline handles cross-view duplication *statistically*
(divide by k ≈ 1,8905, or SVR). The dataset provides ground-truth cross-view
identity via a `_confirmedLinks` graph, and cross-side prediction inconsistency
is measured at **0,2329** (E-028).

*Question:* what literature turns multi-view redundancy into a **training signal**
rather than a post-hoc correction — multi-view consistency losses, set-level
prediction over a view group, cross-view feature aggregation without explicit 3D
reconstruction, re-identification-style association, or differentiable test-time
consensus? Note the geometric difficulty: adjacent views are ~90° apart (wide
baseline, low overlap), the object self-occludes behind fronds, and the canopy
may move between shots. Methods requiring narrow-baseline geometry should be
flagged as high-risk.

### Direction F — Camouflaged object detection (unsearched here)

B4 is literally green-on-green camouflage: measured background contrast ΔE 11,55,
*below* a random-box control of 12,92 (E-010). The local 182-entry corpus has
**no dedicated COD literature**.

*Question:* what does the COD / concealed-object-detection field (2022–2026) offer
that transfers to *detection with ordinal classification* rather than binary
segmentation? Assess boundary-aware and texture-aware modules, search-and-
identification two-branch designs, frequency-domain COD, and uncertainty-guided
refinement. Be explicit about the transfer gap — most COD work is binary
segmentation on curated benchmarks, not multi-class detection in a dense canopy.

### Direction G — Correct integration of sensor depth (objective O2, highest priority)

**This is the direction the project's hardware decision depends on, and it must
not be skipped.** Read §3.2 carefully before answering: what has been falsified
here is **input-channel concatenation** — a fourth channel stuffed into a
pretrained three-channel stem — measured three times (E-027 YOLO26n, E-029
RT-DETR-L, E-022 across three architectures). **The modality itself has never
been falsified.** E-022's own closing verdict is that "the failure is in *how*
depth is admitted, not in what depth contains", and E-032 leaves mid/late fusion
explicitly *untested at scale, not refuted*.

Three facts constrain any answer:

1. **E-030:** a fourth input channel containing *pure noise* significantly
   **harms** models above a turning point of 21,9–26,3 M parameters. Content does
   not rescue it. Whatever admits depth must therefore **not be the input
   channel** at the capacity that actually wins.
2. **RF-DETR-L's advantage is attributed to DINOv2 pretraining** (E-021).
   Modifying `PatchEmbeddings` destroys exactly the asset that produced 0,6038.
   The stem is off-limits — the same constraint as Direction B.
3. **Depth quality is not uniform.** Measured valid-pixel coverage is 0,71032
   dataset-wide, and coverage inside B4 boxes specifically is **unmeasured**.
   The local corpus records that bad depth actively degrades prediction (D3Net,
   entry 037) and that filter-before-fuse gating mitigates it (SA-Gate, entry
   055).

*Question:* what 2012–2026 literature establishes **where** and **through what
operator** a second modality should enter a pretrained single-stage detector?
Specifically:

- **Fusion-point evidence.** Beyond Ophoff et al.'s 28-point sweep and FuseNet's
  4-channel-vs-feature-fusion gap (31,95 vs 37,29 IoU), what systematic studies
  place the optimum, and does the optimum move with backbone capacity or with
  pretraining provenance?
- **Side/adapter admission.** Gated side encoders, zero-initialised residual
  gates (ControlNet-style), cross-attention from a frozen auxiliary encoder,
  modality adapters, prompt/token injection for a second modality into a ViT —
  which of these have been shown to add a modality to a **pretrained** backbone
  without degrading it, and with what measured cost?
- **Quality gating.** Confidence-weighted or entropy-gated fusion, learned depth
  reliability maps, dropout-on-modality training so the network degrades
  gracefully when depth is invalid. What is measured, not merely proposed?
- **Sparse / partially-invalid depth.** Roughly 29 % of pixels carry no valid
  depth. What handles structurally missing modality data — sparse convolutions,
  validity masks as explicit input, completion-before-fusion — and does
  completion help or inject its own errors?
- **Small-data regime.** SawitMVC-Depth is 352 trees / 2.299 boxes. What does the
  RGB-D literature say about fusion modules in low-data settings, where added
  parameters may simply overfit?
- **Negative results.** Where has RGB-D fusion been reported to *fail* on outdoor
  vegetation, active-IR sensors in daylight, or fine-grained classification? This
  is as valuable as a success.

*Deliverable specific to this direction:* an architecture that states its
insertion point against RF-DETR-L, its parameter cost, what happens to the
DINOv2 stem (which must be: nothing), how it behaves when depth is invalid, and
the control arms required to prove the gain came from **depth content** rather
than from added capacity.

*Note on measurability, state it in your answer:* on SawitMVC-Depth the RGB arm
alone swung **0,0759** mAP50 across three seeds on an identical configuration
(E-029). Any depth effect smaller than that is unmeasurable on this dataset. If
your proposal's expected effect is below that floor, say so and propose what
auxiliary measurement could detect it instead.

---

## 9. REQUIRED DELIVERABLE

1. **Executive summary** — the top 3 avenues, each in three sentences: what it
   changes, which mechanism (A or B) it targets, expected effect size with its
   uncertainty.
2. **Per-avenue breakdown**, each containing:
   - Mathematical formulation (loss equations, gradient behaviour, and the effect
     on score ranking under COCO AP).
   - Architectural insertion point against the RF-DETR-L graph, as pseudocode or
     a diagram.
   - Primary citations with arXiv ID or DOI, the originally reported gain, and
     the benchmark it was reported on.
   - **Predicted per-class effect** on B1/B2/B3/B4, stated separately.
   - **Falsification condition**, written before the protocol.
   - Estimated GPU-hours on one RTX A4500 for 3 seeds.
3. **A "what I could not find" section.** State which of Directions A–F returned
   nothing usable, and why. A short honest list here is worth more than a padded
   recommendation.
4. **Validation protocol** — 3-seed design, single-protocol `pycocotools`, frozen
   test split, paired bootstrap CI, and the auxiliary cross-side inconsistency
   probe.
5. **A ranked table** — avenue × expected gain × GPU cost × implementation risk ×
   confidence.

---

## 10. SELF-CHECK BEFORE YOU ANSWER

- [ ] **Have I answered Direction G at all?** → If not, the answer is incomplete.
      O2 is the open question; an RGB-only answer does not satisfy this brief.
- [ ] Have I treated depth as forbidden because E-027 appears in §3.2? → Re-read
      §5.5. What was falsified is the input-channel entry point, not the modality.
- [ ] Have I proposed anything from §5? → Remove it.
- [ ] Have I proposed anything from §6 without defeating the stated objection? →
      Remove it, or address the objection directly.
- [ ] Does every recommendation name mechanism (A) or (B), and predict per-class
      effects?
- [ ] Does every numeric claim carry a source?
- [ ] Have I stated an expected effect size, and is it above 0,05 mAP50?
- [ ] Have I confused val with test, or SawitMVC with SawitMVC-Depth anywhere?
- [ ] Would any of my recommendations be implementable by flipping a library
      flag? → It fails the novelty bar.
