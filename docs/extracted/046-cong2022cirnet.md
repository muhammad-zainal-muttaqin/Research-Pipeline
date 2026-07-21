---
source_id: 046
bibtex_key: cong2022cirnet
title: CIR-Net: Cross-modality Interaction and Refinement for RGB-D Salient Object Detection
year: 2022
domain_theme: RGB-D SOD
verified_pdf: 46_CIR-Net.pdf
char_count: 128367
---

1

                                                 CIR-Net: Cross-modality Interaction and
                                             Refinement for RGB-D Salient Object Detection
                                           Runmin Cong, Member, IEEE, Qinwei Lin, Chen Zhang, Chongyi Li, Xiaochun Cao, Senior Member, IEEE,
                                                         Qingming Huang, Fellow, IEEE, and Yao Zhao, Senior Member, IEEE

                                           Abstract—Focusing on the issue of how to effectively capture
                                        and utilize cross-modality information in RGB-D salient object
                                        detection (SOD) task, we present a convolutional neural network
arXiv:2210.02843v1 [cs.CV] 6 Oct 2022

                                        (CNN) model, named CIR-Net, based on the novel cross-modality
                                        interaction and refinement. For the cross-modality interaction,
                                        1) a progressive attention guided integration unit is proposed
                                        to sufficiently integrate RGB-D feature representations in the
                                        encoder stage, and 2) a convergence aggregation structure is
                                        proposed, which flows the RGB and depth decoding features into
                                        the corresponding RGB-D decoding streams via an importance
                                        gated fusion unit in the decoder stage. For the cross-modality
                                        refinement, we insert a refinement middleware structure between
                                        the encoder and the decoder, in which the RGB, depth, and                         (a)          (b)         (c)          (d)         (e)          (f)
                                        RGB-D encoder features are further refined by successively using
                                        a self-modality attention refinement unit and a cross-modality                Fig. 1. Visual examples of different methods. (a) RGB images. (b) Depth
                                        weighting refinement unit. At last, with the gradually refined                maps. (c) Ground truths. (d) Our results. (e)-(f) Saliency maps produced by
                                        features, we predict the saliency map in the decoder stage.                   FRDT [18] and GCPANet [19], respectively.
                                        Extensive experiments on six popular RGB-D SOD benchmarks
                                        demonstrate that our network outperforms the state-of-the-art
                                        saliency detectors both qualitatively and quantitatively. The code
                                        and results can be found from the link of https://rmcong.github.              [4]–[9], retrieval [10], enhancement [11]–[15], and quality
                                        io/proj CIRNet.html.                                                          assessment [16], [17].
                                          Index Terms—Salient object detection, RGB-D images, Cross-                     With the development of SOD task research, there are many
                                        modality attention, Cross-modality interaction.                               subtasks, such as co-salient object detection (CoSOD) [20]–
                                                                                                                      [22], remote sensing SOD [23]–[27], video SOD [28]–[30],
                                                                                                                      light field SOD [31], have also been developed. In fact, the
                                                                 I. I NTRODUCTION
                                                                                                                      natural binocular structure of humans can also perceive the
                                                                                                                      depth of field of the scene, and then generate stereo perception.
                                        W        HEN viewing an image, humans are involuntarily
                                                 attracted by some objects or regions in the image
                                        (e.g., the Smurfs in the second image of Fig. 1), which is
                                                                                                                      Expressing this depth relationship in the form of an image
                                                                                                                      is a depth/disparity map. In recent years, the development
                                        mainly caused by the human visual attention mechanism, and                    and popularization of depth sensors, especially the rise of
                                        these objects are called salient objects [1]–[3]. Simulating                  affordable and portable consumer depth cameras, has further
                                        this scheme, in the field of computer vision, salient object                  promoted the applications of RGB-D data, such as depth map
                                        detection (SOD) is the task of automatically locating the most                super-resolution [32]–[34], depth estimation [35], superpixel
                                        visually attractive objects or regions in a scene, which has been             segmentation [36], and saliency detection [37]–[43]. For the
                                        successfully applied to numerous tasks, such as segmentation                  RGB-D images, the RGB image contains abundant details
                                                                                                                      and appearance information (e.g., color, texture, structure, etc)
                                           Runmin Cong, Qinwei Lin, Chen Zhang, and Yao Zhao are with the Institute   while the depth map provides some valuable supplementary
                                        of Information Science, Beijing Jiaotong University, Beijing 100044, China,   information (e.g., shape, surface normals, internal consistency,
                                        also with the Beijing Key Laboratory of Advanced Information Science and
                                        Network Technology, Beijing 100044, China (e-mail: rmcong@bjtu.edu.cn,        etc). Recently, more and more studies focus on the introduc-
                                        lqw22@mails.tsinghua.edu.cn, chen.zhang@bjtu.edu.cn, yzhao@bjtu.edu.cn).      tion of depth cue for the SOD task to effectively suppress
                                           Chongyi Li is with the School of Computer Science and En-                  the background interference in complex scenes and further
                                        gineering, Nanyang Technological University, Singapore (e-mail: li-
                                        chongyi25@gmail.com).                                                         completely highlight foreground salient regions. For example,
                                           Xiaochun Cao is with School of Cyber Science and Technology,               in Fig. 1, the first two images have complex and mussy
                                        Shenzhen Campus, Sun Yat-sen University, 518107, China (e-mail:               backgrounds, and the color contrast between the salient object
                                        caoxiaochun@mail.sysu.edu.cn).
                                           Qingming Huang is with the School of Computer Science and Technology,      and the background in the fourth image is low. Thus, for the
                                        University of Chinese Academy of Sciences, Beijing 101408, China, also        RGB SOD method (i.e., the GCPANet [19]) shown in the last
                                        with the Key Laboratory of Intelligent Information Processing, Institute      row of Fig. 1, it is difficult to accurately locate the salient
                                        of Computing Technology, Chinese Academy of Sciences, Beijing 100190,
                                        China, and also with Peng Cheng Laboratory, Shenzhen 518055, China (email:    regions with a clean background and a complete structure.
                                        qmhuang@ucas.ac.cn).                                                          In comparison, the RGB-D SOD methods (e.g., the fourth
                                                                                                                                     2

and fifth rows of Fig. 1) can alleviate this problem with            map space to generate a 3D attention tensor that is used to
the introduction of depth information. Notably, our method           refine the single modality features, which not only reduces the
has better object positioning ability, completeness preserving       computational cost, but also better highlights the important
ability, and background suppression ability.                         features. Further, we design a cross-modality weighting
   The effectiveness of depth map for SOD task has been              refinement (cmWR) unit to refine the multi-modality features
validated in previous work [44]–[47]; however, how to effec-         by considering cross-modality complementary information
tively utilize and integrate the RGB information and depth           and cross-modality global contextual dependencies. Inspired
cue is still an open issue. This is because RGB image                by the non-local model [52], the RGB features, depth features,
and depth map belong to different modalities that have               and RGB-D features are integrated to capture the long-range
different attributes. To achieve this, we design the three-stream    dependencies among different modalities. Then, we use the
structure network to fully capture and utilize cross-modality        integrated features to weight and refine different modality
information. Considering the strengths and complementarities         features, thereby obtaining the refined features embedded
of different modalities, through the three-stream structure with     with cross-modality global context cue, which is important
independent RGB and depth streams, we can sufficiently               for the perception of global information.
preserve the rich information and explore the complementary             In summary, our method is unique in that the cross-modality
relations of different modalities, which is beneficial to jointly    interaction and refinement are closely coupled in a compre-
integrate cross-modality information in the encoder and de-          hensive and in-depth manner. In terms of the cross-modality
coder stage with a more comprehensive and in-depth manner            interaction, for learning the strengths and complementarities of
than the two-stream structure. It is manifested in the following     different modalities, we propose the PAI unit in the encoder
two aspects:                                                         stage and the IGF unit in the decoder stage to jointly explore
   1) Cross-Modality Interaction. In terms of the cross-             the complementary relations of different modalities. In terms
modality information, the primary problem we face is how to          of cross-modality refinement, considering the information
interact them. Specifically, the purpose is to learn the strengths   redundancy of the encoder features and the significance of
and complementarities of different modalities, then obtain           global context cues for the SOD, we design the pluggable
more comprehensive and discriminative feature representa-            refinement middleware structure to refine the encoder features
tions. Different from the existing cross-modality interaction        from the self-modality and cross-modality perspectives. The
methods that operated only in the encoder stage [48], [49] or        main contributions are summarized as follows:
decoder stage [37], [47], [50], we dedicate to integrating cross-       • We propose an end-to-end cross-modality interaction and
modality information into both encoder and decoder stages                  refinement network (CIR-Net) for RGB-D SOD by fully
jointly in a more comprehensive and in-depth manner, which                 capturing and utilizing the cross-modality information in
sufficiently explores the complementary relations of different             an interaction and refinement manner.
modalities. Concretely, in the feature encoder stage, we design         • The progressive attention guided integration unit and the
a progressive attention guided integration (PAI) unit to fuse              importance gated fusion unit are proposed to achieve
cross-modality and cross-level features, thereby attaining the             comprehensive cross-modality interaction in the encoder
RGB-D encoder representations. In the feature decoder stage,               and decoder stages respectively.
we design an aggregation structure to allow RGB and depth               • The refinement middleware structure including the self-
decoder features to flow into the RGB-D mainstream branch                  modality attention refinement unit and cross-modality
and generate more comprehensive saliency-related features.                 weighting refinement unit is designed to refine the multi-
In this structure, the decoder features of the previous layer,             modality encoder features by encoding the self-modality
the RGB and depth decoder features of the corresponding                    3D attention tensor and the cross-modality contextual
layer are integrated into confluence decoder features through              dependencies.
an important gate fusion (IGF) unit in a dynamic weighting              • Without any pre-processing (e.g., HHA [53]) or post-
manner. The gradually refined decoder features of the last layer           processing (e.g., CRF [54]) techniques, our network
are then used to predict the final saliency map.                           achieves competitive performance against the state-of-
   2) Cross-Modality Refinement. In addition to cross-                     the-art methods on six RGB-D SOD datasets.
modality interaction, refining the most valuable information            The rest of this paper is organized as follows. In Section II,
from different modalities is also crucial for RGB-D SOD              we briefly review the related works of RGB-D SOD. In Section
task. To this end, we insert a refinement middleware                 III, we introduce the technical details of the proposed CIR-
between the encoder and the decoder, including the self-             Net. Then, the experiments including the comparisons with
modality refinement and cross-modality refinement. For               state-of-the-art methods and ablation studies are conducted in
the self-modality refinement, in order to reduce the feature         Section IV. Finally, the conclusion is drawn in Section V.
redundancy of the channel dimension and emphasize the
important location of the spatial dimension, we propose
a simple but effective self-modality attention refinement                                 II. R ELATED W ORK
(smAR) unit, which replaces the commonly used progressive              Different from RGB SOD models [55]–[59], depth modality
interaction [51] or feature fusion [47] method with our              together with RGB appearance are introduced into RGB-D
proposed channel-spatial attention generation. We directly           SOD models. In the past ten years, a mass of methods have
integrate spatial attention and channel attention in the feature     been proposed, which can be roughly divided into traditional
                                                                                                                                                                        3

methods [60]–[68] and deep learning-based methods [18],
[37], [39], [44]–[50], [69]–[74]. Especially in recent years,
the deep learning-based methods have achieved great break-                                                                                 D          D           D
                                                                         D
throughs in the performance of RGB-D SOD. For the RGB-                                 D            D      D        D          D
                                                                                                                                           Refinement Middleware
D SOD task, how to make full use of the cross-modality                   E
                                                                                       E            E      E       E           E
information and generate more discriminate saliency-related              C
                                                                                                                                            E        Fusion       E
representation is a challenging issue to be addressed [75].                                                         C
In terms of the model structure, the existing works can be         RGB         Depth   RGB         Depth   RGB   RGB-D         Depth       RGB                  Depth
roughly divided into single-stream, two-stream and three-                (a)                 (b)                   (c)                                (d)
stream structures, as shown in Fig. 2(a)-(c).                       C    Concatenate         Supervision         Interaction           E   Encoder        D   Decoder
   For the single-stream models [72], [76]–[78], the early
feature fusion strategy is commonly adopted, where RGB             Fig. 2. Comparisons among different network structures for RGB-D SOD.
image and depth map are concatenated into four channels            (a)-(c) denote the single-stream, two-stream and three-stream structures,
                                                                   respectively. The (d) is the proposed structure in this paper.
as the input of a network. For examples, Zhao et al. [72]
adopted a single-stream encoder to make full use of the
representation ability of the pre-trained network, and proposed    stream network structure for comprehensive cross-modality
a real-time and robust salient detection model. Zhang et al.       feature interaction, where RGB, depth, and RGB-D are em-
[76], [77] proposed the first uncertainty-inspired RGB-D SOD       bedded in three sub-networks for learning and interaction,
model based on conditional variational auto-encoder. Ji et al.     respectively. For example, Fan et al. [88] designed a gate
[78] proposed a novel collaborative learning framework that        mechanism to filter out the low-quality depth maps using the
integrated the edge, depth, and saliency collaborators, which      decoder results of RGB, depth, and RGB-D branches.
is a more lightweight and versatile network due to the free of        Compared with the existing works, our work differs concep-
depth inputs during testing. However, such models ignore the       tually from theirs in that: Our proposed network architecture
difference between RGB and depth modalities and lack the           (as shown in Fig. 2(d)) is a form between two-stream and
comprehensive cross-modality interaction.                          three-stream networks, and the RGB-D stream is formed
   The two-stream models [39], [46], [47], [50], [51], [79]–       by interacting with the high-level features learned by the
[82] are currently the most widely used structure in RGB-          single-branch network. In this way, the parameters of the
D SOD task, mainly including two independent branches to           network can be reduced, and the RGB-D features can be better
respectively process RGB and depth modality information and        established by our designed PAI unit. On balance, we classify
generate cross-modality features in the encoder or decoder         our network as a three-stream network architecture. This is
stage. For example, Li et al. [46] proposed an attention           also the first point that makes our network different from other
steered interweave fusion network, which progressively and         networks. Second, in addition to the cross-modality feature
interactively captures cross-modality complementarity via the      integration through the PAI unit in the encoder stage, we also
interweave fusion and weighs the saliency regions by the           perform cross-modality information interaction in the decoder
steering of the deeply supervised attention mechanism. Li          stage to obtain the discriminative saliency prediction features.
et al. [47] adopted the late feature fusion strategy to gen-       Considering that the decoder features of RGB and depth
erate cross-modality representation which combines high-           streams can further provide effective guidance information
level RGB and depth features of two independent branches           (e.g., sharp edge, internal consistency) for RGB-D stream,
in the decoder stage. Zhai et al. [51] leveraged the multi-        we design a convergence aggregation structure in the entire
modal and multi-level features to devise a novel cascaded          decoder stage. In this way, we are dedicated to jointly
refinement network, and the RGB and depth modalities can           integrating cross-modality information into the encoder and
be fused in a complementary way. Zhang et al. [83] focused         decoder stages in a more comprehensive manner. Third, to
on the roles of RGB and depth modalities in the cross-             better establish the relationship between encoder features
modality interaction, and presented a discrepant interaction       and decoder features, we introduce a refinement middleware
mode, i.e., the RGB modality and the depth modality guide          structure to further highlight the effective information before
each other interactively. Some studies are taking an interest in   decoding from the perspective of self-modality and cross-
the negative impact of low-quality depth maps by controlling,      modality. It is worth mentioning that such a middleware
updating, or abandoning the depth information in the two-          structure is pluggable for three-stream networks.
stream structure [79], [84]–[87]. Chen et al. [79] introduced
depth quality perception to control the impact of low-quality                                  III. P ROPOSED M ETHOD
depth maps while performing cross-modality interaction in the
two-stream structure. Chen et al. [84] estimated an additional     A. Overview
high-quality depth map as a complement to the original depth          Fig. 3 shows the overview of the proposed CIR-Net that is
map, and all these depth maps are fed into a selective fusion      an encoder-decoder three-stream architecture equipped with a
network to achieve RGB-D SOD. Chen et al. [85] introduced a        refinement middleware between the encoder and the decoder.
depth-quality-aware subnet into the two-stream RGB-D SOD           In what follows, we detail the proposed method.
structure to locate the most valuable depth regions.                  The feature encoder aims to learn the multi-level three-
   In addition, some studies [70], [88], [89] adopted the three-   stream features, i.e., RGB, depth, and RGB-D encoder fea-
                                                                                                                                                                                                    4

                                                                            Skip-connection        Spatial attention             up   Up-sampling operation

                                                                       Refinement Middleware

                                                                                                                   up            up            up            up
                                                                         smAR                             Deconv        Deconv        Deconv        Deconv        Deconv
                              f         _   dnio   2   n   2   p   1

                              dnf
                              1

                              dsd
                          ;         2

                    C
   Progressive
Attention guided                                                         smAR                                  IGF
                                                                                                                         up IGF up         IGF
                                                                                                                                                     up IGF up IGF
Integration (PAI)
                          C
                                                                                    cmWR
       unit
                                                               C

                                                                         smAR                         Deconv            Deconv        Deconv        Deconv        Deconv
                                                                                                                   up            up            up            up

                                                                                Self-modality Attention                          Cross-modality Weighting                        Importance Gated
                                                                         smAR                                      cmWR                                                    IGF
                                                                                   Refinement Unit                                   Refinement Unit                               Fusion Unit

Fig. 3. The overview of the proposed CIR-Net. The extracted RGB and depth features from the backbone are denoted as fri and fdi respectively, where
r and d represent RGB and depth streams, and i ∈ {1, 2, ..., 5} indexes the feature level. In the feature encoder, we also use the PAI unit to generate
                                              i
the cross-modality RGB-D encoder features frgbd    (i ∈ {3, 4, 5}). Then, the top-layer RGB, depth, and RGB-D features are embedded into the refinement
middleware consisting of a smAR unit and a cmWR unit to progressively refine the multi-modality encoder features in a self- and cross-modality manner.
Finally, the decoder features of the RGB branch and depth branch flow into the corresponding RGB-D stream to learn more comprehensive interaction features
through an IGF unit in the feature decoder stage. Note that all three branches output a corresponding saliency prediction map, and we use the output of the
RGB-D branch as the final result.

tures. First, the backbone network (e.g., ResNet50) is used                                                        interaction plays a critical role in the RGB-D SOD task.
to extract the multi-level features from the input RGB image                                                       For an encoder-decoder network architecture, the existing
and depth map, denoted as fri and fdi , respectively, where                                                        interaction strategies are mainly designed separately in
i ∈ {1, 2, 3, 4, 5} indexes the feature level. Then, the RGB                                                       the encoder stage [48], [49] or decoder stage [37], [47],
and depth features at high levels are fed into the proposed pro-                                                   [50]. In comparison, we design specialized modules in
gressive attention-guided integration (PAI) unit to generate the                                                   both encoder and decoder stages according to the different
                                             i
cross-modality RGB-D encoder features frgbd       (i ∈ {3, 4, 5}).                                                 interaction purposes. To achieve that, two key issues need to
At this point, the three-stream encoder structure is formed, as                                                    be addressed: (1) how to effectively integrate and generate
shown on the left side of Fig. 3.                                                                                  the RGB-D representations based on the multi-level RGB
   Considering the information redundancy in the self-modality                                                     and depth features in the encoder stage, and (2) how the
and the content complementarity in the cross-modality, we in-                                                      single-modality stream can better collaborate with the RGB-D
troduce a refinement middleware structure to further highlight                                                     stream to learn more discriminate saliency-related features
the effective information before decoding. Specifically, a two-                                                    and predict more accurate saliency map in the decoder stage.
stage refinement mechanism composing of a self-modality at-                                                        To this end, a PAI unit in the encoder stage and an IGF unit
tention refinement (smAR) unit and a cross-modality weighing                                                       in the decoder stage are proposed in our method. The IGF
refinement (cmWR) unit is designed to progressively refine the                                                     unit will be introduced in Section III-D.
multi-modality top-level encoder features in a self- and cross-
                                                                                                                      Specifically, to effectively integrate the RGB-D represen-
modality manner.
                                                                                                                   tations in the encoder stage, we consider two aspects when
   In the decoder stage, we devise a novel convergence aggre-
                                                                                                                   designing the PAI unit: (1) sufficient multi-level information
gation structure, in which the corresponding decoder features
                                                                                                                   fusion, and (2) effective feature selection and highlighting. For
of the RGB and depth streams flow into the corresponding
                                                                                                                   the former, in the encoder stage, considering the fact that the
RGB-D stream to achieve cross-modality interaction. During
                                                                                                                   features of different levels contain different information with
aggregation, an importance gated fusion (IGF) unit is proposed
                                                                                                                   varying scales, receptive fields, and contents. Thus, the pro-
to integrate the corresponding decoder features of RGB and
                                                                                                                   gressive cross-level fusion strategy is designed to obtain more
depth streams and the previous IGF outputs in a dynamic
                                                                                                                   comprehensive RGB-D representations in a coarse-to-fine
weighting manner. Finally, the output features of the last IGF
                                                                                                                   manner. For the latter, although the encoder features contain
unit are used to infer the final saliency map.
                                                                                                                   rich multi-level information, the commonly used fusion strat-
                                                                                                                   egy (e.g., concat-conv) may introduce information redundancy
B. Progressive Attention Guided Integration Unit                                                                   and easily confuse the feature representations. Therefore, for
 Taking the complementarity and diversity of different                                                             feature selection and enhancement, we introduce the spatial
modalities into account, effective cross-modality information                                                      attention scheme to guide the cross-level and cross-modality
                                                                                                                                                                5

      self-modality attention refinement (smAR) unit                          cross-modality weighting refinement (cmWR) unit

                                                                      H×W×C       HW × C/2
                                              ×      +                                           HW × HW
                                                                                                                         H×W×C
                                                            H×W×C                            ×
                 A

                                                                      H×W×C       C/2 × HW
                                     ×                                                              *                     ×             +
      H×W×C
                 P                                                                                                                             H×W×C
                                                                                             ×
                                                                                                               HW × HW

                                                                      H×W×C       HW × C/2       HW × HW
                                         A   Global Average Pooling                                                           ×   Matrix multiplication

                                         P   Global Max Pooling                                                               +   Element-wise addition

                                                                                                                              *   Element-wise multiplication
                                                                      H×W×C       C/2 × HW

Fig. 4. Illustration of the self-modality attention refinement (smAR) unit and the cross-modality weighting refinement (cmWR) unit in the refinement
middleware structure.

feature fusion by highlighting the complementary information                  weighting manner, thereby generating the RGB-D encoder
and suppressing irrelevant redundancy.                                        features.
   First, motivated by the fact that the shallower depth features
usually contain too much background noise and the high-                       C. Refinement Middleware
level features contain clear information of salient objects but                  To transfer more effective encoder features into the decoder
lack details, we choose to generate the initial cross-modality                stage, we insert a refinement middleware structure as a
features by combining high-level RGB and depth features and                   connecting link between the encoder and decoder to refine
start the combination of features and forward propagation from                the encoder features from the perspectives of self-modality
the third layer, which can be described as:                                   and cross-modality. For the design of refinement middleware,
                                                                              we consider two aspects: 1) the encoder features of each
              f˜rgbd
                i
                     = conv([fri , fdi ]), i ∈ {3, 4, 5},             (1)
                                                                              modality contain abundant spatial and channel information
where fri and fdi respectively denote the RGB and depth                       while indiscriminate information transmission may increase
features at ith encoder level, [·, ·] is the channel-wise concate-            the difficulty of learning effective feature representations.
nation operation, and conv represents a convolutional layer                   Therefore, we design a smAR unit to suppress the background
followed by a batch normalization (BN) layer and a ReLU                       noises and highlight the important cues from a single modality
activation function.                                                          perspective; and 2) considering the strong correlation and
   Then, in order to highlight the complementary information                  complementarity between different modalities where the RGB
and suppress the irrelevant redundancy in the cross-level and                 modality contains figure-ground color contrast and the depth
cross-modality fusion, we employ the spatial attention map                    modality contains internal consistency, we design a cmWR
generated by the previous RGB-D level to guide the current-                   unit to capture the long-range dependencies of multiple modal-
level feature integration in a progressive manner. Thus, the                  ities and refine the modality features from a global perspective.
final RGB-D features at 4th and 5th levels are updated as:                       1) Self-modality Attention Refinement Unit: After the fea-
                                                                              ture encoding, the obtained RGB, depth, and RGB-D encoder
             i
            frgbd = f˜rgbd
                      i
                               Ai−1 + f˜rgbd
                                        i
                                             , i ∈ {4, 5}             (2)     features contain abundant spatial and channel information
                        (                                                     representing the salient objects. However, there will be re-
                             SA(f˜rgbd
                                  i−1
                                       ↓),          i=4                       dundancy in the single-modality information. Moreover, indis-
                Ai−1 =            i−1                                 (3)
                             SA(frgbd ↓),           i=5                       criminate information transmission may increase the difficulty
                                                                              of feature learning, and even contaminate the inference of
where is the element-wise multiplication, Ai−1 denotes the                    subsequent decoding process. Therefore, we design a smAR
attention map of (i − 1)th level, SA is the spatial attention                 unit in the refinement middleware to suppress the background
operation [90], and ↓ denotes the down-sampling operation.                    noises and highlight the important cues from the perspective of
Note that, considering the inaccurate attention that may happen               single modality in a new spatial-channel 3D attention manner.
in some challenging cases, we adopt the residual connection                      The spatial attention (SA) and channel attention (CA) have
in Eq. (2) to learn the optimal relationship between the learned              been widely used in the existing RGB-D SOD tasks [47],
features and the original features for effective feature learning.            [51], [56], which can be summarized into three forms: (a)
In Section IV-C, we provide the ablation study to demonstrate                 Separate utilization. In [56], SA and CA are applied to low-
the effectiveness of this operation. Our PAI unit can not                     level features and high-level features, respectively. (b) Serial
only integrate the different modality information, but also                   utilization. In [51], the CA is first used to generate the CA-
encode the different levels’ features in a progressive attention              enhanced features, and then the SA is subsequently applied
                                                                                                                                   6

to obtain the final enhanced features. (c) Parallel utilization     a unified feature space, which can be formulated as:
via feature fusion. In [47], the CA and SA are respectively
                                                                                          Fθ = Wθ frsmAR ,
used to enhance the same input features, and then the obtained
enhanced features are fused to generate the final features.                               Fξ = Wξ fdsmAR ,
                                                                                                   smAR
                                                                                                                                 (6)
The CA and SA in separate utilization are used for different                              Fϕ = Wϕ frgbd ,
level features, which are not necessarily suitable for all vision                                  smAR
                                                                                          Fψ = Wψ frgbd ,
tasks. However, the serial utilization is sensitive to the order
of SA-CA combination, while the way of feature fusion in            where Wθ , Wξ , Wϕ , and Wψ denote the learnable embedding
parallel utilization has some information redundancy in the         weights through the bottleneck convolutional layers.
structural design, and can only enhance the features in one            Then, similar to the scaled dot-product attention, the cor-
dimension (i.e., spatial or channel) at a time, which increases     relation between the RGB features and depth features, and
computational complexity. To address this issue, we integrate       the self-correlation of the RGB-D features are calculated in a
SA and CA into a spatial-channel 3D attention tensor for: 1)        pixel-wise manner:
enhancing the robustness via parallel utilization and reducing                      M1 = softmax(FθT ⊗ Fξ ),
the computational complexity in a 3D attention manner; and                                                                       (7)
                                                                                    M2 = softmax(FϕT ⊗ Fψ ),
2) refining the single modality features in both spatial and
channel dimension simultaneously.                                   where ⊗ is the matrix multiplication, and softmax is the
   As shown in the left side of Fig. 4, the output features         softmax activation function. M1 ∈ RHW ×HW highlights the
of the three encoder branches (i.e., fr5 , fd5 , and frgbd
                                                        5
                                                            ) are   common response between the RGB and depth modalities,
embedded into the smAR unit. We first calculate the CA and          and M2 ∈ RHW ×HW models the dependencies of RGB-D
SA of the input features in a parallel structure respectively,      modality itself. The fundamental purpose of dividing M1 and
thereby obtaining the corresponding spatial attention map and       M2 separately is that we want the final similarity interaction
channel attention map. Then, we directly fuse them on the           to be performed in the RGB-D feature space.
attention map space via matrix multiplication to generate the          Finally, these two correlation information mapped to the
3D attention tensor. This process can be described as:              RGB-D modality jointly generate cross-modality global de-
                                                                    pendency weights to refine the original input features:
                                                                      cmW R      smAR                                     smAR
                         5
               A3D = SA(fmod         5
                             ) ⊗ CA(fmod ),                  (4)     fmod   = R(fmod  ) ⊗ softmax(M1              M2 ) + fmod  ,
                                                                                                                              (8)
         5
where fmod     denotes the each modality features of the top        where mod ∈ {r, d, rgbd},      is the element-wise multiplica-
encoder layer, mod ∈ {r, d, rgbd}, SA and CA represent the          tion, and R reshapes the feature from RC×H×W to RC×HW .
spatial attention [90] and channel attention [91] operations,       Through the cross-modality global dependency weights gen-
respectively, and ⊗ denotes the matrix multiplication. With the     erated by M1 M2 , we refine the original input modality
3D attention tensor, we refine each modality features through       features from a global perspective, which can improve the
a residual connection:                                              completeness of the detection result, resulting in higher detec-
                                                                    tion accuracy. We conduct various experiments to demonstrate
             smAR                     5      5                      the advantages of the cmWR unit in Table V.
            fmod  = conv(A3D         fmod + fmod ),          (5)
                                                                    D. Importance Gated Fusion Unit
where is the element-wise multiplication. In Section IV-C,
                                                                       As we emphasized before, the cross-modality information
we provide ablation studies with different attention combina-
                                                                    interaction is essential for RGB-D SOD task. Existing methods
tions to demonstrate the effectiveness of our design.
                                                                    usually only interact in a separate encoder or decoder stage,
   2) Cross-modality Weighting Refinement Unit: The smAR            but this is insufficient. In fact, the encoder and decoder play
unit refines the encoder features in each modality, but does not    different roles in feature learning, where the encoder focuses
make full use of the strong correlation and complementarity         more on general feature extraction while the decoder places
between different modalities. For example, the RGB modality         extra emphasis on the learning of saliency-related features.
contains figure-ground color contrast and object texture, and       Thus, in addition to the cross-modality feature integration
the depth modality provides the internal consistency and            through the PAI unit in the encoder stage, we also per-
spatial relations of the salient objects. Therefore, inspired by    form cross-modality information interaction in the decoder
the non-local model [52], [92], we design a novel cmWR unit         stage to obtain the discriminative saliency prediction features.
in the second stage of the refinement middleware to further         Considering that the decoder features of RGB and depth
capture long-range dependencies of multiple modalities.             streams can further provide effective guidance information
   The details of cmWR are shown in the right side of Fig.          (e.g., sharp edge, internal consistency) for RGB-D stream,
                                           smAR
4. The output features of smAR unit fr/d/rgbd      ∈ RC×H×W         we design a convergence aggregation structure in the entire
are embedded into the cmWR unit as the input, where C, H,           decoder stage. In detail, the single modality features (i.e.,
and W denote the channel, height, and width of feature maps,        RGB and depth decoder features) at the same level will flow
respectively. First, we use bottleneck convolutional layers to      to the corresponding RGB-D stream to learn more compre-
half the numbers of channels and map different modalities into      hensive cross-modality decoder features. For the convergence
                                                                                                                                                                                           7

                     Importance Gated Fusion (IGF) unit

                           Previous IGF Features                                    1-P

                                                                                                   ReLU
                                                   Conv

                                                                                                   Conv
                                                                                                    BN
                                                                                          +
                                                                                              P
  Encoder RGB Features

                                                                            Conv
                                                             σ

                                                                    CA
                     ReLU                          P                               C

                                ReLU
                     Conv

                                Conv
                      BN

                                 BN
              C

  Decoder RGB Features

                                                          ReLU
                                                          Conv
                                                           BN
                                             C
 Encoder Depth Features
                                ReLU
                     ReLU
                     Conv

                                Conv
                      BN

                                 BN

              C                                       C     Concatenation          BN     Batch normalization
                                                                                                                       Fig. 6. Learning curve of our network on the training stage.
  Decoder Depth Features                             σ      Sigmoid function       CA     Channel attention

                                                                                                                       saliency maps, which are denoted as S r , S d , and S rgbd . For
Fig. 5. Architecture of the importance gated fusion (IGF) unit.
                                                                                                                       network training, we employ the binary cross-entropy (BCE)
                                                                                                                       loss function to optimize the RGB, depth, and RGB-D streams
aggregation structure, we face a challenging problem, i.e.,                                                            simultaneously. The final loss function is defined as:
how to effectively select the most valuable information from
the afflux streams, because the direct and equal combination                                                              Loss = `bce (S r , G) + `bce (S d , G) + `bce (S rgbd , G),   (11)
of different modality information may be uncontrollable and                                                            where G is the ground truth, and `bce is the BCE loss as
miscellaneous. To solve this issue, we design an IGF unit to                                                           defined in [22], [24]. During the testing phase, we only utilize
learn an importance map P i , which is used to selectively                                                             the prediction of RGB-D stream as the final saliency map.
control the influence of different modalities in a dynamic
weighting manner, as shown in Fig. 5. In this way, the IGF unit                                                                                 IV. E XPERIMENTS
can determine the contribution of supplementary information
                                                                                                                          We first describe the six RGB-D SOD benchmark datasets
of different modalities during cross-modality information in-
                                                                                                                       and three commonly used evaluation metrics, then introduce
teraction. Furthermore, with such learnable important weights,
                                                                                                                       the implementation details of the proposed model. After that,
our network is somewhat resistant to situations where certain
                                                                                                                       the comparisons with 15 state-of-the-art CNN-based methods
modal features are invalid, such as low-quality depth maps.
                                                                                                                       are conducted. Finally, we conduct a series of ablation studies
   First, the RGB decoder features and the depth decoder
                                                                                                                       to validate the effectiveness of our proposed modules.
features are fused with the corresponding skip-connection
encoder features via two convolutional layers, thus attaining
the fused decoder features. Then, the fused decoder features                                                           A. Experimental Settings
of the RGB and depth streams are concatenated to obtain                                                                   1) Benchmark Datasets: We conduct experiments on
the RGB-D decoder features H i . Finally, the previous IGF                                                             six popular RGB-D SOD benchmark datasets, including
            i+1
features fIGF    and the RGB-D decoder features H i are                                                                STEREO797 [60], NLPR [61], NJUD [62], DUT [37],
combined into the current IGF outputs through the learnable                                                            LFSD [93] and SIP [88]. NJUD [62] contains 1985 RGB-D
importance weight:                                                                                                     images and corresponding manually labeled ground truth. The
             i                                                                           i+1                           images are collected from the Internet and stereo movies with
            fIGF = conv(P i                        H i + (1 − P i )                     fIGF ↑),                 (9)
                                                                                                                       diverse objects and complex scenarios, and the depth maps
       i+1
where fIGF     denotes the IGF output features at the (i + 1)th                                                        are estimated from the stereo images. NLPR [61] consists
decoder level, i ∈ {5, 4, ..., 1}, ↑ represents the up-sampling                                                        of 1000 multiple salient objects RGB-D images, where the
operation, and P i is the learnable importance weight, which                                                           depth maps are captured by the Kinect with a resolution
measures the importance of the RGB-D decoder features in the                                                           of 640 × 480. STEREO797 [60] includes 797 stereoscopic
fusion process. Specifically, we first concatenate two features                                                        images collected from the Internet, and the depth maps are
                i+1
(i.e., H i and fIGF ), and then apply 1×1 convolution to reduce                                                        estimated from the stereo images. DUT [37] contains 1200
the numbers of channels, producing the features U i . Next, we                                                         paired RGB-D images captured by a Lytro camera with a
use the channel attention with the sigmoid activation function                                                         resolution of 600 × 400. LFSD [93] is a small-scale dataset
to obtain the importance map P i ∈ RC×H×W :                                                                            including 100 small-resolution RGB-D images, where the
                                           i+1
     P i = σ(CA(U i )) = σ(CA(conv([H i , fIGF ↑]))),                                                           (10)   depth maps are captured via a Lytro light field camera. SIP
                                                                                                                       [88] includes 929 RGB-D images with a high-resolution of
where CA denotes the channel-wise attention [91], and σ is the                                                         744 × 992.
sigmoid activation function. The importance map determines                                                                2) Evaluation Metrics: To quantitatively evaluate the per-
the contribution of supplementary information of different                                                             formance of the proposed method, precision-recall (P-R)
modalities at the ith decoder level.                                                                                   curves, F-measure (Fβ ) [60], Mean Absolute Error (MAE)
                                                                                                                       score [2], and S-measure (Sm ) [97] are employed. By thresh-
E. Loss Function                                                                                                       olding the saliency map from 0 to 255, the precision and recall
   In our CIR-Net, the last layer of decoder features of the                                                           scores can be calculated by comparing the binary mask with
three streams are used to separately predict the corresponding                                                         the corresponding ground truth, and the variation tendency
                                                                                                                                                             8

Common
Scenarios
Depth Maps
Unreliable
Multiple
Objects
Contrast
 Low
Object
Small

              (a)          (b)     (c)       (d)        (e)        (f)          (g)        (h)         (i)         (j)         (k)         (l)        (m)

Fig. 7. Visual examples of different methods. (a) RGB image. (b) Depth map. (c) GT. (d) Ours. (e) A2dele [39]. (f) DANet [72]. (g) S2MA [50]. (h) PGAR
[94]. (i) FRDT [18]. (j) JL-DCF [95]. (k) D3Net [88]. (l) BiANet [96]. (m) DMRA [37]. Our method outperforms other SOTA algorithms in various scenes,
including common scenarios (line 1 and 2), unreliable or confusing depth maps (line 3 and 4), multiple objects (line 5 and 6), low contrast (line 7 and 8),
and small objects (line 9 and 10).

of different precision and recall scores can be drawn in a                         3) Implementation Details: Following [39], [47], we adopt
precision-recall curve.                                                         1485 samples from NJUD dataset, 700 samples from NLPR
   F-measure is a widely used comprehensive evaluation met-                     dataset, and 800 samples from DUT dataset as the training
rics by considering both precision and recall scores, which is                  data. The remaining samples in these three datasets and the
defined as:                                                                     rest three datasets are used as testing datasets. During training,
                                                                                the random flipping, rotating and multi-scale input are adopted
                           (1 + β)2 · P recision × Recall
                    Fβ =                                  ,              (12)   for data augmentation. During the training phase, the training
                              β 2 × P recision + Recall                         samples are randomly resized to 128 × 128, 256 × 256, and
where P recision and Recall respectively represent the preci-                   352 × 352. In the interference stage, the images are resized
sion score and recall score, and β 2 is set to 0.3 for emphasizing              to 352 × 352 and then fed into the network to obtain saliency
the precision as suggested in [60].                                             prediction without any other post-processing or pre-processing
   The MAE score calculates the average pixel-wise absolute                     techniques. We report the experimental results using ResNet50
difference between the predicted saliency map S and the                         and VGG16 as backbone networks, initialized by the pre-
corresponding ground truth G, which is denoted as:                              trained parameters on ImageNet [98].1 The Adam algorithm is
                                                                                used to optimize our network with a batch size of 16, and the
                             H X W
                        1   X                                                   initial learning rate 1e-4 is divided by 5 every 40 epochs. Our
             MAE =                  |S(x, y) − G(x, y)|,                 (13)   network is implemented in PyTorch and accelerated by two
                      H × W y=1 x=1
                                                                                NVIDIA 2080Ti GPUs. We also implement our network by
where H and W represent the height and width of the image,                      using the MindSpore Lite tool2 . In order to show the training
respectively.                                                                   process of our model more clearly, we report the learning curve
   S-measure denotes the structural similarity between the                      of our network in Fig. 6. It takes around 4 hours to optimize
predicted saliency map and the corresponding ground truth:                      our network. The inference time of our method is 0.07 second
                                                                                for an image with the size of 352 × 352.
                      Sm = α × So + (1 − α) × Sr ,                       (14)
                                                                                  1 Unless otherwise stated, the results in this paper are obtained with ResNet
where α is set to 0.5 to balance the region similarity Sr and                   as the backbone network.
object similarity So as suggested in [97].                                        2 https://www.mindspore.cn/
                                                                                                                                                                  9

                          STEREO797                                               NLPR-test                                            NJUD-test

                              DUT-test                                                LFSD                                                SIP

Fig. 8. The P-R curves of different methods. Our model (i.e., the red solid line) achieves both higher precision and recall scores against other compared
methods over all six benchmark datasets.

                                                               TABLE I
  Q UANTITATIVE COMPARISON RESUTLS IN TERMS OF S- MEASURE , MAXIMUM F- MEASURE , AND MAE ON SIX RGB-D BENCHMARK DATASETS . T HE
     BOLD INDICATES THE BEST RESULT UNDER EACH CASE . T HE TYPE INDICATES WHETHER THE METHOD IS SINGLE - STREAM , TWO - STREAM , OR
                        THREE - STREAM . V16, V19 AND R50 DENOTE VGG16, VGG19 AND R ES N ET 50, RESPECTIVELY.

                                           STEREO797 [60]       NLPR-test [61]      NJUD-test [62]      DUT-test [37]         LFSD [93]            SIP [88]
                year   type    backbone
                                          Fβ ↑ Sα ↑ MAE↓ Fβ ↑ Sα ↑ MAE↓ Fβ ↑ Sα ↑ MAE↓ Fβ ↑ Sα ↑ MAE↓ Fβ ↑ Sα ↑ MAE↓ Fβ ↑ Sα ↑ MAE↓
  DMAR [37]     2019   Two       V19      .8861 .8858 .0474   .8749 .8892 .0339   .8883 .8804 .0521   .8975 .8879 .1126   .8523 .8393 .0830   .8209 .8060 .0857
   FRDT [18]    2020   Two       V19      .8987 .9004 .0428   .8976 .9129 .0290   .8982 .8992 .0467   .9263 .9159 .0362   .8555 .8498 .0809   .8714 .8671 .0604
    SSF [49]    2020   Two       V16      .8903 .8920 .0449   .8986 .9141 .0259   .9000 .9002 .0422   .9242 .9157 .0340   .8626 .8495 .0751   .8797 .8737 .0531
  S2MA [50]     2020   Two       V16      .8158 .8424 .0746   .9017 .9155 .0298   .8888 .8943 .0532   .8997 .9031 .0440   .8310 .8292 .1018   .6317 .6919 .1429
  A2dele [39]   2020   Two       V16      .8864 .8868 .0431   .8815 .8979 .0285   .8733 .8704 .0510   .8923 .8864 .0426   .8280 .8258 .0839   .8337 .8287 .0699
  JL-DCF [95] 2020 Single        V16      .8740 .8855 .0509   .8915 .9097 .0295   .9042 .9022 .0413   .8612 .8758 .0556   .8217 .8171 .1031   .7774 .7924 .0967
  PGAR [94]     2020   Two       V16      .9008 .9066 .0422   .9153 .9297 .0245   .9068 .9089 .0422   .9171 .9136 .0372   .8390 .8444 .0818   .8759 .8761 .0552
  DANet [72]    2020 Single      V16      .8199 .8410 .0712   .9013 .9152 .0283   .8927 .8971 .0463   .8954 .8894 .0465   .8417 .8375 .1031   .8740 .8784 .0537
  cmMS [47]     2020   Two       V16      .8971 .8999 .0429   .9031 .9176 .0277   .9034 .9051 .0432   .9090 .9070 .0405   .8623 .8491 .0792   .8814 .8755 .0560
  BiANet [96]   2020   Two       V16      .8844 .8882 .0497   .8764 .9000 .0325   .9121 .9119 .0399   .8156 .8368 .0745   .7287 .7422 .1340   .7869 .8030 .0912
  D3Net [88]    2020 Three       V16      .8495 .8687 .0578   .8969 .9117 .0296   .8996 .9002 .0465   .7855 .8152 .0848   .8062 .8167 .1023   .8611 .8603 .0631
  UCNet [76]    2020   Two       V16      .8355 .8243 .0650   .9034 .9196 .0250   .8860 .8970 .0430   .7785 .8064 .0902   .8595 .8564 .0738   .8792 .8675 .0514
  ASIFNet [46] 2021    Two       V16      .8800 .8820 .0485   .8907 .9079 .0295   .8886 .8902 .0472   .8245 .8396 .0724   .8602 .8520 .0809   .8613 .8594 .0603
  BBSNet [51] 2021     Two       R50      .8778 .8987 .0429   .9153 .9302 .0242   .9194 .9208 .0352   .9237 .9204 .0349   .8689 .8696 .0723   .8945 .8866 .0520
  UCNet* [77] 2021     Two       R50       -     -      -     .9093 .9222 .0234   .8930 .9020 .0390   .8553 .8643 .0561   .8589 .8558 .0713   .8891 .8820 .0452
                                 V16      .9059 .9085 .0413   .9177 .9296 .0227   .9163 .9167 .0382   .9339 .9283 .0320   .8730 .8691 .0682   .8866 .8801 .0553
    CIR-Net      –     Three
                                 R50      .9139 .9166 .0377   .9241 .9334 .0227   .9277 .9250 .0350   .9376 .9324 .0288   .8828 .8753 .0677   .8959 .8884 .0523

B. Comparison with the State-of-the-art Methods                                     method, we provide some visualization comparison results
                                                                                    of different methods in Fig. 7. From it, we can clearly see
   We compared the proposed model with 15 state-of-the-art                          that our proposed model achieves superior performance, which
CNN-based RGB-D SOD methods, including DMRA [37],                                   achieves accurate location and complete structure of the salient
FRDT [18], SSF [49], S2MA [50], A2dele [39], JL-DCF [95],                           objects. For quantitative evaluations, we report the P-R curves
PGAR [94], DANet [72], cmMS [47], BiANet [96], D3Net                                of different methods on six benchmark datasets, which is
[88], UCNet [76], ASIF-Net [46], BBSNet [51], and UCNet*                            shown in Fig. 8. The closer the P-R curve is to (1, 1), the
[77] (the extension version of UCNet). For fair comparisons,                        better the algorithm performance. As visible, our model (i.e.,
all the saliency maps are generated by the released code under                      the red solid line) achieves both higher precision and recall
the default settings or are provided by the authors directly.                       scores against other compared methods over all six benchmark
   To further illustrate the outperformance of our proposed
                                                                                                                                    10

                          TABLE II                                  3.8% for MAE score, F-measure, and S-measure, respectively.
Q UANTITATIVE COMPARISON OF DIFFERENT METHODS IN CHALLENGING        Moreover, as shown in the third and fourth images of Fig.
                           SCENES .
                                                                    7, the depth values of the salient objects are similar to the
                    DANet     SSF BiANet JL-DCF Ours                background, which greatly interferes with the detection of
          Metrics                                                   salient objects. Due to the interference of unreliable depth
                     [72]     [49]  [96]   [95]   -
           MAE↓     .0561    .0581 .0718  .0636 .0449               information, most works (e.g., S2MA [50], A2dele [39],
   No.1    Fβ ↑     .8619    .8608 .8255  .8400 .9022               D3Net [88]) fail to suppress the background noise, leading to
           Sα ↑     .8711    .8660 .8455  .8588 .9039               the inaccurate results. Benefiting for the overall network ar-
           MAE↓     .0914    .0879 .1503  .1603 .0878
                                                                    chitecture and effective cross-modality interactions, our model
   No.2    Fβ ↑     .8495    .8579 .7161  .7150 .8715
                                                                    can obtain robust results in the face of these unreliable factors.
           Sα ↑     .8079    .8139 .7005  .6871 .8270                  (2) Our method has certain advantages when dealing with
           MAE↓     .0742    .0603 .0722  .0603 .0438
                                                                    multi-object scenes. To be specific, we collect all samples with
   No.3    Fβ ↑     .8893    .9162 .8935  .9114 .9438
                                                                    multiple salient objects from the six testing datasets based on
           Sα ↑     .8691    .8895 .8742  .8936 .9225
                                                                    the ground truth, denoted as multi-object subset. As shown in
                                                                    Table II (No.2), the percentage gain in both F-measure and S-
           MAE↓     .0400    .0343 .0393  .0375 .0279
                                                                    measure reaches 1.6% compared with the second best method.
   No.4    Fβ ↑     .7644    .8113 .7742  .7881 .8561
                                                                    In addition, as can be seen from the fifth and sixth images of
           Sα ↑     .8487    .8717 .8520  .8597 .9008
                                                                    Fig. 7, benefiting from the cross-modality feature refinement in
                                                                    a global perspective, our method can not only correctly locate
                                                                    all salient objects, but also obtain a complete and consistent
datasets. Moreover, as shown in Table I, our method achieves        structure, such as the inner area of the person on the right in
the best performance except for the MAE metric on the               the sixth image.
SIP dataset, which also demonstrates the effectiveness and             (3) Our method has certain advantages when dealing with
superiority of the proposed method. For example, compared           low-contrast scenes. Similarly, we select all low-contrast
with the second best method on the large-scale popular              samples with the average color similarity between the salient
NLPR-test, DUT-test, STRERO797 datasets, the minimum                objects and backgrounds exceeding 80% from the six test-
percentage gain reaches 3.0%, 15.3%, 10.7% for MAE scores,          ing datasets (denoted as low-contrast subset) to verify the
respectively. On the small-scale LFSD dataset, compared with        superiority of our method in this case. As shown in Table
the second best model, the percentage gain reaches 1.6% in          II (No.3), compared with the second best method (i.e., SSF),
terms of F-measure and 5.0% in terms of MAE score.                  the percentage gain reaches 25.9%, 3.0%, and 3.7% for MAE
   In order to better illustrate the advantages of our method, we   score, F-measure, and S-measure, respectively. As shown in
analyze and summarize the qualitative and quantitative results      the seventh and eighth images of Fig. 7, most of the existing
from the following aspects:                                         works disturbed by the low color contrast interference, failing
   For some common scenes, such as scenes with obvious              to obtain a complete result. In contrast, our method handles
foreground-background color contrast, large-size object, single     such a challenging scene by better exploiting complementary
object, simple structure, etc., although most of the existing       information across modalities, resulting in more complete and
methods can also achieve good results, our method is more           accurate results, such as hand regions of the person.
stable and robust. As shown in the first two images of Fig. 7,         (4) Our method has certain advantages when dealing with
the salient object is simple in structure and its color contrasts   small-object scenes. Experimentally, we select all samples
sharply with the background. In this case, while most of the        with the salient object occupying less than 10% of the
works can effectively locate the salient object, our work is        image from the six testing datasets (denoted as small-object
able to obtain more accurate results, such as sharp object          subset) to measure the performance of the proposed model in
boundaries (e.g., the pointy tip of the leaf in the first image),   small object scenes. In Table II (No.4), compared with the
clean background suppression (e.g., the leaves in the second        second best method (i.e., SSF),the percentage gain reaches
image).                                                             18.7%, 5.5%, and 3.3% for MAE score, F-measure, and S-
   In addition, to verify the robustness and performance of our     measure, respectively. As can be seen from the ninth and tenth
method on the challenging scenes, we conduct several sensitive      images in Fig 7, our method can effectively locate the small
studies on the testing subsets. The quantitative comparison         salient object, obtaining results with accurate locations, clean
results are shown in Table II.                                      backgrounds, and sharp boundaries.
   (1) Our method has certain advantages when dealing with
unreliable depth maps. As shown in Table II (No.1), we
conduct a sensitive experiment to evaluate the performance          C. Ablation Study
of our method on unreliable depth map samples. Specifically,          1) Analysis of Different Modules: To evaluate the effective-
we select depth maps with the depth confidence λd [64]              ness of each module in the proposed model, we conduct the
score less than 0.1 from the six testing datasets as unreliable     ablation studies on the NJUD-test, STEREO797 and LFSD
depth maps, denoted as unreliable-depth subset. As reported in      datasets. The quantitative evaluations and visual examples are
Table II (No.1), compared with the second best method (i.e.,        shown in Table III and Fig. 9, respectively. We construct our
DANet [72]), the percentage gain reaches 20.0%, 4.7%, and           baseline model by simplifying our full model as follows:
                                                                                                                                          11

       RGB              Depth                GT              Baseline      +PAI             +IGF           +cmWR            +smAR
Fig. 9. Visual examples of different ablation models.

                            TABLE III                                                             TABLE IV
   A BLATION STUDIES ON THE NJUD- TEST, STEREO797 AND LFSD                Q UANTITATIVE COMPARISONS OF THE CONVERGED THREE - STREAM
                            DATASETS .                                      ARCHITECTURE ON THE NJUD- TEST, STEREO797 AND LFSD
                                                                                                  DATASETS .
                    NJUD-test        STEREO797              LFSD
                  Fβ ↑ S α ↑        Fβ ↑ S α ↑          Fβ ↑ Sα ↑                           NJUD-test      STEREO797          LFSD
       Baseline   .8880 .8952       .8769 .8865         .8428 .8502                       Fβ ↑ Sα ↑       Fβ ↑ Sα ↑       Fβ ↑ S α ↑
        +PAI      .8952 .8997       .8853 .8937         .8488 .8532         Full model    .9277 .9250     .9139 .9166     .8828 .8753
        +IGF      .9135 .9144       .9004 .9064         .8705 .8709        Two stream     .9148   .9134   .9027   .9084   .8619   .8568
       +cmWR      .9175 .9168       .9062 .9097         .8799 .8713       RGB branch      .8992   .9002   .9026   .9089   .8324   .8339
       +smAR      .9277 .9250       .9139 .9166         .8828 .8753       Depth branch    .8450   .8600   .7416   .7724   .7681   .7782

   • replacing the PAI unit with the feature concatenation of           structure are improved to a certain extent. Finally, after adding
     the fifth layer in the RGB and depth streams;                      the smAR unit to highlight the important cues from the
   • removing the refinement middleware structure including             single modality perspective, the full model (i.e., ‘+smAR’ in
     its smAR unit and cmWR unit;                                       Fig. 9 and Table III) yields the best performance with the
   • replacing the IGF unit with the simple deconvolutional             percentage gain of 4.5% and 4.2% in terms of F-measure on
     layers.                                                            the NJUD-test dataset and STEREO797 dataset compared with
We use the method of progressively adding designed modules              the baseline model. In summary, the ablation studies further
for ablation experiments. We first introduce the PAI unit into          demonstrate the effectiveness of the proposed modules.
the baseline model (denoted as ‘+PAI’), then we progressively              2) Analysis of the converged three-stream architecture: To
add the IGF unit, cmWR unit, and smAR unit into the model.              demonstrate the effectiveness of the converged three-stream
In other words, ‘+IGF’ denotes the ‘baseline+PAI+IGF’, and              architecture, we conduct several experiments in Table IV and
the like. Moreover, all the ablation models are trained by using        Fig. 10.
the same training configurations as our CIR-Net.                           First, we remove the RGB-D branch in the decoder from
   In Fig. 9, it shows that the baseline model roughly locates          the full model and fuse the output features of RGB and
the salient objects but lacks complete structure and sharp              depth branches via concatenation to obtain the final saliency
boundary, and many background regions are not effectively               map, thereby constructing the two-stream architecture network
suppressed. Compared with the baseline model, the introduc-             (denoted as ‘Two-stream’). From the quantitative results, we
tion of the PAI module obtains more complete and consistent             can see that, with the help of comprehensive feature interaction
structural information (e.g., the flower in the first image), but       in the three-stream structure, the CIR-Net is more effective
still include many wrongly detected background regions. From            than the two-stream architecture. For example, on the LFSD
the quantitative result, the F-measure is improved from 0.8880          dataset, the F-measure of the three-stream network is 0.0209
to 0.8952 on the NJUD-test dataset, and the F-measure is                higher than that of the two-stream network, and the S-measure
increased from 0.8769 to 0.8853 on the STEREO797 dataset.               is 0.0185 higher. Similarly, from the visualization results
Then, after adding the IGF unit for cross-modality feature              shown in Fig. 10, we can see the advantages of the three-
integration in the decoder stage, the clearer boundaries of             stream structure in detection accuracy and completeness. Of
the salient objects (e.g., the flower in the first image) can           course, the performance gain comes at a price. Compared with
be obtained and the quantitative performance is obviously               the two-stream structure, the three-stream design needs more
improved. Specifically, the F-measure score is increased to             computational resources and parameters due to the use of more
0.9135 on the NJUD-test dataset, and the percentage gain                branches. To be specific, due to the additional parameters, the
of the F-measure score reaches 2.0% compared with the                   inference speed for an image of the three-stream architecture
‘+PAI’ model. Furthermore, by introducing the cmWR unit                 is 14 fps, while that of the two-stream architecture is 18 fps.
to refine the different modalities from a global perspective,              In addition, we also quantify the saliency performance of
it is observed that the background suppression and object               the three branches separately. As can be seen from Fig. 10, the
                                                                                                                                                       12

                                                                                                          TABLE VI
                                                                                  A BLATION STUDIES ON PAI AND IGF UNITS ON THE NJUD- TEST,
                                                                                               STEREO797 AND LFSD DATASETS .

                                                                                                        NJUD-test STEREO797       LFSD
                                                                                                       Fβ ↑ Sα ↑ Fβ ↑ Sα ↑ Fβ ↑ Sα ↑
                                                                                        Full model     .9277 .9250 .9139 .9166 .8828 .8753
                                                                                         Fifth Layer   .9098   .9120   .9033   .9063   .8318   .8345
                                                                                        Fourth Layer   .9081   .9130   .8962   .8981   .8657   .8546

                                                                                  PAI
     (a)         (b)      (c)       (d)        (e)          (f)      (g)
                                                                                        Second Layer   .9105   .9134   .9036   .9069   .8620   .8544
Fig. 10. Visual examples of two-stream structure and different branches. (a)
                                                                                         First Layer   .9104   .9123   .9036   .9036   .8555   .8487
RGB image. (b) Depth map. (c) Ground truth. (d) Our result. (e)-(g) Results             Trans Fusion   .9123   .9143   .9034   .9094   .8534   .8480
of Two-stream structure, RGB branch, and Depth branch.
                                                                                           w/ add      .9106 .9131 .9052 .9086 .8609 .8530

                                                                                  IGF
                                                                                           w/ cat      .9132 .9151 .9039 .9082 .8605 .8518
                           TABLE V
A BLATION STUDIES ON MIDDLEWARE ON THE NJUD- TEST, STEREO797
                      AND LFSD DATASETS .
                                                                                                         TABLE VII
                                                                                 A BLATION STUDY OF THE ADDITION OPERATION IN E Q . (2, 5, 8) ON
                            NJUD-test     STEREO797               LFSD                   NJUD- TEST, STEREO797, AND LFSD DATASETS .
                          Fβ ↑ S α ↑       Fβ ↑      Sα ↑    Fβ ↑ Sα ↑
                                                                                                         NJUD-test STEREO797      LFSD
           Full model     .9277 .9250 .9139 .9166 .8828 .8753
                                                                                                       Fβ ↑ S α ↑ Fβ ↑ S α ↑ Fβ ↑ S α ↑
           w/CA, w/o SA   .9152 .9143 .9041 .9090 .8782 .8725                           Full model     .9277 .9250 .9139 .9166 .8828 .8753
  smAR

           w/o CA, w/SA   .9114 .9119 .9031 .9085 .8785 .8689                    w/o add in Eq. (2) .9171 .9159 .9058 .9082 .8500 .8468
              SA-CA       .9167 .9146 .8997 .9030 .8611 .8549                    w/o add in Eq. (5) .9100 .9114 .9023 .9047 .8606 .8490
  cmWR

         w/ M1, w/o M2 .9135 .9114 .9008 .9004 .8623 .8595                       w/o add in Eq. (8) .9096 .9113 .9064 .9071 .8631 .8552
         w/o M1, w/ M2 .9090 .9085 .8959 .9004 .8582 .8462

                                                                                  In terms of the proposed cmWR unit, we replace the final
                                                                               weight map (i.e., M1 × M2 ) with the M1 -only (denoted as ‘w/
RGB branch and the Depth branch have their own advantages                      M1, w/o M2’) and M2 -only (denoted as ‘w/o M1, w/ M2’)
and disadvantages in different regions, but our final RGB-                     cases to demonstrate the advantages of the cmWR unit. From
D branch can concentrate on the advantages of both and                         the quantitative comparison reported in Table V, we can see
suppress the disadvantages, so as to achieve better results                    that the way of M1 × M2 is more effective than the single
with sharper edges and complete structure. For the quantitative                weight map M1 or M2 . For example, on the LFSD dataset,
comparison, it can be found that, with the help of effective                   compared with the case of only M2 , the F-measure score is
cross-modality feature interaction, compared with the RGB                      improved from 0.8582 to 0.8828 with a percentage gain of
branch performance, the final RGB-D saliency performance is                    2.9% and the S-measure score is improved from 0.8462 to
significantly improved. For example, compared with the RGB                     0.8753 with a percentage gain of 3.4%.
branch on the LFSD dataset, the F-measure is improved from                        4) Analysis of different feature interaction strategy in PAI
0.8324 to 0.8828 with a percentage gain of 6.0%, and the S-                    and IGF units: To verify the effectiveness of our design of
measure is improved from 0.8339 to 0.8753 with a percentage                    PAI and IGF units, we conduct various experiments, as shown
gain of 5.0%. These experiments demonstrate the robustness                     in Table VI.
and effectiveness of the proposed model architecture.                             In terms of the PAI unit, we add two ablation experiments.
   3) Analysis of Refinement Middleware: We conduct various                    One is to validate the combination and propagation of dif-
ablation experiments in Table V to validate the effectiveness                  ferent layers, and the other is to replace the spatial attention
of the refinement middleware.                                                  maps with the fused cross-modality RGB-D features in the
   In terms of the proposed smAR unit, we replace the                          corresponding layer (denoted as ‘Trans Fusion’). From Table
3D attention tensor with a single channel attention weight                     VI, we can see that starting combination from the third layer
(denoted as ‘w/ CA, w/o SA’), a single spatial attention weight                (the Full model) achieves the best performance, and the PAI
(denoted as ‘w/o CA, w/ SA’), and a serial utilization of the                  unit is more effective than the commonly used feature fusion
SA-CA combination (denoted as ‘SA-CA’). From Table V,                          strategy. For example, on the LFSD dataset, the F-measure
we can see that the proposed smAR unit is more effective                       score is improved from 0.8555 to 0.8828 with a percentage
than other commonly used attention variants. For example,                      gain of 3.2% compared with the forward propagation from the
compared with the serial utilization of SA-CA combination                      first layer, and the S-measure score is improved from 0.8480
module on the STEREO797 dataset, the F-measure of our full                     to 0.8753 with a percentage gain of 3.2% compared with the
model with smAR unit reaches 0.9139 with a percentage gain                     feature fusion strategy.
of 1.6%, and the percentage gain of S-measure is 1.5%.                            In terms of IGF unit, we replace the dynamic fusion strategy
                                                                                                                                           13

                          TABLE VIII
A BLATION STUDY OF DIFFERENT MODULES IN UNRELIABLE DEPTH MAPS
                 AND MULTIPLE - OBJECT SCENES .

                unreliable-depth subset   multi-object subset
     Metrics   Ours    w/o PAI w/o IGF    Ours    w/o cmWR
     Fβ ↑      .9022    .8886     .8978   .8715     .8626
     Sα ↑      .9039    .8932     .8992   .8270     .8255

                                                                        (a)         (b)          (c)         (d)         (e)         (f)
with the addition (denoted as ‘w/ add’) or concatenation
(denoted as ‘w/ cat’) to suggest the effectiveness of the           Fig. 11. Visual examples of failure cases. (a) RGB image. (b) Depth map.
IGF unit. From Table VI, we can see that with help of               (c) GT. (d) Ours. (e) S2MA [50]. (f) DANet [72].
the proposed IGF unit, the performance is improved when
compared with the commonly used fusions strategy (add or            Similarly, we add an ablation experiment to demonstrate the
concatenation). For example, on the LFSD dataset, compared          effectiveness of the cmWR unit in the multi-object scene. As
with the concatenation operation (i.e., w/ cat), the F-measure      can be reported in the right side of Table VIII, compared with
score is improved from 0.8605 to 0.8828 with a percentage           the model without cmWR unit (denoted as ‘w/o cmWR’),
gain of 2.6% and the S-measure score is improved from 0.8518        the F-measure is improved from 0.8626 to 0.8715 with a
to 0.8753 with a percentage gain of 2.8%.                           percentage gain of 1.0%.
   5) Analysis of residual connection: To demonstrate the
effectiveness of residual features, we conduct the ablation
studies that remove the addition operation in Eqs. (2, 5, 8).       D. Discussion
The quantitative results are shown in Table VII. Compared              1) Failure Cases: Several representative failure cases are
with the only direct multiplication operation, our method with      shown in Fig. 11. We can see that it is difficult to perfectly
residual connection achieves better quantitative performance.       locate salient objects in the following aspects: 1) Multiple and
For example, in Table VII, compared with the result of              small salient objects. In the first scene, although the multiple
removing the addition in Eq. (2), on the LFSD dataset, the F-       salient objects contain the same characteristics in the scene,
measure is improved from 0.8500 to 0.8828 with a percentage         the salient objects far from the lens are too small, so that
gain of 3.9% and the percentage gain of S-measure reaches           the corresponding depth map fails to provide effective depth
3.4%. Similarly, removing the addition operations in Eq. (5,        information of these objects. Hence, it is difficult to completely
8) also degrades the performance.                                   detect all salient objects in such a scene. 2) High contrast but
   6) Analysis of effectiveness to different scenes: When the       not salient objects. In the second scene, it is obvious that the
depth map is unreliable, through the cross-modality interaction     bike seat contrasts sharply with the background in the depth
of PAI unit in the encoder stage, the features of RGB-D branch      map. However, the red logo, the real salient object, is also in
can exploit the correlation between RGB and depth modalities        sharp contrast to the bike seat in the RGB image. Therefore,
to highlight the salient regions. Moreover, in the decoder stage,   the ambiguity introduced by this conflict prevents our model
the IGF unit is able to selectively determine the contribution of   from accurately detecting the red logo as the salient object.
depth modality, thus suppressing the interference of unreliable     3) Complex background noise. In the third scene, due to the
information in depth modality. To validate the effectiveness of     small contrast between the salient object and the background
the PAI and IGF units on unreliable depth maps, we add two          of the RGB image and the misleading depth information in
ablation studies on the unreliable-depth subset that replace the    the depth map, our algorithm fails to suppress the background
PAI unit with the feature concatenation of the fifth layer in the   effectively. It is worthy to note that, for the above challenging
RGB and depth branches (denoted as ‘w/o PAI’), and replace          scenes, the recent state-of-the-art methods (S2MA [50] and
the IGF unit with the direct feature concatenation (denoted as      DANet [72]) also fail to detect the salient objects correctly.
‘w/o IGF’), respectively. As shown in the left side of Table           2) Future Work: In the future, work in three areas can be
VIII, it can be found that after removing the PAI unit and the      further studied. First, our paper mainly focuses on how to
IGF unit, the detection effect of the model on unreliable depth     achieve cross-modality interaction more fully and effectively
maps decreases. For example, with the PAI unit, the F-measure       and does not specifically consider the solution when the
is improved from 0.8886 to 0.9022 with a percentage gain of         quality of the depth map is unreliable, but only uses some
1.5%. Similarly, with the IGF unit, the F-measure is improved       control mechanisms (e.g., cmWR and IGF modules) to reduce
from 0.8978 to 0.9022 with a percentage gain of 0.5%.               the negative impact of low-quality depth maps. Under the
   In addition, concerning the challenging scene containing         existing depth imaging equipment, how to stably and explicitly
multiple salient objects, the cmWR unit can extract the cross-      achieve salient object detection in the case of poor depth
modality global context information by calculating the long-        map quality is a problem worthy of study. Second, as we
range dependency, thus refining features from a global per-         all know, deep learning-based methods are data-driven. Thus,
spective and improving the completeness of saliency results.        more training data would improve the generalization capability
                                                                                                                                            14

                           TABLE IX                                   From the technical design level, as our title says, we
 Q UANTITATIVE EVALUATION OF OUR METHOD WITHOUT NLPR- TRAIN        do two things in this paper: cross-modality interaction and
    DATASET ON NJUD- TEST, STEREO797, AND LFSD DATASETS .
                                                                   cross-modality refinement. For the cross-modality interaction,
                 NJUD-test STEREO797       LFSD
                                                                   different from the existing cross-modality interaction methods
               Fβ ↑ Sα ↑ Fβ ↑ Sα ↑ Fβ ↑ Sα ↑
                                                                   that operated only in the encoder or decoder stage, we dedicate
                                                                   to integrating cross-modality information into both encoder
    Full model .9277 .9250 .9139 .9166 .8828 .8753
                                                                   and decoder stages jointly in a more comprehensive and in-
    w/o NLPR     .9170 .9177 .9096 .9129 .8436 .8488               depth manner. Concretely, in the feature encoder stage, a PAI
                                                                   unit is designed to fuse the cross-modality and cross-level
                                                                   features, thereby attaining the RGB-D encoder representations.
of deep models in most cases. As presented in Table IX,            In the feature decoder stage, we design a convergence structure
when discarding the training data of the NLPR dataset (i.e.,       equipped with the IGF unit to make the RGB and depth
‘w/o NLPR’), the final performance is all degraded, but to         decoder features flow into the RGB-D mainstream branch, and
varying degrees. For example, on the STEREO797 dataset,            effectively select the most valuable supplementary information
the F-measure drops by only 0.5%, but on the LFSD dataset          from RGB and depth modalities to obtain more discriminative
it drops by 4.4%. Put like that, constructing larger datasets or   cross-modality saliency prediction features. For the cross-
reducing the dependence on data volume under the premise           modality refinement, we insert a refinement middleware be-
of ensuring performance can be worked as future research           tween the encoder and decoder to further highlight the effec-
directions. Furthermore, weakly supervised RGB SOD task            tive information before decoding from the perspective of self-
has received a lot of attention, but very little in RGB-D          modality and cross-modality. Specifically, we propose a simple
SOD. Exploring RGB-D SOD models with less supervisory              but effective smAR unit in a 3D-tensor manner to reduce the
information can reduce the dependence on data annotation and       feature redundancy of the channel dimension and emphasize
is a very valuable and promising research direction. Last but      the important location of the spatial dimension, as well as
not least, two- and three-stream based RGB-D SOD models            propose a cmWR unit to refine the multi-modality features
have achieved satisfactory performance, but as a fundamental       by considering cross-modality complementary information and
pre-processing task, how to pursue real-time efficiency while      cross-modality global contextual dependencies. It is worth
maintaining performance is also a valuable research point.         mentioning that such a middleware structure is pluggable for
                                                                   three-stream networks.
                                                                      The mutual cooperation and facilitation of model structure
                      V. C ONCLUSION                               and technical modules enable our method to achieve com-
   In this work, we proposed an end-to-end network, named          petitive performance on six datasets both qualitatively and
CIR-Net, for the task of RGB-D SOD. The strength of our            quantitatively.
algorithm comes from the synergy of the model architecture
and technical modules.                                                                         R EFERENCES
   From the perspective of model architecture, we design a
                                                                   [1] A. Borji, M.-M. Cheng, Q. Hou, H. Jiang, and J. Li, “Salient object
new three-stream-like model architecture to more compre-               detection: A survey,” Computational Visual Media, vol. 5, no. 2, pp.
hensively realize cross-modality information interaction. As           117–150, 2019.
we all know, the two-stream models are currently the most          [2] R. Cong, J. Lei, H. Fu, M. Cheng, W. Lin, and Q. Huang, “Review of
                                                                       visual saliency detectioin with comprehensive information,” IEEE Trans.
widely used structure in RGB-D SOD task, mainly including              Circuits Syst. Video Technol, vol. 29, no. 10, pp. 2941–2959, 2019.
an RGB branch and a depth branch, which can achieve the            [3] W. Wang, Q. Lai, H. Fu, J. Shen, H. Ling, and R. Yang, “Salient object
cross-modality interaction in the feature encoder or decoder           detection in the deep learning era: An in-depth survey,” IEEE Trans.
                                                                       Patt. Anal. Mach. Intell., 2021.
stage. However, the two-stream models can only complete the        [4] W. Wang, J. Shen, R. Yang, and F. Porikli, “Saliency-aware video object
interaction of RGB and depth modalities, while ignoring the            segmentation,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 40, no. 1,
role of RGB-D modality. In contrast, the three-stream structure        pp. 20–33, 2018.
                                                                   [5] G. Li, Z. Liu, R. Shi, Z. Hu, W. Wei, Y. Wu, M. Huang, and H. Ling,
has the opportunity to model the correlation and interaction           “Personal fixations-based object segmentation with object localization
among the RGB, depth, and RGB-D modalities. Moreover, our              and boundary preservation,” IEEE Trans. Image Process., vol. 30, pp.
proposed model architecture is also different from the existing        1461–1475, 2020.
                                                                   [6] P. Wen, R. Yang, Q. Xu, C. Qian, Q. Huang, R. Cong, and
three-stream structures. On the one hand, the generation of            J. Si, “DMVOS: Discriminative matching for real-time video object
our RGB-D stream is not learned from scratch, but obtained             segmentation,” in Proc. ACM MM, 2020, pp. 2048–2056.
through the fusion of the high-level features from the RGB         [7] G. Yue, W. Han, B. Jiang, T. Zhou, R. Cong, and T. Wang, “Boundary
                                                                       constraint network with cross layer feature integration for polyp
branch and depth branch through the PAI module, which can              segmentation,” IEEE J. Biomed. Health Inform., vol. 26, no. 8, pp. 4090–
make the learned RGB-D features more discriminative and                4099, 2022.
reduce the amount of calculation. On the other hand, we adopt      [8] R. Cong, H. Yang, Q. Jiang, W. Gao, H. Li, C. Wang, Y. Zhao, and
                                                                       S. Kwong, “BCS-Net: Boundary, context, and semantic for automatic
a clear convergence structure at the decoder stage to realize          COVID-19 lung infection segmentation from CT images,” IEEE Trans.
the information interaction centered on the RGB-D modality,            Instrum. Meas., vol. 71, pp. 1–11, 2022.
which can further capture the complementarity of the three         [9] R. Cong, Y. Zhang, N. Yang, H. Li, X. Zhang, R. Li, Z. Chen,
                                                                       Y. Zhao, and S. Kwong, “Boundary guided semantic larning for real-time
modalities (i.e., RGB, depth, and RGB-D), thereby obtaining            COVID-19 lung infection segmentation system,” IEEE Trans. Consum.
more discriminative and saliency-related features.                     Electron., early access, doi: 10.1109/TCE.2022.3205376.
                                                                                                                                                               15

[10] Y. Zhang, X. Qian, X. Tan, J. Han, and Y. Tang, “Sketch-based image          [33] Q. Tang, R. Cong, R. Sheng, L. He, D. Zhang, Y. Zhao, and S. Kwong,
     retrieval by salient contour reinforcement,” IEEE Trans. Multimedia,              “Bridgenet: A joint learning network of depth map super-resolution and
     vol. 18, no. 8, pp. 1604–1615, 2016.                                              monocular depth estimation,” in Proc. ACM MM, 2021, pp. 2148–2157.
[11] C. Li, J. Guo, B. Wang, R. Cong, Y. Zhang, and J. Wang, “Single              [34] L. He, H. Zhu, F. Li, H. Bai, R. Cong, C. Zhang, C. Lin, M. Liu, and
     underwater image enhancement based on color cast removal and                      Y. Zhao, “Towards fast and accurate real-world depth super-resolution:
     visibility restoration,” J. Electronic Imaging, vol. 25, no. 3, p. 033012,        Benchmark dataset and baseline,” in Proc. IEEE CVPR, 2021, pp. 9229–
     2016.                                                                             9238.
[12] C. Li, S. Anwar, J. Hou, R. Cong, C. Guo, and W. Ren, “Underwater            [35] L. Wang, J. Zhang, Y. Wang, H. Lu, and X. Ruan, “CLIFFNet for
     image enhancement via medium transmission-guided multi-color space                monocular depth estimation with hierarchical embedding loss,” in Proc.
     embedding,” IEEE Trans. Image Process., vol. 30, pp. 4985–5000, 2021.             ECCV, 2020, pp. 316–331.
[13] J. Hu, Q. Jiang, R. Cong, W. Gao, and F. Shao, “Two-branch deep neural       [36] H. Li, R. Cong, S. Kwong, C. Chen, Q. Xu, and C. Li, “Stereo
     network for underwater image enhancement in HSV color space,” IEEE                superpixel: An iterative framework based on parallax consistency and
     Signal Process. Lett., vol. 28, pp. 2152–2156, 2021.                              collaborative optimization,” Information Sciences, vol. 556, pp. 209–222,
[14] C. Guo, C. Li, J. Guo, C. C. Loy, J. Hou, S. Kwong, and R. Cong, “Zero-           2021.
     reference deep curve estimation for low-light image enhancement,” in         [37] Y. Piao, W. Ji, J. Li, M. Zhang, and H. Lu, “Depth-induced multi-scale
     Proc. CVPR, 2020, pp. 1777–1786.                                                  recurrent attention network for saliency detection,” in Proc. ICCV, 2019,
                                                                                       pp. 7254–7263.
[15] C. Li, C. Guo, J. Guo, P. Han, H. Fu, and R. Cong, “Pdr-net: Perception-
                                                                                  [38] R. Cong, J. Lei, H. Fu, W. Lin, Q. Huang, X. Cao, and C. Hou,
     inspired single image dehazing network with refinement,” IEEE Trans.
                                                                                       “An iterative co-saliency framework for RGBD images,” IEEE Trans.
     Multim., vol. 22, no. 3, pp. 704–716, 2020.
                                                                                       Cybern., vol. 49, no. 1, pp. 233–246, 2019.
[16] Q. Jiang, F. Shao, W. Lin, K. Gu, G. Jiang, and H. Sun,
                                                                                  [39] Y. Piao, Z. Rong, M. Zhang, W. Ren, and H. Lu, “A2dele: Adaptive and
     “Optimizing multistage discriminative dictionaries for blind image
                                                                                       attentive depth distiller for efficient RGB-D salient object detection,” in
     quality assessment,” IEEE Trans. Multimedia, vol. 20, no. 8, pp. 2035–
                                                                                       Proc. CVPR, 2020, pp. 9057–9066.
     2048, 2018.
                                                                                  [40] R. Cong, J. Lei, H. Fu, Q. Huang, X. Cao, and C. Hou, “Co-saliency
[17] N. Yang, Q. Zhong, K. Li, R. Cong, Y. Zhao, and S. Kwong, “A                      detection for RGBD images based on multi-constraint feature matching
     reference-free underwater image quality assessment metric in frequency            and cross label propagation,” IEEE Trans. Image Process., vol. 27, no. 2,
     domain,” Signal Process. Image Commun., vol. 94, p. 116218, 2021.                 pp. 568–579, 2018.
[18] M. Zhang, Y. Zhang, Y. Piao, B. Hu, and H. Lu, “Feature reintegration        [41] R. Cong, J. Lei, H. Fu, Q. Huang, X. Cao, and N. Ling, “HSCS:
     over differential treatment: A top-down and adaptive fusion network for           Hierarchical sparsity based co-saliency detection for RGBD images,”
     RGB-D salient object detection,” in Proc. ACM MM, 2020, pp. 4107–                 IEEE Trans. Multimedia, vol. 21, no. 7, pp. 1660–1671, 2019.
     4115.                                                                        [42] Y. Mao, Q. Jiang, R. Cong, W. Gao, F. Shao, and S. Kwong,
[19] Z. Chen, Q. Xu, R. Cong, and Q. Huang, “Global context-aware                      “Cross-modality fusion and progressive integration network for saliency
     progressive aggregation network for salient object detection,” in Proc.           prediction on stereoscopic 3D images,” IEEE Trans. Multimedia, vol. 24,
     AAAI, 2020, pp. 10 599–10 606.                                                    pp. 2435–2448, 2022.
[20] Y. Zhang, L. Li, R. Cong, X. Guo, H. Xu, and J. Zhang, “Co-saliency          [43] H. Wen, C. Yan, X. Zhou, R. Cong, Y. Sun, B. Zheng, J. Zhang, Y. Bao,
     detection via hierarchical consistency measure,” in Proc. IEEE ICME,              and G. Ding, “Dynamic selective network for RGB-D salient object
     2018, pp. 1–6.                                                                    detection,” IEEE Trans. Image Process., vol. 30, pp. 9179–9192, 2021.
[21] Q. Zhang, R. Cong, J. Hou, C. Li, and Y. Zhao, “CoADNet:                     [44] H. Chen and Y. Li, “Progressively complementarity-aware fusion
     Collaborative aggregation-and-distribution networks for co-salient object         network for RGB-D salient object detection,” in Proc. CVPR, 2018,
     detection,” in Proc. NeurIPS, 2020, pp. 6959–6970.                                pp. 3051–3060.
[22] R. Cong, N. Yang, C. Li, H. Fu, Y. Zhao, Q. Huang, and S. Kwong,             [45] J. Zhao, Y. Cao, D. Fan, M.-M. Cheng, X. Li, and L. Zhang, “Contrast
     “Global-and-local collaborative learning for co-salient object detection,”        prior and fluid pyramid integration for RGBD salient object detection,”
     IEEE Trans. Cybern., early access, doi: 10.1109/TCYB.2022.3169431.                in Proc. CVPR, 2019, pp. 3927–3936.
[23] C. Li, R. Cong, J. Hou, S. Zhang, Y. Qian, and S. Kwong, “Nested             [46] C. Li, R. Cong, S. Kwong, J. Hou, H. Fu, G. Zhu, D. Zhang, and
     network with two-stream pyramid for salient object detection in optical           Q. Huang, “ASIF-Net: Attention steered interweave fusion network for
     remote sensing images,” IEEE Trans. Geosci. Remote Sens., vol. 57,                RGB-D salient object detection,” IEEE Trans. Cybern., vol. 51, no. 1,
     no. 11, pp. 9156–9166, 2019.                                                      pp. 88–100, 2021.
[24] R. Cong, Y. Zhang, L. Fang, J. Li, Y. Zhao, and S. Kwong, “RRNet:            [47] C. Li, R. Cong, Y. Piao, Q. Xu, and C. Loy, “RGB-D salient object
     Relational reasoning network with parallel multi-scale attention for              detection with cross-modality modulation and selection,” in Proc. ECCV,
     salient object detection in optical remote sensing images,” IEEE Trans.           2020, pp. 225–241.
     Geosci. Remote Sens., vol. 60, pp. 1558–0644, 2022.                          [48] G. Li, Z. Liu, L. Ye, Y. Wang, and H. Ling, “Cross-modal weighting
[25] C. Li, R. Cong, C. Guo, H. Li, C. Zhang, F. Zheng, and Y. Zhao, “A                network for RGB-D salient object detection,” in Proc. ECCV, 2020, pp.
     parallel down-up fusion network for salient object detection in optical           1–17.
     remote sensing images,” Neurocomputing, vol. 415, pp. 411–420, 2020.         [49] Y. Piao, R. W, Z. Rong, M. Zhang, and H. Lu, “Select, supplement
                                                                                       and focus for RGB-D saliency detection,” in Proc. CVPR, 2020, pp.
[26] X. Zhou, K. Shen, L. Weng, R. Cong, B. Zheng, J. Zhang, and C. Yan,
                                                                                       3469–3478.
     “Edge-guided recurrent positioning network for salient object detection
                                                                                  [50] N. Liu, N. Zhang, and J. Han, “Learning selective self-mutual attention
     in optical remote sensing images,” IEEE Trans. Cybern., early access,
                                                                                       for RGB-D saliency detection,” in Proc. CVPR, 2020, pp. 13 756–13 765.
     doi: 10.1109/TCYB.2022.3163152.
                                                                                  [51] Y. Zhai, D.-P. Fan, J. Yang, A. Borji, L. Shao, J. Han, and L. Wang,
[27] Q. Zhang et al., “Dense attention fluid network for salient object
                                                                                       “Bifurcated backbone strategy for RGB-D salient object detection,”
     detection in optical remote sensing images,” IEEE Trans. Image
                                                                                       IEEE Trans. Image Process., vol. 30, pp. 8727–8742, 2021.
     Process., vol. 30, pp. 1305–1317, 2021.
                                                                                  [52] X. Wang, R. Girshick, A. Gupta, and K. He, “Non-local neural
[28] R. Cong, J. Lei, H. Fu, F. Porikli, Q. Huang, and C. Hou, “Video                  networks,” in Proc. CVPR, 2018, pp. 7794–7803.
     saliency detection via sparsity-based reconstruction and propagation,”       [53] S. G. R. Girshick, P. Arbeláez, and J. Malik, “Learning rich features
     IEEE Trans. Image Process., vol. 28, no. 10, pp. 4819–4931, 2019.                 from RGB-D images for object detection and segmentation,” in Proc.
[29] G. Li, Y. Xie, T. Wei, K. Wang, and L. Lin, “Flow guided recurrent                ECCV, 2014, pp. 345–360.
     neural encoder for video salient object detection,” in Proc. CVPR, 2018,     [54] P. Krähenbühl and V. Koltun, “Efficient inference in fully connected
     pp. 3243–3252.                                                                    CRFs with gaussian edge potentials,” in Proc. NeurIPS, 2011, pp. 109–
[30] G.-P. Ji, K. Fu, Z. Wu, D.-P. Fan, J. Shen, and L. Shao, “Full-duplex             117.
     strategy for video object segmentation,” in Proc. ICCV, 2021, pp. 4922–      [55] J.-X. Zhao, J.-J. Liu, D.-P. Fan, Y. Cao, J.-F. Yang, and M.-M. Cheng,
     4933.                                                                             “EGNet: Edge guidance network for salient object detection,” in Proc.
[31] D. Jing, S. Zhang, R. Cong, and Y. Lin, “Occlusion-aware bi-directional           ICCV, 2019, pp. 8779–8788.
     guided network for light field salient object detection,” in Proc. ACM       [56] T. Zhao and X. Wu, “Pyramid feature attention network for saliency
     MM, 2021, pp. 1692–1701.                                                          detection,” in Proc. CVPR, 2019, pp. 3085–3094.
[32] C. Guo, C. Li, J. Guo, R. Cong, H. Fu, and P. Han, “Hierarchical features    [57] J.-J. Liu, Q. Hou, M.-M. Cheng, J. Feng, and J. Jiang, “A simple pooling-
     driven residual learning for depth map super-resolution,” IEEE Trans.             based design for real-time salient object detection,” in Proc. CVPR,
     Image Process., vol. 28, no. 5, pp. 2545–2557, 2019.                              2019, pp. 3917–3926.
                                                                                                                                                            16

[58] X. Qin, Z. Zhang, C. Huang, C. Gao, M. Dehghan, and M. Jagersand,           [82] W. Zhou, S. Pan, J. Lei, and L. Yu, “MRINet: Multilevel reverse-
     “BASNet: Boundary-aware salient object detection,” in Proc. CVPR,                context interactive-fusion network for detecting salient objects in RGB-
     2019, pp. 7479–7489.                                                             D images,” IEEE Signal Process. Lett., vol. 28, pp. 1525–1529, 2021.
[59] R. Cong, Q. Qin, C. Zhang, Q. Jiang, S. Wang, Y. Zhao, and S. Kwong,        [83] C. Zhang, R. Cong, Q. Lin, L. Ma, F. Li, Y. Zhao, and S. Kwong,
     “A weakly supervised learning framework for salient object detection via         “Cross-modality discrepant interaction network for RGB-D salient object
     hybrid labels,” IEEE Trans. Circuits Syst. Video Technol., early access,         detection,” in Proc. ACM MM, 2021, pp. 2094–2102.
     doi: 10.1109/TCSVT.2022.3205182.                                            [84] C. Chen, J. Wei, C. Peng, W. Zhang, and H. Qin, “Improved saliency
[60] Y. Niu, Y. Geng, X. Li, and F. Liu, “Leveraging stereopsis for saliency          detection in RGB-D images using two-phase depth estimation and
     analysis,” in Proc. CVPR, 2012, pp. 454–461.                                     selective deep fusion,” IEEE Trans. Image Process., vol. 29, pp. 4296–
[61] H. Peng, B. Li, W. Xiong, W. Hu, and R. Ji, “RGBD salient object                 4307, 2020.
     detection: A benchmark and algorithms,” in Proc. ECCV, 2014, pp. 92–        [85] C. Chen, J. Wei, C. Peng, and H. Qin, “Depth-quality-aware salient
     109.                                                                             object detection,” IEEE Trans. Image Process., vol. 30, pp. 2350–2363,
[62] R. Ju, L. Ge, W. Geng, T. Ren, and G. Wu, “Depth saliency based on               2021.
     anisotropic center-surround difference,” in Proc. ICIP, 2014, pp. 1115–     [86] Z. Bai, Z. Liu, G. Li, L. Ye, and Y. Wang, “Circular complement network
     1119.                                                                            for RGB-D salient object detection,” Neurocomputing, vol. 451, pp. 95–
[63] R. Cong, J. Lei, H. Fu, J. Hou, Q. Huang, and S. Kwong, “Going from              106, 2021.
     RGB to RGBD saliency: A depth-guided transformation model,” IEEE            [87] G. Li, Z. Liu, M. Chen, Z. Bai, W. Lin, and H. Ling, “Hierarchical
     Trans. Cybern., vol. 50, no. 8, pp. 3627–3639, 2020.                             alternate interaction network for RGB-D salient object detection,” IEEE
                                                                                      Trans. Image Process., vol. 30, pp. 3528–3542, 2021.
[64] R. Cong, J. Lei, C. Zhang, Q. Huang, X. Cao, and C. Hou, “Saliency
                                                                                 [88] D. P. Fan, Z. Lin, Z. Zhang, M. Zhu, and M. M. Cheng, “Rethinking
     detection for stereoscopic images based on depth confidence analysis
                                                                                      RGB-D salient object detection: Models, data sets, and large-scale
     and multiple cues fusion,” IEEE Signal Process. Lett., vol. 23, no. 6,
                                                                                      benchmarks,” IEEE Trans. Neural Netw. Learn. Syst., vol. 32, no. 5,
     pp. 819–823, 2016.
                                                                                      pp. 2075–2089, 2021.
[65] D. Feng, N. Barnes, S. You, and C. McCarthy, “Local background              [89] W. Zhou, J. Yuan, J. Lei, and T. Luo, “TSNet: Three-stream self-attention
     enclosure for RGB-D salient object detection,” in Proc. CVPR, 2016,              network for RGB-D indoor semantic segmentation,” IEEE Intell. Syst.,
     pp. 2343–2350.                                                                   vol. 36, no. 4, pp. 73–78, 2020.
[66] R. Ju, Y. Liu, T. Ren, L. Ge, and G. Wu, “Depth-aware salient object        [90] L. Chen, H. Zhang, J. Xiao, L. Nie, J. Shao, W. Liu, and T. Chua, “SCA-
     detection using anisotropic center-surround difference,” Signal Process.:        CNN: Spatial and channel-wise attention in convolutional networks for
     Image Commun., vol. 38, pp. 115–126, 2015.                                       image captioning,” in Proc. CVPR, 2017, pp. 5659–5667.
[67] H. Song, Z. Liu, H. Du, G. Sun, O. Le-Meur, and T. Ren, “Depth-aware        [91] J. Hu, L. Shen, and G. Sun, “Squeeze-and-excitation networks,” in Proc.
     salient object detection and segmentation via multiscale discriminative          CVPR, 2018, pp. 7132–7141.
     saliency fusion and bootstrap learning,” IEEE Trans. Image Process.,        [92] F. Li, R. Cong, H. Bai, and Y. He, “Deep interleaved network for image
     vol. 26, no. 9, pp. 4204–4216, 2017.                                             super-resolution with asymmetric co-attention,” in Proc. IJCAI, 2020,
[68] F. Liang, L. Duan, W. Ma, Y. Qiao, Z. Cai, and L. Qing, “Stereoscopic            pp. 534–543.
     saliency model using contrast and depth-guided-background prior,”           [93] Y. Piao, X. Li, M. Zhang, J. Yu, and H. Lu, “Saliency detection via
     Neurocomputing, vol. 275, pp. 2227–2238, 2018.                                   depth-induced cellular automata on light field,” IEEE Trans. Image
[69] L. Qu, S. He, J. Zhang, J. Tian, Y. Tang, and Q. Yang, “RGBD salient             Process., vol. 29, pp. 1879–1889, 2019.
     object detection via deep fusion,” IEEE Trans. Image Process., vol. 26,     [94] S. Chen and Y. Fu, “Progressively guided alternate refinement network
     no. 5, pp. 2274–2285, 2017.                                                      for RGB-D salient object detection,” in Proc. ECCV, 2020, pp. 520–538.
[70] H. Chen and Y. Li, “Three-stream attention-aware network for RGB-D          [95] K. Fu, D. P. Fan, G. P. Ji, and Q. Zhao, “JL-DCF: Joint learning
     salient object detection,” IEEE Trans. Image Process., vol. 28, no. 6,           and densely-cooperative fusion framework for RGB-D salient object
     pp. 2825–2835, 2019.                                                             detection,” in Proc. CVPR, 2020, pp. 3049–3059.
[71] H. Chen, Y. Li, and D. Su, “Multi-modal fusion network with multiscale      [96] Z. Zhang, Z. Lin, J. Xu, W. D. Jin, S. P. Lu, and D. P. Fan, “Bilateral
     multi-path and cross-modal interactions for RGB-D salient object                 attention network for RGB-D salient object detection,” IEEE Trans.
     detection,” Pattern Recognition, vol. 86, pp. 376–385, 2019.                     Image Process., vol. 30, pp. 1949–1961, 2021.
[72] X. Zhao, L. Zhang, Y. Pang, H. Lu, and L. Zhang, “A single stream           [97] D. Fan, M.-M. Cheng, Y. Liu, T. Li, and A. Borji, “Structure-measure:
     network for robust and real-time RGB-D salient object detection,” in             A new way to evaluate foreground maps,” in Proc. ICCV, 2017, pp.
     Proc. ECCV, 2020, pp. 646–662.                                                   4548–4557.
[73] K. Fu, D.-P. Fan, G.-P. Ji, Q. Zhao, J. Shen, and C. Zhu, “Siamese          [98] J. Deng, W. Dong, R. Socher, L. J. Li, K. Li, and F. F. Li, “ImageNet:
     network for RGB-D salient object detection and beyond,” IEEE Trans.              A large-scale hierarchical image database,” in Proc. CVPR, 2009, pp.
     Pattern Anal. Mach. Intell., 2021.                                               248–255.
[74] W. Zhou, Y. Lv, J. Lei, and L. Yu, “Global and local-contrast guides
     content-aware fusion for RGB-D saliency prediction,” IEEE Trans. Syst.,
     Man, Cybern., Syst., vol. 51, no. 6, pp. 3641–3649, 2019.
[75] T. Zhou, D.-P. Fan, M.-M. Cheng, J. Shen, and L. Shao, “RGB-D salient
     object detection: A survey,” Computational Visual Media, vol. 7, no. 1,
     pp. 37–69, 2021.
[76] J. Zhang, D.-P. Fan, Y. Dai, S. Anwar, F. S. Saleh, T. Zhang, and
     N. Barnes, “UC-Net: Uncertainty inspired RGB-D saliency detection via
     conditional variational autoencoders,” in Proc. CVPR, 2020, pp. 8582–
     8591.
[77] J. Zhang, D.-P. Fan, Y. Dai, S. Anwar, F. Saleh, S. Aliakbarian, and
     N. Barnes, “Uncertainty inspired RGB-D saliency detection,” IEEE
     Trans. Pattern Anal. Mach. Intell., 2021.
[78] W. Ji, J. Li, M. Zhang, Y. Piao, and H. Lu, “Accurate RGB-D salient
     object detection via collaborative learning,” in Proc. ECCV, 2020, pp.
     52–69.
[79] Z. Chen, R. Cong, Q. Xu, and Q. Huang, “DPANet: Depth potentiality-
     aware gated attention network for RGB-D salient object detection,” IEEE
     Trans. Image Process., vol. 30, pp. 7012–7024, 2021.
[80] G. Li, Z. Liu, and H. Ling, “ICNet: Information conversion network for
     RGB-D based salient object detection,” IEEE Trans. Image Process.,
     vol. 29, pp. 4873–4884, 2020.
[81] W. Zhou, Y. Chen, C. Liu, and L. Yu, “GFNet: Gate fusion network with
     res2net for detecting salient objects in RGB-D images,” IEEE Signal
     Process. Lett., vol. 27, pp. 800–804, 2020.
