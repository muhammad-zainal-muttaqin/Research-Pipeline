---
source_id: 196
bibtex_key: yi2025gldmnet
title: Dual Mutual Learning Network with Global-local Awareness for RGB-D Salient Object Detection
year: 2025
domain_theme: RGB-D SOD
verified_pdf: 196_GL-DMNet Dual Mutual Learning RGB-D SOD.pdf
char_count: 100444
---

SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                                          1

                                           Dual Mutual Learning Network with Global–local
                                            Awareness for RGB-D Salient Object Detection
                                                                                Kang Yi, Haoran Tang, Yumeng Li, Jing Xu, Jun Zhang

                                           Abstract—RGB-D salient object detection (SOD), aiming to
                                        highlight prominent regions of a given scene by jointly modeling
                                        RGB and depth information, is one of the challenging pixel-
                                        level prediction tasks. Recently, the dual-attention mechanism
                                        has been devoted to this area due to its ability to strengthen the
arXiv:2501.01648v1 [cs.CV] 3 Jan 2025

                                        detection process. However, most existing methods directly fuse
                                        attentional cross-modality features under a manual-mandatory
                                        fusion paradigm without considering the inherent discrepancy
                                        between the RGB and depth, which may lead to a reduction
                                        in performance. Moreover, the long-range dependencies derived
                                        from global and local information make it difficult to leverage a
                                        unified efficient fusion strategy. Hence, in this paper, we propose
                                        the GL-DMNet, a novel dual mutual learning network with
                                        global-local awareness. Specifically, we present a position mutual
                                        fusion module and a channel mutual fusion module to exploit
                                        the interdependencies among different modalities in spatial and
                                        channel dimensions. Besides, we adopt an efficient decoder
                                        based on cascade transformer-infused reconstruction to integrate
                                        multi-level fusion features jointly. Extensive experiments on six                Fig. 1. The results of our GL-DMNet and other representative methods,
                                                                                                                         including CATNet [8], HiDANet [9] and TriTransNet [10].
                                        benchmark datasets demonstrate that our proposed GL-DMNet
                                        performs better than 24 RGB-D SOD methods, achieving an
                                        average improvement of ∼3% across four evaluation metrics
                                        compared to the second-best model (S3Net). Codes and results                        The idea of dual attention is to model the long-range
                                        are available at https://github.com/kingkung2016/GL-DMNet.
                                                                                                                         contextual dependencies by dual attention modules [7], e.g.,
                                          Index Terms—RGB-D, salient object detection, dual attention,                   position and channel attentions. Consequently, it exploits more
                                        Transformer, cross-modality learning.                                            detailed semantic information from the high-level features of
                                                                                                                         RGB images and depth images and enhances them in turn [8],
                                                                  I. I NTRODUCTION                                       [11]. However, previous methods directly integrate different
                                                                                                                         attention modules under the manual-mandatory fusion strat-
                                             ALIENT object detection (SOD) is one of the most
                                        S    fundamental yet challenging problems in computer vision,
                                        whose goal is to locate the most visually attractive objects or
                                                                                                                         egy to conduct multi-modal feature learning, neglecting the
                                                                                                                         inherent discrepancy (e.g., semantic content) between the RGB
                                                                                                                         and the depth [12]. As a result, most of them may need more
                                        regions of a given scene [1], [2]. It has been successfully
                                                                                                                         flexibility in multi-modal feature fusion, which further limits
                                        applied in various fields, such as autonomous driving [3],
                                                                                                                         performance improvement. Hence, efficiently investigating and
                                        person identification [4], image editing [5], and medical image
                                                                                                                         combining multi-modal information becomes an urgent issue
                                        understanding [6]. Nevertheless, the conventional methods
                                                                                                                         for the RGB-D SOD task.
                                        for SOD task face difficulties when handling complex and
                                        indistinguishable scenarios, causing suboptimal performance.                        Another issue occurring in RGB-D SOD is the deficiency
                                        Especially in the real world, there is rich RGB and depth                        of collaborative effect between local correlation and global
                                        information (RGB-D). Recently, the study on dual attention                       correlation for each pixel [10]. Especially for multi-modal
                                        mechanism, which could effectively capture feature depen-                        learning, the RGB and depth features would pose more long-
                                        dencies in the spatial and channel dimensions [7], provides                      range dependencies [13], [14], making it hard for the RGB and
                                        a new opportunity to this area. Thus, it is possible to improve                  depth features to complement each other. As a consequence,
                                        the performance of RGB-D SOD across different scenarios                          the perception of global-local awareness may be destroyed
                                        without constraints.                                                             passively. Thus, sufficiently capturing cross-modality global-
                                                                                                                         local context is another challenge that needs to be solved.
                                           This work is supported by the National Natural Science Foundation of             To tackle the above issues, we propose a novel model,
                                        China (Grant No. 62233011), Tianjin Natural Science Foundation, China
                                        (Grant No. 21JCYBJC00110). (Kang Yi and Haoran Tang contributed equally          the dual mutual learning network with global-local awareness
                                        to this work.) (Corresponding author: Jing Xu.)                                  (GL-DMNet) for the RGB-D SOD task. Firstly, to fully
                                           Yi Kang, Yumeng Li, Jing Xu and Jun Zhang are with the College of             investigate the features of RGB and depth information, we
                                        Artificial Intelligence, Nankai University, Tianjin 300350, China. Haoran Tang
                                        is with the Department of Computing, The Hong Kong Polytechnic University,       incorporate the dual attention mechanism into cross-modality
                                        Kowloon, Hong Kong.                                                              learning, which naturally connects different local features and
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                                    2

adaptively integrates local features with their global depen-                   Moreover, we have no shared parameters between stages. This
dencies. By applying the dual attention mechanism, our model                    helps us to explore the discriminative features for each stage.
could learn cross-modality features at any scale from a global                  Therefore, compared with TriTransNet and GroupTransNet,
view. In other words, we endow our framework with the                           we leverage fewer parameters, consume less cost, and gain
capabilities of local and global learning. As a result, we would                better performance, which significantly distinguishes our work
obtain multi-scale complementary information, and then we                       from previous studies. Furthermore, extensive experiments are
can devise multi-modal context enhancement to improve the                       conducted on six benchmark datasets, and the results indicate
quality of the SOD task. Secondly, we design an interactive                     that the proposed model achieves competitive performance
manner by constructing a joint transformer-based and CNN-                       against 24 RGB-D SOD methods.
based encoder. This innovation allows us to globally capture                       In summary, the main contributions of this paper can be
the correlation between different stages, further mitigating the                described as follows:
previously-mentioned issues. Last, we leverage an efficient                        • We present a dual mutual learning network with global-
decode strategy that follows the transformed-infused recon-                          local awareness (GL-DMNet) for the RGB-D SOD,
struction to accurately conduct our final SOD predictions and                        which constructs a joint transformer-based and CNN-
also free the whole model from heavy fusion learning.                                based network to extract features from RGB images and
                                                                                     depth inputs.
                                                                                   • To fully exploit the global-local dependencies between
                                                                                     two modalities, we design a position mutual fusion (PMF)
                                                                                     module and a channel mutual fusion (CMF) module for
                                                                                     cross-modality fusion.
                                                                                   • We also develop a cascade transformer-infused recon-
                                                                                     struction (CTR) decoder to augment the global-local
                                                                                     awareness of multi-level fusion features.
                                                                                   • The proposed method is evaluated on six publicly avail-
                                                                                     able datasets under four widely used metrics. Compared
                                                                                     with 24 state-of-the-art approaches, GL-DMNet achieves
                                                                                     superior performance.

                                                                                                     II. R ELATED WORK
                                                                                A. RGB-D salient object detection
                                                                                   Early RGB-D SOD methods usually design handcrafted
                                                                                features and various fusion strategies to integrate RGB and
                                                                                depth cues. Following this direction, numerous models have
                                                                                been proposed to detect salient objects [19]–[21]. However,
                                                                                they merely regard the depth stream as auxiliary information,
Fig. 2. Comparison between (a) FPN framework, (b) dense decode network,         which results in unsatisfactory performance.
(c) group transformer network, (d) visual transformer FPN, (e) triplet trans-      With the rapid development of deep learning, CNN-based
former embedding network, and our (f) transformer-infused reconstruction
network.                                                                        methods have achieved remarkable progress [1], [22]. Wang
                                                                                et al. [23] introduce a depth decomposition and recomposition
   Fig. 1 shows a part of comparisons between our model and                     module to filter out low-quality depth maps and enhance
other representative methods, including CATNet, HiDANet                         the quality of detrimental depth maps. Zhang et al. [24]
and TriTransNet. Our model delivers a better result for the                     present a two-stage model, including an image generation
RGB-D SOD task. Also, in Fig. 2, we illustrate the framework                    stage that produces pseudo-depth images from RGB inputs
difference between our model and the feature pyramid network                    and a saliency reasoning stage that calibrates original depth
(FPN) [15], dense decoding network [16], group transformer                      images with pseudo-depth images and performs cross-modal
network (GroupTransNet) [17], visual transformer FPN [18],                      feature fusion. Zeng et al. [14] introduce a lightweight RGB-
and triplet transformer embedding network (TriTransNet) [10].                   D saliency method named AirSOD, which incorporates a
The traditional models feature pyramid network and dense                        parameter-free parallel attention-shift convolution, multi-level
decoding network, only leverage the simplest decoder without                    multi-modal feature fusion, and multi-path enhancement to
transformer, leading to the worst performance. Our proposed                     achieve a favorable balance between efficiency and perfor-
model, however, divides the transformer into four stages, each                  mance. Xiao et al. [25] construct a depth-guided fusion module
of which can be fed into the decoder separately and indepen-                    to enhance the fusion of RGB and depth features, emphasizing
dently. Hence, such parallelization in our model can speed up                   attention and weighting mechanisms to augment spatial repre-
the whole learning process. On the contrary, the recent ad-                     sentations in saliency regions and effectively reducing the gap
vanced models that leverage transformer, such as TriTransNet                    between modalities. Cheng et al. [26] propose a depth-induced
and GroupTransNet, are designed to repeatedly execute trans-                    gap-reducing network that utilizes cross-modality interaction
former multiple times, leading to high computation costs.                       blocks and interference degree mechanisms in two branches
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                      3

for effective cross-modality feature fusion and refinement        et al. [36] propose a cross-modality point-aware interaction
while mitigating unexpected noise. Sun et al. [8] designed        module to simplify the process by grouping corresponding
a Cascaded and Aggregated Transformer Network (CATNet)            point features from different modalities, thereby addressing
to establish connections between features of different scales     the cross-modality feature interaction challenge in transformer-
to prevent information loss and redundancy. Li et al. [27]        based models. Wang et al. [37] construct a novel and uni-
employed a dynamic searching process module and a dual-           fied transformer-based structure to globally fuse multi-scale
branch consistency learning mechanism to address the weak         multi-modal features and enhance features from the same
richness of pixel training samples (WRPS) and the poor            modality. Gao et al. [38] propose a novel token sparsification
structural integrity of salient objects (PSIO) and proposed an    transformer framework, dynamically sparsifying tokens and
edge-region structure-refinement loss for precise segmentation.   extracting global-local multi-modality features based on the
Zhong et al. [28] utilized a Multi-scale Awareness Fusion         most informative tokens. Liu et al. [10] introduce a triplet
Module (MAFM) for low-level features and a Global Fusion          transformer scheme called TritransNet that shares parameters
Module (GFM) for high-level features, thereby enriching low-      among different stages, to model the long-range correlation
level information while performing a global analysis of multi-    between them globally. TritransNet servers as a supplementary
modal semantic information.                                       encoding strategy for feature fusion, which also inspires our
   Despite the success existing methods have achieved, they       work. Nonetheless, the utilization of sharing parameters cannot
still face some limitations which hinder further improvement      capture the discriminate features of each stage. Meanwhile,
in the area of RGB-D SOD. First, most of them focus on            executing the large parameters from the global view would be
handling low-quality images to strengthen the information         time-consuming for each stage. This motivates us to design an
expressiveness and thus mitigate the noise caused by low qual-    independent encoder for each stage while leveraging a global-
ity. However, they ignore the inherent discrepancy between        aware strategy to protect the correlation among stages. Wu et
different modalities (i.e., RGB and depth modalities), which      al. [39] propose a transformer-based fusion method with pixel-
cannot be solved by only improving the quality of images.         level contrastive learning to explore the potential correlation
Second, there is a natural trade-off between the RGB and depth    between the inter and intra-pixel interactions over modalities.
information. Sometimes depth delivers more significance to        Its core lies in the attention mechanism for cross-modality
the SOD task than RGB information, while sometimes RGB            fusion. However, the large number of its CIPT modules leads
information could play a more leading role [29]. Therefore, our   to a severe overload of fusion strategies, which affects the
scenario’s core research question is how to efficiently utilize   efficiency of the whole model learning.
them together and achieve a double-win balance. Moreover,            Encouraged by the promising results from TriTransNet [10],
the features learned during each stage affect global learning     we attempted to further enhance the feature representation
differently. Unfortunately, most existing methods integrate       ability of multi-modal integrated features by employing the
them without identifying their global awareness, making sys-      transformer-based architecture, aiming to achieve the interac-
tem performance suboptimal. The mentioned issues encourage        tion and fusion of long-distance information across stages.
our work in this paper.
   On the one hand, we aim to model the inherent discrepancy
                                                                  C. Attention mechanism
across modalities by leveraging PMF and CMF. We seek to
learn the relevance between modalities and achieve better            In various vision tasks, attention mechanisms are fully
trade-offs. On the other hand, we aim to explore the local-       exploited to focus on the pivotal information in the image,
global awareness of each stage’s learned features to ensure       and have been proven to be an indispensable means for
their accurate contributions to the SOD prediction. We hope       performance improvement, such as convolutional block [40],
our work could deliver an improvement to existing methods         selective kernel block [41], strip pooling block [42], and
for the RGB-D SOD task and provide some innovations for           coordinate attentions [43].
other researchers in this area.                                      When being applied to RGB-D SOD, the above attention
                                                                  mechanisms enable the encoder to flexibly discern subtle
                                                                  differences between modalities, which provides an opportu-
B. Vision Transformer                                             nity for further exploration. Also, they aim to deepen the
   Transformer is initially proposed to address the limitations   integration of distinct modal features and exploit complemen-
of recurrent and convolutional neural networks in handling        tary information more effectively. Liu et al. [44] leverage
sequential data [30]. The unique ability to handle long-range     cross-modal attention propagation, which contains a contrast
dependencies and high parallelization make it a versatile         inference and incorporates a selective attention mechanism
architecture and has been applied to various domains within       to address the challenges posed by low-quality depth data.
the field of computer science [31]–[33]. The transformer-based    Feng et al. [45] propose a cross-modal mutual guidance
models also open up new directions in RGB-D SOD. Liu              module to model the interdependencies between channels to
et al. [34] design a pure transformer framework that utilizes     implement the global guidance and local refinement of the
the T2T-ViT to divide images into patches and the RT2T            salient region. Wang et al. [46] introduce a depth integration
transformation to decode patch tokens to saliency maps. Liu et    module that merges three feature maps by leveraging depth-
al. [35] propose SwimNet to explore the advantages of CNN         aware and depth-dispelled features to enhance the complemen-
and transformer in modeling local and global features. Cong       tary information from RGB and depth modalities. Cong et
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                                           4

Fig. 3. Detailed framework of the proposed GL-DMNet. We adopt the ResNet-50 network to extract features of RGB and depth inputs, respectively. Then,
position mutual fusion (PMF) and channel mutual fusion (CMF) are proposed to fuse the multi-modal features. The fused features of all stages are decoded
by the cascade transformer-infused reconstruction network. The saliency head [49] is also added to generate the final predicted feature maps.

al. [47] propose a smAR unit to reduce feature redundancy                                                 TABLE I
and emphasize important spatial locations, and also a cmWR                           S YMBOLS AND NOTATIONS USED IN THIS PAPER AND THEIR
                                                                                                       DESCRIPTIONS .
unit to refine multi-modality features by considering cross-
modality complementary information and global contextual                         Notations                              Descriptions
dependencies. Fang et al. [12] employ the adjacent interac-                      Convk (·)       k × k convolution layer together with BN and ReLU
                                                                                MaxPool(·)                        max-pooling operation
tive aggregation module to leverage the parallel interaction                    AvgPool(·)                      average-pooling operation
of progressive and jumping connections to gradually learn                        Cat[·; ·]                             concatenation
information in abundant resolution, enhancing the aggregation                      M(·)                         the moment normalization
                                                                                   N (·)                           the L2 normalization
of high-level, middle-level, and low-level features. Zhang et                     FC(·)                            fully-connected layer
al. [48] utilize a modal-specific dynamic enhanced module to                    T ransi (·)         the i-th stage of the transformer-based encoder
adaptively enhance intra-modality features and a scene-aware                      CA(·)                      channel attention (CA) module
                                                                                   up(·)                upsampling with bilinear interpolations
dynamic fusion module to achieve dynamic feature selection                       upori (·)           upsampling to the raw size of the input data
between RGB and depth modalities. Wu et al. [9] design a                            ⊙                          element-wise multiplication
granularity-based attention module to strengthen saliency de-                       ⊗                              matrix multiplication
                                                                                     i                    the i-th stage in the neural networks
tection by generating distinct local-spatial attentional regions                    Fi             feature maps outside a module in the i-th stage
through depth granularity and improve feature discriminatory                        fi              feature maps inside a module in the i-th stage
power by applying local channel attention.
   Nevertheless, in our work, attention mechanisms are utilized
for feature enhancement and the interaction and fusion of
cross-modality features. Inspired by the dual attention network              denoted as FiRGB and FiD , respectively, where i ∈ {1, 2, 3, 4}
[7], we design the PMF and CMF modules to model semantic                     is the index of the stage in encoder backbones. To model
interdependencies both spatial and channel dimensions, pro-                  semantic interdependencies in spatial and channel dimensions
moting interactions between cross-modality features.                         and further enhance the saliency feature representations, we
                                                                             feed the RGB and depth features into the proposed position
                    III. M ETHODOLOGY                                        mutual fusion module and channel mutual fusion module to
A. Overview                                                                  generate the attentional cross-modality RGB-D features.
   The overall framework of the proposed GL-DMNet is shown                      During the decoding phase, we devise a novel cascade
in Fig. 3, which consists of a multi-modal feature encoder,                  transformer-infused reconstruction decoder, which decom-
dual mutual fusion module, and cascade transformer-infused                   poses the transformer network into four stages. The ob-
reconstruction decoder.                                                      tained fusion features of each stage are fed independently
   Inspired by the triplet-transformer embedding architecture                to establish long-range dependencies. Finally, we perform a
[10] while pursuing a fair comparison, we first adopt the                    progressive decoding reconstruction structure to derive the
ResNet-50 [50] network to extract multi-level features from                  eventual saliency map. The descriptions of some symbols and
the original inputs of RGB image and depth map. They are                     notations are listed in Table. I to improve readability.
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                     5

B. Dual mutual learning module                                    features. The entire process could be described as:
                                                                      fiA = fiRGB + fiD ,                                     (3)
   How to effectively integrate the cross-modality features
has consistently been a challenging problem in RGB-D SOD           WiSP = Conv7 (Cat(M axP ool(fiA ), AvgP ool(fiA ))),       (4)
tasks for a long time. Previous research primarily utilizes a       fiSP = Conv1 (fiA ⊙ WiSP + fiA ),                         (5)
combination of spatial and channel attention mechanisms to        where M axP ool(·) and AvgP ool(·) denote the max-pooling
achieve cross-modal feature fusion. However, this approach        and average-pooling operations along channel dimension, re-
often overlooks the distinctive information of each modality,     spectively. In addition, Cat(·, ·) and ⊙ represent the concate-
resulting in a lack of complementary. Due to the inherent         nation operation and element-wise multiplication.
differences between RGB and depth modalities, where RGB              Then, we reshape the original single-modal features (i.e.,
images contain rich semantic information and depth maps           fiRGB and fiD ) and the fused features fiSP to RC×N , where
provide spatial-geometric clues, aligning and bridging the        N = H × W represents the number of pixels. The matrix
potential gap between these modalities is crucial for accurate    multiplication operations are also employed to generate the
salient object detection [51].                                    spatial attention maps:
   Inspired by the dual attention [7], we propose a dual mutual
                                                                                M sRGB
                                                                                   i   = M(fiSP ⊗ (fiRGB )T ),                (6)
learning module to enhance the coordination of multi-modal
features, which models semantic interdependencies in spatial                     M sD i = M(fi
                                                                                                SP
                                                                                                   ⊗ (fiD )T ),               (7)
and channel dimensions. Even though most studies in SOD                          M sF
                                                                                    i
                                                                                       u
                                                                                         = M sRGB
                                                                                              i    + M sDi ,                  (8)
tasks capture the local features over modalities, they cannot
globally explore the inherent relationship between different      where ⊗ is the matrix multiplication, and M(x) = sign(x) ·
features (or objects). Our dual attention mechanism, however,     x−1/2 is the moment normalization to ensure the stability and
allows the local features to learn from each other, globally      the appropriate scaling of the computed values.
propagating the information for them. It captures the rich           Next, we refine these modality features by multiplying the
global contextual information and could significantly improve     positional weights and the original features. Also, the L2
the performance by modeling dependencies among local fea-         normalization is utilized to ensure that the values in each
tures. Specifically, as shown in Fig. 4, the position mutual      channel belong to the valid probability distribution, further
fusion module selectively aggregates features at each position    strengthening the stability of the network during training:
by learning the spatial dependencies of the single-modal and                    PiRGB = N (fiRGB ⊗ M sRGB
                                                                                                      i   ),                  (9)
fused features. Meanwhile, the channel mutual fusion module                        PiD = N (fiD ⊗ M sD
                                                                                                     i ),                   (10)
weights and updates each channel map by integrating the
channel mapping relationship between single-modal and fused                       Pi = N (fi ⊗ M sF
                                                                                    Fu        SP        u
                                                                                                      i ),                  (11)
features.                                                                             2
                                                                  where N (x) = x/ ∥x∥2 represents the L2 normalization.
   Compared with previous work [52], [53], we revise and            2) Channel mutual fusion module: Similar to the position
improve the dual mutual learning to explore more complex          mutual fusion module, we employ concatenation operations
cross-modality interaction information. Besides, we adopt         to produce fused features, following the channel attention
some beneficial embedding-wise operations to improve the          mechanism [40] to generate more discriminative features. This
basic PMF and CMF. More importantly, our PMF and CMF              could be indicated as:
allow the RGB and depth information to interact fully with            fiC = Cat(fiRGB , fiD ),                              (12)
their fusion result. A simple illustration in Fig. 9 indicates
how our PMF and CMF comprehensively explore fine-grained           WiCH = F C(M axP ool(fiC )) + F C(AvgP ool(fiC )),       (13)
information from images.                                            fiCH = Conv1 (fiC ⊙ WiCH ),                             (14)
   1) Position mutual fusion module: To be specific, we first     where F C(·) composed of two fully-connected layers.
obtain the RGB features FiRGB and the depth features FiD            However, different from the position mutual fusion module,
from their corresponding backbones, and then apply two            we directly adopt the matrix multiplication operations to
convolutional layers to reduce the number of channels:            calculate the channel attention maps:
                                                                                 M cRGB
                                                                                    i   = M(fiRGB ⊗ fiCH ),                 (15)
             fiRGB = Conv3 (Conv1 (FiRGB )),                (1)                    M cD        D   CH
                                                                                       i = M(fi ⊗ fi  ),                    (16)
                fiD = Conv3 (Conv1 (FiD )),                 (2)                       Fu     RGB
                                                                                   M ci = M ci   + M cD
                                                                                                      i .                   (17)
                                                                     We also perform the matrix multiplications to generate the
where Convk (·) denotes a k × k convolutional layer together      multi-modality features with long-range contextual represen-
with a batch normalization (BN) layer [54] and a rectified        tations:
linear unit (ReLU) activation function.                                         CiRGB = N (M cRGB ⊗ fiRGB ),                (18)
                                                                                              i
   Subsequently, we perform element-wise addition to fuse                          CiD = N (M cD      D
                                                                                                i ⊗ fi ),                   (19)
the cross-modality features and adopt the spatial attention
mechanism [40] to acquire more valuable cross-modal fusion                        CiF u = N (M cF
                                                                                                i
                                                                                                  u
                                                                                                    ⊗ fiCH ).               (20)
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                                 6

Fig. 4. The details of position mutual fusion (PMF) module and channel mutual fusion (CMF) module.

   Finally, we aggregate the outputs of the two mutual fusion              into four stages to generate features of different scales. At each
modules and use an element-wise summation to complete                      stage, the input image is separately decomposed into patches
the eventual feature fusion, which will absorb more semantic               by a trainable linear projection layer. Then, these patches
information. This process could be formulated as:                          are fed into a transformer-based encoder with several layers.
                                                                           Afterwards, the output is reshaped into feature maps for multi-
   fiP M F = Conv3 (Conv1 (Cat(PiRGB , PiD , PiF u ))),            (21)
                                                                           level prediction tasks. This design could be described as:
   fiCM F = Conv3 (Conv1 (Cat(CiRGB , CiD , CiF u ))),             (22)
                                                                                                 fit = T ransi FiF us ,
                                                                                                                     
    FiF us = fiP M F + fiCM F                                      (23)                                                                 (24)

   In conclusion, the elaborately designed dual mutual learning            where T ransi (·) indicates the i-th stage of the transformer-
component fully learns the potential features while highlight-             based encoder. Moreover, another advantage of PVTv2 is that
ing each modality’s core cues. It considers the correlation and            the resolution of output feature maps of each stage remains
complementarity between different modalities, thereby estab-               the same as input features, making it an easy plug-and-play
lishing long-range contextual dependence across modalities.                component to integrate with the proposed architecture.
                                                                              Multi-level Feature Reconstruction: Naturally, there are
C. Cascade Transformer-Infused Reconstruction Decoder                      differences between features at different levels. Thus, directly
   Despite the advantages of CNNs, their limited receptive                 aggregating them may lead to information loss or redundancy
field severely restricts the capability to capture global features.        [8]. In our proposed decoder scheme, we utilize high-level fea-
Therefore, we integrate transformers to augment the global-                tures to guide the decoding of low-level features while filtering
local awareness of multi-level fusion features, enabling the               the inherent differences among features. More importantly,
proposed method to inherit the strengths of both CNN and                   our method focuses on the complementary and consistent
Transformer. The decoded feature maps at each stage contain                information between adjacent levels.
more spatial details and could contribute uniquely to the final               Specifically, we first cascade the outputs of the transformer
prediction.                                                                encoder with original fusion features and then adopt two
   Transformer Embedding: We employ PVTv2-B2 [55] to                       successive convolutions to reduce the number of channels,
learn global representations of the obtained multi-level fusion            which could be formulated as:
features Fiu , because it could simultaneously protect local
continuity by overlapping patch embedding. PVTv2 is divided                              fit = Conv3 (Conv1 (Cat(fit , FiF us )).       (25)
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                         7

   Subsequently, we connect the higher-level features through       outputs by jointly training the model with the multiple-
the dense upsampling and concatenation operations. The chan-        auxiliary side outputs. Hence, the total loss of our training
nel attention (CA) [56] mechanism is also employed to model         could be indicated as:
the significant correlation among different channels, which                              4
                                                                                         X
could be expressed as:                                                        ℓtotal =         λi (ℓbce           iou
                                                                                                    i (Si , G) + ℓi (Si , G)),   (33)
                                                                                         i=1
  fiatt = Conv3 (Conv1 (CA(Cat[up(fi+1
                                   t
                                       ), ..., up(f4t )]))),
                                                           (26)     where G denotes the ground truth, and Si refers to the saliency
where up(·) denotes the upsampling operation via the bilinear       map predicted from the i − th level of the decoder, which is
                              t
interpolation that reshapes fi+1  to same resolution with fit .     upsampled to form the same resolution mask as the ground
   Also, we utilize an element-wise multiplication to integrate     truth. λi is the weight of the i − th level. The weight set
multi-level fusion features and leverage a residual connection      λ follows {0.8, 0.6, 0.4, 0.2} to correlate with the network
to preserve the original features:                                  hierarchies.

                      fires = fiatt ⊙ fit + fit .            (27)                          IV. E XPERIMENTS
   Finally, we sequentially concatenate features from adjacent      A. Datasets and evaluation metrics
stages, progressively generating accurate saliency maps:               Datasets: We conduct experiments on six widely used
  f4out = Conv3 (Conv1 (f4res )),                            (28)   datasets to validate our proposed GL-DMNet. SIP [1] is a
                                                                    high-quality RGB-D dataset with 929 images that capture
  fiout = Conv3 (Conv1 (Cat(fires , fi+1
                                     out
                                         ))), i = 1, 2, 3.   (29)
                                                                    various human postures and movements. DUT-RGBD [59]
   In addition, we add deep supervisions to the outputs fiout of    consists of 800 indoor and 400 outdoor scene images paired
the decoder to speed up convergence. The predicted saliency         with corresponding depth maps. NJUD [60] contains 2,003
maps could be formulated as,                                        stereo image pairs with diverse objects, complex scenarios,
                                                                    and ground-truth maps. STEREO [61], which is the first
              Si = upori (Conv1 (Conv3 (fiout )))            (30)   collection of stereo images utilized for saliency analysis,
where Si represents the predictions in the i-th stage. upori (·)    includes 1,000 initial images and then retains 797 images
upsamples the feature maps to the original resolution of the        after official updates. NLPR [62] includes 1,000 stereo images
input image. Only S1 is used as the final saliency map, while       from 11 indoor and outdoor scene types. SSD [63] is a small-
the other three predictions are omitted in the test phase.          scale dataset that only collects 80 natural images of left and
                                                                    right views from three stereoscopic movies. Following the
                                                                    most common setup of previous studies [39], [64], we use
D. Loss function                                                    700 images from NLPR, 800 pairs from DUT-RGBD, and
   To obtain high-quality saliency maps with clear boundaries,      1,485 samples from NJUD as the training set. The remaining
we decide to employ the BCE loss ℓbce [57] and the ℓiou [58]        images with corresponding depth maps (and also the other
to train our proposed model.                                        three datasets) are used for testing.
   Binary Cross-Entropy (BCE) loss is the most widely-used             Evaluation metrics: We adopt five public evaluation met-
loss in segmentation tasks, which computes the discrepancy          rics for the experiments, including E-measure (Eξ ) [65], S-
between predicted saliency maps and ground truth binary             measure (Sα ) [66], max F-measure (Fβ ) [67], mean absolute
labels. It weights both foreground and background pixels            error (MAE) [68], and precision-recall (PR) curve. E-measure
equally and accurately distinguishes salient and non-salient        assesses the similarity by considering region-aware precision,
regions. It could be defined as below:                              recall, and harmonic mean. S-measure evaluates the structural
            W,H
                                                                    similarity at both object and region levels. F-measure is the
 ℓbce = −
            X
                    [Gwh log(Swh ) + (1 − Gwh ) log(1 − Swh )]      harmonic mean of precision and recall, which is more fairly
            w,h=1
                                                                    evaluating the model’s ability to capture salient regions. MAE
                                                         (31)       measures the average absolute differences between predicted
  Intersection over Union (IoU) loss, however, measures the         and ground-truth saliency maps. PR curve illustrates the trade-
overlap between predicted saliency maps and ground truth,           off balance between precision and recall from various thresh-
guiding the model to focus more on the foreground and               old levels, which visually provides intuitive results when com-
produce more accurate spatially-aligned predictions. It could       paring the performance across different models. In summary,
be defined as:                                                      these selected metrics provide sufficient and comprehensive
                                  W,H                               evaluations of structural similarity, region-aware performance,
                                  P
                                         Swh Gwh                    balanced precision-recall rates, and overall discrimination abil-
         ℓiou = 1 − W,H
                                 w,h=1
                                                             (32)   ity.
                    P
                               (Swh + Gwh − Swh Gwh )
                       w,h=1                                        B. Implementation details
   We adopt a multi-task learning strategy to comprehensively         We conduct all experiments using PyTorch on an NVIDIA
learn the hierarchical saliency information from multi-level        GeForce RTX 3090 GPU. The CNN-based network ResNet-50
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                       8

                                                                TABLE II
Q UANTITATIVE RESULTS COMPARED WITH STATE - OF - THE - ART RGB-D SOD METHODS . “-” MEANS THAT THE RESULTS ARE UNAVAILABLE SINCE THE
    AUTHORS DID NOT RELEASE THEM . ↑ (↓) INDICATES THE LARGER ( SMALLER ), THE BETTER . T HE BEST AND THE SECOND BEST RESULTS ARE
                                         HIGHLIGHTED IN BOLD AND UNDERLINE , RESPECTIVELY.

                                      SIP [1]                           DUT-RGBD [59]                        NJUD [60]
         Model
                          Eξ ↑    Sα ↑    Fβ ↑     MAE ↓      Eξ ↑      Sα ↑   Fβ ↑   MAE ↓       Eξ ↑    Sα ↑    Fβ ↑    MAE ↓
         Ours             0.936   0.896   0.915    0.041      0.962     0.931 0.947   0.029       0.950   0.920   0.930   0.033
   FCFNet(24TCSVT)          -       -       -        -        0.956     0.924 0.931   0.032       0.953   0.918   0.923   0.034
   AirSOD(24TCSVT)        0.903   0.858   0.887    0.060      0.946     0.891 0.920   0.048       0.944   0.908   0.918   0.039
    MIRV(24TCSVT)         0.927   0.877   0.894    0.049        -         -       -     -         0.929   0.890   0.899   0.046
      DHFR(23TIP)         0.902   0.843   0.874    0.064        -         -       -     -         0.936   0.893   0.901   0.040
     S3Net(23TMM)         0.933   0.875   0.891    0.051      0.939     0.912 0.922   0.035       0.944   0.913   0.928   0.034
     M2RNet(23PR)         0.921   0.882   0.902    0.049      0.935     0.903 0.925   0.042       0.904   0.910   0.922   0.049
      HINet(23PR)         0.899   0.856   0.880    0.066        -         -       -     -         0.945   0.915   0.914   0.039
    DLMNet(22MM)          0.855   0.777   0.789    0.109      0.897     0.846 0.865   0.074       0.859   0.808   0.818   0.097
  MobileSal(22TPAMI)      0.916   0.873   0.898    0.053      0.950     0.896 0.912   0.041       0.942   0.905   0.914   0.041
   JLDCF(22TPAMI)         0.923   0.881   0.905    0.050      0.938     0.905 0.924   0.043       0.935   0.902   0.912   0.041
      DENet(22TIP)        0.908   0.852   0.873    0.061        -         -       -     -         0.920   0.882   0.893   0.050
   CCAFNet(22TMM)         0.915   0.877   0.881    0.054      0.941     0.905 0.915   0.036       0.920   0.910   0.911   0.037
     DWD(22TMM)             -       -       -        -        0.902     0.864 0.853   0.072       0.927   0.886   0.876   0.050
  MoADNet(22TCSVT)        0.911   0.865   0.890    0.058      0.945     0.907 0.920   0.033       0.929   0.901   0.907   0.042
   MMNet(22TCSVT)         0.871   0.824   0.860    0.080      0.951     0.920 0.939   0.032       0.922   0.910   0.918   0.038
     EMANet(22PR)           -       -       -        -        0.951     0.920 0.937   0.032       0.946   0.914   0.923   0.035
     DCF(21CVPR)          0.920   0.873   0.899    0.052      0.956     0.924 0.940   0.031       0.940   0.903   0.917   0.039
     CDINet(21MM)         0.911   0.875   0.903    0.055      0.956     0.926 0.944   0.030       0.944   0.918   0.827   0.036
    DFM-Net(21MM)         0.926   0.883   0.887    0.051      0.945     0.913 0.928   0.039       0.947   0.906   0.910   0.042
     BiANet(21TIP)        0.920   0.883   0.904    0.053        -         -       -     -         0.928   0.915   0.929   0.039
      DQSD(21TIP)         0.900   0.863   0.890    0.065      0.889     0.844 0.859   0.073       0.912   0.898   0.910   0.051
      DRLF(21TIP)         0.891   0.850   0.868    0.071      0.870     0.825 0.851   0.080       0.901   0.886   0.883   0.055
  cmSalGAN(21TMM)         0.904   0.864   0.889    0.064      0.904     0.867 0.887   0.067       0.923   0.903   0.910   0.047
  IRFRNet(21TNNLS)        0.921   0.879   0.881    0.054      0.951     0.919 0.924   0.035       0.945   0.909   0.908   0.040
                                   STEREO [61]                             NLPR [62]                          SSD [63]
         Model
                          Eξ ↑    Sα ↑    Fβ ↑     MAE ↓      Eξ ↑      Sα ↑   Fβ ↑   MAE ↓       Eξ ↑    Sα ↑    Fβ ↑    MAE ↓
         Ours             0.947   0.908   0.918    0.037      0.962     0.927 0.926   0.022       0.920   0.874   0.887   0.045
   FCFNet(24TCSVT)        0.947   0.906   0.906    0.038      0.960     0.924 0.911   0.024         -       -       -       -
   AirSOD(24TCSVT)        0.939   0.895   0.900    0.043      0.963     0.924 0.923   0.023         -       -       -       -
    MIRV(24TCSVT)         0.937   0.891   0.900    0.042      0.954     0.914 0.914   0.025         -       -       -       -
      DHFR(23TIP)         0.935   0.884   0.896    0.043      0.950     0.904 0.901   0.027       0.911   0.858   0.869   0.051
     S3Net(23TMM)         0.945   0.913   0.918    0.038      0.962     0.927 0.923   0.021         -       -       -       -
     M2RNet(23PR)         0.929   0.899   0.913    0.042      0.941     0.918 0.921   0.033         -       -       -       -
      HINet(23PR)         0.933   0.892   0.883    0.049      0.957     0.922 0.906   0.026       0.916   0.865   0.852   0.049
    DLMNet(22MM)          0.886   0.833   0.838    0.079      0.815     0.795 0.768   0.081       0.841   0.788   0.796   0.101
  MobileSal(22TPAMI)      0.940   0.903   0.906    0.041      0.961     0.920 0.916   0.025       0.914   0.862   0.863   0.052
   JLDCF(22TPAMI)         0.937   0.903   0.914    0.040      0.954     0.925 0.926   0.023         -       -       -       -
      DENet(22TIP)        0.928   0.881   0.891    0.048      0.943     0.900 0.897   0.031       0.875   0.830   0.833   0.070
   CCAFNet(22TMM)         0.921   0.891   0.887    0.044      0.952     0.922 0.909   0.026         -       -       -       -
     DWD(22TMM)           0.933   0.899   0.887    0.046      0.936     0.906 0.882   0.038       0.917   0.861   0.832   0.049
  MoADNet(22TCSVT)        0.931   0.896   0.901    0.043      0.950     0.918 0.908   0.024       0.900   0.854   0.863   0.057
   MMNet(22TCSVT)         0.916   0.884   0.896    0.046      0.955     0.925 0.919   0.023       0.912   0.871   0.872   0.047
     EMANet(22PR)         0.939   0.901   0.911    0.040      0.955     0.924 0.922   0.024       0.909   0.870   0.875   0.047
     DCF(21CVPR)          0.943   0.905   0.914    0.037      0.956     0.921 0.917   0.023       0.905   0.851   0.857   0.054
     CDINet(21MM)           -     0.905   0.903    0.041      0.953     0.927 0.923   0.024       0.906   0.852   0.867   0.057
    DFM-Net(21MM)         0.941   0.898   0.893    0.045      0.957     0.923 0.908   0.026         -       -       -       -
     BiANet(21TIP)        0.929   0.903   0.910    0.044      0.955     0.925 0.921   0.025       0.901   0.867   0.870   0.051
      DQSD(21TIP)         0.911   0.891   0.900    0.052      0.934     0.915 0.909   0.030       0.890   0.868   0.877   0.053
      DRLF(21TIP)         0.915   0.888   0.878    0.050      0.935     0.902 0.904   0.032       0.879   0.834   0.859   0.066
  cmSalGAN(21TMM)         0.932   0.900   0.910    0.050      0.948     0.922 0.923   0.027       0.851   0.791   0.764   0.086
  IRFRNet(21TNNLS)        0.941   0.897   0.893    0.044      0.960     0.921 0.910   0.026       0.910   0.864   0.841   0.053

[50] and transformer-based network PVTv2-B2 [55] are em-              utilize the Adam optimizer [69] to train the proposed network
ployed to extract local and global features, respectively. During     in an end-to-end manner with a batch size of 4 for 200
the training and test phases, we replicate the input depth map        epochs. During the initial 30 epochs, we freeze the ResNet-50
into three channels and resize all images to 256×256 pixels.          networks to train the other parameters of the model. For the
Additionally, different kinds of data augmentations, such as          subsequent 30 epochs, we unfreeze the ResNet-50 network and
random cropping, flipping, rotation, and color enhancement,           freeze the Transformer network. After 60 epochs, we unfreeze
are employed during the training to prevent overfitting. We           all networks to fine-tune the parameters of our model. The
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                                   9

Fig. 5. Visual comparisons of the proposed GL-DMNet and other state-of-the-art RGB-D SOD methods, including MIRV [70], HINet [13], DLMNet [71],
CCAFNet [72], DENet [73], MoADNet [64], MMNet [74], CMINet [22] and DCF [75]. Our approach obtains competitive performance in a variety of
challenging scenarios.

initial learning rate is set to 1e-4 with a decay factor of 0.97.        their performance based on the saliency maps derived from
Last, the entire training process takes approximately 7 hours            their original papers. All the evaluation metrics are calculated
to converge. The inference time for images with 256×256 size             by the official evaluation tools [1].
is 40 frames per second (FPS).                                              Quantitative Analysis: Table. II illustrates the quantitative
                                                                         results of our model. We calculate four evaluation metrics on
C. Comparisons with state-of-the-art methods                             six datasets for comprehensive comparisons. Higher Sα , Fβ
   We compare the proposed GL-DMNet with 24 state-of-the-                and Eξ indicate better performance. On the contrary, lower
art RGB-D SOD models, including FCFNet [24], AirSOD                      MAE is better. We place other baselines in chronological
[14], MIRV [70], DHFR [76], S3Net [77], M2RNet [12],                     order from top to bottom. Compared with other state-of-
HINet [13], DLMNet [71], MobileSal [78], JLDCF [79],                     the-art methods, we could see that the proposed GL-DMNet
DENet [73], CCAFNet [72], DWD [80], MoADNet [64],                        almost achieves the best performance across all datasets, which
MMNet [74], EMANet [45], DCF [75], CDINet [51], DFM-                     demonstrates the effectiveness and superiority of our method.
Net [81], BiANet [82], DQSD [83], DRLF [84], cmSalGAN                    Besides, remarkable improvements are observed in all metrics,
[85], and IRFRNet [86]. For fair comparisons, we compute                 especially on the SIP and the DUT-RGBD datasets. The
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                         10

Fig. 6. PR curves of different saliency detectors on six datasets.

improvement gain of our model achieves 16.3% of MAE,                 maps predicted by GL-DMNet and other SOTA methods in
1.5% of Sα , 1.1% of Fβ and 0.3% of Eξ score on the                  Fig. 5. In particular, our method could capture more fine-
SIP dataset when compared to the second best method. We              grained details and pixel-level information in scenarios with
also improve 3.3% of MAE, 0.5% of Sα , 0.3% of Fβ and                intricate structures (1st row), exhibiting a holistic understand-
0.6% of Eξ score on the DUT-RGBD dataset. Moreover,                  ing of the localized features. Furthermore, in the cases of
FCFNet [24] slightly outperforms our model in terms of the           large objects (2nd row), small objects (3rd row), and multiple
Eξ metric on the NJUD and STEREO datasets, which can be              objects (4th-5th rows), our model efficiently and adequately
attributed to its strategy of discarding some low-quality depth      distinguishes the outline of the object from the background,
maps. Additionally, S3Net [77] introduces supplementary prior        which indicates its strong robustness in discerning salient
information, which enables it to slightly surpass our model          objects with varying scales. Additionally, even though depth
in the Sα and Fβ metrics on the STEREO dataset and the               information is absent (6th-7th rows), our model could still
Fβ and MAE metrics on the NLPR dataset. Nevertheless,                extract meaningful cues from 2D visual information alone
our proposed method outperforms theirs on the vast majority          and produce accurate saliency maps. Our model also performs
of datasets. We attribute our superior performance to the            better when dealing with complex scenes (8th-9th rows) and
fusion strategies incorporating dual mutual learning, which          low contrast (10th row). These results validate the superiority
places greater emphasis on detailed structures and contextual        of our model in handling different visual environments, with
information across different modalities.                             consistent and satisfactory performance for multiple challeng-
                                                                     ing scenarios.
  Qualitative Analysis: To further verify the performance of
our proposed method, we provide some representative saliency           PR Curves: As shown in Fig. 6, the PR curves visually
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                                         11

                                                            TABLE III
                           A BLATION EXPERIMENT OF DUAL MUTUAL FUSION MODULE . T HE BEST RESULT IS IN BOLD .

                                   Candidate                                NLPR                               DUT-RGBD
              Variant
                         PMF     CMF   Serial   Parallel     Eξ ↑      Sα ↑    Fβ ↑    MAE ↓       Eξ ↑      Sα ↑   Fβ ↑      MAE ↓
               No.1       ✓                                  0.955     0.920  0.915    0.026       0.958     0.924  0.940     0.033
               No.2               ✓                          0.957     0.922  0.921    0.026       0.960     0.930  0.946     0.030
               No.3       ✓       ✓       ✓                  0.960     0.927  0.925    0.023       0.959     0.925  0.942     0.033
               No.4                                ✓         0.952     0.920  0.915    0.026       0.955     0.921  0.939     0.033
               No.5       ✓       ✓                ✓         0.962     0.927  0.926    0.022       0.962     0.931  0.947     0.029

                                                           TABLE IV
           A BLATION EXPERIMENT OF CASCADE TRANSFORMER - INFUSED RECONSTRUCTION DECODER . T HE BEST RESULT IS IN BOLD .

                                   Candidate                                 NLPR                               DUT-RGBD
            Variant
                        PVT V2   PVT V1     Reconstruction     Eξ ↑     Sα ↑    Fβ ↑      MAE ↓      Eξ ↑     Sα ↑   Fβ ↑       MAE ↓
             No.1         ✓                                    0.954    0.921  0.921      0.024      0.959    0.928  0.945      0.030
             No.2                     ✓                        0.948    0.918  0.919      0.027      0.958    0.928  0.943      0.032
             No.3                                 ✓            0.951    0.917  0.916      0.028      0.955    0.925  0.939      0.034
             No.4                     ✓           ✓            0.958    0.921  0.918      0.025      0.961    0.931  0.945      0.030
             No.5         ✓                       ✓            0.962    0.927  0.926      0.022      0.962    0.931  0.947      0.029

depict the comparison between the proposed GL-DMNet and
other state-of-the-art methods on six RGB-D datasets. The red
solid line indicates that our method outperforms all compared
methods across most threshold values.

D. Ablation studies
   To further investigate the effectiveness of each key compo-
nent in the proposed GL-DMNet, we conduct ablation studies
on NLPR and DUT-RGBD datasets by systematically remov-
ing components or replacing them with similar structures to
assess their impact on GL-DMNet. Fig. 7 and Fig. 8 also show               Fig. 7. Visual comparison of saliency map results produced by different
                                                                           variants of fusion modules. Please refer to Table III for the explanation of
the qualitative comparisons of different variants.                         No.1 to No.4.
   The effectiveness of dual mutual fusion module. Table
III illustrates the ablation results on the dual-mutual fusion
module. We consider four variants of fusion strategies: (1)                evaluation metrics. Compared with the PVTv1, PVTv2 could
only PMF, (2) only CMF, (3) serial utilization of PMF and                  capture global information while protecting local continuity at
CMF, (4) direct connection without other operations, and                   the same time. Thus, PVTv2 is apparently more suitable for
(5) our dual mutual design. First of all, it is observed that              our model where we aim to explore global-local awareness for
directly catenating multi-modal features without learning their            RGB-D SOD task. Moreover, PVTv2 is capable of speeding
independence would harm the performance, which is the worst                up the decoding process of Transformer-induced architecture.
among all the ablative variants. Second, adopting PMF (from
spatial dimension) or CMF (from channel dimension) can only
bring limited improvement. This may suggest that it is nec-
essary to combine of these two types for better performance.
Thus, if we use the serial means for them, the performance
could be further improved. However, our dual mutual that
utilizes both spatial and channel dimensions to learn the deep
correlation and independence, outperforms all the variants.
The dual mutual design promotes the interactions between
cross-modality features. Hence, it becomes possible to fuse
multi-modal embeddings without destroying their individual
characteristics.                                                           Fig. 8. Visual comparison of saliency map results produced by different
                                                                           variants of decoder. Please refer to Table IV for the explanation of No.1 to
   The effectiveness of transformer embedding. In our GL-                  No.4.
DMNet, we deploy Transformer-induced architecture to learn
the global representations of the multi-level fusion features.                The effectiveness of multi-level feature reconstruction.
Now we verify the different choice of the Transformer-based                To validate the effectiveness of the adopted reconstruction
embedding: (1) PVTv2 and (2) PVTv1. The results are shown                  decoder for the multi-level features, we conduct comparative
in the first and second rows of Table IV. Obviously, the                   experiments on the ablated types: (1) only feature reconstruc-
performance of PVTv2 is better than PVTv1 over all the                     tion without Transformer-based embedding (e.g., PVTv2 and
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                                     12

PVTv1), (2) reconstruction on the output from PVTv2, and
(3) reconstruction on the output from PVTv1. The results are
presented in the fourth and fiveth rows of Table IV. removing
the Transformer-based feature learning is not beneficial to
the reconstruction decoding, leading to a worse performance
after feature reconstruction. This is because there exists in-
herent discrepancy between difference levels. Transformer-
based embedding will help the reconstruction to understand
it and decode them more efficiently. Thus, the performance of
reconstruction with PVTv2 or PVTv1 gets improved. However,
compared with PVTv1-based reconstruction, the reconstruc-
tion with PVTv2 is much superior, obtaining more improve-           Fig. 9. Feature visualizations of the PMF and CMF. S1 represents the channel
ment. This indicates the global-local awareness captured by         images selected from the fusion module of Stage 1.
PVTv2 would further strengthen the decoding process of
multi-level feature reconstruction. Hence, we eventually decide
to adopt the reconstruction decoder with PVTv2.                     independence across multi-level features, we carefully design
                                                                    the cascade transformer-infused reconstruction for multi-level
                                                                    feature decoding. Last, we conduct extensive experiments on
                           TABLE V
  A BLATION EXPERIMENT OF LOSS FUNCTION . T HE BEST RESULT IS IN    six public datasets over 24 state-of-the-art baselines. The
                            BOLD .                                  experimental results demonstrate the superiority and effective-
                         NJUD                       SIP
                                                                    ness of our GL-DMNet. In the future, we intend to leverage the
      Loss                                                          proposed model to tackle several practical challenges within
                Eξ ↑ Sα ↑ Fβ ↑ MAE ↓      Eξ ↑ Sα ↑ Fβ ↑ MAE ↓
     BCE        0.941 0.918 0.928 0.038   0.927 0.888 0.907 0.048   the medical imaging domain, aiming to enhance the model’s
   BCE+DICE     0.939 0.919 0.926 0.038   0.930 0.895 0.912 0.045   generalization ability and robustness and broaden its appli-
   BCE+SSIM     0.943 0.917 0.926 0.035   0.927 0.888 0.910 0.045
     Ours       0.950 0.920 0.930 0.033   0.936 0.896 0.915 0.041   cability. By developing a universal and effective multimodal
                                                                    model, we aspire to simultaneously process data from diverse
   The effectiveness of loss function. To demonstrate the           modalities such as RGB, depth, and thermal. This approach is
effectiveness and optimality of our loss function design, we        expected to significantly enhance the model’s practical utility,
conducted experiments using three different combinations of         enabling it to integrate and analyze complex datasets and
loss functions for comparison. The results show that our            thus provide more comprehensive insights into various medical
combination consistently outperforms the other three on the         conditions.
NJUD and SIP datasets, thereby establishing the superiority
of our design. The results in the table V highlight the robust                                    R EFERENCES
performance of our loss function.
                                                                     [1] D.-P. Fan, Z. Lin, Z. Zhang, M. Zhu, and M.-M. Cheng, “Rethinking
                                                                         rgb-d salient object detection: Models, data sets, and large-scale bench-
E. Visualization                                                         marks,” IEEE Transactions on Neural Networks and Learning Systems,
                                                                         vol. 32, no. 5, pp. 2075–2089, 2021.
   Fig. 9 illustrates the separated channel images processed         [2] T. Zhou, D.-P. Fan, M.-M. Cheng, J. Shen, and L. Shao, “Rgb-d salient
by the PMF and CMF modules. Compared to the RGB and                      object detection: A survey,” Computational Visual Media, vol. 7, pp.
                                                                         37–69, 2021.
depth images of the same channels, the images processed by           [3] K. Muhammad, T. Hussain, H. Ullah, J. D. Ser, M. Rezaei, N. Kumar,
the PMF and CMF modules exhibit clearer edge contours                    M. Hijji, P. Bellavista, and V. H. C. de Albuquerque, “Vision-based
and richer details. This enhancement addresses the inherent              semantic segmentation in scene understanding for autonomous driving:
                                                                         Recent achievements, challenges, and outlooks,” IEEE Transactions on
discrepancies between RGB and depth information. Further-                Intelligent Transportation Systems, vol. 23, no. 12, pp. 22 694–22 715,
more, it demonstrates the effectiveness of the PMF and CMF               2022.
modules, which fully leverage the interrelationships between         [4] Y. Tao, J. Zhang, J. Hong, and Y. Zhu, “Dreamt: Diversity enlarged mu-
different modalities in spatial and channel dimensions, thereby          tual teaching for unsupervised domain adaptive person re-identification,”
                                                                         IEEE Transactions on Multimedia, vol. 25, pp. 4586–4597, 2023.
enhancing the feature fusion effect.                                 [5] B. Li, X. Lin, B. Liu, Z.-F. He, and Y.-K. Lai, “Lightweight text-
                                                                         driven image editing with disentangled content and attributes,” IEEE
                                                                         Transactions on Multimedia, vol. 26, pp. 1829–1841, 2024.
             V. C ONCLUSION AND FUTURE WORK                          [6] D. Zhang, G. Huang, Q. Zhang, J. Han, J. Han, and Y. Yu, “Cross-
   In this work, we propose a novel model called dual mutual             modality deep feature learning for brain tumor segmentation,” Pattern
                                                                         Recognition, vol. 110, p. 107562, 2021.
learning network with global–local awareness (GL-DMNet)              [7] J. Fu, J. Liu, H. Tian, Y. Li, Y. Bao, Z. Fang, and H. Lu, “Dual attention
for the RGB-D salient object detection task. Our motivation              network for scene segmentation,” in 2019 IEEE/CVF Conference on
is existing methods directly fuse attentional cross-modality             Computer Vision and Pattern Recognition (CVPR), 2019, pp. 3141–
                                                                         3149.
features under manual-mandatory fusion strategy without con-         [8] F. Sun, P. Ren, B. Yin, F. Wang, and H. Li, “Catnet: A cascaded and
sidering the inherent discrepancy between the RGB and depth.             aggregated transformer network for rgb-d salient object detection,” IEEE
Firstly, we present the position mutual fusion and channel               Transactions on Multimedia, vol. 26, pp. 2249–2262, 2024.
                                                                     [9] Z. Wu, G. Allibert, F. Meriaudeau, C. Ma, and C. Demonceaux, “Hi-
mutual fusion modules by parallel design to efficiently ex-              danet: Rgb-d salient object detection via hierarchical depth awareness,”
tract features. Secondly, to distinguish the discrepancy and             IEEE Transactions on Image Processing, vol. 32, pp. 2160–2173, 2023.
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                                                   13

[10] Z. Liu, Y. Wang, Z. Tu, Y. Xiao, and B. Tang, “Tritransnet: Rgb-d             [32] W. Wang, E. Xie, X. Li, D.-P. Fan, K. Song, D. Liang, T. Lu, P. Luo,
     salient object detection with a triplet transformer embedding network,”            and L. Shao, “Pyramid vision transformer: A versatile backbone for
     in Proceedings of the 29th ACM international conference on multimedia,             dense prediction without convolutions,” in 2021 IEEE/CVF International
     2021, pp. 4481–4490.                                                               Conference on Computer Vision (ICCV), 2021, pp. 548–558.
[11] J. Fu, J. Liu, J. Jiang, Y. Li, Y. Bao, and H. Lu, “Scene segmentation with   [33] Z. Liu, Y. Lin, Y. Cao, H. Hu, Y. Wei, Z. Zhang, S. Lin, and
     dual relation-aware attention network,” IEEE Transactions on Neural                B. Guo, “Swin transformer: Hierarchical vision transformer using shifted
     Networks and Learning Systems, vol. 32, no. 6, pp. 2547–2560, 2021.                windows,” in 2021 IEEE/CVF International Conference on Computer
[12] X. Fang, M. Jiang, J. Zhu, X. Shao, and H. Wang, “M2rnet: Multi-                   Vision (ICCV), 2021, pp. 9992–10 002.
     modal and multi-scale refined network for rgb-d salient object detection,”    [34] N. Liu, N. Zhang, K. Wan, L. Shao, and J. Han, “Visual saliency
     Pattern Recognition, vol. 135, p. 109139, 2023.                                    transformer,” in 2021 IEEE/CVF International Conference on Computer
[13] H. Bi, R. Wu, Z. Liu, H. Zhu, C. Zhang, and T.-Z. Xiang, “Cross-modal              Vision (ICCV), 2021, pp. 4702–4712.
     hierarchical interaction network for rgb-d salient object detection,”         [35] Z. Liu, Y. Tan, Q. He, and Y. Xiao, “Swinnet: Swin transformer drives
     Pattern Recognition, vol. 136, p. 109194, 2023.                                    edge-aware rgb-d and rgb-t salient object detection,” IEEE Transactions
[14] Z. Zeng, H. Liu, F. Chen, and X. Tan, “Airsod: A lightweight network               on Circuits and Systems for Video Technology, vol. 32, no. 7, pp. 4486–
     for rgb-d salient object detection,” IEEE Transactions on Circuits and             4497, 2022.
     Systems for Video Technology, vol. 34, no. 3, pp. 1656–1669, 2024.            [36] R. Cong, H. Liu, C. Zhang, W. Zhang, F. Zheng, R. Song, and S. Kwong,
[15] T.-Y. Lin, P. Dollár, R. Girshick, K. He, B. Hariharan, and S. Belongie,          “Point-aware interaction and cnn-induced refinement network for rgb-d
     “Feature pyramid networks for object detection,” in 2017 IEEE Confer-              salient object detection,” in Proceedings of the 31st ACM International
     ence on Computer Vision and Pattern Recognition (CVPR), 2017, pp.                  Conference on Multimedia, 2023, pp. 406–416.
     936–944.                                                                      [37] Y. Wang, X. Jia, L. Zhang, Y. Li, J. H. Elder, and H. Lu, “A uniform
[16] G. Huang, Z. Liu, L. Van Der Maaten, and K. Q. Weinberger, “Densely                transformer-based structure for feature fusion and enhancement for rgb-d
     connected convolutional networks,” in 2017 IEEE Conference on Com-                 saliency detection,” Pattern Recognition, vol. 140, p. 109516, 2023.
     puter Vision and Pattern Recognition (CVPR), 2017, pp. 2261–2269.             [38] L. Gao, B. Liu, P. Fu, and M. Xu, “Tsvt: Token sparsification vision
[17] X. Fang, M. Jiang, J. Zhu, X. Shao, and H. Wang, “Grouptransnet: Group             transformer for robust rgb-d salient object detection,” Pattern Recogni-
     transformer network for rgb-d salient object detection,” Neurocomputing,           tion, vol. 148, p. 110190, 2024.
     vol. 594, p. 127865, 2024.                                                    [39] J. Wu, F. Hao, W. Liang, and J. Xu, “Transformer fusion and pixel-
[18] B. Wu, C. Xu, X. Dai, A. Wan, P. Zhang, Z. Yan, M. Tomizuka,                       level contrastive learning for rgb-d salient object detection,” IEEE
     J. Gonzalez, K. Keutzer, and P. Vajda, “Visual transformers: Token-                Transactions on Multimedia, vol. 26, pp. 1011–1026, 2024.
     based image representation and processing for computer vision,” arXiv         [40] S. Woo, J. Park, J.-Y. Lee, and I. S. Kweon, “Cbam: Convolutional
     preprint arXiv:2006.03677, 2020.                                                   block attention module,” in European conference on computer vision.
[19] J. Ren, X. Gong, L. Yu, W. Zhou, and M. Y. Yang, “Exploiting                       Springer, 2018, pp. 3–19.
     global priors for rgb-d saliency detection,” in 2015 IEEE Conference on       [41] X. Li, W. Wang, X. Hu, and J. Yang, “Selective kernel networks,” in
     Computer Vision and Pattern Recognition Workshops (CVPRW), 2015,                   2019 IEEE/CVF Conference on Computer Vision and Pattern Recogni-
     pp. 25–32.                                                                         tion (CVPR), 2019, pp. 510–519.
[20] D. Feng, N. Barnes, S. You, and C. McCarthy, “Local background                [42] Q. Hou, L. Zhang, M.-M. Cheng, and J. Feng, “Strip pooling: Rethinking
     enclosure for rgb-d salient object detection,” in 2016 IEEE Conference             spatial pooling for scene parsing,” in 2020 IEEE/CVF Conference on
     on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 2343–                 Computer Vision and Pattern Recognition (CVPR), 2020, pp. 4002–
     2350.                                                                              4011.
[21] H. Song, Z. Liu, H. Du, G. Sun, O. Le Meur, and T. Ren, “Depth-aware          [43] Q. Hou, D. Zhou, and J. Feng, “Coordinate attention for efficient mobile
     salient object detection and segmentation via multiscale discriminative            network design,” in 2021 IEEE/CVF Conference on Computer Vision
     saliency fusion and bootstrap learning,” IEEE Transactions on Image                and Pattern Recognition (CVPR), 2021, pp. 13 708–13 717.
     Processing, vol. 26, no. 9, pp. 4204–4216, 2017.                              [44] N. Liu, N. Zhang, L. Shao, and J. Han, “Learning selective mutual
[22] K. Yi, J. Zhu, F. Guo, and J. Xu, “Cross-stage multi-scale interaction             attention and contrast for rgb-d saliency detection,” IEEE Transactions
     network for rgb-d salient object detection,” IEEE Signal Processing                on Pattern Analysis and Machine Intelligence, vol. 44, no. 12, pp. 9026–
     Letters, vol. 29, pp. 2402–2406, 2022.                                             9042, 2022.
[23] F. Wang, R. Wang, and F. Sun, “Dcmnet: Discriminant and cross-                [45] G. Feng, J. Meng, L. Zhang, and H. Lu, “Encoder deep interleaved
     modality network for rgb-d salient object detection,” Expert Systems               network with multi-scale aggregation for rgb-d salient object detection,”
     with Applications, vol. 214, p. 119047, 2023.                                      Pattern Recognition, vol. 128, p. 108666, 2022.
[24] Q. Zhang, Q. Qin, Y. Yang, Q. Jiao, and J. Han, “Feature calibrating and      [46] X. Wang, L. Zhu, S. Tang, H. Fu, P. Li, F. Wu, Y. Yang, and Y. Zhuang,
     fusing network for rgb-d salient object detection,” IEEE Transactions on           “Boosting rgb-d saliency detection by leveraging unlabeled rgb images,”
     Circuits and Systems for Video Technology, vol. 34, no. 3, pp. 1493–               IEEE Transactions on Image Processing, vol. 31, pp. 1107–1119, 2022.
     1507, 2024.                                                                   [47] R. Cong, Q. Lin, C. Zhang, C. Li, X. Cao, Q. Huang, and Y. Zhao, “Cir-
[25] F. Xiao, Z. Pu, J. Chen, and X. Gao, “Dgfnet: Depth-guided cross-                  net: Cross-modality interaction and refinement for rgb-d salient object
     modality fusion network for rgb-d salient object detection,” IEEE                  detection,” IEEE Transactions on Image Processing, vol. 31, pp. 6800–
     Transactions on Multimedia, vol. 26, pp. 2648–2658, 2024.                          6815, 2022.
[26] X. Cheng, X. Zheng, J. Pei, H. Tang, Z. Lyu, and C. Chen, “Depth-             [48] M. Zhang, S. Yao, B. Hu, Y. Piao, and W. Ji, “C2 dfnet: Criss-
     induced gap-reducing network for rgb-d salient object detection: An                cross dynamic filter network for rgb-d salient object detection,” IEEE
     interaction, guidance and refinement approach,” IEEE Transactions on               Transactions on Multimedia, vol. 25, pp. 5142–5154, 2023.
     Multimedia, vol. 25, pp. 4253–4266, 2023.                                     [49] M. Fan, S. Lai, J. Huang, X. Wei, Z. Chai, J. Luo, and X. Wei,
[27] L. Li, J. Han, N. Liu, S. Khan, H. Cholakkal, R. M. Anwer, and                     “Rethinking bisenet for real-time semantic segmentation,” in 2021
     F. S. Khan, “Robust perception and precise segmentation for scribble-              IEEE/CVF Conference on Computer Vision and Pattern Recognition
     supervised rgb-d saliency detection,” IEEE Transactions on Pattern                 (CVPR), 2021, pp. 9711–9720.
     Analysis and Machine Intelligence, vol. 46, no. 1, pp. 479–496, 2024.         [50] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
[28] M. Zhong, J. Sun, P. Ren, F. Wang, and F. Sun, “Magnet: Multi-scale                recognition,” in 2016 IEEE Conference on Computer Vision and Pattern
     awareness and global fusion network for rgb-d salient object detection,”           Recognition (CVPR), 2016, pp. 770–778.
     Knowledge-Based Systems, p. 112126, 2024.                                     [51] C. Zhang, R. Cong, Q. Lin, L. Ma, F. Li, Y. Zhao, and S. Kwong,
[29] D. Zhang, J. Han, Y. Zhang, and D. Xu, “Synthesizing supervision                   “Cross-modality discrepant interaction network for rgb-d salient object
     for learning deep saliency network without human annotation,” IEEE                 detection,” in Proceedings of the 29th ACM international conference on
     Transactions on Pattern Analysis and Machine Intelligence, vol. 42,                multimedia, 2021, pp. 2094–2102.
     no. 7, pp. 1755–1769, 2020.                                                   [52] C. Fang, Q. Wang, L. Cheng, Z. Gao, C. Pan, Z. Cao, Z. Zheng, and
[30] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,            D. Zhang, “Reliable mutual distillation for medical image segmentation
     Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in             under imperfect annotations,” IEEE Transactions on Medical Imaging,
     neural information processing systems, vol. 30, 2017.                              vol. 42, no. 6, pp. 1720–1734, 2023.
[31] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai,             [53] C. Fang, L. Wang, D. Zhang, J. Xu, Y. Yuan, and J. Han, “Incremental
     T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly et al.,             cross-view mutual distillation for self-supervised medical ct synthesis,”
     “An image is worth 16x16 words: Transformers for image recognition                 in 2022 IEEE/CVF Conference on Computer Vision and Pattern Recog-
     at scale,” arXiv preprint arXiv:2010.11929, 2020.                                  nition (CVPR), 2022, pp. 20 645–20 654.
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                                                                                                    14

[54] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep                 tion,” IEEE Transactions on Image Processing, vol. 32, pp. 5423–5437,
     network training by reducing internal covariate shift,” in International         2023.
     conference on machine learning, 2015, pp. 448–456.                          [77] L. Zhu, X. Wang, P. Li, X. Yang, Q. Zhang, W. Wang, C.-B. Schönlieb,
[55] W. Wang, E. Xie, X. Li, D.-P. Fan, K. Song, D. Liang, T. Lu, P. Luo, and         and C. L. P. Chen, “S 3 net: Self-supervised self-ensembling network
     L. Shao, “Pvt v2: Improved baselines with pyramid vision transformer,”           for semi-supervised rgb-d salient object detection,” IEEE Transactions
     Computational Visual Media, vol. 8, no. 3, pp. 415–424, 2022.                    on Multimedia, vol. 25, pp. 676–689, 2023.
[56] J. Hu, L. Shen, and G. Sun, “Squeeze-and-excitation networks,” in           [78] Y.-H. Wu, Y. Liu, J. Xu, J.-W. Bian, Y.-C. Gu, and M.-M. Cheng,
     Proceedings of the IEEE conference on computer vision and pattern                “Mobilesal: Extremely efficient rgb-d salient object detection,” IEEE
     recognition, 2018, pp. 7132–7141.                                                Transactions on Pattern Analysis and Machine Intelligence, vol. 44,
[57] P.-T. De Boer, D. P. Kroese, S. Mannor, and R. Y. Rubinstein, “A tutorial        no. 12, pp. 10 261–10 269, 2022.
     on the cross-entropy method,” Annals of operations research, vol. 134,      [79] K. Fu, D.-P. Fan, G.-P. Ji, Q. Zhao, J. Shen, and C. Zhu, “Siamese
     pp. 19–67, 2005.                                                                 network for rgb-d salient object detection and beyond,” IEEE Transac-
[58] G. Máttyus, W. Luo, and R. Urtasun, “Deeproadmapper: Extracting road            tions on Pattern Analysis and Machine Intelligence, vol. 44, no. 9, pp.
     topology from aerial images,” in 2017 IEEE International Conference              5541–5559, 2022.
     on Computer Vision (ICCV), 2017, pp. 3458–3466.                             [80] Y.-f. Zhang, J. Zheng, W. Jia, W. Huang, L. Li, N. Liu, F. Li, and X. He,
[59] W. Ji, G. Yan, J. Li, Y. Piao, S. Yao, M. Zhang, L. Cheng, and H. Lu,            “Deep rgb-d saliency detection without depth,” IEEE Transactions on
     “Dmra: Depth-induced multi-scale recurrent attention network for rgb-d           Multimedia, vol. 24, pp. 755–767, 2022.
     saliency detection,” IEEE Transactions on Image Processing, vol. 31,        [81] W. Zhang, G.-P. Ji, Z. Wang, K. Fu, and Q. Zhao, “Depth quality-
     pp. 2321–2336, 2022.                                                             inspired feature manipulation for efficient rgb-d salient object detection,”
[60] R. Ju, L. Ge, W. Geng, T. Ren, and G. Wu, “Depth saliency based                  in Proceedings of the 29th ACM international conference on multimedia,
     on anisotropic center-surround difference,” in 2014 IEEE International           2021, pp. 731–740.
     Conference on Image Processing (ICIP), 2014, pp. 1115–1119.                 [82] Z. Zhang, Z. Lin, J. Xu, W.-D. Jin, S.-P. Lu, and D.-P. Fan, “Bilateral
[61] Y. Niu, Y. Geng, X. Li, and F. Liu, “Leveraging stereopsis for saliency          attention network for rgb-d salient object detection,” IEEE Transactions
     analysis,” in 2012 IEEE Conference on Computer Vision and Pattern                on Image Processing, vol. 30, pp. 1949–1961, 2021.
     Recognition, 2012, pp. 454–461.                                             [83] C. Chen, J. Wei, C. Peng, and H. Qin, “Depth-quality-aware salient
[62] H. Peng, B. Li, W. Xiong, W. Hu, and R. Ji, “Rgbd salient object                 object detection,” IEEE Transactions on Image Processing, vol. 30, pp.
     detection: A benchmark and algorithms,” in European conference on                2350–2363, 2021.
     computer vision. Springer, 2014, pp. 92–109.                                [84] X. Wang, S. Li, C. Chen, Y. Fang, A. Hao, and H. Qin, “Data-level
[63] G. Li and C. Zhu, “A three-pathway psychobiological framework of                 recombination and lightweight fusion scheme for rgb-d salient object
     salient object detection using stereoscopic technology,” in 2017 IEEE            detection,” IEEE Transactions on Image Processing, vol. 30, pp. 458–
     International Conference on Computer Vision Workshops (ICCVW),                   471, 2021.
     2017, pp. 3008–3014.                                                        [85] B. Jiang, Z. Zhou, X. Wang, J. Tang, and B. Luo, “cmsalgan: Rgb-d
                                                                                      salient object detection with cross-view generative adversarial networks,”
[64] X. Jin, K. Yi, and J. Xu, “Moadnet: Mobile asymmetric dual-stream
                                                                                      IEEE Transactions on Multimedia, vol. 23, pp. 1343–1353, 2021.
     networks for real-time and lightweight rgb-d salient object detection,”
                                                                                 [86] W. Zhou, Q. Guo, J. Lei, L. Yu, and J.-N. Hwang, “Irfr-net: Interactive
     IEEE Transactions on Circuits and Systems for Video Technology,
                                                                                      recursive feature-reshaping network for detecting salient objects in rgb-d
     vol. 32, no. 11, pp. 7632–7645, 2022.
                                                                                      images,” IEEE Transactions on Neural Networks and Learning Systems,
[65] D.-P. Fan, C. Gong, Y. Cao, B. Ren, M.-M. Cheng, and A. Borji,
                                                                                      pp. 1–13, 2021.
     “Enhanced-alignment measure for binary foreground map evaluation,”
     arXiv preprint arXiv:1805.10421, 2018.
[66] D.-P. Fan, M.-M. Cheng, Y. Liu, T. Li, and A. Borji, “Structure-measure:
     A new way to evaluate foreground maps,” in 2017 IEEE International
     Conference on Computer Vision (ICCV), 2017, pp. 4558–4567.
[67] R. Achanta, S. Hemami, F. Estrada, and S. Susstrunk, “Frequency-tuned
     salient region detection,” in 2009 IEEE Conference on Computer Vision
     and Pattern Recognition, 2009, pp. 1597–1604.
[68] A. Borji, M.-M. Cheng, H. Jiang, and J. Li, “Salient object detection: A                              Kang Yi received the B.S. degree from China
     benchmark,” IEEE Transactions on Image Processing, vol. 24, no. 12,                                   Agricultural University, Beijing, China, in computer
     pp. 5706–5722, 2015.                                                                                  science. He is currently pursuing his Ph.D. degree
[69] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,”                                 with College of Artificial Intelligence from Nankai
     arXiv preprint arXiv:1412.6980, 2014.                                                                 University, Tianjin, China. In addition, he had been
[70] A. Li, Y. Mao, J. Zhang, and Y. Dai, “Mutual information regularization                               a visiting scholar in the Polytechnic University of
     for weakly-supervised rgb-d salient object detection,” IEEE Transactions                              Hong Kong. His research interests include computer
     on Circuits and Systems for Video Technology, vol. 34, no. 1, pp. 397–                                vision and multimedia computing.
     410, 2024.
[71] T. Yang, Y. Wang, L. Zhang, J. Qi, and H. Lu, “Depth-inspired label
     mining for unsupervised rgb-d salient object detection,” in Proceedings
     of the 30th ACM International Conference on Multimedia, 2022, pp.
     5669–5677.
[72] W. Zhou, Y. Zhu, J. Lei, J. Wan, and L. Yu, “Ccafnet: Crossflow and
     cross-scale adaptive fusion network for detecting salient objects in rgb-
     d images,” IEEE Transactions on Multimedia, vol. 24, pp. 2192–2204,
     2022.
[73] Y. Xu, X. Yu, J. Zhang, L. Zhu, and D. Wang, “Weakly supervised rgb-d
                                                                                                           Haoran Tang is now a Ph.D. student at the Hong
     salient object detection with prediction consistency training and active
                                                                                                           Kong Polytechnic University and the Univerity of
     scribble boosting,” IEEE Transactions on Image Processing, vol. 31, pp.
                                                                                                           Technology Sydney. He received B.S. and M.S.
     2148–2161, 2022.
                                                                                                           degrees from the Chongqing University. His research
[74] W. Gao, G. Liao, S. Ma, G. Li, Y. Liang, and W. Lin, “Unified                                         interests include temporal graph learning and data
     information fusion network for multi-modal rgb-d and rgb-t salient                                    mining.
     object detection,” IEEE Transactions on Circuits and Systems for Video
     Technology, vol. 32, no. 4, pp. 2091–2106, 2022.
[75] P. Sun, W. Zhang, H. Wang, S. Li, and X. Li, “Deep rgb-d saliency
     detection with depth-sensitive attention and automatic multi-modal fu-
     sion,” in 2021 IEEE/CVF Conference on Computer Vision and Pattern
     Recognition (CVPR), 2021, pp. 1407–1417.
[76] Z. Liu, M. Hayat, H. Yang, D. Peng, and Y. Lei, “Deep hypersphere
     feature regularization for weakly supervised rgb-d salient object detec-
SUBMITTED TO IEEE TRANSCATION ON MULTIMEDIA                                15

                   Yumeng Li is studying at the College of Artifi-
                   cial Intelligence, Nankai University. Her research
                   interests include computer vision and medical image
                   processing.

                   Jing Xu is a professor at the College of Artificial
                   Intelligence, Nankai University. She received her
                   Ph.D. degree from Nankai University in 2003. She
                   has published more than 100 papers in software en-
                   gineering, software security, and big data analytics.
                   She won the second prize of the Tianjin Science and
                   Technology Progress Award twice in 2017 and 2018,
                   respectively.

                   Jun Zhang received his PhD degree in Electri-
                   cal Engineering from the City University of Hong
                   Kong in 2002. His research activities are mainly
                   in the areas of computational intelligence. Based
                   on his research in evolutionary computation and its
                   applications, Zhang Jun has published more than
                   600 peer-reviewed research papers, of which more
                   than 200 have been published in IEEE Transactions.
                   He currently serves as Associate Editor of IEEE
                   Transactions on Artificial Intelligence and IEEE
                   Transactions on Cybernetics.
