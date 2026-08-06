---
source_id: 144
bibtex_key: geiger2012kitti
title: Are We Ready for Autonomous Driving? The KITTI Vision Benchmark Suite
year: 2012
domain_theme: Dataset
verified_pdf: 144_KITTI.pdf
char_count: 74802
---

Are we ready for Autonomous Driving?
                                  The KITTI Vision Benchmark Suite

             Andreas Geiger and Philip Lenz                                  Raquel Urtasun
             Karlsruhe Institute of Technology                   Toyota Technological Institute at Chicago
                   {geiger,lenz}@kit.edu                                       rurtasun@ttic.edu

                         Abstract

   Today, visual recognition systems are still rarely em-
ployed in robotics applications. Perhaps one of the main
reasons for this is the lack of demanding benchmarks that
mimic such scenarios. In this paper, we take advantage
of our autonomous driving platform to develop novel chal-
lenging benchmarks for the tasks of stereo, optical flow, vi-
sual odometry / SLAM and 3D object detection. Our record-
ing platform is equipped with four high resolution video
cameras, a Velodyne laser scanner and a state-of-the-art
localization system. Our benchmarks comprise 389 stereo
                                                                     Figure 1. Recording platform with sensors (top-left), trajectory
and optical flow image pairs, stereo visual odometry se-             from our visual odometry benchmark (top-center), disparity and
quences of 39.2 km length, and more than 200k 3D ob-                 optical flow map (top-right) and 3D object labels (bottom).
ject annotations captured in cluttered scenarios (up to 15
cars and 30 pedestrians are visible per image). Results              [17], Middlebury for stereo [41] and optical flow [2] evalu-
from state-of-the-art algorithms reveal that methods rank-           ation. However, most of these datasets are simplistic, e.g.,
ing high on established datasets such as Middlebury per-             are taken in a controlled environment. A notable exception
form below average when being moved outside the labora-              is the PASCAL VOC challenge [16] for detection and seg-
tory to the real world. Our goal is to reduce this bias by           mentation.
providing challenging benchmarks with novel difficulties to              In this paper, we take advantage of our autonomous driv-
the computer vision community. Our benchmarks are avail-             ing platform to develop novel challenging benchmarks for
able online at: www.cvlibs.net/datasets/kitti                        stereo, optical flow, visual odometry / SLAM and 3D object
                                                                     detection. Our benchmarks are captured by driving around a
                                                                     mid-size city, in rural areas and on highways. Our recording
1. Introduction                                                      platform is equipped with two high resolution stereo cam-
                                                                     era systems (grayscale and color), a Velodyne HDL-64E
   Developing autonomous systems that are able to assist             laser scanner that produces more than one million 3D points
humans in everyday tasks is one of the grand challenges in           per second and a state-of-the-art OXTS RT 3003 localiza-
modern computer science. One example are autonomous                  tion system which combines GPS, GLONASS, an IMU and
driving systems which can help decrease fatalities caused            RTK correction signals. The cameras, laser scanner and lo-
by traffic accidents. While a variety of novel sensors have          calization system are calibrated and synchronized, provid-
been used in the past few years for tasks such as recognition,       ing us with accurate ground truth. Table 1 summarizes our
navigation and manipulation of objects, visual sensors are           benchmarks and provides a comparison to existing datasets.
rarely exploited in robotics applications: Autonomous driv-              Our stereo matching and optical flow estimation bench-
ing systems rely mostly on GPS, laser range finders, radar           mark comprises 194 training and 195 test image pairs at
as well as very accurate maps of the environment.                    a resolution of 1240 × 376 pixels after rectification with
   In the past few years an increasing number of bench-              semi-dense (50%) ground truth. Compared to previous
marks have been developed to push forward the perfor-                datasets [41, 2, 30, 29], this is the first one with realis-
mance of visual recognitions systems, e.g., Caltech-101              tic non-synthetic imagery and accurate ground truth. Dif-

                                                                 1
ficulties include non-lambertian surfaces (e.g., reflectance,      priate sequences and frames for each benchmark as well as
transparency) large displacements (e.g., high speed), a large      the development of metrics for each task. In this section we
variety of materials (e.g., matte vs. shiny), as well as differ-   discuss how we tackle these challenges.
ent lighting conditions (e.g., sunny vs. cloudy).
    Our 3D visual odometry / SLAM dataset consists of              2.1. Sensors and Data Acquisition
22 stereo sequences, with a total length of 39.2 km. To               We equipped a standard station wagon with two color
date, datasets falling into this category are either monocular     and two grayscale PointGrey Flea2 video cameras (10 Hz,
and short [43] or consist of low quality imagery [42, 4, 35].      resolution: 1392 × 512 pixels, opening: 90◦ × 35◦ ), a Velo-
They typically do not provide an evaluation metric, and as         dyne HDL-64E 3D laser scanner (10 Hz, 64 laser beams,
a consequence there is no consensus on which benchmark             range: 100 m), a GPS/IMU localization unit with RTK cor-
should be used to evaluate visual odometry / SLAM ap-              rection signals (open sky localization errors < 5 cm) and a
proaches. Thus often only qualitative results are presented,       powerful computer running a real-time database [22].
with the notable exception of laser-based SLAM [28]. We               We mounted all our cameras (i.e., two units, each com-
believe a fair comparison is possible in our benchmark due         posed of a color and a grayscale camera) on top of our vehi-
to its large scale nature as well as the novel metrics we pro-     cle. We placed one unit on the left side of the rack, and the
pose, which capture different sources of error by evaluating       other on the right side. Our camera setup is chosen such
error statistics over all sub-sequences of a given trajectory      that we obtain a baseline of roughly 54 cm between the
length or driving speed.                                           same type of cameras and that the distance between color
    Our 3D object benchmark focuses on computer vision             and grayscale cameras is minimized (6 cm). We believe
algorithms for object detection and 3D orientation estima-         this is a good setup since color images are very useful for
tion. While existing benchmarks for those tasks do not pro-        tasks such as segmentation and object detection, but provide
vide accurate 3D information [17, 39, 15, 16] or lack real-        lower contrast and sensitivity compared to their grayscale
ism [33, 31, 34], our dataset provides accurate 3D bounding        counterparts, which is of key importance in stereo matching
boxes for object classes such as cars, vans, trucks, pedes-        and optical flow estimation.
trians, cyclists and trams. We obtain this information by             We use a Velodyne HDL-64E unit, as it is one of the few
manually labeling objects in 3D point clouds produced by           sensors available that can provide accurate 3D information
our Velodyne system, and projecting them back into the im-         from moving platforms. In contrast, structured-light sys-
age. This results in tracklets with accurate 3D poses, which       tems such as the Microsoft Kinect do not work in outdoor
can be used to asses the performance of algorithms for 3D          scenarios and have a very limited sensing range. To com-
orientation estimation and 3D tracking.                            pensate egomotion in the 3D laser measurements, we use
    In our experiments, we evaluate a representative set of        the position information from our GPS/IMU system.
state-of-the-art systems using our benchmarks and novel
metrics. Perhaps not surprisingly, many algorithms that            2.2. Sensor Calibration
do well on established datasets such as Middlebury [41, 2]            Accurate sensor calibration is key for obtaining reliable
struggle on our benchmark. We conjecture that this might           ground truth. Our calibration pipeline proceeds as follows:
be due to their assumptions which are violated in our sce-         First, we calibrate the four video cameras intrinsically and
narios, as well as overfitting to a small set of training (test)   extrinsically and rectify the input images. We then find the
images.                                                            3D rigid motion parameters which relate the coordinate sys-
    In addition to the benchmarks, we provide MAT-                 tem of the laser scanner, the localization unit and the refer-
LAB/C++ development kits for easy access. We also main-            ence camera. While our Camera-to-Camera and GPS/IMU-
tain an up-to-date online evaluation server1 . We hope that        to-Velodyne registration methods are fully automatic, the
our efforts will help increase the impact that visual recogni-     Velodyne-to-Camera calibration requires the user to manu-
tion systems have in robotics applications.                        ally select a small number of correspondences between the
                                                                   laser and the camera images. This was necessary as existing
2. Challenges and Methodology                                      techniques for this task are not accurate enough to compute
                                                                   ground truth estimates.
   Generating large-scale and realistic evaluation bench-
marks for the aforementioned tasks poses a number of chal-
lenges, including the collection of large amounts of data in       Camera-to-Camera calibration. To automatically cali-
real time, the calibration of diverse sensors working at dif-      brate the intrinsic and extrinsic parameters of the cameras,
ferent rates, the generation of ground truth minimizing the        we mounted checkerboard patterns onto the walls of our
amount of supervision required, the selection of the appro-        garage and detect corners in our calibration images. Based
                                                                   on gradient information and discrete energy-minimization,
  1 www.cvlibs.net/datasets/kitti                                  we assign corners to checkerboards, match them between
                        Stereo Matching         type        #images    resolution    ground truth   uncorrelated        metric
                            EISATS [30]       synthetic       498       0.3 Mpx         dense
                         Middlebury [41]     laboratory        38       0.2 Mpx         dense               X               X
                      Make3D Stereo [40]        real          257       0.8 Mpx         0.5 %               X               X
                            Ladicky [29]        real           70       0.1 Mpx        manual               X
                       Proposed Dataset         real          389       0.5 Mpx         50 %                X               X

                           Optical Flow        type        #images     resolution   ground truth    uncorrelated       metric
                           EISATS [30]       synthetic       498        0.3 Mpx        dense
                          Middlebury [2]    laboratory        24        0.2 Mpx        dense            X                X
                       Proposed Dataset        real          389        0.5 Mpx        50 %             X                X

               Visual Odometry / SLAM        setting      #sequences     length     #frames    resolution       ground truth      metric
                       TUM RGB-D [43]        indoor           27         0.4 km       65k       0.3 Mpx             X              X
                        New College [42]    outdoor            1         2.2 km       51k       0.2 Mpx
                         Malaga 2009 [4]    outdoor            6         6.4 km       38k       0.8 Mpx             X
                       Ford Campus [35]     outdoor            2         5.1 km        7k       1.0 Mpx             X
                       Proposed Dataset     outdoor           22        39.2 km       41k       0.5 Mpx             X                X

             Object Detection / 3D Estimation    #categories     avg. #labels/category   occlusion labels       3D labels       orientations
                              Caltech 101 [17]      101                 40-800
                         MIT StreetScenes [3]         9                   3,000
                                 LabelMe [39]       3997                    60
                        ETHZ Pedestrian [15]          1                  12,000
                           PASCAL 2011 [16]          20                   1,150                 X
                                   Daimler [8]        1                  56,000                 X
                       Caltech Pedestrian [13]        1                 350,000                 X
                                COIL-100 [33]       100                     72                                     X              72 bins
                    EPFL Multi-View Car [34]         20                     90                                     X              90 bins
                      Caltech 3D Objects [31]       100                    144                                     X             144 bins
                            Proposed Dataset          2                  80,000                 X                  X            continuous

                             Table 1. Comparison of current State-of-the-Art Benchmarks and Datasets.

the cameras and optimize all parameters by minimizing the                   well condition the minimization problem. Next, we ran-
average reprojection error [19].                                            domly sample 1000 pairs of poses from this sequence and
                                                                            obtain the desired result using [14].
Velodyne-to-Camera calibration. Registering the laser                       2.3. Ground Truth
scanner with the cameras is non-trivial as correspondences
                                                                               Having calibrated and registered all sensors, we are
are hard to establish due to the large amount of noise in the
                                                                            ready to generate ground truth for the individual bench-
reflectance values. Therefore we rely on a semi-automatic
                                                                            marks shown in Fig. 1.
technique: First, we register both sensors using the fully au-
                                                                               To obtain a high stereo and optical flow ground truth
tomatic method of [19]. Next, we minimize the number of
                                                                            density, we register a set of consecutive frames (5 before
disparity outliers with respect to the top performing meth-
                                                                            and 5 after the frame of interest) using ICP. We project the
ods in our benchmark jointly with the reprojection errors of
                                                                            accumulated point clouds onto the image and automatically
a few manually selected correspondences between the laser
                                                                            remove points falling outside the image. We then manu-
point cloud and the images. As correspondences, we se-
                                                                            ally remove all ambiguous image regions such as windows
lect edges which can be easily located by humans in both
                                                                            and fences. Given the camera calibration, the correspond-
domains (i.e., images and point clouds). Optimization is
                                                                            ing disparity maps are readily computed. Optical flow fields
carried out by drawing samples using Metropolis-Hastings
                                                                            are obtained by projecting the 3D points into the next frame.
and selecting the solution with the lowest energy.
                                                                            For both tasks we evaluate both non-occluded pixels as well
                                                                            as all pixels for which ground truth is available. Our non-
GPS/IMU-to-Velodyne calibration. Our GPS/IMU to                             occluded evaluation excludes all surface points falling out-
Velodyne registration process is fully automatic. We can-                   side the image plane. Points occluded by objects within the
not rely on visual correspondences, however, if motion esti-                same image could not be reliably estimated in a fully auto-
mates from both sensors are provided, the problem becomes                   matic manner due to the properties of the laser scanner. To
identical to the well-known hand-eye calibration problem,                   avoid artificial errors, we do not interpolate the ground truth
which has been extensively explored in the robotics com-                    disparity maps and optical flow fields, leading to a ∼ 50%
munity [14]. Making use of ICP, we accurately register                      average ground truth density.
laser point clouds of a parking sequence, as this provides                     The ground truth for visual odometry/SLAM is directly
a large variety of orientations and translations necessary to               given by the output of the GPS/IMU localization unit pro-
                                                                                                                 100                                                                   35000                                                                          18000
                              120000
                                                                                                                                                                                                                                                                      16000
                                                                                                                                                                                       30000

                                                                                     % of Object Class Members
                              100000
                                                                                                                                                                                                                                                                      14000
                                                                                                                                                                                       25000

                                                                                                                                                                                                                                              Number of Images
                                                                                                                                                                    Number of Images
          Number of Objects

                               80000                                                                                                                                                                                                                                  12000

                                                                                                                  50                                                                   20000                                                                          10000
                               60000

                                                                                                                                                                                       15000                                                                           8000
                               40000
                                                                                                                                                                                                                                                                       6000
                                                                                                                                                                                       10000
                               20000                                                                                                                                                                                                                                   4000
                                                                                                                                                                                        5000
                                   0                                                                               0                                                                                                                                                   2000
                                         r     n    k     n      )     t         c                                             r                 ian       ian
                                       Ca    Va Truc stria itting yclis Tram Mis                                            Ca ded Car ated destr ded destr ated                           0                                                                                0
                                                     de      s     C
                                                   Pe rson (                                                                 clu      nc Pe cclu Pe runc
                                                      Pe                                                                Oc        Tru      O          T                                    0        2   4   6 8 10 12 14 16 18 20                                           0    2   4   6    8 10 12 14 16 18 20
                                                         Object Class                                                        Occlusion/Truncation Status by Class                                           Pedestrians per Image                                                            Cars per Image

                               20000                                                                              6000                                                                 1000                                                                           100

                                                                                                                  5000                                                                  500                                                                            50
                               15000
                                                                                     Number of Pedestrians

                                                                                                                                                                                                                                              Number of Pedestrians
                                                                                                                  4000                                                                    0                                                                             0
     Number of Cars

                                                                                                                                                                                       1000                                                                           100

                                                                                                                                                                    Number of Cars
                               10000                                                                              3000
                                                                                                                                                                                        500                                                                            50

                                                                                                                  2000
                                                                                                                                                                                          0                                                                             0
                                5000                                                                                                                                                    200                                                                           100
                                                                                                                  1000
                                                                                                                                                                                        100                                                                            50
                                   0                                                                                   0
                                                                                                                           0

                                                                                                                                                               50
                                                                                                                                 0

                                                                                                                                             50

                                                                                                                                                         11 0
                                                                                                                                                              50
                                                                                                                                       50

                                                                                                                                                   0
                                       11 0
                                               0

                                             50

                                              0

                                       15 0
                                              0

                                             50

                                             50

                                                                                                                        .5

                                                                                                                                 .5

                                                                                                                                                         .5
                                                                                                                                                   .5
                                           .5
                                           .5

                                           .5

                                             5
                                           .5

                                                                                                                                                                                          0                                                                             0
                                                                                                                                                            7.
                                                                                                                                             2.

                                                                                                                                                           2.
                                                                                                                                       7.
                                          2.

                                          2.
                                          7.

                                          7.

                                                                                                                       57

                                                                                                                             12

                                                                                                                                                        67
                                                                                                                                                  22
                                        67
                                        12

                                        22
                                  57

                                                                                                                                                         15
                                                                                                                                            -2
                                                                                                                                      -6

                                                                                                                                                                                              1.0          2.0      3.0       4.0       5.0
                                       -2
                                       -6

                                                                                                                                                                                                                                                                                0.0                1.0                2.0
                                                                                                                   -1

                                                                                                                            -1
                                        -1
                                 -1

                                                     Orientation [deg]                                                                      Orientation [deg]                                       height [m] / width [m] / length [m]                                            height [m] / width [m] / length [m]

Figure 2. Object Occurence and Object Geometry Statistics of our Dataset. This figure shows (from left to right and top to bottom):
The different types of objects occuring in our sequences, the power-law shaped distribution of the number of instances within an image
and the orientation histograms and object size distributions for the two most predominant categories ’cars’ and ’pedestrians’.

jected into the coordinate system of the left camera after                                                                                                                             removing scenes with bad illumination conditions as, e.g.,
rectification.                                                                                                                                                                         tunnels, we obtain 194 training and 195 test image pairs for
    To generate 3D object ground-truth we hired a set of                                                                                                                               both benchmarks.
annotators, and asked them to assign tracklets in the form                                                                                                                                For our visual odometry / SLAM evaluation we select
of 3D bounding boxes to objects such as cars, vans, trucks,                                                                                                                            long sequences of varying speed with high-quality localiza-
trams, pedestrians and cyclists. Unlike most existing bench-                                                                                                                           tion, yielding a set of 41.000 frames captured at 10 fps and
marks, we do not rely on online crowd-sourcing to perform                                                                                                                              a total driving distance of 39.2 km with frequent loop clo-
the labeling. Towards this goal, we create a special pur-                                                                                                                              sures which are of interest in SLAM.
pose labeling tool, which displays 3D laser points as well                                                                                                                                Our 3D object detection and orientation estimation
as the camera images to increase the quality of the anno-                                                                                                                              benchmark is chosen according to the number of non-
tations. Following [16], we asked the annotators to addi-                                                                                                                              occluded objects in the scene, as well as the entropy of the
tionally mark each bounding box as either visible, semi-                                                                                                                               object orientation distribution. High entropy is desirable in
occluded, fully occluded or truncated. Statistics of our la-                                                                                                                           order to ensure diversity. Towards this goal we utilize a
beling effort are shown in Fig. 2.                                                                                                                                                     greedy algorithm: We initialize our dataset X to the empty
                                                                                                                                                                                       set ∅ and iteratively add images using the following rule
2.4. Benchmark Selection                                                                                                                                                                                                          "                                                          C
                                                                                                                                                                                                                                                                                                                       #
                                                                                                                                                                                                                           1 X
   We collected a total of ∼ 3 TB of data from which we                                                                                                                                        X ← X ∪ argmax α · noc(x) +       Hc (X ∪ x)                                                                                 (1)
                                                                                                                                                                                                          x                C c=1
select a representative subset to evaluate each task. In our
experiments we currently concentrate on grayscale images,                                                                                                                              where X is the current set, x is an image from our dataset,
as they provide higher quality than their color counterparts.                                                                                                                          noc(x) stands for the number of non-occluded objects in
   For our stereo and optical flow benchmarks we select a                                                                                                                              image x and C denotes the number of object classes. Hc
subset of the sequences where the environment is static. To                                                                                                                            is the entropy of class c with respect to orientation (we use
maximize diversity, we perform k-means (k = 400) cluster-                                                                                                                              8/16 orientation bins for pedestrians/cars). We further en-
ing on the data using a novel representation, and chose the                                                                                                                            sure that images from one sequence do not appear in both
elements closest to the center of each cluster for the bench-                                                                                                                          training and test set.
mark. We describe each image using a 144-dimensional
                                                                                                                                                                                       2.5. Evaluation Metrics
image descriptor, obtained by subdividing the image into
12 × 4 rectangular blocks and computing the average dis-                                                                                                                                  We evaluate state-of-the-art approaches utilizing a di-
parity and optical flow displacement for each block. After                                                                                                                             verse set of metrics. Following [41, 2] we evaluate stereo
and optical flow using the average number of erroneous
pixels in terms of disparity and end-point error. In con-
trast to [41, 2], our images are not downsampled. There-
fore, we employ a disparity/end-point error threshold of
τ ∈ {2, .., 5} px for our benchmark, with τ = 3 px the
default setting which takes into consideration almost all cal-
ibration and laser measurement errors. We report errors for
both non-occluded pixels as well as all pixels where ground-            (a) Best: < 1% errors            (b) Worst: 21% errors
truth is available.
    Evaluating visual odometry/SLAM approaches based              Figure 3. Stereo Results for PCBP [46]. Input image (top), es-
on the error of the trajectory end-point can be misleading,       timated disparity map (middle), disparity errors (bottom). Error
as this measure depends strongly on the point in time where       range: 0 px (black) to ≥ 5 px (white).
the error has been made, e.g., rotational errors earlier in the
sequence lead to larger end-point errors. Kümmerle at al.
[28] proposed to compute the average of all relative rela-
tions at a fixed distance. Here we extend this metric in
two ways. Instead of combining rotation and translation
errors into a single measure, we treat them separately. Fur-
thermore, we evaluate errors as a function of the trajectory
length and velocity. This allows for deeper insights into
the qualities and failure modes of individual methods. For-
mally, our error metrics are defined as                                 (a) Best: < 1% errors            (b) Worst: 59% errors
                       1 X                                        Figure 4. Optical Flow Results for TGV2CENSUS [45]. Input
     Erot (F )   =         ∠ [(p̂j ⊖ p̂i ) ⊖ (pj ⊖ pi )] (2)
                      |F |                                        image (top), estimated flow field (middle), end point errors (bot-
                         (i,j)∈F
                                                                  tom). Error range: 0 px (black) to ≥ 5 px (white).
                       1 X
   Etrans (F)    =         k(p̂j ⊖ p̂i ) ⊖ (pj ⊖ pi )k2 (3)
                      |F |
                         (i,j)∈F
                                                                  where D(r) denotes the set of all object detections at recall
 where F is a set of frames (i, j), p̂ ∈ SE(3) and p ∈                          (i)
                                                                  rate r and ∆θ is the difference in angle between estimated
SE(3) are estimated and true camera poses respectively, ⊖
                                                                  and ground truth orientation of detection i. To penalize mul-
denotes the inverse compositional operator [28] and ∠[·] is
                                                                  tiple detections which explain a single object, we set δi = 1
the rotation angle.
                                                                  if detection i has been assigned to a ground truth bounding
   Our 3D object detection and orientation estimation
                                                                  box (overlaps by at least 50%) and δi = 0 if it has not been
benchmark is split into three parts: First, we evaluate classi-
                                                                  assigned.
cal 2D object detection by measuring performance using the
                                                                      Finally, we also evaluate pure classification (16 bins for
well established average precision (AP) metric as described
                                                                  cars) and regression (continuous orientation) performance
in [16]. Detections are iteratively assigned to ground truth
                                                                  on the task of 3D object orientation estimation in terms of
labels starting with the largest overlap, measured by bound-
                                                                  orientation similarity.
ing box intersection over union. We require true positives
to overlap by more than 50% and count multiple detections
of the same object as false positives. We assess the perfor-      3. Experimental Evaluation
mance of jointly detecting objects and estimating their 3D           We run a representative set of state-of-the-art algorithms
orientation using a novel measure which we called the av-         for each task. Interestingly, we found that algorithms rank-
erage orientation similarity (AOS), which we define as:           ing high on existing benchmarks often fail when confronted
                        1      X                                  with more realistic scenarios. This section tells their story.
              AOS =                     max s(r̃)           (4)
                       11              r̃:r̃≥r
                          r∈{0,0.1,..,1}                          3.1. Stereo Matching
Here, r = T PT+F
               P
                 N is the PASCAL object detection recall,            For stereo matching, we run global [26, 37, 46], semi-
where detected 2D bounding boxes are correct if they over-        global [23], local [5, 20, 38] and seed-growing [27, 10, 9]
lap by at least 50% with a ground truth bounding box. The         methods. The parameter settings we have employed can be
orientation similarity s ∈ [0, 1] at recall r is a normalized     found on www.cvlibs.net/datasets/kitti. Missing disparities
([0..1]) variant of the cosine similarity defined as              are filled-in for each algorithm using background interpola-
                            X 1 + cos ∆(i)                        tion [23] to produce dense disparity maps which can then be
                       1               θ                          compared. As Table 2 shows, errors on our benchmark are
           s(r) =                          δi              (5)
                     |D(r)|        2                              higher than those reported on Middlebury [41], indicating
                            i∈D(r)
              Stereo    Non-Occluded        All      Density                         Optical Flow                           Non-Occluded                                     All        Density
         PCBP [46]         4.72 %         6.16 %    100.00 %                    TGV2CENSUS [45]                               11.14 %                                      18.42 %     100.00 %
         ITGV [37]         6.31 %         7.40 %    100.00 %                              HS [44]                             19.92 %                                      28.86 %     100.00 %
     OCV-SGBM [5]          7.64 %         9.13 %     86.50 %                            LDOF [7]                              21.86 %                                      31.31 %     100.00 %
         ELAS [20]         8.24 %         9.95 %     94.55 %                           C+NL [44]                              24.64 %                                      33.35 %     100.00 %
          SDM [27]        10.98 %        12.19 %     63.58 %                       DB-TV-L1 [48]                              30.75 %                                      39.13 %     100.00 %
          GCSF [9]        12.06 %        13.26 %     60.77 %                            GCSF [9]                              33.23 %                                      41.74 %     48.27 %
          GCS [10]        13.37 %        14.54 %     51.06 %                            HAOF [6]                              35.76 %                                      43.36 %     100.00 %
      CostFilter [38]     19.96 %        21.05 %    100.00 %                          OCV-BM [5]                              63.46 %                                      68.16 %     100.00 %
       OCV-BM [5]         25.39 %        26.72 %     55.84 %                      Pyramid-LK [47]                             65.74 %                                      70.09 %     99.90 %
       GC+occ [26]        33.50 %        34.74 %     87.57 %

Table 2. Stereo (left) and Optical Flow (right) Ranking from April 2, 2012. Numbers denote the percentage of pixels with disparity
error or optical flow end-point error (euclidean distance) larger than τ = 3px, averaged over all test images. Here, non-occluded refers
to pixels which remain inside the image after projection in both images and all denotes all pixels for which ground truth information is
available. Density refers to the number of estimated pixels. Invalid disparities and flow vectors have been interpolated for comparability.

                                                                                                 25                                                                 0.08

                                                                                                                                           Rotation Error [deg/m]
the increased level of difficulty of our real-world dataset. In-                                                   VISO2-S                                                            VISO2-S

                                                                         Translation Error [%]
                                                                                                                  VO3ptLBA                                          0.07             VO3ptLBA
                                                                                                 20
                                                                                                                                                                    0.06
terestingly, methods ranking high on Middlebury, perform                                                             VO3pt
                                                                                                                  VOFSLBA                                           0.05
                                                                                                                                                                                        VO3pt
                                                                                                                                                                                     VOFSLBA
                                                                                                 15
                                                                                                                      VOFS
particularly bad on our dataset, e.g., guided cost-volume fil-                                                     VISO2-M
                                                                                                                                                                    0.04                 VOFS
                                                                                                                                                                                      VISO2-M
                                                                                                 10                                                                 0.03
tering [38], pixel-wise graph cuts [26]. This is mainly due                                                                                                         0.02
                                                                                                 5
                                                                                                                                                                    0.01
to the differences in the data sets: Since the Middlebury                                        0                                                                     0
benchmark is largely well textured and provides a smaller                                             0   50 100 150 200 250 300 350 400                                   0 50 100150200250300350400
                                                                                                               Path Length [m]                                                   Path Length [m]
label set, methods concentrating on accurate object bound-                                       30                                                                  0.3

                                                                                                                                           Rotation Error [deg/m]
                                                                                                                    VISO2-S                                                           VISO2-S
                                                                         Translation Error [%]

ary segmentation peform well. In contrast, our data requires                                     25                VO3ptLBA                                         0.25             VO3ptLBA
                                                                                                                      VO3pt                                                             VO3pt
more global reasoning about areas with little, ambiguous or                                      20                VOFSLBA                                           0.2
                                                                                                                                                                                     VOFSLBA
                                                                                                 15                    VOFS                                         0.15                 VOFS
no texture where segmentation performance is less critical.                                                         VISO2-M
                                                                                                                                                                     0.1
                                                                                                                                                                                      VISO2-M
                                                                                                 10
Purely local methods [5, 38] fail if fronto-parallel surfaces                                     5                                                                 0.05
are assumed, as this assumption is often strongly violated in                                     0                                                                   0
                                                                                                      0 10 20 30 40 50 60 70 80 90                                         0 10 20 30 40 50 60 70 80 90
real-world scenes (e.g., road or buildings).                                                                    Speed [km/h]                                                      Speed [km/h]
    Fig. 3 shows the best and worst test results for the (cur-
rently) top ranked stereo method PCBP [46]. While small                 Figure 5. Visual Odometry Evaluation. Translation and rotation
errors are made in natural environments due to the large de-            errors, averaged over all sub-sequences of a given length or speed.
gree of textureness, inner-city scenarios prove to be chal-
lenging. Here, the predominant error sources are image sat-
uration (wall on the left), disparity shadows (RV occludes              world. Previously hampered by the lack of sufficient train-
road) and non-lambertian surfaces (reflections on RV body).             ing data, such approaches will become feasible in the near
                                                                        future with larger training sets as the one we provide.
3.2. Optical Flow Estimation
                                                                        3.3. Visual Odometry/SLAM
   For optical flow we evaluate state-of-the-art variational
[24, 6, 48, 44, 7, 9, 45] and local [5, 47] methods. The re-               We evaluate five different approaches on our visual
sults of our experiments are summarized in Table 2. We                  odometry / SLAM dataset: VISO2-S/M [21], a real-time
observed that classical variational approaches [24, 44, 45]             stereo/monocular visual odometry library based on incre-
work best on our images. However, the top performing ap-                mental motion estimates, the approach of [1] with and with-
proach TGV2CENSUS [45] still produces about 11% of                      out Local Bundle Adjustment (LBA) [32] as well as the flow
errors on average. As highlighted in Fig. 4, most errors                separation approach of [25]. All algorithms are compara-
are made in regions which undergo large displacements be-               ble as none of them uses loop-closure information. All ap-
tween frames, e.g., close range pixels on the street. Further-          proaches use stereo with the exception of VISO2-M [21]
more, pyramidal implementations lack the ability to esti-               which employs only monocular images. Fig. 5 depicts the
mate flow fields at higher levels of the pyramid due to miss-           rotational and translational errors as a function of the trajec-
ing texture. While best results are obtained at small motions           tory length and driving speed.
(Fig. 4 left, flow ≤ 55 px), driving at high speed (Fig. 4                 In our evaluation, VISO2-S [21] comes closest to the
right, flow ≤ 176 px) leads to large displacements, which               ground truth trajectories with an average translation error of
can not be reliably handled by any of the evaluated meth-               2.2% and an average rotation error of 0.016 deg/m. Akin to
ods. We believe that to overcome these problems we need                 our optical flow experiments, large motion impacts perfor-
more complex models that utilize prior knowledge of the                 mance, especially in terms of translation. With a recording
                                                                                                Classification   Similarity   Regression   Similarity
             1                                         1                                            SVM[11]        0.93          GP [36]     0.92
                                                                                                           NN      0.85        SVM[11]       0.91
                                                                                                                                     NN      0.86
Precision

                                                AOS
            0.5                                       0.5
                   L-SVM variable, #100                                                  Table 3. Object Orientation Errors for Cars. Performance mea-
                   L-SVM fixed init, #100                   L-SVM fixed init, #100       sured in terms of orientation similarity (Eq. 5). Higher is better.
                   L-SVM fixed, #100                        L-SVM fixed, #100
             0                                         0
              0              0.5            1           0             0.5            1
                            Recall                                   Recall
                                                                                         of them achieve high precision, while the recall seems to be
                  (a) Precision-Recall           (b) Average Orientation Similarity      limited by some hard to detect objects. We plan to extend
Figure 6. Object Detection and Orientation Estimation Results.                           our online evaluation to more complex scenarios such as
Details about the metrics can be found in Sec. 2.5                                       semi-occluded or truncated objects and other object classes
                                                                                         like vans, trucks, pedestrians and cyclists.
                                                                                            Finally, we also evaluate object orientation estimation.
rate of 10 frames per second, the vehicle moved up to 2.8
                                                                                         We extract 100 car instances per orientation bin, using 16
meters per frame. Additionally, large motions mainly occur
                                                                                         orientation bins. We compute HOG features [12] on all
on highways which are less rich in terms of 3D structure.
                                                                                         cropped and resized bounding boxes with 19 × 13 blocks,
Large errors at lower speeds stem from the fact that incre-
                                                                                         8 × 8 pixel cells and 12 orientation bins. We evaluate multi-
mental or sliding-window based methods slowly drift over
                                                                                         ple classification and regression algorithms and report aver-
time, with the strongest relative impact at slow speeds. This
                                                                                         age orientation similarity (Eq. 5). Table 3 shows our results.
problem can be easily alleviated if larger timespans are op-
                                                                                         We found that for the classification task SVMs [11] clearly
timized when the vehicle moves slowly or is standing still.
                                                                                         outperform nearest neighbor classification. For the regres-
In our experiments, no ground truth information has been
                                                                                         sion task, Gaussian Process regression [36] performs best.
used to train the model parameters. We expect detecting
loop closures, utilizing more enhanced bundle adjustment
techniques as well as utilizing the training data for parame-                            4. Conclusion and Future Work
ter fitting to further boost performance.                                                    Throwing new light on existing methods, we hope that
                                                                                         the proposed benchmarks will complement others and help
3.4. 3D Object Detection / Orientation Estimation                                        to reduce overfitting to datasets with little training or test
    We evaluate object detection as well as joint detec-                                 examples and contribute to the development of algorithms
tion and orientation estimation using average precision and                              that work well in practice. As our recorded data provides
average orientation similarity as described in Sec. 2.5.                                 more information than compiled into the benchmarks so
Our benchmark extracted from the full dataset comprises                                  far, our intention is to gradually increase their difficul-
12, 000 images with 40, 000 objects. We first subdivide the                              ties. Furthermore, we also plan to include visual SLAM
training set into 16 orientation classes and use 100 non-                                with loop-closure capabilities, object tracking, segmenta-
occluded examples per class for training the part-based ob-                              tion, structure-from-motion and 3D scene understanding
ject detector of [18] using three different settings: We train                           into our evaluation framework.
the model in an unsupervised fashion (variable), by initial-
izing the components to the 16 classes but letting the com-                              References
ponents vary during optimization (fixed init) and by initial-
                                                                                          [1] P. Alcantarilla, L. Bergasa, and F. Dellaert. Visual odometry
izing the components and additionally fixing the latent vari-
                                                                                              priors for robust EKF-SLAM. In ICRA, 2010. 6
ables to the 16 classes (fixed).
                                                                                          [2] S. Baker, D. Scharstein, J. Lewis, S. Roth, M. Black, and
    We evaluate all non- and weakly-occluded (< 20%) ob-
                                                                                              R. Szeliski. A database and evaluation methodology for op-
jects which are neither truncated nor smaller than 40 px in                                   tical flow. IJCV, 92:1–31, 2011. 1, 2, 3, 4, 5
height. We do not count detecting truncated or occluded ob-                               [3] S. M. Bileschi. Streetscenes: Towards scene understanding
jects as false positives. For our object detection experiment,                                in still images. Technical report, MIT, 2006. 3
we require a bounding box overlap of at least 50%, results                                [4] J.-L. Blanco, F.-A. Moreno, and J. Gonzalez. A collection
are shown in Fig. 6(a). For detection and orientation es-                                     of outdoor robotic datasets with centimeter-accuracy ground
timation we require the same overlap and plot the average                                     truth. Auton. Robots, 27:327–351, 2009. 2, 3
orientation similarity (Eq. 5) over recall for the two unsu-                              [5] G. Bradski. The opencv library. Dr. Dobb’s Journal of Soft-
pervised variants (Fig. 6(b)). Note that the precision is an                                  ware Tools, 2000. 5, 6
upper bound to the average orientation similarity.                                        [6] T. Brox, A. Bruhn, N. Papenberg, and J. Weickert. High ac-
    Overall, we could not find any substantial difference be-                                 curacy optical flow estimation based on a theory for warping.
tween the part-based detector variants we investigated. All                                   In ECCV, 2004. 6
 [7] T. Brox and J. Malik. Large displacement optical flow: De-       [29] L. Ladicky, P. Sturgess, C. Russell, S. Sengupta, Y. Bastanlar,
     scriptor matching in variational motion estimation. PAMI,             W. Clocksin, and P. Torr. Joint optimisation for object class
     33:500–513, March 2011. 6                                             segmentation and dense stereo reconstruction. In BMVC,
 [8] M. E. C. G. Keller and D. M. Gavrila. A new benchmark for             2010. 1, 3
     stereo-based pedestrian detection. In IV, 2011. 3                [30] S. Morales and R. Klette. Ground truth evaluation of stereo
 [9] J. Cech, J. Sanchez-Riera, and R. P. Horaud. Scene flow es-           algorithms for real world applications. In ACCV Workshops,
     timation by growing correspondence seeds. In CVPR, 2011.              volume 2 of LNCS, pages 152–162, 2010. 1, 3
     5, 6                                                             [31] P. Moreels and P. Perona. Evaluation of features, detec-
[10] J. Cech and R. Sara. Efficient sampling of disparity space for        tors and descriptors based on 3d objects. IJCV, 73:263–284,
     fast and accurate matching. In BenCOS, 2007. 5, 6                     2007. 2, 3
[11] C.-C. Chang and C.-J. Lin. LIBSVM: a library for support         [32] E. Mouragnon, M. Lhuillier, M. Dhome, F. Dekeyser, and
     vector machines. Technical report, 2001. 7                            P. Sayd. Generic and real-time structure from motion using
[12] N. Dalal and B. Triggs. Histograms of oriented gradients for          local bundle adjustment. IVC, 27:1178–1193, 2009. 6
     human detection. In CVPR, 2005. 7                                [33] Nayar and H. Murase. Columbia Object Image Library:
[13] P. Dollar, C. Wojek, B. Schiele, and P. Perona. Pedestrian            COIL-100. Technical report, Department of Computer Sci-
     detection: An evaluation of the state of the art. In PAMI,            ence, Columbia University, 1996. 2, 3
     volume 99, 2011. 3                                               [34] M. Ozuysal, V. Lepetit, and P.Fua. Pose estimation for cate-
[14] F. Dornaika and R. Horaud. Simultaneous robot-world and               gory specific multiview object localization. In CVPR, 2009.
     hand-eye calibration. Rob. and Aut., 1998. 3                          2, 3
[15] A. Ess, B. Leibe, and L. V. Gool. Depth and appearance for       [35] G. Pandey, J. R. McBride, and R. M. Eustice. Ford campus
     mobile scene analysis. In ICCV, 2007. 2, 3                            vision and lidar data set. IJRR, 2011. 2, 3
[16] M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn, and      [36] C. E. Rasmussen and C. K. I. Williams. Gaussian Processes
     A. Zisserman. The PASCAL Visual Object Classes Chal-                  for Machine Learning. MIT Press, 2005. 7
     lenge 2011 (VOC2011) Results. 1, 2, 3, 4, 5                      [37] T. P. H. B. Rene Ranftl, Stefan Gehrig. Pushing the limits of
                                                                           stereo using variational stereo estimation. In IV, 2012. 5, 6
[17] L. Fei-Fei, R. Fergus, and P. Perona. Learning generative
     visual models from few training examples: an incremental         [38] C. Rhemann, A. Hosni, M. Bleyer, C. Rother, and
     bayesian approach tested on 101 object categories. In Work-           M. Gelautz. Fast cost-volume filtering for visual correspon-
     shop on Generative-Model Based Vision, 2004. 1, 2, 3                  dence and beyond. In CVPR, 2011. 5, 6
[18] P. Felzenszwalb, R.Girshick, D. McAllester, and D. Ra-           [39] B. Russell, A. Torralba, K. Murphy, and W. Freeman. La-
     manan. Object detection with discriminatively trained part-           belme: A database and web-based tool for image annotation.
     based models. PAMI, 32:1627–1645, 2010. 7                             IJCV, 77:157–173, 2008. 2, 3
[19] A. Geiger, F. Moosmann, O. Car, and B. Schuster. A toolbox       [40] A. Saxena, J. Schulte, and A. Y. Ng. Depth estimation using
     for automatic calibration of range and camera sensors using           monocular and stereo cues. In IJCAI, 2007. 3
     a single shot. In ICRA, 2012. 3                                  [41] D. Scharstein and R. Szeliski. A taxonomy and evaluation of
[20] A. Geiger, M. Roser, and R. Urtasun. Efficient large-scale            dense two-frame stereo correspondence algorithms. IJCV,
     stereo matching. In ACCV, 2010. 5, 6                                  47:7–42, 2001. 1, 2, 3, 4, 5
                                                                      [42] M. Smith, I. Baldwin, W. Churchill, R. Paul, and P. Newman.
[21] A. Geiger, J. Ziegler, and C. Stiller. StereoScan: Dense 3d
                                                                           The new college vision and laser data set. IJRR, 28:595–599,
     reconstruction in real-time. In IV, 2011. 6
                                                                           2009. 2, 3
[22] M. Goebl and G. Faerber. A real-time-capable hard- and soft-
                                                                      [43] J. Sturm, S. Magnenat, N. Engelhard, F. Pomerleau, F. Colas,
     ware architecture for joint image and knowledge processing
                                                                           W. Burgard, D. Cremers, and R. Siegwart. Towards a bench-
     in cognitive automobiles. In IV, 2007. 2
                                                                           mark for RGB-D SLAM evaluation. In RGB-D Workshop,
[23] H. Hirschmueller. Stereo processing by semiglobal matching
                                                                           2011. 2, 3
     and mutual information. PAMI, 30:328–41, 2008. 5
                                                                      [44] D. Sun, S. Roth, and M. J. Black. Secrets of optical flow
[24] B. K. P. Horn and B. G. Schunck. Determining optical flow:
                                                                           estimation and their principles. In CVPR, 2010. 6
     A retrospective. AI, 59:81–87, 1993. 6
                                                                      [45] M. Werlberger. Convex Approaches for High Performance
[25] M. Kaess, K. Ni, and F. Dellaert. Flow separation for fast            Video Processing. phdthesis, Graz University of Technology,
     and robust stereo odometry. In ICRA, 2009. 6                          2012. 5, 6
[26] V. Kolmogorov and R. Zabih. Computing visual correspon-          [46] K. Yamaguchi, T. Hazan, D. McAllester, and R. Urtasun.
     dence with occlusions using graph cuts. In ICCV, pages 508–           Continuous markov random fields for robust stereo estima-
     515, 2001. 5, 6                                                       tion. In arXiv:1204.1393v1, 2012. 5, 6
[27] J. Kostkova. Stratified dense matching for stereopsis in com-    [47] J. yves Bouguet. Pyramidal implementation of the Lucas
     plex scenes. In BMVC, 2003. 5, 6                                      Kanade feature tracker. Intel, 2000. 6
[28] R. Kuemmerle, B. Steder, C. Dornhege, M. Ruhnke,                 [48] C. Zach, T. Pock, and H. Bischof. A duality based approach
     G. Grisetti, C. Stachniss, and A. Kleiner. On measuring the           for realtime TV-L1 optical flow. In DAGM, pages 214–223,
     accuracy of SLAM algorithms. Auton. Robots, 27:387–407,               2007. 6
     2009. 2, 5
