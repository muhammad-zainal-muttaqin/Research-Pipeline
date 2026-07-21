---
source_id: 170
bibtex_key: wu2022mobilesal
title: MobileSal: Extremely Efficient RGB-D Salient Object Detection
year: 2022
domain_theme: RGB-D SOD
verified_pdf: 170_MobileSal.pdf
char_count: 95485
---

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                                                          1

                                                                  MobileSal: Extremely Efficient
                                                                 RGB-D Salient Object Detection
                                                        Yu-Huan Wu, Yun Liu, Jun Xu, Jia-Wang Bian, Yu-Chao Gu, and Ming-Ming Cheng

                                              Abstract—The high computational cost of neural networks has prevented recent successes in RGB-D salient object detection (SOD) from
                                              benefiting real-world applications. Hence, this paper introduces a novel network, MobileSal, which focuses on efficient RGB-D SOD using
                                              mobile networks for deep feature extraction. However, mobile networks are less powerful in feature representation than cumbersome
                                              networks. To this end, we observe that the depth information of color images can strengthen the feature representation related to SOD
                                              if leveraged properly. Therefore, we propose an implicit depth restoration (IDR) technique to strengthen the mobile networks’ feature
                                              representation capability for RGB-D SOD. IDR is only adopted in the training phase and is omitted during testing, so it is computationally
arXiv:2012.13095v3 [cs.CV] 12 Jan 2022

                                              free. Besides, we propose compact pyramid refinement (CPR) for efficient multi-level feature aggregation to derive salient objects with
                                              clear boundaries. With IDR and CPR incorporated, MobileSal performs favorably against state-of-the-art methods on six challenging
                                              RGB-D SOD datasets with much faster speed (450fps for the input size of 320 × 320) and fewer parameters (6.5M). The code is released
                                              at https://mmcheng.net/mobilesal.

                                              Index Terms—RGB-D Salient Object Detection, Efficiency, Implicit Depth Restoration.

                                                                                                                 F

                                         1    I NTRODUCTION                                                                                  0.920               Accuracy VS Speed
                                         Salient object detection (SOD) aims to locate and segment                                                                                        Ours
                                         the most eye-catching object(s) in natural images. It is a
                                                                                                                                             0.915
                                                                                                                                                      JLDCF'20
                                         fundamental problem in image understanding and serves                                                                           D3Net'20
                                                                                                                      Accuracy (F-measure)

                                                                                                                                             0.910          UCNet'20
                                         as a preliminary step for many computer vision tasks such
                                         as visual tracking [1], content-aware image editing [2], and                                        0.905                DANet'20
                                         weakly supervised learning [3]. Current SOD methods are
                                         mainly developed for RGB images [4]–[6], which are usually                                          0.900    S2MA'20
                                         hindered by indistinguishable foreground and background                                                           DMRA'19
                                         textures. To this end, researchers resort to the easily accessible                                  0.895
                                         depth information as an important complement to the RGB
                                         counterpart, with promising progress in RGB-D SOD [7]–[14].                                         0.890 CPFP'19TANet'19
                                             While convolutional neural networks (CNNs) have made
                                         brilliant achievements on RGB-D SOD [8]–[12], [14], their                                           0.8855          PCF'18
                                                                                                                                                        10                          100    500
                                         high accuracy often comes at the expense of high com-                                                                        Speed (FPS)
                                         putational costs and large model size. This situation has
                                         prevented recent state-of-the-art methods [8], [14] from being              Figure 1. Comparison with state-of-the-art methods (see references in
                                         applied to real-world applications, especially for those on                 Table 1) on the challenging NJU2K [15] dataset. Our method (MobileSal
                                                                                                                     shows very competitive accuracy and much faster speed.
                                         mobile devices, which are depth accessible, with very limited
                                         energy overhead and computational capability. Hence, it
                                         is essential to design efficient networks for accurate RGB-
                                         D SOD. A naı̈ve solution towards this goal is to adopt                      hinder lightweight networks from accurate RGB-D SOD
                                         lightweight backbones such as MobileNets [16], [17] and                     performance.
                                         ShuffleNets [18], [19] for deep feature extraction, instead                     To overcome this challenge, we note that the depth
                                         of commonly-used cumbersome backbones like VGG [20]                         information of color images, if leveraged properly, can
                                         and ResNets [21]. The problem is that lightweight networks                  strengthen the feature representation for RGB-D SOD [8],
                                         are usually less powerful than cumbersome networks on                       [9]. Unlike some existing studies [11], [12] that leverage the
                                         feature representation learning, as widely acknowledged                     depth information explicitly, in this paper, we propose an
                                         by the research community [16]–[19]. This problem would                     implicit depth restoration (IDR) technique to strengthen the
                                                                                                                     feature representation learning of the lightweight backbone
                                                                                                                     network so as to ensure the accuracy of RGB-D SOD in an
                                         •   Corresponding author: M.-M. Cheng. (E-mail: cmm@nankai.edu.cn)
                                         •   Y.-H. Wu, Y. Liu, J. Xu, Y.-C. Gu, and M.-M. Cheng are with the         efficient setting. More importantly, IDR is only adopted in
                                             TKLNDST, College of Computer Science, Nankai University, Tianjin,       the training phase and is omitted during testing, so it is
                                             China, 300350.                                                          computationally free during the inference stage. Specifically,
                                         •   J.-W. Bian is with the University of Adelaide.
                                                                                                                     we enforce our model to restore the depth map from high-
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                                       2

level backbone features, through which the representation           Zhao et al. [8] proposed a contrast-prior-based network,
learning of the lightweight backbone becomes more powerful          providing strong depth enhancement. Piao et al. [9] proposed
with important supervision on the depth stream. Besides the         to refine depth via depth-induced multi-scale recurrent
IDR module, we propose two more components to ensure the            attention (DMRA). Huang et al. [49] proposed RGB-D fusion
high efficiency: i) we conduct RGB and depth information            via joint cross-modal and unimodal features, providing
fusion only at the coarsest level, because such a small             more comprehensive RGB-D analysis. Zhang et al. [11]
feature resolution (i.e., 1/32 scale) is essential for reducing     provided another perspective of uncertainty RGB-D saliency
computational cost; ii) we propose a compact pyramid                via conditional variational autoencoders. Chen et al. [51]
refinement (CPR) module to efficiently aggregate multi-scale        first introduced 3D CNNs to RGB-D SOD, providing more
deep features, for accurate SOD with clear boundaries.              abundant spatial semantics. Ji et al. [52] introduced a flexible
    With MobileNetV2 [17] as the backbone network, Mobile-          depth calibration module, providing reliable complementary
Sal achieves 450fps on a single NVIDIA RTX 2080Ti GPU               information for saliency models. Zhao et al. [47] proposed a
with the input size of 320 × 320, tens of times faster than         self-supervised learning framework, which only leverages
existing RGB-D SOD methods [8], [9], [14], [22]. Extensive          image-level annotations saving large costs from large-scale
experiments on six challenging datasets demonstrate that            data annotations. More inspiring related works can refer to
MobileSal also achieves competitive performance compared            the recent survey [53].
with state-of-the-art methods (max F-measure of 91.4% and               In terms of the fusion strategy of RGB and depth infor-
91.2% on NJU2K [15] and DUTLF [9] datasets, respectively)           mation, the diagrams of RGB-D SOD architectures can be
with fewer parameters (6.5M). Such high efficiency, good            broadly divided into late fusion [42], [54], [55], early fusion
accuracy, and small model size would benefit many real-             [11]–[13], [51], and multi-scale fusion [8], [9], [14], [22], [46]–
world applications.                                                 [49]. Late fusion appears at the end of feature extraction and
    In summary, our main contributions include:                     only predicts the result from the fused features [42], [54],
   • To the best of our knowledge, MobileSal is the first to        [55]. Early fusion directly concatenates the input RGB image
     shed light upon efficient RGB-D SOD by proposing an            and depth map and then derives the saliency map from such
     extremely efficient network with a speed of 450fps.            RGB-D input using the encoder-decoder network [12] or
   • To ensure the efficiency of MobileSal on cross-modal           hypercolumn network [11]. Multi-scale fusion first extracts
     fusion, MobileSal fuses RGB and depth information only         RGB and depth features separately and then aggregates RGB-
     at the coarsest level and then efficiently aggregates multi-   D features at all levels [9], [49], at middle and high levels [56],
     level deep features using a compact pyramid refinement         or at middle levels [46]. Although the early fusion strategy
     (CPR) module.                                                  is more efficient, multi-scale fusion is more accurate. To
   • To ensure the accuracy of MobileSal, we propose an             ensure high efficiency, our method only fuses RGB and depth
     implicit depth restoration (IDR) technique to strengthen       features at the coarsest level in a small resolution. IDR is then
     the less powerful features learned by mobile backbone          applied to strengthen the feature representation learning of
     networks. This technique is also applicable to other seg-      mobile networks in a computationally free manner.
     mentation tasks such as RGB-D semantic segmentation.
                                                                    2.3   Efficient Backbone Networks
                                                                    Recent growing interests in mobile vision applications have
2     R ELATED W ORK
                                                                    generated a high demand for efficient CNNs. Mobile de-
2.1   Salient Object Detection                                      vices such as autonomous driving vehicles, robots, and
Benefited from the rapid development of deep CNNs [20],             smartphones only have limited computational resources,
[21] in recent years, CNNs-based SOD methods for RGB                so traditional cumbersome networks, like VGG [20] and
images [5], [6], [23]–[28] have achieved substantial progress       ResNets [21], are unsuitable for these platforms. To this end,
compared with conventional methods [29]–[34]. Along this            some efficient networks are proposed for image classification,
direction, much attention is paid to design various effective       such as MobileNets [17], ShuffleNets [19], MnasNet [57], etc.
strategies to fuse multi-scale features generated by multi-         There also emerge some efficient networks for semantic
level CNN layers [6], [23], [24], [26]. Some efforts are also       segmentation [58], object detection [59], and ordinary RGB
spent on exploring the effectiveness of extra boundary              SOD [60], [61]. These efficient networks are with low compu-
information [24], [25], [35] or part-object relationship [36].      tational costs and thus flexible for mobile platforms. In this
Detailed introductions of SOD works can refer to recent             paper, we are the first to shed light upon efficient RGB-D
popular surveys [37]–[39]. Despite many success stories,            SOD by adopting MobileNetV2 [17] as the backbone for deep
RGB SOD is hindered by indistinguishable foreground and             feature extraction. Our proposed techniques aim to ensure
background textures, which can be largely alleviated by             the SOD accuracy and high efficiency simultaneously in such
incorporating the depth information, i.e., RGB-D SOD.               a lightweight setting.

2.2   RGB-D Salient Object Detection                                3     M ETHODOLOGY
Like early SOD methods, conventional RGB-D SOD works                In this section, we first provide an overview of our method
extract hand-crafted features from RGB and depth maps               in §3.1. Then, we introduce the proposed cross-modal feature
and fuse them together [40]–[45]. Recently, RGB-D SOD has           fusion scheme in §3.2, implicit depth restoration in §3.3,
gained more attention and deep-learning-based RGB-D SOD             compact pyramid refinement in §3.4. Finally, we present the
has been developed rapidly [8]–[13], [46]–[50]. Typically,          hybrid loss function in §3.5.
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                                             3

                                                                                                            Element-wise Multiplication
                                                       Ground Truth                                  C      Concatenation
                                                                                                           Sigmoid Function
                                                                                                    IRB     Inverted Residual Block
              RGB-D                                                                                 GAP     Global Average Pooling
      1×1     Stream      1×1                 1×1                 1×1                   1×1
                                                                                                    CPR     Compact Pyramid Refinement
      CPR        C       CPR         C        CPR        C        CPR         C         CPR         IDR     Implicit Depth Restoration
                                                                                                   CMF      Cross-Modality Fusion

                                                                                                           GAP
                                                                                                                 1×1

                                                                                                                       1×1
                                                                                                                              
 RGB Image
                                            IDR                                        CMF                       IRB               IRB
                                                    Depth Restoration               RGB-D
                                                                                  Integration

                                                                                                RGB Flow                     RGB-D Flow
 Depth Map                                                                                      Depth Flow                   Supervision
                                      Separate Streams of RGB and Depth

Figure 2. The pipeline of MobileSal. We fuse RGB and depth information only at the coarsest level and then efficiently do the multi-scale
aggregation with CPRs. The IDR branch strengthens the less powerful features learned by the mobile networks in a computationally free manner.

3.1   Overview                                                          are denoted as D1 , D2 , D3 , D4 , D5 , the first four of which
                                                                        have 16, 32, 64, 96 channels, respectively. D5 and C5 have the
Fig. 2 depicts the overall architecture of our method. We use
                                                                        same number of channels and the same stride.
RGB and depth streams for separate feature extraction.
                                                                             As shown in Fig. 2, with the outputs of the RGB and
    RGB Stream. We employ MobileNetV2 [17] as the back-                 depth stream, we first fuse the extracted RGB feature C5
bone of our method. To adapt it to the SOD task, we remove              and depth feature D5 to generate the RGB-D feature C5D .
the global average pooling layer and the last fully-connected           The proposed IDR technique restores the depth map from
layer from the backbone. For the RGB stream, each stage                 C1 , C2 , C3 , C4 , C5D , which is supervised by the input depth
is followed by a convolutional layer with a stride of 2, and            map to strengthen the feature representation learning. For
thus feature maps are downsampled into half resolution                  saliency prediction, we design a lightweight decoder using
after each stage. For convenience, we denote the output                 the CPR module as the basic unit. The output of the decoder
feature maps for five stages as C1 , C2 , C3 , C4 , C5 , with strides   at the bottom stage is the final predicted saliency map. More
of 2, 22 , 23 , 24 , 25 , respectively.                                 details can be seen in the following sections.
    Depth Stream. Similar to the RGB stream, the depth
stream also has five stages with the same strides. Since
depth maps contain less semantic information than the                   3.2   Cross-Modal Fusion of RGB and Depth Features
corresponding RGB images, we build a lightweight depth                  The depth map reveals spatial cues of color images, which
network with fewer convolutional blocks than the RGB                    helps distinguish the foreground objects from the back-
stream. Each stage only has two Inverted Residual Blocks                ground, especially for scenarios with complicated textures.
(IRB) [17]. Such a design reduces computational complexity              As demonstrated by previous studies [8], [9], [14], [22],
that accords with the goal of efficient RGB-D SOD. In each              [46], [48], proper RGB and depth feature fusion is essential
IRB, we first expand the feature map along the channel                  for accurate RGB-D SOD. Our main consideration here
dimension by M times via a 1 × 1 convolution, followed                  is to ensure the high efficiency of our method. Instead
by a depthwise separable 3 × 3 convolution [16] with the                of conducting fusion at multiple levels [8], [9], [14], [22],
same number of input and output channels. Then, the feature             [46], [48], [64], we only fuse RGB and depth features at the
channels are squeezed to 1/M via another 1 × 1 convolution.             coarsest level because the small feature resolution leads to
Here, each convolution is followed by Batch Normalization               low computational cost.
(BN) [62] and ReLU [63] layers, except for the last 1 × 1                   According to the above analyses, we only fuse the RGB
convolution that only has a BN layer. The final output of               feature map C5 and the depth feature map D5 . We design
the inverted residual block is the element-wise sum of the              a lightweight Cross-Modal Fusion (CMF) module for this
initial input and the output generated by the above three               purpose, as shown in Fig. 2. Intuitively, semantic information
sequential convolutions. For the first layer in each stage, the         mainly exists in the RGB image. The depth map conveys the
stride of the depthwise separable convolution is set as 2, and          prior of depth-smooth regions that approximately represent
the number of hidden feature channels is increased if needed.           the shapes and structures of complete objects or stuff. Hence,
The output feature maps of five stages of the depth stream              we adopt depth features like a gate to enhance RGB semantic
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                                                                                                             4

      16×160×160                   256×20×20
                                                                                                                                           D-Conv,d=1

                                                                                                                                                                    BN-ReLU
      32×80×80

                                                   1280×20×20
                                   256×20×20

                                                                      256×20×20

                                                                                                                                   1×1

                                                                                                                                                                                  1×1

                                                                                                                                                                                             1×1
                                                                                                                                           D-Conv,d=2

                   1×1 - Rescale
      64×40×40                     256×20×20

                                                                1×1

                                                                                              IRB
                                                                                  IRB
                                                                                        IRB

                                                                                                    IRB
                                                                                                          1×1
                                               C                                                                                           D-Conv,d=3

                                                                                                                                                  GAP
                                                                                                                                                                              

                                                                                                                                                        1×1

                                                                                                                                                              1×1
      96×20×20                     256×20×20                                                                    Depth Map
      320×10×10                    256×20×20                                                                                                                                            Element-wise Sum
                                    (a) Implicit Depth Restoration (IDR)                                                                 (b) Compact Pyramid Refinement (CPR)
Figure 3. Illustration of the proposed IDR and CPR. (a) The IDR branch strengthens the less powerful features of the mobile backbone network.
(b) Multi-level deep features are efficiently aggregated by the CPR module. “D-Conv” indicates depthwise separable convolution.

features through multiplication, which can be viewed as and highlight the difference among them. In this way, the
a strong regularization. Note that element-wise addition contrast between salient objects and the background will
or concatenation can only aggregate two feature maps by be strengthened too. With this idea, we design an Implicit
treating features equally, which is orthogonal to our goal. Depth Restoration (IDR) technique. Here, we use the word
Experiments in §4.3 also demonstrate our hypothesis.              “implicit” because IDR is only adopted in the training phase
    Specifically, we first combine the RGB and depth features and is omitted during testing, making it computationally free
with an above-mentioned IRB to derive the transited RGB-D for practical deployment.
feature maps T , which can be formulated as                           We continue by introducing how to use C1 , C2 , C3 , C4 , C5D
                                                                  for the above auxiliary supervision. As shown in Fig. 3 (a),
                       T = IRB(C5 ⊗ D5 ),                     (1) the pipeline of IDR is simple, i.e., just concatenating multi-
where and ⊗ is the element-wise multiplication operator. level feature maps and then fusing them. Specifically, we                D
Meanwhile, we apply a global average pooling (GAP) layer first apply a 1 × 1 convolution to squeeze C1 , C2 , C3 , C4 , C5
to C5 to get a feature vector, followed by two fully-connected    to the same  number  of channels, i.e., 256. Then, the resulting
layers to compute the RGB attention vector v, like                feature maps are resized to the same size as C4 , followed
                                                                  by the concatenation of them. A 1 × 1 convolution changes
            v = σ(FC2 (ReLU(FC1 (GAP(C5 ))))),                (2) the concatenated feature map from 1280 channels to 256
                                                                  channels for saving computational cost. Next, four sequential
in which FC and ReLU denote fully-connected and ReLU
                                                                  IRBs are followed to fuse multi-level features so that we
layers, respectively. The number of output channels of FC1
                                                                  can obtain powerful multi-scale features. At last, a simple
and FC2 is the same as the input. σ indicates the standard
                                                                  1 × 1 convolution converts the fused feature map to a single
sigmoid function. With T and v computed, the multiplication
                                                                  channel. With a standard sigmoid function and bilinear
of v, T , and D5 are fed into an IRB, like
                                                                  upsampling, we can obtain the restored depth map with
                     D
                   C5 = IRB(v ⊗ T ⊗ D5 ),                     (3) the same size as the input. The training loss of IDR adopts
                                                                  the well-known SSIM metric [65] to measure the structural
where C5D indicates the output feature map of the CMF similarity between the restored depth map Dr and input one
module. Note that v is replicated to the same shape as T          Dg , which can be written as
before multiplication. Eq. (3) filters RGB semantic features
again by multiplying D5 , and the channel attention v is used                      LIDR = 1 − SSIM(Dr , Dg ),                   (4)
to recalibrate the fused features. After the fusion of RGB where SSIM uses the default setting. Note that the above
and depth features, we can derive the backbone features, operations are omitted during testing to make IDR free.
including the RGB features C1 , C2 , C3 , C4 , and the fused RGB-
D feature C5D .
                                                                  3.4 Compact Pyramid Refinement
                                                                                                                            It is widely accepted that high-level features in the backbone
3.3     Implicit Depth Restoration                                                                                          network contain semantic abstract features, while low-level
As widely acknowledged [16]–[19], lightweight backbone                                                                      features convey fine-grained details. For accurate SOD, it
networks are less powerful in feature representation learning                                                               is essential to fully utilize both high-level and low-level
than cumbersome networks. To ensure the accuracy of                                                                         features. There exists a lot of literature on this topic [8],
RGB-D SOD, we consider strengthening the representation                                                                     [9], [13], [14], [22], but existing methods usually design
learning of mobile networks. We observe that the depth map                                                                  cumbersome decoders without consideration of efficiency.
conveys depth-smooth regions that usually represent objects,                                                                Here, our decoder should not only fuse multi-level features
object parts, or smooth background, because intuitively,                                                                    effectively but also be efficient as much as possible.
an object or a connected stuff region usually has similar                                                                        The proposed decoder uses the Compact Pyramid Re-
depth. This observation motivates us to use the depth map                                                                   finement (CPR) module as the basic unit. For efficiency, CPR
as an extra supervision source to guide the representation                                                                  uses 1 × 1 and depthwise separable convolutions [16] instead
learning, which would help mobile networks restrain the                                                                     of vanilla convolutions in previous methods [12]–[14], [22].
texture changes within objects or connected stuff regions                                                                   Since multi-level features exhibit multi-scale representations
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                                     5

with the high level corresponding to the coarse scale and vice
versa, multi-scale learning would be necessary for multi-level
feature fusion. Hence, CPR adopts a lightweight multi-scale
learning strategy to enhance such fusion. Suppose that the
input of a CPR module is X . As shown in Fig. 3 (b), CPR
first applies a 1 × 1 convolution to expand the number of
channels by M times. Then, three 3 × 3 depthwise separable
convolutions with dilation rates of 1, 2, 3 are connected
parallel for multi-scale fusion. This can be formulated as
           X1 = Conv1×1 (X ),
           X2d1 = Convd3×3
                        1
                           (X1 ),
           X2d2 = Convd3×3
                        2
                           (X1 ),                          (5)
           X2d3 = Convd3×3
                        3
                           (X1 ),
           X2 = ReLU(BN(X2d1 + X2d2 + X2d3 )),
where d1 , d2 , and d3 are dilation rates, i.e., 1, 2, 3 here,
                                                                   Image   Depth    GT     Ours    CPFP   JLDCF    S2MA    UCNet
respectively. BN is the abbreviation of batch normalization
[62]. A 1 × 1 convolution is used to squeeze channels to the      Figure 4. Qualitative comparison of six challenging datasets. The
same number as the input, i.e.,                                   results from top to bottom are from NJU2K, DUTLF-D, NLPR, STERE,
                                                                  SSD, and SIP datasets, respectively.
                  X3 = Conv1×1 (X2 ) + X ,                 (6)
which uses a residual connection for better optimization. The     where λ is a balance weight. In the testing phase, P1 is the
attention mechanism in Eq. (2) is applied to X to calculate       final predicted saliency map.
an attention vector v0 , so that we have
                  Y = v0 ⊗ Conv1×1 (X3 ).                  (7)
                                                                  4     E XPERIMENTS
Eq. (7) uses global contextual information to recalibrate the     We first provide the experimental setup in §4.1. Then, we
fused features.                                                   compare with state-of-the-art RGB-D SOD methods in §4.2
    As shown in Fig. 2, at each decoder stage, two feature        and conduct comprehensive ablation studies in §4.3. We also
maps from the top decoder and the corresponding encoder           discuss the applications of IDR in §4.4.
stage first reduce their numbers of channels to half using a 1×
1 convolution separately. The results are then concatenated,
followed by a CPR module for feature fusion. In this way,         4.1   Experimental Setup
our lightweight decoder aggregates multi-level features from      Implementation details. We implement our network in
top to bottom.                                                    PyTorch [70] and Jittor [71]. If not specified, we use Mo-
                                                                  bileNetV2 [17] as our backbone. The M values in the depth
3.5 Hybrid Loss Function                                          stream, CPR, and IDR are set to 4, 4, and 6, respectively.
At each decoder stage, we predict the saliency map by We resize both RGB and depth images into 320 × 320. We
sequentially adding a 1×1 convolution with a single channel, use horizontal flipping and random cropping as the default
a sigmoid function, and bilinear upsampling to the output of data augmentation for the ablation study. After freezing the
the CPR module, as shown in Fig. 2. Hence, we can derive designs and parameters, we apply multi-scale training, i.e.,
predicted saliency maps Pi (i = 1, 2, · · · , 5) for five stages, each image is resized into [256, 288, 320] in training, but we
respectively. Let the ground-truth saliency map be G . The keep the size of test images unchanged. We use a single RTX
loss of each side-output can be computed as                       2080Ti GPU for training and testing. The initial learning rate
                                                                  lr is 0.0001, and the batch size is 10. We train our network
               Lisal = BCE(Pi , G) + Dice(Pi , G),            (8) for 60 epochs. The poly learning rate policy is applied, so
BCE denotes binary cross-entropy loss function:                   that the actual learning rate for each epoch cur epoch is
                                                                  (1 − cur 60epoch power
                                                                                   )     × lr, where power is 0.9. The Adam
      BCE(Pi , G) = G · log Pi + (1 − G) · log(1 − Pi ), (9) optimizer [72] is used for optimizing our networks, and the
where “·” indicates the dot-product operation. Dice repre- momentum, weight decay, β1 , and β2 are set as 0.9, 0.0001,
sents the Dice loss [66]:                                         0.9, and 0.99, respectively.
                                                                      Datasets. We conduct experiments on seven widely-used
                                     2 · G · Pi
                Dice(Pi , G) = 1 −                 ,         (10) datasets,   including NJU2K [15], DUTLF-D [9], NLPR [44],
                                   ||G|| + ||Pi ||                STERE [73], SSD [74], and SIP [10]. They contain 1985, 1200,
where || · || denotes the `1 norm. With deep supervision and 1000, 1000, 80, 927 images, respectively. Following [8], [11],
IDR, the training loss can be formulated as                       [12], [22], we use 1500 images of NJU2K [15] and 700 images
                          5
                                                                  of NLPR [44] for training, and the other 485 images of
                         X
                              i                                   NJU2K [15] and 300 images of NLPR [44] for testing. Except
                     L=      Lsal + λ · LIDR ,               (11)
                                                                  for DUTLF-D [9], other datasets are directly used for testing.
                       i=1
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                                                                         6

                                                                  Table 1
Quantitative results on six challenging datasets. The best, second best, and third best results are highlighted in red, blue and bold, respectively.
                                           Our method achieves the best speed-accuracy trade-off.

     Method       DESM      LHM      ACSD DCMC CTMF                 PCF     TANet CPFP DMRA D3Net JLDCF S2MA UCNet DANet BiANet MobileSal
 #PubYear [Ref] 2014 [45] 2014 [44] 2014 [15] 2016 [67] 2017 [54] 2018 [68] 2019 [7] 2019 [8] 2019 [9] 2020 [10] 2020 [14] 2020 [22] 2020 [11] 2020 [12] 2021 [69] (Ours)
   Params (M)        -         -         -         -         -      133.4    232.4     69.5     59.7      43.2     137.0      86.7      33.3      26.7      49.6     6.5
  Speed (FPS)        -         -        1          -        8        17        14       6        16        65        9         9         17        32        50      450
          Fβmax ↑ 0.767     0.703     0.749     0.759     0.857     0.887    0.888 0.890 0.896           0.910     0.912     0.898     0.908     0.904     0.908    0.914
         MAE ↓ 0.286        0.204     0.200     0.171     0.085     0.059    0.060 0.053 0.051           0.047     0.041     0.054     0.043     0.047     0.044    0.041
 NJU2K      Sα ↑ 0.671      0.515     0.708     0.686     0.849     0.877    0.878 0.878 0.886           0.900     0.902     0.894     0.897     0.897     0.904    0.905
          Eξmax ↑ 0.807     0.738     0.814     0.805     0.913     0.924    0.925 0.923 0.927           0.939     0.944     0.930     0.936     0.936     0.941    0.942
         Rank ↓     15        15        13        13        12        11       10        9        8         4        2         7         5          6        3        1
            max
          Fβ ↑ 0.728        0.652     0.212     0.419     0.811     0.782    0.804 0.740 0.887           0.748     0.884     0.882     0.836     0.869     0.885    0.912
         MAE ↓ 0.293        0.162     0.320     0.232     0.095     0.100    0.092 0.100 0.053           0.099     0.053     0.054     0.064     0.054     0.048    0.041
DUTLF-D Sα ↑ 0.659          0.568     0.361     0.499     0.831     0.801    0.808 0.749 0.888           0.775     0.906     0.903     0.863     0.889     0.906    0.896
            max
          Eξ ↑ 0.800        0.734     0.590     0.654     0.899     0.856    0.861 0.811 0.933           0.834     0.943     0.937     0.904     0.931     0.946    0.950
         Rank ↓     13        14        16        15         8        10        9       12        4        11        3         5         7          6        2        1
          Fβmax ↑ 0.680     0.693     0.664     0.706     0.841     0.863    0.877 0.888 0.888           0.907     0.925     0.910     0.915     0.907     0.921    0.916
         MAE ↓ 0.316        0.104     0.163     0.112     0.056     0.044    0.041 0.036 0.031           0.030     0.022     0.030     0.025     0.031     0.024    0.025
  NLPR      Sα ↑ 0.573      0.631     0.684     0.729     0.860     0.874    0.886 0.888 0.899           0.912     0.925     0.915     0.920     0.909     0.927    0.920
            max
          Eξ ↑ 0.808        0.763     0.800     0.795     0.929     0.925    0.941 0.932 0.947           0.953     0.963     0.953     0.956     0.949     0.962    0.961
         Rank ↓     16        14        15        13        12        11       10        9        8         6        1         5         4          7        2        3
            max
          Fβ ↑ 0.738        0.752     0.682     0.789     0.848     0.875    0.878 0.889 0.895           0.904     0.913     0.895     0.908     0.895     0.908    0.906
         MAE ↓ 0.301        0.172     0.197     0.148     0.086     0.064    0.060 0.051 0.047           0.046     0.040     0.051     0.039     0.048     0.042    0.041
 STERE      Sα ↑ 0.642      0.562     0.692     0.731     0.848     0.875    0.871 0.879 0.886           0.899     0.903     0.890     0.903     0.892     0.904    0.903
            max
          Eξ ↑ 0.811        0.771     0.806     0.819     0.912     0.925    0.923 0.925 0.938           0.938     0.947     0.932     0.944     0.930     0.944    0.940
         Rank ↓     14        14        14        13        12        10       10        9        6         5        2         7         1         7         3        4
            max
          Fβ ↑ 0.720        0.633     0.709     0.755     0.744     0.833    0.835 0.801 0.858           0.856     0.860     0.878     0.881     0.878     0.870    0.863
         MAE ↓ 0.313        0.195     0.204     0.169     0.098     0.062    0.063 0.082 0.059           0.059     0.053     0.053     0.049     0.050     0.052    0.052
   SSD      Sα ↑ 0.602      0.566     0.675     0.704     0.776     0.841    0.839 0.807 0.857           0.857     0.860     0.868     0.866     0.869     0.870    0.862
            max
          Eξ ↑ 0.769        0.717     0.785     0.786     0.865     0.894    0.897 0.852 0.906           0.910     0.902     0.909     0.907     0.907     0.907    0.914
         Rank ↓     15        16        14        13        12         9        9       11        8         6        7         3         1          3        2        5
            max
          Fβ ↑ 0.720        0.634     0.788     0.680     0.717     0.860    0.849 0.869 0.852           0.880     0.903     0.891     0.896     0.900     0.895    0.898
         MAE ↓ 0.303        0.184     0.175     0.186     0.140     0.071    0.075 0.064 0.086           0.063     0.049     0.057     0.051     0.054     0.051    0.053
   SIP      Sα ↑ 0.616      0.511     0.732     0.683     0.716     0.842    0.835 0.850 0.806           0.860     0.880     0.872     0.875     0.878     0.884    0.873
            max
          Eξ ↑ 0.770        0.716     0.838     0.743     0.829     0.901    0.895 0.903 0.875           0.909     0.925     0.919     0.919     0.921     0.928    0.916
         Rank ↓     14        16        12        15        13         9       10        8       11         7        1         6         4          3        2        5

                              Table 2                                                                                 Table 4
CPU inference time of different methods. Default input size of each                   Ablation study for the RGB-D fusion and IDR branch. Note that the
           method is applied to test CPU inference time.                              variants of No. 6 and 12 (in bold) fuse RGB and depth features only at
                                                                                                             the coarsest feature level.
         Method                   Ours          JLDCF [14]       UCNet [11]
        Input Size              320 × 320        320 × 320       352 × 352                            Features to be fused                          Fβmax
                                                                                            No.                                           IDR                 MAE
   Inference Time (ms)           43 (1×)        7246 (150×)       784 (18×)                         C1  C2     C3     C4   C5
         Method                 D3Net [10]       S2MA [22]       DMRA [9]                     1     4    4     4      4    4                 4      0.899      0.052
        Input Size              224 × 224        256 × 256       256 × 256                    2     4    4                                   4      0.894      0.050
   Inference Time (ms)          677 (15×)        3049 (70×)      2381 (55×)                   3     4    4     4                             4      0.897      0.047
                                                                                              4          4     4      4                      4      0.902      0.048
                                                                                              5                4      4    4                 4      0.902      0.046
                                  Table 3                                                     6                            4                 4      0.906      0.045
   Quantitative comparisons of restored depth maps by IDR with                                7     4    4     4      4    4                        0.895      0.047
  different scales of input depth maps. The ground-truth depth (GT)                           8     4    4                                          0.892      0.049
recovered from different resolutions using different interpolation methods                    9     4    4     4                                    0.896      0.048
                             are compared.                                                   10          4     4      4                             0.895      0.048
                                                                                             11                4      4    4                        0.898      0.048
    Setting             (a)             (b)            (c)            (d)                    12                            4                        0.896      0.047
     Scale            1/16             1/8           1/32             1/8                    13                                                     0.887      0.052
     Data              IDR             GT             GT              GT
    Up Type          Bilinear        Bilinear       Bilinear        Nearest
     PSNR             22.86           30.17          22.55           24.27            S-measure Sα [76] and maximum E-measure Eξmax [77] under
     SSIM             .8687           .9194          .8445           .8170
                                                                                      different thresholds for reference. We follow the official paper
                                                                                      to compute Sα and Eξmax . We calculate the overall rank of
On the DUTLF-D [9] dataset, we follow [9], [12] to use 800                            each method on each dataset based on the above four metrics.
images for training and the other 400 images for testing.                             Besides, we report the number of parameters and running
    Evaluation metrics. Following recent works [7], [8], [11],                        time of each method for efficiency analysis.
[68], we adopt two widely-used metrics for evaluation. The
first is F-measure Fβ , where β is set as 0.3 to emphasize the                        4.2    Comparison to state-of-the-art methods
significance of the precision, as suggested by [8], [9], [12],                       We first compare our method with 15 recent state-of-the-
[75]. We compute the maximum Fβ as Fβmax under different                             art methods published on six widely-used datasets. Most
thresholds. Higher Fβmax indicates better performance. The                           methods are based on VGG-16 [20], except the ResNet-101-
second is the Mean Absolute Error (MAE), which is the                                based JLDCF and ResNet-50-based UCNet. The saliency
lower, the better. We also report scores of recently proposed                        maps of other methods are from their released results if
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                                           7

                           Table 5                                         4.3   Ablation Study
Comparison of RGB-D fusion strategies. The results of default fusion
                 strategy are with bold fonts.                             We evaluate each proposed component on the test split of
                                                                           the NJU2K [15] dataset. Fβmax and MAE are applied as the
     Metric
                      Single Stream              Two Streams               primary metrics. The results are analyzed below.
                   IDR 4         IDR 6        IDR 4       IDR 6                Different RGB-D fusions. Table 4 shows the results for
     Fβmax          0.900         0.894        0.906       0.896
                                                                           the RGB-D fusion at different stages. When trained with the
     MAE            0.048         0.051        0.045       0.047
                                                                           IDR branch, fusing RGB and depth features at the coarsest
                                                                           level results in the best performance (No. 6). Fusing RGB
                                                                           and depth features in the last three levels results in the best
                                                                           performance when trained without the IDR branch (No. 11).
                                                                           The IDR branch substantially improves the performance in
                                                                           most cases (No. 3 - 6), and only MAE (fusing low-level
                                                                           features) degrades (No. 1, 2). This validates the efficacy
                                                                           of the combination of our proposed fusion strategy and
                                                                           the IDR branch. We also compare the used fusion strategy
                                                                           with the early fusion strategy, which concatenates the input
                                                                           RGB image and depth map at the input stage. Although the
                                                                           latter strategy is more efficient, our initial fusion strategy
                                                                           significantly outperforms it (Table 5). Hence, To ensure
                                                                           accuracy and efficiency, we fuse RGB and depth features
                                                                           at the coarsest level.
                                                                               Saved time for RGB-D fusion. In MobileSal, we conduct
                                                                           RGB and depth information fusion only at the coarsest level.
                                                                           Conducting RGB-D feature fusion of all levels will result in
                                                                           260fps for our method. Hence, we will save 42% (1 − 260    450 )
                                                                           time. In other words, fusing only the coarsest will speed up
                                                                                                  450
    Image         Depth          IDR        Depth (1/8) Depth (1/32)       our method by 73% ( 260    − 1).
                                                                               Depth restoration quality. We explore the restored depth
Figure 5. Visual comparisons of restored depth maps by IDR with
different scales of input depth maps. Results of the last 3 columns        quality of IDR with the widely-used PSNR and SSIM [65]
have been upsampled with bilinear interpolation to match the size of the   metrics. The scale of the restored depth map in IDR is 1/16 of
input depth map.                                                           the input depth map. For comparison, we evaluate the quality
                                                                           of the nearest and bilinear interpolation of the input depth
                                                                           map of 1/8 scale. As the IDR branch receives depth features
                                                                           of the 1/32 scale, we also report the quality of the bilinear
provided, otherwise they are computed by their released                    interpolation of depth GT with the 1/32 scale. Results are
models.                                                                    shown in Table 3. We observe that the restored depth map is
   Quantitative comparison. Table 1 shows the results.                     closer to the input depth map than the upsampled 1/32 GT.
Our method runs at 450fps and only has 6.5M parameters.                    We also conduct visual comparisons of the above settings in
Other methods are much slower and heavier than our                         Fig. 5. One can see that the restored depth maps from IDR
method. For example, JLDCF [14] is 50× slower and has                      keep good restoration quality and are with less noise than
20× more parameters. UCNet is 26× slower and has 5.5×                      the upsampled 1/8 GT.
more parameters. Besides, our method outperforms other                         Loss selection in IDR. As introduced in §3.3, instead of
methods on NJU2K [15] and DUTLF-D [9] datasets, and                        using the trivial L1/L2 loss, the SSIM metric [65] is chosen
ranks from 3rd to 5th on the other 4 datasets. The above                   as the loss of IDR. We validate this design via training
results demonstrate the high efficiency and accuracy of our                our MobileSal with L1/L2/SSIM loss. We find that IDR
method.                                                                    with the L1/L2 loss can enhance MobileSal by 0.5%/0.7%
                                                                           in terms of the Fβmax , and is 0.5%/0.3% lower than IDR
   Qualitative comparison. Fig. 4 shows the results. Due to                with the SSIM loss. This is because SSIM loss provides the
the limited space, here we only compare our method with                    structural similarity rather than the simple point-to-point
CPFP [8], JLDCF [14], S2MA [22], and UCNet [11] on all                     error computed by the L1/L2 loss. Based on the above
involved datasets. Our method can work well on several                     discussion, we choose the SSIM loss as the supervision of
kinds of complex scenarios with noisy depth information,                   IDR.
while others may fail in such scenarios.
                                                                               The λ coefficient in the loss function. λ decides the loss
    CPU inference time. We test the inference time for                     weight of the depth restoration loss, as described in Eq. (11).
different methods in a single core of Intel i7 8700K@3.7GHz                We conduct experiments on our method with different λ
CPU. The results are shown in Table 2. While the inference                 settings. The results are shown in Table 6. The IDR branch
time of other state-of-the-art methods (677 ∼ 7246 ms) is far              brings substantial improvement to the robustness of our
from the bar of real-time speed (∼50 ms), the CPU inference                method with different λ. Since the third column achieves the
time of our method can achieve a real-time speed of 43 ms                  best performance, we adopt λ = 0.3 as the default setting for
for each RGB-D input.                                                      training our network.
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                                                   8

                              Table 6                                                                    Table 9
             Ablation study for λ coefficient selection.                Analysis of the fusion of CMF in Eq. (3). No. 1: trivial RGB-D fusion
                                                                        via element-wise multiplication; No. 2-3: variants of removing v or T in
   No.        1         2          3         4        5        6                          Eq. (3); No. 4: the default design.
     λ        0        0.1        0.3       0.5      1.0      2.0
   Fβmax    0.896     0.902      0.906     0.902    0.903    0.902            No.       Depth      CMF       v      T       Fβmax      MAE
   MAE      0.047     0.046      0.045     0.046    0.044    0.046             1         4                                  0.894      0.048
                                                                               2         4          4       4               0.895      0.049
                                                                               3         4          4               4       0.902      0.046
                               Table 7
                                                                               4         4          4       4       4       0.906      0.045
Efficacy of CMF. “RGB” denotes the RGB backbone with the RGB input.
 “Depth” indicates the network with the depth stream and depth input.
                                                                                                        Table 10
    No.     RGB      CPR      Depth       CMF      Fβmax    MAE          Ablation study for the dilation rates of CPR. “D Rates” means the
     1       4                                     0.852    0.068               dilation rates of each depthwise separable convolution.
     2       4        4                            0.887    0.052
     3       4        4          4                 0.894    0.048              No.          1        2       3        4         5         6
     4       4        4          4         4       0.906    0.045             D Rates    1, 2, 3     1       2        3      1, 3, 6   1, 4, 8
                                                                               Fβmax     0.906     0.900   0.892    0.897    0.903     0.901
                                                                               MAE       0.045     0.047   0.048    0.047    0.046     0.048
                               Table 8
Comparison of different operations for the initial RGB-D fusion in
     Eq. (1). “Multiplication” and “Addition” operations are
 element-wise. Concatenation operation is along channels. The           combinations of dilation rates (No. 5, 6). The default setting
    results of the default fusion strategy are with bold fonts.         with compact dilation rates (1, 2, 3) significantly outperforms
                                                                        other settings, demonstrating the efficacy of CPR.
  Operation     Multiplication         Addition    Concatenation           Hybrid loss. To validate the effectiveness of the Dice loss,
  Metric        Fβmax    MAE         Fβmax MAE     Fβmax   MAE
                                                                        we test the performance only trained with the binary cross-
  Results       0.906    0.045       0.897 0.048   0.900   0.046        entropy loss. We find that adding Dice loss supervision will
                                                                        improve the MAE performance by 0.1% ∼ 0.2% via providing
                                                                        high contrast, but will not affect the performance of Fβmax .
    Depth information and the CMF module. The results in
Table 7 demonstrate the effects of depth information and the
CMF module. Results with depth input are trained with the               4.4     Application of IDR to other tasks
IDR branch. The providence of depth maps without the CMF                Our proposed IDR freely strengthens the feature represen-
module only uses an element-wise multiplication for RGB-D               tations of the backbone network, given the RGB-D input
fusion. The results show that the depth information is very             in the inference stage. It is unbound to RGB-D SOD that
helpful for RGB-D SOD even with a very simple operation.                is a segmentation task aiming at deriving a saliency map.
More specifically, we also observe substantial improvement              To show the potential of IDR on other tasks, we evaluate
with the CMF module.                                                    the performance gain of IDR in the RGB-D semantic seg-
    Operation for initial RGB-D fusion in the CMF mod-                  mentation. The goal of this task, i.e., assigning each pixel
ule. As formulated in Eq. (1), an element-wise multiplication           with semantic labels, is similar to RGB-D SOD that predicts
is applied to the initial RGB-D fusion. To validate the                 saliency probability of each pixel.
effectiveness of the selected operation, we compare this                    Experimental setup. We select two recent state-of-the-
design with the widely-used element-wise addition. The                  art representatives [78], [79] as the baselines. We use the
results are presented in Table 8. Element-wise multiplication           official code provided by the authors to implement our ideas.
largely outperforms element-wise addition and concatena-                Following [78], [79], we conduct our experiments on the
tion by 0.9% and 0.6% in terms of the maximum F-measure,                NYUDv2 dataset [80], which consists of 1449 RGB images
suggesting the superiority of element-wise multiplication in            with corresponding depth maps and pixel-level semantic
the initial RGB-D fusion of the CMF module.                             labels containing 40 semantic classes. This dataset has 795
    Final fusion strategy of the CMF module. As described               and 654 images for training and testing, respectively. The
in Eq. (3), both the RGB attention vector v and RGB-D                   training and testing settings follow the official papers [78],
feature T join the fusion with depth feature D5 . We validate           [79]. Similar to MobileSal, for [79], RGB features re-calibrated
the effectiveness of the above design via removing v or T .             by the depth features for each stage are fed into the IDR
Experimental results are shown in Table 9. We observe a large           branch. However, for [78], different from MobileSal, the
performance degradation after removing T . This is because              output features of the first four stages are the input of the
in the feature fusion of Eq. (3), only T contains spatial-wise          IDR branch because the features of the last stage in [78] are
RGB features. Besides, v is an attention vector obtained by             directly used for the prediction of semantic segmentation.
RGB features, and D5 is the pure depth feature. Removing                    Evaluation metrics. Following [78], [79], mean IoU
v also affects the performance a bit because it provides the            (mIoU), is used as the primary evaluation metric. We also
channel-wise RGB attention in the RGB-D fusion.                         report the results of pixel accuracy (Acc) and mean accuracy
    Compact pyramid refinement. Table 10 shows the results              (mAcc) for reference. Please refer to [78] for more details
for CPR, where different dilation strategies are used. We test          about the computation of the above three metrics.
the default setting (No. 1), single convolution with different              Experimental results. We show the results in Table 11.
dilation rates (No. 2 - 4), and convolutions with sparse                With the computationally-free IDR incorporated, we observe
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                                                          9

                               Table 11                                        [8]  J. Zhao, Y. Cao, D.-P. Fan, X.-Y. Li, L. Zhang, and M.-M. Cheng,
 Effect of IDR for the methods of RGB-D semantic segmentation.                      “Contrast prior and fluid pyramid integration for RGBD salient
       Higher values of all metrics indicate better performance.                    object detection,” in IEEE Conf. Comput. Vis. Pattern Recog., 2019,
                                                                                    pp. 3927–3936.
      Method              SGNet [78]                Chen et al. [79]           [9] Y. Piao, W. Ji, J. Li, M. Zhang, and H. Lu, “Depth-induced multi-
      Metrics (%)   mIoU       Acc mAcc        mIoU        Acc mAcc                 scale recurrent attention network for saliency detection,” in Int.
                                                                                    Conf. Comput. Vis., 2019, pp. 7254–7263.
      Baseline      49.6       75.6 61.9       51.4        77.1 62.9
                                                                               [10] D.-P. Fan, Z. Lin, Z. Zhang, M. Zhu, and M.-M. Cheng, “Rethinking
      + IDR         50.5(+0.9) 76.3 62.2       52.2(+0.8) 77.3 64.0
                                                                                    rgb-d salient object detection: Models, data sets, and large-scale
                                                                                    benchmarks,” IEEE Trans. Neur. Net. Learn. Syst., vol. 32, no. 5, pp.
                                                                                    2075–2089, 2020.
that the performance of both methods [78], [79] has a large                    [11] J. Zhang, D.-P. Fan, Y. Dai, S. Anwar, F. Saleh, S. Aliakbarian, and
                                                                                    N. Barnes, “Uncertainty inspired RGB-D saliency detection,” IEEE
improvement in terms of the mIoU metric. This suggests that                         Trans. Pattern Anal. Mach. Intell., 2021.
the idea of IDR is also applicable and powerful for RGB-D                      [12] X. Zhao, L. Zhang, Y. Pang, H. Lu, and L. Zhang, “A single stream
semantic segmentation without any extra inference cost.                             network for robust and real-time RGB-D salient object detection,”
                                                                                    in Eur. Conf. Comput. Vis., 2020, pp. 646–662.
                                                                               [13] C. Li, R. Cong, Y. Piao, Q. Xu, and C. C. Loy, “RGB-D salient object
                                                                                    detection with cross-modality modulation and selection,” in Eur.
5      C ONCLUSION                                                                  Conf. Comput. Vis., 2020, pp. 225–241.
We propose a new method, MobileSal, which aims at efficient                    [14] K. Fu, D.-P. Fan, G.-P. Ji, Q. Zhao, J. Shen, and C. Zhu, “Siamese
                                                                                    network for RGB-D salient object detection and beyond,” IEEE
RGB-D SOD. Unlike other accurate RGB-D SOD methods,
                                                                                    Trans. Pattern Anal. Mach. Intell., 2021.
we are the first to shed light upon efficient RGB-D SOD by                     [15] R. Ju, L. Ge, W. Geng, T. Ren, and G. Wu, “Depth saliency based on
proposing an extremely efficient network MobileSal with a                           anisotropic center-surround difference,” in Int. Conf. Image Process.,
speed of 450fps. With less powerful features provided by the                        2014, pp. 1115–1119.
mobile backbone network, we propose the implicit depth                         [16] A. G. Howard, M. Zhu, B. Chen, D. Kalenichenko, W. Wang,
                                                                                    T. Weyand, M. Andreetto, and H. Adam, “MobileNets: Efficient
restoration (IDR) technique to strengthen the less powerful                         convolutional neural networks for mobile vision applications,”
features learned by mobile backbone networks. We perform                            arXiv preprint arXiv:1704.04861, 2017.
ablation study for the proposed techniques in MobileSal and                    [17] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen,
                                                                                    “MobileNetV2: Inverted residuals and linear bottlenecks,” in IEEE
demonstrate their effectiveness. We conduct experimental
                                                                                    Conf. Comput. Vis. Pattern Recog., 2018, pp. 4510–4520.
comparisons with state-of-the-art methods on six popular                       [18] X. Zhang, X. Zhou, M. Lin, and J. Sun, “ShuffleNet: An extremely
benchmarks. The results show that MobileSal performs favor-                         efficient convolutional neural network for mobile devices,” in IEEE
ably against state-of-the-art methods, with fewer parameters                        Conf. Comput. Vis. Pattern Recog., 2018, pp. 6848–6856.
and much faster speed. In terms of CPU inference time, our                     [19] N. Ma, X. Zhang, H.-T. Zheng, and J. Sun, “ShuffleNet v2: Practical
                                                                                    guidelines for efficient cnn architecture design,” in Eur. Conf.
method is 15∼150× faster. Our method can serve as a strong                          Comput. Vis., 2018, pp. 116–131.
baseline for future efficient RGB-D SOD research. For future                   [20] K. Simonyan and A. Zisserman, “Very deep convolutional networks
research, we plan to extend our work via pyramid pooling                            for large-scale image recognition,” in Int. Conf. Learn. Represent.,
                                                                                    2015.
transformer [81] for better performance.
                                                                               [21] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for
                                                                                    image recognition,” in IEEE Conf. Comput. Vis. Pattern Recog., 2016,
                                                                                    pp. 770–778.
6      ACKNOWLEDGMENT                                                          [22] N. Liu, N. Zhang, and J. Han, “Learning selective self-mutual
                                                                                    attention for RGB-D saliency detection,” in IEEE Conf. Comput. Vis.
This project is supported by the National Key Re-                                   Pattern Recog., 2020, pp. 13 756–13 765.
search and Development Program of China (Grant No.                             [23] Q. Hou, M.-M. Cheng, X. Hu, A. Borji, Z. Tu, and P. H. Torr, “Deeply
2018AAA0100400) and NSFC (NO. 61922046).                                            supervised salient object detection with short connections.” IEEE
                                                                                    Trans. Pattern Anal. Mach. Intell., vol. 41, no. 4, p. 815, 2019.
                                                                               [24] X. Qin, Z. Zhang, C. Huang, C. Gao, M. Dehghan, and M. Jagersand,
                                                                                    “BASNet: Boundary-aware salient object detection,” in IEEE Conf.
R EFERENCES                                                                         Comput. Vis. Pattern Recog., 2019, pp. 7479–7489.
[1]    S. Hong, T. You, S. Kwak, and B. Han, “Online tracking by learning      [25] J.-J. Liu, Q. Hou, M.-M. Cheng, J. Feng, and J. Jiang, “A simple
       discriminative saliency map with convolutional neural network,”              pooling-based design for real-time salient object detection,” in IEEE
       in Int. Conf. Mach. Learn., 2015, pp. 597–606.                               Conf. Comput. Vis. Pattern Recog., 2019, pp. 3917–3926.
[2]    W. Wang, J. Shen, and H. Ling, “A deep network solution for             [26] P. Zhang, W. Liu, H. Lu, and C. Shen, “Salient object detection with
       attention and aesthetics aware photo cropping,” IEEE Trans. Pattern          lossless feature reflection and weighted structural loss,” IEEE Trans.
       Anal. Mach. Intell., vol. 41, no. 7, pp. 1531–1544, 2018.                    Image Process., vol. 28, no. 6, pp. 3048–3060, 2019.
[3]    Y. Liu, Y.-H. Wu, P.-S. Wen, Y.-J. Shi, Y. Qiu, and M.-M. Cheng,        [27] Y.-H. Wu, Y. Liu, L. Zhang, W. Gao, and M.-M. Cheng, “Regu-
       “Leveraging instance-, image-and dataset-level information for               larized densely-connected pyramid network for salient instance
       weakly supervised instance segmentation,” IEEE Trans. Pattern                segmentation,” IEEE Trans. Image Process., vol. 30, pp. 3897–3907,
       Anal. Mach. Intell., 2020.                                                   2021.
[4]    P. Zhang, D. Wang, H. Lu, H. Wang, and X. Ruan, “Amulet:                [28] Y.-H. Wu, Y. Liu, L. Zhang, M.-M. Cheng, and B. Ren, “EDN:
       Aggregating multi-level convolutional features for salient object            Salient object detection via extremely-downsampled network,”
       detection,” in Int. Conf. Comput. Vis., 2017, pp. 202–211.                   arXiv preprint arXiv:2012.13093, 2021.
[5]    Y. Pang, X. Zhao, L. Zhang, and H. Lu, “Multi-scale interactive         [29] C. Yang, L. Zhang, H. Lu, X. Ruan, and M.-H. Yang, “Saliency
       network for salient object detection,” in IEEE Conf. Comput. Vis.            detection via graph-based manifold ranking,” in IEEE Conf. Comput.
       Pattern Recog., 2020, pp. 9413–9422.                                         Vis. Pattern Recog., 2013, pp. 3166–3173.
[6]    X. Zhao, Y. Pang, L. Zhang, H. Lu, and L. Zhang, “Suppress and          [30] M.-M. Cheng, J. Warrell, W.-Y. Lin, S. Zheng, V. Vineet, and
       balance: A simple gated network for salient object detection,” in            N. Crook, “Efficient salient region detection with soft image
       Eur. Conf. Comput. Vis., 2020, pp. 35–51.                                    abstraction,” in Int. Conf. Comput. Vis., 2013, pp. 1529–1536.
[7]    H. Chen and Y. Li, “Three-stream attention-aware network for            [31] M.-M. Cheng, N. J. Mitra, X. Huang, P. H. Torr, and S.-M. Hu,
       RGB-D salient object detection,” IEEE Trans. Image Process., vol. 28,        “Global contrast based salient region detection,” IEEE Trans. Pattern
       no. 6, pp. 2825–2835, 2019.                                                  Anal. Mach. Intell., vol. 37, no. 3, pp. 569–582, 2014.
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                                                          10

[32] J. Wang, H. Jiang, Z. Yuan, M.-M. Cheng, X. Hu, and N. Zheng,             [57] M. Tan, B. Chen, R. Pang, V. Vasudevan, M. Sandler, A. Howard,
     “Salient object detection: A discriminative regional feature integra-          and Q. V. Le, “MnasNet: Platform-aware neural architecture search
     tion approach,” Int. J. Comput. Vis., vol. 123, no. 2, pp. 251–268,            for mobile,” in IEEE Conf. Comput. Vis. Pattern Recog., 2019, pp.
     2017.                                                                          2820–2828.
[33] X. Li, H. Lu, L. Zhang, X. Ruan, and M.-H. Yang, “Saliency detection      [58] S. Mehta, M. Rastegari, L. Shapiro, and H. Hajishirzi, “ESPNetv2:
     via dense and sparse reconstruction,” in Int. Conf. Comput. Vis., 2013,        A light-weight, power efficient, and general purpose convolutional
     pp. 2976–2983.                                                                 neural network,” in IEEE Conf. Comput. Vis. Pattern Recog., 2019, pp.
[34] L. Zhang, J. Ai, B. Jiang, H. Lu, and X. Li, “Saliency detection via           9190–9200.
     absorbing markov chain with learnt transition probability,” IEEE          [59] M. Tan, R. Pang, and Q. V. Le, “EfficientDet: Scalable and efficient
     Trans. Image Process., vol. 27, no. 2, pp. 987–998, 2017.                      object detection,” in IEEE Conf. Comput. Vis. Pattern Recog., 2020,
[35] R. Wu, M. Feng, W. Guan, D. Wang, H. Lu, and E. Ding, “A mutual                pp. 10 781–10 790.
     learning method for salient object detection with intertwined multi-      [60] Y. Liu, Y.-C. Gu, X.-Y. Zhang, W. Wang, and M.-M. Cheng,
     supervision,” in IEEE Conf. Comput. Vis. Pattern Recog., 2019, pp.             “Lightweight salient object detection via hierarchical visual percep-
     8150–8159.                                                                     tion learning,” IEEE Trans. Cybernetics, vol. 51, no. 9, pp. 4439–4449,
[36] Y. Liu, D. Zhang, Q. Zhang, and J. Han, “Part-object relational                2021.
     visual saliency,” IEEE Trans. Pattern Anal. Mach. Intell., 2021.          [61] Y. Liu, X.-Y. Zhang, J.-W. Bian, L. Zhang, and M.-M. Cheng, “SAM-
[37] J. Han, D. Zhang, G. Cheng, N. Liu, and D. Xu, “Advanced                       Net: Stereoscopically attentive multi-scale network for lightweight
     deep-learning techniques for salient and category-specific object              salient object detection,” IEEE Trans. Image Process., vol. 30, pp.
     detection: a survey,” IEEE Signal Processing Magazine, vol. 35, no. 1,         3804–3814, 2021.
     pp. 84–100, 2018.                                                         [62] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep
[38] A. Borji, M.-M. Cheng, Q. Hou, H. Jiang, and J. Li, “Salient object            network training by reducing internal covariate shift,” in Int. Conf.
     detection: A survey,” Computational Visual Media, vol. 5, no. 2, pp.           Mach. Learn., 2015, pp. 448–456.
     117–150, 2019.                                                            [63] V. Nair and G. E. Hinton, “Rectified linear units improve restricted
[39] W. Wang, Q. Lai, H. Fu, J. Shen, H. Ling, and R. Yang, “Salient                boltzmann machines,” in Int. Conf. Mach. Learn. Madison, WI,
     object detection in the deep learning era: An in-depth survey,” IEEE           USA: Omnipress, 2010, pp. 807–814.
     Trans. Pattern Anal. Mach. Intell., 2021.                                 [64] Y.-H. Wu, S.-H. Gao, J. Mei, J. Xu, D.-P. Fan, R.-G. Zhang, and M.-M.
[40] C. Lang, T. V. Nguyen, H. Katti, K. Yadati, M. Kankanhalli, and                Cheng, “JCS: An explainable covid-19 diagnosis system by joint
     S. Yan, “Depth matters: Influence of depth cues on visual saliency,”           classification and segmentation,” IEEE Trans. Image Process., vol. 30,
     in Eur. Conf. Comput. Vis., 2012, pp. 101–115.                                 pp. 3113–3126, 2021.
[41] J. R. Arridhana Ciptadi, Tucker Hermans, “An in depth view of             [65] Z. Wang, A. C. Bovik, H. R. Sheikh, and E. P. Simoncelli, “Image
     saliency,” in Proceedings of the British Machine Vision Conference.            quality assessment: from error visibility to structural similarity,”
     BMVA Press, 2013.                                                              IEEE Trans. Image Process., vol. 13, no. 4, pp. 600–612, 2004.
[42] K. Desingh, K. M. Krishna, D. Rajan, and C. Jawahar, “Depth really        [66] F. Milletari, N. Navab, and S.-A. Ahmadi, “V-Net: Fully convolu-
     matters: Improving visual salient region detection with depth,” in             tional neural networks for volumetric medical image segmentation,”
     Proceedings of the British Machine Vision Conference. BMVA Press,              in 2016 fourth international conference on 3D vision (3DV). IEEE,
     2013.                                                                          2016, pp. 565–571.
[43] X. Fan, Z. Liu, and G. Sun, “Salient region detection for stereoscopic
                                                                               [67] R. Cong, J. Lei, C. Zhang, Q. Huang, X. Cao, and C. Hou, “Saliency
     images,” in International Conference on Digital Signal Processing.
                                                                                    detection for stereoscopic images based on depth confidence
     IEEE, 2014, pp. 454–458.
                                                                                    analysis and multiple cues fusion,” IEEE Signal Processing Letters,
[44] H. Peng, B. Li, W. Xiong, W. Hu, and R. Ji, “RGBD salient object
                                                                                    vol. 23, no. 6, pp. 819–823, 2016.
     detection: a benchmark and algorithms,” in Eur. Conf. Comput. Vis.,
                                                                               [68] H. Chen and Y. Li, “Progressively complementarity-aware fusion
     2014, pp. 92–109.
                                                                                    network for RGB-D salient object detection,” in IEEE Conf. Comput.
[45] Y. Cheng, H. Fu, X. Wei, J. Xiao, and X. Cao, “Depth enhanced
                                                                                    Vis. Pattern Recog., 2018, pp. 3051–3060.
     saliency detection method,” in International Conference on Internet
     Multimedia Computing and Service, 2014, pp. 23–27.                        [69] Z. Zhang, Z. Lin, J. Xu, W.-D. Jin, S.-P. Lu, and D.-P. Fan, “Bilateral
[46] Y. Pang, L. Zhang, X. Zhao, and H. Lu, “Hierarchical dynamic                   attention network for rgb-d salient object detection,” IEEE Trans.
     filtering network for RGB-D salient object detection,” in Eur. Conf.           Image Process., vol. 30, pp. 1949–1961, 2021.
     Comput. Vis., 2020, pp. 235–252.                                          [70] A. Paszke, S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan,
[47] X. Zhao, Y. Pang, L. Zhang, H. Lu, and X. Ruan, “Self-supervised               T. Killeen, Z. Lin, N. Gimelshein, L. Antiga et al., “PyTorch: An
     representation learning for RGB-D salient object detection,” arXiv             imperative style, high-performance deep learning library,” in Annu.
     preprint arXiv:2101.12482, 2021.                                               Conf. Neur. Inform. Process. Syst. Curran Associates, Inc., 2019, pp.
[48] S. Chen and Y. Fu, “Progressively guided alternate refinement                  8026–8037.
     network for RGB-D salient object detection,” in Eur. Conf. Comput.        [71] S.-M. Hu, D. Liang, G.-Y. Yang, G.-W. Yang, and W.-Y. Zhou, “Jittor:
     Vis., 2020, pp. 520–538.                                                       a novel deep learning framework with meta-operators and unified
[49] N. Huang, Y. Liu, Q. Zhang, and J. Han, “Joint cross-modal and                 graph execution,” Science China Information Sciences, vol. 63, no. 12,
     unimodal features for RGB-D salient object detection,” IEEE Trans.             pp. 1–21, 2020.
     Multimedia, vol. 23, pp. 2428–2441, 2021.                                 [72] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimiza-
[50] L. Qu, S. He, J. Zhang, J. Tian, Y. Tang, and Q. Yang, “RGBD salient           tion,” in Int. Conf. Learn. Represent., 2015.
     object detection via deep fusion,” IEEE Trans. Image Process., vol. 26,   [73] Y. Niu, Y. Geng, X. Li, and F. Liu, “Leveraging stereopsis for saliency
     no. 5, pp. 2274–2285, 2017.                                                    analysis,” in IEEE Conf. Comput. Vis. Pattern Recog. IEEE, 2012, pp.
[51] Q. Chen, Z. Liu, Y. Zhang, K. Fu, Q. Zhao, and H. Du, “RGB-D                   454–461.
     salient object detection via 3d convolutional neural networks,” in        [74] C. Zhu and G. Li, “A three-pathway psychobiological framework
     AAAI Conf. Artif. Intell., 2021.                                               of salient object detection using stereoscopic technology,” in Int.
[52] W. Ji, J. Li, S. Yu, M. Zhang, Y. Piao, S. Yao, Q. Bi, K. Ma, Y. Zheng,        Conf. Comput. Vis. Worksh., 2017, pp. 3008–3014.
     H. Lu et al., “Calibrated rgb-d salient object detection,” in IEEE        [75] R. Achanta, S. Hemami, F. Estrada, and S. Susstrunk, “Frequency-
     Conf. Comput. Vis. Pattern Recog., 2021, pp. 9471–9481.                        tuned salient region detection,” in IEEE Conf. Comput. Vis. Pattern
[53] T. Zhou, D.-P. Fan, M.-M. Cheng, J. Shen, and L. Shao, “RGB-D                  Recog., 2009, pp. 1597–1604.
     salient object detection: A survey,” Computational Visual Media, pp.      [76] D.-P. Fan, M.-M. Cheng, Y. Liu, T. Li, and A. Borji, “Structure-
     1–33, 2021.                                                                    measure: A new way to evaluate foreground maps,” in Int. Conf.
[54] J. Han, H. Chen, N. Liu, C. Yan, and X. Li, “CNNs-based RGB-D                  Comput. Vis., 2017, pp. 4548–4557.
     saliency detection via cross-view transfer and multiview fusion,”         [77] D.-P. Fan, G.-P. Ji, X. Qin, and M.-M. Cheng, “Cognitive vision
     IEEE Trans. Cybernetics, vol. 48, no. 11, pp. 3171–3183, 2017.                 inspired object segmentation metric and loss function,” SCIENTIA
[55] N. Wang and X. Gong, “Adaptive fusion for RGB-D salient object                 SINICA Informationis, vol. 6, 2021.
     detection,” IEEE Access, vol. 7, pp. 55 277–55 284, 2019.                 [78] L.-Z. Chen, Z. Lin, Z. Wang, Y.-L. Yang, and M.-M. Cheng, “Spatial
[56] N. Huang, Y. Yang, D. Zhang, Q. Zhang, and J. Han, “Employing                  information guided convolution for real-time RGBD semantic
     bilinear fusion and saliency prior information for RGB-D salient               segmentation,” IEEE Trans. Image Process., vol. 30, pp. 2313–2324,
     object detection,” IEEE Trans. Multimedia, 2021.                               2021.
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE                                                              11

[79] X. Chen, K.-Y. Lin, J. Wang, W. Wu, C. Qian, H. Li, and G. Zeng,       Yu-Chao Gu received his bachelor’s degree from
     “Bi-directional cross-modality feature propagation with separation-    the Beijing University of Chemical Technology
     and-aggregation gate for RGB-D semantic segmentation,” in Eur.         in 2019. He is currently pursuing the master’s
     Conf. Comput. Vis., 2020, pp. 561–577.                                 degree with the College of Computer Science,
[80] N. Silberman, D. Hoiem, P. Kohli, and R. Fergus, “Indoor segmen-       Nankai University. His research interests include
     tation and support inference from RGBD images,” in Eur. Conf.          efficient deep-learning and computer vision.
     Comput. Vis., 2012, pp. 746–760.
[81] Y.-H. Wu, Y. Liu, X. Zhan, and M.-M. Cheng, “P2T: Pyramid
     pooling transformer for scene understanding,” arXiv preprint
     arXiv:2106.12011, 2021.

                                                                            Ming-Ming Cheng received his PhD degree from
                                                                            Tsinghua University in 2012. Then he did two
                       Yu-Huan Wu is currently a Ph.D. candidate with
                                                                            years research fellow with Prof. Philip Torr in Ox-
                       College of Computer Science at Nankai Uni-
                                                                            ford. He is now a professor at Nankai University,
                       versity, supervised by Prof. Ming-Ming Cheng.
                                                                            leading the Media Computing Lab. His research
                       He received his bachelor’s degree from Xidian
                                                                            interests include computer graphics, computer
                       University in 2018. His research interests include
                                                                            vision, and image processing. He received re-
                       computer vision and machine learning.
                                                                            search awards, including ACM China Rising Star
                                                                            Award, IBM Global SUR Award, and CCF-Intel
                                                                            Young Faculty Researcher Program. He is on the
                                                                            editorial boards of IEEE TPAMI and IEEE TIP.

                       Yun Liu received his bachelor’s and doctoral
                       degrees from Nankai University in 2016 and 2020,
                       respectively. Currently, he works as a postdoc-
                       toral scholar with Prof. Luc Van Gool at ETH
                       Zurich. His research interests include computer
                       vision and machine learning.

                       Jun Xu received his B.Sc. and M.Sc. degrees
                       from School of Mathematics Science, Nankai
                       University, Tianjin, China, in 2011 and 2014,
                       respectively, and the Ph.D. degree from the De-
                       partment of Computing, Hong Kong Polytechnic
                       University, in 2018. He worked as a Research
                       Scientist at IIAI, Abu Dhabi, UAE. He is currently
                       a Lecturer with School of Statistics and Data
                       Science, Nankai University. More information can
                       be found at https://csjunxu.github.io/.

                       Jia-Wang Bian Jia-Wang Bian received the
                       B.Eng. degree from Nankai University, where he
                       was advised by Prof. M.-M. Cheng. He is currently
                       pursuing the Ph.D. degree with The University of
                       Adelaide. He was a Research Assistant with the
                       Singapore University of Technology and Design
                       (SUTD). He also did a Trainee Engineer Job with
                       the Advanced Digital Sciences Center (ADSC),
                       Huawei Technologies Co., Ltd., and Tusimple. He
                       is also an Associated Ph.D. Researcher with the
                       Australian Centre for Robotic Vision (ACRV). He
is advised by Prof. I. Reid and Prof. C. Shen. His research interests
include computer vision and robotics.
