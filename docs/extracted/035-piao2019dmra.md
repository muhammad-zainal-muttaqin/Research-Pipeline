---
source_id: 035
bibtex_key: piao2019dmra
title: Depth-Induced Multi-Scale Recurrent Attention Network for Saliency Detection
year: 2019
domain_theme: RGB-D SOD
verified_pdf: 35_DMRA.pdf
char_count: 78144
---

Depth-induced Multi-scale Recurrent Attention Network for Saliency Detection

               Yongri Piao                    Wei Ji    Jingjing Li       Miao Zhang∗               Huchuan Lu
                                               Dalian University of Technology, China
  yrpiao@dlut.edu.cn, {jiwei521,lijingjing}@mail.dlut.edu.cn, {miaozhang,lhchuan}@dlut.edu.cn

                            Abstract

    In this work, we propose a novel depth-induced multi-
scale recurrent attention network for saliency detection. It
                                                                          R 3 Net[10]   PAGRN[47] PiCANet[30]     Amulet[44]
achieves dramatic performance especially in complex sce-
narios. There are three main contributions of our network
that are experimentally demonstrated to have significant
practical merits. First, we design an effective depth refine-
ment block using residual connections to fully extract and                 PCA[3]       MMCI[4]      PDNet[48]    CTMF[18]
fuse multi-level paired complementary cues from RGB and
depth streams. Second, depth cues with abundant spatial in-
formation are innovatively combined with multi-scale con-
text features for accurately locating salient objects. Third,                RGB          Depth         GT           Ours
we boost our model’s performance by a novel recurrent at-          Figure 1. Saliency maps of several state-of-the-art CNNs-based
tention module inspired by Internal Generative Mechanism           methods in a complex scene. RGB-D methods are marked in bold.
of human brain. This module can generate more accu-
                                                                   to the powerful ability of CNNs [25] to hierarchically ex-
rate saliency results via comprehensively learning the in-
                                                                   tract informative features. Many works [10,22,30,44,45,47]
ternal semantic relation of the fused feature and progres-
                                                                   focus on identifying saliency regions based on RGB images
sively optimizing local details with memory-oriented scene
                                                                   and have achieved superior performance, yet they still re-
understanding. In addition, we create a large scale RGB-D
                                                                   main challenging in some complex scenarios, such as simi-
dataset containing more complex scenarios, which can con-
                                                                   lar foreground and background, low-intensity environment.
tribute to comprehensively evaluating saliency models. Ex-
                                                                   Depth information containing various depth cues such as
tensive experiments on six public datasets and ours demon-
                                                                   spatial structure and 3D layout has been demonstrated to
strate that our method can accurately identify salient ob-
                                                                   alleviate those issues in SOD [3, 4, 35]. In this paper, we
jects and achieve consistently superior performance over
                                                                   mainly focus on effectively using RGB-D data to enhance
16 state-of-the-art RGB and RGB-D approaches.
                                                                   model’s robustness especially in challenging scenes. As ex-
                                                                   emplified in Fig. 1, RGB-D methods are superior to RGB
                                                                   methods in terms of a complex scene, in which the salient
1. Introduction                                                    object shares similar appearance with its surroundings.
   Salient object detection (SOD) aims to identify regions             Nonetheless, previous works for RGB-D SOD share
in a scene that visually attract human attention most [23,33,      some common limitations: 1) Most CNNs-based meth-
44]. Recently, this fundamental task plays an important role       ods [4,18,35] generally fuse RGB and depth features by di-
in various computer vision applications [15,21,29,37], e.g.,       rect concatenation or summation at a shallow or deep stage.
visual tracking, image segmentation and object recognition.        The complementarity of multi-level RGB and depth infor-
   In the past, most saliency methods [11, 28, 32, 34, 41, 50]     mation is not taken into account. Specifically, the deep fea-
focus on extracting hand-crafted features based on limited         tures can provide discriminative semantic information while
domain-specific knowledge, which may limit their general-          the shallow features also contain affluent local details for ac-
ization ability in different scenarios. Recently, CNNs-based       curately identifying salient objects. A recent work [3] con-
methods have yielded a qualitative leap in performances due        centrates on fusing multi-level information for prediction
                                                                   and achieves better performance. 2) Multiple objects in a
  ∗ Prof.Zhang is the corresponding author.                        scene have large variations in both depth and scale. Explor-

                                                                 7254
ing the relationship between depth cues and objects with              2. Related work
different scales can further provide vital guidance cues for
accurately locating salient regions. However, to our best             RGB-D saliency detection. Although many works [10,
knowledge, this relevance has never been researched in pre-           14, 22, 30, 44, 45, 47] have devoted to RGB saliency detec-
vious SOD works. 3) Studies show that people perceive                 tion and have achieved appealing performance, they might
visual information using an Internal Generative Mechanism             fail when coping with complex scenarios, such as multiple
(IGM) [17, 46]. In the IGM, saliency captured by human is             or transparent objects, similar foreground and background,
not a straight translation of the ocular input, but a result of a     complex background and low-intensity environment. Depth
series of active inferences of brains, especially in complex          cues with affluent spatial structure and 3D layout informa-
scenes. However, the benefits of IGM for comprehensively              tion can contribute to handling those cases [3, 8, 11, 18, 32].
understanding a scene and capturing accurate saliency re-             In our work, we mainly focus on RGB-D saliency detection
gions have never been explored in previous works. Particu-            and intend to improve detector’s performance in complex
larly, the fused feature is directly used for prediction while        scenes.
the internal semantic relation in the fused feature is ignored.           Previous RGB-D saliency detection methods can be gen-
                                                                      erally classified into two categories: (1) manually design-
   In order to address the aforementioned limitations, we             ing hand-crafted features; (2) automatically extracting fea-
propose a depth-induced multi-scale recurrent attention net-          tures with CNNs. For the first category, [32] utilize a multi-
work (DMRANet) for saliency detection as illustrated in               stage model combining RGB-produced saliency with new
Fig. 2. There are three main contributions of our DM-                 depth-induced saliency for SOD. [16, 24] present saliency
RANet. First, we design an effective depth refinement                 methods based on anisotropic center-surround difference or
block (DRB) taking advantages of residual connections to              local background enclosure. [36] exploit the normalized
fully extract and fuse complementary RGB and depth fea-               depth prior and the global-context prior for SOD. Those
tures in multiple levels. Second, we innovatively design a            methods, mainly relying on hand-crafted features and lack-
depth-induced multi-scale weighting (DMSW) module. In                 ing of high-level representations, are unadapted for under-
this module, the relationship between depth information and           standing global context. Recently, CNNs have significantly
objects with different scales is explored for the first time          pushed the performance of vision tasks for its powerful abil-
in saliency detection task (see Fig. 4). Ablation analysis            ity in hierarchically extracting informative features. [35]
shows that utilizing this relevance can improve detection             use hand-crafted features to train a CNN-based model and
accuracy and facilitate the integration of RGB and depth              achieve significant improvements over traditional methods.
data. After the two procedures, a fused feature with abun-            [4, 18] utilize two-stream CNNs-based models but perform
dant saliency cues is generated. Third, we design a novel             fusion by directly concatenating or adding paired features
recurrent attention module (RAM) inspired by the IGM of               at shallow or deep layers. [48] propose a prior-model
human brain. Our RAM can iteratively generate more accu-              guided depth-enhanced network for SOD. Those fusion
rate saliency results in a coarse-to-fine manner by compre-           strategies do not take full advantage of multi-level com-
hensively learning the internal semantic relation of the fused        plementary cues. A recent work [3] designs a fusion net-
feature. Specifically, when inferring the current result, our         work, in which cross-level features are progressively com-
RAM retrieves the previous memory to aid current decision.            bined, and achieves better performance. Besides, we ob-
This can progressively optimize local details with memory-            serve that some schemes [4, 18, 48] adopt extra pre-training
oriented scene understanding for generating the final opti-           or post-processing operations for improving model’s perfor-
mal saliency result. This module boosts our model’s perfor-           mance, which entangles the training process to some extent,
mance by a large margin. In addition, we also create a large          whereas our network is trained in an end-to-end manner.
scale RGB-D dataset with 1200 paired images contain-
ing more complex scenarios, such as multiple or transpar-
                                                                      3. The proposed method
ent objects, similar foreground and background, complex
background, low-intensity environment. This challenging                  We first describe the overall architecture briefly in
dataset can comprehensively evaluate saliency models and              Sec. 3.1. Then, we discuss our multi-level fusion strategy
contribute to further studies in saliency field.                      and its key component-DRB in Sec. 3.2 and give a detailed
   Furthermore, extensive experiments on seven datasets               depiction of our DMSW module in Sec. 3.3. Finally, we
demonstrate that our method achieves consistently superior            elaborate on the RAM which significantly improves the per-
performance over 16 state-of-the-art 2D and 3D approaches.            formance in Sec. 3.4.
The code and results can be found at https://github.
                                                                      3.1. The overall architecture
com/OIPLab-DUT/DMRA_RGBD-SOD. Moreover, to
facilitate research in this field, all those partitioned datasets        Our network architecture, shown in Fig. 2, follows a two-
we collected are shared in a ready-to-use manner.                     stream model. The two streams have the same structure,

                                                                    7255
                  Conv1_2        Conv2_2          Conv3_4         Conv4_4              Conv5_4                    Pooling + Conv
                  <=>×<=> ×>@    128×A<B×A<B       6@×>@×<=>       3<×E<×=A<            1>×A>×=A<

                                                                                                                           Softmax
  RGB / Depth                                                                                                                                     supervision

                  Conv1_2        Conv2_2          Conv3_4         Conv4_4              Conv5_4                                 Vdepth
                  <=>×<=> ×>@    128×A<B×A<B       6@×>@×<=>       3<×E<×=A<            1>×A>×=A<

                                                                                                                    Depth-induced
                                                                                                                      multi-scale
                                                                                                                   weighting module
                                                                                                                                                   Recurrent
                                                                                                                                                attention module
                                                                                                                           DMSW
  Multi-level
                                                                                                                                                        RAM
                                                                                                                       Atrous Conv
feature fusion      DRB            DRB              DRB             DRB                  DRB                                                                  Attention
                   >@×>@×>@       6@×>@×>@         6@×>@×>@        6@×>@×>@             6@×>@×>@

                                                                                                    Ffuse                                       ConvLSTM

                      +              +                +               +                    +
                                         Figure 2. The overall architecture of our DMRANet.

where 5 convolutional blocks of VGG-19 [39] are main-

                                                                                                                                 3x3 Conv
                                                                                                                                  PReLU
tained and the last pooling and fully-connected layers are                     RGB
discarded for making a better fit with our task. The only                 fi
difference between two streams is that the depth stream is
further processed to learn a depth vector. We refine and fuse

                                                                                       3x3 Conv

                                                                                       3x3 Conv

                                                                                                                                                   1x1 Conv
                                                                                                                 Reshape
paired side-out features in multiple layers by employing the

                                                                                        PReLU

                                                                                        PReLU
                                                                               depth
                                                                                                        + fuse                              +
proposed DRB. Then, the depth vector and the fused feature                fi                                fi                                                    fi
are fed into a DMSW module, in which multi-scale features
generated from the fused feature are integrated based on the         Figure 3. Detailed diagram of Depth Refinement Block (DRB).
guidance from the depth vector. Moreover, we boost our
model’s performance by a novel RAM which ably combines                                                             all features fi
                                                                     spatial resolution with 64 channels. Finally, P
                                                                                                                      N
the attention mechanism and ConvLSTM [38]. Finally, the              in multiple layers are summated as Ff use = i=1 fi in an
saliency maps are supervised by the ground truths. Our net-          element-wise manner, where N =5 denotes the total num-
work is trained in an end-to-end manner.                             ber of convolutional blocks. In this way, discriminative
                                                                     multi-level RGB and depth features are effectively learned
3.2. Multi-level Fusion Module                                       and fused. This fusion strategy enables our model to pro-
                                                                     duce more accurate saliency results because of the compre-
    Considering the complementarity between paired depth             hensive combination of both local spatial details and global
and RGB cues in multiple layers, we design a simple yet ef-          semantic information.
fective DRB using residual connections [20] to fully extract
and fuse multi-level paired complementary information.               3.3. Depth-induced Multi-scale Weighting Module
Depth refinement block. As illustrated in Fig. 3, the in-               Considering that an image consists of multiple distinct
puts fiRGB and fidepth represent the side-out features from          objects with different sizes, scales and laid across different
the RGB and depth streams in the i-th level respectively.            spatial locations in numerous layouts, we propose a depth-
We feed fidepth into a series of weight layers Ψ(·) con-             induced multi-scale weighting (DMSW) module. In this
taining two convolutional layers and two PReLU activa-               module, depth cues are further connected with multi-scale
tion functions [19] to learn a depth residual ∆depthi =              features to accurately locate salient objects.
Ψ(fidepth ). Then, the depth residual is added to the RGB               As shown in Fig. 4, depth cues with abundant spatial in-
feature by residual connection to learn a fused feature              formation are further processed to learn a depth vector to
fif use = fiRGB + ∆depthi . In this way, complementary               guide the weight allocation of multi-scale features. To be
clues in the i-th level are fused effectively. Then, we re-          specific, in order to capture multi-scale context features, we
shape (i.e., up-sample with bilinear interpolation or down-          impose a global pooling layer and several parallel convolu-
sample with max-pooling operation) fif use to the same               tional layers with different kernel sizes and different dila-
resolution. A conventional residual unit [20] ℜ(·) is fol-           tion rates on the input feature Ff use . In this way, six multi-
lowed for re-scaling feature values and then a 1×1 con-              scale features Fm ( m = 1, 2, . . . , 6) with the same resolution
volution operation Wi is used to adjust the channel di-              but different contexts are generated. Detailed parameters
mension. The final feature in the i-th level is defined as           are shown in Fig. 4. Compared with classic convolution
fi = Wi ∗ ℜ(reshape(fif use )), which is 1/4 of the input            operation, dilated convolution can increase the size of the

                                                                 7256
                                                                  Depth-induced multi-scale      Recurrent attention             × / × Feature-/Element-wise multiplication
                                                                      weighting module                module                              Σ Element-wise summation
                       Pooling       Conv                                  (DMSW)                        (RAM)                            + Element-wise addition
                                                                                                                                              Softmax function
Fconv5_4
                                                                                                                                          D Dilation parameter

                                                                                                                                           Spatial Attention

                    1x1 Conv
                   3x3 Conv
                                                                                                              Attention
                  Max pooling
                                                                   ×                         Σ                                                                       ×
                3x3 Conv D=3                                                                     F Σ ConvLSTM
Ffuse         3x3 Conv D=5                               Vdepth
             3x3 Conv D=7
                                                                                                                                 Fc                                            F cs        Up x 4
                                          Fm

                                                                                                    h0        ConvLSTM
                                                                                                                            h1   ConvLSTM
                                                                                                                                                       h t-1    ConvLSTM
                    Conv                                                                                                                                                              Fc
                                                                                                              ~                  ~                             ~
        FΣ                              Pooling + Softmax                                                     FΣ,0               FΣ,1            ···           FΣ,t-1
                                +                                      ×          ~
                                                                                  FΣ,t                   h0
                                                                                                                Attention
                                                                                                                            h1
                                                                                                                                  Attention
                                                                                                                                                       h t-1
                                                                                                                                                                   Attention

                    Conv
        ht                                Channel Attention                                                       FΣ                 FΣ          ···                FΣ
                                                                                          (a)                                                                                              (b)
Figure 4. Detailed diagram of DMSW and RAM sub-modules. In RAM, (b) is the details of RAM and (a) is the details of attention block.
receptive field without sacrificing image resolution and re-                             the fused feature FΣ for prediction, as described in ablation
dundant computation [5–7, 43]. Meanwhile, in order to ob-                                analysis. However, we claim that exploring the semantic re-
tain the corresponding depth vector, a global average pool-                              lation inside the fused feature is essential, motivated by the
ing layer and a convolutional layer are imposed on Fconv5 4                              Internal Generative Mechanism (IGM) [17] in human visual
in the depth stream. Then we use a softmax function δ to                                 system. In this section, we boost our model’s performance
obtain the depth vector Vdepth ∈ R1×1×M , which can act                                  by a novel recurrent attention module (RAM). This mod-
as the scale factor for weighting each multi-scale feature                               ule, drawing core ideas from the IGM, can comprehensively
Fm , where M responds to the maximum of m. Finally, all                                  understand a scene and learn the internal semantic relation
multi-scale features Fm are weighted based on depth vec-                                 of the fused feature. To be specific, in order to infer con-
tor Vdepth and then summated to form the final output FΣ .                               spicuous objects, the IGM recurrently deduces and predicts
Formally, the DMSW module can be defined as:                                             saliency based on memory stored in the brain, while uncer-
                                                                                         tain information that is not important will be discarded.
             Vdepth = δ(Wb ∗ AvgP ooling(Fconv5 4 )),                       (1)              Inspired by the IGM, we propose the RAM by ably com-
                                Fm = ξ(Ff use ; θm ),                       (2)          bining attention mechanism and ConvLSTM [38]. In this
                                                                                         way, the RAM can retrieve the previous memory to aid
                                    M
                                    X
                                            m                                            current decision when inferring the current result. It it-
                             FΣ =         Vdepth × Fm ,                     (3)
                                                                                         eratively learns the spatio-temporal dependencies between
                                    m=1
                                                                                         different semantics and progressively optimizes detection
where ∗ and Wb denote convolution operation and corre-                                   details with memory-oriented scene understanding. Con-
sponding parameters. δ(·) represents the softmax function.                               cretely, for the attention block (see Fig. 4(a)), ht stands for
ξ(·) denotes those parallel convolution or pooling opera-                                the previous memory for scene understanding and FΣ is the
tions and θm is the parameters to be learned in the m-th                                 input feature. The subscript t denotes time steps in Con-
            m
branch. Vdepth   represents the weight of the corresponding                              vLSTM. Both ht and FΣ are followed by a convolutional
multi-scale feature Fm and × means the feature-wise mul-                                 layer and then we merge the output features by element-
tiplication.                                                                             wise summation. Then, a global average pooling and a soft-
    In summary, it is beneficial to introduce depth cues to                              max function are used to generate the channel-wise atten-
learn the contribution of multi-scale features for determina-                            tion map Attc (ht , FΣ ) ∈ R1×1×C , in which C denotes the
tion of salient objects especially when objects of different                             number of channels of FΣ . By performing element-wise
sizes appear at different depths. This module can also be                                multiplication on Attc (ht , FΣ ) and FΣ , a more informative
regarded as a deeper fusion of RGB and depth information.
                                                                                         feature FeΣ,t is produced. This procedure can be defined as:
3.4. Recurrent Attention Module
                                                                                          Attc (ht , FΣ ) = δ(AvgP ooling(W0 ∗ht +W1 ∗FΣ )), (4)
   Note that our model has outperformed all other state-of-
the-art methods almost across all datasets by directly using                                                  FeΣ,t = Attc (ht , FΣ ) ⊗ FΣ ,                                                 (5)

                                                                                      7257
where W∗ are convolution parameters. ⊗ means element-               Training and test: Our dataset is randomly divided into
wise multiplication. Next, in Fig. 4(b), FeΣ,t is fed into Con-     two parts: 800 images for training and the rest 400 for test-
vLSTM to further learn the spatial correlation between dif-         ing. For other datasets, we adopt the same splitting way
ferent semantic features. The ConvLSTM is calculated by             as [3, 4, 18] to guarantee a fair comparison. We split 1485
                                                                    samples from NJUD and 700 samples from NLPR for train-
it = σ(Wxi ∗ FeΣ,t + Whi ∗ ht−1 + Wci ◦ct−1 + bi ),                 ing. The remaining images in these two datasets and other
ft = σ(Wxf ∗ FeΣ,t + Whf ∗ ht−1 + Wcf ◦ct−1 + bf ),                 four datasets are all for testing to verify the generalization
                                                                    ability of saliency models. To prevent overfitting, we aug-
ct = ft ◦ct−1 + it ◦ tanh(Wxc ∗ FeΣ,t + Whc ∗ ht−1 + bc ),          ment the training set by flipping, cropping and rotating.
ot = σ(Wxo ∗ FeΣ,t + Who ∗ ht−1 + Wco ◦ct−1 + bo ),
                                                                    4.2. Experimental setup
ht = ot ◦ tanh(ct ),
                                                         (6)        Evaluation metrics. For comprehensively evaluating var-
where ◦ denotes the Hadamard product and σ(·) is sigmoid            ious methods, we adopt five evaluation metrics including
function. it , ft and ot stand for input, forget and output         precision-recall (PR) curve, F-measure (Fβ ) [1], mean ab-
gates, respectively. ct stores the earlier information. All         solute error (MAE) [2] and recently proposed S-measure
W∗ and b∗ are model parameters to be learned. h0 and c0             (Sλ ) [12] and E-measure (Eγ ) [13]. Concretely, saliency
are initialized to 0. After N steps, where we set N = 3 in          maps are binarized using a series of thresholds and then
this work, a channel-refined feature Fc = hN is generated.          pairs of precision and recall are computed to plot the PR
    In addition, we add a common spatial attention block            curve. The F-measure can evaluate the overall performance.
to emphasize the contribution of each pixel for the final           The MAE represents the average absolute difference be-
saliency prediction. We first learn a spatial-wise attention        tween the saliency map and ground truth. The S-measure
map Atts (Fc ) = σ(Ws ∗ Fc ), where ∗ and Ws represent a            can evaluate the spatial structure similarities and the E-
1 × 1 convolution operation and corresponding parameters,           measure can jointly capture image level statistics and local
respectively. Then Atts (Fc ) ∈ RW ×H×1 and Fc are mul-             pixel matching information. For MAE, lower value is better
tiplied in an element-wise manner to get a spatial weighted         and for others, higher is better.
feature Fcs = Atts (Fc ) ⊗ Fc .                                     Implementation details. Our method is implemented with
    Eventually, Fcs is followed by a 1 × 1 convolution layer        pytorch toolbox and trained on a PC with GTX 1080 GPU
and up-sample operation to get the final saliency map Smap .        and 16 GB memory. The input image is uniformly resized
                                                                    to 256×256. The momentum, weight decay and learning
4. Experiments                                                      rate are set as 0.9, 0.0005 and 1e-10, respectively. During
                                                                    training, we use softmax entropy loss and the network con-
4.1. Dataset                                                        verges after 50 epochs with mini-batch size 2.
   We evaluate the effectiveness of our network on our pro-
                                                                    4.3. Comparison with state-of-the-art
posed dataset and other six public datasets.
NJUD [24]: contains 1985 images (the latest version),                   We compare our method with 16 state-of-the-art ones,
which are collected from the Internet, 3D movies and pho-           including 5 latest CNNs-based RGB-D methods: PCA [3],
tographs taken by a Fuji W3 stereo camera. NLPR [32]:               PDNet [48], MMCI [4], CTMF [18], DF [35]; 5 tradi-
includes 1000 images captured by Kinect. LFSD [27]: con-            tional RGB-D methods: MB [49], CDCP [50], NLPR [32],
tains 100 images captured by Lytro camera. STEREO [31]:             DES [8], DCMC [9]; 6 top ranking CNNs-based RGB
contains 797 stereoscopic images downloaded from the In-            methods: PiCANet [30], PAGRN [47], R3 Net [10],
ternet. RGBD135 [8]: contains 135 images captured by                Amulet [44], UCF [45], DSS [22]. For fair comparisons, we
Kinect. SSD [26]: contains 80 images picked up from three           use the released code and their default parameters to repro-
stereo movies.                                                      duce those methods. In terms of methods without released
Ours: Compared to other datasets, ours is more challenging          source code, we use their published results for comparisons.
containing many complex scenes (e.g., multiple or transpar-         Quantitative Evaluation. Tab. 1 and Tab. 2 show the
ent objects, similar foreground and background, complex             validation results in terms of four evaluation metrics on
background and low-intensity environment). The bottom               seven datasets. We can see that our model achieves sig-
five rows marked in Fig. 5 show some representative scenes          nificant outperformance over all other methods. The PR
in our dataset. Our dataset contains 800 indoor and 400 out-        curves in Fig. 6 also consistently demonstrate the superior
door scenes paired with corresponding depth maps [40] and           performance of our method. Especially, ours outperforms
ground truths. This challenging dataset can contribute to           all other methods by a dramatic margin on our proposed
comprehensively evaluating saliency models. More details            dataset, NLPR and STEREO, where the images are com-
about this dataset can de found at the github page.                 parably complicated. It further indicates that our model is

                                                                  7258
Other public datasets
Our proposed dataset

                        RGB   Depth   GT   Ours    PCA       PDNet      MMCI       CTMF       PAGRN     PiCANet      R3Net     Amulet
Figure 5. Comparisons of ours with state-of-the-art CNNs-based methods. Those methods are top ranking ones in quantitative evaluation.
Obviously, our results are more consistent with the ground truths (‘GT’), especially in complex scenes, such as cluttered background (5th
and 6th rows), low-contrast (11th row), transparent object (9th and 12th rows) as well as multiple and small objects (10th row).
more powerful in dealing with the complex scenes.                      relative importance and specific contribution.
Qualitative Evaluation. We also visually compare our                   Performance of DRB. In order to verify the effective-
method with the most representative methods as shown in                ness of the proposed multi-level fusion strategy, we eval-
Fig. 5. From those results, we can observe that our saliency           uate the performance of a common fusion strategy (see
maps are closer to the ground truths. For example, other               Fig. 7 (a)) and our DRB fusion strategy (denoted as ‘Base-
methods are difficult to distinguish salient objects in com-           line’ and ‘+DRB’, respectively). As shown in Tab. 3 and
plex environments (see the 5th and 6th rows), while ours               Fig. 8, ‘+DRB’ consistently outperforms ‘Baseline’ across
can precisely identify the whole object. And our DMRANet               all datasets. The predictions produced by our DRB con-
can more accurately locate and detect the entire conspicu-             tain more local details than ‘Baseline’ in Fig. 9. This ad-
ous objects with sharp details than others in more challeng-           vance further confirms the superiority of our DRB in ef-
ing scenes such as low-contrast, transparent object as well            fectively and abundantly extracting and fusing multi-level
as multiple and small objects (see the 9th -12th rows). Those          paired complementary information.
results further verify the effectiveness and robustness of our         Performance of DMSW module. One of our core claims
proposed DMRANet.                                                      is that incorporating depth cues with multi-scale features
                                                                       can help locate saliency regions. To give evidence for this
4.4. Ablation analysis
                                                                       claim, we add the DMSW module (‘+DMSW’) to previ-
  In this section, we perform ablation analysis over each              ous ‘+DRB’ model. Results in Tab. 3 and Fig. 8 show that
component of the DMRANet and further investigate their                 our DMSW module achieves impressive accuracy gains on

                                                                     7259
                          Ours                              NJUD                                  NLPR                  STEREO
      *        Eγ      Sλ      Fβ      MAE       Eγ      Sλ     Fβ        MAE          Eγ      Sλ     Fβ      MAE      Eγ    Sλ
    Ours      0.927   0.888 0.883      0.048    0.908   0.886 0.872       0.051       0.942   0.899 0.855     0.031   0.920 0.886
    PCA       0.858   0.801 0.760      0.100    0.896   0.877 0.844       0.059       0.916   0.873 0.794     0.044   0.905 0.880
   PDNet      0.861   0.799 0.757      0.112    0.890   0.883 0.832       0.062       0.876   0.835 0.740     0.064   0.903 0.874
   MMCI       0.855   0.791 0.753      0.113    0.878   0.859 0.813       0.079       0.871   0.855 0.729     0.059   0.890 0.856
   CTMF       0.884   0.834 0.792      0.097    0.864   0.849 0.788       0.085       0.869   0.860 0.723     0.056   0.870 0.853
     DF       0.842   0.730 0.748      0.145    0.818   0.735 0.744       0.151       0.838   0.769 0.682     0.099   0.844 0.763
  PiCANet     0.895   0.832 0.826      0.080    0.880   0.847 0.806       0.071       0.895   0.834 0.761     0.053   0.904 0.868
  PAGRN       0.883   0.831 0.836      0.079    0.882   0.829 0.827       0.081       0.907   0.844 0.795     0.051   0.900 0.851
   R3 Net     0.833   0.819 0.781      0.113    0.838   0.837 0.775       0.092       0.788   0.798 0.649     0.101   0.856 0.855
   Amulet     0.880   0.846 0.803      0.083    0.859   0.843 0.798       0.085       0.852   0.848 0.722     0.062   0.897 0.881
    UCF       0.848   0.833 0.766      0.108    0.830   0.829 0.758       0.109       0.835   0.837 0.701     0.082   0.874 0.867
    DSS       0.831   0.767 0.732      0.127    0.853   0.807 0.776       0.108       0.879   0.816 0.755     0.076   0.885 0.841
    MB        0.691   0.607 0.577      0.156    0.643   0.534 0.492       0.202       0.814   0.714 0.637     0.089   0.693 0.579
   CDCP       0.794   0.687 0.633      0.159    0.751   0.673 0.618       0.181       0.785   0.724 0.591     0.114   0.801 0.727
   NLPR       0.767   0.568 0.659      0.174    0.722   0.530 0.625       0.201       0.772   0.591 0.520     0.119   0.781 0.567
    DES       0.733   0.659 0.668      0.280    0.421   0.413 0.165       0.448       0.735   0.582 0.583     0.301   0.451 0.473
   DCMC       0.712   0.499 0.406      0.243    0.796   0.703 0.715       0.167       0.684   0.550 0.328     0.196   0.838 0.745
Table 1. Quantitative comparison of E-measure, S-measure, F-measure and MAE on our proposed dataset and six widely-used RGB-D
datasets. The best three results are shown in boldface, red, and green fonts respectively. Our method ranks first on all datasets and
evaluation metrics. From top to bottom: CNNs-based RGB-D methods, the latest RGB methods and traditional RGB-D methods.

                STEREO                     LFSD                             RGBD135                               SSD
      *        Fβ   MAE         Eγ      Sλ     Fβ       MAE       Eγ       Sλ    Fβ           MAE      Eγ      Sλ     Fβ    MAE
    Ours      0.868 0.047      0.899   0.847 0.849      0.075    0.945    0.901 0.857         0.029   0.892   0.857 0.821   0.058
    PCA       0.845 0.061      0.846   0.800 0.794      0.112    0.909    0.845 0.763         0.049   0.883   0.843 0.786   0.064
   PDNet      0.833 0.064      0.872   0.845 0.824      0.109    0.915    0.868 0.800         0.050   0.813   0.802 0.716   0.115
   MMCI       0.812 0.080      0.840   0.787 0.779      0.132    0.899    0.847 0.750         0.064   0.860   0.814 0.748   0.082
   CTMF       0.786 0.087      0.851   0.796 0.781      0.120    0.907    0.863 0.765         0.055   0.837   0.776 0.709   0.100
     DF       0.761 0.142      0.801   0.685 0.566      0.130    0.801    0.685 0.566         0.130   0.802   0.742 0.709   0.151
  PiCANet     0.835 0.062      0.806   0.761 0.730      0.134    0.928    0.854 0.797         0.042   0.882   0.832 0.775   0.068
  PAGRN       0.856 0.067      0.831   0.779 0.786      0.117    0.919    0.858 0.834         0.044   0.862   0.793 0.762   0.088
   R3 Net     0.800 0.084      0.771   0.797 0.791      0.141    0.868    0.847 0.728         0.066   0.833   0.815 0.747   0.095
   Amulet     0.842 0.062      0.863   0.827 0.817      0.101    0.866    0.842 0.725         0.070   0.843   0.828 0.756   0.087
    UCF       0.808 0.083      0.816   0.811 0.773      0.138    0.854    0.835 0.717         0.089   0.807   0.795 0.693   0.117
    DSS       0.814 0.087      0.778   0.718 0.694      0.166    0.855    0.763 0.697         0.098   0.834   0.786 0.752   0.116
    MB        0.572 0.178      0.631   0.538 0.543      0.218    0.798    0.661 0.588         0.102   0.633   0.499 0.414   0.219
   CDCP       0.680 0.149      0.737   0.658 0.634      0.199    0.806    0.706 0.583         0.119   0.714   0.604 0.524   0.219
   NLPR       0.716 0.179      0.742   0.558 0.708      0.211    0.850    0.577 0.857         0.097   0.726   0.562 0.551   0.200
    DES       0.223 0.417      0.475   0.440 0.228      0.415    0.786    0.627 0.689         0.289   0.383   0.341 0.073   0.500
   DCMC       0.761 0.150      0.842   0.754 0.815      0.155    0.674    0.470 0.228         0.194   0.790   0.706 0.684   0.168
                                                  Table 2. Continuation of Table 1.
all datasets by comparing ‘+DMSW’ and ‘+DRB’. From                   improve the detection accuracy. In addition, it is important
Fig. 9, we can see ‘+DMSW’ can identify more saliency                to note that our model has outperformed all other methods
regions compared with ‘+DRB’. Those results demonstrate              almost across all datasets at this stage. This fact further ver-
the advantage of our DMSW module in sufficiently utiliz-             ifies the strength of our proposed module.
ing depth cues and multi-scale information. Moreover, we             Performance of RAM. In this section, we evaluate the
also verify the benefits of utilizing the relationship between       performance of our RAM. By comparing visual results in
depth cues and multi-scale features by performing a new              Fig. 9, we observe our RAM can further suppress back-
model, in which features at multiple scales are integrated           ground irritations and substantially optimize detection de-
by a 1×1 convolution operation instead of depth cues (de-            tails. In addition, we replace the RAM with a basic channel-
noted as ‘+DMSW (w/o d)’). Results in Tab. 3 and Fig. 8              spatial attention block [42] (denoted as ‘+Att(common)’) in
show that removing depth guidance degrades performance               Fig. 7 (b). Results in Tab. 3 suggest that our RAM is su-
to some extent. Those results also demonstrate that the com-         perior to ‘+Att(common)’ and boosts model’s performance
bination of depth information and multi-scale features can           by a large margin. We attribute this advance to its power-

                                                                  7260
              1                                                                                           1                                                                                        1                                                                  1

             0.9                                                                                         0.9                                                                                      0.9                                                                0.9

                                                                                                                                                                                                  0.8
             0.8                                                                                         0.8                                                                                                                                                         0.8

                                                                                                                                                                                                  0.7
             0.7        Amulet                                                                           0.7       Amulet                                                                                   Amulet                                                   0.7       Amulet

                                                                                            Precisio n

                                                                                                                                                                                     Precisio n

                                                                                                                                                                                                                                                        Precisio n
Precisio n
Precision

                                                                                            Precision

                                                                                                                                                                                                                                                        Precision
                                                                                                                                                                                     Precision
                        CTMF                                                                                       CTMF                                                                           0.6       CTMF                                                               CTMF
             0.6        DF                                                                               0.6       DF                                                                                       DF                                                       0.6       DF
                        DSS                                                                                        DSS                                                                                      DSS                                                                DSS
                                                                                                                                                                                                  0.5
                        MMCI                                                                                       MMCI                                                                                     MMCI                                                               MMCI
             0.5        Ours                                                                             0.5       Ours                                                                                     Ours                                                     0.5       Ours
                                                                                                                                                                                                  0.4
                        PAGRN                                                                                      PAGRN                                                                                    PAGRN                                                              PAGRN
             0.4        PCA                                                                              0.4       PCA                                                                                      PCA                                                      0.4       PCA
                        PDNet                                                                                      PDNet                                                                          0.3       PDNet                                                              PDNet
                        PiCANet                                                                                    PiCANet                                                                                  PiCANet                                                            PiCANet
             0.3                                                                                         0.3                                                                                      0.2                                                                0.3
                        R³Net                                                                                      R³Net                                                                                    R³Net                                                              R³Net
                        UCF                         Ours                                                           UCF                       NJUD                                                           UCF            NLPR                                                UCF        STEREO
             0.2                                                                                         0.2                                                                                      0.1                                                                0.2
                   0         0.2              0.4            0.6          0.8           1                      0        0.2                0.4            0.6          0.8       1                      0        0.2     0.4            0.6   0.8   1                      0        0.2   0.4            0.6   0.8   1
                                                    Recall                                                                                       Recall                                                                        Recall                                                           Recall

                                               Figure 6. The PR curves of the proposed method and other state-of-the-art approaches across four datasets.
                                                                   Ours                                            NJUD                                       NLPR                                   STEREO                            LFSD                            RGBD135                        SSD
                    *                                           Fβ    MAE                                       Fβ    MAE                                  Fβ    MAE                                Fβ   MAE                        Fβ    MAE                         Fβ   MAE                     Fβ    MAE
                Baseline                                       0.828 0.070                                     0.820 0.068                                0.758 0.051                              0.822 0.067                     0.822 0.094                       0.780 0.047                  0.758 0.081
                 +DRB                                          0.839 0.065                                     0.828 0.064                                0.774 0.046                              0.828 0.064                     0.825 0.090                       0.792 0.043                  0.768 0.076
             +DMSW(w/o d)                                      0.855 0.061                                     0.844 0.062                                0.805 0.044                              0.837 0.061                     0.836 0.087                       0.823 0.042                  0.774 0.076
                +DMSW                                          0.861 0.057                                     0.850 0.059                                0.801 0.042                              0.852 0.057                     0.836 0.086                       0.828 0.040                  0.783 0.075
              +Att(common)                                     0.869 0.054                                     0.860 0.055                                0.827 0.036                              0.859 0.053                     0.847 0.081                       0.842 0.032                  0.809 0.064
              +RAM(Ours)                                       0.883 0.048                                     0.872 0.051                                0.855 0.031                              0.868 0.047                     0.849 0.075                       0.857 0.029                  0.821 0.058
                   Table 3. Ablation analysis on seven datasets. Obviously, each component of our DMRANet can provide additional accuracy gains.

                                             Conv                  Conv           ···   Conv                                                                                                                  RGB
                         RGB                      1x1                 1x1                     1x1
(a)                                             C Conv              C Conv        ···       C Conv                                Deconv

                                             Conv                  Conv           ···   Conv                                                               Prediction
                                                                                                                                                                                                             Depth
                         Depth                             +                 +                                     +

                                                                        Channel                                                                                                                                GT
                                              Conv                      Attention                           Conv               Spatial
(b)                                          Pooling                       map          ×                  Sigmoid
                                                                                                                              Attention               ×
                                                                                                                                map

                       Feature map                                                                                                                         Refined feature

                                                                                                                                                                                                            Baseline
Figure 7. Diagrams of ablation analysis. (a) Baseline. ‘C’ means
concatenation operation. (b) Att(common).
                                       (a) MAE                                                                                  (b) F-measure
                                  Baseline          +DRB           +DMSW(w/o d)                                                 Baseline           +DRB           +DMSW(w/o d)
                                                                                                                                                                                                            +DRB
                                  +DMSW             +Att(common)   +RAM/Ours                                                    +DMSW              +Att(common)   +RAM/Ours

                                                                                                                                                                                                            +DMSW

                                                                                                                                                                                                        +RAM / Ours
             Ours            NJUD                   NLPR           STEREO                                      Ours           NJUD                NLPR            STEREO

Figure 8. Histograms of F-measure and MAE on four datasets.                                                                                                                                                            Figure 9. The visual results of ablation analysis.
ful ability in progressively optimizing detection details with                                                                                                                                      ages containing more challenging scenes. We comprehen-
memory-oriented scene understanding.                                                                                                                                                                sively validate the effectiveness of each component of our
                                                                                                                                                                                                    network and show the accumulated accuracy gains gradu-
5. Conclusion                                                                                                                                                                                       ally. Experiment results also demonstrate that our method
                                                                                                                                                                                                    achieves new state-of-the-art performance on seven RGB-D
   In this work, our proposed ‘DMRANet’ enhances the
                                                                                                                                                                                                    datasets.
performance of saliency detection from three aspects: 1)
fully extracts and fuses multi-level paired complementary
                                                                                                                                                                                                    Acknowledgment
features by using a simple yet effective DRB; 2) innova-
tively combines depth cues with multi-scale information to                                                                                                                                              This work was supported by the National Natural Sci-
accurately locate and identify salient objects; 3) progres-                                                                                                                                         ence Foundation of China(61605022 and U1708263) and
sively generates more accurate saliency results through a                                                                                                                                           the Fundamental Research Funds for the Central Universi-
novel recurrent attention model. In addition, we build a                                                                                                                                            ties(DUT19JC58). The authors are grateful to the reviewers
large scale RGB-D saliency dataset with 1200 paired im-                                                                                                                                             for their suggestions in improving the quality of the paper.

                                                                                                                                                                                     7261
References                                                                     Conference on Artificial Intelligence (IJCAI), pages 698–
                                                                               704, 2018.
 [1] Radhakrishna Achanta, Sheila S. Hemami, Francisco J.                 [14] Deng-Ping Fan, Jiang-Jiang Liu, Shang-Hua Gao, Qibin
     Estrada, and Sabine Süsstrunk. Frequency-tuned salient re-               Hou, Ali Borji, and Ming-Ming Cheng. Salient objects in
     gion detection. In Conference on Computer Vision and Pat-                 clutter: Bringing salient object detection to the foreground.
     tern Recognition (CVPR), pages 1597–1604, 2009.                           In European Conference on Computer Vision (ECCV), pages
 [2] Ali Borji, Dicky N. Sihite, and Laurent Itti. Salient object de-          1597–1604. Springer, 2018.
     tection: a benchmark. In European Conference on Computer             [15] Deng-Ping Fan, Wenguan Wang, Ming-Ming Cheng, and
     Vision (ECCV), pages 414–429, 2012.                                       Jianbing Shen. Shifting more attention to video salient object
 [3] Hao Chen and Youfu Li. Progressively complementarity-                     detection. In Conference on Computer Vision and Pattern
     aware fusion network for rgb-d salient object detection. In               Recognition (CVPR), pages 8554–8564, 2019.
     Conference on Computer Vision and Pattern Recognition                [16] David Feng, Nick Barnes, Shaodi You, and Chris McCarthy.
     (CVPR), pages 3051–3060, 2018.                                            Local background enclosure for rgb-d salient object detec-
 [4] Hao Chen, Youfu Li, and Dan Su. Multi-modal fusion net-                   tion. In Conference on Computer Vision and Pattern Recog-
     work with multi-scale multi-path and cross-modal interac-                 nition (CVPR), pages 2343–2350, 2016.
     tions for rgb-d salient object detection. Pattern Recognition,       [17] Dashan Gao, Sunhyoung Han, and Nuno Vasconcelos. Dis-
     86:376–385, 2019.                                                         criminant saliency, the detection of suspicious coincidences,
 [5] Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos,                    and applications to visual recognition. IEEE Transactions on
     Kevin Murphy, and Alan L. Yuille. Deeplab: Semantic im-                   Pattern Analysis and Machine Intelligence, 31(6):989–1005,
     age segmentation with deep convolutional nets, atrous con-                2009.
     volution, and fully connected crfs. IEEE Transactions on             [18] Junwei Han, Hao Chen, Nian Liu, Chenggang Yan, and Xue-
     Pattern Analysis and Machine Intelligence, 40(4):834–848,                 long Li. Cnns-based rgb-d saliency detection via cross-view
     2018.                                                                     transfer and multiview fusion. IEEE Transactions on Sys-
 [6] Liang-Chieh Chen, George Papandreou, Florian Schroff, and                 tems, Man, and Cybernetics, 48(11):3171–3183, 2018.
     Hartwig Adam. Rethinking atrous convolution for seman-               [19] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     tic image segmentation. arXiv preprint arXiv:1706.05587,                  Delving deep into rectifiers: Surpassing human-level perfor-
     2017.                                                                     mance on imagenet classification. In International Confer-
 [7] Liang-Chieh Chen, Yukun Zhu, George Papandreou, Florian                   ence on Computer Vision (ICCV), pages 1026–1034, 2015.
     Schroff, and Hartwig Adam. Encoder-decoder with atrous               [20] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
     separable convolution for semantic image segmentation. Eu-                Deep residual learning for image recognition. In Conference
     ropean Conference on Computer Vision (ECCV), pages 833–                   on Computer Vision and Pattern Recognition (CVPR), pages
     851, 2018.                                                                770–778, 2016.
                                                                          [21] Seunghoon Hong, Tackgeun You, Suha Kwak, and Bohyung
 [8] Yupeng Cheng, Huazhu Fu, Xingxing Wei, Jiangjian Xiao,
                                                                               Han. Online tracking by learning discriminative saliency
     and Xiaochun Cao. Depth enhanced saliency detection
                                                                               map with convolutional neural network. International Con-
     method. In International Conference on Internet Multime-
                                                                               ference on Machine Learning (ICML), pages 597–606, 2015.
     dia Computing and Service (ICIMCS), pages 23–27, 2014.
                                                                          [22] Qibin Hou, Ming-Ming Cheng, Xiaowei Hu, Ali Borji,
 [9] Runmin Cong, Jianjun Lei, Changqing Zhang, Qingming
                                                                               Zhuowen Tu, and Philip H.S. Torr. Deeply supervised salient
     Huang, Xiaochun Cao, and Chunping Hou. Saliency de-
                                                                               object detection with short connections. In Conference on
     tection for stereoscopic images based on depth confidence
                                                                               Computer Vision and Pattern Recognition (CVPR), pages
     analysis and multiple cues fusion. IEEE Signal Processing
                                                                               5300–5309, 2017.
     Letters, 23(6):819–823, 2016.
                                                                          [23] Laurent Itti, Christof Koch, and Ernst Niebur. A model
[10] Zijun Deng, Xiaowei Hu, Lei Zhu, Xuemiao Xu, Jing Qin,                    of saliency-based visual attention for rapid scene analysis.
     Guoqiang Han, and Pheng-Ann Heng. R3 net: Recurrent                       IEEE Transactions on Pattern Analysis and Machine Intelli-
     residual refinement network for saliency detection. In Inter-             gence, 20(11):1254–1259, 1998.
     national Joint Conference on Artificial Intelligence (IJCAI),        [24] Ran Ju, Ling Ge, Wenjing Geng, Tongwei Ren, and Gang-
     pages 684–690, 2018.                                                      shan Wu. Depth saliency based on anisotropic center-
[11] Karthik Desingh, Madhava Krishna K, Deepu Rajan, and                      surround difference. In International Conference on Image
     C. V. Jawahar. Depth really matters: Improving visual salient             Processing (ICIP), pages 1115–1119, 2014.
     region detection with depth. In British Machine Vision Con-          [25] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E. Hinton.
     ference (BMVC), 2013.                                                     Imagenet classification with deep convolutional neural net-
[12] Deng-Ping Fan, Ming-Ming Cheng, Yun Liu, Tao Li, and                      works. Communications of The ACM, 60(6):84–90, 2017.
     Ali Borji. Structure-measure: A new way to evaluate fore-            [26] Ge Li and Chunbiao Zhu. A three-pathway psychobiologi-
     ground maps. In International Conference on Computer Vi-                  cal framework of salient object detection using stereoscopic
     sion (ICCV), pages 4558–4567, 2017.                                       technology. In International Conference on Computer Vision
[13] Deng-Ping Fan, Cheng Gong, Yang Cao, Bo Ren, Ming-                        Workshops (ICCVW), pages 3008–3014, 2017.
     Ming Cheng, and Ali Borji. Enhanced-alignment measure                [27] Nianyi Li, Jinwei Ye, Yu Ji, Haibin Ling, and Jingyi Yu.
     for binary foreground map evaluation. In International Joint              Saliency detection on light field. In Conference on Computer

                                                                        7262
     Vision and Pattern Recognition (CVPR), pages 2806–2813,                 spanning tree. In Conference on Computer Vision and Pat-
     2014.                                                                   tern Recognition (CVPR), pages 2334–2342, 2016.
[28] Xiaohui Li, Huchuan Lu, Lihe Zhang, Xiang Ruan, and                [42] Sanghyun Woo, Jongchan Park, Joon-Young Lee, and In So
     Ming-Hsuan Yang. Saliency detection via dense and sparse                Kweon. Cbam: Convolutional block attention module. Euro-
     reconstruction. In International Conference on Computer Vi-             pean Conference on Computer Vision (ECCV), pages 3–19,
     sion (ICCV), pages 2976–2983, 2013.                                     2018.
[29] Yin Li, Xiaodi Hou, Christof Koch, James M. Rehg, and              [43] Fisher Yu and Vladlen Koltun. Multi-scale context aggre-
     Alan L. Yuille. The secrets of salient object segmentation.             gation by dilated convolutions. International Conference on
     In Conference on Computer Vision and Pattern Recognition                Learning Representations (ICLR), 2016.
     (CVPR), pages 280–287, 2014.                                       [44] Pingping Zhang, Dong Wang, Huchuan Lu, Hongyu Wang,
[30] Nian Liu, Junwei Han, and Ming-Hsuan Yang. Picanet:                     and Xiang Ruan. Amulet: Aggregating multi-level convo-
     Learning pixel-wise contextual attention for saliency detec-            lutional features for salient object detection. In Interna-
     tion. In Conference on Computer Vision and Pattern Recog-               tional Conference on Computer Vision (ICCV), pages 202–
     nition (CVPR), pages 3089–3098, 2018.                                   211, 2017.
[31] Yuzhen Niu, Yujie Geng, Xueqing Li, and Feng Liu. Lever-           [45] Pingping Zhang, Dong Wang, Huchuan Lu, Hongyu Wang,
     aging stereopsis for saliency analysis. In Conference on                and Baocai Yin. Learning uncertain convolutional features
     Computer Vision and Pattern Recognition (CVPR), pages                   for accurate saliency detection. In International Conference
     454–461, 2012.                                                          on Computer Vision (ICCV), pages 212–221, 2017.
[32] Houwen Peng, Bing Li, Weihua Xiong, Weiming Hu, and                [46] Xiaoli Zhang, Xiongfei Li, Yuncong Feng, Haoyu Zhao, and
     Rongrong Ji. Rgbd salient object detection: A benchmark                 Zhaojun Liu. Image fusion with internal generative mecha-
     and algorithms. In European Conference on Computer Vi-                  nism. Expert Systems With Applications, 42(5):2382–2391,
     sion (ECCV), pages 92–109, 2014.                                        2015.
[33] Yongri Piao, Zhengkun Rong, Miao Zhang, Xiao Li, and               [47] Xiaoning Zhang, Tiantian Wang, Jinqing Qi, Huchuan Lu,
     Huchuan Lu. Deep light-field-driven saliency detection from             and Gang Wang. Progressive attention guided recurrent net-
     a single view. In International Joint Conference on Artificial          work for salient object detection. In Conference on Com-
     Intelligence (IJCAI), 2019.                                             puter Vision and Pattern Recognition (CVPR), pages 714–
[34] Yao Qin, Huchuan Lu, Yiqun Xu, and He Wang. Saliency de-                722, 2018.
     tection via cellular automata. In Conference on Computer Vi-
                                                                        [48] Chunbiao Zhu, Xing Cai, Kan Huang, Thomas H Li, and Ge
     sion and Pattern Recognition (CVPR), pages 110–119, 2015.
                                                                             Li. Pdnet: Prior-model guided depth-enhanced network for
[35] Liangqiong Qu, Shengfeng He, Jiawei Zhang, Jiandong                     salient object detection. arXiv preprint arXiv:1803.08636,
     Tian, Yandong Tang, and Qingxiong Yang. Rgbd salient ob-                2018.
     ject detection via deep fusion. IEEE Transactions on Image
                                                                        [49] Chunbiao Zhu, Ge Li, Xiaoqiang Guo, Wenmin Wang, and
     Processing, 26(5):2274–2285, 2017.
                                                                             Ronggang Wang. A multilayer backpropagation saliency de-
[36] Jianqiang Ren, Xiaojin Gong, Lu Yu, Wenhui Zhou, and
                                                                             tection algorithm based on depth mining. In International
     Michael Ying Yang. Exploiting global priors for rgb-
                                                                             Conference on Computer Analysis of Images and Patterns
     d saliency detection. In Conference on Computer Vision
                                                                             (CAIP), pages 14–23, 2017.
     and Pattern Recognition Workshops (CVPRW), pages 25–32,
                                                                        [50] Chunbiao Zhu, Ge Li, Wenmin Wang, and Ronggang Wang.
     2015.
                                                                             An innovative salient object detection using center-dark
[37] Zhixiang Ren, Shenghua Gao, Liang-Tien Chia, and Ivor
                                                                             channel prior. In International Conference on Computer Vi-
     Wai-Hung Tsang. Region-based saliency detection and its
                                                                             sion Workshops (ICCVW), pages 1509–1515, 2017.
     application in object recognition. IEEE Transactions on
     Circuits and Systems for Video Technology, 24(5):769–779,
     2014.
[38] Xingjian Shi, Zhourong Chen, Hao Wang, Dit Yan Yeung,
     Wai Kin Wong, and Wangchun Woo. Convolutional lstm
     network: a machine learning approach for precipitation now-
     casting. Neural Information Processing Systems (NIPS),
     pages 802–810, 2015.
[39] Karen Simonyan and Andrew Zisserman. Very deep con-
     volutional networks for large-scale image recognition. In-
     ternational Conference on Learning Representations (ICLR),
     2015.
[40] Michael W. Tao, Sunil Hadap, Jitendra Malik, and Ravi Ra-
     mamoorthi. Depth from combining defocus and correspon-
     dence using light-field cameras. In International Conference
     on Computer Vision (ICCV), pages 673–680, 2013.
[41] Wei-Chih Tu, Shengfeng He, Qingxiong Yang, and Shao-Yi
     Chien. Real-time salient object detection with a minimum

                                                                      7263
