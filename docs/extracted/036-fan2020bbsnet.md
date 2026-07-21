---
source_id: 036
bibtex_key: fan2020bbsnet
title: BBS-Net: RGB-D Salient Object Detection with a Bifurcated Backbone Strategy Network
year: 2020
domain_theme: RGB-D SOD
verified_pdf: 36_BBS-Net.pdf
char_count: 122401
---

IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                           1

                                                                    Bifurcated Backbone Strategy
                                                                for RGB-D Salient Object Detection
                                                              Yingjie Zhai*, Deng-Ping Fan*, Jufeng Yang, Ali Borji, Ling Shao, Fellow, IEEE,
                                                                     Junwei Han, Senior Member, IEEE, and Liang Wang, Fellow, IEEE

                                            Abstract—Multi-level feature fusion is a fundamental topic in              RGB           Ours         DMRA         CPFP         TANet
                                         computer vision. It has been exploited to detect, segment and
arXiv:2007.02713v3 [cs.CV] 18 Aug 2021

                                         classify objects at various scales. When multi-level features meet
                                         multi-modal cues, the optimal feature aggregation and multi-
                                         modal learning strategy become a hot potato. In this paper, we                Depth         GT           PCF          SE           LBE
                                         leverage the inherent multi-modal and multi-level nature of RGB-
                                         D salient object detection to devise a novel cascaded refinement
                                         network. In particular, first, we propose to regroup the multi-
                                         level features into teacher and student features using a bifurcated
                                         backbone strategy (BBS). Second, we introduce a depth-enhanced                RGB           Ours         DMRA         CPFP         TANet
                                         module (DEM) to excavate informative depth cues from the
                                         channel and spatial views. Then, RGB and depth modalities
                                         are fused in a complementary way. Our architecture, named
                                         Bifurcated Backbone Strategy Network (BBS-Net), is simple,                    Depth         GT           PCF          SE           LBE
                                         efficient, and backbone-independent. Extensive experiments show
                                         that BBS-Net significantly outperforms 18 SOTA models on 8
                                         challenging datasets under 5 evaluation measures, demonstrating
                                         the superiority of our approach (∼4% improvement in S-measure
                                         vs. the top-ranked model: DMRA-iccv2019). In addition, we
                                         provide a comprehensive analysis on the generalization ability                Fig. 1. Saliency maps of state-of-the-art (SOTA) CNN-based methods
                                         of different RGB-D datasets and provide a powerful training set               (i.e., DMRA [19], CPFP [21], TANet [18], PCF [22] and Ours) and
                                         for future research.                                                          methods based on handcrafted features (i.e., SE [25] and LBE [26]).
                                                                                                                       Our method generates higher-quality saliency maps and suppresses
                                           Index Terms—RGB-D salient object detection, bifurcated back-                background distractors in challenging scenarios (top: complex back-
                                         bone strategy, multi-level features, cascaded refinement.                     ground; bottom: depth with noise).

                                                                  I. I NTRODUCTION
                                                                                                                       cluttered backgrounds, multiple objects, varying illuminations,

                                         T     HE goal of salient object detection (SOD) is to find
                                               and segment the most visually prominent object(s) in
                                         an image [2], [3]. Over the last decade, SOD has attracted
                                                                                                                       transparent objects, etc) [18]. One of the most important rea-
                                                                                                                       sons behind these failure cases may be the lack of depth infor-
                                                                                                                       mation, which is critical for saliency prediction. For example,
                                         significant attention due to its widespread applications in                   an object with less texture but closer to the camera is usually
                                         object recognition [4], content-based image retrieval [5], image              salient than an object with more texture but farther away.
                                         segmentation [6], image editing [7], video analysis [8], [9], and             Depth maps contain abundant spatial structure and layout
                                         visual tracking [10], [11]. Traditional SOD algorithms [12],                  information [19], providing geometrical cues for improving
                                         [13] are typically based on handcrafted features and fall short               the performance of SOD. Besides, depth information can be
                                         in capturing high-level semantic information (see also [14],                  easily obtained using popular devices, e.g., stereo cameras,
                                         [15]). Recently, convolutional neural networks (CNNs) have                    Kinect and smartphones, which are becoming increasingly
                                         been used for RGB SOD [16], [17], achieving better perfor-                    more ubiquitous. Therefore, various algorithms (e.g., [20],
                                         mance compared to the traditional methods.                                    [21]) have been proposed to solve the SOD problem by
                                            However, the performance of RGB SOD models tends                           combining RGB and depth information (i.e., RGB-D SOD).
                                         to drastically decrease in certain complex scenarios (e.g.,                      To efficiently integrate RGB and depth cues for SOD,
                                                                                                                       researchers have explored different but complementary multi-
                                           *Equal contribution. Listing order is random. Yingjie Zhai, Deng-Ping Fan
                                         and Jufeng Yang are with College of Computer Science, Nankai University.
                                                                                                                       modal and multi-level strategies [22]–[24] and have achieved
                                         Ali Borji is with Primer.AI, SF, USA. Ling Shao is with the Mohamed bin       encouraging results. However, existing RGB-D SOD methods
                                         Zayed University of Artificial Intelligence, Abu Dhabi, UAE, and also with    still have to solve the following challenges:
                                         the Inception Institute of Artificial Intelligence, Abu Dhabi, UAE. Junwei
                                         Han is with School of Automation, Northwestern Polytechnical University,         (1) Effectively aggregating multi-level features. As dis-
                                         China. Liang Wang is with the National Laboratory of Pattern Recognition,     cussed in [16], teacher features contain rich semantic macro
                                         CAS Center for Excellence in Brain Science and Intelligence Technology,       information and can serve as strong guidance for locating
                                         Institute of Automation, Chinese Academy of Sciences, Beijing 100190,
                                         China. A preliminary version of this work has appeared in ECCV 2020 [1].      salient objects, while student features provide affluent micro
                                         Corresponding author: Jufeng Yang (yangjufeng@nankai.edu.cn).                 details that are beneficial for refining object edges. Therefore,
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                               2

current RGB-D SOD methods use either a dedicated aggrega-               Network (BBS-Net) to deal with multiple complicated
tion strategy [19], [21] or a progressive merging process [27],         real-world scenarios in RGB-D SOD. To address the
[28] to leverage multi-level features. However, because they            long-overlooked problem of noise in low-level features
directly fuse multi-level features without considering level-           decreasing the performance of saliency models, we care-
specific characteristics, these operations suffer from the in-          fully explore the characteristics of multi-level features in
herent problem of noisy low-level features [18], [29]. As a             a bifurcated backbone strategy (BBS), i.e., features are
result, several methods are easily confused by the background           split into two groups, as shown in Fig. 2 (b). In this way,
(e.g., first and second rows in Fig. 1).                                noise in student features can be eliminated effectively by
   (2) Excavating informative cues from the depth modality.             the saliency map generated from teacher features.
Previous algorithms usually regard the depth map as a fourth-         • We further introduce a depth-enhanced module
channel input [31], [32] of the original three-channel RGB              (DEM) in BBS-Net to enhance the depth features before
image, or fuse RGB and depth features by simple summa-                  merging them with the RGB features. The DEM module
tion [33], [34] and multiplication [35], [36]. However, these           concentrates on the most informative parts of depth maps
methods treat depth and RGB information from the same                   by two sequential attention operations. We leverage the
perspective and ignore the fact that RGB images capture                 attention mechanism to excavate important cues from the
color and texture, whereas depth maps capture the spatial               depth features of multiple side-out layers. This module
relations among objects. Due to this modality difference, the           is simple but has proven effective for fusing RGB and
above-mentioned simple combination methods are not very                 depth modalities in a complementary way.
efficient. Further, depth maps often have low quality, which          • We conduct a comprehensive comparison with 18
introduces randomly distributed errors and redundancy into              SOTA methods using various metrics (e.g., max F-
the network [37]. For example, the depth map in the last row            measure, MAE, S-measure, max E-measure, and PR
of Fig. 1 is blurry and noisy. As a result, many methods (e.g.,         curves). Experimental results show that BBS-Net outper-
the top-ranked model DMRA [19]) fail to detect the full extent          forms all of these methods on eight public datasets, by
of the salient object.                                                  a large margin. In terms of the predicted saliency maps,
   To address the above issues, we propose a novel Bifurcated           BBS-Net generates maps with sharper edges and fewer
Backbone Strategy Network (BBS-Net) for RGB-D SOD. The                  background distractors compared to existing models.
proposed method exploits multi-level features in a cascaded           • We conduct a number of cross-dataset experiments to
refinement way to suppress distractors in the lower layers.             evaluate the quality of current popular RGB-D datasets
This strategy is based on the observation that teacher features         and introduce a training set with high generalization
provide discriminative semantic information without redun-              ability for fair comparison and future research. Current
dant details [16], [29], which may contribute significantly to          RGB-D methods train their networks using the fixed
eliminating the lower-layer distractors. As shown in Fig. 2             training-test splits of different datasets, without exploring
(b), BBS-Net contains two cascaded decoder stages: (1) Cross-           the difficulties of those datasets. To the best of our
modal teacher features are integrated by the first cascaded             knowledge, we are the first to investigate this important
decoder CD1 to predict an initial saliency map S1 . (2) Student         but overlooked problem in the area of RGB-D SOD.
features are refined by an element-wise multiplication with the       This work is based on our previous conference paper [1] and
initial saliency map S1 and are then aggregated by another         extends it significantly in five ways: 1) We further extend the
cascaded decoder CD2 to produce the final saliency map             approach by designing a depth adapter module, which makes
S2 . To fully capture the informative cues in the depth map        the model contain around 50 percent parameters of the previ-
and improve the compatibility of RGB and depth features,           ous version but with similar performance. 2) We provide more
we further introduce a depth-enhanced module (DEM). This           details and experiments regarding our BBS-Net model, includ-
module exploits the inter-channel and spatial relations of the     ing motivation, feature visualizations, experimental settings,
depth features and discovers informative depth cues.               etc. 3) We investigate several previously unexplored issues,
   Additionally, to obtain reasonable performance in real-world    including cross-dataset generalization ability, post-processing
scenarios, not only an efficient model is needed but also a        methods, failure cases analysis, etc. 4) To further demonstrate
dataset with great generalization ability is required to train     our model performance, we conduct several comprehensive
such model. There are several large-scale RGB-D datasets,          experiments over the recently released dataset, DUT [19].
e.g., NJU2K [38], NLPR [32], STERE [39], SIP [37] and              5) We perform in-depth analyses and draw several novel
DUT [19] with more than 1, 000 image pairs. However,               conclusions which are critical in developing more powerful
researchers have often trained RGB-D models on the fixed           models in the future. We are hopeful that our study will
training set (i.e., 1, 485 images from NJU2K and 700 images        provide deep insights into the underlying design mechanisms
from NLPR). This limits the model’s generation ability in vari-    of RGB-D SOD, and will spark novel ideas. The complete
ous scenarios. Further, they have not studied the generalization   algorithm, benchmark results, and post-processing toolbox are
ability of different datasets and have not proposed powerful       publicly available at https://github.com/zyjwuyan/BBS-Net.
training sets. In this paper, one of our goals is to study this
                                                                                       II. R ELATED W ORKS
problem in detail.                                                 A. Salient Object Detection
   Our main contributions are summarized as follows:                 Over the past several decades, SOD [40]–[42] has gar-
   • We propose a powerful Bifurcated Backbone Strategy            nered significant research interest due to its diverse applica-
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                                            3

                                                                       Student feature Teacher feature
                                                                                                                         FD      Full Decoder
                                                                    In
                                                                                                         CD1    S1      CD1      Cascaded Decoder 1
               In                                           S
         (a)                                        FD           (b)                                                    CD2      Cascaded Decoder 2

                                                                                                                                  Convolutional Block

                                                                                                                S2               Skip Connection
                                                                                                         CD2
                                                                                                                              Element-wise Multiplication
Fig. 2. (a) Existing multi-level feature aggregation methods for RGB-D SOD [18], [19], [21], [22], [27], [28], [30]. (b) In this paper, we adopt a bifurcated
backbone strategy (BBS) to split the multi-level features into student and teacher features. The initial saliency map S1 is utilized to refine the student features
to effectively suppress distractors. Then, the refined features are passed to another cascaded decoder to generate the final saliency map S2 .

tions [43]–[45]. In early years, SOD methods were primarily                          contrast [67], and background prior [68], proposed to compute
based on intrinsic prior knowledge such as center-surround                           saliency by combining both local and global information.
color contrast [46], global region contrast [12], background                            To combine saliency cues from RGB and depth modalities
prior [47] and appearance similarity [48]. However, these                            more effectively, researchers have explored multiple fusion
methods heavily rely on heuristic saliency cues and low-level                        strategies. Some methods [31], [32] process RGB and depth
handcrafted features, thus lacking the guidance of high-level                        images together by regarding depth maps as fourth-channel
semantic information.                                                                inputs (early fusion). This operation is simple but does not
   Recently, to solve this problem, deep learning based meth-                        achieve reliable results, since it disregards the differences
ods [49]–[53] have been explored, exceeding handcrafted                              between the RGB and depth modalities. Therefore, some
feature-based methods in complex scenarios. These deep meth-                         algorithms [33], [36] extract the saliency information from the
ods [54] usually leverage CNNs to extract multi-level multi-                         two modalities separately by first leveraging two backbones to
scale features from RGB images and then aggregate them                               predict saliency maps and then fusing the saliency results (late
to predict the final saliency map. Such multi-level multi-                           fusion). Besides, to enable the RGB and depth modalities to
scale features [55], [56] can help the model better understand                       share benefits, other methods [26], [38] fuse RGB and depth
the contextual and semantic information to generate high-                            features in a middle stage and then produce the corresponding
quality saliency maps. Besides, since image-based SOD may                            saliency maps (middle fusion). Deep models also use the above
be limited in some real-world applications such as video                             three fusion strategies, and our method falls under the middle
captioning [57], autonomous driving [58] and robotic inter-                          fusion category.
action [59], SOD algorithms [8], [9] have also been explored
for video analysis.                                                                  • Deep Models.        Early deep methods [66], [68] compute
   To further overcome the limits of deep models, researchers                        saliency confidence scores by first extracting handcrafted
have also proposed to excavate edge information [60] to guide                        features, and then feeding them to CNNs. However, these
prediction. These methods use an auxiliary boundary loss to                          algorithms need the low-level handcrafted features to be
improve the training and representative ability of segmentation                      manually designed as input, and thus cannot be trained in an
tasks [61]–[63]. With the auxiliary guidance from the edge                           end-to-end manner. More recently, researchers have begun to
information, deep models can predict maps with finer and                             extract deep RGB and depth features using CNNs in a bottom-
sharper edges. In addition to edge guidance, another useful                          up fashion [70]. Unlike handcrafted features, deep features
type of auxiliary information are depth maps, which capture                          contain a lot of contextual and semantic information, and
the spatial distance information. These are the main focus of                        can thus better capture representations of the RGB and depth
this paper.                                                                          modalities. These methods have achieved encouraging results,
                                                                                     which can be attributed to two important aspects of feature
                                                                                     fusion. One is their extraction and fusion of multi-level and
B. RGB-D Salient Object Detection                                                    multi-scale features from different layers, while the other is
                                                                                     the mechanism by which the two different modalities (RGB
• Traditional Models.        Previous algorithms for RGB-D                           and depth) are combined.
SOD mainly rely on extracting handcrafted features [35], [36]                           Various architectures have been designed to effectively
from RGB and depth images. Contrast-based cues, includ-                              integrate the multi-scale features. For example, Liu et al. [27]
ing edge, color, texture and region, are largely utilized by                         obtained saliency map outputs from each side-out features by
these methods to compute the saliency of a local region.                             feeding a four-channel RGB-D image into a single backbone
For example, Desingh et al. [64] adopted the region-based                            (single stream). Chen et al. [22] leveraged two independent
contrast to calculate contrast strengths for the segmented                           networks to extract RGB and depth features respectively, and
regions. Ciptadi et al. [65] used surface normals and color                          then combined them in a progressive merging way (double
contrast to compute saliency. However, the local contrast                            stream). Furthermore, to learn supplementary features, [18]
methods are easily disturbed by high-frequency content [66],                         designed a three-stream network consisting of two modality-
since they mainly rely on the boundaries of salient objects.                         specific streams and a parallel cross-modal distillation stream
Therefore, some algorithms, such as spatial prior [35], global                       to exploit complementary cross-modal information in the
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                                                         4

                                           11×11×2048                  UP×2

                            DEM
                                                                GCM            BConv3                   (a) FCD1
          𝑓5𝑑                       𝑟𝑔𝑏       𝑓5𝑐𝑚                           UP×2
                                   𝑓5                                                                  Cascaded              T1                 S1
                                                                               BConv3

                                                                      UP×4

                                                                                                                                                        352×352×1
          Conv5                         Conv5                                                          Decoder

                                                                                                                           Conv3×3
                                                                                                                            BConv3
                                                                                                          44×44×32                    UP×8
                                           22×22×1024

                            DEM
          𝑓4𝑑                                                   GCM                               C
                                    𝑟𝑔𝑏                𝑓4𝑐𝑚                  UP×2
                                   𝑓4                                          BConv3         UP×2
          Conv4                         Conv4                                                                                                     𝑙𝑐𝑒
                                                                               BConv3           BConv3

                                                                                                                                                        352×352×1 352×352×1
                                           44×44×512
                            DEM

          𝑓3𝑑                                                   GCM                                C
                                  𝑓3
                                    𝑟𝑔𝑏          𝑓3𝑐𝑚                                                                                    G
          Conv3                         Conv3

                                                                                                        88×88×32
                                                                    UP×2              𝑓3𝑐𝑚′
                                                𝑓2𝑐𝑚                                                               (b) T2 PTM                     𝑙𝑐𝑒
                            DEM

          𝑓2𝑑

                                                                                                FCD2
                                    𝑟𝑔𝑏                 88×88×256                     𝑓2𝑐𝑚′

                                                                                                                   Conv1×1

                                                                                                                   Conv1×1

                                                                                                                   Conv1×1
                                   𝑓2

                                                                                                                    TransB

                                                                                                                    TransB
          Conv2                         Conv2                                  UP×4
                                                        88×88×64                                                                                S2
                            DEM

          𝑓1𝑑
                                  𝑓1
                                    rgb                     𝑓1𝑐𝑚                      𝑓1𝑐𝑚′
          Conv1                         Conv1                                                                                        PTM: Progressively
                                                       GCM Global Contextual Module DEM               Depth-Enhanced Module          Transposed Module
                                                                                              BConvN        ConvN×N+BN+ReLU
                    Depth

                                                       C Concatenation                                                               Refinement Flow
                                  RGB

                                                          Element-wise Summation              ConvN         Convolutional Block Data Flow
       352×352×1                   352×352×3              Element-wise Multiplication         TransB         Conv+BN+ReLU+DeConv+BN+ReLU+Residual

Fig. 3. Architecture of our BBS-Net. Feature Extraction: ‘Conv1’∼‘Conv5’ denote different layers from ResNet-50 [69]. Multi-level features (f1d ∼ f5d )
from the depth branch are enhanced by the DEM and are then fused with features (i.e., f1rgb ∼ f5rgb ) from the RGB branch. Stage 1: cross-modal teacher
features (f3cm ∼ f5cm ) are first aggregated by the cascaded decoder (a) to produce the initial saliency map S1 . Stage 2: Then, student features (f1cm ∼ f3cm )
are refined by the initial saliency map S1 and are integrated by another cascaded decoder to predict the final saliency map S2 . See § III for details.

bottom-up feature extraction process (three streams). Depth                           B. Bifurcated Backbone Strategy (BBS)
maps are sometimes low-quality and may thus contain signifi-
cant noise or misleading information, which greatly decreases                           Our cascaded refinement mechanism leverages the rich
the performance of SOD models. To address this issue, Zhao et                         semantic information in high-level cross-modal features to
al. [21] proposed a contrast-enhanced network to improve the                          suppress background distractors. To support such a feat, we
quality of depth maps using the contrast prior. Fan et al. [37]                       devise a bifurcated backbone strategy (BBS). It divides the
designed a depth depurator unit to evaluate the quality of                            multi-level cross-modal features into two groups, i.e., G1 =
depth maps and filter out the low-quality ones automatically.                         {Conv1, Conv2, Conv3} and G2 ={Conv3, Conv4, Conv5},
Three recent works have explored uncertainty [71], depth                              where Conv3 is the split point. The original multi-scale infor-
prediction [72] and a joint learning strategy [73] for saliency                       mation is well preserved by each group.
detection and achieved reasonable performance. There were
also some concurrent works published in recent top confer-                            • Cascaded Refinement Mechanism.                To effectively lever-
ences (e.g., ECCV [74]–[76]). Discussing these works in detail                        age the characteristics of the features in the two groups’
is beyond the scope of this article. Please refer to the online                       features, we train the network using a cascaded refinement
benchmark (http://dpfan.net/d3netbenchmark/) and the latest                           mechanism. This mechanism first generates an initial saliency
survey [77] for more details.                                                         map with three cross-modal teacher features (i.e., G2 ) and then
                                                                                      enhances the details of the initial saliency map S1 with three
                       III. P ROPOSED M ETHOD                                         cross-modal student features (i.e., G1 ), which are refined by
                                                                                      the initial saliency map. This is based on the observation that
A. Overview                                                                           high-level features contain rich semantic information that helps
   Current popular RGB-D SOD models directly integrate                                locate salient objects, while low-level features provide micro-
multi-level features using a single decoder (Fig. 2 (a)). In                          level details that are beneficial for refining the boundaries. In
contrast, the network flow of the proposed BBS-Net (Fig.                              other words, by exploring the characteristics of the multi-level
3) explores a bifurcated backbone strategy. In § III-B, we                            features, this strategy can efficiently suppress noise in low-
first detail the proposed bifurcated backbone strategy with                           level cross-modal features, and can produce the final saliency
the cascaded refinement mechanism. Then, to fully excavate                            map through a progressive refinement.
informative cues from the depth map, we introduce a new                                  Specifically, we first merge RGB and depth features pro-
depth-enhanced module in § III-C. Additionally, we design a                           cessed by the DEM to obtain the cross-modal features
depth adapter module to further improve the efficiency of the                         {ficm ; i = 1, 2, ..., 5}. In stage one, the three cross-modality
model in § III-D.                                                                     teacher features (i.e., f3cm , f4cm , f5cm ) are aggregated by the
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                   5

first cascaded decoder, which is denoted as:                           not of the same scale. represents the element-wise multipli-
                                                                       cation, and Conv(·) represents the standard 3×3 convolution
               S1 = T1 FCD1 (f3cm , f4cm , f5cm ) ,
                                                   
                                                                (1)
                                                                       operation. Then, the updated features are integrated by a
where FCD1 is the first cascaded decoder, S1 is the initial            progressive concatenation strategy to produce the output:
saliency map, and T1 represents two simple convolutional                       h      0
                                                                                                     h
                                                                                                         gcm0
                                                                                                                     
                                                                                                                            gcm0
                                                                                                                                   ii
layers that transform the channel number from 32 to 1. In              S = T fkgcm ; Conv FU P fk+1           ; Conv FU P (fk+2  )       ,
stage two, we leverage the initial saliency map S1 to refine                                                                        (6)
the three cross-modal student features, which is defined as:           where S is the predicted saliency map, [x; y] denotes the
                        0                                              concatenation operation of x and y, and k ∈ {1, 3}. In the first
                   ficm = ficm + ficm       S1 ,                (2)    stage, T denotes two sequential convolutional layers (i.e., T1 ),
          0
where ficm (i ∈ {1, 2, 3}) represents the refined features and         while, for the second stage, it represents the PTM module (i.e.,
   denotes the element-wise multiplication. After that, the three      T2 ). The scale of the output of the second decoder is 88×88,
refined student features are aggregated by another decoder             which is 1/4 of the ground-truth (352×352), so directly
followed by a progressively transposed module (PTM), which             upsampling the output to the size of the ground-truth will
is formulated as:                                                      lose some details. To address this issue, we propose a simple
                                0      0     0
                                                                      yet effective progressively transposed module (PTM, Fig. 3
             S2 = T2 FCD2 (f1cm , f2cm , f3cm ) ,             (3)      (b)) to generate the final predicted map (S2 ) in a progressive
                                                                       upsampling way. It consists of two residual-based transposed
where FCD2 is the second cascaded decoder, S2 denotes the
                                                                       blocks [79] and three sequential 1 × 1 convolutions. Each
final saliency map, and T2 represents the PTM module.
                                                                       residual-based transposed block contains a 3 × 3 convolution
• Cascaded Decoder.           After computing the two groups           and a residual-based transposed convolution.
of multi-level cross-modal features ({ficm , fi+1cm    cm
                                                    , fi+2 }, i ∈         Note that the proposed cascaded refinement mechanism
{1, 3}), which are a fusion of the RGB and depth features from         is different from the recent refinement strategies CRN [80],
multiple layers, we need to efficiently leverage the multi-scale       SRM [81], R3Net [82], and RFCN [17] in its usage of the
multi-level information in each group to carry out the cascaded        initial map and multi-level features. The obvious difference
refinement. Therefore, we introduce a light-weight cascaded            and advantage of the proposed design is that our model
decoder [29] to integrate the two groups of multi-level cross-         only requires one round of saliency refinement to produce a
modal features. As shown in Fig. 3 (a), the cascaded decoder           good saliency map, while CRN, SRM, R3Net, and RFCN all
consists of three global context modules (GCM) and a simple            need more iterations, which increases both the training time
feature aggregation strategy. The GCM is refined from the              and computational resources. Besides, the proposed cascaded
RFB module [78]. Specifically, it contains an additional branch        mechanism is also different from CPD [29] in that it exploits
to enlarge the receptive field and a residual connection [69] to       both the details in student features and the semantic infor-
preserve the information. The GCM module thus includes four            mation in teacher features, while suppressing the noise in the
parallel branches. For all of these branches, a 1×1 convolution        student features at the same time.
is first applied to reduce the channel size to 32. Then, for
the k th (k ∈ {2, 3, 4}) branch, a convolution operation with          C. Depth-Enhanced Module (DEM)
a kernel size of 2k − 1 and dilation rate of 1 is applied.
This is followed by another 3 × 3 convolution operation with              To effectively fuse the RGB and depth features, two main
the dilation rate of 2k − 1. We aim to excavate the global             problems need to be solved: a) the compatibility of RGB
contextual information from the cross-modal features. Next,            and depth features needs to be improved due to the intrinsic
the outputs of the four branches are concatenated together             modality difference, and b) the redundancy and noise in low-
and a 3×3 convolution operation is then applied to reduce              quality depth maps must be reduced. Inspired by [83], we
the channel number to 32. Finally, the concatenated features           design a depth-enhanced module (DEM) to address the issues
form a residual connection with the input features. The GCM            by improving the compatibility of multi-modal features and
module operation in the two cascaded decoders is denoted by:           excavating informative cues from the depth features.
                                                                          Specifically, let firgb , fid represent the feature maps of the
                       figcm = FGCM (fi ).                      (4)     th
                                                                       i (i ∈ 1, 2, ..., 5) side-out layer from the RGB and depth
                                                                       branches, respectively. As shown in Fig. 3, each DEM is added
To further improve the representations of cross-modal features,
                                                                       before each side-out feature map from the depth branch to
we leverage a pyramid multiplication and concatenation fea-
                                                                       enhance the compatibility of the depth features. This side-
ture aggregation strategy to aggregate the cross-modal features
                                                                       out process improves the saliency representation of depth
({figcm , fi+1
            gcm    gcm
                , fi+2 }, i ∈ {1, 3}). As illustrated in Fig. 3 (a),
                                                                       features and, at the same time, preserves the multi-level multi-
first, each refined feature figcm is updated by multiplying it
                                                                       scale information. The fusion process of the two modalities is
with all higher-level features:
                                                                       depicted as:
              0
                                                         
         figcm = figcm Πkk=i+1 max
                                    Conv FU P (fkgcm ) ,         (5)                      ficm = firgb + FDEM (fid ),                 (7)

in which i ∈ {1, 2, 3}, kmax = 3 or i ∈ {3, 4, 5}, kmax = 5.           where ficm denotes the cross-modal features of the ith layer.
FU P represents the upsampling operation if the features are           The DEM module contains a sequential channel attention op-
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                              6

          RGB                                                      depth image are two different modalities, i.e., RGB image
                        －          BConv3
                                                                   contains color, structure, and semantic information while the
                                                                   depth image includes the spatial distance information. Thus a
                                            BConv3                 naive sharing-weight mechanism of the two-branch backbones
                                                       Depth
          Depth                                        Output      cannot be suitable to extract the multi-modal features. To solve
                        BConv3
                                                                   this problem, we design a depth adapter module (DAM) to
                                                                   consider the modality difference of the RGB image and depth
                Element-wise     Element-wise
                                                  － Element-wise   image. The same backbone can be suitable to extract two-
                 Summation       Multiplication      Subtraction
                                                                   modality features without decreasing much performance.
           BConv3 Conv3×3+BN+ReLU                                     The whole architecture of the DAM is shown in Fig. 4. Let
                                                                   Irgb and Idepth denote the input RGB and depth image pair,
Fig. 4.   Architecture of the depth adapter module (DAM).
                                                                   respectively. We first calculate the modality difference Idif by,
                                                                                    Idif = Conv(Irgb − Idepth ),               (11)
eration and a spatial attention operation, which are formulated
as:                                                              where Idepth is broadcast to the same dimension as Irgb .
                FDEM (fid ) = Satt Catt (fid ) ,            (8)    Such an operation can make the model understand the explicit
                                                                   difference between the depth image and the RGB image. Then
in which Catt (·) and Satt (·) represent the spatial and channel   the adapted depth output is computed by:
attention operations, respectively. More specifically, the chan-                                                     
                                                                       0
nel attention is implemented as:                                     Idif = Conv Conv(Idepth ) + Conv(Idepth ) ∗ Idif . (12)
                                         
                 Catt (f ) = M Pmax (f ) ⊗ f,                (9)   In the efficient version of BBS-Net, the backbones of the
                                                                   two branches share parameters. When calculating the depth
where Pmax (·) denotes the global max pooling operation            features, the depth image is first fed to the DAM module
for each feature map, M(·) represents a multi-layer (two-          to obtain the adapted depth information and is then fed to
layer) perceptron, f denotes the input feature map, and ⊗          the backbone to extract features. To further reduce model
is the multiplication by the dimension broadcast. The spatial      parameters, we also remove the last progressively transposed
attention is denoted as:                                           module (which makes negligible performance degradation) in
                                        
               Satt (f ) = Conv Rmax (f )    f,         (10)       the efficient version of BBS-Net.

where Rmax (·) is the global max pooling operation for each        E. Implementation Details
point in the feature map along the channel axis. The proposed
depth enhanced module is different from previous RGB-D             • Training Loss.      Let H and W denote the height and
algorithms, which fuse the multi-level cross-modal features        width of the input images. Given the input RGB image X ∈
by direct concatenation [18], [22], [28], enhance the multi-       RH×W×3 and its corresponding depth map D ∈ RH×W×1 ,
level depth features by a simple convolutional layer [19] or       our model predicts an initial saliency map S1 ∈ [0, 1]H×W×1
improve the depth map by contrast prior [21]. To the best          and a final saliency map S2 ∈ [0, 1]H×W×1 . Let G ∈
of our knowledge, we are the first to introduce the attention      {0, 1}H×W×1 denote the binary ground-truth saliency map.
mechanism to excavate informative cues from depth features in      We jointly optimize the two cascaded stages by defining the
multiple side-out layers. Our experiments (see Tab. VI and Fig.    total loss:
8) demonstrate the effectiveness of our approach in improving
the compatibility of multi-modal features.                                     L = α`ce (S1 , G) + (1 − α)`ce (S2 , G),        (13)
   Besides, the spatial and channel attention mechanisms are
                                                                   in which `ce represents the binary cross entropy loss [21] and
different from the operation proposed in [83]. Based on the
                                                                   α ∈ [0, 1] controls the trade-off between the two parts of the
fact that SOD aims at finding the most prominent objects in
                                                                   losses. The `ce is computed as:
an image, we only leverage a single global max pooling [84]
to excavate the most critical cues in depth features, which                 `ce (S, G) = G log S + (1 − G) log(1 − S),         (14)
reduces the complexity of the module.
                                                                   where S is the predicted saliency map.
D. Improve the efficiency of BBS-Net.                              • Training and Test Protocol.        We use PyTorch [85] to
   Note that the above proposed BBS-Net leverages two back-        implement our model on a single 1080Ti GPU. Parameters of
bones, without sharing weights, to extract RGB features and        the backbone network (ResNet-50 [69]) are initialized from
depth features. Such a design can make the model extract           the model pre-trained on ImageNet [86]. Other parameters
discriminative RGB features and depth features, respectively,      are initialized using the default PyTorch settings. We discard
but also introduces more parameters, leading to a suboptimal       the last pooling and fully connected layers of ResNet-50 and
solution for lightweight applications. However, making the         leverage each middle output of the five convolutional blocks
two branches share weights can cause a big degradation of          as the side-out feature maps. The two branches do not share
the performance. It may be because the RGB image and the           weights and the only difference between them is that the depth
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                             7

Fig. 5. PR Curves of the proposed model and 18 SOTA algorithms over six datasets. Dots on the curves represent the value of precision and recall at
the maximum F-measure.

branch has the input channel number set to one. Note for the                                          TABLE I
efficient version BBS-Net> , the two branches share weights,                 P ERFORMANCE OF DIFFERENT MODELS ON THE DUT [19] DATASET.
                                                                           M ODELS ARE TRAINED AND TESTED ON THE DUT USING THE PROPOSED
and the depth images are first fed to the depth adapter module                         TRAINING AND TEST SETS SPLIT FROM [19].
to reduce the modality difference. The Adam algorithm [87] is
                                                                                  #                   Dataset              DUT [19]
used to optimize our model, the betas are set to 0.9 and 0.99,                             Method                 Sα ↑   max Fβ ↑ max Eξ ↑
and the weight decay is set to 0. We set the initial learning rate                                 MB [90]        .607     .577     .691
                                                                             Handcrafted          LHM [32]        .568     .659     .767
to 1e-4 and divide it by 10 every 60 epochs. The gradients are                                  DESM [35]         .659     .668     .733
                                                                                                DCMC [91]         .499     .406     .712
clipped into [−0.5, 0.5] to make the training stable. The input                                  CDCP [36]        .687     .633     .794
                                                                                                DMRA [19]         .888     .883     .927
RGB and depth images are resized to 352 × 352 for both the                   Deep-based         A2dele [92]       .886     .892     .929
training and test phases. We augment all the training images                                       SSF [93]       .916     .924     .951
                                                                                              BBS-Net (ours)      .920     .927     .955
using multiple strategies (i.e., random flipping, rotating, and
border clipping). It takes about ten hours to train the model                                             TABLE II
with a mini-batch size of 10 for 150 epochs. Our experiments                M ULTIPLE COMPARISONS OF BBS-N ET AND BBS-N ET> . T HE
                                                                                                     >
show that the model is robust to the hyper-parameter α. Thus,              EFFICIENT VERSION BBS-N ET HAS ONLY AROUND 50 PERCENT
                                                                                           PARAMETERS OF BBS-N ET.
we set α to 0.5 (i.e., same importance for the two losses). In
the test phase, the predicted maps are upsampled to the same
dimension of ground truth by the bilinear interpolation and are                   #              Parameters (M)          FLOPs (G)         fps
then normalized to [0,1].                                                       BBS-Net              49.77                 31.40          24.32
                                                                               BBS-Net>              25.96                 25.26          25.54

               IV. E XPERIMENTS AND R ESULTS
A. Experimental Settings                                                   SIP [37] consists of 1, 000 image pairs captured by a smart
                                                                           phone with a resolution of 992 × 744, using a dual camera.
• Datasets.     We conduct our experiments on eight chal-                  DUT [19] includes 1200 images from multiple challenging
lenging RGB-D SOD benchmark datasets: NJU2K [38],                          scenes (e.g., transparent objects, multiple objects, complex
NLPR [32], STERE [39], DES [35], LFSD [88], SSD [89],                      backgrounds and low-intensity environments).
SIP [37] and DUT [19]. NJU2K [38] is the largest RGB-
D dataset containing 1, 985 image pairs. NLPR [32] consists                • Training/Testing.      We follow the same settings as [19],
of 1, 000 image pairs captured by a standard Microsoft Kinect              [22] for fair comparison. In particular, the training set contains
with a resolution of 640×480. STERE [39] is the first stereo-              1, 485 samples from the NJU2K dataset and 700 samples
scopic photo collection, containing 1, 000 images downloaded               from the NLPR dataset. The test set consists of the remaining
from the Internet. DES [35] is a small-scale RGB-D dataset                 images from NJU2K (500) and NLPR (300), and the whole
that includes 135 indoor image pairs. LFSD [88] contains                   of STERE (1, 000), DES, LFSD, SSD and SIP. As for the
60 image pairs from indoor scenes and 40 image pairs from                  recent proposde DUT [19] dataset, following [19], we adopt
outdoor scenes. SSD [89] includes 80 images picked from                    the same training data of DUT, NJU2K, and NLPR to train
three stereo movies with both indoor and outdoor scenes.                   the compared deep models (i.e., DMRA [19], A2dele [92],
The collected images have a high resolution of 960 × 1, 080.               SSF [93], and our BBS-Net) and test the performance on the
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                       8

                                                                TABLE III
  Q UANTITATIVE COMPARISON OF MODELS USING S- MEASURE (Sα ), MAX F- MEASURE (maxFβ ), MAX E- MEASURE (maxEξ ) AND MAE (M ) SCORES
  ON SEVEN PUBLIC DATASETS . ↑ (↓) DENOTES THAT THE HIGHER ( LOWER ) THE SCORE , THE BETTER . > DENOTES THE EFFICIENT VERSION OF BBS-Net.

                                  Hand-crafted-features-Based Models                         CNNs-Based Models            BBS-Net
Data

              Metric LHM CDB DESM GP CDCP ACSD LBE DCMC MDSF SE DF AFNet CTMF MMCI PCF TANet CPFP DMRA Ours Ours
                      [32] [94] [35] [95] [36] [38] [26] [91]         [96] [25] [66] [30] [70]   [23] [22] [18] [21] [19] >
                Sα ↑ .514 .624 .665 .527 .669 .699 .695 .686         .748 .664 .763 .772 .849   .858 .877 .878 .879 .886 .916 .921
NLPR NJU2K

             maxFβ ↑ .632 .648 .717 .647 .621 .711 .748 .715         .775 .748 .650 .775 .845   .852 .872 .874 .877 .886 .918 .920
             maxEξ ↑ .724 .742 .791 .703 .741 .803 .803 .799         .838 .813 .696 .853 .913   .915 .924 .925 .926 .927 .948 .949
                M ↓ .205 .203 .283 .211 .180 .202 .153 .172          .157 .169 .141 .100 .085   .079 .059 .060 .053 .051 .038 .035
                Sα ↑ .630 .629 .572 .654 .727 .673 .762 .724         .805 .756 .802 .799 .860   .856 .874 .886 .888 .899 .925 .930
             maxFβ ↑ .622 .618 .640 .611 .645 .607 .745 .648         .793 .713 .778 .771 .825   .815 .841 .863 .867 .879 .909 .918
             maxEξ ↑ .766 .791 .805 .723 .820 .780 .855 .793         .885 .847 .880 .879 .929   .913 .925 .941 .932 .947 .959 .961
                M ↓ .108 .114 .312 .146 .112 .179 .081 .117          .095 .091 .085 .058 .056   .059 .044 .041 .036 .031 .026 .023
                Sα ↑ .562 .615 .642 .588 .713 .692 .660 .731         .728 .708 .757 .825 .848   .873 .875 .871 .879 .835 .905 .908
DES STERE

             maxFβ ↑ .683 .717 .700 .671 .664 .669 .633 .740         .719 .755 .757 .823 .831   .863 .860 .861 .874 .847 .898 .903
             maxEξ ↑ .771 .823 .811 .743 .786 .806 .787 .819         .809 .846 .847 .887 .912   .927 .925 .923 .925 .911 .940 .942
                M ↓ .172 .166 .295 .182 .149 .200 .250 .148          .176 .143 .141 .075 .086   .068 .064 .060 .051 .066 .043 .041
                Sα ↑ .578 .645 .622 .636 .709 .728 .703 .707         .741 .741 .752 .770 .863   .848 .842 .858 .872 .900 .930 .933
             maxFβ ↑ .511 .723 .765 .597 .631 .756 .788 .666         .746 .741 .766 .728 .844   .822 .804 .827 .846 .888 .921 .927
             maxEξ ↑ .653 .830 .868 .670 .811 .850 .890 .773         .851 .856 .870 .881 .932   .928 .893 .910 .923 .943 .965 .966
                M ↓ .114 .100 .299 .168 .115 .169 .208 .111          .122 .090 .093 .068 .055   .065 .049 .046 .038 .030 .022 .021
                Sα ↑ .553 .515 .716 .635 .712 .727 .729 .753         .694 .692 .783 .738 .788   .787 .786 .801 .828 .839 .859 .864
LFSD

             maxFβ ↑ .708 .677 .762 .783 .702 .763 .722 .817         .779 .786 .813 .744 .787   .771 .775 .796 .826 .852 .855 .858
             maxEξ ↑ .763 .871 .811 .824 .780 .829 .797 .856         .819 .832 .857 .815 .857   .839 .827 .847 .863 .893 .896 .901
                M ↓ .218 .225 .253 .190 .172 .195 .214 .155          .197 .174 .145 .133 .127   .132 .119 .111 .088 .083 .076 .072
                Sα ↑ .566 .562 .602 .615 .603 .675 .621 .704         .673 .675 .747 .714 .776   .813 .841 .839 .807 .857 .858 .882
SSD

             maxFβ ↑ .568 .592 .680 .740 .535 .682 .619 .711         .703 .710 .735 .687 .729   .781 .807 .810 .766 .844 .827 .859
             maxEξ ↑ .717 .698 .769 .782 .700 .785 .736 .786         .779 .800 .828 .807 .865   .882 .894 .897 .852 .906 .894 .919
                M ↓ .195 .196 .308 .180 .214 .203 .278 .169          .192 .165 .142 .118 .099   .082 .062 .063 .082 .058 .058 .044
                Sα ↑ .511 .557 .616 .588 .595 .732 .727 .683         .717 .628 .653 .720 .716   .833 .842 .835 .850 .806 .876 .879
SIP

             maxFβ ↑ .574 .620 .669 .687 .505 .763 .751 .618         .698 .661 .657 .712 .694   .818 .838 .830 .851 .821 .880 .883
             maxEξ ↑ .716 .737 .770 .768 .721 .838 .853 .743         .798 .771 .759 .819 .829   .897 .901 .895 .903 .875 .919 .922
                M ↓ .184 .192 .298 .173 .224 .172 .200 .186          .167 .164 .185 .118 .139   .086 .071 .075 .064 .085 .056 .055

test set of DUT. Please refer to Tab. I for more details.              which is suitable for real-time applications. In terms of param-
                                                                       eters, BBS-Net> contains only around 50 percent parameters
• Evaluation Metrics.       We employ five widely used met-            of the BBS-Net (i.e., 25.96M vs. 49.77M), but its performance
rics, including S-measure (Sα ) [97], E-measure (Eξ ) [98], F-         is similar to the BBS-Net and also superior to other compared
measure (Fβ ) [99], mean absolute error (MAE), and precision-          methods (as shown in the last two columns in Tab. III). It
recall (PR) curves to evaluate various methods. Evaluation             means that BBS-Net> can process more images in the same
code: http://dpfan.net/d3netbenchmark/.                                time (with a larger batch size) for real-world applications.
                                                                          There are three popular backbone models used in deep
B. Comparison with SOTAs                                               RGB-D models (i.e., VGG-16 [100], VGG-19 [100] and
                                                                       ResNet-50 [69]). To further validate the effectiveness of the
• Contenders. We compare the proposed BBS-Net with ten                 proposed method, we provide performance comparisons us-
algorithms based on handcrafted features [25], [26], [32], [35],       ing different backbones in Tab. IV. We find that ResNet-
[36], [38], [91], [94]–[96] and eight methods [18], [19], [21]–        50 performs best among the three backbones, and VGG-19
[23], [30], [66], [70] that use deep learning. We train and test       and VGG-16 have similar performances. Besides, the pro-
these methods using their default settings. For the methods            posed method exceeds the SOTA methods (e.g., TANet [18],
without released source codes, we compare with their reported          CPFP [21], and DMRA [19]) with any of the backbones.
results.
                                                                       • Visual Comparison. Fig. 6 provides examples of maps
• Quantitative Results.        As shown in Tab. I, Tab. III,           predicted by our method and several SOTA algorithms. Vi-
our method outperforms all algorithms based on handcrafted             sualizations cover simple scenes (a) and various challenging
features as well as SOTA CNN-based methods by a large                  scenarios, including small objects (b), multiple objects (c),
margin, in terms of all four evaluation metrics (i.e., S-measure       complex backgrounds (d), and low contrast scenes (e).
(Sα ), F-measure (Fβ ), E-measure (Eξ ) and MAE (M )). Per-                First, the first row of (a) shows an easy example. The flower
formance gains over the best compared algorithms (ICCV’19              in the foreground is evident in the original RGB image, but
DMRA [19] and CVPR’19 CPFP [21]) are (2.5% ∼ 3.5%,                     the depth map is of low quality and contains some misleading
0.7% ∼ 3.9%, 0.8% ∼ 2.3%, 0.009 ∼ 0.016) for the metrics               information. The SOTA algorithms, such as DMRA and CPFP,
(Sα , maxFβ , maxEξ , M ) on seven challenging datasets. The           fail to predict the whole extent of the salient object due to the
PR curves of different methods on various datasets are shown           interference from the depth map. Our method can eliminate the
in Fig. 5. It can be easily deduced from the PR curves that            side-effects of the depth map by utilizing the complementary
our method (i.e., solid red lines) outperforms all the SOTA            depth information more effectively. Second, two examples of
algorithms.                                                            small objects are shown in (b). Despite the handle of the teapot
   In terms of speed, BBS-Net achieves 24.32 fps on a single           in the first row being tiny, our method can accurately detect
GTX 1080Ti GPU (batch size of one), as shown in Tab. II,               it. Third, we show two examples with multiple objects in an
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                            9

                 RGB       Depth      GT        Ours      DMRA       CPFP         TANet      PCF       MMCI      CTMF     AFNet        DF

     (a)
    Simple
    Scene

     (b)
    Small
   Objects

     (c)
  Multiple
  Objects

     (d)
  Complex
 Background

     (e)
     Low
   Contrast
    Scene

Fig. 6.    Qualitative visual comparison of our model versus eight SOTA models.

                                                          TABLE IV
P ERFORMANCE COMPARISON USING DIFFERENT BACKBONE MODELS . W E EXPERIMENT WITH MULTIPLE POPULAR BACKBONE MODELS USED IN RGB-D
                                SOD, INCLUDING VGG-16 [100], VGG-19 [100] AND R ES N ET-50 [69].

              Models           NJU2K [38]      NLPR [32]        STERE [39]          DES [35]        LFSD [88]      SSD [89]         SIP [37]
                              Sα ↑   M ↓      Sα ↑   M ↓       Sα ↑   M ↓         Sα ↑    M ↓      Sα ↑   M ↓    Sα ↑    M ↓      Sα ↑    M ↓
  TANet (VGG-16) [18]         .878    .060    .886   .041      .871    .060       .858    .046     .801   .111   .839    .063     .835    .075
  CPFP (VGG-16) [21]          .879    .053    .888   .036      .879    .051       .872    .038     .828   .088   .807    .082     .850    .064
  Ours (VGG-16)               .916    .039    .923   .026      .896    .046       .908    .028     .845   .080   .858    .055     .874    .056
  DMRA (VGG-19) [19]          .886    .051    .899   .031      .835    .066       .900    .030     .839   .083   .857    .058     .806    .085
  Ours (VGG-19)               .918    .037    .925   .025      .901    .043       .915    .026     .852   .074   .855    .056     .878    .054
  D3Net (ResNet-50) [37]      .900    .041    .912   .030      .899    .046       .898    .031     .825   .095   .857    .058     .860    .063
  Ours (ResNet-50)            .921    .035    .930   .023      .908    .041       .933    .021     .864   .072   .882    .044     .879    .055

image in (c). Our method locates all salient objects in the                 7. ‘Low3’ means that we only integrate the low-level features
image. It segments the objects more accurately and generates                (Conv1∼3) using the decoder without the refinement from the
sharper edges compared to other algorithms. Even though the                 initial map. Low-level features contain abundant details that
depth map in the first row of (c) lacks clear information,                  are beneficial for refining the object edges, but at the same time
our algorithm predicts the salient objects correctly. Fourth,               introduce a lot of background distraction. Integrating only
(d) shows two examples with complex backgrounds. Here,                      low-level features produces inadequate results and generates
our method produces reliable results, while other algorithms                many distractors (e.g., the example in Fig. 7). ‘High3’ only
confuse the background as a salient object. Finally, (e) presents           integrates the high-level features (Conv3∼5) to predict the
two examples in which the contrast between the object and the               saliency map. Compared with low-level features, high-level
background is low. Many algorithms fail to detect and segment               features contain more semantic information. As a result, they
the entire extent of the salient object. Our method produces                help locate the salient objects and preserve edge information.
satisfactory results by suppressing background distractors and              Thus, integrating high-level features leads to better results.
exploring the informative cues from the depth map.                          ‘All5’ aggregates features from all five levels (Conv1∼5)
                                                                            directly, using a single decoder for training and testing. It
                                                                            achieves comparable results with the ’High3’ but may include
C. Ablation Study                                                           background noise introduced by the low-level features (see
                                                                            column ‘All5’ in Fig. 7). ‘BBS-NoRF’ indicates that we
• Analysis of Different Aggregation Strategies.          To
                                                                            directly remove the refinement flow of our model. This leads to
validate the effectiveness of our cascaded refinement mech-
                                                                            poor performance. ‘BBS-RH’ is a reverse refinement strategy
anism, we conduct several experiments to explore different
                                                                            to our cascaded refinement mechanism, where teacher features
aggregation strategies. Results are shown in Tab. V and Fig.
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                                     10

                                                                TABLE V
 C OMPARISON OF FEATURE AGGREGATION STRATEGIES . 1: O NLY AGGREGATING THE LOW- LEVEL FEATURES (Conv1∼3), 2: O NLY AGGREGATING THE
    HIGH - LEVEL FEATURES (Conv3∼5), 3: D IRECTLY INTEGRATING ALL FIVE - LEVEL FEATURES (Conv1∼5) BY A SINGLE DECODER , 4: O UR MODEL
   WITHOUT THE REFINEMENT FLOW, 5: H IGH - LEVEL FEATURES (Conv3∼5) ARE FIRST REFINED BY THE INITIAL MAP AGGREGATED BY LOW- LEVEL
   FEATURES (Conv1∼3) AND ARE THEN INTEGRATED TO GENERATE THE FINAL SALIENCY MAP, AND 6: O UR CASCADED REFINEMENT MECHANISM .

  #         Settings         NJU2K [38]         NLPR [32]           STERE [39]         DES [35]         LFSD [88]         SSD [89]           SIP [37]
                            Sα ↑   M ↓         Sα ↑   M ↓          Sα ↑   M ↓        Sα ↑    M ↓      Sα ↑    M ↓       Sα ↑    M ↓       Sα ↑     M ↓
  1      Low 3 levels       .881    .051       .882   .038         .832    .070      .853    .044     .779    .110      .805    .080      .760     .108
  2      High 3 levels      .902    .042       .911   .029         .886    .048      .912    .026     .845    .080      .850    .058      .833     .073
  3      All 5 levels       .905    .042       .915   .027         .891    .045      .901    .028     .845    .082      .848    .060      .839     .071
  4       BBS-NoRF          .893    .050       .904   .035         .843    .072      .886    .039     .804    .105      .839    .069      .843     .076
  5        BBS-RH           .913    .040       .922   .028         .881    .054      .919    .027     .833    .085      .872    .053      .866     .063
  6     BBS-RL (ours)       .921    .035       .930   .023         .908    .041      .933    .021     .864    .072      .882    .044      .879     .055

                                                              TABLE VI
  A BLATION ANALYSIS OF OUR BBS-Net. ‘BM’ = BASE MODEL . ‘CA’ = CHANNEL ATTENTIO . ‘SA’ = SPATIAL ATTENTION . ‘PTM’ = PROGRESSIVELY
                                                        TRANSPOSED MODULE .

 #             Settings               NJU2K [38]         NLPR [32]         STERE [39]      DES [35]        LFSD [88]        SSD [89]            SIP [37]
       BM     CA     SA      PTM      Sα ↑  M ↓         Sα ↑   M ↓         Sα ↑  M ↓     Sα ↑   M ↓       Sα ↑   M ↓      Sα ↑    M ↓         Sα ↑    M ↓
 1      X                             .908  .045        .918   .029        .882  .055    .917    .027     .842   .083     .862    .057        .864    .066
 2      X      X                      .913  .042        .922   .027        .896  .048    .923    .025     .840   .086     .855    .057        .868    .063
 3      X              X              .912  .045        .918   .029        .891  .054    .914    .029     .855   .083     .872    .054        .869    .063
 4      X      X       X              .919  .037        .928   .026        .900  .045    .924    .024     .861   .074     .873    .052        .869    .061
 5      X      X       X         X    .921  .035        .930   .023        .908  .041    .933    .021     .864   .072     .882    .044        .879    .055

      RGB       GT         Low3      High3      All5 BBS-RH BBS-RL                                          TABLE VII
                                                                                   E FFECTIVENESS ANALYSIS OF THE CASCADED DECODER IN TERMS OF
                                                                                              THE S- MEASURE (Sα ) ON SEVEN DATASETS .

                                                                                           Methods NJU2K
                                                                                                    [38]
                                                                                                         NLPR STERE DES SSD LFSD
                                                                                                          [32]  [39] [35] [89] [88]
                                                                                                                                                      SIP
                                                                                                                                                      [37]
Fig. 7.      Visual comparison of aggregation strategies. ‘Low3’ only              Element-wise sum     .915   .925     .897   .925    .868    .856   .880
integrates low-level features (Conv1∼3), while ‘High3’ aggregates high-level       Cascaded decoder     .921   .930     .908   .933    .882    .864   .879
features (Conv3∼5) for predicting the saliency map. ‘All5’ combines all five-
level features directly for prediction. ‘BBS-RH/BBS-RL’ denotes that high-
level/low-level features are first refined by the initial map aggregated by the                                TABLE VIII
low-level/high-level features and are then integrated to predict the final map.    H YPER - PARAMETER α ANALYSIS ON THE NJU2K DATASET. W E
                                                                                   DO NOT REPORT THE RESULT FOR α = 1, BECAUSE ITS LOSS OF
                                                                                                 THE FINAL PREDICTED MAP IS 0.
      RGB       GT          #1        #2         #3        #4         #5
                                                                                       α         0   0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9
                                                                                   NJU2K (Sα ) .918 .925 .923 .919 .924 .923 .920 .923 .922 .924
                                                                                  NJU2K (MAE) .037 .034 .034 .036 .033 .034 .035 .034 .035 .033

Fig. 8. Analysis of gradually adding various modules. The first two
columns are the RGB and ground-truth images, respectively. ‘#’ denotes the
corresponding row of Tab. VI.                                                     greatly improved on all datasets, compared to the BM. We can
                                                                                  easily conclude from the ‘#2’, ‘#3’ and ‘#4’ columns in Fig.
                                                                                  8 that the spatial attention and channel attention mechanisms
(Conv3∼5) are first refined by the initial map aggregated                         in DEM allow the model to focus on the informative parts
by low-level features (Conv1∼3) and are then integrated                           of the depth features, which results in better suppression of
to generate the final saliency map. It performs worse than                        background clutter. Finally, we add a progressively transposed
the proposed mechanism (BBS-RL), because noise in low-                            block before the second decoder to gradually upsample the
level features cannot be effectively suppressed in this reverse                   feature map to the same resolution as the ground truth. The
refinement strategy. Besides, compared to ‘All5’, our method                      results in the fifth row of Tab. VI and the ’#5’ column of Fig.
fully utilizes the features at different levels, and thus achieves                8 show that the ‘PTM’ achieves impressive performance gains
significant performance improvement (i.e., the last row in Tab.                   on all datasets and generates sharper edges with finer details.
V) with fewer background distractors and sharper edges.                              To further analyze the effectiveness of the cascaded decoder,
                                                                                  we experiment with changing it to an element-wise summation
• Impact of Different Modules.             To validate the ef-                    mechanism. That is to say, we first change the features from
fectiveness of the different modules in the proposed BBS-                         different layers to the same dimension using 1 × 1 convolution
Net, we conduct various experiments, as shown in Tab. VI                          and upsampling operation and then fuse them by element-
and Fig. 8. The base model (BM) is our BBS-Net without                            wise summation. Experimental results in Tab. VII show that
additional modules (i.e., CA, SA, and PTM). Note that the BM                      the cascaded decoder achieves comparable results on SIP, and
alone performs better than the SOTA methods over almost all                       outperforms the element-wise sum on the other six datasets,
datasets, as shown in Tab. III and Tab. VI. Adding the channel                    which demonstrates its effectiveness.
attention (CA) and spatial attention (SA) modules enhances the
performance on most of the datasets (see the results shown in                     • Hyper-parameter Analysis.     We conduct an experiment
the second and third rows of Tab. VI). When we combine the                        to discuss the settings of α. As shown in Tab. VIII, the
two modules (the fourth row in Tab. VI), the performance is                       performance (Sα and MAE) is about the same for different
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                               11

                             TABLE IX                                      RGB       Depth        GT           (a)       (b)        (c)      Ours
 E FFECTIVENESS ANALYSIS OF THE DEPTH ADAPTER MODULE IN TERMS
   OF THE S- MEASURE (Sα ) ON SEVEN DATASETS . > REPRESENTS THE
 EFFICIENT VERSION OF BBS-Net, WHERE THE TWO BACKBONES SHARE
                            PARAMETERS .

                                                                        Fig. 9. Feature visualization. Here, (a), (b), and (c) are the average RGB
             Settings NJU2K
                       [38]
                            NLPR STERE DES SSD LFSD SIP
                             [32]  [39] [35] [89] [88] [37]             feature, depth feature and cross-modal feature of the Conv3 layer. To visualize
BBS-Net> (w/o DAM)     .905   .922   .899   .928 .856     .841   .849   them, we average the feature maps along their channel axis to obtain the
 BBS-Net> (w/ DAM)     .916   .925   .905   .930 .858     .859   .876   visualization map. ‘Ours’ refers to the BBS-Net (w/ depth).

                               TABLE X                                                             TABLE XI
S- MEASURE (Sα ) COMPARISON WITH SOTA RGB SOD METHODS . ‘ W / O          P ERFORMANCE COMPARISON (MAE) OF DIFFERENT POST- PROCESSING
   DEPTH ’ AND ‘ W / DEPTH ’ REPRESENT TRAINING AND TESTING THE          STRATEGIES ON SEVEN DATASETS . T HE LAST COLUMN IS THE TIME FOR
PROPOSED METHOD WITHOUT / WITH THE DEPTH INFORMATION (i.e., THE          THE POST- PROCESSING METHODS TO OPTIMIZE EACH IMAGE . S EE § V-B
    INPUTS OF THE DEPTH BRANCH ARE OR ARE NOT SET TO ZEROS ).                                     FOR DETAILS .

                                                                         Strategy     NJU2K NLPR STERE DES LFSD SSD                        SIP time
            Methods NJU2K
                     [38]
                          NLPR STERE DES LFSD SSD SIP
                           [32]  [39] [35] [88] [89] [37]
                                                                                        [38]  [32]  [39] [35] [88] [89]                    [37] ms
                                                                         BBS-Net       .035  .023  .041 .021 .072 .044                    .055   -
      PiCANet [101]    .847   .834   .868   .854   .761   .832     -     BBS-Net+ADP .050    .024  .049 .018 .072 .053                    .055 1.46
        PAGRN [50]     .829   .844   .851   .858   .779   .793     -     BBS-Net+Ostu .030   .020  .036 .018 .066 .039                    .051 0.99
         R3Net [82]    .837   .798   .855   .847   .797   .815     -     BBS-Net+CRF .030    .020  .035 .019 .065 .038                    .051 450.8
           CPD [29]    .894   .915   .902   .897   .815   .839   .859
        PoolNet [16]   .887   .900   .880   .873   .787   .773   .861
 BBS-Net (w/o depth)   .914   .925   .915   .912   .836   .855   .875        RGB          GT         BBS-Net    BBS-Net+ADP BBS-Net+Ostu BBS-Net+CRF
  BBS-Net (w/ depth)   .921   .930   .908   .933   .864   .882   .879

values of α, thus we simply set it to 0.5 to balance the weight         Fig. 10. Visual effects of different post-processing methods. We explore
between the losses of the initial map and the final map.                three methods, including the adaptive threshold cut (‘ADP’ in the paper),
                                                                        Ostu’s method and the popular algorithm of conditional random fields (CRF).
• Effectiveness Analysis of the Depth Adapter Module.
To demonstrate the effectiveness of the proposed depth adapter          9, depth feature (b) has high activation on the object border.
module (DAM), we conduct an experiment in Tab. IX. As                   Thus, cross-modal feature (c) has clearer borders compared
shown in the table, BBS-Net> (w/ DAM) performs better than              with the original RGB feature (a).
BBS-Net> (w/o DAM) on seven datasets, especially on the
dataset of NJU2K, LFSD, and SIP. The DAM can model the                  B. Analysis of Post-processing Methods
modality difference between the RGB image and depth image,
reduces the gap between them. Thus the same backbone is                    According to [102]–[104], the predicted saliency maps can
more suitable to extract two different modality features.               be further refined by post-processing methods. This may be
                                                                        useful to sharpen the salient edges and suppress the back-
                                                                        ground response. We conduct several experiments to study the
                        V. D ISCUSSION                                  effects of various post-processing methods, including the adap-
A. Utility of Depth Information                                         tive threshold cut (i.e., the threshold is defined as the double
   To explore whether depth information can really contribute           of the mean value of the saliency map), Ostu’s method [105],
to the performance of SOD, we conduct two experiments,                  and conditional random field (CRF) [106]. The performance
results of which are shown in Tab. X. On the one hand, we               comparisons of the post-processing methods in terms of MAE
compare the proposed method with five SOTA RGB SOD                      are shown in Tab. XI, while a visual comparison is provided
methods (i.e., PiCANet [101], PAGRN [50], R3Net [82],                   in Fig. 10.
CPD [29], and PoolNet [16]) by neglecting the depth in-                    From the results, we draw the following conclusions. First,
formation. We train and test CPD and PoolNet using the                  the three post-processing methods all make the salient edges
same training and test sets as our model. For other methods,            sharper, as shown in the fourth to sixth columns in Fig. 10.
we use the published results from [19]. It is clear that the            Second, both Ostu and CRF help reduce the MAE effectively,
proposed methods (i.e., BBS-Net (w/ depth)) can significantly           as shown in Tab. XI. This is possibly because they can suppress
exceed SOTA RGB SOD methods thanks to depth information.                the background noise. As shown in Fig. 10, Ostu and CRF can
On the other hand, we train and test the proposed method                significantly reduce the background noise, while the adaptive
without using the depth information by setting the inputs of the        threshold operation further expands the background blur from
depth branch to zero (i.e., BBSNet (w/o depth)). Comparing              the original results of BBS-Net. Further, in terms of overall
the results of the last two rows in the table, we find that             results, CRF performs the best, while the adaptive threshold
depth information effectively improves the performance of the           algorithm is the worst. Ostu performs worse than CRF, because
proposed model (especially over the small datasets, i.e., DES,          it cannot always fully eliminate the background noise (e.g., the
LFSD, and SSD).                                                         fifth and sixth columns in Fig. 10).
   The two experiments together demonstrate the benefits of
the depth information for SOD. Depth map serves as prior                C. Failure Case Analysis
knowledge and provides spatial distance information and con-              We illustrate six representative failure cases in Fig. 11.
tour guidance to detect salient objects. For example, in Fig.           The failure examples are divided into four categories. In the
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                 12

        (a)      (b)        (c)        (d)        (e)      (f)      of the whole dataset. Therefore, adding more difficult exam-
                                                                    ples to the training data could help mitigate the failure cases.
RGB

                                                                    Finally, depth maps may sometimes introduce misleading
                                                                    information, such as in column (d). Considering how to exploit
Depth

                                                                    salient cues from the RGB image to suppress the noise in the
                                                                    depth map could be a promising solution.
GT

                                                                    D. Cross-Dataset Generalization Analysis
                                                                       For a deep model to obtain reasonable performance in
Ours

                                                                    real-world scenarios, it not only requires an efficient design
                                                                    but must also be trained on a high-quality dataset with a
                                                                    great generalization power. A good dataset usually contains
Fig. 11. Some representative failure cases of the model.            sufficient images, with all types of variations that occur in
                                                                    reality, so that deep models trained on it can generalize well to
                                                                    the real world. In the area of RGB-D SOD, there are several
first category, the model either misses the salient object or       large-scale datasets (i.e., NJU2K, NLPR, STERE, SIP, and
detects it imperfectly. For example, in column (a), our model       DUT), with around 1, 000 training images.
fails to detect the salient object even when the depth map
has clear boundaries. This is because the salient object has        • Single Dataset Generalization Analysis.                Here, we
the same texture and content layout as the background in            conduct cross-dataset generalization experiments on the above-
the RGB image. Thus, the model cannot find the salient              mentioned five datasets to measure their generalization abil-
object based only on the borders. In column (b), our method         ity. To make fair comparisons among multiple datasets, we
cannot fully segment the transparent salient objects, since the     balance the datasets with equal number of training samples.
background has low contrast, and the depth map lacks useful         Specifically, we randomly choose 700 image pairs in each
information. The second situation is that the model identifies      dataset for training, and the remaining images are used for
the background as the salient part. For example, the lanterns in    testing. We then retrain the proposed model on a single
column (c) have a similar color to the background wallpaper,        training set, and test it on all four test sets. The results
which confuses the model into thinking that the wallpaper is        are summarized in Tab. XII. ‘Self’ represents the results
the salient object. Besides, the background of the RGB image        of training and testing on the same dataset. ‘Mean Others’
in column (d) is complex and thus our model does not detect         indicates the average performance on all test sets except ‘self’.
the complete salient objects. The third type of failure case is     ‘Drop’ means the (percent) drop from ‘Self’ to ‘Mean Others’.
when an image contains several separate salient objects. In this    First, it can be seen from the table that NJU2K and DUT
case, our model may not detect them all. As shown in column         are the hardest datasets since their ‘Mean Others’ of column
(e), with five salient objects in the RGB images, the model         ‘NJU2K’ and ‘DUT’ are significantly lower than the other
fails to detect the two objects that are far from the camera.       three datasets. This may be because the two datasets include
This may be because the model tends to consider the objects         multiple challenging scenes (e.g., transparent objects, multiple
that are closer to the camera more salient. The final case is       objects, complex backgrounds, etc). Second, STERE has the
when salient objects are occluded by non-salient ones. Note         best generalization ability, because the average drop of Sα and
that in column (f), the car is occluded by two ropes in front       Fβ is lowest among all five datasets. Besides, SIP generalizes
of the camera. Here our model predicts the ropes as salient         worst (i.e., the drop is the largest among all five datasets), since
objects.                                                            it mainly focuses on a single person or multiple persons in the
   Most of these failure cases can be attributed to interference    wild. We also notice that the score of the SIP column (‘Mean
information from the background (e.g., color, contrast, and         Others’) is the highest. This is likely because the quality of the
content). We propose some ideas that may be useful for solving      depth maps captured by the Huawei Mate10 is higher than that
these failure cases. The first is to introduce some human-          produced by traditional devices. Finally, none of the models
designed prior knowledge, such as providing a boundary              trained with a single dataset perform best over all test sets.
that can approximately distinguish the foreground from the          Thus, we further explore training on different combinations
background. Leveraging such prior knowledge, the model may          of datasets with the aim of building a dataset with a strong
better capture the characteristics of the background and salient    generalization ability for future research.
objects. This strategy may contribute significantly to solving
the failure cases especially for columns (a) and (b). Besides,      • Dataset Combination for Generalization Improvement.
the depth map can also be seen as a type of prior knowledge for     According to the results in Tab. XII, the model trained on
this task. Thus, some failure cases (i.e., (b), (c), and (e)) may   the SIP dataset does not generalize well to other datasets,
be solved when a high-quality depth map is available. Second,       so we discard it. We thus select four relatively large-scale
we find that in the current RGB-D datasets, the image pairs         datasets, i.e., NJU2K, NLPR, STERE, and DUT, to conduct
for challenging scenarios (e.g., complex backgrounds, low-          our multi-dataset training experiments. As shown in Tab. XIII,
contrast backgrounds, transparent objects, multiple objects,        we consider all possible training combinations of these four
shielded objects, and small objects) constitute a small fraction    datasets and test the models on all available test sets. From
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                                 13

                                                         TABLE XII
     P ERFORMANCE COMPARISON WHEN TRAINING WITH DIFFERENT DATASETS . T HE NUMBER IN PARENTHESES DENOTES THE NUMBER OF THE
                               CORRESPONDING TRAINING AND TEST IMAGES . S EE § V-D FOR DETAILS .

          Test   NJU2K (1285)   NLPR (300)      STERE (300)      SIP (229)      DUT (500)             Self         Mean Others            Drop ↓
 Train           Sα ↑   Fβ ↑    Sα ↑ Fβ ↑       Sα ↑ Fβ ↑      Sα ↑ Fβ ↑       Sα ↑ Fβ ↑         Sα ↑ Fβ ↑         Sα ↑ Fβ ↑           Sα       Fβ
 NJU2K (700)     .902   .894    .834  .795      .864   .846    .802    .782    .741   .691       .902      .894    .810  .779        10.2% 12.9%
  NLPR (700)     .712   .689    .919  .903      .876   .882    .883    .881    .795   .779       .919      .903    .817  .808        11.2% 10.5%
 STERE (700)     .779   .741    .897  .868      .915   .913    .900    .900    .724   .731       .915      .913    .825  .810         9.8%    11.3%
     SIP (700)   .436   .325    .618  .528      .534   .479    .963    .972    .423   .303       .963      .972    .503  .409        47.8% 57.9%
   DUT (700)     .751   .777    .808  .761      .736   .764    .801    .802    .887   .877       .887      .877    .774  .776        12.7% 11.5%
  Mean Others    .670   .633    .789  .738      .753   .743    .847    .841    .671   .626         -         -       -     -            -        -

                                                                    TABLE XIII
P ERFORMANCE COMPARISON WHEN TRAINING WITH DIFFERENT COMBINATIONS OF MULTIPLE DATASETS . ‘NJ’, ‘NL’, ‘ST’, ‘SI’ AND ‘DU’ REPRESENT
 NJU2K, NLPR, STERE, SIP AND DUT, RESPECTIVELY. T HE NUMBER IN PARENTHESES DENOTES THE NUMBER OF CORRESPONDING TRAINING AND
       TEST IMAGES . T HE NUMBER OF TRAINING IMAGES FOR EACH DATASET IS 700. T HE TRAINING AND TEST SETS WILL BE AVAILABLE AT:
                HTTPS :// DRIVE . GOOGLE . COM / DRIVE / FOLDERS /1UYG YG 50-0 Y 7 I 21 T WREVM C B PAT QPF P S R 0? USP = SHARING .

           Test          NJ (1285)      NL (300)       ST (300)      DES (135)      LFSD (80)       SSD (80)       SI (229)       DU (500)
     Train           Sα ↑ Fβ ↑ M ↓ Sα ↑ Fβ ↑ M ↓ Sα ↑ Fβ ↑ M ↓ Sα ↑ Fβ ↑ M ↓ Sα ↑ Fβ ↑ M ↓ Sα ↑ Fβ ↑ M ↓ Sα ↑ Fβ ↑ M ↓ Sα ↑ Fβ ↑ M ↓
       NJ+NL (1,400) .911 .905 .039 .926 .916 .025 .899 .898 .044 .934 .932 .019 .865 .862 .070 .861 .836 .054 .890 .893 .048 .799 .748 .095
        NJ+ST (1,400) .913 .909 .038 .885 .859 .040 .916 .912 .035 .927 .910 .022 .853 .836 .078 .869 .848 .054 .885 .882 .052 .729 .719 .118
       NJ+DU (1,400) .906 .893 .043 .852 .802 .050 .875 .854 .053 .884 .859 .037 .861 .854 .070 .862 .839 .053 .834 .825 .075 .905 .903 .041
       NL+ST (1,400) .781 .748 .097 .930 .919 .024 .919 .920 .032 .942 .938 .019 .672 .645 .161 .774 .722 .090 .895 .894 .047 .836 .819 .070
      NL+DU (1,400) .777 .771 .104 .923 .908 .023 .878 .882 .052 .940 .936 .019 .717 .728 .135 .801 .774 .091 .886 .888 .054 .905 .903 .040
       ST+DU (1,400) .821 .794 .082 .893 .863 .036 .917 .914 .034 .940 .935 .020 .762 .734 .125 .777 .736 .092 .907 .910 .039 .913 .914 .037
   NJ+NL+ST (2,100) .913 .910 .038 .923 .904 .027 .922 .924 .033 .943 .939 .018 .865 .858 .072 .853 .818 .056 .902 .905 .043 .816 .780 .088
   NJ+NL+DU (2,100) .911 .905 .041 .924 .909 .027 .902 .901 .043 .942 .939 .018 .865 .856 .067 .866 .838 .051 .894 .897 .048 .916 .915 .036
   NJ+ST+DU (2,100) .910 .903 .041 .890 .867 .039 .923 .923 .031 .932 .918 .021 .859 .851 .073 .863 .838 .055 .896 .899 .046 .917 .916 .035
   NL+ST+DU (2,100) .825 .808 .079 .924 .911 .026 .919 .920 .033 .946 .944 .017 .751 .732 .125 .797 .758 .082 .901 .905 .043 .916 .911 .036
NJ+NL+ST+DU (2,800) .912 .905 .039 .932 .917 .024 .921 .920 .033 .946 .942 .018 .864 .856 .070 .858 .829 .054 .903 .905 .042 .917 .913 .037

the results in the table, we draw the following conclusions.            depth-enhanced module to excavate the informative cues from
First, more training examples do not necessarily lead to                the depth features in the channel and spatial views, in order
better performance on some test sets. For example, although             to improve the cross-modal compatibility when merging RGB
‘NJ+NL+ST’, ‘NJ+NL+DU’ and ‘NJ+NL+ST+DU’ contain                        and depth features. Experiments on eight challenging datasets
external training sets, unlike ‘NJ+NL’, they perform similarly          demonstrate that BBS-Net outperforms 18 SOTA models, by
with ‘NJ+NL’ on the test set of ‘NL’. Second, including the             a large margin, under multiple evaluation metrics. Finally,
NJU2K dataset is important for the model to generalize well             we conduct a comprehensive analysis of the existing RGB-
to small datasets (i.e., LFSD, SSD). The model trained using            D datasets and introduce a powerful training set with a strong
the combinations without NJU2K (i.e., ‘NL+ST’ ‘NL+DU’,                  generalization ability for future research.
‘ST+DU’ and ‘NL+ST+DU’) all obtain low F-measure values
(less than 0.8) on the LFSD and SSD test sets. In contrast,                                           R EFERENCES
including ‘NJ’ in the training sets increases the F-measures on
the LFSD and SSD datasets by over 0.05. Finally, including                [1] D.-P. Fan, Y. Zhai, A. Borji, J. Yang, and L. Shao, “BBS-Net: RGB-
                                                                              D Salient Object Detection with a Bifurcated Backbone Strategy
more examples in the training sets can improve the stability                  Network,” in ECCV, 2020, pp. 275–292.
of the model, as it allows diverse scenarios to be taken into             [2] A. Borji, M.-M. Cheng, H. Jiang, and J. Li, “Salient object detection:
consideration. Thus, the model trained on ‘NJ+NL+ST+DU’,                      A benchmark,” IEEE TIP, vol. 24, no. 12, pp. 5706–5722, 2015.
                                                                          [3] W. Wang, Q. Lai, H. Fu, J. Shen, H. Ling, and R. Yang, “Salient object
which has the most examples, obtains the best, or are very                    detection in the deep learning era: An in-depth survey,” IEEE TPAMI,
close to the best, performance. Due to the limited size of                    2021.
current RGB-D datasets, it is hard for a model trained using              [4] M.-M. Cheng, Y. Liu, W. Lin, Z. Zhang, P. L. Rosin, and P. H. S.
                                                                              Torr, “BING: binarized normed gradients for objectness estimation at
a single dataset to perform well under various scenarios.                     300fps,” CVM, vol. 5, no. 1, pp. 3–20, 2019.
Thus, we recommend training a model using a combination                   [5] M.-M. Cheng, Q. Hou, S. Zhang, and P. L.Rosin, “Intelligent visual
of datasets with diverse examples to avoid model over-fitting                 media processing: When graphics meets vision,” JCST, vol. 32, no. 1,
                                                                              pp. 110–121, 2017.
issues. To promote the development of RGB-D SOD, we hope                  [6] W. Wang, J. Shen, R. Yang, and F. Porikli, “Saliency-aware video object
more challenging RGB-D datasets with diverse examples and                     segmentation,” IEEE TPAMI, vol. 40, no. 1, pp. 20–33, 2017.
high-quality depth maps can be proposed in the future.                    [7] M.-M. Cheng, F.-L. Zhang, N. J. Mitra, X. Huang, and S.-M. Hu,
                                                                              “Repfinder: Finding approximately repeated scene elements for image
                                                                              editing,” TOG, vol. 29, no. 4, pp. 83:1–83:8, 2010.
                       VI. C ONCLUSION                                    [8] D.-P. Fan, W. Wang, M.-M. Cheng, and J. Shen, “Shifting more
                                                                              attention to video salient object detection,” in CVPR, 2019, pp. 8554–
   In this paper, we present a Bifurcated Backbone Strategy                   8564.
Network (BBS-Net) for the RGB-D SOD. To effectively sup-                  [9] P. Yan, G. Li, Y. Xie, Z. Li, C. Wang, T. Chen, and L. Lin, “Semi-
                                                                              supervised video salient object detection using pseudo-labels,” in ICCV,
press the intrinsic distractors in low-level cross-modal features,            2019, pp. 7284–7293.
we propose to leverage the characteristics of multi-level cross-         [10] A. Borji, S. Frintrop, D. N.Sihite, and L. Itti, “Adaptive object tracking
modal features in a cascaded refinement way: low-level fea-                   by learning background context,” in CVPRW, 2012, pp. 23–30.
                                                                         [11] S. Hong, T. You, S. Kwak, and B. Han, “Online tracking by learning
tures are refined by the initial saliency map that is produced by             discriminative saliency map with convolutional neural network,” in
the high-level cross-modal features. Besides, we introduce a                  ICML, 2015, pp. 597–606.
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                                    14

[12] M.-M. Cheng, N. J. Mitra, X. Huang, P. H. S. Torr, and S.-M. Hu,          [41] R. Achanta, S. Hemami, F. Estrada, and S. Susstrunk, “Frequency-tuned
     “Global contrast based salient region detection,” IEEE TPAMI, vol. 37,         salient region detection,” in CVPR, 2009, pp. 1597–1604.
     no. 3, pp. 569–582, 2015.                                                 [42] D.-P. Fan, M.-M. Cheng, J.-J. Liu, S.-H. Gao, Q. Hou, and A. Borji,
[13] D. Zhang, D. Meng, and J. Han, “Co-saliency detection via a self-              “Salient objects in clutter: Bringing salient object detection to the
     paced multiple-instance learning framework,” IEEE TPAMI, vol. 39,              foreground,” in ECCV, 2018, pp. 186–202.
     no. 5, pp. 865–878, 2016.                                                 [43] G. Li and Y. Yu, “Deep contrast learning for salient object detection,”
[14] A. Borji and L. Itti, “State-of-the-art in visual attention modeling,”         in CVPR, 2016, pp. 478–487.
     IEEE TPAMI, vol. 35, no. 1, pp. 185–207, 2012.                            [44] P. Zhang, D. Wang, H. Lu, H. Wang, and B. Yin, “Learning uncertain
[15] A. Borji, “Saliency prediction in the deep learning era: Successes and         convolutional features for accurate saliency detection,” in ICCV, 2017,
     limitations,” IEEE TPAMI, pp. 679–700, 2019.                                   pp. 212–221.
[16] J.-J. Liu, Q. Hou, M.-M. Cheng, J. Feng, and J. Jiang, “A simple          [45] X. Zhao, Y. Pang, L. Zhang, H. Lu, and L. Zhang, “Suppress and
     pooling-based design for real-time salient object detection,” in CVPR,         balance: A simple gated network for salient object detection,” in ECCV,
     2019, pp. 3917–3926.                                                           2020, pp. 35–51.
[17] L. Wang, L. Wang, H. Lu, P. Zhang, and X. Ruan, “Salient object           [46] L. Itti, C. Koch, and E. Niebur, “A model of saliency-based visual
     detection with recurrent fully convolutional networks,” IEEE TPAMI,            attention for rapid scene analysis,” IEEE TPAMI, vol. 20, no. 11, pp.
     vol. 41, no. 7, pp. 1734–1746, 2018.                                           1254–1259, 1998.
[18] H. Chen and Y. Li, “Three-stream attention-aware network for RGB-         [47] G. Li and Y. Yu, “Visual saliency based on multiscale deep features,”
     D salient object detection,” IEEE TIP, vol. 28, no. 6, pp. 2825–2835,          in CVPR, 2015, pp. 5455–5463.
     2019.                                                                     [48] M.-M. Cheng, J. Warrell, W.-Y. Lin, S. Zheng, V. Vineet, and N. Crook,
[19] Y. Piao, W. Ji, J. Li, M. Zhang, and H. Lu, “Depth-induced multi-scale         “Efficient salient region detection with soft image abstraction,” in
     recurrent attention network for saliency detection,” in ICCV, 2019, pp.        ICCV, 2013, pp. 1529–1536.
     7254–7263.                                                                [49] S. Chen, X. Tan, B. Wang, H. Lu, X. Hu, and Y. Fu, “Reverse attention-
[20] N. Li, J. Ye, Y. Ji, H. Ling, and J. Yu, “Saliency detection on light          based residual network for salient object detection,” IEEE TIP, vol. 29,
     field,” IEEE TPAMI, vol. 39, no. 8, pp. 1605–1616, 2016.                       pp. 3763–3776, 2020.
[21] J.-X. Zhao, Y. Cao, D.-P. Fan, M.-M. Cheng, X.-Y. Li, and L. Zhang,       [50] X. Zhang, T. Wang, J. Qi, H. Lu, and G. Wang, “Progressive attention
     “Contrast prior and fluid pyramid integration for RGBD salient object          guided recurrent network for salient object detection,” in CVPR, 2018,
     detection,” in CVPR, 2019, pp. 3927–3936.                                      pp. 714–722.
[22] H. Chen and Y. Li, “Progressively complementarity-aware fusion            [51] J. Su, J. Li, Y. Zhang, C. Xia, and Y. Tian, “Selectivity or invariance:
     network for RGB-D salient object detection,” in CVPR, 2018, pp.                Boundary-aware salient object detection,” in ICCV, 2019, pp. 3799–
     3051–3060.                                                                     3808.
[23] H. Chen, Y. Li, and D. Su, “Multi-modal fusion network with multi-        [52] L. Zhang, J. Wu, T. Wang, A. Borji, G. Wei, and H. Lu, “A multistage
     scale multi-path and cross-modal interactions for RGB-D salient object         refinement network for salient object detection,” IEEE TIP, vol. 29,
     detection,” IEEE TCYBERNETICS, vol. 86, pp. 376–385, 2019.                     pp. 3534–3545, 2020.
[24] G. Li, Z. Liu, L. Ye, Y. Wang, and H. Ling, “Cross-Modal Weighting        [53] H. Li, G. Chen, G. Li, and Y. Yu, “Motion guided attention for video
     Network for RGB-D Salient Object Detection,” in ECCV, 2020, pp.                salient object detection,” in ICCV, 2019, pp. 7274–7283.
     665–681.                                                                  [54] P. Zhang, D. Wang, H. Lu, H. Wang, and X. Ruan, “Amulet: Aggre-
[25] J. Guo, T. Ren, and J. Bei, “Salient object detection for RGB-D image          gating multi-level convolutional features for salient object detection,”
     via saliency evolution,” in IEEE ICME, 2016, pp. 1–6.                          in ICCV, 2017, pp. 202–211.
[26] D. Feng, N. Barnes, S. You, and C. McCarthy, “Local background            [55] B. Wang, Q. Chen, M. Zhou, Z. Zhang, X. Jin, and K. Gai, “Progressive
     enclosure for RGB-D salient object detection,” in CVPR, 2016, pp.              feature polishing network for salient object detection,” in AAAI, 2020,
     2343–2350.                                                                     pp. 12 128–12 135.
[27] Z. Liu, S. Shi, Q. Duan, W. Zhang, and P. Zhao, “Salient object           [56] J. Wei, S. Wang, and Q. Huang, “F3net: Fusion, feedback and focus
     detection for RGB-D image by single stream recurrent convolution               for salient object detection,” in AAAI, 2020, pp. 123 221–12 328.
     neural network,” Neurocomputing, vol. 363, pp. 46–57, 2019.               [57] Y. Pan, T. Yao, H. Li, and T. Mei, “Video captioning with transferred
[28] C. Zhu, X. Cai, K. Huang, T. H. Li, and G. Li, “Pdnet: Prior-model             semantic attributes,” in CVPR, 2017, pp. 984–992.
     guided depth-enhanced network for salient object detection,” in IEEE      [58] Z. Zhang, S. Fidler, and R. Urtasun, “Instance-level segmentation for
     ICME, 2019, pp. 199–204.                                                       autonomous driving with deep densely connected mrfs,” in CVPR,
[29] Z. Wu, L. Su, and Q. Huang, “Cascaded partial decoder for fast and             2016, pp. 669–677.
     accurate salient object detection,” in CVPR, 2019, pp. 3907–3916.         [59] N. Xu, B. L. Price, S. Cohen, J. Yang, and T. S. Huang, “Deep
[30] N. Wang and X. Gong, “Adaptive fusion for RGB-D salient object                 interactive object selection,” in CVPR, 2016, pp. 373–381.
     detection,” IEEE Access, vol. 7, pp. 55 277–55 284, 2019.                 [60] S. Xie and Z. Tu, “Holistically-nested edge detection,” IJCV, vol. 125,
[31] R. Cong, J. Lei, H. Fu, Q. Huang, X. Cao, and N. Ling, “HSCS:                  no. 1-3, pp. 3–18, 2017.
     Hierarchical sparsity based co-saliency detection for RGBD images,”       [61] Y. Zhuge, G. Yang, P. Zhang, and H. Lu, “Boundary-guided feature
     IEEE TMM, vol. 21, no. 7, pp. 1660–1671, 2019.                                 aggregation network for salient object detection,” IEEE SPL, vol. 25,
[32] H. Peng, B. Li, W. Xiong, W. Hu, and R. Ji, “RGBD salient object               no. 12, pp. 1800–1804, 2018.
     detection: a benchmark and algorithms,” in ECCV, 2014, pp. 92–109.        [62] J.-X. Zhao, J.-J. Liu, D.-P. Fan, Y. Cao, J. Yang, and M.-M. Cheng,
[33] X. Fan, Z. Liu, and G. Sun, “Salient region detection for stereoscopic         “EGNet: Edge guidance network for salient object detection,” in ICCV,
     images,” in DSP, 2014, pp. 454–458.                                            2019, pp. 8779–8788.
[34] Y. Fang, J. Wang, M. Narwaria, P. Le Callet, and W. Lin, “Saliency        [63] Z. Wu, L. Su, and Q. Huang, “Stacked cross refinement network for
     detection for stereoscopic images,” IEEE TIP, vol. 23, no. 6, pp. 2625–        edge-aware salient object detection,” in ICCV, 2019, pp. 7264–7273.
     2636, 2014.                                                               [64] K. Desingh, K. Krishna, D. Rajanand, and C. Jawahar, “Depth really
[35] Y. Cheng, H. Fu, X. Wei, J. Xiao, and X. Cao, “Depth enhanced                  matters: Improving visual salient region detection with depth,” in
     saliency detection method,” in ICIMCS, 2014, pp. 23–27.                        BMVC, 2013, pp. 1–11.
[36] C. Zhu, G. Li, W. Wang, and R. Wang, “An innovative salient object        [65] A. Ciptadi, T. Hermans, and J. M. Rehg, “An in depth view of saliency,”
     detection using center-dark channel prior,” in CVPRW, 2017, pp. 1509–          in BMVC, 2013, pp. 1–11.
     1515.                                                                     [66] L. Qu, S. He, J. Zhang, J. Tian, Y. Tang, and Q. Yang, “RGBD salient
[37] D.-P. Fan, Z. Lin, Z. Zhang, M. Zhu, and M.-M. Cheng, “Rethinking              object detection via deep fusion,” IEEE TIP, vol. 26, no. 5, pp. 2274–
     RGB-D Salient Object Detection: Models, Data Sets, and Large-Scale             2285, 2017.
     Benchmarks,” IEEE TNNLS, pp. 2075–2089, 2020.                             [67] R. Cong, J. Lei, H. Fu, J. Hou, Q. Huang, and S. Kwong, “Going from
[38] R. Ju, L. Ge, W. Geng, T. Ren, and G. Wu, “Depth saliency based on             RGB to RGBD saliency: A depth-guided transformation model,” IEEE
     anisotropic center-surround difference,” in ICIP, 2014, pp. 1115–1119.         TCYBERNETICS, pp. 1–13, 2019.
[39] Y. Niu, Y. Geng, X. Li, and F. Liu, “Leveraging stereopsis for saliency   [68] R. Shigematsu, D. Feng, S. You, and N. Barnes, “Learning RGB-D
     analysis,” in CVPR, 2012, pp. 454–461.                                         salient object detection using background enclosure, depth contrast,
[40] T. Liu, Z. Yuan, J. Sun, J. Wang, N. Zheng, X. Tang, and H.-Y. Shum,           and top-down features,” in CVPRW, 2017, pp. 2749–2757.
     “Learning to detect a salient object,” IEEE TPAMI, vol. 33, no. 2, pp.    [69] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image
     353–367, 2010.                                                                 recognition,” in CVPR, 2016, pp. 770–778.
IEEE TRANSACTIONS ON IMAGE PROCESSING                                                                                                                   15

[70] J. Han, H. Chen, N. Liu, C. Yan, and X. Li, “CNNs-Based RGB-D                   saliency fusion and bootstrap learning,” IEEE TIP, vol. 26, no. 9, pp.
     saliency detection via cross-view transfer and multiview fusion,” IEEE          4204–4216, 2017.
     TCYBERNETICS, vol. 48, no. 11, pp. 3171–3183, 2018.                        [97] D.-P. Fan, M.-M. Cheng, Y. Liu, T. Li, and A. Borji, “Structure-
[71] J. Zhang, D.-P. Fan, Y. Dai, S. Anwar, F. Sadat Saleh, T. Zhang, and            measure: A new way to evaluate foreground maps,” in ICCV, 2017,
     N. Barnes, “UC-Net: Uncertainty Inspired RGB-D Saliency Detection               pp. 4548–4557.
     via Conditional Variational Autoencoders,” in CVPR, 2020, pp. 8582–        [98] D.-P. Fan, C. Gong, Y. Cao, B. Ren, M.-M. Cheng, and A. Borji,
     8591.                                                                           “Enhanced-alignment measure for binary foreground map evaluation,”
[72] Y. Wang, Y. Li, J. H. Elder, H. Lu, and R. Wu, “Synergistic saliency            in IJCAI, 2018, pp. 698––704.
     and depth prediction for RGB-D saliency detection,” in ACCV, 2021.         [99] R. Achanta, S. Hemami, F. Estrada, and S. Susstrunk, “Frequency-tuned
[73] K. F. Fu, D.-P. Fan, G.-P. Ji, and Q. Zhao, “JL-DCF: Joint Learning             salient region detection,” in CVPR, 2009, pp. 1597–1604.
     and Densely-Cooperative Fusion Framework for RGB-D Salient Object         [100] K. Simonyan and A. Zisserman, “Very deep convolutional networks for
     Detection,” in CVPR, 2020, pp. 3052–3062.                                       large-scale image recognition,” arXiv preprint arXiv:1409.1556, 2014.
[74] A. Luo, X. Li, F. Yang, Z. Jiao, H. Cheng, and S. Lyu, “Cascade Graph     [101] N. Liu, J. Han, and M.-H. Yang, “PiCANet: Learning Pixel-Wise
     Neural Networks for RGB-D Salient Object Detection,” in ECCV,                   Contextual Attention for Saliency Detection,” in CVPR, 2018, pp.
     2020, pp. 346–364.                                                              3089–3098.
[75] X. Zhao, L. Zhang, Y. Pang, H. Lu, and L. Zhang, “A Single Stream         [102] J. Yang and M.-H. Yang, “Top-down visual saliency via joint crf and
     Network for Robust and Real-time RGB-D Salient Object Detection,”               dictionary learning,” IEEE TPAMI, vol. 39, no. 3, pp. 576–588, 2016.
     in ECCV, 2020, pp. 646–662.                                               [103] W. Wang, S. Zhao, J. Shen, S. C. Hoi, and A. Borji, “Salient object
[76] C. Li, R. Cong, Y. Piao, Q. Xu, and C. C. Loy, “RGB-D Salient Object            detection with pyramid attention and salient edges,” in CVPR, 2019,
     Detection with Cross-Modality Modulation and Selection,” in ECCV,               pp. 1448–1457.
     2020, pp. 225–241.                                                        [104] Y. Zeng, Y. Zhuge, H. Lu, and L. Zhang, “Joint learning of saliency
[77] T. Zhou, D.-P. Fan, M.-M. Cheng, J. Shen, and L. Shao, “RGB-D                   detection and weakly supervised semantic segmentation,” in ICCV,
     Salient Object Detection: A Survey,” IEEE TMM, 2021.                            2019, pp. 7223–7233.
[78] S. Liu, D. Huang, and Y. Wang, “Receptive field block net for accurate    [105] N. Otsu, “A threshold selection method from gray-level histograms,”
     and fast object detection,” in ECCV, 2018, pp. 404–419.                         IEEE SMC, vol. 9, no. 1, pp. 62–66, 1979.
[79] X. Hu, K. Yang, L. Fei, and K. Wang, “ACNet: Attention Based              [106] P. Krähenbühl and V. Koltun, “Efficient inference in fully connected
     Network to Exploit Complementary Features for RGBD Semantic                     crfs with gaussian edge potentials,” in NIPS, 2011, pp. 109–117.
     Segmentation,” in ICIP, 2019, pp. 1440–1444.
[80] Q. Chen and V. Koltun, “Photographic image synthesis with cascaded
     refinement networks,” in CVPR, 2017, pp. 1511–1520.
[81] T. Wang, A. Borji, L. Zhang, P. Zhang, and H. Lu, “A stagewise
     refinement model for detecting salient objects in images,” in ICCV,
     2017, pp. 4039–4048.
[82] Z. Deng, X. Hu, L. Zhu, X. Xu, J. Qin, G. Han, and P.-A. Heng,
     “R3Net: Recurrent residual refinement network for saliency detection,”
     in IJCAI, 2018, pp. 684–690.
[83] S. Woo, J. Park, J.-Y. Lee, and I. So Kweon, “CBAM: Convolutional
     block attention module,” in ECCV, 2018, pp. 3–19.
[84] M. Oquab, L. Bottou, I. Laptev, and J. Sivic, “Is object localization
     for free? - weakly-supervised learning with convolutional neural net-
     works,” in CVPR, 2015, pp. 685–694.
[85] B. Steiner, Z. DeVito, S. Chintala, S. Gross, A. Paszke, F. Massa,
     A. Lerer, G. Chanan, Z. Lin, E. Yang et al., “PyTorch: An imperative
     style, high-performance deep learning library,” in NIPS, 2019, pp.
     8024–8035.
[86] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classification
     with deep convolutional neural networks,” in NIPS, 2012, pp. 1106–
     1114.
[87] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,”
     in ICLR, 2015.
[88] N. Li, J. Ye, Y. Ji, H. Ling, and J. Yu, “Saliency detection on light
     field,” in CVPR, 2014, pp. 2806–2813.
[89] C. Zhu and G. Li, “A three-pathway psychobiological framework of
     salient object detection using stereoscopic technology,” in CVPRW,
     2017, pp. 3008–3014.
[90] C. Zhu, G. Li, X. Guo, W. Wang, and R. Wang, “A multilayer
     backpropagation saliency detection algorithm based on depth mining,”
     in CAIP, 2017, pp. 14–23.
[91] R. Cong, J. Lei, C. Zhang, Q. Huang, X. Cao, and C. Hou, “Saliency
     detection for stereoscopic images based on depth confidence analysis
     and multiple cues fusion,” IEEE SPL, vol. 23, no. 6, pp. 819–823,
     2016.
[92] Y. Piao, Z. Rong, M. Zhang, W. Ren, and H. Lu, “A2dele: Adaptive
     and Attentive Depth Distiller for Efficient RGB-D Salient Object
     Detection,” in CVPR, 2020, pp. 9060–9069.
[93] M. Zhang, W. Ren, Y. Piao, Z. Rong, and H. Lu, “Select, Supplement
     and Focus for RGB-D Saliency Detection,” in CVPR, 2020, pp. 3472–
     3481.
[94] F. Liang, L. Duan, W. Ma, Y. Qiao, Z. Cai, and L. Qing, “Stereoscopic
     saliency model using contrast and depth-guided-background prior,”
     Neurocomputing, vol. 275, pp. 2227–2238, 2018.
[95] J. Ren, X. Gong, L. Yu, W. Zhou, and M. Ying Yang, “Exploiting
     global priors for RGB-D saliency detection,” in CVPRW, 2015, pp.
     25–32.
[96] H. Song, Z. Liu, H. Du, G. Sun, O. Le Meur, and T. Ren, “Depth-aware
     salient object detection and segmentation via multiscale discriminative
