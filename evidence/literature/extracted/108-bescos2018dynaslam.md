---
source_id: 108
bibtex_key: bescos2018dynaslam
title: DynaSLAM: Tracking, Mapping, and Inpainting in Dynamic Scenes
year: 2018
domain_theme: RGB-D SLAM
verified_pdf: 108_DynaSLAM.pdf
char_count: 52858
---

DynaSLAM: Tracking, Mapping and Inpainting in Dynamic Scenes
                                                                           Berta Bescos, José M. Fácil, Javier Civera and José Neira

                                            Abstract— The assumption of scene rigidity is typical in
                                         SLAM algorithms. Such a strong assumption limits the use
                                         of most visual SLAM systems in populated real-world environ-
                                         ments, which are the target of several relevant applications like
                                         service robotics or autonomous vehicles.                                             (a) Input RGB-D frames with dynamic content.
                                            In this paper we present DynaSLAM, a visual SLAM system
arXiv:1806.05620v2 [cs.CV] 15 Aug 2018

                                         that, building on ORB-SLAM2 [1], adds the capabilities of dy-
                                         namic object detection and background inpainting. DynaSLAM
                                         is robust in dynamic scenarios for monocular, stereo and
                                         RGB-D configurations. We are capable of detecting the moving
                                         objects either by multi-view geometry, deep learning or both.
                                         Having a static map of the scene allows inpainting the frame            (b) Output RGB-D frames. Dynamic content has been removed. Occluded
                                         background that has been occluded by such dynamic objects.              background has been reconstructed with information from previous views.
                                            We evaluate our system in public monocular, stereo and
                                         RGB-D datasets. We study the impact of several accuracy/speed
                                         trade-offs to assess the limits of the proposed methodology. Dy-
                                         naSLAM outperforms the accuracy of standard visual SLAM
                                         baselines in highly dynamic scenarios. And it also estimates
                                         a map of the static parts of the scene, which is a must for
                                         long-term applications in real-world environments.

                                                              I. INTRODUCTION
                                            Simultaneous Localization and Mapping (SLAM) is a
                                         prerequisite for many robotic applications, for example
                                         collision-less navigation. SLAM techniques estimate jointly
                                         a map of an unknown environment and the robot pose                      (c) Map of the static part of the scene, after removal of the dynamic objects.
                                         within such map, only from the data streams of its on-board             Fig. 1: Overview of DynaSLAM results for the RGB-D case.
                                         sensors. The map allows the robot to continually localize
                                         within the same environment without accumulating drift.
                                         This is in contrast to odometry approaches that integrate the           a consequence, they can only manage small fractions of
                                         incremental motion estimated within a local window and are              dynamic content by classifying them as outliers to such static
                                         unable to correct the drift when revisiting places.                     model. Although the static assumption holds for some robotic
                                            Visual SLAM, where the main sensor is a camera, has                  applications, it limits the applicability of visual SLAM in
                                         received a high degree of attention and research efforts over           many relevant cases, such as intelligent autonomous systems
                                         the last years. The minimalistic solution of a monocular cam-           operating in populated real-world environments over long
                                         era has practical advantages with respect to size, power and            periods of time.
                                         cost, but also several challenges such as the unobservability              Visual SLAM can be classified into feature-based methods
                                         of the scale or state initialization. By using more complex             [2], [3], that rely on salient points matching and can only esti-
                                         setups, like stereo or RGB-D cameras, these issues are solved           mate a sparse reconstruction; and direct methods [4], [5], [6],
                                         and the robustness of visual SLAM systems can be greatly                which are able to estimate in principle a completely dense
                                         improved.                                                               reconstruction by the direct minimization of the photometric
                                            The research community has addressed SLAM from                       error and TV regularization. Some direct methods focus on
                                         many different angles. However, the vast majority of the                the high-gradient areas estimating semi-dense maps [7], [8].
                                         approaches and datasets assume a static environment. As                    None of the above methods, considered the state of the
                                                                                                                 art, address the very common problem of dynamic objects
                                            This work has been supported by NVIDIA Corporation through the
                                         donation of a Titan X GPU, by the Spanish Ministry of Economy and       in the scene, e.g., people walking, bicycles or cars. Detecting
                                         Competitiveness (projects DPI2015-68905-P and DPI2015-67275-P, FPI      and dealing with dynamic objects in visual SLAM reveals
                                         grant BES-2016-077836), and by the Aragón regional government (Grupo   several challenges for both mapping and tracking, including:
                                         DGA T04-FSE).
                                            Berta Bescos, José M. Fácil, Javier Civera and José Neira            1) How to detect such dynamic objects in the images to:
                                         are with the Instituto de Investigación en Ingenierı́a de
                                         Aragón (I3A), Universidad de Zaragoza, Zaragoza 50018, Spain                  a) Prevent the tracking algorithm from using
                                         {bbescos,jmfacil,jcivera,jneira}@unizar.es                                        matches that belong to dynamic objects.
         b) Prevent the mapping algorithm from including            • Wang and Huang [14] segment the dynamic objects in
            moving objects as part of the 3D map.                     the scene using RGB optical flow.
   2) How to complete the part of the 3D map that is                • Kim et al. [15] propose to obtain the static parts of the

       temporally occluded by a moving object.                        scene by computing the difference between consecutive
   Many applications would greatly benefit from progress              depth images projected over the same plane.
                                                                    • Sun et al. [16] calculate the difference in intensity
along these lines. Among others, augmented reality, au-
tonomous vehicles, and medical imaging. All of them could             between consecutive RGB images. Pixel classification
for instance safely reuse maps from previous runs. Detecting          is done with the segmentation of the quantized depth
and dealing with dynamic objects is a requisite to estimate           image.
stable maps, useful for long-term applications. If the dynamic       All the methods –both feature-based and direct ones–
content is not detected, it becomes part of the 3D map,           that map the static scene parts only from the information
complicating its usability for tracking or relocation purposes.   contained in the sequence [1], [3], [9], [12], [13], [14], [15],
   In this work we propose an on-line algorithm to deal with      [16], [17], fail to estimate lifelong models when an a priori
dynamic objects in RGB-D, stereo and monocular SLAM.              dynamic object remains static, e.g., parked cars or people
This is done by adding a front-end stage to the state-of-         sitting. On the other hand, Wangsiripitak and Murray [10],
the-art ORB-SLAM2 system [1], with the purpose of having          and Riazuelo et al. [11] would detect those a priori dynamic
a more accurate tracking and a reusable map of the scene.         objects, but would fail to detect changes produced by static
In the monocular and stereo cases our proposal is to use a        objects, e.g., a chair a person is pushing, or a ball that
CNN to pixel-wise segment the a priori dynamic objects            someone has thrown. That is, the former approach succeeds
in the frames (e.g., people and cars), so that the SLAM           in detecting moving objects, and the second one in detecting
algorithm does not extract features on them. In the RGB-          several movable objects. Our proposal, DynaSLAM, com-
D case we propose to combine multi-view geometry models           bines multi-view geometry and deep learning in order to
and deep-learning-based algorithms for detecting dynamic          address both situations. Similarly, Anrus et al. [18] segment
objects and, after having removed them from the images,           dynamic objects by combining a dynamic classifier and
inpaint the occluded background with the correct information      multi-view geometry.
of the scene (Fig. 1).
   The rest of the paper is structured as follows: section II                   III. SYSTEM DESCRIPTION
discusses related work, section III gives the details of our         Fig. 2 shows an overview of our system. First of all, the
proposal, section IV details the experimental results, and        RGB channels pass through a CNN that segments out pixel-
section V presents the conclusions and lines for future work.     wise all the a priori dynamic content, e.g., people or vehicles.
                  II. RELATED WORK                                   In the RGB-D case, we use multi-view geometry to im-
                                                                  prove the dynamic content segmentation in two ways. First,
   Dynamic objects are, in most SLAM systems, classified as       we refine the segmentation of the dynamic objects previously
spurious data and therefore neither included in the map nor       obtained by the CNN. Second, we label as dynamic new
used for camera tracking. The most typical outlier rejection      object instances that are static most of the time (i.e., detect
algorithms are RANSAC (e.g., in ORB-SLAM [3], [1]) and            moving objects that were not set to movable in the CNN
robust cost functions (e.g., in PTAM [2]).                        stage).
   There are several SLAM systems that address more
                                                                     For that purpose, it is necessary to know the camera pose,
specifically the dynamic scene content. Within feature-based
                                                                  for which a low-cost tracking module has been implemented
SLAM methods, some of the most relevant are:
                                                                  to localize the camera within the already created scene map.
   • Tan et al. [9] detect changes that take place in the scene   These segmented frames are the ones which are used to
     by projecting the map features into the current frame for    obtain the camera trajectory and the map of the scene.
     appearance and structure validation.                         Notice that if the moving objects in the scene are not within
   • Wangsiripitak and Murray [10] track known 3D dy-             the CNN classes, the multi-view geometry stage would still
     namic objects in the scene. Similarly, Riazuelo et al.       detect the dynamic content, but the accuracy might decrease.
     [11] deal with human activity by detecting and tracking         Once this full dynamic object detection and localization
     people.                                                      of the camera have been done, we aim to reconstruct the
   • More recently, the work of Li and Lee [12] uses
                                                                  occluded background of the current frame with static in-
     depth edges points, which have an associated weight          formation from previous views. These synthetic frames are
     indicating its probability of belonging to a dynamic         relevant for applications like augmented and virtual reality,
     object.                                                      and place recognition in lifelong mapping.
   Direct methods are, in general, more sensitive to dynamic         In the monocular and stereo cases, the images are seg-
objects in the scene. The most relevant works specifically        mented by the CNN so that keypoints belonging to the a
designed for dynamic scenes are:                                  priori dynamic objects are neither tracked nor mapped.
   • Alcantarilla et al. [13] detect moving objects by means         All the different stages are described in depth in the next
     of a scene flow representation with stereo cameras.          subsections (III-A to III-E).
Fig. 2: Block diagram of our proposal. In the stereo and monocular pipeline (black continuous line) the images pass through a
Convolutional Neural Network (Mask R-CNN) for computing the pixel-wise semantic segmentation of the a priori dynamic
objects before being used for the mapping and tracking. In the RGB-D case (black dashed line) a second approach based on
multi-view geometry is added for a more accurate motion segmentation, for which we need a low-cost tracking algorithm.
Once the position of the camera is known (Tracking and Mapping output), we can inpaint the background occluded by
dynamic objects. The red dotted line represents the data flow of the stored sparse map.

A. Segmentation of Potentially Dynamic Content using a             C. Segmentation of Dynamic Content using Mask R-CNN
CNN                                                                and Multi-view Geometry
   For detecting dynamic objects we propose to use a                  By using Mask R-CNN, most of the dynamic objects
CNN that obtains a pixel-wise semantic segmentation of             can be segmented and not used for tracking and mapping.
the images. In our experiments we use Mask R-CNN [19],             However, there are objects that cannot be detected by this
which is the state of the art for object instance segmen-          approach because they are not a priori dynamic, but movable.
tation. Mask R-CNN can obtain both pixel-wise semantic             Examples of the latest are a book carried by someone, a chair
segmentation and the instance labels. For this work we use         that someone is moving, or even furniture changes in long-
the pixel-wise semantic segmentation information, but the          term mapping. The approach utilized for dealing with these
instance labels could be useful in future work for the tracking    cases is detailed in this section.
of the different moving objects. We use the TensorFlow                For each input frame, we select the previous keyframes
implementation by Matterport1 .                                    that have the highest overlaps. This is done by taking into
   The input of Mask R-CNN is the RGB original image. The
                                                                   account both the distance and the rotation between the new
idea is to segment those classes that are potentially dynamic
                                                                   frame and each of the keyframes, similarly to Tan et al. [9].
or movable (person, bicycle, car, motorcycle, airplane, bus,
                                                                   The number of overlapping keyframes has been set to 5 in
train, truck, boat, bird, cat, dog, horse, sheep, cow, elephant,
                                                                   our experiments, as a compromise between computational
bear, zebra and giraffe). We consider that, for most envi-
                                                                   cost and accuracy in the detection of dynamic objects.
ronments, the dynamic objects likely to appear are included
                                                                      We then compute the projection of each keypoint x from
within this list. If other classes were needed, the network,
                                                                   the previous keyframes into the current frame, obtaining the
trained on MS COCO [20], could be fine-tuned with new
                                                                   keypoints x0 , as well as their projected depth zproj , computed
training data.
   The output of the network, assuming that the input is an
RGB image of size m × n × 3, is a matrix of size m × n × l,
where l is the number of objects in the image. For each
output channel i ∈ l a binary mask is obtained. By combining
all the channels into one, we can obtain the segmentation of
all dynamic objects appearing in one image of the scene.
B. Low-Cost Tracking
   After the potentially dynamic content has been segmented,
the pose of the camera is tracked using the static part of the
image. Because the segment contours usually become high-
gradient areas, salient point features tend to appear. We do
not consider the features in such contour areas.
   The tracking implemented at this stage of the algorithm is      (a) Keypoint x0 belongs to a       (b) Keypoint x0 belongs to a
a simpler and therefore computationally lighter version of the     static object (z 0 = zproj ).      dynamic object (z 0  zproj ).
one in ORB-SLAM2 [1]. It projects the map features in the          Fig. 3: Keypoint x from the Key Frame (KF) is projected
image frame, searches for the correspondences in the static        into the Current Frame (CF) using its depth and camera
areas of the image, and minimizes the reprojection error to        pose, resulting in point x0 with depth z 0 . The projected depth
optimize the camera pose.                                          zproj is then computed. A pixel is labeled as dynamic if the
  1 https://github.com/matterport/Mask RCNN                        difference ∆z = zproj − z 0 is greater than a threshold τz .
         (a) Using Multi-view Geometry.               (b) Using Deep Learning.            (c) Using Geometry and Deep Learning.

Fig. 4: Detection and segmentation of dynamic objects using multi-view geometry (left), deep learning (middle), and a
combination of both geometric and learning methods (right). Notice that Fig. 4a cannot detect the person behind the desk,
Fig. 4b cannot segment the book carried by the person, and the combination of the two (Fig. 4c) is the best performing.

from the camera motion. Notice that the keypoints x come           main limitation though is that objects that are supposed
from the features extractor algorithm used in ORB-SLAM2.           to be static can be moved, and the method is not able to
For each keypoint, whose corresponding 3D point is X, we           identify them. This last case can be solved using multi-view
calculate the angle between the back-projections of x and          consistency tests.
x0 , i.e., their parallax angle α. If this angle is greater than      These two ways of facing the moving objects detection
30◦ , the point might be occluded, and will be ignored from        problem are illustrated in Fig. 4. In Fig. 4a we see that the
then on. We observed that, in the TUM dataset, for parallax        person in the back, which is potentially a dynamic object,
angles greater than 30◦ static objects were considered as          is not detected. There are two reasons for this. First, the
dynamic due to their viewpoint difference. We obtain the           difficulties that RGB-D cameras face when measuring the
depth of the remaining keypoints in the current frame z 0          depth of distant objects. And second, the fact that reliable
(directly from the depth measurement), taking into account         features lie on defined, and therefore nearby, parts of the
the reprojection error, and we compare them with zproj . If the    image. Albeit, this person is detected by the deep learning
difference ∆z = zproj − z 0 is over a threshold τz , keypoint      method (Fig. 4b). Apart from this, on one hand we see in
x0 is considered to belong to a dynamic object. This idea is       the Fig. 4a that not only is detected the person in the front
shown in Fig. 3. To set the threshold τz , we manually tagged      of the image, but also the book he is holding and the chair
the dynamic objects of 30 images within the TUM dataset,           he is sitting on. On the other hand, in the Fig. 4b the two
and evaluated both the precision and recall of our method          people are the only objects detected as dynamic, and also
for different thresholds τz . By maximizing the expression         their segmentation is less accurate. If only the deep learning
0.7×P recision+0.3×Recall, we concluded that τz = 0.4m             method is used, a floating book would be left in the images
is a reasonable choice.                                            and would incorrectly become part of the 3D map.
    Some of the keypoints labeled as dynamic lay on the               Because of the advantages and disadvantages of both
borders of moving objects, and might cause problems. To            methods, we consider that they are complementary and
avoid this, we use the information given by the depth images.      therefore their combined use is an effective way of achieving
If a keypoint is set as dynamic, but a patch around itself in      accurate tracking and mapping. In order to achieve this
the depth map has high variance, we change the label to            goal, if an object has been detected with both approaches,
static.                                                            the segmentation mask should be that of the geometrical
    So far, we know which keypoints belong to dynamic              method. If an object has only been detected by the learning
objects, and which ones do not. To classify all the pixels         based method, the segmentation mask should contain this
belonging to dynamic objects, we grow the region in the            information too. The final segmented image of the example
depth image around the dynamic pixels [21]. An example of          in the previous paragraph can be seen in the Fig. 4c. The
a RGB frame and its corresponding dynamic mask can be              segmented dynamic parts are removed from the current frame
seen in Fig. 4a.                                                   and from the map.
    The results of the CNN (Fig. 4b) can be combined with
those of this geometric method for full dynamic object             D. Tracking and Mapping
detection (Fig. 4c). We can find strengths and limitations
in both methods, hence the motivation for their combined              The input to this stage of the system contains the RGB and
use. For geometric approaches, the main problem is that            depth images, as well as their segmentation mask. We extract
initialization is not trivial because of its multi-view nature.    ORB features in the image segments classified as static. As
Learning methods and their impressive performance using a          the segment contours are high-gradient areas, the keypoints
single view, do not have such initialization problems. Their       falling in this intersection have to be removed.
                                     (a) RGB original images.                                      (b) Depth original image.

                                    (c) Inpainted RGB images.                                      (d) Inpainted depth image.
Fig. 5: Qualitative results of our approach. In Fig. 5a we show three RGB input frames, and in Fig. 5c we show the output
of our system, in which all dynamic objects have been detected and the background has been reconstructed. Figs. 5b and
5d show respectively the depth input and output, which has also been processed. Figure best viewed in electronic format.

E. Background Inpainting                                         we have compared our system against the original ORB-
   For every removed dynamic object, we aim at inpaint-          SLAM2 to quantify the improvement of our approach in
ing the occluded background with static information from         dynamic scenes. In this case, the results for some sequences
previous views, so that we can synthesize a realistic image      were not published and we have ourselves completed their
without moving content. We believe that such synthetic           evaluation. Mur and Tardós [1] propose to run each sequence
frames, containing the static structure of the environment,      five times and show median results, to account for the
are useful for applications such as virtual and augmented        non-deterministic nature of the system. We have run each
reality, and for relocation and camera tracking after the map    sequence ten times, as dynamic objects are prone to increase
is created.                                                      this non-deterministic effect.
   Since we know the position of the previous and current
                                                                 A. TUM Dataset
frames, we project into the dynamic segments of the current
frame the RGB and depth channels from a set of all the              The TUM RGB-D dataset [22] is composed of 39 se-
previous keyframes (the last 20 in our experiments). Some        quences recorded with a Microsoft Kinect sensor in different
gaps have no correspondences and are left blank: some areas      indoor scenes at full frame rate (30Hz). Both the RGB and
cannot be inpainted because their correspondent part of the      the depth images are available, together with the ground-truth
scene has not appeared so far in the keyframes, or, if it        trajectory, the latest recorded by a high-accuracy motion-
has appeared, it has no valid depth information. These gaps      capture system. In the sequences named sitting (s) there
cannot be reconstructed with geometrical methods and would       are two people sitting in front of a desk while speaking
need a more elaborate inpainting technique. Fig. 5 shows         and gesticulating, i.e., there is a low degree of motion. In
the resulting synthetic images for three input frames from       the sequences named walking (w), two people walk both in
different sequences of the TUM benchmark. Notice how the         the background and the foreground and sit down in front
dynamic content has been successfully segmented and re-          of the desk. This dataset is highly dynamic and therefore
moved. Also, most of the segmented parts have been properly      challenging for standard SLAM systems. For both types of
inpainted with information from the static background.           sequences sitting (s) and walking (w) there are four types
   Another application of these synthesized frames would be      of camera motions: (1) halfsphere (half): the camera moves
the following: if the frames dynamic areas are inpainted with    following the trajectory of a 1-meter diameter half sphere,
the static content, the system can work as a SLAM system         (2) xyz: the camera moves along the x-y-z axes, (3) rpy: the
under the staticity assumption using the inpainted images.       camera rotates over roll, pitch and yaw axes, and (4) static:
                                                                 the camera is kept static manually.
            IV. EXPERIMENTAL RESULTS                                We use the absolute trajectory RMSE as the error metric
   We have evaluated our system in the public datasets           for our experiments, as proposed by Sturm et al. [22].
TUM RGB-D and KITTI and compared to other state-of-                 The results of different variations of our system for six
the-art SLAM systems in dynamic environments, using when         sequences within this dataset are shown in Table I. Firstly,
possible results published in the original papers. Furthermore   DynaSLAM (N) is the system in which only Mask R-CNN
Sequence        DynaSLAM   DynaSLAM   DynaSLAM    DynaSLAM      pared against RGB-D ORB-SLAM2. Our method outper-
                   (N)        (G)       (N+G)     (N+G+BI)
                                                                forms ORB-SLAM2 in highly dynamic scenarios (walking),
w half sphere     0.025      0.035       0.025      0.029       reaching an error similar to that of the original RGB-D
w xyz             0.015      0.312       0.015      0.015
w rpy             0.040      0.251       0.035      0.136       ORB-SLAM2 system in static scenarios. In the case of low-
w static          0.009      0.009       0.006      0.007       dynamic scenes (sitting) the tracking results are slightly
s half sphere     0.017      0.018       0.017      0.025       worse because the tracked keypoints find themselves fur-
s xyz             0.014      0.009       0.015      0.013       ther than those belonging to dynamic objects. Albeit, Dy-
TABLE I: Absolute trajectory RMSE [m] for several variants      naSLAM’s map does not contain the dynamic objects that
of DynaSLAM (RGB-D).                                            appear along the sequence. Fig. 7 shows an example of
                                                                the estimated trajectories of DynaSLAM and ORB-SLAM2,
                                                                compared to the ground-truth.
segments out the a priori dynamic objects. Secondly, in
DynaSLAM (G) the dynamic objects have been only de-             Sequence         ORB-SLAM2       DynaSLAM (N+G) (RGB-D)
                                                                                 (RGB-D) [1]
tected with the multi-view geometry method based on depth                          median      median         min            max
changes. Thirdly, DynaSLAM (N+G) stands for the system
                                                                w half sphere        0.351     0.025          0.024       0.031
in which the dynamic objects have been detected combining       w xyz                0.459     0.015          0.014       0.016
both the geometrical and deep learning approaches. Finally,     w rpy                0.662     0.035          0.032       0.038
we have considered interesting to analyze the system shown      w static             0.090     0.006          0.006       0.008
in Fig. 6. In this case (N+G+BI), the background inpainting     s half sphere        0.020     0.017          0.016       0.020
                                                                s xyz                0.009     0.015          0.013       0.015
stage (BI) is done before the tracking and mapping. The
motivation for this experiment is that, if the dynamic areas    TABLE II: Comparison of the RMSE of ATE [m] of
are inpainted with the static content, the system can work      DynaSLAM against ORB-SLAM2 for RGB-D cameras. To
as a SLAM system under the staticity assumption using           account for the non-deterministic nature of the system, we
the inpainted images. In this proposal, the ORB features        show the median, minimum and maximum error of ten runs.
extractor algorithm works both in the real and reconstructed
areas of the frames, finding matches with the keypoints of         Table III shows a comparison between our system and
the previously processed keyframes.                             several state-of-the-art RGB-D SLAM systems designed for
   According to Table I, the system (N+G) that uses learning    dynamic environments. In account for the effectiveness of
and geometry is the most accurate one in most sequences.        our and the state-of-the-art approaches for motion detec-
The improvement over (N) comes from the segmentation of         tion (independently of the utilized SLAM system), we also
movable objects and refinement of the dynamic segments.         show the respective improvement values against the original
The system (G) has higher error because it needs motion         SLAM system used in every case. DynaSLAM significantly
and its segmentation is only accurate after a small delay,      outperforms all of them in all sequences (both high and
during which the dynamic content introduces some error in       low dynamic ones). The error is, in general, around 1-2
the estimation.                                                 cm, similar to that of the state of the art in static scenes.
   Adding the background inpainting stage (BI) before the       Our motion detection approach also outperforms the other
localization of the camera (Fig. 6) usually leads to less       methods.
accuracy in the tracking. The reason is that the background        ORB-SLAM, the monocular version of ORB-SLAM2,
reconstruction is strongly correlated with the camera poses.    is generally more accurate than the RGB-D one in dy-
Hence, for sequences with purely rotational motion (rpy,        namic scenes, due to their different initialization algorithms.
halfsphere), the estimated camera poses have a greater error
and lead to a non-accurate background reconstruction. The
background inpainting stage (BI) should be done therefore                                                     ORB-SLAM2
once the tracking stage is finished (Fig. 2). The main                                                         DynaSLAM
                                                                             −2.5
accomplishment of the background reconstruction is seen in                                                    Ground-truth
the synthesis of the static images (Fig. 5) for applications
                                                                      y[m]

such as virtual reality or cinematography. The DynaSLAM
results shown from now on are from the best variant, that is,                   −3
(N+G).
   Table II shows our results on the same sequences, com-
                                                                                        −1.5    −1          −0.5      0
                                                                                                     x[m]

                                                                Fig. 7:   Ground truth and trajectories estimated by
                                                                DynaSLAM and ORB-SLAM2 in the TUM sequence
Fig. 6: Block diagram of RGB-D DynaSLAM (N+G+BI).               f r3/walking xyz.
Sequence   Depth Edge      Motion Segmentation DSLAM [14]          Motion Removal DVO-SLAM [16]                     DynaSLAM (N+G) (RGB-D)
           SLAM [12]
                        w/o Motion    w/ Motion    Improvement w/o Motion        w/ Motion        Improvement w/o Motion    w/ Motion             Improvement
                         Detection    Detection      w/ MD      Detection        Detection          w/ MD      Detection    Detection               w/ MD
              [m]           [m]          [m]          [%]          [m]              [m]              [%]        [1] [m]        [m]                   [%]
w half       0.049         0.116        0.055       52.59%           0.529         0.125           76.32%        0.351            0.025            92.88%
w xyz        0.060         0.202        0.040       80.20%           0.597         0.093           84.38%        0.459            0.015            96.73%
w rpy        0.179         0.515        0.076       85.24%           0.730         0.133           81.75%        0.662            0.035            94.71%
w stat       0.026         0.470        0.024       94.89%           0.212         0.066           69.06%        0.090            0.006            93.33%
s half       0.043           -            -            -             0.062         0.047           23.70%        0.020            0.017            15.00%
s xyz        0.040           -            -            -             0.051         0.048           4.55%         0.009            0.015               X
TABLE III: Absolute trajectory RMSE [m] of DynaSLAM against state-of-the-art RGB-D SLAM systems in dynamic
scenes. To evaluate the effectiveness of the specific module addressing dynamic content, we report the improvement with
respect to the original SLAM systems (w/o Motion Detection). Our results are estimated using Mask R-CNN and multi-view
geometry.

RGB-D ORB-SLAM2 is initialized and starts the track-                         Sequence      ORB-SLAM2 (Stereo) [1]            DynaSLAM (Stereo)
ing from the very first frame, and hence dynamic objects                                   RPE         RRE       ATE       RPE         RRE            ATE
can introduce errors. ORB-SLAM delays the initialization                                   [%]       [◦ /100m]   [m]       [%]       [◦ /100m]        [m]
until there is parallax and consensus using the staticity                    KITTI 00      0.70        0.25       1.3      0.74           0.26         1.4
assumption. Hence, it does not track the camera for the full                 KITTI 01      1.39        0.21      10.4      1.57           0.22         9.4
                                                                             KITTI 02      0.76        0.23       5.7      0.80           0.24         6.7
sequence, sometimes missing a substantial part of it, or even                KITTI 03      0.71        0.18      0.6       0.69           0.18         0.6
not initializing.                                                            KITTI 04      0.48        0.13      0.2       0.45           0.09         0.2
   Table IV shows the tracking results and percentage of                     KITTI 05      0.40        0.16      0.8       0.40           0.16         0.8
                                                                             KITTI 06      0.51        0.15       0.8      0.50           0.17         0.8
the tracked trajectory for ORB-SLAM and DynaSLAM                             KITTI 07      0.50        0.28       0.5      0.52           0.29         0.5
(monocular) in the TUM dataset. The initialization in Dy-                    KITTI 08      1.05        0.32      3.6       1.05           0.32         3.5
naSLAM is always quicker than that of ORB-SLAM. In                           KITTI 09      0.87        0.27       3.2      0.93           0.29         1.6
                                                                             KITTI 10      0.60        0.27       1.0      0.67           0.32         1.2
fact, in highly dynamic sequences, ORB-SLAM initialization
only occurs when the moving objects disappear from the                       TABLE V: Comparison of the RMSE of the ATE [m], the
scene. In conclusion, although the accuracy of DynaSLAM                      average of the RPE [%] and the RRE [◦ /100m] of Dy-
is slightly lower, it succeeds in bootstrapping the system with              naSLAM against ORB-SLAM2 system for stereo cameras.
dynamic content and producing a map without such content
(see Fig. 1), to be re-used for long-term applications. The                  Sequence             ORB-SLAM [1]             DynaSLAM (Monocular)
reason why DynaSLAM is slightly less accurate is that the                    KITTI 00                 5.33                                 7.55
estimated trajectory is longer, and there is therefore room for              KITTI 02                 21.28                               26.29
accumulating errors.                                                         KITTI 03                 1.51                                 1.81
                                                                             KITTI 04                  1.62                                0.97
                                                                             KITTI 05                  4.85                                4.60
Sequence                         ORB-SLAM            DynaSLAM                KITTI 06                 12.34                               14.74
                                    [1]              (Monocular)             KITTI 07                 2.26                                 2.36
                            ATE [m]    % Traj     ATE [m]    % Traj          KITTI 08                 46.68                               40.28
                                                                             KITTI 09                  6.62                                3.32
f r3/walking half sphere      0.017     87.16      0.021     97.84           KITTI 10                  8.80                                6.78
f r3/walking xyz              0.012     57.63      0.014     87.37
                                                                             TABLE VI: Absolute trajectory RMSE [m] for ORB-SLAM
f r2/desk with person         0.006     95.30      0.008      97.07
f r3/sitting xyz              0.007     91.44      0.013     100.00          and DynaSLAM (monocular).
TABLE IV: Absolute trajectory RMSE [m] and percentage
of successfully tracked trajectory for both ORB-SLAM and
DynaSLAM (monocular).                                                           Note that the results are similar in both the monocular
                                                                             and stereo cases, but the former is more sensitive to dynamic
                                                                             objects and therefore to the additions in DynaSLAM. In some
B. KITTI Dataset                                                             sequences the accuracy of the tracking is improved when
   The KITTI Dataset [23] contains stereo sequences                          not using features belonging to a priori dynamic objects,
recorded from a car in urban and highway environments.                       i.e., cars, bicycles, etc. An example of this would be the
Table V shows our results in the eleven training sequences,                  sequences KITTI 01 and KITTI 04, in which all vehicles
compared against stereo ORB-SLAM2. We use two different                      that appear are moving. In the sequences in which most
metrics, the absolute trajectory RMSE proposed in [22], and                  of the recorded cars and vehicles are parked (hence static),
the average relative translation and rotation errors, proposed               the absolute trajectory RMSE is usually bigger since the
in [23]. Table VI shows the results in the same sequences                    keypoints used for tracking are more distant and usually
for the monocular variants of ORB-SLAM and DynaSLAM.                         belong to low-texture areas (KITTI 00, KITTI 02, KITTI
06). However, the loop closure and relocalization algorithms       cases in which dynamic objects represent an important part
work more robustly since the resulting map only contains           of the scene. However, our estimated map only contains
structural objects, i.e., the map can be re-used and work in       structural objects and can therefore be re-used in long-term
long-term applications.                                            applications.
   As future work, it is interesting to make a distinction            Future extensions of this work might include, among oth-
between those movable and moving objects, by using only            ers, real-time performance, an RGB-based motion detector,
RGB information. If a car is detected by the CNN (movable)         or a more realistic appearance of the synthesized RGB frames
but is not currently moving, its corresponding keypoints           by using a more elaborate inpainting technique, e.g., the one
should be used for the local tracking, but should not be in        used by Pathak et al. [24] by the use of GANs.
the map.
                                                                                                R EFERENCES
C. Timing Analysis                                                  [1] R. Mur-Artal and J. D. Tardós, “ORB-SLAM2: An open-source slam
                                                                        system for monocular, stereo, and RGB-D cameras,” IEEE T-RO, 2017.
   To complete the evaluation of our proposal, Table VII            [2] G. Klein and D. Murray, “Parallel tracking and mapping for small AR
shows the average computational time for its different stages.          workspaces,” in ISMAR, pp. 225–234, 2007.
Note that DynaSLAM is not optimized for real-time opera-            [3] R. Mur-Artal, J. M. M. Montiel, and J. D. Tardos, “ORB-SLAM: a
                                                                        versatile and accurate monocular SLAM system,” IEEE T-RO, 2015.
tion. However, its capability for creating life-long maps of the    [4] J. Stühmer, S. Gumhold, and D. Cremers, “Real-time dense geometry
static scene content are also relevant for running on offline           from a handheld camera,” in Joint Pattern Recognition Symposium,
mode.                                                                   2010.
                                                                    [5] R. A. Newcombe, S. J. Lovegrove, and A. J. Davison, “DTAM: Dense
                                                                        tracking and mapping in real-time,” in ICCV, IEEE, 2011.
Sequence          Low-Cost       Multi-view        Background       [6] G. Graber, T. Pock, and H. Bischof, “Online 3D reconstruction using
                Tracking [ms]   Geometry [ms]    Inpainting [ms]        convex optimization,” in ICCV Workshops, IEEE, 2011.
w half sphere        1.69           333.68           208.09         [7] J. Engel, T. Schöps, and D. Cremers, “LSD-SLAM: Large-scale direct
w rpy                1.59           235.98           183.56             monocular SLAM,” in ECCV, pp. 834–849, Springer, 2014.
                                                                    [8] J. Engel, V. Koltun, and D. Cremers, “Direct sparse odometry,” IEEE
TABLE VII: DynaSLAM average computational time [ms].                    Transactions on Pattern Analysis and Machine Intelligence, 2017.
                                                                    [9] W. Tan, H. Liu, Z. Dong, G. Zhang, and H. Bao, “Robust monocular
                                                                        SLAM in dynamic environments,” in ISMAR, pp. 209–218, 2013.
   Mur et al. show real-time results for and ORB-SLAM2             [10] S. Wangsiripitak and D. W. Murray, “Avoiding moving outliers in
                                                                        visual SLAM by tracking moving objects,” in ICRA, pp. 375–380,
[1]. He et al. [19] report that Mask R-CNN runs at 195 ms               IEEE, 2009.
per image on a Nvidia Tesla M40 GPU.                               [11] L. Riazuelo, L. Montano, and J. M. M. Montiel, “Semantic visual
   The addition of the multi-view geometry stage is an addi-            SLAM in populated environments,” ECMR, 2017.
                                                                   [12] S. Li and D. Lee, “RGB-D SLAM in Dynamic Environments Using
tional slowdown, due mainly to the region growth algorithm.             Static Point Weighting,” IEEE RA-L, vol. 2, no. 4, pp. 2263–2270,
The background inpainting also introduces a delay, which is             2017.
another reason why it should be done after the tracking and        [13] P. F. Alcantarilla, J. J. Yebes, J. Almazán, and L. M. Bergasa,
                                                                        “On combining visual SLAM and dense scene flow to increase the
mapping stage, as it has been shown in Fig. 2.                          robustness of localization and mapping in dynamic environments,” in
                                                                        ICRA, 2012.
                    V. CONCLUSIONS                                 [14] Y. Wang and S. Huang, “Motion segmentation based robust RGB-D
                                                                        SLAM,” in WCICA, pp. 3122–3127, IEEE, 2014.
   We have presented a visual SLAM system that, building           [15] D.-H. Kim and J.-H. Kim, “Effective Background Model-Based RGB-
on ORB-SLAM, adds a motion segmentation approach that                   D Dense Visual Odometry in a Dynamic Environment,” IEEE T-RO,
makes it robust in dynamic environments for monocular,                  2016.
                                                                   [16] Y. Sun, M. Liu, and M. Q.-H. Meng, “Improving RGB-D SLAM in
stereo and RGB-D cameras. Our system accurately tracks                  dynamic environments: A motion removal approach,” RAS, 2017.
the camera and creates a static and therefore reusable map         [17] A. Concha and J. Civera, “DPPTAM: Dense piecewise planar tracking
of the scene. In the RGB-D case, DynaSLAM is capable of                 and mapping from a monocular sequence,” in IEEE/RSJ IROS, 2015.
                                                                   [18] R. Ambrus, J. Folkesson, and P. Jensfelt, “Unsupervised object
obtaining the synthetic RGB frames with no dynamic content              segmentation through change detection in a long term autonomy
and with the occluded background inpainted, as well as                  scenario,” in Humanoid Robots (Humanoids), IEEE, 2016.
their corresponding synthesized depth frames, which might          [19] K. He, G. Gkioxari, P. Dollár, and R. Girshick, “Mask R-CNN,” arXiv
                                                                        preprint arXiv:1703.06870, 2017.
be together very useful for virtual reality applications. We       [20] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan,
include a video showing the potential of DynaSLAM 2 .                   P. Dollár, and C. L. Zitnick, “Microsoft coco: Common objects in
   The comparison against the state of the art shows that               context,” in ECCV, 2014.
                                                                   [21] N. L. Gerlach, G. J. Meijer, D.-J. Kroon, E. M. Bronkhorst, S. J.
DynaSLAM achieves in most cases the highest accuracy.                   Bergé, and T. J. J. Maal, “Evaluation of the potential of automatic
   In the TUM Dynamic Objects dataset, DynaSLAM is                      segmentation of the mandibular canal,” BJOMS, 2014.
currently the best RGB-D SLAM solution. In the monoc-              [22] J. Sturm, N. Engelhard, F. Endres, W. Burgard, and D. Cremers, “A
                                                                        benchmark for the evaluation of RGB-D SLAM systems,” in IROS,
ular case, our accuracy is similar to that of ORB-SLAM,                 2012.
obtaining however a static map of the scene with an earlier        [23] A. Geiger, P. Lenz, C. Stiller, and R. Urtasun, “Vision meets robotics:
initialization.                                                         The KITTI dataset,” IJRR, vol. 32, no. 11, pp. 1231–1237, 2013.
                                                                   [24] D. Pathak, P. Krahenbuhl, J. Donahue, T. Darrell, and A. A. Efros,
   In the KITTI dataset DynaSLAM is slightly less accurate              “Context encoders: Feature learning by inpainting,” in CVPR, 2016.
than monocular and stereo ORB-SLAM, except for those
  2 https://youtu.be/EabI goFmQs
