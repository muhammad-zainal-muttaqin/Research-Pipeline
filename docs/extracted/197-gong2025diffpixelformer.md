---
source_id: 197
bibtex_key: gong2025diffpixelformer
title: DiffPixelFormer: Differential Pixel-Aware Transformer for RGB-D Indoor Scene Segmentation
year: 2025
domain_theme: Segmentasi RGB-D
verified_pdf: 197_DiffPixelFormer Segmentasi Scene RGB-D Indoor.pdf
char_count: 91324
---

IEEE TRANSACTIONS ON MULTIMEDIA                                                                                                                        1

                                              DiffPixelFormer: Differential Pixel-Aware
                                         Transformer for RGB-D Indoor Scene Segmentation
                                              Yan Gong , Jianli Lu , Yongsheng Gao* , Jie Zhao , Senior Member, IEEE, Xiaojuan Zhang , Senior
                                                                     Member, IEEE, and Susanto Rahardja , Fellow, IEEE

                                            Abstract—Indoor semantic segmentation is fundamental to
                                         computer vision and robotics, supporting applications such as
                                         autonomous navigation, augmented reality, and smart envi-
arXiv:2511.13047v1 [cs.CV] 17 Nov 2025

                                         ronments. Although RGB-D fusion leverages complementary
                                         appearance and geometric cues, existing methods often depend
                                         on computationally intensive cross-attention mechanisms and
                                         insufficiently model intra- and inter-modal feature relationships,
                                         resulting in imprecise feature alignment and limited discrim-
                                         inative representation. To address these challenges, we pro-
                                         pose DiffPixelFormer, a differential pixel-aware Transformer for
                                         RGB-D indoor scene segmentation that simultaneously enhances
                                         intra-modal representations and models inter-modal interactions.
                                         At its core, the Intra-Inter Modal Interaction Block (IIMIB)
                                         captures intra-modal long-range dependencies via self-attention
                                         and models inter-modal interactions with the Differential–Shared
                                         Inter-Modal (DSIM) module to disentangle modality-specific and
                                         shared cues, enabling fine-grained, pixel-level cross-modal align-
                                         ment. Furthermore, a dynamic fusion strategy balances modality
                                         contributions and fully exploits RGB-D information according to
                                         scene characteristics. Extensive experiments on the SUN RGB-
                                         D and NYUDv2 benchmarks demonstrate that DiffPixelFormer-
                                         L achieves mIoU scores of 54.28% and 59.95%, outperforming
                                         DFormer-L by 1.78% and 2.75%, respectively. Code is available
                                         at https://github.com/gongyan1/DiffPixelFormer.
                                           Index Terms—RGB-D Fusion, Indoor Scene Segmentation,
                                         Cross-Modal Attention, Differential Feature Modeling.

                                                                  I. I NTRODUCTION                                    Fig. 1. Comparison of receptive fields among different cross-attention-based
                                                                                                                      multimodal fusion methods.

                                         I   NDOOR semantic segmentation is crucial for applications
                                             such as autonomous navigation [1], [2], [3], [4], [5],
                                         augmented reality [6], and smart homes [7], [8], [9]. RGB-                   Exchange-based methods emphasize efficiency by leverag-
                                         based methods [10], [11], [12] suffer from illumination and                  ing spatial correspondences for information substitution,
                                         texture variations, while depth-based ones are affected by                   e.g., Wang et al. [16] with position mapping and Token-
                                         noise and lack appearance cues [13], [14], [15]. Consequently,               Fusion [17] using token substitution. However, such ap-
                                         leveraging the complementary strengths of RGB-D modalities                   proaches often cause irreversible loss of modality-specific
                                         thus becomes essential for improving robustness and accuracy                 features, particularly in complementary modalities, thereby
                                         in indoor semantic segmentation.                                             limiting performance. In contrast, interaction-based methods
                                            In multimodal learning, fusion strategies are broadly cate-               explicitly model cross-modal dependencies to enhance rep-
                                         gorized into exchange-based and interaction-based paradigms.                 resentational capacity. Early works used simple concatena-
                                                                                                                      tion [18], while recent studies increasingly rely on attention
                                            This work was supported by the National Outstanding Youth Science         mechanisms [13], [14], [19], [20], [21], with cross-attention
                                         Fund Project of National Natural Science Foundation of China (Grant no.
                                         52025054). (Corresponding author: Yongsheng Gao)                             (CA) [22], [23] proving effective for capturing fine-grained
                                            Yan Gong, Jianli Lu, Yongsheng Gao, and Jie Zhao are with the State Key   relations. However, global dependency modeling incurs pro-
                                         Laboratory of Robotics and System, Harbin Institute of Technology, Harbin    hibitive complexity, as shown in Fig. 1 (a). To address this,
                                         150001, China. (email: gongyan2020@foxmail.com, lujianli364@163.com,
                                         gaoys@hit.edu.cn, jzhao@hit.edu.cn).                                         PVTransformer [24] and Swin Transformer [25] introduce
                                            Xiaojuan Zhang is with the Institute for Infocomm Research, A*STAR,       sparse connections, local windows, or downsampled features,
                                         Singapore. (email: xiaojuanzhang@ieee.org).                                  as shown in Fig. 1 (b) and (c). However, these methods remain
                                            Susanto Rahardja is with the College of Information Science and Elec-
                                         tronic Engineering, Zhejiang University, Hangzhou 310027, China (e-mail:     computationally heavy and degrade pixel-level alignment, lim-
                                         susantorahardja@ieee.org).                                                   iting local cross-modal correlation modeling in RGB-D data.
IEEE TRANSACTIONS ON MULTIMEDIA                                                                                                                                                                                                 2

To address this, we propose differential pixel-aware cross-                                      Params (M) vs mIoU (SUN RGBD)                                                 Params (M) vs mIoU (NYUDv2)
                                                                                                                                  DiffPixelFormer-L              60                                         DiffPixelFormer-L
attention (PACA), as illustrated in Fig. 1 (d), which efficiently                 54
captures fine-grained, pixel-level cross-modal dependencies.                                                 DiffPixelFormer-M                                                         DiffPixelFormer-M
                                                                                                                                                                 58
   Through a systematic investigation of existing RGB-D                                DiffPixelFormer-S
                                                                                  53                                                                                  DiffPixelFormer-S CMX-B5
fusion methods based on interaction-based paradigms, we                                                                                                          56
                                                                                                                                                                                      CMX-B4
                                                                                                              CMX-B5
identify two primary limitations. First, most approaches                                                    CMX-B4

                                                                                                                                                      mIoU (%)
                                                                                  52

                                                                       mIoU (%)
[6], [7], [26], [27] fail to jointly consider intra- and inter-modal                          PACA                                                                        PACA
                                                                                                                                                                 54
                                                                                                                                                                                  PGDENet
feature modeling: intra-modal representations lack sufficient
                                                                                  51                   PGDENet
capture of long-range dependencies and global context, limit-                              Baseline                                                              52 Baseline
ing single-modality expressiveness, while inter-modal interac-                                LCA
                                                                                  50                                                                                                                              CA
tions often rely on coarse-grained cross-attention, which strug-                                                                        CA
                                                                                                                                                                 50
                                                                                                                                                                          LCA
gles to achieve pixel-level alignment and fine-grained correla-                                       SWA                                                                        SWA
                                                                                  49                                                                             48
tion modeling. Second, existing methods [1], [14], [19], [28]                          0         100        200       300        400     500                          0     100        200       300       400     500
                                                                                                                  Params (M)                                                                 Params (M)
do not jointly model shared and differential information
across modalities. Although RGB and depth modalities exhibit
                                                                       Fig. 2. Performance comparison of different attention variants on SUN RGB-
common structural cues such as edges and contours, they                D and NYUDv2 in terms of parameters and mIoU. “CA” denotes Cross-
also contain complementary features, including RGB texture             Attention, “SWA” denotes Shifted Window Attention, “LCA” denotes Local
and color and depth geometry. Current approaches [19], [29]            Cross-Attention, and “PACA” denotes Pixel-Aware Cross-Attention.
typically ignore this distinction and perform undifferentiated
aggregation, weakening the discriminative power and represen-                                benchmarks demonstrate that DiffPixelFormer consis-
tational capacity of the fused features and constraining overall                             tently outperforms state-of-the-art methods in segmen-
performance.                                                                                 tation accuracy while achieving a favorable trade-off
   In this paper, we propose DiffPixelFormer, a Differen-
                                                                                             between performance and efficiency.
tial Pixel-aware Transformer for RGB-D indoor scene seg-
mentation that simultaneously strengthens intra-modal repre-
sentations and models inter-modal interactions. Specifically,                                                                  II. R ELATED W ORK
the Intra-Inter Modal Interaction Block (IIMIB) explicitly             A. RGB-D Indoor Semantic Segmentation
separates intra- and inter-modal learning. Intra-modal inter-             Indoor semantic segmentation is a fundamental task in
actions leverage self-attention (SA) to capture long-range             computer vision and robotic perception, supporting applica-
dependencies and global context, enhancing the robustness              tions such as autonomous navigation, augmented reality, and
and semantic completeness of single-modality features, while           smart homes. RGB-based methods, including FCN [30], U-
inter-modal interactions employ the Differential–Shared Inter-         Net [31], TokenFusion-B5 [17], and DFormerV2 [26], have
Modal (DSIM) module to disentangle modality-specific and               achieved remarkable progress but remain vulnerable to illu-
shared information. Within DSIM, a difference discriminator            mination changes, texture degradation, occlusion, and noise.
ensures precise pixel-level alignment and models modality-             To improve robustness under weak lighting and motion blur,
specific discrepancies, whereas a similarity discriminator ex-         recent approaches integrate depth cues, which provide ge-
tracts shared structural cues such as edges and contours.              ometric priors complementary to appearance features [28],
Furthermore, an adaptive fusion factor dynamically balances            [32]. Building on this, DFormer [27] introduced large-scale
differential and shared cues to produce discriminative, se-            RGB-D pretraining on ImageNet-1K, while DFormerV2 [26]
mantically consistent cross-modal representations. Extensive           treats depth as implicit geometric priors. PDDM [33] alle-
experiments on the NYUv2 and SUN RGB-D benchmarks                      viates depth scarcity via pseudo-depth generation, and EAC-
demonstrate that DiffPixelFormer achieves significantly su-            Net [34] designs lightweight fusion for resource-constrained
perior segmentation performance compared to state-of-the-art           platforms. CMX [35] enables multi-scale cross-modal inter-
methods. Furthermore, as illustrated in Fig. 2, DiffPixelFormer        action, ACNet [36] applies attention-based adaptive fusion,
markedly reduces parameter count relative to representative            and SegFormer [37] demonstrates Transformer-based unified
cross-attention schemes, thereby attaining a favorable balance         representation learning.
between efficiency and accuracy. The contribution of this                 Difference: Existing methods rely on coarse cross-attention,
article can be summarized as follows:                                  which limits pixel-level alignment and incurs substantial com-
   • We propose DiffPixelFormer, a novel Differential Pixel-           putational overhead. DiffPixelFormer enhances intra-modal
      aware Transformer for RGB-D indoor scene segmenta-               features and models inter-modal relations via pixel-aware
      tion, whose core IIMIB jointly models intra-modal and            differential and similarity attention, achieving precise and
      inter-modal interactions to fully exploit complementary          efficient representations.
      and shared information.
   • We introduce DSIM as the inter-modal component of
      IIMIB, which disentangles modality-specific and shared           B. Multimodal Fusion Strategies
      cues to achieve fine-grained, pixel-level alignment and             Multimodal fusion in RGB-D segmentation harnesses the
      semantically consistent cross-modal representations.             complementary strengths of RGB images, which provide
   • Extensive experiments on NYUv2 and SUN RGB-D                      rich appearance and semantic information, and depth maps,
IEEE TRANSACTIONS ON MULTIMEDIA                                                                                                    3

which offer stable geometric priors. Existing research has          the updated RGB and depth features. The computational com-
mainly explored three categories of fusion strategies. (1)          plexity of the above operation is O(N 2 d), where the quadratic
Interaction-based fusion models cross-modal dependencies to         growth imposes a heavy burden when handling large-scale
exploit complementarity, as in ACNet [36], RFNet [38], and          data or high-resolution images. Furthermore, cross-attention
Primkd [39], which employ cross-modal attention to dynam-           mechanisms typically rely on coarse-grained feature aggre-
ically weight features. However, the global modeling nature         gation, which hinders pixel-level alignment and fine-grained
of cross-modal attention necessitates dense pairwise interac-       correspondence modeling, thereby limiting the granularity and
tions between modalities, substantially inflating computational     expressiveness of multimodal fusion.
and memory costs, and thus hindering real-time deployment
in practical scenarios. (2) Alignment-based fusion enforces         B. Network Overview
feature-level consistency to alleviate distributional gaps and         DiffPixelFormer adopts a mainstream encoder-decoder ar-
noise. For instance, GeminiFusion [29] integrates intra- and        chitecture, as illustrated in Fig. 3. Initially, RGB and depth
inter-modal attention with noise control, while CMX [35]            images are converted into encoded features X0R and X0D via
scales fusion to RGB, depth, and LiDAR. Such approaches             overlapped patch embedding. These encoded features are then
often neglect differential modality cues and impose excessive       sequentially fed into four Transformer Blocks, progressively
constraints on feature interactions, thereby limiting the ex-       extracting and generating multi-resolution feature maps, de-
ploitation of modality-specific representations. (3) Backbone-      noted as XiR and XiD for i = 1, 2, 3, 4. For each Transformer
enhanced fusion introduces adaptive modules or dual-path                                         R
                                                                    Block, the input features Xi−1          D
                                                                                                     and Xi−1   are processed by M
designs to strengthen integration efficiency and representation     Intra-Inter Modal Interaction Blocks (IIMIBs) to produce the
robustness [37], [40], [41]. These architectures frequently         output features XiR and XiD , which can be formulated as:
depend on elaborate network designs, which not only elevate
implementation and optimization complexity, but also impede            (XiR , XiD ) = FM ◦ FM −1 ◦ · · · ◦ F1 (Xi−1
                                                                                                                R      D
                                                                                                                    , Xi−1 ),    (2)
scalability and adaptability across heterogeneous multimodal        where FM denotes the operation of the M -th IIMIB. In
scenarios.                                                          practice, the four Transformer Blocks employ 3, 6, 4, and 3
   Difference: Existing fusion strategies neglect the distinction   IIMIBs, respectively.
between intra-modal and inter-modal interactions and fail to           Each IIMIB applies modality-specific layer normalization,
separate shared from modality-specific information. DiffPix-        followed by intra- and inter-modal interaction modules that re-
elFormer addresses these limitations by combining intra-modal       spectively capture long-range dependencies and jointly model
self-attention with a pixel-wise DSIM module, explicitly dis-       shared and specific representations. Subsequent normalization
entangling shared and differential cues to enable fine-grained,     and overlapped patch merging enable spatial aggregation and
discriminative cross-modal representations.                         dimensionality reduction, while residual connections preserve
                                                                    information flow and mitigate feature degradation. Notably,
                         III. M ETHOD                               layer normalization is applied independently to each modality
                                                                    to account for distributional disparities, whereas the remaining
   In this section, we first review commonly used cross-            layers share parameters to improve computational efficiency.
attention mechanisms in Section III-A. We then present the          The decoder fuses multi-scale features and refines them
overall architecture of DiffPixelFormer in Section III-B, fol-      through upsampling and dual MLP layers to generate the final
lowed by a detailed discussion of intra- and inter-modal feature    segmentation map.
interactions in Section III-C.
                                                                    C. Intra-Inter Modal Interaction Block (IIMIB)
A. Cross-Attention Review                                              Due to substantial differences in data distribution, semantic
   Cross-Attention (CA) is widely employed in multimodal            structure, and noise across modalities, direct fusion may am-
fusion to capture inter-modal dependencies by computing             plify noise or obscure useful information. To address this, we
attention weights between the queries of one modality and           introduce the IIMIB module (see Fig. 3 (c)), which explicitly
the key-value pairs of another, thereby enabling effective          separates intra-modal and inter-modal interactions to better
information transfer and integration. For N patches, let the        exploit multimodal features. Intra-modal interaction captures
RGB and depth feature maps be XR , XD ∈ RN ×d , where d             long-range dependencies and enhances feature discriminability
is the feature dimension, and the cross-attention computation       within each modality, while inter-modal interaction integrates
can then be defined as follows:                                     complementary information across modalities. This hierarchi-
                                                                    cal strategy enables more effective multimodal collaboration,
       YR = CA XR WQ , XD WK , XD WV + XR
                                                
                                                                    as detailed below.
       YD = CA XD WQ , XR WK , XR WV + XD
                                                
                                                                       1) Intra-Modal Interaction: To fully exploit the intrinsic
                                        !                 (1)       characteristics of each modality and enhance the quality of
                                  QKT
       CA(Q, K, V) = Softmax √             V                        inputs for inter-modal fusion, we employ an intra-modal
                                     d                              interaction module based on self-attention (SA) for both RGB
                                                                    and depth modalities XiR and XiD , defined as follows:
where WQ , WK , WV are learnable projection matrices for
queries (Q), keys (K), and values (V), YR and YD denote                         (XiR,Intra , XiD,Intra ) = SA(XiR , XiD ),       (3)
IEEE TRANSACTIONS ON MULTIMEDIA                                                                                                                                                                                                                               4

                                                                                                          (a) Encoder                                                             (b) Decoder

                                          Embedding
                                          Over Patch
  RGB

                                                                                                                                                               Decoder Layer 1

                                                                                                                                                                                                       Decoder Layer 2
                                                                             Transformer

                                                                                                     Transformer

                                                                                                                     Transformer

                                                                                                                                          Transformer
                                                                               Block 1

                                                                                                       Block 2

                                                                                                                       Block 3

                                                                                                                                            Block 4
                                          Embedding
                                          Over Patch
  Depth

                                                                                                                                                                                                                                Segmentation
                                                                                                                                                                                       𝐻 𝑊
                                                                                                                                                                                        × ×4𝐶
                                                                                                                                                                                       4 4

                                         (c) Transformer Block                                                                                                                    $
                                                                                                                                                                                 𝑉&'                                     𝑉!%

                                                                                                                            $,,-./0
                                                                                                                                                      Linear

                                                                                                                                                                                                                               PACA
                                                                                                         ×M                                       Transformation
                                                                                                                                                                                  $
                                                                                                                                                                                 𝐾&'             𝐾!$                                    ⊕     $
                                                                                                                                                                                                                                            𝑌!,+

                                                                                                                           𝑥!,+

                                                                                                                                                                                                                                                   MLP
          Normalization

                                              Normalization

                                                                                     Normalization
                                                                                                                                                                                  $
                                                                                                                                                                                 𝑄&'
             Layer

                                                 Layer

                                                                                        Layer

                                         ⊕                                   ⊕                                                                      Difference                   𝐷!$     ⊗         𝑁($ 𝑁)$

                                                                                                                                        −
                          Intra-Model

                                                              Inter-Model

                                                                                                       Embedding
                                                                                                       Over Patch
                           Interaction

                                                               Interaction

                                                                                                                                                   Discriminator                 𝐷!%     ⊗

                                                                                                                                                                                                                                                   MLP
 $
𝑋!"#                                                                                                                𝑋!$                                                                                                               (d) DSIM
                                                                                                                                                    Similarity
                                                                                                                                                                                 𝑆!          ⊗     𝑁(% 𝑁)%

                                                                                                                                        C
          Normalization

                                              Normalization

                                                                                     Normalization

                                                                                                                                                   Discriminator

                                                                                                                                                                                                                                                   Upsample
                                         ⊕                                   ⊕
             Layer

                                                 Layer

                                                                                        Layer

                                                                                                                                                                                  %
                                                                                                                                                                                 𝑄&'
                                                                                                                             %,,-./0                  Linear

                                                                                                                                                                                                                               PACA
                                                                                                                                                                                                                                              $
                                                                                                                                                  Transformation
                                                                                                                                                                                  %
                                                                                                                                                                                 𝐾&'             𝐾!%                                    ⊕   𝑌!,+
                                                                                                                            𝑥!,+
 %
𝑋!"#                                                                                                 IIMIB          𝑋!%
                                                                                                                                                                                  %
                                                                                                                                                                                 𝑉&'                                     𝑉!%

Fig. 3. The overall architecture of DiffPixelFormer adopts an encoder–decoder design, where the encoder employs multiple Intra-Inter Modal Interaction
Blocks (IIMIBs) for efficient intra- and inter-modal fusion, and the decoder restores spatial and semantic details via multi-scale aggregation.

where XiR,Intra and XiD,Intra denote the outputs with enhanced                                                                         implemented as two-layer MLPs with a softmax activation.
features after intra-modal interaction. By adaptively attending                                                                        Note that, due to the inherent asymmetry of inter-modal feature
to salient information and modeling long-range dependencies                                                                            differences, bidirectional modeling is required to fully capture
within each modality, more discriminative and comprehensive                                                                            complementary information, whereas the similarity score is
intra-modal representations are obtained, serving as high-                                                                             uniquely defined for each feature pair without the need for
quality inputs for subsequent multimodal fusion.                                                                                       directional distinction.
   2) Inter-Modal Interaction: Existing cross-attention-based                                                                             Subsequently, features from different modalities are pro-
multimodal fusion methods exploit cross-modal correlations                                                                             jected via linear transformation LT to generate the QLT ,
but often neglect complementary modality-specific cues and                                                                             KLT , and VLT . In standard cross-attention, there is a tendency
suffer from heavy computational and parameter overhead due                                                                             to disproportionately learn from another modality, resulting
to dense token interactions, many of which are uninformative.                                                                          in over-reliance on similar components and neglect of less
To address these issues, we argue that inter-modal fusion                                                                              similar yet potentially important information. To mitigate this,
should focus on corresponding spatial locations, emphasizing                                                                           we modulate the keys of each modality using the previously
discriminative and differential modality information. Accord-                                                                          computed DiR , DiD , and Si scores, and replace the keys in
ingly, we propose DSIM (see Fig. 3 (d)), which adaptively                                                                              Eq (1) as follows:
extracts fine-grained modality-specific features and computes
                                                                                                                                                        KiR = [αR ∗ QR     R    R   R
                                                                                                                                                                     LT ∗ Di , β ∗ QLT ∗ Si ],
cross-modal similarity for shared representation.                                                                                                                                                                                                     (5)
   Firstly, we design two lightweight relation discriminators: a                                                                                        KiD = [αD ∗ QD     D    D   D
                                                                                                                                                                     LT ∗ Di , β ∗ QLT ∗ Si ],
difference discriminator and a similarity discriminator. Given                                                                         where α and β denote learnable factors. Furthermore, we
the input features XiR,Intra and XiD,Intra , the normalized differ-                                                                    construct the embeddings ViR and ViD by combining the
ence and similarity scores are computed as follows:                                                                                    differential feature representations with the complementary
                                R,Intra                                                                                                modality features, formulated as:
                                        − XiD,Intra )
                 R        R
                Di = fd (Xi
                
                                                                                                                                        ViR = [VLT
                                                                                                                                                R     D
                                                                                                                                                   − VLT    D
                                                                                                                                                         , VLT ],                                ViD = [VLT
                                                                                                                                                                                                         D     R
                                                                                                                                                                                                            − VLT    R
                                                                                                                                                                                                                  , VLT ], (6)
                  DiD = fdD (XiD,Intra − XiR,Intra )            (4)
                                                                                                                                       where the ordering of ViR and ViD is kept consistent with KiR
                
                             R,Intra    D,Intra
                  Si = fs ([Xi        , Xi       ])
                                                                                                                                       and KiD to facilitate the computation of pixel-aware cross-
where DiR , DiD , Si ∈ [0, 1] quantify the modality-specific dis-                                                                      attention.
tinction for RGB and Depth, and the shared similarity, respec-                                                                            However, deriving both Q and K from the same modality
tively. [.] denotes the concatenation operation. Here, fd (·) and                                                                      introduces self-referential bias in the attention scores, which
fs (·) denote the difference and similarity discriminators, both                                                                       overemphasizes intra-modal correlations at the expense of
IEEE TRANSACTIONS ON MULTIMEDIA                                                                                                  5

                                                                                                  k
complementary cross-modal cues, ultimately limiting the ef-                                   1X      pii
                                                                                     mAcc =                  ,               (10)
fectiveness of multimodal fusion. To address this limitation,                                 k i=1 kj=1 pij
                                                                                                   P
adaptive noise terms N R and N D are injected at different
layers, formulated as:                                                                                Pk
                                                                                                          i=1 pii
         ′                          ′                                              Pixel Acc = Pk         Pk         .       (11)
      QR      R
        i = Xi W ,
                    Q
                                 QD      D
                                   i = Xi W ,
                                               Q
                                                                                                      i=1    j=1 pij
         ′                          ′
      KiR = [NKR
                 , KiR ]W K ,    KiD = [NKD
                                            , KiD ]W K ,     (7)   Here, k denotes the total number of classes, and pij repre-
         ′                          ′
      ViR = [NVR , ViR ]W V ,    ViD = [NVD , ViD ]W V ,           sents the number of pixels with ground-truth label i that are
                                                                   predicted as class j. Specifically, mIoU quantifies the mean
thereby increasing the diversity of feature representations and    intersection over union between predicted and ground truth
enabling more effective cross-modal integration. The outputs       regions across all classes, mAcc represents the average pixel-
YiR and YiD are obtained via pixel-aware cross-attention,          wise accuracy computed per class, and Pixel ACC denotes
defined as:                                                        the overall proportion of correctly classified pixels in the
                          ′     ′     ′     R,Intra
           R
          Yi,k = CA(QR      D       D
                     i,k , Ki,k , Vi,k ) + Xi,k     ,              dataset. Among these metrics, mIoU is regarded as the primary
           D              ′     ′     ′     D,Intra
                                                             (8)   indicator for evaluating segmentation performance.
          Yi,k = CA(QD      R       R
                     i,k , Ki,k , Vi,k ) + Xi,k     ,
where k denotes the k-th token. Notably, cross-attention is
restricted to tokens at the same spatial location rather than      B. Experiment setting and training details
across all tokens, thereby preserving spatial correspondence          In multimodal semantic segmentation, our training set-
while enabling fine-grained multimodal interaction.                tings largely follow the TokenFusion [17]. Experiments are
                                                                   conducted on NVIDIA V100 GPUs for both the NYUDv2
                      IV. E XPERIMENT                              and SUN RGB-D datasets, under the same environmental
                                                                   conditions as the original works. The encoder backbone is
   This section presents a comprehensive evaluation of Diff-
                                                                   adapted from SegFormer [37], pre-trained only on ImageNet-
PixelFormer. Sections IV-A and IV-B detail the experimental
                                                                   1K. For both datasets, we adopt the training protocols of
setup and implementation. Section IV-C compares our method
                                                                   TokenFusion, ensuring consistency in batch size, optimizer,
with state-of-the-art approaches, followed by quantitative anal-
                                                                   learning rate scheduler, and other key hyperparameters. In our
ysis in Section IV-D. Ablation studies in Section IV-E examine
                                                                   DiffPixelFormer, the number of attention heads is fixed at 8,
the impact of fusion strategies, self-attention mechanisms,
                                                                   with a drop path rate of 0.4 and a drop rate of 0.0 to mitigate
relation discriminators, and backbone on performance.
                                                                   overfitting. Except for setting the learning rate to 2 × 10−4 ,
                                                                   all other hyperparameters, including batch size, optimizer, and
A. Datasets and Evaluation Settings                                weight decay, follow those of TokenFusion [17].
SUN RGB-D: SUN RGB-D [42] is a large-scale RGB-D
dataset designed for indoor scene understanding, containing
                                                                   C. Comparison with SOTA Methods
10,335 images with pixel-level semantic annotations. It pro-
vides a standard split of 5,285 training and 5,050 testing            To thoroughly evaluate the effectiveness and superiority
samples, and incorporates data from NYU Depth V2 [32]              of the proposed DiffPixelFormer, we conduct extensive com-
and Berkeley B3DO [43]. The dataset encompasses a broad            parative experiments on two widely used RGB-D semantic
spectrum of indoor environments, including bedrooms, living        segmentation benchmarks, SUN RGB-D and NYUDv2, as
rooms, offices, kitchens, and classrooms, serving as a compre-     shown in Table I. The results demonstrate that DiffPixelFormer
hensive benchmark for scene understanding research.                consistently outperforms state-of-the-art methods, achieving
NYUDv2: NYUDv2 [32] is a widely-used RGB-D dataset for             the best performance with mIoU scores of 54.28% on SUN
indoor scene understanding, comprising 1,449 densely anno-         RGB-D and 59.95% on NYUDv2. A more detailed analysis
tated images with corresponding depth maps, captured using         of the experiment results is presented below.
a Microsoft Kinect sensor across 464 distinct indoor scenes.          1) Results on SUN RGB-D: As shown in Table I,
Each annotated image provides both class and instance-level        DiffPixelFormer-S achieves 52.84% mIoU on the SUN RGB-
segmentation. Additionally, the dataset includes 407,024 un-       D dataset, clearly surpassing MultiMAE [47], ShapeConv [45],
labeled frames. NYUDv2 covers a broad spectrum of indoor           TokenFusion [17], and GeminiFusion [29] under compara-
environments, such as dining rooms, living rooms, bedrooms,        ble parameter budgets, highlighting superior parameter ef-
bathrooms, and offices.                                            ficiency. With deeper backbones, DiffPixelFormer-M and
Evaluation metrics: To quantitatively assess the segmentation      DiffPixelFormer-L further improve performance to 53.69%
performance, we employ three widely used evaluation metrics,       and 54.28% mIoU, gains of 0.85% and 1.44% over
namely mean Intersection over Union (mIoU), mean Pixel             DiffPixelFormer-S, confirming strong scalability. Under the
Accuracy (mAcc), and Pixel Accuracy (Pixel Acc). Their             same MiT-B5 backbone [37], DiffPixelFormer-M consis-
mathematical definitions are given as follows:                     tently outperforms TokenFusion-B5 [17], CMX-B5 [35], and
                      k
                                                                   DPLNet [51], underscoring robustness and competitiveness
                  1X              pii                              across methods. Moreover, DiffPixelFormer-L exhibits strong
         mIoU =                                   ,          (9)
                  k i=1 kj=1 pij + kj=1 pji − pii                  competitiveness in large-scale settings, reaching 54.28%,
                       P          P
IEEE TRANSACTIONS ON MULTIMEDIA                                                                                                    6

                                                                 TABLE I
 C OMPARISON OF EXISTING STATE - OF - THE - ART METHODS ON THE SUN RGB-D AND NYUDV 2 DATASETS , WHERE BOLD AND UNDERLINED VALUES
         INDICATE THE BEST AND SECOND - BEST PERFORMANCES , AND “–” DENOTES RESULTS NOT REPORTED IN THE ORIGINAL PAPERS .

                                                                                     SUN RGB-D             NYUDv2
 Model                     Backbone               Publication Year Param(M)
                                                                                mIoU Pixel Acc mAcc mIoU Pixel Acc mAcc
 SGNet [44]               ResNet-101                   TIP     2021     64.70   48.60     -      -   51.10    -      -
 ESANet [1]               ResNet-34                  ICRA      2021     31.20   48.20     -      -   50.30    -      -
 ShapeConv [45]           ResNeXt-101                ICCV      2021     86.80   48.60     -      -   51.30    -      -
 CEN [46]                 ResNet-50                    TIP     2022        -    51.10   83.50  63.20 52.50  77.70  65.00
 MultiMAE [47]            ViT-Base                  ECCV       2022     95.20   51.10     -      -   56.00    -      -
 Omnivore [48]            Swin-Small                CVPR       2022     95.70     -       -      -   54.00    -      -
 PGDENet [6]              ResNet-34                  TMM       2022    100.70   51.00     -      -   53.70    -      -
 EMSANet [49]             ResNet-34                 IJCNN      2022     46.90   50.90     -      -   59.00    -      -
 TokenFusion-B2 [17]      MiT-B2                    CVPR       2022     26.00   50.30     -      -   53.30    -      -
 TokenFusion-B3 [17]      MiT-B3                    CVPR       2022     45.90   51.40   82.80  63.60 54.20  79.00  66.90
 TokenFusion-B5 [17]      MiT-B5                    CVPR       2022     83.30   51.80   83.10  63.90 55.10  79.10  67.50
 CMX-B2 [35]              MiT-B2                      TITS     2023     66.60   49.70     -      -   54.40    -      -
 CMX-B4 [35]              MiT-B4                      TITS     2023    139.90   52.10     -      -   56.30    -      -
 CMX-B5 [35]              MiT-B5                      TITS     2023    181.10   52.40     -      -   56.90    -      -
 CMNext [50]              MiT-B4                    CVPR       2023    119.60   51.90     -      -   56.90    -      -
 PGDENet [6]              UNet                       TMM       2023        -    51.00     -    61.70 53.70    -    66.70
 DPLNet [51]              MiT-B5                     IROS      2024        -    52.80     -      -   58.30    -      -
 GeminiFusion [29]        MiT-B3                     ICML      2024     75.80   52.70   83.30  64.60 56.80  79.90  69.90
 DFormer-T [27]           DFormer-Tiny               ICRL      2024      6.00   48.80     -      -   51.80    -      -
 DFormer-S [27]           DFormer-Small              ICRL      2024     18.70   50.00     -      -   53.60    -      -
 DFormer-B [27]           DFormer-Base               ICRL      2024     29.50   51.20     -      -   55.60    -      -
 DFormer-L [27]           DFormer-Large              ICRL      2024     39.00   52.50     -      -   57.20    -      -
 AsymFormer [52]          MiT-B0+ConvNeXt-Tin       CVPR       2024     33.00   49.10     -      -   55.30    -      -
 PolyMaX [53]             ConvNeXt-L                WACV       2024        -       -      -      -   58.10    -      -
 DFormerV2-S [26]         DFormerV2-Small           CVPR       2025     26.70   51.50     -      -   56.00    -      -
 DFormerV2-B [26]         DFormerV2-Base            CVPR       2025     53.90   52.80     -      -   57.70    -      -
 DFormerV2-L [26]         DFormerV2-Large           CVPR       2025     95.50   53.30     -      -   58.40    -      -
 EACNet [34]              ConvNeXt-T+VAN-B0         DDCLS      2025     37.00   52.60     -      -   57.60    -      -
 FCDENet [54]             MiT-B4                       IoT     2025    128.90   52.00   82.60    -   57.70  80.00    -
 DCANet [55]              VMamba                       PR      2025    123.80   49.60   82.60    -   53.30  78.20    -
 Sigma [56]               VMamba                    WACV       2025     69.80   52.40     -      -   57.00    -      -
 ADBNet [57]              ConvNeXt                    KBS      2025     45.90   49.60   82.30    -   56.00  79.40    -
 ECMRN [58]               DFormer                     KBS      2025     68.60   52.90     -      -   58.10    -      -
 DFNet-L [59]             MiT-B4                       TII     2025    108.75   51.73   83.42    -   57.33  79.88    -
 Sigma [56]               VMamba                    WACV       2025     69.80   52.40     -      -   57.00    -      -
 DiffPixelFormer-S (ours) MiT-B3                        -      2025    85.41    52.84   83.37  64.83 56.28  79.79  68.98
 DiffPixelFormer-M (ours) MiT-B5                        -      2025    157.24   53.69   83.47  66.11 58.71  80.30  69.93
 DiffPixelFormer-L (ours) Swin-Large                    -      2025    369.22   54.28   84.14  65.91 59.95  81.70  72.74

84.14%, and 65.91% on mIoU, Pixel ACC, and mAcc, respec-           to 59.95% mIoU, while achieving 81.70% Pixel Accuracy and
tively. Overall, DiffPixelFormer demonstrates clear advantages     72.74% mAcc, outperforming the strongest existing models
across parameter scales and baselines, striking a favorable bal-   and demonstrating clear advantages for high-precision appli-
ance between complexity and generalization, and thus offering      cations. Overall, DiffPixelFormer delivers stable and superior
substantial practical value and research significance.             performance across different parameter scales and backbone
   2) Results on NYUDv2: As shown in Table I, DiffPix-             choices, while maintaining flexibility to adapt to diverse ar-
elFormer demonstrates strong competitiveness across multiple       chitectures, thus exhibiting strong generalization ability and
configurations. The lightweight DiffPixelFormer-S achieves         practical utility in complex indoor scene understanding.
56.28% mIoU with a moderate parameter scale, outperforming
methods such as MultiMAE [47], CMX-B4 [35], DFormer-               D. Quantitative Results
S [27], DFormerV2-S [26], and AsymFormer [52], thereby es-            To further assess the effectiveness of the proposed cross-
tablishing a clear performance advantage. Furthermore, under       modal interaction mechanism, we perform a visual compar-
the same MiT-B5 backbone [37], DiffPixelFormer-M attains           ison on the SUN RGB-D [42] and NYUDv2 [32] datasets
58.71% mIoU, consistently surpassing TokenFusion-B5 [17],          against several representative attention mechanisms, includ-
CMX-B5 [35], and DPLNet [51], highlighting its strong com-         ing the Baseline, Cross-Attention [22], and Local Cross-
petitiveness under identical backbone settings. In the large-      Attention [23], as shown in Figs. 4 and 5. In the six rep-
scale setting, DiffPixelFormer-L further improves performance      resentative indoor scenes from SUN RGB-D and NYUDv2,
IEEE TRANSACTIONS ON MULTIMEDIA                                                                                                                   7

                                                                      NYUDv2
                Dining Room              Kitchen               Bathroom                 Bedroom            Living Room               Vanity

  Image

    GT

 Baseline

   CA

   LCA

   Ours

    background         floor        cabinet         sofa          table          door        window         picture         blinds       pillow

Fig. 4. Quantitative comparison of our DiffPixelFormer with the baseline and various cross-attention methods on NYUDv2, where GT denotes the ground
truth.

                                                                    SUNRGBD
                 Office              Bedroom               Living Room           Reading Room                Pantry                  Balcony

  Image

    GT

 Baseline

    CA

   LCA

  Ours

   background        floor         cabinet         sofa          table          door         window         picture         blinds       pillow

Fig. 5. Quantitative comparison of our DiffPixelFormer with the baseline and various cross-attention methods on SUNRGB-D.

the Baseline model exhibits blurred boundaries and frequent                regions such as tables, doors, and walls. These results clearly
mis-segmentation in complex environments. Cross-Attention                  demonstrate the superiority of the proposed mechanism in cap-
strengthens global dependencies between modalities but re-                 turing cross-modal complementary information and preserving
mains susceptible to background interference, while Local                  semantic structural integrity.
Cross-Attention refines local structural details yet lacks com-
prehensive global semantic modeling. In contrast, the proposed
DiffPixelFormer attains a well-balanced trade-off between                  E. Ablation Studies
global coherence and local precision, delivering more accurate               1) Effect of Overall Network Architecture: To systemati-
and semantically consistent segmentation, particularly in key              cally assess the contributions of the key components to intra-
IEEE TRANSACTIONS ON MULTIMEDIA                                                                                                                            8

                                                                   TABLE II
      E FFECT OF OVERALL N ETWORK A RCHITECTURE ON SUN RGB-D AND NYUDV 2, WHERE SA AND PACA DENOTE SELF - ATTENTION AND
PIXEL - AWARE CROSS - ATTENTION , RESPECTIVELY. T HE S IMILARITY D ISCRIMINATOR AND D IFFERENCE D ISCRIMINATOR ARE INTEGRAL COMPONENTS
                                                   OF DSIM. R ED INDICATES IMPROVEMENT.

                                                                                                 SUN RGB-D                             NYUDv2
 SA PACA Similarity Discriminator Difference Discriminator Learning Factor
                                                                                         mIoU         Pixel Acc mAcc mIoU               Pixel Acc mAcc
  ✓                                                                                      51.02          82.73    61.92    52.83          77.63     63.92
  ✓     ✓                                                                                51.49+0.47     82.86    63.48    53.57+0.74     78.18     65.31
  ✓     ✓                 ✓                                                              51.98+0.49     83.02    63.94    54.36+0.79     78.59     66.63
  ✓     ✓                 ✓                           ✓                                  52.62+0.64     83.31    64.56    56.09+1.73     79.46     68.79
  ✓     ✓                 ✓                           ✓                       ✓          52.84+0.22     83.37    64.83    56.28+0.19     79.79     68.98

                                                            TABLE III
E FFECT OF D IFFERENT ATTENTION M ECHANISMS ON SUN RGB-D AND NYUDV 2 DATASETS , WHERE SW C ROSS -ATTENTION DENOTES THE S HIFTED
                                              W INDOW C ROSS -ATTENTION MECHANISM .

                                                                          SUN RGB-D                                        NYUDv2
 Methods                           Backbone Param(M)
                                                       Input size FLOPs (G) mIoU Pixel Acc mAcc Input size FLOPs (G) mIoU Pixel Acc mAcc
 Baseline                          MiT-B3    44.65      530×730     135.58     51.02    82.73   61.92   480×640      100.75     52.83      77.63   63.92
 Cross-Attention [22]              MiT-B3    527.98     530×730     749.01     49.69    82.30   61.27   480×640      482.78     50.45      76.31   62.60
 SW Cross-Attention [25]           MiT-B3    88.09      530×730     213.19     49.13    81.95   61.06   480×640      165.37     48.51      74.97   61.98
 Local Cross-Attention [23]        MiT-B3    66.38      530×730     174.38     49.81    82.39   60.56   480×640      133.06     48.80      75.23   62.42
 Pixel-wise Cross-Attention [29]   MiT-B3    66.37      530×730     166.79     51.49    82.86   63.48   480×640      124.79     53.57      78.18   65.31
 DSIM (ours)                       MiT-B3     85.40     530×730     205.73     52.84    83.37   64.83   480×640      154.78     56.28      79.79   68.98

                                                                 TABLE IV
                                    E FFECT OF DIFFERENT BACKBONES ON SUN RGB-D AND NYUDV 2 DATASETS .

                                                          SUN RGB-D                                                  NYUDv2
Backbone            Parameters(M)
                                       Input size FLOPs(G) mIoU Pixel Acc mAcc Input size FLOPs(G) mIoU Pixel Acc mAcc
MiT-B1 [37]              25.28          530×730       131.67      47.03      80.93     59.20    480×640         100.08      32.60       66.10      44.01
MiT-B3 [37]              85.41          530×730       205.73      52.84      83.37     64.83    480×640         154.78      56.28       79.79      68.98
MiT-B5 [37]             157.24          530×730       758.40      53.69      83.47     66.11    480×640         569.20      58.71       80.30      69.93
Swin Tiny [25]           51.94          530×730       280.35      49.69      81.84     62.81    480×640         219.32      46.02       73.51      59.33
Swin Large [25]         369.22          530×730       1005.65     54.28      84.14     65.91    480×640         815.10      59.95       81.70      72.74

and inter-modal interactions, ablation studies are conducted on                                             TABLE V
the SUN RGB-D and NYUDv2 datasets (see Table II). The                             E FFECT OF D IFFERENT R ELATION D ISCRIMINATORS ON NYUDV 2
                                                                                                             DATASET.
results show that using only intra-modal self-attention yields
51.02% and 52.83% mIoU on SUN RGB-D and NYUDv2,                               Relation Discriminator            Backbone mIoU Pixel Acc mAcc
respectively. With the introduction of the cross-modal pixel-
                                                                              ECANet [60]                        MiT-b3     53.11        77.92     66.29
level attention module, the mIoU increases to 51.49% and                      SENet [61]                         MiT-b3     53.98        78.18     67.46
53.57%, indicating that explicit cross-modal interaction facili-              2*MLP+gMLP+Softmax [62]            MiT-b3     53.30        77.91     66.80
tates stronger feature association. Further adding the similarity             2*MLP+Sigmoid                      MiT-b3     54.58        78.30     67.42
discriminator brings the performance to 51.98% and 54.36%,                    2*MLP+Softmax                      MiT-b3     56.28        79.79     68.98
suggesting that aligning features across modalities is beneficial
for fusion. Incorporating the difference discriminator achieves
52.62% and 56.09%, highlighting the necessity of modeling                    attention [22], shifted window cross-attention [25], local cross-
modality-specific differences. Finally, with the learnable fac-              attention [23], and pixel-wise cross-attention [29] (see Ta-
tor mechanism, DiffPixelFormer attains 52.84% and 56.28%                     ble III). Standard cross-attention, despite 527.98M parame-
mIoU, corresponding to 1.82% and 3.45% gains over the                        ters, suffers from diluted pixel-level details and redundancy,
baseline with consistent improvements in Pixel Accuracy and                  achieving only 49.69% and 50.45% mIoU on SUN RGB-
mAcc. These results verify that the proposed modules provide                 D and NYUDv2. Shifted window and local variants reduce
complementary advantages and jointly enhance multi-modal                     computation but their limited receptive fields constrain pre-
semantic segmentation.                                                       cise pixel alignment. Pixel-wise cross-attention enhances fine-
                                                                             grained inter-modal fusion, improving mIoU to 51.49% and
   2) Effect of Different Attention Mechanisms: To validate                  53.57%. Building on this, DSIM explicitly models differen-
the proposed DSIM, we compare it with standard cross-                        tial features to capture cross-modal discrepancies, reaching
IEEE TRANSACTIONS ON MULTIMEDIA                                                                                                                9

52.84% and 56.28% mIoU with further gains in Pixel ACC and        leveraging the complementary strengths of RGB and depth
mAcc. Compared to conventional cross-attention mechanisms,        data. DSIM reduces parameter count and FLOPs by 83.83%
DSIM reduces parameter count and FLOPs by 83.83% and              and 72.53% compared to conventional cross-attention mecha-
72.53%, respectively. Overall, by effectively modeling cross-     nisms. Extensive experiments on NYUDv2 and SUN RGB-D
modal complementarity and distinctiveness, DiffPixelFormer        demonstrate that DiffPixelFormer outperforms state-of-the-art
achieves an optimal balance between accuracy and efficiency,      methods while maintaining real-time inference at 41.66 FPS.
while maintaining real-time inference at 41.66 FPS.               In future work, we will extend the proposed differential pixel-
   3) Effect of Different Backbone Architectures: To evaluate     aware mechanism to broader multimodal perception tasks
the influence of backbone networks on multimodal segmen-          and explore its generalization and application potential under
tation, we conducted extensive experiments on SUN RGB-D           modality-missing scenarios.
and NYUDv2, as shown in Table IV. Results show that per-
formance scales with model capacity and computational cost.                                     R EFERENCES
The lightweight MIT-B1 with 25.28M parameters achieves             [1] D. Seichter, M. Köhler, B. Lewandowski, T. Wengefeld, and H.-M.
only 47.03% and 32.60% mIoU, revealing limited ability to              Gross, “Efficient rgb-d semantic segmentation for indoor scene analysis,”
                                                                       in 2021 IEEE international conference on robotics and automation
capture complex multimodal semantics. Increasing capacity,             (ICRA), 2021, pp. 13 525–13 531.
MIT-B3 with 85.41M parameters boosts mIoU to 52.84%                [2] X. Zhang, Y. Gong, J. Lu, J. Wu, Z. Li, D. Jin, and J. Li, “Multi-
and 56.28%, while MIT-B5 further improves to 53.69% and                modal fusion technology based on vehicle information: A survey,” IEEE
                                                                       Transactions on Intelligent Vehicles, vol. 8, no. 6, pp. 3605–3619, 2023.
58.71% at higher cost. Swin Large, with 369.22M parameters         [3] X. Zhang, Z. Li, Y. Gong, D. Jin, J. Li, L. Wang, Y. Zhu, and H. Liu,
and hierarchical window-based self-attention, achieves 54.28%          “Openmpd: An open multimodal perception dataset for autonomous
and 59.95% mIoU and 84.14% and 81.70% pixel accuracy,                  driving,” IEEE Transactions on Vehicular Technology, vol. 71, no. 3,
                                                                       pp. 2437–2447, 2022.
underscoring the importance of multi-scale and long-range          [4] Y. Gong, N. Wang, J. Lu, X. Zhang, Y. Gao, J. Zhao, Z. Huang, H. Bai,
modeling in RGB-D segmentation. However, these gains incur             N. Zeng, N. Su et al., “Progressive bird’s eye view perception for safety-
substantial computational demands, underscoring trade-offs in          critical autonomous driving: A comprehensive survey,” arXiv preprint
                                                                       arXiv:2508.07560, 2025.
resource-limited scenarios. Overall, our method demonstrates       [5] Y. Gong, M. Chen, H. Liu, G. Yongsheng, L. Yang, N. Wang, Z. Song,
strong architectural compatibility, seamlessly integrating with        and H. Ma, “Stable at any speed: Speed-driven multi-object tracking with
diverse backbones to balance performance and efficiency.               learnable kalman filtering,” arXiv preprint arXiv:2508.00358, 2025.
                                                                   [6] W. Zhou, E. Yang, J. Lei, J. Wan, and L. Yu, “Pgdenet: Progressive
   4) Effect of Different Relation Discriminators: To assess           guided fusion and depth enhancement network for rgb-d indoor scene
the effectiveness of the proposed relation discriminator and           parsing,” IEEE Transactions on Multimedia, vol. 25, pp. 3483–3494,
                                                                       2022.
identify the optimal design for cross-modal feature integra-       [7] Y. Zheng, Y. Xu, S. Shu, and M. Sarem, “Indoor semantic segmentation
tion, we compare several representative approaches, including          based on swin-transformer,” Journal of Visual Communication and
ECANet [60], SENet [61], and various MLP variants, as                  Image Representation, vol. 98, p. 103991, 2024.
                                                                   [8] W. Zhou, Y. Cai, L. Zhang, W. Yan, and L. Yu, “Utlnet: Uncertainty-
shown in Table V. Channel attention methods such as ECANet             aware transformer localization network for rgb-depth mirror segmenta-
and SENet achieve 53.11% and 53.98% mIoU with the                      tion,” IEEE Transactions on Multimedia, vol. 26, pp. 4564–4574, 2024.
MiT-b3 backbone, effectively modeling channel dependencies         [9] Y. Gong, J. Lu, W. Liu, Z. Li, X. Jiang, X. Gao, and X. Wu, “Sifdrivenet:
                                                                       Speed and image fusion for driving behavior classification network,”
but lacking explicit pixel-level cross-modal discrimination.           IEEE Transactions on Computational Social Systems, vol. 11, no. 1, pp.
The 2MLP+gMLP+Softmax variant attains 53.30% mIoU, yet                 1244–1259, 2023.
global token mixing introduces redundancy that weakens fine-      [10] S. Cai, R. Wakaki, S. Nobuhara, and K. Nishino, “Rgb road scene
                                                                       material segmentation,” in Proceedings of the Asian Conference on
grained distinctions. Replacing gMLP with a Sigmoid-based              Computer Vision, 2022, pp. 3051–3067.
discriminator improves results to 54.58% mIoU, confirming         [11] J. W. Li, G. W. Yan, J. W. Jiang, Z. Cao, X. Zhang, and B. Song,
that independent pixel-wise discrimination better preserves            “Construction of a multiscale feature fusion model for indoor scene
                                                                       recognition and semantic segmentation,” Scientific Reports, vol. 15,
local differences. Our 2MLP+Softmax design delivers superior           no. 1, pp. 1–18, 2025.
performance, highlighting the critical role of explicit pixel-    [12] Y. Wang, Q. Chen, S. Chen, and J. Wu, “Multi-scale convolutional
level relation modeling and the effectiveness of the Softmax-          features network for semantic segmentation in indoor scenes,” IEEE
                                                                       Access, vol. 8, pp. 89 575–89 583, 2020.
based discriminator for fine-grained multimodal segmentation.     [13] W. Zhou, S. Lv, J. Lei, T. Luo, and L. Yu, “Rfnet: Reverse fusion net-
                                                                       work with attention mechanism for rgb-d indoor scene understanding,”
                                                                       IEEE Transactions on Emerging Topics in Computational Intelligence,
                      V. C ONCLUSION                                   vol. 7, no. 2, pp. 598–603, 2022.
                                                                  [14] Q. Zhao, Y. Wan, J. Xu, and L. Fang, “Cross-modal attention fusion
   In this paper, we propose DiffPixelFormer, a novel RGB-             network for rgb-d semantic segmentation,” Neurocomputing, vol. 548,
D fusion framework whose core Intra-Inter Modal Interaction            p. 126389, 2023.
Block (IIMIB) jointly enhances intra-modal representations        [15] M. Chen, Q. Li, W. Nie, J. Liu, J. Geng, Y. Ma, and X. Guan, “Dsdp:
                                                                       Real-time asymmetric dual-stream instance segmentation embedding
and models inter-modal interactions within a unified archi-            depth-predictive architecture for enhanced scene understanding,” IEEE
tecture. To explicitly distinguish modality-specific and shared        Transactions on Multimedia, 2025.
information, IIMIB incorporates the Differential–Shared Inter-    [16] W. Wang, D. Tran, and M. Feiszli, “What makes training multi-modal
                                                                       classification networks hard?” in Proceedings of the IEEE/CVF con-
Modal (DSIM) module, which leverages pixel-level attention             ference on computer vision and pattern recognition, 2020, pp. 12 695–
guided by differential and similarity cues to achieve fine-            12 705.
grained cross-modal alignment. In addition, a dynamic adap-       [17] Y. Wang, X. Chen, L. Cao, W. Huang, F. Sun, and Y. Wang, “Multimodal
                                                                       token fusion for vision transformers,” in Proceedings of the IEEE/CVF
tive fusion strategy is introduced to flexibly adjust modal-           conference on computer vision and pattern recognition, 2022, pp.
ity weights according to scene characteristics, thereby fully          12 186–12 195.
IEEE TRANSACTIONS ON MULTIMEDIA                                                                                                                               10

[18] W. Su, X. Zhu, Y. Cao, B. Li, L. Lu, F. Wei, and J. Dai, “Vl-bert:           [38] W. Zou, Y. Peng, Z. Zhang, S. Tian, and X. Li, “Rgb-d gate-guided
     Pre-training of generic visual-linguistic representations,” arXiv preprint        edge distillation for indoor semantic segmentation,” Multimedia Tools
     arXiv:1908.08530, 2019.                                                           and Applications, vol. 81, no. 25, pp. 35 815–35 830, 2022.
[19] W. Zhou, Y. Xiao, W. Yan, and L. Yu, “Cmpffnet: Cross-modal and              [39] Z. Hao, Z. Xiao, Y. Luo, J. Guo, J. Wang, L. Shen, and H. Hu, “Primkd:
     progressive feature fusion network for rgb-d indoor scene semantic seg-           Primary modality guided multimodal fusion for rgb-d semantic segmen-
     mentation,” IEEE Transactions on Automation Science and Engineering,              tation,” in Proceedings of the 32nd ACM International Conference on
     vol. 21, no. 4, pp. 5523–5533, 2024.                                              Multimedia, 2024, pp. 1943–1951.
[20] Y. Gong, X. Jiang, L. Wang, L. Xu, J. Lu, H. Liu, L. Lin, and X. Zhang,      [40] C. Yu, J. Wang, C. Peng, C. Gao, G. Yu, and N. Sang, “Bisenet:
     “Tclanenet: Task-conditioned lane detection network driven by vibration           Bilateral segmentation network for real-time semantic segmentation,” in
     information,” IEEE Transactions on Intelligent Vehicles, vol. 9, no. 9,           Proceedings of the European conference on computer vision (ECCV),
     pp. 5680–5693, 2024.                                                              2018, pp. 325–341.
[21] Y. Gong, X. Zhang, J. Lu, X. Jiang, Z. Wang, H. Liu, Z. Li, L. Wang,         [41] M. Yuan, K. Fu, Z. Li, Y. Meng, and M. Wang, “Pointmbf: A multi-
     Q. Yang, and X. Wu, “Steering angle-guided multimodal fusion lane                 scale bidirectional fusion network for unsupervised rgb-d point cloud
     detection for autonomous driving,” IEEE Transactions on Intelligent               registration,” in Proceedings of the IEEE/CVF International Conference
     Transportation Systems, vol. 26, no. 2, pp. 1470–1481, 2025.                      on Computer Vision, 2023, pp. 17 694–17 705.
[22] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,      [42] S. Song, S. P. Lichtenberg, and J. Xiao, “Sun rgb-d: A rgb-d scene
     Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in            understanding benchmark suite,” in Proceedings of the IEEE conference
     neural information processing systems, vol. 30, 2017.                             on computer vision and pattern recognition, 2015, pp. 567–576.
[23] X. Dong, J. Bao, D. Chen, W. Zhang, N. Yu, L. Yuan, D. Chen, and             [43] A. Janoch, S. Karayev, Y. Jia, J. T. Barron, M. Fritz, K. Saenko, and
     B. Guo, “Cswin transformer: A general vision transformer backbone                 T. Darrell, “A category-level 3-d object dataset: Putting the kinect to
     with cross-shaped windows,” in Proceedings of the IEEE/CVF confer-                work,” in 2011 IEEE International Conference on Computer Vision
     ence on computer vision and pattern recognition, 2022, pp. 12 114–                Workshops (ICCV Workshops). IEEE, 2011, pp. 1168–1174.
     12 124.                                                                      [44] L.-Z. Chen, Z. Lin, Z. Wang, Y.-L. Yang, and M.-M. Cheng, “Spatial
[24] Z. Leng, P. Sun, T. He, D. Anguelov, and M. Tan, “Pvtransformer: Point-           information guided convolution for real-time rgbd semantic segmenta-
     to-voxel transformer for scalable 3d object detection,” in 2024 IEEE              tion,” IEEE Transactions on Image Processing, vol. 30, pp. 2313–2324,
     International Conference on Robotics and Automation (ICRA). IEEE,                 2021.
     2024, pp. 4238–4244.                                                         [45] J. Cao, H. Leng, D. Lischinski, D. Cohen-Or, C. Tu, and Y. Li,
[25] Z. Liu, Y. Lin, Y. Cao, H. Hu, Y. Wei, Z. Zhang, S. Lin, and                      “Shapeconv: Shape-aware convolutional layer for indoor rgb-d semantic
     B. Guo, “Swin transformer: Hierarchical vision transformer using shifted          segmentation,” in Proceedings of the IEEE/CVF international conference
     windows,” in Proceedings of the IEEE/CVF international conference on              on computer vision, 2021, pp. 7088–7097.
     computer vision, 2021, pp. 10 012–10 022.                                    [46] F. Wang, J. Pan, S. Xu, and J. Tang, “Learning discriminative cross-
[26] B.-W. Yin, J.-L. Cao, M.-M. Cheng, and Q. Hou, “Dformerv2: Geometry               modality features for rgb-d saliency detection,” IEEE Transactions on
     self-attention for rgbd semantic segmentation,” in Proceedings of the             Image Processing, vol. 31, pp. 1285–1297, 2022.
     Computer Vision and Pattern Recognition Conference, 2025, pp. 19 345–        [47] R. Bachmann, D. Mizrahi, A. Atanov, and A. Zamir, “Multimae: Multi-
     19 355.                                                                           modal multi-task masked autoencoders,” in European Conference on
[27] B. Yin, X. Zhang, Z. Li, L. Liu, M.-M. Cheng, and Q. Hou, “Dformer:               Computer Vision. Springer, 2022, pp. 348–367.
     Rethinking rgbd representation learning for semantic segmentation,”          [48] R. Girdhar, M. Singh, N. Ravi, L. Van Der Maaten, A. Joulin, and
     arXiv preprint arXiv:2309.09668, 2023.                                            I. Misra, “Omnivore: A single model for many visual modalities,”
[28] S. Gupta, R. Girshick, P. Arbeláez, and J. Malik, “Learning rich features        in Proceedings of the IEEE/CVF conference on computer vision and
     from rgb-d images for object detection and segmentation,” in European             pattern recognition, 2022, pp. 16 102–16 112.
     conference on computer vision. Springer, 2014, pp. 345–360.                  [49] D. Seichter, S. B. Fischedick, M. Köhler, and H.-M. Groß, “Efficient
[29] D. Jia, J. Guo, K. Han, H. Wu, C. Zhang, C. Xu, and X. Chen, “Gemini-             multi-task rgb-d scene analysis for indoor environments,” in 2022
     fusion: efficient pixel-wise multimodal fusion for vision transformer,” in        International joint conference on neural networks (IJCNN). IEEE,
     Proceedings of the 41st International Conference on Machine Learning,             2022, pp. 1–10.
     2024, pp. 21 753–21 767.                                                     [50] J. Zhang, R. Liu, H. Shi, K. Yang, S. Reiß, K. Peng, H. Fu, K. Wang, and
[30] J. Long, E. Shelhamer, and T. Darrell, “Fully convolutional networks              R. Stiefelhagen, “Delivering arbitrary-modal semantic segmentation,”
     for semantic segmentation,” in Proceedings of the IEEE conference on              in Proceedings of the IEEE/CVF Conference on Computer Vision and
     computer vision and pattern recognition, 2015, pp. 3431–3440.                     Pattern Recognition, 2023, pp. 1136–1147.
[31] O. Ronneberger, P. Fischer, and T. Brox, “U-net: Convolutional networks      [51] S. Dong, Y. Feng, Q. Yang, Y. Huang, D. Liu, and H. Fan, “Efficient
     for biomedical image segmentation,” in International Conference on                multimodal semantic segmentation via dual-prompt learning,” in 2024
     Medical image computing and computer-assisted intervention. Springer,             IEEE/RSJ International Conference on Intelligent Robots and Systems
     2015, pp. 234–241.                                                                (IROS). IEEE, 2024, pp. 14 196–14 203.
[32] N. Silberman, D. Hoiem, P. Kohli, and R. Fergus, “Indoor segmentation        [52] S. Du, W. Wang, R. Guo, R. Wang, and S. Tang, “Asymformer:
     and support inference from rgbd images,” in European conference on                Asymmetrical cross-modal representation learning for mobile platform
     computer vision. Springer, 2012, pp. 746–760.                                     real-time rgb-d semantic segmentation,” in Proceedings of the IEEE/CVF
[33] X. Xu, H. Liu, J. Wu, and J. Liu, “Pddm: Pseudo depth diffusion model             Conference on Computer Vision and Pattern Recognition, 2024, pp.
     for rgb-pd semantic segmentation based in complex indoor scenes,” in              7608–7615.
     Proceedings of the AAAI Conference on Artificial Intelligence, vol. 39,      [53] X. Yang, L. Yuan, K. Wilber, A. Sharma, X. Gu, S. Qiao, S. Debats,
     no. 9, 2025, pp. 8969–8977.                                                       H. Wang, H. Adam, M. Sirotenko et al., “Polymax: General dense
[34] Y. Mao, Y. Chen, Z. Qian, and J. Zhang, “Eacnet: Efficient asymmetric             prediction with mask transformer,” in Proceedings of the IEEE/CVF
     cross-modal rgb-d semantic segmentation network for indoor robotic                Winter Conference on Applications of Computer Vision, 2024, pp. 1050–
     perception,” in 2025 IEEE 14th Data Driven Control and Learning                   1061.
     Systems (DDCLS). IEEE, 2025, pp. 1078–1083.                                  [54] W. Zhou, B. Jian, and Y. Liu, “Feature contrast difference and enhanced
[35] J. Zhang, H. Liu, K. Yang, X. Hu, R. Liu, and R. Stiefelhagen, “Cmx:              network for rgb-d indoor scene classification in internet of things,” IEEE
     Cross-modal fusion for rgb-x semantic segmentation with transformers,”            Internet of Things Journal, vol. 12, no. 11, pp. 17 610–17 621, 2025.
     IEEE Transactions on intelligent transportation systems, vol. 24, no. 12,    [55] L. Bai, J. Yang, C. Tian, Y. Sun, M. Mao, Y. Xu, and W. Xu,
     pp. 14 679–14 694, 2023.                                                          “Dcanet: Differential convolution attention network for rgb-d semantic
[36] X. Hu, K. Yang, L. Fei, and K. Wang, “Acnet: Attention based network              segmentation,” Pattern Recognition, vol. 162, p. 111379, 2025.
     to exploit complementary features for rgbd semantic segmentation,” in        [56] Z. Wan, P. Zhang, Y. Wang, S. Yong, S. Stepputtis, K. Sycara, and
     2019 IEEE international conference on image processing (ICIP). IEEE,              Y. Xie, “Sigma: Siamese mamba network for multi-modal semantic
     2019, pp. 1440–1444.                                                              segmentation,” in 2025 IEEE/CVF Winter Conference on Applications
[37] E. Xie, W. Wang, Z. Yu, A. Anandkumar, J. M. Alvarez, and P. Luo,                 of Computer Vision (WACV). IEEE, 2025, pp. 1734–1744.
     “Segformer: Simple and efficient design for semantic segmentation            [57] C. Xu, G. Ma, F. Gao, B. Wang, and J. Liu, “Adbnet: Asymmetric
     with transformers,” Advances in neural information processing systems,            dual-branch network for indoor real-time rgb-d semantic segmentation,”
     vol. 34, pp. 12 077–12 090, 2021.                                                 Knowledge-Based Systems, vol. 326, p. 113885, 2025.
IEEE TRANSACTIONS ON MULTIMEDIA                                                11

[58] D. Jia, C. Zhao, H. Song, H. Zhang, and W. Li, “Ecmrn: Efficient cross-
     modal reparameterization network for rgb-d tasks via prompt tuning,”
     Knowledge-Based Systems, p. 114321, 2025.
[59] Y. Yang, Y. Hong, Y. Yuan, H. Pan, and W. Sun, “Difference-aware
     fusion network for efficient rgb-d semantic segmentation in indoor
     robots,” IEEE Transactions on Industrial Informatics, vol. 21, no. 10,
     pp. 7424–7434, 2025.
[60] Q. Wang, B. Wu, P. Zhu, P. Li, W. Zuo, and Q. Hu, “Eca-net:
     Efficient channel attention for deep convolutional neural networks,”
     in Proceedings of the IEEE/CVF conference on computer vision and
     pattern recognition, 2020, pp. 11 534–11 542.
[61] J. Hu, L. Shen, and G. Sun, “Squeeze-and-excitation networks,” in
     Proceedings of the IEEE conference on computer vision and pattern
     recognition, 2018, pp. 7132–7141.
[62] H. Liu, Z. Dai, D. So, and Q. V. Le, “Pay attention to mlps,” Advances
     in neural information processing systems, vol. 34, pp. 9204–9215, 2021.
