---
source_id: 202
bibtex_key: du2026focusabledepth
title: Focusable Monocular Depth Estimation
year: 2026
domain_theme: Estimasi Kedalaman
verified_pdf: 202_Focusable Monocular Depth Estimation.pdf
char_count: 94446
---

Focusable Monocular Depth Estimation

                                             Yuxin Du1,2,* , Tao Lin1,* , Zile Zhong1 , Runting Li1 , Xiyao Chen1 , Jiting Liu1 , Chenglin Liu2 ,
                                                                     Ying-Cong Chen2 , Yuqian Fu3 , and Bo Zhao1,+
                                                                1
                                                                 School of Artificial Intelligence, Shanghai Jiao Tong University
                                                           2
                                                               The Hong Kong University of Science and Technology (Guangzhou)
                                                                    3
                                                                      King Abdullah University of Science and Technology
arXiv:2605.11756v1 [cs.CV] 12 May 2026

                                                                        *
                                                                          These authors contributed equally to this work.
                                                                     +
                                                                       Corresponding author. Email: bo.zhao@sjtu.edu.cn

                                                                                          Abstract

                                                     Monocular depth foundation models generalize well across scenes, yet they are
                                                     typically optimized with uniform pixel-wise objectives that do not distinguish
                                                     user-specified or task-relevant target regions from the surrounding context. We
                                                     therefore introduce Focusable Monocular Depth Estimation (FDE), a region-aware
                                                     depth estimation task in which, given a specified target region, the model is re-
                                                     quired to prioritize foreground depth accuracy, preserve sharp boundary transitions,
                                                     and maintain coherent global scene geometry. To prioritize task-critical region
                                                     modeling, we propose FocusDepth, a prompt-conditioned monocular relative
                                                     depth estimation framework that guides depth modeling to focus on target regions
                                                     via box/text prompts. The core Multi-Scale Spatial-Aligned Fusion (MSSA) in
                                                     FocusDepth spatially aligns multi-scale features from Segment Anything Model
                                                     3 to the Depth Anything family and injects them through scale-specific, gated
                                                     conditional fusion. This enables dense prompt cue injection without disrupting
                                                     geometric representations, thereby endowing the depth estimation model with
                                                     focused perception capability. To study FDE, we establish FDE-Bench, a target-
                                                     centric monocular relative depth benchmark built from image–target–depth triplets
                                                     across five datasets, containing 252.9K/72.5K train/val triplets and 972 categories
                                                     spanning real-world and embodied simulation environments. On FDE-Bench, Fo-
                                                     cusDepth consistently improves over globally fine-tuned DA2/DA3 baselines under
                                                     both box and text prompts, with the largest gains appearing in target boundary and
                                                     foreground regions while preserving global scene geometry. Ablations show that
                                                     MSSA’s spatial alignment is the key design factor, as disrupting prompt–geometry
                                                     correspondence increases AbsRel by up to 13.8%.

                                         1    Introduction
                                         Monocular depth estimation [21, 2, 1] aims to recover dense scene geometry from a single RGB
                                         image and serves as a fundamental visual capability in many vision systems, including robotics,
                                         embodied AI, and augmented reality. The field has been extensively studied under supervised
                                         and self-supervised learning paradigms [38, 7–9], with later work improving robustness through
                                         cross-dataset training, stronger architectures, and generative priors [25, 39, 37, 14, 10, 36]. More
                                         recently, depth foundation models such as Depth Anything [33, 34, 16], UniDepth [23, 24], and
                                         Metric3D [35, 11] have substantially advanced cross-domain generalization by leveraging large-scale
                                         and diverse training data. Despite this progress, monocular depth estimation remains predominantly
                                         image-centric: models are typically trained and evaluated by aggregating errors over all pixels in the
                                         image. This uniform, image-wide treatment contrasts with task-driven spatial perception: humans

                                         Preprint.
                                                       DE                              DE
                          Input: Image Only
                                                Estimation Result                 Abs Error Map
           Standard                                                                            Error
                                                        Blurry
          Monocular                                                                      Low           High

                                                      Boundaries
            Depth                                                    Inaccurate
          Estimation                                                 Foreground

              (DE)

                                                                                               Error
                                                          Clear
                                                                                        Low            High
                                                        Boundaries
           Focusable
          Monocular                                                   Accurate
             Depth                                                   Foreground

          Estimation
                       'the beverage'
             (FDE)
                                                      FDE                              FDE
                        Input: Image + Target
                                                Estimation Result                 Abs Error Map

Figure 1: Illustration of the proposed Focusable Depth Estimation (FDE). Given an image and a
user-specified target, FDE prioritizes foreground and boundary depth quality while preserving global
scene geometry. Compared with standard monocular depth estimation (DE), FDE requires the model
to yield sharper target boundaries and lower depth error in the specified target region.

selectively attend to goal-relevant foreground objects while retaining only contextual awareness of the
background. This mismatch is also relevant to target-centric perception, with robot manipulation as
one motivating example [3, 12, 18, 19, 29, 28], where depth near the target surface and discontinuities
may be important but are not evaluated as downstream task performance here. As a result, strong
full-image depth performance does not necessarily imply reliable target-local geometry under region-
aware evaluation. Prior task-aware depth estimation has similarly observed that foreground objects
can be underweighted by uniform image-wide objectives in downstream 3D perception [30].
To address this formulation gap, we introduce Focusable Depth Estimation (FDE), a short version of
Focusable Monocular Depth Estimation for convenience, which extends monocular depth estimation
from uniform dense prediction to target-conditioned depth inference. As illustrated in Figure 1, given
an image and a user-specified target region, FDE prioritizes target-foreground accuracy and boundary
fidelity while preserving coherent global scene geometry.
To study FDE, we propose FocusDepth, a prompt-conditioned monocular relative depth estimation
framework designed to balance local target sensitivity with global geometric coherence. Our key
intuition is to combine the complementary priors of promptable segmentation and monocular depth
foundation models: Segment Anything Model 3 (SAM3) [4] provides prompt-grounded spatial
selectivity for identifying user-specified target regions, while the Depth Anything family (DAs),
such as DA2 [34] and DA3 [16], provides a strong pretrained prior over dense scene geometry.
However, directly fusing these models is nontrivial, as SAM3 is optimized for 2D prompt-driven
localization whereas DAs are optimized for globally coherent 3D geometry. FocusDepth, therefore,
treats target-aware refinement as a controlled injection problem rather than simple feature fusion. We
introduce MSSA (Multi-Scale Spatial-Aligned Fusion), which injects prompt-conditioned cues into
DAs geometry tokens through spatially aligned token-level fusion, adapts them across depth feature
scales, and uses gated conditional fusion to control prompt-conditioned corrections. This design
encourages target-relevant regions, including foreground and boundary areas, to receive focused
refinement while preserving DAs’ full-scene geometric prior.
To make FDE measurable, we further establish FDE-Bench, a benchmark suite and evaluation proto-
col that reformulates existing depth datasets into image–target–depth triplets. Unlike conventional
depth benchmarks that primarily report full-image error, FDE-Bench evaluates whether a method
improves target-local geometry through three complementary regions: the specified foreground, the
target boundary, and the full scene as a coherence constraint. The benchmark covers diverse RGB-D
sources, including indoor scenes, tabletop object data, and simulated embodied-scene observations
from NYU v2 [26], TUM RGB-D [27], YCB-Video [32], RLBench [13], and RoboTwin [22], con-
taining 252.9K/72.5K train/val triplets. This protocol enables systematic comparison of standard
monocular depth models and prompt-conditioned methods under target-centric criteria, assessing
foreground accuracy, boundary fidelity, and global geometric consistency.

                                                    2
Our contributions are threefold:

       • We introduce Focusable Depth Estimation (FDE), a target-centric formulation of monocular
         depth estimation that prioritizes foreground accuracy and boundary fidelity for a user-
         specified region while preserving coherent global scene geometry.
       • We propose FocusDepth, a prompt-conditioned monocular relative depth estimation frame-
         work that transfers prompt-grounded target evidence from SAM3 into DAs’ dense geometry
         representation via MSSA, enabling spatially aligned, scale-dependent, and gated conditional
         depth refinement.
       • We establish FDE-Bench, a benchmark suite and evaluation protocol that converts existing
         depth datasets into image–target–depth triplets and demonstrates that FocusDepth improves
         target-region accuracy and boundary fidelity while maintaining full-image geometric coher-
         ence.

2     Related Work

Monocular depth estimation and depth foundation models. Monocular depth estimation has
evolved from supervised and self-supervised pipelines to more transferable architectures trained
across diverse datasets [7–9, 25, 39, 37]. These developments have progressively improved depth
accuracy, cross-domain robustness, and dense geometric reasoning, laying the groundwork for recent
depth foundation models. Current leading models include UniDepth [23] and UniDepthV2 [24],
Metric3D [35] and Metric3Dv2 [11], and the Depth Anything family [33, 34, 16]. By leveraging
large-scale training data, metric supervision, synthetic data, or auto-annotated depth, these models
achieve strong zero-shot generalization and robust whole-image depth prediction across diverse scenes.
However, they are still primarily formulated and evaluated at the image level, where objectives and
metrics aggregate errors over the full image plane.

Task-aware and conditioned depth estimation. FDE is related to task-aware, semantic-guided,
and conditioned depth formulations, but differs in how the condition is specified and what depth
quality is prioritized. ForeSeE separates foreground and background depth prediction for 3D object
detection, showing that uniform objectives can underweight task-critical foreground objects [30];
however, it targets category- and task-specific foregrounds rather than arbitrary user-specified regions.
BriGeS fuses depth and segmentation foundation models to improve generalized monocular depth
estimation in complex scenes [20], whereas FocusDepth uses prompt-grounded SAM3 cues for
region-prioritized refinement instead of global image-level enhancement. Other conditioned or object-
centric methods either rely on additional geometric inputs, such as sparse LiDAR prompts [17] or
external geometric priors [31], or focus on object-level/amodal 3D understanding [15, 5]. In contrast,
FDE uses a box or text prompt to specify the visible target region whose foreground accuracy and
boundary fidelity should be improved while preserving full-scene geometric coherence.

3     Method

3.1   Problem Formulation

Given an input image I ∈ RH×W ×3 and an interactive prompt p, FocusDepth aims to predict a
dense depth map that improves depth quality in the specified foreground region while preserving
coherent scene geometry over the full image. Following Section 4, we consider two prompt types:
box prompts and text prompts that specify the target object or region. The model is formulated as
follows: D̂, M̂ = F(I, p), where D̂ ∈ RH×W is the predicted depth map and M̂ ∈ [0, 1]H×W is an
auxiliary prompt-conditioned predicted foreground mask.
The objective of focusable depth estimation is spatially heterogeneous. The foreground region should
be estimated more accurately, the boundary region around the target should preserve sharper depth
transitions, and the global region should remain geometrically coherent. FocusDepth addresses this
objective with prompt-conditioned feature fusion and region-aware supervision.

                                                   3
        Box or Text Prompt                             Prompt-Conditioned Branch (SAM )                    Prediction                       Loss Functions
                                                                                                           Auxiliary Pred.         Mask Loss
                                            Prompt
                                            Encoder
                                                                                                                                                               Segmentation GT

                                                       Prompt-Guided                        Segmentation
                                                        Transformer                           Decoder                              Boundary Loss
                                             Image
                                            Encoder

          "the middle beverage"                                   Prompt-Conditioned
                                                                       Tokens                                Focusable
                                                                                                            Depth Pred.            Foreground Loss                    Depth GT

            Input Image                 Geometry Depth Branch (DAs)                     Fusion
                                                                                       MSSA Fusion
                                                                       Scale                                                       Global Loss

                                                                       Scale           MSSA Fusion
                                           Depth
                                          Encoder
                                                                       Scale           MSSA Fusion
                                                                                                                                                   Total Loss
                                                                       Scale                                   Depth
                                                                                       MSSA Fusion
                                                                                                              Decoder
                                                      Geometry Tokens

                                                                                                                                   Learnable Gate Weights
      Prompt-Conditioned                 Projected Prompt-
                                                                 MSSA: Multi-Scale Spatial-Aligned Fusion
                                                                  Router Weights                                                      0.1 0.7 0.3            ...
           Tokens                       Conditioned Tokens
                                                                                                                                      0.6 0.2 0.8            ...
                             Linear
                                                                                                                                      ...    ...       ...
                           Projection                                                       Expert
                                                                                                                                            Gated Sum
                                          Spatial-Aligned
                                                             C
                                                                                              ...                            ∑                     G
                                             Concatenate
                                                                       Expert
                                                                       Router               Expert N                    Weighted
                                                                                                                                                                   Prompt-conditioned
                                                                                                                         Sum
                                                                                                                                                                    Geometry Tokens

       Geometry Tokens
                                                                                                           Residual Geometry Tokens

         ① Feature Projection                   ② Spatial Alignment                         ③ Routed Conditional Fusion                        ④ Gated Fusion

Figure 2: Overall framework of FocusDepth. The geometry depth branch extracts multi-scale
geometry tokens, the prompt-conditioned branch produces prompt-conditioned tokens, and MSSA
spatially aligns and injects target-aware cues into geometry representations for focusable depth
prediction. The model is trained with foreground, boundary, and global depth losses, together with
auxiliary segmentation supervision.

3.2   Overall Framework

Figure 2 illustrates the overall framework of FocusDepth. FocusDepth is built upon the Depth
Anything family (DAs) as the geometry depth branch, including DA2 [34] and DA3 [16], due to
their strong zero-shot generalization and robust monocular geometric priors learned from large-scale
depth data. SAM3 [4] is incorporated as the prompt-conditioned branch for target-aware region
specification. The geometry depth branch extracts multi-scale geometry features, while the prompt-
conditioned branch produces a prompt-conditioned token feature from the input image and prompt.
The core module, MSSA, spatially aligns and fuses the prompt-conditioned tokens into each scale of
geometry tokens for target-aware depth refinement.
Given an input image I, the geometry depth branch extracts a hierarchy of encoder features X g =
{Xsg }Ss=1 , Xsg ∈ RN ×Cg , where s indexes the feature scale. We use S = 4 geometry to match the
encoder scales. The prompt-conditioned branch takes the image and prompt p as input and produces
a prompt-conditioned token feature X p ∈ RN ×Cp . The two branches share the same token count N
because they process the same image over an identical patch grid of ViT [6]. FocusDepth applies
MSSA at each geometry scale: Y = MSSA(X g , X p ), where each scale has independent fusion
parameters. The fused features Y = {Ys }Ss=1 are passed to the depth decoder to predict D̂. An
auxiliary segmentation decoder on the prompt-conditioned branch predicts M̂ during both training
and inference.

3.3   Multi-Scale Spatial-Aligned Fusion

MSSA is the central target-aware fusion module in FocusDepth. It injects prompt-conditioned cues
into geometry tokens in a spatially adaptive manner while preserving the pretrained geometry prior.
MSSA is applied independently at each geometry encoder scale.

Scale-wise spatial alignment. Under the shared setting of input image size 1008 and patch size
14 of ViT [6], the geometry depth branch and the prompt-conditioned branch produce image tokens
on the same regular patch grid. Thus, their tokens are in one-to-one spatial correspondence. At

                                                                                        4
scale s, the geometry depth branch provides geometry tokens Xsg ∈ RN ×Cg , while the prompt-
conditioned branch provides the prompt-conditioned tokens X p ∈ RN ×Cp . We project X p into the
scale-specific geometry-token space: X̃sp = X p Wsp , where Wsp ∈ RCp ×Cg is a learnable projection.
The projected prompt-conditioned tokens and geometry tokens are then concatenated token-wise:
Zs = [Xsg ∥ X̃sp ] ∈ RN ×2Cg . This spatial-aligned concatenation allows prompt-conditioned target
cues to guide refinement at the corresponding spatial locations at each geometry scale.

Routed conditional fusion. Different image locations can require different prompt-conditioned
corrections. To provide conditional fusion capacity, MSSA applies a lightweight MoE layer to the
fused tokens Zs : Fs = MoEs (Zs ) ∈ RN ×Cg . We use E = 4 experts at each scale. The router
computes input-dependent combinations of expert outputs and is used as a flexible fusion module,
not as an explicitly supervised decomposition into foreground, boundary, or background experts.

Gated fusion output. To avoid overwriting the geometry-token representation, MSSA combines
the routed feature with the original geometry tokens through a learnable gate: Gs = σ(Fs Wsg ),
where Wsg ∈ RCg ×1 and σ(·) denotes the Sigmoid function. The output feature is Ys = Gs ⊙ Fs +
(1 − Gs ) ⊙ Xsg . This gated formulation injects prompt-conditioned corrections selectively while
retaining the pretrained geometry prior.

3.4    Learning Objective

We use the foreground, boundary, and global region partition from FDE-Bench. For each training
triplet, we follow the notation in Section 4: D is the ground-truth depth, M is the foreground mask,
V is the valid-depth mask, and Vfg , Vbd , and Vglb denote the valid foreground, boundary, and global
regions.
In the relative depth setting, we align the prediction to the ground truth by solving a per-image scale
a and shift b over valid pixels: D̃ = aD̂ + b. Regional depth supervision is then computed as

    Lfg = Ldepth (D̃, D; Vfg ),   Lbd = Ldepth (D̃, D; Vbd ),       Lglb = Ldepth (D̃, D; Vglb ), (1)
where Ldepth combines masked MSE and gradient losses within the specified region. For DA2 [34],
we apply a disparity-space processing step before computing the loss. The auxiliary mask prediction
is supervised by Lseg = LBCE (M̂ , M ) + LDice (M̂ , M ). The final objective is L = Lglb + Lfg +
Lbd + Lseg . All terms are equally weighted because each loss is normalized within its valid region.

3.5    Two-Stage Training Strategy

To stabilize adaptation between the pretrained geometry and prompt-conditioned components, we
train FocusDepth in two stages. In Stage 1, only MSSA is optimized, while all pretrained modules
are frozen. This lets MSSA learn to align geometry tokens with prompt-conditioned tokens without
disturbing the pretrained backbones. In Stage 2, we keep the depth encoder, the SAM3 image
encoder, and the SAM3 prompt encoder frozen, and optimize MSSA, the depth decoder, the SAM3
prompt-guided transformer, and the auxiliary segmentation decoder. This separates cross-model
alignment from downstream FDE adaptation and improves training stability.

4     Proposed FDE-Bench

4.1    Benchmark Construction

Existing monocular depth benchmarks are primarily image-centric: they evaluate depth quality over
the whole image, but do not directly test whether a model can prioritize a user-specified target while
preserving coherent geometry elsewhere. This mismatch is limiting for Focusable Depth Estimation
(FDE), where the goal is to improve depth on the target region, preserve sharp depth transitions
around it, and maintain globally consistent scene geometry. To make this setting operational, we
establish FDE-Bench, a target-centric benchmark suite organized around the image–target–depth
triplet. Each triplet contains an RGB image, one target region, and the corresponding ground-truth
depth map. A source image may yield multiple triplets, but each triplet is associated with exactly

                                                  5
one target region, which is defined as the foreground region for evaluation. Targets may be specified
through box prompts and, when available, text prompts.
FDE-Bench is constructed from heterogeneous RGB-D datasets by converting each retained target
region into a standardized triplet. When source instance or semantic masks are available, annotated
regions are filtered by area; otherwise, pseudo masks are generated using SAM automatic mask
generation and filtered with the same protocol, with pseudo-mask entries explicitly marked in the
metadata. Each retained mask defines the foreground region, its tight bounding box defines the
box prompt, and its semantic class name, when available, defines the text prompt. We instantiate
FDE-Bench on five adapted datasets: NYU v2 [26], RLBench [13], b [32], TUM RGB-D [27], and
RoboTwin [22], covering indoor clutter, object-centric tabletop scenes, and embodied manipulation
environments across real and simulated data. All entries derived from the same image or sequence
are assigned to the same split to prevent data leakage. As illustrated in Appendix Table 4, FDE-
Bench contains 20.5K/8.2K train/val images and 252.9K/72.5K train/val triplets, covering 972 target
categories with semantic labels. Box-prompt evaluation is available across all five datasets, while
text-prompt supervision is available on NYU v2, RLBench, and YCB-Video.

4.2   Region-aware Evaluation Metrics

FDE-Bench uses region-aware evaluation metrics aligned with the FDE objective. For each triplet,
we evaluate three spatial regions: the foreground region, the boundary region, and the global region,
respectively measuring target-local depth quality, depth-transition sharpness, and whole-image
geometric consistency. Formally, let D ∈ RH×W , M ∈ {0, 1}H×W , V ∈ {0, 1}H×W denote the
ground-truth depth map, the target-region mask, and the valid-depth mask. We construct a boundary
band B around M with radius r = 10 pixels, given by the ring induced by morphological dilation
and erosion. The valid foreground, boundary, and global regions are defined as Vfg = V ∩ M, Vbd =
V ∩ B, Vglb = V.
For each region, we report δ1 and AbsRel. Region metrics are computed in a per-target manner,
which prevents images with many valid targets from dominating the final benchmark score. For
relative-depth evaluation, scale-shift alignment is applied over the whole image before regional
metrics are computed for coherent scene geometry alignment. More details of FDE-Bench, including
dataset-specific construction rules, split protocols, prompt formats, representative visualizations, and
additional statistics, are provided in Appendix A.1.

5     Experiments

5.1   Experimental Setup

We evaluate FocusDepth(DA2) and FocusDepth(DA3) on FDE-Bench using the dataset scope, prompt
settings, and region-aware evaluation metrics defined in Section 4. The framework design, region-
aware learning objective, and training strategy follow Section 3. Unless otherwise specified, all
experiments are conducted on 4 NVIDIA A100 80GB GPUs. We next describe the comparison
settings and report quantitative and qualitative results. To establish a baseline for the FDE capability
of current representative monocular depth foundation models, we evaluate UniDepth-v1, UniDepth-
v2, Metric3D-v2, Depth Anything 2 (DA2), and Depth Anything 3 (DA3) in the zero-shot setting.
We further report the fine-tuning results of DA2 and DA3, and compare them with FocusDepth under
the same training resources, data, and hyperparameter settings, detailed in Appendix Table 5 and
Appendix Table 6.

5.2   Main Results

Table 1 and Table 2 report the main box-prompt and text-prompt comparison on NYU v2, RLBench,
RoboTwin, and YCB-Video. Appendix Table 7 provides the remaining box-prompt results on TUM
RGB-D and YCB-Video. Following the per-target evaluation protocol in FDE-Bench, we first
compute metrics for each image–target–depth triplet and then report the median over target-level
metrics, with Q25/Q75 shown for δ1 . Across all tables, higher δ1 and lower AbsRel indicate better
performance.

                                                   6
Table 1: Box-prompt results on RLBench, RoboTwin, and NYU v2. We compare zero-shot depth
foundation models, fine-tuned DA2/DA3 baselines, and FocusDepth variants across boundary, fore-
ground, and global regions.
      Dataset         Method                  Boundary region                 Foreground region                    Global region
                                               δ1 ↑           AbsRel ↓          δ1 ↑            AbsRel ↓          δ1 ↑            AbsRel ↓
                      UniDepth-v1 [23] 0.597 (0.386, 0.800)    0.247     0.542 (0.008, 0.997)    0.234     0.665 (0.574, 0.820)    0.214
                      UniDepth-v2 [24] 0.871 (0.572, 0.996)    0.123     0.997 (0.355, 1.000)    0.127     0.921 (0.686, 0.958)    0.097
                      Metric3D-v2 [11] 0.707 (0.470, 0.894)    0.185     0.727 (0.081, 1.000)    0.198     0.815 (0.644, 0.903)    0.165
                      DA2 [34]        0.922 (0.680, 0.996)     0.106     0.996 (0.694, 1.000)    0.097     0.917 (0.726, 0.957)    0.106
      RLBench [13]
                      DA2-ft          0.982 (0.889, 1.000)     0.069     1.000 (0.949, 1.000)    0.066     0.964 (0.953, 0.990)    0.054
                      FocusDepth(DA2) 0.996 (0.960, 1.000)     0.054     1.000 (0.991, 1.000)    0.050     0.992 (0.979, 0.998)    0.045
                      DA3 [16]        0.790 (0.488, 0.985)     0.148     0.944 (0.103, 1.000)    0.147     0.889 (0.648, 0.954)    0.134
                      DA3-ft          0.975 (0.804, 1.000)     0.073     1.000 (0.709, 1.000)    0.095     0.983 (0.921, 0.997)    0.042
                      FocusDepth(DA3) 0.996 (0.949, 1.000)     0.049     1.000 (0.977, 1.000)    0.056     0.996 (0.974, 0.999)    0.030
                      UniDepth-v1 [23] 0.751 (0.502, 0.929)    0.190     0.840 (0.287, 0.995)    0.151     0.930 (0.812, 0.975)    0.102
                      UniDepth-v2 [24] 0.919 (0.689, 0.987)    0.100     0.997 (0.804, 1.000)    0.073     0.983 (0.957, 0.993)    0.056
                      Metric3D-v2 [11] 0.905 (0.703, 0.979)    0.101     0.988 (0.653, 1.000)    0.081     0.983 (0.959, 0.992)    0.051
                      DA2 [34]        0.954 (0.571, 0.991)     0.095     0.993 (0.604, 1.000)    0.082     0.984 (0.849, 0.997)    0.062
      RoboTwin [22]
                      DA2-ft          0.957 (0.680, 0.995)     0.086     0.987 (0.679, 1.000)    0.084     0.989 (0.864, 0.997)    0.053
                      FocusDepth(DA2) 0.976 (0.735, 0.998)     0.070     0.995 (0.878, 1.000)    0.065     0.994 (0.880, 0.999)    0.047
                      DA3 [16]        0.889 (0.565, 0.987)     0.119     0.973 (0.339, 1.000)    0.115     0.962 (0.842, 0.989)    0.077
                      DA3-ft          0.949 (0.772, 0.995)     0.082     0.992 (0.793, 1.000)    0.075     0.985 (0.960, 0.997)    0.037
                      FocusDepth(DA3) 0.979 (0.903, 0.998)     0.058     0.998 (0.955, 1.000)    0.055     0.995 (0.977, 0.999)    0.029
                      UniDepth-v1 [23] 1.000 (0.960, 1.000)    0.054     1.000 (0.995, 1.000)    0.045     0.973 (0.945, 0.987)    0.056
                      UniDepth-v2 [24] 0.998 (0.948, 1.000)    0.047     1.000 (0.993, 1.000)    0.037     0.977 (0.949, 0.990)    0.046
                      Metric3D-v2 [11] 0.996 (0.916, 1.000)    0.059     1.000 (0.979, 1.000)    0.051     0.974 (0.928, 0.990)    0.059
                      DA2 [34]        0.998 (0.946, 1.000)     0.058     1.000 (0.991, 1.000)    0.049     0.975 (0.941, 0.991)    0.057
      NYU v2 [26]
                      DA2-ft          1.000 (0.971, 1.000)     0.058     1.000 (0.997, 1.000)    0.051     0.979 (0.938, 0.995)    0.061
                      FocusDepth(DA2) 1.000 (0.976, 1.000)     0.055     1.000 (0.998, 1.000)    0.048     0.979 (0.941, 0.995)    0.059
                      DA3 [16]        0.970 (0.869, 1.000)     0.074     1.000 (0.986, 1.000)    0.055     0.927 (0.857, 0.956)    0.091
                      DA3-ft          1.000 (0.972, 1.000)     0.051     1.000 (0.997, 1.000)    0.046     0.977 (0.937, 0.993)    0.053
                      FocusDepth(DA3) 1.000 (0.977, 1.000)     0.049     1.000 (0.998, 1.000)    0.044     0.978 (0.939, 0.995)    0.053

Zero-shot baselines. Table 1 shows that current monocular depth foundation models already
provide strong whole-image geometry in several settings, but their target-centric behavior is not
consistently aligned with FDE. On NYU v2, zero-shot baselines are close to saturation in δ1 ,
making differences mainly visible through AbsRel and lower-quartile statistics. On RLBench and
RoboTwin, however, the gap between global performance and target-relevant boundary or foreground
performance becomes more apparent. This suggests that strong image-centric depth estimation does
not by itself ensure reliable focusable depth estimation on manipulation-oriented and object-centric
scenes.

FocusDepth gains. Compared with the corresponding globally fine-tuned DA variants, FocusDepth
more consistently improves the prompted target regions while preserving global geometry. The
clearest gains appear on RLBench: under box prompts, FocusDepth(DA3) reduces boundary AbsRel
from 0.073 to 0.049, foreground AbsRel from 0.095 to 0.056, and global AbsRel from 0.042 to
0.030 relative to DA3-ft. RoboTwin shows the same pattern, with FocusDepth(DA3) improving
boundary, foreground, and global AbsRel over DA3-ft from 0.082/0.075/0.037 to 0.058/0.055/0.029.
FocusDepth(DA3) mainly improves the boundary and foreground regions over DA3-ft on NYU v2,
while matching DA3-ft in global AbsRel at 0.053, indicating that its target-region refinement does
not compromise global geometric coherence. FocusDepth(DA2) follows a similar trend over DA2-ft,
indicating that the benefit is not tied to a single backbone. The text-prompt comparison in Table 2
shows consistent gains on RLBench, NYU v2, and YCB-Video. The appendix results further support
this conclusion: the remaining box-prompt results in Table 7 show clear improvements on TUM RGB-
D and YCB-Video. Overall, these results support the FocusDepth objective: prompt-conditioned
refinement most reliably improves local target regions, with limited global-geometry trade-off in
most evaluated settings.

5.3   RLBench Prompt-Correctness Study

We conduct this study to examine the sensitivity of FocusDepth(DA3) to prompt correctness in the
FDE task. The evaluation includes a correct target prompt, a wrong prompt referring to another
visible object, a wrong prompt referring to an absent object, and an empty prompt. Unlike the main
comparison, which reports medians, this study reports means to better expose the aggregate effect of

                                                                    7
Table 2: Text-prompt results on RLBench, NYU v2, and YCB-Video. We compare zero-shot
depth foundation models, fine-tuned DA2/DA3 baselines, and FocusDepth variants across boundary,
foreground, and global regions.
         Dataset            Method                    Boundary region                  Foreground region                      Global region
                                                       δ1 ↑            AbsRel ↓          δ1 ↑             AbsRel ↓            δ1 ↑            AbsRel ↓
                            UniDepth-v1 [23] 0.601 (0.423, 0.775)       0.247     0.577 (0.148, 0.958)     0.224     0.666 (0.575, 0.822)      0.212
                            UniDepth-v2 [24] 0.859 (0.579, 0.990)       0.121     0.991 (0.454, 1.000)     0.117     0.925 (0.695, 0.958)      0.093
                            Metric3D-v2 [11] 0.716 (0.486, 0.870)       0.183     0.753 (0.271, 0.998)     0.185     0.817 (0.648, 0.905)      0.163
                            DA2 [34]        0.895 (0.691, 0.992)        0.110     0.989 (0.781, 1.000)     0.090     0.921 (0.728, 0.957)      0.103
         RLBench [13]
                            DA2-ft          0.976 (0.888, 0.999)        0.069     0.999 (0.949, 1.000)     0.061     0.964 (0.953, 0.991)      0.054
                            FocusDepth(DA2) 0.994 (0.961, 1.000)        0.053     1.000 (0.988, 1.000)     0.046     0.993 (0.980, 0.998)      0.044
                            DA3 [16]        0.795 (0.507, 0.971)        0.145     0.910 (0.294, 1.000)     0.139     0.893 (0.655, 0.955)      0.129
                            DA3-ft          0.973 (0.824, 0.999)        0.068     0.998 (0.772, 1.000)     0.088     0.984 (0.923, 0.997)      0.041
                            FocusDepth(DA3) 0.995 (0.959, 1.000)        0.045     1.000 (0.977, 1.000)     0.050     0.996 (0.978, 0.999)      0.029
                            UniDepth-v1 [23] 0.998 (0.952, 1.000)       0.054     1.000 (0.991, 1.000)     0.046     0.973 (0.945, 0.987)      0.056
                            UniDepth-v2 [24] 0.994 (0.943, 1.000)       0.048     1.000 (0.989, 1.000)     0.038     0.977 (0.949, 0.990)      0.046
                            Metric3D-v2 [11] 0.990 (0.912, 1.000)       0.060     1.000 (0.970, 1.000)     0.052     0.974 (0.928, 0.990)      0.059
                            DA2 [34]        0.995 (0.939, 1.000)        0.059     1.000 (0.986, 1.000)     0.050     0.975 (0.941, 0.991)      0.057
         NYU v2 [26]
                            DA2-ft          1.000 (0.960, 1.000)        0.059     1.000 (0.993, 1.000)     0.052     0.979 (0.938, 0.995)      0.061
                            FocusDepth(DA2) 1.000 (0.963, 1.000)        0.057     1.000 (0.995, 1.000)     0.049     0.979 (0.940, 0.995)      0.060
                            DA3 [16]        0.959 (0.865, 1.000)        0.077     1.000 (0.979, 1.000)     0.057     0.927 (0.857, 0.956)      0.091
                            DA3-ft          1.000 (0.961, 1.000)        0.052     1.000 (0.992, 1.000)     0.047     0.977 (0.937, 0.993)      0.053
                            FocusDepth(DA3) 1.000 (0.967, 1.000)        0.050     1.000 (0.995, 1.000)     0.044     0.978 (0.938, 0.995)      0.054
                        UniDepth-v1 [23]        1.000 (0.985, 1.000)    0.041     1.000 (0.997, 1.000)     0.037     0.993 (0.981, 0.997)      0.045
                        UniDepth-v2 [24]        0.997 (0.966, 1.000)    0.036     1.000 (0.994, 1.000)     0.026     0.996 (0.991, 0.998)      0.031
                        Metric3D-v2 [11]        1.000 (0.986, 1.000)    0.041     1.000 (0.998, 1.000)     0.031     0.997 (0.988, 0.999)      0.042
         YCB-Video [32] DA2 [34]                0.998 (0.963, 1.000)    0.045     1.000 (0.993, 1.000)     0.037     0.994 (0.972, 0.998)      0.040
                            DA3 [16]        0.993 (0.938, 1.000)        0.053     0.999 (0.986, 1.000)     0.044     0.992 (0.961, 0.997)      0.047
                            DA3-ft          1.000 (0.988, 1.000)        0.042     1.000 (0.999, 1.000)     0.035     0.997 (0.984, 0.999)      0.044
                            FocusDepth(DA3) 1.000 (0.990, 1.000)        0.034     1.000 (0.999, 1.000)     0.024     0.998 (0.993, 0.999)      0.032

bad cases under prompt perturbations; the corresponding mean–median comparison is provided in
Appendix Table 8.
As shown in Figure 3, correct prompts produce the strongest target-centric response and the best
boundary and foreground results. Degraded prompts mainly reduce local target-region gains, with
smaller effects on global geometry. Notably, even wrong or empty prompts remain stronger than the
DA3-ft no-prompt baseline across boundary, foreground, and global regions. This suggests that, after
removing the benefit of correct prompt guidance, the prompt-conditioned branch still provides useful
local and global depth cues.

       (a) Prompt-conditioned attention visualization.                                   (b) Quantitative prompt-correctness study
                                                                                                     with mean values.
                   Correct prompt    Wrong prompt     Wrong prompt
      Image         (robot arm)       (table mat)       (banana)        Empty prompt
                                                                                          Prompt Setting Boundary region Foreground region     Global region
                                                                                                          δ1 ↑ AbsRel ↓ δ1 ↑       AbsRel ↓   δ1 ↑ AbsRel ↓
                                                                                          Correct         0.919    0.108   0.901     0.137    0.943    0.075
                                                                                          Wrong visible   0.914    0.111   0.884     0.148    0.943    0.074
                                                                                          Wrong absent    0.911    0.117   0.886     0.152    0.939    0.078
                                                                                          Empty           0.910    0.118   0.886     0.154    0.939    0.078
                                                                                          DA3-ft          0.860    0.162   0.804     0.226    0.915    0.105

Figure 3: RLBench prompt-correctness study for FocusDepth(DA3) under class-specific text prompts.
(a) Prompt-conditioned attention visualization under correct, wrong-visible, absent, and empty
prompts. (b) Quantitative results reported as means; the corresponding mean–median comparison is
provided in Appendix Table 8. Best results are shown in bold.

5.4      Ablation Studies

We ablate FocusDepth(DA3) on RLBench to examine how each design contributes to target-
conditioned dense refinement. Table 3 reports median AbsRel under box and text prompts across
boundary, foreground, and global regions. The results show a clear hierarchy: spatial alignment is
most critical, scale-specific fusion and routed conditional fusion contribute to MSSA capacity, and
gated injection, region-aware loss, and two-stage training stabilize the local-global trade-off.
The MSSA ablations identify spatial alignment as the dominant factor. Shuffling the correspondence
between prompt-conditioned tokens and geometry tokens causes the largest degradation, increasing
text-prompt global AbsRel by 13.8%. Removing scale-specific fusion or replacing routed conditional

                                                                            8
Table 3: Ablation study of FocusDepth(DA3) on RLBench. We report median AbsRel; lower is better.
Colored values in parentheses denote changes relative to the full model.
 Method                                                          Box prompt                                          Text prompt
                                                 Boundary        Foreground          Global          Boundary        Foreground         Global
 Full model (FocusDepth)                            0.049            0.056             0.030            0.045            0.050            0.029
 w/o spatial alignment (shuffled tokens)       0.054 (+10.2%)   0.062 (+10.7%)    0.033 (+10.0%)   0.050 (+11.1%)   0.056 (+12.0%)   0.033 (+13.8%)
 w/o scale-specific fusion                     0.052 (+6.1%)    0.060 (+7.1%)     0.032 (+6.7%)     0.048 (+6.7%)   0.055 (+10.0%)   0.031 (+6.9%)
 w/o routed fusion (single MLP)                0.052 (+6.1%)    0.061 (+8.9%)     0.032 (+6.7%)     0.048 (+6.7%)   0.055 (+10.0%)   0.031 (+6.9%)
 w/o gated injection                           0.050 (+2.0%)    0.059 (+5.4%)     0.031 (+3.3%)    0.047 (+4.4%)     0.051 (+2.0%)   0.031 (+6.9%)
 global loss only                              0.049 (+0.0%)    0.062 (+10.7%)     0.028 (-6.7%)    0.045 (+0.0%)   0.056 (+12.0%)    0.028 (-3.4%)
 one-stage training                            0.050 (+2.0%)    0.059 (+5.4%)     0.030 (+0.0%)    0.046 (+2.2%)     0.053 (+6.0%)   0.029 (+0.0%)

fusion with a single MLP also consistently worsens foreground and boundary AbsRel; for example,
both variants increase text-prompt foreground AbsRel by 10.0%, indicating that MSSA benefits
from scale-aware and conditional fusion capacity for target-conditioned refinement. Removing gated
injection leads to smaller but consistent degradation, such as increasing box-prompt foreground
AbsRel by 5.4%, supporting its role in stabilizing prompt-conditioned corrections while preserving
the pretrained geometry prior.
The optimization ablations clarify the local-global trade-off. The global-loss-only variant improves
global AbsRel but substantially worsens foreground AbsRel, e.g., by 10.7% under box prompts and
12.0% under text prompts, showing that image-centric supervision can sacrifice the prompted target
region. One-stage training also weakens local refinement, indicating that cross-model alignment and
downstream FDE adaptation benefit from being separated. Together, these results support MSSA as a
spatially aligned, multi-scale, and conditional injection mechanism, and validate the region-aware
objective and two-stage training strategy.

                                    RoboTwin        RLBench            NYU v            TUM RGB-D           YCB-Video Error
                                                                                                                              High
                           Image
                           DA -ft
                FocusDepth
                   (DA )

                                                                                                                              Low

Figure 4: Qualitative comparison of prompt-conditioned depth estimation. Compared with the DA3-ft,
FocusDepth(DA3) produces more accurate target-region depth, cleaner boundary transitions, and
more coherent local structure around the prompted object or specified target region.

5.5     Qualitative Analysis

Figure 4 shows that DA3-ft can maintain low background errors but still produces pronounced errors
on complex prompted objects and their boundaries, visible as highlighted regions in the error maps.
With prompt guidance, FocusDepth(DA3) substantially reduces target-region AbsRel, while largely
preserving surrounding-scene depth quality. This visual evidence is consistent with the quantitative
trend that FocusDepth improves local target geometry without sacrificing global scene consistency.

6     Conclusion
We introduce Focusable Depth Estimation (FDE), a target-centric formulation of monocular depth
estimation that prioritizes foreground accuracy and boundary fidelity around a specified target while
preserving coherent global scene geometry. We further propose FocusDepth, a prompt-conditioned
monocular relative depth estimation framework that uses Multi-Scale Spatial-Aligned Fusion (MSSA)

                                                                              9
to inject spatially aligned target cues into dense depth representations for conditional refinement. To
make this task measurable, we establish FDE-Bench, which converts diverse RGB-D datasets into
standardized image–target–depth triplets and evaluates depth quality over foreground, boundary, and
global regions. Experiments on FDE-Bench show that FocusDepth improves target-region depth
accuracy and boundary fidelity without compromising full-image geometric coherence, particularly
in object-centric and manipulation-oriented scenarios. Together, these results establish FDE as a
concrete task for region-prioritized depth estimation, while also indicating areas where the current
study remains limited, including larger-scale joint training of FocusDepth and its application to
downstream tasks, which can be explored in future work.

                                                  10
References
 [1] Vasileios Arampatzakis, George Pavlidis, Nikolaos Mitianoudis, and Nikos Papamarkos. Monoc-
     ular depth estimation: A thorough review. IEEE Transactions on Pattern Analysis and Machine
     Intelligence, 46(4):2396–2414, 2023.
 [2] Amlaan Bhoi. Monocular depth estimation: A survey. arXiv preprint arXiv:1901.09402, 2019.
 [3] Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo
     Fusai, Lachy Groom, Karol Hausman, Brian Ichter, et al. π0 : A vision-language-action flow
     model for general robot control. arXiv preprint arXiv:2410.24164, 2024.
 [4] Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac
     Suris, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, et al. Sam 3:
     Segment anything with concepts. arXiv preprint arXiv:2511.16719, 2025.
 [5] Xingyu Chen, Fu-Jen Chu, Pierre Gleize, Kevin J Liang, Alexander Sax, Hao Tang, Weiyao
     Wang, Michelle Guo, Thibaut Hardin, Xiang Li, et al. Sam 3d: 3dfy anything in images. arXiv
     preprint arXiv:2511.16624, 2025.
 [6] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai,
     Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, et al.
     An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint
     arXiv:2010.11929, 2020.
 [7] Huan Fu, Mingming Gong, Chaohui Wang, Kayhan Batmanghelich, and Dacheng Tao. Deep
     ordinal regression network for monocular depth estimation. In Proceedings of the IEEE
     conference on computer vision and pattern recognition, pages 2002–2011, 2018.
 [8] Clément Godard, Oisin Mac Aodha, and Gabriel J Brostow. Unsupervised monocular depth
     estimation with left-right consistency. In Proceedings of the IEEE conference on computer
     vision and pattern recognition, pages 270–279, 2017.
 [9] Clément Godard, Oisin Mac Aodha, Michael Firman, and Gabriel J Brostow. Digging into
     self-supervised monocular depth estimation. In Proceedings of the IEEE/CVF international
     conference on computer vision, pages 3828–3838, 2019.
[10] Ming Gui, Johannes Schusterbauer, Ulrich Prestel, Pingchuan Ma, Dmytro Kotovenko, Olga
     Grebenkova, Stefan Andreas Baumann, Vincent Tao Hu, and Björn Ommer. Depthfm: Fast
     generative monocular depth estimation with flow matching. In Proceedings of the AAAI
     Conference on Artificial Intelligence, volume 39, pages 3203–3211, 2025.
[11] Mu Hu, Wei Yin, Chi Zhang, Zhipeng Cai, Xiaoxiao Long, Hao Chen, Kaixuan Wang, Gang Yu,
     Chunhua Shen, and Shaojie Shen. Metric3d v2: A versatile monocular geometric foundation
     model for zero-shot metric depth and surface normal estimation. IEEE Transactions on Pattern
     Analysis and Machine Intelligence, 46(12):10579–10596, 2024.
[12] Physical Intelligence, Kevin Black, Noah Brown, James Darpinian, Karan Dhabalia, Danny
     Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, et al. π0.5 : a vision-
     language-action model with open-world generalization. arXiv preprint arXiv:2504.16054,
     2025.
[13] Stephen James, Zicong Ma, David Rovick Arrojo, and Andrew J Davison. Rlbench: The robot
     learning benchmark & learning environment. IEEE Robotics and Automation Letters, 5(2):
     3019–3026, 2020.
[14] Bingxin Ke, Anton Obukhov, Shengyu Huang, Nando Metzger, Rodrigo Caye Daudt, and Kon-
     rad Schindler. Repurposing diffusion-based image generators for monocular depth estimation.
     In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages
     9492–9502, 2024.
[15] Zhenyu Li, Mykola Lavreniuk, Jian Shi, Shariq Farooq Bhat, and Peter Wonka. Amodal depth
     anything: Amodal depth estimation in the wild. In Proceedings of the IEEE/CVF International
     Conference on Computer Vision, pages 9673–9682, 2025.

                                               11
[16] Haotong Lin, Sili Chen, Junhao Liew, Donny Y Chen, Zhenyu Li, Guang Shi, Jiashi Feng, and
     Bingyi Kang. Depth anything 3: Recovering the visual space from any views. arXiv preprint
     arXiv:2511.10647, 2025.
[17] Haotong Lin, Sida Peng, Jingxiao Chen, Songyou Peng, Jiaming Sun, Minghuan Liu, Hujun
     Bao, Jiashi Feng, Xiaowei Zhou, and Bingyi Kang. Prompting depth anything for 4k reso-
     lution accurate metric depth estimation. In Proceedings of the Computer Vision and Pattern
     Recognition Conference, pages 17070–17080, 2025.
[18] Tao Lin, Gen Li, Yilei Zhong, Yanwen Zou, Yuxin Du, Jiting Liu, Encheng Gu, and Bo Zhao.
     Evo-0: Vision-language-action model with implicit spatial understanding. arXiv preprint
     arXiv:2507.00416, 2025.
[19] Tao Lin, Yilei Zhong, Yuxin Du, Jingjing Zhang, Jiting Liu, Yinxinyu Chen, Encheng Gu, Ziyan
     Liu, Hongyi Cai, Yanwen Zou, et al. Evo-1: Lightweight vision-language-action model with
     preserved semantic alignment. arXiv preprint arXiv:2511.04555, 2025.
[20] Sanggyun Ma, Wonjoon Choi, Jihun Park, Jaeyeul Kim, Seunghun Lee, Jiwan Seo, and
     Sunghoon Im. Bridging geometric and semantic foundation models for generalized monoc-
     ular depth estimation. In 2026 International Conference on Electronics, Information, and
     Communication (ICEIC), pages 1–6. IEEE, 2026.
[21] Yue Ming, Xuyang Meng, Chunxiao Fan, and Hui Yu. Deep learning for monocular depth
     estimation: A review. Neurocomputing, 438:14–33, 2021.
[22] Yao Mu, Tianxing Chen, Zanxin Chen, Shijia Peng, Zhiqian Lan, Zeyu Gao, Zhixuan Liang,
     Qiaojun Yu, Yude Zou, Mingkun Xu, et al. Robotwin: Dual-arm robot benchmark with genera-
     tive digital twins. In Proceedings of the computer vision and pattern recognition conference,
     pages 27649–27660, 2025.
[23] Luigi Piccinelli, Yung-Hsu Yang, Christos Sakaridis, Mattia Segu, Siyuan Li, Luc Van Gool,
     and Fisher Yu. Unidepth: Universal monocular metric depth estimation. In Proceedings of
     the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 10106–10116,
     2024.
[24] Luigi Piccinelli, Christos Sakaridis, Yung-Hsu Yang, Mattia Segu, Siyuan Li, Wim Abbeloos,
     and Luc Van Gool. Unidepthv2: Universal monocular metric depth estimation made simpler.
     IEEE Transactions on Pattern Analysis and Machine Intelligence, 2025.
[25] René Ranftl, Katrin Lasinger, David Hafner, Konrad Schindler, and Vladlen Koltun. Towards
     robust monocular depth estimation: Mixing datasets for zero-shot cross-dataset transfer. IEEE
     transactions on pattern analysis and machine intelligence, 44(3):1623–1637, 2020.
[26] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob Fergus. Indoor segmentation
     and support inference from rgbd images. In European conference on computer vision, pages
     746–760. Springer, 2012.
[27] Jürgen Sturm, Nikolas Engelhard, Felix Endres, Wolfram Burgard, and Daniel Cremers. A
     benchmark for the evaluation of rgb-d slam systems. In 2012 IEEE/RSJ international conference
     on intelligent robots and systems, pages 573–580. IEEE, 2012.
[28] Kuanning Wang, Ke Fan, Yuqian Fu, Siyu Lin, Hu Luo, Daniel Seita, Yanwei Fu, Yu-Gang Jiang,
     and Xiangyang Xue. Ocra: Object-centric learning with 3d and tactile priors for human-to-robot
     action transfer. arXiv preprint arXiv:2603.14401, 2026.
[29] Kuanning Wang, Ke Fan, Chenhao Qiu, Zeyu Shangguan, Yuqian Fu, Yanwei Fu, Daniel Seita,
     and Xiangyang Xue. Oflow: Injecting object-aware temporal flow matching for robust robotic
     manipulation. arXiv preprint arXiv:2604.17876, 2026.
[30] Xinlong Wang, Wei Yin, Tao Kong, Yuning Jiang, Lei Li, and Chunhua Shen. Task-aware
     monocular depth estimation for 3d object detection. In Proceedings of the AAAI conference on
     artificial intelligence, volume 34, pages 12257–12264, 2020.

                                                12
[31] Zehan Wang, Siyu Chen, Lihe Yang, Jialei Wang, Ziang Zhang, Hengshuang Zhao, and Zhou
     Zhao. Depth anything with any prior, 2025. URL https://arxiv.org/abs/2505.10565.
[32] Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, and Dieter Fox. Posecnn: A convo-
     lutional neural network for 6d object pose estimation in cluttered scenes. arXiv preprint
     arXiv:1711.00199, 2017.
[33] Lihe Yang, Bingyi Kang, Zilong Huang, Xiaogang Xu, Jiashi Feng, and Hengshuang Zhao.
     Depth anything: Unleashing the power of large-scale unlabeled data. In Proceedings of the
     IEEE/CVF conference on computer vision and pattern recognition, pages 10371–10381, 2024.
[34] Lihe Yang, Bingyi Kang, Zilong Huang, Zhen Zhao, Xiaogang Xu, Jiashi Feng, and Hengshuang
     Zhao. Depth anything v2. Advances in Neural Information Processing Systems, 37:21875–
     21911, 2024.
[35] Wei Yin, Chi Zhang, Hao Chen, Zhipeng Cai, Gang Yu, Kaixuan Wang, Xiaozhi Chen, and
     Chunhua Shen. Metric3d: Towards zero-shot metric 3d prediction from a single image. In
     Proceedings of the IEEE/CVF international conference on computer vision, pages 9043–9053,
     2023.
[36] Deheng Zhang, Yuqian Fu, Runyi Yang, Yang Miao, Tianwen Qian, Xu Zheng, Guolei Sun,
     Ajad Chhatkuli, Xuanjing Huang, Yu-Gang Jiang, et al. Egonight: Towards egocentric vision
     understanding at night with a challenging benchmark. arXiv preprint arXiv:2510.06218, 2025.
[37] Ning Zhang, Francesco Nex, George Vosselman, and Norman Kerle. Lite-mono: A lightweight
     cnn and transformer architecture for self-supervised monocular depth estimation. In Proceedings
     of the IEEE/CVF conference on computer vision and pattern recognition, pages 18537–18546,
     2023.
[38] Chaoqiang Zhao, Qiyu Sun, Chongzhen Zhang, Yang Tang, and Feng Qian. Monocular depth
     estimation based on deep learning: An overview. Science China Technological Sciences, 63(9):
     1612–1627, 2020.
[39] Chaoqiang Zhao, Youmin Zhang, Matteo Poggi, Fabio Tosi, Xianda Guo, Zheng Zhu, Guan
     Huang, Yang Tang, and Stefano Mattoccia. Monovit: Self-supervised monocular depth esti-
     mation with a vision transformer. In 2022 international conference on 3D vision (3DV), pages
     668–678. IEEE, 2022.

                                                13
A      Technical Appendices
A.1     FDE-Bench

A.1.1      FDE-Bench Details
This appendix complements Section 4 with construction details and visual statistics for FDE-Bench.
Appendix Figure 5 summarizes how heterogeneous RGB-D sources are converted into standardized
image–target–depth triplets, while Appendix Figures 6–9 document the resulting scene diversity,
target-scale distribution, regional depth-gradient statistics, and supported prompt formats.

Table 4: Statistics of FDE-Bench, including the images, triplets, prompt types, and object categories.

                                          Images            Triplets
                    Dataset                                                      Prompt types Categories
                                      train      val     train         val
                    NYU v2     0.8K 0.7K 22.4K 18.4K box / text                                               895
                    YCB-Video 1.2K 0.1K 7.1K     0.8K box / text                                               22
                    TUM RGB-D 12.5K 1.4K 192.7K 22.3K box                                                       -
                    RLBench   1.7K 1.7K 15.1K 15.2K box / text                                                55
                    RoboTwin  4.3K 4.3K 15.6K 15.8K box                                                         -
                    FDE-Bench        20.5K 8.2K 252.9K 72.5K box / text                                       972

                   Workflow of Focusable Depth Estimation Dataset Generation
      Input:                  Stage1:                        Stage2:                          Stage3:                        Output:
 SourceDataset       Interest RegionSelection            Prompt Generation                Entry Assembly                    Focusable
                    Using Existing Masks                                                                                   Depth Dataset
                                              1 Object    Text Prompt
                                                Mask                                                 ①
                                                           Robot
                                                           Arm
                      Existing Semantic
                                                                                          Original
                     Segmentaion Masks
                                                                                           Image
                           Yes                            Class Name                                     Triplet Entry
                                Existing                                     Prompt      ③
                              Segmentation      RoI                                                                              Triplet Entry
                                                                              (Text or                    Image
                                Masks?         Mask                                      Combined                 Prompt
                                                                             Geometry)                                           Image
    Image&Depth             No                             Geometry                                                                      Prompt
                                                                                          Prompt          Depth    RoI
                     Generating Pseudo                      Prompt                       per Region                              Depth    RoI

                     Masks Using SAM
                                                                                                                           Ready Data for
                                              1 Object                                                                       Focusable
                                                Mask                                                 ②                          Depth
    Segmentation                                                                          Original                         Estimation Task
                     Pseudo Segmentaion                    Generated                       Depth
                           Masks                          from Masks

Figure 5: Construction pipeline of FDE-Bench. Existing depth datasets are converted from heteroge-
neous annotations into standardized image–target–depth triplets for unified region-aware evaluation.

The conversion pipeline retains the original RGB image and depth map from each source dataset and
attaches a single target specification to each triplet. Source-provided instance or semantic masks are
used when available; otherwise, SAM automatic mask generation provides pseudo masks that are
filtered with the same area protocol and marked in the metadata. For each retained region, the mask
is stored for evaluation, the tight bounding box is used as the box prompt, and the semantic class
name is used as the text prompt when such labels are available. Consequently, one source image can
produce multiple benchmark triplets that share the same RGB-D observation but differ in their target
region.

A.1.2      Dataset Scope and Statistics
The five adapted sources listed in Table 4 provide complementary coverage of indoor scenes, tabletop
objects, ego-view motion, and manipulation environments. Appendix Figure 6 visualizes repre-
sentative RGB, segmentation, and depth examples, and Appendix Figure 7 shows that target sizes
vary substantially across sources, from small local objects to large scene-dominant regions. Prompt

                                                              14
          Dataset                   RGB Image               Segmentation              Depth Map

         NYU v2
         Indoor clutter
         Heavy occlusion

         YCB-VIDEO
         Tabletop objects
         Clear categories

         TUM RGB-D
         Ego-view
         Dynamic scenes

         RLBench
         Simulated manipulation
         Goal-oriented

         RoboTwin
         Embodied tasks
         Task-driven

Figure 6: Representative examples from the five source datasets adapted into FDE-Bench. For each
dataset, we show an RGB image together with its segmentation and depth map, highlighting the
diversity of scene structures and target-centric contexts covered by the benchmark, including indoor
clutter, large-scale geometry, tabletop objects, ego-view dynamics, and embodied manipulation
settings in both real and simulated environments.

availability follows the annotations of each source: NYU v2, RLBench, and YCB-Video provide both
box and text prompts, whereas TUM RGB-D and RoboTwin are evaluated with box prompts only, as
illustrated in Appendix Figure 9.
All split assignments are made at the image or sequence level to avoid leakage across target triplets.
NYU v2 uses its original train/val partition, TUM RGB-D follows the benchmark-specific train/val
split, and YCB-Video uses a 10% image-level validation split. For RLBench and RoboTwin, each
embodied task contributes two episodes, with one assigned to training and the other to validation.

A.1.3   Region Definitions and Evaluation Protocol

Section 4 defines the foreground, boundary, and global regions used for evaluation. Here, Appendix
Figure 8 provides supporting statistics by plotting depth-gradient distributions for these regions across
the source datasets. Boundary bands consistently show stronger depth variation than foreground or
background areas, which motivates reporting boundary metrics separately from target-interior and
whole-image metrics.
The global region is evaluated on all valid pixels rather than on a background-only complement,
because scene-level geometric coherence is a whole-image property. Regional metrics are nevertheless
aggregated per target: each image–target–depth triplet is scored first, and the resulting target-level
values are then averaged according to the reporting protocol of each experiment. This prevents images
with many retained targets from dominating the benchmark score while preserving global alignment
through whole-image scale-shift normalization for relative-depth models.

                                                   15
                                                                       3 - # F O D I                                                                                                            / : 6  W                                                                                                           5 6 .  3 ( #  %
                                                                                                  . F E J B O                                                                                                        . F E J B O                                                                                                          . F E J B O       
                                                                                                  . F B O                                                                                                          . F B O                                                                                                           . F B O         
                                                                                                                                                                                                                                                                                                       
 % F O T J U Z  	 M P H  T D B M F 
                                                                                                                                     

                                                                                                                               % F O T J U Z  	 M P H  T D B M F 

                                                                                                                                                                                                                                                           % F O T J U Z  	 M P H  T D B M F 

                                                                                                                                                                                                                                                                                                       
                                             
                                                                                                                                                                                                                                                                                                       
                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                       

                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                       
                                                                   1 J Y F M  $ P V O U  Q F S  0 C K F D U                                                                                1 J Y F M  $ P V O U  Q F S  0 C K F D U                                                                                 1 J Y F M  $ P V O U  Q F S  0 C K F D U
                                                                     : $ #  7 J E F P                                                                                                       3 P C P 5 X J O
                                                                                                . F E J B O                                                                                                         . F E J B O       
                                                                                                . F B O                                                                                                           . F B O          

                                                                                                                                                                        
 % F O T J U Z  	 M P H  T D B M F 

                                                                                                                            % F O T J U Z  	 M P H  T D B M F 
       

                                                                                                                                                                        
                                                                                                                                                                                       
                                                                   1 J Y F M  $ P V O U  Q F S  0 C K F D U                                                                                1 J Y F M  $ P V O U  Q F S  0 C K F D U

        Figure 7: Object size statistics across the source datasets of FDE-Bench, measured by pixel count
        per object. Each subplot shows the distribution of target-object pixel sizes for one adapted dataset,
        with density plotted on a logarithmic scale and the corresponding mean and median reported. The
        figure highlights substantial cross-dataset variation in object scale, indicating that FDE-Bench covers
        targets ranging from small local objects to large scene-dominant instances.

         A.2                                        Training Hyperparameters

        Tables 5 and 6 report the training hyperparameters used for FocusDepth and the fine-tuned DA2/DA3
        baselines, respectively. FocusDepth uses a two-stage schedule over the same five-epoch training
        budget, whereas the DA2-ft and DA3-ft baselines are trained with a single-stage fine-tuning schedule.

                                                                                                 Table 5: Training hyperparameters for FocusDepth.

                                                        Hyperparameter                                              Stage 1                                                                                                                   Stage 2
                                                                                                                                                                −4
                                                        Learning rate                                               1 × 10                                                                                                                    1 × 10−5
                                                        Batch size per-device                                       4                                                                                                                         4
                                                        Input resolution                                            1008 × 1008                                                                                                               1008 × 1008
                                                        Max steps                                                   1 epoch                                                                                                                   4 epochs
                                                        Warmup steps                                                1/10 of Stage 1 max steps                                                                                                 1/10 of Stage 2 max steps
                                                        LR scheduler                                                Cosine decay with linear warmup                                                                                           Cosine decay with linear warmup
                                                        Weight decay                                                1 × 10−5                                                                                                                  1 × 10−5
                                                        Dropout                                                     0.1                                                                                                                       0.1
                                                        Optimizer                                                   AdamW                                                                                                                     AdamW
                                                        Gradient clipping                                           1.0                                                                                                                       1.0

         A.3                                        Additional Experimental Results

        Table 2 reports the text-prompt comparison on NYU v2, RLBench, and YCB-Video, complementing
        the main box-prompt results with zero-shot baselines and fine-tuned DA2/DA3 variants.
        Table 7 reports the box-prompt comparison on TUM RGB-D and YCB-Video, where zero-shot
        baselines are shown together with DA3 fine-tuning variants for the datasets not included in the main
        box-prompt table.

                                                                                                                                                                                                   16
                                                                 3 - # F O D I                                                                                                    / : 6  W 
                                                                                                                                        
                                                                                              # B D L H S P V O E                                       # B D L H S P V O E
                                                                                           ' P S F H S P V O E                                    ' P S F H S P V O E
                                                                                           # P V O E B S Z                                        # P V O E B S Z

                                                                                                                                     
 % F O T J U Z

                                                                                                                     % F O T J U Z
                                                                                                                                        
                    
                                                                                                                                        
                                                                                                                                     
                                                                                                                                     
                                                                                                                                                        
                                                  log10  	 H S B E  N B H O J U V E F 
                                                                      log10  	 H S B E  N B H O J U V E F 

                                                           5 6 .  3 ( #  %                                                                                                   : $ #  7 J E F P
                                                                                                                                        
                                                                                              # B D L H S P V O E                                                                                             # B D L H S P V O E
                                                                                              ' P S F H S P V O E                                                                                          ' P S F H S P V O E
                                                                                           # P V O E B S Z                                                                                                 # P V O E B S Z
                                                                                                                                        
 % F O T J U Z

                                                                                                                     % F O T J U Z
                    
                                                                                                                                        
                    
                                                                                                                                        
                                                                                                                                     
                                                                                                                                                                            
                                                  log10  	 H S B E  N B H O J U V E F 
                                                                            log10  	 H S B E  N B H O J U V E F 

                                                               3 P C P 5 X J O
                                                                                           # B D L H S P V O E
                                                                                           ' P S F H S P V O E
                                                                                              # P V O E B S Z
                    
 % F O T J U Z

                    
                    
                    
                    
                                                                                    
                                                  log10  	 H S B E  N B H O J U V E F 

 Figure 8: Depth-gradient statistics across the source datasets of FDE-Bench. For each dataset,
 we plot the distribution of depth gradient magnitudes, shown as log10 (grad magnitude), separately
 for background, foreground, and boundary regions. The distributions reveal systematic regional
 differences, with boundary areas generally exhibiting stronger depth variations, supporting the region-
 aware design of FDE evaluation.

 A.4                  RLBench Prompt-Correctness Mean–Median Comparison

 The prompt-correctness study in Section 5.3 reports mean values, unlike the main comparative results
 that report medians. We use means in this diagnostic experiment because prompt perturbations
 can create bad cases whose aggregate effect is important for measuring robustness. Table 8 reports
 both means and medians for the same RLBench class-specific text-prompt setting, showing how the
 diagnostic mean values relate to the median-based protocol used in the main comparison.

                                                                                                                    17
                                        RGB Image + Prompt                                 Depth Map (Ground Truth)
      Text + Box
       prompt

             +

   FDE-Bench includes
   samples with both a                                                                                                      The fine structure
   bounding box and a                                                                                                       and boundaries of
                                 Text Prompt: “the small tube                                                               small objects.
   text prompt.
                                         on the shell”

          Only Box                      RGB Image + Prompt                                 Depth Map (Ground Truth)
          prompt

 FDE-Bench also includes
 samples with only a                                                                                                       Depth discontinuities
 bounding box without                                                                                                      for transparency and
                                         Only Box Prompt                                                                   occlusion.
 any text prompt.
                                            (No Text)

Figure 9: Illustration of target specification formats in FDE-Bench. Depending on the adapted source
dataset, a target may be specified by a bounding box together with a text prompt, or by a bounding
box alone. The examples also highlight typical target-centric depth challenges addressed by FDE,
including fine object structures, boundary fidelity, and depth discontinuities caused by occlusion or
transparency.

                 Table 6: Training hyperparameters for the DA2-ft and DA3-ft baselines.

                               Hyperparameter                   Value
                               Learning rate                    1 × 10−5
                               Batch size per-device            4
                               Input resolution                 1008 × 1008
                               Max steps                        5 training epochs
                               Warmup steps                     1/10 of max steps
                               LR scheduler                     Cosine decay with linear warmup
                               Weight decay                     1 × 10−5
                               Dropout                          0.1
                               Optimizer                        AdamW
                               Gradient clipping                1.0

Table 7: Additional box-prompt results on TUM RGB-D and YCB-Video. We compare zero-shot
depth foundation models, the fine-tuned DA3 baseline, and FocusDepth variants across boundary,
foreground, and global regions.
Dataset              Method                    Boundary region                  Foreground region                    Global region
                                                δ1 ↑            AbsRel ↓          δ1 ↑            AbsRel ↓          δ1 ↑            AbsRel ↓
               UniDepth-v1 [23]          0.980 (0.744, 1.000)    0.092     1.000 (0.867, 1.000)    0.078     0.948 (0.845, 0.985)      0.085
               UniDepth-v2 [24]          0.979 (0.805, 1.000)    0.080     1.000 (0.922, 1.000)    0.061     0.967 (0.877, 0.987)      0.070
               Metric3D-v2 [11]          0.984 (0.821, 1.000)    0.087     1.000 (0.913, 1.000)    0.076     0.957 (0.856, 0.989)      0.083
TUM RGB-D [27] DA2 [34]                  0.960 (0.709, 1.000)    0.095     0.999 (0.818, 1.000)    0.080     0.946 (0.849, 0.983)      0.076
                     DA3 [16]        0.964 (0.699, 1.000)        0.099     0.999 (0.790, 1.000)    0.080     0.938 (0.778, 0.980)      0.093
                     DA3-ft          0.999 (0.853, 1.000)        0.068     1.000 (0.944, 1.000)    0.057     0.970 (0.905, 0.990)      0.060
                     FocusDepth(DA3) 1.000 (0.882, 1.000)        0.061     1.000 (0.966, 1.000)    0.051     0.975 (0.912, 0.991)      0.057
                     UniDepth-v1 [23]    1.000 (0.984, 1.000)    0.042     1.000 (0.998, 1.000)    0.037     0.993 (0.981, 0.997)      0.045
                     UniDepth-v2 [24]    0.999 (0.965, 1.000)    0.036     1.000 (0.994, 1.000)    0.026     0.996 (0.991, 0.998)      0.031
                     Metric3D-v2 [11]    1.000 (0.986, 1.000)    0.040     1.000 (0.998, 1.000)    0.031     0.997 (0.988, 0.999)      0.042
YCB-Video [32]       DA2 [34]            0.999 (0.963, 1.000)    0.045     1.000 (0.993, 1.000)    0.038     0.994 (0.972, 0.998)      0.040
                     DA3 [16]        0.994 (0.938, 1.000)        0.054     0.999 (0.986, 1.000)    0.045     0.992 (0.961, 0.997)      0.047
                     DA3-ft          1.000 (0.988, 1.000)        0.042     1.000 (0.999, 1.000)    0.036     0.997 (0.984, 0.999)      0.044
                     FocusDepth(DA3) 1.000 (0.990, 1.000)        0.037     1.000 (0.999, 1.000)    0.026     0.998 (0.992, 0.999)      0.032

                                                                    18
Table 8: Mean–median comparison for the RLBench prompt-correctness study under class-specific
text prompts. The main paper reports mean values for this diagnostic study to better reflect bad cases
under prompt perturbations; medians are included here for comparison with the main evaluation
metrics.
Method                                                Boundary region                                Foreground region                                    Global region
                                      δ1 mean ↑ δ1 med. ↑ AbsRel mean ↓ AbsRel med. ↓ δ1 mean ↑ δ1 med. ↑ AbsRel mean ↓ AbsRel med. ↓ δ1 mean ↑ δ1 med. ↑ AbsRel mean ↓ AbsRel med. ↓
Correct prompt                          0.919     0.995       0.108         0.045       0.901     1.000       0.137         0.050       0.943     0.996          0.075      0.029
Wrong prompt (other visible object)     0.914     0.995       0.111         0.045       0.884     1.000       0.148         0.052       0.943     0.996          0.074      0.029
Wrong prompt (absent object)            0.911     0.994       0.117         0.047       0.886     1.000       0.152         0.053       0.939     0.995          0.078      0.030
Empty prompt                            0.910     0.993       0.118         0.045       0.886     1.000       0.154         0.051       0.939     0.995          0.078      0.029
DA3-ft no-prompt baseline               0.860     0.973       0.162         0.068       0.804     0.998       0.226         0.088       0.915     0.984          0.105      0.041

                      RoboTwin                            RLBench                    NYU v                    TUM RGB-D                         YCB-Video Error
                                                                                                                                                                          High
             Image
             DA -ft
  FocusDepth
     (DA )

                                                                                                                                                                          Low

Figure 10: Additional qualitative comparison of prompt-conditioned depth estimation. Compared
with the DA3-ft, FocusDepth(DA3) produces more accurate target-region depth, cleaner boundary
transitions, and more coherent local structure around the prompted object or specified target region.

                                                                                           19
                   Foreground                    Boundary                    Full Image

   NYU v

  RLBench

RoboTwin

Figure 11: Validation curves of DA3-ft and FocusDepth(DA3) over training epochs. We compare δ1
and AbsRel on NYU v2, RLBench, and RoboTwin across foreground, boundary, and global regions.
FocusDepth(DA3) consistently improves target-relevant regions, especially foreground and boundary
areas, while preserving global depth quality.

                                               20
