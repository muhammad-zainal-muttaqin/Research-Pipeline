# English relabeling prompts for figures F01–F08

One complete, copy-paste prompt per figure. In Gemini, **attach the original
Indonesian figure** and paste the matching prompt below. Each prompt already
contains all the English text, so you don't need a separate label list. Save the
result under the **same filename** (e.g. `F03-silsilah-rgb-gpt-image-2.png`) so the
manuscript picks it up on recompile with no `.tex` change.

Terminology locked across all figures: tandan → **bunch** (FFB, not "cluster"),
kematangan → **ripeness**, sawit → **oil palm**, kebun → **plantation**,
fusi menengah → **middle fusion**, atensi lintas-modal → **cross-modal attention**.

## Note: the manuscript uses 10 figures — only these 8 need relabeling

The other two figures, `fig-corpus-year` and `fig-corpus-theme` (the year- and
theme-distribution bar charts), were generated directly from the 182-source matrix
with matplotlib and are **already in English** with accurate numbers ("Publication
year", "Verified sources", English theme names). They need no Gemini prompt. Only the
eight AI-generated conceptual figures F01–F08 below carry Indonesian labels.

---

## F01 — Taxonomy  (save as `F01-taksonomi-gpt-image-2.png`)

```
Recreate this taxonomy diagram exactly: keep the identical layout, tree/branch
structure, box shapes, colours, and positions. Do not add, remove, or rearrange any
node or edge. Only replace the text with the English below, keeping every number and
acronym unchanged and using a clean sans-serif font, same aspect ratio.

Root node: "RGB-D Object Detection for Oil Palm"
Four axis branches, each with its clusters (numbers unchanged; clusters are not additive):
- Axis 1 — YOLO Evolution: "YOLO Evolution (14)", "YOLO Surveys (9)"
- Axis 2 — RGB-based Object Detection: "RGB Foundations & Transformers (27)"
- Axis 3 — RGB+Depth Fusion: "Depth Estimation (20)", "RGB-D Salient Object Detection (23)",
  "RGB-D Semantic Segmentation (16)", "RGB+Depth Fusion for Detection (5)",
  "6D Pose & Robotic Grasping (19)", "3D LiDAR–Camera Detection (18)",
  "Multispectral RGB-T Pedestrian (7)", "Dynamic RGB-D SLAM (7)", "Datasets & Benchmarks (7)"
- Axis 4 — YOLO+RGB-D Integration: "YOLO+RGB-D (7)" (keep this cluster emphasized/highlighted),
  "Applications: agriculture / medical / industrial / remote sensing (22)"
```

---

## F02 — YOLO timeline  (save as `F02-timeline-yolo-gpt-image-2.png`)

```
Recreate this timeline diagram exactly: keep the identical horizontal timeline layout,
markers, colours, and positions. Do not add, remove, or rearrange any point. Only
replace the text with the English below; keep all version names and years unchanged;
clean sans-serif font, same aspect ratio.

Timeline points (year : version : marker):
- 2016 : YOLOv1 : single-stage grid regression
- 2017 : YOLOv2 / YOLO9000 : cluster-based anchors
- 2018 : YOLOv3 : multi-scale prediction, Darknet-53
- 2020 : YOLOv4 : consolidation of training tricks; PP-YOLO : tuning without architecture change
- 2021 : YOLOX : anchor-free, dynamic label assignment
- 2022 : YOLOv6 : hardware efficiency
- 2023 : YOLOv7 : guided layer aggregation
- 2024 : YOLOv9 (programmable gradient); YOLOv10 (NMS-free); YOLOv11 (modular framework);
  YOLO-World (text-prompted open-vocabulary)
- 2025 : YOLO26 : end-to-end real-time, NMS-free
Two transition markers: (a) 2021 "anchor-free begins"; (b) 2024 "NMS-free begins".
```

---

## F03 — RGB detector genealogy  (save as `F03-silsilah-rgb-gpt-image-2.png`)

```
Recreate this genealogy diagram exactly: keep the identical layout, the five coloured
horizontal rows, all boxes, arrows, colours, and positions. Do not add, remove, or
rearrange any box. Keep every box's text unchanged (they are already English acronyms:
R-CNN, Fast R-CNN, Faster R-CNN, Mask R-CNN, FPN, Sparse R-CNN, SSD, RetinaNet,
EfficientDet, FCOS, CenterNet, DETR, Deformable DETR, Conditional DETR, DN-DETR, DINO,
Co-DETR, RT-DETR, RF-DETR, Le-DETR, ResNet, ViT, Swin, Swin V2, PVT, ConvNeXt, CBAM).
ONLY translate the five coloured row labels on the left to English:
- "Dua-tahap" → "Two-stage"
- "Satu-tahap" → "One-stage"
- "Anchor-free" → "Anchor-free" (unchanged)
- "Transformer" → "Transformer" (unchanged)
- "Backbone" → "Backbone" (unchanged)
Clean sans-serif font, same aspect ratio.
```

---

## F04 — Three fusion strategies  (save as `F04-strategi-fusi-gpt-image-2.png`)

```
Recreate this three-panel diagram exactly: keep the identical three side-by-side panels,
block flow, arrows, colours, and positions. Do not add, remove, or rearrange any block.
Only replace the text with the English below; keep example method names unchanged; clean
sans-serif font, same aspect ratio.

Common flow in each panel: "RGB" and "Depth" → (encoder) → "fusion point" → (head) → "Prediction"
- Panel 1 — Early fusion: combine at input / shallow features (channel concatenation).
  Examples: FuseNet, Expandable YOLO. Note: simple, minimal parameters; vulnerable to noisy depth.
- Panel 2 — Middle fusion: combine multi-level features with cross-modal attention.
  Examples: SA-Gate, CMX, CIR-Net. Note: highest accuracy on crowded scenes; higher compute cost.
  (keep this panel emphasized/highlighted — relevant for oil palm)
- Panel 3 — Late fusion: combine outputs of two independent branches (average / select).
  Examples: JL-DCF, detect-then-project. Note: modular, robust to missing modality; ignores feature interaction.
```

---

## F05 — Two YOLO+RGB-D integration patterns  (save as `F05-pola-yolorgbd-gpt-image-2.png`)

```
Recreate this two-path diagram exactly: keep the identical two side-by-side flow paths,
boxes, arrows, colours, and positions. Do not add, remove, or rearrange any box. Only
replace the text with the English below; keep method names unchanged; clean sans-serif
font, same aspect ratio.

- Pattern 1 — Input-channel expansion (early fusion):
  "RGB (3 channels) + Depth (1 channel)" → "4-channel input" → "YOLO backbone" →
  "Detection head" → "Boxes + classes".
  Examples: Expandable YOLO; Ophoff et al. (finding: middle fusion > raw input).
  Note: cheap; sensitive to depth quality & alignment.
- Pattern 2 — Detect-then-project:
  "RGB" → "YOLO (2D detection)" → "2D boxes"; "Depth" → "3D projection / lift" →
  "3D location / range / point cloud".
  Examples: FusionVision, Xu et al. (onboard), YOLOv8-URE.
  Note: robust to noisy depth; does not strengthen hard-instance separation.
```

---

## F06 — Cross-modal attention  (save as `F06-atensi-lintasmodal-gpt-image-2.png`)

```
Recreate this block diagram exactly: keep the identical layout, blocks, bidirectional
arrows, colours, and positions. Do not add, remove, or rearrange any element. Only
replace the text with the English below; keep symbols and method names unchanged; clean
sans-serif font, same aspect ratio.

Two features enter: "F_rgb" and "F_depth" (each from its own encoder).
- "F_depth produces a weight map that reweights F_rgb" — and the reverse, bidirectional.
- Reweighted features combine → "F_fused" → passed to the next layer.
Mechanism note: "spatial/channel weights from the other modality".
Goal note: "suppress noisy depth contribution, strengthen reliable cues".
Adopters: "SA-Gate (alignment gate)", "CIR-Net (bidirectional interaction)",
"CMX (cross-modal feature rectification & exchange)".
```

---

## F07 — Funnel to the oil-palm gap  (save as `F07-funnel-sawit-gpt-image-2.png`)

```
Recreate this funnel diagram exactly: keep the identical funnel shape narrowing from
wide (top) to narrow (bottom), the same layers, colours, and positions. Do not add,
remove, or rearrange any layer. Only replace the text with the English below; keep
method names unchanged; clean sans-serif font, same aspect ratio.

Funnel layers, wide → narrow:
1. Mature RGB object detection (YOLO family, transformers)
2. Cheap depth from monocular foundation models (MiDaS, Depth Anything V2)
3. RGB-D fusion: middle fusion + cross-modal attention lead (SOD, segmentation)
4. YOLO+RGB-D integration proven on generic objects & some fruit
5. Oil-palm gap: (a) no annotated RGB-D oil-palm dataset; (b) fusion robust to depth
   degradation under sunlight not yet established; (c) counting stacked/occluded bunches
   needs depth-based instance separation
6. Research position: a YOLO RGB-D detector specialized for oil-palm bunch counting & ripeness classification
```

---

## F08 — Proposed oil-palm pipeline  (save as `F08-pipeline-sawit-gpt-image-2.png`)

```
Recreate this pipeline flow diagram exactly: keep the identical left-to-right flow, the
two parallel branches, all boxes, solid and dashed arrows, colours, and positions. Do
not add, remove, or rearrange any box. Only replace the text with the English below;
clean sans-serif font, same aspect ratio.

Boxes, left → right:
- "Plantation RGB image"
- Branch A: "RGB encoder"
- Branch B: "Monocular pseudo-depth estimation" → "Depth encoder"
- "Middle fusion + cross-modal attention + adaptive weighting"
- "YOLO detection head"
- "Bunch counting + ripeness classification"
- (dashed arrow) → "3D projection / robotic harvest localization"
Add a small caption note inside the figure: "Conceptual — not an experimental result."
```
