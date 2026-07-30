---
source_id: 153
bibtex_key: zhou2021rgbdsurvey
title: RGB-D Salient Object Detection: A Survey
year: 2021
domain_theme: Uncoded
verified_pdf: 153_Survei RGB-D SOD (Zhou dkk.).pdf
char_count: 261471
---

1

                                                     RGB-D Salient Object Detection: A Survey
                                                                Tao Zhou, Deng-Ping Fan, Ming-Ming Cheng, Jianbing Shen, and Ling Shao

                                            Abstract—Salient object detection (SOD), which simulates the               RGB                      Depth                     GT
                                         human visual perception system to locate the most attractive
                                         object(s) in a scene, has been widely applied to various computer
                                         vision tasks. Now, with the advent of depth sensors, depth
                                         maps with affluent spatial information that can be beneficial
                                         in boosting the performance of SOD can easily be captured.
                                         Although various RGB-D based SOD models with promising                        DCMC                     SE                        D3Net
                                         performance have been proposed over the past several years,
arXiv:2008.00230v4 [cs.CV] 14 Jul 2022

                                         an in-depth understanding of these models and the challenges
                                         in this field remains lacking. In this paper, we provide a
                                         comprehensive survey of RGB-D based SOD models from various
                                         perspectives, and review related benchmark datasets in detail.
                                         Further, considering the fact that light fields can also provide
                                         depth maps, we review SOD models and popular benchmark                        SSF                      A2dele                    S2MA
                                         datasets from this domain as well. Moreover, to investigate the
                                         SOD ability of existing models, we carry out a comprehensive
                                         evaluation and conduct an attribute-based evaluation of several
                                         representative RGB-D based SOD models. Finally, we discuss
                                         several challenges and open directions of RGB-D based SOD for
                                         future research. All collected models, benchmark datasets, source             ICNet                    JL-DCF                    UC-Net
                                         code links, datasets constructed for attribute-based evaluation,
                                         and codes for evaluation have been made publicly available at
                                         https://github.com/taozh2017/RGBD-SODsurvey.
                                           Index Terms—RGB-D based salient object detection, saliency
                                         detection, comprehensive evaluation, light fields.
                                                                                                                      Fig. 1. RGB-D based salient object prediction on a sample image using two
                                                                                                                      classic non-deep models (i.e., DCMC [1] and SE [2]) and seven state-of-the-
                                                                  I. I NTRODUCTION                                    art deep models (i.e., D3 Net [3], SSF [4], A2dele [5], S2 MA [6], ICNet [7],
                                                                                                                      JL-DCF [8], and UC-Net [9]).
                                            Salient object detection (SOD) aims to locate the most
                                         visually prominent object(s) in a given scene [10]. SOD plays
                                         a key role in a range of real-world applications, such as                    of depth-induced saliency. Ciptadi et al. [47] extracted 3D
                                         stereo matching [11], image understanding [12], co-saliency                  layout and shape features from depth measurements. Besides,
                                         detection [13], action recognition [14], video detection and                 several methods [48], [49], [49], [50] measure depth contrast
                                         segmentation [15]–[18], semantic segmentation [19], [20],                    using the depth difference between different regions. In [51],
                                         medical image segmentation [21]–[23], object tracking [24],                  a multi-contextual contrast model including local, global, and
                                         [25], person re-identification [26], [27], camouflaged object                background contrast was developed to detect salient objects
                                         detection [28], image retrieval [29], etc. Although significant              using depth maps. More importantly, however, this work
                                         progress has been made in the SOD field over the past several                also provided the first large-scale RGB-D dataset for SOD.
                                         years [30]–[36], [36]–[44], there is still room for improvement              Despite the effectiveness achieved by traditional methods
                                         when faced with challenging factors, such as complicated                     using handcrafted features, they tend to suffer from a limited
                                         background or different lighting conditions in the scenes. One               generalization ability for low-level features and lack the high-
                                         way to overcome these challenges is to employ depth maps,                    level reasoning required for complex scenes. To address these
                                         which provide complementary spatial information for RGB                      limitations, several deep learning-based RGB-D SOD methods
                                         images and have become easier to capture due to the large                    [3] have been developed, showing improved performance. DF
                                         availability of depth sensors (e.g., Microsoft Kinect).                      [52] was the first model to introduce deep learning technology
                                            Recently, RGB-D based SOD has gained increasing at-                       into the RGB-D based SOD task. More recently, various
                                         tention and various methods have been developed [3], [45].                   deep learning-based models [6]–[9], [53]–[55] have focused
                                         Early RGB-D based SOD models tended to extract handcrafted                   on exploiting effective multi-modal correlations and multi-
                                         features and then fuse RGB image and depth maps. For ex-                     scale/level information to boost SOD performance. To more
                                         ample, Lang et al. [46], the first work on RGB-D based SOD,                  clearly describe the progress in the RGB-D based SOD field,
                                         utilized Gaussian mixture models to model the distribution                   we provide a brief chronology in Fig. 2.
                                                                                                                         In this paper, we provide a comprehensive survey on RGB-
                                           Corresponding author: Ding-Ping Fan (dengpingfan@mail.nankai.edu.cn).      D based SOD, aiming to thoroughly cover various aspects of
                                           T. Zhou, D.-P. Fan, J. Shen, and L. Shao are with Inception Institute of
                                         Artificial Intelligence, Abu Dhabi, UAE.                                     the models for this task and provide insightful discussions on
                                           M.-M. Cheng is with CS, Nankai University, Tianjin 300350, China.          the challenges and open directions for future work. We also
                                                                                                                                                                                                               2

                                                                                                                                              DMRA [54]
                                                           LHM [51]                                                                 propose DUT-RGBD dataset
                                             (first large-scale benchmark)                                    DF [52]
                                                                              GP [50]                  first deep model
                                                                                                                                                               UC-Net [9]
                                                LS [47]                (orientation and                                                               first uncertain model
                                       (collect GIT dataset)          background priors )
                                                                                                LBE [57]                                     CPFP [53]                  D3Net [3]
     Traditional models

                                                                                                                                                                                           Deep-based models
                               DM [46]                                                  (Local Background                         fluid pyramid integration      new SIP dataset
                          (first RGB-D SOD
                                                                                        Enclosure feature)
                                 work)

                              2012           2013              2014             2015              2016          2017             2018            2019              2020

                                                                                                                               CTMF [58]                              JL-DCF [8]
                                                                                                                  (transfer from RGB to depth)             (densely- cooperative fusion)
                                                                 ACSD [56]
                                                        (two prior refinement)
                                                                                                                                                      MMCI [55]
                                                                                                                                         (multi-scale multi-path fusion)

     Fig. 2. A brief chronology of RGB-D based SOD. The first early RGB-D based SOD work was the DM [46] model, proposed in 2012. Deep learning
     techniques have been widely applied to RGB-D based SOD since 2017. More details can be found in § II.

     review another related topic, i.e., light field SOD, in which the                                             • We provide the first systematic review of RGB-D based
     light field can provide more information (including focal stack,                                                SOD models from different perspectives. We summa-
     all-focus images, and depth maps) to boost the performance of                                                   rize existing RGB-D SOD models into traditional or
     salient object detection. Further, we provide a comprehensive                                                   deep methods, fusion-wise methods, single-stream/multi-
     comparison to evaluate existing RGB-D based SOD models                                                          stream methods, and attention-aware methods.
     and discuss their main advantages.                                                                            • We review nine RGB-D datasets that are commonly
V5                                                                                                                   used in this field, and provide details for each dataset.
     A. Related Reviews and Surveys                                                                                  Moreover, we provide a comprehensive as well as an
        There are several surveys that are closely related to salient                                                attribute-based evaluation of several representative RGB-
     object detection. For example, Borji et al. [59] provided a                                                     D based SOD models.
     quantitative evaluation of 35 state-of-the-art non-deep saliency                                              • We supply the first collection and review of the related

     detection methods. Cong et al. [60] reviewed several different                                                  light field SOD models and benchmark datasets.
     saliency detection models, including RGB-D based SOD,                                                         • We thoroughly investigate several challenges for RGB-

     co-saliency detection, and video SOD. Zhang et al. [61]                                                         D based SOD, and the relation between SOD and other
     provided an overview of co-saliency detection and reviewed its                                                  topics, shedding light on potential directions for future
     history, and summarized several benchmark algorithms in this                                                    research.
     field. Han et al. [62] reviewed the recent progress in SOD,
     including models, benchmark datasets, and evaluation metrics,                                              C. Organization
     as well as discussed the underlying connection among general
                                                                                                                  In § II, we review existing RGB-D based models in terms
     object detection, SOD, and category-specific object detection.
                                                                                                                of different aspects. In § III, we summarize and provide
     Nguyen et al. [63] reviewed various works related to saliency
                                                                                                                details for current benchmark datasets for RGB-D salient
     applications and provided insightful discussions on the role of
                                                                                                                object detection. In § IV, we conduct a comprehensive review
     saliency in each. Borji et al. [64] provided a comprehensive
                                                                                                                of light field SOD models and benchmark datasets. In § V,
     review of recent progress in SOD and discussed some related
                                                                                                                we provide a comprehensive and attribute-based evaluation of
     works, including generic scene segmentation, saliency for
                                                                                                                several representative RGB-D based models. We then discuss
     fixation prediction, and object proposal generation. Fan et
                                                                                                                challenges and open directions of this field in § VI. Finally,
     al. [10] provided a comprehensive evaluation of several state-
                                                                                                                we conclude this paper in § VII.
     of-the-art CNNs-based SOD models, and proposed a high
     quality SOD dataset, termed SOC (details can be found at:
     http://dpfan.net/socbenchmark/). Zhao et al. [65] reviewed                                                                  II. RGB-D BASED SOD M ODELS
     various deep learning-based object detection models and al-                                                   Over the past few years, several RGB-D based SOD
     gorithms in detail, as well as various specific tasks, including                                           methods have been developed and obtained promising per-
     SOD works. Wang et al. [66] focused on reviewing deep                                                      formance. These models are summarized in Tables I, II,
     learning-based SOD models. Different from previous SOD                                                     III and IV. The complete benchmark can be found at
     surveys, in this paper, we focus on reviewing the existing                                                 http://dpfan.net/d3netbenchmark/. To review these RGB-D
     RGB-D based SOD models and benchmark datasets.                                                             based SOD models in detail,we introduce them from different
                                                                                                                perspectives as follows. (1) Traditional/deep models: they
     B. Contributions                                                                                           are viewed from the perspective of feature extraction, that is
       Our main contributions are summarized as follows:                                                        using the manual features or deep features. It is convenient
                                                                                                                                    3

for follow-up researchers to grasp the historical development           • CPFP [53] proposes a contrast-enhanced network to
trends of RGB-D SOD models. (2) Fusion-wise models: it               produce an enhanced map, and presents a fluid pyramid inte-
is critical to effectively fuse RGB and depth images in this         gration module to effectively fuse cross-modal information in
task, thus we review different fusion strategies to understand       a hierarchical manner. Besides, considering the fact that depth
their effectiveness. (3) Single-stream/multi-stream models:          cues tend to suffer from noise, a feature-enhanced module
we consider this problem from the perspective of model               is proposed to learn an enhanced depth cue for boosting the
parameters. Single stream can save parameters, but the final         SOD performance. It is worth noting that this is an effective
result may not be optimal, and multiple streams may require          solution.
more parameters. Thus, it is helpful to understand the balance          • UC-Net [9] proposes a probabilistic RGB-D based SOD
between the amount of calculation and accuracy of different          network via conditional variational autoencoders (VAEs) to
models. (4) Attention-aware models: attention mechanisms             model human annotation uncertainty. It generates multiple
have widely been applied in various visual tasks including           saliency maps for each input image by sampling in the learned
SOD. We review related works on RGB-D SOD to analyze                 latent space. This was the first work to investigate uncertainty
how do different models use attention. Thus, it is an alternative    in RGB-D based SOD, and was inspired by the data labeling
to design attention modules for future works.                        process. This method leverages the diverse saliency maps to
                                                                     improve the final SOD performance.
A. Traditional/Deep Models
   Traditional Models. With depth cues, several useful at-           B. Fusion-wise Models
tributes, such as boundary cues, shape attributes, surface              For RGB-D based SOD models, it is important to effectively
normals, etc., can be explored to boost the identification of        fuse RGB images and depth maps. The existing fusion strate-
salient objects in complex scenes. Over the past several years,      gies can be grouped into three categories, including 1) early
many traditional RGB-D models based on handcrafted features          fusion, 2) multi-scale fusion, and 3) late fusion. We provide
have been developed [1], [2], [47]–[51], [56], [57], [69]–[71],      details for each fusion strategy as follows.
[75], [82]–[84], [95]. For example, the early work [47] focused         Early Fusion. Early fusion-based methods can follow one
on modeling the interaction between layout and shape features        of two veins: 1) RGB images and depth maps are directly
generated from the RGB image and depth map. Besides,                 integrated to form a four-channel input [50], [51], [87], [87],
the representative work [51] developed a novel multi-stage           [96]. This is denoted as “input fusion” (shown in Fig. 3); 2)
RGB-D model, and constructed the first large-scale RGB-D             RGB and depth images are first fed into each independent
benchmark dataset, termed NLPR.                                      network and their low-level representations are combined as
   Deep Models. However, the above-mentioned methods suf-            joint representations, which are then fed into a subsequent
fer from unsatisfactory SOD performance due to the limited           network for further saliency map prediction [52]. This is
expression ability of handcrafted features. To address this,         denoted as “early feature fusion” (shown in Fig. 3).
several studies have turned to deep neural networks (DNNs) to           Late Fusion. Late fusion-based methods can also be further
fuse RGB-D data [4], [5], [7]–[9], [52]–[55], [83], [93], [94],      divided into two families: 1) Two parallel network streams
[96]–[108]. These models can learn high-level representations        are adopted to learn high-level features for RGB and depth
to explore complex correlations across RGB images and                data, respectively, which are concatenated and then used for
depth cues for improving SOD performance. We review some             generating the final saliency prediction [48], [58], [102]. This
representative works in detail as follows.                           is denoted as “later feature fusion” (shown in Fig. 3). 2) Two
   • DF [52] develops a novel convolutional neural network           parallel network streams are used to obtain the independent
(CNN) to integrate different low-level saliency cues into            saliency maps for RGB images and depth cues, and then the
hierarchical features, for effectively locating salient regions in   two saliency maps are concatenated to obtain a final prediction
RGB-D images. This was the first CNN-based model for the             map [115]. This is denoted as “late result fusion” (shown in
RGB-D SOD task. However, it utilizes a shallow architecture          Fig. 3).
to learn the saliency map.                                              Multi-scale Fusion. To effectively explore the correlations
   • PCF [92] presents a complementarity-aware fusion mod-           between RGB images and depth maps, several methods pro-
ule to integrate cross-modal and cross-level feature repre-          pose a multi-scale fusion strategy [7], [8], [55], [116], [120],
sentations. It can effectively exploit complementary informa-        [123], [124], [129]. These models can be divided into two cat-
tion by explicitly using cross-modal/level connections and           egories. The first category learn the cross-modal interactions
modal/level-wise supervision to decrease fusion ambiguity.           and then fuse them into a feature learning network. For exam-
   • CTMF [58] employs a computational model to identify             ple, Chen et al. [55] developed a multi-scale multi-path fusion
salient objects from RGB-D scenes, utilizing CNNs to learn           network to integrate RGB images and depth maps, with a
high-level representations for RGB images and depth cues,            cross-modal interaction (termed MMCI) module. This method
while simultaneously exploiting the complementary relation-          introduces cross-modal interactions into multiple layers, which
ships and joint representation. Besides, this model transfers        can empower additional gradients for enhancing the learning
the structure of the model from the source domain (i.e., RGB         of the depth stream, as well as enable complementarity across
images) to be applicable to the target domain (i.e., depth           low-level and high-level representations to be explored. The
maps).                                                               second category fuse the features from RGB images and depth
                                                                                                                                                                                    4

                                                                   TABLE I
                                       S UMMARY OF RGB-D BASED SOD METHODS ( PUBLISHED FROM 2012 TO 2016).
     #      Year         Method      Pub.   Training Set           Backbone      Description
     1      2012       DM [46]      ECCV    Without                Without       Models the correlation between saliency and depth by approximating the joint density
                                                                                 using Gaussian mixture models
     2      2012      RCM [67]      ICCSE   Without                Without       Develops a region contrast based SOD model with depth cues
     3      2013        LS [47]     BMVC    Without                Without       Extends the dissimilarity framework to model the joint interaction between depth cues and
                                                                                 RGB images
     4      2013        RC [48]     BMVC    Withoutt               Without       Derives RGB-D saliency by formulating a 3D saliency model based on the region contrast
                                                                                 of the scene and fuses it using SVM
     5      2013       SOS [68]    NEURO    Without                Without       Incorporates depth cues for salient object segmentation by suppressing background regions
     6      2014      SRDS [69]    ICDSP    Without                Without       Integrates depth and depth weighted color contrast with spatial compactness of color
                                                                                 distribution
     7      2014      LHM [51]      ECCV    Without                Without       Uses a multi-stage RGB-D algorithm to combine both depth and appearance cues to
                                                                                 segment salient objects
     8      2014     DESM [49]     ICIMCS   Without                Without       Combines three saliency cues: color contrast, spatial bias, and depth contrast
     9      2014     ACSD [56]       ICIP   Without                Without       Measures a point’s saliency by how much it stands out from the surroundings, and has two
                                                                                 priors (regions nearer to viewers are more salient and salient objects tend to be located at
                                                                                 the center)
     10     2015        GP [50]    CVPRW    Without                Without       Explores orientation and background priors for detecting salient objects, and uses PageR-
                                                                                 ank and MRFs to optimize the saliency maps
     11     2015       SFP [70]    ICIMCS   Without                Without       Develops a RGB-D based SOD approach using saliency fusion and propagation
     12     2015       DIC [71]      TVC    Without                Without       Fuses the saliency maps from color and depth to generate a noise-free salient patch, and
                                                                                 utilizes random walk algorithm to infer the object boundary
     13     2015       SRD [72]     ICRA    Without                Without       Designs a graph-based segmentation to identify homogeneous regions using color and
                                                                                 depth cues
     14     2015     MGMR [73]       ICIP   Without                Without       Designs a mutual guided manifold ranking strategy to achieve SOD
     15     2015       SF [74]       CAC    Without                Without       Proposes to automatically select discriminative features using decision trees for better
                                                                                 performance
     16     2016       PRC [75]    ACCESS   Without                Without       Saliency fusion and progressive region classification are used to optimize depth-aware
                                                                                 saliency models
     17     2016       LBE [57]     CVPR    Without                Without       Uses a local background enclosure to capture the spread of angular directions
     18     2016         SE [2]     ICME    Without                Without       Utilizes cellular automata to propagate the initial saliency map and then generate the final
                                                                                 saliency prediction result
     19     2016      DCMC [1]       SPL    Without                Without       Develops a new measure to evaluate the reliability of depth maps for reducing the influence
                                                                                 of poor-quality depth maps on saliency detection.
     20     2016        BF [76]     ICPR    Without                Without       Fuses contrasting features from RGB and depth images with a Bayesian framework
     21   V32016       DCI [77]    ICASSP   Without                Without       Adopts the original depth map to subtract the fitted surface for generating a contrast
                                                                                 increased map
     22     2016       DSF [78]    ICASSP   Without                Without       Develops a multi-stage depth-aware saliency model for SOD
     23     2016       GM [79]      ACCV    Without                Without       Combines color and depth-based contrast features using a generative mixture model

                                                Concatenation                                                                                                    saliency map
                                                                                                                                       fusion

                                                                                                                                                                Convolution layer
                           Concatenation                                                                                               fusion

   Concatenation                                                                                                                       fusion                   Skip connection

                                                                                                                                                                   Interaction

   RGB       Depth       RGB        Depth      RGB         Depth         RGB         Depth          RGB        Depth         RGB                Depth

               (a) Early fusion                                    (b) Late fusion                               (c) Multi-scale fusion

Fig. 3. Comparison of three fusion strategies that explore the correlation between RGB images and depth maps for RGB-D based SOD. These include: 1)
Early fusion; 2) Late fusion; 3) Multi-scale fusion.

maps in different layers and then integrate them into a decoder                              lizing a spatial attention mechanism. Besides, this model
network (e.g., skip connection) to produce the final saliency                                controls the fusion rate of the cross-modal information using
detection map (as shown in Fig. 3). Some representative works                                a gate function, which can reduce some effects brought by the
are briefly discussed as follows.                                                            unreliable depth cues.
   • ICNet [7] proposes an information conversion module                                      • BiANet [120] employs a multi-scale bilateral attention
to convert high-level features in an interactive manner. In                                  module (MBAM) to capture better global information in
this model, a cross-modal depth-weighted combination (CDC)                                   multiple layers.
block is introduced to enhance RGB features with depth                                          • JL-DCF [8] treats a depth image as a special case of
features at different levels.                                                                a color image and employs a shared CNN for both RGB and
  • DPANet [116] uses a gated multi-modality attention                                       depth feature extraction. It also proposes a densely-cooperative
(GMA) module to exploit long-range dependencies. The GMA                                     fusion strategy to effectively combine the learned features from
module can extract the most discriminative features by uti-                                  different modalities.
                                                                                                                                                              5

                                                              TABLE II
                                  S UMMARY OF RGB-D BASED SOD METHODS ( PUBLISHED FROM 2017 TO 2018).
    #    Year       Method     Pub.   Training Set   Backbone    Description
    24   2017   HOSO [80]     DICTA   Without        Without     Combines surface orientation distribution contrast with color and depth contrast
    25   2017   M3 Net [81]    IROS   NLPR(0.65K),   VGG-16      Designs a multi-path multi-modal fusion strategy to integrate RGB and depth images in
                                      NJUD(1.4K)                 a task-motivated and adaptive way
    26   2017   MFLN [82]     ICCVS   NLPR(0.65K),   AlexNet     Leverages a CNN to learn high-level representations for depth maps, and uses a multi-
                                      NJUD(1.4K)                 modal fusion network to integrate RGB and depth representations for RGB-D based SOD
    27   2017    BED [83]     ICCVW   NLPR(0.6K),    GoogleNet   Uses a CNN to integrate top-down and bottom-up information for RGB-D based SOD,
                                      NJUD(1.2K)                 and uses a mid-level feature representation to capture background enclosure
    28   2017   CDCP [84]     ICCVW   Without        Without     Proposes a novel RGB-D SOD algorithm using a center dark channel prior to boost
                                                                 performance
    29   2017     TPF [85]    ICCVW   Without        Without     Leverages stereopsis to generate optical flow, which can provide an additional cue (depth
                                                                 cue) for producing the final detection result
    30   2017    MFF [86]      SPL    Without        Without     Uses a multistage fusion framework to integrate multiple visual priors from the RGB
                                                                 image and depth cue for SOD
    31   2017   MDSF [87]      TIP    NLPR(0.5K),    Without     Proposes a RGB-D SOD framework via a multi-scale discriminative saliency fusion
                                      NJUD(1.5K)                 strategy, and utilizes bootstrap learning to achieve the SOD task
    32   2017      DF [52]     TIP    NLPR(0.75K),   Without     Feeds RGB and depth features into a CNN architecture to derive the saliency confidence
                                      NJUD(1.0K)                 value, and uses Laplacian propagation to produce the final detection result
    33   2017   MCLP [88]     TCYB    Without        Without     Utilizes the additional depth maps and employs the existing RGB saliency map as an
                                                                 initialization using a refinement-cycle model to obtain the final co-saliency map
    34   2018    ISC [89]     SIVP    Without        Without     Fuses salient features using both bottom-up and top-down saliency cues
    35   2018   HSCS [90]     TMM     Without        Without     Utilizes a hierarchical sparsity reconstruction and energy function refinement for RGB-D
                                                                 based co-saliency detection
    36   2018     ICS [91]     TIP    Without        Without     Exploits the constraint correlation among multiple images and introduces depth maps into
                                                                 the co-saliency model
    37   2018   CTMF [58]     TCYB    NLPR(0.65K),   VGG-16      Transfers the structure of the deep color network to be applicable for the depth modality
                                      NJUD(1.4K)                 and fuses both modalities to produce the final saliency map
    38   2018     PCF [92]    CVPR    NLPR(0.65K),   VGG-16      Designs the first multi-scale fusion architecture and a novel complementarity-aware fusion
                                      NJUD(1.4K)                 module to fuse both cross-modal and cross-level features
    39   2018   SCDL [93]     ICDSP   NLPR(0.75K),   VGG-16      Designs a new loss function to increase the spatial coherence of salient objects
                                      NJUD(1.0K)
    40   2018   ACCF [94]     IROS    NLPR(0.65K),   VGGNet      Adaptively selects complementary features from different modalities at each level, and
                                      NJUD(1.4K)                 then performs more informative cross-modal cross-level combinations
    41   2018    CDB [95]     NEURO   Without        Without     Utilizes a contrast prior and depth-guided-background prior to construct a 3D stereoscopic
                                                                 saliency model

  • BBS-Net [129] uses a bifurcated backbone strategy (BBS)             worth noting that most recent deep learning-based models [5],
to split the multi-level feature representations into teacher           [7], [45], [55], [92], [100], [104], [106], [116], [118] utilize
and student features, and develops a depth-enhanced module              this two-stream architecture with several models capturing
(DEM) to explore informative parts in depth maps from the               the correlations between RGB images and depth cues across
spatial and channel views.                                              multiple layers. Moreover, some models utilize a multi-stream
                                                                        structure [3], [99] and then design different fusion modules to
                                                                        effectively fuse RGB and depth information in order to exploit
C. Single-stream/Multi-stream Models
                                                                        their correlations.
   Single-stream Models. Several RGB-D based SOD works
[52], [53], [83], [87], [93], [96], [97] focus on a single-stream
architecture to achieve saliency prediction. These models often         D. Attention-aware Models
fuse RGB images and depth information in the input channel                 Existing RGB-D based SOD methods often treat all regions
or feature learning part. For example, MDSF [87] employs                equally using the extracted features equally, while ignoring the
a multi-scale discriminative saliency fusion framework as the           fact that different regions can have different contributions to
SOD model, in which four types of features in three levels              the final prediction map. These methods are easily affected by
are computed and then fused to obtain the final saliency map.           cluttered backgrounds. In addition, some methods either regard
BED [83] utilizes a CNN architecture to integrate bottom-up             the RGB images and depth maps as having the same status
and top-down information for SOD, which also incorporates               or overly rely on depth information. This prevents them from
multiple features, including background enclosure distribution          considering the importance of different domains (RGB images
(BED) and low level depth maps (e.g., depth histogram                   or depth cues). To overcome this, several methods introduce
distance and depth contrast) to boost the SOD performance.              attention mechanisms to weight the importance of different
PDNet [97] extracts depth-based features using a subsidiary             regions or domains.
network, which makes full use of depth information to assist               • ASIF-Net [106] captures complementary information
the main-stream network.                                                from RGB images and depth cues using an interweaved fusion,
   Multi-stream Models. Two-stream models [54], [102],                  and weights the saliency regions through a deeply supervised
[103] consist of two independent branches that process RGB              attention mechanism.
images and depth cues, respectively, and often generate differ-            • AttNet [103] introduces attention maps for differentiating
ent high-level features or saliency maps and then incorporate           between salient objects and background regions to reduce the
them in the middle stage or end of the two streams. It is               negative influence of some low-quality depth cues.
                                                                                                                                                              6

                                                             TABLE III
                                    S UMMARY OF RGB-D BASED SOD MODELS PUBLISHED IN 2019 AND 2020
    No.   Year          Method      Pub.    Training Set     Backbone     Description
    42    2019        SSRC [96]    NEURO    NLPR(0.65K),     VGG-16       Uses a single-stream recurrent convolutional neural network with a four-channel
                                            NJUD(1.4K)                    input and DRCNN subnetwork
    43    2019        MLF [109]     SPL     NJUD(1.588K)     VGG-16       Designs a salient object-aware data augmentation method to expand the training
                                                                          set
    44    2019       TSRN [110]     ICIP    NJUD(1.387K)     VGG-16       Designs a fusion refinement module to integrate output features from different
                                                                          modalities and resolutions
    45    2019        DIL [111]    MTAP     NLPR(0.5K),      Without      Designs a consistency integration strategy to generate an image pre-segmentation
                                            NJUD(0.5K)                    result that is consistent with the depth distribution
    46    2019      CAFM [112]     TSMC     NUS [46], NCTU   VGG-16       Utilizes a content-aware fusion module to integrate global and local information
                                            [113]
    47    2019       PDNet [97]    ICME     NLPR(0.5K),      VGG-16       Adopts a prior-model guided master network to process RGB information, which
                                            NJUD(1.5K)                    is pre-trained on the conventional RGB dataset to overcome the limited size
    48    2019       MMCI [55]       PR     NLPR(0.65K),     VGG-16       Improves the traditional two-stream architecture by diversifying the multi-modal
                                            NJUD(1.4K)                    fusion paths and introducing cross-modal interactions in multiple layers
    49    2019       TANet [99]     TIP     NLPR(0.65K),     VGG-16       Uses a three-stream multi-modal fusion framework to explore cross-modal
                                            NJUD(1.4K)                    complementarity in both the bottom-up and top-down processes
    50    2019      DCMF [100]     TCYB     NLPR(0.65K),     VGG-16       Formulates a CNN-based cross-modal transfer learning problem for depth-
                                            NJUD(1.4K)                    induced SOD, and uses a dense cross-level feedback strategy to exploit cross-
                                                                          level interactions
    51    2019        DGT [101]    TCYB     Without          Without      Exploits depth cues and provides a general transformation model from RGB
                                                                          saliency to RGB-D saliency
    52    2019         LSF [45]     arXiv   NLPR(0.65K),     VGG          Designs an RGB-D system with three key components, including modality-
                                            NJUD(1.4K)                    specific representation learning, complementary information selection, and cross-
                                                                          modal complements fusion
    53    2019      AFNet [102]    ACCESS   NLPR(0.65K),     VGG-16       Learns a switch map that is used to adaptively fuse the predicted saliency maps
                                            NJUD(1.4K)                    from the RGB and depth modality
    54    2019        EPM [114]    ACCESS   Without          Without      Develops an effective propagation mechanism for RGB-D co-saliency detection
    55    2019        CPFP [53]     CVPR    NLPR(0.65K),     VGG-16       Uses a contrast-enhanced network to obtain the one-channel enhanced map,
                                            NJUD(1.4K)                    and designs a fluid pyramid integration module to fuse cross-modal cross-level
                                                                          features in a pyramid style
    56    2019       DMRA [54]      ICCV    NLPR(0.7K),      VGG-19       Designs a depth-induced multiscale recurrent attention network for SOD, includ-
                                            NJUD(1.485K)                  ing a depth refinement block and a recurrent attention module
    57    2019        DSD [115]    JVCIR    NLPR(0.5K),      VGG-16       Uses a saliency fusion network to adaptively fuse both the color and depth
                                            NJUD(1.5K)                    saliency maps
    58    2020     DPANet [116]     arXiv   NLPR(0.65K),     ResNet-50    Uses a saliency-orientated depth perception module to evaluate the potentiality
                                            NJUD(1.4K),                   of depth maps and reduce effects of contamination
                                            DUT(0.8K)
    59    2020       SSDP [117]     arXiv   NLPR(0.7K),      VGG-19       Makes use of existing labeled RGB saliency datasets together with unlabeled
                                            NJUD(1.485K),                 RGB-D data to boost SOD performance
                                            DUT(0.8K)
    60    2020      AttNet [103]    IVC     NLPR(0.65K),     VGG-16       Deploys attention maps to boost the salient objects’ location and pays more
                                            NJUD(1.4K)                    attention to the appearance information
    61    2020          — [104]    NEURO    NLPR(0.65K),     VGG-16       Uses an adaptive gated fusion module via a GAN to obtain a better fused saliency
                                            NJUD(1.4K)                    map from RGB images and depth cues
    62    2020     CoCNN [105]       PR     STERE, NJUD      VGG-16       Fuses color and disparity features from low to high layers in a unified deep
                                                                          model
    63    2020   cmSalGAN [118]     TMM     NLPR(0.65K),     ResNet-50    Aims to learn an optimal view-invariant and consistent pixel-level representation
                                            NJUD(1.4K)                    for both RGB and depth images using an adversarial learning framework
    64    2020       PGHF [119]    ACCESS   NLPR(0.65K),     VGG-16       Leverages powerful representations learned from large-scale RGB datasets to
                                            NJUD(1.4K)                    boost the model ability

   • TANet [99] formulates a multi-modal fusion framework                maps, and annotations) from these datasets. Moreover, we
using RGB images and depth maps from the bottom-up and                   provide the details for each dataset as follows.
top-down views. It then introduces a channel-wise attention                 • STERE [138]. The authors first collected 1,250 stereo-
module to effectively fuse the complementary information                 scopic images from Flickr 1 , NVIDIA 3D Vision Live 2 , and
from different modalities and levels.                                    Stereoscopic Image Gallery 3 . The most salient objects in each
                                                                         image were annotated by three users. All annotated images
                                                                         were then sorted based on the overlaping salient regions and
E. Open-source Implementations
                                                                         the top 1,000 images were selected to construct the final
   We summarize the open-source implementations of RGB-D                 dataset. This is the first collection of stereoscopic images in
based SOD models reviewed in this survey. The implemen-                  this field.
tations and hyperlinks of the source codes of these models                  • GIT [47] consists of 80 color and depth images, which
are provided in Tab V. More source codes will be updated at:             were collected using a mobile-manipulator robot in a real-
https://github.com/taozh2017/RGBD-SODsurvey.                             world home environment. Moreover, each image is annotated
                                                                         based on the pixel-level segmentation of the objects.
                    III. RGB-D DATASETS                                     • DES [49] consists of 135 indoor RGB-D images, which
  With the rapid development of RGB-D based SOD, various                 were taken by Kinect with a resolution of 640 × 640. When
datasets have been constructed over the past several years.               1 http://www.flickr.com/
Tab VI summarizes nine popular RGB-D datasets, and Fig. 4                 2 http://photos.3dvisionlive.com/

shows examples of images (including RGB images, depth                     3 http://www.stereophotography.com/
                                                                                                                                                                   7

                                                                TABLE IV
                                           S UMMARY OF RGB-D BASED SOD MODELS PUBLISHED IN 2020.
   No.   Year           Method     Pub.    Training Set     Backbone     Description
   65    2020     BiANet [120]      TIP    NLPR(0.7K),      VGG-16       Uses a bilateral attention module (BAM) to explore rich foreground and background
                                           NJUD(1.485K)                  information from depth maps
   66    2020   ASIF-Net [106]     TCYB    NLPR(0.65K),     VGG-16       Integrates the attention steered complementarity from RGB-D images and introduces
                                           NJUD(1.4K)                    a global semantic constraint using adversarial learning
   67    2020   Triple-Net [107]    SPL    Triple-Net       ResNe-18     Uses a triple-complementary network for RGB-D based SOD
   68    2020          ICNet [7]    TIP    Triple-Net       VGG-16       Uses a novel information conversion module to fuse high-level RGB and depth
                                                                         features in an interactive and adaptive way
   69    2020        SDF [108]      TIP    NLPR,NJUD,       VGG-16       Proposes a exemplar-driven method to estimate relatively trustworthy depth maps, and
                                           DEC,LFSD(1.5K)                uses a selective deep saliency fusion network to effectively integrate RGB images,
                                                                         original depths, and newly estimated depths
   70    2020      GFNet [121]      SPL    NLPR(0.8K),      Res2Net      Designs a gate fusion block to regularize feature fusion
                                           NJUD(1.588K)
   71    2020      RGBS [122]      MTAP    NLPR(0.65K),     VGG-16       Utilizes a GAN to generate the saliency map
                                           NJUD(1.4K)
   72    2020        D3 Net [3]    TNNLS   NLPR(0.7K),      VGG-16       Uses a depth depurator unit (DDU) and a three-stream feature learning module to
                                           NJUD(1.485K)                  employ low-quality depth cue filtering and cross-modal feature learning, respectively
   73    2020       JL-DCF [8]     CVPR    NLPR(0.7K),      VGG-16,      Uses a joint learning strategy and a densely-cooperative fusion module to achieve
                                           NJUD(1.5K)       ResNet-101   better SOD performance
   74    2020        A2dele [5]    CVPR    NLPR(0.7K),      VGG-16       Employs a depth distiller to explore ways of using network prediction and attention
                                           NJUD(1.485K)                  as two bridges to transfer depth knowledge to RGB images
   75    2020           SSF [4]    CVPR    NLPR(0.7K),      AGG-16       Designs a complimentary interaction module to select useful representations from the
                                           NJUD(1.485K),                 RGB and depth images and then integrate cross-modal features
                                           DUT(0.8K)
   76    2020        S2 MA [6]     CVPR    NLPR(0.65K),     VGG-16       Fuses multi-modal information via self-attention and each other’s attention strategies,
                                           NJUD(1.4K)                    and reweights the mutual attention term to filter out unreliable information
   77    2020       UC-Net [9]     CVPR    NLPR(0.7K),      VGG-16       Uses a probabilistic RGB-D saliency detection network via a conditional VAE to
                                           NJUD(1.5K)                    generate multiple saliency maps
   78    2020   CMWNet [123]       ECCV    NLPR(0.65K),     VGG-16       Exploits feature interactions using three cross-modal cross-scale weighting modules
                                           NJUD(1.4K)                    to improve SOD performance
   79    2020    HDFNet [124]      ECCV    NLPR(0.7K),      VGG-16       Designs a hierarchical dynamic filtering network to effectively make use of cross-
                                           NJUD(1.485K),                 modal fusion information
                                           DUT(0.8K)
   80    2020   CAS-GNN [125]      ECCV    NLPR(0.65K),     VGG-16       Designs cascaded graph neural networks to exploit useful knowledge from RGB and
                                           NJUD(1.4K)                    depth images for building powerful feature embeddings
   81    2020     CMMS [126]       ECCV    NLPR(0.7K),      VGG-16       Proposes a cross-modality feature modulation module to enhance feature represen-
                                           NJUD(1.485K)                  tations and an adaptive feature selection module to gradually select saliency-related
                                                                         features
   82    2020      DANet [127]     ECCV    NLPR(0.65K),     VGG-16,      Develops a single-stream network combined with a depth-enhanced dual attention to
                                           NJUD(1.4K)       VGG-19       achieve real-time SOD
   83    2020      CoNet [128]     ECCV    NLPR(0.7K),      ResNet       Develops a collaborative learning framework for RGB-D based SOD. Three col-
                                           NJUD(1.485K),                 laborators (edge detection, coarse salient object detection and depth estimation) are
                                           DUT(0.8K)                     utilized to jointly boost the performance
   84    2020    BBS-Net [129]     ECCV    NLPR(0.65K),     VGG-16,      Uses a bifurcated backbone strategy to learn teacher and student features, and utilizes
                                           NJUD(1.4K)       VGG-19,      a depth-enhanced module to excavate informative parts of depth cues
                                                            ResNet-50
   85    2020       ATSA [130]     ECCV    NLPR(0.7K),      VGG-19       Proposes an asymmetric two-stream architecture taking account of the inherent
                                           NJUD(1.485K),                 differences between RGB and depth data for SOD
                                           DUT(0.8K)
   86    2020      PGAR [131]      ECCV    NLPR(0.7K),      VGG-16       Propose a progressively guided alternate refinement network to produce a coarse
                                           NJUD(1.485K)                  initial prediction using a multi-scale residual block
   87    2020     MCINet [132]     arXiv   NLPR(0.65K),     ResNet-50    Develops a novel multi-level cross-modal interaction network for RGB-D SOD
                                           NJUD(1.4K)
   88    2020      DRLF [133]       TIP    NLPR(0.65K),     VGG-16       Develops a channel-wise fusion network to conduct multi-net and multi-level selective
                                           NJUD(1.4K)                    fusion for RGB-D SOD
   89    2020     DQAM [134]       arXiv   NLPR(0.65K),     Without      Proposes a depth quality assessment solution to conduct “quality-aware” SOD for
                                           NJUD(1.4K)                    RGB-D images
   90    2020      DQSD [135]       TIP    NLPR(0.65K),     VGG-19       Integrates a depth quality aware subnet into a bi-stream structure to assess the depth
                                           NJUD(1.4K)                    quality before conducting RGB-D fusion
   91    2020    DASNet [136]      ACM     NLPR(0.7K),      ResNet-50    Proposes a new perspective of containing the depth constraints in the learning process
                                   MM      NJUD(1.5K)                    rather than using depths as inputs
   92    2020      DCMF [137]       TIP    NLPR(0.65K),     VGG-16,      Designs a disentangled cross-modal fusion network to expose structural and content
                                           NJUD(1.4K)       ResNet-50    representations from RGB and depth images

collecting this dataset, three users were asked to label the              40 outdoor scenes. To label this dataset, three individuals
salient object in each image, and then the overlapping areas              were asked to manually segment salient regions, and then the
of the labeled object were regarded as the ground truth.                  segmented results were deemed ground truth when the overlap
                                                                          of the three results was over 90%.
  • NLPR [51] consists of 1,000 RGB images and their
                                                                            • NJUD [56] consists of 1,985 stereo image pairs, and
corresponding depth maps, which were obtained by a standard
                                                                          these images were collected from the internet, 3D movies,
Microsoft Kinect. This dataset includes a series of outdoor and
                                                                          and photographs that are taken by a Fuji W3 stereo camera.
indoor locations, e.g., offices, supermarkets, campuses, streets,
                                                                            • SSD [85] was constructed using three stereo movies and
and so on.
                                                                          includes indoor and outdoor scenes. This dataset includes 80
  • LFSD [139] includes 100 light fields collected using                  samples, and each image has the size of 960 × 1080.
a Lytro light field camera, and consists of 60 indoor and                   • DUT-RGBD [98] consists of 800 indoor and 400 outdoor
                                                                                                                                                  8

                  (a) STERE                                        (b) NLPR                                          (c) SSD

                    (d) GIT                                         (e) DES                                          (f) LFSD

                   (g) NJUD                                    (h) DUT-RGBD                                          (i) SIP
Fig. 4. Examples of images, depth maps and annotations in nine RGB-D dataset, including (a) STERE [138], (b) NLPR [51], (c) SSD [85], (d) GIT [47],
(e) DES [49] , (f) LFSD [139], (g) NJUD [56], (h) DUT-RGBD [98], and (i) SIP [3]. In each dataset, the RGB image, depth map and annotation are shown
from left to right.

scenes with their corresponding depth images. This dataset                 provide layout information to improve SOD performance to
includes several challenging factors, i.e., multiple or trans-             some extent. However, inaccurate or low-quality depth maps
parent objects, complex backgrounds, similar foregrounds and               often decrease the performance. To overcome this issue, light
backgrounds, and low-intensity environments.                               field SOD methods have been proposed to make use of rich
   • SIP [3] consists of 929 annotated high-resolution images,             information captured by the light field. Specifically, light
with multiple salient persons in each image. In this dataset,              field data contains an all-focus image, a focal stack, and a
depth maps were captured using a real smartphone (i.e.,                    rough depth map [98]. A summary of related light field SOD
Huawei Mate10). Besides, it is worth noting that this dataset              works is provided in Tab VII. Further, to provide an in-depth
covers diverse scenes, and various challenging factors, and is             understanding of these models, we also review them in more
annotated with pixel-level ground truths.                                  detail as follows.
   Note that a detailed dataset statistics analysis (including cen-
ter bias, size of objects, background objects, object boundary                Traditional/Deep Models. The classic models for light
conditions, and number of salient objects) can be found in [3].            field SOD often use superpixel-level handcrafted features [98],
                                                                           [139], [141]–[146], [148], [154]. Early work [139], [146]
        IV. S ALIENCY D ETECTION ON L IGHT F IELD                          showed that the unique refocusing capability of light fields
                                                                           can provide useful focusness, depth, and objectness cues.
A. Light Field SOD Models                                                  Thus, several SOD models using light field data were further
  Existing works for SOD can be grouped into three cate-                   proposed. For example, Zhang et al. [142] utilized a set
gories according to the input data type, including RGB SOD,                of focal slices to compute the background prior, and then
RGB-D SOD, and light field SOD [155]. We have already                      combined it with the location prior for SOD. Wang et al. [145]
reviewed RGB-D based SOD models, in which depth maps                       proposed a two-stage Bayesian fusion model to integrate
                                                                                                                                                                     9

                                                                   TABLE V
                                     A SUMMARY OF RGB-D BASED SOD MODELS WITH OPEN - SOURCE IMPLEMENTATIONS .

   Year             Model                   Implementation           Code link
                    LHM [51]                Matlab                   https://sites.google.com/site/rgbdsaliency/code
   2014
                    DESM [49]               Matlab                   https://github.com/HzFu/DES code
   2015             GP [50]                 Matlab                   https://github.com/JianqiangRen/Global Priors RGBD Saliency Detection
                    DCMC [1]                Matlab                   https://github.com/rmcong/Code-for-DCMC-method
   2016
                    LBE [57]                Matlab & C++             http://users.cecs.anu.edu.au/ u4673113/lbe.html
                    BED [83]                Caffe                    https://github.com/sshige/rgbd-saliency
                    CDCP [84]               Matlab                   https://github.com/ChunbiaoZhu/ACVR2017
   2017
                    MDSF [87]               Matlab                   https://github.com/ivpshu
                    DF [52]                 Matlab                   https://pan.baidu.com/s/1Y-PqAjuH9xREBjfl7H45HA
                    CTMF [58]               Caffe                    https://github.com/haochen593/CTMF
   2018
                    PCF [92]                Caffe                    https://github.com/haochen593/PCA-Fuse RGBD CVPR18
                    PDNet [97]              TensorFlow               https://github.com/cai199626/PDNet
                    AFNet [102]             TensorFlow               https://github.com/Lucia-Ningning/Adaptive Fusion RGBD Saliency Detection
   2019             CPFP [53]               Caffe                    https://github.com/JXingZhao/ContrastPrior
                    DMRA [54]               PyTorch                  https://github.com/jiwei0921/DMRA
                    DGT [101]               Matlab                   https://github.com/rmcong/Code-for-DTM-Method
                    ICNet [7]               Caffe                    https://github.com/MathLee/ICNet-for-RGBD-SOD
                    JL-DCF [8]              Pytorch, Caffe           https://github.com/kerenfu/JLDCF
                    A2dele [5]              PyTorch                  https://github.com/OIPLab-DUT/CVPR2020-A2dele
                    SSF [4]                 PyTorch                  https://github.com/OIPLab-DUT/CVPR SSF-RGBD
                    ASIF-Net [106]          TensorFlow               https://github.com/Li-Chongyi/ASIF-Net
                    S2 MA [6]               PyTorch                  https://github.com/nnizhang/S2MA
                    UC-Net [9]              PyTorch                  https://github.com/JingZhang617/UCNet
                    D3 Net [3]              PyTorch                  https://github.com/DengPingFan/D3NetBenchmark
   2020
                    CMWNet [123]            Caffe                    https://github.com/MathLee/CMWNet
                    HDFNet [124]            PyTorch                  https://github.com/lartpang/HDFNet
                    CMMS [126]              TensorFlow               https://github.com/Li-Chongyi/cmMS-ECCV20
                    CAS-GNN [125]           PyTorch                  https://github.com/LA30/Cas-Gnn
                    DANet [127]             PyTorch                  https://github.com/Xiaoqi-Zhao-DLUT/DANet-RGBD-Saliency
                    CoNet [128]             PyTorch                  https://github.com/jiwei0921/CoNet
                    DASNet [136]            PyTorch                  http://cvteam.net/projects/2020/DASNet/
                    BBS-Net [129]           PyTorch                  https://github.com/DengPingFan/BBS-Net
                    ATSA [130]              PyTorch                  https://github.com/sxfduter/ATSA
                    PGAR [131]              PyTorch                  https://github.com/ShuhanChen/PGAR ECCV20
                    FRDT [140]              PyTorch                  https://github.com/jack-admiral/ACM-MM-FRDT

                                                                  TABLE VI
S TATISTICS OF NINE RGB-D BENCHMARK DATASETS IN TERMS OF YEAR (Y EAR ), PUBLICATION (P UB .), DATASET SIZE (S IZE ), NUMBER OF OBJECTS IN
 THE IMAGES (#O BJ .), TYPE OF SCENE (T YPES ), DEPTH SENSOR (S ENSOR ), AND RESOLUTION (R ESOLUTION ). S EE § III FOR MORE DETAILS ON EACH
                  DATASET. T HESE DATASETS CAN BE DOWNLOADED FROM OUR WEBSITE : HTTP :// DPFAN . NET / D 3 NETBENCHMARK /.
   #      Dataset                    Year      Pub.          Size     #Obj.       Types                        Sensor                        Resolution
   1      STERE [138]                2012      CVPR          1,000    ∼One        Internet                     Stereo camera+sift flow       [251 ∼ 1200] × [222 ∼
                                                                                                                                             900]
   2      GIT [47]                   2013      BMVC          80       Multiple    Home environment             Microsoft Kinect              640 × 480
   3      DES [49]                   2014      ICIMCS        135      One         Indoor                       Microsoft Kinect              640 × 480
   4      NLPR [51]                  2014      ECCV          1,000    Multiple    Indoor/outdoor               Microsoft Kinect              640 × 480, 480 × 640
   5      LFSD [139]                 2014      CVPR          100      One         Indoor/outdoor               Lytro Illum camera            360 × 360
   6      NJUD [56]                  2014      ICIP          1,985    ∼One        Movie/internet/photo         FujiW3 camera+optical flow    [231 ∼ 1213] × [274 ∼
                                                                                                                                             828]
   7      SSD [85]                   2017      ICCVW         80       Multiple    Movies                       Sun’s optical flow            960 × 1080
   8      DUT-RGBD [98]              2019      ICCV          1,200    Multiple    Indoor/outdoor               –                             400 × 600
   9      SIP [3]                    2020      TNNLS         929      Multiple    Person in the wild           Huawei Mate10                 992 × 744

multiple contrasts for boosting SOD performance. Recently,                                    model robustness. Zhang et al. [152] developed a memory-
several deep learning-based light field SOD models [150]–                                     oriented decoder for light field SOD, which fuses multi-level
[153], [155], [156] have also been developed, obtaining re-                                   features in a top-down manner using high-level information
markable performance. Besides, in [150], an attentive recurrent                               to guide low-level feature selection. LFNet [155] employs
CNN was developed to fuse all focal slices, while the data                                    a new integration module to fuse features from light field
diversity was increased using adversarial examples to enhance                                 data according to their contributions and captures the spatial
                                                                                                                                                                            10

                                                                         TABLE VII
                                                        S UMMARY OF POPULAR LIGHT FIELD SOD METHODS .
     No.   Year          Method      Pub.     Dataset                        Description
     1     2014       LFS [139]     CVPR      LFSD                           The first light-field saliency detection algorithm employs objectness and focusness cues
                                                                             based on the refocusing capability of the light field
     2     2015      WSC [141]      CVPR      LFSD                           Uses a weighted sparse coding framework to learn a saliency/non-saliency dictionary
     3     2015      DILF [142]     IJCAI     LFSD                           Incorporates depth contrast to complement the disadvantage of color and conducts
                                                                             focusness-based background priors to boost the saliency detection performance
     4     2016        RL [143]    ICASSP     LFSD                           Utilizes the inherent structure information in light field images to improve saliency
                                                                             detection
     5     2017        MA [144]    TOMM       HFUT, LFSD                     Integrates multiple saliency cues extracted from light field images using a random-search-
                                                                             based weighting strategy
     6     2017        BIF [145]     NPL      LFSD                           Integrates color-based contrast, depth-induced contrast, focusness map of foreground slice,
                                                                             and background weighted depth contrast using a two-stage Bayesian integration framework
     7     2017       LFS [146]    TPAMI      LFSD                           An extension of [139]
     8     2017      RLM [147]     ICIVC      LFSD                           Utilizes the light field relative location measurement for SOD on light field images
     9     2018     SGDC [148]     CVPR       LFSD                           Designs a saliency-guided depth optimization framework for multi-layer light field displays
     10    2018      DCA [149]      FiO       LFSD                           Proposes a graph model depth-induced cellular automata to optimize saliency maps using
                                                                             light field data
     11    2019      DLLF [150]     ICCV      DUTLF-FS, LFSD                 Utilizes a recurrent attention network to fuse each slice from the focal stack to learn the
                                                                             most informative features
     12    2019     DLSD [151]      IJCAI     DUTLF-MV                       Formulates saliency detection into two subproblems, including 1) light field synthesis from
                                                                             a single view and 2) light-field-driven saliency detection
     13    2019      Molf [152]     NIPS      UTLF-FS                        Uses a memory-oriented decoder for light field SOD
     14    2020     ERNet [153]     AAAI      DUTLF-FS, HFUT, LFSD           Uses an asymmetrical two-stream architecture to overcome computation-intensive and
                                                                             memory-intensive challenges in a high-dimensional light field data
     15    2020        DCA [98]      TIP      LFSD                           Presents a saliency detection framework on light fields based on the depth-induced cellular
                                                                             automata (DCA) model. It can enforce spatial consistency to optimize the inaccurate
                                                                             saliency map using the DCA model
     16    2020     RDFD [154]      MTAP      LFSD                           Defines a region-based depth feature descriptor extracted from the light field focal stack
                                                                             to facilitate low- and high-level cues for saliency detection
     17    2020     LFNet [155]      TIP      DUTLF-FS, LFSD, HFUT           Utilizes a light field refinement module and a light field integration module to effectively
                                                                             integrate multiple cues (i.e., focusness, depths and objectness) from light field images
     18    2020    LFDCN [156]       TIP      Lytro Illum, LFSD, HFUT        Uses a deep convolutional network based on the modified DeepLab-v2 model to explore
                                                                             spatial and multi-view properties of light field images for saliency detection

structure of a scene to improve SOD performance.                                        • DUTLF-FS [150] 6 consists of 1,465 samples, 1,000
   Refinement based Models. Several refinement strategies                            of which are used as the training set, while the remaining
have been used to enforce neighboring constraints or reduce                          465 images make up the test set. The resolution of each
the homogeneity of multiple modalities for SOD. For exam-                            image is 600 × 400. This dataset contains several challenges,
ple, in [141], the saliency dictionary was refined using the                         including lower contrast between salient objects and cluttered
estimated saliency map. The MA method [144] employs a                                background, multiple disconnected salient objects, and dark or
two-stage saliency refinement strategy to produce the final                          strong light conditions.
prediction map, which enables adjacent superpixels to obtain                            • DUTLF-MV [151] 7 consists of 1,580 samples, 1,100 of
similar saliency values. Besides, LFNet [155] presents an                            which are for training and the remaining is for testing. Images
effective refinement module to reduce the homogeneity among                          were captured by a Lytro Illum camera, and each light field
different modalities as well refine their dissimilarities                            consists of multi-view images and a corresponding ground
                                                                                     truth.
B. Light Field Data for SOD                                                             • Lytro Illum [156] 8 consists of 640 light fields and
                                                                                     the corresponding per-pixel ground-truth saliency maps. It
   There are five representative datasets widely used in existing                    includes several challenging factors, e.g., inconsistent illumi-
light field SOD models. We describe the details of each dataset                      nation conditions, and small salient objects existing in a similar
as follows.                                                                          or cluttered background.
   • LFSD [139] 4 consists of 100 light fields of different
scenes with a 360 × 360 spatial resolution, captured using a
Lytro light field camera. This dataset contains 60 indoor and                                      V. M ODEL E VALUATION AND A NALYSIS
40 outdoor scenes, and most scenes consist of only one salient
object. Besides, three individuals were asked to manually                            A. Evaluation Metrics
segment salient regions in each image, and then the ground
truth was determined when all three segmentation results had                            We briefly review several popular metrics for SOD evalu-
an overlap of over 90%.                                                              ation, i.e., precision-recall (PR), F-measure [59], [157], mean
   • HFUT [144] 5 consists of 255 light fields captured using                        absolute error (MAE) [158], structural measure (S-measure)
a Lytro camera. In this dataset, most scenes contain multiple                        [159], and enhanced-alignment measure (E-measure) [160].
objects that appear within different locations and scales under
complex background clutter.                                                             6 https://github.com/OIPLab-DUT/ICCV2019 Deeplightfield Saliency
                                                                                        7 https://github.com/OIPLab-DUT/IJCAI2019-Deep-Light-Field-Driven-
  4 https://sites.duke.edu/nianyi/publication/saliency-detection-on-light-field/     Saliency-Detection-from-A-Single-View
  5 https://github.com/pencilzhang/HFUT-Lytro-dataset                                  8 https://github.com/pencilzhang/MAC-light-field-saliency-net
           0922
                                                                                                                                                        11

     0.9               JL-DCF
                       UCNet
                         SSFS2MA
                             ICNet
                            D3Net
                             CPFP
                                   PCF
    0.85                  A2dele TANet        MMCI

                                     DMRA

     0.8                                                     CTMF
                                                     AFNet

    0.75
              0.9
S

                                                                            DF
                        JL-DCF
                                                                                 DCMC           ACSD
     0.7
            0.895
                         UCNet                                                                               LBE
                                                                       SE
             0.89                                                                        CDCP
                                        S2MA
    0.65
                                           ICNet
            0.885                 SSF
                                            D3Net
                                                                                         GP                                                   DESM
     0.6     0.88
                0.04      0.045      0.05    0.055
                                                                                   CDB
                                                                                    LHM
    0.55
             0.04 0.06 0.08                    0.1                                                     0.2                                       0.3
                                                                                   MAE

Fig. 5. A comprehensive evaluation for 24 representative RGB-D based SOD models, including LHM [51], ACSD [56], DESM [49], GP [50], LBE [57],
DCMC [1], SE [2], CDCP [84], CDB [95], DF [52], PCF [92], CTMF [58], CPFP [53], TANet [99], AFNet [102], MMCI [55], DMRA [54], D3 Net [3],
SSF [4], A2dele [5], S2 MA [6], ICNet [7], JL-DCF [8], and UC-Net [9]. We report the mean values of Sα and MAE across the five datasets (i.e., STERE
[138], NLPR [51], LFSD [139], DES [49], and SIP [3]) in each model. Note that better models are shown in the upper left corner (i.e., with a larger Sα and
smaller MAE). Here, red diamonds denote deep models and green circles denote traditional models.

  • PR. Given a saliency map S, we can convert it to a                              where α ∈ [0, 1] is a trade-off parameter. Here, we set α =
binary mask M , and then compute the precision and recall                           0.5 as the default setting, as suggested by Fan et al. [159].
by comparing M with ground-truth G:                                                    • E-measure (Eφ ). Eφ [160] was proposed based on cog-
                                        |M ∩ G|            |M ∩ G|                  nitive vision studies to capture image-level statistics and their
            P recision =                        , Recall =         .         (1)    local pixel matching information. Thus, Eφ can be defined by
                                          |M |               |G|
   A popular strategy is to partition the saliency map S                                                            W X H
                                                                                                               1   X
using a set of thresholds (i.e., it changes from 0 to 255).                                             Eφ =               φF M (i, j) ,               (5)
                                                                                                             W ∗ H i=1 i=1
For each threshold, we first calculate a pair of recall and
precision scores, and then combine them to obtain a PR curve                        where φF M denotes the enhanced-alignment matrix [160].
that describes the performance of the model at the different
thresholds.
   • F-measure (Fβ ). To comprehensively consider both pre-                         B. Performance Comparison and Analysis
cision and recall, the F-measure is proposed by calculating the                        1) Overall Evaluation: To quantify the performance of
weighted harmonic mean:                                                             different models, we conduct a comprehensive evaluation of 24
                                 P ∗R                                              representative RGB-D based SOD models, including 1) nine
                   Fβ = 1 + β 2 2           ,               (2)
                                   β P +R                                           traditional methods: LHM [51], ACSD [56], DESM [49], GP
where β 2 is set to 0.3 to emphasize the precision [157]. We use                    [50], LBE [57], DCMC [1], SE [2], CDCP [84], CDB [95]; and
different fixed [0, 255] thresholds to compute the F -measure                       2) fifteen deep learning-based methods: DF [52], PCF [92],
metric. This yields a set of F -measure values for which we                         CTMF [58], CPFP [53], TANet [99], AFNet [102], MMCI
report the maximal or average Fβ .                                                  [55], DMRA [54], D3 Net [3], SSF [4], A2dele [5], S2 MA
   • MAE. This measures the average pixel-wise absolute error                       [6], ICNet [7], JL-DCF [8], and UC-Net [9]. We report the
between a predicted saliency map S and a ground truth G for                         mean values of Sα and MAE across the five datasets (STERE
all pixels, which can be defined by                                                 [138], NLPR [51] , LFSD [139], DES [49], and SIP [3]) for
                                                                                    each model in Fig. 5. It is worth noting that better models
                                           W X H
                                      1   X                                         are shown in the upper left corner (i.e., with a larger Sα and
                    M AE =                        |Si,j − Gi,j | ,           (3)    smaller MAE). From Fig. 5, we have following observations:
                                    W ∗ H i=1 i=1
                                                                                       • Traditional vs. Deep Models. Compared with traditional
where W and H denote the width and height of the map,
                                                                                          RGB-D based SOD models, deep learning methods ob-
respectively. MAE values are normalized to [0,1].
                                                                                          tain significantly better performance. This confirms the
   • S-measure (Sα ). To capture the importance of the struc-
                                                                                          powerful feature learning ability of deep networks.
tural information in an image, Sα [159] is used to assess the
                                                                                       • Comparison of Deep Models. Among the deep learning-
structural similarity between the regional perception (Sr ) and
                                                                                          based models, D3 Net [3], JL-DCF [8], UC-Net [9], SSF
object perception (So ). Thus, Sα can be defined by
                                                                                          [4], ICNet [7], and S2 MA [6] obtain the best perfor-
                           Sα = α ∗ So + (1 − α) ∗ Sr ,                      (4)          mance.
                                                                                                                                                                                                                                                                                                                                                                                                            12

                      1                                                                                                                       1                                                                                                                                                 1

1122                 0.8                                                                                                                    0.8                                                                                                                                            0.8

                                                                                                                                Precision

                                                                                                                                                                                                                                                                               Precision
                                                                                                                                            0.6                                                                                                                                            0.6
         Precision

                     0.6

                     0.4                                                                                                                    0.4                                                                                                                                            0.4

                     0.2                                                                                                                    0.2                                                                                                                                            0.2

                               STERE                                                                                                                      NLPR                                                                                                                                             LFSD
                      0                                                                                                                       0                                                                                                                                                 0
                           0               0.2              0.4               0.6                 0.8                     1                       0                    0.2             0.4                       0.6                0.8                       1                                        0                0.2                  0.4               0.6                       0.8                1
                                                                  Recall                                                                                                                          Recall                                                                                                                                         Recall
                      1                                                                                                                       1                                                                                                                                                1

                     0.8                                                                                                                    0.8                                                                                                                                           0.8
        Precision

                                                                                                                                Precision

                                                                                                                                                                                                                                                                              Precision
                     0.6                                                                                                                    0.6                                                                                                                                           0.6

                     0.4                                                                                                                    0.4                                                                                                                                           0.4

                     0.2                                                                                                                    0.2                                                                                                                                           0.2

                               DES                                                                                                                        SIP                                                                                                                                              GIT
                      0                                                                                                                       0                                                                                                                                                0
                           0               0.2              0.4               0.6                 0.8                     1                       0                    0.2             0.4                       0.6                0.8                       1                                    0                    0.2                0.4                 0.6                   0.8                    1
                                                               Recall                                                                                                                             Recall                                                                                                                                         Recall
                      1                                                                                                                      1

                                                                                                                                                                                                                                                                                                                              LHM                                       CPFP
                     0.8                                                                                                                    0.8                                                                                                                                                                               ACSD                                      TANet
                                                                                                                                                                                                                                                                                                                              DESM                                      AFNet
                                                                                                                                                                                                                                                                                                                              GP                                        MMCI
                                                                                                                               Precision
        Precision

                     0.6                                                                                                                    0.6
                                                                                                                                                                                                                                                                                                                              LBE                                       DMRA
                                                                                                                                                                                                                                                                                                                              DCMC                                      D3Net
                     0.4                                                                                                                    0.4                                                                                                                                                                               SE                                        SSF
                                                                                                                                                                                                                                                                                                                              CDCP                                      A2dele
                                                                                                                                                                                                                                                                                                                              CDB                                       S2MA
                     0.2                                                                                                                    0.2
                                                                                                                                                                                                                                                                                                                              DF                                        ICNet
                               SSD                                                                                                                    NJUD                                                                                                                                                                    PCF                                       JL-DCF
                      0                                                                                                                      0                                                                                                                                                                                CTMF                                      UCNet
                           0               0.2              0.4               0.6                 0.8                     1                       0                    0.2             0.4                       0.6                0.8                       1
                                                               Recall                                                                                                                         Recall
       Fig. 6. PR curves for 24 RGB-D based models on the STERE [138], NLPR [51], LFSD [139], DES [49], SIP [3], GIT [47], SSD [85], and NJUD [56]
       datasets.

                                                                      TABLE VIII
                                                                           0
          ATTRIBUTE - BASED STUDY w.r.t. SALIENT OBJECT SCALES . C OMPARISON 0RESULTS
                                                                                200 FOR 24 REPRESENTATIVE RGB-D BASED SOD MODELS (9
       TRADITIONAL MODELS AND 15 DEEP LEARNING - BASED MODELS ) ARE PROVIDED IN TERMS OF MAE AND Sα . T HE THREE BEST RESULTS ARE SHOWN
                                                           IN RED , BLUE AND GREEN FONTS .
                                                                                      Traditional models                                                                                                                                        Deep learning-based models
                                                                                                                                                                                                                                                AFNet [102]

                                                                                                                                                                                                                                                                                           DMRA [54]
                                                                          DESM [49]

                                                                                                                                                                                                                                                                  MMCI [55]

                                                                                                                                                                                                                                                                                                                                                                            JL-DCF [8]
                                                                                                                                                                                                     CTMF [58]

                                                                                                                                                                                                                                   TANet [99]

                                                                                                                                                                                                                                                                                                                                                                                               UC-Net [9]
                                                              ACSD [56]

                                                                                                                                              CDCP [84]
                                                                                                               DCMC [1]

                                                                                                                                                                                                                                                                                                                                    A2dele [5]
                                                                                                                                                                                                                       CPFP [53]

                                                                                                                                                                                                                                                                                                           D3 Net [3]

                                                                                                                                                                                                                                                                                                                                                   S2 MA [6]
                                                 LHM [51]

                                                                                                                                                            CDB [95]

                                                                                                                                                                                                                                                                                                                                                                ICNet [7]
                                                                                                    LBE [57]

                                                                                                                                                                                       PCF [92]
                                                                                        GP [50]

                                                                                                                                                                             DF [52]

                                                                                                                                                                                                                                                                                                                          SSF [4]
                                                                                                                              SE [2]
                                   Scale

                                 Small  .065 .149 .319 .098 .177 .108 .056 .128 .073 .087 .042 .065 .044 .041 .046 .051 .030 .033 .031 .032 .035 .036 .032 .034
                           MAE

                                 Medium .178 .183 .287 .180 .210 .158 .150 .173 .179 .152 .068 .107 .055 .067 .095 .079 .069 .053 .045 .054 .052 .052 .041 .042
                                 Large           .403 .311 .310 .377 .261 .305 .364 .308 .385 .310 .112 .183 .093 .118 .213 .130 .181 .102 .105 .114 .088 .104 .085 .072
                                 Overall         .166 .184 .296 .173 .206 .156 .142 .171 .167 .147 .065 .102 .055 .065 .091 .076 .067 .052 .046 .053 .051 .052 .041 .042
                                 Small  .624 .668 .517 .650 .645 .700 .775 .661 .666 .745 .847 .789 .840 .846 .792 .832 .860 .879 .876 .859 .877 .882 .881 .883
                                 Medium .543 .732 .658 .598 .723 .727 .676 .683 .585 .730 .863 .805 .877 .862 .779 .859 .838 .888 .893 .865 .893 .892 .906 .901
                           Sα

                                 Large           .386 .630 .686 .450 .731 .604 .479 .586 .424 .597 .838 .761 .855 .827 .682 .830 .734 .846 .837 .815 .863 .845 .859 .876
                                 Overall         .552 .710 .626 .601 .705 .712 .686 .671 .593 .725 .857 .798 .867 .856 .776 .851 .836 .883 .885 .860 .887 .886 .897 .895

         Moreover, Fig. 6 and Fig. 7 show the PR and F-measure                                                                                                                                      for NLPR, LFSD, DES, SIP, GIT, and SSD, respectively. For
       curves for the 24 representative RGB-D based SOD models                                                                                                                                      the NJUD [56] dataset, there are 485 test images for CPFP
       on eight datasets (i.e., STERE [138], NLPR [51], LFSD [139],                                                                                                                                 [53], S2 MA [6], ICNet [7], JL-DCF [8], and UC-Net [9], while
       DES [49], SIP [3], GIT [47], SSD [85] , and NJUD [56]). Note                                                                                                                                 498 testing images for all other models.
       that there are 1000, 300, 100, 135, 929, 80, and 80 test samples
                                                                                                                                                                                                                 To understand the top six models in depth, we discuss their
                                                                                                                                                                                                                                                                                                                                                                                            13

                    1                                                                                                                        1                                                                                                                              1

1122               0.8                                                                                                                     0.8                                                                                                                            0.8
       F-measure

                                                                                                                               F-measure

                                                                                                                                                                                                                                                              F-measure
                   0.6                                                                                                                     0.6                                                                                                                            0.6

                   0.4                                                                                                                     0.4                                                                                                                            0.4

                   0.2                                                                                                                     0.2                                                                                                                            0.2

                             STERE                                                                                                                      NLPR                                                                                                                            LFSD
                    0                                                                                                                        0                                                                                                                              0
                         0                    50          100               150                  200              250                            0                   50               100              150                  200                250                              0                     50             100                      150               200                       250
                                                              Threshold                                                                                                               Threshold                                                                                                                       Threshold
                    1                                                                                                                        1                                                                                                                             1

                   0.8                                                                                                                     0.8                                                                                                                            0.8
       F-measure

                                                                                                                               F-measure

                                                                                                                                                                                                                                                             F-measure
                   0.6                                                                                                                     0.6                                                                                                                            0.6

                   0.4                                                                                                                     0.4                                                                                                                            0.4

                   0.2                                                                                                                     0.2                                                                                                                            0.2

                             DES                                                                                                                      SIP                                                                                                                               GIT
                    0                                                                                                                        0                                                                                                                             0
                         0                    50          100               150                  200              250                            0                   50               100              150                  200                250                              0                     50             100                      150               200                       250
                                                              Threshold                                                                                                               Threshold                                                                                                                      Threshold
                    1                                                                                                                       1
                                                                                                                                                                                                                                                                                                       LHM                                          CPFP
                   0.8                                                                                                                     0.8                                                                                                                                                         ACSD                                         TANet
                                                                                                                                                                                                                                                                                                       DESM                                         AFNet
                                                                                                                                                                                                                                                                                                       GP                                           MMCI
                                                                                                                              F-measure
       F-measure

                   0.6                                                                                                                     0.6
                                                                                                                                                                                                                                                                                                       LBE                                          DMRA
                                                                                                                                                                                                                                                                                                       DCMC                                         D3Net
                   0.4                                                                                                                     0.4                                                                                                                                                         SE                                           SSF
                                                                                                                                                                                                                                                                                                       CDCP                                         A2dele
                                                                                                                                                                                                                                                                                                       CDB                                          S2MA
                   0.2                                                                                                                     0.2
                                                                                                                                                                                                                                                                                                       DF                                           ICNet
                             SSD                                                                                                                     NJUD                                                                                                                                              PCF                                          JL-DCF
                    0                                                                                                                       0                                                                                                                                                          CTMF                                         UCNet
                         0                    50          100               150                  200              250                            0                   50               100             150                   200               250
                                                              Threshold                                                                                                               Threshold

       Fig. 7. F-measures under different thresholds for 24 RGB-D based models on the STERE [138], NLPR [51], LFSD [139], DES [49], SIP [3], GIT [47], SSD
       [85], and NJUD [56] datasets.

                                                                         0
                                                                     TABLE0 IX
                                                                             200
           ATTRIBUTE - BASED STUDY w.r.t. BACKGROUND CLUTTER . C OMPARISON RESULTS FOR 24 REPRESENTATIVE RGB-D BASED SOD MODELS (9
       TRADITIONAL MODELS AND 15 DEEP LEARNING - BASED MODELS ) ARE PROVIDED IN TERMS OF MAE AND Sα . T HE THREE BEST RESULTS ARE SHOWN
                                                         IN RED , BLUE AND GREEN FONTS .
                                                                                         Traditional models                                                                                                                                Deep learning-based models
                                                                                                                                                                                                                                           AFNet [102]

                                                                                                                                                                                                                                                                            DMRA [54]
                                                                             DESM [49]

                                                                                                                                                                                                                                                         MMCI [55]

                                                                                                                                                                                                                                                                                                                                                                JL-DCF [8]
                                                                                                                                                                                                    CTMF [58]
                                 background

                                                                                                                                                                                                                              TANet [99]

                                                                                                                                                                                                                                                                                                                                                                             UC-Net [9]
                                                                ACSD [56]

                                                                                                                                                     CDCP [84]
                                                                                                                   DCMC [1]

                                                                                                                                                                                                                                                                                                                     A2dele [5]
                                                                                                                                                                                                                CPFP [53]

                                                                                                                                                                                                                                                                                         D3 Net [3]

                                                                                                                                                                                                                                                                                                                                  S2 MA [6]
                                                   LHM [51]

                                                                                                                                                                 CDB [95]

                                                                                                                                                                                                                                                                                                                                                    ICNet [7]
                                                                                                       LBE [57]

                                                                                                                                                                                        PCF [92]
                                                                                           GP [50]

                                                                                                                                                                            DF [52]

                                                                                                                                                                                                                                                                                                           SSF [4]
                                                                                                                                 SE [2]

                              Simple               .100         .163        .219          .150         .202       .056         .084              .028            .136       .045       .031         .053        .018         .033          .031          .041               .028         .017              .012      .010         .016              .013        .014         .013
                     MAE

                             Uncertain             .164         .195        .294          .175         .210       .140         .133              .139            .159       .129       .062         .081        .050         .059          .075          .070               .058         .045              .043      .043         .049              .041        .037         .037
                             Complex               .159         .190        .349          .180         .205       .190         .147              .236            .143       .163       .085         .110        .079         .077          .108          .094               .087         .071              .065      .070         .072              .079        .063         .065
                              Overall              .160         .193        .295          .174         .209       .140         .132              .141            .157       .127       .063         .082        .051         .059          .076          .070               .059         .046              .043      .043         .049              .043        .038         .038
                              Simple               .781         .787        .761          .694         .748       .930         .856              .941            .704       .944       .944         .913        .958         .937          .922          .933               .935         .960              .966      .965         .965              .969        .961         .962
                             Uncertain             .572         .694        .638          .606         .695       .736         .723              .727            .610       .774       .873         .853        .882         .873          .818          .868               .854         .900              .894      .884         .895              .910        .909         .907
                     Sα

                             Complex               .496         .627        .509          .545         .616       .577         .605              .487            .575       .627       .782         .742        .787         .790          .694          .768               .751         .822              .815      .786         .813              .808        .829         .833
                              Overall              .576         .693        .633          .606         .691       .732         .720              .718            .612       .770       .869         .847        .878         .869          .813          .863               .850         .896              .891      .879         .892              .904        .904         .904

       main advantages for the six models below.                                                                                                                                                   representations for RGB and depth images, respectively, while
                             3
          • D Net [3] consists of two key components, i.e., a                                                                                                                                      the RgbdNet is used to learn their fused representations. It is
       three-stream feature learning module and a depth depurator                                                                                                                                  worth noting that this three-stream feature learning module can
       unit. In the three-stream feature learning module, there are                                                                                                                                capture modality-specific information as well as the correlation
       three subnetworks, i.e., RgbNet, RgbdNet, and DepthNet. The                                                                                                                                 between modalities. Thus, balancing the two aspects is very
       RgbNet and DepthNet are used to learn high-level feature                                                                                                                                    important for multi-modal learning and it has helped to im-
                                                                                                                                           14

prove the SOD performance. Besides, the depth depurator unit                           0.0502               0.0787               0.0981
acts as a gate to explicitly filter out low-quality depth maps,

                                                                       Small
which several existing methods do not consider the effects.
Because low-quality depth maps can inhibit the fusion between
RGB images and depth maps, thus the depth depurator unit
can ensure effective multi-modal fusion to achieve robust SOD                          0.2857               0.2229               0.2262
performance.

                                                                       Medium
   • In JL-DCF [8], there are two key components, i.e., a
joint learning (JL) and a densely-cooperative fusion (DCF).
Specifically, the JL module is used to learn robust saliency
features, while the DCF module is used for complementary                               0.5245               0.4168                0.4417
feature discovery. It is worth noting that this method uses

                                                                       Large
a middle-fusion strategy to extract deep hierarchical features
from RGB images and depth maps, in which the cross-
modal complementarity can be effectively exploited to achieve
accurate prediction.                                                Fig. 8. Sample images with different objects scales. The scale ratios are
   • In UC-Net [9], instead of producing a single saliency pre-     denoted in yellow.
diction, this model produces multiple predictions by modeling
the distribution of the feature output space as a generative
model conditioned on RGB-D images. Because each person              formance, overcoming the limitations of the original self-
has some specific preferences in labeling a saliency map, it        attention, which only uses a single modality. Besides, to reduce
could fail to capture the stochastic characteristic of saliency     the low-quality (e.g., noise) effects of depth cues, a selection
while only a single saliency map is produced for an image           mechanism is proposed to reweight the mutual attention. This
pair using a deterministic learning pipeline. Thus, the strategy    mechanism can filter out unreliable information, resulting in
in this model can take into account human uncertainty in            more accurate saliency prediction.
saliency annotations. Moreover, considering the fact that depth        2) Attribute-based Evaluation: To investigate the influence
maps could suffer from noise, directly fusing RGB images            of different factors, such as object scale, background clutter,
and depth maps could cause the network to fit to this noise.        number of salient objects, indoor or outdoor scene, background
Therefore, a depth correction network, designed as an auxiliary     objects, and lighting conditions, we carry out diverse attribute-
component, is proposed to refine depth information with a           based evaluations on several representative RGB-D based SOD
semantic guided loss. Thus, the above key components are all        models.
helpful for improving SOD performance.                                 • Object Scale. To characterize the scale of a salient object
   • In SSF [4], a complementary interaction module (CIM)           area, we compute the ratio between the size of the salient
is developed to explore discriminative cross-modal comple-          area and the whole image. We define three types of object
mentarities and fuse cross-modal features, where a region-          scales: 1) when the ratio is less than 0.1, it is denoted as
wise attention is introduced to supplement rich boundary            “small”; 2) when the ratio is larger than 0.4, it is denoted as
information for each modality. Besides, a compensation-aware        “large”; and 3) when the ratio is in the range of [0.1, 0.4],
loss is proposed to improve the network’s confidence for hard       it is denoted as “medium”. In this evaluation, we build a
samples in unreliable depth maps. Thus, these key components        hybrid dataset with 2,464 images collected from STERE [138],
enable the proposed model to effectively explore and establish      NLPR [51] , LFSD [139], DES [49], and SIP [3], where
the complementarity of cross-modal feature representations,         24%, 69.2% and 6.8% of images have small, medium, and
while at the same time reducing the negative effects introduced     large salient object areas, respectively. The constructed hybrid
by low-quality depth maps, boosting SOD performance.                dataset can be found at https://github.com/taozh2017/RGBD-
   • In ICNet [7], an information conversion module is pro-         SODsurvey. Some sample images with different object scales
posed to interactively and adaptively explore the correlations      are shown in Fig. 8. The comparison results of the attribute-
between high-level RGB and depth features. Besides, a cross-        based study w.r.t. object scale are shown in Tab. VIII. From
modal depth-weighted combination block is introduced to             the results, it can be observed that all comparison methods
enhance the difference between the RGB and depth features           obtain better performance in detecting small salient objects
in each level, which ensures that the features are treated          while they obtain worse performance in detecting large salient
differently. It is also worth noting that ICNet exploits the        objects. Besides, the three most recent models, i.e., JL-DCF
complementarity of cross-modal features, as well as explores        [8], UC-Net [9], and S2 MA [6], obtain the best performance.
the continuity of cross-level features, both of which are helpful   D3 Net [3], SSF [4], A2dele [5], and ICNet [7] also obtain
for achieving accurate predictions.                                 promising performance.
   • In S2 MA [6], a self-mutual attention module (SAM) is             • Background Clutter. It is difficult to directly characterize
proposed to fuse RGB and depth images, integrating self-            background clutter. Since classic SOD methods tend to use
attention and each other’s attention to propagate context more      prior information or color contrast to locate salient objects,
accurately. The SAM can provide additional complementary            they often fail under complex backgrounds. Thus, in this
information from multi-modal data to improve SOD per-               evaluation, we utilize five traditional SOD methods, i.e., BSCA
                                                                                                                                                                                                                                                                                                                                             15

                                                                  TABLE X
  ATTRIBUTE - BASED STUDY w.r.t. BACKGROUND OBJECTS (i.e., CAR , BARRIER , FLOWER , GRASS , ROAD , SIGN , TREE , AND OTHER ). T HE COMPARISON
   METHODS INCLUDING 24 REPRESENTATIVE RGB-D BASED SOD MODELS (9 TRADITIONAL MODELS AND 15 DEEP LEARNING - BASED MODELS )
    EVALUATED ON THE SIP DATASET [3] IN TERMS OF MAE AND Sα . T HE THREE BEST RESULTS ARE SHOWN IN RED , BLUE AND GREEN FONTS .
                                                                 Traditional models                                                                                                                              Deep learning-based models

                                                                                                                                                                                                                 AFNet [102]

                                                                                                                                                                                                                                           DMRA [54]
                                                     DESM [49]

                                                                                                                                                                                                                               MMCI [55]

                                                                                                                                                                                                                                                                                                                   JL-DCF [8]
                                                                                                                                                         CTMF [58]

                                                                                                                                                                                                    TANet [99]

                                                                                                                                                                                                                                                                                                                                UC-Net [9]
                                         ACSD [56]

                                                                                                            CDCP [84]
                                                                                        DCMC [1]

                                                                                                                                                                                                                                                                              A2dele [5]
                                                                                                                                                                                        CPFP [53]
                 Categories

                                                                                                                                                                                                                                                       D3 Net [3]

                                                                                                                                                                                                                                                                                           S2 MA [6]
                              LHM [51]

                                                                                                                        CDB [95]

                                                                                                                                                                                                                                                                                                       ICNet [7]
                                                                             LBE [57]

                                                                                                                                             PCF [92]
                                                                   GP [50]

                                                                                                                                   DF [52]

                                                                                                                                                                                                                                                                    SSF [4]
                                                                                                   SE [2]
                 Car          .158       .163        .301         .159       .201       .185       .154     .202        .171       .171      .085       .134                      .094              .084         .101          .093        .069        .061         .063      .078         .055        .067        .058         .057
               Barrier        .197       .177        .308         .180       .201       .196       .176     .251        .203       .202      .073       .149                      .060              .078         .128          .089        .093        .068         .054      .074         .057        .075        .052         .053
               Flower         .105       .122        .306         .099       .186       .158       .063     .141        .101       .132      .091       .075                      .133              .100         .090          .081        .046        .095         .107      .051         .104        .025        .054         .075
               Grass          .164       .161        .279         .155       .184       .167       .138     .182        .176       .167      .041       .110                      .035              .048         .088          .059        .056        .037         .030      .046         .033        .043        .023         .029
         MAE

                Road          .189       .167        .281         .176       .187       .181       .164     .225        .189       .169      .070       .140                      .054              .072         .125          .078        .093        .059         .049      .072         .050        .065        .045         .044
                Sign          .107       .126        .268         .110       .184       .126       .079     .134        .118       .096      .058       .101                      .063              .060         .077          .083        .051        .055         .051      .054         .048        .054        .050         .057
                Tree          .192       .193        .310         .190       .241       .194       .183     .230        .219       .205      .083       .157                      .083              .091         .132          .109        .106        .083         .067      .074         .092        .097        .063         .071
               Other          .246       .217        .329         .224       .229       .216       .229     .274        .233       .233      .106       .177                      .111              .111         .170          .124        .140        .095         .083      .099         .100        .100        .084         .086
               Overall        .184       .172        .298         .173       .200       .186       .164     .224        .192       .185      .071       .139                      .064              .075         .118          .086        .085        .063         .053      .070         .057        .069        .049         .051
                 Car          .516       .731        .590         .603       .714       .671       .591     .613        .546       .631      .811       .726                      .786              .807         .736          .813        .817        .856         .845      .804         .870        .846        .855         .859
               Barrier        .497       .727        .609         .575       .728       .672       .612     .553        .552       .643      .837       .698                      .860              .831         .708          .830        .792        .855         .874      .821         .871        .848        .876         .875
               Flower         .477       .775        .573         .673       .703       .707       .772     .667        .639       .750      .771       .738                      .714              .760         .688          .785        .824        .789         .768      .845         .804        .901        .856         .811
               Grass          .537       .756        .643         .605       .760       .728       .683     .672        .559       .672      .908       .770                      .908              .899         .780          .888        .876        .917         .924      .878         .928        .910        .939         .924
         Sα

                Road          .521       .739        .634         .598       .751       .685       .641     .595        .576       .680      .851       .722                      .871              .848         .705          .847        .807        .873         .885      .832         .885        .868        .889         .892
                Sign          .578       .786        .634         .628       .719       .745       .761     .714        .615       .757      .855       .756                      .833              .857         .771          .818        .848        .849         .849      .842         .871        .861        .859         .840
                Tree          .505       .699        .606         .577       .661       .648       .600     .588        .543       .625      .802       .679                      .804              .778         .691          .779        .748        .806         .837      .807         .800        .788        .848         .825
               Other          .460       .687        .594         .532       .706       .669       .563     .554        .542       .600      .786       .677                      .774              .782         .647          .790        .722        .800         .828      .785         .809        .799        .821         .823
               Overall        .511       .732        .616         .588       .727       .683       .628     .595        .557       .653      .842       .716                      .850              .835         .720          .833        .806        .860         .874      .828         .872        .854        .880         .875
   Simple

                                                                                                                                                                     Single object
   Uncertain

                                                                                                                                                                     Multiple objects
   Complex

Fig. 9. Sample images with three types of background clutter.

                                                                                                                                                        Fig. 10. Sample images with single or multiple salient objects.
[161], CLC [162], MDC [163], MIL [164], and WFD [165],
to first detect salient objects in various images and then
group these images into different categories (e.g., simple or                                                                                           SODsurvey. The comparison results of the attribute-based
complex background) according to the results. Specifically, we                                                                                          study w.r.t. background clutter are shown in Tab. IX. As can
first construct a hybrid dataset with 1,400 images collected                                                                                            be seen, all models obtain worse SOD performance on images
from three datasets (STERE [138], NLPR [51], and LFSD                                                                                                   containing complex backgrounds than simple ones. Among the
[139]). Then, we apply the five models to this dataset and                                                                                              representative models, JL-DCF [8], UC-Net [9] and SSF [4]
obtain the Sα values for each, which we use to characterize                                                                                             achieve the top-three best results. Besides, the four most recent
images as follows: 1) If all Sα values are higher than 0.9,                                                                                             models, i.e., D3 Net [3], S2 MA [6], A2dele [5], and ICNet [7],
the image is denoted as having a “simple” background; 2) If                                                                                             also obtain better performance than the other models.
all Sα values are lower than 0.6, the image is said to have a                                                                                              • Single vs. Multiple Objects. In this evaluation, we
“complex” background; 3) The remaining images are denoted                                                                                               construct a hybrid dataset with 1,229 images collected from
as “uncertain”. Some example images with the three types of                                                                                             the NLPR [51] and SIP [3] datasets. Some example images
background clutter are shown in Fig. 9. The constructed hybrid                                                                                          with single or multiple salient objects are shown in Fig. 10.
dataset can be found at https://github.com/taozh2017/RGBD-                                                                                              The comparison results are shown in Fig. 11. From the results,
                                                                                                                                                                                                                                                                                                                                           16

       0.3

       0.2
 MAE

       0.1                               Single
                                         Multiple
                                         Overall

                                                                                             SE

                                                                                                             TA P
             D D

                                                                                                                    P

                                                                                                             AF t
                                                                                                              M t
                 M

             D E

                                                                                                             D A

                                                                                                             A2 F
                                                                                                                    F

                                                                                                             C F

                                                                                                                    A
                  P

                                                                                                              S2 e
                                                                                                                   B

                                                                                                                    F

                                                                                                             U F
                                                                                                                   et

                                                                                                            JL et
                  C

                                                                                                             D I

                                                                                                                   et
                 M

                                                                                                                   e
                                                                                                                   e
                                                                                                                  C

                                                                                                                   l
                                                                                                                PF

                                                                                                                SS
                                                                                                                  D
                                                                                                                PC
                                                                                                        C

                                                                                                                TM

                                                                                                                  C
               LB

                                                                                                                  R
                S

                                                                                                                 M
                G

                                                                                                                 D
                M

                                                                                                                de
                                                                                                                 N
                                                                                                                 N
              ES

                                                                                                                3N

                                                                                                                 N

                                                                                                                 N
              LH

                                                                                                                M
             AC

                                                                                                        D

                                                                                                               -D
                                                                                                                M
                                                                                                                     C

                                                                                                              IC
              C

                                                                                                               C
                                                                                                              C
                                                                                               C                                                           Methods
             1

        0.8

        0.6
S

        0.4
                                         Single
        0.2                              Multiple
                                         Overall
             0
                                                                                             SE

                                                                                                                                      F
                  M

                                                      D E

                                                                                                                                                                                P
                                                           P

                                                                                                                                                                                                    A

                                                                                                                                                                                             A2 F
                                                                                                                                                   F
                SD

                                                                                                                                                                F

                                                                                                                                                                                            JL et
                                                                                                            P

                                                                                                                                                                                             AF t

                                                                                                                                                                                              M t

                                                                                                                                                                                                   et

                                                                                                                                                                                                   le
                                                                                                                         B

                                                                                                                                                                                             U F
                                                                                                                                                                                                   A
                                                           C

                                                                                                                                                                                                   et
                 M

                                                                                                                                                                                             D I
                                                                                                                                                                                                   e

                                                                                                                                                                                                   e
                                                                                                                                                                                                  C
                                                                                                                                     D

                                                                                                                                                                                                SS
                                                                                                                                                PC

                                                                                                                                                           TM
                                                        LB

                                                                                                                                                                       PF
                                                      G

                                                                                                                                                                                                  R

                                                                                                                                                                                                  C
                                                                                                         C

                                                                                                                     D

                                                                                                                                                                                                 M
                                                         M
               ES

                                                                                                                                                                                                de

                                                                                                                                                                                                 N
                                                                                                                                                                                       N

                                                                                                                                                                                                 N

                                                                                                                                                                                                3N

                                                                                                                                                                                                 N
              LH

                                                                                                                                                                                                M
                                                                                                                                                                                                M

                                                                                                                                                                                               -D
             AC

                                                                                                        D

                                                                                                                     C

                                                                                                                                                                                              S2

                                                                                                                                                                                              IC
                                                                                                                                                                                    TA
                                                       C

                                                                                                                                                                                               C
                                                                                                                                                                      C
                                                                                                                                                          C
             D

                                                                                                C

                                                                                                                                                                                             D
                                                                                                                                                           Methods
Fig. 11. Attribute-based study w.r.t. number of salient objects (i.e., single vs. multiple (multi)). The comparison results on 24 representative RGB-D based
SOD models (i.e., LHM [51], ACSD [56], DESM [49], GP [50], LBE [57], DCMC [1], SE [2], CDCP [84], CDB [95], DF [52], PCF [92], CTMF [58],
CPFP [53], TANet [99], AFNet [102], MMCI [55], DMRA [54], D3 Net [3], SSF [4], A2dele [5], S2 MA [6], ICNet [7], JL-DCF [8], and UC-Net [9]) are
given in terms of MAE (top) and Sα (bottom).

                                                                 TABLE XI
  ATTRIBUTE - BASED STUDY w.r.t. LIGHT CONDITIONS ( SUNNY VS . LOW- LIGHT ). T HE COMPARISON METHODS INCLUDE 24 REPRESENTATIVE RGB-D
 BASED SOD MODELS (9 TRADITIONAL MODELS AND 15 DEEP LEARNING - BASED MODELS ) EVALUATED ON THE SIP DATASET [3] IN TERMS OF MAE
                                AND Sα . T HE THREE BEST RESULTS ARE SHOWN IN RED , BLUE AND GREEN FONTS .
                                                                      Traditional models                                                                                                                      Deep learning-based models
                                                                                                                                                                                                               AFNet [102]

                                                                                                                                                                                                                                         DMRA [54]
                                                          DESM [49]

                                                                                                                                                                                                                             MMCI [55]

                                                                                                                                                                                                                                                                                                                 JL-DCF [8]
                                                                                                                                                                        CTMF [58]

                                                                                                                                                                                                 TANet [99]

                                                                                                                                                                                                                                                                                                                              UC-Net [9]
                                          ACSD [56]

                                                                                                                         CDCP [84]
                                                                                             DCMC [1]

                                                                                                                                                                                                                                                                            A2dele [5]
                 Conditions

                                                                                                                                                                                     CPFP [53]

                                                                                                                                                                                                                                                     D3 Net [3]

                                                                                                                                                                                                                                                                                         S2 MA [6]
                              LHM [51]

                                                                                                                                     CDB [95]

                                                                                                                                                                                                                                                                                                     ICNet [7]
                                                                                  LBE [57]

                                                                                                                                                           PCF [92]
                                                                        GP [50]

                                                                                                                                                DF [52]

                                                                                                                                                                                                                                                                  SSF [4]
                                                                                                            SE [2]

              Sunny           .182 .171 .294 .171 .200 .183 .160 .218 .190 .181 .069 .137 .062 .075 .116 .085 .083 .062 .052 .068 .057 .068 .048 .051
       MAE

             Low-light        .198 .178 .323 .187 .201 .207 .193 .268 .208 .211 .078 .154 .073 .076 .130 .091 .103 .067 .059 .080 .058 .081 .059 .055
              Overall         .184 .172 .298 .173 .200 .186 .164 .224 .192 .185 .071 .139 .064 .075 .118 .086 .085 .063 .053 .070 .057 .069 .049 .051
               Sunny          .516 .733 .622 .593 .728 .690 .639 .607 .560 .660 .843 .718 .852 .834 .723 .833 .811 .861 .875 .831 .872 .856 .882 .876
             low-light        .481 .721 .573 .554 .722 .635 .556 .515 .543 .610 .838 .701 .838 .837 .700 .832 .775 .855 .867 .810 .871 .839 .867 .871
       Sα

              Overall         .511 .732 .616 .588 .727 .683 .628 .595 .557 .653 .842 .716 .850 .835 .720 .833 .806 .860 .874 .828 .872 .854 .880 .875

we can see that it is easier to detect single salient object than                                                                                                     light conditions.
multiple ones.                                                                                                                                                           • Background Objects. We evaluate the performance of
   • Indoor vs. Outdoor. We evaluate the performance of                                                                                                               the RGB-D based SOD models when different background
different RGB-D based SOD models on indoor and outdoor                                                                                                                objects are present. We use the SIP dataset [3], and split it
scenes. In this evaluation, we construct a hybrid dataset                                                                                                             into nine categories, i.e., car, barrier, flower, grass, road, sign,
collected from the DES [49], NLPR [51], and LFSD [139]                                                                                                                tree, and other. The comparison results are shown in Tab. X.
datasets. The comparison results are shown in Fig. 12. From                                                                                                           As can be seen, all methods obtain diverse performances under
the results, it can be seen that most models struggle more to                                                                                                         different background objects. Among the 24 representative
detect salient objects in indoor scene than outdoor scenes. This                                                                                                      RGB-D based models, JL-DCF [8], UC-Net [9] and SSF [4]
is possibly because indoor environments often have varying                                                                                                            achieve the top-three best results. In addition, the four most
                                                                                                                                                  17

       0.4
                       Indoor       Outdoor           Overall
       0.3
 MAE

       0.2

       0.1

                                              SE

                                                             TA P
             D D

                                                      P

                                                             AF et
                                                              M et
                 M

                                D E

                                                             D A

                                                             A2 F
                                                                    F

                                                             C F

                                                                   A
                                     P

                                                              S2 le
                                                                   B

                                                              C F

                                                             U F
                                                                   et

                                                            JL et
                                     C

                                                             D I

                                                                   et
                 M

                                                                  C
                                                                PF

                                                                SS
                                                                  D
                                                                PC
                                                    C

                                                                TM

                                                                  C
                                  LB

                                                                  R
                S

                                                                 M
                                G

                                                          D
                                   M

                                                                de
                                                                 N
                                                                 N
              ES

                                                                3N

                                                                 N

                                                                 N
              LH

                                                                M
             AC

                                                 D

                                                               -D
                                                                M
                                                        C

                                                              IC
                                 C

                                                               C
                                                C                       Methods
        1
                       Indoor       Outdoor         Overall
       0.9

       0.8
S

       0.7

       0.6

       0.5
                                              SE

                                                                         F
                       M

                                D E

                                                                 TA P
                                     P

                                                                 D A

                                                                 A2 F
                                                                  C F
                   D D

                                                                        F

                                                                JL et
                                                      P

                                                                 AF t

                                                                  M t

                                                                       et

                                                                  S2 e
                                                            B

                                                                 U F
                                                                       A
                                     C

                                                                       et
              M

                                                                 D I
                                                                       e
                                                                       e
                                                                      C
                                                                      D

                                                                       l
                                                                    SS
                                                                    PC
                                                                    TM
                                  LB

                                                                    PF
                                   G

                                                                      R

                                                                      C
                                                    C
                                                          D
                     S

                                                                     M
                                   M
                    ES

                                                                    de

                                                                     N
                                                                     N
                                                                     N

                                                                    3N

                                                                     N
             LH

                                                                    M
                                                                    M

                                                                   -D
                  AC

                                                  D
                                                        C

                                                                  IC
                                 C

                                                                   C
                                                                  C
                                                C

                                                                        Methods
Fig. 12. Attribute-based study w.r.t. indoor vs. outdoor environments. The comparison results for 24 representative RGB-D based SOD models (i.e., LHM
[51], ACSD [56], DESM [49], GP [50], LBE [57], DCMC [1], SE [2], CDCP [84], CDB [95], DF [52], PCF [92], CTMF [58], CPFP [53], TANet [99],
AFNet [102], MMCI [55], DMRA [54], D3 Net [3], SSF [4], A2dele [5], S2 MA [6], ICNet [7], JL-DCF [8], and UC-Net [9]) are provided in terms of MAE
(top) and Sα (bottom).

recent models, i.e., D3 Net [3], S2 MA [6], A2dele [5], and                 low-light condition. In the 8th row, the depth map is coarse
ICNet [7] obtain better performance than the others.                        with very inaccurate object boundaries, which could inhibit the
   • Lighting Conditions. The performance of SOD can be                     SOD performance. From the results in Fig. 13 and Fig. 14,
affected by different lighting conditions. To determine the                 it can be observed that deep models perform better than
performance of different RGB-D based SOD models under                       non-deep models on these challenging scenes, confirming the
different lighting conditions, we conduct an evaluation on the              powerful expression ability of deep features over handcrafted
SIP dataset [3], which we split it into two categories, i.e.,               ones. In addition, D3 Net [3], S2 MA [6], JL-DCF [8], and UC-
sunny and low-light. The comparison results are shown in                    Net [9] perform better than other deep models.
Tab. XI. As can be seen, low-light negatively impacts SOD
performance. Among comparison models, UC-Net [9] obtains                              VI. C HALLENGES AND O PEN D IRECTIONS
the best performance under sunny conditions while JL-DCF
[8] achieves the best result under low-light condition.                     A. Effects of Imperfect Depth
   In addition, we report the saliency maps generated for                      Effects of Low-quality Depth Maps. Depth maps with
various challenging scenes to visualize the performance of                  affluent spatial information have been proven beneficial in
different RGB-D based SOD models. Fig. 13 and Fig. 14                       detecting salient objects from cluttered backgrounds, while
show some representative examples using two classic non-                    the depth quality also directly affects the subsequent SOD
deep methods (DCMC [1] and SE [2]) and eight state-of-                      performance. The quality of depth maps varies tremendously
the-art CNN-based models (DMRA [54], D3 Net [3], SSF [4],                   across different scenarios due to the limitations of depth
A2dele [5], S2 MA [6], ICNet [7], JL-DCF [8], and UC-Net                    sensors, posing a challenge when trying to reduce the effects
[9]). The 1st row shows a small object, while the 2nd row is an             of low-quality depth maps. However, most existing methods
example of a large one. The 3rd and 4th rows contain complex                directly fuse RGB images and original raw data from depth
backgrounds and boundaries, respectively. The 5th and 6th                   maps, without considering the effects of low-quality depth
rows contain multiple salient objects. In the 7th row, there are            maps. There are a few notable exceptions. For example,
                                                                                                                                                 18

       RGB              Depth                GT             DCMC                 SE             DMRA             D3Net               SSF
Fig. 13. Visual comparisons for two classical non-deep methods (DCMC [1] and SE [2]) and three state-of-the-art CNN-based models (DMRA [54], D3 Net
[3], SSF [4]).

in [53], a contrast-enhanced network was proposed to learn                    Incomplete Depth Maps. In RGB-D datasets, it is in-
enhanced depth maps, which have much higher contrasts                      evitable for there to be some low-quality depth maps due
compared with the original depths. In [4], a compensation-                 to the limitations of the acquisition devices. As previously
aware loss was designed to pay more attention to hard samples              discussed, several depth enhancement algorithms have been
containing unreliable depth information. Moreover, D3 Net [3]              used to improve the quality of depth maps. However, depth
uses a depth depurator unit (DDU) to classify depth maps                   maps that suffer from severe noise or blurred edges, are often
into two classes (i.e., reasonable and low-quality). The DDU               discarded. In this case, we have complete RGB images but
also acts as a gate that can filter out the low-quality depth              some samples do not have depth maps, which is similar to the
maps. However, the above methods often employ a two-step                   incomplete multi-view/modal learning problem [166]–[170].
strategy to achieve depth enhancement and multi-modal fusion               Thus, we call it “incomplete RGB-D based SOD”. As current
[4], [53] or an independent gate operation for filtering out poor          models only focus on the SOD task using complete RGB
depths, which could bring a suboptimal problem. There is thus              images and depth maps, we believe this could be a new
a need to develop an end-to-end framework that can achieve                 direction for RGB-D SOD.
depth enhancement or adaptively weight the depth maps (e.g.,                  Depth Estimation. Depth estimation provides an effective
assign low weights to poor depth maps) during multi-modal                  solution to recover high-quality depths and overcome the
fusion, which would be more helpful for reducing the effects               effects of low-quality depth maps. Various depth estimation
of low-quality depth maps and boosting SOD performance.                    approaches [171]–[174] have been developed, which could
                                                                                                                                                  19

       RGB               Depth                GT              A2dele             S2MA               ICNet             JL-DCF             UC-Net

Fig. 14. Visual comparisons for five state-of-the-art CNN-based models (A2dele [5], S2 MA [6], ICNet [7], JL-DCF [8], and UC-Net [9]).

be introduced into the RGB-D based SOD task to improve                       could be helpful for boosting performance due to their superior
performance.                                                                 feature learning ability. Moreover, GANs could also be used
                                                                             to learn common feature representations for RGB images and
                                                                             depth maps [118], which could help with feature or saliency
B. Effective Fusion Strategies
                                                                             map fusion and further boost the SOD performance.
   Adversarial Learning-based Fusion. It is important to
effectively fuse RGB images and depth maps for RGB-D                            Attention-induced Fusion. Attention mechanisms have
based SOD. Existing models often employ different fusion                     been widely applied to various deep learning-based tasks
strategies (e.g., early fusion, middle fusion, or late fusion) to            [178]–[181], allowing networks to selectively pay attention to
exploit the correlations between RGB images and depth maps.                  a subset of regions for extracting discriminative and powerful
Recently, generative adversarial networks (GANs) [175] have                  features. Besides, co-attention mechanisms have been devel-
gained widespread attention for the saliency detection task                  oped to explore the underlying correlations across multiple
[176], [177]. In common GAN-based SOD models, a generator                    modalities, and are widely studied in visual question answering
takes RGB images as inputs and generates the corresponding                   [182], [183] and video object segmentation [184]. Thus, for
saliency maps, while a discriminator is adopted to determine                 the RGB-D based SOD task, we could also develop attention-
whether a given image is synthetic or ground-truth. GAN-                     based fusion algorithms to exploit correlations between RGB
based models could easily be extended to RGB-D SOD, which                    images and depth cues to improve the performance.
                                                                                                                                            20

C. Different Supervision Strategies                                 F. Extension to RGB-T SOD
   Existing RGB-D models often use a fully supervised strat-           In addition to RGB-D SOD, there are several other methods
egy to learn saliency prediction models. However, annotating        that fuse different modalities for better detection, such as
pixel-level saliency maps is a tedious and time-consuming           RGB-T SOD, which integrates RGB and thermal infrared data.
procedure. To alleviate this issue, there has been increased        Thermal infrared cameras can capture the radiation emitted
interest in weakly and semi-supervised learning, which have         from any object with a temperature above absolute zero,
been applied to salient object detection [185]–[189]. Semi-         making thermal infrared images insensitive to illumination
/weak supervision could also be introduced into RGB-D SOD,          conditions [197]. Therefore, thermal images can provide sup-
by leveraging image-level tags [185] and pseudo pixel-wise          plementary information to improve SOD performance when
annotations [188], [190], for improving the detection perfor-       salient objects suffer from varying light, reflective light, or
mance. Besides, several studies [191], [192] have suggested         shadows. Some RGB-T models [197]–[205] and datasets
that models pretrained using self-supervision can effectively       (VT821 [199], VT1000 [203] and VT5000 [205]) have already
be used to achieve better performance. Therefore, we could          been proposed over the past few years. Similar to RGB-
train saliency prediction models on large amounts of annotated      D SOD, the key aim of RGB-T SOD is to fuse RGB and
RGB images in a self-supervised manner and then transfer the        thermal infrared images and exploit the correlations between
pretrained models to the RGB-D SOD task.                            the two modalities. Thus, several advanced multi-modal fusion
                                                                    technologies in RGB-D SOD could be extended to the RGB-T
                                                                    SOD task.
D. Dataset Collection
   Dataset size. Although there are nine public RGB-D                                       VII. C ONCLUSION
datasets for SOD, their size is quite limited, e.g., the maximum
                                                                       In this paper we present, to the best of our knowledge, the
size is about 2,000 samples for NJUD [56]. When compared
                                                                    first comprehensive review of RGB-D based SOD models. We
with other RGB-D datasets for generic object detection or
                                                                    first review the models from different perspectives, and then
action recognition [193], [194], the size of RGB-D datasets
                                                                    summarize popular RGB-D SOD datasets as well as provide
for SOD is also very small. Thus, it is essential to develop
                                                                    details for each. Considering the fact that light fields also
new large-scale RGB-D datasets that can serve as baselines
                                                                    provide depth information, we also review popular light field
for future research.
                                                                    SOD models and the related benchmark datasets. Next, we
   Complex Background & Task-driven Datasets. Most
                                                                    provide a comprehensive evaluation of 24 representative RGB-
existing RGB-D datasets collect images that contain one
                                                                    D based SOD models as well as an attribute-based evaluation.
salient object or multiple objects but with a relatively clean
                                                                    Specifically, we perform attribute-based performance analysis
background. However, real-world applications often suffer
                                                                    by constructing new datasets for the 24 representative RGB-D
from much more complicated situations (e.g., occlusion, ap-
                                                                    based SOD models. Moreover, we discuss several challenges
pearance change, low illumination, etc), which could decrease
                                                                    and highlight open directions for future research. In addition,
the SOD performance. Thus, collecting images with complex
                                                                    we briefly discuss the extension work to RGB-T SOD to
background is critical to improve the generalization ability
                                                                    improve performance when salient objects suffer from varying
of RGB-D SOD models. Moreover, for some tasks, images
                                                                    light, reflective light, or shadows. Although RGB-D based
with specific salient object(s) must be collected. For example,
                                                                    SOD has made notable progress over the past several decades,
one important technology is road sign recognition in driver
                                                                    there is still significant room for improvement. We hope this
assistance systems, which requires images with road signs to
                                                                    survey will generate more interest in this field.
be collected. Thus, it is essential to construct task-driven RGB-
D datasets like SIP [3].
                                                                                                R EFERENCES
                                                                     [1] Runmin Cong, Jianjun Lei, Changqing Zhang, Qingming Huang,
E. Model Design for Real-world Scenarios                                 Xiaochun Cao, and Chunping Hou, “Saliency detection for stereoscopic
                                                                         images based on depth confidence analysis and multiple cues fusion,”
   Some smartphones can capture depth maps (e.g., images in              IEEE Signal Processing Letters, vol. 23, no. 6, pp. 819–823, 2016.
the SIP dataset were captured using Huawei Mate 10). Thus            [2] Jingfan Guo, Tongwei Ren, and Jia Bei, “Salient object detection for
                                                                         RGB-D image via saliency evolution,” in Proceedings of the IEEE
it would be feasible to conduct the SOD task in real-world               International Conference on Multimedia and Expo. IEEE, 2016, pp.
applications, e.g., on smart devices. However, most existing             1–6.
methods include complicated and deep DNNs to increase the            [3] Deng-Ping Fan, Zheng Lin, Zhao Zhang, Menglong Zhu, and Ming-
                                                                         Ming Cheng, “Rethinking RGB-D salient object detection: Models,
model capacity and achieve better performance, preventing                data sets, and large-scale benchmarks,” IEEE Transactions on Neural
them from being directly applied on real-work platforms. To              Networks and Learning Systems, 2020.
overcome this, model compression [195], [196] techniques             [4] Miao Zhang, Weisong Ren, Yongri Piao, Zhengkun Rong, and Huchuan
                                                                         Lu, “Select, supplement and focus for RGB-D saliency detection,” in
could be used to learn compact RGB-D based SOD models                    Proceedings of the IEEE Conference on Computer Vision and Pattern
with promising detection accuracy. Moreover, JL-DCF [8]                  Recognition, 2020.
utilizes a shared network to locate salient objects using RGB        [5] Yongri Piao, Zhengkun Rong, Miao Zhang, Weisong Ren, and Huchuan
                                                                         Lu, “A2dele: Adaptive and attentive depth distiller for efficient RGB-
and depth views, which largely reduces the model parameters              D salient object detection,” Proceedings of the IEEE Conference on
and makes real-world applications feasible.                              Computer Vision and Pattern Recognition, 2020.
                                                                                                                                                        21

 [6] Nian Liu, Ni Zhang, and Junwei Han, “Learning selective self-mutual       [26] Rui Zhao, Wanli Oyang, and Xiaogang Wang, “Person re-identification
     attention for RGB-D saliency detection,” in Proceedings of the IEEE            by saliency learning,” IEEE Transactions on Pattern Analysis and
     Conference on Computer Vision and Pattern Recognition, 2020.                   Machine Intelligence, vol. 39, no. 2, pp. 356–370, 2016.
 [7] Gongyang Li, Zhi Liu, and Haibin Ling, “Icnet: Information conversion     [27] Niki Martinel, Christian Micheloni, and Gian Luca Foresti, “Kernelized
     network for RGB-D based salient object detection,” IEEE Transactions           saliency-based person re-identification through multiple metric learn-
     on Image Processing, vol. 29, pp. 4873–4884, 2020.                             ing,” IEEE Transactions on Image Processing, vol. 24, no. 12, pp.
 [8] Keren Fu, Deng-Ping Fan, Ge-Peng Ji, and Qijun Zhao, “Jl-dcf: Joint            5645–5658, 2015.
     learning and densely-cooperative fusion framework for RGB-D salient       [28] Deng-Ping Fan, Ge-Peng Ji, Guolei Sun, Ming-Ming Cheng, Jianbing
     object detection,” Proceedings of the IEEE Conference on Computer              Shen, and Ling Shao, “Camouflaged object detection,” in Proceedings
     Vision and Pattern Recognition, 2020.                                          of the IEEE Conference on Computer Vision and Pattern Recognition,
 [9] Jing Zhang, Deng-Ping Fan, Yuchao Dai, Saeed Anwar, Fatemeh Sadat              2020, pp. 2777–2787.
     Saleh, Tong Zhang, and Nick Barnes, “Uc-net: uncertainty inspired         [29] Guanghai Liu and Dengping Fan, “A model of visual attention for
     rgb-d saliency detection via conditional variational autoencoders,” in         natural image retrieval,” in Proceedings of the IEEE Conference on
     Proceedings of the IEEE Conference on Computer Vision and Pattern              Information Science and Cloud Computing Companion. IEEE, 2013,
     Recognition, 2020.                                                             pp. 728–733.
[10] Deng-Ping Fan, Ming-Ming Cheng, Jiang-Jiang Liu, Shang-Hua Gao,           [30] Jia-Xing Zhao, Jiang-Jiang Liu, Deng-Ping Fan, Yang Cao, Jufeng
     Qibin Hou, and Ali Borji, “Salient objects in clutter: Bringing salient        Yang, and Ming-Ming Cheng, “Egnet: Edge guidance network for
     object detection to the foreground,” in Proceedings of the European            salient object detection,” in Proceedings of the IEEE International
     Conference on Computer Vision. Springer, 2018, pp. 186–202.                    Conference on Computer Vision, 2019, pp. 8779–8788.
[11] Guang-Yu Nie, Ming-Ming Cheng, Yun Liu, Zhengfa Liang, Deng-              [31] Wei-Chih Tu, Shengfeng He, Qingxiong Yang, and Shao-Yi Chien,
     Ping Fan, Yue Liu, and Yongtian Wang, “Multi-level context ultra-              “Real-time salient object detection with a minimum spanning tree,” in
     aggregation for stereo matching,” in Proceedings of the IEEE Confer-           Proceedings of the IEEE conference on Computer Vision and Pattern
     ence on Computer Vision and Pattern Recognition, 2019, pp. 3283–               Recognition, 2016, pp. 2334–2342.
     3291.                                                                     [32] Changqun Xia, Jia Li, Xiaowu Chen, Anlin Zheng, and Yu Zhang,
[12] Jun-Yan Zhu, Jiajun Wu, Yan Xu, Eric Chang, and Zhuowen Tu,                    “What is and what is not a salient object? learning salient object
     “Unsupervised object class discovery via saliency-guided multiple              detector by ensembling linear exemplar regressors,” in Proceedings
     class learning,” IEEE Transactions on Pattern Analysis and Machine             of the IEEE Conference on Computer Vision and Pattern Recognition,
     Intelligence, vol. 37, no. 4, pp. 862–875, 2014.                               2017, pp. 4142–4150.
[13] Deng-Ping Fan, Tengpeng Li, Zheng Lin, Ge-Peng Ji, Dingwen Zhang,         [33] Xiaodi Hou and Liqing Zhang, “Saliency detection: A spectral residual
     Ming-Ming Cheng, Huazhu Fu, and Jianbing Shen, “Re-thinking co-                approach,” in Proceedings of the IEEE Conference on Computer Vision
     salient object detection,” arXiv preprint arXiv:2007.03380, 2020.              and Pattern Recognition. IEEE, 2007, pp. 1–8.
[14] Konstantinos Rapantzikos, Yannis Avrithis, and Stefanos Kollias,          [34] Qiong Yan, Li Xu, Jianping Shi, and Jiaya Jia, “Hierarchical saliency
     “Dense saliency-based spatiotemporal feature points for action recog-          detection,” in Proceedings of the IEEE Conference on Computer Vision
     nition,” in Proceedings of the IEEE Conference on Computer Vision              and Pattern Recognition, 2013, pp. 1155–1162.
     and Pattern Recognition. IEEE, 2009, pp. 1454–1461.
                                                                               [35] Chuan Yang, Lihe Zhang, Huchuan Lu, Xiang Ruan, and Ming-Hsuan
[15] Deng-Ping Fan, Wenguan Wang, Ming-Ming Cheng, and Jianbing
                                                                                    Yang, “Saliency detection via graph-based manifold ranking,” in
     Shen, “Shifting more attention to video salient object detection,” in
                                                                                    Proceedings of the IEEE Conference on Computer Vision and Pattern
     Proceedings of the IEEE Conference on Computer Vision and Pattern
                                                                                    Recognition, 2013, pp. 3166–3173.
     Recognition, 2019, pp. 8554–8564.
                                                                               [36] Guanbin Li and Yizhou Yu, “Deep contrast learning for salient object
[16] Wenguan Wang, Jianbing Shen, Ruigang Yang, and Fatih Porikli,
                                                                                    detection,” in Proceedings of the IEEE Conference on Computer Vision
     “Saliency-aware video object segmentation,” IEEE Transactions on
                                                                                    and Pattern Recognition, 2016, pp. 478–487.
     Pattern Analysis and Machine Intelligence, vol. 40, no. 1, pp. 20–33,
                                                                               [37] Dingwen Zhang, Deyu Meng, and Junwei Han, “Co-saliency detection
     2017.
                                                                                    via a self-paced multiple-instance learning framework,” IEEE Trans-
[17] Hongmei Song, Wenguan Wang, Sanyuan Zhao, Jianbing Shen, and
                                                                                    actions on Pattern Analysis and Machine Intelligence, vol. 39, no. 5,
     Kin-Man Lam, “Pyramid dilated deeper convlstm for video salient
                                                                                    pp. 865–878, 2016.
     object detection,” in Proceedings of the European Conference on
     Computer Vision. Springer, 2018, pp. 715–731.                             [38] Pingping Zhang, Dong Wang, Huchuan Lu, Hongyu Wang, and Xiang
[18] Wenguan Wang, Jianbing Shen, and Ling Shao, “Video salient object              Ruan, “Amulet: Aggregating multi-level convolutional features for
     detection via fully convolutional networks,” IEEE Transactions on              salient object detection,” in Proceedings of the IEEE International
     Image Processing, vol. 27, no. 1, pp. 38–49, 2017.                             Conference on Computer Vision, 2017, pp. 202–211.
[19] Wataru Shimoda and Keiji Yanai, “Distinct class-specific saliency maps    [39] Pingping Zhang, Dong Wang, Huchuan Lu, Hongyu Wang, and Baocai
     for weakly supervised semantic segmentation,” in Proceedings of the            Yin, “Learning uncertain convolutional features for accurate saliency
     European Conference on Computer Vision. Springer, 2016, pp. 218–               detection,” in Proceedings of the IEEE International Conference on
     234.                                                                           Computer Vision, 2017, pp. 212–221.
[20] Yu Zeng, Yunzhi Zhuge, Huchuan Lu, and Lihe Zhang, “Joint learning        [40] Tiantian Wang, Ali Borji, Lihe Zhang, Pingping Zhang, and Huchuan
     of saliency detection and weakly supervised semantic segmentation,” in         Lu, “A stagewise refinement model for detecting salient objects in
     Proceedings of the IEEE International Conference on Computer Vision.           images,” in Proceedings of the IEEE International Conference on
     Springer, 2019, pp. 7223–7233.                                                 Computer Vision, 2017, pp. 4019–4028.
[21] Deng-Ping Fan, Ge-Peng Ji, Tao Zhou, Geng Chen, Huazhu Fu,                [41] Xin Li, Fan Yang, Hong Cheng, Wei Liu, and Dinggang Shen, “Contour
     Jianbing Shen, and Ling Shao, “Pranet: Parallel reverse attention              knowledge transfer for salient object detection,” in Proceedings of the
     network for polyp segmentation,” in Medical Image Computing and                Proceedings of the European Conference on Computer Vision. Springer,
     Computer-Assisted Intervention, 2020.                                          September 2018.
[22] Deng-Ping Fan, Tao Zhou, Ge-Peng Ji, Yi Zhou, Geng Chen, Huazhu           [42] Wenguan Wang, Shuyang Zhao, Jianbing Shen, Steven CH Hoi, and
     Fu, Jianbing Shen, and Ling Shao, “Inf-net: Automatic covid-19 lung            Ali Borji, “Salient object detection with pyramid attention and salient
     infection segmentation from ct images,” IEEE Transactions on Medical           edges,” in Proceedings of the IEEE Conference on Computer Vision
     Imaging, 2020.                                                                 and Pattern Recognition, 2019, pp. 1448–1457.
[23] Yu-Huan Wu, Shang-Hua Gao, Jie Mei, Jun Xu, Deng-Ping Fan, Chao-          [43] Jinming Su, Jia Li, Yu Zhang, Changqun Xia, and Yonghong Tian,
     Wei Zhao, and Ming-Ming Cheng, “Jcs: An explainable covid-19                   “Selectivity or invariance: Boundary-aware salient object detection,”
     diagnosis system by joint classification and segmentation,” arXiv              in Proceedings of the IEEE International Conference on Computer
     preprint arXiv:2004.07054, 2020.                                               Vision, 2019, pp. 3799–3808.
[24] Vijay Mahadevan and Nuno Vasconcelos, “Saliency-based discriminant        [44] Ting Zhao and Xiangqian Wu, “Pyramid feature attention network
     tracking,” in Proceedings of the IEEE Conference on Computer Vision            for saliency detection,” in Proceedings of the IEEE Conference on
     and Pattern Recognition. IEEE, 2009, pp. 1007–1013.                            Computer Vision and Pattern Recognition, 2019, pp. 3085–3094.
[25] Seunghoon Hong, Tackgeun You, Suha Kwak, and Bohyung Han,                 [45] Hao Chen and Youfu Li, “Cnn-based rgb-d salient object detection:
     “Online tracking by learning discriminative saliency map with convolu-         Learn, select and fuse,” arXiv preprint arXiv:1909.09309, 2019.
     tional neural network,” in Proceedings of the International Conference    [46] Congyan Lang, Tam V Nguyen, Harish Katti, Karthik Yadati, Mohan
     on Machine Learning, 2015, pp. 597–606.                                        Kankanhalli, and Shuicheng Yan, “Depth matters: Influence of depth
                                                                                                                                                           22

     cues on visual saliency,” in Proceedings of the European Conference       [68] Jianjun Lei, Hailong Zhang, Lei You, Chunping Hou, and Laihua Wang,
     on Computer Vision. Springer, 2012, pp. 101–115.                               “Evaluation and modeling of depth feature incorporated visual attention
[47] Arridhana Ciptadi, Tucker Hermans, and James M Rehg, “An in depth              for salient object segmentation,” Neurocomputing, vol. 120, pp. 24–33,
     view of saliency,” Georgia Institute of Technology, 2013.                      2013.
[48] Karthik Desingh, K Madhava Krishna, Deepu Rajan, and CV Jawahar,          [69] Xingxing Fan, Zhi Liu, and Guangling Sun, “Salient region detection
     “Depth really matters: Improving visual salient region detection with          for stereoscopic images,” in Proceedings of the International Confer-
     depth,” in Proceedings of the British Machine Vision Conference, 2013.         ence on Digital Signal Processing. IEEE, 2014, pp. 454–458.
[49] Yupeng Cheng, Huazhu Fu, Xingxing Wei, Jiangjian Xiao, and Xi-            [70] Jingfan Guo, Tongwei Ren, Jia Bei, and Yujin Zhu, “Salient object
     aochun Cao, “Depth enhanced saliency detection method,” in                     detection in rgb-d image based on saliency fusion and propagation,”
     Proceedings of the International Conference on Internet Multimedia             in Proceedings of the International Conference on Internet Multimedia
     Computing and Service, 2014, pp. 23–27.                                        Computing and Service, 2015, pp. 1–5.
[50] Jianqiang Ren, Xiaojin Gong, Lu Yu, Wenhui Zhou, and Michael              [71] Yanlong Tang, Ruofeng Tong, Min Tang, and Yun Zhang, “Depth
     Ying Yang, “Exploiting global priors for RGB-D saliency detection,” in         incorporating with color improves salient object detection,” The Visual
     Proceedings of the IEEE Conference on Computer Vision and Pattern              Computer, vol. 32, no. 1, pp. 111–121, 2016.
     Recognition Workshops, 2015, pp. 25–32.                                   [72] Lixing Jiang, Artur Koch, and Andreas Zell, “Salient regions detection
[51] Houwen Peng, Bing Li, Weihua Xiong, Weiming Hu, and Rongrong                   for indoor robots using rgb-d data,” in Proceedings of the IEEE
     Ji, “Rgbd salient object detection: a benchmark and algorithms,” in            International Conference on Robotics and Automation. IEEE, 2015,
     Proceedings of the European Conference on Computer Vision. Springer,           pp. 1323–1328.
     2014, pp. 92–109.                                                         [73] Haoyang Xue, Yun Gu, Yijun Li, and Jie Yang, “Rgb-d saliency
[52] Liangqiong Qu, Shengfeng He, Jiawei Zhang, Jiandong Tian, Yandong              detection via mutual guided manifold ranking,” in Proceedings of IEEE
     Tang, and Qingxiong Yang, “RGBD salient object detection via deep              International Conference on Image Processing. IEEE, 2015, pp. 666–
     fusion,” IEEE Transactions on Image Processing, vol. 26, no. 5, pp.            670.
     2274–2285, 2017.                                                          [74] Lei Zhu, Zhiguo Cao, Zhiwen Fang, Yang Xiao, Jin Wu, Huiping Deng,
[53] Jia-Xing Zhao, Yang Cao, Deng-Ping Fan, Ming-Ming Cheng, Xuan-                 and Jing Liu, “Selective features for rgb-d saliency,” in Proceedings
     Yi Li, and Le Zhang, “Contrast prior and fluid pyramid integration for         of Chinese Automation Congress. IEEE, 2015, pp. 512–517.
     RGBD salient object detection,” in Proceedings of the IEEE Conference     [75] Huan Du, Zhi Liu, Hangke Song, Lin Mei, and Zheng Xu, “Improving
     on Computer Vision and Pattern Recognition, 2019, pp. 3927–3936.               RGBD saliency detection using progressive region classification and
[54] Yongri Piao, Wei Ji, Jingjing Li, Miao Zhang, and Huchuan Lu,                  saliency fusion,” IEEE Access, vol. 4, pp. 8987–8994, 2016.
     “Depth-induced multi-scale recurrent attention network for saliency       [76] Song-Tao Wang, Zhen Zhou, Han-Bing Qu, and Bin Li, “Rgb-d
     detection,” in Proceedings of the IEEE International Conference on             saliency detection under bayesian framework,” in Proceedings of
     Computer Vision, 2019, pp. 7254–7263.                                          International Conference on Pattern Recognition. IEEE, 2016, pp.
[55] Hao Chen, Youfu Li, and Dan Su, “Multi-modal fusion network with               1881–1886.
     multi-scale multi-path and cross-modal interactions for RGB-D salient     [77] Hao Sheng, Xiaoyu Liu, and Shuo Zhang, “Saliency analysis based
     object detection,” Pattern Recognition, vol. 86, pp. 376–385, 2019.            on depth contrast increased,” in Proceedings of IEEE International
[56] Ran Ju, Ling Ge, Wenjing Geng, Tongwei Ren, and Gangshan Wu,                   Conference on Acoustics, Speech and Signal Processing. IEEE, 2016,
     “Depth saliency based on anisotropic center-surround difference,” in           pp. 1347–1351.
     Proceedings of the IEEE International Conference on Image Process-        [78] Hangke Song, Zhi Liu, Huan Du, and Guangling Sun, “Depth-aware
     ing. IEEE, 2014, pp. 1115–1119.                                                saliency detection using discriminative saliency fusion,” in Proceedings
[57] David Feng, Nick Barnes, Shaodi You, and Chris McCarthy, “Local                of IEEE International Conference on Acoustics, Speech and Signal
     background enclosure for RGB-D salient object detection,” in Pro-              Processing. IEEE, 2016, pp. 1626–1630.
     ceedings of the IEEE Conference on Computer Vision and Pattern            [79] Song-Tao Wang, Zhen Zhou, Han-Bing Qu, and Bin Li, “Visual
     Recognition, 2016, pp. 2343–2350.                                              saliency detection for RGB-D images with generative model,” in
[58] Junwei Han, Hao Chen, Nian Liu, Chenggang Yan, and Xuelong Li,                 Proceedings of the Asian Conference on Computer Vision. Springer,
     “Cnns-based RGB-D saliency detection via cross-view transfer and               2016, pp. 20–35.
     multiview fusion,” IEEE Transactions on Cybernetics, vol. 48, no.         [80] David Feng, Nick Barnes, and Shaodi You, “Hoso: Histogram of
     11, pp. 3171–3183, 2017.                                                       surface orientation for rgb-d salient object detection,” in Proceedings of
[59] Ali Borji, Ming-Ming Cheng, Huaizu Jiang, and Jia Li, “Salient object          the International Conference on Digital Image Computing: Techniques
     detection: A benchmark,” IEEE Transactions on Image Processing,                and Applications. IEEE, 2017, pp. 1–8.
     vol. 24, no. 12, pp. 5706–5722, 2015.                                     [81] Hao Chen, You-Fu Li, and Dan Su, “M3net: Multi-scale multi-
[60] Runmin Cong, Jianjun Lei, Huazhu Fu, Ming-Ming Cheng, Weisi                    path multi-modal fusion network and example application to rgb-d
     Lin, and Qingming Huang, “Review of visual saliency detection                  salient object detection,” in Proceedings of IEEE/RSJ International
     with comprehensive information,” IEEE Transactions on Circuits and             Conference on Intelligent Robots and Systems. IEEE, 2017, pp. 4911–
     Systems for Video Technology, vol. 29, no. 10, pp. 2941–2959, 2018.            4916.
[61] Dingwen Zhang, Huazhu Fu, Junwei Han, Ali Borji, and Xuelong              [82] Hao Chen, Youfu Li, and Dan Su, “RGB-D saliency detection by
     Li, “A review of co-saliency detection algorithms: Fundamentals,               multi-stream late fusion network,” in Proceedings of the International
     applications, and challenges,” ACM Transactions on Intelligent Systems         Conference on Computer Vision Systems. Springer, 2017, pp. 459–468.
     and Technology, vol. 9, no. 4, pp. 1–31, 2018.                            [83] Riku Shigematsu, David Feng, Shaodi You, and Nick Barnes, “Learn-
[62] Junwei Han, Dingwen Zhang, Gong Cheng, Nian Liu, and Dong Xu,                  ing RGB-D salient object detection using background enclosure, depth
     “Advanced deep-learning techniques for salient and category-specific           contrast, and top-down features,” in Proceedings of the IEEE Inter-
     object detection: a survey,” IEEE Signal Processing Magazine, vol. 35,         national Conference on Computer Vision Workshops, 2017, pp. 2749–
     no. 1, pp. 84–100, 2018.                                                       2757.
[63] Tam V Nguyen, Qi Zhao, and Shuicheng Yan, “Attentive systems: A           [84] Chunbiao Zhu, Ge Li, Wenmin Wang, and Ronggang Wang, “An
     survey,” International Journal of Computer Vision, vol. 126, no. 1, pp.        innovative salient object detection using center-dark channel prior,” in
     86–110, 2018.                                                                  Proceedings of the IEEE International Conference on Computer Vision
[64] Ali Borji, Ming-Ming Cheng, Qibin Hou, Huaizu Jiang, and Jia Li,               Workshops, 2017, pp. 1509–1515.
     “Salient object detection: A survey,” Computational Visual Media, pp.     [85] Chunbiao Zhu and Ge Li, “A three-pathway psychobiological frame-
     1–34, 2014.                                                                    work of salient object detection using stereoscopic technology,” in
[65] Zhong-Qiu Zhao, Peng Zheng, Shou-tao Xu, and Xindong Wu, “Object               Proceedings of the IEEE International Conference on Computer Vision
     detection with deep learning: A review,” IEEE Transactions on Neural           Workshops, 2017, pp. 3008–3014.
     Networks and Learning Systems, vol. 30, no. 11, pp. 3212–3232, 2019.      [86] Anzhi Wang and Minghui Wang, “RGB-D salient object detection via
[66] Wenguan Wang, Qiuxia Lai, Huazhu Fu, Jianbing Shen, Haibin Ling,               minimum barrier distance transform and saliency fusion,” IEEE Signal
     and Ruigang Yang, “Salient object detection in the deep learning era:          Processing Letters, vol. 24, no. 5, pp. 663–667, 2017.
     An in-depth survey,” arXiv preprint arXiv:1904.09146, 2019.               [87] Hangke Song, Zhi Liu, Huan Du, Guangling Sun, Olivier Le Meur, and
[67] Hailong Zhang, Jianjun Lei, Xiaohong Fan, Meimin Wu, Peng Zhang,               Tongwei Ren, “Depth-aware salient object detection and segmentation
     and Shupo Bu, “Depth combined saliency detection based on region               via multiscale discriminative saliency fusion and bootstrap learning,”
     contrast model,” in Proceedings of International Conference on                 IEEE Transactions on Image Processing, vol. 26, no. 9, pp. 4204–4216,
     Computer Science & Education. IEEE, 2012, pp. 763–766.                         2017.
                                                                                                                                                            23

 [88] Runmin Cong, Jianjun Lei, Huazhu Fu, Weisi Lin, Qingming Huang,            [109] Rui Huang, Yan Xing, and ZeZheng Wang, “RGB-D salient object
      Xiaochun Cao, and Chunping Hou, “An iterative co-saliency framework              detection by a CNN with multiple layers fusion,” IEEE Signal
      for RGBD images,” IEEE Transactions on Cybernetics, vol. 49, no. 1,              Processing Letters, vol. 26, no. 4, pp. 552–556, 2019.
      pp. 233–246, 2017.                                                         [110] Di Liu, Yaosi Hu, Kao Zhang, and Zhenzhong Chen, “Two-stream
 [89] Nevrez Imamoglu, Wataru Shimoda, Chi Zhang, Yuming Fang, Asako                   refinement network for rgb-d saliency detection,” in Proceedings of
      Kanezaki, Keiji Yanai, and Yoshifumi Nishida, “An integration of                 IEEE International Conference on Image Processing. IEEE, 2019, pp.
      bottom-up and top-down salient cues on rgb-d data: saliency from                 3925–3929.
      objectness versus non-objectness,” Signal, Image and Video Processing,     [111] Huan Du, Zhi Liu, and Ran Shi, “Salient object segmentation based
      vol. 12, no. 2, pp. 307–314, 2018.                                               on depth-aware image layering,” Multimedia Tools and Applications,
 [90] Runmin Cong, Jianjun Lei, Huazhu Fu, Qingming Huang, Xiaochun                    vol. 78, no. 9, pp. 12125–12138, 2019.
      Cao, and Nam Ling, “HSCS: Hierarchical sparsity based co-saliency          [112] Wujie Zhou, Ying Lv, Jingsheng Lei, and Lu Yu, “Global and local-
      detection for RGBD images,” IEEE Transactions on Multimedia, vol.                contrast guides content-aware fusion for rgb-d saliency prediction,”
      21, no. 7, pp. 1660–1671, 2018.                                                  IEEE Transactions on Systems, Man, and Cybernetics: Systems, 2019.
 [91] Runmin Cong, Jianjun Lei, Huazhu Fu, Qingming Huang, Xiaochun              [113] Chih-Yao Ma and Hsueh-Ming Hang, “Learning-based saliency model
      Cao, and Chunping Hou, “Co-saliency detection for RGBD images                    with depth information,” Journal of vision, vol. 15, no. 6, pp. 19–19,
      based on multi-constraint feature matching and cross label propaga-              2015.
      tion,” IEEE Transactions on Image Processing, vol. 27, no. 2, pp.          [114] Zhigang Jin, Jingkun Li, and Dong Li, “Co-saliency detection for rgbd
      568–579, 2017.                                                                   images based on effective propagation mechanism,” IEEE Access, vol.
 [92] Hao Chen and Youfu Li, “Progressively complementarity-aware fusion               7, pp. 141311–141318, 2019.
      network for RGB-D salient object detection,” in Proceedings of the         [115] Yu Ding, Zhi Liu, Mengke Huang, Ran Shi, and Xiangyang Wang,
      IEEE Conference on Computer Vision and Pattern Recognition, 2018,                “Depth-aware saliency detection using convolutional neural networks,”
      pp. 3051–3060.                                                                   Journal of Visual Communication and Image Representation, vol. 61,
 [93] Posheng Huang, Chin-Han Shen, and Hsu-Feng Hsiao, “Rgbd salient                  pp. 1–9, 2019.
      object detection using spatially coherent deep learning framework,” in     [116] Zuyao Chen and Qingming Huang, “Depth potentiality-aware gated
      Proceedings of the IEEE International Conference on Digital Signal               attention network for RGB-D salient object detection,” arXiv preprint
      Processing. IEEE, 2018, pp. 1–5.                                                 arXiv:2003.08608, 2020.
 [94] Hao Chen, You-Fu Li, and Dan Su, “Attention-aware cross-modal              [117] Yue Wang, Yuke Li, James H Elder, Huchuan Lu, and Runmin
      cross-level fusion network for RGB-D salient object detection,” in               Wu, “Synergistic saliency and depth prediction for RGB-D saliency
      Proceedings of the IEEE/RSJ International Conference on Intelligent              detection,” arXiv preprint arXiv:2007.01711, 2020.
      Robots and Systems. IEEE, 2018, pp. 6821–6826.                             [118] Bo Jiang, Zitai Zhou, Xiao Wang, Jin Tang, and Bin Luo, “cmsalgan:
 [95] Fangfang Liang, Lijuan Duan, Wei Ma, Yuanhua Qiao, Zhi Cai, and                  RGB-D salient object detection with cross-view generative adversarial
      Laiyun Qing, “Stereoscopic saliency model using contrast and depth-              networks,” IEEE Transactions on Multimedia, 2020.
      guided-background prior,” Neurocomputing, vol. 275, pp. 2227–2238,
                                                                                 [119] Fen Xiao, Bin Li, Yimu Peng, Chunhong Cao, Kai Hu, and Xieping
      2018.
                                                                                       Gao, “Multi-modal weights sharing and hierarchical feature fusion for
 [96] Zhengyi Liu, Song Shi, Quntao Duan, Wei Zhang, and Peng Zhao,
                                                                                       rgbd salient object detection,” IEEE Access, vol. 8, pp. 26602–26611,
      “Salient object detection for RGB-D image by single stream recurrent
                                                                                       2020.
      convolution neural network,” Neurocomputing, vol. 363, pp. 46–57,
                                                                                 [120] Zhao Zhang, Zheng Lin, Jun Xu, Wenda Jin, Shao-Ping Lu, and
      2019.
                                                                                       Deng-Ping Fan, “Bilateral attention network for rgb-d salient object
 [97] Chunbiao Zhu, Xing Cai, Kan Huang, Thomas H Li, and Ge Li,
                                                                                       detection,” arXiv preprint arXiv:2004.14582, 2020.
      “PDNet: Prior-model guided depth-enhanced network for salient object
      detection,” in Proceedings of the IEEE International Conference on         [121] Wujie Zhou, Yuzhen Chen, Chang Liu, and Lu Yu, “GFNet: Gate fusion
      Multimedia and Expo. IEEE, 2019, pp. 199–204.                                    network with res2net for detecting salient objects in rgb-d images,”
 [98] Yongri Piao, Xiao Li, Miao Zhang, Jingyi Yu, and Huchuan Lu,                     IEEE Signal Processing Letters, 2020.
      “Saliency detection via depth-induced cellular automata on light field,”   [122] Zhengyi Liu, Jiting Tang, Qian Xiang, and Peng Zhao, “Salient
      IEEE Transactions on Image Processing, vol. 29, pp. 1879–1889, 2020.             object detection for rgb-d images by generative adversarial network,”
 [99] Hao Chen and Youfu Li, “Three-stream attention-aware network                     Multimedia Tools and Applications, pp. 1–23, 2020.
      for RGB-D salient object detection,” IEEE Transactions on Image            [123] Gongyang Li, Zhi Liu, Linwei Ye, Yang Wang, and Haibin Ling,
      Processing, vol. 28, no. 6, pp. 2825–2835, 2019.                                 “Cross-modal weighting network for rgb-d salient object detection,” in
[100] Hao Chen, Youfu Li, and Dan Su, “Discriminative cross-modal transfer             Proceedings of the European Conference on Computer Vision. Springer,
      learning and densely cross-level feedback fusion for RGB-D salient               2020.
      object detection,” IEEE Transactions on Cybernetics, 2019.                 [124] Youwei Pang, Lihe Zhang, Xiaoqi Zhao, and Huchuan Lu, “Hierarchi-
[101] Runmin Cong, Jianjun Lei, Huazhu Fu, Junhui Hou, Qingming Huang,                 cal dynamic filtering network for RGB-D salient object detection,” in
      and Sam Kwong, “Going from RGB to RGBD saliency: A depth-                        Proceedings of the European Conference on Computer Vision. Springer,
      guided transformation model,” IEEE Transactions on Cybernetics,                  2020.
      2019.                                                                      [125] Ao Luo, Xin Li, Fan Yang, Zhicheng Jiao, Hong Cheng, and Siwei Lyu,
[102] Ningning Wang and Xiaojin Gong, “Adaptive fusion for RGB-D salient               “Cascade graph neural networks for rgb-d salient object detection,”
      object detection,” IEEE Access, vol. 7, pp. 55277–55284, 2019.                   in Proceedings of the Proceedings of the European Conference on
[103] Xiaofei Zhou, Gongyang Li, Chen Gong, Zhi Liu, and Jiyong Zhang,                 Computer Vision. Springer, 2020.
      “Attention-guided RGBD saliency detection using appearance informa-        [126] Chongyi Li, Runmin Cong, Yongri Piao, Qianqian Xu, and
      tion,” Image and Vision Computing, vol. 95, pp. 103888, 2020.                    Chen Change Loy, “Rgb-d salient object detection with cross-modality
[104] Zhengyi Liu, Wei Zhang, and Peng Zhao, “A cross-modal adaptive                   modulation and selection,” in Proceedings of the European Conference
      gated fusion generative adversarial network for RGB-D salient object             on Computer Vision. Springer, 2020.
      detection,” Neurocomputing, 2020.                                          [127] Xiaoqi Zhao, Lihe Zhang, Youwei Pang, Huchuan Lu, and Lei Zhang,
[105] Fangfang Liang, Lijuan Duan, Wei Ma, Yuanhua Qiao, Zhi Cai, Jun                  “A single stream network for robust and real-time rgb-d salient object
      Miao, and Qixiang Ye, “Cocnn: RGB-D deep fusion for stereoscopic                 detection,” in Proceedings of the European Conference on Computer
      salient object detection,” Pattern Recognition, p. 107329, 2020.                 Vision. Springer, 2020.
[106] Chongyi Li, Runmin Cong, Sam Kwong, Junhui Hou, Huazhu Fu,                 [128] Wei Ji, Jingjing Li, Miao Zhang, Yongri Piao, and Huchuan Lu,
      Guopu Zhu, Dingwen Zhang, and Qingming Huang, “ASIF-Net:                         “Accurate rgb-d salient object detection via collaborative learning,” in
      Attention steered interweave fusion network for RGB-D salient object             ECCV, 2020.
      detection,” IEEE Transactions on Cybernetics, 2020.                        [129] Deng-Ping Fan, Yingjie Zhai, Ali Borji, Jufeng Yang, and Ling Shao,
[107] Rui Huang, Yan Xing, and Yaobin Zou, “Triple-complementary                       “Bbs-net: Rgb-d salient object detection with a bifurcated backbone
      network for RGB-D salient object detection,” IEEE Signal Processing              strategy network,” in Proceedings of the European Conference on
      Letters, 2020.                                                                   Computer Vision. Springer, 2020.
[108] Chenglizhao Chen, Jipeng Wei, Chong Peng, Weizhong Zhang, and              [130] Miao Zhang, Sun Xiao Fei, Jie Liu, Shuang Xu, Yongri Piao, and
      Hong Qin, “Improved saliency detection in RGB-D images using two-                Huchuan Lu, “Asymmetric two-stream architecture for accurate rgb-d
      phase depth estimation and selective deep fusion,” IEEE Transactions             saliency detection,” in Proceedings of the European Conference on
      on Image Processing, vol. 29, pp. 4296–4307, 2020.                               Computer Vision. Springer, 2020.
                                                                                                                                                               24

[131] Shuhan Chen and Yun Fu, “Progressively guided alternate refinement                  Proceedings of the International Conference on Neural Information
      network for rgb-d salient object detection,” in Proceedings of the                  Processing Systems, 2019, pp. 896–906.
      European Conference on Computer Vision. Springer, 2020.                       [153] Yongri Piao, Zhengkun Rong, Miao Zhang, and Huchuan Lu, “Exploit
[132] Zhou Huang, Huai-Xin Chen, Tao Zhou, Yun-Zhi Yang, and Chang-Yin                    and replace: An asymmetrical two-stream architecture for versatile light
      Wang, “Multi-level cross-modal interaction network for rgb-d salient                field saliency detection,” in Proceedings of the Association for the
      object detection,” arXiv preprint arXiv:2007.14352, 2020.                           Advancement of Artificial Intelligence, 2020.
[133] Xuehao Wang, Shuai Li, Chenglizhao Chen, Yuming Fang, Aimin                   [154] Xue Wang, Yingying Dong, Qi Zhang, and Qing Wang, “Region-
      Hao, and Hong Qin, “Data-level recombination and lightweight fusion                 based depth feature descriptor for saliency detection on light field,”
      scheme for rgb-d salient object detection,” IEEE Transactions on Image              Multimedia Tools and Applications, 2020.
      Processing, 2020.                                                             [155] Miao Zhang, Wei Ji, Yongri Piao, Jingjing Li, Yu Zhang, Shuang Xu,
[134] Xuehao Wang, Shuai Li, Chenglizhao Chen, Aimin Hao, and Hong Qin,                   and Huchuan Lu, “Lfnet: Light field fusion network for salient object
      “Knowing depth quality in advance: A depth quality assessment method                detection,” IEEE Transactions on Image Processing, vol. 29, pp. 6276–
      for rgb-d salient object detection,” arXiv preprint arXiv:2008.04157,               6287, 2020.
      2020.                                                                         [156] Jun Zhang, Yamei Liu, Shengping Zhang, Ronald Poppe, and Meng
[135] Chenglizhao Chen, Jipeng Wei, Chong Peng, and Hong Qin, “Depth                      Wang, “Light field saliency detection with deep convolutional net-
      quality aware salient object detection,” IEEE Transactions on Image                 works,” IEEE Transactions on Image Processing, vol. 29, pp. 4421–
      Processing, 2020.                                                                   4434, 2020.
[136] Jiawei Zhao, Yifan Zhao, Jia Li, and Xiaowu Chen, “Is depth really            [157] Radhakrishna Achanta, Sheila Hemami, Francisco Estrada, and Sabine
      necessary for salient object detection,” in ACM Multimedia, 2020.                   Susstrunk, “Frequency-tuned salient region detection,” in Proceedings
[137] Hao Chen, Yongjian Deng, Youfu Li, Tzu-Yi Hung, and Guosheng Lin,                   of the IEEE conference on Computer Vision and Pattern Recognition.
      “Rgbd salient object detection via disentangled cross-modal fusion,”                IEEE, 2009, pp. 1597–1604.
      IEEE Transactions on Image Processing, vol. 29, pp. 8407–8416, 2020.          [158] Federico Perazzi, Philipp Krähenbühl, Yael Pritch, and Alexander
[138] Yuzhen Niu, Yujie Geng, Xueqing Li, and Feng Liu, “Leveraging stere-                Hornung, “Saliency filters: Contrast based filtering for salient region
      opsis for saliency analysis,” in Proceedings of the IEEE Conference on              detection,” in Proceedings of the IEEE Conference on Computer Vision
      Computer Vision and Pattern Recognition. IEEE, 2012, pp. 454–461.                   and Pattern Recognition. IEEE, 2012, pp. 733–740.
[139] Nianyi Li, Jinwei Ye, Yu Ji, Haibin Ling, and Jingyi Yu, “Saliency            [159] Deng-Ping Fan, Ming-Ming Cheng, Yun Liu, Tao Li, and Ali Borji,
      detection on light field,” in Proceedings of the IEEE Conference on                 “Structure-measure: A new way to evaluate foreground maps,” in
      Computer Vision and Pattern Recognition, 2014, pp. 2806–2813.                       Proceedings of the IEEE International Conference on Computer Vision,
[140] yu Zhang et al., “Feature reintegration over differential treatment:                2017, pp. 4548–4557.
      A top-down and adaptive fusion network for rgb-d salient object               [160] Deng-Ping Fan, Cheng Gong, Yang Cao, Bo Ren, Ming-Ming Cheng,
      detection,” in ACM Multimedia, 2020.                                                and Ali Borji, “Enhanced-alignment measure for binary foreground
[141] Nianyi Li, Bilin Sun, and Jingyi Yu, “A weighted sparse coding                      map evaluation,” in Proceedings of the International Joint Conferences
      framework for saliency detection,” in Proceedings of the IEEE                       on Artificial Intelligence, 2018, pp. 698–704.
      Conference on Computer Vision and Pattern Recognition, 2015, pp.              [161] Yao Qin, Huchuan Lu, Yiqun Xu, and He Wang, “Saliency detection
      5216–5223.                                                                          via cellular automata,” in Proceedings of the IEEE Conference on
[142] Jun Zhang, Meng Wang, Jun Gao, Yi Wang, Xudong Zhang, and                           Computer Vision and Pattern Recognition, 2015, pp. 110–119.
      Xindong Wu, “Saliency detection with a deeper investigation of                [162] Li Zhou, Zhaohui Yang, Qing Yuan, Zongtan Zhou, and Dewen Hu,
      light field.,” in Proceedings of the International Joint Conference on              “Salient region detection via integrating diffusion-based compactness
      Artificial Intelligence, 2015, pp. 2212–2218.                                       and local contrast,” IEEE Transactions on Image Processing, vol. 24,
[143] Hao Sheng, Shuo Zhang, Xiaoyu Liu, and Zhang Xiong, “Relative                       no. 11, pp. 3308–3320, 2015.
      location for light field saliency detection,” in Proceedings of the IEEE      [163] Xiaoming Huang and Yu-Jin Zhang, “300-fps salient object detection
      Conference on Acoustics, Speech and Signal Processing. IEEE, 2016,                  via minimum directional contrast,” IEEE Transactions on Image
      pp. 1631–1635.                                                                      Processing, vol. 26, no. 9, pp. 4243–4254, 2017.
[144] Jun Zhang, Meng Wang, Liang Lin, Xun Yang, Jun Gao, and Yong                  [164] Fang Huang, Jinqing Qi, Huchuan Lu, Lihe Zhang, and Xiang Ruan,
      Rui, “Saliency detection on light field: A multi-cue approach,”                     “Salient object detection via multiple instance learning,” IEEE Trans-
      ACM Transactions on Multimedia Computing, Communications, and                       actions on Image Processing, vol. 26, no. 4, pp. 1911–1922, 2017.
      Applications, vol. 13, no. 3, pp. 1–22, 2017.                                 [165] Xiaoming Huang and Yujin Zhang, “Water flow driven salient object
[145] Anzhi Wang, Minghui Wang, Xiaoyan Li, Zetian Mi, and Huan                           detection at 180 fps,” Pattern Recognition, vol. 76, pp. 95–107, 2018.
      Zhou, “A two-stage bayesian integration framework for salient object          [166] Chang Xu, Dacheng Tao, and Chao Xu, “Multi-view learning with
      detection on light field,” Neural Processing Letters, vol. 46, no. 3, pp.           incomplete views,” IEEE Transactions on Image Processing, vol. 24,
      1083–1094, 2017.                                                                    no. 12, pp. 5812–5825, 2015.
[146] Nianyi Li, Jinwei Ye, Yu Ji, Haibing Ling, and Jingyi Yu, “Saliency           [167] Tao Zhou, Kim-Han Thung, Xiaofeng Zhu, and Dinggang Shen,
      detection on light field,” IEEE Transactions on Pattern Analysis and                “Effective feature learning and fusion of multimodality data using
      Machine Intelligence, vol. 39, no. 8, pp. 1605–1616, 2017.                          stage-wise deep neural network for dementia diagnosis,” Human Brain
[147] Chao Li, Bin Zhan, Shuo Zhang, and Hao Sheng, “Saliency detection                   Mapping, vol. 40, no. 3, pp. 1001–1016, 2019.
      with relative location measure in light field image,” in Proceedings of       [168] Tao Zhou, Mingxia Liu, Kim-Han Thung, and Dinggang Shen, “La-
      the International Conference on Image, Vision and Computing. IEEE,                  tent representation learning for alzheimer’s disease diagnosis with
      2017, pp. 8–12.                                                                     incomplete multi-modality neuroimaging and genetic data,” IEEE
[148] Shizheng Wang, Wenjuan Liao, Phil Surman, Zhigang Tu, Yuanjin                       Transactions on Medical Imaging, vol. 38, no. 10, pp. 2411–2422,
      Zheng, and Junsong Yuan, “Salience guided depth calibration for per-                2019.
      ceptually optimized compressive light field 3d display,” in Proceedings       [169] Tao Zhou, Kim-Han Thung, Mingxia Liu, Feng Shi, Changqing Zhang,
      of the IEEE Conference on Computer Vision and Pattern Recognition,                  and Dinggang Shen, “Multi-modal latent space inducing ensemble
      2018, pp. 2031–2040.                                                                svm classifier for early dementia diagnosis with neuroimaging data,”
[149] Yongri Piao, Xiao Li, and Miao Zhang, “Depth-induced cellular                       Medical Image Analysis, vol. 60, pp. 101630, 2020.
      automata for light field saliency,” in Frontiers in Optics. Optical Society   [170] Tao Zhou, Huazhu Fu, Geng Chen, Jianbing Shen, and Ling Shao,
      of America, 2018, pp. FTh3E–3.                                                      “Hi-net: hybrid-fusion network for multi-modal MR image synthesis,”
[150] Tiantian Wang, Yongri Piao, Xiao Li, Lihe Zhang, and Huchuan Lu,                    IEEE Transactions on Medical Imaging, vol. 39, no. 9, pp. 2772–2781,
      “Deep learning for light field saliency detection,” in Proceedings of the           2020.
      IEEE International Conference on Computer Vision, 2019, pp. 8838–             [171] Clément Godard, Oisin Mac Aodha, and Gabriel J Brostow, “Unsu-
      8848.                                                                               pervised monocular depth estimation with left-right consistency,” in
[151] Yongri Piao, Zhengkun Rong, Miao Zhang, Xiao Li, and Huchuan                        Proceedings of the IEEE Conference on Computer Vision and Pattern
      Lu, “Deep light-field-driven saliency detection from a single view,”                Recognition, 2017, pp. 270–279.
      in Proceedings of the International Joint Conference on Artificial            [172] Fayao Liu, Chunhua Shen, and Guosheng Lin, “Deep convolutional
      Intelligence, 2019.                                                                 neural fields for depth estimation from a single image,” in Proceedings
[152] Miao Zhang, Jingjing Li, JI WEI, Yongri Piao, and Huchuan Lu,                       of the IEEE Conference on Computer Vision and Pattern Recognition,
      “Memory-oriented decoder for light field salient object detection,” in              2015, pp. 5162–5170.
                                                                                                                                                           25

[173] Lijun Wang, Jianming Zhang, Oliver Wang, Zhe Lin, and Huchuan             [193] Kevin Lai, Liefeng Bo, Xiaofeng Ren, and Dieter Fox, “A large-scale
      Lu, “Sdc-depth: Semantic divide-and-conquer network for monocular               hierarchical multi-view rgb-d object dataset,” in Proceedings of the
      depth estimation,” in Proceedings of the IEEE Conference on Computer            IEEE International Conference on Robotics and Automation. IEEE,
      Vision and Pattern Recognition, 2020, pp. 541–550.                              2011, pp. 1817–1824.
[174] Lei Jin, Yanyu Xu, Jia Zheng, Junfei Zhang, Rui Tang, Shugong             [194] Jing Zhang, Wanqing Li, Pichao Wang, Philip Ogunbona, Song Liu,
      Xu, Jingyi Yu, and Shenghua Gao, “Geometric structure based and                 and Chang Tang, “A large scale rgb-d dataset for action recognition,” in
      regularized depth estimation from 360 indoor imagery,” in Proceedings           Proceedings of the International Workshop on Understanding Human
      of the IEEE Conference on Computer Vision and Pattern Recognition,              Activities through 3D Sensors. Springer, 2016, pp. 101–114.
      2020, pp. 889–898.                                                        [195] Yihui He, Ji Lin, Zhijian Liu, Hanrui Wang, Li-Jia Li, and Song Han,
[175] Mehdi Mirza and Simon Osindero, “Conditional generative adversarial             “Amc: Automl for model compression and acceleration on mobile
      nets,” arXiv preprint arXiv:1411.1784, 2014.                                    devices,” in Proceedings of the European Conference on Computer
[176] Dandan Zhu, Lei Dai, Ye Luo, Guokai Zhang, Xuan Shao, Laurent Itti,             Vision. Springer, 2018, pp. 784–800.
      and Jianwei Lu, “Multi-scale adversarial feature learning for saliency    [196] Yu Cheng, Duo Wang, Pan Zhou, and Tao Zhang, “A survey of model
      detection,” Symmetry, vol. 10, no. 10, pp. 457, 2018.                           compression and acceleration for deep neural networks,” arXiv preprint
[177] Junting Pan, Cristian Canton Ferrer, Kevin McGuinness, et al., “Salgan:         arXiv:1710.09282, 2017.
      Visual saliency prediction with generative adversarial networks,” arXiv   [197] Yunpeng Ma, Dengdi Sun, Qianqian Meng, Zhuanlian Ding, and Chen-
      preprint arXiv:1701.01081, 2017.                                                glong Li, “Learning multiscale deep features and svm regressors for
[178] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion               adaptive rgb-t saliency detection,” in Proceedings of the International
      Jones, Aidan N Gomez, Łukasz Kaiser, and Illia Polosukhin, “Attention           Symposium on Computational Intelligence and Design. IEEE, 2017,
      is all you need,” in Proceedings of the Conference on Neural                    vol. 1, pp. 389–392.
      Information Processing Systems, 2017, pp. 5998–6008.                      [198] Chenglong Li, Guizhao Wang, Yunpeng Ma, Aihua Zheng, Bin
[179] Fei Wang, Mengqing Jiang, Chen Qian, Shuo Yang, Cheng Li,                       Luo, and Jin Tang, “A unified rgb-t saliency detection benchmark:
      Honggang Zhang, Xiaogang Wang, and Xiaoou Tang, “Residual                       dataset, baselines, analysis and a novel approach,” arXiv preprint
      attention network for image classification,” in Proceedings of the IEEE         arXiv:1701.02829, 2017.
      Conference on Computer Vision and Pattern Recognition. Springer,          [199] Guizhao Wang, Chenglong Li, Yunpeng Ma, Aihua Zheng, Jin Tang,
      2017, pp. 3156–3164.                                                            and Bin Luo, “Rgb-T saliency detection benchmark: Dataset, baselines,
[180] Hao-Shu Fang, Jinkun Cao, Yu-Wing Tai, and Cewu Lu, “Pairwise                   analysis and a novel approach,” in Proceedings of the Chinese
      body-part attention for recognizing human-object interactions,” in              Conference on Image and Graphics Technologies. Springer, 2018, pp.
      Proceedings of the European Conference on Computer Vision. Springer,            359–369.
      2018, pp. 51–67.                                                          [200] Dengdi Sun, Sheng Li, Zhuanlian Ding, and Bin Luo, “Rgb-t saliency
[181] Wenguan Wang and Jianbing Shen, “Deep visual attention prediction,”             detection via robust graph learning and collaborative manifold rank-
      IEEE Transactions on Image Processing, vol. 27, no. 5, pp. 2368–2378,           ing,” in Proceedings of the International Conference on Bio-Inspired
      2017.                                                                           Computing: Theories and Applications. Springer, 2019, pp. 670–684.
                                                                                [201] Zhengzheng Tu, Tian Xia, Chenglong Li, Yijuan Lu, and Jin Tang,
[182] Jiasen Lu, Jianwei Yang, Dhruv Batra, and Devi Parikh, “Hierarchical
                                                                                      “M3s-nir: Multi-modal multi-scale noise-insensitive ranking for rgb-
      question-image co-attention for visual question answering,” in Proceed-
                                                                                      t saliency detection,” in Proceedings of the IEEE Conference on
      ings of the International Conference on Neural Information Processing
                                                                                      Multimedia Information Processing and Retrieval. IEEE, 2019, pp.
      Systems, 2016, pp. 289–297.
                                                                                      141–146.
[183] Zhou Yu, Jun Yu, Yuhao Cui, Dacheng Tao, and Qi Tian, “Deep
                                                                                [202] Zhengzheng Tu, Zhun Li, Chenglong Li, Yang Lang, and Jin Tang,
      modular co-attention networks for visual question answering,” in
                                                                                      “Multi-interactive encoder-decoder network for rgbt salient object
      Proceedings of the IEEE Conference on Computer Vision and Pattern
                                                                                      detection,” arXiv preprint arXiv:2005.02315, 2020.
      Recognition, 2019, pp. 6281–6290.
                                                                                [203] Zhengzheng Tu, Tian Xia, Chenglong Li, Xiaoxiao Wang, Yan Ma,
[184] Xiankai Lu, Wenguan Wang, Chao Ma, Jianbing Shen, Ling Shao,                    and Jin Tang, “Rgb-t image saliency detection via collaborative graph
      and Fatih Porikli, “See more, know more: Unsupervised video object              learning,” IEEE Transactions on Multimedia, vol. 22, no. 1, pp. 160–
      segmentation with co-attention siamese networks,” in Proceedings of             173, 2019.
      the IEEE Conference on Computer Vision and Pattern Recognition,           [204] Qiang Zhang, Nianchang Huang, Lin Yao, Dingwen Zhang, Caifeng
      2019, pp. 3623–3632.                                                            Shan, and Jungong Han, “Rgb-t salient object detection via fusing
[185] Yu Zeng, Yunzhi Zhuge, Huchuan Lu, Lihe Zhang, Mingyang Qian,                   multi-level cnn features,” IEEE Transactions on Image Processing,
      and Yizhou Yu, “Multi-source weak supervision for saliency detection,”          vol. 29, pp. 3321–3335, 2019.
      in Proceedings of the IEEE Conference on Computer Vision and Pattern      [205] Zhengzheng Tu, Yan Ma, Zhun Li, Chenglong Li, Jieming Xu, and
      Recognition, 2019, pp. 6074–6083.                                               Yongtao Liu, “Rgbt salient object detection: A large-scale dataset and
[186] Dingwen Zhang, Deyu Meng, Long Zhao, and Junwei Han, “Bridging                  benchmark,” arXiv preprint arXiv:2007.03262, 2020.
      saliency detection to weakly supervised object detection based on self-
      paced curriculum learning,” arXiv preprint arXiv:1703.01290, 2017.
[187] Mingyang Qian, Jinqing Qi, Lihe Zhang, Mengyang Feng, and
      Huchuan Lu, “Language-aware weak supervision for salient object
      detection,” Pattern Recognition, vol. 96, pp. 106955, 2019.
[188] Pengxiang Yan, Guanbin Li, Yuan Xie, Zhen Li, Chuan Wang, Tianshui
      Chen, and Liang Lin, “Semi-supervised video salient object detection
      using pseudo-labels,” in Proceedings of the IEEE International Con-
      ference on Computer Vision, 2019, pp. 7284–7293.
[189] Yuan Zhou, Shuwei Huo, Wei Xiang, Chunping Hou, and Sun-Yuan
      Kung, “Semi-supervised salient object detection using a linear feedback
      control system model,” IEEE Transactions on Cybernetics, vol. 49, no.
      4, pp. 1173–1185, 2018.
[190] Dingwen Zhang, Junwei Han, and Yu Zhang, “Supervision by fusion:
      Towards unsupervised learning of deep salient object detector,” in
      Proceedings of the IEEE International Conference on Computer Vision,
      2017, pp. 4048–4056.
[191] Tianlong Chen, Sijia Liu, Shiyu Chang, Yu Cheng, Lisa Amini, and
      Zhangyang Wang, “Adversarial robustness: From self-supervised pre-
      training to fine-tuning,” in Proceedings of the IEEE Conference on
      Computer Vision and Pattern Recognition, 2020, pp. 699–708.
[192] Angela Dai, Christian Diller, and Matthias Nießner, “Sg-nn: Sparse
      generative neural networks for self-supervised scene completion of rgb-
      d scans,” in Proceedings of the IEEE Conference on Computer Vision
      and Pattern Recognition, 2020, pp. 849–858.
