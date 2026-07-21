---
source_id: 071
bibtex_key: yang2024depthanything
title: Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data
year: 2024
domain_theme: Estimasi Kedalaman
verified_pdf: 71_Depth Anything.pdf
char_count: 94040
---

Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data

                                         Lihe Yang1          Bingyi Kang2 †           Zilong Huang2             Xiaogang Xu3,4           Jiashi Feng2     Hengshuang Zhao1‡
                                                                           1                     2                       3                     4
                                                                               HKU                   TikTok                  CUHK                  ZJU
                                                                                            † project lead      ‡ corresponding author
                                                                                        https://depth-anything.github.io
arXiv:2401.10891v2 [cs.CV] 7 Apr 2024

                                        Figure 1. Our model exhibits impressive generalization ability across extensive unseen scenes. Left two columns: COCO [36]. Middle two:
                                        SA-1B [27] (a hold-out unseen set). Right two: photos captured by ourselves. Our model works robustly in low-light environments (1st and
                                        3rd column), complex scenes (2nd and 5th column), foggy weather (5th column), and ultra-remote distance (5th and 6th column), etc.

                                                                    Abstract                                         1. Introduction
                                            This work presents Depth Anything1 , a highly practical                  The field of computer vision and natural language processing
                                        solution for robust monocular depth estimation. Without pur-                 is currently experiencing a revolution with the emergence of
                                        suing novel technical modules, we aim to build a simple yet                  “foundation models” [6] that demonstrate strong zero-/few-
                                        powerful foundation model dealing with any images under                      shot performance in various downstream scenarios [45, 59].
                                        any circumstances. To this end, we scale up the dataset by                   These successes primarily rely on large-scale training data
                                        designing a data engine to collect and automatically anno-                   that can effectively cover the data distribution. Monocular
                                        tate large-scale unlabeled data (∼62M), which significantly                  Depth Estimation (MDE), which is a fundamental problem
                                        enlarges the data coverage and thus is able to reduce the                    with broad applications in robotics [66], autonomous driv-
                                        generalization error. We investigate two simple yet effective                ing [64, 80], virtual reality [48], etc., also requires a foun-
                                        strategies that make data scaling-up promising. First, a more                dation model to estimate depth information from a single
                                        challenging optimization target is created by leveraging data                image. However, this has been underexplored due to the
                                        augmentation tools. It compels the model to actively seek                    difficulty of building datasets with tens of millions of depth
                                        extra visual knowledge and acquire robust representations.                   labels. MiDaS [46] made a pioneering study along this di-
                                        Second, an auxiliary supervision is developed to enforce                     rection by training an MDE model on a collection of mixed
                                        the model to inherit rich semantic priors from pre-trained                   labeled datasets. Despite demonstrating a certain level of
                                        encoders. We evaluate its zero-shot capabilities extensively,                zero-shot ability, MiDaS is limited by its data coverage, thus
                                        including six public datasets and randomly captured photos.                  suffering disastrous performance in some scenarios.
                                        It demonstrates impressive generalization ability (Figure 1).                    In this work, our goal is to build a foundation model for
                                        Further, through fine-tuning it with metric depth information                MDE capable of producing high-quality depth information
                                        from NYUv2 and KITTI, new SOTAs are set. Our better depth                    for any images under any circumstances. We approach this
                                        model also results in a better depth-conditioned ControlNet.                 target from the perspective of dataset scaling-up. Tradition-
                                        Our models are released here.                                                ally, depth datasets are created mainly by acquiring depth
                                                                                                                     data from sensors [18, 55], stereo matching [15], or SfM [33],
                                            Work was done during an internship at TikTok.
                                                                                                                     which is costly, time-consuming, or even intractable in partic-
                                           1While the grammatical soundness of this name may be questionable,        ular situations. We instead, for the first time, pay attention to
                                        we treat it as a whole and pay homage to Segment Anything [27].              large-scale unlabeled data. Compared with stereo images or

                                                                                                                 1
labeled images from depth sensors, our used monocular unla-                cheap, and diverse unlabeled images for MDE.
beled images exhibit three advantages: (i) (simple and cheap             • We point out a key practice in jointly training large-
to acquire) Monocular images exist almost everywhere, thus                 scale labeled and unlabeled images. Instead of learning
they are easy to collect, without requiring specialized de-                raw unlabeled images directly, we challenge the model
vices. (ii) (diverse) Monocular images can cover a broader                 with a harder optimization target for extra knowledge.
range of scenes, which are critical to the model generaliza-
tion ability and scalability. (iii) (easy to annotate) We can            • We propose to inherit rich semantic priors from pre-
simply use a pre-trained MDE model to assign depth labels                  trained encoders for better scene understanding, rather
for unlabeled images, which only takes a feedforward step.                 than using an auxiliary semantic segmentation task.
More than efficient, this also produces denser depth maps                • Our model exhibits stronger zero-shot capability than
than LiDAR [18] and omits the computationally intensive                    MiDaS-BEiTL-512 [5]. Further, fine-tuned with metric
stereo matching process.                                                   depth, it outperforms ZoeDepth [4] significantly.
    We design a data engine to automatically generate depth
annotations for unlabeled images, enabling data scaling-up            2. Related Work
to arbitrary scale. It collects 62M diverse and informative im-
ages from eight public large-scale datasets, e.g., SA-1B [27],        Monocular depth estimation (MDE). Early works [23, 37,
Open Images [30], and BDD100K [82]. We use their raw                  51] primarily relied on handcrafted features and traditional
unlabeled images without any forms of labels. Then, in or-            computer vision techniques. They were limited by their re-
der to provide a reliable annotation tool for our unlabeled           liance on explicit depth cues and struggled to handle complex
images, we collect 1.5M labeled images from six public                scenes with occlusions and textureless regions.
datasets to train an initial MDE model. The unlabeled im-                 Deep learning-based methods have revolutionized monoc-
ages are then automatically annotated and jointly learned             ular depth estimation by effectively learning depth represen-
with labeled images in a self-training manner [31].                   tations from delicately annotated datasets [18, 55]. Eigen
    Despite all the aforementioned advantages of monocular            et al. [17] first proposed a multi-scale fusion network to
unlabeled images, it is indeed not trivial to make positive use       regress the depth. Following this, many works consistently
of such large-scale unlabeled images [73, 90], especially in          improve the depth estimation accuracy by carefully design-
the case of sufficient labeled images and strong pre-training         ing the regression task as a classification task [3, 34], in-
models. In our preliminary attempts, directly combining la-           troducing more priors [32, 54, 76, 83], and better objective
beled and pseudo labeled images failed to improve the base-           functions [68, 78], etc. Despite the promising performance,
line of solely using labeled images. We conjecture that, the          they are hard to generalize to unseen domains.
additional knowledge acquired in such a naive self-teaching           Zero-shot depth estimation. Our work belongs to this re-
manner is rather limited. To address the dilemma, we pro-             search line. We aim to train an MDE model with a diverse
pose to challenge the student model with a more difficult             training set and thus can predict the depth for any given im-
optimization target when learning the pseudo labels. The              age. Some pioneering works [10, 67] explored this direction
student model is enforced to seek extra visual knowledge              by collecting more training images, but their supervision is
and learn robust representations under various strong pertur-         very sparse and is only enforced on limited pairs of points.
bations to better handle unseen images.                                   To enable effective multi-dataset joint training, a mile-
    Furthermore, there have been some works [9, 21] demon-            stone work MiDaS [46] utilizes an affine-invariant loss to
strating the benefit of an auxiliary semantic segmentation            ignore the potentially different depth scales and shifts across
task for MDE. We also follow this research line, aiming to            varying datasets. Thus, MiDaS provides relative depth infor-
equip our model with better high-level scene understanding            mation. Recently, some works [4, 22, 79] take a step further
capability. However, we observed when an MDE model is                 to estimate the metric depth. However, in our practice, we
already powerful enough, it is hard for such an auxiliary             observe such methods exhibit poorer generalization ability
task to bring further gains. We speculate that it is due to           than MiDaS, especially its latest version [5]. Besides, as
severe loss in semantic information when decoding an im-              demonstrated by ZoeDepth [4], a strong relative depth es-
age into a discrete class space. Therefore, considering the           timation model can also work well in generalizable metric
excellent performance of DINOv2 in semantic-related tasks,            depth estimation by fine-tuning with metric depth informa-
we propose to maintain the rich semantic priors from it with          tion. Therefore, we still follow MiDaS in relative depth
a simple feature alignment loss. This not only enhances the           estimation, but further strengthen it by highlighting the value
MDE performance, but also yields a multi-task encoder for             of large-scale monocular unlabeled images.
both middle-level and high-level perception tasks.
    Our contributions are summarized as follows:                      Leveraging unlabeled data. This belongs to the research
                                                                      area of semi-supervised learning [31, 56, 90], which is pop-
   • We highlight the value of data scaling-up of massive,            ular with various applications [71, 75]. However, existing

                                                                  2
works typically assume only limited images are available.                                                                        Dataset                                Indoor Outdoor Label                                   # Images
They rarely consider the challenging but realistic scenario
                                                                                                                                                                  Labeled Datasets
where there are already sufficient labeled images but also
larger-scale unlabeled images. We take this challenging di-                                                                      BlendedMVS [77]                             ✓                    ✓              Stereo           115K
rection for zero-shot MDE. We demonstrate that unlabeled                                                                         DIML [13]                                   ✓                    ✓              Stereo           927K
                                                                                                                                 HRWSI [68]                                  ✓                    ✓              Stereo            20K
images can significantly enhance the data coverage and thus
                                                                                                                                 IRS [62]                                    ✓                                   Stereo           103K
improve model generalization and robustness.
                                                                                                                                 MegaDepth [33]                                                   ✓              SfM              128K
                                                                                                                                 TartanAir [63]                              ✓                    ✓              Stereo           306K
3. Depth Anything
                                                                                                                                                               Unlabeled Datasets
Our work utilizes both labeled and unlabeled images to
                                                                                                                                 BDD100K [82]                                                     ✓              None             8.2M
facilitate better monocular depth estimation (MDE). For-                                                                         Google Landmarks [65]                                            ✓              None             4.1M
mally, the labeled and unlabeled sets are denoted as Dl =                                                                        ImageNet-21K [50]                           ✓                    ✓              None            13.1M
{(xi , di )}M         u          N
            i=1 and D = {ui }i=1 respectively. We aim to                                                                         LSUN [81]                                   ✓                                   None             9.8M
learn a teacher model T from Dl . Then, we utilize T to                                                                          Objects365 [53]                             ✓                    ✓              None             1.7M
assign pseudo depth labels for Du . Finally, we train a stu-                                                                     Open Images V7 [30]                         ✓                    ✓              None             7.8M
dent model S on the combination of labeled set and pseudo                                                                        Places365 [88]                              ✓                    ✓              None             6.5M
labeled set. A brief illustration is provided in Figure 2.                                                                       SA-1B [27]                                  ✓                    ✓              None            11.1M

3.1. Learning Labeled Images                                                                                                    Table 1. In total, our Depth Anything is trained on 1.5M labeled
                                                                                                                                images and 62M unlabeled images jointly.
This process is similar to the training of MiDaS [5, 46].
However, since MiDaS did not release its code, we first
reproduced it. Concretely, the depth value is first transformed                                                                 our easy-to-acquire and diverse unlabeled images will com-
into the disparity space by d = 1/t and then normalized                                                                         prehend the data coverage and greatly enhance the model
to 0∼1 on each depth map. To enable multi-dataset joint                                                                         generalization ability and robustness.
training, we adopt the affine-invariant loss to ignore the                                                                         Furthermore, to strengthen the teacher model T learned
unknown scale and shift of each sample:                                                                                         from these labeled images, we adopt the DINOv2 [43] pre-
                                                                                                                                trained weights to initialize our encoder. In practice, we
                                   \mathcal {L}_l = \frac {1}{HW}\sum _{i=1}^{HW}\rho (d_i^*, d_i),                   (1)       apply a pre-trained semantic segmentation model [70] to de-
                                                                                                                                tect the sky region, and set its disparity value as 0 (farthest).

where d∗i and di are the prediction and ground truth, respec-                                                                   3.2. Unleashing the Power of Unlabeled Images
tively. And ρ is the affine-invariant mean absolute error loss:                                                                 This is the main point of our work. Distinguished from prior
ρ(d∗i , di ) = |dˆ∗i − dˆi |, where dˆ∗i and dˆi are the scaled and                                                             works that laboriously construct diverse labeled datasets,
shifted versions of the prediction d∗i and ground truth di :                                                                    we highlight the value of unlabeled images in enhancing
                                                                                                                                the data coverage. Nowadays, we can practically build a
                                                \hat {d}_i = \frac {d_i - t(d)}{s(d)},                                (2)       diverse and large-scale unlabeled set from the Internet or
                                                                                                                                public datasets of various tasks. Also, we can effortlessly
where t(d) and s(d) are used to align the prediction and                                                                        obtain the dense depth map of monocular unlabeled images
ground truth to have zero translation and unit scale:                                                                           simply by forwarding them to a pre-trained well-performed
                                                                                                                                MDE model. This is much more convenient and efficient
                                                                                                                                than performing stereo matching or SfM reconstruction for
     \label {eq:median} t(d) = \textrm {median}(d),\hspace {2mm} s(d) = \frac {1}{HW}\sum _{i=1}^{HW}|d_i - t(d)|.    (3)       stereo images or videos. We select eight large-scale public
                                                                                                                                datasets as our unlabeled sources for their diverse scenes.
                                                                                                                                They contain more than 62M images in total. The details are
   To obtain a robust monocular depth estimation model, we
                                                                                                                                provided in the bottom half of Table 1.
collect 1.5M labeled images from 6 public datasets. Details
                                                                                                                                   Technically, given the previously obtained MDE teacher
of these datasets are listed in Table 1. We use fewer labeled
                                                                                                                                model T , we make predictions on the unlabeled set Du to
datasets than MiDaS v3.1 [5] (12 training datasets), because
                                                                                                                                obtain a pseudo labeled set D̂u :
1) we do not use NYUv2 [55] and KITTI [18] datasets to
ensure zero-shot evaluation on them, 2) some datasets are                                                                                       \hat {\mathcal {D}}^u = \{(u_i, T(u_i)) | u_i \in \mathcal {D}^u\}_{i=1}^N.          (4)
not available (anymore), e.g., Movies [46] and WSVD [61],
and 3) some datasets exhibit poor quality, e.g., RedWeb (also                                                                      With the combination set Dl ∪ Dˆu of labeled images and
low resolution) [67]. Despite using fewer labeled images,                                                                       pseudo labeled images, we train a student model S on it.

                                                                                                                            3
HRWSI: 102684_LookInStereoDotComDSCF0486                                                                                       feature
SA1B: sa_10000139                                                                                                            alignment

        labeled image                                                                                                                                                                labeled prediction                                      manual label
                                                                                                                                                                                                                                                                                                    LiDAR,
                                                                                                                                                                                                                     sup
                                                                               encoder                                                      decoder                                                                                                                                                 matching,
                                                                                                                                                                                                                                                                                                    SfM, etc
                                                        S
                                                                                                                                  semantic
                                                                                                                                preservation                                                                                                                                                             teacher
                                                                               encoder                                                                                                                                sup                                                                                 model

     unlabeled image                                                                                                                                                                 unlabeled prediction                                    pseudo label

    Figure 2. Our pipeline. Solid line: flow of labeled images, dotted line: unlabeled images. We especially highlight the value of large-scale
    unlabeled images. The S denotes adding strong perturbations (Section 3.2). To equip our depth estimation model with rich semantic priors,
    we enforce an auxiliary constraint between the online student model and a frozen encoder to preserve the semantic capability (Section 3.3).
                                                                                                                                                                                                         P
    Following prior works [74], instead of fine-tuning S from T ,                                                                                                                     where we omit the     and pixel subscript i for simplicity.
    we re-initialize S for better performance.                                                                                                                                        Then we aggregate the two losses via weighted averaging:
       Unfortunately, in our pilot studies, we failed to gain im-
    provements with such a self-training pipeline, which indeed                                                                                                                                     \mathcal {L}_u = \frac {\sum M}{HW}\mathcal {L}^M_u + \frac {\sum (1-M)}{HW}\mathcal {L}^{1-M}_u.          (8)
    contradicts the observations when there are only a few la-
    beled images [56]. We conjecture that, with already suffi-                                                                                                                            We use CutMix with 50% probability. The unlabeled
    cient labeled images in our case, the extra knowledge ac-                                                                                                                          images for CutMix are already strongly distorted in color,
    quired from additional unlabeled images is rather limited.                                                                                                                         but the unlabeled images fed into the teacher model T for
    Especially considering the teacher and student share the                                                                                                                           pseudo labeling are clean, without any distortions.
    same pre-training and architecture, they tend to make similar
    correct or false predictions on the unlabeled set Du , even                                                                                                                        3.3. Semantic-Assisted Perception
    without the explicit self-training procedure.                                                                                                                                     There exist some works [9, 21, 28, 72] improving depth es-
       To address the dilemma, we propose to challenge the stu-                                                                                                                       timation with an auxiliary semantic segmentation task. We
    dent with a more difficult optimization target for additional                                                                                                                     believe that arming our depth estimation model with such
    visual knowledge on unlabeled images. We inject strong per-                                                                                                                       high-level semantic-related information is beneficial. Be-
    turbations to unlabeled images during training. It compels                                                                                                                        sides, in our specific context of leveraging unlabeled images,
    our student model to actively seek extra visual knowledge                                                                                                                         these auxiliary supervision signals from other tasks can also
    and acquire invariant representations from these unlabeled                                                                                                                        combat the potential noise in our pseudo depth label.
    images. These advantages help our model deal with the open                                                                                                                           Therefore, we made an initial attempt by carefully assign-
    world more robustly. We introduce two forms of perturba-                                                                                                                          ing semantic segmentation labels to our unlabeled images
    tions: one is strong color distortions, including color jittering                                                                                                                 with a combination of RAM [86] + GroundingDINO [38] +
    and Gaussian blurring, and the other is strong spatial dis-                                                                                                                       HQ-SAM [26] models. After post-processing, this yields a
    tortion, which is CutMix [84]. Despite the simplicity, the                                                                                                                        class space containing 4K classes. In the joint-training stage,
    two modifications make our large-scale unlabeled images                                                                                                                           the model is enforced to produce both depth and segmenta-
    significantly improve the baseline of labeled images.                                                                                                                             tion predictions with a shared encoder and two individual
       We provide more details about CutMix. It was originally                                                                                                                        decoders. Unfortunately, after trial and error, we still could
    proposed for image classification, and is rarely explored in                                                                                                                      not boost the performance of the original MDE model. We
    monocular depth estimation. We first interpolate a random                                                                                                                         speculated that, decoding an image into a discrete class space
    pair of unlabeled images ua and ub spatially:                                                                                                                                     indeed loses too much semantic information. The limited
                                                                                                                                                                                      information in these semantic masks is hard to further boost
                                          u_{ab} = u_a \odot M + u_b \odot (1 - M),                                                                                        (5)        our depth model, especially when our depth model has es-
                                                                                                                                                                                      tablished very competitive results.
    where M is a binary mask with a rectangle region set as 1.
                                                                                                                                                                                         Therefore, we aim to seek more informative semantic sig-
        The unlabeled loss Lu is obtained by first computing
                                                                                                                                                                                      nals to serve as auxiliary supervision for our depth estimation
    affine-invariant losses in valid regions defined by M and
                                                                                                                                                                                      task. We are greatly astonished by the strong performance
    1 − M , respectively:
                                                                                                                                                                                      of DINOv2 models [43] in semantic-related tasks, e.g., im-
         &\mathcal {L}^M_u = \rho \big (S(u_{ab}) \odot M, \,T(u_a) \odot M\big ),\\ &\mathcal {L}^{1-M}_u = \rho \big (S(u_{ab}) \odot (1-M), T(u_b) \odot (1-M)\big ),              age retrieval and semantic segmentation, even with frozen
                                                                                                                                                                                      weights without any fine-tuning. Motivated by these clues,
                                                                                                                                                                           (7)        we propose to transfer its strong semantic capability to our

                                                                                                                                                                                 4
                                                    KITTI [18]                       NYUv2 [55]         Sintel [7]      DDAD [20]        ETH3D [52]       DIODE [60]
 Method                    Encoder
                                                AbsRel                δ1          AbsRel     δ1     AbsRel       δ1    AbsRel    δ1     AbsRel    δ1     AbsRel    δ1
 MiDaS v3.1 [5]              ViT-L               0.127             0.850            0.048   0.980   0.587      0.699   0.251    0.766   0.139    0.867   0.075    0.942
                             ViT-S               0.080             0.936            0.053   0.972   0.464      0.739   0.247    0.768   0.127    0.885   0.076    0.939
 Depth Anything              ViT-B               0.080             0.939            0.046   0.979   0.432      0.756   0.232    0.786   0.126    0.884   0.069    0.946
                             ViT-L               0.076             0.947            0.043   0.981   0.458      0.760   0.230    0.789   0.127    0.882   0.066    0.952

Table 2. Zero-shot relative depth estimation. Better: AbsRel ↓ , δ1 ↑. We compare with the best model from MiDaS v3.1. Note that MiDaS
does not strictly follow the zero-shot evaluation on KITTI and NYUv2, because it uses their training images. We provide three model scales
for different purposes, based on ViT-S (24.8M), ViT-B (97.5M), and ViT-L (335.3M), respectively. Best, second best results.

depth model with an auxiliary feature alignment loss. The                                                depth regression. All labeled datasets are simply combined
feature space is high-dimensional and continuous, thus con-                                              together without re-sampling. In the first stage, we train a
taining richer semantic information than discrete masks. The                                             teacher model on labeled images for 20 epochs. In the second
feature alignment loss is formulated as:                                                                 stage of joint training, we train a student model to sweep
                                                                                                         across all unlabeled images for one time. The unlabeled
                                                                                                         images are annotated by a best-performed teacher model
               \mathcal {L}_{feat} = 1 - \frac {1}{HW}\sum _{i=1}^{HW}\cos (f_i, f'_i),       (9)
                                                                                                         with a ViT-L encoder. The ratio of labeled and unlabeled
                                                                                                         images is set as 1:2 in each batch. In both stages, the base
where cos(·, ·) measures the cosine similarity between two                                               learning rate of the pre-trained encoder is set as 5e-6, while
feature vectors. f is the feature extracted by the depth model                                           the randomly initialized decoder uses a 10× larger learning
S, while f ′ is the feature from a frozen DINOv2 encoder.                                                rate. We use the AdamW optimizer and decay the learning
We do not follow some works [19] to project the online                                                   rate with a linear schedule. We only apply horizontal flipping
feature f into a new space for alignment, because a randomly                                             as our data augmentation for labeled images. The tolerance
initialized projector makes the large alignment loss dominate                                            margin α for feature alignment loss is set as 0.85. For more
the overall loss in the early stage.                                                                     details, please refer to our appendix.
    Another key point in feature alignment is that, semantic
encoders like DINOv2 tend to produce similar features for
                                                                                                         4.2. Zero-Shot Relative Depth Estimation
different parts of an object, e.g., car front and rear. In depth                                         As aforementioned, this work aims to provide accurate
estimation, however, different parts or even pixels within the                                           depth estimation for any image. Therefore, we compre-
same part, can be of varying depth. Thus, it is not beneficial                                           hensively validate the zero-shot depth estimation capability
to exhaustively enforce our depth model to produce exactly                                               of our Depth Anything model on six representative unseen
the same features as the frozen encoder.                                                                 datasets: KITTI [18], NYUv2 [55], Sintel [7], DDAD [20],
    To solve this issue, we set a tolerance margin α for the                                             ETH3D [52], and DIODE [60]. We compare with the best
feature alignment. If the cosine similarity of fi and fi′ has                                            DPT-BEiTL-512 model from the latest MiDaS v3.1 [5], which
surpassed α, this pixel will not be considered in our Lf eat .                                           uses more labeled images than us. As shown in Table 2,
This allows our method to enjoy both the semantic-aware                                                  both with a ViT-L encoder, our Depth Anything surpasses
representation from DINOv2 and the part-level discrimina-                                                the strongest MiDaS model tremendously across extensive
tive representation from depth supervision. As a side effect,                                            scenes in terms of both the AbsRel (absolute relative error:
our produced encoder not only performs well in downstream                                                |d∗ − d|/d) and δ1 (percentage of max(d∗ /d, d/d∗ ) < 1.25)
MDE datasets, but also achieves strong results in the seman-                                             metrics. For example, when tested on the well-known au-
tic segmentation task. It also indicates the potential of our                                            tonomous driving dataset DDAD [20], we improve the Ab-
encoder to serve as a universal multi-task encoder for both                                              sRel (↓) from 0.251 → 0.230 and improve the δ1 (↑) from
middle-level and high-level perception tasks.                                                            0.766 → 0.789.
    Finally, our overall loss is an average combination of the                                              Besides, our ViT-B model is already clearly superior to
three losses Ll , Lu , and Lf eat .                                                                      the MiDaS based on a much larger ViT-L. Moreover, our
                                                                                                         ViT-S model, whose scale is less than 1/10 of the MiDaS
4. Experiment                                                                                            model, even outperforms MiDaS on several unseen datasets,
                                                                                                         including Sintel, DDAD, and ETH3D. The performance
4.1. Implementation Details
                                                                                                         advantage of these small-scale models demonstrates their
We adopt the DINOv2 encoder [43] for feature extraction.                                                 great potential in computationally-constrained scenarios.
Following MiDaS [5, 46], we use the DPT [47] decoder for                                                    It is also worth noting that, on the most widely used MDE

                                                                                                    5
                   Higher is better ↑       Lower is better ↓                             Higher is better ↑         Lower is better ↓
        Method                                                                 Method
                  δ1      δ2       δ3    AbsRel   RMSE     log10                          δ1      δ2      δ3     AbsRel RMSE RMSE log
   AdaBins [3]   0.903   0.984   0.997   0.103    0.364    0.044           AdaBins [3]   0.964   0.995   0.999   0.058   2.360      0.088
     DPT [47]    0.904   0.988   0.998   0.110    0.357    0.045             DPT [47]    0.959   0.995   0.999   0.062   2.573      0.092
  P3Depth [44]   0.898   0.981   0.996   0.104    0.356    0.043          P3Depth [44]   0.953   0.993   0.998   0.071   2.842      0.103
 SwinV2-L [40]   0.949   0.994   0.999   0.083    0.287    0.035        NeWCRFs [83]     0.974   0.997   0.999   0.052   2.129      0.079
      AiT [42]   0.954   0.994   0.999   0.076    0.275    0.033        SwinV2-L [40]    0.977   0.998   1.000   0.050   1.966      0.075
     VPD [87]    0.964   0.995   0.999   0.069    0.254    0.030         NDDepth [54]    0.978   0.998   0.999   0.050   2.025      0.075
 ZoeDepth∗ [4]   0.951   0.994   0.999   0.077    0.282    0.033         GEDepth [76]    0.976   0.997   0.999   0.048   2.044      0.076
                                                                        ZoeDepth∗ [4]    0.971   0.996   0.999   0.054   2.281      0.082
         Ours    0.984   0.998   1.000   0.056    0.206    0.024
                                                                                 Ours 0.982 0.998 1.000          0.046   1.896      0.069
Table 3. Fine-tuning and evaluating on NYUv2 [55] with our
pre-trained MDE encoder. We highlight best, second best results,       Table 4. Fine-tuning and evaluating on KITTI [18] with our
as well as most discriminative metrics. ∗: Reproduced by us.           pre-trained MDE encoder. ∗: Reproduced by us.

benchmarks KITTI and NYUv2, although MiDaS v3.1 uses                   coder with metric depth information from NYUv2 [55] (for
the corresponding training images (not zero-shot anymore),             indoor scenes) or KITTI [18] (for outdoor scenes). There-
our Depth Anything is still evidently superior to it without           fore, we simply replace the MiDaS encoder with our bet-
training with any KITTI or NYUv2 images, e.g., 0.127 vs.               ter Depth Anything encoder, leaving other components un-
0.076 in AbsRel and 0.850 vs. 0.947 in δ1 on KITTI.                    changed. As shown in Table 5, across a wide range of unseen
                                                                       datasets of indoor and outdoor scenes, our Depth Anything
4.3. Fine-tuned to Metric Depth Estimation                             results in a better metric depth estimation model than the
Apart from the impressive performance in zero-shot relative            original ZoeDepth based on MiDaS.
depth estimation, we further examine our Depth Anything
                                                                       4.4. Fine-tuned to Semantic Segmentation
model as a promising weight initialization for downstream
metric depth estimation. We initialize the encoder of down-            In our method, we design our MDE model to inherit the
stream MDE models with our pre-trained encoder parameters              rich semantic priors from a pre-trained encoder via a sim-
and leave the decoder randomly initialized. The model is               ple feature alignment constraint. Here, we examine the
fine-tuned with correponding metric depth information. In              semantic capability of our MDE encoder. Specifically, we
this part, we use our ViT-L encoder for fine-tuning.                   fine-tune our MDE encoder to downstream semantic segmen-
    We examine two representative scenarios: 1) in-domain              tation datasets. As exhibited in Table 7 of the Cityscapes
metric depth estimation, where the model is trained and                dataset [15], our encoder from large-scale MDE training
evaluated on the same domain (Section 4.3.1), and 2) zero-             (86.2 mIoU) is superior to existing encoders from large-scale
shot metric depth estimation, where the model is trained on            ImageNet-21K pre-training, e.g., Swin-L [39] (84.3) and
one domain, e.g., NYUv2 [55], but evaluated in different               ConvNeXt-XL [41] (84.6). Similar observations hold on the
domains, e.g., SUN RGB-D [57] (Section 4.3.2).                         ADE20K dataset [89] in Table 8. We improve the previous
                                                                       best result from 58.3 → 59.4.
4.3.1   In-Domain Metric Depth Estimation                                  We hope to highlight that, witnessing the superiority of
                                                                       our pre-trained encoder on both monocular depth estimation
As shown in Table 3 of NYUv2 [55], our model outperforms               and semantic segmentation tasks, we believe it has great
the previous best method VPD [87] remarkably, improving                potential to serve as a generic multi-task encoder for both
the δ1 (↑) from 0.964 → 0.984 and AbsRel (↓) from 0.069                middle-level and high-level visual perception systems.
to 0.056. Similar improvements can be observed in Table 4
of the KITTI dataset [18]. We improve the δ1 (↑) on KITTI              4.5. Ablation Studies
from 0.978 → 0.982. It is worth noting that we adopt the
                                                                       Unless otherwise specified, we use the ViT-L encoder for
ZoeDepth framework for this scenario with a relatively ba-
                                                                       our ablation studies here.
sic depth model, and we believe our results can be further
enhanced if equipped with more advanced architectures.                 Zero-shot transferring of each training dataset. In Ta-
                                                                       ble 6, we provide the zero-shot transferring performance of
4.3.2   Zero-Shot Metric Depth Estimation                              each training dataset, which means that we train a relative
                                                                       MDE model on one training set and evaluate it on the six
We follow ZoeDepth [4] to conduct zero-shot metric depth               unseen datasets. With these results, we hope to offer more
estimation. ZoeDepth fine-tunes the MiDaS pre-trained en-              insights for future works that similarly aim to build a general

                                                                   6
                         SUN RGB-D [57]                iBims-1 [29]                  HyperSim [49]       Virtual KITTI 2 [8]         DIODE Outdoor [60]
  Method
                        AbsRel (↓)        δ1 (↑)     AbsRel           δ1         AbsRel           δ1     AbsRel            δ1        AbsRel             δ1
  ZoeDepth [4]            0.520           0.545       0.169        0.656             0.407      0.302     0.106           0.844       0.814        0.237
  Depth Anything          0.500           0.660       0.150        0.714             0.363      0.361     0.085           0.913       0.794        0.288

Table 5. Zero-shot metric depth estimation. The first three test sets in the header are indoor scenes, while the last two are outdoor scenes.
Following ZoeDepth, we use the model trained on NYUv2 for indoor generalization, while use the model trained on KITTI for outdoor
evaluation. For fair comparisons, we report the ZoeDepth results reproduced in our environment.

                        KITTI [18]        NYUv2 [55]             Sintel [7]            DDAD [20]         ETH3D [52]         DIODE [60]            Mean
 Training set
                       AbsRel     δ1     AbsRel       δ1      AbsRel        δ1        AbsRel      δ1    AbsRel     δ1      AbsRel      δ1      AbsRel        δ1
 BlendedMVS [77]       0.089    0.918     0.068     0.958     0.556        0.689      0.305     0.731   0.148     0.845     0.092     0.921    0.210     0.844
 DIML [13]             0.099    0.907     0.055     0.969     0.573        0.722      0.381     0.657   0.142     0.859     0.107     0.908    0.226     0.837
 HRWSI [68]            0.095    0.917     0.062     0.966     0.502        0.731      0.270     0.750   0.186     0.775     0.087     0.935    0.200     0.846
 IRS [62]              0.105    0.892     0.057     0.970     0.568        0.714      0.328     0.691   0.143     0.845     0.088     0.926    0.215     0.840
 MegaDepth [33]        0.217    0.741     0.071     0.953     0.632        0.660      0.479     0.566   0.142     0.852     0.104     0.910    0.274     0.780
 TartanAir [63]        0.088    0.920     0.061     0.964     0.602        0.723      0.332     0.690   0.160     0.818     0.088     0.928    0.222     0.841
 All labeled data      0.085    0.934     0.053     0.971     0.492        0.748      0.245     0.771   0.134     0.874     0.070     0.945    0.180     0.874

Table 6. Examine the zero-shot transferring performance of each labeled training set (left) to six unseen datasets (top). Better performance:
AbsRel ↓ , δ1 ↑. We highlight the best, second, and third best results for each test dataset in bold, underline, and italic, respectively.

            Method                     Encoder     mIoU (s.s.)     m.s.                                 Method                      Encoder        mIoU
   Segmenter [58]             ViT-L [16]               -           82.2                        Segmenter [58]                ViT-L [16]            51.8
   SegFormer [70]            MiT-B5 [70]              82.4         84.0                        SegFormer [70]               MiT-B5 [70]            51.0
 Mask2Former [12]            Swin-L [39]              83.3         84.3                      Mask2Former [12]               Swin-L [39]            56.4
  OneFormer [24]             Swin-L [39]              83.0         84.4                          UperNet [69]                BEiT-L [2]            56.3
  OneFormer [24]        ConvNeXt-XL [41]              83.6         84.6                       ViT-Adapter [11]               BEiT-L [2]            58.3
        DDP [25]         ConvNeXt-L [41]              83.2         83.9                        OneFormer [24]               Swin-L [39]            57.4
                                                                                               OneFormer [24]           ConNeXt-XL [41]            57.4
                Ours              ViT-L [16]          84.8         86.2
                                                                                                          Ours                    ViT-L [16]       59.4
Table 7. Transferring our MDE pre-trained encoder to Cityscapes
for semantic segmentation. We do not use Mapillary [1] for pre-                       Table 8. Transferring our MDE encoder to ADE20K for semantic
training. s.s./m.s.: single-/multi-scale evaluation.                                  segmentation. We use Mask2Former as our segmentation model.

monocular depth estimation system. Among the six training                             since the labeled images are already sufficient. However,
datasets, HRWSI [68] fuels our model with the strongest                               with strong perturbations (S) applied to unlabeled images
generalization ability, even though it only contains 20K im-                          during re-training, the student model is challenged to seek
ages. This indicates the data diversity counts a lot, which                           additional visual knowledge and learn more robust repre-
is well aligned with our motivation to utilize unlabeled im-                          sentations. Consequently, the large-scale unlabeled images
ages. Some labeled datasets may not perform very well, e.g.,                          enhance the model generalization ability significantly.
MegaDepth [33], however, it has its own preferences that                                 Moreover, with our used semantic constraint Lf eat , the
are not reflected in these six test datasets. For example, we                         power of unlabeled images can be further amplified for the
find models trained with MegaDepth data are specialized at                            depth estimation task. More importantly, as emphasized in
estimating the distance of ultra-remote buildings (Figure 1),                         Section 4.4, this auxiliary constraint also enables our trained
which will be very beneficial for aerial vehicles.                                    encoder to serve as a key component in a multi-task visual
                                                                                      system for both middle-level and high-level perception.
Effectiveness of 1) challenging the student model when
learning unlabeled images, and 2) semantic constraint.                                Comparison with MiDaS trained encoder in downstream
As shown in Table 9, simply adding unlabeled images with                              tasks. Our Depth Anything model has exhibited stronger
pseudo labels does not necessarily bring gains to our model,                          zero-shot capability than MiDaS [5, 46]. Here, we further

                                                                                 7
                                                                                    Ours              MiDaS          Ours           MiDaS

       Figure 3. Qualitative results on six unseen datasets.                   Figure 4. We compare our depth prediction with MiDaS. Meantime,
                                                                               we use ControlNet to synthesize new images from the depth map.

 Ll Lu S Lf eat           KI     NY        SI     DD       ET       DI
                                                                                                 NYUv2                KITTI         ADE20K
 ✓                    0.085      0.053   0.492    0.245   0.134    0.070        Encoder
                                                                                           AbsRel (↓)     δ1 (↑)   AbsRel     δ1    mIoU (↑)
 ✓    ✓               0.085      0.054   0.481    0.242   0.138    0.073
 ✓    ✓ ✓             0.081      0.048   0.469    0.235   0.134    0.068        DINOv2        0.066       0.973    0.058    0.971     58.8
 ✓    ✓ ✓       ✓     0.076      0.043   0.458    0.230   0.127    0.066        Ours          0.056       0.984    0.046    0.982     59.4

Table 9. Ablation studies of: 1) challenging the student with strong           Table 11. Comparison between the original DINOv2 and our pro-
perturbations (S) when learning unlabeled images, and 2) semantic              duced encoder in terms of downstream fine-tuning performance.
constraint (Lf eat ). Limited by space, we only report the AbsRel
(↓) metric, and shorten the dataset name with its first two letters.
                                                                               4.6. Qualitative Results
              NYUv2               KITTI          Cityscapes ADE20K             We visualize our model predictions on the six unseen datasets
 Method
          AbsRel     δ1        AbsRel     δ1       mIoU         mIoU           in Figure 3. Our model is robust to test images from various
 MiDaS     0.077    0.951      0.054     0.971     82.1           52.4
                                                                               domains. In addition, we compare our model with MiDaS
 Ours      0.056    0.984      0.046     0.982     84.8           59.4         in Figure 4. We also attempt to synthesis new images con-
                                                                               ditioned on the predicted depth maps with ControlNet [85].
Table 10. Comparison between our trained encoder and MiDaS [5]                 Our model produces more accurate depth estimation than
trained encoder in terms of downstream fine-tuning performance.                MiDaS, as well as better synthesis results. For more accurate
Better performance: AbsRel ↓ , δ1 ↑ , mIoU ↑ .                                 synthesis, we re-trained a better depth-conditioned Control-
                                                                               Net based on our Depth Anything, aiming to provide better
                                                                               control signals for image synthesis and video editing. Please
compare our trained encoder with MiDaS v3.1 [5] trained                        refer to our project page for more qualitative results on video
encoder in terms of the downstream fine-tuning performance.                    editing [35] with our Depth Anything.
As demonstrated in Table 10, on both the downstream depth
estimation task and semantic segmentation task, our pro-                       5. Conclusion
duced encoder outperforms the MiDaS encoder remarkably,
e.g., 0.951 vs. 0.984 in the δ1 metric on NYUv2, and 52.4                      In this work, we present Depth Anything, a highly practical
vs. 59.4 in the mIoU metric on ADE20K.                                         solution to robust monocular depth estimation. Different
                                                                               from prior arts, we especially highlight the value of cheap
Comparison with DINOv2 in downstream tasks. We                                 and diverse unlabeled images. We design two simple yet
have demonstrated the superiority of our trained encoder                       highly effective strategies to fully exploit their value: 1)
when fine-tuned to downstream tasks. Since our finally                         posing a more challenging optimization target when learning
produced encoder (from large-scale MDE training) is fine-                      unlabeled images, and 2) preserving rich semantic priors
tuned from DINOv2 [43], we compare our encoder with the                        from pre-trained models. As a result, our Depth Anything
original DINOv2 encoder in Table 11. It can be observed                        model exhibits excellent zero-shot depth estimation ability,
that our encoder performs better than the original DINOv2                      and also serves as a promising initialization for downstream
encoder in both the downstream metric depth estimation                         metric depth estimation and semantic segmentation tasks.
task and semantic segmentation task. Although the DINOv2
weight has provided a very strong initialization, our large-                   Acknowledgement. This work is supported by the National
scale and high-quality MDE training can further enhance it                     Natural Science Foundation of China (No. 62201484), HKU
impressively in downstream transferring performance.                           Startup Fund, and HKU Seed Fund for Basic Research.

                                                                           8
        Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data
                                               Supplementary Material
6. More Implementation Details                                         α       KITTI NYU Sintel DDAD ETH3D DIODE Mean

We resize the shorter side of all images to 518 and keep the           1.00 0.085 0.055 0.523        0.250    0.134     0.079   0.188
original aspect ratio. All images are cropped to 518×518               0.85 0.080 0.053 0.464        0.247    0.127     0.076   0.175
during training. During inference, we do not crop images               0.70 0.079 0.054 0.482        0.248    0.127     0.077   0.178
and only ensure both sides are multipliers of 14, since the
                                                                      Table 12. Ablation studies on different values of the tolerance
pre-defined patch size of DINOv2 encoders [43] is 14. Eval-
                                                                      margin α for the feature alignment loss Lf eat . Limited by space,
uation is performed at the original resolution by interpolating
                                                                      we only report the AbsRel (↓) metric here.
the prediction. Following MiDaS [5, 46], in zero-shot eval-
uation, the scale and shift of our prediction are manually
                                                                      Lf eat             Unseen datasets (AbsRel ↓)
aligned with the ground truth.                                                                                                   Mean
    When fine-tuning our pre-trained encoder to metric depth          U L KITTI NYU Sintel DDAD ETH3D DIODE
estimation, we adopt the ZoeDepth codebase [4]. We merely                    0.083 0.055 0.478        0.249    0.133    0.080    0.180
replace the original MiDaS-based encoder with our stronger            ✓      0.080 0.053 0.464        0.247    0.127    0.076    0.175
Depth Anything encoder, with a few hyper-parameters mod-                   ✓ 0.084 0.054 0.472        0.252    0.133    0.081    0.179
ified. Concretely, the training resolution is 392×518 on
NYUv2 [55] and 384×768 on KITTI [18] to match the                     Table 13. Ablation studies of applying our feature alignment loss
patch size of our encoder. The encoder learning rate is               Lf eat to unlabeled data (U) or labeled data (L).
set as 1/50 of the learning rate of the randomly initialized
decoder, which is much smaller than the 1/10 adopted for              because the labeled data has relatively higher-quality depth
MiDaS encoder, due to our strong initialization. The batch            annotations. The involvement of semantic loss may interfere
size is 16 and the model is trained for 5 epochs.                     with the learning of these informative manual labels. In com-
    When fine-tuning our pre-trained encoder to semantic seg-         parison, our pseudo labels are noisier and less informative.
mentation, we use the MMSegmentation codebase [14]. The               Therefore, introducing the auxiliary constraint to unlabeled
training resolution is set as 896×896 on both ADE20K [89]             data can combat the noise in pseudo depth labels, as well as
and Cityscapes [15]. The encoder learning rate is set as              arm our model with semantic capability.
3e-6 and the decoder learning rate is 10× larger. We use
Mask2Former [12] as our semantic segmentation model. The              8. Limitations and Future Works
model is trained for 160K iterations on ADE20K and 80K
iterations on Cityscapes both with batch size 16, without             Currently, the largest model size is only constrained to ViT-
any COCO [36] or Mapillary [1] pre-training. Other training           Large [16]. Therefore, in the future, we plan to further scale
configurations are the same as the original codebase.                 up the model size from ViT-Large to ViT-Giant, which is
                                                                      also well pre-trained by DINOv2 [43]. We can train a more
7. More Ablation Studies                                              powerful teacher model with the larger model, producing
                                                                      more accurate pseudo labels for smaller models to learn, e.g.,
All ablation studies here are conducted on the ViT-S model.           ViT-L and ViT-B. Furthermore, to facilitate real-world ap-
The necessity of tolerance margin for feature alignment.              plications, we believe the widely adopted 512×512 training
As shown in Table 12, the gap between the tolerance margin            resolution is not enough. We plan to re-train our model on a
of 1.00 and 0.85 or 0.70 clearly demonstrates the necessity           larger resolution of 700+ or even 1000+.
of this design (mean AbsRel: 0.188 vs. 0.175).
                                                                      9. More Qualitative Results
Applying feature alignment to labeled data. Previously,
we enforce the feature alignment loss Lf eat on unlabeled             Please refer to the following pages for comprehensive quali-
data. Indeed, it is technically feasible to also apply this           tative results on six unseen test sets (Figure 5 for KITTI [18],
constraint to labeled data. In Table 13, apart from applying          Figure 6 for NYUv2 [55], Figure 7 for Sintel [7], Figure 8
Lf eat on unlabeled data, we explore to apply it to labeled           for DDAD [20], Figure 9 for ETH3D [52], and Figure 10
data. We find that adding this auxiliary optimization target          for DIODE [60]). We compare our model with the strongest
to labeled data is not beneficial to our baseline that does not       MiDaS model [5], i.e., DPT-BEiTL-512 . Our model exhibits
involve any feature alignment (their mean AbsRel values are           higher depth estimation accuracy and stronger robustness.
almost the same: 0.180 vs. 0.179). We conjecture that this is         Please refer to our project page for more visualizations.

                                                                  9
                Input image                                  Our prediction                          MiDaS v3.1 prediction

Figure 5. Qualitative results on KITTI. Due to the extremely sparse ground truth which is hard to visualize, we here compare our prediction
with the most advanced MiDaS v3.1 [5] prediction. The brighter color denotes the closer distance.

                                                                    10
            Input image                                 Our prediction                          MiDaS v3.1 prediction

Figure 6. Qualitative results on NYUv2. It is worth noting that MiDaS [5] uses NYUv2 training data (not zero-shot), while we do not.

                                                                11
Input image            Our prediction                    MiDaS v3.1 prediction

              Figure 7. Qualitative results on Sintel.

                                12
Input image           Our prediction                   MiDaS v3.1 prediction

              Figure 8. Qualitative results on DDAD.

                               13
Input image             Our prediction                  MiDaS v3.1 prediction

              Figure 9. Qualitative results on ETH3D.

                                14
Input image             Our prediction                   MiDaS v3.1 prediction

              Figure 10. Qualitative results on DIODE.

                                15
References                                                                 [17] David Eigen, Christian Puhrsch, and Rob Fergus. Depth
                                                                                map prediction from a single image using a multi-scale deep
 [1] Manuel López Antequera, Pau Gargallo, Markus Hofinger,                    network. In NeurIPS, 2014. 2
     Samuel Rota Bulò, Yubin Kuang, and Peter Kontschieder.               [18] Andreas Geiger, Philip Lenz, Christoph Stiller, and Raquel
     Mapillary planet-scale depth dataset. In ECCV, 2020. 7, 9                  Urtasun. Vision meets robotics: The kitti dataset. IJRR, 2013.
 [2] Hangbo Bao, Li Dong, Songhao Piao, and Furu Wei. Beit:                     1, 2, 3, 5, 6, 7, 9
     Bert pre-training of image transformers. In ICLR, 2022. 7             [19] Jean-Bastien Grill, Florian Strub, Florent Altché, Corentin
 [3] Shariq Farooq Bhat, Ibraheem Alhashim, and Peter Wonka.                    Tallec, Pierre Richemond, Elena Buchatskaya, Carl Doer-
     Adabins: Depth estimation using adaptive bins. In CVPR,                    sch, Bernardo Avila Pires, Zhaohan Guo, Mohammad Ghesh-
     2021. 2, 6                                                                 laghi Azar, et al. Bootstrap your own latent-a new approach
 [4] Shariq Farooq Bhat, Reiner Birkl, Diana Wofk, Peter Wonka,                 to self-supervised learning. In NeurIPS, 2020. 5
     and Matthias Müller. Zoedepth: Zero-shot transfer by com-            [20] Vitor Guizilini, Rares Ambrus, Sudeep Pillai, Allan Raventos,
     bining relative and metric depth. arXiv:2302.12288, 2023. 2,               and Adrien Gaidon. 3d packing for self-supervised monocular
     6, 7, 9                                                                    depth estimation. In CVPR, 2020. 5, 7, 9
 [5] Reiner Birkl, Diana Wofk, and Matthias Müller. Midas v3.             [21] Vitor Guizilini, Rui Hou, Jie Li, Rares Ambrus, and Adrien
     1–a model zoo for robust monocular relative depth estimation.              Gaidon. Semantically-guided representation learning for self-
     arXiv:2307.14460, 2023. 2, 3, 5, 7, 8, 9, 10, 11                           supervised monocular depth. In ICLR, 2020. 2, 4
 [6] Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ                     [22] Vitor Guizilini, Igor Vasiljevic, Dian Chen, Rares, Ambrus, ,
     Altman, Simran Arora, Sydney von Arx, Michael S Bern-                      and Adrien Gaidon. Towards zero-shot scale-aware monocu-
     stein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill,                   lar depth estimation. In ICCV, 2023. 2
     et al. On the opportunities and risks of foundation models.           [23] Derek Hoiem, Alexei A Efros, and Martial Hebert. Recover-
     arXiv:2108.07258, 2021. 1                                                  ing surface layout from an image. IJCV, 2007. 2
 [7] Daniel J Butler, Jonas Wulff, Garrett B Stanley, and Michael J        [24] Jitesh Jain, Jiachen Li, Mang Tik Chiu, Ali Hassani, Nikita
     Black. A naturalistic open source movie for optical flow                   Orlov, and Humphrey Shi. Oneformer: One transformer to
     evaluation. In ECCV, 2012. 5, 7, 9                                         rule universal image segmentation. In CVPR, 2023. 7
 [8] Yohann Cabon, Naila Murray, and Martin Humenberger. Vir-              [25] Yuanfeng Ji, Zhe Chen, Enze Xie, Lanqing Hong, Xihui Liu,
     tual kitti 2. arXiv:2001.10773, 2020. 7                                    Zhaoqiang Liu, Tong Lu, Zhenguo Li, and Ping Luo. Ddp:
 [9] Po-Yi Chen, Alexander H Liu, Yen-Cheng Liu, and Yu-                        Diffusion model for dense visual prediction. In ICCV, 2023.
     Chiang Frank Wang. Towards scene understanding: Un-                        7
     supervised monocular depth estimation with semantic-aware             [26] Lei Ke, Mingqiao Ye, Martin Danelljan, Yifan Liu, Yu-Wing
     representation. In CVPR, 2019. 2, 4                                        Tai, Chi-Keung Tang, and Fisher Yu. Segment anything in
                                                                                high quality. In NeurIPS, 2023. 4
[10] Weifeng Chen, Zhao Fu, Dawei Yang, and Jia Deng. Single-
                                                                           [27] Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao,
     image depth perception in the wild. In NeurIPS, 2016. 2
                                                                                Chloe Rolland, Laura Gustafson, Tete Xiao, Spencer White-
[11] Zhe Chen, Yuchen Duan, Wenhai Wang, Junjun He, Tong
                                                                                head, Alexander C Berg, Wan-Yen Lo, et al. Segment any-
     Lu, Jifeng Dai, and Yu Qiao. Vision transformer adapter for
                                                                                thing. In ICCV, 2023. 1, 2, 3
     dense predictions. In ICLR, 2023. 7
                                                                           [28] Marvin Klingner, Jan-Aike Termöhlen, Jonas Mikolajczyk,
[12] Bowen Cheng, Ishan Misra, Alexander G Schwing, Alexander                   and Tim Fingscheidt. Self-supervised monocular depth es-
     Kirillov, and Rohit Girdhar. Masked-attention mask trans-                  timation: Solving the dynamic object problem by semantic
     former for universal image segmentation. In CVPR, 2022. 7,                 guidance. In ECCV, 2020. 4
     9                                                                     [29] Tobias Koch, Lukas Liebel, Friedrich Fraundorfer, and Marco
[13] Jaehoon Cho, Dongbo Min, Youngjung Kim, and Kwanghoon                      Korner. Evaluation of cnn-based single-image depth estima-
     Sohn. Diml/cvl rgb-d dataset: 2m rgb-d images of natural                   tion methods. In ECCVW, 2018. 7
     indoor and outdoor scenes. arXiv:2110.11590, 2021. 3, 7               [30] Alina Kuznetsova, Hassan Rom, Neil Alldrin, Jasper Uijlings,
[14] MMSegmentation Contributors.                   MMSegmenta-                 Ivan Krasin, Jordi Pont-Tuset, Shahab Kamali, Stefan Popov,
     tion:      Openmmlab semantic segmentation toolbox                         Matteo Malloci, Alexander Kolesnikov, et al. The open im-
     and benchmark.         https : / / github . com / open -                   ages dataset v4: Unified image classification, object detection,
     mmlab/mmsegmentation, 2020. 9                                              and visual relationship detection at scale. IJCV, 2020. 2, 3
[15] Marius Cordts, Mohamed Omran, Sebastian Ramos, Timo                   [31] Dong-Hyun Lee et al. Pseudo-label: The simple and efficient
     Rehfeld, Markus Enzweiler, Rodrigo Benenson, Uwe Franke,                   semi-supervised learning method for deep neural networks.
     Stefan Roth, and Bernt Schiele. The cityscapes dataset for                 In ICMLW, 2013. 2
     semantic urban scene understanding. In CVPR, 2016. 1, 6, 9            [32] Bo Li, Chunhua Shen, Yuchao Dai, Anton Van Den Hen-
[16] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,                     gel, and Mingyi He. Depth and surface normal estimation
     Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,                        from monocular images using regression on deep features and
     Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-                   hierarchical crfs. In CVPR, 2015. 2
     vain Gelly, et al. An image is worth 16x16 words: Trans-              [33] Zhengqi Li and Noah Snavely. Megadepth: Learning single-
     formers for image recognition at scale. In ICLR, 2021. 7,                  view depth prediction from internet photos. In CVPR, 2018.
     9                                                                          1, 3, 7

                                                                      16
[34] Zhenyu Li, Xuyang Wang, Xianming Liu, and Junjun Jiang.              [49] Mike Roberts, Jason Ramapuram, Anurag Ranjan, Atulit
     Binsformer: Revisiting adaptive bins for monocular depth                  Kumar, Miguel Angel Bautista, Nathan Paczan, Russ Webb,
     estimation. arXiv:2204.00987, 2022. 2                                     and Joshua M Susskind. Hypersim: A photorealistic synthetic
[35] Jun Hao Liew, Hanshu Yan, Jianfeng Zhang, Zhongcong Xu,                   dataset for holistic indoor scene understanding. In ICCV,
     and Jiashi Feng. Magicedit: High-fidelity and temporally                  2021. 7
     coherent video editing. arXiv:2308.14749, 2023. 8                    [50] Olga Russakovsky, Jia Deng, Hao Su, Jonathan Krause, San-
[36] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,                  jeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy,
     Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence                Aditya Khosla, Michael Bernstein, et al. Imagenet large scale
     Zitnick. Microsoft coco: Common objects in context. In                    visual recognition challenge. IJCV, 2015. 3
     ECCV, 2014. 1, 9                                                     [51] Ashutosh Saxena, Min Sun, and Andrew Y Ng. Make3d:
[37] Ce Liu, Jenny Yuen, Antonio Torralba, Josef Sivic, and                    Learning 3d scene structure from a single still image. TPAMI,
     William T Freeman. Sift flow: Dense correspondence across                 2008. 2
     different scenes. In ECCV, 2008. 2                                   [52] Thomas Schops, Johannes L Schonberger, Silvano Galliani,
[38] Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao                      Torsten Sattler, Konrad Schindler, Marc Pollefeys, and An-
     Zhang, Jie Yang, Chunyuan Li, Jianwei Yang, Hang Su, Jun                  dreas Geiger. A multi-view stereo benchmark with high-
     Zhu, et al. Grounding dino: Marrying dino with grounded                   resolution images and multi-camera videos. In CVPR, 2017.
     pre-training for open-set object detection. arXiv:2303.05499,             5, 7, 9
     2023. 4                                                              [53] Shuai Shao, Zeming Li, Tianyuan Zhang, Chao Peng, Gang
                                                                               Yu, Xiangyu Zhang, Jing Li, and Jian Sun. Objects365: A
[39] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng
                                                                               large-scale, high-quality dataset for object detection. In ICCV,
     Zhang, Stephen Lin, and Baining Guo. Swin transformer:
                                                                               2019. 3
     Hierarchical vision transformer using shifted windows. In
     ICCV, 2021. 6, 7                                                     [54] Shuwei Shao, Zhongcai Pei, Weihai Chen, Xingming Wu, and
                                                                               Zhengguo Li. Nddepth: Normal-distance assisted monocular
[40] Ze Liu, Han Hu, Yutong Lin, Zhuliang Yao, Zhenda Xie,
                                                                               depth estimation. In ICCV, 2023. 2, 6
     Yixuan Wei, Jia Ning, Yue Cao, Zheng Zhang, Li Dong, et al.
                                                                          [55] Nathan Silberman, Derek Hoiem, Pushmeet Kohli, and Rob
     Swin transformer v2: Scaling up capacity and resolution. In
                                                                               Fergus. Indoor segmentation and support inference from rgbd
     CVPR, 2022. 6
                                                                               images. In ECCV, 2012. 1, 2, 3, 5, 6, 7, 9
[41] Zhuang Liu, Hanzi Mao, Chao-Yuan Wu, Christoph Feicht-
                                                                          [56] Kihyuk Sohn, David Berthelot, Nicholas Carlini, Zizhao
     enhofer, Trevor Darrell, and Saining Xie. A convnet for the
                                                                               Zhang, Han Zhang, Colin A Raffel, Ekin Dogus Cubuk,
     2020s. In CVPR, 2022. 6, 7
                                                                               Alexey Kurakin, and Chun-Liang Li. Fixmatch: Simplifying
[42] Jia Ning, Chen Li, Zheng Zhang, Chunyu Wang, Zigang                       semi-supervised learning with consistency and confidence. In
     Geng, Qi Dai, Kun He, and Han Hu. All in tokens: Unifying                 NeurIPS, 2020. 2, 4
     output space of visual tasks via soft token. In ICCV, 2023. 6
                                                                          [57] Shuran Song, Samuel P Lichtenberg, and Jianxiong Xiao.
[43] Maxime Oquab, Timothée Darcet, Théo Moutakanni, Huy Vo,                 Sun rgb-d: A rgb-d scene understanding benchmark suite. In
     Marc Szafraniec, Vasil Khalidov, Pierre Fernandez, Daniel                 CVPR, 2015. 6, 7
     Haziza, Francisco Massa, Alaaeldin El-Nouby, et al. Dinov2:          [58] Robin Strudel, Ricardo Garcia, Ivan Laptev, and Cordelia
     Learning robust visual features without supervision. TMLR,                Schmid. Segmenter: Transformer for semantic segmentation.
     2023. 3, 4, 5, 8, 9                                                       In ICCV, 2021. 7
[44] Vaishakh Patil, Christos Sakaridis, Alexander Liniger, and           [59] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Mar-
     Luc Van Gool. P3depth: Monocular depth estimation with a                  tinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste
     piecewise planarity prior. In CVPR, 2022. 6                               Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al.
[45] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya                        Llama: Open and efficient foundation language models.
     Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,                     arXiv:2302.13971, 2023. 1
     Amanda Askell, Pamela Mishkin, Jack Clark, et al. Learning           [60] Igor Vasiljevic, Nick Kolkin, Shanyi Zhang, Ruotian Luo,
     transferable visual models from natural language supervision.             Haochen Wang, Falcon Z Dai, Andrea F Daniele, Mo-
     In ICML, 2021. 1                                                          hammadreza Mostajabi, Steven Basart, Matthew R Walter,
[46] René Ranftl, Katrin Lasinger, David Hafner, Konrad                       et al. Diode: A dense indoor and outdoor depth dataset.
     Schindler, and Vladlen Koltun. Towards robust monocular                   arXiv:1908.00463, 2019. 5, 7, 9
     depth estimation: Mixing datasets for zero-shot cross-dataset        [61] Chaoyang Wang, Simon Lucey, Federico Perazzi, and Oliver
     transfer. TPAMI, 2020. 1, 2, 3, 5, 7, 9                                   Wang. Web stereo video supervision for depth prediction
[47] René Ranftl, Alexey Bochkovskiy, and Vladlen Koltun. Vi-                 from dynamic scenes. In 3DV, 2019. 3
     sion transformers for dense prediction. In ICCV, 2021. 5,            [62] Qiang Wang, Shizhen Zheng, Qingsong Yan, Fei Deng, Kaiy-
     6                                                                         ong Zhao, and Xiaowen Chu. Irs: A large naturalistic indoor
[48] Alex Rasla and Michael Beyeler. The relative importance                   robotics stereo dataset to train deep models for disparity and
     of depth cues and semantic edges for indoor mobility using                surface normal estimation. In ICME, 2021. 3, 7
     simulated prosthetic vision in immersive virtual reality. In         [63] Wenshan Wang, Delong Zhu, Xiangwei Wang, Yaoyu Hu,
     VRST, 2022. 1                                                             Yuheng Qiu, Chen Wang, Yafei Hu, Ashish Kapoor, and

                                                                     17
     Sebastian Scherer. Tartanair: A dataset to push the limits of         [80] Yurong You, Yan Wang, Wei-Lun Chao, Divyansh Garg, Ge-
     visual slam. In IROS, 2020. 3, 7                                           off Pleiss, Bharath Hariharan, Mark Campbell, and Kilian Q
[64] Yan Wang, Wei-Lun Chao, Divyansh Garg, Bharath Hariha-                     Weinberger. Pseudo-lidar++: Accurate depth for 3d object
     ran, Mark Campbell, and Kilian Q Weinberger. Pseudo-lidar                  detection in autonomous driving. In ICLR, 2020. 1
     from visual depth estimation: Bridging the gap in 3d object           [81] Fisher Yu, Ari Seff, Yinda Zhang, Shuran Song, Thomas
     detection for autonomous driving. In CVPR, 2019. 1                         Funkhouser, and Jianxiong Xiao. Lsun: Construction of a
[65] Tobias Weyand, Andre Araujo, Bingyi Cao, and Jack Sim.                     large-scale image dataset using deep learning with humans in
     Google landmarks dataset v2-a large-scale benchmark for                    the loop. arXiv:1506.03365, 2015. 3
     instance-level recognition and retrieval. In CVPR, 2020. 3            [82] Fisher Yu, Haofeng Chen, Xin Wang, Wenqi Xian, Yingying
[66] Diana Wofk, Fangchang Ma, Tien-Ju Yang, Sertac Karaman,                    Chen, Fangchen Liu, Vashisht Madhavan, and Trevor Dar-
     and Vivienne Sze. Fastdepth: Fast monocular depth estima-                  rell. Bdd100k: A diverse driving dataset for heterogeneous
     tion on embedded systems. In ICRA, 2019. 1                                 multitask learning. In CVPR, 2020. 2, 3
[67] Ke Xian, Chunhua Shen, Zhiguo Cao, Hao Lu, Yang Xiao,                 [83] Weihao Yuan, Xiaodong Gu, Zuozhuo Dai, Siyu Zhu, and
     Ruibo Li, and Zhenbo Luo. Monocular relative depth per-                    Ping Tan. New crfs: Neural window fully-connected crfs for
     ception with web stereo data supervision. In CVPR, 2018. 2,                monocular depth estimation. arXiv:2203.01502, 2022. 2, 6
     3                                                                     [84] Sangdoo Yun, Dongyoon Han, Seong Joon Oh, Sanghyuk
[68] Ke Xian, Jianming Zhang, Oliver Wang, Long Mai, Zhe Lin,                   Chun, Junsuk Choe, and Youngjoon Yoo. Cutmix: Regu-
     and Zhiguo Cao. Structure-guided ranking loss for single                   larization strategy to train strong classifiers with localizable
     image depth prediction. In CVPR, 2020. 2, 3, 7                             features. In ICCV, 2019. 4
                                                                           [85] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Adding
[69] Tete Xiao, Yingcheng Liu, Bolei Zhou, Yuning Jiang, and
                                                                                conditional control to text-to-image diffusion models. In
     Jian Sun. Unified perceptual parsing for scene understanding.
                                                                                ICCV, 2023. 8
     In ECCV, 2018. 7
                                                                           [86] Youcai Zhang, Xinyu Huang, Jinyu Ma, Zhaoyang Li,
[70] Enze Xie, Wenhai Wang, Zhiding Yu, Anima Anandkumar,
                                                                                Zhaochuan Luo, Yanchun Xie, Yuzhuo Qin, Tong Luo, Yaqian
     Jose M Alvarez, and Ping Luo. Segformer: Simple and
                                                                                Li, Shilong Liu, et al. Recognize anything: A strong image
     efficient design for semantic segmentation with transformers.
                                                                                tagging model. arXiv:2306.03514, 2023. 4
     In NeurIPS, 2021. 3, 7
                                                                           [87] Wenliang Zhao, Yongming Rao, Zuyan Liu, Benlin Liu, Jie
[71] Mengde Xu, Zheng Zhang, Han Hu, Jianfeng Wang, Lijuan
                                                                                Zhou, and Jiwen Lu. Unleashing text-to-image diffusion
     Wang, Fangyun Wei, Xiang Bai, and Zicheng Liu. End-to-end
                                                                                models for visual perception. In ICCV, 2023. 6
     semi-supervised object detection with soft teacher. In ICCV,
                                                                           [88] Bolei Zhou, Agata Lapedriza, Aditya Khosla, Aude Oliva,
     2021. 2
                                                                                and Antonio Torralba. Places: A 10 million image database
[72] Xiaogang Xu, Hengshuang Zhao, Vibhav Vineet, Ser-Nam                       for scene recognition. TPAMI, 2017. 3
     Lim, and Antonio Torralba. Mtformer: Multi-task learning
                                                                           [89] Bolei Zhou, Hang Zhao, Xavier Puig, Sanja Fidler, Adela Bar-
     via transformer and cross-task reasoning. In ECCV, 2022. 4
                                                                                riuso, and Antonio Torralba. Scene parsing through ade20k
[73] I Zeki Yalniz, Hervé Jégou, Kan Chen, Manohar Paluri, and                dataset. In CVPR, 2017. 6, 9
     Dhruv Mahajan. Billion-scale semi-supervised learning for
                                                                           [90] Barret Zoph, Golnaz Ghiasi, Tsung-Yi Lin, Yin Cui, Hanx-
     image classification. arXiv:1905.00546, 2019. 2
                                                                                iao Liu, Ekin Dogus Cubuk, and Quoc Le. Rethinking pre-
[74] Lihe Yang, Wei Zhuo, Lei Qi, Yinghuan Shi, and Yang Gao.                   training and self-training. In NeurIPS, 2020. 2
     St++: Make self-training work better for semi-supervised
     semantic segmentation. In CVPR, 2022. 4
[75] Lihe Yang, Lei Qi, Litong Feng, Wayne Zhang, and
     Yinghuan Shi. Revisiting weak-to-strong consistency in semi-
     supervised semantic segmentation. In CVPR, 2023. 2
[76] Xiaodong Yang, Zhuang Ma, Zhiyu Ji, and Zhe Ren. Gedepth:
     Ground embedding for monocular depth estimation. In ICCV,
     2023. 2, 6
[77] Yao Yao, Zixin Luo, Shiwei Li, Jingyang Zhang, Yufan Ren,
     Lei Zhou, Tian Fang, and Long Quan. Blendedmvs: A large-
     scale dataset for generalized multi-view stereo networks. In
     CVPR, 2020. 3, 7
[78] Wei Yin, Yifan Liu, Chunhua Shen, and Youliang Yan. En-
     forcing geometric constraints of virtual normal for depth pre-
     diction. In ICCV, 2019. 2
[79] Wei Yin, Chi Zhang, Hao Chen, Zhipeng Cai, Gang Yu, Kaix-
     uan Wang, Xiaozhi Chen, and Chunhua Shen. Metric3d:
     Towards zero-shot metric 3d prediction from a single image.
     In ICCV, 2023. 2

                                                                      18
