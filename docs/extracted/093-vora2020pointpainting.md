---
source_id: 093
bibtex_key: vora2020pointpainting
title: PointPainting: Sequential Fusion for 3D Object Detection
year: 2020
domain_theme: Deteksi 3D
verified_pdf: 93_PointPainting.pdf
char_count: 70383
---

PointPainting: Sequential Fusion for 3D Object Detection

                                                       Sourabh Vora              Alex H. Lang     Bassam Helou                                                 Oscar Beijbom
                                                                                   nuTonomy: an Aptiv Company
                                                                          {sourabh, alex, bassam, oscar}@nutonomy.com
arXiv:1911.10150v2 [cs.CV] 6 May 2020

                                                                 Abstract                                                                                       KITTI
                                                                                                                             90                                                        90
                                                                                                                             85                                                        85

                                                                                                         Performance (mAP)

                                                                                                                                                                    Performance (AP)
                                             Camera and lidar are important sensor modalities for
                                                                                                                             80                                                        80
                                        robotics in general and self-driving cars in particular. The
                                                                                                                             75                                                        75
                                        sensors provide complementary information offering an op-
                                                                                                                             70                                                        70
                                        portunity for tight sensor-fusion. Surprisingly, lidar-only
                                                                                                                             65                                                        65
                                        methods outperform fusion methods on the main benchmark
                                                                                                                             60                                                        60
                                        datasets, suggesting a gap in the literature. In this work,                               PointPillars VoxelNet PointRCNN                           car   ped   cyclist
                                        we propose PointPainting: a sequential fusion method to                                                              nuScenes
                                                                                                                             80                                                        80
                                        fill this gap. PointPainting works by projecting lidar points
                                                                                                         Performance (mAP)
                                                                                                                                                    Original

                                                                                                                                                                    Performance (AP)
                                        into the output of an image-only semantic segmentation net-                          60                                                        60
                                                                                                                                                    Painted
                                        work and appending the class scores to each point. The ap-                           40                                                        40
                                        pended (painted) point cloud can then be fed to any lidar-
                                                                                                                             20                                                        20
                                        only method. Experiments show large improvements on
                                        three different state-of-the art methods, Point-RCNN, Vox-                            0                                                         0
                                                                                                                                  PointPillars+                                             car   ped   bicycle
                                        elNet and PointPillars on the KITTI and nuScenes datasets.
                                        The painted version of PointRCNN represents a new state of       Figure 1. PointPainting is a general fusion method that be can
                                        the art on the KITTI leaderboard for the bird’s-eye view de-     used with any lidar detection network. Top left: PointPillars[11],
                                        tection task. In ablation, we study how the effects of Paint-    VoxelNet [34, 29], and PointRCNN [21] on the KITTI [6] bird’s-
                                        ing depends on the quality and format of the semantic seg-       eye view val set (Table 1). The painted version of PointRCNN is
                                                                                                         state of the art on the KITTI test set outperforming all published
                                        mentation output, and demonstrate how latency can be min-
                                                                                                         fusion and lidar-only methods (Table 2). Top right: improvements
                                        imized through pipelining.
                                                                                                         are larger for the harder pedestrian (ped.) and cyclist classes. Error
                                                                                                         bars indicate std. across methods. Bottom left: PointPillars+ eval-
                                                                                                         uated on the nuScenes [1] test set. The painted version of PointPil-
                                        1. Introduction                                                  lars+ improves all 10 classes for a total boost of 6.3 mAP (Table
                                                                                                         3). Bottom right: selected class improvements for Painted Point-
                                            Driven partially by the interest in self-driving vehicles,   Pillars+ show the challenging bicycle class has the largest gains.
                                        significant research effort has been devoted to 3D object de-
                                        tection. In this work we consider the problem of fusing a
                                        lidar point cloud with an RGB image. The point cloud pro-        the popular KITTI leaderboard [6] are lidar only. Does this
                                        vides a very accurate range view, but with low resolution        mean lidar makes vision redundant for 3D object detection?
                                        and texture information. The image, on the other hand, has          The answer, surely, must be no. Consider the example in
                                        an inherent depth ambiguity but offers fine-grained texture      Fig. 3, where the pedestrian and signpost are clearly visible
                                        and color information. This offers the compelling research       in the image, yet look more or less identical in the lidar
                                        opportunity of how to design a detector which utilizes the       modality. Surely vision based semantic information should
                                        best of two worlds.                                              be useful to improve detection of such objects. Also, by first
                                            Early work on KITTI [6] such as MV3D [3] and                 principle, adding more information should at the minimum
                                        AVOD [10] proposed multi-view fusion pipelines to exploit        yield the same result, not worse. So why has it been so
                                        these synergies. However recent detectors such as PointPil-      difficult? One reason is due to viewpoint misalignment.
                                        lars [11], VoxelNet [34, 29] and STD [32] use only lidar and        While both sensors are natively captured in the range-
                                        still significantly outperform these methods. Indeed, despite    view, most state of the art methods such as PointPillars [11]
                                        recent fusion research [18, 27, 13, 33], the top methods on      or STD [32] use convolutions in the bird’s-eye view. This
                                                                                                  3
                                             2
                                                                                             Lidar
                                         Point                                               Detector
                                         Painting
                                                                                                 e.g.
                                                                                             Point-RCNN
                                                                                             PointPillars
                                                                                                 etc

                                                               2   Point Painting

                                             1
                                         Sem. Seg

Figure 2. PointPainting overview. The PointPainting architecture consists of three main stages: (1) image based semantics network, (2)
fusion (painting), and (3) lidar based detector. In the first step, the images are passed through a semantic segmentation network obtaining
pixelwise segmentation scores. In the second stage, the lidar points are projected into the segmentation mask and decorated with the scores
obtained in the earlier step. Finally, a lidar based object detector can be used on this decorated (painted) point cloud to obtain 3D detections.

view has several advantages including lack of scale ambigu-                 do the fusion there [25, 28, 33]. Some of the most promis-
ity and minimal occlusions. It also does not suffer from the                ing image-only methods use this idea of first creating an
depth-blurring effect which occurs with applying 2D con-                    artificial point cloud from the image and then proceeding
volutions to the range view [25]. As a result, bird’s-eye                   in the bird’s-eye view [25, 28]. Subsequent work attempts
view methods outperform top range-view methods, such as                     fusion based on this idea, but the performance falls short of
LaserNet [17, 16], on the KITTI leaderboard. However,                       state of the art [33], and requires several expensive steps of
while a lidar point cloud can trivially be converted to bird’s-             processing to build the pseudo-point cloud.
eye view, it is much more difficult to do so with an image.                     A fourth family of methods uses detection seeding.
    Hence, a core challenge of sensor fusion network design                 There, semantics are extracted from an image a priori and
lies in consolidating the lidar bird’s-eye view with the cam-               used to seed detection in the point cloud. Frustrum Point-
era view. Previous methods can be grouped into four cate-                   Net [18] and ConvNet [26] use the 2D detections to limit the
gories: object-centric fusion, continuous feature fusion, ex-               search space inside the frustum while IPOD [31] uses se-
plicit transform and detection seeding.                                     mantic segmentation outputs to seed the 3D proposal. This
    Object-centric fusion, pioneered by MV3D [3] and                        improves precision, but imposes an upper bound on recall.
AVOD [10], is the most obvious choice for a two-stage ar-                       The recent work of Liang et. al [13] tried combining
chitecture. Here, the modalities have different backbones,                  several of these concepts. Results are not disclosed for all
one in each view, and fusion happens at the object pro-                     classes, but the method is outperformed on the car class by
posal level by applying roi-pooling in each modality from                   the top lidar-only method STD [32] (Table 2).
a shared set of 3D proposals. This allows for end-to-end                        In this work we propose PointPainting: a simple yet ef-
optimization but tends to be slow and cumbersome.                           fective sequential fusion method. Each lidar point is pro-
    A second family of methods applies “continuous feature                  jected into the output of an image semantic segmentation
fusion” to allow feature information to be shared across all                network and the channel-wise activations are concatenated
strides of the image and lidar backbones [14, 27]. These                    to the intensity measurement of each lidar point. The con-
methods can be used with single-state detection designs but                 catenated (painted) lidar points can then be used in any lidar
require a mapping to be calculated, a priori, for each sam-                 detection method, whether bird’s-eye view [11, 29, 21, 34,
ple, from the point-cloud to the image. One subtle but im-                  30, 32] or front-view [12, 17]. PointPainting addresses the
portant draw-back of this family of methods is “feature-                    shortcomings of the previous fusion concepts: it does not
blurring”. This occurs since each feature vector from the                   add any restrictions on the 3D detection architecture; it does
bird’s-eye view corresponds to multiple pixels in the image-                not suffer from feature or depth blurring; it does not require
view, and vice versa. ContFuse [14] proposes a sophisti-                    a pseudo-point cloud to be computed, and it does not limit
cated method based on kNN, bilinear interpolation and a                     the maximum recall.
learned MLP to remedy this, but the core problem persists.                      Note that for lidar detection methods that operate di-
    A third family of methods attempts to explicitly trans-                 rectly on the raw point cloud [11, 34, 17, 21], PointPainting
form the image to a bird’s-eye view representation [20] and                 requires minimal network adaptations such as changing the
                                   mAP                Car                       Pedestrian                  Cyclist
                  Method
                                   Mod.      Easy     Mod.      Hard     Easy     Mod.     Hard      Easy    Mod.      Hard
             PointPillars [11]     73.78     90.09    87.57    86.03    71.97     67.84   62.41     85.74    65.92    62.40
            Painted PointPillars   76.27     90.01    87.65    85.56    77.25     72.41   67.53     81.72    68.76    63.99
                   Delta           +2.50     -0.08     0.08    -0.47    +5.28     +4.57   +5.12     -4.02    +2.84    +1.59
             VoxelNet [34, 29]     71.83     89.87    87.29    86.30    70.08     62.44   55.02     85.48    65.77    58.97
             Painted VoxelNet      73.55     90.05    87.51    86.66    73.16     65.05   57.33     87.46    68.08    65.59
                   Delta           +1.71     +0.18    +0.22    +0.36    +3.08     +2.61   +2.31     +1.98    +2.31    +6.62
             PointRCNN [21]        72.42     89.78    86.19    85.02    68.37     63.49   57.89     84.65    67.59    63.06
            Painted PointRCNN      75.80     90.19    87.64    86.71    72.65     66.06   61.24     86.33    73.69    70.17
                   Delta           +3.37     +0.41    +1.45    +1.69    +4.28     +2.57   +3.35     +1.68    +6.10    +7.11
Table 1. PointPainting applied to state of the art lidar based object detectors. All lidar methods show an improvement in bird’s-eye view
(BEV) mean average precision (mAP) of car, pedestrian, and cyclist on KITTI val set, moderate split. The corresponding 3D results are
included in Table 7 in the Supplementary Material where we observe a similar improvement.

                                                                       Contributions. Our main contribution is a novel fusion
                                                                       method, PointPainting, that augments the point cloud with
                                                                       image semantics. Through extensive experimentation we
                                                                       show that PointPainting is:
                                                                         • general – achieving significant improvements when
                                                                           used with 3 top lidar-only methods on the KITTI and
                                                                           nuScenes benchmarks;
Figure 3. Example scene from the nuScenes [1] dataset. The               • accurate – the painted version of PointRCNN
pedestrian and pole are 25 meters away from the ego vehicle.
                                                                           achieves state of the art on the KITTI benchmark;
At this distance the two objects appears very similar in the point
cloud. The proposed PointPainting method would add semantics
                                                                         • robust – the painted versions of PointRCNN and
from the image making the lidar detection task easier.                     PointPillars improved performance on all classes on
                                                                           the KITTI and nuScenes test sets, respectively.
                                                                         • fast – low latency fusion can be achieved by pipelining
                                                                           the image and lidar processing steps.
number of channels dedicated to reading the point cloud.
For methods using hand-coded features [30, 22], some ex-               2. PointPainting Architecture
tra work is required to modify the feature encoder.
                                                                          The PointPainting architecture accepts point clouds and
    PointPainting is sequential by design which means that it          images as input and estimates oriented 3D boxes. It consists
is not always possible to optimize, end-to-end, for the final          of three main stages (Fig. 2). (1) Semantic Segmentation:
task of 3D detection. In theory, this implies sub-optimality           an image based sem. seg. network which computes the
in terms of performance. Empirically, however, PointPaint-             pixel wise segmentation scores. (2) Fusion: lidar points are
ing is more effective than all other proposed fusion meth-             painted with sem. seg. scores. (3) 3D Object Detection: a
ods. Further, a sequential approach has other advantages:              lidar based 3D detection network.
(1) semantic segmentation of an image is often a useful
stand-alone intermediate product, and (2) in a real-time 3D            2.1. Image Based Semantics Network
detection system, latency can be reduced by pipelining the                 The image sem. seg. network takes in an input image
image and lidar networks such that the lidar points are deco-          and outputs per pixel class scores. These scores serve as
rated with the semantics from the previous image. We show              compact summarized features of the image. There are sev-
in ablation that such pipelining does not affect performance.          eral key advantages of using sem. seg. in a fusion pipeline.
   We implement PointPainting with three state of the art              First, sem. seg. is an easier task than 3D object detection
lidar-only methods that have public code: PointPillars [11],           since segmentation only requires local, per pixel classifi-
VoxelNet (SECOND) [34, 29], and PointRCNN [21]. Point-                 cation, while object detection requires 3D localization and
Painting consistently improved results (Figure 1) and in-              classification. Networks that perform sem. seg. are eas-
deed, the painted version of PointRCNN achieves state of               ier to train and are also amenable to perform fast inference.
the art on the KITTI leaderboard (Table 2). We also show               Second, rapid advances are being made in sem. seg. [4, 36],
a significant improvement of 6.3 mAP (Table 4) for Painted             which allows PointPainting to benefit from advances in both
PointPillars+ on nuScenes [1].                                         segmentation and 3D object detection. Finally, in a robotics
A                                                                       B

C                                                                       D

Figure 4. Qualitative analysis of KITTI results. We created four different comparison figures. For each comparison, the upper left is the
original point cloud, while the upper right is the painted point cloud with the segmentation outputs used to color car (orange), cyclist (red)
and pedestrian (blue) points. PointPillars / Painted PointPillars predicted 3D bounding boxes are displayed on the both the input point
cloud (upper left / right) and projected into the image (lower left / right). The orientation of boxes is shown by a line connecting the bottom
center to the front of the box.

or autonomous vehicle system, sem. seg. outputs are useful                ble when using multiple lidar sweeps [1]). The lidar points
independent outputs for tasks like free-space estimation.                 are transformed by a homogenous transformation followed
   In this paper, the segmentation scores for our KITTI                   by a projection into the image. For KITTI this transforma-
experiments are generated from DeepLabv3+ [2, 36, 19],                    tion is given by Tcamera←lidar . The nuScenes transforma-
while for nuScenes experiments we trained a custom,                       tion requires extra care since the lidar and cameras operate
lighter, network. However, we note that PointPainting is                  at different frequencies. The complete transformation is:
agnostic to the image segmentation network design.
                                                                                  T = T(camera←ego) T(egotc ←egotl ) T(ego←lidar)
2.2. PointPainting
                                                                          with transforms: lidar frame to the ego-vehicle frame; ego
                                                                          frame at time of lidar capture, tl , to ego frame at the image
Algorithm 1 PointPainting(L, S, T, M)                                     capture time, tc ; and ego frame to camera frame. Finally,
  Inputs:                                                                 the camera matrix, M , projects the points into the image.
  Lidar point cloud L ∈ RN,D with N points and D ≥ 3.                        The output of the segmentation network is C class
  Segmentation scores S ∈ RW,H,C with C classes.                          scores, where for KITTI C = 4 (car, pedestrian, cyclist,
  Homogenous transformation matrix T ∈ R4,4 .                             background) and for nuScenes C = 11 (10 detection classes
  Camera matrix M ∈ R3,4 .                                                plus background). Once the lidar points are projected into
                                                                          the image, the segmentation scores for the relevant pixel, (h,
  Output:                                                                 w), are appended to the lidar point to create the painted li-
  Painted lidar points P ∈ RN,D+C                                         dar point. Note, if the field of view of two cameras overlap,
                                                                          there will be some points that will project on two images
  for ~l ∈ L do                                                           simultaneously and we randomly choose the segmentation
      ~limage = PROJECT(M, T, ~lxyz )               . ~limage ∈ R2        score vector from one of the two images. Another strat-
       ~s = S[~limage [0], ~limage [1], :]                . ~s ∈ RC       egy can be to choose the more discriminative score vector
        p~ = Concatenate(~l, ~s)                     . p~ ∈ RD+C          by comparing their entropies or the margin between the top
  end for                                                                 two scores. However, we leave that for future studies.
                                                                          2.3. Lidar Detection
    Here we provide details on the painting algorithm. Each
point in the lidar point cloud is (x, y, z, r) or (x, y, z, r,               The decorated point clouds can be consumed by any li-
t) for KITTI and nuScenes respectively, where x, y, z are                 dar network that learns an encoder, since PointPainting just
the spatial location of each lidar point, r is the reflectance,           changes the input dimension of the lidar points. Point-
and t is the relative timestamp of the lidar point (applica-              Painting can also be utilized by lidar networks with hand-
                                         mAP                 Car                        Pedestrian                      Cyclist
           Method            Modality
                                         Mod.       Easy     Mod.     Hard      Easy      Mod.     Hard        Easy      Mod.      Hard
          MV3D[3]             L&I         N/A      86.62    78.93     69.80      N/A       N/A       N/A       N/A       N/A       N/A
       AVOD-FPN[10]           L&I        64.07     90.99    84.82     79.62     58.49     50.32     46.98     69.39     57.12     51.09
          IPOD[31]            L&I        64.60     89.64    84.62     79.96     60.88     49.79     45.43     78.19     59.40     51.38
       F-PointNet[18]         L&I        65.20     91.17    84.67     74.77     57.13     49.57     45.48     77.26     61.37     53.78
       F-ConvNet[26]          L&I        67.89     91.51    85.84     76.11     57.04     48.96     44.33     84.16     68.88     60.05
          MMF[13]            L, I & M     N/A      93.67    88.21     81.99      N/A       N/A       N/A       N/A       N/A       N/A
        LaserNet[17]             L        N/A      79.19.   74.52     68.45      N/A       N/A       N/A       N/A       N/A       N/A
        SECOND[29]               L       61.61     89.39    83.77     78.59     55.99     45.02     40.93      76.5     56.05     49.45
       PointPillars[11]          L       65.98     90.07    86.56     82.81     57.60     48.64     45.78     79.90     62.73     55.58
           STD[32]               L       68.38     94.74    89.19     86.42     60.02     48.72     44.55     81.36     67.23     59.35
       PointRCNN[21]             L       66.92     92.13    87.39     82.72     54.77     46.13     42.84     82.56     67.24     60.28
     Painted PointRCNN        L&I        69.86     92.45    88.11     83.36     58.70     49.93     46.29     83.91     71.54     62.97
            Delta               ∆I       +2.94     +0.32    +0.72     +0.64     +3.93     +3.80     +3.45     +1.35     +4.30     +2.69
Table 2. Results on the KITTI test BEV detection benchmark. We see that Painted PointRCNN sets a new state of the art (69.86 mAP) in
BEV detection performance. The modalities are lidar (L), images (I), and maps (M). The delta is the difference due to Painting, ie Painted
PointRCNN minus PointRCNN. The corresponding 3D results are included in Table 8 in the Supplementary Material.

engineered encoder [30, 22], but requires specialized fea-              tated with 3D bounding boxes for 1000 20-second scenes
ture engineering for each method. In this paper, we demon-              at 2Hz resulting in 28130 samples for training, 6019 sam-
strate that PointPainting works with three different lidar de-          ples for validation and 6008 samples for testing. nuScenes
tectors: PointPillars [11], VoxelNet [34, 29], and PointR-              comprises the full autonomous vehicle data suite: synced
CNN [21]. These are all state of the art lidar detectors with           lidar, cameras and radars with complete 360 coverage; in
distinct network architectures: single stage (PointPillars,             this work, we use the lidar point clouds and RGB images
VoxelNet) vs two stage (PointRCNN), and pillars (PointPil-              from all 6 cameras. The 3D object detection challenge eval-
lars) vs voxels (VoxelNet) vs point-wise features (PointR-              uates the performance on 10 classes: cars, trucks, buses,
CNN). Despite these different design choices, all lidar net-            trailers, construction vehicles, pedestrians, motorcycles, bi-
works benefit from PointPainting (Table 1). Note that we                cycles, traffic cones and barriers. Further, the dataset has
were as inclusive as possible in this selection, and to the             an imbalance challenge with cars and pedestrians most fre-
best of our knowledge, these represent all of the top KITTI             quent, and construction vehicles and bicycles least frequent.
detection leaderboard methods that have public code.
                                                                        3.2. Semantics Network Details
3. Experimental setup                                                      Here we provide more details on the semantics networks.
   In this section we present details of each dataset and the           KITTI. For experiments on KITTI [6], we used the
experimental settings of PointPainting.                                 DeepLabv3+ network1 . The network was first pretrained on
3.1. Datasets                                                           Mapillary [7], then finetuned on Cityscapes [5], and finally
                                                                        finetuned again on KITTI pixelwise sem. seg. [6]. Note that
   We evaluate our method on the KITTI and nuScenes                     the class definition of cyclist differs between KITTI sem.
datasets.                                                               seg. and object detection: in detection a cyclist is defined as
KITTI. The KITTI dataset [6] provides synced lidar point                rider + bike, while in sem. seg. a cyclist is defined as only
clouds and front-view camera images. It is relatively small             the rider with bike a separate class. There was therefore
with 7481 samples for training and 7518 samples for test-               a need to map bikes which had a rider to the cyclist class,
ing. For our test submission, we created a minival set of 784           while supressing parked bikes to background. We did this
samples from the training set and trained on the remaining              after painting by mapping all points painted with the bike
6733 samples. The KITTI object detection benchmark re-                  class within a 1m radius of a rider to the cyclist class; the
quires detection of cars, pedestrians, and cyclists. Ground             rest to background.
truth objects were only annotated if they are visible in the            nuScenes. There was no public semantic segmentation
image, so we follow the standard practice [3, 34] of only               method available on nuScenes so we trained a custom net-
using lidar points that project into the image.                         work using the nuImages dataset.2 nuImages consists of
nuScenes. The nuScenes dataset [1] is larger than the                      1 https://github.com/NVIDIA/semantic-segmentation

KITTI dataset (7x annotations, 100x images). It it anno-                   2 We used an early access version; https://www.nuscenes.org/images.
        Methods             mAP        Car     Truck   Bus    Trailer   Ctr. Vhl.    Ped.   Motorcycle   Bicycle   Tr. Cone   Barrier
   PointPillars [11, 1]      30.5     68.4      23.0   28.2    23.4        4.1       59.7      27.4        1.1       30.8      38.9
      PointPillars+          40.1     76.0      31.0   32.1    36.6       11.3       64.0      34.2       14.0       45.6      56.4
  Painted PointPillars+      46.4     77.9      35.8   36.1    37.3       15.8       73.3      41.5       24.1      62.4       60.2
          Delta              +6.3     +1.9      +4.8   +3.9    +0.7       +4.5       +9.3      +7.3      +10.1      +16.8      +3.8
Table 3. Per class nuScenes performance. Evaluation of detections as measured by average precision (AP) or mean AP (mAP) on nuScenes
test set. Abbreviations: construction vehicle (Ctr. Vhl.), pedestrian (Ped.), and traffic cone (Tr. Cone).

100k images annotated with 2D bounding boxes and seg-                    each class, the predicted velocities and heights of each box
mentation labels for all nuScenes classes. The segmentation              are used to better estimate each attribute. Fourth, to reduce
network uses a ResNet [9] backbone to generate features at               the class imbalance during training, a sample based weight-
strides 8 to 64 for a FCN [15] segmentation head that pre-               ing method was used where each sample was weighted ac-
dicts the nuScenes segmentation scores.                                  cording to the number of annotations in the sample. Fifth,
                                                                         the global yaw augmentation was changed from π to π/6.
3.3. Lidar Network Details
   We perform experiments using three different lidar net-               4. Results
works: PointPillars [11], VoxelNet [34, 29], and PointR-
CNN [21]. The fusion versions of each network that use                     In this section, we present PointPainting results on the
PointPainting will be referred to as being painted (e.g.                 KITTI and nuScenes datasets and compare to the literature.
Painted PointPillars).
                                                                         4.1. Quantitative Analysis
KITTI. We used the publicly released code for PointPil-                  4.1.1      KITTI
lars3 , VoxelNet4 and PointRCNN5 and decorate the point
cloud with the sem. seg. scores for 4 classes. This                      All detection results are measured using the official KITTI
changes the original decorated point cloud dimensions from               evaluation detection for bird’s-eye view (BEV) and 3D. The
9 → 13, 7 → 11, and 4 → 8 for PointPillars, Vox-                         BEV results are presented here while the 3D results are in-
elNet, and PointRCNN respectively. For PointPillars, the                 cluded in the Supplementary Material. The KITTI dataset
new encoder has (13, 64) channels, while for VoxelNet it                 is stratified into easy, moderate, and hard difficulties, and
has (11, 32), (64, 128) channels. The 8 dimensional painted              the official KITTI leaderboard is ranked by performance on
point cloud for PointRCNN is given as input to both the en-              moderate average precision (AP).
coder and the region pooling layer. No other changes were
made to the public experimental configurations.                          Validation Set First, we investigate the effect of Point-
                                                                         Painting on three leading lidar detectors. Fig. 1 and Ta-
nuScenes. We use PointPillars for all nuScenes experi-                   ble 1 demonstrate that PointPainting improves the detec-
ments. This requires changing the decorated point cloud                  tion performance for PointPillars [11], VoxelNet [34, 29],
from 7 → 18, and the encoder has (18, 64) channels now.                  and PointRCNN [21]. The PointPainting semantic informa-
    In order to make sure the effect of painting is measured             tion led to a widespread improvement in detection: 24 of 27
on a state of the art method, we made several improvem-                  comparisons (3 experiments × 3 classes × 3 strata) were
nts to the previously published PointPillars setup [1] boost-            improved by PointPainting. While the greatest changes
ing the mAP by 10% on the nuScenes bechmark (Table 4).                   were for the more challenging scenarios of pedestrian and
We refer to this improved baseline as PointPillars+. The                 cyclist detection, most networks even saw an improvement
changes are inspired by [35] and comprise modifying pillar               on cars. This demonstrates that the utility of PointPainting
resolution, network architecture, attribute estimation, sam-             is independent of the underlying lidar network.
ple weighting, and data augmentation. First, the pillar reso-
lution was reduced from 0.25 m to 0.2 m to allow for better              Test Set Here we compare PointPainting with state of the
localization of small objects. Second, the network archi-                art KITTI test results. The KITTI leaderboard only al-
tecture was changed to include more layers earlier in the                lows one submission per paper, so we could not submit all
network. Third, neither PointPillars nor PointPillars+ pre-              Painted methods from Table 1. While Painted PointPillars
dict attributes, instead the attribute estimation heuristic was          performed better than Painted PointRCNN on the val set,
improved. Rather than using the most common attribute for                of the two only PointPillars has public code for nuScenes.
  3 https://github.com/nutonomy/second.pytorch                           Therefore, to establish the generality of PointPainting, we
  4 https://github.com/traveller59/second.pytorch                        chose to submit Painted PointPillars results to nuScenes
  5 https://github.com/sshaoshuai/PointRCNN                              test, and use our KITTI submission on Painted PointRCNN.
                                                                                        60

                                                                  BEV Detection (mAP)
          Method              Modality       NDS     mAP
      MonoDis [23]             Images        38.4    30.4
    PointPillars [11, 1]        Lidar        45.3    30.5                               50
       PointPillars+            Lidar        55.0    40.1                               40
   Painted PointPillars+   Lidar & Images    58.1    46.4
      MEGVII [35]               Lidar        63.3    52.8                               30
Table 4. nuScenes test results. Detection performance is mea-
                                                                                        20
sured by nuScenes detection score (NDS) [1] and mean average                                 0    20    40      60       ... Oracle
precision (mAP).
                                                                                                 Segmentation Quality (mIOU)
                                                                        Figure 5. PointPainting dependency on segmentation quality. The
                                                                        Painted PointPillars detection performance, as measured by mean
   As shown in Table 2, PointPainting leads to a robust                 average precision (mAP) on the val split, is compared with respect
improvement on the test set for PointRCNN: the average                  to the quality of semantic segmentation network used in the paint-
precision increases for every single class across all strata.           ing step, as measured by mean intersection over union (mIoU).
Painted PointRCNN establishes new state of the art perfor-              The oracle uses the 3D bounding boxes as semantic segmentation.
mance on mAP and cyclist AP.
   Based on the consistency of Painted PointRCNN im-
provements between val and test (+2.73 and +2.94 respec-                classes well detected by lidar only.
tively), and the generality of PointPainting (Table 1), it is           4.3. Qualitative Analysis
reasonable to believe that other methods in Table 2 would
decidedly improve with PointPainting. The strength, gen-                    Here we give context to the evaluation metrics with some
erality, robustness, and flexibility of PointPainting suggests          qualitative comparisons in Fig. 4 using Painted PointPillars,
that it is the leading method for image-lidar fusion.                   the best performing network on KITTI val set. In Fig. 4 A,
                                                                        original PointPillars correctly detects the cars, but misses a
4.2. nuScenes                                                           cyclist. The painted point cloud resolves this and the cy-
                                                                        clist is detected. It also yields better orientation estimates
    To establish the versatility of PointPainting, we exam-
                                                                        for the vehicles. A common failure mode of lidar based
ine Painted PointPillars results on nuScenes. As a first step,
                                                                        methods is confusion between pedestrians and poles (Fig.
we strengthened the lidar network baseline to PointPillars+.
                                                                        3). As expected, PointPainting can help resolve this (Fig. 4
Even with this stronger baseline, PointPainting increases
                                                                        B). Fig. 4 C suggests that the lidar detection step can cor-
mean average precision (mAP) by +6.3 on the test set (Ta-
                                                                        rect incorrect painting. The loose segmentation masks in
ble 4). Painted PointPillars+ is only beat by MEGVII’s li-
                                                                        the image correctly paint nearby pedestrians, but extra paint
dar only method on nuScenes. However, MEGVII’s net-
                                                                        also gets splattered onto the wall behind them. Despite this
work [35] is impractical for a realtime system since it is an
                                                                        incorrect semantic information, the network does not pre-
extremely large two stage network that requires high reso-
                                                                        dict false positive pedestrians. This leaves unanswered the
lution inputs and uses multi-scale inputs and ensembles for
                                                                        precise characteristics of sem. seg. (e.g. precision vs recall)
test evaluation. Therefore, Painted PointPillars+ is the lead-
                                                                        to optimize for PointPainting. In Fig. 4 D, Painted PointPil-
ing realtime method on nuScenes.
                                                                        lars predicts two false positive cyclists on the left because
    The detection performance generalized well across
                                                                        of two compounding mistakes. First, the sem. seg. net-
classes with every class receiving a boost in AP from Point-
                                                                        work incorrectly predicts pedestrians as riders as they are
Painting (Table 3). In general, the worst performing detec-
                                                                        so close to the parked bikes. Next, the heuristic that we
tion classes in PointPillars+ benefited the most from paint-
                                                                        used to resolve the discrepancy in the cyclist definition be-
ing, but there were exceptions. First, traffic cones received
                                                                        tween detection and segmentation annotations (See Section
the largest increase in AP (+16.8) despite already having
                                                                        3.2) exacerbated the problem by painting all bikes with the
robust PointPillars+ detections. This is likely because traffic
                                                                        cyclist class. However, throughout the rest of the crowded
cones often have very few lidar points on them, so the addi-
                                                                        scene, the painted points lead to better oriented pedestrians,
tional information provided by semantic segmentation is ex-
                                                                        fewer false positives, and better detections of far away cars.
tremely valuable. Second, trailer and construction vehicles
had lower detection gains, despite starting from a smaller              5. Ablation Studies
baseline. This was a consequence of the segmentation net-
work having its worst recall on these classes (overall recall              Here we perform ablation studies on the nuScenes
of 72%, but only 39% on trailers and 40% on construction                dataset. All studies used the Painted PointPillars architec-
vehicles; see Supplementary Material for details). Finally,             ture and were trained for a quarter of the training time as
despite a baseline of 76 AP, cars still received a +1.9 AP              compared to the test submissions. Using the one-cycle op-
boost, signaling the value of semantic information even for             timizer [24], we achieved 33.9 mAP and 46.3 NDS on the
  Concurrent Matching                Consecutive Matching                        Method            Matching     NDS     mAP
                                                                           Painted PointPillars   Concurrent    46.3    33.9
Images                  Time        Images                 Time            Painted PointPillars   Consecutive   46.4    33.9
                                                                     Table 5. Time delay analysis. Painted PointPillars results on
  Point                              Point                           nuScenes when using concurrent matching (which incurs latency),
 Clouds                             Clouds                           or consecutive matching (which allows real-time pipelining) as
Figure 6. Reducing latency by pipelining. A Painted lidar network    shown in Figure 6. The use of the previous image minimizes la-
requires both point clouds and images. Using the most recent im-     tency without any drop in detection performance.
age (Concurrent Matching) adds latency since the lidar network
must wait for the image segmentation results. This latency can be
minimized using pipelining if the Painted network uses the seg-
                                                                     a larger PointPillars encoder would perform better.
mentation mask of previous images (Consecutive Matching). Us-            Comparing these results with the segmentation quality
ing consecutive matching, we found that Painted PointPillars only    ablation suggests that future research focus more on im-
adds a latency of 0.75 ms over the original PointPillars architec-   proving segmentation quality and less on representation.
ture. See Supplementary Material for further details.
                                                                     5.2. Sensitivity to Timing
                                                                        We investigate the sensitivity of the lidar network to
nuScenes val set as opposed to 44.85 mAP and 57.34 NDS               delays in semantic information. In the simplest scenario,
for full training of Painted PointPillars+.                          which we used in all previous results, each point cloud is
5.1. Dependency on Semantics                                         matched to the most recent image (Concurrent Matching
Quality. In PointPainting, the lidar points are fused with           - Fig. 6). However, this will introduce a latency in a real
the semantic segmentation of the image. We investigate the           time system as the fusion step will have to wait for the im-
impact of the semantic segmentation quality on the final de-         age based sem. seg. scores. To eliminate the latency, the
tection performance. Using nuScenes, we generate a series            sem. seg. scores of the previous image can be pipelined
of sem. seg. networks with varying segmentation quality by           into the lidar network (Consecutive Matching - Fig. 6). This
using multiple intermediate checkpoints from training. As            involves an ego-motion compensation step where the lidar
shown in Fig. 5, improved sem. seg. (as measured by mean             pointcloud is first transformed to the coordinate system of
IOU), leads to improved 3D object detection.                         the ego-vehicle in the last frame followed by a projection
    For an upper bound, we include an “oracle” which uses            into the image to get the segmentation scores. Our experi-
the ground truth 3D boxes to paint the lidar points. This sig-       ments suggest that using the previous images does not de-
nificantly improves the detection performance (+27 mAP),             grade detection performance (Table 5). Further, we measure
which demonstrates that advances in semantic segmentation            that PointPainting only introduces an additional latency of
would radically boost 3D object detection.                           0.75 ms for the Painted PointPillars architecture (see Sup-
    Using the oracle doesn’t guarantee a perfect mAP be-             plementary Material for details). This demonstrates that
cause of several limitations. First, the ground truth bound-         PointPainting can achieve high detection performance in a
ing box can contain irrelevant points (e.g. from the ground).        realtime system with minimal added latency.
Second, nuScenes annotates all objects that contain a single
lidar point. Turning one lidar point into an accurate, ori-          6. Conclusion
ented 3D bounding box is difficult. Third, we trained it for             In this paper, we present PointPainting, a novel sequen-
the same total time as the other ablation studies, but it would      tial fusion method that paints lidar point clouds with image
probably benefit from longer training. Finally, PointPillars’        based semantics. PointPainting produces state of the art re-
stochastic sampling of the point cloud could significantly           sults on the KITTI and nuScenes challenges with multiple
filter, or eliminate, the points that contain semantic infor-        different lidar networks. The PointPainting framework is
mation if the ground truth object contains only a few points.        flexible and can combine the outputs of any segmentation
                                                                     network with any lidar network. The strength of these re-
Scores vs Labels. We investigate the effect of the seg-
                                                                     sults and the general applicability demonstrate that Point-
mentation prediction format on detection performance. To
                                                                     Painting is the leading architecture when fusing image and
do so we convert the segmentation scores to a one hot en-
                                                                     lidar information for 3D object detection.
coding, effectively labelling each pixel as the class with the
highest score. When using the labels instead of scores, the
                                                                     7. Acknowledgements
NDS was unchanged and the mAP was, surprisingly, +0.4
higher. However, the gains are marginal and within the                  We thank Donghyeon Won, Varun Bankiti and Venice
noise of training. We also hypothesize that for future stud-         Liong for help with the semantic segmentation model for
ies, a combination of calibrated [8] segmentation scores and         nuScenes, and Holger Caesar for access to nuImages.
References                                                           [19] F. A. Reda, G. Liu, K. J. Shih, R. Kirby, J. Barker, D. Tarjan,
                                                                          A. Tao, and B. Catanzaro. Sdc-net: Video prediction using
 [1] H. Caesar, V. Bankiti, A. H. Lang, S. Vora, V. E. Liong,             spatially-displaced convolution. In Proceedings of the Euro-
     Q. Xu, A. Krishnan, Y. Pan, G. Baldan, and O. Beijbom.               pean Conference on Computer Vision (ECCV), pages 718–
     nuscenes: A multimodal dataset for autonomous driving. In            733, 2018. 4
     CVPR, 2020. 1, 3, 4, 5, 6, 7
                                                                     [20] T. Roddick, A. Kendall, and R. Cipolla. Orthographic fea-
 [2] L.-C. Chen, Y. Zhu, G. Papandreou, F. Schroff, and H. Adam.          ture transform for monocular 3d object detection. In BMVC,
     Encoder-decoder with atrous separable convolution for se-            2019. 2
     mantic image segmentation. In Proceedings of the Euro-
                                                                     [21] S. Shi, X. Wang, and H. Li. Pointrcnn: 3d object proposal
     pean conference on computer vision (ECCV), pages 801–
                                                                          generation and detection from point cloud. In CVPR, 2019.
     818, 2018. 4
                                                                          1, 2, 3, 5, 6, 11
 [3] X. Chen, H. Ma, J. Wan, B. Li, and T. Xia. Multi-view 3d
                                                                     [22] M. Simon, S. Milz, K. Amende, and H.-M. Gross. Complex-
     object detection network for autonomous driving. In CVPR,
                                                                          yolo: Real-time 3d object detection on point clouds. CoRR,
     2017. 1, 2, 5, 11
                                                                          abs/1803.06199, 2018. 3, 5
 [4] B. Cheng, M. D. Collins, Y. Zhu, T. Liu, T. S. Huang,
                                                                     [23] A. Simonelli, S. Rota Bulo, L. Porzi, M. Lopez-Antequera,
     H. Adam, and L.-C. Chen. Panoptic-deeplab. ICCV Work-
                                                                          and P. Kontschieder. Disentangling monocular 3d object de-
     shop, 2019. 3
                                                                          tection. ICCV, 2019. 7
 [5] M. Cordts, M. Omran, S. Ramos, T. Rehfeld, M. Enzweiler,
                                                                     [24] L. N. Smith. A disciplined approach to neural network
     R. Benenson, U. Franke, S. Roth, and B. Schiele. The
                                                                          hyper-parameters: Part 1 – learning rate, batch size, momen-
     Cityscapes dataset for semantic urban scene understanding.
                                                                          tum, and weight decay. arXiv preprint arXiv:1803.09820,
     In CVPR, 2016. 5
                                                                          2018. 7
 [6] A. Geiger, P. Lenz, and R. Urtasun. Are we ready for au-
                                                                     [25] Y. Wang, W.-L. Chao, D. Garg, B. Hariharan, M. Camp-
     tonomous driving? the KITTI vision benchmark suite. In
                                                                          bell, and K. Q. Weinberger. Pseudo-lidar from visual depth
     CVPR, 2012. 1, 5
                                                                          estimation: Bridging the gap in 3d object detection for au-
 [7] N. Gerhard, T. Ollmann, S. R. Bulo, and P. Kontschieder.             tonomous driving. In CVPR, 2019. 2
     The Mapillary Vistas dataset for semantic understanding of
                                                                     [26] Z. Wang and K. Jia. Frustum convnet: Sliding frustums to
     street scenes. In ICCV, 2017. 5
                                                                          aggregate local point-wise features for amodal 3d object de-
 [8] C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger. On calibra-         tection. IROS, 2019. 2, 5, 11
     tion of modern neural networks. In ICML, 2017. 8
                                                                     [27] Z. Wang, W. Zhan, and M. Tomizuka. Fusing bird’s eye view
 [9] K. He, X. Zhang, S. Ren, and J. Sun. Deep residual learning          lidar point cloud and front view camera image for 3d object
     for image recognition. In CVPR, 2016. 6                              detection. In IVS, 2018. 1, 2
[10] J. Ku, M. Mozifian, J. Lee, A. Harakeh, and S. Waslander.       [28] X. Weng and K. Kitani. Monocular 3d object detection with
     Joint 3d proposal generation and object detection from view          pseudo-lidar point cloud. ICCV Workshop, 2019. 2
     aggregation. In IROS, 2018. 1, 2, 5, 11
                                                                     [29] Y. Yan, Y. Mao, and B. Li. SECOND: Sparsely embedded
[11] A. H. Lang, S. Vora, H. Caesar, L. Zhou, J. Yang, and O. Bei-        convolutional detection. Sensors, 18(10), 2018. 1, 2, 3, 5, 6,
     jbom. Pointpillars: Fast encoders for object detection from          11
     point clouds. In CVPR, 2019. 1, 2, 3, 5, 6, 7, 11
                                                                     [30] B. Yang, W. Luo, and R. Urtasun. PIXOR: Real-time 3d
[12] B. Li, T. Zhang, and T. Xia. Vehicle detection from 3d lidar         object detection from point clouds. In CVPR, 2018. 2, 3, 5
     using fully convolutional network. In RSS, 2016. 2
                                                                     [31] Z. Yang, Y. Sun, S. Liu, X. Shen, and J. Jia. Ipod: Intensive
[13] M. Liang, B. Yang, Y. Chen, R. Hu, and R. Urtasun. Multi-            point-based object detector for point cloud. arXiv preprint
     task multi-sensor fusion for 3d object detection. In CVPR,           arXiv:1812.05276, 2018. 2, 5, 11
     2019. 1, 2, 5, 11
                                                                     [32] Z. Yang, Y. Sun, S. Liu, X. Shen, and J. Jia. Std: Sparse-
[14] M. Liang, B. Yang, S. Wang, and R. Urtasun. Deep contin-             to-dense 3d object detector for point cloud. In CVPR, pages
     uous fusion for multi-sensor 3d object detection. In ECCV,           1951–1960, 2019. 1, 2, 5, 11
     2018. 2
                                                                     [33] Y. You, Y. Wang, W.-L. Chao, D. Garg, G. Pleiss, B. Hari-
[15] J. Long, E. Shelhamer, and T. Darrell. Fully convolutional           haran, M. Campbell, and K. Q. Weinberger. Pseudo-lidar++:
     networks for semantic segmentation. In CVPR, 2015. 6                 Accurate depth for 3d object detection in autonomous driv-
[16] G. P. Meyer, J. Charland, D. Hegde, A. Laddha, and                   ing. ICLR, 2020. 1, 2
     C. Vallespi-Gonzalez. Sensor fusion for joint 3d object de-     [34] Y. Zhou and O. Tuzel. Voxelnet: End-to-end learning for
     tection and semantic segmentation. In CVPR Workshop,                 point cloud based 3d object detection. In CVPR, 2018. 1, 2,
     2019. 2                                                              3, 5, 6, 11
[17] G. P. Meyer, A. Laddha, E. Kee, C. Vallespi-Gonzalez, and       [35] B. Zhu, Z. Jiang, X. Zhou, Z. Li, and G. Yu. Class-balanced
     C. K. Wellington. Lasernet: An efficient probabilistic 3d            grouping and sampling for point cloud 3d object detection.
     object detector for autonomous driving. In CVPR, 2019. 2,            arXiv preprint arXiv:1908.09492, 2019. 6, 7
     5, 11
                                                                     [36] Y. Zhu, K. Sapra, F. A. Reda, K. J. Shih, S. Newsam, A. Tao,
[18] C. R. Qi, W. Liu, C. Wu, H. Su, and L. J. Guibas. Frus-              and B. Catanzaro. Improving semantic segmentation via
     tum pointnets for 3d object detection from RGB-D data. In            video propagation and label relaxation. In CVPR, 2019. 3, 4
     CVPR, 2018. 1, 2, 5, 11
                     PointPainting: Sequential Fusion for 3D Object Detection

                                               Supplementary Material

A. PointPainting: 3D results                                            Class              Recall (%)      Precision (%)
   In this section, we present 3D results of PointPainting on            Car                  94                 89
the KITTI validation and test sets.                                      Bus                  71                 92
                                                                 Construction Vehicle         40                 58
                                                                       Trailer                39                 79
Validation Set Similar to bird’s-eye view results (Table
                                                                        Truck                 69                 76
1), we see that PointPainting substantially improves 3D de-
                                                                     Motorcycle               89                 87
tection performance on the validation set. As seen in Table
                                                                       Bicycle                58                 84
7, 23 out of 27 comparisons (3 experiments x 3 classes x 3
strata) were improved by PointPainting.                              Pedestrian               80                 86
                                                                       Barrier                81                 80
                                                                    Traffic Cone              78                 84
Test Set In the test set (Table 8), we observe that Point-
                                                                Table 6. Class-wise Precision and Recall of the semantic segmen-
Painting consistently improves 3D detection results of
                                                                tation network trained on the nuImages dataset.
PointRCNN on the pedestrians and cyclists classes across
all difficulty strata (easy, medium and hard). However, we
see that the 3D results on the car class drops substantially.   C. nuImages Semantic Segmentation
We think this could be because of overfitting on our minival
set which was very small (see Section 3.1).                        Here we present some stats on the semantic segmentation
                                                                network that we trained on the nuImages dataset. The mean
                                                                intersection over union (mIoU) on the validation set was
B. PointPainting Latency                                        0.65. The class-wise precision and recall on the validation
   In Section 5.2, we concluded that Consecutive match-         set is shown in Table 6. Our model performs the best on the
ing (see Figure 6) can minimize the latency introduced by       car class and worst on the construction vehicle and trailer
PointPainting without any drop in detection performance.        classes.
Here we provide a detailed breakdown of the latency intro-
duced by PointPainting in the case of Consecutive match-
ing.

Projection This step involves transforming the point-
cloud to the coordinate system of the ego-vehicle in the pre-
vious frame followed by a projection into the camera im-
ages to get the segmentation scores. This operation only
adds a latency of 0.15 ms.

Encoding The Painted PointPillars encoder operates on
an 18 dimensional decorated pointcloud as opposed to the
7 dimensional pointcloud in the original PointPillars archi-
tecture. We measure the runtimes for both the encoders in
TensorRT and find that PointPainting adds an additional
latency of 0.6 ms in the encoding stage.

Thus, Painted PointPillars only introduces an additional
latency of 0.75 ms over PointPillars when Consecutive
matching is used. This makes Painted PointPillars a strong
candidate for realtime camera-lidar fusion.
                                   mAP                 Car                          Pedestrian                       Cyclist
                  Method
                                   Mod.       Easy     Mod.      Hard       Easy      Mod.     Hard        Easy       Mod.      Hard
             PointPillars [11]     66.96     87.22     76.95     73.52      65.37     60.66     56.51      82.29     63.26     59.82
            Painted PointPillars   69.03     86.26     76.77     70.25      71.50     66.15     61.03      79.12     64.18     60.79
                   Delta           +2.07     -0.96     -0.18     -3.27      +6.13     +5.49     +4.52      -3.17     +0.92     +0.97
             VoxelNet [34, 29]     67.12     86.85     76.64     74.41      67.79     59.84     52.38      84.92     64.89     58.59
             Painted VoxelNet      68.01     87.15     76.66     74.75      68.57     60.93     54.01      85.61     66.44     64.15
                   Delta           +0.89     +0.3      +0.02     +0.34      +0.78     +1.09     +1.63      +0.69     +1.55     +5.56
            PointRCNN [21]         67.01     86.75     76.05     74.30      63.29     58.32     51.59      83.68     66.67     61.92
           Painted PointRCNN       70.34     88.38     77.74     76.76      69.38     61.67     54.58      85.21     71.62     66.98
                  Delta            +3.33     +1.63     +1.69     +2.46      +6.09     +3.35     +2.29      +1.53     +4.95     +5.06
Table 7. PointPainting applied to state of the art lidar based object detectors. All lidar methods show an improvement in 3D mean average
precision (mAP) of car, pedestrian, and cyclist on KITTI validation set, moderate split.

                                           mAP                 Car                          Pedestrian                     Cyclist
            Method           Modality
                                           Mod.      Easy      Mod.      Hard       Easy      Mod.     Hard        Easy     Mod.       Hard
           MV3D[3]            L&I           N/A      74.97     63.63     54.00       N/A       N/A       N/A        N/A       N/A       N/A
        AVOD-FPN[10]          L&I          54.86     83.07     71.76     65.73      50.46     42.27     39.04      63.76     50.55     44.93
        F-PointNet[18]        L&I          56.02     82.19     69.79     60.59      50.53     42.15     38.08      72.27     56.12     49.01
        F-ConvNet[26]         L&I          61.61     87.36     76.39     66.69      52.16     43.38     38.80      81.98     65.07     56.54
           MMF[13]           L, I & M       N/A      88.40     77.43     70.22       N/A       N/A       N/A        N/A       N/A       N/A
        PointPillars[11]         L         58.29     82.58     74.31     68.99      51.45     41.92     38.89      77.10     58.65     51.92
            STD[32]              L         61.25     87.95     79.71     75.09      53.29     42.47     38.35      78.69     61.59     55.30
        PointRCNN[21]            L         57.94     86.96     75.64     70.70      47.98     39.37     36.01      74.96     58.82     52.53
      Painted PointRCNN       L&I          58.82     82.11     71.70     67.08      50.32     40.97     37.87      77.63     63.78     55.89
             Delta              ∆I         +0.88     -4.85     -3.94     -3.62      +2.34     +1.6      +1.86      +2.67     +4.96     +3.36
Table 8. Results on the KITTI test 3D detection benchmark. The modalities are lidar (L), images (I), and maps (M). The delta is the
difference due to Painting, ie Painted PointRCNN minus PointRCNN. We don’t include a few entries from Table 2 because LaserNet[17]
did not publish 3D results and SECOND[29], IPOD[31] no longer have their entries on the public leaderboard since KITTI changed to a
40 point interpolated AP metric instead of 11.
