---
source_id: 173
bibtex_key: jia2024geminifusion
title: GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer
year: 2024
domain_theme: Segmentasi RGB-D
verified_pdf: 173_GeminiFusion.pdf
char_count: 110259
---

^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

                                               Ding Jia * 1 Jianyuan Guo * 2 Kai Han 3 Han Wu 2 Chao Zhang 1 Chang XuB 2 Xinghao ChenB 3
                                              jiading@stu.pku.edu.cn; {jianyuan.guo,han.wu}@sydney.edu.au; kai.han@huawei.com; c.zhang@pku.edu.cn

                                                                Abstract                                    sources has emerged as a pivotal catalyst for advancing ar-
                                                                                                            tificial intelligence-driven perception in vision (Smith &
                                             Cross-modal transformers have demonstrated su-
arXiv:2406.01210v2 [cs.CV] 4 Jun 2024

                                                                                                            Gasser, 2005; Baltrušaitis et al., 2018; Guo et al., 2022a).
                                             periority in various vision tasks by effectively
                                                                                                            This approach has demonstrated remarkable potential, sur-
                                             integrating different modalities. This paper first
                                                                                                            passing the unimodal paradigm across various downstream
                                             critiques prior token exchange methods which re-
                                                                                                            tasks, including autonomous driving (Ha et al., 2017; Li
                                             place less informative tokens with inter-modal
                                                                                                            et al., 2022), semantic segmentation (Ye et al., 2019; Cao
                                             features, and demonstrate exchange based meth-
                                                                                                            et al., 2021), video captioning (Sun et al., 2019a; Lu et al.,
                                             ods underperform cross-attention mechanisms,
                                                                                                            2019) and visual question answering (Antol et al., 2015;
                                             while the computational demand of the latter in-
                                                                                                            Ben-Younes et al., 2017).
                                             evitably restricts its use with longer sequences.
                                             To surmount the computational challenges, we                   In the current literature, dominant paradigms for the multi-
                                             propose GeminiFusion, a pixel-wise fusion ap-                  modal fusion can be categorized into two ad-hoc schemes,
                                             proach that capitalizes on aligned cross-modal                 i.e., interaction-based fusion (Shvetsova et al., 2022; Na-
                                             representations. GeminiFusion elegantly com-                   grani et al., 2021; Zhang et al., 2023a) and exchange-based
                                             bines intra-modal and inter-modal attentions, dy-              fusion (Wang et al., 2020c; 2022b; Zhu et al., 2023). In early
                                             namically integrating complementary information                interaction-based methods, a common practice involved di-
                                             across modalities. We employ a layer-adaptive                  rectly concatenating tokens from different modalities (Su
                                             noise to adaptively control their interplay on a               et al., 2019). This straightforward fusion approach neglects
                                             per-layer basis, thereby achieving a harmonized                inter-modal interactions and sometimes leads to a poorer
                                             fusion process. Notably, GeminiFusion maintains                performance than single-modal counterparts (Wang et al.,
                                             linear complexity with respect to the number of                2020b; 2022b). While cross-attention mechanisms are in-
                                             input tokens, ensuring this multimodal framework               troduced as a solution, the quadratic complexity of the full
                                             operates with efficiency comparable to unimodal                attention with an increasing number of input tokens chal-
                                             networks. Comprehensive evaluations across mul-                lenges the feasibility of cross-modal models. To tackle this
                                             timodal image-to-image translation, 3D object                  issue, a simple strategy is to confine cross-modal interaction
                                             detection and arbitrary-modal semantic segmenta-               to later layers, often referred to as late-fusion (Nagrani et al.,
                                             tion tasks, including RGB, depth, LiDAR, event                 2021). However, this method restricts the ability of the
                                             data, etc. demonstrate the superior performance                network’s shallow layers to access valuable features from
                                             of our GeminiFusion against leading-edge tech-                 another modality, diminishing the original goal of facili-
                                             niques. The PyTorch code is available here.                    tating mutual assistance between modalities and hindering
                                                                                                            overall model performance.
                                                                                                            Exchange-based fusion provides a parameter-free solu-
                                        1. Introduction                                                     tion (Wang et al., 2022b; 2020c) to the computational
                                        In light of the increasing availability of low-cost sen-            overhead by leveraging the inherent alignment of differ-
                                        sors, multimodal fusion which leverages data from various           ent modalities in vision tasks. For instance, world-space
                                                                                                            data like LiDAR and point clouds can be projected to pixels
                                           *
                                             Equal contribution 1 Peking University. 2 The University       on the paired image plane. This method entails dynamically
                                        of Sydney. 3 Huawei Noah’s Ark Lab.. Correspondence                 predicting the significance of each input token and subse-
                                        to: Chang Xu <c.xu@sydney.edu.au>, Xinghao Chen <xing-
                                                                                                            quently replacing less crucial tokens from one modality with
                                        hao.chen@huawei.com>.
                                                                                                            those from another.
                                        Proceedings of the 41 st International Conference on Machine
                                                                                                            Our investigation into the prune-then-substitute technique,
                                        Learning, Vienna, Austria. PMLR 235, 2024. Copyright 2024 by
                                        the author(s).                                                      as outlined in the TokenFusion (Wang et al., 2022b), reveals

                                                                                                        1
                                      ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

60                                         54                                          62                                            68                                            69
                            TokenFusion                                 TokenFusion                                   TokenFusion                                   TokenFusion                                TokenFusion
                            GeminiFusion                                GeminiFusion   61                             GeminiFusion   67                             GeminiFusion   68                          GeminiFusion
58                                         53                    52.7                  60                                                                                          67                   66.9
                                                                                                                                     66
                     56.8                                                                                                                                    65.4
                                                      +1.3                             59                      58.5                                                                66
56                                         52                                                                                        65                                                      +3.4
          +2.6                                                                         58                                                         +1.9                             65
                                                         51.4                                       +2.8                             64
             54.2                                                                      57                                                            63.5                          64
54                                         51                                                                                                                                                   63.5
                                                                                                                                     63
                                                                                       56              55.7                                                                        63
                                                                                       55                                            62                                            62
52                                         50
                                                                                       54                                            61                                            61
50   NYUDv2 Semantic Segmentation          49   SUN RGBD Semantic Segmentation         53 DeLiVER Semantic Segmentation (RGB+E)      60 DeLiVER Semantic Segmentation (RGB+D+E) 60DeLiVER Semantic Segmentation (RGB+D+E+L)

Figure 1: Improvements of our ^GeminiFusion across five multimodal semantic segmentation tasks. GeminiFusion achieves +2.6%,
+1.3%, +2.8%, +1.9%, and +3.4% performance gains. All training epoch numbers are aligned. D: Depth, E: Event, L: LiDAR.

that its effectiveness is not as consistent as expected. We                                                    segmentation, i.e., RGB, depth, events, and LiDAR, cover-
observe that the network’s shallow layers deem all tokens                                                      ing four multimodal benchmarks.
insignificant and indiscriminately substitute them with rep-
                                                                                                               Our contributions in this paper include: (i) we empirically
resentations from an alternate modality. This behavior is in
                                                                                                               demonstrate that directly replacing features of one modality
stark contrast to that of the deeper layers, which align more
                                                                                                               with those from another modality is sub-optimal. Simply
closely with our initial expectations by selectively swapping
                                                                                                               exchanging all tokens every time achieves better results;
out representations of less pivotal tokens. Moreover, our
                                                                                                               (ii) we propose an efficient method named GeminiFusion
results suggest that a strategy of unconditionally exchang-
                                                                                                               for multimodal feature fusion, leveraging the inherent high
ing all tokens almost invariably yields the best outcomes, as
                                                                                                               alignment of different modal inputs in vision tasks while
evidenced by the data presented in Figure 3. Upon further
                                                                                                               preserving the original unimodal features; (iii) extensive
analysis, we believe that this phenomenon can be attributed
                                                                                                               experiments on multimodal image-to-image translation, 3D
to the intrinsic unique information carried by each token;
                                                                                                               object detection tasks and arbitrary-modal segmentation
any direct substitution results in an irrevocable loss of infor-
                                                                                                               consistently affirm the effectiveness of our proposed Gemi-
mation. We also note instances of simultaneous information
                                                                                                               niFusion.
exchange at identical positions across modalities, underscor-
ing the necessity for features from different modalities to be
mutually retained and integrated.                                                                              2. Related Work
We observe that the performance of the exchange-based                                                          The process of multimodal fusion involves leveraging di-
fusion consistently underperforms the cross-attention based                                                    verse data sources to enhance associated details, surpassing
fusion, while the additional overhead introduced by the full                                                   the capabilities of their unimodal counterparts. Here, we
attention poses a significant challenge. To overcome this                                                      delve into two prevailing fusion schemes and emphasizing
challenge and maintain the core information captured by the                                                    their applicability in targeted multimodal vision tasks.
original unimodal learning, we introduce a pixel-wise multi-
                                                                                                               Interaction-based multimodal fusion. Early studies of
modal fusion approach called GeminiFusion. Specifically,
                                                                                                               interaction-based fusion (Snoek et al., 2005; Atrey et al.,
given two modalities, only the two matched tokens from cor-
                                                                                                               2010; Bruni et al., 2014) categorizes the fusion strategy into
responding modalities will participate in the fusion process.
                                                                                                               three broad types: early (input-level), mid (feature-level)
This fusion scheme has a minimal impact on the original
                                                                                                               and late (decision-level) fusion. Early fusion methods (Zhao
unimodal representations, on account of the preservation of
                                                                                                               et al., 2020; Zhang et al., 2021a) directly fuse the inputs
skip connections from the original inputs and the retention
                                                                                                               from different modalities through a single-stream network,
of self-consistent part during the fusion process. Meanwhile,
                                                                                                               performed by averaging (Hazirbas et al., 2017) or concate-
the cross-modality part can significantly capture valuable
                                                                                                               nating (Zhang & Funkhouser, 2018) along the input chan-
multimodal information. The computational cost is minor
                                                                                                               nels. However, the supervision signal is distant from the
since the pixel-wise attention is more compact compared to
                                                                                                               blended input, resulting in suboptimal results. Addition-
the full attention. Moreover, GeminiFusion demonstrates its
                                                                                                               ally, maintaining supervision for individual modalities is
superiority by allowing multimodal architectures to lever-
                                                                                                               not feasible within this framework. Mid fusion (Lin et al.,
age parameters from unimodal pre-training, such as on the
                                                                                                               2017; Chen et al., 2019; Fu et al., 2020; Ramachandram &
ImageNet dataset.
                                                                                                               Taylor, 2017; De Vries et al., 2017) harnesses individual
To verify the advantage of the proposed method, we consider                                                    CNN or transformer encoders for each modality to capture
extensive tasks including multimodal image-to-image trans-                                                     intricacies in their respective features (Xu et al., 2023; Guo
lation, 3D object detection and arbitrary-modal semantic                                                       et al., 2022b). For example, MBT(Nagrani et al., 2021)

                                                                                                           2
                                       ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

                                                                GeminiFusion                            Query                                                   ×

                             PE
                                                                                                                                                        ×
                                                                                                         Key                                                ×

                                                                GeminiFusion

                             PE
                                                                                                                                                            ××
                                                                                                         Value
                                                                                         RGB Tokens
                                                                                                                                                                ×

                                         Multi-Head Attention
                                                                GeminiFusion
                             PE

                                                                                                                                                 (c) TokenFusion

                                                                                  FFN
                                                                                                                                      Query
                                                                GeminiFusion                            Query
                             PE

                                                                                                                                      Key
                                                                                                         Key

                                                                GeminiFusion
                             PE

                                                                                                         Value                        Value
                                                                                         Depth Tokens

                                                                GeminiFusion
                             PE

   Modality-1   Modality-2
                                  (a) Overall Architecture                                                       (b) GeminiFusion              (d) Cross-attention

Figure 2: (a) Overall architecture of GeminiFusion: our proposed GeminiFusion model is designed to be plug and play, allowing it to
be seamlessly integrated into various vision backbones. (b) GeminiFusion module:      performing pixel-wise fusion to enrich multimodal
                                                                                Relation Score                                          RGB
feature by utilizing aligned features from two modalities. (c) TokenFusion: swapping      certain pixels between  twoScore              Token in
                                                                                                                         features, but result
                                                                                 RGB                          Relation
information loss. (d) Cross-attention: requires a significant amount of memory resources
                                                                                Token        with quadratic complexity
                                                                                                               RGB     Depthof input token.
                                                                                                                                              Token   Token

subsequently amalgamated the encoded features through                                                   nisms, including self-/cross-attention (Vaswani et al., 2017),
a dedicated fusion layer. RDFNet (Park et al., 2017) and                                                CBAM (Woo et al., 2018), SENet (Hu et al., 2018), and
CMX (Zhang et al., 2023a) employ multilayer fusion, ag-                                                 ECA (Wang et al., 2020a) have demonstrated their success
gregating features iteratively with additional convolutional                                            in various tasks. Several multimodal frameworks (Li et al.,
blocks. EPIC-Fusion (Kazakos et al., 2019) combines inter-                                              2022; Hori et al., 2017; Wei et al., 2020) incorporate atten-
mediate activations via summation in the joint training of                                              tion modules to fuse features from different modalities. For
multiple modality-specific networks. TransFuser (Prakash                                                instance, ACNet (Hu et al., 2019) processes RGB and depth
et al., 2021) utilizes several transformer modules for the                                              with two branches and employs the proposed Attention Com-
fusion of intermediate features between different modalities.                                           plementary Module (ACM) to enable the fusion branch,
Late fusion (Owens & Efros, 2018) aggregates the final de-                                              exploiting more high-quality features from different chan-
cision through an ensemble of multiple outputs (Pandeya &                                               nels. Different from the ACNet, we concentrate more on the
Lee, 2021; Glodek et al., 2011), usually implemented using                                              aligned spatial location to explore an efficient fusion method.
parallel networks.                                                                                      VST (Liu et al., 2021a) utilizes cross-attention to fuse fea-
                                                                                                        tures from two modalities by computing the self-attention
Exchange-based multimodal fusion. CEN (Wang et al.,
                                                                                                        between the queries from one modality and the keys and
2020c) introduces the parameter-free Channel Exchanging
                                                                                                        values from the other modality. TransFuser (Prakash et al.,
Network, which dynamically exchanges channels between
                                                                                                        2021) and TriTransNet (Liu et al., 2021c) concatenate two
sub-networks of different modalities. MLF-VO(Jiang et al.,
                                                                                                        modal features and use self-attention to mix information.
2022) extends this method to fuse color and inferred depth
                                                                                                        Additionally, works like (Zhao et al., 2021; Wang et al.,
maps, incorporating a polarization regularizer to prevent the
                                                                                                        2022a) employ the SE module to blend information. In
model from reaching a singular solution. MuSE (Zhu et al.,
                                                                                                        contrast to previous quadratic complexity cross-attention,
2023) generalizes exchange-based methods from vision-
                                                                                                        our pixel-wise attention has linear complexity with respect
vision fusion to text-vision fusion. TokenFusion (Wang
                                                                                                        to the number of input tokens. This feature enables our
et al., 2022b), on the other hand, performs the exchange in
                                                                                                        fusion method to maintain a nearly as compact multimodal
the token dimension. It dynamically detects uninformative
                                                                                                        architecture as a unimodal network.
tokens and substitutes these tokens with features from other
modalities. In this paper, we contend that the prune-then-                                              Multimodal semantic segmentation. Many segmentation
substitute approach employed by TokenFusion consistently                                                methods excel in standard RGB-based benchmarks, provid-
falls short in performance compared to the cross-attention-                                             ing per-pixel category predictions in a given scene. However,
based interaction method. There is also a risk that all tokens                                          they often face challenges in real-world scenarios with rich
undergo unnecessary exchange, resulting in irreversible in-                                             3D geometric information. To overcome this limitation, re-
formation loss.                                                                                         searchers have sought to enhance scene understanding by
                                                                                                        incorporating multimodal sensing, including depth (Silber-
Attention for multimodal fusion.                                               Attention mecha-
                                                                                                        man et al., 2012; Gupta et al., 2014), thermal (Ha et al.,

                                                                                                   3
                        ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

2017; Sun et al., 2019b), polarimetric optical cues (Kalra             Table 1: Comparison with TokenFusion on the NYUDv2, SUN
et al., 2020), event-driven priors (Zhang et al., 2021b), and          RGB-D and DeLiVER datasets for multimodal semantic segmen-
                                                                       tation task. Evaluation metrics include pixel accuracy (%), mean
LiDAR (Zhuang et al., 2021a; Caesar et al., 2020). Previ-              accuracy (%), and mean IoU (%). Only mIoU is reported on
ous works have primarily focused on the RGB-depth set-                 the DeLiVER dataset following CMNeXt (Zhang et al., 2023b).
                                                                       †
ting, which may not generalize well across different sensing             marks the methods are reproduced by ourselves. All training
data (Zhang et al., 2023a). In this study, we explore a uni-           epochs are aligned. D: Depth, E: Event, L: LiDAR.
fied approach capable of generalizing effectively to diverse            Method          Backbone     Inputs Pixel Acc. mAcc.    mIoU
multimodal combinations for semantic segmentation.                      Results on the NYUDv2 dataset
                                                                        TokenFusion MiT-B3         RGB+D       79.0     66.9    54.2
                                                                        GeminiFusion MiT-B3        RGB+D     79.9+0.9 69.9+3.0 56.8+2.6
3. Our Method
                                                                        TokenFusion† MiT-B5        RGB+D       79.1     67.5    55.1
We first revist the recently proposed TokenFusion (Wang                 GeminiFusion MiT-B5        RGB+D     80.3+1.2 70.4+2.9 57.7+2.6
et al., 2022b) method in Section 3.1. Subsequently, Sec-                Results on the SUN RGB-D dataset
                                                                        TokenFusion† MiT-B3        RGB+D       82.8     63.6    51.4
tion 3.2 details the commonly utilized cross-attention mech-
                                                                        GeminiFusion MiT-B3        RGB+D     83.3+0.5 64.6+1.0 52.7+1.3
anism. Our pixel-wise GeminiFusion module is introduced
                                                                        TokenFusion† MiT-B5        RGB+D       83.1     63.9    51.8
in Section 3.3, and the comprehensive architecture is pre-              GeminiFusion MiT-B5        RGB+D     83.8+0.7 65.3+1.4 53.3+1.5
sented in Section 3.4.                                                  Results on the DeLiVER dataset
                                                                        TokenFusion† MiT-B2        RGB+D         -       -      63.7
3.1. Fusion via exchange                                                GeminiFusion MiT-B2        RGB+D         -       -     66.4+2.7
                                                                        TokenFusion† MiT-B2         RGB+E        -       -      55.7
Based on the motivation that there are always uninformative             GeminiFusion MiT-B2         RGB+E        -       -     58.5+2.8
tokens or channels in single-modal transformers, exchange               TokenFusion† MiT-B2         RGB+L        -       -      55.5
based methods such as TokenFusion (Wang et al., 2022b)                  GeminiFusion MiT-B2         RGB+L        -       -     58.6+3.1
and CEN (Wang et al., 2020c) are designed to dynamically                TokenFusion† MiT-B2 RGB+D+E+L            -       -      63.5
detect and substitute these useless tokens or channels with             GeminiFusion MiT-B2 RGB+D+E+L            -       -     66.9+3.4
features from other modalities. Specifically, at the core of
its functionality, TokenFusion (Wang et al., 2022b) prunes
tokens in each modality and replaces them with correspond-             in Figure 3c and Figure 3d, altering the threshold does not
ing tokens from other modalities that have been projected              prevent the tokens in the initial layers from being entirely
and aggregated to match. This exchange is guided by a                  exchanged. This suggests that TokenFusion does not operate
score predictor integrated within each block of the network,           as initially hoped, where tokens with negligible information
which computes masks that share the dimensions of the mul-             are replaced by those from other modalities. Furthermore, as
timodal inputs. These masks, through a comparison against              illustrated in Figure 3a and Figure 3b, setting the threshold
a predefined threshold, facilitate the selection of tokens to          to 1, thereby allowing all tokens always to be exchanged,
be substituted. Specifically, if there are only two modalities         yields better results. This indicates that the exchange-based
as input, i.e., X1 and X2 , the token exchange process can             method of TokenFusion is not only unstable but also prone
be formulated as:                                                      to the loss of critical information. Hence, it may be less
                                                                       effective than a strategy involving the complete exchange of
         X1[i] = X1[i] ⊙ Is(X1 )≥θ + X2[i] ⊙ Is(X1 )<θ ,
                            [i]                  [i]                   information.
                                                            (1)
         X2[i] = X2[i] ⊙ Is(X2 )≥θ + X1[i] ⊙ Is(X2 )<θ .
                            [i]                  [i]
                                                                       3.2. Fusion via cross-attention
where X1[i] indicates the i-th token of input X1 , I is an indi-       We commence with an exploration of a prevalent cross-
cator asserting the subscript condition, therefore it outputs a        attention-based fusion architecture (Li et al., 2022; Carion
mask tensor ∈ {0, 1}N , the parameter θ is a small threshold           et al., 2020), which is typified by the utilization of a canoni-
set to 0.02, and the operator ⊙ resents the element-wise               cal attention scheme to process inputs derived from multiple
multiplication.                                                        modalities. As illustrated in Figure 2d, consider the scenario
The supervision of the mask generation process is enforced             where we have procured a set of N patches from two modali-
through an L-1 norm constraint. However, this approach                 ties, denoted as X1 , X2 ∈ RN ×d , the corresponding output
introduces an element of stochasticity. The model does                 Y1 , Y2 ∈ RN ×d augmented by multimodal information
not inherently prioritize the informational importance of              can be generated by:
tokens when generating the masks. We contend that the
                                                                             Y1 = Attention(X1 WQ , X2 WK , X2 WV ) + X1
connection between the masks and the tokens’ intrinsic
information content is not well-regulated, which may lead                    Y2 = Attention(X2 WQ , X1 WK , X1 WV ) + X2             (2)
                                                                                                                √
to randomness in the exchange process. As demonstrated                       Attention(Q, K, V) = Softmax(QKT / d)V

                                                                   4
                                                 ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

         57                                                                                                                              1                                                                                  1
                                                                          52.5
         56                                                                                                                             0.8                                                                              0.8

         55                                                               52.0                                                          0.6                                                                              0.6
  mIoU

                                                                   mIoU
                                                                                                                                        0.4                                                                              0.4
         54                                                               51.5
                                                   TokenFusion                                                         TokenFusion      0.2                                                                              0.2
         53                                        GeminiFusion                                                        GeminiFusion
                                                                          51.0                                                           0                                                                                  0
              0.0        0.2      0.4     0.6      0.8       1.0                 0.0         0.2      0.4     0.6       0.8       1.0         1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728                             1 2 3 4 5 6 7 8 9 10111213141516171819202122232425262728
                    Threshold (NYUDV2 semantic segmentation)                           Threshold (SUN RGBD semantic segmentation)                        TokenFusion Exchange Rate (Threshold 0.02)                                             TokenFusion Exchange Rate (Threshold 0.2)

Figure 3: Impact of the threshold on the exchange-based TokenFusion. Exchanging all tokens almost invariably yields the best outcomes.

                                                                                                                                                  1                                                                                 1
                                                                                                                                                0.9                                                                                0.9
                                                                                                                                                0.8                                                                                0.8
                                                                                                                                                0.7                                                                                0.7
                                                                                                                                                0.6                                                                                0.6
                                                                                                                                                0.5                                                                                0.5
                                                                                                                                                0.4                                                                                0.4
                                                                                                                                                0.3                                                                                0.3
                                                                                                                                                0.2                                                                                0.2
                                                                                                                                                0.1                                                                                0.1
                                                                                                                                                  0                                                                                 0
                                                                                                                                                      1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28         1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
                                                                                                                                                                         Self Attn                     Cross Attn                                           Self Attn                     Cross Attn

                                                                                                                                               Figure 5: Comparison of attention scores obtained from self-
                                                                                                                                               attention (intra-modality) and cross-attention (inter-modality).
  (a) Input-0                  (b) Input-1 (c) TokenFusion                               (d) Ours                 (e) GT                       Left: with noise. Right: without noise.
Figure 4: Image-to-image translation results on the validation
split of Taskonomy. Best view in color and zoom in.
                                                                                                                                              Drawing inspiration from TokenFusion (Wang et al., 2022b),
                                                                                                                                              we posit that not all patches contribute equally to the fusion
Table 2:     Comparison on the Taskonomy dataset for the                                                                                      process. Less salient patches could be efficiently substituted
multimodal image-to-image translation task. Evaluation met-                                                                                   by their spatial counterparts from the alternate modality,
rics are FID/KID (×10−2 ) for the RGB predictions and MAE                                                                                     implying that exhaustive interaction among all patches may
(×10−1 )/MSE (×10−1 ) for other predictions. Lower values indi-
cate better performance for all the metrics. All training epoch                                                                               not be obligatory. This insight leads us to the hypothesis that
numbers are aligned.                                                                                                                          the crux of inter-modality information exchange lies in the
                           Shade+Texture             Depth+Normal                    RGB+Shade                  RGB+Edge
                                                                                                                                              patches sharing identical spatial coordinates, as these loca-
 Method
                              → RGB                     → RGB                         → Normal                   → Depth
 TokenFusion                47.31/0.94                103.87/4.24                     0.67/1.75                 0.22/0.55
                                                                                                                                              tions are where information exchange is most pertinent and
 GeminiFusion            41.32-5.99 /0.81-0.13     96.98-6.89 /3.71-0.53          0.65-0.02 /1.69-0.06       0.20-0.02 /0.49-0.06             significant. Leveraging this insight, the GeminiFusion mod-
                                                                                                                                              ule is engineered to prioritize interactions between spatially
Table 3: Comparison with MVX-Net on the 3D object detection
task against vehicle targets. The dataset is the validation set of the
                                                                                                                                              co-located patches from different modalities, thus refining
KITTI 3D object detection dataset. All training epoch numbers are                                                                             the cross-attention mechanism:
aligned. The IoU threshold is 0.7.                                                                                                                     1
                                                                                                                                                      Y[i] = Attention(X1[i] WQ , X2[i] WK , X2[i] WV ) + X1[i] ,
                                                                                                                                                       2
                                                                                                                                                                                                                                                                                                              (3)
              Method                  Param(M)
                                                      Easy
                                                                  3D APR11
                                                                   Medium           Hard          Easy
                                                                                                           3D APR40
                                                                                                            Medium         Hard                       Y[i] = Attention(X2[i] WQ , X1[i] WK , X1[i] WV ) + X2[i] .
      MVX-Net                            33.8        87.49          77.04          74.54         88.41       78.77        74.27
 MVX-Net + GeminiFusion                  34.8        88.49          77.36          74.61         89.43       78.76        74.46
                                                                                                                                              where i is in the range of d. The targeted interaction strategy
                                                                                                                                              of GeminiFusion module not only focuses computational
                                                                                                                                              effort on the most critical information exchanges but also
The computational complexity of above operation is O(N 2 ·                                                                                    significantly slashes the computational load. This efficiency
c), where N is the number of tokens of both modalities.                                                                                       is quantified by a reduction in computational complexity to
Given that N can be exceptionally large, the computational                                                                                    O(N · c2 ). Compared with the cross-attention, the FLOPs
demand of the model is significantly increased. For instance,                                                                                 plummet from 17G to merely 0.14G. This staggering reduc-
CMNeXt (Zhang et al., 2023b) partitions each modality in-                                                                                     tion of 99.2% in computational demand marks a transforma-
put into 16, 384 patches. This partitioning leads to a com-                                                                                   tive improvement, rendering the module exceedingly effi-
putational requirement of over 17G FLOPs for just one                                                                                         cient for deployment in environments where computational
instance of cross-attention, a figure that is prohibitive for                                                                                 resources are at a premium or where real-time performance
practical model deployment.                                                                                                                   is necessary.
                                                                                                                                              However, two main challenges arise here: (i) Incongruity
3.3. ^GeminiFusion: pixel-wise fusion module
                                                                                                                                              outcomes from the attention score. In the TokenFu-
To harness the benefits of modality fusion through cross-                                                                                     sion (Wang et al., 2022b) framework, the exchange of less
attention mechanism while circumventing the computational                                                                                     informative patches with those from a different modality
intensity that it entails, we introduce an innovative pixel-                                                                                  has been shown to enhance model performance. Conversely,
wise fusion module, termed the GeminiFusion module.                                                                                           within the attention module, a tendency arises where one

                                                                                                                                        5
                         ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

modality disproportionately learns from patches of another
                                                                                      58
modality that are more self-similar, as they yield higher at-                                                      b4 b5
tention scores. This proclivity is antithetical to our intended                       57                    b3                            b4
model behavior, which seeks to benefit from the integration                           56

                                                                           mIoU (%)
of dissimilar and potentially more informative patch char-                                                             b5
                                                                                      55
acteristics. (ii) Softmax function limitation in per-pixel                                          b2            b4              CMNext
                                                                                      54                     b3                   TokenFusion
attention mechanism. The current attention formulation                                                                            GeminiFusion (Ours)
operates on a per-pixel basis, resulting in an attention map                               0   50        100 150 200 250 300     2100 2150 2200 2250
of dimension 1 × 1. The application of the softmax function                                                       Latency (ms)
in this context is rendered ineffective as it invariably returns
a value of one, nullifying the intended differentiation of the            Figure 6: Performance vs.latency on the NYUDv2 dataset. Gemi-
                                                                          niFusion achieves the better trade-off compared with others. La-
attention mechanism. This outcome undermines the capac-                   tency is measured by averaging all validation samples of the
ity of the model to assign varying levels of attention across             NYUDv2 dataset. Multi-scale flip test strategy is used in CM-
modalities.                                                               Next as described in (Zhang et al., 2023b).

To address the aforementioned issues, we propose two en-
hancements. Firstly, we introduce a lightweight relation                  mathematically represented as follows:
discriminator to evaluate the disparity between modalities.                            1
                                                                                      Y[i] = Attention(Q1 , K1 , V1 ) + X1[i] ,
Our findings indicate that a synergistic combination of a
1 × 1 convolution followed by a softmax function suffices.                            Q1 = X1[i] W Q ,
The associated experiments are detailed in Table 6. Specif-                           K1 = [(NoiseK    1     K   1      1      2     K
                                                                                                  L + X[i] )W , X[i] ϕ(X[i] , X[i] )W ],
ically, patches from the two modalities are concatenated                               V1 = [(NoiseV    1     V   2    V
                                                                                                   L + X[i] )W , X[i] W ]
and fed into the relation discriminator, which subsequently                            2
                                                                                                                                                        (6)
                                                                                      Y[i] = Attention(Q2 , K2 , V2 ) + X2[i] ,
assigns a relation score ranging from 0 to 1. This relation
score is utilized to modulate the original key, effectively                           Q2 = X2[i] W Q ,
substituting the standard key in Eq. 2:                                               K2 = [(NoiseK    2     K   2      2      1     K
                                                                                                  L + X[i] )W , X[i] ϕ(X[i] , X[i] )W ],

                                                                                       V2 = [(NoiseV    2     V   1    V
                                                                                                   L + X[i] )W , X[i] W ].
   1
  Y[i] = Attention(Q, K, V) + X1[i]
                                                                (4)
  Q = X1[i] WQ , K = X1[i] ϕ(X1[i] , X2[i] )WK , V = X2[i] WV             We have conducted an ablation study on noise selection, de-
                                                                          tailed in Table 7. Our findings indicate that the optimal noise
                                                                          implementation involves a learnable parameter added to the
where ϕ(·) indicates our relation discriminator module. The               key, with this parameter being unique to each layer. This
                2
formula for Y[i]  is obtained in the same way. To prevent                 layer-specific noise facilitates a dynamic balance between
the second issues associated with single-item focus without               self-attention and cross-modal attention and ensures the ap-
adding redundant information, we add the pixel-wise self-                 propriate functioning of the softmax operation. Figure 5
attention into the Eq. 4:                                                 illustrates the variation in attention scores across increasing
                                                                          layer depths.
            K = [X1[i] WK , X1[i] ϕ(X1[i] , X2[i] )WK ],
                                                                (5)       3.4. Overall architecture
            V = [X1[i] WV , X2[i] WV ].
                                                                          Our GeminiFusion model adopts an encoder-decoder archi-
                 2                                                        tecture, with the encoder featuring a four-stage structure
The formula for Y[i] is obtained in the same way.      In the
                                                                          akin to the widely recognized SegFormer (Xie et al., 2021)
self-attention mechanism described by Equation 5, both
                                                                          for the extraction of hierarchical features. For conciseness,
the query and key are derived from identical modal inputs,
                                                                          Figure 2 illustrates only the initial stage out of the four.
leading to an inherent bias towards the self-referential com-
ponent of the attention score. This can diminish the efficacy             The primary focus lies in multimodal fusion based on visual
of learning cross-modal representations. To address this is-              data, encompassing modalities such as RGB, depth, event,
sue, we augment the self-attention with layer-adaptive noise.             and LiDAR. These modalities are inherently homogeneous,
This approach involves the injection of a minimal amount                  as they represent different visual perspectives of the same
of noise at the layer level, subtly enhancing the feature rep-            subject, and can be readily converted into image-like for-
resentation without burdening the model with extraneous                   mats (Zhuang et al., 2021b; Zhang et al., 2023b). Within our
information. To encapsulate this process for input tensors                framework, all modalities utilize shared parameters with the
X1 , X2 ∈ RN ×d at Layer L, the resultant output tensors                  exception of the Layer Normalization (LN) layers, facilitat-
Y1 , Y2 ∈ RN ×d within our GeminiFusion module can be                     ing a uniform processing approach. More specifically, the

                                                                      6
                              ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

Table 4: Comparison of multimodal semantic segmentation re-                   line network complexity but also enhance predictive general-
sults on NYUDv2 and SUN RGBD datasets with Swin (Liu et al.,                  ization capabilities. Moreover, the shared parameter strategy
2021b) and MiT-B3/B5 (Xie et al., 2021) as encoder models. All
training epochs are aligned. Swin-Tiny-1k and Swin-Large-22k are              aids in the detection of common patterns across different
pre-trained on the ImageNet-1K and ImageNet-22k, respectively.                modalities, which is a key objective of multimodal fusion. It
                                                                              should be noted that while our method excels in processing
                                                 NYUDv2     SUNRGBD           homogeneous modalities where each data type represents
  Method            Encoder           Param(M)
                                                  mIoU        mIoU
                    MiT-B3               75.8     56.8        52.7            a different perspective of the same input, it currently does
                    MiT-B5              137.2     57.7        53.3            not accommodate heterogeneous data combinations, such as
  GeminiFusion
                    Swin-Tiny-1k         52.0     52.2        50.2
                    Swin-Large-22k      369.2     60.2        54.6            images paired with audio or text. We also need to pre-define
                                                                              the method for aligning with the above data pairs. Address-
Table 5: Comparison results with state-of-the-art methods on the              ing this limitation remains an avenue for future research.
NYUDv2, SUN RGB-D and DeLiVER datasets for the multimodal
semantic segmentation task. Additional strategies indicate that the
method uses strategies other than ImageNet classification pre-                4. Experiment
training. For the DeLiVER dataset, we follow CMNeXt to use
MiT-B2 as backbone for fair comparison. Therefore “MiT-B5                     4.1. Datasets
(MiT-B2)” indicates that we use MiT-B5 for NUYDv2 and SUN
RGB-D, while MiT-B2 for DeLiVER. ∗ indicates that we use the
                                                                              For multimodal semantic segmentation experiments, we use
SUN RGBD trained model as pre-training on NYUDv2 dataset. †                   the following datasets: NYUDv2 (Silberman et al., 2012)
indicates that the results are reproduced by ourselves.                       dataset provides 795 training and 654 testing images, la-
                                     Additional NYUDv2 SUN RGBD DeLiVER       beled into 40 categories. The resolution we use is 480x640,
 Method          Backbone
                                     Strategies  mIoU    mIoU    mIoU         which is aligned with the setting in CMNeXt (Zhang et al.,
 PSD             ResNet50                ✗       51.0    50.6      -
 FSFNet          ResNet-101              ✗       52.0    50.6      -          2023b) and DFormer (Yin et al., 2023). DeLiVER (Zhang
 TokenFusion†    MiT-B5 (MiT-B2)         ✗       55.1    51.8     63.5
 SMMCL           SegNeXt-B               ✗       55.8      -       -          et al., 2023b) dataset contains 3983 training and 2005 test-
 MultiMAE        ViT-Base                ✓       56.0      -       -          ing images, which is more than four times the size of the
 OMNIVORE        Swin-Large              ✓       56.8      -       -
 CMNeXt          MiT-B4 (MiT-B2)         ✗       56.9    50.4     66.3        NYUDv2 dataset. It has 25 classes. The resolution we use
 CMX             MiT-B5                  ✗       56.9    52.4     62.7
 DFormer         DFormer-L               ✓       57.2    52.5      -          is 1024x1024, which is also aligned with CMNeXt. Accord-
 PolyMaX         ConvNeXt-L              ✓       58.1      -       -
 SwinMTL         SwinV2-Base-MiM         ✓       58.1      -       -
                                                                              ing to CMNext, only mIoU is reported. Thus, we also only
 EMSANet         EMSANet-R34-NBt1D       ✓       59.0    50.9      -          report mIoU in experiments on the DeLiVER dataset. SUN
 DPLNet          MiT-B5                  ✓       59.3    52.8      -
 OmniVec         OmniVec-4               ✓       60.8      -       -          RGB-D (Song et al., 2015) dataset contains 5285 training
 GeminiFusion    MiT-B5 (MiT-B2)         ✗       57.7    53.3     66.9
 GeminiFusion    Swin-Large-22k          ✗       60.2    54.6      -
                                                                              and 5050 testing images, which is about seven times the
 GeminiFusion∗   Swin-Large-22k          ✓       60.9      -       -          size of the NYUDv2 dataset and 1.7 times the size of the
                                                                              DeLiVER dataset. The input resolution is 480x480, which
                                                                              is aligned with DFormer. The class number of the SUN
RGB image I RGB ∈ R3×H×W , along with the other M −1                          RGB-D dataset is 37.
modalities I depth , · · · , I LiDAR ∈ R3×H×W , undergoes
sequential refinement through Multi-Head Self-Attention                       For the image-to-image translation task, we follow the ex-
(MHSA) and Feed-Forward Network (FFN) blocks. These                           periment settings used in CEN (Wang et al., 2020c) and
modalities are then adeptly integrated to harness intra-modal                 TokenFusion (Wang et al., 2022b). Taskonomy (Zamir
information via our proposed GeminiFusion module.                             et al., 2018) dataset is a large-scale indoor scene dataset,
                                                                              which contains about 4 million indoor images. More than
Upon completion of the four encoding stages, we obtain M                      10 modals are provided with each image, like depth, normal,
sets of feature maps at different stages, denoted as f m       l ∈            shade, texture and edge. Each modal is of size 512x512.
{f m
   1 , f m
         2 , f m
               3 , f m
                     4 } for each modality m    ∈    [0,  M    −  1].         We use the same sampling strategy with CEN and Token-
For the l-th encoding stage, the number of blocks per                         Fusion, which takes 1000 training and 500 testing images.
branch is specified by bl ∈ {4, 8, 16, 32}, the stride by                     Our implementation details can be found in the appendix A.
sl ∈ {4, 8, 16, 32}, and the channel dimension by Cl ∈
{64, 128, 320, 512}. Within each stage, the M feature maps                    For the 3D object detection task, we follow the experiment
are fused into a singular feature map f through a process                     settings used in MVX-Net (Sindagi et al., 2019). KITTI 3D
of weighted summation. Following the encoding process,                        object detection (Geiger et al., 2012) dataset contains 7481
the resultant four-stage features f l ∈ {f 1 , f 2 , f 3 , f 4 } are          training samples and 7518 test samples. The test difficulty is
channeled into the decoder. The decoder is responsible for                    categorized into three levels: easy, medium and hard, which
synthesizing the segmentation predictions. We employ an                       is based on the size of the object, the degree of visibility
MLP-based decoder, as outlined in SegFormer (Xie et al.,                      (occlusion), and the degree of truncation. In this paper, like
2021), to serve as our segmentation head.                                     MVX-Net (Sindagi et al., 2019), the training set is further
                                                                              split into a training set and a validation set. After splitting,
By employing a single-branch design, we not only stream-

                                                                          7
                           ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

Table 6: Ablation about the relation discriminator on the NYUDv2             Table 8: Multimodal semantic segmentation results on NYUDv2
dataset. All training epoch numbers are aligned. We use the MiT-             and SUN RGB-D datasets by adding our GeminiFusion only to
B3 as the backbone.                                                          last k layers. All models use the MiT-B3 backbone. All training
                                                                             epoch numbers are aligned. Latency is measured by averaging all
 Relation Discriminator                          Pixel Acc. mAcc. mIoU
 2layer-MLP                                         79.3     69.1 55.7
                                                                             validation samples in the NYUDv2 dataset.
 2layer-MLP + Sigmoid                               79.5     69.7 55.9
 2layer-MLP + Softmax                              79.9     69.9 56.8                                                        NYUDv2 SUN RGB-D
                                                                              Method         k Param(M) GFLOPs Latency(ms)
 1x1CNN + Softmax                                   79.2     69.2 55.7                                                        mIoU    mIoU
 3x3CNN + 1x1CNN + Softmax                          79.4     69.6 55.6        TokenFusion    28   45.9    108      126        54.2     51.4
 5x5CNN + 3x3CNN + 1x1CNN + Softmax                 79.1     68.7 54.9        GeminiFusion   28   75.8    174      153        56.8     52.7
 5x5CNN + 3x3CNN + 1x1CNN + 2layer-MLP + Softmax    79.2     68.9 55.3        GeminiFusion   22   75.1    165      144        56.5     52.5
                                                                              GeminiFusion   16   69.3    152      129        56.4     52.5
                                                                              GeminiFusion   10   62.5    138      116        56.4     52.2
Table 7: Ablation about the noise selection on the NYUDv2                     GeminiFusion    4   55.7    124      103        56.1     51.9
dataset. All training epoch numbers are aligned. We use the MiT-              GeminiFusion    1   48.8    119      102        55.1     51.9
B3 backbone.                                                                  GeminiFusion    0   45.9    108       95        53.3     51.2

 Noise type                      Pixel Acc. mAcc. mIoU
 Random Gaussian Noise, Multiply    79.2     69.3 55.5                       Table 9: Ablation about different parts of GeminiFusion on the
 Random Gaussian Noise, Add         79.2     68.8 55.3                       NYUDv2 dataset. PWC: point-wise cross-attention, NSA: noised
 Learnable parameter, Multiply      79.6     69.2 56.2                       self-attention, ARD: attention relation discriminator.
 Learnable parameter, Add          79.9     69.9 56.8
                                                                                              PWC        NSA     ARD         mIoU
                                                                                               ✗          ✗       ✗          53.3
                                                                                               ✓          ✗       ✗          55.4
the training set consists of 3712 samples and the validation                                   ✓          ✓       ✗          56.3
set consists of 3769 samples.                                                                  ✓          ✓       ✓          56.8

4.2. Comparisons with TokenFusion
                                                                             approach allows GeminiFusion to take advantage of differ-
Table 1 summarizes the comparative analysis between Gem-
                                                                             ent architectures to improve the model’s performance in
iniFusion and TokenFusion on segmentation tasks. Overall,
                                                                             multimodal tasks. In the previous experiments, we follow
with consistent training and testing conditions, GeminiFu-
                                                                             the TokenFusion codebase, which uses the SegFormer (Xie
sion outperforms TokenFusion across the board when it
                                                                             et al., 2021) as the encoder and a simple FFN as the de-
comes to the fusion of two to four modalities. Specifically,
                                                                             coder. However, in addition to SegFormer, models such
in scenarios where RGB is fused with Depth, GeminiFusion
                                                                             as Swin Transformer (Liu et al., 2021b) can also be used
achieves an improvement of approximately 1%-2.6% over
                                                                             as encoder models, which together with the decoder form
TokenFusion. When all four modalities are fused, Gemini-
                                                                             a complete segmentation model. We further conducts sev-
Fusion further extends its lead by a significant margin of
                                                                             eral experiments on the Swin Transformer. Specifically,
3.4% in mIoU, underscoring the efficacy of our attention-
                                                                             we inserts GeminiFusion into the SwinBlock. The official
based fusion approach that retains essential information
                                                                             checkpoints of Swin Transformer pre-trained on the Ima-
without loss.
                                                                             geNet classification task can also be loaded directly without
Table 2 presents the corresponding results for the image-                    degradation of accuracy, which demonstrates the advantages
to-image translation task. Our GeminiFusion outstrips To-                    of our approach. The experimental results are shown in Ta-
kenFusion across all evaluated settings. For instance, in the                ble 4. It can be seen that GeminiFusion is also applicable
Shade+Texture→RGB task, GeminiFusion attains FID/KID                         in frameworks such as Swin Transformer, and in the case
scores of 41.32/0.81, which is notably superior to Token-                    of using the Swin-Large-22k model, which was pre-trained
Fusion with a relative decrease of 12.6% in the FID metric.                  on a larger ImageNet-22k dataset and with a larger num-
Qualitative results, as illustrated in Figure 4, reveal that                 ber of parameters, as the baseline model, GeminiFusion
predictions using our GeminiFusion exhibit more natural                      also achieves optimal results among encoders, which re-
patterns and are smoother and clearer in terms of colors and                 flects the plug-and-play nature of GeminiFusion in different
details. This demonstrates GeminiFusion’s capability to pre-                 frameworks, as well as its ability to successfully leverage
serve a more complete spectrum of the shade information.                     the better representational capabilities provided by larger
                                                                             encoders.
4.3. Applying to Swin Transformer
                                                                             4.4. Comparisons with state-of-the-art methods
The proposed GeminiFusion module is a plug-and-play
module that can be inserted into existing multimodal ar-                     In this paper, GeminiFusion is benchmarked against state-
chitectures (predominantly into encoders) for enhancing the                  of-the-art multimodal segmentation methods on NYUDv2,
model’s cross-modal learning capabilities. This modular                      SUN RGB-D, and DeLiVER datasets, and the results are

                                                                         8
                        ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

detailed in Table 5. To ensure the fairness of the compari-            implementing GeminiFusion in only the final 10 layers still
son, all methods that use pre-training methods and training            yields faster inference speeds while preserving accuracy,
strategies other than pre-training on the ImageNet classi-             outperforming the benchmark method. Incorporating Gem-
fication tasks are labeled as “Additional Strategies”, such            iniFusion even in just the last layer alone surpasses To-
as PolyMax (Yang et al., 2024) (pre-training is performed              kenFusion in terms of both inference latency and accuracy.
using ImageNet-22K and Taskonomy), DPLNet (Dong                        However, it should be noted that the optimal results are
et al., 2023) (using pre-trained segmentation model), Om-              achieved when GeminiFusion is applied across every layer.
niVec (Srivastava & Sharma, 2024) (pre-trained based on
                                                                       Figure 6 graphically represents the trade-off between perfor-
self-supervision of large-scale masks), DFormer (Yin et al.,
                                                                       mance and latency. The comparison clearly demonstrates
2023) (utilizes an RGB-D pre-trained backbone), EM-
                                                                       that our GeminiFusion significantly outperforms TokenFu-
SANet (Seichter et al., 2023) and OMNIVORE (Girdhar
                                                                       sion in terms of efficiency by a considerable margin.
et al., 2022) (both of which utilize a strategy of multi dataset
pre-training coupled with fine-tuning of individual datasets).
In particular, we likewise attempts an additional pre-training         4.7. 3D Object Detection task
strategy, using a GeminiFusion model (Swin Large-22k                   We choose the MVX-Net (Sindagi et al., 2019) framework
backbone) trained on the SUN RGBD dataset and fine-tuned               and the KITTI dataset for our 3D object detection experi-
on the NYUDv2 dataset.                                                 ments for vehicles. The experiments use images and depth
As can be seen from the experimental results, GeminiFusion             maps as inputs for the detection of vehicle categories in the
using the Swin-Large-22k backbone network achieves the                 KITTI dataset, which is aligned with other works (Zhang
highest level of performance on both NYUDv2 and SUN                    et al., 2023c; Zheng et al., 2021). For the processing of
RGB-D datasets. Moreover, when fusing modalities such                  the KITTI dataset, we choose the same dataset division and
as RGB with Depth, Event and LiDAR data, GeminiFusion                  data processing methods as MVX-Net. GeminiFusion is
with the MiT-B2 backbone secures substantial gains over                inserted into the original fusion layer of MVX-Net, and the
CMNeXt, attesting to the efficacy of our pixel-wise fusion             experimental results are shown in Table 3, which show that
methodology in handling highly aligned modalities. Addi-               GeminiFusion achieves significant improvement in most
tionally, we juxtapose the performance of the MiT-B4-based             of the performance indexes with almost no increase in the
GeminiFusion with CMNeXt on the NYUDv2 dataset, as                     number of parameters, and a few performance indexes are
illustrated in Figure 6. Here, GeminiFusion not only attains           almost the same as the benchmark model.
marginally superior results but also boasts significantly re-
duced latency, even in the absence of multi-scale and flip             5. Conclusion
testing augmentations typically employed by CMNeXt.
                                                                       In this paper, we comprehensively examine exchange-based
                                                                       cross-modal transformers and point out their intrinsic de-
4.5. Effect of each component on GeminiFusion
                                                                       ficiency in achieving comparable performance of cross-
We present an ablation study on the NYUDv2 dataset to                  attention mechanisms. Furthermore, we propose a pixel-
assess the contribution of each component within our Gemi-             wise fusion approach named GeminiFusion, combining
niFusion framework. Table 9 shows our implementation of                intra-modality and inter-modality attention for dynamic
point-wise cross-attention yields a 2.1% increase in mIoU              integration of complementary information across modal-
compared to the baseline, demonstrating that direct infor-             ities. GeminiFusion achieves state-of-the-art performance
mation exchange between modalities can lead to substantial             across various multimodal semantic segmentation bench-
gains. Additionally, the effectiveness of the noise-adaptive           mark datasets, and also proved its effectiveness on image-
self-attention mechanism is evidenced by its ability to pre-           to-image translation and 3D object detection tasks. It is
serve intra-modal features, thereby preventing the loss of             worth noting that GeminiFusion operates with linear com-
valuable information. The proposed relation discriminator              plexity with respect to the number of input tokens, achieving
can help refine the generation process of key features within          efficiency comparable with unimodal counterparts.
the attention mechanism, ensuring more precise adjustments
that improve overall performance.                                      Acknowledgements
4.6. Discussion on Inference Latency                                   Ding Jia and Chao Zhang are supported by the National
                                                                       Nature Science Foundation of China under Grant 62071013
Contrary to the TokenFusion approach as documented                     and 61671027, and National Key R&D Program of China
in (Wang et al., 2022b), our GeminiFusion method does                  under Grant 2018AAA0100300. Chang Xu is supported
not require integration at every layer within the network              in part by the Australian Research Council under Projects
architecture. As evidenced by the experiments in Table 8,              DP240101848 and FT230100549.

                                                                   9
                          ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

Impact Statement                                                             Dong, S., Feng, Y., Yang, Q., Huang, Y., Liu, D., and Fan, H.
                                                                               Efficient multimodal semantic segmentation via dual-prompt
This paper contributes to the advancement of multimodal                        learning. arXiv preprint arXiv:2312.00360, 2023.
feature fusion in Machine Learning by comparing exchange-
                                                                             Fu, K., Fan, D.-P., Ji, G.-P., and Zhao, Q. Jl-dcf: Joint learning
based fusion with cross-attention based fusion. Our findings                   and densely-cooperative fusion framework for rgb-d salient
consistently demonstrate that cross-attention based fusion                     object detection. In Proceedings of the IEEE/CVF conference
outperforms exchange-based fusion by effectively preserv-                      on computer vision and pattern recognition, 2020.
ing core information among features from different modal-
                                                                             Geiger, A., Lenz, P., and Urtasun, R. Are we ready for autonomous
ities. Additionally, we propose an efficient GenimiFusion                      driving? the kitti vision benchmark suite. In Conference on
approach to reduce the computational overhead associated                       Computer Vision and Pattern Recognition (CVPR), 2012.
with cross-attention. There are many potential societal con-
                                                                             Girdhar, R., Singh, M., Ravi, N., van der Maaten, L., Joulin,
sequences of our work, none which we feel must be specifi-
                                                                               A., and Misra, I. Omnivore: A single model for many visual
cally highlighted here.                                                        modalities. In Proceedings of the IEEE/CVF Conference on
                                                                               Computer Vision and Pattern Recognition, pp. 16102–16112,
                                                                               2022.
References
Antol, S., Agrawal, A., Lu, J., Mitchell, M., Batra, D., Zitnick,            Glodek, M., Tschechne, S., Layher, G., Schels, M., Brosch, T.,
  C. L., and Parikh, D. Vqa: Visual question answering. In                     Scherer, S., Kächele, M., Schmidt, M., Neumann, H., Palm,
  Proceedings of the IEEE international conference on computer                 G., et al. Multiple classifier systems for the classification of
  vision, 2015.                                                                audio-visual emotional states. In Affective Computing and Intel-
                                                                               ligent Interaction: Fourth International Conference, ACII 2011,
Atrey, P. K., Hossain, M. A., El Saddik, A., and Kankanhalli,                  Memphis, TN, USA, October 9–12, 2011, Proceedings, Part II,
  M. S. Multimodal fusion for multimedia analysis: a survey.                   2011.
  Multimedia systems, 2010.
                                                                             Guo, J., Han, K., Wu, H., Tang, Y., Chen, X., Wang, Y., and Xu, C.
Baltrušaitis, T., Ahuja, C., and Morency, L.-P. Multimodal machine            Cmt: Convolutional neural networks meet vision transformers.
  learning: A survey and taxonomy. IEEE transactions on pattern                In Proceedings of the IEEE/CVF conference on computer vision
  analysis and machine intelligence, 2018.                                     and pattern recognition, 2022a.
Ben-Younes, H., Cadene, R., Cord, M., and Thome, N. Mutan:                   Guo, J., Tang, Y., Han, K., Chen, X., Wu, H., Xu, C., Xu, C., and
  Multimodal tucker fusion for visual question answering. In                   Wang, Y. Hire-mlp: Vision mlp via hierarchical rearrangement.
  Proceedings of the IEEE international conference on computer                 In Proceedings of the ieee/cvf conference on computer vision
  vision, 2017.                                                                and pattern recognition, 2022b.
Bruni, E., Tran, N.-K., and Baroni, M. Multimodal distributional             Gupta, S., Girshick, R., Arbeláez, P., and Malik, J. Learning
  semantics. Journal of artificial intelligence research, 2014.                rich features from rgb-d images for object detection and seg-
                                                                               mentation. In Computer Vision–ECCV 2014: 13th European
Caesar, H., Bankiti, V., Lang, A. H., Vora, S., Liong, V. E., Xu, Q.,
                                                                               Conference, Zurich, Switzerland, September 6-12, 2014, Pro-
  Krishnan, A., Pan, Y., Baldan, G., and Beijbom, O. nuscenes:
                                                                               ceedings, Part VII 13, 2014.
  A multimodal dataset for autonomous driving. In Proceedings
  of the IEEE/CVF conference on computer vision and pattern                  Ha, Q., Watanabe, K., Karasawa, T., Ushiku, Y., and Harada,
  recognition, 2020.                                                           T. Mfnet: Towards real-time semantic segmentation for
Cao, J., Leng, H., Lischinski, D., Cohen-Or, D., Tu, C., and Li,               autonomous vehicles with multi-spectral scenes. In 2017
  Y. Shapeconv: Shape-aware convolutional layer for indoor                     IEEE/RSJ International Conference on Intelligent Robots and
  rgb-d semantic segmentation. In Proceedings of the IEEE/CVF                  Systems (IROS), 2017.
  international conference on computer vision, 2021.                         Hazirbas, C., Ma, L., Domokos, C., and Cremers, D. Fusenet: In-
Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., and            corporating depth into semantic segmentation via fusion-based
  Zagoruyko, S. End-to-end object detection with transformers.                 cnn architecture. In Computer Vision–ACCV 2016: 13th Asian
  In European conference on computer vision, 2020.                             Conference on Computer Vision, Taipei, Taiwan, November
                                                                               20-24, 2016, Revised Selected Papers, Part I 13, 2017.
Chen, C., Rosa, S., Miao, Y., Lu, C. X., Wu, W., Markham, A.,
  and Trigoni, N. Selective sensor fusion for neural visual-inertial         Hori, C., Hori, T., Lee, T.-Y., Zhang, Z., Harsham, B., Hershey,
  odometry. In Proceedings of the IEEE/CVF Conference on                       J. R., Marks, T. K., and Sumi, K. Attention-based multimodal
  Computer Vision and Pattern Recognition, 2019.                               fusion for video description. In Proceedings of the IEEE inter-
                                                                               national conference on computer vision, 2017.
De Vries, H., Strub, F., Mary, J., Larochelle, H., Pietquin, O.,
  and Courville, A. C. Modulating early visual processing by                 Hu, J., Shen, L., and Sun, G. Squeeze-and-excitation networks.
  language. Advances in Neural Information Processing Systems,                 In Proceedings of the IEEE conference on computer vision and
  2017.                                                                        pattern recognition, 2018.
Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., and Fei-Fei, L.           Hu, X., Yang, K., Fei, L., and Wang, K. Acnet: Attention based
  Imagenet: A large-scale hierarchical image database. In 2009                 network to exploit complementary features for rgbd semantic
  IEEE conference on computer vision and pattern recognition,                  segmentation. In 2019 IEEE International conference on image
  pp. 248–255. Ieee, 2009.                                                     processing (ICIP), pp. 1440–1444. IEEE, 2019.

                                                                        10
                          ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

Jiang, Z., Taira, H., Miyashita, N., and Okutomi, M. Self-                   Seichter, D., Stephan, B., Fischedick, S. B., Müller, S., Rabes,
   supervised ego-motion estimation based on multi-layer fusion                L., and Gross, H.-M. Panopticndt: Efficient and robust panop-
   of rgb and inferred depth. In 2022 International Conference on              tic mapping. In 2023 IEEE/RSJ International Conference on
   Robotics and Automation (ICRA), 2022.                                       Intelligent Robots and Systems (IROS), pp. 7233–7240. IEEE,
                                                                               2023.
Kalra, A., Taamazyan, V., Rao, S. K., Venkataraman, K., Raskar,
  R., and Kadambi, A. Deep polarization cues for transparent ob-             Shvetsova, N., Chen, B., Rouditchenko, A., Thomas, S., Kings-
  ject segmentation. In Proceedings of the IEEE/CVF Conference                 bury, B., Feris, R. S., Harwath, D., Glass, J., and Kuehne, H.
  on Computer Vision and Pattern Recognition, 2020.                            Everything at once-multi-modal fusion transformer for video
                                                                               retrieval. In Proceedings of the ieee/cvf conference on computer
Kazakos, E., Nagrani, A., Zisserman, A., and Damen, D. Epic-                   vision and pattern recognition, 2022.
  fusion: Audio-visual temporal binding for egocentric action
  recognition. In Proceedings of the IEEE/CVF International                  Silberman, N., Hoiem, D., Kohli, P., and Fergus, R. Indoor segmen-
  Conference on Computer Vision, 2019.                                          tation and support inference from rgbd images. In Computer
                                                                                Vision–ECCV 2012: 12th European Conference on Computer
Li, Z., Wang, W., Li, H., Xie, E., Sima, C., Lu, T., Qiao, Y., and
                                                                                Vision, Florence, Italy, October 7-13, 2012, Proceedings, Part
   Dai, J. Bevformer: Learning bird’s-eye-view representation
                                                                                V 12, 2012.
   from multi-camera images via spatiotemporal transformers. In
   European conference on computer vision, 2022.                             Sindagi, V. A., Zhou, Y., and Tuzel, O. Mvx-net: Multimodal
Lin, D., Chen, G., Cohen-Or, D., Heng, P.-A., and Huang, H.                    voxelnet for 3d object detection. In 2019 International Con-
  Cascaded feature network for semantic segmentation of rgb-d                   ference on Robotics and Automation (ICRA), pp. 7276–7282.
  images. In Proceedings of the IEEE international conference                   IEEE, 2019.
  on computer vision, 2017.
                                                                             Smith, L. and Gasser, M. The development of embodied cognition:
Liu, N., Zhang, N., Wan, K., Shao, L., and Han, J. Visual saliency             Six lessons from babies. Artificial life, 2005.
  transformer. In Proceedings of the IEEE/CVF international
  conference on computer vision, 2021a.                                      Snoek, C. G., Worring, M., and Smeulders, A. W. Early versus late
                                                                               fusion in semantic video analysis. In Proceedings of the 13th
Liu, Z., Lin, Y., Cao, Y., Hu, H., Wei, Y., Zhang, Z., Lin, S., and            annual ACM international conference on Multimedia, 2005.
  Guo, B. Swin transformer: Hierarchical vision transformer
  using shifted windows. In Proceedings of the IEEE/CVF inter-               Song, S., Lichtenberg, S. P., and Xiao, J. Sun rgb-d: A rgb-d
  national conference on computer vision, 2021b.                               scene understanding benchmark suite. In Proceedings of the
                                                                               IEEE conference on computer vision and pattern recognition,
Liu, Z., Wang, Y., Tu, Z., Xiao, Y., and Tang, B. Tritransnet:                 pp. 567–576, 2015.
  Rgb-d salient object detection with a triplet transformer embed-
  ding network. In Proceedings of the 29th ACM international                 Srivastava, S. and Sharma, G. Omnivec: Learning robust rep-
  conference on multimedia, 2021c.                                              resentations with cross modal sharing. In Proceedings of the
                                                                                IEEE/CVF Winter Conference on Applications of Computer
Lu, J., Batra, D., Parikh, D., and Lee, S. Vilbert: Pretraining task-           Vision, pp. 1236–1248, 2024.
  agnostic visiolinguistic representations for vision-and-language
  tasks. Advances in neural information processing systems, 2019.            Su, W., Zhu, X., Cao, Y., Li, B., Lu, L., Wei, F., and Dai, J. Vl-bert:
                                                                               Pre-training of generic visual-linguistic representations. arXiv
Nagrani, A., Yang, S., Arnab, A., Jansen, A., Schmid, C., and Sun,             preprint arXiv:1908.08530, 2019.
  C. Attention bottlenecks for multimodal fusion. Advances in
  Neural Information Processing Systems, 2021.                               Sun, C., Myers, A., Vondrick, C., Murphy, K., and Schmid, C.
                                                                               Videobert: A joint model for video and language representa-
Owens, A. and Efros, A. A. Audio-visual scene analysis with                    tion learning. In Proceedings of the IEEE/CVF international
  self-supervised multisensory features. In Proceedings of the                 conference on computer vision, 2019a.
 European conference on computer vision (ECCV), 2018.
Pandeya, Y. R. and Lee, J. Deep learning-based late fusion of                Sun, Y., Zuo, W., and Liu, M. Rtfnet: Rgb-thermal fusion network
  multimodal information for emotion classification of music                   for semantic segmentation of urban scenes. IEEE Robotics and
  video. Multimedia Tools and Applications, 2021.                              Automation Letters, 2019b.

Park, S.-J., Hong, K.-S., and Lee, S. Rdfnet: Rgb-d multi-level              Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L.,
  residual feature fusion for indoor semantic segmentation. In                 Gomez, A. N., Kaiser, Ł., and Polosukhin, I. Attention is all
  Proceedings of the IEEE international conference on computer                 you need. Advances in neural information processing systems,
  vision, 2017.                                                                2017.

Prakash, A., Chitta, K., and Geiger, A. Multi-modal fusion trans-            Wang, F., Pan, J., Xu, S., and Tang, J. Learning discriminative
  former for end-to-end autonomous driving. In Proceedings of                  cross-modality features for rgb-d saliency detection. IEEE
  the IEEE/CVF Conference on Computer Vision and Pattern                      Transactions on Image Processing, 2022a.
  Recognition, 2021.
                                                                             Wang, Q., Wu, B., Zhu, P., Li, P., Zuo, W., and Hu, Q. Eca-
Ramachandram, D. and Taylor, G. W. Deep multimodal learning:                   net: Efficient channel attention for deep convolutional neural
  A survey on recent advances and trends. IEEE signal processing               networks. In Proceedings of the IEEE/CVF conference on
  magazine, 2017.                                                              computer vision and pattern recognition, 2020a.

                                                                        11
                          ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

Wang, W., Tran, D., and Feiszli, M. What makes training multi-                Zhang, J., Liu, R., Shi, H., Yang, K., Reiß, S., Peng, K., Fu, H.,
  modal classification networks hard? In Proceedings of the                     Wang, K., and Stiefelhagen, R. Delivering arbitrary-modal
 IEEE/CVF conference on computer vision and pattern recogni-                    semantic segmentation. In Proceedings of the IEEE/CVF Con-
  tion, 2020b.                                                                  ference on Computer Vision and Pattern Recognition, 2023b.

Wang, Y., Huang, W., Sun, F., Xu, T., Rong, Y., and Huang, J.                 Zhang, Y. and Funkhouser, T. Deep depth completion of a sin-
  Deep multimodal fusion by channel exchanging. Advances in                     gle rgb-d image. In Proceedings of the IEEE conference on
  neural information processing systems, 2020c.                                 computer vision and pattern recognition, 2018.

Wang, Y., Chen, X., Cao, L., Huang, W., Sun, F., and Wang, Y.                 Zhang, Y., Zhang, Q., Zhu, Z., Hou, J., and Yuan, Y. Glenet:
  Multimodal token fusion for vision transformers. In Proceed-                  Boosting 3d object detectors with generative label uncertainty
  ings of the IEEE/CVF Conference on Computer Vision and                        estimation. International Journal of Computer Vision, 131(12):
 Pattern Recognition, 2022b.                                                    3332–3352, 2023c.

Wei, X., Zhang, T., Li, Y., Zhang, Y., and Wu, F. Multi-modality              Zhao, X., Zhang, L., Pang, Y., Lu, H., and Zhang, L. A single
  cross attention network for image and sentence matching. In                   stream network for robust and real-time rgb-d salient object
 Proceedings of the IEEE/CVF conference on computer vision                      detection. In Computer Vision–ECCV 2020: 16th European
  and pattern recognition, 2020.                                                Conference, Glasgow, UK, August 23–28, 2020, Proceedings,
                                                                                Part XXII 16, 2020.
Woo, S., Park, J., Lee, J.-Y., and Kweon, I. S. Cbam: Convolu-
                                                                              Zhao, Y., Zhao, J., Li, J., and Chen, X. Rgb-d salient object
 tional block attention module. In Proceedings of the European
                                                                                detection with ubiquitous target awareness. IEEE Transactions
 conference on computer vision (ECCV), 2018.
                                                                                on Image Processing, 2021.
Xie, E., Wang, W., Yu, Z., Anandkumar, A., Alvarez, J. M., and                Zheng, W., Tang, W., Jiang, L., and Fu, C.-W. Se-ssd: Self-
  Luo, P. Segformer: Simple and efficient design for semantic seg-              ensembling single-stage object detector from point cloud. In
  mentation with transformers. Advances in Neural Information                   Proceedings of the IEEE/CVF conference on computer vision
  Processing Systems, 2021.                                                     and pattern recognition, pp. 14494–14503, 2021.
Xu, Y., Li, C., Li, D., Sheng, X., Jiang, F., Tian, L., and Sir-              Zhu, R., Han, C., Qian, Y., Sun, Q., Li, X., Gao, M., Cao, X., and
  asao, A. Fdvit: Improve the hierarchical architecture of vision               Xian, Y. Exchanging-based multimodal fusion with transformer.
  transformer. In Proceedings of the IEEE/CVF International                     arXiv preprint arXiv:2309.02190, 2023.
  Conference on Computer Vision, 2023.
                                                                              Zhuang, Z., Li, R., Jia, K., Wang, Q., Li, Y., and Tan, M.
Yang, X., Yuan, L., Wilber, K., Sharma, A., Gu, X., Qiao, S.,                   Perception-aware multi-sensor fusion for 3d lidar semantic seg-
  Debats, S., Wang, H., Adam, H., Sirotenko, M., et al. Polymax:                mentation. In Proceedings of the IEEE/CVF International Con-
  General dense prediction with mask transformer. In Proceed-                   ference on Computer Vision, 2021a.
  ings of the IEEE/CVF Winter Conference on Applications of
  Computer Vision, pp. 1050–1061, 2024.                                       Zhuang, Z., Li, R., Jia, K., Wang, Q., Li, Y., and Tan, M.
                                                                                Perception-aware multi-sensor fusion for 3D LiDAR seman-
Ye, L., Rochan, M., Liu, Z., and Wang, Y. Cross-modal self-                     tic segmentation. In In Proceedings of the IEEE international
  attention network for referring image segmentation. In Pro-                   conference on computer vision, 2021b.
  ceedings of the IEEE/CVF conference on computer vision and
  pattern recognition, 2019.

Yin, B., Zhang, X., Li, Z., Liu, L., Cheng, M.-M., and Hou, Q.
  Dformer: Rethinking rgbd representation learning for semantic
  segmentation. arXiv preprint arXiv:2309.09668, 2023.

Zamir, A. R., Sax, A., Shen, W., Guibas, L. J., Malik, J., and
  Savarese, S. Taskonomy: Disentangling task transfer learning.
  In Proceedings of the IEEE conference on computer vision and
  pattern recognition, pp. 3712–3722, 2018.

Zhang, J., Fan, D.-P., Dai, Y., Anwar, S., Saleh, F., Aliakbarian, S.,
  and Barnes, N. Uncertainty inspired rgb-d saliency detection.
  IEEE transactions on pattern analysis and machine intelligence,
  2021a.

Zhang, J., Yang, K., and Stiefelhagen, R. Exploring event-driven
  dynamic context for accident scene segmentation. IEEE Trans-
  actions on Intelligent Transportation Systems, 2021b.

Zhang, J., Liu, H., Yang, K., Hu, X., Liu, R., and Stiefelhagen, R.
  Cmx: Cross-modal fusion for rgb-x semantic segmentation with
  transformers. IEEE Transactions on Intelligent Transportation
  Systems, 2023a.

                                                                         12
                      ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

A. Implementation Details
  • In the context of multimodal semantic segmentation, our training hyper-parameters are developed by following
    the methodologies from the TokenFusion (Wang et al., 2022b) and CMNeXt (Zhang et al., 2023b) codebases. For
    model training, we employ NVIDIA V100 GPUs in configurations of 3, 4, and 8 units for the NYUDv2, SUN RGB-D,
    and DeLiVER datasets, respectively, adhering to the same environmental settings as specified in the original papers.
    Our encoder design is an adaptation from SegFormer (Xie et al., 2021), which has been pre-trained solely on the
    ImageNet-1K (Deng et al., 2009) dataset for classification tasks. For experiments on the NYUDv2 and SUN RGB-D
    datasets, we utilize the setup from the TokenFusion, maintaining consistency in batch size, optimizer, learning rate, and
    learning rate scheduler. Within our proposed GeminiFusion model, we configure the number of attention heads to 8. To
    mitigate the risk of overfitting, we set the drop path rate to 0.4, while the drop rate remains at 0.0. Conversely, for the
    DeLiVER dataset, our foundation training hyper-parameters are the same with CMNeXt, which necessitates a smaller
    backbone. Consequently, we reduce the drop path rate to 0.2. All other parameters, including batch size, optimizer,
    weight decay, and learning rate scheduler, remain in line with CMNeXt’s original configuration, except for the learning
    rate, which is modified to 2e−4 .

  • For the image-to-image translation task, we also follow the setting in TokenFusion and set the same hyper-parameters
    as the TokenFusion. We use one NVIDIA V100 card for all image-to-image translation experiments.
  • For the 3D object detection task, we also follow the setting in MVX-Net and set the same hyper-parameters as the
    MVX-Net. We use 4 NVIDIA V100 cards for all experiments.

B. More Visualization Results
                (a) Input-0         (b) Input-1      (c) TokenFusion           (d) Ours           (e) GT

  Figure 7: Shade+Texture→RGB. Image-to-image translation results on the validation split of Taskonomy (Zamir et al., 2018).

                                                             13
          ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

   (a) Input-0         (b) Input-1      (c) TokenFusion           (d) Ours          (e) GT

 Figure 8: RGB+Edge→Depth. Image-to-image translation results on the validation split of Taskonomy.

   (a) Input-0         (b) Input-1      (c) TokenFusion           (d) Ours          (e) GT

Figure 9: Depth+Normal→RGB. Image-to-image translation results on the validation split of Taskonomy.

                                                14
          ^GeminiFusion: Efficient Pixel-wise Multimodal Fusion for Vision Transformer

    (a) Input-0         (b) Input-1      (c) TokenFusion          (d) Ours          (e) GT

Figure 10: RGB+Shade→Normal. Image-to-image translation results on the validation split of Taskonomy.

                                                 15
