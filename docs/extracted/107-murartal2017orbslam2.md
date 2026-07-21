---
source_id: 107
bibtex_key: murartal2017orbslam2
title: ORB-SLAM2: An Open-Source SLAM System for Monocular, Stereo, and RGB-D Cameras
year: 2017
domain_theme: RGB-D SLAM
verified_pdf: 107_ORB-SLAM2.pdf
char_count: 65508
---

This paper has been accepted for publication in IEEE Transactions on Robotics.

                                                                                     DOI: 10.1109/TRO.2017.2705103
                                                                          IEEE Xplore: http://ieeexplore.ieee.org/document/7946260/

                                            c 2017 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any
                                         current or future media, including reprinting /republishing this material for advertising or promotional purposes, creating new
                                         collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other
                                         works.
arXiv:1610.06475v2 [cs.RO] 19 Jun 2017
                                                                                                                                                          1

           ORB-SLAM2: an Open-Source SLAM System for
              Monocular, Stereo and RGB-D Cameras
                                                     Raúl Mur-Artal and Juan D. Tardós

   Abstract—We present ORB-SLAM2 a complete SLAM system
for monocular, stereo and RGB-D cameras, including map reuse,
loop closing and relocalization capabilities. The system works in
real-time on standard CPUs in a wide variety of environments
from small hand-held indoors sequences, to drones flying in
industrial environments and cars driving around a city. Our
back-end based on bundle adjustment with monocular and stereo
observations allows for accurate trajectory estimation with metric
scale. Our system includes a lightweight localization mode that
leverages visual odometry tracks for unmapped regions and
matches to map points that allow for zero-drift localization. The
evaluation on 29 popular public sequences shows that our method
achieves state-of-the-art accuracy, being in most cases the most
accurate SLAM solution. We publish the source code, not only
for the benefit of the SLAM community, but with the aim of
being an out-of-the-box SLAM solution for researchers in other
fields.

                          I. I NTRODUCTION
    Simultaneous Localization and Mapping (SLAM) has been
a hot research topic in the last two decades in the Computer Vi-               (a) Stereo input: trajectory and sparse reconstruction of an urban environment
                                                                               with multiple loop closures.
sion and Robotics communities, and has recently attracted the
attention of high-technological companies. SLAM techniques
build a map of an unknown environment and localize the
sensor in the map with a strong focus on real-time operation.
Among the different sensor modalities, cameras are cheap
and provide rich information of the environment that allows
for robust and accurate place recognition. Therefore Visual
SLAM solutions, where the main sensor is a camera, are of
major interest nowadays. Place recognition is a key module
of a SLAM system to close loops (i.e. detect when the sensor
returns to a mapped area and correct the accumulated error
in exploration) and to relocalize the camera after a tracking
failure, due to occlusion or aggressive motion, or at system
re-initialization.
    Visual SLAM can be performed by using just a monocular
camera, which is the cheapest and smallest sensor setup.                       (b) RGB-D input: keyframes and dense pointcloud of a room scene with one
                                                                               loop closure. The pointcloud is rendered by backprojecting the sensor depth
However as depth is not observable from just one camera,                       maps from estimated keyframe poses. No fusion is performed.
the scale of the map and estimated trajectory is unknown.
                                                                               Fig. 1. ORB-SLAM2 processes stereo and RGB-D inputs to estimate camera
In addition the system bootstrapping require multi-view or                     trajectory and build a map of the environment. The system is able to close
filtering techniques to produce an initial map as it cannot                    loops, relocalize, and reuse its map in real-time on standard CPUs with high
be triangulated from the very first frame. Last but not least,                 accuracy and robustness.

   This work was supported by the Spanish government under Project
DPI2015-67275, the Aragón regional governmnet under Project DGA T04-
FSE and the Ministerio de Educación Scholarship FPU13/04175.                  monocular SLAM suffers from scale drift and may fail if
   R. Mur-Artal was with the Instituto de Investigación en Ingenierı́a de     performing pure rotations in exploration. By using a stereo
Aragón (I3A), Universidad de Zaragoza, 50018 Zaragoza, Spain, until January
2017. He is currently with Oculus Research, Redmond, WA 98052 USA (e-          or an RGB-D camera all these issues are solved and allows
mail: raul.murartal@oculus.com).                                               for the most reliable Visual SLAM solutions.
   J. D. Tardós is with the Instituto de Investigación en Ingenierı́a de
Aragón (I3A), Universidad de Zaragoza, 50018 Zaragoza, Spain (e-mail:           In this paper we build on our monocular ORB-SLAM [1]
tardos@unizar.es).                                                             and propose ORB-SLAM2 with the following contributions:
                                                                                                                                   2

  •   The first open-source1 SLAM system for monocular,            al. [9] uses a relative representation of landmarks and poses
      stereo and RGB-D cameras, including loop closing, relo-      and performs relative BA in an active area which can be
      calization and map reuse.                                    constrained for constant-time. RSLAM is able to close loops
   • Our RGB-D results show that by using Bundle Adjust-           which allow to expand active areas at both sides of a loop,
      ment (BA) we achieve more accuracy than state-of-the-        but global consistency is not enforced. The recent S-PTAM by
      art methods based on ICP or photometric and depth error      Pire et al. [10] performs local BA, however it lacks large loop
      minimization.                                                closing. Similar to these approaches we perform BA in a local
   • By using close and far stereo points and monocular            set of keyframes so that the complexity is independent of the
      observations our stereo results are more accurate than the   map size and we can operate in large environments. However
      state-of-the-art direct stereo SLAM.                         our goal is to build a globally consistent map. When closing
   • A lightweight localization mode that can effectively reuse    a loop, our system aligns first both sides, similar to RSLAM,
      the map with mapping disabled.                               so that the tracking is able to continue localizing using the
   Fig. 1 shows examples of ORB-SLAM2 output from stereo           old map and then performs a pose-graph optimization that
and RGB-D inputs. The stereo case shows the final trajectory       minimizes the drift accumulated in the loop, followed by full
and sparse reconstruction of the sequence 00 from the KITTI        BA.
dataset [2]. This is an urban sequence with multiple loop             The recent Stereo LSD-SLAM of Engel et al. [11] is a
closures that ORB-SLAM2 was able to successfully detect.           semi-dense direct approach that minimizes photometric error
The RGB-D case shows the keyframe poses estimated in               in image regions with high gradient. Not relying on features,
sequence fr1 room from the TUM RGB-D Dataset [3], and              the method is expected to be more robust to motion blur or
a dense pointcloud, rendered by backprojecting sensor depth        poorly-textured environments. However as a direct method its
maps from the estimated keyframe poses. Note that our SLAM         performance can be severely degraded by unmodeled effects
does not perform any fusion like KinectFusion [4] or similar,      like rolling shutter or non-lambertian reflectance.
but the good definition indicates the accuracy of the keyframe
poses. More examples are shown on the attached video.              B. RGB-D SLAM
   In the rest of the paper, we discuss related work in Section
II, we describe our system in Section III, then present the           One of the earliest and most famed RGB-D SLAM systems
evaluation results in Section IV and end with conclusions in       was the KinectFusion of Newcombe et al. [4]. This method
Section V.                                                         fused all depth data from the sensor into a volumetric dense
                                                                   model that is used to track the camera pose using ICP. This
                                                                   system was limited to small workspaces due to its volumetric
                      II. R ELATED W ORK
                                                                   representation and the lack of loop closing. Kintinuous by
  In this section we discuss related work on stereo and RGB-       Whelan et al. [12] was able to operate in large environments
D SLAM. Our discussion, as well as the evaluation in Section       by using a rolling cyclical buffer and included loop closing
IV is focused only on SLAM approaches.                             using place recognition and pose graph optimization.
                                                                      Probably the first popular open-source system was the
A. Stereo SLAM                                                     RGB-D SLAM of Endres et al. [13]. This is a feature-based
    A remarkable early stereo SLAM system was the work of          system, whose front-end computes frame-to-frame motion by
Paz et al. [5]. Based on Conditionally Independent Divide and      feature matching and ICP. The back-end performs pose-graph
Conquer EKF-SLAM it was able to operate in larger environ-         optimization with loop closure constraints from a heuristic
ments than other approaches at that time. Most importantly, it     search. Similarly the back-end of DVO-SLAM by Kerl et al.
was the first stereo SLAM exploiting both close and far points     [14] optimizes a pose-graph where keyframe-to-keyframe con-
(i.e. points whose depth cannot be reliably estimated due to       straints are computed from a visual odometry that minimizes
little disparity in the stereo camera), using an inverse depth     both photometric and depth error. DVO-SLAM also searches
parametrization [6] for the latter. They empirically showed that   for loop candidates in a heuristic fashion over all previous
points can be reliably triangulated if their depth is less than    frames, instead of relying on place recognition.
∼40 times the stereo baseline. In this work we follow this            The recent ElasticFusion of Whelan et al. [15] builds a
strategy of treating in a different way close and far points, as   surfel-based map of the environment. This is a map-centric
explained in Section III-A.                                        approach that forget poses and performs loop closing applying
    Most modern stereo SLAM systems are keyframe-based             a non-rigid deformation to the map, instead of a standard
[7] and perform BA optimization in a local area to achieve         pose-graph optimization. The detailed reconstruction and lo-
scalability. The work of Strasdat et al. [8] performs a joint      calization accuracy of this system is impressive, but the current
optimization of BA (point-pose constraints) in an inner win-       implementation is limited to room-size maps as the complexity
dow of keyframes and pose-graph (pose-pose constraints) in         scales with the number of surfels in the map.
an outer window. By limiting the size of these windows the            As proposed by Strasdat et al. [8] our ORB-SLAM2 uses
method achieves constant time complexity, at the expense of        depth information to synthesize a stereo coordinate for ex-
not guaranteeing global consistency. The RSLAM of Mei et           tracted features on the image. This way our system is agnostic
                                                                   of the input being stereo or RGB-D. Differently to all above
  1 https://github.com/raulmur/ORB SLAM2                           methods our back-end is based on bundle adjustment and
                                                                                                                                                          3

                               (a) System Threads and Modules.                                               (b) Input pre-processing
Fig. 2. ORB-SLAM2 is composed of three main parallel threads: tracking, local mapping and loop closing, which can create a fourth thread to perform
full BA after a loop closure. The tracking thread pre-processes the stereo or RGB-D input so that the rest of the system operates independently of the input
sensor. Although it is not shown in this figure, ORB-SLAM2 also works with a monocular input as in [1].

builds a globally consistent sparse reconstruction. Therefore                  to rotation and scale and present a good invariance to camera
our method is lightweight and works with standard CPUs. Our                    auto-gain and auto-exposure, and illumination changes. More-
goal is long-term and globally consistent localization instead                 over they are fast to extract and match allowing for real-time
of building the most detailed dense reconstruction. However                    operation and show good precision/recall performance in bag-
from the highly accurate keyframe poses one could fuse depth                   of-word place recognition [18].
maps and get accurate reconstruction on-the-fly in a local area                   In the rest of this section we present how stereo/depth
or post-process the depth maps from all keyframes after a full                 information is exploited and which elements of the system
BA and get an accurate 3D model of the whole scene.                            are affected. For a detailed description of each system block,
                                                                               we refer the reader to our monocular publication [1].
                      III. ORB-SLAM2
   ORB-SLAM2 for stereo and RGB-D cameras is built on                          A. Monocular, Close Stereo and Far Stereo Keypoints
our monocular feature-based ORB-SLAM [1], whose main
                                                                                  ORB-SLAM2 as a feature-based method pre-processes the
components are summarized here for reader convenience. A
                                                                               input to extract features at salient keypoint locations, as shown
general overview of the system is shown in Fig. 2. The system
                                                                               in Fig. 2b. The input images are then discarded and all system
has three main parallel threads: 1) the tracking to localize
                                                                               operations are based on these features, so that the system is
the camera with every frame by finding feature matches to
                                                                               independent of the sensor being stereo or RGB-D. Our system
the local map and minimizing the reprojection error applying
                                                                               handles monocular and stereo keypoints, which are further
motion-only BA, 2) the local mapping to manage the local
                                                                               classified as close or far.
map and optimize it, performing local BA, 3) the loop closing
                                                                                  Stereo keypoints are defined by three coordinates xs =
to detect large loops and correct the accumulated drift by
                                                                               (uL , vL , uR ), being (uL , vL ) the coordinates on the left image
performing a pose-graph optimization. This thread launches
                                                                               and uR the horizontal coordinate in the right image. For stereo
a fourth thread to perform full BA after the pose-graph
                                                                               cameras, we extract ORB in both images and for every left
optimization, to compute the optimal structure and motion
                                                                               ORB we search for a match in the right image. This can
solution.
                                                                               be done very efficiently assuming stereo rectified images,
   The system has embedded a Place Recognition module
                                                                               so that epipolar lines are horizontal. We then generate the
based on DBoW2 [16] for relocalization, in case of tracking
                                                                               stereo keypoint with the coordinates of the left ORB and the
failure (e.g. an occlusion) or for reinitialization in an already
                                                                               horizontal coordinate of the right match, which is subpixel
mapped scene, and for loop detection. The system maintains
                                                                               refined by patch correlation. For RGB-D cameras, we extract
a covisibiliy graph [8] that links any two keyframes observing
                                                                               ORB features on the RGB image and, as proposed by Strasdat
common points and a minimum spanning tree connecting
                                                                               et al. [8], for each feature with coordinates (uL , vL ) we
all keyframes. These graph structures allow to retrieve local
                                                                               transform its depth value d into a virtual right coordinate:
windows of keyframes, so that tracking and local mapping
operate locally, allowing to work on large environments, and                                                       fx b
                                                                                                           uR = uL −                       (1)
serve as structure for the pose-graph optimization performed                                                        d
when closing a loop.                                                           where fx is the horizontal focal length and b is the baseline
   The system uses the same ORB features [17] for tracking,                    between the structured light projector and the infrared camera,
mapping and place recognition tasks. These features are robust                 which we approximate to 8cm for Kinect and Asus Xtion.
                                                                                                                                     4

The uncertainty of the depth sensor is represented by the                Local BA optimizes a set of covisible keyframes KL and
uncertainty of the virtual right coordinate. In this way, features    all points seen in those keyframes PL . All other keyframes
from stereo and RGB-D input are handled equally by the rest           KF , not in KL , observing points in PL contribute to the cost
of the system.                                                        function but remain fixed in the optimization. Defining Xk as
   A stereo keypoint is classified as close if its associated depth   the set of matches between points in PL and keypoints in a
is less than 40 times the stereo/RGB-D baseline, as suggested         keyframe k, the optimization problem is the following:
in [5], otherwise it is classified as far. Close keypoints can                                                   X      X
                                                                       {Xi , Rl , tl |i ∈ PL , l ∈ KL } = argmin             ρ (Ekj )
be safely triangulated from one frame as depth is accurately                                           Xi ,Rl ,tl k∈K ∪K j∈X
                                                                                                                     L   F   k
estimated and provide scale, translation and rotation informa-
                                                                                             j                   j
                                                                                                                        2
tion. On the other hand far points provide accurate rotation                       Ekj =    x(·) − π(·) Rk X + tk
                                                                                                                         Σ
information but weaker scale and translation information. We                                                                     (4)
triangulate far points when they are supported by multiple               Full BA is the specific case of local BA, where all
views.                                                                keyframes and points in the map are optimized, except the
   Monocular keypoints are defined by two coordinates xm =            origin keyframe that is fixed to eliminate the gauge freedom.
(uL , vL ) on the left image and correspond to all those ORB
for which a stereo match could not be found or that have              D. Loop Closing and Full BA
an invalid depth value in the RGB-D case. These points are
only triangulated from multiple views and do not provide                 Loop closing is performed in two steps, firstly a loop has to
scale information, but contribute to the rotation and translation     be detected and validated, and secondly the loop is corrected
estimation.                                                           optimizing a pose-graph. In contrast to monocular ORB-
                                                                      SLAM, where scale drift may occur [20], the stereo/depth
                                                                      information makes scale observable and the geometric vali-
B. System Bootstrapping                                               dation and pose-graph optimization no longer require dealing
   One of the main benefits of using stereo or RGB-D cameras          with scale drift and are based on rigid body transformations
is that, by having depth information from just one frame, we          instead of similarities.
do not need a specific structure from motion initialization as           In ORB-SLAM2 we have incorporated a full BA optimiza-
in the monocular case. At system startup we create a keyframe         tion after the pose-graph to achieve the optimal solution. This
with the first frame, set its pose to the origin, and create an       optimization might be very costly and therefore we perform it
initial map from all stereo keypoints.                                in a separate thread, allowing the system to continue creating
                                                                      map and detecting loops. However this brings the challenge
                                                                      of merging the bundle adjustment output with the current state
C. Bundle Adjustment with Monocular and Stereo Constraints            of the map. If a new loop is detected while the optimization
   Our system performs BA to optimize the camera pose in the          is running, we abort the optimization and proceed to close the
tracking thread (motion-only BA), to optimize a local window          loop, which will launch the full BA optimization again. When
of keyframes and points in the local mapping thread (local            the full BA finishes, we need to merge the updated subset
BA), and after a loop closure to optimize all keyframes and           of keyframes and points optimized by the full BA, with the
points (full BA). We use the Levenberg–Marquardt method               non-updated keyframes and points that where inserted while
implemented in g2o [19].                                              the optimization was running. This is done by propagating
   Motion-only BA optimizes the camera orientation R ∈                the correction of updated keyframes (i.e. the transformation
SO(3) and position t ∈ R3 , minimizing the reprojection error         from the non-optimized to the optimized pose) to non-updated
between matched 3D points Xi ∈ R3 in world coordinates and            keyframes through the spanning tree. Non-updated points
keypoints xi(·) , either monocular xim ∈ R2 or stereo xis ∈ R3 ,      are transformed according to the correction applied to their
with i ∈ X the set of all matches:                                    reference keyframe.

                  X                                                 E. Keyframe Insertion
                      i            i
                                        2
  {R, t} = argmin  ρ x(·) − π(·) RX + t                        (2)       ORB-SLAM2 follows the policy introduced in monocular
                R,t                                      Σ
                      i∈X                                             ORB-SLAM of inserting keyframes very often and culling
where ρ is the robust Huber cost function and Σ the covariance        redundant ones afterwards. The distinction between close and
matrix associated to the scale of the keypoint. The projection        far stereo points allows us to introduce a new condition
functions π(·) , monocular πm and rectified stereo πs , are           for keyframe insertion, which can be critical in challenging
defined as follows:                                                   environments where a big part of the scene is far from the
                                                                stereo sensor, as shown in Fig. 3. In such environment we
                                                     fx X
                                                        Z + cx
     
       X           X                X                               need to have a sufficient amount of close points to accurately
                   fx Z + cx
πm  Y  =                   , πs  Y  =  fy YZ + cy 
                                                               
                      Y                                               estimate translation, therefore if the number of tracked close
       Z           fy Z + cy           Z           fx X−b
                                                        Z + cx
                                                                      points drops below τt and the frame could create at least τc
                                                              (3)     new close stereo points, the system will insert a new keyframe.
where (fx , fy ) is the focal length, (cx , cy ) is the principal     We empirically found that τt = 100 and τc = 70 works well
point and b the baseline, all known from calibration.                 in all our experiments.
                                                                                                                                                                                                                  5

                                                                                                                               TABLE I
                                                                                                            C OMPARISON OF ACCURACY IN THE KITTI DATASET.

                                                                                                                     ORB-SLAM2 (stereo)                                 Stereo LSD-SLAM
                                                                                                                  trel     rrel      tabs                          trel        rrel    tabs
                                                                                            Sequence
                                                                                                                  (%)   (deg/100m)    (m)                          (%)      (deg/100m)  (m)
                                                                                                     00           0.70     0.25       1.3                          0.63        0.26     1.0
                                                                                                     01           1.39     0.21      10.4                          2.36        0.36     9.0
                                                                                                     02           0.76     0.23       5.7                          0.79        0.23     2.6
Fig. 3. Tracked points in KITTI 01 [2]. Green points have a depth less than                          03           0.71     0.18       0.6                          1.01        0.28     1.2
40 times the stereo baseline, while blue points are further away. In this kind of                    04           0.48     0.13       0.2                          0.38        0.31     0.2
sequences it is important to insert keyframes often enough so that the amount                        05           0.40     0.16       0.8                          0.64        0.18     1.5
of close points allows for accurate translation estimation. Far points contribute                    06           0.51     0.15       0.8                          0.71        0.18     1.3
to estimate orientation but provide weak information for translation and scale.                      07           0.50     0.28       0.5                          0.56        0.29     0.5
                                                                                                     08           1.05     0.32       3.6                          1.11        0.31     3.9
                                                                                                     09           0.87     0.27       3.2                          1.14        0.25     5.6
F. Localization Mode                                                                                 10           0.60     0.27       1.0                          0.72        0.33     1.5

   We incorporate a Localization Mode which can be useful
for lightweight long-term localization in well mapped areas,
as long as there are not significant changes in the environment.                            500                                                          200

In this mode the local mapping and loop closing threads                                     400                                                             0

are deactivated and the camera is continuously localized by                                 300
                                                                                                                                                          200

the tracking using relocalization if needed. In this mode the                                                                                             400

                                                                                    y [m]

                                                                                                                                                y [m]
                                                                                            200
tracking leverages visual odometry matches and matches to                                   100
                                                                                                                                                          600

                                                                                                                                                          800
map points. Visual odometry matches are matches between                                       0                                                          1000
ORB in the current frame and 3D points created in the previous                              100                                                          1200
                                                                                               300        200   100     0     100   200   300                0         500         1000         1500       2000
frame from the stereo/depth information. These matches make                                                           x [m]                                                        x [m]

the localization robust to unmapped regions, but drift can be                               400                                                           150

accumulated. Map point matches ensure drift-free localization                               300                                                           100

to the existing map. This mode is demonstrated in the accom-
                                                                                            200                                                            50
panying video.
                                                                                    y [m]

                                                                                                                                                 y [m]
                                                                                            100                                                             0

                            IV. E VALUATION                                                   0                                                            50

   We have evaluated ORB-SLAM2 in three popular datasets                                    100
                                                                                               300        200   100     0
                                                                                                                      x [m]
                                                                                                                              100   200   300
                                                                                                                                                          100
                                                                                                                                                             200     150     100
                                                                                                                                                                                   x [m]
                                                                                                                                                                                           50          0    50

and compared to other state-of-the-art SLAM systems, using
always the results published by the original authors and                            Fig. 4. Estimated trajectory (black) and ground-truth (red) in KITTI 00, 01,
standard evaluation metrics in the literature. We have run                          05 and 07.
ORB-SLAM2 in an Intel Core i7-4790 desktop computer with
16Gb RAM. In order to account for the non-deterministic
nature of the multi-threading system, we run each sequence                          system outperforms Stereo LSD-SLAM in most sequences,
5 times and show median results for the accuracy of the                             and achieves in general a relative error lower than 1%. The
estimated trajectory. Our open-source implementation includes                       sequence 01, see Fig. 3, is the only highway sequence in
the calibration and instructions to run the system in all these                     the training set and the translation error is slightly worse.
datasets.                                                                           Translation is harder to estimate in this sequence because very
                                                                                    few close points can be tracked, due to high speed and low
A. KITTI Dataset                                                                    frame-rate. However orientation can be accurately estimated,
   The KITTI dataset [2] contains stereo sequences recorded                         achieving an error of 0.21 degrees per 100 meters, as there are
from a car in urban and highway environments. The stereo                            many far point that can be long tracked. Fig. 4 shows some
sensor has a ∼54cm baseline and works at 10Hz with a                                examples of estimated trajectories.
resolution after rectification of 1240 × 376 pixels. Sequences                         Compared to the monocular results presented in [1], the
00, 02, 05, 06, 07 and 09 contain loops. Our ORB-SLAM2                              proposed stereo version is able to process the sequence 01
detects all loops and is able to reuse its map afterwards,                          where the monocular system failed. In this highway sequence,
except for sequence 09 where the loop happens in very few                           see Fig. 3, close points are in view only for a few frames.
frames at the end of the sequence. Table I shows results in                         The ability of the stereo version to create points from just
the 11 training sequences, which have public ground-truth,                          one stereo keyframe instead of the delayed initialization of
compared to the state-of-the-art Stereo LSD-SLAM [11], to                           the monocular, consisting on finding matches between two
our knowledge the only stereo SLAM showing detailed results                         keyframes, is critical in this sequence not to lose tracking.
for all sequences. We use two different metrics, the absolute                       Moreover the stereo system estimates the map and trajectory
translation RMSE tabs proposed in [3], and the average relative                     with metric scale and does not suffer from scale drift, as seen
translation trel and rotation rrel errors proposed in [2]. Our                      in Fig. 5.
                                                                                                                                                                                                                                                 6

                                                                                                                                  TABLE II
         400                                           400                                                E U RO C DATASET. C OMPARISON OF T RANSLATION RMSE (m).
         300                                           300

                                                                                                              Sequence                                ORB-SLAM2 (stereo)                          Stereo LSD-SLAM
 y [m]

                                               y [m]
         200                                           200
                                                                                                              V1 01 easy                                    0.035                                        0.066
         100                                           100                                                    V1 02 medium                                  0.020                                        0.074
                                                                                                              V1 03 difficult                               0.048                                        0.089
           0                                             0
                                                                                                              V2 01 easy                                    0.037                                          -
               400   200   0       200   400                 400   200   0       200   400
                           x [m]                                         x [m]                                V2 02 medium                                  0.035                                          -
                                                                                                              V2 03 difficult                                 X                                            -
Fig. 5. Estimated trajectory (black) and ground-truth (red) in KITTI 08. Left:                                MH 01 easy                                    0.035                                          -
monocular ORB-SLAM [1], right: ORB-SLAM2 (stereo). Monocular ORB-                                             MH 02 easy                                    0.018                                          -
SLAM suffers from severe scale drift in this sequence, especially at the turns.                               MH 03 medium                                  0.028                                          -
In contrast the proposed stereo version is able to estimate the true scale of                                 MH 04 difficult                               0.119                                          -
the trajectory and map without scale drift.                                                                   MH 05 difficult                               0.060                                          -

B. EuRoC Dataset                                                                                      4                                                                          4

                                                                                                                                                                                 3
   The recent EuRoC dataset [21] contains 11 stereo sequences                                         3

                                                                                                                                                                                 2
recorded from a micro aerial vehicle (MAV) flying around two                                          2
                                                                                                                                                                                  1
different rooms and a large industrial environment. The stereo

                                                                                              y [m]

                                                                                                                                                                         y [m]
                                                                                                      1
                                                                                                                                                                                 0
sensor has a ∼11cm baseline and provides WVGA images                                                  0
                                                                                                                                                                                  1

at 20Hz. The sequences are classified as easy , medium and                                            1                                                                           2

difficult depending on MAV’s speed, illumination and scene                                            2
                                                                                                       2.5      2.0   1.5   1.0   0.5 0.0       0.5    1.0   1.5   2.0
                                                                                                                                                                                  3
                                                                                                                                                                                      4   3       2       1           0        1        2   3
                                                                                                                                    x [m]                                                                     x [m]
texture. In all sequences the MAV revisits the environment
                                                                                                      8                                                                          12
and ORB-SLAM2 is able to reuse its map, closing loops                                                                                                                            10
                                                                                                      6
when necessary. Table II shows absolute translation RMSE                                                                                                                         8
                                                                                                      4                                                                          6
of ORB-SLAM2 for all sequences, comparing to Stereo LSD-                                                                                                                         4
                                                                                              y [m]

                                                                                                                                                                         y [m]
                                                                                                      2
SLAM, for the results provided in [11]. ORB-SLAM2 achieves                                                                                                                       2
                                                                                                      0                                                                          0
a localization precision of a few centimeters and is more                                                                                                                         2
                                                                                                      2
accurate than Stereo LSD-SLAM. Our tracking get lost in                                                                                                                          4
                                                                                                      4                                                                          6
some parts of V2 03 difficult due to severe motion blur. As                                               2      0      2     4      6
                                                                                                                                   x [m]
                                                                                                                                            8         10     12    14                 5       0       5
                                                                                                                                                                                                              x [m]
                                                                                                                                                                                                                          10       15       20

shown in [22], this sequence can be processed using IMU
information. Fig. 6 shows examples of computed trajectories                                  Fig. 6. Estimated trajectory (black) and groundtruth (red) in EuRoC
compared to the ground-truth.                                                                V1 02 medium, V2 02 medium, MH 03 medium and MH 05 difficutlt.

C. TUM RGB-D Dataset                                                                         different image resolutions and sensors. The mean and two
   The TUM RGB-D dataset [3] contains indoors sequences                                      standard deviation ranges are shown for each thread task.
from RGB-D sensors grouped in several categories to evaluate                                 As these sequences contain one single loop, the full BA and
object reconstruction and SLAM/odometry methods under dif-                                   some tasks of the loop closing thread are executed just once
ferent texture, illumination and structure conditions. We show                               and only a single time measurement is reported.The average
results in a subset of sequences where most RGB-D methods                                    tracking time per frame is below the inverse of the camera
are usually evaluated. In Table III we compare our accuracy                                  frame-rate for each sequence, meaning that our system is able
to the following state-of-the-art methods: ElasticFusion [15],                               to work in real-time. As ORB extraction in stereo images is
Kintinuous [12], DVO-SLAM [14] and RGB-D SLAM [13].                                          parallelized, it can be seen that extracting 1000 ORB features
Our method is the only one based on bundle adjustment and                                    in the stereo WVGA images of V2 02 is similar to extracting
outperforms the other approaches in most sequences. As we                                    the same amount of features in the single VGA image channel
already noticed for RGB-D SLAM results in [1], depthmaps                                     of fr3 office.
for freiburg2 sequences have a 4% scale bias, probably coming                                   The number of keyframes in the loop is shown as reference
from miscalibration, that we have compensated in our runs                                    for the times related to loop closing. While the loop in KITTI
and could partly explain our significantly better results. Fig.                              07 contains more keyframes, the covisibility graph built for
7 shows the point clouds that result from backprojecting the                                 the indoor fr3 office is denser and therefore the loop fusion,
sensor depth maps from the computed keyframe poses in four                                   pose-graph optimization and full BA tasks are more expensive.
sequences. The good definition and the straight contours of                                  The higher density of the covisibility graph makes the local
desks and posters prove the high accuracy localization of our                                map contain more keyframes and points and therefore local
approach.                                                                                    map tracking and local BA are also more expensive.

D. Timing Results                                                                                                                                          V. C ONCLUSION
  In order to complete the evaluation of the proposed system,                                   We have presented a full SLAM system for monocular,
we present in Table IV timing results in three sequences with                                stereo and RGB-D sensors, able to perform relocalization, loop
                                                                                                                                                   7

Fig. 7. Dense pointcloud reconstructions from estimated keyframe poses and sensor depth maps in TUM RGB-D fr3 office, fr1 room, fr2 desk and fr3 nst.

                         TABLE III                                          KITTI visual odometry benchmark ORB-SLAM2 is currently
  TUM RGB-D DATASET. C OMPARISON OF T RANSLATION RMSE (m).                  the best stereo SLAM solution. Crucially, compared with the
                                                                            stereo visual odometry methods that have flourished in recent
                                                                            years, ORB-SLAM2 achieves zero-drift localization in already
              ORB-SLAM2       Elastic-                 DVO      RGBD
 Sequence                                Kintinuous                         mapped areas.
               (RGB-D)        Fusion                  SLAM      SLAM
 fr1/desk        0.016         0.020       0.037      0.021     0.026          Surprisingly our RGB-D results demonstrate that if the
 fr1/desk2       0.022         0.048       0.071      0.046       -
 fr1/room        0.047         0.068       0.075      0.043     0.087
                                                                            most accurate camera localization is desired, bundle adjust-
 fr2/desk        0.009         0.071       0.034      0.017     0.057       ment performs better than direct methods or ICP, with the
 fr2/xyz         0.004         0.011       0.029      0.018       -         additional advantage of being less computationally expensive,
 fr3/office      0.010         0.017       0.030      0.035       -         not requiring GPU processing to operate in real-time.
 fr3/nst         0.019         0.016       0.031      0.018       -
                                                                               We have released the source code of our system, with
                                                                            examples and instructions so that it can be easily used by other
                                                                            researchers. ORB-SLAM2 is to the best of our knowledge
closing and reuse its map in real-time on standard CPUs. We                 the first open-source visual SLAM system that can work
focus on building globally consistent maps for reliable and                 either with monocular, stereo and RGB-D inputs. Moreover
long-term localization in a wide range of environments as                   our source code contains an example of an augmented reality
demonstrated in the experiments. The proposed localization                  application2 using a monocular camera to show the potential
mode with the relocalization capability of the system yields                of our solution.
a very robust, zero-drift, and ligthweight localization method                 Future extensions might include, to name some exam-
for known environments. This mode can be useful for certain                 ples, non-overlapping multi-camera, fisheye or omnidirectional
applications, such as tracking the user viewpoint in virtual                cameras support, large scale dense fusion, cooperative map-
reality in a well-mapped space.                                             ping or increased motion blur robustness.
   The comparison to the state-of-the-art shows that ORB-
SLAM2 achieves in most cases the highest accuracy. In the                     2 https://youtu.be/kPwy8yA4CKM
                                                                                                                                                                  8

                                                                                TABLE IV
                                             T IMING R ESULTS OF E ACH T HREAD IN M ILISECONDS ( MEAN ± 2 STD . DEVIATIONS ).

                                                Sequence                       V2 02                07               fr3 office
                                                Dataset                       EuRoC              KITTI                 TUM

                                  Settings
                                                Sensor                         Stereo            Stereo               RGB-D
                                                Resolution                   752 × 480         1226 × 370           640 × 480
                                                Camera FPS                     20Hz               10Hz                 30Hz
                                                ORB Features                   1000               2000                  1000
                                                Stereo Rectification        3.43 ± 1.10              -                    -
                                                ORB Extraction             13.54 ± 4.60       24.83 ± 8.28         11.48 ± 1.84
                                  Tracking
                                                Stereo Matching            11.26 ± 6.64       15.51 ± 4.12         0.02 ± 0.00
                                                Pose Prediction             2.07 ± 1.58       2.36 ± 1.84          2.65 ± 1.28
                                                Local Map Tracking         10.13 ± 11.40      5.38 ± 3.52          9.78 ± 6.42
                                                New Keyframe Decision       1.40 ± 1.14       1.91 ± 1.06          1.58 ± 0.92
                                                Total                      41.66 ± 18.90     49.47 ± 12.10         25.58 ± 9.76
                                                Keyframe Insertion         10.30 ± 7.50       11.61 ± 3.28         11.36 ± 5.04
                                                Map Point Culling           0.28 ± 0.20       0.45 ± 0.38          0.25 ± 0.10
                                  Mapping

                                                Map Point Creation         40.43 ± 36.10     47.69 ± 29.52        53.99 ± 23.62
                                                Local BA                  137.99 ± 248.18    69.29 ± 61.88       196.67 ± 213.42
                                                Keyframe Culling            3.80 ± 8.20       0.99 ± 0.92          6.69 ± 8.24
                                                Total                     174.10 ± 278.80    129.52 ± 88.52      267.33 ± 245.10
                                                Database Query              3.57 ± 5.86       4.13 ± 3.54          2.63 ± 2.26
                                                SE3 Estimation              0.69 ± 1.82       1.02 ± 3.68          0.66 ± 1.68
                                  Loop

                                                Loop Fusion                    21.84             82.70                298.45
                                                Essential Graph Opt.           73.15             178.31               281.99
                                                Total                         108.59             284.88               598.70
                                                Full BA                       349.25            1144.06               1640.96
                                  BA

                                                Map Update                      3.13             11.82                  5.62
                                                Total                         396.02            1205.78               1793.02
                                              Loop size (#keyframes)             82                248                  225

                                R EFERENCES                                           [12] T. Whelan, M. Kaess, H. Johannsson, M. Fallon, J. J. Leonard, and
                                                                                           J. McDonald, “Real-time large-scale dense RGB-D SLAM with volu-
 [1] R. Mur-Artal, J. M. M. Montiel, and J. D. Tardós, “ORB-SLAM: a                       metric fusion,” Int. J. Robot. Res., vol. 34, no. 4-5, pp. 598–626, 2015.
     versatile and accurate monocular SLAM system,” IEEE Trans. Robot.,               [13] F. Endres, J. Hess, J. Sturm, D. Cremers, and W. Burgard, “3-D mapping
     vol. 31, no. 5, pp. 1147–1163, 2015.                                                  with an RGB-D camera,” IEEE Trans. Robot., vol. 30, no. 1, pp. 177–
 [2] A. Geiger, P. Lenz, C. Stiller, and R. Urtasun, “Vision meets robotics:               187, 2014.
     The KITTI dataset,” Int. J. Robot. Res., vol. 32, no. 11, pp. 1231–1237,         [14] C. Kerl, J. Sturm, and D. Cremers, “Dense visual SLAM for RGB-D
     2013.                                                                                 cameras,” in IEEE/RSJ Int. Conf. Intell. Robots and Syst. (IROS), 2013.
 [3] J. Sturm, N. Engelhard, F. Endres, W. Burgard, and D. Cremers, “A                [15] T. Whelan, R. F. Salas-Moreno, B. Glocker, A. J. Davison, and
     benchmark for the evaluation of RGB-D SLAM systems,” in IEEE/RSJ                      S. Leutenegger, “ElasticFusion: Real-time dense SLAM and light source
     Int. Conf. Intell. Robots and Syst. (IROS), 2012, pp. 573–580.                        estimation,” Int. J. Robot. Res., vol. 35, no. 14, pp. 1697–1716, 2016.
 [4] R. A. Newcombe, A. J. Davison, S. Izadi, P. Kohli, O. Hilliges,                  [16] D. Gálvez-López and J. D. Tardós, “Bags of binary words for fast place
     J. Shotton, D. Molyneaux, S. Hodges, D. Kim, and A. Fitzgibbon,                       recognition in image sequences,” IEEE Trans. Robot., vol. 28, no. 5, pp.
     “KinectFusion: Real-time dense surface mapping and tracking,” in IEEE                 1188–1197, 2012.
     Int. Symp. on Mixed and Augmented Reality (ISMAR), 2011.                         [17] E. Rublee, V. Rabaud, K. Konolige, and G. Bradski, “ORB: an efficient
 [5] L. M. Paz, P. Piniés, J. D. Tardós, and J. Neira, “Large-scale 6-DOF                alternative to SIFT or SURF,” in IEEE Int. Conf. Comput. Vision (ICCV),
     SLAM with stereo-in-hand,” IEEE Trans. Robot., vol. 24, no. 5, pp.                    2011, pp. 2564–2571.
     946–957, 2008.                                                                   [18] R. Mur-Artal and J. D. Tardós, “Fast relocalisation and loop closing
 [6] J. Civera, A. J. Davison, and J. M. M. Montiel, “Inverse depth                        in keyframe-based SLAM,” in IEEE Int. Conf. on Robot. and Autom.
     parametrization for monocular SLAM,” IEEE Trans. Robot., vol. 24,                     (ICRA), 2014, pp. 846–853.
     no. 5, pp. 932–945, 2008.                                                        [19] R. Kuemmerle, G. Grisetti, H. Strasdat, K. Konolige, and W. Burgard,
 [7] H. Strasdat, J. M. M. Montiel, and A. J. Davison, “Visual SLAM: Why                   “g2o: A general framework for graph optimization,” in IEEE Int. Conf.
     filter?” Image and Vision Computing, vol. 30, no. 2, pp. 65–77, 2012.                 on Robot. and Autom. (ICRA), 2011, pp. 3607–3613.
 [8] H. Strasdat, A. J. Davison, J. M. M. Montiel, and K. Konolige, “Double           [20] H. Strasdat, J. M. M. Montiel, and A. J. Davison, “Scale drift-aware
     window optimisation for constant time visual SLAM,” in IEEE Int. Conf.                large scale monocular SLAM.” in Robot.: Sci. and Syst. (RSS), 2010.
     Comput. Vision (ICCV), 2011, pp. 2352–2359.                                      [21] M. Burri, J. Nikolic, P. Gohl, T. Schneider, J. Rehder, S. Omari, M. W.
 [9] C. Mei, G. Sibley, M. Cummins, P. Newman, and I. Reid, “RSLAM:                        Achtelik, and R. Siegwart, “The EuRoC micro aerial vehicle datasets,”
     A system for large-scale mapping in constant-time using stereo,” Int. J.              Int. J. Robot. Res., vol. 35, no. 10, pp. 1157–1163, 2016.
     Comput. Vision, vol. 94, no. 2, pp. 198–214, 2011.                               [22] R. Mur-Artal and J. D. Tardós, “Visual-inertial monocular SLAM with
[10] T. Pire, T. Fischer, J. Civera, P. De Cristóforis, and J. J. Berlles, “Stereo        map reuse,” IEEE Robot. and Autom. Lett., vol. 2, no. 2, pp. 796 – 803,
     parallel tracking and mapping for robot localization,” in IEEE/RSJ Int.               2017.
     Conf. Intell. Robots and Syst. (IROS), 2015, pp. 1373–1378.
[11] J. Engel, J. Stueckler, and D. Cremers, “Large-scale direct SLAM with
     stereo cameras,” in IEEE/RSJ Int. Conf. Intell. Robots and Syst. (IROS),
     2015.
