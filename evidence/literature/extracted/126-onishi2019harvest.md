---
source_id: 126
bibtex_key: onishi2019harvest
title: An Automated Fruit Harvesting Robot by Using Deep Learning
year: 2019
domain_theme: Uncoded
verified_pdf: 126_Automated Fruit Harvesting Robot (Onishi dkk.).pdf
char_count: 38176
---

Onishi et al. Robomech J    (2019) 6:13
https://doi.org/10.1186/s40648-019-0141-2

 RESEARCH ARTICLE                                                                                                                               Open Access

An automated fruit harvesting robot
by using deep learning
Yuki Onishi1*, Takeshi Yoshida2, Hiroki Kurita2, Takanori Fukao3, Hiromu Arihara4 and Ayako Iwai4

  Abstract
  Automation and labor saving in agriculture have been required recently. However, mechanization and robots for
  growing fruits have not been advanced. This study proposes a method of detecting fruits and automated harvesting
  using a robot arm. A highly fast and accurate method with a Single Shot MultiBox Detector is used herein to detect
  the position of fruit, and a stereo camera is used to detect the three-dimensional position. After calculating the angles
  of the joints at the detected position by inverse kinematics, the robot arm is moved to the target fruit’s position. The
  robot then harvests the fruit by twisting the hand axis. The experimental results showed that more than 90% of the
  fruits were detected. Moreover, the robot could harvest a fruit in 16 s.
  Keywords: Harvesting fruits, Robot, Manipulation, Deep learning

Background                                                                            fruit as an object is difficult. When a thermal camera
The agriculture industry has many problems, including                                 is used [3], the fruit is detected based on the tempera-
the decreasing number of farm workers and increasing                                  ture difference between the fruit and the background.
cost of fruit harvesting. Saving labor and scale up in agri-                          This method is affected by the fruit size and exposure to
culture is necessary in solving these problems. In recent                             direct sunlight. Various different features are used in fruit
years, the automation of agriculture has been advancing                               detection using color camera. Bulanon et al. [4, 5] used
for labor saving and large-scale agriculture. However,                                luminance and red, green, and blue (RGB) color differ-
much of the work in the field of fruit harvesting is manu-                            ence to segment an apple. Rakun et al. [6] used texture
ally done. The development of an automated fruit har-                                 analysis to detect an apple. Linker et al. [7] integrated
vesting robot is a viable solution to these problems. The                             multiple features to improve the accuracy of fruit detec-
automatic harvesting of fruits by a robot involves two big                            tion methods. Various image classification methods for
tasks: (1) fruit detection and localization on trees using                            fruit detection can also be performed using a color cam-
computer vision with a sensor and (2) robot arm motion                                era. Bulanon et al. [8] used K-mean clustering for apple
to the position of the detected fruit and fruit harvesting                            detection. Linker et al. [7] and Cohen et al. [9] used
by the end effector without damaging target fruit and its                             KNN clustering for apple classification. In addition, Kur-
tree.                                                                                 tulmus et al. [10] used an Artificial Neural Network for
  The fruit detection and localization on trees using com-                            apple classification. Qiang et al. [11] used a Support Vec-
puter vision have been investigated in numerous studies,                              tor Machine classification method for apple detection.
and most of these have been summarized in the review of                               However, these methods are difficult to use in variable
Gongal et al. [1]. Color, spectral, or thermal cameras have                           light conditions because the color information cannot
been widely used in these methods. When using spec-                                   be sufficiently acquired. For better accuracy, fruit detec-
tral camera [2], detecting the fruit shadowed by another                              tion should be performed using multiple features such
                                                                                      as color, shape, texture, and reflection to overcome chal-
                                                                                      lenges like clustering and variable light conditions.
*Correspondence: re0069hi@ed.ritsumei.ac.jp                                              The present study proposes “fruit detection and locali-
1
  Graduate School of Science and Engineering, Ritsumeikan University,                 zation” and “fruit harvesting by a robot manipulator
1‑1‑1, Noji‑higashi, Kusatsu 525‑8577, Shiga, Japan                                   with a hand which is able to harvest without damaging
Full list of author information is available at the end of the article

                                         © The Author(s) 2019. This article is distributed under the terms of the Creative Commons Attribution 4.0 International License
                                         (http://creat​iveco​mmons​.org/licen​ses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium,
                                         provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license,
                                         and indicate if changes were made.
Onishi et al. Robomech J   (2019) 6:13                                                                         Page 2 of 8

the fruit and its tree” to perform automatic fruit har-
vesting by a robot. We used a color camera and a Single
Shot MultiBox Detector (SSD) [12] to detect the two-
dimensional (2D) position of the fruit. The SSD is one
of the general object detection methods that use Con-
volution Neural Network (CNN) [13]. The SSD can
comprehensively judge from color and shape. A three-
                                                                Fig. 2 Flow chart for harvest of apple
dimensional (3D) position must be obtained to send a
command to the robot arm. A stereo camera is used to
measure the 3D position of the fruit detected by the SSD.      detecting the 2D position of the apple, detecting 3D
We used inverse kinematics to calculate the route of the       position of the apple, and calculating the inverse kine-
robot arm. We moved the robot arm to the fruit posi-           matics. These steps were divided into the detection and
tion based on inverse kinematics. We used the harvesting       harvest parts. We explain each method in the sections
robot hand as the end effector. The robot hand harvests a      that follow.
fruit by gripping and rotating it without damaging it and
its tree.
                                                               Fruit position detection method
Methods
                                                               The first step of the detection part was detecting the
We describe each step in our fruit detection and harvest
                                                               2D position of the fruit. We received one image from
method in this section.
                                                               the stereo camera and detected where apples were in
                                                               the received image. We used the SSD [12] to detect the
Apple and tree
                                                               apple positions.
The fruit used in this research is the “Fuji” apple culti-
                                                                 The SSD is a method based on the CNN [13], which
vated in the Miyagi Prefectural Agriculture and Horti-
                                                               detects objects in an image using a single deep neu-
culture Research Center. However, our method can also
                                                               ral network. The other detection methods are Faster
be applied to other apple varieties. A pear has a relatively
                                                               R-CNN [15], and You Only Look Once [16], among
similar shape to an apple; hence, this algorithm is also
                                                               others. The first step of the SSD is the usage of the VGG
considered effective for pears. We used herein a joint
                                                               net to extract the feature maps. The core of the SSD
V-shaped apple tree [14]. The V-shaped tree shape was
                                                               predicts the category scores and the box offsets for a
suitable for mechanization and efficiency, and its fruits
                                                               fixed set of default bounding boxes using small convo-
can be easily harvested. Figure 1 shows the tree used
                                                               lutional filters applied to the feature maps. To achieve
herein.
                                                               high detection accuracy, the SSD produces predictions
                                                               of different scales from feature maps of different scales,
Detection and harvest algorithm
                                                               and explicitly separates predictions by aspect ratio.
The harvest robot was equipped with a stereo camera
                                                               These design features lead to simple end-to-end train-
and a robot arm. Figure 2 presents the detection and
                                                               ing and high accuracy even on low resolution input
harvest algorithm. The algorithm involves three steps:
                                                               images, and improving the speed vs accuracy trade-off.
                                                               We used the SSD herein because it is superior in speed
                                                               and accuracy to others. The SSD was 59 FPS with mAP
                                                               74.3% on the VOC2007 test on a Nvidia Titan X. Faster
                                                               R-CNN was 7 FPS with mAP 73.2%. YOLO was 45 FPS
                                                               with mAP 63.4%. We can detect bounding boxes at the
                                                               2D apple positions in the image using the SSD.
                                                                 For fruits detected by the SSD, we selected a fruit that
                                                               was nearest the robot arm. We received a point cloud
                                                               data from the stereo camera and the pixel at the selected
                                                               2D apple position. We used the stereo camera to do a
                                                               3D reconstruction. The 3D reconstruction by the stereo
                                                               camera was performed by a triangulation from parallax
                                                               between the right and left images to obtain the 3D posi-
                                                               tion of the pixel in the image. We can then measure the
                                                               distance from the stereo camera to the apple.
 Fig. 1 Apple tree
Onishi et al. Robomech J   (2019) 6:13                                                                                      Page 3 of 8

Table 1 Denavit–Hartenberg parameters for UR3
Link            ai (m)         αi (rad)    di (m)               θi
                               π
1               0              2           0.1519               θ1
2               −0.24365       0           0                    θ2
3               −0.21325       0           0                    θ3
                               π
4               0              2           0.11235              θ4
5               0              − π2        0.08535              θ5
6               0              0           0.08190              θ6

                                                                      Fig. 3 UR3 Image [18]
Table 2 UR3 specifications
Weight capacity                                      3 (kg)

Reach                                                500 (mm)
Degree of freedom                                    6
Weight                                               11 (kg)
Repeatability                                        ± 0.1 (mm)

Fruit harvesting method by the robot arm
Position p and posture R of the hand must be moved
to as specified harvest the fruit using the robot hand
attached to the robot arm. In the case of a vertically
articulated robot arm, the position and posture of the
hand ( p, R ) are determined by the angles q of each                  Fig. 4 UR3 Denavit Hartenberg parameters diagrams
joint. Therefore, the relationship between the joint
coordinate system representing the joint angle of the
robot arm and the hand coordinate system representing                posture R(φ, θ, ψ) of the hand for Eq. (1). The rotation
the position and posture of the hand must be clarified.              matrix R is expressed as
  The problem of determining the angles q of each joint
from the hand position p and posture R is called an                   R(φ, θ, ψ)
inverse kinematics problem [17]. The inverse kinemat-
                                                                                                                                    
                                                                              Cφ Cθ      Cφ Sθ Sψ − Sθ Cψ       C φ S θ C ψ + Sθ S ψ
ics problem aims to find a nonlinear function f −1 for                  =  Sφ Cθ        Sφ Sθ Sψ + Cθ Cψ       Sφ Sθ Cψ − Cθ Sψ ,
the equation Eq. (1) is determined by the robot arm                            −Sθ              Cθ Sψ                   Cθ Cψ
mechanism and configuration.
                                                                                                                                   (2)
        q = f −1 (p, R).                                       (1)   where we used the abbreviations of Sx = sin x, and
                                                                     Cx = cos x.
Inverse kinematics model                                               The Denavit–Hartenberg notation [17] is the relationship
We considered that the inverse kinematic problem                     between links i and i + 1. The homogeneous transforma-
of the robot arm had six links. We used UR3 made by                  tion matrix of the Denavit–Hartenberg notation is
UNIVERSAL ROBOTS as the robot arm. UR3 has six
                                                                                       Cθn   −Sθn Cαn    Sθn Sαn     rn Cθn
                                                                                                                           
degrees of freedom; thus, arbitrary position and pos-
                                                                                     S       Cθn Cαn   −Cθn Sαn     rn Sθn 
ture can be expressed as long as they are within the                      n−1
                                                                              T n =  θn                                      ,
                                                                                        0       S αn      C αn         dn 
operating range. Table 1 shows the Denavit–Harten-                                      0        0          0           1
berg parameter of UR3. Table 2 presents the UR3 speci-                                                                       (3)
fication. Figure 3 displays the UR3 used herein. The
                                                                     where we used the abbreviation of Sx = sin x, and
Denavit–Hartenberg parameters in UR3 are described
                                                                     Cx = cos x.
in Fig. 4.
                                                                       We can obtain Eq. (4) from the relationship between the
   We obtain the angles q = θi (i = 1, 2, . . . , 6) of each
                                                                     robot arm Denavit–Hartenberg notation 0 T 6 and the hand
joint when we are given the position p(px , py , pz ) and
                                                                     position p and posture R
Onishi et al. Robomech J      (2019) 6:13                                                                                         Page 4 of 8

                                R11            R12     R13
                                                       px
                                                         
                    �          �
                      R p      R               R22     R23
                                                       py 
        0
          T 6 (q) =         =  21                          .
                              
                    0 0 0 1    R31             R32     R33
                                                       pz 
                                 0              0      10
                                                           (4)
With Eq. (4), the angle θi of each joint of the robot arm
can be obtained as follows, but first, θ1 is presented as
                  �             �
                    py − d6 R23
     A1 = arctan                   ,
                    px − d6 R13
                                                         
                                      d4
     B1 = arccos  �                                      ,
                       (px − d6 R13 ) + (py − d6 R23 )2
                                      2

                       π                                                    Fig. 5 Example of apple image
     θ1 = A1 ± B1 + .
                       2
                                                           (5)
                                                                          Table 3 SSD learning parameters
θ5 is denoted as follows                                                  Architecture                             Caffe

        A5 = px sin θ1 − py cos θ1 − d4 ,                                 Net                                      VGG-16
                                                                          Image (trainval)                         200 images (1081 apples)
                                                                   (6)
                         
                          A5
        θ5 = ± arccos         .                                           Image (test)                             50 images (259 apples)
                          d6
                                                                          Base learning rate                       0.0001
                                                                          Batch size                               4
where sin θ5 = 0, θ6 is
                                                                          Learning times                           10,000 steps

        A6 = (R12 − R11 ) sin θ1 + (R22 − R21 ) cos θ1 ,
                           �                   
             π               ± 2 sin2 θ5 − A26                     (7)            A2 = a3 cos θ3 + a2 ,
        θ6 = − arctan                          .
              4                      A6                                           B2 = a3 sin θ3 ,
                                                                                  C2 = pz − d1 + d6 sin θ234 sin θ5 + d5 cos θ234 ,
                                                                                                                  �                  
                                                                                                                       A 2 + B2 − C 2
If θ234 = θ2 + θ3 + θ4 , θ234 is denoted as
                                                                                               � �
                                                                                                   A2                    2     2    2
                                                                                  θ2 = arctan           − arctan ±                   .
                                                                                                   B2                       C2
        A234 = cos θ5 cos θ6 ,
        B234 = sin θ6 ,                                                                                                                (10)
        C234 = R11 cos θ1 + R21 sin θ1 ,
                                                                   (8)    θ4 is
        D234 = R31 ,
                        
                          A234 D234 − B234 C234
                                                                              θ4 = θ234 − θ2 − θ3 .                            (11)
        θ234 = arctan
                          A234 C234 + B234 D234
                                                 .                        We can calculate the angles q of each joint from the hand
                                                                          position p and posture R by inverse kinematics.

θ3 is                                                                     Results and discussion
                                                                          Fruit position detection
        A3 = px cos θ1 + py sin θ1 + d6 cos θ234 sin θ5 − d5 sin θ234 ,
                                                                          This describes the result of the fruit position detection.
        B3 = pz − d1 + d6 sin θ234 sin θ5 + d5 cos θ234 ,
                                                                          The images taken at Miyagi Prefectural Agriculture and
                      A3 2 + B3 2 − a2 2 − a3 2                           Horticulture Research Center were used for learning and
        θ3 = arccos                               .
                               2a2 a3                                     testing. Shooting was performed to look at the fruit from
                                                                   (9)    below considering the minimized occlusion by the leaves,
                                                                          branches and other fruits. Figure 5 depicts the image
θ2 is
                                                                          taken by this method. We used the learning parameters
                                                                          shown in Table 3.
Onishi et al. Robomech J       (2019) 6:13                                                                     Page 5 of 8

 Fig. 6 Example of test image1                                  Fig. 9 Result of detection2

                                                              Table 4 Result of the apple position detection

                                                              Total                                                169
                                                              Detected apples                                      156
                                                              Undetected apples                                    13
                                                              Falsely detected apples                              0
                                                              Precision                                            100%
                                                              Recall                                               92.31%

 Fig. 7 Example of test image2

                                                                Fig. 10 Harvest robot

                                                              images. Figures 8 and 9 show the test image result. The
                                                              model can detect even if the fruits are partially occluded
 Fig. 8 Result of detection1                                  by other fruits and leaves. However, the fruits at the edge
                                                              of the image and those far from the camera could not be
                                                              detected. The edge of the image could not be detected
  We tested whether fruits can be detected using              because the fruits were cut off in the image. The fruits
unlearned images taken in the orchard using the learned       far from the camera could not be detected because they
model. We surrounded the area where the possibility of        had become smaller in the image. However, this was not
fruit was 60% or more with a red frame. We detected           a problem herein because these fruits were out of reach
the presence of an apple to be tested from 30 images          of the robot arm. Table 4 presents this test result.
with 169 apples in total. Figures 6 and 7 depict the tested
Onishi et al. Robomech J     (2019) 6:13                                                                         Page 6 of 8

Table 5 ZED specification
Output resolution                              3840 × 1080

Frames per second                              30
Depth range                                    0.5–20 (m)
Base line                                      120 (mm)

                                                               Fig. 12 Detection of two-dimensional position

  Fig. 11 Apple tree model

Harvesting robot
Figure 10 displays the harvesting robot used herein. We
conducted fruit harvesting using this robot with a stereo
camera installed at approximately 0.5 (m) below the base
of the robot arm such that the fruit tree is looked up from
                                                               Fig. 13 Detection of three-dimensional position
directly below. If the distance to the target fruit is too
long and the robot arm cannot reach the target, the table
lift on which all equipment rides goes up and down, mov-
ing to the distance where the arm can reach.
   We use UR3 (UNIVERSAL ROBOTS) as the robot arm.
Table 2 shows the robot repeatability is ± 0.1 (mm). The
robot palm diameter was 5 cm; hence, even if an error
occurs, it can be suppressed by the robot hand. We used
ZED (STEREO LABS) as the stereo camera, with specifi-
cations shown in Table 5.

Fruit automated harvest
We describe the automated apple harvesting in this sec-
tion. Figure 11 illustrates the experimented tree and a
model of the apple tree at the Miyagi Prefectural Agricul-
ture and Horticultural Research Center. These trees were       Fig. 14 Approching target apple
joint V-shaped trees [14] like those in the Miyagi Pre-
fectural Agricultural and Horticultural Research Center.
                                                              SSD. We used a learning model that can detect more than
Conducting the experiment during apple harvest time
                                                              90% of the fruits used (fruit position detection section).
was difficult; hence, we experimented with a tree model.
                                                              We surrounded the area where the possibility of fruit
  The results of the automated fruit harvesting experi-
                                                              was 60% or more, with a red frame. The robot was able
ments are presented herein along with the detection unit
                                                              to detect the apples the same as the real ones; hence, it
of the harvesting robot. First, we detected the 2D fruit
                                                              seemed enough for the experiment.
position. Figure 12 shows the fruit detection result by the
Onishi et al. Robomech J    (2019) 6:13                                                                                         Page 7 of 8

                                                              Conclusions
                                                              In this study, we performed automatic fruit harvesting
                                                              through the method of fruit position detection and har-
                                                              vesting using a robot manipulator with a harvesting hand
                                                              that does not damage the fruit and its tree. Using the
                                                              SSD, we showed that the fruit position of 90% or more
                                                              can be detected in 2 s. The proposed fruit harvesting
                                                              algorithm also showed that one fruit can be harvested in
                                                              approximately 16 s.
                                                                The fruit harvesting algorithm proposed herein is
                                                              expected to be applicable even if it is a near species of
                                                              apple. Moreover, if one learns again with the target fruit,
                                                              harvesting fruits, such as pears is highly possible.
 Fig. 15 Harvesting target apple

                                                              Abbreviations
                                                              SSD: Single Shot MultiBox Detector; CNN: Convolution Neural Network.

                                                              Acknowledgements
                                                              This research was supported by grants from the Project of the Bio-oriented
                                                              Technology Research Advancement Institution, NARO (the research project for
                                                              the future agricultural production utilizing artificial intelligence).

                                                              Authors’ contributions
                                                              YO conducted all research and experiments. TY and TF conducted a research
                                                              concept, participated in design adjustment, and drafted a paper draft assis-
                                                              tant. All authors read and approved the final manuscript.

                                                              Competing interests
                                                              The authors declare that they have no competing interests.

                                                              Author details
                                                              1
                                                                Graduate School of Science and Engineering, Ritsumeikan University,
                                                              1‑1‑1, Noji‑higashi, Kusatsu 525‑8577, Shiga, Japan. 2 Research Organiza-
 Fig. 16 Grasping target apple
                                                              tion of Science and Technology, Ritsumeikan University, 1‑1‑1, Noji‑higashi,
                                                              Kusatsu 525‑8577, Shiga, Japan. 3 Department of Electrical and Electronic Engi-
                                                              neering, Ritsumeikan University, 1‑1‑1, Noji‑higashi, Kusatsu 525‑8577, Shiga,
  Second, we measured the 3D fruit position. Figure 13        Japan. 4 DENSO Corporation, 1‑1, Showa‑cho, Kariya 448‑8661, Aichi, Japan.

depicts the 3D position of the center point of the frame      Received: 5 January 2019 Accepted: 10 October 2019
detected by the SSD. The 3D reconstruction of the parts
other than the apples themselves was inadequate, but
in this experiment it is unnecessary except for the bot-
tom surface of the apple. Sufficient results were obtained    References
because we were able to capture the bottom of the apple.      1. Gongal A, Amatya S, Karkee M, Zhang Q, Lewis K (2015) Sensors and
                                                                  systems for fruit detection and localization: a review. Comput Electron
  Next, we will describe the harvesting part of the har-          Agric 116:8–19
vesting robot. To insert the robot hand from the under-       2. Okamoto H, Lee WS (2009) Green citrus detection using hyperspectral
side for fruit harvesting, the robot was first moved              imaging. Comput Electron Agric 66(2):201–208
                                                              3. Stajnko D, Lakota M, Hočevar M (2004) Estimation of number and diam-
10 (cm) below the target fruit (Fig. 14). The arm then rose       eter of apple fruits in an orchard during the growing season by thermal
below the fruit (Fig. 15). The robot hand then grasped the        imaging. Comput Electron Agric 42(1):31–42
fruit and harvesting it by twisting from the peduncle by      4. Bulanon DM, Kataoka T, Ota Y, Hiroma T (2002) Ae-automation and
                                                                  emerging technologies: a segmentation algorithm for the automatic
rotating for four times (Fig. 16).                                recognition of fuji apples at harvest. Biosyst Eng 83(4):405–412
  The harvest time for each fruit was approximately 16 s.     5. Bulanon DM, Kataoka T (2010) Fruit detection system and an end effector
Detecting the fruit position and calculating the joint            for robotic harvesting of fuji apples. Agric Eng Int CIGR J 12(1):203–210
                                                              6. Rakun J, Stajnko D, Zazula D (2011) Detecting fruits in natural scenes by
angle at that position took approximately 2 s. Fruit har-         using spatial-frequency based texture analysis and multiview geometry.
vesting took approximately 14 s. Harvesting consumed              Comput Electron Agric 76(1):80–88
much time because the hand rotated for several times. By      7. Linker R, Cohen O, Naor A (2012) Determination of the number of green
                                                                  apples in rgb images recorded in orchards. Comput Electron Agric
reconsidering these points, speedup is possible.                  81:45–57
Onishi et al. Robomech J          (2019) 6:13                                                                                                             Page 8 of 8

8.    Bulanon DM, Kataoka T, Okamoto H, Hata S-i (2004) Development of a               14. Shinnosuke K (2017) Integration of the tree form and machinery in Japa-
      real-time machine vision system for the apple harvesting robot. In: SICE             nese. Farming Mech 3189:5–9
      2004 annual conference. vol 1, IEEE, New York, pp 595–598                        15. Ren S, He K, Girshick R, Sun J (2015) Faster R-CNN: towards real-time
9.    Cohen O, Linker R, Naor A (2010) Estimation of the number of apples                  object detection with region proposal networks. In: Cortes C, Lawrence
      in color images recorded in orchards. In: International conference on                ND, Lee DD, Sugiyama M, Garnett R (eds) Advances in neural information
      computer and computing technologies in agriculture. Springer, Berlin, pp             processing systems 28. Curran Associates Inc., pp 91–99
      630–642                                                                          16. Redmon J, Divvala S, Girshick R, Farhadi A (2016) You only look once: Uni-
10.   Kurtulmus F, Lee WS, Vardar A (2014) Immature peach detection in colour              fied, real-time object detection. In: Proceedings of the IEEE conference on
      images acquired in natural illumination conditions using statistical classi-         computer vision and pattern recognition. pp 779–788
      fiers and neural network. Precis Agric 15(1):57–79                               17. Slotine J-JE, Asada H (1992) Robot analysis and control, 1st edn. Wiley,
11.   Qiang L, Jianrong C, Bin L, Lie D, Yajing Z (2014) Identification of fruit and       New York
      branch in natural scenes for citrus harvesting robot using machine vision        18. Universal Robot Support. https​://www.unive​rsal-robot​s.com/downl​oad/.
      and support vector machine. Int J Agric Biol Eng 7(2):115–121                        Accessed 23 Oct 2019
12.   Liu W, Anguelov D, Erhan D, Szegedy C, Reed S, Fu C-Y, Berg AC (2016)
      Ssd: single shot multibox detector. In: European conference on computer
      vision. Springer, Berlin, pp 21–37                                               Publisher’s Note
13.   Krizhevsky A, Sutskever I, Hinton GE (2012) ImageNet classification with         Springer Nature remains neutral with regard to jurisdictional claims in pub-
      deep convolutional neural networks. In: Pereira F, Burges CJC, Bottou L,         lished maps and institutional affiliations.
      Weinberger KQ (eds) Advances in neural information processing systems
      25. Curran Associates Inc., pp 1097–1105
