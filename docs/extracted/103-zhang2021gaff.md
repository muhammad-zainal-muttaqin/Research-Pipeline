---
source_id: 103
bibtex_key: zhang2021gaff
title: Guided Attentive Feature Fusion for Multispectral Pedestrian Detection
year: 2021
domain_theme: Pedestrian RGB-T
verified_pdf: 103_GAFF.pdf
char_count: 68554
---

Guided Attentive Feature Fusion for Multispectral Pedestrian Detection

           Heng ZHANG1,3 , Elisa FROMONT1,4 , Sébastien LEFEVRE2 and Bruno AVIGNON3
                 1
                   Univ Rennes 1, IRISA, France 2 Univ Bretagne Sud, IRISA, France
                             3
                               ATERMES company, France 4 IUF, Inria.

                          Abstract

    Multispectral image pairs can provide complementary
visual information, making pedestrian detection systems                                              Thermal feature
                                                                                                       extraction
more robust and reliable. To benefit from both RGB and
                                                                         Multispectral image pairs                                           Joint detection results
                                                                                                         Multispectral
thermal IR modalities, we introduce a novel attentive mul-                                              feature fusion
tispectral feature fusion approach. Under the guidance of                                                                   Pedestrian
                                                                                                                         detection network
the inter- and intra-modality attention modules, our deep
learning architecture learns to dynamically weigh and fuse
                                                                                                     Visible feature
the multispectral features. Experiments on two public multi-                                           extraction

spectral object detection datasets demonstrate that the pro-
posed approach significantly improves the detection accu-
racy at a low computation cost.                                      Figure 1: Multispectral pedestrian detection via a two-
                                                                     stream convolutional neural network.

1. Introduction
    Real world pedestrian detection applications require
accurate detection performance under various conditions,
such as darkness, rain, fog, etc. In these conditions, it is dif-
ficult to perform precise detection using only standard RGB
cameras. Instead, multispectral systems try to combine the
information coming from e.g. thermal and visible cameras
to improve the reliability of the detections.
    Deep learning-based methods, more specifically, two-
stream convolutional neural networks, nowadays largely
dominate the field of multispectral pedestrian detection
[6, 9, 10, 11, 14, 18, 19, 20]. As illustrated in Fig. 1, a
typical two-stream pedestrian detection network consists of
two separate spectra-specific feature extraction branches, a         Figure 2: Typical examples of thermal-visible image pairs
multispectral feature fusion module and a pedestrian detec-          captured during the day (first two rows) and night (bottom
tion network operating on the fused features. The system             row). For each pair, the thermal image is on the left and the
uses some aligned thermal-visible image pairs as input and           RGB image is on the right.
outputs the joint detection results on each image pair.
    Thermal and visible cameras have different imaging
characteristics under different conditions. As shown in              age the information from the most relevant modality.
Fig. 2, visible cameras provide precise visual details (such             An intuitive solution to adapt the feature fusion to the
as color and texture) in a well-lit environment, while ther-         different weather and lighting conditions is to manually
mal cameras are sensitive to temperature changes, which              identify multiple usage scenarios and design a specific so-
is extremely useful for nighttime or shadow detection. An            lution for each scenario. For example, [6] proposes an
adaptive fusion of thermal and visible features should take          illumination-aware network consisting of a day illumina-
such differences into account, and should identify and lever-        tion sub-network and a night illumination sub-network. The

                                                                    72
detection results from the two sub-networks are then fused         fusion architecture is superior to the early one and the tra-
according to the prediction of the illumination context.           ditional ACF method [4]. This late-stage fusion architec-
Such a kind of hand-crafted fusion mechanism improves              ture can be regarded as a prototype of a two-stream neural
the resilience of the model to a certain extent, nonetheless,      network, in which multispectral features are fused through
there are still two limitations: firstly, cherry-picked scenar-    concatenation operations. Both [14] and [9] adapted Faster
ios may not cover all conditions, e.g., different illumina-        R-CNN [16] to a two-stream network architecture for multi-
tion/season/weather conditions; Secondly, the situation may        spectral pedestrian detection. They compare different mul-
be completely different even in the same usage scenario,           tispectral fusion stages and came to the conclusion that
e.g., at nighttime, lighting conditions in urban areas are dif-    the fusion in the middle stage outperforms the fusion in
ferent from those in rural areas.                                  the early or late stage. Based on this, MSDS-RCNN [10]
    In this paper, we propose a novel and fully adaptive mul-      adopted a two-stream middle-level fusion architecture and
tispectral feature fusion approach, named Guided Attentive         combined the pedestrian detection task and the semantic
Feature Fusion (GAFF). By combining the intra- and inter-          segmentation task to further improve the detection accuracy.
modality attention modules, the proposed approach allows
the network to learn the adaptive weighing and fusion of           2.2. Adaptive multispectral feature fusion
multispectral features. These two attention mechanisms are
guided by the prediction and comparison of the pedestrian              As mentioned in Section 1, thermal and visible cameras
masks in the multispectral feature fusion stage. Specifically,     have different imaging characteristics and the adaptive mul-
at each spatial position, thermal or visible features are en-      tispectral fusion can improve the resilience and the detec-
hanced when they are located in the area of a pedestrian           tion accuracy of the system. This has become the main
(intra-modality attention) or when they possess a higher           focus of the multispectral pedestrian detection research in
quality than in the other modality (inter-modality attention).     recent years. Both [11] and [6] use the illumination infor-
To the best of our knowledge, GAFF is the first work that          mation as a clue for the adaptive fusion: they train a separate
regards the multispectral feature fusion as a sub-task in the      network to estimate the illumination value from a given im-
network optimization and that introduces a specific guid-          age pair, then [11] uses the predicted illumination value to
ance in this task to improve the multispectral pedestrian          weigh the detection results from both the thermal and vis-
detection. Extensive experiments on KAIST multispectral            ible images. [6] uses the illumination value to weigh the
pedestrian detection dataset [8] and FLIR ADAS dataset             detection results from a day illumination sub-network and
[1] demonstrate that, compared with common feature fusion          a night illumination sub-network. As mentioned in the pre-
methods (such as addition or concatenation), GAFF brings           vious section, such a handcrafted weighing scheme is lim-
important accuracy gains at a low computational cost.              ited and produces sub-optimal performance. CIAN [20] ap-
    This paper is organized as follows: Section 2 reviews          plies the channel-level attention in the multispectral feature
some representative work applying static/adaptive feature          fusion stage to model the cross-modality interaction and
fusion for multispectral pedestrian detection; Section 3 in-       weigh each feature map extracted from the different spec-
troduces implementation details on how to integrate GAFF           trum. This network realizes a fully adaptive fusion of ther-
into a typical two-stream convolutional neural network; In         mal and visible features, however, in this approach, the fu-
Section 4, we evaluate our methods on two public multi-            sion module is optimized directly while solving the pedes-
spectral object detection datasets [8, 1], then we provide an      trian detection task which means that the network uses in-
extensive ablation study and visualization results to discuss      formation about what (pedestrian or background) and where
the reasons of the accuracy improvements; Section 5 con-           (bounding box) relevant elements are in the images but it
cludes the paper.                                                  does not use the fact that some features may contain more
                                                                   relevant information than others. We believe and we show
2. Related Work                                                    that with these additional information (that we include in
                                                                   our method through the guidance mechanism), we can im-
2.1. Static multispectral feature fusion                           prove the detection precision.
    KAIST released the first large-scale multispectral pedes-
trian detection dataset [8], which contains approximately          3. Proposed approach
95k well-aligned and manually annotated thermal-visible
image pairs captured during daytime and nighttime. Some                The proposed Guided Attentive Feature Fusion (GAFF),
example image pairs are shown in Fig. 2. Then [18] demon-          shown in Fig. 3, takes place in the multispectral feature fu-
strated the first application of deep learning-based solutions     sion stage of a two-stream convolutional neural network.
in multispectral pedestrian detection. They compared the           It consists of two components: an intra-modality attention
early and late fusion architectures and found that the late        module and an inter-modality one.

                                                                  73
                                                                                                 Convolution              Sigmoid
                                                                                                  operation               function

       Thermal feature
         extraction

           Multispectral
          feature fusion
                                                         Thermal features
                                 Pedestrian
                              detection network                                    Feature             Convolution           Softmax
                                                                                concatenation           operation            function

       Visible feature
         extraction                                                                                                                                                                         Fused features

                                                                                                 Convolution              Sigmoid
                                                          Visible features                        operation               function

                                                                                                        Intra-modality       Inter-modality     Feature multiplication   Feature addition
                                 Thermal input image   Visible input image   Ground truth mask          attention path       attention path          operation              operation

Figure 3: The overall architecture of Guided Attentive Feature Fusion (GAFF). Green, blue and purple blocks represent ther-
mal, visible and fused features. Yellow and red paths represent the intra- and inter-modality attention modules, respectively.

3.1. Intra-modality attention module                                                                             3.2. Inter-modality attention module
    The intra-modality attention module aims at enhanc-                                                              Thermal and visible cameras have their own imaging
ing the thermal or visible features in a monospectral view.                                                      characteristics, and under certain conditions, one sensor has
Specifically, as illustrated by the yellow paths on Fig. 3,                                                      superior imaging quality (i.e. is more relevant for the con-
features of an area with a pedestrian are highlighted by                                                         sidered task) than the other. To leverage both modalities, we
multiplying the learnt features with the predicted pedes-                                                        propose the inter-modality attention module, which adap-
trian mask. Moreover, in order to avoid directly affecting                                                       tively selects thermal or visible features according to the
the thermal or visible features, the highlighted features are                                                    dynamic comparison of their feature quality. Concretely,
added as a residual to enhance the mono-spectral features.                                                       an inter-modality attention mask is predicted based on the
This procedure can be formalized as:                                                                             combination of thermal and visible features. This predicted
                                                                                                                 mask has two values for each pixel, corresponding to the
                            t
                           fintra = f t ⊗ (1 + mtintra )                                                         weights for thermal and visible features (summing to 1).
                          v                                                                      (1)
                         fintra = f v ⊗ (1 + mvintra )                                                           This attention module is illustrated as the red paths in Fig. 3.
                                                                                                                 It can be formulated as:
   where
                                                                                                                                                t
                                                                                                                                              finter = f t ⊗ (1 + mtinter )
                            mtintra = σ(Fintra
                                          t
                                               (f t ))                                                                                                                                                       (3)
                                                                                                 (2)                                          finter = f v ⊗ (1 + mvinter )
                                                                                                                                               v
                            mvintra = σ(Fintra
                                         v
                                               (f v ))
                                                                                                                         where
    Superscripts (t or v) denote the thermal (t) or visible (v)
modality; ⊗ denotes the element-wise multiplication; σ rep-
                                                                                                                                     mtinter , mvinter = δ(Finter ([f t , f v ]))                            (4)
resents the sigmoid function; Fintra represents a convolu-
tion operation to predict the intra-modality attention masks                                                        Here, δ denotes the softmax function; [·] denotes the fea-
(pedestrian masks) mintra ; f and fintra represent the orig-                                                     ture concatenation operation; Finter represents a convolu-
inal and enhanced features, respectively.                                                                        tion operation to predict the inter-modality attention mask
    The prediction of the pedestrian masks is supervised                                                         minter . At each spatial position of the mask, the sum of
by the semantic segmentation loss, where the ground truth                                                        mtinter and mvinter equals to 1. Note that this formalization
mask (mgtintra ) is converted from the object detection anno-                                                    could theoretically allow for more than two modalities to be
tations. As illustrated in Fig. 3 the bounding box annota-                                                       fuse following the same principles.
tions are transformed into some filled ellipses to approxi-                                                         The inter-modality attention module allows the network
mate the shape of the true pedestrians.                                                                          to adaptively select the most reliable modality. However, in

                                                                                                               74
order to train this module, we should need a costly ground         where
truth information about the best pixel-level modality qual-                 t
ity. Our solution to relieve the annotation cost is to assign              fhybrid = f t ⊗ (1 + mtintra ) ⊗ (1 + mtinter )
                                                                            v
                                                                                                                                       (8)
labels according to the prediction of the pedestrian masks                 fhybrid = f v ⊗ (1 + mvintra ) ⊗ (1 + mvinter )
from the intra-modality attention module, i.e., we force the
network to select one modality if its intra-modality mask              Here, mintra and minter are predicted intra- and inter-
prediction is better (i.e. closer to the ground truth pedes-       modality attention masks from Eq. 2 and Eq. 4; fhybrid
trian mask) than the other. Specifically, we first calculate an    represents features enhanced by both attention modules;
error mask for each spectrum with the following formula:           f f used represents the final fused features.
                                                                       As mentioned in Section 2, the optimization of the mul-
               etintra = | mtintra − mgt
                                      intra |
                                                                   tispectral feature fusion task may not benefit enough from
                                                           (5)     the sole optimization of the object detection task (as done
               evintra = | mvintra − mgt
                                      intra |                      e.g. in [20]). In GAFF, we propose two specific feature fu-
   then the label for the modality selection is defined as:        sion losses, including the pedestrian segmentation loss for
                                                                   the intra-modality attention and the modality selection loss
                                                                   for the inter-modality attention, to guide the multispectral
                             if (evintra − etintra ) > margin      feature fusion task. These losses are jointly optimized with
         
          1, 0
mgt    =   0, 1              if (etintra − evintra ) > margin      the object detection loss. The final training loss Ltotal is:
 inter
           ignored           otherwise
         
                                                            (6)                   Ltotal = Ldet + Lintra + Linter                      (9)
    Here, | · | denotes the absolute function; eintra repre-
                                                                      where, Ldet , Lintra and Linter are the pedestrian de-
sents the error mask, defined by the L1 distance between the
                                                                   tection, the intra- and inter-modality attention loss, respec-
predicted intra-modality mask mintra and the ground truth
                                                                   tively.
intra-modality mask mgt             gt
                          intra ; minter is the ground truth
mask for inter-modality attention (2 values at each mask po-
sition); margin is a hyper-parameter to be tuned.
                                                                   4. Experiments
    An example of the label assignment for the inter-                  In this section, we conduct experiments on KAIST Mul-
modality attention mask is shown in Fig. 3. If the intra-          tispectral Pedestrian Detection Dataset [8] and FLIR ADAS
modality pedestrian masks are predicted as shown in the            Dataset [1] to evaluate the effectiveness of the proposed
yellow paths, the inter-modality (weak) ground truth masks         method. Moreover, we attempt to interpret the reasons for
are then defined as the ones shown on the red paths, where         improvements by visualizing the predicted attention masks.
white, black and gray areas denote the classification la-          Finally, we provide inference speed analysis on two differ-
bels 1,0 and ignored, respectively. Here, the thermal fea-         ent target platforms.
tures produce a better intra-modality mask prediction for
the pedestrians on the left side of the input images in            4.1. Datasets
Fig. 3. Therefore, according to Eq. 6, the label for the inter-       KAIST dataset contains 7,601 training image pairs and
modality mask on this area is assigned as 1,0 (1 for the ther-     2,252 pairs testing ones. Some example image pairs from
mal mask and 0 for the visible mask). For regions where            this dataset are shown in Fig. 2. [10] proposes a ”sanitized”
the two intra-modality masks have comparable prediction            version of the annotations, where numerous annotation er-
qualities (i.e., the difference between prediction errors is       rors are removed. Our experiments are conducted with the
smaller than the predefined margin), the optimization of the       original as well as the “sanitized” version of annotations
inter-modality attention mask prediction on these areas are        for fair comparisons with our competitors. We found out
ignored (i.e., do not participate in the loss calculation).        that the “sanitized” annotations substantially improve the
                                                                   detection accuracy for different network architectures. All
3.3. Combining intra- and inter-modality attention                 models are evaluated with the improved testing annotations
   The intra-modality attention module enhances features           from [14] and the usual pedestrian detection metric: log-
on areas with pedestrians and the inter-modality attention         average Miss Rate over the range of [10−2 , 100 ] false posi-
module adaptively selects features from the most reliable          tives per image (FPPI) under a “reasonable” setting [5], i.e.,
modality. When these two modules are combined, the fused           only pedestrians taller than 50 pixels under no or partial oc-
features are obtained by:                                          clusions are considered 1 .
                                                                      1 We use the evaluation code provided by [10]: https://github.com/Li-
                            t         v
                           fhybrid + fhybrid                       Chengyang/MSDS-RCNN/tree/master/lib/datasets/KAISTdevkit-matlab-
                f f used =                                 (7)     wrapper
                                   2

                                                                  75
   We also conduct experiments on FLIR ADAS Dataset                                               Miss Rate
                                                                               Residual
[1]. [19] proposed an ”aligned” version of the dataset for                                  All     Day     Night
multispectral object detection. This new version contains                                 7.46%    8.88% 4.85%
5,142 well-aligned multispectral image pairs (4,129 pairs                         X       6.48%    8.35% 3.46%
for training and 1,013 pairs for testing). FLIR covers three
object categories: “person”, “car” and “bicycle”. Models          Table 2: Detection results of GAFF where the attention
are evaluated with the usual object detection metric intro-       masks are directly applied or added as residual.
duced with MS-COCO[13]: the mean Average Precision
(mAP) averaged over ten different IoU thresholds.
                                                                  by comparing in Table 2 the Miss Rate of GAFF where the
4.2. Implementation details                                       attention masks are directly applied to mono-spectral fea-
                                                                  tures (fintra = f ⊗ mintra and finter = f ⊗ minter ) or
    The proposed GAFF module can be included in any type
                                                                  added as residual (as in Eq. 1 and Eq. 3).
of two-stream convolutional neural networks. In these ex-
periments, we choose RetinaNet [12] as our base detector. It
is transformed into a two-stream convolutional neural net-        Necessity of attention. We compare in Tab. 3 the detec-
work by adding an additional branch for the extraction of         tion accuracy on KAIST dataset with different attention set-
thermal features. A ResNet18 [7] or a VGG16 [17] net-             tings, different backbone networks, and different annotation
work is pre-trained on ImageNet [2], then adopted as our          settings (original and “sanitized”). When conducting exper-
backbone network. The input image resolution is fixed to          iments with inter-modality but without intra-modality atten-
640×512 for training and evaluation. Our baseline detector        tion, the pedestrian masks are predicted but are not multi-
applies the basic addition as the multispectral feature fusion    plied with the corresponding mono-spectral features. For
method. GAFF is implemented by adding the intra- and              each backbone network or annotation setting, both intra-
inter-modality attention modules, corresponding to the yel-       and inter-modality attention modules consistently improve
low and the red branches in Fig. 3. Focal loss [12] and Bal-      the baseline detection accuracy, and their combination leads
anced L1 loss [15] are adopted as the classification loss and     to the lowest overall Miss Rate under all experimental set-
the bounding box regression loss to optimize the object de-       tings. The present findings confirm the effectiveness of the
tection task. In order to introduce our specific guidance, we     proposed guided attentive feature fusion modules.
adopt the DICE [3] loss as the pedestrian segmentation loss
(Lintra in Eq. 9) and the cross-entropy loss as the modality      Necessity of guidance. To explore the effect of the pro-
selection loss (Linter in Eq. 9).                                 posed multispectral feature fusion guidance, we compare
4.3. Ablation study                                               our guided approach to one with a similar architecture as
                                                                  ours but where the optimization of the specific fusion losses
                                                                  (Lintra and Linter in Eq. 9) are removed from the train-
                                Miss Rate
            M argin                                               ing process, i.e., the fusion is only supervised by the ob-
                          All     Day     Night
                                                                  ject detection loss (as done with [20]). We report in Tab. 4
               0.05     6.92%    8.47% 3.68%
                                                                  the detection performance with and without guidance, un-
               0.1      6.48%    8.35% 3.46%
               0.2      7.47%    9.31% 4.22%
                                                                  der different backbone networks and annotations settings.
                                                                  The results confirm our assumption that the object detec-
Table 1: Detection results of GAFF with different margin          tion loss is not relevant enough for the multispectral feature
values in the inter-modality attention module.                    fusion task: even though the non-guided attentive fusion
                                                                  module improves the baseline Miss Rate to some degree
Hyper-parameter tuning. As reported in Table 1, we                (e.g., with the “sanitized” annotations and VGG16 back-
conduct experiments with different margin values in the           bone, non-guided model improves the base detector’s Miss
inter-modality attention module on KAIST dataset [8] with         Rate from 9.28% to 8.38%), it could be further improved
“sanitized” annotations. The Miss Rate scores on the              when the specific fusion guidance is added (from 8.38% to
Reasonable-all, Reasonable-day and Reasonable-night sub-          6.48%).
sets are listed. We observe that the optimal Miss Rate is
achieved when margin = 0.1. Thus, we use margin =                 Attention mask interpretation. Fig. 4 provides the vi-
0.1 for all the following experiments.                            sualization results of the intra-modality, the inter-modality
                                                                  and the hybrid attention masks during daytime and night-
Residual attention. As mentioned in Section 3, attention          time. For each figure, the top and bottom two rows of
enhanced features are added as residual to avoid directly af-     images are visualization results of guided and non-guided
fecting the thermal or visible features. We verify this choice    attentive feature fusions, respectively. We can see on the

                                                                 76
    Guided Attentive Feature Fusion

                                                                                                                                                                  Guided Attentive Feature Fusion
    Non-guided Attentive Feature Fusion

                                                                                                                                                                  Non-guided Attentive Feature Fusion
                                          Detection results         Intra-modality attention mask    Inter-modality attention mask   Hybrid attention mask                                               Detection results   Intra-modality attention mask   Inter-modality attention mask   Hybrid attention mask

                                                                                    (a) Daytime                                                                                                                                            (b) Nighttime

                                                          Figure 4: Visualization examples of attention masks on KAIST dataset. Zoom in to see details.

                                                                  GAFF                                                  Miss Rate                                                                                                                                                     Miss Rate
    Backbone                                                                                                                                                                                            Backbone             Guidance
                                                              Intra. Inter.                           All                 Day                 Night                                                                                                            All                      Day                    Night
                                                                                                    13.04%               13.83%              11.60%                                                                                                          13.15%                    13.71%                 11.54%
                                                                                                                                                                                                        ResNet18
                                                               X                                    12.13%               11.97%              11.99%                                                                                    X                     10.74%                    10.46%                 11.10%
    ResNet18
                                                                                 X                  11.15%               10.68%              11.67%                                                                                                          13.67%                    13.19%                 14.51%
                                                               X                 X                  10.74%               10.46%              11.10%                                                     VGG16
                                                                                                                                                                                                                                       X                     10.62%                    10.82%                 10.14%
                                                                                                    12.72%               11.37%              15.57%
                                                                                                                                                                                                                                 (a) Original annotations
                                                               X                                    11.78%               11.45%              12.50%
                   VGG16                                                                                                                                                                                                                               Miss Rate
                                                                                 X                  11.03%               10.99%              11.44%                                                     Backbone               Guidance
                                                               X                 X                  10.62%               10.82%              10.14%                                                                                            All        Day                                                   Night
                                                                                                                                                                                                                                             9.05%      10.63%                                                  6.01%
                                                                    (a) Original annotations                                                                                                            ResNet18
                                                                                                                                                                                                                                  X          7.93%      9.79%                                                   4.33%
                                                                                                                                                                                                                                             8.38%      10.39%                                                  4.44%
                                                                  GAFF                                                    Miss Rate                                                                      VGG16
    Backbone                                                                                                                                                                                                                      X          6.48%      8.35%                                                   3.46%
                                                              Intra. Inter.                            All                   Day                Night
                                                                                                     9.98%                 12.46%               5.29%                                                                             (b) “Sanitized” annotations
                                                                X                                    9.26%                 11.51%               5.32%
    ResNet18                                                                                                                                                  Table 4: Comparison between guided and non-guided mod-
                                                                                    X                9.29%                 11.97%               5.14%
                                                                X                   X                7.93%                  9.79%               4.33%         els on KAIST dataset [8] with both annotation settings.
                                                                                                     9.28%                 11.73%               5.17%
                                                                X                                    8.70%                 11.42%               3.55%
                    VGG16
                                                                                    X                7.73%                 10.35%               2.81%
                                                                X                   X                6.48%                  8.35%               3.46%         due to its human-like shape on the thermal image of Fig. 4a,
                                                                                                                                                              and the pedestrian in the middle right position is missed due
                                                                 (b) “Sanitized” annotations                                                                  to insufficient lighting on the RGB image of Fig. 4b. For
                                                                                                                                                              inter-modality attention masks, it appears that the guided
Table 3: Ablation study of two attentive fusion modules on
                                                                                                                                                              attentive fusion tends to select visible features on well-lit
KAIST dataset [8] with original (top) or “sanitized” (bot-
                                                                                                                                                              areas (such as upside of images in Fig. 4b) and brightly
tom) annotations.
                                                                                                                                                              coloured areas (e.g., traffic cone, road sign, speed bump, car
                                                                                                                                                              tail light, etc), and to select thermal features on dark areas
                                                                                                                                                              and uniform areas (such as sky and road). Note that these
intra-modality attention masks that the guided attention                                                                                                      attention preferences are automatically learnt via our inter-
mechanism focuses on pedestrian areas, even though, some-                                                                                                     modality attention guidance. On the contrary, despite the
times, it is not accurate from a single mono-spectral view.                                                                                                   fact that the non-guided attention mechanism brings some
For example, the traffic cone is misclassified as a pedestrian                                                                                                accuracy improvements, the predicted attention masks are

                                                                                                                                                             77
                                                                                                                                                      quite difficult to interpret. More visualization results are
                                                                                                                                                      shown in Fig. 5. Besides, an interesting error case is shown
   Guided Attentive Feature Fusion

                                                                                                                                                      in Fig. 5c, where the pedestrian on the steps is not detected
                                                                                                                                                      with the guided model but detected with the non-guided
                                                                                                                                                      model. As mentioned earlier, GAFF selects thermal fea-
                                                                                                                                                      tures on uniform areas, which is intuitive since thermal cam-
                                                                                                                                                      eras are sensitive to temperature change and there exist few
                                                                                                                                                      objects on uniform areas of the thermal image. However,
                                                                                                                                                      in this particular case, the pedestrian is not captured on the
   Non-guided Attentive Feature Fusion

                                                                                                                                                      thermal image, which leads to the final detection error.

                                                                                                                                                                                  Intra- and inter-modality attention accuracy evolution
                                                                                                                                                                        0.7                                                                          1.0

                                         Detection results   Intra-modality attention mask   Inter-modality attention mask   Hybrid attention mask                      0.6                                                                          0.9

                                                                                                                                                                        0.5                                                                          0.8
                                                                             (a) Daytime
                                                                                                                                                                        0.4

                                                                                                                                                           Dice socre

                                                                                                                                                                                                                                                       Accuracy
                                                                                                                                                                                                                                                     0.7

                                                                                                                                                                        0.3                                                                          0.6
   Guided Attentive Feature Fusion

                                                                                                                                                                        0.2
                                                                                                                                                                                                                                                     0.5

                                                                                                                                                                        0.1
                                                                                                                                                                                                                           Thermal mask dice score   0.4
                                                                                                                                                                                           Modality selection accuracy     Visible mask dice score
                                                                                                                                                                        0.0
                                                                                                                                                                              0          1000              2000          3000              4000
                                                                                                                                                                                                          Iterations

                                                                                                                                                      Figure 6: Intra- and inter-modality attention accuracy evo-
   Non-guided Attentive Feature Fusion

                                                                                                                                                      lution during training.

                                                                                                                                                      Attention accuracy evolution We plot in Fig. 6 the evo-
                                                                                                                                                      lution of intra- and inter-modality attention accuracy during
                                                                                                                                                      training. Specifically, red solid and dashed lines represent
                                                                                                                                                      the pedestrian segmentation accuracy (via DICE score [3]
                                                                                                                                                                2|A∩B|
                                         Detection results   Intra-modality attention mask   Inter-modality attention mask   Hybrid attention mask
                                                                                                                                                      Dice = |A|+|B|    ) from thermal and visible features in intra-
                                                                           (b) Nighttime                                                              modality attention module; blue line indicates the modal-
                                                                                                                                                      ity selection accuracy in inter-modality attention module.
                                                                                                                                                      From the plot, we can conclude that thermal images are gen-
   Guided Attentive Feature Fusion

                                                                                                                                                      erally better for recognition than visible images. This ob-
                                                                                                                                                      servation is consistent with our mono-spectral experiments,
                                                                                                                                                      where thermal-only model reaches 18.8% of Miss Rate
                                                                                                                                                      while visible-only model achieves 20.74% (both trained
                                                                                                                                                      with “sanitized” annotations). Interestingly, as the segmen-
                                                                                                                                                      tation accuracy increases for both images, the modality se-
                                                                                                                                                      lection task becomes more and more challenging. Note
   Non-guided Attentive Feature Fusion

                                                                                                                                                      that this accuracy is irrelevant at the beginning of the train-
                                                                                                                                                      ing, where predicted pedestrian masks are almost zero for
                                                                                                                                                      both thermal and visible features, thus the difference be-
                                                                                                                                                      tween their error masks is minor and the set of margin
                                                                                                                                                      makes most areas ignored for modality selection optimiza-
                                         Detection results   Intra-modality attention mask   Inter-modality attention mask   Hybrid attention mask
                                                                                                                                                      tion. Such mechanism avoids the “cold start” problem.

                                                                           (c) Error case                                                             Runtime analysis In Tab. 5 we report the total number of
                                                                                                                                                      learnable parameters and the average inference runtime on
Figure 5: More visualization examples of attention masks
                                                                                                                                                      two different computation platforms. Specifically, the mod-
on KAIST dataset. Zoom in to see details.
                                                                                                                                                      els are implemented with Pytorch (TensorRT) framework

                                                                                                                                                     78
                                               Runtime                         Methods           Platform      Runtime
    Backbone    GAFF          Param.
                                           1080Ti    TX2                  ACF+T+THOG [8]         MATLAB        2730ms
                            23,751,725    10.31ms 10.5ms                 Halfway Fusion [14]      Titan X       430ms
    ResNet18
                  X         23,765,553    10.85ms 12.1ms                 Fusion RPN+BF [14]      MATLAB         800ms
                            31,403,053     8.87ms 10.3ms                   IAF R-CNN [11]         Titan X       210ms
     VGG16                                                                IATDNN+IASS [6]         Titan X       250ms
                  X         31,430,705     9.34ms 11.6ms
                                                                              CIAN [20]           1080Ti         70ms
   Table 5: Runtime on different computing platforms.                     MSDS-RCNN [10]          Titan X       220ms
                                                                              CFR [19]            1080Ti         50ms
                                          Miss Rate                          GAFF (ours)          1080Ti        9.34ms
             Methods
                                  All        Day       Night
                                                                 Table 7: Runtime comparisons with different methods on
       ACF+T+THOG [8]           47.24%     42.44%     56.17%
      Halfway Fusion [14]       26.15%     24.85%     27.59%
                                                                 KAIST dataset [8].
      Fusion RPN+BF [14]        16.53%     16.39%     18.16%
        IAF R-CNN [11]          16.22%     13.94%     18.28%            Backbone     GAFF       mAP    AP75      AP50
       IATDNN+IASS [6]          15.78%     15.08%     17.22%                                   36.6%   31.9%     72.8%
           CIAN [20]            14.12%     14.77%     11.13%            ResNet18
                                                                                       X       37.5%   32.9%     72.9%
       MSDS-RCNN [10]           11.63%     10.60%     13.73%
                                                                                               36.3%   30.2%     71.9%
           CFR [19]             10.05%      9.72%     10.80%             VGG16
                                                                                       X       37.3%   30.9%     72.7%
          GAFF (ours)           10.62%     10.82%     10.14%
                       (a) Original annotations                        Table 8: Detection results on FLIR dataset [1].

                                          Miss Rate
            Methods
                                  All       Day       Night      Table 7). According to Tab. 7, thanks to the lightweight de-
       MSDS-RCNN [10]           7.49%      8.09%      5.92%      sign of GAFF, our model has substantial advantage in terms
          CFR [19]              6.13%      7.68%      3.19%      of inference speed compared to e.g. [19].
         GAFF(ours)             6.48%      8.35%      3.46%
                   (b) “Sanitized” annotations
                                                                 FLIR Dataset Tab. 8 reports the detection results with
Table 6: Detection results on KAIST dataset [8] with origi-      and without GAFF on FLIR dataset. We can observe that
nal (top) or “sanitized” (bottom) annotations.                   the average precision is improved for all IoU thresholds
                                                                 with GAFF (around 1% of mAP improvement for both
                                                                 backbone networks), which shows that our method can gen-
for an inference time testing on the Nvidia GTX 1080Ti           eralize well to different types of images. For comparison,
(Nvidia TX2) platform. Since GAFF only involves 3 con-           the more costly CFR [19] reaches 72.39% of AP50 on this
volution layers, the additional parameters and computation       dataset, whereas our best result is 72.9%.
cost is low, i.e., it represents less than 0.1% of additional
parameters and around 0.5ms (1.5ms) of inference time on
1080Ti (TX2). Note that the time for post-processing treat-      5. Conclusion
ments (such as Non-Maximum Suppression) is not taken
                                                                    We argue that the lack guidance is a limitation for effi-
into account for the benchmarking. Our model meets the
                                                                 cient and effective multispectral feature fusion, and we pro-
requirement of real-time treatment on embedded devices,
                                                                 pose Guided Attentive Feature Fusion (GAFF) to guide this
which is essential for many applications.
                                                                 fusion process. Without hand-crafted assumptions or addi-
                                                                 tional annotations, GAFF realizes a fully adaptive fusion of
4.4. Comparison with State-of-the-art Multispec-
                                                                 thermal and visible features. Experiments on KAIST and
     tral Pedestrian Detection Methods
                                                                 FLIR datasets demonstrate the effectiveness of GAFF and
KAIST Dataset Tab. 6 shows the detection results of ex-          the necessity of attention and guidance in the feature fu-
isting methods and our GAFF with the original and “sani-         sion stage. We noticed that certain thermal-visible image
tized” annotations on KAIST. It can be observed that GAFF        pairs are slightly misaligned in the above datasets, such a
achieves state-of-the-art performance on this dataset (it is     problem could be more critical in real life applications. Our
slightly less accurate than CFR [19], which applies cas-         future research is devoted to the development of a real-time
caded Fuse-and-Refine blocks for sequential feature en-          feature calibration module based on the predicted attention
hancement and needs more computation than GAFF (see              masks from GAFF.

                                                                79
References                                                                 Conference 2016, BMVC 2016, York, UK, September 19-22,
                                                                           2016, 2016.
 [1] Free flir thermal dataset for algorithm train-
                                                                      [15] Jiangmiao Pang, Kai Chen, Jianping Shi, Huajun Feng,
     ing.            https://www.flir.com/oem/adas/
                                                                           Wanli Ouyang, and Dahua Lin. Libra r-cnn: Towards bal-
     adas-dataset-form/.
                                                                           anced learning for object detection. In IEEE Conference on
 [2] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei.         Computer Vision and Pattern Recognition, 2019.
     ImageNet: A Large-Scale Hierarchical Image Database. In
                                                                      [16] Shaoqing Ren, Kaiming He, Ross B. Girshick, and Jian Sun.
     CVPR09, 2009.
                                                                           Faster R-CNN: towards real-time object detection with re-
 [3] Lee R. Dice. Measures of the amount of ecologic association
                                                                           gion proposal networks. In Advances in Neural Information
     between species. Ecology, 26(3):297–302, 1945.
                                                                           Processing Systems 28: Annual Conference on Neural In-
 [4] Piotr Dollar, Ron Appel, Serge Belongie, and Pietro Perona.           formation Processing Systems 2015, December 7-12, 2015,
     Fast feature pyramids for object detection. IEEE Trans. Pat-          Montreal, Quebec, Canada, pages 91–99, 2015.
     tern Anal. Mach. Intell., 36(8):1532–1545, Aug. 2014.
                                                                      [17] K. Simonyan and A. Zisserman. Very deep convolutional
 [5] P. Dollar, C. Wojek, B. Schiele, and P. Perona. Pedes-                networks for large-scale image recognition. In International
     trian detection: An evaluation of the state of the art. IEEE          Conference on Learning Representations, 2015.
     Transactions on Pattern Analysis and Machine Intelligence,
                                                                      [18] Jörg Wagner, Volker Fischer, Michael Herman, and Sven
     34(4):743–761, 2012.
                                                                           Behnke. Multispectral pedestrian detection using deep fu-
 [6] Dayan Guan, Yanpeng Cao, Jiangxin Yang, Yanlong Cao,
                                                                           sion convolutional neural networks. In 24th European Sym-
     and Michael Ying Yang. Fusion of multispectral data through
                                                                           posium on Artificial Neural Networks, ESANN 2016, Bruges,
     illumination-aware deep neural networks for pedestrian de-
                                                                           Belgium, April 27-29, 2016, 2016.
     tection. Information Fusion, 50:148–157, 2019.
                                                                      [19] Heng Zhang, Elisa Fromont, Sébastien Lefèvre, and Bruno
 [7] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
                                                                           Avignon. Multispectral Fusion for Object Detection with
     Deep residual learning for image recognition. In 2016 IEEE
                                                                           Cyclic Fuse-and-Refine Blocks. In ICIP 2020 - IEEE Inter-
     Conference on Computer Vision and Pattern Recognition,
                                                                           national Conference on Image Processing, pages 1–5, Abou
     CVPR 2016, Las Vegas, NV, USA, June 27-30, 2016, pages
                                                                           Dabi, United Arab Emirates, Oct. 2020.
     770–778, 2016.
                                                                      [20] Lu Zhang, Zhiyong Liu, Shifeng Zhang, Xu Yang, Hong
 [8] Soonmin Hwang, Jaesik Park, Namil Kim, Yukyung Choi,
                                                                           Qiao, Kaizhu Huang, and Amir Hussain. Cross-modality
     and In So Kweon. Multispectral pedestrian detection:
                                                                           interactive attention network for multispectral pedestrian de-
     Benchmark dataset and baselines. In Proceedings of IEEE
                                                                           tection. Information Fusion, 50:20–29, 2019.
     Conference on Computer Vision and Pattern Recognition
     (CVPR), 2015.
 [9] D. König, M. Adam, C. Jarvers, G. Layher, H. Neumann,
     and M. Teutsch. Fully convolutional region proposal net-
     works for multispectral person detection. In 2017 IEEE Con-
     ference on Computer Vision and Pattern Recognition Work-
     shops (CVPRW), pages 243–250, 2017.
[10] Chengyang Li, Dan Song, Ruofeng Tong, and Min Tang.
     Multispectral pedestrian detection via simultaneous detec-
     tion and segmentation. In British Machine Vision Conference
     2018, BMVC 2018, Northumbria University, Newcastle, UK,
     September 3-6, 2018, page 225, 2018.
[11] Chengyang Li, Dan Song, Ruofeng Tong, and Min Tang.
     Illumination-aware faster R-CNN for robust multispectral
     pedestrian detection. Pattern Recognition, 85:161–171,
     2019.
[12] Tsung-Yi Lin, Priya Goyal, Ross B. Girshick, Kaiming He,
     and Piotr Dollár. Focal loss for dense object detection. In
     IEEE International Conference on Computer Vision, ICCV
     2017, Venice, Italy, October 22-29, 2017, pages 2999–3007,
     2017.
[13] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,
     Pietro Perona, Deva Ramanan, Piotr Dollar, and Larry Zit-
     nick. Microsoft COCO: Common objects in context. In
     ECCV. European Conference on Computer Vision, Septem-
     ber 2014.
[14] Jingjing Liu, Shaoting Zhang, Shu Wang, and Dimitris N.
     Metaxas. Multispectral deep neural networks for pedestrian
     detection. In Proceedings of the British Machine Vision

                                                                     80
