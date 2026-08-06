---
source_id: 084
bibtex_key: fang2020graspnet
title: GraspNet-1Billion: A Large-Scale Benchmark for General Object Grasping
year: 2020
domain_theme: Grasp Robotik
verified_pdf: 84_GraspNet-1Billion.pdf
char_count: 63714
---

GraspNet-1Billion: A Large-Scale Benchmark
                                        for General Object Grasping

                                    Hao-Shu Fang, Chenxi Wang, Minghao Gou. Cewu Lu1
                                               Shanghai Jiao Tong University
                                fhaoshu@gmail.com, {wcx1997,gmh2015,lucewu}@sjtu.edu.cn

                              Abstract

   Object grasping is critical for many applications, which
is also a challenging computer vision problem. However,
for cluttered scene, current researches suffer from the prob-
lems of insufficient training data and the lacking of eval-                                                                            Scene-level
                                                                                            Data
                                                                                                                                       Grasp Poses
uation benchmarks. In this work, we contribute a large-
scale grasp pose detection dataset with a unified evaluation
system. Our dataset contains 97,280 RGB-D image with                                                       …
over one billion grasp poses. Meanwhile, our evaluation
                                                                                          Object-level
system directly reports whether a grasping is successful by                               Grasp Poses                         Object 6D Poses
analytic computation, which is able to evaluate any kind
                                                                                  Figure 1. Our methodology for building the dataset. We collect
of grasp poses without exhaustively labeling ground-truth.                        data with real-world sensors and annotate grasp poses for every
In addition, we propose an end-to-end grasp pose predic-                          single object by analytic computation. Object 6D poses are manu-
tion network given point cloud inputs, where we learn ap-                         ally annotated to project the grasp poses from object coordinate to
proaching direction and operation parameters in a decou-                          the scene coordinate. Such methodology greatly reduces the labor
pled manner. A novel grasp affinity field is also designed to                     of annotating grasp poses. Our dataset is both densely annotated
improve the grasping robustness. We conduct extensive ex-                         and visually coherent with real world.
periments to show that our dataset and evaluation system
can align well with real-world experiments and our pro-                           ingly. The difference in evaluation metrics makes it diffi-
posed network achieves the state-of-the-art performance.                          cult to compare these methods directly in a unified man-
Our dataset, source code and models are publicly available                        ner, while evaluating with real robots would dramatically
at www.graspnet.net.                                                              increase the evaluation cost. Secondly, it is difficult to
                                                                                  obtain large-scale high quality training data [5]. Previous
                                                                                  datasets annotated by human [16, 50, 7] are usually small
1. Introduction                                                                   in scale and only provide sparse annotations. While obtain-
                                                                                  ing training data from the simulated environment [26, 9, 48]
   Object grasping is a fundamental problem and has many                          can generate large scale datasets, the visual domain gap be-
applications in industry, agriculture and service trade. The                      tween simulation and reality would inevitably degrade the
key of grasping is to detect the grasp poses given visual in-                     performance of algorithms in real-world application.
puts (image or point cloud) and it has drawn many attentions                          To form a solid foundation for algorithms built upon, it
in computer vision community [11, 30].                                            is important for a benchmark to i) provide data that aligns
   Though important, there are currently two main hin-                            well with the visual perception from real world sensors, ii)
drances to obtaining further performance gains in this area.                      be densely and accurately annotated with large-scale grasp
Firstly, the grasp poses have different representations in-                       pose ground-truth and iii) evaluate grasp poses with differ-
cluding rectangle [36] and 6D pose [41] representation and                        ent representations in a unified manner. This is nontrivial,
are evaluated with different metrics [16, 14, 41] correspond-                     especially when it comes to the data annotation. Given an
    1 Cewu Lu is corresponding author, member of Qing Yuan Research               image or scene, it’s hard for us to manually annotate end-
Institute and MoE Key Lab of Artificial Intelligence, AI Institute, Shanghai      less grasp poses in continuous space. We circumvent this
Jiao Tong University, China                                                       issue by exploring a new direction, that is, collecting data

                                                                               111444
from the real world and annotating them by analytic com-             it to multi-object scenarios. The grasp poses generated by
putation in simulation, which leverages the advantages from          these methods are constrained in 2D plane which limits the
both sides.                                                          degree of freedom of grasp poses. With the rapid devel-
    Specifically, inspired by previous literature [41], we pro-      opment in monocular object 6D pose estimation [17, 45],
pose a two-step pipeline to generate tremendous grasp poses          some researchers [8] predict 6D poses of the objects and
for a scene. Thanks to our automatic annotation process, we          project predefined grasp poses to the scene. Such meth-
built the first large-scale in-the-wild grasp pose dataset that      ods have no limitation of grasping orientation, but require a
can serve as a base for training and evaluating grasp pose           prior knowledge about the object shape. Recently, starting
detection algorithms. Our dataset contains 97,280 RGB-D              from [42] there is a new line of researches [41, 24, 28, 35]
images taken from different viewpoints of over 190 clut-             that propose grasping candidates on partial observed point
tered scenes. For all 88 objects in our dataset, we provide          clouds and output a classification score for each candidate
accurate 3D mesh models. Each scene is densely annotated             using 3D CNN. Such methods require no prior knowledge
with object 6D poses and grasp poses, bringing over one              about the objects. Currently, these methods are evaluated in
billion grasp poses, which is 5 orders of magnitude larger           their own metrics and hard to compare to others.
than previous datasets. Moreover, embedded with an online
evaluation system, our benchmark is able to evaluate cur-            Grasping Dataset Cornell grasping dataset [16] first pro-
rent mainstream grasping detection algorithms in a unified           posed rectangle representation for grasping detection in im-
manner. Experiments also demonstrate that our benchmark              ages. Single object RGB-D images are provided with rect-
can align well with real-world experiments. Fig 1 shows the          angle grasp poses. [7, 50] built datasets with the same
methodology for building our dataset.                                protocol but extend to multi-object scenarios. These grasp
    Given such a large scale dataset, we further propose a           poses are annotated by human. [30, 22] collect annotations
novel method for learning grasp poses. For better geomet-            with real robot experiments. These data labeling methods
ric reasoning and context encoding, we propose an end-to-            are time consuming and require strong hardware support.
end 3D based grasp pose detection network. Instead of                To avoid such problem, some recent works explore using
predicting grasp pose matrix directly, our network seeks             simulated environment [26, 9, 48, 28, 4] to anotate grasp
a more robust learning way that learns approaching direc-            poses. They can generate a much larger scale dataset but
tion and operation parameters (e.g. in-plane rotation, grasp         the domain gap of visual perception is always a hindrance.
width) explicitly under a unified objective. Moreover, to            Beyond rectangle based annotation, GraspSeg [2] provides
improve the perturbation resistance of the grasp pose, we            pixel-wise annotations for grasp-affordance segmentation
propose a novel representation called grasp affinity fields          and object segmentation. For 6D pose estimation, [45]
to make our network being robust to perturbation. Exper-             contributes a dataset with 21 objects and 92 scenes. These
iments demonstrate the effectiveness and efficiency of our           datasets mainly focus on a subarea of grasp pose detection.
proposed method.                                                     In this work, we aim to build a dataset that is much larger in
                                                                     scale and diversity and covers main aspects of object grasp-
2. Related Work                                                      ing detection.
   In this section, we first review deep learning based grasp-
ing detection algorithms, followed by related datasets in            Point Cloud Based Deep Learning Qi et al. first pro-
this area. Point cloud based deep learning methods are also          posed PointNet [33] to directly learn features from raw
briefly reviewed.                                                    point cloud inputs. After that, many methods [34, 38, 3,
                                                                     23, 12, 43, 39, 40, 20, 19, 49, 47, 44, 46, 15] are pro-
Deep Learning Based Grasping Prediction Algorithms                   posed to perform point cloud classification and segmenta-
For deep learning based grasping detection algorithms, they          tion. Beyond that, some recent works [31, 37, 32] extended
can be divided into three main categories. The most popu-            the PointNet framework to the area of 3D object detection.
lar one is to detect a graspable rectangle based on RGB-D            The most similar network structure to ours is that of Qin et
image input [16, 21, 36, 13, 30, 22, 26, 50, 1, 2, 7, 27, 28].       al. [35], which also predicted grasp poses based on Point-
Lenz et al. [21] proposed a cascaded method with two net-            Net. In this work, we design an end-to-end network with a
works that first prunes out unlikely grasps and then eval-           new representation of grasp pose rather than direct regres-
uates the remaining grasps with a larger network. Red-               sion.
mon et al. [36] proposed a different network structure that
directly regresses the grasp poses in a single step manner,          3. GraspNet-1Billion
which is faster and more accurate. Mahler et al. [26] pro-
posed a grasp quality CNN to predict the robustness scores             We next describe the main features of our dataset and
of grasping candidates. Zhang [50] and Chu [7] extended              how we build it.

                                                                  11445
                                                                6D-Pose               6DoF Grasp Poses
                                    ……

            View 1
                      Object Models
                                     View 2       RGB
                                                                                                                                Grasp? ×

                      Multi-View                Depth

                                                                                                                               Grasp? √
                                                                                       Rectangle-based
                     Kinect4A   RealSense                    Instance Masks
                      Multi-Cam                                                          Grasp Poses
                                              Point Clouds

                         Rich Data                                   Dense Annotations               Unified Evaluation System
Figure 2. The key components of our dataset. RGB-D images are taken using both RealSense camera and Kinect camera from different
views. The 6D pose of each object, the grasp poses, the rectangle grasp poses and the instance masks are annotated. A unified evaluation
system is also provided.
3.1. Overview
   Previous grasping dataset either focuses on isolated ob-                     Grasp Point         Grasp Generation        Grasp Projection
                                                                                 Sampling                & Annotation      Collision Detection
ject [16, 26, 9, 48] or only labels one grasp per scene [30,
22]. Few datasets consider multi-object-multi-grasp setting
and are small in scale [50, 7] due to the labor of annota-
tion. Moreover, most of the datasets adopt the rectangle
                                                                                               Grasp                    In-plane                  Gripper
based representation [16] of grasp pose, which constrains                                       View                    Rotation                  Depth
                                                                                                                        Sampling                 Sampling
the space for placing the gripper. To overcome these is-                                      Sampling

sues, we propose a large-scale dataset in cluttered scenario
with dense and rich annotations for grasp pose prediction                 Figure 3. Grasp pose annotation pipeline. The grasp point is firstly
named GraspNet-1Billion. Our dataset contains 88 daily                    sampled from point cloud. Then the grasp view, the in-plane ro-
objects with high quality 3D mesh models. The images are                  tation and the gripper depth are sampled and evaluated. Finally,
collected from 190 cluttered scenes, each contributes 512                 the grasps are projected on the scene using the 6D pose of each
RGB-D images captured by two different cameras, bring-                    object. Collision detection is also conducted to avoid the collision
ing 97,280 images in total. For each image, we densely an-                between grasps and background or other object.
notate 6-DoF grasp poses by analytic computation of force
closure [29]. The grasp poses for each scene varies from                  different quality of depth image will inevitably affect the
3,000,000 to 9,000,000, and in total our dataset contains                 algorithms, we adopt two popular RGB-D cameras, Intel
over 1.1 billion grasp poses. Besides, we also provide ac-                RealSense 435 and Kinect 4 Azure, to simultaneously cap-
curate object 6D pose annotations, rectangle based grasp                  ture the scene and provide rich data. For each scene, we
poses, object masks and bounding boxes. Each frame is also                randomly pick around 10 objects from our whole object set
associated with a camera pose, thus multi-view point cloud                and place them in a cluttered manner. The robot arm then
can be easily fused. Fig 2 illustrates the key components of              moves along a fixed trajectory that covers 256 distinct view-
our dataset.                                                              points on a quarter sphere. A synchronized image pair from
                                                                          both RGB-D cameras as well as their camera poses will be
3.2. Data Collection                                                      saved. Note that for camera calibration, we conducted cam-
                                                                          era extrinsic parameter calibration to avoid the errors from
   We select 32 objects that are suitable for grasping from
                                                                          forward kinematics. To be specific, we took photos of a
the YCB dataset [6], 13 adversarial objects from DexNet
                                                                          fixed ArUco marker at the 256 data collection points. The
2.0 [26] and collects 43 objects of our own to construct our
                                                                          camera poses w.r.t the marker coordinate system were ob-
object set. The objects have suitable sizes for grasping and
                                                                          tained. These camera poses are pretty accurate and work
are diverse in shape, texture, size, material, etc. We believe
                                                                          well for our dataset. The detail setting of our data collec-
that diverse local geometry can bring better generalization
                                                                          tion process will be provided in supplementary materials.
ability for the algorithm. To collect data of cluttered scene,
we attach the cameras to a robot arm since it can repeat                  3.3. Data Annotation
the trajectory precisely and help automatizing the collect-
ing process. Camera calibration is conducted before data                  6D Pose Annotation With 97,280 images in total, it
collection to obtain accurate camera poses. Considering                   would be labor consuming to annotate 6D poses for each

                                                                   11446
                                Grasps     Objects     Grasp      6D        Total      Total       Total                  Data
               Dataset                                                                                      Modality
                                / scene    / scene     label     pose      objects    grasps      images                 source
       Cornell [16]                ∼8          1       Rect.      No         240       8019        1035      RGB-D       1 Cam.
       Pinto et al. [30]           1          -        Rect.      No         150       50K         50K       RGB-D       1 Cam.
       Levine et al. [22]          1          -        Rect.      No          -        800K       800K       RGB-D       1 Cam.
       Mahler et al. [26]          1          1        Rect.      No        1,500      6.7M       6.7M        Depth       Sim.
       Jacquard [9]              ∼20          1        Rect.      No         11K       1.1M        54K       RGB-D        Sim.
       Zhang et al. [50]         ∼20         ∼3        Rect.      No          -        100K        4683       RGB        1 Cam.
       Multi-Object [7]          ∼30         ∼4        Rect.      No          -        2904         96       RGB-D       1 Cam.
       VR-Grasping-101 [48]      100          1        6-DOF      Yes        101       4.8M        10K       RGB-D        Sim.
       YCB-Video [45]            None        ∼5        None       Yes        21        None       134K       RGB-D       1 Cam.
       GraspNet (ours)          3∼9M        ∼10       6-DOF       Yes        88       ∼1.2B        97K       RGB-D      2 Cams.
Table 1. Summary of the properties of publicly available grasp datasets. “Rect.”, “Cam.” and “Sim.” are short for Rectangle, Camera and
Simulation respectively. “-” denotes the number is unknown.

frame. Thanks to the camera poses recorded, we only need                is not antipodal. The grasp with lower friction coefficient µ
to annotate 6D poses for the first frame of each scene. The             has more probability of success. Thus we define our score
6D poses will then be propagated to the remaining frames                s as:
by:                                                                                               s = 1.1 − µ,                    (2)
                 Pji = cam−1 i cam0 P0 ,
                                        j
                                                         (1)            such that s lies in (0, 1].
where Pji is the 6D pose of object j at frame i and cami                    Second, for each scene, we project these grasps to the
is the camera pose of frame i. All the 6D pose annotations              corresponding objects based on the annotated 6D object
were carefully refined and double-checked by several anno-              poses:
tators to ensure high quality. Object masks and bounding                                       Pi = cam0 Pi0 ,
boxes are also obtained by projecting objects onto the im-                                                                          (3)
                                                                                               Gi(w) = Pi · Gi(o) ,
ages using 6D poses.
                                                                        where Pi is the 6D pose of the i-th object in the world
Grasp Pose Annotation Different from labels in com-
                                                                        frame, Gi(o) is a set of grasp poses in the object frame
mon vision tasks, grasp poses distribute in a large and con-
tinuous search space, which brings infinite annotations. An-            and Gi(w) contains the corresponding poses in the world
notating each scene manually would be dramatically labor                frame. Besides, collision check is performed to avoid in-
expensive. Considering all the objects are known, we pro-               valid grasps. Following [41], we adopt the simplified grip-
pose a two stage automated pipeline for grasp pose annota-              per model as shown in Fig. 4 and check whether there are
tion, which is illustrated in Fig. 3.                                   object points in this area. After these two steps we can gen-
    First, grasp poses are sampled and annotated for each               erate densely distributed grasp set G(w) for each scene. Ac-
single object. To achieve that, high quality mesh models                cording to statistics, the ratio of positive and negative labels
are downsampled such that the sampled points (called grasp              in our dataset is around 1:2. We conduct real world ex-
points) are uniformly distributed in voxel space. For each              periment in Sec. 5 using our robot arm and verify that our
grasp point, we sample V views uniformly distributed in a               generated grasp poses can align well with real world grasp-
spherical space. Grasp candidates are searched in a two di-             ing.
mensional grid D × A, where D is the set of gripper depths              3.4. Evaluation
and A is the set of in-plane rotation angles. Gripper width
is determined accordingly such that no empty grasp or col-              Dataset Split For our 190 scenes, we use 100 for training
lision occurs. Each grasp candidate will be assigned a con-             and 90 for testing. Specifically, we further divide our test
fidence score based on the mesh model.                                  sets into 3 categories: 30 scenes with seen objects, 30 with
    We adopt an analytic computation method to grade each               unseen but similar objects and 30 for novel objects. We
grasp. The force-closure metric [29, 41] has been proved                hope that such setting can better evaluate the generalization
effective in grasp evaluation: given a grasp pose, the associ-          ability of different methods.
ated object and a friction coefficient µ, force-closure metric          New Metrics To evaluate the prediction performance of
outputs a binary label indicating whether the grasp is antipo-          grasp pose, previous methods adopt the rectangle metric
dal under that coefficient. The result is computed based on             that consider a grasp as correct if: i) the rotation error is
physical rules, which is robust. Here we adopt an improved              less than 30◦ and ii) the rectangle IOU is larger than 0.25.
metric described in [24]. With ∆µ = 0.1 as interval, we de-                There are several drawbacks of such metric. Firstly, it
crease µ gradually from 1 to 0.1 step by step until the grasp           can only evaluate rectangle representation of grasp pose.

                                                                  11447
Secondly, the error tolerance is set rather high since the
groundtruth annotations are not exhaustive. It might over-
estimate the performance of grasping algorithm. Currently,                                                                    R

the Cornell dataset [16] has achieved over 99% accuracy. In
this work, we adopt an online evaluation algorithm to eval-
uate the grasp accuracy.                                                      O
                                                                                        Y
   We first illustrate how we classify whether a single grasp                      Z
pose is true positive. For each predicted grasp pose P̂i ,
                                                                                  (a)                          (b)
we associate it with the target object by checking the point
cloud inside the gripper. Then, similar to the process of gen-      Figure 4. (a) The coordinate frame of the gripper. (b) Our new
erating grasp annotation, we can get a binary label for each        representation of grasp pose. “obj.” denotes object point. Our
                                                                    network needs to predict i) the approaching vector V , ii) the ap-
grasp pose by force-closure metric, given different µ.
                                                                    proaching distance from grasp point to the origin of gripper frame
   For cluttered scene, grasp pose prediction algorithms are        D, iii) the in-plane rotation around approaching axis R and iv) the
expected to predict multiple grasps. Since for grasping,            gripper width W .
we usually conduct execution after the prediction, the per-
centage of true positive is more important. Thus, we adopt          tation [16] or simulation [9], cannot cover all feasible so-
Precision@k as our evaluation metric, which measures the            lution. In contrast, we do not pre-compute labels for the
precision of top-k ranked grasps. APµ denotes the aver-             test set, but directly evaluate them by calculating the qual-
age Precision@k for k ranges from 1 to 50 given friction            ity score using force closure metric [29]. Such evaluation
µ. Similar to COCO [25], we report APµ at different µ.              method does not assume the representation of the grasp
Specifically, we denote AP for the average of APµ ranging           pose, thus is general in practice. Related APIs is made pub-
from µ = 0.2 to µ = 1.0, with ∆µ = 0.2 as interval.                 licly available to facilitate the research in this area.
   To avoid dominated by similar grasp poses or grasp
                                                                    4. Method
poses from single object, we run a pose-NMS before evalu-
ation. For the details of pose-NMS please refer to the sup-            We then introduce our end-to-end grasp pose detection
plementary file.                                                    network, which is illustrated in Fig. 5. Our grasp pose rep-
                                                                    resentation is introduced in 4.1. Accordingly, we mainly
3.5. Discussion                                                     divide our pipeline into three parts: Approach Network, Op-
   In this work, we aim to provide a general benchmark              eration Network and Tolerance Network.
for the problem of object grasping. The grasping problem            4.1. Grasp Pose Representation
can be decoupled as: i) predict all possible grasp poses
(by CV community) and ii) conduct motion planning for                  Similar to previous works [41, 24], we define the frame
specific robotic setting and grasp (by robotics community).         of the two-finger parallel gripper as Fig. 4(a). With the
For our benchmark, we focus on the vision problem and               known gripper frame, grasp pose detection aims to predict
decouple the labels from the design choices of the robotic          the orientation and translation of the gripper under the cam-
environment as much as possible. We provided multiple               era frame, as well as the width of the gripper. We represent
cameras and multiple views, simplified the gripper model            the grasp pose G as
and the collision detection to improve the generality of the
                                                                                             G = [R t w],                          (4)
dataset. The motion planning and collisions with real grip-
per and robot arm are not considered as they are related to         where R ∈ R3×3 denotes the gripper orientation, t ∈ R3×1
the robotic environment and should be solved at run-time.           denotes the center of grasp and w ∈ R denotes the gripper
We hope our dataset can facilitate fair comparison among            width that is suitable for grasping the target object. For neu-
different grasp pose detection algorithms.                          ral network, directly learning the rotation matrix in R3×3 is
   We compare our datasets with other publicly available            not intuitive. The explicit constraints, such as the determi-
grasp datasets. Table 1 summaries the main differences at           nant of rotation matrix must equal one and the inverse of
several aspects. We can see that our dataset is much larger in      it is its transpose, are difficult to learn. Instead, we adopt
scale and diversity. With our two-step annotation pipeline,         the representation from 6D pose estimation [17] that decou-
we are able to collect real images with dense annotations,          ples the orientation as viewpoint classification and in-plane
which leverages the advantages from both sides.                     rotation prediction. Our problem is then reformulated as
   For grasp pose evaluation, due to the continuity in grasp-       follows without loss of generality: for a grasp point on the
ing space, there are in fact infinite feasible grasp poses.         surface of objects, we predict the feasible approaching vec-
The previous method that pre-computed ground truth for              tors, approaching distance, in-plane rotation along the ap-
evaluating grasping, no matter collected by human anno-             proaching axis and a tight gripper width. Fig. 4(b) explains

                                                                 11448
Figure 5. Overview of our end-to-end network. (a) For a scene point cloud with N point coordinates as input, a point encoder-decoder
extracts cloud features and samples M points with C-dim features. (b) Approaching vectors are predicted by ApproachNet and are used to
(c) grouped points in cylinder regions. (d) OperationNet predicts the operation parameters and ToleranceNet predicts the grasp robustness.
See text for more details.
our formulation of grasp pose. Following such formulation,              graspable point as vij . We then look for its ground-truth
our network design is illustrated as follows.                           reference vector v̂ij on the sphere space of the ith point.
                                                                        Similarly, we only consider reference vectors that are within
4.2. Approach Network and Grasp Point Selection                         5 degree bound. With such definition, our target function for
   The approaching vectors and feasible grasp points are                an input point cloud is defined as follows:
jointly estimated by our Approach Network, since some di-
                                                                                                               1 X
rections are not suitable for grasping due to occlusion.                               LA ({ci }, {sij }) =          Lcls (ci , c∗i )
                                                                                                              Ncls i
Base Network To build a solid foundation for viewpoint                                                                                  (5)
classification, we first use a base network for capturing well                   1 XX ∗              ∗
                                                                          +λ1            c 1(|vij , vij | < 5◦ )Lreg (sij , s∗ij ).
point cloud geometric features. In this work, we adopt                          Nreg i j i
PointNet++ [34] backbone network. Other networks like
                                                                        Here, ci denotes the binary prediction of graspable or not
VoxelNet [51] can be also adopted. Taking a raw point
                                                                        for point i. c∗i is assigned 1 if point i is positive and 0
cloud with size N × 3 as input, our base network outputs
                                                                        if negative. sij denotes the predicted confidence score for
a new set of points with C channels features. We subsam-
                                                                        viewpoint j of point i. s∗ij is the corresponding ground-
ple M points with farthest point sampling [10] to cover the
                                                                        truth, which is obtained by choosing the maximum grasp
whole scene.
                                                                        confidence (Eqn. 2) from that viewpoint. |vij , vij
                                                                                                                         ∗
                                                                                                                            | denotes
Output Head We classify feasible approaching vectors                    degree difference. Indicator function 1() constrains the loss
into V predefined viewpoints. Meanwhile, for each point,                on approaching vectors that has a nearby groundtruth within
the Approach Network outputs two values to predict its con-             5 degree bound. Here for Lcls we use a two class softmax
fidence of graspable or not. Therefore, the output of our               loss, while for Lreg we use the smooth L1 loss.
proposal generation network is M × (2 + V ), where 2 de-
notes the binary class of graspable or not and V denotes the            4.3. Operation Network
number of predefined approaching vectors.
                                                                           After getting approaching vectors from graspable points,
Loss Function For each candidate point, we assign it a                  we further predict in-plane rotation, approaching distance,
binary label indicating whether it is graspable or not. First,          gripper width and grasp confidence, which is important for
points which are not on the objects are assigned negative               operation. Here, grasp confidence have 10 levels (Eqn. 2).
labels. Next, for points on the objects, we found those who
have at least one graspable ground-truth within 5mm ra-                 Cylinder Region Transformation Before forwarding
dius neighbor area. Their graspable scores are assigned as              through the operation network, we build a unified represen-
1. Finally, points on the objects but cannot find reference             tation for each grasp candidate. Since approaching distance
ground-truth grasps are ignored, which do not contribute to             is relatively less sensitive, we divide it into K bins. For each
the training objective.                                                 given distance dk , we sample points inside the cylinder cen-
   For each graspable point, V virtual approaching vectors              tered along the approaching vectors to a fixed number. For
are sampled around it under the camera frame. Now, we                   better learning, all the sampled points are transformed into
can define the approaching vector of j th virtual view of ith           a new coordinate whose origin is the grasp point and z-axis

                                                                    11449
is vij . The transformation matrix Oij is calculated as:                       Object      s=1   s=0.5   s=0.1     Object      s=1   s=0.5   s=0.1
                                                                              Banana       98%   67%     21%       Apple       97%   65%     16%
                 Oij = [o1ij , [0, −vij (3) , vij (2) ]T , vij ],                 Peeler   95%   59%     9%        Dragon      96%   60%     9%
                                                                                  Mug      96%   62%     12%       Camel       93%   67%     23%
         where   o1ij = [0, −vij (3) , vij (2) ]T × vij ,
                                                                              Scissors     89%   61%     5%      Power Drill   96%   61%     14%
   (k)                                                                            Lion     98%   68%     16%     Black Mouse   98%   64%     13%
vij is the k-th element of vij . After such transformation,
                                                                             Table 2. Summary of real world success rate of grasping given
candidate grasp poses has a unified representation and co-
                                                                             different grasp score.
ordinate.
Rotation and Width It has been proved in previous lit-                       4.5. Training and Inference
erature [17] that for predicting in-plane rotation, classifica-                 During training, the whole network is updated in an end-
tion could achieve better results than regression. Following                 to-end manner by minimizing the follow objective function:
such setting, our rotation network takes the aligned point
cloud as input and predicts classification scores and normal-                 L = LA ({ci }, {sij }) + αLR (Rij , Sij , Wij ) + βLF (Tij )
ized residuals for each binned rotation, as well as the corre-                                                                         (8)
sponding grasp width and confidence. It is worth noticing                    During inference, we refine our grasp poses by dividing
that since gripper is symmetric, we only predict rotations                   them into 10 bins according to their grasp scores and resort
ranging from 0 to 180 degree. The objective function for                     the grasps in each bin according to the perturbation they
the network is:                                                              can resist predicted by our tolerance network. We divide
                         K                                                  the predicted grasps into 10 bins because our labels have 10
    R
                         X    1 X d           ∗                              different grasp scores. Experiments demonstrate that such
  L (Rij , Sij , Wij ) =            L (Rij , Rij )
                             Ncls ij cls                                     refinement can improve the grasping quality effectively.
                             d=1
                                 1 X d                 ∗
                              +λ2       L (Sij , Sij     )          (6)      5. Experiments
                                Nreg ij reg
                              1 X d                                            In this section, we first conduct robotic experiments to
                         +λ3         Lreg (Wij , Wij∗ ) ,                    demonstrate that our ground-truth annotations can align
                             Nreg ij
                                                                             well with real-world grasping. Then we benchmark several
                                                                             representative methods on our dataset and compare them
where Rij denotes the binned rotation degrees, Sij , Wij and
                                                                             with our methods in a unified evaluation metric (Sec. 3.4).
d denote the grasp confidence scores, gripper widths and
                                                                             Finally, we conduct ablation studies to show the effective-
approaching distance respectively. Ld means loss for the
                                                                             ness of our network components.
dth binned distance. Here, for Lcls we use sigmoid cross
entropy loss function for multi-class binary classification.                 5.1. Ground-Truth Evaluation
4.4. Tolerance Network                                                          To evaluate the quality of our generated grasp poses, we
    After previous steps, our end-to-end network can already                 set up a real robotic experiment. Since we need to project
predict accurate grasp poses. Beyond that, we further pro-                   grasp poses to the camera frame using objects’ 6D poses,
pose a representation called grasp affinity fields(GAFs) to                  we paste ArUco code on the objects and only label their 6D
improve the robustness of our grasp poses prediction. Since                  poses once to avoid tedious annotation process.
feasible grasp poses are infinite, humans tend to pick grasp                    We pick 10 objects from our object set and execute grasp
poses that can tolerate larger errors. Inspired by this, our                 poses that has different scores. For each setting we ran-
GAFs learns to predict the tolerance to perturbation for each                domly choose 100 grasp poses. For robot arm we adopt a
grasp.                                                                       Flexiv Rizon arm and for camera we use the Intel RealSense
    Given a ground truth grasp pose, we search its neighbors                 435. Table 2 summarizes the success rate of grasping. We
in the sphere space to see the farthest distance that the grasp              can see that for grasp poses with high score, the success rate
is still robust with grasp score s > 0.5 and set it as the target            can achieve 0.96 in average. Meanwhile, the success rate is
for our GAFs. The loss function is written as:                               pretty low for grasp poses with s = 0.1. It indicates that
                                                                             our generated grasp poses are well aligned with real world
                                   K
                          1 XX d                                             grasping.
         LF (Aij ) =             Lreg (Tij , Tij∗ ),                (7)
                         Nreg ij d=1                                         5.2. Benchmarking Representative Methods
where Tij denotes the maximum perturbation that the grasp                       We benchmark different representative methods on our
pose can resist.                                                             dataset and compare them with our method.

                                                                          11450
Figure 6. Qualitative results of our predicted grasp poses. Scenes are constructed using the RGB-D images taken by cameras. Grasps are
represented by blue lines.
                                     Seen                                     Unseen                                    Novel
    Methods
                        AP           AP0.8         AP0.4          AP           AP0.8         AP0.4           AP          AP0.8         AP0.4
  GG-CNN[27]         15.48/16.89   21.84/22.47   10.25/11.23   13.26/15.05   18.37/19.76    4.62/6.19     5.52/7.38      5.93/8.78    1.86/1.32
  Chu et al. [7]     15.97/17.59   23.66/24.67   10.80/12.74   15.41/17.36   20.21/21.64     7.06/8.86     7.64/8.04     8.69/9.34    2.52/1.76
    GPD [41]         22.87/24.38   28.53/30.16   12.84/13.46   21.33/23.18   27.83/28.64    9.64/11.32     8.24/9.58    8.89/10.14    2.67/3.16
 Liang et al. [24]   25.96/27.59   33.01/34.21   15.37/17.83   22.68/24.38   29.15/30.84   10.76/12.83    9.23/10.66    9.89/11.24    2.74/3.21
      Ours           27.56/29.88   33.43/36.19   16.95/19.31   26.11/27.84   34.18/33.19   14.23/16.62   10.55/11.51   11.25/12.92    3.98/3.56

        Table 3. Evaluation for different methods. The table shows the results on data captured by RealSense/Kinect respectively.

    For rectangle based method, we adopt two methods [27,                                Method              AP     AP0.8 AP0.4
7] with open implementations. For point cloud proposal                                    Full              29.88 36.19 19.31
method, we adopt [41, 24]. We train these models according                        Replace classification
                                                                                                            23.74 33.28 12.15
to their original implementations.                                                  with regression
                                                                                         Remove
    For our method, rotation angle is divided into 12 bins                                                  28.53 35.62 16.33
                                                                                   Tolerance Network
and approaching distance is divided into 4 bins with the                 Table 4. Ablation studies of our network. See text for more details.
value of 0.01, 0.02, 0.03, 0.04 meter. We set M = 1024
and V = 300. PointNet++ has four set abstraction layers
with the radius of 0.04, 0.1, 0.2, 0.3 in meters and group-              grasp pose representations would affect the results by di-
ing size of 64, 32, 16 and 16, by which the point set is                 rectly regressing the direction of the approaching vector and
down-sampled to the size of 2048, 1024, 512 and 256 re-                  degree of in-plane rotation. Then we evaluate the effective-
spectively. Then the points are up-sampled by two feature                ness of our ToleranceNet by removing it from our inference
propagation layers to the size 1024 with 256-dim features.               pipeline. Results are reported in Tab. 4. We can see that
ApproachNet, OperationNet and ToleranceNet is composed                   classification based learning scheme is indeed better than
of MLPs with the size of (256, 302, 302), (128, 128, 36)                 direct regression. Meanwhile, the drop of performance af-
and (128, 64, 12) respectively. For the loss function, we set            ter removing the ToleranceNet demonstrates effectiveness
λ1 , λ2 , λ3 , α, β = 0.5, 1.0, 0.2, 0.5, 0.1.                           of the grasp affinity fields.
    Our model is implemented with PyTorch and trained
with Adam optimizer [18] on one Nvidia RTX 2080 GPU.
                                                                         6. Conclusion
During training, we randomly sample 20k points from each                    In this paper we built a large-scale dataset for cluttered
scene. The initial learning rate is 0.001 and the batch size is          scene object grasping. Our dataset is orders of magnitude
4. The learning rate is decreased to 0.0001 after 60 epochs              larger than previous grasping datasets and diverse in ob-
and then decreased to 0.00001 after 100 epochs.                          jects, scenes and data sources. It consists of images taken
    We report the results of different methods in Tab. 3. As             by real world sensor and has rich and dense annotations.
we can see, rectangle based method has a lower accuracy                  We demonstrated that our dataset align well with real world
among all of the metrics. It denotes that previous rectangle             grasping. Meanwhile, we proposed an end-to-end grasp
based methods might be over-estimated. Our end-to-end                    pose prediction network equipped with a novel representa-
network achieves the state-of-the-art result and outperforms             tion of grasp affinity fields. Experiments showed the superi-
previous methods by a large margin. We show some quali-                  ority of our method. Our code and dataset will be released.
tative results of our predicted grasp poses in Fig. 6.

5.3. Ablation Studies
                                                                         Acknowledgment This work is supported in part by the Na-
   To evaluate the effectiveness of different components of              tional Key R&D Program of China, No. 2017YFA0700800,
our network, we conduct ablation studies on the seen test                National Natural Science Foundation of China under Grants
set of Kinect subset. First we evaluate whether different                61772332 and Shanghai Qi Zhi Institute

                                                                     11451
References                                                               [15] Mingyang Jiang, Yiran Wu, Tianqi Zhao, Zelin Zhao, and
                                                                              Cewu Lu. Pointsift: A sift-like network module for
 [1] Umar Asif, Jianbin Tang, and Stefan Harrer. Ensemblenet:                 3d point cloud semantic segmentation. arXiv preprint
     Improving grasp detection using an ensemble of convolu-                  arXiv:1807.00652, 2018.
     tional neural networks. In BMVC, page 10, 2018.                     [16] Yun Jiang, Stephen Moseson, and Ashutosh Saxena. Effi-
 [2] Umar Asif, Jianbin Tang, and Stefan Harrer. Graspnet: An                 cient grasping from rgbd images: Learning using a new rect-
     efficient convolutional neural network for real-time grasp de-           angle representation. In 2011 IEEE International Conference
     tection for low-powered devices. In IJCAI, pages 4875–                   on Robotics and Automation, pages 3304–3311. IEEE, 2011.
     4882, 2018.                                                         [17] Wadim Kehl, Fabian Manhardt, Federico Tombari, Slobodan
 [3] Matan Atzmon, Haggai Maron, and Yaron Lipman. Point                      Ilic, and Nassir Navab. Ssd-6d: Making rgb-based 3d de-
     convolutional neural networks by extension operators. arXiv              tection and 6d pose estimation great again. In Proceedings
     preprint arXiv:1803.10091, 2018.                                         of the IEEE International Conference on Computer Vision,
 [4] Samarth Brahmbhatt, Ankur Handa, James Hays, and Dieter                  pages 1521–1529, 2017.
     Fox. Contactgrasp: Functional multi-finger grasp synthesis          [18] Diederik Kingma and Jimmy Ba. Adam: A method for
     from contact. arXiv preprint arXiv:1904.03754, 2019.                     stochastic optimization. arXiv preprint arXiv:1412.6980.
 [5] Shehan Caldera, Alexander Rassau, and Douglas Chai. Re-             [19] Roman Klokov and Victor Lempitsky. Escape from cells:
     view of deep learning methods in robotic grasp detection.                Deep kd-networks for the recognition of 3d point cloud mod-
     Multimodal Technologies and Interaction, 2(3):57, 2018.                  els. In Proceedings of the IEEE International Conference on
 [6] Berk Calli, Arjun Singh, James Bruce, Aaron Walsman, Kurt                Computer Vision, pages 863–872, 2017.
     Konolige, Siddhartha Srinivasa, Pieter Abbeel, and Aaron M          [20] Truc Le and Ye Duan. Pointgrid: A deep network for 3d
     Dollar. Yale-cmu-berkeley dataset for robotic manipulation               shape understanding. In Proceedings of the IEEE conference
     research. The International Journal of Robotics Research,                on computer vision and pattern recognition, pages 9204–
     36(3):261–268, 2017.                                                     9214, 2018.
 [7] Fu-Jen Chu, Ruinian Xu, and Patricio A Vela. Real-world             [21] Ian Lenz, Honglak Lee, and Ashutosh Saxena. Deep learning
     multiobject, multigrasp detection. IEEE Robotics and Au-                 for detecting robotic grasps. The International Journal of
     tomation Letters, 3(4):3355–3362, 2018.                                  Robotics Research, 34(4-5):705–724, 2015.
 [8] Xinke Deng, Yu Xiang, Arsalan Mousavian, Clemens Epp-               [22] Sergey Levine, Peter Pastor, Alex Krizhevsky, Julian Ibarz,
     ner, Timothy Bretl, and Dieter Fox. Self-supervised 6d ob-               and Deirdre Quillen. Learning hand-eye coordination for
     ject pose estimation for robot manipulation. arXiv preprint              robotic grasping with deep learning and large-scale data col-
     arXiv:1909.10159, 2019.                                                  lection. The International Journal of Robotics Research,
                                                                              37(4-5):421–436, 2018.
 [9] Amaury Depierre, Emmanuel Dellandréa, and Liming Chen.
                                                                         [23] Yangyan Li, Rui Bu, Mingchao Sun, Wei Wu, Xinhan Di,
     Jacquard: A large scale dataset for robotic grasp detection.
                                                                              and Baoquan Chen. Pointcnn: Convolution on x-transformed
     In 2018 IEEE/RSJ International Conference on Intelligent
                                                                              points. In Advances in Neural Information Processing Sys-
     Robots and Systems (IROS), pages 3511–3516. IEEE, 2018.
                                                                              tems, pages 828–838, 2018.
[10] Yuval Eldar, Michael Lindenbaum, Moshe Porat, and                   [24] Hongzhuo Liang, Xiaojian Ma, Shuang Li, Michael Görner,
     Yehoshua Y Zeevi. The farthest point strategy for progres-               Song Tang, Bin Fang, Fuchun Sun, and Jianwei Zhang.
     sive image sampling. IEEE Transactions on Image Process-                 Pointnetgpd: Detecting grasp configurations from point sets.
     ing, 6(9):1305–1315, 1997.                                               In 2019 International Conference on Robotics and Automa-
[11] Kuan Fang, Yuke Zhu, Animesh Garg, Andrey Kurenkov,                      tion (ICRA), pages 3629–3635. IEEE, 2019.
     Viraj Mehta, Li Fei-Fei, and Silvio Savarese. Learning task-        [25] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,
     oriented grasping for tool manipulation from simulated self-             Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence
     supervision. arXiv preprint arXiv:1806.09266, 2018.                      Zitnick. Microsoft coco: Common objects in context. In Eu-
[12] Benjamin Graham, Martin Engelcke, and Laurens van der                    ropean conference on computer vision(ECCV), pages 740–
     Maaten. 3d semantic segmentation with submanifold sparse                 755. Springer, 2014.
     convolutional networks. In Proceedings of the IEEE Con-             [26] Jeffrey Mahler, Jacky Liang, Sherdil Niyaz, Michael Laskey,
     ference on Computer Vision and Pattern Recognition, pages                Richard Doan, Xinyu Liu, Juan Aparicio Ojea, and Ken
     9224–9232, 2018.                                                         Goldberg. Dex-net 2.0: Deep learning to plan robust grasps
[13] Di Guo, Fuchun Sun, Huaping Liu, Tao Kong, Bin Fang, and                 with synthetic point clouds and analytic grasp metrics. arXiv
     Ning Xi. A hybrid deep architecture for robotic grasp de-                preprint arXiv:1703.09312, 2017.
     tection. In 2017 IEEE International Conference on Robotics          [27] Douglas Morrison, Peter Corke, and Jürgen Leitner. Closing
     and Automation (ICRA), pages 1609–1614. IEEE, 2017.                      the loop for robotic grasping: A real-time, generative grasp
[14] Stefan Hinterstoisser, Vincent Lepetit, Slobodan Ilic, Ste-              synthesis approach. arXiv preprint arXiv:1804.05172, 2018.
     fan Holzer, Gary Bradski, Kurt Konolige, and Nassir Navab.          [28] Arsalan Mousavian, Clemens Eppner, and Dieter Fox. 6-dof
     Model based training, detection and pose estimation of                   graspnet: Variational grasp generation for object manipula-
     texture-less 3d objects in heavily cluttered scenes. In Asian            tion. arXiv preprint arXiv:1905.10520, 2019.
     conference on computer vision, pages 548–562. Springer,             [29] Van-Duc Nguyen. Constructing force-closure grasps. The In-
     2012.                                                                    ternational Journal of Robotics Research, 7(3):3–16, 1988.

                                                                      11452
[30] Lerrel Pinto and Abhinav Gupta.             Supersizing self-       [45] Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, and
     supervision: Learning to grasp from 50k tries and 700 robot              Dieter Fox. Posecnn: A convolutional neural network for
     hours. In 2016 IEEE international conference on robotics                 6d object pose estimation in cluttered scenes. arXiv preprint
     and automation (ICRA), pages 3406–3413. IEEE, 2016.                      arXiv:1711.00199, 2017.
[31] Charles R Qi, Or Litany, Kaiming He, and Leonidas J                 [46] Saining Xie, Sainan Liu, Zeyu Chen, and Zhuowen Tu. At-
     Guibas. Deep hough voting for 3d object detection in point               tentional shapecontextnet for point cloud recognition. In
     clouds. arXiv preprint arXiv:1904.09664, 2019.                           Proceedings of the IEEE Conference on Computer Vision
[32] Charles R Qi, Wei Liu, Chenxia Wu, Hao Su, and Leonidas J                and Pattern Recognition, pages 4606–4615, 2018.
     Guibas. Frustum pointnets for 3d object detection from rgb-         [47] Yifan Xu, Tianqi Fan, Mingye Xu, Long Zeng, and Yu Qiao.
     d data. In Proceedings of the IEEE Conference on Computer                Spidercnn: Deep learning on point sets with parameterized
     Vision and Pattern Recognition, pages 918–927, 2018.                     convolutional filters. In Proceedings of the European Con-
[33] Charles R Qi, Hao Su, Kaichun Mo, and Leonidas J Guibas.                 ference on Computer Vision (ECCV), pages 87–102, 2018.
     Pointnet: Deep learning on point sets for 3d classifica-            [48] Xinchen Yan, Jasmined Hsu, Mohammad Khansari, Yun-
     tion and segmentation. Proc. Computer Vision and Pattern                 fei Bai, Arkanath Pathak, Abhinav Gupta, James Davidson,
     Recognition (CVPR), IEEE, 2017.                                          and Honglak Lee. Learning 6-dof grasping interaction via
[34] Charles R Qi, Li Yi, Hao Su, and Leonidas J Guibas. Point-               deep geometry-aware 3d representations. In 2018 IEEE In-
     net++: Deep hierarchical feature learning on point sets in a             ternational Conference on Robotics and Automation (ICRA),
     metric space. arXiv preprint arXiv:1706.02413, 2017.                     pages 1–9. IEEE, 2018.
[35] Yuzhe Qin, Rui Chen, Hao Zhu, Meng Song, Jing Xu,                   [49] Yaoqing Yang, Chen Feng, Yiru Shen, and Dong Tian. Fold-
     and Hao Su. S4g: Amodal single-view single-shot se                       ingnet: Point cloud auto-encoder via deep grid deformation.
     (3) grasp detection in cluttered scenes. arXiv preprint                  In Proceedings of the IEEE Conference on Computer Vision
     arXiv:1910.14218, 2019.                                                  and Pattern Recognition, pages 206–215, 2018.
[36] Joseph Redmon and Anelia Angelova. Real-time grasp                  [50] Hanbo Zhang, Xuguang Lan, Site Bai, Xinwen Zhou,
     detection using convolutional neural networks. In 2015                   Zhiqiang Tian, and Nanning Zheng. Roi-based robotic grasp
     IEEE International Conference on Robotics and Automation                 detection for object overlapping scenes. arXiv preprint
     (ICRA), pages 1316–1322. IEEE, 2015.                                     arXiv:1808.10313, 2018.
[37] Shaoshuai Shi, Xiaogang Wang, and Hongsheng Li. Pointr-             [51] Yin Zhou and Oncel Tuzel. Voxelnet: End-to-end learning
     cnn: 3d object proposal generation and detection from point              for point cloud based 3d object detection. In Proceedings
     cloud. arXiv preprint arXiv:1812.04244, 2018.                            of the IEEE Conference on Computer Vision and Pattern
[38] Hang Su, Varun Jampani, Deqing Sun, Subhransu Maji,                      Recognition, pages 4490–4499, 2018.
     Evangelos Kalogerakis, Ming-Hsuan Yang, and Jan Kautz.
     Splatnet: Sparse lattice networks for point cloud processing.
     In Proceedings of the IEEE Conference on Computer Vision
     and Pattern Recognition, pages 2530–2539, 2018.
[39] Maxim Tatarchenko, Alexey Dosovitskiy, and Thomas Brox.
     Octree generating networks: Efficient convolutional archi-
     tectures for high-resolution 3d outputs. arXiv preprint
     arXiv:1703.09438, 2017.
[40] Maxim Tatarchenko, Jaesik Park, Vladlen Koltun, and Qian-
     Yi Zhou. Tangent convolutions for dense prediction in 3d.
     In Proceedings of the IEEE Conference on Computer Vision
     and Pattern Recognition, pages 3887–3896, 2018.
[41] Andreas ten Pas, Marcus Gualtieri, Kate Saenko, and Robert
     Platt. Grasp pose detection in point clouds. The International
     Journal of Robotics Research, 36(13-14):1455–1473, 2017.
[42] Jacob Varley, Jonathan Weisz, Jared Weiss, and Peter Allen.
     Generating multi-fingered robotic grasps via deep learning.
     In 2015 IEEE/RSJ International Conference on Intelligent
     Robots and Systems (IROS), pages 4415–4420. IEEE.
[43] Peng-Shuai Wang, Yang Liu, Yu-Xiao Guo, Chun-Yu Sun,
     and Xin Tong. O-cnn: Octree-based convolutional neu-
     ral networks for 3d shape analysis. ACM Transactions on
     Graphics (TOG), 36(4):72, 2017.
[44] Yue Wang, Yongbin Sun, Ziwei Liu, Sanjay E Sarma,
     Michael M Bronstein, and Justin M Solomon. Dynamic
     graph cnn for learning on point clouds. arXiv preprint
     arXiv:1801.07829, 2018.

                                                                      11453
