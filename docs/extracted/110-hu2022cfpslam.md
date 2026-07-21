---
source_id: 110
bibtex_key: hu2022cfpslam
title: CFP-SLAM: A Real-Time Visual SLAM Based on Coarse-to-Fine Probability in Dynamic Environments
year: 2022
domain_theme: RGB-D SLAM
verified_pdf: 110_CFP-SLAM.pdf
char_count: 64046
---

CFP-SLAM: A Real-time Visual SLAM Based on Coarse-to-Fine
                                                           Probability in Dynamic Environments
                                                                               Xinggang Hu1 , Yunzhou Zhang1∗ , Zhenzhong Cao1 ,
                                                                             Rong Ma2 , Yanmin Wu3 , Zhiqiang Deng1 , Wenkai Sun1

                                            Abstract— The dynamic factors in the environment will lead to          segmentation can provide a fine pixel level object mask,
                                         the decline of camera localization accuracy due to the violation of       but its real-time performance is poor. The improvement of
                                         the static environment assumption of SLAM algorithm. Recently,            segmentation accuracy and robustness often comes at the
                                         some related works generally use the combination of semantic
arXiv:2202.01938v2 [cs.RO] 25 Feb 2022

                                         constraints and geometric constraints to deal with dynamic                cost of huge computational cost. Even so, the segmentation
                                         objects, but problems can still be raised, such as poor real-time         boundary of the object can not be extremely accurate and can
                                         performance, easy to treat people as rigid bodies, and poor per-          not completely cover the moving object [12]. Object detection
                                         formance in low dynamic scenes. In this paper, a dynamic scene-           can circumvent the problems above, but there are a large
                                         oriented visual SLAM algorithm based on object detection and              amount of background point clouds in the box of objects, and
                                         coarse-to-fine static probability named CFP-SLAM is proposed.
                                         The algorithm combines semantic constraints and geometric                 some complex cases will be missed easily [3]. In addition,
                                         constraints to calculate the static probability of objects, keypoints     there are two common problems with current schemes: 1) All
                                         and map points, and takes them as weights to participate in               dynamic objects are treated as high dynamic attributes, which
                                         camera pose estimation. Extensive evaluations show that our               leads to poor performance in low dynamic scene. 2) As non-
                                         approach can achieve almost the best results in high dynamic and          rigid objects, human bodies often perform partial movement.
                                         low dynamic scenarios compared to the state-of-the-art dynamic
                                         SLAM methods, and shows quite high real-time ability.                     Directly eliminating the human body as a whole object will
                                                                                                                   reduce the constraint of keypoints and introduce a negative
                                                                I. INTRODUCTION                                    effect on accuracy of localization.
                                                                                                                      For the above problems, we propose CFP-SLAM, which is a
                                            Simultaneous localization and mapping (SLAM) is the key
                                                                                                                   high-performance high-efficiency visual SLAM system based
                                         technology for autonomous navigation of mobile robots, and
                                                                                                                   on object detection and static probability in indoor dynamic
                                         it is widely applied in the fields of autopilot, UAV and
                                                                                                                   environments. On the basis of ORB-SLAM2 [13], CFP-SLAM
                                         augmented reality (AR). SLAM system is based on environ-
                                                                                                                   uses YOLOv5 to obtain semantic information, uses extended
                                         mental static assumption [1], and dynamic factors will bring
                                                                                                                   Kalman filter (EKF) and Hungarian algorithm to compensate
                                         wrong observation data to the system, making it difficult
                                                                                                                   missed detection, calculates the static probability of objects to
                                         to establish various geometric constraints on which SLAM
                                                                                                                   distinguish high dynamic objects from low dynamic objects,
                                         system works, and reducing the accuracy and robustness of
                                                                                                                   and distinguishes foreground points and background points of
                                         SLAM system. The abnormal point processing mechanism of
                                                                                                                   object detection results based on DBSCAN (Density-Based
                                         RANSAC (Random Sample Consensus) algorithm can solve
                                                                                                                   Spatial Clustering of Applications with Noise) algorithm.
                                         the influence of certain abnormal points in static or slightly dy-
                                                                                                                   Established on a variety of constraints, a two-stage calculation
                                         namic environment. However, when dynamic objects occupy
                                                                                                                   method of the static probability of keypoints from coarse to
                                         most of the camera view, RANSAC algorithm has little effect.
                                                                                                                   fine is designed. The static probability of keypoints is used
                                            With the development of deep learning technology, some ad-
                                                                                                                   as a weight to participate in the camera pose optimization.
                                         vanced researchers have used semantic constraints to solve the
                                                                                                                   Considering the needs of different scenarios, we provide a
                                         visual SLAM problem in dynamic environment recent years.
                                                                                                                   lower-performance version to improve the real-time perfor-
                                         The general approach is to take the semantic information ob-
                                                                                                                   mance without calculating the static probability of objects.
                                         tained from object detection [2], [3] or semantic segmentation
                                                                                                                      Extensive experiments are conducted on public datasets.
                                         [4]–[12] as a priori and eliminate the dynamic objects in the
                                                                                                                   Compared with state-of-the-art dynamic SLAM methods, our
                                         environment combined with geometric constraints. Semantic
                                                                                                                   approach achieves the highest localization accuracy in almost
                                           ∗ The corresponding author of this paper.                               all low dynamics and high dynamic scenarios. The main
                                            1 Xinggang Hu, Yunzhou Zhang, Zhenzhong Cao, Zhiqiang Deng             contributions of this paper are as follows:
                                         and Wenkai Sun are with College of Information Science and En-               • Compensating missed detection based on EKF and Hun-
                                         gineering, Northeastern University, Shenyang 110819, China (Email:
                                         zhangyunzhou@mail.neu.edu.cn).                                                  garian algorithm, while using DBSCAN clustering al-
                                            2 Rong Ma is with Beijing Simulation Center, China (Email:
                                                                                                                         gorithm to distinguish the foreground points and back-
                                         mar buaa@163.com).                                                              ground points of box.
                                            3 Yanmin Wu is with School of Electronic and Computer Engineering,
                                         Peking University, Shenzhen, China.                                          • The distinction of object dynamic attributes. Based on the
                                            This work was supported by National Natural Science Foundation of            YOLOv5 object detection and geometric constraints, the
                                         China (No. 61973066), Major Science and Technology Projects of Liaoning         object motion attributes are divided into high dynamics
                                         Province(No.2021JH1/10400049), Fundation of Key Laboratory of Equip-
                                         ment Reliability(No.WD2C20205500306), Fundation of Key Laboratory of            and low dynamics, which are provided to the subsequent
                                         Aerospace System Simulation(No.6142002200301).                                  methods as a priori information for processing with
    different strategies, so as to improve the robustness and      objects combined with selective tracking algorithm. SaD-
    adaptability of SLAM system.                                   SLAM [8] extracts static feature points from objects judged
  • The static probability of keypoints from coarse to fine.       as dynamic based on semantic by verifying whether the inter
    A two-stage static probability of keypoints calculation        frame feature points meet the epipolar constraints. Vincent et
    method based on the static probability of object, the          al. [9] perform semantic segmentation of object instances in
    DBSCAN clustering algorithm, the epipolar constraints          the image, and use EKF to identify, track and remove dynamic
    and the projection constraints is proposed to solve the        objects from the scene. DP-SLAM [10] combines the results of
    problem of false deletion of static keypoints caused by        geometric constraints and semantic segmentation, the dynamic
    non-rigid body local motion.                                   keypoints are tracked in the Bayesian probability estimation
                                                                   framework. Ji et al. [11] only perform semantic segmentation
                     II. R ELATED W ORK
                                                                   on keyframes, cluster the depth map and identifies moving
A. Dynamic SLAM without Priori Semantic Information                objects combined with re-projection error to remove known
   When there is no semantic information as the priori, us-        and unknown dynamic objects. Blitz-SLAM [12] repairs the
ing reliable constraints to find the correct feature matching      mask of BlitzNet [25] based on depth information, and classi-
relationship is the basic method to deal with dynamic SLAM         fies static and dynamic matching points in potential dynamic
problem. Li et al. [14] propose a static weighting method of       areas using epipolar constraints. Generally, the above methods
keyframe edge points, and integrated into the IAICP method to      can accurately eliminate dynamic objects in the environment,
reduce tracking error. Sun et al. [15] roughly detect the motion   but it is difficult to give consideration to both localization
of moving objects based on self motion compensation image          accuracy and real-time, and the performance is generally poor
difference, and enhance the motion detection by tracking           in low dynamic scenes.
the motion using particle filter. Then, they [16] propose a
                                                                                      III. S YSTEM OVERVIEW
novel RGB-D data-based on-line motion removal approach,
and build and update the foreground model incrementally.           A. Definition of Variables
StaticFusion [17] simultaneously estimates the camera motion         In this paper, common variables are defined as follows:
as well as a probabilistic static/dynamic segmentation of the        • Fk - Frame K.
current RGB-D image pair. DMS-SLAM [18] uses GMS [19]                • K - The intrinsic matrix of a pinhole camera model.
to eliminate mismatched points. Kim et al. [20] propose a            • Tk,w ∈ R
                                                                                   4×4
                                                                                          - The transformation from world frame to
dense visual mileage calculation method based on background             camera frame K, which is composed of a rotation Rk,w ∈
model to estimate the nonparametric background model from               R3×3 and a translation tk,w ∈ R3×1 .
depth scene. Dai et al. [21] distinguishe dynamic and static              k
                                                                     • Pi - The keypoint with ID i in Fk . Its pixel co-
map points based on feature correlation. Flowfusion [22] uses                                             T
                                                                        ordinate is Pikuv = uki , vik , camera coordinate is
optical flow residuals to highlight dynamic regions in rgbd                                       T
                                                                        Pikk = Xikk , Yikk , Zikk , world coordinate is Pikw =
point clouds. Because there is no need for deep learning                 k                T
networks to provide semantic priors, the above methods are               Xiw , Yikw , Zikw . (·)f is the form of homogeneous co-
usually fast in dealing with dynamic factors, but lack of               ordinates in each coordinate system.
                                                                          k−1
accuracy.                                                            • Pi ∗    - The keypoint with ID i∗ in Fk−1 which forms a
                                                                        matching relationship with Pik .
B. Dynamic SLAM Based on Semantic Constraints                             k
                                                                     • Oi+ - The static probability of potential moving object
   Semantic segmentation or object detection can provide a              with ID i+ . Pik is the extracted keypoint on the object.
steady and reliable priority constraint for dynamic SLAM.            • OT h - The threshold to distinguish whether the object
Detect-SLAM [2] detects objects in keyframes and propagates             motion attribute is high dynamic or low dynamic.
                                                                           k                                  k
the motion probability of keypoints in real time to eliminate        • Ki - The static probability of Pi , which is in the update
the influence of dynamic objects in SLAM. DS-SLAM [4]                   state and participates in camera pose optimization.
                                                                           Dk     Tk      Fk
uses SegNet [23] to obtain semantic information, combines            • Ki , Ki , Ki           - The static probability of Pik obtained
sparse optical flow and motion consistency detection to judge           by the DBSCAN clustering algorithm, the projection
people’s dynamic and static attributes. Dyna-SLAM [5] com-              constraints and the epipolar constraints respectively.
                                                                           k
bines mask R-CNN [24] and multi view geometry to process             • Mi− - The static probability of the map point forming a
moving objects. Brasch et al. [6] present monocular SLAM                matching relationship with Pik .
approach for highly dynamic environments which models
dynamic outliers with a joint probabilistic model based on         B. System Architecture
semantic prior information predicted by a CNN. With the help         The overview of CFP-SLAM is demonstrated in Fig.1.
of the initial segmentation results, Wang et al. [7] extract       Based on ORB-SLAM2 [13], we design a complete static
the accurate pose from the rough pose by identifying and           probability calculation and update framework of keypoints
processing the moving object and possible moving object            based on multiple constraints to deal with the influence of
respectively, and further help to make up for the error and        moving objects in dynamic environment. The system obtains
boundary inaccuracy of the segmentation area. Dynamic-             semantic information based on YOLOv5, compensates for
SLAM [3] compensates SSD for missed detection based on the         missed detection based on EKF and Hungarian algorithm,
speed invariance of adjacent frames, and eliminates dynamic        and then the box between adjacent frames is associated. In
Fig. 1. The overview of CFP-SLAM. The green portion and the purple portion are the input and output modules of the system respectively. The yellow
portion is the semantic module, including object detection, missed detection compensation, and data association. The orange portion and the blue portion are
static probability calculation modules for two stages of keypoints, respectively. In the first stage, the rough static probability of keypoints is calculated based
on the static probability of objects and the results of DBSCAN clustering. In the second stage, based on the epipolar constraint and projection constraint, and
considering the static probability of the object and the data association result of the box, the accurate static probability of feature points is calculated. During
the whole process, the static probability of the map points is maintained and updated, and together with the static probability of the keypoints will be used as
weight to participate in pose optimization.

Fk , only calculate and update the static probability of the                        is adopted to compensate the missed detection result. After
keypoints inside the potential moving object box. Firstly, the                      missed detection compensation, EKF and Hungarian algorithm
static probability of potential moving object Oik+ is obtained                      are used again for inter frame data association of boxes.
by using the optical flow and the epipolar constraints, and the
                                                                                    B. Static Probability of Objects
object is divided into high dynamic object and low dynamic
object. Initialize Kik as the static probability of the object                         When calculating the static probability of each potential
to which the keypoint belongs. Then, foreground points and                          moving object, we use the idea of DS-SLAM [4] for reference
background points is distinguished and the KiDk is calculated                       to solve the fundamental matrix LFk,k−1 and get the polar
                                                                                             F
by using the DBSCAN clustering results, and the Kik is                              error Ldi k,k−1 . We use the epipolar constraints and chi-square
updated to estimate the camera pose in the first stage to obtain                    distribution to test the epipolar error. Since the pixel coordi-
Tk,w . Next, KiT k , KiF k are obtained by using the projection                     nates of the matching point pair obtained by the optical flow
constraints and the epipolar constraints, Kik and Mik− are                          tracking have k = 2 degrees of freedom, if they are assumed
updated to participate in camera pose optimization as weights                       to follow the Gauss Distribution N (0, 1), then according to
to obtain a more accurate Tk,w .                                                    the chi-square distribution:
                                                                                                               ( (k/2−1) −x/2
                  IV. S PECIFIC IMPLEMENTATION                                                                     x       e
                                                                                                                     2k/2 Γ( k
                                                                                                                                ,x > 0
                                                                                                 chsq(x; k) =                2)                  (1)
A. Missed Detection Compensation Algorithm                                                                               0, x ≤ 0
   When processing dynamic objects, if the semantic informa-                           The definition of the function Γ(v) is:
tion as a priori is suddenly missing in some frames, on the one                                            Z ∞
hand, the subsequent methods based on semantic priors will                                         Γ(v) =       e−t tv−1 dt, Re v > 0                           (2)
                                                                                                                  0
not be able to process dynamic objects. On the other hand,
the sudden emergence of dynamic objects in high dynamic                                The single estimation result of Oik+ can be obtained:
scenes will lead to a sharp increase in the number of keypoints                                                              2 
                                                                                                                        F
                                                                                                  Oik+ m = chsq
                                                                                                       
incorrectly matched between adjacent frames, which leads to                                                           Ldi k,k−1 ; 2                             (3)
the loss of tracking in SLAM system in high dynamic scenario.
Therefore, stable and accurate semantic information is critical.                       After all estimation results are obtained by using all optical
   In order to solve the missed detection problem of YOLOv5,                        flow point pairs belonging to the object, all estimation results
we introduce EKF and Hungarian algorithm to compensate the                          are sorted from small to large. Let the number of all estimation
missed detection of potential moving objects. EKF is used to                        results be M , and take the average value of (Oik+ )m at
predict the boxes of potential moving objects in Fk , while the                     0.1M, 0.2M, 0.3M position after ranking as the estimated
Hungarian algorithm is used to correlate the predicted boxes                        value of object static probability Oik+ .
with the boxes detected by YOLOv5. If the predicted box does                           According to the calculation result of the static probability
not find a matching detected box, it could be considered that                       of the object and the real motion of the object, and taking
Fk has missed detection, and the prediction result of EKF                           into account that the negative effect of the dynamic point is
generally greater than the positive effect of the increase of          with the keypoints in Fk−1 , is calculated precisely based on
the static constraint when the camera pose is estimated, we            the projection constraints and the epipolar constraints.
set OT h = 0.9, the object motion attributes are divided into
high dynamic and low dynamic, which are provided to the                D. Static Probability of Keypoints in the Second Stage
subsequent methods as a priori information for processing with
different strategies. The static probability of all keypoints in          1) Static Probability Based on the Projection Con-
the box of the potential moving object is initialized to Oik+ ,        straints: Convert the Pik−1
                                                                                               ∗   from the pixel coordinate to the
and the static probability of other keypoints is initialized to        camera coordinate:
1.0.                                                                                                      1 k−1 ]
                                                                                           Pik−1
                                                                                             ∗   =         Z ∗ P k−1
                                                                                                                  ∗                             (6)
                                                                                               k−1        K ik−1 iuν
C. Static Probability of Keypoints in the First Stage
                                                                          Transform and project Pik−1
                                                                                                    ∗   to Fk , and the Euclidean
   1) DBSCAN Density Clustering Algorithm: Compared                                                 k−1

with semantic segmentation methods, object detection technol-          distance between the projection point and Pik is:
ogy has great advantages in real-time, but it can not provide
accurate object mask. In the indoor dynamic SLAM scene, this
problem leads to numerous static backgrounds in the boxes                                            1
                                                                        dTi = Pikuv −                              K Tk,k−1 P]
                                                                                                                             k−1
                                                                                                                             i∗    k−1
classified as people, and the false deletion of static keypoints                          Tk,k−1 P]
                                                                                                  k−1
                                                                                                  i∗
will reduce the constraints of camera pose optimization and                                              k−1
                                                                                                               Z                         XY Z uν 2
reduce the accuracy of camera pose estimation. We noticed                                                                              (7)
that people as the foreground as a non-rigid body, his depth              Where function |P |Z represents the z-axis coordinate of
has a good continuity, and usually has a large fault with the          point P , and |P |XY Z represents the non-homogeneous co-
background depth. To this end, we use the DBSCAN density               ordinate form of point P . On the premise that the camera
clustering algorithm to distinguish between the foreground and         pose Tk,w is relatively accurate, the greater dTi , the greater the
background points of boxes classified as people.                       possibility that Pik and Pik−1
                                                                                                   ∗    are mismatched. Based on this
   We adaptively determine eps (the neighborhood radius of             principle, we design a static probability model based on the
DBSCAN density clustering algorithm) and minP ts (the                  projection constraints. After sorting the dTi of all keypoints
threshold of the number of samples in the neighborhood).               outside the box of the dynamic object in Fk from small to
After clustering, the one with the lowest average value of             large, take dTi at the truncated position of 0.8 as the adaptive
samples in cluster C = {C1 , C2 , · · · , Ck } is taken as the         threshold DTT h of the projection error, and obtain the minimum
foreground points of box.                                              value dTmin of dTi . We use the Sigmoid function form to
   After getting the DBSCAN clustering results, we adopt               measure the static probability of keypoints of the matching
a soft strategy to further estimate the static probability of          relationship in the box:
background points in the box of a potential moving object.
Obviously, the static probability of background points must be                                                     1
                                                                                     KiT k =                                                    (8)
                                                                                               1 + e(    dT            )×
                                                                                                              T
greater than that of the object, and it is positively correlated                                          i −DT h              5
                                                                                                                             T −dT
                                                                                                                            DT
with the static probability of the object. Specifies that the static                                                           h min

probability of background points derived from the DBSCAN                 For a pair of matching points, the satisfaction of the
cluster is:                                                            projection constraints is not only related to whether the
                  (
                      1−OT h
                                       3
                                    Kik + 1, Oik+ ≤ OT h               corresponding spatial points strictly meet the static environ-
            Dk                 4
          Ki =        (O T h )                                   (4)   ment assumption, but also directly related to the number of
                                  1
                                 Kk
                                     , Oik+ > OT h
                               i                                       constraints when solving the pose matrix and whether the
  Considering that the static probability estimation of key-           pose matrix itself is correctly solved. Therefore, the statistical
points has not been strictly calculated at each point, in other        confidence CsT k and calculation confidence CcT k of the pose
words, the static probability of the keypoints is coarse at            matrix are introduced:
present, and the camera pose estimation is vulnerable to
dynamic points, we set the static probability of all foreground                                                    1
                                                                                        CST k =                                                 (9)
points in the box of high dynamic objects to 0.                                                   1 + e−NBA +0.5T hBA
  2) First Stage Pose Optimization: Update the static prob-                                                      P T
ability of keypoints:                                                                       Tk                     di
                                                                                           CC  =1−                                             (10)
                        Kik = Kik × KiDk                       (5)                                             NT × DTT h
   When initializing the SLAM system, map points will be
                                                                          Where NBA is the number of interior points obtained by
created. At this time, the static probability of map point Mik−
                                                                       participating in the last camera pose solution, and threshold
will be initialized to the static probability of corresponding
                                                                       T hBA is the minimum number of interior points required
keypoint Kik . In the frame after initialization, Kik and Mik− are                                                             P T
                                                                       to participate in the camera pose solution, NT and        di
used as weights to optimize the camera pose, and the camera
                                                                       respectively represent the number of all sample points and
pose estimation value Tk,w in the first stage is obtained. Then,
                                                                       the sum of dTi satisfying dTi < DTT h .
the static probability of Pik , which has a matching relation
  2) Static Probability Based on the Epipolar Constraints:                       After missed detection compensation, we use EKF and
Based on the camera pose estimation Tk,w in the first stage,                  Hungarian algorithm to correlate the boxes of potential moving
a more accurate fundamental matrix can be calculated:                         objects between adjacent frames. It is easy to know that if the
                                              ∧
                                                                              association result of a box in Fk is not found in Fk−1 , even if
           Fk,k−1 = K−T (tk,k−1 ) Rk,k−1 K−1             (11)                 there is a matching relationship between the foreground points
                                    T                                       in the box, it is generally a false matching, so let Kik = 0 in
  The pole line lik = Aki , Bik , Cik corresponding to Pik is:                this case. For Pik that does not match the keypoints in Fk−1 ,
                                                                              according to the results of DBSCAN clustering, if Pik belongs
                          lik = Fk,k−1 P]
                                        k−1
                                        i∗                           (12)
                                         uv                                   to the foreground points, let Kik = 0, else let Kik = Mik− .
  Then the polar error dF                                                     After the second estimation result of Kik is obtained, Mik− is
                        i is:
                                                                              updated. When Mik− < 0.3, delete the map point. Then Kik
                                            T                               and Mik− are used as weights to participate in the second stage
                                       k
                                      Pg
                                       iuv        lik
                                                                              of camera pose optimization. When there is a big difference
                      dF
                       i = q         2               2             (13)     between Kik and Mik− , it can be considered that Kik and Mik−
                                  Aki +           Bik                         are mismatched and do not participate in optimization.
   Similar to the projection constraints, we calculate static                                  V. E XPERIMENTS AND R ESULTS
probability and confidence based on the epipolar constraints
to obtain KiF k , the statistical confidence CsF k and calculation               In this section, we test the performance of the proposed
confidence CcF k of the fundamental matrix.                                   algorithm in 8 dynamic sequences of the TUM RGB-D dataset
   It should be noted that, as Eq.11 mentioned, the fundamental               [26], including 4 low dynamic sequences (fr3/s for short) and
matrix can not be obtained when the camera translation is                     4 high dynamic sequences (fr3/w for short), and the camera
not large enough. Therefore, when the camera translation is                   includes 4 kinds of motion: static, xyz, halfsphere and rpy. The
less than the set threshold tT h , skip the calculation of static             indicators used to evaluate the accuracy are the Absolute Tra-
probability and confidence based on the epipolar constraints,                 jectory Error (ATE) and the Relative Pose Error (RPE). ATE
that is:                                                                      represents the global consistency of trajectory. RPE includes
                                                                              translation drift and rotation drift. The Root-Mean-Square-
   KiF k = 0, CSF k = CC
                       Fk
                          =0             s. t. ktk,k−1 k2 ≤ tT h     (14)     Error (RMSE) and Standard Deviation (S.D.) of both are used
                                                                              to represent the robustness and stability of the system [12].
   3) Second Stage Pose Optimization: After calculating the                   Firstly, we show the effect of missed detection compensation
static probability of the keypoints based on the projection                   and DBSCAN clustering, then compare our method with some
constraints and the epipolar constraints, we update the static                of the most advanced methods, then design a series of ablation
probability of Pik which matches the keypoints in Fk−1 for                    experiments to test the impact of each module, and finally
the second time. When the object is in high dynamics, the                     carry out real-time analysis. All the experiments are performed
negative impact of dynamic points on camera pose estimation                   on a computer with Intel i7 CPU, 3060 GPU, and 16GB
is generally greater than the positive impact of the increase                 memory.
in the number of static point constraints, which is just the
opposite when the object is in low dynamics. This is because                  A. Missed Detection Compensation and DBSCAN Clustering
ORB-SLAM2 has certain outlier suppression strategies, which                      In the dynamic SLAM scene, the motion of the object,
can suppress dynamic disturbances in low dynamics, but does                   the incomplete appearance of the object to be detected in the
not work in high dynamics. So, when Oik+ ≤ OT h ,                             camera field of view, the blurred image and the singular angle
                   Tk                                                        of view caused by camera rotation all bring severe challenges
             k      Ki × KiF k , ktk,k−1 k2 > tT h
          Ki =                                           (15)                 to the object detection, very easy to cause miss detection,
                       KiT k , ktk,k−1 k2 ≤ tT h
                                                                              even will lead to continuous frame miss detection. Fig.2(a)-
  when Oik+ > OT h ,                                                          (d) and Fig.2(e) show the results of missed detection com-
                                                                              pensation of object detection in the above four cases and six
            KiT k × CsT k CcT k         KiF k × CsF k CcF k                   consecutive frames, respectively. Fig.3 shows the DBSCAN
  Kik =                             +                                (16)
          CsT k CcT k + CsF k CcF k   CsT k CcT k + CsF k CcF k               clustering results after missed detection compensation. We

Fig. 2. Missed detection and the results of missed detection compensation in the following cases: (a) The rapid motion of the object. (b) The incomplete
appearance of the object to be detected in the camera field of view. (c) The blurred image. (d) The singular angle of view caused by camera rotation. (e)
Continuous frame miss detection.
Fig. 3. Effect of DBSCAN density clustering algorithm in two consecutive frames. The top set of images is taken every 8 frames, and the bottom set of
images is taken every 4 frames. The images contain three common states of movement: sitting in a chair, slow motion and fast motion. After clustering, the
foreground and background points are shown in red and green respectively.

select two consecutive frames to show the clustering effect.                   SLAM2. Without calculating the static probability of the ob-
The foreground points are marked with red and the background                   ject, we provide a lower performance version of the algorithm
points are marked with green. The upper image group contains                   in this paper with higher real-time performance, which is
two people sitting on the chair and moving slowly respectively,                called CFP-SLAM− . The quantitative comparison results are
and the people in the lower image group are in the fast walking                shown in Tables I, II and III, in which the best results are
state. It is worth noting from Fig.3 that many keypoints are                   highlighted in bold and the second-best are underlined. The
extracted from the edge of the person, which is generally the                  data of DS-SLAM, Dyna-SLAM, Blitz-SLAM and TRS comes
part with the highest dynamic attributes. However, semantic                    from the source literature, / indicates that the corresponding
segmentation is difficult to accurately judge the boundary of                  data is not provided in the source literature. The experimental
objects [12], which leads to the misjudgment of dynamic and                    results show that, unlike other dynamic SLAM algorithms,
static attributes of keypoints. We use DBSCAN algorithm to                     which only have advantages over ORB-SLAM2 in high dy-
cluster keypoints based on depth information, which can well                   namic scenarios, this algorithm can achieve almost the best
avoid this problem. The experimental results fully show the                    results in high dynamic and low dynamic scenarios. Even the
effectiveness and robustness of the missed detection compen-                   low-performance version we provide shows better performance
sation algorithm and clustering algorithm.                                     than other algorithms. In rpy sequences, on the one hand,
                                                                               the epipolar constraints cannot be used, on the other hand,
B. Comparison with State-of-the-arts
                                                                               the large change of camera angle leads to insufficient feature
  We contrast with ORB-SLAM2 [13] and forth most ad-                           matching, so our method performs slightly worse. The ATE
vanced dynamic SLAM methods, including DS-SLAM [4],                            and RPE plots of our algorithm on 8 sequences are shown in
Dyna-SLAM [5], Blitz-SLAM [12] and TRS [11]. Like our                          Fig.4.
method, these algorithms are all improved based on ORB-

                                                        Fig. 4.   ATE and RPE from CFP-SLAM.

                                                              TABLE I
                                        RESULTS OF METRICS ABSOLUTE TRAJECTORY ERROR (ATE)

                  ORB-SLAM2           Dyna-SLAM            DS-SLAM             Blitz-SLAM             TRS           CFP-SLAM−            CFP-SLAM
  Sequences
                 RMSE      S.D.     RMSE       S.D.     RMSE        S.D.     RMSE       S.D.     RMSE       S.D.   RMSE       S.D.     RMSE       S.D.
  fr3/s/xyz      0.0092   0.0047    0.0127    0.0060       /          /      0.0148    0.0069    0.0117      /     0.0129    0.0068    0.0090    0.0042
  fr3/s/half     0.0192   0.0110    0.0186    0.0086       /          /      0.0160    0.0076    0.0172      /     0.0159    0.0072    0.0147    0.0069
  fr3/s/static   0.0087   0.0042       /         /      0.0065     0.0033       /         /         /        /     0.0061    0.0029    0.0053    0.0027
  fr3/s/rpy      0.0195   0.0124       /         /         /          /         /         /         /        /     0.0244    0.0175    0.0253    0.0154
  fr3/w/xyz      0.7214   0.2560    0.0164    0.0086    0.0247     0.0161    0.0153    0.0078    0.0194      /     0.0149    0.0077    0.0141    0.0072
  fr3/w/half     0.4667   0.2601    0.0296    0.0157    0.0303     0.0159    0.0256    0.0126    0.0290      /     0.0235    0.0114    0.0237    0.0114
  fr3/w/static   0.3872   0.1636    0.0068    0.0032    0.0081     0.0036    0.0102    0.0052    0.0111      /     0.0069    0.0032    0.0066    0.0030
  fr3/w/rpy      0.7842   0.4005    0.0354    0.0190    0.4442     0.2350    0.0356    0.0220    0.0371      /     0.0411    0.0257    0.0368    0.0230
                                                               TABLE II
                                             RESULTS OF METRIC TRANSLATIONAL DRIFT (RPE)

                  ORB-SLAM2           Dyna-SLAM          DS-SLAM          Blitz-SLAM              TRS             CFP-SLAM−            CFP-SLAM
 Sequences
                RMSE       S.D.     RMSE      S.D.    RMSE      S.D.    RMSE      S.D.    RMSE          S.D.     RMSE       S.D.     RMSE       S.D.
 fr3/s/xyz      0.0117    0.0060    0.0142   0.0073      /        /     0.0144   0.0071   0.0166          /      0.0149    0.0081    0.0114    0.0055
 fr3/s/half     0.0231    0.0163    0.0239   0.0120      /        /     0.0165   0.0073   0.0259          /      0.0214    0.0099    0.0162    0.0079
 fr3/s/static   0.0090    0.0043       /        /     0.0078   0.0038      /        /        /            /      0.0078    0.0034    0.0072    0.0035
 fr3/s/rpy      0.0245    0.0144       /        /        /        /        /        /        /            /      0.0322    0.0217    0.0316    0.0186
 fr3/w/xyz      0.3944    0.2964    0.0217   0.0119   0.0333   0.0229   0.0197   0.0096   0.0234          /      0.0196    0.0099    0.0190    0.0097
 fr3/w/half     0.3480    0.2859    0.0284   0.0149   0.0297   0.0152   0.0253   0.0123   0.0423          /      0.0274    0.0130    0.0259    0.0128
 fr3/w/static   0.2349    0.2151    0.0089   0.0044   0.0102   0.0048   0.0129   0.0069   0.0117          /      0.0092    0.0043    0.0089    0.0040
 fr3/w/rpy      0.4582    0.3447    0.0448   0.0262   0.1503   0.1168   0.0473   0.0283   0.0471          /      0.0540    0.0350    0.0500    0.0306

                                                               TABLE III
                                               RESULTS OF METRIC ROTATIONAL DRIFT (RPE)

                  ORB-SLAM2           Dyna-SLAM          DS-SLAM          Blitz-SLAM              TRS             CFP-SLAM−            CFP-SLAM
 Sequences
                RMSE       S.D.     RMSE      S.D.    RMSE      S.D.    RMSE      S.D.    RMSE          S.D.     RMSE       S.D.     RMSE       S.D.
 fr3/s/xyz      0.4890    0.2713    0.5042   0.2651      /        /     0.5024   0.2634   0.5968          /      0.5126    0.2793    0.4875    0.2640
 fr3/s/half     0.6015    0.2924    0.7045   0.3488      /        /     0.5981   0.2739   0.7891          /      0.7697    0.3718    0.5917    0.2834
 fr3/s/static   0.2850    0.1241       /        /     0.2735   0.1215      /        /        /            /      0.2749    0.1192    0.2654    0.1183
 fr3/s/rpy      0.7772    0.3999       /        /        /        /        /        /        /            /      0.8303    0.4653    0.7410    0.3665
 fr3/w/xyz      7.7846    5.8335    0.6284   0.3848   0.8266   0.5826   0.6132   0.3348   0.6368          /      0.6204    0.3850    0.6023    0.3719
 fr3/w/half     7.2138    5.8299    0.7842   0.4012   0.8142   0.4101   0.7879   0.3751   0.9650          /      0.7853    0.3821    0.7575    0.3743
 fr3/w/static   4.1856    3.8077    0.2612   0.1259   0.2690   0.1182   0.3038   0.1437   0.2872          /      0.2535    0.1130    0.2527    0.1051
 fr3/w/rpy      8.8923    6.6658    0.9894   0.5701   3.0042   2.3065   1.0841   0.6668   1.0587          /      1.0521    0.5577    1.1084    0.6722

                                                      TABLE IV
                  RESULTS OF METRICS ABSOLUTE TRAJECTORY ERROR (ATE) WITH DIFFERENT CONFIGURATIONS

                           CFP-SLAM           CFP-SLAM−          W/O-MDC            W/O-DBS                   W/O-KSP         Only-YOLO
          Sequences
                         RMSE       S.D.     RMSE      S.D.    RMSE      S.D.    RMSE      S.D.         RMSE       S.D.     RMSE       S.D.
          fr3/s/xyz      0.0090    0.0042    0.0129   0.0068   0.0123   0.0066   0.0130   0.0060        0.0142    0.0063    0.0174    0.0079
          fr3/s/half     0.0147    0.0069    0.0159   0.0072   0.0150   0.0074   0.0305   0.0179        0.0201    0.0089    0.0281    0.0158
          fr3/s/static   0.0053    0.0027    0.0061   0.0029   0.0055   0.0025   0.0064   0.0030        0.0062    0.0030    0.0064    0.0027
          fr3/s/rpy      0.0253    0.0154    0.0244   0.0175   0.0237   0.0149   0.0297   0.0205        0.0287    0.0195    0.0460    0.0332
          fr3/w/xyz      0.0141    0.0072    0.0149   0.0077   0.0158   0.0079   0.0159   0.0081        0.0154    0.0076    0.0165    0.0082
          fr3/w/half     0.0237    0.0114    0.0235   0.0114   0.0258   0.0134   0.0274   0.0137        0.0307    0.0151    0.0310    0.0165
          fr3/w/static   0.0066    0.0030    0.0069   0.0032   0.0070   0.0031   0.0078   0.0033        0.0076    0.0033    0.0073    0.0032
          fr3/w/rpy      0.0368    0.0230    0.0411   0.0257   0.1910   0.1594   0.0749   0.0536        0.0405    0.0211    0.0456    0.0312

C. Ablation Experiment                                                    especially in w/rpy, when the camera and objects are moving
                                                                          violently. In fact, the tracking is often lost in w/xyz, w/half and
   In order to prove the function of each module of our                   w/rpy because of missed detection. W/O-DBS and W/O-KSP
algorithm, We design a series of ablation experiments, and                show general performance in all sequences, which illustrates
the experimental results are shown in Table IV. Among                     the effectiveness of DBSCAN clustering and the limitation of
them, CFP-SLAM: The algorithm of this paper; CFP-SLAM− :                  dealing with non-rigid bodies with partial motion as a whole,
Do not use static probability of objects; W/O-MDC: With-                  respectively. Only-YOLO encounters difficulties in initializa-
out missed detection compensation; W/O-DBS: Without DB-                   tion due to insufficient features in almost all sequences, and
SCAN clustering; W/O-KSP: Without the static probability                  tracking is lost in some sequences.
of keypoints, that is, all the foreground points after missed
detection compensation and DBSCAN clustering are directly                 D. Real-time Analysis
eliminated; Only-YOLO: Directly eliminate all keypoints in                  Real-time performance is one of the important evaluation
the box with human category.                                              indexes of SLAM system. We test the average running time of
   The experimental results show that CFP-SLAM− shows                     each module, as shown in Table V. EKF represents the missed
worse performance in low dynamic scenes, because we cannot                detection compensation and data association of boxes module,
distinguish between high dynamic objects and low dynamic                  OSP represents the static probability calculation module of
objects, so all objects are processed according to high dy-               objects, and KSP represents the static probability calculation
namic. W/O-MDC is almost unaffected in low dynamic scenes,                module of keypoints based on the epipolar constraints and the
but the performance is very poor in high dynamic scenes,                  projection constraints. Semantic threads based on YOLOv5s
run in parallel with ORB feature extraction. The results show                 [12] Y. Fan, Q. Zhang, Y. Tang, S. Liu, and H. Han, “Blitz-slam: A
that the average processing time per frame for the main                            semantic slam in dynamic environments,” Pattern Recognition, vol. 121,
                                                                                   p. 108225, 2022.
threads of CFP-SLAM and CFP-SLAM− is 42.7 ms and                              [13] R. Mur-Artal and J. D. Tardós, “Orb-slam2: An open-source slam
24.77 ms, that is, the running speed reaches 23 Fps and 40                         system for monocular, stereo, and rgb-d cameras,” IEEE transactions
Fps respectively. Compared with the SLAM system based                              on robotics, vol. 33, no. 5, pp. 1255–1262, 2017.
                                                                              [14] S. Li and D. Lee, “Rgb-d slam in dynamic environments using static
on semantic segmentation, it can better meet the real-time                         point weighting,” IEEE Robotics and Automation Letters, vol. 2, no. 4,
requirements while ensure the accuracy.                                            pp. 2263–2270, 2017.
                                                                              [15] Y. Sun, M. Liu, and M. Q.-H. Meng, “Improving rgb-d slam in dynamic
                       TABLE V                                                     environments: A motion removal approach,” Robotics and Autonomous
                                                                                   Systems, vol. 89, pp. 110–122, 2017.
       THE AVERAGE RUNNING TIME OF EACH MODULE.                               [16] ——, “Motion removal for reliable rgb-d slam in dynamic environ-
    Methods       YOLO      EKF    OSP     DBSCAN      KSP    Tracking             ments,” Robotics and Autonomous Systems, vol. 108, pp. 115–128, 2018.
   CFP-SLAM       12.44     0.07   17.93     1.76      3.66     42.7          [17] R. Scona, M. Jaimez, Y. R. Petillot, M. Fallon, and D. Cremers, “Stat-
   CFP-SLAM-      12.44     0.07     /       1.76      3.66    24.77               icfusion: Background reconstruction for dense rgb-d slam in dynamic
                                                                                   environments,” in 2018 IEEE International Conference on Robotics and
                                                                                   Automation (ICRA). IEEE, 2018, pp. 3849–3856.
                          VI. C ONCLUSION                                     [18] G. Liu, W. Zeng, B. Feng, and F. Xu, “Dms-slam: A general visual
                                                                                   slam system for dynamic scenes with multiple sensors,” Sensors, vol. 19,
   In this paper, we propose a dynamic scene-oriented visual                       no. 17, p. 3714, 2019.
SLAM algorithm based on YOLOv5s and coarse-to-fine static                     [19] J. Bian, W.-Y. Lin, Y. Matsushita, S.-K. Yeung, T.-D. Nguyen, and M.-M.
                                                                                   Cheng, “Gms: Grid-based motion statistics for fast, ultra-robust feature
probability. After missed detection compensation and key-                          correspondence,” in Proceedings of the IEEE conference on computer
points clustering, the static probabilities of objects, keypoints                  vision and pattern recognition, 2017, pp. 4181–4190.
and map points are calculated and updated as weights to                       [20] D.-H. Kim and J.-H. Kim, “Effective background model-based rgb-d
                                                                                   dense visual odometry in a dynamic environment,” IEEE Transactions
participate in pose optimization. Extensive evaluation shows                       on Robotics, vol. 32, no. 6, pp. 1565–1573, 2016.
that our algorithm achieves the highest accuracy of localization              [21] W. Dai, Y. Zhang, P. Li, Z. Fang, and S. Scherer, “Rgb-d slam in dynamic
in almost all low dynamic and high dynamic scenes, and has                         environments using point correlations,” IEEE Transactions on Pattern
                                                                                   Analysis and Machine Intelligence, 2020.
quite high real-time performance. In the future, we intend to                 [22] T. Zhang, H. Zhang, Y. Li, Y. Nakamura, and L. Zhang, “Flowfusion:
build a lightweight plane and object map containing only static                    Dynamic dense rgb-d slam based on optical flow,” in 2020 IEEE
environment for robot navigation and augmented reality.                            International Conference on Robotics and Automation (ICRA). IEEE,
                                                                                   2020, pp. 7322–7328.
                                                                              [23] V. Badrinarayanan, A. Kendall, and R. Cipolla, “Segnet: A deep con-
                             R EFERENCES                                           volutional encoder-decoder architecture for image segmentation,” IEEE
                                                                                   transactions on pattern analysis and machine intelligence, vol. 39,
 [1] M. R. U. Saputra, A. Markham, and N. Trigoni, “Visual slam and                no. 12, pp. 2481–2495, 2017.
     structure from motion in dynamic environments: A survey,” ACM            [24] K. He, G. Gkioxari, P. Dollár, and R. Girshick, “Mask r-cnn,” in
     Computing Surveys (CSUR), vol. 51, no. 2, pp. 1–36, 2018.                     Proceedings of the IEEE international conference on computer vision,
 [2] F. Zhong, S. Wang, Z. Zhang, and Y. Wang, “Detect-slam: Making                2017, pp. 2961–2969.
     object detection and slam mutually beneficial,” in 2018 IEEE Winter      [25] N. Dvornik, K. Shmelkov, J. Mairal, and C. Schmid, “Blitznet: A real-
     Conference on Applications of Computer Vision (WACV). IEEE, 2018,             time deep network for scene understanding,” in Proceedings of the IEEE
     pp. 1001–1010.                                                                international conference on computer vision, 2017, pp. 4154–4162.
 [3] L. Xiao, J. Wang, X. Qiu, Z. Rong, and X. Zou, “Dynamic-slam:            [26] J. Sturm, N. Engelhard, F. Endres, W. Burgard, and D. Cremers, “A
     Semantic monocular visual localization and mapping based on deep              benchmark for the evaluation of rgb-d slam systems,” in 2012 IEEE/RSJ
     learning in dynamic environment,” Robotics and Autonomous Systems,            international conference on intelligent robots and systems. IEEE, 2012,
     vol. 117, pp. 1–16, 2019.                                                     pp. 573–580.
 [4] C. Yu, Z. Liu, X.-J. Liu, F. Xie, Y. Yang, Q. Wei, and Q. Fei, “Ds-
     slam: A semantic visual slam towards dynamic environments,” in 2018
     IEEE/RSJ International Conference on Intelligent Robots and Systems
     (IROS). IEEE, 2018, pp. 1168–1174.
 [5] B. Bescos, J. M. Fácil, J. Civera, and J. Neira, “Dynaslam: Tracking,
     mapping, and inpainting in dynamic scenes,” IEEE Robotics and Au-
     tomation Letters, vol. 3, no. 4, pp. 4076–4083, 2018.
 [6] N. Brasch, A. Bozic, J. Lallemand, and F. Tombari, “Semantic monoc-
     ular slam for highly dynamic environments,” in 2018 IEEE/RSJ Inter-
     national Conference on Intelligent Robots and Systems (IROS). IEEE,
     2018, pp. 393–400.
 [7] K. Wang, Y. Lin, L. Wang, L. Han, M. Hua, X. Wang, S. Lian, and
     B. Huang, “A unified framework for mutual improvement of slam and
     semantic segmentation,” in 2019 International Conference on Robotics
     and Automation (ICRA). IEEE, 2019, pp. 5224–5230.
 [8] X. Yuan and S. Chen, “Sad-slam: A visual slam based on semantic
     and depth information,” in 2020 IEEE/RSJ International Conference on
     Intelligent Robots and Systems (IROS). IEEE, 2020, pp. 4930–4935.
 [9] J. Vincent, M. Labbé, J.-S. Lauzon, F. Grondin, P.-M. Comtois-Rivet,
     and F. Michaud, “Dynamic object tracking and masking for visual slam,”
     in 2020 IEEE/RSJ International Conference on Intelligent Robots and
     Systems (IROS). IEEE, 2020, pp. 4974–4979.
[10] A. Li, J. Wang, M. Xu, and Z. Chen, “Dp-slam: A visual slam
     with moving probability towards dynamic environments,” Information
     Sciences, vol. 556, pp. 128–142, 2021.
[11] T. Ji, C. Wang, and L. Xie, “Towards real-time semantic rgb-d slam
     in dynamic environments,” in 2021 IEEE International Conference on
     Robotics and Automation (ICRA). IEEE, 2021, pp. 11 175–11 181.
