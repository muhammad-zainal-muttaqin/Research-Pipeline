---
source_id: 143
bibtex_key: dai2017scannet
title: ScanNet: Richly-Annotated 3D Reconstructions of Indoor Scenes
year: 2017
domain_theme: Dataset
verified_pdf: 143_ScanNet.pdf
char_count: 78145
---

ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes

Angela Dai1 Angel X. Chang2 Manolis Savva2 Maciej Halber2 Thomas Funkhouser2 Matthias Nießner1,3
             1
               Stanford University 2 Princeton University 3 Technical University of Munich
                                                           www.scan-net.org

                          Abstract

    A key requirement for leveraging supervised deep learn-
 ing methods is the availability of large, labeled datasets.
 Unfortunately, in the context of RGB-D scene understand-
 ing, very little data is available – current datasets cover a
 small range of scene views and have limited semantic an-
 notations. To address this issue, we introduce ScanNet, an
 RGB-D video dataset containing 2.5M views in 1513 scenes
 annotated with 3D camera poses, surface reconstructions,
 and semantic segmentations. To collect this data, we de-
 signed an easy-to-use and scalable RGB-D capture system
 that includes automated surface reconstruction and crowd-
 sourced semantic annotation.We show that using this data
 helps achieve state-of-the-art performance on several 3D
 scene understanding tasks, including 3D object classifica-          Figure 1. Example reconstructed spaces in ScanNet annotated with
 tion, semantic voxel labeling, and CAD model retrieval.             instance-level object category labels through our crowdsourced
                                                                     annotation framework.

                                                                     ciently providing (dense) annotations in 3D is non-trivial.
 1. Introduction                                                     Thus, existing work on 3D datasets often fall back to poly-
     Since the introduction of commodity RGB-D sensors,              gon or bounding box annotations on 2.5D RGB-D images
 such as the Microsoft Kinect, the field of 3D geometry cap-         [74, 92, 77], rather than directly annotating in 3D. In the
 ture has gained significant attention and opened up a wide          latter case, labels are added manually by expert users (typi-
 range of new applications. Although there has been sig-             cally by the paper authors) [32, 71] which limits their over-
 nificant effort on 3D reconstruction algorithms, general 3D         all size and scalability.
 scene understanding with RGB-D data has only very re-                   In this paper, we introduce ScanNet, a dataset of richly-
 cently started to become popular. Research along seman-             annotated RGB-D scans of real-world environments con-
 tic understanding is also heavily facilitated by the rapid          taining 2.5M RGB-D images in 1513 scans acquired in
 progress of modern machine learning methods, such as neu-           707 distinct spaces. The sheer magnitude of this dataset
 ral models. One key to successfully applying theses ap-             is larger than any other [58, 81, 92, 75, 3, 71, 32]. However,
 proaches is the availability of large, labeled datasets. While      what makes it particularly valuable for research in scene
 much effort has been made on 2D datasets [17, 44, 47],              understanding is its annotation with estimated calibration
 where images can be downloaded from the web and directly            parameters, camera poses, 3D surface reconstructions, tex-
 annotated, the situation for 3D data is more challenging.           tured meshes, dense object-level semantic segmentations,
 Thus, many of the current RGB-D datasets [74, 92, 77, 32]           and aligned CAD models (see Fig. 2). The semantic seg-
 are orders of magnitude smaller than their 2D counterparts.         mentations are more than an order of magnitude larger than
 Typically, 3D deep learning methods use synthetic data to           any previous RGB-D dataset.
 mitigate this lack of real-world data [91, 6].                          In the collection of this dataset, we have considered two
     One of the reasons that current 3D datasets are small is        main research questions: 1) how can we design a frame-
 because their capture requires much more effort, and effi-          work that allows many people to collect and annotate large

                                                                  15828
        Dataset              Size           Labels                   Annotation Tool                  Reconstruction         CAD Models
     NYU v2 [58]           464 scans     1449 frames           2D LabelMe-style [69]                        none               some [25]
       TUM [81]             47 scans        none                          -                        aligned poses (Vicon)          no
     SUN 3D [92]           415 scans       8 scans                 2D polygons                       aligned poses [92]           no
   SUN RGB-D [75]         10k frames     10k frames        2D polygons + bounding boxes              aligned poses [92]           no
   BuildingParser [3]     265 rooms       265 rooms             CloudCompare [24]                        point cloud              no
    PiGraphs [71]           26 scans       26 scans         dense 3D, by the authors [71]              dense 3D [62]              no
    SceneNN [32]           100 scans      100 scans         dense 3D, by the authors [60]               dense 3D [9]              no
    ScanNet (ours)        1513 scans      1513 scans     dense 3D, crowd-sourced MTurk                dense 3D [12]                yes
                         2.5M frames                      labels also proj. to 2D frames
Table 1. Overview of RGB-D datasets for 3D reconstruction and semantic scene understanding. Note that in addition to the 1513 scans in
ScanNet, we also provided dense 3D reconstruction and annotations on all NYU v2 sequences.

amounts of RGB-D data, and 2) can we use the rich annota-                48, 43, 92, 80, 61, 72, 93, 36, 16, 35, 57, 40, 29, 70, 52, 45,
tions and data quantity provided in ScanNet to learn better              95, 75, 9, 33, 85, 71, 32, 3, 10, 78, 2].1 These datasets have
3D models for scene understanding?                                       been used to train models for many 3D scene understanding
    To investigate the first question, we built a capture                tasks, including semantic segmentation [67, 58, 26, 86], 3D
pipeline to help novices acquire semantically-labeled 3D                 object detection [73, 46, 27, 76, 77], 3D object classification
models of scenes. A person uses an app on an iPad                        [91, 53, 66], and others [94, 22, 23].
mounted with a depth camera to acquire RGB-D video,                          Most RGB-D datasets contain scans of individual ob-
and then we processes the data off-line and return a com-                jects. For example, the Redwood dataset [10] contains over
plete semantically-labeled 3D reconstruction of the scene.               10,000 scans of objects annotated with class labels, 1,781 of
The challenges in developing such a framework are numer-                 which are reconstructed with KinectFusion [59]. Since the
ous, including how to perform 3D surface reconstruction ro-              objects are scanned in isolation without scene context, the
bustly in a scalable pipeline and how to crowdsource seman-              dataset’s focus is mainly on evaluating surface reconstruc-
tic labeling. The paper discusses our study of these issues              tion quality rather than semantic understanding of complete
and documents our experience with scaling up RGB-D scan                  scenes.
collection (20 people) and annotation (500 crowd workers).                   One of the earliest and most popular datasets for RGB-
    To investigate the second question, we trained 3D deep               D scene understanding is NYU v2 [74]. It is composed of
networks with the data provided by ScanNet and tested their              464 short RGB-D sequences, from which 1449 frames have
performance on several scene understanding tasks, includ-                been annotated with 2D polygons denoting semantic seg-
ing 3D object classification, semantic voxel labeling, and               mentations, as in LabelMe [69]. SUN RGB-D [75] follows
CAD model retrieval. For the semantic voxel labeling task,               up on this work by collecting 10,335 RGB-D frames an-
we introduce a new volumetric CNN architecture.                          notated with polygons in 2D and bounding boxes in 3D.
    Overall, the contributions of this paper are:                        These datasets have scene diversity comparable to ours, but
   • A large 3D dataset containing 1513 RGB-D scans of                   include only a limited range of viewpoints, and do not pro-
      over 707 unique indoor environments with estimated                 vide complete 3D surface reconstructions, dense 3D seman-
      camera parameters, surface reconstructions, textured               tic segmentations, or a large set of CAD model alignments.
      meshes, semantic segmentations. We also provide                        One of the first RGB-D datasets focused on long RGB-
      CAD model placements for a subset of the scans.                    D sequences in indoor environments is SUN3D. It contains
   • A design for efficient 3D data capture and annotation               a set of 415 Kinect v1 sequences of 254 unique spaces.
      suitable for novice users.                                         Although some objects were annotated manually with 2D
   • New RGB-D benchmarks and improved results for                       polygons, and 8 scans have estimated camera poses based
      state-of-the art machine learning methods on 3D ob-                on user input, the bulk of the dataset does not include cam-
      ject classification, semantic voxel labeling, and CAD              era poses, 3D reconstructions, or semantic annotations.
      model retrieval.                                                       Recently, Armeni et al. [3, 2] introduced an indoor
   • A complete open source acquisition and annotation                   dataset containing 3D meshes for 265 rooms captured with
      framework for dense RGB-D reconstructions.                         a custom Matterport camera and manually labeled with se-
                                                                         mantic annotations. The dataset is high-quality, but the cap-
2. Previous Work
                                                                             1 A comprehensive and detailed overview of publicly-accessible RGB-
   A large number of RGB-D datasets have been captured
                                                                         D datasets is given by [20] at http://www0.cs.ucl.ac.uk/
and made publicly available for training and benchmarking                staff/M.Firman/RGBDdatasets/, which is updated on a regular
[56, 34, 50, 65, 79, 83, 74, 4, 58, 81, 15, 55, 1, 68, 30, 51, 21,       basis.

                                                                      5829
  RGB-D Scanning                3D Reconstruction        Segmentation                   Semantic Labeling   Retrieval + Alignment
                                                                              Crowd-
                       Upload                                                sourcing

Figure 2. Overview of our RGB-D reconstruction and semantic annotation framework. Left: a novice user uses a handheld RGB-D device
with our scanning interface to scan an environment. Mid: RGB-D sequences are uploaded to a processing server which produces 3D
surface mesh reconstructions and their surface segmentations. Right: Semantic annotation tasks are issued for crowdsourcing to obtain
instance-level object category annotations and 3D CAD model alignments to the reconstruction.

ture pipeline is based on expensive and less portable hard-          iPad RGB camera data is temporally synchronized with the
ware. Furthermore, only a fused point cloud is provided              depth sensor via hardware, providing synchronized depth
as output. Due to the lack of raw color and depth data, its          and color capture at 30 Hz. Depth frames are captured at a
applicability to research on reconstruction and scene under-         resolution of 640 × 480 and color at 1296 × 968 pixels. We
standing from raw RGB-D input is limited.                            enable auto-white balance and auto-exposure by default.
    The datasets most similar to ours are SceneNN [32] and
PiGraphs [71], which are composed of 100 and 26 densely              Calibration. Our use of commodity RGB-D sensors ne-
reconstructed and labeled scenes respectively. The anno-             cessitates unwarping of depth data and alignment of depth
tations are done directly in 3D [60, 71]. However, both              and color data. Prior work has focused mostly on controlled
scanning and labeling are performed only by expert users             lab conditions with more accurate equipment to inform cal-
(i.e. the authors), limiting the scalability of the system and       ibration for commodity sensors (e.g., Wang et al. [87]).
the size of the dataset. In contrast, we design our RGB-D            However, this is not practical for novice users. Thus the
acquisition framework specifically for ease-of-use by un-            user only needs to print out a checkerboard pattern, place
trained users and for scalable processing through crowd-             it on a large, flat surface, and capture an RGB-D sequence
sourcing. This allows us to acquire a significantly larger           viewing the surface from close to far away. This sequence,
dataset with more annotations (currently, 1513 sequences             as well as a set of infrared and color frame pairs viewing the
are reconstructed and labeled).                                      checkerboard, are uploaded by the user as input to the cali-
                                                                     bration. Our system then runs a calibration procedure based
                                                                     on [84, 14] to obtain intrinsic parameters for both depth and
3. Dataset Acquisition Framework                                     color sensors, and an extrinsic transformation of depth to
   In this section, we focus on the design of the framework          color. We find that this calibration procedure is easy for
used to acquire the ScanNet dataset (Fig. 2). We discuss de-         users and results in improved data and consequently en-
sign trade-offs in building the framework and relay findings         hanced reconstruction quality.
on which methods were found to work best for large-scale
                                                                     User Interface. To make the capture process simple for
RGB-D data collection and processing.
                                                                     untrained users, we designed an iOS app with a simple live
   Our main goal driving the design of our framework was
                                                                     RGB-D video capture UI (see Fig. 2 left). The user provides
to allow untrained users to capture semantically labeled sur-
                                                                     a name and scene type for the current scan and proceeds
faces of indoor scenes with commodity hardware. Thus the
                                                                     to record a sequence. During scanning, a log-scale RGB
RGB-D scanning system must be trivial to use, the data
                                                                     feature detector point metric is shown as a “featurefulness”
processing robust and automatic, the semantic annotations
                                                                     bar to provide a rough measure of tracking robustness and
crowdsourced, and the flow of data through the system han-
                                                                     reconstruction quality in different regions being scanned.
dled by a tracking server.
                                                                     This feature was critical for providing intuition to users who
3.1. RGB-D Scanning                                                  are not familiar with the constraints and limitations of 3D
                                                                     reconstruction algorithms.
Hardware. There is a spectrum of choices for RGB-D
sensor hardware. Our requirement for deployment to large             Storage. We store scans as compressed RGB-D data on
groups of inexperienced users necessitates a portable and            the device flash memory so that a stable internet connec-
low-cost RGB-D sensor setup. We use the Structure sen-               tion is not required during scanning. The user can upload
sor [63], a commodity RGB-D sensor with design similar to            scans to the processing server when convenient by press-
the Microsoft Kinect v1. We attach this sensor to a handheld         ing an “upload” button. Our sensor units used 128 GB iPad
device such as an iPhone or iPad (see Fig. 2 left) — results         Air2 devices, allowing for several hours of recorded RGB-
in this paper were collected using iPad Air2 devices. The            D video. In practice, the bottleneck was battery life rather

                                                                  5830
than storage space. Depth is recorded as 16-bit unsigned
short values and stored using standard zLib compression.
RGB data is encoded with the H.264 codec with a high bi-
trate of 15 Mbps to prevent encoding artifacts. In addition
to the RGB-D frames, we also record Inertial Measurement
Unit (IMU) data, including acceleration, and angular veloc-
ities, from the Apple SDK. Timestamps are recorded for
IMU, color, and depth images.
3.2. Surface Reconstruction
                                                                   Figure 3. Our web-based crowdsourcing interface for annotating a
    Once data has been uploaded from the iPad to our               scene with instance-level object category labels. The right panel
server, the first processing step is to estimate a densely-        lists object instances already annotated in the scene with matching
reconstructed 3D surface mesh and 6-DoF camera poses for           painted colors. This annotation is in progress at ≈ 35%, with gray
all RGB-D frames. To conform with the goal for an au-              regions indicating unannotated surfaces.
tomated and scalable framework, we choose methods that             Validation. This reconstruction process is automatically
favor robustness and processing speed such that uploaded           triggered when a scan is uploaded to the processing server
recordings can be processed at near real-time rates with lit-      and runs unsupervised. In order to establish a clean snap-
tle supervision.                                                   shot to construct the ScanNet dataset reported in this paper,
Dense Reconstruction. We use volumetric fusion [11]                we automatically discard scan sequences that are short, have
to perform the dense reconstruction, since this approach           high residual reconstruction error, or have low percentage
is widely used in the context of commodity RGB-D data.             of aligned frames. We then manually check for and discard
There is a large variety of algorithms targeting this sce-         reconstructions with noticeable misalignments.
nario [59, 88, 7, 62, 37, 89, 42, 9, 90, 38, 12]. We chose
the BundleFusion system [12] as it was designed and evalu-         3.3. Semantic Annotation
ated for similar sensor setups as ours, and provides real-time        After a reconstruction is produced by the processing
speed while being reasonably robust given handheld RGB-            server, annotation HITs (Human Intelligence Tasks) are is-
D video data.                                                      sued on the Amazon Mechanical Turk crowdsourcing mar-
    For each input scan, we first run BundleFusion [12] at         ket. The two HITs that we crowdsource are: i) instance-
a voxel resolution of 1 cm3 . BundleFusion produces accu-          level object category labeling of all surfaces in the recon-
rate pose alignments which we then use to perform volu-            struction, and ii) 3D CAD model alignment to the recon-
metric integration through VoxelHashing [62] and extract a         struction. These annotations are crowdsourced using web-
high resolution surface mesh using the Marching Cubes al-          based interfaces to again maintain the overall scalability of
gorithm on the implicit TSDF (4 mm3 voxels). The mesh              the framework.
is then automatically cleaned up with a set of filtering steps
to merge close vertices, delete duplicate and isolated mesh        Instance-level Semantic Labeling. Our first annotation
parts, and finally to downsample the mesh to high, medium,         step is to obtain a set of object instance-level labels directly
and low resolution versions (each level reducing the number        on each reconstructed 3D surface mesh. This is in contrast
of faces by a factor of two).                                      to much prior work that uses 2D polygon annotations on
                                                                   RGB or RGB-D images, or 3D bounding box annotations.
Orientation. After the surface mesh is extracted, we au-
                                                                       We developed a WebGL interface that takes as input the
tomatically align it and all camera poses to a common co-
                                                                   low-resolution surface mesh of a given reconstruction and a
ordinate frame with the z-axis as the up vector, and the xy
                                                                   conservative over-segmentation of the mesh using a normal-
plane aligned with the floor plane. To perform this align-
                                                                   based graph cut method [19, 39]. The crowd worker then
ment, we first extract all planar regions of sufficient size,
                                                                   selects segments to annotate with instance-level object cate-
merge regions defined by the same plane, and sort them by
                                                                   gory labels (see Fig. 3). Each worker is required to annotate
normal (we use a normal threshold of 25◦ and a planar off-
                                                                   at least 25% of the surfaces in a reconstruction, and encour-
set threshold of 5 cm). We then determine a prior for the up
                                                                   aged to annotate more than 50% before submission. Each
vector by projecting the IMU gravity vectors of all frames
                                                                   scan is annotated by multiple workers (scans in ScanNet are
into the coordinates of the first frame. This allows us to se-
                                                                   annotated by 2.3 workers on average).
lect the floor plane based on the scan bounding box and the
                                                                       A key challenge in designing this interface is to enable
normal most similar to the IMU up vector direction. Finally,
                                                                   efficient annotation by workers who have no prior experi-
we use a PCA on the mesh vertices to determine the rotation
                                                                   ence with the task, or 3D interfaces in general. Our interface
around the z-axis and translate the scan such that its bounds
                                                                   uses a simple painting metaphor where clicking and drag-
are within the positive octant of the coordinate system.

                                                                 5831
                                                                        Statistic                      SceneNN [32]          ScanNet
                                                                        # of scans                                 100           1513
                                                                        # of RGB-D frames                   2,475,905       2,492,518
                                                                        floor area (avg / sum m2 )        22.6 / 2,124   22.6 / 34,453
                                                                        surface area (avg / sum m2 )      75.3 / 7,078   51.6 / 78,595
                                                                        labeled objects (avg / sum)        15.8 / 1482   24.1 / 36,213
                                                                       Table 2. Summary statistics for ScanNet compared to the most
                                                                       similar existing dataset (SceneNN [32]). ScanNet has an order
                                                                       of magnitude more scans, with 3D surface mesh reconstructions
                                                                       covering more than ten times the floor and surface area, and with
                                                                       more than 36,000 annotated object instances.
Figure 4. Crowdsourcing interface for aligning CAD models to
objects in a reconstruction. Objects can be clicked to initiate an     where clicking on a previously labeled object in a recon-
assisted search for CAD models (see list of bookshelves in mid-        struction immediately searched for CAD models with the
dle). A suggested model is placed at the position of the clicked       same category label in the ShapeNetCore [6] dataset, and
object, and the user then refines the position and orientation. A      placed one example model such that it overlaps with the ori-
desk, chair, and nightstand have been already placed here.             ented bounding box of the clicked object (see Fig. 4). The
                                                                       worker then used keyboard and mouse-based controls to ad-
ging over surfaces paints segments with a given label and
                                                                       just the alignment of the model, and was allowed to submit
corresponding color. This functions similarly to 2D paint-
                                                                       the task once at least three CAD models were placed.
ing and allows for erasing and modifying existing regions.
                                                                           Using this interface, we collected sets of CAD mod-
   Another design requirement is to allow for freeform text
                                                                       els aligned to each ScanNet reconstruction. Preliminary
labels, to reduce the inherent bias and scalability issues of
                                                                       results indicate that despite the challenging nature of this
pre-selected label lists. At the same time, it is desirable
                                                                       task, workers select semantically appropriate CAD models
to guide users for consistency and coverage of basic object
                                                                       to match objects in the reconstructions. The main limitation
types. To achieve this, the interface provides autocomplete
                                                                       of this interface is due to the mismatch between the cor-
functionality over all labels previously provided by other
                                                                       pus of available CAD models and the objects observed in
workers that pass a frequency threshold (> 5 annotations).
                                                                       the ScanNet scans. Despite the diversity of the ShapeNet
Workers are always allowed to add arbitrary text labels to
                                                                       CAD model dataset (55K objects), it is still hard to find ex-
ensure coverage and allow expansion of the label set.
                                                                       act instance-level matches for chairs, desks and more rare
   Several additional design details are important to ensure           object categories. A promising way to alleviate this limi-
usability by novice workers. First, a simple distance check            tation is to algorithmically suggest candidate retrieved and
for connectedness is used to disallow labeling of discon-              aligned CAD models such that workers can perform an eas-
nected surfaces with the same label. Earlier experiments               ier verification and adjustment task.
without this constraint resulted in two undesirable behav-
iors: cheating by painting many surfaces with a few labels,            4. ScanNet Dataset
and labeling of multiple object instances with the same la-
bel. Second, the 3D nature of the data is challenging for                 In this section, we summarize the data we collected us-
novice users. Therefore, we first show a full turntable rota-          ing our framework to establish the ScanNet dataset. This
tion of each reconstruction and instruct workers to change             dataset is a snapshot of available data from roughly one
the view using a rotating turntable metaphor. Without the              month of data acquisition by 20 users at locations in several
turntable rotation animation, many workers only annotated              countries. It has annotations by more than 500 crowd work-
from the initial view and never used camera controls despite           ers on the Mechanical Turk platform. Since the presented
the provided instructions.                                             framework runs in an unsupervised fashion and people are
                                                                       continuously collecting data, this dataset continues to grow
CAD Model Retrieval and Alignment. In the second an-                   organically. Here, we report some statistics for an initial
notation task, a crowd worker was given a reconstruction               snapshot of 1513 scans, which are summarized in Table 2.
already annotated with object instances and asked to place                Fig. 5 plots the distribution of scanned scenes over differ-
appropriate 3D CAD models to represent major objects in                ent types of real-world spaces. ScanNet contains a variety
the scene. The challenge of this task lies in the selection            of spaces such as offices, apartments, and bathrooms. The
of closely matching 3D models from a large database, and               dataset contains a diverse set of spaces ranging from small
in precisely aligning each model to the 3D position of the             (e.g., bathrooms, closets, utility rooms) to large (e.g., apart-
corresponding object in the reconstruction.                            ments, classrooms, and libraries). Each scan has been anno-
   We implemented an assisted object retrieval interface               tated with instance-level semantic category labels through

                                                                     5832
                                                                                                              Scans        Instances
                                                                                                           #Train #Test   #Train #Test
                                                                                             ScanNet       1205 312       9305 2606
                                                                            Object
                                                                                               NYU         452     80     3260 613
                                                                            Classification
                                                                                             SceneNN        70     12     377     66
                                                                           Semantic Voxel
                                                                                              ScanNet      1201    312    80554 21300
                                                                             Labeling
                                                                      Table 3. Train/Test split for object classification and dense voxel
                                                                      prediction tasks. Note that the number of instances does not in-
                                                                      clude the rotation augmentation.

                                                                      ing, research has developed approaches to classify ob-
Figure 5. Distribution of the scans in ScanNet organized by type.     jects using only geometric data with volumetric deep nets
                                                                      [91, 82, 52, 13, 66]. All of these methods train on purely
our crowdsourcing task. In total, we deployed 3,391 anno-
                                                                      synthetic data and focus on isolated objects. Although they
tation tasks to annotate all 1513 scans.
                                                                      show limited evaluation on real-world data, a larger evalu-
    The text labels used by crowd workers to annotate object          ation on realistic scanning data is largely missing. When
instances are all mapped to the object category sets of NYU           training data is synthetic and test is performed on real data,
v2 [58], ModelNet [91], ShapeNet [6], and WordNet [18]                there is also a significant discrepancy of test performance,
synsets. This mapping is made more robust by a preprocess             as data characteristics, such as noise and occlusions pat-
that collapses the initial text labels through synonym and            terns, are inherently different.
misspelling detection.
                                                                          With ScanNet, we close this gap as we have captured a
    In addition to reconstructing and annotating the 1513
                                                                      sufficiently large amount of 3D data to use real-world RGB-
ScanNet scans, we have processed all the NYU v2 RGB-D
                                                                      D input for both training and test sets. For this task, we use
sequences with our framework. The result is a set of dense
                                                                      the bounding boxes of annotated objects in ScanNet, and
reconstructions of the NYU v2 spaces with instance-level
                                                                      isolate the contained geometry. As a result, we obtain local
object annotations in 3D that are complementary in nature
                                                                      volumes around each object instance for which we know the
to the existing image-based annotations.
                                                                      annotated category. The goal of the task is to classify the
    We also deployed the CAD model alignment crowd-                   object represented by a set of scanned points within a given
sourcing task to collect a total of 107 virtual scene inter-          bounding box. For this benchmark, we use 17 categories,
pretations consisting of aligned ShapeNet models placed on            with 9, 677 train instances and 2, 606 test instances.
a subset of 52 ScanNet scans by 106 workers. There were a
total of 681 CAD model instances (of 296 unique models)
retrieved and placed on the reconstructions, with an average          Network and training. For object classification, we fol-
of 6.4 CAD model instances per annotated scan.                        low the network architecture of the 3D Network-in-Network
    For more detailed statistics on this first ScanNet dataset        of [66], without the multi-orientation pooling step. In order
snapshot, please see the supplemental material.                       to classify partial data, we add a second channel to the 303
                                                                      occupancy grid input, indicating known and unknown re-
5. Tasks and Benchmarks                                               gions (with 1 and 0, respectively) according to the camera
                                                                      scanning trajectory. As in Qi et al. [66], we use an SGD
   In this section, we describe the three tasks we developed          solver with learning rate 0.01 and momentum 0.9, decaying
as benchmarks for demonstrating the value of ScanNet data.            the learning rate by half every 20 epochs, and training the
                                                                      model for 200 epochs. We augment training samples with
Train/Test split statistics. Table 3 shows the test and               12 instances of different rotations (including both elevation
training splits of ScanNet in the context of the object classi-       and tilt), resulting in a total training set of 111, 660 samples.
fication and dense voxel prediction benchmarks. Note that
our data is significantly larger than any existing compara-           Benchmark performance. As a baseline evaluation, we
ble dataset. We use these tasks to demonstrate that Scan-             run the 3D CNN approach of Qi et al. [66]. Table 4 shows
Net enables the use of deep learning methods for 3D scene             the performance of 3D shape classification with different
understanding tasks with supervised training, and compare             train and test sets. The first two columns show results on
performance to that using data from other existing datasets.          synthetic test data from ShapeNet [6] including both com-
                                                                      plete and partial data. Naturally, training with the corre-
5.1. 3D Object Classification
                                                                      sponding synthetic counterparts of ShapeNet provides the
   With the availability of large-scale synthetic 3D datasets         best performance, as data characteristics are shared. How-
such as [91, 6] and recent advances in 3D deep learn-                 ever, the more interesting case is real-world test data (right-

                                                                    5833
most two columns); here, we show results on test sets of               training samples), from 1201 training scenes. In addition,
SceneNN [32] and ScanNet. First, we see that training on               we extract 18, 750 sample volumes for testing, which are
synthetic data allows only for limited knowledge transfer              also augmented by 8 rotations each (i.e., 150, 000 test sam-
(first two rows). Second, although the relatively small Sce-           ples) from 312 test scenes. We have 20 object class labels
neNN dataset is able to learn within its own dataset to a              plus 1 class for free space.
reasonable degree, it does not generalize to the larger vari-
ety of environments found in ScanNet. On the other hand,
training on ScanNet translates well to testing on SceneNN;             Network and training. For the semantic voxel labeling
as a result, the test results on SceneNN are significantly             task, we propose a network which predicts class labels for
improved by using the training data from ScanNet. In-                  a column of voxels in a scene according to the occupancy
terestingly enough, these results can be slightly improved             characteristics of the voxels’ neighborhood. In order to in-
when mixing training data of ScanNet with partial scans of             fer labels for an entire scene, we use the network to predict
ShapeNet (last row).                                                   a label for every voxel column at test time (i.e., every xy
                                                                       position that has voxels on the surface). The network takes
                            Synthetic Test Sets    Real Test Sets
                                                                       as input a 2 × 31 × 31 × 62 volume and uses a series of fully
                                                                       convolutional layers to simultaneously predict class scores
Training Set             ShapeNet ShapeNet Partial SceneNN ScanNet
                                                                       for the center column of 62 voxels. We use ReLU and batch
ShapeNet                   92.5         37.6       68.2      39.5      normalization for all layers (except the last) in the network.
ShapeNet Partial           88.5         92.1       72.7      45.7
SceneNN                    19.9         27.7       69.8      48.2
                                                                       To account for the unbalanced training data over the class
NYU                        26.2         26.6       72.7      53.2      labels, we weight the cross entropy loss with the inverse log
ScanNet                    21.4         31.0       78.8      74.9      of the histogram of the train data.
ScanNet +ShapeNet Par.     79.7         89.8       81.2      76.6
                                                                           We use an SGD solver with learning rate 0.01 and mo-
Table 4. 3D object classification benchmark performance. Per-          mentum 0.9, decaying the learning rate by half every 20
centages give the classification accuracy over all models in each      epochs, and train the model for 100 epochs.
test set (average instance accuracy).

                                                                       Quantitative Results. The goal of this task is to predict
5.2. Semantic Voxel Labeling
                                                                       semantic labels for all visible surface voxels in a given 3D
    A common task on RGB data is semantic segmentation                 scene; i.e., every voxel on a visible surface receives one
(i.e. labeling pixels with semantic classes) [49]. With our            of the 20 object class labels. We use NYU2 labels, and
data, we can extend this task to 3D, where the goal is to              list voxel classification results on ScanNet in Table 7. We
predict the semantic object label on a per-voxel basis. This           achieve an voxel classification accuracy of 73.0% over the
task of predicting a semantic class for each visible 3D voxel          set of 312 test scenes, which is based purely on the geomet-
has been addressed by some prior work, but using hand-                 ric input (no color is used).
crafted features to predict a small number of classes [41,                 In Table 5, we show our semantic voxel labeling results
86], or focusing on outdoor environments [8, 5].                       on the NYU2 dataset [58]. We are able to outperform previ-
                                                                       ous methods which are trained on limited sets of real-world
Data Generation. We first voxelize a scene and obtain                  data using our volumetric classification network. For in-
a dense voxel grid with 2cm3 voxels, where every voxel                 stance, Hermans et al. [31] classify RGB-D frames using
stores its TSDF value and object class annotation (empty               a dense random decision forest in combination with a con-
space and unlabeled surface points have their own respec-              ditional random field. Additionally, SemanticFusion [54]
tive classes). We now extract subvolumes of the scene vol-             uses a deep net trained on RGB-D frames, and regularize
ume, of dimension 2 × 31 × 31 × 62 and spatial extent                  the predictions with a CRF over a 3D reconstruction of the
1.5m × 1.5m × 3m; i.e., a voxel size of ≈ 4.8cm3 ; the                 frames; note that we compare to their classification results
two channels represent the occupancy and known/unknown                 before the CRF regularization. SceneNet trains on a large
space according to the camera trajectory. These sample vol-            synthetic dataset and fine-tunes on NYU2. Note that in con-
umes are aligned with the xy-ground plane.For ground truth             trast to Hermans et al. and SemanticFusion, neither we nor
data generation, voxel labels are propagated from the scene            SceneNet use RGB information.
voxelization to these sample volumes. The samples are cho-                 Note that we do not explicitly enforce prediction con-
sen that ≥ 2% of the voxels are occupied (i.e., on the sur-            sistency between neighboring voxel columns when the test
face), and ≥ 70% of these surface voxels have valid an-                volume is slid across the xy plane. This could be achieved
notations; samples not meeting these criteria are discarded.           with a volumetric CRF [64], as used in [86]; however, our
Across ScanNet, we generate 93, 721 subvolume examples                 goal in this task to focus exclusively on the per-voxel clas-
for training, augmented by 8 rotations each (i.e., 749, 768            sification accuracy.

                                                                     5834
                                 floor     wall      chair   table   window   bed    sofa    tv     objs.   furn.   ceil.   avg.
       Hermans et al. [31]       91.5      71.8      41.9    27.7     46.1    68.4   28.5   38.4     8.6    37.1    83.4    49.4
      SemanticFusion [54]∗       92.6      86.0      58.4    34.0     60.5    61.7   47.3   33.9    59.1    63.7    43.4    58.2
          SceneNet [28]          96.2      85.3      61.0    43.8     30.0    72.5   62.8   19.4    50.0    60.4    74.1    59.6
      Ours (ScanNet + NYU)       99.0      55.8      67.6    50.9     63.1    81.4   67.2   35.8    34.6    65.6    46.2    60.7
Table 5. Dense pixel classification accuracy on NYU2 [58]. Note that both SemanticFusion [54] and Hermans et. al. [31] use both geometry
and color, and that Hermans et al. uses a CRF, unlike our approach which is geometry-only and has only unary predictions. The reported
SemanticFusion classification is on the 13 class task (13 class average accuracy of 58.9%).

                                Retrieval from ShapeNet                  Thus, we can learn an embedding between real and syn-
          Train                 Top 1 NN      Top 3 NNs                  thetic data in order to perform model retrieval for RGB-D
                                                                         scans. To this end, we use the volumetric shape classifi-
          ShapeNet               10.4%             8.0%
          ScanNet                12.7%            11.7%                  cation network by Qi et al. [66], we use the same training
          ShapeNet + ScanNet     77.5%            77.0%                  procedure as in Sec. 5.1. Nearest neighbors are retrieved
Table 6. 3D model retrieval benchmark performance. Nearest               based on the ℓ2 distance between the extracted feature de-
neighbor models are retrieved for ScanNet objects from ShapeNet-         scriptors, and measured against the ground truth provided
Core. Percentages indicate average instance accuracy of retrieved        by the CAD model retrieval task. In Table 6, we show ob-
model to query region.                                                   ject retrieval results using objects from ScanNet to query
              Class        % of Test Scenes       Accuracy
                                                                         for nearest neighbor models from ShapeNetCore. Note that
              Floor             35.7%              90.3%                 training on ShapeNet and ScanNet independently results in
              Wall              38.8%              70.1%                 poor retrieval performance, as neither are able to bridge the
              Chair              3.8%              69.3%                 gap between the differing characteristics of synthetic and
              Sofa               2.5%              75.7%
              Table              3.3%              68.4%
                                                                         real-world data. Training on both ShapeNet and ScanNet
              Door               2.2%              48.9%                 together is able to find an embedding of shape similarities
             Cabinet             2.4%              49.8%                 between both data modalities, resulting in much higher re-
               Bed               2.0%              62.4%                 trieval accuracy.
              Desk               1.7%              36.8%
              Toilet             0.2%              69.9%
              Sink               0.2%              39.4%                 6. Conclusion
             Window              0.4%              20.1%
             Picture             0.2%               3.4%                     This paper introduces ScanNet: a large-scale RGB-
            Bookshelf            1.6%              64.6%                 D dataset of 1513 scans with surface reconstructions,
             Curtain             0.7%               7.0%
                                                                         instance-level object category annotations, and 3D CAD
          Shower Curtain        0.04%              46.8%
             Counter             0.6%              32.1%                 model placements. To make the collection of this data pos-
           Refrigerator          0.3%              66.4%                 sible, we designed a scalable RGB-D acquisition and se-
             Bathtub             0.2%              74.3%                 mantic annotation framework that we provide for the ben-
          OtherFurniture         2.9%              19.5%
                                                                         efit of the community. We demonstrated that the richly-
              Total                -               73.0%
                                                                         annotated scan data collected so far in ScanNet is useful in
Table 7. Semantic voxel label prediction accuracy on ScanNet test
                                                                         achieving state-of-the-art performance on several 3D scene
scenes.
                                                                         understanding tasks; we hope that ScanNet will inspire fu-
5.3. 3D Object Retrieval                                                 ture work on many other tasks.
    Another important task is retrieval of similar CAD mod-
                                                                         Acknowledgments
els given (potentially partial) RGB-D scans. To this end,
one wants to learn a shape embedding where a feature de-                    This project is funded by Google Tango, Intel, NSF
scriptor defines geometric similarity between shapes. The                (IIS-1251217 and VEC 1539014/1539099), and a Stanford
core idea is to train a network on a shape classification task           Graduate fellowship. We also thank Occipital for donat-
where a shape embedding can be learned as byproduct of                   ing structure sensors and Nvidia for hardware donations, as
the classification task. For instance, Wu et al. [91] and Qi et          well as support by the Max-Planck Center for Visual Com-
al. [66] use this technique to perform shape retrieval queries           puting and the Stanford CURIS program. Further, we thank
within the ShapeNet database.                                            Toan Vuong, Joseph Chang, and Helen Jiang for help on the
    With ScanNet, we have established category-level corre-              mobile scanning app and the scanning process, and Hope
spondences between real-world objects and ShapeNet mod-                  Casey-Allen and Duc Nugyen for early prototypes of the
els. This allows us to train on a classification problem where           annotation interfaces. Last but not least, we would like to
both real and synthetic data are mixed inside of each cate-              thank all the volunteers who helped with scanning and get-
gory using real and synthetic data within shared class labels.           ting us access to scanning spaces.

                                                                      5835
References                                                              [16] N. Erdogmus and S. Marcel. Spoofing in 2D face recognition
                                                                             with 3D masks and anti-spoofing with Kinect. In Biometrics:
 [1] A. Aldoma, F. Tombari, L. Di Stefano, and M. Vincze. A                  Theory, Applications and Systems (BTAS), 2013 IEEE Sixth
     global hypotheses verification method for 3D object recog-              International Conference on, pages 1–6. IEEE, 2013. 2
     nition. In European Conference on Computer Vision, pages
                                                                        [17] M. Everingham, L. Van Gool, C. K. Williams, J. Winn,
     511–524. Springer, 2012. 2
                                                                             and A. Zisserman. The PASCAL visual object classes
 [2] I. Armeni, S. Sax, A. R. Zamir, and S. Savarese. Joint 2d-3d-           (VOC) challenge. International journal of computer vision,
     semantic data for indoor scene understanding. arXiv preprint            88(2):303–338, 2010. 1
     arXiv:1702.01105, 2017. 2
                                                                        [18] C. Fellbaum. WordNet. Wiley Online Library, 1998. 6
 [3] I. Armeni, O. Sener, A. R. Zamir, H. Jiang, I. Brilakis,
                                                                        [19] P. F. Felzenszwalb and D. P. Huttenlocher. Efficient graph-
     M. Fischer, and S. Savarese. 3D semantic parsing of large-
                                                                             based image segmentation. International Journal of Com-
     scale indoor spaces. CVPR, 2016. 1, 2
                                                                             puter Vision, 59(2):167–181, 2004. 4
 [4] I. B. Barbosa, M. Cristani, A. Del Bue, L. Bazzani, and
     V. Murino. Re-identification with RGB-D sensors. In Eu-            [20] M. Firman. RGBD datasets: Past, present and future. In
     ropean Conference on Computer Vision, pages 433–442.                    CVPR Workshop on Large Scale 3D Data: Acquisition, Mod-
     Springer, 2012. 2                                                       elling and Analysis, 2016. 2
 [5] M. Blaha, C. Vogel, A. Richard, J. D. Wegner, T. Pock, and         [21] S. Fothergill, H. Mentis, P. Kohli, and S. Nowozin. Instruct-
     K. Schindler. Large-scale semantic 3d reconstruction: an                ing people for training gestural interactive systems. In Pro-
     adaptive multi-resolution model for multi-class volumetric              ceedings of the SIGCHI Conference on Human Factors in
     labeling. In Proceedings of the IEEE Conference on Com-                 Computing Systems, pages 1737–1746. ACM, 2012. 2
     puter Vision and Pattern Recognition, pages 3176–3184,             [22] D. F. Fouhey, A. Gupta, and M. Hebert. Data-driven 3D
     2016. 7                                                                 primitives for single image understanding. In Proceedings
 [6] A. X. Chang, T. Funkhouser, L. Guibas, P. Hanrahan,                     of the IEEE International Conference on Computer Vision,
     Q. Huang, Z. Li, S. Savarese, M. Savva, S. Song, H. Su,                 pages 3392–3399, 2013. 2
     et al. ShapeNet: An information-rich 3D model repository.          [23] D. F. Fouhey, A. Gupta, and M. Hebert. Unfolding an indoor
     arXiv preprint arXiv:1512.03012, 2015. 1, 5, 6                          origami world. In European Conference on Computer Vision,
 [7] J. Chen, D. Bautembach, and S. Izadi. Scalable real-time                pages 687–702. Springer, 2014. 2
     volumetric surface reconstruction. ACM Transactions on             [24] D. Girardeau-Montaut. CloudCompare3D point cloud and
     Graphics (TOG), 32(4):113, 2013. 4                                      mesh processing software. OpenSource Project, 2011. 2
 [8] I. Cherabier, C. Häne, M. R. Oswald, and M. Pollefeys.            [25] R. Guo and D. Hoiem. Support surface prediction in indoor
     Multi-label semantic 3d reconstruction using voxel blocks.              scenes. In Proceedings of the IEEE International Conference
     In 3D Vision (3DV), 2016 Fourth International Conference                on Computer Vision, pages 2144–2151, 2013. 2
     on, pages 601–610. IEEE, 2016. 7                                   [26] S. Gupta, P. Arbelaez, and J. Malik. Perceptual organiza-
 [9] S. Choi, Q.-Y. Zhou, and V. Koltun. Robust reconstruction               tion and recognition of indoor scenes from RGB-D images.
     of indoor scenes. In 2015 IEEE Conference on Computer                   In Proceedings of the IEEE Conference on Computer Vision
     Vision and Pattern Recognition (CVPR), pages 5556–5565.                 and Pattern Recognition, pages 564–571, 2013. 2
     IEEE, 2015. 2, 4                                                   [27] S. Gupta, R. Girshick, P. Arbeláez, and J. Malik. Learning
[10] S. Choi, Q.-Y. Zhou, S. Miller, and V. Koltun. A large dataset          rich features from RGB-D images for object detection and
     of object scans. arXiv:1602.02481, 2016. 2                              segmentation. In European Conference on Computer Vision,
[11] B. Curless and M. Levoy. A volumetric method for building               pages 345–360. Springer, 2014. 2
     complex models from range images. In Proceedings of the            [28] A. Handa, V. Patraucean, V. Badrinarayanan, S. Stent, and
     23rd annual conference on Computer graphics and interac-                R. Cipolla. Scenenet: Understanding real world indoor
     tive techniques, pages 303–312. ACM, 1996. 4                            scenes with synthetic data. arXiv preprint arXiv:1511.07041,
[12] A. Dai, M. Nießner, M. Zollöfer, S. Izadi, and C. Theobalt.            2015. 8
     BundleFusion: Real-time globally consistent 3D reconstruc-         [29] A. Handa, T. Whelan, J. McDonald, and A. J. Davison. A
     tion using on-the-fly surface re-integration. arXiv preprint            benchmark for RGB-D visual odometry, 3D reconstruction
     arXiv:1604.01093, 2016. 2, 4                                            and SLAM. In 2014 IEEE International Conference on
[13] A. Dai, C. R. Qi, and M. Nießner. Shape completion us-                  Robotics and Automation (ICRA), pages 1524–1531. IEEE,
     ing 3d-encoder-predictor cnns and shape synthesis. arXiv                2014. 2
     preprint arXiv:1612.00101, 2016. 6                                 [30] V. Hedau, D. Hoiem, and D. Forsyth. Recovering free space
[14] M. Di Cicco, L. Iocchi, and G. Grisetti. Non-parametric cal-            of indoor scenes from a single image. In Computer Vision
     ibration for depth sensors. Robotics and Autonomous Sys-                and Pattern Recognition (CVPR), 2012 IEEE Conference on,
     tems, 74:309–317, 2015. 3                                               pages 2807–2814. IEEE, 2012. 2
[15] F. Endres, J. Hess, N. Engelhard, J. Sturm, D. Cremers, and        [31] A. Hermans, G. Floros, and B. Leibe. Dense 3D semantic
     W. Burgard. An evaluation of the RGB-D SLAM system. In                  mapping of indoor scenes from RGB-D images. In Robotics
     Robotics and Automation (ICRA), 2012 IEEE International                 and Automation (ICRA), 2014 IEEE International Confer-
     Conference on, pages 1691–1696. IEEE, 2012. 2                           ence on, pages 2631–2638. IEEE, 2014. 7, 8

                                                                      5836
[32] B.-S. Hua, Q.-H. Pham, D. T. Nguyen, M.-K. Tran, L.-F.            [46] D. Lin, S. Fidler, and R. Urtasun. Holistic scene understand-
     Yu, and S.-K. Yeung. SceneNN: A scene meshes dataset                   ing for 3D object detection with RGBD cameras. In Pro-
     with annotations. In International Conference on 3D Vision             ceedings of the IEEE International Conference on Computer
     (3DV), volume 1, 2016. 1, 2, 3, 5, 7                                   Vision, pages 1417–1424, 2013. 2
[33] M. Innmann, M. Zollhöfer, M. Nießner, C. Theobalt, and           [47] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ra-
     M. Stamminger. VolumeDeform: Real-time volumetric                      manan, P. Dollár, and C. L. Zitnick. Microsoft COCO: Com-
     non-rigid reconstruction. arXiv preprint arXiv:1603.08161,             mon objects in context. In European Conference on Com-
     2016. 2                                                                puter Vision, pages 740–755. Springer, 2014. 1
[34] C. Ionescu, F. Li, and C. Sminchisescu. Latent structured         [48] L. Liu and L. Shao. Learning discriminative representations
     models for human pose estimation. In 2011 International                from RGB-D video data. In IJCAI, volume 1, page 3, 2013.
     Conference on Computer Vision, pages 2220–2227. IEEE,                  2
     2011. 2                                                           [49] J. Long, E. Shelhamer, and T. Darrell. Fully convolutional
[35] C. Ionescu, D. Papava, V. Olaru, and C. Sminchisescu.                  networks for semantic segmentation. In Proceedings of the
     Human3.6M: Large scale datasets and predictive methods                 IEEE Conference on Computer Vision and Pattern Recogni-
     for 3D human sensing in natural environments. IEEE                     tion, pages 3431–3440, 2015. 7
     transactions on pattern analysis and machine intelligence,        [50] M. Luber, L. Spinello, and K. O. Arras. People tracking in
     36(7):1325–1339, 2014. 2                                               RGB-D data with on-line boosted target models. In 2011
[36] A. Janoch, S. Karayev, Y. Jia, J. T. Barron, M. Fritz,                 IEEE/RSJ International Conference on Intelligent Robots
     K. Saenko, and T. Darrell. A category-level 3D object                  and Systems, pages 3844–3849. IEEE, 2011. 2
     dataset: Putting the Kinect to work. In Consumer Depth
                                                                       [51] J. Mason, B. Marthi, and R. Parr. Object disappearance for
     Cameras for Computer Vision, pages 141–165. Springer,
                                                                            object discovery. In 2012 IEEE/RSJ International Confer-
     2013. 2
                                                                            ence on Intelligent Robots and Systems, pages 2836–2843.
[37] O. Kahler, V. Adrian Prisacariu, C. Yuheng Ren, X. Sun,                IEEE, 2012. 2
     P. Torr, and D. Murray.          Very high frame rate vol-
                                                                       [52] O. Mattausch, D. Panozzo, C. Mura, O. Sorkine-Hornung,
     umetric integration of depth images on mobile devices.
                                                                            and R. Pajarola. Object detection and classification from
     IEEE Transactions on Visualization and Computer Graph-
                                                                            large-scale cluttered indoor scans. In Computer Graphics Fo-
     ics, 21(11):1241–1250, 2015. 4
                                                                            rum, volume 33, pages 11–21. Wiley Online Library, 2014.
[38] O. Kähler, V. A. Prisacariu, and D. W. Murray. Real-time
                                                                            2, 6
     large-scale dense 3D reconstruction with loop closure. In
                                                                       [53] D. Maturana and S. Scherer. VoxNet: A 3D convolutional
     European Conference on Computer Vision, pages 500–516.
                                                                            neural network for real-time object recognition. In Intelligent
     Springer, 2016. 4
                                                                            Robots and Systems (IROS), 2015 IEEE/RSJ International
[39] A. Karpathy, S. Miller, and L. Fei-Fei. Object discovery
                                                                            Conference on, pages 922–928. IEEE, 2015. 2
     in 3D scenes via shape analysis. In Robotics and Automa-
     tion (ICRA), 2013 IEEE International Conference on, pages         [54] J. McCormac, A. Handa, A. Davison, and S. Leutenegger.
     2088–2095. IEEE, 2013. 4                                               Semanticfusion: Dense 3d semantic mapping with convo-
[40] M. Kepski and B. Kwolek. Fall detection using ceiling-                 lutional neural networks. arXiv preprint arXiv:1609.05130,
     mounted 3D depth camera. In Computer Vision Theory and                 2016. 7, 8
     Applications (VISAPP), 2014 International Conference on,          [55] S. Meister, S. Izadi, P. Kohli, M. Hämmerle, C. Rother, and
     volume 2, pages 640–647. IEEE, 2014. 2                                 D. Kondermann. When can we use KinectFusion for ground
[41] B.-s. Kim, P. Kohli, and S. Savarese. 3d scene understand-             truth acquisition. In Workshop on Color-Depth Camera Fu-
     ing by voxel-crf. In Proceedings of the IEEE International             sion in Robotics, IROS, volume 2, 2012. 2
     Conference on Computer Vision, pages 1425–1432, 2013. 7           [56] A. Mian, M. Bennamoun, and R. Owens. On the repeatabil-
[42] M. Klingensmith, I. Dryanovski, S. Srinivasa, and J. Xiao.             ity and quality of keypoints for local feature-based 3D ob-
     Chisel: Real time large scale 3D reconstruction onboard a              ject retrieval from cluttered scenes. International Journal of
     mobile device using spatially hashed signed distance fields.           Computer Vision, 89(2-3):348–361, 2010. 2
     In Robotics: Science and Systems, 2015. 4                         [57] R. Min, N. Kose, and J.-L. Dugelay. KinectFaceDB: A
[43] H. S. Koppula, R. Gupta, and A. Saxena. Learning human                 Kinect database for face recognition. IEEE Transactions
     activities and object affordances from RGB-D videos. The               on Systems, Man, and Cybernetics: Systems, 44(11):1534–
     International Journal of Robotics Research, 32(8):951–970,             1548, 2014. 2
     2013. 2                                                           [58] P. K. Nathan Silberman, Derek Hoiem and R. Fergus. Indoor
[44] A. Krizhevsky, I. Sutskever, and G. E. Hinton. ImageNet                segmentation and support inference from RGBD images. In
     classification with deep convolutional neural networks. In             ECCV, 2012. 1, 2, 6, 7, 8
     Advances in neural information processing systems, pages          [59] R. A. Newcombe, S. Izadi, O. Hilliges, D. Molyneaux,
     1097–1105, 2012. 1                                                     D. Kim, A. J. Davison, P. Kohi, J. Shotton, S. Hodges, and
[45] Y. Li, A. Dai, L. Guibas, and M. Nießner. Database-assisted            A. Fitzgibbon. KinectFusion: Real-time dense surface map-
     object retrieval for real-time 3D reconstruction. In Computer          ping and tracking. In Mixed and augmented reality (ISMAR),
     Graphics Forum, volume 34, pages 435–446. Wiley Online                 2011 10th IEEE international symposium on, pages 127–
     Library, 2015. 2                                                       136. IEEE, 2011. 2, 4

                                                                     5837
[60] D. T. Nguyen, B.-S. Hua, L.-F. Yu, and S.-K. Yeung. A ro-         [75] S. Song, S. P. Lichtenberg, and J. Xiao. SUN RGB-D: A
     bust 3D-2D interactive tool for scene segmentation and an-             RGB-D scene understanding benchmark suite. In Proceed-
     notation. arXiv preprint arXiv:1610.05883, 2016. 2, 3                  ings of the IEEE Conference on Computer Vision and Pattern
[61] B. Ni, G. Wang, and P. Moulin. RGBD-HuDaAct: A color-                  Recognition, pages 567–576, 2015. 1, 2
     depth video database for human daily activity recognition. In     [76] S. Song and J. Xiao. Sliding shapes for 3D object detection in
     Consumer Depth Cameras for Computer Vision, pages 193–                 depth images. In European Conference on Computer Vision,
     208. Springer, 2013. 2                                                 pages 634–651. Springer, 2014. 2
[62] M. Nießner, M. Zollhöfer, S. Izadi, and M. Stamminger.           [77] S. Song and J. Xiao. Deep sliding shapes for amodal
     Real-time 3D reconstruction at scale using voxel hashing.              3D object detection in RGB-D images. arXiv preprint
     ACM Transactions on Graphics (TOG), 32(6):169, 2013. 2,                arXiv:1511.02300, 2015. 1, 2
     4                                                                 [78] S. Song, F. Yu, A. Zeng, A. X. Chang, M. Savva, and
[63] Occipital. Occipital: The structure sensor, 2016. 3                    T. Funkhouser. Semantic scene completion from a single
[64] K. Phillip and V. Koltun. Efficient inference in fully con-            depth image. arXiv preprint arXiv:1611.08974, 2016. 2
     nected crfs with gaussian edge potentials. Adv. Neural Inf.       [79] L. Spinello and K. O. Arras. People detection in RGB-D
     Process. Syst, 2011. 7                                                 data. In 2011 IEEE/RSJ International Conference on Intel-
[65] F. Pomerleau, S. Magnenat, F. Colas, M. Liu, and R. Sieg-              ligent Robots and Systems, pages 3838–3843. IEEE, 2011.
     wart. Tracking a depth camera: Parameter exploration for               2
     fast ICP. In 2011 IEEE/RSJ International Conference on In-        [80] S. Stein and S. J. McKenna. Combining embedded ac-
     telligent Robots and Systems, pages 3824–3829. IEEE, 2011.             celerometers with computer vision for recognizing food
     2                                                                      preparation activities. In Proceedings of the 2013 ACM inter-
[66] C. R. Qi, H. Su, M. Niessner, A. Dai, M. Yan, and L. J.                national joint conference on Pervasive and ubiquitous com-
     Guibas. Volumetric and multi-view CNNs for object classi-              puting, pages 729–738. ACM, 2013. 2
     fication on 3D data. arXiv preprint arXiv:1604.03265, 2016.       [81] J. Sturm, N. Engelhard, F. Endres, W. Burgard, and D. Cre-
     2, 6, 8                                                                mers. A benchmark for the evaluation of RGB-D SLAM
[67] X. Ren, L. Bo, and D. Fox. RGB-(D) scene labeling: Fea-                systems. In 2012 IEEE/RSJ International Conference on In-
     tures and algorithms. In Computer Vision and Pattern Recog-            telligent Robots and Systems, pages 573–580. IEEE, 2012.
     nition (CVPR), 2012 IEEE Conference on, pages 2759–2766.               1, 2
     IEEE, 2012. 2
                                                                       [82] H. Su, S. Maji, E. Kalogerakis, and E. G. Learned-Miller.
[68] A. Richtsfeld, T. Mörwald, J. Prankl, M. Zillich, and
                                                                            Multi-view convolutional neural networks for 3D shape
     M. Vincze. Segmentation of unknown objects in indoor en-
                                                                            recognition. In Proc. ICCV, 2015. 6
     vironments. In 2012 IEEE/RSJ International Conference
                                                                       [83] J. Sung, C. Ponce, B. Selman, and A. Saxena. Human activ-
     on Intelligent Robots and Systems, pages 4791–4796. IEEE,
                                                                            ity detection from RGBD images. plan, activity, and intent
     2012. 2
                                                                            recognition, 64, 2011. 2
[69] B. C. Russell, A. Torralba, K. P. Murphy, and W. T. Free-
                                                                       [84] A. Teichman, S. Miller, and S. Thrun. Unsupervised intrinsic
     man. LabelMe: a database and web-based tool for image
                                                                            calibration of depth sensors via SLAM. In Robotics: Science
     annotation. International journal of computer vision, 77(1-
                                                                            and Systems, volume 248, 2013. 3
     3):157–173, 2008. 2
[70] M. Savva, A. X. Chang, P. Hanrahan, M. Fisher, and                [85] J. Valentin, A. Dai, M. Nießner, P. Kohli, P. Torr, S. Izadi,
     M. Nießner. SceneGrok: Inferring action maps in 3D                     and C. Keskin. Learning to navigate the energy landscape.
     environments. ACM Transactions on Graphics (TOG),                      arXiv preprint arXiv:1603.05772, 2016. 2
     33(6):212, 2014. 2                                                [86] J. Valentin, V. Vineet, M.-M. Cheng, D. Kim, J. Shotton,
[71] M. Savva, A. X. Chang, P. Hanrahan, M. Fisher, and                     P. Kohli, M. Nießner, A. Criminisi, S. Izadi, and P. Torr. Se-
     M. Nießner. PiGraphs: Learning interaction snapshots from              manticPaint: Interactive 3D labeling and learning at your fin-
     observations. ACM Transactions on Graphics (TOG), 35(4),               gertips. ACM Transactions on Graphics (TOG), 34(5):154,
     2016. 1, 2, 3                                                          2015. 2, 7
[72] J. Shotton, B. Glocker, C. Zach, S. Izadi, A. Criminisi, and      [87] H. Wang, J. Wang, and W. Liang. Online reconstruction of
     A. Fitzgibbon. Scene coordinate regression forests for cam-            indoor scenes from RGB-D streams. In Proceedings of the
     era relocalization in RGB-D images. In Proceedings of the              IEEE Conference on Computer Vision and Pattern Recogni-
     IEEE Conference on Computer Vision and Pattern Recogni-                tion, pages 3271–3279, 2016. 3
     tion, pages 2930–2937, 2013. 2                                    [88] T. Whelan, M. Kaess, M. Fallon, H. Johannsson, J. Leonard,
[73] A. Shrivastava and A. Gupta. Building part-based object de-            and J. McDonald. Kintinuous: Spatially extended KinectFu-
     tectors via 3D geometry. In Proceedings of the IEEE Inter-             sion. 2012. 4
     national Conference on Computer Vision, pages 1745–1752,          [89] T. Whelan, S. Leutenegger, R. F. Salas-Moreno, B. Glocker,
     2013. 2                                                                and A. J. Davison. ElasticFusion: Dense SLAM without a
[74] N. Silberman and R. Fergus. Indoor scene segmentation us-              pose graph. Proc. Robotics: Science and Systems, Rome,
     ing a structured light sensor. In Proceedings of the Inter-            Italy, 2015. 4
     national Conference on Computer Vision - Workshop on 3D           [90] T. Whelan, R. F. Salas-Moreno, B. Glocker, A. J. Davison,
     Representation and Recognition, 2011. 1, 2                             and S. Leutenegger. ElasticFusion: Real-time dense SLAM

                                                                     5838
     and light source estimation. The International Journal of
     Robotics Research, page 0278364916669237, 2016. 4
[91] Z. Wu, S. Song, A. Khosla, F. Yu, L. Zhang, X. Tang, and
     J. Xiao. 3D ShapeNets: A deep representation for volumetric
     shapes. In Proceedings of the IEEE Conference on Computer
     Vision and Pattern Recognition, pages 1912–1920, 2015. 1,
     2, 6, 8
[92] J. Xiao, A. Owens, and A. Torralba. SUN3D: A database
     of big spaces reconstructed using sfm and object labels. In
     Computer Vision (ICCV), 2013 IEEE International Confer-
     ence on, pages 1625–1632. IEEE, 2013. 1, 2
[93] B. Zeisl, K. Koser, and M. Pollefeys. Automatic registration
     of RGB-D scans via salient directions. In Proceedings of
     the IEEE international conference on computer vision, pages
     2808–2815, 2013. 2
[94] J. Zhang, C. Kan, A. G. Schwing, and R. Urtasun. Estimating
     the 3D layout of indoor scenes and its clutter from depth sen-
     sors. In Proceedings of the IEEE International Conference
     on Computer Vision, pages 1273–1280, 2013. 2
[95] M. Zollhöfer, A. Dai, M. Innmann, C. Wu, M. Stamminger,
     C. Theobalt, and M. Nießner. Shading-based refinement on
     volumetric signed distance functions. ACM Transactions on
     Graphics (TOG), 34(4):96, 2015. 2

                                                                      5839
