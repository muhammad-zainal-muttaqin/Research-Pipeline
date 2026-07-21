---
source_id: 117
bibtex_key: xu2024onboard
title: Onboard Dynamic-Object Detection and Tracking for Autonomous Robot Navigation with RGB-D Camera
year: 2024 (versi arXiv pertama 2023)
domain_theme: YOLO plus RGB-D
verified_pdf: 117_Onboard Dynamic-Object Detection (Xu dkk.).pdf
char_count: 58644
---

IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED NOVEMBER, 2023                                                                     1

                                          Onboard dynamic-object detection and tracking for
                                          autonomous robot navigation with RGB-D camera
                                                         Zhefan Xu*, Xiaoyang Zhan*, Yumeng Xiu, Christopher Suzuki, and Kenji Shimada

                                            Abstract—Deploying autonomous robots in crowded indoor
                                         environments usually requires them to have accurate dynamic
                                         obstacle perception. Although plenty of previous works in the
arXiv:2303.00132v4 [cs.RO] 23 Nov 2023

                                         autonomous driving field have investigated the 3D object de-
                                         tection problem, the usage of dense point clouds from a heavy
                                         Light Detection and Ranging (LiDAR) sensor and their high
                                         computation cost for learning-based data processing make those
                                         methods not applicable to small robots, such as vision-based
                                         UAVs with small onboard computers. To address this issue, we
                                         propose a lightweight 3D dynamic obstacle detection and tracking
                                         (DODT) method based on an RGB-D camera, which is designed
                                         for low-power robots with limited computing power. Our method
                                         adopts a novel ensemble detection strategy, combining multiple
                                         computationally efficient but low-accuracy detectors to achieve
                                         real-time high-accuracy obstacle detection. Besides, we introduce
                                         a new feature-based data association and tracking method to
                                         prevent mismatches utilizing point clouds’ statistical features.
                                         In addition, our system includes an optional and auxiliary
                                         learning-based module to enhance the obstacle detection range
                                         and dynamic obstacle identification. The proposed method is                  Fig. 1. The onboard dynamic obstacle detection results from the proposed
                                         implemented in a small quadcopter, and the results show that                 DODT algorithm. (a) The camera RGB view. (b) An example of an au-
                                         our method can achieve the lowest position error (0.11m) and                 tonomous robot with an RGB-D camera. (c) The onboard 3D dynamic obstacle
                                         a comparable velocity error (0.23m/s) across the benchmarking                detection results shown as blue bounding boxes with point clouds.
                                         algorithms running on the robot’s onboard computer. The flight
                                         experiments prove that the tracking results from the proposed
                                                                                                                      the development of a lightweight RGB-D camera-based dy-
                                         method can make the robot efficiently alter its trajectory for
                                         navigating dynamic environments. Our software is available on                namic obstacle detection and tracking method is necessary for
                                         GitHub1 as an open-source ROS package.                                       autonomous robots operating in dynamic environments.
                                            .                                                                            There are three challenges in small mobile robots’ detection
                                           Index Terms—RGB-D Perception, Vision-Based Navigation,                     and tracking. First, small mobile robots’ onboard computation
                                         Visual Tracking, 3D Object Detection, Collision Avoidance                    resources are limited, making GPU-demanding learning-based
                                                                                                                      methods [1][2] not applicable. Note that we define small
                                                                                                                      mobile robots as those with weights below 1.5kg, equipped
                                                                  I. I NTRODUCTION
                                                                                                                      with low-power (10-20Watts) onboard computers measuring
                                             MALL autonomous mobile robots, frequently employed
                                         S   in indoor scenarios, often operate in dynamic and un-
                                         predictable environments populated by humans, vehicles, and
                                                                                                                      around 10cm in length, shown in Fig. 1b. Second, the range
                                                                                                                      and field of view (FOV) of depth cameras suited for small
                                                                                                                      mobile robots are limited, which makes obstacles either too
                                         other robots. Ensuring safe navigation in such settings ne-                  close or too far and thus not detectable. For example, the
                                         cessitates real-time, accurate perception of dynamic obstacles.              ideal depth range of the popular Intel RealSense D435i depth
                                         However, many small robots are only equipped with onboard                    camera is from 0.3m to 3.0m. This camera limitation makes
                                         computers with limited computational capabilities and rely on                some previous works [3][4] only capable of tracking obstacles
                                         RGB-D cameras. This makes GPU-intensive learning-based                       in the short range. Third, the noises from the depth value
                                         methods, common in autonomous driving, unsuitable. Hence,                    estimation of the camera are not negligible, especially for
                                                                                                                      those noise-sensitive non-learning methods [5][6]. The camera
                                           *The authors contributed equally.                                          noises can make the detection algorithm not only estimate
                                           Manuscript received: July 4 2023; Revised: October 1 2023; Accepted:
                                         November 11 2023.                                                            obstacle states inaccurately but also produce high-frequency
                                           This paper was recommended for publication by Editor Pascal Vasseur upon   false-positive and false-negative results, leading to confusion
                                         evaluation of the Associate Editor and Reviewers’ comments.                  for obstacle avoidance planners.
                                           Zhefan Xu, Xiaoyang Zhan, Yumeng Xiu, Christopher Suzuki, and
                                         Kenji Shimada are with the Department of Mechanical Engineering,               To solve these issues, this paper presents an onboard 3D
                                         Carnegie Mellon University, 5000 Forbes Ave, Pittsburgh, PA, 15213, USA.     dynamic obstacle detection and tracking (DODT) method
                                         zhefanx@andrew.cmu.edu
                                           Digital Object Identifier (DOI): see top of this page.                     based on an RGB-D camera. In contrast to other low-
                                           1 https://github.com/Zhefan-Xu/onboard detector                            computational algorithms [3][4][6], which employ a single
2                                                 IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED NOVEMBER, 2023

detector, we propose a novel ensemble detection strategy            Logoglu et al. [18] combine the 3-image-difference technique
combining multiple computationally efficient but low-accuracy       with epipolar constraints to determine dynamic obstacles. They
detectors to obtain fast and more accurate obstacle detection       extend their approach by utilizing scene flow, an extension
results. Moreover, the proposed method incorporates feature-        of optical flow, in [19] [20], for detecting the velocity of
based data association, utilizing statistical features from point   each pixel and identifying dynamic points. Some alternative
clouds, and employs the Kalman filter for obstacle tracking.        methods focus on detecting and segmenting dynamic obsta-
This approach reduces tracking mismatches that can occur            cles in 2D image planes to enhance SLAM robustness. In
with the center-distance-based association methods employed         [17][21][22][23], these approaches concentrate on removing
by benchmarking algorithms. Then, we use both point cloud           dynamic obstacles from images to mitigate estimation errors,
and velocity criteria to identify dynamic obstacles. Finally,       while Qiu et al. [24] detect pedestrian skeletons to improve
the system introduces a novel usage for the learning-based          SLAM optimization.
detector as an auxiliary and optional module to enhance the            Point cloud-based methods: Unlike image-based methods,
detection range and dynamic obstacle identification when the        point cloud-based approaches directly detect 3D obstacles
robot’s computation resources are enough. The contributions         using geometric information from point clouds. In [3], a
of this work are:                                                   point cloud clustering method is combined with the YOLO
   • Efficient Ensemble Detection: Different from other             detector for human detection. Wang et al. [4] employ a sim-
     detection and tracking algorithms designed for low-            ilar clustering-based detection approach for indoor dynamic
     computational robots with a single detector, the proposed      obstacle avoidance using a quadcopter. To enhance obstacle
     algorithm runs multiple computationally efficient and          tracking robustness, Chen et al. [5] propose using point cloud
     low-accuracy detectors with a novel ensemble strategy          feature vectors and object track points to identify correct object
     to obtain more accurate results with high efficiency.          matches and estimate their states. In [25], a KD-Tree map is
   • Feature-based Association and Tracking: Unlike the             directly constructed from the LiDAR point cloud for dynamic
     traditional center-distance-based association methods in       obstacle avoidance. Min et al. [26] represent dynamic obstacles
     other algorithms, the feature-based association reduces        in a dynamic occupancy map and employ kernel inference
     tracking mismatches by utilizing statistical features from     to reduce computation. Likewise, in [27], a dual-structure
     point clouds, improving the tracking accuracy.                 particle-based dynamic occupancy map is utilized to represent
   • Auxiliary Learning-based Detection Module: The sys-            dynamic environments and classify obstacle particles as static
     tem incorporates a novel integration of the learning-based     or dynamic.
     detector as an auxiliary module, enhancing the detection          Both image and point cloud methods can suffer from
     range and dynamic obstacle identification when the robot       misdetection due to noise and complex environments. To
     has sufficient computational resources.                        address this, we propose an ensemble method that leverages
                                                                    different detectors to mitigate their individual shortcomings.
                                                                    Additionally, we suggest using the learning-based method as
                     II. R ELATED W ORK
                                                                    an optional auxiliary module, enhancing adaptability for robots
   Among small robots with limited computational power, such        with varying computational resources.
as UAVs and small UGVs, the detection and tracking methods
can be categorized based on the sensors, including LiDARs                                III. M ETHODOLOGY
[7][8][9][10], event cameras [11][12], and RGB-D cameras
[3][4][6]. Among them, the RGB-D camera is one of the most          A. System Overview
popular sensors for small mobile robots, and there are mainly          Considering the payload and computational constraints of
two ways of using the RGB-D camera.                                 small mobile robots, both computational-intensive learning-
   Image-based methods: Most methods in this category               based 3D object detectors and heavy LiDAR systems become
leverage depth images for 3D obstacle detection. For instance,      impractical. To address this constraint, we have devised a
in [13], depth images are employed to generate U-depth maps         lightweight detection and tracking framework comprising three
and V-depth maps, enabling the estimation of obstacle states        core modules: the detection module, the tracking module, and
and proving safe navigation with static obstacles. Building on      the identification module, as shown in Fig. 2. The detec-
this, Lin et al. [14] adopt a similar U-depth map to detect         tion module comprises a non-learning and a learning-based
and track obstacles, representing them as 3D ellipsoids. To         component. The non-learning part employs depth images and
enhance the accuracy of obstacle dimension estimation, the          two non-learning detectors for generic obstacle detection.
restricted V-depth map is introduced in [15]. In [6], dynamic       Meanwhile, the learning-based module uses aligned RGB-D
obstacles identified from the depth and U-depth maps are            images for direct dynamic obstacle detection, and its results
characterized by their estimated velocities. These dynamic          are combined with the non-learning module. Details of each
obstacle detection outcomes are integrated with the occupancy       detector are in Sec. III-B, with ensemble detection explained
map to navigate dynamic environments. In contrast to prior          in Sec. III-C. Refined 3D bounding boxes are used in the
depth image-based approaches, Lu et al. [16] apply the YOLO         tracking module (Sec. III-D) to estimate obstacle states using
detector to effectively avoid fast and small dynamic obstacles.     historical data. The identification module (Sec. III-E) classifies
Additionally, Sun et al. [17] employ image differences to           obstacles as static or dynamic based on state and tracking
identify all dynamic points from RGB images. Moreover,              history. The system outputs dynamic obstacle bounding boxes,
XU et al.: ONBOARD DYNAMIC-OBJECT DETECTION AND TRACKING FOR AUTONOMOUS ROBOT NAVIGATION WITH RGB-D CAMERA                                                    3

Fig. 2. The proposed dynamic obstacle detection and tracking system (DODT) framework. The input data are the RGB-D images. The non-learning detection
module first uses the depth image to detect generic obstacles. Then, the tracking module is applied to track and estimate the obstacles states. With the
identification module, the dynamic obstacles are identified from all detected obstacles. Finally, the output results show the dynamic obstacles’ bounding boxes.
The dynamic obstacle regions are cleaned in the static occupancy map. The optional learning-based detection module, presented in the blue dotted line, uses
color and depth images to detect dynamic obstacles, enhancing the detection range and dynamic obstacle identification.

and dynamic obstacle regions are cleared in the static map for
navigation.

B. 3D-Obstacle Detectors
   This section introduces three computationally efficient but
low-accuracy 3D obstacle detectors: the U-depth, the DB-
SCAN, and the YOLO-MAD detector. Note that all detection
results are represented as axis-aligned bounding boxes. We
select the U-depth and the DBSCAN detectors as the non-
learning detectors due to their high computational efficiency
demonstrated in small UAV 3D dynamic obstacle detection                          Fig. 3. Illustration of the U-depth detector. (a) The camera RGB view. (b)
applications [4][6]. Besides, their detection errors come from                   The detected 3D bounding box with the obstacle point cloud. (c) The 2D
                                                                                 detection on the depth map. (d) The 2D detection on the U-depth map.
different sources (the depth image and the point cloud) ob-
tained from the RGB-D camera, ensuring the ensemble strat-
egy takes effect. For the learning-based detector, we choose
an extremely lightweight implementation of a popular model
and extend it into a 3D detector, which can run in real time
on onboard computers without GPU acceleration.
   U-depth Detector: The U-depth detector for obstacle detec-
tion is mentioned in the previous works [13][14][6]. Overall,
the detector takes the depth image to generate 3D bounding
boxes of static and dynamic obstacles. Fig. 3 visualizes sample
detection results. There are three steps in the U-depth detector:
                                                                                 Fig. 4. Illustration of the DBSCAN detector. (a) The robot encounters
(1) the U-depth map generation, (2) the line grouping on U-                      obstacles in a corridor. (b) The raw point cloud data from the RGB-D camera
depth, and (3) the depth continuity search on the original depth                 are unstructured and noisy. (c) The DBSCAN detector takes the filtered point
image.                                                                           cloud and performs clustering to get obstacles’ bounding boxes.
   The U-depth map can be intuitively viewed as the top-
down view from the camera. It has the same width as the                             DBSCAN Detector: Unlike the image-based detector, the
original depth image, and its vertical axis from top to bottom                   DBSCAN detector uses point cloud data to detect obstacles.
indicates the increasing distance to the camera. When we get                     DBSCAN is an unsupervised machine-learning algorithm for
a depth image, we can compute the U-depth map using the                          clustering which can automatically determine the cluster num-
column depth value histogram. Fig. 3c and Fig. 3d show a                         ber. The illustration of the DBSCAN detector is shown in Fig.
depth image and U-depth map pair. Then, we can perform                           4. When the robot encounters obstacles, the raw point cloud
the line grouping method on the generated U-depth map to                         data can be triangulated from the depth image as shown in
get the 2D bounding box of the obstacle of width wi and                          Fig. 4b. Note that because of the sensor, the point cloud data
thickness ti shown in Fig. 3d (note that i indicates the image                   can be noisy on the obstacle boundaries. So, we apply the
plane). With the obstacle width wi , we do the depth value                       voxel filter proposed in [3] to remove the noise of the point
continuity check on the original depth image to get the height                   cloud and then perform DBSCAN clustering to get obstacles’
hi of the obstacle shown in Fig. 3c. After having both 2D                        bounding boxes (Fig. 4c). Similar to the U-depth detector, the
bounding boxes in the U-depth map and the original depth                         DBSCAN detector does not need a training dataset and only
image, we can triangulate 3D points into the camera frame                        requires a few computation resources.
and perform coordinate transform to get the obstacle position                       YOLO-MAD Detector: The previously mentioned detec-
and dimension of the world/map coordinate frame (Fig. 3b).                       tors rely on geometric structures of either depth images or
4                                                        IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED NOVEMBER, 2023

                                                                                 Algorithm 1: Ensemble Detection Algorithm
                                                                             1  Ben ← ∅ ;           ▷ ensembled bounding boxes
                                                                             2  Bd1 ← getDetBBox1() ; ▷ detector1 results
                                                                              3 Bd2 ← getDetBBox2() ;         ▷ detector2 results
                                                                              4 for bd1 in Bd1 do
                                                                              5     Siou1 , bmatch1 ← findBestIOUMatch(bd1 , Bd2 );
                                                                              6     Siou2 , bmatch2 ← findBestIOUMatch(bmatch1 , Bd1 );
                                                                              7     Cmatch ← bmatch2 is bd1 ;
Fig. 5. Illustration of the YOLO-MAD detector. The RGB image is used to
get the 2D detection result, and then the bounding box on the depth image
                                                                              8     if Siou1 > Sthr and Siou2 > Sthr and Cmatch then
is obtained. With the 2D result on the depth image, the 3D bounding box is    9         ben ← fuseBBoxes(bd1 , bmatch1 );
calculated by the proposed median absolute deviation (MAD) method.           10         Ben .push back(ben );
                                                                             11 return Ben ;
point clouds. So, they cannot identify the type of obstacles
(i.e., static or dynamic) and might even fail when the obstacles
are far from the camera. To overcome these limitations, we                      The proposed ensemble detection algorithm follows a pair-
introduce our 3D YOLO-MAD detector based on the 2D                           wise manner presented in Alg. 1. When we obtain two sources
YOLOFastestDet, which can run real-time at an onboard                        of detection results, we go through each bounding box bd1
CPU such as Intel NUC. The illustration of the YOLO-MAD                      from one detector’s results (Line 4). For the bounding box
detector is shown in Fig. 5. The detector first detects the 2D               bd1 , the algorithm finds the bounding box bmatch1 with the
bounding box of each obstacle on the RGB image and finds the                 highest intersection-over-union (IOU) score from the other
corresponding region on the aligned depth image. To find the                 detection bounding boxes (Line 5). Following the same way,
depth and thickness of the 2D bounding box, we first calculate               the bounding box bmatch2 is obtained by finding the highest
the median absolute deviation (MAD) based on the median                      IOU match of bmatch1 in the first detection bounding boxes
depth value d˜ in the bounding box region Rbox :                             (Line 6). Through this process, we want to find the bounding
                                                                             boxes that are detected by both detectors. Then, we need
                           ˜
        MAD = median(|di − d|), di ∈ depth(Rbox ),                    (1)    to ensure that the IOU score of their matched bounding
                                                                             boxes exceeds the predefined threshold and that their matched
where di is the depth value of ith pixel in the bounding box                 bounding boxes have the highest IOU score to each other (Line
region Rbox . Then, we can search the minimum depth dmin                     8). Finally, we fuse two bounding boxes into a new ensembled
and maximum depth dmax in the MAD range SMAD :                               bounding box (Lines 9-10). We adopt a conservative method
       SMAD = {di |d˜ − n · MAD ≤ di ≤ d˜ + n · MAD},                 (2)    for fusing bounding boxes: the new ensembled bounding box
                                                                             takes the maximum values in dimensions and the average
where n is a user-defined parameter. The obstacle’s thickness                value in positions. In our system framework (Fig. 2), we first
tMAD can be calculated based on the minimum and maximum                      ensemble detection results from the U-depth and DBSCAN
depth values. The MAD range SMAD can help filter the outlier                 detectors and then combine the YOLO-MAD results if the
depth values in the bounding box region from the background                  learning-based module is running.
and the sensor noises. Finally, we can triangulate the points
from the depth image at the median depth plane with the                      D. Data Association and Tracking
thickness to get the 3D obstacle’s bounding box. Since this
learning-based detector can still be computationally heavy for                  Overall, the proposed module first applies the feature-based
some extremely low-power onboard computers, we treat it as                   data association method to match the detected obstacles at
an optional and auxiliary module in our framework.                           the current time tn with the obstacles at the previous time
                                                                             tn−1 . Then, it applies the Kalman filter with the constant-
                                                                             acceleration motion model to estimate the obstacles’ states
C. Ensemble Detection                                                        and add them to the estimation histories. In contrast to the
   This section introduces our proposed ensemble detection                   constant-velocity model used in previous works [14][4][6],
method to obtain refined obstacles’ bounding boxes. In our                   the constant acceleration model offers more accurate state
framework, three detectors run in parallel and individually                  estimation and dynamic obstacle identification.
detect obstacles’ bounding boxes. Since the previously men-                     Feature-based Data Association: The detected obstacles
tioned detectors are designed to compensate for the detection                at the current time tn are associated with the obstacles at the
accuracy for high-speed performance, they are all sensitive                  previous time tn−1 using the feature comparison. The feature
to different environments and sensor noises, leading to false                vector of the obstacle Oi is defined as:
positives and inaccurate obstacle dimension estimation. So,                             f eat(Oi ) = [pos(i), dim(i), len(i), std(i)],    (3)
the intuition of the ensemble detection is to combine the
detection results of different detectors and find their “mutual              where pos(i) is the obstacle’s center position, dim(i) is the
agreements” of detection results for reducing the noise effects.             obstacle’s dimension in x, y and z direction, len(i) is the
This technique can significantly improve detection robustness                obstacle’s point cloud size, and std(i) is the obstacle’s point
and accuracy with environment and sensor noises.                             cloud standard deviation. Then, we perform normalization for
XU et al.: ONBOARD DYNAMIC-OBJECT DETECTION AND TRACKING FOR AUTONOMOUS ROBOT NAVIGATION WITH RGB-D CAMERA                                                   5

                                                                                    Fig. 7. Illustration of removing the invalid points using the field of view
                                                                                    (FOV) criteria. (a) The analysis of the observed obstacle’s point cloud at
                                                                                    different time. (b) The robot detecting a partially visible obstacle.
Fig. 6. Illustration of the issue with the center-distance-based data association
method. (a) The RGB image at time t1 . (b) The RGB image at time t2 . (c)           the obstacle state vector. To calculate the measurement of the
The center-distance-based data association method might fail by incorrectly
associating the current detected person with the wall.                              velocity vector Vi and acceleration vector Ai at time t, we
                                                                                    adopt the following equations:
the feature vector to reduce the effects from the different                                             Pt − Pt−1          Vt − Vt−1
dimensions. After that, the similarity score between obstacles                                     Vt =            , At =              ,          (5)
                                                                                                            δt                  δt
Oi and Oj is calculated using the following equation:                               where δt is the time difference. Note that we take the data from
     sim(Oi , Oj ) = exp(−||f eat(Oi ) − f eat(Oj ))||22 ),                  (4)    several time differences δt to calculate smoother observations.
                                                                                    In this way, the system model is described by:
where we take the exponential of the negative L2 norm of the
feature difference. With the scores, the obstacle Oitn at the                                        Xt|t−1 = AXt−1 + But−1 + Q,                           (6)
                                                     t
current time tn can be matched with the obstacle Ojn−1 at the
                                                                                    where A is the state transition matrix, Q is the covariance of
previous time tn−1 with the highest similarity score simmax .
                                                                                    the motion model noise, u is the control input, which is zero
Instead of directly using the previous obstacle’s feature, we
                                                                                    in this case. Since the acceleration model is assumed, the state
apply the linear propagation to get the predicted obstacle’s
                                                                                    transition matrix can be calculated by:
position and replace the previous obstacle’s position with the
                                                                                                                            2
                                                                                                          1 0 δt 0 δt2
                                                                                                                                   
predicted position in the feature vector. Also, the highest                                                                      0
similarity score must be higher than a predefined threshold                                             0 1 0 δt 0             δt2 
                                                                                                                                2 
(simmax > Tsim ) to prevent incorrect associations.                                                     0 0 1 0 δt              0  
                                                                                                   A=                             ,           (7)
   The proposed feature-based data association method can                                               0 0 0 1           0     δt 
                                                                                                                                    
overcome the drawback of traditional center-distance-based                                              0 0 0 0           1     0 
association, as shown in Fig. 6. In Fig. 6a and b, a scenario is                                          0 0 0 0          0     1
presented where a person approaches the wall with the point
clouds of all obstacles shown in Fig. 6c. Since the center of                       and the system measurement is defined as:
the wall (Point C) is closer to the person’s position at the
current time t2 (Point B) than the person’s position at the                                                    Zt = HXt + R,                               (8)
previous time t1 (Point A), a center-distance-based tracking                        where the measurement matrix H is an identity matrix, and
will associate the person with the wall. On the contrary, if                        R is the covariance of measurement noise.
the proposed feature-based association method is applied, the
person and wall will not be matched together because of the
obvious differences in the obstacles’ dimensions, velocities,                       E. Dynamic Obstacle Identification
point cloud sizes, and standard deviations. So, the detected                           This section describes how to identify the status of an
person at the current time t2 will be correctly associated with                     obstacle (dynamic or static). By default, any quantities defined
the person at the previous time t1 .                                                in the following are at the current time tn . As the first
   Constant-Acceleration Kalman Filter: The states of each                          dynamic obstacle identification criteria, all the bounding boxes
obstacle are estimated by the Kalman filter with a constant-                        of obstacles with the center velocity Vcenter less than a
acceleration motion model. Unlike the previous work [4] [6],                        threshold Tvel will be classified as static. Although the velocity
where the velocities of obstacles are assumed to be constant,                       criteria should theoretically filter out all static obstacles, the
our method allows the obstacles’ velocities to change without                       noises from detection and state estimation can cause false-
increasing the complexity of the motion model too much. We                          positive dynamic obstacle identification. To reduce the false-
will discuss all quantities in global map frame for simplicity.                     positive identification results, in the second identification step,
The obstacle states are defined as X = [x, y, ẋ, ẏ, ẍ, ÿ]T ,                    the module takes all valid points of an obstacle’s point cloud
including the position, the velocity, and the acceleration in                       to vote for its status. In this step, every point at the current
x and y directions. The measurement vector is the same as                           time tn is matched with its corresponding point at the time
6                                                   IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED NOVEMBER, 2023

tn−k by the nearest neighbor search. After determining the                                         TABLE I
correspondence, the velocity of each point Vivote is calculated.        B ENCHMARKING OF THE DETECTION AND TRACKING RESULTS IN THE
                                                                       POSITION ERRORS , VELOCITY ERRORS AND THE FALSE POSITIVE RATES .
Then, a point will vote for the obstacle as dynamic if its
velocity exceeds a predefined threshold Tvote . If the ratio of              Method           Pos. Err. (m)   Vel. Err. (m/s)   FP Rate (%)
dynamic votes Nvote over the number of valid points Nvalid                 Method I [14]          0.28             0.47             N/A
is higher than another threshold Tratio , the obstacle will be             Method II [4]          0.18             0.29           16.4%
identified as a dynamic obstacle:                                         Method III [6]          0.19             0.21           19.6%
                                                                          DODT w/o Ens            0.17             0.30           18.6%
                        Nvote                                             DODT w/o FAT            0.14             0.29            6.5%
                               > Tratio .                      (9)        DODT (Ours)             0.11             0.23            3.7%
                        Nvalid
   Before the dynamic voting process, it is necessary to drop
the invalid points from the point cloud. First, if any point
pi,j with the point cloud index i in obstacle j has an invalid
velocity Vivote , it will be removed from the dynamic voting
process. The valid velocity should satisfy the condition:
                                               π
                   angle(Vivote , Vjcenter ) < ,               (10)
                                               2
where we ensure that points with incorrect velocity estimations
are removed. Second, if any point pi,j at time tn is invisible
                                                                      Fig. 8. Illustration of enhancing detection range by the auxiliary learning-
at time tn−k , it will also be removed from voting shown in           based module. The red line measures the maximum ideal range to produce
Fig. 7. Fig. 7(b) shows a scenario where a robot approaches a         dense point cloud data for the DBSCAN and U-depth detectors to detect
partially visible static obstacle. At the previous time t1 , only     obstacles. The yellow line indicates the increased detection distance.
red points are visible; the detected center of the obstacle is the
red star. At the current time t2 , the whole box is visible, and      total number of detections. Ground truth measurements are
the center of the obstacle shifts a lot. In this case, the obstacle   acquired from the OptiTrack motion capture system. Table
will have a large center velocity Vcenter and voting velocity         I summarizes the comparison results. Our DODT method
Vvote due to incorrect points correspondence. Our method              exhibits the lowest position errors among all methods, with
drops the newly observed points from the voting and identifies        our velocity error ranking second, comparable to Method III
the obstacle as static. Finally, when the YOLO-MAD Detector           [6]. Ensemble detection significantly reduces the false-positive
is applied, its classification results will be used for dynamic       detection rate by leveraging consensus among detectors and
obstacle identification, skipping all the processes mentioned         enhances obstacle position and velocity estimation accu-
above.                                                                racy. Additionally, the feature-based association and tracking
                                                                      method results in lower state estimation errors and a reduction
                IV. R ESULT AND D ISCUSSION                           in false-positive rates. From the experiment observation, this
                                                                      reduction in the state estimation errors and false-positive rates
   To evaluate the performance of the proposed method, we
                                                                      comes from fewer obstacle mismatches and more accurate
conduct experiments in dynamic environments. The algorithm
                                                                      velocity estimation.
is implemented in C++, running on two customized quad-
                                                                         The result illustration of enhancing detection range by the
copters with the Intel NUC and NVIDIA Jetson Xavier NX
                                                                      auxiliary learning-based module is visualized in Fig. 8. In Fig.
onboard computers, respectively. All the computations are
                                                                      8b, we label our depth camera’s dense point cloud distance
performed real-time on the robots’ onboard computers.
                                                                      (around 3m). Since both non-learning detectors, the U-depth
                                                                      and the DBSCAN detectors, require geometric information
A. Performance Benchmarking                                           from either depth image or point cloud, detecting obstacles
   To assess our algorithm’s performance, we conduct compar-          using the non-learning detectors outside the dense point cloud
ative experiments with state-of-the-art dynamic obstacle detec-       region can fail. On the contrary, the learning-based module
tion and tracking methods in the UAV platform [14][4][6]. We          can use the color image to detect obstacles (Fig. 8a) even
also evaluate the impact of ensemble detection and feature-           though the obstacle is in a sparse point cloud region. Fig. 8b
based association and tracking by comparing our method’s              shows that our YOLO-MAD detector can successfully detect
performance with and without these features. For experiments          the dynamic obstacle (shown as the purple bounding box) in
without ensemble detection (DDOT w/o Ens), we use the                 the sparse point cloud region with the increasing detection
U-depth detector due to its higher accuracy compared to               distance labeled as the yellow line.
the DBSCAN detector. In the absence of feature-based as-
sociation and tracking (DODT w/o FAT), we apply center-
distance-based association with the constant-velocity model.          B. Runtime Analysis
We employ various evaluation metrics, including position and             The runtime of the entire system is detailed in Table II,
velocity estimation errors and the false-positive detection rate.     with measurements conducted on both the Intel NUC and
The false-positive rate is determined by dividing the number of       Xavier NX onboard computers. Notably, the total runtime
misdetections (identifying static obstacles as dynamic) by the        for the Intel NUC and Xavier NX is 19.12ms and 40.08ms,
XU et al.: ONBOARD DYNAMIC-OBJECT DETECTION AND TRACKING FOR AUTONOMOUS ROBOT NAVIGATION WITH RGB-D CAMERA                                   7

                           TABLE II
     T HE RUNTIME OF EACH MODULE OF THE PROPOSED SYSTEM .

   System Modules              Intel NUC (ms)   Xavier NX (ms)
   U-depth detection                  3.4             12.0
   DBSCAN detection                   1.3              4.0
   YOLO-MAD detection                 14.3            23.5
   Feature-based Data Assoc.          0.03            0.08
   Kalman filter tracking            0.07             0.17
   Dynamic Obstacle Id.               0.12            0.33
   System Total Runtime              19.12           40.08

respectively, indicating the real-time performance on both plat-
forms. The runtime breakdown results reveal that the YOLO-
MAD detector consumes a significant portion of the processing
time, accounting for 75.7% and 59.5% of the total detector
runtime on the Intel NUC and Xavier NX, respectively. As
discussed in Section III-B, we recommend using the YOLO-
MAD detector as an optional and auxiliary module based             Fig. 9. Autonomous robot navigation in dynamic environments using the
on the computational resources. Experiments demonstrate that       proposed algorithm. The onboard obstacle detection results (blue bounding
                                                                   boxes) can help the robot modify its planned path to avoid obstacles safely.
if the user disables the learning-based module, the detection
frame rate on the Intel NUC and Xavier NX can increase
                                                                   safely. The figure shows that the walking person is successfully
substantially, reaching around 210Hz and 60Hz, respectively,
                                                                   detected as a dynamic obstacle, and the robot can efficiently
up from 50Hz and 25Hz.
                                                                   modify its planned trajectory based on the dynamic obstacle’s
                                                                   states.
C. Physical Experiments
   To verify the proposed algorithm’s performance in robot                      V. C ONCLUSION AND F UTURE W ORK
navigation, we conduct handheld experiments using the robot           This paper presents our lightweight 3D dynamic obstacle
camera and do the autonomous navigation tests with the             detection and tracking (DODT) algorithm for autonomous
trajectory planner [28][29] in dynamic environments.               robots navigating dynamic environments with limited com-
   Handheld Experiments: The handheld experiments are              putation. Our method adopts an ensemble detection strategy
conducted by moving the robot’s camera in dynamic en-              to obtain refined detection results by combining multiple
vironments to simulate the navigation trajectories. Fig. 10        computationally efficient but low-accuracy detectors. In addi-
shows the example experiments with results. The first example      tion, the proposed feature-based data association and tracking
experiment (Fig. 10a-b) shows persons walking in circles in        method prevents incorrect matches of obstacles with detected
front of the camera. One can see that our proposed algorithm       histories. Besides, with the obstacles’ state estimations, our
can detect multiple persons in the camera’s FOV and track          dynamic obstacle identification module can classify the de-
the history trajectories (shown as green curves) of dynamic        tected obstacles into static and dynamic. Finally, we propose
obstacles. Note that we only visualized the past 3 seconds’        using the learning-based method as an optional and auxiliary
history trajectories. The second example experiment (Fig. 10d-     module to enhance the detection range and dynamic obstacle
e) lets the camera follow a walking person. The timestamp          identification. Our experimental results show that our method
ti denotes the time starting from when the first time the          has the lowest position error (0.11m) and a velocity error
dynamic obstacle is detected. The detection results show that      (0.23m/s) compared with benchmarking algorithms. In the
our method can allow the robot to perform long-distance            flight experiments, our method enables the robot to adapt its
detection and tracking of the dynamic obstacle. However, from      trajectory efficiently for dynamic collision avoidance. Future
the experiment observation, we also notice that the occlusion      improvements can be realized through sensor fusion by har-
can cause losing track of the obstacles, which is the limitation   nessing the capabilities of multiple-camera systems. Further-
of the current system. Besides, due to the camera range            more, more advanced tracking techniques can be investigated
limitation, the robot can only detect and track the obstacles      to address tracking losses caused by occlusion.
in the camera’s field of view.
   Navigation Experiments: We prepare the dynamic environ-                                      R EFERENCES
ment consisting of both static and dynamic obstacles to test        [1] Y. Yan, Y. Mao, and B. Li, “Second: Sparsely embedded convolutional
the autonomous robot’s navigation ability. The experiment is            detection,” Sensors, vol. 18, no. 10, p. 3337, 2018.
shown in Fig. 9. Note that the static occupancy voxel map is        [2] S. Shi, C. Guo, L. Jiang, Z. Wang, J. Shi, X. Wang, and H. Li, “Pv-
                                                                        rcnn: Point-voxel feature set abstraction for 3d object detection,” in
also used for static obstacle avoidance. In the experiment, the         Proceedings of the IEEE/CVF Conference on Computer Vision and
robot is required to navigate to the given goal position, which         Pattern Recognition, 2020, pp. 10 529–10 538.
is 15 meters from the start location. During the navigation         [3] T. Eppenberger, G. Cesari, M. Dymczyk, R. Siegwart, and R. Dubé,
                                                                        “Leveraging stereo-camera data for real-time dynamic obstacle detection
period, two persons (only one shown in the figure) are walking          and tracking,” in 2020 IEEE/RSJ International Conference on Intelligent
randomly as dynamic obstacles, and the robot must avoid them            Robots and Systems (IROS). IEEE, 2020, pp. 10 528–10 535.
8                                                            IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED NOVEMBER, 2023

Fig. 10. The dynamic obstacle detection and tracking experiments with a handheld robot camera. The blue bounding boxes containing point clouds visualize
the dynamic obstacles’ detection results, and the tracking histories are shown as green curves. Figures (a) and (b) show the detection results of persons walking
in circles. Figures (c), (d), and (e) show the long-distance dynamic obstacle detection and tracking ability following a walking person.

 [4] Y. Wang, J. Ji, Q. Wang, C. Xu, and F. Gao, “Autonomous flights              [18] K. B. Logoglu, H. Lezki, M. K. Yucel, A. Ozturk, A. Kucukkomurler,
     in dynamic environments with onboard vision,” in 2021 IEEE/RSJ                    B. Karagoz, A. Erdem, and E. Erdem, “Feature-based efficient moving
     International Conference on Intelligent Robots and Systems (IROS).                object detection for low-altitude aerial platforms,” in 2017 IEEE Inter-
     IEEE, 2021, pp. 1966–1973.                                                        national Conference on Computer Vision Workshops (ICCVW), 2017,
 [5] H. Chen and P. Lu, “Real-time identification and avoidance of simulta-            pp. 2119–2128.
     neous static and dynamic obstacles on point cloud for uavs navigation,”      [19] W. Wu, Z. Wang, Z. Li, W. Liu, and L. Fuxin, “Pointpwc-net: A coarse-
     Robotics and Autonomous Systems, vol. 154, p. 104124, 2022.                       to-fine network for supervised and self-supervised scene flow estimation
 [6] Z. Xu, X. Zhan, B. Chen, Y. Xiu, C. Yang, and K. Shimada, “A real-time            on 3d point clouds,” arXiv preprint arXiv:1911.12408, 2019.
     dynamic obstacle tracking and mapping system for uav navigation and          [20] S. L. Francis, S. G. Anavatti, and M. Garratt, “Detection of obstacles
     collision avoidance with an rgb-d camera,” in 2023 IEEE International             in the path planning module using differential scene flow technique,” in
     Conference on Robotics and Automation (ICRA), 2023, pp. 10 645–                   2015 International Conference on Advanced Mechatronics, Intelligent
     10 651.                                                                           Manufacture, and Industrial Automation (ICAMIMIA), 2015, pp. 53–57.
 [7] X. Liu, G. V. Nardari, F. C. Ojeda, Y. Tao, A. Zhou, T. Donnelly, C. Qu,     [21] C. Yu, Z. Liu, X.-J. Liu, F. Xie, Y. Yang, Q. Wei, and Q. Fei, “Ds-
     S. W. Chen, R. A. Romero, C. J. Taylor et al., “Large-scale autonomous            slam: A semantic visual slam towards dynamic environments,” in 2018
     flight with real-time semantic slam under dense forest canopy,” IEEE              IEEE/RSJ International Conference on Intelligent Robots and Systems
     Robotics and Automation Letters, vol. 7, no. 2, pp. 5512–5519, 2022.              (IROS). IEEE, 2018, pp. 1168–1174.
 [8] A. Moffatt, E. Platt, B. Mondragon, A. Kwok, D. Uryeu, and S. Bhan-          [22] W. Dai, Y. Zhang, P. Li, Z. Fang, and S. Scherer, “Rgb-d slam in dynamic
     dari, “Obstacle detection and avoidance system for small uavs using a             environments using point correlations,” IEEE Transactions on Pattern
     lidar,” in 2020 International Conference on Unmanned Aircraft Systems             Analysis and Machine Intelligence, vol. 44, no. 1, pp. 373–389, 2020.
     (ICUAS). IEEE, 2020, pp. 633–640.                                            [23] I. Ballester, A. Fontán, J. Civera, K. H. Strobl, and R. Triebel, “Dot:
                                                                                       Dynamic object tracking for visual slam,” in 2021 IEEE International
 [9] W. Shi, J. Li, Y. Liu, D. Zhu, D. Yang, and X. Zhang, “Dynamic
                                                                                       Conference on Robotics and Automation (ICRA). IEEE, 2021, pp.
     obstacles rejection for 3d map simultaneous updating,” IEEE Access,
                                                                                       11 705–11 711.
     vol. 6, pp. 37 715–37 724, 2018.
                                                                                  [24] Y. Qiu, C. Wang, W. Wang, M. Henein, and S. Scherer, “Airdos: dynamic
[10] D. Yoon, T. Tang, and T. Barfoot, “Mapless online detection of dynamic            slam benefits from articulated objects,” in 2022 International Conference
     objects in 3d lidar,” 05 2019, pp. 113–120.                                       on Robotics and Automation (ICRA). IEEE, 2022, pp. 8047–8053.
[11] D. Falanga, K. Kleber, and D. Scaramuzza, “Dynamic obstacle avoid-           [25] F. Kong, W. Xu, Y. Cai, and F. Zhang, “Avoiding dynamic small
     ance for quadrotors with event cameras,” Science Robotics, vol. 5, no. 40,        obstacles with onboard sensing and computation on aerial robots,” IEEE
     p. eaaz9712, 2020.                                                                Robotics and Automation Letters, vol. 6, no. 4, pp. 7869–7876, 2021.
[12] A. Z. Zhu, D. Thakur, T. Özaslan, B. Pfrommer, V. Kumar, and                [26] Y. Min, D.-U. Kim, and H.-L. Choi, “Kernel-based 3-d dynamic oc-
     K. Daniilidis, “The multivehicle stereo event camera dataset: An event            cupancy mapping with particle tracking,” in 2021 IEEE International
     camera dataset for 3d perception,” IEEE Robotics and Automation                   Conference on Robotics and Automation (ICRA). IEEE, 2021, pp.
     Letters, vol. 3, no. 3, pp. 2032–2039, 2018.                                      5268–5274.
[13] H. Oleynikova, D. Honegger, and M. Pollefeys, “Reactive avoidance            [27] G. Chen, W. Dong, P. Peng, J. Alonso-Mora, and X. Zhu, “Continuous
     using embedded stereo vision for mav flight,” in 2015 IEEE Interna-               occupancy mapping in dynamic environments using particles,” IEEE
     tional Conference on Robotics and Automation (ICRA). IEEE, 2015,                  Transactions on Robotics, 2023.
     pp. 50–56.                                                                   [28] Z. Xu, Y. Xiu, X. Zhan, B. Chen, and K. Shimada, “Vision-aided
[14] J. Lin, H. Zhu, and J. Alonso-Mora, “Robust vision-based obstacle                 uav navigation and dynamic obstacle avoidance using gradient-based b-
     avoidance for micro aerial vehicles in dynamic environments,” in 2020             spline trajectory optimization,” in 2023 IEEE International Conference
     IEEE International Conference on Robotics and Automation (ICRA).                  on Robotics and Automation (ICRA), 2023, pp. 1214–1220.
     IEEE, 2020, pp. 2682–2688.                                                   [29] Z. Xu, D. Deng, Y. Dong, and K. Shimada, “Dpmpc-planner: A real-
[15] A. Saha, B. C. Dhara, S. Umer, K. Yurii, J. M. Alanazi, and A. A.                 time uav trajectory planning framework for complex static environments
     AlZubi, “Efficient obstacle detection and tracking using rgb-d sensor             with dynamic obstacles,” in 2022 International Conference on Robotics
     data in dynamic environments for robotic applications,” Sensors, vol. 22,         and Automation (ICRA). IEEE, 2022, pp. 250–256.
     no. 17, p. 6537, 2022.
[16] M. Lu, H. Chen, and P. Lu, “Perception and avoidance of multiple small
     fast moving objects for quadrotors with only low-cost rgbd camera,”
     IEEE Robotics and Automation Letters, vol. 7, no. 4, pp. 11 657–11 664,
     2022.
[17] Y. Sun, M. Liu, and M. Q.-H. Meng, “Improving rgb-d slam in
     dynamic environments: A motion removal approach,” Robotics and
     Autonomous Systems, vol. 89, pp. 110–122, 2017. [Online]. Available:
     https://www.sciencedirect.com/science/article/pii/S0921889015302232
