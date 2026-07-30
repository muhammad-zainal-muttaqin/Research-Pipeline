---
source_id: 168
bibtex_key: zhou2021spnet
title: Specificity-preserving RGB-D Saliency Detection
year: 2021
domain_theme: RGB-D SOD
verified_pdf: 168_SPNet.pdf
char_count: 137443
---

Specificity-preserving RGB-D Saliency Detection

                       Tao Zhou1 , Deng-Ping Fan2 *, Geng Chen3 , Yi Zhou4 , Huazhu Fu5
           1
             School of Computer Science and Engineering, Nanjing University of Science and Technology, China
                                              2
                                                CVL, ETH Zurich, Switzerland
            3
              School of Computer Science and Engineering, Northwestern Polytechnical University, Xi’an, China
                          4
                            School of Computer Science and Engineering, Southeast University, China
           4
             Institute of High Performance Computing, Agency for Science, Technology and Research, Singapore

                          Abstract                                1. Introduction
                                                                      Salient object detection (SOD)1 aims to model the mech-
    Salient object detection (SOD) on RGB and depth im-           anism of human visual attention and locate the most vi-
ages has attracted more and more research interests, due          sually distinctive object(s) in a given scene [62]. SOD
to its effectiveness and the fact that depth cues can now be      has been widely applied in various vision-related tasks,
conveniently captured. Existing RGB-D SOD models usu-             such as image understanding [108], action recognition [68],
ally adopt different fusion strategies to learn a shared rep-     [72], video/semantic segmentation [72, 78], and person re-
resentation from the two modalities (i.e., RGB and depth),        identification [95]. Although significant progress has been
while few methods explicitly consider how to preserve             made, it is still challenging to accurately locate salient
modality-specific characteristics. In this study, we propose      objects in many challenging scenarios, such as instance
a novel framework, termed SPNet (Specificity-Preserving           cluttered background, low-contrast lighting conditions, and
Network), which benefits SOD performance by exploring             salient object(s) having a similar appearance with the back-
both the shared information and modality-specific proper-         ground. Recently, with the large availability of depth sen-
ties (e.g., specificity). Specifically, we propose to adopt two   sors in smart devices, depth maps have been introduced
modality-specific networks and a shared learning network          to provide geometric and spatial information to improve
to generate individual and shared saliency prediction maps,       SOD performance. Consequently, fusing RGB and depth
respectively. To effectively fuse cross-modal features in the     images has gained increasing interest in the SOD commu-
shared learning network, we propose a cross-enhanced in-          nity [6, 22, 25, 43, 53, 86, 87, 99, 101], and it is a challenging
tegration module (CIM) and then propagate the fused fea-          task to adaptively fuse the two modalities (i.e., RGB and
ture to the next layer for integrating cross-level information.   depth).
Moreover, to capture rich complementary multi-modal in-               Over the past years, various RGB-D SOD methods have
formation for boosting the SOD performance, we propose a          been proposed and they often focus on how effectively fuse
multi-modal feature aggregation (MFA) module to integrate         RGB and depth images. The existing fusion strategies can
the modality-specific features from each individual decoder       be divided into three categories, i.e., early fusion, late fu-
into the shared decoder. By using a skip connection, the hi-      sion, and middle fusion. The early fusion strategy often
erarchical features between the encoder and decoder layers        adopts a simple concatenation to integrate the two modali-
can be fully combined. Extensive experiments demonstrate          ties. For example, these methods [54, 62, 69, 73] directly in-
that our SP-Net outperforms cutting-edge approaches on            tegrate RGB and depth images to form a four-channel input.
six popular RGB-D SOD and three camouflaged object de-            However, this type of fusion does not consider the distribu-
tection benchmarks. The project is publicly available at:         tion gap between the two modalities, which could result in
https://github.com/taozh2017/SPNet.                               an inaccurate feature fusion. The late fusion strategy is to
                                                                  use two parallel network streams to generate independent
                                                                  saliency maps for RGB and depth data, then the two maps
                                                                  are fused to obtain a final prediction map [17, 28, 76]. How-
                                                                  ever, it is still challenging to capture the complex interac-
                                                                  tions between the two modalities.
  * Corresponding author: Deng-Ping Fan (dengpfan@gmail.com)         1 We use “saliency detection” & “SOD” interchangeably.
                 ...                                   ...                  the shared information
                                                                                            ...      as well as capture modality-specific
RGB                                            RGB
                                                                            characteristics to improve the SOD performance. In the
                           F                                                proposed SP-Net, two encoder subnetworks are used to ex-
                 ...                                   ...                  tract multi-scale features for the two modalities (i.e., RGB
Depth           (a)                            Depth   (b)                  and depth), and a cross-enhanced integration module (CIM)
                                                                            is proposed to integrate cross-modal features at different
                               ...                             Conv layer   feature layers. Then, we use a simple U-Net [70] struc-
RGB                                                                         ture to construct a modality-specific decoder, in which skip
            F          F         F ...     F                    Decoder
                                                                            connections between the encoder and decoder layers are
                               ...
                                                             F Fusion       used to combine hierarchical features. In this way, we can
Depth                                (c)                                    learn powerful modality-specific features in each indepen-
Figure 1. Comparison between existing RGB-D salient object de-              dent decoder, which also captures modality-specific char-
tection frameworks and our proposed model. (a) RGB and depth                acteristics to provide cross-modal complementary. Further,
images are fed into two independent network streams, and then               we construct a shared decoder to combine hierarchical fea-
the fused high-level features are fed into a decoder to obtain the          tures from outputs of the previous CIM via a skip connec-
predicted saliency maps (e.g., [4, 5, 29, 49]). (b) Depth features are
                                                                            tion. To make full use of the modality-specific features, a
integrated into the RGB network using an auxiliary subnetwork
(e.g., [7, 23, 84, 94, 105]). (c) Our method adopts two modality-
                                                                            multi-modal
                                                                                      F    feature aggregation (MFA) is proposed to in-
specific networks and a shared learning network to explicitly ex-           tegrate them into the shared decoder. Finally, we formu-
plore the modality-specific characteristics and shared information,         late a unified and end-to-end trainable framework where
respectively. Then, the features learned from the modality-specific         shared and modality-specific information can be simultane-
decoders are integrated into the shared decoder to boost the SOD            ously exploited to boost the SOD performance.
performance.                                                                   The main contributions of our paper are summarized as
                                                                            follows:
    Recent researches mainly focus on the middle fusion
strategy, which utilizes two independent networks to learn
                                                                              • We propose a novel RGB-D salient object detec-
intermediate features of the two modalities separately, and
                                                                                tion framework, i.e., Specificity-Preserving Network
then the fused features are fed into a subsequent net-
                                                                                (termed SP-Net), which can explore the shared infor-
work or decoder (as shown in Fig. 1 (a)). Besides, other
                                                                                mation from RGB and depth images as well as pre-
methods carry out cross-modal fusion at multiple scales
                                                                                serve modality-specific characteristics.
[4, 5, 8, 29, 33, 34, 49]. As a result, the complex correlations
can be effectively exploited from the two modalities. More-
                                                                              • We propose a cross-enhanced integration module
over, several methods utilize depth information to enhance
                                                                                (CIM) to integrate the cross-modal features and learn
RGB features via an a auxiliary subnetwork [7, 94, 105] (as
                                                                                shared representations for the two modalities. More
shown in Fig. 1 (b)). For example, Zhao et al. [94] in-
                                                                                importantly, the output of each CIM is propagated to
troduced a contrast prior into a CNN-based architecture to
                                                                                the next layer to explore rich cross-level information.
enhance the depth information, and then the enhanced depth
was integrated with RGB features using a fluid pyramid in-
                                                                              • We propose an effective multi-modal feature aggrega-
tegration module. Zhu et al. [105] utilized an independent
                                                                                tion (MFA) module to integrate the learned modality-
subnetwork to extract depth-based features, which were
                                                                                specific features. By using it, our model can make
then incorporated into the RGB network. It should be noted
                                                                                full use of the features learned in the modality-specific
that the above methods mainly focus on learning shared
                                                                                decoder to boost the salient object detection perfor-
representations by fusing them and then use a decoder to
                                                                                mance.
generate the final saliency map. What is more, there is no
decoder with supervision to guide the depth-based feature
                                                                              • Extensive experiments on six public RGB-D SOD and
learning [94, 105], which may prevent optimal depth fea-
                                                                                three camouflaged object detection (COD) datasets
tures from being obtained. From a multi-modal learning
                                                                                demonstrate the superiority of our model over other
perspective, several works [32,55,102,104] have shown that
                                                                                cutting-edge methods. Moreover, we carry out an
exploring both the shared information and modality-specific
                                                                                attribute-based evaluation to study the performance of
characteristics can improve the model performance. How-
                                                                                many state-of-the-art RGB-D SOD methods under dif-
ever, in the RGB-D SOD community, few methods explic-
                                                                                ferent challenging factors (e.g., number of salient ob-
itly exploit modality-specific characteristics.
                                                                                jects, indoor or outdoor environments, light conditions,
    To alleviate the above issue, in this paper, we propose a
                                                                                and object scale), which has not been done previously
novel RGB-D SOD framework, i.e., Specificity-Preserving
                                                                                by existing studies.
Network (termed SP-Net), which can effectively explore
    This paper significantly extends our previous work pub-      have been proposed to effectively integrate multi-level/scale
lished in the ICCV-2021 [103], with multi-fold improve-          features [61, 79, 89, 91] to boost the SOD performance. As
ments as follows. (1) We provide some insightful discus-         in the proposed method, we mainly consider how to effec-
sions for the differences between the proposed CIM and           tively cross-modal features (i.e., RGB and depth), and the
some existing fusion strategies (see 3.3.1), and the differ-     multi-level information can be exploited via the proposed
ences between the proposed CIM and MFA (Sec. 3.3.2). (2)         cross-enhanced integration module.
We provide more details to the conference version. Specif-
ically, we add a subsection to review some existing RGB          2.2. RGB-D Salient Object Detection
SOD methods and discuss the importance of integrating               Early RGB-D based SOD methods often extract hand-
multi-level/scale features (refer to Sec. 2.1). Besides, we      crafted features from the input RGB-D data. For exam-
provide the details of evaluation metrics to better under-       ple, Lang et al. [39] proposed the first RGB-D SOD work,
stand their characteristics (see Sec. 4.1.2). (3) We pro-        which utilized Gaussian mixture models to model the distri-
vide an additional ablation study and attribute-based eval-      bution of depth-induced saliency. After that, several meth-
uation. We validate the effectiveness of the shared decoder      ods were explored based on different principles, such as
(4.3.2), and study the effects on different numbers of CIM       center-surround difference [28, 38], contrast [15, 62, 69],
(Sec. 4.3.4). Besides, we add an attribute-based evalua-         center/boundary prior [47, 107], and background enclosure
tion on object scale, and the results also show our model        [24]. However, these methods usually suffer from unsat-
can effectively handle scale variations of the objects (see      isfactory performance due to the limited expression abil-
Sec. 4.4). (4) We extend the proposed SP-Net to a new            ity of handcrafted features. Benefiting from the rapid de-
RGB-D task, i.e., COD. Quantitative and qualitative eval-        velopment of deep convolutional neural networks (CNNs),
uations conducted on three COD benchmarks demonstrate            several deep learning-based works [22, 64, 67, 86, 94] have
the superiority of our SP-Net over other existing RGB and        recently been developed and obtained promising results.
RGB-D COD methods (presented in Sec. 4.6).                       For example, Qu et al. [67] develop a CNN model to
                                                                 fuse saliency cues from different low levels into hierarchi-
2. Related Work                                                  cal features for boosting the SOD performance. Chen et
   In this section, we review three types of works that are      al. [4] propose a complementarity-aware fusion module
most related to the proposed model, i.e., RGB salient object     to effectively integrate cross-modal and cross-level features
detection, RGB-D salient object detection, and multi-modal       for RGB and depth modalities. Piao et al. [64] propose
learning.                                                        a depth-induced multi-scale recurrent attention network to
                                                                 enhance the cross-modality feature fusion. Fan et al. [22]
2.1. RGB Salient Object Detection                                design a depth depurator unit to filter out some low-quality
    Early salient object detection methods are based on          depth maps. Most other models [5, 8, 29, 42, 45, 49] employ
hand-crafted features and some saliency priors, such as          cross-modal fusion at multiple scales using different inte-
background prior [109], color contrast [1], compactness          gration strategies.
prior [100], and center prior [37]. However, the general-
                                                                 2.3. Multi-modal Learning
ization and effectiveness of these traditional methods are
limited. With the breakthrough of deep learning in the field         Recently, multi-modal (or multi-view) learning has at-
of computer vision, various deep learning-based salient ob-      tracted more and more attention, as most data can be col-
ject detection methods have been developed and obtained          lected from multiple sources or represented with different
promising performance. For example, Hou et al. [31] pro-         types of features. One traditional strategy is to directly con-
pose a novel salient object detection method by introduc-        catenate the feature vectors from such multi-modal data into
ing short connections to the skip-layer structures within        a feature vector. However, this simple concatenation may
the holistically-nested edge detector architecture. Wang         fail to exploit the complex correlations across multi-modal
et al. [75] propose a recurrent fully convolutional net-         data. As such, several multi-modal learning methods have
work framework for salient object detection and it obtains       been developed to explicitly fuse the complementary infor-
promising performance. Liu et al. [51] propose to hierarchi-     mation from different modalities to improve model perfor-
cally embed global and local context modules into the top-       mance. These popular methods can be divided into three
down pathway, which can generate attention over the con-         following types. 1) Co-training [3, 16] tries to minimize
text regions for each pixel. Deng et al. [14] propose a recur-   the disagreement between different modalities, 2) Multi-
rent residual refinement network with residual refinement        ple kernel learning [27] utilizes a predefined set of kernels
blocks to accurately detect salient objects. More methods        from multiple modalities and integrates these modalities us-
can be found in a survey paper [77]. Besides, scale variation    ing the learned weights of the kernels, and 3) Subspace
is one key challenge in the SOD task, thus several methods       learning [81, 85] assumes that there exists a latent subspace
v2

                                                                                                                                                                                                                 Up× 4
                   88*88*64      88*88*256      44*44*512 22*22*1024       11*11*2048

                                                                                                                                                                                                      1*1 Conv
                                                                                                Up× 2                     Up× 2                     Up× 2                   Up× 2

                                                                                          RFB

                                                                                                                                                                                          RFB
                                                                                                                    RFB

                                                                                                                                                                      RFB
                                                                                                                                              RFB
                    En-1           En-2           En-3         En-4              En-5                     C                         C                       C                       C
                                                                                                  𝑔1𝑅                         𝑔2𝑅                     𝑔3𝑅                    𝑔4𝑅                𝑔5𝑅
       RGB
                                                                                           𝑓4𝑆                        𝑓3𝑆                             𝑓2𝑆                           𝑓1𝑆

                                                                                                                                                                                                                 Up× 4
                                                                                                                                                                                                      1*1 Conv
             𝑓1𝑆           𝑓2𝑆            𝑓3𝑆            𝑓4𝑆         𝑓5𝑆

                                                                                                                                                                                          RFB
                                                                                                                                                                            MFA
                                                                                                                                              MFA

                                                                                                                                                                RFB
                                                                                                              MFA
                                                                                    MFA

                                                                                                                                RFB
                                                                                                  RFB
                                                                           RFB
       CIM           CIM           CIM           CIM           CIM                         C                              C                           C                             C
                                                                             𝑔1S                        𝑔2S                             𝑔3S                       𝑔4S                       𝑔5S

                                                                                                                                                                                                                 Up× 4
                                                                                                  𝑔1𝐷                         𝑔2𝐷                     𝑔3𝐷                    𝑔4𝐷                𝑔5𝐷

                                                                                                                                                                                                      1*1 Conv
                                                                                                                    RFB
                                                                                          RFB

                                                                                                                                                                      RFB

                                                                                                                                                                                          RFB
                                                                                                                                              RFB
                    En-1           En-2           En-3         En-4              En-5                     C                         C                       C                       C
                                                                                                Up× 2                     Up× 2                     Up× 2                   Up× 2
                   88*88*64      88*88*256      44*44*512 22*22*1024        11*11*2048
       Depth

     Figure 2. The overall architecture of the proposed SP-Net. Our model consists of two modality-specific learning networks and a shared
     learning network. The modality-specific learning networks are used to preserve the individual properties for each modality (i.e., RGB or
     depth), while the shared network is used to fuse cross-modal features and explore their complementary information. Skip connections are
     adopted to combine hierarchical features between the encoder and decoder layers. The learned features from the modality-specific decoder
     are integrated into the shared decoder to provide rich multi-modal complementary information for boosting saliency detection performance.
     Here, “C” denotes feature concatenation.

     shared by different modalities, in which multiple modali-                                            skip connection. Finally, to make full use of the features
     ties can be originated from one underlying latent represen-                                          learned by using the modality-specific decoder, we propose
     tation. Besides, to effectively fuse multi-modal data, several                                       an MFA module to effectively integrate these features into
     deep learning-based models have also been explored. For                                              the shared decoder. We give the details of each key part
     example, Ngiam et al. [57] propose to learn a shared rep-                                            below.
     resentation from audio and video inputs. Eitel et al. [18]
     adopt two separate CNN streams for RGB and depth, re-                                                3.2. Modality-specific Learning Network
     spectively, and then combine them using a late fusion net-
     work to achieve RGB-D object recognition. Besides, Hu et                                                 As shown in Fig. 2, the modality-specific subnetwork is
     al. [32] present a shareable and individual multi-view learn-                                        built using the Res2Net-50 [26], which has been pretrained
     ing algorithm to explore more properties of multi-modal                                              on ImageNet [71] dataset. Thus, there are five multi-level
     data. Lu et al. [55] present a shared-specific feature transfer                                      features, i.e., F R = [fm   R
                                                                                                                                        , m = 1, 2, . . . , 5] and F D =
                                                                                                             D
     framework to achieve a cross-modal person ReID task.                                                 [fm , m = 1, 2, . . . , 5], in the modality-specific encoder
                                                                                                          subnetworks for RGB and depth, respectively. In our study,
     3. Methodology                                                                                       we denote the input resolution of the modality-specific en-
                                                                                                          coder subnetwork as W × H. Thus, we have a feature reso-
        In this section, we first present the overall framework of                                        lution of H8 ∗ W 8 for the first layer, and a general resolution
     the proposed SP-Net in Sec. 3.1. Then we describe the two                                            of 2Hm ∗ 2Wm (when m > 1). Besides, the channel number of
     key components in our model, i.e., the modality-specific                                             features in the m-th layer is given as Cm (m = 1, 2, . . . ),
     learning network and shared learning network, in Sec. 3.2                                            and we have C = [64, 256, 512, 1024, 2048].
     and Sec. 3.3, respectively. Finally, Sec. 3.4 provides the                                               After obtaining the high-level features f5R and f5D , they
     overall loss function.                                                                               are then fed into the modality-specific decoder subnetworks
                                                                                                          to generate individual saliency maps. Besides, we utilize
     3.1. Overview
                                                                                                          a U-Net [70] structure to construct the modality-specific
        Fig. 2 shows the framework of the proposed specificity-                                           decoder, where the skip connections between the encoder
     preserving network for RGB-D SOD. First, the RGB and                                                 and decoder layers are used to combine hierarchical fea-
     depth images are fed into two-stream modality-specific                                               tures. Moreover, the concatenated features (only f5R or f5D
     learning networks to obtain their multi-level feature rep-                                           in the first stage of the decoder subnetwork) are fed to the
     resentations, and a CIM is proposed to learn their shared                                            receptive field block (RFB) [82] to capture global context
     feature representation. Second, the specific and shared de-                                          information. It is worth noting that the modality-specific
     coder subnetworks are utilized to generate saliency predic-                                          learning network enables us to learn effective and powerful
     tion maps, respectively. Besides, the original features from                                         individual features for each modality by retaining its spe-
     the encoder networks are integrated into the decoder via a                                           cific properties. These features are then integrated into the
                                                 V6

        1*1 Conv
                                                                                                                                              𝑅                                   ×
                                                                                                                                             𝑔𝑚

                                      3*3 Conv
                   3*3 Conv

                                                                                                                                                                                                                     3*3 Conv
                    Sigmoid
                              ×   +                                                                                                                                                                C                                    +
                                                 ×                                                              𝑆
                                                                                                               𝑔𝑚

                                                         3*3 Conv

                                                                           3*3 Conv
 𝑓𝑚𝑅                                                 C               C                                                                       𝐷                                    ×
                                                                                      𝑓𝑚S                                                   𝑔𝑚
                                                 M
                   3*3 Conv

                                      3*3 Conv
        1*1 Conv

                    Sigmoid

                                                                     S
                              ×   +                                 𝑓𝑚−1                    Figure 4. Diagram of the proposed multi-modal feature aggrega-
                                                                                            tion (MFA) module. Here “+”, “×”, “C” denote element-wise ad-
 𝑓𝑚𝐷                                                                                        dition, element-wise multiplication, and feature concatenation, re-
                                                                                            spectively.
Figure 3. Diagram of the proposed cross-enhanced integration
module (CIM). Here, “C” denotes feature concatenation, and “+”,
“×”, and “M” denote the element-wise addition, multiplication,                              feature representations for the two modalities as follows:
and maximization, respectively.
                                                                                                              \left \{ \begin {aligned} f_m^{R'}=f_{m}^{R}+f_{m}^{R}\otimes {w_m^{D}} ,\\ f_m^{D'}=f_{m}^{D}+f_{m}^{D}\otimes {w_m^{R}} ,\\ \end {aligned} \right . 
                                                                                                                                                                                                                                                                   (1)
shared decoder subnetwork to boost the saliency detection
performance.
                                                                                            where ⊗ denotes element-wise multiplication.
3.3. Shared Learning Network                                                                   Once we have obtained the cross-enhanced feature rep-
                                                                                                                                                        R′                              D′
   As shown in Fig. 2, in the shared learning network,                                      resentations (i.e., fm                                                 and fm                       ), one critical task is to ef-
we fuse the cross-modal features from the RGB and depth                                     fectively fuse them. Various strategies can be used to fuse
modalities to learn their shared representation, which is fed                               features from different modalities, including element-wise
into the shared decoder to generate the final saliency map.                                 multiplication and maximization. However, it is unclear
Besides, we also adopt skip connections between the en-                                     which is best for specific tasks. In order to benefit from the
coder and decoder layers to combine hierarchical features.                                  advantages of different strategies, we apply element-wise
Moreover, to make full use of the features learned by the                                   multiplication and maximization, and then concatenate the
                                                                                                                                                                                                                                                          R′              D′
modality-specific decoder, we integrate them into the shared                                results together. Specifically, the two features fm                                                                                                                      and fm
decoder to improve the saliency detection performance.                                      are first fed into a 3 × 3 convolutional layer to obtain their
                                                                                            smooth representations, and then we carry out element-wise
                                                                                            multiplication and maximization. Thus, we can obtain:
3.3.1    Cross-enhanced Integration Module
                                                                                                   \left \{ \begin {aligned} &p_{mul}=Bconv_3(f_m^{R'})\otimes {Bconv_3(f_m^{D'})} ,\\ &p_{max}=Max(Bconv_3(f_m^{R'}),{Bconv_3(f_m^{D'})}) , \\ \end {aligned} \right . 
We propose a CIM to effectively fuse cross-modal features.                                                                                                                                                                                                         (2)
Taking fm R
             ∈ RWm ∗Hm ∗Cm and fm     D
                                         ∈ RWm ∗Hm ∗Cm as
an example (for convenience, the width, height, and chan-
nel number of the m-th layer are denoted as Wm , Hm , and                                   where Bconv(·) is a sequential operation that combines a
Cm ), we use a 1 × 1 convolutional layer to reduce the chan-                                3 × 3 convolution followed by batch normalization, and
nel number to Cm /2 for acceleration. The CIM includes                                      a ReLU function. Then, we concatenate the results as
two parts, i.e., cross-modal feature enhancement and adap-                                  pcat = [pmul , pmax ] ∈ RWm ∗Hm ∗Cm , and obtain p1cat =
tive feature fusion. First, we use a cross-enhanced strategy                                Bconv3 (pcat ) through a Bconv3 operation to adaptively
to exploit the correlations between the two modalities by                                   weigh the two parts. Further, the output p1cat is concatenated
                                                                                                                        S
learning their enhanced features. Specifically, as shown in                                 with the previous output fm−1   of the (m − 1)-th CIM, and
Fig. 3, the two features can be fed into a 3 × 3 convolu-                                   fed into the second Bconv3 operation. Finally, we obtain
                                                                                                         S
tional layer with a Sigmoid activation function, and then                                   the output fm  of the m-th CIM. Note that, when m = 1, we
                                                       R                                    do not need to use a 1 × 1 convolutional layer for reducing
we can obtain the normalized feature maps, i.e., wm       =
             R                     D                 R
σ(Conv3 (fm )) ∈ [0, 1] and wm = σ(Conv3 (fm )) ∈                                           the channel number. Besides, there is no previous output
                                                                                              S
[0, 1], where σ is the logistic Sigmoid activation function.                                fm−1   (when m = 1), so we only feed the concatenated fea-
To exploit the correlations between the two modalities, the                                 tures into one Bconv3 operation.
normalized feature maps can be regarded as feature-level                                        Remarks. It is worth noting that our CIM can effec-
attention maps to adaptively enhance the feature represen-                                  tively exploit the correlations between the two modalities
tation. In this way, the feature map from one modality can                                  via cross-enhanced feature learning, and fuse them by adap-
be used to enhance another modality. Besides, to preserve                                   tively weighting the different feature representations. Be-
                                                                                                                                         S
the original information of each modality, a residual con-                                  sides, the fused feature representation fm       is propagated
nection is adapted to combine the enhanced features with                                    to the next layer to capture and integrate cross-level in-
their original features. Thus, we have the cross-enhanced                                   formation. As some works [54, 62, 73] directly integrate
RGB images and depth maps to form a four-channel in-                                                                                                       for Lsp and Lsh , which can pay different attention to hard
put (i.e., a cascade operation), while other methods carry                                                                                                 and easy pixels to boost the performance.
out cross-modal fusion strategies, e.g., attention-based fu-
sion modules [5, 8], fusion-refinement module (e.g., sum-                                                                                                  4. Experimental Results and Analysis
mation) [49], etc. Different from these methods, the pro-
                                                                                                                                                               In this section, we first provide the experimental setup
posed CIM mainly exploits the correlation between RGB
                                                                                                                                                           (4.1), including datasets, evaluation metrics, and implemen-
and depth images, and then adaptively integrates enhanced
                                                                                                                                                           tation details. Then we show the performance comparison
cross-modal features to obtain their fused feature represen-
                                                                                                                                                           (4.2) including quantitative and qualitative evaluation, as
tation.
                                                                                                                                                           well as conduct ablation studies to validate the effective-
                                                                                                                                                           ness of each key component (4.3). Finally, we conduct an
3.3.2           Multi-modal Feature Aggregation                                                                                                            attribute-based evaluation to show the effectiveness of our
To make full use of the features learned in the modality-                                                                                                  model in dealing with different challenges (4.4).
specific decoder, we propose a simple but effective MFA
                                                                                                                                                           4.1. Experimental Setup
module to integrate them into the shared decoder. Specif-
ically, in the m-th layer of the shared decoder, we have                                                                                                   4.1.1   Datasets
                              S                               R
the shared representation gm    , and the learned features gm
       D                                                                                                                                                   To validate the effectiveness of the proposed model, we
and gm in the modality-specific decoder. As shown in
                       R        D                                                                                                                          evaluate it on six public RGB-D SOD datasets, includ-
Fig. 4, two features gm   and gm   are multiplied by the shared
                                        RS        S      R                                                                                                 ing NJU2K [38], NLPR [62], DES [11], SSD [106],
features of the current layer, i.e., gm      = gm    ⊗ gm   and
  DS       S      D                                                                                                                                        STERE [58] and SIP [22]. The details of each dataset can
gm = gm ⊗ gm . The two features are further concate-
          DR DS                                                                                                                                            be found at: https://github.com/taozh2017/
nated ([gm    , gm ]) and then fed into a Bconv(·) operation
             Sc                                                                                                                                            RGBD-SODsurvey.
to obtain gm    . Finally, we obtain the output of the MFA
                                                    Sc                                                                                                         For a fair comparison, we utilize the same protocol to
module to combine the convolutional feature gm         with the
                   S                                                                                                                                       form the training and test sets, as introduced in [22,64]. The
original feature gm via an addition operation.
                                                                                                                                                           training set includes 2,195 samples in total, where 1,485
    Remarks. In the MFA, the learned modality-specific
                                                                                                                                                           samples from NJU2K [38] and 700 samples from the NLPR
features are used to enhance the shared features and provide
                                                                                                                                                           [62]. The remaining samples from NJU2K (500) and NLPR
rich and complementary cross-modal information. Specif-
                                                              R                                                                                            (300), and the whole DES (135), SSD (80), STERE (1,000),
ically, we use the two modality-specific features (i.e., gm
       D                S                                                                                                                                  and SIP (929), are used for testing.
and gm ) to enhance gm . More importantly, the modality-
specific decoder is given a supervision signal to guide fea-
ture learning for the modality-specific property preserva-                                                                                                 4.1.2   Evaluation Metrics
tion, which benefits the final prediction results when inte-                                                                                               We adopt four widely used metrics to evaluate the effective-
grating them into the shared decoder. We also note that                                                                                                    ness of the proposed model. The detailed definitions of the
the differences between CIM and MFA, i.e., the CIM is                                                                                                      four metrics are provided as follows.
used to learn the fused multi-modal (i.e., RGB and depth)
feature representation, while the MFA utilizes the learned                                                                                                    • Precision-recall (PR) [1]. Given a saliency map S, we
modality-specific feature to aggregate the feature represen-                                                                                                    convert it to a binary map M , and then we can compute
tation in the shared decoder.                                                                                                                                   the Precision and Recall by

3.4. Loss Function
                                                                                                                                                                      \textup {Precision}=\frac {|M\cap {G}|}{|M|},~ \textup {Recall}=\frac {|M\cap {G}|}{|G|},                      (4)
    Finally, we formulate a unified and end-to-end trainable
framework. The overall loss function consists of two parts,                                                                                                     where G denotes the ground-truth. A popular strategy
i.e., Lsp and Lsh , for the modality-specific and shared de-                                                                                                    is to partition S by using a set of thresholds (i.e., vary-
coders, respectively. For convenience, SR and SD denote                                                                                                         ing from 0 to 255). For each threshold, we calculate a
the prediction maps when using RGB and depth images,                                                                                                            pair of recall and precision scores, and then combine
respectively, Ssh denotes the prediction map using their                                                                                                        all scores to obtain a PR curve.
shared representation, and G denotes the ground truth map.
Therefore, the overall loss function can be formulated as                                                                                                     • Structure Measure. S-measure (Sα ) [9] is proposed
follows:                                                                                                                                                        to assess the structural similarity between the regional
                                                                                                                                                                perception (Sr ) and object perception (So ), which is
   \begin {aligned} \mathcal {L}_{total}=\mathcal {L}_{sh}(S_{sh},G)+\mathcal {L}_{sp}(S_R,G)+\mathcal {L}_{sp}(S_D,G). \end {aligned} \label {eq3}  (3)        defined by

    In Eq. (3), we utilize the pixel position-aware loss [80]                                                                                                                          \begin {aligned} S_{\alpha }=\alpha * S_{o}+\left (1-\alpha \right )*S_{r}, \end {aligned}    (5)
Table 1. Benchmarking results of 8 representative traditional models and 23 deep models on six public RGB-D saliency detection datasets
using four widely used evaluation metrics (i.e., Sα [9], max Eϕ [19], max Fβ [1], and M [63]). “↑“ & “↓” indicate that larger or smaller
is better. The subscript of each model denotes the publication year. The best results are highlighted in Bold fonts.
                     NJU2K [38]         STERE [58]          DES [11]          NLPR [62]          SSD [106]           SIP [22]
          Model Sα ↑ Fβ ↑ Eξ ↑ M ↓ Sα ↑ Fβ ↑ Eξ ↑ M ↓ Sα ↑ Fβ ↑ Eξ ↑ M ↓ Sα ↑ Fβ ↑ Eξ ↑ M ↓ Sα ↑ Fβ ↑ Eξ ↑ M ↓ Sα ↑ Fβ ↑ Eξ ↑ M ↓

     LHM14 [62] .514                      .632                .724                .205                 .562               .683                .771                .172                .562   .511   .653   .114    .630   .622        .766        .108        .566        .568        .717        .195        .511        .574        .716   .184
    ACSD14 [38] .699                      .711                .803                .202                 .692               .669                .806                .200                .728   .756   .850   .169    .673   .607        .780        .179        .675        .682        .785        .203        .732        .763        .838   .172
      LBE16 [24] .695                     .748                .803                .153                 .660               .633                .787                .250                .703   .788   .890   .208    .762   .745        .855        .081        .621        .619        .736        .278        .727        .751        .853   .200
   DCMC16 [13] .686                       .715                .799                .172                 .731               .740                .819                .148                .707   .666   .773   .111    .724   .648        .793        .117        .704        .711        .786        .169        .683        .618        .743   .186
       SE16 [28] .664                     .748                .813                .169                 .708               .755                .846                .143                .741   .741   .856   .090    .756   .713        .847        .091        .675        .710        .800        .165        .628        .661        .771   .164
    MDSF17 [73] .748                      .775                .838                .157                 .728               .719                .809                .176                .741   .746   .851   .122    .805   .793        .885        .095        .673        .703        .779        .192        .717        .698        .798   .167
   CDCP17 [107] .669                      .621                .741                .180                 .713               .664                .786                .149                .709   .631   .811   .115    .669   .621        .741        .180        .603        .535        .700        .214        .595        .505        .721   .224
     DTM20 [12] .706                      .716                .799                .190                 .747               .743                .837                .168                .752   .697   .858   .123    .733   .677        .833        .145        .677        .651        .773        .199        .690        .659        .778   .203

       DF17 [67] .763                     .804                .864                .141                 .757               .757                .847                .141                .752   .766   .870   .093    .802   .778        .880        .085        .747        .735        .828        .142        .653        .657        .759   .185
   CTMF18 [29] .849                       .845                .913                .085                 .848               .831                .912                .086                .863   .844   .932   .055    .860   .825        .929        .056        .776        .729        .865        .099        .716        .694        .829   .139
       PCF18 [4] .877                     .872                .924                .059                 .875               .860                .925                .064                .842   .804   .893   .049    .874   .841        .925        .044        .841        .807        .894        .062        .842        .838        .901   .071
   AFNet19 [76] .772                      .775                .853                .100                 .825               .823                .887                .075                .770   .729   .881   .068    .799   .771        .879        .058        .714        .687        .807        .118        .720        .712        .819   .118
     CPFP19 [94] .878                     .877                .923                .053                 .879               .874                .925                .051                .872   .846   .923   .038    .888   .867        .932        .036        .807        .766        .852        .082        .850        .851        .903   .064
     MMCI19 [7] .859                      .853                .915                .079                 .873               .863                .927                .068                .848   .822   .928   .065    .856   .815        .913        .059        .813        .781        .882        .082        .833        .818        .897   .086
     TANet19 [5] .878                     .874                .925                .060                 .871               .861                .923                .060                .858   .827   .910   .046    .886   .863        .941        .041        .839        .810        .897        .063        .835        .830        .895   .075
   DMRA19 [64] .886                       .886                .927                .051                 .886               .886                .938                .047                .900   .888   .943   .030    .899   .879        .947        .031        .857        .844        .906        .058        .806        .821        .875   .085
cmSalGAN20 [36] .903                      .896                .940                .046                 .900               .894                .936                .050                .913   .899   .943   .028    .922   .907        .957        .027        .791        .735        .867        .086        .865        .864        .906   .064
  ASIFNet20 [41] .889                     .888                .927                .047                 .878               .878                .927                .049                .934   .935   .974   .019    .906   .888        .944        .030        .857        .834        .884        .056        .857        .859        .896   .061
    ICNet20 [44] .894                     .891                .926                .052                 .903               .898                .942                .045                .920   .913   .960   .027    .923   .908        .952        .028        .848        .841        .902        .064        .854        .857        .903   .069
   A2dele20 [65] .871                     .874                .916                .051                 .878               .879                .928                .044                .886   .872   .920   .029    .898   .882        .944        .029        .802        .776        .861        .070        .828        .833        .889   .070
  JL-DCF20 [25] .903                      .903                .944                .043                 .905               .901                .946                .042                .929   .919   .968   .022    .925   .916        .962        .022        .830        .795        .885        .068        .879        .885        .923   .051
   S2 MA20 [52] .894                      .889                .930                .053                 .890               .882                .932                .051                .941   .935   .973   .021    .915   .902        .953        .030        .868        .848        .909        .052        .872        .877        .919   .057
   UCNet20 [86] .897                      .895                .936                .043                 .903               .899                .944                .039                .933   .930   .976   .018    .920   .903        .956        .025        .865        .854        .907        .049        .875        .879        .919   .051
      SSF20 [90] .899                     .896                .935                .043                 .893               .890                .936                .044                .904   .884   .941   .026    .914   .896        .953        .026        .845        .824        .897        .058        .876        .882        .922   .052
  HDFNet20 [59] .908                      .911                .944                .038                 .900               .900                .943                .041                .926   .921   .970   .021    .923   .917        .963        .023        .879        .870        .925        .045        .886        .894        .930   .047
 Cas-GNN20 [56] .911                      .903                .933                .035                 .899               .901                .930                .039                .905   .906   .947   .028    .919   .904        .947        .028        .872        .862        .915        .047        .875        .879        .919   .051
   CMMS20 [42] .900                       .897                .936                .044                 .895               .893                .939                .043                .937   .930   .976   .018    .915   .896        .949        .027        .874        .864        .922        .046        .872        .877        .911   .058
    CoNet20 [35] .895                     .893                .937                .046                 .908               .905                .949                .040                .909   .896   .945   .028    .908   .887        .945        .031        .853        .840        .915        .059        .858        .867        .913   .063
   DANet20 [97] .899                      .910                .935                .045                 .901               .892                .937                .043                .924   .928   .968   .023    .915   .916        .953        .028        .864        .866        .914        .050        .875        .892        .918   .054
    PGAR20 [10] .909                      .907                .940                .042                 .907               .898                .939                .041                .913   .902   .945   .026    .930   .916        .961        .024        .865        .838        .898        .057        .876        .876        .915   .055
   D3 Net21 [22] .900                     .900                .950                .041                 .899               .891                .938                .046                .898   .885   .946   .031    .912   .897        .953        .030        .857        .834        .910        .058        .860        .861        .909   .063

    SP-Net (Ours) .925 .935 .954 .028 .907 .915 .944 .037 .945 .950 .980 .014 .927 .925 .959 .021 .871 .883 .915 .044 .894 .916 .930 .043

     where α ∈ [0, 1] is a trade-off parameter and it is set to                                                                                                                                                   the F -measure. This yields a set of F -measure val-
     0.5 as default [9].                                                                                                                                                                                          ues for which we report the maximal Fβ in our exper-
                                                                                                                                                                                                                  iments.
   • Enhanced-alignment Measure. Eϕ [19] is used
     to capture image-level statistics and their local pixel
     matching information, and it is defined as                                                                                                                                                             • Mean Absolute Error (M). It is adopted to evalu-
                                                                                                                                                                                                              ate the average pixel-level relative error between the
                         \begin {aligned} E_{\phi }=\frac {1}{W*H}\sum _{i=1}^{W}\sum _{i=1}^{H}\phi _{FM}\left (i,j\right ), \end {aligned}                                                 (6)              ground truth (i.e., G) and normalized prediction (i.e.,
                                                                                                                                                                                                              S), which is defined by
     where ϕF M denotes the enhanced-alignment matrix
     [19].
   • F-measure (Fβ [1]). It is used to comprehensively                                                                                                                                                                  \mathcal {M}=\frac {1}{W*H}\sum _{i=1}^{W}\sum _{i=1}^{H}\left |S\left (i,j\right )-G\left (i,j\right ) \right |,     (8)
     consider both precision and recall, and we can obtain
     the weighted harmonic mean by
                                                                                                                                                                                                                  where W and H denote the width and height of
                 \begin {aligned} F_{\beta }=\left (1+\beta ^2\right )\frac {\textup {Precision}*\textup {Recall}}{\beta ^{2}\textup {Precision}+\textup {Recall}}, \end {aligned}           (7)                  the map, respectively. M estimates the similarity
                                                                                                                                                                                                                  between the saliency map and the ground-truth map,
     where β 2 is set to 0.3 to emphasize the precision [1].                                                                                                                                                      and normalizes it to [0, 1].
     We use different fixed [0, 255] thresholds to compute
4.1.3   Implementation Details                                   promising performance in locating salient object(s) in a
                                                                 given scene. In addition, we show the PR curves [2] (Fig. 5)
The proposed model is implemented with the PyTorch li-           and F-measure curves in Fig. 6. For a clear view, we pro-
brary, and trained on one NVIDIA Tesla V100 GPU with 32          vide the results of 29 RGB-D saliency detection methods,
GB memory. The backbone network (Res2Net-50 [26]) is             including 28 SOTA models with complete saliency maps.
used, which has been pre-trained on ImageNet [71]. When          As observed, the superiority of our model is more visible
using the backbone network, since RGB and depth images           on these reported datasets.
have different channels, the input channel of the depth en-
                                                                     In addition, we compare the proposed SP-Net with 13 re-
coder is modified to 1. We utilize the Adam algorithm to op-
                                                                 cent state-of-the-art models on the ReDWeb-S dataset. The
timize the proposed model. The initial learning rate is set to
                                                                 results of all compared methods are collected from https:
1e − 4 and is divided by 10 every 60 epochs. The input res-
                                                                 //github.com/nnizhang/SMAC, and the results of
olutions of RGB and depth images are resized to 352 × 352.
                                                                 our method are obtained by testing the model (trained us-
To enhance the generalizability of the proposed learning al-
                                                                 ing NJU2K [38] and NLPR [62]) on the ReDWeb-S dataset.
gorithm, we adopt multiple data augmented strategies, con-
                                                                 The comparison results are shown in Table 2. From the
sisting of random flipping, rotating, and border clipping.
                                                                 results, it can be observed that our method performs bet-
The batch size is set to 20 and the model has trained over
                                                                 ter than most compared methods, and it is comparable with
200 epochs.
                                                                 UCNet and JL-DCF on the ReDWeb-S dataset.
    For testing, the RGB and depth images are first resized to
                                                                     Moreover, we compare the proposed model using dif-
352×352 and then fed into the model to obtain the predicted
                                                                 ferent backbone networks, and the results are shown in Ta-
saliency map. Then, the predicted saliency map is resized
                                                                 ble 3. From the results, we can see that the proposed model
back to the original size of the input images. Finally, the
                                                                 obtains better performance when using Res2Net-50 as the
output of the shared decoder can be regarded as the final
                                                                 backbone, and the model using ResNet-50 as backbone still
prediction for our model.
                                                                 performs better than other compared methods (see Table 1).
4.2. Performance Comparison
4.2.1   Compared RGB-D SOD Models                                4.2.3   Qualitative Evaluation

We compare the proposed SP-Net with 30 benchmarking              Fig. 7 shows several representative samples of results com-
RGB saliency detection methods, including 8 handcrafted          paring our model with eight top state-of-the-art methods.
traditional models (i.e., LHM [62], ACSD [38], LBE [24],         The first row shows a scene with a small object. Our
DCMC [13], SE [28], MDSF [73], CDCP [107]), and                  method, A2dele, PGAR, and D3Net can accurately detect
DTM [12], and 23 deep models (i.e., DF [67], CTMF [29],          the salient object, while JL-DCF, S2MA, SSF, and UCNet
PCF [4], AFNet [76], CPFP [94], MMCI [7], TANet [5],             predict some non-object regions. In the 2nd and 3rd rows,
DMRA [64], cmSalGAN [36], ASIFNet [41], ICNet [44],              we show two examples when the scene is with complex
A2dele [65], JL-DCF [25], S2 MA [52], UCNet [86], SSF            backgrounds. From the comparison results, it can be ob-
[90], HDFNet [59], Cas-GNN [56], CMMS [42], D3 Net               served that our method and S2MA produce reliable results,
[22], CoNet [35], DANet [97], and PGAR [10]). Details            while other RGB-D saliency detection models fail to locate
for these methods can be referred to the related papers and      the object or confuse the background as a salient object. In
the survey paper [101].                                          the 4th row, the comparison methods (except D3Net) locate
                                                                 a non-salient and small object. In the 5th row, we show an
                                                                 example with multiple salient objects, where it is challeng-
4.2.2   Quantitative Evaluation                                  ing to accurately locate all salient objects. Our method lo-
As shown in Table 1, our method is superior to eight tra-        cates all salient objects and segments them more accurately,
ditional methods (i.e., LHM [62], ACSD [38], LBE [24],           generating sharper edges compared to other approaches. We
DCMC [13], SE [28], MDSF [73], and CDCP [107]) by                show an example under low-light conditions in the last row.
a large margin on all six datasets. Besides, our method          It can be seen that some approaches fail to detect the entire
outperforms all of the comparison state-of-the-art methods       extent of the salient object. Our model can produce promis-
and obtains the best performance in terms of four evalu-         ing results by suppressing background distractors to boost
ation metrics on NJU2K, DES, and SIP datasets. More-             the saliency detection performance.
over, it is worth noting that our model obtains better perfor-
mance on STERE and NLPR than most compared RGB-D                 4.2.4   Inference Time and Model Size
saliency detection methods. Our model is also comparable
with CoNet on the STERE dataset, and JL-DCF and PGAR             We test the inference time for different methods on NVIDIA
on the NLPR dataset. Overall, our proposed SP-Net obtains        TESLA P40 GPU with 24G memory. The inference time
                  1
V2                                                                                              1                                                                               1

                 0.8                                                                           0.8                                                                             0.8
     Precision

                                                                                   Precision

                                                                                                                                                                   Precision
                 0.6                                                                           0.6                                                                             0.6

                 0.4                                                                           0.4                                                                             0.4

                                    NJU2K                                                                             STERE                                                                         DES
                 0.2                                                                           0.2                                                                             0.2

                       0        0.2       0.4        0.6         0.8          1                      0          0.2         0.4           0.6      0.8         1                     0        0.2           0.4           0.6          0.8          1
                                              Recall                                                                            Recall                                                                        Recall
                  1                                                                             1                                                                               1

                 0.8                                                                           0.8                                                                             0.8
                                                                                   Precision

                                                                                                                                                                   Precision
     Precision

                 0.6                                                                           0.6                                                                             0.6

                 0.4                                                                           0.4                                                                             0.4

                                    NLPR                                                                              SSD                                                                           SIP
                 0.2                                                                           0.2                                                                             0.2

                       0        0.2       0.4        0.6         0.8          1                      0          0.2         0.4           0.6      0.8         1                     0        0.2           0.4           0.6      0.8              1
                                              Recall                                                                            Recall                                                                        Recall

                                        LHM         ACSD        LBE        DCMC                 SE         CDCP            DF       CTMF         PCF      AFNet                CPFP          MMCI          TANet          DMRA
                             cmSalGAN      ASIF       ICNet       A2dele       JLDCF                     S2MA           UCNet       SSF         Cas-GNN        CMMS                 D3Net       CoNet             DANet         PGAR         Ours

                              Figure 5. PR curves on six datasets (i.e., NJU2K [38], STERE [58], DES [11], NLPR [62], SSD [106], and SIP [22]).

     Table 2. Comparison results of our model and 13 state-of-the art methods (i.e., CTMFF [29], PCF [4], AFNet [76], MMCI [7], CPFP [94],
     DMRA [64], TANet [5], A2dele [65], UCNet [86], JL-DCF [25], S2 MA [52], SSF [90], and D3 Net [22]) on the ReDWeb-S dataset.
                           Models     CTMF        PCF         AFNet      MMCI                  CPFP         DMRA            TANet         A2dele       UCNet       JL-DCF                S2 MA            SSF        D3 Net        Ours
                            Sα ↑      0.641       0.655       0.546        0.660               0.685        0.592           0.656          0.641       0.713         0.734                  0.711         0.595      0.689        0.710
                            Fβ ↑      0.607       0.627       0.549        0.641               0.645        0.579           0.623          0.603       0.710         0.727                  0.696         0.558      0.673        0.715
                            Eϕ ↑      0.739       0.743       0.693        0.754               0.744        0.7211          0.741          0.672       0.794         0.805                  0.781         0.710      0.768        0.800
                            M↓        0.204       0.166       0.213        0.176               0.142        0.188
                                                                                                                0.8
                                                                                                                            0.165          0.160       0.130         0.128                  0.139         0.189      0.149        0.129

                                                                                                                  0.6
                                                               Table 3. Comparison of our model using different backbone networks.
                                                                                                                  0.4

                                          NJU2K [38]         STERE [58]           DES [11]             NLPR [62]             SSD [106]             SIP [22]
                                                                             0.2
                               Model Sα ↑ Fβ ↑ Eξ ↑ M ↓ Sα ↑ Fβ ↑ Eξ ↑ M ↓ Sα ↑0 Fβ ↑ E0.1ξ ↑ M 0.2
                                                                                                ↓ Sα ↑ F0.3β ↑ Eξ 0.4
                                                                                                                  ↑ M ↓ S0.5
                                                                                                                         α ↑ Fβ ↑ Eξ ↑ M ↓ Sα ↑ Fβ ↑ Eξ ↑ M ↓
                                                                                                                                0.6     0.7    0.8        0.9 1

             Ours(ResNet-50) .922 .934 .952 .030 .904 .914 .942 .037 .936 .944 .974 .016 .930 .931 .965 .020 .869 .876 .906 .044 .896 .916 .934 .041
            Ours(Res2Net-50) .925 .935 .954 .028 .907 .915 .944 .037 .945 .950 .980 .014 .927 .925 .959 .021 .871 .883 .915 .044 .894 .916 .930 .043

     Table 4. Comparisons with inference time and model size of dif-                                                                diction maps, it has a relatively large model size and takes
     ferent methods.
                               Method                Ours          JL-DCF [25]                  S2MA [52]
                                                                                                                                    much inference time for the saliency prediction than other
                      Model Size (MB)                175.3            124.5                       82.7                              compared methods. Thus, we can design lightweight net-
                   Inference Time (ms)                91.7             21.8                       22.1                              works to improve the efficiency of the proposed SP-Net in
                               Method             UCNet [86]           SSF [90]                HDFNet [59]                          future work.
                      Model Size (MB)               31.3                 32.9                    153.2
                   Inference Time (ms)              31.8                 45.7                     57.1

     and model size of different methods (including our SP-                                                                         4.3. Ablation Studies
     Net, JL-DCF [25], S2MA [52], UCNet [86], SSF [90], and
     HDFNet [59] ) are shown in Table 4. Because our model                                                                             To verify the relative importance of different key compo-
     adopts two modality-specific networks and a shared learn-                                                                      nents of our model, we conduct ablation studies by remov-
     ing network to generate individual and shared saliency pre-                                                                    ing or replacing them from our full model.
                  1                                                                   1                                                                                      1
V2
                 0.8                                                                 0.8                                                                                   0.8
     F-measure

                                                                         F-measure

                                                                                                                                                               F-measure
                 0.6                                                                 0.6                                                                                   0.6

                 0.4                                                                 0.4                                                                                   0.4

                               NJU2K                                                                   STERE                                                                                      DES
                 0.2                                                                 0.2                                                                                   0.2

                       0     50       100      150      200        250                     0      50             100          150         200          250                       0           50           100       150         200          250
                                      Threshold                                                                  Threshold                                                                                Threshold
                  1                                                                   1                                                                                      1

                 0.8                                                                 0.8                                                                                    0.8
     F-measure

                                                                         F-measure

                                                                                                                                                                F-measure
                 0.6                                                                 0.6                                                                                    0.6

                 0.4                                                                 0.4                                                                                    0.4

                               NLPR                                                                    SSD                                                                                        SIP
                 0.2                                                                 0.2                                                                                    0.2

                       0     50       100      150      200        250                     0      50             100          150         200          250                        0          50           100       150          200          250
                                      Threshold                                                                  Threshold                                                                                Threshold

                                       LHM     ACSD     LBE        DCMC                SE        CDCP            DF          CTMF         PCF         AFNet                 CPFP            MMCI          TANet         DMRA
                           cmSalGAN     ASIF    ICNet     A2dele         JLDCF                 S2MA          UCNet           SSF      Cas-GNN           CMMS                      D3Net           CoNet         DANet         PGAR         Ours

     Figure 6. F-measure curves under different thresholds on six datasets (i.e., NJU2K [38], STERE [58], DES [11], NLPR [62], SSD [106],
     and SIP [22]).

                                                                                                        1

                                                                                                       0.8

                                                                                                       0.6

                                                                                                       0.4

                                                                                                       0.2
                                                                                                             0         0.1          0.2         0.3           0.4                     0.5     0.6           0.7         0.8          0.9          1

                  RGB          Depth           GT         Ours               A2dele                   JL-DCF            S2MA               UCNet                            SSF              D3Net                DANet         PGAR
     Figure 7. Visual comparisons of our method and eight state-of-the-art methods (including A2dele [65], JL-DCF [25], S2MA [52], UCNet
     [86], SSF [90], D3Net [22], DANet [97], and PGAR [10].
        Table 5. Quantitative evaluation for ablation studies.                                              Table 6. Ablation study on different numbers of CIM.
      NJU2K [38] STERE [58] DES [11] NLPR [62] SSD [106] SIP [22]                                          NJU2K     STERE      DES      NLPR       SSD       SIP
      Sα ↑ M ↓ Sα ↑ M ↓ Sα ↑ M ↓ Sα ↑ M ↓ Sα ↑ M ↓ Sα ↑ M ↓                                              Sα ↑ M ↓ Sα ↑ M ↓ Sα ↑ M ↓ Sα ↑ M ↓ Sα ↑ M ↓ Sα ↑ M ↓
                                                                                                    CIM1 .918 .034 .908 .039 .929 .019 .928 .022 .865 .047 .889 .046
Ours .925 .028 .907 .037 .945 .014 .927 .021 .871 .044 .894 .043                                    CIM3 .920 .032 .900 .041 .935 .017 .928 .021 .857 .049 .891 .045
 A1     .916   .034   .898   .042   .939   .016    .926          .022   .869   .047   .892   .044   Ours .925 .028 .907 .037 .945 .014 .927 .021 .871 .044 .894 .043
 A2     .921   .031   .895   .042   .938   .016    .925          .022   .865   .051   .896   .042
 A3     .919   .032   .895   .043   .938   .016    .929          .020   .864   .049   .887   .048
 A4     .924   .029   .903   .038   .930   .019    .927          .023   .867   .049   .888   .046
                                                                                                    provide more multi-modal complementary information. To
 B1     .918 .034 .901 .041 .939 .017 .922 .024 .858 .050 .885 .048                                 validate its effectiveness, we delete this module, denoted as
 B2     .924 .029 .900 .041 .941 .015 .926 .022 .864 .049 .893 .044
                                                                                                    “B1“. Besides, we consider comparing two other feature
 B3     .921 .031 .903 .039 .938 .016 .925 .022 .863 .050 .891 .045
                                                                                                    fusion strategies with our MFA. As shown in Fig. 8, one
 C1     .913 .037 .900 .047 .935 .019 .922 .025 .861 .055 .880 .051
                                                                                                    is the cross-modal feature enhancement fusion; the other is
 C2     .916 .034 .906 .040 .923 .021 .924 .022 .866 .049 .882 .051
                                                                                                    a simple concatenation strategy. The comparison experi-
                                                                                                    ments for the two strategies are denoted “B2” and “B3”. As
                                                                                                    shown in Table 5, Comparing “B1” and our full model, the
                                                                                  𝑅
                       3*3 Conv                                                  𝑔𝑚
           𝑅           + Sigmoid
                                           ×                                                        results demonstrate the effectiveness of integrating the fea-
          𝑔𝑚
                                                      3*3 Conv

                                                                                                C   tures learned into the shared decoder. Comparing “B2” and
                                               C                    +
 𝑆
𝑔𝑚                                                                         𝑆
                                                                          𝑔𝑚                        “B3” with our full model, we can see that the MFA module
                       3*3 Conv                                                                     outperforms both of the other fusion strategies.
           𝐷
                                       ×                                          𝐷
                                                                                 𝑔𝑚
          𝑔𝑚           + Sigmoid
                             (a)                                                       (b)
Figure 8. Comparison of MFA module with other fusion strategies.                                    4.3.3     Effectiveness of Modality-specific Decoder
4.3.1     Effectiveness of CIM                                                                      We delete the two modality-specific decoders, and the eval-
Since the proposed CIM is used to fuse cross-modal fea-                                             uation is as shown in “C1” of Table 5. It can be ob-
tures and learn their shared representation, we utilize a di-                                       served that the performance will degrade without using the
rect concatenation strategy instead of the CIM. Specifically,                                       two parts. This indicates the effectiveness of the modality-
the two features fmR
                      and fmD
                              (as shown in Fig. 3) are directly                                     specific decoder, which can provide supervision signals to
concatenated and then fed into a 3×3 convolutional layer to                                         ensure that modality-specific properties can be learned.
obtain the fused representation in each layer. We denote this                                          Besides, to evaluate the effectiveness of the combina-
evaluation as “A1” in Table 5. From the comparison results,                                         tion of the two modality-specific decoders, we add an ex-
it can be seen that our model performs better when using                                            periment to compare the SOD results when using the out-
the proposed CIM than using a simple feature concatenation                                          put from the shared decoder and the combination of two
strategy. This also indicates the contribution of the CIM in                                        modality-specific decoders. The evaluation is as shown
boosting the saliency detection performance. Besides, there                                         in “C2” of Table 5. From the compared results, we can
are two parts in CIM, i.e., cross-modal feature enhancement                                         see that the performance of the shared decoder outper-
and adaptive feature fusion. Thus, to evaluate the contribu-                                        forms the combination of two modality-specific decoders.
tion of each part, we denote the CIM with only cross-modal                                          This indicates the shared decoder can combine multi-modal
feature enhancement or adaptive feature fusion as “A2” and                                          shared information and modality-specific characteristics to
“A3”, respectively. When comparing the two independent                                              improve the SOD performance.
parts with the full version of the CIM, we can see that the
effectiveness of the proposed CIM. Moreover, in CIM, the
features of the last layer are propagated to the next layer to                                      4.3.4     Effects on Different Numbers of CIM
capture cross-level correlations. To validate the effective-
ness of the propagation strategy, we delete this propagation                                        To investigate the effects of different numbers of CIM, we
in the CIM, denoted as “A4”. The comparison results be-                                             compare our full model (i.e., using five CIMs) with two
tween “A4” and CIM show that this propagation strategy                                              degraded versions, including 1) “CIM1 ”: we only conduct
improves the saliency detection performance.                                                        CIM on the features from the last layer in the encoder net-
                                                                                                    work; 2) “CIM3 ”: we conduct CIMs on the features from
                                                                                                    the last three layers in the encoder network, i.e., using three
4.3.2     Effectiveness of MFA
                                                                                                    CIMs. Table 6 shows the comparison results using differ-
In the proposed framework, the MFA is proposed to make                                              ent numbers of CIMs. From the results, we can see that our
full use of the features learned in the modality-specific de-                                       model with five CIMs obtains better performance on most
coder, which are then integrated into the shared decoder to                                         datasets.
                1
                                                                                                           Single                Multiple         Overall
              0.9
6
         S

              0.8

              0.7

                            F        CI         et             le      F       et                  t        F              t         t             rs
                       PC                    N         RA   de
                                                                           A
                                                                     DC S2M UCN                 Ne        SS         Ne          Ne         AR   Ou
                                MM        TA         DM   A2      JL                          IC                   D3          DA        PG
                                                                                 (a)
                                                                                Methods
                1
                                                                                                         Indoor                Outdoor           Overall
             0.95

              0.9
       S

             0.85

              0.8
                          F       CI           t                    le      F       et               t         F           t         t                rs
                       PC                    Ne        RA        de
                                                                                A
                                                                          DC S2M UCN            Ne        SS            Ne        Ne      AR     Ou
                                MM        TA         DM        A2      JL                     IC                   D3          DA      PG
                                                                                (b)
                                                                                Methods
             0.95
                                                                                                         Low-light                  Sunny        Overall
              0.9

             0.85
       S

              0.8

             0.75
                            F        CI          t                     le      F       et            t         F           t         t                rs
                       PC                      Ne         RA        de
                                                                                   A
                                                                             DC S2M UCN         Ne        SS            Ne        Ne      AR     Ou
                                MM        TA         DM        A2         JL                  IC                   D3          DA      PG
                                                                                (c)
                                                                                Methods
    Figure 9. Attribute-based evaluation w.r.t. (a) number of salient objects (i.e., single vs. multiple), (b) indoor vs. outdoor environments, and
    (c) light conditions (low-light vs. sunny).

                                          Figure 10. Attribute-based evaluation w.r.t. scales of the salient object(s).
                                                                    termed “small”; 2) when the ratio is larger than 0.4, termed
                                                                    “large”; and 3) when the ratio is in the range of [0.1, 0.4],
                                                                    termed “medium”. To evaluate different methods in han-
                                                                    dling scale variation, we construct a hybrid dataset with
                                                                    2,444 images collected from STERE [58], NLPR [62], SSD
                                                                    [106], DES [11], and SIP [22]. Fig. 10 shows the compar-
                                                                    ison results of the attribute-based evaluation w.r.t. scales of
                                                                    the salient object(s). From the results, we can see that all
                                                                    comparison methods obtain better performance in detect-
                                                                    ing small salient objects while they obtain relatively worse
                                                                    performance in detecting large salient objects. Besides, the
                                                                    most recent models, i.e., JL-DCF, DANet, PGAR, and our
                                                                    model, obtain promising performance.

      RGB              Depth             GT               Ours      4.5. Failure Cases and Discussion
            Figure 11. Some failure cases of our model.                 The proposed SP-Net has shown good RGB-D saliency
                                                                    detection performance in most cases. However, our model
                                                                    fails to detect salient objects when dealing with some
4.4. Attribute-based Evaluation                                     challenging scenes such as complex background and low-
    There are several challenging factors that affect the per-      quality depth. Some failure cases of our model are shown in
formance of RGB-D saliency detection models, such as the            Fig. 11. In the first row, we can see that the depth quality is
number of salient objects, indoor or outdoor environment,           very poor, which makes our model can only roughly locate
light conditions, and so on. Thus, it is interesting to evalu-      the boat without fine details. Thus, it is helpful to enhance
ate the saliency detection performance under different con-         or filter depth maps for boosting the saliency detection per-
ditions, to show the strengths and weaknesses of state-of-          formance. In the second row, the annotated salient object
the-art models in handling these challenges.                        has a similar appearance to other objects in the scene, thus
    1) Single vs. Multiple Objects. In this evaluation, we          it is challenging to accurately detect the salient object. In
construct a hybrid dataset with 1,229 images collected from         the third row, we can see that the object has fine details,
the NLPR [62] and SIP [22] datasets. The comparison re-             our model only locates the main regions without fine de-
sults using Sα are shown in Fig. 9 (a). As can be observed,         tails. Thus, there is still considerable room for improving
it is easier to detect a single salient object than multiple. Be-   our model to handle some scenes with fine structures in fur-
sides, our model outperforms other state-of-the-art methods         ther work.
in locating single and multiple objects.
                                                                    4.6. Application for RGB-D Camouflaged Object
    2) Indoor vs. Outdoor. We evaluate the performance
                                                                         Detection
of different RGB-D SOD models under indoor and out-
door scenes. In this evaluation experiment, DES [11] and                The proposed SP-Net is originally designed for the RGB-
NLPR [62] include indoor and outdoor scenes, we thus con-           D SOD task, which can be easily extended to other re-
struct a hybrid dataset collected from the two datasets. The        lated RGB-D tasks, e.g., RGB-D based camouflaged ob-
comparison results are shown in Fig. 9 (b). As can be ob-           ject detection (COD). The aim of COD is to identify ob-
served, many models struggle more to detect salient ob-             jects that are “seamlessly” embedded in their background
jects in indoor scenes than outdoor scenes, while JL-DCF,           surroundings. Thus, it is a very challenging task due to
S2MA, UCNet, ICNet, SSF, DANet, and our model perform               the high intrinsic similarities between the target object and
a little better in outdoor scenes.                                  the background [20, 46, 74]. A recent research [88] sug-
    3) Light Conditions. We carry out this evaluation on the        gests that depth can also provide useful spatial information
SIP dataset [22], and the data is grouped into two categories,      to boost COD performance. Thus, we extend the proposed
i.e., sunny and low-light. The comparison results are shown         SP-Net to the RGB-D COD task.
in Fig. 9 (c). As can be seen, all models struggle more to de-          Dataset. We conduct this extension experiment on three
tect salient objects in low-light conditions, confirming that       public benchmark datasets for camouflaged object detec-
low-light negatively impacts SOD performance.                       tion, including 1) CHAMELEON [20] dataset, it consists
    4) Object Scale. To characterize the scale of a salient         of 76 camouflaged images, 2) CAMO [40] dataset, it has
object, we compute the ratio between the size of the salient        1, 250 images (1, 000 for training, 250 for testing) with
region and the whole image. Here three types of object              8 categories, and 3) COD10K [20] dataset, it consists of
scales can be defined: 1) when the ratio is less than 0.1,          5, 066 camouflaged images (3, 040 for training, 2, 026 for
Table 7. Comparison results of different camouflaged object detec-    the SOD performance. To learn the shared representations
tion models on benchmark datasets using two widely used evalu-
                                                                      for the two modalities, we introduce a cross-enhanced inte-
ation metrics (i.e., Sα [9] and M [63]). “↑“ & “↓” indicate that
                                                                      gration module (CIM) to fuse the cross-modal features, and
larger or smaller is better.
                                                                      the output of each CIM can be propagated to the next layer
                      CHAMELEON         CAMO           COD10K
                                                                      for exploring rich cross-level information. Besides, we
            Model     Sα ↑ M ↓        Sα ↑ M ↓        Sα ↑ M ↓
                                                                      adopt a multi-modal feature aggregation (MFA) module to
         FPN [48]     0.794   0.075   0.684   0.131   0.697   0.075
                                                                      integrate the learned modality-specific features for enhanc-
   MaskRCNN [30]      0.643   0.099   0.574   0.151   0.613   0.080
      PSPNet [92]     0.773   0.085   0.663   0.139   0.678   0.080
                                                                      ing the complementary multi-modal information. Extensive
     PiCANet [50]     0.769   0.085   0.609   0.156   0.649   0.090   results on benchmark datasets show the effectiveness of our
      BASNet [66]     0.687   0.118   0.618   0.159   0.634   0.105   model against other state-of-the-art RGB-D SOD methods.
      PFANet [96]     0.679   0.144   0.659   0.172   0.636   0.128   Moreover, we thoroughly validate the effectiveness of
         CPD [83]     0.853   0.052   0.726   0.115   0.747   0.059
                                                                      key components in our framework, and an attribute-based
       EGNet [93]     0.848   0.050   0.732   0.104   0.737   0.056
        SINet [20]    0.869   0.044   0.751   0.100   0.771   0.051
                                                                      evaluation is conducted to study the performance of many
                                                                      cutting-edge RGB-D SOD approaches under different
       DANet [98]     0.874   0.043   0.752   0.100   0.765   0.051
                                                                      challenging factors. Finally, we extend the proposed SP-
      HDFNet [60]     0.875   0.032   0.778   0.085   0.779   0.045
                                                                      Net to the recently proposed RGB-D camouflaged object
      SP-Net (Ours)   0.895   0.027   0.795   0.082   0.797   0.042
                                                                      detection task, and the effectiveness has also been validated.

testing) with 5 super-classes and 69 sub-classes. Following           References
the same setting in [21], we divide the training and testing
                                                                        [1] Radhakrishna Achanta, Sheila Hemami, Francisco Estrada,
sets and then train our model using the training set.
                                                                            and Sabine Susstrunk. Frequency-tuned salient region de-
   Comparison Methods. We compare with some exist-                          tection. In CVPR, pages 1597–1604. IEEE, 2009. 3, 6, 7
ing COD models, including FPN [48], MaskRCNN [30],                      [2] Ali Borji, Ming-Ming Cheng, Huaizu Jiang, and Jia Li.
PSPNet [92], PiCANet [50], BASNet [66], PFANet [96],                        Salient object detection: A benchmark.          IEEE TIP,
CPD [83], EGNet [93], and SINet [21]. Note that the re-                     24(12):5706–5722, 2015. 8
sults for the above results are collected from the work [21].           [3] Kamalika Chaudhuri, Sham M Kakade, Karen Livescu, and
Since there are fewer works designed for RGB-D cam-                         Karthik Sridharan. Multi-view clustering via canonical cor-
ouflaged object detection, we compare two recent RGB-                       relation analysis. In ICML, pages 129–136, 2009. 3
D salient object detection methods, i.e., DANet [98], and               [4] Hao Chen and Youfu Li. Progressively complementarity-
HDFNet [60], in this experiment. We re-train the two RGB-                   aware fusion network for RGB-D salient object detection.
D SOD models and our model using RGB and depth im-                          In CVPR, pages 3051–3060, 2018. 2, 3, 7, 8, 9
ages.                                                                   [5] Hao Chen and Youfu Li. Three-stream attention-aware
                                                                            network for RGB-D salient object detection. IEEE TIP,
   Results. Table 7 shows the quantitative results of dif-                  28(6):2825–2835, 2019. 2, 3, 6, 7, 8, 9
ferent COD methods on three public datasets. From the                   [6] Hao Chen, Youfu Li, Yongjian Deng, and Guosheng Lin.
results, it can be observed that our model performs better                  CNN-based RGB-D salient object detection: Learn, select,
than other comparison COD methods. Besides, it is worth                     and fuse. IJCV, pages 1–21, 2021. 1
noting that our model and two RGB-D COD methods with                    [7] Hao Chen, Youfu Li, and Dan Su. Multi-modal fusion net-
using depth cues perform better than other methods with-                    work with multi-scale multi-path and cross-modal interac-
out using them, which indicates the depth cues can pro-                     tions for RGB-D salient object detection. Pattern Recogni-
vide spatial information to improve the COD performance.                    tion, 86:376–385, 2019. 2, 7, 8, 9
Fig. 12 shows the qualitative results of different COD meth-            [8] Hao Chen, You-Fu Li, and Dan Su. Attention-aware cross-
ods. Compared with other COD models, we can see that our                    modal cross-level fusion network for RGB-D salient object
SP-Net can achieve better visual effects by detecting more                  detection. In IEEE IROS, pages 6821–6826. IEEE, 2018. 2,
                                                                            3, 6
accurate boundaries of camouflaged objects.
                                                                        [9] Ming-Ming Chen and Deng-Ping Fan. Structure-measure:
                                                                            A new way to evaluate foreground maps. IJCV, 129:2622–
5. Conclusion                                                               2638, 2021. 6, 7, 14
                                                                       [10] Shuhan Chen and Yun Fu. Progressively guided alternate
   In this paper, we present a novel RGB-D salient object                   refinement network for RGB-D salient object detection. In
detection framework, termed SP-Net. Different from most                     ECCV. Springer, 2020. 7, 8, 10
existing RGB-D SOD methods, which mainly focus on                      [11] Yupeng Cheng, Huazhu Fu, Xingxing Wei, Jiangjian Xiao,
learning shared representations, our SP-Net not only                        and Xiaochun Cao. Depth enhanced saliency detection
explores the shared cross-modal information but also                        method. In ICIMCS, pages 23–27, 2014. 6, 7, 9, 10, 11,
compensates modality-specific characteristics to improve                    13
       RGB                GT                  Depth                 SINet              DANet              HDFNet             SPNet

    Figure 12. COD results of our SPNet and three state-of-the-art COD methods (i.e., SINet [21], DANet [98], and HDFNet [60]).

[12] Runmin Cong, Jianjun Lei, Huazhu Fu, Junhui Hou, Qing-                      for binary foreground map evaluation. In IJCAI, pages 698–
     ming Huang, and Sam Kwong. Going from RGB to RGBD                           704, 2018. 7
     saliency: A depth-guided transformation model. IEEE                    [20] D.-P. Fan, G.-P. Ji, M.-M. Cheng, and L. Shao. Concealed
     TCYB, 2019. 7, 8                                                            object detection. IEEE TPAMI, 2021. 13, 14
[13] Runmin Cong, Jianjun Lei, Changqing Zhang, Qingming                    [21] Deng-Ping Fan, Ge-Peng Ji, Guolei Sun, Ming-Ming
     Huang, Xiaochun Cao, and Chunping Hou. Saliency de-                         Cheng, Jianbing Shen, and Ling Shao. Camouflaged ob-
     tection for stereoscopic images based on depth confidence                   ject detection. In CVPR, pages 2777–2787, 2020. 14, 15
     analysis and multiple cues fusion. SPL, 23(6):819–823,                 [22] Deng-Ping Fan, Zheng Lin, Zhao Zhang, Menglong Zhu,
     2016. 7, 8                                                                  and Ming-Ming Cheng. Rethinking RGB-D salient object
[14] Zijun Deng, Xiaowei Hu, Lei Zhu, Xuemiao Xu, Jing Qin,                      detection: Models, data sets, and large-scale benchmarks.
     Guoqiang Han, and Pheng-Ann Heng. R3net: Recurrent                          IEEE TNNLS, 32(5):2075–2089, 2021. 1, 3, 6, 7, 8, 9, 10,
     residual refinement network for saliency detection. In IJ-                  11, 13
     CAI. 3                                                                 [23] Deng-Ping Fan, Yingjie Zhai, Ali Borji, Jufeng Yang, and
[15] Karthik Desingh, K Madhava Krishna, Deepu Rajan, and                        Ling Shao. Bbs-net: RGB-D salient object detection with
     CV Jawahar. Depth really matters: Improving visual salient                  a bifurcated backbone strategy network. In ECCV, pages
     region detection with depth. In BMVC, 2013. 3                               275–292, 2020. 2
[16] Changxing Ding and Dacheng Tao. Robust face recogni-                   [24] David Feng, Nick Barnes, Shaodi You, and Chris Mc-
     tion via multimodal deep face representation. IEEE TMM,                     Carthy. Local background enclosure for RGB-D salient ob-
     17(11):2049–2058, 2015. 3                                                   ject detection. In CVPR, pages 2343–2350, 2016. 3, 7, 8
[17] Yu Ding, Zhi Liu, Mengke Huang, Ran Shi, and Xiangyang                 [25] Keren Fu, Deng-Ping Fan, Ge-Peng Ji, Qijun Zhao, Jian-
     Wang. Depth-aware saliency detection using convolutional                    bing Shen, and Ce Zhu. Siamese network for RGB-D
     neural networks. Journal of Visual Communication and Im-                    salient object detection and beyond. IEEE TPAMI, 2021.
     age Representation, 61:1–9, 2019. 1                                         1, 7, 8, 9, 10
[18] Andreas Eitel, Jost Tobias Springenberg, Luciano Spinello,             [26] Shang-Hua Gao, Ming-Ming Cheng, Kai Zhao, Xin-Yu
     Martin Riedmiller, and Wolfram Burgard. Multimodal deep                     Zhang, Ming-Hsuan Yang, and Philip Torr. Res2net: A new
     learning for robust rgb-d object recognition. In IROS, pages                multi-scale backbone architecture. IEEE TPAMI, 2020. 4,
     681–687. IEEE, 2015. 4                                                      8
[19] Deng-Ping Fan, Cheng Gong, Yang Cao, Bo Ren, Ming-                     [27] Mehmet Gönen and Ethem Alpaydın. Multiple kernel
     Ming Cheng, and Ali Borji. Enhanced-alignment measure                       learning algorithms. JMLR, 12:2211–2268, 2011. 3
[28] Jingfan Guo, Tongwei Ren, and Jia Bei. Salient object de-     [44] Gongyang Li, Zhi Liu, and Haibin Ling. Icnet: Information
     tection for RGB-D image via saliency evolution. In ICME,           conversion network for RGB-D based salient object detec-
     pages 1–6. IEEE, 2016. 1, 3, 7, 8                                  tion. IEEE TIP, 29:4873–4884, 2020. 7, 8
[29] Junwei Han, Hao Chen, Nian Liu, Chenggang Yan, and            [45] Gongyang Li, Zhi Liu, Linwei Ye, Yang Wang, and Haibin
     Xuelong Li. CNNs-based RGB-D saliency detection via                Ling. Cross-modal weighting network for RGB-D salient
     cross-view transfer and multiview fusion. IEEE TCYB,               object detection. In ECCV. Springer, 2020. 3
     48(11):3171–3183, 2017. 2, 3, 7, 8, 9                         [46] Lin Li, Bo Dong, Eric Rigall, Tao Zhou, Junyu Dong, and
[30] K.M. He, G. Gkioxari, P. Dollár, and R. Girshick. Mask            Geng Chen. Marine animal segmentation. IEEE TCSVT,
     r-cnn. In ICCV, 2017. 14                                           2021. 13
[31] Qibin Hou, Ming-Ming Cheng, Xiaowei Hu, Ali Borji,            [47] Fangfang Liang, Lijuan Duan, Wei Ma, Yuanhua Qiao, Zhi
     Zhuowen Tu, and Philip HS Torr. Deeply supervised salient          Cai, and Laiyun Qing. Stereoscopic saliency model using
     object detection with short connections. In CVPR, pages            contrast and depth-guided-background prior. Neurocomput-
     3203–3212, 2017. 3                                                 ing, 275:2227–2238, 2018. 3
[32] Junlin Hu, Jiwen Lu, and Yap-Peng Tan. Sharable and           [48] T.Y. Lin, P. Dollár, R. Girshick, K.M. He, B. Hariharan, and
     individual multi-view metric learning. IEEE TPAMI,                 S. Belongie. Feature pyramid networks for object detection.
     40(9):2281–2288, 2017. 2, 4                                        In CVPR, 2017. 14
[33] Zhou Huang, Huai-Xin Chen, Tao Zhou, Yun-Zhi Yang,            [49] Di Liu, Yaosi Hu, Kao Zhang, and Zhenzhong Chen. Two-
     and Bi-Yuan Liu. Multi-level cross-modal interaction net-          stream refinement network for RGB-D saliency detection.
     work for rgb-d salient object detection. Neurocomputing,           In ICIP, pages 3925–3929. IEEE, 2019. 2, 3, 6
     452:200–211, 2021. 2                                          [50] N. Liu, J.W. Han, and M.H. Yang. Picanet: Learning pixel-
[34] Wei Ji, Jingjing Li, Shuang Yu, Miao Zhang, Yongri Piao,           wise contextual attention for saliency detection. In CVPR,
     Shunyu Yao, Qi Bi, Kai Ma, Yefeng Zheng, Huchuan Lu,               2018. 14
     et al. Calibrated RGB-D salient object detection. In CVPR,    [51] Nian Liu, Junwei Han, and Ming-Hsuan Yang. Picanet:
     pages 9471–9481, 2021. 2                                           Learning pixel-wise contextual attention for saliency detec-
[35] Wei Ji, Jingjing Li, Miao Zhang, Yongri Piao, and Huchuan          tion. In CVPR, pages 3089–3098, 2018. 3
     Lu. Accurate RGB-D salient object detection via collabo-      [52] Nian Liu, Ni Zhang, and Junwei Han. Learning selec-
     rative learning. In ECCV, 2020. 7, 8                               tive self-mutual attention for RGB-D saliency detection. In
[36] Bo Jiang, Zitai Zhou, Xiao Wang, Jin Tang, and Bin Luo.            CVPR, 2020. 7, 8, 9, 10
     cmsalgan: RGB-D salient object detection with cross-view      [53] Nian Liu, Ni Zhang, Kaiyuan Wan, Ling Shao, and Junwei
     generative adversarial networks. IEEE TMM, 2020. 7, 8              Han. Visual saliency transformer. In ICCV, 2021. 1
[37] Zhuolin Jiang and Larry S Davis. Submodular salient re-       [54] Zhengyi Liu, Song Shi, Quntao Duan, Wei Zhang, and Peng
     gion detection. In CVPR, pages 2043–2050, 2013. 3                  Zhao. Salient object detection for RGB-D image by single
[38] Ran Ju, Ling Ge, Wenjing Geng, Tongwei Ren, and Gang-              stream recurrent convolution neural network. Neurocom-
     shan Wu. Depth saliency based on anisotropic center-               puting, 363:46–57, 2019. 1, 5
     surround difference. In ICIP, pages 1115–1119. IEEE,          [55] Yan Lu, Yue Wu, Bin Liu, Tianzhu Zhang, Baopu Li,
     2014. 3, 6, 7, 8, 9, 10, 11                                        Qi Chu, and Nenghai Yu. Cross-modality person re-
[39] Congyan Lang, Tam V Nguyen, Harish Katti, Karthik Ya-              identification with shared-specific feature transfer. In
     dati, Mohan Kankanhalli, and Shuicheng Yan. Depth mat-             CVPR, pages 13379–13389, 2020. 2, 4
     ters: Influence of depth cues on visual saliency. In ECCV,    [56] Ao Luo, Xin Li, Fan Yang, Zhicheng Jiao, Hong Cheng,
     pages 101–115. Springer, 2012. 3                                   and Siwei Lyu. Cascade graph neural networks for RGB-D
[40] T.N. Le, T.V. Nguyen, Z.L. Nie, M.T. Tran, and A. Sugi-            salient object detection. In ECCV. Springer, 2020. 7, 8
     moto. Anabranch network for camouflaged object segmen-        [57] Jiquan Ngiam, Aditya Khosla, Mingyu Kim, Juhan Nam,
     tation. CVIU, 2019. 13                                             Honglak Lee, and Andrew Y. Ng. Multimodal deep learn-
[41] Chongyi Li, Runmin Cong, Sam Kwong, Junhui Hou,                    ing. In ICML, 2011. 4
     Huazhu Fu, Guopu Zhu, Dingwen Zhang, and Qingming             [58] Yuzhen Niu, Yujie Geng, Xueqing Li, and Feng Liu. Lever-
     Huang. ASIF-Net: Attention steered interweave fusion net-          aging stereopsis for saliency analysis. In CVPR, pages 454–
     work for RGB-D salient object detection. IEEE TCYB,                461. IEEE, 2012. 6, 7, 9, 10, 11, 13
     2020. 7, 8                                                    [59] Youwei Pang, Lihe Zhang, Xiaoqi Zhao, and Huchuan Lu.
[42] Chongyi Li, Runmin Cong, Yongri Piao, Qianqian Xu,                 Hierarchical dynamic filtering network for RGB-D salient
     and Chen Change Loy. RGB-D salient object detection                object detection. In ECCV. Springer, 2020. 7, 8, 9
     with cross-modality modulation and selection. In ECCV.        [60] Youwei Pang, Lihe Zhang, Xiaoqi Zhao, and Huchuan Lu.
     Springer, 2020. 3, 7, 8                                            Hierarchical dynamic filtering network for RGB-D salient
[43] Gongyang Li, Zhi Liu, Minyu Chen, Zhen Bai, Weisi Lin,             object detection. In ECCV, 2020. 14, 15
     and Haibin Ling. Hierarchical alternate interaction network   [61] Youwei Pang, Xiaoqi Zhao, Lihe Zhang, and Huchuan Lu.
     for rgb-d salient object detection. IEEE Transactions on           Multi-scale interactive network for salient object detection.
     Image Processing, 30:3528–3542, 2021. 1                            In CVPR, pages 9413–9422, 2020. 3
[62] Houwen Peng, Bing Li, Weihua Xiong, Weiming Hu, and           [77] Wenguan Wang, Qiuxia Lai, Huazhu Fu, Jianbing Shen,
     Rongrong Ji. RGBD salient object detection: a benchmark            Haibin Ling, and Ruigang Yang. Salient object detection
     and algorithms. In ECCV, pages 92–109. Springer, 2014.             in the deep learning era: An in-depth survey. IEEE TPAMI,
     1, 3, 5, 6, 7, 8, 9, 10, 11, 13                                    2021. 3
[63] Federico Perazzi, Philipp Krähenbühl, Yael Pritch, and      [78] Wenguan Wang, Jianbing Shen, Ruigang Yang, and Fatih
     Alexander Hornung. Saliency filters: Contrast based filter-        Porikli. Saliency-aware video object segmentation. IEEE
     ing for salient region detection. In CVPR, pages 733–740.          TPAMI, 40(1):20–33, 2017. 1
     IEEE, 2012. 7, 14                                             [79] Xiang Wang, Huimin Ma, Xiaozhi Chen, and Shaodi You.
[64] Yongri Piao, Wei Ji, Jingjing Li, Miao Zhang, and Huchuan          Edge preserving and multi-scale contextual neural network
     Lu. Depth-induced multi-scale recurrent attention network          for salient object detection. IEEE TIP, 27(1):121–134,
     for saliency detection. In ICCV, pages 7254–7263, 2019. 3,         2017. 3
     6, 7, 8, 9                                                    [80] Jun Wei, Shuhui Wang, and Qingming Huang. F3Net: Fu-
[65] Yongri Piao, Zhengkun Rong, Miao Zhang, Weisong Ren,               sion, feedback and focus for salient object detection. AAAI,
     and Huchuan Lu. A2dele: Adaptive and attentive depth               2019. 6
     distiller for efficient RGB-D salient object detection. In    [81] Martha White, Xinhua Zhang, Dale Schuurmans, and Yao-
     CVPR, 2020. 7, 8, 9, 10                                            liang Yu. Convex multi-view subspace learning. In NIPS,
[66] X.B. Qin, Z.C. Zhang, C.Y. Huang, C. Gao, M. Dehghan,              pages 1673–1681, 2012. 3
     and M. Jagersand. Basnet: Boundary-aware salient object       [82] Zhe Wu, Li Su, and Qingming Huang. Cascaded partial
     detection. In CVPR, 2019. 14                                       decoder for fast and accurate salient object detection. In
                                                                        CVPR, pages 3907–3916, 2019. 4
[67] Liangqiong Qu, Shengfeng He, Jiawei Zhang, Jiandong
     Tian, Yandong Tang, and Qingxiong Yang. RGBD salient          [83] Z. Wu, L. Su, and Q.M. Huang. Cascaded partial decoder
     object detection via deep fusion. IEEE TIP, 26(5):2274–            for fast and accurate salient object detection. In CVPR,
     2285, 2017. 3, 7, 8                                                2019. 14
                                                                   [84] Yingjie Zhai, Deng-Ping Fan, Jufeng Yang, Ali Borji, Ling
[68] Konstantinos Rapantzikos, Yannis Avrithis, and Stefanos
                                                                        Shao, Junwei Han, and Liang Wang. Bifurcated backbone
     Kollias.      Dense saliency-based spatiotemporal feature
                                                                        strategy for rgb-d salient object detection. IEEE TIP, 2021.
     points for action recognition. In CVPR, pages 1454–1461,
                                                                        2
     2009. 1
                                                                   [85] Changqing Zhang, Qinghua Hu, Huazhu Fu, Pengfei Zhu,
[69] Jianqiang Ren, Xiaojin Gong, Lu Yu, Wenhui Zhou, and
                                                                        and Xiaochun Cao. Latent multi-view subspace clustering.
     Michael Ying Yang. Exploiting global priors for RGB-D
                                                                        In CVPR, pages 4279–4287, 2017. 3
     saliency detection. In CVPRW, pages 25–32, 2015. 1, 3
                                                                   [86] Jing Zhang, Deng-Ping Fan, Yuchao Dai, Saeed Anwar,
[70] Olaf Ronneberger, Philipp Fischer, and Thomas Brox. U-
                                                                        Fatemeh Saleh, Sadegh Aliakbarian, and Nick Barnes. Un-
     net: Convolutional networks for biomedical image segmen-
                                                                        certainty inspired RGB-D saliency detection. IEEE TPAMI,
     tation. In MICCAI, pages 234–241. Springer, 2015. 2, 4
                                                                        2021. 1, 3, 7, 8, 9, 10
[71] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause,          [87] Jing Zhang, Deng-Ping Fan, Yuchao Dai, Xin Yu, Yiran
     Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej                   Zhong, Nick Barnes, and Ling Shao. RGB-D saliency de-
     Karpathy, Aditya Khosla, et al. Imagenet large scale vi-           tection via cascaded mutual information minimization. In
     sual recognition challenge. IJCV, 115(3):211–252, 2015.            ICCV, 2021. 1
     4, 8
                                                                   [88] Jing Zhang, Yunqiu Lv, Mochu Xiang, Aixuan Li, Yuchao
[72] Wataru Shimoda and Keiji Yanai. Distinct class-specific            Dai, and Yiran Zhong. Depth confidence-aware camou-
     saliency maps for weakly supervised semantic segmenta-             flaged object detection. arXiv preprint arXiv:2106.13217,
     tion. In ECCV, pages 218–234. Springer, 2016. 1                    2021. 13
[73] Hangke Song, Zhi Liu, Huan Du, Guangling Sun, Olivier         [89] Lu Zhang, Ju Dai, Huchuan Lu, You He, and Gang Wang.
     Le Meur, and Tongwei Ren. Depth-aware salient ob-                  A bi-directional message passing model for salient object
     ject detection and segmentation via multiscale discrimi-           detection. In CVPR, pages 1741–1750, 2018. 3
     native saliency fusion and bootstrap learning. IEEE TIP,      [90] Miao Zhang, Weisong Ren, Yongri Piao, Zhengkun Rong,
     26(9):4204–4216, 2017. 1, 5, 7, 8                                  and Huchuan Lu. Select, supplement and focus for RGB-D
[74] Yujia Sun, Geng Chen, Tao Zhou, Yi Zhang, and Nian Liu.            saliency detection. In CVPR, 2020. 7, 8, 9, 10
     Context-aware cross-level fusion network for camouflaged      [91] Pingping Zhang, Dong Wang, Huchuan Lu, Hongyu Wang,
     object detection. IJCAI, 2021. 13                                  and Xiang Ruan. Amulet: Aggregating multi-level convo-
[75] Linzhao Wang, Lijun Wang, Huchuan Lu, Pingping Zhang,              lutional features for salient object detection. In ICCV, pages
     and Xiang Ruan. Salient object detection with recurrent            202–211, 2017. 3
     fully convolutional networks. IEEE TPAMI, 41(7):1734–         [92] H.S. Zhao, J.P. Shi, X.J. Qi, X.G. Wang, and J.Y. Jia. Pyra-
     1746, 2018. 3                                                      mid scene parsing network. In CVPR, 2017. 14
[76] Ningning Wang and Xiaojin Gong. Adaptive fusion for           [93] J.X. Zhao, J.J. Liu, D.P. Fan, Y. Cao, J.F. Yang, and M.M.
     RGB-D salient object detection. IEEE Access, 7:55277–              Cheng. Egnet: Edge guidance network for salient object
     55284, 2019. 1, 7, 8, 9                                            detection. In CVPR, 2019. 14
 [94] Jia-Xing Zhao, Yang Cao, Deng-Ping Fan, Ming-Ming
      Cheng, Xuan-Yi Li, and Le Zhang. Contrast prior and fluid
      pyramid integration for RGBD salient object detection. In
      CVPR, pages 3927–3936, 2019. 2, 3, 7, 8, 9
 [95] Rui Zhao, Wanli Oyang, and Xiaogang Wang. Per-
      son re-identification by saliency learning. IEEE TPAMI,
      39(2):356–370, 2016. 1
 [96] T. Zhao and X.Q. Wu. Pyramid feature attention network
      for saliency detection. In CVPR, 2019. 14
 [97] Xiaoqi Zhao, Lihe Zhang, Youwei Pang, Huchuan Lu, and
      Lei Zhang. A single stream network for robust and real-
      time RGB-D salient object detection. In ECCV. Springer,
      2020. 7, 8, 10
 [98] Xiaoqi Zhao, Lihe Zhang, Youwei Pang, Huchuan Lu, and
      Lei Zhang. A single stream network for robust and real-
      time RGB-D salient object detection. In ECCV, pages 646–
      662, 2020. 14, 15
 [99] Yifan Zhao, Jiawei Zhao, Jia Li, and Xiaowu Chen. Rgb-d
      salient object detection with ubiquitous target awareness.
      IEEE Transactions on Image Processing, 30:7717–7731,
      2021. 1
[100] Li Zhou, Zhaohui Yang, Qing Yuan, Zongtan Zhou,
      and Dewen Hu. Salient region detection via integrating
      diffusion-based compactness and local contrast. IEEE TIP,
      24(11):3308–3320, 2015. 3
[101] Tao Zhou, Deng-Ping Fan, Ming-Ming Cheng, Jianbing
      Shen, and Ling Shao. RGB-D salient object detection: A
      survey. Computational Visual Media, pages 1–33, 2021. 1,
      8
[102] Tao Zhou, Huazhu Fu, Geng Chen, Jianbing Shen, and Ling
      Shao. Hi-net: hybrid-fusion network for multi-modal MR
      image synthesis. IEEE TMI, 39(9):2772–2781, 2020. 2
[103] Tao Zhou, Huazhu Fu, Geng Chen, Yi Zhou, Deng-
      Ping Fan, and Ling Shao. Specificity-preserving RGB-D
      saliency detection. In ICCV, 2021. 3
[104] Tao Zhou, Changqing Zhang, Xi Peng, Harish Bhaskar, and
      Jie Yang. Dual shared-specific multiview subspace cluster-
      ing. IEEE TCYB, 50(8):3517–3530, 2019. 2
[105] Chunbiao Zhu, Xing Cai, Kan Huang, Thomas H Li, and Ge
      Li. PDNet: Prior-model guided depth-enhanced network
      for salient object detection. In ICME, pages 199–204, 2019.
      2
[106] Chunbiao Zhu and Ge Li. A three-pathway psychobiologi-
      cal framework of salient object detection using stereoscopic
      technology. In ICCVW, pages 3008–3014, 2017. 6, 7, 9, 10,
      11, 13
[107] Chunbiao Zhu, Ge Li, Wenmin Wang, and Ronggang
      Wang. An innovative salient object detection using center-
      dark channel prior. In ICCVW, pages 1509–1515, 2017. 3,
      7, 8
[108] Jun-Yan Zhu, Jiajun Wu, Yan Xu, Eric Chang, and
      Zhuowen Tu. Unsupervised object class discovery via
      saliency-guided multiple class learning. IEEE TPAMI,
      37(4):862–875, 2014. 1
[109] Wangjiang Zhu, Shuang Liang, Yichen Wei, and Jian Sun.
      Saliency optimization from robust background detection. In
      CVPR, pages 2814–2821, 2014. 3
