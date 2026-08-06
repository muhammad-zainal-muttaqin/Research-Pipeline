---
source_id: 021
bibtex_key: tan2020efficientdet
title: EfficientDet: Scalable and Efficient Object Detection
year: 2020
domain_theme: Fondasi RGB
verified_pdf: 21_EfficientDet.pdf
char_count: 83818
---

EfficientDet: Scalable and Efficient Object Detection

                                                                                  Mingxing Tan Ruoming Pang Quoc V. Le
                                                                                        Google Research, Brain Team
                                                                                   {tanmingxing, rpang, qvl}@google.com
arXiv:1911.09070v7 [cs.CV] 27 Jul 2020

                                                                     Abstract                                                                         EfficientDet-D7
                                                                                                                                                 D6
                                                                                                                                          D5
                                            Model efficiency has become increasingly important in                         50
                                                                                                                                                                                  AmoebaNet + NAS-FPN + AA
                                                                                                                                    D4
                                         computer vision. In this paper, we systematically study neu-
                                                                                                                                   D3
                                         ral network architecture design choices for object detection
                                                                                                                          45                                                           ResNet + NAS-FPN
                                         and propose several key optimizations to improve efficiency.                              D2

                                                                                                                COCO AP
                                         First, we propose a weighted bi-directional feature pyra-
                                         mid network (BiFPN), which allows easy and fast multi-                                                       RetinaNet
                                                                                                                          40       D1
                                         scale feature fusion; Second, we propose a compound scal-
                                                                                                                                           Mask R-CNN
                                         ing method that uniformly scales the resolution, depth, and                                                                                            AP FLOPs (ratio)
                                                                                                                          35
                                         width for all backbone, feature network, and box/class pre-                                                              EfficientDet-D0              33.8 2.5B
                                                                                                                                                                  YOLOv3 [34]                  33.0 71B (28x)
                                         diction networks at the same time. Based on these optimiza-                                    YOLOv3                    EfficientDet-D1              39.6 6.1B
                                                                                                                                                                  RetinaNet [24]               39.2 97B (16x)
                                         tions and better backbones, we have developed a new family                       30                                      EfficientDet-D7x†            55.1 410B
                                         of object detectors, called EfficientDet, which consistently                                                             AmoebaNet+ NAS-FPN +AA [45]† 50.7 3045B (13x)
                                                                                                                                                                   † Not plotted.

                                         achieve much better efficiency than prior art across a wide                           0          200         400       600        800          1000        1200
                                         spectrum of resource constraints. In particular, with single-                                                         FLOPs (Billions)
                                         model and single-scale, our EfficientDet-D7 achieves state-           Figure 1: Model FLOPs vs. COCO accuracy – All num-
                                         of-the-art 55.1 AP on COCO test-dev with 77M param-                   bers are for single-model single-scale. Our EfficientDet
                                         eters and 410B FLOPs1 , being 4x – 9x smaller and using               achieves new state-of-the-art 55.1% COCO AP with much
                                         13x – 42x fewer FLOPs than previous detectors. Code is                fewer parameters and FLOPs than previous detectors. More
                                         available at https://github.com/google/automl/tree/                   studies on different backbones and FPN/NAS-FPN/BiFPN
                                         master/efficientdet.                                                  are in Table 4 and 5. Complete results are in Table 2.

                                                                                                               stage [27, 33, 34, 24] and anchor-free detectors [21, 44, 40],
                                         1. Introduction                                                       or compress existing models [28, 29]. Although these meth-
                                                                                                               ods tend to achieve better efficiency, they usually sacrifice
                                            Tremendous progresses have been made in recent years               accuracy. Moreover, most previous works only focus on a
                                         towards more accurate object detection; meanwhile, state-             specific or a small range of resource requirements, but the
                                         of-the-art object detectors also become increasingly more             variety of real-world applications, from mobile devices to
                                         expensive. For example, the latest AmoebaNet-based NAS-               datacenters, often demand different resource constraints.
                                         FPN detector [45] requires 167M parameters and 3045B
                                                                                                                   A natural question is: Is it possible to build a scal-
                                         FLOPs (30x more than RetinaNet [24]) to achieve state-of-
                                                                                                               able detection architecture with both higher accuracy and
                                         the-art accuracy. The large model sizes and expensive com-
                                                                                                               better efficiency across a wide spectrum of resource con-
                                         putation costs deter their deployment in many real-world
                                                                                                               straints (e.g., from 3B to 300B FLOPs)? This paper aims
                                         applications such as robotics and self-driving cars where
                                                                                                               to tackle this problem by systematically studying various
                                         model size and latency are highly constrained. Given these
                                                                                                               design choices of detector architectures. Based on the one-
                                         real-world resource constraints, model efficiency becomes
                                                                                                               stage detector paradigm, we examine the design choices for
                                         increasingly important for object detection.
                                                                                                               backbone, feature fusion, and class/box network, and iden-
                                            There have been many previous works aiming to de-
                                                                                                               tify two main challenges:
                                         velop more efficient detector architectures, such as one-
                                                                                                                   Challenge 1: efficient multi-scale feature fusion – Since
                                           1 Similar to [14, 39], FLOPs denotes number of multiply-adds.       introduced in [23], FPN has been widely used for multi-

                                                                                                           1
scale feature fusion. Recently, PANet [26], NAS-FPN [10],             have attracted substantial attention due to their efficiency
and other studies [20, 18, 42] have developed more network            and simplicity [21, 42, 44]. In this paper, we mainly follow
structures for cross-scale feature fusion. While fusing dif-          the one-stage detector design, and we show it is possible
ferent input features, most previous works simply sum them            to achieve both better efficiency and higher accuracy with
up without distinction; however, since these different input          optimized network architectures.
features are at different resolutions, we observe they usu-
                                                                      Multi-Scale Feature Representations: One of the main
ally contribute to the fused output feature unequally. To
                                                                      difficulties in object detection is to effectively represent and
address this issue, we propose a simple yet highly effective
                                                                      process multi-scale features. Earlier detectors often directly
weighted bi-directional feature pyramid network (BiFPN),
                                                                      perform predictions based on the pyramidal feature hierar-
which introduces learnable weights to learn the importance
                                                                      chy extracted from backbone networks [4, 27, 36]. As one
of different input features, while repeatedly applying top-
                                                                      of the pioneering works, feature pyramid network (FPN)
down and bottom-up multi-scale feature fusion.
                                                                      [23] proposes a top-down pathway to combine multi-scale
   Challenge 2: model scaling – While previous works
                                                                      features. Following this idea, PANet [26] adds an extra
mainly rely on bigger backbone networks [24, 35, 34, 10] or
                                                                      bottom-up path aggregation network on top of FPN; STDL
larger input image sizes [13, 45] for higher accuracy, we ob-
                                                                      [43] proposes a scale-transfer module to exploit cross-scale
serve that scaling up feature network and box/class predic-
                                                                      features; M2det [42] proposes a U-shape module to fuse
tion network is also critical when taking into account both
                                                                      multi-scale features, and G-FRNet [2] introduces gate units
accuracy and efficiency. Inspired by recent works [39], we
                                                                      for controlling information flow across features. More re-
propose a compound scaling method for object detectors,
                                                                      cently, NAS-FPN [10] leverages neural architecture search
which jointly scales up the resolution/depth/width for all
                                                                      to automatically design feature network topology. Although
backbone, feature network, box/class prediction network.
                                                                      it achieves better performance, NAS-FPN requires thou-
   Finally, we also observe that the recently introduced Effi-
                                                                      sands of GPU hours during search, and the resulting feature
cientNets [39] achieve better efficiency than previous com-
                                                                      network is irregular and thus difficult to interpret. In this
monly used backbones. Combining EfficientNet backbones
                                                                      paper, we aim to optimize multi-scale feature fusion with a
with our propose BiFPN and compound scaling, we have
                                                                      more intuitive and principled way.
developed a new family of object detectors, named Effi-
cientDet, which consistently achieve better accuracy with             Model Scaling: In order to obtain better accuracy, it
much fewer parameters and FLOPs than previous object                  is common to scale up a baseline detector by employing
detectors. Figure 1 and Figure 4 show the performance                 bigger backbone networks (e.g., from mobile-size models
comparison on COCO dataset [25]. Under similar accu-                  [38, 16] and ResNet [14], to ResNeXt [41] and AmoebaNet
racy constraint, our EfficientDet uses 28x fewer FLOPs than           [32]), or increasing input image size (e.g., from 512x512
YOLOv3 [34], 30x fewer FLOPs than RetinaNet [24], and                 [24] to 1536x1536 [45]). Some recent works [10, 45] show
19x fewer FLOPs than the recent ResNet based NAS-FPN                  that increasing the channel size and repeating feature net-
[10]. In particular, with single-model and single test-time           works can also lead to higher accuracy. These scaling
scale, our EfficientDet-D7 achieves state-of-the-art 55.1 AP          methods mostly focus on single or limited scaling dimen-
with 77M parameters and 410B FLOPs, outperforming pre-                sions. Recently, [39] demonstrates remarkable model effi-
vious best detector [45] by 4 AP while being 2.7x smaller             ciency for image classification by jointly scaling up network
and using 7.4x fewer FLOPs. Our EfficientDet is also up to            width, depth, and resolution. Our proposed compound scal-
4x to 11x faster on GPU/CPU than previous detectors.                  ing method for object detection is mostly inspired by [39].
   With simple modifications, we also demonstrate that
our single-model single-scale EfficientDet achieves 81.74%            3. BiFPN
mIOU accuracy with 18B FLOPs on Pascal VOC 2012 se-
                                                                         In this section, we first formulate the multi-scale feature
mantic segmentation, outperforming DeepLabV3+ [6] by
                                                                      fusion problem, and then introduce the main ideas for our
1.7% better accuracy with 9.8x fewer FLOPs.
                                                                      proposed BiFPN: efficient bidirectional cross-scale connec-
                                                                      tions and weighted feature fusion.
2. Related Work
                                                                      3.1. Problem Formulation
One-Stage Detectors:          Existing object detectors are
mostly categorized by whether they have a region-of-                     Multi-scale feature fusion aims to aggregate features at
interest proposal step (two-stage [11, 35, 5, 13]) or not (one-       different resolutions. Formally, given a list of multi-scale
stage [36, 27, 33, 24]). While two-stage detectors tend to be         features P~ in = (Plin  1
                                                                                                , Plin
                                                                                                    2
                                                                                                       , ...), where Plin
                                                                                                                       i
                                                                                                                          represents the
more flexible and more accurate, one-stage detectors are of-          feature at level li , our goal is to find a transformation f that
ten considered to be simpler and more efficient by leverag-           can effectively aggregate different features and output a list
ing predefined anchors [17]. Recently, one-stage detectors            of new features: P~ out = f (P~ in ). As a concrete example,

                                                                  2
                                                                           repeated blocks                      repeated blocks

                               P7                                 P7                                   P7
  P7

                               P6                                 P6                                   P6
  P6

                               P5                                 P5                                   P5
  P5

                               P4                                 P4                                   P4
  P4

                               P3                                 P3                                   P3
  P3

             (a) FPN                      (b) PANet                          (c) NAS-FPN                          (d) BiFPN

Figure 2: Feature network design – (a) FPN [23] introduces a top-down pathway to fuse multi-scale features from level 3 to
7 (P3 - P7 ); (b) PANet [26] adds an additional bottom-up pathway on top of FPN; (c) NAS-FPN [10] use neural architecture
search to find an irregular feature network topology and then repeatedly apply the same block; (d) is our BiFPN with better
accuracy and efficiency trade-offs.

Figure 2(a) shows the conventional top-down FPN [23]. It               efficiency, this paper proposes several optimizations for
takes level 3-7 input features P~ in = (P3in , ...P7in ), where        cross-scale connections: First, we remove those nodes that
Piin represents a feature level with resolution of 1/2i of the         only have one input edge. Our intuition is simple: if a
input images. For instance, if input resolution is 640x640,            node has only one input edge with no feature fusion, then
then P3in represents feature level 3 (640/23 = 80) with res-           it will have less contribution to feature network that aims
olution 80x80, while P7in represents feature level 7 with res-         at fusing different features. This leads to a simplified bi-
olution 5x5. The conventional FPN aggregates multi-scale               directional network; Second, we add an extra edge from the
features in a top-down manner:                                         original input to output node if they are at the same level,
                                                                       in order to fuse more features without adding much cost;
                                                                       Third, unlike PANet [26] that only has one top-down and
           P7out = Conv(P7in )                                         one bottom-up path, we treat each bidirectional (top-down
           P6out = Conv(P6in + Resize(P7out ))                         & bottom-up) path as one feature network layer, and repeat
              ...                                                      the same layer multiple times to enable more high-level fea-
                                                                       ture fusion. Section 4.2 will discuss how to determine the
           P3out = Conv(P3in + Resize(P4out ))                         number of layers for different resource constraints using a
                                                                       compound scaling method. With these optimizations, we
where Resize is usually a upsampling or downsampling
                                                                       name the new feature network as bidirectional feature pyra-
op for resolution matching, and Conv is usually a convo-
                                                                       mid network (BiFPN), as shown in Figure 2 and 3.
lutional op for feature processing.
                                                                       3.3. Weighted Feature Fusion
3.2. Cross-Scale Connections
                                                                           When fusing features with different resolutions, a com-
   Conventional top-down FPN is inherently limited by the
                                                                       mon way is to first resize them to the same resolution and
one-way information flow. To address this issue, PANet
                                                                       then sum them up. Pyramid attention network [22] intro-
[26] adds an extra bottom-up path aggregation network, as
                                                                       duces global self-attention upsampling to recover pixel lo-
shown in Figure 2(b). Cross-scale connections are further
                                                                       calization, which is further studied in [10]. All previous
studied in [20, 18, 42]. Recently, NAS-FPN [10] employs
                                                                       methods treat all input features equally without distinction.
neural architecture search to search for better cross-scale
                                                                       However, we observe that since different input features are
feature network topology, but it requires thousands of GPU
                                                                       at different resolutions, they usually contribute to the output
hours during search and the found network is irregular and
                                                                       feature unequally. To address this issue, we propose to add
difficult to interpret or modify, as shown in Figure 2(c).
                                                                       an additional weight for each input, and let the network to
   By studying the performance and efficiency of these
                                                                       learn the importance of each input feature. Based on this
three networks (Table 5), we observe that PANet achieves
                                                                       idea, we consider three weighted fusion approaches:
better accuracy than FPN and NAS-FPN, but with the cost                                                 P
of more parameters and computations. To improve model                  Unbounded fusion: O =               i wi · Ii , where wi is a

                                                                   3
learnable weight that can be a scalar (per-feature), a vec-             4.1. EfficientDet Architecture
tor (per-channel), or a multi-dimensional tensor (per-pixel).
                                                                           Figure 3 shows the overall architecture of EfficientDet,
We find a scale can achieve comparable accuracy to other
                                                                        which largely follows the one-stage detectors paradigm
approaches with minimal computational costs. However,
                                                                        [27, 33, 23, 24]. We employ ImageNet-pretrained Effi-
since the scalar weight is unbounded, it could potentially
                                                                        cientNets as the backbone network. Our proposed BiFPN
cause training instability. Therefore, we resort to weight
                                                                        serves as the feature network, which takes level 3-7 features
normalization to bound the value range of each weight.
                                                                        {P3 , P4 , P5 , P6 , P7 } from the backbone network and re-
                               P ewi                                    peatedly applies top-down and bottom-up bidirectional fea-
Softmax-based fusion: O = i P wj · Ii . An intuitive
                                      je                                ture fusion. These fused features are fed to a class and box
idea is to apply softmax to each weight, such that all weights          network to produce object class and bounding box predic-
are normalized to be a probability with value range from 0              tions respectively. Similar to [24], the class and box net-
to 1, representing the importance of each input. However,               work weights are shared across all levels of features.
as shown in our ablation study in section 6.3, the extra soft-
max leads to significant slowdown on GPU hardware. To                   4.2. Compound Scaling
minimize the extra latency cost, we further propose a fast                 Aiming at optimizing both accuracy and efficiency, we
fusion approach.                                                        would like to develop a family of models that can meet
                                  P        wi                           a wide spectrum of resource constraints. A key challenge
Fast normalized fusion: O = i             P        · Ii , where
                                      + j wj                           here is how to scale up a baseline EfficientDet model.
wi ≥ 0 is ensured by applying a Relu after each wi , and                   Previous works mostly scale up a baseline detector by
 = 0.0001 is a small value to avoid numerical instability.             employing bigger backbone networks (e.g., ResNeXt [41]
Similarly, the value of each normalized weight also falls               or AmoebaNet [32]), using larger input images, or stack-
between 0 and 1, but since there is no softmax operation                ing more FPN layers [10]. These methods are usually in-
here, it is much more efficient. Our ablation study shows               effective since they only focus on a single or limited scal-
this fast fusion approach has very similar learning behavior            ing dimensions. Recent work [39] shows remarkable per-
and accuracy as the softmax-based fusion, but runs up to                formance on image classification by jointly scaling up all
30% faster on GPUs (Table 6).                                           dimensions of network width, depth, and input resolution.
                                                                        Inspired by these works [10, 39], we propose a new com-
   Our final BiFPN integrates both the bidirectional cross-             pound scaling method for object detection, which uses a
scale connections and the fast normalized fusion. As a con-             simple compound coefficient φ to jointly scale up all dimen-
crete example, here we describe the two fused features at               sions of backbone , BiFPN, class/box network, and resolu-
level 6 for BiFPN shown in Figure 2(d):                                 tion. Unlike [39], object detectors have much more scaling
                                                                        dimensions than image classification models, so grid search
                                                                        for all dimensions is prohibitive expensive. Therefore, we
                   w1 · P6in + w2 · Resize(P7in )
                                                   
                                                                        use a heuristic-based scaling approach, but still follow the
 P6td = Conv                                                            main idea of jointly scaling up all dimensions.
                            w1 + w2 + 
                   w10 · P6in + w20 · P6td + w30 · Resize(P5out )
                                                                   
P6out = Conv                                                            Backbone network – we reuse the same width/depth
                                w10 + w20 + w30 + 
                                                                        scaling coefficients of EfficientNet-B0 to B6 [39] such that
                                                                        we can easily reuse their ImageNet-pretrained checkpoints.
where P6td is the intermediate feature at level 6 on the top-
down pathway, and P6out is the output feature at level 6 on
                                                                        BiFPN network – we linearly increase BiFPN depth
the bottom-up pathway. All other features are constructed
                                                                        Dbif pn (#layers) since depth needs to be rounded to small
in a similar manner. Notably, to further improve the effi-
                                                                        integers. For BiFPN width Wbif pn (#channels), exponen-
ciency, we use depthwise separable convolution [7, 37] for
                                                                        tially grow BiFPN width Wbif pn (#channels) as similar to
feature fusion, and add batch normalization and activation
                                                                        [39]. Specifically, we perform a grid search on a list of val-
after each convolution.
                                                                        ues {1.2, 1.25, 1.3, 1.35, 1.4, 1.45}, and pick the best value
                                                                        1.35 as the BiFPN width scaling factor. Formally, BiFPN
4. EfficientDet                                                         width and depth are scaled with the following equation:
                                                                                Wbif pn = 64 · 1.35φ ,
                                                                                                       
   Based on our BiFPN, we have developed a new family                                                          Dbif pn = 3 + φ (1)
of detection models named EfficientDet. In this section, we
will discuss the network architecture and a new compound                Box/class prediction network – we fix their width to be
scaling method for EfficientDet.                                        always the same as BiFPN (i.e., Wpred = Wbif pn ), but lin-

                                                                    4
                      P7 / 128
                                                                                                          Class prediction net

                   P6 / 64                                                                                  conv          conv

               P5 / 32

                                                                                                            conv          conv
            P4 / 16
                                                                                                          Box prediction net

          P3 / 8

    P2 / 4                                         BiFPN Layer

  P1 / 2
  Input
                      EfficientNet backbone

Figure 3: EfficientDet architecture – It employs EfficientNet [39] as the backbone network, BiFPN as the feature network,
and shared class/box prediction network. Both BiFPN layers and class/box net layers are repeated multiple times based on
different resource constraints as shown in Table 1.

early increase the depth (#layers) using equation:                                  Input    Backbone         BiFPN              Box/class
                                                                                     size    Network    #channels #layers         #layers
                       Dbox = Dclass = 3 + bφ/3c           (2)                      Rinput               Wbif pn   Dbif pn        Dclass
                                                                       D0 (φ = 0)   512        B0          64         3             3
                                                                       D1 (φ = 1)   640        B1          88         4             3
Input image resolution – Since feature level 3-7 are used              D2 (φ = 2)   768        B2         112         5             3
in BiFPN, the input resolution must be dividable by 27 =               D3 (φ = 3)   896        B3         160         6             4
128, so we linearly increase resolutions using equation:               D4 (φ = 4)   1024       B4         224         7             4
                                                                       D5 (φ = 5)   1280       B5         288         7             4
                          Rinput = 512 + φ · 128           (3)         D6 (φ = 6)   1280       B6         384         8             5
                                                                       D7 (φ = 7)   1536       B6         384         8             5
                                                                       D7x          1536       B7         384         8             5
Following Equations 1,2,3 with different φ, we have devel-
oped EfficientDet-D0 (φ = 0) to D7 (φ = 7) as shown
                                                                     Table 1: Scaling configs for EfficientDet D0-D6 – φ is
in Table 1, where D7 and D7x have the same BiFPN and
                                                                     the compound coefficient that controls all other scaling di-
head, but D7 uses higher resolution and D7x uses larger
                                                                     mensions; BiFPN, box/class net, and input size are scaled
backbone network and one more feature level (from P3 to
                                                                     up using equation 1, 2, 3 respectively.
P8 ). Notably, our compound scaling is heuristic-based and
might not be optimal, but we will show that this simple scal-
ing method can significantly improve efficiency than other
single-dimension scaling methods in Figure 6.                        2}. During training, we apply horizontal flipping and scale
                                                                     jittering [0.1, 2.0], which randomly rsizes images between
5. Experiments                                                       0.1x and 2.0x of the original size before cropping. We ap-
                                                                     ply soft-NMS [3] for eval. For D0-D6, each model is trained
5.1. EfficientDet for Object Detection                               for 300 epochs with total batch size 128 on 32 TPUv3 cores,
    We evaluate EfficientDet on COCO 2017 detection                  but to push the envelope, we train D7/D7x for 600 epochs
datasets [25] with 118K training images. Each model                  on 128 TPUv3 cores.
is trained using SGD optimizer with momentum 0.9 and                     Table 2 compares EfficientDet with other object de-
weight decay 4e-5. Learning rate is linearly increased from          tectors, under the single-model single-scale settings with
0 to 0.16 in the first training epoch and then annealed down         no test-time augmentation. We report accuracy for both
using cosine decay rule. Synchronized batch norm is added            test-dev (20K test images with no public ground-truth)
after every convolution with batch norm decay 0.99 and ep-           and val with 5K validation images. Notably, model perfor-
silon 1e-3. Same as the [39], we use SiLU (Swish-1) ac-              mance depends on both network architecture and trainning
tivation [8, 15, 31] and exponential moving average with             settings (see appendix), but for simplicity, we only repro-
decay 0.9998. We also employ commonly-used focal loss                duce RetinaNet using our trainers and refer other models
[24] with α = 0.25 and γ = 1.5, and aspect ratio {1/2, 1,            from their papers. In general, our EfficientDet achieves bet-

                                                                 5
                                                   test-dev        val                                               Latency (ms)
 Model                                      AP       AP50 AP75     AP      Params    Ratio   FLOPs     Ratio   TitianV        V100
 EfficientDet-D0 (512)                      34.6     53.0   37.1   34.3      3.9M     1x       2.5B     1x        12          10.2
 YOLOv3 [34]                                33.0     57.9   34.4    -            -     -       71B     28x         -           -
 EfficientDet-D1 (640)                      40.5     59.1   43.7   40.2      6.6M     1x        6.1B    1x        16          13.5
 RetinaNet-R50 (640) [24]                   39.2     58.0   42.3   39.2       34M    6.7x       97B    16x        25           -
 RetinaNet-R101 (640)[24]                   39.9     58.5   43.0   39.8       53M    8.0x      127B    21x        32           -
 EfficientDet-D2 (768)                      43.9     62.7   47.6   43.5     8.1M      1x        11B     1x        23          17.7
 Detectron2 Mask R-CNN R101-FPN [1]          -        -      -     42.9      63M     7.7x      164B    15x         -          56‡
 Detectron2 Mask R-CNN X101-FPN [1]          -        -      -     44.3     107M     13x       277B    25x         -          103‡
 EfficientDet-D3 (896)                      47.2     65.9   51.2   46.8      12M      1x       25B     1x         37          29.0
 ResNet-50 + NAS-FPN (1024) [10]            44.2      -      -      -        60M     5.1x     360B     15x        64           -
 ResNet-50 + NAS-FPN (1280) [10]            44.8      -      -      -        60M     5.1x     563B     23x        99           -
 ResNet-50 + NAS-FPN (1280@384)[10]         45.4      -      -      -       104M     8.7x    1043B     42x       150           -
 EfficientDet-D4 (1024)                     49.7     68.4   53.9   49.3      21M      1x       55B     1x         65          42.8
 AmoebaNet+ NAS-FPN +AA(1280)[45]            -        -      -     48.6     185M     8.8x    1317B     24x       246           -
 EfficientDet-D5 (1280)                     51.5     70.5   56.1   51.3      34M      1x       135B     1x       128          72.5
 Detectron2 Mask R-CNN X152 [1]              -        -      -     50.2         -      -           -     -        -           234‡
 EfficientDet-D6 (1280)                     52.6     71.5   57.2   52.2      52M      1x      226B     1x        169          92.8
 AmoebaNet+ NAS-FPN +AA(1536)[45]            -        -      -     50.7     209M     4.0x    3045B     13x       489           -
 EfficientDet-D7 (1536)                     53.7 72.4         58.4 53.4        52M              325B                232          122
 EfficientDet-D7x (1536)                    55.1 74.3         59.9 54.4        77M              410B                285          153
 We omit ensemble and test-time multi-scale results [30, 12]. RetinaNet APs are reproduced with our trainer and others are from papers.
 ‡
   Latency numbers with ‡ are from detectron2, and others are measured on the same machine (TensorFlow2.1 + CUDA10.1, no TensorRT).

Table 2: EfficientDet performance on COCO [25] – Results are for single-model single-scale. test-dev is the COCO
test set and val is the validation set. Params and FLOPs denote the number of parameters and multiply-adds. Latency is
for inference with batch size 1. AA denotes auto-augmentation [45]. We group models together if they have similar accuracy,
and compare their model size, FLOPs, and latency in each group.

ter efficiency than previous detectors, being 4x – 9x smaller          they are also efficient on real-world hardware.
and using 13x - 42x less FLOPs across a wide range of ac-
curacy or resource constraints. On relatively low-accuracy             5.2. EfficientDet for Semantic Segmentation
regime, our EfficientDet-D0 achieves similar accuracy as
YOLOv3 with 28x fewer FLOPs. Compared to RetinaNet                         While our EfficientDet models are mainly designed for
[24] and Mask-RCNN [13], our EfficientDet achieves simi-               object detection, we are also interested in their performance
lar accuracy with up to 8x fewer parameters and 21x fewer              on other tasks such as semantic segmentation. Following
FLOPs. On high-accuracy regime, our EfficientDet also                  [19], we modify our EfficientDet model to keep feature
consistently outperforms recent object detectors [10, 45]              level {P 2, P 3, ..., P 7} in BiFPN, but only use P 2 for the
with much fewer parameters and FLOPs. In particular,                   final per-pixel classification. For simplicity, here we only
our single-model single-scale EfficientDet-D7x achieves a              evaluate a EfficientDet-D4 based model, which uses a Ima-
new state-of-the-art 55.1 AP on test-dev, outperform-                  geNet pretrained EfficientNet-B4 backbone (similar size to
ing prior art by a large margin in both accuracy (+4 AP) and           ResNet-50). We set the channel size to 128 for BiFPN and
efficiency (7x fewer FLOPs).                                           256 for classification head. Both BiFPN and classification
    In addition, we have also compared the inference latency           head are repeated by 3 times.
on Titan-V FP32 , V100 GPU FP16, and single-thread CPU.                    Table 3 shows the comparison between our models
Notably, our V100 latency is end-to-end including prepro-              and previous DeepLabV3+ [6] on Pascal VOC 2012 [9].
cessing and NMS postprocessing. Figure 4 illustrates the               Notably, we exclude those results with ensemble, test-
comparison on model size and GPU/CPU latency. For fair                 time augmentation, or COCO pretraining. Under the
comparison, these figures only include results that are mea-           same single-model single-scale settings, our model achieves
sured on the same machine with the same settings. Com-                 1.7% better accuracy with 9.8x fewer FLOPs than the prior
pared to previous detectors, EfficientDet models are up to             art of DeepLabV3+ [6]. These results suggest that Efficient-
4.1x faster on GPU and 10.8x faster on CPU, suggesting                 Det is also quite promising for semantic segmentation.

                                                                   6
          52.5                                                                               52                                                                         52
                                     EfficientDet-D6                                                                  EfficientDet-D6                                                        EfficientDet-D6
          50.0                 D5                                            AN              50                  D5                                      AN             50              D5                                                  AN

                          D4                                                                              D4                                                                      D4
          47.5                                                                               48                                                                         48
                                                   ResNet + NAS-FPN
          45.0        D3                                                                     46                      ResNet + NAS-FPN                                   46                           ResNet + NAS-FPN

                                                                                                                                                              COCO AP
                                                                                   COCO AP
COCO AP

                                                                                                     D3                                                                          D3

          42.5       D2                                                                      44                                                                         44
                                                                                                    D2                                          LAT Ratio                        D2                                               LAT Ratio
                                     RetinaNet                    Params Ratio
          40.0                                                                               42                        EfficientDet-D1           16ms                   42
                     D1 Mask R-CNN EfficientDet-D1           7M                                                                                                                                          EfficientDet-D1          0.74s
                                   RetinaNet [24]            53M 8.0x                                    RetinaNet     RetinaNet [24]            32ms 2.0x                             RetinaNet         RetinaNet [24]            3.6s 4.9x
          37.5                     EfficientDet-D3           12M                             40                        EfficientDet-D3           37ms                   40                               EfficientDet-D3           2.5s
                                   ResNet + NASFPN [10]     104M 8.7x                               D1                 ResNet + NASFPN [10]     150ms 4.1x                   D1                          ResNet + NASFPN [10]      27s 11x
                                                                                                                       EfficientDet-D6          169ms                                                    EfficientDet-D6           16s
          35.0                     EfficientDet-D6           52M                             38                                                                         38
                                   AmoebaNet + NAS-FPN [45] 209M 4.0x                                                  AmoebaNet + NAS-FPN [45] 489ms 2.9x                                               AmoebaNet + NAS-FPN [45] 83s 5.2x
                     D0
                 0                  50         100         150         200                    0.0          0.1          0.2       0.3        0.4        0.5                  0                20           40           60             80
                                            Parameters (M)                                                              GPU latency (s)                                                                 CPU latency (s)

                                    (a) Model Size                                                             (b) GPU Latency                                                                 (c) CPU Latency
Figure 4: Model size and inference latency comparison – Latency is measured with batch size 1 on the same machine
equipped with a Titan V GPU and Xeon CPU. AN denotes AmoebaNet + NAS-FPN trained with auto-augmentation [45].
Our EfficientDet models are 4x - 9x smaller, 2x - 4x faster on GPU, and 5x - 11x faster on CPU than other detectors.

          Model                                                   mIOU            Params                 FLOPs                                                                                AP         Parameters            FLOPs
          DeepLabV3+ (ResNet-101) [6]                            79.35%              -                   298B                           ResNet50 + FPN                                       37.0              34M               97B
          DeepLabV3+ (Xception) [6]                              80.02%              -                   177B
                                                                                                                                        EfficientNet-B3 + FPN                                40.3              21M               75B
          Our EfficientDet†                                      81.74%            17M                   18B
           †
                                                                                                                                        EfficientNet-B3 + BiFPN                              44.4              12M               24B
               A modified version of EfficientDet-D4.

Table 3: Performance comparison on Pascal VOC se-                                                                                Table 4: Disentangling backbone and BiFPN – Starting
mantic segmentation.                                                                                                             from the standard RetinaNet (ResNet50+FPN), we first re-
                                                                                                                                 place the backbone with EfficientNet-B3, and then replace
6. Ablation Study                                                                                                                the baseline FPN with our proposed BiFPN.

   In this section, we ablate various design choices for our
                                                                                                                                 times and replace all convs with depthwise separable convs,
proposed EfficientDet. For simplicity, all accuracy results
                                                                                                                                 which is the same as BiFPN. We use the same backbone and
here are for COCO validation set.
                                                                                                                                 class/box prediction network, and the same training settings
6.1. Disentangling Backbone and BiFPN                                                                                            for all experiments. As we can see, the conventional top-
                                                                                                                                 down FPN is inherently limited by the one-way informa-
   Since EfficientDet uses both a powerful backbone and a                                                                        tion flow and thus has the lowest accuracy. While repeated
new BiFPN, we want to understand how much each of them                                                                           FPN+PANet achieves slightly better accuracy than NAS-
contributes to the accuracy and efficiency improvements.                                                                         FPN [10], it also requires more parameters and FLOPs. Our
Table 4 compares the impact of backbone and BiFPN us-                                                                            BiFPN achieves similar accuracy as repeated FPN+PANet,
ing RetinaNet training settings. Starting from a RetinaNet                                                                       but uses much less parameters and FLOPs. With the addi-
detector [24] with ResNet-50 [14] backbone and top-down                                                                          tional weighted feature fusion, our BiFPN further achieves
FPN [23], we first replace the backbone with EfficientNet-                                                                       the best accuracy with fewer parameters and FLOPs.
B3, which improves accuracy by about 3 AP with slightly
less parameters and FLOPs. By further replacing FPN with                                                                         6.3. Softmax vs Fast Normalized Fusion
our proposed BiFPN, we achieve additional 4 AP gain with
much fewer parameters and FLOPs. These results suggest                                                                              As discussed in Section 3.3, we propose a fast normal-
that EfficientNet backbones and BiFPN are both crucial for                                                                       ized feature fusion approach to get ride of the expensive
our final models.                                                                                                                softmax while retaining the benefits of normalized weights.
                                                                                                                                 Table 6 compares the softmax and fast normalized fusion
6.2. BiFPN Cross-Scale Connections                                                                                               approaches in three detectors with different model sizes. As
    Table 5 shows the accuracy and model complexity for                                                                          shown in the results, our fast normalized fusion approach
feature networks with different cross-scale connections                                                                          achieves similar accuracy as the softmax-based fusion, but
listed in Figure 2. Notably, the original FPN [23] and                                                                           runs 1.26x - 1.31x faster on GPUs.
PANet [26] only have one top-down or bottom-up flow, but                                                                            In order to further understand the behavior of softmax-
for fair comparison, here we repeat each of them multiple                                                                        based and fast normalized fusion, Figure 5 illustrates the

                                                                                                                           7
                                                                                           0.5

                                                                       Input1 weight (%)
Input1 weight (%)

                                                                                                                                                        Input1 weight (%)
                                                                                                                                           softmax                          0.525
                    0.50                                                                                                                   fast
                                                                                           0.4
                                                                                                                                                                            0.500
                    0.45
                                                         softmax
                                                                                           0.3                                                                              0.475                                             softmax
                                                         fast                                                                                                                                                                 fast
                    0.40                                                                   0.2                                                                              0.450
                           0    25000   50000   75000   100000                                   0      25000   50000     75000           100000                                    0     25000     50000        75000   100000
                               (a) Example Node 1                                                      (b) Example Node 2                                                               (c) Example Node 3
Figure 5: Softmax vs. fast normalized feature fusion – (a) - (c) shows normalized weights (i.e., importance) during training
for three representative nodes; each node has two inputs (input1 & input2) and their normalized weights always sum up to 1.

                                                                   #Params                       #FLOPs                              46
                                                        AP
                                                                     ratio                        ratio                              44

                Repeated top-down FPN               42.29           1.0x                             1.0x
                                                                                                                                     42
                Repeated FPN+PANet                  44.08           1.0x                             1.0x

                                                                                                                           COCO AP
                NAS-FPN                             43.16           0.71x                            0.72x                           40
                Fully-Connected FPN                 43.06           1.24x                            1.21x
                                                                                                                                     38
                BiFPN (w/o weighted)                43.94           0.88x                            0.67x
                BiFPN (w/ weighted)                 44.39           0.88x                            0.68x                                                                                         Compound Scaling
                                                                                                                                     36
                                                                                                                                                                                                   Scale by image size
                                                                                                                                                                                                   Scale by #channels
                                                                                                                                     34                                                            Scale by #BiFPN layers
Table 5: Comparison of different feature networks – Our                                                                                                                                            Scale by #box/class layers
weighted BiFPN achieves the best accuracy with fewer pa-                                                                                           10               20               30       40            50           60
rameters and FLOPs.                                                                                                                                                                 FLOPs (B)

                                 Softmax Fusion          Fast Fusion                                                    Figure 6: Comparison of different scaling methods –
                Model                                                                            Speedup                compound scaling achieves better accuracy and efficiency.
                                      AP                 AP (delta)
                Model1                  33.96            33.85 (-0.11)                            1.28x
                Model2                  43.78            43.77 (-0.01)                            1.26x                 ing from the same baseline detector, our compound scaling
                Model3                  48.79            48.74 (-0.05)                            1.31x                 method achieves better efficiency than other methods, sug-
                                                                                                                        gesting the benefits of jointly scaling by better balancing
                                                                                                                        difference architecture dimensions.
Table 6: Comparison of different feature fusion – Our
fast fusion achieves similar accuracy as softmax-based fu-
sion, but runs 28% - 31% faster.
                                                                                                                        7. Conclusion
                                                                                                                           In this paper, we systematically study network architec-
learned weights for three feature fusion nodes randomly se-                                                             ture design choices for efficient object detection, and pro-
lected from the BiFPN layers in EfficientDet-D3.     Notably,                                                           pose a weighted bidirectional feature network and a cus-
                                   wi                                                                                   tomized compound scaling method, in order to improve ac-
                                        P wj
the normalized weights (e.g.,    e    /   j e   for softmax-
                                                                                                                        curacy and efficiency. Based on these optimizations, we de-
                            P
based fusion, and wi /( + j wj ) for fast normalized fu-
sion) always sum up to 1 for all inputs. Interestingly, the                                                             velop a new family of detectors, named EfficientDet, which
normalized weights change rapidly during training, sug-                                                                 consistently achieve better accuracy and efficiency than the
gesting different features contribute to the feature fusion                                                             prior art across a wide spectrum of resource constraints. In
unequally. Despite the rapid change, our fast normalized                                                                particular, our scaled EfficientDet achieves state-of-the-art
fusion approach always shows very similar learning behav-                                                               accuracy with much fewer parameters and FLOPs than pre-
ior to the softmax-based fusion for all three nodes.                                                                    vious object detection and semantic segmentation models.

6.4. Compound Scaling                                                                                                   Acknowledgements
   As discussed in section 4.2, we employ a compound                                                                       Special thanks to Golnaz Ghiasi, Adams Yu, Daiyi
scaling method to jointly scale up all dimensions of                                                                    Peng for their help on infrastructure and discussion. We
depth/width/resolution for backbone, BiFPN, and box/class                                                               also thank Adam Kraft, Barret Zoph, Ekin D. Cubuk,
prediction networks. Figure 6 compares our compound                                                                     Hongkun Yu, Jeff Dean, Pengchong Jin, Samy Bengio,
scaling with other alternative methods that scale up a sin-                                                             Reed Wanderman-Milne, Tsung-Yi Lin, Xianzhi Du, Xi-
gle dimension of resolution/depth/width. Although start-                                                                aodan Song, Yunxing Dai, and the Google Brain team. We

                                                                                                                8
thank the open source community for the contributions.                  [19] Alexander Kirillov, Ross Girshick, Kaiming He, and Piotr
                                                                             Dollr. Panoptic feature pyramid networks. CVPR, 2019. 6
References                                                              [20] Tao Kong, Fuchun Sun, Chuanqi Tan, Huaping Liu, and
                                                                             Wenbing Huang. Deep feature pyramid reconfiguration for
 [1] Detectron2. https://github.com/facebookresearch/                        object detection. ECCV, 2018. 2, 3
     detectron2. Accessed: 05/01/2020. 6, 10
                                                                        [21] Hei Law and Jia Deng. Cornernet: Detecting objects as
 [2] Md Amirul Islam, Mrigank Rochan, Neil DB Bruce, and                     paired keypoints. ECCV, 2018. 1, 2
     Yang Wang. Gated feedback refinement network for dense
                                                                        [22] Hanchao Li, Pengfei Xiong, Jie An, and Lingxue Wang.
     image labeling. CVPR, pages 3751–3759, 2017. 2
                                                                             Pyramid attention networks. BMVC, 2018. 3
 [3] Navaneeth Bodla, Bharat Singh, Rama Chellappa, and
                                                                        [23] Tsung-Yi Lin, Piotr Dollár, Ross Girshick, Kaiming He,
     Larry S Davis. Soft-nms–improving object detection with
                                                                             Bharath Hariharan, and Serge Belongie. Feature pyramid
     one line of code. ICCV, pages 5561–5569, 2017. 5
                                                                             networks for object detection. CVPR, 2017. 1, 2, 3, 4, 7
 [4] Zhaowei Cai, Quanfu Fan, Rogerio S Feris, and Nuno Vas-
                                                                        [24] Tsung-Yi Lin, Piotr Dollár, Ross Girshick, Kaiming He,
     concelos. A unified multi-scale deep convolutional neural
                                                                             Bharath Hariharan, and Serge Belongie. Focal loss for dense
     network for fast object detection. ECCV, pages 354–370,
                                                                             object detection. ICCV, 2017. 1, 2, 4, 5, 6, 7, 10
     2016. 2
                                                                        [25] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,
 [5] Zhaowei Cai and Nuno Vasconcelos. Cascade r-cnn: Delving
                                                                             Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence
     into high quality object detection. CVPR, pages 6154–6162,
                                                                             Zitnick. Microsoft COCO: Common objects in context.
     2018. 2
                                                                             ECCV, 2014. 2, 5, 6
 [6] Liang-Chieh Chen, Yukun Zhu, George Papandreou, Flo-
     rian Schroff, and Hartwig Adam. Encoder-decoder with               [26] Shu Liu, Lu Qi, Haifang Qin, Jianping Shi, and Jiaya Jia.
     atrous separable convolution for semantic image segmenta-               Path aggregation network for instance segmentation. CVPR,
     tion. ECCV, 2018. 2, 6, 7                                               2018. 2, 3, 7
 [7] François Chollet. Xception: Deep learning with depthwise          [27] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian
     separable convolutions. CVPR, pages 1610–02357, 2017. 4                 Szegedy, Scott Reed, Cheng-Yang Fu, and Alexander C
 [8] Stefan Elfwing, Eiji Uchibe, and Kenji Doya. Sigmoid-                   Berg. SSD: Single shot multibox detector. ECCV, 2016.
     weighted linear units for neural network function approxima-            1, 2, 4
     tion in reinforcement learning. Neural Networks, 107:3–11,         [28] Zhuang Liu, Mingjie Sun, Tinghui Zhou, Gao Huang, and
     2018. 5                                                                 Trevor Darrell. Rethinking the value of network pruning.
 [9] Mark Everingham, S. M. Ali Eslami, Luc Van Gool, Christo-               ICLR, 2019. 1
     pher K. I. Williams, John Winn, and Andrew Zisserman. The          [29] Jonathan Pedoeem and Rachel Huang. Yolo-lite: a real-time
     pascal visual object classes challenge: A retrospective. In-            object detection algorithm optimized for non-gpu computers.
     ternational Journal of Computer Vision, 2015. 6                         arXiv preprint arXiv:1811.05588, 2018. 1
[10] Golnaz Ghiasi, Tsung-Yi Lin, Ruoming Pang, and Quoc V.             [30] Chao Peng, Tete Xiao, Zeming Li, Yuning Jiang, Xiangyu
     Le. Nas-fpn: Learning scalable feature pyramid architecture             Zhang, Kai Jia, Gang Yu, and Jian Sun. Megdet: A large
     for object detection. CVPR, 2019. 2, 3, 4, 6, 7                         mini-batch object detector, 2018. 6
[11] Ross Girshick. Fast r-cnn. ICCV, 2015. 2                           [31] Prajit Ramachandran, Barret Zoph, and Quoc V Le. Search-
[12] Kaiming He, Ross Girshick, and Piotr Dollár. Rethinking                ing for activation functions. ICLR workshop, 2018. 5
     imagenet pre-training. ICCV, 2019. 6, 10                           [32] Esteban Real, Alok Aggarwal, Yanping Huang, and Quoc V
[13] Kaiming He, Georgia Gkioxari, Piotr Dollár, and Ross Gir-              Le. Regularized evolution for image classifier architecture
     shick. Mask r-cnn. ICCV, pages 2980–2988, 2017. 2, 6                    search. AAAI, 2019. 2, 4
[14] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.             [33] Joseph Redmon and Ali Farhadi. Yolo9000: better, faster,
     Deep residual learning for image recognition. CVPR, pages               stronger. CVPR, 2017. 1, 2, 4
     770–778, 2016. 1, 2, 7                                             [34] Joseph Redmon and Ali Farhadi. Yolov3: An incremental
[15] Dan Hendrycks and Kevin Gimpel. Gaussian error linear                   improvement. arXiv preprint arXiv:1804.02767, 2018. 1, 2,
     units (gelus). arXiv preprint arXiv:1606.08415, 2016. 5                 6
[16] Andrew Howard, Mark Sandler, Grace Chu, Liang-Chieh                [35] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.
     Chen, Bo Chen, Mingxing Tan, Weijun Wang, Yukun Zhu,                    Faster r-cnn: Towards real-time object detection with region
     Ruoming Pang, Vijay Vasudevan, Quoc V. Le, and Hartwig                  proposal networks. NIPS, 2015. 2
     Adam. Searching for mobilenetv3. ICCV, 2019. 2                     [36] Pierre Sermanet, David Eigen, Xiang Zhang, Michaël Math-
[17] Jonathan Huang, Vivek Rathod, Chen Sun, Menglong Zhu,                   ieu, Rob Fergus, and Yann LeCun. Overfeat: Integrated
     Anoop Korattikara, Alireza Fathi, Ian Fischer, Zbigniew Wo-             recognition, localization and detection using convolutional
     jna, Yang Song, Sergio Guadarrama, et al. Speed/accuracy                networks. ICLR, 2014. 2
     trade-offs for modern convolutional object detectors. CVPR,        [37] Laurent Sifre. Rigid-motion scattering for image classifica-
     2017. 2                                                                 tion. Ph.D. thesis section 6.2, 2014. 4
[18] Seung-Wook Kim, Hyong-Keun Kook, Jee-Young Sun,                    [38] Mingxing Tan, Bo Chen, Ruoming Pang, Vijay Vasudevan,
     Mun-Cheon Kang, and Sung-Jea Ko. Parallel feature pyra-                 and Quoc V Le. Mnasnet: Platform-aware neural architec-
     mid network for object detection. ECCV, 2018. 2, 3                      ture search for mobile. CVPR, 2019. 2

                                                                    9
[39] Mingxing Tan and Quoc V. Le. Efficientnet: Rethinking                            size; (3) compared to the default 37 AP [24], our reproduced
     model scaling for convolutional neural networks. ICML,                           RetinaNet achieves higher accuracy (+2AP) using our train-
     2019. 1, 2, 4, 5                                                                 ing settings. In this paper, we mainly use 300 epochs for the
[40] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. Fcos:                             good trade-off between accuracy and training time.
     Fully convolutional one-stage object detection. ICCV, 2019.
     1
                                                                                      Scale Jittering: A common training-time augmentation
[41] Saining Xie, Ross Girshick, Piotr Dollár, Zhuowen Tu, and
     Kaiming He. Aggregated residual transformations for deep
                                                                                      is to first resize images and then crop them into fixed size,
     neural networks. CVPR, pages 5987–5995, 2017. 2, 4                               known as scale jitterinig. Previous object detectors often
[42] Qijie Zhao, Tao Sheng, Yongtao Wang, Zhi Tang, Ying Chen,                        use small jitters such as [0.8, 1.2], which randomly sample a
     Ling Cai, and Haibin Ling. M2det: A single-shot object de-                       scaling size between 0.8x to 1.2x of the original image size.
     tector based on multi-level feature pyramid network. AAAI,                       However, we observe large jitters can improve accuracy if
     2019. 2, 3                                                                       training longer. Figure 8 shows the results for different jit-
[43] Peng Zhou, Bingbing Ni, Cong Geng, Jianguo Hu, and Yi                            ters: (1) when training with 30 epochs, a small jitter like
     Xu. Scale-transferrable object detection. CVPR, pages 528–                       [0.8, 1.2] performs quite good, and large jitters like [0.1,
     537, 2018. 2                                                                     2.0] actually hurts accuracy; (2) when training with 300
[44] Xingyi Zhou, Dequan Wang, and Philipp Krhenbhl. Objects                          epochs, large jitters consistently improve accuracy, perhaps
     as points. arXiv:1904.07850, 2019. 1, 2                                          due to the stronger regularization. This paper uses a large
[45] Barret Zoph, Ekin D. Cubuk, Golnaz Ghiasi, Tsung-Yi Lin,                         jitter [0.1, 2.0] for all models.
     Jonathon Shlens, and Quoc V. Le. Learning data aug-                                                                                                                          40.2
     mentation strategies for object detection. arXiv preprint                                         40                                                    39.1
     arXiv:1804.02767, 2019. 1, 2, 6, 7                                                                                             38.1
                                                                                                       38
                                                                                         COCO val AP          36.8

Appendix                                                                                               36                                                    35.3
                                                                                                                                    34.7                                          34.6
                                                                                                       34
1.1. Hyperparameters                                                                                          32.2
                                                                                                       32                                           EfficientDet-D1 (300 epochs)
    Neural network architecture and training hyperparamters                                                                                         EfficientDet-D1 (30 epochs)
are both crucial for object detection. Here we ablate two                                              30
                                                                                                            no-jitter         jitter[0.8, 1.2]        jitter[0.5, 1.5]      jitter[0.1, 2.0]
important hyperparamters: training epochs and multi-scale
                                                                                                                  Figure 8: Accuracy vs. Scale Jittering.
jittering, using RetinaNet-R50 and our EfficientDet-D1. All
other hyperparameters are kept the same as section 5.                                 1.2. Image Resolutions
                                                                         40.5            In addition to our compound scaling that progres-
                                                    40.2
                 40                                                                   sively increases image sizes, we are also interested in the
                                                                          39.5        accuracy-latency trade-offs with fixed image resolutions.
                                                     39.2
   COCO val AP

                                  38.2
                 38                                                                   Figure 9 compares EfficientDet-D1 to D6 with fixed and
                                   37.9
                                                                                      scaled resolutions. Surprisingly, their accuracy-latency
                 36
                      35.5                                                            trade-offs are very similar even though they have very
                                                             EfficientDet-D1          different preferences: under similar accuracy constraints,
                       34.6                                  RetinaNet-R50
                                                                                      models with fixed resolutions require much more param-
                 34
                      30           90                300                 600          eters, but less activations and peak memory usage, than
                                 Number of training epochs
                                                                                      those with scaled resolutions. With fixed 640x640, our
                      Figure 7: Accuracy vs. Training Epochs.                         EfficientDet-D6 achieves real-time 47.9AP at 34ms latency.
                                                                                                       50                                                                         D4(1024)

Training Epochs: Many previous work only use a small                                                   48                                          D3(896)
number of epochs: for example, Detectron2 [1] trains each                                                                                                       D6(640)
                                                                                         COCO val AP

                                                                                                       46                                        D5(640)
model with 12 epochs (1x schedule) in default, and at most                                                                         D4(640)
                                                                                                                        D2(768)
110 epochs (9x scahedule). Recent work [12] shows train-                                               44
                                                                                                                            D3(640)
ing longer is not helpful if using pretrained backbone net-                                            42
works; however, we observe training longer can signifi-                                                40
                                                                                                                  D2(640)                                           Scaled resolution
                                                                                                                D1(640)                                             Fixed resolution
ciantly improve accuracy in our settings. Figure 7 shows
                                                                                                       38
the performance comparison for different training epochs.                                                         15          20       25      30        35                  40
We obseve: (1) both models benefit from longer training                                                                            V100 GPU Latency (ms)

until reaching 300 epochs; (2) longer training is particularly                        Figure 9: Comparison for Fixed and Scaled Resolution – fixed
important for EfficientDet, perhaps due to its small model                            denotes 640x640 size and scaled denotes increased sizes.

                                                                                 10
