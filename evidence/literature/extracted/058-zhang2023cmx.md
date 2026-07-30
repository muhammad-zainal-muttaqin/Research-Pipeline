---
source_id: 058
bibtex_key: zhang2023cmx
title: CMX: Cross-Modal Fusion for RGB-X Semantic Segmentation with Transformers
year: 2023
domain_theme: Segmentasi RGB-D
verified_pdf: 58_CMX.pdf
char_count: 168187
---

1

                                             CMX: Cross-Modal Fusion for RGB-X Semantic
                                                   Segmentation with Transformers
                                                    Jiaming Zhang∗ , Huayao Liu∗ , Kailun Yang∗† , Xinxin Hu, Ruiping Liu, and Rainer Stiefelhagen

                                            Abstract—Scene understanding based on image segmentation is
                                         a crucial component of autonomous vehicles. Pixel-wise semantic
                                         segmentation of RGB images can be advanced by exploiting
arXiv:2203.04838v5 [cs.CV] 24 Nov 2023

                                         complementary features from the supplementary modality (X-
                                         modality). However, covering a wide variety of sensors with a
                                         modality-agnostic model remains an unresolved problem due to                  RGB + Depth   RGB + Thermal RGB + Polarization RGB + Event   RGB + LiDAR

                                         variations in sensor characteristics among different modalities.
                                         Unlike previous modality-specific methods, in this work, we
                                         propose a unified fusion framework, CMX, for RGB-X semantic                                           Feature                Feature
                                         segmentation. To generalize well across different modalities, that
                                         often include supplements as well as uncertainties, a unified cross-
                                         modal interaction is crucial for modality fusion. Specifically, we                                            CM-FRM
                                         design a Cross-Modal Feature Rectification Module (CM-FRM)
                                         to calibrate bi-modal features by leveraging the features from                                                  FFM
                                         one modality to rectify the features of the other modality. With
                                         rectified feature pairs, we deploy a Feature Fusion Module (FFM)                                     Semantic Segmentation
                                         to perform sufficient exchange of long-range contexts before
                                         mixing. To verify CMX, for the first time, we unify five modalities
                                         complementary to RGB, i.e., depth, thermal, polarization, event,
                                         and LiDAR. Extensive experiments show that CMX generalizes
                                         well to diverse multi-modal fusion, achieving state-of-the-art
                                         performances on five RGB-Depth benchmarks, as well as RGB-
                                         Thermal, RGB-Polarization, and RGB-LiDAR datasets. Besides,
                                         to investigate the generalizability to dense-sparse data fusion,
                                         we establish an RGB-Event semantic segmentation benchmark                  Fig. 1: RGB-X semantic segmentation unifies diverse sensing
                                         based on the EventScape dataset, on which CMX sets the new                 modality combinations: RGB-Depth, -Thermal, -Polarization,
                                         state-of-the-art. The source code of CMX is publicly available at          -Event, and -LiDAR segmentation. CMX is established with
                                         https://github.com/huaaaliu/RGBX_Semantic_Segmentation.
                                                                                                                    Cross-Modal Feature Rectification Module (CM-FRM) to cali-
                                          Index Terms—Semantic Segmentation, Scene Parsing, Cross-                  brate the features of RGB- and X-modality and Feature Fusion
                                         Modal Fusion, Vision Transformers, Scene Understanding.                    Module (FFM) to perform the exchange of long-range context
                                                                                                                    and combine features for RGB-X semantic segmentation.
                                                                 I. I NTRODUCTION
                                             CENE understanding is a fundamental component in Au-
                                         S   tonomous Vehicles (AVs) since it can provide comprehen-
                                         sive information to support the Advanced Driver-Assistance
                                                                                                                    computer vision – is an ideal perception solution to transform
                                                                                                                    an image input into its underlying semantically meaningful
                                                                                                                    regions, providing pixel-wise dense scene understanding for
                                         System (ADAS) to make correct decisions when interacting                   Intelligent Transportation Systems (ITS) [3], [4]. Image se-
                                         with the driving surrounding [1]. As exteroceptive sensors,                mantic segmentation has made significant progress on accu-
                                         cameras are adopted in AVs for perceiving the surround-                    racy [5], [6], [7]. Yet, current models may struggle to extract
                                         ings [2]. Image semantic segmentation – a fundamental task in              high-quality features in certain circumstances, e.g., when two
                                                                                                                    objects have similar colors or textures, leading to difficulty in
                                           This work was supported in part by the Federal Ministry of Labor and
                                         Social Affairs (BMAS) through the AccessibleMaps project under Grant       distinguishing them through pure RGB images [8].
                                         01KM151112, in part by the “KIT Future Fields” project, in part by the        Thanks to the development of sensor technologies, there
                                         MWK through the Cooperative Graduate School Accessibility through AI-      is a growing variety of modular sensors which are highly
                                         based Assistive Technology (KATE) under Grant BW6-03, and in part by the
                                         BMBF through a fellowship within the IFI program of the German Academic    applicable for ITS applications. Different types of sensors can
                                         Exchange Service (DAAD), in part by the HoreKA@KIT supercomputer           supply RGB images with rich complementary information (see
                                         partition, and in part by Hangzhou SurImage Technology Company Ltd.        Fig. 1). For example, depth measurement can help identify the
                                           J. Zhang, R. Liu, and R. Stiefelhagen are with Karlsruhe Institute of
                                         Technology, 76131 Karlsruhe, Germany.                                      boundaries of objects and offer geometric information of dense
                                           K. Yang is with Hunan University, Changsha 410082, China.                scene elements [8], [9]. Thermal images facilitate to discern
                                           H. Liu is with NIO, Shanghai 201804, China.                              different objects through their specific infrared imaging [10],
                                           X. Hu is with ByteDance Inc., Hangzhou 310000, China.
                                           ∗ indicates equal contribution.                                          [11]. Besides, polarimetric- and event information are advan-
                                           † corresponding author. (E-Mail: kailun.yang@hnu.edu.cn.)                tageous for perception in specular- and dynamic real-world
                                                                                                                                                                                                    2

                                                                     95%

                                                                     85%

                                                                     75%

                                                                     65%

                                                                     55%

                                                                     45%

                                                                     35%

                                                                                                                            EAFNet
                                                                           ACNet

                                                                                                   ACNet
                                                                                             CMX

                                                                                                                     CMX

                                                                                                                                              CMX

                                                                                                                                                                        CMX

                                                                                                                                                                              HRFuser

                                                                                                                                                                                              CMX
                                                                                                                                     NLFNet

                                                                                                                                                                                        PMF
                                                                                                                                                     ISSAFE
                                                                                   SA-Gate

                                                                                                           SA-Gate

                                                                                                                                                              SA-Gate
   (a) Input fusion   (b) Feature fusion   (c) Interactive fusion
                                                                      (a) RGB-D               (b) RGB-T                    (c) RGB-P                (d) RGB-E                 (e) RGB-L
Fig. 2: Comparison of different fusion methods. (a) Input
fusion merges inputs with modality-specific operations [15],         Fig. 3: Performance comparison on different RGB-X semantic
[16]. (b) Feature fusion applies channel attention to fuse           segmentation benchmarks. SA-Gate [9] designed for RGB-D
features in a unidirectional manner [8], [9]. (c) Our interactive    data (e.g., on NYU Depth V2 dataset [24]), is less effective
fusion incorporates bidirectional cross-modal feature recti-         on RGB-T or RGB-E tasks. Our modality-agnostic CMX, for
fication, and sequence-to-sequence cross-attention, yielding         the first time, outperforms modality-specific methods on five
comprehensive cross-modal interactions.                              segmentation tasks.

scenes [12], [13]. LiDAR data can provide spatial information        sensing data combinations [11]. We hypothesize that for
in driving scenarios [14]. Thereby, a research question arises:      RGB-X semantic segmentation with various supplements and
How to construct a unified model to incorporate the fusion of        uncertainties, comprehensive cross-modal interactions should
RGB with various modalities, i.e., RGB-X semantic segmenta-          be provided, to fully exploit the potential of cross-modal
tion as illustrated in Fig. 1?                                       complementary features.
   Existing multi-modal semantic segmentation methods can               To tackle the aforementioned challenges, we propose CMX,
be divided into two categories: (1) The first category [15],         a universal cross-modal fusion framework for RGB-X seman-
[16] employs a single network to extract features from RGB           tic segmentation in an interactive fusion manner (Fig. 2c).
and another modality, which are fused in the input stage (see        Specifically, CMX is built as a two-stream architecture, i.e.,
Fig. 2a). (2) The second type of approaches [9], [11], [17]          RGB- and X-modal stream. Two specific modules are designed
deploys two backbones to perform feature extraction from             for feature interaction and feature fusion in between. (1) Cross-
RGB- and another modality separately then fuses the extracted        Modal Feature Rectification Module (CM-FRM), calibrates the
two features into one feature for semantic prediction (see           bi-modal features by leveraging their spatial- and channel-wise
Fig. 2b). However, both types are usually well-tailored for a        correlations, which enables both streams to focus more on the
single specific modality pair (e.g., RGB-D or RGB-T), yet hard       complementary informative cues from each other, as well as
to be extended to operate with other modality combinations.          mitigates the effects of uncertainties and noisy measurements
For example, regarding our observation in Fig. 3, ACNet [8]          from different modalities. Such a feature rectification tackles
and SA-Gate [9], designed for RGB-D data, perform less               varying noises and uncertainties in diverse modalities. It
satisfactorily in RGB-T tasks. To flexibly cover various sensor      enables better multi-modal feature extraction and interaction.
combinations for ITS applications, a unified RGB-X semantic          (2) Feature Fusion Module (FFM), is constructed in two stages
segmentation, is desirable and advantageous. Its benefits are        and it performs sufficient information exchange before merg-
two-fold: (1) It can save research and engineering efforts,          ing features. Motivated by the large receptive fields obtained
with no need to adapt architectures for a specific modality          via self-attention [20], a cross-attention mechanism is devised
combination scenario. (2) It makes it possible that a system         in the first stage of FFM for realizing cross-modal global
equipped with multi-modal sensors can readily leverage new           reasoning. In its second stage, mixed channel embedding is
sensors when they become available [18], [19], which is              applied to produce enhanced output features. Thereby, our
conducive to robust scene perception. For this purpose, in           introduced comprehensive interactions lie in multiple levels
this work, we spend efforts to construct a modality-agnostic         (see Fig. 2c). It includes channel- and spatial-wise rectification
framework for unified RGB-X semantic segmentation.                   from the feature map perspective, as well as cross-attention
   Recently, vision transformers [20], [21], [22], [23] han-         from the sequence-to-sequence perspective, which are critical
dle inputs as sequences and are able to acquire long-range           for generalization across modality combinations.
correlations, offering the possibility for a unified framework          To verify our unification proposal, we consider and assess
for diverse multi-modal tasks. Compared to existing multi-           CMX on 5 different multi-modal semantic segmentation tasks,
modal fusion modules [8], [12], [17] based on Convolutional          including RGB-Depth, -Thermal, -Polarization, -Event, and
Neural Networks (CNNs), it remains unclear whether poten-            -LiDAR semantic segmentation. A total of 9 datasets are
tial improvements on RGB-X semantic segmentation can be              involved. In particular, CMX attains top mIoU of 56.9% on
materialized via vision transformers. Crucially, while some          NYU Depth V2 (RGB-D) [24], 59.7% on MFNet (RGB-
previous works [8], [9] use a simple global multi-modal              T) [10], 92.6% on ZJU-RGB-P (RGB-P) [12], and 64.3%
interaction strategy, it does not generalize well across different   on KITTI-360 (RGB-L) [25] datasets. Our universal approach
                                                                                                                                   3

CMX clearly outperforms specialized architectures (Fig. 3).        B. Multi-modal Semantic Segmentation
Furthermore, to address the lack of RGB-Event parsing
benchmark in the community, we establish an RGB-Event                 While previous works reach high performance on standard
semantic segmentation benchmark based on the EventScape            RGB-based semantic segmentation benchmarks, in challeng-
dataset [26], where our CMX sets the new state-of-the-art          ing real-world conditions, it is desirable to involve multi-
among >10 benchmarked models. Besides, our experiments             modality sensing for a reliable and comprehensive scene
demonstrate that the CMX framework is effective for both           understanding. RGB-Depth [38], [39] and RGB-Thermal [40],
CNN- and Transformer-based architectures. Moreover, our            [41], [42] semantic segmentation are broadly investigated. Po-
investigation on representations of polarization- and event-       larimetric optical cues [43] and event-driven priors [44] are of-
based data indicates the path to follow and the sweet spot for     ten intertwined for robust perception under adverse conditions.
reaching robust multi-modal semantic segmentation, trumping        In automated driving, LiDAR data [14] is incorporated for
original representation methods [12], [26].                        enhanced semantic road scene understanding. However, most
   At a glance, we deliver the following contributions:            of these works only address a single modality combination. In
   • For the first time, we explore RGB-X semantic segmen-         this work, we explore a unified approach, which can generalize
     tation in five types of multi-modal sensing data com-         well to diverse multi-modal combinations.
     binations, including RGB-Depth, RGB-Thermal, RGB-                For multi-modal semantic segmentation, there are two dom-
     Polarization, RGB-Event, and RGB-LiDAR.                       inant strategies. The first mainstream paradigm models cross-
   • We rethink multi-modality fusion from a generalization        modal complementary information into layer- or operator de-
     perspective and prove that comprehensive cross-modal          signs [15], [16], [45], [46], [47]. While these works verify that
     interaction is crucial for the unification of fusion across   multi-modal features can be learned within a shared network,
     diverse modalities.                                           they are carefully designed for a single modality, e.g., RGB-D
   • We propose an RGB-X semantic segmentation framework           semantic segmentation, which is hard to be applied to other
     CMX with cross-modal feature rectification and feature        modalities. Moreover, there are multi-task frameworks [48],
     fusion modules, intertwining cross-attention and mixed        [49] that facilitate inter-task feature propagation for RGB-D
     channel embedding for enhanced global reasoning.              scene understanding, but they rely on supervision from other
   • We investigate different representations of polarimetric-     tasks for joint learning. The second paradigm dedicates to
     and event data and indicate the optimal path to follow for    developing fusion schemes to bridge two parallel modality
     reaching robust multi-modal semantic segmentation.            streams. ACNet [8] proposes attention modules to exploit in-
   • An RGB-Event semantic segmentation benchmark is               formative features for RGB-D semantic segmentation, whereas
     established to assess dense-sparse data fusion, and is        ABMDRNet [11] suggests reducing the modality differences
     incorporated into the RGB-X semantic segmentation.            of features before selectively extracting discriminative cues for
                                                                   RGB-T fusion. For RGB-P segmentation, Xiang et al. [12]
                     II. R ELATED W ORK                            connect RGB- and polarization branches via channel attention
A. Transformer-driven Semantic Segmentation                        bridges. For RGB-E parsing, Zhang et al. [13] explore sparse-
   For dense semantic segmentation, pyramid-, strip-, and          to-dense and dense-to-sparse fusion flows to extract dynamic
atrous spatial pyramid pooling are designed to harvest multi-      context for accident scene segmentation. Salient object detec-
scale feature representations [5], [6]. Besides, cross-image       tion, seen as a specific type of image segmentation, can also
pixel contrast learning [27] is applied to address intra-class     benefit from multimodal fusion to identify the most important
compactness and inter-class dispersion, while nonparametric        objects, such as Hyperfusion-Net [50] tailored for RGB-D and
nearest prototype retrieving [28] is proposed to achieve se-       CAVER [51] for RGB-D and RGB-T. In this research, we also
mantic segmentation in a prototype view. Inspired by the non-      advocate this paradigm but unlike previous works, we address
local block [29], self-attention in transformers [20] has been     RGB-X semantic segmentation with a unified framework, for
used to establish long-range dependencies by DANet [7] and         generalizing to diverse sensing modality combinations.
CCNet [30]. Recently, SETR [31] and Segmenter [32] directly           While previous works use a simple global channel-wise
adopt vision transformers [21], [22] as the backbone, which        strategy, it does not work well across different sensing data.
captures global context from very early layers. SegFormer [33]     For example, ACNet [8] and SA-Gate [9], designed for RGB-
and Swin [23] create hierarchical structures to make use of        D segmentation, perform less satisfactorily in RGB-T scene
multi-resolution features. Following this trend, various archi-    parsing [11]. In contrast, we hypothesize that comprehensive
tectures of dense prediction transformers [34], [35] and seman-    cross-modal interactions are crucial for RGB-X semantic seg-
tic segmentation transformers [36], [37] emerge in the field.      mentation with various supplements and uncertainties, so as
While these approaches have achieved high performance, most        to fully unleash the potential of cross-modal complementary
of them focus on using RGB images and suffer when RGB              features. Besides, most of the previous works adopt CNN
images cannot provide sufficient information in real-world         backbone without considering that long-range dependency. We
scenes, e.g., under low-illumination conditions or in high-        put forward a framework with transformers, which has global
dynamic areas. In this work, we tackle multi-modal semantic        dependencies already in its architecture design. Differing
segmentation to take advantage of complementary information        from existing works, we perform fusion on different levels
from other modalities such as depth, thermal, polarization,        with cross-modal feature rectification and cross-attentional
event, and LiDAR data for boosting RGB segmentation.               exchanging for enhanced dense semantic prediction.
                                                                                                                                                                                                                                                                                                                4

                                    Layer 1                                       Layer 2                                                   Layer 3                                    Layer 4
                                                                                                                                                                                                                                                Low-level
                                                                                                                                                                                                                                                 features

  RGB                                                  CM-                                                    CM-                                              CM-                                                     CM-
                                                                          FFM                                                           FFM                                       FFM                                                               FFM            Decoder
                                                       FRM                                                    FRM                                              FRM                                                     FRM

                                    Layer 1                                       Layer 2                                                   Layer 3                                    Layer 4                                                                                   Semantic Segmentation

  Modal X

                                                                                                                                            a) Overall Framework

                                                                                                                                                                                                                                                                                        RGB Branch
                                                                                                                                                                                                                                                 +
                                                                                                                                                                                                                                                      Next RGB                            X Branch
                            A
                                                                                            X                                                                                                                      X           +                        layer
   FRGB
                            M                                                                                                                                                                                                                                                             CM-FRM
                                           C                                                                                            C
                                                           MLP                                                                                                      MLP along                                                                                                               FFM
                            A                                                                                                                                      channel axis
    FX
                                                                                            X                                                                                                                      X           +
                                                             2       1        1    C                                                                                                                                                                      Next X                     FFM integrated only
                                                                                                                                               H   W     2C
                            M                                                                                                                                                 2        H          W            1                                           layer                   low-level features needed
                                                  1    1   4C                                                                                                                                                                                   +                                         by decoder
                                                                                                                                                                                                                                                                                         To decoder
                                      Channel-wise rectification                                                                                         Spatial-wise rectification
                                                                                                                                                                                                                                                                             C           Concatenate
                                                           b) CM-FRM: Cross-Modal Feature Rectification Module
                                                                                                                                                                                                                                                                             A         Average Pooling

                                                                                                                                                                                                    Conv 1 1
                                                                 N       Ci
                            N   C      RGB Residual
                                                                                                  Channel Proj.

                                                                                                                          Add & Norm
                Embedding
                 Channel

                                      RGB Interactive                                                                                                                                                                                                                        M           Max Pooling
         FRGB                                                                       C
                                              K                                         N   2Ci                   N   C

                                                                                                                                                                                       3

                                                                                                                                                                                                                                   Add & Norm
                                                      X     GRGB              X                                                                                               1

                                                                                                                                                                                                          1
                                              V
                                                                                                                                                                                       DWConv 3
                                                                                                                                                                                                  RELU
                                                                                                                                                       Merge

                                                                                                                                                                                                                                                      Fmerged                +        Element-wise Add
                                                                                                                                                                              Conv 1

                                                                                                                                                                                                          Conv 1
                                                                                                                                               C
                                                                                                                                                               H    W    2C                                        H   W   C
                                              K
                                                                                                  Channel Proj.

                                                                                                                           Add & Norm

                                                             GX               X
                Embedding

                                                      X
                 Channel

                                              V                                                                                                                                                                                                                              X   Channel-wise Multiplication
          FX                                                                        C
                                       X Interactive                                 N      2Ci                   N   C

                                        X Residual
                                                                N x Ci
                                                                                                                                                                                                                                                                             X    Spatial-wise Multiplication

                                                  Stage 1                                                                                                                                         Stage 2
                                                                                                                                                                                                                                                                             X          Cross Product
                                                                                    c) FFM: Feature Fusion Module

Fig. 4: a) Overview of CMX for RGB-X semantic segmentation. The inputs are RGB and another modality (e.g., Depth, Thermal,
Polarization, Event, or LiDAR). b) Cross-Modal Feature Rectification Module (CM-FRM) with colored arrows as information
flows of the two modalities. c) Feature Fusion Module (FFM) with two stages of information exchange and fusion.

                III. P ROPOSED F RAMEWORK : CMX                                                                                                                       While features from different modalities have their specific
                                                                                                                                                                   noisy measurements, the feature of another modality has the
A. Framework Overview                                                                                                                                              potential for rectifying and calibrating the noisy information.
                                                                                                                                                                   As shown in Fig. 4b, we design a Cross-Modal Feature
   The overview of CMX is shown in Fig. 4a. We use two                                                                                                             Rectification Module (CM-FRM) to rectify one feature regard-
parallel branches to extract features from RGB- and X-modal                                                                                                        ing another feature, and vice versa. In this manner, features
inputs, which can be RGB-Depth, -Thermal, -Polarization, -                                                                                                         from both modalities can be rectified. Besides, CM-FRMs are
Event, -LiDAR data, etc. Specifically, our proposed framework                                                                                                      assembled between two adjacent stages of backbones. In this
for RGB-X semantic segmentation adopts a two-branch design                                                                                                         way, both rectified features are sent to the next stage to further
to effectively extract features from both RGB and X modal                                                                                                          deepen and improve the feature extraction. Furthermore, as
inputs. The two branches involve the simultaneous processing                                                                                                       shown in Fig. 4c, we design a two-stage Feature Fusion
of RGB and X modal data in a parallel but interactive                                                                                                              Module (FFM) to fuse features belonging to the same level
manner, each of which is designed to capture the unique                                                                                                            into a single feature map. Then, a decoder is used to predict the
characteristics of the respective input modality. We introduce a                                                                                                   final semantic map. In Sec. III-B and Sec. III-C, we detail the
rectification mechanism between both branches, enabling the                                                                                                        design of CM-FRM and FFM, respectively. In the following,
feature from one modality to be rectified based on the fea-                                                                                                        we use X to refer to the supplementary modality, which can
ture from another modality. Additionally, we facilitate cross-                                                                                                     be Depth-, Thermal-, Polarization-, Event-, LiDAR data, etc.
modal feature interaction by exchanging rectified features from
both modalities at each stage of the two-branch architecture.
Based on two-branch architecture, our framework leverages                                                                                                          B. Cross-Modal Feature Rectification
the complementary information of both modalities to enhance                                                                                                           As analyzed above, the information originating from dif-
the performance of RGB-X semantic segmentation.                                                                                                                    ferent sensing modalities are usually complementary [8], [9]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             5

but contain noisy measurements. The noisy information can                                                                                                                                                                                                                                                            λC and λS are two hyperparameters. We set them both as 0.5
be filtered and calibrated by using features coming from                                                                                                                                                                                                                                                             as default and will ablate in Sec. V-F. RGBout and Xout
another modality. To this purpose, in Fig. 4b, we propose a                                                                                                                                                                                                                                                          are the rectified features after the comprehensive calibration,
novel Cross-Modal Feature Rectification Module (CM-FRM)                                                                                                                                                                                                                                                              which will be sent into the next stage for feature fusion.
to perform feature rectification between parallel streams at
each stage in feature extraction. To tackle noises and un-                                                                                                                                                                                                                                                           C. Feature Fusion
certainties in diverse modalities, CM-FRM processes features
in two dimensions, including channel-wise and spatial-wise                                                                                                                                                                                                                                                              After obtaining the feature maps at each layer, we build a
feature rectification, which together offer a holistic calibration,                                                                                                                                                                                                                                                  two-stage Feature Fusion Module (FFM) to enhance the infor-
enabling better multi-modal feature extraction and interaction.                                                                                                                                                                                                                                                      mation interaction and combination. As shown in Fig. 4(c), in
Channel-wise feature rectification. We embed bi-modal fea-                                                                                                                                                                                                                                                           the information exchange stage (Stage 1), the two branches are
tures RGBin ∈ RH×W ×C and Xin ∈ RH×W ×C along the                                                                                                                                                                                                                                                                    still maintained, and a cross-attention mechanism is designed
spatial axis into two attention vectors WRGB   C
                                                       ∈ RC and                                                                                                                                                                                                                                                      to globally exchange information between the two branches.
WX C
      ∈ RC . Different from previous channel-wise attention                                                                                                                                                                                                                                                          In the fusion stage (Stage 2), the concatenated feature is trans-
methods [9], [17], [52], we apply both global max pooling and                                                                                                                                                                                                                                                        formed into the original size via a mixed channel embedding.
global average pooling to RGBin and Xin along the channel                                                                                                                                                                                                                                                            Information exchange stage. At this stage, the bi-modal
dimension to retain more information. We concatenate the four                                                                                                                                                                                                                                                        features will exchange their information via a symmetric
resulted vectors, having Y ∈ R4C . Then, an MLP is applied,                                                                                                                                                                                                                                                          dual-path structure. For brevity, we take the X-modal path
followed by a sigmoid function to obtain WC ∈ R2C from                                                                                                                                                                                                                                                               for illustration. We first flatten the input feature with size
Y, which will be split into WRGB C
                                       and WX  C
                                                 :                                                                                                                                                                                                                                                                   RH×W ×C to RN ×C , where N =H×W . Afterward, a linear
                                                                                                                                                                                                                                                                                                                     embedding is used to generate two vectors with the same
                                                                                                                                                                                                                                                                                                                     size RN ×Ci , which we call residual vector Xres and in-
                                                    \mathbf {W}_{RGB}^{C}, \mathbf {W}_{X}^{C} = \mathcal {F}_{split}\Bigg (\sigma \bigg (\mathcal {F}_{mlp}(\rm \mathbf Y)\bigg )\Bigg ),                                                                                                                     (1)
                                                                                                                                                                                                                                                                                                                     teractive vector Xinter . We further put forward an efficient
                                                                                                                                                                                                                                                                                                                     cross-attention mechanism applied to these two interactive
where σ(·) denotes the sigmoid function. The channel-wise                                                                                                                                                                                                                                                            vectors from different modal paths, which will carry out
rectification is then operated as:                                                                                                                                                                                                                                                                                   sufficient information exchange across modalities. This offers
                                                                                         \begin {aligned} \mathbf {RGB}_{rec}^{C} &= \mathbf {W}_{X}^{C} \circledast \mathbf {X}_{in},\\ \mathbf {X}_{rec}^{C} &= \mathbf {W}_{RGB}^{C} \circledast \mathbf {RGB}_{in}, \end {aligned}                               complementary interactions from the sequence-to-sequence
                                                                                                                                                                                                                                                                                                               (2)   perspective beyond the rectification-based interactions from
                                                                                                                                                                                                                                                                                                                     the feature map perspective in CM-FRM.
where ⊛ denotes channel-wise multiplication.                                                                                                                                                                                                                                                                            Our cross-attention mechanism for enhancing cross-modal
Spatial-wise feature rectification. As the aforementioned                                                                                                                                                                                                                                                            feature fusion is based on the traditional self-attention [20].
channel-wise feature rectification module concentrates on                                                                                                                                                                                                                                                            The original self-attention operation encodes the input vectors
learning global weights for a global calibration, we further                                                                                                                                                                                                                                                         into Query (Q), Key (K), and Value (V). The global attention
introduce a spatial-wise feature rectification for calibrating                                                                                                                                                                                                                                                       map is calculated via a matrix multiplication QKT , which
local information. The bi-modal inputs RGBin and Xin will                                                                                                                                                                                                                                                            has a size of RN ×N and causes a high memory occupation.
be concatenated and embedded into two spatial weight maps:                                                                                                                                                                                                                                                           In contrast, [53] uses a global context vector G = KT V
   S
WRGB    ∈RH×W and WX    S
                          ∈RH×W . The embedding operation                                                                                                                                                                                                                                                            with a size RChead ×Chead and the attention result is calculated
has two 1×1 convolution layers assembled with a RELU                                                                                                                                                                                                                                                                 by QG. We flexibly adapt the reformulation and develop
function. Afterward, a sigmoid function is applied to obtain                                                                                                                                                                                                                                                         our multi-head cross-attention based on this efficient self-
the embedded feature map F∈RH×W ×2 , which is further split                                                                                                                                                                                                                                                          attention mechanism. Specifically, the interactive vectors will
into two weight maps. The process to obtain the spatial weight                                                                                                                                                                                                                                                       be embedded into K and V for each head, and both sizes of
maps is formulated as:                                                                                                                                                                                                                                                                                               them are RN ×Chead . The output is obtained by multiplying
                                                                                                                                                                                                                                                                                                                     the interactive vector and the context vector from the other
    \rm {\mathbf {F}} = {Conv}_{1\times 1}\Bigg ({RELU}\bigg ({Conv}_{1\times 1}(\mathbf {RGB}_{in} \parallel \mathbf {X}_{in})\bigg )\Bigg ),  (3)                                                                                                                                                                  modality path, namely a cross-attention process, and it is
                                                                                                                                                                                                                                                                                                                     depicted in the following equations:

                                                                                        \mathbf {W}_{RGB}^{S}, \mathbf {W}_{X}^{S} = \mathcal {F}_{split}\bigg (\sigma (\rm \mathbf F)\bigg ).                                                                                                                 (4)                                                \begin {aligned} \mathbf {G}_{RGB} &= \mathbf {K}_{RGB}^{T}\mathbf {V}_{RGB},\\ \mathbf {G}_{X} &= \mathbf {K}_{X}^{T}\mathbf {V}_{X}, \end {aligned} 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           (7)
Similar to channel-wise rectification, spatial-wise rectification
is formulated as:                                                                                                                                                                                                                                                                                                                  \begin {aligned} \mathbf {U}_{RGB} &= \mathbf {X}_{RGB}^{inter}\ SoftMax(\mathbf {G}_{X}),\\ \mathbf {U}_{X} &= \mathbf {X}_{X}^{inter}\ SoftMax(\mathbf {G}_{RGB}). \end {aligned} 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           (8)
                                                                                           \begin {aligned} \mathbf {RGB}_{rec}^{S} &= \mathbf {W}_{X}^{S} * \mathbf {X}_{in},\\ \mathbf {X}_{rec}^{S} &= \mathbf {W}_{RGB}^{S} * \mathbf {RGB}_{in}, \end {aligned} 
                                                                                                                                                                                                                                                                                                               (5)
                                                                                                                                                                                                                                                                                                                     Note that G denotes the global context vector, while U
                                                                                                                                                                                                                                                                                                                     indicates the attended result. To realize the attention from
where ∗ denotes spatial-wise multiplication.
                                                                                                                                                                                                                                                                                                                     different representation subspaces, we remain the multi-head
  The whole rectified feature for both modalities RGBout
                                                                                                                                                                                                                                                                                                                     mechanism, where the number of heads matches the trans-
and Xout is organized as:
                                                                                                                                                                                                                                                                                                                     former backbone. Then, the attended result vector U and the
       ~\label {eq:CM_FRM} \begin {aligned} \mathbf {RGB}_{out} &= \mathbf {RGB}_{in} + \lambda _{C}\mathbf {RGB}_{rec}^{C} + \lambda _{S}\mathbf {RGB}_{rec}^{S},\protect \\ \mathbf {X}_{out} &= \mathbf {X}_{in} + \lambda _{C}\mathbf {X}_{rec}^{C} + \lambda _{S}\mathbf {X}_{rec}^{S}. \end {aligned}          residual vector Xres are concatenated. Finally, we apply a
                                                                                                                                                                                                                                                                                                               (6)
                                                                                                                                                                                                                                                                                                                     second linear embedding and resize the feature to RH×W ×C .
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       6

Fusion stage. In the second stage of FFM, precisely the
fusion stage, we use a simple channel embedding to merge
the two paths’ features, which is realized via 1×1 convolution
layers. Further, we consider that during such a channel-wise
fusion, the information of surrounding areas should also be
exploited for robust RGB-X segmentation. Thereby, inspired
by Mix-FFN in [33] and ConvMLP [54], we add one more                                                                                                                                                                                                           (a) Direct                                                                                                                                                  (b) Ours
depth-wise convolution layer DW Conv 3×3 to realize a skip-
                                                                                                                                                                                                                                   Fig. 5: Comparison between event representations.
connected structure. In this way, the merged features with the
size RH×W ×2C are fused into the final output with the size
of RH×W ×C for feature decoding.                                                                                                                                                                        In our experiments, we further study monochromatic and
                                                                                                                                                                                                        trichromatic polarization cues, coupled with RGB images in
D. Multi-modal Data Representations                                                                                                                                                                     multi-modal RGB-P semantic segmentation. For monochro-
RGB-Depth. Depth images naturally offer range, position, and                                                                                                                                            matic representation used in previous works [12], [56], we
contour information. The fusion of RGB and depth information                                                                                                                                            obtain it from monochromatic intensity measurements and
can better separate objects with indistinguishable colors and                                                                                                                                           convert it to 3-channel input by copying the single-channel
textures at different spatial locations. We encode the depth im-                                                                                                                                        information. For trichromatic polarization representation in
ages into HHA format [55]. HHA offers geometric properties,                                                                                                                                             either DoLP or AoLP , we compute separately for their
including horizontal disparity, height above ground, and angle.                                                                                                                                         respective RGB channels.
RGB-Thermal. At night or in places with insufficient light,                                                                                                                                             RGB-Event. Event data provide multiple advantages such
objects, and backgrounds have similar color information and                                                                                                                                             as high dynamic range, high temporal resolution, and not
are difficult to distinguish. Thermal images provide infrared                                                                                                                                           being influenced by motion blur [57], which are critical in
characteristics of objects, which are the potential to improve                                                                                                                                          dynamic scenes with motion information such as road-driving
objects with thermal properties such as people. We directly                                                                                                                                             environments [13], [44]. To process event data, a set of raw
use the infrared thermal image and copy the single-channel                                                                                                                                              events in a time window ∆T =tN −t1 is embedded into a
thermal image input 3 times to match the backbone input.                                                                                                                                                voxel grid with spatial dimensions H×W and time bins B,
RGB-Polarization. High-reflectivity objects such as glasses                                                                                                                                             where t1 and tN are the start- and the end time stamp. Unlike
and cars in RGB images are easily confused with surround-                                                                                                                                               previous work [26] converting event data to B=3, in this work,
ings. Polarization cameras record the optical polarimetric                                                                                                                                              events are first embedded into a voxel grid with a higher time
information when polarized reflection occurs, which offers                                                                                                                                              resolution, which we set the upscale size of the event bin as
complementary information in scenes with specular surfaces.                                                                                                                                             6. Then, every 6 panels are superimposed to obtain a fine-
The polarization sensor is equipped with a polarization mask                                                                                                                                            grained event embedding. A comparison between the direct
layer with four different directions [12] and thereby each                                                                                                                                              representation [26] and our event representation is shown in
captured image set consists of four pixel-aligned images                                                                                                                                                Fig. 5, in which our representation is more fine-grained in
at different polarization angles [I0◦ , I45◦ , I90◦ , I135◦ ], where                                                                                                                                    each event panel. Apart from B=3, we further investigate
Iangle denotes the image recorded at the corresponding angle.                                                                                                                                           different settings of event time bin B={1, 5, 10, 15, 20, 30} in
   We investigate two representations, i.e., the Degree of Lin-                                                                                                                                         our method for reaching robust RGB-E semantic segmentation.
ear Polarization (DoLP ) and the Angle of Linear Polarization                                                                                                                                           RGB-LiDAR. LiDAR camera can provide reliable and accu-
(AoLP ), which are key polarimetric properties characterizing                                                                                                                                           rate spatial-depth information on the physical world [14]. To
light polarization patterns [12]. They are derived by Stokes                                                                                                                                            make the representation of LiDAR data consistent with RGB
vectors S={S0 , S1 , S2 , S3 } that describe the polarization state                                                                                                                                     images, we follow [14] to convert LiDAR data to a range-view
of light. Precisely, S0 represents the total light intensity, S1                                                                                                                                        image-like format. The Field-of-View (FoV) of the camera is
and S2 denote the ratio of 0◦ and 45◦ linear polarization                                                                                                                                               90◦ and the image resolution is H×W =1408×376. The origin
over its perpendicular polarized portion, and S3 stands for the                                                                                                                                         is (u0 , v0 )=(H/2, W/2). Then, the focal length (fx , fy ) can
circular polarization power which is not involved in our work.                                                                                                                                          be calculated through:
The Stokes vectors S0 , S1 , S2 can be calculated from image                                                                                                                                                                                                                  \label {eq:fov} \begin {aligned} f_x &= H/(2{\times }tan(FoV{\times }\pi /360)), \\ f_y &= W/(2{\times }tan(FoV{\times }\pi /360)). \end {aligned} 
intensity measurements {I0◦ , I45◦ , I90◦ , I135◦ } via:                                                                                                                                                                                                                                                                                                                                                                                                                                               (12)

                  \begin {aligned} S_0 &= I_{0^\circ }+I_{90^\circ }=I_{45^\circ }+I_{135^\circ },\\ S_1 &= I_{0^\circ }-I_{90^\circ },\\ S_2 &= I_{45^\circ }-I_{135^\circ }. \end {aligned}           Similar to [58], we project the LiDAR 3D points from the
                                                                                                                                                                                                  (9)   world coordinate to the 2D image coordinate by using:
                                                                                                                                                                                                                \begin {bmatrix} u \\ v \\ 1 \\ \end {bmatrix} = \begin {bmatrix} f_x & 0 & u_0 & 0 \\ 0 & f_y & v_0 & 0 \\ 0 & 0 & 1 & 0 \\ \end {bmatrix} \begin {bmatrix} \boldsymbol {R} & \boldsymbol {t} \\ \boldsymbol {0}^T_{3{\times }1} & 1 \\ \end {bmatrix} \begin {bmatrix} X \\ Y \\ Z \\ 1 \\ \end {bmatrix},
Then, DoLP and AoLP are formally computed as:                                                                                                                                                                                                                                                                                                                                                                                                                                                          (13)

                                                                DoLP = \frac {\sqrt {S_1^2+S_2^2}}{S_0},                                                                                         (10)
                                                                                                                                                                                                        where (X, Y, Z) is the LiDAR point, (u, v) is the 2D image
                                                                                                                                                                                                        pixel, and the rotation (R) and the translation (t) matrices are
                                              AoLP = \frac {1}{2}arctan\bigg (\frac {S_2}{S_1}\bigg ).                                                                                           (11)   given by KITTI-360 dataset [25].
                                                                                                                                                                     7

          IV. E XPERIMENT DATASETS AND S ETUPS                            TABLE I: C OMPARISON OF EVENT- BASED SEMANTIC SEG -
                                                                          MENTATION DATASETS .
A. Datasets
                                                                           Dataset              Image        Event   Train/Val      Label       Resolution   Class
   We use five RGB-Depth semantic segmentation datasets,                   DDD17 [57]           Gray-scale   50Hz    15950/3890     pseudo      346 × 260       6
and datasets of RGB-Thermal, RGB-Polarization, RGB-Event,                  DSEC-Semantic [65]
                                                                           EventScape [26]
                                                                                                Gray-scale
                                                                                                RGB
                                                                                                             20Hz
                                                                                                             500Hz
                                                                                                                     8082/2809
                                                                                                                     122329/22493
                                                                                                                                    pseudo
                                                                                                                                    synthetic
                                                                                                                                                640 × 440
                                                                                                                                                512 × 256
                                                                                                                                                               11
                                                                                                                                                               12
and RGB-LiDAR combinations to verify our proposed CMX.
NYU Depth V2 dataset [24] contains 1449 RGB-D images
with the size 640×480, divided into 795 training images and               RoadLines, Fences, Pedestrian, TrafficSign,
654 testing images with annotations on 40 semantic categories.            Sidewalk, and TrafficLight.
SUN-RGBD dataset [59] has 10335 RGB-D images with                         RGB-L KITTI-360 dataset. KITTI-360 [25] is a suburban
37 classes, and 5285/5050 for training/testing. Following [9],            driving dataset, which has 49004/12276 images at the size
[60], we randomly crop and resize the input to 480×480.                   of 1408×376 for training/validation. There are 19 semantic
Stanford2D3D dataset [61] has 70496 RGB-D images with                     classes following the Cityscapes dataset [63].
13 object categories. Following the data splitting [15], [45],
areas of {1, 2, 3, 4, 6} are used for training and area 5 is for
                                                                          B. Implementation Details
testing. The input image is resized to 480×480.
ScanNetV2 dataset [62] provides 19466/5436/2135 RGB-D                        During training on all datasets, data augmentation is per-
samples for training/validation/testing. There are 20 classes.            formed by random flipping and scaling with random scales
During training, the RGB images are re-scaled to the same                 [0.5, 1.75]. We take Mix Transformer encoder (MiT) pre-
size of 640×480 as the depth images. During testing, the                  trained on ImageNet [66] as the backbone and MLP-decoder
predictions are in the original size of 1296×968.                         with an embedding dimension of 512 unless specified, both in-
Cityscapes dataset [63] is an outdoor RGB-D dataset of urban              troduced in SegFormer [33]. We select AdamW optimizer [67]
road-driving street scenes. It is divided into 2975/500/1525              with weight decay 0.01. The original learning rate is set as
images in the training/validation/testing splits, both with finely        6e−5 and we employ a poly learning rate schedule. We use
annotated dense labels on 19 classes. The image scenes cover              cross-entropy as the loss function. When reporting multi-scale
50 different cities with a full resolution of 2048×1024.                  testing results on NYU Depth V2 and SUN RGB-D, we use
RGB-T MFNet dataset [10] is a multi-spectral RGB-Thermal                  multiple scales {0.75, 1, 1.25} with horizontal flipping. We use
image dataset, which has 1569 images annotated in 8 classes               mean Intersection over Union (mIoU) averaged across seman-
at the resolution of 640×480. 820 images are captured during              tic classes as the primary evaluation metric to measure the
the day and the other 749 are at night. The training set has 50%          segmentation performance. More specific settings for different
of the daytime- and 50% of the nighttime images, while the                datasets are described in detail in the appendix.
validation- and test set respectively have 25% of the daytime-
and 25% of the nighttime images.                                                     V. E XPERIMENTAL R ESULTS AND A NALYSES
RGB-P ZJU dataset [12] is an RGB-Polarization dataset col-                   In this section, we present experimental results to verify the
lected by a multi-modal vision sensor designed for automated              effectiveness of our proposed CMX for RGB-X semantic seg-
driving [18] on complex campus street scenes. It is composed              mentation. In Sec. V-A, we show the results of CMX on mul-
of 344 images for training and 50 images for evaluation, both             tiple indoor and outdoor RGB-Depth benchmarks, compared
labeled with 8 semantic classes at the pixel level. The input             with state-of-the-art methods. In Sec. V-B, we analyze the
image is resized to 612×512.                                              RGB-Thermal segmentation performance for robust daytime-
RGB-E EventScape dataset. A large-scale multi-modal                       and nighttime semantic perception. In Sec. V-C and Sec. V-D,
RGB-Event semantic segmentation benchmark is not avail-                   we study the generalization of CMX to RGB-Polarization
able. To fill this gap, we create an RGB-Event multi-                     and RGB-Event modality combinations and representations of
modal semantic segmentation benchmark1 based on the                       these multi-modal data. In Sec. V-E, we present the results of
EventScape dataset [26], which is originally designed for                 CMX on the RGB-LiDAR dataset. In Sec. V-F, we conduct a
depth estimation. The comparison between three event-                     comprehensive variety of ablation studies to confirm the effects
based semantic segmentation datasets is presented in Ta-                  of different components in our solution. Finally, we perform
ble. I. Unlike previous datasets using gray-scale images                  efficiency- and qualitative analysis in Sec. V-G and Sec. V-H.
and pseudo labels, the RGB and the synthetic labels are
available in our benchmark, which can provide more suf-
ficient information and more precise annotations. To main-
                                                                          A. Results on RGB-Depth Datasets
tain data diversity from the original sequences generated by
CARLA simulator [64], we select one frame from every                         We first conduct experiments on RGB-D semantic segmen-
30 frames, obtaining 4077/749 images from 122329/22493                    tation datasets. The results are grouped in Table II.
for training/evaluation. The images have a 512×256 resolu-                NYU Depth V2. The results on the NYU Depth V2 dataset
tion and are annotated with 12 semantic classes, including                are shown in Table IIa. It can be easily seen that our approach
Vehicle, Building, Wall, Vegetation, Road, Pole,                          achieves leading scores. The proposed method with MiT-
                                                                          B2 already exceeds previous methods, attaining 54.4% in
  1 https://paperswithcode.com/sota/semantic-segmentation-on-eventscape   mIoU. Our CMX models based on MiT-B4 and -B5 further
                                                                                                                                             8

  TABLE II: R ESULTS ON FIVE RGB-D EPTH DATASETS . Acc AND ∗ DENOTE PIXEL ACCURACY AND MULTI - SCALE TEST.
  (a) Results on NYU Depth V2 [24].             (c) Results on SUN-RGBD [59].                  (e) Results on Cityscapes val set [63].
 Method              mIoU (%) Acc (%)         Method             mIoU (%)     Acc (%)       Method           Modal   Backbone     mIoU (%)
 3DGNN [68]               43.1      -         3DGNN [68]             45.9        -
 Kong et al. [69]         44.5     72.1       RDF-152 [72]           47.7       81.5        SwiftNet [80]    RGB     ResNet-18      70.4
 LS-DeconvNet [70]        45.9     71.9       CFN [71]               48.1        -          ESANet [81]      RGB     ResNet-50      79.2
 CFN [71]                 47.7      -         D-CNN [45]             42.0        -
                                              ACNet [8]              48.1        -          GSCNN [82]       RGB WideResNet-38      80.8
 ACNet [8]                48.3      -
 RDF-101 [72]             49.1     75.6       TCD [74]               49.5       83.1        CCNet [30]       RGB     ResNet-101     81.3
                                              SGNet [16]             48.6       82.0
 SGNet [16]               51.1     76.8       SA-Gate [9]            49.4       82.5        DANet [7]        RGB     ResNet-101     81.5
 ShapeConv [15]           51.3     76.4       NANet [60]             48.8       82.3
 NANet [60]               52.3     77.9                                                     ACFNet [83]      RGB     ResNet-101     81.5
                                              ShapeConv [15]         48.6       82.2
 SA-Gate [9]              52.4     77.9                                                     SegFormer [33]   RGB      MiT-B2        81.0
                                              CMX (MiT-B2)∗          49.7       82.8
 CMX (MiT-B2)             54.1     78.7       CMX (MiT-B4)∗          52.1       83.5        SegFormer [33]   RGB      MiT-B4        82.3
 CMX (MiT-B2)∗            54.4     79.9       CMX (MiT-B5)∗          52.4       83.8
 CMX (MiT-B4)             56.0     79.6                                                     RFNet [3]        RGB-D   ResNet-18      72.5
 CMX (MiT-B4)∗            56.3     79.9
 CMX (MiT-B5)             56.8     79.9
                                             (d) Results on ScanNetV2 test set [62].        PADNet [84]      RGB-D   ResNet-50      76.1
 CMX (MiT-B5)∗            56.9     80.1        Method                Modal   mIoU (%)       Kong et al. [69] RGB-D   ResNet-101     79.1
                                                                                            ESANet [81]      RGB-D   ResNet-50      80.0
  (b) Results on Stanford2D3D [61].            PSPNet [6]            RGB       47.5
                                               AdapNet++ [75]        RGB       50.3         SA-Gate [9]      RGB-D   ResNet-50      80.7
  Method                 mIoU (%) Acc (%)      3DMV (2d-proj) [76]   RGB-D     49.8         SA-Gate [9]      RGB-D   ResNet-101     81.7
                                               FuseNet [77]          RGB-D     53.5         AsymFusion [85] RGB-D    Xception65     82.1
  Depth-aware CNN [45]     39.5     65.4       SSMA [75]             RGB-D     57.7
  MMAF-Net-152 [73]        52.9     76.5       GRBNet [38]           RGB-D     59.2         SSMA [75]        RGB-D   ResNet-50      82.2
  ShapeConv-101 [15]       60.6     82.7       MCA-Net [78]          RGB-D     59.5
                                               DMMF [79]             RGB-D     59.7         CMX              RGB-D    MiT-B2        81.6
  CMX (MiT-B2)             61.2     82.3
  CMX (MiT-B4)             62.1     82.6       CMX (MiT-B2)          RGB-D     61.3         CMX              RGB-D    MiT-B4        82.6

dramatically improve the mIoU to 56.3% and 56.9%, clearly               other datasets, because the performance of RGB-only models
standing out in front of all state-of-the-art approaches. The best      on this dataset shows a saturation trend. Compared with MiT-
CMX model even reaches superior results than recent strong              B2 (RGB), our RGB-D approach elevates the mIoU by 0.6%.
pretraining-based methods [19], [49] like Omnivore [19] that            Our approach based on MiT-B4 achieves a state-of-the-art
uses images, videos, and single-view 3D data for supervision.           score of 82.6%, outstripping all existing RGB-D methods by
Stanford2D3D. In Table IIb, our CMX achieves state-of-the-              more than 0.4% in absolute mIoU values, verifying that CMX
art mIoU scores. Our B2-based CMX surpasses the previous                generalizes well to street scene understanding.
best ShapeConv [15] based on ResNet-101 [86] in mIoU and
our model based on MiT-B4 further reaches mIoU of 62.1%.                B. Results on RGB-Thermal Dataset
The results demonstrate the effectiveness and learning capacity
                                                                        Comparison with the state-of-the-art. In Table III, we
of our approach on such a large RGB-D dataset.
                                                                        compare our method against RGB-only models and multi-
SUN-RGBD. As presented in Table IIc, our method achieves                modal methods using RGB-T inputs of MFNet dataset [10].
leading performances on the SUN-RGBD dataset. Our inter-                As unfolded, ACNet [8] and SA-Gate [9], carefully designed
active cross-modal fusion approach (Fig. 2c) exceeds previ-             for RGB-Depth segmentation, perform less satisfactorily on
ous input fusion methods (Fig. 2a), e.g., SGNet [16] and                RGB-T data, as they focus on feature extraction without
ShapeConv [15], as well as feature fusion methods (Fig. 2b),            sufficient feature interaction before fusion and thereby fail
e.g., ACNet [8] and SA-Gate [9]. In particular, with MiT-B4             to generalize to other modality. Depth-aware CNN [45], an
and -B5, CMX elevates the mIoU to >52.0%. CMX is also                   input fusion method with modality-specific operator design,
better than multi-task methods like PAP [48] and TET [87].              also does not yield high performance. In contrast, the proposed
ScanNetV2. We test our CMX model with MiT-B2 on the                     CMX strategy, enabling comprehensive interactions from var-
ScanNetV2 benchmark. As shown in Table IId, it can be                   ious perspectives, generalizes smoothly in RGB-T semantic
clearly seen that CMX outperforms RGB-only methods and                  segmentation. It can be seen that our method based on MiT-B2
achieves the top mIoU of 61.3% among the RGB-D methods.                 achieves mIoU of 58.2%, clearly outperforming the previous
On the ScanNetV2 leaderboard, methods like BPNet [88]                   best RGB-T methods ABMDRNet [11], FEANet [17], and
reach higher scores by using 3D supervision from point clouds           GMNet [42]. Our CMX with MiT-B4 further elevates state-
to perform joint 2D- and 3D reasoning. In contrast, our                 of-the-art mIoU to 59.7%, widening the accuracy gap in
method attains a competitively accurate performance by using            contrast to existing methods. Moreover, it is worth pointing
purely 2D data and effectively leveraging the complementary             out that the improvements brought by our RGB-X approach
information inside RGB-D modalities.                                    compared with the RGB-only baselines are compelling, i.e.,
Cityscapes. Besides indoor RGB-D datasets, to study the                 +5.0% and +4.9% in mIoU for MiT-B2 and -B4 backbones,
generalizability to outdoor scenes, we assess the effectiveness         respectively. Our approach overall achieves top scores on car,
of CMX on Cityscapes. As shown in Table IIe, we note that               person, bike, curve, car stop, and bump. For person with
the improvement on the Cityscapes dataset is not as obvious as          infrared properties, our approach enjoys more than +11.0%
                                                                                                                                                9

                TABLE III: P ER - CLASS RESULTS ON MFN ET DATASET [10] FOR RGB-T HERMAL SEGMENTATION .
   Method                    Modal     Unlabeled    Car     Person      Bike     Curve    Car Stop   Guardrail    Color Cone   Bump     mIoU

   ERFNet [89]               RGB            96.7    67.1      56.2      34.3      30.6       9.4         0.0          0.1       30.5     36.1
   DANet [7]                 RGB            96.3    71.3      48.1      51.8      30.2      18.2         0.7         30.3       18.8     41.3
   PSPNet [6]                RGB            96.8    74.8      61.3      50.2      38.4      15.8         0.0         33.2       44.4     46.1
   HRNet [90]                RGB            98.0    86.9      67.3      59.2      35.3      23.1         1.7         46.6       47.3     51.7
   SegFormer-B2 [33]         RGB            97.9    87.4      62.8      63.2      31.7      25.6         9.8         50.9       49.6     53.2
   SegFormer-B4 [33]         RGB            98.0    88.9      64.0      62.8      38.1      25.9         6.9         50.8       57.7     54.8
   MFNet [10]                RGB-T          96.9    65.9      58.9      42.9      29.9       9.9         0.0         25.2       27.7     39.7
   SA-Gate [9]               RGB-T          96.8    73.8      59.2      51.3      38.4      19.3         0.0         24.5       48.8     45.8
   Depth-aware CNN [45]      RGB-T          96.9    77.0      53.4      56.5      30.9      29.3         8.5         30.1       32.3     46.1
   ACNet [8]                 RGB-T          96.7    79.4      64.7      52.7      32.9      28.4         0.8         16.9       44.4     46.3
   PSTNet [91]               RGB-T          97.0    76.8      52.6      55.3      29.6      25.1        15.1         39.4       45.0     48.4
   RTFNet [40]               RGB-T          98.5    87.4      70.3      62.7      45.3      29.8         0.0         29.1       55.7     53.2
   FuseSeg [41]              RGB-T          97.6    87.9      71.7      64.6      44.8      22.7         6.4         46.9       47.9     54.5
   AFNet [92]                RGB-T          98.0    86.0      67.4      62.0      43.0      28.9         4.6         44.9       56.6     54.6
   ABMDRNet [11]             RGB-T          98.6    84.8      69.6      60.3      45.1      33.1         5.1         47.4       50.0     54.8
   FEANet [17]               RGB-T          98.3    87.8      71.1      61.1      46.5      22.1         6.6         55.3       48.9     55.3
   DHFNet [93]               RGB-T          97.7    87.6      71.7      61.1      39.5      42.4        9.5          49.3       56.0     57.2
   GMNet [42]                RGB-T          97.5    86.5      73.1      61.7      44.0      42.3        14.5         48.7       47.4     57.3
   CMX (MiT-B2)              RGB-T          98.3    89.4      74.8      64.7      47.3      30.1         8.1         52.4       59.4     58.2
   CMX (MiT-B4)              RGB-T          98.3    90.1      75.2      64.5      50.2      35.3         8.5         54.2       60.6     59.7

TABLE IV: S EGMENTATION RESULTS ON DAYTIME - AND                               the capacity of the transformer backbone and our cross-modal
NIGHTTIME IMAGES ON MFN ET DATASET [10].                                       fusion mechanisms. Compared to the RGB-only baseline with
 Method              Modal    Daytime mIoU (%)     Nighttime mIoU (%)          MiT-B2 [33]), the IoU improvements on classes with polari-
                                                                               metric characteristics are clear, such as glass (>8.0%) and car
 FRRN [94]             RGB           40.0                  37.3
 DFN [95]              RGB           38.0                  42.3                (>2.5%), further evidencing the generalizability of our cross-
 BiSeNet [96]          RGB           44.8                  47.7                modal fusion solution in bridging RGB-P streams.
 SegFormer-B2 [33]     RGB           48.6                  49.2
 SegFormer-B4 [33]     RGB           49.4                  52.4                Analysis of polarization data representations. We study
 MFNet [10]          RGB-T           36.1                  36.8                polarimetric data representations and the results displayed in
 FuseNet [77]        RGB-T           41.0                  43.9                Table V indicate that the Angle of Linear Polarization (AoLP )
 RTFNet [40]         RGB-T           45.8                  54.8
 FuseSeg [41]        RGB-T           47.8                  54.6                and the Degree of Linear Polarization (DoLP ) representa-
 GMNet [42]          RGB-T           49.0                  57.7                tions both carry effective polarization information beneficial
 CMX (MiT-B2)        RGB-T           51.3                  57.8                for semantic scene understanding, which is consistent with
 CMX (MiT-B4)        RGB-T           52.5                  59.4
                                                                               the finding in [12]. Besides, trichromatic representations are
                                                                               consistently better than monochromatic representations used
                                                                               in previous RGB-P segmentation works [12], [56]. This is
gain in IoU, confirming the effectiveness of CMX in harvesting                 expected as the trichromatic representation provides more de-
complementary cross-modal information.                                         tailed information, which should be leveraged to fully unlock
Day and night performances. Following [41], [42], we assess                    the potential of trichromatic polarization cameras.
day- and night segmentation results on the RGB-T benchmark
(see Table IV). For daytime scenes, our approach increases
mIoU by 2.7%∼3.1% compared with RGB-only baselines. At                         D. Results on RGB-Event Dataset
nighttime, RGB segmentation often suffers from poor lighting
                                                                               Comparison with the state-of-the-art. In Table VI, we
conditions, and it even carries much noisy information in the
                                                                               benchmark more than 10 semantic segmentation methods,
RGB data. Yet, our CMX rectifies the noisy images and ex-
                                                                               including RGB-only methods, CNN-based [80], [97], [98],
ploits supplementary features from thermal data, dramatically
                                                                               [100] and transformer-based [23], [33], [99] methods, as well
improving the mIoU by >7.0% and enhancing the robustness
                                                                               as multi-modal methods [3], [9], [13]. In contrast, our models
of semantic scene understanding in unfavorable environments
                                                                               improve performance by mixing RGB-Event features, as seen
with adverse illuminations.
                                                                               in Table VI and Fig. 6. Our model using MiT-B4 reaches
                                                                               64.28% in mIoU, towering over all other methods and setting
C. Results on RGB-Polarization Dataset                                         the state-of-the-art on the RGB-E benchmark. This further
Comparison with the state-of-the-art. Table V shows per-                       verifies the versatility of our solution for different multi-modal
class accuracy of our approach compared to RGB-only [33],                      combinations. Fig. 6 depicts a per-class accuracy comparison
[80] and RGB-Polarization fusion methods [12], [56] on ZJU-                    between the RGB baseline and our RGB-Event model with
RGB-P dataset [12]. Our unified CMX outperforms the previ-                     MiT-B2. With event data, the foreground objects are more
ous best RGB-P method [12] by >6.0% in mIoU. We observe                        accurately parsed by our RGB-E model, e.g., vehicle (+2.1%),
that the improvement on pedestrian is significant thanks to                    pedestrian (+11.7%), and traffic light (+7.0%).
                                                                                                                                                                                                                                                             10

                          TABLE V: P ER - CLASS RESULTS ON ZJU-RGB-P [12] DATASET FOR RGB-P OLARIZATION SEGMENTATION .
         Method                                                                            Modal                                     Building                   Glass     Car              Road   Vegetation    Sky       Pedestrian   Bicycle    mIoU

         SwiftNet [80]                                                                       RGB                                           83.0                 73.4      91.6             96.7      94.5       84.7         36.1       82.5          80.3
         SegFormer-B2 [33]                                                                   RGB                                           90.6                 79.0      92.8             96.6      96.2       89.6         82.9       89.3          89.6
         NLFNet [56]                                                                       RGB-P                                           85.4                 77.1      93.5             97.7      93.2       85.9         56.9       85.5          84.4
         EAFNet [12]                                                                       RGB-P                                           87.0                 79.3      93.6             97.4      95.3       87.1         60.4       85.6          85.7
         CMX (SegFormer-B2)                                        RGB-AoLP (Monochromatic)                                                91.9                 87.0      95.6             98.2      96.7       89.0         84.9       92.0          91.8
         CMX (SegFormer-B2)                                         RGB-AoLP (Trichromatic)                                                91.5                 87.3      95.8             98.2      96.6       89.3         85.6       91.9          92.0
         CMX (SegFormer-B4)                                        RGB-AoLP (Monochromatic)                                                91.8                 88.8      96.3             98.3      96.7       89.1         86.3       92.3          92.4
         CMX (SegFormer-B4)                                         RGB-AoLP (Trichromatic)                                                91.6                 88.8      96.3             98.3      96.8       89.7         86.2       92.8          92.6
         CMX (SegFormer-B2)                                        RGB-DoLP (Monochromatic)                                                91.4                 87.6      96.0             98.2      96.6       89.1         87.1       92.3          92.1
         CMX (SegFormer-B2)                                         RGB-DoLP (Trichromatic)                                                91.8                 87.8      96.1             98.2      96.7       89.4         86.1       91.8          92.2
         CMX (SegFormer-B4)                                        RGB-DoLP (Monochromatic)                                                91.8                 88.6      96.3             98.3      96.7       89.4         86.0       92.1          92.4
         CMX (SegFormer-B4)                                         RGB-DoLP (Trichromatic)                                                91.6                 88.6      96.3             98.3      96.7       89.5         86.4       92.2          92.5

         TABLE VI: R ESULTS FOR RGB-E VENT SEGMENTATION .                                                                                                                                                      Original       Ours
                                                                                                                                                                                      62
         Method                                                   Modal Backbone mIoU (%) Pixel Acc. (%)

                                                                                                                                                                           mIoU (%)
        SwiftNet [80]                                         RGB ResNet-18                                    36.67                       83.46                                      61
            SegFormerOurs
        Fast-SCNN [97]                                        RGB Fast-SCNN                                    44.27                       87.10
Vehicle
        CGNet [98]85.0                                   87.1
                                                              RGB   M3N21                                      44.75                       87.13                                      60
BuildingTrans4Trans
                  84.8
                     [99]                                85.4 RGB  PVT-B2                                      51.86                       89.03
Wall Swin-s [23]  51.0                                   49.4 RGB   Swin-s                                     52.49                       88.78
        Swin-b [23]
Vegetation        88.6                                   90.7 RGB   Swin-b                                     53.31                       89.21                                      59
Road
        DeepLabV3+96.2
                      [100]                              96.5
                                                              RGB ResNet-101                                   53.65                       89.92                                             1      3        5       10        15      20        30
        SegFormer-B2 [33]                                     RGB  MiT-B2                                      58.69                       91.21                                                            Event time bins
Pole              34.4
        SegFormer-B4 [33]                                40.6 RGB  MiT-B4                                      59.86                       91.61
RoadLines                         35.7                   37.6
        RFNet [3]                                           RGB-E ResNet-18                                    41.34                       86.25                           Fig. 7: Analysis of event representations and time bins.
Fences            27.3                                   28.8
        ISSAFE [13]                                         RGB-E ResNet-18                                    43.61                       86.83
Pedestrian        51.6
        SA-Gate [9]                                      63.3
                                                            RGB-E ResNet-101                                   53.94                       90.03
TrafficSign                       33.8                   37.8
Sidewalk
        CMX (DeepLabV3+) RGB-E ResNet-101
                79.8     82.2
                                                                                                               54.91                       89.67                        +7.90% gains in mIoU. The results show that our RGB-X
        CMX (Swin-s)        RGB-E Swin-s                                                                       60.86                       91.25                        solution consistently improves the segmentation performance,
TrafficLight    36.3
        CMX (Swin-b)     43.3
                            RGB-E Swin-b                                                                       61.21                       91.61
        CMX (SegFormer-B2) RGB-E MiT-B2                                                                        61.90                       91.88                        confirming that our unified framework is not strictly tied to
        CMX (SegFormer-B4) RGB-E MiT-B4                                                                        64.28                       92.60                        a concrete backbone type, but can be flexibly deployed with
                                                                                                                                                                        CNN- or transformer models, which helps to yield effective
                                                                                                                                                                        unified architecture for RGB-X semantic segmentation.
                                                                        SegFormer                     Ours                                                              Analysis of event data representations. We study with
      100                                                              96.5

                   87.1          85.4
                                                            90.7                                                                                                        different settings of event time bin B={1, 3, 5, 10, 15, 20, 30}
                                                                                                                                               82.2
         80
                                                                                                                                                                        based on our CMX fusion model with MiT-B2. Compared
                                                                                                                        63.3
                                                                                                                                                                        with the original event representation [26], our representation
         60
                                                                    96.2
                                                                                                                                                                        achieves consistent improvements (in Fig. 7) on different
                                           49.4         88.6
               85.0          84.8
                                                                                                                                            79.8
                                                                                                                                                          43.3
                                                                                                                                                                        settings of event time bins, such as +1.63% of mIoU when
                                                                                40.6
         40
                                         51.0
                                                                                                 37.6
                                                                                                                     51.6
                                                                                                                                    37.8
                                                                                                                                                                        B=30. In particular, it helps our CMX to obtain the highest
                                                                                                             28.8
                                                                              34.4           35.7                               33.8                   36.3             mIoU of 61.90% in the setting of B=3. In B=1, embedding
                                                                                                         27.3
         20
                                                                                                                                                                        all events in a single time bin leads to dragging behind images
                  icl
                     e
                                in
                                   g      all             tio
                                                              n        ad          le           ne
                                                                                                  s         es        ian          ig
                                                                                                                                      n        alk        gh
                                                                                                                                                            t
                                                                                                                                                                        of moving objects and being sub-optimal for feature fusion.
               eh           ild          W                          Ro        Po              Li          nc       str          cS                      Li
                                                       eta                                  d           Fe        e            i            ew        ic
           V             Bu                         eg                                     a
                                                                                                               Pe
                                                                                                                 d          af
                                                                                                                              f
                                                                                                                                        Si
                                                                                                                                          d
                                                                                                                                                   af
                                                                                                                                                     f
                                                V                                       Ro                               Tr                      Tr
                                                                                                                                                                        In higher time bins, events produced in a short interval are
                                                                                                                                                                        dispersed to more bins, resulting in insufficient events in a
     Fig. 6: Per-class IoU results of the RGB-only baseline and our                                                                                                     single bin. These corroborate observations in [13], [44] and
     RGB-Event model on our RGB-Event benchmark.                                                                                                                        that the event representation B=3 is an effective time bin
                                                                                                                                                                        setting for RGB-E semantic segmentation with CMX.
     Analysis of using different backbones. To verify that our
     unified method is effective with using different backbones,                                                                                                        E. Results on RGB-LiDAR Dataset
     we compare CNN- and transformer-based backbones in the                                                                                                                In Table VII, we compare CMX with other models dedicated
     CMX framework. Specifically, in addition to MiT backbones,                                                                                                         to RGB-LiDAR data fusion, including PMF [14] and Trans-
     we experiment with DeepLabV3+ [100] and Swin trans-                                                                                                                Fuser [104]. These two methods achieve respective 54.48%
     former [23] backbones with UperNet [101] to construct CMX.                                                                                                         and 56.57% in mIoU. Besides, other general multimodal
     Compared to the RGB-only DeepLabV3+, Swin-s, and Swin-b                                                                                                            fusion methods, e.g., HRFuser [102] and TokenFusion [103],
     methods, CMX models achieve respective +1.26%, +8.37%,                                                                                                             are included for comparison. In contrast, our CMX obtains the
                                                                                                                                  11

TABLE VII: R ESULTS FOR RGB-L I DAR SEGMENTATION .                 spatial only means using spatial-wise rectification only (λC =0
                                                                   and λS =1 in Eq. 6). It can be seen that substituting the
    Method                    Backbone           mIoU (%)
                                                                   proposed CM-FRM by either channel-only or spatial-only
    HRFuser [102]            HRFormer-T            48.74           variant causes a sub-optimal accuracy, further confirming the
    PMF [14]                  SalsaNext            54.48           efficacy of combining the bi-modal rectification for holistic
    TokenFusion [103]          MiT-B2              54.55           feature calibration, which is crucial for robust multi-modal
    TransFuser [104]        RegNetY-3.2GF          56.57
                                                                   segmentation. In our channel-wise calibration, we use both
    CMX                        MiT-B2              64.31
                                                                   global average pooling and global max pooling to retain more
                                                                   information. Table X shows that using only global average
                                                                   pooling (avg. p.) and using only global max pooling (max. p.)
state-of-the-art performance with 64.31% in mIoU, having a
                                                                   are less effective than our complete CM-FRM, which offers a
+9.76% gain compared with TokenFusion which is also based
                                                                   more comprehensive rectification.
on MiT-B2. The sufficient improvement proves the advantage
                                                                      Previous ablation studies support the design of CM-FRM.
of using a symmetric dual-stream architecture in modal fusion
                                                                   To understand the capability of FFM, we here test with two
and the effectiveness of our proposed cross-modal rectification
                                                                   variants. As shown in Table X, stage 2 only means there is no
and fusion methods.
                                                                   information exchange before the mixed channel embedding,
                                                                   whereas self attn denotes that context vectors will not be
F. Ablation Study                                                  exchanged in stage 1 of FFM. The two variants are less
   We perform a series of ablation studies to explore how dif-     constructive as compared to our complete FFM. Thanks to the
ferent parts of our architecture affect the segmentation. We use   crucial cross-attention design for information exchange, our
depth information encoded into HHA as the complementary            complete FFM productively rectifies and fuses the features at
modality here. We take MiT-B2 as the backbone with the MLP         different levels. These indicate the importance of fusion from
decoder in our ablation studies unless specified. The semantic     the sequence-to-sequence perspective, which is not considered
segmentation performance is evaluated on NYU Depth V2.             in previous works. Overall, the ablation shows that our interac-
RGB-only Baseline and CMX. In order to comprehen-                  tive strategy, providing comprehensive interactions, is effective
sively compare the RGB-only baseline [33] and our RGB-             for cross-modal fusion.
X-based model, we conduct experiments on five different            Ablation of the supplementary modality. Previous works
types of modality fusion, including RGB-Depth, -Thermal, -         have shown that multi-modal segmentation has a better per-
Polarization, -Event, and -LiDAR. Both methods are based           formance than single-modal RGB segmentation [8]. We carry
on the same backbone with MiT-B2 [33] As presented in              out experiments to certify that and the results are shown in
Table VIII, on six different datasets, i.e., NYU Depth V2,         Table XI. Note that here, the MLP decoder is not used, in
Cityscapes, MFNet, ZJU-RGB-P, EventScape, and KITTI-360,           order to focus on studying the influence of feature extraction
our CMX model obtains improvements of +6.1%, +0.6%,                from different supplementary modalities. As compared to the
+5.0%, +2.6%, +3.2%, and +3.0%, respectively. We note              RGB-only method, we conduct experiments with modalities
that the improvement on the Cityscapes dataset is not as obvi-     of RGB-RGB, RGB-Noise, RGB-Depth, and RGB-HHA. We
ous as other datasets, because the performance of RGB-only         found that replacing the supplementary modality with random
models on this dataset shows a saturation trend. Nonetheless,      noise can obtain even better results than two RGB inputs.
the consistent improvements achieved across five different         This means that even pure noise information may help the
multi-modal fusion tasks are a strong testament to the effec-      model identify noisy information in the RGB branch. The
tiveness of our proposed unified CMX framework for RGB-X           model learns to focus on relevant features and thus gains
semantic segmentation.                                             robustness. It may also help prevent over-fitting during the
Effectiveness of CM-FRM and FFM. We design CM-                     learning process. However, when using depth information, we
FRM and FFM to rectify and merge features coming from              have observed obvious improvements, which further proves
the RGB- and X-modality branches. We take out these two            that the fusion of RGB and depth information brings clearly
modules from the architecture respectively, where the results      better predictions. Encoding depth images using the HHA
are shown in Table IX. If CM-FRM is ablated, the features          representation further increases the scores. The overall gain
will be extracted independently in their own branches, and         of 5.3% in mIoU, compared with the RGB-only baseline, is
for FFM we simply average the two features for semantic            also compelling, which is similar to that in RGB-T semantic
prediction. Compared with the baseline, using only CM-FRM          segmentation, demonstrating the effectiveness of our proposed
improves mIoU by 2.5%, using only FFM improves mIoU by             method for rectifying and fusing cross-modal information.
1.2%, and together CM-FRM and FFM improve the semantic
segmentation performance by 3.8%. The improvements show
that our CM-FRM and FFM modules are both crucial for the           G. Efficiency Analysis
success of the unified CMX framework.                                 In Table XII, we present the computational complexity
Ablation with CM-FRM and FFM variants. We further                  results. Compared with the previous best method SA-Gate [9]
experiment with variants of CM-FRM and FFM modules.                on the NYU Depth V2 dataset, our model with MiT-B2 has
As shown in Table X, channel only denotes using channel-           similar #Params and lower FLOPs but significantly higher
wise rectification only (λC =1 and λS =0 in Eq. 6), and            mIoU. Our CMX model with MiT-B4 greatly elevates the
                                                                                                                                                     12

TABLE VIII: C OMPARISON BETWEEN RGB- ONLY BASELINE AND OUR CMX MODEL FOR RGB-X SEMANTIC SEGMENTA -
TION , WHERE ALL RESULTS ( M I O U) ARE BASED ON THE SAME BACKBONE WITH M I T-B2.

  Method                Modal          NYU Depth V2         Cityscapes       MFNet            ZJU-RGB-P            EventScape        KITTI-360
  SegFormer-B2 [33]     RGB-only       48.0                 81.0             53.2             89.6                 58.7              61.3
  CMX-B2                Multimodal     54.1 (RGB-D)         81.6 (RGB-D)     58.2 (RGB-T)     92.2 (RGB-P)         61.9 (RGB-E)      64.3 (RGB-L)

TABLE IX: A BLATION STUDY OF CM-FRM AND FFM ON                             TABLE XI: A BLATION OF THE SUPPLEMENTARY MODALITY
NYU D EPTH V2 test SET. Avg. IS THE AVERAGE FUSION .                       ON NYU D EPTH V2 test SET.

    CM-FRM            FFM       mIoU (%)             Pixel Acc. (%)          Modalities                   mIoU (%)                Pixel Acc. (%)

    ×                 Avg.           50.3                 76.8               RGB                             46.7                      73.8
    ✓                 Avg.           52.8                 78.0
                                                                             RGB + RGB                       47.2                      74.1
    ×                 ✓              51.5                 77.1               RGB + Noise                     47.7                      74.5
    ✓                 ✓              54.1                 78.7               RGB + Raw depth                 51.1                      75.7
                                                                             RGB + HHA                       52.0                      77.0

TABLE X: A BLATION WITH CM-FRM/FFM VARIANTS ON
NYU D EPTH V2 test SET.                                                    TABLE XII: E FFICIENCY RESULTS . FLOP S ARE ESTI -
                                                                           MATED FOR INPUTS OF RGB AND HHA, WITH A SIZE OF
  Feature Rectify       Feature Fusion      mIoU (%) Pixel Acc. (%)
                                                                           480×640×3.
  CM-FRM channel only FFM                     53.6          78.5
  CM-FRM spatial only FFM                     53.3          78.3             Method                     #Params (M)      FLOPs (G)       mIoU (%)

  CM-FRM avg. p. only FFM                     53.0          78.1             SA-Gate [9] (ResNet50)         63.4           204.9              50.4
  CM-FRM max. p. only FFM                     53.5          78.5             CMX (SegFormer-B2)             66.6            67.6              54.1
                                                                             CMX (SegFormer-B4)            139.9           134.3              56.0
  CM-FRM                FFM stage 2 only      53.8          78.5             CMX (SegFormer-B5)            181.1           167.8              56.8
  CM-FRM                FFM self attn         53.8          78.6
  CM-FRM                FFM                   54.1          78.7

                                                                                the distance is easily disturbed by overexposed lights in
                                                                                RGB, which can be rectified by Thermal modality.
mIoU score to 56.0%, further widening the accuracy gap                      (3) For RGB-Polarization, the specular glass areas are more
with moderate model complexity. With MiT-B5, mIoU further                       precisely parsed by our CMX model, as compared to the
increases to 56.8%, but it also comes with larger complexity.                   baseline. Besides, the cars which also contain polariza-
For efficiency-critical applications, the CMX solution with                     tion cues are completely and smoothly segmented with
MiT-B2 or -B4 would be preferred to enable both accurate                        delineated borders, and the boundaries ofpedestrians also
and efficient multi-modal semantic scene perception.                            show beneficial effects.
                                                                            (4) For RGB-Event, our CMX generalizes well and enhances
H. Qualitative Analysis                                                         the segmentation of moving objects, such as the seg-
Visualization of segmentation results. We compare the re-                       mentation results of cyclists and poles. It indicates that
sults of the RGB-only baseline and our CMX, where both are                      incorporating features extracted from Event data can
based on SegFormer-B2. We analyze each row from top to                          enhance the modeling of dynamics that are not captured
bottom in Fig. 8.                                                               by RGB images alone.
 (1) For RGB-Depth, we present results from the NYU Depth                   (5) For RGB-LiDAR, thanks to the spatial information from
      V2 dataset [24]. CMX leverages geometric information                      the LiDAR modality, our CMX model can correctly
      and correctly identifies the bed while the model wrongly                  recognize the wall, while the RGB-only method misiden-
      classifies it as a sofa. It proves that the CMX model can                 tifies it as part of a truck. Furthermore, our CM-FRM
      obtain discriminative features from depth information in                  module makes CMX robust against the noise of LiDAR
      the low-texture scenario.                                                 modality, such as the truck glass area, yielding a complete
 (2) For RGB-Thermal, our CMX demonstrates improvement                          segmentation mask of the truck.
      over the baseline under low illumination conditions, e.g.,              Overall, the qualitative examination backs up that our gen-
      the night scene. The use of Thermal in addition to RGB               eral approach is suitable for a diverse mix of multi-modal
      enables the model to make much clearer boundaries, such              sensing combinations for robust semantic scene understanding.
      as between persons and unlabeled background. Besides,
      by combining features from both modalities, our CMX                                             VI. C ONCLUSION
      can more effectively filter out the noise and other un-                To revitalize multi-modal pixel-wise semantic scene un-
      wanted artifacts that can negatively impact segmentation             derstanding for autonomous vehicles, we investigate RGB-
      accuracy. For example, the segmentation of persons in                X semantic segmentation and propose CMX, a universal
                                                                                                                                            13

      (a) RGB input           (b) Modal X input        (c) RGB-only results         (d) RGB-X results                      (e) GT
Fig. 8: Visualization results of RGB-only and RGB-X methods, where both are based on the same backbone. From top to
bottom: RGB-Depth, RGB-Thermal, RGB-Polarization (AoLP), RGB-Event, and RGB-LiDAR semantic segmentation.

transformer-based cross-modal fusion architecture, which is                                    R EFERENCES
generalizable to a diverse mix of sensing data combina-
tions. We put forward a Cross-Modal Feature Rectification           [1] W. Zhou, J. S. Berrio, S. Worrall, and E. Nebot, “Automated evaluation
Module (CM-FRM) and a Feature Fusion Module (FFM)                       of semantic segmentation robustness for autonomous driving,” T-ITS,
                                                                        vol. 21, no. 5, pp. 1951–1963, 2020.
for facilitating interactions toward accurate RGB-X seman-          [2] K. Yang, X. Hu, Y. Fang, K. Wang, and R. Stiefelhagen, “Omnisuper-
tic segmentation. CM-FRM conducts channel- and spatial-                 vised omnidirectional semantic segmentation,” T-ITS, vol. 23, no. 2,
wise rectification, rendering comprehensive feature calibration.        pp. 1184–1199, 2022.
FFM intertwines cross-attention and mixed channel embedding         [3] L. Sun, K. Yang, X. Hu, W. Hu, and K. Wang, “Real-time fusion
                                                                        network for RGB-D semantic segmentation incorporating unexpected
for enhanced global information exchange. To further assess             obstacle detection for road-driving images,” RA-L, vol. 5, no. 4, pp.
the generalizability of CMX to dense-sparse data fusion, we             5558–5565, 2020.
establish an RGB-Event semantic segmentation benchmark.             [4] J. Zhang, K. Yang, A. Constantinescu, K. Peng, K. Müller, and
                                                                        R. Stiefelhagen, “Trans4Trans: Efficient transformer for transparent
We study effective representations of polarimetric- and event           object and semantic scene segmentation in real-world navigation as-
data, indicating the optimal path to follow for reaching robust         sistance,” T-ITS, vol. 23, no. 10, pp. 19 173–19 186, 2022.
multi-modal semantic segmentation. The proposed model sets          [5] L.-C. Chen, G. Papandreou, I. Kokkinos, K. Murphy, and A. L. Yuille,
                                                                        “DeepLab: Semantic image segmentation with deep convolutional nets,
the new state-of-the-art on nine benchmarks, spanning five              atrous convolution, and fully connected CRFs,” TPAMI, vol. 40, no. 4,
RGB-D datasets, as well as RGB-Thermal, RGB-Polarization,               pp. 834–848, 2018.
RGB-Event, and RGB-LiDAR combinations.                              [6] H. Zhao, J. Shi, X. Qi, X. Wang, and J. Jia, “Pyramid scene parsing
                                                                        network,” in CVPR, 2017.
                                                                    [7] J. Fu et al., “Dual attention network for scene segmentation,” in CVPR,
                                                                        2019.
                                                                    [8] X. Hu, K. Yang, L. Fei, and K. Wang, “ACNet: Attention based network
                                                                                                                                                            14

     to exploit complementary features for RGBD semantic segmentation,”          [39] H. Zhou, L. Qi, H. Huang, X. Yang, Z. Wan, and X. Wen, “CANet: Co-
     in ICIP, 2019.                                                                   attention network for RGB-D semantic segmentation,” PR, vol. 124, p.
 [9] X. Chen et al., “Bi-directional cross-modality feature propagation with          108468, 2022.
     separation-and-aggregation gate for RGB-D semantic segmentation,” in        [40] Y. Sun, W. Zuo, and M. Liu, “RTFNet: RGB-thermal fusion network
     ECCV, 2020.                                                                      for semantic segmentation of urban scenes,” RA-L, vol. 4, no. 3, pp.
[10] Q. Ha, K. Watanabe, T. Karasawa, Y. Ushiku, and T. Harada, “MFNet:               2576–2583, 2019.
     Towards real-time semantic segmentation for autonomous vehicles with        [41] Y. Sun, W. Zuo, P. Yun, H. Wang, and M. Liu, “FuseSeg: Semantic
     multi-spectral scenes,” in IROS, 2017.                                           segmentation of urban scenes based on RGB and thermal data fusion,”
[11] Q. Zhang, S. Zhao, Y. Luo, D. Zhang, N. Huang, and J. Han,                       T-ASE, vol. 18, no. 3, pp. 1000–1011, 2021.
     “ABMDRNet: Adaptive-weighted bi-directional modality difference             [42] W. Zhou, J. Liu, J. Lei, L. Yu, and J.-N. Hwang, “GMNet: Graded-
     reduction network for RGB-T semantic segmentation,” in CVPR, 2021.               feature multilabel-learning network for RGB-thermal urban scene se-
[12] K. Xiang, K. Yang, and K. Wang, “Polarization-driven semantic                    mantic segmentation,” TIP, vol. 30, pp. 7790–7802, 2021.
     segmentation via efficient attention-bridged fusion,” OE, vol. 29, no. 4,   [43] A. Kalra, V. Taamazyan, S. K. Rao, K. Venkataraman, R. Raskar, and
     pp. 4802–4820, 2021.                                                             A. Kadambi, “Deep polarization cues for transparent object segmenta-
[13] J. Zhang, K. Yang, and R. Stiefelhagen, “ISSAFE: Improving semantic              tion,” in CVPR, 2020.
     segmentation in accidents by fusing event-based data,” in IROS, 2021.       [44] J. Zhang, K. Yang, and R. Stiefelhagen, “Exploring event-driven
[14] Z. Zhuang, R. Li, K. Jia, Q. Wang, Y. Li, and M. Tan, “Perception-               dynamic context for accident scene segmentation,” T-ITS, vol. 23, no. 3,
     aware multi-sensor fusion for 3D LiDAR semantic segmentation,” in                pp. 2606–2622, 2022.
     ICCV, 2021.                                                                 [45] W. Wang and U. Neumann, “Depth-aware CNN for RGB-D segmen-
[15] J. Cao, H. Leng, D. Lischinski, D. Cohen-Or, C. Tu, and Y. Li,                   tation,” in ECCV, 2018.
     “ShapeConv: Shape-aware convolutional layer for indoor RGB-D se-            [46] Y. Xing, J. Wang, and G. Zeng, “Malleable 2.5D convolution: Learning
     mantic segmentation,” in ICCV, 2021.                                             receptive fields along the depth-axis for RGB-D scene parsing,” in
[16] L.-Z. Chen, Z. Lin, Z. Wang, Y.-L. Yang, and M.-M. Cheng, “Spatial               ECCV, 2020.
     information guided convolution for real-time RGBD semantic segmen-          [47] Z. Wu, G. Allibert, C. Stolz, and C. Demonceaux, “Depth-adapted
     tation,” TIP, vol. 30, pp. 2313–2324, 2021.                                      CNN for RGB-D cameras,” in ACCV, 2020.
[17] F. Deng et al., “FEANet: Feature-enhanced attention network for RGB-        [48] Z. Zhang, Z. Cui, C. Xu, Y. Yan, N. Sebe, and J. Yang, “Pattern-
     thermal real-time semantic segmentation,” in IROS, 2021.                         affinitive propagation across depth, surface normal and semantic seg-
[18] D. Sun, X. Huang, and K. Yang, “A multimodal vision sensor for                   mentation,” in CVPR, 2019.
     autonomous driving,” in SPIE, 2019.                                         [49] R. Bachmann, D. Mizrahi, A. Atanov, and A. Zamir, “MultiMAE:
[19] R. Girdhar, M. Singh, N. Ravi, L. van der Maaten, A. Joulin, and                 Multi-modal multi-task masked autoencoders,” in ECCV, 2022.
     I. Misra, “Omnivore: A single model for many visual modalities,” in         [50] P. Zhang, W. Liu, Y. Lei, and H. Lu, “Hyperfusion-net: Hyper-densely
     CVPR, 2022.                                                                      reflective feature fusion for salient object detection,” PR, vol. 93, pp.
[20] A. Vaswani et al., “Attention is all you need,” in NeurIPS, 2017.                521–533, 2019.
[21] A. Dosovitskiy et al., “An image is worth 16x16 words: Transformers         [51] Y. Pang, X. Zhao, L. Zhang, and H. Lu, “CAVER: Cross-modal view-
     for image recognition at scale,” in ICLR, 2021.                                  mixed transformer for bi-modal salient object detection,” TIP, 2023.
                                                                                 [52] L. Chen et al., “SCA-CNN: Spatial and channel-wise attention in
[22] H. Touvron, M. Cord, M. Douze, F. Massa, A. Sablayrolles, and
                                                                                      convolutional networks for image captioning,” in CVPR, 2017.
     H. Jégou, “Training data-efficient image transformers & distillation
                                                                                 [53] Z. Shen, M. Zhang, H. Zhao, S. Yi, and H. Li, “Efficient attention:
     through attention,” in ICML, 2021.
                                                                                      Attention with linear complexities,” in WACV, 2021.
[23] Z. Liu et al., “Swin transformer: Hierarchical vision transformer using
                                                                                 [54] J. Li, A. Hassani, S. Walton, and H. Shi, “ConvMLP: hierarchical
     shifted windows,” in ICCV, 2021.
                                                                                      convolutional MLPs for vision,” arXiv preprint arXiv:2109.04454,
[24] N. Silberman, D. Hoiem, P. Kohli, and R. Fergus, “Indoor segmentation
                                                                                      2021.
     and support inference from RGBD images,” in ECCV, 2012.
                                                                                 [55] S. Gupta, R. Girshick, P. Arbeláez, and J. Malik, “Learning rich features
[25] Y. Liao, J. Xie, and A. Geiger, “KITTI-360: A novel dataset and                  from RGB-D images for object detection and segmentation,” in ECCV,
     benchmarks for urban scene understanding in 2D and 3D,” TPAMI,                   2014.
     vol. 45, no. 3, pp. 3292–3310, 2023.                                        [56] R. Yan, K. Yang, and K. Wang, “NLFNet: Non-local fusion towards
[26] D. Gehrig, M. Rüegg, M. Gehrig, J. Hidalgo-Carrió, and D. Scara-                 generalized multimodal semantic segmentation across RGB-depth, po-
     muzza, “Combining events and frames using recurrent asynchronous                 larization, and thermal images,” in ROBIO, 2021.
     multimodal networks for monocular depth prediction,” RA-L, vol. 6,          [57] I. Alonso and A. C. Murillo, “EV-SegNet: Semantic segmentation for
     no. 2, pp. 2822–2829, 2021.                                                      event-based cameras,” in CVPRW, 2019.
[27] W. Wang, T. Zhou, F. Yu, J. Dai, E. Konukoglu, and L. Van Gool,             [58] E. Mohammadbagher, N. P. Bhatt, E. Hashemi, B. Fidan, and A. Kha-
     “Exploring cross-image pixel contrast for semantic segmentation,”                jepour, “Real-time pedestrian localization and state estimation using
     ICCV, 2021.                                                                      moving horizon estimation,” in ITSC, 2020.
[28] T. Zhou, W. Wang, E. Konukoglu, and L. Van Gool, “Rethinking                [59] S. Song, S. P. Lichtenberg, and J. Xiao, “SUN RGB-D: A RGB-D
     semantic segmentation: A prototype view,” in CVPR, 2022.                         scene understanding benchmark suite,” in CVPR, 2015.
[29] X. Wang, R. Girshick, A. Gupta, and K. He, “Non-local neural                [60] G. Zhang, J.-H. Xue, P. Xie, S. Yang, and G. Wang, “Non-local
     networks,” in CVPR, 2018.                                                        aggregation for RGB-D semantic segmentation,” SPL, vol. 28, pp. 658–
[30] Z. Huang, X. Wang, L. Huang, C. Huang, Y. Wei, and W. Liu, “CCNet:               662, 2021.
     Criss-cross attention for semantic segmentation,” in ICCV, 2019.            [61] I. Armeni, S. Sax, A. R. Zamir, and S. Savarese, “Joint 2D-3D-semantic
[31] S. Zheng et al., “Rethinking semantic segmentation from a sequence-              data for indoor scene understanding,” arXiv preprint arXiv:1702.01105,
     to-sequence perspective with transformers,” in CVPR, 2021.                       2017.
[32] R. Strudel, R. Garcia, I. Laptev, and C. Schmid, “Segmenter: Trans-         [62] A. Dai, A. X. Chang, M. Savva, M. Halber, T. Funkhouser, and
     former for semantic segmentation,” in ICCV, 2021.                                M. Nießner, “ScanNet: Richly-annotated 3D reconstructions of indoor
[33] E. Xie, W. Wang, Z. Yu, A. Anandkumar, J. M. Alvarez, and P. Luo,                scenes,” in CVPR, 2017.
     “SegFormer: Simple and efficient design for semantic segmentation           [63] M. Cordts et al., “The cityscapes dataset for semantic urban scene
     with transformers,” in NeurIPS, 2021.                                            understanding,” in CVPR, 2016.
[34] W. Wang et al., “Pyramid vision transformer: A versatile backbone for       [64] A. Dosovitskiy, G. Ros, F. Codevilla, A. Lopez, and V. Koltun,
     dense prediction without convolutions,” in ICCV, 2021.                           “CARLA: An open urban driving simulator,” in CoRL, 2017.
[35] Y. Yuan et al., “HRFormer: High-resolution transformer for dense            [65] Z. Sun, N. Messikommer, D. Gehrig, and D. Scaramuzza, “ESS:
     prediction,” in NeurIPS, 2021.                                                   Learning event-based semantic segmentation from still images,” in
[36] Y. Zhang, B. Pang, and C. Lu, “Semantic segmentation by early region             ECCV, 2022.
     proxy,” in CVPR, 2022.                                                      [66] O. Russakovsky et al., “ImageNet large scale visual recognition chal-
[37] F. Lin, Z. Liang, J. He, M. Zheng, S. Tian, and K. Chen, “StructToken :          lenge,” IJCV, vol. 115, no. 3, pp. 211–252, 2015.
     Rethinking semantic segmentation with structural prior,” TCSVT, 2023.       [67] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,”
[38] Y. Qian, L. Deng, T. Li, C. Wang, and M. Yang, “Gated-residual block             in ICLR, 2015.
     for semantic segmentation using RGB-D data,” T-ITS, vol. 23, no. 8,         [68] X. Qi, R. Liao, J. Jia, S. Fidler, and R. Urtasun, “3D graph neural
     pp. 11 836–11 844, 2022.                                                         networks for RGBD semantic segmentation,” in ICCV, 2017.
                                                                                                                                                           15

[69] S. Kong and C. C. Fowlkes, “Recurrent scene parsing with perspective        [97] R. P. K. Poudel, S. Liwicki, and R. Cipolla, “Fast-SCNN: Fast semantic
     understanding in the loop,” in CVPR, 2018.                                       segmentation network,” in BMVC, 2019.
[70] Y. Cheng, R. Cai, Z. Li, X. Zhao, and K. Huang, “Locality-sensitive         [98] T. Wu, S. Tang, R. Zhang, and Y. Zhang, “CGNet: A light-weight
     deconvolution networks with gated fusion for RGB-D indoor semantic               context guided network for semantic segmentation,” TIP, vol. 30, pp.
     segmentation,” in CVPR, 2017.                                                    1169–1179, 2021.
[71] D. Lin, G. Chen, D. Cohen-Or, P.-A. Heng, and H. Huang, “Cascaded           [99] J. Zhang, K. Yang, A. Constantinescu, K. Peng, K. Müller, and
     feature network for semantic segmentation of RGB-D images,” in                   R. Stiefelhagen, “Trans4Trans: Efficient transformer for transparent
     ICCV, 2017.                                                                      object segmentation to help visually impaired people navigate in the
[72] S.-J. Park, K.-S. Hong, and S. Lee, “RDFNet: RGB-D multi-level                   real world,” in ICCVW, 2021.
     residual feature fusion for indoor semantic segmentation,” in ICCV,        [100] L.-C. Chen, Y. Zhu, G. Papandreou, F. Schroff, and H. Adam,
     2017.                                                                            “Encoder-decoder with atrous separable convolution for semantic im-
[73] F. Fooladgar and S. Kasaei, “Multi-modal attention-based fusion model            age segmentation,” in ECCV, 2018.
     for semantic segmentation of RGB-depth images,” arXiv preprint             [101] T. Xiao, Y. Liu, B. Zhou, Y. Jiang, and J. Sun, “Unified perceptual
     arXiv:1912.11691, 2019.                                                          parsing for scene understanding,” in ECCV, 2018.
[74] Y. Yue, W. Zhou, J. Lei, and L. Yu, “Two-stage cascaded decoder for        [102] T. Broedermann, C. Sakaridis, D. Dai, and L. Van Gool, “HRFuser: A
     semantic segmentation of RGB-D images,” SPL, vol. 28, pp. 1115–                  multi-resolution sensor fusion architecture for 2D object detection,” in
     1119, 2021.                                                                      ITSC, 2023.
[75] A. Valada, R. Mohan, and W. Burgard, “Self-supervised model adap-          [103] Y. Wang, X. Chen, L. Cao, W. Huang, F. Sun, and Y. Wang, “Multi-
     tation for multimodal semantic segmentation,” IJCV, vol. 128, no. 5,             modal token fusion for vision transformers,” in CVPR, 2022.
     pp. 1239–1285, 2019.                                                       [104] A. Prakash, K. Chitta, and A. Geiger, “Multi-modal fusion transformer
[76] A. Dai and M. Nießner, “3DMV: Joint 3D-multi-view prediction for                 for end-to-end autonomous driving,” in CVPR, 2021.
     3D semantic scene segmentation,” in ECCV, 2018.
[77] C. Hazirbas, L. Ma, C. Domokos, and D. Cremers, “FuseNet: In-
     corporating depth into semantic segmentation via fusion-based CNN
     architecture,” in ACCV, 2016.
[78] W. Shi et al., “Multilevel cross-aware RGBD indoor semantic segmen-
     tation for bionic binocular robot,” T-MRB, vol. 2, no. 3, pp. 382–390,
     2020.
[79] W. Shi et al., “RGB-D semantic segmentation and label-oriented
     voxelgrid fusion for accurate 3D semantic mapping,” TCSVT, vol. 32,
     no. 1, pp. 183–197, 2022.
[80] M. Orsic, I. Kreso, P. Bevandic, and S. Segvic, “In defense of pre-
     trained ImageNet architectures for real-time semantic segmentation of
     road-driving images,” in CVPR, 2019.
[81] D. Seichter, M. Köhler, B. Lewandowski, T. Wengefeld, and H.-
     M. Gross, “Efficient RGB-D semantic segmentation for indoor scene
     analysis,” in ICRA, 2021.
[82] T. Takikawa, D. Acuna, V. Jampani, and S. Fidler, “Gated-SCNN:
     Gated shape CNNs for semantic segmentation,” in ICCV, 2019.
[83] F. Zhang et al., “ACFNet: Attentional class feature network for
     semantic segmentation,” in ICCV, 2019.
[84] D. Xu, W. Ouyang, X. Wang, and N. Sebe, “PAD-net: Multi-tasks
     guided prediction-and-distillation network for simultaneous depth esti-
     mation and scene parsing,” in CVPR, 2018.
[85] Y. Wang, F. Sun, M. Lu, and A. Yao, “Learning deep multimodal
     feature representation with asymmetric multi-layer fusion,” in MM,
     2020.
[86] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
     recognition,” in CVPR, 2016.
[87] X. Zhang, S. Zhang, Z. Cui, Z. Li, J. Xie, and J. Yang, “Tube-embedded
     transformer for pixel prediction,” TMM, vol. 25, pp. 2503–2514, 2023.
[88] W. Hu, H. Zhao, L. Jiang, J. Jia, and T.-T. Wong, “Bidirectional
     projection network for cross dimension scene understanding,” in CVPR,
     2021.
[89] E. Romera, J. M. Alvarez, L. M. Bergasa, and R. Arroyo, “ERFNet:
     Efficient residual factorized ConvNet for real-time semantic segmenta-
     tion,” T-ITS, vol. 19, no. 1, pp. 263–272, 2018.
[90] J. Wang et al., “Deep high-resolution representation learning for visual
     recognition,” TPAMI, vol. 43, no. 10, pp. 3349–3364, 2021.
[91] S. S. Shivakumar, N. Rodrigues, A. Zhou, I. D. Miller, V. Kumar,
     and C. J. Taylor, “PST900: RGB-thermal calibration, dataset and
     segmentation network,” in ICRA, 2020.
[92] J. Xu, K. Lu, and H. Wang, “Attention fusion network for multi-spectral
     semantic segmentation,” PRL, vol. 146, pp. 179–184, 2021.
[93] Y. Cai, W. Zhou, L. Zhang, L. Yu, and T. Luo, “DHFNet: Dual-
     decoding hierarchical fusion network for RGB-thermal semantic seg-
     mentation,” The Visual Computer, pp. 1–11, 2023.
[94] T. Pohlen, A. Hermans, M. Mathias, and B. Leibe, “Full-resolution
     residual networks for semantic segmentation in street scenes,” in CVPR,
     2017.
[95] C. Yu, J. Wang, C. Peng, C. Gao, G. Yu, and N. Sang, “Learning a
     discriminative feature network for semantic segmentation,” in CVPR,
     2018.
[96] C. Yu, J. Wang, C. Peng, C. Gao, G. Yu, and N. Sang, “BiSeNet:
     Bilateral segmentation network for real-time semantic segmentation,”
     in ECCV, 2018.
                                                                                                                                16

                       A PPENDIX A                                the Cityscapes dataset based on the backbone of SegFormer-
             M ORE I MPLEMENTATION D ETAILS                       B4. We show the results of the RGB-only baseline and our
   We implement our experiments with PyTorch. We employ a         RGB-X approach, in particular, the difference maps w.r.t. the
poly learning rate schedule with a factor of 0.9 and an initial   segmentation ground truth. As displayed in Fig. A.1, in spite
learning rate of 6e−5 . The number of warm-up epochs is 10.       of the noisy depth measurements, our CMX still benefits from
We now describe implementation details for different datasets.    the HHA-encoded image, thanks to the ability to rectify and
NYU Depth V2 dataset. We train our model with the MiT-            fuse cross-modal complementary features. Our approach has
B2 backbone on four 2080Ti GPUs, models with MiT-B4               higher pixel accuracy scores on a wide variety of driving scene
and MiT-B5 backbones on three 3090 GPUs. The number of            elements such as fence, and sidewalk in the positive group (in
training epochs is set as 500. We take the whole image with       green boxes). However, the shadows and weak illumination
the size 640×480 for training and inference. We use a batch       conditions are still challenging for both models and make the
size of 8 for the MiT-B2 backbone and 6 for MiT-B4 and -B5.       depth cues less effective. For example, depth information in
SUN-RGBD dataset. The models are trained with a batch             the regions of sidewalk in the negative group (in red boxes),
size of 4 per GPU. During training, the images are randomly       may be less informative for fusion.
cropped to 480×480. The model based on MiT-B2 is trained          Failure case analysis. In Fig. A.2, we show a set of failure
on two V100 GPUs for 200 epochs. The models based on              cases in different sensing modality combination scenarios. The
MiT-B4 and MiT-B5 are trained on eight V100 GPUs, 250             first row shows that for the RGB-D semantic segmentation
epochs for MiT-B4 and 300 epochs for MiT-B5.                      in a highly composite indoor scene with extremely densely
Stanford2D3D dataset. The model is trained on four 2080Ti         arranged objects, the parsing results are still less visually
GPUs. The number of training epochs here is set as 32. We         satisfactory. In the second row of a nighttime scene, the
resize the input images to 480×480. We use a batch size of        guardrails are misclassified by the RGB-X method as color
12 for the MiT-B2 backbone and 8 for MiT-B4.                      cone, despite our model delivering more complete and con-
ScanNetV2 dataset. The model is trained on four 2080Ti            sistent segmentation than the RGB-only model and having
GPUs. The number of training epochs here is set as 100. We        better segmentation of person with thermal properties. This
resize the input RGB images to 640×480. We use a batch size       illustrates that at night, the perception of some remote objects
of 12 for the MiT-B2 backbone.                                    is still challenging in RGB-T semantic segmentation and it
Cityscapes dataset. The model is trained on eight A100 GPUs       should be noted for safety-critical applications like automated
for 500 epochs. The batch size is set as 8. The images are        driving. In the third row, the RGB-P model might be misguided
randomly cropped into 1024×1024 for training and inference        by the polarized background area in an occluded situation and
is performed on the full resolution with a sliding window of      yields less accurate parsing results, indicating that polariza-
512×512. The embedding dimension of the MiT-B4 backbone           tion, as a strong prior for segmentation of specular surfaces
and MLP-decoder is set as 768.                                    like glass and car regions, should be carefully leveraged in
RGB-T MFNet dataset. The model is trained on four 2080Ti          unconstrained scenes with a lot of occlusions. In the fourth
GPUs. We use the original image size of 640×480 for training      row, the fences are partially detected as vehicles in the RGB-
and inference. The batch size is set to 8 for the MiT-B2          E segmentation result, but our model still yields more correctly
backbone and we train for 500 epochs. Consistent with the         identified pixels than the RGB-only model by harvesting
batch size of 8, the model based on MiT-B4 is trained on four     complementary cues from event data. In the last row, the over-
A100 GPUs, which requires a larger memory.                        exposed sidewalk region is still a challenge for segmentation.
                                                                  Nonetheless, our RGB-LiDAR CMX predicts a much better
RGB-P ZJU dataset. The model is trained on four 2080Ti
                                                                  mask on the fence region, where the spatial information given
GPUs. We resize the image from 1224×1024 to 612×512. The
number of training epochs is set as 400. We use a batch size of   by LiDAR data is more accurate.
                                                                  Feature analysis. To understand the key module for feature
8 for the MiT-B2 backbone and 4 for MiT-B4. In practice, we
                                                                  rectification, we visualize the input- and rectified features of
calculate the image encoding pixel-wise AoLP information by
                                                                  CM-FRM in layer 1, and their difference map, as shown
mapping the values of arctan(S1 /S2 ) to the range of [0, 255].
                                                                  in Fig. B.1. It can be seen that the feature maps are en-
RGB-E EventScape dataset. The proposed model is trained
                                                                  hanced in both streams after the cross-modal calibration. The
with a batch size of 4 and the original resolution of 512×256
                                                                  RGB stream delivers texture information to the supplement
on a single 1080Ti GPU. The number of training epochs is set
                                                                  modality, while the supplement modality further improves
as 100. The embedding dimension of the MiT-B4 backbone
                                                                  the boundary and emphasizes complementary discontinuities
and MLP-decoder is set as 768.
                                                                  of RGB features. In the RGB-D segmentation scenario, the
RGB-L KITTI-360 dataset. The model is trained with a batch
                                                                  RGB-feature difference map shows that the ground area is
size of 2 and the original resolution of 1408×376. The number
                                                                  better spotlighted, thanks to the HHA image encoding depth
of training epochs is set as 40.
                                                                  information, which provides geometric cues such as height
                                                                  above ground, beneficial for higher-level semantic prediction
                      A PPENDIX B                                 of ground-related classes. In the RGB-T nighttime scene
              M ORE Q UALITATIVE A NALYSIS                        parsing cases, the pedestrians are hard to be seen in the RGB
Segmentation results on the Cityscapes dataset. We further        images. But the RGB-feature difference map clearly highlights
view the outdoor RGB-D semantic segmentation results on           the pedestrians thanks to the supplementary thermal modality
                                                                                                                          17

          RGB              Baseline difference map         HHA                Our difference map              GT
                         Acc=66.09%                                       Acc=66.62%

                         Acc=78.04%                                       Acc=79.57%

                         Acc=83.25%                                       Acc=81.02%

Fig. A.1: Visualization of semantic segmentation results for the RGB-only baseline and our RGB-X approach, both of which
are based on SegFormer-B4. “Acc” is short for pixel accuracy of the segmentation result. From left to right: RGB image,
baseline difference map w.r.t. the ground truth, HHA image encoding depth information, our difference map, and ground truth.

   a) RGB Input              b) Modal X              c) RGB results          d) RGB-X results               e) GT

Fig. A.2: Visualization of failure cases. We use SegFormer-B2 for RGB segmentation and the proposed approach with the
same backbone MiT-B2 and MLP-Decoder for RGB-X segmentation. From top to bottom: RGB-Depth, RGB-Thermal, RGB-
Polarization (AoLP), and RGB-Event semantic segmentation.
                                                                                                                            18

 RGB

 HHA

 RGB

   T

                        Before Rec.     After Rec.    Difference                    Before Rec.     After Rec.     Difference

        Fig. B.1: Visualization of the feature extracted in layer 1 and the rectified feature, and their difference map.

with infrared imaging. These indicate that the complementary
features have been infused into the RGB stream. The RGB
features have been rectified to better focus on informative
ones and capture such complementary discontinuities towards
accurate semantic understanding.
