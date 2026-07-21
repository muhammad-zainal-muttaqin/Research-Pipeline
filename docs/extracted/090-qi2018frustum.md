---
source_id: 090
bibtex_key: qi2018frustum
title: Frustum PointNets for 3D Object Detection from RGB-D Data
year: 2018
domain_theme: Deteksi 3D
verified_pdf: 90_Frustum PointNets.pdf
char_count: 105276
---

Frustum PointNets for 3D Object Detection from RGB-D Data

                                                     Charles R. Qi1∗    Wei Liu2      Chenxia Wu2       Hao Su3     Leonidas J. Guibas1
                                                                  1                        2               3
                                                                    Stanford University      Nuro, Inc.      UC San Diego

                                                                      Abstract                                                                     depth to point cloud
arXiv:1711.08488v2 [cs.CV] 13 Apr 2018

                                                                                                                                                                      3D box (from PointNet)
                                            In this work, we study 3D object detection from RGB-
                                         D data in both indoor and outdoor scenes. While previous
                                         methods focus on images or 3D voxels, often obscuring nat-
                                         ural 3D patterns and invariances of 3D data, we directly
                                         operate on raw point clouds by popping up RGB-D scans.                     2D region (from CNN) to 3D frustum
                                         However, a key challenge of this approach is how to effi-            Figure 1. 3D object detection pipeline. Given RGB-D data, we
                                         ciently localize objects in point clouds of large-scale scenes       first generate 2D object region proposals in the RGB image using a
                                         (region proposal). Instead of solely relying on 3D propos-           CNN. Each 2D region is then extruded to a 3D viewing frustum in
                                         als, our method leverages both mature 2D object detec-               which we get a point cloud from depth data. Finally, our frustum
                                         tors and advanced 3D deep learning for object localization,          PointNet predicts a (oriented and amodal) 3D bounding box for
                                         achieving efficiency as well as high recall for even small ob-       the object from the points in frustum.
                                         jects. Benefited from learning directly in raw point clouds,
                                         our method is also able to precisely estimate 3D bound-
                                         ing boxes even under strong occlusion or with very sparse            This data representation transformation, however, may ob-
                                         points. Evaluated on KITTI and SUN RGB-D 3D detection                scure natural 3D patterns and invariances of the data. Re-
                                         benchmarks, our method outperforms the state of the art by           cently, a number of papers have proposed to process point
                                         remarkable margins while having real-time capability.                clouds directly without converting them to other formats.
                                                                                                              For example, [25, 27] proposed new types of deep net archi-
                                                                                                              tectures, called PointNets, which have shown superior per-
                                                                                                              formance and efficiency in several 3D understanding tasks
                                         1. Introduction                                                      such as object classification and semantic segmentation.
                                            Recently, great progress has been made on 2D image un-                While PointNets are capable of classifying a whole point
                                         derstanding tasks, such as object detection [13] and instance        cloud or predicting a semantic class for each point in a point
                                         segmentation [14]. However, beyond getting 2D bounding               cloud, it is unclear how this architecture can be used for
                                         boxes or pixel masks, 3D understanding is eagerly in de-             instance-level 3D object detection. Towards this goal, we
                                         mand in many applications such as autonomous driving and             have to address one key challenge: how to efficiently pro-
                                         augmented reality (AR). With the popularity of 3D sensors            pose possible locations of 3D objects in a 3D space. Imi-
                                         deployed on mobile devices and autonomous vehicles, more             tating the practice in image detection, it is straightforward
                                         and more 3D data is captured and processed. In this work,            to enumerate candidate 3D boxes by sliding windows [8]
                                         we study one of the most important 3D perception tasks –             or by 3D region proposal networks such as [33]. However,
                                         3D object detection, which classifies the object category and        the computational complexity of 3D search typically grows
                                         estimates oriented 3D bounding boxes of physical objects             cubically with respect to resolution and becomes too ex-
                                         from 3D sensor data.                                                 pensive for large scenes or real-time applications such as
                                            While 3D sensor data is often in the form of point clouds,        autonomous driving.
                                         how to represent point cloud and what deep net architec-                 Instead, in this work, we reduce the search space fol-
                                         tures to use for 3D object detection remains an open prob-           lowing the dimension reduction principle: we take the ad-
                                         lem. Most existing works convert 3D point clouds to im-              vantage of mature 2D object detectors (Fig. 1). First, we
                                         ages by projection [36, 26] or to volumetric grids by quan-          extract the 3D bounding frustum of an object by extruding
                                         tization [40, 23, 26] and then apply convolutional networks.         2D bounding boxes from image detectors. Then, within the
                                                                                                              3D space trimmed by each of the 3D frustums, we consecu-
                                           ∗ Majority of the work done as an intern at Nuro, Inc.             tively perform 3D object instance segmentation and amodal

                                                                                                          1
3D bounding box regression using two variants of Point-            and use advanced 3D deep networks (PointNets) that can
Net. The segmentation network predicts the 3D mask of              exploit 3D geometry more effectively.
the object of interest (i.e. instance segmentation); and the           Bird’s eye view based methods: MV3D [6] projects Li-
regression network estimates the amodal 3D bounding box            DAR point cloud to bird’s eye view and trains a region pro-
(covering the entire object even if only part of it is visible).   posal network (RPN [29]) for 3D bounding box proposal.
    In contrast to previous work that treats RGB-D data as         However, the method lags behind in detecting small objects,
2D maps for CNNs, our method is more 3D-centric as we              such as pedestrians and cyclists and cannot easily adapt to
lift depth maps to 3D point clouds and process them us-            scenes with multiple objects in vertical direction.
ing 3D tools. This 3D-centric view enables new capabilities            3D based methods: [38, 34] train 3D object classifiers
for exploring 3D data in a more effective manner. First,           by SVMs on hand-designed geometry features extracted
in our pipeline, a few transformations are applied succes-         from point cloud and then localize objects using sliding-
sively on 3D coordinates, which align point clouds into a          window search. [8] extends [38] by replacing SVM with
sequence of more constrained and canonical frames. These           3D CNN on voxelized 3D grids. [30] designs new geomet-
alignments factor out pose variations in data, and thus make       ric features for 3D object detection in a point cloud. [35, 17]
3D geometry pattern more evident, leading to an easier job         convert a point cloud of the entire scene into a volumetric
of 3D learners. Second, learning in 3D space can better ex-        grid and use 3D volumetric CNN for object proposal and
ploits the geometric and topological structure of 3D space.        classification. Computation cost for those method is usu-
In principle, all objects live in 3D space; therefore, we be-      ally quite high due to the expensive cost of 3D convolutions
lieve that many geometric structures, such as repetition, pla-     and large 3D search space. Recently, [16] proposes a 2D-
narity, and symmetry, are more naturally parameterized and         driven 3D object detection method that is similar to ours
captured by learners that directly operate in 3D space. The        in spirit. However, they use hand-crafted features (based
usefulness of this 3D-centric network design philosophy has        on histogram of point coordinates) with simple fully con-
been supported by much recent experimental evidence.               nected networks to regress 3D box location and pose, which
    Our method achieve leading positions on KITTI 3D ob-           is sub-optimal in both speed and performance. In contrast,
ject detection [1] and bird’s eye view detection [2] bench-        we propose a more flexible and effective solution with deep
marks. Compared with the previous state of the art [6], our        3D feature learning (PointNets).
method is 8.04% better on 3D car AP with high efficiency
(running at 5 fps). Our method also fits well to indoor RGB-
D data where we have achieved 8.9% and 6.4% better 3D              Deep Learning on Point Clouds Most existing works
mAP than [16] and [30] on SUN-RGBD while running one               convert point clouds to images or volumetric forms before
to three orders of magnitude faster.                               feature learning. [40, 23, 26] voxelize point clouds into
    The key contributions of our work are as follows:              volumetric grids and generalize image CNNs to 3D CNNs.
                                                                   [19, 31, 39, 8] design more efficient 3D CNN or neural net-
   • We propose a novel framework for RGB-D data based
                                                                   work architectures that exploit sparsity in point cloud. How-
      3D object detection called Frustum PointNets.
                                                                   ever, these CNN based methods still require quantitization
  • We show how we can train 3D object detectors un-               of point clouds with certain voxel resolution. Recently, a
    der our framework and achieve state-of-the-art perfor-         few works [25, 27] propose a novel type of network archi-
    mance on standard 3D object detection benchmarks.              tectures (PointNets) that directly consumes raw point clouds
  • We provide extensive quantitative evaluations to vali-         without converting them to other formats. While PointNets
    date our design choices as well as rich qualitative re-        have been applied to single object classification and seman-
    sults for understanding the strengths and limitations of       tic segmentation, our work explores how to extend the ar-
    our method.                                                    chitecture for the purpose of 3D object detection.

                                                                   3. Problem Definition
2. Related Work
                                                                      Given RGB-D data as input, our goal is to classify and
3D Object Detection from RGB-D Data Researchers                    localize objects in 3D space. The depth data, obtained from
have approached the 3D detection problem by taking var-            LiDAR or indoor depth sensors, is represented as a point
ious ways to represent RGB-D data.                                 cloud in RGB camera coordinates. The projection matrix
   Front view image based methods: [4, 24, 41] take                is also known so that we can get a 3D frustum from a 2D
monocular RGB images and shape priors or occlusion pat-            image region. Each object is represented by a class (one
terns to infer 3D bounding boxes. [18, 7] represent depth          among k predefined classes) and an amodal 3D bounding
data as 2D maps and apply CNNs to localize objects in 2D           box. The amodal box bounds the complete object even if
image. In comparison we represent depth as a point cloud           part of the object is occluded or truncated. The 3D box is
        Depth                   2d region                       point cloud                                  segmented
                                proposal                        in frustum                                  object points       T-Net

                                                                                                                                                                       Box Parameters
                                                                 (n points)                                  (m points)

                                               region2frustum
        RGB image

                                                                                                                             center residual         Amodal
                                                                                  3D Instance

                                                                                                  masking
                                                                                                                                                     3D Box

                                                                                                                mxc
                                                                   nxc
                                                                                 Segmentation                                translation
                    CNN                                                                                                                             Estimation
                                                                                   PointNet
                                                                                                                                                     PointNet
                                                                    k
                                  one-hot class vector

                        Frustum Proposal                                      3D Instance Segmentation                      Amodal 3D Box Estimation

Figure 2. Frustum PointNets for 3D object detection. We first leverage a 2D CNN object detector to propose 2D regions and classify
their content. 2D regions are then lifted to 3D and thus become frustum proposals. Given a point cloud in a frustum (n × c with n points
and c channels of XYZ, intensity etc. for each point), the object instance is segmented by binary classification of each point. Based on the
segmented object point cloud (m × c), a light-weight regression PointNet (T-Net) tries to align points by translation such that their centroid
is close to amodal box center. At last the box estimation net estimates the amodal 3D bounding box for the object. More illustrations on
coordinate systems involved and network input, output are in Fig. 4 and Fig. 5.

parameterized by its size h, w, l, center cx , cy , cz , and ori-                          based model. We pre-train the model weights on ImageNet
entation θ, φ, ψ relative to a predefined canonical pose for                               classification and COCO object detection datasets and fur-
each category. In our implementation, we only consider the                                 ther fine-tune it on a KITTI 2D object detection dataset to
heading angle θ around the up-axis for orientation.                                        classify and predict amodal 2D boxes. More details of the
                                                                                           2D detector training are provided in the supplementary.
4. 3D Detection with Frustum PointNets
                                                                                           4.2. 3D Instance Segmentation
   As shown in Fig. 2, our system for 3D object detection
consists of three modules: frustum proposal, 3D instance                                       Given a 2D image region (and its corresponding 3D frus-
segmentation, and 3D amodal bounding box estimation. We                                    tum), several methods might be used to obtain 3D loca-
will introduce each module in the following subsections.                                   tion of the object: One straightforward solution is to di-
We will focus on the pipeline and functionality of each mod-                               rectly regress 3D object locations (e.g., by 3D bounding
ule, and refer readers to supplementary for specific architec-                             box) from a depth map using 2D CNNs. However, this
tures of the deep networks involved.                                                       problem is not easy as occluding objects and background
                                                                                           clutter is common in natural scenes (as in Fig. 3), which
4.1. Frustum Proposal                                                                      may severely distract the 3D localization task. Because ob-
    The resolution of data produced by most 3D sensors, es-                                jects are naturally separated in physical space, segmentation
pecially real-time depth sensors, is still lower than RGB                                  in 3D point cloud is much more natural and easier than that
images from commodity cameras. Therefore, we leverage                                      in images where pixels from distant objects can be near-by
mature 2D object detector to propose 2D object regions in                                  to each other. Having observed this fact, we propose to seg-
RGB images as well as to classify objects.
    With a known camera projection matrix, a 2D bounding
box can be lifted to a frustum (with near and far planes spec-
ified by depth sensor range) that defines a 3D search space
                                                                                                                                                                 Background
for the object. We then collect all points within the frustum                                                                                                    Clutter
to form a frustum point cloud. As shown in Fig 4 (a), frus-                                                                     Object of Interest
tums may orient towards many different directions, which
result in large variation in the placement of point clouds.                                                                             Foreground
                                                                                                                                          Occluder
We therefore normalize the frustums by rotating them to-
ward a center view such that the center axis of the frustum is
orthogonal to the image plane. This normalization helps im-                                                                                camera

prove the rotation-invariance of the algorithm. We call this                               Figure 3. Challenges for 3D detection in frustum point cloud.
entire procedure for extracting frustum point clouds from                                  Left: RGB image with an image region proposal for a person.
RGB-D data frustum proposal generation.                                                    Right: bird’s eye view of the LiDAR points in the extruded frus-
    While our 3D detection framework is agnostic to the ex-                                tum from 2D box, where we see a wide spread of points with both
act method for 2D region proposal, we adopt a FPN [20]                                     foreground occluder (bikes) and background clutter (building).
                  ..                     ..                        ..                    ..                                                                                  Set
                                                                                                                                                                                   T-Net

                                                                                                                                                                    mxc
                                                                                                             3D Instance Segmentation PointNet                            Abstraction      FCs
                                       .....

                                                                                                                                                                                                 3
                .....                                            .....                 .....                                                                                Layers

                                                                                                                                                              object point cloud          center residual
       z    .       frustum
                                   .           mask point
                                                             .           T-Net     .                             Set
                                                                                                                                   Point
                                                                                                                                  Feature
                                                                                                                                                             (mask coordinate)          (mask coordinate)

                                                                                                                                                 nx1
                    rotation                    centroid

                                                                                                       nxc
           .                      .                         .                     .
                                                                                                              Abstraction
                                                                                                                Layers
                                                                                                                                Propagation
                                                                                                                                  Layers
                                                                                                                                                                   Amodal 3D Box Estimation PointNet

                                                                                                                                                                                                 3+2NH+4NS
                                                                                                                                                                             Set

                                                                                                                                                                    mxc
   y                    x                                                                                                                                                 Abstraction      FCs
                                                                                                                                                                            Layers
                                                                                                 frustum point cloud                    object of interest
 (a) camera                 (b) frustum            (c) 3D mask             (d) 3D object       (frustum coordinate)                        probability
                                                                                                                                                              object point cloud          box parameters
 coordinate                 coordinate              coordinate              coordinate                                                                       (object coordinate)        (object coordinate)

Figure 4. Coordinate systems for point cloud. Artificial points                                Figure 5. Basic architectures and IO for PointNets. Architecture
(black dots) are shown to illustrate (a) default camera coordi-                                is illustrated for PointNet++ [27] (v2) models with set abstraction
nate; (b) frustum coordinate after rotating frustums to center view                            layers and feature propagation layers (for segmentation). Coordi-
(Sec. 4.1); (c) mask coordinate with object points’ centroid at ori-                           nate systems involved are visualized in Fig. 4.
gin (Sec. 4.2); (d) object coordinate predicted by T-Net (Sec. 4.3).

                                                                                               Having obtained these segmented object points, we further
ment instances in 3D point cloud instead of in 2D image or                                     normalize its coordinates to boost the translational invari-
depth map. Similar to Mask-RCNN [14], which achieves                                           ance of the algorithm, following the same rationale as in
instance segmentation by binary classification of pixels in                                    the frustum proposal step. In our implementation, we trans-
image regions, we realize 3D instance segmentation using a                                     form the point cloud into a local coordinate by subtracting
PointNet-based network on point clouds in frustums.                                            XYZ values by its centroid. This is illustrated in Fig. 4 (c).
   Based on 3D instance segmentation, we are able to                                           Note that we intentionally do not scale the point cloud, be-
achieve residual based 3D localization. That is, rather than                                   cause the bounding sphere size of a partial point cloud can
regressing the absolute 3D location of the object whose off-                                   be greatly affected by viewpoints and the real size of the
set from the sensor may vary in large ranges (e.g. from 5m                                     point cloud helps the box size estimation.
to beyond 50m in KITTI data), we predict the 3D bounding                                          In our experiments, we find that coordinate transforma-
box center in a local coordinate system – 3D mask coordi-                                      tions such as the one above and the previous frustum rota-
nates as shown in Fig. 4 (c).                                                                  tion are critical for 3D detection result as shown in Tab. 8.

3D Instance Segmentation PointNet. The network takes                                           4.3. Amodal 3D Box Estimation
a point cloud in frustum and predicts a probability score for                                     Given the segmented object points (in 3D mask coordi-
each point that indicates how likely the point belongs to the                                  nate), this module estimates the object’s amodal oriented
object of interest. Note that each frustum contains exactly                                    3D bounding box by using a box regression PointNet to-
one object of interest. Here those “other” points could be                                     gether with a preprocessing transformer network.
points of non-relevant areas (such as ground, vegetation) or
other instances that occlude or are behind the object of in-
                                                                                               Learning-based 3D Alignment by T-Net Even though
terest. Similar to the case in 2D instance segmentation, de-
                                                                                               we have aligned segmented object points according to their
pending on the position of the frustum, object points in one
                                                                                               centroid position, we find that the origin of the mask coordi-
frustum may become cluttered or occlude points in another.
                                                                                               nate frame (Fig. 4 (c)) may still be quite far from the amodal
Therefore, our segmentation PointNet is learning the occlu-
                                                                                               box center. We therefore propose to use a light-weight re-
sion and clutter patterns as well as recognizing the geometry
                                                                                               gression PointNet (T-Net) to estimate the true center of the
for the object of a certain category.
                                                                                               complete object and then transform the coordinate such that
   In a multi-class detection case, we also leverage the se-
                                                                                               the predicted center becomes the origin (Fig. 4 (d)).
mantics from a 2D detector for better instance segmenta-
tion. For example, if we know the object of interest is                                           The architecture and training of our T-Net is similar to
a pedestrian, then the segmentation network can use this                                       the T-Net in [25], which can be thought of as a special type
prior to find geometries that look like a person. Specifi-                                     of spatial transformer network (STN) [15]. However, differ-
cally, in our architecture we encode the semantic category                                     ent from the original STN that has no direct supervision on
as a one-hot class vector (k dimensional for the pre-defined                                   transformation, we explicitly supervise our translation net-
k categories) and concatenate the one-hot vector to the in-                                    work to predict center residuals from the mask coordinate
termediate point cloud features. More details of the specific                                  origin to real object center.
architectures are described in the supplementary.
   After 3D instance segmentation, points that are classified                                  Amodal 3D Box Estimation PointNet The box estima-
as the object of interest are extracted (“masking” in Fig. 2).                                 tion network predicts amodal bounding boxes (for entire
object even if part of it is unseen) for objects given an ob-                      In essence, the corner loss is the sum of the distances
ject point cloud in 3D object coordinate (Fig. 4 (d)). The                      between the eight corners of a predicted box and a ground
network architecture is similar to that for object classifica-                  truth box. Since corner positions are jointly determined by
tion [25, 27], however the output is no longer object class                     center, size and heading, the corner loss is able to regularize
scores but parameters for a 3D bounding box.                                    the multi-task training for those parameters.
   As stated in Sec. 3, we parameterize a 3D bounding box                          To compute the corner loss, we firstly construct N S ×
by its center (cx , cy , cz ), size (h, w, l) and heading angle                 N H “anchor” boxes from all size templates and heading
θ (along up-axis). We take a “residual” approach for box                        angle bins. The anchor boxes are then translated to the es-
center estimation. The center residual predicted by the box                     timated box center. We denote the anchor box corners as
estimation network is combined with the previous center                         Pkij , where i, j, k are indices for the size class, heading
residual from the T-Net and the masked points’ centroid to                      class, and (predefined) corner order, respectively. To avoid
recover an absolute center (Eq. 1). For box size and heading                    large penalty from flipped heading estimation, we further
angle, we follow previous works [29, 24] and use a hybrid                       compute distances to corners (Pk∗∗ ) from the flipped ground
of classification and regression formulations. Specifically                     truth box and use the minimum of the original and flipped
we pre-define N S size templates and N H equally split an-                      cases. δij , which is one for the ground truth size/heading
gle bins. Our model will both classify size/heading (N S                        class and zero else wise, is a two-dimensional mask used to
scores for size, N H scores for heading) to those pre-defined                   select the distance term we care about.
categories as well as predict residual numbers for each cate-
gory (3 × N S residual dimensions for height, width, length,                    5. Experiments
N H residual angles for heading). In the end the net outputs
3 + 4 × N S + 2 × N H numbers in total.                                            Experiments are divided into three parts1 . First we com-
                                                                                pare with state-of-the-art methods for 3D object detection
        Cpred = Cmask + ∆Ct−net + ∆Cbox−net                               (1)   on KITTI [10] and SUN-RGBD [33] (Sec 5.1). Second,
                                                                                we provide in-depth analysis to validate our design choices
4.4. Training with Multi-task Losses                                            (Sec 5.2). Last, we show qualitative results and discuss the
                                                                                strengths and limitations of our methods (Sec 5.3).
   We simultaneously optimize the three nets involved (3D
instance segmentation PointNet, T-Net and amodal box es-                        5.1. Comparing with state-of-the-art Methods
timation PointNet) with multi-task losses (as in Eq. 2).
Lc1−reg is for T-Net and Lc2−reg is for center regression                          We evaluate our 3D object detector on KITTI [11] and
of box estimation net. Lh−cls and Lh−reg are losses for                         SUN-RGBD [33] benchmarks for 3D object detection. On
heading angle prediction while Ls−cls and Ls−reg are for                        both tasks we have achieved significantly better results
box size. Softmax is used for all classification tasks and                      compared with state-of-the-art methods.
smooth-l1 (huber) loss is used for all regression cases.
                                                                                KITTI Tab. 1 shows the performance of our 3D detector
  Lmulti−task =Lseg + λ(Lc1−reg + Lc2−reg + Lh−cls +                            on the KITTI test set. We outperform previous state-of-the-
                                                                          (2)
                 Lh−reg + Ls−cls + Ls−reg + γLcorner )                          art methods by a large margin. While MV3D [6] uses multi-
                                                                                view feature aggregation and sophisticated multi-sensor fu-
Corner Loss for Joint Optimization of Box Parameters                            sion strategy, our method based on the PointNet [25] (v1)
While our 3D bounding box parameterization is compact                           and PointNet++ [27] (v2) backbone is much cleaner in de-
and complete, learning is not optimized for final 3D box ac-                    sign. While out of the scope for this work, we expect that
curacy – center, size and heading have separate loss terms.                     sensor fusion (esp. aggregation of image feature for 3D de-
Imagine cases where center and size are accurately pre-                         tection) could further improve our results.
dicted but heading angle is off – the 3D IoU with ground                            We also show our method’s performance on 3D object
truth box will then be dominated by the angle error. Ide-                       localization (bird’s eye view) in Tab. 2. In the 3D localiza-
ally all three terms (center,size,heading) should be jointly                    tion task bounding boxes are projected to bird’s eye view
optimized for best 3D box estimation (under IoU metric).                        plane and IoU is evaluated on oriented 2D boxes. Again,
To resolve this problem we propose a novel regularization                       our method significantly outperforms previous works which
loss, the corner loss:                                                          include DoBEM [42] and MV3D [6] that use CNNs on pro-
                                                                                jected LiDAR images, as well as 3D FCN [17] that uses 3D
            NS X
            X  NH                8
                                 X                      8
                                                        X                       CNNs on voxelized point cloud.
Lcorner =             δij min{         kPkij − Pk∗ k,         kPkij − Pk∗∗ k}
                                                                                   1 Details on network architectures, training parameters as well as more
            i=1 j=1              k=1                    i=1
                                                                          (3)   experiments are included in the supplementary material.
                                           Cars                        Pedestrians                     Cyclists
               Method
                                  Easy Moderate Hard           Easy Moderate Hard             Easy Moderate Hard
                DoBEM [42]        7.42      6.95      13.45      -         -           -       -           -          -
                MV3D [6]         71.09     62.35      55.12      -         -           -       -           -          -
                Ours (v1)        80.62     64.70      56.07   50.88      41.55      38.04    69.36      53.50      52.88
                Ours (v2)        81.20     70.39      62.19   51.21      44.89      40.23    71.96      56.77      50.39
Table 1. 3D object detection 3D AP on KITTI test set. DoBEM [42] and MV3D [6] (previous state of the art) are based on 2D CNNs with
bird’s eye view LiDAR image. Our method, without sensor fusion or multi-view aggregation, outperforms those methods by large margins
on all categories and data subsets. 3D bounding box IoU threshold is 70% for cars and 50% for pedestrians and cyclists.

                                           Cars                        Pedestrians                     Cyclists
               Method
                                Easy Moderate Hard              Easy Moderate Hard            Easy Moderate Hard
                DoBEM [42]      36.49      36.95      38.10      -          -          -        -         -           -
                3D FCN [17]     69.94      62.54      55.94      -          -          -        -         -           -
                MV3D [6]        86.02      76.90      68.49      -          -          -        -         -           -
                Ours (v1)       87.28      77.09      67.90    55.26     47.56       42.57    73.42     59.87      52.88
                Ours (v2)       88.70      84.00      75.33    58.09     50.22       47.20    75.38     61.96      54.68
Table 2. 3D object localization AP (bird’s eye view) on KITTI test set. 3D FCN [17] uses 3D CNNs on voxelized point cloud and is far
from real-time. MV3D [6] is the previous state of the art. Our method significantly outperforms those methods on all categories and data
subsets. Bird’s eye view 2D bounding box IoU threshold is 70% for cars and 50% for pedestrians and cyclists.

       Method                 Easy Moderate Hard                                   Benchmark              Easy Moderate Hard
       Mono3D [4]             2.53      2.31        2.31                   Pedestrian (3D Detection)     70.00       61.32      53.59
       3DOP [5]               6.55      5.07        4.10                 Pedestrian (Bird’s Eye View) 72.38          66.39      59.57
       VeloFCN [17]           15.20    13.66       15.98                     Cyclist (3D Detection)      77.15       56.49      53.37
       MV3D (LiDAR) [6]       71.19    56.60       55.30                   Cyclist (Bird’s Eye View)     81.82       60.03      56.32
       MV3D [6]               71.29    62.68       56.56               Table 5. Performance on KITTI val set for pedestrians and cyclists.
       Ours (v1)              83.26    69.28       62.56               Model evaluated is Ours (v2).
       Ours (v2)              83.76    70.92       63.65
Table 3. 3D object detection AP on KITTI val set (cars only).
                                                                       that image CNNs can be easily applied. However, methods
       Method                  Easy Moderate Hard                      designed for bird’s eye view may be incapable for indoor
       Mono3D [4]              5.22      5.19       4.13               rooms where multiple objects often exist together in verti-
       3DOP [5]                12.63     9.49       7.59               cal space. On the other hand, indoor focused methods could
       VeloFCN [17]            40.14    32.08      30.47               find it hard to apply to sparse and large-scale point cloud
       MV3D (LiDAR) [6]        86.18    77.32      76.33
                                                                       from LiDAR scans.
       MV3D [6]                86.55    78.10      76.67
       Ours (v1)               87.82    82.44      74.77
                                                                          In contrast, our frustum-based PointNet is a generic
       Ours (v2)               88.16    84.02      76.44               framework for both outdoor and indoor 3D object detec-
Table 4. 3D object localization AP on KITTI val set (cars only).       tion. By applying the same pipeline we used for KITTI data
                                                                       set, we’ve achieved state-of-the-art performance on SUN-
                                                                       RGBD benchmark (Tab. 6) with significantly higher mAP
   The output of our network is visualized in Fig. 6 where             as well as much faster (10x-1000x) inference speed.
we observe accurate 3D instance segmentation and box pre-
diction even under very challenging cases. We defer more               5.2. Architecture Design Analysis
discussions on success and failure case patterns to Sec. 5.3.
We also report performance on KITTI val set (the same split              In this section we provide analysis and ablation experi-
as in [6]) in Tab. 3 and Tab. 4 (for cars) to support compari-         ments to validate our design choices.
son with more published works, and in Tab. 5 (for pedestri-
ans and cyclists) for reference.                                       Experiment setup. Unless otherwise noted, all experi-
                                                                       ments in this section are based on our v1 model on KITTI
SUN-RGBD Most previous 3D detection works special-                     data using train/val split as in [6]. To decouple the influence
ize either on outdoor LiDAR scans where objects are well               of 2D detectors, we use ground truth 2D boxes for region
separated in space and the point cloud is sparse (so that              proposals and use 3D box estimation accuracy (IoU thresh-
it’s feasible for bird’s eye projection), or on indoor depth           old 0.7) as the evaluation metric. We will only focus on the
maps that are regular images with dense pixel values such              car category which has the most training examples.
Figure 6. Visualizations of Frustum PointNet results on KITTI val set (best viewed in color with zoom in). These results are based
on PointNet++ models [27], running at 5 fps and achieving test set 3D AP of 70.39, 44.89 and 56.77 for car, pedestrian and cyclist,
respectively. 3D instance masks on point cloud are shown in color. True positive detection boxes are in green, while false positive boxes
are in red and groundtruth boxes in blue are shown for false positive and false negative cases. Digit and letter beside each box denote
instance id and semantic class, with “v” for cars, “p” for pedestrian and “c” for cyclist. See Sec. 5.3 for more discussion on the results.

                    bathtub bed bookshelf chair desk dresser nightstand sofa table toilet                           Runtime     mAP
  DSS [35]           44.2     78.8       11.9      61.2    20.5      6.4        15.4      53.5 50.3        78.9      19.55s     42.1
  COG [30]           58.3     63.7       31.8      62.2 45.2        15.5        27.4      51.0 51.3        70.1 10-30min 47.6
  2D-driven [16]     43.5     64.5       31.4      48.3    27.9     25.9        41.9      50.4 37.0        80.4       4.15s     45.1
  Ours (v1)          43.3     81.1       33.3      64.2 24.7        32.0        58.1      61.1 51.1        90.9       0.12s     54.0
Table 6. 3D object detection AP on SUN-RGBD val set. Evaluation metric is average precision with 3D IoU threshold 0.25 as proposed
by [33]. Note that both COG [30] and 2D-driven [16] use room layout context to boost performance while ours and DSS [35] not.
Compared with previous state-of-the-arts our method is 6.4% to 11.9% better in mAP as well as one to three orders of magnitude faster.

Comparing with alternative approaches for 3D detec-                     sualize a typical 2D mask prediction in Fig. 7. While the
tion. In this part we evaluate a few CNN-based baseline                 estimated 2D mask appears in high quality on an RGB im-
approaches as well as ablated versions and variants of our              age, there are still lots of clutter and foreground points in
pipelines using 2D masks. In the first row of Tab. 7, we                the 2D mask. In comparison, our 3D instance segmenta-
show 3D box estimation results from two CNN-based net-                  tion gets much cleaner result, which greatly eases the next
works. The baseline methods trained VGG [32] models                     module in finer localization and bounding box regression.
on ground truth boxes of RGB-D images and adopt the
same box parameter and loss functions as our main method.                   In the third row of Tab. 7, we experiment with an ablated
While the model in the first row directly estimates box lo-             version of frustum PointNet that has no 3D instance seg-
cation and parameters from vanilla RGB-D image patch,                   mentation module. Not surprisingly, the model gets much
the other one (second row) uses a FCN trained from the                  worse results than our main method, which indicates the
COCO dataset for 2D mask estimation (as that in Mask-                   critical effect of our 3D instance segmentation module. In
RCNN [14]) and only uses features from the masked region                the fourth row, instead of 3D segmentation we use point
for prediction. The depth values are also translated by sub-            clouds from 2D masked depth maps (Fig. 7) for 3D box es-
tracting the median depth within the 2D mask. However,                  timation. However, since a 2D mask is not able to cleanly
both CNN baselines get far worse results compared to our                segment the 3D object, the performance is more than 12%
main method.                                                            worse than that with the 3D segmentation (our main method
                                                                        in the fifth row). On the other hand, a combined usage of 2D
   To understand why CNN baselines underperform, we vi-                 and 3D masks – applying 3D segmentation on point cloud
  network arch.     mask    depth representation accuracy                RGB         2d mask by CNN   points from masked     points from our 3d
                                                                                                         2d depth map      instance segmentation
     ConvNet           -           image           18.3                                                    (baseline)
     ConvNet         2D            image           27.4
     PointNet          -        point cloud        33.5
                                                                         depth
     PointNet        2D         point cloud        61.6
     PointNet        3D         point cloud        74.3
     PointNet      2D+3D        point cloud        70.0                          range: 8m ~ 55m       range: 9m ~ 55m      range: 12m ~ 16m
Table 7. Comparing 2D and 3D approaches. 2D mask is from
FCN on RGB image patch. 3D mask is from PointNet on frustum       Figure 7. Comparisons between 2D and 3D masks. We show a
point cloud. 2D+3D mask is 3D mask generated by PointNet on       typical 2D region proposal from KITTI val set with both 2D (on
point cloud poped up from 2D masked depth map.                    RGB image) and 3D (on frustum point cloud) instance segmenta-
                                                                  tion results. The red numbers denote depth ranges of points.
       frustum rot.   mask centralize   t-net  accuracy
             -              -             -      12.5
            √                                                     5.3. Qualitative Results and Discussion
                            -             -      48.1
                            √
             -                            -      64.6                 In Fig. 6 we visualize representative outputs of our frus-
            √               √
                                          -      71.5             tum PointNet model. We see that for simple cases of non-
            √               √             √
                                                 74.3
                                                                  occluded objects in reasonable distance (so we get enough
Table 8. Effects of point cloud normalization. Metric is 3D box
estimation accuracy with IoU=0.7.                                 number of points), our model outputs remarkably accurate
                                                                  3D instance segmentation mask and 3D bounding boxes.
              loss type        regularization accuracy            Second, we are surprised to find that our model can even
           regression only            -         62.9              predict correctly posed amodal 3D box from partial data
               cls-reg                -         71.8              (e.g. parallel parked cars) with few points. Even humans
        cls-reg (normalized)          -         72.2              find it very difficult to annotate such results with point cloud
        cls-reg (normalized)     corner loss    74.3              data only. Third, in some cases that seem very challenging
Table 9. Effects of 3D box loss formulations. Metric is 3D box    in images with lots of nearby or even overlapping 2D boxes,
estimation accuracy with IoU=0.7.                                 when converted to 3D space, the localization becomes much
                                                                  easier (e.g. P11 in second row third column).
                                                                      On the other hand, we do observe several failure pat-
from 2D masked depth map – also shows slightly worse re-          terns, which indicate possible directions for future efforts.
sults than our main method probably due to the accumulated        The first common mistake is due to inaccurate pose and
error from inaccurate 2D mask predictions.                        size estimation in a sparse point cloud (sometimes less than
                                                                  5 points). We think image features could greatly help esp.
Effects of point cloud normalization. As shown in                 since we have access to high resolution image patch even
Fig. 4, our frustum PointNet takes a few key coordinate           for far-away objects. The second type of challenge is when
transformations to canonicalize the point cloud for more ef-      there are multiple instances from the same category in a
fective learning. Tab. 8 shows how each normalization step        frustum (like two persons standing by). Since our current
helps for 3D detection. We see that both frustum rotation         pipeline assumes a single object of interest in each frus-
(such that frustum points have more similar XYZ distribu-         tum, it may get confused when multiple instances appear
tions) and mask centroid subtraction (such that object points     and thus outputs mixed segmentation results. This prob-
have smaller and more canonical XYZ) are critical. In addi-       lem could potentially be mitigated if we are able to propose
tion, extra alignment of object point cloud to object center      multiple 3D bounding boxes within each frustum. Thirdly,
by T-Net also contributes significantly to the performance.       sometimes our 2D detector misses objects due to dark light-
Effects of regression loss formulation and corner loss.           ing or strong occlusion. Since our frustum proposals are
In Tab. 9 we compare different loss options and show that a       based on region proposal, no 3D object will be detected
combination of “cls-reg” loss (the classification and residual    given no 2D detection. However, our 3D instance segmen-
regression approach for heading and size regression) and a        tation and amodal 3D box estimation PointNets are not re-
regularizing corner loss achieves the best result.                stricted to RGB view proposals. As shown in the supple-
    The naive baseline using regression loss only (first row)     mentary, the same framework can also be extended to 3D
achieves unsatisfactory result because the regression target      regions proposed in bird’s eye view.
is large in range (object size from 0.2m to 5m). In com-          Acknowledgement The authors wish to thank the support
parison, the cls-reg loss and a normalized version (residual      of Nuro Inc., ONR MURI grant N00014-13-1-0341, NSF
normalized by heading bin size or template shape size) of it      grants DMS-1546206 and IIS-1528025, a Samsung GRO
achieve much better performance. At last row we show that         award, and gifts from Adobe, Amazon, and Apple.
a regularizing corner loss further helps optimization.
References                                                           [16] J. Lahoud and B. Ghanem. 2d-driven 3d object detection
                                                                          in rgb-d images. In Proceedings of the IEEE Conference
 [1] Kitti 3d object detection benchmark leader board.                    on Computer Vision and Pattern Recognition, pages 4622–
     http://www.cvlibs.net/datasets/kitti/                                4630, 2017. 2, 7
     eval_object.php?obj_benchmark=3d. Accessed:
                                                                     [17] B. Li. 3d fully convolutional network for vehicle detection
     2017-11-14 12PM. 2
                                                                          in point cloud. arXiv preprint arXiv:1611.08069, 2016. 2, 5,
 [2] Kitti bird’s eye view object detection benchmark leader              6
     board.        http://www.cvlibs.net/datasets/
                                                                     [18] B. Li, T. Zhang, and T. Xia. Vehicle detection from 3d
     kitti/eval_object.php?obj_benchmark=bev.
                                                                          lidar using fully convolutional network. arXiv preprint
     Accessed: 2017-11-14 12PM. 2
                                                                          arXiv:1608.07916, 2016. 2, 13
 [3] M. Abadi, A. Agarwal, P. Barham, E. Brevdo, Z. Chen,
                                                                     [19] Y. Li, S. Pirk, H. Su, C. R. Qi, and L. J. Guibas. Fpnn:
     C. Citro, G. S. Corrado, A. Davis, J. Dean, M. Devin, et al.
                                                                          Field probing neural networks for 3d data. arXiv preprint
     Tensorflow: Large-scale machine learning on heterogeneous
                                                                          arXiv:1605.06240, 2016. 2
     distributed systems. arXiv preprint arXiv:1603.04467, 2016.
     14                                                              [20] T.-Y. Lin, P. Dollár, R. Girshick, K. He, B. Hariharan, and
 [4] X. Chen, K. Kundu, Z. Zhang, H. Ma, S. Fidler, and R. Urta-          S. Belongie. Feature pyramid networks for object detection.
     sun. Monocular 3d object detection for autonomous driving.           arXiv preprint arXiv:1612.03144, 2016. 3, 12
     In Proceedings of the IEEE Conference on Computer Vision        [21] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár.
     and Pattern Recognition, pages 2147–2156, 2016. 2, 6, 11             Focal loss for dense object detection. arXiv preprint
 [5] X. Chen, K. Kundu, Y. Zhu, A. G. Berneshawi, H. Ma, S. Fi-           arXiv:1708.02002, 2017. 12
     dler, and R. Urtasun. 3d object proposals for accurate object   [22] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed, C.-
     class detection. In Advances in Neural Information Process-          Y. Fu, and A. C. Berg. Ssd: Single shot multibox detector.
     ing Systems, pages 424–432, 2015. 6                                  In European conference on computer vision, pages 21–37.
 [6] X. Chen, H. Ma, J. Wan, B. Li, and T. Xia. Multi-view 3d             Springer, 2016. 12
     object detection network for autonomous driving. In IEEE        [23] D. Maturana and S. Scherer. Voxnet: A 3d convolutional
     CVPR, 2017. 2, 5, 6, 11, 12, 13                                      neural network for real-time object recognition. In IEEE/RSJ
 [7] Z. Deng and L. J. Latecki. Amodal detection of 3d objects:           International Conference on Intelligent Robots and Systems,
     Inferring 3d bounding boxes from 2d ones in rgb-depth im-            September 2015. 1, 2
     ages. In Conference on Computer Vision and Pattern Recog-       [24] A. Mousavian, D. Anguelov, J. Flynn, and J. Kosecka. 3d
     nition (CVPR), volume 2, 2017. 2                                     bounding box estimation using deep learning and geometry.
 [8] M. Engelcke, D. Rao, D. Z. Wang, C. H. Tong, and I. Posner.          arXiv preprint arXiv:1612.00496, 2016. 2, 5
     Vote3deep: Fast object detection in 3d point clouds using       [25] C. R. Qi, H. Su, K. Mo, and L. J. Guibas. Pointnet: Deep
     efficient convolutional neural networks. In Robotics and Au-         learning on point sets for 3d classification and segmentation.
     tomation (ICRA), 2017 IEEE International Conference on,              Proc. Computer Vision and Pattern Recognition (CVPR),
     pages 1355–1361. IEEE, 2017. 1, 2                                    IEEE, 2017. 1, 2, 4, 5, 10, 11, 13
 [9] C.-Y. Fu, W. Liu, A. Ranga, A. Tyagi, and A. C. Berg.           [26] C. R. Qi, H. Su, M. Nießner, A. Dai, M. Yan, and L. Guibas.
     Dssd: Deconvolutional single shot detector. arXiv preprint           Volumetric and multi-view cnns for object classification on
     arXiv:1701.06659, 2017. 12                                           3d data. In Proc. Computer Vision and Pattern Recognition
[10] A. Geiger, P. Lenz, C. Stiller, and R. Urtasun. Vision meets         (CVPR), IEEE, 2016. 1, 2
     robotics: The kitti dataset. The International Journal of       [27] C. R. Qi, L. Yi, H. Su, and L. J. Guibas. Pointnet++: Deep
     Robotics Research, 32(11):1231–1237, 2013. 5                         hierarchical feature learning on point sets in a metric space.
[11] A. Geiger, P. Lenz, and R. Urtasun. Are we ready for au-             arXiv preprint arXiv:1706.02413, 2017. 1, 2, 4, 5, 7, 10, 11,
     tonomous driving? the kitti vision benchmark suite. In               13, 14
     Conference on Computer Vision and Pattern Recognition           [28] J. Ren, X. Chen, J. Liu, W. Sun, J. Pang, Q. Yan, Y.-W. Tai,
     (CVPR), 2012. 5                                                      and L. Xu. Accurate single stage detector using recurrent
[12] R. Girshick. Fast r-cnn. In Proceedings of the IEEE inter-           rolling convolution. In CVPR, 2017. 13
     national conference on computer vision, pages 1440–1448,        [29] S. Ren, K. He, R. Girshick, and J. Sun. Faster r-cnn: Towards
     2015. 12                                                             real-time object detection with region proposal networks. In
[13] R. Girshick, J. Donahue, T. Darrell, and J. Malik. Rich fea-         Advances in neural information processing systems, pages
     ture hierarchies for accurate object detection and semantic          91–99, 2015. 2, 5, 12
     segmentation. In Computer Vision and Pattern Recognition        [30] Z. Ren and E. B. Sudderth. Three-dimensional object detec-
     (CVPR), 2014 IEEE Conference on, pages 580–587. IEEE,                tion and layout prediction using clouds of oriented gradients.
     2014. 1                                                              In Proceedings of the IEEE Conference on Computer Vision
[14] K. He, G. Gkioxari, P. Dollár, and R. Girshick. Mask r-cnn.         and Pattern Recognition, pages 1525–1533, 2016. 2, 7, 12
     arXiv preprint arXiv:1703.06870, 2017. 1, 3, 7                  [31] G. Riegler, A. O. Ulusoys, and A. Geiger. Octnet: Learning
[15] M. Jaderberg, K. Simonyan, A. Zisserman, et al. Spatial              deep 3d representations at high resolutions. arXiv preprint
     transformer networks. In NIPS 2015. 4                                arXiv:1611.05009, 2016. 2
[32] K. Simonyan and A. Zisserman. Very deep convolutional            A. Overview
     networks for large-scale image recognition. arXiv preprint
     arXiv:1409.1556, 2014. 7, 12, 13                                     This document provides additional technical details, ex-
[33] S. Song, S. P. Lichtenberg, and J. Xiao. Sun rgb-d: A rgb-d      tra analysis experiments, more quantitative results and qual-
     scene understanding benchmark suite. In Proceedings of the       itative test results to the main paper.
     IEEE Conference on Computer Vision and Pattern Recogni-              In Sec.B we provide more details on network architec-
     tion, pages 567–576, 2015. 1, 5, 7, 12                           tures of PointNets and training parameters while Sec. C ex-
[34] S. Song and J. Xiao. Sliding shapes for 3d object detection      plains more about our 2D detector. Sec. D shows how our
     in depth images. In Computer Vision–ECCV 2014, pages             framework can be extended to bird’s eye view (BV) propos-
     634–651. Springer, 2014. 2                                       als and how combining BV and RGB proposals can further
[35] S. Song and J. Xiao. Deep sliding shapes for amodal 3d ob-       improve detection performance. Then Sec. E presents re-
     ject detection in rgb-d images. In Proceedings of the IEEE       sults from more analysis experiments. At last, Sec. F shows
     Conference on Computer Vision and Pattern Recognition,           more visualization results for 3D detection on SUN-RGBD
     pages 808–816, 2016. 2, 7
                                                                      dataset.
[36] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller.
     Multi-view convolutional neural networks for 3d shape
                                                                      B. Details on Frustum PointNets (Sec 4.2, 4.3)
     recognition. In Proc. ICCV, 2015. 1
[37] C. Sun, A. Shrivastava, S. Singh, and A. Gupta. Revisiting       B.1. Network Architectures
     unreasonable effectiveness of data in deep learning era. arXiv
     preprint arXiv:1707.02968, 1, 2017. 14                               We adopt similar network architectures as in the origi-
[38] D. Z. Wang and I. Posner. Voting for voting in online point      nal works of PointNet [25] and PointNet++ [27] for our v1
     cloud object detection. Proceedings of the Robotics: Science     and v2 models respectively. What is different is that we
     and Systems, Rome, Italy, 1317, 2015. 2                          add an extra link for class one-hot vector such that instance
[39] P.-S. Wang, Y. Liu, Y.-X. Guo, C.-Y. Sun, and X. Tong.           segmentation and bounding box estimation can leverage se-
     O-cnn: Octree-based convolutional neural networks for 3d         mantics predicted from RGB images. The detailed network
     shape analysis. ACM Transactions on Graphics (TOG),              architectures are shown in Fig. 8.
     36(4):72, 2017. 2                                                    For v1 model our architecture involves point embed-
[40] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and         ding layers (as shared MLP on each point independently), a
     J. Xiao. 3d shapenets: A deep representation for volumetric      max pooling layer and per-point classification multi-layer
     shapes. In Proceedings of the IEEE Conference on Computer        perceptron (MLP) based on aggregated information from
     Vision and Pattern Recognition, pages 1912–1920, 2015. 1,
                                                                      global feature and each point as well as an one-hot class
     2
                                                                      vector. Note that we do not use the transformer networks
[41] Y. Xiang, W. Choi, Y. Lin, and S. Savarese. Data-driven 3d
                                                                      as in [25] because frustum points are viewpoint based (not
     voxel patterns for object category recognition. In Proceed-
     ings of the IEEE Conference on Computer Vision and Pattern       complete point cloud as in [25]) and are already normalized
     Recognition, pages 1903–1911, 2015. 2                            by frustum rotation. In addition to XYZ , we also leverage
[42] S.-L. Yu, T. Westfechtel, R. Hamada, K. Ohno, and S. Ta-         LiDAR intensity as a fourth channel.
     dokoro. Vehicle detection and localization on birds eye view         For v2 model we use set abstraction layers for hierarchi-
     elevation images using convolutional neural network. 2017        cal feature learning in point clouds. In addition, because Li-
     IEEE International Symposium on Safety, Security and Res-        DAR point cloud gets increasingly sparse as it gets farther,
     cue Robotics (SSRR), 2017. 5, 6                                  feature learning has to be robust to those density variations.
                                                                      Therefore we used a robust type of set abstraction layers
                                                                      – multi-scale grouping (MSG) layers as introduced in [27]
                                                                      for the segmentation network. With hierarchical features
                                                                      and learned robustness to varying densities, our v2 model
                                                                      shows superior performance than v1 model in both segmen-
                                                                      tation and box estimation.
                                                                      B.2. Data Augmentation and Training
                                                                      Data augmentation Data augmentation plays an impor-
                                                                      tant role in preventing model overfitting. Our augmentation
                                                                      involves two branches: one is 2D box augmentation and the
                                                                      other is frustum point cloud augmentation.
                                                                         We use ground truth 2D boxes to generate frustum point
                                                                      clouds for Frustum PointNets training and augment the 2D
                                                                      boxes by random translation and scaling. Specifically, we
                                                                                                                               v1 3D Instance Segmentation PointNet

                                                                                                                                                                                                                                           output scores
                                                                                     mlp (64,64)                     mlp (64,128,1024)                        max

                                                                                                                                                                                                                                                                              object prob.
                                                             input points
                                                                                                                                                              pool 1024

                                                                                                              nx64

                                                                                                                                                                                                                                                  nx2

                                                                                                                                                                                                                                                             nx1
                                                                                                                                                                                                            n x (1088+k)

                                                                             nx4
                                                                                        shared                             shared           nx1024                                                                                     shared
                                                                                                                                                                        global feature
                                                                                                                                                                                                                           mlp (512,256,128,128,2)

                                                                            T-Net for estimating residual center                                                                                      v1 Amodal 3D Box Estimation PointNet
                                                         mlp (128,256,512)                                       max                                                                                 mlp (128,128,256,512)                 max

                                                                                                                                                          residual center

                                                                                                                                                                                                                                                                                                             box parameters
                                                                                                                                                                                                                                                                                             FCs (512,256,
                                        input points

                                                                                                                                                                                     input points
                                                                                                                 pool                   FCs (256,128,3)                                                                                    pool
                                                                                                                         512        k                                                                                                             512                    k                   3+4NS+2NH)
                                                       mx3

                                                                                                                                                                                                    mx3
                                                                            shared                   mx512                                                                                                    shared        mx512
                                                                                                                     global feature                                                                                                         global feature

                                                                                                                               v2 3D Instance Segmentation PointNet
                                                                                                                                                                                                                           skip link

                                                                                                                                                                                                      skip link
                                                                                                                                                       skip link

                                                                                                                                                                                                                                                                                                                                          object prob.
        input points

                               Set                                                     SA                                        SA                  1024                        k
                       nx4

                                                                                                                                                                                                     FP      32x128

                                                                                                                                                                                                                                                                                                                              nx2

                                                                                                                                                                                                                                                                                                                                    nx1
                             Abstract                  128x320                       (MSG)                   32x640            (SSG)                                                                                        FP         128x128          FP                                   nx128     shared
                             (MSG)                                                                                                               global feature
                                                                                                                            r=inf,                                            mlp (128,128)
                                                                                      np=32, r=[0.4,0.8,1.6]                                                                                                   mlp (128,128)
                                                                                                                            mlp=[128,256,1024]
                                np=128, r=[0.2,0.4,0.8]                                 mlp=[[64,64,128],                                                                                                                               mlp (128,128)
                                   mlp=[[32,32,64],                                      [128,128,256],                                                                                                                                                                                              mlp (128,2)
                               [64,64,128], [64,96,128]]                                 [128,128,256]]

                                                                                                                                v2 Amodal 3D Box Estimation PointNet

                                                                                                                                                                                                                                                             box parameters
                                                                                                                                                                                                                                   FCs (512,256,
                                                                                      input points

                                                                                                                Set                                                                                                  512           3+4NS+2NH)
                                                                                                                                                                                                      SA                       k
                                                                                                      mx4

                                                                                                                                                 SA
                                                                                                             Abstract          128x320                                      32x640                  (SSG)
                                                                                                                                               (SSG)
                                                                                                              (SSG)                                                                                               global feature
                                                                                                                                                  r=0.4,                                            r=inf,
                                                                                                                 r=0.2,                           mlp=[128,128,256]                                 mlp=[256,256,512]
                                                                                                                 mlp=[64,64,128]

Figure 8. Network architectures for Frustum PointNets. v1 models are based on PointNet [25]. v2 models are based on PointNet++ [27]
set abstraction (SA) and feature propagation (FP) layers. The architecture for residual center estimation T-Net is shared for Ours (v1) and
Ours (v2). The colors (blue for segmentaiton nets, red for T-Net and green for box estimation nets) of the network background indicate the
coordinate system of the input point cloud. Segmentation nets operate in frustum coordinate, T-Net processes points in mask coordinate
while box estimation nets take points in object coordinate. The small yellow square (or bar) concatenated with global features is class
one-hot vector that tells the predicted category of the underlying object.

firstly compute the 2D box height (h) and width (w) and                                                                                                                              is pointing down). Thirdly, we perturb the points by shift-
translate the 2D box center by random distances sampled                                                                                                                              ing the entire frustum point cloud in Z-axis direction such
from Uniform[−0.1w, 0.1w] and Uniform[−0.1h, 0.1h] in                                                                                                                                that the depth of points is augmented. Together with all
u,v directions respectively. The height and width are also                                                                                                                           data augmentation, we modify the ground truth labels for
augmented by two random scaling factor sampled from                                                                                                                                  3D mask and headings correspondingly.
Uniform[0.9, 1.1].

   We augment each frustum point cloud by three ways.                                                                                                                                KITTI Training The object detection benchmark in
First, we randomly sample a subset of points from the frus-                                                                                                                          KITTI provides synchronized RGB images and LiDAR
tum point cloud on the fly (1,024 for KITTI and 2,048 for                                                                                                                            point clouds with ground truth amodal 2D and 3D box an-
SUN-RGBD). For object points segmented from our pre-                                                                                                                                 notations for vehicles, pedestrians and cyclists. The training
dicted 3D mask, we randomly sample 512 points from it (if                                                                                                                            set contains 7,481 frames and an undisclosed test set con-
there are less than 512 points we will randomly resample                                                                                                                             tains 7,581 frames. In our own experiments (except those
to make up for the number). Second, we randomly flip the                                                                                                                             for test sets), we follow [4, 6] to split the official train-
frustum point cloud (after rotating the frustum to the center)                                                                                                                       ing set to a train set of 3,717 frames and a val set of 3769
along the YZ plane in camera coordinate (Z is forward, Y                                                                                                                             frames such that frames in train/val sets belong to different
video clips. For models evaluated on the test set we train      layers to convolution layers with 3 × 3 kernel size and stride
our model on our own train/val split where around 80% of        of 2. Then we fine-tune it on ImageNet CLS-LOC dataset
the training data is used such that the model can achieve       for 400k iterations with batch size of 260 on 10 GPUs. The
better generalization by seeing more examples.                  resulting base network architecture has about 66.7% top-1
    To get ground truth for 3D instance segmentation we         classification accuracy on the CLS-LOC validation dataset
simply consider all points that fall into the ground truth 3D   and only needs about 1.2ms to process a 224 × 224 image
bounding box as object points. Although there are some-         on a NVIDIA GTX 1080.
times false labels from ground points or points from other          We then add the feature pyramid layers [20] from
closeby objects (e.g. a person standing by), the auto-labeled   conv3 3, conv4 3, conv5 3, and fc7, which are used to pre-
segmentation ground truth is in general acceptable.             dict region proposals with scales of 16, 32, 64, 128 respec-
    For both of our v1 and v2 models, we use Adam opti-         tively. We also add an extra convolutional layer (conv8)
mizer with starting learning rate 0.001, with step-wise de-     which halves the fc7 feature map size, and use it to predict
cay (by half) in every 60k iterations. For all trainable lay-   proposals with scale of 256. We use 5 different aspect ra-
ers except the last classification or regression ones, we use   tios { 31 , 12 , 1, 2, 3} for all layers except that we ignore { 31 ,
batch normalization with a start decay rate of 0.5 and gradu-   3} for conv3 3. Following SSD, we also use normalization
ally decay the decay rate to 0.99 (step-wise decay with rate    layer on conv3 3, conv4 3, and conv5 3 and initialize the
0.5 in every 20k iterations). We use batch size 32 for v1       norm 40. For Fast R-CNN part, we extract features from
models and batch size 24 for v2 models. All three Point-        conv3 3, conv5 3, and conv8 for each region proposal and
Nets are trained end-to-end.                                    concatenate all the features to predict class scores and fur-
    Trained on a single GTX 1080 GPU, it takes around one       ther adjust the proposals. We train this detector from COCO
day to train a v1 model (all three nets) for 200 epochs while   dataset with 384 × 384 input image and have achieved 35.5
it takes around three days for a v2 model. We picked the        mAP on the COCO minival dataset, with only 10ms pro-
early stopped (200 epochs) snapshot models for evaluation.      cessing time for a 384 × 384 image on a single GPU.
                                                                    Finally, we fine-tune the detector on car, people, and bi-
                                                                cycle from COCO dataset, and have achieved 48.5, 44.1,
SUN-RGBD Training The data set consists of 10,355               and 40.1 for these three classes on COCO. We take this
RGB-D images captured from various depth sensors for in-        model and further fine-tune it on car, pedestrian, and cy-
door scenes (bedrooms, dining rooms etc.). We follow the        clist from KITTI dataset. The final model takes about 30ms
same train/val splits as [33, 30] for experiments. The data     to process a 384 × 1280 image. To increase the recall of the
augmentation and optimization parameters are the same as        detector, we also do detection from the center crop of the
that in KITTI.                                                  image besides the full image, and then merge the detections
   As to auto-labeling of instance segmentation mask, how-      using non-maximum suppression.
ever, data quality is much lower than that in KITTI because         Tab. 10 shows our detector’s AP (2D) on KITTI test set.
of strong occlusions and tight arrangement of objects in in-    Our detector has achieved competitive or better results than
door scenes (see Fig. 11 for some examples). Nonetheless        current leading players on KITTI leader board. We’ve also
we still consider all points within the ground truth boxes as   reported our AP (2D) on val set in Tab. 11 for reference.
object points for our training. For 3D segmentation we get
only a 82.7% accuracy compared to around 90% in KITTI.          D. Bird’s Eye View PointNets (Sec 5.3)
Due to the heavy noise in segmentation mask label, we
choose to only train and evaluate on v1 models that has            In this section, we show that our 3D detection frame-
more strength in global feature learning than v2 ones. For      work can also be extended to using bird’s eye view pro-
future works, we think higher quality in 3D mask labels can     posals, which adds another orthogonal proposal source to
greatly help the instance segmentation network training.        achieve better overall 3D detection performance. We evalu-
                                                                ate the results of car detection using LiDAR bird’s eye view
                                                                only proposals + point net (Ours(BV)), and combine frus-
C. Details on RGB Detector (Sec 4.1)
                                                                tum point net and bird’s eye view point net using 3D non-
   For 2D RGB image detector, we use the encoder-decoder        maximum suppression (NMS) (Ours(Frustum + BV)). The
structure (e.g. DSSD [9], FPN [20]) to generate region pro-     results are shown in Table 12.
posals from multiple feature maps using focal loss [21] and
use Fast R-CNN [12] to predict final 2D detection bounding      Bird’s Eye View Proposal Similar to MV3D [6] we use
boxes from the region proposals.                                point features such as height, intensity and density, and
   To make the detector faster, we take the reduced             train the bird’s eye view 2D proposal net using the standard
VGG [32] base network architecture from SSD [22], sample        Faster-RCNN [29] structure. The net outputs axis-aligned
half of the channels per layer and change all max pooling       2D bounding boxes in the bird’s eye view. In detail, we
                                            Cars                       Pedestrians                     Cyclists
                 Method
                                 Easy Moderate Hard            Easy Moderate Hard           Easy Moderate Hard
                  SWC           90.82       90.05     80.59   87.06       78.65      73.92  86.02       77.58     68.44
                  RRC [28] 90.61            90.22     87.44   84.14       75.33      70.39  84.96       76.47     65.46
                  Ours          90.78       90.00     80.80   87.81       77.25      74.46  84.90       72.25     65.14
Table 10. 2D object detection AP on KITTI test set. Evaluation IoU threshold is 0.7. SWC is the first place winner on KITTI leader board
for pedestrians and cyclists at the time of submission. Our 2D results are based on a CNN model on monocular RGB images.

      Subset                Easy      Moderate     Hard                    Method                     Easy     Moderate      Hard
      AP (2D) for cars      96.48      90.31       87.63                   VeloFCN [18]               15.20     13.66        15.98
    Table 11. Our 2D object detection AP on KITTI val set.                 MV3D [6] (BV+FV)           71.19     56.60        55.30
                                                                           Ours (BV)                  69.50     62.30        59.73
                                                                           Ours (Frustum)             83.76     70.92        63.65
discretize the projected point clouds into 2D grids with res-              Ours (Frustum + BV)        83.76     70.91        67.47
olution of 0.1 meter and with the depth and width range                Table 12. 3D object detection AP on KITTI val set. By using both
0 60 meters, which gives us the 600 × 600 input size. For              proposals from RGB view (frustum) and bird’s eye view (BV), we
each cell, we take the intensity and the density of the high-          see a significant improvement in 3D AP (3.82%) on hard cases
est point and divide the heights into 7 bins with the height           compared with our frustum only method. Ours (Frustum) here is
of the highest point in each bin, which gives us 9 channels            the Ours (v2) in the main paper using PointNet++ architectures.
in total. In Faster R-CNN, we use the VGG-16 [32] with 3
anchor scales (16, 32, 48) and 3 aspect ratios ( 12 , 1, 2). We
train RPN and Fast R-CNN together using the approximate
joint training.
    To combine 3D detection boxes from frustum PointNets
and the bird’s eye view PointNets, we use 3D NMS with
IoU threshold 0.8. We also apply a weight (0.5) to 3D boxes
from BV PointNets since it is a weaker detector compared
with our frustum one.

Bird’s Eye View (BV) PointNets Similar to Frustum
PointNets that take point cloud in frustum, segment point
                                                                       Figure 9. Comparing Frustum PointNets and BV PointNets.
cloud and estimate amodal bounding box, we can apply
                                                                       This is a scene with lots of parallel parking cars (sample 5595
PointNets to points in bird’s eye view regions. Since bird’s           from val set). Left column shows 2D boxes from our 2D detec-
eye view is based on orthogonal projection, the 3D space               tor in image and 3D boxes from our Frustum PointNets in point
specified by a BV 2D box is a 3D cuboid (cut by minimum                cloud. Right column shows 3D boxes from BV PointNets in point
and maximum height) instead of a frustum.                              cloud and the 2D boxes (projected from the 3D detection boxes)
                                                                       in image. Note that 2D detection boxes from Ours (Frustum) that
                                                                       have box height less than 25 pixels or contain no LiDAR points in
Results Tab. 12 (Ours BV) shows the APs we get by using
                                                                       the frustum are not shown in the image.
bird’s eye view proposals only (without and RGB informa-
tion). We compare with two previous LiDAR only methods
(VeloFCN [18] and MV3D (BV+FV) [6]) and show that our
BV proposal based detector greatly outperforms VeloFCN                 E. More Experiments (Sec 5.2)
on all cases and outperforms MV3D (BV+FV) on moderate
and hard cases by a significant margin.                                E.1. Effects of PointNet Architectures
   More importantly, we show in the last row of Tab. 12 that
bird’s eye view and RGB view proposals can be combined                    Table 13 compares PointNet [25] (v1) and Point-
to achieve an even better performance (3.8% AP improve-                Net++ [27] (v2) architectures for instance segmentation and
ment on hard cases). Fig. 9 gives an intuitive explanation             amodal box estimation. The v2 model outperforms v1
of why bird’s eye view proposals could help. In the sample             model on both tasks because 1) v2 model learns hierarchical
frame shown: while our 2D detector misses some highly oc-              features that are richer and more generalizable; 2) v2 model
cluded cars (Fig. 9: left RGB image), bird’s eye view based            uses multi-scale feature learning that adapts to varying point
RPN successfully detects them (Fig. 9: blue arrows in right            densities. Note that the ours (v1) model corresponds to first
LiDAR image).                                                          row of Table 13 while the ours (v2) links to the last row.
          seg net           box net            seg acc.             box acc.   therefore 47MB for v1 model and 50MB for v2 model.
            v1                v1                 90.6                 74.3
            v2                v1                 91.0                 74.7        Model Frustum Proposal 3D Seg Box Est.                Total
            v1                v2                 90.6                 76.0          v1          60 ms           18 ms      10 ms       88 ms
                                                                                    v2          60 ms           88 ms      19 ms      167 ms
            v2                v2                 91.0                 77.1
                                                                               Table 14. 3D detector runtime. Thirty-two region proposals used
Table 13. Effects of PointNet architectures. Metric is 3D box
                                                                               for frustum-based PointNets. 1,024 points are used for instance
estimation accuracy with IoU=0.7.
                                                                               segmentation and 512 points are used for box estimation.

E.2. Effects of Training Data Size
   Recently [37] observed linear improvement in perfor-
                                                                               F. Visualizations for SUN-RGBD (Sec 5.1)
mance of deep learning models with exponential growth of                          In Fig. 11 we visualize some representative detection
data set size. In our Frustum PointNets we observe similar                     results on SUN-RGBD data. We can see that compared
trend (Fig. 10). This trend indicates a promising perfor-                      with KITTI LiDAR data, depth images can be popped up
mance potential of our methods with larger datasets.                           to much more dense point clouds. However even with such
   We train three separate group of Frustum PointNets on                       dense point cloud, strong occlusions of indoor objects as
three sets of training data and then evaluate the model on a                   well as the tight arrangement present new challenges for
fixed validation set (1929 samples). The three data points in                  detection in indoor scenes.
Fig. 10 represent training set sizes of 1388, 2776, 5552 sam-                     In Fig. 12 we report the 3D AP curves of our Frustum
ples (0.185x, 0.371x, 0.742x of the entire trainval set) re-                   PointNets on SUN-RGBD val set. 2D detection APs of our
spectively. We augment the training data such that the total                   RGB detector are also provided in Tab. 11 for reference.
amount of samples are the same for each of the three cases
(20x, 10x and 5x augmentation respectively). The training
set and validation set are chosen such that they don’t share
frames from the same video clips.
                       72
                       71
                       70
                       69
            Accuracy

                       68
                       67
                       66
                       65
                       64
                            1388               2776                 5552
                                   Training Data Size (log scale)

Figure 10. Effects of training data size. Evaluation metric is
3D box estimation accuracy (IoU threshold 0.7). We see a clear
trend of linear improvement in accuracy with exponential growth
of training data size.

E.3. Runtime and Model Size
   In Table 14, we show decomposed runtime cost (infer-
ence time) for our frustum PointNets (v1 and v2). The eval-
uation is based on TensorFlow [3] with a NVIDIA GTX
1080 and a single CPU core. While for v1 model frus-
tum proposal (with CNN and backprojection) takes the ma-
jority time, for v2 model since a PointNet++ [27] model
with multi-scale grouping is used, computation bottleneck
shifts to instance segmentation. Note that we merge batch
normalization and FC/convolution layers for faster infer-
ence (since they are both linear operation with multiply and
sum), which results in close to 50% speedup for inference.
   CNN model has size 28 MB. v1 PointNets have size
19MB. v2 PointNets have size 22MB. The total size is
   (2D detections)
       Image
   (3D detections)
     Point cloud
   (3D GT boxes)
     Point cloud

Figure 11. Visualization of Frustum PointNets results on SUN-RGBD val set. First row: RGB image with 2D detection boxes. Second
row: point cloud popped up from depth map and predicted amodal 3D bounding boxes (the numbers beside boxes correspond to 2D boxes
on images). Green boxes are true positive. Red boxes are false positives. False negatives are not visualized. Third row: point cloud popped
up from depth map and ground truth amodal 3D bounding boxes.

             Category   bathtub   bed     bookshelf    chair    desk    dresser     nightstand     sofa    table    toilet   mean
             AP (2D)     81.3     56.7      67.2       64.1     77.8     33.3          37.2        57.4    49.9      43.5    50.3
             AP (3D)     43.3     81.1      33.3       64.2     24.7     32.0          58.1        61.1    51.1      90.9    54.0
Table 15. 2D and 3D object detection AP on SUN-RGBD val set. 2D IoU threshold is 0.5. Note that on some categories we get higher
3D AP (displayed in the table as well, the same results as in main paper) than 2D AP because our network is able to recover 3D geometry
from very partial scan and is also due to a more loose 3D IoU threshold (0.25) in SUN-RGBD 3D AP evaluation.

                           Figure 12. Precision recall (PR) curves for 3D object detection on SUN-RGBD val set.
