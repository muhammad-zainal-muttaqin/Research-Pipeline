---
source_id: 154
bibtex_key: lopes2022rgbddatasets
title: A Survey on RGB-D Datasets
year: 2022
domain_theme: Fusi Multimodal
verified_pdf: 154_Survei Dataset RGB-D (Lopes dkk.).pdf
char_count: 266114
---

Final Open Access Version at: https://doi.org/10.1016/j.cviu.2022.103489
                                                                                                                                                                                        1

                                                                                      Computer Vision and Image Understanding
                                                                                              journal homepage: www.elsevier.com

                                        A survey on RGB-D datasets

                                        Alexandre Lopesa,∗∗, Roberto Souzab,c , Helio Pedrinia
                                        a Institute of Computing, University of Campinas, Brazil
                                        b Department of Electrical and Computer Engineering, University of Calgary, Canada
                                        c Hotchkiss Brain Institute, University of Calgary, Canada
arXiv:2201.05761v2 [cs.CV] 8 Aug 2022

                                            ABSTRACT

                                           RGB-D data is essential for solving many problems in computer vision. Hundreds of public RGB-D
                                           datasets containing various scenes, such as indoor, outdoor, aerial, driving, and medical, have been
                                           proposed. These datasets are useful for different applications and are fundamental for addressing
                                           classic computer vision tasks, such as monocular depth estimation. This paper reviewed and catego-
                                           rized image datasets that include depth information. We gathered 231 datasets that contain accessible
                                           data and grouped them into three categories: scene/objects, body, and medical. We also provided
                                           an overview of the different types of sensors, depth applications, and we examined trends and future
                                           directions of the usage and creation of datasets containing depth data, and how they can be applied to
                                           investigate the development of generalizable machine learning models in the monocular depth estima-
                                           tion field.
                                                                                                        © 2022 Elsevier Ltd. All rights reserved.

                                        1. Introduction                                                                 tups. Also, it can be applied to existing monocular systems, that
                                                                                                                        comprise the majority of image capturing systems available.
                                           Depth is a critical information for many computer vision and                 For instance, Light Detection And Ranging (LiDAR) scanners
                                        image analysis applications. For example, it has been applied                   usually cost thousands of dollars, and their cost and weight can
                                        for tasks such as synthetic object insertion in computer graph-                 be impractical for many small drone applications.
                                        ics (Luo et al., 2020), robotic grasping (Lenz et al., 2015) au-                   As a result of the extensive range of applications of depth, a
                                        tomatic 2D to 3D conversion in film (Xie et al., 2016), robot-                  considerable number of datasets include distance measurements
                                        assisted surgery (Stoyanov et al., 2010), and autonomous driv-                  of points of the scene they acquire. These datasets are collected
                                        ing (Levinson et al., 2011).                                                    using different sensors in distinct scenes for applications such
                                           Despite using depth sensors that capture the distance infor-                 as Simultaneous Localization and Mapping (SLAM) (Sturm
                                        mation, researchers also use stereo vision matching to infer it,                et al., 2012), Reconstruction (Dai et al., 2017), Object Segmen-
                                        especially for its condensed size and cost. Lately, deep learn-                 tation (McCormac et al., 2017), and Human Activity Recogni-
                                        ing methods are being used to produce more precise and dense                    tion (Zhang et al., 2016a). With the increasing number and di-
                                        depth maps. For example, they can improve finer-grained de-                     versity of datasets, researchers were able to explore more gener-
                                        tails (Miangoleh et al., 2021), produce dense maps from sparse                  alistic forms of depth estimation, leading to techniques focused
                                        inputs (Uhrig et al., 2017), and refine depth for mirror sur-                   on zero-shot cross-dataset depth estimation (Li and Snavely,
                                        faces (Tan et al., 2021a).                                                      2018a; Xian et al., 2020a; Ranftl et al., 2021a, 2020). The idea
                                           An important field of study for depth is monocular depth es-                 is to produce powerful methods able to estimate depth for in-
                                        timation, especially because it does not require using depth sen-               the-wild scenes, increasing the range of applications for depth
                                        sors, reducing the size and cost of computer vision systems’ se-                estimation.
                                                                                                                           The main contribution of this paper is to categorize and sum-
                                          ∗∗ Corresponding author.
                                                                                                                        marize the existing datasets with depth data. We propose a
                                           e-mail: alexandre.lopes@ic.uncamp.br (Alexandre Lopes),
                                                                                                                        survey that can be used by researchers of both individual ap-
                                        roberto.medeirosdeso@ucalgary.ca (Roberto Souza),                               plications and general systems. While there are good reviews
                                        pedrini@unicamp.br (Helio Pedrini)                                              of RGB-D datasets (Firman, 2016; Cai et al., 2017), the most
                                                                                                                                       2

recent one was published in 2017, and datasets have evolved          information, it is possible to create a triangle and calculate the
both in complexity and size since then. Our survey presents          height of the triangle formed by the camera, projector, and illu-
a comprehensive literature review on more than 200 publicly          minated scene point to determine the distance. The strategy of
available datasets included from an initial list of more than 300    projecting points would be slow in practice since it is necessary
datasets. Nearly half of the public datasets were published in       to project a point for every position that is represented as a pixel
2017 or after, therefore, not included in any other review. We       in the image.
also made this work available on a website1 to facilitate the fil-      A more efficient strategy is to project the light as a stripe
tering by application, scene type, sensor, and year.                 that associated with different coding strategies, such as the Bi-
   The remainder of this paper is structured as follows. In the      nary Coded Structured Light strategy, can reduce the number
next section, we discuss and categorize depth sensors, explain-      of frames necessary to produce a full depth map. It can also
ing the main differences and applications for each category. In      be coded with RGB lights. Details about different codification
Section 3, we present the methodology used to perform the liter-     strategies are discussed by Salvi et al. (2004).
ature review. In Section 4, we present the datasets divided into        Most Structured Light sensors do not work under direct sun-
categories, describing the most influential datasets for each cat-   light since they rely on light projection in a scene. There-
egory and presenting the rest in tables. In Section 5, we present    fore, they are usually suitable for indoor scene applications.
tendencies and discuss future directions for RGB-D data usage.       Researchers have proposed strategies to overcome challenging
Finally, we provide a summary of the field and discuss how the       light conditions (O’Toole et al., 2015), and now these sensors
area is evolving in Section 6.                                       appear in smartphones for face identification systems for both
                                                                     indoor and outdoor scenes. They typically have a low range
                                                                     limit, not going further than 10 meters. Examples of this type
2. Sensors
                                                                     of sensor include Matterport, Kinect v1, and RealSense SR300
   Range (or depth) data is crucial for understanding the 3D         cameras.
scene projected onto a 2D plane forming an image. There are
multiple ways to obtain such information, either using a depth       2.2. Time-of-Flight
sensor or estimating depth. A depth sensor is a device that pro-        TOF sensors estimate the distance of an object in the scene
vides the distance from the sensor to an element in the scene, al-   to a sensor by measuring the time it takes for an emitted light
though it is possible to collect distance information using two or   to be received by the sensor. Therefore, TOF sensors rely on
more RGB cameras from a scene. We define as Stereo Camera            the time that a light wave takes to go to a point in a scene and
Sensing, all systems formed by two or more cameras. There-           to be reflected to a sensor. The concept is barely the same as
fore, light field cameras are also included here.                    the Ultrasonic and Radar Sensors, but here light is used as the
   Previously, authors proposed distinct divisions for the types     emitted signal.
of sensors (Fisher and Konolige, 2008; Choi, 2019). In this sur-        There are multiple strategies for capturing the time-of-flight
vey, we use a categorization of depth sensors inspired by Choi       of light. The most straightforward strategy is using a technique
(2019)’s work. We divide the sensors into the following cat-         called Pulse Modulation, where a very fast pulse of light is
egories: Structured Light, Time-of-Flight (TOF), Light Detec-        emitted and then received by the sensor. The time delay be-
tion and Ranging (LiDAR), and Stereo Camera Sensing. We              tween the emitted light pulse and the received light pulse is used
display examples of each category in Figure 1.                       to compute the distance of the object in the scene. Continuous-
   Ultrasonic and Radar sensors also produce distance informa-       Wave Modulation is another strategy, where the light is mod-
tion, but they are out of the scope of this work because they        ulated by its intensity, and the distance is measured by calcu-
are rarely used to produce depth information associated with         lating the shift in phase of the original emitted light and the
RGB data. We detail each one of the sensors categories in the        received light.
following sub-sections and show the differences of these types          TOF sensors generally are compromised under strong sun-
and possible application scenes in Table 1.                          light conditions (Kazmi et al., 2012), making this sensor more
                                                                     commonly applied to indoor scenes. Existing studies try to
2.1. Structured Light                                                overcome the effect under intense background light (Buttgen
   Structured Light sensors (also called Active Stereo sensors)      and Seitz, 2008) and to reduce the measurement uncertainty
rely on a projector of light captured by a camera. The simplest      under such conditions. Examples of this type of sensor include
way to achieve such a goal is to project a point with a device       Kinect v2 (Xbox One sensor), SoftKinetic DS 325, and RIEGL
and capture this point in the scene with the camera. The depth       VZ-400.
of this point can be measured by a technique called Triangula-
tion. For estimating depth, it is necessary to find the position     2.3. LiDAR
of the projected point in the image plane, have the distance be-       LiDAR sensors use the same idea of measuring the time that
tween the camera and the light projector, the camera’s internal      an emitted light is received by a sensor, but they rely on one
parameters, and the position in space of the projector. With this    or multiple laser beams (concentrated light) to produce depth
                                                                     measurements of points in the scene, and the device usually
                                                                     has a rotating mirror to generate 360° scans of a scene. Hence,
  1 www.alexandre-lopes.com/rgbd-datasets                            LiDAR sensors produce point clouds of a scene, not a dense
                                                                                                                                                  3
                        Table 1: Sensors overview comparing the usual application, distances and sparsity for each type of sensor.

              Type                       Typical Application Scenes                         Typical Distance Usage                    Sparsity
         Structured Light                           Indoor                                  Close Distances (0-10m)                  Dense Map
               TOF                                  Indoor                                  Close Distances (0-10m)                  Dense Map
              LiDAR                     Aerial, Street, Outdoor, Indoor               Medium/Large Distances (10-1000m)              Sparse Map
      Stereo Camera Sensing                Street, Outdoor, Indoor                     Close/Medium Distances (0-100m)               Dense Map

depth map of it. They rely on focused laser beams, which allow                 depth with acceptable accuracy without the correspondence of
them to collect distance measurements as far as a few kilome-                  the pixels in both image planes. Recently, Deep Learning based
ters. LiDAR sensor models have different specifications (e.g.,                 methods have tried to address this limitation, increasing the ac-
resolution, scans per second, and distance accuracy), and some                 curacy of the estimation (Zbontar and LeCun, 2015). Examples
scans are built in a multilayer (multiple laser beams) configura-              of such types of sensors include light field cameras and ZED
tion, allowing them to measure not only in a 360° plane of the                 cameras.
sensor but in 3D.
   LiDAR measurement accuracy is usually independent of dis-
tance, although some models can fail in adverse weather con-                   3. Methodology
ditions, such as dense fogs and turbulent snow (Jokela et al.,
                                                                                  A literature review should synthesize previous knowledge,
2019). Each LiDAR point also includes the intensity measure-
                                                                               identify biases and gaps in the literature (Rowe, 2014). Since
ments, which can be interpreted as a measurement of reflec-
                                                                               our study aims to describe, categorize, and identify future
tivity of the point that the light hit. This value is suitable for
                                                                               trends for RGB-D datasets, we defined a non-conventional
many applications, such as vegetation cover understanding and
                                                                               methodology to find the related papers. Instead of defining
tunnel damage detection (Kashani et al., 2015), giving LiDAR
                                                                               search terms to find the papers directly, we collected datasets
additional information that other types of sensors do not pro-
                                                                               using backward snowballing. The premise is that many datasets
duce.
                                                                               containing depth data do not have depth estimation as their pri-
   LiDAR sensors emit light; therefore, they work in difficult
                                                                               mary goal, as in KITTI Dataset (Geiger et al., 2013). There-
lighting conditions, such as dark environments. They are suit-
                                                                               fore, defining search strings that could find depth datasets us-
able for indoor and outdoor application scenes, but the avail-
                                                                               ing generalist terms would result in numerous false-positive re-
able models are usually limited to specific applications, such as
                                                                               sults. For instance, the search string RGB-D OR Depth AND
aerial measurements, outdoor/driving applications, and small
                                                                               Dataset searching in abstract, keywords, or title brings more
indoor spaces depth estimation. Examples of such types of sen-
                                                                               than 23 thousand results in Scopus. Moreover, if we define a
sors include Velodyne Sensors, Faro Focus 3D Laser, and SICK
                                                                               complex composed search string to filter the results, we would
LMS-511.
                                                                               miss many datasets in the search.
                                                                                  As monocular depth estimation, salient object detection, and
2.4. Stereo Camera Sensing                                                     action recognition are prominent fields in the area, we defined
   We define here Stereo Camera Sensing (SCS) as any sys-                      the following search string to perform backward snowballing:
tem formed by two or more image sensors or lenses used to                      (("single image" OR monocular) AND depth AND
produce a Depth Map of a scene. Hence, simplistic pairs of                     estimation) OR (("Salient Object Detection" OR
cameras and complex light field systems composed by multiple                   "Action Recognition") AND RGB-D). The terms “monoc-
microlenses are both identified in the same category. A straight-              ular” and “single image” are applied mainly for monocular
forward strategy to measure depth from two or more cameras is                  depth estimation but are also used for stereo trained systems,
Triangulation. The Triangulation idea is the same as applied in                depth completion, and other applications. We conducted the re-
Structured Light sensors, but using a camera instead of a projec-              view in Scopus and Google Scholar search engines. In Scopus,
tor. The idea is that finding the position of a pixel in the image             we revised all papers from January 1st, 2016, through August
plane of camera A projected from a point P in the space, and                   31st, 2021. From Google Scholar, we followed the same dates,
the position of a pixel projected by the same point P in camera                but we also included a stop criterion. If we found one search
B, it is possible to find the depth of that point in a scene with              page without relevant items, we would end the year’s search.
the intrinsic parameters of the camera. After finding both lines               The inclusion of Google Scholar is justified because many
projected in both cameras from point P, it is only necessary to                relevant papers are published in arXiv. Consequently, those
know the distance between the two cameras (baseline distance)                  could also be included in this work.
and internal parameters of the cameras to know the depth of the                   The exclusion and inclusion criteria for papers are defined in
point P.                                                                       Table 2. These criteria are applied to the papers found using the
   A limitation of this strategy occurs when the point of interest             previous search term. After excluding papers, backward snow-
has no texture. For instance, it is practically impossible to deter-           balling was applied to find the datasets used/described by the
mine which point of a smooth painted wall observed in the im-                  remaining works. Initially, we reviewed 2,119 papers, which
age projected by camera A is equivalent to the image projected                 led to 374 dataset candidates. We also applied an exclusion cri-
by camera B. Therefore, it is difficult to determine a point’s                 terion to these candidates, and only papers with active project
                                                                                                                                         4

                               (a)                            (b)                   (c)                      (d)

Fig. 1: Examples of depth data with image (first row) and depth (second row) of the following sensors: (a) Structured Light from
NYUv2 (Silberman et al., 2012), (b) TOF from AVD (Ammirato et al., 2017), (c) LiDAR from KITTI (Geiger et al., 2013), and (d)
Stereo Camera Sensing from ReDWeb (Xian et al., 2018), where the authors compute correspondence maps by using optical flow.

                 Table 2: Inclusion and Exclusion Criteria.                4.1. Scene/Objects
                                                                              In this category, we grouped all datasets generally intended
                         Criterion                             Category
                                                                           to expose scenes, individual objects, or groups of objects con-
            Papers that discuss depth estimation               Inclusion   taining or not humans.. Therefore, datasets that reconstruct
          Papers using depth sensors, stereo image
                  sensing, or synthetic data
                                                               Inclusion   scenes/objects, segment elements of a scene, salient objects
                Papers not written in English                  Exclusion   using depth, and contain exclusively depth maps are sub-
          Papers exclusively using private datasets            Exclusion   categorized here. We created an “Other” sub-category to ac-
   Papers not presenting minimal evidence of valid results     Exclusion   commodate datasets that did not fit into these previous sub-
   Duplicated paper/report. We kept the most complete one      Exclusion
                                                                           categories.
                                                                              Some papers explore multiple applications, primarily syn-
                                                                           thetic datasets, since they can create reconstruction and seg-
websites, contact information to download the dataset, or direct
                                                                           mentation data directly using simulation environments. These
download link were included. Hence, the final list of datasets
                                                                           papers are presented in one of their application areas to reduce
to be included was reduced to 231 datasets.
                                                                           redundancy. The only exception is for datasets of “SLAM,
                                                                           Odometry, or Reconstruction” and “Segmentation or Other Ex-
4. Datasets                                                                tra Information” sub-categories that are presented together in
                                                                           Table 5, since this combination is very frequent for datasets.
   In recent years, many datasets have been created using the
sensors or stereo vision sensing presented in the previous sec-            4.1.1. SLAM, Odometry, or Reconstruction
tion. In addition to datasets using real data, this paper also in-            This sub-category contains multiple types of applications,
cludes datasets containing synthetic data. These were created              however, all of them have a common characteristic: they
mainly by simulation systems and often presented extra data                present extra information that makes possible to recreate in
such as semantic segmentation and 3D object detection bound-               any detail level, a 3D scene. For SLAM and odometry related
ing boxes. We divided the selected datasets into three different           papers, they typically present camera pose information, giv-
categories and six different sub-categories representing differ-           ing position and orientation of the capturing apparatus of each
ent application areas. The taxonomy tree is available in Fig-              frame/image. We treated odometry differently from SLAM
ure 2.                                                                     since odometry essentially aims to estimate the path of the cam-
   The categories represent the intended application of the                era, and SLAM tries to obtain a consistent trajectory and scene
dataset. In the first level, we identify datasets that are mainly          map of the camera (Yousif et al., 2015).
interested in Scenes/Objects, Human Body, or Medical Appli-                   All collected datasets that contain data exclusively for
cations. The following sub-sections explore each application               SLAM, Odometry, or Reconstruction are shown in Table 3.
area, and list all of them in each sub-category’s table. We also           In general, applications of indoor scenes focus on recon-
detail three, two or one datasets for each sub-category, based on          struction, and external scenes (such as driving scenes) focus
the total number of datasets of each sub-category. If we detail            on SLAM/odometry. Table 5 also contains datasets of this
three papers, the two first ones are the most cited papers that            sub-category, however, with extra annotated information such
contain complementary scenarios. For example, KITTI Dataset                as semantic segmentation data. Some of the most cited datasets
and ScanNet Dataset contain street and indoor scenes, respec-              in the field include:
tively. The third paper is the most cited paper published in 2017
or later. If we detail two papers, these are the most cited ones              KITTI Dataset. Analyzing the datasets presented in this pa-
that contain complementary scenarios, and if we detailed one               per, this is the most cited one. The KITTI Dataset consists of
paper, it is the most cited in the sub-category.                           a complex system of IMU/GPS, LiDAR scanner, and multiple
                                                                                                                                          5

                                                                Dataset

                             Scene/Objects                          Body                           Medical

                                      SLAM, Odometry,                 Human Activities
                                      or Reconstruction
                                                                      Gestures (Partial body)
                                      Segmentation or Other
                                      Extra Information

                                      Depth Data Only

                                      Other

                                               Fig. 2: Taxonomy for RGB-D datasets.

cameras (Geiger et al., 2013). They recorded 6 hours of traf-          3D model scene (which can be related to reconstruction), with
fic scenes and, in addition to collecting the information from         semantic labels associated with it.
the sensors, provided data from 3D object detection bound-
ing boxes, optical flow, and visual odometry/SLAM (Geiger              4.1.2. Segmentation or Other Extra Information
et al., 2012). The project was expanded over the years, and               In this sub-category, all datasets have extra information that
the authors included data for tracking, road/lane detection, se-       leads to a better scene understanding. Extra information can be
mantic/instance segmentation, and depth completion. Its depth          seen as semantic or instance segmentation, 2D or 3D object de-
completion data is composed of 94 thousand depth annotated             tection, optical flow, salient object detection, etc. For instance,
RGB images (Uhrig et al., 2017) to produce dense depth maps            datasets that explore potential applications for depth estimation
from LiDAR points.                                                     algorithms and semantic segmentation, and datasets dedicated
   This dataset influenced the creation of the synthetic datasets      to salient object detection were categorized here.
Virtual KITTI (Gaidon et al., 2016) and Virtual KITTI                     The complete list of datasets containing extra information is
2 (Cabon et al., 2020). Recently, the KITTI authors released           available in Table 4. We provide the type of extra information
the KITTI-360 Dataset (Liao et al., 2021), which has more              for each dataset in the “Extra Data” column. Researchers
cameras, sensors, and more annotated data than the original            interested in a specific application, for instance, salient object
KITTI Dataset.                                                         detection, should use it to filter datasets related to their field of
                                                                       interest. Table 5 also reports datasets for this sub-category, as
   ScanNet Dataset. ScanNet is an indoor dataset collected             well as information of “SLAM, Odometry, or Reconstruction”
using an occipital structure sensor - a structured light sensor        sub-category. Therefore, researchers interested in semantic
similar to Microsoft Kinect v1 (Dai et al., 2017). The au-             segmentation datasets may check both tables and refer to
thors performed a dense reconstruction and conducted object            the “Extra Data” column to find the datasets that match their
instance-level annotation of all surfaces in the reconstruction.       interest. Next, three of the most influencing and promising
They also conducted a CAD Model Retrieval and Alignment                papers for this sub-category are presented.
for the objects in the scenes, which means that a 3D CAD
model represented each instance of the annotated object in a             NYUv2. This dataset contains indoor images and is the
scene. This dataset contains 2.5M views in 2,119 different             most cited dataset for this type of scene in the “Segmentation
scenes.                                                                or Other Extra Information” sub-category. It was collected
                                                                       using Microsoft Kinect v1 sensor and is composed of aligned
   SunCG Dataset. The project associated with this dataset             RGB and depth images, labeled data containing semantic
is focused on semantic scene completion, where from a single           segmentation, and raw data (Silberman et al., 2012). This
point of view, it estimates a complete 3D representation with          project is a continuation of NYUv1 (Silberman and Fergus,
the semantic label associated with the scene (Song et al., 2017).      2011), which uses the same sensor and type of data, but has
Instead of estimating the semantic segmentation of visible sur-        fewer scenes and total frames.
faces, this project aims to predict the occluded space (3D scene
representation) and a label for each voxel in the scene. There-           Scene Flow Datasets. This dataset is a collection of
fore, it deals with Reconstruction and Segmentation as a unified       three datasets: FlyingThing3D, Monkaa, and Driving. The
task. This dataset comprises synthetic data containing an entire       first is composed of everyday objects flying along random
                                                                                                                                                                                                   6
                                                        Table 3: Datasets of “SLAM, Odometry, or Reconstruction” sub-category

Dataset Name           Ref.                             Year   Scene Type           Sensor Type          Sensor Name              Data Modalities      Extra Data           Images/Scenes
                                                                                                                                                                            543 Scenes (125623
GL3D                   Shen et al. (2018)               2018   Aerial               SCS                  Stereo Camera            Color, Depth         -
                                                                                                                                                                            Images)
                                                                                                         Velodyne HDL-64E         Color, Depth, GPS,                        155 Min With 93k
ApolloScape            Wang et al. (2019b)              2020   Driving              LiDAR                                                              -
                                                                                                         S3                       Radar                                     Frames
                                                                                                         Velodyne VLP-16, SICK    Color, Depth, GPS,                        19 Sequences (191
KAIST                  Jeong et al. (2019)              2019   Driving              SCS, LiDAR                                                         -
                                                                                                         LMS-511, Stereo Camera   IMU, Altimeter                            Km)
                                                                                                                                  Color, Deph, GPS,
                                                                                                         2 X SICK LMS-151 2D                                                133 Scenes (almost
                                                                                                                                  INS (Inertial
RobotCar               Maddern et al. (2017)            2016   Driving              LiDAR                LiDAR, 1 X SICK                               -                    20M Images (from
                                                                                                                                  Navigation
                                                                                                         LD-MRS 3D LiDAR                                                    Multiple Sensors)
                                                                                                                                  System)
                                                                                                         2 SICK LMS, 3 HOKUYO,    Color, Depth, IMU,
Malaga Urban           Blanco-Claraco et al. (2014)     2014   Driving              SCS, LiDAR                                                         -                    15 Sequences
                                                                                                         Stereo Camera            GPS
                                                                                                         Velodyne HDL-64E,                                                  152 Scenes (12607
Omniderectional        Schönbein et al. (2014)         2014   Driving              SCS, LiDAR                                    Color, Depth         -
                                                                                                         Stereo Camera                                                      Frames)
Ford Campus Vision                                                                                       Velodyne HDL-64E,        Color, Depth, IMU,
                       Pandey et al. (2011)             2011   Driving              SCS, LiDAR                                                         -                    2 Sequences
And LiDAR                                                                                                Stereo Camera            GPS
                                                                                                                                                                            20 Sequences
Karlsruhe              Geiger et al. (2011)             2011   Driving              SCS                  Stereo Camera            Color, GPS/IMU       -
                                                                                                                                                                            (16657 Frames)
Multi-FoV (Urban
                       Zhang et al. (2016b)             2016   Driving, Indoor      -                    Synthetic                Color, Depth         -                    2 Sequences
Canyon )
                                                                                                                                                                            13 Scenes (5
–                      Zeisl et al. (2013)              2013   Driving, Outdoor     N/A                  RGB-D Scans (N/A)        Color, Depth         -                    Castle, 5 Church, 3
                                                                                                                                                                            Street Scenes)
                                                                                                                                                                            113 Scenes (17k
BlendedStereo Camera   Yao et al. (2020)                2020   In-the-wild          -                    Synthetic                Color, Depth         -
                                                                                                                                                                            Images)
                                                                                                         Two Points
                                                                                                                                  Color, Relative
Youtube3D              Chen et al. (2019)               2019   In-the-wild          -                    Automatically                                 -                    795066 Images
                                                                                                                                  Depth
                                                                                                         Annotated
                                                                                    Structured Light,    Kinect V1, V2 And                                                  10 Scenes (2703
–                      Malleson et al. (2019)           2019   In-the-wild                                                        Color, Depth         -
                                                                                    TOF                  Synthetic                                                          Frames)
4D Light Field                                                                                           Light-field
                       Honauer et al. (2016)            2016   In-the-wild          -                                             Color, Depth         -                    24 Scenes
Benchmark                                                                                                (Synthetic)
Habitat
                       Ramakrishnan et al. (2021)       2021   Indoor               Structured Light     Matterport Pro2          Color, Depth         -                    1000 Scenes
Matterport (HM3D)
                                                                                                         Intel D435i Depth,
                                                                                                                                                                            17 Distinct Floors
                                                                                    Structured Light,    Velodyne HDL-32E /       Radar, IMU, LiDAR,
MilliEgo               Lu et al. (2020)                 2020   Indoor                                                                                  -                    From 6 Different
                                                                                    LiDAR                Velodyne Ultra           Depth
                                                                                                                                                                            Multistorey
                                                                                                         Puck
                                                                                                         MiniPolar 360                                                      6 Indoor Areas
ODS                    Lai et al. (2019)                2019   Indoor               SCS                                           Color, Depth         Normal Maps
                                                                                                         Camera (Stereo Camera)                                             (50k Images)
                                                                                                                                                                            12072 Scanned
                                                                                                         Synthetic And
360D                   Zioulis et al. (2018)            2018   Indoor               Structured Light                              Color, Depth         -                    Scenes And 10024 CG
                                                                                                         Matterport Camera
                                                                                                                                                                            Scenes
                                                                                                                                                                            103 Scenes (25k
PanoSUNCG              Wang et al. (2018)               2018   Indoor               -                    Synthetic                Color, Depth         -
                                                                                                                                                                            Images)
                                                                                                                                                                            4 Scenes (9 Hours Of
CoRBS                  Wasenmüller et al. (2016)       2016   Indoor               TOF                  Kinect V2                Color, Depth         -
                                                                                                                                                                            Recording)
                                                                                                         Vicon Motion
EuRoC MAV              Burri et al. (2016)              2016   Indoor               TOF, Stereo Camera   Capture, Leica           Color, Depth, IMU    -                    11 Scenes
                                                                                                         MS50
Augmented                                                                                                                                                                   4 Scenes (2 Living
                       Choi et al. (2015)               2015   Indoor               -                    Synthetic                Color, Depth         -
ICL-NUIM                                                                                                                                                                    Room, 2 Offices)
                                                                                                         Kinect V1 And
Ikea                   Li et al. (2015)                 2015   Indoor               Structured Light                              Color, Depth         -                    7 Scenes
                                                                                                         PrimeSense
                                                                                                                                                       Semantic Category    5 Sequences (22454
ViDRILO                Martı́nez-Gómez et al. (2015)   2015   Indoor               Structured Light     Kinect V1                Color, Depth
                                                                                                                                                       of the Scene         Images)
                                                                                                                                                                            8 Scenes (4 Living
ICL-NUIM               Handa et al. (2014)              2014   Indoor               -                    Synthetic                Color, Depth         -
                                                                                                                                                                            Room, 4 Office)
                                                                                                                                                                            3 Scenes (9.5 Hours
MobileRGBD             Vaufreydaz and Nègre (2014)     2014   Indoor               TOF                  Kinect V2                Color, Depth         -
                                                                                                                                                                            Of Recording)
RGBD Object V2         Lai et al. (2014)                2014   Indoor               Structured Light     Kinect V1                Color, Depth         -                    14 Sequences
                                                                                                                                                                            40 Scenes (rooms
–                      Mattausch et al. (2014)          2014   Indoor               LiDAR                Faro Focus 3D Laser      Depth                -                    From Three
                                                                                                                                                                            Offices)
                                                                                                                                                                            7 Scenes (500-1000
RGB-D 7-Scenes         Glocker et al. (2013)            2013   Indoor               Structured Light     Kinect V1                Color, Depth         -
                                                                                                                                                                            Frames/scene)
Reading Room           Zhou et al. (2013)               2013   Indoor               Structured Light     Asus Xtion Pro Live      Color, Depth         -                    1 Scene
                                                                                                                                  Color, Depth,
TUM-RGBD               Sturm et al. (2012)              2012   Indoor               Structured Light     Kinect V1                                     -                    39 Sequences
                                                                                                                                  Accelerometer
IROS 2011 Paper
                       Pomerleau et al. (2011)          2011   Indoor               Structured Light     Kinect V1                Depth                -                    27 Sequences
Kinect
                                                               Indoor, Isolated
–                      Zhou and Koltun (2013)           2013   Objects / Focussed   Structured Light     Asus Xtion Pro Live      Color, Depth         -                    6 Scenes
                                                               On Objects
                                                                                                         KinectFusion
                                                               Indoor, Isolated
                                                                                    Structured Light,    (Kinect V1) For Two                                                2 Scenes: Statue
–                      Meister et al. (2012)            2012   Objects / Focussed                                                 Color, Depth         -
                                                                                    TOF                  Scenes. Riegl                                                      And Targetbox
                                                               On Objects
                                                                                                         VZ-400 For Office
                                                                                                                                                                            4690 Sequences
M&M                    Ren et al. (2020)                2020   Indoor, Outdoor      SCS                  Stereo Camera            Color, Depth         -                    (170k Frames) And
                                                                                                                                                                            130k Images
Mannequin                                                                                                                                                                   4690 Sequences
                       Li et al. (2019)                 2019   Indoor, Outdoor      SCS                  Stereo Camera            Color                -
Challenge                                                                                                                                                                   (170k Frames)
                                                                                                         Velodyne (LiDAR),
Stereo CameraEC        Zhu et al. (2018)                2018   Indoor, Outdoor      SCS, LiDAR                                    Color, Depth, IMU    -                    5 Sequences
                                                                                                         Stereo Camera
                                                                                                         FaroFocus X 330
                                                                                                                                                                            25 High-res, 10
ETH3D                  Schöps et al. (2017)            2017   Indoor, Outdoor      SCS, LiDAR           (Laser Sensor),          Color, Depth         -
                                                                                                                                                                            Low-res
                                                                                                         Stereo Camera
                                                                                                                                                                           Continue on Next Page
                                                                                                                                                                                             7
 Dataset Name         Ref.                             Year   Scene Type           Sensor Type         Sensor Name           Data Modalities     Extra Data   Images/Scenes
                                                              Isolated Objects /
 DiLigGent-MV         Li et al. (2020)                 2020   Focussed On          SCS                 Stereo Camera         Color               -            5 Objects (scenes)
                                                              Objects
                                                              Isolated Objects /
 A Large Dataset of                                                                                    PrimeSense                                             Over 10k 3D Scans
                      Choi et al. (2016)               2016   Focussed On          Structured Light                          Color, Depth        -
 Object Scans                                                                                          Carmine                                                Of Objects.
                                                              Objects
                                                              Isolated Objects /                                                                              9 Scenes: 4 Scenes
                                                                                   SCS, Structured     PrimeSense,
 –                    Zollhöfer et al. (2015)         2015   Focussed On                                                    Color, Depth        -            Using PrimeSense,
                                                                                   Light               Stereo Camera
                                                              Objects                                                                                         5 Scenes Using Stereo Camera
                                                              Isolated Objects /
                                                                                                       PrimeSense                                             600 Images (from
 BigBIRD              Singh et al. (2014)              2014   Focussed On          Structured Light                          Color, Depth        -
                                                                                                       Carmine 1.09                                           125 Objects)
                                                              Objects
                                                              Isolated Objects /
                                                                                                       Asus Xtion
 Fountain             Zhou and Koltun (2014)           2014   Focussed On          Structured Light                          Color, Depth        -            1 Scene
                                                                                                       Pro Live
                                                              Objects
                                                              Isolated Objects /
 MVS                  Jensen et al. (2014)             2014   Focussed On          SCS                 Stereo Camera         Color, Depth        -            124 Scenes
                                                              Objects
                                                                                                       Intel D435i,
                                                                                   Structured Light,
 The Newer College    Ramezani et al. (2020)           2020   Outdoor                                  Ouster OS-1           Color, Depth, IMU   -            6 Scenes
                                                                                   LiDAR
                                                                                                       (Gen 1) 64
 Megadepth            Li and Snavely (2018b)           2018   Outdoor              SCS                 Stereo Camera         Color, Depth        -            130k Images
 CVC-13:
                      Barrera Campo et al. (2012)      2013   Outdoor              SCS                 Stereo Camera         Color, Infrared     -            4 Scenes
 Multimodal Stereo
 Live Color+3D                                                                                         Range Scanner
                      Su et al. (2013)                 2011   Outdoor              TOF                                       Color, Depth        -            12 Scenes
 Database                                                                                              (RIEGL VZ-400)
                                                                                                       Custom-built 3-D
 Make3D               Saxena et al. (2009)             2009   Outdoor              TOF                                       Color, Depth        -            534 Images
                                                                                                       Scanner
 Fountain-P11 And                                                                                                                                             2 Scenes (19
                      Schöning and Heidemann (2015)   2008   Outdoor              LiDAR               N/A                   Color, Depth        -
 Herz-Jesu-P8                                                                                                                                                 Images)
                                                              Partial Body W/o                         Stereo Camera
 –                    Beeler et al. (2011)             2011                        SCS                                       Color, Depth        -            N/A (2 Actors)
                                                              Scene                                    (seven Cameras)
                                                                                                                             Color, IMU,
 –                    Quattrini Li et al. (2017)       2016   Underwater           SCS                 Stereo Camera                             -            3 Sequences
                                                                                                                             Sonar
                                                                                                       Synthetic, Stereo
                                                                                   SCS, Synthetic,                                                            20537 Sequences
 DeMon                Ummenhofer et al. (2017)         2017   N/A                                      Camera, Asus Xtion    Color, Depth        -
                                                                                   Structured Light                                                           And Scenes
                                                                                                       Pro Live, Kinect V1
 Scenes11             Ummenhofer et al. (2017)         2017   N/A                  -                   Synthetic             Color, Depth        -            19959 Sequences

trajectories (Mayer et al., 2016). The second was created using                                   criterion for papers to be incorporated to this work. Some
Blender computer graphics software, based on the information                                      relevant papers in this sub-category are:
from an animated short film called Monkaa. The third is
composed of a street scene. Scene Flow contains only synthetic                                       ReDWeb Dataset. This dataset deals with the in-the-wild
data for all three datasets and, in addition to depth and RGB                                     scenario, covering scenes such as street, office, park, farm, etc.
frames, the authors also include optical flow, segmentation, and                                  As formed in the acronym of this dataset’s name “Relative
stereo disparity change data.                                                                     Depth from Web” (ReDWeb), this dataset is formed by stereo
                                                                                                  images collected from the Internet (Xian et al., 2018). The
   Waymo Perception. This dataset is a street scene dataset                                       authors use optical flow to generate correspondence maps and
composed of RGB and LiDAR labels. It consists of street                                           create a relative depth map of the image. They post-process the
scenes, and the authors labeled LiDAR using 3D bounding                                           data by segmenting the sky to increase the quality of the depth
boxes for vehicles, pedestrians, cyclists, and signs (Sun et al.,                                 maps.
2020). They also provide RGB images annotations with 2D
bounding boxes of vehicles, pedestrians, and cyclists. The 3D                                       SQUID Dataset. This dataset is composed of underwater
bounding boxes also have unique tracking IDs for tracking ap-                                     images collected from four different sites: two in the Red Sea
plications. The Waymo Perception Dataset is composed of                                           and two in the Mediterranean Sea (Berman et al., 2021). In
1,150 scenes with 20 seconds of recording each.                                                   addition to collecting stereo pair images, the authors included
                                                                                                  a ColorChecker to propose color restoration techniques in
4.1.3. Depth Data Only                                                                            underwater images.
   The datasets presented here are for the specific purpose of
training depth estimation algorithms. They do not directly                                           Middlebury Datasets. These datasets are a composition of
provide reconstruction, SLAM, or other information, although                                      data released in different papers over the years of 2001, 2003,
some of these applications are direct results of depth estima-                                    2005, 2006, and 2014. These datasets are acquired using dif-
tion. For example, these works explore monocular depth es-                                        ferent strategies: custom structured light using a video projec-
timation (Cho et al., 2021b), zero-shot depth estimation (Yin                                     tor for the Middlebury 2003 (Scharstein and Szeliski, 2003),
et al., 2020), and multi-camera depth estimation (Antequera                                       Middlebury 2005 (Scharstein and Pal, 2007; Hirschmüller
et al., 2020).                                                                                    and Scharstein, 2007), Middlebury 2006 (Scharstein and
   We present all papers found specifically for depth estimation                                  Pal, 2007; Hirschmüller and Scharstein, 2007), and Mid-
in Table 6. All datasets for all categories and sub-categories in                                 dlebury 2014 (Scharstein et al., 2014), while Middlebury
this paper also contain depth information as it is an inclusion                                   2001 (Scharstein and Szeliski, 2002) uses stereo image pair dis-
                                                                                                                                                                                                           8
                                                            Table 4: Datasets of “Segmentation or Other Extra Information”

Dataset Name       Ref.                          Year   Scene Type         Application        Sensor Type        Sensor Name              Data Modalities      Extra Data             Images/Scenes
                                                                                                                                                               Object Detection,
                                                                                                                                                               Panoptic
                                                                                                                                                               Segmentation,
                                                                                                                                                                                      6 Scenes (6690
VALID              Chen et al. (2020a)           2020   Aerial             SOE                -                  Synthetic                Color, Depth         Instance
                                                                                                                                                                                      Images)
                                                                                                                                                               Segmentation,
                                                                                                                                                               Semantic
                                                                                                                                                               Segmentation
                                                                                                                                                                                      4160 Images From 3
                                                                                                                                                               Semantic               Different Cities
US3D               Foster et al. (2020)          2019   Aerial             SOE                LiDAR              Airborne LiDAR           Color, Depth
                                                                                                                                                               Segmentation           (a Fourth Is Not
                                                                                                                                                                                      Available)
                                                                                                                 Leica ALS50 And                               Semantic
Vaihingen          Haala et al. (2010)           2011   Aerial             SOE                LiDAR                                       Color, Depth                                33 Patches
                                                                                                                 ALTM-ORION M                                  Segmentation
                                                                                                                                                               Semantic
Potsdam            Rottensteiner et al. (2012)   2011   Aerial             SOE                N/A                N/A                      Color, Depth                                38 Patches
                                                                                                                                                               Segmentation
                                                                                                                                                               3D Bounding Boxes,
                                                                           SOE and Tracking                      Leddar Pixell            Color, Depth, IMU,   2D Bounding Boxes,     97 Sequences (29k
Leddar Pixset      Déziel et al. (2021)         2021   Driving                               LiDAR
                                                                           (Other)                               LiDAR                    Radar                Semantic               Frames)
                                                                                                                                                               Segmentation
                                                                                                                                                               Semantic
                                                                                                                                                               Segmentation,          5 Scenes (multiple
                                                                           SOE and Tracking
Virtual Kitti 2    Cabon et al. (2020)           2020   Driving                               -                  Synthetic                Color, Depth         Instance               Conditions For
                                                                           (Other)
                                                                                                                                                               Segmentation,          Each Scene)
                                                                                                                                                               Optical Flow
                                                                                                                                                               3D Object              1150 Scenes (20
Waymo Perception   Sun et al. (2020)             2020   Driving            SOE                LiDAR              N/A                      Color, Depth
                                                                                                                                                               Detection              Seconds/scene)
                                                                           SOE and Tracking                      Argo LiDAR,                                   3D Object
Argoverse          Chang et al. (2019)           2019   Driving                               SCS, LiDAR                                  Color, Depth                                113 Scenes
                                                                           (Other)                               Stereo Camera                                 Detection
                                                                                                                                                               Semantic
                                                                                                                                                               Segmentation,          50 Cities (25k
CityScapes         Cordts et al. (2016)          2016   Driving            SOE                SCS                Stereo Camera            Color, Odometry
                                                                                                                                                               3D-object              Images)
                                                                                                                                                               Detection And Pose
                                                                                                                                                                                      5 Sequences (with
                                                                                              Virtual 8 Depth                                                  Instance               Sub-sequences) At
SYNTHIA            Ros et al. (2016)             2016   Driving            SOE                                   Synthetic                Color, Depth
                                                                                              Sensors                                                          Segmentation           5 Fps. 200k Images
                                                                                                                                                                                      From Videos
Daimler Urban
                   Scharwächter et al. (2014)   2014   Driving            SOE                SCS                Stereo Camera            Color                Semantic Labeling      5k Images
Segmentation
Ground Truth
                   Pfeiffer et al. (2013)        2013   Driving            SOE                SCS                Stereo Camera            Color                Stixels                12 Sequences
Stixel
Daimler Stereo
                   Keller et al. (2011)          2011   Driving            SOE                SCS                Stereo Camera            Color                Object Detection       28919 Images
Pedestrian
                                                                                                                                                               Semantic               21 Sequences (100k
Unreal             Mancini et al. (2018)         2018   Driving, Outdoor   SOE                -                  Synthetic                Color, Depth
                                                                                                                                                               Segmentation           Images)
                                                                                                                                                               Normal Maps,
                                                                                                                 From Human
OASIS V2           Chen et al. (2020b)           2021   In-the-wild        SOE                -                                           Color, Depth         Instance               102k Images
                                                                                                                 Annotation
                                                                                                                                                               Segmenation
                                                                                                                                                               Normal Maps,
                                                                                                                 From Human
OASIS              Chen et al. (2020b)           2020   In-the-wild        SOE                -                                           Color, Depth         Instance               140k Images
                                                                                                                 Annotation
                                                                                                                                                               Segmenation
RedWeb-S           Liu et al. (2021)             2020   In-the-wild        SOE                SCS                Stereo Camera            Color, Depth         Saliency Mask          3179 Images
                                                                                                                 Lytro Illum (Light
DUTLF-Depth        Piao et al. (2019)            2019   In-the-wild        SOE                SCS                                         Color, Depth         Saliency Mask          1200 Images
                                                                                                                 Field) (Stereo Camera)
                                                                                                                                                               Optical Flow,
                                                                                                                                                                                      2256 Scenes (39049
Scene Flow         Mayer et al. (2016)           2016   In-the-wild        SOE                -                  Synthetic                Color                Object
                                                                                                                                                                                      Frames)
                                                                                                                                                               Segmentation
                                                                                                                 Lytro Illum (Light
LFSD               Li et al. (2014)              2015   In-the-wild        SOE                SCS                                         Color                Saliency Mask          100 Images
                                                                                                                 Field) (Stereo Camera)
RGBD Salient
                   Peng et al. (2014)            2014   In-the-wild        SOE                Structured Light   Kinect V1                Color, Depth         Saliency Mask          1000 Images
Object Detection
                                                                                                                                                                                      35 Scenes (50
MPI Sintel         Butler et al. (2012)          2012   In-the-wild        SOE                -                  Synthetic                Color, Depth         Optical Flow
                                                                                                                                                                                      Frames/scene)
                                                                                                                                          Color, Depth,        Occlusion              1449 Images From
NYUv2-OC++         Ramamonjisoa et al. (2020)    2020   Indoor             SOE                Structured Light   Kinect V1
                                                                                                                                          Accelerometer        Boundaries Maps        NYUv2
Near-Collision                                                                                                   LiDAR (N/A),                                  2D Object
                   Manglik et al. (2019)         2019   Indoor             SOE                SCS, LiDAR                                  Color, Depth                                13658 Sequences
Set                                                                                                              Stereo Camera                                 Detection
                                                                                                                                                                                      33 sequences
SBM-RGBD           Camplani et al. (2017)        2017   Indoor             SOE                Structured Light   Kinect V1                Color, Depth         Saliency Mask
                                                                                                                                                                                      ( 15000 frames)
                                                                                                                 Intel RealSense 3D                            Semantic
                                                                                              Structured Light   Camera, Asus Xtion                            Segmentation,
SUN RGB-D          Song et al. (2015)            2015   Indoor             SOE                                                            Color, Depth                                10335 Images
                                                                                              And TOF            LIVE PRO, Kinect                              Object Detection
                                                                                                                 V1 and V2                                     And Pose
                                                                                                                 ASUS Xtion                                    Object Instance        15 Sequences (163
TUW                Aldoma et al. (2014)          2014   Indoor             SOE                Structured Light                            Color, Depth
                                                                                                                 ProLive RGB-D                                 Recognition            Frames)
                                                                                                                                                                                      24 Sequences (353
                                                                                                                                                                                      Frames) For
Willow And                                                                                                                                                     Object Instance
                   Aldoma et al. (2014)          2014   Indoor             SOE                Structured Light   Kinect V1                Color, Depth                                Willow, 39
Challenge                                                                                                                                                      Recognition
                                                                                                                                                                                      Sequences (176
                                                                                                                                                                                      Frames)
An In Depth View
                   Ciptadi et al. (2013)         2013   Indoor             SOE                Structured Light   Kinect V1                Color, Depth         Saliency Mask          80 Images
of Saliency
                                                                                                                                                                                      464 Scenes (407024
                                                                                                                                          Color, Depth,        Semantic               Frames) With 1449
NYU Depth V2       Silberman et al. (2012)       2012   Indoor             SOE                Structured Light   Kinect V1
                                                                                                                                          Accelerometer        Segmentation           Labeled Aligned
                                                                                                                                                                                      RGB-D Images
                                                                                                                                                                                   Continue on Next Page
                                                                                                                                                                                                       9
Dataset Name        Ref.                                  Year   Scene Type           Application   Sensor Type         Sensor Name         Data Modalities   Extra Data         Images/Scenes
                                                                                                                                                                                 3 Options. Large: 2
                                                                                                                                                              Semantic
–                   Mason et al. (2012)                   2012   Indoor               SOE           Structured Light    Kinect V1           Color, Depth                         Sequences (397
                                                                                                                                                              Segmentation
                                                                                                                                                                                 Frames)
                                                                                                                                                                                 75 Scenes (849
Berkeley B3DO       Janoch et al. (2013)                  2011   Indoor               SOE           Structured Light    Kinect V1           Color, Depth      Object Detection
                                                                                                                                                                                 Images)
                                                                                                                                                                                 64 Scenes (108617
                                                                                                                                                              Semantic           Frames) With 2347
NYU Depth V1        Silberman and Fergus (2011)           2011   Indoor               SOE           Structured Light    Kinect V1           Color, Depth
                                                                                                                                                              Segmentation       Labeled RGB-D
                                                                                                                                                                                 Frames
                                                                 Isolated Objects /
                                                                                                                        Intel Realsense
COTS                Seychell et al. (2021)                2021   Focussed On          SOE           SCS                                     Color, Depth      Saliency Mask      120 Images
                                                                                                                        D435
                                                                 Objects
                                                                                                                                                                                 Over 50k
                                                                                                                                                              Normal Maps,
                                                                 Isolated Objects /                                                                                              Synthetic Images
                                                                                                                        Synthetic, Intel                      Semantic
ClearGrasp          Sajjan et al. (2020)                  2019   Focussed On          SOE           SCS                                     Color, Depth                         Of 9 Objects. 286
                                                                                                                        RealSense D415                        Segmentation -
                                                                 Objects                                                                                                         Real Images Of 10
                                                                                                                                                              Synthetic
                                                                                                                                                                                 Objects
                                                                                                                                                                                 N/A Scenes (38k
                                                                                                                                                                                 Images) For
                                                                 Isolated Objects /                                     Kinect V2,
                                                                                                    Structured Light,                                         3D Instance        Training. 20
T-LESS              Hodaň et al. (2017)                  2017   Focussed On          SOE                               PrimeSense          Color, Depth
                                                                                                    TOF                                                       Segmentation       Scenes (10k
                                                                 Objects                                                Carmine 1.0
                                                                                                                                                                                 Images) For
                                                                                                                                                                                 Testing
                                                                 Isolated Objects /
                                                                                                    Structured Light,   Kinect V1, V2 And                                        5 Scenes (112
DROT                Rotman and Gilboa (2016)              2016   Focussed On          SOE                                                   Color, Depth      Object Motion
                                                                                                    TOF                 RealSense R200                                           Frames)
                                                                 Objects
                                                                 Isolated Objects /
                                                                                                    SCS, Structured     Kinect V1,                                               33 Scenes (560
MPII Multi-Kinect   Susanto et al. (2012)                 2012   Focussed On          SOE                                                   Color, Depth      Object Detection
                                                                                                    Light               Stereo Camera                                            Images)
                                                                 Objects
                                                                                                                                            Color, Depth,     Normal Maps,
                                                                                                                                                                                 54 Sequences
Mid-Air             Fonder and Van Droogenbroeck (2019)   2019   Outdoor              SOE           -                   Synthetic           Accelerometer,    Semantic
                                                                                                                                                                                 (420k Frames)
                                                                                                                                            Gyroscope, GPS    Segmentation
SOE: Segmentation or Other Extra Information

parities. Despite using a custom structure light system, Middle-                                        and sign language recognition. Here, we have only two sub-
bury 2014 contains improvements in the acquisition process.                                             categories: the first one encompass full-body activities and the
                                                                                                        second one includes partial body parts, such as hands or face.
4.1.4. Other                                                                                               It is essential to notice that some of these datasets also in-
                                                                                                        clude depth maps of the scene, but the focus of the dataset is on
   This sub-category contains all datasets that do not fit into the
                                                                                                        the Human Body (or part of it). Therefore, they are classified in
previous divisions. There is no sub-category in “Other” with
                                                                                                        this category.
more than four examples. Therefore, we did not create a spe-
cific sub-section for them.
   All datasets here contain depth data and are divided into the                                        4.2.1. Human Activities
following applications: novel view synthesis, foggy images for                                             This sub-category has all datasets focused on human activ-
visibility restoration, relative depth between pairs of random                                          ities, such as drinking, eating, playing tennis, and walking.
points, object tracking, depth refinement for mirror surfaces,                                          Here, we have datasets that analyze actions for an individ-
and synthesis of 4D RGB-D light field images. In Table 7, we                                            ual person (Wang et al., 2012b, 2014) or two-person interac-
display all these datasets and their respective application as a                                        tions (Yun et al., 2012).
column of the table. The most cited dataset included here is:                                              The majority of the works in the “Human Activities” sub-
                                                                                                        category are collected in controlled scenes, and we only found
   FRIDA2. This dataset is a synthetic dataset of foggy images                                          Hollywood 3D (Hadfield and Bowden, 2013) using in-the-wild
of the street view. It is formed by 330 synthetic images of 66                                          datasets. The majority of the datasets are indoor scenes, but as
different scenes, where each image without fog is associated                                            they are centered on actions, they are classified in the “Scene
with four images that vary the intensity of the artificial fog                                          Type” column as “Full Body”. The most common extra data
presented in it (Tarel et al., 2012). Therefore, 66 images with-                                        is the person pose (or skeleton) of the people involved in the
out fog have one depth map and four foggy images associated                                             scene. Such information can help improve automatic action
with it. FRIDA2 is a continuation of The Foggy Road Image                                               recognition algorithms. Datasets containing Human Activities
DAtabase (FRIDA) (Tarel et al., 2010), which has similar                                                are presented in Table 8. Next, we present three influential
characteristics to FRIDA2, but fewer images (only 18 distinct                                           datasets in this sub-category:
scenes). These datasets are created for image enhancement
in foggy images, trying to reduce the impact of the fog in the                                             NTU RGB+D. This dataset contains more than 50,000 video
visibility of street scenes.                                                                            samples representing 60 distinct actions that are divided into
                                                                                                        three major groups: health-related actions (e.g., falling down,
                                                                                                        staggering), 40 daily actions (e.g., eating, drinking), 11 mutual
4.2. Body                                                                                               actions (e.g., kicking, hugging) (Shahroudy et al., 2016). Forty
                                                                                                        subjects aged between 10 and 35 performed the actions in this
  In this category, all datasets are focused on body activities,                                        dataset. The dataset was collected using three Kinect v2 from
such as action recognition, facial expression, hand activities,                                         different horizontal views and is available with RGB, Depth, in-
                                                                                                                                                                                               10
                        Table 5: Datasets of “SLAM, Odometry, or Reconstruction” and “Segmentation or Other Extra Information’ Categories”

Dataset Name     Ref.                            Year   Scene Type   Application   Sensor Type         Sensor Name             Data Modalities      Extra Data            Images/Scenes
                                                                                                                                                    Normal Maps,
                                                                                                                                                                          15 Scenes (144k
–                Wu et al. (2021)                2020   Aerial       SOR and SOE   -                   Synthetic               Color, Depth         Edges, Semantic
                                                                                                                                                                          Images)
                                                                                                                                                    Labels
                                                                                                                                                    Semantic
                                                                                                                                                    Segmentation,
                                                                                                                                                    Navigation Data
EventScape       Gehrig et al. (2021a)           2021   Driving      SOR and SOE   -                   Synthetic               Color, Depth         (Position,            758 Sequences
                                                                                                                                                    Orientation,
                                                                                                                                                    Angular Velocity,
                                                                                                                                                    Etc)
                                                                                                                                                    2D-object
                                                                                                                                                    Detection,
                                                                                                                                                    3D-object
                                                                                                                                                    Detection,
                                                                                                                                                                          11 Sequences To
                                                                                                       Velodyne (LiDAR)                             Tracking,
                                                                                                                               Color, Depth, GPS,                         Over 320k Images
KITTI-360        Liao et al. (2021)              2021   Driving      SOR and SOE   SCS, LiDAR          Points Cloud,                                Instance
                                                                                                                               IMU                                        And 100k Laser
                                                                                                       Stereo Camera                                Segmentation,
                                                                                                                                                                          Scans
                                                                                                                                                    Optical Flow.
                                                                                                                                                    These Are Not In
                                                                                                                                                    Necessary In The
                                                                                                                                                    Same Dataset
                                                                                                                                                    Instance              150 Scenes (12650
DDAD             Guizilini et al. (2020)         2020   Driving      SOR and SOE   LiDAR               Luminar-H2 LiDAR        Color, Deph
                                                                                                                                                    Segmentation          Frames)
                                                                                                       3 LiDAR (40 And
                                                                                                                               Color, Depth,        3D Object             170k Scenes (25
Lyft Level 5     Houston et al. (2020)           2020   Driving      SOR and SOE   SCS, LiDAR          64-beam LiDARs), 5
                                                                                                                               Radar                Detection             Seconds Each)
                                                                                                       Radars, Stereo Camera
                                                                                                                                                    3D Object             1000 Scenes (20
                                                                                                                               Color, Depth,        Detection,            Seconds Each).
NuScenes         Caesar et al. (2020)            2020   Driving      SOR and SOE   LiDAR               N/A
                                                                                                                               Radar, IMU           Semantic              1.4M Images And
                                                                                                                                                    Segmentation          390k LiDAR Sweeps
                                                                                                                                                    Instance
                                                                                                                               Color, IMU, GPS,                           50 Sequences (100k
Woodscape        Yogamani et al. (2019)          2019   Driving      SOR and SOE   LiDAR               Velodyne HDL-64E                             Segmentation, 2D
                                                                                                                               Depth                                      Frames)
                                                                                                                                                    Object Detection
                                                                                                                                                    Semantic
                                                                                                                                                    Segmentation,
                                                                                                                                                                          50 Videos (21260
Virtual Kitti    Gaidon et al. (2016)            2016   Driving      SOR and SOE   -                   Synthetic               Color, Depth         Instance
                                                                                                                                                                          Frames)
                                                                                                                                                    Segmentation,
                                                                                                                                                    Optical Flow
                                                                                                       Velodyne (LiDAR)
                                                                                                                               Color, Grayscale,    Instance              61 Scenes (42746
KITTI            Geiger et al. (2013)            2012   Driving      SOR and SOE   SCS, LiDAR          Points Cloud,
                                                                                                                               Depth, GPS, IMU      Segmentation          Frames)
                                                                                                       Stereo Camera
                                                                                                                                                    Normal Maps,
                                                                                                                                                    Instance
                                                                                                                                                                          461 Scenes (77400
Hypersim         Roberts et al. (2021)           2021   Indoor       SOR and SOE   -                   Synthetic               Color, Depth         Segmentation,
                                                                                                                                                                          Images)
                                                                                                                                                    Diffuse
                                                                                                                                                    Reflectance
                                                                                                                                                    Instance
RoboTHOR         Deitke et al. (2020)            2020   Indoor       SOR and SOE   -                   Synthetic               Color, Depth                               75 Scenes
                                                                                                                                                    Segmentation
                                                                                                                                                    Object Detection,     3500 Scenes With
Structured3D     Zheng et al. (2020)             2020   Indoor       SOR and SOE   -                   Synthetic               Color, Depth         Semantic              21835 Rooms
                                                                                                                                                    Segmentation          (196515 Frames)
                                                                                                                                                    Normal Maps,
                                                                                                                               Color, Depth, IMU,
Replica          Straub et al. (2019)            2019   Indoor       SOR and SOE   Structured Light    N/A                                          Instance              18 Scenes
                                                                                                                               Grayscale Camera
                                                                                                                                                    Segmentation
                                                                                                       NavVis,
                                                                                                                                                    Normal Maps,          572 Scenes. 1400
                                                                                   LiDAR, Structured   Matterport
Gibson           Xia et al. (2018)               2018   Indoor       SOR and SOE                                               Color, Depth         Semantic              Floor Spaces From
                                                                                   Light               Camera,
                                                                                                                                                    Segmentation          572 Buildings
                                                                                                       DotProduct
                                                                                                                                                    Normal Maps,
InteriorNet      Li et al. (2018)                2018   Indoor       SOR and SOE   -                   Synthetic               Color, Depth, IMU    Semantic              20 Million Images
                                                                                                                                                    Segmentation
                                                                                                                                                    25 Tags (Normals
                                                                                                                                                    Maps, Semantic
                                                                                                                                                    Segmentation,
Taskonomy        Garcia-Hernando et al. (2018)   2018   Indoor       SOR and SOE   Structured Light    N/A                     Color, Depth                               4.5 Million Scenes
                                                                                                                                                    Scene
                                                                                                                                                    Classification,
                                                                                                                                                    Etc.)
                                                                                                                                                                          15 Scenes (over 30k
AVD              Ammirato et al. (2017)          2017   Indoor       SOR and SOE   TOF                 Kinect V2               Color, Depth         Object Detection
                                                                                                                                                                          Images)
                                                                                                                                                    Semantic
                                                                                                       Matterport                                                         90 Scenes, 10800
                                                                                   SCS, Structured                                                  Segmentation, 3D
MatterPort3D     Chang et al. (2017)             2017   Indoor       SOR and SOE                       Camera, Stereo          Color, Depth                               Panoramic Views
                                                                                   Light                                                            Semantic-voxel
                                                                                                       Camera                                                             (194400 Images)
                                                                                                                                                    Segmentation
                                                                                                       Occipital
                                                                                                                                                                          1513 Sequences
                                                                                                       Structure Sensor -                           3D Semantic-voxel
ScanNet          Dai et al. (2017)               2017   Indoor       SOR and SOE   Structured Light                            Color, Depth                               (over 2.5 Million
                                                                                                       Similar to                                   Segmentation
                                                                                                                                                                          Frames)
                                                                                                       Kinect V1
                                                                                                                                                    Instance              15K Trajectories
SceneNet RGB-D   McCormac et al. (2017)          2017   Indoor       SOR and SOE   -                   Synthetic               Color, Depth         Segmentation,         (scenes) (5M
                                                                                                                                                    Optical Flow          Images)
                                                                                                                                                    Semantic
SunCG            Song et al. (2017)              2017   Indoor       SOR and SOE   -                   Synthetic               Color, Depth                               45622 Scenes
                                                                                                                                                    Segmentation
                                                                                                                                                                          9 Scenes (6735
GMU Kitchen      Georgakis et al. (2016)         2016   Indoor       SOR and SOE   TOF                 Kinect V2               Color, Depth         Object Detection
                                                                                                                                                                          Frames)

                                                                                                                                                                        Continue on Next Page
                                                                                                                                                                                          11
Dataset Name       Ref.                     Year   Scene Type           Application     Sensor Type        Sensor Name         Data Modalities      Extra Data           Images/Scenes
                                                                                                                                                    Semantic             6 Large-scale
Stanford2D3D       Armeni et al. (2017)     2016   Indoor               SOR and SOE     Structured Light   Matterport Camera   Color, Depth         Segmentation,        Indoor Areas
                                                                                                                                                    Normal Maps          (70496 Images)
                                                                                                           Asus Xtion                               Semantic
SUN3D              Xiao et al. (2013)       2013   Indoor               SOR and SOE     Structured Light                       Color, Depth                              415 Sequences
                                                                                                           Pro Live                                 Segmentation
                                                                                                                                                    Normals Maps,
                                                                                                                                                    Semantic
                                                                                                                               Color, Depth, IMU,
                                                                        SOR And SOE                        Synthetic,                               Segmentation,
                                                   Indoor,                                                                     Grayscale Camera                          Over 14.6M Images
Starter            Eftekhar et al. (2021)   2021                        (depending On   Structured Light   Matterport Pro2,                         Scene
                                                   In-the-wild                                                                 (depending On                             (multiple Scenes)
                                                                        Subdataset)                        NA                                       Classification,
                                                                                                                               Subdataset)
                                                                                                                                                    Etc. (depending On
                                                                                                                                                    Subdataset)
                                                   Indoor, Isolated                                                                                                      8 Sequences And 300
RGBD Object        Lai et al. (2011)        2011   Objects / Focussed   SOR and SOE     Structured Light   Kinect V1           Color, Depth         3D Segmentation      Isolated Objects
                                                   On Objects                                                                                                            (250k Frames)
                                                                                                                                                                         1037 Scenes (Over
                                                                                                                                                    Semantic
                                                                                                                                                                         1M Frames). Each
TartanAir          Wang et al. (2020b)      2020   Indoor, Outdoor      SOR and SOE     -                  Synthetic LiDAR     Color, Depth         Segmentation,
                                                                                                                                                                         Scene Contains
                                                                                                                                                    Optical Flow
                                                                                                                                                                         500-4000 Frames.
                                                   Isolated Objects /
RGB-D Semantic                                                                                                                                      3D Semantic
                   Tombari et al. (2011)    2011   Focussed On          SOR and SOE     Structured Light   Kinect V1           Color, Depth                              16 Test Scenes
Segmentation                                                                                                                                        Segmentation
                                                   Objects
GTA-SfM            Wang and Shen (2020)     2020   Outdoor              SOR and SOE     -                  Synthetic           Color, Depth         Optical Flow         76k Images
SOR: SLAM, Odometry, or Reconstruction
SOE: Segmentation or Other Extra Information

frared (IR) sequences, and person pose (skeleton) information.                                    person used for training and the other two for testing, leading
   The authors extended the NTU RGB+D to a new dataset                                            to over 80 thousand acquired frames.
called NTU RGB+D 120, which contains other 60 classes and
57,600 samples, also containing the same capturing system and                                        MSR Gesture3D. This dataset contains sign language ges-
data modalities as the previous dataset (Liu et al., 2019).                                       tures. The authors collected 12 dynamic American Sign Lan-
   MSR DailyActivity3D Dataset. This dataset covers sixteen                                       guage (ASL) gestures from ten people. The dataset was cap-
different activities: drink, eat, read a book, call cellphone,                                    tured using Kinect v1, and has 336 sequences since each per-
write on a paper, use a laptop, use a vacuum cleaner, cheer                                       son performed multiple recordings of all selected signs. The
up, sit still, toss paper, play games, lie down on a sofa, walk,                                  authors performed a hand segmentation, and depth information
play guitar, stand up, and sit down (Wang et al., 2012b). Ten                                     is available only for the segmented hand regions. Background
subjects performed each action twice: one for standing and                                        and body portions below the wrist were removed.
one for sitting position. This dataset also includes person pose
information for each frame. The authors used the Kinect v1 to
acquire the depth of the scenes.
                                                                                                  4.3. Medical
   MSR Action3D. This dataset covers twenty different actions
performed by ten subjects. Each action was performed two
to three times, resulting in 557 filtered sequences and 23,797                                       In this category, we present datasets that are from any part
frames (Li et al., 2010). The actions are divided into three                                      of the medical field. The exclusion criteria removed most of
sets, where the first categorize actions with similar moviments.                                  the datasets found here because these contained only private
The third set is composed by complex actions together. All se-                                    data. For instance, we collected eleven datasets containing en-
quences were acquired using Kinect v1 sensor.                                                     doscopic data, but only three meets all criteria to be included in
                                                                                                  our work. This situation is common in medical applications as
4.2.2. Gestures (Partial Body)                                                                    sharing medical information requires regulated procedures.
   Here, we grouped all works that involve human actions or                                          We found only four datasets available in this category, of
activities and have data available for human body parts, such                                     which three of them contain endoscopic data and one contains
as arms, head, and hand. There is a wide variety of dataset pur-                                  3D models of the iris. The most cited dataset in containing
poses in this sub-category, such as action recognition based on a                                 depth information in the medical field is:
first-person view (no torso/head parts available in video) (Tang
et al., 2017), salad preparation (Stein and McKenna, 2013),                                          Colonoscopy CG Dataset. This dataset is composed of en-
hand-pose information (Tompson et al., 2014), and sign lan-                                       doscopic data of the colon. To the best of our knowledge, this
guage recognition (Wang et al., 2012a).                                                           is the most frequent type of data that contains depth maps in the
   The most cited datasets in this sub-category include:                                          Medical category, even if analyzing datasets with non-shared
                                                                                                  data. The authors generated a synthetic dataset using Unity
   NYU Hand Pose Dataset. This dataset was captured using                                         graphic engine based on a human CT colonography scan. They
three Kinect v1, with two side views and a frontal view.                                          extracted a surface mesh using manual segmentation and mesh-
The authors also re-created a synthetic hand pose for each                                        ing (Rau et al., 2019). Their work also proposed and tested
view (Tompson et al., 2014), and made available 36 hand point                                     an algorithm in real data, but this data is not available for the
locations for each frame. Three people acquired the data: one                                     community thus not included in this paper.
                                                                                                                                                                                                 12
                                                               Table 6: Datasets of “Depth Data Only” sub-category

Dataset Name      Ref.                                        Year          Scene Type        Sensor Type         Sensor Name          Data Modalities      Extra Data         Images/Scenes
                                                                                                                                                                               49 Environments
Espada            Lopez-Campos and Martinez-Carranza (2021)   2021          Aerial            -                   Synthetic            Color, Depth         -
                                                                                                                                                                               (80k Images)
                                                                                                                  Velodyne VLP-16,
DSEC              Gehrig et al. (2021b)                       2021          Driving           SCS, LiDAR                               Color, Depth, GPS    -                  53 Sequences
                                                                                                                  Stereo Camera
                                                                                                                                                                               50k Scenes
Mapillary         Antequera et al. (2020)                     2020          Driving           SCS                 Stereo Camera        Color, Depth         -
                                                                                                                                                                               (750k Images)
                                                                                                                                                                               200 Scenes (100 For
RabbitAI                                                                                                          17-camera
                  Schilling et al. (2020)                     2020          Driving           SCS                                      Color, Depth         -                  Training, 100 For
Benchmark                                                                                                         Light-field
                                                                                                                                                                               Testing)
DrivingStereo -                                                                                                   Velodyne HDL-64E,    Color, Depth, IMU,                      42 Sequences
                  Yang et al. (2019)                          2019          Driving           SCS, LiDAR                                                    -
Driving Stereo                                                                                                    Stereo Camera        GPS                                     (182188 Frames)
Urban Virtual
                  Mancini et al. (2017)                       2017          Driving           -                   Synthetic            Color, Depth         -                  58500 Images
(UVD)
DiverseDepth      Yin et al. (2020)                           2020          In-the-wild       SCS                 Stereo Camera        Color                -                  320k Images
HRWSI             Xian et al. (2020b)                         2020          In-the-wild       SCS                 Stereo Camera        Color, Depth         -                  20778 Images
Holopix50k        Hua et al. (2020)                           2020          In-the-wild       SCS                 Stereo Camera        Color                -                  49368 Images
DualPixels        Garg et al. (2019)                          2019          In-the-wild       SCS                 Stereo Camera        Color, Depth         -                  3190 Images
TAU Agent         Gil et al. (2019)                           2019          In-the-wild       -                   Synthetic            Color, Depth         -                  5 Scenes
                                                                                                                                                                               553 Videos
WSVD              Wang et al. (2019a)                         2019          In-the-wild       SCS                 Stereo Camera        Color, Depth         -
                                                                                                                                                                               (1.5M Frames)
ReDWeb            Xian et al. (2018)                          2018          In-the-wild       SCS                 Stereo Camera        Color, Depth         -                  3600 Images
AirSim
                  Keltjens et al. (2021)                      2021          Indoor            -                   Synthetic            Color, Depth         -                  20k Images
Building 99
                                                                                                                  3 RGB Cameras. The
                                                                                                                  3 Depth Cameras.
                                                                                                                  Matterport
                                                                                              LiDAR, Structured
Pano3D            Albanis et al. (2021)                       2021          Indoor                                Camera, NavVis,      Color, Depth         Normal Maps        42923 Samples
                                                                                              Light
                                                                                                                  DotProduct
                                                                                                                  (depending On
                                                                                                                  Subdataset)
                                                                                                                                                                               Around 1200 Scenes
Multiscopic                                                                                                                                                                    Of Synthetic Data,
                  Yuan et al. (2020)                          2020          Indoor            -                   Synthetic            Color                -
Vision                                                                                                                                                                         92 Scenes Of Real
                                                                                                                                                                               Data.
IRS               Wang et al. (2019c)                         2019          Indoor            -                   Synthetic            Color, Depth         Normal Maps        100025 Images
                                                                                                                                                            Semantic
                                                                                                                  Laser (Leica                              Segmentation
IBims-1           Koch et al. (2019)                          2019          Indoor            TOF                 HDS7000 Laser        Color, Depth         (only For Planar   100 Images
                                                                                                                  Scanner)                                  Areas: Walls,
                                                                                                                                                            Tables, Floor)
Middlebury 2014   Scharstein et al. (2014)                    2014          Indoor            SCS                 Stereo Camera        Color, Depth         -                  33 Images
                                                                                                                  Custom-build
Middlebury 2006   Scharstein and Pal (2007)                   2006          Indoor            Structured Light                         Color, Depth         -                  21 Images
                                                                                                                  Structured Light
                                                                                                                  Custom-build
Middlebury 2005   Scharstein and Pal (2007)                   2005          Indoor            Structured Light                         Color, Depth         -                  9 Images
                                                                                                                  Structured Light
                                                                                                                  Custom-build
Middlebury 2003   Scharstein and Szeliski (2003)              2003          Indoor            Structured Light                         Color, Depth         -                  2 Images
                                                                                                                  Structured Light
Middlebury 2001   Scharstein and Szeliski (2003)              2001          Indoor            SCS                 Stereo Camera        Color, Depth         -                  6 Images
                                                                                                                                                                               30 Scenes (8574
                                                                                                                                                                               Indoor Images,
DIODE             Vasiljevic et al. (2019)                    2019          Indoor, Outdoor   LiDAR               FARO Focus S350      Color, Depth         Normal Maps
                                                                                                                                                                               16884 Outdoor
                                                                                                                                                                               Images)
                                                                                                                  Kinectv2 For
                                                              2016, 2017,                                         Indoor, ZED Stereo                                           More Than 200
DIML/CVL          Cho et al. (2021a)                                        Indoor, Outdoor   SCS, TOF                                 Color, Depth         -
                                                              2018, 2021                                          Camera                                                       Scenes
                                                                                                                  for Outdoor
Forest Virtual
                  Mancini et al. (2017)                       2017          Outdoor           -                   Synthetic            Color, Depth         -                  49500 Images
(FVD)
                                                                                                                                                                               3 Sequences (9846
Zurich Forest     Mancini et al. (2017)                       2017          Outdoor           SCS                 Stereo Camera        Color, Depth         -
                                                                                                                                                                               Images)
                                                                                                                                                                               600 Pairs (51 With
–                 Cui et al. (2021)                           2021          Underwater        SCS                 Stereo Camera        Color, Depth         -                  Depth Ground
                                                                                                                                                                               Truth)
SQUID             Berman et al. (2021)                        2020          Underwater        SCS                 Stereo Camera        Color, Depth         -                  57 Images

5. Discussion                                                                                       found a 50% increase in the numbers of datasets containing
                                                                                                    synthetic data. Synthetic datasets are usually cheaper to pro-
   The datasets presented in Section 4 compose a collection of                                      duce than performing real data acquisition because extra an-
different scenes, sensors, and activities. We provide informa-                                      notations, e.g., semantic segmentation or object tracking, are
tion about the Sensor Type, Number of Images/Scenes, Scene                                          automatically generated. On the other hand, complex scene an-
Type, Sensor Name, and Data Modalities available for each                                           notations for real data are costly, especially in scenes such as
dataset. Unlike previous surveys of RGB-D datasets (Firman,                                         driving and aerial.
2016), we do not categorize the datasets regarding their realism
since this is a subjective criterion and it is up to the researcher
who will analyze the datasets to decide. Despite the variety of                                        Synthetic datasets were initially created using simula-
datasets presented, we identified common tendencies in all ar-                                      tors (Tarel et al., 2010, 2012), but these simulators were dis-
eas and discussed them in this section.                                                             tinct to real-world scenarios since the computational power of
   Although synthetic data is becoming more present each time,                                      the machines was limited. Hence, it was not possible to gen-
the usage of real data is presented in the majority of the datasets.                                erate consistent and realistic datasets for complex scenes. Re-
Comparing the 2016-2018 to the 2019-2021 trienniums, we                                             cently, realistic simulators were created for driving scenes, such
                                                                                                                                                                                         13
                                                                 Table 7: “Other” Scene/Objects RGB-D Datasets

 Dataset Name    Ref.                       Year   Scene Type        Application         Sensor Type        Sensor Name              Data Modalities     Extra Data     Images/Scenes
                                                                                                                                                                        66 Scenes (330
 FRIDA2          Tarel et al. (2012)        2012   Driving           Fog (Other)         -                  Synthetic                Color, Depth        -
                                                                                                                                                                        Images)
                                                                                                                                                                        18 Scenes (90
 FRIDA           Tarel et al. (2010)        2010   Driving           Fog (Other)         -                  Synthetic                Color, Depth        -
                                                                                                                                                                        Images)
                                                                     3D Ken Burns
 3D Ken Burns    Niklaus et al. (2019)      2019   In-the-wild                           -                  Synthetic                Color, Depth        Normal Maps    46 Sequences
                                                                     (Other)
                                                                                                            Two Points
                                                                                                                                     Color, Depth
 DIW             Chen et al. (2016)         2016   In-the-wild       Points (Other)      -                  (manually                                    -              495k Images
                                                                                                                                     Points (2 Points)
                                                                                                            Anotated)
                                                                                                            Matterport Camera,
                                                                                                            Stereo Camera,
                                                                                                            Kinect V1,
                                                                                         Structured                                                                     7011 Scenes With
 Mirror3D        Tan et al. (2021b)         2021   Indoor            Mirror (Other)                         Occipital                Color, Depth        Mirror Mask
                                                                                         Light, SCS                                                                     Mirror
                                                                                                            Structure Sensor -
                                                                                                            Similar To
                                                                                                            Kinect V1
 Princeton
 Tracking        Song and Xiao (2013)       2013   Indoor            Tracking (Other)    Structured Light   Kinect V1                Color, Depth        -              100 Sequences
 Benchmark
                                                                     Novel View                                                                          Semantic
 Dynamic Scene   Shin Yoon et al. (2020)    2020   Indoor, Outdoor                       SCS                Stereo Camera            Color                              9 Scenes
                                                                     Synthesis (Other)                                                                   Segmentation
                                                                     Synthesizes A 4D                       Lytro Illum (Light
 LightField      Srinivasan et al. (2017)   2017   Other (Flowers)                       SCS                                         Color               -              3343 Images
                                                                     RGBD LF (Other)                        Field) (Stereo Camera)

as CARLA (Dosovitskiy et al., 2017), Nvidia Drive Sim2 , and                                   that directly using synthetic data may not improve the results
indoor scenes, such as Habitat (Szot et al., 2021; Savva et al.,                               for realistic data evaluation due to dataset bias. They adapt the
2019). Despite the usage of simulators, other datasets rely on                                 domain of a synthetic dataset to a real dataset using Style Trans-
game engines or general computer graphics engines to build                                     fer and combine them to train their models. Zhao et al. (2019)
their systems, such as SYNTHIA (Ros et al., 2016), Virtual                                     also performs domain adaptation, and they claim that due to
KITTI (Gaidon et al., 2016), and Virtual KITTI 2 (Cabon et al.,                                the lack of paired synthetic and real images, the synthetic-to-
2020) that used Unity3 as graphic engine, and GTA-SfM (Wang                                    realistic image translation adds distortions to the depth esti-
and Shen, 2020) that uses scenes from the game GTAV.                                           mation. They overcome this difficulty by exploring a more
   The usage of synthetic data has been combined with real data                                complex training procedure involving synthetic-to-realistic and
to produce more complex scenes. These are applied especially                                   realistic-to-synthetic translations. To generate more realistic
for techniques that explore the generalization of their methods                                synthetic data, Su et al. (2015) proposed the use of 3D CAD
in non-expected scenes, i.e., using datasets not used in the train-                            Models to produce 2D synthetic images, since these CAD Mod-
ing step (Ummenhofer et al., 2017; Ranftl et al., 2020; Eftekhar                               els allow multiple viewpoints and complete control of the defor-
et al., 2021).                                                                                 mations in the modeled objects to increase the variability of the
   These papers combine datasets containing different types of                                 created dataset. Planche et al. (2017) also used 3D CAD Mod-
acquisition and scenes to produce generalizable models. Ran-                                   els, but they intended to create realistic depth data from the 3D
ftl et al. (2020) created multiple cross-dataset training strate-                              objects. They proposed a framework that simulates real distor-
gies, and its combination of datasets with more images —                                       tion factors of depth data acquisition, e.g., material reflectance
called MIX5— contains data from DIML, MegaDepth, Red-                                          and sensor noise, to generate reliable depth data. In addition to
Web, WSVD, and 3D Movies datasets. Ranftl et al. (2021b)                                       using synthetic data, domain adaptation could also be applied
expanded this combination, creating the MIX6 cross-dataset set                                 to real-to-real translation (Lopez-Rodriguez and Mikolajczyk,
containing about 1.4 million training images. Both works were                                  2020; Hornauer et al., 2021) since the dataset bias also affects
evaluated using a mixture of testing datasets. The robustness of                               distinct real datasets, especially by variations of scale and cap-
the models are also evaluated in a cross-dataset strategy for es-                              ture’s position of the scenes (Torralba and Efros, 2011).
timating depth from a monocular video (Kopf et al., 2021), and
instead of testing in multiple types of scenes, Ji et al. (2021)
combined distinct datasets of the same type of scene to improve                                6. Conclusions
the results for the indoor environment.
   Recently, domain adaptation has been applied to improve                                        In this work, we presented a survey of publicly available im-
the performance of the combination of datasets in the training                                 age datasets that contain depth information. We categorized
step (Guo et al., 2018; Atapour-Abarghouei and Breckon, 2018;                                  and summarized over 200 datasets based on the image scenes,
Zhao et al., 2019). Atapour-Abarghouei and Breckon (2018),                                     sensors used to collect the depth information, and the different
for instance, combines one synthetic and one real dataset using                                applications for which these datasets can be used. Almost half
domain adaptation to improve the result of training. They claim                                of the datasets we describe were proposed after the publication
                                                                                               of the last survey (Cai et al., 2017). The new datasets expand
                                                                                               the scope of applications that depth datasets can be used for,
   2 https://developer.nvidia.com/drive/drive-sim                                              such as medical applications. The new datasets also expand the
   3 https://unity.com/                                                                        quality and quantity of data for other areas.
                                                                                                                                                                     14
                                                         Table 8: Datasets of “Human Activity” sub-category

Dataset Name          Ref.                        Year    Scene Type   Sensor Type        Sensor Name    Data Modalities    Extra Data          Images/Scenes
Depth 2 Height        Yin and Zhou (2020)         2020    Full Body    TOF                Kinect V2      Color, Depth       -                   2136 Images
SOR3D-AFF             Thermos et al. (2020)       2020    Full Body    TOF                Kinect V2      Color, Depth       -                   1201 Sequences
                                                                                                                            Person Pose
NTU RGB+D 120         Liu et al. (2019)           2019    Full Body    TOF                Kinect V2      Color, Depth, IR                       111480 Sequences
                                                                                                                            (Skeleton)
                                                                                                                                                800 Frames For Each
–                     Tang et al. (2019)          2019    Full Body    TOF                Kinect V2      Color, Depth       -
                                                                                                                                                Person (26 People)
                                                                                                         Color, Depth
CMDFALL               Tran et al. (2018)          2018    Full Body    Structured Light   Kinect V1                         -                   20 Sequences
                                                                                                         Accelerometer
UESTC                 Ji et al. (2019)            2018    Full Body    TOF                Kinect V2      Color, Depth       -                   25600 Sequences
                                                                                                                                                20 Sequences (20
                                                                                                                                                Participants
UOW Online                                                                                                                  Person Pose
                      Tang et al. (2018)          2018    Full Body    TOF                Kinect V2      Color, Depth                           Performing
Action3D                                                                                                                    (Skeleton)
                                                                                                                                                Multiple Actions
                                                                                                                                                In A Sequence)
                                                                                                         Color, Depth       Person Pose
PKU-MMD               Chunhui et al. (2017)       2017    Full Body    TOF                Kinect V2                                             3076 Sequences
                                                                                                         Accelerometer      (Skeleton)
                                                                                          Asus Xtion                                            23 Sequences (100
TVPR                  Liciotti et al. (2017)      2017    Full Body    Structured Light                  Color, Depth       -
                                                                                          Pro Live                                              People, 2004 Secs)
Chalearn LAP
                      Wan et al. (2016)           2016    Full Body    Structured Light   Kinect V1      Color, Depth       -                   47933 Sequences
IsoGD
                                                                                                                            Person Pose
                                                                                                                                                7 Sequences
                                                                                                                            (Skeleton)
G3D                   Bloom et al. (2016)         2016    Full Body    Structured Light   Kinect V1      Color, Depth                           (Multiple Actions
                                                                                                                            Semantic
                                                                                                                                                Per Sequence)
                                                                                                                            Segmentation
                                                                                                                                                8 Actors Recorded
                                                                                                                                                Interections.
                                                                                                                            Person Pose         Each Interaction
HHOI                  Shu et al. (2016)           2016    Full Body    TOF                Kinect V2      Color, Depth
                                                                                                                            (Skeleton)          Lasts 2-7 Seconds
                                                                                                                                                Presented At 10-15
                                                                                                                                                Fps
ISR-UoL 3D                                                                                                                  Person Pose
                      Coppola et al. (2016)       2016    Full Body    Structured Light   Kinect V1      Color, Depth                           10 Sequences
Social Activity                                                                                                             (Skeleton)
                                                                                                                            Person Pose
NTU RGB+D             Shahroudy et al. (2016)     2016    Full Body    TOF                Kinect V2      Color, Depth, IR                       56880 Sequences
                                                                                                                            (Skeleton)
TST Fall Detection                                                                                       Color, Depth,      Person Pose
                      Gasparrini et al. (2015b)   2016    Full Body    TOF                Kinect V2                                             264 Scenes
V2                                                                                                       Accelerometer      (Skeleton)
UOW LargeScale                                                                                                              Person Pose
                      Zhang et al. (2016a)        2016    Full Body    TOF                Kinect V2      Color, Depth                           4953 Sequences
Combined Action3D                                                                                                           (Skeleton)
                                                                                                                                                65 Sequences (5.5
CMU Panoptic          Joo et al. (2017)           2015    Full Body    TOF                Kinect V2      Color, Depth       3D Skeleton
                                                                                                                                                Capture Hours)
                                                                                                                            Person Pose
SYSU 3D HOI           Hu et al. (2017)            2015    Full Body    Structured Light   Kinect V1      Color, Depth                           480 Sequences
                                                                                                                            (Skeleton)
TST Intake
                      Gasparrini et al. (2015a)   2015    Full Body    Structured Light   Kinect V1      Color, Depth       -                   48 Sequences
Monitoring V1
TST Intake
                      Gasparrini et al. (2015a)   2015    Full Body    Structured Light   Kinect V1      Color, Depth       -                   60 Sequences
Monitoring V2
                                                                                                         Color, Depth,      Person Pose
TST TUG DataBase      Cippitelli et al. (2015)    2015    Full Body    TOF                Kinect V2                                             60 Sequences
                                                                                                         Accelerometer      (Skeleton)
                                                                                                         Color, Depth,      Person Pose
UTD-MHAD              Chen et al. (2015)          2015    Full Body    Structured Light   Kinect V1                                             861 Sequences
                                                                                                         Accelerometer      (Skeleton)
                                                                                          MESA Imaging   Color, Depth,                          447260 RGB-D
                                                                                                                            Person Pose
Human3.6M             Ionescu et al. (2014)       2014    Full Body    TOF                SR4000 From    Motion Capture                         Frames (almost
                                                                                                                            (Skeleton)
                                                                                          SwissRanger    (mx) Camera                            3.6M RGB Frames)
                                                                                                                            Person Pose
KARD                  Gaglio et al. (2015)        2014    Full Body    Structured Light   Kinect V1      Color, Depth                           540 Sequences
                                                                                                                            (Skeleton)
LIRIS                 Wolf et al. (2014)          2014    Full Body    Structured Light   Kinect V1      Color, Depth       -                   180 Sequences
                                                                                                                            Person Pose
MAD                   Huang et al. (2014)         2014    Full Body    Structured Light   Kinect V1      Color, Depth                           40 Sequences
                                                                                                                            (Skeleton)
Northwestern-UCLA
                      Wang et al. (2014)          2014    Full Body    Structured Light   Kinect V1      Color, Depth       -                   1473 Sequences
Multiview Action 3D
Online RGBD
                                                                                                                            Person Pose
Action Dataset        Yu et al. (2014)            2014    Full Body    Structured Light   Kinect V1      Color, Depth                           48 Sequences
                                                                                                                            (Skeleton)
(ORGBD)
TST Fall Detection                                                                                       Color, Depth,      Person Pose
                      Gasparrini et al. (2014)    2014    Full Body    Structured Light   Kinect V1                                             20 Sequences
V1                                                                                                       Accelerometer      (Skeleton)
                                                                                                         Color, Depth,
UR Fall Detection     Kwolek and Kepski (2014)    2014    Full Body    Structured Light   Kinect V1                         -                   70 Sequences
                                                                                                         Accelerometer
Chalearn
Multimodal                                                                                               Color, Depth,      User Mask, Person   707 Sequences
                      Escalera et al. (2013)      2013    Full Body    Structured Light   Kinect V1
Gesture                                                                                                  Audio              Pose (Skeleton)     (1720800 Frames)
Recognition
Florence 3D                                                                                                                 Person Pose
                      Seidenari et al. (2013)     2013    Full Body    Structured Light   Kinect V1      Color, Depth                           215 Sequences
Actions                                                                                                                     (Skeleton)
                                                                                                                                                Continue on Next Page
                                                                                                                                                                  15
 Dataset Name        Ref.                         Year   Scene Type    Sensor Type        Sensor Name       Data Modalities    Extra Data         Images/Scenes
                                                                                                                               Person Pose
                                                                                                                               (Skeleton)
 IAS-Lab RGBD-ID     Munaro et al. (2013)         2013   Full Body     Structured Light   Kinect V1         Color, Depth                          33 Sequences
                                                                                                                               Semantic
                                                                                                                               Segmentation
                                                                                                            Color, Depth,
                                                                                                            Accelerometer,
 MHAD                Ofli et al. (2013)           2013   Full Body     Structured Light   Kinect V1                            -                  660 Sequences
                                                                                                            Motion Capture
                                                                                                            System
 Mivia Action        Carletti et al. (2016)       2013   Full Body     Structured Light   Kinect V1         Color, Depth       -                  28 Sequences
 ChaLearn Gesture
                     Guyon et al. (2014)          2012   Full Body     Structured Light   Kinect V1         Color, Depth       -                  50k Sequences
 Challenge
                                                                                                                                                  583 Sequences (53
 DGait               Borràs et al. (2012)        2012   Full Body     Structured Light   Kinect V1         Color, Depth       -
                                                                                                                                                  Subjects)
 MSR                                                                                                                           Person Pose
                     Wang et al. (2012b)          2012   Full Body     Structured Light   Kinect V1         Color, Depth                          320 Sequences
 DailyActivity3D                                                                                                               (Skeleton)
                                                                                                                               Person Pose        316 Sequences (79
 RGBD-ID             Barbosa et al. (2012)        2012   Full Body     Structured Light   Kinect V1         Color, Depth
                                                                                                                               (Skeleton)         People)
                                                                                                                                                  21 Sequences From
 SBU Kinect                                                                                                                    Person Pose
                     Yun et al. (2012)            2012   Full Body     Structured Light   Kinect V1         Color, Depth                          Seven
 Interaction                                                                                                                   (Skeleton)
                                                                                                                                                  Participants
                                                                                                                               Person Pose
 UTKinect-Action3D   Xia et al. (2012)            2012   Full Body     Structured Light   Kinect V1         Color, Depth                          200 Sequences
                                                                                                                               (Skeleton)
                                                                                                                                                  1 Sequence (1132
                                                                                                                               Object Detection
 RGB-D People        Spinello and Arras (2011)    2011   Full Body     Structured Light   Kinect V1         Color, Depth                          Frames Of 3
                                                                                                                               And Tracking
                                                                                                                                                  Sensors)
                                                                                          Similar to                                              557 Sequences
 MSR Action3D        Li et al. (2010)             2010   Full Body     Structured Light                     Color, Depth       -
                                                                                          Kinect V1 (N/A)                                         (23797 Frames)
                                                                                                                                                  Around 650 Video
 Hollywood 3D        Hadfield and Bowden (2013)   2013   In-the-wild   SCS                Stereo Camera     Color, Depth       -
                                                                                                                                                  Clips

   We also presented different forms of acquiring depth infor-                       References
mation from a scene. We expect that this explanation could
be used in conjunction with extra information of the datasets                        Aksoy, E.E., Tamosiunaite, M., Wörgötter, F., 2015. Model-Free Incremental
to allow researchers to choose the ones that best fulfill their                         Learning Of The Semantics Of Manipulation Actions. Robotics and Au-
                                                                                        tonomous Systems , 118–133.
needs. Researchers of zero-shot learning trying to increase gen-                     Albanis, G., Zioulis, N., Drakoulis, P., Gkitsas, V., Sterzentsenko, V., Alvarez,
eralization capabilities for their model could also benefit from                        F., Zarpalas, D., Daras, P., 2021. Pano3D: A Holistic Benchmark and A
our work since they may select distinct datasets in terms of sen-                       Solid Baseline for 360Deg Depth Estimation, in: IEEE Conference on Com-
sor type, application, and scene type for training and evaluating                       puter Vision and Pattern Recognition (CVPR), pp. 3727–3737.
                                                                                     Aldoma, A., Fäulhammer, T., Vincze, M., 2014. Automation Of ”Ground
their methods.                                                                          Truth” Annotation for Multi-View RGB-D Object Instance Recognition
                                                                                        Datasets, in: IEEE/RSJ International Conference on Intelligent Robots and
                                                                                        Systems, pp. 5016–5023.
CRediT authorship contribution statement                                             Allan, M., Mcleod, J., Wang, C., Rosenthal, J.C., Hu, Z., Gard, N., Eisert, P.,
                                                                                        Fu, K.X., Zeffiro, T., Xia, W., 2021. Stereo Correspondence and Recon-
                                                                                        struction of Endoscopic Data Challenge. arXiv preprint arXiv:2101.01133 ,
   Alexandre Lopes: Conceptualization, Formal analysis, In-                             1–7.
vestigation, Methodology, Writing - review & editing. Roberto                        Ammirato, P., Poirson, P., Park, E., Kosecka, J., Berg, A.C., 2017. A Dataset
Souza: Funding acquisition, Methodology, Project administra-                            for Developing and Benchmarking Active Vision, in: IEEE International
tion, Supervision, Writing – review & editing. Helio Pedrini:                           Conference on Robotics and Automation (ICRA), pp. 1378–1385.
                                                                                     Antequera, M.L., Gargallo, P., Hofinger, M., Bulò, S.R., Kuang, Y.,
Methodology, Project administration, Supervision, Writing –                             Kontschieder, P., 2020. Mapillary Planet-Scale Depth Dataset, in: European
review & editing.                                                                       Conference on Computer Vision (ECCV), pp. 589–604.
                                                                                     Armeni, I., Sax, S., Zamir, A.R., Savarese, S., 2017. Joint 2D-3D-Semantic
                                                                                        Data for Indoor Scene Understanding. arXiv preprint arXiv:1702.01105 ,
Declaration of competing interest                                                       1–9.
                                                                                     Atapour-Abarghouei, A., Breckon, T.P., 2018. Real-time Monocular Depth
                                                                                        Estimation using synthetic Data with Domain Adaptation via Image Style
  The authors declare that they have no known competing fi-                             Transfer, in: IEEE Conference on Computer Vision and Pattern Recognition
nancial interests or personal relationships that could have ap-                         (CVPR), pp. 2800–2810.
peared to influence the work reported in this paper.                                 Bagdanov, A.D., Del Bimbo, A., Masi, I., 2011. The Florence 2D/3D Hybrid
                                                                                        Face Dataset, in: Joint ACM Workshop on Human Gesture and Behavior
                                                                                        Understanding, p. 79–80.
                                                                                     Barbosa, I.B., Cristani, M., Del Bue, A., Bazzani, L., Murino, V., 2012. Re-
Acknowledgements                                                                        Identification With RGB-D Sensors, in: European Conference on Computer
                                                                                        Vision (ECCV), pp. 433–442.
  The authors are grateful to the National Council for Sci-                          Barrera Campo, F., Lumbreras Ruiz, F., Sappa, A.D., 2012. Multimodal Stereo
entific and Technological Development, Brazil (CNPq grant                               Vision System: 3D Data Extraction and Algorithm Evaluation. IEEE Journal
                                                                                        of Selected Topics in Signal Processing , 437–446.
309330/2018-1). Roberto Souza thanks the Natural Sciences                            Beeler, T., Hahn, F., Bradley, D., Bickel, B., Beardsley, P., Gotsman, C., Sum-
and Engineering Research Council (NSERC - RGPIN-2021-                                   ner, R.W., Gross, M., 2011. High-Quality Passive Facial Performance Cap-
02867) for ongoing operational support.                                                 ture Using Anchor Frames. ACM Trans. Graph. , 1–10.
                                                                                                                                                                                                           16
                                                               Table 9: Datasets of “Gestures (Partial Body) sub-category”

 Dataset Name        Ref.                                              Year     Scene Type            Sensor Type        Sensor Name           Data Modalities     Extra Data           Images/Scenes
 Bimanual                                                                       Part Of Body (hand,                      PrimeSense
                     Dreher et al. (2020)                              2020                           Structured Light                         Color, Depth        -                    540 Sequences
 Actions                                                                        Head, Etc.)                              Carmine 1.09
                                                                                                                                                                   Segmentation, 2D
                                                                                                                                                                   Keypoints, Dense
                                                                                                                                                                   Matching Map,        Real: 4 Sequences
                                                                                Part Of Body (hand,                      Intel RealSense
 RGB2Hands           Wang et al. (2020a)                               2020                           Structured Light                         Color, Depth        Inter-hand           (1724 Frames).
                                                                                Head, Etc.)                              SR300/Synthetic
                                                                                                                                                                   Distance,            Synthetic: NA
                                                                                                                                                                   Intra-hand
                                                                                                                                                                   Distance
                                                                                                                                                                   3D Hand Keypoints,
                                                                                Part Of Body (hand,                                                                Object
 ObMan               Hasson et al. (2019)                              2019                           -                  Synthetic             Color, Depth                             150k Images
                                                                                Head, Etc.)                                                                        Segmentation,
                                                                                                                                                                   Hand Segmentation
                                                                                Part Of Body (hand,                      Intel RealSense
 EgoGesture          Zhang et al. (2018)                               2018                           Structured Light                         Color, Depth        -                    2081 Sequences
                                                                                Head, Etc.)                              SR300/Synthetic
                                                                                                                                               Color, Depth,                            1175 Sequences
                                                                                Part Of Body (hand,                      Intel RealSense
 –                   Garcia-Hernando et al. (2018)                     2018                           Structured Light                         Magnetic And        -                    (over 100k
                                                                                Head, Etc.)                              SR300
                                                                                                                                               Kinematic Sensors                        Frames)
                                                                                                                                                                                        N/A Sequences (2.2
                                                                                Part Of Body (hand,                      Intel RealSense       Color, Depth, 6D
 BigHand2.2M         Yuan et al. (2017)                                2017                           Structured Light                                             -                    Million Images),
                                                                                Head, Etc.)                              SR300                 Magnetic Sensor
                                                                                                                                                                                        10 Subjects
                                                                                                                                                                                        100 Sequences
                                                                                                                                                                   Upper Body Part
                                                                                Part Of Body (hand,                                                                                     (more Than 250k
 Pandora             Borghi et al. (2017)                              2017                           TOF                Kinect V2             Color, Depth        Person Pose
                                                                                Head, Etc.)                                                                                             Frames) From 20
                                                                                                                                                                   (Skeleton)
                                                                                                                                                                                        Subjects
                                                                                Part Of Body (hand,                                                                Segmentation,
 RHD                 Zimmermann and Brox (2017)                        2017                           -                  Synthetic             Color, Depth                             43986 Images
                                                                                Head, Etc.)                                                                        Keypoints
                                                                                Part Of Body (hand,                      PrimeSense
 THU-READ            Tang et al. (2017)                                2017                           Structured Light                         Color, Depth        -                    1920 Sequences
                                                                                Head, Etc.)                              Carmine
                                                                                Part Of Body (hand,   SCS, Structured    Intel Real Sense                                               12 Sequences
 STB                 Zhang et al. (2017)                               2016                                                                    Color, Depth        -
                                                                                Head, Etc.)           Light              F200, Stereo Camera                                            (18k Images)
                                                                                Part Of Body (hand,
 Creative Senz3D     Memo et al. (2015); Memo and Zanuttigh (2018)     2015                           Structured Light   Creative Senz3D       Color, Depth        -                    1320 Sequences
                                                                                Head, Etc.)
                                                                                Part Of Body (hand,                                                                Eye Points, Head
 EYEDIAP             Funes Mora et al. (2014)                          2014                           Structured Light   Kinect V1             Color, Depth                             94 Sequences
                                                                                Head, Etc.)                                                                        Pose
 Eurecom Kinect                                                                 Part Of Body (hand,
                     Min et al. (2014)                                 2014                           Structured Light   Kinect V1             Color, Depth        Face Points          936 Sequences
 Face                                                                           Head, Etc.)
                                                                                Part Of Body (hand,
 Hand Gesture        Marin et al. (2014, 2016)                         2014                           Structured Light   Kinect V1             Color, Depth        -                    1400 Sequences
                                                                                Head, Etc.)
                                                                                Part Of Body (hand,
 MANIAC              Aksoy et al. (2015)                               2014                           Structured Light   Kinect V1             Color, Depth        -                    103 Sequences
                                                                                Head, Etc.)
                                                                                Part Of Body (hand,                      Synthetic/Kinect
 NYU Hand Pose       Tompson et al. (2014)                             2014                           Structured Light                         Color, Depth        Hand Pose            81009 Frames
                                                                                Head, Etc.)                              V1
                                                                                Part Of Body (hand,                                                                                     255 Sequences
 3DMAD               Nesli and Marcel (2013)                           2013                           Structured Light   Kinect V1             Color, Depth        Eye Points
                                                                                Head, Etc.)                                                                                             (76500 Frames)
                                                                                Part Of Body (hand,                                            Color, Depth,       Activity             50 Sequences (25
 50 Salads           Stein and McKenna (2013)                          2013                           Structured Light   Kinect V1
                                                                                Head, Etc.)                                                    Accelerometer       Classification       People)
                                                                                                                         Kinect V1, Creative
                                                                                Part Of Body (hand,   SCS, Structured
 Dexter 1            Sridhar et al. (2013)                             2013                                              Gesture Camera,       Color, Depth        -                    7 Sequences
                                                                                Head, Etc.)           Light, TOF
                                                                                                                         Stereo Camera
                                                                                                                                               Color, Depth,
                                                                                Part Of Body (hand,                                                                                     870 Images (30
 –                   Xu and Cheng (2013)                               2013                           TOF                SoftKinetic DS 325    Measurand           -
                                                                                Head, Etc.)                                                                                             Subjects)
                                                                                                                                               ShapeHand
 MSRC-12                                                                        Part Of Body (hand,                                                                                     594 Sequences
                     Fothergill et al. (2012)                          2012                           Structured Light   Kinect V1             Color, Depth        -
 Kinect Gesture                                                                 Head, Etc.)                                                                                             (719359 Frames)
                                                                                Part Of Body (hand,
 MSR Gesture3D       Wang et al. (2012a)                               2012                           Structured Light   Kinect V1             Depth               -                    336 Sequences
                                                                                Head, Etc.)
                                                                                Part Of Body (hand,                                                                                     53 People (N/A
 Florence 3D Faces   Bagdanov et al. (2011)                            2011                           -                  Synthetic             Color               -
                                                                                Head, Etc.)                                                                                             Frames/Seqs)

                                                                              Table 10: Datasets of “Medical” Category.

 Dataset Name               Ref.                        Year         Scene Type        Sensor Type            Sensor Name                       Data Modalities         Extra Data      Images/Scenes
                                                                                                              Structured Light
                                                                                       SCS, Structured
 SCARED                     Allan et al. (2021)         2021         Endoscopy                                System (using P300                Color, Depth            -               9 Sequences
                                                                                       Light
                                                                                                              Neo Pico), Stereo Camera
 Colonoscopy CG             Rau et al. (2019)           2019         Endoscopy         -                      Synthetic                         Color, Depth            -               16016 Images
 Endoscopic Video           Mountney et al. (2010)      2010         Endoscopy         SCS                    Stereo Camera                     Color                   -               25 Scenes
                                                                                                                                                                                        100 Irises (72k
 –                          Benalcazar et al. (2020)    2020         Iris Scan         -                      Synthetic                         Color, Depth            -
                                                                                                                                                                                        Images)

Benalcazar, D.P., Zambrano, J.E., Bastias, D., Perez, C.A., Bowyer, K.W.,                                     for Online Recognition of Compound Actions. Computer Vision and Image
   2020. A 3D Iris Scanner From A Single Image Using Convolutional Neural                                     Understanding , 62–72.
   Networks. IEEE Access , 98584–98599.                                                                     Borghi, G., Venturelli, M., Vezzani, R., Cucchiara, R., 2017. Poseidon: Face-
Berman, D., Levy, D., Avidan, S., Treibitz, T., 2021. Underwater Single Image                                 From-Depth for Driver Pose Estimation, in: IEEE Conference on Computer
   Color Restoration Using Haze-Lines and A New Quantitative Dataset. IEEE                                    Vision and Pattern Recognition (CVPR), pp. 4661–4670.
   Transactions on Pattern Analysis and Machine Intelligence , 2822–2837.                                   Borràs, R., Lapedriza, À., Igual, L., 2012. Depth Information In Human Gait
Blanco-Claraco, J.L., Moreno-Duenas, F.A., González-Jiménez, J., 2014. The                                  Analysis: An Experimental Study On Gender Recognition, in: International
   MáLaga Urban Dataset: High-Rate Stereo and LiDAR In A Realistic Urban                                     Conference Image Analysis and Recognition, pp. 98–105.
   Scenario. The International Journal of Robotics Research , 207–214.                                      Burri, M., Nikolic, J., Gohl, P., Schneider, T., Rehder, J., Omari, S., Achtelik,
Bloom, V., Argyriou, V., Makris, D., 2016. Hierarchical Transfer Learning                                     M.W., Siegwart, R., 2016. The Euroc Micro Aerial Vehicle Datasets. The
                                                                                                                                                                  17

   International Journal of Robotics Research , 1157–1163.                             ligent Robots and Systems (IROS), pp. 5055–5061.
Butler, D.J., Wulff, J., Stanley, G.B., Black, M.J., 2012. A Naturalistic Open      Cordts, M., Omran, M., Ramos, S., Rehfeld, T., Enzweiler, M., Benenson, R.,
   Source Movie for Optical Flow Evaluation, in: European Conference on                Franke, U., Roth, S., Schiele, B., 2016. The Cityscapes Dataset for Semantic
   Computer Vision (ECCV), pp. 611–625.                                                Urban Scene Understanding, in: IEEE Conference on Computer Vision and
Buttgen, B., Seitz, P., 2008. Robust Optical Time-Of-Flight Range Imaging              Pattern Recognition (CVPR), pp. 3213–3223.
   Based On Smart Pixel Structures. IEEE Transactions on Circuits and Sys-          Cui, J., Jin, L., Kuang, H., Xu, Q., Schwertfeger, S., 2021. Underwater Depth
   tems I: Regular Papers , 1512–1525.                                                 Estimation for Spherical Images. Journal of Robotics , 6644986.
Cabon, Y., Murray, N., Humenberger, M., 2020. Virtual KITTI 2. arXiv preprint       Dai, A., Chang, A.X., Savva, M., Halber, M., Funkhouser, T., Nießner, M.,
   arXiv:2001.10773 , 1–11.                                                            2017. Scannet: Richly-Annotated 3D Reconstructions Of Indoor Scenes, in:
Caesar, H., Bankiti, V., Lang, A.H., Vora, S., Liong, V.E., Xu, Q., Krishnan, A.,      IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp.
   Pan, Y., Baldan, G., Beijbom, O., 2020. Nuscenes: A Multimodal Dataset              2432–2443.
   for Autonomous Driving, in: IEEE Conference on Computer Vision and               Deitke, M., Han, W., Herrasti, A., Kembhavi, A., Kolve, E., Mottaghi, R.,
   Pattern Recognition (CVPR), pp. 11621–11631.                                        Salvador, J., Schwenk, D., VanderBilt, E., Wallingford, M., 2020. Robothor:
Cai, Z., Han, J., Liu, L., Shao, L., 2017. RGB-D Datasets Using Microsoft              An Open Simulation-To-Real Embodied AI Platform, in: IEEE Conference
   Kinect Or Similar Sensors: A Survey. Multimedia Tools and Applications ,            on Computer Vision and Pattern Recognition (CVPR), pp. 3164–3174.
   4313–4355.                                                                       Dosovitskiy, A., Ros, G., Codevilla, F., Lopez, A., Koltun, V., 2017. CARLA:
Camplani, M., Maddalena, L., Moyá Alcover, G., Petrosino, A., Salgado, L.,            An Open Urban Driving Simulator, in: 1st Annual Conference on Robot
   2017. A Benchmarking Framework for Background Subtraction in RGBD                   Learning, pp. 1–16.
   Videos, in: International Conference on Image Analysis and Processing, pp.       Dreher, C.R.G., Wächter, M., Asfour, T., 2020. Learning Object-Action Rela-
   219–229.                                                                            tions from Bimanual Human Demonstration Using Graph Networks. IEEE
Carletti, V., Foggia, P., Percannella, G., Saggese, A., Vento, M., 2016. Recog-        Robotics and Automation Letters (RA-L) , 187–194.
   nition of Human Actions from RGB-D Videos Using a Reject Option, in:             Déziel, J.L., Merriaux, P., Tremblay, F., Lessard, D., Plourde, D., Stanguennec,
   International Workshop on Social Behaviour Analysis, pp. 436—-445.                  J., Goulet, P., Olivier, P., 2021. Pixset : An Opportunity for 3D Computer
Chang, A., Dai, A., Funkhouser, T., Halber, M., Niessner, M., Savva, M., Song,         Vision To Go Beyond Point Clouds With A Full-Waveform LiDAR Dataset.
   S., Zeng, a., Zhang, Y., 2017. Matterport3D: Learning From RGB-D Data               arXiv preprint arXiv:2102.12010 , 1–8.
   In Indoor Environments, in: International Conference on 3D Vision (3DV),         Eftekhar, A., Sax, A., Malik, J., Zamir, A., 2021. Omnidata: A Scalable
   pp. 667–676.                                                                        Pipeline for Making Multi-Task Mid-Level Vision Datasets From 3D Scans,
Chang, M.F., Lambert, J., Sangkloy, P., Singh, J., Bak, S., Hartnett, A., Wang,        in: IEEE International Conference on Computer Vision (ICCV), pp. 10786–
   D., Carr, P., Lucey, S., Ramanan, D., Hays, J., 2019. Argoverse: 3D Track-          10796.
   ing and Forecasting With Rich Maps, in: IEEE Conference on Computer              Escalera, S., Gonzàlez, J., Baró, X., Reyes, M., Lopes, O., Guyon, I., Athit-
   Vision and Pattern Recognition (CVPR), pp. 8740–8749.                               sos, V., Escalante, H., 2013. Multi-Modal Gesture Recognition Challenge
Chen, C., Jafari, R., Kehtarnavaz, N., 2015. UTD-MHAD: A Multimodal                    2013: Dataset and Results, in: 15th ACM on International conference on
   Dataset for Human Action Recognition Utilizing A Depth Camera and A                 multimodal interaction, pp. 445–452.
   Wearable Inertial Sensor, in: IEEE International conference on image pro-        Firman, M., 2016. RGBD Datasets: Past, Present and Future, in: IEEE Confer-
   cessing (ICIP), pp. 168–172.                                                        ence on Computer Vision and Pattern Recognition Workshops (CVPRW),
Chen, L., Liu, F., Zhao, Y., Wang, W., Yuan, X., Zhu, J., 2020a. Valid: A Com-         pp. 19–31.
   prehensive Virtual Aerial Image Dataset, in: IEEE International Conference       Fisher, R.B., Konolige, K., 2008. Range Sensors. pp. 521–542.
   on Robotics and Automation (ICRA), pp. 2009–2016.                                Fonder, M., Van Droogenbroeck, M., 2019. Mid-Air: A Multi-Modal Dataset
Chen, W., Fu, Z., Yang, D., Deng, J., 2016. Single-Image Depth Perception In           for Extremely Low Altitude Drone Flights, in: IEEE Conference on Com-
   The Wild, in: 30th International Conference on Neural Information Process-          puter Vision and Pattern Recognition Workshops (CVPRW), pp. 553–562.
   ing Systems, p. 730–738.                                                         Foster, K., Christie, G., Brown, M., 2020. Urban Semantic 3D Dataset.
Chen, W., Qian, S., Deng, J., 2019. Learning Single-Image Depth From Videos         Fothergill, S., Mentis, H., Kohli, P., Nowozin, S., 2012. Instructing People for
   Using Quality Assessment Networks, in: IEEE Conference on Computer                  Training Gestural Interactive Systems, in: SIGCHI Conference on Human
   Vision and Pattern Recognition (CVPR), pp. 5604–5613.                               Factors in Computing Systems, p. 1737–1746.
Chen, W., Qian, S., Fan, D., Kojima, N., Hamilton, M., Deng, J., 2020b. Oasis:      Funes Mora, K.A., Monay, F., Odobez, J.M., 2014. Eyediap: A Database
   A Large-Scale Dataset for Single Image 3D In The Wild, in: IEEE Confer-             for The Development and Evaluation Of Gaze Estimation Algorithms From
   ence on Computer Vision and Pattern Recognition (CVPR), pp. 679–688.                RGB and RGB-D Cameras, in: Symposium on Eye Tracking Research and
Cho, J., Min, D., Kim, Y., Sohn, K., 2021a. Deep Monocular Depth Estimation            Applications, pp. 255–258.
   Leveraging A Large-Scale Outdoor Stereo Dataset. Expert Systems with             Gaglio, S., Re, G.L., Morana, M., 2015. Human Activity Recognition Process
   Applications , 114877.                                                              Using 3-D Posture Data. IEEE Transactions on Human-Machine Systems ,
Cho, J., Min, D., Kim, Y., Sohn, K., 2021b. Deep Monocular Depth Estimation            586–597.
   Leveraging A Large-Scale Outdoor Stereo Dataset. Expert Systems with             Gaidon, A., Wang, Q., Cabon, Y., Vig, E., 2016. Virtualworlds As Proxy for
   Applications , 114877.                                                              Multi-Object Tracking Analysis, in: IEEE Conference on Computer Vision
Choi, J., 2019. Range Sensors: Ultrasonic Sensors, Kinect, and LiDAR. pp.              and Pattern Recognition (CVPR), pp. 4340–4349.
   2521–2538.                                                                       Garcia-Hernando, G., Yuan, S., Baek, S., Kim, T.K., 2018. First-Person Hand
Choi, S., Zhou, Q.Y., Koltun, V., 2015. Robust Reconstruction Of Indoor                Action Benchmark With RGB-D Videos and 3D Hand Pose Annotations, in:
   Scenes, in: IEEE Conference on Computer Vision and Pattern Recognition              IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp.
   (CVPR), pp. 5556–5565.                                                              409–419.
Choi, S., Zhou, Q.Y., Miller, S., Koltun, V., 2016. A Large Dataset Of Object       Garg, R., Wadhwa, N., Ansari, S., Barron, J.T., 2019. Learning Single Camera
   Scans. arXiv preprint arXiv:1602.02481 , 1–7.                                       Depth Estimation Using Dual-Pixels, in: IEEE International Conference on
Chunhui, L., Yueyu, H., Yanghao, L., Sijie, S., Jiaying, L., 2017. PKU-MMD:            Computer Vision (ICCV), pp. 7628–7637.
   A Large Scale Benchmark for Continuous Multi-Modal Human Action Un-              Gasparrini, S., Cippitelli, E., Gambi, E., Spinsante, S., Florez-Revuelta, F.,
   derstanding. arXiv preprint arXiv:1703.07475 , 1–10.                                2015a. Performance Analysis Of Self-Organising Neural Networks Track-
Cippitelli, E., Gasparrini, S., Gambi, E., Spinsante, S., Wåhslény, J., Orhany,       ing Algorithms for Intake Monitoring Using Kinect, in: IET International
   I., Lindhy, T., 2015. Time Synchronization and Data Fusion for RGB-Depth            Conference on Technologies for Active and Assisted Living (TechAAL),
   Cameras and Inertial Sensors In AAL Applications, in: IEEE International            pp. 1–6.
   Conference on Communication Workshop (ICCW), pp. 265–270.                        Gasparrini, S., Cippitelli, E., Gambi, E., Spinsante, S., Wåhslén, J., Orhan, I.,
Ciptadi, A., Hermans, T., Rehg, J.M., 2013. An In Depth View of Saliency, in:          Lindh, T., 2015b. Proposal and Experimental Evaluation Of Fall Detection
   British Machine Vision Conference (BMVC), pp. 1–11.                                 Solution Based On Wearable and Depth Data Fusion, in: International con-
Coppola, C., Faria, D., Nunes, U., Bellotto, N., 2016. Social Activity Recog-          ference on ICT innovations, pp. 99–108.
   nition based on Probabilistic Merging of Skeleton Features with Proximity        Gasparrini, S., Cippitelli, E., Spinsante, S., Gambi, E., 2014. A Depth-Based
   Priors from RGB-D Data, in: IEEE/RSJ International Conference on Intel-             Fall Detection System Using A Kinect® Sensor. Sensors , 2756–2775.
                                                                                                                                                                   18

Gehrig, D., Ruegg, M., Gehrig, M., Hidalgo-Carrio, J., Scaramuzza, D., 2021a.           pp. 410–424.
   Combining Events and Frames Using Recurrent Asynchronous Multimodal              Ionescu, C., Papava, D., Olaru, V., Sminchisescu, C., 2014. Human3.6M: Large
   Networks for Monocular Depth Prediction. IEEE Robotic and Automation                 Scale Datasets and Predictive Methods for 3D Human Sensing In Natural
   Letters. (RA-L) , 2822–2829.                                                         Environments. IEEE Transactions on Pattern Analysis and Machine Intelli-
Gehrig, M., Aarents, W., Gehrig, D., Scaramuzza, D., 2021b. DSEC: A Stereo              gence , 1325–1339.
   Event Camera Dataset for Driving Scenarios. IEEE Robotics and Automa-            Janoch, A., Karayev, S., Jia, Y., Barron, J.T., Fritz, M., Saenko, K., Darrell, T.,
   tion Letters , 4947–4954.                                                            2013. A Category-Level 3D Object Dataset: Putting The Kinect To Work,
Geiger, A., Lenz, P., Stiller, C., Urtasun, R., 2013. Vision Meets Robotics:            in: Consumer depth cameras for computer vision, pp. 141–165.
   The KITTI Dataset. International Journal of Robotics Research (IJRR) ,           Jensen, R., Dahl, a., Vogiatzis, G., Tola, E., Aanæs, H., 2014. Large Scale
   1231–1237.                                                                           Multi-View Stereopsis Evaluation, in: IEEE Conference on Computer Vi-
Geiger, A., Lenz, P., Urtasun, R., 2012. Are We Ready for Autonomous Driv-              sion and Pattern Recognition (CVPR), pp. 406–413.
   ing? The KITTI Vision Benchmark Suite, in: IEEE Conference on Com-               Jeong, J., Cho, Y., Shin, Y.S., Roh, H., Kim, A., 2019. Complex Urban Dataset
   puter Vision and Pattern Recognition (CVPR), pp. 3354–3361.                          With Multi-Level Sensors From Highly Diverse Urban Environments. Inter-
Geiger, A., Ziegler, J., Stiller, C., 2011. Stereoscan: Dense 3D Reconstruction         national Journal of Robotics Research , 642–657.
   In Real-Time, in: IEEE Intelligent Vehicles Symposium (IV), pp. 963–968.         Ji, P., Li, R., Bhanu, B., Xu, Y., 2021. Monoindoor: Towards good practice
Georgakis, G., Reza, M.A., Mousavian, A., Le, P.H., Košecká, J., 2016. Multi-         of self-supervised monocular depth estimation for indoor environments, in:
   view RGB-D Dataset for Object Instance Detection, in: Fourth International           IEEE International Conference on Computer Vision (ICCV), pp. 12787–
   Conference on 3D Vision (3DV), pp. 426–434.                                          12796.
Gil, Y., Elmalem, S., Haim, H., Marom, E., Giryes, R., 2019. Monster: Awak-         Ji, Y., Xu, F., Yang, Y., Shen, F., Shen, H.T., Zheng, W.S., 2019. A Large-
   ening The Mono In Stereo. arXiv preprint arXiv:1910.13708 , 1–13.                    scale Varying-view RGB-D Action Dataset for Arbitrary-view Human Ac-
Glocker, B., Izadi, S., Shotton, J., Criminisi, A., 2013. Real-Time RGB-D               tion Recognition. arXiv preprint arXiv:1904.10681 , 187–194.
   Camera Relocalization, in: IEEE International Symposium on Mixed and             Jokela, M., Kutila, M., Pyykönen, P., 2019. Testing and Validation Of Automo-
   Augmented Reality (ISMAR), pp. 173–179.                                              tive Point-Cloud Sensors In Adverse Weather Conditions. Applied Sciences
Guizilini, V., Ambrus, , R., Pillai, S., Raventos, A., Gaidon, A., 2020. 3D Pack-       , 2341.
   ing for Self-Supervised Monocular Depth Estimation, in: IEEE Conference          Joo, H., Simon, T., Li, X., Liu, H., Tan, L., Gui, L., Banerjee, S., Godisart,
   on Computer Vision and Pattern Recognition (CVPR), pp. 2482–2491.                    T.S., Nabbe, B., Matthews, I., Kanade, T., Nobuhara, S., Sheikh, Y., 2017.
Guo, X., Li, H., Yi, S., Ren, J., Wang, X., 2018. Learning Monocular Depth              Panoptic Studio: A Massively Multiview System for Social Interaction Cap-
   by Distilling Cross-domain Stereo Networks, in: European Conference on               ture. IEEE Transactions on Pattern Analysis and Machine Intelligence ,
   Computer Vision (ECCV), pp. 484–500.                                                 190–204.
Guyon, I., Athitsos, V., Jangyodsuk, P., Escalante, H.J., 2014. The Chalearn        Kashani, A.G., Olsen, M.J., Parrish, C.E., Wilson, N., 2015. A Review Of LI-
   Gesture Dataset (Cgd 2011). Machine Vision and Applications , 1929–1951.             DAR Radiometric Processing: From Ad Hoc Intensity Correction To Rigor-
Haala, N., Cramer, M., Jacobsen, K., 2010. The German Camera Evaluation                 ous Radiometric Calibration. Sensors , 28099–28128.
   Project-Results From The Geometry Group, in: International Archives of the       Kazmi, W., Foix, S., Alenya, G., 2012. Plant Leaf Imaging Using Time Of
   Photogrammetry, Remote Sensing and Spatial Information Sciences: Cana-               Flight Camera Under Sunlight, Shadow and Room Conditions, in: IEEE In-
   dian Geomatics Conference and Symposium Of Commission I, ISPRS Con-                  ternational Symposium on Robotic and Sensors Environments Proceedings,
   vergence In Geomatics-Shaping Canada’s Competitive Landscape, pp. 1–6.               pp. 192–197.
Hadfield, S., Bowden, R., 2013. Hollywood 3D: Recognizing Actions In                Keller, C.G., Enzweiler, M., Gavrila, D.M., 2011. A New Benchmark for
   3D Natural Scenes, in: IEEE Conference on Computer Vision and Pattern                Stereo-Based Pedestrian Detection, in: IEEE Intelligent Vehicles Sympo-
   Recognition (CVPR), pp. 3398–3405.                                                   sium (IV), pp. 691–696.
Handa, A., Whelan, T., McDonald, J., Davison, A.J., 2014. A Benchmark for           Keltjens, B., van Dijk, T., de Croon, G., 2021. Self-Supervised Monocular
   RGB-D Visual Odometry, 3D Reconstruction and Slam, in: IEEE Interna-                 Depth Estimation of Untextured Indoor Rotated Scenes. arXiv preprint
   tional Conference on Robotics and Automation (ICRA), pp. 1524–1531.                  arXiv:2106.12958 , 1–13.
Hasson, Y., Varol, G., Tzionas, D., Kalevatykh, I., Black, M.J., Laptev, I.,        Koch, T., Liebel, L., Fraundorfer, F., Körner, M., 2019. Evaluation of CNN-
   Schmid, C., 2019. Learning Joint Reconstruction Of Hands and Manipulated             Based Single-Image Depth Estimation Methods, in: European Conference
   Objects, in: IEEE Conference on Computer Vision and Pattern Recognition              on Computer Vision Workshops (ECCV-WS), pp. 331–348.
   (CVPR), pp. 11807–11816.                                                         Kopf, J., Rong, X., Huang, J.B., 2021. Robust consistent video depth estima-
Hirschmüller, H., Scharstein, D., 2007. Evaluation Of Cost Functions for Stereo        tion, in: IEEE International Conference on Computer Vision (ICCV), pp.
   Matching. IEEE Conference on Computer Vision and Pattern Recognition                 1611–1621.
   (CVPR) , 1–8.                                                                    Kwolek, B., Kepski, M., 2014. Human Fall Detection On Embedded Platform
Hodaň, T., Haluza, P., Obdržálek, Š., Matas, J., Lourakis, M., Zabulis, X.,         Using Depth Maps and Wireless Accelerometer. Computer methods and
   2017. T-Less: An RGB-D Dataset for 6D Pose Estimation Of Texture-                    programs in biomedicine , 489–501.
   Less Objects. IEEE Winter Conference on Applications of Computer Vision          Lai, K., Bo, L., Fox, D., 2014. Unsupervised Feature Learning for 3D Scene
   (WACV) , 880–888.                                                                    Labeling, in: IEEE International Conference on Robotics and Automation
Honauer, K., Johannsen, O., Kondermann, D., Goldluecke, B., 2016. A Dataset             (ICRA), pp. 3050–3057.
   and Evaluation Methodology for Depth Estimation On 4D Light Fields, in:          Lai, K., Bo, L., Ren, X., Fox, D., 2011. A Large-Scale Hierarchical Multi-View
   The Asian Conference on Computer Vision (ACCV, pp. 19–34.                            RGB-D Object Dataset, in: IEEE International Conference on Robotics and
Hornauer, J., Nalpantidis, L., Belagiannis, V., 2021. Visual Domain Adaptation          Automation, pp. 1817–1824.
   for Monocular Depth Estimation on Resource-Constrained Hardware, in:             Lai, P.K., Xie, S., Lang, J., Laganière, R., 2019. Real-Time Panoramic Depth
   IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pp.               Maps From Omni-Directional Stereo Images for 6 Dof Videos In Virtual
   954–962.                                                                             Reality, in: IEEE Conference on Virtual Reality and 3D User Interfaces
Houston, J., Zuidhof, G., Bergamini, L., Ye, Y., Chen, L., Jain, A., Omari,             (VR), pp. 405–412.
   S., Iglovikov, V., Ondruska, P., 2020. One Thousand and One Hours: Self-         Lenz, I., Lee, H., Saxena, A., 2015. Deep Learning for Detecting Robotic
   Driving Motion Prediction Dataset. arXiv preprint arXiv:2006.14480 , 1–10.           Grasps. The International Journal of Robotics Research , 705–724.
Hu, J.F., Zheng, W.S., Lai, J., Zhang, J., 2017. Jointly Learning Heterogeneous     Levinson, J., Askeland, J., Becker, J., Dolson, J., Held, D., Kammel, S., Kolter,
   Features for RGB-D Activity Recognition. IEEE Transactions on Pattern                J.Z., Langer, D., Pink, O., Pratt, V., Sokolsky, M., Stanek, G., Stavens, D.,
   Analysis and Machine Intelligence , 2186–2200.                                       Teichman, A., Werling, M., Thrun, S., 2011. Towards Fully Autonomous
Hua, Y., Kohli, P., Uplavikar, P., Ravi, A., Gunaseelan, S., Orozco, J., Li, E.,        Driving: Systems and Algorithms, in: IEEE Intelligent Vehicles Symposium
   2020. Holopix50K: A Large-Scale In-The-Wild Stereo Image Dataset, in:                (IV), pp. 163–168.
   CVPR Workshop on Computer Vision for Augmented and Virtual Reality,              Li, M., Zhou, Z., Wu, Z., Shi, B., Diao, C., Tan, P., 2020. Multi-View Photomet-
   pp. 1–5.                                                                             ric Stereo: A Robust Solution and Benchmark Dataset for Spatially Varying
Huang, D., Yao, S., Wang, Y., Torre, F.D.L., 2014. Sequential Max-Margin                Isotropic Materials. IEEE Transactions on Image Processing , 4159–4173.
   Event Detectors, in: European Conference on Computer Vision (ECCV),              Li, N., Ye, J., Ji, Y., Ling, H., Yu, J., 2014. Saliency Detection On Light Field,
                                                                                                                                                                  19

    in: IEEE Conference on Computer Vision and Pattern Recognition (CVPR),             The Visual and Depth Robot Indoor Localization With Objects Information
    pp. 2806–2813.                                                                     Dataset. The International Journal of Robotics Research , 1681–1687.
Li, W., Saeedi, S., McCormac, J., Clark, R., Tzoumanikas, D., Ye, Q., Huang,        Mason, J., Marthi, B., Parr, R., 2012. Object Disappearance for Object Dis-
    Y., Tang, R., Leutenegger, S., 2018. Interiornet: Mega-Scale Multi-Sensor          covery, in: IEEE/RSJ International Conference on Intelligent Robots and
    Photo-Realistic Indoor Scenes Dataset, in: British Machine Vision Confer-          Systems, pp. 2836–2843.
    ence (BMVC), pp. 1–13.                                                          Mattausch, O., Panozzo, D., Mura, C., Sorkine-Hornung, O., Pajarola, R.,
Li, W., Zhang, Z., Liu, Z., 2010. Action Recognition Based On A Bag Of 3D              2014. Object Detection and Classification From Large-Scale Cluttered In-
    Points, in: IEEE Conference on Computer Vision and Pattern Recognition             door Scans. Computer Graphics Forum , 11–21.
    Workshops (CVPRW), pp. 9–14.                                                    Mayer, N., Ilg, E., Häusser, P., Fischer, P., Cremers, D., Dosovitskiy, A., Brox,
Li, Y., Dai, A., Guibas, L., Nießner, M., 2015. Database-Assisted Object Re-           T., 2016. A Large Dataset To Train Convolutional Networks for Disparity,
    trieval for Real-Time 3D Reconstruction, in: Computer Graphics Forum, pp.          Optical Flow, and Scene Flow Estimation, in: IEEE Conference on Com-
    435–446.                                                                           puter Vision and Pattern Recognition (CVPR), pp. 4040–4048.
Li, Z., Dekel, T., Cole, F., Tucker, R., Snavely, N., Liu, C., Freeman, W.T.,       McCormac, J., Handa, A., Leutenegger, S., Davison, A.J., 2017. Scenenet
    2019. Learning The Depths Of Moving People By Watching Frozen People,              RGB-D: Can 5M Synthetic Images Beat Generic Imagenet Pre-Training On
    in: IEEE Conference on Computer Vision and Pattern Recognition (CVPR),             Indoor Segmentation?, in: IEEE International Conference on Computer Vi-
    pp. 4516–4525.                                                                     sion (ICCV), pp. 2697–2706.
Li, Z., Snavely, N., 2018a. Megadepth: Learning Single-View Depth Prediction        Meister, S., Izadi, S., Kohli, P., Hämmerle, M., Rother, C., Kondermann, D.,
    From Internet Photos, in: IEEE Conference on Computer Vision and Pattern           2012. When Can We Use Kinectfusion for Ground Truth Acquisition, in:
    Recognition (CVPR), pp. 2041–2050.                                                 Proc. Workshop on Color-Depth Camera Fusion in Robotics, p. 3.
Li, Z., Snavely, N., 2018b. Megadepth: Learning Single-View Depth Prediction        Memo, A., Minto, L., Zanuttigh, P., 2015. Exploiting Silhouette Descriptors
    From Internet Photos, in: IEEE Conference on Computer Vision and Pattern           and Synthetic Data for Hand Gesture Recognition , 1–9.
    Recognition (CVPR), pp. 2041–2050.                                              Memo, A., Zanuttigh, P., 2018. Head-mounted gesture controlled interface for
Liao, Y., Xie, J., Geiger, A., 2021. KITTI-360: A Novel Dataset and Bench-             human-computer interaction. Multimedia Tools and Applications , 27–53.
    marks for Urban Scene Understanding In 2D and 3D. arXiv preprint                Miangoleh, S.M.H., Dille, S., Mai, L., Paris, S., Aksoy, Y., 2021. Boost-
    arXiv:2109.13410 , 1–31.                                                           ing Monocular Depth Estimation Models To High-Resolution Via Content-
Liciotti, D., Paolanti, M., Frontoni, E., Mancini, A., Zingaretti, P., 2017. Per-      Adaptive Multi-Resolution Merging, in: IEEE Conference on Computer Vi-
    son Re-Identification Dataset With RGB-D Camera In A Top-View Config-              sion and Pattern Recognition (CVPR), pp. 9685–9694.
    uration, in: Video Analytics. Face and Facial Expression Recognition and        Min, R., Kose, N., Dugelay, J.L., 2014. Kinectfacedb: A Kinect Database for
    Audience Measurement, pp. 1–11.                                                    Face Recognition. Systems, Man, and Cybernetics: Systems, IEEE Trans-
Liu, J., Shahroudy, A., Perez, M., Wang, G., Duan, L.Y., Kot, A.C., 2019. NTU          actions on , 1534–1548.
    RGB+D 120: A Large-Scale Benchmark for 3D Human Activity Under-                 Mountney, P., Stoyanov, D., Yang, G.Z., 2010. Three-Dimensional Tissue De-
    standing. IEEE Transactions on Pattern Analysis and Machine Intelligence           formation Recovery and Tracking. IEEE Signal Processing Magazine , 14–
    , 2684–2701.                                                                       24.
Liu, N., Zhang, N., Shao, L., Han, J., 2021. Learning Selective Mutual At-          Munaro, M., Ballin, G., Michieletto, S., Menegatti, E., 2013. 3D Flow Esti-
    tention and Contrast for RGB-D Saliency Detection. IEEE Transactions on            mation for Human Action Recognition from Colored Point Clouds. Biolog-
    Pattern Analysis and Machine Intelligence , 1–14.                                  ically Inspired Cognitive Architectures , 42–51.
Lopez-Campos, R., Martinez-Carranza, J., 2021. Espada: Extended Synthetic           Nesli, E., Marcel, S., 2013. Spoofing In 2D Face Recognition With 3D Masks
    and Photogrammetric Aerial-Image Dataset. IEEE Robotics and Automa-                and Anti-Spoofing With Kinect, in: IEEE 6th International Conference on
    tion Letters , 1–1.                                                                Biometrics: Theory, Applications and Systems (BTAS’13), pp. 1–8.
Lopez-Rodriguez, A., Mikolajczyk, K., 2020. DESC: Domain adaptation for             Niklaus, S., Mai, L., Yang, J., Liu, F., 2019. 3D Ken Burns Effect From A
    depth estimation via semantic consistency. arXiv preprint arXiv:2009.01579         Single Image. ACM Transactions on Graphics (ToG) , 1–15.
    , 1–16.                                                                         Ofli, F., Chaudhry, R., Kurillo, G., Vidal, R., Bajcsy, R., 2013. Berkeley Mhad:
Lu, C.X., Saputra, M.R.U., Zhao, P., Almalioglu, Y., de Gusmao, P.P.B., Chen,          A Comprehensive Multimodal Human Action Database, in: IEEE Workshop
    C., Sun, K., Trigoni, N., Markham, A., 2020. Milliego: Single-Chip                 on Applications of Computer Vision (WACV), pp. 53–60.
    Mmwave Radar Aided Egomotion Estimation Via Deep Sensor Fusion, in:             O’Toole, M., Achar, S., Narasimhan, S.G., Kutulakos, K.N., 2015. Homoge-
    18th Conference on Embedded Networked Sensor Systems, p. 109–122.                  neous Codes for Energy-Efficient Illumination and Imaging. ACM Transac-
Luo, X., Huang, J.B., Szeliski, R., Matzen, K., Kopf, J., 2020. Consistent Video       tions on Graphics (ToG) , 1–13.
    Depth Estimation. ACM Transactions on Graphics (ToG) , 71–1.                    Pandey, G., McBride, J.R., Eustice, R.M., 2011. Ford Campus Vision and Lidar
Maddern, W., Pascoe, G., Linegar, C., Newman, P., 2017. 1 Year, 1000Km: The            Data Set. The International Journal of Robotics Research , 1543–1552.
    Oxford Robotcar Dataset. The International Journal of Robotics Research         Peng, H., Li, B., Xiong, W., Hu, W., Ji, R., 2014. RGBD Salient Object Detec-
    (IJRR) , 3–15.                                                                     tion: A Benchmark and Algorithms, in: European Conference on Computer
Malleson, C., Guillemaut, J., Hilton, A., 2019. Hybrid Modeling Of Non-Rigid           Vision (ECCV), pp. 92–109.
    Scenes From RGBD Cameras. IEEE Transactions on Circuits and Systems             Pfeiffer, D., Gehrig, S., Schneider, N., 2013. Exploiting The Power Of Stereo
    for Video Technology , 2391–2404.                                                  Confidences, in: IEEE Conference on Computer Vision and Pattern Recog-
Mancini, M., Costante, G., Valigi, P., Ciarfuglia, T.A., 2018. J-Mod 2: Joint          nition (CVPR), pp. 297–304.
    Monocular Obstacle Detection and Depth Estimation. IEEE Robotics and            Piao, Y., Ji, W., Li, J., Zhang, M., Lu, H., 2019. Depth-induced Multi-scale
    Automation Letters , 1490–1497.                                                    Recurrent Attention Network for Saliency Detection, in: IEEE International
Mancini, M., Costante, G., Valigi, P., Ciarfuglia, T.A., Delmerico, J., Scara-         Conference on Computer Vision (ICCV), pp. 7254–7263.
    muzza, D., 2017. Toward Domain Independence for Learning-Based                  Planche, B., Wu, Z., Ma, K., Sun, S., Kluckner, S., Lehmann, O., Chen, T.,
    Monocular Depth Estimation. IEEE Robotics and Automation Letters ,                 Hutter, A., Zakharov, S., Kosch, H., Ernst, J., 2017. DepthSynth: Real-Time
    1778–1785.                                                                         Realistic Synthetic Data Generation from CAD Models for 2.5D Recogni-
Manglik, A., Weng, X., Ohn-Bar, E., Kitanil, K.M., 2019. Forecasting Time-             tion, in: International Conference on 3D Vision (3DV), pp. 1–10.
    To-Collision From Monocular Video: Feasibility, Dataset, and Challenges,        Pomerleau, F., Magnenat, S., Colas, F., Liu, M., Siegwart, R., 2011. Tracking
    in: IEEE/RSJ International Conference on Intelligent Robots and Systems            A Depth Camera: Parameter Exploration for Fast Icp, in: IEEE/RSJ Inter-
    (IROS), pp. 8081–8088.                                                             national Conference on Intelligent Robots and Systems, pp. 3824–3829.
Marin, G., Dominio, F., Zanuttigh, P., 2014. Hand Gesture Recognition with          Quattrini Li, A., Coskun, A., Doherty, S.M., Ghasemlou, S., Jagtap, A.S.,
    Leap Motion and Kinect Devices, in: IEEE International Conference on               Modasshir, M., Rahman, S., Singh, A., Xanthidis, M., O’Kane, J.M., Rek-
    Image Processing (ICIP), pp. 1565–1569.                                            leitis, I., 2017. Experimental Comparison Of Open Source Vision-Based
Marin, G., Dominio, F., Zanuttigh, P., 2016. Hand gesture recognition with             State Estimation Algorithms, in: International Symposium on Experimental
    jointly calibrated leap motion and depth sensor. Multimedia Tools and Ap-          Robotics, pp. 775–786.
    plications , 14991–15015.                                                       Ramakrishnan, S.K., Gokaslan, A., Wijmans, E., Maksymets, O., Clegg, A.,
Martı́nez-Gómez, J., Garcı́a-Varea, I., Cazorla, M., Morell, V., 2015. Vidrilo:       Turner, J., Undersander, E., Galuba, W., Westbury, A., Chang, A.X., 2021.
                                                                                                                                                                      20

   Habitat-Matterport 3D Dataset (Hm3D): 1000 Large-Scale 3D Environ-                       A Medium-Level Model for Real-Time Semantic Scene Understanding, in:
   ments for Embodied AI. arXiv preprint arXiv:2109.08238 , 1–21.                           European Conference on Computer Vision (ECCV), pp. 533–548.
Ramamonjisoa, M., Du, Y., Lepetit, V., 2020. Predicting Sharp and Accurate               Schilling, H., Gutsche, M., Brock, A., Spath, D., Rother, C., Krispin, K., 2020.
   Occlusion Boundaries In Monocular Depth Estimation Using Displacement                    Mind The Gap-A Benchmark for Dense Depth Prediction Beyond Lidar, in:
   Fields, in: IEEE Conference on Computer Vision and Pattern Recognition                   IEEE Conference on Computer Vision and Pattern Recognition Workshops
   (CVPR), pp. 14636–14645.                                                                 (CVPRW), pp. 338–339.
Ramezani, M., Wang, Y., Camurri, M., Wisth, D., Mattamala, M., Fallon, M.,               Schöning, J., Heidemann, G., 2015. Evaluation Of Multi-View 3D Reconstruc-
   2020. The Newer College Dataset: Handheld LiDAR, Inertial and Vision                     tion Software, in: Computer Analysis of Images and Patterns, pp. 450–461.
   With Ground Truth, in: IEEE/RSJ International Conference on Intelligent               Schönbein, M., Strauß, T., Geiger, A., 2014. Calibrating and Centering
   Robots and Systems (IROS), pp. 4353–4360.                                                Quasi-Central Catadioptric Cameras, in: IEEE International Conference on
Ranftl, R., Bochkovskiy, A., Koltun, V., 2021a. Vision Transformers for Dense               Robotics and Automation (ICRA), pp. 4443–4450.
   Prediction, in: IEEE Conference on Computer Vision and Pattern Recogni-               Schöps, T., Schönberger, J.L., Galliani, S., Sattler, T., Schindler, K., Polle-
   tion (CVPR), pp. 12179–12188.                                                            feys, M., Geiger, A., 2017. A Multi-View Stereo Benchmark With High-
Ranftl, R., Bochkovskiy, A., Koltun, V., 2021b. Vision Transformers for Dense               Resolution Images and Multi-Camera Videos, in: IEEE Conference on
   Prediction, in: IEEE Conference on Computer Vision and Pattern Recogni-                  Computer Vision and Pattern Recognition (CVPR), pp. 2538–2547.
   tion (CVPR), pp. 12179–12188.                                                         Seidenari, L., Varano, V., Berretti, S., Del Bimbo, A., Pala, P., 2013. Recog-
Ranftl, R., Lasinger, K., Hafner, D., Schindler, K., Koltun, V., 2020. Towards              nizing Actions from Depth Cameras as Weakly Aligned Multi-part Bag-of-
   Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-                  Poses, in: IEEE Conference on Computer Vision and Pattern Recognition
   Dataset Transfer. IEEE Transactions on Pattern Analysis and Machine In-                  Workshops (CVPRW), pp. 479–485.
   telligence (TPAMI) , 1–14.                                                            Seychell, D., Debono, C.J., Bugeja, M., Borg, J., Sacco, M., 2021. COTS: A
Rau, A., Edwards, P.E., Ahmad, O.F., Riordan, P., Janatka, M., Lovat, L.B.,                 Multipurpose RGB-D Dataset for Saliency and Image Manipulation Appli-
   Stoyanov, D., 2019. Implicit Domain Adaptation With Conditional Genera-                  cations. IEEE Access , 21481–21497.
   tive Adversarial Networks for Depth Prediction in Endoscopy. International            Shahroudy, A., Liu, J., Ng, T.T., Wang, G., 2016. NTU RGB+D: A Large Scale
   Journal of Computer Assisted Radiology and Surgery , 1–10.                               Dataset for 3D Human Activity Analysis, in: IEEE Conference on Computer
Ren, H., Raj, A., El-Khamy, M., Lee, J., 2020. Suw-Learn: Joint Supervised,                 Vision and Pattern Recognition (CVPR), pp. 1010–1019.
   Unsupervised, Weakly Supervised Deep Learning for Monocular Depth Es-                 Shen, T., Luo, Z., Zhou, L., Zhang, R., Zhu, S., Fang, T., Quan, L., 2018.
   timation, in: IEEE Conference on Computer Vision and Pattern Recognition                 Matchable Image Retrieval By Learning From Surface Reconstruction, in:
   Workshops (CVPRW), pp. 750–751.                                                          The Asian Conference on Computer Vision (ACCV, pp. 415–431.
Roberts, M., Ramapuram, J., Ranjan, A., Kumar, A., Bautista, M.A., Paczan,               Shin Yoon, J., Kim, K., Gallo, O., Park, H.S., Kautz, J., 2020. Novel View Syn-
   N., Webb, R., Susskind, J.M., 2021. Hypersim: A Photorealistic Synthetic                 thesis Of Dynamic Scenes With Globally Coherent Depths From A Monoc-
   Dataset for Holistic Indoor Scene Understanding, in: IEEE International                  ular Camera, in: IEEE Conference on Computer Vision and Pattern Recog-
   Conference on Computer Vision (ICCV), pp. 10912–10922.                                   nition (CVPR), pp. 5335–5344.
Ros, G., Sellart, L., Materzynska, J., Vazquez, D., Lopez, A.M., 2016. The               Shu, T., Ryoo, M.S., Zhu, S.C., 2016. Learning Social Affordance for Human-
   Synthia Dataset: A Large Collection Of Synthetic Images for Semantic Seg-                Robot Interaction, in: International Joint Conference on Artificial Intelli-
   mentation Of Urban Scenes, in: IEEE Conference on Computer Vision and                    gence (IJCAI), pp. 3454–3461.
   Pattern Recognition (CVPR), pp. 3234–3243.                                            Silberman, N., Fergus, R., 2011. Indoor Scene Segmentation Using A Struc-
Rotman, D., Gilboa, G., 2016. A Depth Restoration Occlusionless Temporal                    tured Light Sensor, in: IEEE International Conference on Computer Vision
   Dataset, in: Fourth International Conference on 3D Vision (3DV), pp. 176–                Workshops (ICCV Workshops), pp. 601–608.
   184.                                                                                  Silberman, N., Hoiem, D., Kohli, P., Fergus, R., 2012. Indoor Segmentation
Rottensteiner, F., Sohn, G., Jung, J., Gerke, M., Baillard, C., Benitez, S., Bre-           and Support Inference From RGBD Images, in: European Conference on
   itkopf, U., 2012. The Isprs Benchmark On Urban Object Classification and                 Computer Vision (ECCV), pp. 746–760.
   3D Building Reconstruction. ISPRS Annals of the Photogrammetry, Remote                Singh, A., Sha, J., Narayan, K.S., Achim, T., Abbeel, P., 2014. Bigbird: A
   Sensing and Spatial Information Sciences I-3 , 293–298.                                  Large-Scale 3D Database Of Object Instances, in: IEEE International Con-
Rowe, F., 2014. What Literature Review Is Not: Diversity, Boundaries and                    ference on Robotics and Automation (ICRA), pp. 509–516.
   Recommendations. European Journal of Information Systems , 241–255.                   Song, S., Lichtenberg, S.P., Xiao, J., 2015. Sun RGB-D: A RGB-D Scene
Sajjan, S., Moore, M., Pan, M., Nagaraja, G., Lee, J., Zeng, a., Song, S.,                  Understanding Benchmark Suite, in: IEEE Conference on Computer Vision
   2020. Clear Grasp: 3D Shape Estimation Of Transparent Objects for Ma-                    and Pattern Recognition (CVPR), pp. 567–576.
   nipulation, in: IEEE International Conference on Robotics and Automation              Song, S., Xiao, J., 2013. Tracking Revisited Using RGBD Camera: Unified
   (ICRA), pp. 3634–3642.                                                                   Benchmark and Baselines, in: IEEE International Conference on Computer
Salvi, J., Pagès, J., Batlle, J., 2004. Pattern Codification Strategies In Structured      Vision (ICCV), pp. 233–240.
   Light Systems. Pattern Recognition , 827–849.                                         Song, S., Yu, F., Zeng, a., Chang, A.X., Savva, M., Funkhouser, T., 2017.
Savva, M., Kadian, A., Maksymets, O., Zhao, Y., Wijmans, E., Jain, B., Straub,              Semantic Scene Completion From A Single Depth Image. IEEE Conference
   J., Liu, J., Koltun, V., Malik, J., Parikh, D., Batra, D., 2019. Habitat: A              on Computer Vision and Pattern Recognition (CVPR) , 1746–1754.
   Platform for Embodied AI Research, in: IEEE International Conference on               Spinello, L., Arras, K.O., 2011. People Detection In RGB-D Data, in:
   Computer Vision (ICCV), pp. 9338–9346.                                                   IEEE/RSJ International Conference on Intelligent Robots and Systems, pp.
Saxena, A., Sun, M., Ng, A.Y., 2009. Make3D: Learning 3D Scene Structure                    3838–3843.
   From A Single Still Image. IEEE Transactions on Pattern Analysis and                  Sridhar, S., Oulasvirta, A., Theobalt, C., 2013. Interactive Markerless Articu-
   Machine Intelligence , 824–840.                                                          lated Hand Motion Tracking Using RGB and Depth Data, in: IEEE Interna-
Scharstein, D., Hirschmüller, H., Kitajima, Y., Krathwohl, G., Nešić, N., Wang,          tional Conference on Computer Vision (ICCV), pp. 2456–2463.
   X., Westling, P., 2014. High-Resolution Stereo Datasets With Subpixel-                Srinivasan, P.P., Wang, T., Sreelal, A., Ramamoorthi, R., Ng, R., 2017. Learn-
   Accurate Ground Truth, in: German conference on pattern recognition, pp.                 ing To Synthesize A 4D RGBD Light Field From A Single Image, in: IEEE
   31–42.                                                                                   International Conference on Computer Vision (ICCV), pp. 2243–2251.
Scharstein, D., Pal, C., 2007. Learning Conditional Random Fields for Stereo,            Stein, S., McKenna, S.J., 2013. Combining Embedded Accelerometers With
   in: IEEE Conference on Computer Vision and Pattern Recognition (CVPR),                   Computer Vision for Recognizing Food Preparation Activities, in: ACM
   pp. 1–8.                                                                                 International Joint Conference on Pervasive and Ubiquitous Computing, pp.
Scharstein, D., Szeliski, R., 2002. A Taxonomy and Evaluation Of Dense Two-                 729–738.
   Frame Stereo Correspondence Algorithms. International Journal of Com-                 Stoyanov, D., Scarzanella, M.V., Pratt, P., Yang, G.Z., 2010. Real-Time
   puter Vision , 7–42.                                                                     Stereo Reconstruction In Robotically Assisted Minimally Invasive Surgery,
Scharstein, D., Szeliski, R., 2003. High-Accuracy Stereo Depth Maps Us-                     in: International Conference on Medical Image Computing and Computer-
   ing Structured Light, in: IEEE Conference on Computer Vision and Pattern                 Assisted Intervention, pp. 275–282.
   Recognition (CVPR), pp. I–I.                                                          Straub, J., Whelan, T., Ma, L., Chen, Y., Wijmans, E., Green, S., Engel,
Scharwächter, T., Enzweiler, M., Franke, U., Roth, S., 2014. Stixmantics:                  J.J., Mur-Artal, R., Ren, C., Verma, S., Clarkson, A., Yan, M., Budge,
                                                                                                                                                                 21

   B., Yan, Y., Pan, X., Yon, J., Zou, Y., Leon, K., Carter, N., Briales, J.,          2019. DIODE: A DEnse INdoor and OUtdoor DePth DAtaset. arXiv
   Gillingham, T., Mueggler, E., Pesqueira, L., Savva, M., Batra, D., Stras-           preprint arXiv:1908.00463 , 1–8.
   dat, H.M., Nardi, R.D., Goesele, M., Lovegrove, S., Newcombe, R., 2019.          Vaufreydaz, D., Nègre, A., 2014. MobileRGBD, An Open Benchmark Corpus
   The REplica Dataset: A Digital Replica Of Indoor Spaces. arXiv preprint             for Mobile RGB-D Related Algorithms, in: 13th International Conference
   arXiv:1906.05797 , 1–10.                                                            on Control Automation Robotics & Vision (ICARCV), pp. 1668–1673.
Sturm, J., Engelhard, N., Endres, F., Burgard, W., Cremers, D., 2012. A Bench-      Wan, J., Zhao, Y., Zhou, S., Guyon, I., Escalera, S., Li, S.Z., 2016. ChaLearn
   mark for The Evaluation Of RGB-D Slam Systems, in: IEEE/RSJ Interna-                Looking at People RGB-D Isolated and Continuous Datasets for Gesture
   tional Conference on Intelligent Robots and Systems, pp. 573–580.                   Recognition, in: IEEE Conference on Computer Vision and Pattern Recog-
Su, C.C., Cormack, L.K., Bovik, A.C., 2013. Color and Depth Priors In Natural          nition Workshops (CVPRW), pp. 56–64.
   Images. IEEE Transactions on Image Processing , 2259–2274.                       Wang, C., Lucey, S., Perazzi, F., Wang, O., 2019a. Web Stereo Video Supervi-
Su, H., Qi, C.R., Li, Y., Guibas, L.J., 2015. Render for CNN: Viewpoint Es-            sion for Depth Prediction From Dynamic Scenes, in: International Confer-
   timation in Images Using CNNs Trained with Rendered 3D Model Views,                 ence on 3D Vision (3DV), pp. 348–357.
   in: IEEE International Conference on Computer Vision (ICCV), pp. 2686–           Wang, F.E., Hu, H.N., Cheng, H.T., Lin, J.T., Yang, S.T., Shih, M.L., Chu,
   2694.                                                                               H.K., Sun, M., 2018. Self-supervised learning of depth and camera motion
Sun, P., Kretzschmar, H., Dotiwalla, X., Chouard, A., Patnaik, V., Tsui, P.,           from 360 °videos, in: The Asian Conference on Computer Vision (ACCV),
   Guo, J., Zhou, Y., Chai, Y., Caine, B., 2020. Scalability In Perception for         pp. 53–68.
   Autonomous Driving: Waymo Open Dataset, in: IEEE Conference on Com-              Wang, J., Liu, Z., Chorowski, J., Chen, Z., Wu, Y., 2012a. Robust 3D Action
   puter Vision and Pattern Recognition (CVPR), pp. 2446–2454.                         Recognition With Random Occupancy Patterns, in: European Conference
Susanto, W., Rohrbach, M., Schiele, B., 2012. 3D Object Detection With Mul-            on Computer Vision (ECCV), pp. 872–885.
   tiple Kinects, in: European Conference on Computer Vision (ECCV), pp.            Wang, J., Liu, Z., Wu, Y., Yuan, J., 2012b. Mining Actionlet Ensemble for Ac-
   93–102.                                                                             tion Recognition With Depth Cameras, in: IEEE Conference on Computer
Szot, A., Clegg, A., Undersander, E., Wijmans, E., Zhao, Y., Turner, J.,               Vision and Pattern Recognition (CVPR), pp. 1290–1297.
   Maestre, N., Mukadam, M., Chaplot, D., Maksymets, O., Gokaslan, A.,              Wang, J., Mueller, F., Bernard, F., Sorli, S., Sotnychenko, O., Qian, N., Otaduy,
   Vondrus, V., Dharur, S., Meier, F., Galuba, W., Chang, A., Kira, Z., Koltun,        M.A., Casas, D., Theobalt, C., 2020a. RGB2Hands: Real-Time Tracking Of
   V., Malik, J., Savva, M., Batra, D., 2021. Habitat 2.0: Training Home Assis-        3D Hand Interactions From Monocular RGB Video. ACM Transactions on
   tants To Rearrange Their Habitat. arXiv preprint arXiv:2106.14405 , 1–16.           Graphics (ToG) , 1–16.
Tan, J., Lin, W., Chang, A.X., Savva, M., 2021a. Mirror3D: Depth Refinement         Wang, J., Nie, X., Xia, Y., Wu, Y., Zhu, S.C., 2014. Cross-View Action Mod-
   for Mirror Surfaces, in: IEEE Conference on Computer Vision and Pattern             eling, Learning and Recognition, in: IEEE Conference on Computer Vision
   Recognition (CVPR), pp. 15990–15999.                                                and Pattern Recognition (CVPR), pp. 2649–2656.
Tan, J., Lin, W., Chang, A.X., Savva, M., 2021b. Mirror3D: Depth Refinement         Wang, K., Shen, S., 2020. Flow-Motion and Depth Network for Monocular
   for Mirror Surfaces, in: IEEE Conference on Computer Vision and Pattern             Stereo and Beyond. IEEE Robotics and Automation Letters , 3307–3314.
   Recognition (CVPR), pp. 15985–15994.                                             Wang, P., Huang, X., Cheng, X., Zhou, D., Geng, Q., Yang, R., 2019b. The
Tang, C., Li, W., Wang, P., Wang, L., 2018. Online Human Action Recogni-               Apolloscape Open Dataset for Autonomous Driving and Its Application.
   tion Based On Incremental Learning Of Weighted Covariance Descriptors.              IEEE transactions on pattern analysis and machine intelligence , 2702–2719.
   Information Sciences , 219–237.                                                  Wang, Q., Zheng, S., Yan, Q., Deng, F., Zhao, K., Chu, X., 2019c. IRS: A
Tang, S., Tan, F., Cheng, K., Li, Z., Zhu, S., Tan, P., 2019. A Neural Net-            Large Naturalistic Indoor Robotics Stereo Dataset To Train Deep Models for
   work for Detailed Human Depth Estimation From A Single Image, in: IEEE              Disparity and Surface Normal Estimation. arXiv preprint arXiv:1912.09678
   International Conference on Computer Vision (ICCV), pp. 7749–7758.                  , 1–12.
Tang, Y., Tian, Y., Lu, J., Feng, J., Zhou, J., 2017. Action Recognition In         Wang, W., Zhu, D., Wang, X., Hu, Y., Qiu, Y., Wang, C., Hu, Y., Kapoor,
   RGB-D Egocentric Videos, in: IEEE International Conference on Image                 A., Scherer, S., 2020b. TartanAir: A Dataset To Push The Limits Of Vi-
   Processing (ICIP), pp. 3410–3414.                                                   sual Slam, in: IEEE/RSJ International Conference on Intelligent Robots and
Tarel, J.P., Hautiere, N., Caraffa, L., Cord, A., Halmaoui, H., Gruyer, D., 2012.      Systems (IROS), pp. 4909–4916.
   Vision Enhancement In Homogeneous and Heterogeneous Fog. IEEE Intel-             Wasenmüller, O., Meyer, M., Stricker, D., 2016. CoRBS: Comprehensive RGB-
   ligent Transportation Systems Magazine , 6–20.                                      D Benchmark for Slam Using Kinect V2, in: IEEE Winter Conference on
Tarel, J.P., Hautiere, N., Cord, A., Gruyer, D., Halmaoui, H., 2010. Improved          Applications of Computer Vision (WACV), pp. 1–7.
   Visibility Of Road Scene Images Under Heterogeneous Fog, in: IEEE Intel-         Wolf, C., Lombardi, E., Mille, J., Celiktutan, O., Jiu, M., Dogan, E., Eren, G.,
   ligent Vehicles Symposium, pp. 478–485.                                             Baccouche, M., Dellandréa, E., Bichot, C.E., 2014. Evaluation of Video Ac-
Thermos, S., Daras, P., Potamianos, G., 2020. A Deep Learning Approach                 tivity Localizations Integrating Quality and Quantity Measurements. Com-
   to Object Affordance Segmentationn, in: IEEE International Conference on            puter Vision and Image Understanding , 14–30.
   Acoustics, Speech and Signal Processing (ICASSP), pp. 2358–2362.                 Wu, S., Liebel, L., Körner, M., 2021. Derivation Of Geometrically and Seman-
Tombari, F., Di Stefano, L., Giardino, S., 2011. Online Learning for Auto-             tically Annotated Uav Datasets At Large Scales From 3D City Models, in:
   matic Segmentation Of 3D Data, in: IEEE/RSJ International Conference on             International Conference on Pattern Recognition (ICPR), pp. 4712–4719.
   Intelligent Robots and Systems, pp. 4857–4864.                                   Xia, F., Zamir, A.R., He, Z., Sax, A., Malik, J., Savarese, S., 2018. Gibson
Tompson, J., Stein, M., LeCun, Y., Perlin, K., 2014. Real-Time Continuous              Env: Real-World Perception for Embodied Agents, in: IEEE Conference on
   Pose Recovery Of Human Hands Using Convolutional Networks. ACM                      Computer Vision and Pattern Recognition (CVPR), pp. 9068–9079.
   Transactions on Graphics (ToG) , 1–10.                                           Xia, L., Chen, C., Aggarwal, J., 2012. View Invariant Human Action Recog-
Torralba, A., Efros, A.A., 2011. Unbiased Look at Dataset Bias, in: IEEE Con-          nition Using Histograms of 3D Joints, in: IEEE Conference on Computer
   ference on Computer Vision and Pattern Recognition (CVPR), pp. 1521–                Vision and Pattern Recognition Workshops (CVPRW), pp. 20–27.
   1528.                                                                            Xian, K., Shen, C., Cao, Z., Lu, H., Xiao, Y., Li, R., Luo, Z., 2018. Monocular
Tran, T.H., Le, T.L., Pham, D.T., Hoang, V.N., Khong, V.M., Tran, Q.T.,                Relative Depth Perception With Web Stereo Data Supervision, in: IEEE
   Nguyen, T.S., Pham, C., 2018. A Multi-modal Multi-view Dataset for Hu-              Conference on Computer Vision and Pattern Recognition (CVPR), pp. 311–
   man Fall Analysis and Preliminary Investigation on Modality, in: Interna-           320.
   tional Conference on Pattern Recognition (ICPR), pp. 1947–1952.                  Xian, K., Zhang, J., Wang, O., Mai, L., Lin, Z., Cao, Z., 2020a. Structure-
Uhrig, J., Schneider, N., Schneider, L., Franke, U., Brox, T., Geiger, A., 2017.       Guided Ranking Loss for Single Image Depth Prediction, in: IEEE Confer-
   Sparsity Invariant Cnns, in: International Conference on 3D Vision (3DV),           ence on Computer Vision and Pattern Recognition (CVPR), pp. 611–620.
   pp. 11–20.                                                                       Xian, K., Zhang, J., Wang, O., Mai, L., Lin, Z., Cao, Z., 2020b. Structure-
Ummenhofer, B., Zhou, H., Uhrig, J., Mayer, N., Ilg, E., Dosovitskiy, A., Brox,        Guided Ranking Loss for Single Image Depth Prediction, in: IEEE Confer-
   T., 2017. Demon: Depth and Motion Network for Learning Monocular                    ence on Computer Vision and Pattern Recognition (CVPR), pp. 608–617.
   Stereo, in: IEEE Conference on Computer Vision and Pattern Recognition           Xiao, J., Owens, A., Torralba, A., 2013. Sun3D: A Database Of Big Spaces
   (CVPR), pp. 5038–5047.                                                              Reconstructed Using SfM and Object Labels, in: IEEE International Con-
Vasiljevic, I., Kolkin, N., Zhang, S., Luo, R., Wang, H., Dai, F.Z., andrea            ference on Computer Vision (ICCV), pp. 1625–1632.
   F. Daniele, Mostajabi, M., Basart, S., Walter, M.R., Shakhnarovich, G.,          Xie, J., Girshick, R., Farhadi, A., 2016. Deep3D: Fully Automatic 2D-To-3D
                                                                                                                                                            22

   Video Conversion With Deep Convolutional Neural Networks, in: European              2018. The Multivehicle Stereo Event Camera Dataset: An Event Camera
   Conference on Computer Vision (ECCV), pp. 842–857.                                  Dataset for 3D Perception. IEEE Robotics and Automation Letters , 2032–
Xu, C., Cheng, L., 2013. Efficient Hand Pose Estimation From A Single Depth            2039.
   Image, in: IEEE International Conference on Computer Vision (ICCV), pp.          Zimmermann, C., Brox, T., 2017. Learning to estimate 3D hand pose from
   3456–3462.                                                                          single RGB images, in: IEEE Conference on Computer Vision and Pattern
Yang, G., Song, X., Huang, C., Deng, Z., Shi, J., Zhou, B., 2019. Driving-             Recognition (CVPR), pp. 4903–4911.
   stereo: A Large-Scale Dataset for Stereo Matching In Autonomous Driving          Zioulis, N., Karakottas, A., Zarpalas, D., Daras, P., 2018. Omnidepth: Dense
   Scenarios, in: IEEE Conference on Computer Vision and Pattern Recogni-              Depth Estimation for Indoors Spherical Panoramas, in: European Confer-
   tion (CVPR), pp. 899–908.                                                           ence on Computer Vision (ECCV), pp. 448–465.
Yao, Y., Luo, Z., Li, S., Zhang, J., Ren, Y., Zhou, L., Fang, T., Quan, L., 2020.   Zollhöfer, M., Dai, A., Innmann, M., Wu, C., Stamminger, M., Theobalt, C.,
   BlendedMVS: A Large-Scale Dataset for Generalized Multi-View Stereo                 Nießner, M., 2015. Shading-Based Refinement On Volumetric Signed Dis-
   Networks. IEEE Conference on Computer Vision and Pattern Recognition                tance Functions. ACM Transactions on Graphics (ToG) , 1–14.
   (CVPR) , 1790–1799.
Yin, F., Zhou, S., 2020. Accurate Estimation Of Body Height From A Single
   Depth Image Via A Four-Stage Developing Network, in: IEEE Conference
   on Computer Vision and Pattern Recognition (CVPR), pp. 8267–8276.
Yin, W., Wang, X., Shen, C., Liu, Y., Tian, Z., Xu, S., Sun, C., Renyin, D.,
   2020. Diversedepth: Affine-Invariant Depth Prediction Using Diverse Data.
   arXiv preprint arXiv:2002.00569 , 1–17.
Yogamani, S., Hughes, C., Horgan, J., Sistu, G., Varley, P., O’Dea, D., Uricár,
   M., Milz, S., Simon, M., Amende, K., 2019. Woodscape: A Multi-Task,
   Multi-Camera Fisheye Dataset for Autonomous Driving, in: IEEE Confer-
   ence on Computer Vision and Pattern Recognition (CVPR), pp. 9308–9318.
Yousif, K., Bab-Hadiashar, A., Hoseinnezhad, R., 2015. An Overview To Vi-
   sual Odometry and Visual Slam: Applications To Mobile Robotics. Intelli-
   gent Industrial Systems , 289–311.
Yu, G., Liu, Z., Yuan, J., 2014. Discriminative Orderlet Mining for Real-Time
   Recognition of Human-Object Interaction, in: The Asian Conference on
   Computer Vision (ACCV, pp. 50–65.
Yuan, S., Ye, Q., Stenger, B., Jain, S., Kim, T.K., 2017. BigHand2.2M Bench-
   mark: Hand Pose Dataset and State Of The Art Analysis, in: IEEE Confer-
   ence on Computer Vision and Pattern Recognition (CVPR), pp. 2605–2613.
Yuan, W., Fan, R., Wang, M.Y., Chen, Q., 2020. Mfusenet: Robust Depth Es-
   timation With Learned Multiscopic Fusion. IEEE Robotics and Automation
   Letters , 3113–3120.
Yun, K., Honorio, J., Chattopadhyay, D., Berg, T.L., Samaras, D., 2012. Two-
   Person Interaction Detection Using Body-Pose Features and Multiple In-
   stance Learning, in: IEEE Conference on Computer Vision and Pattern
   Recognition Workshops (CVPRW), pp. 28–35.
Zbontar, J., LeCun, Y., 2015. Computing The Stereo Matching Cost With A
   Convolutional Neural Network, in: IEEE Conference on Computer Vision
   and Pattern Recognition (CVPR), pp. 1592–1599.
Zeisl, B., Koser, K., Pollefeys, M., 2013. Automatic Registration Of RGB-D
   Scans Via Salient Directions, in: IEEE International Conference on Com-
   puter Vision (ICCV), pp. 2808–2815.
Zhang, J., Jiao, J., Chen, M., Qu, L., Xu, X., Yang, Q., 2017. A Hand Pose
   Tracking Benchmark From Stereo Matching, in: IEEE International Con-
   ference on Image Processing (ICIP), pp. 982–986.
Zhang, J., Li, W., Wang, P., Ogunbona, P., Liu, S., Tang, C., 2016a. A Large
   Scale RGB-D Dataset for Action Recognition, in: International Workshop
   on Understanding Human Activities through 3D Sensors, pp. 101–114.
Zhang, Y., Cao, C., Cheng, J., Lu, H., 2018. EgoGesture: A New Dataset and
   Benchmark for Egocentric Hand Gesture Recognition. IEEE Transactions
   on Multimedia , 1038–1050.
Zhang, Z., Rebecq, H., Forster, C., Scaramuzza, D., 2016b. Benefit Of Large
   Field-Of-View Cameras for Visual Odometry, in: IEEE International Con-
   ference on Robotics and Automation (ICRA), pp. 801–808.
Zhao, S., Fu, H., Gong, M., Tao, D., 2019. Geometry-aware Symmetric Do-
   main Adaptation for Monocular Depth Estimation, in: IEEE Conference on
   Computer Vision and Pattern Recognition (CVPR), pp. 9788–9798.
Zheng, J., Zhang, J., Li, J., Tang, R., Gao, S., Zhou, Z., 2020. Structured3D:
   A Large Photo-Realistic Dataset for Structured 3D Modeling, in: European
   Conference on Computer Vision (ECCV), pp. 519–535.
Zhou, Q.Y., Koltun, V., 2013. Dense Scene Reconstruction With Points Of
   Interest. ACM Transactions on Graphics (ToG) , 1–8.
Zhou, Q.Y., Koltun, V., 2014. Color Map Optimization for 3D Reconstruction
   With Consumer Depth Cameras. ACM Transactions on Graphics (ToG) ,
   1–10.
Zhou, Q.Y., Miller, S., Koltun, V., 2013. Elastic Fragments for Dense Scene
   Reconstruction, in: IEEE International Conference on Computer Vision
   (ICCV), pp. 473–480.
Zhu, A.Z., Thakur, D., Özaslan, T., Pfrommer, B., Kumar, V., Daniilidis, K.,
