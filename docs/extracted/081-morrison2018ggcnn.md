---
source_id: 081
bibtex_key: morrison2018ggcnn
title: Closing the Loop for Robotic Grasping: A Real-Time, Generative Grasp Synthesis Approach
year: 2018
domain_theme: Grasp Robotik
verified_pdf: 81_GG-CNN.pdf
char_count: 68598
---

Closing the Loop for Robotic Grasping:
                                         A Real-time, Generative Grasp Synthesis Approach
                                                                             Douglas Morrison, Peter Corke and Jürgen Leitner
                                                                                       Australian Centre for Robotic Vision
                                                                                       Queensland University of Technology
                                                                                             Brisbane, Australia, 4000
                                                                                      Email: douglas.morrison@hdr.qut.edu.au

                                            Abstract—This paper presents a real-time, object-independent
arXiv:1804.05172v2 [cs.RO] 15 May 2018

                                         grasp synthesis method which can be used for closed-loop
                                         grasping. Our proposed Generative Grasping Convolutional
                                         Neural Network (GG-CNN) predicts the quality and pose of
                                         grasps at every pixel. This one-to-one mapping from a depth
                                         image overcomes limitations of current deep-learning grasping
                                         techniques by avoiding discrete sampling of grasp candidates and
                                         long computation times. Additionally, our GG-CNN is orders of
                                         magnitude smaller while detecting stable grasps with equivalent
                                         performance to current state-of-the-art techniques. The light-
                                         weight and single-pass generative nature of our GG-CNN allows
                                         for closed-loop control at up to 50Hz, enabling accurate grasping
                                         in non-static environments where objects move and in the
                                         presence of robot control inaccuracies. In our real-world tests,    Fig. 1. Our real-time, generative grasping pipeline. A camera mounted to the
                                         we achieve an 83% grasp success rate on a set of previously         wrist of the robot captures depth images containing an object to be grasped.
                                         unseen objects with adversarial geometry and 88% on a set of        Our Generative Grasping Convolutional Neural Network (GG-CNN) generates
                                                                                                             antipodal grasps – parameterised as a grasp quality, angle and gripper width –
                                         household objects that are moved during the grasp attempt. We
                                                                                                             for every pixel in the input image in a fraction of a second. The best grasp is
                                         also achieve 81% accuracy when grasping in dynamic clutter.         calculated and a velocity command (v) is issued to the robot. The closed-loop
                                                                                                             system is capable of grasping dynamic objects and reacting to control errors.
                                                               I. I NTRODUCTION
                                            In order to perform grasping and manipulation tasks in the       input depth image and is fast enough for closed-loop control
                                         unstructured environments of the real world, a robot must be        of grasping in dynamic environments (Fig. 1). We use the
                                         able to compute grasps for the almost unlimited number of           term “generative” to differentiate our direct grasp generation
                                         objects it might encounter. In addition, it needs to be able to     method from methods which sample grasp candidates.
                                         act in dynamic environments, whether that be changes in the            The advantages of GG-CNN over other state-of-the-art
                                         robot’s workspace, noise and errors in perception, inaccuracies     grasp synthesis CNNs are twofold. Firstly, we do not rely on
                                         in the robot’s control, or perturbations to the robot itself.       sampling of grasp candidates, but rather directly generate grasp
                                            Robotic grasping has been investigated for decades, yielding     poses on a pixelwise basis, analogous to advances in object
                                         a multitude of different techniques [2, 3, 27, 29]. Most            detection where fully-convolutional networks are commonly
                                         recently, deep learning techniques have enabled some of the         used to perform pixelwise semantic segmentation rather than
                                         biggest advancements in grasp synthesis for unknown items.          relying on sliding windows or bounding boxes [19]. Secondly,
                                         These approaches allow learning of features that correspond         our GG-CNN has orders of magnitude fewer parameters than
                                         to good quality grasps that exceed the capabilities of human-       other CNNs used for grasp synthesis, allowing our grasp
                                         designed features [12, 17, 21, 23].                                 detection pipeline to execute in only 19 ms on a GPU-equipped
                                            However, these approaches typically use adapted versions of      desktop computer, fast enough for closed-loop grasping.
                                         Convolutional Neural Network (CNN) architectures designed              We evaluate the performance of our system in different
                                         for object recognition [12, 15, 23, 25], and in most cases          scenarios by performing grasping trials with a Kinova Mico
                                         sample and rank grasp candidates individually [17, 21, 23],         robot, with static, dynamic and cluttered objects. In dynamic
                                         resulting in long computation times in the order of a sec-          grasping trials, where objects are moved during the grasp
                                         ond [21] to tens of seconds [17]. As such, these techniques         attempt, we achieve 83% grasping success rate on a set of
                                         are rarely used in closed-loop grasp execution and rely on          eight 3D-printed objects with adversarial geometry [21] and
                                         precise camera calibration and precise robot control to grasp       88% on a set of 12 household items chosen from standardised
                                         successfully, even in static environments.                          object sets. Additionally, we reproduce the dynamic clutter
                                            We propose a different approach to selecting grasp points        grasping experiments of [32] and show an improved grasp
                                         for previously unseen items. Our Generative Grasping Con-           success rate of 81%. We further illustrate the advantages of
                                         volutional Neural Network (GG-CNN) directly generates an            using a closed-loop method by reporting experimental results
                                         antipodal grasp pose and quality measure for every pixel in an      when artificial inaccuracies are added to the robot’s control.
                                      [17]           [25]       [23]       [12]        [15]        [21]        [18]       [32]       Ours
     Real Robot Experiments            X              ×          X          X           ×           X           X          X           X
     Objects from Standard Sets        ×              -          ×          ×           -           ×           ×          ×           X
     Adversarial Objects [21]          ×              -          ×          ×           -           X           ×          ×           X
     Clutter                           ×              ×          X          ×           ×           ×           X          X           X
     Closed-loop                       ×              -          ×          ×           -           ×           X          X           X
     Dynamic Objects                   ×              -          ×          ×           -           ×           ×          X           X
     Code Available                    X              ×          X          ×           ×           X           ×          ×          X*
     Training Data Available           X              X          X          ×           X           X           X          ×           X
     Training Data Type               Real           Real       Real     Synthetic     Real      Synthetic     Real     Synthetic     Real
                                  (Cornell [17])   (Cornell)   (Trial)               (Cornell)                (Trial)               (Cornell)

                  TABLE I: A comparison of our work to related deep learning approaches to grasp synthesis.
                                           * Code is available at https://github.com/dougsm/ggcnn

                      II. R ELATED W ORK                                   itself may not be a valid grasp [25].
                                                                              Similar to our method, Varley et al. [31] use a neural
   Grasping Unknown Objects Grasp synthesis refers to the                  network to generate pixelwise heatmaps for finger placement
formulation of a stable robotic grasp for a given object, which            in an image, but still rely on a grasp planner to determine the
is a topic which has been widely researched resulting in a                 final grasp pose.
plethora of techniques. Broadly, these can be classified into                 We address the issues of execution time and grasp sampling
analytic methods and empirical methods [3, 27]. Analytic                   by directly generating grasp poses for every pixel in an image
methods use mathematical and physical models of geometry,                  simultaneously, using a comparatively small neural network.
kinematics and dynamics to calculate grasps that are sta-                     Closed-Loop Grasping Closed-loop control of a robot to
ble [2, 24], but tend to not transfer well to the real world due           a desired pose using visual feedback is commonly referred to
to the difficultly in modelling physical interactions between a            as visual servoing. The advantages of visual servoing methods
manipulator and an object [2, 26, 27].                                     are that they are able to adapt to dynamic environments and
   In contrast, empirical methods focus on using models and                do not necessarily require fully accurate camera calibration
experience-based approaches. Some techniques work with                     or position control. A number of works apply visual servoing
known items, associating good grasp points with an offline                 directly to grasping applications, with a survey given in [14].
database of object models or shapes [6, 8, 22], or familiar                However, the nature of visual servoing methods mean that
items, based on object classes [28] or object parts [7], but are           they typically rely on hand-crafted image features for object
unable to generalise to new objects.                                       detection [13, 30] or object pose estimation [11], so do not
   For grasping unknown objects, large advancements have                   perform any online grasp synthesis but instead converge to a
been seen recently with a proliferation of vision-based deep-              pre-determined goal pose and are not applicable to unknown
learning techniques [17, 21, 23, 25, 33]. Many of these tech-              objects.
niques share a common pipeline: classifying grasp candidates                  CNN-based controllers for grasping have very recently
sampled from an image or point cloud, then ranking them                    been proposed to combine deep learning with closed loop
individually using Convolutional Neural Networks (CNN).                    grasping [18, 32]. Rather than explicitly performing grasp
Once the best grasp candidate is determined, a robot executes              synthesis, both systems learn controllers which map potential
the grasp open-loop (without any feedback) which requires                  control commands to the expected quality of or distance to a
precise calibration between the camera and the robot, precise              grasp after execution of the control, requiring many potential
control of the robot and a completely static environment.                  commands to be sampled at each time step. In both cases, the
   Execution time is the primary reason that grasps are exe-               control executes at no more than approximately 5 Hz. While
cuted open-loop. In many cases, deep-learning approaches use               both are closed-loop controllers, grasping in dynamic scenes
large neural networks with millions of parameters [12, 21, 23]             is only presented in [32] and we reproduce these experiments.
and process grasp candidates using a sliding window at                        The grasp regression methods [15, 25] report real-time
discrete intervals of offset and rotation [17, 23], which is               performance, but are not validated with robotic experiments.
computationally expensive and results in grasp planning times                 Benchmarking for Robotic Grasping Directly comparing
in the order of a second [21] to tens of seconds [17].                     results between robotic grasping experiments is difficult due
   Some approaches reduce execution time by pre-processing                 to the wide range of grasp detection techniques used, the
and pruning the grasp candidates [17, 33] or predicting                    lack of standardisation between object sets, and the limitations
the quality of a discrete set of grasp candidates simultane-               of different physical hardware, e.g. robot arms, grippers or
ously [12, 23], trading off execution time against the number of           cameras. Many people report grasp success rates on sets of
grasps which are sampled, but ignoring some potential grasps.              “household” objects, which vary significantly in the number
   Instead of sampling grasp candidates, both [15] and [25]                and types of objects used.
use a deep CNN to regress a single best grasp pose for an                     The ACRV Picking Benchmark (APB) [16] and the YCB
input image. However, these regression methods are liable to               Object Set [5] define item sets and manipulation tasks, but
output the average of the possible grasps for an object, which             benchmark on tasks such as warehouse order fulfilment (APB)
                                                                                   where tRC transforms from the camera frame to the
                                                                                   world/robot frame and tCI transforms from 2D image co-
                                                                                   ordinates to the 3D camera frame, based on the camera
                                                                                   intrinsic parameters and known calibration between the robot
                                                                                   and camera.
                                                                                      We refer to the set of grasps in the image space as the grasp
                                                                                   map, which we denote
                                                                                                    G = (Φ, W, Q) ∈ R3×H×W
                                                                                   where Φ, W and Q are each ∈ RH×W and contain values of
Fig. 2. Left: A grasp g is defined by its Cartesian position (x, y, z), rotation   φ̃, w̃ and q respectively at each pixel s.
around the z-axis φ and gripper width w required for a successful grasp. Right:       Instead of sampling the input image to create grasp candi-
In the depth image the grasp pose g̃ is defined by its centre pixel (u, v), its
rotation φ̃ around the image axis and perceived width w̃.                          dates, we wish to directly calculate a grasp g̃ for each pixel in
                                                                                   the depth image I. To do this, we define a function M from
or table setting and block stacking (YCB) rather than raw grasp                    a depth image to the grasp map in the image coordinates:
success rate as is typically reported. Additionally, many of the                   M (I) = G. From G we can calculate the best visible grasp
items from these two sets are impractically small, large or                        in the image space g̃∗ = max G, and calculate the equivalent
heavy for many robots and grippers, so have not been widely                                                     Q
adopted for robotic grasping experiments.                                          best grasp in world coordinates g∗ via Eq. (1).
   We propose a set of 20 reproducible items for testing, com-                         IV. G ENERATIVE G RASPING C ONVOLUTIONAL
prising comprising 8 3D printed adversarial objects from [21]                                        N EURAL N ETWORK
and 12 items from the APB and YCB object sets, which we
                                                                                      We propose the use of a neural network to approximate the
believe provide a wide enough range of sizes, shapes and
                                                                                   complex function M : I → G. Mθ denotes a neural network
difficulties to effectively compare results while not excluding
                                                                                   with θ being the weights of the network.
use by any common robots, grippers or cameras.
                                                                                      We show that Mθ (I) = (Qθ , Φθ , Wθ ) ≈ M (I), can be
   In Table I we provide a summary of the recent related work                      learned with a training set of inputs IT and corresponding
on grasping for unknown objects, and how they compare to                           outputs GT and applying the L2 loss function L, such that
our own approach. This is not intended to be a comprehensive
review, but rather to highlight the most relevant work.                                             θ = argmin L(GT , Mθ (IT )).
                                                                                                            θ
                   III. G RASP P OINT D EFINITION                                  A. Grasp Representation
   Like much of the related literature [12, 17, 21, 23, 32],                          G estimates the parameters of a set of grasps, executed
we consider the problem of detecting and executing antipodal                       at the Cartesian point p, corresponding to each pixel s. We
grasps on unknown objects, perpendicular to a planar surface,                      represent the grasp map G as a set of three images, Q, Φ and
given a depth image of the scene (Fig. 2).                                         W. The representations are as follows:
   Let g = (p, φ, w, q) define a grasp, executed perpendic-                           Q is an image which describes the quality of a grasp
ular to the x-y plane. The grasp is determined by its pose,                        executed at each point (u, v). The value is a scalar in the
i.e. the gripper’s centre position p = (x, y, z) in Cartesian                      range [0, 1] where a value closer to 1 indicates higher grasp
coordinates, the gripper’s rotation φ around the z axis and                        quality, i.e. higher chance of grasp success.
the required gripper width w. A scalar quality measure q,                             Φ is an image which describes the angle of a grasp to
representing the chances of grasp success, is added to the pose.                   be executed at each point. Because the antipodal grasp is
The addition of the gripper width enables a better prediction                      symmetrical around ± π2 radians, the angles are given in the
and better performance over the more commonly used position                        range [− π2 , π2 ].
and rotation only representation.
                                                                                      W is an image which describes the gripper width of a grasp
   We want to detect grasps given a 2.5D depth image I =
                                                                                   to be executed at each point. To allow for depth invariance,
RH×W with height H and width W , taken from a camera
                                                                                   values are in the range of [0, 150] pixels, which can be
with known intrinsic parameters. In the image I a grasp is
                                                                                   converted to a physical measurement using the depth camera
described by
                                                                                   parameters and measured depth.
                        g̃ = (s, φ̃, w̃, q),
                                                                                   B. Training Dataset
where s = (u, v) is the centre point in image coordinates
(pixels), φ̃ is the rotation in the camera’s reference frame and                      To train our network, we create a dataset (Fig. 3) from
w̃ is the grasp width in image coordinates. A grasp in the                         the Cornell Grasping Dataset [17]. The Cornell Grasping
image space g̃ can be converted to a grasp in world coordinates                    Dataset contains 885 RGB-D images of real objects, with
g by applying a sequence of known transforms,                                      5110 human-labelled positive and 2909 negative grasps. While
                                                                                   this is a relatively small grasping dataset compared to some
                            g = tRC (tCI (g̃))                              (1)    more recent, synthetic datasets [20, 21], the data best suits
                                                                             width of the gripper and set the corresponding portion of WT .
                                                                                                                              1
                                                                             During training, we scale the values of WT by 150   to put it in
                                                                             the range [0, 1]. The physical gripper width can be calculated
                                                                             using the parameters of the camera and the measured depth.
                                                                                Depth Input: As the Cornell Grasping Dataset is captured
                                                                             with a real camera it already contains realistic sensor noise
                                                                             and therefore no noise addition is required. The depth images
                                                                             are inpainted using OpenCV [4] to remove invalid values.
                                                                             We subtract the mean of each depth image, centring its value
                                                                             around 0 to provide depth invariance.
                                                                             C. Network Architecture
                                                                                Our GG-CNN is a fully convolutional topology, shown
                                                                             in Fig. 4a. It is used to directly approximate the grasp
                                                                             map Gθ from an input depth image I. Fully convolutional
                                                                             networks have been shown to perform well at computer vision
Fig. 3.    Generation of training data used to train our GG-CNN. Left:
The cropped and rotated depth and RGB images from the Cornell Grasping       tasks requiring transfer between image domains, such image
Dataset [17], with the ground-truth positive grasp rectangles representing   segmentation [1, 19] and contour detection [34].
antipodal grasps shown in green. The RGB image is for illustration and is       The GG-CNN computes the function Mθ (I)                  =
not used by our system. Right: From the ground-truth grasps, we generate
the Grasp Quality (QT ), Grasp Angle (ΦT ) and Grasp Width (WT ) images      (Qθ , Φθ , Wθ ), where I, Qθ , Φθ and Wθ are represented
to train our network. The angle is further decomposed into cos(2ΦT ) and     as 300×300 pixel images. As described in Section IV-B,
sin(2ΦT ) for training as described in Section IV-B.                         the network outputs two images representing the unit vector
our pixelwise grasp representation as multiple labelled grasps               components of 2Φθ , from which we calculate the grasp
                                                                                                        sin(2Φθ )
are provided per image. This is a more realistic estimate of                 angles by Φθ = 21 arctan cos(2Φ  θ)
                                                                                                                  .
the full pixel-wise grasp map, than using a single image to                     Our final GG-CNN contains 62,420 parameters, mak-
represent one grasp, such as in [21]. We augment the Cornell                 ing it significantly smaller and faster to compute than
Grasping Dataset with random crops, zooms and rotations to                   the CNNs used for grasp candidate classification in other
create a set of 8840 depth images and associated grasp map                   works which contain hundreds of thousands [10, 18] or
images GT , effectively incorporating 51,100 grasp examples.                 millions [12, 21, 23, 25] of parameters. Our code is available
   The Cornell Grasping Dataset represents antipodal grasps                  at https://github.com/dougsm/ggcnn.
as rectangles using pixel coordinates, aligned to the position
                                                                             D. Training
and rotation of a gripper [35]. To convert from the rectangle
representation to our image-based representation G, we use                      We train our network on 80% of our training dataset, and
the centre third of each grasping rectangle as an image mask                 keep 20% as an evaluation dataset. We trained 95 networks
which corresponds to the position of the centre of the gripper.              with similar architectures but different combinations of con-
We use this image mask to update sections of our training                    volutional filters and stride sizes for 100 epochs each.
images, as described below and shown in Fig. 3. We consider                     To determine the best network configuration, we compare
only the positive labelled grasps for training our network and               relative performance between our trained networks by eval-
assume any other area is not a valid grasp.                                  uating each on detecting ground-truth grasps in our 20%
   Grasp Quality: We treat each ground-truth positive grasp                  evaluation dataset containing 1710 augmented images.
from the Cornell Grasping Dataset as a binary label and set                                   V. E XPERIMENTAL S ET- UP
the corresponding area of QT to a value of 1. All other pixels
are 0.                                                                       A. Physical Components
   Angle: We compute the angle of each grasping rectangle                       To perform our grasping trials we use a Kinova Mico 6DOF
in the range [− π2 , π2 ], and set the corresponding area of ΦT .            robot fitted with a Kinova KG-2 2-fingered gripper.
We encode the angle as two vector components on a unit                          Our camera is an Intel RealSense SR300 RGB-D camera.
circle, producing values in the range [−1, 1] and removing                   The camera is mounted to the wrist of the robot, approximately
any discontinuities that would occur in the data where the                   80 mm above the closed fingertips and inclined at 14◦ towards
angle wraps around ± π2 if the raw angle was used, making                    the gripper. This set-up is shown in Fig. 4a.
the distribution easier for the network to learn [9]. Because                   The GG-CNN computations were performed on a PC run-
the antipodal grasp is symmetrical around ± π2 radians, we                   ning running Ubuntu 16.04 with a 3.6 GHz Intel Core i7-7700
use use two components sin(2ΦT ) and cos(2ΦT ) which                         CPU and NVIDIA GeForce GTX 1070 graphics card. On this
provides values which are unique within ΦT ∈ [− π2 , π2 ] and                platform, the GG-CNN takes 6 ms to compute for a single
symmetrical at ± π2 .                                                        depth image, and computation of the entire grasping pipeline
   Width: Similarly, we compute the width in pixels (max-                    (Section V-C) takes 19 ms, with the code predominantly writ-
imum of 150) of each grasping rectangle representing the                     ten in Python.
Fig. 4. (a) The Generative Grasping CNN (GG-CNN) takes an inpainted depth image (I), and directly generates a grasp pose for every pixel (the grasp
map Gθ ), comprising the grasp quality Qθ , grasp width Wθ and grasp angle Φθ . (b) From the combined network output, we can compute the best grasp
point to reach for, gθ∗ .

                                                                                 objects with adversarial geometry, which were used by Mahler
                                                                                 et al. [21] to verify the performance of their Grasp Quality
                                                                                 CNN. The objects all have complex geometry, meaning there
                                                                                 is a high chance of a collision with the object in the case
                                                                                 of an inaccurate grasp, as well as many curved and inclined
                                                                                 surfaces which are difficult or impossible to grasp. The object
                                                                                 models are available online as part of the released datatasets
                                                                                 for Dex-Net 2.01 [21].
                                                                                    Household Set This set of items contains twelve household
                                                                                 items of varying sizes, shapes and difficulty with minimal
Fig. 5. The objects used for grasping experiments. Left: The 8 adversarial       redundancy (i.e. minimal objects with similar shapes). The ob-
objects from [21]. Right: The 12 household objects selected from [5] and [16].   jects were chosen from the standard robotic grasping datasets
                                                                                 the ACRV Picking Benchmark (APB) [16] and the YCB
   1) Limitations: The RealSense camera has a specified min-
                                                                                 Object Set [5], both of which provide item specifications
imum range of 200 mm. In reality, we find that the RealSense
                                                                                 and online purchase links. Half of the item classes (mug,
camera is unable to produce accurate depth measurements
                                                                                 screwdriver, marker pen, die, ball and clamp) appear in both
from a distance closer than 150 mm, as the separation between
                                                                                 data sets. We have made every effort to produce a balanced
the camera’s infra-red projector and camera causes shadowing
                                                                                 object set containing objects which are deformable (bear and
in the depth image caused by the object. For this reason, when
                                                                                 cable), perceptually challenging (black clamp and screwdriver
performing closed-loop grasping trials (Section V-D2), we stop
                                                                                 handle, thin reflective edges on the mug and duct tape, and
updating the target grasp pose at this point, which equates
                                                                                 clear packaging on the toothbrush), and objects which are
to the gripper being approximately 70 mm from the object.
                                                                                 small and require precision (golf ball, duck and die).
Additionally, we find that the RealSense is unable to provide
                                                                                    While both the APB and YCB object sets contain a large
any valid depth data on many black or reflective objects.
                                                                                 number of objects, many are physically impossible for our
   The Kinova KG-2 gripper has a maximum stroke of
                                                                                 robot to grasp due to being too small and thin (e.g. screws,
175 mm, which could easily envelop many of the test items. To
                                                                                 washers, envelope), too large (e.g. large boxes, saucepan,
encourage more precise grasps, we limit the maximum gripper
                                                                                 soccer ball) or too heavy (e.g. power drill, saucepan). While
width to approximately 70 mm. The fingers of the gripper
                                                                                 manipulating these objects is an open problem in robotics, we
have some built-in compliance and naturally splay slightly
                                                                                 do not consider them for our experiments in order to compare
at the tips, so we find that objects with a height less than
                                                                                 our results to other work which use similar object classes to
15 mm (especially those that are cylindrical, like a thin pen)
                                                                                 ours [12, 17, 18, 21, 23].
cannot be grasped.
                                                                                 C. Grasp Detection Pipeline
B. Test Objects
                                                                                    Our grasp detection pipeline comprises three stages: image
   There is no set of test objects which are commonly used                       processing, evaluation of the GG-CNN and computation of a
for robotic grasping experiments, with many people using                         grasp pose.
random “household” objects which are not easily reproducible.                       The depth image is first cropped to a square, and scaled to
We propose here two sets of reproducible benchmark objects                       300 × 300 pixels to suit the input of the GG-CNN. We inpaint
(Fig. 5) on which we test the grasp success rate of our                          invalid depth values using OpenCV [4].
approach.
   Adversarial Set The first set consists of eight 3D-printed                     1 https://berkeleyautomation.github.io/dex-net/
   The GG-CNN is then evaluated on the processed depth              gripper fingers to the computed gripper width via velocity
image, to produce the grasp map Gθ . We filter Qθ with a            control. Control is stopped when the grasp pose is reached
Gaussian kernel, similar to [12], and find this helps improve       or a collision is detected. The gripper is closed and lifted and
our grasping performance by removing outliers and causing           the grasp is recorded as a success if the object is successfully
the local maxima of Gθ to converge to regions of more robust        lifted to the starting position.
grasps.
   Finally, the best grasp pose in the image space g̃θ∗ is          E. Object Placement
computed by identifying the maximum pixel s∗ in Qθ , and               To remove bias related to object pose, objects are shaken
the rotation and width are computed from Φθ |s∗ and Wθ |s∗          in a cardboard box and emptied into the robot’s workspace
respectively. The grasp in Cartesian coordinates gθ∗ is com-        for each grasp attempt. The workspace is an approximately
puted via Eq. (1) (Fig. 4b).                                        250×300 mm area in the robot’s field of view in which the
D. Grasp Execution                                                  robot’s kinematics allow it to execute a vertical grasp.
   We evaluate the performance of our system using two
                                                                                         VI. E XPERIMENTS
grasping methods. Firstly, an open-loop grasping method sim-
ilar to [17, 23, 21], where the best grasp pose is calculated          To evaluate the performance of our grasping pipeline and
from a single viewpoint and executed by the robot open-             GG-CNN, we perform several experiments comprising over
loop. Secondly, we implement a closed-loop visual servoing          2000 grasp attempts. In order to compare our results to others,
controller which we use for evaluating our system in dynamic        we aim to reproduce similar experiments where possible, and
environments.                                                       also aim to present experiments which are reproducible in
   1) Open Loop Grasping: To perform open-loop grasps, the          themselves by using our defined set of objects (Section V-B)
camera is positioned approximately 350 mm above and parallel        and defined dynamic motions.
to the surface of the table. An item is placed in the field of         Firstly, to most closely compare to existing work in robotic
view of the camera. A depth image is captured and the pose of       grasping, we perform grasping on singulated, static objects
the best grasp is computed using the grasp detection pipeline.      from our two object sets. Secondly, to highlight our pri-
The robot moves to a pre-grasp position, with the gripper tips      mary contribution, we evaluate grasping on objects which are
aligned with and approximately 170 mm above the computed            moved during the grasp attempt, to show the ability of our
grasp. From here, the robot moves straight down until the           system to perform dynamic grasping. Thirdly, we show our
grasp pose is met or a collision is detected via force feedback     system’s ability to generalise to dynamic cluttered scenes by
in the robot. The gripper is closed and lifted, and the grasp is    reproducing the experiments from [32] and show improved
recorded as a success if the object is successfully lifted to the   results. Finally, we further show the advantage of our closed-
starting position.                                                  loop grasping method over open-loop grasping by performing
   2) Closed Loop Grasping: To perform closed-loop grasp-           grasps in the presence of simulated kinematic errors of our
ing, we implement a Position Based Visual Servoing (PBVS)           robot’s control.
controller [14]. The camera is initially positioned approxi-           Table II provides a summary of our results in different
mately 400 mm above the surface of the table, and an object         grasping tasks and comparisons to other work where possible.
is placed in the field of view. Depth images are generated at
a rate of 30 Hz and processed by the grasp detection pipeline       A. Static Grasping
to generate grasp poses in real time. There may be multiple            To evaluate the performance of our GG-CNN under static
similarly-ranked good quality grasps in an image, so to avoid       conditions, we performed grasping trials using both the open-
rapidly switching between them, which would confuse the             and closed-loop methods on both sets of test objects, using the
controller, we compute three grasps from the highest local          set-up shown in Fig. 6a. We perform 10 trials on each object.
maxima of Gθ and select the one which is closest (in image          For the adversarial object set, the grasp success rates were
coordinates) to the grasp used on the previous iteration. As        84% (67/80) and 81% (65/80) for the open- and closed-loop
the control loop is fast compared to the movement of the            methods respectively. For the household object set, the open-
robot, there is unlikely to be a major change between frames.       loop method achieved 92% (110/120) and the closed-loop 91%
The system is initialised to track the global maxima of Qθ at       (109/120).
the beginning of each grasp attempt. We represent the poses
                                                                       A comparison to other work is provided in Table II. We
of the grasp Tgθ∗ and the gripper fingers Tf as 6D vectors
                                                                    note that the results may not be directly comparable due to
comprising the Cartesian position and roll, pitch and yaw Euler
                                                                    the different objects and experimental protocol used, however
angles (x, y, z, α, β, γ), and generate a 6D velocity signal for
                                                                    we aim to show that we achieve comparable performance to
the end-effector:
                                                                    other works which use much larger neural networks and have
                                                                    longer computation times. A noteworthy difference in method
                      v = λ(Tgθ∗ − Tf )
                                                                    is [18], which does not require precise camera calibration, but
where λ is a 6D scale for the velocity, which causes the gripper    rather learns the spatial relationship between the robot and the
to converge to the grasp pose. Simultaneously, we control the       objects using vision.
                                                                                   [17]         [23]    [12]    [21]      [18]     [32]    Ours
                       Grasp Success Rate (%)
                       Household Objects (Static)#                                     89        73      80     80        80              92±5
                       Adversarial Objects (Static)                                                             93*                       84±8
                       Household Objects (Dynamic)                                                                                        88±6
                       Adversarial Objects (Dynamic)                                                                                      83±8
                       Objects from [32] (Single)                                                                                   98     100
                       Objects from [32] (Clutter)                                                                                  89    87±7
                       Objects from [32] (Clutter, Dynamic)                                                                         77    81±8
                       Network Parameters (approx.)                                            60M      60M     18M       1M                62k
                       Computation Time (to generate pose or command)             13.5s                         0.8s    0.2-0.5s   0.2s    19ms

   TABLE II: Results from grasping experiments with 95% confidence intervals, and comparison to other deep learning approaches where available.
        # Note that all experiments use different item sets and experimental protocol, so comparative performance is indicative only.
                                 *Contrary to our approach, [21] train their grasp network on the adversarial objects!

                                                                                            Fig. 7. Left: The objects used to reproduce the dynamic grasping in clutter
                                                                                            experiment of [32]. Right: The test objects used by [32]. We have attempted
                                                                                            to recreate the object set as closely as possible.
                                                                                            perform a comparison. Even though our GG-CNN has not been
Fig. 6. Grasping experiments. (a) Set-up for static grasping, and initial set-              trained on cluttered environments, we show here its ability to
up for dynamic grasping. (b) During a dynamic grasp attempt, the object is                  perform grasping in the presence of clutter. We recreate the
translated at least 100 mm and rotated at least 25◦ , measured by the grid on               three grasping experiments from [32] as follows:
the table. (c) Set-up for static grasping in clutter, and initial set-up for dynamic
grasping in clutter. (d) During a dynamic grasp attempt, the cluttered objects                 1) Isolated Objects: We performed 4 grasps on each of
are translated at least 100 mm and rotated at least 25◦ , measured by the grid              the 10 test objects (Fig. 7) in isolation, and achieved a grasp
on the table.                                                                               success rate of 100%, compared to 98% (39/40) in [32].
B. Dynamic Grasping                                                                            2) Cluttered Objects: The 10 test objects are shaken in a
                                                                                            box and emptied in a pile below the robot (Fig. 6c). The robot
   To perform grasps on dynamic objects we take inspiration                                 attempts multiple grasps, and any objects that are grasped are
from recent work in [32], where items are moved once by hand                                removed. This continues until all objects are grasped, three
randomly during each grasp attempt. To assist reproducibility,                              consecutive grasps are failures or all objects are outside the
we define this movement to consist of a translation of at least                             workspace of the robot. We run this experiment 10 times.
100 mm and a rotation of at least 25◦ after the grasp attempt                                  Despite our GG-CNN not being trained on cluttered scenes,
has begun, shown in Fig. 6a-b, which we measure using a grid                                we achieved a grasp success rate of 87% (83/96) compared to
on the table.                                                                               89% (66/74) in [32]. Our most common failure cause was
   We perform 10 grasp attempts on each adversarial and                                     collision of the gripper with two objects that had fallen up
household object using our closed-loop method, and achieve                                  against each other. 8 out of the 13 failed grasps were from
grasp success rates of 83% (66/80) for the adversarial objects                              two runs where objects had fallen into an ungraspable position
and 88% (106/120) for the household objects. These results                                  and failed repeatedly. 8 out of the 10 runs finished with 0 or
are not significantly different to our results on static objects,                           1 grasp failures.
and are within the 95% confidence bounds of our results on                                     3) Dynamic Cluttered Objects: For dynamic scenes, we
static objects, showing our method’s ability to maintain a high                             repeat the procedure as above with the addition of a random
level of accuracy when grasping dynamic objects.                                            movement of the objects during the grasp attempt. Viereck
   We do not compare directly to an open-loop method as the                                 et al. [32] do not give specifications for their random move-
object movement moves the object sufficiently far from the                                  ment, so we use the same procedures as in Section VI-B,
original position that no successful grasps would be possible.                              where we move the objects randomly, at least 100 mm and
                                                                                            25◦ during each grasp attempt (Fig. 6d).
C. Dynamic Grasping in Clutter                                                                 In 10 runs of the experiment, we performed 94 grasp
   Viereck et al. [32] demonstrate a visuomotor controller for                              attempts of which 76 were successful (81%), compared to
robotic grasping in clutter that is able to react to disturbances                           77% (58/75) in [32]. Like the static case, 8 of the 18 failed
to the objects being grasped. As this work is closely related to                            grasps were from two runs where the arrangement of the
our own, we have made an effort to recreate their experiments                               objects resulted in repeated failed attempts. In the other 8 runs,
using objects as close as possible to their set of 10 (Fig. 7) to                           all available objects (i.e. those that didn’t fall/roll out of the
workspace) were successfully grasped with 2 or fewer failed                                                         Adversarial Objects

                                                                     Grasp Success Rate (%)
                                                                                              100
grasps.
                                                                                               80
   Despite not being trained on cluttered scenes, this shows
our approach’s ability to perform grasping in clutter and its                                  60
ability to react to dynamic scenes, showing only a 5% decrease                                        Open-loop
                                                                                               40
in performance for the dynamic case compared to 12% in [32].                                          Closed-loop
   For the same experiments, [32] shows that an open-loop                                      20
                                                                                                    0.00           0.05              0.10             0.15
baseline approach on the same objects that is able to achieve                                               (Simiulated Velocity Cross-correlation)
95% grasp success rate for the static cluttered scenes achieves                                                     Household Objects

                                                                     Grasp Success Rate (%)
                                                                                              100
only 23% grasp success rate for dynamic scenes as it is able
to react to the change in item location.                                                       80

D. Robustness to Control Errors                                                                60

   The control of a robot may not always be precise. For exam-                                 40     Open-loop
ple, when performing grasping trials with a Baxter Research                                           Closed-loop
                                                                                               20
Robot, Lenz et al. [17] found that positioning errors of up to                                      0.00           0.05              0.10             0.15
                                                                                                            (Simiulated Velocity Cross-correlation)
20 mm were typical. A major advantage of using a closed-
loop controller for grasping is the ability to perform accurate     Fig. 8. Comparison of grasp success rates for open-loop and closed-loop
                                                                    control methods with velocity cross-correlation added to simulate kinematic
grasps despite inaccurate control. We show this by simulating       errors (see Section VI-D for full details). The closed-loop method out-
an inaccurate kinematic model of our robot by introducing a         performs the open-loop method in all cases where kinematic errors are present.
cross-correlation between Cartesian (x, y and z) velocities:        10 trials were performed on each object in both the adversarial and household
                                                                    object sets.
                                                   
                       1 + cxx     cxy        cxz                      The addition of control inaccuracy effects objects which
           vc = v ·  cyx        1 + cyy      cyz                  require precise grasps (e.g. the adversarial objects, and small
                         czx       czy      1 + czz                 objects such as the die and ball) the most. Simpler objects
where each c ∼ N (0, σ 2 ) is sampled at the beginning of each      which are more easily caged by the gripper, such as the pen,
grasp attempt. While a real kinematic error (e.g. a link length     still report good grasp results in the presence of kinematic
being incorrectly configured) would result in a more non-linear     error.
response, our noise model provides a good approximation                                    VII. C ONCLUSION
which is independent of the robot’s kinematic model, so has            We present our Generative Grasping Convolutional Neural
a deterministic effect with respect to end-effector positioning     Network (GG-CNN), an object-independent grasp synthesis
and is more easily replicated on a different robotic system.        model which directly generates grasp poses from a depth
   We test grasping on both object sets with 10 grasp attempts      image on a pixelwise basis, instead of sampling and clas-
per object for both the open- and closed-loop methods with          sifying individual grasp candidates like other deep learning
σ = 0.0 (the baseline case), 0.05, 0.1 and 0.15. In the case        techniques. Our GG-CNN is orders of magnitude smaller than
of our open-loop controller, where we only control velocity         other recent grasping networks, allowing us to generate grasp
for 170 mm in the z direction from the pre-grasp pose (Sec-         poses at a rate of up to 50 Hz and perform closed-loop control.
tion V-D1), this corresponds to having a robot with an end-         We show through grasping trials that our system is able to gain
effector precision described by a normal distribution with zero     state-of-the-art results in grasping unknown, dynamic objects,
mean and standard deviation 0.0, 8.5, 17.0 and 25.5 mm re-          including objects in dynamic clutter. Additionally, our closed-
spectively, by the relationship for scalar multiplication of the    loop grasping method significantly outperforms an open-loop
normal distribution:                                                method in the presence of simulated robot control error.
∆x = ∆y = ∆z · N (0, σ 2 ) = N (0, ∆z 2 σ 2 ); ∆z = 170 mm             We encourage reproducibility in robotic grasping exper-
                                                                    iments by using two standard object sets, a set of eight
   The results are illustrated in Fig. 8, and show that the         3D-printed objects with adversarial geometry [21] plus a
closed-loop method outperforms the open-loop method in the          proposed set of twelve household items from standard robotic
presence of control error. This highlights a major advantage        benchmark object sets, and by defining the parameters of our
of being able to perform closed-loop grasping, as the open-         dynamic grasping experiments. On our two object sets we
loop methods are unable to respond, achieving only 38% grasp        achieve 83% and 88% grasp success rate respectively when
success rate in the worst case. In comparison, the closed-loop      objects are moved during the grasp attempt, and 81% for
method achieves 68% and 73% grasp success rate in the worst         objects in dynamic clutter.
case on the adversarial and household objects respectively.
   The decrease in performance of the closed-loop method is                          ACKNOWLEDGMENTS
due to the limitation of our camera (Section V-A1), where we          This research was supported by the Australian Research
are unable to update the grasp pose when the gripper is within      Council Centre of Excellence for Robotic Vision (project
70 mm of the object, so can not correct for errors in this range.   number CE140100016).
                       R EFERENCES                              [15] S. Kumra and C. Kanan. Robotic Grasp Detection using
                                                                     Deep Convolutional Neural Networks. In Proc. of the
 [1] Vijay Badrinarayanan, Alex Kendall, and Roberto                 IEEE/RSJ International Conference on Intelligent Robots
     Cipolla.     SegNet: A Deep Convolutional Encoder-              and Systems (IROS), pages 769–776, 2017.
     Decoder Architecture for Image Segmentation. arXiv         [16] Jürgen Leitner, Adam W Tow, Niko Sünderhauf, Jake E
     preprint arXiv:1511.00561, 2015.                                Dean, Joseph W Durham, Matthew Cooper, Markus
 [2] Antonio Bicchi and Vijay Kumar. Robotic Grasping and            Eich, Christopher Lehnert, Ruben Mangels, Christopher
     Contact: A Review . In Proc. of the IEEE International          McCool, et al. The ACRV Picking Benchmark: A
     Conference on Robotics and Automation (ICRA), pages             Robotic Shelf Picking Benchmark to Foster Reproducible
     348–353, 2000.                                                  Research. In Proc. of the IEEE International Conference
 [3] Jeannette Bohg, Antonio Morales, Tamim Asfour, and              on Robotics and Automation (ICRA), pages 4705–4712,
     Danica Kragic. Data-Driven Grasp Synthesis – A Survey.          2017.
     IEEE Transactions on Robotics, 30(2):289–309, 2014.        [17] Ian Lenz, Honglak Lee, and Ashutosh Saxena. Deep
 [4] G. Bradski. The OpenCV Library. Dr. Dobb’s Journal              learning for detecting robotic grasps. The International
     of Software Tools, 2000.                                        Journal of Robotics Research (IJRR), 34(4-5):705–724,
 [5] Berk Calli, Aaron Walsman, Arjun Singh, Siddhartha              2015.
     Srinivasa, Pieter Abbeel, and Aaron M Dollar. Bench-       [18] Sergey Levine, Peter Pastor, Alex Krizhevsky, and
     marking in Manipulation Research: Using the Yale-               Deirdre Quillen. Learning Hand-Eye Coordination for
     CMU-Berkeley Object and Model Set. IEEE Robotics                Robotic Grasping with Large-Scale Data Collection.
     & Automation Magazine, 22(3):36–52, 2015.                       In International Symposium on Experimental Robotics,
 [6] Renaud Detry, Emre Baseski, Mila Popovic, Younes                pages 173–184, 2016.
     Touati, N Kruger, Oliver Kroemer, Jan Peters, and Justus   [19] Jonathan Long, Evan Shelhamer, and Trevor Darrell.
     Piater. Learning Object-specific Grasp Affordance Den-          Fully Convolutional Networks for Semantic Segmenta-
     sities. In Proc. of the IEEE International Conference on        tion. In Proc. of the IEEE Conference on Computer
     Development and Learning (ICDL), pages 1–7, 2009.               Vision and Pattern Recognition (CVPR), pages 3431–
 [7] Sahar El-Khoury and Anis Sahbani. Handling Objects By           3440, 2015.
     Their Handles. In IEEE/RSJ International Conference on     [20] Jeffrey Mahler, Florian T. Pokorny, Brian Hou, Melrose
     Intelligent Robots and Systems (IROS), 2008.                    Roderick, Michael Laskey, Mathieu Aubry, Kai Kohlhoff,
 [8] Corey Goldfeder, Peter K Allen, Claire Lackner, and             Torsten Kroger, James Kuffner, and Ken Goldberg. Dex-
     Raphael Pelossof. Grasp Planning via Decomposition              Net 1.0: A cloud-based network of 3D objects for robust
     Trees. In Proc. of the IEEE International Conference            grasp planning using a Multi-Armed Bandit model with
     on Robotics and Automation (ICRA), pages 4679–4684,             correlated rewards. In Proc. of the IEEE International
     2007.                                                           Conference on Robotics and Automation (ICRA), pages
 [9] Kota Hara, Raviteja Vemulapalli, and Rama Chellappa.            1957–1964, 2016.
     Designing Deep Convolutional Neural Networks for Con-      [21] Jeffrey Mahler, Jacky Liang, Sherdil Niyaz, Michael
     tinuous Object Orientation Estimation. arXiv preprint           Laskey, Richard Doan, Xinyu Liu, Juan Aparicio Ojea,
     arXiv:1702.01499, 2017.                                         and Ken Goldberg. Dex-Net 2.0: Deep Learning to Plan
[10] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian               Robust Grasps with Synthetic Point Clouds and Analytic
     Sun. Deep Residual Learning for Image Recognition. In           Grasp Metrics. In Robotics: Science and Systems (RSS),
     Proc. of the IEEE Conference on Computer Vision and             2017.
     Pattern Recognition (CVPR), pages 770–778, 2016.           [22] Andrew T Miller, Steffen Knoop, Henrik I Christensen,
[11] Radu Horaud, Fadi Dornaika, and Bernard Espiau. Vi-             and Peter K Allen. Automatic Grasp Planning Using
     sually Guided Object Grasping. IEEE Transactions on             Shape Primitives. In Proc. of the IEEE International
     Robotics and Automation, 14(4):525–532, 1998.                   Conference on Robotics and Automation (ICRA), pages
[12] Edward Johns, Stefan Leutenegger, and Andrew J. Davi-           1824–1829, 2003.
     son. Deep Learning a Grasp Function for Grasping under     [23] Lerrel Pinto and Abhinav Gupta. Supersizing self-
     Gripper Pose Uncertainty. In Proc. of the IEEE/RSJ In-          supervision: Learning to grasp from 50k tries and 700
     ternational Conference on Intelligent Robots and Systems        robot hours. In Proc. of the IEEE International Confer-
     (IROS), pages 4461–4468, 2016.                                  ence on Robotics and Automation (ICRA), pages 3406–
[13] Jens Kober, Matthew Glisson, and Michael Mistry. Play-          3413, 2016.
     ing Catch and Juggling with a Humanoid Robot. In Proc.     [24] Domenico Prattichizzo and Jeffrey C. Trinkle. Grasping.
     of the IEEE-RAS International Conference on Humanoid            In Springer Handbook of Robotics, chapter 28, pages
     Robots (Humanoids), pages 875–881, 2012.                        671–700. Springer Berlin Heidelberg, 2008.
[14] Danica Kragic, Henrik I Christensen, et al. Survey on      [25] Joseph Redmon and Anelia Angelova. Real-Time Grasp
     Visual Servoing for Manipulation. Computational Vision          Detection Using Convolutional Neural Networks. In
     and Active Perception Laboratory, Fiskartorpsv, 2002.           Proc. of the IEEE International Conference on Robotics
     and Automation (ICRA), pages 1316–1322, 2015.
[26] Carlos Rubert, Daniel Kappler, Antonio Morales, Stefan
     Schaal, and Jeannette Bohg. On the Relevance of Grasp
     Metrics for Predicting Grasp Success. In Proc. of the
     IEEE/RSJ International Conference of Intelligent Robots
     and Systems (IROS), pages 265–272, 2017.
[27] Anis Sahbani, Sahar El-Khoury, and Philippe Bidaud.
     An overview of 3D object grasp synthesis algorithms.
     Robotics and Autonomous Systems, 60(3):326–336, 2012.
[28] Ashutosh Saxena, Justin Driemeyer, and Andrew Y. Ng.
     Robotic Grasping of Novel Objects using Vision. The
     International Journal of Robotics Research (IJRR), 27
     (2):157–173, 2008.
[29] Karun B Shimoga. Robot Grasp Synthesis Algorithms: A
     Survey. The International Journal of Robotics Research
     (IJRR), 15(3):230–266, 1996.
[30] N. Vahrenkamp, S. Wieland, P. Azad, D. Gonzalez, T. As-
     four, and R. Dillmann. Visual servoing for humanoid
     grasping and manipulation tasks. In Proc. of the Inter-
     national Conference on Humanoid Robots (Humanoids),
     pages 406–412, 2008.
[31] Jacob Varley, Jonathan Weisz, Jared Weiss, and Peter
     Allen. Generating Multi-Fingered Robotic Grasps via
     Deep Learning. In Proc. of the IEEE/RSJ International
     Conference on Intelligent Robots and Systems (IROS),
     pages 4415–4420. IEEE, 2015.
[32] Ulrich Viereck, Andreas Pas, Kate Saenko, and Robert
     Platt. Learning a visuomotor controller for real world
     robotic grasping using simulated depth images. In Proc.
     of the Conference on Robot Learning (CoRL), pages 291–
     300, 2017.
[33] Z. Wang, Z. Li, B. Wang, and H. Liu. Robot grasp
     detection using multimodal deep convolutional neural
     networks. Advances in Mechanical Engineering, 8(9),
     2016.
[34] Jimei Yang, Brian Price, Scott Cohen, Honglak Lee, and
     Ming-Hsuan Yang. Object Contour Detection with a
     Fully Convolutional Encoder-Decoder Network. In Proc.
     of the IEEE Conference on Computer Vision and Pattern
     Recognition (CVPR), pages 193–202, 2016.
[35] Yun Jiang, Stephen Moseson, and Ashutosh Saxena.
     Efficient Grasping from RGBD Images: Learning using
     a new Rectangle Representation. In Proc. of the IEEE
     International Conference on Robotics and Automation
     (ICRA), pages 3304–3311, 2011.
