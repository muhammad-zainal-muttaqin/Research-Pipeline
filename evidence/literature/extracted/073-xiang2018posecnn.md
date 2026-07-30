---
source_id: 073
bibtex_key: xiang2018posecnn
title: PoseCNN: A Convolutional Neural Network for 6D Object Pose Estimation in Cluttered Scenes
year: 2018
domain_theme: Pose 6D
verified_pdf: 73_PoseCNN.pdf
char_count: 61819
---

PoseCNN: A Convolutional Neural Network for 6D
                                             Object Pose Estimation in Cluttered Scenes
                                                                Yu Xiang1,2 , Tanner Schmidt2 , Venkatraman Narayanan3 and Dieter Fox1,2
                                                                  1
                                                                 NVIDIA Research, 2 University of Washington, 3 Carnegie Mellon University
                                                           yux@nvidia.com, tws10@cs.washington.edu, venkatraman@cs.cmu.edu, dieterf@nvidia.com

                                            Abstract—Estimating the 6D pose of known objects is impor-
                                         tant for robots to interact with the real world. The problem is                                               Semantic labels
arXiv:1711.00199v3 [cs.CV] 26 May 2018

                                         challenging due to the variety of objects as well as the complexity
                                         of a scene caused by clutter and occlusions between objects. In
                                                                                                                                        PoseCNN
                                         this work, we introduce PoseCNN, a new Convolutional Neural                                                    3D translation
                                         Network for 6D object pose estimation. PoseCNN estimates the
                                         3D translation of an object by localizing its center in the image
                                         and predicting its distance from the camera. The 3D rotation
                                         of the object is estimated by regressing to a quaternion repre-        An input image
                                         sentation. We also introduce a novel loss function that enables                                                 3D rotation
                                         PoseCNN to handle symmetric objects. In addition, we contribute
                                         a large scale video dataset for 6D object pose estimation named                                                                    6D pose
                                         the YCB-Video dataset. Our dataset provides accurate 6D poses
                                         of 21 objects from the YCB dataset observed in 92 videos with         Fig. 1. We propose a novel PoseCNN for 6D object pose estimation, where
                                         133,827 frames. We conduct extensive experiments on our YCB-          the network is trained to perform three tasks: semantic labeling, 3D translation
                                         Video dataset and the OccludedLINEMOD dataset to show that            estimation, and 3D rotation regression.
                                         PoseCNN is highly robust to occlusions, can handle symmetric
                                         objects, and provide accurate pose estimation using only color        of existing methods. We introduce a novel Convolutional
                                         images as input. When using depth data to further refine the          Neural Network (CNN) for end-to-end 6D pose estimation
                                         poses, our approach achieves state-of-the-art results on the chal-    named PoseCNN. A key idea behind PoseCNN is to decouple
                                         lenging OccludedLINEMOD dataset. Our code and dataset are             the pose estimation task into different components, which
                                         available at https://rse-lab.cs.washington.edu/projects/posecnn/.     enables the network to explicitly model the dependencies
                                                                                                               and independencies between them. Specifically, PoseCNN
                                                              I. INTRODUCTION
                                                                                                               performs three related tasks as illustrated in Fig. 1. First, it
                                            Recognizing objects and estimating their poses in 3D has           predicts an object label for each pixel in the input image.
                                         a wide range of applications in robotic tasks. For instance,          Second, it estimates the 2D pixel coordinates of the object
                                         recognizing the 3D location and orientation of objects is             center by predicting a unit vector from each pixel towards the
                                         important for robot manipulation. It is also useful in human-         center. Using the semantic labels, image pixels associated with
                                         robot interaction tasks such as learning from demonstration.          an object vote on the object center location in the image. In
                                         However, the problem is challenging due to the variety of             addition, the network also estimates the distance of the object
                                         objects in the real world. They have different 3D shapes,             center. Assuming known camera intrinsics, estimation of the
                                         and their appearances on images are affected by lighting              2D object center and its distance enables us to recover its
                                         conditions, clutter in the scene and occlusions between objects.      3D translation T. Finally, the 3D Rotation R is estimated by
                                            Traditionally, the problem of 6D object pose estimation is         regressing convolutional features extracted inside the bounding
                                         tackled by matching feature points between 3D models and              box of the object to a quaternion representation of R. As we
                                         images [20, 25, 8]. However, these methods require that there         will show, the 2D center voting followed by rotation regression
                                         are rich textures on the objects in order to detect feature           to estimate R and T can be applied to textured/texture-less
                                         points for matching. As a result, they are unable to handle           objects and is robust to occlusions since the network is trained
                                         texture-less objects. With the emergence of depth cameras,            to vote on object centers even when they are occluded.
                                         several methods have been proposed for recognizing texture-              Handling symmetric objects is another challenge for pose
                                         less objects using RGB-D data [13, 3, 2, 26, 15]. For template-       estimation, since different object orientations may generate
                                         based methods [13, 12], occlusions significantly reduce the           identical observations. For instance, it is not possible to
                                         recognition performance. Alternatively, methods that perform          uniquely estimate the orientation of the red bowl or the wood
                                         learning to regress image pixels to 3D object coordinates in          block shown in Fig. 5. While pose benchmark datasets such as
                                         order to establish the 2D-3D correspondences for 6D pose              the OccludedLINEMOD dataset [17] consider a special sym-
                                         estimation [3, 4] cannot handle symmetric objects.                    metric evaluation for such objects, symmetries are typically
                                            In this work, we propose a generic framework for 6D object         ignored during network training. However, this can result in
                                         pose estimation where we attempt to overcome the limitations          bad training performance since a network receives inconsistent
loss signals, such as a high loss on an object orientation even    To deal with texture-less objects, several methods are proposed
though the estimation from the network is correct with respect     to learn feature descriptors using machine learning techniques
to the symmetry of the object. Inspired by this observation, we    [32, 10]. A few approaches have been proposed to directly
introduce ShapeMatch-Loss, a new loss function that focuses        regress to 3D object coordinate location for each pixel to
on matching the 3D shape of an object. We will show that           establish the 2D-3D correspondences [3, 17, 4]. But 3D
this loss function produces superior estimation for objects with   coordinate regression encounters ambiguities in dealing with
shape symmetries.                                                  symmetric objects.
   We evaluate our method on the OccludedLINEMOD                      In this work, we combine the advantages of both template-
dataset [17], a benchmark dataset for 6D pose estimation.          based methods and feature-based methods in a deep learning
On this challenging dataset, PoseCNN achieves state-of-the-        framework, where the network combines bottom-up pixel-wise
art results for both color only and RGB-D pose estimation          labeling with top-down object pose regression. Recently, the
(we use depth images in the Iterative Closest Point (ICP)          6D object pose estimation problem has received more attention
algorithm for pose refinement). To thoroughly evaluate our         thanks to the competition in the Amazon Picking Challenge
method, we additionally collected a large scale RGB-D video        (APC). Several datasets and approaches have been introduced
dataset named YCB-Video, which contains 6D poses of 21             for the specific setting in the APC [24, 35]. Our network has
objects from the YCB object set [5] in 92 videos with a total      the potential to be applied to the APC setting as long as the
of 133,827 frames. Objects in the dataset exhibit different        appropriate training data is provided.
symmetries and are arranged in various poses and spatial
configurations, generating severe occlusions between them.                                III. P OSE CNN
   In summary, our work has the following key contributions:          Given an input image, the task of 6D object pose estimation
   • We propose a novel convolutional neural network for 6D        is to estimate the rigid transformation from the object coordi-
      object pose estimation named PoseCNN. Our network            nate system O to the camera coordinate system C. We assume
      achieves end-to-end 6D pose estimation and is very robust    that the 3D model of the object is available and the object
      to occlusions between objects.                               coordinate system is defined in the 3D space of the model.
   • We introduce ShapeMatch-Loss, a new training loss func-       The rigid transformation here consists of an SE(3) transform
      tion for pose estimation of symmetric objects.               containing a 3D rotation R and a 3D translation T, where R
   • We contribute a large scale RGB-D video dataset for           specifies the rotation angles around the X-axis, Y -axis and Z-
      6D object pose estimation, where we provide 6D pose          axis of the object coordinate system O, and T is the coordinate
      annotations for 21 YCB objects.                              of the origin of O in the camera coordinate system C. In the
This paper is organized as follows. After discussing related       imaging process, T determines the object location and scale
work, we introduce PoseCNN for 6D object pose estimation,          in the image, while R affects the image appearance of the
followed by experimental results and a conclusion.                 object according to the 3D shape and texture of the object.
                                                                   Since these two parameters have distinct visual properties,
                   II. RELATED WORK                                we propose a convolutional neural network architecture that
   6D object pose estimation methods in the literature can be      internally decouples the estimation of R and T.
roughly classified into template-based methods and feature-
based methods. In template-based methods, a rigid template         A. Overview of the Network
is constructed and used to scan different locations in the input      Fig. 2 illustrates the architecture of our network for 6D
image. At each location, a similarity score is computed, and       object pose estimation. The network contains two stages. The
the best match is obtained by comparing these similarity scores    first stage consists of 13 convolutional layers and 4 max-
[12, 13, 6]. In 6D pose estimation, a template is usually          pooling layers, which extract feature maps with different reso-
obtained by rendering the corresponding 3D model. Recently,        lutions from the input image. This stage is the backbone of the
2D object detection methods are used as template matching          network since the extracted features are shared across all the
and augmented for 6D pose estimation, especially with deep         tasks performed by the network. The second stage consists of
learning-based object detectors [28, 23, 16, 29]. Template-        an embedding step that embeds the high-dimensional feature
based methods are useful in detecting texture-less objects.        maps generated by the first stage into low-dimensional, task-
However, they cannot handle occlusions between objects very        specific features. Then, the network performs three different
well, since the template will have low similarity score if the     tasks that lead to the 6D pose estimation, i.e., semantic
object is occluded.                                                labeling, 3D translation estimation, and 3D rotation regression,
   In feature-based methods, local features are extracted from     as described next.
either points of interest or every pixel in the image and
matched to features on the 3D models to establish the 2D-          B. Semantic Labeling
3D correspondences, from which 6D poses can be recovered              In order to detect objects in images, we resort to semantic
[20, 25, 30, 22]. Feature-based methods are able to handle         labeling, where the network classifies each image pixel into an
occlusions between objects. However, they require sufficient       object class. Compared to recent 6D pose estimation methods
textures on the objects in order to compute the local features.    that resort to object detection with bounding boxes [23, 16,
                        Feature Extraction                     Embedding                           Classification / Regression

                                                             64

                                                                    64                   Labels
                                                                      64 #classes
                                                              64

                                      512           512
A RGB Image                  256
                       128
                  64
                                                             128
                                                                                        Center          Center           Center
                                                                 128            direction X           direction Y       distance
                                                                   128 3 ×
                                                             128       #classes
     Convolution
                        Hough Voting
     + ReLU
                                                                                              RoIs
     Max Pooling        RoI Pooling                                                                                     For each RoI

    Deconvolution
                       Fully Connected                                                     512
       Addition                                                                                                       4×
                                                                                                     512
                                                                                                            4096 4096 #classes             6D Poses
                                                                                           512

                                         Fig. 2.   Architecture of PoseCNN for 6D object pose estimation.

29], semantic labeling provides richer information about the
objects and handles occlusions better.
   The embedding step of the semantic labeling branch, as
shown in Fig. 2, takes two feature maps with channel dimen-
sion 512 generated by the feature extraction stage as inputs.              camera coordinate
The resolutions of the two feature maps are 1/8 and 1/16 of
the original image size, respectively. The network first reduces
the channel dimension of the two feature maps to 64 using
two convolutional layers. Then it doubles the resolution of the                                                                     object coordinate
1/16 feature map with a deconvolutional layer. After that, the
two feature maps are summed and another deconvolutional
layer is used to increase the resolution by 8 times in order to            Fig. 3. Illustration of the object coordinate system and the camera coordinate
obtain a feature map with the original image size. Finally, a              system. The 3D translation can be estimated by localizing the 2D center of
                                                                           the object and estimating the 3D center distance from the camera.
convolutional layer operates on the feature map and generates
semantic labeling scores for pixels. The output of this layer              any location in the image. Also, it cannot handle multiple
has n channels with n the number of the semantic classes. In               object instances in the same category. Therefore, we propose
training, a softmax cross entropy loss is applied to train the             to estimate the 3D translation by localizing the 2D object
semantic labeling branch. While in testing, a softmax function             center in the image and estimating object distance from the
is used to compute the class probabilities of the pixels. The              camera. To see, suppose the projection of T on the image
design of the semantic labeling branch is inspired by the fully            is c = (cx , cy )T . If the network can localize c in the image
convolutional network in [19] for semantic labeling. It is also            and estimate the depth Tz , then we can recover Tx and Ty
used in our previous work for scene labeling [34].                         according to the following projection equation assuming a
                                                                           pinhole camera:
C. 3D Translation Estimation
                                                                                                 " # " Tx               #
  As illustrated in Fig. 3, the 3D translation T =                                                 cx      f x Tz + p x
(Tx , Ty , Tz )T is the coordinate of the object origin in the                                         =       T
                                                                                                                          ,            (1)
                                                                                                   cy      fy Tyz + py
camera coordinate system. A naive way of estimating T is
to directly regress the image features to T. However, this                 where fx and fy denote the focal lengths of the camera, and
approach is not generalizable since objects can appear in                  (px , py )T is the principal point. If the object origin O is the
                                                                                    After generating a set of object centers, we consider the
                                                                                  pixels that vote for an object center to be the inliers of the
                                                                                  center. Then the depth prediction of the center, Tz , is simply
                                                                                  computed as the mean of the depths predicted by the inliers.
                                                                                  Finally, using Eq. 1, we can estimate the 3D translation T.
                                                                                  In addition, the network generates the bounding box of the
                                                                                  object as the 2D rectangle that bounds all the inliers, and the
                                                                                  bounding box is used for 3D rotation regression.
                                                                                  D. 3D Rotation Regression
Fig. 4. Illustration of Hough voting for object center localization: Each pixel      The lowest part of Fig. 2 shows the 3D rotation regression
casts votes for image locations along the ray predicted from the network.         branch. Using the object bounding boxes predicted from the
                                                                                  Hough voting layer, we utilize two RoI pooling layers [11]
centroid of the object, we call c the 2D center of the object.                    to “crop and pool” the visual features generated by the first
   A straightforward way for localizing the 2D object center                      stage of the network for the 3D rotation regression. The pooled
is to directly detect the center point as in existing key point                   feature maps are added together and fed into three Fully-
detection methods [22, 7]. However, these methods would not                       Connected (FC) layers. The first two FC layers have dimension
work if the object center is occluded. Inspired by the tradi-                     4096, and the last FC layer has dimension 4 × n with n the
tional Implicit Shape Model (ISM) in which image patches                          number of object classes. For each class, the last FC layer
vote for the object center for detection [18], we design our                      outputs a 3D rotation represented by a quaternion.
network to regress to the center direction for each pixel in the                     To train the quaternion regression, we propose two loss
image. Specifically, for a pixel p = (x, y)T on the image, it                     functions, one of which is specifically designed to handle
regresses to three variables:                                                     symmetric objects. The first loss, called PoseLoss (PL OSS),
                          cx − x          cy − y      
                                                                                  operates in the 3D model space and measures the average
        (x, y) → nx =             , ny =           , Tz .    (2)
                          kc − pk         kc − pk                                 squared distance between points on the correct model pose and
Note that instead of directly regressing to the displacement                      their corresponding points on the model using the estimated
vector c−p, we design the network to regress to the unit length                   orientation. PL OSS is defined as
                               c−p                                                                          1 X
vector n = (nx , ny )T = kc−pk      , i.e., 2D center direction,
                                                                                          PL OSS(q̃, q) =           kR(q̃)x − R(q)xk2 ,       (3)
which is scale-invariant and therefore easier to be trained (as                                            2m
                                                                                                                       x∈M
we verified experimentally).
   The center regression branch of our network (Fig. 2) uses                      where M denotes the set of 3D model points and m is
the same architecture as the semantic labeling branch, except                     the number of points. R(q̃) and R(q) indicate the rotation
that the channel dimensions of the convolutional layers and                       matrices computed from the the estimated quaternion and the
the deconvolutional layers are different. We embed the high-                      ground truth quaternion, respectively. This loss has its unique
dimensional features into a 128-dimensional space instead of                      minimum when the estimated orientation is identical to the
64-dimensional since this branch needs to regress to three                        ground truth orientation 1 . Unfortunately, PL OSS does not
variables for each object class. The last convolutional layer in                  handle symmetric objects appropriately, since a symmetric
this branch has channel dimension 3 × n with n the number                         object can have multiple correct 3D rotations. Using such a
of object classes. In training, a smoothed L1 loss function is                    loss function on symmetric objects unnecessarily penalizes the
applied for regression as in [11].                                                network for regressing to one of the alternative 3D rotations,
   In order to find the 2D object center c of an object, a Hough                  thereby giving possibly inconsistent training signals.
voting layer is designed and integrated into the network. The                        While PL OSS could potentially be modified to handle
Hough voting layer takes the pixel-wise semantic labeling                         symmetric objects by manually specifying object symmetries
results and the center regression results as inputs. For each                     and then considering all correct orientations as ground truth
object class, it first computes the voting score for every                        options, we here introduce ShapeMatch-Loss (SL OSS), a loss
location in the image. The voting score indicates how likely                      function that does not require the specification of symmetries.
the corresponding image location is the center of an object                       SL OSS is defined as
in the class. Specifically, each pixel in the object class adds                                       1 X
                                                                                    SL OSS(q̃, q) =             min kR(q̃)x1 − R(q)x2 k2 . (4)
votes for image locations along the ray predicted from the                                           2m        x2 ∈M
                                                                                                               x1 ∈M
network (see Fig. 4). After processing all the pixels in the
object class, we obtain the voting scores for all the image                       As we can see, just like ICP, this loss measures the offset
locations. Then the object center is selected as the location                     between each point on the estimated model orientation and the
with the maximum score. For cases where multiple instances                        closest point on the ground truth model. SL OSS is minimized
of the same object class may appear in the image, we apply                        when the two 3D models match each other. In this way, the
non-maximum suppression to the voting scores, and then select                       1 It is very similar to a regression loss on the quaternions, as we have verified
locations with scores larger than a certain threshold.                            experimentally. We use this formulation for consistency with the other loss.
                                                                                                          TABLE I
                                                                                        S TATISTICS OF OUR YCB-V IDEO DATASET

                                                                                               Number of Objects         21
                                                                                             Total Number of Videos      92
                                                                                                 Held-out Videos         12
                                                                                                Min Object Count          3
                                                                                               Max Object Count           9
                                                                                               Mean Object Count        4.47
                                                                                               Number of Frames        133,827
                                                                                                    Resolution        640 x 480

                                                                             Fig. 6. Left: an example image from the dataset. Right: Textured 3D
 Fig. 5.   The subset of 21 YCB Objects selected to appear in our dataset.   object models (provided with the YCB dataset) rendered according
                                                                             to the pose annotations for this frame.
SL OSS will not penalize rotations that are equivalent with
respect to the 3D shape symmetry of the object.                              lower FOV, but given the minimum range of the depth sensor
                                                                             this was an acceptable trade-off. The full dataset comprises
                  IV. T HE YCB-V IDEO DATASET                                133,827 images, two full orders of magnitude larger than the
   Object-centric datasets providing ground-truth annotations                LINEMOD dataset. For more statistics relating to the dataset,
for object poses and/or segmentations are limited in size by the             see Table I. Fig. 6 shows one annotation example in our dataset
fact that the annotations are typically provided manually. For               where we render the 3D models according to the annotated
example, the popular LINEMOD dataset [13] provides manual                    ground truth pose. Note that our annotation accuracy suffers
annotations for around 1,000 images for each of the 15 objects               from several sources of error, including the rolling shutter
in the dataset. While such a dataset is useful for evaluation                of the RGB sensor, inaccuracies in the object models, slight
of model-based pose estimation techniques, it is orders of                   asynchrony between RGB and depth sensors, and uncertainties
magnitude smaller than a typical dataset for training state-                 in the intrinsic and extrinsic parameters of the cameras.
of-the-art deep neural networks. One solution to this problem
is to augment the data with synthetic images. However, care                                       V. EXPERIMENTS
must be taken to ensure that performance generalizes between
                                                                             A. Datasets
real and rendered scenes.
                                                                                In our YCB-Video dataset, we use 80 videos for training,
A. 6D Pose Annotation
                                                                             and test on 2,949 key frames extracted from the rest 12
   To avoid annotating all the video frames manually, we                     test videos. We also evaluate our method on the Occluded-
manually specify the poses of the objects only in the first                  LINEMOD dataset [17]. The authors of [17] selected one
frame of each video. Using Signed Distance Function (SDF)                    video with 1,214 frames from the original LINEMOD dataset
representations of each object, we refine the pose of each                   [13], and annotated ground truth poses for eight objects in
object in the first depth frame. Next, the camera trajectory                 that video: Ape, Can, Cat, Driller, Duck, Eggbox, Glue and
is initialized by fixing the object poses relative to one another            Holepuncher. There are significant occlusions between objects
and tracking the object configuration through the depth video.               in this video sequence, which makes this dataset challenging.
Finally, the camera trajectory and relative object poses are                 For training, we use the eight sequences from the original
refined in a global optimization step.                                       LINEMOD dataset corresponding to these eight objects. In
B. Dataset Characteristics                                                   addition, we generate 80,000 synthetic images for training on
                                                                             both datasets by randomly placing objects in a scene.
   The objects we used are a subset of 21 of the YCB objects
[5] as shown in Fig. 5, selected due to high-quality 3D models
                                                                             B. Evaluation Metrics
and good visibility in depth. The videos are collected using an
Asus Xtion Pro Live RGB-D camera in fast-cropping mode,                         We adopt the average distance (ADD) metric as proposed
which provides RGB images at a resolution of 640x480 at 30                   in [13] for evaluation. Given the ground truth rotation R and
FPS by capturing a 1280x960 image locally on the device and                  translation T and the estimated rotation R̃ and translation
transmitting only the center region over USB. This results in                T̃, the average distance computes the mean of the pairwise
higher effective resolution of RGB images at the cost of a                   distances between the 3D model points transformed according
to the ground truth pose and the estimated pose:                                  PLoss (non-symmetry)          SLoss (symmetry)
                  1 X
         ADD =            k(Rx + T) − (R̃x + T̃)k,           (5)
                  m
                     x∈M

where M denotes the set of 3D model points and m is the
number of points. The 6D pose is considered to be correct if
                                                                    wood block
the average distance is smaller than a predefined threshold. In
the OccludedLINEMOD dataset, the threshold is set to 10%
of the 3D model diameter. For symmetric objects such as the
Eggbox and Glue, the matching between points is ambiguous                         PLoss (non-symmetry)           SLoss (symmetry)
for some views. Therefore, the average distance is computed
using the closest point distance:
              1 X
  ADD-S =               min k(Rx1 + T) − (R̃x2 + T̃)k. (6)
             m         x2 ∈M
                x1 ∈M
                                                                    large clamp
Our design of the loss function for rotation regression is
motivated by these two evaluation metrics. Using a fixed
threshold in computing pose accuracy cannot reveal how a
method performs on these incorrect poses with respect to that      Fig. 7.    Comparison between the PL OSS and the SL OSS for 6D pose
threshold. Therefore, we vary the distance threshold in eval-      estimation on three symmetric objects in the YCB-Video dataset.
uation. In this case, we can plot an accuracy-threshold curve,     given the 3D model and an estimated pose, and assume that
and compute the area under the curve for pose evaluation.          each observed depth value is associated with the predicted
   Instead of computing distances in the 3D space, we can          depth value at the same pixel location. The residual for each
project the transformed points onto the image, and then            pixel is then the smallest distance from the observed point
compute the pairwise distances in the image space. This metric     in 3D to the plane defined by the rendered point in 3D and
is called the reprojection error that is widely used for 6D pose   its normal. Points with residuals above a specified threshold
estimation when only color images are used.                        are rejected and the remaining residuals are minimized using
C. Implementation Details                                          gradient descent. Semantic labels from the network are used
                                                                   to crop the observed points from the depth image. Since
   PoseCNN is implemented using the TensorFlow library [1].
                                                                   ICP is not robust to local minimums, we refinement multiple
The Hough voting layer is implemented on GPU as in [31]. In
                                                                   poses by perturbing the estimated pose from the network, and
training, the parameters of the first 13 convolutional layers in
                                                                   then select the best refined pose using the alignment metric
the feature extraction stage and the first two FC layers in the
                                                                   proposed in [33].
3D rotation regression branch are initialized with the VGG16
network [27] trained on ImageNet [9]. No gradient is back-         E. Analysis on the Rotation Regress Losses
propagated via the Hough voting layer. Stochastic Gradient
Descent (SGD) with momentum is used for training.                     We first conduct experiments to analyze the effect of the two
                                                                   loss functions for rotation regression on symmetric objects.
D. Baselines                                                       Fig. 7 shows the rotation error histograms for two symmetric
   3D object coordinate regression network. Since the state-       objects in the YCB-Video dataset (wood block and large
of-the-art 6D pose estimation methods mostly rely on re-           clamp) using the two loss functions in training. The rotation
gressing image pixels to 3D object coordinates [3, 4, 21],         errors of the PL OSS for the wood block and the large clamp
we implement a variation of our network for 3D object              span from 0 degree to 180 degree. The two histograms indicate
coordinate regression for comparison. In this network, instead     that the network is confused by the symmetric objects. While
of regressing to center direction and depth as in Fig. 2, we       the histograms of the SL OSS concentrate on the 180 degree
regress each pixel to its 3D coordinate in the object coordinate   error for the wood block and 0 degree and 180 degree for
system. We can use the same architecture since each pixel still    the large clamp, since they are symmetric with respect to 180
regresses to three variables for each class. Then we remove        degree rotation around their coordinate axes.
the 3D rotation regression branch. Using the semantic labeling
results and 3D object coordinate regression results, the 6D        F. Results on the YCB-Video Dataset
pose is recovered using the pre-emptive RANSAC as in [4].             Table II and Fig. 8(a) presents detailed evaluation for all the
   Pose refinement. The 6D pose estimated from our network         21 objects in the YCB-Video dataset. We show the area under
can be refined when depth is available. We use the Iterative       the accuracy-threshold curve using both the ADD metric and
Closest Point (ICP) algorithm to refine the 6D pose. Specif-       the ADD-S metric, where we vary the threshold for the average
ically, we employ ICP with projective data association and a       distance and then compute the pose accuracy. The maximum
point-plane residual term. We render a predicted point cloud       threshold is set to 10cm.
                                                           TABLE II
A REA UNDER THE ACCURACY- THRESHOLD CURVE FOR 6D POSE EVALUATION ON THE YCB-V IDEO DATASET. R ED COLORED OBJECTS ARE SYMMETRIC .

                                                     RGB                                              RGB-D
                                       3D Coordinate       PoseCNN            3D Coordinate      3D Coordinate+ICP     PoseCNN+ICP
              Object                   ADD ADD-S        ADD ADD-S             ADD ADD-S          ADD      ADD-S        ADD ADD-S
              002 master chef can      12.3    34.4     50.9     84.0         61.4    90.1       72.7      95.7        69.0   95.8
              003 cracker box          16.8    40.0     51.7     76.9         57.4    77.4       82.7      91.0        80.7   91.8
              004 sugar box            28.7    48.9     68.6     84.3         85.5    93.3       94.6      97.5        97.2   98.2
              005 tomato soup can      27.3    42.2     66.0     80.9         84.5    92.1       86.1      94.5        81.6   94.5
              006 mustard bottle       25.9    44.8     79.9     90.2         82.8    91.1       97.6      98.3        97.0   98.4
              007 tuna fish can         5.4    10.4     70.4     87.9         68.8    86.9       76.7      91.4        83.1   97.1
              008 pudding box          14.9    26.3     62.9     79.0         74.8    89.3       86.0      94.9        96.6   97.9
              009 gelatin box          25.4    36.7     75.2     87.1         93.9    97.2       98.2      98.8        98.2   98.8
              010 potted meat can      18.7    32.3     59.6     78.5         70.9    84.0       78.9      87.8        83.8   92.8
              011 banana                3.2     8.8     72.3     85.9         50.7    77.3       73.5      94.3        91.6   96.9
              019 pitcher base         27.3    54.3     52.5     76.8         58.2    83.8       81.1      95.6        96.7   97.8
              021 bleach cleanser      25.2    44.3     50.5     71.9         74.1    89.2       87.2      95.7        92.3   96.8
              024 bowl                  2.7    25.4      6.5     69.7          8.7    67.4        8.3      77.9        17.5   78.3
              025 mug                   9.0    20.0     57.7     78.0         57.1    85.3       67.0      91.1        81.4   95.1
              035 power drill          18.0    36.1     55.1     72.8         79.4    89.4       93.2      96.2        96.9   98.0
              036 wood block            1.2    19.6     31.8     65.8         14.6    76.7       21.7      85.2        79.2   90.5
              037 scissors              1.0     2.9     35.8     56.2         61.0    82.8       66.0      88.3        78.4   92.2
              040 large marker          0.2     0.3     58.0     71.4         72.4    82.8       74.1      85.5        85.4   97.2
              051 large clamp           6.9    14.6     25.0     49.9         48.0    67.6       54.6      74.9        52.6   75.4
              052 extra large clamp     2.7    14.0     15.8     47.0         22.1    49.0       25.2      56.4        28.7   65.3
              061 foam brick            0.6     1.2     40.4     87.8         40.0    82.4       46.5      89.9        48.3   97.1
              ALL                      15.1    29.8     53.7     75.9         64.6    83.7       74.5      90.1        79.3   93.0

                  (a) YCB-Video Results                                                        (b) OccludedLINEMOD Results

    Fig. 8.   (a) Detailed results on the YCB-Video dataset. (b) Accuracy-threshold curves with reprojectin error on the OccludedLINEMOD dataset.

   We can see that i) By only using color images, our network                 Fig. 9 displays some 6D pose estimation results on the
significantly outperforms the 3D coordinate regression net-                 YCB-Video dataset. We can see that the center prediction is
work combined with the pre-emptive RANSAC algorithm for                     quite accurate even if the center is occluded by another object.
6D pose estimation. When there are errors in the 3D coordinate              Our network with color only is already able to provide good
regression results, the estimated 6D pose can drift far away                6D pose estimation. With ICP refinement, the accuracy of the
from the ground truth pose. While in our network, the center                6D pose is further improved.
localization helps to constrain the 3D translation estimation
even if the object is occluded. ii) Refining the poses with ICP             G. Results on the OccludedLINEMOD Dataset
significantly improves the performance. PoseCNN with ICP
                                                                               The OccludedLINEMOD dataset is challenging due to sig-
achieves superior performance compared to the 3D coordinate
                                                                            nificant occlusions between objects. We first conduct experi-
regression network when using depth images. The initial pose
                                                                            ments using color images only. Fig. 8(b) shows the accuracy-
in ICP is critical for convergence. PoseCNN provides better
                                                                            threshold curves with reprojection error for 7 objects in the
initial 6D poses for ICP refinement. iii) We can see that some
                                                                            dataset, where we compare PoseCNN with [29] that achieves
objects are more difficult to handle such as the tuna fish
                                                                            the current state-of-the-art result on this dataset using color im-
can that is small and with less texture. The network is also
                                                                            ages as input. Our method significantly outperforms [29] by a
confused by the large clamp and the extra large clamp since
                                                                            large margin, especially when the reprojection error threshold
they have the same appearance. The 3D coordinate regression
                                                                            is small. These results show that PoseCNN is able to correctly
network cannot handle symmetric objects very well such as
                                                                            localize the target object even under severe occlusions.
the banana and the bowl.
                                                                               By refining the poses using depth images in ICP, our method
                                                          TABLE III
  6D POSE ESTIMATION ACCURACY ON THE O CCLUDED LINEMOD DATASET. R ED COLORED OBJECTS ARE SYMMETRIC . A LL METHODS USE DEPTH
                                                 EXCEPT FOR P OSE CNN C OLOR .

   Method        Michel et al. [21] Hinterstoisser et al. [14] Krull et al. [17] Brachmann et al. [3] Ours PoseCNN Color Ours PoseCNN+ICP
   Ape                 80.7                   81.4                   68.0              53.1                   9.6               76.2
   Can                 88.5                   94.7                   87.9              79.9                   45.2              87.4
   Cat                 57.8                   55.2                   50.6              28.2                   0.93              52.2
   Driller             94.7                   86.0                   91.2              82.0                   41.4              90.3
   Duck                74.4                   79.7                   64.7              64.3                   19.6              77.7
   Eggbox              47.6                   65.5                   41.5               9.0                   22.0              72.2
   Glue                73.8                   52.1                   65.3              44.5                   38.5              76.7
   Holepuncher         96.3                   95.5                   92.9              91.6                   22.1              91.4
   MEAN                76.7                   76.3                   70.3              56.6                   24.9              78.0

     Input
    Image

 Labeling
 & Centers

 PoseCNN
   Color

 PoseCNN
    ICP
                                          YCB-Video Dataset                                    OccludedLINEMOD Dataset
                         Fig. 9.   Examples of 6D object pose estimation results on the YCB-Video dataset from PoseCNN.

also outperforms the state-of-the-art methods using RGB-                  robustly independent of scale. More importantly, pixels vote
D data as input. Table III summarizes the pose estimation                 the object center even if it is occluded by other objects.
accuracy on the OccludedLINEMOD dataset. The most im-                     The 3D rotation is predicted by regressing to a quaternion
provement comes from the two symmetric objects “Eggbox”                   representation. Two new loss functions are introduced for
and “Glue”. By using our ShapeMatch-Loss for training,                    rotation estimation, with the ShapeMatch-Loss designed for
PoseCNN is able to correctly estimate the 6D pose of the two              symmetric objects. As a result, PoseCNN is able to handle
objects with respect to symmetry. We also present the result              occlusion and symmetric objects in cluttered scenes. We also
of PoseCNN using color only in Table III. These accuracies                introduce a large scale video dataset for 6D object pose
are much lower since the threshold here is usually smaller                estimation. Our results are extremely encouraging in that they
than 2cm. It is very challenging for color-based methods to               indicate that it is feasible to accurately estimate the 6D pose of
obtain 6D poses within such small threshold when there are                objects in cluttered scenes using vision data only. This opens
occlusions between objects. Fig. 9 shows two examples of the              the path to using cameras with resolution and field of view that
6D pose estimation results on the OccludedLINEMOD dataset.                goes far beyond currently used depth camera systems. We note
                                                                          that the SL OSS sometimes results in local minimums in the
                     VI. CONCLUSIONS                                      pose space similar to ICP. It would be interesting to explore
   In this work, we introduce PoseCNN, a convolutional neural             more efficient way in handle symmetric objects in 6D pose
network for 6D object pose estimation. PoseCNN decouples                  estimation in the future.
the estimation of 3D rotation and 3D translation. It estimates
                                                                                              ACKNOWLEDGMENTS
the 3D translation by localizing the object center and predict-
ing the center distance. By regressing each pixel to a unit                 This work was funded in part by Siemens and by NSF STTR
vector towards the object center, the center can be estimated             grant 63-5197 with Lula Robotics.
                       R EFERENCES                                   888, 2012.
                                                                [13] Stefan Hinterstoisser, Vincent Lepetit, Slobodan Ilic,
 [1] Martı́n Abadi, Paul Barham, Jianmin Chen, Zhifeng               Stefan Holzer, Gary Bradski, Kurt Konolige, and Nassir
     Chen, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay          Navab. Model based training, detection and pose estima-
     Ghemawat, Geoffrey Irving, Michael Isard, et al. Ten-           tion of texture-less 3D objects in heavily cluttered scenes.
     sorFlow: A system for large-scale machine learning. In          In Asian Conference on Computer Vision (ACCV), pages
     OSDI, volume 16, pages 265–283, 2016.                           548–562, 2012.
 [2] Liefeng Bo, Xiaofeng Ren, and Dieter Fox. Learning         [14] Stefan Hinterstoisser, Vincent Lepetit, Naresh Rajkumar,
     hierarchical sparse features for RGB-D object recogni-          and Kurt Konolige. Going further with point pair
     tion. International Journal of Robotics Research (IJRR),        features. In European Conference on Computer Vision
     33(4):581–599, 2014.                                            (ECCV), pages 834–848, 2016.
 [3] Eric Brachmann, Alexander Krull, Frank Michel, Stefan      [15] Wadim Kehl, Fausto Milletari, Federico Tombari, Slo-
     Gumhold, Jamie Shotton, and Carsten Rother. Learning            bodan Ilic, and Nassir Navab. Deep learning of local
     6D object pose estimation using 3D object coordinates.          RGB-D patches for 3D object detection and 6D pose
     In European Conference on Computer Vision (ECCV),               estimation. In European Conference on Computer Vision
     pages 536–551, 2014.                                            (ECCV), pages 205–220, 2016.
 [4] Eric Brachmann, Frank Michel, Alexander Krull,             [16] Wadim Kehl, Fabian Manhardt, Federico Tombari, Slo-
     Michael Ying Yang, Stefan Gumhold, and Carsten                  bodan Ilic, and Nassir Navab. SSD-6D: Making RGB-
     Rother. Uncertainty-driven 6D pose estimation of ob-            based 3D detection and 6D pose estimation great again.
     jects and scenes from a single RGB image. In IEEE               In IEEE International Conference on Computer Vision
     Conference on Computer Vision and Pattern Recognition           (ICCV), pages 1521–1529, 2017.
     (CVPR), pages 3364–3372, 2016.                             [17] Alexander Krull, Eric Brachmann, Frank Michel,
 [5] Berk Calli, Arjun Singh, Aaron Walsman, Siddhartha              Michael Ying Yang, Stefan Gumhold, and Carsten
     Srinivasa, Pieter Abbeel, and Aaron M Dollar. The YCB           Rother. Learning analysis-by-synthesis for 6D pose
     object and model set: Towards common benchmarks for             estimation in RGB-D images. In IEEE International
     manipulation research. In International Conference on           Conference on Computer Vision (ICCV), pages 954–962,
     Advanced Robotics (ICAR), pages 510–517, 2015.                  2015.
 [6] Zhe Cao, Yaser Sheikh, and Natasha Kholgade Banerjee.      [18] Bastian Leibe, Ales Leonardis, and Bernt Schiele. Com-
     Real-time scalable 6DOF pose estimation for textureless         bined object categorization and segmentation with an
     objects. In IEEE International Conference on Robotics           implicit shape model. In ECCV Workshop on statistical
     and Automation (ICRA), pages 2441–2448, 2016.                   learning in computer vision, 2004.
 [7] Zhe Cao, Tomas Simon, Shih-En Wei, and Yaser Sheikh.       [19] Jonathan Long, Evan Shelhamer, and Trevor Darrell.
     Realtime multi-person 2D pose estimation using part             Fully convolutional networks for semantic segmentation.
     affinity fields. In IEEE Conference on Computer Vision          In IEEE Conference on Computer Vision and Pattern
     and Pattern Recognition (CVPR), 2017.                           Recognition (CVPR), pages 3431–3440, 2015.
 [8] Alvaro Collet, Manuel Martinez, and Siddhartha S Srini-    [20] David G Lowe. Object recognition from local scale-
     vasa. The MOPED framework: Object recognition and               invariant features. In IEEE International Conference on
     pose estimation for manipulation. International Journal         Computer Vision (ICCV), volume 2, pages 1150–1157,
     of Robotics Research (IJRR), 30(10):1284–1306, 2011.            1999.
 [9] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li,     [21] Frank Michel, Alexander Kirillov, Erix Brachmann,
     and Li Fei-Fei. ImageNet: A large-scale hierarchical            Alexander Krull, Stefan Gumhold, Bogdan Savchynskyy,
     image database. In IEEE Conference on Computer Vision           and Carsten Rother. Global hypothesis generation for 6D
     and Pattern Recognition (CVPR), pages 248–255, 2009.            object pose estimation. IEEE Conference on Computer
[10] Andreas Doumanoglou, Vassileios Balntas, Rigas Kousk-           Vision and Pattern Recognition (CVPR), 2017.
     ouridas, and Tae-Kyun Kim. Siamese regression net-         [22] Georgios Pavlakos, Xiaowei Zhou, Aaron Chan, Kon-
     works with efficient mid-level feature extraction for 3D        stantinos G Derpanis, and Kostas Daniilidis. 6-DOF
     object pose estimation. arXiv preprint arXiv:1607.02257,        object pose from semantic keypoints. IEEE International
     2016.                                                           Conference on Robotics and Automation (ICRA), 2017.
[11] Ross Girshick. Fast R-CNN. In IEEE International           [23] Mahdi Rad and Vincent Lepetit. BB8: A scalable, ac-
     Conference on Computer Vision (ICCV), pages 1440–               curate, robust to partial occlusion method for predicting
     1448, 2015.                                                     the 3D poses of challenging objects without using depth.
[12] Stefan Hinterstoisser, Cedric Cagniart, Slobodan Ilic,          In IEEE International Conference on Computer Vision
     Peter Sturm, Nassir Navab, Pascal Fua, and Vincent              (ICCV), 2017.
     Lepetit. Gradient response maps for real-time detection    [24] Colin Rennie, Rahul Shome, Kostas E Bekris, and Al-
     of textureless objects. IEEE Transactions on Pattern            berto F De Souza. A dataset for improved RGBD-based
     Analysis and Machine Intelligence (TPAMI), 34(5):876–           object detection and pose estimation for warehouse pick-
     and-place. IEEE Robotics and Automation Letters, 1(2):
     1179–1185, 2016.
[25] Fred Rothganger, Svetlana Lazebnik, Cordelia Schmid,
     and Jean Ponce. 3D object modeling and recognition
     using local affine-invariant image descriptors and multi-
     view spatial constraints. International Journal of Com-
     puter Vision (IJCV), 66(3):231–259, 2006.
[26] Max Schwarz, Hannes Schulz, and Sven Behnke. RGB-
     D object recognition and pose estimation based on pre-
     trained convolutional neural network features. In IEEE
     International Conference on Robotics and Automation
     (ICRA), pages 1329–1335, 2015.
[27] Karen Simonyan and Andrew Zisserman. Very deep
     convolutional networks for large-scale image recognition.
     arXiv preprint arXiv:1409.1556, 2014.
[28] Hao Su, Charles R Qi, Yangyan Li, and Leonidas J
     Guibas. Render for CNN: Viewpoint estimation in
     images using CNNs trained with rendered 3D model
     views. In IEEE International Conference on Computer
     Vision (ICCV), pages 2686–2694, 2015.
[29] Bugra Tekin, Sudipta N Sinha, and Pascal Fua. Real-time
     seamless single shot 6D object pose prediction. In IEEE
     Conference on Computer Vision and Pattern Recognition
     (CVPR), 2018.
[30] Shubham Tulsiani and Jitendra Malik. Viewpoints and
     keypoints. In IEEE Conference on Computer Vision and
     Pattern Recognition (CVPR), pages 1510–1519, 2015.
[31] Gert-Jan van den Braak, Cedric Nugteren, Bart Mesman,
     and Henk Corporaal. Fast Hough transform on GPUs:
     Exploration of algorithm trade-offs. In International
     Conference on Advanced Concepts for Intelligent Vision
     Systems, pages 611–622, 2011.
[32] Paul Wohlhart and Vincent Lepetit. Learning descriptors
     for object recognition and 3D pose estimation. In IEEE
     Conference on Computer Vision and Pattern Recognition
     (CVPR), pages 3109–3118, 2015.
[33] Jay M Wong, Vincent Kee, Tiffany Le, Syler Wagner,
     Gian-Luca Mariottini, Abraham Schneider, Lei Hamilton,
     Rahul Chipalkatty, Mitchell Hebert, David Johnson, et al.
     SegICP: Integrated deep semantic segmentation and pose
     estimation. arXiv preprint arXiv:1703.01661, 2017.
[34] Yu Xiang and Dieter Fox. DA-RNN: Semantic map-
     ping with data associated recurrent neural networks. In
     Robotics: Science and Systems (RSS). 2017.
[35] Andy Zeng, Kuan-Ting Yu, Shuran Song, Daniel Suo,
     Ed Walker, Alberto Rodriguez, and Jianxiong Xiao.
     Multi-view self-supervised deep learning for 6D pose
     estimation in the amazon picking challenge. In IEEE
     International Conference on Robotics and Automation
     (ICRA), pages 1386–1383, 2017.
