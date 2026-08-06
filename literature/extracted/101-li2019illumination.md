---
source_id: 101
bibtex_key: li2019illumination
title: Illumination-aware Faster R-CNN for Robust Multispectral Pedestrian Detection
year: 2019 (jurnal); pracetak arXiv 2018
domain_theme: Pedestrian RGB-T
verified_pdf: 101_IAF R-CNN (Illumination-Aware).pdf
char_count: 102325
---

Illumination-aware Faster R-CNN for Robust Multispectral Pedestrian Detection

                                                                                Chengyang Li, Dan Song, Ruofeng Tong∗, Min Tang
                                                                          State Key Lab of CAD&CG, Zhejiang University, Hangzhou, Zhejiang, China

                                         Abstract
                                         Multispectral images of color-thermal pairs have shown more effective than a single color channel for pedestrian de-
arXiv:1803.05347v2 [cs.CV] 14 Aug 2018

                                         tection, especially under challenging illumination conditions. However, there is still a lack of studies on how to fuse
                                         the two modalities effectively. In this paper, we deeply compare six different convolutional network fusion architec-
                                         tures and analyse their adaptations, enabling a vanilla architecture to obtain detection performances comparable to the
                                         state-of-the-art results. Further, we discover that pedestrian detection confidences from color or thermal images are
                                         correlated with illumination conditions. With this in mind, we propose an Illumination-aware Faster R-CNN (IAF R-
                                         CNN). Specifically, an Illumination-aware Network is introduced to give an illumination measure of the input image.
                                         Then we adaptively merge color and thermal sub-networks via a gate function defined over the illumination value.
                                         The experimental results on KAIST Multispectral Pedestrian Benchmark validate the effectiveness of the proposed
                                         IAF R-CNN.
                                         Keywords: multispectral pedestrian detection, illumination-aware, gated fusion

                                         1. Introduction                                                        appearance of KAIST multispectral pedestrian dataset
                                                                                                                [12], some approaches designed for color modality are
                                            Pedestrian detection, as a canonical sub-problem of                 extended to perform multispectral pedestrian detection,
                                         general object detection, has been intensively investi-                including convnets based approaches [16, 17, 18, 19].
                                         gated by the computer vision community [1, 2, 3], due
                                                                                                                   However, there is a lack of in-depth comparison of
                                         to its diversified applications in video surveillance, car
                                                                                                                different network architectures with respect to neces-
                                         safety, image retrieval, robotics, etc. Thanks to the in-
                                                                                                                sary adaptations to the pedestrian detection task. It is
                                         troduction of convolutional neural networks (convnets),
                                                                                                                still unclear what upper limit a vanilla convnet architec-
                                         especially Faster R-CNN [4] and its variants, the past
                                                                                                                ture could reach, and in what aspects further improve-
                                         few years have witnessed remarkable improvement in
                                                                                                                ments are expected. Therefore, in this paper we com-
                                         pedestrian detection quality [5, 6, 7, 8, 9, 10, 11]. How-
                                                                                                                pare six different convnet fusion architectures which are
                                         ever, most of current pedestrian detectors are restricted
                                                                                                                derived from Faster R-CNN and discuss several poten-
                                         to the benchmarks of color images with good lighting
                                                                                                                tial adaptations. We show that once properly adapted, a
                                         conditions, whereas they probably fail to work under
                                                                                                                vanilla multispectral Faster R-CNN obtains significant
                                         bad illumination conditions, e.g., images captured dur-
                                                                                                                improvement from baseline and almost matches the de-
                                         ing nighttime or bad weather days.
                                                                                                                tection performance of the state-of-the-art approach.
                                            Efforts have been invested to deal with bad illumi-
                                                                                                                   Intuitively, color and thermal modalities are comple-
                                         nation conditions by considering other types of sen-
                                                                                                                mentary with each other since they provide different
                                         sors, such as near infrared cameras, time-of-flight cam-
                                                                                                                visual cues. Nevertheless, it remains a question how
                                         eras and long-wave infrared (thermal) cameras. Among
                                                                                                                confidently we can rely on each modality. Our exper-
                                         these sensors, thermal cameras are the most widely used
                                                                                                                iments reveal that under good illumination conditions,
                                         [12, 13, 14, 15], due to their visibility of pedestrian in-
                                                                                                                color and thermal images are complementary with each
                                         stances in challenging illumination conditions. With the
                                                                                                                other; whereas under bad illumination conditions, using
                                            ∗ Corresponding author
                                                                                                                thermal images alone is a better choice and fusing with
                                             Email addresses: licy_cs@zju.edu.cn (Chengyang Li),
                                                                                                                color modality offers no improvement in detection accu-
                                         songdan1992@zju.edu.cn (Dan Song), trf@zju.edu.cn                      racy (details will be given in Section 3.4). This suggests
                                         (Ruofeng Tong), tang_m@zju.edu.cn (Min Tang)                           that the illumination measure can be used as an indicator
                                         Preprint submitted to Pattern Recognition                                                                          August 15, 2018
to facilitate the fusion problem.                                  The remainder of this paper is organized as follows.
   Existing convnets based approaches address the fu-           We first review related work in Section 2. Then we com-
sion problem of color and thermal modalities mainly             pare and analyse six different network fusion architec-
via two ways. One is to merge the two streams with              tures and explore their key adaptations in Section 3. Our
equal-weight at score level, regardless of the contribu-        IAF R-CNN is proposed in Section 4, followed by ex-
tions of the two modalities. This strategy is especially        tensive experimental results given in Section 5. Finally,
error-prone under bad lighting situations. The other is         we conclude the paper in Section 6.
to fuse the two streams at a specific layer, expecting
the network to learn the weighting parameters automat-
ically. However, either image classification or object          2. Related work
detection models are tuned to be insensitive to illumina-
tion changes, which makes their parameters unsuitable           Convnets for pedestrian detection. Driven by the
to draw the weighting decision. To better handle the            success of convolutional neural networks (convnets)
fusion problem, a weighting mechanism which takes il-           in other classification and detection tasks, the re-
lumination conditions into account is in demand.                search community has also explored convnets based ap-
   Motivated by the above idea, in this paper we de-            proaches for pedestrian detection in the past couple of
velop a novel Illumination-Aware Faster R-CNN (IAF              years. Most of initial attempts [5, 6, 20, 21, 22] to
R-CNN) framework. We show our weighting mecha-                  apply convnets for pedestrian detection task adopted a
nism in Fig. 1. Given a pair of color-thermal images            two-stage pipeline in an R-CNN [23] style. In these ap-
and pedestrian proposals generated from region pro-             proaches, traditional detectors (usually ICF [24] and its
posal network (omitted in the figure for conciseness),          extensions [25, 26, 27]) were used to generate region
color and thermal sub-networks output separate detec-           proposals, followed by a convnet to re-classify the pro-
tion confidence scores and bounding box regressions for         posed regions. Other approaches applied convnets in
each proposal. The final detection result is acquired           a sliding window manner. ConvNet [28] used convo-
by merging the outputs of the two sub-networks with             lutional sparse auto-encoders to initialize the layer pa-
an illumination-aware weighing mechanism which con-             rameters, then fine-tuned in a small pedestrian dataset.
sists of two steps. First, an illumination-aware network        VeryFast [29] built a convnet cascade, in which a tiny
is used to offer an illumination measure for the given          convnet is adopted to filter candidates before passing
image. Then, the illumination-aware weights for two             through to a deep convent. F-DNN [11] used a soft
modalities are predicted by a gate function defined over        cascade mechanism and fused multiple convnets in the
the illumination measure. It should be noticed that us-         second cascade stage. Although Faster R-CNN [4] has
ing the proposed IAF R-CNN framework, we can jointly            become the de-facto standard architecture for general
train both multispectral Faster R-CNN and weighting             object detection, it under-performed when directly ap-
parameters, which makes our method efficient in train-          plied to pedestrian detection task, due to low object res-
ing.                                                            olution as well as background confusion [8]. Better
   To sum up, our major contributions are threefold:            performances can be achieved when boosted decision
(1) We make in-depth comparison of six convnet fu-              forest was applied on top of convolution feature maps
sion architectures derived from Faster R-CNN and point          [8, 30, 31]. Other top-performing approaches typically
out their key adaptations. We reveal that once prop-            adopted customized convnets derived from Fast/Faster
erly adapted, the performance of a vanilla multispec-           R-CNN architectures [7, 10]. Zhang et al. [9] re-
tral Faster R-CNN gains remarkable improvement from             vealed that after proper adaptation, a plain Faster R-
baseline and almost matches that of the state-of-the-           CNN model can match the state-of-the-art detection
art approach. (2) We propose an IAF R-CNN model                 performances. Recent work [32, 33] were built upon
for multispectral pedestrian detection, which integrates        Faster R-CNN architecture and focused on occlusion
color sub-network, thermal sub-network and a weight-            handling. Wang et al. [32] proposed a new bounding
ing layer into a unified framework. (3) We propose              box regression loss called Repulsion Loss, which par-
an illumination-aware weighting mechanism to lift the           ticully imporved detection performance in crowd occlu-
contributions of color and thermal sub-networks and             sion scenes. Zhang et al. [33] explored different kinds
boost the final detection performance under both good           of attention mechinism, incluing self attention, bound-
and bad illumination conditions. Using the proposed             ing box based attention and body part based attention,
IAF R-CNN, we achieve new state-of-the-art perfor-              among which body part based attention was the most
mance on KAIST Multispectral Pedestrian Benchmark.              effecitve one. Xu et al. [34] first trained a RGB-thermal
                                                            2
                                                     Illumination-aware weighting
                       Good Illumination Condition                                         Bad Illumination Condition

                                   Color                                                              Color
                                Sub-network                                                        Sub-network

                                                     Detection Results                                                  Detection Results

                                  Thermal                                                            Thermal
                                Sub-network                                                        Sub-network

Figure 1: Illustration of the illumination-aware weighting mechanism of our IAF R-CNN. A color and a thermal sub-network are responsible for
detecting pedestrian instances from color and thermal images respectively. The final detection result is obtained by merging the outputs of the
two sub-networks according to the illumination conditions. Left: under good illumination conditions, the weight for color sub-network is higher
than that for the thermal sub-network. In this way, color sub-network contributes more than thermal sub-network. Right: under bad illumination
conditions, the weight for the thermal sub-network is close to 1. Thus, the final result is dominant by the thermal sub-network. For the sake of
conciseness, the region proposal stage is hidden from view in this figure.

transfer network using multispectral data. During in-                        cantly outperform that in [18].
ference stage only RGB images were used and cross-                           Network fusion problems. In this paper we focus on
modal representations were extracted from raw RGB                            network based multispectral fusion, but we should note
images to perform detection. Existing convnets based                         that other methods exist than network based ones (see
approaches typically focus on color images only. In this                     [36, 37] for surveys of visible and infrared image fu-
paper, we explore Faster R-CNN architecture for multi-                       sion). Although network fusion is less explored for
spectral pedestrian detection.                                               multispectral pedestrian detection [16, 18], it is widely
Multispectral pedestrian detection. Despite the ex-                          discussed in other vision tasks, such as action recogni-
tensive studies of pedestrian detection task, only a few                     tion [38, 39, 40], semantic segmentation [41, 42, 43],
works have targeted multispectral images. Hwang et                           3D object classification/detection [44, 45], etc. In [38],
al. [12] extended aggregated channel features (ACF)                          Simonyan et al. proposed two-stream convnets for ac-
pedestrian detector [25] and proposed multispectral                          tion recognition, applying two sub-networks to tackle
ACF by augmenting the thermal intensity and HOG fea-                         color images and optical flow images separately, which
ture of the thermal image as additional channel fea-                         were then combined by averaging the obtained confi-
tures. Wagner et al. [16] generated the proposals us-                        dence scores. Karpathy et al. [39] discussed several
ing multispectral ACF, followed by a late fusion based                       schemes to fuse temporal frames at different speeds for
CNN classifier to re-score them. Choi et al. [17] first                      video classification. Cheng et al. [43] introduced a
generated proposals separate color and thermal stream,                       gated fusion layer combining RGB and depth stream
and then classified the proposals using support vector                       according to their varying contributions with respect to
regression (SVR) on top of the concatenated convolu-                         different categories and scenes for better semantic seg-
tional features. This pipeline was further extended by                       mentation. Targeting scale-variance problem in pedes-
Park et al. [35], by replacing shallow modules to net-                       trian detection, SAF R-CNN [7] designed a large-scale
work components, thus it can be optimized end-to-end.                        sub-network and a small-scale sub-network to tackle
Liu et al. [18] introduced Faster R-CNN architecture for                     large instances and small instances respectively, and
multispectral pedestrian detection, and they discussed                       then fused the two sub-networks by weighting accord-
four different covnet fusion architectures to fuse color                     ing to the height of proposals. Our IAF R-CNN is sim-
and thermal information at different stages. König et                       ilar to SAF R-CNN, as we share a similar divide-and-
al. [19] applied boosted decision trees to re-score the                      conquer philosophy. However, our approach is different
proposal regions generated by region proposal network.                       from theirs in four aspects: (1) SAF R-CNN focuses
Our first contribution is most closely related to [18], but                  on a single color channel while our IAF R-CNN tar-
we provide better adapted models through making more                         gets multispectral images; (2) SAF R-CNN is designed
comprehensive and in-depth investigations. We analyse                        to address the scale-variance problem in single color
six fusion architectures while Liu et al. [18] only inves-                   modality while our IAF R-CNN is proposed to tackle
tigate four. We examine the impacts of several potential                     color-thermal fusion problem; (3) SAF R-CNN is built
adaptations, enable the detection performances signifi-                      upon Fast R-CNN pipeline [46] while our IAF R-CNN
                                                                         3
is derived from Faster R-CNN framework [4]; (4) our                Late Fusion is a kind of high-level fusion, which con-
IAF R-CNN adopts a novel weighting mechanism con-                  catenates the last fully-connected layers from color and
sidering the property of specific multispectral pedestrian         thermal sub-networks. The feature maps after the last
detection task.                                                    convolutional blocks of the two sub-networks are con-
                                                                   catenated, upon which region proposal module is built.
                                                                   Score fusion I generates proposals and detections by
3. Faster R-CNN for multispectral pedestrian detec-
                                                                   the two sub-networks separately. The detections are
   tion
                                                                   then fed to the other sub-network to re-score the con-
                                                                   fidence. The final detections are obtained by merging
   Features at different network stages exhibit different
                                                                   the two-stage detection confidence scores with equal
focuses, with finer visual details in lower layers and
                                                                   weights of 0.5. Thus, it can be viewed as a cascade
richer semantic meanings in higher layers. In this sec-
                                                                   design of the two sub-networks.
tion, we make an in-depth comparison of six network
fusion architectures derived from Faster R-CNN [4],                Score fusion II is a non-cascade way of fusion at score
namely Input Fusion, Early Fusion, Halfway Fusion,                 level. Similar to Late Fusion, human proposals are
Late Fusion, Score Fusion I and Score Fusion II. As                generated by exploiting feature maps from two sub-
shown in Fig. 2, the six architectures integrate color             networks. Then the proposals are taken as input by both
and thermal modalities at a different stages. Four of              sub-networks to generate detection results separately.
them have been referred in [18], while other two archi-            Finally, both detection scores and bounding box regres-
tectures (i.e. Input Fusion and Score Fusion II) are in-           sions from two sub-networks are averaged to obtain the
cluded for more comprehensive study. These two fusion              final detections. Compared with Score Fusion I, this ex-
architectures have been adopted in many vision tasks               ecution is more efficient in training and testing.
[16, 43], but have not been explored under the frame-
work of Faster R-CNN. Throughout this paper, we build              3.2. Adaptations
our networks based on the VGG-16 architecture [47],                Default setting. By default, we mainly follow the origi-
and initialize the networks with weights pre-trained on            nal Faster R-CNN [4] built upon VGG-16 model but add
the ImageNet dataset [48]. Since the models in [18] is             minor modifications as follows. Since we aim to detect
not well adapted for pedestrian detection, here we ex-             standing persons, the anchor ratio of 0.5 is discarded to
plore several potential adaptations and point out the key          facilitate the training and testing speed, as is done in
adaptations benefiting the detection performance. The              [18]. For preparing the training data, we follow [18]
aim of the experiments is not only to seek the upper               to filter the pedestrian instances by excluding occluded
limits of detection performance of these vanilla archi-            or truncated ones as well as small instances with the
tectures, but also to reveal their common limitations and          height smaller than 50 pixels, resulting in 7,095 training
to guide our further improvements.                                 images with a total of 12,790 valid instances. During
                                                                   training, we adopt the image-centric training scheme
3.1. Architectures                                                 and use a minibatch consisting 1 image and 120 ran-
Input Fusion simply stacks color and thermal images                domly sampled anchors, with the ratio of positive and
before feeding them into the network. It is the most               negative ones 1:5 [8]. We start training with a learning
direct extension of Faster R-CNN from single color                 rate of 0.001, divide it by 10 after 4 epochs, and termi-
modality to color-thermal multi-modality, since only the           nate training after 6 epochs.
first convolutional layer needs to be modified due to the          Finer feature stride. In the default setting, the VGG-
increasing of input channels.                                      16 model has a feature stride of 16 pixels, which is too
Early Fusion integrates color and thermal sub-                     coarse especially for those small pedestrian instances.
networks right after the first convolutional block, by first       To better handle small objects, we remove the last max-
concatenating the feature maps from both sub-networks              pooling layer, providing a finer feature stride of 8 pixels.
and a subsequent Network-in-Network (NIN) [49] for                 Input up-sampling. Up-sampling the input images is
dimension reduction. Thus, layers after fusion point can           another strategy to handle coarse feature stride in the
also benefit from pre-trained VGG-16 initialization.               default setting. Here, we simply up-sample the input
Halfway Fusion combines color and thermal sub-                     image by a factor of 2.
networks at a later stage, immediately after the fourth            Include occluded instances. The default pedestrian
convolutional block, via similar feature map concatena-            instances for training only include non-occluded ones.
tion and NIN based dimension reduction.                            However, the reasonable configuration we use for
                                                               4
                                                                                            detection
                                                                                     fc7                                                                                    detection
                               detection
                        fc7                                                          fc6                                                                             merge

                        fc6                                                   roi pooling                        proposal                                fc7_c                      fc7_t
                  roi pooling                                                    conv5                     conv-rpn
                                                   proposal                                                                                              fc6_c                      fc6_t
                       conv5                  conv-rpn                           NIN
                                                                                                                            proposal                 roi pooling                  roi pooling                 proposal
                       conv4                                                    concat
                                                                                                                                 conv-rpn_c             conv5_c                    conv5_t               conv-rpn_t
                       conv3
                                                                    conv4_c                  conv4_t                                                    conv4_c                    conv4_t
                       conv2
                                                                    conv3_c                  conv3_t                                                    conv3_c                    conv3_t
                       conv1
                                                                    conv2_c                  conv2_t                                                    conv2_c                    conv2_t
                       concat
                                                                    conv1_c                  conv1_t                                                    conv1_c                    conv1_t
                                                                                                                                                                                   conv2_t
         color image          thermal image                       color image              thermal image                                             color image               thermal image

                       (a)                                                                 (c)                                                                          (e)

                               detection
                        fc7                                                                                                                                      detection
                                                                                 detection                                                                  merge
                        fc6
                                                                            concat
                  roi pooling                      proposal     fc7_c                       fc7_t                                               fc7_c                 fc7_t
                       conv5                  conv-rpn
                                                                fc6_c                       fc6_t                     proposal                  fc6_c                 fc6_t                         proposal
                       conv4
                                                              roi pooling             roi pooling                conv-rpn                     roi pooling           roi pooling              conv-rpn
                       conv3
                                                               conv5_c                     conv5_t                concat                       conv5_c               conv5_t                    concat
                       conv2
                                                               conv4_c                     conv4_t                                             conv4_c               conv4_t
                       NIN
                                                               conv3_c                     conv3_t                                             conv3_c               conv3_t
                       concat
                                                               conv2_c                     conv2_t                                             conv2_c               conv2_t
          conv1_c               conv1_t                        conv1_c                     conv1_t                                             conv1_c               conv1_t
         color image          thermal image                   color image            thermal image                                            color image         thermal image

                       (b)                                                            (d)                                                                             (f)

Figure 2: We compare six fusion architectures which integrate color and thermal modalities at different stages: (a) Input Fusion, (b) Early Fusion
(c) Halfway Fusion (d) Late Fusion (e) Score Fusion I (f) Score Fusion II. For more details, please refer to Section 3.1.

testing consists of both non-occluded and partially-                                                                  annotations, we find the visible and FIR images are not
occluded pedestrian instances. As an adaptation, we                                                                   well aligned. The disparity is particularly noticeable
include partially-occluded instances in training data,                                                                for small pedestrian instances. Thus we use KAIST for
which gives 7,601 training images with 14,911 pedes-                                                                  analysis in this paper.
trian instances.                                                                                                         The KAIST benchmark consists of 95,328 color-
Ignore region handling. In the KAIST annotations,                                                                     thermal image pairs recorded via a color and a thermal
there are bounding boxes labelled as person? and peo-                                                                 cameras mounted on the rooftop of a car at a equal frame
ple, which are areas that containing undistinguishable                                                                rate of 20 fps. The spatial alignment between the two
pedestrians and where a human annotator cannot deter-                                                                 cameras is ensured by a beam splitter and a later cam-
mine if a person is present or not. Additionally, since we                                                            era calibration process. The manual annotations amount
only use pedestrian instances with a minimum height of                                                                to a total of 103,128 bounding boxes covering 1,182
50 pixels for training, smaller instances are neglected                                                               unique pedestrians. Detection methods are evaluated on
and might be confused as hard negatives. We make sure                                                                 a test set consisting of 2,252 images sampled every 20th
that these areas are not sampled during training.                                                                     frame from videos, among which 1,455 images are cap-
                                                                                                                      tured during daytime and the other 797 images during
3.3. Multispectral pedestrian detection benchmark                                                                     nighttime. The initial procedure for training is to sam-
   To the best of our knowledge, KAIST Multispec-                                                                     ple every 20th video frame [12]. Recent method [18, 19]
tral Pedestrian Benchmark [12] is the only pedestrian                                                                 used a finer sampling skip of every 2nd frame to benefit
dataset that provide large-scale aligned visible and far                                                              from more training data, which will be adopted in this
infrared (FIR, also known as thermal) images with man-                                                                work.
ual annotations. It should be mentioned that the newly                                                                   As for evaluation, the miss rate (MR) averaged over
published CVC-14 [14] is also a multimodal dataset                                                                    the range of [10−2 , 100 ] false positives per image (FPPI)
containing visible-FIR image pairs. However, when we                                                                  is taken as the measure of each detection accuracy. The
visualize the images and the corresponding pedestrian                                                                 curves of FPPI vs. MR are plotted by the provided eval-
                                                                                                             5
uation toolbox.                                                   18.43% respectively. The spatial correspondence is lost
   We perform experiments under reasonable configura-             when fusing the two sub-networks at fully-connected
tion [12]. The original annotations contain some prob-            layer, which could lead to the slightly inferior perfor-
lematic bounding boxes. Recently, improved annota-                mance of Late Fusion. For Score Fusion II, lack of cas-
tions were published by Liu et al. [50]. In this paper,           cade stage or enough supervision, may explain its infe-
we report the experimental results on both original and           rior performance, compared with Score Fusion I. Input
improved annotations for more comprehensive compar-               Fusion and Early Fusion obtain the worst performance,
ison. We denote them as MRO and MRI for brevity,                  probably due to the lack of semantic information. As
where O and I stands for “original annotations” and               of writing, the current best performance on KAIST is
“improved annotations” respectively.                              RPN+BF [19], with 16.53% in MRI , and the adapted
                                                                  Halfway Fusion and Score Fusion I just lag by 1% with-
3.4. Results                                                      out using boosting algorithms or other add-ons.
   The step-by-step comparisons of the detection per-                4. Our last finding is about the complementation be-
formance are manifested in Table 1. From the table, we            tween color and thermal modalities under different illu-
have conclusions / findings as follows.                           mination conditions. As shown in Fig. 4, during day-
   1. MRI is more suitable than MRO to measure the de-            time, the detection performance of color is slightly bet-
tection performances. Compared MRI (using improved                ter than that of thermal. All six fusion architectures ob-
annotations) with MRO (using original annotations), we            tain better results than using a single modality, indicat-
discover that the value of MRI is generally lower than            ing color and thermal information are complementary
that of MRO by around 10% to 15%. The overall rank-               with each other. During nighttime, the performance of
ing trends of the two metrics are consistent when MRI             thermal modality is better than that of color by a large
remains high. However, when MRI goes below 25% or                 margin, due to the invisibility of visual-optical spectrum
so, the metric of MRO seems to lose discrimination, as            at night. Nevertheless, it is surprising that all six archi-
its value oscillates between 30% and 35%. Close ex-               tectures fail to surpass the result of thermal modality,
amination of the original test annotations, we find there         suggesting color images actually cause confusion rather
exist many unlabelled pedestrian instances (see Fig. 3            than offer help for pedestrian detection under bad illu-
for examples). With the improvement of the pedestrian             mination conditions.
detector, those instances not labelled in the original an-
notations are detected which are then regarded as false
negatives when measuring with the original annotations.           4. Illumination-aware Faster R-CNN
This indicates that MRO is no longer suitable to measure
                                                                  4.1. Overall architecture
the detection performance. Thus in the rest of this paper,
we only measure and report the detection performances                Fig. 5 illustrates the overall architecture of the pro-
in terms of MRI .                                                 posed Illumination-aware Faster R-CNN (IAF R-CNN),
   2. After proper adaptation, all six fusion architectures       which is developed based on the Faster R-CNN detec-
gain significant improvements compared with the de-               tion framework [4] and our experimental findings dis-
fault setting, with averagely 10.41% lower in MRI and             cussed in Section 3. IAF R-CNN is composed of three
7.44% lower in MRO . Using finer feature stride or input          parts: the trunk multispectral Faster R-CNN, the side
up-sampling alone obtains approximately 6%, but com-              illumination estimation module, and the final gated fu-
bining both does not show further improvement. Con-               sion layer. A multispectral Faster R-CNN is adopted to
sidering the training and testing speeds, we retain finer         generate separate detections from the color image and
feature stride and switch off input up-sampling. Adding           the thermal image respectively. The illumination esti-
the rest two adaptations gains further 5% improvement             mation module is designed to give an illumination con-
in MRI .                                                          dition measure of the given image. Finally, to enable
   3. Among the six fusion architectures, Halfway Fu-             accurate and robust detection, a gated fusion layer is in-
sion and Score Fusion I outperform others, achieving              troduced to fuse the color and thermal detection results,
17.57% and 17.43% respectively, in terms of MRI . The             which takes the estimated illumination measure into ac-
superior performance of Halfway Fusion may benefit                count.
from its balance between semantic information and low-               We adopt the architecture of Score Fusion II for the
level cue, while that of Score Fusion I could attribute           truck multispectral Faster R-CNN model, but remove
to its cascade design. Late Fusion and Score Fusion II            the original average weighting layer, enabling the out-
are just 1% behind the former two, with 18.89% and                put of this stage to be separate detections from the two
                                                              6
Table 1: Detection performances (in terms of both MRO and MRI ) of six architectures with different adaptation settings. For each setting, we also
report the average performance of all architectures and its improvement from baseline.

            Finer    Input        Include      Ignore
                                                                                    Input      Early    Halfway    Late    Score      Score
           feature    up-         occluded     region    Metric   Color   Thermal                                                               Average      ∆
                                                                                    Fusion     Fusion   Fusion    Fusion   FusionI   FusionII
            stride   scaling      instances   handling

                                                         MRO      49.27   46.16     41.60      42.68    40.90     38.96    39.02     41.56      40.79     0.00
                        Default setting
                                                         MRI      44.57   31.94     31.04      32.79    29.82     27.36    28.11     30.82      29.99     0.00
              √                                          MRO      45.87   43.86     37.70      40.33    34.37     36.08    33.97     36.26      36.45     -4.34
                                                         MRI      39.42   27.50     26.34      29.38    22.03     24.85    21.49     22.50      24.43     -5.56
                       √                                 MRO      47.64   42.65     37.24      38.10    32.77     39.13    35.30     39.28      36.97     -3.82
                                                         MRI      40.98   27.02     23.94      26.79    20.30     24.31    22.67     25.05      23.84     -6.15
              √        √                                 MRO      51.20   42.95     42.16      41.31    36.86     39.35    35.15     39.27      39.02     -1.77
                                                         MRI      43.78   26.41     31.49      28.82    20.09     26.75    20.66     24.96      25.46     -4.53
              √                      √                   MRO      43.78   41.30     35.69      34.35    30.90     33.70    32.48     32.66      33.30     -7.49
                                                         MRI      36.51   23.54     24.79      24.08    19.42     20.32    17.80     19.72      21.02     -8.97
              √                      √           √       MRO      43.08   40.70     34.99      35.84    29.99     33.55    32.68     33.05      33.35     -7.44
                                                         MRI      34.62   22.71     22.47      22.72    17.57     18.89    17.43     18.42      19.58     -10.41

Figure 3: Illustration of the original and improved annotations on KAIST test set. Top: the original annotations. Bottom: our improved annotations.
For the sake of conciseness, we only show color images for daytime scenario and thermal images for nighttime scenario. The original annotations
are relatively coarse and suffer from missing annotation of valid instances.

modalities, in terms of classification confidence scores                                     lumination conditions by Illumination-aware Network
and bounding box coordinates. We choose this fusion                                          (IAN) is the most effective. IAN consists of a chains of
type with following two reasons. Compared with fu-                                           convolutional, fully-connected and max pooling layers,
sion at convolutional level or fully-connected level, fu-                                    taking the color image as input and providing an illu-
sion at score level is more semantic and explicit which                                      mination condition measure. Towards the gated fusion
can be better weighted. Compared with Score Fusion                                           layer, we use a gate function defined over the illumina-
I, Score Fusion II removes the additional cascade stage,                                     tion measure to compute the fusion weights for the two
thus is more concise and straightforward. To improve                                         modalities, which will be used for weighting the detec-
the shortcomings of Score Fusion II, we replace the                                          tion results from the two modalities to obtain the final
weighting scheme and modify the optimization strategy.                                       results. More details of the proposed IAF R-CNN will
Besides, we use pedestrian masks as additional super-                                        be described in the following subsections.
vision following Brazil et al. [51], since they demon-
strated its benefits in color image based pedestrian de-                                     4.2. Illumination Estimation
tection. For implementation, the segmentation module                                            Given an image pair, we estimate the illumination
is simply a single 1 × 1 convolutional layer. We con-                                        conditions from the color image because the thermal im-
sider three different ways to measure illumination con-                                      age is less sensitive to illumination changes. Formally,
ditions given input images, two in a traditional style and                                   illumination estimation can be defined as the mapping
one in a network fashion. We find that predicting il-                                        I → iv, where I denotes an input image and iv ∈ [0, 1]
                                                                                    7
                                                              color                 puted features in the trunk multispectral Faster R-CNN,
                  60                                          thermal
                                                              input fusion          we estimate the illumination value from the color image
                  50                                          early fusion          directly for two reasons. First, the trunk network is pre-
                                                              halfway fusion
                                                              late fusion           trained on image classification task and then fine-tuned
                  40                                          score fusion I
  miss rate (%)

                                                              score fusion II       on object detection task, however, models in both tasks
                  30                                                                are adapted to be invariant to illumination changes. An-
                                                                                    other reason is that we adopts the “image-centric” sam-
                  20                                                                pling strategy in training, while learning the illumina-
                                                                                    tion estimation requires large mini-batch to ensure con-
                  10
                                                                                    vergence.
                   0 reasonable-all   reasonable-day   reasonable-night                We experimentally determine that IAN is the most
                                                                                    effective method for illumination estimation (see Sec-
Figure 4: Comparison of six fusion architectures as well as color                   tion 5.3 for details), which will be adopted in our final
or thermal modality alone under three test configurations, i.e.,                    pipeline.
reasonable-all, reasonable-day and reasonable-night, in terms of MRI .

                                                                                    4.3. Gated fusion
represents an illumination value. It is a non-trival task                              The gated fusion layer is introduced to effectively
since illumination condition is an ambiguous concept                                combine color and thermal for pedestrian detection. An
and the ground-truth illumination labels are not avail-                             illumination-aware weighting mechanism is designed to
able in the pedestrian dataset. We consider three differ-                           generate fusion weights for color and thermal modali-
ent illumination measures in our experiment.                                        ties according to the illumination conditions. As dis-
   Key & Range. According to Kopf et al. [52], the                                  cussed in Section 3.4, the fusion weights for color and
luminance characteristics of an image can be measured                               thermal modalities should satisfy the following con-
by its Key (average luminance) and Range. Specifically,                             straints. Under good illumination conditions, the weight
we determine the key as the average pixel value in an                               for color sub-network should be high while the weight
image, while the range is the difference between the 90th                           for thermal sub-network should not be too small, so
and 10th pixel value percentiles. Finally the Key and the                           that the final detection results would benefit from both
Range are normalized to the interval [0, 1].                                        modalities. Conversely, under bad illumination condi-
   The distribution of the Key and the Range in the                                 tions, the weight for the thermal sub-network is sup-
KAIST train set is illustrated in Fig. 6. We can observed                           posed to be dominant while that for the color sub-
that nighttime images generally have relative smaller                               network is supposed to be insignificant, because color
values than daytime images for both the Key and the                                 images provide more interference than help. With these
Range, but there exist certain overlaps between daytime                             observations in mind, we carefully design a gate func-
and nighttime images with regard to these two mea-                                  tion defined over the estimated illumination value iv ∈
sures.                                                                              [0, 1] as follows.
   IAN. We also consider introducing a network, de-
noted IAN, to estimate the illumination conditions.                                                               iv
                                                                                                      w=                                      (1)
Since there is no ground-truth labels in the dataset, we                                                   1 + αexp(− iv−0.5
                                                                                                                         β )
use the coarse day/night labels instead to train IAN.
   The input color image is resized to 56 × 56 pixels to                            where α and β are two learnable parameters. We term
facilitate training and testing efficiency. IAN consists                            wcolor = w and wthermal = 1 − w as the weights for fus-
of two convolutional layers with 3 × 3 filters, each of                             ing the two modalities, where wcolor and wthermal indi-
which followed by a ReLU layer and a 2×2 max pooling                                cate how confidently we can rely on color and thermal
layer, and two subsequent fully-connected layers with                               respectively to predict the occurrence of pedestrian in-
256 and 2 neurons respectively. A dropout layer with                                stances in the given image.
a ratio of 0.5 is inserted after the first fully-connected                             Recall that each sub-network generates two outputs:
layer to alleviate over-fitting. The network is trained by                          confidence score s = (s0 , . . . , sK ) over K+1 categories
minimizing the softmax loss between the prediction and                              and bounding-box regression offsets t = (t1 , . . . , tK ) for
the label, and the softmax score of day category is used                            each of K object categories. Thus, given scolor and tcolor
as the output illumination value.                                                   from color sub-network and sthermal and tthermal from
   It should be noted that rather than reusing the com-                             thermal sub-network, we obtain the final detection re-
                                                                                8
                                                                    Illumination-aware Network

                                                                                                                              Illumination-
                                                                                                                             aware Weighting          Weight_c
                                                                                                    Illumination
                                                                                                        Value
                                                                                                                                                      Weight_t

                                                                     Segmentation

                                           VGG-16 conv1-5
                                                                                                                              Segmentation
              color image
                                                                                                                                               cls_score_c
                                                                                                                     roi
                                                                                                                   pooling

                                                                                                                                               bbox_pred_t
                                                                                       RPN                                                                       cls_score

                                                                                      Module
                                           VGG-16 conv1-5
                                                                                                                                               cls_score_t       bbox_pred
              thermal image

                                                                                                                     roi                       bbox_pred_t
                                                                                                                   pooling

                                                                                                                              Segmentation

                                                                  Segmentation

Figure 5: The architecture of the proposed IAF R-CNN. Two sub-networks takes color image and thermal image respectively as input and generate
separate detections in terms of classification confidence scores and bounding box coordinates. Meanwhile, in a side branch, an illumination-aware
network is used to estimate the illumination value from the given color image, followed by an illumination-aware weighting layer to compute the
fusion weights for the two modalities via a gate function defined over the estimated illumination value. The final detection results are obtained by
weighting the results of the two sub-networks using the computed fusion weights. Purple boxes denote segmentation layers, which are only used
during training stage. Best viewed in color.

        1.0                                                            day               4.4. Optimization
                                                                       night
                                                                                            The training procedure of IAF R-CNN consists of
        0.8                                                                              two main phases. In the first phase, we only train the
                                                                                         trunk Faster R-CNN by minimizing the following joint
        0.6                                                                              loss function with seven terms:
range

                                                                                             L =λ1 Lrpn + λ2 Lcolor
                                                                                                              dn + λ3 Ldn
                                                                                                                       thermal
        0.4                                                                                                                                                                  (4)
                                                                                                 +λ4 Lcolor
                                                                                                      seg + λ5 L seg
                                                                                                                thermal
                                                                                                                        + λ6 Lcolor
                                                                                                                              segroi + λ7 L segroi
                                                                                                                                           thermal

        0.2                                                                              where Lrpn is the proposal loss, Lcolor       and Lthermal  are
                                                                                                                                dn            dn
                                                                                         the detection losses of color and thermal sub-networks
        0.0                                                                              respectively. The formulation of proposal loss and de-
              0.0             0.2   0.4          0.6        0.8            1.0           tection loss remain the same as Faster R-CNN [4].
                                          key
                                                                                            Following [51], we also introduce two kinds of per-
Figure 6: Distribution of key and range on KAIST train set, sampled                      son segmentation loss in the joint loss function. Lcolor   seg
every 20th frame.                                                                        and Lthermal  are the image-level per-pixel loss. Let G x,y ,
                                                                                                 seg
                                                                                         P x,y respectively be the ground-truth and predicted seg-
                                                                                         mentation masks, the image-level per-pixel loss is de-
sults as                                                                                 fined as:
                                                                                                                  1 X
              s f inal = wcolor × scolor + wthermal × sthermal                 (2)                     L seg =              l(G x,y , P x,y )        (5)
                                                                                                                H × W (x,y)

                                                                                         where H and W are the size of the feature map and l is
               t f inal = wcolor × tcolor + wthermal × tthermal                (3)       the cross-entropy loss function. Lcolor       thermal
                                                                                                                           segroi and L segroi are

                                                                                     9
the roi-level per-pixel loss. Let G x,y,c , P x,y,c respectively          during daytime our approach obtains the best perfor-
represent the ground-truth and predicted segmentation                     mance, while during nighttime using thermal modality
masks of the cth roi, the roi-level per-pixel loss can be                 alone provide the lowest log-average miss rate and our
computed as:                                                              approach as well as RPN+BF [19] have a similar perfor-
                                                                          mance of around 18.2% just second to that of thermal.
                         1      X
        L segroi =                     l(G x,y,c , P x,y,c )   (6)           Table 2 illustrates the computational cost of our
                     H × W × C (x,y,c)                                    method compared to the state-of-the-art methods. It can
                                                                          be observed that the proposed IAF R-CNN is also time-
where C is the number of rois and other notations re-                     efficient during inference stage, with only 0.21s/image.
main the same as L seg . In our experiments, we set all
λi = 1.                                                                   5.3. Ablation studies
   In the second phase, we optimize the weighting pa-
rameter in the gated function by minimizing the loss                      5.3.1. Illumination-aware weighting
                 f inal         f inal
function L = Ldn        where Ldn      is the detection loss                 To demonstrate the effectiveness of “illumination-
defined over the final detections. In this phase, we only                 aware weighting”, we compare it with other weighting
propagate back to the gated fusion layer, since full back-                mechanisms, namely “average weighting” and “hard 0-
propagation does not make further improvement.                            1 weighting”. For average weighting, we merge the de-
                                                                          tections from both sub-networks with equal weights of
                                                                          0.5, while for hard 0-1 weighting, we directly adopt the
5. Experiments                                                            detections from color sub-network when the illumina-
                                                                          tion value is larger than 0.5, otherwise the opposite. We
5.1. Implementation details                                               also test the three illumination estimation methods, i.e,
   Our framework is implemented under Tensorflow                          Key, Range and IAN.
[53]. For training IAN, we use the color images from                         Fig. 8 illustrates the comparison of the three weight-
the training set of KAIST dataset. The network is                         ing mechanisms as well as three illumination estima-
initialized with random Gaussian distribution and is                      tion methods. It can be observed that the results using
trained by Adam solver for 2 epochs with a learning                       Key or Range as illumination measure under-perform
rate of 0.0001 and a batch size of 64. No data augmen-                    that using IAN. We believe the reason is that outdoor
tation is used during the training. For optimizing the                    scenes contain complex and challenging backgrounds,
parameters in the trunk multispectral Faster R-CNN we                     which can not be straightforward handled by pixel value
use exactly the identical training schedule and hyper-                    statistics. Although the training procedure of IAN only
parameters as we described in Section 3 for the sake of                   makes use of day/night labels, IAN is able to learn the
comparison purpose. For optimizing the parameters in                      distinctive characteristic between daytime and night-
the gated function, we start training with a learning rate                time. If provided more rich illumination labels, the de-
of 0.01, divide it by 10 after 2 epochs, and terminate                    tection performance can be further boosted. Using IAN
training after 3 epochs. We set the initial values of pa-                 as the illumination estimator, the result of the proposed
rameter α and β in Eq. 1 to 0.1 and 1 respectively.                       illumination-aware weighting outperforms that of aver-
                                                                          age weighting by 0.67% and outperforms that of hard
5.2. Comparison with state-of-the-arts                                    0-1 weighting by 5.03%, in terms of MRI . It indicates
   We train our model on the KAIST training set and                       that the proposed illumination-aware weighting mecha-
evaluate it on the KAIST testing set. We compare the                      nism can effectively merge the detections from the two
proposed approach with other published approaches,                        sub-networks according to the illumination conditions
in terms of MRI under reasonable configuration [12].                      and is robust to the illumination changes of the given
ROC curves are presented in Fig. 7, where we com-                         images.
pare our approach with [12, 18, 19] as well as the ar-
chitectures we discussed in Section 3. The authors of                     5.3.2. Visualization of Illumination-aware Fusion
[12, 18, 19] provide their codes or detections, so we re-                    Some examples with regard to the illumination-aware
evaluate and report their detection performances on the                   weighting mechanism is illustrated in Fig. 9 (a) and
improved test annotations using the toolbox provided by                   the automatically optimized gated function is plotted
KAIST dataset. It can be observed that IAF R-CNN                          in Fig. 9 (b). It can be observed that the proposed
outperforms all these methods and achieves the lowest                     illumination-aware weighting mechanism can adap-
MRI of 15.73%. From the figure we can observe that                        tively choose weights for the color and thermal network
                                                                     10
                                                                                                                    1
             1                                                                                                                                                                                    1
                                                                                                               .80
            .80                                                                                                                                                                                  .80
                                                                                                               .64
            .64                                                                                                                                                                                  .64
                                                                                                               .50
            .50                                                                                                                                                                                  .50
                                                                                                               .40
            .40                                                                                                                                                                                  .40
                                                                                                               .30
            .30                                                                                                                                                                                  .30

                                                                                                   miss rate

                                                                                                                                                                                     miss rate
miss rate

                                                                                                               .20      23.53% Color
            .20                 34.62% Color                                                                            25.65% Thermal                                                           .20   58.81% Color
                                22.71% Thermal                                                                          20.07% Input Fusion                                                            16.79% Thermal
                                22.47% Input Fusion                                                                     19.55% Early Fusion                                                            27.74% Input Fusion
                                22.72% Early Fusion                                                                     16.61% Halfway Fusion                                                          30.20% Early Fusion
                                17.57% Halfway Fusion                                                          .10      16.60% Late Fusion                                                             20.81% Halfway Fusion
            .10                 18.89% Late Fusion                                                                                                                                               .10
                                                                                                                        14.96% Score Fusion I                                                          23.57% Late Fusion
                                17.43% Score Fusion I                                                                   15.34% Score Fusion II                                                         22.15% Score Fusion I
                                18.42% Score Fusion II                                                                  14.55% IAF R−CNN                                                               24.98% Score Fusion II
                                15.73% IAF R−CNN                                                                        42.44% ACF+T+THOG                                                              18.26% IAF R−CNN
                                47.24% ACF+T+THOG                                                              .05                                                                                     56.17% ACF+T+THOG
            .05                                                                                                         24.85% Halfway Fusion                                                    .05
                                26.15% Halfway Fusion                                                                   16.39% Fusion RPN+BF                                                           27.59% Halfway Fusion
                                16.53% Fusion RPN+BF                                                                                                                                                   18.16% Fusion RPN+BF
                                    −3             −2            −1               0            1                         −3             −2             −1              0         1                      −3             −2             −1               0    1
                                10              10             10                10          10                         10            10             10            10           10                     10            10             10                10   10
                                                     false positives per image                                                             false positives per image                                                      false positives per image

                                         (a) Reasonable all                                                                        (b) Reasonable day                                                        (c) Reasonable night

                                                               Figure 7: Comparison of detection results (MRI ) reported on the test set of KAIST dataset.

                                                        Methods              Choi et al.[17]                   Park et al. [35]        Halfway Fusion [18]                 Fusion RPN+BF [19]                 IAF R-CNN
                                                        Time (s.)                2.73                               0.58                      0.43                                 0.80                          0.21

                                                                Table 2: Comparison of computation time using a NVIDIA GeForce GTX TITAN X GPU.

                               1

                              .80
                                                                                                                                                     rectangles depict the ground-truth bounding boxes and
                              .64                                                                                                                    the predicted bounding boxes respectively. Detection
                              .50                                                                                                                    results with FPPI 1 are presented. We can observe that
                              .40
                                                                                                                                                     IAF R-CNN can obtain superior detection results than
                              .30
                                                                                                                                                     ACF+T+THOG, Halfway Fusion Faster R-CNN and
                  miss rate

                              .20
                                                                                                                                                     Fusion RPN+BF in some challenging cases under dif-
                                                                                                                                                     ferent illumination situations.
                              .10
                                           15.73% Illumination−aware weighting (IAN)
                                           21.24% Illumination−aware weighting (Key)
                                           17.99% Illumination−aware weighting (Range)
                                                                                                                                                     6. Conclusion
                                           16.40% Average weighting
                              .05          20.76% Hard 0−1 weighting (IAN)
                                           27.82% Hard 0−1 weighting (Key)
                                           26.31% Hard 0−1 weighting (Range)                                                                            In this paper, we target the problem of multispectral
                                           10
                                              −3
                                                                10
                                                                    −2                 −1
                                                                                      10                  10
                                                                                                                0              1
                                                                                                                              10                     pedestrian detection via convnets and make improve-
                                                                         false positives per image
                                                                                                                                                     ments in two aspects. First, we revisit several multi-
Figure 8: Comparison of detection performances (reasonable-all,                                                                                      spectral Faster R-CNN architectures and show that once
MRI ) with different weighting mechanisms: average weighting, hard                                                                                   properly adapted, these architectures can obtain promis-
0-1 weighting and illumination-aware weighting as well as illumina-                                                                                  ing improvements, some of which even achieve state-
tion estimation methods Key, Range and IAN.
                                                                                                                                                     of-the-art performance on KAIST dataset. Second, we
                                                                                                                                                     propose a novel Illumination-aware Faster R-CNN (IAF
fusion, according to the estimated illumination value                                                                                                R-CNN) architecture which incorporates a color sub-
generated by the IAN.                                                                                                                                network and a thermal sub-network into a unified frame-
                                                                                                                                                     work by taking illumination conditions into considera-
                                                                                                                                                     tion. An illumination-aware weighting mechanism is in-
5.3.3. Visualization of detection results                                                                                                            troduced to adaptively weight the detection confidence
   To further demonstrate the effectiveness of the pro-                                                                                              of two modalities according to the illumination measure
posed IAF R-CNN, we illustrate several detection sam-                                                                                                and adaptively merge the two sub-networks to obtain fi-
ples in Fig. 10. Two samples are daytime images and the                                                                                              nal detections. Experimental results have demonstrated
other two are nighttime images. The first column illus-                                                                                              that the proposed IAF R-CNN is robust to different il-
trates the input pair images and the rest three columns                                                                                              lumination conditions and outperforms all existing ap-
illustrate the detection results of ACF+T+THOG [12],                                                                                                 proaches on challenging KAIST dataset. In the future,
Halfway Fusion Faster R-CNN [18], Fusion RPN + BF                                                                                                    we plan to further improve the robustness of our ap-
[19] and IAF R-CNN. The red rectangles and the green                                                                                                 proach by fusing lidar data with multispectral images.
                                                                                                                                             11
                          Illumination value                             Illumination value                         Illumination value
                IAN            0.000001                        IAN                                         IAN                                                               0.7
                                                                              0.669010                                   0.914047

                                                                                                                                         Fusion weight (color sub−network)
                                                                                                                                                                             0.6

                                                                                                                                                                             0.5

                                                                                                                                                                             0.4

                                                                                                                                                                             0.3
                            Detections                                     Detections                                 Detections
                                                                                                                                                                             0.2

                                                                                                                                                                             0.1

                                                                                                                                                                              0
                                                                                                                                                                                   0   0.1   0.2   0.3   0.4   0.5   0.6   0.7   0.8   0.9   1
                                                                                                                                                                                                     Illumiantion value

                                                          (a) Examples                                                                                                                       (b) Gated function

                                               Figure 9: Illustration of illumination-aware examples and gated function.

Acknowledgements                                                                              [12] S. Hwang, J. Park, N. Kim, Y. Choi, I. So Kweon, Multispec-
                                                                                                   tral pedestrian detection: Benchmark dataset and baseline, in:
  The research is supported in part by NSFC                                                        Proceedings of the IEEE Conference on Computer Vision and
                                                                                                   Pattern Recognition, 2015.
(61572424) and the Science and Technology Depart-                                             [13] C.-F. Lin, C.-S. Chen, W.-J. Hwang, C.-Y. Chen, C.-H. Hwang,
ment of Zhejiang Province (2018C01080). Min Tang is                                                C.-L. Chang, Novel outline features for pedestrian detection sys-
supported in part by NSFC (61572423,61732015) and                                                  tem with thermal images, Pattern Recognition 48 (11) (2015)
                                                                                                   3440–3450.
Zhejiang Provincial NSFC (LZ16F020003).
                                                                                              [14] A. González, Z. Fang, Y. Socarras, J. Serrat, D. Vázquez, J. Xu,
                                                                                                   A. M. López, Pedestrian detection at day/night time with visible
                                                                                                   and fir cameras: A comparison, Sensors 16 (6) (2016) 820.
References                                                                                    [15] T. Kim, S. Kim, Pedestrian detection at night time in fir domain:
                                                                                                   Comprehensive study about temperature and brightness and new
 [1] R. Benenson, M. Omran, J. Hosang, B. Schiele, Ten years of                                    benchmark, Pattern Recognition 79 (2018) 44–54.
     pedestrian detection, what have we learned?, arXiv preprint                              [16] J. Wagner, V. Fischer, M. Herman, S. Behnke, Multispectral
     arXiv:1411.4304.                                                                              pedestrian detection using deep fusion convolutional neural net-
 [2] D. T. Nguyen, W. Li, P. O. Ogunbona, Human detection from                                     works, in: Proceeding of the European Symposium on Artifi-
     images and videos: A survey, Pattern Recognition 51 (2016)                                    cial Neural Networks, Computational Intelligence and Machine
     148–175.                                                                                      Learning, 2016.
 [3] P. Dollar, C. Wojek, B. Schiele, P. Perona, Pedestrian detection:                        [17] H. Choi, S. Kim, K. Park, K. Sohn, Multi-spectral pedestrian
     An evaluation of the state of the art, IEEE Transactions on Pat-                              detection based on accumulated object proposal with fully con-
     tern Analysis and Machine Intelligence 34 (4) (2012) 743–761.                                 volutional networks, in: Proceeding of the International Confer-
 [4] S. Ren, K. He, R. Girshick, J. Sun, Faster r-cnn: Towards                                     ence on Pattern Recognition, 2016.
     real-time object detection with region proposal networks, IEEE                           [18] S. W. Jingjing Liu, Shaoting Zhang, D. Metaxas, Multispectral
     Transactions on Pattern Analysis and Machine Intelligence                                     deep neural networks for pedestrian detection, in: Proceedings
     39 (6) (2017) 1137–1149.                                                                      of the British Machine Vision Conference, 2016.
 [5] J. Hosang, M. Omran, R. Benenson, B. Schiele, Taking a deeper                            [19] D. König, M. Adam, C. Jarvers, G. Layher, H. Neumann,
     look at pedestrians, in: Proceedings of the IEEE Conference on                                M. Teutsch, Fully convolutional region proposal networks for
     Computer Vision and Pattern Recognition, 2015.                                                multispectral person detection, in: Proceedings of the IEEE
 [6] S. Zhang, R. Benenson, M. Omran, J. Hosang, B. Schiele, How                                   Conference on Computer Vision and Pattern Recognition Work-
     far are we from solving pedestrian detection?, in: Proceeding of                              shops, 2017.
     the IEEE Conference on Computer Vision and Pattern Recogni-                              [20] Y. Tian, P. Luo, X. Wang, X. Tang, Deep learning strong parts
     tion, 2016.                                                                                   for pedestrian detection, in: Proceedings of the IEEE Interna-
 [7] J. Li, X. Liang, S. Shen, T. Xu, J. Feng, S. Yan, Scale-aware fast                            tional Conference on Computer Vision, 2015.
     r-cnn for pedestrian detection, arXiv preprint arXiv:1510.08160.                         [21] Y. Tian, P. Luo, X. Wang, X. Tang, Pedestrian detection aided
 [8] L. Zhang, L. Lin, X. Liang, K. He, Is faster r-cnn doing well for                             by deep learning semantic tasks, in: Proceedings of the IEEE
     pedestrian detection?, in: Proceeding of the European Confer-                                 Conference on Computer Vision and Pattern Recognition, 2015.
     ence on Computer Vision, 2016.                                                           [22] D. Ribeiro, J. C. Nascimento, A. Bernardino, G. Carneiro, Im-
 [9] S. Zhang, R. Benenson, B. Schiele, Citypersons: A diverse                                     proving the performance of pedestrian detectors using convolu-
     dataset for pedestrian detection, in: Proceeding of the IEEE                                  tional learning, Pattern Recognition 61 (2017) 641–649.
     Conference on Computer Vision and Pattern Recognition, 2017.                             [23] R. Girshick, J. Donahue, T. Darrell, J. Malik, Rich feature hier-
[10] Z. Cai, Q. Fan, R. S. Feris, N. Vasconcelos, A unified multi-scale                            archies for accurate object detection and semantic segmentation,
     deep convolutional neural network for fast object detection, in:                              in: Proceedings of the IEEE conference on Computer Vision and
     Proceeding of the European Conference on Computer Vision,                                     Pattern Recognition, 2014.
     2016.                                                                                    [24] P. Dollar, Z. Tu, P. Perona, S. Belongie, Integral channel fea-
[11] X. Du, M. El-Khamy, J. Lee, L. Davis, Fused dnn: A deep neural                                tures, in: Proceedings of the British Machine Vision Confer-
     network fusion approach to fast and robust pedestrian detection,                              ence, 2009.
     in: Proceeding of the IEEE Winter Conference on Applications                             [25] P. Dollár, R. Appel, S. Belongie, P. Perona, Fast feature pyra-
     of Computer Vision, 2017.

                                                                                        12
     mids for object detection, IEEE Transactions on Pattern Analy-                 Convolutional-recursive deep learning for 3d object classifica-
     sis and Machine Intelligence 36 (8) (2014) 1532–1545.                          tion, in: Proceedings of the Advances in Neural Information
[26] W. Nam, P. Dollár, J. H. Han, Local decorrelation for improved                Processing Systems, 2012.
     pedestrian detection, in: Proceedings of the Advances in Neural           [45] S. Gupta, R. Girshick, P. Arbeláez, J. Malik, Learning rich fea-
     Information Processing Systems, 2014.                                          tures from rgb-d images for object detection and segmentation,
[27] R. Benenson, M. Mathias, T. Tuytelaars, L. Van Gool, Seeking                   in: Proceedings of the European Conference on Computer Vi-
     the strongest rigid detector, in: Proceedings of the IEEE Confer-              sion, 2014.
     ence on Computer Vision and Pattern Recognition, 2013.                    [46] R. Girshick, Fast r-cnn, in: Proceedings of the IEEE Interna-
[28] P. Sermanet, K. Kavukcuoglu, S. Chintala, Y. LeCun, Pedes-                     tional Conference on Computer Vision, 2015.
     trian detection with unsupervised multi-stage feature learning,           [47] K. Simonyan, A. Zisserman, Very deep convolutional net-
     in: Proceedings of the IEEE Conference on Computer Vision                      works for large-scale image recognition, arXiv preprint
     and Pattern Recognition, 2013.                                                 arXiv:1409.1556.
[29] A. Angelova, A. Krizhevsky, V. Vanhoucke, A. S. Ogale, D. Fer-            [48] A. Krizhevsky, I. Sutskever, G. E. Hinton, Imagenet classifi-
     guson, Real-time pedestrian detection with deep network cas-                   cation with deep convolutional neural networks, in: Proceed-
     cades., in: Proceedings of the British Machine Vision Confer-                  ings of the Advances in Neural Information Processing Systems,
     ence, 2015.                                                                    2012.
[30] Q. Hu, P. Wang, C. Shen, A. van den Hengel, F. Porikli,                   [49] M. Lin, Q. Chen, S. Yan, Network in network, arXiv preprint
     Pushing the limits of deep cnns for pedestrian detection, IEEE                 arXiv:1312.4400.
     Transactions on Circuits and Systems for Video Technology-                [50] J. Liu, S. Zhang, S. Wang, D. Metaxas, Improved annotations
     Doi:10.1109/TCSVT.2017.2648850.                                                of test set of kaist, http://paul.rutgers.edu/~jl1322/
[31] Z. Cai, M. Saberian, N. Vasconcelos, Learning complexity-                      multispectral.htm, accessed December 20, 2017.
     aware cascades for deep pedestrian detection, in: Proceedings of          [51] G. Brazil, X. Yin, X. Liu, Illuminating pedestrians via simulta-
     the IEEE International Conference on Computer Vision, 2015.                    neous detection & segmentation, in: Proceedings of the IEEE
[32] X. Wang, T. Xiao, Y. Jiang, S. Shao, J. Sun, C. Shen, Repulsion                Conference on Computer Vision and Pattern Recognition, 2017.
     loss: Detecting pedestrians in a crowd, in: Proceedings of the            [52] J. Kopf, M. Uyttendaele, O. Deussen, M. F. Cohen, Capturing
     IEEE Conference on Computer Vision and Pattern Recognition,                    and viewing gigapixel images, in: ACM Transactions on Graph-
     2018.                                                                          ics, Vol. 26, 2007, p. 93.
[33] S. Zhang, J. Yang, B. Schiele, Occluded pedestrian detection              [53] M. Abadi, A. Agarwal, P. Barham, E. Brevdo, Z. Chen, C. Citro,
     through guided attention in cnns, in: Proceedings of the IEEE                  G. S. Corrado, A. Davis, J. Dean, M. Devin, et al., Tensorflow:
     Conference on Computer Vision and Pattern Recognition, 2018.                   Large-scale machine learning on heterogeneous distributed sys-
[34] X. Dan, W. Ouyang, E. Ricci, X. Wang, N. Sebe, et al., Learn-                  tems, arXiv preprint arXiv:1603.04467.
     ing cross-modal deep representations for robust pedestrian de-
     tection, in: Proceedings of the IEEE Conference on Computer
     Vision and Pattern Recognition, 2017.
[35] K. Park, S. Kim, K. Sohn, Unified multi-spectral pedestrian de-
     tection based on probabilistic fusion networks, Pattern Recogni-
     tion 80 (2018) 143–155.
[36] X. Jin, Q. Jiang, S. Yao, D. Zhou, R. Nie, J. Hai, K. He, A survey
     of infrared and visual image fusion methods, Infrared Physics &
     Technology 85 (2017) 478–501.
[37] J. Ma, Y. Ma, C. Li, Infrared and visible image fusion methods
     and applications: a survey, Information Fusion 45 (2019) 153–
     178.
[38] K. Simonyan, A. Zisserman, Two-stream convolutional net-
     works for action recognition in videos, in: Proceedings of the
     Advances in neural information processing systems, 2014.
[39] A. Karpathy, G. Toderici, S. Shetty, T. Leung, R. Sukthankar,
     L. Fei-Fei, Large-scale video classification with convolutional
     neural networks, in: Proceedings of the IEEE conference on
     Computer Vision and Pattern Recognition, 2014.
[40] C. Feichtenhofer, A. Pinz, A. Zisserman, Convolutional two-
     stream network fusion for video action recognition, in: Proceed-
     ings of the IEEE Conference on Computer Vision and Pattern
     Recognition, 2016.
[41] C. Couprie, C. Farabet, L. Najman, Y. LeCun, Indoor se-
     mantic segmentation using depth information, arXiv preprint
     arXiv:1301.3572.
[42] J. Long, E. Shelhamer, T. Darrell, Fully convolutional networks
     for semantic segmentation, in: Proceedings of the IEEE Confer-
     ence on Computer Vision and Pattern Recognition, 2015.
[43] Y. Cheng, R. Cai, Z. Li, X. Zhao, K. Huang, Locality-sensitive
     deconvolution networks with gated fusion for rgb-d indoor se-
     mantic segmentation, in: Proceedings of the IEEE Conference
     on Computer Vision and Pattern Recognition, 2017.
[44] R. Socher, B. Huval, B. Bath, C. D. Manning, A. Y. Ng,

                                                                          13
Figure 10: Comparison of multispectral pedestrian detection results with other approaches. The first column shows the input pair images with
ground-truth annotations depicted with red rectangles. The rest columns show the detection results (see green rectangles) of ACF+T+THOG [12],
Halfway Fusion Faster R-CNN [18], Fusion RPN + BF [19] and IAF R-CNN respectively. Our IAF R-CNN obtains a better overall detection
accuracy than other three approaches.

                                                                    14
