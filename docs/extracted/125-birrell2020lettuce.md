---
source_id: 125
bibtex_key: birrell2020lettuce
title: A Field-Tested Robotic Harvesting System for Iceberg Lettuce
year: 2020
domain_theme: Pertanian
verified_pdf: 125_Iceberg_Lettuce_Harvesting_Robot.pdf
char_count: 109595
---

Received: 15 August 2018    | Revised: 2 May 2019 | Accepted: 21 May 2019
DOI: 10.1002/rob.21888

REGULAR ARTICLE

A field‐tested robotic harvesting system for iceberg lettuce

Simon Birrell            | Josie Hughes                 | Julia Y. Cai | Fumiya Iida

Department of Engineering, University of
Cambridge, Cambridge, UK                          Abstract
                                                  Agriculture provides an unique opportunity for the development of robotic systems;
Correspondence
Josie Hughes, Department of Engineering,          robots must be developed which can operate in harsh conditions and in highly
University of Cambridge, Cambridge, CB2           uncertain and unknown environments. One particular challenge is performing
1PZ, UK.
Email: jaeh2@cam.ac.uk                            manipulation for autonomous robotic harvesting. This paper describes recent and
                                                  current work to automate the harvesting of iceberg lettuce. Unlike many other
Funding information
Engineering and Physical Sciences Research        produce, iceberg is challenging to harvest as the crop is easily damaged by handling
Council, Grant/Award Number: EP/L015889/          and is very hard to detect visually. A platform called Vegebot has been developed to
1; G's Growers, Grant/Award Number: DTP
icase; Royal Society, Grant/Award Number:         enable the iterative development and field testing of the solution, which comprises of
TA160113; Royal Society ERA Foundation            a vision system, custom end effector and software. To address the harvesting
Translation Award, Grant/Award Number:
TA160113; EPSRC Doctoral Training Program         challenges posed by iceberg lettuce a bespoke vision and learning system has been
ICASE Award, Grant/Award Number:                  developed which uses two integrated convolutional neural networks to achieve
RG84492; EPSRC Small Partnership Award,
Grant/Award Number: RG86264; BBSRC                classification and localization. A custom end effector has been developed to allow
Small Partnership Grant, Grant/Award              damage free harvesting. To allow this end effector to achieve repeatable and
Number: RG81275
                                                  consistent harvesting, a control method using force feedback allows detection of the
                                                  ground. The system has been tested in the field, with experimental evidence gained
                                                  which demonstrates the success of the vision system to localize and classify the
                                                  lettuce, and the full integrated system to harvest lettuce. This study demonstrates
                                                  how existing state‐of‐the art vision approaches can be applied to agricultural robotics,
                                                  and mechanical systems can be developed which leverage the environmental
                                                  constraints imposed in such environments.

                                                  KEYWORDS
                                                  agriculture, learning, mechanisms

1 | INTRODUCTION                                                                 Flemmer, 2009), cucumbers (Van Henten et al., 2002), citrus fruit
                                                                                 (Harrell, Adsit, Munilla, & Slaughter, 1990), strawberries (Hayashi et al.,
The story of agriculture is one of increasing automation. Crops are              2010), broccoli (Kusumam, Krajnik, Pearson, Cielniak, & Duckett, 2016),
planted, weeded, and harvested with ever decreasing direct human                 grapes (Luo et al., 2016; Monta, Kondo, & Shibano, 1995), and many
involvement, reducing labor costs, and improving yield. However, every           others (Bac, van Henten, Hemming, & Edan, 2014) have resisted
fruit or vegetable is different, and solutions for a single crop can vary        commercial automation. Agricultural robotics presents unique chal-
from country to country and even company to company. While some                  lenges compared to robotics in the more common factory environments
crops such as wheat or potatoes have long been harvested mechanically            (Oetomo, Billingsley, & Reid, 2009). Agricultural environments are
at scale, many others such kiwi fruit (Scarfe, Flemmer, Bakker, &                unstructured, intrinsically uncertain, harsh on mechanical equipment

---------------------------------------------------------------------------------------------------------------------------
This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium,
provided the original work is properly cited.
© 2019 The Authors. Journal of Field Robotics Published by Wiley Periodicals, Inc.

J Field Robotics. 2020;37:225–245.                                                                                 wileyonlinelibrary.com/journal/rob   |   225
226     |                                                                                                                            BIRRELL ET AL.

(Reddy, Reddy, Pranavadithya, & Kumar, 2016) and have high variability      First, the lettuces are localized and classified using a data‐driven
over weather conditions, locations, and time. Autonomous agricultural       approach. This is implemented using two CNNs, the architecture
systems must be flexible and adaptive (Edan, Han, & Kondo, 2009;            being shaped by the data sets available. Using this method in field
Hajjaj & Sahari, 2016) to cope. Harvesting and other crop manipulation      tests, a visual‐based localization success of 91% in field tests was
tasks (Hughes, Scimeca, Ifrim, Maiolino, & Iida, 2018; Kemp, Edsinger, &    achieved, and the crop accurately classified. Second, the lettuces are
Torres‐Jara, 2007), are particularly challenging (Bac et al., 2014) along   harvested with a custom‐designed end effector that incorporates a
all these dimensions.                                                       camera, pneumatics, a belt drive, and a soft gripper. The end effector
      Iceberg lettuce is an example of a crop that is still harvested by    cuts the lettuce stems efficiently while grasping the lettuce head in a
hand using a handheld knife, and presents two main challenges to            way that avoids damage. As the ground is uneven and its depth hard
automation. First, visually identifying the vegetable’s location and        to detect under the foliage, a force‐feedback control system is used
suitability for harvesting in what appears to be a sea of green leaves is   to detect when the end effector has reached the correct position to
hard even for humans (Figure 1a). Any solution must be robust to the        make the cut and achieve a consistent cutting height.
variation in individual lettuces, with their appearance varying greatly        Following a review of the state of the art in crop harvesting,
over weather conditions, maturity and surrounding vegetation.               Section 3 defines the problem posed by iceberg lettuce harvesting and
Second, in a terrain with an uneven ground the lettuce stem must            outlines the overall system that was developed. Section 4 focuses on
be cut cleanly at a specified height to meet commercial standards,          the details of the two harvesting methods developed: the vision
while the lettuce head can easily be damaged by unpractised handling.       system and end effector. The field tests and experimental results are
A lettuce harvesting solution should therefore incorporate a high‐          detailed in Section 5 and the paper concludes with a discussion and
precision, high force cutting mechanism while being capable of              conclusion that suggests the application of the techniques and
handling the vegetable delicately. There is a growing need for              approaches in this study to other agricultural challenges.
automated, robotic iceberg lettuce harvesting due to increasing
uncertainty in the reliability of labor and to allow for more flexible,
“on‐demand” harvesting of lettuce (Bechar & Vigneault, 2016).               2 | STAT E O F THE ART
      This study investigates automating the harvesting of iceberg
lettuce with three key research goals. First, how vision systems            There is prior work on vision techniques for agriculture. Many of
can be developed using off‐the‐shelf convolutional neural net-              the examples in the literature are from before the use of CNNs in
works (CNNs) as opposed to hand‐tailored computer vision                    the late 2000s, and so use a wide variety of hand‐crafted features.
pipelines, with pragmatic architectural adjustments made to                 The detection of volunteer potato plants was performed using
allow for the data sets available. Secondly, how mechanical                 adaptive Bayesian classification of Canny Edge Detectors among
systems can be developed to work within the operational                     other features (Nieuwenhuizen, Hofstee, & Van Henten, 2010).
constraints imposed by the agricultural environment. Finally,               Broad‐leaved dock detection (a weeding task) was performed
how field robots can be developed to allow rapid integration and            using a texture‐based approach, where image tiles were subjected
hence testing in the field.                                                 to a Fourier analysis (Evert et al., 2011; weeding is a similar task
      This paper describes the results to date of the Vegebot project,      to harvesting, just with less concern for the fate of the extracted
where a lettuce harvesting robot has been developed using an                plant). An alternative approach to weed detection used wavelet
approach of rapid iterative design, prototyping, and field testing. Two     features of near infrared (NIR) imagery (Scarfe et al., 2009),
key methods are described for automating the harvesting of the              subsequently passed to a principle component analysis (PCA)
iceberg lettuce under challenging and uncertain field conditions.           component and a k‐means classifier (Kiani, Azimifar, & Kamgar,

F I G U R E 1 (a) The challenging localization and classification problem posed by the lettuce field. (b) The existing harvesting method [Color
figure can be viewed at wileyonlinelibrary.com]
BIRRELL ET AL.                                                                                                                                      | 227
2010). Grapes have also been detected with Canny Edge filters,                 sugar beet classifying system (Lottes, Hörferlin, Sander, & Stachniss,
using decision trees as the classification mechanism (Berenstein,              2017) and a grape pruning system (Botterill et al., 2017). There are a
Shahar, Shapiro, & Edan, 2010). Foliage detection on the same                  number of patents specifically relating to the harvesting of iceberg lettuce
project required a separate algorithm. Grapes were classified on               (Ottaway, 1996, 2009; Shepardson & Pollock, 1974); however, these
another project using the AdaBoost framework, which combined                   have not been demonstrated under field conditions and do not clearly
the results of four weak classifiers into one strong one (Luo et al.,          demonstrate how selective plant harvesting is possible. These previous
2016). Radicchios have been detected by thresholding hue                       approaches include using a belt‐driven band saw‐type mechanisms or
saturation luminance images and applying particle filters (Foglia              water jet cutting. These approaches have limitations, most notably that
& Reina, 2006). Cucumbers were detected using NIR photography                  the outer leaves of the lettuce can be easily damaged when harvesting
at two positions 5 cm apart, to give stereoscopic depth informa-               and there is a lack of reliability in stem cutting height and quality.
tion (Van Henten et al., 2006) and classified for maturity by
estimating their weight from the perceived volume (Van Henten
                                                                               3 | P ROBL EM D EF IN I TION A ND S Y S TEM
et al., 2002). A more recent experiment detected broccoli heads
                                                                               ARCHITEC TURE
using an RGB‐D sensor had the disadvantage that the robot had to
move a tent across the field to prevent interference from outdoor
                                                                               3.1 | Problem
light. Point clouds were clustered from the depth information,
outliers were removed, and viewpoint feature histograms con-                   The lettuces to be harvested must be both localized (their position
structed. A support vector machine performed the actual                        detected) and classified according to their suitability for picking. For
classification of the broccoli heads (Kusumam et al., 2016). The               a mature lettuce, using the custom end effector, the lettuce head
use of vision to provide control through methods including visual              center must be localized to within approximately 2 cm of the ground‐
servoing has also been shown to increase positional accuracy                   truth position. The identified classes should include at a minimum (a)
when harvesting citrus fruit (Mehta & Burks, 2014; Mehta,                      harvest‐ready lettuces (which may be picked immediately), (b)
MacKunis, & Burks, 2016).                                                      immature lettuces (which can be returned to later), and (c) infected
    These solutions are not appropriate for iceberg lettuce. Color             lettuces (which should not be touched with the end effector so as to
cues as used in (Berenstein et al., 2010; Cubero, Alegre, Aleixos, &           avoid spreading the infection). The vision system should operate
Blasco, 2015; Foglia & Reina, 2006) are less useful because the                under varying weather and lighting conditions.
lettuces appear to be a “sea of green.” Depth cues, as used in                     Once a harvest‐ready lettuce has been identified it must be cut to
Kusumam et al. (2016) and Rajendra et al. (2008) also provide limited          supermarket standards. This is currently performed by a human
information because the plants and their leaves overlap and the                worker with a knife. The worker tilts the head of the lettuce and then
heads are often hidden.                                                        uses a high impulse maneuver to cut the stem of the lettuce. The
    Similarly, there are a number of existing autonomous harvesting            lettuce is then bagged and placed on a harvesting rig (see Figure 1b).
systems. Harvesting is a challenging task to automate and a recent review      There is a high degree of dexterity and accuracy required to achieve a
came to the gloomy conclusion that almost no progress had been made in         supermarket‐quality cut. The lettuce must have a stem of the correct
the past 30 years (Bac et al., 2014). Many research projects have been         length (1–2 mm protruding), and it must be clean, with minimal
performed, but little has filtered through into the commercial world. The      browning and have no damage to outer leaves. Additionally, if outer
more successful projects include a harvester for apples (Silwal et al.,        leaves remain after harvesting, these should be removed, which has
2017) using a suction method, rice harvesting using custom harvesting          proved to be a challenging manipulation problem in itself (Hughes
systems (Kurita, Iida, Cho, & Suguri, 2017), and a sweet pepper harvesting     et al., 2018). If the lettuce falls outside these requirements, it is not
system (Bac et al., 2017). There has also been significant work in the         accepted by supermarkets. A lettuce worker can harvest a lettuce in
development of autonomous weeding or grading systems including a               under 10 s, which sets the benchmark for a robotic harvesting system.

T A B L E 1 Conditions for the design and development of a lettuce harvesting system determined by the agricultural environment
                               Parameters                              Specification                         Influence on design
 Environment                   Width of lettuce lanes                  2                                     Determines width of platform
                               Spacing between lettuce                 30 cm                                 Determines maximum size of end effector
                               Height of lettuce plants                30 cm                                 Determines of height of platform
                               Diameter of lettuce                     20 cm                                 Determines size of end effector
                               Diameter of lettuce stem                Approximately 30 mm                   Determined blade specification
 Robot                         Generator power                         240 V, 2 kW                           Sufficient to power all systems
                               Compressor air pressure                 8 bar                                 Sufficient for pneumatics
                               Vegebot dimensions                      2 m x 0.6 m x 0.5 m                   Fits within lettuce lanes
228     |                                                                                                                                BIRRELL ET AL.

                                                                                                       F I G U R E 2 The Vegebot harvesting
                                                                                                       system, shown undergoing field
                                                                                                       experiments [Color figure can be viewed at
                                                                                                       wileyonlinelibrary.com]

      There are also a number of constraints arising for the agricultural   lettuce stalk and retract, while the gripper actuator causes the soft
environment, which dictate the form factor and design decisions, and        gripper to grasp and release the target lettuce.
these are summarized in Table 1.                                               The mobile platform supports the above hardware items and is
                                                                            moved manually around the field. The system is powered by a
                                                                            generator, which provides sufficient power to meet the peak
                                                                            demands of the system. An air compressor is used to enable
3.2 | System architecture
                                                                            actuation of the pneumatic systems. The generator and compressor
The system developed for autonomous iceberg lettuce harvesting              can sit on the Vegebot to allow the system to be completely mobile.
(Vegebot) is shown in Figure 2. Vegebot comprises a laptop computer            The software architecture is shown in Figure B1a and detailed in
running control software, a standard six‐degree‐of‐freedom (DOF)            Appendix B. The web‐based user interface is shown in Figure B1b.
UR10 robot arm, two cameras, and a custom end effector, all housed
on a mobile platform for field testing. A block diagram showing the
integration of the system is shown in Figure 3.                             3.2.1 | Control and processes
      Vegebot contains two cameras: an overhead camera positioned
                                                                            The processes for training and operating Vegebot can be analyzed at
approximately 2 m above the ground and another end‐effector camera
                                                                            three levels (see Figure 4). At the highest level, the learning cycle, data
mounted inside the end effector. Both are ordinary, low‐cost USB
                                                                            sets are gathered for the initial training of the vision system,
webcams and stream video to the control laptop. Together, these
                                                                            harvesting is performed and additional data are gathered. As soon as
allow Vegebot to detect (localize and classify) lettuces, and to move
                                                                            enough new data are gathered to merit it, the system can be
the end effector into position. There are additional sensors built into
                                                                            retrained. In this way, the accuracy and generalization abilities of the
the robot arm: the standard joint encoders and a force‐feedback sensor
                                                                            Vegebot can in principle be improved as images are obtained from
that records the force and torque being applied to the end effector.
                                                                            new fields and under different weather conditions. The testing of
      The UR10 arm provides a wide range of movements, and provides
                                                                            these improvements is the subject of a future paper.
force and torque information allowing force feedback to be
                                                                               The harvesting session outlines the structure of the work in the
implemented. A commercial implementation would likely have
                                                                            field. First the Vegebot is moved along the lettuce lanes (seen in Figure
simpler arms each with an end effector, all operating in parallel (for
                                                                            2) to bring approximately 10 lettuces within the robot’s workspace
an example of such a system, see Scarfe et al., 2009). The control
                                                                            and field of view. The current iteration of Vegebot is simply manually
laptop controls the end effector using two digital I/O lines routed
                                                                            pushed into position. Next, the Vegebot is optionally calibrated, using
through the UR10 arm. These switch the two pneumatic actuators on
                                                                            the method described in Section 4.1.3. Calibration is always performed
and off, the blade actuator causing the blade to slice through the
                                                                            at the start of a session and then on an as‐needed basis as discrepancy

                                                                                                       F I G U R E 3 Block diagram of the robotic
                                                                                                       lettuce harvester system developed
BIRRELL ET AL.                                                                                                                             | 229

F I G U R E 4 Processes for training and operation of the Vegebot, showing the key processes in green. The trajectory diagram for the lowest
level pick sequence is shown in Figure 14 [Color figure can be viewed at wileyonlinelibrary.com]

between the lettuce position inferred by the overhead camera and            inaccurate to a greater or lesser degree. At this point, the camera
that detected by the end‐effector camera increases.                         in the end effector takes over to fine‐tune the end‐effector position
    Next, the vision system detects lettuces in the video feed from the     to be directly over the center of the lettuce. The end effector then
overhead camera. A human then selects a lettuce by clicking on the user     descends vertically down over the lettuce until the force‐feedback
interface. This was a manual process during the experiments for the         sensor registers the upward force of the ground resisting the
sake of safety. Selection could be automated with a trivial modification.   downward trajectory. The soft gripper is then activated and grasps
The pick sequence then begins, with the lettuce being picked and placed     the lettuce. Next, the blade actuator is activated and the blade
onto the platform. Once the reachable lettuces have been picked, the        moves horizontally and cuts through the lettuce stalk. Still grasping
Vegebot can either be moved to a new position or the session finished.      the lettuce, the end effector then lifts vertically to the same height
    The pick sequence is fully automated and comprises seven                as the pregrasp position, clearing it from contact with the
stages. First, the end‐effector approaches the pregrasp position, a         surrounding lettuces. The arm then moves the end effector to a
point centered approximately 10 cm over the inferred top of the             convenient place position where the soft gripper is deactivated and
lettuce, based on the localization predictions from the overhead            the lettuce is released.
camera. Because of the rugged nature of the environment and the                The following section addresses key the harvesting methods
impacts received by the Vegebot, this prediction is inevitably              which have been implemented to allow robust and reliable harvesting

F I G U R E 5 Obtaining data for the data set showing the user holding a webcamera to capture data sets at different heights [Color figure can
be viewed at wileyonlinelibrary.com]
230   |                                                                                                                                  BIRRELL ET AL.

F I G U R E 6 The vision system pipeline showing the two stages of convolutional neural network. First, the lettuces are localized using one
network. A second network using both the lettuces localized from the first network and presegmented lettuce images from a classification data
set is used [Color figure can be viewed at wileyonlinelibrary.com]

in the agriculture environment (and are shown in green boxes in               robot‐centric coordinates for picking in the face of very rugged physical
Figure 4).                                                                    conditions. All these operations must be performed in close to real time
                                                                              given that Vegebot uses localization information dynamically to fine‐
                                                                              tune the trajectory of its end effector.
4 | HARVE ST IN G METHODS
                                                                                 In principle, any of the latest deep‐learning based object detectors
                                                                              could fulfill this function. Candidates such as YOLOv3 and Faster R‐
4.1 | Lettuce localization and classification
                                                                              CNN (Redmon & Farhadi, 2018; Ren, He, Girshick, & Sun, 2015) can
The visual lettuce detection process comprises both localization              both provide object bounding boxes and class labels in real time (Ren
(discovering where the lettuce is relative to the robot) and classification   et al., 2015). In this case, YOLOv3 was chosen as it gave the fastest
(determining whether the lettuce is a suitable candidate for being            detection times and its principal disadvantage (poor performance on
harvested). Lettuces heads are variable in appearance and are typically       very small close‐together objects) was irrelevant in this use case. Fast
partially or wholly occluded by their own leaves and by leaves of             detection times on a laptop implied the possibility of later re‐
neighboring lettuces. The outdoor lighting conditions also vary               implementing the algorithm on more modest, embedded hardware.
drastically with different weather, including very different levels of           With a large enough detection data set, rich in examples of all
brightness and contrast. The lettuces need to be classified as “harvest       lettuce categories, there would be little more to do. In the present
ready” (for immediate picking), “immature” (for picking at a later date),     project there were only two data sets available. The first was a
or “infected” (to be avoided and reported). Additionally, the localization    detection data set gathered by one of the authors (see Figure 5), with
system must transform the viewpoint coordinates of the lettuce into           images captured by a webcam and bounding boxes and class labels

F I G U R E 7 Development of lettuce harvesting end effectors. (a) Two‐handed approach with one hand to hold the lettuce, one hand with
knife, (b) rotary DC motor cutting mechanisms, (c) linear actuator knife‐powered mechanism, and (d) pneumatic cutter chosen as the best
mechanism [Color figure can be viewed at wileyonlinelibrary.com]
BIRRELL ET AL.                                                                                                                            | 231

F I G U R E 8 The final end effector developed, showing the belt drive mechanisms and dual pneumatic actuator system [Color figure can be
viewed at wileyonlinelibrary.com]

added manually. This data set (detailed in Table 2) was rich in                Ideally, a more extensive detection database would have been
positional data but the less common classes such as “infected” were         gathered from multiple fields and stages of the crop cycle, to fully
underrepresented. The second data set originated from a previous            represent the position and location of exemplars of all classes.
student project (Nagrani, 20151) in lettuce classification and was rich     Alternatively, the existing classification images could have been
in examples of all classes, but had no useful positional information, all   inserted over other backgrounds to produce an artificial training set
lettuces being in the center of each image.                                 for detection. This latter strategy runs the risk of the network

F I G U R E 9 The force‐feedback method, allowing a repeatable height between the ground and the knife to be achieved [Color figure can be
viewed at wileyonlinelibrary.com]

1
http://mi.eng.cam.ac.uk/projects/lettuce/
232     |                                                                                                                             BIRRELL ET AL.

F I G U R E 1 0 (a) The requirements for successfully lettuce harvesting determined by the physical end effector. The lettuce center must be
detected within a distance such that the lettuce is fully within the footprint of the end effector when cutting. (b) The distribution of accuracy of
the lettuce localization system for the two different cameras used, with images from sub‐data sets C and E, respectively [Color figure can be
viewed at wileyonlinelibrary.com]

learning to detect artefacts in the synthetic images, rather than           simply to discover the presence and location of lettuces (the
genuinely localizing the vegetables based on natural visual cues.           number of classes being reduced to a single “lettuce” class) and
      Instead, the solution chosen was to divide the pipeline into two      output their bounding boxes. Narrow bounding boxes, likely
networks (see Figure 6), each trained by one of the existing data           caused by lettuces at the edge of the viewport and out of reach
sets. The first network, a YOLOv3 object detector would be used             of the arm, are rejected as candidates. Each of the remaining

F I G U R E 1 1 Localization performance with varying brightness and image contrast. The precision and recall are given in both cases. The
images below show the contrast and brightness enhancement added applied to a typical image in the test data set [Color figure can be viewed at
wileyonlinelibrary.com]
BIRRELL ET AL.                                                                                                                        | 233

F I G U R E 1 2 Examples of the localization system working on different lettuce and with camera setups with different heights and angles and
showing usage on different crops and different fields demonstrating robustness. Blue bounding boxes indicate the entire head of lettuce could
be seen, green indicate where only part of the head is visible [Color figure can be viewed at wileyonlinelibrary.com]

F I G U R E 1 3 (a) Accuracy of the classification network with changes in image brightness and image contrast. (b) The confusion matrix
showing the classification performance of lettuce [Color figure can be viewed at wileyonlinelibrary.com]
234   |                                                                                                                             BIRRELL ET AL.

F I G U R E 1 4 End‐effector trajectories when undergoing the field experiments. It shows all trajectories centered on cutting (at 0 s) and an
example representative trajectory. The vertical divisions correspond to the different stages of the pick sequence from Figure 4 [Color figure can
be viewed at wileyonlinelibrary.com]

F I G U R E 1 5 Examples of harvested lettuce showing some with an ideal cut, unwanted outer leaves and damaged outer leaves [Color figure
can be viewed at wileyonlinelibrary.com]

F I G U R E 1 6 Distribution of the cycle times, leaves to remove, and extra cuts required for the various lettuce harvesting experiments [Color
figure can be viewed at wileyonlinelibrary.com]
BIRRELL ET AL.                                                                                                                                | 235
T A B L E 2 Details of the different sub‐data sets used to create the localization data set including the number of lettuce and conditions in
which the images were taken
                                                                                                              Weather               Image
 Sub‐data set     Number of images      Number of lettuce per image       Camera height from ground (m)       conditions            quality
 A                157                   7–10                              ≈1.8                                Cloudy/sunny          Medium
 B                209                   8–14                              ≈2                                  Sunny                 High
 C                117                   3–6                               ≈1                                  Cloudy                Medium
 D                131                   4–11                              ≈1.2                                Cloudy/rainy          Low
 E                891                   1                                 ≈0.3                                Cloudy/sunny/rainy    High

bounded boxes is then cropped (adding a small margin round the                 data set suitable for the propose of this project, a new lettuce
outside of the bounding box to provide more visual information to              localization data set was collected, labeled, and assembled. Images
the next stage) and then a second Darknet Object Classification                were collected from three different sources: images taken by the
Network was applied to each. Finally, bounding boxes predicted by              overhead camera on the Vegebot platform, images taken directly
the first stage and the class labels predicted by the second stage             with a camera, and extracted images from videos taken by mobile
are merged. Although requiring a two‐stage network, this                       phones and webcams. Figure 5 shows the process of obtaining
approach offers greater performance of both localization and                   images from the field using a webcam.
classification. The architecture has been chosen to achieve the                   Images were divided into five sub‐data sets (A, B, C, D, and E)
best performance with the data sets available and given the                    according to the characteristics of the images and corresponding
information content of those data sets.                                        to the different field experiments in which they were obtained.
     There is an additional advantage to using a two‐stage network.            This allowed better tracking of the data set to make sure the
Images input to YOLO are resized from 1,920 × 1,080 to a resolution            assembled data set was well balanced. Figure 6 shows some
of 320 × 320. This is still enough visual information to distinguish,          sample images from each of the five data sets. The images cover
say, a man from a dog, but may not be enough to determine whether              different weather conditions, camera heights, lettuce fields,
one of the 10 lettuces visible in the overhead camera is infected or           lettuce layouts, lettuce maturity, and image qualities, since these
not. By first detecting the bounding boxes and then cropping each              are factors that can vary during lettuce harvesting. Table 2 gives a
lettuce from the original 1,920 × 1,080 image before resizing to               detailed overview for each subset including the number of images,
224 × 224, much more visual information on each lettuce is available           number of lettuces per image, camera heights, weather conditions,
for the classification network. This improves the likelihood of a              and image quality. Image quality refers to the subjectively
correct classification on images from the overhead camera.                     evaluated blurriness of the images.
     Predictions on the network took 0.082 s for localization in the              The images were labeled manually in square bounding boxes
first stage and 0.013 s classification time for each detected lettuce          using the VoTT Visual Object Tagging Tool (Vott, 2018). The lettuce
passed to the second stage. Assuming 10 candidate lettuces per                 images were labeled such that center of the bounding box is the
image the total time for localization and classification on the current        geometrical center of the corresponding lettuce and the dimensions
hardware is approximately 0.212 s, slower than a single YOLO object            of the bounding box are 10% larger than the lettuce head. Only the
detection network would be, but still sufficiently fast for real‐time          lettuces whose heads are fully included in the image were labeled.
adjustments. The end‐effector camera typically has only one lettuce            The data set was randomly separated into training (70%), validation
in view during fine‐tuning, reducing the detection time to 0.095 s.            (20%), and test (10%) sets, where the validation set is used for
The harvesting time is somewhat longer, and thus this is not the time          hyperparameter tuning and the test set is only used for benchmark-
limiting step. The pipeline processes images from both overhead and            ing the final performance.
end‐effector cameras. The overhead camera provides candidates for                 Even though only lettuces that were fully visible within the
picking and the end‐effector camera is used to fine‐tune the                   image were labeled, the YOLO algorithm was robust enough to
approach of the end effector to the desired lettuce.                           detect lettuces at the edges as well. Classifying these partial
     The two‐stage network uses the existing data sets to maximum              lettuces would have increased the complexity of the problem
advantage and provides better classification by maintaining a higher           unnecessarily. Practically, these lettuces were likely to be out of
resolution on the images of individual lettuces.                               the reach of the Vegebot robot arm and therefore they were
                                                                               rejected from the detected candidates. There were also cases
                                                                               where lettuces were blocked by weeds, the Vegebot itself or other
4.1.1 | Localization data set
                                                                               obstacles, which led to narrow bounding boxes instead of square
Training a deep CNN object detector requires a large amount of data.           ones. Lettuce rejection algorithms were implemented to reject
The data set also needed to be a good representation of the real               such candidates. A candidate was rejected if it met either of the
scenarios the Vegebot would encounter. Since there was no existing             following criteria:
236     |                                                                                                                                               BIRRELL ET AL.

• Rejection of nonsquare bounding boxes which are on the edges of                              T A B L E 3 Classification data set, showing the number of each type
    the images                                                                                 of lettuce in the data set
                                                                                                Lettuce      Harvest
            l                                                            L+W                    class        ready      Immature      Infected   Background   Total
              > 1.15 and        d < margin        where margin =             .
            w                                                             75
                                                                                                Number of 181           149           121        214          665
                                                                                                 images
• Rejection of narrow bounding boxes

                                        l
                                          > 1.4,                                               4.1.3 | Calibration and end‐effector positioning
                                        w

where w and l are the lengths of the bounding box edges, with w                                The first approach tried on the positioning problem was the classic
being the longer of the two. L and W are the width and height of the                           one of modeling the robot and its coordinate systems, calibrating
overall image, and d is the distance between the bounding box and                              the camera parameters, and then transforming the target center
the edge of the image.                                                                         pixel of the lettuce (the center of the bounding box) to a position in
                                                                                               3D space and finally using inverse kinematics to move the arm as
      The localization network was based on the YOLOv3 architecture                            required. The problem encountered was that the system worked
and was trained with a batch size of 64, subdivision of 8, and 10,000                          well in the lab, but would fail once subjected to knocks and bumps in
iterations. The network was trained on a PC with a 4.5 GHz Intel i7‐                           the field. Even small deviations in the position of the overhead
7700k CPU and an nVidia 1080Ti GeForce GTX GPU. Training took                                  camera would mean that the robot might incorrectly locate its
around 12 hr. Pretrained weights based on ImageNet were used. No                               target by up to 10 cm.
data augmentation was applied: This could improve localization                                    A different approach was therefore attempted, where the robot
performance and remains for future work.                                                       could self‐calibrate the transformation from viewport pixels to arm
                                                                                               position, using Aruco markers positioned on the top of the end
                                                                                               effector. An occasional self‐calibration would be sufficient to reset
                                                                                               the transformation, for example, after moving the platform. Calibra-
4.1.2 | Classification data set                                                                tion also resets the target location of the lettuce center within the
The goal of the classification network is to pick out the harvest‐ready                        viewport of the end‐effector camera. We assume the platform is kept
(i.e., mature and healthy) lettuces among all the lettuces recognized                          approximately level with reference to the field due to the tracks in
from the previous localization step. Immature and infected lettuces                            which them Vegebot moves. Further details of the final calibration
should be left in the field. False‐negative localization results can be                        procedure can be found in appendix.
hazardous: Reaching for a nonlettuce object can damage the robot
(if the object is a rock) as well as the object itself (if the object is a
human hand or robot part). Adding a negative “background” class
                                                                                               4.2 | Force feedback‐driven harvesting
acted as an additional filter to prevent false positives: By explicitly
labeling edge cases as not being lettuces, the classification network’s                        The lettuce harvester has been designed to achieve reliable, efficient
performance improved.                                                                          harvesting of lettuce with minimal damage to the lettuce. To meet
      The images were labeled by one of the authors with assistance                            supermarket specifications, the lettuce stem should be cut with a
provided by cultivation experts to allow labeling and classification of                        single consistent straight cut such that there is approximately 2 mm
the data set. Figure 6 shows sample images from each of the four                               of stem. The outer leaves of the lettuce should also be removed
classes. Table 3 is an overview of the size of the data set. The 665                           where possible. A UR10 6‐DOF arm is used to provide movement of
images were randomly separated into training (87.5%) and test                                  a custom end effector which has been specifically designed for
                 2
(12.5%) sets. A higher portion of images were allocated to the                                 lettuce harvesting. The UR10 arm is mounted on a mobile base which
training set deliberately due to the limitation of the images available.                       can be moved along the rows of lettuce.
      The classification network used was the standard object classifier                          The picking sequence (Figure 4 “pick sequence”) demonstrates
supplied with Darknet, with no transfer learning (the use of                                   how there are two stages to the physical cutting aspect of the
pretrained weights would likely increase performance further). The                             harvesting procedure. To minimize the damage to the lettuce and
batch size was 64, the subdivision was 4, and the network was                                  also achieve a clean cut a method where the end effector is made of
trained to 260 iterations. The training was on the same hardware as                            two mechanisms has been used. First, a soft clamping method is used
the localization network and took 2 hr.                                                        to hold the lettuce throughout cutting and when lifting. Secondly, a
                                                                                               cutting mechanism is required to cut the stem of the lettuce at a
                                                                                               given height. The cutting mechanism requires force (≈20 N) to cut
2
 The Darknet classifier has no separate validation data set; the experimenter chooses the      through the stem and outer leaves, while also requiring height
length of training based on periodically evaluating against the test set. For the robustness   adjustability and also a straight linear cut.
evaluation below, fresh data was used.
BIRRELL ET AL.                                                                                                                                         | 237
4.2.1 | End‐effector design                                              4.2.2 | Force‐feedback control
To achieve sufficient cutting force to cut the stem, a high impact,      A key challenge to successful harvesting was reliably cutting the lettuce
straight cut is required at the base of the lettuce. A number of         stalk at the correct height in an environment which is highly varying,
different mechanisms were tested to determine which could achieve        uncertain, and unknown. To achieve this, the ground was used as a fixed
sufficient force and quality of cut: soft gripper and knife hand,        reference point and the stem was assumed to be a fixed distance above
pneumatic actuation, belt drive, and rotary chopping. Figure 7 shows     the surface. Using force feedback from the joints of the UR10 robot
the different mechanisms considered.                                     arm, the end effector is lowered toward the ground, enveloping the
    The two‐handed approach lacked sufficient cutting force and          lettuce, until a given force was achieved and contact with the ground
required a high level of coordination between the two arms. A rotary     could be assumed. The cutting height relative to the ground can be
electric motor approach lacked the force to reliably cut the stem and    adjusted by manually varying the height of the cutting mechanism. A
led to the mechanism having to hack at the stem. Although the linear     force threshold, T , was found by experimentally determining what force
actuator approach provided sufficient force, the speed was low,          is required for the end effector to interact with the ground, that is, when
leading to poor cut quality. The pneumatic cutting mechanics             it overcomes the resistive force of the leaves and other ground reaction
provides a high power‐to‐weight ratio, making it highly suited for       forces, FR . The force threshold was experimentally determined to be
this application where a fast clean cut is required. Although there is   60N to ensure all leaves were pushed away from the lettuce head and
no position control, pneumatic actuation allows for easy to              the end effector was in contact and level with the ground. This approach
implement cut/open control.                                              is summarized in Figure 9.
    The soft gripping mechanism has a single moving gripper and a            This approach helped push out the outer leaves of the lettuce which
fixed gripper lined with foam. Similar to other harvesting end           interfered with the cutting mechanism. This also allows the end effector
effectors (De‐An, Jidong, Wei, Ying, & Yu, 2011; Foglia & Reina,         to self‐level on the ground, and provided stability and consistency. Small
2006), a pneumatic actuator is used to control the gripper as this can   “feet” were added to the end effector to allow stability to be achieved
be used to provide controllable compliance by varying the air            and prevent it from pressing too low into the ground. This approach
pressure such that the lettuce is held but not damaged with simple       allows the system to adapt to different field conditions, for example,
open/close control                                                       different soil heights relative to the tractor track heights.
    The end effector developed is shown in Figure 8, with the design         Once fully positioned, the lettuce is grasped and the cutting
parameters given in Table 4. The end effector used only two              takes place. Each of the pneumatic actuators is controlled by a
actuators, one for grasping and one for cutting to enable simple         valve which has two position controls. Two digital outputs from
control. A timing belt system was used to transfer the linear motion     the UR10 end effector are used to control the valves. After the
from a single actuator to both sides of the blade to allow smooth        correct height is achieved using force feedback, cutting is
movement. This allows the actuator to be mounted above the height        triggered by first actuating the grabbing mechanism so the lettuce
of the lettuce, such that when cutting it does not interfere. The belt   is held in a fixed place. The cutter pneumatic system is then
drive system allows for the height of the cutting mechanism to be        actuated so the blade cuts the stem of the lettuce. The arm can
easily altered by changing the height of the cutting mechanism.          then be lifted, with the knife released and then the grabber
                                                                         retracted to release the lettuce.
                                                                             Besides these two challenges, an additional one was that the weight
                                                                         of the end effector was at the limit of the payload ability of the UR10.
T A B L E 4 Specification of the end‐effector developed
                                                                         This restricted the arm to moving more slowly than would otherwise be
 End‐effector parameters             Specification                       necessary. This will be discussed in the experimental results.
 Weight                              8 kg
 Height                              45 cm
 Width                               45 cm
                                                                         5 | F I E L D EX P E RI M E N T R E S U L T S
 Depth                               30 cm
 Gripper pneumatic actuator          1 MPa, bore 10 mm, stroke           Ten experimental sessions were carried out in the harvesting seasons
  specification                       15 cm
                                                                         in 2016–2018 in lettuce fields in Cambridgeshire, UK, in varying
 Cutter pneumatic actuator           1.5 MPa, bore 15 mm, stroke
                                                                         weather conditions and across many (over 10) different fields. In
  specification                       20 cm
                                                                         these field trips, the system was developed and tested3.Field
 Timing belt                         5.08 mm pitch, 203 cm length,
                                                                         experiments were undertaken to test the performance of the
                                      20 mm width
                                                                         localization and classification system in isolation from the harvester.
 Length of travel of blade           200 mm
                                                                         The entire system was also integrated to test the full functioning of
 Cutting knife length                250 mm
                                                                         the system in conjunction with its physical harvesting abilities. In this
 Inner area to encapsulate           25 cm × 25 cm
  lettuce
                                                                         3
                                                                         These were in collaboration with a major agricultural company, G’s Growers.
238     |                                                                                                                               BIRRELL ET AL.

section, the localization and classification is presented for both         T A B L E 5 Overall system harvesting tests showing the localization
individual and system level tests, after which the harvesting system       performance
results are presented.                                                      Metric                           Result     Definition
      At the beginning of each experimental session, the Vegebot was        Lettuce localization success     91.0%      Number of detected qualified
                                                                                                                          Number of real qualified
assembled at the start of a lettuce lane. Typically, a three person
crew participated, one operating the control laptop, one observer,          False‐positive detection         1.5%       Number of false qualified
                                                                                                                        Number of real qualified
and one checking and resolving any physical issues and enabling the
air compressor when required.
                                                                              When integrated into the full system, the overall performance of
                                                                           the localization system could be tested in harvesting trials. The
                                                                           success rate (number of correctly identified lettuce over total
5.1 | Localization
                                                                           number of lettuce observed) and false‐positive detections were
In order for a lettuce to be successfully picked, the center of the end    recorded. The results from this overall system results include over 60
effector must be placed with a tolerance, D , of the true center of the    individual lettuce harvesting experiments, where the localization
lettuce. The tolerance, D , which is determined by the mechanical          results of all lettuce that could be visible observed by the system
design of the end effector is approximately 2 cm for average sized         were recorded. The results are shown in Table 5.
lettuce (approximately 15–20 cm diameter). For successful harvest-
ing, the localization system must predict the center of the lettuce,
                                                                           5.2 | Classification
such that the absolute difference from the ground truth, ΔD is less
than the tolerance (ΔD < D ). In practice, for a given camera height       Robustness and accuracy of the classification system is critical for
the threshold was specified in pixels, calculated taking into account      avoiding infected or damaged crops which could infect the harvesting
the scale of the image. This threshold is illustrated by Figure 10a.       system. By skipping immature heads and avoiding unnecessary
      To test the ability of the system to localize lettuce heads with     harvesting the efficiency of the harvester can be maximized. To test
sufficient accuracy to allow success harvesting, images taken with         the robustness of the system, the same images from the localization
both low‐level and high‐level cameras were used (approximately 30          experiments (modified for brightness and contrast) were passed to
and 170 cm above the crop, respectively). The difference between           the classification network and the accuracy recorded. The results are
the detected and ground truth of the lettuce center was found. The         shown in Figure 13a. For classification, the network showed greatest
distributions of the accuracy in the localization performance of the       robustness to contrast as opposed to brightness variations; this could
two cameras is shown in Figure 10b.                                        be because the training data showed greater variation in contrast as
      In the field, the lighting and weather conditions may vary           opposed to brightness. Images taken in bright sunlight were high
significantly. To test robustness to different lighting conditions, the    contrast rather than high brightness and there were no late‐night
test subsets of data sets A‐E in Figure 6 were artificially modified       images in the data set to train for low brightness. Judicious data
with image processing (using ImageEnhance brightness and Ima-              augmentation before training should improve performance.
geEnhance contrast functions in the Python Willow library) to                 To understand the classification decisions made by the network a
different levels of brightness and contrast, producing six times           confusion matrix of the field tests has been generated and is shown
(7,200) the original number of test images (1,200). The localization       in Figure 13b. The diagonal shows the correctly classified lettuce,
system was then tested on this set of images (Figure 11). The              showing that the classification performs adequately for identifying
precision and recall were then found. The system showed a high             background, infected and harvest‐ready lettuce. Identifying infected
robustness to changes in image brightness (the most likely changing        lettuce is crucial for avoiding contamination and further work should
field conditions), with minimal changes in precision and recall. For the   be undertaken to further improve the classification.
variation in image contrast, although the precision remained high, the        The network struggles to separate harvest‐ready and immature
recall dropped significantly for high changes in contrast. It is likely    lettuces. One of the reasons is that the boundary between harvest‐
that using data augmentation techniques on the original training data      ready and immature lettuces is very vague and changes accordingly
set would have improved this.                                              to current market requirements, and thus creating a meaningful data
      Figure 12 shows some examples of the localization results. Figure    set is challenging. The classification data set was labeled under the
12a–c shows the robustness at different camera heights, different          rules that a “harvest‐ready” lettuce head is around 18 cm in diameter,
angles (12d), and different parts of the field (middle and edges). The     which for the majority of the time is the harvesting requirement. On
system was able to avoid detecting weed (12a,c), human feet (12a,b)        the day of the field test, there was a change in harvesting
as well as lettuces that fail to form lettuce heads (12b). Figure 12b      specification: lettuces that would normally be treated as “immature”
also shows that the lettuce rejection algorithm is able to effectively     and left in the field were also harvested, which explains why many of
reject lettuces which are on the edge of the image. Localization was       the “immature” predictions got corrected to “harvest‐ready.”
also effective at different heights (ranging from 20 cm to 170 cm) and        When entire system tests of the Vegebot were later ran in the
with the camera tilted by up to 45°.                                       field, the system provide 100% accuracy when classifying lettuce.
BIRRELL ET AL.                                                                                                                                        | 239
Although a reasonable number of experiments were ran (69), the                which reflects the desired trajectory and demonstrates the different
number of nonideal (i.e., diseased or immature) lettuce in this               parts of the harvesting process. The breakdown of the time series
experiment was low, so there was little variation in the classification       into the processes from Figure 4 is shown. The X, Y, and Z
of lettuce seen.                                                              coordinates are shown with respect to the base of robot platform,
                                                                              with X pointing forwards in the direction of travel, Y pointing to the
                                                                              left, and Z pointing up.
5.3 | Harvesting performance                                                     With the exception of the grasp‐cut section, all of the other
The final field tests were performed in May 2018 at a lettuce field in        trajectory sections were slowed considerably by the burden of the
Cambridgeshire, UK. These final tests followed on from over 10                end effector weight on the robot arm. This led to an average cycle
previous visits to the field with well over 300 lettuce harvested. The        time of 31.7 s. Critically, the rate‐limiting step, the grasping and
Vegebot was positioned at the start of a lettuce lane, the lettuces           cutting, required only 2 s. Thus, using a lighter end effector, for
within the viewport of the overhead camera were detected and picks            example, constructing from a lighter material such as carbon fiber,
attempted. Once attempts had been made to pick all feasible lettuces,         or using a stronger arm could lead to a significantly lower cycle
the platform was moved forward down the lane to the next unpicked             time.
rows. Each lettuce position, and false positives or negatives were               The trajectories clearly show the impact of the force feedback,
recorded, together with the number and trajectory of all pick attempts.       with the robot arm descending in the Z axis at a consistent rate until
Finally, each lettuce was inspected for damage, in particular for the         the force threshold is met. This shows that the end height of arm
stalk being cut too close to the lettuce body. In total, 69 lettuces were     varies considerably for different lettuce, showing how using force
detected by the vision system, 60 were in range of the robot arm and          feedback allows a consistent height to be achieved. There is also
harvesting attempted with 31 lettuce harvested successfully. A video          slight variability in the X and Y axis close to when the force threshold
of the Vegebot in operation was recorded.   4                                 is reached as the end‐effector self‐levels on the ground.

5.3.1 | End‐effector trajectory                                               5.3.2 | Overall harvesting performance metrics
During the final field experiments, 69 qualified lettuces were                The results of the field experiments are shown in Table 6.
detected by the vision system. Of these, attempts were made to                Considering all the harvesting attempts, the detachment success if
pick 60, the remainder being out of range of the robot arm. Thirty‐           found to be 52% (31 out of 60 lettuces correctly identified, excluding
one pick attempts were successful, with 29 failures, almost entirely          false positives). However, in 28 cases, the harvesting failure was due
due to the weight of the end effector causing mechanical failures on          to practical restrictions (weight of the arm, practical workspace of
the arm which made attempting harvesting impossible.                          the robot arm, and the range of the overhead camera viewport), such
      The 31 successful trajectories of the end effector are shown in         that it was physically not possible to pick some lettuce. If the
gray in Figure 14, with a representative trajectory highlighted in            limitations of the arm are ignored, and the denominator reflects only
black. This representative trajectory shows a single experiment               those lettuces within the practical workspace, then the detachment

T A B L E 6 Overall system performance in the harvesting tests. Total lettuces attempted considers only lettuces within restrictions imposed by
arm strength
    Metric                                            Result                                    Definition
    Total ground‐truth lettuces                       69
    Total lettuces detected                           61 (1 false positive)
    Total lettuces attempted                          32
    Total lettuces detached                           31
    Detachment success                                97%                                       Number of successfully picked qualified
                                                                                                    Number of detected qualified

    Harvest success                                   88%                                       (Lettuce localization success) × (detachment success)
    Cycle time                                        31.7 s, σ 2= 32.6                         Complete cycle time from lettuce to next

    Damage rate                                       38%                                       Number of lettuce harvested in unsaleable condition
                                                                                                             Total number harvested

    Leaves to be removed                              0.75, σ 2= 1.42                           Average leaves to be removed to achieve scalability

    Total lettuces attempted                          69

4
https://youtu.be/UR-7LBdI7Z4
240     |                                                                                                                              BIRRELL ET AL.

success rises to 97% (31 out of 32). In other words, with one               6 | D I S C U SS I O N
exception, if the arm could reach the lettuce, the end effector could
pick it. Although this is a considerable exception, it could be simply      There is much remaining work required to achieve an iceberg lettuce
achieved by using a robot arm with increased torque output.                 harvester for commercial operation. Existing challenges include visual
      Examples of the harvested lettuce are shown in Figure 15,             analysis, precise manipulator control, harvesting rig development, and
showing high‐quality cuts and also showing those with unwanted              reduction of the overall cycle time and costs. In this study the focus
outer leaves or damage. The distribution of the lettuces which              was not to develop a commercial product, but to demonstrate proof‐
required extra leaves to be removed, extra cutting attempts and the         of‐concept experiments which provide research outcomes which can
cycle time is shown in Figure 16. The cycle time varies greatly             aid future development of agricultural robotics systems not only for
depending on how far the arm needs to travel from lettuce to lettuce,       iceberg lettuce, but many other crops. This section discusses the
exacerbated by end‐effector weight slowing the movements. In a few          design rationale behind the development process and in particular the
cases, one extra leaf needed to be removed (manually) to achieve            visual processing strategies which were chosen and how these
supermarket perfection. Additionally, in some cases extra cuts were         approaches can be used to aid future work in this field.
required. This was often due to the leaves of the lettuce and                  The final prototype of Vegebot is a result of more than 15
movement of the lettuce head within the cutting area. Additionally,         iterations and on‐site field tests which were carried out in the UK
the cuts were generally a little too close to the body to be acceptable     harvest seasons (July–September) between 2016 and 2018, and also
in the current market.                                                      countless lab based experiments. In each iteration, new software and
      The average cycle time was 31.7 s, with a variance of 32.6 s.         hardware redesigns were tested in the field, data gathered, and
Again, this value was largely due to the limitations of the arm and the     results compared. The development approach adopted was to
weight of the end effector. Of the trajectory sections in Figure 14, all    produce a modular system to enable rapid integration and testing
but the short grasp‐cut section (2 s) have their speed limited by the       of the architecture systematically. Frequent field tests were used to
arm’s payload capacity. A much reduced cycle time should be                 provide feedback and to identifying the improvements required. As a
achievable with a stronger arm or lighter end effector. In addition,        consequence of this approach, the physical design changed radically
around a quarter of the cycle time is taken by the fine‐tuning of the       from week to week (see Figure 7). This process was kept grounded by
end‐effector position. Any improvements to the accuracy of the              the use of standard harvesting metrics (Bac et al., 2014) to monitor
overhead camera localization would further reduce the overall cycle         progress. The authors believe that this iterative approach is more
time.                                                                       likely to yield robust, field‐worthy robots than careful upfront design
      Reducing the damage rate (38%) will require further experi-           based on an idealized version of the problem.
mentation. Supermarket chains, the largest wholesale lettuce buyers,           As an example of the approach taken, the available visual data
have strict standards for the length of the cut stalk to improve the        sets of lettuces were not ideally suited for an optimal vision system.
vegetable’s appearance in packaging. According to these standards,          Two separate data sets, one for localization and one for classification,
esthetic rather than relevant to the lettuce’s suitability for eating or    were both of reasonable quality in themselves but in an ideal world
not, the end effector often missed the ideal length, cutting in most        would have been combined into one integrated whole. Rather than
cases slightly too close to the lettuce head. Of the 32 picks, only two     spend time and resources gathering yet another data set to replace
actually resulted in inedible lettuces. Improvement can probably be         them, the Vegebots neural networks were quickly adapted to make
made by refining the force‐feedback mechanism and perhaps                   use of what was available. This enabled the robot to detect lettuces
introducing field‐dependent depth calibration at the start of each          correctly, solving the problem for the time being and allowing work
session. This remains for future work.                                      on the overall system to continue. With future iterations and online
      Again, buyer standards dictate that a packaged lettuce should not     data‐gathering this architecture could be simplified once again into a
have too many superfluous leaves in the packaging. At present, a human      single, fully‐integrated CNN architecture.
harvester will deftly remove a few leaves after each pick before passing       It is noteworthy that a vision system based on a standard CNN
the lettuce onto the harvesting rig. The end effector left the picked       architecture was able to achieve the localization results that it did,
lettuce with an average of 0.75 additional leaves that are undesirable by   given the difficulty of the task for a human harvester. Many of the
these standards. These would have to be removed further down the            previous harvesting robots detailed in Section 2 required vision
production chain by hand, or in an automated fashion.                       systems carefully tailored to the fruit or vegetable in question (e.g.,
      It is worth noting that both the metrics for damage rate and          detecting color or depth). For example, broccoli heads are detected
leaves to be removed could be substantially improved by permitting a        using an elaborate pipeline of RGB‐D sensors, point clouds, and
greater range of appearance of the vegetable on supermarket                 feature extraction in Kusumam et al. (2016) and radicchios using hand‐
shelves. Until the robot improves, this suggests a dual pricing             crafted features and particle filters in Foglia and Reina (2006). CNNs,
strategy, with a higher price paid by the consumer for a “perfect”          together with some rapid and informal data gathering, proved “good
hand‐picked lettuce and a lower price for a more variable but quite         enough” for the nontrivial localization of iceberg and may turn out to
edible robot‐picked one.                                                    be sufficient for other crops (Kamilaris & Prenafeta‐Boldú, 2018).
BIRRELL ET AL.                                                                                                                                   | 241
    Considering the mechanical development, by making field testing          success of 91% and a classification accuracy of 82% when tested on a
central to the project, the robot design naturally adapted itself to real‐   significant test data set. The average cycle time on Vegebot (31.7 s)
world commercial conditions. Vegebot operates in the same fields and         was restricted by the weight of the end effector and thus currently
along the same lane layout as human harvesters. Neither the                  slower than humans, but could be easily improved in subsequent
environment nor the crop itself was altered in any way to facilitate         versions made from lighter materials. Although the harvest success
the automated harvesting. By contrast, solutions using water knives          rate was high (88.2%) the damage rate was poor (38%). The sample
require careful selection of the crop variety and modifications to the       size of 60 lettuce demonstrates potential and identifies that future
way they are planted (Simon, 2017). Vegebot‐derived solutions could be       work is required to reduce the damage rate. Further optimization is
gradually deployed alongside existing methods, rather than requiring         required to meet supermarket standards.
major changes to existing practices. The control and calibration                 In comparison with other work in this study ecosystem, we have
software was repeatedly simplified to provide a solution that worked         demonstrated a number of new approaches and techniques for
robustly in the field. Sensors were stripped out, not added. Complex         agricultural robotics. In using a two‐stage CNN we have used an “out‐
algorithms to model in 3D and determine the optimal cutting position         of‐the box” learning system for a specific agricultural problem as
were replaced with mechanical legs that provided force feedback from         opposed to creating a bespoke system for this particular problem.
the ground, giving the robot a simple signal on when to cut. A design        This is different from many state‐of‐the‐art solutions (Berenstein
change was considered an improvement whenever a mechanical feature           et al., 2010; Ren et al., 2015). We have also explored how this
or software module was eliminated. In the long term, this preference for     approach can make best use of the available data sets and can
simplicity over sophisticated solutions may prove limiting, yet Vegebot      implement full data collection, training, and testing. Additionally, in
has already achieved important results. The use of standard metrics as       the development of the mechanical components of the harvesting
proposed by Bac et al. (2014) kept the project on track and focused on       system we have shown how the environmental constraints can be
steady, incremental improvements. The authors feeling is that the            exploited. This has been shown to help achieve a consistent cutting
iterative, simple approach can yield yet many more dividends before          height. This use of the environment, and designing mechanical
being exhausted.                                                             systems to work within an existing agricultural environment, is
    As the project stands, the damage rate, caused by cutting the            different to many other approaches. This presents an approach to
lettuce stem too short, is too high for supermarket standards, although      achieve robustness in challenging agricultural environments.
the harvested vegetables were perfectly edible. The most recent                  While the immediate future would appear to be robot arms
sample size of 69 lettuces was enough to confirm this as the next            attached to harvesting rigs, an autonomous Vegebot is also a distinct
problem to address (hundreds of lettuces had been harvested over             possibility. While its capacity would clearly be more limited, it would
previous iterations). Future versions of Vegebot will need to address        have agility in the sense of responding quickly to sudden spikes in
and improve the damage rate, perhaps with visual feedback from the           demand. Marshaling a human team and a harvesting rig can be difficult
harvested lettuces dynamically adjusting the force threshold at which        at short notice and may be overkill for unexpected but smaller orders,
the cut is made. In parallel, the end effector needs to be made lighter      whereas an autonomous Vegebot could be conveniently sent into the
to achieve a human‐level cycle time, possibly by manufacturing with          field to fulfill them. Outside of harvesting time, it could also be used for
carbon fiber, or by using an alternative, stronger cartesian arm design.     data gathering. The vision and learning system in combination with the
    In summary, the adaptation of CNNs to pre‐existing data sets and         end‐effector system provides the potential for selective plant harvest-
the use of simple, low‐sensory, environmental feedback may prove             ing. This could increase crop and harvesting efficiency.
useful in other harvesting projects. The authors key recommendation              Agriculture is an industry where margins are low; cost efficiency
would be rapid iteration with radically different hardware designs,          and time efficiency are key. To make the presented approach viable,
testing in the field as often as possible and relentlessly simplifying       the cycle time would need to be reduce to that comparable to humans.
and using the standard metrics to stay on track.                             However, using a robotic system would enable certain advantages
                                                                             such as a more flexible work force and nighttime operation. The
                                                                             techniques and approaches here have been applied to iceberg lettuce;
7 | CONC LU SION S                                                           however, the concepts could be applied to other harvesting and
                                                                             robotic agriculture situations. Further work to investigate wider
This paper presented a proof‐of‐concept platform called Vegebot              applicability, and developing a more universal harvesting system would
that demonstrated an automated and potentially autonomous                    increase both commercial and research impact.
approach to harvesting iceberg lettuces. The vision system,
mechanics, and control strategy were described and the experi-
mental results detailed.                                                     ACKN OWL EDGMENTS
    The goals of the project were to achieve a robust localization and
classification, to achieve a cycle time comparable to humans and to          This project was possible thanks to EPSRC Grant EP/L015889/1, the
avoid damage to harvested lettuces. The localization and classifica-         Royal Society ERA Foundation Translation Award (TA160113), EPSRC
tion were reasonably robust, as demonstrated by a localization               Doctoral Training Program ICASE AwardRG84492 (cofunded by G’s
242    |                                                                                                                                               BIRRELL ET AL.

Growers), EPSRC Small Partnership AwardRG86264 (in collaboration                      Kiani, S., Azimifar, Z., & Kamgar, S. (2010). Wavelet‐based crop detection
with G’s Growers), and the BBSRC Small Partnership GrantRG81275.                          and classification. 2010 18th Iranian Conference on Electrical Engineer-
                                                                                          ing (ICEE). Isfahan: IEEE, 587–591.
In addition, we are extremely grateful from the support and valuable
                                                                                      Kurita, H., Iida, M., Cho, W., & Suguri, M. (2017). Rice autonomous harvesting:
time input from G’s Growers, in particular Charlie Kisby, John Currah,                    Operation framework. Journal of Field Robotics, 34(6), 1084–1099.
James Green, and Jacob Kirwan. We would also like to thank Dr. Alex                   Kusumam, K., Krajnik, T., Pearson, S., Cielniak, G., & Duckett, T. (2016).
Jones from the Sainsburys Laboratory and many who have contributed                        Can you pick a broccoli? 3d‐vision based detection and localisation of
                                                                                          broccoli heads in the field. 2016 IEEE/RSJ International Conference on
to the iterations of Vegebot: Luca Scimeca, Andre Rosendo, Fabio
                                                                                          Intelligent Robots and Systems (IROS). Deajeon: IEEE.
Giardina, Claudio Ravasio, and Vivian Wong.                                           Lottes, P., Hörferlin, M., Sander, S., & Stachniss, C. (2017). Effective vision‐
                                                                                          based classification for separating sugar beets and weeds for
                                                                                          precision farming. Journal of Field Robotics, 34(6), 1160–1178.
OR CID                                                                                Luo, L., Tang, Y., Zou, X., Wang, C., Zhang, P., & Feng, W. (2016). Robust
                                                                                          grape cluster detection in a vineyard by combining the adaboost
Josie Hughes       http://orcid.org/0000-0001-8410-3565                                   framework and multiple color components. Sensors, 16(12), 2098.
                                                                                      Mehta, S. S., & Burks, T. (2014). Vision‐based control of robotic
                                                                                          manipulator for citrus harvesting. Computers and Electronics in
REFERENC ES                                                                               Agriculture, 102, 146–158.
                                                                                      Mehta, S. S., MacKunis, W., & Burks, T. F. (2016). Robust visual servo
Bac, C. W., Hemming, J., van Tuijl, B., Barth, R., Wais, E., & van Henten, E. J.          control in the presence of fruit motion for robotic citrus harvesting.
    (2017). Performance evaluation of a harvesting robot for sweet                        Computers and Electronics in Agriculture, 123, 362–375.
    pepper. Journal of Field Robotics, 34(6), 1123–1139.                              Monta, M., Kondo, N., & Shibano, Y. (1995). Agricultural robot in grape
Bac, C. W., van Henten, E. J., Hemming, J., & Edan, Y. (2014). Harvesting                 production system. Proceedings of 1995 IEEE International Conference
    robots for high‐value crops: State‐of‐the‐art review and challenges                   on Robotics and Automation. Nagoya, Japan: IEEE, 3, 2504–2509.
    ahead. Journal of Field Robotics, 31(6), 888–911.                                 Nagrani, A. (2015). Deepfarm: Lettuce image classification using deep
Bechar, A., & Vigneault, C. (2016). Agricultural robots for field                         learning. undergraduate project. University of Cambridge. http://
    operations: Concepts and components. Biosystems Engineering,                          mi.eng.cam.ac.uk/projects/lettuce/
    149, 94–111.                                                                      Nieuwenhuizen, A., Hofstee, J., & Van Henten, E. (2010). Adaptive
Berenstein, R., Shahar, O. B., Shapiro, A., & Edan, Y. (2010). Grape clusters             detection of volunteer potato plants in sugar beet fields. Precision
    and foliage detection algorithms for autonomous selective vineyard                    Agriculture, 11(5), 433–447.
    sprayer. Intelligent Service Robotics, 3(4), 233–243.                             Oetomo, D., Billingsley, J., & Reid, J. F. (2009). Agricultural robotics.
Botterill, T., Paulin, S., Green, R., Williams, S., Lin, J., Saxton, V., & Corbett‐       Journal of Field Robotics, 26(6‐7), 501–503.
    Davies, S. (2017). A robot system for pruning grape vines. Journal of             Ottaway, J. N. (1996). Lettuce harvesting method and apparatus to
    Field Robotics, 34(6), 1100–1122.                                                     perform the same. U.S. Patent No. 5,560,190.
Cubero, S., Alegre, S., Aleixos, N., & Blasco, J. (2015). Computer vision system      Ottaway, J. (2009). Method and apparatus for harvesting lettuce. U.S.
    for individual fruit inspection during harvesting on mobile platforms. In J.          Patent No. 8,272,200.
    V. Stafford (Ed.), Precision Agriculture’15 1, (pp. 3412–3419). Wageningen,       Rajendra, P., Kondo, N., Ninomiya, K., Kamata, J., Kurita, M., Shiigi, T., …
    Netherlands: Wageningen Academic Publishers.                                          Kohno, Y. (2008). Machine vision algorithm for robots to harvest
De‐An, Z., Jidong, L., Wei, J., Ying, Z., & Yu, C. (2011). Design and control             strawberries in tabletop culture greenhouses. Engineering in Agricul-
    of an apple harvesting robot. Biosystems Engineering, 110(2), 112–122.                ture, Environment and Food, 2(1), 24–30.
Edan, Y., Han, S., & Kondo, N. (2009). Automation in agriculture. In S. Y.            Reddy, N. V., Reddy, A. V. V., Pranavadithya, S., & Kumar, J. J. (2016). A
    Nof (Ed.), Springer handbook of automation (pp. 1095–1128). Germany:                  critical review on agricultural robots. International Journal of Mechan-
    Springer.                                                                             ical Engineering and Technology, 7(4), 183–188.
Evert van, F., Samsom, J., Polder, G., Vijn, M., Dooren van, H., Lamaker, E., &       Redmon, J. (2013). Darknet: Open source neural networks in c. Retrieved
    Lotz, L. (2011). A robot to detect and control broad‐leaved dock (rumex               from http://pjreddie.com/darknet/
    obtusifolius l.) in grassland. Journal of Field Robotics, 28(2), 264–277.         Redmon, J., & Farhadi, A. (2018). Yolov3: An incremental improvement.
Foglia, M. M., & Reina, G. (2006). Agricultural robot for radicchio                       Retrieved from https://arxiv.org/abs/1804.02767
    harvesting. Journal of Field Robotics, 23(6‐7), 363–377.                          Ren, S., He, K., Girshick, R., & Sun, J. (2015). Faster r‐cnn: Towards real‐
Hajjaj, S. S. H., & Sahari, K. S. M. (2016). Review of agriculture robotics:              time object detection with region proposal networks. Advances in
    Practicality and feasibility. 2016 IEEE International Symposium on                    neural information processing systems. Montreal, 91–99.
    Robotics and Intelligent Sensors (IRIS). Tokyo: IEEE, 194–198.                    Scarfe, A. J., Flemmer, R. C., Bakker, H., & Flemmer, C. L. (2009). Development
Harrell, R., Adsit, P. D., Munilla, R., & Slaughter, D. (1990). Robotic picking           of an autonomous kiwifruit picking robot. 4th International Conference on
    of citrus. Robotica, 8(4), 269–278.                                                   Autonomous Robots and Agents, 2009, ICARA 2009, Wellington, New
Hayashi, S., Shigematsu, K., Yamamoto, S., Kobayashi, K., Kohno, Y.,                      Zealand: IEEE, 380–384.
    Kamata, J., & Kurita, M. (2010). Evaluation of a strawberry‐                      Shepardson, E., & Pollock, J. (1974). Lettuce harvesting apparatuss. U.S.
    harvesting robot in a field test. Biosystems Engineering, 105(2),                     Patent No. 3,821,987.
    160–171.                                                                          Silwal, A., Davidson, J. R., Karkee, M., Mo, C., Zhang, Q., & Lewis, K. (2017).
Hughes, J., Scimeca, L., Ifrim, I., Maiolino, P., & Iida, F. (2018). Achieving            Design, integration, and field evaluation of a robotic apple harvester.
    robotically peeled lettuce. IEEE Robotics and Automation Letters, 3(4),               Journal of Field Robotics, 34(6), 1140–1159.
    4337–4342.                                                                        Simon, M. (2017). Robots wielding water knives are the future of farming.
Kamilaris, A., & Prenafeta‐Boldú, F. X. (2018). Deep learning in agriculture: A           Wired Magazine. https://www.wired.com/2017/05/robots‐agriculture/
    survey. Computers and Electronics in Agriculture, 147, 70–90.                     Van Henten, E. J., van Tuijl, B., Hoogakker, G.‐J., Van Der Weerd, M.,
Kemp, C. C., Edsinger, A., & Torres‐Jara, E. (2007). Challenges for robot                 Hemming, J., Kornet, J., & Bontsema, J. (2006). An autonomous robot
    manipulation in human environments [grand challenges of robotics].                    for de‐leafing cucumber plants grown in a high‐wire cultivation
    IEEE Robotics and Automation Magazine, 14(1), 20–29.                                  system. Biosystems Engineering, 94(3), 317–323.
BIRRELL ET AL.                                                                                                                                      | 243
Van Henten, E. J., Hemming, J., van Tuijl, B., Kornet, J., Meuleman, J.,           APP ENDIX B: SOFTWA RE
   Bontsema, J., & Van Os, E. (2002). An autonomous robot for harvesting
   cucumbers in greenhouses. Autonomous Robots, 13(3), 241–258.
                                                                                   The software (see Figure B1a) was written on the kinetic release of
Vott, M. (2018). Visual object tagging tool: An electron app for building end to
   end object detection models from images and videos. Retrieved from              robot operating system (ROS). Custom ROS modules for Vegebot
   https://github.com/Microsoft/VoTT                                               were written in Python and are bundled as the package vegebot5:

     How to cite this article: Birrell S, Hughes J, Cai JY, Iida F.                • vegebot_commander: This node is responsible for receiving user
     A field‐tested robotic harvesting system for iceberg                              commands from the web‐based user interface front‐end and either
     lettuce. J Field Robotics. 2020;37:225–245.                                       executing them or passing them to the appropriate node.
     https://doi.org/10.1002/rob.21888                                             • lettuce_detect: This node encapsulates the code that classifies and
                                                                                       localizes lettuces from a 2D image. It calls the two deep neural
                                                                                       networks running on Darknet.
                                                                                   • lettuce_sampler: This node supplies sample 2D lettuce imagery for
AP PEN D IX A: IN DEX TO M ULT IME DIA                                                 testing purposes when not in the field.
E X T E N S IO N S                                                                 • vegebot_msgs: This node defines the custom ROS messages used
                                                                                       for internode communication, including lettuce hypotheses.
           Media                                                                   • vegebot_webserver: This node serves the HTML front‐end user
 Extension type           Description                                                  interface to the robot operator.
 1               Image    Overhead view of lettuces                                • vegebot_run: This module contains the 3D model of the Vegebot
                                                                                       (in URDF format) and the scripts for launching the entirety of the
 2               Image    A lettuce harvesting rig with workers
                                                                                       software under different conditions.
 3               Image    The Vegebot lettuce harvesting robot
                                                                                        Standard ROS hardware drivers (universal_robot, ur_modern, and
 4               Image    Block diagram of Vegebot
                                                                                   usb_cam) are used to drive the UR10 arm and the webcams. A
 5               Image    Process diagram of Vegebot                               standard installation of Darknet (Redmon, 2013) with YOLOv3 was
 6               Image    Scientist gathering data in lettuce field—two            accelerated by CUDA drivers version 9 to provide image detection
                           photos                                                  services. The HTML user interface (see Figure B1b) can be operated
                                                                                   on the same control laptop or remotely, via an onboard WiFi router.
 7               Image    Image pipeline of Vegebot
                                                                                   The two cameras stream live video to the user interface and
 8               Image    Four photos of four end effectors                        bounding boxes and classes for the detected lettuces are overlaid.
 9               Image    Labelled photo of final end effector                     The position of the calibration marker is also shown. The roslib.js
                                                                                   library provides an interactive 3D model of the robot which displays
 10              Image    Diagram of how end effector works
                                                                                   the real robot’s movements. The force feedback on the end effector
 11              Image    Overhead diagram of end effector positioning             is shown by three bar graphs to the left of the display. Detected
                           over lettuce                                            lettuces are added dynamically as menu items to the screen, using
 12              Image    Distribution diagram                                     the d3.js library. The operator can test individual actions (such as
                                                                                   “move to pregrasp position”) or simply select a detected lettuce and
 13              Image    Two line graphs with photos below
                                                                                   instruct Vegebot to pick and place it.
 14              Image    Four photos of lettuces with bounding boxes

 15              Image    Line graph
                                                                                   APP ENDIX C : CA LIBRATION D ETAILS
 16              Image    Confusion matrix

 17              Image    Diagram of trajectories                                  The full calibration sequence was as follows and is summarized in
                                                                                   Figure C1.
 18              Image    Five photos of lettuces

 19              Image    Three distribution graphs                                1. Manually position the end effector over any lettuce X using
                                                                                       standard UR10 controls.
 20              Image    Software architecture
                                                                                   2. Manually raise the end effector vertically until approximately
 21              Image    User interface
                                                                                       10 cm clear of the lettuce.
 22              Image    Calibration diagram

                                                                                   5
                                                                                    https://bitbucket.org/robotlux/vegebot/src/master/
244     |                                                                                                                                BIRRELL ET AL.

FIGURE B1            (a) The software architecture of Vegebot showing the structure and various packages used. (b) The web‐based user interface
for Vegebot

3. Trigger automatic calibration:                                             position” phase of the pick sequence (see Figure 4). For further
      (a) The center pixel of the bounding box for lettuce X in the end‐      details of the calculations, see Appendix C.
            effector camera is recorded as the target center pixel for           This rough positioning proved robust enough to move the end
            fine‐tuning (the camera is not centered in the end effector for   effector into the pregrasp position, but not to exactly center it
            space reasons)                                                    accurately over the top of the lettuce. At this point, the end effector
      (b) The calibration records the vertical position of the end            “fine‐tunes” the position using a simple visual servoing method. The
            effector (Z axis in ROS) and assumes this to be the height of     bounding box of the target lettuce is now visible in the end‐effector
            the plane containing all future “pregrasp” positions.             video feed (see Figure B1b, right‐hand video feed for an example),
      (c) The end effector then moves to three positions at the edges         the center point is calculated and then the arm is moved in the
            of the viewport, in the same horizontal plane. Each position is   horizontal plane (along the X and Y axes) until this center point
            recorded in terms of the X, Y, Z of the end effector in the       coincides roughly with the target pixel recorded in Step 3a of the
            robot arm’s coordinate frame and in terms of the u,v center       calibration sequence. The end effector is now positioned over the
            pixel of the detected Aruco marker.                               center of the target lettuce and can then descend vertically.
                                                                                 While the full calibration sequence involves human input to
      The three calibration positions define a horizontal plane with          position the end effector over a sample lettuce, the resampling of the
respect to the ground, around 10 cm over the tops of the lettuces.            horizontal plane itself is automatic and could be triggered without
Given any pixel u,v in the viewport, the corresponding x, y, z in the         human intervention on an as‐needed basis, for instance when the
horizontal plane can be found by linear interpolation between these           ‘fine‐tuning’ phase of the trajectory starts to take too long or to fail.
three points. The UR10’s built‐in inverse kinematics were then used              The calibration procedure is always undertaken when the
to move the end effector into position in the “approach pregrasp              Vegebot is positioned at the start of a lettuce lane. When the

                                                                                                         F I G U R E C 1 Calibration method,
                                                                                                         showing how position and camera
                                                                                                         coordinates are gained from three
                                                                                                         positions to allow a mapping from camera
                                                                                                         to real‐world coordinates to be achieved
BIRRELL ET AL.                                                                                                                           | 245
                                                                                                           vt − ūt v2/ ū2
platform is manually moved between harvesting sessions, there is a                                    b=                                   (C2)
                                                                                                            v3 ū3 v2/ ū2
human decision (see Figure 4) on whether recalibration is required, if
for example the change in terrain has caused the relative position of        and
the platform to the field to change. This can be seen in the increasing
                                                                                                            v3 − bū3
amount of time taken to fine‐tune the end‐effector position.                                           a=            .                     (C3)
                                                                                                               ū2
Long term, this process would be automated. Three calibration
points in robot space (see Figure C1) are found (P1, P2 , P3 ) and their        This allows an equivalent point in robot space to be found as
equivalent viewpoint coordinate are found in the camera space (C1 ,
                                                                                                     Pt = Pt − P1
C2 , C3 ). Any viewpoint coordinate, Ct (ut , vt ) can be expressed as the                                                                 (C4)
                                                                                                         = aP2 + bP3.
sum of two vectors:

                                                                                Such that the point Ct transformed into robot space can be
                 Ct = aC2 + bC3,   where C2 = C2 − C1,
                                           C3 = C3 − C1,             (C1)    calculated by
                                           Ct = Ct − C1.                                                                                   (C5)
                                                                                                    Pt = P1 + aP2 + bP3.

    The values of a and b can be found as
