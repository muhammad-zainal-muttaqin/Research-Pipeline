---
source_id: 019
bibtex_key: tian2019fcos
title: FCOS: Fully Convolutional One-Stage Object Detection
year: 2019
domain_theme: Fondasi RGB
verified_pdf: 19_FCOS.pdf
char_count: 81429
---

FCOS: Fully Convolutional One-Stage Object Detection

                                                                      Zhi Tian          Chunhua Shen∗        Hao Chen                 Tong He
                                                                                      The University of Adelaide, Australia

                                                                     Abstract
arXiv:1904.01355v5 [cs.CV] 20 Aug 2019

                                             We propose a fully convolutional one-stage object detec-
                                         tor (FCOS) to solve object detection in a per-pixel predic-                    t
                                         tion fashion, analogue to semantic segmentation. Almost                    l       r
                                         all state-of-the-art object detectors such as RetinaNet, SSD,
                                         YOLOv3, and Faster R-CNN rely on pre-defined anchor
                                         boxes. In contrast, our proposed detector FCOS is anchor                       b
                                         box free, as well as proposal free. By eliminating the pre-
                                         defined set of anchor boxes, FCOS completely avoids the
                                         complicated computation related to anchor boxes such as
                                         calculating overlapping during training. More importantly,
                                         we also avoid all hyper-parameters related to anchor boxes,        Figure 1 – As shown in the left image, FCOS works by pre-
                                         which are often very sensitive to the final detection perfor-      dicting a 4D vector (l, t, r, b) encoding the location of a bound-
                                                                                                            ing box at each foreground pixel (supervised by ground-truth
                                         mance. With the only post-processing non-maximum sup-
                                                                                                            bounding box information during training). The right plot shows
                                         pression (NMS), FCOS with ResNeXt-64x4d-101 achieves
                                                                                                            that when a location residing in multiple bounding boxes, it
                                         44.7% in AP with single-model and single-scale testing,            can be ambiguous in terms of which bounding box this location
                                         surpassing previous one-stage detectors with the advantage         should regress.
                                         of being much simpler. For the first time, we demonstrate
                                         a much simpler and flexible detection framework achieving
                                         improved detection accuracy. We hope that the proposed
                                         FCOS framework can serve as a simple and strong alterna-          mark [16]. As a result, these hyper-parameters need to be
                                         tive for many other instance-level tasks. Code is available       carefully tuned in anchor-based detectors. 2) Even with
                                         at:                                                               careful design, because the scales and aspect ratios of an-
                                             tinyurl.com/FCOSv1                                            chor boxes are kept fixed, detectors encounter difficulties to
                                                                                                           deal with object candidates with large shape variations, par-
                                                                                                           ticularly for small objects. The pre-defined anchor boxes
                                         1. Introduction                                                   also hamper the generalization ability of detectors, as they
                                                                                                           need to be re-designed on new detection tasks with differ-
                                            Object detection is a fundamental yet challenging task in      ent object sizes or aspect ratios. 3) In order to achieve
                                         computer vision, which requires the algorithm to predict a        a high recall rate, an anchor-based detector is required to
                                         bounding box with a category label for each instance of in-       densely place anchor boxes on the input image (e.g., more
                                         terest in an image. All current mainstream detectors such         than 180K anchor boxes in feature pyramid networks (FPN)
                                         as Faster R-CNN [24], SSD [18] and YOLOv2, v3 [23] rely           [14] for an image with its shorter side being 800). Most
                                         on a set of pre-defined anchor boxes and it has long been         of these anchor boxes are labelled as negative samples dur-
                                         believed that the use of anchor boxes is the key to detectors’    ing training. The excessive number of negative samples ag-
                                         success. Despite their great success, it is important to note     gravates the imbalance between positive and negative sam-
                                         that anchor-based detectors suffer some drawbacks: 1) As          ples in training. 4) Anchor boxes also involve complicated
                                         shown in [15, 24], detection performance is sensitive to the      computation such as calculating the intersection-over-union
                                         sizes, aspect ratios and number of anchor boxes. For exam-        (IoU) scores with ground-truth bounding boxes.
                                         ple, in RetinaNet [15], varying these hyper-parameters af-           Recently, fully convolutional networks (FCNs) [20] have
                                         fects the performance up to 4% in AP on the COCO bench-           achieved tremendous success in dense prediction tasks such
                                           ∗ Corresponding author, email:   chunhua.shen@adelaide.edu.au   as semantic segmentation [20, 28, 9, 19], depth estimation
[17, 31], keypoint detection [3] and counting [2]. As one                • Detection is now unified with many other FCN-
of high-level vision tasks, object detection might be the                  solvable tasks such as semantic segmentation, making
only one deviating from the neat fully convolutional per-                  it easier to re-use ideas from those tasks.
pixel prediction framework mainly due to the use of anchor               • Detection becomes proposal free and anchor free,
boxes. It is nature to ask a question: Can we solve object                 which significantly reduces the number of design pa-
detection in the neat per-pixel prediction fashion, analogue               rameters. The design parameters typically need heuris-
to FCN for semantic segmentation, for example? Thus                        tic tuning and many tricks are involved in order to
those fundamental vision tasks can be unified in (almost)                  achieve good performance. Therefore, our new de-
one single framework. We show that the answer is affir-                    tection framework makes the detector, particularly its
mative. Moreover, we demonstrate that, for the first time,                 training, considerably simpler.
the much simpler FCN-based detector achieves even better                 • By eliminating the anchor boxes, our new detector
performance than its anchor-based counterparts.                            completely avoids the complicated computation re-
    In the literature, some works attempted to leverage the                lated to anchor boxes such as the IOU computation and
FCNs-based framework for object detection such as Dense-                   matching between the anchor boxes and ground-truth
Box [12]. Specifically, these FCN-based frameworks di-                     boxes during training, resulting in faster training and
rectly predict a 4D vector plus a class category at each spa-              testing as well as less training memory footprint than
tial location on a level of feature maps. As shown in Fig. 1               its anchor-based counterpart.
(left), the 4D vector depicts the relative offsets from the four         • Without bells and whistles, we achieve state-of-the-
sides of a bounding box to the location. These frameworks                  art results among one-stage detectors. We also show
are similar to the FCNs for semantic segmentation, except                  that the proposed FCOS can be used as a Region
that each location is required to regress a 4D continuous                  Proposal Networks (RPNs) in two-stage detectors and
vector. However, to handle the bounding boxes with dif-                    can achieve significantly better performance than its
ferent sizes, DenseBox [12] crops and resizes training im-                 anchor-based RPN counterparts. Given the even better
ages to a fixed scale. Thus DenseBox has to perform detec-                 performance of the much simpler anchor-free detector,
tion on image pyramids, which is against FCN’s philosophy                  we encourage the community to rethink the necessity of
of computing all convolutions once. Besides, more signif-                  anchor boxes in object detection, which are currently
icantly, these methods are mainly used in special domain                   considered as the de facto standard for detection.
objection detection such as scene text detection [33, 10] or
                                                                         • The proposed detector can be immediately extended
face detection [32, 12], since it is believed that these meth-
                                                                           to solve other vision tasks with minimal modification,
ods do not work well when applied to generic object de-
                                                                           including instance segmentation and key-point detec-
tection with highly overlapped bounding boxes. As shown
                                                                           tion. We believe that this new method can be the new
in Fig. 1 (right), the highly overlapped bounding boxes re-
                                                                           baseline for many instance-wise prediction problems.
sult in an intractable ambiguity: it is not clear w.r.t. which
bounding box to regress for the pixels in the overlapped re-
gions.                                                                 2. Related Work
    In the sequel, we take a closer look at the issue and show         Anchor-based Detectors. Anchor-based detectors inherit
that with FPN this ambiguity can be largely eliminated. As             the ideas from traditional sliding-window and proposal
a result, our method can already obtain comparable detec-              based detectors such as Fast R-CNN [6]. In anchor-based
tion accuracy with those traditional anchor based detectors.           detectors, the anchor boxes can be viewed as pre-defined
Furthermore, we observe that our method may produce a                  sliding windows or proposals, which are classified as pos-
number of low-quality predicted bounding boxes at the lo-              itive or negative patches, with an extra offsets regression
cations that are far from the center of an target object. In           to refine the prediction of bounding box locations. There-
order to suppress these low-quality detections, we intro-              fore, the anchor boxes in these detectors may be viewed
duce a novel “center-ness” branch (only one layer) to pre-             as training samples. Unlike previous detectors like Fast
dict the deviation of a pixel to the center of its correspond-         RCNN, which compute image features for each sliding win-
ing bounding box, as defined in Eq. (3). This score is then            dow/proposal repeatedly, anchor boxes make use of the fea-
used to down-weight low-quality detected bounding boxes                ture maps of CNNs and avoid repeated feature computation,
and merge the detection results in NMS. The simple yet ef-             speeding up detection process dramatically. The design of
fective center-ness branch allows the FCN-based detector               anchor boxes are popularized by Faster R-CNN in its RPNs
to outperform anchor-based counterparts under exactly the              [24], SSD [18] and YOLOv2 [22], and has become the con-
same training and testing settings.                                    vention in a modern detector.
    This new detection framework enjoys the following ad-                  However, as described above, anchor boxes result in
vantages.                                                              excessively many hyper-parameters, which typically need

                                                                   2
          7 x 8 /1 28                              P7                Head

          1 3x 1 6 /64                             P6                Head                                                   Classification
                                                                                                                               H xW xC

                               C5               P5                                                                           Center-ness
          25x 32 /32                                                 Head                                                      H xW x1
                                                                                                      x4
                                                                                        H x W x 256    H x W x 256
                           C4                   P4
          50x 64 /1 6
                                                                     Head                                                     Regression
                                                                                                                               H xW x4

                          C3                  P3                                                      x4
          1 00x 1 28 /8                                              Head             H x W x 256     H x W x 256

          800x 1 024
                                                                                            Shared Heads Between Feature Levels

          H x W /s        Backbone           Feature Pyramid                    Classification + Center-ness + Regression

 Figure 2 – The network architecture of FCOS, where C3, C4, and C5 denote the feature maps of the backbone network and P3 to P7 are
 the feature levels used for the final prediction. H × W is the height and width of feature maps. ‘/s’ (s = 8, 16, ..., 128) is the down-
 sampling ratio of the feature maps at the level to the input image. As an example, all the numbers are computed with an 800 × 1024
 input.

to be carefully tuned in order to achieve good perfor-                  free detector, which detects a pair of corners of a bound-
mance. Besides the above hyper-parameters describing an-                ing box and groups them to form the final detected bound-
chor shapes, the anchor-based detectors also need other                 ing box. CornerNet requires much more complicated post-
hyper-parameters to label each anchor box as a positive,                processing to group the pairs of corners belonging to the
ignored or negative sample. In previous works, they of-                 same instance. An extra distance metric is learned for the
ten employ intersection over union (IOU) between anchor                 purpose of grouping.
boxes and ground-truth boxes to determine the label of an                  Another family of anchor-free detectors such as [32] are
anchor box (e.g., a positive anchor if its IOU is in [0.5, 1]).         based on DenseBox [12]. The family of detectors have been
These hyper-parameters have shown a great impact on the                 considered unsuitable for generic object detection due to
final accuracy, and require heuristic tuning. Meanwhile,                difficulty in handling overlapping bounding boxes and the
these hyper-parameters are specific to detection tasks, mak-            recall being relatively low. In this work, we show that both
ing detection tasks deviate from a neat fully convolutional             problems can be largely alleviated with multi-level FPN
network architectures used in other dense prediction tasks              prediction. Moreover, we also show together with our pro-
such as semantic segmentation.                                          posed center-ness branch, the much simpler detector can
                                                                        achieve even better detection performance than its anchor-
                                                                        based counterparts.
Anchor-free Detectors. The most popular anchor-free
detector might be YOLOv1 [21]. Instead of using anchor                  3. Our Approach
boxes, YOLOv1 predicts bounding boxes at points near
the center of objects. Only the points near the center are                 In this section, we first reformulate object detection in
used since they are considered to be able to produce higher-            a per-pixel prediction fashion. Next, we show that how
quality detection. However, since only points near the cen-             we make use of multi-level prediction to improve the re-
ter are used to predict bounding boxes, YOLOv1 suffers                  call and resolve the ambiguity resulted from overlapped
from low recall as mentioned in YOLOv2 [22]. As a result,               bounding boxes. Finally, we present our proposed “center-
YOLOv2 [22] employs anchor boxes as well. Compared to                   ness” branch, which helps suppress the low-quality detected
YOLOv1, FCOS takes advantages of all points in a ground                 bounding boxes and improves the overall performance by a
truth bounding box to predict the bounding boxes and the                large margin.
low-quality detected bounding boxes are suppressed by the
proposed “center-ness” branch. As a result, FCOS is able to             3.1. Fully Convolutional One-Stage Object Detector
provide comparable recall with anchor-based detectors as                   Let Fi ∈ RH×W ×C be the feature maps at layer i of
shown in our experiments.                                               a backbone CNN and s be the total stride until the layer.
   CornerNet [13] is a recently proposed one-stage anchor-              The ground-truth bounding boxes for an input image are

                                                                    3
                                       (i)   (i)   (i) (i)
defined as {Bi }, where Bi = (x0 , y0 , x1 y1 , c(i) ) ∈                 sification and regression branches. Moreover, since the re-
                               (i) (i)             (i) (i)               gression targets are always positive, we employ exp(x) to
R4 × {1, 2 ... C}. Here (x0 , y0 ) and (x1 y1 ) denote
the coordinates of the left-top and right-bottom corners of              map any real number to (0, ∞) on the top of the regression
the bounding box. c(i) is the class that the object in the               branch. It is worth noting that FCOS has 9× fewer network
bounding box belongs to. C is the number of classes, which               output variables than the popular anchor-based detectors
is 80 for MS-COCO dataset.                                               [15, 24] with 9 anchor boxes per location.
    For each location (x, y) on the feature map Fi ,we can
map it back onto the input image as (b 2s c + xs, 2s + ys),              Loss Function.        We define our training loss function as
which is near the center of the receptive field of the location          follows:
(x, y). Different from anchor-based detectors, which con-
sider the location on the input image as the center of (multi-                                       1 X
                                                                          L({ppx,y }, {ttx,y }) =            Lcls (ppx,y , c∗x,y )
ple) anchor boxes and regress the target bounding box with                                          Npos x,y
these anchor boxes as references, we directly regress the tar-
                                                                                                     λ X
get bounding box at the location. In other words, our detec-                                    +            1{c∗x,y >0} Lreg (ttx,y , t ∗x,y ),
tor directly views locations as training samples instead of                                         Npos x,y
anchor boxes in anchor-based detectors, which is the same                                                                                     (2)
as FCNs for semantic segmentation [20].
    Specifically, location (x, y) is considered as a positive            where Lcls is focal loss as in [15] and Lreg is the IOU loss
sample if it falls into any ground-truth box and the class la-           as in UnitBox [32]. Npos denotes the number of positive
bel c∗ of the location is the class label of the ground-truth            samples and λ being 1 in this paper is the balance weight
box. Otherwise it is a negative sample and c∗ = 0 (back-                 for Lreg . The summation is calculated over all locations
ground class). Besides the label for classification, we also             on the feature maps Fi . 1{c∗i >0} is the indicator function,
have a 4D real vector t ∗ = (l∗ , t∗ , r∗ , b∗ ) being the regres-       being 1 if c∗i > 0 and 0 otherwise.
sion targets for the location. Here l∗ , t∗ , r∗ and b∗ are the
distances from the location to the four sides of the bound-              Inference. The inference of FCOS is straightforward.
ing box, as shown in Fig. 1 (left). If a location falls into             Given an input images, we forward it through the network
multiple bounding boxes, it is considered as an ambiguous                and obtain the classification scores p x,y and the regression
sample. We simply choose the bounding box with minimal                   prediction t x,y for each location on the feature maps Fi .
area as its regression target. In the next section, we will              Following [15], we choose the location with px,y > 0.05 as
show that with multi-level prediction, the number of am-                 positive samples and invert Eq. (1) to obtain the predicted
biguous samples can be reduced significantly and thus they               bounding boxes.
hardly affect the detection performance. Formally, if loca-
tion (x, y) is associated to a bounding box Bi , the training            3.2. Multi-level Prediction with FPN for FCOS
regression targets for the location can be formulated as,
                                                                             Here we show that how two possible issues of the pro-
                 ∗        (i)      ∗        (i)                          posed FCOS can be resolved with multi-level prediction
                l = x − x0 ,      t = y − y0 ,
                      (i)               (i)
                                                              (1)        with FPN [14]. 1) The large stride (e.g., 16×) of the final
                r∗ = x1 − x,      b∗ = y1 − y.                           feature maps in a CNN can result in a relatively low best
                                                                         possible recall (BPR)1 . For anchor based detectors, low re-
It is worth noting that FCOS can leverage as many fore-
                                                                         call rates due to the large stride can be compensated to some
ground samples as possible to train the regressor. It is dif-
                                                                         extent by lowering the required IOU scores for positive an-
ferent from anchor-based detectors, which only consider the
                                                                         chor boxes. For FCOS, at the first glance one may think that
anchor boxes with a highly enough IOU with ground-truth
                                                                         the BPR can be much lower than anchor-based detectors
boxes as positive samples. We argue that it may be one of
                                                                         because it is impossible to recall an object which no loca-
the reasons that FCOS outperforms its anchor-based coun-
                                                                         tion on the final feature maps encodes due to a large stride.
terparts.
                                                                         Here, we empirically show that even with a large stride,
                                                                         FCN-based FCOS is still able to produce a good BPR, and
Network Outputs. Corresponding to the training targets,                  it can even better than the BPR of the anchor-based detec-
the final layer of our networks predicts an 80D vector p of              tor RetinaNet [15] in the official implementation Detectron
classification labels and a 4D vector t = (l, t, r, b) bound-            [7] (refer to Table 1). Therefore, the BPR is actually not
ing box coordinates. Following [15], instead of training a               a problem of FCOS. Moreover, with multi-level FPN pre-
multi-class classifier, we train C binary classifiers. Simi-             diction [14], the BPR can be improved further to match the
lar to [15], we add four convolutional layers after the fea-
ture maps of the backbone networks respectively for clas-                  1 Upper bound of the recall rate that a detector can achieve.

                                                                     4
best BPR the anchor-based RetinaNet can achieve. 2) Over-               3.3. Center-ness for FCOS
laps in ground-truth boxes can cause intractable ambiguity
                                                                             After using multi-level prediction in FCOS, there is still
, i.e., which bounding box should a location in the overlap
                                                                        a performance gap between FCOS and anchor-based detec-
regress? This ambiguity results in degraded performance of
                                                                        tors. We observed that it is due to a lot of low-quality pre-
FCN-based detectors. In this work, we show that the am-
                                                                        dicted bounding boxes produced by locations far away from
biguity can be greatly resolved with multi-level prediction,
                                                                        the center of an object.
and the FCN-based detector can obtain on par, sometimes
even better, performance compared with anchor-based ones.                    We propose a simple yet effective strategy to suppress
                                                                        these low-quality detected bounding boxes without intro-
   Following FPN [14], we detect different sizes of ob-                 ducing any hyper-parameters. Specifically, we add a single-
jects on different levels of feature maps. Specifically,                layer branch, in parallel with the classification branch (as
we make use of five levels of feature maps defined as                   shown in Fig. 2) to predict the “center-ness” of a location2 .
{P3 , P4 , P5 , P6 , P7 }. P3 , P4 and P5 are produced by the           The center-ness depicts the normalized distance from the
backbone CNNs’ feature maps C3 , C4 and C5 followed by                  location to the center of the object that the location is re-
a 1 × 1 convolutional layer with the top-down connections               sponsible for, as shown Fig. 7. Given the regression targets
in [14], as shown in Fig. 2. P6 and P7 are produced by ap-              l∗ , t∗ , r∗ and b∗ for a location, the center-ness target is de-
plying one convolutional layer with the stride being 2 on P5            fined as,
and P6 , respectively. As a result, the feature levels P3 , P4 ,                                 s
P5 , P6 and P7 have strides 8, 16, 32, 64 and 128, respec-                                          min(l∗ , r∗ )    min(t∗ , b∗ )
                                                                                 centerness∗ =                    ×                . (3)
tively.                                                                                             max(l∗ , r∗ ) max(t∗ , b∗ )

   Unlike anchor-based detectors, which assign anchor                   We employ sqrt here to slow down the decay of the center-
boxes with different sizes to different feature levels, we di-          ness. The center-ness ranges from 0 to 1 and is thus trained
rectly limit the range of bounding box regression for each              with binary cross entropy (BCE) loss. The loss is added to
level. More specifically, we firstly compute the regression             the loss function Eq. (2). When testing, the final score (used
targets l∗ , t∗ , r∗ and b∗ for each location on all feature lev-       for ranking the detected bounding boxes) is computed by
els. Next, if a location satisfies max(l∗ , t∗ , r∗ , b∗ ) > mi         multiplying the predicted center-ness with the correspond-
or max(l∗ , t∗ , r∗ , b∗ ) < mi−1 , it is set as a negative sam-        ing classification score. Thus the center-ness can down-
ple and is thus not required to regress a bounding box any-             weight the scores of bounding boxes far from the center
more. Here mi is the maximum distance that feature level                of an object. As a result, with high probability, these low-
i needs to regress. In this work, m2 , m3 , m4 , m5 , m6 and            quality bounding boxes might be filtered out by the final
m7 are set as 0, 64, 128, 256, 512 and ∞, respectively.                 non-maximum suppression (NMS) process, improving the
Since objects with different sizes are assigned to different            detection performance remarkably.
feature levels and most overlapping happens between ob-                    An alternative of the center-ness is to make use of only
jects with considerably different sizes. If a location, even            the central portion of ground-truth bounding box as posi-
with multi-level prediction used, is still assigned to more             tive samples with the price of one extra hyper-parameter,
than one ground-truth boxes, we simply choose the ground-               as shown in works [12, 33]. After our submission, it has
truth box with minimal area as its target. As shown in our              been shown in [1] that the combination of both methods
experiments, the multi-level prediction can largely alleviate           can achieve a much better performance. The experimental
the aforementioned ambiguity and improve the FCN-based                  results can be found in Table 3.
detector to the same level of anchor-based ones.
                                                                        4. Experiments
   Finally, following [14, 15], we share the heads be-
tween different feature levels, not only making the detector               Our experiments are conducted on the large-scale detec-
parameter-efficient but also improving the detection perfor-            tion benchmark COCO [16]. Following the common prac-
mance. However, we observe that different feature levels                tice [15, 14, 24], we use the COCO trainval35k split
are required to regress different size range (e.g., the size            (115K images) for training and minival split (5K images)
range is [0, 64] for P3 and [64, 128] for P4 ), and therefore it        as validation for our ablation study. We report our main re-
is not reasonable to make use of identical heads for differ-            sults on the test dev split (20K images) by uploading our
ent feature levels. As a result, instead of using the standard          detection results to the evaluation server.
exp(x), we make use of exp(si x) with a trainable scalar si                2 After the initial submission, it has been shown that the AP on MS-
to automatically adjust the base of the exponential function            COCO can be improved if the center-ness is parallel with the regression
for feature level Pi , which slightly improves the detection            branch instead of the classification branch. However, unless specified, we
performance.                                                            still use the configuration in Fig. 2.

                                                                    5
                                                                             Method       w/ FPN Low-quality matches BPR (%)
                                                                             RetinaNet       X              None                86.82
                                                                             RetinaNet       X              ≥ 0.4               90.92
                                       t*                                    RetinaNet       X                All               99.23
                                                                             FCOS                              -                95.55
                                                                             FCOS            X                 -                98.40
                                                                          Table 1 – The BPR for anchor-based RetinaNet under a vari-
                          l*              r*                              ety of matching rules and the BPR for FCN-based FCOS. FCN-
                                                                          based FCOS has very similar recall to the best anchor-based one
                                                                          and has much higher recall than the official implementation in
                                                                          Detectron [7], where only low-quality matches with IOU ≥ 0.4
                                       b*                                 are considered.

                                                                            w/ FPN      Amb. samples (%) Amb. samples (diff.) (%)
 Figure 3 – Center-ness. Red, blue, and other colors denote 1, 0                               23.16                   17.84
 and the values between them, respectively. Center-ness is com-                X                7.14                   3.75
 puted by Eq. (3) and decays from 1 to 0 as the location deviates         Table 2 – Amb. samples denotes the ratio of the ambiguous
 from the center of the object. When testing, the center-ness pre-        samples to all positive samples. Amb. samples (diff.) is similar
 dicted by the network is multiplied with the classification score        but excludes those ambiguous samples in the overlapped regions
 thus can down-weight the low-quality bounding boxes predicted            but belonging to the same category as the kind of ambiguity
 by a location far from the center of an object.                          does not matter when inferring. We can see that with FPN, this
                                                                          percentage of ambiguous samples is small (3.75%).

Training Details. Unless specified, ResNet-50 [8] is used
                                                                         with multi-level prediction.
as our backbone networks and the same hyper-parameters
with RetinaNet [15] are used. Specifically, our network is
trained with stochastic gradient descent (SGD) for 90K it-               Best Possible Recalls. The first concern about the FCN-
erations with the initial learning rate being 0.01 and a mini-           based detector is that it might not provide a good best pos-
batch of 16 images. The learning rate is reduced by a factor             sible recall (BPR). In the section, we show that the con-
of 10 at iteration 60K and 80K, respectively. Weight de-                 cern is not necessary. Here BPR is defined as the ratio of
cay and momentum are set as 0.0001 and 0.9, respectively.                the number of ground-truth boxes a detector can recall at
We initialize our backbone networks with the weights pre-                the most divided by all ground-truth boxes. A ground-truth
trained on ImageNet [4]. For the newly added layers, we                  box is considered being recalled if the box is assigned to
initialize them as in [15]. Unless specified, the input im-              at least one sample (i.e., a location in FCOS or an anchor
ages are resized to have their shorter side being 800 and                box in anchor-based detectors) during training. As shown
their longer side less or equal to 1333.                                 in Table 1, only with feature level P4 with stride being 16
                                                                         (i.e., no FPN), FCOS can already obtain a BPR of 95.55%.
                                                                         The BPR is much higher than the BPR of 90.92% of the
Inference Details. We firstly forward the input image
                                                                         anchor-based detector RetinaNet in the official implemen-
through the network and obtain the predicted bounding
                                                                         tation Detectron, where only the low-quality matches with
boxes with a predicted class. Unless specified, the following
                                                                         IOU ≥ 0.4 are used. With the help of FPN, FCOS can
post-processing is exactly the same with RetinaNet [15] and
                                                                         achieve a BPR of 98.40%, which is very close to the best
we directly make use of the same post-processing hyper-
                                                                         BPR that the anchor-based detector can achieve by using all
parameters of RetinaNet. We use the same sizes of input
                                                                         low-quality matches. Due to the fact that the best recall of
images as in training. We hypothesize that the performance
                                                                         current detectors are much lower than 90%, the small BPR
of our detector may be improved further if we carefully tune
                                                                         gap (less than 1%) between FCOS and the anchor-based de-
the hyper-parameters.
                                                                         tector will not actually affect the performance of detector.
4.1. Ablation Study                                                      It is also confirmed in Table 3, where FCOS achieves even
                                                                         better AR than its anchor-based counterparts under the same
4.1.1   Multi-level Prediction with FPN                                  training and testing settings. Therefore, the concern about
As mentioned before, the major concerns of an FCN-based                  low BPR may not be necessary.
detector are low recall rates and ambiguous samples re-
sulted from overlapping in ground-truth bounding boxes. In               Ambiguous Samples. Another concern about the FCN-
the section, we show that both issues can be largely resolved            based detector is that it may have a large number of ambigu-

                                                                     6
      Method               C5 /P5 w/ GN nms thr.            AP   AP50 AP75 APS APM APL AR1 AR10 AR100
      RetinaNet              C5                   .50      35.9   56.0     38.2     20.0     39.8    47.4    31.0     49.4      52.5
      FCOS                   C5                   .50      36.3   54.8     38.7     20.5     39.8    47.8    31.5     50.6      53.5
      FCOS                   P5                   .50      36.4   54.9     38.8     19.7     39.7    48.8    31.4     50.6      53.4
      FCOS                   P5                   .60      36.5   54.5     39.2     19.8     40.0    48.9    31.3     51.2      54.5
      FCOS                   P5        X          .60      37.1   55.9     39.8     21.3     41.0    47.8    31.4     51.4      54.9
      Improvements
      + ctr. on reg.         P5        X          .60      37.4   56.1     40.3     21.8     41.2    48.8    31.5     51.7      55.2
      + ctr. sampling [1]    P5        X          .60      38.1   56.7     41.4     22.6     41.6    50.4    32.1     52.8      56.3
      + GIoU [1]             P5        X          .60      38.3   57.1     41.0     21.9     42.4    49.5    32.0     52.9      56.5
      + Normalization        P5        X          .60      38.6   57.4     41.4     22.3     42.5    49.8    32.3     53.4      57.1
 Table 3 – FCOS vs. RetinaNet on the minival split with ResNet-50-FPN as the backbone. Directly using the training and testing
 settings of RetinaNet, our anchor-free FCOS achieves even better performance than anchor-based RetinaNet both in AP and AR. With
 Group Normalization (GN) in heads and NMS threshold being 0.6, FCOS can achieve 37.1 in AP. After our submission, some almost
 cost-free improvements have been made for FCOS and the performance has been improved by a large margin, as shown by the rows
 below “Improvements”. “ctr. on reg.”: moving the center-ness branch to the regression branch. “ctr. sampling”: only sampling the
 central portion of ground-truth boxes as positive samples. “GIoU”: penalizing the union area over the circumscribed rectangle’s area in
 IoU Loss. “Normalization”: normalizing the regression targets in Eq. (1) with the strides of FPN levels. Refer to our code for details.

ous samples due to the overlapping in ground-truth bound-                                AP     AP50 AP75 APS APM APL
ing boxes, as shown in Fig. 1 (right). In Table 2, we show               None           33.5     52.6    35.2    20.8    38.5    42.6
the ratios of the ambiguous samples to all positive samples              center-ness† 33.5       52.4    35.1    20.8    37.8    42.8
on minival split. As shown in the table, there are indeed a              center-ness    37.1     55.9    39.8    21.3    41.0    47.8
large amount of ambiguous samples (23.16%) if FPN is not                Table 4 – Ablation study for the proposed center-ness branch
                                                                        on minival split. “None” denotes that no center-ness is
used and only feature level P4 is used. However, with FPN,
                                                                        used. “center-ness† ” denotes that using the center-ness com-
the ratio can be significantly reduced to only 7.14% since              puted from the predicted regression vector. “center-ness” is
most of overlapped objects are assigned to different feature            that using center-ness predicted from the proposed center-ness
levels. Moreover, we argue that the ambiguous samples re-               branch. The center-ness branch improves the detection perfor-
sulted from overlapping between objects of the same cate-               mance under all metrics.
gory do not matter. For instance, if object A and B with the
same class have overlap, no matter which object the loca-              4.1.2   With or Without Center-ness
tions in the overlap predict, the prediction is correct because
it is always matched with the same category. The missed ob-            As mentioned before, we propose “center-ness” to suppress
ject can be predicted by the locations only belonging to it.           the low-quality detected bounding boxes produced by the
Therefore, we only count the ambiguous samples in over-                locations far from the center of an object. As shown in
lap between bounding boxes with different categories. As               Table 4, the center-ness branch can boost AP from 33.5%
shown in Table 2, the multi-level prediction reduces the ra-           to 37.1%, making anchor-free FCOS outperform anchor-
tio of ambiguous samples from 17.84% to 3.75%. In order                based RetinaNet (35.9%). Note that anchor-based Reti-
to further show that the overlapping in ground truth boxes is          naNet employs two IoU thresholds to label anchor boxes as
not a problem of our FCN-based FCOS, we count that when                positive/negative samples, which can also help to suppress
inferring how many detected bounding boxes come from                   the low-quality predictions. The proposed center-ness can
the ambiguous locations. We found that only 2.3% detected              eliminate the two hyper-parameters. However, after our ini-
bounding boxes are produced by the ambiguous locations.                tial submission, it has shown that using both center-ness and
By further only considering the overlap between different              the thresholds can result in a better performance, as shown
categories, the ratio is reduced to 1.5%. Note that it does            by the row “+ ctr. sampling” in Table 3. One may note
not imply that there are 1.5% locations where FCOS cannot              that center-ness can also be computed with the predicted
work. As mentioned before, these locations are associated              regression vector without introducing the extra center-ness
with the ground-truth boxes with minimal area. Therefore,              branch. However, as shown in Table 4, the center-ness com-
these locations only take the risk of missing some larger ob-          puted from the regression vector cannot improve the perfor-
jects. As shown in the following experiments, they do not              mance and thus the separate center-ness is necessary.
make our FCOS inferior to anchor-based detectors.
                                                                       4.1.3   FCOS vs. Anchor-based Detectors
                                                                       The aforementioned FCOS has two minor differences from
                                                                       the standard RetinaNet. 1) We use Group Normalization

                                                                   7
             Method                            Backbone                         AP    AP50 AP75 APS APM APL
           Two-stage methods:
             Faster R-CNN w/ FPN [14]          ResNet-101-FPN                   36.2   59.1     39.0    18.2      39.0   48.2
             Faster R-CNN by G-RMI [11] Inception-ResNet-v2 [27]                34.7   55.5     36.7    13.5      38.1   52.0
             Faster R-CNN w/ TDM [25]          Inception-ResNet-v2-TDM 36.8            57.7     39.2    16.2      39.8   52.1
           One-stage methods:
             YOLOv2 [22]                       DarkNet-19 [22]                  21.6   44.0     19.2     5.0      22.4   35.5
             SSD513 [18]                       ResNet-101-SSD                   31.2   50.4     33.3    10.2      34.5   49.8
             DSSD513 [5]                       ResNet-101-DSSD                  33.2   53.3     35.2    13.0      35.4   51.1
             RetinaNet [15]                    ResNet-101-FPN                   39.1   59.1     42.3    21.8      42.7   50.2
             CornerNet [13]                    Hourglass-104                    40.5   56.5     43.1    19.4      42.7   53.9
             FSAF [34]                         ResNeXt-64x4d-101-FPN            42.9   63.8     46.3    26.6      46.2   52.7
             FCOS                              ResNet-101-FPN                   41.5   60.7     45.0    24.4      44.8   51.6
             FCOS                              HRNet-W32-5l [26]                42.0   60.4     45.3    25.4      45.0   51.0
             FCOS                              ResNeXt-32x8d-101-FPN            42.7   62.2     46.1    26.0      45.6   52.6
             FCOS                              ResNeXt-64x4d-101-FPN            43.2   62.8     46.6    26.5      46.2   53.3
             FCOS w/ improvements              ResNeXt-64x4d-101-FPN            44.7   64.1     48.4    27.6      47.5   55.6
 Table 5 – FCOS vs. other state-of-the-art two-stage or one-stage detectors (single-model and single-scale results). FCOS outperforms the
 anchor-based counterpart RetinaNet by 2.4% in AP with the same backbone. FCOS also outperforms the recent anchor-free one-stage
 detector CornerNet with much less design complexity. Refer to Table 3 for details of “improvements”.

 Method                        # samples AR100 AR1k                     4.2. Comparison with State-of-the-art Detectors
 RPN w/ FPN & GN (ReImpl.)      ∼200K       44.7     56.9
 FCOS w/ GN w/o center-ness      ∼66K       48.0     59.3                  We compare FCOS with other state-of-the-art object de-
 FCOS w/ GN                      ∼66K       52.8     60.3               tectors on test − dev split of MS-COCO benchmark. For
 Table 6 – FCOS as Region Proposal Networks vs. RPNs with               these experiments, we randomly scale the shorter side of
 FPN. ResNet-50 is used as the backbone. FCOS improves                  images in the range from 640 to 800 during the training and
 AR100 and AR1k by 8.1% and 3.4%, respectively. GN: Group               double the number of iterations to 180K (with the learn-
 Normalization.                                                         ing rate change points scaled proportionally). Other set-
                                                                        tings are exactly the same as the model with AP 37.1% in
(GN) [29] in the newly added convolutional layers except                Table 3. As shown in Table 5, with ResNet-101-FPN, our
for the last prediction layers, which makes our training more           FCOS outperforms the RetinaNet with the same backbone
stable. 2) We use P5 to produce the P6 and P7 instead of                ResNet-101-FPN by 2.4% in AP. To our knowledge, it is
C5 in the standard RetinaNet. We observe that using P5 can              the first time that an anchor-free detector, without any bells
improve the performance slightly.                                       and whistles outperforms anchor-based detectors by a large
    To show that our FCOS can serve as an simple and strong             margin. FCOS also outperforms other classical two-stage
alternative of anchor-based detectors, and for a fair compar-           anchor-based detectors such as Faster R-CNN by a large
ison, we remove GN (the gradients are clipped to prevent                margin. With ResNeXt-64x4d-101-FPN [30] as the back-
them from exploding) and use C5 in our detector. As shown               bone, FCOS achieves 43.2% in AP. It outperforms the re-
in Table 3, with exactly the same settings, our FCOS still              cent state-of-the-art anchor-free detector CornerNet [13] by
compares favorably with the anchor-based detector (36.3%                a large margin while being much simpler. Note that Cor-
vs 35.9%). Moreover, it is worth to note that we directly use           nerNet requires to group corners with embedding vectors,
all hyper-parameters (e.g., learning rate, the NMS threshold            which needs special design for the detector. Thus, we ar-
and etc.) from RetinaNet, which have been optimized for                 gue that FCOS is more likely to serve as a strong and sim-
the anchor-based detector. We argue that the performance                ple alternative to current mainstream anchor-based detec-
of FCOS can be improved further if the hyper-parameters                 tors. Moreover, FCOS with the improvements in Table 3
are tuned for it.                                                       achieves 44.7% in AP with single-model and single scale
    It is worth noting that with some almost cost-free im-              testing, which surpasses previous detectors by a large mar-
provements, as shown in Table 3, the performance of                     gin.
our anchor-free detector can be improved by a large mar-
gin. Given the superior performance and the merits of the               5. Extensions on Region Proposal Networks
anchor-free detector (e.g., much simpler and fewer hyper-
parameters than anchor-based detectors), we encourage the                  So far we have shown that in a one-stage detector, our
community to rethink the necessity of anchor boxes in ob-               FCOS can achieve even better performance than anchor-
ject detection.                                                         based counterparts. Intuitively, FCOS should be also able

                                                                    8
to replace the anchor boxes in Region Proposal Networks                             1.0
(RPNs) with FPN [14] in the two-stage detector Faster R-
CNN. Here, we confirm that by experiments.
                                                                                    0.8
   Compared to RPNs with FPN [14], we replace anchor
boxes with the method in FCOS. Moreover, we add GN into
the layers in FPN heads, which can make our training more                           0.6

                                                                        Precision
stable. All other settings are exactly the same with RPNs
with FPN in the official code [7]. As shown in Table 6, even
                                                                                    0.4
without the proposed center-ness branch, our FCOS already
improves both AR100 and AR1k significantly. With the pro-
posed center-ness branch, FCOS further boosts AR100 and                             0.2
AR1k respectively to 52.8% and 60.3%, which are 18% rel-                                      FCOS
                                                                                              Original RetinaNet
ative improvement for AR100 and 3.4% absolute improve-                                        Retinanet w/ GN
ment for AR1k over the RPNs with FPN.                                                     0         0.2            0.4            0.6   0.8   0.9   1.0
                                                                                                                         Recall

6. Conclusion
                                                                              Figure 4 – Class-agnostic precision-recall curves at IOU =
   We have proposed an anchor-free and proposal-free one-                     0.50.
stage detector FCOS. As shown in experiments, FCOS
compares favourably against the popular anchor-based one-
stage detectors, including RetinaNet, YOLO and SSD,                        being 0.50, 0.75 and 0.90, respectively. Table 7 shows APs
but with much less design complexity. FCOS completely                      corresponding to the three curves.
avoids all computation and hyper-parameters related to an-                    As shown in Table 7, our FCOS achieves better perfor-
chor boxes and solves the object detection in a per-pixel pre-             mance than its anchor-based counterpart RetinaNet. More-
diction fashion, similar to other dense prediction tasks such              over, it worth noting that with a stricter IOU threshold,
as semantic segmentation. FCOS also achieves state-of-the-                 FCOS enjoys a larger improvement over RetinaNet, which
art performance among one-stage detectors. We also show                    suggests that FCOS has a better bounding box regressor to
that FCOS can be used as RPNs in the two-stage detector                    detect objects more accurately. One of the reasons should
Faster R-CNN and outperforms the its RPNs by a large mar-                  be that FCOS has the ability to leverage more foreground
gin. Given its effectiveness and efficiency, we hope that                  samples to train the regressor as mentioned in our main pa-
FCOS can serve as a strong and simple alternative of cur-                  per.
rent mainstream anchor-based detectors. We also believe                       Finally, as shown in all precision-recall curves, the best
that FCOS can be extended to solve many other instance-                    recalls of these detectors in the precision-recall curves are
level recognition tasks.                                                   much lower than 90%. It further suggests that the small gap
                                                                           (98.40% vs. 99.23%) of best possible recall (BPR) between
Appendix                                                                   FCOS and RetinaNet hardly harms the final detection per-
                                                                           formance.
7. Class-agnostic Precision-recall Curves
                                                                           8. Visualization for Center-ness
   Method                     AP      AP50     AP75     AP90                   As mentioned in our main paper, by suppressing low-
   Orginal RetinaNet [15]     39.5    63.6     41.8     10.6               quality detected bounding boxes, the proposed center-ness
   RetinaNet w/ GN [29]       40.0    64.5     42.2     10.4               branch improves the detection performance by a large mar-
   FCOS                       40.5    64.7     42.6     13.1               gin. In this section, we confirm this.
                                      +0.2     +0.4     +2.7                   We expect that the center-ness can down-weight the
 Table 7 – The class-agnostic detection performance for Reti-              scores of low-quality bounding boxes such that these
 naNet and FCOS. FCOS has better performance than RetinaNet.               bounding boxes can be filtered out in following post-
 Moreover, the improvement over RetinaNet becomes larger with              processing such as non-maximum suppression (NMS). A
 a stricter IOU threshold. The results are obtained with the same          detected bounding box is considered as a low-quality one if
 models in Table 4 of our main paper.                                      it has a low IOU score with its corresponding ground-truth
                                                                           bounding box. A bounding box with low IOU but a high
                                                                           confidence score is likely to become a false positive and
   In Fig. 4, Fig. 5 and Fig. 6, we present class-agnostic                 harm the precision.
precision-recall curves on split minival at IOU thresholds                     In Fig. 7, we consider a detected bounding box as a 2D

                                                                    9
            1.0                                                                        9. Qualitative Results
                                                                                          Some qualitative results are shown in Fig. 8. As shown
            0.8                                                                        in the figure, our proposed FCOS can detect a wide range
                                                                                       of objects including crowded, occluded, highly overlapped,
                                                                                       extremely small and very large objects.
            0.6
Precision

                                                                                       10. More discussions
            0.4
                                                                                       Center-ness vs. IoUNet:
                                                                                           Center-ness and IoUNet of Jiang et al. “Acquisition of
            0.2                                                                        Localization Confidence for Accurate Object Detection”
                      FCOS
                      Original RetinaNet                                               shares a similar purpose (i.e., to suppress low-quality pre-
                      Retinanet w/ GN                                                  dictions) with different approaches. IoUNet trains a sep-
                  0          0.2           0.4            0.6   0.8   0.9   1.0        arate network to predict the IoU score between predicted
                                                 Recall
                                                                                       bounding-boxes and ground-truth boxes. Center-ness, as a
                                                                                       part of our detector, only has a single layer and is trained
      Figure 5 – Class-agnostic precision-recall curves at IOU =                       jointly with the detector, thus being much simpler. More-
      0.75.                                                                            over, “center-ness” does not take as input the predicted
                                                                                       bounding-boxes. Instead, it directly accesses the location’s
            1.0       FCOS                                                             ability to predict high-quality bounding-boxes.
                      Original RetinaNet
                      Retinanet w/ GN                                                  BPR in Section 4.1 and ambiguity analysis:
                                                                                           We do not aim to compare “recall by specific IoU” with
            0.8
                                                                                       “recall by pixel within box”. The main purpose of Table 1
                                                                                       is to show that the upper bound of recall of FCOS is very
            0.6                                                                        close to the upper bound of recall of anchor-based Reti-
Precision

                                                                                       naNet (98.4% vs. 99.23%). BPR by other IoU thresholds
                                                                                       are listed as those are used in the official code of RetinaNet.
            0.4                                                                        Moreover, no evidence shows that the regression targets of
                                                                                       FCOS are difficult to learn because they are more spread-
            0.2                                                                        out. FCOS in fact yields more accurate bounding-boxes.
                                                                                           During training, we deal with the ambiguity at the same
                                                                                       FPN level by choosing the ground-truth box with the min-
                  0         0.2            0.4            0.6   0.8   0.9   1.0        imal area. When testing, if two objects A and B with the
                                                 Recall                                same class have overlap, no matter which one object the
                                                                                       locations in the overlap predict, the prediction is correct
      Figure 6 – Class-agnostic precision-recall curves at IOU =                       and the missed one can be predicted by the locations only
      0.90.                                                                            belonging to it. In the case that A and B do not belong
                                                                                       to the same class, a location in the overlap might predict
                                                                                       A’s class but regress B’s bounding-box, which is a mistake.
   point (x, y) with x being its score and y being the IOU with                        That is why we only count the ambiguity across different
   its corresponding ground-truth box. As shown in Fig. 7                              classes. Moreover, it appears that this ambiguity does not
   (left), before applying the center-ness, there are a large                          make FCOS worse than RetinaNet in AP, as shown in Table
   number of low-quality bounding boxes but with a high con-                           8.
   fidence score (i.e., the points under the line y = x). Due                          Additional ablation study:
   to their high scores, these low-quality bounding boxes can-                         As shown in Table 8, a vanilla FCOS performs on par with
   not be eliminated in post-processing and result in lowering                         RetinaNet, being of simpler design and with ∼ 9× less net-
   the precision of the detector. After multiplying the classi-                        work outputs. Moreover, FCOS works much better than
   fication score with the center-ness score, these points are                         RetinaNet with single anchor. As for the 2% gain on test-
   pushed to the left side of the plot (i.e., their scores are re-                     dev, besides the performance gain brought by the compo-
   duced), as shown in Fig. 7 (right). As a result, these low-                         nents in Table 8, we conjecture that different training details
   quality bounding boxes are much more likely to be filtered                          (e.g., learning rate schedule) might cause slight differences
   out in post-processing and the final detection performance                          in performance.
   can be improved.                                                                    RetinaNet with Center-ness:

                                                                                  10
                                           1.0                                                                                 1.0

                                           0.8                                                                                 0.8
             IOU with Ground-truth Boxes

                                                                                                 IOU with Ground-truth Boxes
                                           0.6                                                                                 0.6

                                           0.4                                                                                 0.4

                                           0.2                                                                                 0.2

                                           0.0                                                                                 0.0
                                                 0.0   0.2     0.4          0.6     0.8   1.0                                        0.0   0.2          0.4         0.6         0.8   1.0
                                                             classification_score                                                             classification_score * center-ness

 Figure 7 – Without (left) or with (right) the proposed center-ness. A point in the figure denotes a detected bounding box. The dashed line
 is the line y = x. As shown in the figure (right), after multiplying the classification scores with the center-ness scores, the low-quality
 boxes (under the line y = x) are pushed to the left side of the plot. It suggests that the scores of these boxes are reduced substantially.

   Method               C5 /P5 GN Scalar IoU             AP                                                        thank Chaorui Deng for HRNet based FCOS and his sug-
   RetinaNet (#A=1)      C5                             32.5                                                       gestion of positioning the center-ness branch with box re-
   RetinaNet (#A=9)      C5                             35.7                                                       gression.
   FCOS (pure)           C5                             35.7
   FCOS                  P5                             35.8
   FCOS                  P5       X                     36.3                                                       References
   FCOS                  P5       X       X             36.4                                                                   [1] https://github.com/yqyao/FCOS_PLUS, 2019.
   FCOS                  P5       X       X        X    36.6
                                                                                                                               [2] Lokesh Boominathan, Srinivas SS Kruthiventi, and
 Table 8 – Ablation study on MS-COCO minival. “#A” is the
                                                                                                                                   R Venkatesh Babu. Crowdnet: A deep convolutional
 number of anchor boxes per location in RetinaNet. “IOU” is
                                                                                                                                   network for dense crowd counting. In Proc. ACM Int. Conf.
 IOU loss. “Scalar” denotes whether to use scalars in exp. All
                                                                                                                                   Multimedia, pages 640–644. ACM, 2016.
 experiments are conducted with the same settings.
                                                                                                                               [3] Yu Chen, Chunhua Shen, Xiu-Shen Wei, Lingqiao Liu, and
                                                                                                                                   Jian Yang. Adversarial PoseNet: A structure-aware convo-
                                                                                                                                   lutional network for human pose estimation. In Proc. IEEE
                                                                                                                                   Int. Conf. Comp. Vis., 2017.
   Center-ness cannot be directly used in RetinaNet with
multiple anchor boxes per location because one location on                                                                     [4] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li,
                                                                                                                                   and Li Fei-Fei. ImageNet: A large-scale hierarchical im-
feature maps has only one center-ness score but different
                                                                                                                                   age database. In Proc. IEEE Conf. Comp. Vis. Patt. Recogn.,
anchor boxes on the same location require different “center-                                                                       pages 248–255. IEEE, 2009.
ness” (note that center-ness is also used as “soft” thresholds
                                                                                                                               [5] Cheng-Yang Fu, Wei Liu, Ananth Ranga, Ambrish Tyagi,
for positive/negative samples).                                                                                                    and Alexander Berg. DSSD: Deconvolutional single shot de-
   For anchor-based RetinaNet, the IoU score between an-                                                                           tector. arXiv preprint arXiv:1701.06659, 2017.
chor boxes and ground-truth boxes may serve as an alterna-                                                                     [6] Ross Girshick. Fast R-CNN. In Proc. IEEE Conf. Comp. Vis.
tive of “center-ness”.                                                                                                             Patt. Recogn., pages 1440–1448, 2015.
Positive samples overlap with RetinaNet:                                                                                       [7] Ross Girshick, Ilija Radosavovic, Georgia Gkioxari, Piotr
   We want to highlight that center-ness comes into play                                                                           Dollár, and Kaiming He. Detectron. https://github.
only when testing. When training, all locations within                                                                             com/facebookresearch/detectron, 2018.
ground-truth boxes are marked as positive samples. As a                                                                        [8] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.
result, FCOS can use more foreground locations to train the                                                                        Deep residual learning for image recognition. In Proc. IEEE
regressor and thus yield more accurate bounding-boxes.                                                                             Conf. Comp. Vis. Patt. Recogn., pages 770–778, 2016.
                                                                                                                               [9] Tong He, Chunhua Shen, Zhi Tian, Dong Gong, Changming
                                                                                                                                   Sun, and Youliang Yan. Knowledge adaptation for efficient
Acknowledgments. We would like to thank the author of                                                                              semantic segmentation. In Proc. IEEE Conf. Comp. Vis. Patt.
[1] for the tricks of center sampling and GIoU. We also                                                                            Recogn., June 2019.

                                                                                                11
 Figure 8 – Some detection results on minival split. ResNet-50 is used as the backbone. As shown in the figure, FCOS works well with
 a wide range of objects including crowded, occluded, highly overlapped, extremely small and very large objects.

[10] Tong He, Zhi Tian, Weilin Huang, Chunhua Shen, Yu Qiao,                  Bharath Hariharan, and Serge Belongie. Feature pyramid
     and Changming Sun. An end-to-end textspotter with explicit               networks for object detection. In Proc. IEEE Conf. Comp.
     alignment and attention. In Proc. IEEE Conf. Comp. Vis.                  Vis. Patt. Recogn., pages 2117–2125, 2017.
     Patt. Recogn., pages 5020–5029, 2018.                               [15] Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, and
[11] Jonathan Huang, Vivek Rathod, Chen Sun, Menglong Zhu,                    Piotr Dollár. Focal loss for dense object detection. In Proc.
     Anoop Korattikara, Alireza Fathi, Ian Fischer, Zbigniew Wo-              IEEE Conf. Comp. Vis. Patt. Recogn., pages 2980–2988,
     jna, Yang Song, Sergio Guadarrama, et al. Speed/accuracy                 2017.
     trade-offs for modern convolutional object detectors. In            [16] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,
     Proc. IEEE Conf. Comp. Vis. Patt. Recogn., pages 7310–                   Pietro Perona, Deva Ramanan, Piotr Dollár, and Lawrence
     7311, 2017.                                                              Zitnick. Microsoft COCO: Common objects in context. In
[12] Lichao Huang, Yi Yang, Yafeng Deng, and Yinan Yu. Dense-                 Proc. Eur. Conf. Comp. Vis., pages 740–755. Springer, 2014.
     box: Unifying landmark localization with end to end object          [17] Fayao Liu, Chunhua Shen, Guosheng Lin, and Ian Reid.
     detection. arXiv preprint arXiv:1509.04874, 2015.                        Learning depth from single monocular images using deep
[13] Hei Law and Jia Deng. Cornernet: Detecting objects as                    convolutional neural fields. IEEE Trans. Pattern Anal. Mach.
     paired keypoints. In Proc. Eur. Conf. Comp. Vis., pages 734–             Intell., 2016.
     750, 2018.                                                          [18] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian
[14] Tsung-Yi Lin, Piotr Dollár, Ross Girshick, Kaiming He,                  Szegedy, Scott Reed, Cheng-Yang Fu, and Alexander C

                                                                    12
     Berg. SSD: Single shot multibox detector. In Proc. Eur.
     Conf. Comp. Vis., pages 21–37. Springer, 2016.
[19] Yifan Liu, Ke Chen, Chris Liu, Zengchang Qin, Zhenbo Luo,
     and Jingdong Wang. Structured knowledge distillation for
     semantic segmentation. In Proc. IEEE Conf. Comp. Vis. Patt.
     Recogn., June 2019.
[20] Jonathan Long, Evan Shelhamer, and Trevor Darrell. Fully
     convolutional networks for semantic segmentation. In Proc.
     IEEE Conf. Comp. Vis. Patt. Recogn., pages 3431–3440,
     2015.
[21] Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali
     Farhadi. You only look once: Unified, real-time object de-
     tection. In Proc. IEEE Conf. Comp. Vis. Patt. Recogn., pages
     779–788, 2016.
[22] Joseph Redmon and Ali Farhadi. YOLO9000: better, faster,
     stronger. In Proc. IEEE Conf. Comp. Vis. Patt. Recogn.,
     pages 7263–7271, 2017.
[23] Joseph Redmon and Ali Farhadi. Yolov3: An incremental
     improvement. arXiv preprint arXiv:1804.02767, 2018.
[24] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.
     Faster R-CNN: Towards real-time object detection with re-
     gion proposal networks. In Proc. Adv. Neural Inf. Process.
     Syst., pages 91–99, 2015.
[25] Abhinav Shrivastava, Rahul Sukthankar, Jitendra Malik, and
     Abhinav Gupta. Beyond skip connections: Top-down mod-
     ulation for object detection. In Proc. IEEE Conf. Comp. Vis.
     Patt. Recogn., 2017.
[26] Ke Sun, Bin Xiao, Dong Liu, and Jingdong Wang. Deep
     high-resolution representation learning for human pose esti-
     mation. In Proc. IEEE Conf. Comp. Vis. Patt. Recogn., 2019.
[27] Christian Szegedy, Sergey Ioffe, Vincent Vanhoucke, and
     Alexander A Alemi. Inception-v4, inception-resnet and the
     impact of residual connections on learning. In Proc. National
     Conf. Artificial Intell., 2017.
[28] Zhi Tian, Tong He, Chunhua Shen, and Youliang Yan. De-
     coders matter for semantic segmentation: Data-dependent
     decoding enables flexible feature aggregation. In Proc. IEEE
     Conf. Comp. Vis. Patt. Recogn., pages 3126–3135, 2019.
[29] Yuxin Wu and Kaiming He. Group normalization. In Proc.
     Eur. Conf. Comp. Vis., pages 3–19, 2018.
[30] Saining Xie, Ross Girshick, Piotr Dollár, Zhuowen Tu, and
     Kaiming He. Aggregated residual transformations for deep
     neural networks. In Proc. IEEE Conf. Comp. Vis. Patt.
     Recogn., pages 1492–1500, 2017.
[31] Wei Yin, Yifan Liu, Chunhua Shen, and Youliang Yan. En-
     forcing geometric constraints of virtual normal for depth pre-
     diction. In Proc. IEEE Int. Conf. Comp. Vis., 2019.
[32] Jiahui Yu, Yuning Jiang, Zhangyang Wang, Zhimin Cao, and
     Thomas Huang. Unitbox: An advanced object detection net-
     work. In Proc. ACM Int. Conf. Multimedia, pages 516–520.
     ACM, 2016.
[33] Xinyu Zhou, Cong Yao, He Wen, Yuzhi Wang, Shuchang
     Zhou, Weiran He, and Jiajun Liang. EAST: an efficient and
     accurate scene text detector. In Proc. IEEE Conf. Comp. Vis.
     Patt. Recogn., pages 5551–5560, 2017.
[34] Chenchen Zhu, Yihui He, and Marios Savvides. Feature se-
     lective anchor-free module for single-shot object detection.
     In Proc. IEEE Conf. Comp. Vis. Patt. Recogn., June 2019.

                                                                      13
