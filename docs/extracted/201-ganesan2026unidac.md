---
source_id: 201
bibtex_key: ganesan2026unidac
title: UniDAC: Universal Metric Depth Estimation for Any Camera
year: 2026
domain_theme: Estimasi Kedalaman
verified_pdf: 201_UniDAC Kedalaman Metrik Universal untuk Sembarang Kamera.pdf
char_count: 85055
---

UniDAC: Universal Metric Depth Estimation for Any Camera

                                                           Girish Chandar Ganesan1                 Yuliang Guo2         Liu Ren2        Xiaoming Liu1,3
                                                            1
                                                                Michigan State University 2 Bosch Research North America & Bosch Center for AI (BCAI)
                                                                                     3
                                                                                         University of North Carolina at Chapel Hill
                                                      ganesang@msu.edu           [yuliang.guo2,liu.ren]@us.bosch.com                        liuxm@cs.unc.edu
                                                                                 https://girish1511.github.io/UniDAC
arXiv:2603.27105v2 [cs.CV] 8 Apr 2026

                                                                  Abstract
                                                                                                                                UniK3D                       DAC
                                        Monocular metric depth estimation (MMDE) is a core chal-                              Indoor                              Persp.
                                        lenge in computer vision, playing a pivotal role in real-
                                        world applications that demand accurate spatial under-
                                        standing. Although prior works have shown promising zero-                                            UniDAC
                                        shot performance in MMDE, they often struggle with gen-                               Outdoor                      360◦        Fisheye
                                        eralization across diverse camera types, such as fisheye
                                        and 360◦ cameras. Recent advances have addressed this
                                        through unified camera representations or canonical rep-
                                        resentation spaces, but they require either including large-
                                        FoV camera data during training or separately trained
                                        models for different domains. We propose UniDAC, an                                 Universal Domain              Cross-Camera
                                        MMDE framework that presents universal robustness in all                               Robustness                 Generalization
                                        domains and generalizes across diverse cameras using a
                                                                                                                 Figure 1. We propose UniDAC, a universal, domain-agnostic met-
                                        single model. We achieve this by decoupling metric depth                 ric depth estimation framework that generalizes to any camera.
                                        estimation into relative depth prediction and spatially vary-            Unlike prior methods that either rely on large-FoV data during
                                        ing scale estimation, enabling robust performance across                 training or require separate models for indoor and outdoor do-
                                        different domains. We propose a lightweight Depth-Guided                 mains, UniDAC is trained solely on perspective images yet gener-
                                        Scale Estimation module that upsamples a coarse scale map                alizes effectively to large-FoV inputs, leveraging a universal model
                                        to high resolution using the relative depth map as guid-                 to robustly handle both indoor and outdoor environments.
                                        ance to account for local scale variations. Furthermore,
                                        we introduce RoPE-ϕ, a distortion-aware positional embed-
                                        ding that respects the spatial warping in Equi-Rectangular               itation by predicting depth up to an unknown scale in addi-
                                        Projections (ERP) via latitude-aware weighting. UniDAC                   tion to leveraging large-scale data [44, 61, 62] and diffusion
                                        achieves state of the art (SoTA) in cross-camera generaliza-             priors [12, 26, 27]. However, despite their success, these
                                        tion by consistently outperforming prior methods across all              up-to-scale methods encounter limitations in real-world ap-
                                        datasets.                                                                plications where precise spatial measurements are essential,
                                                                                                                 necessitating the inherently challenging and ill-constrained
                                                                                                                 task of monocular metric depth estimation.
                                        1. Introduction
                                                                                                                    Recent works [18, 23, 40, 42, 57, 65] have demonstrated
                                        Depth estimation plays a pivotal role in bridging the gap be-            zero-shot performance in MMDE by conditioning upon
                                        tween 2D and 3D vision, enabling a wide range of applica-                camera parameters [40, 42], adopting a canonical space
                                        tions such as autonomous vehicles [37, 58], robotics [6, 49],            [23, 65] or explicitly estimating the scale [57], thereby over-
                                        and AR/VR [8, 50].                                                       coming the scale-depth ambiguity. However, despite their
                                           With the advent of deep learning, early works [3, 10, 29,             remarkable performance, these methods have been devel-
                                        39, 66] achieve promising results. However, they fail to                 oped with images from perspective cameras and thereby
                                        generalize across diverse scenes due to scale-depth ambi-                struggle with large FoV images captured from fisheye or
                                        guity. Recent methods [26, 44, 61, 62, 64] address this lim-             360◦ cameras.
                                                                s∈R                                      S ∈ RH×W

               (a) No Scaling                             (b) Median Scaling                        (c) Depth-Guided Scaling

Figure 2. We show the Abs.Rel error between the predicted relative depth and the ground truth by performing (a) no scaling, (b) median
scaling, and (c) depth guided scaling. Theoretically, the relative and metric depth are aligned with a single scale s. Practically, (b) we
observe that the irregularities in the relative depth cannot be compensated with a single scalar s. Thus, to tackle this, (c) we propose a
Depth-Guided Scale Estimation module that predicts a high-resolution scale map S respecting local variations.

    Recently, [19, 41] demonstrate remarkable MMDE per-                 using the predicted relative depth as a non-parametric guid-
formance on diverse cameras. UniK3D [41] introduces a                   ance signal, ensuring that spatially coherent regions share
unified angular representation based on spherical harmonics             consistent scale values—while adding negligible computa-
to represent diverse camera models and subsequently con-                tional overhead.
dition the metric depth prediction. While UniK3D achieves                   To better harness the potential of modern transformer
strong cross-dataset generalization with a single model cov-            architectures for large FoV images, we propose RoPE-ϕ,
ering both indoor and outdoor domains, it relies on training            a distortion-aware rotary positional embedding specifically
with a diverse set of camera models, including large-FoV                designed for the Equi-Rectangular Projection (ERP) do-
data that closely resemble the test distribution. In contrast,          main. By incorporating latitude-aware weighting, RoPE-ϕ
DAC [19] achieves strong cross-camera generalization from               ensures that positional distances more faithfully correspond
perspective-only training by adopting an Equi-Rectangular               to geodesic proximity on the sphere. Comprehensive exper-
Projection (ERP) as a canonical representation space, along             iments demonstrate that UniDAC achieves robust general-
with FoV-aligned and multi-resolution training strategies.              ization across both scenes and cameras, substantially out-
However, DAC requires separate models for indoor and out-               performing prior SoTA approaches.
door domains, and its performance degrades when using a                     We summarize our contributions as follows:
single unified model across both domains—partly due to its             ✓ We propose UniDAC, a unified framework for monocu-
smaller-scale training compared to UniK3D.                                 lar metric depth estimation that generalizes across diverse
    In this work, we ask: Can we design a monocular metric                 camera models and scene types using a single model.
depth estimation (MMDE) framework that generalizes ef-                 ✓ We design a Depth-Guided Scale Estimation module that
fectively across all camera types and scene domains, with-                 generates a spatially adaptive scale map with minimal
out substantially increasing model or dataset scale? We                    computational overhead.
propose UniDAC, a unified MMDE framework that gener-                   ✓ We introduce RoPE-ϕ, a distortion-aware RoPE, that re-
alizes across both diverse camera geometries and visual do-                spects the ERP geometry via latitude-based weighting.
mains within a single model, as illustrated in Fig. 1. Our key         ✓ Extensive experiments show that UniDAC achieves state-
insight is to achieve scene–camera unification by decom-                   of-the-art cross-camera generalization in MMDE.
posing metric depth estimation into relative depth predic-
tion and scale estimation - two components that inherently              2. Related Works
rely on different contextual scopes and benefit differently
from pre-trained foundation model backbones. To this end,               2.1. Perspective Monocular Depth Estimation
we partition encoder features into early and late-stage repre-          Monocular depth estimation can be broadly categorized into
sentations: the former captures local structural details well-          affine-invariant, up-to-scale depth estimation, and absolute,
suited for relative depth, while the latter encodes global,             metric depth estimation.
scene-level context crucial for estimating scale.                           Prior works [26, 44, 61, 62, 64] achieve notable general-
    Although metric and relative depth are theoretically con-           ization performance by leveraging large-scale labeled data
nected by a single global scalar (scene scale), in practice,            [44, 64], extensive unlabeled data [61, 62], or strong gener-
relative depth often exhibits spatially non-uniform scaling             ative priors [26] of pre-trained diffusion models [48]. How-
across the scene, as illustrated in Fig. 2. To handle this, we          ever, despite their success, these methods encounter limita-
introduce a Depth-Guided Scale Estimation (DGSE) mod-                   tions in real-world applications where accurate metric depth
ule that first predicts a coarse, low-resolution scale map              is essential.
from global encoder features. We then upsample this map                     Recent works [18, 23, 40, 42, 65] exhibit robustness
in the zero-shot monocular metric depth estimation. [18,         The relative depth map Drel contains local information,
23, 65] implicitly infer the scale of the scene by in-           such as object shapes and boundaries, whereas the scale-
stilling the ground-truth camera parameters [18] or map-         shift scalars are global factors that depend on the scene as
ping the camera parameters to a canonical space [23, 65].        a whole, such as indoor or outdoor. Therefore, the metric
UniDepth [40, 42] implicitly predicts the scale in the form      depth Dm can be split into local and global components and
of camera parameters and applies them as a condition for         are represented using Drel and {s, t} respectively.
the metric depth estimation, achieving incredible zero-shot
metric depth performance without the need for intrinsic pa-      3.2. RoPE
rameters during inference. Despite these advances, none of       Rotary Positional Embedding (RoPE) was first introduced
these methods achieves satisfactory zero-shot performance        by [54] in the language domain. RoPE embeds relative po-
on large FoV images.                                             sitional information among transformer tokens as position-
                                                                 dependent rotations. Specifically, given the n-th token
2.2. Large FoV Monocular Depth Estimation                        qn ∈ R1×d , RoPE rotates them using Euler’s formula eiψ to
Fisheye and 360◦ capture rich contextual information due         get q′n = qn einψ , before applying the attention operations.
to large FoV and can thereby benefit the task of depth esti-     RoPE practically implements the rotations by first convert-
mation [1, 24, 30, 51, 67]. Due to the scarcity of large-FoV     ing the tokens qn to the complex domain, q¯n ∈ C1×d/2 , in
depth data, initial works [11, 24, 30, 46, 51, 55, 60, 67, 70]   addition to using multiple frequencies ψk across the channel
are constrained to in-domain setting. These works handle         dimensions. The rotations for N tokens are then compactly
distortions by adjusting the convolutional kernels through       represented in a rotation matrix R ∈ CN ×d defined as:
deformable CNNs [55, 60, 70], partitioning ERP into seg-
                                                                                       R(n, t) = einψk .                     (2)
ments [24, 46], and employing transformers to model the
distortions [11, 30, 51, 67]. Although these methods             [21] later proposes 2D-RoPE, designed to be compatible
achieve remarkable in-domain performance, they struggle          with vision transformers. Given an image I ∈ RH×W ×3 ,
to generalize across diverse cameras.                            [21] replaces the 1D indexing n to 2D pixel indices pn =
                                                                 {un , vn } ∈ R{0,...,H}×{0,...,W } . Thus, the rotation matrix
2.3. Cross-Camera Generalizable MMDE                             in Eq. (2) is modified to:
A key challenge in building a foundational model for di-
verse cameras is the lack of large-scale, large-FoV datasets.           R(n, 2k) = eiun ψk ; R(n, 2k + 1) = eivn ψk ,        (3)
UniK3D [41] combines perspective and large-FoV datasets          where, the frequencies ψk are calculated as:
using a spherical harmonics-based angular representation to
share information across camera types. However, its per-                    ψk = {100−4k/d : k ∈ {0, . . . , d/4}}.          (4)
formance is limited by training-time camera diversity and
lacks cross-camera generalization. Recent methods [13, 19]       4. UniDAC
achieve strong cross-camera generalization using only per-
spective images. [13] extends UniDepth [40] to fisheye           We propose UniDAC, a unified framework for monocular
images via steering tokens but is restricted to perspective      metric depth estimation with cross-camera generalization.
and fisheye inputs. DAC [19] introduces a canonical Equi-        We posit that one of the main issues with developing a uni-
Rectangular Projection (ERP) space with pitch-aware aug-         fied model is the variation in depth ranges across different
mentation to simulate large-FoV images from perspective          domains. For example, the maximum depth is typically
data, achieving SOTA cross-camera results. However, it re-       around 10 meters for indoor scenes, whereas it’s 80 me-
quires separate models for indoor and outdoor domains. In        ters for outdoor scenes. Thus, to prevent the model from
contrast, UniDAC achieves cross-camera and cross-domain          getting confused trying to predict varied ranges, we decou-
generalization with a single unified model.                      ple the metric depth prediction into domain-agnostic and
                                                                 domain-specific components, i.e., relative depth map and
                                                                 scene scale, respectively. As mentioned in Sec. 3.1, the rel-
3. Preliminaries                                                 ative depth map depends only on local pixel variations in
3.1. Metric Depth Decomposition                                  the image; thus, we utilize features rich in local informa-
                                                                 tion to estimate relative depth as described in Sec. 4.1. On
Given a metric depth map Dm ∈ RH×W , it can be decom-            the other hand, the scale and shift parameters depend on
posed into a relative depth map Drel ∈ RH×W and scale-           the scene as a whole, and we estimate it using the global
shift scalars {s, t} ∈ R as follows:                             information-rich features as detailed in Sec. 4.2. To account
                                                                 for the irregularities in the predicted relative depth, we esti-
                      Dm = sDrel + t.                     (1)    mate a high-resolution scale map as opposed to a 1-D scale
                 Sph. Repr.                        Distortion-Aware                                                              Standard
                                                                                    Relative Depth Estimation
                                    ϕ              Feature Extraction                                                            Proposed
                 ϕ = vπ
                     W

 I     p = [u, v]                  w(ϕ)                              Fl                                       Drel
                                                                           Fg                                                      Lrel
                                        RoPE-ϕ      Enc.                                         Dec.

Depth-Guided Scale Estimation
                              Sr                                           S                                  Dm
         Self                                          Depth                                                                       Lm
                 MLP                                   Guided
         Attn
                                                       Upsample

Figure 3. Overview of proposed method. UniDAC decouples metric depth estimation into relative depth and scale estimation. Relative
depth relies on local scene information, while scene scale is domain-specific and depends on global scene information. Therefore, given
an ERP image I, we split the features from the encoder into local Fl and the global features Fg . We predict the relative depth Drel using
the local features Fl . We predict a scale map S from the global features Fg to account for the irregularities in Drel . We first predict a
low-resolution scale map Sr and obtain the high-resolution S through our proposed Depth-Guided Scale (DGS) estimation module. The
DGS upsamples Sr by using the Drel as a guide to ensure the upsampling process respects object boundaries. The final metric depth Dm
is calculated using Drel and S as shown in Eq. (8). We introduce distortion-aware positional embedding, termed RoPE-ϕ, that applies a
weight w(ϕ) to the RoPE rotations based on the latitude ϕ. We train using two losses Lrel and Lm applied on Drel and Dm , respectively.

through our proposed Depth-Guided Scale Estimation mod-                   to each other by a couple of 1-D scalars {s, t} as shown in
ule (Sec. 4.2). Specifically, we achieve higher efficiency by             Eq. (1). However, in practice, the relative depth predicted
first predicting a low-resolution scalar map (Sec. 4.2.1) and             by a network may be slightly stretched or compressed in
followed by a depth-guided upsampling (Sec. 4.2.2). An                    different regions due to local errors or occlusions. Thus,
overview of our pipeline is shown in Fig. 3.                              to adjust for the irregularities in Drel , we predict a scalar
                                                                          map S ∈ RH×W . A naive solution is to predict S through
4.1. Relative Depth Estimation                                            a series of transpose convolutions, but this would incur an
Given an input image I ∈ RH×W ×3 , we derive set of fea-                  additional computational cost. Moreover, predicting a high-
tures F = {Fl , Fg } ∈ Rh×w×C from encoder E, where                       dimensional output S is challenging and may lead to poor
Fl , Fg are the local and global features respectively. Fl and            estimates. Thus, we propose a low-resolution scale predic-
Fg are split as the outputs from the early and final layers               tion followed by a lightweight non-parametric depth-guided
of E, respectively. We then estimate the relative depth map               upsampling to estimate S. We predict t from the CLS token
D¯rel ∈ RH×W ×1 from local features Fl via a decoder D.                   of the Fg by passing it through a shallow MLP.
    The predicted relative depth map can have an arbitrary
scale, which can affect the later scale estimation step. We               4.2.1. Patch-level Scale Estimation
normalize Dˆrel by median scaling to get Drel :                           The global features are low-resolution features correspond-
                                                                          ing to non-overlapping patches on the image I. Since we
                      Dˆrel                                               want similar features to have similar scales, we employ a
             Drel =         ; ŝ = Median(Dˆrel ).             (5)
                       ŝ                                                 self-attention on Fg followed by a shallow-MLP to esti-
                                                                          mate a low-resolution scale map Sr ∈ Rh×w . Thus, we
4.2. Depth-Guided Scale Estimation                                        get Sr = MLP(SelfAttn(Fg )).
The predicted relative depth map Drel requires global                        Sr is a low-resolution spatial map that must be upsam-
scalars, i.e., scale s and shift t, to be converted to met-               pled to obtain S, while maintaining low computational over-
ric depth. The global scalars are low-dimensional terms                   head; hence, we adopt a non-parametric approach. Nearest-
dependent on the scene as a whole and are not affected                    neighbor upsampling provides a simple solution, but it does
much by local variations in the scene. Therefore, we uti-                 not respect boundaries while upsampling. To ensure non-
lize the global features Fg from Sec. 4.1 to estimate s and               parametric upsampling while respecting inter-object bound-
t. Theoretically, the metric and relative depth are related               aries, we utilize the predicted relative depth Drel .
           Drel                   Drel
                                   r            Drel
                                                 r [pr + δp ]                    θ1           θ2

                                                                               p11             p12               G(p11 , p12 )
                                                                       ϕ1
   r p                           pr
      r
                                                                       ϕ2      p21             p22
                                                                                                                     G(p21 , p22 )
                                                     W[p]
                            !
                   − Drel [p]         SoftMax                                          (a)                             (b)

                                                                      Figure 5. Motivation for RoPE-ϕ. We show the difference
           Sr          Sr [pr + δp]                  S[p]             between (a) the pixel distance in ERP and (b) the correspond-
                                                                      ing geodesic distance on the curvature of the sphere. Although
          pr                                     p                    |p11 − p12 | = |p21 − p22 | in the ERP, we see that G(p11 , p12 ) <
                                                                      G(p21 , p22 ) on the sphere. Geodesic distance respects the actual
                                                                      separation in the 3D space. Thus, we modify 2D-RoPE to reflect
                                                                      the geodesic distance to get RoPE-ϕ.

Figure 4. Depth-Guided Upsampling. We leverage the pre-
dicted relative depth Drel as a guide to upsample the predicted         The final metric depth Dm is then estimated using the
                                  H  W
low-resolution scale map Sr ∈ R r × r to get S ∈ RH×W . We            Hadamard product ⊙ as follows:
            rel
compare D and its downsampled version Dr to get the local in-
formation in the form of weights W ∈ RH×W ×9 . We compare                                    Dm = S ⊙ Drel + t.                      (8)
the spatial mapping between S and Sr and combine it with W to
obtain S. The Depth-Guided Upsampling is non-parametric and
thus does not add computational overhead.
                                                                      4.3. RoPE-ϕ
                                                                      We take a step back and observe the encoder E. E employs
                                                                      2D-RoPE as the positional embedding scheme as defined
4.2.2. Depth-Guided Upsampling                                        in Sec. 3.2. The 2D-RoPE design ensures the relative posi-
The relative depth map Drel already has local boundary in-            tional embedding is dependent solely on the pixel locations
formation, which we leverage as a guide to upsample Sr .              p = [u, v]. While this is desired for tasks involving per-
We first obtain a low-resolution relative depth map Drel
                                                      r by
                                                                      spective images, it is not suitable for ERP representation,
applying median pooling on Drel with a kernel size and a              which encodes spherical data. ERP is a 2D representation
stride of r. Thus, every pixel p = [u, v] in Drel would               of the surface of the sphere. The pixel distance in ERP is
                                                  u     v
be mapped to pixel pr in Drelr such that pr = [⌊ r ⌋, ⌊ r ⌋].
                                                                      the warped distance between points on the curvature of a
                                              2                       sphere, referred to as the geodesic distance. We propose
Then, with a neighborhood Ω = {−1, 0, 1} we obtain a
distance matrix ∆ ∈ RH×W ×9 defined as follows:                       RoPE-ϕ, an enhanced 2D-RoPE that respects the geodesic
                                                                      distance while applying the rotations in 2D-RoPE.
    ∆[p] = {|Drel [p] − Drel
                         r [pr + δp ]| : ∀ δp ∈ Ω}.             (6)      Every pixel in an ERP denotes a direction in the 3D
                                                                      space. Specifically, given an ERP image I ∈ RH×W ×3 , a
We apply softmax for every pixel over the negative dis-               pixel pn = {un , vn } denotes direction {θn = uHn , ϕn =
tance values in ∆ to get a per-pixel weight map such that             vn
                                                                      W }, where θn , ϕn are the longitude and latitude respec-
W[p] = softmax(−∆[p]) ∈ RH×W ×9 . ∆ and W                             tively. Given two pixels {p1 , p2 } = {{θ1 , ϕ1 }, {θ2 , ϕ2 }}
contain the pseudo mapping from low-resolution data (Dr )             in I, and ∆θ = |θ1 − θ2 |; ∆ϕ = |ϕ1 − ϕ2 |, their geodesic
to high-resolution data (D). We use this information as               distance on unit-sphere G(p1 , p2 ) is defined as:
the routing signal to get the high-resolution scale data S
from low-resolution scale data Sr . Finally, the scalar map            G(p1 , p2 ) = arccos(sin ϕ1 sin ϕ2 +cos ϕ1 cos ϕ2 ∆θ). (9)
S is calculated as the weighted summation over the low-
resolution scales as follows:                                         We observe from Eq. (9) that when ∆θ = 0, i.e., when
                                                                      the pixels are along the same longitude, G ∝ ∆ϕ, aligning
                  S[p] = W[p, :]⊺ N (Sr , pr ),                 (7)   with 2D-RoPE design. However, when ∆ϕ = 0, i.e., when
                                                                      the pixels are along the same latitude, we can approximate
where, N (Sr , pr ) = {Sr [pr + δp ] : ∀ δp ∈ Ω} is the               that G ∝ cos ϕ∆θ. In other words, given a pair of pixels
neighborhood extractor.                                               on the same latitude ϕ and fixed longitudinal distance ∆θ,
the geodesic distance reduces as we move towards the pole,     Baselines. We compare UniDAC to the following works:
even though the pixel distance in ERP remains the same, as     • UniK3D [41]: A SoTA method in zero-shot MMDE that
shown in Fig. 5. With this observation, we add a latitude-        does not require any camera parameters in inference.
based cosine weighting to the 2D-RoPE and modify the ro-       • DAC [19]: A SoTA method for cross-camera generaliza-
tation matrix R in Eq. (3) to get Rϕ as follows:                  tion that is trained only on perspective images. DACI ,
                                                                  DACO denote models trained on indoor and outdoor
  Rϕ [n] = R[n]w(ϕn ) ; w(ϕ) = δ + (1 − δ) cos ϕ,      (10)       datasets, respectively. DACU denotes a model trained
where δ controls the attenuation of weight towards the poles      from scratch on combined indoor and outdoor datasets.
such that w(ϕ) ∈ [δ, 1].                                          Since it was not released by [19], we train it using the
                                                                  same setup as our method for a fair comparison.
4.4. Optimization                                              We additionally include UniDepth [40] and Met-
We train UniDAC by optimizing relative depth loss Lrel and     ric3Dv2 [23] evaluated in DAC [19] for comparison.
metric depth loss Lm on the predicted relative depth map       Evaluation Metrics. We employ standard metrics in
Drel and metric depth map Dm , respectively. The losses        MMDE, i.e., percentage of inliers (δi ↑) with a threshold
Lrel , Lm are both SIlog loss widely in MMDE. Given pre-       of 1.25i , absolute mean relative error (A.Rel ↓), and root
dicted depth map D and corresponding ground-truth depth        mean squared error (RMSE ↓).
map D̄, we estimate the logarithmic error ϵp = ln D̄[p] −
ln D[p]. The SIlog is then computed as follows:                Implementation. We implement UniDAC in PyTorch [38]
                 v                                             and CUDA [36]. We initialize ViT-L [7] backbone with
                                               !2
                                                               DINO [53] pre-trained weights as our encoder and use
                 u
                 u1 X             λ X
       LSI log =              2
                         (ϵp ) − 2        (ϵp ) .     (11)     DPT [45] as our decoder. We utilize the AdamW optimizer
                 t
                   n p           n      p                      initialized with hyperparameters β1 = 0.9, β2 = 0.999,
Using expectation E and variance V, we rearrange Eq. (11)      and an initial learning rate of 0.0001. Cosine Annealing,
to get the following:                                          proposed by [33], is employed as the learning rate sched-
                      q                                        uler with the final learning rate set to one-tenth of the initial
             LSI log = V[ϵp ] + (1 − λ)E2 [ϵp ].     (12)      learning rate. We train the model for 120k iterations with a
                                                               batch size of 128. We follow the training setup of [19] and
We can observe from Eq. (12) that by setting λ = 1 we          apply FoV-alignment, multi-resolution sampling, and ERP
get a purely scale-invariant loss. The standard SIlog used     augmentations. All ablations are performed by training on
in MMDE sets the λ = 0.85 allowing a mixture of scale-         HM3D and KITTI-360 datasets using the ViT-B backbone.
invariant and scale-variant components. We utilize this ob-
servation to define the losses Lrel and Lm as follows:         5.2. Comparison with SoTA
              Lrel = Lλ=1            λ=0.85                    Tab. 1 compares UniDAC with [19, 23, 40, 41] in univer-
                      SI log ; Lm = LSI log .          (13)
                                                               sal domain robustness on large FoV datasets. We observe
5. Experiments                                                 that UniDAC outperforms all the prior methods trained with
                                                               perspective images on both indoor and outdoor datasets and
5.1. Setup                                                     sets the SoTA in cross-camera generalization. UniK3D’s
                                                               [41] training set contains images from large FoV cam-
Training Datasets. Our training set comprises three indoor     eras, and thus does not constitute a fair comparison to the
and four outdoor datasets captured from perspective cam-       other methods trained only on perspective images. How-
eras. The indoor datasets consist of HM3D [43], Hyper-         ever, UniDAC still outperforms UniK3D [41], demonstrat-
sim [47], and Taskonomy [68], while the outdoor datasets       ing the strong generalization prowess of UniDAC. We omit
consists of DDAD [17], LYFT [22], Argoverse2 [59], and         the evaluation on Matterport3D [5] from Tab. 1 since it is
A2D2 [16]. We use the tiny version of HM3D and Taskon-         present in the training set of [41] and would be an unfair
omy provided by OmniData [9] to streamline training. We        comparison to other methods.
exclude images of rear-center camera in A2D2 and front-
                                                                  We observe from Tab. 1 that UniDAC achieves ∼26%
camera in Argoverse2 as explained in Sec. 7.1. Altogether,
                                                               improvement in δ1 metric in the ScanNet++ dataset com-
the training set comprises 1.1M perspective images; 670K
                                                               pared to both UniK3D and DACU . While we improve the
from indoor datasets and 780K from outdoor datasets.
                                                               Pano3D-GV2 by ∼8.4% over DACU , we achieve similar
Testing Datasets. We evaluate the cross-camera general-        performance as that of UniK3D. As mentioned previously,
ization of UniDAC on two fisheye datasets, namely, Scan-       UniK3D contains Matterport3D, a 360◦ dataset similar to
Net++ [63] and KITTI-360 [31], and two 360◦ datasets,          Pano3D-GV2, and we still come close to UniK3D on the
namely, Pano3D-GV2 [2] and Matterport3D [5].                   Pano3D-GV2 dataset, demonstrating the robustness of our
Table 1. Zero-shot evaluation of universal domain robustness. We evaluate all unified methods on a zero-shot setting across both indoor
and outdoor domains. All models are trained on a mix of indoor and outdoor datasets. UniK3D is trained on large FoV images, while the
rest of the methods are only trained on perspective images. [Key: Best, Second Best, S: Swin-L [32], V: ViT-L [7]]

                           Dataset             ScanNet++                       Pano3D-GV2                            KITTI-360
    Methods
                            Size       δ1 ↑     A.Rel ↓ RMSE ↓        δ1 ↑       A.Rel ↓ RMSE ↓            δ1 ↑      A.Rel ↓ RMSE ↓
    UniK3D [41] - V         7.94M      0.651    0.253      0.285     0.785       0.170         0.400       0.817       0.244          2.400
    Metric3Dv2 [23] - V    16.20M     0.536     0.223      0.895      0.404      0.307         0.855      0.716       0.200           4.580
    UniDepth [40] - V       3.83M     0.364     0.497      1.166      0.247      0.789         1.268      0.481       0.294           6.564
    DACU [19] - S           0.79M     0.658     0.233      0.464      0.684      0.203         0.507      0.708       0.186           5.079
    UniDAC- V               1.45M     0.918     0.097      0.277      0.768      0.161         0.394      0.836       0.141           3.977

Table 2. Zero-shot evaluation of cross-camera generalization. We evaluate all methods on a zero-shot setting across diverse cameras.
*I , *O indicate models trained only on the indoor and outdoor datasets, respectively. [Key: Best, Second Best, R: ResNet101 [20], S:
Swin-L [32], V: ViT-L [7]]

                          ScanNet++                    Pano3D-GV2                      Matterport3D                          KITTI-360
 Methods
                   δ1 ↑    A.Rel ↓ RMSE ↓       δ1 ↑     A.Rel ↓ RMSE ↓        δ1 ↑     A.Rel ↓ RMSE ↓             δ1 ↑      A.Rel ↓ RMSE ↓
 DACI [19] - R    0.852    0.132      0.309    0.812     0.139     0.478       0.773      0.156        0.619       0.082      0.464      10.046
 DACI [19] - S    0.854    0.128      0.287    0.729     0.184     0.483       0.723      0.179        0.591       0.245      0.365       9.508
 DACO [19] - R    0.256    0.901      2.312    0.340     0.616     1.713       0.390      0.548        1.630       0.786      0.156       4.361
 DACO [19] - S    0.109    1.412      3.539    0.323     0.870     2.056       0.330      0.924        2.164       0.822      0.149       3.751
 DACU [19] - S   0.658     0.233     0.464     0.684     0.203     0.507       0.662     0.215         0.662      0.708       0.186      5.079
 UniDAC- V       0.918     0.097     0.277     0.768     0.161     0.394       0.745     0.175         0.442      0.836       0.141      3.977

method. We outperform prior methods on KITTI-360, in-                 Table 3. Ablation on Scale Estimation. We study the impact of
cluding UniK3D by ∼2%, even though [41] contains aiMo-                depth-guided scale estimation by comparing it against single-scale
tive [34], an outdoor fisheye dataset in its training set.            estimation. The model performances are compared in a zero-shot
                                                                      setting. ‘-’ indicates we directly estimate metric depth without
5.2.1. Comparison with DAC                                            decoupling relative depth and metric scale. [Key: Best]

Tab. 2 compares UniDAC against unified and domain spe-                                         ScanNet++                      KITTI-360
                                                                       Scale
cific DAC models across all testing datasets. As expected,                              δ1 ↑    A.Rel ↓ RMSE ↓        δ1 ↑    A.Rel ↓ RMSE ↓
DACI [19] and DACO [19] performance drops catastroph-                  −               0.782      0.152    0.401     0.563     0.286      5.461
ically when evaluated using outdoor and indoor datasets,               s∈R             0.773      0.166    0.426     0.601     0.245      5.257
                                                                       S ∈ RH×W        0.792      0.140    0.396     0.622     0.239      5.057
respectively. Although DACU [19] is trained on both indoor
and outdoor data, it fails to generalize well since it tries
to learn a single global scale for both domains. UniDAC               and direct metric-depth estimation without decoupling. For
outperforms DACU , consistently and significantly across in-          direct metric-depth estimation, we remove the scale esti-
door and outdoor domains, underscoring the effect of de-              mation module and use the decoder’s output as the metric
coupling metric depth into relative and scale estimation.             depth. We keep the relative depth estimation architecture
    In addition to outperforming DACU , Tab. 2 shows that             the same, but replace the Depth-Guided Scale estimation
UniDAC outperforms DACI on ScanNet++. Although                        module with a single scalar estimation. We follow [57] and
UniDAC beats DACI with the Swin backbone on Pano3D-                   utilize the [CLS] token from the global features Fg of the
GV2 and Matterport3D, we fall short of beating DACI with              encoder. We estimate the scale as s = MLP(Fg [CLS]) ∈
the ResNet backbone. We believe this is because transform-            R, where MLP is a shallow fully-connected network.
ers struggle with scale equivariance as noted in [19]. While              Tab. 3 shows that directly predicting metric depth per-
comparing between transformer backbones, i.e., Swin and               forms well on ScanNet++ but fails on KITTI-360. This
ViT, we outperform DACI on Pano3D-GV2 and Matter-                     is due to strong indoor bias in the ablation data: HM3D
port3D with ∼4% and ∼2.2% respectively.                               (310K) vs. DDAD (80K). Predicting a scale map S gives
                                                                      2% performance gain over single-scale and thus validates
5.3. Ablation Studies
                                                                      our approach.
Impact of Scale Map. We analyze the benefits of scale                 Impact of RoPE-ϕ. We evaluate the impact of our pro-
map estimation by comparing with single-scale estimation              posed distortion-aware positional embedding RoPE-ϕ by
 ScanNet++ [63]

 Pano3D-GV2 [2]

 KITTI-360 [31]

            RGB & GT                      DACU [19]                      UniK3D [41]                       UniDAC []

Figure 6. Qualitative Results. Every pair of consecutive rows corresponds to a single sample. Odd rows display the input RGB image, and
A.Rel error between predicted and GT depth maps. Even rows display the GT depth map and predicted depth maps. UniDAC reduces error
in the distorted region as seen around the table in ScanNet++ compared to DACU and on the walls in Pano3D-GV2 compared to UniK3D.

comparing it with 2D RoPE defined in Sec. 3.2. We can ob-             6. Conclusion
serve from Eq. (10) that simply setting δ = 1 would give us
2D RoPE, thus indicating that 2D RoPE is a special case of            We presented UniDAC, a unified framework for monocular
                                                                      metric depth estimation that universally generalizes across
RoPE-ϕ. We observe from Tab. 4 that ScanNet++ benefits
                                                                      diverse camera models and scene domains using a single
from RoPE-ϕ more than KITTI-360. We believe that this
is because KITTI-360 contains valid depth along a narrow              model. By decoupling metric depth into relative depth and
band around close to the equator as opposed to ScanNet++,             scale map, we enable robust estimation across indoor and
which provides a dense-depth map spanning a large FoV.                outdoor domains with a single model. Our proposed Depth-
                                                                      Guided Scale Estimation effectively fuses global and local
Table 4. Ablation on RoPE. We evaluate the benefit of RoPE-ϕ,         information to produce scale-aware predictions with min-
comparing it against a model trained with 2D RoPE. The model          imal overhead. Furthermore, we introduced RoPE-ϕ, a
performances are compared in a zero-shot setting. [Key: Best]         distortion-aware positional encoding tailored for ERP im-
                                                                      ages, enhancing the model’s performance on large FoV
                    ScanNet++                 KITTI-360               images. Extensive experiments demonstrate that UniDAC
 Pos. Emb
             δ1 ↑    A.Rel ↓ RMSE ↓    δ1 ↑   A.Rel ↓ RMSE ↓
                                                                      achieves state-of-the-art performance in cross-camera and
 RoPE       0.750    0.177   0.452    0.592    0.254    5.313
 RoPE-ϕ     0.792    0.140   0.396    0.622    0.239    5.057
                                                                      cross-domain generalization, establishing a strong founda-
                                                                      tion for scalable and universal depth perception systems.
References                                                            [11] Hao Feng, Wendi Wang, Jiajun Deng, Wengang Zhou, Li Li,
                                                                           and Houqiang Li. Simfir: A simple framework for fisheye
 [1] Hao Ai, Zidong Cao, Yan-Pei Cao, Ying Shan, and Lin                   image rectification with self-supervised representation learn-
     Wang. Hrdfuse: Monocular 360° depth estimation by collab-             ing. In IEEE/CVF International Conference on Computer
     oratively learning holistic-with-regional depth distributions.        Vision, ICCV 2023, Paris, France, October 1-6, 2023, 2023.
     In IEEE/CVF Conference on Computer Vision and Pattern                 3
     Recognition, CVPR 2023, Vancouver, BC, Canada, June 17-          [12] Xiao Fu, Wei Yin, Mu Hu, Kaixuan Wang, Yuexin Ma, Ping
     24, 2023, 2023. 3                                                     Tan, Shaojie Shen, Dahua Lin, and Xiaoxiao Long. Geowiz-
 [2] Georgios Albanis, Nikolaos Zioulis, Petros Drakoulis,                 ard: Unleashing the diffusion priors for 3d geometry esti-
     Vasileios Gkitsas, Vladimiros Sterzentsenko, Federico Al-             mation from a single image. In European Conference on
     varez, Dimitrios Zarpalas, and Petros Daras. Pano3d: A                Computer Vision, pages 241–258. Springer, 2024. 1
     holistic benchmark and a solid baseline for 360deg depth         [13] Suchisrit Gangopadhyay, Jung-Hee Kim, Xien Chen, Patrick
     estimation. In Proceedings of the IEEE/CVF Conference                 Rim, Hyoungseob Park, and Alex Wong. Extending foun-
     on Computer Vision and Pattern Recognition, pages 3727–               dational monocular depth estimators to fisheye cameras with
     3737, 2021. 6, 8, 1, 3, 5                                             calibration tokens. In Proceedings of the IEEE/CVF Inter-
 [3] Shariq Farooq Bhat, Ibraheem Alhashim, and Peter Wonka.               national Conference on Computer Vision, pages 5198–5209,
     Adabins: Depth estimation using adaptive bins. In Proceed-            2025. 3
     ings of the IEEE/CVF conference on computer vision and           [14] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we
     pattern recognition, pages 4009–4018, 2021. 1                         ready for autonomous driving? the kitti vision benchmark
 [4] Holger Caesar, Varun Bankiti, Alex H Lang, Sourabh Vora,              suite. In 2012 IEEE conference on computer vision and pat-
     Venice Erin Liong, Qiang Xu, Anush Krishnan, Yu Pan, Gi-              tern recognition, pages 3354–3361. IEEE, 2012. 2
     ancarlo Baldan, and Oscar Beijbom. nuscenes: A multi-            [15] Christopher Geyer and Kostas Daniilidis. A unifying theory
     modal dataset for autonomous driving. In Proceedings of               for central panoramic systems and practical implications. In
     the IEEE/CVF conference on computer vision and pattern                European conference on computer vision, pages 445–461.
     recognition, pages 11621–11631, 2020. 2                               Springer, 2000. 1, 2
 [5] Angel Chang, Angela Dai, Thomas Funkhouser, Maciej               [16] Jakob Geyer, Yohannes Kassahun, Mentar Mahmudi,
     Halber, Matthias Niessner, Manolis Savva, Shuran Song,                Xavier Ricou, Rupesh Durgesh, Andrew S Chung, Lorenz
     Andy Zeng, and Yinda Zhang. Matterport3d: Learning                    Hauswald, Viet Hoang Pham, Maximilian Mühlegg, Sebas-
     from rgb-d data in indoor environments. arXiv preprint                tian Dorn, et al. A2d2: Audi autonomous driving dataset.
     arXiv:1709.06158, 2017. 6, 1                                          arXiv preprint arXiv:2004.06320, 2020. 6, 1
 [6] Xingshuai Dong, Matthew A Garratt, Sreenatha G Ana-              [17] Vitor Guizilini, Rares Ambrus, Sudeep Pillai, Allan Raven-
     vatti, and Hussein A Abbass. Towards real-time monocular              tos, and Adrien Gaidon. 3d packing for self-supervised
     depth estimation for robotics: A survey. IEEE Transactions            monocular depth estimation.         In Proceedings of the
     on Intelligent Transportation Systems, 23(10):16940–16961,            IEEE/CVF conference on computer vision and pattern
     2022. 1                                                               recognition, pages 2485–2494, 2020. 6, 1
                                                                      [18] Vitor Guizilini, Igor Vasiljevic, Dian Chen, Rares, Ambrus, ,
 [7] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,
                                                                           and Adrien Gaidon. Towards zero-shot scale-aware monocu-
     Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,
                                                                           lar depth estimation. In Proceedings of the IEEE/CVF Inter-
     Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-
                                                                           national Conference on Computer Vision, pages 9233–9243,
     vain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image is
                                                                           2023. 1, 2, 3
     worth 16x16 words: Transformers for image recognition at
                                                                      [19] Yuliang Guo, Sparsh Garg, S Mahdi H Miangoleh, Xinyu
     scale. In International Conference on Learning Representa-
                                                                           Huang, and Liu Ren. Depth any camera: Zero-shot metric
     tions (ICLR). OpenReview.net, 2021. 6, 7
                                                                           depth estimation from any camera. In Proceedings of the
 [8] Ruofei Du, Eric Turner, Maksym Dzitsiuk, Luca Prasso, Ivo             Computer Vision and Pattern Recognition Conference, pages
     Duarte, Jason Dourgarian, Joao Afonso, Jose Pascoal, Josh             26996–27006, 2025. 2, 3, 6, 7, 8, 1, 4, 5
     Gladstone, Nuno Cruces, et al. Depthlab: Real-time 3d in-        [20] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     teraction with depth maps for mobile augmented reality. In            Deep residual learning for image recognition. In Proceed-
     Proceedings of the 33rd Annual ACM Symposium on User                  ings of the IEEE conference on computer vision and pattern
     Interface Software and Technology, pages 829–843, 2020. 1             recognition, pages 770–778, 2016. 7
 [9] Ainaz Eftekhar, Alexander Sax, Jitendra Malik, and Amir          [21] Byeongho Heo, Song Park, Dongyoon Han, and Sangdoo
     Zamir. Omnidata: A scalable pipeline for making multi-                Yun. Rotary position embedding for vision transformer. In
     task mid-level vision datasets from 3d scans. In Proceedings          European Conference on Computer Vision, pages 289–305.
     of the IEEE/CVF International Conference on Computer Vi-              Springer, 2024. 3, 2
     sion, pages 10786–10796, 2021. 6                                 [22] John Houston, Guido Zuidhof, Luca Bergamini, Yawei
[10] David Eigen, Christian Puhrsch, and Rob Fergus. Depth map             Ye, Long Chen, Ashesh Jain, Sammy Omari, Vladimir
     prediction from a single image using a multi-scale deep net-          Iglovikov, and Peter Ondruska. One thousand and one hours:
     work. Advances in neural information processing systems,              Self-driving motion prediction dataset. In Conference on
     27, 2014. 1                                                           Robot Learning, pages 409–418. PMLR, 2021. 6, 1
[23] Mu Hu, Wei Yin, Chi Zhang, Zhipeng Cai, Xiaoxiao Long,           [35] Christopher Mei and Patrick Rives. Single view point om-
     Hao Chen, Kaixuan Wang, Gang Yu, Chunhua Shen, and                    nidirectional camera calibration from planar grids. In Pro-
     Shaojie Shen. Metric3d v2: A versatile monocular geomet-              ceedings 2007 IEEE International Conference on Robotics
     ric foundation model for zero-shot metric depth and surface           and Automation, pages 3945–3950. IEEE, 2007. 1, 2
     normal estimation. IEEE Transactions on Pattern Analysis         [36] John Nickolls, Ian Buck, Michael Garland, and Kevin
     and Machine Intelligence, 46(12):10579–10596, 2024. 1, 2,             Skadron. Scalable parallel programming with cuda: Is cuda
     3, 6, 7                                                               the parallel programming model that application developers
[24] Hualie Jiang, Zhe Sheng, Siyu Zhu, Zilong Dong, and Rui               have been waiting for? Queue, 6(2):40–53, 2008. 6
     Huang. Unifuse: Unidirectional fusion for 360° panorama          [37] Dennis Park, Rares Ambrus, Vitor Guizilini, Jie Li, and
     depth estimation. IEEE Robotics Autom. Lett., 2021. 3                 Adrien Gaidon. Is pseudo-lidar needed for monocular 3d
[25] Juho Kannala and Sami S Brandt. A generic camera model                object detection? In Proceedings of the IEEE/CVF Inter-
     and calibration method for conventional, wide-angle, and              national Conference on Computer Vision, pages 3142–3152,
     fish-eye lenses. IEEE transactions on pattern analysis and            2021. 1
     machine intelligence, 28(8):1335–1340, 2006. 1                   [38] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer,
[26] Bingxin Ke, Anton Obukhov, Shengyu Huang, Nando Met-                  James Bradbury, Gregory Chanan, Trevor Killeen, Zeming
     zger, Rodrigo Caye Daudt, and Konrad Schindler. Repurpos-             Lin, Natalia Gimelshein, Luca Antiga, et al. Pytorch: An im-
     ing diffusion-based image generators for monocular depth              perative style, high-performance deep learning library. Ad-
     estimation. In Proceedings of the IEEE/CVF Conference on              vances in neural information processing systems, 32, 2019.
     Computer Vision and Pattern Recognition, 2024. 1, 2                   6
[27] Bingxin Ke, Kevin Qu, Tianfu Wang, Nando Metzger,                [39] Luigi Piccinelli, Christos Sakaridis, and Fisher Yu. idisc: In-
     Shengyu Huang, Bo Li, Anton Obukhov, and Konrad                       ternal discretization for monocular depth estimation. In Pro-
     Schindler. Marigold: Affordable adaptation of diffusion-              ceedings of the IEEE/CVF Conference on Computer Vision
     based image generators for image analysis. arXiv preprint             and Pattern Recognition, pages 21477–21487, 2023. 1, 2
     arXiv:2505.09358, 2025. 1                                        [40] Luigi Piccinelli, Yung-Hsu Yang, Christos Sakaridis, Mattia
[28] Tobias Koch, Lukas Liebel, Friedrich Fraundorfer, and                 Segu, Siyuan Li, Luc Van Gool, and Fisher Yu. Unidepth:
     Marco Korner. Evaluation of cnn-based single-image depth              Universal monocular metric depth estimation. In Proceed-
     estimation methods. In Proceedings of the European Con-               ings of the IEEE/CVF Conference on Computer Vision and
     ference on Computer Vision (ECCV) Workshops, pages 0–0,               Pattern Recognition, pages 10106–10116, 2024. 1, 2, 3, 6, 7
     2018. 2                                                          [41] Luigi Piccinelli, Christos Sakaridis, Mattia Segu, Yung-
[29] Jin Han Lee, Myung-Kyu Han, Dong Wook Ko, and                         Hsu Yang, Siyuan Li, Wim Abbeloos, and Luc Van Gool.
     Il Hong Suh. From big to small: Multi-scale local planar              Unik3d: Universal camera monocular 3d estimation. In Pro-
     guidance for monocular depth estimation. arXiv preprint               ceedings of the Computer Vision and Pattern Recognition
     arXiv:1907.10326, 2019. 1                                             Conference, pages 1028–1039, 2025. 2, 3, 6, 7, 8, 1, 4, 5
[30] Yuyan Li, Yuliang Guo, Zhixin Yan, Xinyu Huang, Ye Duan,         [42] Luigi Piccinelli, Christos Sakaridis, Yung-Hsu Yang, Mat-
     and Liu Ren. Omnifusion: 360 monocular depth estima-                  tia Segu, Siyuan Li, Wim Abbeloos, and Luc Van Gool.
     tion via geometry-aware fusion. In IEEE/CVF Conference                Unidepthv2: Universal monocular metric depth estimation
     on Computer Vision and Pattern Recognition, CVPR 2022,                made simpler, 2025. 1, 2, 3
     New Orleans, LA, USA, June 18-24, 2022, 2022. 3                  [43] Santhosh K Ramakrishnan, Aaron Gokaslan, Erik Wijmans,
[31] Yiyi Liao, Jun Xie, and Andreas Geiger. Kitti-360: A novel            Oleksandr Maksymets, Alex Clegg, John Turner, Eric Un-
     dataset and benchmarks for urban scene understanding in 2d            dersander, Wojciech Galuba, Andrew Westbury, Angel X
     and 3d. IEEE Transactions on Pattern Analysis and Machine             Chang, et al. Habitat-matterport 3d dataset (hm3d): 1000
     Intelligence, 45(3):3292–3310, 2022. 6, 8, 1, 2, 3                    large-scale 3d environments for embodied ai. arXiv preprint
[32] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng                arXiv:2109.08238, 2021. 6, 1
     Zhang, Stephen Lin, and Baining Guo. Swin transformer:           [44] René Ranftl, Katrin Lasinger, David Hafner, Konrad
     Hierarchical vision transformer using shifted windows. In             Schindler, and Vladlen Koltun. Towards robust monocular
     Proceedings of the IEEE/CVF international conference on               depth estimation: Mixing datasets for zero-shot cross-dataset
     computer vision, pages 10012–10022, 2021. 7                           transfer. IEEE transactions on pattern analysis and machine
[33] Ilya Loshchilov and Frank Hutter.           Sgdr: Stochas-            intelligence, 44(3):1623–1637, 2020. 1, 2
     tic gradient descent with warm restarts. arXiv preprint          [45] René Ranftl, Alexey Bochkovskiy, and Vladlen Koltun. Vi-
     arXiv:1608.03983, 2016. 6                                             sion transformers for dense prediction. In Proceedings of
[34] Tamas Matuszka, Ivan Barton, Ádám Butykai, Péter Hajas,            the IEEE/CVF international conference on computer vision,
     Dávid Kiss, Domonkos Kovács, Sándor Kunsági-Máté, Péter        pages 12179–12188, 2021. 6
     Lengyel, Gábor Németh, Levente Pető, Dezső Ribli, Dávid     [46] Manuel Rey, Mingze Yuan Area, and Christian Richardt.
     Szeghy, Szabolcs Vajna, and Balint Viktor Varga. aimotive             360monodepth: High-resolution 360 monocular depth esti-
     dataset: A multimodal dataset for robust autonomous driving           mation. in 2022 ieee. In CVF Conference on Computer Vi-
     with long-range perception. In International Conference on            sion and Pattern Recognition (CVPR), 2022. 3
     Learning Representations 2023 Workshop on Scene Repre-           [47] Mike Roberts, Jason Ramapuram, Anurag Ranjan, Atulit
     sentations for Autonomous Driving, 2023. 7                            Kumar, Miguel Angel Bautista, Nathan Paczan, Russ Webb,
     and Joshua M. Susskind. Hypersim: A photorealistic syn-        [59] Benjamin Wilson, William Qi, Tanmay Agarwal, John
     thetic dataset for holistic indoor scene understanding. In          Lambert, Jagjeet Singh, Siddhesh Khandelwal, Bowen
     International Conference on Computer Vision (ICCV) 2021,            Pan, Ratnesh Kumar, Andrew Hartnett, Jhony Kaesemodel
     2021. 6, 1                                                          Pontes, et al. Argoverse 2: Next generation datasets for
[48] Robin Rombach, Andreas Blattmann, Dominik Lorenz,                   self-driving perception and forecasting. arXiv preprint
     Patrick Esser, and Björn Ommer. High-resolution image              arXiv:2301.00493, 2023. 6, 1
     synthesis with latent diffusion models. In Proceedings of      [60] Yuwen Xiong, Zhiqi Li, Yuntao Chen, Feng Wang, Xizhou
     the IEEE/CVF conference on computer vision and pattern              Zhu, Jiapeng Luo, Wenhai Wang, Tong Lu, Hongsheng Li,
     recognition, pages 10684–10695, 2022. 2                             Yu Qiao, Lewei Lu, Jie Zhou, and Jifeng Dai. Efficient de-
[49] Anupa Sabnis and Leena Vachhani. Single image based                 formable convnets: Rethinking dynamic and sparse operator
     depth estimation for robotic applications. In 2011 IEEE Re-         for vision applications. 2024. 3
     cent Advances in Intelligent Computational Systems, pages      [61] Lihe Yang, Bingyi Kang, Zilong Huang, Xiaogang Xu, Jiashi
     102–106. IEEE, 2011. 1                                              Feng, and Hengshuang Zhao. Depth anything: Unleashing
[50] Irawati Nurmala Sari, Weiwei Du, et al. Depth map esti-             the power of large-scale unlabeled data. In Proceedings of
     mation of single-view image using smartphone camera for a           the IEEE/CVF Conference on Computer Vision and Pattern
     3-dimension image generation in augmented reality. In 2023          Recognition, pages 10371–10381, 2024. 1, 2
     Sixth International Symposium on Computer, Consumer and        [62] Lihe Yang, Bingyi Kang, Zilong Huang, Zhen Zhao, Xiao-
     Control (IS3C), pages 167–170. IEEE, 2023. 1                        gang Xu, Jiashi Feng, and Hengshuang Zhao. Depth any-
[51] Zhijie Shen, Chunyu Lin, Kang Liao, Lang Nie, Zishuo                thing v2. Advances in Neural Information Processing Sys-
     Zheng, and Yao Zhao. Panoformer: Panorama transformer               tems, 37:21875–21911, 2024. 1, 2
     for indoor 360$ˆ{\circ }$ depth estimation. In Computer        [63] Chandan Yeshwanth, Yueh-Cheng Liu, Matthias Nießner,
     Vision - ECCV 2022 - 17th European Conference, Tel Aviv,            and Angela Dai. Scannet++: A high-fidelity dataset of 3d in-
     Israel, October 23-27, 2022, Proceedings, Part I, 2022. 3           door scenes. In Proceedings of the IEEE/CVF International
                                                                         Conference on Computer Vision, pages 12–22, 2023. 6, 8, 1,
[52] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob
                                                                         3, 4
     Fergus. Indoor segmentation and support inference from
                                                                    [64] Wei Yin, Jianming Zhang, Oliver Wang, Simon Niklaus,
     rgbd images. In Computer Vision–ECCV 2012: 12th Eu-
                                                                         Long Mai, Simon Chen, and Chunhua Shen. Learning to
     ropean Conference on Computer Vision, Florence, Italy, Oc-
                                                                         recover 3d scene shape from a single image. In Proceed-
     tober 7-13, 2012, Proceedings, Part V 12, pages 746–760.
                                                                         ings of the IEEE/CVF Conference on Computer Vision and
     Springer, 2012. 2
                                                                         Pattern Recognition, pages 204–213, 2021. 1, 2
[53] Oriane Siméoni, Huy V Vo, Maximilian Seitzer, Federico
                                                                    [65] Wei Yin, Chi Zhang, Hao Chen, Zhipeng Cai, Gang Yu,
     Baldassarre, Maxime Oquab, Cijo Jose, Vasil Khalidov,
                                                                         Kaixuan Wang, Xiaozhi Chen, and Chunhua Shen. Metric3d:
     Marc Szafraniec, Seungeun Yi, Michaël Ramamonjisoa,
                                                                         Towards zero-shot metric 3d prediction from a single image.
     et al. Dinov3. arXiv preprint arXiv:2508.10104, 2025. 6
                                                                         In Proceedings of the IEEE/CVF International Conference
[54] Jianlin Su, Murtadha Ahmed, Yu Lu, Shengfeng Pan, Wen               on Computer Vision, pages 9043–9053, 2023. 1, 2, 3
     Bo, and Yunfeng Liu. Roformer: Enhanced transformer with       [66] Weihao Yuan, Xiaodong Gu, Zuozhuo Dai, Siyu Zhu, and
     rotary position embedding. Neurocomputing, 568:127063,              Ping Tan. Neural window fully-connected crfs for monocu-
     2024. 3                                                             lar depth estimation. In Proceedings of the IEEE/CVF con-
[55] Yu-Chuan Su and Kristen Grauman. Learning spherical con-            ference on computer vision and pattern recognition, pages
     volution for fast features from 360° imagery. In Advances in        3916–3925, 2022. 1
     Neural Information Processing Systems 30: Annual Confer-       [67] Ilwi Yun, Chanyong Shin, Hyunku Lee, Hyuk-Jae Lee,
     ence on Neural Information Processing Systems 2017, De-             and Chae-Eun Rhee. Egformer: Equirectangular geometry-
     cember 4-9, 2017, Long Beach, CA, USA, 2017. 3                      biased transformer for 360 depth estimation. In IEEE/CVF
[56] Javier Tirado-Garı́n and Javier Civera. Anycalib: On-               International Conference on Computer Vision, ICCV 2023,
     manifold learning for model-agnostic single-view camera             Paris, France, October 1-6, 2023, 2023. 3
     calibration. In Proceedings of the IEEE/CVF International      [68] Amir R Zamir, Alexander Sax, William Shen, Leonidas J
     Conference on Computer Vision, pages 8044–8055, 2025. 1             Guibas, Jitendra Malik, and Silvio Savarese. Taskonomy:
[57] Ruicheng Wang, Sicheng Xu, Yue Dong, Yu Deng, Jianfeng              Disentangling task transfer learning. In Proceedings of the
     Xiang, Zelong Lv, Guangzhong Sun, Xin Tong, and Jiaolong            IEEE conference on computer vision and pattern recogni-
     Yang. Moge-2: Accurate monocular geometry with metric               tion, pages 3712–3722, 2018. 6, 1
     scale and sharp details. arXiv preprint arXiv:2507.02546,      [69] Shengjie Zhu, Girish Chandar Ganesan, Abhinav Kumar,
     2025. 1, 7                                                          and Xiaoming Liu. Replay: Remove projective lidar
[58] Yan Wang, Wei-Lun Chao, Divyansh Garg, Bharath Hari-                depthmap artifacts via exploiting epipolar geometry. In Eu-
     haran, Mark Campbell, and Kilian Q Weinberger. Pseudo-              ropean Conference on Computer Vision, pages 393–411.
     lidar from visual depth estimation: Bridging the gap in 3d          Springer, 2024. 2
     object detection for autonomous driving. In Proceedings of     [70] Xizhou Zhu, Han Hu, Stephen Lin, and Jifeng Dai. De-
     the IEEE/CVF conference on computer vision and pattern              formable convnets V2: more deformable, better results.
     recognition, pages 8445–8453, 2019. 1                               2019. 3
                UniDAC: Universal Metric Depth Estimation for Any Camera
                                                  Supplementary Material
7. Data                                                               Table 6. Testing Datasets. List of testing datasets with the follow-
                                                                      ing attributes: camera type, scene type, and acquisition method.
7.1. Training Data                                                    [Key: Rec=Mesh reconstruction]

Tab. 5 provides an overview of the training datasets. In ad-
                                                                       Dataset                Cam.Type         Scene      Acquisition
dition to the training datasets utilized in DAC [19], we add
Argoverse2 and A2D2 to balance the indoor and outdoor                  ScanNet++ [63]           Fisheye       Indoor             Rec
distribution in the training set.                                      Matterport3D [5]          ERP          Indoor             Rec
    We observe that out of seven cameras in Argoverse2,                Pano3D-GV2 [2]            ERP          Indoor             Rec
the front camera’s aspect ratio is different than the rest             KITTI-360 [31]           Fisheye       Outdoor           LiDAR
of the six cameras. Specifically, the resolution (H×W) is
1550 × 2048 while the rest of the cameras have a resolution
of 2048 × 1550. Since the aspect ratio of the front camera            both fisheye datasets, they differ in their respective distor-
is less than one, we omit images from the front camera for            tion models. ScanNet++ follows the KB [25] model while
our training. Furthermore, Argoverse2 contains 1.5M sam-              KITTI-360 follows the MEI [35] model. We adopt the
ples, and to prevent introducing bias to outdoor data, we             lookup table provided by DAC for fast fisheye to ERP con-
randomly sample 300K image-depth pairs to complete our                version. Pano3D-GV2 and Matterport3D datasets consist
training set.                                                         of 360◦ images, which are provided in the ERP images by
    A2D2 consists of six cameras, namely, front-center,               default, and therefore we use them as is.
                                                                      Table 7. Effect of camera intrinsics on depth performance.
front-right, front-left, side-right, side-left, and rear-center,
                                                                      We study the impact of utilizing predicted and ground-truth {P,G}
with corresponding LiDAR acquisitions. We exclude the
                                                                      camera intrinsics during inference. [Key: Best, Second Best]
images from the rear-center cameras and add 350K images
                                                                                            ScanNet++                  KITTI-360
obtained from the remaining five cameras to the training set.          Method
                                                                                     δ1 ↑    A.Rel ↓ RMSE ↓     δ1 ↑   A.Rel ↓ RMSE ↓
    We note that UniK3D’s [41] training set consists of                UniK3D       0.651    0.253    0.285    0.817    0.244     2.400
more than 8M samples, whereas our training set consists                UniDAC- P    0.894    0.110    0.274    0.706    0.198     4.397
only 1.45M samples. Moreover, out of the 8M images in                    +A2D2      0.917    0.104    0.279    0.815    0.154     4.091
the training set of UniK3D, 72.4% are perspective images,              UniDAC- G    0.905    0.104    0.274    0.757    0.169     4.470
27.27% are fisheye images, and 0.33% are ERP images. In                  +A2D2      0.918    0.097    0.277    0.836    0.141     3.977
contrast, 100% of UniDAC’s training set consists of per-
spective images as seen in Tab. 5                                     8. Comparison with UniK3D
Table 5. Training Datasets. List of training datasets with the fol-   As mentioned in Sec. 5.2, the comparison with
lowing attributes: number of images, scene type, and acquisition      UniK3D [41] is not fair to UniDAC, since [41] is trained
method. [Key: Syn=Synthetic, Rec=Mesh reconstruction]                 on large-FoV images. However, we note that the compar-
                                                                      ison is also unfair towards [41] since UniDAC requires
 Dataset                   #Images       Scene      Acquisition       ground-truth camera parameters while [41] doesn’t.
 HM3D-tiny [43]              310K       Indoor         Rec               For a fairer comparison, we employ AnyCalib [56], an
 Taskonomy-tiny [68]         300K       Indoor        RGB-D           off-the-shelf camera intrinsics estimation model, and utilize
 Hypersim [47]                54K       Indoor         Syn            the predicted intrinsics for ERP transformations. [56] pre-
 DDAD [17]                    80K       Outdoor       LiDAR           dicts intrinsics for KB [25] and UCM [25] camera models.
 LYFT [22]                    50K       Outdoor       LiDAR           ScanNet++ [63] follows the KB model, whereas KITTI-
 Argoverse2 [59]             300K       Outdoor       LiDAR           360 [31] follows the MEI [35] model, which is not han-
 A2D2 [16]                   350K       Outdoor       LiDAR           dled by [56]. We approximate the MEI [35] model from
                                                                      UCM [15] by setting the distortion parameters to zero.
                                                                         Tab. 7 provides the performance comparison between
                                                                      [41] and UniDAC using predicted and ground-truth intrin-
7.2. Testing Data
                                                                      sics. ‘+A2D2’ denotes adding A2D2 [16] in the training
Tab. 6 details the testing data used to evaluate UniDAC. We           data as detailed in Sec. 7.1. We observe that even under
follow the testing data setup of DAC and evaluate all our             this fairer comparison, we still outperform [41] on Scan-
baselines on them. While ScanNet++ and KITTI-360 are                  Net++ [63]. We attribute the decrease in the performance
Table 8. Zero-shot evaluation on perspective datasets. We evaluate all unified models on perspective datasets. All models are trained on
a mix of indoor and outdoor datasets. [Key: Best]

              Training                KITTI                             NYU-v2                      nuScenes                  IBims-1
 Method
                Size       δ1 ↑      A.Rel ↓ RMSE ↓             δ1 ↑    A.Rel ↓ RMSE ↓       δ1 ↑   A.Rel ↓ RMSE ↓     δ1 ↑   A.Rel ↓ RMSE ↓
 Metric3Dv2     16M       0.974      0.053        2.493      0.972      0.067      0.262    0.841   0.236    9.400    0.684    0.207    0.700
 UniDepth        3M       0.964      0.116        2.788      0.988      0.052      0.194    0.846   0.127    4.560    0.157    0.410    1.250
 UniK3D          8M        0.833      0.159          4.323      0.899      0.133    0.400   0.840    0.189   10.830   0.919   0.104     0.406
 DACU           0.8M       0.767      0.180          5.332      0.816      0.140    0.505   0.631    0.225    8.321   0.808   0.370     1.182
 UniDAC         1.1M       0.872      0.122          3.784      0.934      0.093    0.354   0.801    0.151    6.335   0.845   0.129     0.577

on KITTI-360 [31] to the approximation of predicted in-                            model, they use iDisc [39] for its simplicity and effective-
trinsics from UCM [15] to the MEI [35] model. We believe                           ness. iDisc requires multi-scale features from the encoder
that with better intrinsic estimation models that can handle                       for its pipeline. Since DINO features are at a downscaled
the MEI [35] camera model, UniDAC will retain its perfor-                          resolution, we apply consecutive upsampling via transpose
mance even with predicted intrinsics.                                              convolutions to obtain multi-resolution features.
                                                                                       One of the major differences between DINOv2 and DI-
Table 9. Ablation on Encoder Weight. D2, D3 indicate the ViT                       NOv3 is the positional embedding scheme. DINOv2 uses
encoders have been initialized with DINOv2 and DINOv3 pre-                         additive absolute positional embedding, whereas DINOv3
trained weights, respectively. [Key: Best]
                                                                                   utilizes 2D-RoPE [21]. We do not modify the positional em-
                       ScanNet++                       KITTI-360
                                                                                   bedding scheme of the DINO encoders, and thus the overall
 Method                                                                            performance of DAC and UniDAC is affected by the com-
               δ1 ↑     A.Rel ↓ RMSE ↓         δ1 ↑    A.Rel ↓ RMSE ↓
 DACU - D2    0.368     0.305      0.939      0.334     0.318      6.872           patibility of the positional embeddings with the respective
 DACU - D3    0.707     0.211      0.471      0.428     0.342      5.305           frameworks and the task of large-FoV depth estimation.
 UniDAC- D2   0.533     0.242      0.703      0.445     0.287      6.924
 UniDAC- D3   0.792     0.140      0.396      0.622     0.239      5.057
                                                                                       We observe that utilizing DINOv3 as the encoder gives
                                                                                   the best performance for both DAC and UniDAC. Since we
                                                                                   train on small-FoV perspective images and test on large-
9. Evaluation on Perspective Datasets                                              FoV images, the absolute positional embedding of DINOv2
                                                                                   is not suitable for the task. However, the RoPE in DINOv3
We compare UniDAC against our baselines on four per-                               offers relative positional embedding, thus facilitating gen-
spective datasets, KITTI [14], NYU-v2 [52], IBims-1 [28],                          eralization.
and nuScenes [4]. While [14, 28, 52] provide artifact-                                 iDisc, utilized by DAC, internally uses absolute posi-
free depthmaps in their official dataset, we utilize [69]                          tional embedding for their proposed Internal Discretization
to estimate artifact-free depthmaps for [4]. We observe                            Module. Therefore, the proposed method in UniDAC is
from Tab. 8 that UniDAC outperforms UniK3D and DAC                                 most compatible with the DINOv3 encoder, giving the best
on two important perspective benchmarks, namely, KITTI                             performance. We believe the mismatch between the RoPE
and NYU-v2, demonstrating the generalization capability                            in DINOv3 and the absolute positional embedding in iDisc
of UniDAC even in perspective datasets, beyond large-FoV                           architecture to be one of the reasons for the performance
datasets.                                                                          gap between DAC-D3 and UniDAC-D3.
Table 10. Ablation on Shift Estimation. We study the impact of
                                                                                       We also observe that the performance of DAC-D3 on
depth-guided shift map estimation. [Key: Best]                                     KITTI-360 is quite low compared to UniDAC-D3, under-
                                                                                   scoring the benefit of our proposed depth-guided scale esti-
                      ScanNet++                        KITTI-360
 Shift                                                                             mation module.
              δ1 ↑     A.Rel ↓ RMSE ↓         δ1 ↑     A.Rel ↓ RMSE ↓
 t∈R          0.792    0.140       0.396      0.622     0.239      5.057
 T ∈ RH×W     0.798    0.139       0.393      0.630     0.235      4.985           11. Ablation on Shift Estimation
                                                                                   As mentioned in Sec. 4.2, we estimate a scale map S in-
10. Ablation on Encoder Weights                                                    stead of a 1-D scalar s to adjust for irregularities. How-
                                                                                   ever, we still estimated shift t as a 1-D scalar. Tab. 10
Tab. 9 evaluates the effect of initializing encoders E with                        provides an ablation on estimating a shift scalar and a shift
different pre-trained weights on the model performance. We                         map while keeping scale estimation in the form of a scale
train DACU and UniDAC using DINOv2 and DINOv3 en-                                  map. Formally, we modify the architecture slightly to out-
coders on HM3D and DDAD datasets. While DAC’s pro-                                 put {S, T} ∈ RH×W . As expected, we can observe from
posed framework is compatible with any depth estimation                            Tab. 10 that there is a slight increase in performance by in-
corporating a shift map. However, the improvement from
adopting the shift map is still smaller than the improvement
from adopting the scale map, as seen in Tab. 3.

12. Additional Qualitative results
We provide additional qualitative results on Scan-
Net++ [63], Pano3D-GV2 [2], and KITTI-360 [31] for vi-
sual comparison in Fig. 7, Fig. 8 and Fig. 9 respectively.
          RGB & GT                        DACU [19]                     UniK3D [41]                      UniDAC

Figure 7. Qualitative Results on ScanNet++ [63]. Every pair of consecutive rows corresponds to a single sample. Odd rows display the
input RGB image, and A.Rel error between predicted and GT depth maps. Even rows display the GT depth map and predicted depth maps.
          RGB & GT                        DACU [19]                     UniK3D [41]                      UniDAC

Figure 8. Qualitative Results on Pano3D-GV2 [2]. Every pair of consecutive rows corresponds to a single sample. Odd rows display the
input RGB image, and A.Rel error between predicted and GT depth maps. Even rows display the GT depth map and predicted depth maps.
          RGB & GT                        DACU [19]                     UniK3D [41]                      UniDAC

Figure 9. Qualitative Results on KITTI-360 [31]. Every pair of consecutive rows corresponds to a single sample. Odd rows display the
input RGB image, and A.Rel error between predicted and GT depth maps. Even rows display the GT depth map and predicted depth maps.
