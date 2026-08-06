---
source_id: 053
bibtex_key: park2017rdfnet
title: RDFNet: RGB-D Multi-level Residual Feature Fusion for Indoor Semantic Segmentation
year: 2017
domain_theme: Segmentasi RGB-D
verified_pdf: 53_RDFNet.pdf
char_count: 72710
---

RDFNet: RGB-D Multi-level Residual Feature Fusion for
                            Indoor Semantic Segmentation

                 Seong-Jin Park                       Ki-Sang Hong                          Seungyong Lee
                   POSTECH                             POSTECH                                POSTECH
                                      {windray,hongks,leesy}@postech.ac.kr

                        Abstract
                                                                            &11            &11            &11            &11
    In multi-class indoor semantic segmentation using RGB-
D data, it has been shown that incorporating depth feature
into RGB feature is helpful to improve segmentation accu-
racy. However, previous studies have not fully exploited the
                                                                            &11            &11            &11            &11
potentials of multi-modal feature fusion, e.g., simply con-
catenating RGB and depth features or averaging RGB and
depth score maps. To learn the optimal fusion of multi-
                                                                                  00)            00)            00)            00)
modal features, this paper presents a novel network that ex-
                                                                                  1HW          1HW          1HW          1HW
tends the core idea of residual learning to RGB-D seman-
tic segmentation. Our network effectively captures multi-                                                                      5HILQH
level RGB-D CNN features by including multi-modal fea-                                                                         1HW
ture fusion blocks and multi-level feature refinement blocks.                                                   5HILQH
                                                                                                                1HW
Feature fusion blocks learn residual RGB and depth fea-
                                                                                                 5HILQH
tures and their combinations to fully exploit the comple-                                        1HW
mentary characteristics of RGB and depth data. Feature                            5HILQH
refinement blocks learn the combination of fused features                         1HW
from multiple levels to enable high-resolution prediction.
Our network can efficiently train discriminative multi-level
features from each modality end-to-end by taking full ad-
                                                                  Figure 1. Diagram of the proposed RDFNet for RGB-D seman-
vantage of skip-connections. Our comprehensive experi-            tic segmentation. The network fistly fuses multi-modal features
ments demonstrate that the proposed architecture achieves         through a block called MMFNet and refines the fused features
the state-of-the-art accuracy on two challenging RGB-D in-        through a series of RefineNet blocks.
door datasets, NYUDv2 and SUN RGB-D.

                                                                  Subsequent research [45, 29, 1, 3, 28] that incorporates the
1. Introduction                                                   CRF framework into DCNN further improved the accuracy.
                                                                  However, indoor semantic segmentation is still one of the
    Semantic segmentation that assigns all pixels into dif-       most challenging problem due to complex and various ob-
ferent semantic classes is a fundamental task for visual          ject configurations with severe occlusions.
scene understanding. In the past, there was broad research           With the availability of commercial RGB-D sensors such
for semantic segmentation based on conditional random             as Microsoft Kinect [44], it has been consistently proved
field (CRF) using conventional hand-crafted visual features       that utilizing features extracted from depth information is
[34, 23, 41]. Recently, deep convolutional neural networks        useful to reduce the uncertainty for recognizing objects
(DCNNs) have achieved great success in image classifi-            [32, 10, 20, 35, 6, 5, 11, 7, 25, 39, 13]. Depth features can
cation task [22, 43, 36, 14]. Built on the success of im-         describe 3D geometric information which might be missed
age recognition using DCNNs, many semantic segmenta-              in RGB-only features. To extract useful features from both
tion methods have also adopted DCNNs by extending them            RGB and depth data, it is crucial to develop an effective
to fully convolutional pixel-wise classification [30, 4, 42].     method for fusing two modalities. There have been many

                                                                4980
attempts to utilize the depth information for semantic seg-                Our main contributions can be summarized as follows:
mentation in different ways.
                                                                          1. We propose a network that effectively extracts and
    Previously most methods [32, 10, 20, 35, 6] designed
                                                                             fuses multi-level RGB-D features in very deep network
hand-crafted depth features and constructed various mod-
                                                                             by extending the core idea of residual learning to RGB-
els to classify each region or pixel. In contrast, recent ap-
                                                                             D semantic segmentation.
proaches [5, 11, 7, 25, 39, 13] employ DCNNs which suc-
cessfully learn informative RGB features from low level                   2. Our multi-modal feature fusion block enables efficient
primitives for high level semantics. As the main issue of                    end-to-end training of discriminative RGB-D features
RGB-D semantic segmentation is how to effectively ex-                        on a single GPU by taking full advantage of residual
tract and fuse depth features along with color features, vari-               learning with skip-connection.
ous approaches have been proposed to exploit the ability of
DCNN for integrating depth information. The approaches                    3. We show that our network for RGB-D semantic seg-
include concatenating input RGB and D channels, fusing                       mentation outperforms existing methods and achieves
score maps computed from each modality, extracting com-                      the state-of-the-art performance on two public RGB-D
mon and specific features for different modalities, and so                   datasets, NYUDv2 and SUN RGB-D.
on. Although previous approaches achieved meaningful re-
sults, there has been a lack of research that fully utilizes re-     2. Related Work
cent successful CNN architectures using skip-connections.               Since great advance in image classification task using
    In the case of RGB semantic segmentation, Lin et al. [26]        DCNN [22, 43, 36, 14], most recent semantic segmenta-
has recently achieved great success in utilizing multi-level         tion methods have employed DCNN. Long et al. [30] pro-
RGB features with different resolutions by iteratively fus-          posed a fully convolutional network (FCN) that extended
ing and refining them. They designed a network called Re-            DCNN image classification to dense pixel-wise classifica-
fineNet by taking advantage of residual learning with skip-          tion by convolutionalization.
connection [14, 15] that enables effortless backpropagation             The main limitation of the FCN-based methods is low-
of gradients during training. The multi-level features in            resolution prediction due to multiple pooling operations. To
RefineNet are connected through the short and long-range             resolve the limitation, there have been various approaches.
residual connections and thus can be efficiently trained and         One approach [42, 4] employed astrous convolution, also
merged into a high-resolution feature map.                           known as dilated convolution, which supports exponential
    Inspired by the work, we present a novel RGB-D fusion            expansion of the receptive field without loss of resolution.
network (RDFNet) that extends the core idea of residual              Chen et al. [4] additionally applied dense CRF method
learning to RGB-D semantic segmentation. We extend the               [21] to achieve detailed final prediction. Several follow-
RefineNet to effectively extract and fuse RGB and depth              up studies [45, 29, 1, 3, 28] proposed sophisticated meth-
features through residual feature fusion. Our network con-           ods to combine CRF framework into DCNNs. Another
sists of two feature fusion blocks: multi-modal feature fu-          approach [31, 2, 19] learned multiple deconvolution layers
sion (MMF) block and multi-level feature refinement (Re-             from low-resolution features to upsample the coarse feature
fine) block (Figure 1). The MMF block is crucial to ex-              map while recovering detailed boundaries.
ploit different modality of RGB and depth features. The                 The other approach [30, 12, 2, 33, 17, 26] exploited
block is constructed by mimicking the RefineNet block but            middle layer features to achieve high-resolution prediction.
with different inputs; The inputs are multi-level RGB and            Long et al. [30] designed a skip architecture and merged
depth features computed from deep residual network [14].             score maps computed from multi-level features to obtain
Then, it fuses the different modality features through resid-        the final prediction. Hariharan et al. [12] constructed a fea-
ual convolutional units and feature adaptation convolution,          ture vector called hypercolumn for every location by stack-
followed by optional residual pooling. The MMF block                 ing features from some or all of the layers in the network.
adaptively trains residual feature to effectively fuse the           Several methods [2, 33, 17] applied skip-connections in fea-
complementary features in different modalities, while learn-         ture upsampling procedures using deconvolution. In partic-
ing the relative importance of each modality feature. The            ular, Lin et al. [26] very recently achieved large improve-
block is subsequently followed by the Refine block to fur-           ment by designing a network called RefineNet that itera-
ther process the fused features for high-resolution seman-           tively refines higher-level features by employing low-level
tic segmentation. In this architecture, discriminative multi-        features through residual connections. The network effec-
level RGB and depth features can be effectively trained and          tively conveys the low-level features as well as semantic
fused, while retaining the key advantage of the skip con-            high-level features and it can be efficiently trained end-to-
nection, i.e., all the gradients effectively flow backwards          end. Our RGB-D network revises this state-of-the-art archi-
through residual connections to the ResNet input features.           tecture and takes the same advantage.

                                                                   4981
                                                                                      &11&11
                                                                                         &11
                                                                                      &11
                     &&              &11
                                    &11                                                                            
                      &               &11                                                                           
                     &               &11                                              &11&11                   
                                                                                         &11
                                                                                      &11

                                       (a)                                                         (b)
                    &RQY
                    &RQY               'HFRQY
                                        'HFRQY                                 &RQY&RQY      &RQY&RQY    'HFRQY
                                                                                                                  'HFRQY
                    &RQY                                                           &RQY                           'HFRQY
                                                                                                            'HFRQY
                    &RQY       77
                                        'HFRQY
                                       'HFRQY
                                                                              &RQY        &RQY&RQY 

                    &RQY
                    &RQY
                               77      'HFRQY
                                        'HFRQY
                                                                             &RQY
                                                                                  &RQY        &RQY
                                                                                                  &RQY
                    &RQY
                    &RQY                'HFRQY
                                       'HFRQY                                      &RQY
                                                                                &RQY          &RQY&RQY

                                       (c)                                                         (d)

Figure 2. Different existing architectures for RGB-D semantic segmentation. (a) early fusion, (b) late fusion, (c) the architecture proposed
by [39], (d) the architecture proposed by [13], where ‘C’, ‘T’, and ‘+’ represent the concatenation, transformation, and element-wise
summation, respectively.

    For indoor semantic segmentation, a variety of methods               by discovering common and modality specific features. It
utilizing depth information have been studied. Previously,               does not exploit any informative intermediate features of
most methods [32, 10, 20, 35, 6] computed hand-crafted                   both modalities and it adopts simple score fusion of two
features specifically designed for capturing depth features              modalities at the end of the network for final prediction.
as well as color features. Then, they constructed a model                The training procedures consist of two stages rather than
to classify each region such as superpixel based on the fea-             end-to-end. Hazirbas et al. [13] proposed a method that ex-
tures.                                                                   ploits intermediate depth features (Figure 2 (d)). However,
    In contrast, recent methods [5, 11, 7, 25, 39, 13] usu-              as they simply sum intermediate RGB and depth features
ally employ DCNN that automatically trains features cap-                 only in encoder part, it does not fully exploit effective mid-
turing different levels of representations. Couprie et al. [5]           level RGB-D features, reporting accuracy worse than the
extended multi-scale RGB CNN architecture [8] to RGB-                    state-of-the-art RGB-only CNN architecture [27].
D situation by simply concatenating input color and depth                   In this paper, we propose a network that effectively ex-
channels, i.e., early fusion (Figure 2 (a)). Long et al. [30]            ploits multi-level RGB and depth features simultaneously.
additionally reported the result of fusing two predictions               Our network is trained to obtain optimal fusion of two com-
made by each RGB and depth modality, i.e., late fusion                   plementary modality features through residual learning with
(Figure 2 (b)), as well as the result of early fusion. Gupta             skip-connection and iteratively refines the fused features.
et al. [11] generalized the R-CNN system introduced by                   The multi-path residual feature fusion with skip-connection
Girshick et al. [9] to leverage depth information. For that              allows the backward gradient to easily propagate to both
purpose, they encoded the depth image with three channels                RGB and depth layers. In this way, the network trains end-
called HHA at each pixel: horizontal disparity, height above             to-end the discriminative RGB-D features which should be
ground, and angle with gravity. Li et al. [25] captured and              fused from low to high level.
fused contextual information from RGB and depth features
through bi-directional vertical and horizontal LSTM layers               3. Multi-level Residual Feature Fusion
[38]. They used rather simple architecture especially for
depth feature and partly utilized only RGB intermediate fea-                 Utilizing multi-level features is important for high reso-
tures through simple feature concatenation.                              lution dense prediction. Existing RGB-D semantic segmen-
    There have been encoder-decoder architectures [39, 13]               tation approaches do not effectively extract or fuse those
similarly to RGB deconvolution-based methods. Wang et                    features in the two modalities. We propose a network that
al. [39] proposed a structure for deconvolution of multi-                exploits multi-level RGB-D features and effectively fuses
ple modalities (Figure 2 (c)). It contains additional feature            the features in different modalities through residual learn-
transformation network that correlates the two modalities                ing with skip-connections.

                                                                     4982
        &11                 &11                           &11                                              &11
             CNN                       CNN                CNN                                             CNN
                                                                                                                     5HILQH

                                                                                                                                                                                                                                                                      &KDLQHG5HVLGXDO
                                                                                                                                                                                                                        0XOWL5HVROXWLRQ
                                                                                                                     Refine
                                                                                                                      1HW                                                                          5&8          5&8
                                                                                                                     Net-4

                                                                                                                                                                                                                                                                          3RROLQJ
                                                                     5HILQH

                                                                                                                                                                                                                             )XVLRQ
                                                                     Refine
                                                                                                                                                                                                                                                                                                         5&8

                                                                                                                       &KDLQHG5HVLGXDO3RROLQJ
                                                                     1HW

                                                                                0XOWLUHVROXWLRQ)XVLRQ
                                                                      Net-3
                                          5HILQH
                                            Refine
                      5&8                  5&8                                                                                                                                                       5&8          5&8
                                          1HW
                                            Net-2
                 Refine
              5HILQH
                  Net-1
              1HW                                                                                                                                                    5&8                                                                                                                5HILQH1HW

                      5&8                      5&8
Figure 3. Building blocks of the network proposed by [26]. Left: network architecture for semantic segmentation. Right: detailed diagram
of RefineNet block.                                              5HILQH1HW

                                                                                                                                                                                                                                                                                                     ൈ&RQY
                                                                                                                                                                                                                                                                                          ൈ3RRO
                                                                                                                                                         ൈ&RQY

                                                                                                                                                                       8SVDPSOH
                            ൈ&RQY

                                               ൈ&RQY
                     5H/8

                                        5H/8

                                                                                                                                                                                                                                                                         ൈ&RQY
                                                                                                                                                                                                                                                       ൈ3RRO
                                                                                                                                                                                                
                                                          
                                                                                                                                                         ൈ&RQY

                                                                                                                                                                       8SVDPSOH

                                                                                                                                                                                              0XOWL
                                                                                                                                                                                             5HVROXWLRQ
                                                                                                                                                                                                                                5H/8                                                                           
                                                   5&8                                                                                                                                        )XVLRQ                                                                                                 &53

           5*%                                                                  Figure 4. Details of the sub-modules in RefineNet.
                                                                     ൈ&RQY

                                                                                                          ൈ&RQY

                                                                                                                                                            ൈ&RQY

                                                                                                                                                                                  ൈ&RQY

          IHDWXUH
                                                              5H/8

                                                                                              5H/8

                                                                                                                                                  5H/8

                                                                                                                                                                        5H/8

                                                                                                                                                                                                                                                           ൈ&RQY
                                                                                                                                                                                                       ൈ&RQY

                                                                                                                                                                                                                                            ൈ3RRO
   In this section, we first review the recently proposed Re-                                                                                                                     higher-resolution feature map. One convolution in the block
fineNet architecture ൈ&RQY                       in RGB
                      [26] that achieved great success                                                                                                                            is forinput adaptation, which matches the number of feature
semantic segmentation by employing residual connections.                                                                                                                          channels and re-scales the feature values appropriately for
                                                                     ൈ&RQY

                                                                                                          ൈ&RQY

                                                                                                                                                            ൈ&RQY

                                                                                                                                                                                  ൈ&RQY
                                                                                                                                                  5H/8

                                                                                                                                                                        5H/8
                                                              5H/8

                                                                                              5H/8

Then, we describe our network that extends the RefineNet                                                                                                                          summation. The purpose 5H/8                pooling
                                                                                                                                                                                                             of chained residual     5HILQH (CRP)
to effectively train the way to extract and fuse multi-level                                                                                                                      is to encode contextual information from a large region. The
                                                                                                                                                                                                       ൈ&RQY

RGB and depth features     for indoor semantic segmentation.
                      ൈ&RQY                                                                                                                                                   blockconsists of a chain of multiple pooling blocks, each
                                                                                                                                                                                  consisting of one max-pooling     layer and one convolution
                                                                                                                                                                                                        0XOWL0RGDO)HDWXUH
3.1. Review of RefineNet
         'HSWK                                                                                                                                                                   layer. The pooling operation    has an
                                                                                                                                                                                                         )XVLRQ 00)   QHWeffect that spreads the
           IHDWXUH                                                                                                                                                                large activation values which can be accessed from nearby
    Recently ResNet [14, 15] has shown outstanding perfor-                                                                                                                        locations as contextual features. The additional convolution
mance on image recognition. The simplest way to employ                                                                                                                            layer learns the importance of the pooled feature, which is
the ResNet to semantic segmentation is replacing the single                                                                                                                       fused to the original feature through residual connection.
label prediction layer with a dense prediction layer. How-                                                                                                                        There is an additional RCU at the end of the RefineNet to
ever, it outputs prediction with 32 times smaller in each spa-                                                                                                                    employ non-linearity operations on the fused feature maps.
tial dimension than the original image. To address the lim-
                                                                                                                                                                                      The core design philosophy of the RefineNet is mo-
itation, RefineNet iteratively refines higher-level features
                                                                                                                                                                                  tivated by the advantage of identity mapping with skip-
by incorporating low-level features through sub-building
                                                                                                                                                                                  connection [15]. The residual connections enable efficient
blocks, called RefineNet (Figure 3).
                                                                                                                                                                                  backward propagation of gradients through RefineNet and
    The RefineNet takes as inputs each multi-level ResNet                                                                                                                         facilitates end-to-end training of the multi-path network.
feature through skip connection and the previously re-
fined feature. Then, those features are refined and fused                                                                                                                         3.2. Our RDFNet with Multi-Modal Feature Fusion
through a series of sub-components: residual convolutional
unit, multi-resolution fusion, and chained residual pool-                                                                                                                            The main issue of RGB-D semantic segmentation is how
ing (Figure 4); The residual convolution unit (RCU) is                                                                                                                            to effectively extract depth features along with color fea-
an adaptive convolution set that fine-tunes the pretrained                                                                                                                        tures and to utilize those features for the desired task of se-
ResNet weights for semantic segmentation. The multi-                                                                                                                              mantic segmentation. The RefineNet described in Section
resolution fusion block fuses the multi-path input into a                                                                                                                         3.1 proposed a generic means for fusing different levels of

                                                                                                                                                                         4983
                                                                                                                                                                   ൈ
                                                                                                                                                                                ൈ
                

                          
                                                                                                                          
                              

                                                                                 ൈ&RQY

                                                                                               8SVDPSOH
                                                                                                                       0XOWL
                                                                                                                      5HVROXWLRQ
                                                                                                                                                     5H/8                                           
                          5&8                                                                                          )XVLRQ                                                                  &53

    5*%

                                         ൈ&RQY

                                                           ൈ&RQY

                                                                                    ൈ&RQY

                                                                                                           ൈ&RQY
   IHDWXUH

                                  5H/8

                                                    5H/8

                                                                          5H/8

                                                                                                5H/8

                                                                                                                                                                     ൈ&RQY
                                                                                                                                 ൈ&RQY

                                                                                                                                                        ൈ3RRO
               ൈ&RQY                                                                                                 

                                         ൈ&RQY

                                                           ൈ&RQY

                                                                                    ൈ&RQY

                                                                                                           ൈ&RQY
                                  5H/8

                                                    5H/8

                                                                          5H/8

                                                                                                5H/8
                                                                                                                                                5H/8                                          5HILQH

                                                                                                                                 ൈ&RQY
               ൈ&RQY                                                                                                 
                                                                                                                                             0XOWL0RGDO)HDWXUH
   'HSWK                                                                                                                                   )XVLRQ 00) QHWZRUN
   IHDWXUH

                                   Figure 5. Diagram of our multi-modal feature fusion (MMF) network.

features, which is more effective than simple feature con-                                                            confusing patterns. The importance of each modality fea-
catenation. In this paper, we employ a similar architecture                                                           ture can be controlled by the learnable parameters in the
for multi-modal CNN feature fusion while retaining the ad-                                                            convolution after RCUs.
vantage of skip connection.                                                                                               Finally, we perform an additional residual pooling op-
   Our RDFNet extends the RefineNet to handle multi-                                                                  eration to incorporate certain contextual information in the
modal feature fusion and includes RefineNet blocks for                                                                fused feature. We found one residual pooling in MMFNet of
fused feature refinement. The overall diagram of our net-                                                             each level is enough. The stronger contextual information
work is illustrated in Figure 1. Differently from existing                                                            can be further incorporated in the following multi-level fu-
networks that utilize depth information (Figure 2), our net-                                                          sion through RefineNet blocks. Note that we skip the addi-
work is designed to fully exploit multi-level depth features                                                          tional RCU at the end of original RefineNet in our MMFNet
through MMF blocks with an additional deep depth feature                                                              because the output of our MMFNet directly goes through
path based on ResNet [14].                                                                                            the RCUs in the fore part of the RefineNet.
    The detailed components of our MMFNet is shown in                                                                     Our network is constructed to retain the philosophy of
Figure 5. Our feature fusion block consists of the same                                                               the RefineNet by employing residual learning with skip-
components as in RefineNet but with different inputs, from                                                            connections through all the layers, which facilitates both of
which desired operations are slightly different. Given RGB                                                            effective multi-level RGB and depth feature extraction and
and depth ResNet features, our MMFNet first reduces the                                                               efficient end-to-end training.
dimension of each feature through one convolution to fa-                                                              3.3. Architecture details
cilitate efficient training while mitigating explosion of pa-
rameters. Then, each feature goes through two RCUs and                                                                   Following the success of Gupta et al. [11], We encode
one convolution as in RefineNet. There is a certain dif-                                                              the depthmap to a 3D image called HHA [10], which can be
ference between the purpose of RCUs in MMFNet and                                                                     directly used as an input of the pre-trained network path for
those in RefineNet. The RCUs in our MMFNet are desired                                                                depth feature along with fine-tuning. The HHA representa-
to perform some nonlinear transformations specifically for                                                            tion encodes the properties of geocentric poses that empha-
modality fusion. Two features in different modalities are                                                             size complementary discontinuities in the image, which is
complementarily combined to improve each other through                                                                hard to be trained through convolutional network. We com-
the operations, where as those in RefineNet are mainly to                                                             pute depth features through ResNet with the same number
refine coarse higher level feature by employing lower level                                                           of layers as RGB.
feature with higher-resolution. Subsequent additional con-                                                               As depicted in Figure 1, we utilize 4-level RGB and
volution in MMFNet is crucial to adaptively fuse features                                                             depth features with different resolutions similarly to the
in different modalities as well as re-scaling the feature val-                                                        RefineNet. We take res5, res4, res3, and res2 features in
ues appropriately for summation. As color features gener-                                                             ResNet [14] as inputs to our MMFNet. For each MMFNet,
ally have better discrimination power than depth features for                                                         we include a dropout layer for regularization with ratio
semantic segmentation, the summation fusion in the block                                                              of 0.5 before 1×1 convolution. The MMFNet consists
mainly works to learn supplementary or residual depth fea-                                                            of ReLU nonlinearity, 3×3 convolution, and 5×5 pooling
tures which might improve RGB features to discriminate                                                                layer with stride of 1 and the number of filters (channels) in

                                                                                                          4984
the block is set to 512 for MMFNet-4 and 256 for the oth-                                data     pixel acc.   mean acc.   IoU
ers. RefineNet blocks take the fused features and the pre-           Gupta et al. [11] RGB-D          -       35.1    -
viously refined feature as inputs except RefineNet-4 which           Eigen et al. [7]  RGB-D        65.6      45.1   34.1
only takes a fused feature from res5. The RefineNet-4 does           FCN [30]          RGB-D        65.4      46.1   34.0
not perform multi-resolution fusion. The number of fil-              Wang et al. [39]  RGB-D          -       47.3    -
ters in each RefineNet is set to the same as those of each           Context [27]       RGB         70.0      53.6   40.6
                                                                     Refine-101 [26]    RGB         72.8      57.8   44.9
MMFNet output. Final feature map obtained by RefineNet-
                                                                     Refine-152 [26]    RGB         73.6      58.9   46.5
1 goes through two additional RCUs, then another 1×1 con-
                                                                     RDF-152 (ours)    RGB-D        76.0      62.8   50.1
volution for the prediction with a dropout layer with ratio of     Table 1. Semantic segmentation accuracy on NYUDv2. Our
0.5. We add a softmax loss layer for loss computation. Our         RDFNet outperforms all existing methods.
network with MMF blocks can be efficiently trained on a
single GPU while fully utilizing the potentials of extremely                            pixel acc.    mean acc.    IoU
deep RGB-D network.
                                                                           RDF-50          74.8         60.4       47.7
4. Experiments                                                             RDF-101         75.6         62.2       49.1
                                                                           RDF-152         76.0         62.8       50.1
   In this section, we evaluate our network through compre-        Table 2. Semantic segmentation accuracy on NYUDv2 of our net-
hensive experiments. We use two publicly available RGB-            work with variants of the pre-trained residual network.
D datasets: NYUDv2 [35] and SUN RGB-D [37]. For the
evaluation, we report three types of metrics (pixel accuracy,
mean accuracy, and mean intersection over union (IoU))             methods, demonstrating that our network effectively uti-
widely-used to measure the performance of semantic seg-            lizes depth information. It improves the accuracy of RGB-
mentation [30]. As mentioned before, we use HHA encod-             only RefineNet by 2.4%, 3.9%, and 3.6% for pixel accuracy,
ing computed from a depthmap as our depth modality input.          mean accuracy, and mean IoU, respectively.
                                                                       As the multi-level features of our network are not lim-
4.1. Training details                                              ited to a specific pre-trained network, we report the accura-
    We implemented our network using the publicly avail-           cies of our network using residual networks with different
able Caffe toolbox [18] with an Nvidia GTX Titan X GPU.            number of layers, i.e., Res-50, Res-101, and Res-152. The
We employed general data augmentation schemes: random              results are shown in Table 2. It shows that the deeper the
scaling, random cropping, and random flipping. We applied          network becomes, the better results we generally get, while
test-time multi-scale evaluation for all experiments by aver-      the amount of improvement decreases. It is noteworthy that
aging the resulting predictions. We set the momentum and           the accuracy of our network with Res-50 using RGB-D data
weight decay to 0.9 and 0.0005, respectively. We used the          (RDF-50) is higher than those of RefineNet with Res-152
initial learning rate of 10−4 and divided it by 10 when the        using RGB data (Refine-152 [26]).
loss converges to a certain range and stops decreasing. We             Class-wise accuracies of our results compared with those
multiplied the learning rate by 0.1 for the base ResNet lay-       of RefineNet are shown in Table 3. Our results show signifi-
ers. All the parameters not in the base ResNet are initialized     cant improvement in most categories by effectively employ-
by a normal distribution with zero mean and 10−2 variance,         ing depth features, especially in categories with clear geo-
while the biases were initialized with zero.                       metric distinction such as table, counter, and dresser. The
                                                                   lower accuracy reported for the board class is due to the fact
4.2. NYUDv2                                                        that there are few images containing boards in the dataset. It
   NYUDv2 [35] is one of the most popular RGB-D                    is also hard to improve the discrimination between a board
dataset, which contains 1449 densely labeled pairs of RGB          and a picture with little geometric differences even using
and depth images captured by using Microsoft Kinect. The           additional depth features.
dataset also provides inpainted depthmaps computed by the              We validate our network in Table 4 by comparing with
colorization method of Levin et al. [24], and we used the          other variants. Here we use Res-101 for the experiments.
inpainted depthmaps for experiments. Following the stan-           We first report the accuracies of depth-only networks to
dard train/test split, we use 795 training images and 654 test     show that the RefineNet also works properly for extract-
images. We evaluate our network for 40 classes using the           ing depth features from HHA encoding, which validates
labels provided by [10].                                           our choice of depth feature part. We trained a RefineNet
   We first compare our RDFNet with the existing indoor            model based on ResNet features finetuned using only HHA
semantic segmentation methods using CNN features. The              input. The accuracy of RefineNet only using HHA (Refine-
results are shown in Table 1. It shows that our network            HHAonly) is even higher than FCN using both RGB and
outperforms all existing RGB-D methods as well as RGB              HHA. This result demonstrates that ResNet with finetuning

                                                                 4985
                         wall       floor      cabinet       bed      chair     sofa     table      door     window     bkshelf
   Refine-101 [26]       77.5       82.9         58.7       65.7      59.1     57.8       40.1       36.7     45.8        42.8
   RDF-101               78.8       87.3         63.0       71.6      65.1     62.8       49.7       39.5     48.5        46.5
   RDF-152               79.7       87.0         60.9       73.4      64.6     65.4       50.7       39.9     49.6        44.9
                        picture    counter      blind       desk      shelf   curtain   dresser    pillow    mirror       mat
   Refine-101 [26]       60.1       56.8         61.4       22.6      12.3     53.5       38.3       39.6     38.7        29.7
   RDF-101               60.8       65.5         61.5       30.8      12.4     54.0       54.0       46.6     55.5        41.6
   RDF-152               61.2       67.1         63.9       28.6      14.2     59.7       49.0       49.9     54.3        39.4
                        cloths     ceiling      books      refridg      tv     paper     towel     shower      box       board
   Refine-101 [26]       24.4       66.0         33.0       52.4      52.6     31.3       36.8       23.6     11.1        63.7
   RDF-101               26.3       69.7         36.0       55.7      63.2     34.6       39.1       38.5     13.1        46.0
   RDF-152               26.9       69.1         35.0       58.9      63.8     34.1       41.6       38.5     11.6        54.0
                        person      stand       toilet      sink      lamp    bathtub     bag       othstr   othfurn    othprop
   Refine-101 [26]       78.6       38.6         68.4       53.2      45.9     32.9       14.6       32.9     18.7        36.4
   RDF-101               81.8       42.5         68.9       56.1      45.8     49.0       13.4       31.0     19.5        38.6
   RDF-152               80.0       45.3         65.7       62.1      47.1     57.3       19.1       30.7     20.6        39.0
                               Table 3. Class-wise semantic segmentation accuracy (IoU) on NYUDv2.

                           pixel acc.    mean acc.       IoU                                data     pixel acc.   mean acc.   IoU
    FCN32-HHAonly             58.3         35.7          25.2            Ren et al. [32]   RGB-D            -         36.3  -
    Refine-HHAonly            66.5         46.5          36.3            B-SegNet [19]      RGB          71.2         45.9 30.7
    Refine-Concat             74.5         59.2          47.0            LSTM [25]         RGB-D            -         48.1  -
                                                                         FuseNet [13]      RGB-D         76.3         48.3 37.3
    RDF-101                   75.6         62.2          49.1
                                                                         Context [28]       RGB          78.4         53.4 42.3
     -Without RP              75.4         61.1          48.7
                                                                         Refine-152 [26]    RGB          80.6         58.5 45.9
      -Without conv           74.7         59.6          47.7            RDF-152 (ours) RGB-D            81.5         60.1 47.7
       -Without skip          73.8         58.7          45.8          Table 5. Semantic segmentation accuracy on SUN RGB-D. Our
    RDF-101-depth             75.3         60.9          48.2          RDFNet achieves the state-of-the-art accuracy.
     Table 4. Comparison for different variants of network.

                                                                       tively controls the weight to fuse each modality feature, we
can extract appropriate features from depth data.                      obtained much less accuracy while it is only slightly higher
   We also compare our MMFNet with a baseline fusion                   than those of concat fusion. We additionally report the accu-
method. For the comparison, we replace our MMFNet with                 racy without skip connection in RCUs (Without skip). Here
feature concatenation fusion with additional dropout layer             the features directly go through the nonlinearity transforma-
and one convolution layer for dimension reduction. Here                tions and sum fusion. By comparing the accuracies, we can
we only compare with the multi-level concatenation fusion              see the importance of skip connection for effective end-to-
(Refine-Concat) because we found that it generally shows               end training of multi-level features.
better accuracy than other fusion architectures (early fusion,            We finally report the result of our network trained di-
late fusion, and other variations). Note that the results show         rectly on depth data instead of HHA to show that our
that our MMFNet effectively utilizes multi-modal features,             network can be applied to different types of RGBD in-
achieving higher accuracies for all metrics, specifically by           puts. We preprocessed the depth to roughly scale the val-
1.1%, 3.0%, and 2.1%, respectively. It confirms that the im-           ues into the range of 0 ∼ 255. Specifically, we simply used
provement specifically comes from MMF rather than simple               k/depth, similarly to the disparity channel in HHA, where
addition of depth information.                                         k is a constant. The result (RDF-101-depth) shows consis-
   We additionally conduct ablative experiments for our                tent improvement over RefineNet while slightly worse than
MMFNet by successively eliminating each component (Ta-                 our RDFNet with HHA (RDF-101). It indicates that our
ble 4). Without residual pooling (Without RP) the accu-                RDFNet can efficiently learn to extract meaningful features
racy decreases slightly, which means the additional residual           directly from the depth data as well.
pooling is rather optional. We found further pooling did
                                                                       4.3. SUN RGB-D
not improve the accuracy. However, the experiments show
that the other components are crucial for effective feature              SUN RGB-D dataset [37] has been built for a large-scale
fusion. Without the convolution (Without conv) that adap-              RGB-D benchmark. The dataset consists of 10335 pairs of

                                                                     4986
 (a)                                                                    (b)

 (c)                                                                    (d)

 (e)                                                                    (f)

 (g)                                                                    (h)

 (i)                                                                    (j)

Figure 6. Qualitative results of our RDFNet compared with RefineNet [26]. From left to right for each example: image, ground truth, the
results obtained by RefineNet, and ours. Note that the depth features help to discriminate regions that might be confusing only with color
features, e.g., pillow with patterns similar to bed (a), the door with a homogeneous pattern (b, e), ceiling with clear geometric distinction
(c), counter with vertical surface normal (d, f), cabinet with low illumination (g), mirror reflecting other color patterns (a, b), floor mat on
the floor (h), and top surface of a table (c,i). The last example shows a failure case of ours (j). Best viewed in color.

RGB and depth images captured from four different depth                       5. Conclusion
sensors, which contains images from NYUDv2 depth [35],
Berkeley B3DO [16], and SUN3D [40], as well as newly                             We proposed a novel network that takes full advantage of
captured images. We use the standard split of 5285 training                   residual learning with skip-connection to extract effective
images and 5050 test images with pixel-wise labeling of 37                    multi-modal CNN features for semantic segmentation. The
classes for evaluation.                                                       residual architecture facilitates efficient end-to-end training
                                                                              of very deep RGB-D CNN features on a single GPU. Our
   Table 5 shows that our network outperforms existing                        MMFNet shows that the recent multi-level feature refine-
RGB-D methods by a large margin. It also achieves the                         ment architecture [26] can be effectively extended to utilize
state-of-the-art accuracy for all metrics, improving the ac-                  features in different modalities, while retaining the advan-
curacy of RGB-only RefineNet by a considerable amount.                        tage of skip-connection. Our experiments demonstrated that
The ability of depth feature might be slightly diminished                     the proposed network outperforms existing methods, ob-
for this dataset because it contains many bad depth images                    taining the state-of-the-art mean IoUs of 50.1% and 47.7%
with invalid measurements, e.g., images obtained by Re-                       for NYUDv2 and SUN RGB-D indoor datasets, respec-
alSense RGB-D camera. Nevertheless, the results demon-                        tively.
strate that our network learns effective RGB-D features on a
large-scale dataset even without manually weeding the bad
images out.                                                                   Acknowledgements This work was supported by the
                                                                              Ministry of Science and ICT, Korea, through IITP grant
                                                                              (R0126-17-1078), Giga Korea grant (GK17P0300), and
4.4. Qualitative results                                                      NRF grant (NRF-2014R1A2A1A11052779).
   We show some qualitative results of ours compared with
RefineNet [26] in Figure 6. We obtained the results of the                    References
RefineNet by running the publicly available source code                        [1] A. Arnab, S. Jayasumana, S. Zheng, and P. H. Torr. Higher
with the provided model based on Res-101. We compare                               order conditional random fields in deep neural networks. In
the results with our RDF-101 using RGB-D inputs. The                               Proc. ECCV, pages 524–540. Springer, 2016. 1, 2
comparisons illustrate that our network effectively utilizes                   [2] V. Badrinarayanan, A. Kendall, and R. Cipolla. Segnet: A
depth features to discriminate regions that might be confus-                       deep convolutional encoder-decoder architecture for image
ing with only color features.                                                      segmentation. arXiv preprint arXiv:1511.00561, 2015. 2

                                                                       4987
 [3] S. Chandra and I. Kokkinos. Fast, exact and multi-scale in-        [19] A. Kendall, V. Badrinarayanan, and R. Cipolla. Bayesian
     ference for semantic image segmentation with deep gaussian              segnet: Model uncertainty in deep convolutional encoder-
     crfs. In Proc. ECCV, pages 402–418. Springer, 2016. 1, 2                decoder architectures for scene understanding.             arXiv
 [4] L.-C. Chen, G. Papandreou, I. Kokkinos, K. Murphy, and                  preprint arXiv:1511.02680, 2015. 2, 7
     A. L. Yuille. Semantic image segmentation with deep con-           [20] S. H. Khan, M. Bennamoun, F. Sohel, and R. Togneri. Ge-
     volutional nets and fully connected crfs. arXiv preprint                ometry driven semantic labeling of indoor scenes. In Proc.
     arXiv:1412.7062, 2014. 1, 2                                             ECCV, pages 679–694. Springer, 2014. 1, 2, 3
 [5] C. Couprie, C. Farabet, L. Najman, and Y. LeCun. Indoor se-        [21] V. Koltun. Efficient inference in fully connected crfs with
     mantic segmentation using depth information. arXiv preprint             gaussian edge potentials. In Proc. NIPS, 2011. 2
     arXiv:1301.3572, 2013. 1, 2, 3                                     [22] A. Krizhevsky, I. Sutskever, and G. E. Hinton. Imagenet
 [6] Z. Deng, S. Todorovic, and L. Jan Latecki. Semantic seg-                classification with deep convolutional neural networks. In
     mentation of rgbd images with mutex constraints. In Proc.               Proc. NIPS, pages 1097–1105, 2012. 1, 2
     ICCV, pages 1733–1741, 2015. 1, 2, 3                               [23] L. Ladickỳ, P. Sturgess, K. Alahari, C. Russell, and P. H.
 [7] D. Eigen and R. Fergus. Predicting depth, surface normals               Torr. What, where and how many? combining object de-
     and semantic labels with a common multi-scale convolu-                  tectors and crfs. In Proc. ECCV, pages 424–437. Springer,
     tional architecture. In Proc. ICCV, pages 2650–2658, 2015.              2010. 1
     1, 2, 3, 6                                                         [24] A. Levin, D. Lischinski, and Y. Weiss. Colorization using
 [8] C. Farabet, C. Couprie, L. Najman, and Y. LeCun. Learning               optimization. In ACM transactions on graphics (tog), vol-
     hierarchical features for scene labeling. IEEE transactions             ume 23, pages 689–694. ACM, 2004. 6
     on pattern analysis and machine intelligence, 35(8):1915–          [25] Z. Li, Y. Gan, X. Liang, Y. Yu, H. Cheng, and L. Lin. Lstm-
     1929, 2013. 3                                                           cf: Unifying context modeling and fusion with lstms for rgb-
 [9] R. Girshick, J. Donahue, T. Darrell, and J. Malik. Rich fea-            d scene labeling. In Proc. ECCV, pages 541–557. Springer,
     ture hierarchies for accurate object detection and semantic             2016. 1, 2, 3, 7
     segmentation. In Proc. CVPR, pages 580–587, 2014. 3                [26] G. Lin, A. Milan, C. Shen, and I. Reid. RefineNet: Multi-
[10] S. Gupta, P. Arbelaez, and J. Malik. Perceptual organization            path refinement networks for high-resolution semantic seg-
     and recognition of indoor scenes from rgb-d images. In Proc.            mentation. In CVPR, July 2017. 2, 4, 6, 7, 8
     CVPR, pages 564–571, 2013. 1, 2, 3, 5, 6                           [27] G. Lin, C. Shen, A. v. d. Hengel, and I. Reid. Exploring con-
[11] S. Gupta, R. Girshick, P. Arbeláez, and J. Malik. Learning             text with deep structured models for semantic segmentation.
     rich features from rgb-d images for object detection and seg-           arXiv preprint arXiv:1603.03183, 2016. 3, 6
     mentation. In Proc. ECCV, pages 345–360. Springer, 2014.           [28] G. Lin, C. Shen, A. van den Hengel, and I. Reid. Efficient
     1, 2, 3, 5, 6                                                           piecewise training of deep structured models for semantic
[12] B. Hariharan, P. Arbeláez, R. Girshick, and J. Malik. Hyper-           segmentation. In Proc. CVPR, pages 3194–3203, 2016. 1, 2,
     columns for object segmentation and fine-grained localiza-              7
     tion. In Proc. CVPR, pages 447–456, 2015. 2                        [29] Z. Liu, X. Li, P. Luo, C.-C. Loy, and X. Tang. Semantic im-
[13] C. Hazirbas, L. Ma, C. Domokos, and D. Cremers. Fusenet:                age segmentation via deep parsing network. In Proc. ICCV,
     Incorporating depth into semantic segmentation via fusion-              pages 1377–1385, 2015. 1, 2
     based cnn architecture. In Proc. ACCV, volume 2, 2016. 1,          [30] J. Long, E. Shelhamer, and T. Darrell. Fully convolutional
     2, 3, 7                                                                 networks for semantic segmentation. In Proc. CVPR, pages
[14] K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learn-               3431–3440, 2015. 1, 2, 3, 6
     ing for image recognition. arXiv preprint arXiv:1512.03385,        [31] H. Noh, S. Hong, and B. Han. Learning deconvolution
     2015. 1, 2, 4, 5                                                        network for semantic segmentation. In Proc. ICCV, pages
[15] K. He, X. Zhang, S. Ren, and J. Sun. Identity mappings                  1520–1528, 2015. 2
     in deep residual networks. In Proc. ECCV, pages 630–645.           [32] X. Ren, L. Bo, and D. Fox. Rgb-(d) scene labeling: Features
     Springer, 2016. 2, 4                                                    and algorithms. In Proc. CVPR, pages 2759–2766. IEEE,
[16] A. Janoch, S. Karayev, Y. Jia, J. T. Barron, M. Fritz,                  2012. 1, 2, 3, 7
     K. Saenko, and T. Darrell. A category-level 3d object dataset:     [33] O. Ronneberger, P. Fischer, and T. Brox. U-net: Convolu-
     Putting the kinect to work. In Consumer Depth Cameras for               tional networks for biomedical image segmentation. In In-
     Computer Vision, pages 141–165. Springer, 2013. 8                       ternational Conference on Medical Image Computing and
[17] S. Jégou, M. Drozdzal, D. Vazquez, A. Romero, and Y. Ben-              Computer-Assisted Intervention, pages 234–241. Springer,
     gio. The one hundred layers tiramisu: Fully convolu-                    2015. 2
     tional densenets for semantic segmentation. arXiv preprint         [34] C. Russell, P. Kohli, P. H. Torr, et al. Associative hierarchical
     arXiv:1611.09326, 2016. 2                                               crfs for object class image segmentation. In Proc. ICCV,
[18] Y. Jia, E. Shelhamer, J. Donahue, S. Karayev, J. Long, R. Gir-          pages 739–746. IEEE, 2009. 1
     shick, S. Guadarrama, and T. Darrell. Caffe: Convolu-              [35] N. Silberman, D. Hoiem, P. Kohli, and R. Fergus. Indoor
     tional architecture for fast feature embedding. arXiv preprint          segmentation and support inference from rgbd images. In
     arXiv:1408.5093, 2014. 6                                                Proc. ECCV, pages 746–760. Springer, 2012. 1, 2, 3, 6, 8

                                                                      4988
[36] K. Simonyan and A. Zisserman. Very deep convolutional
     networks for large-scale image recognition. arXiv preprint
     arXiv:1409.1556, 2014. 1, 2
[37] S. Song, S. P. Lichtenberg, and J. Xiao. Sun rgb-d: A rgb-d
     scene understanding benchmark suite. In Proc. CVPR, pages
     567–576, 2015. 6, 7
[38] F. Visin, K. Kastner, K. Cho, M. Matteucci, A. Courville,
     and Y. Bengio.       Renet: A recurrent neural network
     based alternative to convolutional networks. arXiv preprint
     arXiv:1505.00393, 2015. 3
[39] J. Wang, Z. Wang, D. Tao, S. See, and G. Wang. Learning
     common and specific features for rgb-d semantic segmenta-
     tion with deconvolutional networks. In Proc. ECCV, pages
     664–679. Springer, 2016. 1, 2, 3, 6
[40] J. Xiao, A. Owens, and A. Torralba. Sun3d: A database
     of big spaces reconstructed using sfm and object labels. In
     Proc. ICCV, pages 1625–1632, 2013. 8
[41] J. Yao, S. Fidler, and R. Urtasun. Describing the scene as
     a whole: Joint object detection, scene classification and se-
     mantic segmentation. In Proc. CVPR, pages 702–709. IEEE,
     2012. 1
[42] F. Yu and V. Koltun. Multi-scale context aggregation by di-
     lated convolutions. In ICLR, 2016. 1, 2
[43] M. D. Zeiler and R. Fergus. Visualizing and understand-
     ing convolutional networks. In Proc. ECCV, pages 818–833.
     Springer, 2014. 1, 2
[44] Z. Zhang. Microsoft kinect sensor and its effect. IEEE mul-
     timedia, 19(2):4–10, 2012. 1
[45] S. Zheng, S. Jayasumana, B. Romera-Paredes, V. Vineet,
     Z. Su, D. Du, C. Huang, and P. H. Torr. Conditional random
     fields as recurrent neural networks. In Proc. ICCV, pages
     1529–1537, 2015. 1, 2

                                                                     4989
