---
source_id: 044
bibtex_key: liu2021tritransnet
title: TriTransNet: RGB-D Salient Object Detection with a Triplet Transformer Embedding Network
year: 2021
domain_theme: RGB-D SOD
verified_pdf: 44_TriTransNet.pdf
char_count: 75884
---

TriTransNet: RGB-D Salient Object Detection with a Triplet
                                                           Transformer Embedding Network
                                                              Zhengyi Liu∗                                                    Yuan Wang                                    Zhengzheng Tu
                                                School of Computer Science and                                  School of Computer Science and                    School of Computer Science and
                                                 Technology, Anhui University                                    Technology, Anhui University                      Technology, Anhui University
                                                          Hefei, China                                                    Hefei, China                                      Hefei, China
                                                    liuzywen@ahu.edu.cn                                            wangyuan.ahu@qq.com                                  15352718@qq.com

                                                                                                 Yun Xiao                                             Bin Tang
arXiv:2108.03990v1 [cs.CV] 9 Aug 2021

                                                                                School of Computer Science and                          School of Artificial Intelligence and
                                                                                 Technology, Anhui University                               Big Data, Hefei University
                                                                                          Hefei, China                                             Hefei, China
                                                                                     280240406@qq.com                                          424539820@qq.com

                                        ABSTRACT                                                                                        ACM Reference Format:
                                        Salient object detection is the pixel-level dense prediction task                               Zhengyi Liu, Yuan Wang, Zhengzheng Tu, Yun Xiao, and Bin Tang. 2021.
                                                                                                                                        TriTransNet: RGB-D Salient Object Detection with a Triplet Transformer
                                        which can highlight the prominent object in the scene. Recently
                                                                                                                                        Embedding Network. In Proceedings of the 29th ACM International Conference
                                        U-Net framework is widely used, and continuous convolution and                                  on Multimedia (MM ’21), October 20–24, 2021, Virtual Event, China. ACM,
                                        pooling operations generate multi-level features which are com-                                 New York, NY, USA, 10 pages. https://doi.org/10.1145/3474085.3475601
                                        plementary with each other. In view of the more contribution of
                                        high-level features for the performance, we propose a triplet trans-
                                        former embedding module to enhance them by learning long-range
                                                                                                                                        1    INTRODUCTION
                                        dependencies across layers. It is the first to use three transformer                            Salient object detection (SOD) simulates the visual attention mech-
                                        encoders with shared weights to enhance multi-level features. By                                anism to capture the prominent object in the scene. It has been
                                        further designing scale adjustment module to process the input,                                 widely applied in the computer vision tasks, such as image segmen-
                                        devising three-stream decoder to process the output and attaching                               tation [18], tracking [30, 47, 83], retrieval [25], compression [32],
                                        depth features to color features for the multi-modal fusion, the                                edit [65] and quality assessment [34].
                                        proposed triplet transformer embedding network (TriTransNet)                                       As a pixel-level dense prediction task, salient object detection
                                        achieves the state-of-the-art performance in RGB-D salient object                               usually uses CNN based U-Net framework[58] (Fig. 1(a)) to encode
                                        detection, and pushes the performance to a new level. Experimental                              images from low-level to high-level, and then decode back to the
                                        results demonstrate the effectiveness of the proposed modules and                               full spatial resolution. Research[74] points out that the performance
                                        the competition of TriTransNet.1                                                                tends to saturate quickly when gradually aggregating features from
                                                                                                                                        high-level to low-level. In other words, high-level features con-
                                        CCS CONCEPTS                                                                                    tribute more to the performance. Therefore, we propose a triplet
                                                                                                                                        transformer embedding module (TTEM) to enhance the feature
                                        • Computing methodologies → Interest point and salient re-                                      representation of high three layers.
                                        gion detections.                                                                                   As we all known, Transformer[62] has recently attracted a lot
                                                                                                                                        of attention in computer vision domain, but it is also encounter-
                                        KEYWORDS                                                                                        ing high computational cost problem. PVT[66] adopts a spatial-
                                        salient object detection; RGB-D image; transformer; shared weights;                             reduction attention (SRA) layer to reduce the resource cost to learn
                                        self-attention                                                                                  high-resolution feature maps. CvT[72] introduces convolutional
                                                                                                                                        into the Vision Transformer architecture to concurrently main-
                                        ∗ Corresponding author.                                                                         tain a high degree of computational and memory efficiency. Swin
                                        1 The code is available at https://github.com/liuzywen/TriTransNet.                             Transformer[44] uses the shifted windows calculation method to
                                                                                                                                        propose a hierarchical Transformer, which has the flexibility of
                                                                                                                                        modelling at various scales and has linear computational complex-
                                        Permission to make digital or hard copies of all or part of this work for personal or
                                        classroom use is granted without fee provided that copies are not made or distributed           ity relative to the image size. Multi-Scale Vision Longformer[82]
                                        for profit or commercial advantage and that copies bear this notice and the full citation       proposes multi-scale coding structure, and further improves its
                                        on the first page. Copyrights for components of this work owned by others than the              attention mechanism to reduce the computational and memory
                                        author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
                                        republish, to post on servers or to redistribute to lists, requires prior specific permission   cost.
                                        and/or a fee. Request permissions from permissions@acm.org.                                        Unlike these profound designs, we introduce Transformer into
                                        MM ’21, October 20–24, 2021, Virtual Event, China                                               U-Net framework to enhance the features of high three layers,
                                        © 2021 Copyright held by the owner/author(s). Publication rights licensed to ACM.
                                        ACM ISBN 978-1-4503-8651-7/21/10. . . $15.00                                                    which can be easily integrated into existing U-Net framework for
                                        https://doi.org/10.1145/3474085.3475601                                                         significant improvement with less cost. The features of high three
layers show the different attributions but the same in nature, which      In addition, depth information is proved to supply the useful
are the different aspects of the same input image. The proposed        cues and boost the performance for saliency detection [51], es-
triplet transformer embedding module (TTEM) is composed of             pecially in some challenging and complex scenarios, e.g. the low
three standard transformer encoders[62] with shared weights. It        color contrasts between salient objects and background, the clut-
is beneficial to find the common information which is hidden in        tered background interferences. But depth image with poor quality,
the multi-level features and achieve the better fusion by learning     which likes a noise, brings some negative influences [22]. Following
long-range dependencies across levels.                                 depth guided manners [11, 12, 23, 52, 57, 60, 79, 89, 93] we design
                                                                       depth purification module, which uses depth information to purify
                                                                       the color features.
                                                                          Our main contributions can be summarized as follows:

                                                                           • A triplet transformer embedding module is proposed and
                                                                             embedded into CNN based U-Net framework to enhance the
                       (a) U-Net framework                                   feature representation. It is composed of three standard trans-
                                                                             former encoders with shared weights, learning the common
                                                                             information from multi-level features.
                                                                           • Based on the proposed triplet transformer embedding mod-
                                                                             ule, triplet transformer embedding network is designed to
                                                                             detect the salient objects in RGB-D image. Multi-level fea-
                                                                             tures from encoder need to be adjusted to the same size by a
                                                                             transition layer and progressively upsampling fusion mod-
                                                                             ule, and then fed into triplet transformer embedding module.
                                                                             Then the output of triplet transformer embedding module
              (b) visual-transformer-FPN (VT-FPN)                            need to be combined with the features of low two layers by
                                                                             three-stream decoder to achieve the decoding process.
                                                                           • Depth image is viewed as the supplement to color feature,
                                                                             and attached to color feature to enhance the feature repre-
                                                                             sentation by depth purification module which introduces
                                                                             spatial attention and channel attention.
                                                                           • Due to the advantage of the proposed triplet transformer
                                                                             embedding module, the proposed model pushes the perfor-
                                                                             mance of RGB-D salient object detection to a new level and
                                                                             shows the state-of-the-art performance on several public
                                                                             datasets.
    (c) Our proposed triplet transformer embedding network

Figure 1: Comparison between U-Net framework, VT-FPN                   2 RELATED WORK
and our proposed network.
                                                                       2.1 RGB-D saliency detection
                                                                       In RGB-D image, color image provides appearance and texture infor-
   Taking TTME as the core, we further propose the triplet trans-      mation, and depth image contains 3D layout and spatial structure.
former embedding network (TriTransNet). At first, multi-level fea-     The fusion of color feature and depth feature is always an important
tures are adjusted to the same size by a transition layer and pro-     issue in RGB-D saliency detection. References[10, 45, 85, 90] use
gressively upsampling fusion module. Second, features are fed into     early fusion or input fusion, references[7, 11, 38, 39, 41] employ
TTME to be enhanced. Last, the output features of TTME and the         two-stream subnetwork to achieve the middle fusion, references[53,
features of low two layers are effectively fused by a three-stream     57, 73, 89, 93] apply depth guided fusion and references [14, 46, 64]
decoder.                                                               adopt late fusion.
   Our proposed TriTransNet is the first attempt to use three stan-        Although depth information can supply the useful cues for
dard transformer encoders with shared weights to enhance the           saliency detection [51], depth image with poor quality can bring
feature representation. Different from visual-transformer-FPN (VT-     some negative influences too [22]. In order to solve the filtering
FPN)[71] in Fig. 1(b) which merges visual tokens from feature map      issue of low-quality depth map, D3Net [22] uses gate mechanism to
of each layer with one transformer, our TriTransNet in Fig. 1(c)       filter the poor depth map, EF-Net [9] enhances the depth maps by
adopts weight sharing strategy to make visual tokens extracted         color hint map, DQSD [5] integrates a depth quality aware subnet-
from multi-level features more abundant enough to express the          work into the classic bi-stream structure, assigning the weight of
original information, and meanwhile high-layer semantic informa-       depth feature before conducting the fusion. In addition, CoNet[33],
tion and middle-layer texture or shape information are both better     DASNet [88], SSDP[68] and MobileSal [73] introduce depth estima-
excavated by parallel self-attention mechanism.                        tion, learning to detect the salient object simultaneously.
   In the paper, we adopt depth guided manner. Depth information       some coarse textures, and uses CNN to enhances local texture de-
is viewed as the supplement to the color feature. It enhances the      tails of coarse priors, so as to achieve excellent results on the image
color feature by attention mechanism.                                  completion task. TransT[13] uses Siamese-based CNN network for
                                                                       feature extraction, and designs the self-attention-based ego-context
                                                                       augment (ECA) and cross-attention-based cross-feature augment
2.2    Transformer                                                     (CFA) modules for feature fusion. Compact Transformers[28] elim-
Transformer is first proposed by[62] to replace recurrent neural       inates the requirement for class token and position embedding
networks (RNN), e.g.long short-term memory (LSTM) and gated            through a novel sequence pooling strategy and the use of convolu-
recurrent unit(GRU) for machine translation tasks. It can over-        tions, so as to perform head-to-head with state-of-the-art CNNs on
come intrinsic shortages of RNN and has dominated nature lan-          small datasets.
guage processing (NLP) field and are becoming increasingly pop-           Follow this strategy, we present triplet transformer embedding
ular in computer vision tasks, e.g. image classification[19], object   module which is embedded into a U-Net framework to improve
detection[4], semantic segmentation[? ], line segment[77], person      the performance of RGB-D saliency detection. Combining both
re-identification[94], action detection[87], image completion[91],     advantages, our model achieves the state-of-the-art performance.
3D point cloud processing[26, 86], pose estimation[59], facial ex-
pression recognition[48], object tracking[49] etc. DETR[4] takes       3 PROPOSED METHOD
the lead in applying Transformer to the field of object detection
and achieves the better performance. The successful use of ViT[19]
                                                                       3.1 Overview
in image classification tasks has made the research on visual Trans-   The overall framework of the proposed triplet transformer embed-
former a hot topics. SETR[92] deploys a pure Transformer as the        ding network is depicted in Fig.2(a), which consists of multi-modal
encoder, combined with a simple decoder, to achieve a powerful         fusion encoder, feature enhancement module and three-stream de-
semantic segmentation model. Besides, TransUNet[8] uses the pre-       coder. The details can be seen in the following sections.
trained ViT[19] as a powerful backbone of the U-Net[58] network
structure, and performs well in the field of medical image segmen-     3.2    Multi-modal fusion encoder
tation.                                                                Color and depth image in RGB-D image are two expressions for
   However, pure transformer has great limitations. As a result,       different modalities of the same scene. Color image provides ap-
many improved visual transformers have emerged. The Conditional        pearance cue and depth image shows three dimension spatial in-
Position encodings Visual Transformer (CPVT)[17] replaces the          formation. Due to existence of poor quality depth map induced by
fixed position encoding in ViT[19] with the proposed conditional       the imaging devices or conditions, we propose multi-modal fusion
position encoding (CPE), which makes it possible for Transformer to    encoder, in which depth features are first purified by multi-modal
process inputs of arbitrary sizes. Tokens-to-Token (T2T)[78] adopts    features using attention mechanism, and then served as supple-
a novel progressive tetanization mechanism, which models local         ment to the color feature by the residual connection[29]. Residual
structural information by aggregating adjacent tokens into one         part is designed as depth purification module (DPM), and shortcut
token, while reducing the length of the token. LocalViT[42] adds lo-   connection part is used to preserve more original color information.
cality to vision transformers by introducing depth-wise convolution       In DPM which is shown in Fig. 2(b), depth feature is concatenated
into the feed-forward network, improving a locality mechanism          with color feature, and fed into a channel attention module to get
for information exchange within a local region. Considering that       attentive channel mask, which is used to purify the depth feature in
most visual Transformers ignore the inherent structural informa-       a channel manner. Next, purified depth feature is fed into a spatial
tion inside the sequence of patches, Transformer-iN-Transformer        attention module again to generate attentive spatial mask, which is
(TNT)[27] proposes to use outer Transformer block and inner Trans-     used to purify the depth feature in a spatial manner. The process
former block to model patch-level and pixel-level representations,     can be described as:
respectively. Co-Scale Conv-Attentional Image Transformers[76]
designs a conv-attention module to realize relative position embed-                𝐹𝑖𝑟 = 𝑓𝑖𝑑 × 𝑆𝐴(𝑓𝑖𝑑 × 𝐶𝐴(𝐶𝑎𝑡 (𝑓𝑖𝑑 , 𝑓𝑖𝑟 ))) + 𝑓𝑖𝑟       (1)
ding and enhance computation efficiency, and further proposes a
co-scale mechanism to introduce cross-scale attention to enrich        where 𝑓𝑖𝑟 and 𝑓𝑖𝑑 represent color and depth features extracted by
multi-scale feature.                                                   backbone network respectively in which 𝑖 = 1, · · · , 5, 𝐶𝑎𝑡 (·) de-
   On the other hand, CNN has the advantages of extracting low         notes concatenation and following convolution operation, 𝐶𝐴(·)
level features and strengthening locality, while Transformer has       and 𝑆𝐴(·) are channel and spatial attention operation which is pro-
the advantages in establishing long-range dependencies. Some re-       posed by CBAM[70], “×" is element-wise multiplication operation,
search makes full use of both advantages. TransFuse[84] uses a         “+" is element-wise addition operation.
dual-branch structure, which uses Transformer to capture global           Thus, the depth feature with poor quality can be purified, and
dependencies, while low-level spatial details are extracted by CNN     then attached to color feature to generate more accuracy feature
branches. Similarly, CoTr[75] uses the CNN backbone to extract fea-    representation 𝐹𝑖𝑟 (𝑖 = 1, · · · , 5).
ture representations and proposes to use deformable Transformer
(DeTrans) to model long-range dependencies, effectively bridging       3.3    Feature enhancement module
the convolutional neural network and Transformer. ICT[63] uses         In this module, we first adjust the features of high three layers
transformer to recover pluralistic coherent structures together with   to the same size, and then use the triplet transformer embedding
              Figure 2: Our proposed triplet transformer embedding network for RGB-D salient object detection.

module to enhance the feature representation by learning long-             Then, we design a progressively upsampling fusion module
range dependency across levels, and last concatenate the input and      which is used to adjust the resolution of the features in the high
output of triplet transformer embedding module to preserve more         three layers to the same size. Since the direct upsampling with 2×
original information.                                                   or 4× ratio will bring some noises, the features are progressively
                                                                        upsampled and fused. The fusion process can be described as:
3.3.1 Scale adjustment module. The triplet transformer embedding
module is composed of three standard transformer encoders with                          𝐹 5 = 𝑈 𝐹 𝑀 (𝑈 𝐹 𝑀 (𝐹 5′𝑟 , 𝐹 4′𝑟 ), 𝐹 3′𝑟 )
shared weights. Its input should be the features with the same size.                    𝐹 4 = 𝑈 𝐹 𝑀 (𝐹 4′𝑟 , 𝐹 3′𝑟 )                       (3)
But the sizes of the multi-level features 𝐹𝑖𝑟 from multi-modal fusion                   𝐹 3 = 𝐹 3′𝑟
encoder are the different. Therefore, the first important task is to
adjust the sizes of multi-level features.                               where 𝑈 𝐹 𝑀 (·) is shown in Fig.2(d). The detail can be described as:
   At first, a transition layer which contains a 3×3 convolution
and a ReLU activation function is applied on 𝐹𝑖𝑟 . It can adjust the            𝑈 𝐹 𝑀 (𝐹ℎ𝑖𝑔ℎ , 𝐹𝑙𝑜𝑤 ) = 𝐶𝑎𝑡 (𝐶𝑜𝑛𝑣 (𝑈 𝑝 (𝐹ℎ𝑖𝑔ℎ )), 𝐹𝑙𝑜𝑤 )   (4)
number of channels of multi-level features to the same size. It can     where 𝐹ℎ𝑖𝑔ℎ and 𝐹𝑙𝑜𝑤 denote the feature from the higher layer
be described as:                                                        with low resolution and the feature from the lower layer with
                 𝐹𝑖′𝑟 = 𝜎 (𝐶𝑜𝑛𝑣 (𝐹𝑖𝑟 ))   𝑖 = 3, · · · , 5       (2)    high resolution, respectively, and 𝑈 𝑝 (·) denotes 2×upsampling
                                                                        operation.
where 𝐶𝑜𝑛𝑣 (·) is 3×3 convolution operation, and 𝜎 (·) is ReLU acti-       Compared with direct 2×, 4×upsampling on 𝐹 4′𝑟 and 𝐹 5′𝑟 , progres-
vation function.                                                        sively upsampling fusion module can not only adjust the features
to the same resolution but also increase the spatial detail of feature          use formula to show three-stream decoder as follow:
in the high layer by progressive fusion process.                                           𝐹𝑖′′ = 𝐶𝑎𝑡 (𝐶𝑎𝑡 (𝑈 𝑝 (𝐹𝑖′ ), 𝐹𝑟2 ), 𝐹𝑟1 )    𝑖 = 3, · · · 5    (8)
   Thus, the features 𝐹𝑖 (𝑖 = 3, · · · , 5) with the same scales will be
served as the input and fed into next triplet transformer embedding                 The above three features are performed upsampling, convolution
module.                                                                         operation and sigmoid function to generate the saliency maps 𝑆𝑖 (𝑖 =
                                                                                1, · · · , 3) which are supervised by the ground truth maps.
3.3.2 Triplet Transformer Embedding Module (TTEM). The fea-
                                                                                              𝑆𝑖 = 𝑠𝑖𝑔(𝐶𝑜𝑛𝑣 (𝑈 𝑝 (𝐶𝑜𝑛𝑣 (𝑈 𝑝 (𝐹𝑖′′ )))))                   (9)
tures are first converted into the sequences of feature embedding,
and then fed to three standard transformer encoders with shared                 where 𝑠𝑖𝑔(·) denotes sigmoid function.
weights to model the long-range relationship among different levels,               At last, we also fuse all the features above to generate the final
and last reshaped to the original size of features.                             saliency map.
   Specifically, each input feature 𝐹𝑖 (𝑖 = 3, · · · , 5) are first flattened                                 5
                                                                                                             ∑︁
into a 1D sequence {𝐹𝑖 |𝑝 = 1, · · · , 𝑁 }, where 𝑁 is the number of
                          𝑝
                                                                                           𝑆 𝑓 𝑖𝑛𝑎𝑙 = 𝑠𝑖𝑔(         𝐶𝑜𝑛𝑣 (𝑈 𝑝 (𝐶𝑜𝑛𝑣 (𝑈 𝑝 (𝐹𝑖′′ )))))      (10)
patches. Each patch 𝐹𝑖 is then mapped into a latent 𝐷-dimensional
                        𝑝                                                                                    𝑖=3
embedding space by a trainable linear projection layer. Furthermore,               Pixel position aware loss 𝐿𝑝𝑝𝑎
                                                                                                               𝑠   [69] is adopted for end-to-end
we learn specific position embedding which are added to the patch               training. The whole loss is defined as:
embedding to retain positional information. The process can be                                                                5
                                                                                                                             ∑︁
described as:                                                                                       𝑠
                                                                                               𝐿 = 𝐿𝑝𝑝𝑎 (𝑆 𝑓 𝑖𝑛𝑎𝑙 , 𝐺) +            𝑠
                                                                                                                                   𝐿𝑝𝑝𝑎 (𝑆𝑖 , 𝐺)         (11)
                                                                                                                             𝑖=3
            𝑍𝑖0 = [𝐹𝑖1 + 𝑃𝐸 1 ; 𝐹𝑖2 + 𝑃𝐸 2 ; · · · , ; 𝐹𝑖𝑁 + 𝑃𝐸 𝑁 ]      (5)
                                                                                where 𝐺 is ground truth saliency map.
where 𝑃𝐸 = {𝑃𝐸 𝑝 |𝑝 = 1, · · · , 𝑁 } is a 1D learnable positional em-
bedding.                                                                        4 EXPERIMENTS
   The remaining architecture essentially follows the standard
                                                                                4.1 Datasets and evaluation metrics
transformer encoder[62] which stacks 𝐿 transformer layer. It is
shown in Fig.2(c). Each transformer layer contains multi-headed                 4.1.1 Datasets. We evaluate the proposed method on six challeng-
self-attention (MSA) and multi-layer perceptron (MLP) sublayer.                 ing RGB-D SOD datasets. NLPR [54] includes 1000 images with
Layer normalization (LN)[2] are inserted before these two sublayers,            single or multiple salient objects. NJU2K [36] consists of 2003 stereo
and the residual connection is performed after these two sublayers.             image pairs and ground-truth maps with different objects, com-
The process can be described as:                                                plex and challenging scenes. STERE [50] incorporates 1000 pairs
                                                                                of binocular images downloaded from the Internet. DES [15] has
              ′
                                 
          𝑍𝑖𝑙 = 𝑀𝑆𝐴 𝐿𝑁 𝑍𝑖𝑙−1 + 𝑍𝑖𝑙−1                                           135 indoor images collected by Microsoft Kinect. SIP [22] contains
         
         
                                                                 (6)
         
                           ′         ′       𝑙 = 1, · · · 𝐿                 1000 high-resolution images of multiple salient persons. DUT [56]
          𝑍𝑖𝑙 = 𝑀𝐿𝑃 𝐿𝑁 𝑍𝑖𝑙
                                  + 𝑍𝑖𝑙
                                                                               contains 1200 images captured by Lytro camera in real life scenes.
where 𝐿 denotes the number of transformer layers in the standard                   For the sake of fair comparison, we use the same training dataset
transformer encoder.                                                            as in [11, 22], which consists of 1,485 images from the NJU2K dataset
                                                                                and 700 images from the NLPR dataset. The remaining images in the
3.3.3 Feature concatenation module. The outputs of three weights                NJU2K and NLPR datasets and the whole datasets of STERE, DES
shared transformer encoders 𝑍𝑖𝐿 (𝑖 = 3, · · · , 5) fuses the informa-           and SIP are used for testing. In addition, on the DUT dataset, we
tion of three layers by Transformer mechanism, so as to enhance                 follow the same protocols as in [33, 39, 56, 57, 90] to add additional
the original feature representation. In order to preserve the more              800 pairs from DUT for training and test on the remaining 400 pairs.
original information, we further cascade these outputs with original            In summary, our training set contains 2,185 paired RGB and depth
features to generate the enhanced features of high three layers. The            images, but when testing is conducted on DUT, our training set
process can be described as:                                                    contains 2,985 paired ones.
                   𝐹𝑖′ = 𝐶𝑎𝑡 (𝑍𝑖𝐿 , 𝐹𝑖 )      𝑖 = 3, · · · 5             (7)    4.1.2 Evaluation Metrics. We adopt five widely used metrics to
                                                                                evaluate the performance of our model and other state-of-the-art
3.4    Three-stream decoder                                                     RGB-D SOD models, including the precision-recal(PR) curve [3],
After the features of high three layers are enhanced by the proposed            E-measure [21], S-measure [20], F-measure [1] and mean absolute
triplet transformer embedding module, we will combine them with                 error (MAE) [55]. Specifically, the PR curve plots precision and
the features of low two layers to achieve the decoding process. There           recall values by setting a series of thresholds on the saliency maps to
are two decoding methods. One is single-stream decoding and the                 get the binary masks and further comparing them with the ground
other is three-stream decoding. The single-stream decoding first                truth maps. The E-measure simultaneously captures global statistics
fuses three output results of feature enhancement module, and then              and local pixel matching information. The S-measure can evaluate
combine it with two features in the low layers. The three-stream                both region-aware and object-aware structural similarity between
decoding first combines each output result of feature enhancement               saliency map and ground truth. The F-measure is the weighted
module with two features in the low layers, and then fuses three-               harmonic mean of precision and recall, which can evaluate the
stream results. We conduct two decoding processes, and find three-              overall performance. The MAE measures the average of the per-
stream decoding is better than single-stream decoding. Next, we                 pixel absolute difference between the saliency maps and the ground
truth maps. In our experiment, E-measure and F-measure adopts          TTEM with gated recurrent unit (GRU) [16], whose result is shown
adaptive values.                                                       in the variant No.2 of Table. 2. The variant No.3 of Table. 2 is the
                                                                       result of siamese transformer applied in the high two layers. The
4.2 Implementation details                                             variant No.4 of Table. 2 is the result of quadruplet transformer ap-
During the training and testing phase, the input RGB and depth         plied in the high four layers. The variant No.5 of Table. 2 is our
images are resized to 256×256. Multiple enhancement strategies         result of triplet transformer applied in the high three layers.
are used for all training images, i.e. random flipping, rotating and       It can be clearly observed that compared with No.1, the result of
border clipping. Parameters of the backbone network are initialized    our   TriTransNet is improved 0.016 in the S-measure metric, 0.021
with the pretrained parameters of ResNet-50 network [29]. The          in the   F-measure metric, 0.008 in the E-measure metric and 0.007
hyper-parameters in transformer encoder are set as: 𝐿 = 12,𝐷 =         in the MAE metric on average. Meanwhile, compared with No.2, the
768,𝑁 = 1024. The rest of parameters are initialized to PyTorch        result of our TriTransNet is improved 0.012 in the S-measure metric,
default settings. We employ the Adam optimizer [37] to train our       0.014 in the F-measure metric, 0.006 in the E-measure metric and
network with a batch size of 3 and an initial learning rate 1e-5, and  0.005 in the MAE metric on average. TTEM plays an important
the learning rate will be divided by 10 every 60 epochs. Our model     role in the performance improvement.
is trained on a machine with a single NVIDIA GTX 3090 GPU. The             In addition, we compare No.3, No.4 and No.5 and find that Triplet
model converges within 150 epochs, which takes nearly 15 hours.        win   Siamese in S-measure, F-measure, E-measure, and MAE about
                                                                       0.009,0.016,0.006 and 0.005 on average, and outperform Quadruplet
4.3 Comparisons with the state-of-the-art                              about 0.010,0.009,0.005 and 0.004 on average. Our TriTransNet en-
                                                                       hances long-range dependency of semantic information by using
Our model is compared with 16 state-of-the-art RGB-D SOD models,       the features in the high three layers, and further combines with
including D3Net [22], ICNet [41], DCMF [6], DRLF [67], SSF [81],       three-stream usampling decoding in the low two layers to perfectly
SSMA [43], A2dele [57], UCNet [80], CoNet [33], DANet [90], JLDCF[24], depict the detailed boundary, so as to achieve the best performance.
EBFSP[31],CDNet[35], HAINet[40], RD3D[10] and DSA2F[61]. To
ensure the fairness of the comparison results, the saliency maps of
the evaluation are provided by the authors or generated by running     4.4.2 The effectiveness of three-stream decoder. we further conduct
source codes.                                                          the ablation study by replacing three stream decoder with single-
                                                                       stream decoder to check the effectiveness of the designed three-
4.3.1 Quantitative Evaluation. Figure.3 shows the comparison re-
                                                                       stream decoder. Table. 3 No.1 denotes the model which adopts
sults on PR curve. Table.1 shows the quantitative comparison results
                                                                       single-stream decoder and No.2 means our three-stream decoder.
of four evaluation metrics. As can be clearly observed from figure
                                                                       From Table. 3, we can see that the use of three-stream decoder
that our curves are very short, which means that our recall is very
                                                                       obviously improves the detection performance. It benefits from the
high. Furthermore, from the table, we can see that all the evalua-
                                                                       full integration of multi-layer features.
tion metrics are nearly the best on six datasets, so as to verify the
effectiveness and advantages of our proposed method. Only two          4.4.3 The effectiveness of depth purification module (DPM). The
S-measure values in NLPR and STERE datasets are inferior to the        baseline model used here removes depth purification module (DPM).
best, but they are also the second best. Combined with the results of  It attaches the depth feature to color feature by element-wise ad-
figure and table, our method achieves the impressive performance.      dition operation in the encoder. Its performance is illustrated in
4.3.2 Qualitative Evaluation. To make the qualitative comparisons,       the variant No.1 of Table. 4. Further, we discuss the similar depth-
we show some visual examples in Figure.4. It can be observed that        enhanced module (DEM) proposed in BBS[23] whose result is
our method has better detection results than other methods in            shown in the variant No.2 of Table. 4. The variant No.3 of Table. 4
some challenging cases: similar foreground and background(1𝑠𝑡 -          denotes the model which adopts DPM instead of element-wise
2𝑛𝑑 rows), complex scene(3𝑟𝑑 -4𝑡ℎ rows), low quality depth map(5𝑡ℎ -     addition operation based on the baseline.
                                                                            Compared with No.1, the performance of the variant No.3 is
6𝑡ℎ rows), small object(7𝑡ℎ -8𝑡ℎ rows) and multiple objects(9𝑡ℎ -10𝑡ℎ
                                                                         significantly improved. Meanwhile, compared with No.2 which
rows). These indicate that our approach can better locate salient
                                                                         using DEM, our detection effect is also better than that of No.2. It
objects and produce more accurate saliency maps. In addition, our
                                                                         verified that the effectiveness of DPM.
approach can produce more fine-grained details as highlighted in
the salient region(11𝑡ℎ -12𝑡ℎ rows). This is also the proof of the
effectiveness of our method.                                             5   CONCLUSIONS
                                                                         In the paper, we introduce transformer into U-Net framework to
4.4    Ablation studies                                                  detect salient object in RGB-D image. Different from existing com-
We conduct ablation studies on NLPR, NJU2K, SIP and STERE                bination method of transformer and convolutional neural networks,
datasets to investigate the contributions of different modules in the    we propose a triplet transformer embedding module which can be
proposed method.                                                         embedded into existing U-Net models for the better feature rep-
                                                                         resentation by learning long-range dependency among different
4.4.1 The effectiveness of triplet transformer embedding module          levels with less cost. Furthermore, we use depth information to
(TTEM). The baseline model used here removes TTEM. Its perfor-           enhance RGB features by depth purification module. Experimental
mance is shown in the variant No.1 of Table. 2. Further, we replace      results show our method pushes the performance to a new level,
                (a)NLPR dataset                                                    (b)NJU2K dataset                                                (c)STERE dataset

                (d)DES dataset                                                     (e)SIP dataset                                            (f)DUT dataset

                                    Figure 3: P-R curves comparisons of different models on six datasets.

Table 1: S-measure, adaptive F-measure, adaptive E-measure, MAE comparisons with different models. The best result is in
bold.

                 DatasetsMetric D3Net ICNetDCMF DRLF SSF SSMA A2dele UCNet CoNet DANet JLDCF EBFSP CDNetHAINet RD3D DSA2F TriTransNet
                               TNNLS20 TIP20 TIP20 TIP20CVPR20CVPR20CVPR20CVPR20ECCV20ECCV20CVPR20TMM21 TIP21 TIP21 AAAI21CVPR21 Ours
                           S↑     .912   .923   .900   .903   .914   .915   .896    .920   .908   .920   .925   .915   .902   .924   .930   .918      .928
                  NLPR    F𝛽 ↑    .861   .870   .839   .843   .875   .853   .878    .890   .846   .875   .878   .897   .848   .897   .892   .892      .909
                          𝐸𝜉 ↑    .944   .944   .933   .936   .949   .938   .945    .953   .934   .951   .953   .952   .935   .957   .958   .950      .960
                          MAE ↓   .030   .028   .035   .032   .026   .030   .028    .025   .031   .027   .022   .026   .032   .024   .022   .024      .020
                         S↑       .901   .894   .889   .886   .899   .894   .869    .897   .895   .899   .902   .903   .885   .912   .916   .904      .920
                  NJU2K F ↑       .865   .868   .859   .849   .886   .865   .874    .889   .872   .871   .885   .894   .866   .900   .901   .898      .919
                         𝛽
                          𝐸𝜉 ↑    .914   .905   .897   .901   .913   .896   .897    .903   .912   .908   .913   .907   .911   .922   .918   .922      .925
                          MAE ↓   .046   .052   .052   .055   .043   .053   .051    .043   .046   .045   .041   .039   .048   .038   .036   .039      .030
                            S↑    .899   .903   .883   .888   .887   .890   .878    .903   .905   .901   .903   .900   .896   .907   .911   .897      .908
                  STERE    F𝛽 ↑   .859   .865   .841   .845   .867   .855   .874    .885   .884   .868   .869   .870   .873   .885   .886   .893      .893
                          𝐸𝜉 ↑    .920   .915   .904   .915   .921   .907   .915    .922   .927    921   .919   .912   .922   .925   .927   .927      .927
                          MAE ↓   .046   .045   .054   .050   .046   .051   .044    .039   .037   .043   .040   .045   .042   .040   .037   .039      .033
                           S↑     .898   .920   .877   .895   .905   .941   .885    .933   .911   .924   .931   .937   .875   .935   .935   .916      .943
                   DES    F𝛽 ↑    .870   .889   .820   .868   .876   .906   .865    .917   .861   .899   .900   .913   .839   .924   .917   .901      .936
                          𝐸𝜉 ↑    .951   .959   .923   .954   .948   .974   .922    .974   .945   .968   .969   .974   .921   .974   .975   .955      .981
                          MAE ↓   .031   .027   .040   .030   .025   .021   .028    .018   .027   .023   .020   .018   .034   .018   .019   .023      .014
                            S↑    .860   .854   .859   .850   .868   .872   .826    .875   .858   .875   .880   .885   .823   .880   .885   .862      .886
                   SIP     F𝛽 ↑   .835   .836   .819   .813   .851   .854   .825    .868   .842   .855   .873   .869   .805   .875   .874   .865      .892
                          𝐸𝜉 ↑    .902   .899   .898   .891   .911   .911   .892    .913   .909   .914   .921   .917   .880   .919   .920   .908      .924
                          MAE ↓   .063   .069   .068   .071   .056   .057   .070    .051   .063   .054   .049   .049   .076   .053   .048   .057      .043
                            S↑    .775   .852   .798   .826   .916   .903   .886    .864   .919   .899   .906   .858   .880   .910   .931   .921      .933
                  DUT      F𝛽 ↑   .756   .830   .750   .803   .914   .866   .890    .856   .909   .888   .882   .842   .874   .906   .924   .926      .938
                          𝐸𝜉 ↑    .847   .897   .848   .870    946   .921   .924    .903   .948   .934   .931   .890   .918   .938   .949   .950      .957
                          MAE ↓   .097   .072   .104   .080   .034   .044   .043    .056   .033   .043   .043   .067   .048   .038   .031   .030      .025

and ablation studies also verify the effectiveness of each module. In                        ACKNOWLEDGMENTS
the future, we will achieve the same task by a pure transformer, and                         This work is supported by National Natural Science Foundation of
further discuss their respective advantages to achieve the better                            China (62006002), Natural Science Foundation of Anhui Province
combination.                                                                                 (1908085MF182) and Key Program of Natural Science Project of
                                                                                             Educational Commission of Anhui Province(KJ2019A0034).
                     Figure 4: Visual comparison results with other the state-of-the-art models.

Table 2: Ablation experiment of triplet transformer embedding module (TTEM). The best result is in bold.

                                       Candidate                             NLPR                NJUD2K                     SIP                    STERE
         Variant
                   Baseline GRU Siamese Quadruplet Triplet S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓ S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓ S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓ S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓
          No.1        ✓                                            .910 .882 .952    .026 .904 .897 .917   .038 .876 .877 .918      .049 .888 .873 .916    .042
          No.2        ✓        ✓                                   .914 .891 .953    .024 .905 .901 .919   .037 .879 .882 .919      .047 .895 .883 .920    .038
          No.3        ✓                 ✓                          .917 .888 .956    .024 .910 .903 .915   .035 .882 .885 .926      .046 .896 .872 .917    .040
          No.4        ✓                            ✓               .922 .903 .958    .022 .911 .908 .922   .034 .875 .886 .913      .048 .895 .881 .922    .038
          No.5        ✓                                       ✓   .928 .909 .960 .020 .920 .919 .925 .030 .886 .892 .924 .043 .908 .893 .927 .033

              Table 3: Ablation experiment of three-stream decoder. The best result is in bold.

                                       Candidate                   NLPR                   NJUD2K                   SIP                   STERE
                   Variant
                             single-stream three-stream S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓ S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓ S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓ S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓
                    No.1           ✓                        .923 .892 .958     .022 .916 .904 .919   .035 .884 .886 .920    .045 .903 .879 .920     .037
                    No.2                           ✓       .928 .909 .960 .020 .920 .919 .925 .030 .886 .892 .924 .043 .908 .893 .927 .033

      Table 4: Ablation experiment of depth purification module (DPM). The best result is in bold.

                                   Candidate                   NLPR                    NJUD2K                    SIP                     STERE
                 Variant
                             Baseline DEM DPM S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓ S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓ S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓ S ↑ F𝛽 ↑ 𝐸𝜉 ↑ MAE ↓
                   No.1         ✓             .917 .897 .956 .023 .909 .904 .920 .035 .883 .887 .921 .044 .894 .875 .918 .039
                   No.2        ✓         ✓             .923 .901 .958   .021    .914 .910 .922   .033   .884 .889 .923     .044   .905 .889 .925    .035
                   No.3        ✓               ✓       .928 .909 .960 .020 .920 .919 .925 .030 .886 .892 .924 .043 .908 .893 .927 .033
REFERENCES                                                                                 [26] Meng-Hao Guo, Jun-Xiong Cai, Zheng-Ning Liu, Tai-Jiang Mu, Ralph R Mar-
 [1] Radhakrishna Achanta, Sheila Hemami, Francisco Estrada, and Sabine Susstrunk.              tin, and Shi-Min Hu. 2020. PCT: Point Cloud Transformer. arXiv preprint
     2009. Frequency-tuned salient region detection. In 2009 IEEE conference on                 arXiv:2012.09688 (2020).
     computer vision and pattern recognition. IEEE, 1597–1604.                             [27] Kai Han, An Xiao, Enhua Wu, Jianyuan Guo, Chunjing Xu, and Yunhe Wang.
 [2] Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. 2016. Layer normaliza-              2021. Transformer in transformer. arXiv preprint arXiv:2103.00112 (2021).
     tion. arXiv preprint arXiv:1607.06450 (2016).                                         [28] Ali Hassani, Steven Walton, Nikhil Shah, Abulikemu Abuduweili, Jiachen Li, and
 [3] Ali Borji, Ming-Ming Cheng, Huaizu Jiang, and Jia Li. 2015. Salient object                 Humphrey Shi. 2021. Escaping the Big Data Paradigm with Compact Transform-
     detection: A benchmark. IEEE transactions on image processing 24, 12 (2015),               ers. arXiv preprint arXiv:2104.05704 (2021).
     5706–5722.                                                                            [29] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep residual
 [4] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexan-                learning for image recognition. In Proceedings of the IEEE conference on computer
     der Kirillov, and Sergey Zagoruyko. 2020. End-to-end object detection with                 vision and pattern recognition. 770–778.
     transformers. In European Conference on Computer Vision. Springer, 213–229.           [30] Seunghoon Hong, Tackgeun You, Suha Kwak, and Bohyung Han. 2015. Online
 [5] Chenglizhao Chen, Jipeng Wei, Chong Peng, and Hong Qin. 2021. Depth-Quality-               tracking by learning discriminative saliency map with convolutional neural
     Aware Salient Object Detection. IEEE Transactions on Image Processing 30 (2021),           network. In International conference on machine learning. 597–606.
     2350–2363.                                                                            [31] Nianchang Huang, Yang Yang, Dingwen Zhang, Qiang Zhang, and Jungong Han.
 [6] Hao Chen, Yongjian Deng, Youfu Li, Tzu-Yi Hung, and Guosheng Lin. 2020. RGBD               2021. Employing Bilinear Fusion and Saliency Prior Information for RGB-D
     salient object detection via disentangled cross-modal fusion. IEEE Transactions            Salient Object Detection. IEEE Transactions on Multimedia (2021).
     on Image Processing 29 (2020), 8407–8416.                                             [32] Qing-Ge Ji, Zhi-Dang Fang, Zhen-Hua Xie, and Zhe-Ming Lu. 2013. Video
 [7] Hao Chen and Youfu Li. 2018. Progressively complementarity-aware fusion                    abstraction based on the visual attention model and online clustering. Signal
     network for RGB-D salient object detection. In Proceedings of the IEEE conference          Processing: Image Communication 28, 3 (2013), 241–253.
     on computer vision and pattern recognition. 3051–3060.                                [33] Wei Ji, Jingjing Li, Miao Zhang, Yongri Piao, and Huchuan Lu. 2020. Accurate rgb-
 [8] Jieneng Chen, Yongyi Lu, Qihang Yu, Xiangde Luo, Ehsan Adeli, Yan Wang, Le                 d salient object detection via collaborative learning. In Computer Vision–ECCV
     Lu, Alan L Yuille, and Yuyin Zhou. 2021. Transunet: Transformers make strong               2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings,
     encoders for medical image segmentation. arXiv preprint arXiv:2102.04306 (2021).           Part XVIII 16. Springer, 52–69.
 [9] Qian Chen, Keren Fu, Ze Liu, Geng Chen, Hongwei Du, Bensheng Qiu, and Ling            [34] Qiuping Jiang, Feng Shao, Weisi Lin, Ke Gu, Gangyi Jiang, and Huifang Sun.
     Shao. 2020. EF-Net: A novel enhancement and fusion network for RGB-D saliency              2017. Optimizing multistage discriminative dictionaries for blind image quality
     detection. Pattern Recognition (2020), 107740.                                             assessment. IEEE Transactions on Multimedia 20, 8 (2017), 2035–2048.
[10] Qian Chen, Ze Liu, Yi Zhang, Keren Fu, Qijun Zhao, and Hongwei Du. 2021.              [35] Wen-Da Jin, Jun Xu, Qi Han, Yi Zhang, and Ming-Ming Cheng. 2021. CDNet:
     RGB-D Salient Object Detection via 3D Convolutional Neural. AAAI (2021).                   Complementary Depth Network for RGB-D Salient Object Detection. IEEE
[11] Shuhan Chen and Yun Fu. 2020. Progressively guided alternate refinement                    Transactions on Image Processing 30 (2021), 3376–3390.
     network for RGB-D salient object detection. In European Conference on Computer        [36] Ran Ju, Ling Ge, Wenjing Geng, Tongwei Ren, and Gangshan Wu. 2014. Depth
     Vision. Springer, 520–538.                                                                 saliency based on anisotropic center-surround difference. In 2014 IEEE interna-
[12] Sihan Chen, Xinxin Zhu, Wei Liu, Xingjian He, and Jing Liu. 2021. Global-                  tional conference on image processing (ICIP). IEEE, 1115–1119.
     Local Propagation Network for RGB-D Semantic Segmentation. arXiv preprint             [37] Diederik P Kingma and Jimmy Ba. 2014. Adam: A method for stochastic opti-
     arXiv:2101.10801 (2021).                                                                   mization. arXiv preprint arXiv:1412.6980 (2014).
[13] Xin Chen, Bin Yan, Jiawen Zhu, Dong Wang, Xiaoyun Yang, and Huchuan Lu.               [38] Chongyi Li, Runmin Cong, Sam Kwong, Junhui Hou, Huazhu Fu, Guopu Zhu,
     2021. Transformer tracking. In Proceedings of the IEEE/CVF Conference on Com-              Dingwen Zhang, and Qingming Huang. 2020. ASIF-Net: Attention steered inter-
     puter Vision and Pattern Recognition. 8126–8135.                                           weave fusion network for RGB-D salient object detection. IEEE Transactions on
[14] Zuyao Chen, Runmin Cong, Qianqian Xu, and Qingming Huang. 2020. DPANet:                    Cybernetics (2020).
     Depth Potentiality-Aware Gated Attention Network for RGB-D Salient Object             [39] Chongyi Li, Runmin Cong, Yongri Piao, Qianqian Xu, and Chen Change Loy. 2020.
     Detection. IEEE Transactions on Image Processing (2020).                                   RGB-D salient object detection with cross-modality modulation and selection. In
[15] Yupeng Cheng, Huazhu Fu, Xingxing Wei, Jiangjian Xiao, and Xiaochun Cao.                   European Conference on Computer Vision. Springer, 225–241.
     2014. Depth enhanced saliency detection method. In Proceedings of international       [40] Gongyang Li, Zhi Liu, Minyu Chen, Zhen Bai, Weisi Lin, and Haibin Ling. 2021.
     conference on internet multimedia computing and service. 23–27.                            Hierarchical Alternate Interaction Network for RGB-D Salient Object Detection.
[16] Kyunghyun Cho, Bart Van Merriënboer, Caglar Gulcehre, Dzmitry Bahdanau,                    IEEE Transactions on Image Processing 30 (2021), 3528–3542.
     Fethi Bougares, Holger Schwenk, and Yoshua Bengio. 2014. Learning phrase              [41] Gongyang Li, Zhi Liu, and Haibin Ling. 2020. ICNet: Information Conversion
     representations using RNN encoder-decoder for statistical machine translation.             Network for RGB-D Based Salient Object Detection. IEEE Transactions on Image
     arXiv preprint arXiv:1406.1078 (2014).                                                     Processing 29 (2020), 4873–4884.
[17] Xiangxiang Chu, Bo Zhang, Zhi Tian, Xiaolin Wei, and Huaxia Xia. 2021. Do We          [42] Yawei Li, Kai Zhang, Jiezhang Cao, Radu Timofte, and Luc Van Gool. 2021. Lo-
     Really Need Explicit Position Encodings for Vision Transformers? arXiv preprint            calViT: Bringing Locality to Vision Transformers. arXiv preprint arXiv:2104.05707
     arXiv:2102.10882 (2021).                                                                   (2021).
[18] Michael Donoser, Martin Urschler, Martin Hirzer, and Horst Bischof. 2009.             [43] Nian Liu, Ni Zhang, and Junwei Han. 2020. Learning Selective Self-Mutual At-
     Saliency driven total variation segmentation. In 2009 IEEE 12th International              tention for RGB-D Saliency Detection. In Proceedings of the IEEE/CVF Conference
     Conference on Computer Vision. IEEE, 817–824.                                              on Computer Vision and Pattern Recognition. 13756–13765.
[19] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xi-          [44] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng Zhang, Stephen Lin,
     aohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg                 and Baining Guo. 2021. Swin transformer: Hierarchical vision transformer using
     Heigold, Sylvain Gelly, Jakob Uszkoreit, and Neil Houlsby. 2021. An Image is               shifted windows. arXiv preprint arXiv:2103.14030 (2021).
     Worth 16x16 Words: Transformers for Image Recognition at Scale. In International      [45] Zhengyi Liu, Song Shi, Quntao Duan, Wei Zhang, and Peng Zhao. 2019. Salient
     Conference on Learning Representations.                                                    object detection for RGB-D image by single stream recurrent convolution neural
[20] Deng-Ping Fan, Ming-Ming Cheng, Yun Liu, Tao Li, and Ali Borji. 2017. Structure-           network. Neurocomputing 363 (2019), 46–57.
     measure: A new way to evaluate foreground maps. In Proceedings of the IEEE            [46] Zhengyi Liu, Wei Zhang, and Peng Zhao. 2020. A cross-modal adaptive gated
     international conference on computer vision. 4548–4557.                                    fusion generative adversarial network for RGB-D salient object detection. Neuro-
[21] Deng-Ping Fan, Cheng Gong, Yang Cao, Bo Ren, Ming-Ming Cheng, and Ali Borji.               computing 387 (2020), 210–220.
     2018. Enhanced-alignment measure for binary foreground map evaluation. arXiv          [47] Cong Ma, Zhenjiang Miao, Xiao-Ping Zhang, and Min Li. 2017. A saliency prior
     preprint arXiv:1805.10421 (2018).                                                          context model for real-time object tracking. IEEE Transactions on Multimedia 19,
[22] Deng-Ping Fan, Zheng Lin, Zhao Zhang, Menglong Zhu, and Ming-Ming Cheng.                   11 (2017), 2415–2424.
     2020. Rethinking RGB-D Salient Object Detection: Models, Data Sets, and Large-        [48] Fuyan Ma, Bin Sun, and Shutao Li. 2021. Robust Facial Expression Recognition
     Scale Benchmarks. IEEE Transactions on Neural Networks and Learning Systems                with Convolutional Visual Transformers. arXiv preprint arXiv:2103.16854 (2021).
     (2020).                                                                               [49] Tim Meinhardt, Alexander Kirillov, Laura Leal-Taixe, and Christoph Feichten-
[23] Deng-Ping Fan, Yingjie Zhai, Ali Borji, Jufeng Yang, and Ling Shao. 2020. BBS-             hofer. 2021. TrackFormer: Multi-Object Tracking with Transformers. arXiv
     Net: RGB-D salient object detection with a bifurcated backbone strategy network.           preprint arXiv:2101.02702 (2021).
     In European Conference on Computer Vision. Springer, 275–292.                         [50] Yuzhen Niu, Yujie Geng, Xueqing Li, and Feng Liu. 2012. Leveraging stereopsis
[24] Keren Fu, Deng-Ping Fan, Ge-Peng Ji, and Qijun Zhao. 2020. JL-DCF: Joint                   for saliency analysis. In 2012 IEEE Conference on Computer Vision and Pattern
     learning and densely-cooperative fusion framework for rgb-d salient object                 Recognition. IEEE, 454–461.
     detection. In Proceedings of the IEEE/CVF conference on computer vision and pattern   [51] Nabil Ouerhani and Heinz Hugli. 2000. Computing visual attention from scene
     recognition. 3052–3062.                                                                    depth. In Proceedings 15th International Conference on Pattern Recognition. ICPR-
[25] Yuan Gao, Miaojing Shi, Dacheng Tao, and Chao Xu. 2015. Database saliency for              2000, Vol. 1. IEEE, 375–378.
     fast image retrieval. IEEE Transactions on Multimedia 17, 3 (2015), 359–369.
[52] Liang Pan, Xiaofei Zhou, Ran Shi, Jiyong Zhang, and Chenggang Yan. 2020.                     preprint arXiv:2103.15808 (2021).
     Cross-modal feature extraction and integration based RGBD saliency detection.           [73] Yu-Huan Wu, Yun Liu, Jun Xu, Jia-Wang Bian, Yuchao Gu, and Ming-Ming Cheng.
     Image and Vision Computing 101 (2020), 103964.                                               2020. MobileSal: Extremely Efficient RGB-D Salient Object Detection. arXiv
[53] Youwei Pang, Lihe Zhang, Xiaoqi Zhao, and Huchuan Lu. 2020. Hierarchi-                       preprint arXiv:2012.13095 (2020).
     cal dynamic filtering network for rgb-d salient object detection. In Computer           [74] Zhe Wu, Li Su, and Qingming Huang. 2019. Cascaded partial decoder for fast
     Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020,                 and accurate salient object detection. In Proceedings of the IEEE Conference on
     Proceedings, Part XXV 16. Springer, 235–252.                                                 Computer Vision and Pattern Recognition. 3907–3916.
[54] Houwen Peng, Bing Li, Weihua Xiong, Weiming Hu, and Rongrong Ji. 2014. Rgbd             [75] Yutong Xie, Jianpeng Zhang, Chunhua Shen, and Yong Xia. 2021. CoTr: Efficiently
     salient object detection: a benchmark and algorithms. In European conference on              Bridging CNN and Transformer for 3D Medical Image Segmentation. arXiv
     computer vision. Springer, 92–109.                                                           preprint arXiv:2103.03024 (2021).
[55] Federico Perazzi, Philipp Krähenbühl, Yael Pritch, and Alexander Hornung. 2012.         [76] Weijian Xu, Yifan Xu, Tyler Chang, and Zhuowen Tu. 2021. Co-Scale Conv-
     Saliency filters: Contrast based filtering for salient region detection. In 2012 IEEE        Attentional Image Transformers. arXiv preprint arXiv:2104.06399 (2021).
     conference on computer vision and pattern recognition. IEEE, 733–740.                   [77] Yifan Xu, Weijian Xu, David Cheung, and Zhuowen Tu. 2021. Line segment detec-
[56] Yongri Piao, Wei Ji, Jingjing Li, Miao Zhang, and Huchuan Lu. 2019. Depth-                   tion using transformers without edges. In Proceedings of the IEEE/CVF Conference
     induced multi-scale recurrent attention network for saliency detection. In Pro-              on Computer Vision and Pattern Recognition. 4257–4266.
     ceedings of the IEEE International Conference on Computer Vision. 7254–7263.            [78] Li Yuan, Yunpeng Chen, Tao Wang, Weihao Yu, Yujun Shi, Francis EH Tay, Jiashi
[57] Yongri Piao, Zhengkun Rong, Miao Zhang, Weisong Ren, and Huchuan Lu. 2020.                   Feng, and Shuicheng Yan. 2021. Tokens-to-token vit: Training vision transformers
     A2dele: Adaptive and Attentive Depth Distiller for Efficient RGB-D Salient Object            from scratch on imagenet. arXiv preprint arXiv:2101.11986 (2021).
     Detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and             [79] Jin Zeng, Yanfeng Tong, Yunmu Huang, Qiong Yan, Wenxiu Sun, Jing Chen, and
     Pattern Recognition. 9060–9069.                                                              Yongtian Wang. 2019. Deep surface normal estimation with hierarchical rgb-d
[58] Olaf Ronneberger, Philipp Fischer, and Thomas Brox. 2015. U-Net: Convolutional               fusion. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
     networks for biomedical image segmentation. In International Conference on                   Recognition. 6153–6162.
     Medical image computing and computer-assisted intervention. Springer, 234–241.          [80] Jing Zhang, Deng-Ping Fan, Yuchao Dai, Saeed Anwar, Fatemeh Sadat Saleh,
[59] Lucas Stoffl, Maxime Vidal, and Alexander Mathis. 2021. End-to-End Train-                    Tong Zhang, and Nick Barnes. 2020. UC-Net: uncertainty inspired rgb-d saliency
     able Multi-Instance Pose Estimation with Transformers. arXiv preprint                        detection via conditional variational autoencoders. In Proceedings of the IEEE/CVF
     arXiv:2103.12115 (2021).                                                                     Conference on Computer Vision and Pattern Recognition. 8582–8591.
[60] Lei Sun, Kailun Yang, Xinxin Hu, Weijian Hu, and Kaiwei Wang. 2020. Real-time           [81] Miao Zhang, Weisong Ren, Yongri Piao, Zhengkun Rong, and Huchuan Lu. 2020.
     fusion network for RGB-D semantic segmentation incorporating unexpected                      Select, Supplement and Focus for RGB-D Saliency Detection. In Proceedings of
     obstacle detection for road-driving images. IEEE Robotics and Automation Letters             the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 3472–3481.
     5, 4 (2020), 5558–5565.                                                                 [82] Pengchuan Zhang, Xiyang Dai, Jianwei Yang, Bin Xiao, Lu Yuan, Lei Zhang, and
[61] Peng Sun, Wenhu Zhang, Huanyu Wang, Songyuan Li, and Xi Li. 2021. Deep                       Jianfeng Gao. 2021. Multi-Scale Vision Longformer: A New Vision Transformer
     RGB-D Saliency Detection with Depth-Sensitive Attention and Automatic Multi-                 for High-Resolution Image Encoding. arXiv preprint arXiv:2103.15358 (2021).
     Modal Fusion. In Proceedings of the IEEE/CVF Conference on Computer Vision and          [83] Pingping Zhang, Wei Liu, Dong Wang, Yinjie Lei, Hongyu Wang, and Huchuan
     Pattern Recognition. 1407–1417.                                                              Lu. 2020. Non-rigid object tracking via deep multi-scale spatial-temporal dis-
[62] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones,                     criminative saliency maps. Pattern Recognition 100 (2020), 107130.
     Aidan N Gomez, Ł ukasz Kaiser, and Illia Polosukhin. 2017. Attention is All             [84] Yundong Zhang, Huiye Liu, and Qiang Hu. 2021. Transfuse: Fusing transformers
     you Need. In Advances in Neural Information Processing Systems, Vol. 30. Curran              and cnns for medical image segmentation. arXiv preprint arXiv:2102.08005 (2021).
     Associates, Inc., 5998–6008.                                                            [85] Zhao Zhang, Zheng Lin, Jun Xu, Wen-Da Jin, Shao-Ping Lu, and Deng-Ping
[63] Ziyu Wan, Jingbo Zhang, Dongdong Chen, and Jing Liao. 2021. High-Fidelity                    Fan. 2021. Bilateral attention network for RGB-D salient object detection. IEEE
     Pluralistic Image Completion with Transformers. arXiv preprint arXiv:2103.14031              Transactions on Image Processing 30 (2021), 1949–1961.
     (2021).                                                                                 [86] Hengshuang Zhao, Li Jiang, Jiaya Jia, Philip Torr, and Vladlen Koltun. 2020. Point
[64] Ningning Wang and Xiaojin Gong. 2019. Adaptive fusion for RGB-D salient                      transformer. arXiv preprint arXiv:2012.09164 (2020).
     object detection. IEEE Access 7 (2019), 55277–55284.                                    [87] Jiaojiao Zhao, Xinyu Li, Chunhui Liu, Shuai Bing, Hao Chen, Cees GM Snoek,
[65] Wenguan Wang, Jianbing Shen, and Haibin Ling. 2018. A deep network solution                  and Joseph Tighe. 2021. TubeR: Tube-Transformer for Action Detection. arXiv
     for attention and aesthetics aware photo cropping. IEEE transactions on pattern              preprint arXiv:2104.00969 (2021).
     analysis and machine intelligence 41, 7 (2018), 1531–1544.                              [88] Jiawei Zhao, Yifan Zhao, Jia Li, and Xiaowu Chen. 2020. Is depth really neces-
[66] Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao Song, Ding Liang, Tong                sary for salient object detection?. In Proceedings of the 28th ACM International
     Lu, Ping Luo, and Ling Shao. 2021. Pyramid vision transformer: A versatile back-             Conference on Multimedia. 1745–1754.
     bone for dense prediction without convolutions. arXiv preprint arXiv:2102.12122         [89] Jia-Xing Zhao, Yang Cao, Deng-Ping Fan, Ming-Ming Cheng, Xuan-Yi Li, and
     (2021).                                                                                      Le Zhang. 2019. Contrast prior and fluid pyramid integration for RGBD salient
[67] Xuehao Wang, Shuai Li, Chenglizhao Chen, Yuming Fang, Aimin Hao, and Hong                    object detection. In Proceedings of the IEEE Conference on Computer Vision and
     Qin. 2020. Data-level recombination and lightweight fusion scheme for RGB-D                  Pattern Recognition. 3927–3936.
     salient object detection. IEEE Transactions on Image Processing 30 (2020), 458–471.     [90] Xiaoqi Zhao, Lihe Zhang, Youwei Pang, Huchuan Lu, and Lei Zhang. 2020. A
[68] Yue Wang, Yuke Li, James H Elder, Runmin Wu, Huchuan Lu, and Lu Zhang.                       single stream network for robust and real-time rgb-d salient object detection. In
     2020. Synergistic saliency and depth prediction for RGB-D saliency detection. In             European Conference on Computer Vision. Springer, 646–662.
     Proceedings of the Asian Conference on Computer Vision. 1–17.                           [91] Chuanxia Zheng, Tat-Jen Cham, and Jianfei Cai. 2021. TFill: Image Completion
[69] Jun Wei, Shuhui Wang, and Qingming Huang. 2020. F3 Net: Fusion, Feedback                     via a Transformer-Based Architecture. arXiv preprint arXiv:2104.00845 (2021).
     and Focus for Salient Object Detection. In Proceedings of the AAAI Conference on        [92] Sixiao Zheng, Jiachen Lu, Hengshuang Zhao, Xiatian Zhu, Zekun Luo, Yabiao
     Artificial Intelligence. 12321–12328.                                                        Wang, Yanwei Fu, Jianfeng Feng, Tao Xiang, Philip HS Torr, et al. 2021. Re-
[70] Sanghyun Woo, Jongchan Park, Joon-Young Lee, and In So Kweon. 2018. CBAM:                    thinking semantic segmentation from a sequence-to-sequence perspective with
     Convolutional block attention module. In Proceedings of the European conference              transformers. In Proceedings of the IEEE/CVF Conference on Computer Vision and
     on computer vision (ECCV). 3–19.                                                             Pattern Recognition. 6881–6890.
[71] Bichen Wu, Chenfeng Xu, Xiaoliang Dai, Alvin Wan, Peizhao Zhang, Masayoshi              [93] Chunbiao Zhu, Xing Cai, Kan Huang, Thomas H Li, and Ge Li. 2019. PDNet:
     Tomizuka, Kurt Keutzer, and Peter Vajda. 2020. Visual transformers: Token-                   Prior-model guided depth-enhanced network for salient object detection. In 2019
     based image representation and processing for computer vision. arXiv preprint                IEEE International Conference on Multimedia and Expo (ICME). IEEE, 199–204.
     arXiv:2006.03677 (2020).                                                                [94] Kuan Zhu, Haiyun Guo, Shiliang Zhang, Yaowei Wang, Gaopan Huang, Honglin
[72] Haiping Wu, Bin Xiao, Noel Codella, Mengchen Liu, Xiyang Dai, Lu Yuan, and                   Qiao, Jing Liu, Jinqiao Wang, and Ming Tang. 2021. AAformer: Auto-Aligned
     Lei Zhang. 2021. CvT: Introducing Convolutions to Vision Transformers. arXiv                 Transformer for Person Re-Identification. arXiv preprint arXiv:2104.00921 (2021).
