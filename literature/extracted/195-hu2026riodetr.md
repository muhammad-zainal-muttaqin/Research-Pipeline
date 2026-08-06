---
source_id: 195
bibtex_key: hu2026riodetr
title: RiO-DETR: DETR for Real-time Oriented Object Detection
year: 2026
domain_theme: Remote Sensing
verified_pdf: 195_RiO-DETR Deteksi Objek Berorientasi Real-Time.pdf
char_count: 109284
---

RiO-DETR: DETR for Real-time Oriented
                                                         Object Detection

                                         Zhangchi Hu1 , Yifan Zhao1 , Yansong Peng1 , Wenzhang Sun3 , Xiangchen
                                           Yin1 , Jie Chen1 , Peixi Wu1 , Hebei Li1 † , Xinghao Wang2 , Dongsheng
                                                               Jiang2 , and Xiaoyan Sun1,4
                                                           1
                                                              University of Science and Technology of China
arXiv:2603.09411v1 [cs.CV] 10 Mar 2026

                                                                     2
                                                                       Huawei Technologies Co., Ltd.
                                                                           3
                                                                              Tsinghua University
                                          4
                                            Institute of Artificial Intelligence, Hefei Comprehensive National Science Center
                                               {huzhangchi, lihebei}@mail.ustc.edu.cn, sunxiaoyan@ustc.edu.cn
                                                                           †
                                                                             Corresponding author

                                         Fig. 1: Comparisons with other detectors in terms of model size (left), latency (mid),
                                         and computational cost (right) on DOTA-1.0 under single-scale training and testing
                                         protocol. * denotes a community implemented version.

                                                Abstract. We present RiO-DETR: DETR for Real-time Oriented
                                                Object Detection, the first real-time oriented detection transformer to
                                                the best of our knowledge. Adapting DETR to oriented bounding boxes
                                                (OBBs) poses three challenges: semantics-dependent orientation, angle
                                                periodicity that breaks standard Euclidean refinement, and an enlarged
                                                search space that slows convergence. RiO-DETR resolves these issues
                                                with task-native designs while preserving real-time efficiency. First, we
                                                propose Content-Driven Angle Estimation by decoupling angle from po-
                                                sitional queries, together with Rotation-Rectified Orthogonal Attention
                                                to capture complementary cues for reliable orientation. Second, Decou-
                                                pled Periodic Refinement combines bounded coarse-to-fine updates with
                                                a Shortest-Path Periodic Loss for stable learning across angular seams.
                                                Third, Oriented Dense O2O injects angular diversity into dense super-
                                                vision to speed up angle convergence at no extra cost. Extensive ex-
                                                periments on DOTA-1.0, DIOR-R, and FAIR-1M-2.0 demonstrate RiO-
                                                DETR establishes a new speed–accuracy trade-off for real-time oriented
                                                detection. Code will be made publicly available.

                                                Keywords: Oriented Object Detection · Detection Transformer · Aerial
                                                Object Detection · Real-time Object Detection
2       Z. Hu et al.

1    Introduction

Oriented object detection extends horizontal bounding boxes (HBBs) to localize
objects with arbitrary rotations, which is crucial for aerial imagery, remote sens-
ing, and scene text understanding [6,9,12,34,35,39,40,42,46,55,56,65,67]. With
the rise of edge computing, the bottleneck has evolved from mere detection accu-
racy to the speed-accuracy trade-off. This raises a critical question: how can we
maintain high-quality oriented bounding boxes (OBBs) detection while meeting
rigorous real-time performance requirements?
     In the CNN paradigm, real-time oriented detectors have established robust
baselines, especially oriented variants of YOLO and RTMDet-style frameworks
[11,13,20,31,45,47,49]. Meanwhile, DETR-style detectors have recently achieved
real-time efficiency in horizontal detection by leveraging lightweight designs and
efficient training strategies [4, 16, 19, 28, 33, 36, 62]. However, real-time oriented
DETRs remain under-explored. Existing oriented DETR variants are often bur-
dened by heavy attention designs and complex sampling modules in pursuit of
peak accuracy [7, 17, 22, 59, 61, 63], which inherently limits their ability to match
the high throughput of CNN-based counterparts.
     This gap is not primarily due to insufficient model capacity; rather, it reflects
inherent architectural bottlenecks that emerge when adapting DETR from HBB
to OBB. We identify three key bottlenecks that systematically limit real-time ori-
ented DETRs: (1) Semantic–Geometric Coupling and Feature Collapse.
Unlike the standard (cx, cy, w, h) format, the orientation θ is strongly driven by
semantic appearance cues such as texture flow and dominant axes. Encoding
θ solely as a geometric prior in positional queries can introduce noise and mis-
guide the attention mechanism. Furthermore, naively aligning attention with the
major axis risks feature collapse, where lateral structures are insufficiently at-
tended. (2) Periodicity Mismatch in Angle Refinement. Standard DETR
decoders typically refine bounding boxes through Euclidean additive updates,
such as the inverse-sigmoid formulation. Applying such updates to the cyclic
angular domain introduces discontinuities at periodic boundaries, leading to un-
stable gradients and unreliable refinement [5,51–54]. (3) Slow Convergence in
the Expanded Search Space. OBBs introduce additional degrees of freedom,
which significantly expands the search space for bipartite matching and slows
convergence. While techniques like dense supervision or one-to-many training
are effective for HBB detection, they often lack sufficient angular diversity to
accelerate orientation learning in the OBB setting.
     These observations motivate a fundamental shift in design: achieving real-
time oriented detection requires moving beyond simply appending an angle
branch or increasing computational overhead. Instead, we focus on reformu-
lating core components to natively handle oriented geometry. To this end, we
present RiO-DETR, a Real-time Oriented detection transformer that effec-
tively bridges the gap between accuracy and latency. Built upon a delicately
implemented baseline, RiO-DETR introduces three task-specific designs to re-
solve the aforementioned bottlenecks:
                RiO-DETR: DETR for Real-time Oriented Object Detection            3

 – To decouple semantic and geometric cues, we introduce Content-Driven
   Angle Estimation. This approach employs a Geometry-Decoupled Query
   Encoding that facilitates angle prediction by leveraging semantic context
   rather than relying on rigid geometric priors. To address feature collapse
   with minimal overhead, we further propose Rotation-Rectified Orthog-
   onal Attention, which captures both axial and lateral cues to enhance
   orientation inference.
 – To address periodicity issues, we introduce Decoupled Periodic Refine-
   ment. Specifically, we replace standard Euclidean updates with a bounded
   coarse-to-fine periodic mechanism and a Shortest-path Periodic L1 Loss.
   This approach enables stable optimization across angular boundaries and re-
   solves refinement artifacts caused by periodic discontinuities.
 – To address slow convergence, we develop Oriented Dense O2O, a training
   strategy that injects angular diversity by applying independent random rota-
   tions to stitched image quadrants, significantly accelerating the convergence
   of angle predictions.

    RiO-DETR achieves a superior speed–accuracy balance for real-time
oriented detection (Fig. 1). On DOTA-1.0, RiO-DETR-n attains 78.4 AP50 with
only 2.7 ms end-to-end latency (TensorRT FP16 on NVIDIA T4). Meanwhile,
RiO-DETR-x reaches 81.8 AP50 at 29.9 ms. Both models outperform state-of-
the-art real-time detectors at similar speeds. Our approach also shows consistent
improvements on DIOR-R and FAIR-1M-2.0 across various scales. These results
demonstrate that end-to-end transformers can be highly efficient for oriented
object detection. We hope our design provides a robust framework and inspires
further exploration in this field.

2   Related Works

CNN-based Oriented Object Detection. Early oriented detectors mainly
extended horizontal CNN detectors with angle regression. Two-stage methods
[27,47,50] (e.g., RoI Transformer [8]) achieve high precision via rotation-invariant
RoI operations, while single-stage/anchor-free counterparts (e.g., S2ANet [58],
FCOS-O [42]) simplify the pipeline for higher efficiency. Recently, oriented YOLO
variants [11, 20, 21, 37, 38, 41, 49] and RTMDet-R [31] have advanced real-time
oriented detection. However, most still depend on dense prediction and heuris-
tic anchors, typically requiring NMS, which complicates deployment and adds
hyperparameter sensitivity. Moreover, lightweight designs for oriented detec-
tion [2, 25, 57] often introduce complex structures that raise compute/memory
access costs, leading to noticeable inference latency.

Real-time Object Detection. While the YOLO [20] ecosystem long domi-
nated real-time detection, the emergence of DETR [3] introduced a NMS-free,
end-to-end paradigm. Early DETR variants [23, 29, 32, 60, 66] struggled with
computational overhead, but recent models like RT-DETR [4, 62] have bridged
4      Z. Hu et al.

this gap using efficient hybrid encoders and uncertainty-minimal query selection.
Further advancements [16,26,30,36,44], such as D-FINE [33] and DEIM [18,19],
have enhanced precision and accelerated convergence through refined optimiza-
tion and dense supervision. These breakthroughs prove the feasibility of real-time
DETRs, yet their success remains largely confined to horizontal bounding boxes.

DETR-based Oriented Object Detection. Motivated by the success of
DETRs [3], several works have attempted to adapt the Transformer architec-
ture for oriented bounding boxes [61]. Methods like AO2-DETR [7] and EMO2-
DETR [17] introduce oriented proposal generation and rotation-aware attention
mechanisms to align features with arbitrary object orientations. Recent state-of-
the-art models, such as ARS-DETR [59], Oriented-DETR [63] and RHINO [22],
further address the matching and representation problem of OBBs. Despite their
strong performance, these methods predominantly build upon heavy architec-
tures and prioritize precision over inference speed, excluding them from real-time
applications. To the best of our knowledge, designing a DETR-based oriented
detector that maintains high accuracy while meeting strict real-time constraints
remains an unresolved challenge.

3     Methods

3.1   Best of Both Worlds: Building a Strong Real-time Baseline

While numerous studies have migrated oriented object detection to the DETR
family, most of them rely on DINO [60] or Deformable-DETR [66], which is
not fully optimized for inference efficiency. RT-DETRv2 is originally designed
for horizontal object detection and does not come with an oriented detection
(OBB) implementation. Therefore, we first develop an oriented RT-DETRv2
baseline by introducing an OBB regression head and adapting the angle repre-
sentation, losses, and denoising scheme following RHINO-DETR [22]. To make
the baseline strong and fair under real-time constraints, we further consolidate
two complementary training designs that have proven effective for DETR-style
detectors: the universal matching strategy from D-FINE and Dense O2O from
DEIM [19]. Additional implementation details are provided in Appendix A.
    Table 6 shows the comparison between our implemented baseline and previ-
ous works. Our implementation exhibits competitive performance, which forms
a solid foundation for our method. However, there remains a noticeable gap
compared with state-of-the-art counterparts (1.18 AP50 ), indicating that simply
porting existing DETR techniques is insufficient for closing the accuracy–efficiency
gap in oriented detection. It is our task-oriented improvements that solve the
rooted issues in DETR-based oriented object detection, and elevate RiO-DETR
to state-of-the-art accuracy–efficiency performance while keeping the parameter
count, FLOPs, and inference latency virtually unchanged.
                                          RiO-DETR: DETR for Real-time Oriented Object Detection                                                                                            5

        Pos. Encoding                     𝐐!$%&'(&'                                 𝐐!)%*         Multi-Head Deformable Attention (MHDA)                                        𝜃
                                                                                                                   %                    %
                                                               𝑥!       𝑦!   𝑤!      ℎ!              Heads 1 ~                  Heads       +1~𝐻
         Pos. Queries
                                                                                             𝜃!                    &                    &
                                                                                                  Scale           Final Sampling Points
                                                                                                  Factors 𝐬
    Activation Function
                                                  Decoupled Periodic                                ×      Scaled Sampling Points               ×
 × Multiply    + Add                                                                         +
                                                     Refinement                     ∆Q )%*                                              𝑹(𝜃 $ )
                                                                                                    Learned Offsets ∆𝐩'()
       𝐂 Concat
                                                Rotation-Rectified
                                                                                                         Angle                      Angle
                                               Orthogonal Attention                                                                       𝜋
    Feature Maps                                                                                        𝜃$ =𝜃                    𝜃 $ =𝜃+
                                                                              ref                                                         2
                                           V                        Q

                                                                                    no 𝜃                  𝑥 !"# 𝑦!"# 𝑤!"# ℎ!"#          𝜃!"#            Group 1     Group 2 Sampling Points
                        Decoder Layer 𝑖

                                                      Self-Attention                                             (B) Rotation-Rectified Orthogonal Attention
  Hybrid Encoder                           V            K           Q
                                                                                                                                                           !"#                         𝑥!
                                                                                                                                   𝑥 !"# 𝑦 !"# 𝑤 !"# ℎ!"# 𝐐)%* [: 4]
      Backbone                                                                      no 𝜃                                                                                               𝑦!
                                                                                                     ∆𝑥 ∆𝑦 ∆𝑤 ∆ℎ                                +        𝑥!   𝑦!    𝑤!    ℎ!
                                                                                                                                                                                      𝑤!
                                                                                                                                                                                𝐂
                                                                                                                            ×       +                   modulo to
                                                                                                     ∆𝜃                                        𝜃+,-                      𝜃&(-          ℎ!
                                                              𝑥 !"# 𝑦 !"# 𝑤 !"# ℎ!"# 𝜃 !"#                                                               [0, 𝜋)
                                                                                                                       𝛼!
                                                                                                                                            𝜃+(. (𝐐!"#                                 𝜃!
                                                𝐐!"#                          !"#
                                                                             𝐐)%*                                                  𝜃 !"#           )%* [5])
                                                 $%&'(&'
                                                                                                                                                                                     𝐐$!"#
              (A) Content-Driven Angle Estimation                                                                      (C) Decoupled Periodic Refinement

Fig. 2: The main architecture of our proposed RiO-DETR. The framework highlights
three key components: (A) Content-Driven Angle Estimation, (B) Rotation-Rectified
Orthogonal Attention, and (C) Decoupled Periodic Refinement.

3.2      Content-Driven Angle Estimation

Existing DETR-based oriented object detectors treat the orientation θ as a ge-
ometric component symmetric to box coordinates (cx , cy , w, h). Consequently,
these methods [7, 17, 22, 59, 61, 63] intuitively embed the full 5-dimensional tuple
(cx, cy, w, h, θ) into the query embeddings. This joint design implicitly assumes
that spatial localization and angular rotation can be optimized in a homoge-
neous Euclidean manner, letting the decoder refine the entire geometric state as
a unified representation.
    However, unlike (cx , cy ), the OBB orientation θ is not uniquely determined
by geometric correspondence. It is periodic and admits equivalent parameter-
izations; for instance, (w, h, θ) and (h, w, (θ + π/2) mod π) describe the same
physical rectangle. As a result, θ is effectively a canonical choice induced by an-
notation conventions (e.g., long-side direction or heading) rather than a purely
geometric quantity, and is often disambiguated only by appearance cues such
as dominant axes, part layouts, texture flows, and semantic definitions. Inject-
ing θ into positional embeddings therefore imposes a rigid geometric prior that
can be noisy during early training and potentially non-smooth around periodic
boundaries, which may misguide attention sampling and interfere with content-
driven refinement in the decoder. We provide a more formal discussion from the
viewpoint of quotient-consistency in Appendix B.
    Motivated by this asymmetry, we propose Content-Driven Angle Esti-
mation (illustrated in Fig. 2(A)(B)). Specifically, we decouple orientation from
the positional prior via Geometry-Decoupled Query Encoding, encourag-
ing the model to regress angles primarily from semantic context learned through
6       Z. Hu et al.

content queries. Then, we design Rotation-Rectified Orthogonal Attention
to extract rotation-aligned object features for more robust angle estimation.

Geometry-Decoupled Query Encoding We formulate the object query Q
as a composition of a content part Qcontent and a positional part Qpos . Unlike
previous works, we strictly limit the positional embedding to the 4-dimensional
spatial domain, explicitly excluding angular information.
    Let pref ∈ RN ×5 denote the reference points containing (cx, cy, w, h, θ),
where N is the number of object queries. The positional embedding is generated
via a coordinate encoder ϕ(·), which consists of a sinusoidal positional encoding
(PE) and a multi-layer perceptron (MLP):

                   Q_{pos} = \phi (\mathbf {p}_{ref}[..., :4]) = \text {MLP}(\text {PE}(\mathbf {p}_{ref}[..., :4]))                                                                        (1)
    where pref [..., : 4] represents only the spatial coordinates (cx, cy, w, h). By
masking the θ dimension during embedding generation, we ensure the positional
queries remain rotation-invariant.
    Simultaneously, the orientation information is latently modeled within the
learnable content embeddings Qcontent . This forces the decoder to extract rota-
tion cues from the image features such as texture direction and object heading.

Rotation-Rectified Orthogonal Attention While decoupling angle from po-
sitional embedding aids convergence, precise feature extraction requires sampling
locations that align with the object’s geometry. Previous oriented DETRs uni-
formly align all attention heads with the object’s major axis, which leads to
a feature collapse where the model disproportionately focuses on longitudinal
details while neglecting lateral structural information.
    To address this, we impose an orthogonal constraint on the multi-head at-
tention mechanism to ensure feature coverage along both the major and minor
axes of the oriented bounding box. For a query with predicted orientation θ,
we divide the total attention heads H (assuming H is an even integer) into
two distinct groups. The sampling rotation angle θ(h) for the h-th head, where
h ∈ {1, 2, . . . , H}, is defined as:

                                          \theta ^{(h)} = \begin {cases} \theta & \text {if } h \le \frac {H}{2} \\ \theta + \frac {\pi }{2} & \text {if } h > \frac {H}{2} \end {cases}    (2)

    This formulation forces the first half of the heads to sample features aligned
with the object’s predicted heading, while the second half samples orthogonally.
Notably, this design introduces merely no additional parameters or GFlops,
achieving performance gains without extra computational overhead.
    Let ∆pqk ∈ R2 be the learned offset for the k-th sampling point of the q-th
query, and sq ∈ R2 be its corresponding scale factor (width and height). The
spatial center of the query is denoted as pq = pref [q, : 2]. The final sampling
location S is rectified by the head-specific rotation matrix R(θ(h) ):
                         RiO-DETR: DETR for Real-time Oriented Object Detection                                                                                                                                                  7

                              ∆𝜃                       w/
                                                              0          𝜋/4           𝜋/2          3𝜋/4          𝜋          𝜋/4           𝜋/2          3𝜋/4           𝜋

                                                                                                  Gradient flows along the
                                                                                                  shortest path

                                                     w/o
                                                                        𝜋/4           𝜋/2          3𝜋/4            0         𝜋/4           𝜋/2         3𝜋/4            𝜋

                  Current Prediction
                                                                                                  Gradient is constrained by
       0   𝜋/4   𝜋/2   3𝜋/4    𝜋   𝜋/4       𝜋/2         3𝜋/4           𝜋                         the non-periodic range

                              (D) Decoupled Periodic Refinement                                                                                                                                        (E) Oriented Dense O2O

Fig. 3: An intuitive illustration of (D) Decoupled Periodic Refinement and (E) Oriented
Dense O2O.

                                     S(\mathbf {p}_q, \Delta \mathbf {p}_{qk}) = \mathbf {p}_{q} + \mathbf {R}(\theta ^{(h)}) (\Delta \mathbf {p}_{qk} \odot \mathbf {s}_q)                                                     (3)
  where ⊙ denotes the element-wise multiplication, and R(θ(h) ) is the rotation
matrix derived from the head-specific angle:

                                                 \mathbf {R}(\theta ^{(h)}) = \begin {bmatrix} \cos (\theta ^{(h)}) & -\sin (\theta ^{(h)}) \\ \sin (\theta ^{(h)}) & \cos (\theta ^{(h)}) \end {bmatrix}                       (4)

    This orthogonal splitting strategy allows the model to explicitly disentangle
features along the object’s length and width, improving robustness for aspect-
ratio and angle combined prediction.

3.3   Decoupled Periodic Refinement

Standard DETR-style decoders refine boxes by iteratively adding predicted off-
sets in the inverse-sigmoid space. This update rule implicitly assumes that each
regressed variable lies in a Euclidean and globally continuous domain, which
holds well for spatial coordinates (cx , cy , w, h). However, the orientation θ in
OBB resides on a periodic space. Treating θ as an unconstrained Euclidean
scalar, i.e., directly applying additive updates and standard L1 regression in-
duces a mismatched geometric assumption in decoder refinement: numerically
distant angles can be geometrically adjacent across the boundary (e.g., 0 ↔ π),
leading to discontinuous gradients and unstable refinement near periodic seams.
    To resolve this geometry mismatch, we introduce Decoupled Periodic Re-
finement, which jointly redesigns both the refinement update and the optimiza-
tion metric for θ. In other words, we make the decoder refinement consistent with
the periodic topology of orientation, rather than merely adding an auxiliary trick.
The overall workflow is illustrated in Fig. 2 (C) and 3 (D).
    For spatial dimensions, we retain the standard inverse-sigmoid update. Given
the predicted spatial offset ∆b and the reference box spatial parameters bref ,
the refined spatial coordinates are computed as σ(∆b + σ −1 (bref )), where σ(·)
denotes the sigmoid function. For orientation, we adopt a bounded coarse-to-fine
periodic update that explicitly respects the cyclic domain. Let ∆θi be the raw
8       Z. Hu et al.

angle offset predicted by the i-th decoder layer (i ∈ {1, . . . , L}) and θref be the
reference angle. We first bound the update magnitude with tanh(·) and scale it
using a layer-wise decaying factor αi :

                                                                                                         \alpha _i = \alpha _0^{-i},                                                              (5)

where α0 > 1 controls the decay rate. This design enforces a coarse-to-fine
refinement schedule: early layers perform larger corrective rotations, while later
layers are restricted to fine-grained tuning, improving stability under periodicity.
The bounded update is then applied as

                                                              \theta _{raw} = \theta _{ref} + \tanh (\Delta \theta _i)\cdot \alpha _i.                                                            (6)

Finally, we map the result back onto the canonical angular domain [0, π) via
periodic normalization:

                  \theta _{new} = \begin {cases} (\theta _{raw} \bmod \pi ) + \pi & \text {if } (\theta _{raw} \bmod \pi ) < 0 \\ (\theta _{raw} \bmod \pi ) & \text {otherwise.} \end {cases}    (7)

     Crucially, a periodic update alone is insufficient if the optimization objective
still measures distance in a Euclidean sense. A standard L1 loss over-penalizes
boundary-adjacent cases, producing gradients that point along the longer arc
and thus contradict the periodic refinement behavior. Therefore, we additionally
replace the angular regression metric with a Shortest-path Periodic L1 Loss:

                       \mathcal {L}_{angle} = \min \left (|\theta _{pred} - \theta _{tgt}|, \pi - |\theta _{pred} - \theta _{tgt}|\right ),                                                       (8)
which guarantees that gradients always follow the shortest angular displacement
on the circle. Appendix C provides further analysis and discussion on this point.
   By simultaneously adopting a periodic, bounded coarse-to-fine update and
a shortest-path periodic loss, our decoder refinement for θ becomes consistent
with the orientation setting. The overall box regression loss concatenates the
standard L1 loss for (cx , cy , w, h) with Langle for θ.

3.4   Oriented Dense O2O
We introduce Oriented Dense O2O to provide dense supervision while ex-
plicitly accelerating the convergence of angle predictions. As shown in Fig. 3
(E), building upon the Dense O2O [19] which combines four replicated images
into a single composite grid to increase GT counts, we apply an independent
random rotation θrot ∈ {0◦ , 90◦ , 180◦ , 270◦ } to each individual quadrant prior
to stitching them together. By artificially enriching the angular diversity within
a single training image, this computation-free mechanism forces the model to
simultaneously process semantic features at various orientations. Consequently,
Oriented Dense O2O seamlessly integrates rotational variance into the dense su-
pervision framework, accelerating the model’s convergence on angle predictions
and enhancing its robustness against rotated objects.
                RiO-DETR: DETR for Real-time Oriented Object Detection            9

4     Experiments
4.1   Evaluation Datasets
DOTA-1.0. DOTA-1.0 [46] is a large-scale oriented object detection dataset
containing 2,806 images and 188,282 instances across 15 categories, with signif-
icant variations in orientation, shape, and scale. Two evaluation protocols are
provided: (A) single-scale and (B) multi-scale training and testing. In single-scale
settings, images are cropped into 1024 × 1024 patches with a stride of 824. In
multi-scale settings, images are resized to 0.5, 1.0, and 1.5 scales before being
cropped into 1024 × 1024 patches with a stride of 524.

DIOR-R. DIOR-R [6] is constructed from DIOR by adding annotations for
rotated bounding boxes. It comprises 23,463 images of size 800 × 800, totaling
190,288 oriented instances across 20 categories. The dataset is split into training,
validation, and testing sets with a ratio of 1:1:2.

FAIR-1M-2.0. FAIR-1M-2.0 [1] is a recently published remote sensing dataset
that consists of 15,266 high-resolution images and more than 1 million instances.
It contains 5 categories and 37 subcategories. For multi-scale training and test-
ing, images are processed in the same way as in DOTA.

4.2   Implementation Details
For DOTA-1.0 and DIOR-R, models are trained on the combined train and val
sets and evaluated on the test set. For FAIR-1M-2.0, models are trained on the
train set and evaluated on the val set. The results on DOTA are reported using
the official evaluation server. The training schedules for different RiO-DETR
variants and the corresponding hyperparameter configurations are detailed in
Appendix A. All models are trained on a single NVIDIA A800 or H200 GPU.
All latencies are measured equally on a single NVIDIA T4 GPU using TensorRT
10 with FP16. For end-to-end models, the latency excludes pre-processing and
post-processing time, while for others the BatchedNMSPlugin is employed to
get the actual latency under production scenes. Unless otherwise specified, all
ablation studies are conducted on the DIOR-R dataset with RiO-DETR-m.

4.3   Comparison with State-of-the-Art Methods
Results on DOTA-1.0. Under single-scale training and testing protocol (Ta-
ble 1), RiO-DETR performs strongly across all scales. RiO-DETR-n achieves
78.4% AP50 with 2.7 ms latency and 4.0M parameters, surpassing YOLO26n-
obb. At the high end, RiO-DETR-x reaches 81.8% AP50 at 29.9 ms, outperform-
ing YOLO26x-obb (80.4%, 30.5 ms) and heavy DETR variants such as RHINO-
DETR (79.4%, 242.6 ms). Under multi-scale evaluation (Table 2), RiO-DETR-x
attains 81.76% AP50 with the lowest latency among high-precision models. Per-
class AP50 under multi-scale protocol, results under high precision metrics and
results on different backbones are provided in Appendix D.
10     Z. Hu et al.

Results on DIOR-R. RiO-DETR maintains a clear speed–accuracy advantage
on DIOR-R (Table 3). RiO-DETR-s achieves 74.44% AP50 at 3.01 ms, while RiO-
DETR-x reaches 77.43% at 17.31 ms, exceeding YOLO26x-obb (76.48%) under
similar latency and outperforming prior state-of-the-art models.

Results on FAIR-1M-2.0. On FAIR-1M-2.0 (Table 4), RiO-DETR-x achieves
a new state of the art with 47.4 AP50 under multi-scale training and testing, sur-
passing YOLO26x-obb (46.7%), LSKNet-S (46.3%), and ReDet (43.2%), demon-
strating strong scalability to large-scale remote sensing benchmarks. Per-class
AP50 are provided in Appendix D.

4.4   Efficiency Analysis of RiO-DETR
Our RiO-DETR series operates at the same latency level as the YOLO26 fam-
ily across all model scales (n–x). Specifically, RiO-DETR-n/s/m/l/x achieve
2.7/5.2/8.8/13.4/29.9 ms, closely matching the corresponding YOLO26 variants
(2.8/4.9/10.2/13.0/30.5 ms), demonstrating that RiO-DETR maintains a fully
real-time regime comparable to state-of-the-art CNN-based real-time detectors.
    Several CNN-based counterparts [2, 25, 57] that claim efficiency exhibit sub-
stantially higher latency (200–360 ms). This gap stems largely from computa-
tionally expensive components such as large-kernel convolutions. By explicitly
avoiding such high-latency operators, RiO-DETR achieves a clear advantage over
these methods. Notably, RiO-DETR is the first oriented DETR to achieve end-
to-end real-time inference for a single image, closing the long-standing efficiency
gap between transformer-based and CNN-based oriented detectors.

4.5   Ablation Studies
The Roadmap to RiO-DETR. Table 5 showcases the stepwise progression
from the baseline model to our proposed RiO-DETR framework. Starting from
RT-DETRv2 adding a simple OBB head, we first introduce a stronger bipartite
matching and optimization objective, which yields a notable improvement in
AP50 . Specifically, we formulate the matching cost Cmatch as a combination of
focal loss, KLD loss, and Hausdorff distance:
             Cmatch = λcls Cf ocal + λkld Ckld + λhausdorf f Chausdorf f
Correspondingly, the overall training loss L is optimized using a shortest-path
periodic L1 loss (Langle ) alongside the focal and KLD losses:
                      L = λcls Lf ocal + λkld Lkld + λangle Langle
By integrating the matching strategy from D-FINE and the training scheme from
DEIM, the baseline increases to 73.47 AP50 . On this basis, Content-Driven An-
gle Estimation yields steady gains: Geometry-Decoupled Query Encoding raises
AP50 to 74.18 with negligible cost, and Rotation-Rectified Orthogonal Attention
further improves it to 74.74 with slight latency overhead. Finally, Decoupled Pe-
riodic Refinement and Oriented Dense O2O push performance to 75.73 AP50
while keeping parameters, FLOPs, and latency nearly unchanged.
                           RiO-DETR: DETR for Real-time Oriented Object Detection                                                                11

Table 1: Comparison with state-of-the-art oriented object detectors on DOTA-1.0
under single-scale training and testing protocol.

Methods              Backbone      #P      Flops Lat. AP50 PL         BD BR GTF SV            LV   SH   TC   BC   ST SBF RA HA             SP   HC
                                          CNN-based Non-Real-time Oriented Object Detectors
LSKNet-S [25]        LSKNet-S      31.0M   161G 203.5     77.5   89.7 85.5 57.7   75.7   75.0 78.7 88.2 90.9 90.9 86.4   66.9    63.8 77.8 74.5 64.8
PKINet-S [2]         PKINet-S      30.8M   190G 359.7     78.4   89.7 84.2 55.8   77.6   80.2 84.5 88.1 90.9 87.6 86.1   66.9    70.2 77.5 73.6 62.9
PSD-SQ [10]          R-50             -      -    -       78.5   89.7 85.4 57.3   75.2   80.0 81.2 88.3 89.9 88.0 86.3   69.6    68.5 75.3 69.5 72.7
RVSA [43]            ViTAE-B      114.4M   414G   -       79.0   89.4 84.3 59.4   73.2   80.0 85.4 88.1 90.9 88.5 86.5   58.9    72.2 77.3 79.6 71.2
Strip R-CNN-S [57]   StripNet-S    30.5M   159G 241.9     80.1   88.9 86.4 57.4   76.4   79.7 84.4 88.2 90.9 86.7 87.5   69.9    66.8 79.2 82.9 75.6
                                        DETR-based Non-Real-time Oriented Object Detectors
R. D-DETR [59]     R-50           41.1M    409G   216.9   69.5   84.8 70.7 46.0   61.9   73.9 78.8 87.7 90.0 77.9 78.4   47.0    54.4 66.8 67.6 55.6
R. D-DETR [59]     R-50 w/ CSL    41.4M    411G   221.7   72.2   86.2 76.6 46.6   65.2   76.8 76.3 87.7 90.7 79.3 82.3   54.0    61.7 66.0 70.4 61.9
EMO2-DETR [17]     Swin-T            -       -      -     72.3   89.0 79.6 48.7   60.2   77.3 76.4 84.5 90.8 84.8 85.7   48.9    67.6 66.3 71.5 53.5
ARS-DETR [59]      R-50           41.4M    411G   221.7   74.2   86.9 75.5 48.3   69.2   77.9 77.9 87.6 90.5 77.3 82.8   60.2    64.5 74.8 71.7 66.6
ARS-DETR [59]      Swin-T         41.9M    431G   303.6   75.5   87.7 76.5 50.6   69.9   79.8 83.9 87.9 90.3 86.2 85.1   54.6    67.0 75.6 73.7 63.4
AO2-DETR [7]       R-50           74.3M    304G     -     77.7   89.3 85.0 56.7   74.9   78.9 82.7 87.3 90.5 84.7 85.4   62.0    70.0 74.7 72.4 71.6
RHINO-DETR [22] R-50              47.6M    566G   187.9   78.7   88.2 85.1 55.8   72.7   80.2 83.1 89.0 90.8 87.1 86.8   65.3    71.6 77.7 81.2 64.7
RHINO-DETR [22] Swin-T            50.8M    609G   242.6   79.4   88.2 84.8 58.5   77.7   81.1 85.6 89.2 90.9 87.0 86.4   65.5    71.3 78.2 82.8 64.3
Oriented-DETR [63] R-50           57.2M    302G   217.3   79.1   89.2 86.4 57.7   75.3   81.1 84.7 89.1 90.9 86.1 87.0   59.5    70.3 79.3 81.5 68.8
Oriented-DETR [63] Swin-T         57.7M    309G   235.5   79.8   89.4 85.1 57.8   75.0   81.2 86.1 89.1 90.9 88.7 87.0   62.9    69.1 80.7 82.8 71.0
                                                  Real-time Oriented Object Detectors
PPYOLOE-R-l [49]     CRN-l        52.2M    141G   33.3    78.1   89.2 81.0 54.0   70.2   81.8 85.2 88.8 90.8 87.0 88.0   62.9    67.9 76.6 79.1 69.7
PPYOLOE-R-x [49]     CRN-x        98.4M    264G   51.0    78.3   89.5 79.7 55.0   75.6   82.4 85.2 88.3 90.8 85.7 87.7   63.2    69.5 77.1 75.1 69.4
RTMDet-R-m [31]      CSPNext-m    24.7M    100G   22.4    78.2   89.2 84.7 53.9   74.7   81.5 84.0 88.7 90.8 87.4 87.2   59.4    66.7 77.7 82.4 65.3
RTMDet-R-l [31]      CSPNext-l    52.3M    205G   30.2    78.8   89.4 84.2 55.2   75.1   80.8 84.5 89.0 90.9 87.4 87.2   63.1    67.9 78.1 80.8 69.1
YOLO26n-obb [37]     YOLO26n       2.5M     14G    2.8    77.7   89.7 84.7 52.1   71.1   83.1 78.9 88.7 91.1 87.3 86.9   58.5    69.1 76.6 82.8 65.1
YOLO26s-obb [37]     YOLO26s       9.8M     55G    4.9    79.7   89.7 86.3 55.5   71.8   82.5 81.9 88.9 91.1 88.2 88.1   62.9    72.5 78.0 83.9 74.5
YOLO26m-obb [37]     YOLO26m      21.2M    183G   10.2    80.0   89.2 86.8 56.4   73.0   82.6 78.3 89.1 91.2 88.3 87.9   64.5    78.0 78.3 83.1 79.7
YOLO26l-obb [37]     YOLO26l      25.6M    230G   13.0    80.2   89.5 86.3 56.2   74.2   82.8 78.8 89.3 91.1 88.6 88.1   67.8    72.2 78.2 83.5 76.5
YOLO26x-obb [37]     YOLO26x      57.6M    517G   30.5    80.4   89.7 86.6 57.3   73.8   82.8 79.2 89.2 91.1 89.1 88.1   66.7    70.6 77.9 83.3 80.7
RiO-DETR-n           HGNet-B0      4.0M     17G    2.7    78.4   87.3 86.1 54.9   73.6   80.5 85.1 88.0 90.8 87.4 86.9   60.9    72.0 76.8 73.4 71.8
RiO-DETR-s           HGNet-B2      8.2M     53G    5.2    80.3   85.6 84.8 57.5   75.5   80.7 86.2 89.0 90.8 88.4 88.2   65.2    74.2 78.3 80.1 79.6
RiO-DETR-m           HGNet-B2     18.6M    158G    8.8    80.9   85.9 86.4 61.7   78.1   82.0 86.8 89.2 90.8 88.9 87.7   67.4    73.3 78.8 77.4 78.8
RiO-DETR-l           HGNet-B4     27.5M    230G   13.4    81.7   86.7 86.8 60.8   79.4   82.0 86.4 89.0 90.8 88.7 88.5   70.0    76.0 79.2 83.4 76.9
RiO-DETR-x           HGNet-B5     62.5M    527G   29.9    81.8   88.3 87.5 61.9   79.2   83.2 86.5 89.2 90.8 88.4 87.8   71.2    75.1 78.5 82.2 77.1

Table 2: Comparison with state-of-the-art oriented object detectors on DOTA-1.0
under multi-scale training and testing protocol.

           PKINet-S LSKNet-S Strip R-CNN-S PPYOLOE-R-x RTMDet-R-l YOLO26m-obb        YOLO26x-obb
 Model                                                                        Ours-m             Ours-x
             [2]      [25]         [57]        [49]       [31]        [37]              [37]
 Latency     359.7        203.5           241.9             51.0              30.2               10.2         8.8                30.5        29.9
 AP50        81.06        81.64           82.28             80.73            81.33              81.00        81.49              81.70       81.76

Ablation on Geometry-Decoupled Query Encoding. Table 9 analyzes
different geometry components used in query encoding. Encoding the center
coordinates alone achieves limited performance (72.56 AP50 ), and additionally
encoding the angle further degrades accuracy (72.34), suggesting that directly
injecting θ into the query can introduce optimization ambiguity. Incorporating
size information provides a clear gain (73.57), and the best result is obtained
by encoding center and size while leaving the angle to be inferred from content
features, reaching 73.81 AP50 . These results validate our design choice of geom-
etry decoupling: use (cx, cy, w, h) to guide localization while predicting θ in a
content-driven manner.

Ablation on Decoupled Periodic Refinement Components. Table 8 an-
alyzes the contribution of each component in Decoupled Periodic Refinement.
Using SP-L1 alone slightly improves AP50 from 74.18 to 74.32. The periodic
update mechanism alone leads to a small drop in AP50 (74.18 → 74.05), sug-
12         Z. Hu et al.

Table 3: Performance comparison with                             Table 4: Performance comparison with
state-of-the-art oriented object detectors                       SoTA methods on FAIR-1M-2.0 under
on DIOR-R.                                                       multi-scale training and testing protocol.

Methods            Backbone     #P      Flops   Lat.     AP50    Methods             Backbone   #P   Flops Lat. AP50
      Non-Real-time Oriented Object Detectors                    SASM RepPoints [15]   R-101    55.8M 542G   144.5   30.9
                                                                 R-FCOS [42]           R-101    50.9M 284G   156.9   36.1
LSKNet-S [25]      LSKNet-S     31.0M   111G    138.75   65.90
                                                                 S2A-Net [58]           R-50    31.6M 588G     -     37.4
PKINet-S [2]       PKINet-S     30.8M   118G    217.33   67.03
                                                                 R-Faster RCNN [50]    R-101    60.1M 289G   163.4   37.5
Strip R-CNN-S [57] StripNet-S   30.5M   157G    236.98   68.70
                                                                 O-RepPoints [24]     Swin-T    37.3M 200G     -     38.9
RHINO-DETR [22] Swin-T          50.8M   383G    164.51   72.67
                                                                 O-RCNN [47]           R-101    60.3M 289G   160.8   40.4
         Real-time Oriented Object Detectors                     RoI Trans. [8]        R-101    67.8M 607G     -     40.2
                                                                 LOOD (RT) [64]         R-50       -    -      -     42.6
YOLO26n-obb [37] YOLO26n 2.5M 10G               2.23     71.88
                                                                 ReDet [14]           ReR-50    31.8M 225G   448.2   43.2
YOLO26s-obb [37] YOLO26s 9.8M 39G               2.84     74.07
                                                                 PKINet-S [2]        PKINet-S 30.8M 190G     359.7   44.5
YOLO26m-obb [37] YOLO26m 21.2M 129G              5.91    74.65
                                                                 LOOD (RD) [64]        R-101       -    -      -     44.9
YOLO26l-obb [37] YOLO26l 25.6M 158G             7.53     75.31
                                                                 LSKNet-S [25]       LSKNet-S 31.0M 161G     203.5   46.3
YOLO26x-obb [37] YOLO26x 57.6M 353G             17.66    76.48
                                                                 Strip-RCNN-S [57]   StripNet-S 30.5M 159G   241.9   46.8
RiO-DETR-n         HGNet-B0 4.0M 11G   2.20              71.92
                                                                 YOLO26m-obb [37]    YOLO26m 21.2M 183G      10.2    42.5
RiO-DETR-s         HGNet-B2 8.2M 16G    3.01             74.44
                                                                 YOLO26x-obb [37]    YOLO26x 57.6M 517G      30.5    46.7
RiO-DETR-m         HGNet-B2 18.6M 97G  5.10              75.73
RiO-DETR-l         HGNet-B4 27.5M 141G 7.76              76.11   RiO-DETR-m          HGNet-B2 18.6M 158G      8.8    43.6
RiO-DETR-x         HGNet-B5 62.7M 324G 17.31             77.43   RiO-DETR-x          HGNet-B5 62.5M 527G     29.9    47.4

Table 5: Step-by-step modifications from baseline model to RiO-DETR-m on DIOR-
R. Each step shows changes in AP50 , the number of parameters, latency, and Flops.

Methods                                                                              #P    Flops Latency AP50
Oriented RT-DETRv2 (Ours Scratch Implementation)          18.61M 97.06G                               5.04       70.35
+ Hausdorff Matching from RHINO-DETR [22] & KLD Loss [53]                                                        72.86
+ Universal Matching Strategy from D-FINE [33]                                                                   73.33
+ Dense O2O from DEIM [19] (Our Implemented Baseline) 18.61M 97.06G                                   5.04       73.47
+ Content-Driven Angle Estimation
  Geometry-Decoupled Query Encoding                                                 18.59M 97.01G     5.04       74.18
  Rotation-Rectified Orthogonal Attention                                           18.67M 97.18G     5.10       74.74
+ Decoupled Periodic Refinement                                                                                  75.46
+ Oriented Dense O2O (Our RiO-DETR-m)                                               18.67M 97.18G     5.10       75.73

gesting that constraining angles within [0, π) without a consistent periodic loss
is insufficient and may introduce instability. Combining both components yields
the largest gain, reaching 74.74 AP50 , demonstrating that consistent periodic
modeling in both the loss and update steps is crucial for stable OBB refinement.

Ablation on Oriented Dense O2O. Compared to Regular Augmentation
(73.33 AP50 at 86 epochs), Dense O2O achieves 73.47 AP50 in 68 epochs, proving
that denser supervision mitigates sparse matching. Oriented Dense O2O reaches
the highest AP50 (73.88) with the fastest convergence, demonstrating the value
of rotation diversity. While random rotation yields a smaller gain (73.66), we
attribute this to noisy angle supervision from orientation ambiguity in near-
square objects. In contrast, the discrete rotations in Oriented Dense O2O enrich
patterns while reducing ambiguity, resulting in more stable training and superior
performance. Oriented Dense O2O is essentially equivalent to performing angle-
stratified dense supervision within a single composite image, which improves
the angular separability of targets in each Hungarian matching step. Moreover,
                   RiO-DETR: DETR for Real-time Oriented Object Detection                                13

Table 6: Comparison of our implemented                   Table 7: Ablation on Oriented Dense
baseline with SoTA methods on DIOR-R.                    O2O. Epoch notes the one with highest
                                                         AP50 on Stage 1.
Methods                 #P      Flops Latency AP50

RoI Trans. [8]         68.1M    373G      -     63.87    Methods                        Epoch    AP50
RVSA-ViTAE-B [43]      114.4M     -       -     71.05
DCFL-ReR-101 [48]          -      -       -     71.03    No Augmentation                    94    72.18
LSKNet-S [25]            31M    111G   138.75   65.90
                                                         Regular Augmentation               86    73.33
PKINet-S [2]           30.8M    118G   217.33   67.03
                                                         Dense O2O [19]                     68    73.47
Strip R-CNN-S [57]      30.5M   157G   236.98   68.70
RHINO-DETR-Swin-T [22] 50.8M    383G   164.51   72.67    Oriented Dense O2O (Ours)          60    73.88
YOLO26m-obb [37]       21.2M    129G    5.91    74.65    Dense O2O w/ random rotation       62    73.66
                                                         Pure Angle Augmentation            84    73.53
Baseline               18.61M   97G    5.04      73.47

Table 8: Ablation study on the compo-                    Table 9: Ablation study on Geometry-
nents of Decoupled Periodic Refinement.                  Decoupled Query Encoding.

      SP-L1         Periodic             AP50              Center        Size       Angle        AP50
                                                           (cx, cy)     (w, h)       (θ)
                                         74.18
       ✓                                 74.32                ✓                                  72.56
                       ✓                 74.05                ✓                         ✓        72.34
       ✓               ✓                 74.74                ✓           ✓             ✓        73.57
                                                              ✓           ✓                      73.81

using discrete rotations maximizes angular coverage while minimizing equivalent-
parameterization noise of near-square objects; as a result, the angle branch enters
a stable refinement regime earlier, with lower gradient variance and reduced jitter
near periodic boundaries. Further analysis is provided in Appendix E.

4.6     Visualization Analysis
Visualization Analysis of Sampling Patterns. To intuitively understand
how Rotation-Rectified Orthogonal Attention improves feature extraction, we
visualize the deformable attention sampling points in Fig. 4. Our proposed
Rotation-Rectified Orthogonal Attention enforces an orthogonal sampling pat-
tern, effectively capturing both longitudinal and lateral structural features of the
oriented objects.

Visualization Analysis of Angular Prediction. Figure 5 illustrates this
refinement on a challenging instance. Starting from a coarse estimate, the pre-
dicted OBB progressively aligns with object boundaries: Layer 1 corrects the
global heading, while Layers 2–4 remove minor angular deviations without over-
shooting, further validating the stability and precision of the proposed strategy.
More cases are provided in Appendix E.

Visualizing Angular Feature Distribution. To further validate the effec-
tiveness of Geometry-Decoupled Query Encoding, we employ t-SNE to visualize
the query angular features on FAIR-1M-2.0 in Fig. 6. Our decoupled formulation
yields content-query embeddings that organize into clear and separated clus-
ters across orientation intervals, indicating that the model encodes orientation-
sensitive semantic evidence in the content space rather than relying on a rigid
14      Z. Hu et al.

      Fig. 4: Visualization of deformable attention sampling points on DOTA.

                                                                                                        𝜋
                   Decoder Layer 1 Output

                                            Decoder Layer 2 Output
                                                                                                        3
                                                                                                          𝜋
                                                                                                        4

                                                                                                        1
                                                                                                          𝜋
                   Decoder Layer 3 Output

                                            Decoder Layer 4 Output

                                                                                                        4

                                                                                                        0

                                                                     Fig. 6: t-SNE visualization of angu-
Fig. 5: Visual illustration of layer-wise                            lar features, demonstrating Geometry-
angular refinement for a specific instance.                          Decoupled Query Encoding’s clustering.

geometric prior, which is consistent with our design choice to avoid injecting θ
as positional geometry. Further t-SNE analyses are provided in Appendix E.

5    Conclusion
In this paper, we present RiO-DETR, the first real-time oriented detection
transformer that offers a meaningful step forward in oriented object detection.
Content-Driven Angle Estimation, Decoupled Periodic Refinement, and Oriented
Dense O2O jointly address angle-content entanglement, periodicity-induced op-
timization instability, and slow convergence of existing methods. Extensive ex-
periments on DOTA-1.0, DIOR-R, and FAIR-1M-2.0 demonstrate a new accu-
racy–latency frontier compared to all state-of-the-art CNN and DETR counter-
parts. Limitation and Future Work: While RiO-DETR significantly opti-
mizes the detection pipeline, designing a real-time yet high-performance back-
bone specifically tailored for the complexities of oriented/remote sensing object
detection remains an open challenge. Future work may focus on specialized fea-
ture extraction to further enhance the real-time trade-off. We hope RiO-DETR
serves as a strong, practical baseline for the community and inspires further
exploration into real-time end-to-end perception for oriented objects.
                 RiO-DETR: DETR for Real-time Oriented Object Detection                  15

References
 1. Fair1m: A benchmark dataset for fine-grained object recognition in high-resolution
    remote sensing imagery. ISPRS Journal of Photogrammetry and Remote Sens-
    ing 184, 116–130 (2022). https://doi.org/https://doi.org/10.1016/j.
    isprsjprs.2021.12.004
 2. Cai, X., Lai, Q., Wang, Y., Wang, W., Sun, Z., Yao, Y.: Poly kernel inception
    network for remote sensing detection. In: Proceedings of the IEEE/CVF conference
    on computer vision and pattern recognition. pp. 27706–27716 (2024)
 3. Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., Zagoruyko, S.: End-
    to-end object detection with transformers. In: European conference on computer
    vision. pp. 213–229. Springer (2020)
 4. Chen, Q., Su, X., Zhang, X., Wang, J., Chen, J., Shen, Y., Han, C., Chen, Z.,
    Xu, W., Li, F., et al.: Lw-detr: A transformer replacement to yolo for real-time
    detection. arXiv preprint arXiv:2406.03459 (2024)
 5. Chen, Z., Chen, K., Lin, W., See, J., Yu, H., Ke, Y., Yang, C.: Piou loss: To-
    wards accurate oriented object detection in complex environments. In: European
    conference on computer vision. pp. 195–211. Springer (2020)
 6. Cheng, G., Wang, J., Li, K., Xie, X., Lang, C., Yao, Y., Han, J.: Anchor-free
    oriented proposal generator for object detection. IEEE Transactions on Geoscience
    and Remote Sensing 60, 1–11 (2022)
 7. Dai, L., Liu, H., Tang, H., Wu, Z., Song, P.: Ao2-detr: Arbitrary-oriented object
    detection transformer. IEEE transactions on circuits and systems for video tech-
    nology 33(5), 2342–2356 (2022)
 8. Ding, J., Xue, N., Long, Y., Xia, G.S., Lu, Q.: Learning roi transformer for oriented
    object detection in aerial images. In: Proceedings of the IEEE/CVF conference on
    computer vision and pattern recognition. pp. 2849–2858 (2019)
 9. Ding, J., Xue, N., Xia, G.S., Bai, X., Yang, W., Yang, M.Y., Belongie, S., Luo,
    J., Datcu, M., Pelillo, M., et al.: Object detection in aerial images: A large-scale
    benchmark and challenges. IEEE transactions on pattern analysis and machine
    intelligence 44(11), 7778–7796 (2021)
10. Feng, S., Wang, B.: Psd-sq: Point set decoding based on semantic query for object
    detection in remote sensing images. IEEE Transactions on Geoscience and Remote
    Sensing 62, 1–12 (2024)
11. Ge, Z., Liu, S., Wang, F., Li, Z., Sun, J.: Yolox: Exceeding yolo series in 2021.
    arXiv preprint arXiv:2107.08430 (2021)
12. Girshick, R.: Fast r-cnn. In: Proceedings of the IEEE international conference on
    computer vision. pp. 1440–1448 (2015)
13. Han, J., Ding, J., Li, J., Xia, G.S.: Align deep features for oriented object detection.
    IEEE transactions on geoscience and remote sensing 60, 1–11 (2021)
14. Han, J., Ding, J., Xue, N., Xia, G.S.: Redet: A rotation-equivariant detector for
    aerial object detection. In: Proceedings of the IEEE/CVF conference on computer
    vision and pattern recognition. pp. 2786–2795 (2021)
15. Hou, L., Lu, K., Xue, J., Li, Y.: Shape-adaptive selection and measurement for
    oriented object detection. In: Proceedings of the AAAI conference on artificial
    intelligence. vol. 36, pp. 923–932 (2022)
16. Hu, Z., Wu, P., Chen, J., Zhu, H., Wang, Y., Peng, Y., Li, H., Sun, X.: Dome-detr:
    Detr with density-oriented feature-query manipulation for efficient tiny object de-
    tection. In: Proceedings of the 33rd ACM International Conference on Multimedia.
    pp. 101–110 (2025)
16      Z. Hu et al.

17. Hu, Z., Gao, K., Zhang, X., Wang, J., Wang, H., Yang, Z., Li, C., Li, W.: Emo2-
    detr: Efficient-matching oriented object detection with transformers. IEEE trans-
    actions on geoscience and remote sensing 61, 1–14 (2023)
18. Huang, S., Hou, Y., Liu, L., Yu, X., Shen, X.: Real-time object detection meets
    dinov3. arXiv preprint arXiv:2509.20787 (2025)
19. Huang, S., Lu, Z., Cun, X., Yu, Y., Zhou, X., Shen, X.: Deim: Detr with improved
    matching for fast convergence. In: Proceedings of the computer vision and pattern
    recognition conference. pp. 15162–15171 (2025)
20. Jocher, G., Chaurasia, A., Stoken, A., Borovec, J., Kwon, Y., Michael, K., Fang, J.,
    Wong, C., Yifu, Z., Montes, D., et al.: ultralytics/yolov5: v6. 2-yolov5 classification
    models, apple m1, reproducibility, clearml and deci. ai integrations. Zenodo (2022)
21. Khanam, R., Hussain, M.: Yolov11: An overview of the key architectural enhance-
    ments. arXiv preprint arXiv:2410.17725 (2024)
22. Lee, H., Song, M., Koo, J., Seo, J.: Hausdorff distance matching with adaptive
    query denoising for rotated detection transformer. In: 2025 IEEE/CVF Winter
    Conference on Applications of Computer Vision (WACV). pp. 1872–1882. IEEE
    (2025)
23. Li, F., Zhang, H., Liu, S., Guo, J., Ni, L.M., Zhang, L.: Dn-detr: Accelerate detr
    training by introducing query denoising. In: Proceedings of the IEEE/CVF con-
    ference on computer vision and pattern recognition. pp. 13619–13627 (2022)
24. Li, W., Chen, Y., Hu, K., Zhu, J.: Oriented reppoints for aerial object detection. In:
    Proceedings of the IEEE/CVF conference on computer vision and pattern recog-
    nition. pp. 1829–1838 (2022)
25. Li, Y., Li, X., Dai, Y., Hou, Q., Liu, L., Liu, Y., Cheng, M.M., Yang, J.: Lsknet:
    A foundation lightweight backbone for remote sensing: Y. li et al. International
    Journal of Computer Vision 133(3), 1410–1431 (2025)
26. Liao, Z., Zhao, Y., Shan, X., Yan, Y., Liu, C., Lu, L., Ji, X., Chen, J.: Rt-detrv4:
    Painlessly furthering real-time object detection with vision foundation models.
    arXiv preprint arXiv:2510.25257 (2025)
27. Lin, T.Y., Goyal, P., Girshick, R., He, K., Dollár, P.: Focal loss for dense object
    detection. In: Proceedings of the IEEE international conference on computer vision.
    pp. 2980–2988 (2017)
28. Liu, H., Sun, W., Zhang, Q., Di, D., Gong, B., Li, H., Wei, C., Zou, C.: Hi-
    vae: Efficient video autoencoding with global and detailed motion. arXiv preprint
    arXiv:2506.07136 (2025)
29. Liu, S., Li, F., Zhang, H., Yang, X., Qi, X., Su, H., Zhu, J., Zhang, L.: Dab-detr:
    Dynamic anchor boxes are better queries for detr. arXiv preprint arXiv:2201.12329
    (2022)
30. Lv, W., Zhao, Y., Chang, Q., Huang, K., Wang, G., Liu, Y.: Rt-detrv2: Improved
    baseline with bag-of-freebies for real-time detection transformer. arXiv preprint
    arXiv:2407.17140 (2024)
31. Lyu, C., Zhang, W., Huang, H., Zhou, Y., Wang, Y., Liu, Y., Zhang, S., Chen, K.:
    Rtmdet: An empirical study of designing real-time object detectors. arXiv preprint
    arXiv:2212.07784 (2022)
32. Meng, D., Chen, X., Fan, Z., Zeng, G., Li, H., Yuan, Y., Sun, L., Wang, J.: Con-
    ditional detr for fast training convergence. In: Proceedings of the IEEE/CVF in-
    ternational conference on computer vision. pp. 3651–3660 (2021)
33. Peng, Y., Li, H., Wu, P., Zhang, Y., Sun, X., Wu, F.: D-fine: Redefine re-
    gression task in detrs as fine-grained distribution refinement. arXiv preprint
    arXiv:2410.13842 (2024)
                 RiO-DETR: DETR for Real-time Oriented Object Detection               17

34. Redmon, J., Divvala, S., Girshick, R., Farhadi, A.: You only look once: Unified,
    real-time object detection. In: Proceedings of the IEEE conference on computer
    vision and pattern recognition. pp. 779–788 (2016)
35. Ren, S., He, K., Girshick, R., Sun, J.: Faster r-cnn: Towards real-time object de-
    tection with region proposal networks. IEEE transactions on pattern analysis and
    machine intelligence 39(6), 1137–1149 (2016)
36. Robinson, I., Robicheaux, P., Popov, M., Ramanan, D., Peri, N.: Rf-detr:
    neural architecture search for real-time detection transformers. arXiv preprint
    arXiv:2511.09554 (2025)
37. Sapkota, R., Cheppally, R.H., Sharda, A., Karkee, M.: Yolo26: key architectural
    enhancements and performance benchmarking for real-time object detection. arXiv
    preprint arXiv:2509.25164 (2025)
38. Sohan, M., Sai Ram, T., Rami Reddy, C.V.: A review on yolov8 and its advance-
    ments. In: International conference on data intelligence and cognitive informatics.
    pp. 529–545. Springer (2024)
39. Sun, W., Che, Y., Huang, H., Guo, Y.: Neural reconstruction of relightable human
    model from monocular video. In: Proceedings of the IEEE/CVF International Con-
    ference on Computer Vision. pp. 397–407 (2023)
40. Sun, W., Wang, Z., Hu, Z., Wang, C., Li, H., Chen, W.: Muse: A multi-agent frame-
    work for unconstrained story envisioning via closed-loop cognitive orchestration.
    arXiv preprint arXiv:2602.03028 (2026)
41. Tian, Y., Ye, Q., Doermann, D.: Yolov12: Attention-centric real-time object detec-
    tors. arXiv preprint arXiv:2502.12524 (2025)
42. Tian, Z., Shen, C., Chen, H., He, T.: Fcos: Fully convolutional one-stage object
    detection. In: Proceedings of the IEEE/CVF international conference on computer
    vision. pp. 9627–9636 (2019)
43. Wang, D., Zhang, Q., Xu, Y., Zhang, J., Du, B., Tao, D., Zhang, L.: Advancing
    plain vision transformer toward remote sensing foundation model. IEEE transac-
    tions on geoscience and remote sensing 61, 1–15 (2022)
44. Wang, S., Xia, C., Lv, F., Shi, Y.: Rt-detrv3: Real-time end-to-end object detection
    with hierarchical dense positive supervision. In: WACV. pp. 1628–1636 (2025)
45. Wen, L., Cheng, Y., Fang, Y., Li, X.: A comprehensive survey of oriented object
    detection in remote sensing images. Expert Systems with Applications 224, 119960
    (2023)
46. Xia, G.S., Bai, X., Ding, J., Zhu, Z., Belongie, S., Luo, J., Datcu, M., Pelillo, M.,
    Zhang, L.: Dota: A large-scale dataset for object detection in aerial images. In:
    Proceedings of the IEEE conference on computer vision and pattern recognition.
    pp. 3974–3983 (2018)
47. Xie, X., Cheng, G., Wang, J., Yao, X., Han, J.: Oriented r-cnn for object detection.
    In: Proceedings of the IEEE/CVF international conference on computer vision. pp.
    3520–3529 (2021)
48. Xu, C., Ding, J., Wang, J., Yang, W., Yu, H., Yu, L., Xia, G.S.: Dynamic coarse-to-
    fine learning for oriented tiny object detection. In: Proceedings of the IEEE/CVF
    conference on computer vision and pattern recognition. pp. 7318–7328 (2023)
49. Xu, S., Wang, X., Lv, W., Chang, Q., Cui, C., Deng, K., Wang, G., Dang, Q.,
    Wei, S., Du, Y., et al.: Pp-yoloe: An evolved version of yolo. arXiv preprint
    arXiv:2203.16250 (2022)
50. Yang, S., Pei, Z., Zhou, F., Wang, G.: Rotated faster r-cnn for oriented object
    detection in aerial images. In: Proceedings of the 2020 3rd International Conference
    on Robot Systems and Applications. pp. 35–39 (2020)
18      Z. Hu et al.

51. Yang, X., Yan, J.: Arbitrary-oriented object detection with circular smooth label.
    In: European conference on computer vision. pp. 677–694. Springer (2020)
52. Yang, X., Yan, J., Ming, Q., Wang, W., Zhang, X., Tian, Q.: Rethinking rotated
    object detection with gaussian wasserstein distance loss. In: International confer-
    ence on machine learning. pp. 11830–11841. PMLR (2021)
53. Yang, X., Yang, X., Yang, J., Ming, Q., Wang, W., Tian, Q., Yan, J.: Learning high-
    precision bounding box for rotated object detection via kullback-leibler divergence.
    Advances in Neural Information Processing Systems 34, 18381–18394 (2021)
54. Yang, X., Zhou, Y., Zhang, G., Yang, J., Wang, W., Yan, J., Zhang, X., Tian, Q.:
    The kfiou loss for rotated object detection. arXiv preprint arXiv:2201.12558 (2022)
55. Yin, X., Di, D., Fan, L., Li, H., Chen, W., , G., Song, Y., Sun, X., Yang, X.:
    Grpose: Learning graph relations for human image generation with pose priors.
    Proceedings of the AAAI Conference on Artificial Intelligence 39(9), 9526–9534
    (2025). https://doi.org/10.1609/aaai.v39i9.33032
56. Yin, X., Yu, Z., Jiang, L., Gao, X., Sun, X., Liu, Z., Yang, X.: Structure-guided
    diffusion transformer for low-light image enhancement. IEEE Transactions on Mul-
    timedia (2025)
57. Yuan, X., Zheng, Z., Li, Y., Liu, X., Liu, L., Li, X., Hou, Q., Cheng, M.M.: Strip
    r-cnn: Large strip convolution for remote sensing object detection. arXiv preprint
    arXiv:2501.03775 (2025)
58. Yujie, L., Xiaorui, S., Wenbin, S., Yafu, Y.: S2anet: Combining local spectral and
    spatial point grouping for point cloud processing. Virtual Reality & Intelligent
    Hardware 6(4), 267–279 (2024)
59. Zeng, Y., Chen, Y., Yang, X., Li, Q., Yan, J.: Ars-detr: Aspect ratio-sensitive
    detection transformer for aerial oriented object detection. IEEE transactions on
    geoscience and remote sensing 62, 1–15 (2024)
60. Zhang, H., Li, F., Liu, S., Zhang, L., Su, H., Zhu, J., Ni, L.M., Shum, H.Y.: Dino:
    Detr with improved denoising anchor boxes for end-to-end object detection. arXiv
    preprint arXiv:2203.03605 (2022)
61. Zhao, J., Ding, Z., Zhou, Y., Zhu, H., Du, W.L., Yao, R., El Saddik, A.: Ori-
    entedformer: An end-to-end transformer-based oriented object detector in remote
    sensing images. IEEE Transactions on Geoscience and Remote Sensing 62, 1–16
    (2024)
62. Zhao, Y., Lv, W., Xu, S., Wei, J., Wang, G., Dang, Q., Liu, Y., Chen, J.: Detrs beat
    yolos on real-time object detection. In: Proceedings of the IEEE/CVF conference
    on computer vision and pattern recognition. pp. 16965–16974 (2024)
63. Zhao, Z., Xue, Q., He, Y., Bai, Y., Wei, X., Gong, Y.: Projecting points to axes:
    Oriented object detection via point-axis representation. In: European conference
    on computer vision. pp. 161–179. Springer (2024)
64. Zhou, B., Bi, Q., Ding, J., Xia, G.S.: Boosting fine-grained oriented object detection
    via text features. In: International Conference on Pattern Recognition. pp. 109–
    125. Springer (2024)
65. Zhou, Y., Yang, X., Zhang, G., Wang, J., Liu, Y., Hou, L., Jiang, X., Liu, X.,
    Yan, J., Lyu, C., et al.: Mmrotate: A rotated object detection benchmark using
    pytorch. In: Proceedings of the 30th ACM international conference on multimedia.
    pp. 7331–7334 (2022)
66. Zhu, X., Su, W., Lu, L., Li, B., Wang, X., Dai, J.: Deformable detr: Deformable
    transformers for end-to-end object detection. arXiv preprint arXiv:2010.04159
    (2020)
67. Zou, Z., Chen, K., Shi, Z., Guo, Y., Ye, J.: Object detection in 20 years: A survey.
    Proceedings of the IEEE 111(3), 257–276 (2023)
    Appendix of RiO-DETR: DETR for Real-time
             Oriented Object Detection

A     More Implementation Details

A.1   More Details about Our Implemented Baseline

As described in Sec. 3.1, because the community lacked real-time DETR-style
oriented detectors, we built a baseline by extending the official RT-DETRv2
codebase with full oriented-detection support [9].
    Specifically, we added an OBB data pipeline (loading, format conversion,
and geometry-aware augmentation), an oriented regression head that outputs a
5D box parameterization, as well as the corresponding post-processing utilities
and submission interface required by oriented benchmarks. Some classes and
functions were adapted from MMRotate for implementation convenience [18]. To
make the baseline stable and competitive under one-to-one matching, we followed
RHINO-DETR’s rotated-DETR practice by replacing the IoU-style regression
objective with a KLD-based loss, and further adopted the Hausdorff-distance
matching cost to reduce assignment ambiguity caused by angle periodicity and
near-square instances [7]. Building on recent advances in real-time DETRs, we
further incorporated (i) the universal matching strategy from D-FINE to improve
matching robustness and optimization behavior [11], and (ii) the Dense O2O
training scheme from DEIM to densify supervision without adding extra heads or
decoders, thus accelerating convergence while preserving end-to-end inference [6].
    These modifications produced an efficient real-time oriented DETR baseline,
but did not resolve the core challenges of DETR-based oriented object detection.
It provided a strong foundation for our subsequent task-native designs.

A.2   More Implementation Details of RiO-DETR Series

Table 1 summarizes the hyperparameter settings of the RiO-DETR models. All
variants adopt HGNetV2 backbones pretrained on ImageNet [3] and use the
AdamW optimizer. To support different computational budgets, the model scale
is adjusted by reducing the embedding dimension from 384 to 128 and decreasing
the number of decoder layers from 4 in larger models to 3 in lighter ones. Most
variants use three feature levels, while RiO-DETR-n adopts two levels for higher
efficiency. Across all models, the number of queries is fixed at 300, and the same
loss weights are used, with both LL1 and LKLD set to 5. We follow training
strategies similar to RT-DETRv2. In particular, the training schedule is scaled
inversely with model size: larger models such as RiO-DETR-x are trained for
72 epochs with a batch size of 16, whereas the Nano variant is trained for 160
epochs with a batch size of 128.
2

    Table 1: Hyperparameter configurations for RiO-DETR models on DOTA-1.0.

Setting             RiO-DETR-x RiO-DETR-l RiO-DETR-m RiO-DETR-s RiO-DETR-n
Backbone Name         HGNetv2-B5       HGNetv2-B4                          HGNetv2-B2         HGNetv2-B0   HGNetv2-B0
Optimizer              AdamW            AdamW                               AdamW              AdamW        AdamW
Embedding Dimension      384              256                                 256                224          128
Feedforward Dimension   2048             1024                                1024               1024          512
Decoder Layers            4                4                                   3                  3            3
Queries                  300              300                                 300                300          300
Number of Levels          3                3                                   3                  3            2
Base LR                 8e-5                   8e-5                                 1e-4         1e-4         2e-4
Backbone LR             8e-6                   8e-6                                 1e-5         1e-5         2e-5
Weight Decay           1.25e-4                1.25e-4                               1e-4         1e-4         1e-4
Weight of LFocal          1                         1                                   1         1            1
Weight of LL1             5                         5                                   5         5            5
Weight of LKLD            5                         5                                   5         5            5
Total Batch Size         16                       16                                  16          16          128
Total Epochs             72                      102                                 102         132          160
Flat Epochs              20                       51                                  51          66           80
No Aug Epochs            12                       12                                  12          12           12

A.3    Details of Latency Measurement

For fairness, all models are evaluated for end-to-end inference latency under a
single NVIDIA T4 GPU with TensorRT.
    Engine execution. Each model is serialized into a TensorRT engine and ex-
ecuted via IExecutionContext. For TensorRT 10 engines, inference is launched
with execute_async_v3; otherwise we fall back to execute_async_v2.
    I/O shapes and memory binding. For dynamic-shape engines, we choose
optimization profile 0 and benchmark at the OPT shape. GPU buffers for all
inputs/outputs are allocated once as CUDA tensors, and their device pointers are
bound to TensorRT using tensor addresses (TensorRT 10) or bindings (legacy).
This avoids repeated allocation overhead and ensures the benchmark measures
pure GPU inference.
    Warm-up. We run 50 warm-up iterations before timing to stabilize GPU
states and eliminate one-time overhead (e.g., CUDA context initialization). All
warm-up iterations are executed asynchronously on a dedicated CUDA stream
followed by synchronization.
    Timing protocol. Latency is measured using CUDA events recorded on the
same CUDA stream. We record a start event, run inference for 1000 iterations
back-to-back, record an end event, and synchronize on the end event. The average
per-image latency (ms) is computed by

                                     \mathrm {Latency} = \frac {t_{\mathrm {elapsed}}}{N},                           (1)

where telapsed is the CUDA-event elapsed time (ms) and N is the number of
runs. Throughput is reported as FPS = 1000/Latency.
    Appendix of RiO-DETR: DETR for Real-time Oriented Object Detection                                                                      3

B    Discussion on Content-Driven Angle Estimation

Why Angle-Coupled Positional Queries Can Be Ill-Posed We first dis-
cuss the representation-level issue of coupling angle into positional queries. Let
the physical state space of an oriented bounding box be

                                      \mathcal {M}\triangleq \mathbb {R}^4 \times \big (S^1/(\theta \sim \theta +\pi )\big ), 

where (cx , cy , w, h) ∈ R4 , and θ is defined only up to a π rotation for rectangles
under the long-side definition; the same argument applies analogously to other
common angle parameterizations. Consider a DETR-style positional query

                 Q_{\mathrm {pos}} = f(c_x,c_y,w,h,\theta ), \qquad f:\mathbb {R}^4\times [0,\pi )\to \mathbb {R}^d, 

where θ is represented by a scalar chart and f is an Euclidean network.

(1) Quotient-consistency is required. Since θ and θ + π correspond to the same
physical rectangle, a well-defined representation on M should satisfy

                                                   f(x,\theta )=f(x,\theta +\pi ), 

with x = (cx , cy , w, h) and θ + π understood modulo π. Equivalently, the seam
endpoints of [0, π) should map continuously:

                                     \lim _{\varepsilon \to 0^+} f(x,\varepsilon ) = \lim _{\varepsilon \to 0^+} f(x,\pi -\varepsilon ). 

Otherwise, two physically adjacent states near the seam may produce separated
query vectors, making attention or matching overly sensitive to small angular
perturbations.

(2) Standard scalar-angle constructions do not enforce this property. For com-
mon designs such as MLP ◦ PE with a scalar angle channel, the invariance above
is generally not guaranteed unless the encoding is explicitly made π-periodic.
Thus, angle-coupled positional queries can suffer from seam inconsistency and a
mismatch between Euclidean regression and the periodic quotient geometry of
OBBs.

(3) Long-side canonicalization does not fully remove instability. Although the
long-side convention removes the (w, h, θ) ↔ (h, w, θ + π2 ) ambiguity for clearly
non-square instances, it becomes ill-conditioned near w ≈ h. A tiny perturbation
may flip the long/short-side assignment and induce an approximately π2 jump in
the canonical angle. If Qpos depends on θ, this instability is directly injected into
the positional prior, which may hurt attention, matching, and optimization for
near-square objects. Moreover, model predictions are not guaranteed to satisfy
the canonical constraint during training, so nearly equivalent parameterizations
may still yield unstable gradients.
4

Implication. A simple robust remedy is to exclude θ from the positional query:
                                        Q_{\mathrm {pos}}=\phi (c_x,c_y,w,h). 
This prevents angular ambiguity from contaminating the geometric localization
prior. However, this only explains why naive angle coupling is unstable. One may
still ask whether a better periodic or quotient-consistent encoding is sufficient.
The next subsection explains why the answer is still negative.

Why Decoupling Angle from Positional Queries Is Preferred The above
discussion concerns representation validity, but the deeper issue is information
decomposition. Even if angle is encoded in a periodic or quotient-consistent way,
it is still not ideal to inject it into the positional branch.
     The reason is that (cx , cy , w, h) and θ play different roles. The variables
(cx , cy , w, h) are geometric localization variables: they are spatially grounded and
can reliably guide cross-attention before rich semantic evidence is aggregated.
By contrast, the correct orientation is often a content-disambiguated variable,
depending on appearance cues such as texture flow, object heading, part arrange-
ment, and annotation convention. Hence, angle is not merely another coordinate
to be encoded in the positional prior.
     Suppose the decoder query is
                          Q = Q_{\mathrm {content}} + Q_{\mathrm {pos}}(c_x,c_y,w,h,\hat {\theta }),    (2)

where θ̂ is the current angle estimate. If θ̂ is inaccurate in early training or
decoding, then the model uses an orientation-conditioned positional prior before
sufficient content evidence has been collected. As a result, feature aggregation is
biased by an unreliable angle prior exactly when orientation is most ambiguous.
    This also explains why alternative encodings do not fully solve the prob-
lem. Encodings such as [sin θ, cos θ], unit-vector parameterizations, or quotient-
consistent embeddings such as [sin 2θ, cos 2θ] may improve how angle is repre-
sented, but they do not change where angle is inferred. They still route orientation-
dependent information through the positional branch, rather than letting it
emerge from content.
    Therefore, we adopt the following principle: the positional query should en-
code only variables that are both spatially grounded and reliably available before
content aggregation. Under this principle, (cx , cy , w, h) belong to Qpos , while θ
should be inferred primarily from Qcontent . Our decoupled formulation is thus
not merely a workaround for scalar-angle ill-posedness, but a better information
decomposition for oriented detection.
    Our claims above are further proved by Sec. 4.6 in the main text, Appendix
E.3 and F.

C    Details on Decoupled Periodic Refinement
Problem setting. We parameterize an OBB as (cx , cy , w, h, θ) with θ ∈ [0, π) due
to the π-periodic symmetry of rectangles. Standard DETR-style iterative refine-
    Appendix of RiO-DETR: DETR for Real-time Oriented Object Detection                                                                                                                                                                             5

ment (e.g., inverse-sigmoid additive updates) is natural for Euclidean variables
(cx , cy , w, h), but applying the same unbounded Euclidean regression/update to
θ is ill-posed since angles live on a periodic domain with the seam 0 ≡ π.

Why Euclidean regression can contradict periodic geometry. Consider θtgt = ε
and θpred = π − ε with ε → 0+ . They are geometrically adjacent on [0, π), yet the
Euclidean gap is |θpred −θtgt | ≈ π. Thus, a Euclidean L1 objective may encourage
traversing the long arc in the chart, causing seam instability and slowing early
optimization (especially for near-square/ambiguous instances).

Periodic shortest-path operator. We define a π-periodic wrap and the signed
shortest angular difference. For any u ∈ R,

                                                              \mathrm {wrap}_{\pi }(u)=u-\pi \left \lfloor \frac {u}{\pi }\right \rfloor \in [0,\pi ). \label {eq:dpr_wrap}                                                                       (3)

Then
                       \Delta _{\pi }(\theta _p,\theta _t) = \mathrm {wrap}_{\pi }\!\left (\theta _p-\theta _t+\tfrac {\pi }{2}\right )-\tfrac {\pi }{2} \in \left [-\tfrac {\pi }{2},\tfrac {\pi }{2}\right ). \label {eq:dpr_shortest_delta}    (4)
This is seam-consistent: crossing 0/π does not create a large jump in ∆π (a.e.).

Shortest-path periodic L1 for angle regression.

                                                                                 \mathcal {L}_{\angle } = \left |\Delta _{\pi }(\theta _{\mathrm {pred}},\theta _{\mathrm {tgt}})\right |. \label {eq:dpr_sp_l1}                                  (5)

Compared with Euclidean L1 , Eq. (5) measures the geodesic error on the π-
periodic domain and yields shortest-path gradients.

Bounded periodic refinement update. We keep inverse-sigmoid refinement for
(cx , cy , w, h), and decouple θ with a bounded periodic update:

                                                        \theta ^{(i+1)} = \mathrm {wrap}_{\pi }\!\Big (\theta ^{(i)} + \alpha _i \cdot g(\delta ^{(i)})\Big ), \label {eq:dpr_update}                                                             (6)

where δ (i) is the raw angle offset at decoder layer i, g(·) is bounded (we use
tanh), and
                         \alpha _i = \alpha _0^{-i}, \qquad i\in \{0,1,\dots ,L-1\}. \label {eq:dpr_alpha}  (7)
This yields bounded steps and a coarse-to-fine refinement across layers.

D      Detailed Results on Benchmarks

D.1      Per-class Results on DOTA-1.0 Multi-scale

We provide the per-class results on DOTA-1.0 under the multi-scale training/testing
protocol in Table 3. The table reports detailed AP50 scores for each category.
These results supplement the overall comparisons in the main text with a category-
level evaluation under the multi-scale setting.
6

Table 2: Comparison on DOTA-1.0 under single-scale training and testing protocol.
Left: high-precision comparison. Right: results of RiO-DETR on other backbones.

Method                          Backbone    AP50        AP75                Methods                    Backbone     #P         Flops   Lat.     AP50

Oriented R-CNN [13]               R-50         74.19    46.96               LSKNet-S [8]               LSKNet-S    31.0M       161G    203.5    77.5
RoI Trans. [4]                    R-50         74.05    46.54               AO2-DETR [2]               R-50        74.3M       304G      -      77.7
RoI Trans. [4]                   Swin-T        76.49    50.15               RHINO-DETR [7]             R-50        47.6M       566G    187.9    78.7
                                                                            RHINO-DETR [7]             Swin-T      50.8M       609G    242.6    79.4
ReDet [5]                        ReR-50        76.25    50.86
                                                                            Oriented-DETR [17]         R-50        57.2M       302G    217.3    79.1
ARS-DETR [16]                     R-50         73.79    49.01
                                                                            Oriented-DETR [17]         Swin-T      57.7M       309G    235.5    79.8
ARS-DETR [16]                    Swin-T        75.79    51.11
                                                                            YOLO26m-obb [12]           YOLO26m     21.2M       183G     10.2    80.0
RHINO w/ KLD [7]                  R-50         78.49    51.84               YOLO26l-obb [12]           YOLO26l     25.6M       230G     13.0    80.2
RHINO w/ GRIoU [7]                R-50         77.24    53.91               YOLO26x-obb [12]           YOLO26x     57.6M       517G     30.5    80.4
YOLO26x-obb                     YOLO26x        80.12    58.04
                                                                            RiO-DETR-R50    R-50                   52.7M       217G    12.6     80.1
RiO-DETR-x w/ KLD               HGNet-B5    81.78       56.35               RiO-DETR-Swin-T Swin-T                 55.9M       221G    28.5     80.8
RiO-DETR-x w/ GRIoU             HGNet-B5    80.62       58.49               RiO-DETR-LSKNet LSKNet-S               42.1M       176G    88.7     81.2

Table 3: Comparison with state-of-the-art oriented object detectors on DOTA-1.0
under multi-scale training and testing protocol.

Methods            Backbone      #P    Flops Lat. AP50 PL            BD BR GTF SV            LV   SH   TC   BC    ST SBF RA HA             SP    HC
                                               Non-Real-time Oriented Object Detectors
PKINet-S [1]       PKINet-S      30.8M 190G 359.7 81.06 89.0 86.7 59.0 81.2 80.4 84.9 88.1 90.9 86.6 87.3 67.1 74.8 78.2 81.9 70.6
LSKNet-S [8]       LSKNet-S      31.0M 161G 203.5 81.64 89.6 86.3 63.1 83.7 82.2 86.1 88.7 90.9 88.4 87.4 71.7 69.6 78.9 81.8 76.5
Strip R-CNN-S [15] StripNet-S    30.5M 159G 241.9 82.28 89.2 85.6 62.4 83.7 81.9 86.6 88.8 90.9 88.0 87.9 72.1 71.9 79.2 82.5 82.8
                                                 Real-time Oriented Object Detectors
PPYOLOE-R-x [14] CRN-x      98.4M       264G     51.0   80.73   88.5 84.5 60.6   77.7   83.3 85.4 89.0 90.8 88.5 87.5   69.3   66.0 77.9 81.4 80.9
RTMDet-R-l [10]  CSPNext-l  52.3M       205G     30.2   81.33   88.4 85.0 57.3   80.5   80.6 84.9 88.1 90.9 86.3 87.6   69.3   70.6 78.6 81.0 79.2
YOLO26m-obb [12] YOLO26l    25.6M       230G     10.2   81.00   89.1 86.1 59.1   78.1   81.2 85.7 88.7 90.9 87.7 88.9   70.6   69.3 78.8 82.4 83.3
YOLO26x-obb [12] YOLO26x    57.6M       517G     30.5   81.70   89.2 86.9 62.0   80.7   81.6 86.0 88.7 90.8 87.2 88.8   70.1   68.1 84.5 81.7 88.1
RiO-DETR-m       HGNetv2-B2 18.6M       158G      8.8   81.49   87.3 87.2 61.7   81.8   82.5 86.2 89.2 90.6 88.7 88.7   74.5   71.4 78.8 74.4 79.7
RiO-DETR-x       HGNetv2-B5 62.5M       527G     29.9   81.76   83.8 87.3 62.6   79.9   82.7 86.3 89.1 90.6 88.5 88.0   72.5   75.2 78.9 81.8 79.2

D.2       Per-class Results on FAIR-1M-2.0 Multi-scale

We provide the per-class results on FAIR-1M-2.0 under the multi-scale setting in
Table 4. The table presents detection results for all categories and supplements
the overall quantitative comparisons in the main text by providing a class-wise
evaluation of RiO-DETR-m, RiO-DETR-x, and other compared methods.

D.3       Results of High-Precision Metrics

In mainstream oriented object detection benchmarks, AP50 is commonly used as
the only metric for performance comparison. We follow this convention and use
AP50 as the main evaluation criterion. To further assess localization accuracy
under stricter matching conditions, we additionally report AP75 .
    Our default model adopts KLD as part of the regression loss, since it is a
widely used and stable choice in rotated object detection, providing a fair and
standard setting for comparison with prior methods. Under this default setting,
RiO-DETR-x achieves the best AP50 of 81.78, surpassing all previous methods.
    Lee et al. [7] found that replacing KLD with GRIoU can shifts the optimiza-
tion more toward overlap-aware high-precision localization in oriented DETRs.
We follow their setting, and RiO-DETR-x w/ GRIoU achieves 80.62 AP50 and
58.49 AP75 , outperforming all compared methods on both metrics.
    Appendix of RiO-DETR: DETR for Real-time Oriented Object Detection                                                          7

Table 4: Comparison with state-of-the-art models on the FAIR-1M-2.0 dataset. The
object categories in the table of C1–C37 (in order) is: Boeing737, Boeing747, Boe-
ing777, Boeing787, C919, A220, A321, A330, A350, ARJ21, OtherAirplane, SmallCar,
Bus, CargoTruck, DumpTruck, Van, Trailer, Tractor, Excavator, TruckTractor, Oth-
erVehicle, BasketballCourt, TennisCourt, FootballField, BaseballField, Intersection,
Roundabout, Bridge, PassengerShip, Motorboat, FishingBoat, Tugboat, Engineering-
Ship, LiquidCargoShip, DryCargoShip, Warship, OtherShip.

                     C1 C2 C3 C4 C5 C6 C7 C8 C9 C10 C11 C12 C13 C14 C15 C16 C17 C18 C19 AP50
Method
                     C20 C21 C22 C23 C24 C25 C26 C27 C28 C29 C30 C31 C32 C33 C34 C35 C36 C37 – (%)
                     38.3 61.7 15.0 35.4 0.4 44.0 53.3 30.6 20.7 3.9 70.7 53.6 9.4 29.9 21.2 48.3 2.8       0.1   2.2
SASM RepPoints∗                                                                                                          30.9
                      0.1 2.4 37.2 80.4 49.9 87.4 44.5 54.8 28.3 14.7 31.9 14.3 24.8 17.7 25.7 48.4 32.2    5.9    –

         ∗           39.2 82.7 15.9 52.0 0.2 41.0 54.5 44.2 43.5 9.3 73.1 55.1 11.5 37.9 26.0 51.0 6.3      1.1   12.9
R-FCOS                                                                                                                   36.1
                      5.4 2.7 43.7 86.2 56.3 88.1 48.0 57.2 25.7 24.0 43.8 22.0 18.9 31.5 33.4 56.8 27.3    7.3    –
                     40.4 83.7 17.2 49.9 0.2 42.5 57.0 42.7 52.0 10.3 74.8 66.2 13.4 39.7 35.7 61.7 2.8     0.8   10.5
S2A-Net∗                                                                                                                 37.4
                      2.5 2.2 46.2 82.1 59.0 88.2 41.5 62.9 20.3 24.8 42.9 19.9 24.8 32.5 33.3 58.5 34.9    6.6    –
                     37.5 82.5 15.4 47.7 9.4 41.7 50.8 47.5 60.6 8.3 72.5 57.7 12.9 41.4 38.2 53.4 11.7     2.1   16.8
R-Faster R-CNN∗                                                                                                          37.5
                     11.9 2.0 42.6 83.3 55.4 89.4 50.4 65.1 26.1 19.0 47.5 17.9 24.2 26.3 30.5 54.1 26.3    8.0    –

                 ∗   37.7 81.4 15.4 48.8 7.9 43.4 54.6 43.5 56.6 9.5 73.3 62.9 15.4 42.0 42.8 59.5 4.5      0.6   17.0
O-RepPoints                                                                                                              38.9
                      5.7 0.9 46.3 84.3 61.4 89.2 46.7 60.8 33.2 24.6 50.4 24.9 22.2 32.8 34.7 60.0 37.9    7.4    –
                     37.6 84.8 16.9 49.0 7.3 41.6 49.7 43.1 62.4 13.1 72.1 59.8 18.5 43.9 41.5 56.0 7.9  2.2 24.4
O-RCNN∗                                                                                                                  40.4
                     10.4 1.2 47.2 83.3 59.6 89.1 48.3 62.6 31.8 26.6 58.5 28.2 25.5 38.8 37.3 64.6 38.7 10.7 –

             ∗       38.9 81.8 14.6 46.1 7.1 42.4 55.4 38.6 57.3 10.3 73.4 62.2 20.6 43.7 43.4 58.5 13.7    1.9   21.0
RoI Trans.                                                                                                               40.2
                     16.5 1.3 50.4 86.2 61.0 88.7 50.2 66.3 30.7 26.3 52.1 27.7 26.9 32.2 32.6 61.9 37.0    9.3    –

                 ∗   44.6 83.4 18.5 47.9 11.7 44.6 59.4 47.5 59.9 18.0 76.1 63.3 20.2 45.0 45.5 59.1 10.4   2.2   21.7
LOOD (RT)                                                                                                                42.6
                     22.2 1.7 52.3 84.7 67.3 89.8 50.8 68.2 37.3 28.8 51.9 28.3 24.6 33.9 39.0 64.1 41.4    9.7    –
                     37.1 86.6 16.5 57.2 9.4 44.9 59.1 45.4 60.3 11.1 76.4 63.7 20.9 44.2 42.7 59.7 13.2 1.8 24.2
ReDet∗                                                                                                                   43.2
                     16.7 1.4 55.8 86.2 66.8 91.0 51.1 74.5 37.6 31.8 57.2 33.8 21.3 45.5 36.5 67.0 39.9 10.8 –
                     43.1 90.6 22.2 55.8 9.4 46.6 63.7 55.8 68.3 16.5 77.0 64.9 23.3 45.8 45.5 61.2 12.5    4.8   19.0
LOOD (RD)∗                                                                                                               44.9
                     14.9 1.6 54.2 84.6 64.7 92.4 50.7 71.7 41.2 34.1 56.5 34.6 22.6 46.3 38.8 68.6 48.0    9.6    –
                     35.2 80.1 11.9 45.3 19.8 38.9 52.4 43.5 64.2 10.7 68.3 73.7 31.8 53.9 54.4 72.9 26.3 4.6 37.4
Strip-RCNN-S                                                                                                             45.3
                     54.7 5.6 51.1 79.5 59.9 87.2 48.5 55.4 39.7 27.1 61.4 45.4 22.0 42.3 37.7 67.0 49.0 17.1  –
                     31.9 80.0 4.7 38.3 19.7 42.3 43.1 39.1 70.1 14.3 68.5 74.2 40.6 55.4 54.7 73.4 24.5 1.0 40.4
LSKNet-S                                                                                                                 45.8
                     56.6 10.8 49.9 79.5 62.6 86.9 50.8 65.4 46.3 28.7 58.3 42.6 26.0 40.9 38.1 66.5 52.7 15.2 –
                     28.2 80.7 3.7 38.6 16.5 40.8 41.7 40.7 60.7 8.7 66.7 71.6 31.9 52.3 50.7 71.3 18.9 0.1 29.2
YOLO26m-obb                                                                                                              42.5
                     47.8 6.9 46.8 78.1 57.9 85.7 46.8 62.0 35.7 29.0 55.0 41.0 24.2 38.1 34.7 64.7 50.0 15.1 –
                     34.2 83.3 7.5 44.3 23.6 43.4 45.7 45.2 65.8 14.5 69.7 74.4 37.1 56.4 54.8 74.2 25.3 1.0 35.2
YOLO26x-obb                                                                                                              46.7
                     54.6 8.2 50.5 80.5 61.9 87.8 51.2 67.1 41.2 33.4 60.0 47.1 26.0 43.6 39.6 68.0 53.9 17.7 –
                     36.0 82.4 9.6 44.9 20.5 37.4 46.1 53.0 54.6 13.5 68.7 72.7 22.4 51.9 49.5 73.1 17.7 0.7 27.2
RiO-DETR-m                                                                                                               43.6
                     40.4 6.0 45.1 78.9 56.9 85.6 51.6 67.2 30.3 34.7 62.6 44.4 25.3 41.3 38.8 65.8 42.6 12.4 –
                     35.4 85.2 9.0 48.2 26.0 43.5 47.0 49.3 61.7 14.0 69.9 75.2 35.1 57.8 55.5 75.5 26.7 1.6 31.8
RiO-DETR-x                                                                                                               47.4
                     53.7 6.8 50.6 80.9 61.0 88.2 54.0 71.0 39.7 36.6 60.8 50.0 25.4 45.2 40.2 68.7 54.3 19.2 –

D.4          Results on Other Backbones
Table 2 reports the single-scale training and testing results of RiO-DETR when
instantiated with different backbones on DOTA-1.0. The base model size is x.
We keep the detector head and training protocol unchanged and only replace
the backbone, so that the comparison reflects the portability of the proposed
oriented DETR design. Across all tested backbones, RiO-DETR consistently
achieves better accuracy than compared DETR-based and CNN-based models,
while maintaining a favorable efficiency profile.

E        Further Analyses and Visualizations
E.1          Further Visualization of Oriented Dense O2O
Fig. 2 shows the per-epoch AP50 during training for three settings: without
Dense O2O, with standard Dense O2O, and with our Oriented Dense O2O. In-
troducing Dense O2O already improves the convergence speed compared with
8

                                                      0.7

                                                      0.6

                                                      0.5

                                               AP50
                                                      0.4

                                                      0.3
                                                                                        RiO-DETR-m
                                                      0.2                               w/o Dense O2O
                                                                                        w/o Oriented Dense O2O
                                                            0   10   20   30       40      50      60     70
                                                                               Epoch

Fig. 1: Visualizations of layer-wise angular re- Fig. 2: Per-epoch AP50 , which shows
finement for square-like instances.              the difference in convergence speed.

the vanilla training scheme, indicating that denser one-to-one supervision pro-
vides stronger learning signals at early stages. Our Oriented Dense O2O further
accelerates convergence and achieves consistently higher AP50 throughout train-
ing. In particular, the gap becomes evident in the early epochs, suggesting that
orientation-aware densification provides more effective angular supervision and
allows the model to enter a stable refinement regime earlier.

E.2   Angular Prediction across Decoder Layers

To further analyze the coarse-to-fine refinement behavior, we present a layer-wise
evaluation of angular predictions in Table 6. “Avg Error” denotes the mean ab-
solute angular error w.r.t. ground truth, while “Avg Delta” measures the angular
adjustment introduced by each decoder layer. As expected, Layer 1 produces the
largest shift (0.515◦ ), establishing the primary orientation. In later layers, the
“Avg Delta” decreases exponentially (0.221◦ → 0.048◦ ), indicating a transition
to fine-grained refinements. This confirms that the decaying factor αi stabilizes
decoding, suppressing late-stage oscillations and enabling precise convergence.
We also provide visualizations for square-like cases in Figure 1 to prove the
robustness of our angle prediction.

E.3   More t-SNE Visualizations

We provide additional t-SNE visualizations on FAIR-1M-2.0 to better under-
stand the representation learned by the content queries. Figure 3 presents per-
category t-SNE plots, with points colored by the oriented bounding-box angle θ.
Across many categories, the color distribution is not strictly separated into iso-
lated angle-specific islands; instead, different angles are often interleaved within
the same local neighborhoods. This indicates that the content-query space is not
trivially dominated by the periodic angle signal, but retains content/appearance
cues as the primary organizing factor. Meanwhile, for categories with strong
viewpoint regularities (e.g., vehicles on roads or ships aligned with shipping
   Appendix of RiO-DETR: DETR for Real-time Oriented Object Detection                                       9

Fig. 3: Per-category t-SNE visualizations with orientation coloring on FAIR-1M-2.0.

lanes), we occasionally observe mild angle-correlated gradients or sub-structures,
which is expected given dataset bias and scene geometry. Overall, these visualiza-
tions qualitatively support the design goal of learning orientation from content
while avoiding degenerate representations that collapse to a single direction cue.

Table 5: Hyperparameter ablations for                 Table 6: Layer-wise analysis of angular
Decoupled Periodic Refinement.                        prediction during decoding of TROD-x.

α0            1.0       1.5        2.0      2.5             Layer         Avg Error (◦ )   Avg Delta (◦ )
AP50         74.27     74.74      74.45    74.68
                                                          0 (Initial)          8.20            0.000
Strategy     None     Linear       Exp     Power               1               8.11            0.515
AP50         74.18    74.49       74.74    74.61               2               8.09            0.221
                                                               3               8.08            0.048
Activation   Linear    Tanh        Sin    Sigmoid
AP50         73.92     74.74      74.69    74.23

Table 7: Ablation study on Attention Head Splitting Strategy for Rotation-Rectified
Orthogonal Attention. H denotes the number of attention heads (default H = 8)

                      Strategy                      Ratio (θ : θ + π/2)       AP50

                      Vanilla Alignment                     8 : 0             73.81
                      Asymmetric Alignment                  6 : 2             74.02
                      Multi-angle Distribution         2 : 2 : 2 : 2∗         73.95
                      Symmetric Orthogonal                  4 : 4             74.18
                      ∗
                          Multi-angle includes θ, θ + π/4, θ + π/2, and θ + 3π/4.
10

             Table 8: Ablation on injecting angle into the positional query.

         Positional Query Representation Angle in Positional Branch Periodicity-aware Encoding AP50
         (cx , cy , w, h, θ)                        Yes                        No             73.47
         (cx , cy , w, h, sin θ, cos θ)             Yes                       Yes             72.60
         (cx , cy , w, h, sin 2θ, cos 2θ)           Yes                       Yes             73.52
         (cx , cy , w, h) (Ours)                    No                        N/A             74.18

F    Further Ablation Studies
Ablation on Positional Encodings. Table 8 examines whether the gain of
our design mainly comes from using a better periodic angle parameterization, or
from decoupling angle from the positional branch altogether. Replacing the raw
angle θ with (sin θ, cos θ) even degrades performance from 73.47 to 72.60 AP50 ,
while the quotient-consistent encoding (sin 2θ, cos 2θ) only brings a marginal im-
provement to 73.52 AP50 . In contrast, our fully decoupled design, which removes
angle from the positional query and keeps only (cx , cy , w, h), achieves the best re-
sult of 74.18 AP50 . These results suggest that the limitation is not merely caused
by a suboptimal periodic encoding. Instead, injecting angle into the positional
branch is itself less suitable for oriented DETR. Overall, this ablation supports
our claim that angle should be primarily estimated from content features, rather
than being encoded in the positional query.

Hyperparameter Ablation on Decoupled Periodic Refinement. Table 5
examines key hyperparameters in Decoupled Periodic Refinement. The decay
base factor α0 = 1.5 yields the best result (74.74 AP50 ), while smaller (1.0) or
larger values (2.0–3.0) degrade performance, highlighting the need for a proper
decay rate. Exponential decay consistently outperforms none, linear, and power
schedules, and tanh achieves the highest AP50 (74.74) among the tested activa-
tion functions.

Ablation on the Design of Rotation-Rectified Orthogonal Attention.
Table 7 analyzes head splitting in Rotation-Rectified Orthogonal Attention.
Aligning all heads to θ yields 73.81 AP50 , while an asymmetric 6:2 split slightly
improves performance to 74.02. The symmetric orthogonal design (4:4 for θ and
θ + π/2) performs best at 74.18, showing that modeling orthogonal directions
better captures longitudinal and lateral structures. Distributing heads across
four angles further reduces performance (73.95), due to diluted capacity per
direction.
   Appendix of RiO-DETR: DETR for Real-time Oriented Object Detection                 11

References
 1. Cai, X., Lai, Q., Wang, Y., Wang, W., Sun, Z., Yao, Y.: Poly kernel inception
    network for remote sensing detection. In: Proceedings of the IEEE/CVF conference
    on computer vision and pattern recognition. pp. 27706–27716 (2024)
 2. Dai, L., Liu, H., Tang, H., Wu, Z., Song, P.: Ao2-detr: Arbitrary-oriented object
    detection transformer. IEEE transactions on circuits and systems for video tech-
    nology 33(5), 2342–2356 (2022)
 3. Deng, J., Dong, W., Socher, R., Li, L.J., Li, K., Fei-Fei, L.: Imagenet: A large-
    scale hierarchical image database. In: 2009 IEEE conference on computer vision
    and pattern recognition. pp. 248–255. Ieee (2009)
 4. Ding, J., Xue, N., Long, Y., Xia, G.S., Lu, Q.: Learning roi transformer for oriented
    object detection in aerial images. In: Proceedings of the IEEE/CVF conference on
    computer vision and pattern recognition. pp. 2849–2858 (2019)
 5. Han, J., Ding, J., Xue, N., Xia, G.S.: Redet: A rotation-equivariant detector for
    aerial object detection. In: Proceedings of the IEEE/CVF conference on computer
    vision and pattern recognition. pp. 2786–2795 (2021)
 6. Huang, S., Lu, Z., Cun, X., Yu, Y., Zhou, X., Shen, X.: Deim: Detr with improved
    matching for fast convergence. In: Proceedings of the computer vision and pattern
    recognition conference. pp. 15162–15171 (2025)
 7. Lee, H., Song, M., Koo, J., Seo, J.: Hausdorff distance matching with adaptive
    query denoising for rotated detection transformer. In: 2025 IEEE/CVF Winter
    Conference on Applications of Computer Vision (WACV). pp. 1872–1882. IEEE
    (2025)
 8. Li, Y., Li, X., Dai, Y., Hou, Q., Liu, L., Liu, Y., Cheng, M.M., Yang, J.: Lsknet:
    A foundation lightweight backbone for remote sensing: Y. li et al. International
    Journal of Computer Vision 133(3), 1410–1431 (2025)
 9. Lv, W., Zhao, Y., Chang, Q., Huang, K., Wang, G., Liu, Y.: Rt-detrv2: Improved
    baseline with bag-of-freebies for real-time detection transformer. arXiv preprint
    arXiv:2407.17140 (2024)
10. Lyu, C., Zhang, W., Huang, H., Zhou, Y., Wang, Y., Liu, Y., Zhang, S., Chen, K.:
    Rtmdet: An empirical study of designing real-time object detectors. arXiv preprint
    arXiv:2212.07784 (2022)
11. Peng, Y., Li, H., Wu, P., Zhang, Y., Sun, X., Wu, F.: D-fine: Redefine re-
    gression task in detrs as fine-grained distribution refinement. arXiv preprint
    arXiv:2410.13842 (2024)
12. Sapkota, R., Cheppally, R.H., Sharda, A., Karkee, M.: Yolo26: key architectural
    enhancements and performance benchmarking for real-time object detection. arXiv
    preprint arXiv:2509.25164 (2025)
13. Xie, X., Cheng, G., Wang, J., Yao, X., Han, J.: Oriented r-cnn for object detection.
    In: Proceedings of the IEEE/CVF international conference on computer vision. pp.
    3520–3529 (2021)
14. Xu, S., Wang, X., Lv, W., Chang, Q., Cui, C., Deng, K., Wang, G., Dang, Q.,
    Wei, S., Du, Y., et al.: Pp-yoloe: An evolved version of yolo. arXiv preprint
    arXiv:2203.16250 (2022)
15. Yuan, X., Zheng, Z., Li, Y., Liu, X., Liu, L., Li, X., Hou, Q., Cheng, M.M.: Strip
    r-cnn: Large strip convolution for remote sensing object detection. arXiv preprint
    arXiv:2501.03775 (2025)
16. Zeng, Y., Chen, Y., Yang, X., Li, Q., Yan, J.: Ars-detr: Aspect ratio-sensitive
    detection transformer for aerial oriented object detection. IEEE transactions on
    geoscience and remote sensing 62, 1–15 (2024)
12

17. Zhao, Z., Xue, Q., He, Y., Bai, Y., Wei, X., Gong, Y.: Projecting points to axes:
    Oriented object detection via point-axis representation. In: European conference
    on computer vision. pp. 161–179. Springer (2024)
18. Zhou, Y., Yang, X., Zhang, G., Wang, J., Liu, Y., Hou, L., Jiang, X., Liu, X.,
    Yan, J., Lyu, C., et al.: Mmrotate: A rotated object detection benchmark using
    pytorch. In: Proceedings of the 30th ACM international conference on multimedia.
    pp. 7331–7334 (2022)
