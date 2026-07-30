---
source_id: 020
bibtex_key: zhou2019objects
title: Objects as Points
year: 2019
domain_theme: Fondasi RGB
verified_pdf: 20_CenterNet (Objects as Points).pdf
char_count: 72246
---

Objects as Points

                                                            Xingyi Zhou                          Dequan Wang                            Philipp Krähenbühl
                                                             UT Austin                           UC Berkeley                                 UT Austin
                                                     zhouxy@cs.utexas.edu                 dqwang@cs.berkeley.edu                   philkr@cs.utexas.edu
arXiv:1904.07850v2 [cs.CV] 25 Apr 2019

                                                                  Abstract
                                                                                                                          40
                                            Detection identifies objects as axis-aligned boxes in an
                                         image. Most successful object detectors enumerate a nearly

                                                                                                                COCO AP
                                         exhaustive list of potential object locations and classify                       35
                                         each. This is wasteful, inefficient, and requires additional
                                         post-processing. In this paper, we take a different approach.
                                         We model an object as a single point — the center point                                                         CenterNet(ours)
                                         of its bounding box. Our detector uses keypoint estima-                          30
                                                                                                                                                         FasterRCNN
                                         tion to find center points and regresses to all other ob-                                                       RetinaNet
                                         ject properties, such as size, 3D location, orientation, and                                                    YOLOv3
                                         even pose. Our center point based approach, CenterNet, is                        25
                                         end-to-end differentiable, simpler, faster, and more accurate                         0   50            100         150           200
                                         than corresponding bounding box based detectors. Center-                                        Inference time (ms)
                                         Net achieves the best speed-accuracy trade-off on the MS             Figure 1: Speed-accuracy trade-off on COCO validation for
                                         COCO dataset, with 28.1% AP at 142 FPS, 37.4% AP at 52               real-time detectors. The proposed CenterNet outperforms a
                                         FPS, and 45.1% AP with multi-scale testing at 1.4 FPS. We            range of state-of-the-art algorithms.
                                         use the same approach to estimate 3D bounding box in the
                                         KITTI benchmark and human pose on the COCO keypoint
                                                                                                              moves duplicated detections for the same instance by com-
                                         dataset. Our method performs competitively with sophisti-
                                                                                                              puting bounding box IoU. This post-processing is hard to
                                         cated multi-stage methods and runs in real-time.
                                                                                                              differentiate and train [23], hence most current detectors
                                                                                                              are not end-to-end trainable. Nonetheless, over the past
                                                                                                              five years [19], this idea has achieved good empirical suc-
                                         1. Introduction                                                      cess [12,21,25,26,31,35,47,48,56,62,63]. Sliding window
                                            Object detection powers many vision tasks like instance           based object detectors are however a bit wasteful, as they
                                         segmentation [7, 21, 32], pose estimation [3, 15, 39], track-        need to enumerate all possible object locations and dimen-
                                         ing [24, 27], and action recognition [5]. It has down-stream         sions.
                                         applications in surveillance [57], autonomous driving [53],             In this paper, we provide a much simpler and more effi-
                                         and visual question answering [1]. Current object detec-             cient alternative. We represent objects by a single point at
                                         tors represent each object through an axis-aligned bounding          their bounding box center (see Figure 2). Other properties,
                                         box that tightly encompasses the object [18, 19, 33, 43, 46].        such as object size, dimension, 3D extent, orientation, and
                                         They then reduce object detection to image classification            pose are then regressed directly from image features at the
                                         of an extensive number of potential object bounding boxes.           center location. Object detection is then a standard keypoint
                                         For each bounding box, the classifier determines if the              estimation problem [3,39,60]. We simply feed the input im-
                                         image content is a specific object or background. One-               age to a fully convolutional network [37, 40] that generates
                                         stage detectors [33, 43] slide a complex arrangement of              a heatmap. Peaks in this heatmap correspond to object cen-
                                         possible bounding boxes, called anchors, over the image              ters. Image features at each peak predict the objects bound-
                                         and classify them directly without specifying the box con-           ing box height and weight. The model trains using standard
                                         tent. Two-stage detectors [18, 19, 46] recompute image-              dense supervised learning [39,60]. Inference is a single net-
                                         features for each potential box, then classify those features.       work forward-pass, without non-maximal suppression for
                                         Post-processing, namely non-maxima suppression, then re-             post-processing.

                                                                                                          1
Figure 2: We model an object as the center point of its bounding box. The bounding box size and other object properties are
inferred from the keypoint feature at the center. Best viewed in color.

   Our method is general and can be extended to other tasks     Changing the proposal classifier to a multi-class classi-
with minor effort. We provide experiments on 3D object de-      fication forms the basis of one-stage detectors. Several
tection [17] and multi-person human pose estimation [4], by     improvements to one-stage detectors include anchor shape
predicting additional outputs at each center point (see Fig-    priors [44, 45], different feature resolution [36], and loss
ure 4). For 3D bounding box estimation, we regress to the       re-weighting among different samples [33].
object absolute depth, 3D bounding box dimensions, and              Our approach is closely related to anchor-based one-
object orientation [38]. For human pose estimation, we con-     stage approaches [33, 36, 43]. A center point can be seen
sider the 2D joint locations as offsets from the center and     as a single shape-agnostic anchor (see Figure 3). However,
directly regress to them at the center point location.          there are a few important differences. First, our CenterNet
   The simplicity of our method, CenterNet, allows it to        assigns the “anchor” based solely on location, not box over-
run at a very high speed (Figure 1). With a simple Resnet-      lap [18]. We have no manual thresholds [18] for foreground
18 and up-convolutional layers [55], our network runs           and background classification. Second, we only have one
at 142 FPS with 28.1% COCO bounding box AP. With                positive “anchor” per object, and hence do not need Non-
a carefully designed keypoint detection network, DLA-           Maximum Suppression (NMS) [2]. We simply extract lo-
34 [58], our network achieves 37.4% COCO AP at 52 FPS.          cal peaks in the keypoint heatmap [4, 39]. Third, CenterNet
Equipped with the state-of-the-art keypoint estimation net-     uses a larger output resolution (output stride of 4) compared
work, Hourglass-104 [30, 40], and multi-scale testing, our      to traditional object detectors [21, 22] (output stride of 16).
network achieves 45.1% COCO AP at 1.4 FPS. On 3D                This eliminates the need for multiple anchors [47].
bounding box estimation and human pose estimation, we
perform competitively with state-of-the-art at a higher in-     Object detection by keypoint estimation. We are not the
ference speed. Code is available at https://github.             first to use keypoint estimation for object detection. Cor-
com/xingyizhou/CenterNet.                                       nerNet [30] detects two bounding box corners as keypoints,
                                                                while ExtremeNet [61] detects the top-, left-, bottom-, right-
2. Related work                                                 most, and center points of all objects. Both these methods
                                                                build on the same robust keypoint estimation network as our
Object detection by region classification. One of the           CenterNet. However, they require a combinatorial group-
first successful deep object detectors, RCNN [19], enu-         ing stage after keypoint detection, which significantly slows
merates object location from a large set of region candi-       down each algorithm. Our CenterNet, on the other hand,
dates [52], crops them, and classifies each using a deep        simply extracts a single center point per object without the
network. Fast-RCNN [18] crops image features instead,           need for grouping or post-processing.
to save computation. However, both methods rely on slow
low-level region proposal methods.
                                                                Monocular 3D object detection. 3D bounding box esti-
                                                                mation powers autonomous driving [17]. Deep3Dbox [38]
Object detection with implicit anchors. Faster                  uses a slow-RCNN [19] style framework, by first detecting
RCNN [46] generates region proposal within the de-              2D objects [46] and then feeding each object into a 3D es-
tection network. It samples fixed-shape bounding boxes          timation network. 3D RCNN [29] adds an additional head
(anchors) around a low-resolution image grid and classifies     to Faster-RCNN [46] followed by a 3D projection. Deep
each into “foreground or not”. An anchor is labeled fore-       Manta [6] uses a coarse-to-fine Faster-RCNN [46] trained
ground with a >0.7 overlap with any ground truth object,        on many tasks. Our method is similar to a one-stage version
background with a < 0.3 overlap, or ignored otherwise.          of Deep3Dbox [38] or 3DRCNN [29]. As such, CenterNet
Each generated region proposal is again classified [18].        is much simpler and faster than competing methods.
                                                                   for each center point. All classes c share the same offset
                                                                   prediction. The offset is trained with an L1 loss
                                                                                         1 X             p     
                                                                                Lof f =           Ôp̃ −    − p̃ .        (2)
                                                                                        N p               R
(a) Standard anchor based detec-     (b) Center point based de-
tion. Anchors count as positive      tection. The center pixel
                                                                   The supervision acts only at keypoints locations p̃, all other
with an overlap IoU > 0.7 to         is assigned to the object.
                                                                   locations are ignored.
any object, negative with an over-   Nearby points have a re-
lap IoU < 0.3, or are ignored oth-   duced negative loss. Object      In the next section, we will show how to extend this key-
erwise.                              size is regressed.            point estimator to a general purpose object detector.

Figure 3: Different between anchor-based detectors (a) and         4. Objects as Points
our center point detector (b). Best viewed on screen.                                (k)        (k)            (k)   (k)
                                                                      Let (x1 , y1 , x2 , y2 ) be the bounding box of ob-
                                                                   ject k with category ck . Its center point is lies at pk =
                                                                        (k)        (k)        (k)        (k)
                                                                    x         +x          y         +y
3. Preliminary                                                     ( 1 2 2 , 1 2 2 ). We use our keypoint estimator Ŷ to
                                                                   predict all center points. In addition, we regress to the ob-
    Let I ∈ RW ×H×3 be an input image of width W and                                 (k)     (k) (k)      (k)
height H. Our aim is to produce a keypoint heatmap Ŷ ∈            ject size sk = (x2 − x1 , y2 − y1 ) for each object k.
       W   H
[0, 1] R × R ×C , where R is the output stride and C is the        To limit the computational burden, we use a single size pre-
                                                                                   W   H

number of keypoint types. Keypoint types include C = 17            diction Ŝ ∈ R R × R ×2 for all object categories. We use an
human joints in human pose estimation [4, 55], or C = 80           L1 loss at the center point similar to Objective 2:
object categories in object detection [30,61]. We use the de-                                                              N
                                                                                                                     1 X
fault output stride of R = 4 in literature [4,40,42]. The out-                                      Lsize =              Ŝpk − sk .     (3)
put stride downsamples the output prediction by a factor R.                                                          N
                                                                                                                       k=1
A prediction Ŷx,y,c = 1 corresponds to a detected keypoint,
                                                                   We do not normalize the scale and directly use the raw pixel
while Ŷx,y,c = 0 is background. We use several different
                                                                   coordinates. We instead scale the loss by a constant λsize .
fully-convolutional encoder-decoder networks to predict Ŷ         The overall training objective is
from an image I: A stacked hourglass network [30, 40], up-
convolutional residual networks (ResNet) [22,55], and deep                               Ldet = Lk + λsize Lsize + λof f Lof f .         (4)
layer aggregation (DLA) [58].
    We train the keypoint prediction network following             We set λsize = 0.1 and λof f = 1 in all our experiments un-
Law and Deng [30]. For each ground truth keypoint                  less specified otherwise. We use a single network to predict
p ∈ R2 of class c, we compute a low-resolution equiva-             the keypoints Ŷ , offset Ô, and size Ŝ. The network pre-
lent p̃ = b Rp
               c. We then splat all ground truth keypoints         dicts a total of C + 4 outputs at each location. All outputs
                             W   H                                 share a common fully-convolutional backbone network. For
onto a heatmap Y ∈ [0, 1] R × R ×C using a Gaussian ker-
                     (x−p̃ )2 +(y−p̃ )2
                          x         y
                                                                   each modality, the features of the backbone are then passed
nel Yxyc = exp −            2σp2          , where σp is an ob-     through a separate 3 × 3 convolution, ReLU and another
ject size-adaptive standard deviation [30]. If two Gaussians       1 × 1 convolution. Figure 4 shows an overview of the net-
of the same class overlap, we take the element-wise maxi-          work output. Section 5 and supplementary material contain
mum [4]. The training objective is a penalty-reduced pixel-        additional architectural details.
wise logistic regression with focal loss [33]:
                 
                                α
                                                                   From points to bounding boxes At inference time, we
                 (1 − Ŷxyc ) log(Ŷxyc ) if Yxyc = 1
                                                                  first extract the peaks in the heatmap for each category in-
         −1  X   
  Lk =               (1 − Yxyc )β (Ŷxyc )α                (1)     dependently. We detect all responses whose value is greater
         N xyc                              otherwise            or equal to its 8-connected neighbors and keep the top
                        log(1 − Ŷxyc )
                 
                                                                   100 peaks. Let P̂c be the set of n detected center points
where α and β are hyper-parameters of the focal loss [33],         P̂ = {(x̂i , ŷi )}ni=1 of class c. Each keypoint location is
and N is the number of keypoints in image I. The nor-              given by an integer coordinates (xi , yi ). We use the key-
malization by N is chosen as to normalize all positive focal       point values Ŷxi yi c as a measure of its detection confidence,
loss instances to 1. We use α = 2 and β = 4 in all our             and produce a bounding box at location
experiments, following Law and Deng [30].                                                (x̂i + δ x̂i − ŵi /2, ŷi + δ ŷi − ĥi /2,
    To recover the discretization error caused by the output
                                                      W   H
stride, we additionally predict a local offset Ô ∈ R R × R ×2                            x̂i + δ x̂i + ŵi /2, ŷi + δ ŷi + ĥi /2),
                                                                          The 3D dimensions of an object are three scalars. We
                                                                       directly regress to their absolute values in meters using a
                                                                                              W   H
                                                                       separate head Γ̂ ∈ R R × R ×3 and an L1 loss.
                                                                          Orientation is a single scalar by default. However, it can
                                                                       be hard to regress to. We follow Mousavian et al. [38] and
                                                                       represent the orientation as two bins with in-bin regression.
   (a) Final
keypoint     Layer [C]
         heatmap         (b) 2Doffset
                         local  Detection
                                      [2]     (c) 3D size
                                              object Estimation
                                                          [2]       (d)Specifically,
                                                                        Pose Estimation
                                                                                     the orientation is encoded using 8 scalars, with
                                                                       4 scalars for each bin. For one bin, two scalars are used
                                                                       for softmax classification and the rest two scalar regress to
                                                                       an angle within each bin. Please see the supplementary for
                                                                       details about these losses.

                                                                      4.2. Human pose estimation
                                                                         Human pose estimation aims to estimate k 2D hu-
     3D size [3]           depth [1]          orientation [8]
                                                                      man joint locations for every human instance in the image
                                                                      (k = 17 for COCO). We considered the pose as a k × 2-
                                                                      dimensional property of the center point, and parametrize
                                                                      each keypoint by an offset to the center point. We directly
                                                                      regress to the joint offsets (in pixels) Jˆ ∈ R R × R ×k×2 with
                                                                                                                        W    H

                                                                      an L1 loss. We ignore the invisible keypoints by masking
                                                                      the loss. This results in a regression-based one-stage multi-
joint locations [k × 2] joint heatmap [k]     joint offset [2]        person human pose estimator similar to the slow-RCNN
Figure 4: Outputs of our network for different tasks: top for         version counterparts Toshev et al. [51] and Sun et al. [49].
object detection, middle for 3D object detection, bottom:                To refine the keypoints, we further estimate k human
                                                                                                   W   H

for pose estimation. All modalities are produced from a               joint heatmaps Φ̂ ∈ R R × R ×k using standard bottom-up
common backbone, with a different 3 × 3 and 1 × 1 output              multi-human pose estimation [4,39,41]. We train the human
convolutions separated by a ReLU. The number in brackets              joint heatmap with focal loss and local pixel offset analo-
indicates the output channels. See section 4 for details.             gous to the center detection discussed in Section. 3.
                                                                         We then snap our initial predictions to the closest de-
                                                                      tected keypoint on this heatmap. Here, our center offset
where (δ x̂i , δ ŷi ) = Ôx̂i ,ŷi is the offset prediction and      acts as a grouping cue, to assign individual keypoint detec-
(ŵi , ĥi ) = Ŝx̂i ,ŷi is the size prediction. All outputs are     tions to their closest person instance. Specifically, let (x̂, ŷ)
produced directly from the keypoint estimation without the            be a detected center point. We first regress to all joint loca-
need for IoU-based non-maxima suppression (NMS) or                    tions lj = (x̂, ŷ) + Jˆx̂ŷj for j ∈ 1 . . . k. We also extract all
                                                                                                          nj
other post-processing. The peak keypoint extraction serves            keypoint locations Lj = {˜lji }i=1      with a confidence > 0.1
as a sufficient NMS alternative and can be implemented ef-            for each joint type j from the corresponding heatmap Φ̂··j .
ficiently on device using a 3 × 3 max pooling operation.              We then assign each regressed location lj to its closest de-
                                                                      tected keypoint arg minl∈Lj (l − lj )2 considering only joint
4.1. 3D detection                                                     detections within the bounding box of the detected object.
    3D detection estimates a three-dimensional bounding
box per objects and requires three additional attributes per          5. Implementation details
center point: depth, 3D dimension, and orientation. We add
a separate head for each of them. The depth d is a sin-                  We experiment with 4 architectures: ResNet-18, ResNet-
gle scalar per center point. However, depth is difficult to           101 [55], DLA-34 [58], and Hourglass-104 [30]. We mod-
regress to directly. We instead use the output transforma-            ify both ResNets and DLA-34 using deformable convolu-
tion of Eigen et al. [13] and d = 1/σ(d)  ˆ − 1, where σ              tion layers [12] and use the Hourglass network as is.
is the sigmoid function. We compute the depth as an ad-
                                    W   H
ditional output channel D̂ ∈ [0, 1] R × R of our keypoint             Hourglass The stacked Hourglass Network [30, 40]
estimator. It again uses two convolutional layers separated           downsamples the input by 4×, followed by two sequential
by a ReLU. Unlike previous modalities, it uses the inverse            hourglass modules. Each hourglass module is a symmetric
sigmoidal transformation at the output layer. We train the            5-layer down- and up-convolutional network with skip con-
depth estimator using an L1 loss in the original depth do-            nections. This network is quite large, but generally yields
main, after the sigmoidal transformation.                             the best keypoint estimation performance.
                             AP                   AP50                AP75               Time (ms)           FPS
                      N.A. F MS             N.A. F MS           N.A. F MS            N.A. F MS           N.A. F MS
    Hourglass-104     40.3 42.2 45.1        59.1 61.1 63.5      44.0 46.0 49.3        71 129 672          14 7.8 1.4
    DLA-34            37.4 39.2 41.7        55.1 57.0 60.1      40.8 42.7 44.9        19 36 248           52 28 4
    ResNet-101        34.6 36.2 39.3        53.0 54.8 58.5      36.9 38.7 42.0        22 40 259           45 25 4
    ResNet-18         28.1 30.0 33.2        44.9 47.5 51.5      29.6 31.6 35.1         7 14 81           142 71 12

Table 1: Speed / accuracy trade off for different networks on COCO validation set. We show results without test augmentation
(N.A.), flip testing (F), and multi-scale augmentation (MS).

ResNet Xiao et al. [55] augment a standard residual net-        and DLA-34 train in 2.5 days on 8 TITAN-V GPUs, while
work [22] with three up-convolutional networks to allow         Hourglass-104 requires 5 days.
for a higher-resolution output (output stride 4). We first
change the channels of the three upsampling layers to           Inference We use three levels of test augmentations: no
256, 128, 64, respectively, to save computation. We then        augmentation, flip augmentation, and flip and multi-scale
add one 3 × 3 deformable convolutional layer before each        (0.5, 0.75, 1, 1.25, 1.5). For flip, we average the network
up-convolution with channel 256, 128, 64, respectively. The     outputs before decoding bounding boxes. For multi-scale,
up-convolutional kernels are initialized as bilinear interpo-   we use NMS to merge results. These augmentations yield
lation. See supplement for a detailed architecture diagram.     different speed-accuracy trade-off, as is shown in the next
                                                                section.
DLA Deep Layer Aggregation (DLA) [58] is an image
classification network with hierarchical skip connections.      6. Experiments
We utilize the fully convolutional upsampling version of           We evaluate our object detection performance on the
DLA for dense prediction, which uses iterative deep ag-         MS COCO dataset [34], which contains 118k training im-
gregation to increase feature map resolution symmetrically.     ages (train2017), 5k validation images (val2017) and 20k
We augment the skip connections with deformable convo-          hold-out testing images (test-dev). We report average pre-
lution [63] from lower layers to the output. Specifically, we   cision over all IOU thresholds (AP), AP at IOU thresholds
replace the original convolution with 3 × 3 deformable con-     0.5(AP50 ) and 0.75 (AP75 ). The supplement contains addi-
volution at every upsampling layer. See supplement for a        tional experiments on PascalVOC [14].
detailed architecture diagram.
    We add one 3 × 3 convolutional layer with 256 channel       6.1. Object detection
before each output head. A final 1 × 1 convolution then            Table 1 shows our results on COCO validation with dif-
produces the desired output. We provide more details in the     ferent backbones and testing options, while Figure 1 com-
supplementary material.                                         pares CenterNet with other real-time detectors. The run-
                                                                ning time is tested on our local machine, with Intel Core
Training We train on an input resolution of 512 × 512.          i7-8086K CPU, Titan Xp GPU, Pytorch 0.4.1, CUDA 9.0,
This yields an output resolution of 128×128 for all the mod-    and CUDNN 7.1. We download code and pre-trained mod-
els. We use random flip, random scaling (between 0.6 to         els12 to test run time for each model on the same machine.
1.3), cropping, and color jittering as data augmentation, and      Hourglass-104 achieves the best accuracy at a relatively
use Adam [28] to optimize the overall objective. We use no      good speed, with a 42.2% AP in 7.8 FPS. On this back-
augmentation to train the 3D estimation branch, as cropping     bone, CenterNet outperforms CornerNet [30] (40.6% AP
or scaling changes the 3D measurements. For the residual        in 4.1 FPS) and ExtremeNet [61](40.3% AP in 3.1 FPS)
networks and DLA-34, we train with a batch-size of 128          in both speed and accuracy. The run time improvement
(on 8 GPUs) and learning rate 5e-4 for 140 epochs, with         comes from fewer output heads and a simpler box decod-
learning rate dropped 10× at 90 and 120 epochs, respec-         ing scheme. Better accuracy indicates that center points are
tively (following [55]). For Hourglass-104, we follow Ex-       easier to detect than corners or extreme points.
tremeNet [61] and use batch-size 29 (on 5 GPUs, with mas-          Using ResNet-101, we outperform RetinaNet [33] with
ter GPU batch-size 4) and learning rate 2.5e-4 for 50 epochs    the same network backbone. We only use deformable con-
with 10× learning rate dropped at the 40 epoch. For detec-      volutions in the upsampling layers, which does not affect
tion, we fine-tune the Hourglass-104 from ExtremeNet [61]       RetinaNet. We are more than twice as fast at the same ac-
to save computation. The down-sampling layers of Resnet-        curacy (CenterNet 34.8%AP in 45 FPS (input 512 × 512)
101 and DLA-34 are initialized with ImageNet pretrain and          1 https://github.com/facebookresearch/Detectron

the up-sampling layers are randomly initialized. Resnet-101        2 https://github.com/pjreddie/darknet
                        Backbone        FPS       AP            AP50         AP75          APS           APM           APL
 MaskRCNN [21] ResNeXt-101      11                39.8          62.3          43.4          22.1          43.2          51.2
 Deform-v2 [63]    ResNet-101    -                46.0          67.9          50.8          27.8          49.1          59.5
 SNIPER [48]         DPN-98     2.5               46.1          67.0          51.6          29.6          48.9          58.1
 PANet [35]       ResNeXt-101    -                47.4          67.2          51.8          30.1          51.7          60.0
 TridentNet [31] ResNet-101-DCN 0.7               48.4          69.7          53.5          31.8          51.3          60.3
 YOLOv3 [45]       DarkNet-53   20                33.0          57.9          34.4          18.3          25.4          41.9
 RetinaNet [33] ResNeXt-101-FPN 5.4               40.8          61.1          44.1          24.1          44.2          51.2
 RefineDet [59]    ResNet-101    -             36.4 / 41.8   57.5 / 62.9   39.5 / 45.7   16.6 / 25.6   39.9 / 45.1   51.4 / 54.1
 CornerNet [30]   Hourglass-104 4.1            40.5 / 42.1   56.5 / 57.8   43.1 / 45.3   19.4 / 20.8   42.7 / 44.8   53.9 / 56.7
 ExtremeNet [61] Hourglass-104  3.1            40.2 / 43.7   55.5 / 60.5   43.2 / 47.0   20.4 / 24.1   43.2 / 46.9   53.1 / 57.6
 FSAF [62]        ResNeXt-101   2.7            42.9 / 44.6   63.8 / 65.2   46.3 / 48.6   26.6 / 29.7   46.2 / 47.1   52.7 / 54.6
 CenterNet-DLA      DLA-34      28             39.2 / 41.6   57.1 / 60.3   42.8 / 45.1   19.9 / 21.5   43.0 / 43.9   51.4 / 56.0
 CenterNet-HG     Hourglass-104 7.8            42.1 / 45.1   61.1 / 63.9   45.9 / 49.3   24.1 / 26.6   45.5 / 47.1   52.8 / 57.7

Table 2: State-of-the-art comparison on COCO test-dev. Top: two-stage detectors; bottom: one-stage detectors. We show
single-scale / multi-scale testing for most one-stage detectors. Frame-per-second (FPS) were measured on the same machine
whenever possible. Italic FPS highlight the cases, where the performance measure was copied from the original publication.
A dash indicates methods for which neither code and models, nor public timings were available.

vs. RetinaNet 34.4%AP in 18 FPS (input 500 × 800)). Our           CenterNet is unable to predict < 0.1% of objects due to col-
fastest ResNet-18 model also achieves a respectable perfor-       lisions in center points. This is much less than slow- or fast-
mance of 28.1% COCO AP at 142 FPS.                                RCNN miss due to imperfect region proposals [52] (∼ 2%),
   DLA-34 gives the best speed/accuracy trade-off. It runs        and fewer than anchor-based methods miss due to insuffi-
at 52FPS with 37.4%AP. This is more than twice as fast as         cient anchor placement [46] (20.0% for Faster-RCNN with
YOLOv3 [45] and 4.4%AP more accurate. With flip testing,          15 anchors at 0.5 IOU threshold). In addition, 715 pairs
our model is still faster than YOLOv3 [45] and achieves ac-       of objects have bounding box IoU > 0.7 and would be
curacy levels of Faster-RCNN-FPN [46] (CenterNet 39.2%            assigned to two anchors, hence a center-based assignment
AP in 28 FPS vs Faster-RCNN 39.8% AP in 11 FPS).                  causes fewer collisions.

                                                                  NMS To verify that IoU based NMS is not needed for
State-of-the-art comparison We compare with other
                                                                  CenterNet, we ran it as a post-processing step on our
state-of-the-art detectors in COCO test-dev in Table 2.
                                                                  predictions. For DLA-34 (flip-test), the AP improves from
With multi-scale evaluation, CenterNet with Hourglass-
                                                                  39.2% to 39.7%. For Hourglass-104, the AP stays at
104 achieves an AP of 45.1%, outperforming all exist-
                                                                  42.2%. Given the minor impact, we do not use it.
ing one-stage detectors. Sophisticated two-stage detec-
tors [31,35,48,63] are more accurate, but also slower. There
                                                                  Next, we ablate the new hyperparameters of our model. All
is no significant difference between CenterNet and sliding
                                                                  the experiments are done on DLA-34.
window detectors for different object sizes or IoU thresh-
olds. CenterNet behaves like a regular detector, just faster.
                                                                  Training and Testing resolution During training, we fix
                                                                  the input resolution to 512 × 512. During testing, we follow
6.1.1   Additional experiments                                    CornerNet [30] to keep the original image resolution and
                                                                  zero-pad the input to the maximum stride of the network.
In unlucky circumstances, two different objects might share       For ResNet and DLA, we pad the image with up to 32 pix-
the same center, if they perfectly align. In this scenario,       els, for HourglassNet, we use 128 pixels. As is shown in
CenterNet would only detect one of them. We start by              Table. 3a, keeping the original resolution is slightly better
studying how often this happens in practice and put it in         than fixing test resolution. Training and testing in a lower
relation to missing detections of competing methods.              resolution (384 × 384) runs 1.7 times faster but drops 3AP.

Center point collision In the COCO training set, there            Regression loss We compare a vanilla L1 loss to a
are 614 pairs of objects that collide onto the same center        Smooth L1 [18] for size regression. Our experiments in Ta-
point at stride 4. There are 860001 objects in total, hence       ble 3c show that L1 is considerably better than Smooth L1.
Resolution AP AP50 AP75 Time               λsize AP AP50 AP75              Loss      AP AP50 AP75         Epoch AP AP50 AP75
Original 36.3 54.0 39.6 19                 0.2 33.5 49.9 36.2              l1        36.3 54.0 39.6       140 36.3 54.0 39.6
512        36.2 54.3 38.7 16               0.1 36.3 54.0 39.6              smooth l1 33.9 50.9 36.8       230 37.4 55.1 40.8
384        33.2 50.5 35.0 11               0.02 35.4 54.6 37.9
(a) Testing resolution: Lager resolu-   (b) Size regression weight.        (c) Regression loss. L1 loss   (d) Training schedule.
tions perform better but run slower.    λsize ≤ 0.1 yields good results.   works better than Smooth L1.   Longer performs better.
  Table 3: Ablation of design choices on COCO validation set. The results are shown in COCO AP, time in milliseconds.
It yields a better accuracy at fine-scale, which the COCO             converges in 70 epochs, with learning rate dropped at the 45
evaluation metric is sensitive to. This is independently ob-          and 60 epoch, respectively. We use the DLA-34 backbone
served in keypoint regression [49, 50].                               and set the loss weight for depth, orientation, and dimen-
                                                                      sion to 1. All other hyper-parameters are the same as the
Bounding box size weight We analyze the sensitivity of                detection experiments.
our approach to the loss weight λsize . Table 3b shows 0.1                Since the number of recall thresholds is quite small, the
gives a good result. For larger values, the AP degrades sig-          validation AP fluctuates by up to 10% AP. We thus train 5
nificantly, due to the scale of the loss ranging from 0 to            models and report the average with standard deviation.
output size w/R or h/R, instead of 0 to 1. However, the                   We compare with slow-RCNN based Deep3DBox [38]
value does not degrade significantly for lower weights.               and Faster-RCNN based method Mono3D [9], on their spe-
                                                                      cific validation split. As is shown in Table 4, our method
Training schedule By default, we train the keypoint esti-             performs on-par with its counterparts in AP and AOS and
mation network for 140 epochs with a learning rate drop at            does slightly better in BEV. Our CenterNet is two orders of
90 epochs. If we double the training epochs before dropping           magnitude faster than both methods.
the learning rate, the performance further increases by 1.1
                                                                      6.3. Pose estimation
AP (Table 3d), at the cost of a much longer training sched-
ule. To save computational resources (and polar bears), we                Finally, we evaluate CenterNet on human pose estima-
use 140 epochs in ablation experiments, but stick with 230            tion in the MS COCO dataset [34]. We evaluate keypoint
epochs for DLA when comparing to other methods.                       AP, which is similar to bounding box AP but replaces the
   Finally, we tried a multiple “anchor” version of Center-           bounding box IoU with object keypoint similarity. We test
Net by regressing to more than one object size. The experi-           and compare with other methods on COCO test-dev.
ments did not yield any success. See supplement.                          We experiment with DLA-34 and Hourglass-104, both
                                                                      fine-tuned from center point detection. DLA-34 converges
6.2. 3D detection                                                     in 320 epochs (about 3 days on 8GPUs) and Hourglass-104
   We perform 3D bounding box estimation experiments on               converges in 150 epochs (8 days on 5 GPUs). All additional
KITTI dataset [17], which contains carefully annotated 3D             loss weights are set to 1. All other hyper-parameters are the
bounding box for vehicles in a driving scenario. KITTI con-           same as object detection.
tains 7841 training images and we follow standard training                The results are shown in Table 5. Direct regression to
and validation splits in literature [10, 54]. The evaluation          keypoints performs reasonably, but not at state-of-the-art. It
metric is the average precision for cars at 11 recalls (0.0 to        struggles particularly in high IoU regimes. Projecting our
1.0 with 0.1 increment) at IOU threshold 0.5, as in object            output to the closest joint detection improves the results
detection [14]. We evaluate IOUs based on 2D bounding                 throughout, and performs competitively with state-of-the-
box (AP), orientation (AOP), and Bird-eye-view bounding               art multi-person pose estimators [4,21,39,41]. This verifies
box (BEV AP). We keep the original image resolution and               that CenterNet is general, easy to adapt to a new task.
pad to 1280×384 for both training and testing. The training               Figure 5 shows qualitative examples on all tasks.

                                     AP                         AOS                      BEV AP
                           Easy    Mode      Hard     Easy    Mode      Hard     Easy    Mode      Hard
    Deep3DBox [38]         98.8     97.2     81.2     98.6     96.7     80.5     30.0     23.7     18.8
    Ours                 90.2±1.2 80.4±1.4 71.1±1.6 85.3±1.7 75.0±1.6 66.2±1.8 31.4±3.7 26.5±1.6 23.8±2.9
    Mono3D [9]             95.8     90.0     80.6     93.7     87.6     78.0     30.5     22.4     19.1
    Ours                 97.1±0.3 87.9±0.1 79.3±0.1 93.4±0.7 83.9±0.5 75.3±0.4 31.5±2.0 29.7±0.7 28.1±4.6
Table 4: KITTI evaluation. We show 2D bounding box AP, average orientation score (AOS), and bird eye view (BEV) AP
on different validation splits. Higher is better.
Figure 5: Qualitative results. All images were picked thematically without considering our algorithms performance. First
row: object detection on COCO validation. Second and third row: Human pose estimation on COCO validation. For each
pair, we show the results of center offset regression (left) and heatmap matching (right). fourth and fifth row: 3D bounding
box estimation on KITTI validation. We show projected bounding box (left) and bird eye view map (right). The ground truth
detections are shown in solid red solid box. The center heatmap and 3D boxes are shown overlaid on the original image.

                         kp   kp   kp
                 AP kp AP50 AP75 APM  APLkp                      7. Conclusion
  CMU-Pose [4]   61.8 84.9 67.5 58.0 70.4
                                                                    In summary, we present a new representation for objects:
  Pose-AE [39]   62.8 84.6 69.2 57.5 70.6
                                                                 as points. Our CenterNet object detector builds on success-
  Mask-RCNN [21] 63.1 87.3 68.7 57.8 71.4
                                                                 ful keypoint estimation networks, finds object centers, and
  PersonLab [41] 66.5 85.5 71.3 62.3 70.0
                                                                 regresses to their size. The algorithm is simple, fast, accu-
  DLA-reg        51.7 81.4 55.2 44.6 63.0
                                                                 rate, and end-to-end differentiable without any NMS post-
  HG-reg         55.0 83.5 59.7 49.4 64.0
                                                                 processing. The idea is general and has broad applications
  DLA-jd         57.9 84.7 63.1 52.5 67.4
                                                                 beyond simple two-dimensional detection. CenterNet can
  HG-jd          63.0 86.8 69.6 58.9 70.4
                                                                 estimate a range of additional object properties, such as
Table 5: Keypoint detection on COCO test-dev. -reg/ -jd are      pose, 3D orientation, depth and extent, in one single for-
for direct center-out offset regression and matching regres-     ward pass. Our initial experiments are encouraging and
sion to the closest joint detection, respectively. The results   open up a new direction for real-time object recognition and
are shown in COCO keypoint AP. Higher is better.                 related tasks.
References                                                      [15] H.-S. Fang, S. Xie, Y.-W. Tai, and C. Lu. RMPE: Re-
                                                                     gional multi-person pose estimation. In ICCV, 2017.
 [1] S. Antol, A. Agrawal, J. Lu, M. Mitchell, D. Batra,
     C. Lawrence Zitnick, and D. Parikh. Vqa: Visual            [16] C.-Y. Fu, W. Liu, A. Ranga, A. Tyagi, and A. C. Berg.
     question answering. In ICCV, 2015.                              Dssd: Deconvolutional single shot detector. arXiv
                                                                     preprint arXiv:1701.06659, 2017.
 [2] N. Bodla, B. Singh, R. Chellappa, and L. S. Davis.
     Soft-nmsimproving object detection with one line of        [17] A. Geiger, P. Lenz, and R. Urtasun. Are we ready for
     code. In ICCV, 2017.                                            autonomous driving? the kitti vision benchmark suite.
                                                                     In CVPR, 2012.
 [3] Z. Cao, G. Hidalgo, T. Simon, S.-E. Wei, and
     Y. Sheikh. OpenPose: realtime multi-person 2D pose         [18] R. Girshick. Fast r-cnn. In ICCV, 2015.
     estimation using Part Affinity Fields. In arXiv preprint   [19] R. Girshick, J. Donahue, T. Darrell, and J. Malik. Rich
     arXiv:1812.08008, 2018.                                         feature hierarchies for accurate object detection and
 [4] Z. Cao, T. Simon, S.-E. Wei, and Y. Sheikh. Real-               semantic segmentation. In CVPR, 2014.
     time multi-person 2d pose estimation using part affin-     [20] P. Goyal, P. Dollár, R. Girshick, P. Noordhuis,
     ity fields. In CVPR, 2017.                                      L. Wesolowski, A. Kyrola, A. Tulloch, Y. Jia, and
 [5] J. Carreira and A. Zisserman. Quo vadis, action recog-          K. He. Accurate, large minibatch sgd: Training im-
     nition? a new model and the kinetics dataset. In                agenet in 1 hour. arXiv preprint arXiv:1706.02677,
     CVPR, 2017.                                                     2017.

 [6] F. Chabot, M. Chaouch, J. Rabarisoa, C. Teuliere, and      [21] K. He, G. Gkioxari, P. Dollár, and R. Girshick. Mask
     T. Chateau. Deep manta: A coarse-to-fine many-                  r-cnn. In ICCV, 2017.
     task network for joint 2d and 3d vehicle analysis from     [22] K. He, X. Zhang, S. Ren, and J. Sun. Deep residual
     monocular image. In CVPR, 2017.                                 learning for image recognition. In CVPR, 2016.
 [7] L.-C. Chen, G. Papandreou, I. Kokkinos, K. Murphy,         [23] J. H. Hosang, R. Benenson, and B. Schiele. Learning
     and A. L. Yuille. Deeplab: Semantic image segmenta-             non-maximum suppression. In CVPR, 2017.
     tion with deep convolutional nets, atrous convolution,     [24] H.-N. Hu, Q.-Z. Cai, D. Wang, J. Lin, M. Sun,
     and fully connected crfs. TPAMI, 2018.                          P. Krähenbühl, T. Darrell, and F. Yu. Joint monocu-
 [8] X. Chen and A. Gupta. An implementation of faster               lar 3d vehicle detection and tracking. arXiv preprint
     rcnn with study for region sampling. arXiv preprint             arXiv:1811.10742, 2018.
     arXiv:1702.02138, 2017.                                    [25] J. Huang, V. Rathod, C. Sun, M. Zhu, A. Korattikara,
 [9] X. Chen, K. Kundu, Z. Zhang, H. Ma, S. Fidler, and              A. Fathi, I. Fischer, Z. Wojna, Y. Song, S. Guadar-
     R. Urtasun. Monocular 3d object detection for au-               rama, et al. Speed/accuracy trade-offs for modern con-
     tonomous driving. In CVPR, 2016.                                volutional object detectors. In CVPR, 2017.
[10] X. Chen, K. Kundu, Y. Zhu, A. G. Berneshawi, H. Ma,        [26] B. Jiang, R. Luo, J. Mao, T. Xiao, and Y. Jiang. Ac-
     S. Fidler, and R. Urtasun. 3d object proposals for ac-          quisition of localization confidence for accurate object
     curate object class detection. In NIPS, 2015.                   detection. In ECCV, 2018.
[11] J. Dai, Y. Li, K. He, and J. Sun. R-fcn: Object detec-     [27] Z. Kalal, K. Mikolajczyk, and J. Matas. Tracking-
     tion via region-based fully convolutional networks. In          learning-detection. TPAMI, 2012.
     NIPS, 2016.                                                [28] D. P. Kingma and J. Ba. Adam: A method for stochas-
[12] J. Dai, H. Qi, Y. Xiong, Y. Li, G. Zhang, H. Hu, and            tic optimization. ICLR, 2014.
     Y. Wei. Deformable convolutional networks. In ICCV,        [29] A. Kundu, Y. Li, and J. M. Rehg.           3d-rcnn:
     2017.                                                           Instance-level 3d object reconstruction via render-
[13] D. Eigen, C. Puhrsch, and R. Fergus. Depth map pre-             and-compare. In CVPR, 2018.
     diction from a single image using a multi-scale deep       [30] H. Law and J. Deng. Cornernet: Detecting objects as
     network. In NIPS, 2014.                                         paired keypoints. In ECCV, 2018.
[14] M. Everingham, L. Van Gool, C. K. I. Williams,             [31] Y. Li, Y. Chen, N. Wang, and Z. Zhang. Scale-aware
     J. Winn, and A. Zisserman. The PASCAL Visual Ob-                trident networks for object detection. arXiv preprint
     ject Classes Challenge 2012 (VOC2012) Results.                  arXiv:1901.01892, 2019.
[32] Y. Li, H. Qi, J. Dai, X. Ji, and Y. Wei. Fully con-        [47] B. Singh and L. S. Davis. An analysis of scale invari-
     volutional instance-aware semantic segmentation. In             ance in object detection–snip. In CVPR, 2018.
     CVPR, 2017.                                                [48] B. Singh, M. Najibi, and L. S. Davis. SNIPER: Effi-
[33] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár.        cient multi-scale training. NIPS, 2018.
     Focal loss for dense object detection. ICCV, 2017.         [49] X. Sun, J. Shang, S. Liang, and Y. Wei. Compositional
[34] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona,           human pose regression. In ICCV, 2017.
     D. Ramanan, P. Dollár, and C. L. Zitnick. Microsoft       [50] X. Sun, B. Xiao, F. Wei, S. Liang, and Y. Wei. Integral
     coco: Common objects in context. In ECCV, 2014.                 human pose regression. In ECCV, 2018.
[35] S. Liu, L. Qi, H. Qin, J. Shi, and J. Jia. Path aggre-     [51] A. Toshev and C. Szegedy. Deeppose: Human pose
     gation network for instance segmentation. In CVPR,              estimation via deep neural networks. In CVPR, 2014.
     2018.                                                      [52] J. R. Uijlings, K. E. Van De Sande, T. Gevers, and
[36] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed,             A. W. Smeulders. Selective search for object recogni-
     C.-Y. Fu, and A. C. Berg. Ssd: Single shot multibox             tion. IJCV, 2013.
     detector. In ECCV, 2016.                                   [53] D. Wang, C. Devin, Q.-Z. Cai, F. Yu, and T. Darrell.
[37] J. Long, E. Shelhamer, and T. Darrell. Fully convolu-           Deep object centric policies for autonomous driving.
     tional networks for semantic segmentation. In CVPR,             In ICRA, 2019.
     2015.                                                      [54] Y. Xiang, W. Choi, Y. Lin, and S. Savarese.
[38] A. Mousavian, D. Anguelov, J. Flynn, and J. Kosecka.            Subcategory-aware convolutional neural networks for
     3d bounding box estimation using deep learning and              object proposals and detection. In WACV, 2017.
     geometry. In CVPR, 2017.                                   [55] B. Xiao, H. Wu, and Y. Wei. Simple baselines for
[39] A. Newell, Z. Huang, and J. Deng. Associative em-               human pose estimation and tracking. In ECCV, 2018.
     bedding: End-to-end learning for joint detection and       [56] S. Xie, R. Girshick, P. Dollár, Z. Tu, and K. He. Ag-
     grouping. In NIPS, 2017.                                        gregated residual transformations for deep neural net-
[40] A. Newell, K. Yang, and J. Deng. Stacked hourglass              works. In CVPR, 2017.
     networks for human pose estimation. In ECCV, 2016.         [57] J. Xu, R. Zhao, F. Zhu, H. Wang, and W. Ouyang.
[41] G. Papandreou, T. Zhu, L.-C. Chen, S. Gidaris,                  Attention-aware compositional network for person re-
     J. Tompson, and K. Murphy. Personlab: Person pose               identification. In CVPR, 2018.
     estimation and instance segmentation with a bottom-        [58] F. Yu, D. Wang, E. Shelhamer, and T. Darrell. Deep
     up, part-based, geometric embedding model. ECCV,                layer aggregation. In CVPR, 2018.
     2018.                                                      [59] S. Zhang, L. Wen, X. Bian, Z. Lei, and S. Z. Li.
[42] G. Papandreou, T. Zhu, N. Kanazawa, A. Toshev,                  Single-shot refinement neural network for object de-
     J. Tompson, C. Bregler, and K. Murphy. Towards ac-              tection. In CVPR, 2018.
     curate multi-person pose estimation in the wild. In        [60] X. Zhou, A. Karpur, L. Luo, and Q. Huang. Starmap
     CVPR, 2017.                                                     for category-agnostic keypoint and viewpoint estima-
[43] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi.             tion. In ECCV, 2018.
     You only look once: Unified, real-time object detec-       [61] X. Zhou, J. Zhuo, and P. Krähenbühl. Bottom-up ob-
     tion. In CVPR, 2016.                                            ject detection by grouping extreme and center points.
[44] J. Redmon and A. Farhadi. Yolo9000: better, faster,             In CVPR, 2019.
     stronger. CVPR, 2017.                                      [62] C. Zhu, Y. He, and M. Savvides. Feature selective
[45] J. Redmon and A. Farhadi. Yolov3: An incremen-                  anchor-free module for single-shot object detection.
     tal improvement. arXiv preprint arXiv:1804.02767,               arXiv preprint arXiv:1903.00621, 2019.
     2018.                                                      [63] X. Zhu, H. Hu, S. Lin, and J. Dai. Deformable con-
[46] S. Ren, K. He, R. Girshick, and J. Sun. Faster r-cnn:           vnets v2: More deformable, better results. arXiv
     Towards real-time object detection with region pro-             preprint arXiv:1811.11168, 2018.
     posal networks. In NIPS, 2015.
     IN             OUT    (a)                OUT        IN       (b)   OUT        IN            (c)              OUT        IN            (d)

      4       4       4          4      4       4        4               4          4        4             4       4         4         4         4        4

      8       8       8          8      8       8        8               8          8        8             8                 8         8         8        4

     16      16      16          16    16      16        16              16        16        16                              16       16                  4

     32      32      32          32    32      32        32              32        32                                        32                           4

     64      64      64          64    64      64                                                                                                    OUT
                                                              Sum Node            Up Node                      Deform Conv                 Stage
     128             128         128           128

Figure 6: Model diagrams. The numbers in the boxes represent the stride to the image. (a): Hourglass Network [30]. We
use it as is in CornerNet [30]. (b): ResNet with transpose convolutions [55]. We add one 3 × 3 deformable convolutional
layer [63] before each up-sampling layer. Specifically, we first use deformable convolution to change the channels and then
use transposed convolution to upsample the feature map (such two steps are shown separately in 32 → 16. We show these
two steps together as a dashed arrow for 16 → 8 and 8 → 4). (c): The original DLA-34 [58] for semantic segmentation.
(d): Our modified DLA-34. We add more skip connections from the bottom layers and upgrade every convolutional layer in
upsampling stages to deformable convolutional layer.

Appendix A: Model Architecture                                          bin center mi ). I.e., α̂ = [b̂1 , â1 , b̂2 , â2 ] The classification
                                                                        are trained with softmax and the angular values are trained
   See figure. 6 for diagrams of the architectures.                     with L1 loss:
Appendix B: 3D BBox Estimation Details                                                  1 XX
                                                                                            N          2
                                                                              Lori =           (sof tmax(b̂i , ci ) + ci |âi − ai |) (7)
    Our network outputs maps for depths D̂ ∈ R R × R ,
                                                         W    H                         N  i=1
                                                                                            k=1
                         W  H
3d dimensions Γ̂ ∈ R R × R ×3 , and orientation encoding
         W   H
Â ∈ R R × R ×8 . For each object instance k, we extract                where ci = 1(θ ∈ Bi ), ai = (sin (θ − mi ), cos (θ − mi )).
the output values from the three output maps at the ground              1 is the indicator function. The predicted orientation θ is
truth center point location: dˆk ∈ R, γ̂k ∈ R3 , α̂k ∈ R8 .             decoded from the 8-scalar encoding by
The depth is trained with L1 loss after converting the output
                                                                                             θ̂ = arctan2(âj1 , âj2 ) + mj                                  (8)
to the absolute depth domain:
                            N
                                                                        where j is the bin index which has a larger classification
                     1 X     1                                          score.
              Ldep =     |         − 1 − dk |                 (5)
                     N     σ(dˆk )
                           k=1
                                                                        Appendix C: Collision Experiment Details
where dk is the groud truth absolute depth (in meter). Sim-
                                                                           We analysis the annotations of COCO training set to
ilarly, the 3D dimension is trained with L1 Loss in absolute
                                                                        show how often the collision cases happen. COCO train-
metric:
                               N                                        ing set (train 2017) contains N = 118287 images and M =
                           1 X
                  Ldim =          |γ̂k − γk |            (6)            860001 objects (with MS = 356340 small objects, MM =
                          N                                             295163 medium objects, and ML = 208498 large objects)
                                 k=1

where γk is the object height, width, and length in meter.              in C = 80 categories. Let the i-th bounding box of image k
                                                                                                       (kci) (kci) (kci) (kci)
   The orientation θ is a single scalar by default. Following           of category c be bb(kci) = (x1 , y1 , x2 , y2 ), its
                                                                                                                                      (kci)      (kci)
                                                                                                                                     x1       +x2
Mousavian et al. [24, 38], We use an 8-scalar encoding to               center after the 4× stride is pkci = (b 41 ·                          2          c, b 41 ·
ease learning. The 8 scalars are divided into two groups,                 (kci)
                                                                         y1
                                                                                    (kci)
                                                                                  +y2
                                                                                     c). And Let n(kc) be the number of object of
each for an angular bin. One bin is for angles in B1 =                            2
                                                                        category c in image k. The number of center point colli-
[− 7π   π                                                 π 7π
    6 , 6 ] and the other is for angles in B2 = [− 6 , 6 ].             sions is calculated by:
Thus we have 4 scalars for each bin. Within each bin, 2 of
the scalars bi ∈ R2 are used for softmax classification (if                                        N X
                                                                                                     C nX nX        (kc)   (kc)

the orientation falls into to this bin i). And the rest 2 scalars                                                                 1(pkci = pkcj )
                                                                                                   X
                                                                                   Ncenter =                                                                  (9)
ai ∈ R2 are for the sin and cos value of in-bin offset (to the                                     k=1 c=1 i=1 j=i+1
We get Ncenter = 614 on the dataset.                                                         Resolution mAP@0.5 FPS
  Similarly, we calculate the IoU based collision by                        Faster RCNN [46] 600 × 1000 76.4     5
                      (kc)   (kc)
                                                                            Faster RCNN* [8] 600 × 1000 79.8     5
            N X
              C nX nX
                                                                            R-FCN [11]       600 × 1000 80.5     9
                                    1(IoU (bb(kci) , bb(kcj) ) > t)
            X
NIoU @t =
                                                                            Yolov2 [44]      544 × 544    78.6   40
            k=1 c=1 i=1 j=i+1
                                                              (10)          SSD [16]         513 × 513    78.9   19
This gives NIoU @0.7 = 715 and NIoU @0.5 = 5179.                            DSSD [16]        513 × 513    81.5  5.5
                                                                            RefineDet [59]   512 × 512    81.8   24
                                                                            CenterNet-Res18 384 × 384     72.6  142
Missed objects in anchor based detector. Reti-
                                                                            CenterNet-Res18 512 × 512     75.7  100
naNet [33] assigns anchors to a ground truth bounding box
                                                                            CenterNet-Res101 384 × 384    77.6   45
if they have > 0.5 IoU. In the case that a ground truth
                                                                            CenterNet-Res101 512 × 512    78.7   30
bounding box has not been covered by any anchor with IoU
                                                                            CenterNet-DLA 384 × 384       79.3   50
> 0.5, the anchor with the largest IoU will be assigned to
                                                                            CenterNet-DLA 512 × 512       80.7   33
it. We calculate how often this forced assignment happens.
We use 15 anchors (5 size: 32, 64, 128, 256, 512, and 3               Table 6: Experimental results on Pascal VOC 2007 test. The
aspect-ratio: 0.5, 1, 2, as is in RetinaNet [33]) at stride           results are shown in mAP@0.5. Flip test is used for Cen-
S = 16. For each image, after resizing it as its shorter              terNet. The FPSs for other methods are copied from the
edge to be 800 [33], we place these anchors at positions              original publications.
{(S/2 + i × S, S/2 + j × S)}, where i ∈ [0, b (W −S/2) S     c]
and j ∈ [0, b (H−S/2)
                  S    c].  W, H   are the image  weight   and                                        AP AP50 AP75
height (the smaller one is equal to 800). This results in a set                                       36.3 54.0 39.6
of anchors A. |A| = 15 × b (W −S/2)
                                S      + 1c × b (H−S/2)
                                                   S     + 1c.                  w/ gt size            41.9 56.6 45.4
We calculate the number of the forced assignments by:                           w/ gt heatmap         54.2 82.6 58.1
                     (k)
                                                                                w/ gt heatmap+size 83.1 97.9 90.1
                N n
                                                                                w/ gt hm.+size+offset 99.5 99.7 99.6
                           1((max IoU (bb(k·i) , A)) < 0.5)
                X X
   Nanchor =
                              A∈A
                k=1 i=1
                                                        (11)          Table 7: Error analysis on COCO validation. We show
RenitaNet requires Nanchor = 170220 forced assignments:               COCO AP(%) after replacing each network prediction with
125831 for small objects (35.3% of all small objects),                its ground truth.
18505 for medium objects (6.3% of all medium objects),
and 25884 for large objects (12.4% of all large objects).
                                                                         The results are shown in Table. 6. Our best CenterNet-
                                                                      DLA model performs competitively with top-tier methods,
Appendix D: Experiments on PascalVOC
                                                                      and keeps a real-time speed.
    Pascal VOC [14] is a popular small object detection
dataset. We train on VOC 2007 and VOC 2012 trainval                   Appendix E: Error Analysis
sets, and test on VOC 2007 test set. It contains 16551 train-
                                                                         We perform an error analysis by replacing each output
ing images and 4962 testing images of 20 categories. The
                                                                      head with its ground truth. For the center point heatmap,
evaluation metric is mean average precision (mAP) at IOU
                                                                      we use the rendered Gaussian ground truth heatmap. For
threshold 0.5.
                                                                      the bounding box size, we use the nearest ground truth size
    We experiment with our modified ResNet-18, ResNet-
                                                                      for each detection.
101, and DLA-34 (See main paper Section. 5) in two train-
                                                                         The results in Table 7 show that improving both size map
ing resolution: 384 × 384 and 512 × 512. For all networks,
                                                                      leads to a modest performance gain, while the center map
we train 70 epochs with learning rate dropped 10× at 45
                                                                      gains are much larger. If only the keypoint offset is not pre-
and 60 epochs, respectively. We use batchsize 32 and learn-
                                                                      dicted, the maximum AP reaches 83.1. The entire pipeline
ing rate 1.25e-4 following the linear learning rate rule [20].
                                                                      on ground truth misses about 0.5% of objects, due to dis-
It takes one GPU 7 hours/ 10 hours to train in 384 × 384 for
                                                                      cretization and estimation errors in the Gaussian heatmap
ResNet-101 and DLA-34, respectively. And for 512 × 512,
                                                                      rendering.
the training takes the same time in two GPUs. Flip augmen-
tation is used in testing. All other hyper-parameters are the
same as the COCO experiments. We do not use Hourglass-
104 [30] because it fails to converge in a reasonable time (2
days) when trained from scratch.
