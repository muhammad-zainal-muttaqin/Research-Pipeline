---
source_id: 078
bibtex_key: wen2024foundationpose
title: FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects
year: 2024
domain_theme: Pose 6D
verified_pdf: 78_FoundationPose.pdf
char_count: 141924
---

Model-

                                                                                                                                                                                Model-based tracking

                                            FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects
                                                                                                                                                                                           Model-free tracking

                                                                      Bowen Wen          Wei Yang         Jan Kautz         Stan Birchfield

                                                                                                    NVIDIA
arXiv:2312.08344v2 [cs.CV] 26 Mar 2024

                                                                  Abstract

                                             We present FoundationPose, a unified foundation model
                                         for 6D object pose estimation and tracking, supporting both
                                         model-based and model-free setups. Our approach can be
                                         instantly applied at test-time to a novel object without fine-
                                         tuning, as long as its CAD model is given, or a small num-
                                         ber of reference images are captured. Thanks to the uni-
                                         fied framework, the downstream pose estimation modules
                                         are the same in both setups, with a neural implicit repre-
                                         sentation used for efficient novel view synthesis when no
                                         CAD model is available. Strong generalizability is achieved
                                         via large-scale synthetic training, aided by a large lan-
                                         guage model (LLM), a novel transformer-based architec-
                                         ture, and contrastive learning formulation. Extensive evalu-
                                         ation on multiple public datasets involving challenging sce-
                                         narios and objects indicate our unified approach outper-
                                                                                                            Figure 1. Our unified framework enables both 6D pose estimation and
                                         forms existing methods specialized for each task by a large        tracking for novel objects, supporting the model-based and model-free se-
                                         margin. In addition, it even achieves comparable results           tups. On each of these four tasks, it outperforms prior work specially de-
                                         to instance-level methods despite the reduced assumptions.         signed for the task (• indicates RGB-only; × indicates RGBD, like ours).
                                                                                                            The metric for each task is explained in detail in the experimental results.
                                         Project page: https:// nvlabs.github.io/ FoundationPose/
                                                                                                            considered, depending upon what information is available at
                                                                                                            test time: model-based, where a textured 3D CAD model of
                                         1. Introduction
                                                                                                            the object is provided, and model-free, where a set of refer-
                                         Computing the rigid 6D transformation from the object to           ence images of the object is provided. While much progress
                                         the camera, also known as object pose estimation, is cru-          has been made on both setups individually, there remains a
                                         cial for a variety of applications, such as robotic manipu-        need for a single method to address both setups in a unified
                                         lation [30, 69, 70] and mixed reality [43]. Classic meth-          way, since different real-world applications provide differ-
                                         ods [20, 21, 31, 50, 68] are known as instance-level because       ent types of information.
                                         they only work on the specific object instance determined at          Orthogonal to single-frame object pose estimation, pose
                                         training time. Such methods usually require a textured CAD         tracking methods [8, 29, 36, 39, 56, 63, 67, 72] leverage
                                         model for generating training data, and they cannot be ap-         temporal cues to enable more efficient, smooth and accu-
                                         plied to an unseen novel object at test time. While category-      rate pose estimation on a video sequence. These methods
                                         level methods [5, 34, 60, 64, 75] remove these assumptions         share the similar aforementioned issues to their counterparts
                                         (instance-wise training and CAD models), they are limited          in pose estimation, depending on their assumptions on the
                                         to objects within the predefined category on which they are        object knowledge.
                                         trained. Moreover, obtaining category-level training data is          In this paper we propose a unified framework called
                                         notoriously difficult, in part due to additional pose canoni-      FoundationPose that performs both pose estimation and
                                         calization and examination steps [64] that must be applied.        tracking for novel objects in both the model-based and
                                             To address these limitations, more recent efforts have fo-     model-free setups, using RGBD images. As seen in Fig. 1,
                                         cused on the problem of instant pose estimation of arbitrary       our method outperforms existing state-of-art methods spe-
                                         novel objects [19, 32, 40, 55, 58]. Two different setups are       cialized for each of these four tasks. Our strong gen-
eralizability is achieved via large-scale synthetic training,   the gap between the model-based and model-free scenarios.
aided by a large language model (LLM), as well as a novel       In addition, we focus on generalizable novel object pose es-
transformer-based architecture and contrastive learning. We     timation in this work, which is not the case for [3, 35]. To
bridge the gap between model-based and model-free setups        handle novel objects, Gen6D [40] designs a detection, re-
with a neural implicit representation that allows for effec-    trieval and refinement pipeline. However, to avoid difficul-
tive novel view synthesis with a small number (∼16) of          ties with out-of-distribution test set, it requires fine-tuning.
reference images, achieving rendering speeds that are sig-      OnePose [58] and its extension OnePose++ [19] leverage
nificantly faster than previous render-and-compare meth-        structure-from-motion (SfM) for object modeling and pre-
ods [32, 36, 67]. Our contributions can be summarized as        train 2D-3D matching networks to solve the pose from cor-
follows:                                                        respondences. FS6D [22] adopts a similar scheme and fo-
• We present a unified framework for both pose estimation       cuses on RGBD modality. Nevertheless, reliance on cor-
   and tracking for novel objects, supporting both model-       respondences becomes fragile when applied to textureless
   based and model-free setups. An object-centric neural        objects or under severe occlusion.
   implicit representation for effective novel view synthesis   Object Pose Tracking. 6D object pose tracking aims to
   bridges the gap between the two setups.                      leverage temporal cues to enable more efficient, smooth
• We propose a LLM-aided synthetic data generation              and accurate pose prediction on video sequence. Through
   pipeline which scales up the variety of 3D training assets   neural rendering, our method can be trivially extended
   by diverse texture augmentation.                             to the pose tracking task with high efficiency. Similar
• Our novel design of transformer-based network architec-       to single-frame pose estimation, existing tracking meth-
   tures and contrastive learning formulation leads to strong   ods can be categorized into their counterparts depending
   generalization when trained solely on synthetic data.        on the assumptions of object knowledge. These include
• Our method outperforms existing methods specialized           instance-level methods [8, 11, 36, 67], category-level meth-
   for each task by a large margin across multiple public       ods [39, 63], model-based novel object tracking [29, 56, 72]
   datasets. It even achieves comparable results to instance-   and model-free novel object tracking [66, 71]. Under
   level methods despite reduced assumptions.                   both model-based and model-free setups, we set a new
Code and data developed in this work will be released.          benchmark record across public datasets, even outperform-
                                                                ing state-of-art methods that require instance-level train-
2. Related Work                                                 ing [8, 36, 67].
CAD Model-based Object Pose Estimation. Instance-               3. Approach
level pose estimation methods [20, 21, 31, 50] assume a
textured CAD model is given for the object. Training and        Our system as a whole is illustrated in Fig. 2, showing the
testing is performed on the exact same instance. The object     relationships between the various components, which are
pose is often solved by direct regression [37, 73], or con-     described in the following subsections.
structing 2D-3D correspondences followed by PnP [50, 61],
                                                                3.1. Language-aided Data Generation at Scale
or 3D-3D correspondences followed by least squares fit-
ting [20, 21]. To relax the assumptions about the object        To achieve strong generalization, a large diversity of ob-
knowledge, category-level methods [5, 34, 60, 64, 75, 77]       jects and scenes is needed for training. Obtaining such data
can be applied to novel object instances of the same cate-      in the real world, and annotating accurate ground-truth 6D
gory, but they cannot generalize to arbitrary novel objects     pose, is time- and cost-prohibitive. Synthetic data, on the
beyond the predefined categories. To address this limita-       other hand, often lacks the size and diversity in 3D assets.
tion, recent efforts [32, 55] aim for instant pose estimation   We developed a novel synthetic data generation pipeline
of arbitrary novel objects as long as the CAD model is pro-     for training, powered by the recent emerging resources and
vided at test time.                                             techniques: large scale 3D model database [6, 10], large
Few-shot Model-free Object pose estimation. Model-              language models (LLM), and diffusion models [4, 24, 53].
free methods remove the requirement of an explicit textured     This approach dramatically scales up both the amount and
model. Instead, a number of reference images capturing          diversity of data compared with prior work [22, 26, 32].
the target object are provided [19, 22, 51, 58]. RLLG [3]       3D Assets. We obtain training assets from recent large
and NeRF-Pose [35] propose instance-wise training without       scale 3D databases including Objaverse [6] and GSO [10].
the need of an object CAD model. In particular, [35] con-       For Objaverse [6] we chose the objects from the Objaverse-
structs a neural radiance field to provide semi-supervision     LVIS subset that consists of more than 40K objects belong-
on the object coordinate map and mask. Differently, we          ing to 1156 LVIS [13] categories. This list contains the most
introduce the neural object field built on top of SDF repre-    relevant daily-life objects with reasonable quality, and di-
sentation for efficient RGB and depth rendering to bridge       versity of shapes and appearances. It also provides a tag
             A traditional wooden
             armoire in a rich mahogany
             finish, showcasing
             intricate carvings and
             brass hardware for an
             elegant look

Figure 2. Overview of our framework. To reduce manual efforts for large scale training, we developed a novel synthetic data generation pipeline by
leveraging recent emerging techniques and resources including 3D model database, large language models and diffusion models (Sec. 3.1). To bridge the
                                                                                                                                99.00for subsequent render-
gap between model-free and model-based setup, we leverage an object-centric neural field (Sec. 3.2) for novel view RGBD rendering
and-compare. For pose estimation, we first initialize global poses uniformly around the object, which are then refined by the refinement network (Sec. 3.3).
Finally, we forward the refined poses to the pose selection module which predicts their scores. The pose with the best score is selected as output (Sec. 3.4).

                            Random texture blending                               LLM-aided Texture Augmentation.     97.00  While most Obja-
                                                                                  verse objects have high quality shapes, their texture fidelity
                                                                                  varies significantly. FS6D [22] proposes to augment object
                                                                                  texture by randomly pasting images95.00from ImageNet [7] or
                       A unique wineglass with a
                                                                                  MS-COCO [38]. However, due to the random UV mapping,
                                                                                                                        ADD (%)

                       stem shaped like a                                         this method yields artifacts such as seams on the result-
                       corkscrew, showcasing a                                                                        93.00
                       bowl made of hand‐blown                                    ing textured mesh (Fig. 3 top); and applying holistic scene
                       glass in a mix of swirling
                       red and white                                              images to objects leads to unrealistic results. In contrast,
                                                                                  we explore how recent advances in91.00  large language mod-
                       An artistic wineglass
                       hand‐painted with vibrant
                                                                                  els and diffusion models can be harnessed for more real-
                       strokes of brown, blue,                                    istic (and fully automatic) texture augmentation. Specifi-
                       and green, creating a
                       striking abstract design                                                                       89.00 shape, and a ran-
                                                                                  cally, we provide a text prompt, an object
                                                                                  domly initialized noisy texture to TexFusion [4] to produce
                                                                                  an augmented textured model. Of course, providing such
                      A vibrant red bulb with a
                      gradient of orange and
                                                                                  a prompt manually is not scalable 87.00
                                                                                                                       if we want to augment
                      yellow, emitting a warm glow                                a large number of objects in diverse styles under different
                                                                                  prompt guidance. As a result, we introduce a two-level hi-
Figure 3. Top: Random texture blending proposed in FS6D [22]. Bot-                                                    85.00 in Fig. 2 top-left,
                                                                                  erarchical prompt strategy. As illustrated
tom: Our LLM-aided texture augmentation yields more realistic appear-
                                                                                  we first prompt ChatGPT, asking it to describe the possi- 4
ance. Leftmost is the original 3D assets. Text prompts are automatically
generated by ChatGPT.                                                             ble appearance of an object; this prompt is templated so                       Num
                                                                                  that each time we only need to replace the tag paired with
for each object describing its category, which benefits au-                       the object, which is given by the Objaverse-LVIS list. The
tomatic language prompt generation in the following LLM-                          answer from ChatGPT then becomes the text prompt pro-
aided texture augmentation step.
vided to the diffusion model for texture synthesis. Because                                                                                                                                                           ness of the distribution. The probability peaks at the surface
this approach enables full automation for texture augmenta-                                                                                                                                                           intersection. In Eq. (1), z(r) is the depth value of the ray
tion, it facilitates diversified data generation at scale. Fig. 3                                                                                                                                                     from the depth image, and λ is the truncation distance. We
presents more examples including different stylization for                                                                                                                                                            ignore the contribution from empty space that is more than
the same object.                                                                                                                                                                                                      λ away from the surface for more efficient training, and we
Data Generation. Our synthetic data generation is imple-                                                                                                                                                              only integrate up to a 0.5λ penetrating distance to model
mented in NVIDIA Isaac Sim, leveraging path tracing for                                                                                                                                                               self-occlusion [65]. During training, we compare this quan-
high-fidelity photo-realistic rendering.1 We perform grav-                                                                                                                                                            tity against the reference RGB images for color supervision:
ity and physics simulation to produce physically plausible
scenes. In each scene, we randomly sample objects includ-                                                                                                                                                                                                                                         \mathcal {L}_{c}=\frac {1}{|\mathcal {R}|}\sum _{r\in \mathcal {R}}\left \| c(r)-\bar {c}(r) \right \|_2,                                                                                                                                                                                                                                                                                                              (3)
ing the original and texture-augmented versions. The object
size, material, camera pose, and lighting are also random-                                                                                                                                                            where c̄(r) denotes the ground-truth color at the pixel where
ized; more details can be found in the appendix.                                                                                                                                                                      the ray r passes through.
3.2. Neural Object Modeling
                                                                                                                                                                                                                         For geometry learning, we adopt the hybrid SDF
For the model-free setup, when the 3D CAD model is un-                                                                                                                                                                model [71] by dividing the space into two regions to learn
available, one key challenge is to represent the object to                                                                                                                                                            the SDF, leading to the empty space loss and the near-
effectively render images with sufficient quality for down-                                                                                                                                                           surface loss. We also apply eikonal regularization [12] to
stream modules. Neural implicit representations are both                                                                                                                                                              the near-surface SDF:
effective for novel view synthesis and parallelizable on a
                                                                                                                                                                                                                                                                &\mathcal {L}_{\textit {e}}=\frac {1}{|\mathcal {X}_{\textit {e}}|}\sum _{x\in \mathcal {X}_{\textit {e}}} | \Omega (x)-\lambda |, \\ &\mathcal {L}_{\textit {s}}=\frac {1}{|\mathcal {X}_{\textit {s}}|}\sum _{x\in \mathcal {X}_{\textit {s}}}\left (\Omega (x) +d_x - d_D \right )^2, \\ &\mathcal {L}_{\textit {eik}}=\frac {1}{|\mathcal {X}_{\textit {s}}|}\sum _{x\in \mathcal {X}_{\textit {s}}} ( \left \|\nabla \Omega (x)\right \|_2-1 )^2,
GPU, thus providing high computational efficiency when
rendering multiple pose hypotheses for downstream pose
estimation modules, as shown in Fig. 2. To this end, we
introduce an object-centric neural field representation for
object modeling, inspired by previous work [45, 65, 71, 74].
Field Representation. We represent the object by two                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     (6)
functions [74] as shown in Fig. 2. First, the geometry func-
tion Ω : x 7→ s takes as input a 3D point x ∈ R3 and                                                                                                                                                                  where x denotes a sampled 3D point along the rays in the
outputs a signed distance value s ∈ R. Second, the appear-                                                                                                                                                            divided space; dx and dD are the distance from ray origin
ance function Φ : (fΩ(x) , n, d) 7→ c takes the intermedi-                                                                                                                                                            to the sample point and the observed depth point, respec-
ate feature vector fΩ(x) from the geometry network, a point                                                                                                                                                           tively. We do not use the uncertain free-space loss [71], as
normal n ∈ R3 , and a view direction d ∈ R3 , and outputs                                                                                                                                                             the template images are pre-captured offline in the model-
the color c ∈ R3+ . In practice, we apply multi-resolution                                                                                                                                                            free setup. The total training loss is
hash encoding [45] to x before forwarding to the network.                                                                                                                                                                          \begin {aligned} \mathcal {L}=w_{c}\mathcal {L}_{c}+w_{\textit {e}}\mathcal {L}_{\textit {e}}+w_{\textit {s}}\mathcal {L}_{\textit {s}}+w_{\textit {eik}}\mathcal {L}_{\textit {eik}}. \end {aligned}  (7)
Both n and d are embedded by a fixed set of second-order                                                                                                                                                              The learning is optimized per object without priors and can
spherical harmonic coefficients. The implicit object surface                                                                                                                                                          be efficiently performed within seconds. The neural field
is obtained by taking the zero level set of the signed dis-                                                                                                                                                          only needs to be trained once for a novel object.
tance field (SDF): S = x ∈ R3 | Ω(x) = 0 . Compared
to NeRF [44], the SDF representation Ω provides higher                                                                                                                                                                Rendering. Once trained, the neural field can be used as
quality depth rendering while removing the need to manu-                                                                                                                                                              a drop-in replacement for a conventional graphics pipeline,
ally select a density threshold.                                                                                                                                                                                      to perform efficient rendering of the object for subsequent
Field Learning. For texture learning, we follow the volu-                                                                                                                                                             render-and-compare iterations. In addition to the color ren-
metric rendering over truncated near-surface regions [71]:                                                                                                                                                            dering as in the original NeRF [44], we also need depth
                                                                                                                                                                                                                      rendering for our RGBD based pose estimation and track-
                                                                                                                                                                                                                      ing. To do so, we perform marching cubes [41] to extract a
    &c(r)=\int _{z(r)-\lambda }^{z(r)+0.5\lambda } w(x_i)\Phi (f_{\Omega (x_i)},n(x_i),d(x_i))\,dt, \label {eq:render} \\ &w(x_i)= \frac {1}{1+e^{-\alpha \Omega (x_i)}}\frac {1}{1+e^{\alpha \Omega (x_i)}},
                                                                                                                                                                                                                      textured mesh from the zero level set of the SDF, combined
                                                                                                                                                                                                                      with color projection. This only needs to be performed once
                                                                                                                                                                                                                (2)   for each object. At inference, given an object pose, we then
                                                                                                                                                                                                                      render the RGBD image following the rasterization process.
where w(xi ) is the bell-shaped probability density function
                                                                                                                                                                                                                      Alternatively, one could directly render the depth image us-
[65] that depends on the signed distance Ω(xi ) from the
                                                                                                                                                                                                                      ing Ω online with sphere tracing [14]; however, we found
point to the implicit object surface, and α adjusts the soft-
                                                                                                                                                                                                                      this leads to less efficiency, especially when there is a large
     1 https://developer.nvidia.com/isaac-sim                                                                                                                                                                         number of pose hypotheses to render in parallel.
3.3. Pose Hypothesis Generation                                                                                                                                             Decreasing pose rank
                                                                                                                  Ours

                                                                           Observation
Pose Initialization. Given the RGBD image, the object
is detected using an off-the-shelf method such as Mask R-
CNN [18] or CNOS [47]. We initialize the translation using                                                        W/o hierarchical comparison
the 3D point located at the median depth within the detected
2D bounding box. To initialize rotations, we uniformly
sample Ns viewpoints from an icosphere centered on the
object with the camera facing the center. These camera           Figure 4. Pose ranking visualization. Our proposed hierarchical compar-
poses are further augmented with Ni discretized in-plane         ison leverages the global context among all pose hypotheses for a better
rotations, resulting in Ns · Ni global pose initializations      overall trend prediction that aligns both shape and texture. The true best
                                                                 pose is annotated with red circle.
which are sent as input to the pose refiner.
Pose Refinement. Since the coarse pose initializations from      by:
the previous step are often quite noisy, a refinement mod-                                                                                                  \boldsymbol {t}^{+}=\boldsymbol {t}+\Delta \boldsymbol {t}                                                                    (8)
ule is needed to improve the pose quality. Specifically, we                                                                                        \boldsymbol {R}^{+}=\Delta \boldsymbol {R}\otimes \boldsymbol {R},                                                                     (9)
build a pose refinement network which takes as input the         where ⊗ denotes update on SO(3). Instead of using a single
rendering of the object conditioned on the coarse pose, and      homogeneous pose update, this disentangled representation
a crop of the input observation from the camera; the network     removes the dependency on the updated orientation when
outputs a pose update that improves the pose quality. Un-        applying the translation update. This unifies both the up-
like MegaPose [32], which renders multiple views around          dates and input observation in the camera coordinate frame
the coarse pose to find the anchor point, we observed ren-       and thus simplifies the learning process. The network train-
dering a single view corresponding to the coarse pose suf-       ing is supervised by L2 loss:
fices. For the input observation, instead of cropping based          \label {eq:refine_loss} \mathcal {L}_{\text {refine}}=w_1\left \| \Delta \boldsymbol {t}-\Delta \bar {\boldsymbol {t}} \right \|_2 + w_2\left \| \Delta \boldsymbol {R}-\Delta \bar {\boldsymbol {R}} \right \|_2,  (10)
on the 2D detection which is constant, we perform a pose-
conditioned cropping strategy so as to provide feedback to       where t̄ and R̄ are ground truth; w1 and w2 are the weights
the translation update. Concretely, we project the object        balancing the losses, which are set to 1 empirically.
origin to the image space to determine the crop center. We
                                                                 3.4. Pose Selection
then project the slightly enlarged object diameter (the max-
imum distance between any pair of points on the object sur-      Given a list of refined pose hypotheses, we use a hierarchi-
face) to determine the crop size that encloses the object and    cal pose ranking network to compute their scores. The pose
the nearby context around the pose hypothesis. This crop         with the highest score is selected as the final estimate.
is thus conditioned on the coarse pose and encourages the        Hierarchical Comparison. The network uses a two-level
network to update the translation to make the crop better        comparison strategy. First, for each pose hypothesis, the
aligned with the observation. The refinement process can be      rendered image is compared against the cropped input ob-
repeated multiple times by feeding the latest updated pose       servation, using the pose-conditioned cropping operation
as input to the next inference, so as to iteratively improve     was introduced in Sec. 3.3. This comparison (Fig. 2 bottom-
the pose quality.                                                left) is performed with a pose ranking encoder, utilizing
    The refinement network architecture is illustrated in        the same backbone architecture for feature extraction as in
Fig. 2; details are in the appendix. We first extract fea-       the refinement network. The extracted features are con-
ture maps from the two RGBD input branches with a single         catenated, tokenized and forwarded to the multi-head self-
shared CNN encoder. The feature maps are concatenated,           attention module so as to better leverage the global image
fed into CNN blocks with residual connection [17], and to-       context for comparison. The pose ranking encoder performs
kenized by dividing into patches [9] with position embed-        average pooling to output a feature embedding F ∈ R512
ding. Finally, the network predicts the translation update       describing the alignment quality between the rendering and
∆t ∈ R3 and rotation update ∆R ∈ SO(3), each individu-           the observation (Fig. 2 bottom-middle). At this point, we
ally processed by a transformer encoder [62] and linearly        could directly project F to a similarity scalar as typically
projected to the output dimension. More concretely, ∆t           done [2, 32, 46]. However, this would ignore the other pose
represents the object’s translation shift in the camera frame,   hypotheses, forcing the network to output an absolute score
∆R represents the object’s orientation update expressed in       assignment which can be difficult to learn.
the camera frame. In practice, the rotations are parame-             To leverage the global context of all pose hypotheses in
terized in axis-angle representation. We also experimented       order to make a more informed decision, we introduce a sec-
with the 6D representation [78] which achieves similar re-       ond level of comparison among all the K pose hypotheses.
sults. The input coarse pose [R | t] ∈ SE(3) is then updated     Multi-head self-attention is performed on the concatenated
feature embedding F = [F0 , . . . , FK−1 ]⊤ ∈ RK×512 ,                                                                                                                                                                                                                                   PREDATOR [28]    LoFTR [57]    FS6D-DPM [22]      Ours
                                                                                                                                                                                                                                                                     Ref. images              16             16              16             16
which encodes the pose alignment information from all                                                                                                                                                                                                                Finetune-free             ✓              ✓              ✗               ✓
                                                                                                                                                                                                                                                                        Metrics          ADD-S   ADD     ADD-S ADD      ADD-S ADD       ADD-S ADD
poses. By treating F as a sequence, this approach natu-
                                                                                                                                                                                                                                                                 002_master_chef_can      73.0   17.4    87.2    50.6    92.6   36.8    96.9      91.3
rally generalizes to varying lengths of K [62]. We do not                                                                                                                                                                                                        003_cracker_box          41.7    8.3    71.8    25.5    83.9   24.5    97.5      96.2
                                                                                                                                                                                                                                                                 004_sugar_box            53.7   15.3    63.9    13.4    95.1   43.9    97.5      87.2
apply position encoding to F, so as to be agnostic to the                                                                                                                                                                                                        005_tomato_soup_can      81.2   44.4    77.1    52.9    93.0   54.2    97.6      93.3
permutation. The attended feature is then linearly projected                                                                                                                                                                                                     006_mustard_bottle
                                                                                                                                                                                                                                                                 007_tuna_fish_can
                                                                                                                                                                                                                                                                                          35.5
                                                                                                                                                                                                                                                                                          78.2
                                                                                                                                                                                                                                                                                                  5.0
                                                                                                                                                                                                                                                                                                 34.2
                                                                                                                                                                                                                                                                                                         84.5
                                                                                                                                                                                                                                                                                                         72.6
                                                                                                                                                                                                                                                                                                                 59.0
                                                                                                                                                                                                                                                                                                                 55.7
                                                                                                                                                                                                                                                                                                                         97.0
                                                                                                                                                                                                                                                                                                                         94.5
                                                                                                                                                                                                                                                                                                                                71.1
                                                                                                                                                                                                                                                                                                                                53.9
                                                                                                                                                                                                                                                                                                                                        98.4
                                                                                                                                                                                                                                                                                                                                        97.7
                                                                                                                                                                                                                                                                                                                                                  97.3
                                                                                                                                                                                                                                                                                                                                                  73.7
to the scores S ∈ RK to be assigned to the pose hypotheses.                                                                                                                                                                                                      008_pudding_box          73.5   24.2    86.5    68.1    94.9   79.6    98.5      97.0
                                                                                                                                                                                                                                                                 009_gelatin_box          81.4   37.5    71.6    45.2    98.3   32.1    98.5      97.3
The effectiveness of this hierarchical comparison strategy is                                                                                                                                                                                                    010_potted_meat_can      62.0   20.9    67.4    45.1    87.6   54.9    96.6      82.3
                                                                                                                                                                                                                                                                 011_banana               57.7    9.9    24.2     1.6    94.0   69.1    98.1      95.4
shown in a typical example in Fig. 4.                                                                                                                                                                                                                            019_pitcher_base         83.7   18.1    58.7    22.3    91.1   40.4    97.9      96.6
Contrast Validation. To train the pose ranking network,                                                                                                                                                                                                          021_bleach_cleanser
                                                                                                                                                                                                                                                                 024_bowl
                                                                                                                                                                                                                                                                                          88.3
                                                                                                                                                                                                                                                                                          73.2
                                                                                                                                                                                                                                                                                                 48.1
                                                                                                                                                                                                                                                                                                 17.4
                                                                                                                                                                                                                                                                                                         36.9
                                                                                                                                                                                                                                                                                                         32.7
                                                                                                                                                                                                                                                                                                                 16.7
                                                                                                                                                                                                                                                                                                                  1.4
                                                                                                                                                                                                                                                                                                                         89.4
                                                                                                                                                                                                                                                                                                                         74.7
                                                                                                                                                                                                                                                                                                                                44.1
                                                                                                                                                                                                                                                                                                                                 0.9
                                                                                                                                                                                                                                                                                                                                        97.4
                                                                                                                                                                                                                                                                                                                                        94.9
                                                                                                                                                                                                                                                                                                                                                  93.3
                                                                                                                                                                                                                                                                                                                                                  89.7
we propose a pose-conditioned triplet loss:                                                                                                                                                                                                                      025_mug                  84.8   29.5    47.3    23.6    86.5   39.2    96.2      75.8
                                                                                                                                                                                                                                                                 035_power_drill          60.6   12.3    18.8     1.3    73.0   19.8    98.0      96.3
           \label {eq:triplet} \mathcal {L}(i^+, i^-)=\text {max}(\mathbf {S}(i^{-})-\mathbf {S}(i^{+})+\alpha , 0),                                                                                                                                     (11)    036_wood_block           70.5   10.0    49.9     1.4    94.7   27.9    97.4      94.7
                                                                                                                                                                                                                                                                 037_scissors             75.5   25.0    32.3    14.6    74.2   27.7    97.8      95.5
where α denotes the contrastive margin; i− and i+ repre-                                                                                                                                                                                                         040_large_marker         81.8   38.9    20.7     8.4    97.4   74.2    98.6      96.5
                                                                                                                                                                                                                                                                 051_large_clamp          83.0   34.4    24.1    11.2    82.7   34.7    96.9      92.7
sent the negative and positive pose samples, respectively,                                                                                                                                                                                                       052_extra_large_clamp    72.9   24.1    15.0     1.8    65.7   10.1    97.6      94.1
                                                                                                                                                                                                                                                                 061_foam_brick           79.2   35.5    59.4    31.4    95.7   45.8    98.1      93.4
which are determined by computing the ADD metric [73]                                                                                                                                                                                                                   MEAN              71.0   24.3    52.5    26.2    88.4   42.1    97.4      91.5
using ground truth. Note that different from standard triplet
                                                                                                                                                                                                                                                                Table 1. Model-free pose estimation results measured by AUC of ADD
loss [27], the anchor sample is not shared between the pos-
                                                                                                                                                                                                                                                                and ADD-S on YCB-Video dataset. “Finetuned” means the method was
itive and negative samples in our case, since the input is                                                                                                                                                                                                      fine-tuned with group split of object instances on the testing dataset, as
cropped depending on each pose hypothesis to account for                                                                                                                                                                                                        introduced by [22].
translations. While we can compute this loss over each pair
in the list, the comparison becomes ambiguous when both                                                                                                                                                                                                         are selected from the training split of the datasets, equipped
poses are far from ground truth. Therefore, we only keep                                                                                                                                                                                                        with the ground-truth annotation of the object pose, follow-
those pose pairs whose positive sample is from a viewpoint                                                                                                                                                                                                      ing [22]. For the model-based setup, a CAD model is pro-
that is close enough to the ground truth to make the com-                                                                                                                                                                                                       vided for the novel object. In all evaluation except for ab-
parison meaningful:                                                                                                                                                                                                                                             lation, our method always uses the same trained model and
                                \mathbb {V}^+ &=\{i \,:\, D(\boldsymbol {R}_i, \bar {\boldsymbol {R}})<d \} \\ \mathbb {V}^- &= \{0, 1, 2, \ldots , K-1\} \\ \mathcal {L}_{\text {rank}} &=\sum _{i^+, i^-} \mathcal {L}(i^+, i^-) \label {eq:list_loss}        configurations for inference without any fine-tuning.
                                                                                                                                                                                                                                                                4.2. Metric
                                                                                                                                                                                                                                           (14)                 To closely follow the baseline protocols on each setup, we
                                                                                                                                                                                                                                                                consider the following metrics:
where the summation is over i+ ∈ V+ , i− ∈ V− , i+ ̸= i− ;                                                                                                                                                                                                      • Area under the curve (AUC) of ADD and ADD-S [73].
Ri and R̄ are the rotation of the hypothesis and ground                                                                                                                                                                                                         • Recall of ADD that is less than 0.1 of the object diameter
truth, respectively; D(·) denotes the geodesic distance be-                                                                                                                                                                                                       (ADD-0.1d), as used in [19, 22].
tween rotations; and d is a predefined threshold. We also                                                                                                                                                                                                       • Average recall (AR) of VSD, MSSD and MSPD metrics
experimented with the InfoNCE loss [49] as used in [46] but                                                                                                                                                                                                       introduced in the BOP challenge [26].
observed worse performance (Sec. 4.5). We attribute this to
                                                                                                                                                                                                                                                                4.3. Pose Estimation Comparison
the perfect translation assumption made in [46] which is not
the case in our setup.                                                                                                                                                                                                                                          Model-free. Table 1 presents the comparison results against
                                                                                                                                                                                                                                                                the state-of-art RGBD methods [22, 28, 57] on YCB-Video
4. Experiments                                                                                                                                                                                                                                                  dataset. The baselines results are adopted from [22]. Fol-
                                                                                                                                                                                                                                                                lowing [22], all methods are given the perturbed ground-
4.1. Dataset and Setup
                                                                                                                                                                                                                                                                truth bounding box as 2D detection for fair comparison. Ta-
We consider 5 datasets: LINEMOD [23], Occluded-                                                                                                                                                                                                                 ble 2 presents the comparison results on LINEMOD dataset.
LINEMOD [1], YCB-Video [73], T-LESS [25], and YCBI-                                                                                                                                                                                                             The baseline results are adopted from [19, 22]. RGB-based
nEOAT [67]. These involve various challenging scenar-                                                                                                                                                                                                           methods [19, 40, 58] are given the privilege of much larger
ios (dense clutter, multi-instance, static or dynamic scenes,                                                                                                                                                                                                   number of reference images to compensate for the lack of
table-top or robotic manipulation), and objects with diverse                                                                                                                                                                                                    depth. Among RGBD methods, FS6D [22] requires fine-
properties (textureless, shiny, symmetric, varying sizes).                                                                                                                                                                                                      tuning on the target dataset. Our method significantly out-
   As our framework is unified, we consider the combina-                                                                                                                                                                                                        performs the existing methods on both datasets without
tions among two setups (model-free and model-based) and                                                                                                                                                                                                         fine-tuning on the target dataset or ICP refinement.
two pose prediction tasks (6D pose estimation and track-                                                                                                                                                                                                            Fig. 5 visualizes the qualitative comparison. We do not
ing), resulting in 4 tasks in total. For the model-free setup,                                                                                                                                                                                                  have access to the pose predictions of FS6D [22] for qual-
a number of reference images capturing the novel object                                                                                                                                                                                                         itative results, since its code is not publicly released. The
                                                   Finetune-      Ref.                                                                      Objects
                   Method            Modality         free       images     ape         benchwise      cam       can      cat    driller   duck eggbox    glue    holepuncher   iron    lamp    phone   Avg.

                 Gen6D [40]           RGB             ✗           200        -              77         66.1        -      60.7    67.4     40.5   95.7     87.2       -           -       -       -      -
                Gen6D* [40]           RGB             ✓           200        -             62.1        45.6        -      40.9   48.8      16.2     -       -         -           -       -       -      -
                OnePose [58]          RGB             ✓           200       11.8          92.6          88.1     77.2    47.9     74.5     34.2   71.3     37.5      54.9       89.2    87.6     60.6   63.6
              OnePose++ [19]          RGB             ✓           200       31.2          97.3          88.0     89.8    70.4     92.5     42.3   99.7     48.0      69.7       97.4    97.8     76.0   76.9
              LatentFusion [51]      RGBD             ✓            16       88.0          92.4          74.4     88.8    94.5     91.7     68.1   96.3     94.9      82.1       74.6    94.7     91.5   87.1
                 FS6D [22]           RGBD             ✗            16       74.0          86.0          88.5     86.0    98.5     81.0     68.5   100.0    99.5      97.0       92.5    85.0    99.0    88.9
              FS6D [22] + ICP        RGBD             ✗            16       78.0          88.5          91.0     89.5    97.5     92.0     75.5   99.5     99.5      96.0       87.5    97.0     97.5   91.5
                    Ours             RGBD             ✓            16       99.0          100.0        100.0     100.0   100.0   100.0     99.4   100.0   100.0      99.9       100.0   100.0   100.0   99.9

  Table 2. Model-free pose estimation results measured by ADD-0.1d on LINEMOD dataset. Gen6D* [40] represents the variation without fine-tuning.
          Input                     OnePose++                  LatentFusion                          Ours
                                                                                                                            to the evaluated methods in the case of tracking lost, in order
                                                                                                                            to evaluate long-term tracking robustness. We defer to our
                                                                                                                            supplemental materials for qualitative results.
                                                                                                                                For comprehensive comparison on the challenges of
                                                                                                                            abrupt out-of-plane rotations, dynamic external occlusions
Figure 5. Qualitative comparison of pose estimation on LINEMOD dataset
                                                                                                                            and disentangled camera motions, we evaluate pose track-
under the model-free setup. Images are cropped and zoomed-in for better                                                     ing methods on the YCBInEOAT [67] dataset which in-
visualization.                                                                                                              cludes videos of dynamic robotic manipulation. Results un-
severe self-occlusion and lack of texture on the glue largely                                                               der the model-based setup are presented in Table 4. Our
challenge OnePose++ [19] and LatentFusion [51], while                                                                       method achieves the best performance and even outper-
our method successfully estimates the pose.                                                                                 forms the instance-wise training method [67] with ground-
                                                                                                                            truth pose initialization. Moreover, our unified frame-
                                        Unseen                       Dataset                                                work also allows for end-to-end pose estimation and track-
                Method                   objects          LM-O      T-LESS            YCB-V           Mean
                                                                                                                            ing without external pose initialization, which is the only
         SurfEmb [15] + ICP                    ✗          75.8           82.8            80.6          79.7                 method with such capability, noted as Ours† in the table.
          OSOP [55] + ICP                   ✓             48.2            -              57.2           -
       (PPF, Sift) + Zephyr [48]            ✓             59.8            -              51.6           -
                                                                                                                                Table 5 presents the comparison results of pose track-
        MegaPose-RGBD [32]                  ✓             58.3           54.3            63.3          58.6                 ing on YCB-Video [73] dataset. Among the baselines,
              OVE6D [2]                     ✓             49.6           52.3             -             -
             GCPose [76]                    ✓             65.2           67.9             -             -
                                                                                                                            DeepIM [36], se(3)-TrackNet [67] and PoseRBPF [8] need
                  Ours                      ✓             78.8           83.0            88.0          83.3                 training on the same object instances, while Wüthrich et
Table 3. Model-based pose estimation results measured by AR score on                                                        al. [72], RGF [29], ICG [56] and our method can be in-
representative BOP datasets. All methods use the RGBD modality.                                                             stantly applied to novel objects when provided with a CAD
                                                                                                                            model.
Model-based.      Table 3 presents the comparison re-
sults among RGBD methods on 3 core datasets from                                                                            4.5. Analysis
BOP: Occluded-LINEMOD [1], YCB-Video [73] and T-
LESS [25]. All methods use Mask R-CNN [18] for 2D de-                                                                       Ablation Study. Table 6 presents the ablation study of crit-
tection. Our method outperforms the existing model-based                                                                    ical design choices. The results are evaluated by AUC of
methods that deal with novel objects, and the instance-level                                                                ADD and ADD-S metrics on the YCB-Video dataset. Ours
method [15], by a large margin.                                                                                             (proposed) is the default version under the model-free (16
                                                                                                                            reference images) setup. W/o LLM texture augmentation
4.4. Pose Tracking Comparison                                                                                               removes the LLM-aided texture augmentation for synthetic
                                                                                                                            training. In W/o transformer, we replace the transformer-
                                         se(3)-        RGF      Bundle-     Bundle-        Wüthrich     Ours     Ours†      based architecture by convolutional and linear layers while
                                     TrackNet [67]     [29]    Track [66]   SDF [71]        [72]
                     Novel object          ✗           ✓          ✓              ✓              ✓           ✓      ✓
                                                                                                                            keeping the similar number of parameters. W/o hierarchical
 Properties          Initial pose         GT           GT         GT             GT             GT          GT    Est.      comparison only compares the rendering and the cropped
                     ADD-S               94.06        55.44      89.41          90.63        88.13      95.10    94.92
 cracker_box         ADD                 90.76        34.78      85.07          85.37        79.00      91.32    91.54      input trained by pose-conditioned triplet loss (Eq. 11) with-
                     ADD-S               94.44        45.03      94.72          94.28        68.96      95.96    96.36
 bleach_cleanser
                     ADD                 89.58        29.40      89.34          87.46        61.47      91.45    92.63      out two-level hierarchical comparison. At test time, it com-
                     ADD-S               94.80        16.87      90.22          93.81        92.75      96.67    96.61
 sugar_box
                     ADD                 92.43        15.82      85.56          88.62        86.78      94.14    93.96      pares each pose hypothesis with the input observation inde-
                     ADD-S               96.95        26.44      95.13          95.24        93.17      96.58    96.54
 tomato_soup_can
                     ADD                 93.40        15.13      86.00          83.10        63.71      91.71    91.85      pendently and outputs the pose with the highest score. Ex-
                     ADD-S               97.92        60.17      95.35          95.75        95.31      97.89    97.77
 mustard_bottle      ADD                 97.00        56.49      92.26          89.87        91.31      96.34    95.95      ample qualitative result is shown in Fig. 4. Ours-InfoNCE
 All
                     ADD-S               95.53        39.90      92.53          93.77        89.18      96.42    96.40      replaces contrast validated pair-wise loss (Eq. 14) by the In-
                     ADD                 92.66        29.98      87.34          86.95        78.28      93.09    93.22
                                                                                                                            foNCE loss as used in [46].
Table 4. Pose tracking results of RGBD methods measured by AUC of
ADD and ADD-S on YCBInEOAT dataset. Ours† represents our unified                                                            Effects of number of reference images. We study how
pipeline that uses the pose estimation module for pose initialization.                                                      the number of reference images affects the results measured
                                                                                                                            by AUC of ADD and ADD-S on YCB-Video dataset, as
       Unless otherwise specified, no re-initialization is applied                                                          shown in Fig. 6. Overall, our method is robust to the num-
                                             DeeplM [36]     se(3)-TrackNet                     PoseRBPF [8]               Wüthrich [72]        RGF [29]                           ICG [56]               Ours                      Ours†
                     Approach                                      [67]                            + SDF
              Initial pose                       GT             GT                              PoseCNN                        GT              GT                                 GT                  GT                      GT
            Re-initialization                 Yes (290)         No                               Yes (2)                       No              No                                 No                  No                      No
             Novel object                         ✗              ✗                                  ✗                           ✓               ✓                                  ✓                   ✓                       ✓
             Object setup                    Model-based     Model-based                       Model-based                  Model-based     Model-based                        Model-based         Model-based              Model-free
                Metric                      ADD ADD-S       ADD ADD-S                         ADD ADD-S                    ADD ADD-S       ADD ADD-S                          ADD ADD-S           ADD ADD-S                ADD ADD-S
         002_master_chef_can                89.0    93.8     93.9         96.3                 89.3                 96.7   55.6    90.7    46.2                 90.2          66.4      89.7     93.6     97.0               91.2        96.9
         003_cracker_box                    88.5    93.0     96.5         97.2                 96.0                 97.1   96.4    97.2    57.0                 72.3          82.4      92.1     96.9     97.8               96.2        97.5
         004_sugar_box                      94.3    96.3     97.6         98.1                 94.0                 96.4   97.1    97.9    50.4                 72.7          96.1      98.4     96.9     98.2               94.5        97.4
         005_tomato_soup_can                89.1    93.2     95.0         97.2                 87.2                 95.2   64.7    89.5    72.4                 91.6          73.2      97.3     96.3     98.1               94.3        97.9
                                                                          A traditional wooden
         006_mustard_bottle                 92.0    95.1     95.8         97.4                 98.3
                                                                          armoire in a rich mahogany
                                                                          finish, showcasing
                                                                                                                    98.5   97.1    98.0    87.7                 98.2          96.2      98.4     97.3     98.4               97.3        98.5
                                                                          intricate carvings and
         007_tuna_fish_can                  92.0    96.4     86.5         91.1
                                                                          brass hardware for an
                                                                          elegant look
                                                                                               86.8                 93.6   69.1    93.3    28.7                 52.9          73.2      95.8     96.9     98.5               84.0        97.8
         008_pudding_box                    80.1    88.3     97.9         98.4                 60.9                 87.1   96.8    97.9    12.7                 18.0          73.8      88.9     97.8     98.5               96.9        98.5
         009_gelatin_box                    92.0    94.4     97.8         98.4                 98.2                 98.6   97.5    98.4    49.1                 70.7
                                                                                                                                                                 100.00       97.2      98.8     97.7     98.5               97.6        98.5
         010_potted_meat_can                78.0    88.9     77.8         84.2                 76.4                 83.5   83.7    86.7    44.1                 45.6          93.3      97.3     95.1     97.7               94.8        97.5
                                                                                                                                                                  95.00
         011_banana                         81.0    90.5     94.9         97.2                 92.8
                                                                                          Random texture blending
                                                                                                                    97.7   86.3    96.1    93.3                 97.7          95.6      98.4     96.4     98.4               95.6        98.1
         019_pitcher_base                   90.4    94.7     96.8         97.5                 97.7                 98.1   97.3    97.7    97.9                 98.2
                                                                                                                                                                  90.00       97.0      98.8     96.7     98.0               96.8        98.0
         021_bleach_cleanser                81.7    90.5     95.9         97.2                 95.9
                                                                                    A unique wineglass with a
                                                                                                                    97.0   95.2    97.2    95.9                 97.3
                                                                                                                                                                  85.00
                                                                                                                                                                              92.6      97.5     95.5     97.8               94.7        97.5

                                                                                                                                                              AUC (%)
                                                                                    stem shaped like a
         024_bowl                           38.8    90.6     80.9         94.5                 34.0
                                                                                    corkscrew, showcasing a
                                                                                    bowl made of hand‐blown
                                                                                                                    93.0   30.4    97.2    24.2                 82.4          74.4      98.4     95.2     97.6               90.5        95.3
                                                                                    glass in a mix of swirling
         025_mug                            83.2    92.0     91.5         96.9                 86.9
                                                                                    red and white                   96.7   83.2    93.3    60.0                   80.00
                                                                                                                                                                71.2          95.6      98.5     95.6     97.9               91.5        96.1
         035_power_drill                    85.4    92.3     96.4         97.4                 97.8
                                                                                    An artistic wineglass
                                                                                    hand‐painted with vibrant
                                                                                                                    98.2   97.1    97.8    97.9                 98.3
                                                                                                                                                                  75.00       96.7      98.5     96.9     98.2               96.3        97.9
                                                                                    strokes of brown, blue,
         036_wood_block                     44.3    75.4     95.2         96.7                 37.8
                                                                                    and green, creating a
                                                                                    striking abstract design
                                                                                                                    93.6   95.5    96.9    45.7                 62.5          93.5      97.2     93.2     97.0               92.9        97.0
                                                                                                                                                                  70.00
         037_scissors                       70.3    84.5     95.7         97s                  72.7                 85.5    4.2    16.2    20.9                 38.6          93.5      97.3     94.8     97.5               95.5        97.8
                                                                                                                                                                                                                                       ADD
         040_large_marker                   80.4    91.2     92.2         96.0                 89.2
                                                                                   A vibrant red bulb with a
                                                                                   gradient of orange and           97.3   35.6    53.0    12.2                 18.9
                                                                                                                                                                  65.00       88.5      97.8     96.9     98.6               96.6        98.6
                                                                                                                                                                                                                                       ADD-S
                                                                                   yellow, emitting a warm glow

         051_large_clamp                    73.9    84.1     94.7         96.9                 90.1                 95.5   61.2    72.3    62.8                 80.1          91.8      96.9     93.6     97.3               92.5        96.7
                                                                                                                                                                  60.00
         052_extra_large_clamp              49.3    90.3     91.7         95.8                 84.4                 94.1   93.7    96.6    67.5                 69.7 3        85.9 5    94.37    94.4
                                                                                                                                                                                                   9      97.5
                                                                                                                                                                                                            11             1393.4     15 97.3 17

         061_foam_brick                     91.6    95.5     93.7         96.7                 96.1                 98.3   96.8    98.1    70.0                 86.5          96.2      98.5 Num 97.9
                                                                                                                                                                                                 reference98.6
                                                                                                                                                                                                           images            96.8        98.3
         All Frames                         82.3    91.9     93.0         95.7                 87.5                 95.2   78.0    90.2    59.2                 74.3          86.4      96.5       96.0       97.9         93.7            97.5

Table 5. Pose tracking results of RGBD methods measured by AUC of ADD and ADD-S on YCB-Video dataset. Ours† represents our method under the
model-free setup with reference images.
                                                                                                                                                     99.00
                                                                 ADD               ADD-S
                                                                                                                                                     97.00
                           Ours (proposed)                       91.52               97.40
                                                                                                                                                     95.00
                           W/o LLM texture augmentation          90.83               97.38
                           W/o transformer                       90.77               97.33
                                                                                                                                           AUC (%)

                                                                                                                                                     93.00

                           W/o hierarchical comparison           89.05               96.67                                                           91.00
                           Ours-InfoNCE                          89.39               97.29
                                                                                                                                                     89.00

                                                                                                                                                                                                                           ADD
                           Table 6. Ablation study of critical design choices.                                                                       87.00
                                                                                                                                                                                                                           ADD-S
                                                                                                                                                     85.00
ber of reference images especially on the ADD-S metric,                                                                                                      3.5               4          4.5             5          5.5               6
                                                                                                                                                                                       Train data size (log10)
and saturates at 12 images for both metrics. Notably, even                                                                                                              Figure 7. Effects of training data size.
when only 4 reference images are provided, our method still
yields stronger performance than FS6D [22] equipped with
16 reference images (Table 1).                                                                                                    ject, where pose initialization takes 4 ms, refinement takes
Training data scaling law. Theoretically, an unbounded                                                                            0.88 s, pose selection takes 0.42 s. Tracking runs much
amount of synthetic data can be produced for training.                                                                            faster at ∼32 Hz, since only pose refinement is needed and
Fig. 7 presents how the amount of training data affects the                                                                       there are not multiple pose hypotheses. In practice, we
results measured by AUC of ADD and ADD-S metrics on                                                                               can run pose estimation once for initialization and switch
YCB-Video dataset. The gain saturates around 1M.                                                                                  to tracking mode for real-time performance.
Running time. We measure the running time on the hard-
ware of Intel i9-10980XE CPU and NVIDIA RTX 3090
GPU. The pose estimation takes about 1.3 s for one ob-
                                                                                                                                  5. Conclusion
                           100.00

                            95.00
                                                                                                                                  We present a unified foundation model for 6D pose estima-
                            90.00
                                                                                                                                  tion and tracking of novel objects, supporting both model-
                            85.00
                                                                                                                                  based and model-free setups. Extensive experiments on
                 AUC (%)

                            80.00
                                                                                                                                  the combinations of 4 different tasks indicate it is not only
                            75.00

                            70.00
                                                                                                                                  versatile but also outperforms existing state-of-art methods
                            65.00
                                                                                      ADD                                         specially designed for each task by a considerable margin.
                                                                                      ADD-S
                            60.00
                                                                                                                                  It even achieves comparable results to those methods requir-
                                    3   5    7      9       11       13              15                     17
                                              Num reference images                                                                ing instance-level training. In future work, exploring state
                            Figure 6. Effects of number of reference images.                                                      estimation beyond single rigid object will be of interest.

         99.00

         97.00

         95.00
   (%)

         93.00
References                                                            [12] Amos Gropp, Lior Yariv, Niv Haim, Matan Atzmon, and
                                                                           Yaron Lipman. Implicit geometric regularization for learning
 [1] Eric Brachmann, Alexander Krull, Frank Michel, Stefan                 shapes. In International Conference on Machine Learning
     Gumhold, Jamie Shotton, and Carsten Rother. Learning 6D               (ICML), pages 3789–3799, 2020. 4
     object pose estimation using 3d object coordinates. In 13th
                                                                      [13] Agrim Gupta, Piotr Dollar, and Ross Girshick. LVIS: A
     European Conference on Computer Vision (ECCV), pages
                                                                           dataset for large vocabulary instance segmentation. In Pro-
     536–551, 2014. 6, 7
                                                                           ceedings of the IEEE/CVF Conference on Computer Vision
 [2] Dingding Cai, Janne Heikkilä, and Esa Rahtu. OVE6D: Ob-               and Pattern Recognition (CVPR), pages 5356–5364, 2019. 2
     ject viewpoint encoding for depth-based 6D object pose es-       [14] John C Hart. Sphere tracing: A geometric method for the
     timation. In Proceedings of the IEEE/CVF Conference on                antialiased ray tracing of implicit surfaces. The Visual Com-
     Computer Vision and Pattern Recognition (CVPR), pages                 puter, 12(10):527–545, 1996. 4
     6803–6813, 2022. 5, 7, 3
                                                                      [15] Rasmus Laurvig Haugaard and Anders Glent Buch. Sur-
 [3] Ming Cai and Ian Reid. Reconstruct locally, localize glob-            femb: Dense and continuous correspondence distributions
     ally: A model free method for object pose estimation. In Pro-         for object pose estimation with learnt surface embeddings.
     ceedings of the IEEE/CVF Conference on Computer Vision                In Proceedings of the IEEE/CVF Conference on Computer
     and Pattern Recognition (CVPR), pages 3153–3163, 2020. 2              Vision and Pattern Recognition (CVPR), pages 6749–6758,
 [4] Tianshi Cao, Karsten Kreis, Sanja Fidler, Nicholas Sharp,             2022. 7
     and Kangxue Yin. TexFusion: Synthesizing 3D textures             [16] Poly Haven. Poly Haven: The public 3D asset library. https:
     with text-guided image diffusion models. In Proceedings of            //polyhaven.com/, 2023. 2
     the IEEE/CVF International Conference on Computer Vision         [17] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     (ICCV), pages 4169–4181, 2023. 2, 3                                   Deep residual learning for image recognition. In Proceed-
 [5] Dengsheng Chen, Jun Li, Zheng Wang, and Kai Xu. Learn-                ings of the IEEE/CVF Conference on Computer Vision and
     ing canonical shape space for category-level 6D object pose           Pattern Recognition (CVPR), pages 770–778, 2016. 5, 2
     and size estimation. In Proceedings of the IEEE Inter-           [18] Kaiming He, Georgia Gkioxari, Piotr Dollár, and Ross Gir-
     national Conference on Computer Vision (CVPR), pages                  shick. Mask R-CNN. In Proceedings of the IEEE/CVF
     11973–11982, 2020. 1, 2                                               Conference on Computer Vision and Pattern Recognition
 [6] Matt Deitke, Dustin Schwenk, Jordi Salvador, Luca Weihs,              (CVPR), pages 2961–2969, 2017. 5, 7, 3
     Oscar Michel, Eli VanderBilt, Ludwig Schmidt, Kiana              [19] Xingyi He, Jiaming Sun, Yuang Wang, Di Huang, Hujun
     Ehsani, Aniruddha Kembhavi, and Ali Farhadi. Objaverse:               Bao, and Xiaowei Zhou. OnePose++: Keypoint-free one-
     A universe of annotated 3D objects. In Proceedings of                 shot object pose estimation without CAD models. Advances
     the IEEE/CVF Conference on Computer Vision and Pattern                in Neural Information Processing Systems (NeurIPS), 35:
     Recognition (CVPR), pages 13142–13153, 2023. 2                        35103–35115, 2022. 1, 2, 6, 7, 3
 [7] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li,           [20] Yisheng He, Wei Sun, Haibin Huang, Jianran Liu, Haoqiang
     and Li Fei-Fei. ImageNet: A large-scale hierarchical im-              Fan, and Jian Sun. PVN3D: A deep point-wise 3D keypoints
     age database. In Proceedings of the IEEE/CVF Conference               voting network for 6DoF pose estimation. In Proceedings of
     on Computer Vision and Pattern Recognition (CVPR), pages              the IEEE/CVF Conference on Computer Vision and Pattern
     248–255, 2009. 3                                                      Recognition (CVPR), pages 11632–11641, 2020. 1, 2
 [8] Xinke Deng, Arsalan Mousavian, Yu Xiang, Fei Xia, Timo-          [21] Yisheng He, Haibin Huang, Haoqiang Fan, Qifeng Chen, and
     thy Bretl, and Dieter Fox. PoseRBPF: A Rao-Blackwellized              Jian Sun. FFB6D: A full flow bidirectional fusion network
     particle filter for 6D object pose tracking. In Robotics: Sci-        for 6D pose estimation. In Proceedings of the IEEE/CVF
     ence and Systems (RSS), 2019. 1, 2, 7, 8                              Conference on Computer Vision and Pattern Recognition
 [9] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,                (CVPR), pages 3003–3013, 2021. 1, 2
     Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,              [22] Yisheng He, Yao Wang, Haoqiang Fan, Jian Sun, and Qifeng
     Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-              Chen. FS6D: Few-shot 6D pose estimation of novel objects.
     vain Gelly, et al. An image is worth 16x16 words: Trans-              In Proceedings of the IEEE/CVF Conference on Computer
     formers for image recognition at scale. In International Con-         Vision and Pattern Recognition (CVPR), pages 6814–6824,
     ference on Learning Representations (ICLR), 2021. 5                   2022. 2, 3, 6, 7, 8
[10] Laura Downs, Anthony Francis, Nate Koenig, Brandon Kin-          [23] Stefan Hinterstoisser, Stefan Holzer, Cedric Cagniart, Slobo-
     man, Ryan Hickman, Krista Reymann, Thomas B McHugh,                   dan Ilic, Kurt Konolige, Nassir Navab, and Vincent Lepetit.
     and Vincent Vanhoucke. Google scanned objects: A high-                Multimodal templates for real-time detection of texture-less
     quality dataset of 3D scanned household items. In Inter-              objects in heavily cluttered scenes. In International Confer-
     national Conference on Robotics and Automation (ICRA),                ence on Computer Vision (ICCV), pages 858–865, 2011. 6
     pages 2553–2560, 2022. 2                                         [24] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffu-
[11] Mathieu Garon, Denis Laurendeau, and Jean-François                    sion probabilistic models. Advances in Neural Information
     Lalonde. A framework for evaluating 6-dof object trackers.            Processing Systems (NeurIPS), 33:6840–6851, 2020. 2
     In Proceedings of the European Conference on Computer Vi-        [25] Tomáš Hodan, Pavel Haluza, Štepán Obdržálek, Jiri Matas,
     sion (ECCV), pages 582–597, 2018. 2                                   Manolis Lourakis, and Xenophon Zabulis. T-LESS: An
     RGB-D dataset for 6D pose estimation of texture-less ob-             Proceedings of the European Conference on Computer Vi-
     jects. In IEEE Winter Conference on Applications of Com-             sion (ECCV), pages 683–698, 2018. 1, 2, 7, 8
     puter Vision (WACV), pages 880–888, 2017. 6, 7                  [37] Zhigang Li, Gu Wang, and Xiangyang Ji.                 CDPN:
[26] Tomas Hodan, Frank Michel, Eric Brachmann, Wadim Kehl,               Coordinates-based disentangled pose network for real-time
     Anders GlentBuch, Dirk Kraft, Bertram Drost, Joel Vidal,             RGB-based 6-DoF object pose estimation. In CVF Interna-
     Stephan Ihrke, Xenophon Zabulis, et al. BOP: Benchmark               tional Conference on Computer Vision (ICCV), pages 7677–
     for 6D object pose estimation. In Proceedings of the Euro-           7686, 2019. 2
     pean Conference on Computer Vision (ECCV), pages 19–34,         [38] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,
     2018. 2, 6                                                           Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence
[27] Elad Hoffer and Nir Ailon. Deep metric learning using triplet        Zitnick. Microsoft COCO: Common objects in context.
     network. In Third International Workshop on Similarity-              In 13th European Conference on Computer Vision (ECCV),
     Based Pattern Recognition (SIMBAD), pages 84–92, 2015.               pages 740–755, 2014. 3
     6                                                               [39] Yunzhi Lin, Jonathan Tremblay, Stephen Tyree, Patricio A
[28] Shengyu Huang, Zan Gojcic, Mikhail Usvyatsov, Andreas                Vela, and Stan Birchfield. Keypoint-based category-level ob-
     Wieser, and Konrad Schindler. PREDATOR: Registration                 ject pose tracking from an RGB sequence with uncertainty
     of 3D point clouds with low overlap. In Proceedings of               estimation. In International Conference on Robotics and Au-
     the IEEE/CVF Conference on Computer Vision and Pattern               tomation (ICRA), 2022. 1, 2
     Recognition (CVPR), pages 4267–4276, 2021. 6                    [40] Yuan Liu, Yilin Wen, Sida Peng, Cheng Lin, Xiaoxiao Long,
[29] Jan Issac, Manuel Wüthrich, Cristina Garcia Cifuentes, Jean-         Taku Komura, and Wenping Wang. Gen6D: Generalizable
     nette Bohg, Sebastian Trimpe, and Stefan Schaal. Depth-              model-free 6-DoF object pose estimation from RGB images.
     based object tracking using a robust gaussian filter. In             ECCV, 2022. 1, 2, 6, 7
     IEEE International Conference on Robotics and Automation        [41] William E Lorensen and Harvey E Cline. Marching cubes:
     (ICRA), pages 608–615, 2016. 1, 2, 7, 8                              A high resolution 3d surface construction algorithm. In Sem-
[30] Daniel Kappler, Franziska Meier, Jan Issac, Jim Main-                inal graphics: pioneering efforts that shaped the field, pages
     price, Cristina Garcia Cifuentes, Manuel Wüthrich, Vin-              347–353. 1998. 4
     cent Berenz, Stefan Schaal, Nathan Ratliff, and Jeannette       [42] Miles Macklin. Warp: A high-performance python frame-
     Bohg. Real-time perception meets reactive motion gener-              work for gpu simulation and graphics. https://github.com/
     ation. IEEE Robotics and Automation Letters, 3(3):1864–              nvidia/warp, 2022. NVIDIA GPU Technology Conference
     1871, 2018. 1                                                        (GTC). 1
[31] Yann Labbé, Justin Carpentier, Mathieu Aubry, and Josef         [43] Eric Marchand, Hideaki Uchiyama, and Fabien Spindler.
     Sivic. CosyPose: Consistent multi-view multi-object 6D               Pose estimation for augmented reality: A hands-on survey.
     pose estimation. In European Conference on Computer Vi-              IEEE Transactions on Visualization and Computer Graphics
     sion (ECCV), pages 574–591, 2020. 1, 2                               (TVCG), 22(12):2633–2651, 2015. 1
[32] Yann Labbé, Lucas Manuelli, Arsalan Mousavian, Stephen          [44] Ben Mildenhall, Pratul P Srinivasan, Matthew Tancik,
     Tyree, Stan Birchfield, Jonathan Tremblay, Justin Carpentier,        Jonathan T Barron, Ravi Ramamoorthi, and Ren Ng. NeRF:
     Mathieu Aubry, Dieter Fox, and Josef Sivic. MegaPose: 6D             Representing scenes as neural radiance fields for view syn-
     pose estimation of novel objects via render & compare. In            thesis. Communications of the ACM, 65(1):99–106, 2021.
     6th Annual Conference on Robot Learning (CoRL), 2022. 1,             4
     2, 5, 7, 3                                                      [45] Thomas Müller, Alex Evans, Christoph Schied, and Alexan-
[33] Samuli Laine, Janne Hellsten, Tero Karras, Yeongho Seol,             der Keller. Instant neural graphics primitives with a multires-
     Jaakko Lehtinen, and Timo Aila. Modular primitives for               olution hash encoding. ACM Trans. Graph., 41(4):102:1–
     high-performance differentiable rendering. ACM Transac-              102:15, 2022. 4, 2
     tions on Graphics, 39(6), 2020. 1                               [46] Van Nguyen Nguyen, Yinlin Hu, Yang Xiao, Mathieu Salz-
[34] Taeyeop Lee, Jonathan Tremblay, Valts Blukis, Bowen Wen,             mann, and Vincent Lepetit. Templates for 3D object pose es-
     Byeong-Uk Lee, Inkyu Shin, Stan Birchfield, In So Kweon,             timation revisited: Generalization to new objects and robust-
     and Kuk-Jin Yoon. TTA-COPE: Test-time adaptation for                 ness to occlusions. In Proceedings of the IEEE/CVF Confer-
     category-level object pose estimation. In Proceedings of             ence on Computer Vision and Pattern Recognition (CVPR),
     the IEEE/CVF Conference on Computer Vision and Pattern               pages 6771–6780, 2022. 5, 6, 7
     Recognition (CVPR), pages 21285–21295, 2023. 1, 2               [47] Van Nguyen Nguyen, Thibault Groueix, Georgy Ponimatkin,
[35] Fu Li, Shishir Reddy Vutukur, Hao Yu, Ivan Shugurov, Ben-            Vincent Lepetit, and Tomas Hodan. Cnos: A strong base-
     jamin Busam, Shaowu Yang, and Slobodan Ilic. NeRF-                   line for cad-based novel object segmentation. In Proceedings
     Pose: A first-reconstruct-then-regress approach for weakly-          of the IEEE/CVF International Conference on Computer Vi-
     supervised 6D object pose estimation. In Proceedings of              sion, pages 2134–2140, 2023. 5, 1, 3
     the IEEE/CVF International Conference on Computer Vision        [48] Brian Okorn, Qiao Gu, Martial Hebert, and David Held.
     (ICCV), pages 2123–2133, 2023. 2                                     Zephyr: Zero-shot pose hypothesis rating. In IEEE Inter-
[36] Yi Li, Gu Wang, Xiangyang Ji, Yu Xiang, and Dieter Fox.              national Conference on Robotics and Automation (ICRA),
     DeepIM: Deep iterative matching for 6D pose estimation. In           pages 14141–14148, 2021. 7
[49] Aaron van den Oord, Yazhe Li, and Oriol Vinyals. Repre-            [61] Jonathan Tremblay, Thang To, Balakumar Sundaralingam,
     sentation learning with contrastive predictive coding. arXiv            Yu Xiang, Dieter Fox, and Stan Birchfield. Deep object pose
     preprint arXiv:1807.03748, 2018. 6                                      estimation for semantic robotic grasping of household ob-
[50] Kiru Park, Timothy Patten, and Markus Vincze. Pix2Pose:                 jects. In Conference on Robot Learning (CoRL), pages 306–
     Pixel-wise coordinate regression of objects for 6D pose es-             316, 2018. 2
     timation. In Proceedings of the IEEE/CVF International             [62] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-
     Conference on Computer Vision (ICCV), pages 7668–7677,                  reit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia
     2019. 1, 2                                                              Polosukhin. Attention is all you need. Advances in Neural
[51] Keunhong Park, Arsalan Mousavian, Yu Xiang, and Dieter                  Information Processing Systems (NeurIPS), 30, 2017. 5, 6
     Fox. LatentFusion: End-to-end differentiable reconstruction        [63] Chen Wang, Roberto Martín-Martín, Danfei Xu, Jun Lv,
     and rendering for unseen object pose estimation. In Proceed-            Cewu Lu, Li Fei-Fei, Silvio Savarese, and Yuke Zhu. 6-
     ings of the IEEE/CVF Conference on Computer Vision and                  PACK: Category-level 6D pose tracker with anchor-based
     Pattern Recognition (CVPR), pages 10710–10719, 2020. 2,                 keypoints. In IEEE International Conference on Robotics
     7                                                                       and Automation (ICRA), pages 10059–10066, 2020. 1, 2
[52] Edgar Riba, Dmytro Mishkin, Daniel Ponsa, Ethan Rublee,            [64] He Wang, Srinath Sridhar, Jingwei Huang, Julien Valentin,
     and Gary Bradski. Kornia: an open source differentiable                 Shuran Song, and Leonidas J Guibas. Normalized object
     computer vision library for pytorch. In Proceedings of the              coordinate space for category-level 6D object pose and size
     IEEE/CVF Winter Conference on Applications of Computer                  estimation. In Proceedings of the IEEE International Confer-
     Vision, pages 3674–3683, 2020. 1                                        ence on Computer Vision (CVPR), pages 2642–2651, 2019.
[53] Robin Rombach, Andreas Blattmann, Dominik Lorenz,                       1, 2
     Patrick Esser, and Björn Ommer. High-resolution image              [65] Peng Wang, Lingjie Liu, Yuan Liu, Christian Theobalt, Taku
     synthesis with latent diffusion models. In Proceedings of               Komura, and Wenping Wang. NeuS: Learning neural im-
     the IEEE/CVF Conference on Computer Vision and Pattern                  plicit surfaces by volume rendering for multi-view recon-
     Recognition (CVPR), pages 10684–10695, 2022. 2                          struction. In Advances in Neural Information Processing
[54] Johannes Lutz Schönberger and Jan-Michael Frahm.                        Systems (NeurIPS), 2021. 4
     Structure-from-motion revisited. In Conference on Com-             [66] Bowen Wen and Kostas Bekris. BundleTrack: 6D pose track-
     puter Vision and Pattern Recognition (CVPR), 2016. 3                    ing for novel objects without instance or category-level 3D
[55] Ivan Shugurov, Fu Li, Benjamin Busam, and Slobodan Ilic.                models. In IEEE/RSJ International Conference on Intelli-
     OSOP: A multi-stage one shot object pose estimation frame-              gent Robots and Systems (IROS), pages 8067–8074, 2021. 2,
     work. In Proceedings of the IEEE/CVF Conference on Com-                 7
     puter Vision and Pattern Recognition (CVPR), pages 6835–           [67] Bowen Wen, Chaitanya Mitash, Baozhang Ren, and Kostas E
     6844, 2022. 1, 2, 7                                                     Bekris. se(3)-TrackNet: Data-driven 6D pose tracking
[56] Manuel Stoiber, Martin Sundermeyer, and Rudolph Triebel.                by calibrating image residuals in synthetic domains. In
     Iterative corresponding geometry: Fusing region and depth               IEEE/RSJ International Conference on Intelligent Robots
     for highly efficient 3D tracking of textureless objects. In Pro-        and Systems (IROS), pages 10367–10373, 2020. 1, 2, 6, 7, 8
     ceedings of the IEEE/CVF Conference on Computer Vision             [68] Bowen Wen, Chaitanya Mitash, Sruthi Soorian, Andrew
     and Pattern Recognition (CVPR), pages 6855–6865, 2022.                  Kimmel, Avishai Sintov, and Kostas E Bekris. Robust,
     1, 2, 7, 8                                                              occlusion-aware pose estimation for objects grasped by
[57] Jiaming Sun, Zehong Shen, Yuang Wang, Hujun Bao, and                    adaptive hands. In 2020 IEEE International Conference on
     Xiaowei Zhou. LoFTR: Detector-free local feature matching               Robotics and Automation (ICRA), pages 6210–6217. IEEE,
     with transformers. In IEEE/CVF Conference on Computer                   2020. 1
     Vision and Pattern Recognition (CVPR), pages 8922–8931,            [69] Bowen Wen, Wenzhao Lian, Kostas Bekris, and Stefan
     2021. 6                                                                 Schaal. CatGrasp: Learning category-level task-relevant
[58] Jiaming Sun, Zihao Wang, Siyu Zhang, Xingyi He,                         grasping in clutter from simulation. In International Confer-
     Hongcheng Zhao, Guofeng Zhang, and Xiaowei Zhou.                        ence on Robotics and Automation (ICRA), pages 6401–6408,
     OnePose: One-shot object pose estimation without CAD                    2022. 1
     models. In Proceedings of the IEEE/CVF Conference on               [70] Bowen Wen, Wenzhao Lian, Kostas Bekris, and Stefan
     Computer Vision and Pattern Recognition (CVPR), pages                   Schaal. You only demonstrate once: Category-level manip-
     6825–6834, 2022. 1, 2, 6, 7, 3                                          ulation from single visual demonstration. RSS, 2022. 1
[59] Zachary Teed and Jia Deng. DROID-SLAM: Deep visual                 [71] Bowen Wen, Jonathan Tremblay, Valts Blukis, Stephen
     slam for monocular, stereo, and RGB-D cameras. Advances                 Tyree, Thomas Müller, Alex Evans, Dieter Fox, Jan Kautz,
     in Neural Information Processing Systems (NeurIPS), 34:                 and Stan Birchfield. BundleSDF: Neural 6-DoF tracking and
     16558–16569, 2021. 3                                                    3D reconstruction of unknown objects. In Proceedings of
[60] Meng Tian, Marcelo H Ang, and Gim Hee Lee. Shape prior                  the IEEE/CVF Conference on Computer Vision and Pattern
     deformation for categorical 6D object pose and size estima-             Recognition (CVPR), pages 606–617, 2023. 2, 4, 7, 3
     tion. In Proceedings of the European Conference on Com-            [72] Manuel Wüthrich, Peter Pastor, Mrinal Kalakrishnan, Jean-
     puter Vision (ECCV), pages 530–546, 2020. 1, 2                          nette Bohg, and Stefan Schaal. Probabilistic object tracking
     using a range camera. In IEEE/RSJ International Conference
     on Intelligent Robots and Systems (IROS), pages 3195–3202,
     2013. 1, 2, 7, 8
[73] Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, and
     Dieter Fox. PoseCNN: A convolutional neural network for
     6D object pose estimation in cluttered scenes. In Robotics:
     Science and Systems (RSS), 2018. 2, 6, 7
[74] Lior Yariv, Yoni Kasten, Dror Moran, Meirav Galun, Matan
     Atzmon, Basri Ronen, and Yaron Lipman. Multiview neu-
     ral surface reconstruction by disentangling geometry and ap-
     pearance. Advances in Neural Information Processing Sys-
     tems (NeurIPS), 33:2492–2502, 2020. 4
[75] Ruida Zhang, Yan Di, Fabian Manhardt, Federico Tombari,
     and Xiangyang Ji. SSP-Pose: Symmetry-aware shape prior
     deformation for direct category-level object pose estimation.
     In IEEE/RSJ International Conference on Intelligent Robots
     and Systems (IROS), pages 7452–7459, 2022. 1, 2
[76] Heng Zhao, Shenxing Wei, Dahu Shi, Wenming Tan,
     Zheyang Li, Ye Ren, Xing Wei, Yi Yang, and Shiliang Pu.
     Learning symmetry-aware geometry correspondences for 6D
     object pose estimation. In Proceedings of the IEEE/CVF In-
     ternational Conference on Computer Vision (ICCV), pages
     14045–14054, 2023. 7, 3
[77] Linfang Zheng, Chen Wang, Yinghan Sun, Esha Dasgupta,
     Hua Chen, Aleš Leonardis, Wei Zhang, and Hyung Jin
     Chang. HS-Pose: Hybrid scope feature extraction for
     category-level object pose estimation. In Proceedings of
     the IEEE/CVF Conference on Computer Vision and Pattern
     Recognition (CVPR), pages 17163–17173, 2023. 2
[78] Yi Zhou, Connelly Barnes, Jingwan Lu, Jimei Yang, and
     Hao Li. On the continuity of rotation representations in neu-
     ral networks. In Proceedings of the IEEE/CVF Conference
     on Computer Vision and Pattern Recognition (CVPR), pages
     5745–5753, 2019. 5
Embeded Tokens
       FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects
                                                         Supplementary Material
   5.1. Performance on BOP Leaderboard                                          abling effective generalization as a unified framework. In
                                                                                terms of the refinement and selection networks, we first
   Fig. 8 presents our results on the BOP challenge of “6D lo-
                                                                                train them separately. We then perform end-to-end fine-
   calization of unseen objects”.2 At the time of submission,
                                                                                tuning for another 5 epochs. The whole training process is
   our FoundationPose is #1 on the leaderboard. This corre-
                                                                                conducted over synthetic data which takes about a week on
   sponds to one of the four tasks considered in this work:
                                                                                4 NVIDIA V100 GPUs. At test time, the model is directly
   model-based pose estimation for novel objects. We use the
                                                                                applied to the real world data and runs on one NVIDIA RTX
   2D detection from CNOS [47], which is the default pro-
                                                                                3090 GPU. Under the few-shot setup, rendering is obtained
   vided by the BOP challenge.
                                                                                from the neural object field which is optimized per object.
                                                                                Under the model-based setup, rendering is obtained via con-
   5.2. Implementation Details
                                                                                ventional graphics pipeline [33]. We perform denoising to
   During training, for each 3D asset we first pretrain the neu-                the depth images implemented in Warp [42], which includes
   ral object field with a random number of synthetic reference                 erosion and bilateral filtering. The pose-conditioned crop-
   images. The trained neural object field is then frozen and                   ping is implemented in batch using Kornia [52].
   provides rendering which will be mixed with the model-
                                                                                Neural Object Field. We normalize the object into the
   based OpenGL rendering as input for the pose refinement
                                                                                neural volume bound of [−1, 1]. The geometry network Ω
   and selection networks. Such combination better covers the
                                                                                consists of two-layer MLP with hidden dimension 64 and
   distribution of both model-based and model-free setups, en-
                                                                                ReLU activation except for the last layer. The intermedi-
      2 https://bop.felk.cvut.cz/leaderboards/pose-estimation-unseen-bop23/     ate geometric feature fΩ(·) has dimension 16. The appear-
   core-datasets/                                                               ance network Φ consists of three-layer MLP with hidden

   Figure 8. Screenshot on BOP leaderboard. At the time of submission, our approach outperforms the previous best method “PoMZ” (not yet published) by a
   considerable margin of 0.03 on ARCore , setting a new benchmark record on the leaderboard.
dimension 64 and ReLU activation except for the last layer,                     module can be found in the main paper (Fig. 2), where the
where we apply sigmoid activation to map the color pre-                         network architecture used for image feature embedding is
diction to [0, 1]. We implement the multi-resolution hash                       illustrated in Fig. 9. When performing the two-level hier-
encoding [45] in CUDA and simplify to 4 levels, with num-                       archical comparison, we use the same architecture for both
ber of feature vectors from 16 to 128. Each level’s fea-                        self-attention modules. Concretely, the embedding dimen-
ture dimension is set to 2. The hash table size is set to                       sion is 512, number of heads is 4, feed-forward dimension
222 . In each iteration the ray batch size is 2048. The                         is 512.
truncation distance λ is set to 1 cm. In the training loss,                     Pose Tracking. Our framework can be trivially adapted to
we = 1, ws = 1000, wc = 100. Training takes about 2k                            the pose tracking task while leveraging temporal cues. To
steps which is often within seconds.                                            do so, at each timestamp, we send the cropped current frame
Pose Hypothesis Generation. For global pose initializa-                         and the rendering using the previous pose to the pose refine-
tion, Ns = 42, Ni = 12. To train the refinement network,                        ment module. The refined pose becomes the current pose
the pose is randomly perturbed by adding translation noise                      output. This operation repeats along the video sequence.
under the magnitude of 0.02m, 0.02m, 0.05m for XYZ axis                         The first frame’s pose can be initialized by our pose estima-
respectively and rotation under the magnitude of 20◦ , where                    tion mode.
the direction is randomized. Both the rendering and input                       Synthetic Data. Objaverse assets vary extremely in the
observation are cropped based on the perturbed pose and re-                     object size and mesh complexity. Therefore, we further
sized into 160×160 before sending to the network. In the                        normalize the objects and remove the disconnected com-
training loss (Eq. 10), w1 and w2 are both set to 1. The                        ponents automatically based on the mesh edge connectivity
individual training stage takes 50 epochs. The refinement                       graph, to make the objects suitable for learning pose esti-
iteration is set to 1 for training efficiency, At test time, it is              mation. To create each scene, we randomly sampled 70 to
set to 5 for pose estimation and 1 for tracking. The com-                       90 objects and dropped them onto a platform with invisible
plete network architecture of the pose refinement module                        walls until the object velocities were smaller than a thresh-
can be found in the main paper (Fig. 2), where the network                      old. We randomly scaled the objects from 5 to 30 cm and
architecture used for image feature embedding is illustrated                    sampled the size of the platform between 1 to 1.5 meter.
in Fig. 9. In the transformer encoder, the embedding dimen-                     The LLM-aided texture augmentation is applied to each ob-
sion is 512, number of heads is 4, feed-forward dimension                       ject from Objaverse [6] with 3 to 5 different seeds for var-
is 512.                                                                         ious styles. To produce diverse and photorealistic images,
                                                                                we randomly created 0 to 5 lights with varied size, color,
                   ImageA                                  ImageB
                                                                                intensity, temperature and exposure, and Nc = 2 cameras
               7x7, 64, /2 Conv                        7x7, 64, /2 Conv         on a hemisphere with radius ranging from 0.2 to 3.0 meter
              3x3, 128, /2 Conv        Shared
                                                      3x3, 128, /2 Conv
                                                                                above the platform. We also randomize the material prop-
                                       weights
                                                                                erties, including metallicness and reflection, and textures of
              3x3, 128 ResBlock                       3x3, 128 ResBlock
                                                                             Addthe   objects and the platform. For the environment, we cre-
                                                                                  & Norm

                3x3, ResBlock                         3x3, 128 ResBlock         ated
                                                                            Feed Forwarda dome light with a random orientation and sampled
                                                                                the background from 662 HDR images obtained from Poly
                                             Concat

                                                                             AddHaven
                                                                                  & Norm [16]. In addition to RGBD rendering, we also store
                                  3x3, 256 ResBlock
                                                                                the corresponding object segmentation, camera parameters
                                                                          Multi-head Attention
                                  3x3, 256 ResBlock                             and the object poses similar to [26, 32]. In total, our dataset
                                  3x3, 512, /2 Conv                             has about 600K scenes and 1.2M images. The dataset will
                                  3x3, 512 ResBlock
                                                                                be released on the project page upon acceptance.
                                                                           Embeded Tokens
                                                                                Creating Reference Images. In the model-free few-shot
                                  3x3, 512 ResBlock
                                                                                setup, similar to [22], on YCB-Video and LINEMOD
Figure 9. Network architecture for image feature embedding used in pose         datasets, we select a subset of reference images Sr from the
refinement and selection networks. The ResBlock is from ResNet-34 [17].         training split St . To do so, we first initialize the selection set
Pose Selection. The individual training for the selection                       by choosing the image with the maximum number of pixels
network takes 25 epochs, where we perform the similar                           according to the mask. Next, for each of the remaining im-
pose perturbation to refinement network, and the number of                      age, we compute its rotational geodesic distance to all the
pose hypotheses K = 5. During the end-to-end fine-tuning,                       selected reference image, and choose the remaining frame
the pose hypotheses come from the output of the refinement                      based on:
network. In the training loss (Eq. 11), α is set to 0.1. The                                  i^*= \argmaxB _{i \in \mathbb {S}_t, i \notin \mathbb {S}_r} \left ( \min _{j \in \mathbb {S}_r} D(\boldsymbol {R}_i, \boldsymbol {R}_j) \right ),   (15)
valid positive sample’s rotation threshold d is set to 10◦ .
The complete network architecture of the pose refinement                      where D(·, ·) denotes the geodesic distance on SO(3). We
     repeat the process until enough number of reference images                                                        external 2D detection, which is obtained from methods such
     is obtained, which is typically set to 16 following [22].                                                         as CNOS [47], or Mask-RCNN [18]. We observe false or
         For applications in the wild when the ground truth object                                                     missing detection frequently bottlenecks the 6D pose esti-
     pose is not readily available, we can leverage off-the-shelf                                                      mation. In future work, an end-to-end framework for novel
                                                 Decreasing pose rank

     SLAM algorithms [54, 59, 71] to compute the poses from
       Observation
                         Ours
                                                                                                                       object detection, 6D pose estimation and tracking would
     the video. Please refer to our supplemental video for rele-                                                       be of interest. Additionally, another typical failure mode
OnePose++
     vant results.            LatentFusion
                         W/o hierarchical comparison

                                                                                                                      Ours
                                                                                                                       due to a combination of multiple challenges is illustrated in
                                                                                                                       Fig. 11.
                     5.3. Details on Disentangled Representation for
                          Pose Updates.                                                                                 5.5. Acknowledgement
                     y                                                       y                 y
                                                                                                                        We would like to thank Tianshi Cao for the valuable dis-
                                                                                                                        cussions; NVIDIA Isaac Sim and Omniverse team for the
                                                                        ∆R                ∆t
                                                 x                                                                      support on synthetic data generation.
                                                                                 x
                                                                                                              x
                                                                  x                   x                   x
                     y                                                       y                 y

                                                                        ∆R                ∆t
                                                 x
                                                                                 x                                x

                                                                  x                   x                   x
                         Figure 10. Illustration of disentangled representation for pose updates.

                     As mentioned in the main paper, we disentangle the trans-
                     lation and rotation for two reasons. First, ∆t ∈ R3 and
                     ∆R ∈ SO(3) are variables in two different spaces. There-
                     fore, compared to using a single linear projection at the end
                     to predict them jointly, the early disentanglement benefits
                     the learning process. Second, the disentanglement allows
                     us to represent both ∆t and ∆R in the camera’s coordinate
                     frame, such that ∆t is independent of ∆R. This is illus-
                     trated by a 2D example in Fig. 10. The top row shows the
                     commonly used homogeneous representation, in which the
                     pose update is: x′ = ∆T x = ∆Rx + ∆t. Thus, ∆t is
                     applied based on the updated local coordinate system of the
                     disk (object) after applying ∆R, so that the rotation affects
                     the translation. In contrast, theGTbottom row shows
                                                                      Oursthe disen-
                     tanglement of ∆t and ∆R, which resolves the dependency
                     issue and stabilizes training.

                                  Observation                                    GT                Ours

                     Figure 11. Failure mode. Under the combination of multiple challenges
                     including texture-less, severe occlusion, and limited edge cues, our method
                     fails to estimate the correct orientation.

                     5.4. Limitations
                     Similar to related works [2, 19, 22, 32, 58, 76], our approach
                     focuses on 6D pose estimation and tracking, and relies on
