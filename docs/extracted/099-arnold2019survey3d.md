---
source_id: 099
bibtex_key: arnold2019survey3d
title: A Survey on 3D Object Detection Methods for Autonomous Driving Applications
year: 2019
domain_theme: Deteksi 3D
verified_pdf: 99_Survei Deteksi 3D (Arnold dkk.).pdf
char_count: 117890
---

Manuscript version: Author’s Accepted Manuscript
The version presented in WRAP is the author’s accepted manuscript and may differ from the
published version or Version of Record.

Persistent WRAP URL:
http://wrap.warwick.ac.uk/114314

How to cite:
Please refer to published version for the most recent bibliographic citation information.
If a published version is known of, the repository item page linked to above, will contain
details on accessing it.

Copyright and reuse:
The Warwick Research Archive Portal (WRAP) makes this work by researchers of the
University of Warwick available open access under the following conditions.

Copyright © and all moral rights to the version of the paper presented here belong to the
individual author(s) and/or other copyright owners. To the extent reasonable and
practicable the material made available in WRAP has been checked for eligibility before
being made available.

Copies of full items can be used for personal research or study, educational, or not-for-profit
purposes without prior permission or charge. Provided that the authors, title and full
bibliographic details are credited, a hyperlink and/or URL is given for the original metadata
page and the content is not changed in any way.

Publisher’s statement:
Please refer to the repository item page, publisher’s statement section, for further
information.

For more information, please contact the WRAP Team at: wrap@warwick.ac.uk.

                               warwick.ac.uk/lib-publications
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                     1

       A Survey on 3D Object Detection Methods for
            Autonomous Driving Applications
     Eduardo Arnold, Omar Y. Al-Jarrah, Mehrdad Dianati, Saber Fallah, David Oxtoby and Alex Mouzakitis

   Abstract—An Autonomous Vehicle (AV) requires an accurate                 the object detection task is of fundamental importance, as
perception of its surrounding environment to operate reliably.              failing to identify and recognize road agents might lead to
The perception system of an AV, which normally employs ma-                  safety-related incidents. For instance, failing in detecting a
chine learning (e.g., deep learning), transforms sensory data into
semantic information that enables autonomous driving. Object                leading vehicle can result in traffic accidents, threatening
detection is a fundamental function of this perception system               human lives [4].
that has been tackled by several works, most of which use                      One factor for failure in the perception system arises from
2D detection methods. However, 2D methods do not provide                    sensors limitations and environment variations such as lighting
depth information, which is required for driving tasks, such as             and weather conditions. Other challenges include generalisa-
path planning, collision avoidance, etc. Alternatively, 3D object
detection methods introduce a third dimension that reveals more             tion across driving domains such as motorways, rural and
detailed object’s size and location information. Nonetheless, the           urban areas. While motorways have well-structured lanes with
detection accuracy of such methods needs to be improved. To                 vehicles following a standard orientation, urban areas exhibit
the best of our knowledge this is the first survey on 3D object             vehicles parked at no particular orientation, more diverse
detection methods used for autonomous driving applications. This            classes such as pedestrians, cyclists, and background clutter
paper presents an overview of 3D object detection methods and
prevalently used sensors and datasets in AVs. It then discusses             such as bollards and bins. Another factor is occlusion, when
and categorizes recent works based on sensors modalities into               one object blocks the view of another, resulting in partial or
monocular, point cloud-based and fusion methods. We then sum-               complete invisibility of the object. Not only objects’ sizes can
marize the results of the surveyed works and identify research              be very dissimilar, e.g., comparing a truck with a dog, but
gaps and future research directions.                                        objects can be very close or far away from the subject AV.
   Index Terms—Machine learning, deep learning, computer                    The object’s scale dramatically affects the sensors’ readings,
vision, object detection, autonomous vehicles, intelligent vehicles.        resulting in very dissimilar representations for the objects of
                                                                            the same class.
                                                                               Despite the aforementioned challenges, the performance
                         I. I NTRODUCTION                                   of 2D object detection methods for autonomous driving has
                                                                            greatly improved, achieving an Average Precision (AP) of

B     ETWEEN the years 2016 and 2017, the number of
      road casualties in the U.K. was approximately 174,510
, of which 27,010 were killed or severely injured casualties
                                                                            more than 90% on the well established “KITTI” object de-
                                                                            tection benchmark [5]. While 2D methods detect objects on
                                                                            the image plane, their 3D counterpart introduce a third dimen-
[1]. As reported by the U.S. Department of Transportation,                  sion to the localization and size regression, revealing depth
more than 90% of car crashes in the U.S. are attributed to                  information in world coordinates. However, the performance
drivers’ errors [2]. The adoption of connected and autonomous               gap between 2D and 3D methods in the context of AVs is still
vehicles is expected to improve driving safety, traffic flow and            significant [6]. Further research should be conducted to fill the
efficiency [3]. However, for an autonomous vehicle to operate               performance gap of 3D methods, as 3D scene understanding
safely, an accurate environment perception and awareness is                 is crucial for driving tasks. A comparison between 2D and 3D
fundamental.                                                                detection methods is presented in Table I.
   The perception system of an Autonomous Vehicle (AV)                         In previous work Ranft & Stiller [7] reviewed machine
transforms sensory data into semantic information, such as                  vision methods for different tasks of intelligent vehicles,
identification and recognition of road agents (e.g., vehicles,              including localization and mapping, driving scene understand-
pedestrians, cyclists, etc.) positions, velocity and class; lane            ing and object classification. In [8], on-road object detection
marking; drivable areas and traffic signs information. Notably,             was briefly reviewed among other perception functions, how-
                                                                            ever, authors predominantly considered 2D object detection.
   This work was supported by Jaguar Land Rover and the U.K.-EPSRC as
part of the jointly funded Towards Autonomy: Smart and Connected Control    Mukhtar et al. [9] reviewed 2D vehicle detection methods
(TASCC) Programme under Grant EP/N01300X/1.                                 for Driver Assistance Systems with focus on motion and
   E. Arnold, O. Y. Al-Jarrah and M. Dianati are with the Warwick Manu-     appearance-based approaches using a traditional pipeline. A
facturing Group, University of Warwick, Coventry CV4 7AL, U.K. (e-mail:
{e.arnold, omar.al-jarrah, m.dianati}@warwick.ac.uk).                       traditional pipeline consists of segmentation (e.g., graph-based
   S. Fallah is with the Centre for Automotive Engineering, University of   segmentation [10] and voxel-based clustering methods [11]),
Surrey, Guildford GU2 7XH, U.K. (e-mail: s.fallah@surrey.ac.uk).            hand-engineered feature extraction (e.g., voxel’s probabilistic
   D. Oxtoby and A. Mouzakitis are with Jaguar Land Rover Ltd., Coventry
CV4 7HS, U.K. (e-mail: doxtoby@jaguarlandrover.com)                         features [11]) and classification stages (e.g., a mixture of bag-
                                                                            of-words classifiers [12]).
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                                   2

                            TABLE I
                 2D VERSUS 3D O BJECT DETECTION

              Advantages                     Disadvantages
2D Object     Well established datasets      Limited information: lack
Detection     and detection architectures.   of object’s pose, occlusion
              Usually RGB only input         and 3D position informa-
              can achieve accurate re-       tion.
              sults in the image plane.
3D Object     3D bounding box provides       Requires depth estimation
Detection     object size and position in    for precise localization.
              world coordinates. These       Extra           dimension
              detailed information allows    regression       increases
              better environment under-      model complexity. Scarse
              standing.                      3D labelled datasets.
                                                                           Fig. 1. IMX390 sensor sample image on a tunnel exit. The image on the left
                                                                           was taken with both LED flickering mitigation and High-Dynamic-Ranging
                                                                           (HDR) capability enabled. The top right image shows HDR functionality
   Unlike traditional pipelines, which optimize each stage                 without LED flickering mitigation – note that the traffic sign velocity indicator
individually, end-to-end pipelines optimize the overall pipeline           does not appear. The bottom right image shows the image without any of
performance. An end-to-end detection method leverages learn-               the functionalities enabled, clearly showing the sensor capabilities. Image
                                                                           obtained from the Sony website [21].
ing algorithms to propose regions of interest and extract fea-
tures from the data. The shift towards representation learning
and end-to-end detection was possible by using deep learning               these two categories are described in higher detail. A more
methods, such as deep convolutional networks, which showed                 comprehensive report on current sensors for AV applications
a significant performance gain in different applications [13],             can be found in [15], [16].
[14]. In this paper we focus on end-to-end pipelines and
learning approaches, since these have become the state-of-
the-art for 3D object detection and have rapidly progressed                A. Cameras
in recent years.                                                              Monocular cameras provide detailed information in the form
   This paper presents an overview of 3D object detection                  of pixel intensities, which at a bigger scale reveal shape and
methods and prevalently used sensors and datasets in AVs. We               texture properties. The shape and texture information can be
discuss and categorise existing works based on sensor modality             used to detect lane geometry, traffic signs [17] and the object
into: monocular-based methods, point cloud-based methods                   class [7].
and fusion methods. Finally, we discuss current research
                                                                              One disadvantage of monocular cameras is the lack of depth
challenges and future research directions. The contributions
                                                                           information, which is required for accurate object size and
of this paper are as follows:
                                                                           position estimation. A stereo camera setup can be used to
   • summarizing datasets and simulation tools used to eval-
                                                                           recover depth channels. Such configuration uses matching al-
      uate the performance of detection models                             gorithms to find correspondences in both images and calculate
   • providing a summary of 3D object detection advance-
                                                                           the depth of each point relative to the camera, demanding more
      ments for autonomous driving vehicles                                processing power [18].
   • comparing 3D object detection methods performances on
                                                                              Other camera modalities that offer depth estimation are
      a baseline benchmark                                                 Time-of-Flight (ToF) cameras where depth is inferred by
   • identifying research gaps and future research directions.
                                                                           measuring the delay between emitting and receiving modulated
   This paper is structured as follows. Section II describes               infrared pulses [19]. This technology has been applied for ve-
commonly used sensors for perception tasks in autonomous                   hicle safety applications [20], but despite the lower integration
vehicles. Section III lists well-referenced datasets used for ob-          price and computational complexity has low resolution when
ject detection in AVs. We review 3D object detection methods               compared to stereo cameras.
in Section IV. Section V compares the performance of existing                 Camera sensors are susceptible to light and weather con-
methods on a benchmark dataset and highlights research                     ditions. Examples range from low luminosity at night-time to
challenges and potential research opportunities. Section VI                extreme brightness disparity when entering or leaving tunnels.
provides a brief summary and concludes this work.                          The recent use of LEDs on traffic signs and vehicles brake
                                                                           lights creates a flickering problem. It happens as the camera
                           II. S ENSORS                                    sensor cannot reliably capture the emitted light due to the
   Although humans primarily use their visual and auditory                 LEDs’ switching behaviour. Sony has recently announced a
systems while driving, artificial perception methods rely on               new camera technology designed to mitigate flickering effects
multiple modalities to overcome shortcomings of individual                 and enhance colors dynamic range [21], as illustrated in Figure
sensors. There are a wide range of sensors used by autonomous              1. Additionally, image degradation can occur due to rainy or
vehicles: passive ones, such as monocular and stereo cameras,              snowy weather. Chen et al. [22] propose to mitigate this using
and active ones, including lidar, radar and sonar. Since most              a de-raining filter based on a multi-scale pyramid structure and
research on perception for AVs focus on cameras and lidars,                conditional generative adversarial networks.
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                                 3

                                                                                                            TABLE II
                                                                                                      S ENSORS C OMPARISON

                                                                                           Advantages                     Disadvantages
                                                                             Monocular     Readily available and inex-    Prone to adverse light
                                                                             Camera        pensive. Multiple specifica-   and weather conditions.
                                                                                           tions available.               No depth information
                                                                                                                          provided.
                                                                             Stereo        Higher point density when      Depth       estimation   is
                                                                             Camera        compared to lidar. Provides    computationally expensive.
                                                                                           dense depth map.               Poor performance with
                                                                                                                          textureless     regions or
                                                                                                                          during night-time. Limited
                                                                                                                          Field-of-View (FoV).
                                                                             Lidar         360 degrees FoV, precise       Raw point cloud does not
                                                                                           distance    measurements.      provide texture informa-
                                                                                           Not affected by light          tion. Expensive and large
                                                                                           conditions.                    equipment.
                                                                             Solid-State   No moving mechanical           Limited FoV when com-
                                                                             lidar         parts, compact size. Large     pared to mechanical scan-
                                                                                           scale production should        ning lidar. Still under de-
                                                                                           reduce final cost.             velopment.
Fig. 2. The two images show the point clouds obtained by two lidar sensors
on the same scene. The top image was captured using the newer VLS-128
model while the bottom one used the standard HDL-64 model. Image obtained
from [24].
                                                                             However, having spatial targets makes this method laborious
                                                                             for on-site calibration. As an alternative, Ishikawa et al. [27]
                                                                             devised a calibration method without spatial targets using
B. Lidar                                                                     odometry estimation of the sensors w.r.t. the environment to
   Lidar sensors emit laser beams and measure the time                       iteratively calibrate them.
between emitting and detecting the pulse back. The timing
information determines the distance of obstacles in any given                C. Discussion
direction. The sensor readings result in a set of 3D points,
                                                                                Monocular cameras are inexpensive sensors, but they lack
also called Point Cloud (PCL), and corresponding reflectance
                                                                             depth information which is required for accurate 3D object
values representing the strength of the received pulses. Unlike
                                                                             detection. Depth cameras can be used for depth recovery, but
images, point clouds are sparse: the samples are not uniformly
                                                                             fail in adverse lighting conditions and textureless scenes and
distributed in space. As active sensors, external illumination is
                                                                             ToF camera sensors have limited resolution. In contrast, lidar
not required and thus more reliable detection can be achieved
                                                                             sensors can be used for accurate depth estimation during night-
considering adverse weather and extreme lighting conditions
                                                                             time, but is prone to noise during adverse weather, such as
(e.g., night-time or sun glare scenarios).
                                                                             snow and fog, and cannot provide texture information. We
   Standard lidar models, such as the HDL-64L [23], use an
                                                                             summarize the advantages and disadvantages of each sensor
array of rotating laser beams to obtain 3D point clouds in
                                                                             modality in Table II.
360 degrees and up to 120m radius. This sensor can output
120 thousand points per frame, which amounts to 1,200
million points per second on a 10 Hz frame rate. Velodyne                                                III. DATASETS
recently announced the VLS-128 model [24] featuring 128                         As learning approaches become widely used the need of
laser beams, higher angular resolution and 300m radius range.                training data also increases. The availability of large scale
Figure 2 shows a comparison between the point densities of                   image datasets such as ImageNet [28] allowed fast develop-
the two models. The announcement suggests that the increased                 ment and evolution of image classification and object detection
point density might enhance the recall of methods using this                 models. The same phenomena occurs in the driving scenario,
modality but challenges real time processing performance. The                where more data means broader scenario coverage. In partic-
primary challenge to the widespread use of lidar is its price:               ular, tasks such as object detection and semantic segmentation
a single sensor can cost more than $70,000. Nevertheless, this               require finely labelled data. In this section we present common
price is expected to decrease in the following years with the                datasets for driving tasks, specifically to object detection.
introduction of solid state lidar technology [25] and large scale               One of the most used datasets in the driving context
production.                                                                  is KITTI [29], which provides stereo color images, lidar
   Some methods rely on both lidar and camera modalities.                    point clouds and GPS coordinates, all synchronized in time.
Before fusing these modalities it is required to calibrate the               Recorded scenes range from well-structured highways, com-
sensors to obtain a single spatial frame of reference. In [26] the           plex urban areas and narrow countryside roads. The dataset
authors propose to use polygonal planar boards as targets that               can be used for multiple tasks: stereo matching, visual odom-
can be detected by both modalities to generate accurate 3D-                  etry, 3D tracking and 3D object detection. In particular, the
2D correspondences and obtain a more accurate calibration.                   specific object detection dataset contains 7,481 training and
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                        4

7,518 test frames, which are provided with sensor calibration
information and annotated 3D boxes around objects of interest.
The annotations are categorized in “easy, moderate and hard”
cases, according to object size, occlusion and truncation levels.
   Despite widely adopted, this dataset has several limitations.
Notably, limited sensor configuration and lighting conditions:
all the measurements were obtained by the same set of sensors
during daytime and mostly under sunny conditions. In addition
the classes frequency is highly unbalanced [30] – 75% car, 4%
cyclist and 15% pedestrians. Furthermore, most scene objects
follow a predominant orientation, facing the ego-vehicle. The
lack of variety challenges the evaluation of current methods in
more general scenarios, reducing their reliability for real-world
applications.
   Considering these limitations and the expensive process of
obtaining and labelling a dataset, Gaidon et al. proposed the
Virtual KITTI dataset [31]. The authors manually recreated
the KITTI environment using a game-engine, 3D model assets          Fig. 3. Frames from 5 real KITTI videos (first column) and respective virtual
                                                                    clones on Virtual KITTI (second column). Image from [31].
and the original video sequences, see Figure 3. Different
lighting and weather conditions, vehicles colors and models,
etc., were adjusted to automatically generate labelled data.        A. Monocular image based methods
They provide approximately 17,000 frames consisting of the
photo-realistic images, a depth frame, and pixel-level semantic        Although 2D object detection is a largely addressed task that
segmentation ground-truth. Additionally, the authors assessed       has been successfully tackled in several datasets [37], [38], the
the transferability across real and virtual domains for a track-    KITTI dataset offers particular settings that pose challenges
ing application (which requires detection). They evaluated a        to object detection. These settings, common to most driving
tracker trained on real images and tested on virtual ones.          environments, include small, occluded or truncated objects and
The results revealed that the gap in performance is minimal,        highly saturated areas or shadows. Furthermore, 2D detection
showing the equivalence of the datasets. They also concluded        on the image plane is not enough for reliable driving systems:
that the best performance was obtained when training on the         more accurate 3D space localization and size estimation is
virtual data and fine-tuning on real data.                          required for such application. This section focuses on methods
                                                                    that are able to estimate 3D bounding boxes based only on
   Simulation tools can be used to both generate training data
                                                                    monocular images. Since no depth information is available,
on specific conditions or to train end-to-end driving systems
                                                                    most approaches first detect 2D candidates before predicting
[32], [33]. Using virtual data during training can enhance the
                                                                    a 3D bounding box that contains the object using neural
performance of detection models on real environments. This
                                                                    networks [39], geometrical constraints [40] or 3D model
data can be obtained through game-engines [34] or simulated
                                                                    matching [41], [42].
environments [31]. CARLA [35] is an open-source simulation
                                                                       Chen et al. propose Mono3D [39], which leverages a
tool for autonomous driving that allows flexible environmental
                                                                    simple region proposal algorithm using context, semantics,
setup and sensor configuration. It provides several 3D models
                                                                    hand-engineered shape features and location priors. For any
for pedestrians, cars and includes two virtual towns. Envi-
                                                                    given proposal, these features can be efficiently computed
ronmental conditions, such as weather and lighting, can be
                                                                    and scored by an energy model. Proposals are generated by
adjusted to generate unseen scenarios. The virtual sensor suite
                                                                    exhaustive search on 3D space and filtered with Non-Maxima
includes RGB and depth cameras with ground-truth segmenta-
                                                                    Suppression (NMS). The proposals are further scored by a
tion frames and a ray-casting lidar model. Another simulation
                                                                    Fast R-CNN [37] model that regresses 3D bounding boxes.
tool, Sim4CV [36] allows easy environment customization and
                                                                    The work builds upon the authors’ previous work 3DOP
simultaneous multi-view rendering of the driving scenes, while
                                                                    [43], which considers depth images to generate proposals in a
providing ground-truth bounding boxes for object detection
                                                                    similar framework. Despite using only monocular images, the
purposes.
                                                                    Mono3D model slightly improves the performance obtained
                                                                    by [43], which uses depth images. Pham et al. [44] extends
                                                                    the 3DOP proposal generation considering class-independent
          IV. 3D O BJECT D ETECTION M ETHODS                        proposals, then re-ranks the proposals using both monocular
                                                                    images and depth maps. Their method outperforms both 3DOP
  We divide 3D object detection methods in three categories:        and Mono3D methods, despite using depth images to refine
monocular image, point cloud and fusion based methods. An           proposals.
overview of methodology, advantages and limitations for these          An important characteristic of driving environments is se-
methods is provided in Table III. The following subsections         vere occlusion present in crowded scenes where vehicles can
address each category individually.                                 block the view of other agents and themselves. Xiang et
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                                      5

                                                                 TABLE III
                                         C OMPARISON OF 3D O BJECT D ETECTION METHODS BY C ATEGORY

 Category                   Methodology/Advantages                      Limitations/Drawbacks                        Research Gaps
 Monocular                  Uses single RGB images to predict           The lack of explicit depth information       CNNs that estimate depth channels
                            3D object bounding boxes. Predicts 2D       on the input format limits the accuracy      could be investigated to increase local-
                            bounding boxes on the image plane           of localization performance.                 ization accuracy.
                            then extrapolate them to 3D through re-
                            projection constraints or bounding box
                            regression.
               Projection   Projects point clouds into a 2D image       Projecting the point cloud data in-          The encoding of the input image is per-
                            and use established architectures for ob-   evitably causes information loss. It also    formed with hand-engineered features
                            ject detection on 2D images with exten-     prevents the explicit encoding of spatial    (point density, etc.). Learned input rep-
                            sions to regress 3D bounding boxes.         information as in raw point cloud data.      resentations could improve the detection
                                                                                                                     results.
               Volumetric   Generates a 3 dimensional represen-         Expensive 3D convolutions increase           Volumetric methods have not consid-
                            tation of the point cloud in a voxel        models inference time. The volumetric        ered region proposals, which could im-
 Point-cloud                structure and uses Fully Convolutional      representation is sparse and computa-        prove both localization accuracy and
                            Networks (FCNs) to predict object de-       tionally inefficient.                        processing time.
                            tections. Shape information is encoded
                            explicitly.
                PointNet    Uses feed-forward networks consuming        Considering the whole point cloud as         PointNet architectures rely on region
                            raw 3D point clouds to generate predic-     input can increase run-time. Difficult es-   proposals to limit the number of points.
                            tions on class and estimated bounding       tablishing region proposals considering      Proposal methods based uniquely on
                            boxes.                                      raw point inputs.                            point-cloud data should be investigated.
 Fusion                     Fuses both front view images and point      Requires calibration between sensors,        These methods represent state-of-the-
                            clouds to generate a robust detections.     and depending on the architecture can        art detectors. However, they should be
                            Architectures usually consider multiple     be computationally expensive.                evaluated on more general scenarios
                            branches, one per modality, and rely on                                                  including diverse lighting and weather
                            region proposals. Allows modalities to                                                   conditions.
                            interact and complement each other.

al. introduce visibility patterns into the model to mitigate                  to improve small object detection by introducing multi-scale
occlusion effects through object reasoning. They propose the                  image pyramids.
3D Voxel Pattern (3DVP) [41] representation that models                          Despite the previous 3DVP representations [41], [45] allow
appearance through RGB intensities, 3D shape as a set of                      to model occlusion and parts appearance, they are obtained
voxels and occlusion masks. This representation allows to                     as a classification among an existing dictionary of visibility
recover which parts of the object are visible, occluded or                    patterns common in the training set. Thus, may fail to gener-
truncated. They obtain a dictionary of 3DVPs by clustering                    alize to an arbitrary vehicle pose that differs from the existing
the patterns observed on the data and training a classifier                   patterns. To overcome this, Deep MANTA [42] uses a many-
for each specific pattern given a 2D image segment of the                     task network to estimate vehicle position, part localization and
vehicle. During the test phase the pattern obtained through                   shape based only on monocular images. The vehicle shape
classification is used for occlusion reasoning and 3D pose                    consists of a set of key points that characterize the vehicle 3-
and localization estimation. They achieve 3D detection by                     dimensional boundaries, e.g. external vertices of the vehicle.
minimizing the reprojection error between the projected 3D                    They first obtain 2D bounding regression and parts localization
bounding box to the image plane and the 2D detection. Their                   through a two-level refinement region-proposal network. Next,
pipeline is still dependent on the performance of Region                      based on the inferred shape 3D model matching is performed
Proposal Networks (RPNs).                                                     to obtain the 3D pose.
   Although some RPNs were able to improve traditional                           Previous attempts performed either exhaustive search on
proposal methods [37] they still fail to handle occlusion,                    the 3D bounding box space [39], estimated 3D pose through
truncation and different object scales. Extending the previous                a cluster of appearance patterns [41] or 3D templates [42].
3DVP framework, the same authors propose SubCNN [45],                         Mousavian et al. [40] first extend a standard 2D object detector
a CNN that explores class information for object detection at                 with 3D orientation (yaw) and bounding box sizes regression.
the RPN level. They use the concept of subcategory, which are                 This is justified by the box dimensions having smaller variance
classes of objects sharing similar attributes such as 3D pose                 and being invariant with respect to the orientation. Most
or shape. Candidates are extracted using convolutional layers                 models use L2 regression for orientation angle prediction. In
to predict heat maps for each subcategory at the RPN level.                   contrast, the authors propose a Multi-bin method to regress
After Region of Interest (ROI) proposal the network outputs                   orientation. The angle is considered to belong to one of n
category classification along with refined 2D bounding box                    overlapping bins and a network estimates the confidence of
estimates. Using 3DVPs [41] as subcategories for pedestrian,                  the angle belonging to each bin along with a residual angle
cyclist and vehicle classes, the model recovers 3D shape,                     to be added to the bin center to recover the output angle. The
pose and occlusion patterns. An extrapolating layer is used                   3D box dimensions and orientations are fixed as determined
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                             6

by the network prediction. Then 3D object pose is recovered        is part of a vehicle or the background, effectively working as
solving for a translation matrix that minimizes the reprojection   a weak classifier. The second output encodes the vertices of
error of the 3D bounding box w.r.t. the 2D detection box on        the 3D bounding box delimiting the vehicle conditioned by the
the image plane.                                                   first output. Since there will be many BB estimates for each
   All previous monocular methods can only detect objects          vehicle, an NMS strategy is employed to reduce overlapping
from the front-facing camera, ignoring objects on the sides        predictions based on score and distance. The authors train this
and rear of the vehicle. While lidar methods can be used           detection model in an end-to-end fashion on the KITTI dataset
effectively for 360 degrees detection, [46] proposes the first     with loss balancing to avoid bias towards negative samples or
360 degrees panoramic image based method for 3D object             near cars, which appear more frequently.
detection. They estimate dense depth maps of panoramic                While previous methods used cylindrical and spherical
images and adapt standard object detection methods for the         projections, [30], [50], [51] use the bird-eye view projection
equirectangular representation. Due to the lack of panoramic       to generate 3D proposals. They differ regarding the input
labelled datasets for driving, they adapt the KITTI dataset        representation: the first encodes the 2D input cells using the
using style and projection transformations. They additionally      minimum, median and maximum height values of the points
provide benchmark detection results on a synthetic dataset.        lying inside the cell as channels, while the last two use height,
   Monocular methods have been widely researched. Although         intensity and density channels. The first approach uses a Faster
previous works considered hand-engineered features for region      R-CNN [13] architecture as a base with an adjusted refinement
proposals [39], most methods have shifted towards a learned        network that outputs oriented 3D bounding boxes. Despite
paradigm for Region Proposals and second stage of 3D model         their reasonable bird-eye view results, their method performs
matching and reprojection to obtain 3D bounding boxes. The         poor orientation angle regression. Most lidar base methods use
main drawbacks of monocular based methods is the lack of           sensors with high point density, which limits the application
depth cues, which limits detection and localization accuracy       of the resulting models on low-end lidar sensors. Beltran et
specially for far and occluded objects, and sensitivity to         al. [51] propose a novel encoding that normalizes the density
lighting and weather conditions, limiting the use of these         channel based on the parameters of the lidar being used.
methods for day time. Also, since most methods rely on a           This normalization creates a uniform representation and allows
front facing camera (except for [46]), it is only possible to      to generalise the detection model to sensors with different
detect objects in front of the vehicle, contrasting to point       specifications and number of beams.
clouds methods that, in principle, have a coverage all around         One fundamental requirement of safety-critical systems de-
the vehicle. We summarize the methodology/contributions and        ployed on autonomous vehicles, including object detection,
limitations of monocular methods in Table IV.                      is real-time operation capability. These systems must meet
                                                                   strict response time deadlines to allow the vehicle to respond
                                                                   to the environment. Complex-YOLO [30] focus on efficiency
B. Point cloud based methods
                                                                   using a YOLO [52] based architecture, with extensions to
   Current 3D object detection methods based on point-clouds       predict the extra dimension and yaw angle. While classical
can be divided into three subcategories: projection based,         RPN approaches further process each region for finer predic-
volumetric representations and point-nets. Each category is        tions, this architecture is categorized as a single-shot detector,
explained and reviewed below, followed by a summary dis-           obtaining detections in a single forward step. This allows
cussion.                                                           Complex-YOLO to achieve a runtime of 50 fps, up to five
   1) Projection methods: Image classification and object          times more efficient than previous methods, despite inferior,
detection in 2D images is a well-researched topic in the           but comparable detection performance.
computer vision community. The availability of datasets and           Quantifying the confidence of predictions made by an AV’s
benchmarked architectures for 2D images make using these           object detection system is fundamental for the safe operation
methods even more attractive. For this reason, point cloud         of such vehicle. As with human drivers, if the system has
(PCL) projection methods first transform the 3D points into        low confidence on its predictions, it should enter a safe state
a 2D image via plane [47], cylindrical [48] or spherical           to avoid risks. Although most detection models offer a score
[34] projections that can then be processed using standard         for each prediction, they tend to use softmax normalization to
2D object detection models such as [49]. The 3D bounding           obtain class distributions. Since this normalization forces the
box can then be recovered using position and dimensions            sum of probabilities to unity, it does not necessarily reflect the
regression.                                                        absolute confidence on the prediction. Feng et al. [53] uses a
   Li et al. [48] uses a cylindrical projection mapping and a      Bayesian Neural Network to predict the class and 3D bounding
Fully Convolutional Network (FCN) to predict 3D bounding           box after ROI pooling, which allows to quantify the network
boxes around vehicles only. The input image resulting from         confidence for both outputs. The authors quantify epistemic
the projection has channels encoding the points’ height and        and aleatoric uncertainties. While the former measures the
distance from the sensor. This input is fed to a 2D FCN            model uncertainty to explain the observed object, the latter
which down-samples the input for three consecutive layers and      relates to observation noises in scenarios of occlusion and
then uses transposed convolutional layers to up-sample these       low point density. They observed an increase in detection
maps into point-wise “objectness” and bounding box (BB)            performance when modelling aleatoric uncertainty by adding
prediction outputs. The first output defines if a given point      a constraint that penalizes noisy training samples.
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                                        7

                                                                      TABLE IV
                                                       S UMMARY OF M ONOCULAR BASED METHODS

Method         Methodology/Contributions                                                    Limitations
Mono3D         Improves detection performance over 3DOP that relied on the depth            Poor localization accuracy given the lack of depth cues.
[39]           channel.
3DVP [41]      Novel 3DVP object representation includes appearance, 3D shape and           Fixed set of 3DVPs extracted during training limits generalisa-
               occlusion information. Classification among an existing set of 3DVPs         tion to arbitrary object poses.
               allows occlusion reasoning and recovering 3D pose and localization.
SubCNN         Uses 3DVP representation to generate occlusion-aware region proposals.       Since the 3DVP representation is employed, this method has
[45]           The proposals are refined and classified within the object representations   the same limitations as the previous one.
               (3DVP). Improves RPN model refinement network using CNNs.
DeepManta      CNN to predict parts localization and visibility, fine orientation, 3D       Detection restricted to vehicles, ignoring other classes.
[42]           localization and template, 3D template matching to recover 3D position.
Deep3DBox      Simplified network architecture by independently regressing bounding         The reprojection error is dependent on the BB size and angle re-
[40]           box size and angle. Then using image reprojection error minimization         gressed by the network. This dependence increases localization
               to obtain 3D localization.                                                   error.
360Panoramic Estimates depth for 360 degrees panoramic monocular images. Then               Limited to vehicle detection and fails when the vehicle is too
[46]         adapt a CNN to predict 3D object detections on the recovered panoramic         close to the camera. The resolution of the camera limits the
             image. The only method capable of using images to detect objects at            range of detection.
             any angle around the vehicle.

   2) Volumetric convolutional methods: Volumetric methods                        fore, it is not obvious how to incorporate their structure to
assume that the object or scene is represented in a 3D grid, or                   traditional feed-forward deep neural networks pipelines that
a voxel representation, where each unit has attributes, such as                   assume fixed input data sizes. Previous methods attempted
binary occupancy or a continuous point density. One advan-                        to either transform the point cloud raw points into images
tage of such methods is that they encode shape information                        using projections or into volumetric structures using voxel
explicitly. However, as a consequence, most of the volume is                      representations. A third category of methods, called Point-nets,
empty, resulting in reduced efficiency while processing these                     handle the irregularities by using the raw points as input in an
empty cells. Additionally, since data is three dimensional by                     attempt to reduce information loss caused by either projection
nature 3D convolutions are necessary, drastically increasing                      or quantization in 3D space. We first review seminal work and
the computational cost of such models.                                            then progress to driving specific applications.
   To this effect [54], [55] address the problem of object                           The seminal work in the category is introduced by PointNet
detection on driving scenarios using one-stage FCN on the                         [56]. Segmented 3D PCLs are used as input to perform object
entire scene volumetric representation. This one-stage detec-                     classification and part-segmentation. The network performs
tion differs from two-stage where region proposals are first                      point-wise transformations using Fully-Connected (FC) layers
generated and then refined on a second processing stage.                          and aggregates a global feature through a max-pooling layer,
Instead, one-stage detectors infer detection predictions in a                     ensuring independence on point order. Experimental results
single forward pass. Li et al. [54] uses a binary volumetric                      show that this approach outperforms volumetric methods [57],
input and detects vehicles only. The model’s output maps                          [58]. This model is further extended in PointNet++ [59], where
represent “objectness” and BB vertices predictions, similarly                     each layer progressively encode more complex features in a
to the authors’ previous work [48]. The first output predicts                     hierarchical structure. The model generate overlapping sets of
if the estimated region belongs to an object of interest, while                   points and local attribute features are obtained by feeding each
the second predicts its coordinates. They use expensive 3D                        set to a local PointNet. Follow up work by Wang et al. [60]
convolutions which limits temporal performance.                                   further generalize the PointNet architecture by considering
   Aiming at a more efficient implementation, [55] fixes BB                       points pair-wise relationships. More detailed information on
sizes for each class but detects cars, pedestrians and cyclists.                  convolutional neural networks for irregular domains is out of
This assumption simplifies the architecture and together with a                   the scope of this paper but can be found in [61].
sparse convolution algorithm greatly reduces the model’s com-                        The seminal methods assumed segmented PCLs that contain
plexity. L1 regularization and Rectified Linear Unit (ReLU)                       a single object, but the gap between object classification
activation functions are used to maintain sparsity across con-                    and detection is still an open question. VoxelNet [62] uses
volutional layers. Parallel networks are used independently                       raw point subsets to generate voxel-wise features, creating
for each class during inference. The assumption of fixed BB                       a uniform representation of the point cloud, as obtained in
sizes allows to train the network directly on the 3D crops                        volumetric methods. The first step randomly selects a fixed
of positive samples. During training they augment the data                        number of points from each voxel, reducing evaluation time
with rotation and translation transformation and employ hard                      and enhancing generalization. Each set of points is used by
negative mining to reduce false positives.                                        a voxel-feature-encoding (VFE) layer to generate a 4D point
   3) Point-nets methods: Point clouds consist of a variable                      cloud representation. This representation is fed to 3D convo-
number of 3D points sparsely distributed in space. There-                         lutional layers, followed by a 3D region proposal network to
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                              8

predict BB location, size and class. The authors implement             One fusion strategy consists of using the point cloud pro-
an efficient convolution operation considering the sparsity of      jection method, presented in Section IV-B1, with extra RGB
the voxel representation. Different voxel sizes are used for        channels of front facing cameras along the projected PCL
cars and pedestrians/cyclists to avoid detail loss. Models are      maps to obtain higher detection performance. Two of these
trained independently for each class, resulting in three models     methods [6], [64] use 3D region proposal networks (RPNs)
that must be used simultaneously during inference. In Frustum       to generate 3D Regions of Interest (ROI) which are then
PointNet [63] detection is achieved by selecting sets of 3D         projected to the specific views and used to predict classes and
points and using a PointNet to classify and predict bounding        3D bounding boxes.
boxes for each set. The set selection criterion is based on 2D         The first method, MV3D [64], uses bird-eye and front
detections on the image plane, thus this method is classified       view projections of lidar points along the RGB channels of
as a Fusion method, reviewed in Section IV-C.                       a forward facing camera. The network consists of three input
   4) Discussion: Among point cloud based methods, the              branches, one for each view, with VGG [38] based feature
projection subcategory has gained most attention due to the         extractors. The 3D proposals, generated based on the bird-
proximity to standard image object detection. Particularly, it      eye view features only, are projected to each view’s feature
offers a good trade-off between time complexity and detection       maps. A ROI pooling layer extracts the features corresponding
performance. However, most methods rely on hand-engineered          to each view’s branch. These proposal-specific features are
features when projecting the point cloud (density, height, etc.).   aggregated in a deep fusion scheme, where feature maps
In contrast, PointNet methods uses the raw 3D points to learn       can hierarchically interact with one another. The final layers
a representation in feature space. In this last category it is      output the classification result and the refined vertices of
still necessary to investigate new forms of using a whole           the regressed 3D bounding box. The authors investigate the
scene point cloud as input, as regular PointNet models assume       performance of different fusion methods and conclude that
segmented objects. Volumetric methods transform the point           the deep fusion approach obtains the best performance since
cloud into voxel representations where the space information        it provides more flexible means of aggregating features from
in explicitly encoded. This approach causes a sparse represen-      different modalities.
tation which is inefficient given the need of 3D convolutions.         The second method, AVOD [6], is the first to introduce an
We present a summary of point cloud-based methods in Table          early fusion approach where the bird-eye view and RGB chan-
V.                                                                  nels are merged for region proposal. The input representations
                                                                    are similar to MV3D [64] except that only the bird-eye view
                                                                    and image input branches are used. Both modalities’ feature
C. Fusion based methods                                             maps are used by the RPN, achieving high proposal recall. The
   As mentioned previously, point clouds do not provide tex-        highest scoring region proposals are sampled and projected
ture information, which is valuable for class discrimination        into the corresponding views’ feature maps. Each modality
in object detection and classification. In contrast, monocular      proposal specific features are merged and a FC layer outputs
images cannot capture depth values, which are necessary for         class distribution and refined 3D boxes for each proposal.
accurate 3D localization and size estimation. Additionally, the     Commonly, loss of details after convolutional stages prevents
density of point clouds tends to reduce quickly as the distance     detection of small objects. The authors circumvent this by
from the sensor increases, while images can still provide           upsampling the feature maps using Feature Pyramid Networks
a means of detecting far vehicles and objects. In order to          [66]. Qualitative results show robustness to snowy scenes and
increase the overall performance, some methods try to use           poor illumination conditions on private data.
both modalities with different strategies and fusion schemes.          A second strategy consists of using the monocular image
Generally there are three types of fusion schemes [64]:             to obtain 2D candidates and extrapolate these detections to
                                                                    the 3D space where point cloud data is employed. In this
Early fusion: Modalities are combined at the beginning of           category Frustum Point-Net [63] generates region proposals
    the process, creating a new representation that is depen-       on the image plane with monocular images and use the point
    dent on all modalities.                                         cloud to perform classification and bounding box regression.
Late fusion: Modalities are processed separately and inde-          The 2D boxes obtained over the image plane are extrapolated
    pendently up to the last stage, where fusion occurs. This       to 3D using the camera calibration parameters, resulting
    scheme does not require all modalities be available as it       in frustums region proposals. The points enclosed by each
    can rely on the predictions of a single modality.               frustum are selected and segmented with a PointNet instance
Deep fusion: Proposed in [64], it mixes the modalities hier-        to remove the background clutter. This set is then fed to a
    archically in neural network layers, allowing the features      second PointNet instance to perform classification and 3D BB
    from different modalities to interact over layers, resulting    regression. Similarly, Du et al. [67] first select the points that
    in a more general fusion scheme.                                lie in the detection box when projected to the image plane,
In [65] the authors evaluate the fusion at different stages of      then use these points to perform model fitting, resulting in
a 3D pedestrian detection pipeline. Their model considered          a preliminary 3D proposal. The proposal is processed by a
two inputs: monocular image and a depth frame. The authors          two-stage refinement CNN that outputs the final 3D box and
conclude that late fusion yields the best performance, although     confidence score. The detections in both these approaches are
early fusion can be used with minor performance drop.               constrained by the proposal on monocular images, which can
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                                      9

                                                                  TABLE V
                                                  S UMMARY OF P OINT CLOUD - BASED METHODS

SubCategory   Method       Methodology/Contributions                                            Limitations
              VeloFCN      Uses fully convolutional architecture with lidar point cloud bird-   Detects vehicles only. Limited performance on small or
              [48]         eye view projections. Output maps represent 3D bounding box          occluded objects due to the loss of resolution across
                           regressions and “objectness” score, the likelihood of having an      feature maps.
                           object at that position.
              C-YOLO       Uses a YOLO based single-shot detector extended for 3D BB            There is a tradeoff between inference time and detection
              [30]         and orientation regression. The proposed architecture achieves       accuracy. Single-shot networks underperform networks
 Projection                50 fps runtime, more than any previous method.                       that use a second stage for refinement.
              TowardsSafe Uses variational dropout inference to quantify uncertainty in         The uncertaity estimation requires several forward
              [53]        class and bounding box predictions. Aleatoric noise modelling         passes of the network. This limits the temporal perfor-
                          allows the network to generalise better by reducing the impact        mance of this method, preventing real-time results.
                          of noisy samples in the training process.
              BirdNet      Normalizes point cloud representation to allow detection gen-        Input image with only 3 channels encoding height,
              [51]         eralisation across different lidar models and specifications.        density and intensity information looses detailed infor-
                                                                                                mation, which degrades performance.
              3DFCN        Extension of the FCN architecture to voxelized lidar points          Requires 3D convolutions, limiting temporal perfor-
 Volumetric   [54]         clouds. Single shot detection method.                                mance to 1 fps.
              Vote3Deep    Proposes an efficient convolutional algorithm to exploit the         Assumes fixed sizes for all detected objects, limiting the
              [55]         sparsity of volumetric point cloud data. Uses L1 regularisation      detection performance.
                           and Rectified Linear Unit (ReLU) to maintain sparsity.
              VoxelNet     Extends PointNet concept to point clouds in a scene scale.           Expensive 3D convolutions limits time performance.
  PointNet    [62]         Uses raw 3D points to learn a volumetric representation through      Models are class specific, thus multiple models must
                           Voxel Feature Encoding layers. The volumetric features are used      be run in parallel at run time.
                           for 3D region proposal.

be a limiting factor due to lighting conditions, etc.                           Although both precision and recall are parametrized by t,
   Fusion methods obtain state-of-the-art detection results by               the precision/recall curve can be parametrized by the recall
exploring complimentary information from multiple sensor                     r. This curve can be summarized by a single metric called
modalities. While lidar point clouds provide accurate depth                  Average Precision (AP) [68]:
information with sparse and low point density at far locations,                                     1     X
cameras can provide texture information which is valuable                                    AP =                 pinterp (r)         (3)
                                                                                                    11
for class discrimination. Fusion of information at feature                                                    r∈{0,0.1,...,1}
levels allow to use complimentary information to enhance                     where pinterp (r) = maxr̃:r̃≥r p(r̃) is an interpolated version of
performance. We provide a summary of fusion methods in                       the precision for a recall level r. This metric is the average
Table VI.                                                                    precision at 11 different recall levels, ranging from 0 to 1 with
                                                                             0.1 step size, and reduces the impact of small variations in the
                         V. E VALUATION                                      probabilistic output.
   This section presents metrics commonly used for 3D object                    Most of the discussed works used the KITTI dataset for
detection. Performance for some of the reviewed methods                      training and evaluation, which provides a consistent baseline
is also provided, followed by a comprehensive discussion                     for comparison. Detections are evaluated considering the im-
of the results. Finally, we present research challenges and                  age plane AP, hereafter called AP2D . Samples are considered
opportunities.                                                               true positives if the overlapping area of the estimated and
                                                                             ground-truth boxes exceeds a certain threshold. Specifically,
                                                                             the Intersection over Union (IoU) of the bounding boxes areas
A. Metrics                                                                   in the image plane should exceed 0.5 for pedestrians and
   For any detection or classification task that outputs a con-              cyclists and 0.7 for vehicles. The dataset guidelines suggest
fidence yi of sample xi belonging to the positive class, it is               to evaluate 3D object detection using both AP2D and Average
possible to compute a precision/recall curve using the ranked                Orientation Similarity (AOS) metrics [29]. The latter jointly
output. Recall is defined as the proportion of all positive                  measures the 2D detection and 3D orientation performance by
samples ranked above a given threshold t:                                    weighting the AP2D score with the cosine similarity between
                                                                             the estimated and ground-truth orientations.
                  r(t) = P (yi ≥ t | xi ∈ C)                          (1)       Despite being employed by most monocular models, these
where C is the set of positive samples.                                      two metrics fail to decouple the effects of localization and
   Likewise, precision is the proportion of all samples above                bounding box sizes estimation [69]. They also introduce
threshold t which are from the positive class:                               distortion due to image plane projection. For example, two
                                                                             objects of different sizes at different locations can have the
                 p(t) = P (xi ∈ C | yi ≥ t).                          (2)    same bounding box projection on the image plane. To solve
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                                        10

                                                                    TABLE VI
                                                        S UMMARY OF F USION BASED METHODS

Method       Methodology/Contributions                                                    Limitations
MV3D [64]    Uses bird-eye and front view lidar projections as well as monocular          Although far objects might be visible through the camera, the
             camera frames to detect vehicles. 3D proposal network based on the           low lidar point density prevents detection of these objects.
             bird-eye-view. Introduces a deep fusion architecture to allow interactions   Specifically, the RPN based on the bird-eye view only limits
             between modalities.                                                          these detections. Detects vehicles only.
AVOD [6]     Uses bird-eye lidar projection and monocular camera only. New RPN            Detection method only sensitive to objects in front of the vehicle
             uses both modalities to generate proposals. A Feature Pyramid Network        due to the forward-facing camera used.
             extension improves detection of small objects by up sampling feature
             maps. New vector representation removes ambiguities in the orientation
             regression. Can detect vehicles, pedestrians and cyclists.
F-PointNet   Extracts 2D detection from image plane, extrapolates detection to a 3D       Since proposals are obtained from the front view image, failing
[63]         frustum, selecting lidar points. Uses a PointNet instance to segment         to detect objects in this view limits the detection performance.
             background points and generate 3D detections. Can detect vehicles,           This limits the use of this method at night time, for example.
             pedestrians and cyclists.

this, Chen et al. [64] project the 3D detections into the bird-                 object detection results in Table VII for the car class and Table
eye view to compute a more meaningful 3D localization                           VIII for pedestrian and cyclists classes obtained on the original
metric (APBV ). To overcome the projection distortion, they                     papers and the KITTI online benchmark [5].
also use an AP3D metric, which uses the IoU of volumes of 3D                       The first group in Tables VII and VIII lists monocular based
boxes. These metrics are crucial because they allow to assess                   methods which optimize 2D detections separately. On the other
localization and size regression performance that cannot be                     hand, methods in the second group optimize 3D bounding
reliably captured only by the image plane AP.                                   boxes directly. For evaluation, the latter group projects the
   Still, the AP3D metric fails to precisely assess orientation                 3D boxes onto the image plane. This projection result in 2D
estimation. This is due to the metric considering positive                      boxes that does not necessarily fit tightly to predictions based
samples based on a threshold of the IoU metric. In this case, it                on the image plane directly due to the yaw angle and size
will not penalize orientation error as long as there is sufficient              predictions. This explains the disparity of results between the
overlapping volume. Ku et al. [6] penalize orientation angle                    two groups, specifically for the Easy category.
by extending the AOS metric with 3D volume overlapping.                            The same tables reveal a disparity in performance between
They use the AP3D metric weighted by the cosine similarity                      classes: cars’ AP2D is at least 10% higher than pedestrians
of regressed and ground-truth orientations, resulting in the                    and cyclists for most methods. This effect happens for two
Average Heading Similarity (AHS) metric:                                        reasons. Firstly, bigger objects are more easily detected and
                        1      X                                                are more resilient to occlusion than smaller ones. Secondly,
               AHS =                     max s(r̃)             (4)              many methods only fine-tune their models for vehicles, where
                       11                r̃:r̃≥r
                             r∈{0,0.1,...,1}
                                                                                different classes may require another set of hyper-parameters.
with s(r) being the orientation similarity defined for every                    In addition, the intra-class performance degrades as the com-
recall r as                                                                     plexity increases, which is explained by severe occlusion in
                                                                                moderate and hard samples.
                1                     1 + cos(θ − θ̃)
                          1(IoU ≥ λ)
                     X
       s(r) =                                            (5)                       Despite the reasonable results on image plane projections,
              |D(r)|                         2
                       i∈D(r)                                                   the first two tables fail to assess all the components of 3D de-
                                                                                tection, e.g. localization, dimension and orientation regression.
where θ is the orientation estimate and θ̃ the ground-truth
                                                                                To this effect, Table IX obtained from [6] presents 3D metrics
orientation, D(r) is the set of all detections at recall r and
                                                                                on three methods for the car class on the KITTI validation
1(IoU ≥ λ) is the indicator function to consider valid                          set with 0.7 3D IoU threshold. The AHS metric confirms that
detection during AHS computation. The indicator function can
                                                                                the orientation regression proposed by AVOD [6] fixes the
be shaped to compute both the 3D (using IoU of the volumes)
                                                                                ambiguity in the representation adopted in MV3D [64].
and bird-eye (IoU of the bird-eye projections) AHS. Note that
                                                                                   Monocular detection methods show very limited perfor-
the AHS is upper bounded by AP3D or APBV , depending on
                                                                                mance on 3D detection metrics, as evidenced by the large
the metric used.
                                                                                performance gap on 3D metrics between the two groups in
                                                                                Table IX. This poor performance arises from the lack of
B. Performance of Existing Methods                                              depth information in monocular images. Hence, monocular
  All the reviewed methods in this paper provide 3D bounding                    methods cannot be reliably used for 3D object detection in
box outputs. However, most monocular based methods directly                     AVs. Moreover, this evaluation suggests that the AP2D and
predict 2D detections on their pipeline before generating the                   AOS metrics are not enough to confidently assess 3D object
3D detection. Many of these methods only provide AP2D                           detection methods.
and AOS result metrics. For this reason and considering an                         Table X presents 3D metrics on the KITTI 3D object detec-
extensive comparison between methods, we report image plane                     tion benchmark [5] considering the impact of localization and
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                              11

                          TABLE VII
 KITTI TEST SET RESULTS ON 2D O BJECT DETECTION FOR CAR CLASS

                                         AP2D                    AOS
Method            Modality
                                  E       M      H        E       M      H
DeepManta [42]    Mono           96.4    90.1    80.79   96.32   89.91   80.55
SubCNN [45]       Mono           90.81   89.04   79.27   90.67   88.62   78.68
Deep3DBox [40]    Mono           92.98   89.04   77.17   92.9    88.75   76.76
DeepStOP [44]     Stereo         93.45   89.04   79.58   92.04   86.86   77.34 Fig. 4. Recall vs number of proposals 3D IoU threshold of 0.5 for three
Mono3D [39]       Mono           92.33   88.66   78.96   91.01   86.62   76.84 classes on KITTI validation set with moderate samples. Obtained from [6].
3DOP [43]         Stereo         93.04   88.64   79.1    91.44   86.1    76.52
3DVP [41]         Mono           87.46   75.77   65.38   86.92   74.9    64.11
F-PointNet [63]   LIDAR+Mono 90.78       90      80.8                          C. Research Challenges and Opportunities
MV3D [64]         LIDAR+Mono 90.53       89.17   80.16
AVOD-FPN [6]      LIDAR+Mono 89.99       87.44   80.05 89.95 87.13 79.74          We propose some further research topics that should be
VoxelNet [62]     LIDAR      90.3        85.95   79.21                         considered to advance the performance of 3D object detection
3DFCN [54]        LIDAR      84.2        75.3    68    84.1 75.2 67.9
Vote3Deep [55]    LIDAR      76.79       68.24   63.23                         in the context of autonomous vehicles. The topics were elab-
VeloFCN [48]      LIDAR      60.3        47.5    42.7 59.1 459     41.1        orated based on the significant performance disparity between
      E, M and H stands for Easy, Moderate and Hard, respectively.             2D and 3D detectors and gaps found in the literature.
                                                                                  1) Most research in 3D object detection has focused on
                                                                                     improving the benchmark performance of such methods.
bounding box parameters. The results of monocular methods                            Although this is a valid goal, there is no understanding
are not available because the 3D object detection benchmark                          on the required detection performance levels for reliable
has been established after the publication of those methods.                         driving applications. In this regard, a valid research op-
Clearly the detection performance gap evidenced in 2D and                            portunity is in investigating how detection performance
3D AP metrics is still large. The best performing method                             relates to the safety of driving, measured by relevant
achieves approximately 82% AP3D on the easy car class, while                         Key Performance Indicators (KPIs).
the image plane counterpart achieves higher than 95% AP2D .                       2) The recent advances in PointNets, described in Section
This is explained by the complexity in regressing parameters                         IV-B3, can be explored to verify resilience to missing
for an extra dimension and also motivates further research to                        points and occlusion, which is still the main cause of
improve results and enable robust detection for autonomous                           poor performance on hard samples. More specifically,
driving applications.                                                                the geometrical relationships between points could be
                                                                                     explored to obtain significant information that cannot
   Region proposal networks’ performance is critical as they                         be attained considering each point individually.
impose the upper bound detection recall for two stage de-                         3) Many methods consider sensor fusion to improve reli-
tectors. These networks can be regarded as weak classifiers,                         ability of the perception system. Considering the dis-
which aim at narrowing down the object search space. Thus,                           parity in point density, a possible contribution would
reducing the number of possibilities that a more specific,                           include a collaborative perception approach in a multi-
complex network has to process. Ideally, it should retrieve all                      agent fusion scheme. Vehicles could use V2X or LTE
the instances in order to avoid false negatives, although it is not                  communication technology to share relevant perception
expected to get a high precision on these primitive proposals.                       information that could improve and extend the visibility
Ku et al. [6] assess their fusion RPN scheme using the recall                        of the environment and thus reduce uncertainty and
metric and compare it to other baseline methods, see Figure 4.                       improve performance perception methods.
These results show the performance improvement achieved by                        4) An important limitation of the KITTI dataset is its
learning approaches versus hand-engineered based proposals                           characteristic daylight scenes and very standard weather
such as in [39], [43]. Unlike cars, pedestrians and cyclists                         conditions. Although [6] reports having tested their
have a significant improvement when considering the fusion                           method during night-time and under snow, they only
scheme. These classes have smaller dimensions and cannot                             report qualitative results. Further research should be
be completely represented exclusively in the bird-eye view,                          conducted to evaluate the effect of such conditions on
benefiting from more information obtained from the image                             the object detection pipeline and how to achieve reliable
plane.                                                                               performance under general conditions. The simulation
   Regarding runtime, most methods cannot operate in the                             tools described in Section III could be used to obtain
real-time, considering the lidar or camera frame rate. As                            preliminary results.
an exception, Complex-YOLO [30] achieves a 50 fps frame                           5) The run time presented in Table X show that most
rate. The simpler single-shot architecture reflects in a small                       methods can only achieve lower than 10 fps, which is
performance drop. It must be noted that the authors did                              the minimum rate to keep real time operation with the
not provide public results on the KITTI test set, reporting                          lidar frame rate. Significant improvement has to be done
their results on the validation set instead, which makes direct                      to obtain fast and reliable recognition systems operating
comparison to other methods dubious.                                                 on real environments.
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                                                 12

                                                                   TABLE VIII
                                  KITTI TEST SET RESULTS ON 2D O BJECT DETECTION FOR PEDESTRIANS AND CYCLISTS

                                                                              AP2D                                                     AOS
    Method                  Modality
                                                          Pedestrians                    Cyclists                   Pedestrians                      Cyclists
                                                    E         M           H          E     M         H        E         M          H          E         M       H
    SubCNN [45]             Mono                  83.28     71.33       66.36    79.48    71.06     62.68   78.45     6.28        61.36      72        63.65    56.32
    DeepStereoOP [39]       Stereo                81.82     67.32       65.12    79.58    65.84     57.90   72.82     59.28       56.85      69.20     55.69    48.95
    Mono3D [39]             Mono                  80.35     66.68       63.44    76.04    66.36     58.87   71.15     58.15       54.94      65.56     54.97    48.77
    3DOP [43]               Stereo                81.78     67.47       64.7     78.39    68.94     61.37   72.94     59.8        57.03      70.13     58.68    52.35
    F-PointNet [63]         LIDAR+Mono            87.81     77.5        74.46    84.9     72.25     65.14
    AVOD-FPN [6]            LIDAR+Mono            67.32     58.4        57.44    68.65    59.32     55.82   53.36     44.92       43.77      67.61     57.53    54.16
    VoxelNet [62]           LIDAR                 50.61     44.08       42.84    72.04    59.33     54.72
    Vote3Deep [55]          LIDAR                 68.39     55.37       52.59    79.92    67.88     62.98
                                                  E, M and H stands for Easy, Moderate and Hard, respectively.

                           TABLE IX                                                                                 VI. C ONCLUSION
 KITTI VALIDATION SET RESULTS FOR AP 3D AND AHS FOR CAR CLASS .
                  O BTAINED FROM [6] AND [64].                          This paper reviewed the state-of-the-art of 3D object detec-
                                                                     tion within the context of autonomous vehicles. We analysed
Method            Modality
                                      AP3D                  AHS      sensors technologies with their advantages and disadvantages,
                                                                     and discussed standard datasets. The reviewed works were
                                  E     M      H       E      M    H
                                                                     categorized based on sensor modality: monocular images,
Mono3D [39]       Mono           2.53 2.31 2.31
Deep3DBox [40]    Mono           5.84 4.09 3.83 5.84 4.09 3.83 point clouds (obtained through lidars or depth cameras) and
3DOP [43]         Stereo         6.55 5.07 4.1                       fusion of both.
MV3D [64]         LIDAR+Mono 83.87 52.74 72.35 64.56 43.75 39.86        Quantitative results, obtained from the KITTI benchmark,
AVOD-FPN [6]      LIDAR+Mono 84.41 74.44 68.65 84.19 74.11 68.28 showed that monocular methods are not reliable for 3D object
      E, M and H stands for Easy, Moderate and Hard, respectively.   detection, due to lack of depth information, which prevents
                                                                     accurate 3D positioning. On the other hand, fusion methods
                              TABLE X
                                                                     were used to extract the most relevant information from each
 3D OBJECT DETECTION BENCHMARK ON KITTI TEST SET. 3D I O U 0.7       modality and achieve state-of-the-art results for 3D object
                                                                     detection. Finally, we presented directions of future work.
                                             AP3D                       APBV
Method             Time(s)Class       E       M         H        E       M       H
MV3D [64]          0.36              71.09   62.35      55.12   86.02    76.9    68.49                                R EFERENCES
AVOD [6]           0.08              73.59   65.78      58.38   86.8     85.44   77.73
AVOD-FPN [6]       0.1               81.94   71.88      66.38   88.53    83.79   77.9    [1] “Reported road casualties in Great Britain: quarterly provisional
                           Car                                                               estimates year ending September 2017,” UK Department for
F-Pointnet [63]    0.17              81.2    70.39      62.19   88.7     84      75.33
Voxelnet [62]      0.23              77.47   65.11      57.73   89.35    79.26   77.39       Transport, Tech. Rep., February 2018. [Online]. Available:
C-YOLO1 [30]       0.02              67.72   64         63.01   85.89    77.4    77.33       https://assets.publishing.service.gov.uk/government/uploads/system/
                                                                                             uploads/attachment data/file/681593/quarterly-estimates-july-to-
AVOD [6]           0.08              38.28   31.51      26.98   42.51    35.24   33.97       september-2017.pdf
AVOD-FPN [6]       0.1               50.8    42.81      40.88   58.75    51.05   47.54   [2] “Traffic Safety Facts,” National Highway Traffic Safety Administration,
F-Pointnet [63]    0.17   Ped        51.21   44.89      40.23   58.09    50.22   47.2        US Department of Transportation, Tech. Rep. DOT HS 812 115,
Voxelnet [62]      0.23              39.48   33.69      31.51   46.13    40.74   38.11       February 2015. [Online]. Available: https://crashstats.nhtsa.dot.gov/Api/
C-YOLO1 [30]       0.02              41.79   39.7       35.92   46.08    45.9    44.2        Public/ViewPublication/812115
AVOD [6]           0.08              60.11   44.9       38.8    63.66    47.74   46.55   [3] “Research on the Impacts of Connected and Autonomous
AVOD-FPN [6]       0.1               64      52.18      46.61   68.09    57.48   50.77       Vehicles (CAVs) on Traffic Flow,” UK Department for
F-Pointnet [63]    0.17   Cyc        71.96   56.77      50.39   75.38    61.96   54.68       Transport,     Tech.    Rep.,     May     2016.    [Online].   Available:
Voxelnet [62]      0.23              61.22   48.36      44.37   66.7     54.76   50.55       https://assets.publishing.service.gov.uk/government/uploads/system/
C-YOLO1 [30]       0.02              68.17   58.32      54.3    72.37    63.36   60.27       uploads/attachment data/file/530091/impacts-of-connected-and-
                                                                                             autonomous-vehicles-on-traffic-flow-summary-report.pdf
  1 The authors did not provide public test set results, only validation set             [4] “Technical report, Tesla Crash,” National Highway Traffic Safety Ad-
      E, M and H stands for Easy, Moderate and Hard, respectively.                           ministration, US Department of Transportation, Tech. Rep. PE 16-007,
                                                                                             January 2017.
                                                                                         [5] KITTI 3D Object Detection Online Benchmark. [Online]. Available:
                                                                                             http://www.cvlibs.net/datasets/kitti/eval object.php?obj benchmark=3d
  6) Most methods cannot output a calibrated confidence [70]                             [6] J. Ku, M. Mozifian, J. Lee, A. Harakeh, and S. Waslander, “Joint 3d
     on predictions, which can lead to dangerous behaviours                                  proposal generation and object detection from view aggregation,” IROS,
                                                                                             2018.
     in real scenarios. Seminal work [53] identified this
                                                                                         [7] B. Ranft and C. Stiller, “The Role of Machine Vision for Intelligent
     gap and proposed a method to quantify uncertainty                                       Vehicles,” IEEE Transactions on Intelligent Vehicles, vol. 1, no. 1, pp.
     in detection models, but failed to achieve real-time                                    8–19, 2016.
     performance. More research should be conducted in this                              [8] S. D. Pendleton, H. Andersen, X. Du, X. Shen, M. Meghjani, Y. H.
                                                                                             Eng, D. Rus, and M. H. Ang, “Perception, Planning, Control, and
     area to understand the origins of uncertainty and how to                                Coordination for Autonomous Vehicles,” Machines, vol. 5, no. 1, p. 6,
     mitigate them.                                                                          Feb. 2017. [Online]. Available: http://www.mdpi.com/2075-1702/5/1/6
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                                    13

 [9] A. Mukhtar, L. Xia, and T. B. Tang, “Vehicle Detection Techniques            [30] M. Simon, S. Milz, K. Amende, and H. Gross, “Complex-YOLO: Real-
     for Collision Avoidance Systems: A Review,” IEEE Transactions on                  time 3D Object Detection on Point Clouds,” CoRR, vol. abs/1803.06199,
     Intelligent Transportation Systems, vol. 16, no. 5, pp. 2318–2338, Oct.           2018. [Online]. Available: http://arxiv.org/abs/1803.06199
     2015.                                                                        [31] A. Gaidon, Q. Wang, Y. Cabon, and E. Vig, “Virtual Worlds as Proxy
[10] D. Z. Wang, I. Posner, and P. Newman, “What could move? Finding cars,             for Multi-Object Tracking Analysis,” in 2016 IEEE Conference on
     pedestrians and bicyclists in 3d laser data,” in 2012 IEEE International          Computer Vision and Pattern Recognition (CVPR), June 2016.
     Conference on Robotics and Automation, May 2012, pp. 4038–4044.              [32] S. Chen, S. Zhang, J. Shang, B. Chen, and N. Zheng, “Brain-inspired
[11] A. Azim and O. Aycard, “Layer-based supervised classification of                  Cognitive Model with Attention for Self-Driving Cars,” IEEE Transac-
     moving objects in outdoor dynamic environment using 3d laser scanner,”            tions on Cognitive and Developmental Systems, vol. PP, no. 99, pp. 1–1,
     in 2014 IEEE Intelligent Vehicles Symposium Proceedings, Jun. 2014,               2017.
     pp. 1408–1414.                                                               [33] H. Xu, Y. Gao, F. Yu, and T. Darrell, “End-to-End Learning of Driving
[12] J. Behley, V. Steinhage, and A. B. Cremers, “Laser-based segment                  Models from Large-Scale Video Datasets,” in 2017 IEEE Conference
     classification using a mixture of bag-of-words,” in Intelligent Robots and        on Computer Vision and Pattern Recognition (CVPR), Jul. 2017, pp.
     Systems (IROS), 2013 IEEE/RSJ International Conference on. IEEE,                  3530–3538.
     2013, pp. 4195–4200.                                                         [34] B. Wu, A. Wan, X. Yue, and K. Keutzer, “SqueezeSeg:
[13] S. Ren, K. He, R. Girshick, and J. Sun, “Faster R-CNN: Towards real-              Convolutional Neural Nets with Recurrent CRF for Real-
     time object detection with region proposal networks,” in Advances in              Time Road-Object Segmentation from 3D LiDAR Point
     Neural Information Processing Systems (NIPS), 2015.                               Cloud,” CoRR, vol. abs/1710.07368, 2017. [Online]. Available:
[14] Y. Zhang, M. Pezeshki, P. Brakel, S. Zhang, C. Laurent, Y. Bengio,                http://arxiv.org/abs/1710.07368
     and A. Courville, “Towards End-to-End Speech Recognition with Deep           [35] A. Dosovitskiy, G. Ros, F. Codevilla, A. Lopez, and V. Koltun,
     Convolutional Neural Networks,” in Interspeech 2016, 2016, pp. 410–               “CARLA: An Open Urban Driving Simulator,” 1st Conference on Robot
     414. [Online]. Available: http://dx.doi.org/10.21437/Interspeech.2016-            Learning (CoRL), Nov. 2017.
     1446                                                                         [36] M. Mller, V. Casser, J. Lahoud, N. Smith, and B. Ghanem, “Sim4cv: A
[15] J. Van Brummelen, M. OBrien, D. Gruyer, and H. Najjaran, “Au-                     Photo-Realistic Simulator for Computer Vision Applications,” Interna-
     tonomous vehicle perception: The technology of today and tomorrow,”               tional Journal of Computer Vision, Mar. 2018.
     Transportation Research Part C: Emerging Technologies, vol. 89, pp.          [37] R. Girshick, “Fast R-CNN,” in Proceedings of the 2015 IEEE
     384–406, Apr. 2018.                                                               International Conference on Computer Vision (ICCV), ser. ICCV ’15.
[16] S. Kuutti, S. Fallah, K. Katsaros, M. Dianati, F. Mccullough, and                 Washington, DC, USA: IEEE Computer Society, 2015, pp. 1440–1448.
     A. Mouzakitis, “A Survey of the State-of-the-Art Localization Tech-               [Online]. Available: http://dx.doi.org/10.1109/ICCV.2015.169
     niques and Their Potentials for Autonomous Vehicle Applications,”            [38] K. Simonyan and A. Zisserman, “Very deep convolutional networks for
     IEEE Internet of Things Journal, vol. 5, no. 2, pp. 829–846, April 2018.          large-scale image recognition,” in International Conference on Learning
[17] M. Weber, P. Wolf, and J. M. Zllner, “DeepTLR: A single deep                      Representations, 2015.
     convolutional network for detection and classification of traffic lights,”   [39] X. Chen, K. Kundu, Z. Zhang, H. Ma, S. Fidler, and R. Urtasun,
     in 2016 IEEE Intelligent Vehicles Symposium (IV), Jun. 2016, pp. 342–             “Monocular 3d Object Detection for Autonomous Driving,” in 2016
     348.                                                                              IEEE Conference on Computer Vision and Pattern Recognition (CVPR),
[18] S. Sivaraman and M. M. Trivedi, “Looking at Vehicles on the Road:                 Jun. 2016, pp. 2147–2156.
     A Survey of Vision-Based Vehicle Detection, Tracking, and Behavior           [40] A. Mousavian, D. Anguelov, J. Flynn, and J. Koeck, “3d Bounding
     Analysis,” IEEE Transactions on Intelligent Transportation Systems,               Box Estimation Using Deep Learning and Geometry,” in 2017 IEEE
     vol. 14, no. 4, pp. 1773–1795, Dec. 2013.                                         Conference on Computer Vision and Pattern Recognition (CVPR), Jul.
[19] S. Hsu, S. Acharya, A. Rafii, and R. New, “Performance of a time-                 2017, pp. 5632–5640.
     of-flight range camera for intelligent vehicle safety applications,” in      [41] Y. Xiang, W. Choi, Y. Lin, and S. Savarese, “Data-driven 3d Voxel
     Advanced Microsystems for Automotive Applications 2006. Springer,                 Patterns for object category recognition,” in 2015 IEEE Conference on
     2006, pp. 205–219.                                                                Computer Vision and Pattern Recognition (CVPR), Jun. 2015, pp. 1903–
                                                                                       1911.
[20] O. Elkhalili, O. M. Schrey, W. Ulfig, W. Brockherde, B. J. Hosticka,
     P. Mengel, and L. Listl, “A 64× 8 pixel 3-D CMOS time of flight              [42] F. Chabot, M. Chaouch, J. Rabarisoa, C. Teulire, and T. Chateau, “Deep
     image sensor for car safety applications,” in 2006 Proceedings of the             MANTA: A Coarse-to-Fine Many-Task Network for Joint 2d and 3d
     32nd European Solid-State Circuits Conference. IEEE, 2006, pp. 568–               Vehicle Analysis from Monocular Image,” in 2017 IEEE Conference
     571.                                                                              on Computer Vision and Pattern Recognition (CVPR), Jul. 2017, pp.
                                                                                       1827–1836.
[21] Sony IMX390CQV CMOS Image sensor for Automotive
                                                                                  [43] X. Chen, K. Kundu, Y. Zhu, A. G. Berneshawi, H. Ma, S. Fidler,
     Cameras. [Online]. Available: https://www.sony.net/SonyInfo/News/
                                                                                       and R. Urtasun, “3d Object Proposals for Accurate Object Class
     Press/201704/17-034E/index.html
                                                                                       Detection,” in Advances in Neural Information Processing Systems
[22] Q. Chen, X. Yi, B. Ni, Z. Shen, and X. Yang, “Rain removal via residual           28, C. Cortes, N. D. Lawrence, D. D. Lee, M. Sugiyama,
     generation cascading,” in 2017 IEEE Visual Communications and Image               and R. Garnett, Eds. Curran Associates, Inc., 2015, pp. 424–
     Processing (VCIP), Dec 2017, pp. 1–4.                                             432. [Online]. Available: http://papers.nips.cc/paper/5644-3d-object-
[23] Velodyne HDL-64E Lidar Specification. [Online]. Available: http:                  proposals-for-accurate-object-class-detection.pdf
     //velodynelidar.com/hdl-64e.html                                             [44] C. C. Pham and J. W. Jeon, “Robust object proposals re-ranking
[24] Velodyne VLS-128 Announcement Article. [Online]. Avail-                           for object detection in autonomous driving using convolutional neural
     able: http://www.repairerdrivennews.com/2018/01/02/velodyne-leading-              networks,” Signal Processing: Image Communication, vol. 53, pp.
     lidar-price-halved-new-high-res-product-to-improve-self-driving-cars/             110–122, Apr. 2017. [Online]. Available: http://www.sciencedirect.com/
[25] Leddar Solid-State Lidar technology. [Online]. Available: https:                  science/article/pii/S0923596517300231
     //leddartech.com/technology-fundamentals/                                    [45] Y. Xiang, W. Choi, Y. Lin, and S. Savarese, “Subcategory-Aware
[26] Y. Park, S. Yun, C. S. Won, K. Cho, K. Um, and S. Sim, “Calibration               Convolutional Neural Networks for Object Proposals and Detection,”
     between color camera and 3D LIDAR instruments with a polygonal                    in 2017 IEEE Winter Conference on Applications of Computer Vision
     planar board,” Sensors, vol. 14, no. 3, pp. 5333–5353, 2014.                      (WACV), Mar. 2017, pp. 924–933.
[27] R. Ishikawa, T. Oishi, and K. Ikeuchi, “LiDAR and Camera                     [46] G. Payen de La Garanderie, A. Atapour Abarghouei, and T. P. Breckon,
     Calibration using Motion Estimated by Sensor Fusion Odometry,”                    “Eliminating the blind spot: Adapting 3d object detection and monocular
     CoRR, vol. abs/1804.05178, 2018. [Online]. Available: http://arxiv.org/           depth estimation to 360 panoramic imagery,” in The European Confer-
     abs/1804.05178                                                                    ence on Computer Vision (ECCV), September 2018.
[28] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, “ImageNet:     [47] H. Su, S. Maji, E. Kalogerakis, and E. Learned-Miller, “Multi-view
     A Large-Scale Hierarchical Image Database,” in 2009 IEEE Conference               Convolutional Neural Networks for 3d Shape Recognition,” in 2015
     on Computer Vision and Pattern Recognition (CVPR), 2009.                          IEEE International Conference on Computer Vision (ICCV), Dec. 2015,
[29] A. Geiger, P. Lenz, and R. Urtasun, “Are We Ready for Autonomous                  pp. 945–953.
     Driving? The KITTI vision benchmark suite,” in 2012 IEEE Conference          [48] B. Li, T. Zhang, and T. Xia, “Vehicle Detection from 3d Lidar Using
     on Computer Vision and Pattern Recognition (CVPR). IEEE, 2012, pp.                Fully Convolutional Network,” in Proceedings of Robotics: Science and
     3354–3361.                                                                        Systems, AnnArbor, Michigan, Jun. 2016.
IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS                                                                                                     14

[49] F. N. Iandola, M. W. Moskewicz, K. Ashraf, S. Han, W. J. Dally,            [69] C. Redondo-Cabrera, R. J. López-Sastre, Y. Xiang, T. Tuytelaars,
     and K. Keutzer, “Squeezenet: AlexNet-level accuracy with 50x fewer              and S. Savarese, “Pose estimation errors, the ultimate diagnosis,” in
     parameters and <1mb model size,” CoRR, vol. abs/1602.07360, 2016.               European Conference on Computer Vision ECCV, 2016, pp. 118–134.
     [Online]. Available: http://arxiv.org/abs/1602.07360                       [70] C. Guo, G. Pleiss, Y. Sun, and K. Q. Weinberger, “On Calibration of
[50] S. L. Yu, T. Westfechtel, R. Hamada, K. Ohno, and S. Tadokoro, “Vehicle         Modern Neural Networks,” CoRR, vol. abs/1706.04599, 2017. [Online].
     detection and localization on bird’s eye view elevation images using            Available: http://arxiv.org/abs/1706.04599
     convolutional neural network,” in 2017 IEEE International Symposium
     on Safety, Security and Rescue Robotics (SSRR), Oct. 2017, pp. 102–
     109.
[51] J. Beltrán, C. Guindel, F. M. Moreno, D. Cruzado, F. Garcı́a, and
     A. de la Escalera, “BirdNet: a 3D Object Detection Framework               Eduardo Arnold is a PhD candidate with the Warwick Manufacturing Group
     from LiDAR information,” CoRR, vol. abs/1805.01195, 2018. [Online].        (WMG) at University of Warwick, UK. He completed his B.S. degree in
     Available: http://arxiv.org/abs/1805.01195                                 Electrical Engineering at Federal University of Santa Catarina (UFSC), Brazil,
[52] J. Redmon and A. Farhadi, “YOLO9000: Better, Faster, Stronger,” in         in 2017. He was also an exchange student at University of Surrey through
     2017 IEEE Conference on Computer Vision and Pattern Recognition            the Science without Borders program in 2014. His research interests include
     (CVPR), July 2017, pp. 6517–6525.                                          machine learning, computer vision, connected and autonomous vehicles.
[53] D. Feng, L. Rosenbaum, and K. Dietmayer, “Towards Safe Autonomous
     Driving: Capture Uncertainty in the Deep Neural Network For Lidar          Omar Y. Al-Jarrah received the B.S. degree in Computer Engineering
     3D Vehicle Detection,” CoRR, vol. abs/1804.05132, 2018. [Online].          from Yarmouk University, Jordan, in 2005, the MSc degree in Engineering
     Available: http://arxiv.org/abs/1804.05132                                 from The University of Sydney, Sydney, Australia in 2008 and the Ph.D.
[54] B. Li, “3d fully convolutional network for vehicle detection in point      degree in Electrical and Computer Engineering from Khalifa University, UAE,
     cloud,” in 2017 IEEE/RSJ International Conference on Intelligent Robots    in 2016. Omar has worked as a postdoctoral fellow in the Department of
     and Systems (IROS), Sep. 2017, pp. 1513–1518.                              Electrical and Computer Engineering, Khalifa University, UAE, and currently
[55] M. Engelcke, D. Rao, D. Z. Wang, C. H. Tong, and I. Posner,                he works as a research fellow at WMG, The University of Warwick, U.K. His
     “Vote3deep: Fast object detection in 3d point clouds using efficient       main research interest involves machine learning, connected and autonomous
     convolutional neural networks,” in 2017 IEEE International Conference      vehicles, intrusion detection, big data analytics, and knowledge discovery
     on Robotics and Automation (ICRA), May 2017, pp. 1355–1361.                in various applications. He has authored/co-authored several publications on
[56] R. Q. Charles, H. Su, M. Kaichun, and L. J. Guibas, “PointNet: Deep        these topics. Omar has served as TPC member of several conferences, such
     Learning on Point Sets for 3d Classification and Segmentation,” in 2017    as IEEE Globecom 2018. He was the recipient of several scholarships during
     IEEE Conference on Computer Vision and Pattern Recognition (CVPR),         his undergraduate and graduate studies.
     Jul. 2017, pp. 77–85.
[57] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and J. Xiao, “3d      Mehrdad Dianati is a Professor of Autonomous and Connected Vehicles at
     ShapeNets: A deep representation for volumetric shapes,” in 2015 IEEE      Warwick Manufacturing Group (WMG), University of Warwick, as well as, a
     Conference on Computer Vision and Pattern Recognition (CVPR), Jun.         visiting professor at 5G Innovation Centre (5GIC), University of Surrey, where
     2015, pp. 1912–1920.                                                       he was previously a Professor. He has been involved in a number of national
[58] D. Maturana and S. Scherer, “VoxNet: A 3d Convolutional Neural Net-        and international projects as the project leader and work-package leader in
     work for real-time object recognition,” in 2015 IEEE/RSJ International     recent years. Prior to his academic endeavour, he have worked in the industry
     Conference on Intelligent Robots and Systems (IROS), Sep. 2015, pp.        for more than 9 years as senior software/hardware developer and Director of
     922–928.                                                                   R&D. He frequently provide voluntary services to the research community in
[59] C. R. Qi, L. Yi, H. Su, and L. J. Guibas, “PointNet++: Deep Hierarchical   various editorial roles; for example, he has served as an associate editor for
     Feature Learning on Point Sets in a Metric Space,” in Advances in Neural   the IEEE Transactions on Vehicular Technology, IET Communications and
     Information Processing Systems 30. Curran Associates, Inc., 2017, pp.      Wiley’s Journal of Wireless Communications and Mobile.
     5099–5108.
[60] Y. Wang, Y. Sun, Z. Liu, S. E. Sarma, M. M. Bronstein, and                 Saber Fallah is a Senior Lecturer (Associate Professor) at the University of
     J. M. Solomon, “Dynamic Graph CNN for Learning on Point                    Surrey, a past Research Associate and Postdoctoral Research Fellow at the
     Clouds,” CoRR, vol. abs/1801.07829, 2018. [Online]. Available:             Waterloo Centre for Automotive Research (WatCar), University of Waterloo,
     http://arxiv.org/abs/1801.07829                                            Canada, and a past Research Assistant at the Concordia Centre for Advanced
[61] M. M. Bronstein, J. Bruna, Y. LeCun, A. Szlam, and P. Vandergheynst,       Vehicle Engineering (CONCAVE), Concordia University, Montreal, Canada.
     “Geometric deep learning: going beyond euclidean data,” IEEE Signal        Currently, he is the director of Connected Autonomous Vehicles (CAV) lab
     Processing Magazine, vol. 34, no. 4, pp. 18–42, 2017.                      and leading and contributing to several CAV research activities funded by
[62] Y. Zhou and O. Tuzel, “VoxelNet: End-to-End Learning for Point             the UK and European governments (e.g. EPSRC, Innovate UK, H2020) in
     Cloud Based 3D Object Detection,” CoRR, vol. abs/1711.06396, 2017.         collaboration with companies active in this domain. Dr Fallah’s research
     [Online]. Available: http://arxiv.org/abs/1711.06396                       has contributed significantly to the state-of-the-art research in the areas of
[63] C. R. Qi, W. Liu, C. Wu, H. Su, and L. J. Guibas, “Frustum PointNets       connected autonomous vehicles and advanced driver assistance systems.
     for 3D Object Detection From RGB-D Data,” in 2018 IEEE Conference
     on Computer Vision and Pattern Recognition (CVPR), June 2018.              David Oxtoby has received a BEng degree in Electronic Engineering from the
[64] X. Chen, H. Ma, J. Wan, B. Li, and T. Xia, “Multi-View 3D Object           University of York, UK in 1993. He worked in the field of telecommunication
     Detection Network for Autonomous Driving,” in 2017 IEEE Conference         for Nortel Networks from 1993-2002 before making a career change into
     on Computer Vision and Pattern Recognition (CVPR), 2017.                   Automotive in 2003, first working for Nissan on audio/navigation, telephone
[65] J. Schlosser, C. K. Chow, and Z. Kira, “Fusing LIDAR and images            and camera systems. Since 2013 he has been working for Jaguar Land Rovers
     for pedestrian detection using convolutional neural networks,” in 2016     Electrical Research team on a wide variety of projects and is now responsible
     IEEE International Conference on Robotics and Automation (ICRA),           for a team delivering new Electrical technologies from initial idea to concept
     May 2016, pp. 2198–2205.                                                   ready for production.
[66] T.-Y. Lin, P. Dollar, R. Girshick, K. He, B. Hariharan, and S. Belongie,
     “Feature Pyramid Networks for Object Detection,” in Proceedings of the     Alex Mouzakitis is the head of the Electrical, Electronics and Software
     IEEE Conference on Computer Vision and Pattern Recognition, 2017,          Engineering Research Department at Jaguar Land Rover. Dr Mouzakitis has
     pp. 2117–2125.                                                             over 15 years of technological and managerial experience especially in the area
[67] X. Du, M. H. Ang, S. Karaman, and D. Rus, “A general                       of automotive embedded systems. In his current role is responsible for leading
     pipeline for 3d detection of vehicles,” in 2018 IEEE International         a multidisciplinary research and technology department dedicated to deliver
     Conference on Robotics and Automation, ICRA 2018, Brisbane,                a portfolio of advanced research projects in the areas of human-machine in-
     Australia, May 21-25, 2018, 2018, pp. 3194–3200. [Online]. Available:      terface, digital transformation, self-learning vehicle, smart/connected systems
     https://doi.org/10.1109/ICRA.2018.8461232                                  and onboard/off board data platforms. In his previous position within JLR,
[68] M. Everingham, L. Van Gool, C. K. Williams, J. Winn, and A. Zisser-        Dr Mouzakitis served as the head of the Model-based Product Engineering
     man, “The Pascal Visual Object Classes (VOC) challenge,” International     department responsible for model-based development and automated testing
     journal of computer vision, vol. 88, no. 2, pp. 303–338, 2010.             standards and processes.
