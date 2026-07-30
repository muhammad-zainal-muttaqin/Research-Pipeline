---
source_id: 151
bibtex_key: zou2023objectdetectionsurvey
title: Object Detection in 20 Years: A Survey
year: 2023
domain_theme: Uncoded
verified_pdf: 151_Object Detection in 20 Years (Zou dkk.).pdf
char_count: 195827
---

1

                                                                                                  Object Detection in 20 Years: A Survey
                                                                 Zhengxia Zou? , Keyan Chen, Zhenwei Shi, Member, IEEE, Yuhong Guo, and Jieping Ye? , Fellow, IEEE

                                                     Abstract—Object detection, as of one the most fundamental                                                                                                                                                                             Number of Publications in Object Detection
                                                  and challenging problems in computer vision, has received great                                                                                                                                           4000
                                                Number  of Publications
                                                  attention  in recent in Object
                                                                        years.   Detection
                                                                               Over  the past two decades, we have                                                                                                                                          3500
1400                                              seen a rapid technological evolution of object detection and                                                                                                                                              3000
1200                                              its profound impact on the entire computer vision field. If we                                                                                                                                            2500
                                                  consider today’s object detection technique as a revolution driven                                                                                                                                        2000
1000
                                                  by deep learning, then back in the 1990s, we would see the                                                                                                                                                1500
800
                                                  ingenious thinking and long-term perspective design of early                                                                                                                                              1000
       arXiv:1905.05055v3 [cs.CV] 18 Jan 2023

600                                                                                                                                                                                                                                                          500
                                                  computer vision. This paper extensively reviews this fast-moving
400                                                                                                                                                                                                                                                                0
                                                  research field in the light of technical evolution, spanning over

                                                                                                                                                                                                                                                                          1998
                                                                                                                                                                                                                                                                                 1999
                                                                                                                                                                                                                                                                                         2000
                                                                                                                                                                                                                                                                                                2001
                                                                                                                                                                                                                                                                                                       2002
                                                                                                                                                                                                                                                                                                              2003
                                                                                                                                                                                                                                                                                                                     2004
                                                                                                                                                                                                                                                                                                                            2005
                                                                                                                                                                                                                                                                                                                                   2006
                                                                                                                                                                                                                                                                                                                                          2007
                                                                                                                                                                                                                                                                                                                                                 2008
                                                                                                                                                                                                                                                                                                                                                        2009
                                                                                                                                                                                                                                                                                                                                                               2010
                                                                                                                                                                                                                                                                                                                                                                      2011
                                                                                                                                                                                                                                                                                                                                                                             2012
                                                                                                                                                                                                                                                                                                                                                                                    2013
                                                                                                                                                                                                                                                                                                                                                                                           2014
                                                                                                                                                                                                                                                                                                                                                                                                  2015
                                                                                                                                                                                                                                                                                                                                                                                                         2016
                                                                                                                                                                                                                                                                                                                                                                                                                2017
                                                                                                                                                                                                                                                                                                                                                                                                                       2018
                                                                                                                                                                                                                                                                                                                                                                                                                              2019
                                                                                                                                                                                                                                                                                                                                                                                                                                     2020
                                                                                                                                                                                                                                                                                                                                                                                                                                            2021
200                                               a quarter-century’s time (from the 1990s to 2022). A number of
  0                                               topics have been covered in this paper, including the milestone                                                                                                                                                                                                                                        Year
                 1998
                                      1999
                                                 2000
                                                        2001
                                                               2002
                                                                      2003
                                                                             2004
                                                                                    2005
                                                                                           2006
                                                                                                  2007
                                                                                                         2008
                                                                                                                2009
                                                                                                                       2010
                                                                                                                              2011
                                                                                                                                      2012
                                                                                                                                             2013
                                                                                                                                                     2014
                                                                                                                                                            2015
                                                                                                                                                                   2016
                                                                                                                                                                           2017
                                                                                                                                                                                  2018

                                                  detectors in history, detection datasets, metrics, fundamental                                                                                                                                            Fig. 1: The increasing number of publications in object detec-
                                                  building blocks of Year
                                                                      the detection system, speed-up techniques, and
                                                  the recent state-of-the-art detection methods.                                                                                                                                                            tion from 1998 to 2021. (Data from Google scholar advanced
                                                                                                                                                                                                                                                            search: allintitle: “object detection” OR “detecting objects”.)
                                                       Index Terms—Object detection, Computer vision, Deep learn-
                                                    ing, Convolutional neural networks, Technical evolution.
                                                                               Number of Publications in Object Detection
                                                                                                                                                                                                                                                               As different detection tasks have totally different objectives
                                                                                                         3000
                                                                                                         2500
                                                                                                                  I. I NTRODUCTION                                                                                                                          and constraints, their difficulties may vary from each other. In
                                                                                                         2000
                                                          BJECT detection is an important computer vision task                                                                                                                                              addition to some common challenges in other computer vision
                                                    O                  1500
                                                          that deals with
                                                                       1000
                                                    certain class (such 500
                                                                            detecting instances of visual objects of a
                                                                         as humans, animals, or cars) in digital im-
                                                                                                                                                                                                                                                            tasks such as objects under different viewpoints, illuminations,
                                                                                                                                                                                                                                                            and intraclass variations, the challenges in object detection
                                                    ages. The goal of object
                                                                          0    detection is to develop computational                                                                                                                                        include but are not limited to the following aspects: object
                                                                                                                                                                                                                                                            rotation and scale changes (e.g., small objects), accurate object
                                                                                                                       1998
                                                                                                                              1999
                                                                                                                                     2000
                                                                                                                                            2001
                                                                                                                                                   2002
                                                                                                                                                          2003
                                                                                                                                                                 2004
                                                                                                                                                                        2005
                                                                                                                                                                               2006
                                                                                                                                                                                      2007
                                                                                                                                                                                             2008
                                                                                                                                                                                                    2009
                                                                                                                                                                                                           2010
                                                                                                                                                                                                                  2011
                                                                                                                                                                                                                         2012
                                                                                                                                                                                                                                2013
                                                                                                                                                                                                                                       2014
                                                                                                                                                                                                                                              2015
                                                                                                                                                                                                                                                     2016
                                                                                                                                                                                                                                                            2017
                                                                                                                                                                                                                                                                   2018
                                                                                                                                                                                                                                                                          2019
                                                                                                                                                                                                                                                                                 2020
                                                                                                                                                                                                                                                                                        2021

                                                    models and techniques that provide one of the most basic
                                                    pieces of knowledge needed by computer visionYear    applications:                                                                                                                                      localization, dense and occluded object detection, speed up of
                                                    What objects are where? The two most significant metrics for                                                                                                                                            detection, etc. In Sec. IV, we will give a more detailed analysis
                                                    object detection are accuracy (including classification accuracy                                                                                                                                        of these topics.
                                                                                                                                                                                                                                                               This survey seeks to provide novices with a complete grasp
                                                    and localization accuracy) and speed.
                                                                                                                                                                                                                                                            of object detection technology from many viewpoints, with an
                                                       Object detection serves as a basis for many other computer
                                                                                                                                                                                                                                                            emphasis on its evolution. The key features are three-folds:
                                                    vision tasks, such as instance segmentation [1–4], image
                                                                                                                                                                                                                                                            A comprehensive review in the light of technical evolutions,
                                                    captioning [5–7], object tracking [8], etc. In recent years,
                                                                                                                                                                                                                                                            an in-depth exploration of the key technologies and the recent
                                                    the rapid development of deep learning techniques [9] has
                                                                                                                                                                                                                                                            state of the arts, and a comprehensive analysis of detection
                                                    greatly promoted the progress of object detection, leading to
                                                                                                                                                                                                                                                            speed-up techniques. The main clue focuses on the past,
                                                    remarkable breakthroughs and propelling it to a research hot-
                                                                                                                                                                                                                                                            present, and future, complemented with some other necessary
                                                    spot with unprecedented attention. Object detection has now
                                                                                                                                                                                                                                                            components in object detection, like datasets, metrics, and
                                                    been widely used in many real-world applications, such as
                                                                                                                                                                                                                                                            acceleration techniques. Standing on the technical highway,
                                                    autonomous driving, robot vision, video surveillance, etc. Fig.
                                                                                                                                                                                                                                                            this survey aims to present the evolution of related technolo-
                                                    1 shows the growing number of publications that are associated
                                                                                                                                                                                                                                                            gies, allowing readers to grasp the essential concepts and find
                                                    with “object detection” over the past two decades.
                                                                                                                                                                                                                                                            potential future directions, while neglecting their technical
                                                       The work was supported by the National Natural Science Foundation of                                                                                                                                 specifics.
                                                    China under Grant 62125102, the National Key Research and Development                                                                                                                                      The rest of this paper is organized as follows. In Section
                                                    Program of China (Titled “Brain-inspired General Vision Models and Ap-
                                                    plications”), and the Fundamental Research Funds for the Central Universi-                                                                                                                              II, we review the 20 years’ evolution of object detection.
                                                    ties. (Corresponding Author: Zhengxia Zou (zhengxiazou@buaa.edu.cn) and                                                                                                                                 In Section III, we review the speed-up techniques in object
                                                    Jieping Ye (jpye@umich.edu)).                                                                                                                                                                           detection. The state-of-the-art detection methods of the recent
                                                       Zhengxia Zou is with the Department of Guidance, Navigation and Control,
                                                    School of Astronautics, Beihang University, Beijing 100191, China, and also                                                                                                                             three years are reviewed in Section IV. In Section V, we
                                                    with Shanghai Artificial Intelligence Laboratory, Shanghai 200232, China.                                                                                                                               conclude this paper and make a deep analysis of the further
                                                       Keyan Chen and Zhenwei Shi are with the Image Processing Center, School                                                                                                                              research directions.
                                                    of Astronautics, and with the Beijing Key Laboratory of Digital Media, and
                                                    with the State Key Laboratory of Virtual Reality Technology and Systems,
                                                    Beihang University, Beijing 100191, China, and also with the Shanghai                                                                                                                                                II. O BJECT D ETECTION IN 20 Y EARS
                                                    Artificial Intelligence Laboratory, Shanghai 200232, China.                                                                                                                                                In this section, we will review the history of object detection
                                                       Yuhong Guo is with the School of Computer Science, Carleton University,
                                                    Ottawa, Ontario, K1S 5B6, Canada.                                                                                                                                                                       from multiple views, including milestone detectors, datasets,
                                                       Jieping Ye is with the Alibaba Group, Hangzhou 310030, China.                                                                                                                                        metrics and the evolution of key techniques.
                                                                                                                                                                                                       2

                                                                                                                               + Keypoint Based Detection
 Object Detection Milestones                                                                 + Multi-resolution Detection
                                                                                                                                     CornerNet
                                                                                                                                                                  + End to End Detection

                                                                                             + Hard-negative Mining                                      CenterNet
                                                                                                                                     (L. Hei et al-18)
                                                                                                    SSD (W. Liu Retina-Net                               (X. Zhou et al-19)
                                                 + Bounding Box Regression                          et al-16)   (T. Y. Lin et al-17)
                                       DPM
                HOG Det.                                                                                                                                      + Reference-free Detection
                                       (P. Felzenszwalb et al-08, 10)                    YOLO (J. Redmon                                                            DETR (N. Carion
                (N. Dalal et al-05）                                                                                                                                                        One-stage
                                                                                         et al-16,17)                                                               et al-20)
   VJ Det.                                                                                                                                                                                 detector
   (P. Viola et al-01)                                  + AlexNet
                                                                                       2014       2015     2016      2017        2018      2019     2020        2021      2022
                                                      …
  2001        2004       2006   2008             2012
                                                                                       2014       2015     2016      2017        2018      2019     2020        2021      2022

             Traditional Detection                                                  RCNN                                                                                      Two-stage
                                                                    (R. Girshick et al-14)                                         FPN (T. Y. Lin et al-17)
                   Methods                                                                   SPPNet                                                                           detector
                                                                                     (K. He et al-14)                                 + Feature Fusion
                                                  Deep Learning based                             Fast RCNN
                                                                                                                       Faster RCNN (S. Ren et al-15)
                                                   Detection Methods                         (R. Girshick-15)
                                                                                                                            + Multi-reference Detection (Anchors Boxes)

Fig. 2: A road map of object detection. Milestone detectors in this figure: VJ Det. [10, 11], HOG Det. [12], DPM [13–
15], RCNN [16], SPPNet [17], Fast RCNN [18], Faster RCNN [19], YOLO [20–22], SSD [23], FPN [24], Retina-Net [25],
CornerNet [26], CenterNet [27], DETR [28].

A. A Road Map of Object Detection                                                                   dense grid of uniformly spaced cells and use overlapping local
   In the past two decades, it is widely accepted that the                                          contrast normalization (on “blocks”). Although HOG can be
progress of object detection has generally gone through two                                         used to detect a variety of object classes, it was motivated
historical periods: “traditional object detection period (be-                                       primarily by the problem of pedestrian detection. To detect
fore 2014)” and “deep learning based detection period (after                                        objects of different sizes, the HOG detector rescales the input
2014)”, as shown in Fig. 2. In the following, we will summa-                                        image for multiple times while keeping the size of a detection
rize the milestone detectors of this period, with the emergence                                     window unchanged. The HOG detector has been an important
time and performance serving as the main clue to highlight the                                      foundation of many object detectors [13, 14, 32] and a large
behind driving technology, seeing Fig. 3.                                                           variety of computer vision applications for many years.
   1) Milestones: Traditional Detectors: If we consider to-                                            Deformable Part-based Model (DPM): DPM, as the
day’s object detection technique as a revolution driven by deep                                     winners of VOC-07, -08, and -09 detection challenges, was
learning, then back in the 1990s, we would see the ingenious                                        the epitome of the traditional object detection methods. DPM
design and long-term perspective of early computer vision.                                          was originally proposed by P. Felzenszwalb [13] in 2008 as
Most of the early object detection algorithms were built based                                      an extension of the HOG detector. It follows the detection
on handcrafted features. Due to the lack of effective image                                         philosophy of “divide and conquer”, where the training can
representation at that time, people have to design sophisticated                                    be simply considered as the learning of a proper way of de-
feature representations and a variety of speed-up skills.                                           composing an object, and the inference can be considered as an
   Viola Jones Detectors: In 2001, P. Viola and M. Jones                                            ensemble of detections on different object parts. For example,
achieved real-time detection of human faces for the first                                           the problem of detecting a “car” can be decomposed to the
time without any constraints (e.g., skin color segmentation)                                        detection of its window, body, and wheels. This part of the
[10, 11]. Running on a 700MHz Pentium III CPU, the detector                                         work, a.k.a. “star-model”, was introduced by P. Felzenszwalb
was tens or even hundreds of times faster than other algorithms                                     et al. [13]. Later on, R. Girshick has further extended the star
in its time under comparable detection accuracy. The VJ                                             model to the “mixture models” to deal with the objects in the
detector follows a most straightforward way of detection, i.e.,                                     real world under more significant variations and has made a
sliding windows: to go through all possible locations and                                           series of other improvements [14, 15, 33, 34].
scales in an image to see if any window contains a human face.                                         Although today’s object detectors have far surpassed DPM
Although it seems to be a very simple process, the calculation                                      in detection accuracy, many of them are still deeply influenced
behind it was far beyond the computer’s power of its time.                                          by its valuable insights, e.g., mixture models, hard negative
The VJ detector has dramatically improved its detection speed                                       mining, bounding box regression, context priming, etc. In
by incorporating three important techniques: “integral image”,                                      2010, P. Felzenszwalb and R. Girshick were awarded the
“feature selection”, and “detection cascades” (to be introduced                                     “lifetime achievement” by PASCAL VOC.
in section III).                                                                                       2) Milestones: CNN based Two-stage Detectors: As the
   HOG Detector: In 2005, N. Dalal and B. Triggs proposed                                           performance of hand-crafted features became saturated, the
Histogram of Oriented Gradients (HOG) feature descriptor                                            research of object detection reached a plateau after 2010.
[12]. HOG can be considered as an important improvement                                             In 2012, the world saw the rebirth of convolutional neural
of the scale-invariant feature transform [29, 30] and shape                                         networks [35]. As a deep convolutional network is able to learn
contexts [31] of its time. To balance the feature invariance                                        robust and high-level feature representations of an image, a
(including translation, scale, illumination, etc) and the nonlin-                                   natural question arises: can we introduce it to object detection?
earity, the HOG descriptor is designed to be computed on a                                          R. Girshick et al. took the lead to break the deadlocks in
                                                                                                                                                                                                                               3

                                        Object detection accuracy improvements                                                                                 the convolutional features. SPPNet is more than 20 times
      85.00
                                                                                                        83.80
      80.00                        VOC07 mAP                                                 76.80
                                                                                                                                                               faster than R-CNN without sacrificing any detection accuracy
                                                                                                                      83.50
      75.00
                                   VOC12 mAP
                                   COCO mAP@[.5, .95]                              73.20                74.90
                                                                                                                                                               (VOC07 mAP=59.2%). Although SPPNet has effectively im-
                                                                                                                                               71.90
      70.00                        COCO mAP@.5                          70.00
                                                                                                    70.40                                                      proved the detection speed, it still has some drawbacks: first,
                                                                                                                    62.90      64.10 65.70
                                                                                       68.40
      65.00
                                                                                                       59.10
                                                                                                                                                               the training is still multi-stage, second, SPPNet only fine-tunes
      60.00                                                                                                                              63.90
                                                                   58.50
                                                                                     53.70
                                                                                                                                 61.10                 57.70   its fully connected layers while simply ignoring all previous
      55.00
                                                                                                                                                52.30
                                                                                                                                                               layers. Later in the next year, Fast RCNN [18] was proposed
mAP

      50.00                                                                                 46.50                                      47.10
                                                                                                                               44.70
      45.00                                                                           42.70                            42.10                                   and solved these problems.
                                                                                                            39.10
      40.00                                                                   35.90                36.20                                       43.50              Fast RCNN: In 2015, R. Girshick proposed Fast RCNN
                                                                                                                       41.80
                                                          33.70
      35.00                                                                                                                                                    detector [18], which is a further improvement of R-CNN and
      30.00                                                                                26.80                                                               SPPNet [16, 17]. Fast RCNN enables us to simultaneously
      25.00                21.00
                                                                           19.70
                                                                                   21.90                                                                       train a detector and a bounding box regressor under the
      20.00

      15.00
                                                                                                                                                               same network configurations. On VOC07 dataset, Fast RCNN
               20 0
                   8   )                                             14 ) 14 ) 1 5) 15 ) 1 6) 17 ) 1 7 ) 1 8) 1 9 ) 1 9) 19 ) 2 0 ) 2 1) 2 1 )                 increased the mAP from 58.5% (RCNN) to 70.0% while with
           (                                                     (20 (20 (20 (20 (2 0 (20 (2 0 (2 0 (2 0 (2 0 (20 (2 0 (20 (2 0
        v1                                                     v5 CNN CNN CNN SS D FPN -Net e D et rNet COS H TC LOv4 E TR rm er
   M-                                                     M-     R st R r R                   a            e F
                                                                                                                       Y O a ble Dans fo
 DP                                                     DP         Fa Fa ste               tin Re fi n Cent
                                                                                        Re                               m       r                             a detection speed over 200 times faster than R-CNN. Although
                                                                                                                      for in T
                                                                                                                   D e Sw

                                                                                                                                                               Fast-RCNN successfully integrates the advantages of R-CNN
Fig. 3: Accuracy improvement of object detection on VOC07,
                                                                                                                                                               and SPPNet, its detection speed is still limited by the proposal
VOC12 and MS-COCO datasets. Detectors in this figure:
                                                                                                                                                               detection (see Section II-C1 for more details). Then, a question
DPM-v1 [13], DPM-v5 [37], RCNN [16], SPPNet [17], Fast
                                                                                                                                                               naturally arises: “can we generate object proposals with a CNN
RCNN [18], Faster RCNN [19], SSD [23], FPN [24], Retina-
                                                                                                                                                               model?” Later, Faster R-CNN [19] answered this question.
Net [25], RefineDet [38], TridentNet [39] CenterNet [40],
                                                                                                                                                                  Faster RCNN: In 2015, S. Ren et al. proposed Faster
FCOS [41], HTC [42], YOLOv4 [22], Deformable DETR [43],
                                                                                                                                                               RCNN detector [19, 47] shortly after the Fast RCNN. Faster
Swin Transformer [44].
                                                                                                                                                               RCNN is the first near-realtime deep learning detector (COCO
                                                                                                                                                               mAP@.5=42.7%, VOC07 mAP=73.2%, 17fps with ZF-Net
                                                                                                                                                               [48]). The main contribution of Faster-RCNN is the introduc-
2014 by proposing the Regions with CNN features (RCNN)                                                                                                         tion of Region Proposal Network (RPN) that enables nearly
[16, 36]. Since then, object detection started to evolve at an                                                                                                 cost-free region proposals. From R-CNN to Faster RCNN,
unprecedented speed. There are two groups of detectors in                                                                                                      most individual blocks of an object detection system, e.g., pro-
the deep learning era: “two-stage detectors” and “one-stage                                                                                                    posal detection, feature extraction, bounding box regression,
detectors”, where the former frames the detection as a “coarse-                                                                                                etc, have been gradually integrated into a unified, end-to-end
to-fine” process while the latter frames it as to “complete in                                                                                                 learning framework. Although Faster RCNN breaks through
one step”.                                                                                                                                                     the speed bottleneck of Fast RCNN, there is still computation
   RCNN: The idea behind RCNN is simple: It starts with                                                                                                        redundancy at the subsequent detection stage. Later on, a
the extraction of a set of object proposals (object candidate                                                                                                  variety of improvements have been proposed, including RFCN
boxes) by selective search [45]. Then each proposal is rescaled                                                                                                [49] and Light head RCNN [50]. (See more details in Section
to a fixed size image and fed into a CNN model pretrained                                                                                                      III.)
on ImageNet (say, AlexNet [35]) to extract features. Finally,                                                                                                     Feature Pyramid Networks (FPN): In 2017, T.-Y. Lin
linear SVM classifiers are used to predict the presence of an                                                                                                  et al. proposed FPN [24]. Before FPN, most of the deep
object within each region and to recognize object categories.                                                                                                  learning based detectors run detection only on the feature maps
RCNN yields a significant performance boost on VOC07, with                                                                                                     of the networks’ top layer. Although the features in deeper
a large improvement of mean Average Precision (mAP) from                                                                                                       layers of a CNN are beneficial for category recognition, it
33.7% (DPM-v5 [46]) to 58.5%. Although RCNN has made                                                                                                           is not conducive to localizing objects. To this end, a top-
great progress, its drawbacks are obvious: the redundant fea-                                                                                                  down architecture with lateral connections is developed in
ture computations on a large number of overlapped proposals                                                                                                    FPN for building high-level semantics at all scales. Since a
(over 2000 boxes from one image) lead to an extremely slow                                                                                                     CNN naturally forms a feature pyramid through its forward
detection speed (14s per image with GPU). Later in the same                                                                                                    propagation, the FPN shows great advances for detecting
year, SPPNet [17] was proposed and has solved this problem.                                                                                                    objects with a wide variety of scales. Using FPN in a basic
   SPPNet: In 2014, K. He et al. proposed Spatial Pyramid                                                                                                      Faster R-CNN system, it achieves state-of-the-art single model
Pooling Networks (SPPNet) [17]. Previous CNN models re-                                                                                                        detection results on the COCO dataset without bells and
quire a fixed-size input, e.g., a 224x224 image for AlexNet                                                                                                    whistles (COCO mAP@.5=59.1%). FPN has now become a
[35]. The main contribution of SPPNet is the introduction                                                                                                      basic building block of many latest detectors.
of a Spatial Pyramid Pooling (SPP) layer, which enables a                                                                                                         3) Milestones: CNN based One-stage Detectors: Most of
CNN to generate a fixed-length representation regardless of                                                                                                    the two-stage detectors follow a coarse-to-fine processing
the size of the image/region of interest without rescaling it.                                                                                                 paradigm. The coarse strives to improve recall ability, while
When using SPPNet for object detection, the feature maps can                                                                                                   the fine refines the localization on the basis of the coarse
be computed from the entire image only once, and then fixed-                                                                                                   detection, and places more emphasis on the discriminate
length representations of arbitrary regions can be generated                                                                                                   ability. They can easily attain a high precision without any
for training the detectors, which avoids repeatedly computing                                                                                                  bells and whistles, but rarely employed in engineering due to
                                                                                                                                        4

the poor speed and enormous complexity. On the contrary, one-       previous detection paradigm, and view the task as a keypoint
stage detectors can retrieve all objects in one-step inference.     (corners of a box) prediction problem. After obtaining the key
They are well-liked by mobile devices with real-time and easy-      points, it will decouple and re-group the corner points using
deployed features, but their performance suffers noticeably         extra embedding information to form the bounding boxes.
when detecting dense and small objects.                             CornerNet outperforms most one-stage detectors at that time
   You Only Look Once (YOLO): YOLO was proposed by R.               (COCO mAP@.5=57.8%).
Joseph et al. in 2015. It was the first one-stage detector in the      CenterNet: X. Zhou et al proposed CenterNet [40] in 2019.
deep learning era [20]. YOLO is extremely fast: a fast version      It also follows a keypoint-based detection paradigm, but elim-
of YOLO runs at 155fps with VOC07 mAP=52.7%, while                  inates costly post-processes such as group-based keypoint as-
its enhanced version runs at 45fps with VOC07 mAP=63.4%.            signment (in CornerNet [26], ExtremeNet [53], etc) and NMS,
YOLO follows a totally different paradigm from two-stage de-        resulting in a fully end-to-end detection network. CenterNet
tectors: to apply a single neural network to the full image. This   considers an object to be a single point (the object’s center) and
network divides the image into regions and predicts bounding        regresses all of its attributes (such as size, orientation, location,
boxes and probabilities for each region simultaneously. In spite    pose, etc) based on the reference center point. The model is
of its great improvement of detection speed, YOLO suffers           simple and elegant, and it can integrate 3-D object detection,
from a drop of localization accuracy compared with two-             human pose estimation, optical flow learning, depth estima-
stage detectors, especially for some small objects. YOLO’s          tion, and other tasks into a single framework. Despite using
subsequent versions [21, 22, 51] and the latter proposed            such a concise detection concept, CenterNet can also achieve
SSD [23] has paid more attention to this problem. Recently,         comparative detection results (COCO mAP@.5=61.1%).
YOLOv7 [52], a follow-up work from YOLOv4 team, has                    DETR: In recent years, Transformers have deeply affected
been proposed. It outperforms most existing object detectors        the entire field of deep learning, particularly the field of com-
in terms of speed and accuracy (range from 5 FPS to 160             puter vision. Transformers discard the traditional convolution
FPS) by introducing optimized structures like dynamic label         operator in favor of attention-alone calculation in order to
assignment and model structure reparameterization.                  overcome the limitations of CNNs and obtain a global-scale
   Single Shot MultiBox Detector (SSD): SSD [23] was                receptive field. In 2020, N. Carion et al proposed DETR
proposed by W. Liu et al. in 2015. The main contribution            [28], where they viewed object detection as a set prediction
of SSD is the introduction of the multi-reference and multi-        problem and proposed an end-to-end detection network with
resolution detection techniques (to be introduced in Section        Transformers. So far, object detection has entered a new era in
II-C1), which significantly improves the detection accuracy of      which objects can be detected without the use of anchor boxes
a one-stage detector, especially for some small objects. SSD        or anchor points. Later, X. Zhu et al proposed Deformable
has advantages in terms of both detection speed and accuracy        DETR [43] to address the DETR’s long convergence time and
(COCO mAP@.5=46.5%, a fast version runs at 59fps). The              limited performance on detecting small objects. It achieves
main difference between SSD and previous detectors is that          state-of-the-art performance on MSCOCO dataset (COCO
SSD detects objects of different scales on different layers of      mAP@.5=71.9%).
the network, while the previous ones only run detection on
their top layers.
   RetinaNet: Despite its high speed and simplicity, the one-       B. Object Detection Datasets and Metrics
stage detectors have trailed the accuracy of two-stage detectors       1) Datasets: Building larger datasets with less bias is es-
for years. T.-Y. Lin et al. have explored the reasons behind        sential for developing advanced detection algorithms. A num-
and proposed RetinaNet in 2017 [25]. They found that the            ber of well-known detection datasets have been released in the
extreme foreground-background class imbalance encountered           past 10 years, including the datasets of PASCAL VOC Chal-
during the training of dense detectors is the central cause.        lenges [54, 55] (e.g., VOC2007, VOC2012), ImageNet Large
To this end, a new loss function named “focal loss” has             Scale Visual Recognition Challenge (e.g., ILSVRC2014) [56],
been introduced in RetinaNet by reshaping the standard cross        MS-COCO Detection Challenge [57], Open Images Dataset
entropy loss so that detector will put more focus on hard,          [58, 59], Objects365 [60], etc. The statistics of these datasets
misclassified examples during training. Focal Loss enables the      are given in Table I. Fig. 4 shows some image examples of
one-stage detectors to achieve comparable accuracy of two-          these datasets. Fig. 3 shows the improvements of detection
stage detectors while maintaining a very high detection speed       accuracy on VOC07, VOC12 and MS-COCO datasets from
(COCO mAP@.5=59.1%).                                                2008 to 2021.
   CornerNet: Previous methods primarily used anchor boxes             Pascal VOC: The PASCAL Visual Object Classes (VOC)
to provide classification and regression references. Objects        Challenges1 (from 2005 to 2012) [54, 55] was one of the
frequently exhibit variation in terms of number, location,          most important competitions in the early computer vision
scale, ratio, etc. They have to follow the path of setting up       community. Two versions of Pascal-VOC are mostly used
a large number of reference boxes to better match ground            in object detection: VOC07 and VOC12, where the former
truths in order to achieve high performance. However, the           consists of 5k tr. images + 12k annotated objects, and the latter
network would suffer from further category imbalance, lots          consists of 11k tr. images + 27k annotated objects. 20 classes
of hand-designed hyper-parameters, and a long convergence
time. To address these problems, H. Law et al [26] discard the        1 http://host.robots.ox.ac.uk/pascal/VOC/
                                                                                                                                                  5

Fig. 4: Some example images and annotations in (a) PASCAL-VOC07, (b) ILSVRC, (c) MS-COCO, and (d) Open Images.

                                         train                 validation                   trainval                             test
  Dataset
                               images            objects   images      objects         images        objects           images           objects
  VOC-2007                       2,501           6,301      2,510      6,307           5,011            12,608          4,952           14,976
  VOC-2012                       5,717          13,609      5,823     13,841          11,540            27,450         10,991                -
  ILSVRC-2014                  456,567         478,807     20,121     55,502         476,688           534,309         40,152                -
  ILSVRC-2017                  456,567         478,807     20,121     55,502         476,688           534,309         65,500                -
  MS-COCO-2015                  82,783         604,907     40,504    291,875         123,287           896,782         81,434                -
  MS-COCO-2017                 118,287         860,001      5,000     36,781         123,287           896,782         40,670                -
  Objects365-2019              600,000       9,623,000     38,000    479,000         638,000        10,102,000        100,000         1,700,00
  OID-2020                   1,743,042      14,610,229     41,620    303,980       1,784,662        14,914,209        125,436          937,327

                               TABLE I: Some well-known object detection datasets and their statistics.

of objects that are common in life are annotated in these two             Open Images: The year of 2018 sees the introduction of
datasets, e.g., “person”, “cat”, “bicycle”, “sofa”, etc.               the Open Images Detection (OID) challenge4 [62], following
   ILSVRC: The ImageNet Large Scale Visual Recognition                 MS-COCO but at an unprecedented scale. There are two tasks
Challenge (ILSVRC)2 [56] has pushed forward the state of               in Open Images: 1) the standard object detection, and 2) the
the art in generic object detection. ILSVRC is organized each          visual relationship detection which detects paired objects in
year from 2010 to 2017. It contains a detection challenge using        particular relations. For the standard detection task, the dataset
ImageNet images [61]. The ILSVRC detection dataset contains            consists of 1,910k images with 15,440k annotated bounding
200 classes of visual objects. The number of its images/object         boxes on 600 object categories.
instances is two orders of magnitude larger than VOC.                     2) Metrics: How can we evaluate the accuracy of a de-
   MS-COCO: MS-COCO3 [57] is one of the most chal-                     tector? This question may have different answers at different
lenging object detection dataset available today. The annual           times. In the early time’s detection research, there are no
competition based on MS-COCO dataset has been held since               widely accepted evaluation metrics on detection accuracy.
2015. It has less number of object categories than ILSVRC, but         For example, in the early research of pedestrian detection
more object instances. For example, MS-COCO-17 contains                [12], the “miss rate vs. false positives per window (FPPW)”
164k images and 897k annotated objects from 80 categories.             was commonly used as the metric. However, the per-window
Compared with VOC and ILSVRC, the biggest progress of                  measurement can be flawed and fails to predict full image
MS-COCO is that apart from the bounding box annotations,               performance [63]. In 2009, the Caltech pedestrian detection
each object is further labeled using per-instance segmentation         benchmark was introduced [63, 64] and since then, the eval-
to aid in precise localization. In addition, MS-COCO contains          uation metric has changed from FPPW to false positives per-
more small objects (whose area is smaller than 1% of the               image (FPPI).
image) and more densely located objects. Just like ImageNet               In recent years, the most frequently used evaluation for
in its time, MS-COCO has become the de facto standard for              detection is “Average Precision (AP)”, which was originally
the object detection community.                                        introduced in VOC2007. AP is defined as the average detection
                                                                       precision under different recalls, and is usually evaluated in
 2 http://image-net.org/challenges/LSVRC/
 3 http://cocodataset.org/                                               4 https://storage.googleapis.com/openimages/web/index.html
                                                                                                                                                                                       6

       Evolution of Multi-                                                                                                                                             Feature map
                                                                                                                                                                       Detector
       scale Detection     1. Feature pyramids                         2. Detection with        3. Anchor-free      4. Multi-reference         5.Multi-resolu.         Proposals
                                          and sliding windows          object proposals            detection            detection                detection

                Year:        2001         2006            2008         2013          2014            2015              2016          2017        2018         2019   2020      2021
                        Feature Pyramids and Sliding Windows

                                                                       Detection with Object Proposals

                                                                           Anchor-free detection                                                      Anchor-free detection

      @VJ Det. (P. Viola et al-CVPR2001), @HOG Det. (N.                                                            Multi-reference Detection
      Dalal et al-CVPR2005), @DPM (P. Felzenszwalb et
      al-CVPR2008, TPAMI2010), @ Exemplar SVM (T.                                                                                Multi-resolution Detection
      Malisiewicz et al-ICCV2011), @ Overfeat (P.
      Sermanet et al-ICLR2014) …                                 @DNN Det. (C. Szegedy et al-
                                                                 NIPS2013), @YOLO (J. Redmon              Faster-RCNN (S. Ren et al-NIPS2015), @SSD (W. Liu
                                                                 et al-CVPR2016) …                        et al-ECCV2016), @FCOS (Z. Tian et al-ICCV2019),
                                                                                                          @YOLOv4 (A. Bochkovskiy et al-arXiv2020) …

      @RCNN (R. Girshick et al-CVPR2014), @SPPNet (K. He            @SSD (W. Liu et al-ECCV2016), @Unified Det. (Z. Cai et al-
      et al-ECCV2014), @Fast RCNN (R. Girshick-ICCV2015),           ECCV2016) @FPN (T. Y. Lin et al-CVPR2017), @RetinaNet(T.       @CornerNet (H. Law et al-ECCV2018), @CenterNet
      @Faster RCNN (S. Ren et al-NIPS2015) …                        Y. Lin et al-ICCV2017), @Cascade R-CNN (Z. Cai et al-          (X. Zhou et al-arXiv2019), @Reppoints (Z. Yang et
                                                                    CVPR2018), @Swin Transformer (Z. Liu et al-arXiv2021) …        al-ICCV2019), @DETR (N. Carion et al-ECCV2020) …

Fig. 5: Evolution of multi-scale detection techniques in object detection. Detectors in this figure: VJ Det. [10], HOG Det.
[12], DPM [13], Exemplar SVM [32], Overfeat [65], RCNN [16], SPPNet [17], Fast RCNN [18], Faster RCNN [19], DNN
Det. [66], YOLO [20], SSD [23], Unified Det. [67], FPN [24], RetinaNet [25], RefineDet [38], Cascade R-CNN [68], Swin
Transformer [44], FCOS [41], YOLOv4 [22], CornerNet [26], CenterNet [40], Reppoints [69], DETR [28].

a category-specific manner. The mean AP (mAP) averaged                                             detection. In the past 20 years, multi-scale detection has gone
over all categories is usually used as the final metric of                                         through multiple historical periods, as shown in Fig. 5.
performance. To measure the object localization accuracy, the                                         Feature pyramids + sliding windows: After the VJ de-
IoU between the predicted box and the ground truth is used                                         tector, researchers started to pay more attention to a more
to verify whether it is greater than a predefined threshold,                                       intuitive way of detection, i.e. by building “feature pyramid +
say, 0.5. If yes, the object will be identified as “detected”,                                     sliding windows”. From 2004, a number of milestone detectors
otherwise, “missed”. The 0.5-IoU mAP has then become the                                           were built based on this paradigm, including the HOG detector,
de facto metric for object detection.                                                              DPM, etc. They frequently glide a fixed size detection window
   After 2014, due to the introduction of MS-COCO datasets,                                        over the image, paying little attention to ”different aspect
researchers started to pay more attention to the accuracy of                                       ratios”. To detect objects with a more complex appearance, R.
object localization. Instead of using a fixed IoU threshold,                                       Girshick et al. began to seek better solutions outside the feature
MS-COCO AP is averaged over multiple IoU thresholds                                                pyramid. The “mixture model” [15] was a solution at that time,
between 0.5 and 0.95, which encourages more accurate object                                        i.e. to train multiple detectors for objects of different aspect
localization and may be of great importance for some real-                                         ratios. Apart from this, exemplar-based detection [32, 70]
world applications (e.g., imagine there is a robot trying to                                       provided another solution by training individual models for
grasp a spanner).                                                                                  every object instance (exemplar).
                                                                                                      Detection with object proposals: Object proposals refer
C. Technical Evolution in Object Detection                                                         to a group of class-agnostic reference boxes that are likely to
   In this section, we will introduce some important building                                      contain any objects. Detection with object proposals helps to
blocks of a detection system and their technical evolutions.                                       avoid the exhaustive sliding window search across an image.
First, we describe the multi-scale and context priming on                                          We refer readers to the following papers for a comprehensive
model designing, followed by the sample selection strategy                                         review on this topic [71, 72]. Early time’s proposal detection
and the design of the loss function in the training process, and                                   methods followed a bottom-up detection philosophy [73, 74].
lastly, the Non-Maximum Suppression in the inference. The                                          After 2014, with the popularity of deep CNN in visual
time-stamp in the chart and text is supplied by the publication                                    recognition, the top-down, learning-based approaches began
time of papers. The evolution order shown in the figures is                                        to show more advantages in this problem [19, 75, 76]. Now,
primarily to assist readers in understanding and there may be                                      the proposal detection gradually slipped out of sight after the
temporal overlap.                                                                                  rise of one-stage detectors.
   1) Technical Evolution of Multi-Scale Detection: Multi-                                           Deep regression and anchor-free detection: In recent
scale detection of objects with “different sizes” and “different                                   years, with the increase of GPU’s computing power, multi-
aspect ratios” is one of the main technical challenges in object                                   scale detection has become more and more straightforward
                                                                                                                                                                                       7

    Evolution of Context                                                                                                                                       Image      Window
    Priming in Object                                                                                                                                          Feature    Context
    Detection                                 1. With local context
                                                                                2. With global context
                                                                                                                   3. Context interactives

    Year:             2001                2005         2008           2011        2013              2015                 2016    2017        2018     2019         2020      2021

                                                                                                                                Detection with Local Context

                                                                                                                                     Detection with Global Context
    @Face Det. (A. Torralba et al-MIT2001), @MultiPath
    (S. Zagoruyko et al-BMVC2016), @GBDNet (X. Zeng                                                                                  Context Interactives
    et al-ECCV2016, TPAMI2018), @CC-Net (W. Ouyang
    et al-arXiv2017), @MultiRegion-CNN (S. Gidaris et al-
    CVPR2015), @CoupleNet (Y. Zhu et al-ICCV2017) …
                                                                      @ION (S. Bell et al-CVPR2016), @RFCN++ (Z. Li et      @CtxSVM (Q. Chen et al-TPAMI2015), @PersonContext (S.
                                   @DPM (P. Felzenszwalb et           al-AAAI2018), @RBFNet (S. Liu et al-ECCV2018) ,       Gupta et al-arXiv2015), @SMN (X. Chen-ICCV2017),
                                   al-CVPR2010), @StrucDet            @TridentNet (Y. Li et al-ICCV2019), @Non-local        @RelationNet (H. Hu et al-CVPR2018), @SIN (Y. Liu et al-
                                   (C. Desai et al-IJCV2011) …        (X. Wang et al –CVPR2018), @DETR (N. Carion et        CVPR2018), @RescoringNet (L. V. Pato et al-CVPR2020) …
                                                                      al-ECCV2020) …

Fig. 6: Evolution of context priming in object detection. Detectors in this figure: Face Det. [78], MultiPath [79], GBDNet
[80, 81], CC-Net [82], MultiRegion-CNN [83], CoupleNet [84], DPM [14, 15], StructDet [85], ION [86], RFCN++ [87],
RBFNet [88], TridentNet [39], Non-local [89], DETR [28], CtxSVM [90], PersonContext [91], SMN [92], RelationNet [93],
SIN [94], RescoringNet [95].

and brute-force. The idea of using the deep regression to solve                               improve object detection. In the early 2000s, Sinha and Tor-
multi-scale problems becomes simple, i.e., to directly predict                                ralba [78] found that the inclusion of local contextual regions
the coordinates of a bounding box based on the deep learning                                  such as the facial bounding contour substantially improves
features [20, 66]. After 2018, researchers began to think                                     face detection performance. Dalal and Triggs also found
about the object detection problem from the perspective of                                    that incorporating a small amount of background information
keypoint detection. These methods often follow two ideas: One                                 improves the accuracy of pedestrian detection [12]. Recent
is the group-based method which detects keypoints (corners,                                   deep learning based detectors can also be improved with local
centers, or representative points) and then conducts object-                                  context by simply enlarging the networks’ receptive field or
wise grouping [26, 53, 69, 77]; the other is the group-free                                   the size of object proposals [79–84, 97].
method which regards an object as one/many points and then                                       Detection with global context: Global context exploits
regresses the object attributes (size, ratio, etc.) under the                                 scene configuration as an additional source of information
reference of the points [40, 41].                                                             for object detection. For early time detectors, a common
   Multi-reference/-resolution detection: Multi-reference de-                                 way of integrating global context is to integrate a statistical
tection is now the most used method for multi-scale detection                                 summary of the elements that comprise the scene, like Gist
[19, 22, 23, 41, 47, 51]. The main idea of multi-reference                                    [96]. For recent detectors, there are two methods to integrate
detection [19, 22, 23, 41, 47, 51] is to first define a set                                   the global context. The first method is to take advantage
of references (a.k.a. anchors, including boxes and points) at                                 of deep convolution, dilated convolution, deformable con-
every location of an image, and then predict the detection                                    volution, pooling operation [39, 87, 88] to receive a large
box based on these references. Another popular technique                                      receptive field (even larger than the input image). But now,
is multi-resolution detection [23, 24, 44, 67, 68], i.e. by                                   researchers have explored the potential to apply attention based
detecting objects of different scales at different layers of the                              mechanisms (non-local, transformers, etc.) to achieve a full-
network. Multi-reference and multi-resolution detection have                                  image receptive field and have obtained great success [28, 89].
now become two basic building blocks in the state-of-the-art                                  The second method is to think of the global context as a kind
object detection systems.                                                                     of sequential information and to learn it with the recurrent
   2) Technical Evolution of Context Priming: Visual objects                                  neural networks [86, 98].
are usually embedded in a typical context with the surrounding                                   Context interactive: Context interactive refers to the con-
environments. Our brain takes advantage of the associations                                   straints and dependencies that conveys between visual ele-
among objects and environments to facilitate visual perception                                ments. Some recent researches suggested that modern de-
and cognition [96]. Context priming has long been used to                                     tectors can be improved by considering context interactives.
improve detection. Fig. 6 shows the evolution of context                                      Some recent improvements can be grouped into two categories,
priming in object detection.                                                                  where the first one is to explore the relationship between
   Detection with local context: Local context refers to the                                  individual objects [15, 85, 90, 92, 93, 95], and the second
visual information in the area that surrounds the object to                                   one is to explore the dependencies between objects and scenes
detect. It has long been acknowledged that local context helps                                [91, 94].
                                                                                                                                                                                                      8

                                                                 Evolution of Hard Negative Mining
             Year:      1994        2001         2005              2008              2014              2015             2016         2017        2018        2019        2020         2021

           Method                              Bootstrap                                Without Hard Negative Mining                            Bootstrap + New Loss Functions

                        Bootstrap was widely used to deal with the insufficient     By simply balancing the weights between                      Focusing on hard examples
           Remarks
                                  computing resources of early time                      object and background classes                      Computing power is no longer a problem

  @Face Det. (H. A. Rowley et al-CMUTechRep1995), @Haar                                                                       @SSD (W. Liu et al-ECCV2016), @FasterPed (L. Zhang et al-ECCV2016),
  Det. (C. P. Papageorgiou et al-ICCV1998), @VJ Det. (P. Viola   @RCNN (R. Girshick et al-CVPR2014), @SPPNet (K. He           @OHEM (A. Shrivastava et al-CVPR2016), @RetinaNet (T. Y. Lin et al-
  et al-CVPR2001), @HOG Det. (N. Dalal et al-CVPR2005),          et al-ECCV2014), @Fast RCNN (R. Girshick-ICCV2015),          ICCV2017), @RefineDet (Zhang et al-CVPR18), @FCOS (Z. Tian et al-
  @DPM (P. Felzenszwalb et al-CVPR2008, TPAMI2010) …             @Faster RCNN (S. Ren et al-NIPS2015), @YOLO (J.              ICCV2019), @YOLOv4 (A. Bochkovskiy et al-arXiv2020) …
                                                                 Redmon et al-CVPR2016) …

Fig. 7: Evolution of hard negative mining techniques in object detection. Detectors in this figure: Face Det. [99], Haar Det.
[100], VJ Det. [10], HOG Det. [12], DPM [13, 15], RCNN [16], SPPNet [17], Fast RCNN [18], Faster RCNN [19], YOLO
[20], SSD [23], FasterPed [101], OHEM [102], RetinaNet [25], RefineDet [38], FCOS [41], YOLOv4 [22].

   3) Technical Evolution of Hard Negative Mining: The train-                                        where t and t∗ are the locations of predicted and ground-
ing of a detector is essentially an imbalanced learning problem.                                     truth bounding boxes, p and p∗ are their category probabilities.
In the case of sliding window based detectors, the imbalance                                         IoU{a, a∗ } is the IoU between the reference box/point a and
between backgrounds and objects could be as extreme as 107 :1                                        its ground-truth a∗ . η is an IoU threshold, say, 0.5. If an anchor
[71]. In this case, using all backgrounds will be harmful to                                         box/point does not match any objects, its localization loss does
training as the vast number of easy negatives will overwhelm                                         not count in the final loss.
the learning process. Hard negative mining (HNM) aims to                                                Classification loss: Classification loss is used to evaluate
overcome this problem. The technical evolution of HNM is                                             the divergence of the predicted category from the actual
shown in Fig. 7.                                                                                     category, which was not thoroughly investigated in prevIoUs
   Bootstrap: Bootstrap in object detection refers to a group                                        work such as YOLOv1 [20] and YOLOv2 [51] employing
of training techniques in which the training starts with a small                                     MSE/L2 loss (Mean Squared Error). Later, CE loss (Cross-
part of background samples and then iteratively adds new                                             Entropy) is typically used [21, 23, 47]. L2 loss is a measure
miss-classified samples. In early times detectors, bootstrap was                                     in Euclidean space, whereas CE loss can measure distribution
commonly used with the purpose of reducing the training                                              differences (termed as a form of likelihood). The prediction
computations over millions of backgrounds [10, 99, 100].                                             of classification is a probability, so CE loss is preferable to
Later it became a standard technique in DPM and HOG                                                  L2 loss with greater misclassification cost and lower gradi-
detectors [12, 13] for solving the data imbalance problem.                                           ent vanishing effect. For improving categorization efficiency,
   HNM in deep learning based detectors: In the deep                                                 Label Smooth has been proposed to enhance the model gen-
learning era, due to the increase of computing power, bootstrap                                      eralization ability and solve the overconfidence problem on
was shortly discarded in object detection during 2014-2016                                           noise labels [103, 104], and Focal loss is designed to solve the
[16–20]. To ease the data-imbalance problem during training,                                         problem of category imbalance and differences in classification
detectors like Faster RCNN and YOLO simply balance the                                               difficulty [25].
weights between the positive and negative windows. However,                                             Localization loss: Localization loss is used to optimize
researchers later noticed this cannot completely solve the                                           position and size deviation. L2 loss is prevalent in early
imbalanced problem [25]. To this end, the bootstrap was re-                                          research [16, 20, 51], but it is highly affected by outliers and
introduced to object detection after 2016 [23, 38, 101, 102].                                        prone to gradient explosion. Combining the benefits of L1 loss
An alternative improvement is to design new loss functions                                           and L2 loss, the researchers propose Smooth L1 loss [18], as
[25] by reshaping the standard cross entropy loss so that it                                         illustrated in the following formula,
will put more focus on hard, misclassified examples [25].                                                                           (
   4) Technical Evolution of Loss Function: The loss function                                                                         0.5x2      if |x| < 1
                                                                                                                 SmoothL1 (x) =                                      (2)
measures how well the model matches the data (i.e., the                                                                               |x| − 0.5 else
deviation of the predictions from the true labels). Calculating
the loss yields the gradients of the model weights, which can                                        where x denotes the difference between the target and pre-
subsequently be updated by backpropagation to better suit                                            dicted values. When calculating the error, the above losses
the data. Classification loss and localization loss make up the                                      treat four numbers (x, y, w, h) representing a bounding box as
supervision of the object detection problem, seeing Eq. 1. A                                         independent variables, however, a correlation exists between
general form of the loss function can be written as follows:                                         them. Moreover, IoU is utilized to determine if the prediction
                                                                                                     box corresponds to the actual ground truth box in evaluation.
         L(p, p∗ , t, t∗ ) = Lcls. (p, p∗ ) + βI(t)Lloc. (t, t∗ )                                    Equal Smooth L1 values will have totally different IoU values,
                             (                                                                       hence IoU loss [105] is introduced as follows:
                               1 IoU{a, a∗ } > η                                            (1)
                    I(t) =
                               0 else                                                                                               IoU loss = − log(IoU)                                           (3)
                                                                                                                                                                                                             9

       Evolution of Non-Max                                                                                                                  Learner
                                                                                                                                                                                Detector

       Suppression
                                                          1. Greedy selection             2. Bounding box aggregation                 3. Learning to NMS                       4. NMS-free Detector

           Year:        1994         2001           2005             2008          2011          2014          2015        2016            2017          2018         2019          2020         2021

                                                                            Traditional Greedy Selection                                     Greedy Selection with Improvements

                                                                                                      Bounding Box Aggregation

                                                                                               Learning to Non-Maximum Suppression
                                     @VJ Det. (P. Viola
                                     et al-CVPR2001)
                                                                                                                                                         Non-Maximum Suppression Free Detector

   @Face Det. (R. Vaillant et al-VISP1994), @HOG Det. (N. Dalal et al-CVPR2005),                 @StrucDet (C. Desai et al-IJCV2011),                  @SoftNMS (N. Bodla et al-ICCV2017), @FitnessNMS (L.
   @DPM (P. Felzenszwalb et al-CVPR2008, TPAMI2010), @RCNN (R. Girshick et al-                   @MAP-Det (P. Henderson et al-ACCV2016),               Tychsen-Smith et al-CVPR2018), @SofterNMS (Y. He et
   CVPR2014), @SPPNet (K. He et al-ECCV2014) @Fast RCNN (R. Girshick-ICCV2015),                  @LearnNMS (J. Hosang et al-ICCV2017),                 al-CVPR2019), @AdaptiveNMS (S. Liu et al-CVPR2019),
   @Faster RCNN (S. Ren et al-NIPS2015), @YOLO (J. Redmon et al-CVPR2016),                       @RelationNet (H. Hu et al-CVPR2018),                  @DIoUNMS (Z. Zheng et al-AAAI2020) …
   @SSD (W. Liu et al-ECCV2016), @FPN (T. Y. Lin et al-CVPR2017), @RetinaNet(T. Y.               @Learn2Rank (Z. Tan et al-ICCV2019) …
   Lin et al-ICCV2017), @FCOS (Z. Tian et al-ICCV2019) …                                                                                      @CenterNet (X. Zhou et al-arXiv2019), @DETR
                                                                                                                                              (N. Carion et al-ECCV2020), @POTO (J. Wang et
                   @Overfeat (P. Sermanet et al-ICLR2014), @APC-NMS(R. Rothe et al-ACCV2014), @MAPC (D. Mrowca et al-                         al-CVPR2021) …
                   ICCV2015), @WBF (R. Solovyev et al-IVC2021), @ ClusterNMS (Z. Zheng et al-Trans. Cybernetics2021) …

Fig. 8: Evolution of non-max suppression (NMS) techniques in object detection from 1994 to 2021: 1) Greedy selection, 2)
Bounding box aggregation, 3) Learning to NMS, and 4) NMS-free detection. Detectors in this figure: Face Det. [108], HOG
Det. [12], DPM [13, 15], RCNN [16], SPPNet [17], Fast RCNN [18], Faster RCNN [19], YOLO [20], SSD [23], FPN [24],
RetinaNet [25], FCOS [41], StrucDet [85], MAP-Det [109], LearnNMS [110], RelationNet [93], Learn2Rank [111], SoftNMS
[112], FitnessNMS [113], SofterNMS [114], AdaptiveNMS [115], DIoUNMS [107], Overfeat [65], APC-NMS [116], MAPC
[117], WBF [118], ClusterNMS [119], CenterNet [40], DETR [28], POTO [120].

   Following that, several algorithms improved IoU loss. G-                                                   Bounding Box aggregation: BB aggregation is another
IoU (Generalized IoU) [106] improved the case when IoU                                                     group of techniques for NMS [10, 65, 116, 117] with the
loss could not optimize the non-overlapping bounding boxes,                                                idea of combining or clustering multiple overlapped bounding
i.e., IoU = 0. According to Distance-IoU [107], a successful                                               boxes into one final detection. The advantage of this type of
detection regression loss should meet three geometric metrics:                                             method is that it takes full consideration of object relationships
overlap area, center point distance, and aspect ratio. So, based                                           and their spatial layout [118, 119]. Some well-known detectors
on IoU loss and G-IoU loss, DIoU (Distance IoU) is defined                                                 use this method, such as the VJ detector [10] and the Overfeat
as the distance between the center point of the prediction and                                             (winner of ILSVRC-13 localization task) [65].
the ground truth, and CIoU (Complete IoU) [107] considered                                                    Learning based NMS: A recent group of NMS improve-
the aspect ratio difference on the basis of DIoU.                                                          ments that have recently received much attention is learning
   5) Technical Evolution of Non-Maximum Suppression: As                                                   based NMS [85, 93, 109–111, 122]. The main idea is to think
the neighboring windows usually have similar detection scores,                                             of NMS as a filter to re-score all raw detections and to train
the non-maximum suppression is used as a post-processing                                                   the NMS as part of a network in an end-to-end fashion or
step to remove the replicated bounding boxes and obtain the                                                train a net to imitate NMS’s behavior. These methods have
final detection result. At early times of object detection, NMS                                            shown promising results in improving occlusion and dense
was not always integrated [121]. This is because the desired                                               object detection over traditional hand-crafted NMS methods.
output of an object detection system was not entirely clear at                                                NMS-free detector: To release from NMS and achieve a
that time. Fig. 8 shows the evolution of NMS in the past 20                                                fully end-to-end object detection training network, researchers
years.                                                                                                     developed a series of methods to complete one-to-one label
   Greedy selection: Greedy selection is an old-fashioned but                                              assignment (a.k.a. one object with just one prediction box)
the most popular way to perform NMS. The idea behind it                                                    [28, 40, 120]. These methods frequently adhere to a rule that
is simple and intuitive: for a set of overlapped detections,                                               calls for the use of the highest-quality box for training in order
the bounding box with the maximum detection score is se-                                                   to achieve free NMS. NMS-free detectors are more similar to
lected while its neighboring boxes are removed according                                                   the human visual perception system and are also a possible
to a predefined overlap threshold. Although greedy selection                                               way to the future of object detection.
has now become the de facto method for NMS, it still has
some space for improvement. First, the top-scoring box may
                                                                                                                                  III. S PEED -U P OF D ETECTION
not be the best fit. Second, it may suppress nearby objects.
Finally, it does not suppress false positives [116]. Many works                                              The acceleration of a detector has long been a challenging
have been proposed to solve the problems mentioned above                                                   problem. The speed-up techniques in object detection can be
[107, 112, 114, 115].                                                                                      divided into three levels of groups: speed up of “detection
                                                                                                                                                 10

pipeline”, “detector backbone”, and “numerical computation”.
                                                                                            Speed up of
, as shown in Fig. 9. Refer to [123] for a more detailed version.                              detec.           ü Feat. map shared comput.
                                                                                              pipeline          ü Cascaded detection
A. Feature Map Shared Computation                                           Detection
   Among the different computational stages of a detector,                  Speed Up                              ü Network pruning and
                                                                                             Speed up of            quantification
feature extraction usually dominates the amount of compu-                                   detec. engine
                                                                                                                  ü Lightweight network design
tation. The most commonly used idea to reduce the feature
computational redundancy is to compute the feature map of                                                                ü Integral image
the whole image only once [18, 19, 124], which have achieved                            Speed up of numerical            ü FFT
tens or even hundreds of times of acceleration.                                             computations                 ü Vector Quantization
                                                                                                                         ü Reduced rank approx.
B. Cascaded Detection
                                                                       Fig. 9: An overview of the speed-up techniques in object
   Cascaded detection is a commonly used technique [10, 125].
                                                                       detection.
It takes a coarse to fine detection philosophy: to filter out most
of the simple background windows using simple calculations,
then to process those more difficult windows with complex                 3) Depth-wise Separable Convolution: Depth-wise sepa-
ones. In recent years, cascaded detection has been especially          rable convolution [142], as shown in Fig. 10 (e) can be
applied to those detection tasks of “small objects in large            viewed as a special case of the group convolution when the
scenes”, e.g., face detection [126, 127], pedestrian detection         number of groups is set equal to the number of channels.
[101, 124, 128], etc.                                                  Usually, a number of 1x1 filters are used to make a dimension
                                                                       transform so that the final output will have the desired number
C. Network Pruning and Quantification
                                                                       of channels. By using depth-wise separable convolution, the
   “Network pruning” and “network quantification” are two              computation can be reduced from O(dk 2 c) to O(ck 2 )+O(dc).
commonly used methods to speed up a CNN model. The                     This idea has been recently applied to object detection and
former refers to pruning the network structure or weights and          fine-grain classification [143–145].
the latter refers to reducing their code length. The research             4) Bottle-neck Design: A bottleneck layer in a neural net-
of “network pruning” can be traced back to as early as the             work contains few nodes compared to the previous layers. In
1980s [129]. The recent network pruning methods usually                recent years, the bottle-neck design has been widely used for
take an iterative training and pruning process, i.e., to remove        designing lightweight networks [50, 133, 146–148]. Among
only a small group of unimportant weights after each stage             these methods, the input layer of a detector can be compressed
of training, and to repeat those operations [130]. The recent          to reduce the amount of computation from the very beginning
works on network quantification mainly focus on network                of the detection [133, 146, 147]. One can also compress the
binarization, which aims to compress a network by quantifying          feature map to make it thinner, so that to speed up subsequent
its activations or weights to binary variables (say, 0/1) so that      detection [50, 148].
the floating-point operation is converted to logical operations.          5) Detection with NAS: Deep learning-based detectors are
                                                                       becoming increasingly sophisticated, relying heavily on hand-
D. Lightweight Network Design
                                                                       crafted network architecture and training parameters. Neural
   The last group of methods to speed up a CNN based detector          architecture search (NAS) is primarily concerned with defining
is to directly design lightweight networks. In addition to some        the proper space of candidate networks, improving strategies
general designing principles like “fewer channels and more             for searching quickly and accurately, and validating the search-
layers” [131], some other methods have been proposed in                ing results at a low cost. When designing a detection model,
recent years [132–136].                                                NAS can reduce the need for human intervention on the design
   1) Factorizing Convolutions: Factorizing convolutions is            of the network backbone and anchor boxes [149–155].
the most straightforward way to build a lightweight CNN
model. There are two groups of factorizing methods. The first
group is to factorize a large convolution filter into a set of small   E. Numerical Acceleration
ones [50, 87, 137], as shown in Fig. 10 (b). For example, one             Numerical Acceleration aims to accelerate object detectors
can factorize a 7x7 filter into three 3x3 filters, where they share    from the bottom of their implementations.
the same receptive field but the latter one is more efficient.            1) Speed Up with Integral Image: The integral image is
The second group is to factorize convolutions in their channel         an important method in image processing. It helps to rapidly
dimension [138, 139], as shown in Fig. 10 (c).                         calculate summations over image sub-regions. The essence
   2) Group Convolution: Group convolution aims to reduce              of integral image is the integral-differential separability of
the number of parameters in a convolution layer by dividing            convolution in signal processing:
the feature channels into different groups, and then convolve                                      Z
                                                                                                                 dg(x)
on each group independently [140, 141], as shown in Fig.                           f (x) ∗ g(x) = ( f (x)dx) ∗ (       ),         (4)
10 (d). If we evenly divide the features into m groups,                                                            dx
without changing other configurations, the computation will            where if dg(x)/dx is a sparse signal, then the convolution
be theoretically reduced to 1/m of that before.                        can be accelerated by the right part of this equation [10, 156].
                                                                                                                                                                                     11

                                   Feature map                                          Small conv. filters                                                    Feature map
        Feature map         '                                Large conv. filter                                          Feature map …
                                                                                                                                             '!           '…
                       … filters
                                                   '                                                                                                                         '
    (                                                                                                                   (

                                                                    !×!                 ! ! ×! !       !×1   1×!

              (a) Standard convolution                            (b) Factorizing convolutional filters                          (c) Factorizing convolutional channels

                                         '/2 filters
                                                               Feature map
                                                                                                                         ∗                     ' filters (1×1×()
         Feature map                           …                                                                             …
                                     ∗                                            '/2                                    ∗
   (/2                                                                                                                                            (       …                      '
                                               '/2 filters                                         (               …                                  ∗
                                                                                                                             …
   (/2                                                                            '/2
                                           ∗       …

                        (d) Group convolution (#groups = 2)                                                        (e) Depth-wise separable convolution

Fig. 10: An overview of speed up methods of a CNN’s convolutional layer and the comparison of their computational complexity:
                                                                                     0   0                      0
(a) Standard convolution: O(dk 2 c). (b) Factoring convolutional filters (k ×k → (k ×k )2 or 1×k, k ×1): O(dk 2 c) or O(dkc).
(c) Factoring convolutional channels: O(d0 k 2 c) + O(dk 2 d0 ). (d) Group convolution (#groups=m): O(dk 2 c/m). (e) Depth-wise
separable convolution: O(ck 2 ) + O(dc).

 From HOG Map to
                                       Gradient                                Gradient
 Integral HOG Map                                                                                            ! "#"$                   Integral                 Gradient Orientation
                             Orientation Vector                            Orientation image
                                                                                                                                 Orientation image                 Histogram

                                                                                                                                       ! #
                                                                                                                                   $    &
            Cell

           Block
                                                                                                                                                                !−#−$+&

Fig. 11: An illustration of how to compute the “Integral HOG Map” [124]. With integral image techniques, we can efficiently
compute the histogram feature of any location and any size with constant computational complexity.

The integral image can also be used to speed up more general                                       can be accelerated by using the Fast Fourier Transform (FFT)
features in object detection, e.g., color histogram, gradient                                      and the Inverse FFT (IFFT) [160–163].
histogram [124, 157–159], etc. A typical example is to speed                                          3) Vector Quantization: The Vector Quantization (VQ) is a
up HOG by computing integral HOG maps [124, 157], as                                               classical quantization method in signal processing that aims to
shown in Fig. 11. Integral HOG map has been used in pedes-                                         approximate the distribution of a large group of data by a small
trian detection and has achieved dozens of times’ acceleration                                     set of prototype vectors. It can be used for data compression
without losing any accuracy [124].                                                                 and accelerating the inner product operation in object detection
   2) Speed Up in Frequency Domain: Convolution is an                                              [164, 165].
important type of numerical operation in object detection.
As the detection of a linear detector can be viewed as the                                               IV. R ECENT A DVANCES IN O BJECT D ETECTION
window-wise inner product between the feature map and de-                                             The continual appearance of new technologies over the past
tector’s weights, which can be implemented by convolutions.                                        two decades has a considerable influence on object detection,
The Fourier transform is a very practical way to speed up                                          while its fundamental principles and underlying logic have
convolutions, where the theoretical basis is the convolution                                       remained unchanged. In the above sections, we introduced
theorem in signal processing, i.e. under suitable conditions,                                      the evolution of technology over the past two decades in
the Fourier transform F of a convolution of two signals I ∗ W                                      a large-scale time range to help readers comprehend object
is the point-wise product in their Fourier space:                                                  detection; in this section, we will focus more on state-of-the-
                                                                                                   art algorithms in recent years on a short time range to help
                   I ∗ W = F −1 (F (I)                 F (W ))                      (5)            readers understand object detection. Some are expansions of
                                                                                                   previously discussed techniques (e.g., Sec. IV-A – IV-E), while
where F is Fourier transform, F −1 is Inverse Fourier trans-                                       others are novel crossovers that mix concepts (e.g., Sec. IV-F
form, and is the point-wise product. The above calculation                                         – IV-H).
                                                                                                                                   12

Fig. 12: Different training strategies for multi-scale object detection: (a): Training on a single resolution image, back propagate
objects of all scales [17–19, 23]. (b) Training on multi-resolution images (image pyramid), back propagate objects of selected
scale. If an object is too large or too small, its gradient will be discarded [39, 176, 177].

A. Beyond Sliding Window Detection                                    2) Scale Robust Detection: Recent studies have been made
   Since an object in an image can be uniquely determined          for scale robust detection at both training and detection stages.
by its upper left corner and lower right corner of the ground         Scale adaptive training: Modern detectors usually re-scale
truth box, the detection task, therefore, can be equivalently      input images to a fixed size and back propagate the loss of the
framed as a pair-wise key points localization problem. One         objects in all scales. A drawback of doing this is there will be a
recent implementation of this idea is to predict a heat-map        “scale imbalance” problem. Building an image pyramid during
for the corners [26]. Some other methods follow the idea           detection could alleviate this problem but not fundamentally
and utilize more key points (corner and center [77], extreme       [49, 178]. A recent improvement is Scale Normalization for
and center points [53], representative points [69] ) to obtain     Image Pyramids (SNIP) [176], which builds image pyramids
better performance. Another paradigm views an object as a          at both training and detection stages and only backpropagates
point/points and directly predicts the object’s attributes (e.g.   the loss of some selected scales, as shown in Fig. 12. Some
height and width) without grouping. The advantage of this          researchers have further proposed a more efficient training
approach is that it can be implemented under a semantic            strategy: SNIP with Efficient Resampling (SNIPER) [177], i.e.
segmentation framework, and there is no need to design multi-      to crop and re-scale an image to a set of sub-regions so that
scale anchor boxes. Furthermore, by viewing object detection       to benefit from large batch training.
as a set prediction, DETR [28, 43] completely liberates it in         Scale adaptive detection: In CNN based detectors, the size
a reference-based framework.                                       of and aspect ratio of anchors are usually carefully designed. A
                                                                   drawback of doing this is the configurations cannot be adaptive
B. Robust Detection of Rotation and Scale Changes                  to unexpected scale changes. To improve the detection of small
                                                                   objects, some “adaptive zoom-in” techniques are proposed in
   In recent years, efforts have been made on robust detection
                                                                   some recent detectors to adaptively enlarge the small objects
of rotation and scale changes.
                                                                   into the “larger ones” [179, 180]. Another recent improvement
   1) Rotation Robust Detection: Object rotation is common
                                                                   is to predict the scale distribution of objects in an image, and
to see in face detection, text detection, and remote sensing
                                                                   then adaptively re-scaling the image according to it [181, 182].
object detection. The most straightforward solution to this
problem is to perform data augmentation so that an object
in any orientation can be well covered by the augmented data       C. Detection with Better Backbones
distribution [166], or to train independent detectors separately      The accuracy/speed of a detector depends heavily on the
for each orientation [167, 168]. Designing rotation invariant      feature extraction networks, a.k.a, backbones, e.g. the ResNet
loss functions is a recent popular solution, where a constraint    [178], CSPNet [183], Hourglass [184], and Swin Transformer
on the detection loss is added so that the feature of rotated      [44]. For a detailed introduction of some important detection
objects keeps unchanged [169–171]. Another recent solution         backbones in deep learning era, we refer readers to the
is to learn geometric transformations of the objects candidates    following surveys [185]. Fig. 13 shows the detection accuracy
[172–175]. In two-stage detectors, ROI pooling aims to extract     of three well-known detection systems: Faster RCNN [19], R-
a fixed-length feature representation for an object proposal       FCN [49] and SSD [23] with different backbones [186]. Object
with any location and size. Since the feature pooling usually      detection has recently benefited from the powerful feature
is performed in Cartesian coordinates, it is not invariant to      extraction capabilities of Transformers. On the COCO dataset,
rotation transform. A recent improvement is to perform ROI         the top-10 detection methods are all transformer-based 5 . The
pooling in polar coordinates so that the features can be robust
to the rotation changes [167].                                       5 https://paperswithcode.com/sota/object-detection-on-coco
                                                                                                                                     13

performance gap between Transformers and CNNs have been
gradually widened.

D. Improvements of Localization
   To improve localization accuracy, there are two groups of
methods in recent detectors: 1) bounding box refinement, and
2) new loss functions for accurate localization.
   1) Bounding Box Refinement: The most intuitive way to
improve localization accuracy is bounding box refinement,
which can be considered as a post-processing of the detection
results. One recent method is to iteratively feed the detection
results into a BB regressor until the prediction converges
to a correct location and size [187–189]. However, some               Fig. 13: A comparison of detection accuracy of three detectors:
researchers also claimed that this method does not guarantee          Faster RCNN [19], R-FCN [49] and SSD [23] on MS-COCO
the monotonicity of localization accuracy [187] and may               dataset with different detection backbones. Image from J.
degenerate the localization if the refinement is applied for          Huang et al. CVPR 2017 [186].
multiple times.
   2) New Loss Functions for Accurate Localization: In most
modern detectors, object localization is considered as a co-          attention in many tasks such as image generation[194, 195],
ordinate regression problem. However, the drawbacks of this           image style transfer [196], and image super-resolution [197].
paradigm are obvious. First, the regression loss does not                Recently, adversarial training has also been applied to object
correspond to the final evaluation of localization, especially        detection, especially for improving the detection of the small
for some objects with very large aspect ratios. Second, the tra-      and occluded objects. For small object detection, GAN can be
ditional BB regression method does not provide the confidence         used to enhance the features of small objects by narrowing the
of localization. When there are multiple BB’s overlapping with        representations between small and large ones [198, 199]. To
each other, this may lead to failure in non-maximum suppres-          improve the detection of occluded objects, one recent idea is to
sion. The above problems can be alleviated by designing new           generate occlusion masks by using adversarial training [200].
loss functions. The most intuitive improvement is to directly         Instead of generating examples in pixel space, the adversarial
use IoU as the localization loss [105–107, 190]. Besides,             network directly modifies the features to mimic occlusion.
some researchers also tried to improve localization under a
probabilistic inference framework [191]. Different from the
                                                                      G. Weakly Supervised Object Detection
previous methods that directly predict the box coordinates,
this method predicts the probability distribution of a bounding          Training a deep learning based object detector usually
box location.                                                         requires a large amount of manually labeled data. Weakly
                                                                      Supervised Object Detection (WSOD) aims at easing the
E. Learning with Segmentation Loss                                    reliance on data annotation by training a detector with only
                                                                      image-level annotations instead of bounding boxes [201].
   Object detection and semantic segmentation are two fun-               Multi-instance learning is a group of supervised learning
damental tasks in computer vision. Recent researches suggest          algorithms that has seen widespread application in WSOD
object detection can be improved by learning with semantic            [202–209]. Instead of learning with a set of instances which
segmentation losses.                                                  are individually labeled, a multi-instance learning model re-
   To improve detection with segmentation, the simplest way           ceives a set of labeled bags, each containing many instances.
is to think of the segmentation network as a fixed feature            If we consider object candidates in an image as a bag and
extractor and to integrate it into a detector as auxiliary features   image-level annotation as the label, then the WSOD can be
[83, 192, 193]. The advantage of this approach is that it is easy     formulated as a multi-instance learning process.
to implement, while the disadvantage is that the segmentation            Class activation mapping is another recent group of methods
network may bring additional computation.                             for WSOD [210, 211]. The research on CNN visualization has
   Another way is to introduce an additional segmentation             shown that the convolutional layer of a CNN behaves as object
branch on top of the original detector and to train this model        detectors despite there is no supervision on the location of the
with multi-task loss functions (seg. + det.) [4, 42, 192]. The        object. Class activation mapping shed light on how to enable
advantage is the seg. brunch will be removed at the inference         a CNN with localization capability despite being trained on
stage and the detection speed will not be affected. However,          image-level labels [212].
the disadvantage is that the training requires pixel-level image         In addition to the above approaches, some other researchers
annotations.                                                          considered the WSOD as a proposal ranking process by
                                                                      selecting the most informative regions and then training these
F. Adversarial Training                                               regions with image-level annotation [213]. Some other re-
   The Generative Adversarial Networks (GAN) [194], intro-            searchers proposed to mask out different parts of the image. If
duced by A. Goodfellow et al. in 2014, has received great             the detection score drops sharply, then the masked region may
                                                                                                                                 14

contain an object with high probability [214]. More recently,      RGB images and 3D lidar points from multiple sensors) [231,
generative adversarial training has also been used for WSOD        232].
[215].                                                                Detection in videos: Real-time object detection/tracking in
                                                                   HD videos is of great importance for video surveillance and
H. Detection with Domain Adaptation                                autonomous driving. Traditional object detectors are usually
                                                                   designed under for image-wise detection, while simply ignores
   The training process of most object detectors can be es-        the correlations between videos frames. Improving detection
sentially viewed as a likelihood estimation process under the      by exploring the spatial and temporal correlation under the
assumption of independent and identically distributed (i.i.d.)     calculation limitation is an important research direction [233,
data. Object detection with non-i.i.d. data, especially for some   234].
real-world applications, still remains a challenge. Aside from        Cross-modality detection: Object detection with multiple
collecting more data or applying proper data augmentation,         sources/modalities of data, e.g., RGB-D image, lidar, flow,
domain adaptation offers the possibility of narrowing the          sound, text, video, etc, is of great importance for a more
gap between domains. To obtain domain-invariant feature            accurate detection system which performs like human-being’s
representation, feature regularization and adversarial training    perception. Some open questions include: how to immigrate
based methods have been explored at the image, category, or        well-trained detectors to different modalities of data, how to
object levels [216–221]. Cycle-consistent transformation [222]     make information fusion to improve detection, etc [235, 236].
has also been applied to bridge the gap between source and            Towards open-world detection: Out-of-domain general-
target domain [223, 224]. Some other methods also incorporate      ization, zero-shot detection, and incremental detection are
both ideas [225] to acquire better performance.                    emerging topics in object detection. The majority of them
                                                                   devised ways to reduce catastrophic forgetting or utilized
        V. C ONCLUSION AND F UTURE D IRECTIONS                     supplemental information. Humans have an instinct to discover
   Remarkable achievements have been made in object detec-         objects of unknown categories in the environment. When the
tion over the past 20 years. This paper extensively reviews        corresponding knowledge (label) is given, humans will learn
some milestone detectors, key technologies, speed-up meth-         new knowledge from it, and get to keep the patterns. However,
ods, datasets, and metrics in its 20 years of history. Some        it is difficult for current object detection algorithms to grasp
promising future directions may include but are not limited to     the detection ability of unknown classes of objects. Object
the following aspects to help readers get more insights beyond     detection in the open world aims at discovering unknown cat-
the scheme mentioned above.                                        egories of objects when supervision signals are not explicitly
   Lightweight object detection: Lightweight object detection      given or partially given, which holds great promise in appli-
aims to speed up the detection inference to run on low-            cations such as robotics and autonomous driving [237, 238].
power edge devices. Some important applications include               Standing on the highway of technical evolutions, we believe
mobile augmented reality, automatic driving, smart city, smart     this paper will help readers to build a complete road map
cameras, face verification, etc. Although a great effort has       of object detection and to find future directions of this fast-
been made in recent years, the speed gap between a machine         moving research field.
and human eyes still remains large, especially for detecting
some small objects or detecting with multi-source information                              R EFERENCES
[226, 227].                                                          [1] B. Hariharan, P. Arbeláez, R. Girshick, and J. Malik,
   End-to-End object detection: Although some methods                    “Simultaneous detection and segmentation,” in ECCV.
have been developed to detect objects in a fully end-to-                 Springer, 2014, pp. 297–312.
end manner (image to box in a network) using one-to-one              [2] ——, “Hypercolumns for object segmentation and fine-
label assignment training, the majority still use a one-to-many          grained localization,” in Proceedings of the IEEE con-
label assignment method where the non-maximum suppression                ference on computer vision and pattern recognition,
operation is separately designed. Future research on this topic          2015, pp. 447–456.
may focus on designing end-to-end pipelines that maintain            [3] J. Dai, K. He, and J. Sun, “Instance-aware semantic seg-
both high detection accuracy and efficiency [228].                       mentation via multi-task network cascades,” in CVPR,
   Small object detection: Detecting small objects in large              2016, pp. 3150–3158.
scenes has long been a challenge. Some potential application         [4] K. He, G. Gkioxari, P. Dollár, and R. Girshick, “Mask
of this research direction includes counting the population of           r-cnn,” in ICCV. IEEE, 2017, pp. 2980–2988.
people in crowd or animals in the open air and detecting mili-       [5] A. Karpathy and L. Fei-Fei, “Deep visual-semantic
tary targets from satellite images. Some further directions may          alignments for generating image descriptions,” in
include the integration of the visual attention mechanisms and           CVPR, 2015, pp. 3128–3137.
the design of high resolution lightweight networks [229, 230].       [6] K. Xu, J. Ba, R. Kiros, K. Cho, A. Courville,
   3D object detection: Despite recent advances in 2-D object            R. Salakhudinov, R. Zemel, and Y. Bengio, “Show,
detection, applications like autonomous driving rely on access           attend and tell: Neural image caption generation with
to the objects’ location and pose in a 3D world. The future of           visual attention,” in ICML, 2015, pp. 2048–2057.
object detection will receive more attention in the 3D world         [7] Q. Wu, C. Shen, P. Wang, A. Dick, and A. van den
and the utilization of multi-source and multi-view data (e.g.,           Hengel, “Image captioning and visual question an-
                                                                                                                               15

     swering based on attributes and external knowledge,”               “Focal loss for dense object detection,” IEEE trans-
     IEEE transactions on pattern analysis and machine                  actions on pattern analysis and machine intelligence,
     intelligence, vol. 40, no. 6, pp. 1367–1381, 2018.                 2018.
 [8] K. Kang, H. Li, J. Yan, X. Zeng, B. Yang, T. Xiao,            [26] H. Law and J. Deng, “Cornernet: Detecting objects
     C. Zhang, Z. Wang, R. Wang, X. Wang et al., “T-cnn:                as paired keypoints,” in Proceedings of the European
     Tubelets with convolutional neural networks for object             conference on computer vision (ECCV), 2018, pp. 734–
     detection from videos,” IEEE Transactions on Circuits              750.
     and Systems for Video Technology, vol. 28, no. 10, pp.        [27] Z.-Q. Zhao, P. Zheng, S.-t. Xu, and X. Wu, “Object
     2896–2907, 2018.                                                   detection with deep learning: A review,” IEEE transac-
 [9] Y. LeCun, Y. Bengio, and G. Hinton, “Deep learning,”               tions on neural networks and learning systems, vol. 30,
     nature, vol. 521, no. 7553, p. 436, 2015.                          no. 11, pp. 3212–3232, 2019.
[10] P. Viola and M. Jones, “Rapid object detection using a        [28] N. Carion, F. Massa, G. Synnaeve, N. Usunier, A. Kir-
     boosted cascade of simple features,” in CVPR, vol. 1.              illov, and S. Zagoruyko, “End-to-end object detection
     IEEE, 2001, pp. I–I.                                               with transformers,” in European Conference on Com-
[11] P. Viola and M. J. Jones, “Robust real-time face detec-            puter Vision. Springer, 2020, pp. 213–229.
     tion,” International journal of computer vision, vol. 57,     [29] D. G. Lowe, “Object recognition from local scale-
     no. 2, pp. 137–154, 2004.                                          invariant features,” in ICCV, vol. 2. Ieee, 1999, pp.
[12] N. Dalal and B. Triggs, “Histograms of oriented gra-               1150–1157.
     dients for human detection,” in CVPR, vol. 1. IEEE,           [30] ——, “Distinctive image features from scale-invariant
     2005, pp. 886–893.                                                 keypoints,” International journal of computer vision,
[13] P. Felzenszwalb, D. McAllester, and D. Ramanan, “A                 vol. 60, no. 2, pp. 91–110, 2004.
     discriminatively trained, multiscale, deformable part         [31] S. Belongie, J. Malik, and J. Puzicha, “Shape matching
     model,” in CVPR. IEEE, 2008, pp. 1–8.                              and object recognition using shape contexts,” CALI-
[14] P. F. Felzenszwalb, R. B. Girshick, and D. McAllester,             FORNIA UNIV SAN DIEGO LA JOLLA DEPT OF
     “Cascade object detection with deformable part mod-                COMPUTER SCIENCE AND ENGINEERING, Tech.
     els,” in CVPR. IEEE, 2010, pp. 2241–2248.                          Rep., 2002.
[15] P. F. Felzenszwalb, R. B. Girshick, D. McAllester, and        [32] T. Malisiewicz, A. Gupta, and A. A. Efros, “Ensemble
     D. Ramanan, “Object detection with discriminatively                of exemplar-svms for object detection and beyond,” in
     trained part-based models,” IEEE transactions on pat-              ICCV. IEEE, 2011, pp. 89–96.
     tern analysis and machine intelligence, vol. 32, no. 9,       [33] R. B. Girshick, P. F. Felzenszwalb, and D. A. Mcallester,
     pp. 1627–1645, 2010.                                               “Object detection with grammar models,” in Advances
[16] R. Girshick, J. Donahue, T. Darrell, and J. Malik, “Rich           in Neural Information Processing Systems, 2011, pp.
     feature hierarchies for accurate object detection and              442–450.
     semantic segmentation,” in CVPR, 2014, pp. 580–587.           [34] R. B. Girshick, From rigid templates to grammars:
[17] K. He, X. Zhang, S. Ren, and J. Sun, “Spatial pyra-                Object detection with structured models.        Citeseer,
     mid pooling in deep convolutional networks for visual              2012.
     recognition,” in ECCV. Springer, 2014, pp. 346–361.           [35] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Ima-
[18] R. Girshick, “Fast r-cnn,” in ICCV, 2015, pp. 1440–                genet classification with deep convolutional neural net-
     1448.                                                              works,” in Advances in neural information processing
[19] S. Ren, K. He, R. Girshick, and J. Sun, “Faster r-                 systems, 2012, pp. 1097–1105.
     cnn: Towards real-time object detection with region           [36] R. Girshick, J. Donahue, T. Darrell, and J. Malik,
     proposal networks,” in Advances in neural information              “Region-based convolutional networks for accurate ob-
     processing systems, 2015, pp. 91–99.                               ject detection and segmentation,” IEEE transactions
[20] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi,                on pattern analysis and machine intelligence, vol. 38,
     “You only look once: Unified, real-time object detec-              no. 1, pp. 142–158, 2016.
     tion,” in CVPR, 2016, pp. 779–788.                            [37] M. A. Sadeghi and D. Forsyth, “30hz object detection
[21] J. Redmon and A. Farhadi, “Yolov3: An incremental                  with dpm v5,” in ECCV. Springer, 2014, pp. 65–79.
     improvement,” arXiv preprint arXiv:1804.02767, 2018.          [38] S. Zhang, L. Wen, X. Bian, Z. Lei, and S. Z. Li, “Single-
[22] A. Bochkovskiy, C.-Y. Wang, and H.-Y. M. Liao,                     shot refinement neural network for object detection,” in
     “Yolov4: Optimal speed and accuracy of object detec-               CVPR, 2018.
     tion,” arXiv preprint arXiv:2004.10934, 2020.                 [39] Y. Li, Y. Chen, N. Wang, and Z. Zhang, “Scale-aware
[23] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed,                trident networks for object detection,” arXiv preprint
     C.-Y. Fu, and A. C. Berg, “Ssd: Single shot multibox               arXiv:1901.01892, 2019.
     detector,” in ECCV. Springer, 2016, pp. 21–37.                [40] X. Zhou, D. Wang, and P. Krähenbühl, “Objects as
[24] T.-Y. Lin, P. Dollár, R. B. Girshick, K. He, B. Hariharan,        points,” arXiv preprint arXiv:1904.07850, 2019.
     and S. J. Belongie, “Feature pyramid networks for             [41] Z. Tian, C. Shen, H. Chen, and T. He, “Fcos: Fully con-
     object detection.” in CVPR, vol. 1, no. 2, 2017, p. 4.             volutional one-stage object detection,” in Proceedings
[25] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár,           of the IEEE/CVF international conference on computer
                                                                                                                           16

     vision, 2019, pp. 9627–9636.                                      lenge,” International Journal of Computer Vision, vol.
[42] K. Chen, J. Pang, J. Wang, Y. Xiong, X. Li, S. Sun,               115, no. 3, pp. 211–252, 2015.
     W. Feng, Z. Liu, J. Shi, W. Ouyang et al., “Hybrid           [57] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona,
     task cascade for instance segmentation,” in Proceedings           D. Ramanan, P. Dollár, and C. L. Zitnick, “Microsoft
     of the IEEE/CVF Conference on Computer Vision and                 coco: Common objects in context,” in ECCV. Springer,
     Pattern Recognition, 2019, pp. 4974–4983.                         2014, pp. 740–755.
[43] X. Zhu, W. Su, L. Lu, B. Li, X. Wang, and J. Dai,            [58] A. Kuznetsova, H. Rom, N. Alldrin, J. Uijlings,
     “Deformable detr: Deformable transformers for end-to-             I. Krasin, J. Pont-Tuset, S. Kamali, S. Popov, M. Mal-
     end object detection,” arXiv preprint arXiv:2010.04159,           loci, A. Kolesnikov, T. Duerig, and V. Ferrari, “The
     2020.                                                             open images dataset v4: Unified image classification,
[44] Z. Liu, Y. Lin, Y. Cao, H. Hu, Y. Wei, Z. Zhang,                  object detection, and visual relationship detection at
     S. Lin, and B. Guo, “Swin transformer: Hierarchical vi-           scale,” IJCV, 2020.
     sion transformer using shifted windows,” arXiv preprint      [59] R. Benenson, S. Popov, and V. Ferrari, “Large-scale
     arXiv:2103.14030, 2021.                                           interactive object segmentation with human annotators,”
[45] J. R. Uijlings, K. E. Van De Sande, T. Gevers, and A. W.          in CVPR, 2019.
     Smeulders, “Selective search for object recognition,”        [60] S. Shao, Z. Li, T. Zhang, C. Peng, G. Yu, X. Zhang,
     International journal of computer vision, vol. 104, no. 2,        J. Li, and J. Sun, “Objects365: A large-scale, high-
     pp. 154–171, 2013.                                                quality dataset for object detection,” in Proceedings of
[46] R. B. Girshick, P. F. Felzenszwalb, and D. McAllester,            the IEEE/CVF International Conference on Computer
     “Discriminatively trained deformable part models,                 Vision, 2019, pp. 8430–8439.
     release 5,” http://people.cs.uchicago.edu/ rbg/latent-       [61] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and
     release5/.                                                        L. Fei-Fei, “Imagenet: A large-scale hierarchical image
[47] S. Ren, K. He, R. Girshick, and J. Sun, “Faster r-cnn:            database,” in CVPR. Ieee, 2009, pp. 248–255.
     towards real-time object detection with region proposal      [62] I. Krasin and T. e. a. Duerig, “Openimages: A
     networks,” IEEE Transactions on Pattern Analysis &                public dataset for large-scale multi-label and multi-
     Machine Intelligence, no. 6, pp. 1137–1149, 2017.                 class image classification.” Dataset available from
[48] M. D. Zeiler and R. Fergus, “Visualizing and under-               https://storage.googleapis.com/openimages/web/index.html,
     standing convolutional networks,” in ECCV. Springer,              2017.
     2014, pp. 818–833.                                           [63] P. Dollár, C. Wojek, B. Schiele, and P. Perona, “Pedes-
[49] J. Dai, Y. Li, K. He, and J. Sun, “R-fcn: Object de-              trian detection: A benchmark,” in CVPR. IEEE, 2009,
     tection via region-based fully convolutional networks,”           pp. 304–311.
     in Advances in neural information processing systems,        [64] P. Dollar, C. Wojek, B. Schiele, and P. Perona, “Pedes-
     2016, pp. 379–387.                                                trian detection: An evaluation of the state of the art,”
[50] Z. Li, C. Peng, G. Yu, X. Zhang, Y. Deng, and J. Sun,             IEEE transactions on pattern analysis and machine
     “Light-head r-cnn: In defense of two-stage object de-             intelligence, vol. 34, no. 4, pp. 743–761, 2012.
     tector,” arXiv preprint arXiv:1711.07264, 2017.              [65] P. Sermanet, D. Eigen, X. Zhang, M. Mathieu, R. Fer-
[51] J. Redmon and A. Farhadi, “Yolo9000: better, faster,              gus, and Y. LeCun, “Overfeat: Integrated recogni-
     stronger,” arXiv preprint, 2017.                                  tion, localization and detection using convolutional net-
[52] C.-Y. Wang, A. Bochkovskiy, and H.-Y. M. Liao,                    works,” arXiv preprint arXiv:1312.6229, 2013.
     “Yolov7: Trainable bag-of-freebies sets new state-of-        [66] C. Szegedy, A. Toshev, and D. Erhan, “Deep neural
     the-art for real-time object detectors,” arXiv preprint           networks for object detection,” in Advances in neural
     arXiv:2207.02696, 2022.                                           information processing systems, 2013, pp. 2553–2561.
[53] X. Zhou, J. Zhuo, and P. Krahenbuhl, “Bottom-up object       [67] Z. Cai, Q. Fan, R. S. Feris, and N. Vasconcelos, “A
     detection by grouping extreme and center points,” in              unified multi-scale deep convolutional neural network
     Proceedings of the IEEE/CVF Conference on Computer                for fast object detection,” in ECCV. Springer, 2016,
     Vision and Pattern Recognition, 2019, pp. 850–859.                pp. 354–370.
[54] M. Everingham, L. Van Gool, C. K. Williams, J. Winn,         [68] Z. Cai and N. Vasconcelos, “Cascade r-cnn: Delving
     and A. Zisserman, “The pascal visual object classes               into high quality object detection,” in Proceedings of
     (voc) challenge,” International journal of computer               the IEEE conference on computer vision and pattern
     vision, vol. 88, no. 2, pp. 303–338, 2010.                        recognition, 2018, pp. 6154–6162.
[55] M. Everingham, S. A. Eslami, L. Van Gool, C. K.              [69] Z. Yang, S. Liu, H. Hu, L. Wang, and S. Lin, “Rep-
     Williams, J. Winn, and A. Zisserman, “The pascal visual           points: Point set representation for object detection,” in
     object classes challenge: A retrospective,” International         Proceedings of the IEEE/CVF International Conference
     journal of computer vision, vol. 111, no. 1, pp. 98–136,          on Computer Vision, 2019, pp. 9657–9666.
     2015.                                                        [70] T. Malisiewicz, Exemplar-based representations for ob-
[56] O. Russakovsky, J. Deng, H. Su, J. Krause, S. Satheesh,           ject detection, association and beyond.         Carnegie
     S. Ma, Z. Huang, A. Karpathy, A. Khosla, M. Bernstein             Mellon University, 2011.
     et al., “Imagenet large scale visual recognition chal-       [71] J. Hosang, R. Benenson, P. Dollár, and B. Schiele,
                                                                                                                              17

     “What makes for effective detection proposals?” IEEE              accurate and fast object detection,” in Proceedings of
     transactions on pattern analysis and machine intelli-             the European Conference on Computer Vision (ECCV),
     gence, vol. 38, no. 4, pp. 814–830, 2016.                         2018, pp. 385–400.
[72] J. Hosang, R. Benenson, and B. Schiele, “How                 [89] X. Wang, R. Girshick, A. Gupta, and K. He, “Non-
     good are detection proposals, really?” arXiv preprint             local neural networks,” in Proceedings of the IEEE
     arXiv:1406.6962, 2014.                                            conference on computer vision and pattern recognition,
[73] B. Alexe, T. Deselaers, and V. Ferrari, “What is an               2018, pp. 7794–7803.
     object?” in CVPR. IEEE, 2010, pp. 73–80.                     [90] Q. Chen, Z. Song, J. Dong, Z. Huang, Y. Hua, and
[74] ——, “Measuring the objectness of image windows,”                  S. Yan, “Contextualizing object detection and classi-
     IEEE transactions on pattern analysis and machine                 fication,” IEEE transactions on pattern analysis and
     intelligence, vol. 34, no. 11, pp. 2189–2202, 2012.               machine intelligence, vol. 37, no. 1, pp. 13–27, 2015.
[75] M.-M. Cheng, Z. Zhang, W.-Y. Lin, and P. Torr, “Bing:        [91] S. Gupta, B. Hariharan, and J. Malik, “Exploring person
     Binarized normed gradients for objectness estimation at           context and local scene context for object detection,”
     300fps,” in CVPR, 2014, pp. 3286–3293.                            arXiv preprint arXiv:1511.08177, 2015.
[76] D. Erhan, C. Szegedy, A. Toshev, and D. Anguelov,            [92] X. Chen and A. Gupta, “Spatial memory for context rea-
     “Scalable object detection using deep neural networks,”           soning in object detection,” in Proceedings of the IEEE
     in CVPR, 2014, pp. 2147–2154.                                     international conference on computer vision, 2017, pp.
[77] K. Duan, S. Bai, L. Xie, H. Qi, Q. Huang, and Q. Tian,            4086–4096.
     “Centernet: Keypoint triplets for object detection,” in      [93] H. Hu, J. Gu, Z. Zhang, J. Dai, and Y. Wei, “Rela-
     Proceedings of the IEEE/CVF International Conference              tion networks for object detection,” in Proceedings of
     on Computer Vision, 2019, pp. 6569–6578.                          the IEEE conference on computer vision and pattern
[78] A. Torralba and P. Sinha, “Detecting faces in impover-            recognition, 2018, pp. 3588–3597.
     ished images,” MASSACHUSETTS INST OF TECH                    [94] Y. Liu, R. Wang, S. Shan, and X. Chen, “Structure
     CAMBRIDGE ARTIFICIAL INTELLIGENCE LAB,                            inference net: Object detection using scene-level context
     Tech. Rep., 2001.                                                 and instance-level relationships,” in CVPR, 2018, pp.
[79] S. Zagoruyko, A. Lerer, T.-Y. Lin, P. O. Pinheiro,                6985–6994.
     S. Gross, S. Chintala, and P. Dollár, “A multi-             [95] L. V. Pato, R. Negrinho, and P. M. Q. Aguiar, “See-
     path network for object detection,” arXiv preprint                ing without looking: Contextual rescoring of object
     arXiv:1604.02135, 2016.                                           detections for ap maximization,” in Proceedings of the
[80] X. Zeng, W. Ouyang, B. Yang, J. Yan, and X. Wang,                 IEEE/CVF Conference on Computer Vision and Pattern
     “Gated bi-directional cnn for object detection,” in               Recognition (CVPR), June 2020.
     ECCV. Springer, 2016, pp. 354–369.                           [96] S. K. Divvala, D. Hoiem, J. H. Hays, A. A. Efros, and
[81] X. Zeng, W. Ouyang, J. Yan, H. Li, T. Xiao, K. Wang,              M. Hebert, “An empirical study of context in object
     Y. Liu, Y. Zhou, B. Yang, Z. Wang et al., “Crafting gbd-          detection,” in CVPR. IEEE, 2009, pp. 1271–1278.
     net for object detection,” IEEE transactions on pattern      [97] C. Chen, M.-Y. Liu, O. Tuzel, and J. Xiao, “R-cnn
     analysis and machine intelligence, vol. 40, no. 9, pp.            for small object detection,” in Asian conference on
     2109–2123, 2018.                                                  computer vision. Springer, 2016, pp. 214–230.
[82] W. Ouyang, K. Wang, X. Zhu, and X. Wang, “Learning           [98] J. Li, Y. Wei, X. Liang, J. Dong, T. Xu, J. Feng, and
     chained deep features and classifiers for cascade in ob-          S. Yan, “Attentive contexts for object detection,” IEEE
     ject detection,” arXiv preprint arXiv:1702.07054, 2017.           Transactions on Multimedia, vol. 19, no. 5, pp. 944–
[83] S. Gidaris and N. Komodakis, “Object detection via                954, 2017.
     a multi-region and semantic segmentation-aware cnn           [99] H. A. Rowley, S. Baluja, and T. Kanade, “Human
     model,” in ICCV, 2015, pp. 1134–1142.                             face detection in visual scenes,” in Advances in Neural
[84] Y. Zhu, C. Zhao, J. Wang, X. Zhao, Y. Wu, H. Lu et al.,           Information Processing Systems, 1996, pp. 875–881.
     “Couplenet: Coupling global structure with local parts      [100] C. P. Papageorgiou, M. Oren, and T. Poggio, “A general
     for object detection,” in ICCV, vol. 2, 2017.                     framework for object detection,” in ICCV. IEEE, 1998,
[85] C. Desai, D. Ramanan, and C. C. Fowlkes, “Discrimina-             pp. 555–562.
     tive models for multi-class object layout,” International   [101] L. Zhang, L. Lin, X. Liang, and K. He, “Is faster r-
     journal of computer vision, vol. 95, no. 1, pp. 1–12,             cnn doing well for pedestrian detection?” in ECCV.
     2011.                                                             Springer, 2016, pp. 443–457.
[86] S. Bell, C. Lawrence Zitnick, K. Bala, and R. Girshick,     [102] A. Shrivastava, A. Gupta, and R. Girshick, “Training
     “Inside-outside net: Detecting objects in context with            region-based object detectors with online hard example
     skip pooling and recurrent neural networks,” in CVPR,             mining,” in CVPR, 2016, pp. 761–769.
     2016, pp. 2874–2883.                                        [103] C. Szegedy, V. Vanhoucke, S. Ioffe, J. Shlens, and
[87] Z. Li, Y. Chen, G. Yu, and Y. Deng, “R-fcn++: Towards             Z. Wojna, “Rethinking the inception architecture for
     accurate region-based fully convolutional networks for            computer vision,” in Proceedings of the IEEE confer-
     object detection.” in AAAI, 2018.                                 ence on computer vision and pattern recognition, 2016,
[88] S. Liu, D. Huang et al., “Receptive field block net for           pp. 2818–2826.
                                                                                                                                18

[104] R. Müller, S. Kornblith, and G. E. Hinton, “When does             107, p. 104117, 2021.
      label smoothing help?” Advances in neural information        [119] Z. Zheng, P. Wang, D. Ren, W. Liu, R. Ye, Q. Hu, and
      processing systems, vol. 32, 2019.                                 W. Zuo, “Enhancing geometric factors in model learn-
[105] J. Yu, Y. Jiang, Z. Wang, Z. Cao, and T. Huang,                    ing and inference for object detection and instance seg-
      “Unitbox: An advanced object detection network,” in                mentation,” IEEE Transactions on Cybernetics, 2021.
      Proceedings of the 2016 ACM on Multimedia Confer-            [120] J. Wang, L. Song, Z. Li, H. Sun, J. Sun, and N. Zheng,
      ence. ACM, 2016, pp. 516–520.                                      “End-to-end object detection with fully convolutional
[106] H. Rezatofighi, N. Tsoi, J. Gwak, A. Sadeghian, I. Reid,           network,” in Proceedings of the IEEE/CVF Conference
      and S. Savarese, “Generalized intersection over union:             on Computer Vision and Pattern Recognition, 2021, pp.
      A metric and a loss for bounding box regression,” in               15 849–15 858.
      Proceedings of the IEEE/CVF Conference on Computer           [121] C. Papageorgiou and T. Poggio, “A trainable system
      Vision and Pattern Recognition, 2019, pp. 658–666.                 for object detection,” International journal of computer
[107] Z. Zheng, P. Wang, W. Liu, J. Li, R. Ye, and D. Ren,               vision, vol. 38, no. 1, pp. 15–33, 2000.
      “Distance-iou loss: Faster and better learning for bound-    [122] L. Wan, D. Eigen, and R. Fergus, “End-to-end integra-
      ing box regression,” in Proceedings of the AAAI Con-               tion of a convolution network, deformable parts model
      ference on Artificial Intelligence, vol. 34, no. 07, 2020,         and non-maximum suppression,” in CVPR, 2015, pp.
      pp. 12 993–13 000.                                                 851–859.
[108] R. Vaillant, C. Monrocq, and Y. Le Cun, “Original            [123] Z. Zou, Z. Shi, Y. Guo, and J. Ye, “Object detection in
      approach for the localisation of objects in images,” IEE           20 years: A survey,” arXiv preprint arXiv:1905.05055,
      Proceedings-Vision, Image and Signal Processing, vol.              2019.
      141, no. 4, pp. 245–250, 1994.                               [124] Q. Zhu, M.-C. Yeh, K.-T. Cheng, and S. Avidan, “Fast
[109] P. Henderson and V. Ferrari, “End-to-end training of               human detection using a cascade of histograms of
      object class detectors for mean average precision,” in             oriented gradients,” in CVPR, vol. 2. IEEE, 2006, pp.
      Asian Conference on Computer Vision. Springer, 2016,               1491–1498.
      pp. 198–213.                                                 [125] F. Fleuret and D. Geman, “Coarse-to-fine face detec-
[110] J. H. Hosang, R. Benenson, and B. Schiele, “Learning               tion,” International Journal of computer vision, vol. 41,
      non-maximum suppression.” in CVPR, 2017, pp. 6469–                 no. 1-2, pp. 85–107, 2001.
      6477.                                                        [126] H. Li, Z. Lin, X. Shen, J. Brandt, and G. Hua, “A con-
[111] Z. Tan, X. Nie, Q. Qian, N. Li, and H. Li, “Learning to            volutional neural network cascade for face detection,”
      rank proposals for object detection,” in Proceedings of            in CVPR, 2015, pp. 5325–5334.
      the IEEE/CVF International Conference on Computer            [127] K. Zhang, Z. Zhang, Z. Li, and Y. Qiao, “Joint face
      Vision, 2019, pp. 8273–8281.                                       detection and alignment using multitask cascaded con-
[112] N. Bodla, B. Singh, R. Chellappa, and L. S. Davis,                 volutional networks,” IEEE Signal Processing Letters,
      “Soft-nms—improving object detection with one line                 vol. 23, no. 10, pp. 1499–1503, 2016.
      of code,” in ICCV. IEEE, 2017, pp. 5562–5570.                [128] Z. Cai, M. Saberian, and N. Vasconcelos, “Learning
[113] L. Tychsen-Smith and L. Petersson, “Improving object               complexity-aware cascades for deep pedestrian detec-
      localization with fitness nms and bounded iou loss,”               tion,” in ICCV, 2015, pp. 3361–3369.
      arXiv preprint arXiv:1711.00164, 2017.                       [129] Y. LeCun, J. S. Denker, and S. A. Solla, “Optimal brain
[114] Y. He, C. Zhu, J. Wang, M. Savvides, and X. Zhang,                 damage,” in Advances in neural information processing
      “Bounding box regression with uncertainty for accurate             systems, 1990, pp. 598–605.
      object detection,” in Proceedings of the IEEE/CVF Con-       [130] S. Han, H. Mao, and W. J. Dally, “Deep compres-
      ference on Computer Vision and Pattern Recognition,                sion: Compressing deep neural networks with prun-
      2019, pp. 2888–2897.                                               ing, trained quantization and huffman coding,” arXiv
[115] S. Liu, D. Huang, and Y. Wang, “Adaptive nms: Re-                  preprint arXiv:1510.00149, 2015.
      fining pedestrian detection in a crowd,” in Proceedings      [131] K. He and J. Sun, “Convolutional neural networks at
      of the IEEE/CVF Conference on Computer Vision and                  constrained time cost,” in CVPR, 2015, pp. 5353–5360.
      Pattern Recognition, 2019, pp. 6459–6468.                    [132] Z. Qin, Z. Li, Z. Zhang, Y. Bao, G. Yu, Y. Peng,
[116] R. Rothe, M. Guillaumin, and L. Van Gool, “Non-                    and J. Sun, “Thundernet: Towards real-time generic
      maximum suppression for object detection by passing                object detection on mobile devices,” in Proceedings of
      messages between windows,” in Asian Conference on                  the IEEE/CVF International Conference on Computer
      Computer Vision. Springer, 2014, pp. 290–306.                      Vision, 2019, pp. 6718–6727.
[117] D. Mrowca, M. Rohrbach, J. Hoffman, R. Hu,                   [133] R. J. Wang, X. Li, and C. X. Ling, “Pelee: A real-time
      K. Saenko, and T. Darrell, “Spatial semantic regular-              object detection system on mobile devices,” in Advances
      isation for large scale object detection,” in ICCV, 2015,          in Neural Information Processing Systems 31, S. Ben-
      pp. 2003–2011.                                                     gio, H. Wallach, H. Larochelle, K. Grauman, N. Cesa-
[118] R. Solovyev, W. Wang, and T. Gabruseva, “Weighted                  Bianchi, and R. Garnett, Eds. Curran Associates, Inc.,
      boxes fusion: Ensembling boxes from different object               2018, pp. 1967–1976.
      detection models,” Image and Vision Computing, vol.          [134] R. Huang, J. Pedoeem, and C. Chen, “Yolo-lite: a real-
                                                                                                                                  19

      time object detection algorithm optimized for non-gpu              fpn: Automatic network architecture adaptation for ob-
      computers,” in 2018 IEEE International Conference on               ject detection beyond classification,” in Proceedings of
      Big Data (Big Data). IEEE, 2018, pp. 2503–2510.                    the IEEE/CVF International Conference on Computer
[135] H. Law, Y. Teng, O. Russakovsky, and J. Deng,                      Vision, 2019, pp. 6649–6658.
      “Cornernet-lite: Efficient keypoint based object detec-      [151] G. Ghiasi, T.-Y. Lin, and Q. V. Le, “Nas-fpn: Learning
      tion,” arXiv preprint arXiv:1904.08900, 2019.                      scalable feature pyramid architecture for object detec-
[136] G. Yu, Q. Chang, W. Lv, C. Xu, C. Cui, W. Ji, Q. Dang,             tion,” in Proceedings of the IEEE/CVF Conference on
      K. Deng, G. Wang, Y. Du et al., “Pp-picodet: A better              Computer Vision and Pattern Recognition, 2019, pp.
      real-time object detector on mobile devices,” arXiv                7036–7045.
      preprint arXiv:2111.00902, 2021.                             [152] J. Guo, K. Han, Y. Wang, C. Zhang, Z. Yang, H. Wu,
[137] C. Szegedy, V. Vanhoucke, S. Ioffe, J. Shlens, and                 X. Chen, and C. Xu, “Hit-detector: Hierarchical trinity
      Z. Wojna, “Rethinking the inception architecture for               architecture search for object detection,” in Proceedings
      computer vision,” in CVPR, 2016, pp. 2818–2826.                    of the IEEE/CVF Conference on Computer Vision and
[138] X. Zhang, J. Zou, X. Ming, K. He, and J. Sun, “Efficient           Pattern Recognition, 2020, pp. 11 405–11 414.
      and accurate approximations of nonlinear convolutional       [153] N. Wang, Y. Gao, H. Chen, P. Wang, Z. Tian, C. Shen,
      networks,” in CVPR, 2015, pp. 1984–1992.                           and Y. Zhang, “Nas-fcos: Fast neural architecture search
[139] X. Zhang, J. Zou, K. He, and J. Sun, “Accelerating                 for object detection,” in Proceedings of the IEEE/CVF
      very deep convolutional networks for classification and            Conference on Computer Vision and Pattern Recogni-
      detection,” IEEE transactions on pattern analysis and              tion, 2020, pp. 11 943–11 951.
      machine intelligence, vol. 38, no. 10, pp. 1943–1955,        [154] L. Yao, H. Xu, W. Zhang, X. Liang, and Z. Li, “Sm-
      2016.                                                              nas: structural-to-modular neural architecture search for
[140] X. Zhang, X. Zhou, M. Lin, and J. Sun, “Shufflenet:                object detection,” in Proceedings of the AAAI Confer-
      An extremely efficient convolutional neural network for            ence on Artificial Intelligence, vol. 34, no. 07, 2020, pp.
      mobile devices,” 2017.                                             12 661–12 668.
[141] G. Huang, S. Liu, L. van der Maaten, and K. Q.               [155] C. Jiang, H. Xu, W. Zhang, X. Liang, and Z. Li,
      Weinberger, “Condensenet: An efficient densenet using              “Sp-nas: Serial-to-parallel backbone search for object
      learned group convolutions,” group, vol. 3, no. 12, p. 11,         detection,” in Proceedings of the IEEE/CVF Conference
      2017.                                                              on Computer Vision and Pattern Recognition, 2020, pp.
[142] F. Chollet, “Xception: Deep learning with depthwise                11 863–11 872.
      separable convolutions,” arXiv preprint, pp. 1610–           [156] P. Simard, L. Bottou, P. Haffner, and Y. LeCun,
      02 357, 2017.                                                      “Boxlets: a fast convolution algorithm for signal pro-
[143] A. G. Howard, M. Zhu, B. Chen, D. Kalenichenko,                    cessing and neural networks,” in Advances in Neural
      W. Wang, T. Weyand, M. Andreetto, and H. Adam,                     Information Processing Systems, 1999, pp. 571–577.
      “Mobilenets: Efficient convolutional neural networks         [157] X. Wang, T. X. Han, and S. Yan, “An hog-lbp human
      for mobile vision applications,” arXiv preprint                    detector with partial occlusion handling,” in ICCV.
      arXiv:1704.04861, 2017.                                            IEEE, 2009, pp. 32–39.
[144] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and             [158] F. Porikli, “Integral histogram: A fast way to extract
      L.-C. Chen, “Mobilenetv2: Inverted residuals and linear            histograms in cartesian spaces,” in CVPR, vol. 1. IEEE,
      bottlenecks,” in CVPR. IEEE, 2018, pp. 4510–4520.                  2005, pp. 829–836.
[145] Y. Li, J. Li, W. Lin, and J. Li, “Tiny-dsod: Lightweight     [159] P. Dollár, Z. Tu, P. Perona, and S. Belongie, “Integral
      object detection for resource-restricted usages,” arXiv            channel features,” 2009.
      preprint arXiv:1807.11013, 2018.                             [160] M. Mathieu, M. Henaff, and Y. LeCun, “Fast training
[146] F. N. Iandola, S. Han, M. W. Moskewicz, K. Ashraf,                 of convolutional networks through ffts,” arXiv preprint
      W. J. Dally, and K. Keutzer, “Squeezenet: Alexnet-level            arXiv:1312.5851, 2013.
      accuracy with 50x fewer parameters and¡ 0.5 mb model         [161] H. Pratt, B. Williams, F. Coenen, and Y. Zheng, “Fcnn:
      size,” arXiv preprint arXiv:1602.07360, 2016.                      Fourier convolutional neural networks,” in Joint Euro-
[147] B. Wu, F. N. Iandola, P. H. Jin, and K. Keutzer,                   pean Conference on Machine Learning and Knowledge
      “Squeezedet: Unified, small, low power fully convolu-              Discovery in Databases. Springer, 2017, pp. 786–798.
      tional neural networks for real-time object detection for    [162] N. Vasilache, J. Johnson, M. Mathieu, S. Chintala,
      autonomous driving.” in CVPR Workshops, 2017, pp.                  S. Piantino, and Y. LeCun, “Fast convolutional nets with
      446–454.                                                           fbfft: A gpu performance evaluation,” arXiv preprint
[148] T. Kong, A. Yao, Y. Chen, and F. Sun, “Hypernet:                   arXiv:1412.7580, 2014.
      Towards accurate region proposal generation and joint        [163] O. Rippel, J. Snoek, and R. P. Adams, “Spectral rep-
      object detection,” in CVPR, 2016, pp. 845–853.                     resentations for convolutional neural networks,” in Ad-
[149] Y. Chen, T. Yang, X. Zhang, G. Meng, C. Pan, and                   vances in neural information processing systems, 2015,
      J. Sun, “Detnas: Neural architecture search on object              pp. 2449–2457.
      detection,” arXiv preprint arXiv:1903.10979, 2019.           [164] M. A. Sadeghi and D. Forsyth, “Fast template evalu-
[150] H. Xu, L. Yao, W. Zhang, X. Liang, and Z. Li, “Auto-               ation with vector quantization,” in Advances in neural
                                                                                                                                   20

      information processing systems, 2013, pp. 2949–2957.                CVPR, 2016, pp. 2351–2359.
[165] I. Kokkinos, “Bounding part scores for rapid detection        [181] S. Qiao, W. Shen, W. Qiu, C. Liu, and A. L. Yuille,
      with deformable part models,” in ECCV. Springer,                    “Scalenet: Guiding object proposal generation in super-
      2012, pp. 41–50.                                                    markets and beyond.” in ICCV, 2017, pp. 1809–1818.
[166] H. Zhu, X. Chen, W. Dai, K. Fu, Q. Ye, and J. Jiao,           [182] Z. Hao, Y. Liu, H. Qin, J. Yan, X. Li, and X. Hu, “Scale-
      “Orientation robust object detection in aerial images               aware face detection,” in CVPR, vol. 3, 2017.
      using deep convolutional neural network,” in ICIP.            [183] C.-Y. Wang, H.-Y. M. Liao, Y.-H. Wu, P.-Y. Chen, J.-
      IEEE, 2015, pp. 3735–3739.                                          W. Hsieh, and I.-H. Yeh, “Cspnet: A new backbone that
[167] B. Cai, Z. Jiang, H. Zhang, Y. Yao, and S. Nie, “Online             can enhance learning capability of cnn,” in Proceedings
      exemplar-based fully convolutional network for aircraft             of the IEEE/CVF conference on computer vision and
      detection in remote sensing images,” IEEE Geoscience                pattern recognition workshops, 2020, pp. 390–391.
      and Remote Sensing Letters, no. 99, pp. 1–5, 2018.            [184] A. Newell, K. Yang, and J. Deng, “Stacked hourglass
[168] G. Cheng, J. Han, P. Zhou, and L. Guo, “Multi-                      networks for human pose estimation,” in European
      class geospatial object detection and geographic image              conference on computer vision. Springer, 2016, pp.
      classification based on collection of part detectors,”              483–499.
      ISPRS Journal of Photogrammetry and Remote Sensing,           [185] J. Gu, Z. Wang, J. Kuen, L. Ma, A. Shahroudy, B. Shuai,
      vol. 98, pp. 119–132, 2014.                                         T. Liu, X. Wang, L. Wang, G. Wang et al., “Re-
[169] G. Cheng, P. Zhou, and J. Han, “Rifd-cnn: Rotation-                 cent advances in convolutional neural networks,” arXiv
      invariant and fisher discriminative convolutional neural            preprint arXiv:1512.07108, 2015.
      networks for object detection,” in CVPR, 2016, pp.            [186] J. Huang, V. Rathod, C. Sun, M. Zhu, A. Korattikara,
      2884–2893.                                                          A. Fathi, I. Fischer, Z. Wojna, Y. Song, S. Guadarrama
[170] ——, “Learning rotation-invariant convolutional neural               et al., “Speed/accuracy trade-offs for modern convolu-
      networks for object detection in vhr optical remote                 tional object detectors,” in CVPR, vol. 4, 2017.
      sensing images,” IEEE Transactions on Geoscience and          [187] Z. Cai and N. Vasconcelos, “Cascade r-cnn: Delving
      Remote Sensing, vol. 54, no. 12, pp. 7405–7415, 2016.               into high quality object detection,” in CVPR, vol. 1,
[171] G. Cheng, J. Han, P. Zhou, and D. Xu, “Learn-                       no. 2, 2018, p. 10.
      ing rotation-invariant and fisher discriminative convo-       [188] R. N. Rajaram, E. Ohn-Bar, and M. M. Trivedi, “Re-
      lutional neural networks for object detection,” IEEE                finenet: Iterative refinement for accurate object localiza-
      Transactions on Image Processing, vol. 28, no. 1, pp.               tion,” in ITSC. IEEE, 2016, pp. 1528–1533.
      265–278, 2018.                                                [189] M.-C. Roh and J.-y. Lee, “Refining faster-rcnn for accu-
[172] X. Shi, S. Shan, M. Kan, S. Wu, and X. Chen, “Real-                 rate object detection,” in Machine Vision Applications
      time rotation-invariant face detection with progressive             (MVA), 2017 Fifteenth IAPR International Conference
      calibration networks,” in CVPR, 2018, pp. 2295–2303.                on. IEEE, 2017, pp. 514–517.
[173] M. Jaderberg, K. Simonyan, A. Zisserman et al., “Spa-         [190] B. Jiang, R. Luo, J. Mao, T. Xiao, and Y. Jiang,
      tial transformer networks,” in Advances in neural infor-            “Acquisition of localization confidence for accurate
      mation processing systems, 2015, pp. 2017–2025.                     object detection,” in Proceedings of the ECCV, Munich,
[174] D. Chen, G. Hua, F. Wen, and J. Sun, “Supervised                    Germany, 2018, pp. 8–14.
      transformer network for efficient face detection,” in         [191] S. Gidaris and N. Komodakis, “Locnet: Improving
      ECCV. Springer, 2016, pp. 122–138.                                  localization accuracy for object detection,” in CVPR,
[175] J. Ding, N. Xue, Y. Long, G.-S. Xia, and Q. Lu, “Learn-             2016, pp. 789–798.
      ing roi transformer for oriented object detection in aerial   [192] S. Brahmbhatt, H. I. Christensen, and J. Hays, “Stuffnet:
      images,” in Proceedings of the IEEE/CVF Conference                  Using ‘stuff’to improve object detection,” in Applica-
      on Computer Vision and Pattern Recognition, 2019, pp.               tions of Computer Vision (WACV), 2017 IEEE Winter
      2849–2858.                                                          Conference on. IEEE, 2017, pp. 934–943.
[176] B. Singh and L. S. Davis, “An analysis of scale in-           [193] A. Shrivastava and A. Gupta, “Contextual priming and
      variance in object detection–snip,” in CVPR, 2018, pp.              feedback for faster r-cnn,” in ECCV. Springer, 2016,
      3578–3587.                                                          pp. 330–348.
[177] B. Singh, M. Najibi, and L. S. Davis, “Sniper: Efficient      [194] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu,
      multi-scale training,” arXiv preprint arXiv:1805.09300,             D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio,
      2018.                                                               “Generative adversarial nets,” in Advances in neural
[178] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual                 information processing systems, 2014, pp. 2672–2680.
      learning for image recognition,” in CVPR, 2016, pp.           [195] A. Radford, L. Metz, and S. Chintala, “Unsuper-
      770–778.                                                            vised representation learning with deep convolu-
[179] M. Gao, R. Yu, A. Li, V. I. Morariu, and L. S. Davis,               tional generative adversarial networks,” arXiv preprint
      “Dynamic zoom-in network for fast object detection in               arXiv:1511.06434, 2015.
      large images,” in CVPR, 2018.                                 [196] J.-Y. Zhu, T. Park, P. Isola, and A. A. Efros, “Unpaired
[180] Y. Lu, T. Javidi, and S. Lazebnik, “Adaptive object                 image-to-image translation using cycle-consistent ad-
      detection using adjacency and zoom prediction,” in                  versarial networks,” arXiv preprint, 2017.
                                                                                                                                21

[197] C. Ledig, L. Theis, F. Huszár, J. Caballero, A. Cun-               and L. Van Gool, “Weakly supervised cascaded convo-
      ningham, A. Acosta, A. P. Aitken, A. Tejani, J. Totz,               lutional networks.” in CVPR, vol. 1, no. 2, 2017, p. 8.
      Z. Wang et al., “Photo-realistic single image super-          [212] B. Zhou, A. Khosla, A. Lapedriza, A. Oliva, and
      resolution using a generative adversarial network.” in              A. Torralba, “Learning deep features for discriminative
      CVPR, vol. 2, no. 3, 2017, p. 4.                                    localization,” in CVPR, 2016, pp. 2921–2929.
[198] J. Li, X. Liang, Y. Wei, T. Xu, J. Feng, and S. Yan,          [213] H. Bilen and A. Vedaldi, “Weakly supervised deep
      “Perceptual generative adversarial networks for small               detection networks,” in CVPR, 2016, pp. 2846–2854.
      object detection,” in CVPR, 2017.                             [214] L. Bazzani, A. Bergamo, D. Anguelov, and L. Torresani,
[199] Y. Bai, Y. Zhang, M. Ding, and B. Ghanem, “Sod-                     “Self-taught object localization with deep networks,” in
      mtgan: Small object detection via multi-task generative             Applications of Computer Vision (WACV), 2016 IEEE
      adversarial network,” Computer Vision-ECCV, pp. 8–14,               Winter Conference on. IEEE, 2016, pp. 1–9.
      2018.                                                         [215] Y. Shen, R. Ji, S. Zhang, W. Zuo, and Y. Wang,
[200] X. Wang, A. Shrivastava, and A. Gupta, “A-fast-rcnn:                “Generative adversarial learning towards fast weakly
      Hard positive generation via adversary for object detec-            supervised detection,” in CVPR, 2018, pp. 5764–5773.
      tion,” in CVPR, 2017.                                         [216] Y. Chen, W. Li, C. Sakaridis, D. Dai, and L. Van Gool,
[201] D. Zhang, J. Han, G. Cheng, and M.-H. Yang, “Weakly                 “Domain adaptive faster r-cnn for object detection in
      supervised object localization and detection: A survey,”            the wild,” in Proceedings of the IEEE conference on
      IEEE transactions on pattern analysis and machine                   computer vision and pattern recognition, 2018, pp.
      intelligence, vol. 44, no. 9, pp. 5866–5885, 2021.                  3339–3348.
[202] T. G. Dietterich, R. H. Lathrop, and T. Lozano-Pérez,        [217] Y. Wang, R. Zhang, S. Zhang, M. Li, Y. Xia, X. Zhang,
      “Solving the multiple instance problem with axis-                   and S. Liu, “Domain-specific suppression for adaptive
      parallel rectangles,” Artificial intelligence, vol. 89, no.         object detection,” in Proceedings of the IEEE/CVF Con-
      1-2, pp. 31–71, 1997.                                               ference on Computer Vision and Pattern Recognition,
[203] S. Andrews, I. Tsochantaridis, and T. Hofmann, “Sup-                2021, pp. 9603–9612.
      port vector machines for multiple-instance learning,”         [218] L. Hou, Y. Zhang, K. Fu, and J. Li, “Informative
      in Advances in neural information processing systems,               and consistent correspondence mining for cross-domain
      2003, pp. 577–584.                                                  weakly supervised object detection,” in Proceedings of
[204] R. G. Cinbis, J. Verbeek, and C. Schmid, “Weakly                    the IEEE/CVF Conference on Computer Vision and
      supervised object localization with multi-fold multiple             Pattern Recognition, 2021, pp. 9929–9938.
      instance learning,” IEEE transactions on pattern anal-        [219] X. Zhu, J. Pang, C. Yang, J. Shi, and D. Lin, “Adapting
      ysis and machine intelligence, vol. 39, no. 1, pp. 189–             object detectors via selective cross-domain alignment,”
      203, 2017.                                                          in Proceedings of the IEEE/CVF Conference on Com-
[205] D. P. Papadopoulos, J. R. Uijlings, F. Keller, and                  puter Vision and Pattern Recognition, 2019, pp. 687–
      V. Ferrari, “We don’t need no bounding-boxes: Training              696.
      object class detectors using only human verification,” in     [220] K. Saito, Y. Ushiku, T. Harada, and K. Saenko, “Strong-
      CVPR, 2016, pp. 854–863.                                            weak distribution alignment for adaptive object detec-
[206] D. Zhang, W. Zeng, J. Yao, and J. Han, “Weakly su-                  tion,” in Proceedings of the IEEE/CVF Conference on
      pervised object detection using proposal-and semantic-              Computer Vision and Pattern Recognition, 2019, pp.
      level relationships,” IEEE Transactions on Pattern Anal-            6956–6965.
      ysis and Machine Intelligence, 2020.                          [221] C.-D. Xu, X.-R. Zhao, X. Jin, and X.-S. Wei, “Exploring
[207] P. Tang, X. Wang, S. Bai, W. Shen, X. Bai, W. Liu, and              categorical regularization for domain adaptive object
      A. Yuille, “Pcl: Proposal cluster learning for weakly               detection,” in Proceedings of the IEEE/CVF Conference
      supervised object detection,” IEEE transactions on pat-             on Computer Vision and Pattern Recognition, 2020, pp.
      tern analysis and machine intelligence, vol. 42, no. 1,             11 724–11 733.
      pp. 176–191, 2018.                                            [222] J.-Y. Zhu, T. Park, P. Isola, and A. A. Efros, “Unpaired
[208] E. Sangineto, M. Nabi, D. Culibrk, and N. Sebe,                     image-to-image translation using cycle-consistent ad-
      “Self paced deep learning for weakly supervised object              versarial networks,” in Proceedings of the IEEE interna-
      detection,” IEEE transactions on pattern analysis and               tional conference on computer vision, 2017, pp. 2223–
      machine intelligence, vol. 41, no. 3, pp. 712–725, 2018.            2232.
[209] D. Zhang, J. Han, L. Zhao, and D. Meng, “Leveraging           [223] T. Kim, M. Jeong, S. Kim, S. Choi, and C. Kim,
      prior-knowledge for weakly supervised object detection              “Diversify and match: A domain adaptive representation
      under a collaborative self-paced curriculum learning                learning paradigm for object detection,” in Proceedings
      framework,” International Journal of Computer Vision,               of the IEEE/CVF Conference on Computer Vision and
      vol. 127, no. 4, pp. 363–380, 2019.                                 Pattern Recognition, 2019, pp. 12 456–12 465.
[210] Y. Zhu, Y. Zhou, Q. Ye, Q. Qiu, and J. Jiao, “Soft            [224] N. Inoue, R. Furuta, T. Yamasaki, and K. Aizawa,
      proposal networks for weakly supervised object local-               “Cross-domain weakly-supervised object detection
      ization,” in ICCV, 2017, pp. 1841–1850.                             through progressive domain adaptation,” in Proceedings
[211] A. Diba, V. Sharma, A. M. Pazandeh, H. Pirsiavash,                  of the IEEE conference on computer vision and pattern
                                                                                                                              22

      recognition, 2018, pp. 5001–5009.                           [238] Y. Zhong, J. Yang, P. Zhang, C. Li, N. Codella, L. H.
[225] H.-K. Hsu, C.-H. Yao, Y.-H. Tsai, W.-C. Hung, H.-                 Li, L. Zhou, X. Dai, L. Yuan, Y. Li et al., “Regionclip:
      Y. Tseng, M. Singh, and M.-H. Yang, “Progressive                  Region-based language-image pretraining,” in Proceed-
      domain adaptation for object detection,” in Proceedings           ings of the IEEE/CVF Conference on Computer Vision
      of the IEEE/CVF Winter Conference on Applications of              and Pattern Recognition, 2022, pp. 16 793–16 803.
      Computer Vision, 2020, pp. 749–757.
[226] B. Bosquet, M. Mucientes, and V. M. Brea, “Stdnet-
      st: Spatio-temporal convnet for small object detection,”
      Pattern Recognition, vol. 116, p. 107929, 2021.
[227] C. Yang, Z. Huang, and N. Wang, “Querydet: Cascaded
      sparse query for accelerating high-resolution small ob-
      ject detection,” in Proceedings of the IEEE/CVF Con-
      ference on Computer Vision and Pattern Recognition,
      2022, pp. 13 668–13 677.
[228] P. Sun, Y. Jiang, E. Xie, W. Shao, Z. Yuan, C. Wang,
      and P. Luo, “What makes for end-to-end object detec-
      tion?” in International Conference on Machine Learn-
      ing. PMLR, 2021, pp. 9934–9944.
[229] X. Zhou, X. Xu, W. Liang, Z. Zeng, S. Shimizu, L. T.
      Yang, and Q. Jin, “Intelligent small object detection
      for digital twin in smart manufacturing with industrial
      cyber-physical systems,” IEEE Transactions on Indus-
      trial Informatics, vol. 18, no. 2, pp. 1377–1386, 2021.
[230] G. Cheng, X. Yuan, X. Yao, K. Yan, Q. Zeng,
      and J. Han, “Towards large-scale small object de-
      tection: Survey and benchmarks,” arXiv preprint
      arXiv:2207.14096, 2022.
[231] Y. Wang, V. C. Guizilini, T. Zhang, Y. Wang, H. Zhao,
      and J. Solomon, “Detr3d: 3d object detection from
      multi-view images via 3d-to-2d queries,” in Conference
      on Robot Learning. PMLR, 2022, pp. 180–191.
[232] Y. Wang, T. Ye, L. Cao, W. Huang, F. Sun, F. He, and
      D. Tao, “Bridged transformer for vision and point cloud
      3d object detection,” in Proceedings of the IEEE/CVF
      Conference on Computer Vision and Pattern Recogni-
      tion, 2022, pp. 12 114–12 123.
[233] X. Cheng, H. Xiong, D.-P. Fan, Y. Zhong, M. Harandi,
      T. Drummond, and Z. Ge, “Implicit motion handling
      for video camouflaged object detection,” in Proceedings
      of the IEEE/CVF Conference on Computer Vision and
      Pattern Recognition, 2022, pp. 13 864–13 873.
[234] Q. Zhou, X. Li, L. He, Y. Yang, G. Cheng, Y. Tong,
      L. Ma, and D. Tao, “Transvod: End-to-end video ob-
      ject detection with spatial-temporal transformers,” arXiv
      preprint arXiv:2201.05047, 2022.
[235] R. Cong, Q. Lin, C. Zhang, C. Li, X. Cao, Q. Huang,
      and Y. Zhao, “Cir-net: Cross-modality interaction and
      refinement for rgb-d salient object detection,” IEEE
      Transactions on Image Processing, 2022.
[236] Y. Wang, L. Zhu, S. Huang, T. Hui, X. Li, F. Wang,
      and S. Liu, “Cross-modality domain adaptation for
      freespace detection: A simple yet effective baseline,” in
      Proceedings of the 30th ACM International Conference
      on Multimedia, 2022, pp. 4031–4042.
[237] C. Feng, Y. Zhong, Z. Jie, X. Chu, H. Ren, X. Wei,
      W. Xie, and L. Ma, “Promptdet: Expand your detec-
      tor vocabulary with uncurated images,” arXiv preprint
      arXiv:2203.16513, 2022.
