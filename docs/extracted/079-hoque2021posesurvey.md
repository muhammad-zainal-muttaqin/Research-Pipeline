---
source_id: 079
bibtex_key: hoque2021posesurvey
title: A Comprehensive Review on 3D Object Detection and 6D Pose Estimation With Deep Learning
year: 2021
domain_theme: Pose 6D
verified_pdf: 79_Review_Pose_6D_Hoque.pdf
char_count: 175128
---

Received July 12, 2021, accepted August 29, 2021, date of publication September 22, 2021, date of current version October 27, 2021.
Digital Object Identifier 10.1109/ACCESS.2021.3114399

A Comprehensive Review on 3D Object Detection
and 6D Pose Estimation With Deep Learning
SABERA HOQUE , MD. YASIR ARAFAT , SHUXIANG XU , ANANDA MAITI , (Member, IEEE),
AND YUCHEN WEI
School of Information and Communication Technology, University of Tasmania, Newnham, TAS 7248, Australia
Corresponding author: Sabera Hoque (sabera.hoque@utas.edu.au)

  ABSTRACT Nowadays, computer vision with 3D (dimension) object detection and 6D (degree of freedom)
  pose assumptions are widely discussed and studied in the field. In the 3D object detection process,
  classifications are centered on the object’s size, position, and direction. And in 6D pose assumptions,
  networks emphasize 3D translation and rotation vectors. Successful application of these strategies can have a
  huge impact on various machine learning-based applications, including the autonomous vehicles, the robotics
  industry, and the augmented reality sector. Although extensive work has been done on 3D object detection
  with a pose assumption from RGB images, the challenges have not been fully resolved. Our analysis provides
  a comprehensive review of the proposed contemporary techniques for complete 3D object detection and
  the recovery of 6D pose assumptions of an object. In this review research paper, we have discussed several
  proposed sophisticated methods in 3D object detection and 6D pose estimation, including some popular data
  sets, evaluation matrix, and proposed method challenges. Most importantly, this study makes an effort to offer
  some possible future directions in 3D object detection and 6D pose estimation. We accept the autonomous
  vehicle as the sample case for this detailed review. Finally, this review provides a complete overview of
  the latest in-depth learning-based research studies related to 3D object detection and 6D pose estimation
  systems and points out a comparison between some popular frameworks. To be more concise, we propose
  a detailed summary of the state-of-the-art techniques of modern deep learning-based object detection and
  pose estimation models.

  INDEX TERMS Machine learning, deep neural network, computer vision, image processing, convolutional
  neural network, 3D object detection, 6D pose estimation.

I. INTRODUCTION                                                                                challenges of retrieving 3D objects from 2D images are still
Recently with the advancement of three-dimensional (3D)                                        being explored. Moreover, estimating poses from this model
technology, the reconstruction of 3D models with pose                                          is also important for the robot industry. One of the core
assumptions has become a popular research topic. The main                                      examples in the 3D object detection and pose estimation
purpose of 3D model identification is to extract powerful                                      research sector is the autonomous vehicle, where image
features from RGB or RGBD images that can automatically                                        detection plays a vital role in recovering 3D objects from
improve the transportation system. Advanced models can                                         2D images [109]. The modern world is automatically moving
make the map smarter and reduce vehicle costs. There                                           towards an intelligent transportation system that requires
are many challenges to this research concept, such as dif-                                     the successful implementation of autonomous vehicles. The
ferentiation of perspectives, scaling, posture determination,                                  most important issue for self-driving systems is how various
illumination change, partial inclusion, adaptation detection,                                  modern technologies can be applied to enhance the efficiency
and background clutter.                                                                        of self-driving vehicles.
   Although many approaches and algorithms have been                                              The great debate in smart car systems is which one works
proposed and implemented for 2D image detection, the                                           better for object detection, the LiDAR (Light Detection and
                                                                                               Ranging) or camera. Also, it needs to be studied whether it
   The associate editor coordinating the review of this manuscript and
                                                                                               is effective to use a combination of the LiDAR and camera
approving it for publication was Claudio Cusano            .
                                                                                               systems. For example, both Waymo and Uber include LiDAR

                     This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/
143746                                                                                                                                                                VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

where Tesla only uses cameras in their smart car system. Yet        we will mainly focus on the papers that work on the
no technology has been universally accepted as a final self-        autonomous car and predicting the position of on-road cars
driving solution on the road [182].                                 or obstacles.
   LiDAR, a proven technique of measuring distance, applies            The rest of the section is organized as follows: In I-A
light pulses to determine both the distance and range of            we present the contributions of this review article of deep
the surrounding object to avoid a collision and reduce the          learning for 3D Object Detection and 6D Pose Estimation.
vehicle’s speed. The technology helps self-propelled vehicles       In I-B we have shown the difference between our review
create visual 3D maps using on-board software, sending mil-         and other existing review articles. In I-C and I-D we have
lions of pulses per second based on readings from light pulses      discussed the pervasiveness of both 3D object detection and
and providing the vehicle with information about its sur-           6D pose estimation. Finally, in I-E, we have briefly discussed
roundings. LiDAR is used in conjunction with cameras that           the paper collection process.
provide a 360-degree view of the surroundings in self-driving       A. CONTRIBUTIONS OF THIS REVIEW TO DEEP LEARNING
cars, so they are not a standalone solution in themselves.
                                                                    The purpose of this thinking is to thoroughly review the
   The camera provides images in intelligent car software           advanced essays in the 3D learning object detection literature
that can analyze with a high level of accuracy using AI             and the 6D pose assumptions from RGB and RGB-D images.
(artificial intelligence). The autopilot system uses cameras to
                                                                    It provides a brief overview of current research that is easily
provide a 360-degree view of its surroundings. The system
                                                                    comprehensible, and anyone who is interested can grasp
returns entirely visual data from the lens’s optics to on-board
                                                                    the basics of 3D object detection (3DOD) and a 6D pose
software and does not rely on the range and detection like
                                                                    aspiration (6DPE) system. Moreover, most importantly, this
LiDAR for situation analysis. With the development of NNs           review provides explicit knowledge of 3DOD and 6DPE
(Neural Network) and CV (Computer Vision) algorithms,               applications in the field of computer vision to encourage
objects can be identified to provide surrounding information
                                                                    a whole new set of novel methods and ideas. This paper
while driving. This helps the car avoid collisions, slow down
                                                                    proposes a rich survey for academics interested in research,
or brake when there is traffic, change lanes safely, and read
                                                                    the autonomous industry and the 3DOD and 6DPE fields. The
text from road or highway signs using OCR (Recognition of
                                                                    survey will provide rough guidelines and possible directions
Optical Character).                                                 for 3D object detection and 6D pose estimation methods,
   Although LiDAR has been proven to see things even in             where most of the paperwork relates to autonomous vehicles.
dangerous or foggy weather, it is not always reliable, as it is
                                                                       Altogether, the survey has several objectives, such as:
affected by wavelength stability, temperature, and detective           1) We have provided a comprehensive review for a 3D
sensitivity. This difficulty makes LiDAR technology more                  object detection and 6D pose estimation system based
expensive. Moreover, LiDAR requires more space to apply                   on deep learning.,
to cars, thus making self-driving cars look bulky and less             2) We have created an overview for advanced strategies,
attractive. On the other hand, cameras are better, easy                3) We discussed the challenges, advantages, disadvan-
to implement, and comparatively less expensive in visual                  tages of the various proposed strategies
recognition. The software requires more data processing to             4) We have identified and cited a significant number of
create images and identify objects for LiDAR data than                    innovative concepts and incoming directions in this
visual data. Finally, the camera has been implemented with                research sector
Tesla as a standalone system; however, other OEMs(original             5) We can detect vision and broaden the horizons of 3D
equipment manufacturer) believe that applying other sensors,              object detection and research DL (Deep Learning)
including radar, to detect range and distance can improve the             methods of 6D pose estimation research techniques,
performance of self-driving.                                           6) In this review, we have tried to give a brief overview
   The ultimate visual recognition system also required                   on some of the popular datasets available for computer
the accurate calculation of other vehicles pose on the                    vision.,
road. Without predicting the actual pose of other vehicles,            7) We have focused on a few popular assessment methods
an autonomous car cannot make accurate decisions on                       and created a shortlist.
whether to slow, brake or change direction. Recent state-
of-the-art RGB-based 6 DoF (Degree of Freedom) pose                 B. DIFFERENCE WITH OTHER FORMER REVIEWS
estimation frameworks can be divided into two stages [51],          To date, much work has been done on 3D Object detection
[116], [241], including the object detection with 3D rotation       (3DOD) and 6D Pose estimation (6DPE), where most of
by applying a trained framework and the estimation of 3D            them are deep learning-based. Nevertheless, the progress of
translation and 3D orientation (6D pose estimation) via             a comprehensive review on the subject is still insufficient.
relative distance estimation. Basically, the camera pose            This review sought to create a broad abstraction of modern
estimation is related to object localization, coordinates, and      research with DNN (Deep Neural Network) based 3D
orientation. It is a crucial task not only for the autonomous car   object detection 6D pose estimation systems and showed
but also for the robot and navigation technology, the medical       future directions. We can keep an eye on the paper by
sector, and AR (augmented reality) [269]. In this review,           Mukhtar et al. [173], where they reviewed 194 documents

VOLUME 9, 2021                                                                                                              143747
                                                                         S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

and worked on on-road-based vehicle detection and tracking        analyze both object identification and pose hypotheses. Their
systems for collision avoidance systems. This review is           review article mainly focuses on multiple dataset challenges
organized based on various vehicle detection processes,           such as occlusion, cluttered background, lighting conditions,
including car detection and tracking sensors.                     symmetry, texture, illustration, and appearance. The reviewed
   Sahin et al. [209], presents a comprehensive and up-to-        datasets can be used to evaluate the effectiveness of methods
date review where authors discuss object detection, examine       that work in the RGB theme modality. According to the
more than 200 documents, and pose recovery methods                review, the 3D visual understanding is a challenge for
with some popular data sets. In addition, several evaluation      complex interactions between objects in terms of perspective,
methods, open issues, and future research directions have         fully or partially chaotic internal environments, and scale
been discussed in the paper.                                      changes in different scenes.
   Sivaraman et al. [229], has also conducted a literary survey      Lateef et al., [132] and Minaee et al. [167], have provided
on the method of identifying, tracking and behaving on-           a comprehensive review of the literature of pioneering works
road aspects of self-driving vehicles. This study focuses         for semantics and example level image division using over
on the current literature related to vision and sensor-           one hundred deep learning-based segmentation methods
based vehicle detection techniques. It began with about           proposed in 2019 and 2020, respectively. Naseer et al. [177],
200 papers on environmental perception on the road from           created a review of advanced technology based on visual con-
2005. The review papers are mostly related to single vision,      cepts, including visual classification, object identification,
stereo vision, the combination of single and stereo vision        pose estimation, semantic segmentation, 3D reconstruction,
and sensor-fusion methods for vehicle tracking, detailed          salinity detection, physics-based reasoning and internal
image aircraft, 3D modelling, measurement and filtering.          visual skills.
Finally, they have called for visionary vehicle identification,      In addition, a recent comprehensive review was presented
tracking, and behavioural analysis with future research           by Rahman et al. [199], where they reviewed the latest
directions.                                                       3 DODTs (3D object detection technology). This review
   Ioannidou et al. [105], discussed the various method of        maintains some common steps, including descriptions of
deep learning architecture on different types of 3D data          some popular public datasets, several performance appraisal
and provided a classification of multiple approaches.             metrics, and 3D BB techniques. They focused on cutting-
Zhao et al. [295], provided a regular survey of DL-based          edge technology in the 3DOD sector with their significance,
object detection frameworks by reviewing a total                  contributions and future directional flaws. Zaixing et al. [89],
of 194 research papers. This review begins with a brief history   discussed several approaches for 6D pose estimation in their
of deep learning with several DL type classifications. Generic    review, including the advantages and disadvantages. A further
Object Detection strategies are discussed here, along with        up to date survey for 3D object understanding, classification,
some changes and improved detection performance concepts          identification, defining size and shape, and tracking with 3D
such as object detection, salient object detection, pedestrian    visualization and segmentation is present by Guo et al. [80].
detection, and face detection.                                       Additionally, when listing recent approaches, we ignore
   Zhou et al. [301], have conducted a review for aspect-         traditional solutions to offer up-to-date reviews. Our survey
based SFM (Structure Form Motion) method, VO (Visual              paper looks back at later high profile research publications
Odometry), and SLAM (Simultaneous Localization and                from a variety of perspectives on object detection and pose
Mapping) based methods where the methods play an                  estimation. At the end of our survey, we proposed some new
important role for support in autonomous driving systems.         insights. In short, as of June 2021, this survey summarized
In their work, they focused on multiple sensor-based methods      and discussed more than 300 high profile states of art
such as Internal Measurement Unit (IMU) sensors, LiDAR,           techniques (most of them the most recent). We have tried to
GPS (global positioning system), monocular-based methods          make this review paper exceptional and comprehensive than
(depending on the height of the camera).                          other existing reviews by presenting the graphical outlines
   One of the latest online reviews of 3D object detection        of the currently relevant papers. Also, we mentioned the
written by Liu [151], published in the science blog ‘‘Towards     future directions given by multiple authors and aim to make
Data Science,’’ has covered around 32 current state-of-the-       a decision based on them. This survey will help researchers
art mono3DOD methods as of November 2019. This review             (from start to end) who want to work with 3D object detection
did not focus on pose estimation and gave only a brief            or 6D pose assessment.
idea about it. This review is more organized (papers are
grouped into several groups) than other previous surveys          C. UNIVERSALITY AND UBIQUITY OF DEEP LEARNING IN
and gives a more accurate picture of the related article.         3D OBJECT DETECTION (3DOD) SYSTEMS
Unfortunately, there are insufficient numbers of surveys on       One of the critical and mandatory tasks for developing
DL (deep learning) - which stem from the 6D pose estimation       computer vision (CV) in the autonomous field is 3D object
system, so researchers should focus on this.                      detection. Driving without a driver, for example, requires
   Sahin et al. [210], wrote a review related to 6D pose          an authentic representation of 3D space around autonomous
hypotheses where they cover numerous research articles that       vehicles of various important categories (prediction, plan-

143748                                                                                                                   VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

ning, detection and speed control). Although LiDAR point            improperly trained models. These earlier object detection
cloud has proven successful for accurate 3D object detection,       problems were overcome with the emergence of the Deep
it is weather sensitive and expensive. Although the concept of      Neural Network (DNN) [123]. Eventually, identifying and
monocular 3D object detection (mono3DOD) from RGB or                detecting 3D objects from 2D images is a difficult task. The
RGB-D image is not a fancy concept, it still differs immensely      task becomes even more challenging as the level of depth of
from the LiDAR-based approach.                                      the 2D image during formation. Nevertheless, it is possible
    In order to detect a 3D object and guess the pose, we need      to identify 3D objects from 2D images with some efficient
to fully understand an image, rather than just knowing the          proposed methods.
classification or image localization. 3DOD is a significant
work that can be broken down into several subtasks to               D. UNIVERSALITY AND UBIQUITY OF DEEP LEARNING IN
make important steps for accurate knowledge of images               6D POSE ESTIMATION SYSTEMS
and videos, such as some other notable applications are             To detect 3D objects from monocular 2D RGB images,
classification [110], [123], human behavior analysis [26],          we need to create a 3D oriented BB (bounding box), while
pedestrian detection [53], skeleton detection [121], face           3D reasoning from a single 2D input is a complex and
recognition [299] and autonomous driving [33].                      difficult task. In the autonomous sector, other than object
    There are some significant hurdles in achieving the             detection, pose estimation is a complex job that needs to
identification and object localization tasks such as occlusions,    be done. It is easier to predict the 6D pose in RGBD
chaotic environment, lighting conditions, size differences          images than in RGB images because the 6D pose is a
and viewpoints. Due to the notable impact of accurate               complex combination of 3D rotation of an object (raw, pitch,
object detection in robotic and autonomous fields, more             yaw) and 3D coordinates (X, Y, Z) at the camera focal
efforts are being made to identify a (3D / 2D) object more          point [152]. One significant step in identifying the 3D object
accurately with intense care and attention [76], [77], [202],       and estimating the 6D pose of any object from the image
[203]. 3D object identification can be divided into object          can be divided into egocentric and allocentric positions [119].
localization (specific content located in a test image) and         In the context of autonomous driving, the orientation related
object classification (category by object). Conventional 3D         to the camera is called egocentric, and the orientation related
object detection models can be divided into three main              to an object is called allocentric. Also, full 6D pose estimation
categories: informative zone selection, feature extraction, and     is required for successful implementation of AR (augmented
classification.                                                     reality) [163], robotics grasp [39], autopilot [33], and so on.
    Any given image can have multiple objects in different             Recent improvements to visual depth sensors and the avail-
positions of the image with different aspect ratios or sizes;       ability of low-cost depth data have significantly improved
It is best to handle the whole image with a different               object pose estimation. In addition, successful implementa-
image sliding window. Strategies attempt to identify all            tion of 6D pose estimation method to solve some problems
possible positions and orientations of objects. Due to a            such as variability of viewpoint, similar objects, symmetrical
large number of test windows, the process is comparatively          property, occlusion and cluttered environment; All have
expensive and generates additional windows. Moreover,               been overcome due to the availability of RGB-D sensors
if some stable sliding window template is applied, it will          and the recent improvement of the Convolutional Neural
create unsatisfactory areas.                                        Networks (CNN).
    Some important steps to detect object:                             Typically, the recovery of a 6D pose estimation depends
    • Feature extraction: This step helps to identify diverse       on two factors, the familiar instances and the raw/unknown
       objects and reveal features with meaningful and strong       instance of an object. Moreover, some challenges such as
       representations about complex cells as neurons in the        shape mood, target domain, shift distribution between several
       human brain [157] such as HOG [45], Haar-like [145]          sources, and classification of objects prevent calculating the
       and SIFT [157]. However, due to the varied lighting          pose accurately. These challenges have been widely studied
       conditions, it is challenging to accurately describe all     in recent years because of their significance in augmented
       kinds of things.                                             reality (AR) [163], robotics [251], and autonomous vehi-
    • Classification: A classifier has to differentiate the         cles [74]. In the robotics and automated car industries,
       target object from different types to create recognition     accurate object detection, the successful application of self-
       of more semantic, categorized, and informative ocular        management of objects (robotic groups), and the assumption
       objects. The common classifier used for classifications      of 6D poses by robots play an important role in advancing the
       is SVM [41], AdaBoost [68], DPM (Deformable Part-            challenge of autonomous manipulation.
       bas ed Model) [64] (more flexible for low level features).
A state of the art results has been achieved in the Pascal-         E. THE PAPER COLLECTION PROCESS
VOC [62] object identification competition by applying the          Google Scholar is one of the primary sources of our
concept of describing local features. However, there were           paper collection. Also, the well-known Database ‘‘Web
some issues with this model, such as inaccurate bounding            of Science’’ is another notable source through which we
boxes, inefficient and unwanted low-level descriptors, and          have introduced and collected a number of related papers.

VOLUME 9, 2021                                                                                                                143749
                                                                         S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

In addition, we should mention ‘‘Wikipedia,’’ which is an         teaching theories to generate numerical or symbolic data from
authentic source of information and documentation. YouTube        those images [108], [120], [170]. The CV process is gradually
plays a vital role in understanding any new concept in            seeing new revolutionary concepts related to object detection
this case. UTAS (University of Tasmania) Open Access              where the main challenges are image processing and machine
Repository [183], [184] is a great choice for collecting recent   vision [193].
papers.                                                              Moreover, a self-driving vehicle is a notable example
   The keywords we have used for searching references             where ANN and CV have been widely used. However, it is a
include deep learning (DL), deep neural networks (DNN),           big challenge for autonomous vehicles to accurately estimate
Convolutional neural network (CNN), object localization,          the position of a 3D object from a 2D image. Although much
image processing, autonomous vehicle (AV), 2D/3D object           progress has been made in identifying 2D objects from an
detection, 2D/3D bounding box (BB), 2D/3D object pro-             image or video, identifying a 3D object and determining the
posal, 2D/3D object identification, and 6D pose estimation.       3D properties of an object from a single image is still a
In addition, ACM Digital Library, IEEE Explore, Scopus,           challenging problem.
ScienceDirect is a collection of the best research databases         Typical Tasks of Computer Vision: Content-based image
that make our survey resourceful. Last but not least,             retrieval [230], Pose estimation [269], Optical character
Researchgate is a legitimate source of information and paper.     recognition (OCR) [165], 2D code reading [206], Automatic
Most importantly, we have gone through some highly ranked         face recognition, Recognition Features [67], Egomotion
conferences such as CVPR, ICCV, NIPS, AAI, ICLR, ECCV,            [16], [303], Optical flow [10]. Scene reconstruction [233],
ICRA, ICML, IV, IROS, ACM, ITSC, ICIP, TPAMI, IRS,                Image restoration [7], Image acquisition [46], Feature
WACV, ECCV, ACCV, and Sensors.                                    extraction [46], Detection/segmentation [155], High-level
                                                                  processing [46], Decision making [46].
F. OUTLINE OF THE REVIEW
This paper proposes a comprehensive study reviewing the           B. ARTIFICIAL NEURAL NETWORK (ANN)
current methods of object pose detection and recovery. Our        The function of ANN is almost the same as that of
contributions are as follows:                                     the human brain, as knowledge is acquired through the
  • Discussed computer vision and deep learning networks,         network through a learning process from near it and stored
     autonomous car and its challenges in section II and III      using some synaptic weight neurons. To achieve the final
     briefly.                                                     design goal and change the synaptic weight of the network,
  • The datasets used for the 3D object detection and 6D          NN has implemented a learning process known as a learning
     pose estimation method were observed to identify its         algorithm. Nowadays, ANN has been applied to multiple
     challenges, which are represented in Table 1.                jobs, including computer vision, image recognition, speech
  • We Discussed the range of state-of-the-art (SOTA)             recognition, social network filtering, machine translation,
     technology from 3D BB detectors to full 6D pose              diagnostics, and video games [72], [178].
     guessers in IV section.
  • In Table 3 where some of the SOTA 3D object detection         C. DEEP NEURAL NETWORK (DNN)
     methods are compared and in Table 5 some SOTA 6D             Deep Neural Network (DNN), a section of a machine
     poses estimation methods are compared.                       learning (ML) where the machine has to predict any output,
  • The Table 4 represents the 3D Object Detection Paper          can be supervised, semi-supervised or unsupervised [219].
     Collection and this table is represented graphically in      Since traditional ML techniques cannot process natural
     Figure 2. The significant amount of paper collection on      data in their raw form, DL (Deep Learning), an advanced
     6D pose estimation in recent years is shown in Table 6       DNN technique, applies multiple layers to reveal high-level
     and this table is represented figuratively in Figure 3.      features from the raw data. For example, in image processing,
  • Open issues are discussed to identify potential future        where the lower layers of the DL model can recognize the
     research directions in VI.                                   edges only, the upper layers can detect a certain number of
  • Finally, section VII sums up the present situation of the     letters or objects or features of the object [239].
     field and concludes the review work.                            Eventually, DL processed unsorted/sorted, labelled or
                                                                  unlabelled data and construct a pattern to make a better
II. COMPUTER VISION AND DEEP LEARNING                             prediction [120], [123], [176]. Though DL was popular
A. COMPUTER VISION                                                since 1980-90s, offered the concept of the back-propagation
Computer Vision (CV) in artificial intelligence trains com-       classifier [207]; nonetheless, it soon lost its popularity due
puters to interpret and understand the visual world, working      to over fitting, scarcity of big data, and poor computation
with technologies where computers can achieve a high-level        capacity as compared to other ML tools.
understanding of any digital image or video.                         The popularity of Deep learning algorithm has increased
  The CV system is a method of taking, processing,                since 2006 [94] with the advancement in speech recog-
exploring and mastering digital images and using models           nition [93] application. Convolutional Neural Networks
built with the help of geometry, statistics, physics and some     (CNN), the popular DL framework, which is applied on

143750                                                                                                                   VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

multiple sectors such as Natural Language Processing (NLP),        four offset values. The main problem with this classifier is
Computer Vision, Speech Recognition, Audio Recognition,            time.
Machine Translation, Social Network Filtering, Bioinformat-
ics, Medical image analysis, and much more [171].                  3) FAST RCNN
                                                                   The algorithm previously proposed to create a quick object
1) CONVOLUTIONAL NEURAL NETWORK (CNN)                              recognition classification updated some of the errors of
The Convolutional Neural Network (CNN) has a deep feed-            R-CNN and renamed as Fast R-CNN [76]. This method is
forward architecture and remarkable ability to generalize to       almost the same as the R-CNN classification. Since it uses
better networks with fully connected layers. CNN has largely       CNN once, there is a significant gain over time. The training
applied to image analysis, especially pattern recognition,         time is about 8.75 hours, and the estimated time is about
which can also be employed to solve other data analysis            2.3 seconds.
problems, such as classification problems. CNN is a deep
learning network developed for image and video processing          4) FASTER RCNN
that has made significant progress since 2010 and is now           Both of the above algorithms (R-CNN and Fast R-CNN) use
widely used worldwide.                                             SS to determine region proposals. SS [253] is a slow and time-
   The two most notable qualities as classified composition        consuming process that over-segmenting the image affects
and the ability to extract powerful features from an image         network performance. Therefore, Shaoqing Ren et al. [203]
prove that CNN is one of the most powerful object                  proposed an object identification algorithm that removes
detection classifieds. Several important CNN architectures         the SS algorithm and allows the network to learn region
have been proposed times for image processing such                 recommendations. After the predicted regions are resized
as ImageNet [48], AlexNet [123], ConvNet [124], [134]              using the ROI(Region of Interest) pooling layer, which is
LeNet [243], VGGNet [228], ResNet [87], ZFNet [284],               then used to classify the image in the proposed region
GoogLeNet [243], GPU (Graphics Processing Unit) proces-            and predict the IoU (Intersection-over-Union) ratio of the
sor large-scale distributed clusters [47], and OverFeat [218].     bounding boxes.
   On top of that, CNN is a powerful algorithm that is widely
used for image classification and object detection [123],          5) SINGLE SHOT MultiBox DETECTOR (SSD)
[284]. Because of the notable advantages, CNN has been             Liu et al. [153] proposed SSD (Single Shot Multibox Detec-
widely applied in many research fields including image             tor), a single shot detector for multiple segments, applies an
super-resolution reconstruction [179], [285], image classifi-      additional small conventional filter to maps that are faster
cation, image retrieval [110], face recognition [299], pedes-      and significantly more accurate than previous single shot
trian detection [249], [272], [294] and video analysis [228],      detectors like YOLO.
[270], [284], car detection [33], and pose estimation [296].
   Most importantly, CNN can be adequately trained that            6) MASK RCNN
does not suffer from over fitting and is easy to apply to          He et al. [86] presents the concept of flexible structures
large networks [123]. However, CNN cannot provide accurate         called Mask R-CNN for object instance segmentation.
results when the length of the output level is variable and        This method effectively recognizes objects from an image
the presence of objects of interest is not fixed. Therefore,       while creates a high-quality segmentation mask for each
more sophisticated algorithms such as R-CNN, Fast R-CNN            instance at the same time. Mask R-CNN is a practical
and YOLO have been developed to solve advanced image               extension of Faster R-CNN, where an additional branch
processing problems.                                               is added to predict an object mask parallel to an existing
                                                                   branch. Moreover, this method is a slightly improved version
2) REGION BASED CONVOLUTIONAL                                      of R-CNN that runs at 5fps and can adapt quickly to
NEURAL NETWORK (RCNN)                                              predict human posture. Also, Mask R-CNN has won the
Girshick [76] proposed a method where a large number of            COC 2016 Challenge by overcoming three key issues:
regions were selected, and the Selective Search (SS) [253]         Instant Segmentation, Bounding-Box Object Identification,
method was applied to select only 2000 regions from an             and Individual Keypoint Identification.
image, which he named the region proposals.
   Since each region of the image is applied to CNN individu-      7) YOLO
ally, the training time is about 84 hours, and the forecast time   Redmon et al. [202] Proposed a novel object detection tech-
is about 47 seconds. As a result, the process becomes time-        nique called YOLO (You Only Look Once), where the clas-
consuming because it has to classify 2000 region propositions      sifier does not process the whole image; Instead, it focuses
for each image. Here, the CNN functions as a feature extractor     partly on the image with a high probability of having the
and the revealed features are processed through an SVM [41]        object in that part. This single convolutional network is faster
classifier to distribute the object inside the region proposal.    than existing object detection algorithms. However, above all
Additionally, to anticipate the region proposals and increase      advantages, the YOLO algorithm struggles to detect small
the bounding box’s precision quality, the algorithm creates        objects within the image. For example, the spatial limitations

VOLUME 9, 2021                                                                                                              143751
                                                                        S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

of algorithms can make it difficult to identify flocks of        generates outputs and sends commands to the vehicle actuator
birds. Some other notable DL structures are: RefineDet [287],    responsible for steering, braking and control acceleration.
Retina-Net [147], Deformable convolutional networks [44],        AV can be identified as a complete package of hard-
Cascade R-CNN [21], 3D-RCNN [128], Libra R-CNN [186].            coded rules, a complex algorithm and efficient predictive
                                                                 models, helping sophisticated software to run on the road
8) MESH R-CNN                                                    smoothly [73], [192], [245].
Facebook introduced a novel RCNN method in artificial               To date, autonomous vehicles are equipped with two types
intelligence called Mesh R-CNN that can convert 2D objects       of sensor such as active sensor: LiDAR [138], [139], [279],
to 3D shapes and mesh [267]. Facebook has highlighted            radar [277] and passive sensors: Single/Stereo cameras [32],
its latest advances that can identify complex issues. This       [172], and their fused systems [33], [107], short-range sensor
study has applied in-deep learning to understand the 3D          (Ultrasonic sensors) [122]. Veli et al. [104] made lots of
shapes of complex objects and novel architectures such as        progress in sensor technology and GNSS (Global Navigation
Bounding Box, 3D Voxel Pattern, Point Cloud and Message          Satellite Systems).
for prediction and localization. Mesh R-CNN can effectively         A research team from the Massachusetts Institute of
detect and classify objects in 3D form from chaotic 2D           Technology (MIT) [84] announced in May 2018 that they
images and occluded objects and ultimately estimate their full   had successfully built a driverless car that could successfully
3D shape.                                                        navigate unmapped roads with a novel system known as
                                                                 MapLite [40]. This application enables the driverless car to
                                                                 drive on a completely new road without using pre-loaded 3D
                                                                 maps. The basic idea is to combine the vehicle’s position
                                                                 with sensors that monitor the surrounding conditions, and
                                                                 OpenStreetMap (OSM) is used to detect the GPS of a
                                                                 vehicle [40].
                                                                    Also, an AV has been divided into 5 levels such as
                                                                 level 1 - requires driver support, level 2 - partial automation
                                                                 phase, level 3 - limited driver support, level 4 - higher
                                                                 automation and level 5 - fully automated [225], [84] [190].
                                                                 At present, level 3 autopilot is available on the road, as Level
                                                                 4 and Level 5 autonomy require large-scale neural network
                                                                 training and visual recognition, including accurate pose
                                                                 estimations. Multiple companies produce intelligent vehicles
                                                                 and test them to drive autonomously in certain situations,
                                                                 such as Tesla Autopilot, Waymo, Uber, Volvo, Google, BMW,
                                                                 Mercedes Benz, Nissan and General Motors. However, they
                                                                 are still in the testing phase and unable to operate without
                                                                 assistance.

                                                                 A. TECHNICAL AND SOCIAL CHALLENGES OF
                                                                 AUTONOMOUS VEHICLES
                                                                 Although the concept of autonomous or self-propelled
                                                                 vehicles has come a long way in recent years and numerous
III. AUTONOMOUS VEHICLE (AV)                                     studies have been done in this sector, this technology is still
An autonomous vehicle (AV) is a combination of some              not flawless. Lawmakers and consumers still feel confused
actuators, sensors, complex analytical algorithms, machine       and anxious about implementing self-driving cars and feel
learning methods, and high-speed processors that are needed      insecure and uncertain about the autonomous vehicle’s
to implement complex software. Self-driving vehicles create      ability to move freely. So self-propelled cars are still in
and maintain a map called Simultaneous Localization and          the experimental stage, and more research is needed to
Mapping (SLAM) of their surroundings by multiple sensors         perform them properly. One of the significant challenges
placed in different parts. Such as LiDAR or radar measures       of autonomous vehicles is accurately estimating the exact
distances of other vehicles or obstacles, detect road edges.     position and orientation of nearby vehicles. The five core
In addition, one or more cameras mounted on autonomous           reasons are classified as why the AV still are not on the roads
vehicles can detect traffic lights, road signs, lane signs,      are listed in below:
vehicles, obstacles and pedestrians [52].                           Sensors: An autonomous vehicle faces various challenges
   During parking, ultrasonic sensors placed on wheels to        for smooth automation systems such as proper vehicle
detect obstructions and other vehicles. Advanced complex         navigation system, GPS, environmental perception, LiDAR
software [131] then processes all these sensory inputs,          and radar, visual perception, speed and direct perception and

143752                                                                                                                  VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

a vehicle control system [192], [293]. Furthermore, to be           2) Feature extraction: To identify different objects,
qualified as perfect autonomous vehicles, these sensors need           we need to figure out visual features that can represent
to work in all weather conditions anywhere on the earth.               a semantic and robust.
Undoubtedly, the critical issue for driverless vehicles is that     3) Classification: A classifier needs to differentiate a
there should be a control system capable of automatically              target object from all other categories and further
analyzing sensor data and making accurate estimates of                 classify the presentation.
vehicle postures, obstacles, pedestrians and road signs [306].
   Machine learning Algorithm: At the moment, there               A. 3D OBJECT RECOGNITION
is no widely approved and authorised ML algorithm to              Object recognition is one of the primary pillars of a
ensure that they are 100 % error-free, safe and secure for        computer’s vision and is sometimes confused with the
use in any driverless vehicle. The most popular algorithm         problem of object classification/shape retrieval. 3D object
applied to current driverless vehicles is SLAM, which             recognition methods can be divided into two main categories
integrates data from various sensing components and uses          such as voting methods, Hough transform [6], and geometric
offline maps [266]. WAYMO has improved the performance            hashing [130] and the correspondence based method, spin
of the algorithm SLAM and named DATMO (Detection                  images [112], local feature histograms [90], 3D shape and
and Tracking of Moving Objects), which can handle any             harmonic shape context [69].
curbs, including vehicles and pedestrians. Zhang et al. [291],       David et al. [156] developed an object recognition system
proposed a concept that collaborated with the existing Visual     using local image features in cluttered real-world scenarios.
odometry (VO) system such as SLAM and ORB-SLAM2 (                 Cordelia et al. Schmid et al. [214], has shown that recogni-
an updated version of the SLAM) [174].                            tion of successful objects can often be achieved by applying a
   The open road: When the AV drives on new roads,                sample local image descriptor to a large number of repetitive
it should identify things that did not come before in the         locations. Papazov et al. [187] proposed the recognition of a
training process and may be subject to software updates. As a     3D object, especially for noisy and scattered data in cluttered
result, it would be not easy to ensure that the system is as      and occluded environments. This proposed concept applies
secure as its former version.                                     a combination of strong geometric descriptors, a hashing
   Regulation To date, adequate standards and regulations for     technique and a sampling technique - RANSAC [65].
autonomous systems do not exist. There have been numerous
high-profile accidents involving Tesla’s current automobiles,     B. 3D OBJECT DETECTION FROM RGB AND RGB-D IMAGE
as well as other automotive and autonomous vehicles [9].          3D object detection is a significant key part of the visual
   Social acceptability: Applying an automatic car on the         perception system of robotic and autonomous technologies.
road is not only a problem for those who want to buy and use      It has many applications with different category some of them
a driver-less vehicle, but also for others who share the road     described in FIGURE 1.
with them [9].

IV. LITERATURE REVIEWS
An essential part of computer vision is the identification of
objects from images or videos. Object detection helps in
pose estimation, vehicle detection, pedestrian and other curb
detection. Previously, the image was processed and classified
using traditional machine learning (ML) algorithms such as
colour histogram [220], SVM (Support Vector Machine) [41],
logistic regression [202]. However, there are some differences
between the recent object detection algorithms (CNN, R-
CNN, YOLO) and traditional ML classification algorithms
(SVM, logistic regression).
  The definition of object identification problem determines
where objects are located in a given image is called object       FIGURE 1. The application domain of object detection.
localization, and what class each object belongs to is called
object classification. Thus, the traditional thematic object         In generic object detection, object instances are identified
detection model’s pipeline is divided into three stages           by applying predefined sections/categories. It has some chal-
such as:                                                          lenges such as the immense range of inner-class variations
   1) Informative region selection: Different objects can         and the large-scale object categories [150]. Salient object
      appear in any position of the image and have different      detection detects the most significant and notable object
      aspect ratios or sizes, so scanning the entire image with   in an image, and then it segments the whole area of that
      a multi-scale sliding window is a natural choice.           object [12].

VOLUME 9, 2021                                                                                                            143753
                                                                         S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

1) FEATURE EXTRACTION, SEGMENTATION AND MATCHING                  mirrors) and defines a 3D shape for each 3D model.
Rapid and accurate image segmentation with feature extrac-        Zhou et al., [304] has built the CenterNet framework, which
tion is the primary task of the computer vision field.            is simpler, faster, and more accurate than traditional BB
Lowe et al. [156] proposed SIFT (Scale Invariant Feature          detectors and poses estimators.
Transform), an object recognition system for image scaling,
translation, matching and rotation, and a partial constant for    3) 3D PROJECTIONS OF THE 3D BOUNDING BOX VERTICES
illumination changes, including 3D projection. The images         Chen et al., [34] proposed 3DOP (3D Object Proposal)
here have been converted to a wide collection of local feature    for accurate object class identification in the context of
vectors and can generate approximately 1000 SIFT keys             autonomous driving. 3DOP produced several sets of 3D
in 1k ms during each image count by applying classification.      candidate boxes to identify almost every object in 3D space.
Although occlusion may be present in the image, SIFT can          This method has featured object size, ground plane, different
provide a high level of accuracy.                                 depths, spaces, the density of points inside the box, visibility
   Kang et al., [114] Created a structure called DaSNet-          and soil distance.
V2 that matches identification, category, localization, and          Mono 3D (Monocular 3D Object Detection) [32] uses
object instances. A method capable of achieving real-time         ground planes and some segmentation features to generate
performance by adopting PWP 3D (count per pixel) and              3D proposals from monocular images in the context of
applying the region-based simultaneous strategy of 2D             autonomous driving. In addition, both 3DOP and Mono3D
partitioning using the NVIDIA CUDA framework is largely           methods applied some common hand-crafted features. This
developing parallel algorithms [194]. Fu et al. [70] introduced   technique applies several intuitive potentials to each candi-
DORN (Deep Ordinary Regression Network), a multi-                 date box expected in the image plane encoding synthetic
scale network framework that achieves a spacing-increasing        segmentation, relevant information, size and location pre-
discretion (SID) strategy to rebuild depth and depth networks     requisites, and ideal object sizes. Also, the S-SVM [111],
to reduce the complexity of existing feature maps.                structured SVM [252], parallel cutting plane [228] and IoU
                                                                  has been implemented with a comprehensive search model.
                                                                     The proposed DSS (Deep Sliding Shapes) [236] is a 3D
2) SHAPE VARIATION                                                convergent formulation that takes 3D volumetric views as
Xiang and Dollar offered 3DVP (3D Voxel pattern), which           input from an RGB-D image and then outputs a 3D object
uses ACF (Aggregate Channel Features) detectors to find out       bounding boxes. In addition, this method proposes the first
the basic features of each object such as shape, appearance,      3D Region Proposal Network (RPN) to learn objects from
aspect and curbs [54], [271]. In addition, the 3D pose of a       geometric shapes and the first Joint Object Recognition
vehicle can be accurately localized from the context of this      Network (ORN) to extract geometric features in colour
method and can detect other vehicles and guess the pose [74].     properties in 2D.
   Novotny et al., [181] have created the C3DPO (Canonical           Ding et al., [49] proposed a fancy wire-frame model called
3D Pose) Network for non-rigid structure motion where no          the CPO (Cross Projection Optimization Method) that can
training images and messes are available. It has partially        detect both 3D pose and shape estimation of a vehicle for
reconstructed a 3D object from a monochromatic RGB image          an autonomous vehicle. The CPO method applies a simple
to change perspectives and distort the object. It has also        wire-frame model combined with the Hierarchical Wire-
emphasized the mandatory presence of certain canonical-           frame Constant (HWC) method instead of bounding box
ization functions of reconstituted size and shape. The input      annotation to shape detection for 3D pose and accurate 3D
depth proposes objects pose according to the classification of    localization [33].
convex hulls that align the clusters of convex sections drawn        The solution provided is primarily based on local prop-
from the images. This is an example of a highly efficient         erties, especially for matching objects in a 2D image of a
size identification pipeline that uses the CHAL (convex hull      rigid 3D object [79]. This method creates an accurate 3D
alignment) algorithm for hypothesis generation and is used to     model of the object with the locations of its features and
identify objects in complex scenes with multiple objects [42].    then places it in an image to identify new features. Finally,
   Qian et al., [196] presented a method for evaluating           the position, orientation, and shape of the virtual object are
individual 3D sizes, where there was a balance and robustness     defined concerning the object’s coordinates.
between the accuracy and efficiency of the conventional stage        Rad [198] has created a framework where a total of 8
recovery method, significant measurement limits and high-         corners of the bounding box are applied to the multiple-input
frequency fringe patterns. Chabot [28] made a framework           image called BB8. This method is trained to predict their
called Deep MANTA for 3D object detection based on a              poses in the form of 2D projections of the corners of their
single-dimensional image in an end-to-end fashion network,        3D bounding boxes and calculates 3D poses from this 2D-3D
determining the object class, 2D region proposal generation,      correspondence with a PNP algorithm [136].
2D location, orientation, dimension and 3D position. This            Another strategy called Mono3OD [227] where a single
model has implemented a 3D vehicle dataset featuring 3D           RGB image uniquely transformed to reduce object detection
mesh with real size to match vehicle parts (wheels, headlights,   and increase the credit count for 3D BBs. Li [142]

143754                                                                                                                   VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

suggested RTM3D (Real-time Monocular 3D Detection),              framework creates efficient 3D candidate boxes from a 3D
the first real-time 3D identification method for autonomous      point cloud BEV (Bird’s Eye View) [154] image, and the
driving, predicting the nine point-of-view of the 3D BB          main goal of this method is to identify 3D objects using
in place of the image and using 3D and 2D perspective            both LiDAR and image data. Current LiDAR-based methods
geometry to restore orientation, location and dimensions in      set 3D windows in 3D Voxel Grid [58], [260] or apply
3D space.                                                        convolutional networks [139] to front viewpoint maps.
   Liu [150] has claimed a deep fitting degree scoring network      On the other hand, a hybrid method has introduced that
for mono 3DOD, which focuses on the active fitting degree        combined both LiDAR and camera data for 2D detection
among proposals and objects. It is discrete from other           to get accurate results [59], [78]. Qi et al., [195] offered a
existing monocular frameworks by attaining localization          fancy concept called ‘‘Frastum PointNets’’ based on RGB-D
by computing the visible degree of calculation among the         data in a point cloud and expects a semantic class for
3D project proposals and the object. A concept named             each point in that point cloud. A method named PV-RCNN
FQNet, [150], can assume the 3D IoU (Intersection over           provides accurate 3D object detection from point clouds
Union) among the 3D proposals and the object.                    that deeply integrates 3D visualization with point-to-point
   Zhang et al., [291] proposed a framework for 3D               set-based abstraction with a 3D visual convoluted neural
object detection by determining object class, 2D region          network and multiple receiving fields [221]. Finally, a novel
proposition production, 2D position, position, dimension         method called SAANet (Special Adaptive Alignment) uses an
and 3D positioning based on a single image in an end-to-         ‘‘SAA’’ module that addresses fusion-based deep structures
end fashion network. Furthermore, Bao et al. [8], recently       that combine clouds and images for 3D object detection with
introduced Mono-Fenet, a compelling feature enhancement          complements cloud properties and image properties [31].
method for the 3D object detection, which includes the
ROI Mean Pooling layer, the PointFE network, and feature         5) SPEED / ACCURACY TRADE-OFF
enhancement networks using 3D-NMS and exclusive RGB              Huang et al., [103] introduced a process that helps deter-
imagery.                                                         mine the speed and accuracy of the calculation and also
   The full 3D poses and dimensions of an object from            recommend which method is better suited for a specific
a 2D BB by applying some restrictions to calculate the           application. Shrivastava et al., [224] proposed a TDM (top-
orientation and volume of the object using DCNN, where           down modulation) approach to include image quality for a
the novel DCNN method known as MultiBin regression is            ConvNet architecture such as VGGNet [228], ResNet [87],
used to estimate the orientation of the object [172]. SS3D,      and Inception-Resnet [242]. Song [236] proposed Deep
a single-phase monocular 3D object detector where the            Sliding Shapes (DSS) that convert an RGB-D image into
3D representation is returned by a representative and uses       a point cloud and then slides a 3D detection window into
for the geometric shapes of the 3D box with autonomous           3D space. Luo [158] made a concept that identifies 3D
driving [113].                                                   objects and accurately predicts the position, size, orientation
   Hu et al., [102], introduced a complete 3D vehicle            and division of objects in 3D space at very fast speeds.
bounding box tracking information method from exclusive          Li [140] has come up with an idea called GS3D, a 3DOD
videos and a method for dealing with 3D vehicle detection        method based on an RGB (single) image in autonomous
guesswork. A new pipeline based on LSTM [254] is designed        driving.
to collect large-sized 3D trajectories from real-world driving
environments and track 3D vehicles within 30 meters.             6) OBJECT DETECTION BY KEY POINT ESTIMATION.
The method called M3D-RPN implemented exclusive 3D               The most famous classifier that detected an object using key-
identification and 3D zone proposal networks and lifting the     point inference (identifies the object as a point to the key)
geometric relationship of 2D and 3D perspectives, including      is Cornernet [133], ExtremeNet [305], and CenterNet [304].
3D boxes [15].                                                   In CornerNet, the corners of 2D BB are used as semantic
                                                                 key points. ExtremeNet, on the other hand, highlights all
4) 3D OBJECT DETECTION IN POINT CLOUD                            points, including the top, left, bottom, right, and centre of the
Scientists proposed a method for identifying free-form           bounding box. Compared to these classifiers, the Centernet is
3-dimensional objects in point clouds with global represen-      much faster, which only chooses the object’s centre.
tations [56]. The basic idea of the model is to create a
universal approach statement based on the point pair factor.     V. LITERATURE REVIEW OF 6D/6DoF (DEGREE OF
Free-form objects in 3D datasets can be achieved by a            FREEDOM) POSE ESTIMATION
number of sensors, such as a laser scan, a TOF (Time of          In the computer vision sector, guessing a 6D pose of an
Flight) camera, which has been widely disseminated from a        object is a significant problem that needs to detect both 3D
computer perspective [25], [160].                                orientation and 3D position of an object in the case of the
   Chen et al., [33] introduced accurate 3D object detection     camera centred coordinates [116]. In short, the three factors
for individual behaviour, known as Multi-View 3D Network         for the 6D pose estimation are the critical role of rotating left
(MV3D), which works with multimodal datasets. MV3D               and right on the X-axis (roll) side as well as on the Y-axis

VOLUME 9, 2021                                                                                                             143755
                                                                                       S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

TABLE 1. Data-sets used for multiple 3D object detection and pose estimation method.

(pitch) and tilting backwards on the Z-axis (Yaw). Thus,                    A. 6D POSE ESTIMATION DIRECTLY FROM RGB IMAGES
these features encourage concentration on the recovery of                   Wu et al., [269] proposed an algorithm named 6D-VNet,
vehicle posture and size estimates to enhance the intelligence              and won the first place in the ‘‘Apolloscape Challenge 3D
of the intelligent transport system and the robotic sector.                 Car Instance’’ competition. It is an abstract structure for
Therefore, the conventional states of industrial techniques                 autonomous vehicles assuming 6 DOF object poses that can
of 6D pose estimation are discussed here in the context of                  detect all aspects of traffic in a single RGB image while
the autonomous car.                                                         rotating vectors and 3D translation. The basic technique of

143756                                                                                                                                 VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

TABLE 2. Evaluation metrics: Different types of evaluation metrics to identify and measure the performance of proposed classifiers.

this method is to control the 6D position of the vehicle using                 applies to the collection of small objects and objects with
the outputs from the RPN (Region Proposal Network) [77]                        many conceptual and practical advantages.
and 2D object detection network (Mask R-CNN) [86] that can                        Inspired by BB8 [198] method Zhang et al., [289] re-
learn both rotation and translation by outlining a loss function               imposed the coordinates of the image and applied the
model.                                                                         Perspective-n-Point (PNP) [136] algorithm without any post-
   Brachmann et al., [13] created a template-based model                       refinement. Similar to recent work, the method uses 2D BB to
for calculating 6D pose for a specific object from a single                    calculate the coordinate regression of images based on their
RGB image. The algorithm optimizes the power following                         centres, focusing on the gap between image classification
the RANSAC concept for a large and uninterrupted 6D pose                       and pose estimates [248]. Deep-6DPose is an end-to-end
space. The technical feasibility of classification is using a new              deep learning solution, which finds objects and compresses
composite dense 3D object coordinate form, including object                    them and retrieves instances of 6D objects from single RGB
class labelling. Kehl et al., [116] developed SSD-6D, a CNN                    images [50]. It consists of two main components, such as RPN
method to detect the 3D object and accurately guess the 6D                     and a mask R-CNN, including Lie algebra.
pose from an RGB image. It is a unique detector method                            Billings et al., [11] has developed a new proposal to
for relevant training on synthetic model information, which                    predict 6D object poses from monocular RGB images

VOLUME 9, 2021                                                                                                                        143757
                                                                                    S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

TABLE 3. Advantages and disadvantages of some state-of-the-art 3D object detection techniques.

TABLE 4. 3D object detection paper collection.

by applying the CNN pipeline with the ROI proposal.                         6-D category level pose estimation, two-level BB-based
It predicts the presence of intermediate outlines for 3D                    alternative methods have been developed that directly output
objects, 3D orientation and 3D translation vectors. For the                 the 6D pose without the use of any PNP but consist of

143758                                                                                                                              VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

ResNet (Residual Neural Network), RPN, and FCN (Fully               the object’s posture. It has mixed colour and depth data from
Convolutional Network) [149].                                       the RGB-D image and then integrates repetitive refinement
                                                                    methods into neural network architectures.
B. POSE FROM DEPTH / POINT CLOUD METHOD                                Li et al., [141] applied CNN to process the depth image
Mitash et al., [168] advocated a concept for efficient object       as an additional image channel. However, the built-in 3D
6D pose estimation in cluttered scenes, where the Cartesian         structure in the depth channel was neglected. In contrast,
product of the candidate’s post for interactive objects is used     the geometric features of the dense fusion method convert
to identify the best view and create an efficient search, and the   pixels into sectional depths into 3D point clouds by applying
candidate post clusters for each object. The MCTS (Monte            built-in cameras. The proposed DPOD (Dense Pose Object
Carlo Tree Search) technique is applied to conduct tradeoffs        Detector) applies PNP and RANSAC to compute an input
in fine-tuning and explore new instances.                           image and a map of dense multi-class 2D / 3D correspon-
   Xiang et al., [276] has created a generic structure called       dence between available 3D models [282].
POSNN that calculates the 3D translation of an object in the
image and predicts its distance from the camera. Furthermore,       D. INSTANCE-LEVEL 6 DoF POSE ESTIMATION
this method reduces the ShapeMatch-Loss function and                Collet et al., [38] created 3D object metric models using local
enables POSNN to handle symmetrical objects where the               descriptors of different images. Each model was optimized
VGG16 backbone is used to extract features.                         to easily fit a sequential training image, resulting in the
   The PointPoseNet classifier for 6DoF objects gives the           best possible alignment between the 3D model and the
idea of inference of rigid objects using deep learning in           original object. It combines the well-known RANSAC [65]
point clouds. A point-to-point correspondence assignment            and Mean Shift algorithm [36] to register multiple instances
is performed with a joint classification and segmentation           of each object that can successfully guess the 6-DOF pose
within a point cloud system [83]. Capellen [27] suggested that      for any complex and chaotic scene. In addition, it can handle
ConvPoseCNN has evolved from the concept of PoseCNN                 randomly complex non-planning objects, powerful to handle
but can avoid cutting individual objects. Instead, it offers        outliers and occlusions, and able to control illumination, scale
accurate predictions for pixel-based translation of object          and rotation change.
poses and orientation modules and has been replaced with               The vision-based system, which is actually an extension
a complete CNN prediction network. Also, [191] recently             of Gordon’s method [79], enables the accurate localization
removed the ROI pooled orientation layer and introduced             initialization step called POSESEQ and enables full pose
PVNet (Pixelwise Voting Network) to deny pixel-based                inference in object recognition in a complete cluttered
vectors and use them for key-point positions.                       environment. Thanh et al. presented LieNet [51], as a unique
                                                                    template-based pose estimation method that uses the Lie
C. 6D POSE ESTIMATION DIRECTLY FROM RGB-D IMAGES                    algebraic rotation matrix to estimate the rotation matrix of
A scene coordinate regression (SCoRe) forest is used, trained       an object. It estimates the translation vector by predicting the
in a specific scene, employs only RGB-D image pixel                 distance of the object from the centre of the camera. This
comparison features and has fast calculation accuracy. The          method takes the input of an image and then outputs the
proposed method is an RNSAC-based pose optimization                 object’s identification with a 6D pose, including a bounding
algorithm where SCoRe Forest is evaluated by the RNSAC              box, label, and segmentation mask.
algorithm and makes accurate posture estimates [223]. Since            Vidal et al., [256] developed a method that followed
the additional depth channel of the RGB-D image helps               the basic structure of the point pair feature (PPF) method
extracts the entire 6D pose (3D rotation and 3D translation) of     introduced by Drost [56], which is a combination of two
rigid object instances present in the scene. The core objective     levels, such as global modelling and local matching. The
of the approach is the intermediate representation of the form      main structure identifies the rotation points, model points and
of a dense 3D object coordinate labelled and paired with a          angles of each scene. The expansion of Vidal’s work is the
dense class.                                                        concept of the posture of free-form objects, critical work in
   On the other hand, Taylor [246] did not predict 6 DoF            favour of a highly confused autonomous system. A novel
directly from an RGB image but instead followed the object’s        pre-processing step has been added here, transforming the
coordinates in that image. Each pixel in this image points to       classification into a better efficient feature matching method.
a coordinate of the canonical body in a canonical position
called VM (Vitruvian Manifold). The popular RF (Random              E. CATEGORY-LEVEL 6 DoF POSE ESTIMATION
Forest) [3] classifier is used to vote here, and geometric          Sahin et al., [208] covers various challenges for 6D pose
validity is used.                                                   estimation such as inconsistency of viewpoint, objects (both
   Brachmann et al., [14] provided an idea that is both an          texture and texture-less), curbs, cluttered scene and identical
extension and combination of [223] and [246]. This hybrid           objects. Wang et al., [261] has created a method that assumes
concept estimates the 6D pose of a specific object from a sin-      both 6D poses of hidden object instances without an object
gle RGB-D image. Wang et al., [258] initiated a compelling          CAD model in an RGB-D image. Furthermore, a novel
method in cluttered scenes, which can successfully predict          concept called NOCS (Normalised Object Coordinate Space)

VOLUME 9, 2021                                                                                                               143759
                                                                               S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

FIGURE 2. Increasing amount of efforts in literature on monocular 3D   FIGURE 3. Increasing amount of efforts in literature on 6D pose
object detection in recent years.                                      estimation in recent years.

                                                                       to combine 2D visual context, 3D dimension and ground
has been introduced here, representing a partnership principle
                                                                       plane. Eppner et al., [60] presented and evaluated the winning
for all possible instances of an object.
                                                                       system for the 2015 Amazon Picking Challenge, where they
   Schuster et al., [216] evaluates dense 3D data located in
                                                                       created four key aspects of system building: integration,
multiple light situations and applies online graph SLAM
                                                                       manipulation, manipulation planning, and estimation.
to generate a dense 3D composite map and estimates 6D
                                                                          Google has announced the release of MediaPipe, a 3D
poses. This technique also creates a fancy graph topology for
                                                                       object detection pipeline that identifies objects in 2D images
incorporating the results of local reference filters and overall
                                                                       on everyday objects and estimates their poses and sizes.
high-bandwidth sensor data into sub-maps.
                                                                       MediaPipe is a cross-platform structure that builds ML
                                                                       pipelines and creates 3D bounding boxes with augmented
F. FEATURE MATCHING METHODS                                            reality (AR) [5] and identifies additional information such
To solve the 6D object pose hypothesis and ensure the                  as camera pose, 3D point cloud, lighting and planar
best possible accuracy, Krull [126] successfully applied               surfaces [85], [268]. Basically, MediaPipe performs object
Reinforcement Learning to the pose agent classification                detection, face detection, hand tracking, hair segmentation
for the first time. Each decision here follows the potential           with ML frameworks called Tensorflow and Tensorflow
distribution of a stochastic policy gradient approach that takes       Lite [1].
a direct gradient in terms of the expected loss of interest.              A novel model [101] designed to predict the pose and size
                                                                       of an object from a monocular RGB image has applied a
G. TEMPLATE-MATCHING TECHNIQUES                                        multi-task-learning approach named MobileNetv2 [212] and
Hinterstoisser et al., [91] built a framework called LineMod           predicts object size. The Gaussian regression task applies
for automatic detection and tracking of 3D objects based on            a pose estimation algorithm (EPnP) [136] to the final 3D
the latest template-based approach that uses both depth and            coordinates for the bounding box. A novel model [101]
colour images to capture the object’s presence and 3D shape            designed to predict the pose and size of an object from
on a set of templates with different aspects of an object. Also,       a monocular RGB image has applied a multi-task-learning
the 3D model can be used for the accurate estimation of                approach named MobileNetv2 [212] and predicts object
the position of the object. Tejani et al., [247] developed a           size. The Gaussian regression task applies a pose estimation
novel patch-based framework where a Latent-Class Hough                 algorithm (EPnP) [136] to the final 3D coordinates for the
Forests method for 3D object detection was introduced, and             bounding box.
estimations were made in a heavily cluttered and occluded                 Tremblay et al., [251] introduced the first one-shot deep
environment. This method absorbs the classification labels             neural network for robotic manipulation trained only on
during training, and as a by-product, it creates the right             synthetic data capable of achieving 6-DoF object pose
image-ground mask.                                                     estimates of 3D objects. The system is called DOPE (Deep
                                                                       Object Pose Estimation), which applies the Perspective-N-
H. CNN/ DEEP LEARNING - BASED APPROACHES                               Point (PNP) algorithm, which combines 3D bounding boxes
Krull [125] presented a model for 6D pose estimation, which            with 2D images. Li [141] has proposed a pose correction
applied a CNN to map images and revealed that training                 algorithm where the solution is to correct the pose because the
on a single object was sufficient and that CNN successfully            object is being observed from the centre line of the camera.
generalized all the different objects and backgrounds of an            It is a multi-philosophy fusion framework with a single
image. Rangesh et al., [200] applied an exclusive idea for a           philosophical ambiguity and quick guess selection based on
3D identification box suitable for the object on the ground            a voting scheme.

143760                                                                                                                           VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

TABLE 5. Advantages and disadvantages of some state-of-the-art 6D pose estimation methods.

TABLE 6. 6D full object pose estimation paper collection.

  On the other hand, a model called DeepIM [143] is                        backbone network project as DeepHMap++, which centres
able to predict a relational pose transformation by applying               a two-stage pipeline and integrates two learning concepts
3D location and 3D orientation and a repetitive training                   to estimate 6D poses of invisible objects in challenging
process. The network FlowNetSimple architecture uses the                   scenes [71].

VOLUME 9, 2021                                                                                                                143761
                                                                         S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

I. TEMPLATE-CLUSTERING APPROACHES                                 usually fail to give accurate results. Do et al., [51] has
Zhang et al., [288] has proposed City-LineMod (advanced           suggested an idea to overcome this complicated problem,
to Cognitive Template-Clustering Line mode) method. The           but not entirely successful. Although the work on symmetric
technique applies a 7D (4D geometry + 3D texture) cognitive       object detection is starting to get deeper, not much work has
feature vector to restore the standard 3D spacing points in the   been done to date. More attention and research needs to be
patch-linemode clustering method. Moreover, the distance of       done on this case of symmetrical object identification.
different 3D spatial points will also be affected by the 4D
additional information regarding the direction and width of       3) TRACKING A OBJECT FROM VIDEO
the features.                                                     One possible incoming direction is to simultaneously explore
                                                                  its application as part of a system that uses repetitive
J. HYBRID POSE METHOD                                             neural networks to detect and track objects in video [116].
Martinez et al., [162] presented a hybrid GPU / CPU               In addition, the intense colour variation between the CAD
architecture that uses parallelism at all levels named MOPED      model and the visual avatar is a significant work. Another
(Multiple Object Position Estimation and Detection), a bright     potential research aspect in this context is online model
and measurable perception concept for both object recog-          learning and relocalization [223]. A hypothesis can be
nition and fracture estimation. Furthermore, a mode based         developed to represent both single and multiview with an
on another object recognition algorithm known as POS-             extended update of a new frame [141]. In addition, to avoid
ESEQ [38] showed a massive increase in scalability and            the problem of proper loss, the term-balancing required for
accuracy and optimizes the algorithm’s speed. Technically,        upcoming potential research direction [116].
MOPED has employed a new feature-matching algorithm
that optimizes databases to handle complexity and a robust
                                                                  B. FUTURE RESEARCH DIRECTIONS FOR
pose merge algorithm capable of efficiently rejecting out-
                                                                  6D POSE ESTIMATION
siders with matching K-NN (K-Nearest Neighbour) method
where k > 2 [245]. The default classification algorithm and       1) IMPROVING THE VO (VISUAL ODOMETRY)
SIFTGPU is the MOPED feature extraction algorithm.                Appropriate VO (Visual Odometry) is mandatory in the
                                                                  context of autonomous driving; Thus, the future design of
VI. FUTURE RESEARCH DIRECTIONS
                                                                  both automated car and street scene construction needs to
                                                                  be improved [291]. It is not possible to apply driverless cars
From the above discussion, it is clear that plenty of work
has been done on 3D object detection, which forms a solid         without the proper implementation of VO.
foundation for this field. Nevertheless, further research is
needed as 6D pose estimation systems have not yet performed       2) IMPROVING THE 6D POSE ESTIMATE ACCURACY
adequately. Therefore, this part of the article will give some    One can improve the version of the DeepIM method [143]
possible ideas of the future directions for both sectors, which   for autonomous applications to produce accurate 6D pose
will help understand the status and involvement of 3DOD and       estimates from high-resolution camera images (colour only)
6 DPE.                                                            at high frame rates with a large field view. The authors
                                                                  also mentioned using stereotype camera images as input
A. FUTURE RESEARCH DIRECTIONS FOR 3D                              to improve the quality of this method. Another work can
OBJECT DETECTION                                                  be done by combining the advanced two-step method to
1) DETECTING A RIGID OBJECT                                       transform it into a new pose tracking framework where the
Several existing work [32], [33], [151], [271] showed the         pose parameters from the previous frame can be reused to
efficacy of deep learning in detecting a rigid object. Even       replace the pose detection step in DeepHMap [71]. Adding
though the classifiers are mainly focused on the ‘‘car’’          a branch to the back for object segmentation in DeepHMap
category, the concept of these methods can be contextual to       may provide some additional regularization.
all other solid and inflexible types of objects. The accurate
detection of the 3D rigid object is a complex job and is          3) IMPROVING THE MAP OR VPS
very significant in the domain of computer vision. Currently,     It is an open challenge to efficiently and consistently
using some proposed deep learning techniques, we can detect       merge sub-maps into multi-robot systems to create a long-
inflexible objects, but still, lots of works need to do to        term mapping system, aiming at improving the algorithm
make the process flawless. In developing an autonomous            that matches the map [216]. The globalization strategy
car, accurately identifying rigid objects can be a significant    combines visual positioning services (VPS), street view,
research idea.                                                    and machine learning for more accurate location and
                                                                  adaptation detection. Mutual technology is essential to
2) HANDING ROTATIONALLY SYMMETRIC OBJECTS                         enhance the correct positioning and orientation of blue dots
Identifying half and full symmetry objects like a coffee mug      on digital maps in our cars, smartphones, and up-to-date
or glass is a confusing and complex matter that classifiers       interactions.

143762                                                                                                                   VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

4) IMPROVING THE POSE OF SYMMETRICAL OBJECTS                       resolving visible gaps between machines and humans can be
Since managing the poses of symmetrical or symmetrical             a future inspiration for research.
objects is a complex task, relevant classifiers should be
improved to accomplish the task efficiently [276]. In order        9) EXPLORE GEOMETRIC PROPERTIES
to properly manage symmetrical properties, methods need            Estimating the 6DoF pose of an object from a single RGB
to learn the symmetry of objects and update their capa-            image is a significant and challenging task, especially under
bilities [27]. One of the notable tasks may be to manage           heavy occlusion and for the Texture-Less object. In such
the symmetry property of objects and pose estimation               a case, the exploring of geometric features needs to be
automatically.                                                     improved to estimate the 6 DOF object more efficiently [81].

                                                                   VII. CONCLUSION
5) IMPROVING THE FUNCTION OF MOBILE MANIPULATORS
                                                                   This review paper studies the state-of-the-art deep learning
The efficiency of the POSSEQ [38] classifier can be enriched       techniques for 3D object detection and 6D pose estimation.
by enabling mobile manipulators to work more perfectly to          Most current object detection methods identify images with
communicate with the crowd’s internal environment. Some            a 2D bounding box technique that can recognize both the
hypothetical 6DoF pose [269] reprocessing techniques will          position and range of the objects in the image. However,
be filtered using repetitive closet point-based algorithms         recognizing a vehicle as a 2D BB is not always sufficient
or repetitive retrieval networks. Also, classifiers need to        for perfect autonomous driving. Therefore, predicting the
successfully model and recognize scenes of different sizes         position of the 3D object from the images is just as important
and complexities in large environments [79] (campus,               as determining the 2D position of the vehicle. For 3D
laboratory, shopping centre or a museum).                          object detection, current works report sophisticated results
                                                                   using RGB / RGB-D imagery, point cloud, and fusion-based
6) IMPROVING THE 3D POINT CLOUD NETWORKS                           techniques.
A number of 3D point cloud networks can be replaced directly          Here, with the help of this review, we have addressed the
by the PointNet network [83] for potential improvement             advantages and disadvantages of each of the basic techniques,
in accurate 3D object detection and 6DF pose estimation.           both 3D object detection and 6D pose estimation tech-
A computational budget can be created to know the                  niques. We have also mentioned some traditional theoretical
appropriate time for the softer version of the PoseAgent [126]     evaluation metrics and summarised the popular Big Image
classification. For parallelism, multiple computational cores      datasets applied by well-known object identification and
can be applied by advanced PoseAgent. In addition, training        pose estimation methods. Since the deep learning method
can be provided to replace the processing steps of an existing     of 3D object detection and 6D pose estimation are not as
CNN method and improve the results by observing and                mature as 2D object detection, research is needed for real-
predicting updated postures from the given images [125].           time operation. From now on, a significant improvement
                                                                   needs to be made to manage a fast and reliable 3 DOD
                                                                   and 6 DPE system across a broad set of real-time practical
7) IMPROVING THE DATASET
                                                                   applications. Although RGB-D is much simpler than RGB,
To deal with the common challenges of objects, such as             it faces problems for some depth issues, such as not being
reflective and texture-less objects, and the adverse conditions,   able to recognize small objects properly.
such as occlusion and changing lighting conditions, we can            Several classifications have been proposed in the 6D Pose
integrate some multi-dimensional object models into the            estimation functions, such as the point addition method,
dataset packages. To facilitate the reconstruction of indoor       the template matching method, the Hough forest method,
and outdoor dynamic scenes, 4D or 5D models can be added           and the deep learning method. However, the effectiveness of
to the dataset, which can play an important role in any visual     the proposed classifiers is still far from the level of actual
applications such as navigational systems for moving objects       application, which should be able to successfully predict
(for example: autonomous car) [281].                               6D poses of multi-objects, including severe occurrence and
                                                                   chaos scene situations. Therefore, this article presents an in-
8) REMOVING THE VISIBLE GAP BETWEEN MACHINE                        depth review of the most significant work to date on in-depth
PERFORMANCE AND THAT OF HUMAN’s                                    learning-based 3D object detection and 6D pose estimation
In AppolloCar3D, researchers [238] mentioned four visible          systems. Until then, we believe that this review article can be
surfaces and manually defines a correspondence between             cited and used as a sample source of reference and forms an
critical points and surfaces. They suggested that a total          important endorsement to the research community.
of 66 key points were assigned to every single car model (for
both SUVs and Sedans). According to [238], since people            REFERENCES
cannot memorize the semantic meaning of 66 key points               [1] An End-to-End Open Source Machine Learning Platform.
                                                                    [2] G. N. Albanis, N. Zioulis, A. Chatzitofis, A. Dimou, D. Zarpalas, and
correctly, there is a noticeable gap (∼ 10 %) in between                P. Daras, ‘‘On end-to-end 6DOF object pose estimation and robustness to
algorithms/machines with humans. Henceforth, correctly                  object scale,’’ in Proc. ML Reproducibility Challenge, 2021, pp. 1–9.

VOLUME 9, 2021                                                                                                                         143763
                                                                                            S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

 [3] M. Y. Arafat, S. Hoque, and D. M. Farid, ‘‘Cluster-based under-sampling         [27] C. Capellen, M. Schwarz, and S. Behnke, ‘‘ConvPoseCNN: Dense
     with random forest for multi-class imbalanced classification,’’ in Proc.             convolutional 6D object pose estimation,’’ in Proc. 15th Int. Joint Conf.
     11th Int. Conf. Softw., Knowl., Inf. Manage. Appl. (SKIMA), Dec. 2017,               Comput. Vis., Imag. Comput. Graph. Theory Appl., 2020.
     pp. 1–6.                                                                        [28] F. Chabot, M. Chaouch, J. Rabarisoa, C. Teulière, and A. T. Chateau,
 [4] M. Y. Arafat, S. Hoque, S. Xu, and D. M. Farid, ‘‘An under-                          ‘‘Deep MANTA: A coarse-to-fine many-task network for joint 2D and
     sampling method with support vectors in multi-class imbalanced data                  3D vehicle analysis from monocular image,’’ Tech. Rep., 2017.
     classification,’’ in Proc. 13th Int. Conf. Softw., Knowl., Inf. Manage. Appl.   [29] X. A. Chang, T. Funkhouser, L. Guibas, P. Hanrahan, Q. Huang, Z. Li,
     (SKIMA), Aug. 2019.                                                                  S. Savarese, M. Savva, S. Song, H. Su, J. Xiao, L. Yi, and F. Yu,
 [5] T. R. Azuma, A Survey of Augmented Reality, vol. 6. Hughes Research                  ‘‘ShapeNet: An information-rich 3D model repository,’’ in Proc. Comput.
     Laboratories, 1997.                                                                  Vis. Pattern Recognit., 2015.
 [6] D. H. Ballard, ‘‘Generalizing the Hough transform to detect arbitrary           [30] B. Chen, A. Parra, J. Cao, N. Li, and T.-J. Chin, ‘‘End-to-end learnable
     shapes,’’ Pattern Recognit., vol. 13, no. 2, pp. 111–122, 1981.                      geometric vision by backpropagating PnP optimization,’’ Tech. Rep.,
 [7] M. R. Banham and A. K. Katsaggelos, ‘‘Digital image restoration,’’ IEEE              2020.
     Signal Process. Mag., vol. 14, no. 2, pp. 24–41, Mar. 1997.                     [31] J. Chen and T. Bai, ‘‘SAANet: Spatial adaptive alignment network for
 [8] W. Bao, B. Xu, and Z. Chen, ‘‘MonoFENet: Monocular 3D object                         object detection in automatic driving,’’ Image Vis. Comput., vol. 94,
     detection with feature enhancement networks,’’ IEEE Trans. Image                     Feb. 2020, Art. no. 103873.
     Process., vol. 29, pp. 2753–2765, 2020.                                         [32] X. Chen, K. Kundu, Z. Zhang, H. Ma, S. Fidler, and R. Urtasun,
 [9] I. Barabás, A. Todoruţ, N. Cordoş, and A. Molea, ‘‘Current challenges                ‘‘Monocular 3D object detection for autonomous driving,’’ in Proc. IEEE
     in autonomous driving,’’ IOP Conf. Ser., Mater. Sci. Eng., vol. 252,                 Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2016, pp. 2147–2156.
     Oct. 2017, Art. no. 012096.                                                     [33] X. Chen, H. Ma, J. Wan, B. Li, and T. Xia, ‘‘Multi-view 3D object
[10] J. L. Barron, D. J. Fleet, and S. S. Beauchemin, ‘‘Performance of optical            detection network for autonomous driving,’’ in Proc. IEEE Conf. Comput.
     flow techniques,’’ Int. J. Comput. Vis., vol. 12, no. 1, pp. 43–77, 1994.            Vis. Pattern Recognit. (CVPR), Jul. 2017.
[11] G. Billings and M. Johnson-Roberson, ‘‘SilhoNet: An RGB method for              [34] X. Chen, K. Kundu, Y. Zhu, A. G. Berneshawi, H. Ma, S. Fidler,
     6D object pose estimation,’’ IEEE Robot. Autom. Lett., vol. 4, no. 4,                and R. Urtasun, ‘‘3D object proposals for accurate object class
     pp. 3727–3734, Oct. 2019.                                                            detection,’’ in Advances in Neural Information Processing Systems,
[12] A. Borji, M.-M. Cheng, H. Jiang, and J. Li, ‘‘Salient object detec-                  C. Cortes, N. D. Lawrence, D. D. Lee, M. Sugiyama, and R. Garnett, Eds.
     tion: A benchmark,’’ IEEE Trans. Image Process., vol. 24, no. 12,                    Red Hook, NY, USA: Curran Associates, 2015, pp. 424–432.
     pp. 5706–5722, Dec. 2015.                                                       [35] M.-M. Cheng, Y. Liu, W.-Y. Lin, Z. Zhang, L. P. Rosin, and S. P. H. Torr,
[13] E. Brachmann, F. Michel, A. Krull, M. Y. Yang, S. Gumhold, and                       ‘‘BING: Binarized normed gradients for objectness estimation at 300fps,’’
     C. Rother, ‘‘Uncertainty-driven 6D pose estimation of objects and scenes             Comput. Vis. Media, vol. 5, no. 1, pp. 3–20, 2019.
     from a single RGB image,’’ in Proc. IEEE Conf. Comput. Vis. Pattern             [36] Y. Cheng, ‘‘Mean shift, mode seeking, and clustering,’’ IEEE Trans.
     Recognit. (CVPR), Jun. 2016, pp. 3364–3372.                                          Pattern Anal. Mach. Intell., vol. 17, no. 8, pp. 790–799, Aug. 1995.
[14] E. Brachmann, A. Krull, F. Michel, S. Gumhold, J. Shotton, and                  [37] C. Li, J. Bohren, E. Carlson, and G. D. Hager, ‘‘Hierarchical semantic
     A. C. Rother, ‘‘Learning 6D object pose estimation using 3D object                   parsing for object pose estimation in densely cluttered scenes,’’ in Proc.
     coordinates,’’ in Computer Vision—ECCV 2014, D. Fleet, T. Pajdla,                    IEEE Int. Conf. Robot. Autom. (ICRA), May 2016, pp. 5068–5075.
     B. Schiele, and T. Tuytelaars, Eds. Cham, Switzerland: Springer, 2014,
                                                                                     [38] A. Collet, D. Berenson, S. S. Srinivasa, and D. Ferguson, ‘‘Object
     pp. 536–551.
                                                                                          recognition and full pose registration from a single image for robotic
[15] G. Brazil and X. Liu, ‘‘M3D-RPN: Monocular 3D region proposal
                                                                                          manipulation,’’ in Proc. IEEE Int. Conf. Robot. Autom., May 2009,
     network for object detection,’’ Tech. Rep., 2019.
                                                                                          pp. 48–55.
[16] M. Bruijning, M. D. Visser, C. A. Hallmann, and E. Jongejans,
                                                                                     [39] A. Collet, M. Martinez, and S. S. Srinivasa, ‘‘The MOPED framework:
     ‘‘Trackdem: Automated particle tracking to obtain population counts and
                                                                                          Object recognition and pose estimation for manipulation,’’ Int. J. Robot.
     size distributions from videos in R,’’ Methods Ecol. Evol., vol. 9, no. 4,
                                                                                          Res., vol. 30, no. 10, pp. 1284–1306, Apr. 2011.
     pp. 965–973, Apr. 2018.
                                                                                     [40] A. Conner-Simons and R. Gordon, ‘‘Self-driving cars for country roads,’’
[17] F. Bu, T. Le, X. Du, R. Vasudevan, and M. Johnson-Roberson,
                                                                                          Tech. Rep., May 2018.
     ‘‘Pedestrian planar LiDAR pose (PPLP) network for oriented pedestrian
     detection based on planar LiDAR and monocular images,’’ IEEE Robot.             [41] C. Cortes and V. Vapnik, ‘‘Support-vector networks,’’ Mach. Learn.,
     Autom. Lett., vol. 5, no. 2, pp. 1626–1633, Apr. 2020.                               vol. 20, no. 3, pp. 273–297, 1995, doi: 10.1023/A:1022627411411.1995.
[18] Y. Bukschat and M. Vetter, ‘‘EfficientPose: An efficient, accurate and          [42] R. Cupec, I. Vidović, D. Filko, and P. Ðurović, ‘‘Object recognition
     scalable end-to-end 6D multi object pose estimation approach,’’ in Proc.             based on convex hull alignment,’’ Pattern Recognit., vol. 102, Jun. 2020,
     CVPR, 2020.                                                                          Art. no. 107199.
[19] M. Burenius, J. Sullivan, and S. Carlsson, ‘‘3D pictorial structures for        [43] J. Dai, Y. Li, K. He, and J. Sun, ‘‘R-FCN: Object detection via
     multiple view articulated pose estimation,’’ in Proc. IEEE Conf. Comput.             region-based fully convolutional networks,’’ 2016, arXiv:1605.06409.
     Vis. Pattern Recognit., Jun. 2013, pp. 3618–3625.                                    https://arxiv.org/abs/1605.06409
[20] H. Caesar, V. Bankiti, A. H. Lang, S. Vora, V. E. Liong, Q. Xu,                 [44] J. Dai, H. Qi, Y. Xiong, Y. Li, G. Zhang, H. Hu, and Y. Wei, ‘‘Deformable
     A. Krishnan, Y. Pan, G. Baldan, and O. Beijbom, ‘‘NuScenes: A mul-                   convolutional networks,’’ in Proc. Comput. Vis. Pattern Recognit., 2017.
     timodal dataset for autonomous driving,’’ 2019, arXiv:1903.11027.               [45] N. Dalal and B. Triggs, ‘‘Histograms of oriented gradients for human
     [Online]. Available: http://arxiv.org/abs/1903.11027                                 detection,’’ in Proc. IEEE Comput. Soc. Conf. Comput. Vis. Pattern
[21] Z. Cai and N. Vasconcelos, ‘‘Cascade R-CNN: Delving into high quality                Recognit., vol. 1, Jun. 2005, pp. 886–893.
     object detection,’’ in Proc. Comput. Vis. Pattern Recognit., 2017.              [46] E. R. Davies, Machine Vision: Theory, Algorithms, Practicalities.
[22] B. Calli, A. Singh, J. Bruce, A. Walsman, K. Konolige, S. Srinivasa,                 San Mateo, CA, USA: Morgan Kaufmann, 2004.
     P. Abbeel, and A. M. Dollár, ‘‘Yale-CMU-Berkeley dataset for robotic            [47] J. Dean, G. Corrado, R. Monga, K. Chen, M. Devin, M. Mao,
     manipulation research,’’ Int. J. Robot. Res., vol. 36, no. 3, pp. 261–268,           M. Ranzato, A. Senior, P. Tucker, K. Yang, V. Q. Le, and Y. A.
     Mar. 2017.                                                                           Ng, ‘‘Large scale distributed deep networks,’’ in Advances in Neural
[23] B. Calli, A. Singh, A. Walsman, S. Srinivasa, P. Abbeel, and A. M. Dollár,           Information Processing Systems, F. Pereira, C. J. C. Burges, L. Bottou,
     ‘‘The YCB object and model set: Towards common benchmarks for                        and K. Q. Weinberger, Eds. Red Hook, NY, USA: Curran Associates,
     manipulation research,’’ in Proc. Int. Conf. Adv. Robot. (ICAR), Jul. 2015.          2012, pp. 1223–1231.
[24] D. Campbell, L. Petersson, L. Kneip, and H. Li, ‘‘Globally-optimal inlier       [48] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, ‘‘ImageNet:
     set maximisation for camera pose and correspondence estimation,’’ IEEE               A large-scale hierarchical image database,’’ in Proc. IEEE Conf. Comput.
     Trans. Pattern Anal. Mach. Intell., vol. 42, no. 2, pp. 328–342, Feb. 2020.          Vis. Pattern Recognit., Jun. 2009.
[25] R. J. Campbell and P. J. Flynn, ‘‘A survey of free-form object repre-           [49] W. Ding, S. Li, G. Zhang, X. Lei, and H. Qian, ‘‘Vehicle pose and shape
     sentation and recognition techniques,’’ Comput. Vis. Image Understand.,              estimation through multiple monocular vision,’’ Tech. Rep., 2018.
     vol. 81, no. 2, pp. 166–210, 2001.                                              [50] T.-T. Do, M. Cai, T. Pham, and I. Reid, ‘‘Deep-6DPose: Recovering
[26] Z. Cao, T. Simon, S.-E. Wei, and Y. Sheikh, ‘‘Realtime multi-person 2D               6D object pose from a single RGB image,’’ 2018, arXiv:1802.10367.
     pose estimation using part affinity fields,’’ Tech. Rep., 2016.                      [Online]. Available: http://arxiv.org/abs/1802.10367

143764                                                                                                                                              VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

 [51] T.-T. Do, T. Pham, M. Cai, and D. I. Reid, ‘‘LieNet: Real-time monocular        [73] S. K. Gehrig and F. J. Stein, ‘‘Dead reckoning and cartography using
      object instance 6D pose estimation,’’ in Proc. BMVC, 2018.                           stereo vision for an autonomous car,’’ in Proc. IEEE/RSJ Int. Conf. Intell.
 [52] J. Dokic, B. Müller, and G. Meyer, ‘‘European roadmap smart systems for              Robots Systems. Hum. Environ. Friendly Robots High Intell. Emotional
      automated driving,’’ in Proc. Eur. Technol. Platform Smart Syst. Integr.             Quotients, vol. 3, Oct. 1999, pp. 1507–1512.
      (EPoSS), Apr. 2015.                                                             [74] A. Geiger, P. Lenz, and R. Urtasun, ‘‘Are we ready for autonomous
 [53] P. Dollár, C. Wojek, B. Schiele, and P. Perona, ‘‘Pedestrian detection:              driving? The KITTI vision benchmark suite,’’ in Proc. IEEE Conf.
      An evaluation of the state of the art,’’ IEEE Trans. Pattern Anal. Mach.             Comput. Vis. Pattern Recognit., Jun. 2012, pp. 3354–3361.
      Intell., vol. 34, no. 4, pp. 743–761, Apr. 2012.                                [75] N. Gessert, M. Schlüter, and A. Schlaefer, ‘‘A deep learning approach for
                                                                                           pose estimation from volumetric OCT data,’’ Med. Image Anal., vol. 46,
 [54] P. Dollár, R. Appel, S. Belongie, and P. Perona, ‘‘Fast feature pyramids
                                                                                           pp. 162–179, May 2018.
      for object detection,’’ IEEE Trans. Pattern Anal. Mach. Intell., vol. 36,
                                                                                      [76] R. Girshick, J. Donahue, T. Darrell, and J. Malik, ‘‘Rich feature
      no. 8, pp. 1532–1545, Aug. 2014.
                                                                                           hierarchies for accurate object detection and semantic segmentation,’’ in
 [55] A. Doumanoglou, R. Kouskouridas, S. Malassiotis, and T.-K. Kim,                      Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Jun. 2014, pp. 580–587.
      ‘‘Recovering 6D object pose and predicting next-best-view in the crowd,’’
                                                                                      [77] R. Girshick, ‘‘Fast R-CNN,’’ Tech. Rep., 2015.
      in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2016.
                                                                                      [78] A. González, D. Vázquez, A. M. López, and J. Amores, ‘‘On-board
 [56] B. Drost, M. Ulrich, N. Navab, and S. Ilic, ‘‘Model globally, match                  object detection: Multicue, multimodal, and multiview random forest of
      locally: Efficient and robust 3D object recognition,’’ in Proc. IEEE Com-            local experts,’’ IEEE Trans. Cybern., vol. 47, no. 11, pp. 3980–3990,
      put. Soc. Conf. Comput. Vis. Pattern Recognit., Jun. 2010, pp. 998–1005.             Nov. 2017.
 [57] B. Drost, M. Ulrich, P. Bergmann, P. Hartinger, and C. Steger,                  [79] I. Gordon and D. Lowe, ‘‘What and where: 3D object recognition with
      ‘‘Introducing MVTec ITODD—A dataset for 3D object recognition in                     accurate pose,’’ in Toward Category-Level Object Recognition, vol. 4170,
      industry,’’ in Proc. IEEE Int. Conf. Comput. Vis. Workshops (ICCVW),                 J. Ponce, M. Hebert, C. Schmid, and A. Zisserman, Eds. Berlin, Germany:
      Oct. 2017.                                                                           Springer, Jan. 2006, pp. 67–82.
 [58] M. Engelcke, D. Rao, D. Z. Wang, C. H. Tong, and I. Posner, ‘‘Vote3Deep:        [80] Y. Guo, H. Wang, Q. Hu, H. Liu, L. Liu, and M. Bennamoun, ‘‘Deep
      Fast object detection in 3D point clouds using efficient convolutional               learning for 3D point clouds: A survey,’’ in Proc. CVPR, 2020.
      neural networks,’’ in Proc. IEEE Int. Conf. Robot. Autom. (ICRA),               [81] A. Gupta, J. Medhi, A. Chattopadhyay, and V. Gupta, ‘‘End-to-end
      May 2017.                                                                            differentiable 6DoF object pose estimation with local and global
 [59] M. Enzweiler and D. M. Gavrila, ‘‘A multilevel mixture-of-experts                    constraints,’’ Tech. Rep., 2020.
      framework for pedestrian classification,’’ IEEE Trans. Image Process.,          [82] F. K. Gustafsson, M. Danelljan, and T. B. Schon, ‘‘Accurate 3D
      vol. 20, no. 10, pp. 2967–2979, Oct. 2011.                                           object detection using energy-based models,’’ in Proc. IEEE/CVF Conf.
 [60] C. Eppner, S. Höfer, R. Jonschkowski, R. Martín-Martín, A. Sieverling,               Comput. Vis. Pattern Recognit. Workshops (CVPRW), Jun. 2021.
      V. Wall, and O. Brock, ‘‘Lessons from the Amazon picking challenge:             [83] F. Hagelskjaer and A. Buch, ‘‘PointVoteNet: Accurate object detection
      Four aspects of building robotic systems,’’ in Proc. 12th Robot., Sci. Syst.,        and 6 DOF pose estimation in point clouds,’’ in Proc. Comput. Vis. Pattern
      2017, pp. 4831–4835.                                                                 Recognit. (CVPR), Dec. 2019.
                                                                                      [84] J. A. Hawkins, ‘‘Mit built a self-driving car that can navigate unmapped
 [61] M. Everingham, S. M. A. Eslami, L. Van Gool, C. K. I. Williams,
                                                                                           country roads,’’ Tech. Rep., May 2015.
      J. Winn, and A. Zisserman, ‘‘The Pascal visual object classes challenge:
      A retrospective,’’ Int. J. Comput. Vis., vol. 111, no. 1, pp. 98–136,           [85] M. Hays and T. Mullen, ‘‘Mediapipe on the web, blog,’’ Tech. Rep.,
      Jan. 2015.                                                                           Jan. 2020.
                                                                                      [86] K. He, G. Gkioxari, P. Dollár, and R. Girshick, ‘‘Mask R-CNN,’’ in Proc.
 [62] M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn, and
                                                                                           IEEE Int. Conf. Comput. Vis. (ICCV), Oct. 2017.
      A. Zisserman. (2007). The PASCAL Visual Object Classes Chal-
                                                                                      [87] K. He, X. Zhang, S. Ren, and J. Sun, ‘‘Deep residual learning for
      lenge 2007 (VOC2007) Results. [Online]. Available: http://www.pascal-
                                                                                           image recognition,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit.
      network.org/challenges/VOC/voc2007/workshop/index.html
                                                                                           (CVPR), Jun. 2016.
 [63] J. Fang, L. Zhou, and G. Liu, ‘‘3D bounding box estimation for                  [88] Q. He, Z. Wang, H. Zeng, Y. Zeng, S. Liu, and B. Zeng, ‘‘SVGA-Net:
      autonomous vehicles by cascaded geometric constraints and depurated                  Sparse voxel-graph attention network for 3D object detection from point
      2D detections using 3D results,’’ Tech. Rep., 2019.                                  clouds,’’ in Proc. CVPR, 2020.
 [64] P. F. Felzenszwalb, R. B. Girshick, D. McAllester, and D. Ramanan,              [89] Z. He, W. Feng, X. Zhao, and Y. Lv, ‘‘6D pose estimation of objects:
      ‘‘Object detection with discriminatively trained part-based models,’’                Recent technologies and challenges,’’ Appl. Sci., vol. 11, no. 1, p. 228,
      IEEE Trans. Pattern Anal. Mach. Intell., vol. 32, no. 9, pp. 1627–1645,              Dec. 2020.
      Sep. 2010.                                                                      [90] G. Hetzel, B. Leibe, P. Levi, and B. Schiele, ‘‘3D object recognition from
 [65] M. A. Fischler and R. Bolles, ‘‘Random sample consensus: A paradigm                  range images using local feature histograms,’’ in Proc. IEEE Comput. Soc.
      for model fitting with applications to image analysis and automated                  Conf. Comput. Vis. Pattern Recognit. (CVPR), vol. 2, Dec. 2001, p. 2.
      cartography,’’ Commun. ACM, vol. 24, no. 6, pp. 381–395, Jun. 1981.             [91] S. Hinterstoisser, V. Lepetit, S. Ilic, S. Holzer, G. Bradski, K. Konolige,
 [66] R. Fisher, ‘‘CVonline: The evolving, distributed, non-proprietary, on-               and N. Navab, ‘‘Model based training, detection and pose estimation of
      line compendium of computer visio,’’ School Inform., Univ. Edinburgh,                texture-less 3D objects in heavily cluttered scenes,’’ in Computer Vision—
      Edinburgh, U.K., Tech. Rep., 2019.                                                   ACCV 2012, K. M. Lee, Y. Matsushita, J. M. Rehg, and Z. Hu, Eds. Berlin,
 [67] A. D. Forsyth and J. Ponce, Computer Vision: A Modern Approach,                      Germany: Springer, 2013, pp. 548–562.
      no. 792. London, U.K.: Pearson, 2011.                                           [92] S. Hinterstoisser, V. Lepetit, N. Rajkumar, and K. Konolige, Going
                                                                                           Further With Point Pair Features (Lecture Notes in Computer Science).
 [68] Y. Freund and R. E. Schapire, ‘‘A decision-theoretic generalization of
                                                                                           2016, pp. 834–848.
      on-line learning and an application to boosting,’’ J. Comput. Syst. Sci.,
      vol. 55, no. 1, pp. 119–139, Aug. 1997.                                         [93] G. Hinton, L. Deng, D. Yu, G. E. Dahl, A. Mohamed, N. Jaitly, A. Senior,
                                                                                           V. Vanhoucke, P. Nguyen, T. N. Sainath, and B. Kingsbury, ‘‘Deep neural
 [69] A. Frome, D. Huber, R. Kolluri, T. Bülow, and J. Malik, ‘‘Recognizing
                                                                                           networks for acoustic modeling in speech recognition: The shared views
      objects in range data using regional point descriptors,’’ in Computer
                                                                                           of four research groups,’’ IEEE Signal Process. Mag., vol. 29, no. 6,
      Vision—ECCV 2004, T. Pajdla and J. Matas, Eds. Berlin, Germany:
                                                                                           pp. 82–97, Nov. 2012.
      Springer, 2004, pp. 224–237.
                                                                                      [94] G. E. Hinton and R. R. Salakhutdinov, ‘‘Reducing the dimensionality of
 [70] H. Fu, M. Gong, C. Wang, K. Batmanghelich, and D. Tao, ‘‘Deep ordinal                data with neural networks,’’ Science, vol. 313, no. 5786, pp. 504–507,
      regression network for monocular depth estimation,’’ in Proc. IEEE/CVF               2006.
      Conf. Comput. Vis. Pattern Recognit., Jun. 2018.                                [95] D.-C. Hoang, A. J. Lilienthal, and T. Stoyanov, ‘‘Panoptic 3D mapping
 [71] M. Fu and W. Zhou, ‘‘DeepHMap++: Combined projection grouping and                    and object pose estimation using adaptively weighted semantic informa-
      correspondence learning for full DoF pose estimation,’’ Sensors, vol. 19,            tion,’’ IEEE Robot. Autom. Lett., vol. 5, no. 2, pp. 1962–1969, Apr. 2020.
      no. 5, p. 1032, Feb. 2019.                                                      [96] T. Hodan, P. Haluza, S. Obdrzalek, J. Matas, M. Lourakis, and X. Zabulis,
 [72] L. A. Gatys, A. S. Ecker, and M. Bethge, ‘‘A neural algorithm                        ‘‘T-LESS: An RGB-D dataset for 6D pose estimation of texture-less
      of artistic style,’’ 2015, arXiv:1508.06576. [Online]. Available:                    objects,’’ in Proc. IEEE Winter Conf. Appl. Comput. Vis. (WACV),
      http://arxiv.org/abs/1508.06576                                                      Mar. 2017.

VOLUME 9, 2021                                                                                                                                               143765
                                                                                              S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

 [97] T. Hodan, E. J. S. Matas, and S. Obdrzálek, ‘‘On evaluation of 6D object       [121] H. Kobatake and Y. Yoshinaga, ‘‘Detection of spicules on mammogram
      pose estimation,’’ in Proc. ECCV Workshops, 2016.                                    based on skeleton analysis,’’ IEEE Trans. Med. Imag., vol. 15, no. 3,
 [98] T. Hodan, F. Michel, E. Brachmann, W. Kehl, A. G. Buch, D. Kraft,                    pp. 235–245, Jun. 1996.
      B. Drost, J. Vidal, S. Ihrke, X. Zabulis, C. Sahin, F. Manhardt, F. Tombari,   [122] L. Koval, J. Vaňuš, and P. Bilík, ‘‘Distance measuring by ultrasonic
      T.-K. Kim, J. Matas, and C. Rother, ‘‘Bop: Benchmark for 6D object pose              sensor,’’ IFAC-PapersOnLine, vol. 49, no. 25, pp. 153–158, 2016.
      estimation,’’ in Proc. Eur. Conf. Comput. Vis., 2018, pp. 19–34.               [123] A. Krizhevsky, I. Sutskever, and G. Hinton, ‘‘ImageNet classification with
 [99] T. Hodaň, X. Zabulis, M. Lourakis, Š. Obdržálek, and J. Matas,                       deep convolutional neural networks,’’ in Proc. Neural Inf. Process. Syst.,
      ‘‘Detection and fine 3D pose estimation of texture-less objects in RGB-              vol. 25, Jan. 2012.
      D images,’’ in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS),          [124] A. Krizhevsky, I. Sutskever, and G. E. Hinton, ‘‘ImageNet classification
      Sep. 2015, pp. 4421–4428.                                                            with deep convolutional neural networks,’’ Commun. ACM, vol. 60, no. 6,
[100] S. Hoque, D. M. Farid, and M. Y. Arafat, ‘‘Advanced data balancing                   pp. 84–90, May 2017.
      method with SVM decision boundary and bagging,’’ in Proc. 6th IEEE             [125] A. Krull, E. Brachmann, F. Michel, M. Y. Yang, S. Gumhold, and
      CSDE. Melbourne, VIC, Australia: CQUniv. Australia, 2019.                            C. Rother, ‘‘Learning analysis-by-synthesis for 6D pose estimation in
[101] T. Hou, A. Ahmadyan, L. Zhang, J. Wei, and M. Grundmann,                             RGB-D images,’’ Tech. Rep., 2015.
      ‘‘MobilePose: Real-time pose estimation for unseen objects with weak           [126] A. Krull, E. Brachmann, S. Nowozin, F. Michel, J. Shotton, and
      shape supervision,’’ in Proc. Comput. Vis. Pattern Recognit. (CVPR),                 C. Rother, ‘‘PoseAgent: Budget-constrained 6D object pose estimation
      2020.                                                                                via reinforcement learning,’’ in Proc. IEEE Conf. Comput. Vis. Pattern
[102] H.-N. Hu, Q.-Z. Cai, D. Wang, J. Lin, M. Sun, P. Krähenbühl, T. Darrell,             Recognit. (CVPR), Jul. 2017.
      and F. Yu, ‘‘Joint monocular 3D vehicle detection and tracking,’’              [127] A. Krull, F. Michel, E. Brachmann, S. Gumhold, S. Ihrke, and
      Tech. Rep., 2018.                                                                    A. C. Rother, ‘‘6-DOF model based tracking via object coordinate regres-
[103] J. Huang, V. Rathod, C. Sun, M. Zhu, A. Korattikara, A. Fathi, I. Fischer,           sion,’’ in Computer Vision—ACCV 2014, D. Cremers, I. Reid, H. Saito,
      Z. Wojna, Y. Song, S. Guadarrama, and K. Murphy, ‘‘Speed/accuracy                    M.-H. Yang, Eds. Cham, Switzerland: Springer, 2015, pp. 384–399.
      trade-offs for modern convolutional object detectors,’’ in Proc. IEEE          [128] A. Kundu, Y. Li, and J. M. Rehg, ‘‘3D-RCNN: Instance-level 3D
      Conf. Comput. Vis. Pattern Recognit. (CVPR), Jul. 2017.                              object reconstruction via render-and-compare,’’ in Proc. IEEE/CVF Conf.
[104] V. Ilci and C. Toth, ‘‘High definition 3D map creation using                         Comput. Vis. Pattern Recognit., Jun. 2018, pp. 3559–3568.
      GNSS/IMU/LiDAR sensor integration to support autonomous vehicle                [129] K. Lai, L. Bo, X. Ren, and D. Fox, ‘‘A large-scale hierarchical multi-
      navigation,’’ Sensors, vol. 20, no. 3, p. 899, Feb. 2020.                            view RGB-D object dataset,’’ in Proc. IEEE Int. Conf. Robot. Autom.,
[105] A. Ioannidou, E. Chatzilari, S. Nikolopoulos, and I. Kompatsiaris, ‘‘Deep            May 2011, pp. 1817–1824.
      learning advances in computer vision with 3D data: A survey,’’ ACM             [130] Y. Lamdan and H. J. Wolfson, ‘‘Geometric hashing: A general and
      Comput. Surveys, vol. 50, no. 2, pp. 1–38, Jun. 2017.                                efficient model-based recognition scheme,’’ in Proc. 2nd Int. Conf.
                                                                                           Comput. Vis., 1988, pp. 238–249.
[106] S. Iwase, X. Liu, R. Khirodkar, R. Yokota, and M. K. Kitani,
      ‘‘Repose: Real-time iterative rendering and refinement for 6D object pose      [131] T. Lassa, ‘‘The beginning of the end of driving,’’ Tech. Rep., Nov. 2012.
      estimation,’’ Tech. Rep., 2021.                                                [132] F. Lateef and Y. Ruichek, ‘‘Survey on semantic segmentation using deep
                                                                                           learning techniques,’’ Neurocomputing, vol. 338, pp. 321–348, Apr. 2019.
[107] J. Ku, M. Mozifian, J. Lee, A. Harakeh, and S. L. Waslander, ‘‘Joint 3D
      proposal generation and object detection from view aggregation,’’ in Proc.     [133] H. Law and J. Deng, ‘‘CornerNet: Detecting objects as paired keypoints,’’
      IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS), Oct. 2018, pp. 1–8.                 Tech. Rep., 2018.
[108] B. Jähne and H. Haußecker, Computer Vision and Applications a Guide            [134] Y. LeCun, B. Boser, J. S. Denker, D. Henderson, R. E. Howard,
      for Students and Practitioners. New York, NY, USA: Academic, 2000.                   W. Hubbard, and L. D. Jackel, ‘‘Backpropagation applied to handwritten
                                                                                           zip code recognition,’’ Neural Comput., vol. 1, no. 4, pp. 541–551,
[109] J. Janai, F. Güney, A. Behl, and A. Geiger, ‘‘Computer vision for
                                                                                           Dec. 1989.
      autonomous vehicles: Problems, datasets and state of the art,’’ Tech. Rep.,
                                                                                     [135] Y. LeCun, Y. Bengio, and G. Hinton, ‘‘Deep learning,’’ Nature, vol. 521,
      2017.
                                                                                           no. 7553, pp. 436–444, May 2015.
[110] Y. Jia, E. Shelhamer, J. Donahue, S. Karayev, J. Long, R. Girshick,
                                                                                     [136] V. Lepetit, F. Moreno-Noguer, and P. Fua, ‘‘EPnP: An accurate O(n)
      S. Guadarrama, and T. Darrell, ‘‘Caffe: Convolutional architecture for fast
                                                                                           solution to the PnP problem,’’ Int. J. Comput. Vis., vol. 81, no. 2,
      feature embedding,’’ Tech. Rep., 2014.
                                                                                           pp. 155–166, Feb. 2009.
[111] T. Joachims, T. Finley, and C.-N. J. Yu, ‘‘Cutting-plane training of
                                                                                     [137] V. Lepetit, L. Vacchetti, D. Thalmann, and P. Fua, ‘‘Fully automated and
      structural SVMs,’’ Mach. Learn., vol. 77, no. 1, pp. 27–59, Oct. 2009.
                                                                                           stable registration for augmented reality applications,’’ in Proc. 2nd IEEE
[112] A. E. Johnson and M. Hebert, ‘‘Using spin images for efficient object                ACM Int. Symp. Mixed Augmented Reality, Nov. 2003, pp. 93–102.
      recognition in cluttered 3D scenes,’’ IEEE Trans. Pattern Anal. Mach.          [138] B. Li, ‘‘3D fully convolutional network for vehicle detection in point
      Intell., vol. 21, no. 5, pp. 433–449, May 1999.                                      cloud,’’ in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS),
[113] E. Jörgensen, C. Zach, and F. Kahl, ‘‘Monocular 3D object detection                  Sep. 2017, pp. 1513–1518.
      and box fitting trained end-to-end using intersection-over-union loss,’’       [139] B. Li, T. Zhang, and T. Xia, ‘‘Vehicle detection from 3D lidar using fully
      Tech. Rep., 2019.                                                                    convolutional network,’’ Tech. Rep., 2016.
[114] H. Kang and C. Chen, ‘‘Fruit detection, segmentation and 3D visuali-           [140] B. Li, W. Ouyang, L. Sheng, X. Zeng, and X. Wang, ‘‘GS3D: An efficient
      sation of environments in apple orchards,’’ Comput. Electron. Agricult.,             3D object detection framework for autonomous driving,’’ Tech. Rep.,
      vol. 171, Apr. 2020, Art. no. 105302.                                                2019.
[115] L. Ke, S. Li, Y. Sun, Y.-W. Tai, and C.-K. Tang, ‘‘GSNet: Joint                [141] C. Li, J. Bai, and D. G. Hager, ‘‘A unified framework for multi-view multi-
      vehicle pose and shape reconstruction with geometrical and scene-aware               class object pose estimation,’’ Tech. Rep., 2018.
      supervision,’’ in Proc. CVPR, 2020.                                            [142] P. Li, H. Zhao, P. Liu, and F. Cao, ‘‘RTM3D: Real-time monocular 3D
[116] W. Kehl, F. Manhardt, F. Tombari, S. Ilic, and N. Navab, ‘‘SSD-6D:                   detection from object keypoints for autonomous driving,’’ Tech. Rep.,
      Making RGB-based 3D detection and 6D pose estimation great again,’’                  2020.
      Tech. Rep., 2017.                                                              [143] Y. Li, G. Wang, X. Ji, Y. Xiang, and D. Fox, ‘‘DeepIM: Deep iterative
[117] W. Kehl, F. Tombari, N. Navab, S. Ilic, and V. Lepetit, ‘‘Hashmod:                   matching for 6D pose estimation,’’ Int. J. Comput. Vis., vol. 128, no. 3,
      A hashing method for scalable 3D object detection,’’ in Proc. Brit. Mach.            pp. 657–678, Nov. 2019.
      Vis. Conf., 2015.                                                              [144] M. Liang, B. Yang, Y. Chen, R. Hu, and R. Urtasun, ‘‘Multi-task multi-
[118] Y. Kim and D. Kum, ‘‘Deep learning based vehicle position and                        sensor fusion for 3D object detection,’’ in Proc. IEEE/CVF Conf. Comput.
      orientation estimation via inverse perspective mapping image,’’ in Proc.             Vis. Pattern Recognit. (CVPR), Jun. 2019.
      IEEE Intell. Vehicles Symp. (IV), Jun. 2019, pp. 317–323.                      [145] R. Lienhart and J. Maydt, ‘‘An extended set of Haar-like features for
[119] L. R. Klatzky, Allocentric and Egocentric Spatial Representations: Def-              rapid object detection,’’ in Proc. Int. Conf. Image Process., vol. 1, 2002,
      initions, Distinctions, and Interconnections (Lecture Notes in Computer              pp. 1–900.
      Science), vol. 1404. Springer, 1998.                                           [146] J. J. Lim, H. Pirsiavash, and A. Torralba, ‘‘Parsing IKEA objects: Fine
[120] R. Klette, Concise Computer Vision, An Introduction Into Theory and                  pose estimation,’’ in Proc. IEEE Int. Conf. Comput. Vis., Dec. 2013,
      Algorithms. Springer, 2014.                                                          pp. 2992–2999.

143766                                                                                                                                                VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

[147] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár, ‘‘Focal loss for      [173] A. Mukhtar, L. Xia, and T. B. Tang, ‘‘Vehicle detection techniques for
      dense object detection,’’ Tech. Rep., 2017.                                         collision avoidance systems: A review,’’ IEEE Trans. Intell. Transp. Syst.,
[148] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan,                   vol. 16, no. 5, pp. 2318–2338, May 2015.
      P. Dollár, and C. L. Zitnick, ‘‘Microsoft COCO: Common objects in             [174] R. Mur-Artal and J. D. Tardós, ‘‘ORB-SLAM2: An open-source slam
      context,’’ in Computer Vision—ECCV 2014, D. Fleet, T. Pajdla, B.                    system for monocular, stereo, and RGB-D cameras,’’ IEEE Trans. Robot.,
      Schiele, and T. Tuytelaars, Eds. Cham, Switzerland: Springer, 2014,                 vol. 33, no. 5, pp. 1255–1262, Oct. 2017.
      pp. 740–755.                                                                  [175] A. Naiden, V. Paunescu, G. Kim, B. Jeon, and M. Leordeanu, ‘‘Shift R-
[149] F. Liu, P. Fang, Z. Yao, R. Fan, Z. Pan, W. Sheng, and H. Yang,                     CNN: Deep monocular 3D object detection with closed-form geometric
      ‘‘Recovering 6D object pose from RGB indoor image based on two-                     constraints,’’ Tech. Rep., 2019.
      stage detection network with multi-task loss,’’ Neurocomputing, vol. 337,     [176] V. Nair and E. G. Hinton, ‘‘Rectified linear units improve restricted
      pp. 15–23, Apr. 2019.                                                               Boltzmann machines,’’ in Proc. 27th Int. Conf. Int. Conf. Mach. Learn.
[150] L. Liu, J. Lu, C. Xu, Q. Tian, and J. Zhou, ‘‘Deep fitting degree scoring           (ICML). Madison, WI, USA: Omnipress, 2010, pp. 807–814.
      network for monocular 3D object detection,’’ in Proc. IEEE/CVF Conf.          [177] M. Naseer, S. Khan, and F. Porikli, ‘‘Indoor scene understanding
      Comput. Vis. Pattern Recognit. (CVPR), Jun. 2019.                                   in 2.5/3D for autonomous agents: A survey,’’ IEEE Access, vol. 7,
[151] P. L. Liu, ‘‘Monocular 3D object detection in autonomous driving—A                  pp. 1859–1887, 2019.
      review,’’ Blog, 2019.                                                         [178] C. Nicholson, ‘‘A beginner’s guide to important topics in AI, machine
[152] P. L. Liu, ‘‘Orientation estimation in monocular 3D object detection,’’             learning, and deep learning,’’ Tech. Rep., 2019.
      Blog, Oct. 2019.                                                              [179] H. Noh, S. Hong, and B. Han, ‘‘Learning deconvolution network for
[153] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed, C.-Y. Fu, and                   semantic segmentation,’’ Tech. Rep., 2015.
      C. A. Berg, SSD: Single Shot MultiBox Detector (Lecture Notes in              [180] D. Nospes, K. Safronov, S. Gillet, K. Brillowski, and U. E. Zimmermann,
      Computer Science). 2016, pp. 21–37.                                                 ‘‘Recognition and 6D pose estimation of large-scale objects using 3D
[154] Y.-C. Liu, K.-Y. Lin, and Y.-S. Chen, ‘‘Bird’s-eye view vision system               semi-global descriptors,’’ in Proc. 16th Int. Conf. Mach. Vis. Appl. (MVA),
      for vehicle surrounding monitoring,’’ in Robot Vision, G. Sommer and                May 2019, pp. 1–6.
      R. Klette, Eds. Berlin, Germany: Springer, 2008, pp. 207–218.                 [181] D. Novotny, N. Ravi, B. Graham, N. Neverova, and A. Vedaldi, ‘‘C3DPO:
[155] Z. Liu, L. Wang, G. Hua, Q. Zhang, Z. Niu, Y. Wu, and N. Zheng, ‘‘Joint             Canonical 3D pose networks for non-rigid structure from motion,’’ in
      video object discovery and segmentation by coupled dynamic Markov                   Proc. IEEE/CVF Int. Conf. Comput. Vis. (ICCV), Oct. 2019.
      networks,’’ IEEE Trans. Image Process., vol. 27, no. 12, pp. 5840–5853,       [182] Oceanservice.noaa.gov, ‘‘What is lidar,’’ Nat. Ocean. Atmos. Admin.,
      Dec. 2018.                                                                          Feb. 2021.
[156] D. G. Lowe, ‘‘Object recognition from local scale-invariant features,’’ in    [183] International Theses, Univ. Tasmania, Hobart, TAS, Australia.
      Proc. IEEE Int. Conf. Comput. Vis., vol. 2, Sep. 1999, pp. 1150–1157.         [184] Open Access Repository, Univ. Tasmania, Hobart, TAS, Australia.
[157] D. G. Lowe, ‘‘Distinctive image features from scale-invariant keypoints,’’    [185] M. Ozuysal, V. Lepetit, and P. Fua, ‘‘Pose estimation for category specific
      Int. J. Comput. Vis., vol. 60, no. 2, pp. 91–110, 2004.                             multiview object localization,’’ in Proc. IEEE Conf. Comput. Vis. Pattern
[158] Q. Luo, H. Ma, Y. Wang, L. Tang, and R. Xiong, ‘‘3D-SSD: Learning                   Recognit., Jun. 2009, pp. 778–785.
      hierarchical features from RGB-D images for amodal 3D object                  [186] J. Pang, K. Chen, J. Shi, H. Feng, W. Ouyang, and D. Lin, ‘‘Libra R-
      detection,’’ Tech. Rep., 2017.                                                      CNN: Towards balanced learning for object detection,’’ in Proc. Comput.
[159] X. Ma, Z. Wang, H. Li, P. Zhang, X. Fan, and W. Ouyang, ‘‘Accurate                  Vis. Pattern Recognit., 2019.
      monocular object detection via color-embedded 3D reconstruction for           [187] C. Papazov and D. Burschka, ‘‘An efficient RANSAC for 3D object
      autonomous driving,’’ Tech. Rep., 2019.                                             recognition in noisy and occluded scenes,’’ in Proc. 10th Asian Conf.
[160] G. Mamic and M. Bennamoun, ‘‘Representation and recognition of 3D                   Comput. Vis. (ACCV), Jan. 2010, pp. 135–148.
      free-form objects,’’ Digit. Signal Process., vol. 12, pp. 47–76, Jan. 2002.   [188] K. Park, T. Patten, and M. Vincze, ‘‘Pix2Pose: Pixel-wise coordinate
[161] F. Manhardt, W. Kehl, and A. Gaidon, ‘‘ROI-10D: Monocular lifting of                regression of objects for 6D pose estimation,’’ in Proc. IEEE/CVF Int.
      2D detection to 6D pose and metric shape,’’ Tech. Rep., 2018.                       Conf. Comput. Vis. (ICCV), Oct. 2019.
[162] M. Martinez, A. Collet, and S. S. Srinivasa, ‘‘MOPED: A scalable and low      [189] N. Payet and S. Todorovic, ‘‘From contours to 3D object detection
      latency object recognition and pose estimation system,’’ in Proc. IEEE Int.         and pose estimation,’’ in Proc. Int. Conf. Comput. Vis., Nov. 2011,
      Conf. Robot. Autom., May 2010, pp. 2043–2049.                                       pp. 983–990.
[163] E. Marchand, H. Uchiyama, and F. Spindler, ‘‘Pose estimation for              [190] S. Pendleton, H. Andersen, X. Du, X. Shen, M. Meghjani, Y. Eng,
      augmented reality: A hands-on survey,’’ IEEE Trans. Vis. Comput.                    D. Rus, and M. Ang, ‘‘Perception, planning, control, and coordination
      Graph., vol. 22, no. 12, pp. 2633–2651, Dec. 2016.                                  for autonomous vehicles,’’ Machines, vol. 5, no. 1, p. 6, Feb. 2017.
[164] K. Matzen and N. Snavely, ‘‘NYC3DCars: A dataset of 3D vehicles in            [191] S. Peng, Y. Liu, Q. Huang, H. Bao, and X. Zhou, ‘‘PVNet: Pixel-wise
      geographic context,’’ in Proc. IEEE Int. Conf. Comput. Vis., Dec. 2013,             voting network for 6DoF pose estimation,’’ Tech. Rep., 2018.
      pp. 761–768.                                                                  [192] K. Piper, ‘‘It’s 2020. Where are our self-driving cars?’’ Tech. Rep., 2020.
[165] J. Memon, M. Sami, and R. A. Khan, ‘‘Handwritten optical character            [193] D. Forsyth and J. Ponce, Computer Vision: A Modern Approach. 2003.
      recognition (OCR): A comprehensive systematic literature review               [194] V. Prisacariu and I. Reid, ‘‘PWP3D: Real-time segmentation and tracking
      (SLR),’’ Tech. Rep., 2020.                                                          of 3D objects,’’ Int. J. Comput. Vis., vol. 98, no. 3, pp. 335–354, 2012.
[166] F. Michel, A. Kirillov, E. Brachmann, A. Krull, S. Gumhold,                   [195] R. C. Qi, W. Liu, C. Wu, H. Su, and J. L. Guibas, ‘‘Frustum PointNets for
      B. Savchynskyy, and C. Rother, ‘‘Global hypothesis generation for 6D                3D object detection from RGB-D data,’’ Tech. Rep., 2017.
      object pose estimation,’’ Tech. Rep., 2016.                                   [196] J. Qian, S. Feng, T. Tao, Y. Hu, Y. Li, Q. Chen, and C. Zuo, ‘‘Deep-
[167] S. Minaee, Y. Boykov, F. Porikli, A. Plaza, N. Kehtarnavaz, and                     learning-enabled geometric constraints and phase unwrapping for single-
      A. D. Terzopoulos, ‘‘Image segmentation using deep learning: A survey,’’            shot absolute 3D shape measurement,’’ APL Photon., vol. 5, no. 4,
      in Proc. CVPR, 2020.                                                                Apr. 2020, Art. no. 046105.
[168] C. Mitash, A. Boularias, and K. E. Bekris, ‘‘Improving 6D pose                [197] Z. Qin, J. Wang, and Y. Lu, ‘‘MonoGRNet: A geometric reasoning
      estimation of objects in clutter via physics-aware Monte Carlo tree                 network for monocular 3D object localization,’’ Tech. Rep., 2018.
      search,’’ in Proc. IEEE Int. Conf. Robot. Autom. (ICRA), May 2018,            [198] M. Rad and V. Lepetit, ‘‘BB8: A scalable, accurate, robust to partial
      pp. 1–8.                                                                            occlusion method for predicting the 3D poses of challenging objects
[169] F. Mokhtarian, N. Khalili, and P. Yuen, ‘‘Multi-scale free-form 3D object           without using depth,’’ in Proc. ICCV, 2017, pp. 3828–3836.
      recognition using 3D models,’’ Image Vis. Comput., vol. 19, no. 5,            [199] M. M. Rahman, Y. Tan, J. Xue, and K. Lu, ‘‘Recent advances in 3D object
      pp. 271–281, 2001.                                                                  detection in the era of deep neural networks: A survey,’’ IEEE Trans.
[170] T. Morris, Computer Vision and Image Processing. Red Globe Press,                   Image Process., vol. 29, pp. 2947–2962, 2020.
      2003.                                                                         [200] A. Rangesh and M. M. Trivedi, ‘‘Ground plane polling for 6DoF pose
[171] T. Morris, Enlarge Computer Vision and Image Processing, no. 320.                   estimation of objects on the road,’’ Tech. Rep., 2018.
      Red Globe Press, 2004.                                                        [201] E. Real, J. Shlens, S. Mazzocchi, X. Pan, and V. Vanhoucke, ‘‘YouTube-
[172] A. Mousavian, D. Anguelov, J. Flynn, and J. Kosecka, ‘‘3D bounding box              BoundingBoxes: A large high-precision human-annotated data set for
      estimation using deep learning and geometry,’’ Tech. Rep., 2016.                    object detection in video,’’ Tech. Rep., 2017.

VOLUME 9, 2021                                                                                                                                              143767
                                                                                             S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

[202] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, ‘‘You only look once:     [227] A. Simonelli, S. R. R. Bulò, L. Porzi, M. López-Antequera, and
      Unified, real-time object detection,’’ Tech. Rep., 2015.                            P. Kontschieder, ‘‘Disentangling monocular 3D object detection,’’
[203] S. Ren, K. He, R. Girshick, and J. Sun, ‘‘Faster R-CNN: Towards real-time           Tech. Rep., 2019.
      object detection with region proposal networks,’’ in Proc. Adv. Neural Inf.   [228] K. Simonyan and A. Zisserman, ‘‘Very deep convolutional networks for
      Process. Syst., 2015.                                                               large-scale image recognition,’’ in Proc. ICLR, 2015.
[204] C. Rennie, R. Shome, E. K. Bekris, and F. A. D. Souza, ‘‘A dataset            [229] S. Sivaraman and M. M. Trivedi, ‘‘Looking at vehicles on the road:
      for improved RGBD-based object detection and pose estimation for                    A survey of vision-based vehicle detection, tracking, and behavior
      warehouse pick-and-place,’’ Tech. Rep., 2015.                                       analysis,’’ IEEE Trans. Intell. Transp. Syst., vol. 14, no. 4, pp. 1773–1795,
[205] R. Rios-Cabrera and T. Tuytelaars, ‘‘Discriminatively trained templates             Dec. 2013.
      for 3D object detection: A real time scalable approach,’’ in Proc. IEEE       [230] A. W. M. Smeulders, M. Worring, S. Santini, A. Gupta, and R. Jain,
      Int. Conf. Comput. Vis., Dec. 2013, pp. 2048–2055.                                  ‘‘Content-based image retrieval at the end of the early years,’’ IEEE Trans.
[206] J. Rouillard, ‘‘Contextual QR codes,’’ in Proc. 3rd Int. Multi-Conf.                Pattern Anal. Mach. Intell., vol. 22, no. 12, pp. 1349–1380, Dec. 2000.
      Comput. Global Inf. Technol. (ICCGI), Jul. 2008, pp. 50–55.                   [231] J. Sock, S. H. Kasaei, L. S. Lopes, and T.-K. Kim, ‘‘Multi-view 6D object
[207] D. E. Rumelhart, G. E. Hinton, and R. J. Williams, Learning Internal                pose estimation and camera motion planning using RGBD images,’’ in
      Representations by Error Propagation. Cambridge, MA, USA: MIT                       Proc. IEEE Int. Conf. Comput. Vis. Workshops (ICCVW), Oct. 2017,
      Press, 1986, pp. 318–362.                                                           pp. 2228–2235.
[208] C. Sahin, G. Garcia-Hernando, J. Sock, and T.-K. Kim, ‘‘Instance- and         [232] J. Sock, P. Castro, A. Armagan, G. Garcia-Hernando, and T.-K. Kim,
      category-level 6D object pose estimation,’’ Tech. Rep., 2019.                       ‘‘Tackling two challenges of 6D object pose estimation: Lack of real
[209] C. Sahin, G. Garcia-Hernando, J. Sock, and T.-K. Kim, ‘‘A review on                 annotated RGB images and scalability to number of objects,’’ Tech. Rep.,
      object pose recovery: From 3D bounding box detectors to full 6D pose                Mar. 2020.
      estimators,’’ Tech. Rep., 2020.                                               [233] A. Soltani, H. Haibin, J. Wu, T. Kulkarni, and J. Tenenbaum, ‘‘Synthesiz-
[210] C. Sahin and T.-K. Kim, ‘‘Recovering 6D object pose: A review and                   ing 3D shapes via modeling multi-view depth maps and silhouettes with
      multi-modal analysis,’’ in Computer Vision—ECCV 2018 Workshops,                     deep generative networks,’’ in Proc. Conf. Comput. Vis. Pattern Recognit.,
      L. Leal-Taixé and S. Roth, Eds. Cham, Switzerland: Springer, 2019,                  Jul. 2017, pp. 1511–1519.
      pp. 15–31.                                                                    [234] C. Song, J. Song, and Q. Huang, ‘‘HybridPose: 6D object pose estimation
                                                                                          under hybrid representations,’’ in Proc. IEEE/CVF Conf. Comput. Vis.
[211] H. Sahloul, S. Shirafuji, and J. Ota, ‘‘3D affine: An embedding of local
                                                                                          Pattern Recognit. (CVPR), Jun. 2020.
      image features for viewpoint invariance using RGB-D sensor data,’’
      Sensors, vol. 19, no. 2, p. 291, Jan. 2019, doi: 10.3390/s19020291.           [235] S. Song and J. Xiao, ‘‘Sliding shapes for 3D object detection in
                                                                                          depth images,’’ in Computer Vision—ECCV 2014, D. Fleet, T. Pajdla,
[212] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen,
                                                                                          B. Schiele, and T. Tuytelaars, Eds. Cham, Switzerland: Springer, 2014,
      ‘‘MobileNetV2: Inverted residuals and linear bottlenecks,’’ Tech. Rep.,
                                                                                          pp. 634–651.
      2018.
                                                                                    [236] S. Song and J. Xiao, ‘‘Deep sliding shapes for amodal 3D object detection
[213] S. Savarese and L. Fei-Fei, ‘‘3D generic object categorization, localiza-
                                                                                          in RGB-D images,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit.
      tion and pose estimation,’’ in Proc. IEEE 11th Int. Conf. Comput. Vis.,
                                                                                          (CVPR), Jun. 2016.
      Oct. 2007, pp. 1–8.
                                                                                    [237] X. Song, P. Wang, D. Zhou, R. Zhu, C. Guan, Y. Dai, H. Su, H. Li,
[214] C. Schmid and R. Mohr, ‘‘Local grayvalue invariants for image retrieval,’’
                                                                                          and R. Yang, ‘‘ApolloCar3D: A large 3D car instance understanding
      IEEE Trans. Pattern Anal. Mach. Intell., vol. 19, no. 5, pp. 530–535,
                                                                                          benchmark for autonomous driving,’’ Tech. Rep., 2018.
      May 1997.
                                                                                    [238] X. Song, P. Wang, D. Zhou, R. Zhu, C. Guan, Y. Dai, H. Su, H. Li, and R.
[215] H. Schneiderman and T. Kanade, ‘‘A statistical method for 3D object
                                                                                          Yang, ‘‘ApolloCar3D: A large 3D car instance understanding benchmark
      detection applied to faces and cars,’’ in Proc. Comput. Vis. Pattern
                                                                                          for autonomous driving,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern
      Recognit. (CVPR), vol. 1, Feb. 2000, pp. 746–751.
                                                                                          Recognit. (CVPR), Jun. 2019, pp. 5452–5462.
[216] M. J. Schuster, K. Schmid, C. Brand, and M. Beetz, ‘‘Distributed stereo       [239] M. Sonka, V. Hlavac, and R. Boyle, Image Processing, Analysis, and
      vision-based 6D localization and mapping for multi-robot teams,’’ J. Field          Machine Vision, 2nd ed., no. 3216-7. Boston, MA, USA: Springer, 1993.
      Robot., vol. 36, no. 2, pp. 305–332, Mar. 2019.
                                                                                    [240] G. Spampinato, J. Lidholm, C. Ahlberg, F. Ekstrand, M. Ekstrom,
[217] M. Schwarz, H. Schulz, and S. Behnke, ‘‘RGB-D object recognition                    and L. Asplund, ‘‘An embedded stereo vision module for 6D pose
      and pose estimation based on pre-trained convolutional neural network               estimation and mapping,’’ in Proc. IEEE/RSJ Int. Conf. Intell. Robots
      features,’’ in Proc. IEEE Int. Conf. Robot. Autom. (ICRA), May 2015.                Syst., Sep. 2011, pp. 1626–1631.
[218] P. Sermanet, D. Eigen, X. Zhang, M. Mathieu, R. Fergus, and A.                [241] M. Sundermeyer, Z.-C. Marton, M. Durner, M. Brucker, and A. Triebel,
      LeCun, ‘‘OverFeat: Integrated recognition, localization and detection               ‘‘Implicit 3D orientation learning for 6D object detection from RGD
      using convolutional networks,’’ Tech. Rep., 2013.                                   images,’’ in Proc. CVPR, 2019.
[219] L. G. Shapiro and G. C. Stockman, Computer Vision. Upper Saddle River,        [242] C. Szegedy, S. Ioffe, V. Vanhoucke, and A. Alemi, ‘‘Inception-v4,
      NJ, USA: Prentice-Hall, 2001.                                                       inception-resnet and the impact of residual connections on learning,’’ in
[220] L. G. Shapiro and G. C. Stockman, Computer Vision. London, U.K.:                    Proc. CVPR, 2016.
      Pearson, 2001.                                                                [243] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, D. Erhan,
[221] S. Shi, C. Guo, L. Jiang, Z. Wang, J. Shi, X. Wang, and A. Li, ‘‘PV-                V. Vanhoucke, and A. Rabinovich, ‘‘Going deeper with convolutions,’’
      RCNN: Point-voxel feature set abstraction for 3D object detection,’’ in             Tech. Rep., 2014.
      Proc. Comput. Vis. Pattern Recognit., 2019.                                   [244] C. Szegedy, S. Reed, D. Erhan, D. Anguelov, and S. Ioffe, ‘‘Scalable,
[222] S. Shi, L. Jiang, J. Deng, Z. Wang, C. Guo, J. Shi, X. Wang, and H. Li,             high-quality object detection,’’ 2014, arXiv:1412.1441. [Online]. Avail-
      ‘‘PV-RCNN++: Point-voxel feature set abstraction with local vector                  able: http://arxiv.org/abs/1412.1441
      representation for 3D object detection,’’ Tech. Rep., 2021.                   [245] A. Taeihagh and H. S. M. Lim, ‘‘Governing autonomous vehicles:
[223] J. Shotton, B. Glocker, C. Zach, S. Izadi, A. Criminisi, and A. Fitzgibbon,         Emerging responses for safety, liability, privacy, cybersecurity, and
      ‘‘Scene coordinate regression forests for camera relocalization in RGB-D            industry risks,’’ Transp. Rev., vol. 39, no. 1, pp. 103–128, Jul. 2019.
      images,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., Jun. 2013.      [246] J. Taylor, J. Shotton, T. Sharp, and A. Fitzgibbon, ‘‘The vitruvian
[224] A. Shrivastava, R. Sukthankar, J. Malik, and A. Gupta, ‘‘Beyond skip                manifold: Inferring dense correspondences for one-shot human pose
      connections: Top-down modulation for object detection,’’ in Proc. CVPR,             estimation,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit.,
      2016.                                                                               Jun. 2012.
[225] J. Shuttleworth, ‘‘Automated driving levels of driving automation are         [247] A. Tejani, D. Tang, R. Kouskouridas, and T.-K. Kim, ‘‘Latent-class
      defined in new SAE international standard j3016,’’ SAE Int. J3016, 2018,            Hough forests for 3D object detection and pose estimation,’’ in Computer
      p. 2.                                                                               Vision—ECCV 2014, D. Fleet, T. Pajdla, B. Schiele, T. Tuytelaars, Eds.
[226] N. Silberman, D. Hoiem, P. Kohli, and R. Fergus, ‘‘Indoor segmentation              Cham, Switzerland: Springer, 2014, pp. 462–477.
      and support inference from rgbd images,’’ in Computer Vision—ECCV             [248] B. Tekin, S. N. Sinha, and P. Fua, ‘‘Real-time seamless single shot 6D
      2012, A. Fitzgibbon, S. Lazebnik, P. Perona, Y. Sato, and C. Schmid, Eds.           object pose prediction,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern
      Berlin, Germany: Springer, 2012, pp. 746–760.                                       Recognit., Jun. 2018.

143768                                                                                                                                                 VOLUME 9, 2021
S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

[249] D. Tomè, F. Monti, L. Baroffio, L. Bondi, M. Tagliasacchi, and S. Tubaro,      [274] Y. Xiang, R. Mottaghi, and S. Savarese, ‘‘Beyond Pascal: A benchmark
      ‘‘Deep convolutional neural networks for pedestrian detection,’’ Signal              for 3D object detection in the wild,’’ in Proc. IEEE Winter Conf. Appl.
      Process., Image Commun., vol. 47, pp. 482–489, Sep. 2016.                            Comput. Vis. (WACV), Mar. 2014, pp. 75–82.
[250] J. Tremblay, T. To, and S. Birchfield, ‘‘Falling things: A synthetic dataset   [275] Y. Xiang and S. Savarese, ‘‘Estimating the aspect layout of object
      for 3D object detection and pose estimation,’’ in Proc. IEEE/CVF Conf.               categories,’’ in Proc. IEEE Conf. Comput. Vis. Pattern Recognit.,
      Comput. Vis. Pattern Recognit. Workshops (CVPRW), Jun. 2018.                         Jun. 2012, pp. 3410–3417.
[251] J. Tremblay, T. To, B. Sundaralingam, Y. Xiang, D. Fox, and A. Birchfield,     [276] Y. Xiang, T. Schmidt, V. Narayanan, and D. Fox, ‘‘PoseCNN: A
      ‘‘Deep object pose estimation for semantic robotic grasping of household             convolutional neural network for 6D object pose estimation in cluttered
      objects,’’ Tech. Rep., 2018.                                                         scenes,’’ in Proc. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2018.
[252] I. Tsochantaridis, T. Hofmann, T. Joachims, and Y. Altun, ‘‘Support            [277] X. Mao, D. Inoue, S. Kato, and M. Kagami, ‘‘Amplitude-modulated laser
      vector machine learning for interdependent and structured output spaces,’’           radar for range and speed measurement in car applications,’’ IEEE Trans.
      in Proc. 21st Int. Conf. Mach. Learn. (ICML), New York, NY, USA, 2004,               Intell. Transp. Syst., vol. 13, no. 1, pp. 408–413, Mar. 2012.
      p. 104.                                                                        [278] B. Xu and Z. Chen, ‘‘Multi-level fusion based 3D object detection from
[253] J. R. R. Uijlings, K. E. A. van de Sande, T. Gevers, and                             monocular images,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern
      A. W. M. Smeulders, ‘‘Selective search for object recognition,’’                     Recognit., Jun. 2018, pp. 2345–2353.
      Int. J. Comput. Vis., vol. 104, no. 2, pp. 154–171, Apr. 2013.                 [279] B. Yang, W. Luo, and R. Urtasun, ‘‘PIXOR: Real-time 3D object detection
[254] G. Van Houdt, C. Mosquera, and G. Nápoles, ‘‘A review on the long short-             from point clouds,’’ Tech. Rep., 2019.
      term memory model,’’ Artif. Intell. Rev., vol. 53, no. 8, pp. 5929–5955,       [280] Y. You, Y. Wang, W.-L. Chao, D. Garg, G. Pleiss, B. Hariharan,
      Dec. 2020.                                                                           M. Campbell, and K. Q. Weinberger, ‘‘Pseudo-LiDAR++: Accurate
[255] J. Vidal, C.-Y. Lin, X. Lladó, and R. Martí, ‘‘A method for 6D pose                  depth for 3D object detection in autonomous driving,’’ Tech. Rep., 2019.
      estimation of free-form rigid objects using point pair features on range       [281] H. Yuan, T. Hoogenkamp, and R. C. Veltkamp, ‘‘RobotP: A benchmark
      data,’’ Sensors, vol. 18, no. 8, p. 2678, Aug. 2018.                                 dataset for 6D object pose estimation,’’ Sensors, vol. 21, no. 4, p. 1299,
[256] J. Vidal, C.-Y. Lin, and R. Marti, ‘‘6D pose estimation using an improved            Feb. 2021.
      method based on point pair features,’’ in Proc. 4th Int. Conf. Control,        [282] S. Zakharov, I. Shugurov, and S. Ilic, ‘‘DPOD: 6D pose object detector
      Autom. Robot. (ICCAR), Apr. 2018, pp. 405–409.                                       and refiner,’’ Tech. Rep., 2019.
[257] D. Wagner, G. Reitmayr, A. Mulloni, T. Drummond, and D. Schmalstieg,           [283] S. Zakharov, I. Shugurov, and S. Ilic, ‘‘DPOD: 6d pose object detector
      ‘‘Pose tracking from natural features on mobile phones,’’ in Proc. 7th               and refiner,’’ Tech. Rep., 2019.
      IEEE/ACM Int. Symp. Mixed Augmented Reality, Sep. 2008, pp. 125–134.           [284] M. D. Zeiler and R. Fergus, ‘‘Visualizing and understanding convolu-
[258] C. Wang, D. Xu, Y. Zhu, R. Martín-Martín, C. Lu, L. Fei-Fei, and                     tional networks,’’ Tech. Rep., 2013.
      S. Savarese, ‘‘Densefusion: 6D object pose estimation by iterative dense       [285] M. D. Zeiler, D. Krishnan, G. W. Taylor, and R. Fergus, ‘‘Deconvolutional
      fusion,’’ Tech. Rep., 2019.                                                          networks,’’ in Proc. IEEE Comput. Soc. Conf. Comput. Vis. Pattern
[259] C.-Y. Wang, I.-H. Yeh, and H.-Y. M. Liao, ‘‘You only learn one                       Recognit., Jun. 2010, pp. 2528–2535.
      representation: Unified network for multiple tasks,’’ Tech. Rep., 2021.        [286] H. Zhang and Q. Cao, ‘‘Fast 6D object pose refinement in depth images,’’
[260] D. Z. Wang and I. Posner, ‘‘Voting for voting in online point cloud object           Int. J. Speech Technol., vol. 49, no. 6, pp. 2287–2300, Jun. 2019.
      detection,’’ in Robotics: Science and Systems. 2015.                           [287] S. Zhang, L. Wen, X. Bian, Z. Lei, and Z. S. Li, ‘‘Single-shot refinement
[261] H. Wang, S. Sridhar, J. Huang, J. Valentin, S. Song, and J. L. Guibas,               neural network for object detection,’’ Tech. Rep., 2017.
      ‘‘Normalized object coordinate space for category-level 6D object pose         [288] T. Zhang, Y. Yang, Y. Zeng, and Y. Zhao, ‘‘Cognitive template-clustering
      and size estimation,’’ Tech. Rep., 2019.                                             improved LINEMOD for efficient multi-object pose estimation,’’ Cognit.
[262] Z. Tian, C. Shen, H. Chen, and T. He, ‘‘FCOS: Fully convolutional                    Comput., pp. 1–10, Mar. 2020.
      one-stage object detection,’’ in Proc. IEEE/CVF Int. Conf. Comput. Vis.        [289] X. Zhang, Z. Jiang, and H. Zhang, ‘‘Real-time 6D pose estimation
      (ICCV), Oct. 2019.                                                                   from a single RGB image,’’ Image Vis. Comput., vol. 89, pp. 1–11,
[263] X. Wang, W. Yin, T. Kong, Y. Jiang, L. Li, and C. Shen, ‘‘Task-aware                 Sep. 2019.
      monocular depth estimation for 3D object detection,’’ Tech. Rep., 2019.        [290] X. Zhang, Z. Jiang, and H. Zhang, ‘‘Out-of-region keypoint localization
[264] Y. Wang, W.-L. Chao, D. Garg, B. Hariharan, M. Campbell, and                         for 6D pose estimation,’’ Image Vis. Comput., vol. 93, Jan. 2020,
      Q. K. Weinberger, ‘‘Pseudo-LiDAR from visual depth estimation: Bridg-                Art. no. 103854.
      ing the gap in 3D object detection for autonomous driving,’’ Tech. Rep.,       [291] Y. Zhang, H. Zhang, G. Wang, J. Yang, and J.-N. Hwang, ‘‘Bundle
      2018.                                                                                adjustment for monocular visual odometry based on detections of traffic
[265] X. Weng and K. Kitani, ‘‘Monocular 3D object detection with pseudo-                  signs,’’ IEEE Trans. Veh. Technol., vol. 69, no. 1, pp. 151–162, Jan. 2020.
      lidar point cloud,’’ Tech. Rep., 2019.                                         [292] Y. Zhang, D. Huang, and Y. Wang, ‘‘PC-RGNN: Point cloud completion
[266] H. D. Whyte and T. Bailey, ‘‘Simultaneous localization and mapping,’’                and graph neural network for 3D object detection,’’ in Proc. CVPR, 2020.
      IEEE Robot. Autom. Mag., vol. 13, no. 2, pp. 99–110, Jun. 2006.                [293] J. Zhao, B. Liang, and Q. Chen, ‘‘The key technology toward the self-
[267] K. Wiggers, ‘‘Facebook highlights AI that converts 2D objects into 3D                driving car,’’ Int. J. Intell. Unmanned Syst., vol. 6, no. 1, pp. 2–20,
      shapes,’’ Online Blog, Oct. 2019.                                                    Jan. 2018.
[268] K. Wiggers, ‘‘Google brings cross-platform AI pipeline framework,’’            [294] Z.-Q. Zhao, H. Bian, D. Hu, W. Cheng, and H. Glotin, ‘‘Pedestrian
      Tech. Rep., Jan. 2020.                                                               detection based on fast R-CNN and batch normalization,’’ in Proc. Intell.
[269] D. Wu, Z. Zhuang, C. Xiang, W. Zou, and X. Li, ‘‘6D-VNet: End-to-end                 Comput. Theories Appl. (ICIC), Jul. 2017, pp. 735–746.
      6DoF vehicle pose estimation from monocular RGB images,’’ in Proc.             [295] Z.-Q. Zhao, P. Zheng, S. T. Xu, and X. Wu, ‘‘Object detection with deep
      IEEE/CVF Conf. Comput. Vis. Pattern Recognit. Workshops (CVPRW),                     learning: A review,’’ Tech. Rep., 2018.
      Jun. 2019.                                                                     [296] Z. Cao, Y. Sheikh, and N. K. Banerjee, ‘‘Real-time scalable 6DOF pose
[270] Z. Wu, X. Wang, Y.-G. Jiang, H. Ye, and X. Xue, ‘‘Modeling                           estimation for textureless objects,’’ in Proc. IEEE Int. Conf. Robot. Autom.
      spatial-temporal clues in a hybrid deep learning framework for video                 (ICRA), May 2016, pp. 2441–2448.
      classification,’’ Tech. Rep., 2015.                                            [297] W. Zheng, W. Tang, S. Chen, L. Jiang, and C.-W. Fu, ‘‘CIA-SSD:
[271] Y. Xiang, W. Choi, Y. Lin, and S. Savarese, ‘‘Data-driven 3D voxel                   Confident IoU-aware single-stage object detector from point cloud,’’ in
      patterns for object category recognition,’’ in Proc. IEEE Conf. Comput.              Proc. CVPR, 2020.
      Vis. Pattern Recognit. (CVPR), Jun. 2015, pp. 1903–1911.                       [298] W. Zheng, W. Tang, L. Jiang, and C.-W. Fu, ‘‘SE-SSD: Self-ensembling
[272] Y. Xiang, W. Choi, Y. Lin, and S. Savarese, ‘‘Subcategory-aware                      single-stage object detector from point cloud,’’ in Proc. CVPR, 2021.
      convolutional neural networks for object proposals and detection,’’            [299] Z. Yang and R. Nevatia, ‘‘A multi-scale cascade fully convolutional
      Tech. Rep., 2016.                                                                    network face detector,’’ in Proc. 23rd Int. Conf. Pattern Recognit. (ICPR),
[273] Y. Xiang, W. Kim, W. Chen, J. Ji, C. Choy, H. Su, R. Mottaghi, L. Guibas,            Dec. 2016, pp. 633–638.
      and S. Savarese, ‘‘ObjectNet3D: A large scale database for 3D object           [300] Y. Zhong, ‘‘Intrinsic shape signatures: A shape descriptor for 3D object
      recognition,’’ in Proc. Eur. Conf. Comput. Vis., vol. 9912, Oct. 2016,               recognition,’’ in Proc. IEEE 12th Int. Conf. Comput. Vis. Workshops
      pp. 160–176.                                                                         (ICCV Workshop), Sep. 2009, pp. 689–696.

VOLUME 9, 2021                                                                                                                                                143769
                                                                                        S. Hoque et al.: Comprehensive Review on 3DOD and 6DPE With DL

[301] D. Zhou, Y. Dai, and H. Li, ‘‘Ground-plane-based absolute scale                                     SHUXIANG XU received the bachelor’s degree
      estimation for monocular visual odometry,’’ IEEE Trans. Intell. Transp.                             in applied mathematics from the University of
      Syst., vol. 21, no. 2, pp. 791–802, Feb. 2019.                                                      Electronic Science and Technology of China,
[302] D. Zhou, J. Fang, X. Song, L. Liu, J. Yin, Y. Dai, H. Li, and R. Yang,                              China, in 1986, the master’s degree in applied
      ‘‘Joint 3D instance segmentation and object detection for autonomous                                mathematics from Sichuan Normal University,
      driving,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit.                                   China, in 1989, and the Ph.D. degree in comput-
      (CVPR), Jun. 2020, pp. 1836–1846.                                                                   ing from Western Sydney University, Australia,
[303] T. Zhou, M. Brown, N. Snavely, and D. G. Lowe, ‘‘Unsupervised learning
                                                                                                          in 2000. He is currently working as a Lecturer
      of depth and ego-motion from video,’’ in Proc. IEEE Conf. Comput. Vis.
                                                                                                          and a Ph.D. Student Supervisor with the Discipline
      Pattern Recognit. (CVPR), Jul. 2017, pp. 6612–6619.
[304] X. Zhou, D. Wang, and P. Krähenbühl, ‘‘Objects as points,’’ Tech. Rep.,                             of Information and Communication Technology,
      2019.                                                                     School of Technology, Environments and Design, University of Tasmania,
[305] X. Zhou, J. Zhuo, and P. Krähenbühl, ‘‘Bottom-up object detection by      Australia. Much of his work is focused on developing new machine learning
      grouping extreme and center points,’’ Tech. Rep., 2019.                   algorithms and using them to solve problems in various application fields.
[306] W. Zhu, J. Miao, J. Hu, and L. Qing, ‘‘Vehicle detection in driving       His research interests include artificial intelligence, machine learning, and
      simulation using extreme learning machine,’’ Neurocomputing, vol. 128,    data mining. He received an Overseas Postgraduate Research Award from the
      pp. 160–165, Mar. 2014.                                                   Australian Government, in 1996, to research his Ph.D. degree in computing.

                          SABERA HOQUE received the bachelor’s degree
                          in computer science and engineering from                                        ANANDA MAITI (Member, IEEE) received the
                          Northern University Bangladesh, in 2007, and the                                Ph.D. degree from the University of Southern
                          master’s degree in computer science and engineer-                               Queensland, in 2016. He is currently an Early
                          ing from United International University, in 2017.                              Career Researcher. His current research interests
                          She is currently pursuing the Ph.D. degree with the                             include computer networking, and algorithms
                          School of Information and Communication Tech-                                   along with the Internet-of-Things and its various
                          nology, University of Tasmania, Australia. Her                                  applications in agriculture and remote laborato-
                          research interests include artificial intelligence,                             ries. He is also interested in augmented and virtual
                          machine learning, data mining, image processing,                                reality and their application in e-learning.
                          and software development.

                          MD. YASIR ARAFAT received the bachelor’s
                          degree in computer science and engineering from                                 YUCHEN WEI received the B.E. degree in
                          Northern University Bangladesh, in 2007, and                                    information engineering from China University of
                          the master’s degree in computer science and                                     Mining and Technology, Xuzhou, China, in 2012,
                          engineering from United International University,                               and the M.Sc. degree from Tongji University,
                          in 2017. Throughout his career, he has been                                     Shanghai, China, in 2015. He is currently pursuing
                          working as a Software Engineer. He is currently                                 the Ph.D. degree with the School of Technology,
                          working as a Lead Developer at Bundle Australia                                 Environments and Design, University of Tasma-
                          Pty Ltd. His research interests include artificial                              nia. His research interests include artificial intel-
                          intelligence, machine learning, data mining, image                              ligence, machine learning, and image processing.
                          processing, and software development.

143770                                                                                                                                         VOLUME 9, 2021
