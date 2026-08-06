---
source_id: 068
bibtex_key: ranftl2022midas
title: Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-Shot Cross-Dataset Transfer
year: 2022 (praterbit arXiv 2019; diterima 2020)
domain_theme: Estimasi Kedalaman
verified_pdf: 68_MiDaS (Robust Monocular Depth).pdf
char_count: 97922
---

IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                                 1

                                             Towards Robust Monocular Depth Estimation:
                                                        Mixing Datasets for
                                                  Zero-shot Cross-dataset Transfer
                                                          René Ranftl*, Katrin Lasinger*, David Hafner, Konrad Schindler, and Vladlen Koltun

                                               Abstract—The success of monocular depth estimation relies on large and diverse training sets. Due to the challenges associated with
                                               acquiring dense ground-truth depth across different environments at scale, a number of datasets with distinct characteristics and
                                               biases have emerged. We develop tools that enable mixing multiple datasets during training, even if their annotations are incompatible.
arXiv:1907.01341v3 [cs.CV] 25 Aug 2020

                                               In particular, we propose a robust training objective that is invariant to changes in depth range and scale, advocate the use of
                                               principled multi-objective learning to combine data from different sources, and highlight the importance of pretraining encoders on
                                               auxiliary tasks. Armed with these tools, we experiment with five diverse training datasets, including a new, massive data source: 3D
                                               films. To demonstrate the generalization power of our approach we use zero-shot cross-dataset transfer, i.e. we evaluate on datasets
                                               that were not seen during training. The experiments confirm that mixing data from complementary sources greatly improves monocular
                                               depth estimation. Our approach clearly outperforms competing methods across diverse datasets, setting a new state of the art for
                                               monocular depth estimation.

                                               Index Terms—Monocular depth estimation, Single-image depth prediction, Zero-shot cross-dataset transfer, Multi-dataset training

                                                                                                                         F

                                         1    I NTRODUCTION

                                         D      EPTH is among the most useful intermediate representations
                                               for action in physical environments [1]. Despite its utility,
                                         monocular depth estimation remains a challenging problem that
                                                                                                                             diverse environments. We develop novel loss functions that are
                                                                                                                             invariant to the major sources of incompatibility between datasets,
                                                                                                                             including unknown and inconsistent scale and baselines. Our
                                         is heavily underconstrained. To solve it, one must exploit many,                    losses enable training on data that was acquired with diverse
                                         sometimes subtle, visual cues, as well as long-range context and                    sensing modalities such as stereo cameras (with potentially un-
                                         prior knowledge. This calls for learning-based techniques [2], [3].                 known calibration), laser scanners, and structured light sensors.
                                             To learn models that are effective across a variety of scenarios,               We also quantify the value of a variety of existing datasets for
                                         we need training data that is equally varied and captures the diver-                monocular depth estimation and explore optimal strategies for
                                         sity of the visual world. The key challenge is to acquire such data                 mixing datasets during training. In particular, we show that a
                                         at sufficient scale. Sensors that provide dense ground-truth depth                  principled approach based on multi-objective optimization [12]
                                         in dynamic scenes, such as structured light or time-of-flight, have                 leads to improved results compared to a naive mixing strategy.
                                         limited range and operating conditions [6], [7], [8]. Laser scanners                We further empirically highlight the importance of high-capacity
                                         are expensive and can only provide sparse depth measurements                        encoders, and show the unreasonable effectiveness of pretraining
                                         when the scene is in motion. Stereo cameras are a promising                         the encoder on a large-scale auxiliary task.
                                         source of data [9], [10], but collecting suitable stereo images
                                         in diverse environments at scale remains a challenge. Structure-
                                         from-motion (SfM) reconstruction has been used to construct                             Our extensive experiments, which cover approximately six
                                         training data for monocular depth estimation across a variety                       GPU months of computation, show that a model trained on
                                         of scenes [11], but the result does not include independently                       a rich and diverse set of images from different sources, with
                                         moving objects and is incomplete due to the limitations of multi-                   an appropriate training procedure, delivers state-of-the-art results
                                         view matching. On the whole, none of the existing datasets is                       across a variety of environments. To demonstrate this, we use the
                                         sufficiently rich to support the training of a model that works                     experimental protocol of zero-shot cross-dataset transfer. That is,
                                         robustly on real images of diverse scenes. At present, we are faced                 we train a model on certain datasets and then test its performance
                                         with multiple datasets that may usefully complement each other,                     on other datasets that were never seen during training. The intu-
                                         but are individually biased and incomplete.                                         ition is that zero-shot cross-dataset performance is a more faithful
                                             In this paper, we investigate ways to train robust monocular                    proxy of “real world” performance than training and testing on
                                         depth estimation models that are expected to perform across                         subsets of a single data collection that largely exhibit the same
                                                                                                                             biases [13].

                                         •   R. Ranftl, D. Hafner, and V. Koltun are with the Intelligent Systems Lab,
                                             Intel Labs.
                                                                                                                                 In an evaluation across six different datasets, we outperform
                                         •   K. Lasinger and K. Schindler are with the Institute of Geodesy and              prior art both quantitatively and qualitatively, and set a new state
                                             Photogrammetry, ETH Zürich.                                                    of the art for monocular depth estimation. Example results are
                                         *Equal contribution                                                                 shown in Figure 1.
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                        2

Fig. 1. We show how to leverage training data from multiple, complementary sources for single-view depth estimation, in spite of varying and
unknown depth range and scale. Our approach enables strong generalization across datasets. Top: input images. Middle: inverse depth maps
predicted by the presented approach. Bottom: corresponding point clouds rendered from a novel view-point. Point clouds rendered via Open3D [4].
Input images from the Microsoft COCO dataset [5], which was not seen during training.

2   R ELATED W ORK                                                       [28], [29] or indoor environments [30]. We note in particular that
Early work on monocular depth estimation used MRF-based                  these datasets show only a small number of dynamic objects.
formulations [3], simple geometric assumptions [2], or non-              Models that are trained on data with such strong biases are prone
parametric methods [14]. More recently, significant advances have        to fail in less constrained environments.
been made by leveraging the expressive power of convolutional                 Efforts have been made to create more diverse datasets. Chen
networks to directly regress scene depth from the input image [15].      et al. [34] used crowd-sourcing to sparsely annotate ordinal rela-
Various architectural innovations have been proposed to enhance          tions in images collected from the web. Xian et al. [32] collected a
prediction accuracy [16], [17], [18], [19], [20]. These methods          stereo dataset from the web and used off-the-shelf tools to extract
need ground-truth depth for training, which is commonly acquired         dense ground-truth disparity; while this dataset is fairly diverse,
using RGB-D cameras or LiDAR sensors. Others leverage existing           it only contains 3,600 images. Li and Snavely [11] used SfM
stereo matching methods to obtain ground truth for supervi-              and multi-view stereo (MVS) to reconstruct many (predominantly
sion [21], [22]. These methods tend to work well in the specific         static) 3D scenes for supervision. Li et al. [38] used SfM and MVS
type of scenes used to train them, but do not generalize well to         to construct a dataset from videos of people imitating mannequins
unconstrained scenes, due to the limited scale and diversity of the      (i.e. they are frozen in action while the camera moves through the
training data.                                                           scene). Chen et al. [39] propose an approach to automatically
    Garg et al. [9] proposed to use calibrated stereo cameras for        assess the quality of sparse SfM reconstructions in order to
self-supervision. While this significantly simplifies the acquisition    construct a large dataset. Wang et al. [33] build a large dataset
of training data, it still does not lift the restriction to a very       from stereo videos sourced from the web, while Cho et al. [40]
specific data regime. Since then, various approaches leverage self-      collect a dataset of outdoor scenes with handheld stereo cameras.
supervision, but they either require stereo images [10], [23], [24]      Gordon et al. [41] estimate the intrinsic parameters of YouTube
or exploit apparent motion [24], [25], [26], [27], and are thus          videos in order to leverage them for training. Large-scale datasets
difficult to apply to dynamic scenes.                                    that were collected from the Internet [33], [38] require a large
    We argue that high-capacity deep models for monocular depth          amount of pre- and post-processing. Due to copyright restrictions,
estimation can in principle operate on a fairly wide and uncon-          they often only provide links to videos, which frequently become
strained range of scenes. What limits their performance is the lack      unavailable. This makes reproducing these datasets challenging.
of large-scale, dense ground truth that spans such a wide range of            To the best of our knowledge, the controlled mixing of mul-
conditions. Commonly used datasets feature homogeneous scene             tiple data sources has not been explored before in this context.
layouts, such as street scenes in a specific geographic region [3],      Ummenhofer et al. [42] presented a model for two-view structure
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                               3

                                                                     TABLE 1
 Datasets used in our work. Top: Our training sets. Bottom: Our test sets. No single real-world dataset features a large number of diverse scenes
                                                      with dense and accurate ground truth.

              Dataset            Indoor Outdoor Dynamic Video Dense Accuracy Diversity Annotation             Depth         # Images
              DIML Indoor [31]    3                        3       3      Medium   Medium     RGB-D          Metric          220K
              MegaDepth [11]              3       (3)             (3)     Medium   Medium      SfM          No scale         130K
              ReDWeb [32]         3       3        3               3      Medium    High      Stereo     No scale & shift    3600
              WSVD [33]           3       3        3       3       3      Medium    High      Stereo     No scale & shift    1.5M
              3D Movies           3       3        3       3       3      Medium    High      Stereo     No scale & shift     75K
              DIW [34]            3       3        3                       Low      High  User clicks      Ordinal pair      496K
              ETH3D [35]          3       3                        3       High     Low      Laser           Metric           454
              Sintel [36]         3       3        3       3       3       High    Medium Synthetic         (Metric)         1064
              KITTI [28], [29]            3       (3)      3      (3)     Medium    Low   Laser/Stereo       Metric           93K
              NYUDv2 [30]         3               (3)      3       3      Medium    Low     RGB-D            Metric          407K
              TUM-RGBD [37]       3               (3)      3       3      Medium    Low     RGB-D            Metric           80K

and motion estimation and trained it on a dataset of (static)              a collection of links to the stereo videos. No ground truth is
scenes that is the union of multiple smaller datasets. However,            provided. We thus recreate the ground truth according to the
they did not consider strategies for optimal mixing, or study the          procedure outlined by the original authors. DIML Indoor [31]
impact of combining multiple datasets. Similarly, Facil et al. [43]        (DL) is an RGB-D dataset of predominantly static indoor scenes,
used multiple datasets with a naive mixing strategy for learning           captured with a Kinect v2.
monocular depth with known camera intrinsics. Their test data is           Test datasets. To benchmark the generalization performance of
very similar to half of their training collection, namely RGB-D            monocular depth estimation models, we chose six datasets based
recordings of indoor scenes.                                               on diversity and accuracy of their ground truth. DIW [34] is highly
                                                                           diverse but provides ground truth only in the form of sparse
3    E XISTING DATASETS                                                    ordinal relations. ETH3D [35] features highly accurate laser-
                                                                           scanned ground truth on static scenes. Sintel [36] features perfect
Various datasets have been proposed that are suitable for monoc-           ground truth for synthetic scenes. KITTI [29] and NYU [30] are
ular depth estimation, i.e. they consist of RGB images with                commonly used datasets with characteristic biases. For the TUM
corresponding depth annotation of some form [3], [11], [28], [29],         dataset [37], we use the dynamic subset that features humans in
[30], [31], [32], [33], [34], [35], [36], [37], [38], [40], [44], [45],    indoor environments [38]. Note that we never fine-tune models on
[46], [47], [48]. Datasets differ in captured environments and             any of these datasets. We refer to this experimental procedure as
objects (indoor/outdoor scenes, dynamic objects), type of depth            zero-shot cross-dataset transfer.
annotation (sparse/dense, absolute/relative depth), accuracy (laser,
time-of-flight, SfM, stereo, human annotation, synthetic data),
image quality and camera settings, as well as dataset size.                4   3D M OVIES
    Each single dataset comes with its own characteristics and has         To complement the existing datasets we propose a new data
its own biases and problems [13]. High-accuracy data is hard to            source: 3D movies (MV). 3D movies feature high-quality video
acquire at scale and problematic for dynamic objects [35], [47],           frames in a variety of dynamic environments that range from
whereas large data collections from Internet sources come with             human-centric imagery in story- and dialogue-driven Hollywood
limited image quality and depth accuracy as well as unknown                films to nature scenes with landscapes and animals in documentary
camera parameters [33], [34]. Training on a single dataset leads           features. While the data does not provide metric depth, we can
to good performance on the corresponding test split of the same            use stereo matching to obtain relative depth (similar to RW and
dataset (same camera parameters, depth annotation, environment),           WS). Our driving motivation is the scale and diversity of the data.
but may have limited generalization capabilities to unseen data            3D movies provide the largest known source of stereo pairs that
with different characteristics. Instead, we propose to train on a          were captured in carefully controlled conditions. This offers the
collection of datasets, and demonstrate that this approach leads           possibility of tapping into millions of high-quality images from
to strongly enhanced generalization by testing on diverse datasets         an ever-growing library of content. We note that 3D movies have
that were not seen during training. We list our training and test          been used in related tasks in isolation [49], [50]. We will show
datasets, together with their individual characteristics, in Table 1.      that their full potential is unlocked by combining them with other,
Training datasets. We experiment with five existing and com-               complementary data sources. In contrast to similar data collections
plementary datasets for training. ReDWeb [32] (RW) is a small,             in the wild [32], [33], [38], no manual filtering of problematic
heavily curated dataset that features diverse and dynamic scenes           content was required with this data source. Hence, the dataset
with ground truth that was acquired with a relatively large                can easily be extended or adapted to specific needs (e.g. focus on
stereo baseline. MegaDepth [11] (MD) is much larger, but shows             dancing humans or nature documentaries).
predominantly static scenes. The ground truth is usually more              Challenges. Movie data comes with its own challenges and
accurate in background regions since wide-baseline multi-view              imperfections. The primary objective when producing stereoscopic
stereo reconstruction was used for acquisition. WSVD [33] (WS)             film is providing a visually pleasing viewing experience while
consists of stereo videos obtained from the web and features               avoiding discomfort for the viewer [51]. This means that the
diverse and dynamic scenes. This dataset is only available as              disparity range for any given scene (also known as the depth
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                      4

Fig. 2. Sample images from the 3D Movies dataset. We show images from some of the films in the training set together with their inverse depth
maps. Sky regions and invalid pixels are masked out. Each image is taken from a different film. 3D movies provide a massive source of diverse
data.

budget) is limited and depends on both artistic and psychophysical          We extract stereo image pairs at 1920x1080 resolution and
considerations. For example, disparity ranges are often increased       24 frames per second (fps). Movies have varying aspect ratios,
in the beginning and the end of a movie, in order to induce a very      resulting in black bars on the top and bottom of the frame, and
noticeable stereoscopic effect for a short time. Depth budgets in       some movies have thin black bars along frame boundaries due
the middle may be lower to allow for more comfortable viewing.          to post-production. We thus center-crop all frames to 1880x800
Stereographers thus adjust their depth budget depending on the          pixels. We use the chapter information (Blu-ray meta-data) to split
content, transitions, and even the rhythm of scenes [52].               each movie into individual chapters. We drop the first and last
    In consequence, focal lengths, baseline, and convergence angle      chapters since they usually include the introduction and credits.
between the cameras of the stereo rig are unknown and vary                  We use the scene detection tool of FFmpeg [53] with a
between scenes even within a single film. Furthermore, in contrast      threshold of 0.1 to extract individual clips. We discard clips that
to image pairs obtained directly from a standard stereo camera,         are shorter than one second to filter out chaotic action scenes and
stereo pairs in movies usually contain both positive and negative       highly correlated clips that rapidly switch between protagonists
disparities to allow objects to be perceived either in front of         during dialogues. To balance scene diversity, we sample the first
or behind the screen. Additionally, the depth that corresponds          24 frames of each clip and additionally sample 24 frames every
to the screen is scene-dependent and is often modified in post-         four seconds for longer clips. Since multiple frames are part of
production by shifting the image pairs. We describe data extraction     the same clip, the complete dataset is highly correlated. Hence,
and training procedures that address these challenges.                  we further subsample the training set at 4 fps and the test and
                                                                        validation sets at 1 fps.
Movie selection and preprocessing. We selected a diverse set
of 23 movies. The selection was based on the following con-             Disparity extraction. The extracted image pairs can be used
siderations: 1) We only selected movies that were shot using a          to estimate disparity maps using stereo matching. Unfortunately,
physical stereo camera. (Some 3D films are shot with a monocular        state-of-the-art stereo matchers perform poorly when applied to
camera and the stereoscopic effect is added in post-production by       movie data, since the matchers were designed and trained to match
artists.) 2) We tried to balance realism and diversity. 3) We only      only over positive disparity ranges. This assumption is appropriate
selected movies that are available in Blu-ray format and thus allow     for the rectified output of a standard stereo camera, but not to
extraction of high-resolution images.                                   image pairs extracted from stereoscopic film. Moreover, disparity
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                        5

                                  TABLE 2                               different forms (see Table 1). It may be in the form of absolute
    List of films and the number of extracted frames in the 3D Movies   depth (from laser-based measurements or stereo cameras with
                    dataset after automatic processing.
                                                                        known calibration), depth up to an unknown scale (from SfM), or
                                                                        disparity maps (from stereo cameras with unknown calibration).
         Movie title                                   # frames         The main requirement for a sensible training scheme is to carry
         Training set                                    75074          out computations in an appropriate output space that is compatible
         Battle of the Year (2013)                        4821          with all ground-truth representations and is numerically well-
         Billy Lynn’s Long Halftime Walk (2016)           4178
         Drive Angry (2011)                                328          behaved. We further need to design a loss function that is flexible
         Exodus: Gods and Kings (2014)                    8063          enough to handle diverse sources of data while making optimal
         Final Destination 5 (2011)                       1437          use of all available information.
         A very Harold & Kumar 3D Christmas (2011)        3690
         Hellbenders (2012)                                120
                                                                            We identify three major challenges. 1) Inherently different
         The Hobbit: An Unexpected Journey (2012)         8874          representations of depth: direct vs. inverse depth representations.
         Hugo (2011)                                      3189          2) Scale ambiguity: for some data sources, depth is only given up
         The Three Musketeers (2011)                      5028          to an unknown scale. 3) Shift ambiguity: some datasets provide
         Nurse 3D (2013)                                   492
         Pina (2011)                                      1215          disparity only up to an unknown scale and global disparity shift
         Dawn of the Planet of the Apes (2014)            5571          that is a function of the unknown baseline and a horizontal shift
         The Amazing Spider-Man (2012)                    5618          of the principal points due to post-processing [33].
         Step Up 3D (2010)                                 509
         Step Up: All In (2014)                           2187          Scale- and shift-invariant losses. We propose to perform pre-
         Transformers: Age of Extinction (2014)           8740          diction in disparity space (inverse depth up to scale and shift)
         Le Dernier Loup / Wolf Totem (2015)              4843          together with a family of scale- and shift-invariant dense losses
         X-Men: Days of Future Past (2014)                6171
                                                                        to handle the aforementioned ambiguities. Let M denote the
         Validation set                                   3058          number of pixels in an image with valid ground truth and let θ
         The Great Gatsby (2013)                          1815
         Step Up: Miami Heat / Revolution (2012)          1243          be the parameters of the prediction model. Let d = d(θ) ∈ RM
                                                                        be a disparity prediction and let d∗ ∈ RM be the corresponding
         Test set                                          788
         Doctor Who - The Day of the Doctor (2013)         508          ground-truth disparity. Individual pixels are indexed by subscripts.
         StreetDance 2 (2012)                              280              We define the scale- and shift-invariant loss for a single sample
                                                                        as
                                                                                                             M
                                                                                                        1 X                 
ranges encountered in 3D movies are usually smaller than ranges                      Lssi (d̂, d̂∗ ) =          ρ d̂i − d̂∗i ,            (1)
                                                                                                       2M i=1
that are common in standard stereo setups due to the limited depth
budget.
                                                                        where d̂ and d̂∗ are scaled and shifted versions of the predictions
    To alleviate these problems, we apply a modern optical flow
                                                                        and ground truth, and ρ defines the specific type of loss function.
algorithm [54] to the stereo pairs. We retain the horizontal compo-
                                                                            Let s : RM → R+ and t : RM → R denote estimators
nent of the flow as a proxy for disparity. Optical flow algorithms
                                                                        of the scale and translation. To define a meaningful scale- and
naturally handle both positive and negative disparities and usually
                                                                        shift-invariant loss, a sensible requirement is that prediction and
perform well for displacements of moderate size. For each stereo
                                                                        ground truth should be appropriately aligned with respect to their
pair we use the left camera as the reference and extract the optical
                                                                        scale and shift, i.e. we need to ensure that s(d̂) ≈ s(d̂∗ ) and
flow from the left to the right image and vice versa. We perform
a left-right consistency check and mark pixels with a disparity
                                                                        t(d̂) ≈ t(d̂∗ ). We propose two different strategies for performing
                                                                        this alignment.
difference of more than 2 pixels as invalid. We automatically filter
out frames of bad disparity quality following the guidelines of             The first approach aligns the prediction to the ground truth
Wang et al. [33]: frames are rejected if more than 10% of all pixels    based on a least-squares criterion:
have a vertical disparity >2 pixels, the horizontal disparity range                                       M
                                                                                                                                    2
                                                                                                          X
is <10 pixels, or the percentage of pixels passing the left-right                    (s, t) = arg min           (sdi + t − d∗i ) ,
                                                                                                   s,t
consistency check is <70%. In a final step, we detect pixels that                                         i=1
belong to sky regions using a pre-trained semantic segmentation                          d̂ = sd + t,        ∗
                                                                                                              d̂ = d∗ ,                     (2)
model [55] and set their disparity to the minimum disparity in the
image.                                                                  where d̂ and d̂∗ are the aligned prediction and ground truth,
    The complete list of selected movies together with the number       respectively. The factors s and t can be efficiently determined in
of frames that remain after filtering with the automatic cleaning       closed form by rewriting (2) as a standard least-squares problem:
pipeline is shown in Table 2. Note that discrepancies in the number     Let ~
                                                                            di = (di , 1)> and h = (s, t)> , then we can rewrite the
of extracted frames per movie occur due to varying runtimes as          objective as
well as varying disparity quality. We use frames from 19 movies
                                                                                                          M 
for training and set aside two movies for validation and two movies                                                     2
                                                                                                             ~d> h − d∗ ,
                                                                                                          X
for testing, respectively. Example frames from the resulting dataset                  hopt = arg min           i      i                     (3)
                                                                                                      h
                                                                                                          i=1
are shown in Figure 2.
                                                                        which has the closed-form solution
5    T RAINING ON D IVERSE DATA                                                                M
                                                                                                          !−1        M
                                                                                                                                    !
                                                                                                  ~di ~d                   ~di d∗
                                                                                               X                     X
                                                                                      opt               >
Training models for monocular depth estimation on diverse                           h =                   i                     i       .   (4)
datasets presents a challenge because the ground truth comes in                                 i=1                  i=1
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                             6

We set ρ(x) = ρmse (x) = x2 to define the scale- and shift-            difference between ground-truth and rescaled estimates at multiple
invariant mean-squared error (MSE). We denote this loss as             scales k :
Lssimse .                                                                                    K X
                                                                                             X M
    The MSE is not robust to the presence of outliers. Since all           Lnmg (d, d∗ ) =             |s∇kx d − ∇kx d∗ | + |s∇ky d − ∇ky d∗ |.
existing large-scale datasets only provide imperfect ground truth,                           k=1 i=1
we conjecture that a robust loss function can improve training.                                                                               (10)
We thus define alternative, robust loss functions based on robust      In contrast, our losses are evaluated directly on the ground-truth
estimators of scale and shift:                                         disparity values, while also accounting for unknown scale and
                                                M                      shift. While both the ordinal loss and NMG can, conceptually, be
                                           1 X
       t(d) = median(d),          s(d) =         |d − t(d)|.     (5)   applied to arbitrary depth representations and are thus suited for
                                           M i=1                       mixing diverse datasets, we will show that our scale- and shift-
We align both the prediction and the ground truth to have zero         invariant loss variants lead to consistently better performance.
translation and unit scale:                                            Final loss. To define the complete loss, we adapt the multi-
                                            ∗       ∗                  scale, scale-invariant gradient matching term [11] to the disparity
                     d − t(d)              d − t(d )
              d̂ =            ,    d̂∗ =             .           (6)   space. This term biases discontinuities to be sharp and to coincide
                       s(d)                  s(d∗ )                    with discontinuities in the ground truth. We define the gradient
We define two robust losses. The first, which we denote as             matching term as
Lssimae , measures the absolute deviations ρmae (x) = |x|. We                                       K M
define the second robust loss by trimming the 20% largest residu-                                1 XX
                                                                             Lreg (d̂, d̂∗ ) =             |∇x Rik | + |∇y Rik | ,
                                                                                                                                
                                                                                                                                              (11)
als in every image, irrespective of their magnitude:                                             M k=1 i=1
                                      U
                                  1 Xm                               where Ri = d̂i − d̂∗i , and Rk denotes the difference of disparity
         Lssitrim (d̂, d̂∗ ) =          ρmae d̂j − d̂∗j ,        (7)   maps at scale k . We use K = 4 scale levels, halving the image
                                 2M j=1
                                                                       resolution at each level. Note that this term is similar to Lnmg ,
with |d̂j −d̂∗j | ≤ |d̂j+1 −d̂∗j+1 | and Um = 0.8M (set empirically    but with different approaches to compute the scaling s.
based on experiments on the ReDWeb dataset). Note that this is             Our final loss for a training set l is
in contrast to commonly used M-estimators, where the influence                       N
                                                                                     l
                                                                                1 X
                                                                                       Lssi d̂n , (d̂∗ )n + α Lreg d̂n , (d̂∗ )n , (12)
                                                                                                                               
of large residuals is merely down-weighted. Our reasoning for              Ll =
trimming is that outliers in the ground truth should never influence            Nl n=1
training.                                                              where Nl is the training set size and α is set to 0.5.
Related loss functions. The importance of accounting for un-           Mixing strategies. While our loss and choice of prediction
known or varying scale in the training of monocular depth estima-      space enable mixing datasets, it is not immediately clear in what
tion models has been recognized early. Eigen et al. [15] proposed      proportions different datasets should be integrated during training
a scale-invariant loss in log-depth space. Their loss can be written   with a stochastic optimization algorithm. We explore two different
as                                                                     strategies in our experiments.
                                  M                                        The first, naive strategy is to mix datasets in equal parts in each
                            1 X                          2
 Lsilog (z, z∗ ) = min            log(es zi ) − log(z∗i ) , (8)        minibatch. For a minibatch of size B , we sample B/L training
                       s   2M i=1                                      samples from each dataset, where L denotes the number of distinct
                                                                       datasets. This strategy ensures that all datasets are represented
where zi = d−1  i   and z∗i = (d∗i )−1 are depths up to unknown
                                                                       equally in the effective training set, regardless of their individual
scale. Both (8) and Lssimse account for the unknown scale of the
                                                                       size.
predictions, but only Lssimse accounts for an unknown global               Our second strategy explores a more principled approach,
disparity shift. Moreover, the losses are evaluated on different       where we adapt a recent procedure for Pareto-optimal multi-task
depth representations. Our loss is defined in disparity space, which   learning to our setting [12]. We define learning on each dataset
is numerically stable and compatible with common representations       as a separate task and seek an approximate Pareto optimum over
of relative depth.                                                     datasets (i.e. a solution where the loss cannot be decreased on any
    Chen et al. [34] proposed a generally applicable loss for          training set without increasing it for at least one of the others).
relative depth estimation based on ordinal relations:                  Formally, we use the algorithm presented in [12] to minimize the
                     (
                      log(1 + exp(−(zi − zj )lij ), lij 6= 0           multi-objective optimization criterion
  ρord (zi − zj ) =                                              (9)                                                  >
                      (zi − zj )2 ,                     lij = 0,                            min L1 (θ), . . . , LL (θ) ,                  (13)
                                                                                             θ
where lij ∈ {−1, 0, 1} encodes the ground-truth ordinal relation of    where model parameters θ are shared across datasets.
point pairs. This encourages pushing points as far apart as possible
when lij 6= 0 and pulling them to the same depth when lij = 0.
Xian et al. [32] suggest to sparsely evaluate this loss by randomly    6    E XPERIMENTS
sampling point pairs from the dense ground truth. In contrast, our     We start from the experimental setup of Xian et al. [32] and
proposed losses take all available data into account.                  use their ResNet-based [56] multi-scale architecture for single-
    Recently, Wang et al. [33] proposed the normalized multiscale      image depth prediction. We initialize the encoder with pretrained
gradient (NMG) loss. To achieve shift invariance in addition to        ImageNet [57] weights and initialize other layers randomly. We
scale invariance in disparity space, they evaluate the gradient        use Adam [58] with a learning rate of 10−4 for randomly
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                                                                                                  7

Relative Performance [%]

                                                                                                           Relative Performance [%]
                            0                                                                                                          15          RW
                                                                                                                                                   MD
                                                                                                                                       10          MV
                           5                                                                        RW                                             mean
                                                                                                    MD                                  5
                                                                                                    MV
                                                                                                    mean
                           10                                                                                                           0
                                                                                                                                            t-50             1                  1                 1                L
                                ord     re g   nmg          re g         re g         re g          re g                                  Ne            et-10              et-16             t-10              -WS
                                      +                 +            +            +             +                                     Res           esN                seN              Ne X
                                                                                                                                                                                                        t-1 01
                                 silo
                                     g
                                                sim
                                                      se
                                                            ssim
                                                                   se
                                                                         ssim
                                                                                ae
                                                                                      ssit
                                                                                             rim                                                   R             Den                Res           s NeX
                                                                                                                                                                                               R e

Fig. 3. Relative performance of different loss functions (higher is better)                                Fig. 4. Relative performance of different encoders across datasets
with the best performing loss Lssitrim + Lreg used as reference. All                                       (higher is better). ImageNet performance of an encoder is predictive of
our four proposed losses (white area) outperform current state-of-the-                                     its performance in monocular depth estimation.
art losses (gray area).

                                                                                                           maximum value for datasets that are evaluated in depth space. For
initialized layers and 10−5 for pretrained layers, and set the                                             ETH3D, KITTI, NYU, and TUM, the depth cap was set to the
exponential decay rate to β1 = 0.9 and β2 = 0.999. Images are                                              maximum ground-truth depth value (72, 80, 10, and 10 meters,
flipped horizontally with a 50% chance, and randomly cropped                                               respectively). For Sintel, we evaluate on areas with ground-truth
and resized to 384 × 384 to augment the data and maintain the                                              depth below 72 meters and accordingly use a depth cap of 72
aspect ratio across different input images. No other augmentations                                         meters. For all our models and baselines, we align predictions and
are used.                                                                                                  ground truth in scale and shift for each image before measuring
     Subsequently, we perform ablation studies on the loss function                                        errors. We perform the alignment in inverse-depth space based
and, since we conjecture that pretraining on ImageNet data has sig-                                        on the least-squares criterion. Since absolute numbers quickly
nificant influence on performance, also the encoder architecture.                                          become hard to interpret when evaluating on multiple datasets,
We use the best-performing pretrained model as the starting point                                          we also present the relative change in performance compared to
for our dataset mixing experiments. We use a batch size of 8L, i.e.                                        an appropriate baseline method.
when mixing three datasets the batch size is 24. When comparing                                            Input resolution for evaluation. We resize test images so that the
datasets of different sizes, the term epoch is not well-defined; we                                        larger axis equals 384 pixels while the smaller axis is resized to a
thus denote an epoch as processing 72,000 images, roughly the                                              multiple of 32 pixels (a constraint imposed by the encoder), while
size of MD and MV, and train for 60 epochs. We shift and scale                                             keeping an aspect ratio as close as possible to the original aspect
the ground-truth disparity to the range [0, 1] for all datasets.                                           ratio. Due to the wide aspect ratio in KITTI this strategy would
Test datasets and metrics. For ablation studies of loss and                                                lead to very small input images. We thus resize the smaller axis to
encoders, we use our held-out validation sets of RW (360 images),                                          be equal to 384 pixels on this dataset and adopt the same strategy
MD (2,963 images – official validation set), and MV (3,058                                                 otherwise to maintain the aspect ratio.
images – see Table 2). For all training dataset mixing experiments                                             Most state-of-the-art methods that we compare to are special-
and comparisons to the state of the art, we test on a collection                                           ized to a specific dataset (with fixed image dimensions) and thus
of datasets that were never seen during training: DIW, ETH3D,                                              did not specify how to handle different image sizes and aspect
Sintel, KITTI, NYU, and TUM. For DIW [34] we created a                                                     ratios during inference. We tried to find the best-performing setting
validation set of 10,000 images from the DIW training set for                                              for all methods, following their evaluation scripts and training
our ablation studies and used the official test set of 74,441 images                                       dimensions. For approaches trained on square patches [32], we
when comparing to the state of the art. For NYU we used the                                                follow our setup and set the larger axis to the training image
official test split (654 images). For KITTI we used the intersection                                       axis length and adapt the smaller one, keeping the aspect ratio
of the official validation set for depth estimation (with improved                                         as close as possible to the original. For approaches with non-
ground-truth depth [59]) and the Eigen test split [60] (161 images).                                       square patches [11], [33], [34], [38] we fix the smaller axis to
For ETH3D and Sintel we used the whole dataset for which ground                                            the smaller training image axis dimension. For DORN [19] we
truth is available (454 and 1,064 images, respectively). For the                                           followed their tiling protocol, resizing the images to the dimen-
TUM dataset, we use the dynamic subset that features humans in                                             sions stated for their NYU and KITTI evaluation, respectively.
indoor environments [38] (1,815 images).                                                                   For Monodepth2 [24] and Struct2Depth [27], which were both
    For each dataset, we use a single metric that fits the ground                                          trained on KITTI and thus expect a very wide aspect ratio, we
truth in that dataset. For DIW we use the Weighted Human                                                   pad the input image using reflection padding to obtain the same
Disagreement Rate (WHDR) [34]. For datasets that are based                                                 aspect ratio, resize to their specific input dimension, and crop
on relative depth, we measure the root mean squared error in                                               the resulting prediction to the original target dimensions. For
disparity space (MV, RW, MD). For datasets that provide accurate                                           methods where model weights were available for different training
absolute depth (ETH3D, Sintel), wePmeasure the mean absolute                                               resolutions we evaluated all of them and report numbers for the
                                          M
value of the relative error (1/M ) i=1 |zi − zi∗ | /zi∗ in depth                                           best-performing variant.
space (AbsRel).∗ Finally, we use the percentage of pixels with                                                 All predictions were rescaled to the resolution of the ground
                 z                                                                                         truth for evaluation.
δ = max( zz∗i , zii ) > 1.25 to evaluate models on KITTI, NYU, and
              i
TUM [15]. Following [10], we cap predictions at an appropriate                                             Comparison of loss functions. We show the effect of different
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                                               8

loss functions on the validation performance in Figure 3. We used                                            TABLE 5
RW to train networks with different losses. For the ordinal loss (cf.                        Combinations of datasets used for training.
Equation (9)), we sample 5,000 point pairs randomly [32]. Where
appropriate, we combine losses with the gradient regularization                                      Mix    RW DL MV MD WS
term (11). We also test a scale-invariant, but not shift-invariant,                                 MIX 1      3         3
MSE in disparity space Lsimse by fixing t = 0 in (1). The model                                     MIX 2      3         3    3
trained with Lord corresponds to our reimplementation of Xian                                       MIX 3      3         3    3      3
                                                                                                    MIX 4      3         3           3       3
et al. [32]. Figure 3 shows that our proposed trimmed MAE loss                                      MIX 5      3         3    3      3       3
yields the lowest validation error over all datasets. We thus conduct
all experiments that follow using Lssitrim + Lreg .
Comparison of encoders. We evaluate the influence of the                        Training on diverse datasets. We evaluate the usefulness of
encoder architecture in Figure 4. We define the model with a                    different training datasets for generalization in Table 3 and Table 4.
ResNet-50 [56] encoder as used originally by Xian et al. [32]                   While more specialized datasets reach better performance on
as our baseline and show the relative improvement in perfor-                    similar test sets (DL for indoor scenes or MD for ETH3D),
mance when swapping in different encoders (higher is better). We                performance on the remaining datasets declines. Interestingly,
tested ResNet-101, ResNeXt-101 [61] and DenseNet-161 [62]. All                  every single dataset used in isolation leads to worse generalization
encoders were pretrained on ImageNet [57]. For ResNeXt-101,                     performance on average than just using the small, but curated, RW
we additionally use a variant that was pretrained with a massive                dataset, i.e. the gains on compatible datasets are offset on average
corpus of weakly-supervised data (WSL) [63] before training on                  by the decrease on the other datasets.
ImageNet. All models were fine-tuned on RW.                                         The difference in performance for RW, MV, and WS is espe-
    We observe that a significant performance boost is achieved                 cially interesting since they have similar characteristics. Although
by using better encoders. Higher-capacity encoders perform better               substantially larger than RW, both MV and WS show worse indi-
than the baseline. The ResNeXt-101 encoder that was pretrained                  vidual performance. This could be explained partly by redundant
on weakly-supervised data performs significantly better than the                data due to the video nature of these datasets and possibly more
same encoder that was only trained on ImageNet. We found                        rigorous filtering in RW (human experts pruned samples that had
pretraining to be crucial. A network with a ResNet-50 encoder                   obvious flaws). Comparing WS and MV, we see that MV leads to
with random initialization performs on average 35% worse than                   more general models, likely because of higher-quality stereo pairs
its pretrained counterpart. In general, we find that ImageNet                   due to the more controlled nature of the images.
performance of an encoder is a strong predictor for its perfor-                     For our subsequent mixing experiments, we use Table 3 as
mance in monocular depth estimation. This is encouraging, since                 reference, i.e. we start with the best performing individual training
advancements made in image classification can directly yield gains              dataset and consecutively add datasets to the mix. We show which
in robust monocular depth estimation. The performance gain over                 datasets are included in the individual training sets in Table 5.
the baseline is remarkable: up to 15 % relative improvement,                    To better understand the influence of the Movies dataset, we
without any task-specific adaptations. We use ResNeXt-101-WSL                   additionally show results where we train on all datasets except
for all subsequent experiments.                                                 Movies (MIX 4). We always start training from the pretrained RW

                                  TABLE 3
                                                                                                               TABLE 6
   Relative performance with respect to the baseline in percent when
                                                                                 Relative performance of naive dataset mixing with respect to the RW
      fine-tuning on different single training sets (higher is better).
                                                                                     baseline (top row) – higher is better. While we usually see an
 Performance better than the baseline in green, worse performance in
                                                                                    improvement when adding datasets, adding datasets can hurt
red. Best performance is bold, second best is underlined. The absolute
                                                                                            generalization performance with naive mixing.
   errors of the RW baseline are shown on the top row. While some
  datasets provide better performance on individual, similar datasets,
  average performance for zero-shot cross-dataset transfer degrades.                      DIW       ETH3D      Sintel        KITTI       NYU       TUM    Mean [%]
                                                                                 RW        14.6       0.2          0.3        28.0       18.7      21.7      —
            DIW      ETH3D      Sintel   KITTI      NYU      TUM     Mean [%]
                                                                                 MIX 1     10.9       9.9       −3.7          18.0       41.4      33.0      18.3
RW → RW      14.6       0.2       0.3        28.0    18.7     21.7      —        MIX 2      6.7       8.6        3.2           9.2       40.8      35.7      17.3
RW → DL     −37.6       2.0      −4.3    −73.0       32.3     19.4    −10.2      MIX 3     13.5      10.6        4.9          13.9       43.8      29.1      19.3
RW → MV     −26.1     −15.9     −15.5     10.1      −10.2     −3.5    −10.2      MIX 4     11.7      11.3        5.2          11.3       38.8      35.5      19.0
RW → MD     −31.5       4.0      −9.7    −24.3       −1.7    −52.0    −19.2      MIX 5     12.3      12.6        7.2           9.1       38.5      37.2      19.5
RW → WS     −32.4     −29.8      −2.9    −34.5      −31.9      3.2    −21.4
                                                                                                              TABLE 7
                                TABLE 4                                          Absolute performance of naive dataset mixing – lower is better. This
Absolute performance when fine-tuning on different single training sets                            table corresponds to Table 6.
         – lower is better. This table corresponds to Table 3.
                                                                                            DIW       ETH3D         Sintel         KITTI          NYU      TUM
              DIW     ETH3D        Sintel       KITTI        NYU      TUM                  WHDR       AbsRel        AbsRel        δ>1.25         δ>1.25   δ>1.25
             WHDR     AbsRel       AbsRel      δ>1.25       δ>1.25   δ>1.25       RW        14.59      0.151         0.349           27.95       18.74    21.69
RW → RW      14.59      0.151        0.349      27.95       18.74    21.69        MIX 1     13.00      0.136         0.362           22.91       10.98    14.53
RW → DL      20.08      0.148        0.364      48.35       12.68    17.48        MIX 2     13.62      0.138         0.338           25.39       11.10    13.94
RW → MV      18.39      0.175        0.403      25.12       20.65    22.44        MIX 3     12.62      0.135         0.332           24.06       10.54    15.39
RW → MD      19.18      0.145        0.383      34.73       19.05    32.96        MIX 4     12.88      0.134         0.331           24.78       11.46    14.00
RW → WS      19.31      0.196        0.359      37.59       24.72    20.99        MIX 5     12.79      0.132         0.324           25.41       11.52    13.62
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                                 9

           Input                     MIX 1                          MIX 2                 MIX 3                  MIX 4                  MIX 5

Fig. 5. Comparison of models trained on different combinations of datasets using Pareto-optimal mixing. Images from Microsoft COCO [5].

                                TABLE 8                                              (i.e. zero-shot transfer, akin to our model). The bottom parts show
       Relative performance of dataset mixing with multi-objective                   baselines that were fine-tuned on a subset of the datasets for
   optimization with respect to the RW baseline (top row) – higher is
better. Principled mixing dominates the solutions found by naive mixing.             reference. In the training set column, MC refers to Mannequin
                                                                                     Challenge [38] and CS to Cityscapes [45]. A → B indicates
                                                                                     pretraining on A and fine-tuning on B.
            DIW       ETH3D      Sintel   KITTI         NYU       TUM     Mean [%]
                                                                                          Our model outperforms the baselines by a comfortable margin
 RW          14.6       0.2        0.3        28.0       18.7      21.7      —       in terms of zero-shot performance. Note that our model outper-
 MIX 1        9.4       7.3       −7.7        13.2       44.1      33.2      16.6    forms the Mannequin Challenge model of Li et al. [38] on a
 MIX 2       14.1       8.6        0.9        17.5       45.5      32.0      19.8
                                                                                     subset of the TUM dataset that was specifically curated by Li et
 MIX 3       15.8      11.9        5.2        11.7       47.8      32.4      20.8
 MIX 4       15.4      13.9        1.7        17.2       43.4      38.2      21.6    al. to showcase the advantages of their model. We show additional
 MIX 5       15.9      14.6        6.3        14.5       49.0      34.1      22.4    results on a variant of our model that has a smaller encoder based
                                                                                     on ResNet-50 (Ours – small). This architecture is equivalent to
                                TABLE 9                                              the network proposed by Xian et al. [32]. The smaller model also
     Absolute performance of dataset mixing with multi-objective
   optimization – lower is better. This table corresponds to Table 8.
                                                                                     outperforms the state of the art by a comfortable margin. This
                                                                                     shows that the strong performance of our model is not only due to
                                                                                     increased network capacity, but fundamentally due to the proposed
              DIW       ETH3D       Sintel        KITTI          NYU       TUM
             WHDR       AbsRel      AbsRel       δ>1.25         δ>1.25    δ>1.25     training scheme.
                                                                                          Some models that were trained for one specific dataset (e.g.
   RW         14.59      0.151        0.349          27.95      18.74     21.69
   MIX 1      13.22      0.140        0.376          24.26      10.48     14.50      KITTI or NYU in the lower part of the table) perform very well
   MIX 2      12.54      0.138        0.346          23.05      10.21     14.76      on those individual datasets but perform significantly worse on all
   MIX 3      12.29      0.133        0.331          24.68       9.78     14.66      other test sets. Fine-tuning on individual datasets leads to strong
   MIX 4      12.35      0.130        0.343          23.13      10.61     13.41
   MIX 5      12.27      0.129        0.327          23.90       9.55     14.29
                                                                                     priors about specific environments. This can be desirable in some
                                                                                     applications, but is ill-suited if the model needs to generalize. A
                                                                                     qualitative comparison of our model to the four best-performing
                                                                                     competitors is shown in Figure 6.
baseline.
                                                                                     Additional qualitative results. Figure 7 shows additional qual-
    Tables 6 and 7 show that, in contrast to using individual                        itative results on the DIW test set [34]. We show results on a
datasets, mixing multiple training sets consistently improves per-                   diverse set of input images depicting various objects and scenes,
formance with respect to the baseline. However, we also see that                     including humans, mammals, birds, cars, and other man-made
adding datasets does not unconditionally improve performance                         and natural objects. The images feature indoor, street and nature
when naive mixing is used (see MIX 1 vs. MIX 2). Tables 8                            scenes, various lighting conditions, and various camera angles.
and 9 report the results of an analogous experiment with Pareto-                     Additionally, subject areas vary from close-up to long-range shots.
optimal dataset mixing. We observe that this approach improves                            We show qualitative results on the DAVIS video dataset [64] in
over the naive mixing strategy. It is also more consistently able                    our supplementary video https://youtu.be/D46FzVyL9I8.
to leverage additional datasets. Combining all five datasets with                    Note that every frame was processed individually, i.e. no temporal
Pareto-optimal mixing yields our best-performing model. We                           information was used in any way. For each clip, the inverse depth
show a qualitative comparison of the resulting models in Figure 5.                   maps were jointly scaled and shifted for visualization. The dataset
Comparison to the state of the art. We compare our best-                             consists of a diverse set of videos and includes humans, animals,
performing model to various state-of-the-art approaches in Ta-                       and cars in action. This dataset was filmed with monocular
ble 10 and Table 11. The top part of each table compares to                          cameras, hence no ground-truth depth information is available.
baselines that were not fine-tuned on any of the evaluated datasets                       Hertzmann [65] recently observed that our publicly available
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                     10

Input
Xian et al. [32]
Wang et al. [33]
Li et al. [38]
Li & Snavely [11]
 Ours

Fig. 6. Qualitative comparison of our approach to the four best competitors on images from the Microsoft COCO dataset [5].

model provides plausible results even on abstract line drawings.         pellets at approximately the same distance to the camera are
Similarly, we show results on drawings and paintings with differ-        reconstructed closer to the camera in the lower part of the image.
ent levels of abstraction in Figure 8. We can qualitatively confirm      Such cases could be prevented by augmenting training data with
the findings in [65]: The model shows a surprising capability to         rotated images. However, it is not clear if invariance to image
estimate plausible relative depth even on relatively abstract inputs.    rotations is a desired property for this task.
This seems to be true as long as some (coarse) depth cues such as            Another interesting failure case is shown in the second row of
shading or vanishing points are present in the artwork.                  Figure 9. Paintings, photos, and mirrors are often not recognized
Failure cases. We identify common failure cases and biases of            as such. The network estimates depth based on the content that
our model. Images have a natural bias where the lower parts of           is depicted on the reflector rather than predicting the depth of the
the image are closer to the camera than the higher image regions.        reflector itself.
When randomly sampling two points and classifying the lower                  Additional failure cases are shown in the remaining rows.
point as closer to the camera, [34] achieved an agreement rate of        Strong edges can lead to hallucinated depth discontinuities. Thin
85.8% with human annotators. This bias has also been learned             structures can be missed and relative depth arrangement between
by our network and can be observed in some extreme cases that            disconnected objects might fail in some situations. Results tend to
are shown in the first row of Figure 9. In the example on the            get blurred in background regions, which might be explained by
left, the model fails to recover the ground plane, likely because        the limited resolution of the input images and imperfect ground
the input image was rotated by 90 degrees. In the right image,           truth in the far range.
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020   11

Fig. 7. Qualitative results on the DIW test set.
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                          12

Fig. 8. Results on paintings and drawings. Top row: A Friend in Need, Cassius Marcellus Coolidge, and Bathers at Asniéres, Georges Pierre Seurat.
Bottom row: Mittagsrast, Vincent van Gogh, and Vector drawing of central street of old european town, Vilnius, @Misha

Fig. 9. Failure cases. Subtle failures in relative depth arrangement or missing details are highlighted in green.
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                                                    13

7       C ONCLUSION                                                                           R EFERENCES
                                                                                              [1]  B. Zhou, P. Krähenbühl, and V. Koltun, “Does computer vision matter
                                                                                                   for action?” Science Robotics, vol. 4, no. 30, 2019.
The success of deep networks has been driven by massive datasets.                             [2] D. Hoiem, A. A. Efros, and M. Hebert, “Automatic photo pop-up,” ACM
                                                                                                   Transactions on Graphics, vol. 24, no. 3, 2005.
For monocular depth estimation, we believe that existing datasets                             [3] A. Saxena, M. Sun, and A. Y. Ng, “Make3D: Learning 3D scene structure
are still insufficient and likely constitute the limiting factor.                                  from a single still image,” PAMI, vol. 31, no. 5, 2009.
Motivated by the difficulty of capturing diverse depth datasets                               [4] Q.-Y. Zhou, J. Park, and V. Koltun, “Open3D: A modern library for 3D
at scale, we have introduced tools for combining complementary                                     data processing,” arXiv:1801.09847, 2018.
                                                                                              [5] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan,
sources of data. We have proposed a flexible loss function and a                                   P. Dollár, and C. L. Zitnick, “Microsoft COCO: Common objects in
principled dataset mixing strategy. We have further introduced a                                   context,” in ECCV, 2014.
dataset based on 3D movies that provides dense ground truth for                               [6] K. Khoshelham and S. O. Elberink, “Accuracy and resolution of Kinect
                                                                                                   depth data for indoor mapping applications,” Sensors, vol. 12, no. 2,
diverse dynamic scenes.                                                                            2012.
    We have evaluated the robustness and generality of models via                             [7] M. Hansard, S. Lee, O. Choi, and R. Horaud, Time-of-Flight Cameras:
                                                                                                   Principles, Methods and Applications. Springer, 2013.
zero-shot cross-dataset transfer. We find that systematically testing
                                                                                              [8] P. Fankhauser, M. Blösch, D. Rodriguez, R. Kaestner, M. Hutter, and
models on datasets that were never seen during training is a better                                R. Siegwart, “Kinect v2 for mobile robot navigation: Evaluation and
proxy for their performance “in the wild” than testing on a held-                                  modeling,” in International Conference on Advanced Robotics, 2015.
out portion of even the most diverse datasets that are currently                              [9] R. Garg, B. V. Kumar, G. Carneiro, and I. Reid, “Unsupervised CNN for
                                                                                                   single view depth estimation: Geometry to the rescue,” in ECCV, 2016.
available.                                                                                    [10] C. Godard, O. Mac Aodha, and G. J. Brostow, “Unsupervised monocular
    Our work advances the state of the art in generic monoc-                                       depth estimation with left-right consistency,” in CVPR, 2017.
                                                                                              [11] Z. Li and N. Snavely, “MegaDepth: Learning single-view depth predic-
ular depth estimation and indicates that the presented ideas                                       tion from Internet photos,” in CVPR, 2018.
substantially improve performance across diverse environments.                                [12] O. Sener and V. Koltun, “Multi-task learning as multi-objective optimiza-
We hope that this work will contribute to the deployment                                           tion,” in NeurIPS, 2018.
of monocular depth models that meet the requirements of                                       [13] A. Torralba and A. A. Efros, “Unbiased look at dataset bias,” in CVPR,
                                                                                                   2011.
practical applications. Our models are freely available at                                    [14] K. Karsch, C. Liu, and S. B. Kang, “Depth transfer: Depth extraction
https://github.com/intel-isl/MiDaS.                                                                from video using non-parametric sampling,” PAMI, vol. 36, no. 11, 2014.
                                                                                              [15] D. Eigen, C. Puhrsch, and R. Fergus, “Depth map prediction from a
                                                                                                   single image using a multi-scale deep network,” in NIPS, 2014.
                                                                                              [16] I. Laina, C. Rupprecht, V. Belagiannis, F. Tombari, and N. Navab,
                                                                                                   “Deeper depth prediction with fully convolutional residual networks,”
                                                                                                   in 3DV, 2016.
                              TABLE 10                                                        [17] A. Roy and S. Todorovic, “Monocular depth estimation using neural
  Relative performance of state of the art methods with respect to our                             regression forest,” in CVPR, 2016.
   best model (top row) – higher is better. Top: models that were not                         [18] F. Liu, C. Shen, and G. Lin, “Deep convolutional neural fields for depth
fine-tuned on any of the datasets. Bottom: models that were fine-tuned                             estimation from a single image,” in CVPR, 2015.
                  on a subset of the tested datasets.                                         [19] H. Fu, M. Gong, C. Wang, K. Batmanghelich, and D. Tao, “Deep ordinal
                                                                                                   regression network for monocular depth estimation,” in CVPR, 2018.
                Training sets     DIW ETH3D Sintel KITTI            NYU      TUM Mean [%]     [20] R. Li, K. Xian, C. Shen, Z. Cao, H. Lu, and L. Hang, “Deep attention-
                                                                                                   based classification network for robust depth prediction,” in ACCV, 2018.
 Ours             MIX 5          12.46     0.129 0.327     23.90    9.55     14.29     —
                                                                                              [21] X. Guo, H. Li, S. Yi, J. Ren, and X. Wang, “Learning monocular depth
 Ours – small     MIX 5            -0.2    -20.2    -0.9    8.7 -64.7 -19.0           −16.0        by distilling cross-domain stereo networks,” in ECCV, 2018.
 Xian [32]         RW             -17.1    -44.2   -29.1 -42.6 -182.7 -75.1           −65.1   [22] Y. Luo, J. Ren, M. Lin, J. Pang, W. Sun, H. Li, and L. Lin, “Single view
 Li [38]           MC            -112.8    -41.9   -23.9 -100.6 -94.5 -23.9           −66.2        stereo matching,” in CVPR, 2018.
 Wang [33]         WS             -53.2    -58.9   -19.3 -33.6 -209.6 -41.2           −69.3
                                                                                              [23] H. Zhan, R. Garg, C. S. Weerasekera, K. Li, H. Agarwal, and I. D.
 Li [11]           MD             -85.8    -41.1   -17.7 -51.8 -188.2 -106.7          −81.9
 Casser [27]       CS            -163.2    -82.2   -29.1   11.5 -314.5 -160.2        −122.9        Reid, “Unsupervised learning of monocular depth estimation and visual
                                                                                                   odometry with deep feature reconstruction,” in CVPR, 2018.
 Fu [19]     NYU                 -131.1    -51.2   -32.4 -157.8    9.0 -72.5          −72.6   [24] C. Godard, O. Mac Aodha, M. Firman, and G. J. Brostow, “Digging into
 Chen [34] NYUDIW                -16.1    -71.3   -34.6 -51.9 -196.6 -111.1          −80.3        self-supervised monocular depth prediction,” in ICCV, 2019.
 Godard [24] KITTI               -138.1    -46.5   -24.2   76.9 -248.6 -152.1         −88.8
                                                                                              [25] T. Zhou, M. Brown, N. Snavely, and D. G. Lowe, “Unsupervised learning
 Casser [27] KITTI               -168.8    -68.2   -25.1   50.1 -277.8 -159.1        −108.2
 Fu [19]     KITTI               -143.9    -67.4   -32.1   70.2 -325.2 -180.8        −113.2        of depth and ego-motion from video,” in CVPR, 2017.
                                                                                              [26] R. Mahjourian, M. Wicke, and A. Angelova, “Unsupervised learning
                                                                                                   of depth and ego-motion from monocular video using 3D geometric
                              TABLE 11                                                             constraints,” in CVPR, 2018.
 Absolute performance of state of the art methods, sorted by average                          [27] V. Casser, S. Pirk, R. Mahjourian, and A. Angelova, “Unsupervised
              rank. This table corresponds to Table 10.                                            learning of depth and ego-motion: A structured approach,” in AAAI, 2019.
                                                                                              [28] A. Geiger, P. Lenz, and R. Urtasun, “Are we ready for autonomous
                                                                                                   driving? The KITTI vision benchmark suite,” in CVPR, 2012.
                 Training sets     DIW ETH3D Sintel KITTI NYU TUM Rank                        [29] M. Menze and A. Geiger, “Object scene flow for autonomous vehicles,”
                                  WHDR AbsRel AbsRel δ>1.25 δ>1.25 δ>1.25
                                                                                                   in CVPR, 2015.
 Ours              MIX 5           12.46   0.129   0.327    23.90     9.55     14.29    2.0   [30] N. Silberman, D. Hoiem, P. Kohli, and R. Fergus, “Indoor segmentation
 Ours – small      MIX 5           12.48   0.155   0.330    21.81    15.73     17.00    2.7        and support inference from RGBD images,” in ECCV, 2012.
 Li [11]            MD             23.15   0.181   0.385    36.29    27.52     29.54    5.7   [31] Y. Kim, H. Jung, D. Min, and K. Sohn, “Deep monocular depth estima-
 Li [38]            MC             26.52   0.183   0.405    47.94    18.57     17.71    5.7        tion via integration of global and local predictions,” IEEE Transactions
 Wang [33]          WS             19.09   0.205   0.390    31.92    29.57     20.18    6.0
                                                                                                   on Image Processing, vol. 27, no. 8, 2018.
 Xian [32]          RW             14.59   0.186   0.422    34.08    27.00     25.02    6.1
 Casser [27]        CS             32.80   0.235   0.422    21.15    39.58     37.18    9.6
                                                                                              [32] K. Xian, C. Shen, Z. Cao, H. Lu, Y. Xiao, R. Li, and Z. Luo, “Monocular
                                                                                                   relative depth perception with web stereo data supervision,” in CVPR,
 Godard [24] KITTI                 29.67   0.189   0.406     5.53    33.29     36.03    6.7        2018.
 Fu [19]     NYU                   28.79   0.195   0.433    61.61     8.69     24.65    7.3   [33] C. Wang, O. Wang, F. Perazzi, and S. Lucey, “Web stereo video
 Chen [34] NYU  DIW               14.47   0.221   0.440    36.30    28.33     30.16    8.5        supervision for depth prediction from dynamic scenes,” in 3DV, 2019.
 Casser [27] KITTI                 33.49   0.217   0.409    11.93    36.08     37.03    8.7
                                                                                              [34] W. Chen, Z. Fu, D. Yang, and J. Deng, “Single-image depth perception
 Fu [19]     KITTI                 30.39   0.216   0.432     7.13    40.61     40.13    9.2
                                                                                                   in the wild,” in NIPS, 2016.
IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. XX, NO. XX, 2020                                                                     14

[35] T. Schöps, J. L. Schönberger, S. Galliani, T. Sattler, K. Schindler,                                René Ranftl is a Senior Research Scientist at
     M. Pollefeys, and A. Geiger, “A multi-view stereo benchmark with high-                                the Intelligent Systems Lab at Intel in Munich,
     resolution images and multi-camera videos,” in CVPR, 2017.                                            Germany. He received an M.Sc. degree and a
[36] D. J. Butler, J. Wulff, G. B. Stanley, and M. J. Black, “A naturalistic open                          Ph.D. degree from Graz University of Technol-
     source movie for optical flow evaluation,” in ECCV, 2012.                                             ogy, Austria, in 2010 and 2015, respectively. His
[37] J. Sturm, N. Engelhard, F. Endres, W. Burgard, and D. Cremers, “A                                     research interests broadly span topics in com-
     benchmark for the evaluation of RGB-D SLAM systems,” in IROS, 2012.                                   puter vision, machine learning, and robotics.
[38] Z. Li, T. Dekel, F. Cole, R. Tucker, N. Snavely, C. Liu, and W. T.
     Freeman, “Learning the depths of moving people by watching frozen
     people,” in CVPR, 2019.
[39] W. Chen, S. Qian, and J. Deng, “Learning single-image depth from
     videos using quality assessment networks,” in CVPR, 2019.
[40] J. Cho, D. Min, Y. Kim, and K. Sohn, “A large RGB-D dataset for semi-
     supervised monocular depth estimation,” arXiv:1904.10230, 2019.
[41] A. Gordon, H. Li, R. Jonschkowski, and A. Angelova, “Depth from
     videos in the wild: Unsupervised monocular depth learning from un-
     known cameras,” in ICCV, 2019.                                                                        Katrin Lasinger received her Master’s degree
[42] B. Ummenhofer, H. Zhou, J. Uhrig, N. Mayer, E. Ilg, A. Dosovitskiy, and                               in computer science from TU Wien in 2015. She
     T. Brox, “DeMoN: Depth and motion network for learning monocular                                      is currently pursuing her Ph.D. degree in com-
     stereo,” in CVPR, 2017.                                                                               puter vision at the group of Photogrammetry and
[43] J. M. Facil, B. Ummenhofer, H. Zhou, L. Montesano, T. Brox, and                                       Remote Sensing at ETH Zurich. Her research is
     J. Civera, “CAM-Convs: Camera-aware multi-scale convolutions for                                      focused on 3D computer vision, including vol-
     single-view depth,” in CVPR, 2019.                                                                    umetric fluid flow estimation and dense depth
[44] S. Song, S. P. Lichtenberg, and J. Xiao, “SUN RGB-D: A RGB-D scene                                    estimation from single or multiple views.
     understanding benchmark suite,” in CVPR, 2015.
[45] M. Cordts, M. Omran, S. Ramos, T. Rehfeld, M. Enzweiler, R. Benenson,
     U. Franke, S. Roth, and B. Schiele, “The Cityscapes dataset for semantic
     urban scene understanding,” in CVPR, 2016.
[46] A. Dai, A. X. Chang, M. Savva, M. Halber, T. Funkhouser, and
     M. Nießner, “ScanNet: Richly-annotated 3D reconstructions of indoor
     scenes,” in CVPR, 2017.
[47] A. Knapitsch, J. Park, Q.-Y. Zhou, and V. Koltun, “Tanks and temples:                                 David Hafner received a Master’s and a Ph.D.
     Benchmarking large-scale scene reconstruction,” ACM Transactions on                                   degree from Saarland University, Germany, in
     Graphics, vol. 36, no. 4, 2017.                                                                       2012 and 2018, respectively. Since 2019, he
[48] I. Vasiljevic, N. Kolkin, S. Zhang, R. Luo, H. Wang, F. Z.                                            has been a research engineer at the Intelligent
     Dai, A. F. Daniele, M. Mostajabi, S. Basart, M. R. Walter, and                                        Systems Lab at Intel in Munich, Germany.
     G. Shakhnarovich, “DIODE: A Dense Indoor and Outdoor DEpth
     Dataset,” arXiv:1908.00463, 2019.
[49] S. Hadfield, K. Lebeda, and R. Bowden, “Hollywood 3D: What are the
     best 3D features for action recognition?” IJCV, vol. 121, no. 1, 2017.
[50] J. Xie, R. B. Girshick, and A. Farhadi, “Deep3D: Fully automatic 2D-to-
     3D video conversion with deep convolutional neural networks,” in ECCV,
     2016.
[51] F. Devernay and P. A. Beardsley, “Stereoscopic cinema,” in Image and
     Geometry Processing for 3-D Cinematography. Springer, 2010.
[52] R. Neuman, “Bolt 3D: a case study,” in Stereoscopic Displays and
     Applications XX, vol. 7237. SPIE, 2009.
[53] FFmpeg developers, “FFmpeg,” https://ffmpeg.org, 2018.                                                Konrad Schindler (M’05SM’12) received the
[54] D. Sun, X. Yang, M.-Y. Liu, and J. Kautz, “PWC-Net: CNNs for optical                                  Diplomingenieur (M.Tech.) degree from Vienna
     flow using pyramid, warping, and cost volume,” in CVPR, 2018.                                         University of Technology, Vienna, Austria, in
[55] S. Rota Bulò, L. Porzi, and P. Kontschieder, “In-place activated batch-                              1999, and the Ph.D. degree from Graz University
     norm for memory-optimized training of DNNs,” in CVPR, 2018.                                           of Technology, Graz, Austria, in 2003. He was a
[56] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image                                Photogrammetric Engineer in the private indus-
     recognition,” in CVPR, 2016.                                                                          try and held researcher positions at Graz Uni-
[57] J. Deng, W. Dong, R. Socher, L. Li, K. Li, and F. Li, “ImageNet: A                                    versity of Technology, Monash University, Mel-
     large-scale hierarchical image database,” in CVPR, 2009.                                              bourne, VIC, Australia, and ETH Zuürich, Zürich,
[58] D. P. Kingma and J. L. Ba, “Adam: A method for stochastic optimiza-                                   Switzerland. He was an Assistant Professor of
     tion,” in ICLR, 2015.                                                                                 Image Understanding with TU Darmstadt, Darm-
[59] J. Uhrig, N. Schneider, L. Schneider, U. Franke, T. Brox, and A. Geiger,       stadt, Germany, in 2009. Since 2010, he has been a Tenured Professor
     “Sparsity invariant cnns,” in 3DV, 2017.                                       of Photogrammetry and Remote Sensing with ETH Zürich. His research
[60] D. Eigen and R. Fergus, “Predicting depth, surface normals and semantic        interests include computer vision, photogrammetry, and remote sensing.
     labels with a common multi-scale convolutional architecture,” in ICCV,
     2015.
[61] S. Xie, R. Girshick, P. Dollár, Z. Tu, and K. He, “Aggregated residual
     transformations for deep neural networks,” in CVPR, 2017.
[62] G. Huang, Z. Liu, L. van der Maaten, and K. Q. Weinberger, “Densely
     connected convolutional networks,” in CVPR, 2017.
                                                                                                           Vladlen Koltun is the Chief Scientist for Intelli-
[63] D. Mahajan, R. Girshick, V. Ramanathan, K. He, M. Paluri, Y. Li,
                                                                                                           gent Systems at Intel. He directs the Intelligent
     A. Bharambe, and L. van der Maaten, “Exploring the limits of weakly
                                                                                                           Systems Lab, which conducts high-impact basic
     supervised pretraining,” in ECCV, 2018.
                                                                                                           research in computer vision, machine learning,
[64] F. Perazzi, J. Pont-Tuset, B. McWilliams, L. J. V. Gool, M. H. Gross, and
                                                                                                           robotics, and related areas. He has mentored
     A. Sorkine-Hornung, “A benchmark dataset and evaluation methodology
                                                                                                           more than 50 PhD students, postdocs, research
     for video object segmentation,” in CVPR, 2016.
                                                                                                           scientists, and PhD student interns, many of
[65] A. Hertzmann, “Why do line drawings work? a realism hypothesis,”
                                                                                                           whom are now successful research leaders.
     Perception, 2020.
