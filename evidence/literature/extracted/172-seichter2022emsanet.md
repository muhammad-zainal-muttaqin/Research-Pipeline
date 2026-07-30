---
source_id: 172
bibtex_key: seichter2022emsanet
title: Efficient Multi-Task RGB-D Scene Analysis for Indoor Environments
year: 2022
domain_theme: Segmentasi RGB-D
verified_pdf: 172_EMSANet.pdf
char_count: 91805
---

© 2022 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including
                                            reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any
                                                                                                        copyrighted component of this work in other works.

                                              Efficient Multi-Task RGB-D Scene Analysis for
                                                           Indoor Environments
                                                              Daniel Seichter, Söhnke Benedikt Fischedick, Mona Köhler, and Horst-Michael Groß
                                                                       Ilmenau University of Technology, Neuroinformatics and Cognitive Robotics Lab
                                                                                                  98684 Ilmenau, Germany
                                                                            daniel.seichter@tu-ilmenau.de, ORCID: 0000-0002-3828-2926

                                             Abstract—Semantic scene understanding is essential for mo-
                                         bile agents acting in various environments. Although semantic

                                                                                                                                                                                                                                                  Panoptic Segmentation
                                         segmentation already provides a lot of information, details about                                                                 RGB Encoder                      Semantic Decoder
arXiv:2207.04526v1 [cs.CV] 10 Jul 2022

                                                                                                                                                                                           Context Module
                                         individual objects as well as the general scene are missing but
                                         required for many real-world applications. However, solving
                                         multiple tasks separately is expensive and cannot be accomplished                                                                                                   Instance Decoder
                                                                                                                                                                           Depth Encoder
                                         in real time given limited computing and battery capabilities on a                                                                                                  (with orientation)

                                         mobile platform. In this paper, we propose an efficient multi-task
                                         approach for RGB-D scene analysis (EMSANet) that simultane-                                    EMSANet                                                             Scene Head            "living room"

                                         ously performs semantic and instance segmentation (panoptic
                                                                                                                                         Driving to the closest chair in
                                         segmentation), instance orientation estimation, and scene clas-                                  the living room and taking
                                         sification. We show that all tasks can be accomplished using                                      a good interaction pose...

                                         a single neural network in real time on a mobile platform
                                         without diminishing performance – by contrast, the individual
                                         tasks are able to benefit from each other. In order to evaluate
                                         our multi-task approach, we extend the annotations of the
                                         common RGB-D indoor datasets NYUv2 and SUNRGB-D for
                                         instance segmentation and orientation estimation. To the best
                                         of our knowledge, we are the first to provide results in such                                Fig. 1. Prediction of our proposed Efficient Multi-task Scene Analysis
                                         a comprehensive multi-task setting for indoor scene analysis on                              Network (EMSANet) that simultaneously performs panoptic segmentation,
                                         NYUv2 and SUNRGB-D.                                                                          orientation estimation, and scene classification. With 24.5 FPS on an NVIDIA
                                             Index Terms—Multi-task learning, orientation estimation,                                 Jetson AGX Xavier it is well suited for mobile robotic applications. See Fig. 4
                                         panoptic segmentation, scene classification, semantic segmenta-                              for semantic label colors. Color variations indicate individual instances.
                                         tion, NYUv2, SUNRGB-D
                                                                                                                                      the aforementioned challenges in order to accomplish such
                                                                I. I NTRODUCTION                                                      a high-level task. Our approach performs scene classification,
                                            In computer vision, semantic scene understanding is often                                 semantic and instance segmentation (panoptic segmentation),
                                         equated with semantic segmentation as it enables gaining                                     as well as instance orientation estimation. However, given
                                         precise knowledge about the structure of a scene by assigning                                limited computing and battery resources on a mobile platform,
                                         a semantic label to each pixel of an image. However, this                                    solving all these tasks separately is expensive and cannot be
                                         kind of knowledge is not sufficient for the agents in our                                    accomplished in real time. Therefore, we design our approach
                                         ongoing research projects MORPHIA and CO-HUMANICS                                            to solve all aforementioned tasks using a single efficient multi-
                                         that require operating autonomously in their environments.                                   task network. Our approach extends ESANet [2], an efficient
                                         Imagine a mobile robot that is supposed to navigate to a                                     approach for semantic segmentation, by adding additional
                                         semantic entity, e.g., a specific chair within a group of chairs                             heads for tackling panoptic segmentation, instance orientation
                                         in the living room, as shown in Fig. 1. Performing such a                                    estimation, and scene classification. ESANet processes both
                                         high-level task requires a much broader understanding of the                                 RGB and depth data as input. As shown in [2], especially
                                         scene. First, even with a semantic map of the environment [1],                               for indoor environments, depth data provide complementary
                                         the robot still needs to know which part of its environment                                  geometric information that help analyzing cluttered indoor
                                         belongs to the living room. Subsequently, it needs to be able                                scenes. In this paper, we show that this also holds true for
                                         to distinguish individual instances of the same semantic class,                              panoptic segmentation, instance orientation estimation, and
                                         and, finally, for approaching the chair from the right direction,                            scene classification. Thus, our approach also relies on both
                                         its orientation is required.                                                                 RGB and depth data.
                                            In this paper, we present an approach called Efficient Multi-                                Training such a multi-task approach requires comprehensive
                                         task Scene Analysis Network (EMSANet) for tackling all                                       datasets. However, to the best of our knowledge, there is no
                                                                                                                                      real-world RGB-D indoor dataset encompassing ground-truth
                                           This work has received funding from the German Federal Ministry of
                                         Education and Research (BMBF) to the project MORPHIA (grant agreement                        annotations for all aforementioned tasks. Therefore, we enrich
                                         no. 16SV8426) and from Carl-Zeiss-Stiftung to the project CO-HUMANICS.                       the existing datasets NYUv2 [3] and SUNRGB-D [4] with

                                                                                                                                  1
additional annotations for instance segmentation and instance          enabling fast inference. Our experiments in [2] reveal that
orientation estimation. With this data at hand, we first train         processing both RGB and depth data with shallow backbones
single-task baselines and subsequently combine multiple tasks          is superior to utilizing only RGB data and a deeper backbone.
in several multi-task settings. We experimentally show that all           Therefore, our approach follows ESANet and extends its
tasks can be solved using a single neural network in real time         architecture with additional heads tackling the remaining tasks.
without diminishing performance – by contrast, the individual
tasks are able to boost each other. Our full multi-task approach       B. Panoptic Segmentation
reaches 24.5 FPS on the mobile platform NVIDIA Jetson AGX                 Panoptic segmentation [17] was introduced to unify seman-
Xavier, while achieving state-of-the-art performance. Thus, it         tic segmentation (assigning a class label to each pixel) and
is well suited for real-world applications on mobile platforms.        instance segmentation (assigning a unique id to pixels of the
In summary, our main contributions are:                                same instance) in a single task. In panoptic segmentation,
  • an efficient RGB-D multi-task approach for panoptic seg-           semantic classes for countable objects are regarded as thing
    mentation, scene classification, and instance orientation          classes and represent foreground. Background classes, such
    estimation (EMSANet) including a novel encoding for                as wall or floor – known as stuff classes – do not require
    instance orientations                                              instances. Thus, all associated pixels have the same instance id.
  • enriched annotations for NYUv2 and SUNRGB-D                        Approaches for panoptic segmentation can be categorized in
  • detailed experiments regarding performance of each task            top-down, bottom-up, and end-to-end approaches. Top-down
    in single- and multi-task settings as well as corresponding        approaches typically extend two-stage instance segmentation
    inference throughputs on an NVIDIA Jetson AGX Xavier.              approaches such as Mask R-CNN [18] with an additional
   Our code, the additional annotations for NYUv2 and                  decoder for semantic segmentation [19], [20]. Although top-
SUNRGB-D as well as the trained models are publicly avail-             down approaches typically achieve superior performance, they
able at: https://github.com/TUI-NICR/EMSANet.                          have several major drawbacks: As instance segmentation ap-
                                                                       proaches can output overlapping instance masks, further logic
                     II. R ELATED W ORK                                is required to resolve these issues in order to merge instance
   In the following, we briefly summarize related work for each        and semantic segmentation without contradictions. Moreover,
task. Moreover, we give some insights on combining tasks in            they require complex training and inference pipelines, making
multi-task settings.                                                   them less suitable for mobile applications. On the other hand,
                                                                       bottom-up approaches extend encoder-decoder-based architec-
A. Semantic Segmentation                                               tures for semantic segmentation and separate thing classes
   Architectures for semantic segmentation typically follow            into instances by grouping their pixels into clusters [21]–
an encoder-decoder design to accomplish dense pixel-wise               [23]. As bottom-up approaches neither require region pro-
predictions. Well-known approaches such as PSPNet [5] or               posals, estimating multiple masks independently, nor further
the DeepLab series [6]–[8] achieve good results but cannot be          refinement steps, their pipelines for training and inference are
executed in real time on mobile platforms due to their low             much simpler compared to top-down approaches. However,
downsampling of intermediate feature representation. Thus,             until Panoptic DeepLab [23] bottom-up approaches could not
another line of research emerged, focusing on low inference            compete with top-down approaches in terms of panoptic qual-
time while still keeping high performance. For example,                ity. Nevertheless, both top-down and bottom-up approaches
ERFNet [9] introduces a more efficient block by spatially              require additional logic for merging instance and semantic
factorizing the expensive 3×3 convolution into a 3×1 and a             segmentation. The recently proposed MaX-DeepLab [24] fol-
1×3 convolution and, thus, reduces computational effort. By            lows another approach based on a novel dual-path transformer
contrast, SwiftNet [10] simply uses a pretrained ResNet18 [11]         architecture [25] and attempts to directly predict the panoptic
as encoder with early and high downsampling, resulting in low          segmentation using an end-to-end pipeline. However, research
inference time but still good performance as well.                     for this kind of approaches currently focuses on establishing
   While the aforementioned approaches only process RGB                new architectures and not on fast and efficient inference.
data, especially for indoor applications, others [12]–[16] also           Unlike for semantic segmentation, there are only a few ap-
incorporate depth data as they provide complementary geo-              proaches targeting efficiency [26]–[30]. However, their target
metric information that help analyzing cluttered scenes. Most          hardware is different as they only report inference times on
approaches use two encoders for processing RGB and depth               high-end GPUs. Execution on mobile platforms, such as an
data (RGB-D) first separately and fuse the resulting features          NVIDIA Jetson AGX Xavier, is expected to be much slower.
later in the network. However, almost all RGB-D approaches                Our approach follows the bottom-up idea as it is straight-
use deep and complex network architectures and do not                  forward to be integrated into ESANet and expected to enable
focus on fast inference. By contrast, our recently published           faster inference on mobile platforms.
ESANet [2] combines the merits of efficient and RGB-D
semantic segmentation. It utilizes a carefully designed archi-         C. Orientation Estimation
tecture featuring a dual-branch RGB-D ResNet-based encoder               Orientation estimation is often done along with 3D bound-
with high downsampling and spatially factorized convolutions           ing box detection [31]–[33] and deeply integrated into such

                                                                   2
architectures. Adapting these detectors to also accomplish              backbone. For even faster inference and improved accuracy,
dense predictions would require fundamental changes and,                the 3×3 convolutions are spatially factorized, resulting in
thus, is not suitable for our application. Another field of             the NonBottleneck1D block (NBt1D) [9] (see Fig. 2 violet).
research strongly related to orientation estimation is person           At each resolution stage of the encoders, an attention-based
perception [34]–[38]. Besides estimating a person’s orientation         mechanism is used to fuse depth features into the RGB
inherently using its skeleton [34], there are also approaches           branch enhancing its representation with additional geometric
directly estimating the orientation from patches [35]–[38]. This        information. After the last fusion, a context module similar to
can be performed using either classification or regression.             the Pyramid Pooling Module in PSPNet [5] is attached. It in-
However, as shown in [35], classification adds further dis-             corporates context information at multiple scales using several
cretization inaccuracy and does not account well for periodic-          branches with different pooling sizes (see [2] for details). The
ity. Therefore, approaches such as [35], [36] rely on regression        decoder is comprised of three decoder modules (see Fig. 2
and estimate the angle through its sine and cosine parts, which         light red), each is refining and upsampling the intermediate
is often called Biternion encoding [35]. The same authors also          feature maps to gradually restore input resolution. This is done
proposed to use the von Mises loss function [35] instead of             by a 3×3 convolution followed by three NonBottleneck1D
L1 or MSE loss as it further improves accounting periodicity            blocks and a final learned upsampling by a factor of two. The
and avoiding discontinuities.                                           learned upsampling (see Fig. 2 dark green) is initialized to
   Our approach follows the latter idea and formulates orien-           mimic bilinear upsampling first. However, as its weights are
tation estimation as regression. However, instead of using a            not fixed, the network is able to learn to combine adjacent
patch-based approach, we propose a novel way to accomplish              features in a more useful manner during training. Additional
dense orientation estimation.                                           encoder-decoder skip connections further help to restore spa-
                                                                        tial details that were lost during downsampling in the encoders.
D. Scene Classification                                                 Following the last decoder module, a 3×3 convolution maps
   Scene classification, i.e., assigning a scene label such as          the features to semantic classes. Finally, two additional learned
kitchen or living room to an input image, is similar to                 upsamplings restore the input resolution. The entire network is
other classification tasks such as the ImageNet-Challenge [39].         trained end-to-end with additional side outputs and multi-scale
Thus, well known architectures [11], [40]–[42] can be used.             supervision as depicted in Fig. 2.
                                                                           ESANet builds a strong and efficient baseline for seman-
E. Multi-task Learning                                                  tic segmentation. However, the architecture is specifically
   Multi-task learning refers to learning multiple tasks simulta-       tailored for semantic segmentation. In order to improve its
neously in a single neural network. As these tasks commonly             generalization capability for the remaining tasks, we further
share at least some network parameters, inference is faster             add a slight dropout with rate of 0.1 to all NonBottle-
compared to using an independent network for each task.                 neck1D blocks. Furthermore, we change the initialization in
Moreover, in [43] it is shown, that dense prediction tasks              all RGB-D fusion modules to He-initialization [47] and force
may benefit from another when trained together. Especially              zero-initialization [48] in all NonBottleneck1D blocks. Finally,
early network layers are known to learn common features                 to incorporate the loss of other tasks more effectively, we do
and, thus, can be shared among multiple tasks – in literature           not reduce the accumulated loss by the sum of the applied
this is referred to as hard-parameter sharing [44]. Some                semantic class weights but only by the number of all pixels
approaches [45], [46] also exchange information in the task-            across all outputs of the network.
specific heads, which is called soft-parameter sharing. How-               Next, we present the extension to a multi-task network.
ever, when utilizing soft-parameter-shared task heads, these
tasks cannot be decoupled anymore. This means that the whole            A. Panoptic Segmentation
network needs to be applied during inference, even though                  For panoptic segmentation, a second decoder for instance
only a single task may be of interest. Therefore, our approach          segmentation is required. As shown in Fig. 2 (middle), our
uses a hard-parameter shared RGB-D encoder and independent              instance decoder follows the same architecture as the semantic
task-specific heads, not sharing any network parameters or in-          decoder except the task-specific heads. The instance encoding
formation. We show that semantic and instance segmentation,             follows the implementation of Panoptic DeepLab [23]: In-
instance orientation estimation as well as scene classification         stances are represented by their center of mass encoded as
benefit from such a multi-task setting.                                 small 2D Gaussian within a heatmap, similar to keypoint
                                                                        estimation in other domains [34]. With an additional head,
  III. E FFICIENT M ULTI - TASK RGB-D S CENE A NALYSIS                  the instance decoder also predicts offset vectors for each pixel
   Our Efficient Multi-task Scene Analysis Network (EM-                 pointing towards a corresponding instance center in x and y
SANet) extends the encoder-decoder-based ESANet [2]                     direction. As instances are only required for pixels belonging
for efficient RGB-D semantic segmentation. As shown in                  to thing classes – i.e., all classes except wall, floor, and
Fig. 2 (top), ESANet features two identical encoders, one               ceiling – a corresponding foreground mask is derived from the
for processing RGB images and one for depth images. For                 semantic segmentation. All thing pixels are then grouped into
efficiency reasons, both encoders are based on a ResNet34 [11]          class-agnostic instances by combining both instance centers

                                                                    3
                                                                                                                                                                  Legend:
                                                                                                                                                                           Convolution with kernel size
                                                                                                                                                                  BN: Batch Normalization, Up.: Upsampling, DW: Depthwise
                                                                                                                                                                    : attention-based fusion of depth features into RGB branch
                                           RGB Encoder                                                                                                            FC: Fully Connected Layer

                                                                                                  Context Module

                                                                                                                                  Decoder

                                                                                                                                                Decoder
                                                                                                                                  Module

                                                                                                                                                Module
                                                                                                                   Mod
                                                                                                                   Dec

                                                                                                                                                                                                            Foreground Mask
                                                                                                                                                                             Semantic Segmentation
                                                                                                                                                                                     (Sem)
                                           Depth Encoder

     ESANet                                                                                                                                                               Semantic Decoder

                                                                                                                                                                                                                              Panoptic Segmentation

                                                                                                                                  Decoder

                                                                                                                                                Decoder
                                                                                                                                  Module

                                                                                                                                                Module
                                      NBt1D
                                                                                                                   Mod
 Up. ×2

                                                                                                                   Dec
                                                                                                                                                                                    Center
                                                                                    ReLU
                                                  NonBottleneck1D (NBt1D)

                                      NBt1D
                                                                                    BN, ReLU
                                                                                                                                                                                                     Instance Segmentation
                                      NBt1D                                                                                                                                                                   (Ins)
 Decoder Module

                                                                                    ReLU
                                                                                                                                                                                    Offset
                                                                                    BN, Dropout
                  Multi-Scale
                  Supervision                                                       ReLU

                                                                             180°                                                                                               Raw Orientation         Orientation (Or)

                                                                            Sofa
                                                                                                                                                                          Instance Decoder
                                                  270°                                 90°

                                                                                                                         "living room"
                                                            0°
                                Offset Encoding   Orientation Encoding                                             Scene Classification (Sce)                                    Scene Head                                      EMSANet
Fig. 2. Architecture of our Efficient Multi-task Scene Analysis Network (EMSANet) extending ESANet [2] for semantic segmentation (top) with an additional
decoder for instance segmentation and instance orientation estimation as well as a head for scene classification. See Fig. 4 for semantic label colors.

and offset predictions. The semantic class for each instance is                                                                                     bed, chair, sofa, bookshelf, shelves, dresser, refrigerator, tv,
derived by a majority vote from the semantic segmentation.                                                                                          person, nightstand, and toilet. The orientation is crucial when
   Similar to Panoptic DeepLab, we use MSE loss for center                                                                                          approaching objects from the right direction (e.g., chairs
prediction and L1 loss for offset prediction. However, un-                                                                                          or persons) or to restrict waiting positions (e.g., the robot
like Panoptic DeepLab, we mask predicted centers using the                                                                                          should not wait in the sightline to a TV or in front of a
ground-truth instance mask instead of the thing-class mask to                                                                                       freestanding chair or cabinet). To accomplish this, as shown
account for missing instance annotations in the ground truth.                                                                                       in Fig. 2 (middle), our instance decoder also predicts orien-
We also adopt their postprocessing, including thresholding and                                                                                      tations as continuous angles around the axis perpendicular to
keypoint non-maximum suppression using max-pooling for the                                                                                          the ground (see bottom-left legend for orientation encoding
centers and the final merging of instance and semantic seg-                                                                                         in Fig. 2). Instead of relying on a patch-based orientation
mentation putting more focus on instances. However, we faced                                                                                        estimation, we follow our dense prediction design and propose
some problems when applying their training regime. Panoptic                                                                                         to predict the orientation for all pixels of an instance. This way,
DeepLab uses linear outputs for estimating both centers and                                                                                         the instance awareness of our instance decoder can further be
absolute offsets. This results in losses being unbounded and                                                                                        strengthened. Moreover, to determine an instance’s orientation,
quite imbalanced, and, thus, requires a carefully tuned initial-                                                                                    we are able to average multiple predictions approximating an
ization and loss weights such as 200 : 0.1 for center : offsets as                                                                                  ensemble effect. We use the biternion encoding [35] and the
used in their implementation. Moreover, absolute offset vectors                                                                                     von Mises loss function [35] to account for the periodicity of
do not generalize to varying input resolutions. To address these                                                                                    angles and to avoid discontinuities in the loss.
issues, we use sigmoid activation for instance centers and a
                                                                                                                                                    C. Scene Classification
tanh activation for encoding relative instance offsets. Thus,
the outputs are bounded within [0, 1] and [−1, 1], respectively.                                                                                       For scene classification, as shown in Fig. 2 (bottom), we
We observed great improvements in terms of stability during                                                                                         simply apply a fully-connected layer on top of the context
optimization and performance for instance segmentation.                                                                                             module. However, as scene classification requires global con-
                                                                                                                                                    text, we connect the fully-connected layer directly to the global
B. Instance Orientation Estimation                                                                                                                  average pooled branch of the context module. Due to the noisy
  Our approach further predicts the orientation for instances                                                                                       nature of scene classes, we further utilize label smoothing
of thing classes relevant for our indoor scenario, i.e., cabinet,                                                                                   during training.

                                                                                                                                                4
                         IV. DATASETS                                                                     TABLE I
                                                                                 Overview about the datasets used for our multi-task approach.
   Training our proposed multi-task approach is challenging                                        Split     # Images    # Instances    # Orientations
as it requires comprehensive data providing annotations for
                                                                                 NYUv2             train         795         12,092               2,696
all tasks. Moreover, our approach relies on both RGB and                                           test          654          9,874               2,069
depth images as input. Based on these requirements and our                       SUNRGB-D          train        5,285        18,171              13,076
application scenario, below, we examine common RGB-D                                               test         5,050        16,961              12,440
datasets for their suitability. Furthermore, we describe how                     Hypersim          train       57,443     3,009,566                   -
we enriched these datasets to enable training our multi-task                                       valid        7,286       261,677                   -
                                                                                                   test         7,690       374,052                   -
approach. Additional annotations are publicly available.
   NYUv2: The NYUv2 dataset [3] provides dense anno-                                                        TABLE II
tations for both semantic and instance segmentation. For                          Distribution of scene classes for all datasets and their splits.
semantics, we use the common 40 classes setting. However,                                      NYUv2              SUNRGB-D                      Hypersim
                                                                                            train  test          train  test            train     valid     test
this may lead to very small instances getting assigned to
misleading classes, e.g. door knobs are assigned to cabinet,              void                29        0          745     507          1,370         0        0
                                                                          bathroom            63       58          331     293          3,378       400      300
dresser, or nightstand. To avoid such bad assignments, we                 bedroom            192      191          558     526          4,386       499      400
restrict instances to have at least an area of 0.25% of the               dining room         66       55          311     296          1,894       200      100
                                                                          discussion room      5        0          691     753          1,013       100        0
image area. For enabling panoptic segmentation, we declare                hallway              0        0          222     151            400       100        0
wall, floor, and ceiling to be background (stuff classes) and             kitchen            125      110          288     297          6,221       400      600
                                                                          living room        114      107          274     250         18,287     3,017    2,855
consider the remaining classes as thing classes. In addition to           office              88       78          820     792          5,026       100      389
these dense annotations, NYUv2 also provides ground-truth                 other indoor       113       55        1,041   1,180         15,068     2,370    2,846
                                                                          stairs               0        0            4       5            400       100      200
labels for scene classification. However, annotations for in-
stance orientations are missing so far. Therefore, we manually               Hypersim: Unlike SUNRGB-D and NYUv2, Hyper-
annotated the orientation for instances of the semantic classes           sim [49] is a photo-realistic synthetic dataset. For its creation,
mentioned in Sec. III-B. Due to perspective distortions, exact            virtual cameras were placed in 461 professionally rendered
annotation of the orientation as egocentric angle around the              3D scenes, resulting in 77,400 samples, of which we use
axis perpendicular to the ground is not possible in the pure              72,419. We blacklisted the remaining samples due to several
RGB image, which is why we annotated them directly in a                   scene or trajectory issues, i.e., void/single semantic label only,
point cloud.                                                              missing textures, or invalid depth. Each sample provides an
   SUNRGB-D: The SUNRGB-D dataset [4] combines mul-                       RGB-D image, a mask for semantics and instances, instance
tiple indoor RGB-D datasets, including NYUv2, and enriches                orientations, and a scene label. However, the annotations for
them with additional annotations, making SUNRGB-D to be                   instance orientation are not consistent and, thus, cannot be
one of the most important datasets for real-world applications.           used without further manual refinement. As Hypersim adopts
The dataset comes with annotations for scene classification and           the NYUv2 semantic classes, the same partitioning for stuff
semantic segmentation. Compared to NYUv2, the last three                  and thing can be applied for panoptic segmentation.
semantic filling classes, i.e., otherstructure, otherfurniture, and          Final remarks and further adjustments: Due to the addi-
otherprop, are omitted and assigned to void. Moreover, some               tional annotations, both NYUv2 and SUNRGB-D are suitable
semantic annotations in the NYUv2 part have further been                  for training our full multi-task approach. HyperSim provides
assigned to the void class, resulting in minor differences to             high-quality synthetic data and, thus, is well suited for pre-
the original NYUv2 dataset. Unfortunately, annotations for                training. Tab. I summarizes important statistics for all datasets
instance segmentation and instance orientation estimation are             used for training and evaluating our multi-task approach. For
missing. However, fortunately, SUNRGB-D also provides 3D                  scene classification, we further created an own spectrum of
bounding boxes, each with a class label and orientation, that             classes that unifies the classes in all datasets and accounts for
can be used for instance extraction. To obtain instances, we              similar classes. The resulting spectrum is tailored for indoor
first created a mapping between semantic and box classes.                 applications and is comprised of the classes listed in Tab. II.
Subsequently, we matched the box clusters with the semantic               Note that the void class is used for images with unclear
point cloud in 3D. During matching, a unique instance label               assignment that may disturb the learning process. Furthermore,
was assigned to all pixels belonging to the same semantic                 images that show indoor scenes but cannot be assigned to one
class. This way, an instance mask as well as the orientation              of the mentioned classes are considered as other indoor.
could be extracted for each bounding box. However, one
limitation of this approach is that not all objects within a scene                                         V. E XPERIMENTS
were annotated with a 3D bounding box, making the instance                  We evaluate our approach in several settings on the indoor
masks more sparse. To compensate this to some extent, we                  datasets NYUv2 and SUNRGB-D. First, we use the smaller
also merged the instance masks and orientations of NYUv2                  NYUv2 dataset to elaborate suitable hyperparameters and task
back to SUNRGB-D. For panoptic segmentation, we consider                  weights. We establish single-task baselines for each task and,
the same semantic classes to belong to stuff as for NYUv2.                subsequently, compare them to several multi-task settings.

                                                                      5
Finally, we extend our studies to SUNRGB-D and Hypersim to                  Orientation Estimation (Or): For evaluating instance ori-
examine the applicability to larger datasets and the relevance           entations, we use the mean absolute angular error (MAAE)
of synthetic data for pretraining.                                       in degrees similar to [36], [38], i.e., in contrast to the other
                                                                         metrics, lower is better, and the maximum error is 180. We
A. Implementation Details                                                report the MAAE for two settings: 1) independently of other
   Our architecture as well as the pipelines for training and            tasks, i.e., using the ground-truth instances, and 2) for matched
evaluation are implemented using PyTorch [50]. We used pre-              instances after panoptic merging. Note that we do not penalize
trained weights on ImageNet [39] to initialize both encoders             unmatched instances for the latter setting.
and trained each network for 500 epochs with a batch size                   Scene Classification (Sce): As the scene class labels are
of 8. For optimization, we used SGD with momentum of                     imbalanced, we evaluate scene classification with the balanced
0.9 and a small weight decay of 0.0001. For determining                  accuracy (bAcc).
a suitable learning rate, we performed a grid search with
values of {0.00125, 0.0025, 0.005, 0.01, 0.02, 0.03, 0.04,               C. Single-task Setting
0.08, 0.12}. The learning rate was further adapted during                   We aim at solving multiple tasks at once using a single neu-
training using a one-cycle learning rate scheduler. To increase          ral network. To be able to elaborate whether this diminishes or
the number of samples, we augmented images using random                  boosts the performance of individual tasks, we first conducted
scaling, cropping, and flipping. For RGB images, we further              experiments in a single-task setting. Furthermore, the goal was
applied slight color jittering in HSV space.                             to examine how the new tasks behave for different modalities,
   For postprocessing instance centers, we first apply a thresh-         and how the additional network parts affect inference time on
old of 0.1 and max-pooling with pooling size of 17 to perform            a mobile platform. Note that performing instance segmentation
keypoint non-maximum suppression, and finally filter the top-            solely requires semantics and a foreground mask. We use the
64 instances. The pooling size results in the network not being          ground-truth semantic segmentation in this case, leading to
able to predict instance centers closer than 8 pixels away               RQst , SQst , and PQst to always be equal to 1. Moreover, as
from each other. However, for both NYUv2 and SUNRGB-                     instance orientation estimation requires instance masks, we
D, this decision affects less than 1% of the instances. For              rely on the ground-truth instances as well.
further details and other hyperparameters, we refer to our                  Fig. 3 shows the results of this set of experiments. It
implementation available on GitHub.                                      becomes obvious that all tasks are able to benefit from incorpo-
                                                                         rating complementary information processed in an additional
B. Metrics                                                               depth branch instead of processing RGB only. For semantic
   As we focus on fast inference, we do not apply any testing            and instance segmentation, the results coincide with our find-
tricks such as horizontal flipping or multiscale inputs. Before          ings in [2] that, whenever possible, processing both RGB and
obtaining any performance metric for dense predictions, we               depth should be preferred over applying a more sophisticated
resize the predictions to the full resolution of the ground truth.       single-modality RGB encoder. The results further show that
   Semantic Segmentation (Sem): As common for this task,                 depth is crucial for estimating the orientation more accurately,
we use the mean intersection over union (mIoU).                          and that RGB is essential for scene classification. Finally,
   Panoptic Segmentation: The common metric for panoptic                 when comparing different backbones, it becomes obvious
segmentation is the panoptic quality (PQ) [17]. The panoptic             that, for all tasks except of scene classification, backbones
quality PQc for each class c is determined by the product of             featuring the NonBottleneck1D block (NBt1D) lead to better
the recognition quality (RQc ), i.e. the percentage of correctly         results in terms of both performance and inference throughput
detected instances similar to F1 -score, and the segmentation            compared to their counterparts with BasicBlock. Even more,
quality (SQc ), i.e., the segmentation accuracy similar to mIoU          ResNet34 NBt1D often competes with the more complex
but only for matched segments. These metrics are typically               ResNet50 while enabling faster inference. Therefore, we stick
averaged across all stuff (st) and thing (th) classes, resulting         to ResNet34 NBt1D for the remaining experiments.
in RQst , SQst , PQst and RQth , SQth , PQth , respectively. It is
also common to average the three metrics independently of                D. Multi-task Setting
stuff and things across all classes, resulting in RQ, SQ, and               Learning multiple tasks using a single neural network is
PQ. Note that determining the metrics this way results in PQ             challenging, as the tasks may influence each other. Thus,
to be typically not equal to RQ · SQ. For SUNRGB-D, we                   tuning the task weights, which balance the losses to each other,
further ignore the classes floor mat and shower curtain as no            is crucial. With uncertainty weighting [52], GradNorm [53],
instances of these classes occur in the test split.                      Dynamic Weight Average [54], and VarNorm [55], several
   Instance Segmentation (Ins): For instance segmentation,               approaches for determining the weights automatically have
we also stick to panoptic quality instead of reporting the               been proposed. Unfortunately, none of them led to good
average precision (AP) as this would require assigning a                 performance in our scenario. Therefore, we performed exten-
confidence score to each instance [51]. Moreover, AP and PQ              sive experiments to determine suitable task weights. We first
track closely, which is why the latter also evaluates instance           combined two tasks at a time to elaborate essential relations
segmentation in a meaningful way [17].                                   between tasks. With these findings at hand, we were able to

                                                                     6
                       (a) Semantic Segmentation (Sem)                                                 (b) Instance Segmentation (Ins)
               ResNet101                                                               62
       50                     ResNet34 NBt1D
            ResNet50
→

                                                                                       60

                                                                                →
       48
                 ResNet34             ResNet18 NBt1D
       46                           ResNet18                                           58
mIoU

                                                                                PQ
       44                                                                              56
       42
                                                                                       54
               RGB-D
       40
               RGB                                                                     52
       38      Depth
                                                                                       50
               20        30      40        50        60       70       80                        20    30      40         50       60      70       80
                                        FPS      →                                                                   FPS       →
                    (c) Instance Orientation Estimation (Or)                                            (d) Scene Classification (Sce)
       26      ResNet18         ResNet18 NBt1D                                         76
               ResNet34         ResNet34 NBt1D
←

                                                                                →
       24      ResNet50                                                                74
               ResNet101
MAAE

                                                                                bAcc
       22                                                                              72

       20                                                                              70

       18                                                                              68

               20        30      40        50        60       70       80                   25    50   75    100    125    150     175   200     225
                                      FPS       →                                                                    FPS       →
Fig. 3. Results on NYUv2 test split when performing each task in a single-task setting with various backbones over the inference throughput in frames per
second measured on an NIVIDA Jetson AGX Xavier (Jetpack 4.6, TensorRT 8, Float16). See Sec. V-B for metric abbreviations.

restrict the search space for the full multi-task setting. Tab. III              of the predicted foreground mask.
summarizes the best results and compares them to their single-                      Ins + Or: The results in Tab. III (MT III) reveal that both
task counterparts of Fig. 3. Furthermore, it lists the applied                   tasks can be performed using a single decoder. Compared to
task weights, the learning rate, and the achieved frames per                     the single-task baseline, this setting slightly improves orien-
second on an NVIDIA Jetson AGX Xavier.                                           tation estimation, almost surpassing the reachable level for
   Sem + Sce: As shown in Tab. III (MT I), combining both                        annotating orientations in 3D. However, even when putting
tasks requires a much larger weight for semantic segmentation                    more weight on instance segmentation, we always observed a
to reach its single-task performance. However, even when                         slight drop in PQ.
putting more weight on semantic segmentation, scene clas-                           Sem + Sce + Ins + Or: With the findings of the aforemen-
sification benefits from such a setting, already closing the gap                 tioned dual-task experiments at hand, we combined all tasks
shown in Fig. 3 (d) for ResNet34 NBt1D and ResNet34. This                        in a single neural network. The best result is presented in
shows that knowledge about the individual parts of a scene is                    Tab. III (MT IV). It becomes obvious that both semantic
shared and helps to classify the scene.                                          segmentation and scene classification greatly benefit from the
   Sem + Ins: This setting allows obtaining panoptic results                     entire multi-task setting. Instance segmentation and instance
with predicted semantic segmentation for the first time. As                      orientation estimation almost reach the same level of accu-
the semantic segmentation provides the semantics and the                         racy as when performed in single-task settings. The panoptic
foreground mask for instance segmentation, combing these                         results, i.e., after merging semantic and instance predictions,
two tasks is crucial for our multi-task system. As shown in                      are similar to the multi-task setting MT II. The mIoU obtained
Tab. III (MT II), the best PQ is achieved by putting more                        after merging is slightly lower than before merging but still
focus on instance segmentation. The mIoU obtained for the                        at a similar level. This indicates that the applied merging of
semantic decoder indicates that the network further benefits                     both predictions with focus on instances does not diminish
from performing both tasks in conjunction. When keeping in                       the semantic segmentation result. The detailed breakdown of
mind, that the PQ for the instance decoder is computed using                     the IoUs in Fig. 4 shows that this holds true for almost
the ground-truth semantic segmentation, it is reasonable that                    all classes. Finally, when taking a look at the results for
the PQ for the panoptic results is lower. With ground-truth                      orientation estimation, it can be seen that the orientation error
semantic segmentation, the network reaches an RQ of 70.15                        after merging is lower than the error for the instance decoder.
and a SQ of 85.78 (not listed in Tab. III). This shows that the                  However, this does not necessarily indicate better results, as
drop in PQ is mainly due to a loss in RQ. We observed that                       the MAAE after panoptic merging only represents instances
this is mostly caused by small instances, which are not part                     that could be matched.

                                                                            7
                                                                           TABLE III
Results obtained on NYUv2 test split when training EMSANet with ResNet34 NBt1D backbone in various multi-task settings. See Sec. V-B for details on
  the reported metrics. Panoptic results are obtained after merging semantic and instance prediction. Legend: italic: metric used for determining the best
 checkpoint, *: best result within the same run, Lr: learning rate, pre.: additional pretraining on Hypersim, FPS: frames per second on an NVIDIA Jetson
                                                      AGX Xavier (Jetpack 4.6, TensorRT 8, Float16).
                                                                                                          Semantic                     Instance          Scene                 Panoptic Results
                                                                                                          Decoder                      Decoder            Head                  (after merging)
                                                           Task Weights                    Lr              mIoU ↑                   PQ ↑ MAAE ↓          bAcc ↑      mIoU ↑   PQ ↑ RQ ↑ SQ ↑ MAEE ↓          FPS ↑
          Semantic Segmentation (Sem)                             —                       0.04                49.66                  —        —            —           —       —     —     —       —         32.4
          Instance Segmentation (Ins)                             —                       0.08                 —                    61.39     —            —           —       —     —     —       —         38.3
 ST

          Orientation Estimation (Or)                             —                       0.02                 —                     —       18.06         —           —       —     —     —       —         35.5
          Scene Classification (Sce)                              —                       0.02                 —                     —        —           72.40        —       —     —     —       —         55.9
          Sem + Sce                                              3:1                      0.02                49.57                  —        —           74.29        —       —     —     —       —         32.2
MT
 I

          Sem + Sce *                                                                                         49.57                  —        —           77.30        —       —     —     —       —
          Sem + Ins                                              1:3                      0.03                50.22                 60.90     —            —          50.24   43.74 52.46 82.43    —         25.8
MT
II

          Sem + Ins *                                                                                         50.22                 61.61     —            —          50.54   43.74 52.50 82.63    —
          Ins + Or                                               3:1                      0.04                 —                    59.72    17.66         —           —       —     —     —       —         35.5
MT
III

          Ins + Or *                                                                                           —                    59.72    17.53         —           —       —     —     —       —
          Sem + Sce + Ins + Or                             1 : 0.25 : 3 : 1               0.04                50.97                 61.35    19.01        76.46       50.54   43.56 52.20 82.48   16.38      24.5
MT
IV

          Sem + Sce + Ins + Or *                                                                              51.15                 61.53    18.93        78.18       51.31   43.56 52.27 82.70   15.76

          Sem + Sce + Ins + Or (pre.)                      1 : 0.25 : 3 : 1               0.01                53.34                 64.41    18.84        75.25       53.79   47.38 55.95 83.74   15.91      24.5
MT
V

          Sem + Sce + Ins + Or (pre.) *                                                                       53.55                 64.98    18.27        76.98       54.00   47.38 55.99 84.08   15.56

E. Results on SUNRGB-D                                                                                                                   Note that the panoptic quality does not account for these
                                                                                                                                         areas as they are labeled as void class in the ground truth.
   After elaborating suitable multi-task parameters, we also
                                                                                                                                         However, as shown in the last row, missing instance centers
applied our approach to the larger SUNRGB-D dataset. How-
                                                                                                                                         can still lead to assigning pixels far away to the same instance,
ever, as instances in SUNRGB-D are more sparse, we put
                                                                                                                                         lowering the PQ and mIoU after merging. We already observed
less weight on the instance decoder and used the mIoU for
                                                                                                                                         a great benefit when masking centers based on the ground-
determining the best checkpoint. The results are listed in
                                                                                                                                         truth instance mask during training, as proposed in Sec. III-A.
Tab. IV. Compared to the single-task baselines, our multi-
                                                                                                                                         For real-world application, we further tackle this issue by
task approach reaches slightly better performance for semantic
                                                                                                                                         thresholding predicted offsets after shifting and assign an
segmentation and scene classification. The result for orienta-
                                                                                                                                         unknown instance label if they are too far away from a center.
tion estimation is still suitable for real-world application. As
shown in Fig. 5, the network generalizes well for instance                                                                               F. Additional Pretraining on Hypersim
segmentation even though annotations are much more sparse.                                                                                  Finally, we examined how pretraining on the synthetic
                                                              book-                                                                      Hypersim dataset affects the performance of our derived multi-
                                              counter picture
                                         blinds               shelf window
                                  desk                                                    door
                                                                                                                                         task setting for both NYUv2 and SUNRGB-D. For further
                       shelves                                                                   table                                   details on the pretraining, we refer to our implementation. The
                curtain
                                                  before merging (mIoU: 50.97)
                                                                                                          sofa                           results are shown in Tab. III (MT V) and Tab. IV (MT V). It
                                                  after merging (mIoU: 50.54)
           dresser                                                                                               chair
                                                                                                                                         turns out that, for NYUv2, especially mIoU and PQ greatly
                                                                                                                                         benefit from additional pretraining, while, for SUNRGB-D,
      pillow                                                                                                          bed
                                                                                                                                         only the performance of instance-related tasks is improved.
  mirror                                                                                                                 cabinet         This can be deduced to the fact that SUNRGB-D alone is
                                                                                                                                         already much larger than NYUv2. Fig. 6 shows qualitative
 floor
                                                                                                                            floor
 mat

clothes
                                                             0                                                              wall
                                                                 10
                                                                      20
                                                                           30                                              other
ceiling
                                                                                                                           prop
                                                                                40
                                                                                     50                                 other
  books                                                                                   60                          furniture
                                                                                               70
                                                                                                    80               other
 refrigerator
                                                                                                         90        structure

          television                                                                                           bag

                  paper                                                                                  bathtub

                          towel                                                                  lamp
                                  shower
                                                                                          sink
                                  curtain
                                            box    white-       night toilet
                                                   board person stand
                                                                                                                                         Fig. 5. Qualitative results on SUNRGB-D test split highlighting faced
Fig. 4. Semantic IoUs on NYUv2 test split for the full multi-task network                                                                challenges (Sec V-E) as RGB image, ground-truth panoptic segmentation with
(MT IV) before and after merging semantic and instance segmentation.                                                                     orientations, and predicted panoptic segmentation with orientations.

                                                                                                                                     8
                                                                             TABLE IV
      Results obtained on SUNRGB-D test split when training EMSANet with ResNet34 NBt1D backbone in both single-task and multi-task settings. See
    Sec. V-B for details on the reported metrics. Panoptic results are obtained after merging semantic and instance prediction. Legend: italic: metric used for
                 determining the best checkpoint, *: best result within the same run, Lr: learning rate, pre.: additional pretraining on Hypersim.
                                                                                      Semantic            Instance          Scene                    Panoptic Results
                                                                                      Decoder             Decoder            Head                     (after merging)
                                                        Task Weights          Lr       mIoU ↑          PQ ↑ MAAE ↓          bAcc ↑       mIoU ↑     PQ ↑ RQ ↑ SQ ↑ MAEE ↓
                       Semantic Segmentation (Sem)            —             0.005      48.23            —         —          —             —         —     —      —        —
                       Instance Segmentation (Ins)            —             0.01        —              60.99      —          —             —         —     —      —        —
                  ST

                       Orientation Estimation (Or)            —             0.005       —               —        13.68       —             —         —     —      —        —
                       Scene Classification (Sce)             —             0.001       —               —         —         58.66          —         —     —      —        —
                       Sem + Sce + Ins + Or            1 : 0.25 : 2 : 0.5   0.005      48.39           60.60     16.81      61.83         45.56     50.15 58.14 84.85     14.24
                  MT
                  IV

                       Sem + Sce + Ins + Or *                                          48.39           61.48     16.70      62.66         45.66     50.53 58.66 85.20     14.15

                       Sem + Sce + Ins + Or (pre.)     1 : 0.25 : 2 : 0.5   0.0025     48.47           64.24     18.40      57.22         44.18     52.84 60.67 86.01     14.10
                  MT
                  V

                       Sem + Sce + Ins + Or (pre.) *                                   48.47           64.82     17.94      59.39         45.04     53.35 61.31 86.25     14.04

results from pretraining on Hypersim and subsequent training                                                                         TABLE V
on NYUv2. The latter represents our best network for NYUv2.                                        Comparison to other state-of-the-art approaches on NYUv2 test split without
                                                                                                   test-time augmentation. Legend: italic: metric used for determining the best
                                                                                                      checkpoint, *: (re)training on our enriched NYUv2 dataset, †: ten-crop
G. Comparison to State of the Art                                                                         evaluation at 224×224. pre.: additional pretraining on Hypersim.
   Comparing our approach to the state of the art is challenging                                                          Backbone           Mod.        mIoU ↑   PQ ↑       bAcc ↑
as tasks such as orientation estimation or scene classification
                                                                                                   ESANet [2]             2×R34-Nbt1d      RGB-D         50.30        —           —
have not been considered so far in related work due to                                             ShapeConv [16]         ResNext101 32x8d RGB-D         50.20
missing annotations and a deviating class spectrum. Moreover,                                      Panoptic DeepLab* [23] R50                RGB         39.42    30.99           —
panoptic segmentation has not yet been attempted on NYUv2                                                                 R101               RGB         42.55    35.32           —

or SUNRGB-D. Therefore, we first established comprehensive                                         MobileNetV2* [41]      α=1                RGB           —          —        69.30†
                                                                                                   EfficientNet* [42]     B0                 RGB           —          —        70.83†
single-task baselines (see Fig. 3) covering common backbones
                                                                                                   Mod. ResNet34 (ours)   R34-Nbt1d          RGB           —          —        70.25†
ranging from sophisticated backbones to more efficient back-
bones that also enable mobile application. Beyond that, we                                         EMSANet (ours)         R34-Nbt1d          RGB         44.66    37.69        70.88
                                                                                                                          2×R34-Nbt1d        RGB-D       50.97    43.56        76.46
further trained well-known approaches for panoptic segmenta-                                                              2×R101-Nbt1d       RGB-D       50.83    45.12        77.41
tion and scene classification on NYUv2, as shown in Tab. V.                                        EMSANet pre. (ours)    2×R34-Nbt1d        RGB-D       53.34    47.38        75.25
For Panoptic DeepLab, we applied the same parameters as de-
scribed in Sec. III-A for keypoint non-maximum suppression                                         training and evaluation, we have enriched the annotations of
to postprocess instance centers. To summarize, our proposed                                        the common RGB-D indoor datasets NYUv2 and SUNRGB-
lightweight EMSANet achieves comparable or even better                                             D, which we also make publicly available. To the best of
results than other approaches. Moreover, larger backbones do                                       our knowledge, we are the first to provide results in such a
not necessarily improve performance but significantly increase                                     comprehensive multi-task setting for indoor scene analysis.
resource requirements.                                                                             We have shown that all tasks can be solved using a single
                                                                                                   multi-task network. Moreover, the individual tasks can benefit
                                          VI. C ONCLUSION                                          from each other when trained together. Due to the efficient
   In this paper, we have proposed an efficient RGB-D multi-                                       design, our approach enables fast inference, i.e. 24.5 FPS on
task approach for panoptic segmentation, instance orientation                                      an NVIDIA Jetson AGX Xavier and, thus, is well suited for
estimation, and scene classification, called EMSANet. For                                          mobile robotic applications.
Hypersim (test)

                                       living room                     other indoor                            kitchen                   living room                        living room
NYUv2 (test)

                                         bedroom                            kitchen                            kitchen                       kitchen                        living room
  Fig. 6. Qualitative results as RGB image overlayed with predicted panoptic segmentation, predicted scene class, and, for NYUv2, estimated orientations.

                                                                                               9
                              R EFERENCES                                              [29] R. Hou et al., “Real-time panoptic segmentation from dense detections,”
                                                                                            in Proc. of CVPR, 2020, pp. 8523–8532.
 [1] D. Seichter, P. Langer, T. Wengefeld, B. Lewandowski, D. Höchemer,               [30] D. de Geus, P. Meletis, and G. Dubbelman, “Fast panoptic segmentation
     and H.-M. Gross, “Efficient and robust semantic mapping for indoor                     network,” RAL, vol. 5, no. 2, pp. 1742–1749, 2020.
     environments,” in Proc. of ICRA, 2022.                                            [31] A. Mousavian, D. Anguelov, J. Flynn, and J. Kosecka, “3d bounding
 [2] D. Seichter, M. Köhler, B. Lewandowski, T. Wengefeld, and H.-M.                       box estimation using deep learning and geometry,” in Proc. of CVPR,
     Gross, “Efficient rgb-d semantic segmentation for indoor scene analysis,”              2017, pp. 7074–7082.
     in Proc. of ICRA, 2021, pp. 13 525–13 531.                                        [32] L. Liu, J. Lu, C. Xu, Q. Tian, and J. Zhou, “Deep fitting degree scoring
 [3] N. Silberman, D. Hoiem, P. Kohli, and R. Fergus, “Indoor Segmentation                  network for monocular 3d object detection,” in Proc. of CVPR, 2019,
     and Support Inference from RGBD Images,” in Proc. of ECCV, 2012.                       pp. 1057–1066.
 [4] S. Song, S. P. Lichtenberg, and J. Xiao, “SUN RGB-D: A RGB-D Scene                [33] Y. Zhang, J. Lu, and J. Zhou, “Objects are different: Flexible monocular
     Understanding Benchmark Suite,” in Proc. of CVPR, 2015, pp. 567–576.                   3d object detection,” in Proc. of CVPR, 2021, pp. 3289–3298.
 [5] H. Zhao, J. Shi, X. Qi, X. Wang, and J. Jia, “Pyramid scene parsing               [34] Z. Cao, T. Simon, S.-E. Wei, and Y. Sheikh, “Realtime multi-person 2d
     network,” in Proc. of CVPR, 2017, pp. 2881–2890.                                       pose estimation using part affinity fields,” in Proc. of CVPR, 2017, pp.
 [6] L.-C. Chen, G. Papandreou, I. Kokkinos, K. Murphy, and A. L. Yuille,                   7291–7299.
     “Semantic image segmentation with deep convolutional nets and fully               [35] L. Beyer, A. Hermans, and B. Leibe, “Biternion nets: Continuous
     connected crfs,” in Proc. of ICLR, 2015.                                               head pose regression from discrete training labels,” in Proc. of GCPR.
 [7] L.-C. Chen, G. Papandreou, F. Schroff, and H. Adam, “Rethinking                        Springer, 2015, pp. 157–168.
     Atrous Convolution for Semantic Image Segmentation,” arXiv preprint               [36] B. Lewandowski, D. Seichter, T. Wengefeld, L. Pfennig, H. Drumm, and
     arXiv:1706.05587, 2017.                                                                H.-M. Gross, “Deep orientation: Fast and robust upper body orientation
 [8] L.-C. Chen, Y. Zhu, G. Papandreou, F. Schroff, and H. Adam, “Encoder-                  estimation for mobile robotic applications,” in Proc. of IROS, 2019, pp.
     Decoder with Atrous Separable Convolution for Semantic Image Seg-                      441–448.
     mentation,” in Proc. of ECCV, 2018, pp. 801–818.                                  [37] T. Wengefeld, B. Lewandowski, D. Seichter, L. Pfennig, and H.-M.
                                                                                            Gross, “Real-time person orientation estimation using colored point-
 [9] E. Romera, J. M. Alvarez, L. M. Bergasa, and R. Arroyo, “ERFNet:
                                                                                            clouds,” in Proc. of ECMR, 2019.
     Efficient Residual Factorized ConvNet for Real-Time Semantic Segmen-
                                                                                       [38] D. Seichter, B. Lewandowski, D. Höchemer, T. Wengefeld, and H.-M.
     tation,” ITS, pp. 263–272, 2018.
                                                                                            Gross, “Multi-task deep learning for depth-based person perception in
[10] M. Oršić, I. Krešo, P. Bevandić, and S. Šegvić, “In Defense of Pre-
                                                                                            mobile robotics,” in Proc. of IROS. IEEE, 2020, pp. 10 497–10 504.
     trained ImageNet Architectures for Real-time Semantic Segmentation
                                                                                       [39] O. Russakovsky et al., “ImageNet Large Scale Visual Recognition
     of Road-driving Images,” in Proc. of CVPR, 2019, pp. 12 607–12 616.
                                                                                            Challenge,” in IJCV, 2015, pp. 211–252.
[11] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image            [40] J. Hu, L. Shen, and G. Sun, “Squeeze-and-excitation networks,” in Proc.
     recognition,” in Proc. of CVPR, 2016, pp. 770–778.                                     of CVPR, 2018, pp. 7132–7141.
[12] C. Hazirbas, L. Ma, C. Domokos, and D. Cremers, “FuseNet: Incor-                  [41] M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen,
     porating Depth into Semantic Segmentation via Fusion-based CNN                         “Mobilenetv2: Inverted residuals and linear bottlenecks,” in Proc. of
     Architecture,” in Proc. of ACCV, 2016, pp. 213–228.                                    CVPR, 2018, pp. 4510–4520.
[13] X. Hu, K. Yang, L. Fei, and K. Wang, “ACNet: Attention Based Network              [42] M. Tan and Q. Le, “Efficientnet: Rethinking model scaling for convo-
     to Exploit Complementary Features for RGBD Semantic Segmentation,”                     lutional neural networks,” in Proc. of ICML, 2019, pp. 6105–6114.
     in Proc. of ICIP, 2019.                                                           [43] T. Standley, A. Zamir, D. Chen, L. Guibas, J. Malik, and S. Savarese,
[14] A. Valada, R. Mohan, and W. Burgard, “Self-supervised model adapta-                    “Which tasks should be learned together in multi-task learning?” in Proc.
     tion for multimodal semantic segmentation,” IJCV, 2019.                                of ICML. PMLR, 2020, pp. 9120–9132.
[15] S. Lee, S. J. Park, and K. S. Hong, “RDFNet: RGB-D Multi-level                    [44] S. Vandenhende, S. Georgoulis, W. Van Gansbeke, M. Proesmans,
     Residual Feature Fusion for Indoor Semantic Segmentation,” Proc. of                    D. Dai, and L. Van Gool, “Multi-task learning for dense prediction tasks:
     ICCV, pp. 4990–4999, 2017.                                                             A survey,” TPAMI, 2021.
[16] J. Cao, H. Leng, D. Lischinski, D. Cohen-Or, C. Tu, and Y. Li,                    [45] S. Vandenhende, S. Georgoulis, and L. V. Gool, “Mti-net: Multi-scale
     “Shapeconv: Shape-aware convolutional layer for indoor rgb-d semantic                  task interaction networks for multi-task learning,” in Proc. of ECCV.
     segmentation,” in Proc. of CVPR, 2021, pp. 7088–7097.                                  Springer, 2020, pp. 527–543.
[17] A. Kirillov, K. He, R. Girshick, C. Rother, and P. Dollár, “Panoptic             [46] Z. Zhang, Z. Cui, C. Xu, Z. Jie, X. Li, and J. Yang, “Joint task-recursive
     segmentation,” in Proc. of CVPR, 2019, pp. 9404–9413.                                  learning for semantic segmentation and depth estimation,” in Proc. of
[18] K. He, G. Gkioxari, P. Dollár, and R. Girshick, “Mask R-CNN,” Proc.                   ECCV, 2018, pp. 235–251.
     of ICCV, pp. 2961–2969, 2017.                                                     [47] K. He, X. Zhang, S. Ren, and J. Sun, “Delving deep into rectifiers:
[19] A. Kirillov, R. Girshick, K. He, and P. Dollár, “Panoptic feature pyramid             Surpassing human-level performance on imagenet classification,” in
     networks,” in Proc. of CVPR, 2019, pp. 6399–6408.                                      Proc. of ICCV, 2015, pp. 1026–1034.
[20] Y. Xiong et al., “Upsnet: A unified panoptic segmentation network,” in            [48] P. Goyal et al., “Accurate, large minibatch sgd: Training imagenet in 1
     Proc. of CVPR, 2019, pp. 8818–8826.                                                    hour,” arXiv preprint arXiv:1706.02677, 2017.
[21] T.-J. Yang et al., “Deeperlab: Single-shot image parser,” arXiv preprint          [49] M. Roberts et al., “Hypersim: A Photorealistic Synthetic Dataset for
     arXiv:1902.05093, 2019.                                                                Holistic Indoor Scene Understanding,” in Proc. of ICCV, 2021.
[22] N. Gao et al., “Ssap: Single-shot instance segmentation with affinity             [50] A. Paszke et al., “Pytorch: An imperative style, high-performance deep
     pyramid,” in Proc. of ICCV, 2019, pp. 642–651.                                         learning library,” in Proc. of NeurIPS. Curran Associates, Inc., 2019,
[23] B. Cheng et al., “Panoptic-deeplab: A simple, strong, and fast baseline                pp. 8024–8035.
     for bottom-up panoptic segmentation,” in Proc. of CVPR, 2020, pp.                 [51] T.-Y. Lin et al., “Microsoft coco: Common objects in context,” in Proc.
     12 475–12 485.                                                                         of ECCV, 2014.
[24] H. Wang, Y. Zhu, H. Adam, A. Yuille, and L.-C. Chen, “Max-deeplab:                [52] A. Kendall, Y. Gal, and R. Cipolla, “Multi-task learning using uncer-
     End-to-end panoptic segmentation with mask transformers,” in Proc. of                  tainty to weigh losses for scene geometry and semantics,” in Proc. of
     CVPR, 2021, pp. 5463–5474.                                                             CVPR, 2018, pp. 7482–7491.
[25] A. Vaswani et al., “Attention is all you need,” Proc. of NeurIPS, vol. 30,        [53] Z. Chen, V. Badrinarayanan, C.-Y. Lee, and A. Rabinovich, “Gradnorm:
     2017.                                                                                  Gradient normalization for adaptive loss balancing in deep multitask
[26] R. Mohan and A. Valada, “Efficientps: Efficient panoptic segmentation,”                networks,” in Proc. of ICML. PMLR, 2018, pp. 794–803.
     IJCV, vol. 129, no. 5, pp. 1551–1579, 2021.                                       [54] S. Liu, E. Johns, and A. J. Davison, “End-to-end multi-task learning
[27] W. Hong, Q. Guo, W. Zhang, J. Chen, and W. Chu, “Lpsnet: A                             with attention,” in Proc. of CVPR, 2019, pp. 1871–1880.
     lightweight solution for fast panoptic segmentation,” in Proc. of CVPR,           [55] V. R. Kumar et al., “Omnidet: Surround view cameras based multi-task
     2021, pp. 16 746–16 754.                                                               visual perception network for autonomous driving,” RAL, vol. 6, no. 2,
[28] C.-Y. Chang, S.-E. Chang, P.-Y. Hsiao, and L.-C. Fu, “Epsnet: efficient                pp. 2830–2837, 2021.
     panoptic segmentation network with cross-layer attention fusion,” in
     Proc. of ACCV, 2020.

                                                                                  10
