---
source_id: 150
bibtex_key: feng2021multimodalsurvey
title: Deep Multi-Modal Object Detection and Semantic Segmentation for Autonomous Driving: Datasets, Methods, and Challenges
year: 2021
domain_theme: Fusi Multimodal
verified_pdf: 150_Survei Deteksi & Segmentasi Multimodal (Feng dkk.).pdf
char_count: 246146
---

1

                                           Deep Multi-modal Object Detection and Semantic
                                           Segmentation for Autonomous Driving: Datasets,
                                                      Methods, and Challenges
                                         Di Feng∗,1,2,† , Christian Haase-Schütz∗,3,4 , Lars Rosenbaum1 , Heinz Hertlein3 , Claudius Gläser1 , Fabian Timm1 ,
                                                                             Werner Wiesbeck4 , Klaus Dietmayer2

                                           Abstract—Recent advancements in perception for autonomous
arXiv:1902.07830v4 [cs.RO] 8 Feb 2020

                                        driving are driven by deep learning. In order to achieve robust                                       RGB Image                       LiDAR Points            Radar Points                  Map

                                        and accurate scene understanding, autonomous vehicles are
                                        usually equipped with different sensors (e.g. cameras, LiDARs,
                                        Radars), and multiple sensing modalities can be fused to exploit
                                        their complementary properties. In this context, many methods
                                        have been proposed for deep multi-modal perception problems.
                                        However, there is no general guideline for network architecture
                                        design, and questions of “what to fuse”, “when to fuse”, and                                                                                                               0.96   0.96

                                        “how to fuse” remain open. This review paper attempts to sys-                                                  0.99                              0.8

                                        tematically summarize methodologies and discuss challenges for                                                                                                      0.94
                                                                                                                                                                                                                             0.99

                                        deep multi-modal object detection and semantic segmentation in                                                                                         0.98

                                        autonomous driving. To this end, we first provide an overview of
                                        on-board sensors on test vehicles, open datasets, and background                                    Vehicle             Person
                                        information for object detection and semantic segmentation in                                      Road sign          Traffic light
                                        autonomous driving research. We then summarize the fusion
                                        methodologies and discuss challenges and open questions. In the
                                        appendix, we provide tables that summarize topics and methods.                              Fig. 1: A complex urban scenario for autonomous driving. The
                                        We also provide an interactive online platform to navigate each                             driverless car uses multi-modal signals for perception, such as
                                        reference: https://boschresearch.github.io/multimodalperception/.                           RGB camera images, LiDAR points, Radar points, and map
                                                                                                                                    information. It needs to perceive all relevant traffic participants
                                           Keywords—multi-modality, object detection, semantic segmen-                              and objects accurately, robustly, and in real-time. For clarity,
                                        tation, deep learning, autonomous driving                                                   only the bounding boxes and classification scores for some
                                                                                                                                    objects are drawn in the image. The RGB image is adapted
                                                                                                                                    from [4].
                                                                     I. I NTRODUCTION
                                           Significant progress has been made in autonomous driving                                 ronments; (2). robust: they should work properly in adverse
                                        since the first successful demonstration in the 1980s [1] and                               weather, in situations that are not covered during training
                                        the DARPA Urban Challenge in 2007 [2]. It offers high                                       (open-set conditions), and when some sensors are degraded or
                                        potential to decrease traffic congestion, improve road safety,                              even defective; and (3). real-time: especially when the cars are
                                        and reduce carbon emissions [3]. However, developing reliable                               driving at high speed. Towards these goals, autonomous cars
                                        autonomous driving is still a very challenging task. This is                                are usually equipped with multi-modal sensors (e.g. cameras,
                                        because driverless cars are intelligent agents that need to                                 LiDARs, Radars), and different sensing modalities are fused
                                        perceive, predict, decide, plan, and execute their decisions in                             so that their complementary properties are exploited (cf. Sec.
                                        the real world, often in uncontrolled or complex environments,                              II-A). Furthermore, deep learning has been very successful
                                        such as the urban areas shown in Fig. 1. A small error in the                               in computer vision. A deep neural network is a powerful
                                        system can cause fatal accidents.                                                           tool for learning hierarchical feature representations given a
                                           Perception systems in driverless cars need to be (1). accu-                              large amount of data [5]. In this regard, many methods have
                                        rate: they need to give precise information of driving envi-                                been proposed that employ deep learning to fuse multi-modal
                                                                                                                                    sensors for scene understanding in autonomous driving. Fig. 2
                                          ∗ Di Feng and Christian Haase-Schütz contributed equally to this work.
                                                                                                                                    shows some recently published methods and their performance
                                          1 Driver Assistance Systems and Automated Driving, Corporate Research,
                                                                                                                                    on the KITTI dataset [6]. All methods with the highest perfor-
                                        Robert Bosch GmbH, 71272 Renningen, Germany.
                                          2 Institute of Measurement, Control and Microtechnology, Ulm University,                  mance are based on deep learning, and many methods that fuse
                                        89081 Ulm, Germany.                                                                         camera and LiDAR information produce better performance
                                          3 Engineering Cognitive Systems, Automated Driving, Chassis Systems
                                                                                                                                    than those using either LiDAR or camera alone. In this paper,
                                        Control, Robert Bosch GmbH, 74232 Abstatt, Germany.
                                          4 Institute of Radio Frequency Engineering and Electronics, Karlsruhe                     we focus on two fundamental perception problems, namely,
                                        Institute of Technology, 76131 Karlsruhe, Germany.                                          object detection and semantic segmentation. In the rest of
                                          † Corresponding author: Di.Feng@de.bosch.com                                              this paper, we will call them deep multi-modal perception
                                        ©2020 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing
                                        this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this
                                        work in other works. DOI: 10.1109/TITS.2020.2972974.
                                                                                                                                                                                                 2

                            HDNET ContFuse F-PointNet

      PointPillars
                      0.9
                                      AVOD        PointRCNN                                             LiDAR                   B. Contributions
                                                          MV3D(LiDAR)
                      0.8               AVOD-FPN            VoxelNet       MV3D                         LiDAR+Camera
                                PIXOR
                                        A3DODWTDA
                                                                                           F-PC_CNN
                                                                                                        Camera                     To the best of our knowledge, there is no survey that
                                                                 TopNet-HighRes
                      0.7                     TopNet-DecayRate                                                  3D-FCN
                                                                                                          (inference time>5s)
                                                                                                                                focuses on deep multi-modal object detection (2D or 3D)
                      0.6                                                                                                       and semantic segmentation for autonomous driving, which
  Average Precision

                                          BirdNet
                      0.5                                                         Pseudo-LiDAR
                                                                                                                                makes it difficult for beginners to enter this research field.
                      0.4
                                                                                                                                Our review paper attempts to narrow this gap by conducting a
                                                                                                                                summary of newly-published datasets (2013-2019), and fusion
                      0.3
                                                                                                                                methodologies for deep multi-modal perception in autonomous
                      0.2
                                              MonoFusion
                                                                                                          A3DODWTDA(image)      driving, as well as by discussing the remaining challenges and
                                                                                      OFT-NET
                      0.1
                                          3D-SSMFCNN
                                                                                                                                open questions.
                      0.0                                                                                                          We first provide background information on multi-modal
                            0           100         200          300         400         500      600    700        800
                                                                 Reported Runtime (ms)                                          sensors, test vehicles, and modern deep learning approaches
                                                                                                                                in object detection and semantic segmentation in Sec. II. We
Fig. 2: Average precision (AP) vs. runtime. Visualized are deep
                                                                                                                                then summarize multi-modal datasets and perception problems
learning approaches that use LiDAR, camera, or both as inputs
                                                                                                                                in Sec. III and Sec. IV, respectively. Sec. V summarizes
for car detection on the KITTI bird’s eye view test dataset.
                                                                                                                                the fusion methodologies regarding “what to fuse”, “when to
Moderate APs are summarized. The results are mainly based
                                                                                                                                fuse” and “how to fuse”. Sec. VI discusses challenges and
on the KITTI leader-board [6] (visited on Apr. 20, 2019). On
                                                                                                                                open questions when developing deep multi-modal perception
the leader-board only the published methods are considered.
                                                                                                                                systems in order to fulfill the requirements of “accuracy”,
                                                                                                                                “robustness” and “real-time”, with a focus on data preparation
unless mentioned otherwise.                                                                                                     and fusion methodology. We highlight the importance of
   When developing methods for deep multi-modal object                                                                          data diversity, temporal and spatial alignment, and labeling
detection or semantic segmentation, it is important to consider                                                                 efficiency for multi-modal data preparation. We also high-
the input data: Are there any multi-modal datasets available                                                                    light the lack of research on fusing Radar signals, as well
and how is the data labeled (cf. Tab. II)? Do the datasets                                                                      as the importance of developing fusion methodologies that
cover diverse driving scenarios (cf. Sec. VI-A1)? Is the data                                                                   tackle open dataset problems or increase network robustness.
of high quality (cf. Sec. VI-A2)? Additionally, we need to                                                                      Sec. VII concludes this work. In addition, we provide an
answer several important questions on designing the neural                                                                      interactive online platform for navigating topics and methods
network architecture: Which modalities should be combined                                                                       for each reference. The platform can be found here: https:
via fusion, and how to represent and process them properly                                                                      //boschresearch.github.io/multimodalperception/.
(“What to fuse” cf. Sec. VI-B1)? Which fusion operations and
methods can be used (“How to fuse” cf. Sec. VI-B2)? Which                                                                                             II. BACKGROUND
stage of feature representation is optimal for fusion (“When
to fuse” cf. Sec. VI-B2)?                                                                                                          This section provides the background information for deep
                                                                                                                                multi-modal perception in autonomous driving. First, we
                                                                                                                                briefly summarize typical automotive sensors, their sensing
                                                                                                                                modalities, and some vehicles for test and research pur-
A. Related Works
                                                                                                                                poses. Next, we introduce deep object detection and semantic
   Despite the fact that many methods have been proposed                                                                        segmentation. Since deep learning has most-commonly been
for deep multi-modal perception in autonomous driving, there                                                                    applied to image-based signals, here we mainly discuss image-
is no published summary examining available multi-modal                                                                         based methods. We will introduce other methods that process
datasets, and there is no guideline for network architecture                                                                    LiDAR and Radar data in Sec. V-A. For a more comprehensive
design. Yin et al. [7] summarize 27 datasets for autonomous                                                                     overview on object detection and semantic segmentation, we
driving that were published between 2006 and 2016, in-                                                                          refer the interested reader to the review papers [11], [12]. For a
cluding the datasets recorded with a single camera alone or                                                                     complete review of computer vision problems in autonomous
multiple sensors. However, many new multi-modal datasets                                                                        driving (e.g. optical flow, scene reconstruction, motion estima-
have been released since 2016, and it is worth summarizing                                                                      tion), cf. [9].
them. Ramachandram et al. [8] provide an overview on deep
multi-modal learning, and mention its applications in diverse
                                                                                                                                A. Sensing Modalities for Autonomous Driving
research fields, such as robotic grasping and human action
recognition. Janai et al. [9] conduct a comprehensive summary                                                                      1) Visual and Thermal Cameras: Images captured by visual
on computer vision problems for autonomous driving, such                                                                        and thermal cameras can provide detailed texture information
as scene flow and scene construction. Recently, Arnold et                                                                       of a vehicle’s surroundings. While visual cameras are sensitive
al. [10] survey the 3D object detection problem in autonomous                                                                   to lighting and weather conditions, thermal cameras are more
driving. They summarize methods based on monocular images                                                                       robust to daytime/nighttime changes as they detect infrared
or point clouds, and briefly mention some works that fuse                                                                       radiation that relates to heat from objects. However, both types
vision camera and LiDAR information.                                                                                            of cameras however cannot directly provide depth information.
                                                                                                                                  3

   2) LiDARs: LiDARs (Light Detection And Ranging) give
accurate depth information of the surroundings in the form
of 3D points. They measure reflections of laser beams which
they emit with a certain frequency. LiDARs are robust to
different lighting conditions, and less affected by various
weather conditions such as fog and rain than visual cameras.
However, typical LiDARs are inferior to cameras for object
classification since they cannot capture the fine textures of                    (a)                            (b)
objects, and their points become sparse with distant objects.
Recently, flash LiDARs were developed which can produce de-       Fig. 3: (a) The Boss autonomous car at DARPA 2007 [2], (b)
tailed object information similar to camera images. Frequency     Waymo self-driving car [14].
Modulated Continuous Wave (FMCW) LiDARs can provide
velocity information.
   3) Radars: Radars (Radio Detection And Ranging) emit           to drive autonomously on the Bertha Benz memorial route in
radio waves to be reflected by an obstacle, measures the          2013 [16]. Our interactive online platform provides a detailed
signal runtime, and estimates the object’s radial velocity by     description for more autonomous driving tests, including Uber,
the Doppler effect. They are robust against various lighting      Nvidia, GM Cruise, Baidu Apollo, as well as their sensor
and weather conditions, but classifying objects via Radars        setup.
is very challenging due to their low resolution. Radars are          Besides driving demonstrations, real-world datasets are cru-
often applied in adaptive cruise control (ACC) and traffic jam    cial for autonomous driving research. In this regard, several
assistance systems [13].                                          research projects use data vehicles with multi-modal sensors to
   4) Ultrasonics: Ultrasonic sensors send out high-frequency     build open datasets. These data vehicles are usually equipped
sound waves to measure the distance to objects. They are          with cameras, LiDARs and GPS/IMUs to collect images, 3D
typically applied for near-range object detection and in low      point clouds, and vehicle localization information. Sec. III
speed scenarios, such as automated parking [13]. Due to           provides an overview of multi-modal datasets in autonomous
the sensing properties, Ultrasonics are largely affected by air   driving.
humidity, temperature, or dirt.
   5) GNSS and HD Maps: GNSS (Global Navigation Satel-
                                                                  C. Deep Object Detection
lite Systems) provide accurate 3D object positions by a global
satellite system and the receiver. Examples of GNSS are GPS,         Object detection is the task of recognizing and localizing
Galileo and GLONASS. First introduced to automotive as            multiple objects in a scene. Objects are usually recognized
navigation tools in driver assistance functions [13], currently   by estimating a classification probability and localized with
GNSS is also used together with HD Maps for path planning         bounding boxes (cf. Fig. 1). Deep learning approaches have
and ego-vehicle localization for autonomous vehicles.             set the benchmark on many popular object detection datasets,
   6) IMU and Odometers: Unlike sensors discussed above           such as PASCAL VOC [17] and COCO [18], and have been
which capture information in the external environment (i.e.       widely applied in autonomous driving, including detecting
“exteroceptive sensors”), Inertial Measurement Units (IMU)        traffic lights [19]–[22], road signs [23]–[25], people [26]–[28],
and odometers provide vehicles’ internal information (i.e.        or vehicles [29]–[33], to name a few. State-of-the-art deep
“proprioceptive sensors”) [13]. IMU measure the vehicles’         object detection networks follow one of two approaches: the
accelerations and rotational rates, and odometers the odometry.   two-stage or the one-stage object detection pipelines. Here we
They have been used in vehicle dynamic driving control            focus on image-based detection.
systems since the 1980s. Together with the exteroceptive             1) Two-stage Object Detection: In the first stage, several
sensors, they are currently used for accurate localization in     class-agnostic object candidates called regions of interest
autonomous driving.                                               (ROI) or region proposals (RP) are extracted from a scene.
                                                                  Then, these candidates are verified, classified, and refined in
                                                                  terms of classification scores and locations. OverFeat [34] and
B. Test Vehicle Setup                                             R-CNN [35] are among pioneering works that employ deep
   Equipped with multiple sensors introduced in Sec. II-A,        learning for object detection. In these works, ROIs are first
many autonomous driving tests have been conducted. For            generated by the sliding window approach (OverFeat [34])
example, the Tartan Racing Team developed an autonomous           or selective search (R-CNN [35]) and then advanced into a
vehicle called “Boss” and won the DARPA Urban Challenge           regional CNN to extract features for object classification and
in 2007 (cf. Fig. 3(a)) [2]. The vehicle was equipped with a      bounding box regression. SPPnet [36] and Fast-RCNN [37]
camera and several Radars and LiDARs. Google (Waymo) has          propose to obtain regional features directly from global feature
tested their driverless cars in more than 20 US cities driving    maps by applying a larger CNN (e.g. VGG [38], ResNet [39],
8 million miles on public roads (cf. Fig. 3(b)) [14]; BMW         GoogLeNet [40]) on the whole image. Faster R-CNN [41]
has tested autonomous driving on highways around Munich           unifies the object detection pipeline and adopts the Region
since 2011 [15]; Daimler mounted a stereo camera, two mono        Proposal Network (RPN), a small fully-connected network, to
cameras, and several Radars on a Mercedes Benz S-Class car        slide over the high-level CNN feature maps for ROI generation
                                                                                                                                                                                        4

                                                 Region Proposal Network (RPN)
                                                                                                                       pixel-wise semantic segmentation for multiple classes includ-
                                                                    Objectness
                                                                   classification                                      ing road, car, bicycle, column-pole, tree, sky, etc; [52] and [63]
                                                                   Bounding box                                        concentrate on road segmentation; and [51], [64], [65] deal
                                                                    regression
                                                                                                                       with instance segmentation for various traffic participants.
                                                                                    Faster-RCNN Header network
                                                  ROI generation
                                                                                                   Bounding box
                                                                                                                          Similar to object detection introduced in Sec. II-C, semantic
                                                                                                    refinement
                                                                                                                       segmentation can also be classified into two-stage and one-
   Input image
                 Pre-processing Network                                                                                stage pipelines. In the two-stage pipeline, region proposals are
                 (ResNet, VGG, GoogLeNet etc.)                                                       Object class
                                                                                                   probability score   first generated and then fine-tuned mainly for instance-level
                                                                                    For each ROI
                                                                                                                       segmentation (e.g. R-CNN [66], SDS [67], Mask-RCNN [64]).
                                                                                                                       A more common way for a semantic segmentation is the
Fig. 4: The Faster R-CNN object detection network. It consists
                                                                                                                       one-stage pipeline based on a Fully Convolutional Network
of three parts: a pre-processing network to extract high-
                                                                                                                       (FCN) originally proposed by Long et al. [68]. In this work,
level image features, a Region Proposal Network (RPN) that
                                                                                                                       the fully-connected layers in a CNN classifier for predicting
produces region proposals, and a Faster-RCNN head which
                                                                                                                       classification scores are replaced with convolutional layers
fine-tunes each region proposal.
                                                                                                                       to produce coarse output maps. These maps are then up-
                                                                                                                       sampled to dense pixel labels by backwards convolution (i.e.
                                                                                                                       deconvolution). Kendall et al. [62] extend FCN by intro-
(cf. Fig. 4). Following this line, R-FCN [42] proposes to
                                                                                                                       ducing an encoder-decoder CNN architecture. The encoder
replace fully-connected layers in an RPN with convolutional
                                                                                                                       serves to produce hierarchical image representations with a
layers and builds a fully-convolutional object detector.
                                                                                                                       CNN backbone such as VGG or ResNet (removing fully-
   2) One-stage Object Detection: This method aims to map
                                                                                                                       connected layers). The decoder, conversely, restores these low-
the feature maps directly to bounding boxes and classification
                                                                                                                       dimensional features back to original resolution by a set of
scores via a single-stage, unified CNN model. For example,
                                                                                                                       upsampling and convolution layers. The restored feature maps
MultiBox [43] predicts a binary mask from the entire input
                                                                                                                       are finally used for pixel-label prediction.
image via a CNN and infers bounding boxes at a later
                                                                                                                          Global image information provides useful context cues for
stage. YOLO [44] is a more complete unified detector which
                                                                                                                       semantic segmentation. However, vanilla CNN structures only
regresses the bounding boxes directly from the CNN model.
                                                                                                                       focus on local information with limited receptive fields. In
SSD [45] handles objects with various sizes by regressing
                                                                                                                       this regard, many methods have been proposed to incorporate
multiple feature maps of different resolution with small con-
                                                                                                                       global information, such as dilated convolutions [69], [70],
volutional filters to predict multi-scale bounding boxes.
                                                                                                                       multi-scale prediction [71], as well as adding Conditional
   In general, two-stage object detectors like Faster-RCNN
                                                                                                                       Random Fields (CRFs) as post-processing step [72].
tend to achieve better detection accuracy due to the region
                                                                                                                          Real-time performance is important in autonomous driving
proposal generation and refinement paradigm. This comes with
                                                                                                                       applications. However, most works only focus on segmen-
the cost of higher inference time and more complex training.
                                                                                                                       tation accuracy. In this regard, Siam et al. [73] made a
Conversely, one-stage object detectors are faster and easier to
                                                                                                                       comparative study on the real-time performance among several
be optimized, yet under-perform compared to two-stage object
                                                                                                                       semantic segmentation architectures, regarding the operations
detectors in terms of accuracy. Huang et al. [46] systemati-
                                                                                                                       (GFLOPs) and the inference speed (fps).
cally evaluate the speed/accuracy trade-offs for several object
detectors and backbone networks.
                                                                                                                                      III. M ULTI - MODAL DATASETS
                                                                                                                         Most deep multi-modal perception methods are based on
D. Deep Semantic Segmentation
                                                                                                                       supervised learning. Therefore, multi-modal datasets with la-
   The target of semantic segmentation is to partition a scene                                                         beled ground-truth are required for training such deep neural
into several meaningful parts, usually by labeling each pixel in                                                       networks. In the following, we summarize several real-world
the image with semantics (pixel-level semantic segmentation)                                                           datasets published since 2013, regarding sensor setups, record-
or by simultaneously detecting objects and doing per-instance                                                          ing conditions, dataset size and labels (cf. Tab. II). Note that
per-pixel labeling (instance-level semantic segmentation). Re-                                                         there exist some virtual multi-modal datasets generated from
cently, panoptic segmentation [47] is proposed to unify pixel-                                                         game engines. We will discuss them in Sec. VI-A1.
level and instance-level semantic segmentation, and it starts to
get more attentions for autonomous driving [48]–[50]. Though
semantic segmentation was first introduced to process camera                                                           A. Sensing Modalities
images, many methods have been proposed for segmenting                                                                    All reviewed datasets include RGB camera images. In
LiDAR points as well (e.g. [51]–[56]).                                                                                 addition, [6], [60], [74]–[89] provide LiDAR point clouds,
   Many datasets have been published for semantic segmen-                                                              and [90]–[92] thermal images. The KAIST Multispectral
tation, such as Cityscape [57], KITTI [6], Toronto City [58],                                                          Dataset [93] provides both thermal images and LiDAR data.
Mapillary Vistas [59], and ApolloScape [60]. These datasets                                                            Bus data is included additionally in [87]. Only the very
advance the deep learning research for semantic segmentation                                                           recently nuScenes [89], Oxford Radar RobotCar [85] and
in autonomous driving. For example, [54], [61], [62] focus on                                                          Astyx HiRes2019 Datasets [94] provide Radar data.
                                                                                                                                                                          5

B. Recording Conditions                                                                        1
                                                                                                          Car                                                      1.4M

   Even though the KITTI dataset [75] is widely used for                                                  Person
                                                                                              0.8
                                                                                                          Cyclist
autonomous driving research, the diversity of its recording

                                                                      Normalized proportion

                                                                                                                    # of image frames
conditions is relatively low: it is recorded in Karlsruhe - a                                 0.6

mid-sized city in Germany, only during daytime and on sunny
                                                                                              0.4
days. Other reviewed datasets such as [60], [78], [79], [82],
[87]–[89] are recorded in more than one location. To increase                                 0.2                                                           200K
                                                                                                                                                     144K
the diversity of lighting conditions, [60], [80]–[82], [82], [84],                                                                      15K   8.9K
                                                                                               0
[86], [88]–[92] collect data in both daytime and nighttime, and
[93] considers various lighting conditions throughout the day,
                                                                                                    (a)                                              (b)
including sunrise, morning, afternoon, sunset, night, and dawn.
The Oxford Dataset [74] and the Oxford Radar RobotCar                Fig. 5: (a). Normalized percentage of objects of car, person,
Dataset [85] are collected by driving the car around the             and cyclist classes in KAIST Multispectral [93], KITTI [6],
Oxford area during the whole year. It contains data under            Apolloscape [60] (E: easy, M: moderate, and H: hard refer
different weather conditions, such as heavy rain, night, direct      to the number of moveable objects in the frame - details can
sunlight and snow. Other datasets containing diverse weather         be found in [60]), and nuScene dataset [89]. (b). Number of
conditions are [60], [86], [88], [89]. In [95], LiDAR is used as     camera image frames in several datasets. An increase by two
a reference sensor for generating ground-truth, hence we do          orders of magnitude of the dataset size can be seen.
not consider it a multi-modal dataset. However the diversity
in the recording conditions is large, ranging from dawn to
night, as well as reflections, rain and lens flare. The cross-       cone, and trash can. The Eurocity dataset [88] focuses on
season dataset [96] emphasizes the importance of changes             vulnerable road-users (mostly pedestrian). Instead of labeling
throughout the year. However, it only provides camera images         objects, [77] provides a dataset for place categorization. Scenes
and labels for semantic segmentation. Similarly, the visual          are classified into forest, coast, residential area, urban area and
localization challenge and the corresponding benchmark [97]          indoor/outdoor parking lot. [78] provides vehicle speed and
cover weather and season diversity (but no new multi-modal           wheel angles for driving behavior predictions. The BLV3D
dataset is introduced). The recent Eurocity dataset [88] is          dataset [80] provides unique labeling for interaction and in-
the most diverse dataset we have reviewed. It is recorded in         tention.
different cities from several European countries. All seasons           The object classes are very imbalanced. Fig. 5(a) compares
are considered, as well as weather and daytime diversity. To         the percentage of car, person, and cyclist classes from four
date, the dataset is camera-only and other modalities (e.g.          reviewed datasets. There are much more objects labeled as
LiDARs) are announced.                                               car than person or cyclist.

                                                                     IV. D EEP M ULTI - MODAL P ERCEPTION P ROBLEMS FOR
C. Dataset Size
                                                                                   AUTONOMOUS D RIVING
   The dataset size ranges from only 1,569 frames up to over
                                                                       In this section, we summarize deep multi-modal perception
11 million frames. The largest dataset with ground-truth labels
                                                                     problems for autonomous driving based on sensing modalities
that we have reviewed is the nuScenes Dataset [89] with nearly
                                                                     and targets. An overview of the existing methods is shown in
1,4M frames. Compared to the image datasets in the computer
                                                                     Tab. III and Tab. IV. An accuracy and runtime comparison
vision community, the multi-modal datasets are still relatively
                                                                     among several methods is shown in Tab. V and Tab. VI.
small. However, the dataset size has grown by two orders of
magnitudes between 2014 and 2019 (cf. Fig. 5(b)).
                                                                     A. Deep Multi-modal Object Detection
                                                                       1) Sensing Modalities: Most existing works combine RGB
D. Labels                                                            images from visual cameras with 3D LiDAR point clouds
   Most of the reviewed datasets provide ground-truth labels         [98]–[116]. Some other works focus on fusing the RGB
for 2D object detection and semantic segmentation tasks [60],        images from visual cameras with images from thermal cameras
[75], [88], [90]–[93]. KITTI [75] also labels tracking, optical      [91], [117]–[119]. Furthermore, Mees et al. [120] employ a
flow, visual odometry, and depth for various computer vision         Kinect RGB-D camera to fuse RGB images and depth images;
problems. BLV3D [80] provides labels for tracking, interaction       Schneider et al. [61] generate depth images from a stereo
and intention. Labels for 3D scene understanding are provided        camera and combine them with RGB images; Yang et al. [121]
by [60], [75], [79]–[84], [89].                                      and Cascas et al. [122] leverage HD maps to provide prior
   Depending on the focus of a dataset, objects are labeled          knowledge of the road topology.
into different classes. For example, [90] only contains label          2) 2D or 3D Detection: Many works [61], [91], [99]–
for people, including distinguishable individuals (labeled as        [101], [106], [108], [109], [111], [117]–[120], [123] deal
“Person”), non-distinguishable individuals (labeled as “Peo-         with the 2D object detection problem on the front-view 2D
ple”), and cyclists; [60] classifies objects into five groups, and   image plane. Compared to 2D detection, 3D detection is
provides 25 fine-grained labels, such as truck, tricycle, traffic    more challenging since the object’s distance to the ego-vehicle
                                                                                                                                    6

needs to be estimated. Therefore, accurate depth information        features (Horizontal disparity, Height, Angle) [66], or any
provided by LiDAR sensors is highly beneficial. In this regard,     other 3D coordinate system. The reflectance information is
some papers including [98], [102]–[105], [107], [113], [115]        given by intensity.
combine RGB camera images and LiDAR point clouds for                   There are mainly three ways to process point clouds. One
3D object detection. In addition, Liang et al. [116] propose        way is by discretizing the 3D space into 3D voxels and as-
a multi-task learning network to aid 3D object detection. The       signing the points to the voxels (e.g. [29], [113], [135]–[137]).
auxiliary tasks include camera depth completion, ground plane       In this way, the rich 3D shape information of the driving
estimation, and 2D object detection. How to represent the           environment can be preserved. However, this method results in
modalities properly is discussed in section V-A.                    many empty voxels as the LiDAR points are usually sparse and
   3) What to detect: Complex driving scenarios often contain       irregular. Processing the sparse data via clustering (e.g. [100],
different types of road users. Among them, cars, cyclists, and      [106]–[108]) or 3D CNN (e.g. [29], [136]) is usually very
pedestrians are highly relevant to autonomous driving. In this      time-consuming and infeasible for online autonomous driving.
regard, [98], [99], [106], [108], [110] employ multi-modal          Zhou et al. [135] propose a voxel feature encoding (VFE) layer
neural networks for car detection; [101], [108], [109], [117]–      to process the LiDAR points efficiently for 3D object detec-
[120] focus on detecting non-motorized road users (pedestrians      tion. They report an inference time of 225 ms on the KITTI
or cyclists); [61], [91], [100], [102]–[105], [111], [115], [116]   dataset. Yan et al. [138] add several sparse convolutional layers
detect both.                                                        after the VFE to convert the sparse voxel data into 2D images,
                                                                    and then perform 3D object detection on them. Unlike the
                                                                    common convolution operation, the sparse convolution only
B. Deep Multi-modal Semantic Segmentation
                                                                    computes on the locations associated with input points. In
   Compared to the object detection problem summarized in           this way, they save a lot of computational cost, achieving an
Sec. IV-A, there are fewer works on multi-modal semantic            inference time of only 25 ms.
segmentation: [92], [119], [124] employ RGB and thermal                The second way is to directly learn over 3D LiDAR points in
images, [61] fuses RGB images and depth images from a               continuous vector space without voxelization. PointNet [139]
stereo camera, [125]–[127] combine RGB, thermal, and depth          and its improved version PointNet++ [140] propose to predict
images for semantic segmentation in diverse environments            individual features for each point and aggregate the features
such as forests, [123] fuses RGB images and LiDAR point             from several points via max pooling. This method was firstly
clouds for off-road terrain segmentation and [128]–[132] for        introduced in 3D object recognition and later extended by Qi et
road segmentation. Apart from the above-mentioned works for         al. [105], Xu et al. [104] and Shin et al. [141] to 3D object de-
semantic segmentation on the 2D image plane, [125], [133]           tection in combination with RGB images. Furthermore, Wang
deal with 3D segmentation on LiDAR points.                          et al. [142] propose a new learnable operator called Parametric
                                                                    Continuous Convolution to aggregate points via a weighted
                     V. M ETHODOLOGY                                sum, and Li et al. [143] propose to learn a χ transformation
   When designing a deep neural network for multi-modal             before applying transformed point cloud features into standard
perception, three questions need to be addressed - What to          CNN. They are tested in semantic segmentation or LiDAR
fuse: what sensing modalities should be fused, and how to           motion estimation tasks.
represent and process them in an appropriate way; How to               A third way to represent 3D point clouds is by projecting
fuse: what fusion operations should be utilized; When to fuse:      them onto 2D grid-based feature maps so that they can be
at which stage of feature representation in a neural network        processed via 2D convolutional layers. In the following, we
should the sensing modalities be combined. In this section,         distinguish among spherical map, camera-plane map (CPM),
we summarize existing methodologies based on these three            as well as bird’s eye view (BEV) map. Fig. 6 illustrates
aspects.                                                            different LiDAR representations in 2D.
                                                                       A spherical map is obtained by projecting each 3D point
                                                                    onto a sphere, characterized by azimuth and zenith angles.
A. What to Fuse                                                     It has the advantage of representing each 3D point in a
   LiDARs and cameras (visual cameras, thermal cameras) are         dense and compact way, making it a suitable representation
the most common sensors for multi-modal perception in the           for point cloud segmentation (e.g. [51]). However, the size
literature. While the interest in processing Radar signals via      of the representation can be different from camera images.
deep learning is growing, only a few papers discuss deep            Therefore, it is difficult to fuse them at an early stage. A
multi-modal perception with Radar for autonomous driving            CPM can be produced by projecting the 3D points into the
(e.g. [134]). Therefore, we focus on several ways to represent      camera coordinate system, provided the calibration matrix. A
and process LiDAR point clouds and camera images sepa-              CPM can be directly fused with camera images, as their sizes
rately, and discuss how to combine them together. In addition,      are the same. However, this representation leaves many pixels
we briefly summarize Radar perception using deep learning.          empty. Therefore, many methods have been proposed to up-
   1) LiDAR Point Clouds: LiDAR point clouds provide both           sample such a sparse feature map, e.g. mean average [111],
depth and reflectance information of the environment. The           nearest neighbors [144], or bilateral filter [145]. Compared
depth information of a point p can be encoded by its Cartesian      to the above-mentioned feature maps which encode LiDAR
coordinates [x, y, z], distance x2 + y2 + z2 , density, or HHA      information in the front-view, a BEV map avoids occlusion
                                                                                                                                    7

                                                                    view that is commonly used for LiDAR point clouds might
                                                                    be a better representation. Roddick et al. [147] propose a
                                                                    Orthographic Feature Transform (OFT) algorithm to project
                                                                    the RGB image features onto the BEV plane. The BEV feature
         (a) RGB camera image           (e) LiDAR spherical map
                                                                    maps are further processed for 3D object detection from
                                                                    monocular camera images. Lv et al. [130] project each image
                                                                    pixel with the corresponding LiDAR point onto the BEV plane
                                                                    and fuse the multi-modal features for road segmentation. Wang
        (b) LiDAR sparse depth map                                  et al. [148] and their successive work [149] propose to convert
                                                                    RGB images into pseudo-lidar representation by estimating
                                                                    the image depth, and then use state-of-the-art BEV LiDAR
                                                                    detector to significantly improve the detection performance.
                                                                       3) Processing LiDAR Points and Camera Images in Deep
        (c) LiDAR dense depth map
                                                                    Multi-modal Perception: Tab. III and Tab. IV summarize
                                                                    existing methods to process sensors’ signals for deep multi-
                                                                    modal perception, mainly LiDAR points and camera images.
                                                                    From the tables we have three observations: (1). Most works
       (d) LiDAR dense intensity map   (f) LiDAR BEV density map    propose to fuse LiDAR and camera features extracted from 2D
                                                                    convolution neural networks. To do this, they project LiDAR
                                                                    points on the 2D plane and process the feature maps through
Fig. 6: RGB image and different 2D LiDAR representation
                                                                    2D convolutions. Only a few works extract LiDAR features
methods. (a) A standard RGB image, represented by a pixel
                                                                    by PointNet (e.g. [104], [105], [128]) or 3D convolutions
grid and color channel values. (b) A sparse (front-view)
                                                                    (e.g. [123]); (2). Several works on multi-modal object detec-
depth map obtained from LiDAR measurements represented
                                                                    tion cluster and segment 3D LiDAR points to generate 3D
on a grid. (c) Interpolated depth map. (d) Interpolation of
                                                                    region proposals (e.g. [100], [106], [108]). Still, they use a
the measured reflectance values on a grid. (e) Interpolated
                                                                    LiDAR 2D representation to extract features for fusion; (3).
representation of the measured LiDAR points (surround view)
                                                                    Several works project LiDAR points on the camera-plane or
on a spherical map. (f) Projection of the measured LiDAR
                                                                    RGB camera images on the LiDAR BEV plane (e.g. [130],
points (front-facing) to bird’s eye view (no interpolation).
                                                                    [131], [150]) in order to align the features from different
                                                                    sensors, whereas many works propose to fuse LiDAR BEV
problems because objects occupy different space in the map.         features directly with RGB camera images (e.g. [98], [103]).
In addition, the BEV preserves the objects’ length and width,       This indicates that the networks implicitly learn to align
and directly provides the objects’ positions on the ground          features of different viewpoints. Therefore, a well-calibrated
plane, making the localization task easier. Therefore, the          sensor setup with accurate spatial and temporal alignment is
BEV map is widely applied to 3D environment perception.             the prerequisite for accurate multi-modal perception, as will
For example, Chen et al. [98] encode point clouds by height,        be discussed in Sec. VI-A2.
density and intensity maps in BEV. The height maps are                 4) Radar Signals: Radars provide rich environment infor-
obtained by dividing the point clouds into several slices. The      mation based on received amplitudes, ranges, and the Doppler
density maps are calculated as the number of points within          spectrum. The Radar data can be represented by 2D feature
a grid cell, normalized by the number of channels. The              maps and processed by convolutional neural networks. For
intensity maps directly represent the reflectance measured          example, Lombacher et al. employ Radar grid maps made by
by the LiDAR on a grid. Lang et al. [146] argue that the            accumulating Radar data over several time-stamps [151] for
hard-coded features for BEV representation may not be               static object classification [152] and semantic segmentation
optimal. They propose to learn features in each column of           [153] in autonomous driving. Visentin et al. show that CNNs
the LiDAR BEV representation via PointNet [139], and feed           can be employed for object classification in a post-processed
these learnable feature maps to standard 2D convolution             range-velocity map [154]. Kim et al. [155] use a series
layers.                                                             of Radar range-velocity images and convolutional recurrent
                                                                    neural networks for moving objects classification. Moeness et
   2) Camera Images: Most methods in the literature employ          al. [156] feed spectrogram from Time Frequency signals as 2D
RGB images from visual cameras or one type of infrared              images into a stacked auto-encoders to extract high-level Radar
images from thermal cameras (near-infrared, mid-infrared,           features for human motion recognition. The Radar data can
far-infrared). Besides, some works extract additional sensing       also be represented directly as “point clouds” and processed
information, such as optical flow [120], depth [61], [125],         by PointNet++ [140] for dynamic object segmentation [157].
[126], or other multi-spectral images [91], [125].                  Besides, Woehler et al. [158] encode features from a cluster
   Camera images provide rich texture information of the            of Radar points for dynamic object classification. Chadwick et
driving surroundings. However, objects can be occluded and          al. [134] first project Radar points on the camera plane to build
the scale of a single object can vary significantly in the camera   Radar range-velocity images, and then combine with camera
image plane. For 3D environment inference, the bird’s eye           images for distant vehicle detection.
                                                                                                                                              8

     Expert Network i                                                C. When to Fuse
                                                                        Deep neural networks represent features hierarchically and
                                                                     offer a wide range of choices to combine sensing modalities at
     Expert Network j                                     Addition   early, middle, or late stages (Fig. 8). In the sequel, we discuss
                                                                     the early, middle, and late fusions in detail. For each fusion
                                         Gating Network              scheme, we first give mathematical descriptions using the same
                           Combined                                  notations as in Sec. V-B, and then discuss their properties.
                           features of
                           experts                                   Note that there exists some works that fuse features from the
                                                                     early stage till late stages in deep neural networks (e.g. [161]).
Fig. 7: An illustration of the Mixture of Experts fusion method.     For simplicity, we categorize this fusion scheme as “middle
Here we show the combined features which are derived from            fusion”. Compared to the semantic segmentation where multi-
the output layers of the expert networks. They can be extracted      modal features are fused at different stages in FCN, there exist
from the intermediate layers as well.                                more diverse network architectures and more fusion variants
                                                                     in object detection. Therefore, we additionally summarize the
                                                                     fusion methods specifically for the object detection problem.
B. How to Fuse                                                       Finally, we discuss the relationship between the fusion opera-
                                                                     tion and the fusion scheme.
   This section summarizes typical fusion operations in a deep          Note that we do not find conclusive evidence from the
neural network. For simplicity we restrict our discussion to two     methods we have reviewed that one fusion method is better
sensing modalities, though more still apply. Denote Mi and M j       than the others. The performance is highly dependent on
                                             M
as two different modalities, and flMi and fl j their feature maps    sensing modalities, data, and network architectures.
in the l th layer of the neural network. Also denote Gl (·) as a        1) Early Fusion: This method fuses the raw or pre-
                                                                                                                  Mi     M
mathematical description of the feature transformation applied       processed sensor data. Let us define fl = fl−1  ⊕ fl−1j as a fusion
in layer l of the neural network.                                    operation introduced in Sec. V-B. For a network that has L + 1
   1) Addition or Average Mean: This join operation
                                                             adds
                                                                    layers, an early fusion scheme can be described as:
                                                      Mi     Mj
the feature maps element-wise, i.e. fl = Gl−1 fl−1 + fl−1 ,                                                               
                                                                                                                               !
                                                                                                                      M
                                                                         fL = GL GL−1 · · · Gl · · · G2 G1 ( f0Mi ⊕ f0 j )
                                                                                                                          
or calculates the average mean of the feature maps.                                                                              , (2)
   2) Concatenation:
                         Combines feature maps by fl =
          Mi _ M j
Gl−1 fl−1 fl−1 . The feature maps are usually stacked along          with l = [1, 2, · · · , L]. Early fusion has several pros and cons.
their depth before they are advanced to a convolution layer. For     First, the network learns the joint features of multiple modal-
a fully connected layer, these features are usually flattened into   ities at an early stage, fully exploiting the information of the
vectors and concatenated along the rows of the feature maps.         raw data. Second, early fusion has low computation require-
   3) Ensemble: This operation ensembles feature                     ments and a low memory budget as it jointly processes the
                                                          maps
                                                                     multiple sensing modalities. This comes with the cost of model
                                                               
                                                           Mi
from different sensing modalities via fl = Gl−1 fl−1             ∪
                                                                   inflexibility. As an example, when an input is replaced with a
          Mj
Gl−1 fl−1 . As will be introduced in the following sections          new sensing modality or the input channels are extended, the
(Sec. V-C4 and Sec. V-C5), ensembles are often used to fuse          early fused network needs to be retrained completely. Third,
ROIs in object detection networks.                                   early fusion is sensitive to spatial-temporal data misalignment
   4) Mixture of Experts: The above-mentioned fusion opera-          among sensors which are caused by calibration error, different
tions do not consider the informativeness of a sensing modality      sampling rate, and sensor defect.
(e.g. at night time RGB camera images bring less information              2) Late Fusion: This fusion scheme combines decision
than LiDAR points). These operations are applied, hoping that        outputs of each domain specific network of a sensing modality.
the network can implicitly learn to weight the feature maps.         It can be described as:
In contrast, the Mixture of Experts (MoE) approach explicitly
                                                                                                                                           
                                                                                                               M    Mj          M       M 
                                                                      f L = GM i   Mi            Mi Mi 
                                                                              L GL−1 · · · G1 ( f 0 )      ⊕GL j GL−1    · · · G1 j ( f 0 j ) .
models the weight of a feature map. It is first introduced
in [159] for neural networks and then extended in [120], [126],                                                                              (3)
[160]. As Fig. 7 illustrates, the feature map of a sensing           Late fusion has high flexibility and modularity. When a
modality is processed by its domain-specific network called          new sensing modality is introduced, only its domain specific
“expert”. Afterwards, the outputs of multiple expert networks        network needs to be trained, without affecting other networks.
are averaged with the weights wMi , wM j predicted by a gating       However, it suffers from high computation cost and memory
network which takes the combined features output by the              requirements. In addition, it discards rich intermediate features
expert networks as inputs h via a simple fusion operation such       which may be highly beneficial when being fused.
as concatenation:                                                         3) Middle Fusion: Middle fusion is the compromise of
                                                                     early and late fusion: It combines the feature representations
                                                                     from different sensing modalities at intermediate layers. This
                                    
                    Mi           M
   fl = Gl wMi · fl−1  + wM j · fl−1j , with wMi + wM j = 1. (1)
                                                                     enables the network to learn cross modalities with different
                                                                     feature representations and at different depths. Define l ? as
                                                                                                                                                 9

                     (a) Early Fusion                         (b) Late Fusion                           (c) Middle Fusion
                                                                                                       fusion in one layer

                                                                                                   Modality         Intermediate layers

                                                                                                 Network output      Fusion operation

                    (d) Middle Fusion                         (e) Middle Fusion
                       deep fusion                             short-cut fusion

                       Fig. 8: An illustration of early fusion, late fusion, and several middle fusion methods.

the layer from which intermediate features begin to be fused. Chen et al. [98] use LiDAR BEV maps to generate region
The middle fusion can be executed at this layer only once:                         proposals. For each ROI, the regional features from the LiDAR
                                                                             BEV maps are fused with those from the LiDAR front-view
                                                                                
                                                         Mj         Mj Mj 
 fL = GL · · · Gl ? +1 GM     l?
                                 i
                                    · · · G Mi Mi 
                                            1 ( f 0 ) ⊕G l? · · · G 1 ( f 0 )    . maps as well as camera images via deep fusion. Compared
                                                                             (4) to object detections from LiDAR point clouds, camera images
Alternatively, they can be fused hierarchically, such as by deep have been well investigated with larger labeled dataset and bet-
fusion [98], [162]:                                                                ter 2D detection performance. Therefore, it is straightforward
                                                                                   to exploit the predictions from well-trained image detectors
                 Mi        Mj
      fl +1 = fl ? ⊕ fl ? ,
        ?                                                                          when doing camera-LiDAR fusion. In this regard, [104],
                                  M
                                                                             (5)   [105], [107] propose to utilize a pre-trained image detector to
      fk+1 = GM                     j                  ?
                 k ( f k ) ⊕ Gk ( f k ), ∀k : k ∈ {l + 1, · · · , L} .
                   i
                                                                                   produce 2D bounding boxes, which build frustums in LiDAR
or “short-cut fusion” [92]:                                                        point clouds. Then, they use these point clouds within the
                              M                                                    frustums for 3D object detection. Fig. 9 shows some exemplary
          fl+1 = flMi ⊕ fl j ,                                                     fusion architectures for two-stage object detection networks.
                            Mi        Mj                                     (6)   Tab. III summarizes the methodologies for multi-modal object
          fk+1 = fk ⊕ fk? ⊕ fk? ,
                                                                                   detection.
          ∀k : k ∈ {l + 1, · · · , L} ; ∃k? : k? ∈ {1, · · · , l − 1} .
                                                                                      5) Fusion Operation and Fusion Scheme: Based on the
Although the middle fusion approach is highly flexible, it is papers that we have reviewed, feature concatenation is the
not easy to find the “optimal” way to fuse intermediate layers most common operation, especially at early and middle stages.
given a specific network architecture. We will discuss this Element-wise average mean and addition operations are ad-
challenge in detail in Sec. VI-B3.                                                 ditionally used for middle fusion. Ensemble and Mixture of
    4) Fusion in Object Detection Networks: Modern multi- Experts are often used for middle to decision level fusion.
modal object detection networks usually follow either the
two-stage pipeline (RCNN [35], Fast-RCNN [37], Faster-
                                                                                            VI. C HALLENGES AND O PEN Q UESTIONS
RCNN [41]) or the one-stage pipeline (YOLO [44] and
SSD [45]), as explained in detail in Sec. II-C. This offers                           As discussed in the Introduction (cf. Sec. I), developing
a variety of alternatives for network fusion. For instance, the deep multi-modal perception systems is especially challenging
sensing modalities can be fused to generate regional proposals for autonomous driving because it has high requirements in ac-
for a two-stage object detector. The regional multi-modal curacy, robustness, and real-time performance. The predictions
features for each proposal can be fused as well. Ku et al. [103] from object detection or semantic segmentation are usually
propose AVOD, an object detection network that fuses RGB transferred to other modules such as maneuver prediction
images and LiDAR BEV images both in the region proposal and decision making. A reliable perception system is the
network and the header network. Kim et al. [109] ensemble the prerequisite for a driverless car to run safely in uncontrolled
region proposals that are produced by LiDAR depth images and complex driving environments. In Sec. III and Sec. V
and RGB images separately. The joint region proposals are we have summarized the multi-modal datasets and fusion
then fed to a convolutional network for final object detection. methodologies. Correspondingly, in this section we discuss the
                                                                                                                                                                                                                            10

            LiDAR BEV map                                                                                           LiDAR BEV map
                                               Projection
                                              and pooling
                                                     3D ROI                                                                                                                           Projection
                                               3D ROI                                                                                                                                and pooling
                                              generation
                                                                                                                                                  Projection                      3D ROI
                                                     3D ROI                                                                                      and pooling
           LiDAR front view map
                                                                                                                                                                                      3D ROI                    3D object
                                                                                                                          3D Anchors                                  Fusion                       Fusion
                                                         Projection                        3D object                                                                                 generation                 detection
                                                                            Fusion
                                                        and pooling                        detection                                              Projection
                                                                                                                                                 and pooling
                                                                                                                                                                                  3D ROI
                                                      3D ROI
                                                                                                                   RGB camera image
            RGB camera image
                                                         Projection                                                                                                                   Projection
                                                        and pooling                                                                                                                  and pooling

                                        (a) MV3D                                                                                                               (b) AVOD

                                                                LiDAR frustum proposal
                                                                                                                          LiDAR front view map

                                                                                                                                                     2D ROI
                                                                                                                                                    generation

                                                                                                                                                          2D ROI
                                                                            Point Cloud        3D object                                                             2D ROI                             2D object
                                                                                                                                                      Fusion                    Projection
                                                                           Segmentation        detection                                                                                                detection
                                                                                                                                                    (ensemble)                 and pooling
                                                    2D ROI
      RGB camera image                                                                                                     RGB camera image               2D ROI
                                                                  Object class
                                          2D object detection                                                                                        2D ROI
                                                                                                                                                    generation

                                  (c) Frustum PointNet                                                                                                 (d) Ensemble Proposals

Fig. 9: Examplary fusion architectures for two-stage object detection networks. (a). MV3D [98]; (b). AVOD [103]; (c). Frustum
PointNet [105]; (d). Ensemble Proposals [109].

                                          TABLE I: AN OVERVIEW OF CHALLENGES AND OPEN QUESTIONS
                               Topics                                                                     Challenges                                                              Open Questions
                                               Data diversity                    •   Relative small size of training dataset.                                  • Develop more realistic virtual datasets.
                                                                                 •   Limited driving scenarios and conditions, limited sensor                  • Finding optimal way to combine real- and virtual data.
                                                                                     variety, object class imbalance.                                          • Increasing labeling efficiency through cross-modal label-
                                                                                                                                                                 ing, active learning, transfer learning, semi-supervised
                                                                                                                                                                 learning etc. Leveraging lifelong learning to update net-
  Multi-modal data preparation                                                                                                                                   works with continual data collection.

                                                Data quality                     •   Labeling errors.                                                          • Teaching network robustness with erroneous and noisy
                                                                                 •   Spatial and temporal misalignment of different sensors.                     labels.
                                                                                                                                                               • Integrating prior knowledge in networks.
                                                                                                                                                               • Developing methods (e.g. using deep learning) to
                                                                                                                                                                 automatically register sensors.
                                              “What to fuse”                     •   Too few sensing modalities are fused.                                     • Fusing multiple sensors with the same modality.
                                                                                 •   Lack of studies for different feature representations.                    • Fusing more sensing modalities, e.g. Radar, Ultrasonic,
                                                                                                                                                                 V2X communication.
                                                                                                                                                               • Fusing with physical models and prior knowledge, also
                                                                                                                                                                 possible in the multi-task learning scheme.
                                                                                                                                                               • Comparing different feature representation w.r.t informa-
                                                                                                                                                                 tiveness and computational costs.

    Fusion methodology                        “How to fuse”                      •   Lack of uncertainty quantification for each sensor chan-                  • Uncertainty estimation via e.g. Bayesian neural networks
                                                                                     nel.                                                                        (BNN).
                                                                                 •   Too simple fusion operations.                                             • Propagating uncertainties to other modules, such as track-
                                                                                                                                                                 ing and motion planning.
                                                                                                                                                               • Anomaly detection by generative models.
                                                                                                                                                               • Developing fusion operations that are suitable for
                                                                                                                                                                 network pruning and compression.

                                              “When to fuse”                     •   Fusion architecture is often designed by empirical results.               • Optimal fusion architecture search.
                                                                                     No guideline for optimal fusion architecture design.                      • Incorporating requirements of computation time or mem-
                                                                                 •   Lack of study for accuracy/speed or memory/robustness                       ory as regularization term.
                                                                                     trade-offs.                                                               • Using visual analytics tool to find optimal fusion
                                                                                                                                                                 architecture.
                                            Evaluation metrics                   •   Current metrics focus on comparing networks’ accuracy.                    •   Metrics to quantify the networks’ robustness should
            Others
                                                                                                                                                                   be developed and adapted to multi-modal perception
                                                                                                                                                                   problems.

                                        More network architectures               • Current networks lack temporal cues and cannot guaran-                      • Using Recurrent Neural Network (RNN) for sequential
                                                                                   tee prediction consistency over time.                                         perception.
                                                                                 • They are designed mainly for modular autonomous                             • Multi-modal end-to-end learning or multi-modal direct-
                                                                                   driving.                                                                      perception.
                                                                                                                                                                                      11

remaining challenges and open questions for multi-modal data          (a) “collaborative labeling”

preparation and network architecture design. We focus on how
to improve the accuracy and robustness of the multi-modal
perception systems while guaranteeing real-time performance.            Human
                                                                                           Weakly human-labeled LiDAR         Pre-trained LiDAR       Fine-tuned full object labels
We also discuss some open questions, such as evaluation                annotator
                                                                                            data: one click per object       detector (F-PointNet)     (class and bounding box)

metrics and network architecture design. Tab. I summarizes
the challenges and open questions.                                    (b) “collaborative training”                                                         LiDAR data labeled by

                                                                       LiDAR data labeled by a pre-trained SegNet                              +             human annotaters

A. Multi-modal Data Preparation
                                                                                              Semantic labels from   Registrating LiDAR data
   1) Data Diversity: Training a deep neural network on a                                     a pre-trained SegNet    with semantic labels
                                                                                                                                                     Training a LiDAR point SegNet
complex task requires a huge amount of data. Therefore, using
large multi-modal datasets with diverse driving conditions, ob-      Fig. 10: Two examples of increasing data labeling efficiency in
ject labels, and sensors can significantly improve the network’s     LiDAR data. (a) Collaborative labeling LiDAR points for 3D
accuracy and robustness against changing environments. How-          detection [175]: the LiDAR points within each object are firstly
ever, it is not an easy task to acquire real-world data due          weakly-labeled by human annotators, and then fine-tuned
to cost and time limitations as well as hardware constraints.        by a pre-trained LiDAR detector based on the F-PointNet.
The size of open multi-modal datasets is usually much smaller        (b) Collaborative training a semantic segmentation network
than the size of image datasets. As a comparison, KITTI [6]          (SegNet) for LiDAR points [133]: To boost the training data,
records only 80,256 objects whereas ImageNet [163] pro-              a pre-trained image SegNet can be employed to transfer the
vides 1,034,908 samples. Furthermore, the datasets are usually       image semantics.
recorded in limited driving scenarios, weather conditions, and
sensor setups (more details are provided in Sec. III). The           a multi-modal training dataset, it is relatively easy to drive
distribution of objects is also very imbalanced, with much           the test vehicle and collect many data samples. However, it
more objects being labeled as car than person or cyclist             is very tedious and time-consuming to label them, especially
(Fig. 5). As a result, it is questionable how a deep multi-modal     when dealing with 3D labeling and LiDAR points. Lee et
perception system trained with those public datasets performs        al. [175] develop a collaborative hybrid labeling tool, where
when it is deployed to an unstructured environment.                  3D LiDAR point clouds are firstly weakly-labeled by human
   One way to overcome those limitations is by data augmen-          annotators, and then fine-tuned by pre-trained network based
tation via simulation. In fact, a recent work [164] states that      on F-PointNet [105]. They report that the labeling tool can
the most performance gain for object detection in the KITTI          significantly reduce the “task complexity” and “task switch-
dataset is due to data augmentation, rather than advances            ing”, and have a 30× labeling speed-up (Fig. 10(a)). Piewak et
in network architectures. Pfeuffer et al. [111] and Kim et           al. [133] leverage a pre-trained image segmentation network
al. [110] build augmented training datasets by adding artificial     to label LiDAR point clouds without human intervention. The
blank areas, illumination change, occlusion, random noises,          method works by registering each LiDAR point with an image
etc. to the KITTI dataset. The datasets are used to simulate         pixel, and transferring the image semantics predicted by the
various driving environment changes and sensor degradation.          pre-trained network to the corresponding LiDAR points (cf.
They show that trained with such datasets, the network accu-         Fig. 10(b)). In another work, Mei et al. [176] propose a
racy and robustness are improved. Some other works aim at            semi-supervised learning method to do 3D point segmentation
developing virtual simulators to generate varying driving con-       labeling. With only a few manual labels together with pair-
ditions, especially some dangerous scenarios where collecting        wise spatial constraints between adjacent data frames, a lot of
real-world data is very costly or hardly possible. Gaidon et         objects can be labeled. Several works [177]–[179] propose to
al. [165] build a virtual KITTI dataset by introducing a real to     introduce active learning in semantic segmentation or object
virtual cloning method to the original KITTI dataset, using the      detection for autonomous driving. The networks iteratively
Unity Game Engine. Other works [166]–[171] generate virtual          query the human annotator some most informative samples in
datasets purely from game engines, such as GTA-V, without a          an unlabeled data pool and then update the networks’ weights.
proxy of real-world datasets. Griffiths and Boehm [172] create       In this way, much less labeled training data is required while
a purely virtual LiDAR only dataset. In addition, Dosovit-           reaching the same performance and saving human labeling
skiy et al. [173] develop an open-source simulator that can          efforts. There are many other methods in the machine learning
simulate multiple sensors in autonomous driving and Hurl et          literature that aim to reduce data labeling efforts, such as trans-
al. [174] release a large scale, virtual, multi-modal dataset with   fer learning [180], domain adaptation [181]–[185], and semi-
LiDAR data and visual camera. Despite many available virtual         supervised learning [186]. How to efficiently label multi-modal
datasets, it is an open question to which extend a simulator can     data in autonomous driving is an important and challenging
represent real-world phenomena. Developing more realistic            future work, especially in scenarios where the signals from
simulators and finding the optimal way to combine real and           different sensors may not be matched (e.g. due to the distance
virtual data are important open questions.                           some objects are only visible by visual camera but not by
   Another way to overcome the limitations of open datasets          LiDAR). Finally, as there can always be new driving scenarios
is by increasing the efficiency of data labeling. When building      that are different from the training data, it is an interesting
                                                                                                                                                            12

   (a)           1                                        (b)                                 in an end-to-end fashion.
                0.9

                0.8

                                                                                              B. Fusion Methodology
  𝐦𝐀𝐏𝐛𝐚𝐬𝐞𝐥𝐢𝐧𝐞

                0.7

                0.6

                0.5                                             Labeling with random noises      1) What to Fuse: Most reviewed methods combine RGB
                0.4
                                                                                              images with thermal images or LiDAR 3D points. The net-
 𝐦𝐀𝐏

                0.3

                0.2       Labeling with biases                                                works are trained and evaluated on open datasets such as
                0.1       Labeling with random noises
                                                                                              KITTI [6] and KAIST Pedestrian [93]. These methods do
                 0
                      0            50               100
                                                                  Labeling with biases
                                                                                              not specifically focus on sensor redundancy, e.g. installing
                                 Noises δ [px]
                                                                                              multiple cameras on a driverless car to increase the reliability
Fig. 11: (a) An illustration for the influence of label quality                               of perception systems even when some sensors are defective.
on the performance of an object detection network [196]. The                                  How to fuse the sensing information from multiple sensors
network is trained on labels which are incrementally disturbed.                               (e.g. RGB images from multiple cameras) is an important open
The performance is measured by mAP normalized to the                                          question.
performance trained on the undisturbed dataset. The network is                                   Another challenge is how to represent and process different
much more robust against random labeling errors (drawn from                                   sensing modalities appropriately before feeding them into
a Gaussian distribution with variance σ ) than biased labeling                                a fusion network. For instance, many approaches exist to
(all labels shifted by σ ) cf. [194], [195]. (b) An illustration of                           represent LiDAR point clouds, including 3D voxels, 2D BEV
the random labeling noises and labeling biases (all bounding                                  maps, spherical maps, as well as sparse or dense depth maps
boxes are shifted in the upper-right direction).                                              (more details cf. Sec. V-A). However, only Pfeuffer et al. [111]
                                                                                              have studied the pros and cons for several LiDAR front-view
research topic to leverage lifelong learning [187] to update the                              representations. We expect more works to compare different
multi-modal perception network with continual data collection.                                3D point representation methods.
   2) Data Quality and Alignment: Besides data diversity and                                     In addition, there are very few studies for fusing LiDAR
the size of the training dataset, data quality significantly affects                          and camera outputs with signals from other sources such
the performance of a deep multi-modal perception system as                                    as Radars, ultrasonics or V2X communication. Radar data
well. Training data is usually labeled by human annotators to                                 differs from LiDAR data and it requires different network
ensure the high labeling quality. However, humans are also                                    architecture and fusion schmes. So far, we are not aware of
prone to making errors. Fig. 11 shows two different errors in                                 any work fusing Ultrasonic sensor signals in deep multi-modal
the labeling process when training an object detection network.                               perception, despite its relevance for low-speed scenarios. How
The network is much more robust against labeling errors when                                  to fuse these sensing modalities and align them temporally and
they are randomly distributed, compared to biased labeling                                    spatially are big challenges.
from the use of a deterministic pre-labeling. Training networks                                  Finally, it is an interesting topic to combine physical con-
with erroneous labels is further studied in [188]–[191]. The                                  straints and model-based approaches with data-driven neural
impact on weak or erroneous labels on the performance of                                      networks. For example, Ramos et al. [199] propose to fuse
deep learning based semantic segmentation is investigated                                     semantics and geometric cues in a Bayesian framework for
in [192], [193]. The influence of labelling errors on the                                     unexpected objects detections. The semantics are predicted by
accuracy of object detection is discussed in [194], [195].                                    a FCN network, whereas the geometric cues are provided by
   Well-calibrated sensors are the prerequisite for accurate and                              model-based stereo detections. The multi-task learning scheme
robust multi-modal perception systems. However, the sensor                                    also helps to add physical constraints in neural networks. For
setup is usually not perfect. Temporal and spatial sensing mis-                               example, to aid 3D object detection task, Liang et al. [116]
alignments might occur while recording the training data or de-                               design a fusion network that additionally estimate LiDAR
ploying the perception modules. This could cause severe errors                                ground plane and camera image depth. The ground plane
in training datasets and degrade the performance of networks,                                 estimation provides useful cues for object locations, while
especially for those which are designed to implicitly learn                                   the image depth completion contributes to better cross-modal
the sensor alignment (e.g. networks that fuse LiDAR BEV                                       representation; Panoptic segmentation [47] aims to achieve
feature maps and front view camera images cf. Sec. V-A3).                                     complete scene understanding by jointly doing semantic seg-
Interestingly, several works propose to calibrate sensors by                                  mentation and instance segmentation.
deep neural networks: Giering et al. [197] discretize the spatial                                2) How to Fuse: Explicitly modeling uncertainty or in-
misalignments between LiDAR and visual camera into nine                                       formativeness of each sensing modality is important safe
classes, and build a network to classify misalignment taking                                  autonomous driving. As an example, a multi-modal percep-
LiDAR and RGB images as inputs; Schneider et al. [198]                                        tion system should show higher uncertainty against adverse
propose to fully regress the extrinsic calibration parameters                                 weather or detect unseen driving environments (open-world
between LiDAR and visual camera by deep learning. Sev-                                        problem). It should also reflect sensor’s degradation or defects
eral multi-modal CNN networks are trained on different de-                                    as well. The perception uncertainties need to be propagated
calibration ranges to iteratively refine the calibration output. In                           to other modules such as motion planning [200] so that
this way, the feature extraction, feature matching, and global                                the autonomous vehicles can behave accordingly. Reliable
optimization problems for sensor registration could be solved                                 uncertainty estimation can show the networks’ robustness (cf.
                                                                                                                                              13

    LiDAR                                                                   in object detectors and semantic segmentation networks to
                                     Object located     Yes (Prob. = 90%)   other modules, such as tracking and motion planning. How
                                    Object classified
                                                          “Pedestrian”
                                                          (Prob. = 60%)     to employ these uncertainties to improve the robustness of an
                                     Camera signal         Uncertain
  Camera
                                     LiDAR signal            Certain        autonomous driving system is a challenging open question.
                   Fusion network           Detection outputs
                                                                               Another way that can increase the networks’ robustness
     Night drive
                                                                            is generative models. In general, generative models aim at
Fig. 12: The importance of explicitly modeling and propagat-                modeling the data distribution in an unsupervised way as
ing uncertainties in a multi-modal object detection network.                well as generating new samples with some variations. Varia-
Ideally, the network should produce reliable prediction prob-               tional Autoencoders (VAEs) [219] and Generative Adversarial
abilities (object classification and localization). It should e.g.          Networks (GANs) [220] are the two most popular deep
depict high uncertainty for camera signals during a night drive.            generative models. They have been widely applied to image
Such uncertainty information is useful for the decision making              analysis [221]–[223], and recently introduced to model Radar
modules, such as maneuver planning or emergency braking                     data [224] and road detection [225] for autonomous driving.
systems.                                                                    Generative models could be useful for multi-modal perception
                                                                            problems. For example, they might generate labeled simulated
                                                                            sensor data, when it is tedious and difficult to collect in the real
Fig 12). However, most reviewed papers only fuse multiple                   world; they could also serve to detect situations where sensors
sensing modalities by a simple operation (e.g. addition and                 are defect or an autonomous car is driving into a new scenario
average mean, cf. Sec. V-B). Those methods are designed to                  that differs from those seen during training. Designing specific
achieve high average precision (AP) without considering the                 fusion operations for deep generative models is an interesting
networks’ robustness. The recent work by Bijelic et al. [112]               open question.
uses dropout to increase the network robustness in foggy                       3) When to Fuse: As discussed in Sec. V-C, the choice of
images. Specifically, they add pixel-wise dropout masks in dif-             when to fuse the sensing modalities in the reviewed works
ferent fusion layers so that the network randomly drops LiDAR               is mainly based on intuition and empirical results. There
or camera channels during training. Despite promising results               is no conclusive evidence that one fusion scheme is better
for detections in foggy weather, their method cannot express                than the others. Ideally, the “optimal” fusion architecture
which sensing modality is more reliable given the distorted                 should be found automatically instead of by meticulous en-
sensor inputs. To the best of our knowledge, only the gating                gineering. Neural network structure search can potentially
network (cf. Sec. V-B) explicitly models the informativeness                solve the problem. It aims at finding the optimal number of
of each sensing modality.                                                   neurons and layers in a neural network. Many approaches
   One way to estimate uncertainty and to increase network                  have been proposed, including the bottom-up construction
robustness is Bayesian Neural Networks (BNNs). They assume                  approach [226], pruning [227], Bayesian optimization [228],
a prior distribution over the network weights and infer the pos-            genetic algorithms [229], and the recent reinforcement learning
terior distribution to extract the prediction probability [201].            approach [230]. Another way to optimize the network struc-
There are two types of uncertainties BNNs can model. Epis-                  ture is by regularization, such as l1 regularization [231] and
temic uncertainty illustrates the models’ uncertainty when                  stochastic regularization [232], [233].
describing the training dataset. It can be obtained by esti-                   Furthermore, visual analytics techniques could be employed
mating the weight posterior by variational inference [202],                 for network architecture design. Such visualization tools can
sampling [203]–[205], batch normalization [206], or noise                   help to understand and analyze how networks behave, to
injection [207]. It has been applied to semantic segmenta-                  diagnose the problems, and finally to improve the network
tion [208] and open-world object detection problems [209],                  architecture. Several methods have been proposed for under-
[210]. Aleatoric uncertainty represents observation noises in-              standing CNNs for image classification [234], [235]. So far,
herent in sensors. It can be estimated by the observation                   there has been no research on visual analytics for deep multi-
likelihood such as a Gaussian distribution or Laplacian dis-                modal learning problems.
tribution. Kendall et al. [211] study both uncertainties for                   4) Real-time Consideration: Deep multi-modal neural net-
semantic segmentation; Ilg et al. [212] propose to extract                  works should perceive driving environments in real-time.
uncertainties for optical flow; Feng et al. [213] examine                   Therefore, computational costs and memory requirements
the epistemic and aleatoric uncertainties in a LiDAR vehicle                should be considered when developing the fusion methodol-
detection network for autonomous driving. They show that                    ogy. At the “what to fuse” level, sensing modalities should
the uncertainties encode very different information. In the                 be represented in an efficient way. At the “how to fuse”
successive work, [214] employ aleatoric uncertainties in a 3D               level, finding fusion operations that are suitable for network
object detection network to significantly improve its detection             acceleration, such as pruning and quantization [236]–[239],
performance and increase its robustness against noisy data.                 is an interesting future work. At the “when to fuse” level,
Other works that introduce aleatoric uncertainties in object                inference time and memory constraints can be considered as
detectors include [215]–[218]. Although much progress has                   regularization term for network architecture optimization.
been made for BNNs, to the best of our knowledge, so far they                  It is difficult to compare the inference speed among the
have not been introduced to multi-modal perception. Further-                methods we have reviewed, as there is no benchmark with
more, few works have been done to propagate uncertainties                   standard hardware or programming languages. Tab. V and
                                                                                                                                               14

Tab. VI summarize the inference speed of several object de-         and “when to fuse”. We have also discussed challenges and
tection and semantic segmentation networks on the KITTI test        open questions. Furthermore, our interactive online tool allows
set. Each method uses different hardware, and the inference         readers to navigate topics and methods for each reference. We
time is reported only by the authors. It is an open question how    plan to frequently update this tool.
these methods perform when they are deployed on automotive             Despite the fact that an increasing number of multi-modal
hardware.                                                           datasets have been published, most of them record data from
                                                                    RGB cameras, thermal cameras, and LiDARs. Correspond-
C. Others                                                           ingly, most of the papers we reviewed fuse RGB images
                                                                    either with thermal images or with LiDAR point clouds. Only
   1) Evaluation Metrics: The common way to evaluate object
                                                                    recently has the fusion of Radar data been investigated. This
detection methods is mean average precision (mAP) [6], [240].
                                                                    includes nuScene dataset [89], the Oxford Radar RobotCar
It is the mean value of average precision (AP) over object
                                                                    Dataset [85], the Astyx HiRes2019 Dataset [94], and the
classes, given a certain intersection over union (IoU) threshold
                                                                    seminal work from Chadwick et al. [134] that proposes to fuse
defined as the geometric overlap between predictions and
                                                                    RGB camera images with Radar points for vehicle detection.
ground truths. As for the pixel-level semantic segmentation,
                                                                    In the future, we expect more datasets and fusion methods
metrics such as average precision, false positive rate, false
                                                                    concerning Radar signals.
negative rate, and IoU calculated at pixel level [57] are often
                                                                       There are various ways to fuse sensing modalities in neural
used. However, these metrics only summarize the prediction
                                                                    networks, encompassing different sensor representations, cf.
accuracy to a test dataset. They do not consider how sensor
                                                                    Sec. V-A, fusion operations cf. Sec. V-B, and fusion stages,
behaves in different situations. As an example, to evaluate the
                                                                    cf. Sec. V-C. However, we do not find conclusive evidence
performance of a multi-modal network, the IoU thresholds
                                                                    that one fusion method is better than the others. Additionally,
should depend on object distance, occlusion, and types of
                                                                    there is a lack of research on multi-modal perception in open-
sensors.
                                                                    set conditions or with sensor failures. We expect more focus
   Furthermore, common evaluation metrics are not designed
                                                                    on these challenging research topics.
specifically to illustrate how the algorithm handles open-set
conditions or in situations where some sensors are degraded or
defective. There exist several metrics to evaluate the quality of                           ACKNOWLEDGMENT
predictive uncertainty, e.g. empirical calibration curves [241]        We thank Fabian Duffhauss for collecting literature and
and log predictive probabilities. The detection error [242] mea-    reviewing the paper. We also thank Bill Beluch, Rainer Stal,
sures the effectiveness of a neural network in distinguishing       Peter Möller and Ulrich Michael for their suggestions and
in- and out-of-distribution data. The Probability-based Detec-      inspiring discussions.
tion Quality (PDQ) [243] is designed to measure the object
detection performance for spatial and semantic uncertainties.
These metrics can be adapted to the multi-modal perception                                       R EFERENCES
problems to compare the networks’ robustness.                        [1] E. D. Dickmanns and B. D. Mysliwetz, “Recursive 3-d road and relative
   2) More Network Architectures: Most reviewed methods                  ego-state recognition,” IEEE Trans. Pattern Anal. Mach. Intell., no. 2,
                                                                         pp. 199–213, 1992.
are based on CNN architectures for single frame perception.          [2] C. Urmson et al., “Autonomous driving in urban environments: Boss
The predictions in a frame are not dependent on previous                 and the urban challenge,” J. Field Robotics, vol. 25, no. 8, pp. 425–466,
frames, resulting in inconsistency over time. Only a few works           2008.
                                                                     [3] R.    Berger,     “Autonomous       driving,”     Think     Act,    2014.
incorporate temporal cues (e.g. [122], [244]). Future work is            [Online]. Available: http://www.rolandberger.ch/media/pdf/Roland
expected to develop multi-modal perception algorithms that               Berger TABAutonomousDrivingfinal20141211
can handle time series, e.g. via Recurrent Neural Networks.          [4] G. Neuhold, T. Ollmann, S. R. Bulò, and P. Kontschieder, “The
                                                                         Mapillary Vistas dataset for semantic understanding of street scenes,”
Furthermore, current methods are designed to propagate results           in Proc. IEEE Conf. Computer Vision, Oct. 2017, pp. 5000–5009.
to other modules in autonomous driving, such as localization,        [5] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,” Nature, vol.
planning, and reasoning. While the modular approach is the               521, no. 7553, p. 436, 2015.
                                                                     [6] A. Geiger, P. Lenz, and R. Urtasun, “Are we ready for autonomous
common pipeline for autonomous driving, some works also try              driving? the KITTI vision benchmark suite,” in Proc. IEEE Conf.
to map the sensor data directly to the decision policy such as           Computer Vision and Pattern Recognition, 2012.
steering angles or pedal positions (end-to-end learning) [245]–      [7] H. Yin and C. Berger, “When to use what data set for your self-driving
                                                                         car algorithm: An overview of publicly available driving datasets,” in
[247], or to some intermediate environment representations               IEEE 20th Int. Conf. Intelligent Transportation Systems, 2017, pp. 1–8.
(direct-perception) [248], [249]. Multi-modal end-to-end learn-      [8] D. Ramachandram and G. W. Taylor, “Deep multimodal learning: A
ing and direct perception can be potential research directions           survey on recent advances and trends,” IEEE Signal Process. Mag.,
                                                                         vol. 34, no. 6, pp. 96–108, 2017.
as well.                                                             [9] J. Janai, F. Güney, A. Behl, and A. Geiger, “Computer vision
                                                                         for autonomous vehicles: Problems, datasets and state-of-the-art,”
            VII. C ONCLUSION AND D ISCUSSION                             arXiv:1704.05519 [cs.CV], 2017.
                                                                    [10] E. Arnold, O. Y. Al-Jarrah, M. Dianati, S. Fallah, D. Oxtoby, and
   We have presented our survey for deep multi-modal object              A. Mouzakitis, “A survey on 3d object detection methods for au-
detection and segmentation applied to autonomous driving. We             tonomous driving applications,” IEEE Trans. Intell. Transp. Syst., pp.
                                                                         1–14, 2019.
have provided a summary of both multi-modal datasets and fu-        [11] L. Liu et al., “Deep learning for generic object detection: A survey,”
sion methodologies, considering “what to fuse”, “how to fuse”,           arXiv:1809.02165 [cs.CV], 2018.
                                                                                                                                                              15

[12] A. Garcia-Garcia, S. Orts-Escolano, S. Oprea, V. Villena-Martinez, and         [37] R. Girshick, “Fast R-CNN,” in Proc. IEEE Conf. Computer Vision,
     J. Garcia-Rodriguez, “A review on deep learning techniques applied to               2015, pp. 1440–1448.
     semantic segmentation,” Applied Soft Computing, 2017.                          [38] K. Simonyan and A. Zisserman, “Very deep convolutional networks
[13] K. Bengler, K. Dietmayer, B. Farber, M. Maurer, C. Stiller, and                     for large-scale image recognition,” arXiv:1409.1556 [cs.CV], 2014.
     H. Winner, “Three decades of driver assistance systems: Review and             [39] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for
     future perspectives,” IEEE Intell. Transp. Syst. Mag., vol. 6, no. 4, pp.           image recognition,” in Proc. IEEE Conf. Computer Vision and Pattern
     6–22, 2014.                                                                         Recognition, 2016, pp. 770–778.
[14] Waymo. (2017) Waymo safety report: On the road to fully self-driving.          [40] C. Szegedy et al., “Going deeper with convolutions,” in Proc. IEEE
     [Online]. Available: https://waymo.com/safety                                       Conf. Computer Vision and Pattern Recognition, 2015, pp. 1–9.
[15] M. Aeberhard et al., “Experience, results and lessons learned from             [41] S. Ren, K. He, R. Girshick, and J. Sun, “Faster R-CNN: Towards real-
     automated driving on Germany’s highways,” IEEE Intell. Transp. Syst.                time object detection with region proposal networks,” in Advances in
     Mag., vol. 7, no. 1, pp. 42–57, 2015.                                               Neural Information Processing Systems, 2015, pp. 91–99.
[16] J. Ziegler et al., “Making Bertha drive – an autonomous journey on a           [42] J. Dai, Y. Li, K. He, and J. Sun, “R-FCN: Object detection via region-
     historic route,” IEEE Intell. Transp. Syst. Mag., vol. 6, no. 2, pp. 8–20,          based fully convolutional networks,” in Advances in Neural Information
     2014.                                                                               Processing Systems, 2016, pp. 379–387.
[17] M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn,
                                                                                    [43] C. Szegedy, A. Toshev, and D. Erhan, “Deep neural networks for object
     and A. Zisserman, “The PASCAL Visual Object Classes
                                                                                         detection,” in Advances in Neural Information Processing Systems,
     Challenge       2007      (VOC2007)        Results,”     http://www.pascal-
                                                                                         2013, pp. 2553–2561.
     network.org/challenges/VOC/voc2007/workshop/index.html.
[18] T.-Y. Lin et al., “Microsoft COCO: Common objects in context,” in              [44] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, “You only
     Proc. Eur. Conf. Computer Vision. Springer, 2014, pp. 740–755.                      look once: Unified, real-time object detection,” in Proc. IEEE Conf.
[19] M. Weber, P. Wolf, and J. M. Zöllner, “DeepTLR: A single deep                      Computer Vision and Pattern Recognition, 2016, pp. 779–788.
     convolutional network for detection and classification of traffic lights,”     [45] W. Liu et al., “SSD: Single shot multibox detector,” in Proc. Eur. Conf.
     in IEEE Intelligent Vehicles Symp., 2016, pp. 342–348.                              Computer Vision. Springer, 2016, pp. 21–37.
[20] J. Müller and K. Dietmayer, “Detecting traffic lights by single shot          [46] J. Huang et al., “Speed/accuracy trade-offs for modern convolutional
     detection,” in 21st Int. Conf. Intelligent Transportation Systems. IEEE,            object detectors,” in Proc. IEEE Conf. Computer Vision and Pattern
     2016, pp. 342–348.                                                                  Recognition, vol. 4, 2017.
[21] M. Bach, S. Reuter, and K. Dietmayer, “Multi-camera traffic light              [47] A. Kirillov, K. He, R. Girshick, C. Rother, and P. Dollár, “Panoptic
     recognition using a classifying labeled multi-bernoulli filter,” in IEEE            segmentation,” in Proc. IEEE Conf. Computer Vision and Pattern
     Intelligent Vehicles Symp., 2017, pp. 1045–1051.                                    Recognition, 2018.
[22] K. Behrendt, L. Novak, and R. Botros, “A deep learning approach to             [48] A. Kirillov, R. Girshick, K. He, and P. Dollár, “Panoptic feature
     traffic lights: Detection, tracking, and classification,” in IEEE Int. Conf.        pyramid networks,” in Proc. IEEE Conf. Computer Vision and Pattern
     Robotics and Automation, 2017, pp. 1370–1377.                                       Recognition, 2019, pp. 6399–6408.
[23] Z. Zhu, D. Liang, S. Zhang, X. Huang, B. Li, and S. Hu, “Traffic-sign          [49] Y. Xiong et al., “Upsnet: A unified panoptic segmentation network,”
     detection and classification in the wild,” in Proc. IEEE Conf. Computer             in Proc. IEEE Conf. Computer Vision and Pattern Recognition, 2019,
     Vision and Pattern Recognition, 2016, pp. 2110–2118.                                pp. 8818–8826.
[24] H. S. Lee and K. Kim, “Simultaneous traffic sign detection and                 [50] L. Porzi, S. R. Bulo, A. Colovic, and P. Kontschieder, “Seamless
     boundary estimation using convolutional neural network,” IEEE Trans.                scene segmentation,” in Proc. IEEE Conf. Computer Vision and Pattern
     Intell. Transp. Syst., 2018.                                                        Recognition, 2019, pp. 8277–8286.
[25] H. Luo, Y. Yang, B. Tong, F. Wu, and B. Fan, “Traffic sign recognition         [51] B. Wu, A. Wan, X. Yue, and K. Keutzer, “SqueezeSeg: Convolutional
     using a multi-task convolutional neural network,” IEEE Trans. Intell.               neural nets with recurrent CRF for real-time road-object segmentation
     Transp. Syst., vol. 19, no. 4, pp. 1100–1111, 2018.                                 from 3d lidar point cloud,” in IEEE Int. Conf. Robotics and Automation,
[26] S. Zhang, R. Benenson, M. Omran, J. Hosang, and B. Schiele,                         May 2018, pp. 1887–1893.
     “Towards reaching human performance in pedestrian detection,” IEEE             [52] L. Caltagirone, S. Scheidegger, L. Svensson, and M. Wahde, “Fast
     Trans. Pattern Anal. Mach. Intell., vol. 40, no. 4, pp. 973–986, 2018.              lidar-based road detection using fully convolutional neural networks,”
[27] L. Zhang, L. Lin, X. Liang, and K. He, “Is Faster R-CNN doing well for              in IEEE Intelligent Vehicles Symp., 2017, pp. 1019–1024.
     pedestrian detection?” in Proc. Eur. Conf. Computer Vision. Springer,          [53] Q. Huang, W. Wang, and U. Neumann, “Recurrent slice networks for
     2016, pp. 443–457.                                                                  3d segmentation of point clouds,” in Proc. IEEE Conf. Computer Vision
[28] X. Chen, K. Kundu, Y. Zhu, H. Ma, S. Fidler, and R. Urtasun,                        and Pattern Recognition, 2018, pp. 2626–2635.
     “3d object proposals using stereo imagery for accurate object class            [54] A. Dewan, G. L. Oliveira, and W. Burgard, “Deep semantic classifica-
     detection,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 40, no. 5, pp.            tion for 3d lidar data,” in IEEE/RSJ Int. Conf. Intelligent Robots and
     1259–1272, 2018.                                                                    Systems, 2017, pp. 3544–3549.
[29] B. Li, “3d fully convolutional network for vehicle detection in point          [55] A. Dewan and W. Burgard, “DeepTemporalSeg: Temporally con-
     cloud,” in IEEE/RSJ Int. Conf. Intelligent Robots and Systems, 2017,                sistent semantic segmentation of 3d lidar scans,” arXiv preprint
     pp. 1513–1518.                                                                      arXiv:1906.06962, 2019.
[30] B. Li, T. Zhang, and T. Xia, “Vehicle detection from 3d lidar using
                                                                                    [56] A. Milioto, I. Vizzo, J. Behley, and C. Stachniss, “RangeNet++: Fast
     fully convolutional network,” in Proc. Robotics: Science and Systems,
                                                                                         and Accurate LiDAR Semantic Segmentation,” in IEEE/RSJ Int. Conf.
     Jun. 2016.
                                                                                         Intelligent Robots and Systems, 2019.
[31] X. Chen, K. Kundu, Z. Zhang, H. Ma, S. Fidler, and R. Urtasun,
     “Monocular 3d object detection for autonomous driving,” in Proc. IEEE          [57] M. Cordts et al., “The Cityscapes dataset for semantic urban scene
     Conf. Computer Vision and Pattern Recognition, 2016, pp. 2147–2156.                 understanding,” in Proc. IEEE Conf. Computer Vision and Pattern
[32] J. Fang, Y. Zhou, Y. Yu, and S. Du, “Fine-grained vehicle model recog-              Recognition, 2016, pp. 3213–3223.
     nition using a coarse-to-fine convolutional neural network architecture,”      [58] S. Wang et al., “TorontoCity: Seeing the world with a million eyes,”
     IEEE Trans. Intell. Transp. Syst., vol. 18, no. 7, pp. 1782–1792, 2017.             in Proc. IEEE Conf. Computer Vision, 2017, pp. 3028–3036.
[33] A. Mousavian, D. Anguelov, J. Flynn, and J. Košecká, “3d bounding            [59] G. Neuhold, T. Ollmann, S. Rota Bulò, and P. Kontschieder, “The
     box estimation using deep learning and geometry,” in Proc. IEEE Conf.               mapillary vistas dataset for semantic understanding of street scenes,”
     Computer Vision and Pattern Recognition, 2017, pp. 5632–5640.                       in Proc. IEEE Conf. Computer Vision, 2017. [Online]. Available:
[34] P. Sermanet, D. Eigen, X. Zhang, M. Mathieu, R. Fergus, and Y. LeCun,               https://www.mapillary.com/dataset/vistas
     “OverFeat: Integrated recognition, localization and detection using            [60] X. Huang et al., “The ApolloScape dataset for autonomous driving,” in
     convolutional networks,” in Int. Conf. Learning Representations, 2013.              Workshop Proc. IEEE Conf. Computer Vision and Pattern Recognition,
[35] R. Girshick, J. Donahue, T. Darrell, and J. Malik, “Rich feature                    2018, pp. 954–960.
     hierarchies for accurate object detection and semantic segmentation,”          [61] L. Schneider et al., “Multimodal neural networks: RGB-D for semantic
     in Proc. IEEE Conf. Computer Vision and Pattern Recognition, 2014,                  segmentation and object detection,” in Scandinavian Conf. Image
     pp. 580–587.                                                                        Analysis. Springer, 2017, pp. 98–109.
[36] K. He, X. Zhang, S. Ren, and J. Sun, “Spatial pyramid pooling in deep          [62] V. Badrinarayanan, A. Kendall, and R. Cipolla, “SegNet: A deep
     convolutional networks for visual recognition,” IEEE Trans. Pattern                 convolutional encoder-decoder architecture for image segmentation,”
     Anal. Mach. Intell., vol. 37, no. 9, pp. 1904–1916, 2015.                           IEEE Trans. Pattern Anal. Mach. Intell., no. 12, pp. 2481–2495, 2017.
                                                                                                                                                              16

[63] M. Teichmann, M. Weber, M. Zoellner, R. Cipolla, and R. Urtasun,              [89] H. Caesar et al., “nuScenes: A multimodal dataset for autonomous
     “MultiNet: Real-time joint semantic reasoning for autonomous driv-                 driving,” arXiv preprint arXiv:1903.11027, 2019.
     ing,” in IEEE Intelligent Vehicles Symp., 2018.                               [90] S. Hwang, J. Park, N. Kim, Y. Choi, and I. So Kweon, “Multispectral
[64] K. He, G. Gkioxari, P. Dollár, and R. Girshick, “Mask R-CNN,” in                  pedestrian detection: Benchmark dataset and baseline,” in Proc. IEEE
     Proc. IEEE Conf. Computer Vision, 2017, pp. 2980–2988.                             Conf. Computer Vision and Pattern Recognition, 2015, pp. 1037–1045.
[65] J. Uhrig, E. Rehder, B. Fröhlich, U. Franke, and T. Brox, “Box2Pix:          [91] K. Takumi, K. Watanabe, Q. Ha, A. Tejero-De-Pablos, Y. Ushiku, and
     Single-shot instance segmentation by assigning pixels to object boxes,”            T. Harada, “Multispectral object detection for autonomous vehicles,”
     in IEEE Intelligent Vehicles Symp., 2018.                                          in Proc. Thematic Workshops of ACM Multimedia, 2017, pp. 35–43.
[66] S. Gupta, R. Girshick, P. Arbeláez, and J. Malik, “Learning rich features    [92] Q. Ha, K. Watanabe, T. Karasawa, Y. Ushiku, and T. Harada, “MFNet:
     from RGB-D images for object detection and segmentation,” in Proc.                 Towards real-time semantic segmentation for autonomous vehicles with
     Eur. Conf. Computer Vision. Springer, 2014, pp. 345–360.                           multi-spectral scenes,” in IEEE/RSJ Int. Conf. Intelligent Robots and
[67] B. Hariharan, P. Arbeláez, R. Girshick, and J. Malik, “Simultaneous               Systems, 2017, pp. 5108–5115.
     detection and segmentation,” in Proc. Eur. Conf. Computer Vision.             [93] Y. Choi et al., “KAIST multi-spectral day/night data set for autonomous
     Springer, 2014, pp. 297–312.                                                       and assisted driving,” IEEE Trans. Intell. Transp. Syst., vol. 19, no. 3,
[68] J. Long, E. Shelhamer, and T. Darrell, “Fully convolutional networks               pp. 934–948, 2018.
     for semantic segmentation,” in Proc. IEEE Conf. Computer Vision and           [94] M. Meyer and G. Kuschk, “Automotive radar dataset for deep learning
     Pattern Recognition, 2015, pp. 3431–3440.                                          based 3d object detection,” in Proceedings of the 16th European Radar
[69] L.-C. Chen, G. Papandreou, I. Kokkinos, K. Murphy, and A. L. Yuille,               Conference, 2019.
     “DeepLab: Semantic image segmentation with deep convolutional nets,           [95] D. Kondermann et al., “Stereo ground truth with error bars,” in 12th
     atrous convolution, and fully connected CRFs,” IEEE Trans. Pattern                 Asian Conf. on Computer Vision. Springer, 2014, pp. 595–610.
     Anal. Mach. Intell., vol. 40, no. 4, pp. 834–848, 2018.                       [96] M. Larsson, E. Stenborg, L. Hammarstrand, T. Sattler, M. Pollefeys,
[70] A. Paszke, A. Chaurasia, S. Kim, and E. Culurciello, “ENet: A                      and F. Kahl, “A cross-season correspondence dataset for robust seman-
     deep neural network architecture for real-time semantic segmentation,”             tic segmentation,” in Proc. IEEE Conf. Computer Vision and Pattern
     arXiv:1606.02147 [cs.CV], 2016.                                                    Recognition, 2019.
[71] A. Roy and S. Todorovic, “A multi-scale CNN for affordance segmen-            [97] T. Sattler et al., “Benchmarking 6DOF outdoor visual localization in
     tation in RGB images,” in Proc. Eur. Conf. Computer Vision. Springer,              changing conditions,” in Proc. IEEE Conf. Computer Vision and Pattern
     2016, pp. 186–201.                                                                 Recognition, 2018, pp. 8601–8610.
[72] S. Zheng et al., “Conditional random fields as recurrent neural net-          [98] X. Chen, H. Ma, J. Wan, B. Li, and T. Xia, “Multi-view 3D object
     works,” in Proc. IEEE Conf. Computer Vision, 2015, pp. 1529–1537.                  detection network for autonomous driving,” in Proc. IEEE Conf.
[73] M. Siam, M. Gamal, M. Abdel-Razek, S. Yogamani, M. Jagersand, and                  Computer Vision and Pattern Recognition, 2017, pp. 6526–6534.
     H. Zhang, “A comparative study of real-time semantic segmentation for         [99] A. Asvadi, L. Garrote, C. Premebida, P. Peixoto, and U. J. Nunes,
     autonomous driving,” in Workshop Proc. IEEE Conf. Computer Vision                  “Multimodal vehicle detection: fusing 3d-lidar and color camera data,”
     and Pattern Recognition, 2018, pp. 587–597.                                        Pattern Recognition Lett., 2017.
[74] W. Maddern, G. Pascoe, C. Linegar, and P. Newman, “1 year, 1000              [100] S.-I. Oh and H.-B. Kang, “Object detection and classification by
     km: The Oxford RobotCar dataset,” Int. J. Robotics Research, vol. 36,              decision-level fusion for intelligent vehicle systems,” Sensors, vol. 17,
     no. 1, pp. 3–15, 2017.                                                             no. 1, p. 207, 2017.
[75] A. Geiger, P. Lenz, C. Stiller, and R. Urtasun, “Vision meets robotics:      [101] J. Schlosser, C. K. Chow, and Z. Kira, “Fusing lidar and images for
     The KITTI dataset,” Int. J. Robotics Research, 2013.                               pedestrian detection using convolutional neural networks,” in IEEE Int.
[76] J.-L. Blanco-Claraco, F.-Á. Moreno-Dueñas, and J. González-Jiménez,            Conf. Robotics and Automation, 2016, pp. 2198–2205.
     “The Málaga urban dataset: High-rate stereo and lidar in a realistic        [102] Z. Wang, W. Zhan, and M. Tomizuka, “Fusing bird view lidar point
     urban scenario,” Int. J. Robotics Research, vol. 33, no. 2, pp. 207–214,           cloud and front view camera image for deep object detection,” in IEEE
     2014.                                                                              Intelligent Vehicles Symp., 2018.
[77] H. Jung, Y. Oto, O. M. Mozos, Y. Iwashita, and R. Kurazume, “Multi-          [103] J. Ku, M. Mozifian, J. Lee, A. Harakeh, and S. Waslander, “Joint 3d
     modal panoramic 3d outdoor datasets for place categorization,” in                  proposal generation and object detection from view aggregation,” in
     IEEE/RSJ Int. Conf. Intelligent Robots and Systems, 2016, pp. 4545–                IEEE/RSJ Int. Conf. Intelligent Robots and Systems, Oct. 2018, pp.
     4550.                                                                              1–8.
[78] Y. Chen et al., “Lidar-video driving dataset: Learning driving policies      [104] D. Xu, D. Anguelov, and A. Jain, “PointFusion: Deep sensor fusion for
     effectively,” in Proc. IEEE Conf. Computer Vision and Pattern Recog-               3D bounding box estimation,” in Proc. IEEE Conf. Computer Vision
     nition, 2018, pp. 5870–5878.                                                       and Pattern Recognition, 2018.
[79] A. Patil, S. Malla, H. Gang, and Y.-T. Chen, “The H3D dataset for            [105] C. R. Qi, W. Liu, C. Wu, H. Su, and L. J. Guibas, “Frustum PointNets
     full-surround 3D multi-object detection and tracking in crowded urban              for 3d object detection from RGB-D data,” in Proc. IEEE Conf.
     scenes,” in IEEE Int. Conf. Robotics and Automation, 2019.                         Computer Vision and Pattern Recognition, 2018.
[80] X. Jianru et al., “BLVD: Building a large-scale 5D semantics bench-          [106] X. Du, M. H. Ang, and D. Rus, “Car detection for autonomous vehicle:
     mark for autonomous driving,” in IEEE Int. Conf. Robotics and                      Lidar and vision fusion approach through deep learning framework,”
     Automation, 2019.                                                                  in IEEE/RSJ Int. Conf. Intelligent Robots and Systems, 2017, pp. 749–
[81] R. Kesten et al. (2019) Lyft level 5 AV dataset 2019. [Online].                    754.
     Available: https://level5.lyft.com/dataset/                                  [107] X. Du, M. H. Ang Jr., S. Karaman, and D. Rus, “A general pipeline for
[82] M.-F. Chang et al., “Argoverse: 3D tracking and forecasting with rich              3d detection of vehicles,” in IEEE Int. Conf. Robotics and Automation,
     maps,” in Proc. IEEE Conf. Computer Vision and Pattern Recognition,                2018.
     June 2019.                                                                   [108] D. Matti, H. K. Ekenel, and J.-P. Thiran, “Combining lidar space
[83] (2019) PandaSet: Public large-scale dataset for autonomous driving.                clustering and convolutional neural networks for pedestrian detection,”
     [Online]. Available: https://scale.com/open-datasets/pandaset                      in 14th IEEE Int. Conf. Advanced Video and Signal Based Surveillance,
[84] (2019) Waymo open dataset: An autonomous driving dataset. [Online].                2017, pp. 1–6.
     Available: https://www.waymo.com/open                                        [109] T. Kim and J. Ghosh, “Robust detection of non-motorized road users
[85] D. Barnes, M. Gadd, P. Murcutt, P. Newman, and I. Posner, “The                     using deep learning on optical and lidar data,” in IEEE 19th Int. Conf.
     Oxford radar RobotCar dataset: A radar extension to the Oxford                     Intelligent Transportation Systems, 2016, pp. 271–276.
     RobotCar dataset,” arXiv preprint arXiv: 1909.01300, 2019. [Online].         [110] J. Kim, J. Koh, Y. Kim, J. Choi, Y. Hwang, and J. W. Choi, “Robust
     Available: https://arxiv.org/pdf/1909.01300                                        deep multi-modal learning based on gated information fusion network,”
[86] Q.-H. Pham et al., “A*3D Dataset: Towards autonomous driving in                    in Asian Conf. Computer Vision, 2018.
     challenging environments,” arXiv preprint arXiv: 1909.07541, 2019.           [111] A. Pfeuffer and K. Dietmayer, “Optimal sensor data fusion architecture
[87] J. Geyer et al. (2019) A2D2: AEV autonomous driving dataset.                       for object detection in adverse weather conditions,” in Proc. 21st Int.
     [Online]. Available: https://www.audi-electronics-venture.de/aev/web/              Conf. Information Fusion. IEEE, 2018, pp. 2592–2599.
     en/driving-dataset.html                                                      [112] M. Bijelic, F. Mannan, T. Gruber, W. Ritter, K. Dietmayer, and F. Heide,
[88] M. Braun, S. Krebs, F. B. Flohr, and D. M. Gavrila, “EuroCity Persons:             “Seeing through fog without seeing fog: Deep sensor fusion in the
     A novel benchmark for person detection in traffic scenes,” IEEE Trans.             absence of labeled training data,” in Proc. IEEE Conf. Computer Vision,
     Pattern Anal. Mach. Intell., pp. 1–1, 2019.                                        2019.
                                                                                                                                                           17

[113] V. A. Sindagi, Y. Zhou, and O. Tuzel, “MVX-Net: Multimodal voxelnet       [137] S. Shi, Z. Wang, X. Wang, and H. Li, “Part − A2 Net: 3d part-aware
      for 3D object detection,” in IEEE Int. Conf. Robotics and Automation,           and aggregation neural network for object detection from point cloud,”
      2019.                                                                           arXiv preprint arXiv:1907.03670, 2019.
[114] J. Dou, J. Xue, and J. Fang, “SEG-VoxelNet for 3D vehicle detection       [138] Y. Yan, Y. Mao, and B. Li, “Second: Sparsely embedded convolutional
      from rgb and lidar data,” in IEEE Int. Conf. Robotics and Automation.           detection,” Sensors, vol. 18, no. 10, p. 3337, 2018.
      IEEE, 2019, pp. 4362–4368.                                                [139] C. R. Qi, H. Su, K. Mo, and L. J. Guibas, “PointNet: Deep learning on
[115] Z. Wang and K. Jia, “Frustum convnet: Sliding frustums to aggregate             point sets for 3d classification and segmentation,” in Proc. IEEE Conf.
      local point-wise features for amodal 3D object detection,” in IEEE/RSJ          Computer Vision and Pattern Recognition, Jul. 2017, pp. 77–85.
      Int. Conf. Intelligent Robots and Systems. IEEE, 2019.                    [140] C. R. Qi, L. Yi, H. Su, and L. J. Guibas, “PointNet++: Deep hierarchical
[116] M. Liang, B. Yang, Y. Chen, R. Hu, and R. Urtasun, “Multi-task multi-           feature learning on point sets in a metric space,” in Advances in Neural
      sensor fusion for 3D object detection,” in Proc. IEEE Conf. Computer            Information Processing Systems, 2017, pp. 5099–5108.
      Vision and Pattern Recognition, 2019, pp. 7345–7353.                      [141] K. Shin, Y. P. Kwon, and M. Tomizuka, “RoarNet: A robust 3D
[117] J. Wagner, V. Fischer, M. Herman, and S. Behnke, “Multispectral                 object detection based on region approximation refinement,” in IEEE
      pedestrian detection using deep fusion convolutional neural networks,”          Intelligent Vehicles Symp., 2018.
      in 24th Eur. Symp. Artificial Neural Networks, Computational Intelli-     [142] S. Wang, S. Suo, M. Wei-Chiu, A. Pokrovsky, and R. Urtasun, “Deep
      gence and Machine Learning, 2016, pp. 509–514.                                  parametric continuous convolutional neural networks,” in Proc. IEEE
[118] S. W. Jingjing Liu, Shaoting Zhang and D. Metaxas, “Multispectral               Conf. Computer Vision and Pattern Recognition, 2018, pp. 2589–2597.
      deep neural networks for pedestrian detection,” in Proc. British Ma-
                                                                                [143] Y. Li, R. Bu, M. Sun, W. Wu, X. Di, and B. Chen, “PointCNN: Con-
      chine Vision Conf., Sep. 2016, pp. 73.1–73.13.
                                                                                      volution on χ -transformed points,” in Advances in Neural Information
[119] D. Guan, Y. Cao, J. Liang, Y. Cao, and M. Y. Yang, “Fusion of
                                                                                      Processing Systems, 2018, pp. 826–836.
      multispectral data through illumination-aware deep neural networks for
      pedestrian detection,” Information Fusion, vol. 50, pp. 148–157, 2019.    [144] A. Asvadi, L. Garrote, C. Premebida, P. Peixoto, and U. J. Nunes,
[120] O. Mees, A. Eitel, and W. Burgard, “Choosing smartly: Adaptive                  “DepthCN: Vehicle detection using 3d-lidar and ConvNet,” in IEEE
      multimodal fusion for object detection in changing environments,” in            20th Int. Conf. Intelligent Transportation Systems, 2017.
      IEEE/RSJ Int. Conf. Intelligent Robots and Systems, 2016, pp. 151–        [145] C. Premebida, L. Garrote, A. Asvadi, A. P. Ribeiro, and U. Nunes,
      156.                                                                            “High-resolution lidar-based depth mapping using bilateral filter,” in
[121] B. Yang, M. Liang, and R. Urtasun, “HDNET: Exploiting HD maps                   IEEE 19th Int. Conf. Intelligent Transportation Systems, Nov. 2016,
      for 3D object detection,” in Proc. 2nd Annu. Conf. Robot Learning,              pp. 2469–2474.
      2018, pp. 146–155.                                                        [146] A. H. Lang, S. Vora, H. Caesar, L. Zhou, J. Yang, and O. Beijbom,
[122] S. Casas, W. Luo, and R. Urtasun, “IntentNet: Learning to predict               “PointPillars: Fast encoders for object detection from point clouds,” in
      intention from raw sensor data,” in Proc. 2nd Annu. Conf. Robot                 Proc. IEEE Conf. Computer Vision and Pattern Recognition, 2018.
      Learning, 2018, pp. 947–956.                                              [147] T. Roddick, A. Kendall, and R. Cipolla, “Orthographic feature trans-
[123] D.-K. Kim, D. Maturana, M. Uenoyama, and S. Scherer, “Season-                   form for monocular 3d object detection,” in Proc. British Machine
      invariant semantic segmentation with a deep multimodal network,” in             Vision Conf., 2019.
      Field and Service Robotics. Springer, 2018, pp. 255–270.                  [148] Y. Wang, W.-L. Chao, D. Garg, B. Hariharan, M. Campbell, and
[124] Y. Sun, W. Zuo, and M. Liu, “RTFNet: Rgb-thermal fusion network                 K. Weinberger, “Pseudo-lidar from visual depth estimation: Bridging
      for semantic segmentation of urban scenes,” IEEE Robotics and Au-               the gap in 3d object detection for autonomous driving,” in Proc. IEEE
      tomation Letters, 2019.                                                         Conf. Computer Vision and Pattern Recognition, 2019.
[125] A. Valada, G. L. Oliveira, T. Brox, and W. Burgard, “Deep multi-          [149] Y. You et al., “Pseudo-lidar++: Accurate depth for 3d object detection
      spectral semantic scene understanding of forested environments using            in autonomous driving,” arXiv preprint arXiv:1906.06310, 2019.
      multimodal fusion,” in Int. Symp. Experimental Robotics. Springer,        [150] M. Liang, B. Yang, S. Wang, and R. Urtasun, “Deep continuous fusion
      2016, pp. 465–477.                                                              for multi-sensor 3d object detection,” in Proc. Eur. Conf. Computer
[126] A. Valada, J. Vertens, A. Dhall, and W. Burgard, “AdapNet: Adaptive             Vision, 2018, pp. 641–656.
      semantic segmentation in adverse environmental conditions,” in IEEE       [151] K. Werber et al., “Automotive radar gridmap representations,” in IEEE
      Int. Conf. Robotics and Automation, 2017, pp. 4644–4651.                        MTT-S Int. Conf. Microwaves for Intelligent Mobility, 2015, pp. 1–4.
[127] A. Valada, R. Mohan, and W. Burgard, “Self-supervised model adap-         [152] J. Lombacher, M. Hahn, J. Dickmann, and C. Wöhler, “Potential of
      tation for multimodal semantic segmentation,” Int. J. Computer Vision,          radar for static object classification using deep learning methods,” in
      2018.                                                                           IEEE MTT-S Int. Conf. Microwaves for Intelligent Mobility, 2016, pp.
[128] F. Yang, J. Yang, Z. Jin, and H. Wang, “A fusion model for road                 1–4.
      detection based on deep learning and fully connected CRF,” in 13th        [153] J. Lombacher, K. Laudt, M. Hahn, J. Dickmann, and C. Wöhler,
      Annu. Conf. System of Systems Engineering. IEEE, 2018, pp. 29–36.               “Semantic radar grids,” in IEEE Intelligent Vehicles Symp., 2017, pp.
[129] L. Caltagirone, M. Bellone, L. Svensson, and M. Wahde, “Lidar-camera            1170–1175.
      fusion for road detection using fully convolutional neural networks,”
                                                                                [154] T. Visentin, A. Sagainov, J. Hasch, and T. Zwick, “Classification of
      Robotics and Autonomous Systems, vol. 111, pp. 125–131, 2019.
                                                                                      objects in polarimetric radar images using cnns at 77 ghz,” in 2017
[130] X. Lv, Z. Liu, J. Xin, and N. Zheng, “A novel approach for detecting
                                                                                      IEEE Asia Pacific Microwave Conference (APMC). IEEE, 2017, pp.
      road based on two-stream fusion fully convolutional network,” in IEEE
                                                                                      356–359.
      Intelligent Vehicles Symp., 2018, pp. 1464–1469.
[131] F. Wulff, B. Schäufele, O. Sawade, D. Becker, B. Henke, and              [155] S. Kim, S. Lee, S. Doo, and B. Shim, “Moving target classification
      I. Radusch, “Early fusion of camera and lidar for robust road detection         in automotive radar systems using convolutional recurrent neural net-
      based on U-Net FCN,” in IEEE Intelligent Vehicles Symp., 2018, pp.              works,” in 26th Eur. Signal Processing Conf. IEEE, 2018, pp. 1482–
      1426–1431.                                                                      1486.
[132] Z. Chen, J. Zhang, and D. Tao, “Progressive lidar adaptation for road     [156] M. G. Amin and B. Erol, “Understanding deep neural networks per-
      detection,” IEEE/CAA Journal of Automatica Sinica, vol. 6, no. 3, pp.           formance for radar-based human motion recognition,” in IEEE Radar
      693–702, 2019.                                                                  Conf., 2018, pp. 1461–1465.
[133] F. Piewak et al., “Boosting lidar-based semantic labeling by cross-       [157] O. Schumann, M. Hahn, J. Dickmann, and C. Wöhler, “Semantic seg-
      modal training data generation,” in Workshop Proc. Eur. Conf. Com-              mentation on radar point clouds,” in Proc. 21st Int. Conf. Information
      puter Vision, 2018.                                                             Fusion. IEEE, 2018, pp. 2179–2186.
[134] S. Chadwick, W. Maddern, and P. Newman, “Distant vehicle detection        [158] C. Wöhler, O. Schumann, M. Hahn, and J. Dickmann, “Comparison
      using radar and vision,” in IEEE Int. Conf. Robotics and Automation,            of random forest and long short-term memory network performances
      2019.                                                                           in classification tasks using radar,” in Sensor Data Fusion: Trends,
[135] Y. Zhou and O. Tuzel, “VoxelNet: End-to-end learning for point cloud            Solutions, Applications. IEEE, 2017, pp. 1–6.
      based 3d object detection,” in Proc. IEEE Conf. Computer Vision and       [159] R. A. Jacobs, M. I. Jordan, S. J. Nowlan, and G. E. Hinton, “Adaptive
      Pattern Recognition, 2018.                                                      mixtures of local experts,” Neural Computation, vol. 3, pp. 79–87,
[136] M. Engelcke, D. Rao, D. Z. Wang, C. H. Tong, and I. Posner,                     1991.
      “Vote3Deep: Fast object detection in 3d point clouds using efficient      [160] D. Eigen, M. Ranzato, and I. Sutskever, “Learning factored represen-
      convolutional neural networks,” in IEEE Int. Conf. Robotics and                 tations in a deep mixture of experts,” in Workshop Proc. Int. Conf.
      Automation, 2017, pp. 1355–1361.                                                Learning Representations, 2014.
                                                                                                                                                              18

[161] M. Bloesch, J. Czarnowski, R. Clark, S. Leutenegger, and A. J.              [187] G. I. Parisi, R. Kemker, J. L. Part, C. Kanan, and S. Wermter,
      Davison, “Codeslam: learning a compact, optimisable representation                “Continual lifelong learning with neural networks: A review,” Neural
      for dense visual slam,” in Proc. IEEE Conf. Computer Vision and                   Networks, 2019.
      Pattern Recognition, 2018, pp. 2560–2568.                                   [188] Y. Wang et al., “Iterative learning with open-set noisy labels,” in Proc.
[162] J. Wang, Z. Wei, T. Zhang, and W. Zeng, “Deeply-fused nets,”                      IEEE Conf. Computer Vision and Pattern Recognition, 2018, pp. 8688–
      arXiv:1605.07716 [cs.CV], 2016.                                                   8696.
[163] O. Russakovsky et al., “ImageNet large scale visual recognition chal-       [189] M. Ren, W. Zeng, B. Yang, and R. Urtasun, “Learning to reweight
      lenge,” Int. J. Computer Vision, vol. 115, no. 3, pp. 211–252, 2015.              examples for robust deep learning,” in Int. Conf. Machine Learning,
[164] J. Ngiam et al., “Starnet: Targeted computation for object detection in           2018.
      point clouds,” arXiv preprint arXiv:1908.11069, 2019.                       [190] L. Jiang, Z. Zhou, T. Leung, L.-J. Li, and L. Fei-Fei, “MentorNet:
[165] A. Gaidon, Q. Wang, Y. Cabon, and E. Vig, “Virtual worlds as proxy for            Learning data-driven curriculum for very deep neural networks on
      multi-object tracking analysis,” in Proc. IEEE Conf. Computer Vision              corrupted labels,” in Int. Conf. Machine Learning, 2018, pp. 2309–
      and Pattern Recognition, 2016.                                                    2318.
[166] S. R. Richter, V. Vineet, S. Roth, and V. Koltun, “Playing for data:        [191] X. Ma et al., “Dimensionality-driven learning with noisy labels,” in
      Ground truth from computer games,” in Proc. Eur. Conf. Computer                   Int. Conf. Machine Learning, 2018, pp. 3361–3370.
      Vision, 2016, pp. 102–118.                                                  [192] A. Zlateski, R. Jaroensri, P. Sharma, and F. Durand, “On the importance
[167] G. Ros, L. Sellart, J. Materzynska, D. Vazquez, and A. M. Lopez, “The             of label quality for semantic segmentation,” in Proc. IEEE Conf.
      SYNTHIA dataset: A large collection of synthetic images for semantic              Computer Vision and Pattern Recognition, 2018, pp. 1479–1487.
      segmentation of urban scenes,” in Proc. IEEE Conf. Computer Vision
                                                                                  [193] P. Meletis and G. Dubbelman, “On boosting semantic street scene
      and Pattern Recognition, 2016, pp. 3234–3243.
                                                                                        segmentation with weak supervision,” in IEEE Intelligent Vehicles
[168] S. R. Richter, Z. Hayder, and V. Koltun, “Playing for benchmarks,” in
                                                                                        Symp., 2019.
      Proc. IEEE Conf. Computer Vision, Oct. 2017, pp. 2232–2241.
[169] X. Yue, B. Wu, S. A. Seshia, K. Keutzer, and A. L. Sangiovanni-             [194] C. Haase-Schütz, H. Hertlein, and W. Wiesbeck, “Estimating labeling
      Vincentelli, “A lidar point cloud generator: from a virtual world to              quality with deep object detectors,” in IEEE Intelligent Vehicles Symp.,
      autonomous driving,” in Proc. ACM Int. Conf. Multimedia Retrieval.                June 2019, pp. 33–38.
      ACM, 2018, pp. 458–464.                                                     [195] S. Chadwick and P. Newman, “Training object detectors with noisy
[170] M. Wrenninge and J. Unger, “Synscapes: A photorealistic synthetic                 data,” in IEEE Intelligent Vehicles Symp., June 2019, pp. 1319–1325.
      dataset for street scene parsing,” arXiv preprint arXiv:1810.08705,         [196] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár, “Focal loss for
      2018.                                                                             dense object detection,” IEEE Trans. Pattern Anal. Mach. Intell., 2018.
[171] P.-H. Huang, K. Matzen, J. Kopf, N. Ahuja, and J.-B. Huang, “Deep-          [197] M. Giering, V. Venugopalan, and K. Reddy, “Multi-modal sensor
      mvs: Learning multi-view stereopsis,” in Proc. IEEE Conf. Computer                registration for vehicle perception via deep neural networks,” in IEEE
      Vision and Pattern Recognition, 2018.                                             High Performance Extreme Computing Conf., 2015, pp. 1–6.
[172] D. Griffiths and J. Boehm, “SynthCity: A large scale synthetic point        [198] N. Schneider, F. Piewak, C. Stiller, and U. Franke, “RegNet: Mul-
      cloud,” in ArXiv preprint, 2019.                                                  timodal sensor registration using deep neural networks,” in IEEE
[173] A. Dosovitskiy, G. Ros, F. Codevilla, A. Lopez, and V. Koltun,                    Intelligent Vehicles Symp., 2017, pp. 1803–1810.
      “CARLA: An open urban driving simulator,” in Proc. 1st Annu. Conf.          [199] S. Ramos, S. Gehrig, P. Pinggera, U. Franke, and C. Rother, “Detecting
      Robot Learning, 2017, pp. 1–16.                                                   unexpected obstacles for self-driving cars: Fusing deep learning and
[174] B. Hurl, K. Czarnecki, and S. Waslander, “Precise synthetic image and             geometric modeling,” in IEEE Intelligent Vehicles Symp., 2017, pp.
      lidar (presil) dataset for autonomous vehicle perception,” arXiv preprint         1025–1032.
      arXiv:1905.00160, 2019.                                                     [200] H. Banzhaf, M. Dolgov, J. Stellet, and J. M. Zöllner, “From footprints
[175] J. Lee, S. Walsh, A. Harakeh, and S. L. Waslander, “Leveraging pre-               to beliefprints: Motion planning under uncertainty for maneuvering
      trained 3d object detection models for fast ground truth generation,” in          automated vehicles in dense scenarios,” in 21st Int. Conf. Intelligent
      21st Int. Conf. Intelligent Transportation Systems. IEEE, Nov. 2018,              Transportation Systems. IEEE, 2018, pp. 1680–1687.
      pp. 2504–2510.                                                              [201] D. J. C. MacKay, “A practical Bayesian framework for backpropagation
[176] J. Mei, B. Gao, D. Xu, W. Yao, X. Zhao, and H. Zhao, “Semantic                    networks,” Neural Computation, vol. 4, no. 3, pp. 448–472, 1992.
      segmentation of 3d lidar data in dynamic scene using semi-supervised        [202] G. E. Hinton and D. Van Camp, “Keeping the neural networks simple
      learning,” IEEE Trans. Intell. Transp. Syst., 2018.                               by minimizing the description length of the weights,” in Proc. 6th
[177] R. Mackowiak, P. Lenz, O. Ghori, F. Diego, O. Lange, and C. Rother,               Annu. Conf. Computational Learning Theory. ACM, 1993, pp. 5–13.
      “CEREALS – cost-effective region-based active learning for semantic         [203] Y. Gal, “Uncertainty in deep learning,” Ph.D. dissertation, University
      segmentation,” in Proc. British Machine Vision Conf., 2018.                       of Cambridge, 2016.
[178] S. Roy, A. Unmesh, and V. P. Namboodiri, “Deep active learning for          [204] A. Graves, “Practical variational inference for neural networks,” in
      object detection,” in Proc. British Machine Vision Conf., 2018, p. 91.            Advances in Neural Information Processing Systems, 2011, pp. 2348–
[179] D. Feng, X. Wei, L. Rosenbaum, A. Maki, and K. Dietmayer, “Deep                   2356.
      active learning for efficient training of a lidar 3d object detector,” in   [205] S. Mandt, M. D. Hoffman, and D. M. Blei, “Stochastic gradient descent
      IEEE Intelligent Vehicles Symp., 2019.                                            as approximate Bayesian inference,” J. Machine Learning Research,
[180] S. J. Pan, Q. Yang et al., “A survey on transfer learning,” IEEE Trans.           vol. 18, no. 1, pp. 4873–4907, 2017.
      Knowl. Data Eng., vol. 22, no. 10, pp. 1345–1359, 2010.
                                                                                  [206] M. Teye, H. Azizpour, and K. Smith, “Bayesian uncertainty estimation
[181] V. M. Patel, R. Gopalan, R. Li, and R. Chellappa, “Visual domain
                                                                                        for batch normalized deep networks,” in Int. Conf. Machine Learning,
      adaptation: A survey of recent advances,” IEEE Signal Process. Mag.,
                                                                                        2018.
      vol. 32, no. 3, pp. 53–69, 2015.
[182] Y. Chen, W. Li, X. Chen, and L. V. Gool, “Learning semantic                 [207] J. Postels, F. Ferroni, H. Coskun, N. Navab, and F. Tombari, “Sampling-
      segmentation from synthetic data: A geometrically guided input-output             free epistemic uncertainty estimation using approximated variance
      adaptation approach,” in Proc. IEEE Conf. Computer Vision and Pattern             propagation,” in Proc. IEEE Conf. Computer Vision, 2019.
      Recognition, 2019, pp. 1841–1850.                                           [208] A. Kendall, V. Badrinarayanan, and R. Cipolla, “Bayesian SegNet:
[183] Y. Chen, W. Li, C. Sakaridis, D. Dai, and L. Van Gool, “Domain                    Model uncertainty in deep convolutional encoder-decoder architectures
      adaptive faster r-cnn for object detection in the wild,” in Proc. IEEE            for scene understanding,” in Proc. British Machine Vision Conf., 2017.
      Conf. Computer Vision and Pattern Recognition, 2018, pp. 3339–3348.         [209] D. Miller, L. Nicholson, F. Dayoub, and N. Sünderhauf, “Dropout
[184] K.-H. Lee, G. Ros, J. Li, and A. Gaidon, “Spigan: Privileged adversarial          sampling for robust object detection in open-set conditions,” in IEEE
      learning from simulation,” in Proc. Int. Conf. Learning Representations,          Int. Conf. Robotics and Automation, 2018.
      2019.                                                                       [210] D. Miller, F. Dayoub, M. Milford, and N. Sünderhauf, “Evaluating
[185] J. Tremblay et al., “Training deep networks with synthetic data:                  merging strategies for sampling-based uncertainty techniques in object
      Bridging the reality gap by domain randomization,” in Workshop Proc.              detection,” in IEEE Int. Conf. Robotics and Automation, 2018.
      IEEE Conf. Computer Vision and Pattern Recognition, 2018, pp. 969–          [211] A. Kendall and Y. Gal, “What uncertainties do we need in Bayesian
      977.                                                                              deep learning for computer vision?” in Advances in Neural Information
[186] D. P. Kingma, S. Mohamed, D. J. Rezende, and M. Welling, “Semi-                   Processing Systems, 2017, pp. 5574–5584.
      supervised learning with deep generative models,” in Advances in            [212] E. Ilg et al., “Uncertainty estimates and multi-hypotheses networks for
      Neural Information Processing Systems, 2014, pp. 3581–3589.                       optical flow,” in Proc. Eur. Conf. Computer Vision, 2018.
                                                                                                                                                              19

[213] D. Feng, L. Rosenbaum, and K. Dietmayer, “Towards safe autonomous            [238] Y. Cheng, D. Wang, P. Zhou, and T. Zhang, “A survey of model
      driving: Capture uncertainty in the deep neural network for lidar 3d               compression and acceleration for deep neural networks,” IEEE Signal
      vehicle detection,” in 21st Int. Conf. Intelligent Transportation Systems,         Process. Mag., 2017.
      Nov. 2018, pp. 3266–3273.                                                    [239] L. Enderich, F. Timm, L. Rosenbaum, and W. Burgard, “Learning
[214] D. Feng, L. Rosenbaum, F. Timm, and K. Dietmayer, “Leveraging                      multimodal fixed-point weights using gradient descent,” in 27th Eur.
      heteroscedastic aleatoric uncertainties for robust real-time lidar 3d              Symp. Artificial Neural Networks, Computational Intelligence and
      object detection,” in IEEE Intelligent Vehicles Symp., 2019.                       Machine Learning, 2019.
[215] G. P. Meyer, A. Laddha, E. Kee, C. Vallespi-Gonzalez, and C. K.              [240] M. Everingham, L. Van Gool, C. K. Williams, J. Winn, and A. Zis-
      Wellington, “Lasernet: An efficient probabilistic 3d object detector for           serman, “The PASCAL visual object classes (VOC) challenge,” Int. J.
      autonomous driving,” in Proc. IEEE Conf. Computer Vision and Pattern               Computer Vision, vol. 88, no. 2, pp. 303–338, 2010.
      Recognition, 2019, pp. 12 677–12 686.                                        [241] A. P. Dawid, “The well-calibrated Bayesian,” J. American Statistical
[216] S. Wirges, M. Reith-Braun, M. Lauer, and C. Stiller, “Capturing object             Association, vol. 77, no. 379, pp. 605–610, 1982.
      detection uncertainty in multi-layer grid maps,” in IEEE Intelligent         [242] S. Liang, Y. Li, and R. Srikant, “Enhancing the reliability of out-of-
      Vehicles Symp., 2019.                                                              distribution image detection in neural networks,” in Int. Conf. Learning
[217] M. T. Le, F. Diehl, T. Brunner, and A. Knol, “Uncertainty estimation               Representations, 2017.
      for deep neural object detectors in safety-critical applications,” in IEEE   [243] D. Hall, F. Dayoub, J. Skinner, P. Corke, G. Carneiro, and
      21st Int. Conf. Intelligent Transportation Systems. IEEE, 2018, pp.                N. Sünderhauf, “Probability-based detection quality (PDQ): A prob-
      3873–3878.                                                                         abilistic approach to detection evaluation,” arXiv:1811.10800 [cs.CV],
[218] D. Feng, L. Rosenbaum, C. Gläser, F. Timm, and K. Dietmayer, “Can                 2018.
      we trust you? on calibration of a probabilistic object detector for          [244] W. Luo, B. Yang, and R. Urtasun, “Fast and furious: Real time end-
      autonomous driving,” arXiv:1909.12358 [cs.RO], 2019.                               to-end 3d detection, tracking and motion forecasting with a single
                                                                                         convolutional net,” in Proc. IEEE Conf. Computer Vision and Pattern
[219] D. P. Kingma and M. Welling, “Auto-encoding variational Bayes,” in
                                                                                         Recognition, 2018, pp. 3569–3577.
      Int. Conf. Learning Representations, 2014.
                                                                                   [245] M. Bojarski et al., “End to end learning for self-driving cars,”
[220] I. Goodfellow et al., “Generative adversarial nets,” in Advances in                arXiv:1604.07316 [cs.CV], 2016.
      Neural Information Processing Systems, 2014, pp. 2672–2680.                  [246] G.-H. Liu, A. Siravuru, S. Prabhakar, M. Veloso, and G. Kantor,
[221] A. B. L. Larsen, S. K. Sønderby, H. Larochelle, and O. Winther,                    “Learning end-to-end multimodal sensor policies for autonomous nav-
      “Autoencoding beyond pixels using a learned similarity metric,” in Int.            igation,” in Proc. 1st Annu. Conf. Robot Learning, 2017, pp. 249–261.
      Conf. Machine Learning, 2016, pp. 1558–1566.                                 [247] M. Bansal, A. Krizhevsky, and A. Ogale, “Chauffeurnet: Learning
[222] A. Deshpande, J. Lu, M.-C. Yeh, M. J. Chong, and D. A. Forsyth,                    to drive by imitating the best and synthesizing the worst,” in Proc.
      “Learning diverse image colorization,” in Proc. IEEE Conf. Computer                Robotics: Science and Systems, 2019.
      Vision and Pattern Recognition, 2016, pp. 2877–2885.                         [248] A. Sauer, N. Savinov, and A. Geiger, “Conditional affordance learning
[223] P. Isola, J.-Y. Zhu, T. Zhou, and A. A. Efros, “Image-to-image                     for driving in urban environments,” in Proc. 2st Annu. Conf. Robot
      translation with conditional adversarial networks,” in Proc. IEEE Conf.            Learning, 2018, pp. 237–252.
      Computer Vision and Pattern Recognition, 2017, pp. 5967–5976.                [249] C. Chen, A. Seff, A. Kornhauser, and J. Xiao, “DeepDriving: Learning
[224] T. A. Wheeler, M. Holder, H. Winner, and M. J. Kochenderfer, “Deep                 affordance for direct perception in autonomous driving,” in Proc. IEEE
      stochastic radar models,” in IEEE Intelligent Vehicles Symp., 2017, pp.            Conf. Computer Vision, 2015, pp. 2722–2730.
      47–53.                                                                       [250] B. Yang, W. Luo, and R. Urtasun, “PIXOR: Real-time 3d object
[225] X. Han, J. Lu, C. Zhao, S. You, and H. Li, “Semi-supervised and                    detection from point clouds,” in Proc. IEEE Conf. Computer Vision
      weakly-supervised road detection based on generative adversarial net-              and Pattern Recognition, 2018, pp. 7652–7660.
      works,” IEEE Signal Process. Lett., 2018.                                    [251] Ö. Erkent, C. Wolf, C. Laugier, D. S. González, and V. R. Cano,
[226] J. L. Elman, “Learning and development in neural networks: The                     “Semantic grid estimation with a hybrid bayesian and deep neural
      importance of starting small,” Cognition, vol. 48, no. 1, pp. 71–99,               network approach,” in 2018 IEEE/RSJ International Conference on
      1993.                                                                              Intelligent Robots and Systems (IROS). IEEE, 2018, pp. 888–895.
[227] J. Feng and T. Darrell, “Learning the structure of deep convolutional        [252] S. Gu, T. Lu, Y. Zhang, J. Alvarez, J. Yang, and H. Kong, “3D lidar+
      networks,” in Proc. IEEE Conf. Computer Vision, 2015, pp. 2749–2757.               monocular camera: an inverse-depth induced fusion framework for
[228] D. Ramachandram, M. Lisicki, T. J. Shields, M. R. Amer, and G. W.                  urban road detection,” IEEE Transactions on Intelligent Vehicles, 2018.
      Taylor, “Structure optimization for deep multimodal fusion networks          [253] Y. Cai, D. Li, X. Zhou, and X. Mou, “Robust drivable road region de-
      using graph-induced kernels,” in 25th Eur. Symp. Artificial Neural                 tection for fixed-route autonomous vehicles using map-fusion images,”
      Networks, Computational Intelligence and Machine Learning, 2017.                   Sensors, vol. 18, no. 12, p. 4158, 2018.
[229] D. Whitley, T. Starkweather, and C. Bogart, “Genetic algorithms and
      neural networks: Optimizing connections and connectivity,” Parallel
      computing, vol. 14, no. 3, pp. 347–361, 1990.
[230] B. Zoph and Q. V. Le, “Neural architecture search with reinforcement
      learning,” arXiv:1611.01578 [cs.LG], 2016.
[231] P. Kulkarni, J. Zepeda, F. Jurie, P. Pérez, and L. Chevallier, “Learning
      the structure of deep architectures using l1 regularization,” in Proc.
      British Machine Vision Conf., 2015.
[232] C. Murdock, Z. Li, H. Zhou, and T. Duerig, “Blockout: Dynamic
                                                                                                             Di Feng (Member, IEEE) is currently pursuing
      model selection for hierarchical deep networks,” in Proc. IEEE Conf.
                                                                                                             his doctoral degree in the Corporate Research of
      Computer Vision and Pattern Recognition, 2016, pp. 2583–2591.
                                                                                                             Robert Bosch GmbH, Renningen, in cooperation
[233] F. Li, N. Neverova, C. Wolf, and G. Taylor, “Modout: Learning multi-                                   with the Ulm University. He finished his master’s
      modal architectures by stochastic regularization,” in 12th IEEE Int.                                   degree with distinction in electrical and computer
      Conf. Automatic Face & Gesture Recognition, 2017, pp. 422–429.                                         engineering at the Technical University of Munich.
[234] A. Bilal, A. Jourabloo, M. Ye, X. Liu, and L. Ren, “Do convolutional                                   During his studies, he was granted the opportunity
      neural networks learn class hierarchy?” IEEE Trans. Vis. Comput.                                       to work in several teams with reputable companies
      Graphics, vol. 24, no. 1, pp. 152–162, 2018.                                                           and research institutes such as BMW AG, German
[235] M. Liu, J. Shi, Z. Li, C. Li, J. Zhu, and S. Liu, “Towards better analysis                             Aerospace Center (DLR), and Institute for Cognitive
      of deep convolutional neural networks,” IEEE Trans. Vis. Comput.                                       Systems (ICS) at Technical University of Munich.
      Graphics, vol. 23, no. 1, pp. 91–100, 2017.                                  He received the bachelor’s degree in mechatronics with honor from Tongji
[236] S. Han, H. Mao, and W. J. Dally, “Deep compression: Compressing              University. His current research is centered on robust multi-modal object
      deep neural networks with pruning, trained quantization and huffman          detection using deep learning approach for autonomous driving. He is also
      coding,” in Int. Conf. Learning Representations, 2015.                       interested in robotic active learning and exploration through tactile sensing
[237] A. G. Howard et al., “MobileNets: Efficient convolutional neural             and cognitive systems.
      networks for mobile vision applications,” arXiv:1704.04861 [cs.CV],
      2017.
                                                                                                                                                                20

                           Christian Haase-Schütz (Member, IEEE) is cur-                                    Fabian Timm studied Computer Science at the
                           rently pursuing his PhD degree at Chassis Systems                                 University of Lübeck, Germany. In 2006 he did
                           Control, Robert Bosch GmbH, Abstatt, in coop-                                     his diploma thesis at Philips Lighting Systems in
                           eration with the Karlsruhe Institute of Technol-                                  Aachen, Germany. Afterwards he started his PhD
                           ogy. Before joining Bosch, he finished his mas-                                   also at Philips Lighting Systems in the field of
                           ter’s degree in physics at the Friedrich-Alexander-                               Machine Vision and Machine Learning and finished
                           University Erlangen-Nuremberg. He did his thesis                                  it in 2011 at the University of Lübeck, Institute
                           with the Center for Medical Physics. During his                                   for Neuro- and Bioinformatics. In 2012 he joined
                           master studies he was granted a scholarship by                                    corporate research at Robert Bosch GmbH and
                           the Bavarian state to visit Huazhong University of                                worked on industrial image processing and machine
                           Science and Technology, Wuhan, China, from March                                  learning. Afterwards he worked in the business unit
2015 till July 2015. He received his bachelor’s degree in physics from the          at Bosch and developed new perception algorithms, such as pedestrian and
University of Stuttgart in 2013, where he did his thesis with the Max Planck        cyclist protection only with a single radar sensor. Since 2018 he leads the
Institute for Intelligent Systems. His professional experience includes work        research group ”automated driving perception and sensors” at Bosch corporate
with ETAS GmbH, Stuttgart, and Andreas Stihl AG, Waiblingen. His current            research. His main research interests are machine and deep learning, signal
research is centered on multi-modal object detection using deep learning            processing, and sensors for automated driving.
approaches for autonomous driving. He is further interested in challenges
of AI systems in the wild. Christian Haase-Schütz is a member of the IEEE
and the German Physical Society DPG.

                                                                                                             Werner Wiesbeck (Fellow, IEEE) received the
                                                                                                             Dipl.-Ing. (M.S.) and the Dr. -Ing. (Ph.D.) degrees in
                      Lars Rosenbaum received his Dipl.-Inf. (M.S.) and
                                                                                                             electrical engineering from the Technical University
                      the Dr. rer. nat. (Ph.D.) degrees in bioinformatics
                                                                                                             Munich, Germany, in 1969 and 1972, respectively.
                      from the University of Tuebingen, Germany, in
                                                                                                             From 1972 to 1983, he was with product responsibil-
                      2009 and 2013, respectively. During this time he
                                                                                                             ity for mm-wave radars, receivers, direction finders,
                      was working on machine learning approaches for
                                                                                                             and electronic warfare systems in industry. From
                      computer-aided molecular drug design and analysis
                                                                                                             1983 to 2007, he was the Director of the Institut für
                      of metabolomics data. In 2014, he joined ITK En-
                                                                                                             Höchstfrequenztechnik und Elektronik, University of
                      gineering in Marburg, Germany, working on driver
                                                                                                             Karlsruhe. He is currently a Distinguished Senior
                      assistance systems. Since 2016, he is a research en-
                                                                                                             Fellow at the Karlsruhe Institute of Technology. His
                      gineer at Corporate Research, Robert Bosch GmbH
                                                                                    research topics include antennas, wave propagation, radar, remote sensing,
                      in Renningen, Germany, where he is currently doing
                                                                                    wireless communication, and ultra wide band technologies.
research on machine learning algorithms in the area of perception for
                                                                                    He has authored and co-authored several books and over 850 publications,
automated driving.
                                                                                    is a supervisor of over 90 Ph.D. students, a responsible supervisor of over
                                                                                    600 Diploma-/Master theses, and holds over 60 patents. He is an Honorary
                                                                                    Life Member of IEEE GRS-S and a member of the Heidelberger Academy
                                                                                    of Sciences and Humanities, and the German Academy of Engineering and
                          Heinz Hertlein (Member, IEEE) received the                Technology. He was a recipient of a number of awards, including the IEEE
                          Dipl.-Inf. degree (diploma in computer science)           Millennium Award, the IEEE GRS Distinguished Achievement Award, the
                          from the Friedrich-Alexander-University Erlangen-         Honorary Doctorate (Dr. h. c.) from the University Budapest/Hungary, the
                          Nuremberg, Germany, in 1999, and the Dr.-Ing.             Honorary Doctorate (Dr.-Ing. E. h.) from the University Duisburg/Germany,
                          (Ph.D.) degree from the same university in 2010 for       the Honorary Doctorate (Dr. -Ing. E. h.) from Technische Universität Ilmenau,
                          his research in the field of biometric speaker recogni-   and the IEEE Electromagnetics Award in 2008. He is the Chairman of the
                          tion. From 2002, he was working on algorithms and         GRS-S Awards Committee. He was the Executive Vice President of IEEE
                          applications of multi modal biometric pattern recog-      GRS-S (1998-1999) and the President of IEEE GRS-S (2000-2001). He has
                          nition at the company BioID in Erlangen-Tennenlohe        been a general chairman of several conferences.
                          and Nuremberg. From 2012, he was appointed at the
                          University of Hertfordshire in the UK, initially as a
Postdoctoral Research Fellow and later as a Senior Lecturer. He was teaching
in the fields of signal processing and pattern recognition, and his research
activities were mainly focused on biometric speaker and face recognition.
Since 2015, he is employed at Chassis Systems Control, Robert Bosch GmbH
in Abstatt, Germany, where he is currently working in the area of perception                                  Klaus Dietmayer (Member, IEEE) was born in
for autonomous driving.                                                                                       Celle, Germany in 1962. He received his Diploma
                                                                                                              degree in 1989 in Electrical Engineering from the
                                                                                                              Technical University of Braunschweig (Germany),
                                                                                                              and the Dr.-Ing. degree (equivalent to PhD) in 1994
                                                                                                              from the University of Armed Forces in Hamburg
                         Claudius Gläser was born in Gera, Germany in                                        (Germany). In 1994 he joined the Philips Semicon-
                         1982. He received his Diploma degree in Computer                                     ductors Systems Laboratory in Hamburg, Germany
                         Science from the Technical University of Ilmenau,                                    as a research engineer. Since 1996 he became a
                         Germany, in 2006, and the Dr.-Ing. degree (equiv-                                    manager in the field of networks and sensors for au-
                         alent to PhD) from Bielefeld University, Germany,                                    tomotive applications. In 2000 he was appointed to a
                         in 2012. From 2006 he was a Research Scientist             professorship at the University of Ulm in the field of measurement and control.
                         at the Honda Research Institute Europe GmbH in             Currently he is Full Professor and Director of the Institute of Measurement,
                         Offenbach/Main, Germany, working in the fields of          Control and Microtechnology in the school of Engineering and Computer
                         speech processing and language understanding for           Science at the University of Ulm. Research interests include information
                         humanoid robots. In 2011 he joined the Corporate           fusion, multi-object tracking, environment perception, situation understanding
                         Research of Robert Bosch GmbH in Renningen,                and trajectory planning for autonomous driving. Klaus Dietmayer is member
Germany, where he developed perception algorithms for driver assistance             of the IEEE and the German society of engineers VDI / VDE.
and highly automated driving functions. Currently, he is Team Lead for
perception for automated driving and manages various related projects. His
research interests include environment perception, multimodal sensor data
fusion, multi-object tracking, and machine learning for highly automated
driving.
                                                                   TABLE II: OVERVIEW OF MULTI-MODAL DATASETS
Name                         Sensing Modalities       Year (pub-   Labelled                Recording area      Size                            Categories / Remarks                  Link
                                                      lished)      (benchmark)
Astyx HiRes2019 [94]         Radar, Visual camera,    2019         3D bounding boxes       n.a.                500 frames (5000 annotated      Car, Bus, Cyclist, Motorcyclist,      https://www.astyx.com/development/
                             3D LiDAR                                                                          objects)                        Person, Trailer, Truck                astyx-hires2019-dataset.html
A2D2 [87]                    Visual cameras (6); 3D   2019         2D/3D bounding          Gaimersheim,        40k frames (semantics), 12k     Car, Bicycle, Pedestrian, Truck,      https://www.audi-electronics-venture.de/
                             LiDAR (5); Bus data                   boxes, 2D/3D instance   Ingolstadt,         frames (3D objects), 390k       Small vehicles, Traffic signal,       aev/web/en/driving-dataset.html
                                                                   segmentation            Munich              frames unlabeled                Utility vehicle, Sidebars, Speed
                                                                                                                                               bumper, Curbstone, Solid line,
                                                                                                                                               Irrelevant signs, Road blocks,
                                                                                                                                               Tractor, Non-drivable street, Zebra
                                                                                                                                               crossing, Obstacles / trash, Poles,
                                                                                                                                               RD restricted area, Animals, Grid
                                                                                                                                               structure, Signal corpus, Drivable
                                                                                                                                               cobbleston, Electronic traffic,
                                                                                                                                               Slow drive area, Nature object,
                                                                                                                                               Parking area, Sidewalk, Ego car,
                                                                                                                                               Painted driv. instr., Traffic guide
                                                                                                                                               obj., Dashed line, RD normal
                                                                                                                                               street, Sky, Buildings, Blurred
                                                                                                                                               area, Rain dirt
A*3D Dataset [86]            Visual cameras (2); 3D   2019         3D bounding boxes       Singapore           39k frames, 230k objects        Car, Van, Bus, Truck, Pedestrians,    https://github.com/I2RDL2/ASTAR-3D
                             LiDAR                                                                                                             Cyclists, and Motorcyclists;
                                                                                                                                               Afternoon and night, wet and dry
EuroCity Persons [88]        Visual camera;           2019         2D bounding boxes       12 countries in     47k frames, 258k objects        Pedestrian, Rider, Bicycle,           https://eurocity-dataset.tudelft.nl/eval/
                             Announced: stereo,                                            Europe, 27 cities                                   Motorbike, Scooter, Tricycle,         overview/home
                             LiDAR, GNSS and                                                                                                   Wheelchair, Buggy, Co-Rider;
                             intertial sensors                                                                                                 Highly diverse: 4 seasons, day and
                                                                                                                                               night, wet and dry
Oxford RobotCar [74], [85]   2016: Visual cameras     2016, 2019   no                      Oxford              2016: 11, 070, 651 frames       Long-term autonomous driving.         http://robotcar-dataset.robots.ox.ac.uk/
                             (fisheye & stereo), 2D                                                            (stereo), 3, 226, 183 frames    Various weather conditions,           downloads/, http://ori.ox.ac.uk/datasets/
                             & 3D LiDAR, GNSS,                                                                 (3D LiDAR); 2019: 240k          including heavy rain, night, direct   radar-robotcar-dataset
                             and inertial sensors;                                                             scans (Radar), 2.4M frames      sunlight and snow.
                             2019: Radar, 3D Lidar                                                             (LiDAR)
                             (2), 2D LiDAR (2),
                             visual cameras (6),
                             GNSS and inertial
                             sensors
Waymo Open Dataset [84]      3D LiDAR (5), Visual     2019         3D bounding box,        n.a.                200k frames, 12M objects        Vehicles, Pedestrians, Cyclists,      https://waymo.com/open/
                             cameras (5)                           Tracking                                    (3D LiDAR), 1.2M objects        Signs
                                                                                                               (2D camera)
Lyft Level 5 AV Dataset      3D LiDAR (5), Visual     2019         3D bounding box         n.a.                55k frames                      Semantic HD map included              https://level5.lyft.com/dataset/
2019 [81]                    cameras (6)
Argoverse [82]               3D LiDAR (2), Visual     2019         3D bounding box,        Pittsburgh,         113 scenes, 300k trajectories   Vehicle, Pedestrian, Other Static,    https://www.argoverse.org/data.html
                             cameras (9, 2 stereo)                 Tracking, Forecasting   Pennsylvania,                                       Large Vehicle, Bicycle, Bicyclist,
                                                                                           Miami, Florida                                      Bus, Other Mover, Trailer,
                                                                                                                                               Motorcyclist, Moped, Motorcycle,
                                                                                                                                               Stroller, Emergency Vehicle,
                                                                                                                                               Animal, Wheelchair, School Bus;
                                                                                                                                               Semantic HD maps (2) included
PandaSet [83]                3D LiDAR (2), Visual     2019         3D bounding box         San Francisco,      Announced: 60k frames           28 classes, 37 semantic               https://scale.com/open-datasets/pandaset
                             cameras (6), GNSS                                             El Camino Real      (camera), 20k frames            segmentation labels; Solid state
                             and inertial sensors                                                              (LiDAR), 125 scenes             LiDAR

                                                                                                                                                                                                                                 21
                                                                    TABLE II: OVERVIEW OF MULTI-MODAL DATASETS
Name                          Sensing Modalities       Year (pub-   Labelled                  Recording area      Size                            Categories / Remarks                   Link
                                                       lished)      (benchmark)
nuScenes dataset [89]         Visual cameras (6), 3D   2019         3D bounding box           Boston,             1000 scenes, 1.4M frames        25 Object classes, such as Car /       https://www.nuscenes.org/download
                              LiDAR, and Radars                                               Singapore           (camera, Radar), 390k           Van / SUV, different Trucks,
                              (5)                                                                                 frames (3D LiDAR)               Buses, Persons, Animal, Traffic
                                                                                                                                                  Cone, Temporary Traffic Barrier,
                                                                                                                                                  Debris, etc.
BLVD [80]                     Visual (Stereo)          2019         3D bounding box,          Changshu            120k frames,                    Vehicle, Pedestrian, Rider during      https://github.com/VCCIV/BLVD/
                              camera, 3D LiDAR                      Tracking, Interaction,                        249, 129 objects                day and night
                                                                    Intention
H3D dataset [79]              Visual cameras (3), 3D   2019         3D bounding box           San Francisco,      27, 721 frames,                 Car, Pedestrian, Cyclist, Truck,       https:
                              LiDAR                                                           Mountain View,      1, 071, 302 objects             Misc, Animals, Motorcyclist, Bus       //usa.honda-ri.com/hdd/introduction/h3d
                                                                                              Santa Cruz, San
                                                                                              Mateo
ApolloScape [60]              Visual (Stereo)          2018, 2019   2D/3D pixel-level         Multiple areas in   143, 906 image frames,          Rover, Sky, Car, Motobicycle,          http://apolloscape.auto/scene.html
                              camera, 3D LiDAR,                     segmentation, lane        China               89, 430 objects                 Bicycle, Person, Rider, Truck,
                              GNSS, and inertial                    marking, instance                                                             Bus, Tricycle, Road, Sidewalk,
                              sensors                               segmentation, depth                                                           Traffic Cone, Road Pile, Fence,
                                                                                                                                                  Traffic Light, Pole, Traffic Sign,
                                                                                                                                                  Wall, Dustbin, Billboard,
                                                                                                                                                  Building, Bridge, Tunnel,
                                                                                                                                                  Overpass, Vegetation
DBNet Dataset [78]            3D LiDAR, Dashboard      2018         Driving behaviours        Multiple areas in   Over 10k frames                 In total seven datasets with           http://www.dbehavior.net/
                              visual camera, GNSS                   (Vehicle speed and        China                                               different test scenarios, such as
                                                                    wheel angles)                                                                 seaside roads, school areas,
                                                                                                                                                  mountain roads.
KAIST multispectral dataset   Visual (Stereo) and      2018         2D bounding box,          Seoul               7, 512 frames,                  Person, Cyclist, Car during day        http://multispectral.kaist.ac.kr
[93]                          thermal camera, 3D                    drivable region, image                        308, 913 objects                and night, fine time slots (sunrise,
                              LiDAR, GNSS, and                      enhancement, depth,                                                           afternoon,...)
                              inertial sensors                      and colorization
Multi-spectral Object         Visual and thermal       2017         2D bounding box           University          7, 512 frames, 5, 833 objects   Bike, Car, Car Stop, Color Cone,       https://www.mi.t.u-tokyo.ac.jp/static/
Detection dataset [91]        cameras                                                         environment in                                      Person during day and night            projects/mil multispectral/
                                                                                              Japan
Multi-spectral Semantic       Visual and thermal       2017         2D pixel-level            n.a.                1569 frames                     Bike, Car, Person, Curve,              https://www.mi.t.u-tokyo.ac.jp/static/
Segmentation dataset [92]     camera                                segmentation                                                                  Guardrail, Color Cone, Bump            projects/mil multispectral/
                                                                                                                                                  during day and night
Multi-modal Panoramic 3D      Visual camera,           2016         Place categorization      Fukuoka             650 scans (dense),              No dynamic objects                     http:
Outdoor (MPO) dataset [77]    LiDAR, and GNSS                                                                     34200 scans (sparse)                                                   //robotics.ait.kyushu-u.ac.jp/∼kurazume/
                                                                                                                                                                                         research-e.php?content=db#d08
KAIST multispectral           Visual and thermal       2015         2D bounding box           Seoul               95, 328 frames,                 Person, People, Cyclist during day     https://sites.google.com/site/
pedestrian [90]               camera                                                                              103, 128 objects                and night                              pedestrianbenchmark/home
KITTI [6], [75]               Visual (Stereo)          2012,        2D/3D bounding box,       Karlsruhe           7481 frames (training)          Car, Van, Truck, Pedestrian,           http://www.cvlibs.net/datasets/kitti/
                              camera, 3D LiDAR,        2013, 2015   visual odometry, road,                        80.256 objects                  Person (sitting), Cyclist, Tram,
                              GNSS, and inertial                    optical flow, tracking,                                                       Misc
                              sensors                               depth, 2D instance and
                                                                    pixel-level
                                                                    segmentation
The Málaga Stereo and        Visual (Stereo)          2014         no                        Málaga             113, 082 frames, 5, 654.6 s     n.a.                                   https:
Laser Urban dataset [76]      camera, 5× 2D                                                                       (camera); > 220, 000 frames,                                           //www.mrpt.org/MalagaUrbanDataset
                              LiDAR (yielding 3D                                                                  5, 000 s (LiDARs)
                              information), GNSS
                              and inertial sensors

                                                                                                                                                                                                                                    22
                                                  TABLE III: SUMMARY OF MULTI-MODAL OBJECT DECTECTION METHODS
Reference      Sensors          Obj Type              Sensing Modality Representations      Network    How to generate Region    When to      Fusion Operation and          Fusion     Dataset(s) used
                                                      and Processing                        Pipeline   Proposals (RP) a          fuse         Method                        Levelb
Liang et       LiDAR, visual    3D Car, Pedestrian,   LiDAR BEV maps, RGB image.            Faster     Predictions with fused    Before RP    Addition, continuous fusion   Middle     KITTI, self-recorded
al., 2019      camera           Cyclist               Each processed by a ResNet with       R-CNN      features                               layer
[116]                                                 auxiliary tasks: depth estimation
                                                      and ground segmentation
Wang et al.,   LiDAR, visual    3D Car, Pedestrian,   LiDAR voxelized frustum (each         R-CNN      Pre-trained RGB image     After RP     Using RP from RGB image       Late       KITTI, SUN-RGBD
2019 [115]     camera           Cyclist, Indoor       frustum processed by the PointNet),              detector                               detector to build LiDAR
                                objects               RGB image (using a pre-trained                                                          frustums
                                                      detector).
Dou et al.,    LiDAR, visual    3D Car                LiDAR voxel (processed by             Two        Predictions with fused    Before RP    Feature concatenation         Middle     KITTI
2019 [114]     camera                                 VoxelNet), RGB image (processed       stage      features
                                                      by a FCN to get semantic features)    detector
Sindagi et     LiDAR, visual    3D Car                LiDAR voxel (processed by             One        Predictions with fused    Before RP    Feature concatenation         Early,     KITTI
al., 2019      camera                                 VoxelNet), RGB image (processed       stage      features                                                             Middle
[113]                                                 by a pre-trained 2D image             detector
                                                      detector).
Bijelic et     LiDAR, visual    2D Car in foggy       Lidar front view images (depth,       SSD        Predictions with fused    Before RP    Feature concatenation         From       Self-recorded datasets
al., 2019      camera           weather               intensity, height), RGB image. Each              features                                                             early to   focused on foggy weather,
[112]                                                 processed by VGG16                                                                                                    middle     simulated foggy images
                                                                                                                                                                            layers     from KITTI
Chadwick       Radar, visual    2D Vehicle            Radar range and velocity maps,        One        Predictions with fused    Before RP    Addition, feature             Middle     Self-recorded
et al., 2019   camera                                 RGB image. Each processed by          stage      features                               concatenation
[134]                                                 ResNet                                detector
Liang et       LiDAR, visual    3D Car, Pedestrian,   LiDAR BEV maps, RGB image.            One        Predictions with fused    Before RP    Addition, continuous fusion   Middle     KITTI, self-recorded
al., 2018      camera           Cyclist               Each processed by ResNet              stage      features                               layer
[150]                                                                                       detector
Du et al.,     LiDAR, visual    3D Car                LiDAR voxel (processed by             R-CNN      Pre-trained RGB image     Before and   Ensemble: use RGB image       Late       KITTI, self-recorded data
2018 [107]     camera                                 RANSAC and model fitting), RGB                   detector produces 2D      at RP        detector to regress car
                                                      image (processed by VGG16 and                    bounding boxes to crop                 dimensions for a model
                                                      GoogLeNet)                                       LiDAR points, which are                fitting algorithm
                                                                                                       then clustered
Kim et al,     LiDAR, visual    2D Car                LiDAR front-view depth image,         SSD        SSD with fused features   Before RP    Feature concatenation,        Middle     KITTI
2018 [110]     camera                                 RGB image Each input processed                                                          Mixture of Experts
                                                      by VGG16
Yang et al.,   LiDAR, HD-map    3D Car                LiDAR BEV maps, Road mask             One        Detector predictions      Before RP    Feature concatenation         Early      KITTI, TOR4D
2018 [121]                                            image from HD map. Inputs             stage                                                                                      Dataset [250]
                                                      processed by PIXOR++ [250] with       detector
                                                      the backbone similar to FPN
Pfeuffer et    LiDAR, visual    Multiple 2D objects   LiDAR spherical, and front-view       Faster     RPN from fused features   Before RP    Feature concatenation         Early,     KITTI
al., 2018      camera                                 sparse depth, dense depth image,      R-CNN                                                                           Mid-
[111]                                                 RGB image. Each processed by                                                                                          dle,
                                                      VGG16                                                                                                                 Late
Casas et       LiDAR, HD-map    3D Car                sequential LiDAR BEV maps,            One        Detector predictions      Before RP    Feature concatenation         Middle     self-recorded data
al., 2018                                             sequential several road topology      stage
[122]c                                                mask images from HD map. Each         detector
                                                      input processed by a base network
                                                      with residual blocks
Guan et al.,   visual camera,   2D Pedestrian         RGB image, thermal image. Each        Faster     RPN with fused features   Before and   Feature concatenation,        Early,     KAIST Pedestrian Dataset
2018 [119]     thermal camera                         processed by a base network built     R-CNN                                after RP     Mixture of Experts            Middle,
                                                      on VGG16                                                                                                              Late

                                                                                                                                                                                                                   23
                                                  TABLE III: SUMMARY OF MULTI-MODAL OBJECT DECTECTION METHODS
Reference       Sensors          Obj Type              Sensing Modality Representations    Network    How to generate Region        When to      Fusion Operation and         Fusion    Dataset(s) used
                                                       and Processing                      Pipeline   Proposals (RP) a              fuse         Method                       Levelb
Shin et al.,    LiDAR, visual    3D Car                LiDAR point clouds, (processed by   R-CNN      A 3D object detector for      After RP     Using RP from RGB image      Late      KITTI
2018 [141]      camera                                 PointNet [139]); RGB image                     RGB image                                  detector to search LiDAR
                                                       (processed by a 2D CNN)                                                                   point clouds
Schneider       Visual camera    Multiple 2D objects   RGB image (processed by             SSD        SSD predictions               Before RP    Feature concatenation        Early,    Cityscape
et al., 2017                                           GoogLeNet), depth image from                                                                                           Mid-
[61]                                                   stereo camera (processed by NiN                                                                                        dle,
                                                       net)                                                                                                                   Late
Takumi et       Visual camera,   Multiple 2D objects   RGB image, NIR, FIR, FIR image.     YOLO       YOLO predictions for each     After RP     Ensemble: ensemble final     Late      self-recorded data
al., 2017       thermal camera                         Each processed by YOLO                         spectral image                             predictions for each YOLO
[91]                                                                                                                                             detector
Chen et al.,    LiDAR, visual    3D Car                LiDAR BEV and spherical maps,       Faster     A RPN from LiDAR BEV          After RP     average mean, deep fusion    Early,    KITTI
2017 [98]       camera                                 RGB image. Each processed by a      R-CNN      map                                                                     Mid-
                                                       base network built on VGG16                                                                                            dle,
                                                                                                                                                                              Late
Asvadi et       LiDAR, visual    2D Car                LiDAR front-view dense-depth        YOLO       YOLO outputs for LiDAR        After RP     Ensemble: feed engineered    Late      KITTI
al., 2017       camera                                 (DM) and reflectance maps (RM),                DM and RM maps, and                        features from ensembled
[99]                                                   RGB image. Each processed                      RGB image                                  bounding boxes to a
                                                       through a YOLO net                                                                        network to predict scores
                                                                                                                                                 for NMS
Oh et al.,      LiDAR, visual    2D Car, Pedestrian,   LiDAR front-view dense-depth map    R-CNN      LiDAR voxel and RGB           After RP     Association matrix using     Late      KITTI
2017 [100]      camera           Cyclist               (for fusion: processed by VGG16),              image separately                           basic belief assignment
                                                       LiDAR voxel (for ROIs:
                                                       segmentation and region growing),
                                                       RGB image (for fusion: processed
                                                       by VGG16; for ROIs: segmentation
                                                       and grouping)
Wang et al.,    LiDAR, visual    3D Car, Pedestrian    LiDAR BEV map, RGB image.           One        Fused LiDAR and RGB           Before RP    Sparse mean manipulation     Middle    KITTI
2017 [102]      camera                                 Each processed by a                 stage      image features extracted
                                                       RetinaNet [196]                     detector   from CNN
Ku et al.,      LiDAR, visual    3D Car, Pedestrian,   LiDAR BEV map, RGB image.           Faster     Fused LiDAR and RGB           Before and   Average mean                 Early,    KITTI
2017 [103]      camera           Cyclist               Each processed by VGG16             R-CNN      image features extracted      after RP                                  Middle,
                                                                                                      from CNN                                                                Late
Xu et al.,      LiDAR, visual    3D Car, Pedestrian,   LiDAR points (processed by          R-CNN      Pre-trained RGB image         After RP     Feature concatenation for    Middle    KITTI, SUN-RGBD
2017 [104]      camera           Cyclist, Indoor       PointNet), RGB image (processed                detector                                   local and global features
                                 objects               by ResNet)
Qi et al.,      LiDAR, visual    3D Car, Pedestrian,   LiDAR points (processed by          R-CNN      Pre-trained RGB image         After RP     Feature concatenation        Middle,   KITTI, SUN-RGBD
2017 [105]      camera           Cyclist, Indoor       PointNet), RGB image (using a                  detector                                                                Late
                                 objects               pre-trained detector)
Du et al.,      LiDAR, visual    2D Car                LiDAR voxel (processed by           Faster     First clustered by LiDAR      Before RP    Ensemble: feed LiDAR RP      Late      KITTI
2017 [106]      camera                                 RANSAC and model fitting), RGB      R-CNN      point clouds, then                         to RGB image-based CNN
                                                       image (processed by VGG16 and                  fine-tuned by a RPN of                     for final prediction
                                                       GoogLeNet)                                     RGB image
Matti et al.,   LiDAR, visual    2D Pedestrian         LiDAR points (clustering with       R-CNN      Clustered by LiDAR point      Before and   Ensemble: feed LiDAR RP      Late      KITTI
2017 [108]      camera                                 DBSCAN) and RGB image                          clouds, then size and ratio   at RP        to RGB image-based CNN
                                                       (processed by ResNet)                          corrected on RGB image.                    for final prediction
Kim et al.,     LiDAR, visual    2D Pedestrian,        LiDAR front-view depth image,       Fast       Selective search for LiDAR    At RP        Ensemble: joint RP are fed   Late      KITTI
2016 [109]      camera           Cyclist               RGB image. Each processed by        R-CNN      and RGB image separately.                  to RGB image based CNN.
                                                       Fast R-CNN network [37]
Mees et al.,    RGB-D camera     2D Pedestrian         RGB image, depth image from         Fast       Dense multi-scale sliding     After RP     Mixture of Experts           Late      RGB-D People Unihall
2016 [120]                                             depth camera, optical flow. Each    R-CNN      window for RGB image                                                              Dataset, InOutDoor RGB-D
                                                       processed by GoogLeNet                                                                                                           People Dataset.

                                                                                                                                                                                                                   24
                                                           TABLE III: SUMMARY OF MULTI-MODAL OBJECT DECTECTION METHODS
Reference       Sensors                  Obj Type                 Sensing Modality Representations         Network     How to generate Region           When to      Fusion Operation and         Fusion    Dataset(s) used
                                                                  and Processing                           Pipeline    Proposals (RP) a                 fuse         Method                       Levelb
Wagner et       visual camera,           2D Pedestrian            RGB image, thermal image. Each           R-CNN       ACF+T+THOG detector              After RP     Feature concatenation        Early,    KAIST Pedestrian Dataset
al., 2016       thermal camera                                    processed by CaffeeNet                                                                                                          Late
[117]
Liu et al.,     Visual camera,           2D Pedestrian            RGB image, thermal image. Each           Faster      RPN with fused (or               Before and   Feature concatenation,       Early,    KAIST Pedestrian Dataset
2016 [118]      thermal camera                                    processed by NiN network                 R-CNN       separate) features               after RP     average mean, Score fusion   Mid-
                                                                                                                                                                     (Cascaded CNN)               dle,
                                                                                                                                                                                                  Late
Schlosser et    LiDAR, visual            2D Pedestrian            LiDAR HHA image, RGB image.              R-CNN       Deformable Parts Model           After RP     Feature concatenation        Early,    KITTI
al., 2016       camera                                            Each processed by a small ConvNet                    with RGB image                                                             Middle,
[101]                                                                                                                                                                                             Late

a
  For one-stage detector, we refer region proposals to be the detection outputs of a network.
b
  Some methods compare multiple fusion levels. We mark the fusion level with the best reported performance in bold.

                                                                                                                                                                                                                                       25
c
  Besides object detection, this paper also proposes intention prediction and trajectory prediction up to 3s in the unified network (multi-task prediction).
                                                     TABLE IV: SUMMARY OF MULTI-MODAL SEMANTIC SEGMENTATION METHODS
Reference                Sensors                      Semantics                   Sensing Modality Representations                     Fusion Operation and Method                    Fusion Level a        Dataset(s) used
Chen et al., 2019        LiDAR, visual camera         Road segmentation           RGB image, altitude difference image. Each           Feature adaptation module, modified            Middle                KITTI
[132]                                                                             processed by a CNN                                   concatenation.
Valada et al., 2019      Visual camera, depth         Multiple 2D objects         RGB image, thermal image, depth image. Each          Extension of Mixture of Experts                Middle                Six datasets,
[127]                    camera, thermal camera                                   processed by FCN with ResNet backbone                                                                                     including
                                                                                  (Adapnet++ architecture)                                                                                                  Cityscape, Sun
                                                                                                                                                                                                            RGB-D, etc.
Sun et al., 2019         Visual camera, thermal       Multiple 2D objects in      RGB image, thermal image. Each processed by a        Element-wise summation in the encoder          Middle                Datasets published
[124]                    camera                       campus environments         base network built on ResNet                         networks                                                             by [92]
Caltagirone et al.,      LiDAR, visual camera         Road segmentation           LiDAR front-view depth image, RGB image. Each        Feature concatenation (For early and late      Early, Middle, Late   KITTI
2019 [129]                                                                        input processed by a FCN                             fusion), weighted addition similar to gating
                                                                                                                                       network (for middle-level cross fusion)
Erkent et al., 2018      LiDAR, visual camera         Multiple 2D objects         LiDAR BEV occupancy grids (processed based on        Feature concatenation                          Middle                KITTI,
[251]                                                                             Bayesian filtering and tracking), RGB image                                                                               self-recorded
                                                                                  (processed by a FCN with VGG16 backbone)
Lv et al., 2018          LiDAR, visual camera         Road segmentation           LiDAR BEV maps, RGB image. Each input                Feature concatenation                          Middle                KITTI
[130]                                                                             processed by a FCN with dilated convolution
                                                                                  operator. RGB image features are also projected
                                                                                  onto LiDAR BEV plane before fusion
Wulff et al., 2018       LiDAR, visual camera         Road segmentation.          LiDAR BEV maps, RGB image projected onto             Feature concatenation                          Early                 KITTI
[131]                                                 Alternatives: freespace,    BEV plane. Inputs processed by a FCN with UNet
                                                      ego-lane detection
Kim et al., 2018         LiDAR, visual camera         2D Off-road terrains        LiDAR voxel (processed by 3D convolution), RGB       Addition                                       Early, Middle, Late   self-recorded data
[123]                                                                             image (processed by ENet)
Guan et al., 2018        Visual camera, thermal       2D Pedestrian               RGB image, thermal image. Each processed by a        Feature concatenation, Mixture of Experts      Early, Middle, Late   KAIST Pedestrian
[119]b                   camera                                                   base network built on VGG16                                                                                               Dataset
Yang et al., 2018        LiDAR, visual camera         Road segmentation           LiDAR points (processed by PointNet++), RGB          Optimizing Conditional Random Field            Late                  KITTI
[128]                                                                             image (processed by FCN with VGG16 backbone)         (CRF)
Gu et al., 2018          LiDAR, visual camera         Road segmentation           LiDAR front-view depth and height maps               Optimizing Conditional Random Field            Late                  KITTI
[252]                                                                             (processed by a inverse-depth histogram based line
                                                                                  scanning strategy), RGB image (processed by a
                                                                                  FCN).
Cai et al., 2018         Satellite map with route     Road segmentation           Route map image, RGB image. Images are fused         Overlaying the line and curve segments in      Early                 self-recorded data
[253]                    information, visual                                      and processed by a FCN                               the route map onto the RGB image to
                         camera                                                                                                        generate the Map Fusion Image (MFI)
Ha et al., 2017          Visual camera, thermal       Multiple 2D objects in      RGB image, thermal image. Each processed by a        Feature concatenation, addition (“short-cut    Middle                self-recorded data
[92]                     camera                       campus environments         FCN and mini-inception block                         fusion”)
Valada et al., 2017      Visual camera, thermal       Multiple 2D objects         RGB image, thermal image, depth image. Each          Mixture of Experts                             Late                  Cityscape, Freiburg
[126]                    camera                                                   processed by FCN with ResNet backbone                                                                                     Multispectral
                                                                                                                                                                                                            Dataset, Synthia
Schneider et al.,        Visual camera                Multiple 2D Objects         RGB image, depth image                               Feature concatenation                          Early, Middle, Late   Cityscape
2017 [61]
Schneider et al.,        Visual camera                Multiple 2D Objects         RGB image (processed by GoogLeNet), depth            Feature concatenation                          Early, Middle, Late   Cityscape
2017 [61]2                                                                        image from stereo camera (processed by NiN net)
Valada et al., 2016      Visual camera, thermal       Multiple 2D objects in      RGB image, thermal image, depth image. Each          Feature concatenation, addition                Early, Late           self-recorded data
[125]                    camera                       forested environments       processed by the UpNet (built on VGG16 and
                                                                                  up-convolution)

                                                                                                                                                                                                                                  26
a
    Some methods compare multiple fusion levels. We mark the fusion level with the best reported performance in bold.
b
    They also test the methods for object detection problem with different network architectures (see Table III).
                         TABLE V: PERFORMANCE AND RUNTIME FOR 3D OBJECT DETECTION ON KITTI TEST SET
       Reference                           Car                                 Pedestrian                                Cyclist                Runtime             Environment
                             Moderate     Easy         Hard        Moderate     Easy          Hard         Moderate      Easy        Hard

Liang et al., 2019 [116]     76.75 %      86.81 %      68.41 %     45.61 %        52.37 %     41.49 %      64.68 %       79.58 %     57.03 %    0.08 s     GPU @ 2.5 Ghz (Python)
Wang et al., 2019 [115]      76.51 %      85.88 %      68.08 %     -              -           -            -             -           -          0.47 s     GPU @ 2.5 Ghz (Python + C/C++)
Sindagi et al., 2019 [113]   72.7 %       83.2 %       65.12 %     -              -           -            -             -           -          -          -
Shin et al., 2018 [141]      73.04 %      83.71 %      59.16 %     -              -           -            -             -           -          -          GPU Titan X (not Pascal)
Du et al., 2018 [107]        73.80 %      84.33 %      64.83 %     -              -           -            -             -           -          0.5 s      GPU @ 2.5 Ghz (Matlab + C/C++)
Liang et al., 2018 [150]     66.22 %      82.54 %      64.04 %     -              -           -            -             -           -          0.06 s     GPU @ 2.5 Ghz (Python)
Ku et al., 2017 [103]        71.88 %      81.94 %      66.38 %     42.81 %        50.80 %     40.88 %      52.18 %       64.00 %     46.61 %    0.1 s      GPU Titan X (Pascal)
Qi et al., 2017 [105]        70.39 %      81.20 %      62.19 %     44.89 %        51.21 %     40.23 %      56.77 %       71.96 %     50.39 %    0.17 s     GPU @ 3.0 Ghz (Python)
Chen et al., 2017 [98]       62.35 %      71.09 %      55.12 %     -              -           -            -             -           -          0.36 s     GPU @ 2.5 Ghz (Python + C/C++)

                 TABLE VI: PERFORMANCE AND RUNTIME FOR ROAD SEGMENTATION (URBAN) ON KITTI TEST SET
                               Method                            MaxF        AP         PRE          REC        FPR         FNR       Runtime     Environment

                               Chen et al., 2019 [132]           97.03 %     94.03 %    97.19 %      96.88 %    1.54 %      3.12 %    0.16 s      GPU
                               Caltagirone et al., 2019 [129]    96.03 %     93.93 %    96.23 %      95.83 %    2.07 %      4.17 %    0.15 s      GPU
                               Gu et al., 2018 [252]             95.22 %     89.31 %    94.69 %      95.76 %    2.96 %      4.24 %    0.07 s      CPU
                               Lv et al., 2018 [130]             94.48 %     93.65 %    94.28 %      94.69 %    3.17 %      5.31 %    -           GPU Titan X
                               Yang et al., 2018 [128]           91.40 %     84.22 %    89.09 %      93.84 %    6.33 %      6.16 %    -           GPU

                                                                                                                                                                                            25
