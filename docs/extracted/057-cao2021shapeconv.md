---
source_id: 057
bibtex_key: cao2021shapeconv
title: ShapeConv: Shape-aware Convolutional Layer for Indoor RGB-D Semantic Segmentation
year: 2021
domain_theme: Segmentasi RGB-D
verified_pdf: 57_ShapeConv.pdf
char_count: 68389
---

ShapeConv: Shape-aware Convolutional Layer
                                                                       for Indoor RGB-D Semantic Segmentation

                                          Jinming Cao1 Hanchao Leng1 Dani Lischinski2 Danny Cohen-Or3 Changhe Tu1 * Yangyan Li4∗
                                                     1                                  2
                                                       Shandong University, China         The Hebrew University of Jerusalem, Israel
                                                                3                                4
                                                                  Tel Aviv University, Israel      Alibaba Group, China
arXiv:2108.10528v1 [cs.CV] 24 Aug 2021

                                                  {jinming.ccao, hanchao.leng, danix3d, cohenor, changhe.tu, yangyan.lee}@gmail.com

                                                                    Abstract

                                             RGB-D semantic segmentation has attracted increasing
                                         attention over the past few years. Existing methods mostly
                                         employ homogeneous convolution operators to consume the
                                         RGB and depth features, ignoring their intrinsic differences.
                                         In fact, the RGB values capture the photometric appearance
                                         properties in the projected image space, while the depth fea-
                                         ture encodes both the shape of a local geometry as well as
                                         the base (whereabout) of it in a larger context. Compared                            ℙ!                             ℙ!
                                                                                                                                        ℙ"                             ℙ"
                                         with the base, the shape probably is more inherent and has
                                         a stronger connection to the semantics, and thus is more                        ℙ#                             ℙ#
                                                                                                                                   ℙ$                             ℙ$
                                         critical for segmentation accuracy. Inspired by this obser-
                                         vation, we introduce a Shape-aware Convolutional layer
                                                                                                                       !"#                             $%&'ℎ
                                         (ShapeConv) for processing the depth feature, where the         Figure 1. Visual demonstration of why the shape of an RGB-D im-
                                         depth feature is firstly decomposed into a shape-component      age matters. Regarding the images on the top, lines with the same
                                         and a base-component, next two learnable weights are in-        color share a same shape, yet with different base. The correspond-
                                         troduced to cooperate with them independently, and finally      ing patches are shown on the bottom.
                                         a convolution is applied on the re-weighted combination
                                         of these two components. ShapeConv is model-agnostic
                                         and can be easily integrated into most CNNs to replace          1. Introduction
                                         vanilla convolutional layers for semantic segmentation. Ex-         With the widespread use of depth sensors (such as Mi-
                                         tensive experiments on three challenging indoor RGB-D se-       crosoft Kinect [31]), the availability of RGB-D data has
                                         mantic segmentation benchmarks, i.e., NYU-Dv2(-13,-40),         boosted the advancement of RGB-D semantic segmenta-
                                         SUN RGB-D, and SID, demonstrate the effectiveness of our        tion, which contributes to an indispensable task in the com-
                                         ShapeConv when employing it over five popular architec-         puter vision community. Thanks to the flourishing of Con-
                                         tures. Moreover, the performance of CNNs with ShapeConv         volutional Neural Networks (CNNs), recent studies mostly
                                         is boosted without introducing any computation and mem-         resort to CNNs for tackling this problem. Convolutional
                                         ory increase in the inference phase. The reason is that         layers, deemed as the core building blocks of CNNs, are
                                         the learnt weights for balancing the importance between         accordingly the key elements in RGB-D semantic segmen-
                                         the shape and base components in ShapeConv become con-          tation models [6, 13, 15, 17, 21].
                                         stants in the inference phase, and thus can be fused into the
                                                                                                             However, RGB and depth information are inherently dif-
                                         following convolution, resulting in a network that is identi-
                                                                                                         ferent from each other. In particular, RGB values capture
                                         cal to one with vanilla convolutional layers.
                                                                                                         the photometric appearance properties in the projected im-
                                                                                                         age space, while the depth feature encodes both the shape
                                                                                                         of a local geometry as well as the base (whereabout) of it in
                                                                                                         a larger context. As a result, the convolution operator that
                                           * Corresponding Author                                        is widely adopted for consuming RGB data might not be
the optimal for processing the depth data. Taking Figure 1                     we conduct extensive experiments on three challenging
as an example, we would expect the corresponding patches                       RGB-D indoor semantic segmentation benchmarks: NYU-
of the same chairs to have the same features, as they share                    Dv2 [25](-13,-40), SUN RGBD [26], and SID [1]. We ap-
the same shape. The shape is a more inherent property of                       ply our ShapeConv to five popular semantic segmentation
the underlying object and has stronger connection to the se-                   architectures and can observe promising performance im-
mantics. We would expect to achieve shape invariance in                        provements compared with baseline models. We found that
the learning process. When a vanilla convolution operator                      ShapeConv can significantly improve the segmentation ac-
is applied on these corresponding patches, the resulting fea-                  curacy around the object boundaries (see Figure 5), which
tures are different due to the differences in their base com-                  demonstrates the effective leveraging of the depth informa-
ponent, hindering the learning from achieving shape invari-                    tion2 .
ance. On the other hand, the base components cannot be
simply discarded for pursuing the shape invariance in the                      2. Related Work
current layer, as they form the shape in a followup layer                          CNNs have been widely used for semantic segmentation
with a larger context.                                                         on RGB images [3, 4, 19, 18, 23, 33]. In general, exist-
    To address these problems, we propose a Shape-aware                        ing segmentation architectures usually involve two stages:
Convlutional layer (ShapeConv), to learn the adaptive bal-                     the backbone and the segmentation stage. The former stage
ance between the importance of shape and base informa-                         is leveraged to extract features from RGB images, wherein
tion, giving the network the chance to focus more on the                       popular models are ResNet [12], ResNeXt [29] which are
shape information whenever necessary for benefiting the                        pre-trained on the ImageNet dataset [24]. The latter stage
RGB-D semantic segmentation task. We firstly decom-                            aims to generate predictions based on the extracted features.
pose a patch1 into two separate components, i.e., a base-                      Methods in this stage include Upsample [19], PPM [33] and
component and a shape-component. The mean of patch val-                        ASPP [3, 4], etc. It is worth noting that both stages adopt
ues depicts the whereabout of the patch in a larger context,                   the convolutional layers as the core building blocks.
thus constitutes the base component, while the residual is                         As RGB semantic segmentation has been extensively
the relative changes in the patch, which depicts the shape                     studied in literature, a straightforward solution for RGB-D
of the underlying geometry, thus constitutes to the shape                      semantic segmentation is to adapt the well-developed archi-
component. Specifically, for an input patch (such as P1 in                     tectures from the ones designed for RGB data. However,
Figure 1), the base describes where the patch is, i.e., the dis-               implementing such a idea is non-trivial due to the asym-
tance from the observation point; while the shape expresses                    metric modality problem between the RGB and the depth
what the patch is, e.g., a chair corner. We then employ two                    information. To tackle this, researchers have devoted ef-
operations, namely, base-product and shape-product, to re-                     forts into two directions: designing dedicated architectures
spectively process these two components with two learn-                        for RGB-D data [6, 8, 13, 15, 17, 21, 28], and presenting
able weights, i.e., base-kernel and shape-kernel. The output                   novel layers to enhance or replace the convolutional layers
from these two is then combined in an addition manner to                       in RGB semantic segmentation [5, 27, 30]. Our method falls
form a shape-aware patch, which is further convolved with                      into the second category.
a normal convolutional kernel. In contrast to the original                         Methods in the first category propose to feed RGB and
patch, the shape-aware one is capable of adaptively learn-                     depth channels to two parallel CNNs streams, where the
ing the shape characteristic with the shape-kernel, and the                    output features are fused with specific strategies. For ex-
base-kernel serves to balance the contributions of the shape                   ample, [6] presents a gate-fusion method, [8, 13, 21] fuse
and the base for the final prediction.                                         the features in multi-levels of the backbone stages. Never-
    In addition, since the base-kernel and shape-kernel be-                    theless, these methods mostly leverage separate networks to
come constants in the inference phase, we can fuse them                        consume RGB and depth features, they are yet faced with
into the following convolution kernel, resulting in a network                  two limitations: 1) it is hard to decide when is the best stage
that is identical to the one with vanilla convolutional layers.                for the fusion to happen; and 2) the two-stream or multi-
The proposed ShapeConv can be easily plugged into most                         level way often results in large increase of computation.
CNNs as a replacement of the vanilla convolution in seman-                         In contrast, methods along the second direction target at
tic segmentation without introducing any computation and                       designing novel layers based on the geometric character-
memory increase in the inference phase. This simple re-                        istics of RGB-D data, which are more flexible and time-
placement transforms CNNs designed for RGB data into                           efficient. For instance, Wang et al. [27] proposed the depth-
ones better suited for consuming RGB-D data.                                   aware convolution to weight pixels based on a hand-crafted
    To validate the effectiveness of the proposed method,                      Gaussian function by leveraging the depth similarity be-
                                                                               tween pixels. [30] presents a novel operator called mal-
   1 The operation unit of input features for the convolutional layer, whose

spatial size is the same as the convolution kernel.                              2 Our code is released through https://github.com/hanchaoleng/ShapeConv.
leable 2.5D convolution, to learn the receptive field along      ShapeConv Formulation. Based on the aforementioned
the depth-axis. [5] devises a S-Conv to infer the sampling       analysis, in this paper, we offer to decompose an input
offset of the convolution kernel guided by the 3D spatial        patch into two components: a base-component PB describ-
information, enabling the convolutional layer to adjust the      ing where the patch is, and a shape-component PS express-
receptive field and geometric transformations. ShapeConv         ing what the patch is. Therefore, we refer the mean3 of
proposed a novel view of the content in each patch and a         patch values to be PB , and its relative values to be as PS :
mechanism to leverage them adaptively with learnt weights.
Moreover, ShapeConv can be converted into vanilla convo-                                  PB = m(P),
lution in the inference phase, resulting in ZERO increase of                              PS = P − m(P),
memory and computation compared with the models with
vanilla convolution.                                             where m(P) is the mean function on P (over the Kh ×
                                                                 Kw dimensions), and PB ∈ R1×1×Cin , and PS ∈
3. Method                                                        RKh ×Kw ×Cin .
   In this section, we first provide the basic formulation           Note that directly convolved PS with K in Equation 1
of the Shape-aware convolutional layer (ShapeConv) for           is sub-optimal, as the values from PB contributes the class
RGB-D data, followed by its application in the training and      discrimination across patches. Thus, our ShapeConv in-
inference phase. We end this section with the method archi-      stead leverages two learnable weights, WB ∈ R1 and
tectures.                                                        WS ∈ RKh ×Kw ×Kh ×Kw ×Cin , to separately consume the
                                                                 above two components. The outputted features are then
3.1. ShapeConv for RGB-D Data
                                                                 combined in an element-wise addition manner, which forms
Method Intuition. Given an input patch P                 ∈       a new shape-aware patch with the same size as the original
RKh ×Kw ×Cin , Kh and Kw are the spatial dimen-                  one P. The formulation of ShapeConv is given as,
sions of the kernel; Cin represents the channel numbers in
the input feature map, the output features from the vanilla                   F = ShapeConv(K, WB , WS , P)
convolution layer are obtained by,                                              = Conv(K, WB  PB + WS ∗ PS )
                                                                                                                                      (2)
                      F = Conv(K, P),                     (1)                   = Conv(K, PB + PS )
                                                                                = Conv((K, PBS ),
where K ∈ RKh ×Kw ×Cin ×Cout denotes the learnable
                                                                 where  and ∗ denote the base-product and shape-product
weights of kernels in a convolutional layer (The bias terms
                                                                 operator, respectively, which are defined as,
are not included for simplicity.); Cout represents the chan-
nel numbers in the output feature map. Each element of
                                                                               (
                                                                                 PB = WB  PB
F ∈ RCout is calculated as,                                                                                          (3)
                                                                                 PB1,1,cin = WB × PB1,1,cin ,
                      Kh ×K
                          X w ×Cin                                 (
            Fcout =                  (Ki,cout × Pi ).                  PS = WS ∗ PS
                           i
                                                                                      PK ×K
                                                                       PSkh ,kw ,cin = i h w (WSi,kh ,kw ,cin × PSi,cin ),
    It can be easily recognized that F usually changes with                                                               (4)
respect to different values of P. Take the two patches in the    where cin , kh , kw are the indices of the elements in Cin ,
Figure 1, P1 and P2 , as an example. The corresponding out-      Kh , Kw dimensions, respectively.
put features, F1 and F2 from the vanilla convolution layer           We reconstruct the shape-aware patch PBS from the addi-
are learned by: F1 = Conv(K, P1 ), F2 = Conv(K, P2 ).            tion of PB and PS , and PBS ∈ RKh ×Kw ×Cin , which enables
Since P1 and P2 are not identical (different distances from      it to be smoothly convolved by the kernel K of vanilla con-
the observation points), accordingly, their features are usu-    volutional layer. Nevertheless, the PBS is equipped with the
ally different, and this may lead to distinct prediction re-     important shape information which is learned by the two
sults.                                                           additional weights, making the convolutional layer to focus
    Nevertheless, P1 and P2 , corresponding to the red re-       on the situations when merely using depth values fails.
gions in Figure 1, actually belong to the same class - chair.    3.2. ShapeConv in Training and Inference
And vanilla convolutional layers cannot well handle such         Training phase. The proposed ShapeConv in Sec-
situations. In fact, there exists some invariants of these       tion 3.1 can effective leverage the shape information of
two patches, namely, the shape. It refers to the relative
                                                                    3 As the depth values are obtained from a fixed observation point, we
depth correlation under local features, which is however,
                                                                 notice that the rotational transformations cannot be addressed due to the
unexpectedly ignored by the existing methods. In view of
                                                                 angle of view limitation. As a result, we focus more on the translational
this, we propose to fill this gap via effectively modeling the   transformations in this paper.
shape for RGB-D semantic segmentation.
                                                                                             In fact, the two formulations of ShpeConv, i.e., Equa-
                                                                                          tion 2 and Equation 5 are mathematically equivalent, i.e.,

                                                                                                        F = ShapeConv(K, WB , WS , P)
                        ℙ                       (         ℙ                   (
                                                                                                           = Conv(K, PBS )                                  (6)
                                    -                                7+,                                   = Conv(KBS , P),
                                                       ! = #ℎ%&'()*+(,, .! , ." , ℙ)
                             % ! = ()*+(,, ℙ)        6                                                           Kh ×K w ×Cin
                                                              =()*+(0#$ , ℙ)                                         X
                                                                                                      Fcout =                   (Ki,cout × PBSi )
                                                                                                                       i
                                  8 -                               6) 8 -                                                                                  (7)
                                                                                                                 Kh ×K w ×Cin
                                                    6)                                                               X
                                                                                                             =                  (KBSi,cout × Pi ),
                                                                      +                                                i

                        -                                                    7+,          please refer to the Supp. for detailed proof. In this way, we
                              -−8 -                                                       utilize the ShapeConv in Equation 5 in our implementation
                                                                     6* ∗ - − 8 -
                                                                                          as illustrated in Figure 2(b) and (c).
                                                                                          Inference phase. During inference, since the two addi-
                                                     6*
                                                                                          tional weights i.e. WB and WS , become constants, we can
                                 5 0#$ = .! 1 , + ." ∗ , − 1 ,
                                                                                          fuse them into KBS as shown in Figure 2(c) with KBS =
                  Figure 2. Comparison of vanilla convolution and ShapeConv               WB  KB + WS ∗ KS . And KBS shares the same tensor
!# = 2, %$% = 3, %&'( = 2
                  within a patch P. In this figure, Kh = Kw = 2, Cin = 3, and             size with K in Equation 1, thus, our ShapeConv is actually
                  Cout = 2, “+” denotes element-wise addition. (a) Vanilla convo-         the same as the vanilla convolutional layer in Figure 2(a).
                  lution with kernel K; (b) ShapeConv with folding the WB and WS
                                                                                          In other words, when replacing vanilla convolution with
                  into KBS ; (c) The computation of KBS from K, WB and WS .
                                                                                          ShapeConv, there would introduce zero additional inference
                                                                                          time.
                  patches. However, replacing vanilla convolutional layer                 3.3. ShapeConv-enhanced Network Architecture
                  with ShapeConv in CNNs introduces more computational
                  cost due to the two product operation in Equation 3 and 4.                  Different from devising specially dedicated architec-
                  To tackle this problem, we propose to shift these two oper-             tures for RGB-D segmentation [21, 22, 17], the proposed
                  ations from patches to kernels,                                         ShapeConv is a more generalized approach that can be eas-
                                                                                          ily plugged into most CNNs as a replacement for the vanilla
                                                                                          convolution in semantic segmentation, which is then trans-
                           (
                             KB = WB  KB
                                                                                          formed for adapting the RGB-D data.
                             KB1,1,cin ,cout = WB × KB1,1,cin ,cout ,
                                                                                              Figure 3 depicts an example of the overall method archi-
                  (                                                                       tecture. In order to leverage the advanced backbones in se-
                   KS = W S ∗ KS                                                          mantic segmentation, we firstly require to convert the input
                                        PK ×K
                   KSkh ,kw ,cin ,cout = i h w (WSi,kh ,kw ,cin × KSi,cin ,cout ),        features from RGB images to RGB-D data via the concate-
                                                                                          nation of the RGB and D information. In practice, D can
                  where KB         ∈     R1×1×Cin ×Cout and KS           ∈                be depth values [11, 20] or HHA4 images [10, 19, 16, 6].
                    Kh ×Kw ×Cin ×Cout
                  R                    denote the base-component of kernels               We then replace the vanilla convolution layer with the
                  and shape-component, respectively, and K = KB + KS .                    ShapeConv in both the backbone and segmentation stages.
                     We therefore re-formalize ShapeConv the Equation 2 to                It is worth noting that, WB is initialized to one, WS can
                  following:                                                              be viewed as Cin square (Kh × Kw ) × (Kh × Kw ) matri-
                      F = ShapeConv(K, WB , WS , P)                                       ces, which are initialized to the identity matrix. In this way,
                                                                                          ShapeConv is equivalent to the vanilla convolution at the
                            = Conv(WB  m(K) + WS ∗ (K − m(K)), P)                        beginning of training since KBS = K. This initialization ap-
                            = Conv(WB  KB + WS ∗ KS , P)                           (5)   proach offers two advantages: 1) It makes the ShapeConv-
                            = Conv(KB + KS , P)                                           enhanced networks do not interfere with the RGB data, i.e.,
                            = Conv(KBS , P),                                              the RGB features are processed in the same way as before.
                                                                                          2) It facilitates ShapeConv to reuse the parameters from pre-
                  where m(K) is the mean function on K (over the Kh × Kw                  trained models.
                  dimensions). And we require KBS = KB + KS , KBS ∈                          4 Horizontal disparity, Height above ground and normal Angle to the

                  RKh ×Kw ×Cin ×Cout .                                                    vertical axis.
                                                                                                    )*+,
                                                            )*+, E'%!0*+5 2@'F5                  25F85+@'@?*+
                                                                                                    2@'F5

GCE

                                         Baseline
                     C                   Ours

 H                          I+4B@                                                                                     <=5>?%@?*+ C=*B+>
                                                                                                                       (AB@4B@)   @=B@ℎ
                                                                                                  2ℎ'45)*+,
                                                         2ℎ'45)*+, E'%!0*+5 2@'F5                25F85+@'@?*+
                                                                                                    2@'F5
Figure 3. The overall semantic segmentation network architecture. In this figure, yellow and orange cube denote the RGB and D inputs; “C”
denotes channel-wise concatenation; Green and blue boxes denote architectures consisting of vanilla convolutional layers and ShapeConv
layers, respectively.

   Thus, with this approach, future advances in RGB se-                demonstrate the effectiveness and generalization capability
mantic segmentation architectures can be easily transferred            of ShapeConv. For all the baseline methods, we only re-
to consuming the RGB-D data, greatly reducing the effort               placed the vanilla convolutional layers with our ShapeConv,
that would otherwise be spent on designing dedicated net-              without any change to other settings. This guarantees that
works for RGB-D semantic segmentation. We have shown                   the obtained performance improvements is due to the appli-
the results of building RGB-D segmentation networks with               cation of ShapeConv, but not other factors.
this style using several popular architectures [3, 4, 18, 23,
33] in Sec 4.2.                                                        Table 1. Performance comparison with baselines on NYUDv2-13
                                                                       dataset. Deeplabv3+ is the adopted architecture.
4. Experiments                                                              Back                   Pixel     Mean        Mean       f.w.
                                                                                       Setting
Datasets and metrics. Among the existing RGB-D seg-                         bone                  Acc.(%)   Acc.(%)     IoU.(%)   IoU.(%)
mentation problems, the indoor semantic segmentation is                               Baseline     80.0      72.5         60.8      67.6
                                                                                     BaselineF     80.6      72.7         61.6      68.5
rather challenging, as the objects are often complex and                   ResNet       Ours       80.4      73.0         61.8      68.1
with severe occlusions [5]. Thus, in order to validate the                 50 [12]     OursF       81.1      73.4         62.7      69.1
effectiveness of the proposed method, we conducted exper-                                +          0.4       0.5         1.0       0.5
iments on three indoor RGB-D benchmarks: NYU-Depth-                                     +F          0.5       0.7         1.1       0.6
                                                                                      Baseline     80.0      73.4         61.3      67.6
V2 (NYUDv2-13 and -40) [25], SUN-RGBD [26] and Stan-
                                                                                     BaselineF     81.0      74.3         63.1      68.9
ford Indoor Dataset (SID) [1]. NYUDv2 contains 1,449                      ResNet        Ours       81.2      74.9         62.9      69.1
RGB-D scene images, where 795 images are split for train-                 101 [12]     OursF       81.9      75.7         64.0      70.1
ing and 654 images for testing. We adopted two popular                                   +          1.2       1.5         1.6       1.5
                                                                                        +F          0.9       1.4         0.9       1.2
settings for this dataset, i.e., 13-class [25] and 40-class [9],
                                                                                      Baseline     81.8      73.9         63.2      70.1
where all pixels are labeled with 13 and 40 classes, respec-                         BaselineF     82.2      74.4         63.7      70.6
tively. SUN-RGBD is composed of 10,355 RGB-D indoor                       ResNext       Ours       82.6      75.7         65.1      71.2
images with 37 categories for each pixel label. We followed              101 32x8d     OursF       82.9      76.0         65.6      71.6
the widely used setting in [26] to split the dataset into a                 [29]         +          0.8       1.8         1.9       1.1
                                                                                        +F          0.7       1.6         1.9       1.0
training set of 5285 images and a testing set of 5050 im-
ages. SID contains 70, 496 RGB-D images with 13 object
categories. In particular, areas 1, 2, 3, 4, and 6 used for the        Implementation Details. We used the ResNet [12] and
training and Area 5 is for testing following [27].                     ResNeXt [29] initialized with the pre-trained model on Im-
    We reported the results using the same evaluation pro-             ageNet [24] in the backbone stage. If not otherwise noted,
tocol and metrics as FCN [19], i.e., Pixel Accuracy (Pixel             the inputs of both the baseline and ours are the concate-
Acc.), Mean Accuracy (Mean Acc.), Mean Region Intersec-                nation of RGB and HHA images. We adopted both single-
tion Over Union (Mean IoU), and Frequency Weighted In-                 scale and multi-scale testing strategies during inference. For
tersection Over Union (f.w. IoU).                                      the latter one, left-right flipped images and five scales are
Comparison protocol. We adopted several popular archi-                 exploited: [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]. F in tables of
tectures with different backbones as our baseline methods to           this section denotes the multi-scale strategy. Note that, no
post-processing tricks like CRF [2] is used in our experi-          Table 4.  Performance comparison with other methods on
                                                                    NYUDv2-40 dataset.
ments.                                                                                          Pixel       Mean        Mean         f.w.
                                                                           Method
                                                                                               Acc.(%)     Acc.(%)     IoU.(%)     IoU.(%)
Table 2. Performance comparison with baselines on NYUDv2-40                FCN [19]             65.4        46.1         34.0        49.5
dataset. Deeplabv3+ is the adopted architecture.                         LSD-GF [6]             71.9        60.7         45.9        59.3
    Back                   Pixel     Mean      Mean         f.w.
                Setting                                                  D-CNN [27]               -         61.1         48.4          -
    bone                  Acc.(%)   Acc.(%)   IoU.(%)     IoU.(%)
                                                                        MMAF-Net [8]            72.2        59.2         44.8          -
              Baseline     73.1      57.7       45.6        59.2
             BaselineF     74.2      59.0       47.1        60.2         ACNet [13]               -           -          48.3          -
   ResNet       Ours       74.1      59.1       47.3        60.5             Ours               75.8        62.8         50.2        62.6
   50 [12]     OursF       75.0      60.4       48.8        61.4          CFN [17]F               -           -          47.7          -
                 +          1.0       1.4       1.7         1.3         3DGNN [22]F               -         55.7         43.1          -
                +F          0.8       1.4       1.7         1.2           RDF [21]F             76.0        62.8         50.1          -
              Baseline     73.4      58.9       45.9        59.7         M2.5D [30]F            76.9          -          50.9          -
             BaselineF     74.4      60.2       47.6        60.7         SGNet [5]F             76.8        63.3         51.1          -
  ResNet        Ours       74.5      59.5       47.4        60.8
                                                                            OursF               76.4        63.5         51.3        63.0
  101 [12]     OursF       75.5      60.7       49.0        61.7
                 +          1.1       0.6       1.59        1.1
                +F          1.1       0.5       1.4         1.0     Table 5. Performance comparison with baselines on SUN-RGBD
              Baseline     74.7      61.5       48.9        61.5    dataset. The architectures adopted in this table is deeplabv3+ with
             BaselineF     75.4      62.6       50.3        62.2    different backbones.
  ResNext       Ours       75.8      62.8       50.2        62.6                                   Pixel       Mean       Mean         f.w.
                                                                      Backbone       Setting
 101 32x8d     OursF       76.4      63.5       51.3        63.0                                  Acc.(%)     Acc.(%)    IoU.(%)     IoU.(%)
    [29]         +          1.1       1.3       1.3         1.1                    Baseline        81.1        56.5        45.5        69.7
                +F          1.0       0.9       1.0         0.8                   BaselineF        81.4        57.5        46.6        70.0
                                                                       ResNet        Ours          81.6        56.8        46.3        70.3
                                                                       50 [12]      OursF          81.9        57.9        47.7        70.6
                                                                                      +             0.5         0.3        0.8         0.6
4.1. Experiments on Different Datasets                                               +F             0.5         0.4        1.1         0.6
                                                                                   Baseline        81.6        57.8        46.9        70.4
NYUDv2 Dataset. We adopted two popular settings for                               BaselineF        81.6        58.4        47.6        70.5
this dataset, i.e., 13-class [25] and 40-class [9], and show          ResNet         Ours          82.0        58.5        47.6        71.2
the results of baseline and our method with different back-           101 [12]      OursF          82.2        59.2        48.6        71.3
                                                                                      +             0.4         0.7        0.7         0.8
bones on NYUDv2-13 and NYUDv2-40 in Table 1 and Ta-                                  +F             0.6         0.8        1.0         0.8
ble 2, respectively. It can be seen that architectures with
ShapeConv outperform the baselines with a large margin
under all settings.                                                 Table 5. It can be observed that our ShapeConv also pro-
   We also compare the performance of our ShapeConv                 duces a positive effect under all settings. We also com-
with several recently developed methods in Table 3 and Ta-          pared the performance of ours with several recently devel-
ble 4. As illustrated in Table 3, ShapeConv achieves the            oped methods in Table 6. It is worth noting that the perfor-
best over all the four metrics on NYUDv2-13. Compared               mance of the ShapeConv-enhanced Network with backbone
to the recently proposed method [32], our approach yields           of ResNet-50 in Table 5 has already achieved better results
around 6.3% improvements on Mean IOU which is the most              than several methods in Table 6, such as 3DGNN-101 [22]
commonly used metric for semantic segmentation. In addi-            and RDF-152 [21] which take the ResNet-101 and -152 as
tion, our method also achieves a competitive performance            backbone, respectively.
on NYUDv2-40 in Table 4.                                               Table 6. Performance comparison on SUN-RGBD dataset.
                                                                                                  Pixel       Mean        Mean         f.w.
Table 3.  Performance comparison with other methods on                      Method
                                                                                                 Acc.(%)     Acc.(%)     IoU.(%)     IoU.(%)
NYUDv2-13 dataset.
                       Pixel     Mean      Mean            f.w.        3DGNN-101 [22]               -         55.7         44.1          -
       Method                                                           D-CNN-50 [27]               -         53.5         42.0          -
                      Acc.(%)   Acc.(%)   IoU.(%)       IoU.(%)
     Eigen [7]         75.4      66.9         -              -        MMAF-Net-152 [8]            81.0        58.2         47.0          -
   MVCNet [20]         77.8      69.5       57.3             -          SGNet-101 [5]             81.0        59.8         47.5          -
       Ours            82.6      75.7       65.1          71.2             Ours-101               82.0        58.5         47.6        71.2
   MVCNet [20]F        79.1      70.6       59.1             -          CFN-101 [17]F               -           -          48.1          -
    PVNet [32]F        82.5      74.4       59.3             -        3DGNN-101 [22]F               -         57.0         45.9          -
      OursF            82.9      76.0       65.6          71.6          RDF-152 [21]F             81.5        60.1         47.7          -
                                                                       SGNet-101 [5]F             82.0        60.7         48.6          -
                                                                          Ours-101F               82.2        59.2         48.6        71.3

SUN-RGBD Dataset. The comparison results between                    SID Dataset. Note that SID dataset is much larger than
baseline and ours with SUN-RGBD dataset are reported in             the other two datasets, contributing to a better testbed for
      #$%&'(             )*            +!(,-.$,          /&0(            #$%&'(                )*              +!(,-.$,            /&0(

                                  !                                                                            "
Figure 4. Visualization results from NYUDv2 dataset. Input column denotes RGB, Depth, HHA images from top to bottom; the black
regions in the GT, Baseline and Ours indicate the ignored category. The upper and lower cases are from NYUDv2-40 and NYUDv2-13,
respectively.

evaluating RGB-D semantic segmentation model capabili-                Table 8. Performance comparison with different baseline methods
                                                                      on NYUDv2-40 dataset.
ties. The results on SID dataset between the baseline with                             Back               Pixel     Mean      Mean       f.w.
                                                                        Architecture          Setting
ours and the state-of-the-art methods are reported in Table 7.                         bone              Acc.(%)   Acc.(%)   IoU.(%)   IoU.(%)
                                                                                       Res    Baseline    73.4      58.9       45.9      59.7
We can observe that our ShapeConv surpasses these meth-                                 Net    Ours       74.5      59.5       47.4      60.8
ods with a large margin. Note that even though we utilized              Deeplabv3+     101       +         1.1       0.6        1.5       1.1
a strong baseline (ResNet-101 backbone) which surpasses                     [4]        Res    Baseline    73.1      57.7       45.6      59.2
                                                                                        Net    Ours       74.1      59.1       47.3      60.5
MMAF-Net-152 (ResNet-152 backbone) with 1.7% Mean                                       50       +         1.0       1.4        1.7       1.3
IoU, our ShapeConv can still achieves a 6% Mean IoU im-                                Res    Baseline    73.3      57.3       45.1      59.2
                                                                                        Net    Ours       73.6      58.5       46.4      59.7
provement. This highlights the effectiveness of our method.              Deeplabv3     101       +         0.3       1.2        1.3       0.5
                                                                            [3]        Res    Baseline    71.6      55.5       43.2      57.2
                                                                                        Net    Ours       72.8      56.6       44.9      58.5
Table 7. Performance comparison on SID dataset. The architec-                           50       +         1.2       1.1        1.7       1.3
tures of baseline and ours adopted in this table is deeplabv3+ with                    Res    Baseline    70.9      54.7       42.1      57.7
ResNet-101 backbone and the “+” denote the deltas relative to the                       Net    Ours       72.3      56.5       43.9      58.8
                                                                           UNet        101       +         1.4       1.8        1.8       1.1
baseline method.
                                                                            [23]       Res    Baseline    70.0      51.7       39.7      55.5
                         Pixel      Mean       Mean        f.w.
        Method                                                                          Net    Ours       70.8      54.1       42.0      56.9
                        Acc.(%)    Acc.(%)    IoU.(%)    IoU.(%)                        50       +         0.8       2.4        2.3       1.4
    D-CNN [27]           65.4       55.5        39.5       49.9                        Res    Baseline    72.8      56.8       44.2      58.9
  MMAF-Net-152 [8]       76.5       62.3        52.9         -                          Net    Ours       73.3      59.2       46.3      59.6
                                                                          PSPNet       101       +         0.5       2.4        2.1       0.7
    Baseline-101         78.7       63.2        54.6       65.6             [33]       Res    Baseline    71.1      53.6       42.0      56.7
     Ours-101            82.7       70.0        60.6       71.2                         Net    Ours       72.0      56.2       44.0      57.7
         +                4.0        6.8         6.0        5.6                         50       +         0.9       2.6        2.0       1.0
                                                                                       Res    Baseline    72.8      57.3       44.7      59.1
                                                                                        Net    Ours       73.6      58.4       45.9      60.0
                                                                           FPN         101       +         0.8       1.1        1.2       0.9
                                                                           [18]        Res    Baseline    70.3      52.8       40.9      56.0
4.2. Experiments on Different Architectures                                             Net    Ours       71.5      54.9       42.8      57.5
                                                                                        50       +         1.2       2.1        1.9       1.5
    Our proposed ShapeConv is a general layer for RGB-
D semantic segmentation which can be easily plugged into
most CNNs as a replacement for the vanilla convolution in
semantic segmentation. To verify its generalization proper-           4.3. Visualization
ties, we also evaluated the effectiveness of our method in                Figure 4 illustrates the qualitative results on NYUDv2-
several representative semantic segmentation architectures:           13 and -40, more results can be found in the Supp. As
Deeplabv3+ [4], Deeplabv3 [3], UNet [23], PSPNet [33]                 shown in this figure, the depth information, especially the
and FPN [18] with different backbones (ResNet-50 [12],                detailed one, can be well utilized by ShapeConv to extract
ResNet-101 [12]) on NYUDv2-40 dataset, and reported the               the object features. For instance, the chair and table re-
performance in Table 8. We can see that ShapeConv brings              gions in the top example of Figure 4(a) are with gradually
significant performance improvements under all settings,              changed colors, making it hard to predict accurate segmen-
demonstrating the generalization capability of our method.            tation boundaries of the baseline method. The shape fea-
                                                                                                                  44
                                                                                                                                                              Baseline (ResNet-50)
                                                                                                                  42                                         ShapeConv (ResNet-50)
                                                                                                                                                              Baseline (ResNet-101)
                                                                                                                  40                                         ShapeConv (ResNet-101)

                                                                                                Pixel Error (%)
                                                                                                                  38

                                                                                                                  36

                                                                                                                  34

                                                                                                                  32

                                                                                                                  30

                                                                                                                  28
                                                                                                                       0   2     4    6     8    10   12     14    16     18     20

      Image              GT              Trimap (4pix)        Trimap (8pix)    Trimap (12pix)                                        Trimap Width (Pixels)
Figure 5. Segmentation accuracy around object boundaries. In this figure, the left is the visualization of the “trimap” measure; The right is
the percent of misclassified pixels within trimaps of different widths.

tures learned by ShapeConv makes the accurate cut follow-                     Table 10. Ablation study of the proposed ShapeConv on the
                                                                              NYUDv2-40 dataset. RGB, Detph and HHA denote the inputs
ing the geometric hints compare with the conventional con-
                                                                              consisting of RGB images, depth images and HHA images.
volutional layer. For other two cases, i.e., the chair in the                                                                  Pixel      Mean         Mean             f.w.
                                                                               Setting
bottom example of Figure 4(a) and the desk in the top exam-                                                                    Acc.(%)    Acc.(%)      IoU.(%)          IoU.(%)
ple of Figure 4(b), the ShapeConv can also significantly im-                   a.RGB                                           71.8       56.9         43.9             57.3
                                                                               b.RGB+Depth                                     72.8       58.9         44.9             57.7
prove the segmentation results in edge areas compared with                     c.RGB+DepthF                                    73.9       59.1         46.8             60.0
the baseline. It is worth noting that for the multiple book-                   d.RGB+HHA                                       73.4       58.9         45.9             59.7
shelves in the bottom example of Figure 4(b), ShapeConv                        e.RGB+HHAF                                      74.4       60.2         47.6             60.7
achieves more consistent predictions. This is because our                      f.RGB+Depth+ShapeConv                           73.9       58.2         46.2             60.0
                                                                               g.RGB+Depth+ShapeConvF                          74.8       59.2         47.5             60.8
ShapeConv yields a positive tendency for smoothing neigh-                      h.RGB+HHA+ShapeConv                             74.5       59.5         47.4             60.8
borhood regions within same classes.                                           i.RGB+HHA+ShapeConvF                            75.5       60.7         49.0             61.7
   To validate the effectiveness of our method on modeling
the depth information, we adopted the comparison strategy
proposed by Kohli et al. [14]. Specifically, we counted the                   key observations from this table are as follows: 1) The in-
relative number of misclassified pixels within a narrow band                  put features with HHA outperform the Depth images for
(“trimap”) surrounding ground-truth object boundaries. As                     the baseline and ours; 2) Replacing the vanilla convolu-
shown in Figure 5, our method outperforms the baseline                        tion with ShapeConv leads to considerable performance im-
across all trimap widths. This further demonstrates the seg-                  provements on both Depth and HHA; 3) The multi-scale
mentation effectiveness of our method on edge areas, where                    setting in testing phase brings more performance gains; 4)
the shape information matters.                                                Cascading the ShapeConv with HHA and multi-scale test-
                                                                              ing can achieve the best result.
4.4. Ablation Study
   We conducted ablation experiments to validate the indis-
pensability of the two introduced weights in Equation 5. As                   5. Conclusion
can be observed in Table 9, the model performance degrades                       In this paper, we propose a ShapeConv layer to effec-
when removing either WB or WS , or both. This proves                          tively leverage the depth information for RGB-D semantic
that both the base-kernel and shape-kernel are essential for                  segmentation. In particular, an input patch is firstly decom-
the final performance improvement, and combing these two                      posed into two components, i.e., shape and base, which are
achieves the best results.                                                    then decorated with two corresponding learnable weights
Table 9. Performance comparison with and without WB and WS                    before the convolution is applied. We have conducted ex-
in ShapeConv on NYUDv2-40. The architecture adopted in this                   tensive experiments on several challenging indoor RGB-D
table is deeplabv3+ with ResNet-101 as backbone.                              semantic segmentation benchmarks and promising experi-
                     Pixel      Mean        Mean           f.w.               mental results can be observed. Moreover, it is worth noting
       WB     WS
                    Acc.(%)    Acc.(%)     IoU.(%)       IoU.(%)
                     73.4       58.9         45.9          59.7
                                                                              that our ShapeConv introducing no additional computation
        X            73.9       59.4         47.0          60.1               or memory in comparison with the vanilla convolution dur-
               X     74.1       59.2         46.3          60.1               ing inference, yet with superior performance.
        X      X     74.5       59.5         47.4          60.8                  In fact, the shape-component is inherent in the local ge-
   To provide a more in-depth analysis of ShapeConv, we                       ometry and highly relevant to the semantics in images. In
conducted detailed ablation studies on the NYUDv2-40                          the future, we plan to expand the application scope to other
dataset with deeplabv3+ and ResNet-101 as baseline and                        geometry entities, such as point clouds, where the shape-
backbone, respectively. Results on more datasets can be                       base decomposition is more challenging due to the addi-
found at the Supp. Table 10 illustrates the results and the                   tional degree of freedom.
Acknowledgments. This work is supported by the National            Conference on Computer Vision and Pattern Recogni-
Key Research and Development Program of China grant                tion, pages 564–571, 2013.
No.2017YFB1002603, the National Science Foundation of         [10] Saurabh Gupta, Ross Girshick, Pablo Arbeláez, and
China General Program grant No.61772317, 61772318 and              Jitendra Malik. Learning rich features from rgb-d im-
62072284, “Qilu” Young Talent Program of Shandong Uni-             ages for object detection and segmentation. In Pro-
versity, and the Research Intern Program of Alibaba Group.         ceedings of the European Conference on Computer Vi-
                                                                   sion, pages 345–360. Springer, 2014.
References
                                                              [11] Caner Hazirbas, Lingni Ma, Csaba Domokos, and
 [1] Iro Armeni, Sasha Sax, Amir R Zamir, and Silvio               Daniel Cremers. Fusenet: Incorporating depth into
     Savarese. Joint 2d-3d-semantic data for indoor scene          semantic segmentation via fusion-based cnn architec-
     understanding. arXiv preprint arXiv:1702.01105,               ture. In Asian Conference on Computer Vision, pages
     2017.                                                         213–228. Springer, 2016.
 [2] Liang-Chieh Chen, George Papandreou, Iasonas             [12] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian
     Kokkinos, Kevin Murphy, and Alan L Yuille. Deeplab:           Sun. Deep residual learning for image recognition.
     Semantic image segmentation with deep convolutional           In Proceedings of the IEEE Conference on Computer
     nets, atrous convolution, and fully connected crfs.           Vision and Pattern Recognition, pages 770–778, 2016.
     IEEE transactions on pattern analysis and machine        [13] Xinxin Hu, Kailun Yang, Lei Fei, and Kaiwei Wang.
     intelligence, 40(4):834–848, 2017.                            Acnet: Attention based network to exploit comple-
 [3] Liang-Chieh Chen, George Papandreou, Florian                  mentary features for rgbd semantic segmentation. In
     Schroff, and Hartwig Adam. Rethinking atrous con-             2019 IEEE International Conference on Image Pro-
     volution for semantic image segmentation. arXiv               cessing (ICIP), pages 1440–1444. IEEE, 2019.
     preprint arXiv:1706.05587, 2017.                         [14] Pushmeet Kohli, Philip HS Torr, et al. Robust higher
 [4] Liang-Chieh Chen, Yukun Zhu, George Papandreou,               order potentials for enforcing label consistency. Inter-
     Florian Schroff, and Hartwig Adam. Encoder-decoder            national Journal of Computer Vision, 82(3):302–324,
     with atrous separable convolution for semantic image          2009.
     segmentation. In Proceedings of the European Con-        [15] Siqi Li, Changqing Zou, Yipeng Li, Xibin Zhao, and
     ference on Computer Vision, pages 801–818, 2018.              Yue Gao. Attention-based multi-modal fusion net-
 [5] Lin-Zhuo Chen, Zheng Lin, Ziqin Wang, Yong-Liang              work for semantic scene completion. In Proceedings
     Yang, and Ming-Ming Cheng. Spatial information                of the AAAI Conference on Artificial Intelligence, vol-
     guided convolution for real-time rgbd semantic seg-           ume 34, pages 11402–11409, 2020.
     mentation. IEEE Transactions on Image Processing,        [16] Zhen Li, Yukang Gan, Xiaodan Liang, Yizhou Yu, Hui
     30:2313–2324, 2021.                                           Cheng, and Liang Lin. Lstm-cf: Unifying context
 [6] Yanhua Cheng, Rui Cai, Zhiwei Li, Xin Zhao, and               modeling and fusion with lstms for rgb-d scene label-
     Kaiqi Huang. Locality-sensitive deconvolution net-            ing. In Proceedings of the European Conference on
     works with gated fusion for rgb-d indoor semantic seg-        Computer Vision, pages 541–557. Springer, 2016.
     mentation. In Proceedings of the IEEE Conference         [17] Di Lin, Guangyong Chen, Daniel Cohen-Or, Pheng-
     on Computer Vision and Pattern Recognition, pages             Ann Heng, and Hui Huang. Cascaded feature net-
     3029–3037, 2017.                                              work for semantic segmentation of rgb-d images. In
 [7] David Eigen and Rob Fergus. Predicting depth, sur-            Proceedings of the IEEE International Conference on
     face normals and semantic labels with a common                Computer Vision, pages 1311–1319, 2017.
     multi-scale convolutional architecture. In Proceedings   [18] Tsung-Yi Lin, Piotr Dollár, Ross Girshick, Kaiming
     of the IEEE International Conference on Computer Vi-          He, Bharath Hariharan, and Serge Belongie. Feature
     sion, pages 2650–2658, 2015.                                  pyramid networks for object detection. In Proceed-
 [8] Fahimeh Fooladgar and Shohreh Kasaei. Multi-                  ings of the IEEE Conference on Computer Vision and
     modal attention-based fusion model for semantic               Pattern Recognition, pages 2117–2125, 2017.
     segmentation of rgb-depth images. arXiv preprint         [19] Jonathan Long, Evan Shelhamer, and Trevor Darrell.
     arXiv:1912.11691, 2019.                                       Fully convolutional networks for semantic segmenta-
 [9] Saurabh Gupta, Pablo Arbelaez, and Jitendra Ma-               tion. In Proceedings of the IEEE Conference on Com-
     lik. Perceptual organization and recognition of indoor        puter Vision and Pattern Recognition, pages 3431–
     scenes from rgb-d images. In Proceedings of the IEEE          3440, 2015.
[20] Lingni Ma, Jörg Stückler, Christian Kerl, and Daniel   [30] Yajie Xing, Jingbo Wang, and Gang Zeng. Malleable
     Cremers. Multi-view deep learning for consistent              2.5 d convolution: Learning receptive fields along the
     semantic mapping with rgb-d cameras. In 2017                  depth-axis for rgb-d scene parsing. arXiv preprint
     IEEE/RSJ International Conference on Intelligent              arXiv:2007.09365, 2020.
     Robots and Systems (IROS), pages 598–605. IEEE,          [31] Zhengyou Zhang. Microsoft kinect sensor and its ef-
     2017.                                                         fect. IEEE multimedia, 19(2):4–10, 2012.
[21] Seong-Jin Park, Ki-Sang Hong, and Seungyong Lee.         [32] Cheng Zhao, Li Sun, Pulak Purkait, Tom Duckett,
     Rdfnet: Rgb-d multi-level residual feature fusion for         and Rustam Stolkin. Dense rgb-d semantic mapping
     indoor semantic segmentation. In Proceedings of the           with pixel-voxel neural network. Sensors, 18(9):3099,
     IEEE International Conference on Computer Vision,             2018.
     pages 4980–4989, 2017.                                   [33] Hengshuang Zhao, Jianping Shi, Xiaojuan Qi, Xiao-
[22] Xiaojuan Qi, Renjie Liao, Jiaya Jia, Sanja Fidler, and        gang Wang, and Jiaya Jia. Pyramid scene parsing
     Raquel Urtasun. 3d graph neural networks for rgbd             network. In Proceedings of the IEEE Conference
     semantic segmentation. In Proceedings of the IEEE             on Computer Vision and Pattern Recognition, pages
     International Conference on Computer Vision, pages            2881–2890, 2017.
     5199–5208, 2017.
[23] Olaf Ronneberger, Philipp Fischer, and Thomas Brox.
     U-net: Convolutional networks for biomedical image
     segmentation. In International Conference on Med-
     ical Image Computing and Computer-assisted Inter-
     vention, pages 234–241. Springer, 2015.
[24] Olga Russakovsky, Jia Deng, Hao Su, Jonathan
     Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang,
     Andrej Karpathy, Aditya Khosla, Michael Bernstein,
     et al. ImageNet large scale visual recognition chal-
     lenge. International Journal of Computer Vision,
     115(3):211–252, 2015.
[25] Nathan Silberman, Derek Hoiem, Pushmeet Kohli,
     and Rob Fergus. Indoor segmentation and support in-
     ference from rgbd images. In Proceedings of the Euro-
     pean Conference on Computer Vision, pages 746–760.
     Springer, 2012.
[26] Shuran Song, Samuel P Lichtenberg, and Jianxiong
     Xiao. Sun rgb-d: A rgb-d scene understanding bench-
     mark suite. In Proceedings of the IEEE Conference
     on Computer Vision and Pattern Recognition, pages
     567–576, 2015.
[27] Weiyue Wang and Ulrich Neumann. Depth-aware cnn
     for rgb-d segmentation. In Proceedings of the Euro-
     pean Conference on Computer Vision, pages 135–150,
     2018.
[28] Yikai Wang, Wenbing Huang, Fuchun Sun, Tingyang
     Xu, Yu Rong, and Junzhou Huang. Deep multimodal
     fusion by channel exchanging. Advances in Neural
     Information Processing Systems, 33, 2020.
[29] Saining Xie, Ross Girshick, Piotr Dollár, Zhuowen Tu,
     and Kaiming He. Aggregated residual transformations
     for deep neural networks. In Proceedings of the IEEE
     Conference on Computer Vision and Pattern Recogni-
     tion, pages 1492–1500, 2017.
