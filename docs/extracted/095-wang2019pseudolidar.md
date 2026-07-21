---
source_id: 095
bibtex_key: wang2019pseudolidar
title: Pseudo-LiDAR from Visual Depth Estimation: Bridging the Gap in 3D Object Detection for Autonomous Driving
year: 2019
domain_theme: Deteksi 3D
verified_pdf: 95_Pseudo-LiDAR.pdf
char_count: 76879
---

Pseudo-LiDAR from Visual Depth Estimation:
                                                     Bridging the Gap in 3D Object Detection for Autonomous Driving

                                          Yan Wang, Wei-Lun Chao, Divyansh Garg, Bharath Hariharan, Mark Campbell, and Kilian Q. Weinberger
                                                                           Cornell University, Ithaca, NY
                                                                        {yw763, wc635, dg595, bh497, mc288, kqw4}@cornell.edu
arXiv:1812.07179v6 [cs.CV] 22 Feb 2020

                                                                                                                          Input                  Pseudo-LiDAR (Bird’s-eye)
                                                                  Abstract                                                                       View)

                                             3D object detection is an essential task in autonomous
                                         driving. Recent techniques excel with highly accurate de-                      Depth Map

                                         tection rates, provided the 3D input data is obtained from
                                         precise but expensive LiDAR technology. Approaches based
                                         on cheaper monocular or stereo imagery data have, un-
                                         til now, resulted in drastically lower accuracies — a gap            Figure 1: Pseudo-LiDAR signal from visual depth esti-
                                         that is commonly attributed to poor image-based depth es-            mation. Top-left: a KITTI street scene with super-imposed
                                         timation. However, in this paper we argue that it is not             bounding boxes around cars obtained with LiDAR (red) and
                                         the quality of the data but its representation that accounts         pseudo-LiDAR (green). Bottom-left: estimated disparity
                                         for the majority of the difference. Taking the inner work-           map. Right: pseudo-LiDAR (blue) vs. LiDAR (yellow) —
                                         ings of convolutional neural networks into consideration,            the pseudo-LiDAR points align remarkably well with the
                                         we propose to convert image-based depth maps to pseudo-              LiDAR ones. Best viewed in color (zoom in for details.)
                                         LiDAR representations — essentially mimicking the LiDAR
                                         signal. With this representation we can apply different ex-
                                         isting LiDAR-based detection algorithms. On the popular
                                         KITTI benchmark, our approach achieves impressive im-                a single sensor is an inherent safety risk and it would be
                                         provements over the existing state-of-the-art in image-based         advantageous to have a secondary sensor to fall-back onto
                                         performance — raising the detection accuracy of objects              in case of an outage. A natural candidate are images from
                                         within the 30m range from the previous state-of-the-art of           stereo or monocular cameras. Optical cameras are highly
                                         22% to an unprecedented 74%. At the time of submis-                  affordable (several orders of magnitude cheaper than Li-
                                         sion our algorithm holds the highest entry on the KITTI              DAR), operate at a high frame rate, and provide a dense
                                         3D object detection leaderboard for stereo-image-based               depth map rather than the 64 or 128 sparse rotating laser
                                         approaches. Our code is publicly available at https:                 beams that LiDAR signal is inherently limited to.
                                         //github.com/mileyan/pseudo_lidar.                                       Several recent publications have explored the use of
                                                                                                              monocular and stereo depth (disparity) estimation [13, 21,
                                                                                                              35] for 3D object detection [5, 6, 24, 33]. However, to-date
                                                                                                              the main successes have been primarily in supplementing
                                         1. Introduction
                                                                                                              LiDAR approaches. For example, one of the leading algo-
                                            Reliable and robust 3D object detection is one of the fun-        rithms [18] on the KITTI benchmark [11, 12] uses sensor
                                         damental requirements for autonomous driving. After all, in          fusion to improve the 3D average precision (AP) for cars
                                         order to avoid collisions with pedestrians, cyclist, and cars,       from 66% for LiDAR to 73% with LiDAR and monocular
                                         a vehicle must be able to detect them in the first place.            images. In contrast, among algorithms that use only images,
                                            Existing algorithms largely rely on LiDAR (Light Detec-           the state-of-the-art achieves a mere 10% AP [33].
                                         tion And Ranging), which provide accurate 3D point clouds                One intuitive and popular explanation for such inferior
                                         of the surrounding environment. Although highly precise,             performance is the poor precision of image-based depth es-
                                         alternatives to LiDAR are desirable for multiple reasons.            timation. In contrast to LiDAR, the error of stereo depth es-
                                         First, LiDAR is expensive, which incurs a hefty premium              timation grows quadratically with depth. However, a visual
                                         for autonomous driving hardware. Second, over-reliance on            comparison of the 3D point clouds generated by LiDAR and

                                                                                                          1
a state-of-the-art stereo depth estimator [3] reveals a high       in self-driving cars — potentially yielding substantial cost
quality match (cf. Fig. 1) between the two data modalities         reductions and/or safety improvements.
— even for faraway objects.
    In this paper we provide an alternative explanation with       2. Related Work
significant performance implications. We posit that the
major cause for the performance gap between stereo and             LiDAR-based 3D object detection. Our work is inspired
LiDAR is not a discrepancy in depth accuracy, but a                by the recent progress in 3D vision and LiDAR-based 3D
poor choice of representations of the 3D information for           object detection. Many recent techniques use the fact that
ConvNet-based 3D object detection systems operating on             LiDAR is naturally represented as 3D point clouds. For
stereo. Specifically, the LiDAR signal is commonly rep-            example, frustum PointNet [25] applies PointNet [26] to
resented as 3D point clouds [25] or viewed from the top-           each frustum proposal from a 2D object detection network.
down “bird’s-eye view” perspective [36], and processed ac-         MV3D [7] projects LiDAR points into both bird-eye view
cordingly. In both cases, the object shapes and sizes are in-      (BEV) and frontal view to obtain multi-view features. Vox-
variant to depth. In contrast, image-based depth is densely        elNet [37] encodes 3D points into voxels and extracts fea-
estimated for each pixel and often represented as additional       tures by 3D convolutions. UberATG-ContFuse [18], one of
image channels [6, 24, 33], making far-away objects smaller        the leading algorithms on the KITTI benchmark [12], per-
and harder to detect. Even worse, pixel neighborhoods in           forms continuous convolutions [30] to fuse visual and BEV
this representation group together points from far-away re-        LiDAR features. All these algorithms assume that the pre-
gions of 3D space. This makes it hard for convolutional            cise 3D point coordinates are given. The main challenge
networks relying on 2D convolutions on these channels to           there is thus on predicting point labels or drawing bounding
reason about and precisely localize objects in 3D.                 boxes in 3D to locate objects.
    To evaluate our claim, we introduce a two-step approach
for stereo-based 3D object detection. We first convert the
                                                                   Stereo- and monocular-based depth estimation. A key
estimated depth map from stereo or monocular imagery into
                                                                   ingredient for image-based 3D object detection methods is a
a 3D point cloud, which we refer to as pseudo-LiDAR as it
                                                                   reliable depth estimation approach to replace LiDAR. These
mimics the LiDAR signal. We then take advantage of ex-
                                                                   can be obtained through monocular [10, 13] or stereo vi-
isting LiDAR-based 3D object detection pipelines [17, 25],
                                                                   sion [3, 21]. The accuracy of these systems has increased
which we train directly on the pseudo-LiDAR representa-
                                                                   dramatically since early work on monocular depth estima-
tion. By changing the 3D depth representation to pseudo-
                                                                   tion [8, 16, 29]. Recent algorithms like DORN [10] com-
LiDAR we obtain an unprecedented increase in accuracy
                                                                   bine multi-scale features with ordinal regression to predict
of image-based 3D object detection algorithms. Specifi-
                                                                   pixel depth with remarkably low errors. For stereo vision,
cally, on the KITTI benchmark with IoU (intersection-over-
                                                                   PSMNet [3] applies Siamese networks for disparity estima-
union) at 0.7 for “moderately hard” car instances — the
                                                                   tion, followed by 3D convolutions for refinement, resulting
metric used in the official leaderboard — we achieve a
                                                                   in an outlier rate less than 2%. Recent work has made these
45.3% 3D AP on the validation set: almost a 350% im-
                                                                   methods mode efficient [31], enabling accurate disparity es-
provement over the previous state-of-the-art image-based
                                                                   timation to run at 30 FPS on mobile devices.
approach. Furthermore, we halve the gap between stereo-
based and LiDAR-based systems.
    We evaluate multiple combinations of stereo depth es-          Image-based 3D object detection. The rapid progress on
timation and 3D object detection algorithms and arrive at          stereo and monocular depth estimation suggests that they
remarkably consistent results. This suggests that the gains        could be used as a substitute for LiDAR in image-based
we observe are because of the pseudo-LiDAR representation          3D object detection algorithms. Existing algorithms of this
and are less dependent on innovations in 3D object detec-          flavor are largely built upon 2D object detection [28], im-
tion architectures or depth estimation techniques.                 posing extra geometric constraints [2, 4, 23, 32] to create
    In sum, the contributions of the paper are two-fold. First,    3D proposals. [5, 6, 24, 33] apply stereo-based depth es-
we show empirically that a major cause for the performance         timation to obtain the true 3D coordinates of each pixel.
gap between stereo-based and LiDAR-based 3D object de-             These 3D coordinates are either entered as additional in-
tection is not the quality of the estimated depth but its repre-   put channels into a 2D detection pipeline, or used to extract
sentation. Second, we propose pseudo-LiDAR as a new rec-           hand-crafted features. Although these methods have made
ommended representation of estimated depth for 3D object           remarkable progress, the state-of-the-art for 3D object de-
detection and show that it leads to state-of-the-art stereo-       tection performance lags behind LiDAR-based methods. As
based 3D object detection, effectively tripling prior art. Our     we discuss in Section 3, this might be because of the depth
results point towards the possibility of using stereo cameras      representation used by these methods.
3. Approach                                                       system, as follows,

    Despite the many advantages of image-based 3D object                        (depth)       z = D(u, v)                      (2)
recognition, there remains a glaring gap between the state-
                                                                                                 (u − cU ) × z
of-the-art detection rates of image and LiDAR-based ap-                         (width)       x=                               (3)
proaches (see Table 1 in Section 4.3). It is tempting to                                              fU
attribute this gap to the obvious physical differences and                                       (v − cV ) × z
                                                                                (height)      y=               ,               (4)
its implications between LiDAR and camera technology.                                                 fV
For example, the error of stereo-based 3D depth estimation
grows quadratically with the depth of an object, whereas          where (cU , cV ) is the pixel location corresponding to the
for Time-of-Flight (ToF) approaches, such as LiDAR, this          camera center and fV is the vertical focal length.
relationship is approximately linear.                                 By back-projecting all the pixels into 3D coordinates, we
                                                                  arrive at a 3D point cloud {(x(n) , y (n) , z (n) )}N
                                                                                                                      n=1 , where N
    Although some of these physical differences do likely
                                                                  is the pixel count. Such a point cloud can be transformed
contribute to the accuracy gap, in this paper we claim that a
                                                                  into any cyclopean coordinate frame given a reference view-
large portion of the discrepancy can be explained by the data
                                                                  point and viewing direction. We refer to the resulting point
representation rather than its quality or underlying physical
                                                                  cloud as pseudo-LiDAR signal.
properties associated with data collection.
    In fact, recent algorithms for stereo depth estimation can
generate surprisingly accurate depth maps [3] (see figure 1).     LiDAR vs. pseudo-LiDAR. In order to be maximally
Our approach to “close the gap” is therefore to carefully re-     compatible with existing LiDAR detection pipelines we ap-
move the differences between the two data modalities and          ply a few additional post-processing steps on the pseudo-
align the two recognition pipelines as much as possible. To       LiDAR data. Since real LiDAR signals only reside in a cer-
this end, we propose a two-step approach by first estimating      tain range of heights, we disregard pseudo-LiDAR points
the dense pixel depth from stereo (or even monocular) im-         beyond that range. For instance, on the KITTI bench-
agery and then back-projecting pixels into a 3D point cloud.      mark, following [36], we remove all points higher than 1m
By viewing this representation as pseudo-LiDAR signal, we         above the fictitious LiDAR source (located on top of the au-
can then apply any existing LiDAR-based 3D object detec-          tonomous vehicle). As most objects of interest (e.g., cars
tion algorithm. Fig. 2 depicts our pipeline.                      and pedestrians) do not exceed this height range there is
                                                                  little information loss. In addition to depth, LiDAR also re-
                                                                  turns the reflectance of any measured pixel (within [0,1]).
Depth estimation. Our approach is agnostic to different           As we have no such information, we simply set the re-
depth estimation algorithms. We primarily work with stereo        flectance to 1.0 for every pseudo-LiDAR points.
disparity estimation algorithms [3, 21], although our ap-             Fig 1 depicts the ground-truth LiDAR and the pseudo-
proach can easily use monocular depth estimation methods.         LiDAR points for the same scene from the KITTI
    A stereo disparity estimation algorithm takes a pair of       dataset [11, 12]. The depth estimate was obtained with
left-right images Il and Ir as input, captured from a pair        the pyramid stereo matching network (PSMNet) [3]. Sur-
of cameras with a horizontal offset (i.e., baseline) b, and       prisingly, the pseudo-LiDAR points (blue) align remarkably
outputs a disparity map Y of the same size as either one of       well to true LiDAR points (yellow), in contrast to the com-
the two input images. Without loss of generality, we assume       mon belief that low precision image-based depth is the main
the depth estimation algorithm treats the left image, Il , as     cause of inferior 3D object detection. We note that a LiDAR
reference and records in Y the horizontal disparity to Ir for     can capture > 100, 000 points for a scene, which is of the
each pixel. Together with the horizontal focal length fU          same order as the pixel count. Nevertheless, LiDAR points
of the left camera, we can derive the depth map D via the         are distributed along a few (typically 64 or 128) horizontal
following transform,                                              beams, only sparsely occupying the 3D space.

                                fU × b                            3D object detection. With the estimated pseudo-LiDAR
                    D(u, v) =            .                 (1)
                                Y (u, v)                          points, we can apply any existing LiDAR-based 3D object
                                                                  detectors for autonomous driving. In this work, we con-
                                                                  sider those based on multimodal information (i.e., monoc-
Pseudo-LiDAR generation. Instead of incorporating the             ular images + LiDAR), as it is only natural to incorporate
depth D as multiple additional channels to the RGB im-            the original visual information together with the pseudo-
ages, as is typically done [33], we can derive the 3D location    LiDAR data. Specifically, we experiment on AVOD [17]
(x, y, z) of each pixel (u, v), in the left camera’s coordinate   and frustum PointNet [25], the two top ranked algorithms
Stereo/Mono images      Depth estimation        Depth map            Pseudo LiDAR      3D object detection          Predicted 3D boxes

                           Stereo/Mono                                                     LiDAR-based
                               depth                                                         detection

Figure 2: The proposed pipeline for image-based 3D object detection. Given stereo or monocular images, we first predict
the depth map, followed by back-projecting it into a 3D point cloud in the LiDAR coordinate system. We refer to this
representation as pseudo-LiDAR, and process it exactly like LiDAR — any LiDAR-based detection algorithms can be applied.

                                                                  Depth Map                         Depth Map (Convolved)
with open-sourced code on the KITTI benchmark. In gen-
eral, we distinguish between two different setups:

 a) In the first setup we treat the pseudo-LiDAR informa-
                                                                  Pseudo-LiDAR                      Pseudo-LiDAR (Convolved)
    tion as a 3D point cloud. Here, we use frustum Point-
    Net [25], which projects 2D object detections [19] into
    a frustum in 3D, and then applies PointNet [26] to ex-
    tract point-set features at each 3D frustum.

 b) In the second setup we view the pseudo-LiDAR infor-
    mation from a Bird’s Eye View (BEV). In particular,
    the 3D information is converted into a 2D image from          Figure 3: We apply a single 2D convolution with a uniform
    the top-down view: width and depth become the spa-            kernel to the frontal view depth map (top-left). The result-
    tial dimensions, and height is recorded in the channels.      ing depth map (top-right), after back-projected into pseudo-
    AVOD connects visual features and BEV LiDAR fea-              LiDAR and displayed from the bird’s-eye view (bottom-
    tures to 3D box proposals and then fuses both to per-         right), reveals a large depth distortion in comparison to the
    form box classification and regression.                       original pseudo-LiDAR representation (bottom-left), espe-
                                                                  cially for far-away objects. We mark points of each car in-
                                                                  stance by a color. The boxes are super-imposed and contain
Data representation matters. Although pseudo-LiDAR                all points of the green and cyan cars respectively.
conveys the same information as a depth map, we claim
that it is much better suited for 3D object detection pipelines
that are based on deep convolutional networks. To see this,          In contrast, 3D convolutions on point clouds or 2D con-
consider the core module of the convolutional network: 2D         volutions in the bird’s-eye view slices operate on pixels that
convolutions. A convolutional network operating on images         are physically close together (although the latter do pull to-
or depth maps performs a sequence of 2D convolutions on           gether pixels from different heights, the physics of the world
the image/depth map. Although the filters of the convolu-         implies that pixels at different heights at a particular spatial
tion can be learned, the central assumption is two-fold: (a)      location usually do belong to the same object). In addi-
local neighborhoods in the image have meaning, and the            tion, both far-away objects and nearby objects are treated
network should look at local patches, and (b) all neighbor-       exactly the same way. These operations are thus inherently
hoods can be operated upon in an identical manner.                more physically meaningful and hence should lead to better
    These are but imperfect assumptions. First, local patches     learning and more accurate models.
on 2D images are only coherent physically if they are en-            To illustrate this point further, in Fig. 3 we conduct a
tirely contained in a single object. If they straddle object      simple experiment. In the left column, we show the origi-
boundaries, then two pixels can be co-located next to each        nal depth-map and the pseudo-LiDAR representation of an
other in the depth map, yet can be very far away in 3D            image scene. The four cars in the scene are highlighted in
space. Second, objects that occur at multiple depths project      color. We then perform a single 11 × 11 convolution with
to different scales in the depth map. A similarly sized patch     a box filter on the depth-map (top right), which matches the
might capture just a side-view mirror of a nearby car or the      receptive field of 5 layers of 3 × 3 convolutions. We then
entire body of a far-away car. Existing 2D object detec-          convert the resulting (blurred) depth-map into a pseudo-
tion approaches struggle with this breakdown of assump-           LiDAR representation (bottom right). From the figure, it
tions and have to design novel techniques such as feature         becomes evident that this new pseudo-LiDAR representa-
pyramids [19] to deal with this challenge.                        tion suffers substantially from the effects of the blurring.
The cars are stretched out far beyond their actual physical      Scene Flow dataset [21], with over 30,000 pairs of synthetic
proportions making it essentially impossible to locate them      images and dense disparity maps, and fine-tuned on the 200
precisely. For better visualization, we added rectangles that    training pairs of KITTI stereo 2015 benchmark [12, 22]. We
contain all the points of the green and cyan cars. After the     note that, MLF- STEREO [33] also uses the released D ISP -
convolution, both bounding boxes capture highly erroneous        N ET model. The third approach, SPS- STEREO [35], is non-
areas. Of course, the 2D convolutional network will learn        learning-based and has been used in [5, 6, 24].
to use more intelligent filters than box filters, but this ex-       D ISP N ET has two versions, without and with correla-
ample goes to show how some operations the convolutional         tions layers. We test both and denote them as D ISP N ET-S
network might perform could border on the absurd.                and D ISP N ET-C, respectively.
                                                                     While performing these experiments, we found that the
4. Experiments                                                   200 training images of KITTI stereo 2015 overlap with the
                                                                 validation images of KITTI object detection. That is, the re-
   We evaluate 3D-object detection with and without              leased PSMN ET and D ISP N ET models actually used some
pseudo-LiDAR across different settings with varying              validation images of detection. We therefore train a version
approaches for depth estimation and object detection.            of PSMN ET using Scene Flow followed by finetuning on
Throughout, we will highlight results obtained with pseudo-      the 3,712 training images of detection, instead of the 200
LiDAR in blue and those with actual LiDAR in gray.               KITTI stereo images. We obtain pseudo disparity ground
                                                                 truth by projecting the corresponding LiDAR points into
4.1. Setup
                                                                 the 2D image space. We denote this version PSMN ET?.
Dataset. We evaluate our approach on the KITTI object            Details are included in the Supplementary Material.
detection benchmark [11, 12], which contains 7,481 images            The results with PSMN ET? in Table 3 (fined-tuned on
for training and 7,518 images for testing. We follow the         3,712 training data) are in fact better than PSMN ET (fine-
same training and validation splits as suggested by Chen et      tuned on KITTI stereo 2015). We attribute the improved
al. [5], containing 3,712 and 3,769 images respectively. For     accuracy of PSMN ET? on the fact that it is trained on a
each image, KITTI provides the corresponding Velodyne            larger training set. Nevertheless, future work on 3D object
LiDAR point cloud, right image for stereo information, and       detection using stereo must be aware of this overlap.
camera calibration matrices.
                                                                 Monocular depth estimation. We use the state-of-the-art
Metric. We focus on 3D and bird’s-eye-view (BEV)             1   monocular depth estimator DORN [10], which is trained by
object detection and report the results on the validation        the authors on 23,488 KITTI images. We note that some
set. Specifically, we focus on the “car” category, follow-       of these images may overlap with our validation data for
ing [7, 34]. We follow the benchmark and prior work and          detection. Nevertheless, we decided to still include these
report average precision (AP) with the IoU thresholds at         results and believe they could serve as an upper bound for
0.5 and 0.7. We denote AP for the 3D and BEV tasks by            monocular-based 3D object detection. Future work, how-
AP3D and APBEV , respectively. Note that the benchmark di-       ever, must be aware of this overlap.
vides each category into three cases — easy, moderate, and
hard — according to the bounding box height and occlu-           Pseudo-LiDAR generation. We back-project the esti-
sion/truncation level. In general, the easy case corresponds     mated depth map into 3D points in the Velodyne LiDAR’s
to cars within 30 meters of the ego-car distance [36].           coordinate system using the provided calibration matrices.
                                                                 We disregard points with heights larger than 1 in the system.
Baselines. We compare to M ONO 3D [4], 3DOP [5], and
MLF [33]. The first is monocular and the second is stereo-       3D Object detection. We consider two algorithms: Frus-
based. MLF [33] reports results with both monocular [13]         tum PointNet (F-P OINT N ET) [25] and AVOD [17]. More
and stereo disparity [21], which we denote as MLF- MONO          specifically, we apply F-P OINT N ET-v1 and AVOD-FPN.
and MLF- STEREO, respectively.                                   Both of them use information from LiDAR and monocular
                                                                 images. We train both models on the 3,712 training data
4.2. Details of our approach                                     from scratch by replacing the LiDAR points with pseudo-
Stereo disparity estimation. We apply PSMN ET [3],               LiDAR data generated from stereo disparity estimation. We
D ISP N ET [21], and SPS- STEREO [35] to estimate dense          use the hyper-parameters provided in the released code.
disparity. The first two approaches are learning-based and           We note that AVOD takes image-specific ground planes
we use the released models, which are pre-trained on the         as inputs. The authors provide ground-truth planes for train-
                                                                 ing and validation images, but do not provide the proce-
  1 The BEV detection task is also called 3D localization.       dure to obtain them (for novel images). We therefore fit the
ground plane parameters with a straight-forward application     P OINT N ET) or use a convolutional network on the BEV
of RANSAC [9] to our pseudo-LiDAR points that fall into a       projection (in AVOD). This introduces invariance to depth,
certain range of road height, during evaluation. Details are    since far-away objects are no longer smaller. Furthermore,
included in the Supplementary Material.                         convolutions and pooling operations in these representa-
                                                                tions put together points that are physically nearby.
4.3. Experimental results                                           To further control for other differences between MLF-
    We summarize the main results in Table 1. We orga-          STEREO and our method we ablate our approach to use the
nize methods according to the input signals for performing      same frontal depth representation used by MLF- STEREO.
detection. Our stereo approaches based on pseudo-LiDAR          AVOD fuses information of the frontal images with BEV
significantly outperform all image-based alternatives by a      LiDAR features. We modify the algorithm, following
large margin. At IoU = 0.7 (moderate) — the metric used         [6, 33], to generate five frontal-view feature maps, including
to rank algorithms on the KITTI leaderboard — we achieve        3D pixel locations, disparity, and Euclidean distance to the
double the performance of the previous state of the art. We     camera. We concatenate them with the RGB channels while
also observe that pseudo-LiDAR is applicable and highly         disregarding the BEV branch in AVOD, making it fully de-
beneficial to two 3D object detection algorithms with very      pendent on the frontal-view branch. (We make no additional
different architectures, suggesting its wide compatibility.     architecture changes.) The results in Table 2 reveal a stag-
    One interesting comparison is between approaches using      gering gap between frontal and pseudo-LiDAR results. We
pseudo-LiDAR with monocular depth (DORN) and stereo             found that the frontal approach struggles with inferring ob-
depth (PSMN ET?). While DORN has been trained with              ject depth, even when the five extra maps have provided
almost ten times more images than PSMN ET? (and some            sufficient 3D information. Again, this might be because 2d
of them overlap with the validation data), the results with     convolutions put together pixels from far away depths, mak-
PSMN ET? dominate. This suggests that stereo-based de-          ing accurate localization difficult. This experiment suggests
tection is a promising direction to move in, especially con-    that the chief source of the accuracy improvement is indeed
sidering the increasing affordability of stereo cameras.        the pseudo-LiDAR representation.
    In the following section, we discuss key observations and
conduct a series of experiments to analyze the performance      Impact of stereo disparity estimation accuracy. We
gain through pseudo-LiDAR with stereo disparity.                compare PSMN ET [3] and D ISP N ET [21] on pseudo-
                                                                LiDAR-based detection accuracies. On the leaderboard of
Impact of data representation. When comparing our               KITTI stereo 2015, PSMN ET achieves 1.86% disparity er-
results using D ISP N ET-S or D ISP N ET-C to MLF-              ror, which far outperforms the error of 4.32% by D ISP N ET-
STEREO [33] (which also uses D ISP N ET as the underlying       C.
stereo engine), we observe a large performance gap (see Ta-         As shown in Table 3, the accuracy of disparity estima-
ble. 2). Specifically, at IoU= 0.7, we outperform MLF-          tion does not necessarily correlate with the accuracy of ob-
STEREO by at least 16% on APBEV and 16% on AP3D . The           ject detection. F-P OINT N ET with D ISP N ET-C even out-
later is equivalent to a 160% relative improvement. We          performs F-P OINT N ET with PSMN ET. This is likely due
attribute this improvement to the way in which we repre-        to two reasons. First, the disparity accuracy may not reflect
sent the resulting depth information. We note that both our     the depth accuracy: the same disparity error (on a pixel)
approach and MLF- STEREO [33] first back-project pixel          can lead to drastically different depth errors dependent on
depths into 3D point coordinates. MLF- STEREO construes         the pixel’s true depth, according to Eq. (1). Second, differ-
the 3D coordinates of each pixel as additional feature maps     ent detection algorithms process the 3D points differently:
in the frontal view. These maps are then concatenated with      AVOD quantizes points into voxels, while F-P OINT N ET
RGB channels as the input to a modified 2D object detection     directly processes them and may be vulnerable to noise.
pipeline based on Faster-RCNN [28]. As we point out ear-            By far the most accurate detection results are obtained
lier, this has two problems. Firstly, distant objects become    by PSMN ET?, which we trained from scratch on our own
smaller, and detecting small objects is a known hard prob-      KITTI training set. These results seem to suggest that sig-
lem [19]. Secondly, while performing local computations         nificant further improvements may be possible through end-
like convolutions or ROI pooling along height and width of      to-end training of the whole pipeline.
an image makes sense to 2D object detection, it will oper-          We provide results using SPS- STEREO [35] and further
ate on 2D pixel neighborhoods with pixels that are far apart    analysis on depth estimation in the Supplementary Material.
in 3D, making the precise localization of 3D objects much
harder (cf. Fig. 3).                                            Comparison to LiDAR information. Our approach sig-
    By contrast, our approach treats these coordinates as       nificantly improves stereo-based detection accuracies. A
pseudo-LiDAR signals and applies PointNet [26] (in F-           key remaining question is, how close the pseudo-LiDAR
Table 1: 3D object detection results on the KITTI validation set. We report APBEV / AP3D (in %) of the car category, corresponding
to average precision of the bird’s-eye view and 3D object box detection. Mono stands for monocular. Our methods with pseudo-LiDAR
estimated by PSMN ET? [3] (stereo) or DORN [10] (monocular) are in blue. Methods with LiDAR are in gray. Best viewed in color.

                                                              IoU = 0.5                                   IoU = 0.7
 Detection algorithm        Input signal          Easy        Moderate           Hard          Easy       Moderate         Hard
 M ONO 3D [4]                  Mono            30.5 / 25.2    22.4 / 18.2     19.2 / 15.5    5.2 / 2.5     5.2 / 2.3     4.1 / 2.3
 MLF- MONO [33]                Mono            55.0 / 47.9    36.7 / 29.5     31.3 / 26.4   22.0 / 10.5    13.6 / 5.7   11.6 / 5.4
 AVOD                          Mono            61.2 / 57.0    45.4 / 42.8     38.3 / 36.3   33.7 / 19.5   24.6 / 17.2   20.1 / 16.2
 F-P OINT N ET                 Mono            70.8 / 66.3    49.4 / 42.3     42.7 / 38.5   40.6 / 28.2   26.3 / 18.5   22.9 / 16.4
 3DOP [5]                      Stereo          55.0 / 46.0    41.3 / 34.6     34.6 / 30.1    12.6 / 6.6    9.5 / 5.1     7.6 / 4.1
 MLF- STEREO [33]              Stereo               -         53.7 / 47.4          -             -         19.5 / 9.8        -
 AVOD                          Stereo          89.0 / 88.5    77.5 / 76.4     68.7 / 61.2   74.9 / 61.9   56.8 / 45.3   49.0 / 39.0
  F-P OINT N ET                Stereo          89.8 / 89.5    77.6 / 75.5     68.2 / 66.3   72.8 / 59.4   51.8 / 39.8   44.0 / 33.5
 AVOD [17]                LiDAR + Mono         90.5 / 90.5    89.4 / 89.2     88.5 / 88.2   89.4 / 82.8   86.5 / 73.5   79.3 / 67.1
 F-P OINT N ET [25]       LiDAR + Mono         96.2 / 96.1    89.7 / 89.3     86.8 / 86.2   88.1 / 82.6   82.2 / 68.8   74.0 / 62.0

Table 2: Comparison between frontal and pseudo-LiDAR repre-          Table 4: 3D object detection on the pedestrian and cyclist cat-
sentations. AVOD projects the pseudo-LiDAR representation into       egories on the validation set. We report APBEV / AP3D at IoU =
the bird-eye’s view (BEV). We report APBEV / AP3D (in %) of the      0.5 (the standard metric) and compare F-P OINT N ET with pseudo-
moderate car category at IoU = 0.7. The best result of each col-     LiDAR estimated by PSMN ET? (in blue) and LiDAR (in gray).
umn is in bold font. The results indicate strongly that the data
representation is the key contributor to the accuracy gap.                  Input signal       Easy       Moderate         Hard
                                                                                                Pedestrian
 Detection Disparity Representation APBEV / AP3D                          Stereo            41.3 / 33.8 34.9 / 27.4     30.1 / 24.0
 MLF [33] D ISP N ET        Frontal  19.5 / 9.8                        LiDAR + Mono         69.7 / 64.7 60.6 / 56.5     53.4 / 49.9
 AVOD      D ISP N ET-S Pseudo-LiDAR 36.3 / 27.0                                                  Cyclist
 AVOD      D ISP N ET-C Pseudo-LiDAR 36.5 / 26.2                          Stereo            47.6 / 41.3 29.9 / 25.2     27.0 / 24.9
 AVOD      PSMN ET?         Frontal  11.9 / 6.6                        LiDAR + Mono         70.3 / 66.6 55.0 / 50.9     52.0 / 46.6
 AVOD      PSMN ET? Pseudo-LiDAR 56.8 / 45.3

Table 3: Comparison of different combinations of stereo dispar-      are not surprising, since stereo algorithms are known to
ity and 3D object detection algorithms, using pseudo-LiDAR. We       have larger depth errors for far-away objects, and a stricter
report APBEV / AP3D (in %) of the moderate car category at IoU       metric requires higher depth precision. Both observations
= 0.7. The best result of each column is in bold font.               emphasize the need for accurate depth estimation, espe-
                                                                     cially for far-away distances, to bridge the gap further. A
                             Detection algorithm
                                                                     key limitation of our results may be the low resolution of
         Disparity        AVOD         F-P OINT N ET
                                                                     the 0.4 MegaPixel images, which cause far away objects to
        D ISP N ET-S     36.3 / 27.0    31.9 / 23.5                  only consist of a few pixels.
        D ISP N ET-C     36.5 / 26.2    37.4 / 29.2
        PSMN ET          39.2 / 27.4    33.7 / 26.7
        PSMN ET?         56.8 / 45.3    51.8 / 39.8                  Pedestrian and cyclist detection. We also present results
                                                                     on 3D pedestrian and cyclist detection. These are much
                                                                     more challenging tasks than car detection due to the small
detection results are to those based on real LiDAR signal.           sizes of the objects, even given LiDAR signals. At an IoU
In Table 1, we further compare to AVOD and F-P OINT N ET             threshold of 0.5, both APBEV and AP3D of pedestrians and
when actual LiDAR signal is available. For fair comparison,          cyclists are much lower than that of cars at IoU 0.7 [25].
we retrain both models. For the easy cases with IoU = 0.5,           We also notice that none of the prior work on image-based
our stereo-based approach performs very well, only slightly          methods report results in this category.
worse than the corresponding LiDAR-based version. How-                   Table 4 shows our results with F-P OINT N ET and com-
ever, as the instances become harder (e.g., for cars that are        pares to those with LiDAR, on the validation set. Compared
far away), the performance gaps resurfaces — although not            to the car category (cf. Table 1), the performance gap is sig-
nearly as pronounced as without pseudo-LiDAR. We also                nificant. We also observe a similar trend that the gap be-
see a larger gap when moving to IoU = 0.7. These results             comes larger when moving to the hard cases. Nevertheless,
                   LiDAR                             Pseudo-LiDAR (Stereo)                      Front-View (Stereo)

Figure 4: Qualitative comparison. We compare AVOD with LiDAR, pseudo-LiDAR, and frontal-view (stereo). Ground-
truth boxes are in red, predicted boxes in green; the observer in the pseudo-LiDAR plots (bottom row) is on the very left side
looking to the right. The frontal-view approach (right) even miscalculates the depths of nearby objects and misses far-away
objects entirely. Best viewed in color.

Table 5: 3D object detection results on the car category on the   nearby objects. This corroborates the quantitative results
test set. We compare pseudo-LiDAR with PSMN ET? (in blue)         we observed in Table 2. We provide additional qualitative
and LiDAR (in gray). We report APBEV / AP3D at IoU = 0.7. †:      results and failure cases in the Supplementary Material.
Results on the KITTI leaderboard.

    Input signal         Easy      Moderate           Hard
                                                                  5. Discussion and Conclusion
                           AVOD                                      Sometimes, it is the simple discoveries that make the
     Stereo           66.8 / 55.4 47.2 / 37.2      40.3 / 31.4    biggest differences. In this paper we have shown that a key
 †LiDAR + Mono        88.5 / 81.9 83.8 / 71.9      77.9 / 66.4    component to closing the gap between image- and LiDAR-
                       F-P OINT N ET                              based 3D object detection may be simply the representation
     Stereo           55.0 / 39.7 38.7 / 26.7      32.9 / 22.3    of the 3D information. It may be fair to consider these re-
 †LiDAR + Mono        88.7 / 81.2 84.0 / 70.4      75.3 / 62.2    sults as the correction of a systemic inefficiency rather than
                                                                  a novel algorithm — however, that does not diminish its
                                                                  importance. Our findings are consistent with our under-
our approach has set a solid starting point for image-based       standing of convolutional neural networks and substantiated
pedestrian and cyclist detection for future work.                 through empirical results. In fact, the improvements we ob-
                                                                  tain from this correction are unprecedentedly high and af-
4.4. Results on the test set
                                                                  fect all methods alike. With this quantum leap it is plau-
   We report our results on the car category on the test set      sible that image-based 3D object detection for autonomous
in Table 5. We see a similar gap between pseudo-LiDAR             vehicle will become a reality in the near future. The im-
and LiDAR as on the validation set, suggesting that our ap-       plications of such a prospect are enormous. Currently, the
proach does not simply over-fit to the “validation data.” We      LiDAR hardware is arguably the most expensive additional
also note that, at the time we submit the paper, we are at        component required for robust autonomous driving. With-
the first place among all the image-based algorithms on the       out it, the additional hardware cost for autonomous driving
KITTI leaderboard. Details and results on the pedestrian          becomes relatively minor. Further, image-based object de-
and cyclist categories are in the Supplementary Material.         tection would also be beneficial even in the presence of Li-
                                                                  DAR equipment. One could imagine a scenario where the
4.5. Visualization                                                LiDAR data is used to continuously train and fine-tune an
    We further visualize the prediction results on valida-        image-based classifier. In case of our sensor outage, the
tion images in Fig. 4. We compare LiDAR (left), stereo            image-based classifier could likely function as a very reli-
pseudo-LiDAR (middle), and frontal stereo (right). We             able backup. Similarly, one could imagine a setting where
used PSMN ET? to obtain the stereo depth maps. LiDAR              high-end cars are shipped with LiDAR hardware and con-
and pseudo-LiDAR lead to highly accurate predictions, es-         tinuously train the image-based classifiers that are used in
pecially for the nearby objects. However, pseudo-LiDAR            cheaper models.
fails to detect far-away objects precisely due to inaccurate
depth estimates. On the other hand, the frontal-view-based        Future work. There are multiple immediate directions
approach makes extremely inaccurate predictions, even for         along which our results could be improved in future work:
First, higher resolution stereo images would likely signif-           [7] X. Chen, H. Ma, J. Wan, B. Li, and T. Xia. Multi-view 3d
icantly improve the accuracy for faraway objects. Our re-                 object detection network for autonomous driving. In CVPR,
sults were obtained with 0.4 megapixels — a far cry from                  2017. 2, 5
the state-of-the-art camera technology. Second, in this pa-           [8] D. Eigen, C. Puhrsch, and R. Fergus. Depth map prediction
per we did not focus on real-time image processing and the                from a single image using a multi-scale deep network. In
                                                                          Advances in neural information processing systems, pages
classification of all objects in one image takes on the or-
                                                                          2366–2374, 2014. 2
der of 1s. However, it is likely possible to improve these
                                                                      [9] M. A. Fischler and R. C. Bolles. Random sample consen-
speeds by several orders of magnitude. Recent improve-                    sus: a paradigm for model fitting with applications to image
ments on real-time multi-resolution depth estimation [31]                 analysis and automated cartography. Communications of the
show that an effective way to speed up depth estimation is                ACM, 24(6):381–395, 1981. 6, 11
to first compute a depth map at low resolution and then in-          [10] H. Fu, M. Gong, C. Wang, K. Batmanghelich, and D. Tao.
corporate high-resolution to refine the previous result. The              Deep ordinal regression network for monocular depth esti-
conversion from a depth map to pseudo-LiDAR is very                       mation. In CVPR, pages 2002–2011, 2018. 2, 5, 7, 12
fast and it should be possible to drastically speed up the           [11] A. Geiger, P. Lenz, C. Stiller, and R. Urtasun. Vision meets
detection pipeline through e.g. model distillation [1] or                 robotics: The kitti dataset. The International Journal of
anytime prediction [15]. Finally, it is likely that future                Robotics Research, 32(11):1231–1237, 2013. 1, 3, 5
work could improve the state-of-the-art in 3D object detec-          [12] A. Geiger, P. Lenz, and R. Urtasun. Are we ready for au-
                                                                          tonomous driving? the kitti vision benchmark suite. In
tion through sensor fusion of LiDAR and pseudo-LiDAR.
                                                                          CVPR, 2012. 1, 2, 3, 5, 11
Pseudo-LiDAR has the advantage that its signal is much
                                                                     [13] C. Godard, O. Mac Aodha, and G. J. Brostow. Unsupervised
denser than LiDAR and the two data modalities could have                  monocular depth estimation with left-right consistency. In
complementary strengths. We hope that our findings will                   CVPR, 2017. 1, 2, 5
cause a revival of image-based 3D object recognition and             [14] K. He, G. Gkioxari, P. Dollár, and R. Girshick. Mask r-cnn.
our progress will motivate the computer vision community                  In ICCV, 2017. 11
to fully close the image/LiDAR gap in the near future.               [15] G. Huang, D. Chen, T. Li, F. Wu, L. van der Maaten, and
                                                                          K. Q. Weinberger. Multi-scale dense convolutional networks
Acknowledgments                                                           for efficient prediction. CoRR, abs/1703.09844, 2, 2017. 9
                                                                     [16] K. Karsch, C. Liu, and S. B. Kang. Depth extraction from
   This research is supported in part by grants from the Na-              video using non-parametric sampling. In ECCV, 2012. 2
tional Science Foundation (III-1618134, III-1526012, IIS-            [17] J. Ku, M. Mozifian, J. Lee, A. Harakeh, and S. Waslander.
1149882, IIS-1724282, and TRIPODS-1740822), the Of-                       Joint 3d proposal generation and object detection from view
fice of Naval Research DOD (N00014-17-1-2175), and the                    aggregation. In IROS, 2018. 2, 3, 5, 7, 11
Bill and Melinda Gates Foundation. We are thankful for               [18] M. Liang, B. Yang, S. Wang, and R. Urtasun. Deep contin-
generous support by Zillow and SAP America Inc. We                        uous fusion for multi-sensor 3d object detection. In ECCV,
                                                                          2018. 1, 2
thank Gao Huang for helpful discussion.
                                                                     [19] T.-Y. Lin, P. Dollár, R. B. Girshick, K. He, B. Hariharan, and
                                                                          S. J. Belongie. Feature pyramid networks for object detec-
References                                                                tion. In CVPR, volume 1, page 4, 2017. 4, 6
                                                                     [20] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ra-
 [1] C. Bucilu, R. Caruana, and A. Niculescu-Mizil. Model com-
                                                                          manan, P. Dollár, and C. L. Zitnick. Microsoft coco: Com-
     pression. In SIGKDD, 2006. 9
                                                                          mon objects in context. In ECCV, 2014. 11
 [2] F. Chabot, M. Chaouch, J. Rabarisoa, C. Teulière, and
                                                                     [21] N. Mayer, E. Ilg, P. Hausser, P. Fischer, D. Cremers,
     T. Chateau. Deep manta: A coarse-to-fine many-task net-
                                                                          A. Dosovitskiy, and T. Brox. A large dataset to train convo-
     work for joint 2d and 3d vehicle analysis from monocular
                                                                          lutional networks for disparity, optical flow, and scene flow
     image. In CVPR, 2017. 2
                                                                          estimation. In CVPR, 2016. 1, 2, 3, 5, 6
 [3] J.-R. Chang and Y.-S. Chen. Pyramid stereo matching net-        [22] M. Menze and A. Geiger. Object scene flow for autonomous
     work. In CVPR, 2018. 2, 3, 5, 6, 7, 11, 12                           vehicles. In CVPR, 2015. 5, 11
 [4] X. Chen, K. Kundu, Z. Zhang, H. Ma, S. Fidler, and R. Urta-     [23] A. Mousavian, D. Anguelov, J. Flynn, and J. Košecká. 3d
     sun. Monocular 3d object detection for autonomous driving.           bounding box estimation using deep learning and geometry.
     In CVPR, 2016. 2, 5, 7                                               In CVPR, 2017. 2
 [5] X. Chen, K. Kundu, Y. Zhu, A. G. Berneshawi, H. Ma, S. Fi-      [24] C. C. Pham and J. W. Jeon. Robust object proposals re-
     dler, and R. Urtasun. 3d object proposals for accurate object        ranking for object detection in autonomous driving using
     class detection. In NIPS, 2015. 1, 2, 5, 7                           convolutional neural networks. Signal Processing: Image
 [6] X. Chen, K. Kundu, Y. Zhu, H. Ma, S. Fidler, and R. Urtasun.         Communication, 53:110–122, 2017. 1, 2, 5
     3d object proposals using stereo imagery for accurate object    [25] C. R. Qi, W. Liu, C. Wu, H. Su, and L. J. Guibas. Frustum
     class detection. IEEE transactions on pattern analysis and           pointnets for 3d object detection from rgb-d data. In CVPR,
     machine intelligence, 40(5):1259–1272, 2018. 1, 2, 5, 6              2018. 2, 3, 4, 5, 7, 11, 12
[26] C. R. Qi, H. Su, K. Mo, and L. J. Guibas. Pointnet: Deep
     learning on point sets for 3d classification and segmentation.
     In CVPR, 2017. 2, 4, 6
[27] J. Ren, X. Chen, J. Liu, W. Sun, J. Pang, Q. Yan, Y.-W. Tai,
     and L. Xu. Accurate single stage detector using recurrent
     rolling convolution. In CVPR, 2017. 11
[28] S. Ren, K. He, R. Girshick, and J. Sun. Faster r-cnn: Towards
     real-time object detection with region proposal networks. In
     NIPS, 2015. 2, 6
[29] A. Saxena, M. Sun, and A. Y. Ng. Make3d: Learning 3d
     scene structure from a single still image. IEEE transactions
     on pattern analysis and machine intelligence, 31(5):824–
     840, 2009. 2
[30] S. Wang, S. Suo, W.-C. M. A. Pokrovsky, and R. Urtasun.
     Deep parametric continuous convolutional neural networks.
     In CVPR, 2018. 2
[31] Y. Wang, Z. Lai, G. Huang, B. H. Wang, L. van der Maaten,
     M. Campbell, and K. Q. Weinberger. Anytime stereo im-
     age depth estimation on mobile devices. arXiv preprint
     arXiv:1810.11408, 2018. 2, 9
[32] Y. Xiang, W. Choi, Y. Lin, and S. Savarese. Subcategory-
     aware convolutional neural networks for object proposals
     and detection. In WACV, 2017. 2
[33] B. Xu and Z. Chen. Multi-level fusion based 3d object de-
     tection from monocular images. In CVPR, 2018. 1, 2, 3, 5,
     6, 7
[34] D. Xu, D. Anguelov, and A. Jain. Pointfusion: Deep sensor
     fusion for 3d bounding box estimation. In CVPR, 2018. 5
[35] K. Yamaguchi, D. McAllester, and R. Urtasun. Efficient joint
     segmentation, occlusion labeling, stereo and flow estimation.
     In ECCV, 2014. 1, 5, 6, 11
[36] B. Yang, W. Luo, and R. Urtasun. Pixor: Real-time 3d object
     detection from point clouds. In CVPR, 2018. 2, 3, 5
[37] Y. Zhou and O. Tuzel. Voxelnet: End-to-end learning for
     point cloud based 3d object detection. In CVPR, 2018. 2
           Supplementary Material                                  Table 6: Comparison of different stereo disparity methods on
                                                                   pseudo-LiDAR-based detection accuracy with AVOD. We report
                                                                   APBEV / AP3D (in %) of the moderate car category at IoU = 0.7.
   In this Supplementary Material, we provide details omit-
ted in the main text.                                                       Method       Disparity       APBEV / AP3D
                                                                                       SPS- STEREO        39.1 / 28.3
  • Section A: additional details on our approach (Sec-                                D ISP N ET-S       36.3 / 27.0
    tion 4.2 of the main paper).                                            AVOD       D ISP N ET-C       36.5 / 26.2
                                                                                       PSMN ET            39.2 / 27.4
  • Section B: results using SPS- STEREO [35] (Sec-                                    PSMN ET?           56.8 / 45.3
    tion 4.3 of the main paper).
                                                                   Table 7: The impact of over-smoothing the depth estimates
  • Section C: further analysis on depth estimation (Sec-          on the 3D detection results. We evaluate pseudo-LiDAR with
    tion 4.3 of the main paper).                                   PSMN ET?. We report APBEV / AP3D (in %) of the moderate car
                                                                   category at IoU = 0.7 on the validation set.
  • Section D: additional results on the test set (Section 4.4
                                                                                                 Detection algorithm
    of the main paper).
                                                                           Depth estimates    AVOD         F-P OINT N ET
                                                                           Non-smoothed      56.8 / 45.3    51.8 / 39.8
  • Section E: additional qualitative results (Section 4.5 of              Over-smoothed     53.7 / 37.8    48.3 / 31.6
    the main paper).

A. Additional Details of Our Approach                              B. Results Using SPS- STEREO [35]
A.1. Ground plane estimation                                          In Table 6, we report the 3D object detection accuracy
                                                                   of pseudo-LiDAR with SPS- STEREO [35], a non-learning-
   As mentioned in the main paper, AVOD [17] takes                 based stereo disparity approach. On the leaderboard of
image-specific ground planes as inputs. A ground plane is          KITTI stereo 2015, SPS- STEREO achieves 3.84% disparity
parameterized by a normal vector w = [wx , wy , wz ]> ∈            error, which is worse than the error of 1.86% by PSMN ET
R3 and a ground height h ∈ R. We estimate the pa-                  but better than 4.32% by D ISP N ET-C. The object detection
rameters according to the pseudo-LiDAR points {p(n) =              results with SPS- STEREO are on par with those with PSM-
[x(n) , y (n) , z (n) ]> }N
                          n=1 (see Section 3 of the main paper).   N ET and D ISP N ET, even if it is not learning-based.
Specifically, we consider points that are close to the camera
and fall into a certain range of possible ground heights:          C. Further Analysis on Depth Estimation
              (width)       15.0 ≥ x ≥ −15.0,               (5)       We study how over-smoothing the depth estimates
                                                                   would impact the 3D object detection accuracy. We train
              (height)     1.86 ≥ y ≥ 1.5,                  (6)    AVOD [17] and F-P OINT N ET [25] using pseudo-LiDAR
              (depth)      40.0 ≥ z ≥ 0.0.                  (7)    with PSMN ET?. During evaluation, we obtain over-
                                                                   smoothed depth estimates using an average kernel of size
Ideally, all these points will be on the plane: w> p + h = 0.      11 × 11 on the depth map. Table 7 shows the results: over-
We fit the parameters with a straight-forward application of       smoothing leads to degraded performance, suggesting the
RANSAC [9], in which we constraint wy = −1. We then                importance of high quality depth estimation for accurate 3D
normalize the resulting w to have a unit `2 norm.                  object detection.

A.2. Pseudo disparity ground truth                                 D. Additional Results on the Test Set
   We train a version of PSMN ET [3] (named PSMN ET?)                  We report the results on the pedestrian and cyclist cate-
using the 3,712 training images of detection, instead of the       gories on the KITTI test set in Table 8. For F-P OINT N ET
200 KITTI stereo images [12, 22]. We obtain pseudo dispar-         which takes 2D bounding boxes as inputs, [25] does not pro-
ity ground truth as follows: We project the corresponding          vide the 2D object detector trained on KITTI or the detected
LiDAR points into the 2D image space, followed by apply-           2D boxes on the test images. Therefore, for the car category
ing Eq. (1) of the main paper to derive disparity from pixel       we apply the released RRC detector [27] trained on KITTI
depth. If multiple LiDAR points are projected to a single          (see Table 5 in the main paper). For the pedestrian and cy-
pixel location, we randomly keep one of them. We ignore            clist categories, we apply Mask R-CNN [14] trained on MS
those pixels with no depth (disparity) in training PSMN ET.        COCO [20]. The detected 2D boxes are then inputted into
Table 8: 3D object detection results on the pedestrian and cy-          E. Additional Qualitative Results
clist categories on the test set. We compare pseudo-LiDAR with
PSMN ET? (in blue) and LiDAR (in gray). We report APBEV /               E.1. LiDAR vs. pseudo-LiDAR
AP3D at IoU = 0.5 (the standard metric). †: Results on the KITTI
                                                                           We include in Fig. 5 more qualitative results comparing
leaderboard.
                                                                        the LiDAR and pseudo-LiDAR signals. The pseudo-LiDAR
    Method       Input signal       Easy    Moderate       Hard         points are generated by PSMN ET?. Similar to Fig. 1 in the
                            Pedestrian                                  main paper, the two modalities align very well.
    AVOD            Stereo      27.5 / 25.2 20.6 / 19.0 19.4 / 15.3
 F-P OINT N ET      Stereo      31.3 / 29.8 24.0 / 22.1 21.9 / 18.8     E.2. PSMN ET vs. PSMN ET?
    AVOD       †LiDAR + Mono 58.8 / 50.8 51.1 / 42.8 47.5 / 40.9
 F-P OINT N ET †LiDAR + Mono 58.1 / 51.2 50.2 / 44.9 47.2 / 40.2            We further compare the pseudo-LiDAR points generated
                              Cyclist                                   by PSMN ET? and PSMN ET. The later is trained on the 200
    AVOD            Stereo      13.5 / 13.3 9.1 / 9.1 9.1 / 9.1         KITTI stereo images with provided denser ground truths.
 F-P OINT N ET      Stereo        4.1 / 3.7 3.1 / 2.8 2.8 / 2.1         As shown in Fig. 6, the two models perform fairly simi-
    AVOD       †LiDAR + Mono 68.1 / 64.0 57.5 / 52.2 50.8 / 46.6        larly for nearby distances. For far-away distances, however,
 F-P OINT N ET †LiDAR + Mono 75.4 / 72.0 62.0 / 56.8 54.7 / 50.4        the pseudo-LiDAR points by PSMN ET start to show no-
                                                                        table deviation from LiDAR signal. This result suggest that
                                                                        significant further improvements could be possible through
               Input                   Pseudo-Lidar (Bird’s-eye View)   learning disparity on a large training set or even end-to-end
                                                                        training of the whole pipeline.
                                                                        E.3. Visualization and failure cases
             Depth Map
                                                                           We provide additional visualization of the prediction re-
                                                                        sults (cf. Section 4.5 of the main paper). We consider
                                                                        AVOD with the following point clouds and representations.
                                                                          • LiDAR
Figure 5: Pseudo-LiDAR signal from visual depth esti-
mation. Top-left: a KITTI street scene with super-imposed                 • pseudo-LiDAR (stereo): with PSMN ET? [3]
bounding boxes around cars obtained with LiDAR (red) and
pseudo-LiDAR (green). Bottom-left: estimated disparity                    • pseudo-LiDAR (mono): with DORN [10]
map. Right: pseudo-LiDAR (blue) vs. LiDAR (yellow) —
                                                                          • frontal-view (stereo): with PSMN ET? [3]
the pseudo-LiDAR points align remarkably well with the
LiDAR ones. Best viewed in color (zoom in for details).                 We note that, as DORN [10] applies ordinal regression, the
                                                                        predicted monocular depth are discretized.
                                                                           As shown in Fig. 7, both LiDAR and pseudo-LiDAR
                                                                        (stereo or mono) lead to accurate predictions for the nearby
F-P OINT N ET [25]. We note that, MS COCO has no cyclist                objects. However, pseudo-LiDAR detects far-away objects
category. We thus use the detection results of bicycles as              less precisely (mislocalization: gray arrows) or even fails
the substitute.                                                         to detect them (missed detection: yellow arrows) due to
                                                                        in-accurate depth estimates, especially for the monocular
    On the pedestrian category, we see a similar gap between            depth. For example, pseudo-LiDAR (mono) completely
pseudo-LiDAR and LiDAR as the validation set (cf. Table 4               misses the four cars in the middle. On the other hand, the
in the main paper). However, on the cyclist category we see             frontal-view (stereo) based approach makes extremely inac-
a drastic performance drop by pseudo-LiDAR. This is likely              curate predictions, even for nearby objects.
due to the fact that cyclists are relatively uncommon in the               To analyze the failure cases, we show the precision-recall
KITTI dataset and the algorithms have over-fitted. For F-               (PR) curves on both 3D object and BEV detection in Fig. 8.
P OINT N ET, the detected bicycles may not provide accurate             The pseudo-LiDAR-based detection has a much lower re-
heights for cyclists, which essentially include riders and bi-          call compared to the LiDAR-based one, especially for the
cycles. Besides, the detected bicycles without riders are               moderate and hard cases (i.e., far-away or occluded ob-
false positives to cyclists, hence leading to a much worse              jects). That is, missed detections are one major issue that
accuracy.                                                               pseudo-LiDAR-based detection needs to resolve.
                                                                           We provide another qualitative result for failure cases in
  We note that, so far no image-based algorithms report                 Fig. 9. The partially occluded car is missed detected by
3D results on these two categories on the test set.                     AVOD with pseudo-LiDAR (the yellow arrow) even if it
             Image

             PSMNet Depth Map                                  PSMNet* Depth Map

             PSMNet Pseudo Lidar                               PSMNet* Pseudo Lidar

Figure 6: PSMN ET vs. PSMN ET?. Top: a KITTI street scene. Left column: the depth map and pseudo-LiDAR points
(from the bird’s-eye view) by PSMN ET, together with a zoomed-in region. Right column: the corresponding results by
PSMN ET?. The observer is on the very right side looking to the left. The pseudo-LiDAR points are in blue; LiDAR points
are in yellow. The pseudo-LiDAR points by PSMN ET have larger deviation at far-away distances. Best viewed in color
(zoom in for details).

is close to the observer, which likely indicates that stereo
disparity approaches suffer from noisy estimation around
occlusion boundaries.
                                  LiDAR                          pseudo-LiDAR (stereo)

                     pseudo-LiDAR (mono)                           frontal-view (stereo)

Figure 7: Qualitative comparison and failure cases. We compare AVOD with LiDAR, pseudo-LiDAR (stereo), pseudo-
LiDAR (monocular), and frontal-view (stereo). Ground-truth boxes are in red; predicted boxes in green. The observer in the
pseudo-LiDAR plots (bottom row) is on the very left side looking to the right. The mislocalization cases are indicated by
gray arrows; the missed detection cases are indicated by yellow arrows. The frontal-view approach (bottom-right) makes
extremely inaccurate predictions, even for nearby objects. Best viewed in color.
                                               Car                                                                    Car
                  1                                                                      1
                                                                Easy                                                                   Easy
                                                             Moderate                                                               Moderate
                                                                Hard                                                                   Hard
                 0.8                                                                    0.8

                 0.6                                                                    0.6
     Precision

                                                                            Precision
                 0.4                                                                    0.4

                 0.2                                                                    0.2

                  0                                                                      0
                       0       0.2      0.4            0.6        0.8   1                     0       0.2      0.4            0.6        0.8   1
                                              Recall                                                                 Recall

                 (a) 3D detection: AVOD + pseudo-LiDAR (stereo)                         (b) BEV detection: AVOD + pseudo-LiDAR (stereo)

                                               Car                                                                    Car
                  1                                                                      1
                                                                Easy                                                                   Easy
                                                             Moderate                                                               Moderate
                                                                Hard                                                                   Hard
                 0.8                                                                    0.8

                 0.6                                                                    0.6
     Precision

                                                                            Precision

                 0.4                                                                    0.4

                 0.2                                                                    0.2

                  0                                                                      0
                       0       0.2      0.4            0.6        0.8   1                     0       0.2      0.4            0.6        0.8   1
                                              Recall                                                                 Recall

                           (c) 3D detection: AVOD + LiDAR                                         (d) BEV detection: AVOD + LiDAR

Figure 8: Precision-recall curves. We compare the precision and recall on AVOD using pseudo-LiDAR with PSMN ET?
(top) and using LiDAR (bottom) on the test set. We obtain the curves from the KITTI website. We show both the 3D detection
results (left) and the BEV detection results (right). AVOD using pseudo-LiDAR has a much lower recall, suggesting that
missed detections are one of the major issues of pseudo-LiDAR-based detection.
                               LiDAR                                 pseudo-LiDAR (stereo)

Figure 9: Qualitative comparison and failure cases. We compare AVOD with LiDAR and pseudo-LiDAR (stereo).
Ground-truth boxes are in red; predicted boxes in green. The observer in the pseudo-LiDAR plots (bottom row) is on
the bottom side looking to the top. The pseudo-LiDAR-based detection misses the partially occluded car (the yellow arrow),
which is a hard case. Best viewed in color.
