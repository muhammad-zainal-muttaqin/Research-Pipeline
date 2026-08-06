---
source_id: 098
bibtex_key: liu2023bevfusion
title: BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's-Eye View Representation
year: 2023 (versi awal diunggah 2022)
domain_theme: Deteksi 3D
verified_pdf: 98_BEVFusion.pdf
char_count: 61841
---

BEVFusion: Multi-Task Multi-Sensor Fusion
                                                                     with Unified Bird’s-Eye View Representation
                                         Zhijian Liu∗,1 , Haotian Tang∗,1 , Alexander Amini1 , Xinyu Yang1 , Huizi Mao2 , Daniela L. Rus1 , Song Han1

                                                                                                                                                                         The intersection region is not covered.
                                           Abstract— Multi-sensor fusion is essential for an accurate
                                        and reliable autonomous driving system. Recent approaches
                                        are based on point-level fusion: augmenting the LiDAR point
                                                                                                                       close (red) and faraway (blue) points in 3D
                                        cloud with camera features. However, the camera-to-LiDAR                                   are neighbors in 2D
                                        projection throws away the semantic density of camera features,
                                        hindering the effectiveness of such methods, especially for
arXiv:2205.13542v3 [cs.CV] 1 Sep 2024

                                                                                                                       (a) To Camera: geometric-lossy                    (b) To LiDAR: semantic-lossy
                                        semantic-oriented tasks (such as 3D scene segmentation). In

                                                                                                                              Camera features
                                        this paper, we propose BEVFusion, an efficient and generic                                              BEV features (camera)     BEV features (LiDAR)

                                                                                                                                                                                                          LiDAR features
                                        multi-task multi-sensor fusion framework. It unifies multi-modal
                                        features in the shared bird’s-eye view (BEV) representation
                                        space, which nicely preserves both geometric and semantic
                                        information. To achieve this, we diagnose and lift the key
                                        efficiency bottlenecks in the view transformation with optimized
                                        BEV pooling, reducing latency by more than 40×. BEVFusion                                                (c) Shared       BEVFusion         space
                                                                                                                                                                     

                                        is fundamentally task-agnostic and seamlessly supports different
                                        3D perception tasks with almost no architectural changes. It                   Fig. 1: BEVFusion unifies camera and LiDAR features in a
                                        establishes the new state of the art on the nuScenes benchmark,                shared BEV space instead of mapping one modality to the
                                        achieving 1.3% higher mAP and NDS on 3D object detection and                   other. It preserves camera’s semantic density and LiDAR’s
                                        13.6% higher mIoU on BEV map segmentation, with 1.9× lower
                                        computation cost. Code to reproduce our results is available at
                                                                                                                       geometric structure.
                                        https://github.com/mit-han-lab/bevfusion.                                      3D bounding boxes. Although they have demonstrated remark-
                                                                                                                       able performance on large-scale detection benchmarks, these
                                                                 I. I NTRODUCTION
                                                                                                                       point-level fusion methods barely work on semantic-oriented
                                           Autonomous driving systems are equipped with diverse                        tasks, such as BEV map segmentation [5], [6], [7], [8]. This
                                        sensors. For instance, Waymo’s self-driving vehicles have 29                   is because the camera-to-LiDAR projection is semantically
                                        cameras, 6 radars, and 5 LiDARs. Different sensors provide                     lossy (see Figure 1b): for a typical 32-beam LiDAR scanner,
                                        complementary signals: e.g., cameras capture rich semantic                     only 5% camera features will be matched to a LiDAR point
                                        information, LiDARs provide accurate spatial information,                      while all others will be dropped. Such density differences will
                                        while radars offer instant velocity estimation. Thus, multi-                   become even more drastic for sparser LiDARs (or radars).
                                        sensor fusion is essential for accurate and reliable perception.                  In this paper, we propose BEVFusion to unify multi-modal
                                           Data from different sensors are expressed in fundamentally                  features in a shared bird’s-eye view (BEV) representation
                                        different modalities: e.g., cameras capture data in perspective                space for task-agnostic learning. We maintain both geometric
                                        view and LiDAR in 3D view. To resolve this view discrepancy,                   structure and semantic density (see Figure 1c) and naturally
                                        we have to find a unified representation that is suitable for                  support most 3D perception tasks (since their output space can
                                        multi-task multi-modal feature fusion. Due to the tremendous                   be naturally captured in BEV). While converting all features
                                        success in 2D perception, the natural idea is to project                       to BEV, we identify the major prohibitive efficiency bottleneck
                                        the LiDAR point cloud onto the camera and process the                          in the view transformation: i.e., the BEV pooling operation
                                        RGB-D data with 2D CNNs. However, this LiDAR-to-                               alone takes more than 80% of the model’s runtime. Then, we
                                        camera projection introduces severe geometric distortion                       propose a specialized kernel with precomputation and interval
                                        (see Figure 1a), which makes it less effective for geometric-                  reduction to eliminate this bottleneck, achieving more than
                                        oriented tasks, such as 3D object recognition.                                 40× speedup. Finally, we apply the fully-convolutional BEV
                                           Recent sensor fusion methods follow the other direction.                    encoder to fuse the unified BEV features and append a few
                                        They augment the LiDAR point cloud with semantic labels [1],                   task-specific heads to support different target tasks.
                                        CNN features [2], [3] or virtual points from 2D images [4],                       BEVFusion sets the new state-of-the-art 3D object detection
                                        and then apply an existing LiDAR-based detector to predict                     performance on both nuScenes and Waymo benchmarks. It
                                                                                                                       outperforms all published methods with or without test-time
                                          ∗ The first two authors contributed equally and are listed alphabetically.
                                        This work was supported by MIT-IBM Watson AI Lab, National Science             augmentation and model ensemble. BEVFusion demonstrates
                                        Foundation, Hyundai Motor, Qualcomm, NVIDIA and Apple. Zhijian Liu             even more significant improvements on BEV map segmenta-
                                        was partially supported by the Qualcomm Innovation Fellowship.                 tion. It achieves 6% higher mIoU than camera-only models
                                          1 Z. Liu, H. Tang, A. Amini, X. Yang, D. Rus, and S. Han are with
                                        Massachusetts Institute of Technology, Cambridge, MA 02139, USA.               and 13.6% higher mIoU than LiDAR-only models, while
                                          2 H. Mao is with OmniML, San Jose, CA 95131, USA.                            existing fusion methods hardly work. Moreover, BEVFusion
                                                                                                                               Task-Speci c Heads
                                                                                 Camera Feat
                                                                                  (in BEV)

                                          Camer     Camer      Camera-to-BE                                                   BEV Map Segmentation
                                          Encoder   Features   View Transform
Multi-View RGB Images                                                                                                                  …

                                                                                                    BE        Fused BE
                                                                                                   Encoder     Features

                                          LiDA      LiDA            Flatte       LiDAR Feat
                                                                                                                               3D Object Detection
                                          Encoder   Features    (along z-axis)    (in BEV)
   LiDAR Point Cloud
  V

       n

       R

       R

            a

            a

                 V

                      fi
                           .

                            .

                                 V

Fig. 2: BEVFusion extracts features from multi-modal inputs and converts them into a shared bird’s-eye view (BEV) space
efficiently using view transformations. It fuses the unified BEV features with a fully-convolutional BEV encoder and supports
different tasks with task-specific heads.

is highly efficient, delivering all these results with 1.9× lower                   Multi-Sensor Fusion. Recently, multi-sensor fusion arouses
computation cost.                                                                   significant interest among the 3D detection community.
   While point-level fusion has been the go-to choice over the                      Existing approaches can be classified into proposal-level
past three years, BEVFusion provides a fresh perspective to                         and point-level fusion methods. Early approach MV3D [44]
the field of multi-sensor fusion by rethinking “Is LiDAR space                      creates object proposals in 3D and projects the proposals to
the right place to perform sensor fusion?”. It showcases the                        images to extract RoI features. [45], [46], [47] all lift image
superior performance of an alternative paradigm that has been                       proposals into a 3D frustum. Recent work FUTR3D [48]
previously overlooked. Simplicity is also its key strength. We                      and TransFusion [49] define object queries in the 3D space
hope this work will serve as a simple yet strong baseline                           and fuses image features onto these proposals. All proposal-
for future sensor fusion research and inspire the researchers                       level fusion methods are object-centric and cannot trivially
to rethink the design and paradigm for generic multi-task                           generalize to other tasks such as BEV map segmentation.
multi-sensor fusion.                                                                Point-level fusion methods, on the other hand, usually paint
                                                                                    image semantic features onto foreground LiDAR points
                                      II. R ELATED W ORK                            and perform LiDAR-based detection on the decorated point
                                                                                    cloud inputs. As such, they are both object-centric and
LiDAR-Based 3D Perception. Researchers have designed                                geometric-centric. Among these methods, [1], [2], [4], [50],
single-stage 3D object detectors [9], [10], [11], [12], [13], [14]                  [51] are (LiDAR) input-level decoration, while DCF [52] and
that extract flattened point cloud features using PointNets [15]                    DeepFusion [3] are feature-level decoration.
or SparseConvNet [16] and perform detection in the BEV                                 In contrast to all existing methods, BEVFusion performs
space. Later, [17], [18], [19], [20], [21], [22], [23] explore                      sensor fusion in a shared BEV space and treats foreground
anchor-free single-stage 3D object detection. Another stream                        and background, geometric and semantic information equally.
of research [24], [25], [26], [27], [28], [29] focuses on two-                      It is a generic multi-task multi-sensor perception framework.
stage object detector design, which adds an RCNN network
                                                                                                             III. M ETHOD
to existing one-stage object detectors.
                                                                                       BEVFusion, as shown in Figure 2, focuses on multi-
Camera-Based 3D Perception. Due to the high cost of                                 sensor fusion (i.e., multi-view cameras and LiDAR) for multi-
LiDAR sensors, researchers spend significant efforts on                             task 3D perception (i.e., detection and segmentation). Given
camera-only 3D perception. FCOS3D [30] extends an image                             different sensory inputs, we first apply modality-specific
detector [31] with additional 3D regression branches, which                         encoders to extract their features. We transform multi-modal
is later improved by [32], [33] in depth modeling. Instead                          features into a unified BEV representation that preserves
of performing object detection in the perspective view, [34],                       both geometric and semantic information. We identify the
[35] design a DETR [36], [37]-based detection head with                             efficiency bottleneck of the view transformation and accelerate
learnable object queries in the 3D space. Inspired by the                           BEV pooling with precomputation and interval reduction. We
design of LiDAR-based detectors, another type of camera-                            then apply the convolution-based BEV encoder to the unified
only 3D perception models explicitly converts the camera                            BEV features to alleviate the local misalignment between
features from perspective view to the bird’s-eye view using                         different features. Finally, we append a few task-specific
a view transformer [5], [38], [39], [6]. BEVDet [40] and                            heads to support different 3D tasks.
M2 BEV [41] extends LSS [6] and OFT [38] to 3D object
detection and CaDDN [42] adds explicit depth estimation                             A. Unified Representation
supervision to the view transformer. Recent research [43], [8]                         Different features can exist in different views. For in-
also studies view transformation with multi-head attention.                         stance, camera features are in the perspective view, while
                                                                                                         Depth         Grid Association     Feat. Aggregation
                                                       Index 0       0 1 1 1 2 2 2
         0.1                                           Value 1       3 7 -1 -2 4 -3 6
                                                                                                                              Interval Reduction: 22.1×
                               0.1            0.1
            0.5                                                   Pre x Sum Reduction (LSS)
                   0.2
                               0.1           0.1                                                                       Precomputation: 1.9×
                               0.5                  Pref. Sum 1      4 11 10 8 12 9 15                   0            20        40      log scale     500ms
                     0.2                   0.2
                               0.3                   Results         4           4           7                 (c) Improvement breakdown
                                         0.6
                                     B                             Interval Reduction (Ours)
                           C                                                                                 LSS:
                                                                                                                    136.8ms
                                                                                                                               512.1ms
                                                                                                                                             2127.3ms
                                         A                      Thread 1   Thread 2    Thread 3

                                                      Results      4          4           7                  Ours:             12.0ms
                                                                                                                 4.8ms                        45.1ms

                   (a) Camera-to-BEV                                   : Stored to DRAM (Slow)
                                                                                                               1/16 FPN       1/8 FPN       1/4 FPN
                      transformation                              (b) Ef cient BEV pooling                                (d) Scalability
         fi
              fi
Fig. 3: Camera-to-BEV transformation (a) is the key step to perform sensor fusion in the unified BEV space. Existing
implementation is extremely slow and takes up to 2s for a single scene. We propose efficient BEV pooling (b) using interval
reduction and fast grid association with precomputation, bringing about 40× speedup to view transformation (c, d).

LiDAR/radar features are typically in the 3D/bird’s-eye                               dense BEV feature map in Figure 1c that retains full semantic
view. Even for camera features, each one of them has a                                information from the cameras.
distinct viewing angle (i.e., front, back, left, right). This view                    B. Efficient Camera-to-BEV Transformation
discrepancy makes the feature fusion difficult since the same
element in different feature tensors might correspond to very                            Camera-to-BEV transformation is non-trivial because the
different spatial locations (and the naı̈ve elementwise feature                       depth associated with each camera feature pixel is inherently
fusion will not work in this case). Thus, it is crucial to find                       ambiguous. Following LSS [6], we explicitly predict the
a shared representation, such that (1) all sensor features can                        discrete depth distribution of each pixel. We then scatter each
be easily converted to it without information loss, and (2) it                        feature pixel into D discrete points along the camera ray and
is suitable for different types of tasks.                                             rescale the associated features by their corresponding depth
                                                                                      probabilities (Figure 3a). This generates a camera feature
To Camera. Motivated by RGB-D data, one choice is to                                  point cloud of size N HW D, where N is the number of
project the LiDAR point cloud to the camera plane and                                 cameras and (H, W ) is the camera feature map size. Such
render the 2.5D sparse depth. However, this conversion is                             3D feature point cloud is quantized along the x, y axes with a
geometrically lossy. Two neighbors on the depth map can                               step size of r (e.g., 0.4m). We use the BEV pooling operation
be far away from each other in the 3D space. This makes                               to aggregate all features within each r × r BEV grid and
the camera view less effective for tasks that focus on the                            flatten the features along the z-axis.
object/scene geometry, such as 3D object detection.                                      Though simple, BEV pooling is surprisingly inefficient
                                                                                      and slow, taking more than 500ms on an RTX 3090 GPU
To LiDAR. Most state-of-the-art sensor fusion methods [1],
                                                                                      (while the rest of our model only takes around 100ms). This
[4], [3] decorate LiDAR points with their corresponding
                                                                                      is because the camera feature point cloud is very large: for
camera features (e.g., semantic labels, CNN features or
                                                                                      a typical workload* , there could be around 2 million points
virtual points). However, this camera-to-LiDAR projection
                                                                                      generated for each frame, two orders of magnitudes denser
is semantically lossy. Camera and LiDAR features have
                                                                                      than a LiDAR feature point cloud. To lift this efficiency
drastically different densities, resulting in only less than 5%
                                                                                      bottleneck, we propose to optimize the BEV pooling with
of camera features being matched to a LiDAR point (for a
                                                                                      precomputation and interval reduction.
32-channel LiDAR scanner). Giving up the semantic density
of camera features severely hurts the model’s performance                             Precomputation. The first step of BEV pooling is to
on semantic-oriented tasks (such as BEV map segmentation).                            associate each point in the camera feature point cloud with a
Similar drawbacks also apply to more recent fusion methods                            BEV grid. Different from LiDAR point clouds, the coordinates
in the latent space (e.g., object query) [48], [49].                                  of the camera feature point cloud are fixed (as long as the
                                                                                      camera intrinsics and extrinsics stay the same, which is
To Bird’s-Eye View. We adopt the bird’s-eye view (BEV)                                usually the case after proper calibration). Motivated by this,
as the unified representation for fusion. This view is friendly                       we precompute the 3D coordinate and the BEV grid index of
to almost all perception tasks since the output space is also                         each point. We also sort all points according to grid indices
in BEV. More importantly, the transformation to BEV keeps                             and record the rank of each point. During inference, we only
both geometric structure (from LiDAR features) and semantic                           need to reorder all feature points based on the precomputed
density (from camera features). On the one hand, the LiDAR-                           ranks. This caching mechanism can reduce the latency of
to-BEV projection flattens the sparse LiDAR features along                            grid association from 17ms to 4ms.
the height dimension, thus does not create geometric distortion
                                                                                        * N = 6, (H, W ) = (32, 88), and D = (60 − 1)/0.5 = 118. This
in Figure 1a. On the other hand, camera-to-BEV projection
                                                                                      corresponds to six multi-view cameras, each associated with a 32×88 camera
casts each camera feature pixel back into a ray in the 3D                             feature map (which is downsampled from a 256×704 image by 8×). The
space (detailed in the next section), which can result in a                           depth is discretized into [1, 60] meters with a step size of 0.5 meter.
Tab. I: BEVFusion achieves state-of-the-art 3D object detection performance on nuScenes (val and test) without bells and
whistles. It breaks the convention of decorating camera features onto the LiDAR point cloud and delivers at least 1.3% higher
mAP and NDS with 1.5-2× lower computation cost. (∗ : our re-implementation; † : with test-time augmentation)

                             Modality     mAP (test)    NDS (test)      mAP (val)     NDS (val)      MACs (G)          Latency (ms)
      2
    M BEV [41]                  C            42.9           47.4           41.7             47.0            –               –
    BEVFormer [43]              C            44.5           53.5           41.6             51.7            –               –
    PointPillars [10]           L             –              –             52.3             61.3            65.5           34.4
    SECOND [11]                 L            52.8           63.3           52.6             63.0            85.0           69.8
    CenterPoint [17]            L            60.3           67.3           59.6             66.8           153.5           80.7
    PointPainting [1]          C+L            –              –             65.8∗            69.6∗      370.0              185.8
    PointAugmenting [2]        C+L           66.8†          71.0†           –                –         408.5              234.4
    MVP [4]                    C+L           66.4           70.5           66.1∗            70.0∗      371.7              187.1
    FusionPainting [50]        C+L           68.1           71.6           66.5             70.7          –                 –
    AutoAlign [51]             C+L            –              –             66.6             71.1          –                 –
    FUTR3D [48]                C+L            –              –             64.5             68.3       1069.0             321.4
    TransFusion [49]           C+L           68.9           71.6           67.5             71.3        485.8             156.6
    BEVFusion (Ours)           C+L           70.2           72.9           68.5             71.4       253.2              119.2

Interval Reduction. After grid association, all points               Tab. II: BEVFusion achieves state-of-the-art 3D object
within the same BEV grid will be consecutive in the tensor           detection performance among all submissions on Waymo
representation. The next step of BEV pooling is to aggregate         open dataset (test). († : with test-time augmentation, ‡ : with
the features within each BEV grid by some symmetric                  both test-time augmentation and model ensemble)
function (e.g., mean, max, and sum). As in Figure 3b, existing                              Frames mAP/L1 mAPH/L1 mAP/L2 mAPH/L2
implementation [6] first computes the prefix sum over all
                                                                      AFDetV2-Ens [18]‡        3    84.1        82.6    79.0      77.6
points and then subtracts the values at the boundaries where          InceptionLiDAR          10    83.8        82.5    79.2      77.8
indices change. However, the prefix sum operation requires            3DAL-Ens [20]            5    84.6        83.1    79.7      78.2
tree reduction on the GPU and produces many unused partial            DeepFusion-Ens [3]‡      5    84.4        83.2    79.5      78.4
                                                                      MT-Net‡ [55]             3    84.7        83.2    79.9      78.5
sums (since we only need those values on the boundaries),             MT3D                     4    85.0        83.7    80.1      78.7
both of which are inefficient. To accelerate feature aggregation,     LIVOX-Detection          7    84.8        83.5    80.2      79.0
we implement a specialized GPU kernel that parallelizes               MPPNet-Ens‡ [56]        16    85.0        83.7    80.5      79.1
                                                                      3DAM-Ens                 5    85.3        83.8    80.7      79.2
directly over BEV grids: we assign a GPU thread to each               BEVFusion (Ours)†        3    85.7        84.4    80.8      79.5
grid that calculates its interval sum and writes the result back.
This kernel removes the dependency between outputs (thus             blocks) to compensate for such local misalignments. Our
does not require multi-level tree reduction) and avoids writing      method could potentially benefit from more accurate depth
the partial sums to the DRAM, reducing the latency of feature        estimation (e.g., supervising the view transformer with ground-
aggregation from 500ms to 2ms (Figure 3c).                           truth depth [42], [53]), which we leave for future work.
Takeaways. The camera-to-BEV transformation is 40×                   D. Multi-Task Heads
faster with our optimized BEV pooling: the latency is
reduced from more than 500ms to 12ms (only 10% of our                   We apply multiple task-specific heads to the fused BEV
model’s end-to-end runtime) and scales well across different         feature map. Our method is applicable to most 3D perception
feature resolutions (Figure 3d). This is a key enabler for           tasks. For 3D object detection, we follow [17], [49] to use
unifying multi-modal sensory features in the shared BEV              a class-specific center heatmap head to predict the center
representation. Two concurrent works of ours also identify           location of all objects and a few regression heads to estimate
this efficiency bottleneck in the camera-only 3D detection.          the object size, rotation, and velocity. For map segmentation,
They approximate the view transformer by assuming uniform            different map categories may overlap (e.g., crosswalk is
depth distribution [41] or truncating the points within each         a subset of drivable space). Therefore, we formulate this
BEV grid [40]. In contrast, our techniques are exact without         problem as multiple binary semantic segmentation, one for
any approximation, while still being faster.                         each class. We follow CVT [8] to train the segmentation head
                                                                     with the standard focal loss [54].
C. Fully-Convolutional Fusion
   With all sensory features converted to the shared BEV                                     IV. E XPERIMENTS
representation, we can easily fuse them together with an                We evaluate BEVFusion for camera-LiDAR fusion on 3D
elementwise operator (such as concatenation). Though in the          object detection and BEV map segmentation, covering both
same space, LiDAR BEV features and camera BEV features               geometric- and semantic-oriented tasks. Our framework can
can still be spatially misaligned to some extent due to the          be easily extended to support other types of sensors (such
inaccurate depth in the view transformer. To this end, we            as radars and event-based cameras) and other 3D perception
apply a convolution-based BEV encoder (with a few residual           tasks (such as 3D object tracking and motion forecasting).
Tab. III: BEVFusion outperforms the state-of-the-art multi-sensor fusion methods by 13.6% on BEV map segmentation on
nuScenes (val) with consistent improvements across different categories.

                               Modality           Drivable          Ped. Cross.         Walkway         Stop Line             Carpark       Divider          Mean
    OFT [38]                       C                  74.0             35.3                45.9            27.5                 35.9          33.9           42.1
    LSS [6]                        C                  75.4             38.8                46.3            30.3                 39.1          36.5           44.4
    CVT [8]                        C                  74.3             36.8                39.9            25.8                 35.0          29.4           40.2
    M2 BEV [41]                    C                  77.2              –                   –               –                    –            40.5            –
    BEVFusion (Ours)               C                  81.7             54.8                58.4            47.4                 50.7          46.4           56.6
    PointPillars [10]               L                 72.0             43.1                53.1            29.7                 27.7          37.5           43.8
    CenterPoint [17]                L                 75.6             48.4                57.5            36.5                 31.7          41.9           48.6
    PointPainting [1]              C+L                75.9             48.5                57.1            36.9                 34.5          41.9           49.1
    MVP [4]                        C+L                76.1             48.7                57.0            36.9                 33.0          42.2           49.0
    BEVFusion (Ours)               C+L                85.5             60.5                67.6            52.0                 57.0          53.7           62.7

Tab. IV: BEVFusion is robust under different lighting and weather conditions, significantly boosting the performance
single-modality models under challenging rainy(+10.7) and nighttime(+12.8) scenes.
                                                  Sunny                           Rainy                               Day                            Night
                        Modality          mAP                mIoU          mAP              mIoU          mAP                 mIoU          mAP              mIoU
  CenterPoint [17]         L               62.9              50.7          59.2              42.3          62.8                48.9          35.4             37.0
  BEVFormer [43]           C               41.0               –            44.0               –            41.9                 –            21.2              –
  BEVFusion                C                –                59.0           –                50.5           –                  57.4           –               30.8
  MVP                    C+L            65.9 (+3.0)     51.0 (+0.3)     66.3 (+7.1)       42.9 (+0.6)   66.3 (+3.5)         49.2 (+0.3)   38.4 (+3.0)    37.5 (+0.5)
  BEVFusion              C+L            68.2 (+5.3)     65.6 (+6.6)     69.9 (+10.7)      55.9 (+5.4)   68.5 (+5.7)         63.1 (+5.7)   42.8 (+7.4)    43.6 (+12.8)

Model. We use Swin-T [57] as our image backbone and                                    methods PointPainting [1] and MVP [4] with 1.6× speedup,
VoxelNet [11] as our LiDAR backbone. We apply FPN [58]                                 1.5× MACs reduction and 3.8% higher mAP on the test
to fuse multi-scale camera features to produce a feature                               set. We argue that the efficiency gain of BEVFusion comes
map of 1/8 input size. We downsample camera images to                                  from the fact that we choose the BEV space as the shared
256×704 and voxelize the LiDAR point cloud with 0.075m                                 fusion space, which fully utilizes all camera features instead
(for detection) and 0.1m (for segmentation). As detection and                          of just a 5% sparse set. Consequently, BEVFusion can achieve
segmentation tasks require BEV feature maps with different                             the same performance with much smaller resolution for the
spatial ranges and sizes, we apply grid sampling with bilinear                         camera inputs, resulting in significantly lower MACs. Com-
interpolation before each task-specific head to explicitly                             bined with the efficient BEV pooling operator in Section III-B,
transform between different BEV feature maps.                                          BEVFusion transfers MACs reduction into measured speedup.
Dataset. We evaluate our method on nuScenes [59] and                                      BEVFusion also achieves state-of-the-art performance
Waymo [60], which are large-scale datasets for 3D perception                           on the Waymo open dataset [60] (Table II). BEVFusion
with >40k annotated scenes. Each sample in both datasets are                           outperforms the previous state-of-the-art multi-modal detector,
equipped with both LiDAR and surrounding camera inputs.                                DeepFusion [3] with 60% of input frames. Furthermore,
                                                                                       DeepFusion ensembles 25 models evaluated with test-time
A. 3D Object Detection                                                                 augmentation, while we deliver better performance by apply-
                                                                                       ing test-time augmentation to a single BEVFusion model.
   We first experiment on the geometric-centric 3D object
detection benchmark, where BEVFusion achieves superior                                 B. BEV Map Segmentation
performance with lower computation cost and measured                                      We further compare BEVFusion with state-of-the-art mod-
latency. We use the mean average precision (mAP) across 10                             els on the semantic-centric BEV map segmentation task,
foreground classes and the nuScenes detection score (NDS) as                           where BEVFusion achieves an even larger performance boost.
our detection metrics. We also measure the single-inference                            We report the Intersection-over-Union (IoU) on 6 background
#MACs and latency on an RTX3090 GPU for all open-                                      classes and the class-averaged mean IoU as our evaluation
source methods. We use a single model without any test-time                            metric. As different classes may have overlappings (e.g.
augmentation for both val and test results.                                            car-parking area is also drivable), we evaluate the binary
   As in Table I, BEVFusion achieves state-of-the-art results                          segmentation performance for each class separately and select
on the nuScenes detection benchmark, with close-to-real-time                           the highest IoU across different thresholds [8]. For each frame,
(8.4 FPS) inference speed on a desktop GPU. Compared                                   we only perform the evaluation in the [-50m, 50m]×[-50m,
with TransFusion [49], BEVFusion offers 1.3% improvement                               50m] region around the ego car following [6], [8], [41], [43].
in test split mAP and NDS, while significantly reduces                                    We report the BEV map segmentation results in Table III. In
the MACs by 1.9× and measured latency by 1.3×. It also                                 contrast to 3D object detection which is a geometric-oriented
compares favorably against representative point-level fusion                           task, map segmentation is semantic-oriented. As a result,
           LiDAR-only     MVP       BEVFusion                    LiDAR-only               BEVFusion                       CenterPoint           MVP       BEVFusion
      62     61.9                                      80             78.5
                                                                                                                   65                                          64.4
                                                                                                                                        63.2
                                                                                                                                                             63.8
             61.0                                              77.1
      60                                               72                                                          59                           61.4
            5.8%                                                                   64.6                                                                      58.5
            better
      58                                57.9           64                                                          53    52.0                   54.9
mAP

                                                                                                             NDS
                                                 mAP
             56.1                                                            60.4
      56                                4.2%                                                                       47   +12%
                                                       56                                         50.5                                         MACs (G) @ 16 beam
                                        better                  Improvements
                                                                                                                                          CenterPoint      75.3
                                                              0-20m          1.4                                         39.8
      54                                               48                                                          41                           MVP        292.7
                                        53.7                  20-30m         4.2
                                                                                                                         35.8             BEVFusion        186.1
                                        53.1                  >30m           7.3           43.2
      52                                                                                                           35
                                size ≥ 4m
                                                       40
             size < 4m                                         0-20m          20-30m              >30m                    1 beam           4 beam         16 beam

           (a) Different object sizes                       (b) Different object distances                              (c) Different LiDAR sparsity
Fig. 4: BEVFusion outperforms state-of-the-art single- and multi-modality detectors under different LiDAR sparsity, object
sizes and object distances, especially under more challenging settings (i.e., sparser point clouds, small/distant objects).
our camera-only BEVFusion model outperforms LiDAR-only                              its LiDAR-only counterpart for both small and large objects,
baselines by 8-13%. This observation is the exact opposite                          while MVP has only negligible improvements for objects
of results in Table I, where state-of-the-art camera-only                           larger than 4m. This is because larger objects are typically
3D detectors got outperformed by LiDAR-only detectors                               much denser, benefiting less from augmented multi-modal
by almost 20 mAP. Our camera-only model boosts the                                  virtual points (MVPs). Additionally, BEVFusion yields greater
performance of existing monocular BEV map segmentation                              improvements to the LiDAR-only detector for smaller objects
methods by at least 12%. In the multi-modality setting, we                          (in Figure 4a) and more distant objects (in Figure 4b), both of
further improve the performance of the monocular BEVFusion                          which are inadequately captured by LiDAR and can therefore
by 6 mIoU and achieved >13% improvement over state-of-                              derive more benefit from the dense camera information.
the-art sensor fusion methods [1], [4]. This is because both                        Sparser LiDARs. We finally demonstrate the performance of
baseline methods are object-centric and geometric-oriented.                         CenterPoint [17] (LiDAR-only), MVP [4] (multi-modal), and
PointPainting [1] only decorates the foreground LiDAR                               our BEVFusion under different LiDAR sparsities in Figure 4c.
points and MVP only densifies foreground 3D objects. Both                           BEVFusion consistently outperforms MVP across all sparsity
approaches are not helpful for segmenting map components.                           levels with a 1.6× reduction in #MACs and achieves a 12%
Worse still, both methods assume that LiDAR should be the                           improvement in the 1-beam LiDAR scenario. MVP decorates
more effective modality in sensor fusion, which is not true                         the point cloud and directly applies CenterPoint on the painted
according to our observations in Table III.                                         and densified LiDAR input. As a result, it naturally requires
                             V. A NALYSIS                                           the LiDAR-only detector (CenterPoint) to perform well, which
                                                                                    is not valid under sparse LiDAR settings (i.e., 35.8 NDS with
   We present in-depth analyses of BEVFusion over single-                           1-beam input in Figure 4c). In contrast, BEVFusion integrates
modality models and state-of-the-art multi-modality models.                         multi-sensor information in the shared BEV space and does
Weather and Lighting. We first analyze the performance of                           not rely solely on a robust LiDAR-only detector.
BEVFusion under different weather and lighting conditions in
Table IV. LiDAR-only models face significant challenges in                                                VI. C ONCLUSION
detecting objects in rainy weather due to sensor noise, while                          We present BEVFusion, an efficient and generic framework
BEVFusion leverages the robustness of camera sensors to                             for multi-task multi-sensor 3D perception. BEVFusion unifies
achieve a 10.7 mAP improvement, which largely narrows the                           camera and LiDAR features in a shared BEV space that fully
performance gap between sunny and rainy scenarios. Poor                             preserves geometric and semantic information. To achieve
lighting conditions pose challenges for both detection and                          this, we accelerate the slow camera-to-BEV transformation
segmentation models. For detection, MVP’s improvement is                            by more than 40 times. BEVFusion rethinks the effectiveness
relatively small compared to BEVFusion, which relies less on                        of point-level fusion in multi-sensor perception systems
accurate 2D instance segmentations to generate virtual points                       and achieves superior performance on both nuScenes 3D
and therefore performs better in dark or overexposed scenes.                        detection and BEV map segmentation tasks with 1.5-1.9× less
For segmentation, while camera-only BEVFusion outperforms                           computation and 1.3-1.6× measured speedup over existing
CenterPoint on the entire benchmark, its performance drops                          solutions. BEVFusion also outperforms all existing sensor
significantly at nighttime. However, multi-modal BEVFusion                          fusion methods on Waymo open dataset. We hope that
achieves a 12.8 mIoU improvement, even greater than its                             BEVFusion can serve as a simple but powerful baseline
improvement in the daytime, demonstrating the importance                            to inspire future research on multi-task multi-sensor fusion.
of leveraging geometric clues when camera sensors fail.
Sizes and Distances. We also analyze the performance of                                                      R EFERENCES
BEVFusion under different object sizes and distances. From                           [1] S. Vora, A. H. Lang, B. Helou, and O. Beijbom, “PointPainting:
Figure 4a, BEVFusion achieves consistent improvements over                               Sequential Fusion for 3D Object Detection,” in CVPR, 2020.
 [2] C. Wang, C. Ma, M. Zhu, and X. Yang, “PointAugmenting: Cross-              [32] T. Wang, X. Zhu, J. Pang, and D. Lin, “Probabilistic and geometric
     Modal Augmentation for 3D Object Detection,” in CVPR, 2021.                     depth: Detecting objects in perspective,” in CoRL, 2021.
 [3] Y. Li, A. W. Yu, T. Meng, B. Caine, J. Ngiam, D. Peng, J. Shen, B. Wu,     [33] H. Chen, P. Wang, F. Wang, W. Tian, L. Xiong, and H. Li, “EPro-
     Y. Lu, D. Zhou et al., “DeepFusion: Lidar-Camera Deep Fusion for                PnP: Generalized End-to-End Probabilistic Perspective-n-Points for
     Multi-Modal 3D Object Detection,” in CVPR, 2022.                                Monocular Object Pose Estimation,” in CVPR, 2022.
 [4] T. Yin, X. Zhou, and P. Krähenbühl, “Multimodal Virtual Point 3D         [34] Y. Wang, V. Guizilini, T. Zhang, Y. Wang, H. Zhao, and J. M. Solomon,
     Detection,” in NeurIPS, 2021.                                                   “DETR3D: 3D Object Detection from Multi-view Images via 3D-to-2D
 [5] B. Pan, J. Sun, H. Y. T. Leung, A. Andonian, and B. Zhou, “Cross-View           Queries,” in CoRL, 2021.
     Semantic Segmentation for Sensing Surroundings,” RA-L, 2020.               [35] Y. Liu, T. Wang, X. Zhang, and J. Sun, “PETR: Position Embedding
 [6] J. Philion and S. Fidler, “Lift, Splat, Shoot: Encoding Images From             Transformation for Multi-View 3D Object Detection,” arXiv, 2022.
     Arbitrary Camera Rigs by Implicitly Unprojecting to 3D,” in ECCV,          [36] X. Zhu, W. Su, L. Lu, B. Li, X. Wang, and J. Dai, “Deformable DETR:
     2020.                                                                           Deformable Transformers for End-to-End Object Detection,” in ICLR,
 [7] Q. Li, Y. Wang, Y. Wang, and H. Zhao, “HDMapNet: An Online HD                   2021.
     Map Construction and Evaluation Framework,” in ICRA, 2022.                 [37] Y. Wang, X. Zhang, T. Yang, and J. Sun, “Anchor DETR: Query
 [8] B. Zhou and P. Krähenbühl, “Cross-View Transformers for Real-Time             Design for Transformer-Based Detector,” in AAAI, 2022.
     Map-View Semantic Segmentation,” in CVPR, 2022.                            [38] T. Roddick, A. Kendall, and R. Cipolla, “Orthographic Feature
 [9] Y. Zhou and O. Tuzel, “VoxelNet: End-to-End Learning for Point                  Transform for Monocular 3D Object Detection,” in BMVC, 2019.
     Cloud Based 3D Object Detection,” in CVPR, 2018.                           [39] T. Roddick and R. Cipolla, “Predicting Semantic Map Representations
[10] A. H. Lang, S. Vora, H. Caesar, L. Zhou, and J. Yang, “PointPillars:            from Images using Pyramid Occupancy Networks,” in CVPR, 2020.
     Fast Encoders for Object Detection from Point Clouds,” in CVPR,            [40] J. Huang, G. Huang, Z. Zhu, Y. Ye, and D. Du, “BEVDet: High-
     2019.                                                                           performance Multi-camera 3D Object Detection in Bird-Eye-View,”
[11] Y. Yan, Y. Mao, and B. Li, “SECOND: Sparsely Embedded Convolu-                  arXiv, 2021.
     tional Detection,” Sensors, 2018.                                          [41] E. Xie, Z. Yu, D. Zhou, J. Philion, A. Anandkumar, S. Fidler, P. Luo,
[12] B. Zhu, Z. Jiang, X. Zhou, Z. Li, and G. Yu, “Class-Balanced Grouping           and J. M. Alvarez, “M2 BEV: Multi-Camera Joint 3D Detection and
     and Sampling for Point Cloud 3D Object Detection,” arXiv, 2019.                 Segmentation with Unified Birds-Eye View Representation,” arXiv,
[13] Z. Yang, Y. Sun, S. Liu, and J. Jia, “3DSSD: Point-Based 3D Single              2022.
     Stage Object Detector,” CVPR, 2020.                                        [42] C. Reading, A. Harakeh, J. Chae, and S. L. Waslander, “Categorical
[14] Y. Zhou, P. Sun, Y. Zhang, D. Anguelov, J. Gao, T. Ouyang, J. Guo,              depth distributionnetwork for monocular 3d object detection,” in CVPR,
     J. Ngiam, and V. Vasudevan, “End-to-End Multi-View Fusion for 3D                2021.
     Object Detection in LiDAR Point Clouds,” CoRL, 2019.                       [43] Z. Li, W. Wang, H. Li, E. Xie, C. Sima, T. Lu, Y. Qiao, and J. Dai,
[15] C. R. Qi, L. Yi, H. Su, and L. J. Guibas, “PointNet++: Deep Hierarchical        “BEVFormer: Learning Bird’s-Eye-View Representation from Multi-
     Feature Learning on Point Sets in a Metric Space,” in NeurIPS, 2017.            Camera Images via Spatiotemporal Transformers,” arXiv, 2022.
[16] B. Graham, M. Engelcke, and L. van der Maaten, “3D Semantic                [44] X. Chen, H. Ma, J. Wan, B. Li, and T. Xia, “Multi-View 3D Object
     Segmentation With Submanifold Sparse Convolutional Networks,” in                Detection Network for Autonomous Driving,” in CVPR, 2017.
     CVPR, 2018.                                                                [45] C. R. Qi, W. Liu, C. Wu, H. Su, and L. J. Guibas, “Frustum PointNets
[17] T. Yin, X. Zhou, and P. Krähenbühl, “Center-Based 3D Object Detection         for 3D Object Detection from RGB-D Data,” in CVPR, 2018.
     and Tracking,” in CVPR, 2021.                                              [46] Z. Wang and K. Jia, “Frustum ConvNet: Sliding Frustums to Aggregate
[18] R. Ge, Z. Ding, Y. Hu, W. Shao, L. Huang, K. Li, and Q. Liu, “1st               Local Point-Wise Features for Amodal 3D Object Detection,” in IROS,
     Place Solutions to the Real-time 3D Detection and the Most Efficient            2019.
     Model of the Waymo Open Dataset Challenge 2021,” in CVPRW,                 [47] R. Nabati and H. Qi, “CenterFusion: Center-Based Radar and Camera
     2021.                                                                           Fusion for 3D Object Detection,” in WACV, 2021.
[19] Q. Chen, L. Sun, Z. Wang, K. Jia, and A. Yuille, “Object as Hotspots:      [48] X. Chen, T. Zhang, Y. Wang, Y. Wang, and H. Zhao, “FUTR3D: A
     An Anchor-Free 3D Object Detection Approach via Firing of Hotspots,”            Unified Sensor Fusion Framework for 3D Detection,” arXiv, 2022.
     in ECCV, 2020.                                                             [49] X. Bai, Z. Hu, X. Zhu, Q. Huang, Y. Chen, H. Fu, and C.-L. Tai,
[20] C. R. Qi, Y. Zhou, M. Najibi, P. Sun, K. Vo, B. Deng, and D. Anguelov,          “TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection
     “Offboard 3D Object Detection from Point Cloud Sequences,” in CVPR,             with Transformers,” in CVPR, 2022.
     2021.                                                                      [50] S. Xu, D. Zhou, J. Fang, J. Yin, B. Zhou, and L. Zhang, “FusionPainting:
[21] L. Fan, X. Xiong, F. Wang, N. Wang, and Z. Zhang, “RangeDet: In                 Multimodal Fusion with Adaptive Attention for 3D Object Detection,”
     Defense of Range View for LiDAR-Based 3D Object Detection,” in                  in ITSC, 2021.
     ICCV, 2021.                                                                [51] Z. Chen, Z. Li, S. Zhang, L. Fang, Q. Jiang, F. Zhao, B. Zhou, and
[22] Q. Chen, S. Vora, and O. Beijbom, “PolarStream: Streaming Lidar                 H. Zhao, “AutoAlign: Pixel-Instance Feature Aggregation for Multi-
     Object Detection and Segmentation with Polar Pillars,” in NeurIPS,              Modal 3D Object Detection,” arXiv, 2022.
     2021.                                                                      [52] M. Liang, B. Yang, S. Wang, and R. Urtasun, “Deep Continuous Fusion
[23] Y. Wang and J. M. Solomon, “Object DGCNN: 3D Object Detection                   for Multi-Sensor 3D Object Detection,” in ECCV, 2018.
     using Dynamic Graphs,” in NeurIPS, 2021.                                   [53] D. Park, R. Ambrus, V. Guizilini, J. Li, and A. Gaidon, “Is Pseudo-Lidar
[24] S. Shi, X. Wang, and H. Li, “PointRCNN: 3D Object Proposal                      needed for Monocular 3D Object detection?” in ICCV, 2021.
     Generation and Detection From Point Cloud,” in CVPR, 2019.                 [54] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár, “Focal Loss for
[25] Y. Chen, S. Liu, X. Shen, and J. Jia, “Fast Point R-CNN,” in ICCV,              Dense Object Detection,” in ICCV, 2017.
     2019.                                                                      [55] S. Chen, Z. Jie, X. Wei, and L. Ma, “MT-Net Submission to the Waymo
[26] S. Shi, Z. Wang, J. Shi, X. Wang, and H. Li, “From Points to Parts:             3D Detection Leaderboard,” arXiv, 2022.
     3D Object Detection from Point Cloud with Part-aware and Part-             [56] X. Chen, S. Shi, B. Zhu, K. C. Cheung, H. Xu, and H. Li, “MPPNet:
     aggregation Network,” TPAMI, 2020.                                              Multi-Frame Feature Intertwining with Proxy Points for 3D Temporal
[27] S. Shi, C. Guo, L. Jiang, Z. Wang, J. Shi, X. Wang, and H. Li, “PV-             Object Detection,” in ECCV, 2022.
     RCNN: Point-Voxel Feature Set Abstraction for 3D Object Detection,”        [57] Z. Liu, Y. Lin, Y. Cao, H. Hu, Y. Wei, Z. Zhang, S. Lin, and B. Guo,
     in CVPR, 2020.                                                                  “Swin Transformer: Hierarchical Vision Transformer using Shifted
[28] S. Shi, L. Jiang, J. Deng, Z. Wang, C. Guo, J. Shi, X. Wang, and                Windows,” in ICCV, 2021.
     H. Li, “PV-RCNN++: Point-Voxel Feature Set Abstraction With Local          [58] T.-Y. Lin, P. Dollár, R. Girshick, K. He, B. Hariharan, and S. Belongie,
     Vector Representation for 3D Object Detection,” arXiv, 2021.                    “Feature Pyramid Networks for Object Detection,” in CVPR, 2017.
[29] Z. Li, F. Wang, and N. Wang, “LiDAR R-CNN: An Efficient and                [59] H. Caesar, V. Bankiti, A. H. Lang, S. Vora, V. E. Liong, Q. Xu,
     Universal 3D Object Detector,” CVPR, 2021.                                      A. Krishnan, Y. Pan, G. Baldan, and O. Beijbom, “nuScenes: A
[30] T. Wang, X. Zhu, J. Pang, and D. Lin, “FCOS3D: Fully Convolutional              Multimodal Dataset for Autonomous Driving,” in CVPR, 2020.
     One-Stage Monocular 3D Object Detection,” in ICCVW, 2021.                  [60] P. Sun, H. Kretzschmar, X. Dotiwalla, A. Chouard, V. Patnaik, P. Tsui,
[31] Z. Tian, C. Shen, H. Chen, and T. He, “FCOS: Fully Convolutional                J. Guo, Y. Zhou, Y. Chai, B. Caine, V. Vasudevan, W. Han, J. Ngiam,
     One-Stage Object Detection,” in ICCV, 2019.                                     H. Zhao, A. Timofeev, S. Ettinger, M. Krivokon, A. Gao, A. Joshi,
Y. Zhang, J. Shlens, Z. Chen, and D. Anguelov, “Scalability in
Perception for Autonomous Driving: Waymo Open Dataset,” in CVPR.
