---
source_id: 104
bibtex_key: zhang2020cfr
title: Multispectral Fusion for Object Detection with Cyclic Fuse-and-Refine Blocks
year: 2020
domain_theme: Pedestrian RGB-T
verified_pdf: 104_Cyclic Fuse-and-Refine (CFR).pdf
char_count: 35191
---

MULTISPECTRAL FUSION FOR OBJECT DETECTION
                                                                     WITH CYCLIC FUSE-AND-REFINE BLOCKS

                                                          Heng ZHANG1,3 , Elisa FROMONT1,4 , Sbastien LEFEVRE2 , Bruno AVIGNON3
                                                     1
                                                         Univ Rennes, IRISA 2 Univ Bretagne Sud, IRISA, 3 ATERMES company,4 IUF, Inria

                                                                 ABSTRACT
arXiv:2009.12664v1 [cs.CV] 26 Sep 2020

                                         Multispectral images (e.g. visible and infrared) may be partic-
                                         ularly useful when detecting objects with the same model in
                                         different environments (e.g. day/night outdoor scenes). To ef-
                                         fectively use the different spectra, the main technical problem
                                         resides in the information fusion process. In this paper, we
                                         propose a new halfway feature fusion method for neural net-
                                         works that leverages the complementary/consistency balance
                                         existing in multispectral features by adding to the network
                                         architecture, a particular module that cyclically fuses and re-
                                         fines each spectral feature. We evaluate the effectiveness of
                                         our fusion method on two challenging multispectral datasets           visible images   visible masks   thermal images   thermal masks

                                         for object detection. Our results show that implementing our
                                         Cyclic Fuse-and-Refine module in any network improves the         Fig. 1. Examples of thermal and RGB images of the same
                                         performance on both datasets compared to other state-of-the-      aligned scenes taken from KAIST multispectral pedestrian
                                         art multispectral object detection methods.                       detection dataset [1] with detected bounding boxes. The seg-
                                                                                                           mentation masks (2nd and 4th columns) are predicted based
                                            Index Terms— Multispectral object detection, Multi-
                                                                                                           on the (mono-)spectral features before any fusion process.
                                         spectral feature fusion, Deep learning

                                                             1. INTRODUCTION                               small, i.e., the multispectral features may be inconsistent.
                                                                                                                In order to augment the consistency between features of
                                         Visible and thermal image channels are expected to be com-        different spectra, we design a novel feature fusion approach
                                         plementary when used for object detection in the same out-        for convolutional neural networks based on Cyclic Fuse-and-
                                         door scenes. In particular, visible images tend to provide        Refine modules. Our main idea is to refine the mono-spectral
                                         color and texture details while thermal images are sensitive to   features with the fused multispectral features multiple times
                                         objects’ temperature, which may be very helpful at night time.    consecutively in the network. Such a fusion scheme has two
                                         However, because they provide a very different view of the        advantages: 1) since the fused features are generally more dis-
                                         same scene, the features extracted from different image spec-     criminative than the spectral ones, the refined spectral features
                                         tra may be inconsistent and lead to a difficult, uncertain and    should also be more discriminative than the original spec-
                                         error-prone fusion (Fig. 1). In this figure, we use a Convo-      tral features and the fuse-and-refine loop gradually improves
                                         lutional Neural Network (CNN, detailed later) to predict two      the overall feature quality; 2) since the mono-spectral fea-
                                         segmentation masks based on the two (aligned) mono-spectral       tures keep being refined with the same features, their consis-
                                         extracted features from the same image and then fuse the fea-     tency progressively increases, along with the decrease of their
                                         tures to detect pedestrians in the dataset. During the train-     complementary, and the consistency/complementary balance
                                         ing phase, the object detection and the semantic segmentation     is achieved by controlling the number of loops.
                                         losses are jointly optimised (the segmentation ground truths           We review the related works on multispectral feature fu-
                                         are generated according to pedestrian bounding box annota-        sion with CNN in Section 2. We detail our novel network
                                         tions). We can observe that most pedestrians are visible either   module named Cyclic Fuse-and-Refine, which loops on the
                                         on the RGB or on the infrared segmentation masks which il-        fuse-and-refine operations to adjust the multispectral features’
                                         lustrates the complementary of the channels. However, even        complementary/consistency balance in Section 3. In Section
                                         though the visible-thermal image pairs are well aligned, the      4, we show experiments on the well known KAIST multispec-
                                         similarity between the two predicted segmentation masks is        tral pedestrian detection dataset [1] on which we obtain new
                                                                                                                                                                    semantic supervision

                                                                       identity                         identity                         identity
                                                            thermal                          thermal                          thermal                          thermal
     thermal      residual
                                                            features                         features                         features                         features
     features                                                                     residual                         residual                         residual
                                                               ft0                              ft1                              ft2                              ft3
                                                                                fused                            fused                            fused
                        fused                                                 features                         features                         features
    concat+conv       features                              concat+conv                      concat+conv                      concat+conv
                                                                                  ff1                              ff2                              ff3
                                                             visible                          visible                          visible                          visible
      visible                                      unfold   features              residual                         residual                         residual
                                                                                             features                         features                         features
     features     residual
                                                               fv0   identity                   fv1   identity                   fv2   identity                   fv3
                             cycling for 3 times
                                                                                                                                                                    semantic supervision

Fig. 2. Illustration (folded on the left part and unfolded on the right) of the proposed Cyclic Fuse-and-Refine Module with 3
loops. Better viewed in color.

state-of-the-art results, and on the less known FLIR ADAS                                      features. An illustration of our Cyclic Fuse-and-Refine mod-
dataset [2] on which we set a first strong baseline.                                           ule with 3 loops in the cycle is presented in Fig. 2.
                                                                                               Fuse-and-Refine. In each loop i, for the fused (f ), visible
                                                                                               (v ) and thermal (t ) features, the multispectral feature fusion
                             2. RELATED WORK
                                                                                               can be formalized as ffi = F(σ(fti−1 , fvi−1 )), where σ is a
                                                                                               feature concatenation operation, and F is a 3 × 3 convolution
Existing approaches mainly differ on the strategies (“when”
                                                                                               followed by a batch normalization operation. For simplicity
and “how”) used to fuse the multispectral features.
                                                                                               and to avoid over-fitting, the operation F in all loops shares
When to fuse. The first study on CNN-based multispectral
                                                                                               weights. The fused features are then assigned as residuals of
pedestrian detection is made by [3], and they evaluate two
                                                                                               the spectral features for refinement: fti = H(fti−1 +ffi ), fvi =
fusion strategies: early and late fusions. Then [4] and [5] ex-
plore this further and show that a fusion of features halfway in                               H(fvi−1 + ffi ). H is the activation function (e.g. ReLU).
the network, achieves better results than the early or the late                                Semantic supervision. In order to prevent the vanishing gra-
fusion. Since then, the halfway fusion has become the de-                                      dient problem when learning the parameters of the network
fault strategy in deep learning-based multispectral (and mul-                                  and to better guide the multispectral feature fusion, an aux-
timodal) works ([5, 6, 7, 8, 9]). We also choose to locate our                                 iliary semantic segmentation task is used to bring separate
fuse-and-refine fusion module halfway in the network.                                          supervision information for each refined spectral features.
How to fuse. Features extracted from each spectral chan-                                       Concretely, after being refined with the fused features, the
nel have different physical properties and choosing how to                                     thermal and visible features go through a 1 × 1 convolution
fuse these complementary information is another central re-                                    (aiming at replacing a fully-connected layer so to ensure a
search topic. Basic fusion methods include element-wise                                        fully-convolutional network) to predict two pedestrian seg-
addition/average, element-wise maximum and concatenation                                       mentation masks, one for each channel. These predicted
sometimes in addition to a 1 × 1 convolution to compress the                                   masks are also used to tune (or at least visualize) the number
number of channels as done e.g. in [10]. Building on this,                                     of loops in the cyclic module according to the complemen-
more advanced methods such as [5] and [6] use illumination                                     tary/consistency variations in the features.
information to guide the multispectral feature fusion. [11]                                    Final fusion. Following [14], since the optimal cycling num-
apply Gated Fusion Units (GFU) [12] to combine two SSD                                         ber is unknown and could be different for different image
networks [13] on color and thermal inputs. [8] propose a                                       pairs, we aggregate all the refined spectral features to gen-
cross-modality interactive attention network to dynamically                                    erate the final fused features that will be used for the object
weight the fusion of thermal/visible features. Our strategy is                                 detection part of the network. The aggregation is a simple
different: we suggest a cyclic fusion scheme to progressively                                  element-wise average function.
                                                                                                                           1
                                                                                                                               PILet I be
                                                                                                                                        Pthe
                                                                                                                                          I
                                                                                                                                              number of loops,
improve the quality of the spectral features and automatically                                 the final computation is: 2I   ( 1 fti + 1 fvi ).
adjust the complementary/consistence balance.
                                                                                                                              4. EXPERIMENTS
                      3. PROPOSED APPROACH
                                                                                               We evaluate the proposed Cyclic Fuse-and-Refine Module
Overview. The fusion and refinement operations are the main                                    on KAIST Multispectral Pedestrian Detection [1] and FLIR
ones of our proposed approach. They are repeated (through a                                    ADAS dataset [2], and compare our results with the state-of-
cycle) multiple times to increase the consistency of the mul-                                  the-art multispectral methods. Examples of image pairs with
tispectral features and to decrease the complementarity of the                                 their ground truth bounding boxes are shown in Fig. 3.
                                                                   object detector [13]. Note that our proposed module is in-
                                                                   dependent from the chosen network architecture. Following
                                                                   [4] and [5], the mono-spectral features are extracted indepen-
                                                                   dently through a VGG16 [16] network, and fused after the
                                                                   conv4 3 layer (halfway through the network). Our baseline
                                                                   architecture uses the element-wise average for the multispec-
                                                                   tral feature fusion and we integrate and evaluate the proposed
                                                                   module with different number of loops.
                                                                   Data augmentation. As implemented in SSD [13] and FSSD
                                                                   [15], a few data augmentation methods are applied, such as
                                                                   image random cropping, padding, flipping and distorting for
                                                                   both visible and thermal images.
                                                                   Anchor designing. Following [17], the anchor designing
Fig. 3. Examples of visible/thermal image pairs with their         strategy is adapted for the pedestrian detection for KAIST
ground truth from the KAIST dataset (in the first line) and        dataset: we fix the aspect ratio of each anchor box to 0.41
from the FLIR dataset in the second and third lines (the           and√we only keep√three detection layers√ with scales 32 and
ground truth annotations are given according to the thermal        32 2, 64 and 64 2, 128 and 128 2 from fine to coarse
images). The third line gives an example of misaligned pairs       respectively. For FLIR, we use the same scale settings but we
in the FLIR dataset. Better viewed in color and zoomed in.         augment the aspect ratio setting to {1, 2, 21 }.
                                                                   Loss functions. To improve object detection, SDS RCNN
                                                                   [18] and MSDS RCNN [7] use an additional task, semantic
4.1. Datasets                                                      segmentation, and jointly optimize the loss for the segmenta-
                                                                   tion and detection tasks while training the network. To fairly
KAIST. We use the processed version of this multispec-             compare our work to these competitors, we also use this aux-
tral pedestrian detection dataset which contains 7,601 color-      iliary loss to supervise the training of the proposed module.
thermal image pairs for training and 2,252 pairs for testing.
We kept the bounding boxes annotated as “person”, “person?”
                                                                   4.3. Comparison with state-of-the-art methods
or “people” as positive pedestrian examples. [7] proposed a
“sanitized” version of the training annotations which elimi-       On KAIST. We compare the experimental results of our ap-
nated some of the annotation errors from the original training     proach with state-of-the-art methods in Table 1. For these ex-
annotations. According to [4], inaccurate annotations in the       periments, we make 3 loops in the Fuse-and-Refine cycle. De-
test set leads to unfair comparisons, so we only use their “san-   pending on what was done in the literature and to allow a fair
itized” testing annotations for our evaluation, with the usual     comparison, we report our detection accuracy with sanitized
“Miss Rate” performance metric under reasonable setting,           and original training annotations respectively. All the deep
i.e., a test subset containing not/partially occluded pedestri-    learning-based methods [4, 19, 5, 6, 7] use the same input im-
ans which are larger than 55 pixels.                               age resolution (640 × 512) and the same backbone network
FLIR. This recently released multispectral (multi-)object de-      (VGG16). The results show that our proposed method allows
tection dataset contains around 10k manually-annotated ther-       us to obtain better detection results than all its competitors for
mal images with their corresponding reference visible images,      both the sanitized and original training annotations. Note that
collected during daytime and nighttime. We only kept the 3         the computational overhead from CFR is quite small. During
more frequent classes which are “bicycle”, “car” and “per-         inference, each cycle only add ∼0.4ms of inference time.
son”. We manually removed the misaligned visible-thermal           On FLIR. Because of the misalignment problems in the
image pairs and ended with 4,129 well-aligned image pairs          dataset, there is, to our knowledge, no paper which uses the
for training and 1,013 image pairs for test 1 . Some exam-         FLIR dataset [2] for multispectral object detection. We use
ples of the well-aligned and misaligned visible-thermal image      our sanitized version of the dataset and compare the mAP
pairs are shown in Figure 3.                                       percentage of two different models: a baseline model which
                                                                   uses the traditional halfway fusion architecture (with the
                                                                   VGG backbone) and the same model with our proposed mod-
4.2. Training details
                                                                   ule. Again, we can see in Table 2 that our method provides
Network architecture. We implemented our Cyclic Fuse-              important mAP gains for all the considered object categories.
and-Refine module on the single stage object detector FSSD
[15], which is an improved version of the well known SSD           4.4. Ablation study
  1 This new aligned dataset can be downloaded here:   http://     We study in details (on the KAIST dataset with the sani-
shorturl.at/ahAY4                                                  tized training annotations and the reasonable test set) the ef-
                                                                                                  Miss Rate (lower, better)
                                                                              Methods
                                                                                                 R-All    R-Day      R-Night
                                                                       Training with sanitized annotations:
                                                                       MSDS-RCNN [7]            7.49%     8.09%      5.92%
                                                                       CFR 3                    6.13%     7.68%      3.19%
                                                                       Training with original annotations:
                                                                       ACF+T+THOG [1]           47.24% 42.44% 56.17%
                                                                       Halfway Fusion [4]       26.15% 24.85% 27.59%
                                                                       Fusion RPN+BF [19] 16.53% 16.39% 18.16%
                                                                       IAF R-CNN [5]            16.22% 13.94% 18.28%
                                                                       IATDNN+IASS [6]          15.78% 15.08% 17.22%
                                                                       MSDS-RCNN [7]            11.63% 10.60% 13.73%
                                                                       CFR 3                    10.05% 9.72%         10.80%

                                                                    Table 1. Detection accuracy comparisons in terms of Miss
                                                                    Rate percentage on KAIST Dataset [1]. Our competitors’ re-
     input images    first refine   second refine    third refine   sults are taken from [5] and [7].

Fig. 4. Examples of pedestrian segmentation masks predicted             Methods       mAP      Bicycle     Car         Person
on 2 visible/thermal image pairs (one taken at day time, one            Baseline     71.17%    56.39%      83.90%     73.28%
taken at night) of the KAIST dataset after a different number           CFR 3        72.39%    57.77%      84.91%     74.49%
of loops (1-3) in the fuse-and-refine cycle.
                                                                    Table 2. mAP results for two CNN object detection archi-
                                                                    tectures which use (or not) our Cyclic Fuse-and-Refine (CFR)
                                                                    blocks on FLIR dataset [2].
fectiveness of the proposed fusion module and the relation-
ship between the number of loops in the fuse-and-refine cy-          Methods       Miss Rate   DICE Scores
cle and the multispectral feature complementary/consistency          Baseline      7.68%       -
balance. The experimental results are summarised in Table            CFR 1         6.90%       {64.53%}
3. We provide the Miss Rate and DICE scores [20] between             CFR 2         6.40%       {78.89%, 89.70%}
the pedestrian masks predicted by each version of the refined        CFR 3         6.13%       {74.60%, 90.60%, 94.17%}
thermal/visible features. These DICE scores are used as an in-       CFR 4         7.09%       {58.25%, 85.91%, 92.9%, 96.11%}
dicator of similarity between the spectral features. From the
table we observe successive accuracy gains from the baseline        Table 3. Miss rates versus DICE scores w.r.t. different num-
(no loop) to 3 loops, and a decrease after 4 loops; meanwhile       bers of Fuse-and-Refine loops. Each experiment is repeated
the value of DICE scores continue to increase along with the        five times and we report the average performance.
number of loops. We then visualize, on two sample image
pairs, the pedestrian masks predicted by visible/thermal fea-
                                                                                         5. CONCLUSION
tures after each refinement in Figure 4. The first column cor-
responds to input images marked with the detected pedestri-         This paper proposes a novel cycle fuse-and-refine module to
ans; The second, third and fourth columns correspond to seg-        improve the multispectral feature fusion while taking into ac-
mentation masks predicted after 1 to 3 loops. The first and         count the complementary/consistency balance of the features.
third lines (resp. second and fourth) are for visible (res. ther-   Experiments on KAIST [1] and FLIR [2] datasets show that
mal) images and their corresponding segmentation masks. It          integrating the proposed fusion module to a “vanilla” multi-
can be observed that the quality and similarity of the masks        spectral pedestrian detector leads to substantial accuracy im-
gradually increase with the number of loops. With the in-           provements. Several visible/thermal image pairs have a mis-
crease of similarity between the spectral features, their con-      alignment problem in FLIR dataset. This problem could be
sistency increases and their complementarity decreases. As          more serious in real world applications due to calibration er-
mentioned in Section 1, the lack of consistency between the         rors or temporal shifts. A Region Feature Alignment (RFA)
multispectral features is harmful; on the contrary, too much        module [21] tackled such a cross-modality disparity problem
consistency leads to sharp emerge/plunge in the feature val-        in a supervised manner and in a two-stage object detection
ues, and makes the fusion meaningless. That explains why            setting. In the future, we would like to explore a more general
the Miss Rate starts to decrease after 4 loops. In practice the     solution to this problem with a similar cyclic-align scheme.
number of loops should be tuned for any dataset but we be-
lieve that very few values should be tried (between 2 and 5).
                    6. REFERENCES                                [11] Yang Zheng, Izzat H. Izzat, and Shahrzad Ziaee, “GFD-
                                                                      SSD: gated fusion double SSD for multispectral pedes-
 [1] Soonmin Hwang, Jaesik Park, Namil Kim, Yukyung                   trian detection,” CoRR, vol. abs/1903.06999, 2019.
     Choi, and In So Kweon, “Multispectral pedestrian de-
     tection: Benchmark dataset and baselines,” in Proceed-      [12] John Edison Arevalo Ovalle, Thamar Solorio,
     ings of IEEE Conference on Computer Vision and Pat-              Manuel Montes y Gmez, and Fabio A. Gonzlez,
     tern Recognition (CVPR), 2015.                                   “Gated multimodal units for information fusion,”
                                                                      CoRR, vol. abs/1702.01992, 2017.
 [2] “Free flir thermal dataset for algorithm train-
     ing,”     https://www.flir.com/oem/adas/                    [13] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Chris-
     adas-dataset-form/.                                              tian Szegedy, Scott E. Reed, Cheng-Yang Fu, and
                                                                      Alexander C. Berg, “SSD: single shot multibox detec-
 [3] Jörg Wagner, Volker Fischer, Michael Herman, and                tor,” in Computer Vision - ECCV 2016 - 14th Euro-
     Sven Behnke, “Multispectral pedestrian detection us-             pean Conference, Amsterdam, The Netherlands, Octo-
     ing deep fusion convolutional neural networks,” in               ber 11-14, 2016, Proceedings, Part I, Bastian Leibe, Jiri
     24th European Symposium on Artificial Neural Net-                Matas, Nicu Sebe, and Max Welling, Eds. 2016, vol.
     works, ESANN 2016, Bruges, Belgium, April 27-29,                 9905 of Lecture Notes in Computer Science, pp. 21–37,
     2016, 2016.                                                      Springer.
 [4] Jingjing Liu, Shaoting Zhang, Shu Wang, and Dim-            [14] Zhiwen Fan, Huafeng Wu, Xueyang Fu, Yue Huang, and
     itris N. Metaxas, “Multispectral deep neural networks            Xinghao Ding, “Residual-guide network for single im-
     for pedestrian detection,” in Proceedings of the British         age deraining,” in Proceedings of the 26th ACM Interna-
     Machine Vision Conference 2016, BMVC 2016, York,                 tional Conference on Multimedia, New York, NY, USA,
     UK, September 19-22, 2016, 2016.                                 2018, MM 18, p. 17511759, Association for Computing
                                                                      Machinery.
 [5] Chengyang Li, Dan Song, Ruofeng Tong, and Min Tang,
     “Illumination-aware faster R-CNN for robust multispec-
                                                                 [15] Zuoxin Li and Fuqiang Zhou, “FSSD: feature fu-
     tral pedestrian detection,” Pattern Recognition, vol. 85,
                                                                      sion single shot multibox detector,” CoRR, vol.
     pp. 161–171, 2019.
                                                                      abs/1712.00960, 2017.
 [6] Dayan Guan, Yanpeng Cao, Jiangxin Yang, Yanlong
                                                                 [16] K. Simonyan and A. Zisserman, “Very deep convolu-
     Cao, and Michael Ying Yang, “Fusion of multispectral
                                                                      tional networks for large-scale image recognition,” in
     data through illumination-aware deep neural networks
                                                                      International Conference on Learning Representations,
     for pedestrian detection,” Information Fusion, vol. 50,
                                                                      2015.
     pp. 148–157, 2019.

 [7] Chengyang Li, Dan Song, Ruofeng Tong, and Min Tang,         [17] Liliang Zhang, Liang Lin, Xiaodan Liang, and Kaim-
     “Multispectral pedestrian detection via simultaneous de-         ing He, “Is faster r-cnn doing well for pedestrian detec-
     tection and segmentation,” in British Machine Vision             tion?,” arXiv:1607.07032, 2016.
     Conference 2018, BMVC 2018, Northumbria Univer-
     sity, Newcastle, UK, September 3-6, 2018, 2018, p. 225.     [18] Garrick Brazil, Xi Yin, and Xiaoming Liu, “Illuminat-
                                                                      ing pedestrians via simultaneous detection & segmenta-
 [8] Lu Zhang, Zhiyong Liu, Shifeng Zhang, Xu Yang,                   tion,” in Proceedings of the IEEE International Confer-
     Hong Qiao, Kaizhu Huang, and Amir Hussain, “Cross-               ence on Computer Vision, Venice, Italy, 2017.
     modality interactive attention network for multispectral
     pedestrian detection,” Information Fusion, vol. 50, pp.     [19] Daniel König, Michael Adam, Christian Jarvers, Georg
     20–29, 2019.                                                     Layher, Heiko Neumann, and Michael Teutsch, “Fully
                                                                      convolutional region proposal networks for multispec-
 [9] Lu Zhang, Xiangyu Zhu, Xiangyu Chen, Xu Yang,                    tral person detection,” in 2017 IEEE Conference on
     Zhen Lei, and Zhiyong Liu, “Weakly aligned cross-                Computer Vision and Pattern Recognition Workshops,
     modal learning for multispectral pedestrian detection,”          CVPR Workshops 2017, Honolulu, HI, USA, July 21-26,
     in The IEEE International Conference on Computer Vi-             2017, 2017, pp. 243–250.
     sion (ICCV), October 2019.
                                                                 [20] Lee R. Dice, “Measures of the amount of ecologic as-
[10] Min Lin, Qiang Chen, and Shuicheng Yan, “Network in              sociation between species,” Ecology, vol. 26, no. 3, pp.
     network,” arXiv:1312.4400, 2013.                                 297–302, 1945.
[21] Lu Zhang, Zhiyong Liu, Xiangyu Chen, and Xu Yang,
     “The cross-modality disparity problem in multispec-
     tral pedestrian detection,” CoRR, vol. abs/1901.02645,
     2019.
