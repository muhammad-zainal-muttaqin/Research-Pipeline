---
source_id: 012
bibtex_key: girshick2014rcnn
title: Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation
year: 2014
domain_theme: Fondasi RGB
verified_pdf: 12_R-CNN.pdf
char_count: 203261
---

Rich feature hierarchies for accurate object detection and semantic segmentation
                                                                                               Tech report (v5)

                                                                  Ross Girshick Jeff Donahue Trevor Darrell Jitendra Malik
                                                                                        UC Berkeley
                                                                          {rbg,jdonahue,trevor,malik}@eecs.berkeley.edu
arXiv:1311.2524v5 [cs.CV] 22 Oct 2014

                                                                 Abstract                                                   R-CNN: Regions with CNN features
                                                                                                                                          warped region            aeroplane? no.
                                                                                                                                                                         ..
                                            Object detection performance, as measured on the                                                                              .
                                                                                                                                                                   person? yes.
                                        canonical PASCAL VOC dataset, has plateaued in the last                                                                          ..
                                                                                                                                                            CNN           .
                                        few years. The best-performing methods are complex en-                                                                     tvmonitor? no.
                                        semble systems that typically combine multiple low-level                1. Input   2. Extract region     3. Compute        4. Classify
                                        image features with high-level context. In this paper, we                image     proposals (~2k)      CNN features         regions
                                        propose a simple and scalable detection algorithm that im-             Figure 1: Object detection system overview. Our system (1)
                                        proves mean average precision (mAP) by more than 30%                   takes an input image, (2) extracts around 2000 bottom-up region
                                        relative to the previous best result on VOC 2012—achieving             proposals, (3) computes features for each proposal using a large
                                        a mAP of 53.3%. Our approach combines two key insights:                convolutional neural network (CNN), and then (4) classifies each
                                        (1) one can apply high-capacity convolutional neural net-              region using class-specific linear SVMs. R-CNN achieves a mean
                                        works (CNNs) to bottom-up region proposals in order to                 average precision (mAP) of 53.7% on PASCAL VOC 2010. For
                                                                                                               comparison, [39] reports 35.1% mAP using the same region pro-
                                        localize and segment objects and (2) when labeled training
                                                                                                               posals, but with a spatial pyramid and bag-of-visual-words ap-
                                        data is scarce, supervised pre-training for an auxiliary task,
                                                                                                               proach. The popular deformable part models perform at 33.4%.
                                        followed by domain-specific fine-tuning, yields a significant          On the 200-class ILSVRC2013 detection dataset, R-CNN’s
                                        performance boost. Since we combine region proposals                   mAP is 31.4%, a large improvement over OverFeat [34], which
                                        with CNNs, we call our method R-CNN: Regions with CNN                  had the previous best result at 24.3%.
                                        features. We also compare R-CNN to OverFeat, a recently
                                        proposed sliding-window detector based on a similar CNN                archical, multi-stage processes for computing features that
                                        architecture. We find that R-CNN outperforms OverFeat                  are even more informative for visual recognition.
                                        by a large margin on the 200-class ILSVRC2013 detection                    Fukushima’s “neocognitron” [19], a biologically-
                                        dataset. Source code for the complete system is available at           inspired hierarchical and shift-invariant model for pattern
                                        http://www.cs.berkeley.edu/˜rbg/rcnn.                                  recognition, was an early attempt at just such a process.
                                                                                                               The neocognitron, however, lacked a supervised training
                                        1. Introduction                                                        algorithm. Building on Rumelhart et al. [33], LeCun et
                                                                                                               al. [26] showed that stochastic gradient descent via back-
                                           Features matter. The last decade of progress on various             propagation was effective for training convolutional neural
                                        visual recognition tasks has been based considerably on the            networks (CNNs), a class of models that extend the neocog-
                                        use of SIFT [29] and HOG [7]. But if we look at perfor-                nitron.
                                        mance on the canonical visual recognition task, PASCAL                     CNNs saw heavy use in the 1990s (e.g., [27]), but then
                                        VOC object detection [15], it is generally acknowledged                fell out of fashion with the rise of support vector machines.
                                        that progress has been slow during 2010-2012, with small               In 2012, Krizhevsky et al. [25] rekindled interest in CNNs
                                        gains obtained by building ensemble systems and employ-                by showing substantially higher image classification accu-
                                        ing minor variants of successful methods.                              racy on the ImageNet Large Scale Visual Recognition Chal-
                                           SIFT and HOG are blockwise orientation histograms,                  lenge (ILSVRC) [9, 10]. Their success resulted from train-
                                        a representation we could associate roughly with complex               ing a large CNN on 1.2 million labeled images, together
                                        cells in V1, the first cortical area in the primate visual path-       with a few twists on LeCun’s CNN (e.g., max(x, 0) rectify-
                                        way. But we also know that recognition occurs several                  ing non-linearities and “dropout” regularization).
                                        stages downstream, which suggests that there might be hier-                The significance of the ImageNet result was vigorously

                                                                                                           1
debated during the ILSVRC 2012 workshop. The central                 is scarce and the amount currently available is insufficient
issue can be distilled to the following: To what extent do           for training a large CNN. The conventional solution to this
the CNN classification results on ImageNet generalize to             problem is to use unsupervised pre-training, followed by su-
object detection results on the PASCAL VOC Challenge?                pervised fine-tuning (e.g., [35]). The second principle con-
    We answer this question by bridging the gap between              tribution of this paper is to show that supervised pre-training
image classification and object detection. This paper is the         on a large auxiliary dataset (ILSVRC), followed by domain-
first to show that a CNN can lead to dramatically higher ob-         specific fine-tuning on a small dataset (PASCAL), is an
ject detection performance on PASCAL VOC as compared                 effective paradigm for learning high-capacity CNNs when
to systems based on simpler HOG-like features. To achieve            data is scarce. In our experiments, fine-tuning for detection
this result, we focused on two problems: localizing objects          improves mAP performance by 8 percentage points. After
with a deep network and training a high-capacity model               fine-tuning, our system achieves a mAP of 54% on VOC
with only a small quantity of annotated detection data.              2010 compared to 33% for the highly-tuned, HOG-based
    Unlike image classification, detection requires localiz-         deformable part model (DPM) [17, 20]. We also point read-
ing (likely many) objects within an image. One approach              ers to contemporaneous work by Donahue et al. [12], who
frames localization as a regression problem. However, work           show that Krizhevsky’s CNN can be used (without fine-
from Szegedy et al. [38], concurrent with our own, indi-             tuning) as a blackbox feature extractor, yielding excellent
cates that this strategy may not fare well in practice (they         performance on several recognition tasks including scene
report a mAP of 30.5% on VOC 2007 compared to the                    classification, fine-grained sub-categorization, and domain
58.5% achieved by our method). An alternative is to build a          adaptation.
sliding-window detector. CNNs have been used in this way                 Our system is also quite efficient. The only class-specific
for at least two decades, typically on constrained object cat-       computations are a reasonably small matrix-vector product
egories, such as faces [32, 40] and pedestrians [35]. In order       and greedy non-maximum suppression. This computational
to maintain high spatial resolution, these CNNs typically            property follows from features that are shared across all cat-
only have two convolutional and pooling layers. We also              egories and that are also two orders of magnitude lower-
considered adopting a sliding-window approach. However,              dimensional than previously used region features (cf. [39]).
units high up in our network, which has five convolutional               Understanding the failure modes of our approach is also
layers, have very large receptive fields (195 × 195 pixels)          critical for improving it, and so we report results from the
and strides (32×32 pixels) in the input image, which makes           detection analysis tool of Hoiem et al. [23]. As an im-
precise localization within the sliding-window paradigm an           mediate consequence of this analysis, we demonstrate that
open technical challenge.                                            a simple bounding-box regression method significantly re-
    Instead, we solve the CNN localization problem by oper-          duces mislocalizations, which are the dominant error mode.
ating within the “recognition using regions” paradigm [21],              Before developing technical details, we note that because
which has been successful for both object detection [39] and         R-CNN operates on regions it is natural to extend it to the
semantic segmentation [5]. At test time, our method gener-           task of semantic segmentation. With minor modifications,
ates around 2000 category-independent region proposals for           we also achieve competitive results on the PASCAL VOC
the input image, extracts a fixed-length feature vector from         segmentation task, with an average segmentation accuracy
each proposal using a CNN, and then classifies each region           of 47.9% on the VOC 2011 test set.
with category-specific linear SVMs. We use a simple tech-
nique (affine image warping) to compute a fixed-size CNN
                                                                     2. Object detection with R-CNN
input from each region proposal, regardless of the region’s              Our object detection system consists of three modules.
shape. Figure 1 presents an overview of our method and               The first generates category-independent region proposals.
highlights some of our results. Since our system combines            These proposals define the set of candidate detections avail-
region proposals with CNNs, we dub the method R-CNN:                 able to our detector. The second module is a large convo-
Regions with CNN features.                                           lutional neural network that extracts a fixed-length feature
    In this updated version of this paper, we provide a head-        vector from each region. The third module is a set of class-
to-head comparison of R-CNN and the recently proposed                specific linear SVMs. In this section, we present our design
OverFeat [34] detection system by running R-CNN on the               decisions for each module, describe their test-time usage,
200-class ILSVRC2013 detection dataset. OverFeat uses a              detail how their parameters are learned, and show detection
sliding-window CNN for detection and until now was the               results on PASCAL VOC 2010-12 and on ILSVRC2013.
best performing method on ILSVRC2013 detection. We
show that R-CNN significantly outperforms OverFeat, with             2.1. Module design
a mAP of 31.4% versus 24.3%.                                         Region proposals. A variety of recent papers offer meth-
    A second challenge faced in detection is that labeled data       ods for generating category-independent region proposals.

                                                                 2
                                                                      are low-dimensional when compared to other common ap-
                                                                      proaches, such as spatial pyramids with bag-of-visual-word
                                                                      encodings. The features used in the UVA detection system
                                                                      [39], for example, are two orders of magnitude larger than
   aeroplane        bicycle           bird             car            ours (360k vs. 4k-dimensional).
  Figure 2: Warped training samples from VOC 2007 train.                 The result of such sharing is that the time spent com-
                                                                      puting region proposals and features (13s/image on a GPU
Examples include: objectness [1], selective search [39],              or 53s/image on a CPU) is amortized over all classes. The
category-independent object proposals [14], constrained               only class-specific computations are dot products between
parametric min-cuts (CPMC) [5], multi-scale combinatorial             features and SVM weights and non-maximum suppression.
grouping [3], and Cireşan et al. [6], who detect mitotic cells       In practice, all dot products for an image are batched into
by applying a CNN to regularly-spaced square crops, which             a single matrix-matrix product. The feature matrix is typi-
are a special case of region proposals. While R-CNN is ag-            cally 2000 × 4096 and the SVM weight matrix is 4096 × N ,
nostic to the particular region proposal method, we use se-           where N is the number of classes.
lective search to enable a controlled comparison with prior              This analysis shows that R-CNN can scale to thousands
detection work (e.g., [39, 41]).                                      of object classes without resorting to approximate tech-
                                                                      niques, such as hashing. Even if there were 100k classes,
Feature extraction. We extract a 4096-dimensional fea-                the resulting matrix multiplication takes only 10 seconds on
ture vector from each region proposal using the Caffe [24]            a modern multi-core CPU. This efficiency is not merely the
implementation of the CNN described by Krizhevsky et                  result of using region proposals and shared features. The
al. [25]. Features are computed by forward propagating                UVA system, due to its high-dimensional features, would
a mean-subtracted 227 × 227 RGB image through five con-               be two orders of magnitude slower while requiring 134GB
volutional layers and two fully connected layers. We refer            of memory just to store 100k linear predictors, compared to
readers to [24, 25] for more network architecture details.            just 1.5GB for our lower-dimensional features.
   In order to compute features for a region proposal, we                It is also interesting to contrast R-CNN with the recent
must first convert the image data in that region into a form          work from Dean et al. on scalable detection using DPMs
that is compatible with the CNN (its architecture requires            and hashing [8]. They report a mAP of around 16% on VOC
inputs of a fixed 227 × 227 pixel size). Of the many possi-           2007 at a run-time of 5 minutes per image when introducing
ble transformations of our arbitrary-shaped regions, we opt           10k distractor classes. With our approach, 10k detectors can
for the simplest. Regardless of the size or aspect ratio of the       run in about a minute on a CPU, and because no approxi-
candidate region, we warp all pixels in a tight bounding box          mations are made mAP would remain at 59% (Section 3.2).
around it to the required size. Prior to warping, we dilate the
tight bounding box so that at the warped size there are ex-           2.3. Training
actly p pixels of warped image context around the original            Supervised pre-training. We discriminatively pre-trained
box (we use p = 16). Figure 2 shows a random sampling                 the CNN on a large auxiliary dataset (ILSVRC2012 clas-
of warped training regions. Alternatives to warping are dis-          sification) using image-level annotations only (bounding-
cussed in Appendix A.                                                 box labels are not available for this data). Pre-training
2.2. Test-time detection                                              was performed using the open source Caffe CNN library
                                                                      [24]. In brief, our CNN nearly matches the performance
   At test time, we run selective search on the test image            of Krizhevsky et al. [25], obtaining a top-1 error rate 2.2
to extract around 2000 region proposals (we use selective             percentage points higher on the ILSVRC2012 classification
search’s “fast mode” in all experiments). We warp each                validation set. This discrepancy is due to simplifications in
proposal and forward propagate it through the CNN in or-              the training process.
der to compute features. Then, for each class, we score
each extracted feature vector using the SVM trained for that          Domain-specific fine-tuning. To adapt our CNN to the
class. Given all scored regions in an image, we apply a               new task (detection) and the new domain (warped proposal
greedy non-maximum suppression (for each class indepen-               windows), we continue stochastic gradient descent (SGD)
dently) that rejects a region if it has an intersection-over-         training of the CNN parameters using only warped region
union (IoU) overlap with a higher scoring selected region             proposals. Aside from replacing the CNN’s ImageNet-
larger than a learned threshold.                                      specific 1000-way classification layer with a randomly ini-
                                                                      tialized (N + 1)-way classification layer (where N is the
Run-time analysis. Two properties make detection effi-                number of object classes, plus 1 for background), the CNN
cient. First, all CNN parameters are shared across all cate-          architecture is unchanged. For VOC, N = 20 and for
gories. Second, the feature vectors computed by the CNN               ILSVRC2013, N = 200. We treat all region proposals with

                                                                  3
≥ 0.5 IoU overlap with a ground-truth box as positives for           densely sampled SIFT, Extended OpponentSIFT, and RGB-
that box’s class and the rest as negatives. We start SGD at          SIFT descriptors, each vector quantized with 4000-word
a learning rate of 0.001 (1/10th of the initial pre-training         codebooks. Classification is performed with a histogram
rate), which allows fine-tuning to make progress while not           intersection kernel SVM. Compared to their multi-feature,
clobbering the initialization. In each SGD iteration, we uni-        non-linear kernel SVM approach, we achieve a large im-
formly sample 32 positive windows (over all classes) and             provement in mAP, from 35.1% to 53.7% mAP, while also
96 background windows to construct a mini-batch of size              being much faster (Section 2.2). Our method achieves sim-
128. We bias the sampling towards positive windows be-               ilar performance (53.3% mAP) on VOC 2011/12 test.
cause they are extremely rare compared to background.
                                                                     2.5. Results on ILSVRC2013 detection
Object category classifiers. Consider training a binary
classifier to detect cars. It’s clear that an image region               We ran R-CNN on the 200-class ILSVRC2013 detection
tightly enclosing a car should be a positive example. Simi-          dataset using the same system hyperparameters that we used
larly, it’s clear that a background region, which has nothing        for PASCAL VOC. We followed the same protocol of sub-
to do with cars, should be a negative example. Less clear            mitting test results to the ILSVRC2013 evaluation server
is how to label a region that partially overlaps a car. We re-       only twice, once with and once without bounding-box re-
solve this issue with an IoU overlap threshold, below which          gression.
regions are defined as negatives. The overlap threshold, 0.3,            Figure 3 compares R-CNN to the entries in the ILSVRC
was selected by a grid search over {0, 0.1, . . . , 0.5} on a        2013 competition and to the post-competition OverFeat re-
validation set. We found that selecting this threshold care-         sult [34]. R-CNN achieves a mAP of 31.4%, which is sig-
fully is important. Setting it to 0.5, as in [39], decreased         nificantly ahead of the second-best result of 24.3% from
mAP by 5 points. Similarly, setting it to 0 decreased mAP            OverFeat. To give a sense of the AP distribution over
by 4 points. Positive examples are defined simply to be the          classes, box plots are also presented and a table of per-
ground-truth bounding boxes for each class.                          class APs follows at the end of the paper in Table 8. Most
    Once features are extracted and training labels are ap-          of the competing submissions (OverFeat, NEC-MU, UvA-
plied, we optimize one linear SVM per class. Since the               Euvision, Toronto A, and UIUC-IFP) used convolutional
training data is too large to fit in memory, we adopt the            neural networks, indicating that there is significant nuance
standard hard negative mining method [17, 37]. Hard neg-             in how CNNs can be applied to object detection, leading to
ative mining converges quickly and in practice mAP stops             greatly varying outcomes.
increasing after only a single pass over all images.                     In Section 4, we give an overview of the ILSVRC2013
    In Appendix B we discuss why the positive and negative           detection dataset and provide details about choices that we
examples are defined differently in fine-tuning versus SVM           made when running R-CNN on it.
training. We also discuss the trade-offs involved in training
detection SVMs rather than simply using the outputs from
the final softmax layer of the fine-tuned CNN.                       3. Visualization, ablation, and modes of error
2.4. Results on PASCAL VOC 2010-12                                   3.1. Visualizing learned features
    Following the PASCAL VOC best practices [15], we                    First-layer filters can be visualized directly and are easy
validated all design decisions and hyperparameters on the            to understand [25]. They capture oriented edges and oppo-
VOC 2007 dataset (Section 3.2). For final results on the             nent colors. Understanding the subsequent layers is more
VOC 2010-12 datasets, we fine-tuned the CNN on VOC                   challenging. Zeiler and Fergus present a visually attrac-
2012 train and optimized our detection SVMs on VOC 2012              tive deconvolutional approach in [42]. We propose a simple
trainval. We submitted test results to the evaluation server         (and complementary) non-parametric method that directly
only once for each of the two major algorithm variants (with         shows what the network learned.
and without bounding-box regression).                                   The idea is to single out a particular unit (feature) in the
    Table 1 shows complete results on VOC 2010. We com-              network and use it as if it were an object detector in its own
pare our method against four strong baselines, including             right. That is, we compute the unit’s activations on a large
SegDPM [18], which combines DPM detectors with the                   set of held-out region proposals (about 10 million), sort the
output of a semantic segmentation system [4] and uses ad-            proposals from highest to lowest activation, perform non-
ditional inter-detector context and image-classifier rescor-         maximum suppression, and then display the top-scoring re-
ing. The most germane comparison is to the UVA system                gions. Our method lets the selected unit “speak for itself”
from Uijlings et al. [39], since our systems use the same re-        by showing exactly which inputs it fires on. We avoid aver-
gion proposal algorithm. To classify regions, their method           aging in order to see different visual modes and gain insight
builds a four-level spatial pyramid and populates it with            into the invariances computed by the unit.

                                                                 4
VOC 2010 test aero bike bird boat bottle bus car cat chair cow table dog horse mbike person plant sheep sofa train tv mAP
DPM v5 [20]† 49.2 53.8 13.1 15.3 35.5 53.4 49.7 27.0 17.2 28.8 14.7 17.8 46.4 51.2    47.7 10.8 34.2 20.7 43.8 38.3 33.4
UVA [39]        56.2 42.4 15.3 12.6 21.8 49.3 36.8 46.1 12.9 32.1 30.0 36.5 43.5 52.9 32.9 15.3 41.1 31.8 47.0 44.8 35.1
Regionlets [41] 65.0 48.9 25.9 24.6 24.5 56.1 54.5 51.2 17.0 28.9 30.2 35.8 40.2 55.7 43.5 14.3 43.9 32.6 54.0 45.9 39.7
SegDPM [18]† 61.4 53.4 25.6 25.2 35.5 51.7 50.6 50.8 19.3 33.8 26.8 40.4 48.3 54.4    47.1 14.8 38.7 35.0 52.8 43.1 40.4
R-CNN           67.1 64.1 46.7 32.0 30.5 56.4 57.2 65.9 27.0 47.3 40.9 66.6 57.8 65.9 53.6 26.7 56.5 38.1 52.8 50.2 50.2
R-CNN BB        71.8 65.8 53.0 36.8 35.9 59.7 60.0 69.9 27.9 50.6 41.4 70.0 62.0 69.0 58.1 29.5 59.4 39.3 61.2 52.4 53.7

Table 1: Detection average precision (%) on VOC 2010 test. R-CNN is most directly comparable to UVA and Regionlets since all
methods use selective search region proposals. Bounding-box regression (BB) is described in Section C. At publication time, SegDPM
was the top-performer on the PASCAL VOC leaderboard. † DPM and SegDPM use context rescoring not used by the other methods.

                                  ILSVRC2013 detection test set mAP                                                                                ILSVRC2013 detection test set class AP box plots
                                                                                                                               100
      *R−CNN BB                                 31.4%

                                                                                                 average precision (AP) in %
                                                                                                                                90
      *OverFeat (2)                      24.3%                                                                                  80
  UvA−Euvision                          22.6%                                                                                   70
                                                                                                                                60
        *NEC−MU                         20.9%
                                                                                                                                50
      *OverFeat (1)                    19.4%                                                                                    40
         Toronto A              11.5%                                                                                           30
      SYSU_Vision               10.5%
                                                                                                                                20
                                                                                                                                10
      GPU_UCLA                  9.8%
                                                                                                                                 0

                                                                                                                                                       UvA−Euvision

                                                                                                                                                                                                                   SYSU_Vision
                                                                                                                                                                                 *OverFeat (1)
             Delta        6.1%                                                                                                         *R−CNN BB

                                                                                                                                                                                                                                 GPU_UCLA
                                                                                                                                                                      *NEC−MU

                                                                                                                                                                                                                                                            UIUC−IFP
                                                               competition result

                                                                                                                                                                                                       Toronto A
        UIUC−IFP 1.0%                                          post competition result

                                                                                                                                                                                                                                              Delta
                      0            20             40         60          80          100
                                   mean average precision (mAP) in %

Figure 3: (Left) Mean average precision on the ILSVRC2013 detection test set. Methods preceeded by * use outside training data
(images and labels from the ILSVRC classification dataset in all cases). (Right) Box plots for the 200 average precision values per
method. A box plot for the post-competition OverFeat result is not shown because per-class APs are not yet available (per-class APs for
R-CNN are in Table 8 and also included in the tech report source uploaded to arXiv.org; see R-CNN-ILSVRC2013-APs.txt). The red
line marks the median AP, the box bottom and top are the 25th and 75th percentiles. The whiskers extend to the min and max AP of each
method. Each AP is plotted as a green dot over the whiskers (best viewed digitally with zoom).

1.0          1.0          0.9            0.9           0.9    0.9        0.9        0.9    0.9                                   0.9                  0.9                  0.9                   0.9               0.9                  0.9           0.9

1.0          0.9          0.9            0.8           0.8    0.8        0.7        0.7    0.7                                   0.7                  0.7                  0.7                   0.7               0.7                  0.6           0.6

1.0          0.8          0.7            0.7           0.7    0.7        0.7        0.7    0.7                                   0.7                  0.7                  0.7                   0.7               0.7                  0.6           0.6

1.0          0.9          0.8            0.8           0.8    0.7        0.7        0.7    0.7                                   0.7                  0.7                  0.7                   0.7               0.7                  0.7           0.7

1.0          1.0          0.9            0.9           0.9    0.8        0.8        0.8    0.8                                   0.8                  0.8                  0.8                   0.8               0.8                  0.8           0.8

1.0          0.9          0.8            0.8           0.8    0.7        0.7        0.7    0.7                                   0.7                  0.7                  0.7                   0.7               0.7                  0.7           0.7

Figure 4: Top regions for six pool5 units. Receptive fields and activation values are drawn in white. Some units are aligned to concepts,
such as people (row 1) or text (4). Other units capture texture and material properties, such as dot arrays (2) and specular reflections (6).

                                                                                           5
VOC 2007 test   aero bike bird boat bottle bus car cat chair cow table dog horse mbike person plant sheep sofa train tv mAP
R-CNN pool5     51.8 60.2 36.4 27.8 23.2 52.8 60.6 49.2 18.3 47.8 44.3 40.8 56.6 58.7   42.4 23.4 46.1 36.7 51.3 55.7 44.2
R-CNN fc6       59.3 61.8 43.1 34.0 25.1 53.1 60.6 52.8 21.7 47.8 42.7 47.8 52.5 58.5   44.6 25.6 48.3 34.0 53.1 58.0 46.2
R-CNN fc7       57.6 57.9 38.5 31.8 23.7 51.2 58.9 51.4 20.0 50.5 40.9 46.0 51.6 55.9   43.3 23.3 48.1 35.3 51.0 57.4 44.7
R-CNN FT pool5 58.2 63.3 37.9 27.6 26.1 54.1 66.9 51.4 26.7 55.5 43.4 43.1 57.7 59.0    45.8 28.1 50.8 40.6 53.1 56.4 47.3
R-CNN FT fc6    63.5 66.0 47.9 37.7 29.9 62.5 70.2 60.2 32.0 57.9 47.0 53.5 60.1 64.2   52.2 31.3 55.0 50.0 57.7 63.0 53.1
R-CNN FT fc7    64.2 69.7 50.0 41.9 32.0 62.6 71.0 60.7 32.7 58.5 46.5 56.1 60.6 66.8   54.2 31.5 52.8 48.9 57.9 64.7 54.2
R-CNN FT fc7 BB 68.1 72.8 56.8 43.0 36.8 66.3 74.2 67.6 34.4 63.5 54.5 61.2 69.1 68.6   58.7 33.4 62.9 51.1 62.5 64.8 58.5
DPM v5 [20]       33.2 60.3 10.2 16.1 27.3 54.3 58.2 23.0 20.0 24.1 26.7 12.7 58.1        48.2   43.2   12.0   21.1 36.1 46.0 43.5 33.7
DPM ST [28]       23.8 58.2 10.5 8.5 27.1 50.4 52.0 7.3 19.2 22.8 18.1 8.0 55.9           44.8   32.4   13.3   15.9 22.8 46.2 44.9 29.1
DPM HSC [31]      32.2 58.3 11.5 16.3 30.6 49.9 54.8 23.5 21.5 27.7 34.0 13.7 58.1        51.6   39.9   12.4   23.5 34.4 47.4 45.2 34.3

Table 2: Detection average precision (%) on VOC 2007 test. Rows 1-3 show R-CNN performance without fine-tuning. Rows 4-6 show
results for the CNN pre-trained on ILSVRC 2012 and then fine-tuned (FT) on VOC 2007 trainval. Row 7 includes a simple bounding-box
regression (BB) stage that reduces localization errors (Section C). Rows 8-10 present DPM methods as a strong baseline. The first uses
only HOG, while the next two use different feature learning approaches to augment or replace HOG.

VOC 2007 test  aero bike bird boat bottle bus car cat chair cow table dog horse mbike person plant sheep sofa train tv mAP
R-CNN T-Net    64.2 69.7 50.0 41.9 32.0 62.6 71.0 60.7 32.7 58.5 46.5 56.1 60.6 66.8   54.2 31.5 52.8 48.9 57.9 64.7 54.2
R-CNN T-Net BB 68.1 72.8 56.8 43.0 36.8 66.3 74.2 67.6 34.4 63.5 54.5 61.2 69.1 68.6   58.7 33.4 62.9 51.1 62.5 64.8 58.5
R-CNN O-Net    71.6 73.5 58.1 42.2 39.4 70.7 76.0 74.5 38.7 71.0 56.9 74.5 67.9 69.6   59.3 35.7 62.1 64.0 66.5 71.2 62.2
R-CNN O-Net BB 73.4 77.0 63.4 45.4 44.6 75.1 78.1 79.8 40.5 73.7 62.2 79.4 78.1 73.1   64.2 35.6 66.8 67.2 70.4 71.1 66.0

Table 3: Detection average precision (%) on VOC 2007 test for two different CNN architectures. The first two rows are results from
Table 2 using Krizhevsky et al.’s architecture (T-Net). Rows three and four use the recently proposed 16-layer architecture from Simonyan
and Zisserman (O-Net) [43].

    We visualize units from layer pool5 , which is the max-               Layer fc6 is fully connected to pool5 . To compute fea-
pooled output of the network’s fifth and final convolutional           tures, it multiplies a 4096×9216 weight matrix by the pool5
layer. The pool5 feature map is 6 × 6 × 256 = 9216-                    feature map (reshaped as a 9216-dimensional vector) and
dimensional. Ignoring boundary effects, each pool5 unit has            then adds a vector of biases. This intermediate vector is
a receptive field of 195×195 pixels in the original 227×227            component-wise half-wave rectified (x ← max(0, x)).
pixel input. A central pool5 unit has a nearly global view,               Layer fc7 is the final layer of the network. It is imple-
while one near the edge has a smaller, clipped support.                mented by multiplying the features computed by fc6 by a
    Each row in Figure 4 displays the top 16 activations for           4096 × 4096 weight matrix, and similarly adding a vector
a pool5 unit from a CNN that we fine-tuned on VOC 2007                 of biases and applying half-wave rectification.
trainval. Six of the 256 functionally unique units are visu-              We start by looking at results from the CNN without
alized (Appendix D includes more). These units were se-                fine-tuning on PASCAL, i.e. all CNN parameters were
lected to show a representative sample of what the network             pre-trained on ILSVRC 2012 only. Analyzing performance
learns. In the second row, we see a unit that fires on dog             layer-by-layer (Table 2 rows 1-3) reveals that features from
faces and dot arrays. The unit corresponding to the third row          fc7 generalize worse than features from fc6 . This means
is a red blob detector. There are also detectors for human             that 29%, or about 16.8 million, of the CNN’s parameters
faces and more abstract patterns such as text and triangular           can be removed without degrading mAP. More surprising is
structures with windows. The network appears to learn a                that removing both fc7 and fc6 produces quite good results
representation that combines a small number of class-tuned             even though pool5 features are computed using only 6% of
features together with a distributed representation of shape,          the CNN’s parameters. Much of the CNN’s representational
texture, color, and material properties. The subsequent fully          power comes from its convolutional layers, rather than from
connected layer fc6 has the ability to model a large set of            the much larger densely connected layers. This finding sug-
compositions of these rich features.                                   gests potential utility in computing a dense feature map, in
                                                                       the sense of HOG, of an arbitrary-sized image by using only
3.2. Ablation studies
                                                                       the convolutional layers of the CNN. This representation
Performance layer-by-layer, without fine-tuning. To un-                would enable experimentation with sliding-window detec-
derstand which layers are critical for detection performance,          tors, including DPM, on top of pool5 features.
we analyzed results on the VOC 2007 dataset for each of the
CNN’s last three layers. Layer pool5 was briefly described             Performance layer-by-layer, with fine-tuning. We now
in Section 3.1. The final two layers are summarized below.             look at results from our CNN after having fine-tuned its pa-

                                                                   6
rameters on VOC 2007 trainval. The improvement is strik-                  To use O-Net in R-CNN, we downloaded the pub-
ing (Table 2 rows 4-6): fine-tuning increases mAP by 8.0              licly available pre-trained network weights for the
percentage points to 54.2%. The boost from fine-tuning is             VGG ILSVRC 16 layers model from the Caffe Model
much larger for fc6 and fc7 than for pool5 , which suggests           Zoo.1 We then fine-tuned the network using the same pro-
that the pool5 features learned from ImageNet are general             tocol as we used for T-Net. The only difference was to use
and that most of the improvement is gained from learning              smaller minibatches (24 examples) as required in order to
domain-specific non-linear classifiers on top of them.                fit within GPU memory. The results in Table 3 show that R-
                                                                      CNN with O-Net substantially outperforms R-CNN with T-
Comparison to recent feature learning methods. Rela-                  Net, increasing mAP from 58.5% to 66.0%. However there
tively few feature learning methods have been tried on PAS-           is a considerable drawback in terms of compute time, with
CAL VOC detection. We look at two recent approaches that              the forward pass of O-Net taking roughly 7 times longer
build on deformable part models. For reference, we also in-           than T-Net.
clude results for the standard HOG-based DPM [20].
   The first DPM feature learning method, DPM ST [28],                3.4. Detection error analysis
augments HOG features with histograms of “sketch token”                  We applied the excellent detection analysis tool from
probabilities. Intuitively, a sketch token is a tight distri-         Hoiem et al. [23] in order to reveal our method’s error
bution of contours passing through the center of an image             modes, understand how fine-tuning changes them, and to
patch. Sketch token probabilities are computed at each pixel          see how our error types compare with DPM. A full sum-
by a random forest that was trained to classify 35 × 35 pixel         mary of the analysis tool is beyond the scope of this pa-
patches into one of 150 sketch tokens or background.                  per and we encourage readers to consult [23] to understand
   The second method, DPM HSC [31], replaces HOG with                 some finer details (such as “normalized AP”). Since the
histograms of sparse codes (HSC). To compute an HSC,                  analysis is best absorbed in the context of the associated
sparse code activations are solved for at each pixel using            plots, we present the discussion within the captions of Fig-
a learned dictionary of 100 7 × 7 pixel (grayscale) atoms.            ure 5 and Figure 6.
The resulting activations are rectified in three ways (full and
both half-waves), spatially pooled, unit `2 normalized, and           3.5. Bounding-box regression
then power transformed (x ← sign(x)|x|α ).                               Based on the error analysis, we implemented a sim-
   All R-CNN variants strongly outperform the three DPM               ple method to reduce localization errors. Inspired by the
baselines (Table 2 rows 8-10), including the two that use             bounding-box regression employed in DPM [17], we train a
feature learning. Compared to the latest version of DPM,              linear regression model to predict a new detection window
which uses only HOG features, our mAP is more than 20                 given the pool5 features for a selective search region pro-
percentage points higher: 54.2% vs. 33.7%—a 61% rela-                 posal. Full details are given in Appendix C. Results in Ta-
tive improvement. The combination of HOG and sketch to-               ble 1, Table 2, and Figure 5 show that this simple approach
kens yields 2.5 mAP points over HOG alone, while HSC                  fixes a large number of mislocalized detections, boosting
improves over HOG by 4 mAP points (when compared                      mAP by 3 to 4 points.
internally to their private DPM baselines—both use non-
public implementations of DPM that underperform the open              3.6. Qualitative results
source version [20]). These methods achieve mAPs of                       Qualitative detection results on ILSVRC2013 are pre-
29.1% and 34.3%, respectively.                                        sented in Figure 8 and Figure 9 at the end of the paper. Each
                                                                      image was sampled randomly from the val2 set and all de-
3.3. Network architectures
                                                                      tections from all detectors with a precision greater than 0.5
   Most results in this paper use the network architecture            are shown. Note that these are not curated and give a re-
from Krizhevsky et al. [25]. However, we have found that              alistic impression of the detectors in action. More qualita-
the choice of architecture has a large effect on R-CNN de-            tive results are presented in Figure 10 and Figure 11, but
tection performance. In Table 3 we show results on VOC                these have been curated. We selected each image because it
2007 test using the 16-layer deep network recently proposed           contained interesting, surprising, or amusing results. Here,
by Simonyan and Zisserman [43]. This network was one of               also, all detections at precision greater than 0.5 are shown.
the top performers in the recent ILSVRC 2014 classifica-
tion challenge. The network has a homogeneous structure               4. The ILSVRC2013 detection dataset
consisting of 13 layers of 3 × 3 convolution kernels, with
                                                                         In Section 2 we presented results on the ILSVRC2013
five max pooling layers interspersed, and topped with three
                                                                      detection dataset. This dataset is less homogeneous than
fully-connected layers. We refer to this network as “O-Net”
for OxfordNet and the baseline as “T-Net” for TorontoNet.               1 https://github.com/BVLC/caffe/wiki/Model-Zoo

                                                                  7
                                    R−CNN fc6: sensitivity and impact                                                                R−CNN FT fc7: sensitivity and impact                                                               R−CNN FT fc7 BB: sensitivity and impact                                       DPM voc−release5: sensitivity and impact

                          0.8                                                                                                  0.8                                                0.766
                                                                                                                                                                                                                                  0.8                           0.786           0.779                           0.8
                                                         0.720                                                                                                                                    0.723                                         0.731                   0.709           0.720
                                                                                               0.677                                                            0.701                                     0.685                                         0.676
                                                                                                                                                                                          0.672
   normalized AP

                                                                                                               normalized AP

                                                                                                                                                                                                                  normalized AP

                                                                                                                                                                                                                                                                                                normalized AP
                                         0.612                                         0.606           0.609                                                            0.634                                                           0.633
                          0.6                                                                                                  0.6 0.593                                                                                          0.6                                                                           0.6
                                                 0.557                                                                                                                                                                                                  0.542
                                 0.516                                                                                                                                  0.498                                                                                                                                                                 0.487
                                                                                                                                                                                                                                                                        0.484
                                                                                                                                                                                          0.442 0.429                                                                           0.453                                                                 0.453
                          0.4                    0.420                                                                         0.4                                                                                                0.4                                                                           0.4                                           0.391 0.388
                                                                                                                                                                                                                                                                0.385                   0.368
                                                                                       0.344 0.351                                                                                0.335                   0.325                                                                                                               0.339 0.347
                                                                                                                                                                                                                                                                                                                      0.297
                                                                                                       0.244                                                                                                                                                                                                                          0.216
                          0.2            0.212           0.201                                                                 0.2                                                                                                0.2           0.211                                                           0.2
                                                                                                                                                                0.179
                                                                                                                                                                                                                                                                                                                              0.132                   0.126 0.137
                                                                                                                                                                                                                                                                                                                                                                    0.094
                                                                                                                                                                                                                                                                                                                                              0.056
                            0                                                                                                   0                                                                                                  0                                                                             0
                                    occ      trn    size asp view part                                                                occ                             trn     size asp view part                                           occ      trn    size asp view part                                            occ      trn    size asp view part

Figure 6: Sensitivity to object characteristics. Each plot shows the mean (over classes) normalized AP (see [23]) for the highest and
lowest performing subsets within six different object characteristics (occlusion, truncation, bounding-box area, aspect ratio, viewpoint, part
visibility). We show plots for our method (R-CNN) with and without fine-tuning (FT) and bounding-box regression (BB) as well as for
DPM voc-release5. Overall, fine-tuning does not reduce sensitivity (the difference between max and min), but does substantially improve
both the highest and lowest performing subsets for nearly all characteristics. This indicates that fine-tuning does more than simply improve
the lowest performing subsets for aspect ratio and bounding-box area, as one might conjecture based on how we warp network inputs.
Instead, fine-tuning improves robustness for all characteristics including occlusion, truncation, viewpoint, and part visibility.
                                  R−CNN fc6: animals                                           R−CNN FT fc7: animals                                               R−CNN FT fc7 BB: animals
                          100                                                          100                                                                      100                                                                val and test splits are drawn from the same image distribu-
percentage of each type

                                                             percentage of each type

                                                                                                                                      percentage of each type

                           80                                                           80                                                                       80                                                                tion. These images are scene-like and similar in complexity
                           60                                                           60                                                                       60
                                                                                                                                                                                                                                   (number of objects, amount of clutter, pose variability, etc.)
                           40                                                           40                                                                       40
                                                                                                                                                                                                                                   to PASCAL VOC images. The val and test splits are exhaus-
                                  Loc                                                            Loc                                                                        Loc
                                  Sim                                                            Sim                                                                        Sim                                                    tively annotated, meaning that in each image all instances
                           20     Oth                                                   20       Oth                                                             20         Oth
                                  BG                                                             BG                                                                         BG
                                                                                                                                                                                                                                   from all 200 classes are labeled with bounding boxes. The
                            0                            0                                                             0
                            25      100 400 1600 6400 25
                                   total false positives
                                                                                                  100 400 1600 6400 25
                                                                                                 total false positives
                                                                                                                                                                             100 400 1600 6400
                                                                                                                                                                            total false positives
                                                                                                                                                                                                                                   train set, in contrast, is drawn from the ILSVRC2013 clas-
                                  R−CNN fc6: furniture                                         R−CNN FT fc7: furniture                                             R−CNN FT fc7 BB: furniture                                      sification image distribution. These images have more vari-
                          100                                                          100                                                                      100
                                                                                                                                                                                                                                   able complexity with a skew towards images of a single cen-
percentage of each type

                                                             percentage of each type

                                                                                                                                      percentage of each type

                           80                                                           80                                                                       80
                                                                                                                                                                                                                                   tered object. Unlike val and test, the train images (due to
                           60                                                           60                                                                       60
                                                                                                                                                                                                                                   their large number) are not exhaustively annotated. In any
                           40
                                  Loc
                                                                                        40
                                                                                                 Loc
                                                                                                                                                                 40
                                                                                                                                                                            Loc                                                    given train image, instances from the 200 classes may or
                                  Sim                                                            Sim                                                                        Sim
                           20
                                  Oth
                                                                                        20
                                                                                                 Oth
                                                                                                                                                                 20
                                                                                                                                                                            Oth                                                    may not be labeled. In addition to these image sets, each
                                  BG                                                             BG                                                                         BG
                            0
                            25      100 400 1600 6400 25
                                                         0
                                                                                                  100 400 1600 6400 25
                                                                                                                       0
                                                                                                                                                                             100 400 1600 6400
                                                                                                                                                                                                                                   class has an extra set of negative images. Negative images
                                   total false positives                                         total false positives                                                      total false positives
                                                                                                                                                                                                                                   are manually checked to validate that they do not contain
Figure 5: Distribution of top-ranked false positive (FP) types.                                                                                                                                                                    any instances of their associated class. The negative im-
Each plot shows the evolving distribution of FP types as more FPs                                                                                                                                                                  age sets were not used in this work. More information on
are considered in order of decreasing score. Each FP is catego-                                                                                                                                                                    how ILSVRC was collected and annotated can be found in
rized into 1 of 4 types: Loc—poor localization (a detection with                                                                                                                                                                   [11, 36].
an IoU overlap with the correct class between 0.1 and 0.5, or a du-
plicate); Sim—confusion with a similar category; Oth—confusion                                                                                                                                                                        The nature of these splits presents a number of choices
with a dissimilar object category; BG—a FP that fired on back-                                                                                                                                                                     for training R-CNN. The train images cannot be used for
ground. Compared with DPM (see [23]), significantly more of                                                                                                                                                                        hard negative mining, because annotations are not exhaus-
our errors result from poor localization, rather than confusion with                                                                                                                                                               tive. Where should negative examples come from? Also,
background or other object classes, indicating that the CNN fea-
                                                                                                                                                                                                                                   the train images have different statistics than val and test.
tures are much more discriminative than HOG. Loose localiza-
tion likely results from our use of bottom-up region proposals and
                                                                                                                                                                                                                                   Should the train images be used at all, and if so, to what
the positional invariance learned from pre-training the CNN for                                                                                                                                                                    extent? While we have not thoroughly evaluated a large
whole-image classification. Column three shows how our simple                                                                                                                                                                      number of choices, we present what seemed like the most
bounding-box regression method fixes many localization errors.                                                                                                                                                                     obvious path based on previous experience.
                                                                                                                                                                                                                                       Our general strategy is to rely heavily on the val set and
PASCAL VOC, requiring choices about how to use it. Since
                                                                                                                                                                                                                                   use some of the train images as an auxiliary source of pos-
these decisions are non-trivial, we cover them in this sec-
                                                                                                                                                                                                                                   itive examples. To use val for both training and valida-
tion.
                                                                                                                                                                                                                                   tion, we split it into roughly equally sized “val1 ” and “val2 ”
                                                                                                                                                                                                                                   sets. Since some classes have very few examples in val (the
4.1. Dataset overview
                                                                                                                                                                                                                                   smallest has only 31 and half have fewer than 110), it is
   The ILSVRC2013 detection dataset is split into three                                                                                                                                                                            important to produce an approximately class-balanced par-
sets: train (395,918), val (20,121), and test (40,152), where                                                                                                                                                                      tition. To do this, a large number of candidate splits were
the number of images in each set is in parentheses. The                                                                                                                                                                            generated and the one with the smallest maximum relative

                                                                                                                                                                                                              8
class imbalance was selected.2 Each candidate split was                        train because the annotations are not exhaustive. The ex-
generated by clustering val images using their class counts                    tra sets of verified negative images were not used. The
as features, followed by a randomized local search that may                    bounding-box regressors were trained on val1 .
improve the split balance. The particular split used here has
a maximum relative imbalance of about 11% and a median                         4.4. Validation and evaluation
relative imbalance of 4%. The val1 /val2 split and code used                       Before submitting results to the evaluation server, we
to produce them will be publicly available to allow other re-                  validated data usage choices and the effect of fine-tuning
searchers to compare their methods on the val splits used in                   and bounding-box regression on the val2 set using the train-
this report.                                                                   ing data described above. All system hyperparameters (e.g.,
                                                                               SVM C hyperparameters, padding used in region warp-
4.2. Region proposals                                                          ing, NMS thresholds, bounding-box regression hyperpa-
    We followed the same region proposal approach that was                     rameters) were fixed at the same values used for PAS-
used for detection on PASCAL. Selective search [39] was                        CAL. Undoubtedly some of these hyperparameter choices
run in “fast mode” on each image in val1 , val2 , and test (but                are slightly suboptimal for ILSVRC, however the goal of
not on images in train). One minor modification was re-                        this work was to produce a preliminary R-CNN result on
quired to deal with the fact that selective search is not scale                ILSVRC without extensive dataset tuning. After selecting
invariant and so the number of regions produced depends                        the best choices on val2 , we submitted exactly two result
on the image resolution. ILSVRC image sizes range from                         files to the ILSVRC2013 evaluation server. The first sub-
very small to a few that are several mega-pixels, and so we                    mission was without bounding-box regression and the sec-
resized each image to a fixed width (500 pixels) before run-                   ond submission was with bounding-box regression. For
ning selective search. On val, selective search resulted in an                 these submissions, we expanded the SVM and bounding-
average of 2403 region proposals per image with a 91.6%                        box regressor training sets to use val+train1k and val, re-
recall of all ground-truth bounding boxes (at 0.5 IoU thresh-                  spectively. We used the CNN that was fine-tuned on
old). This recall is notably lower than in PASCAL, where                       val1 +train1k to avoid re-running fine-tuning and feature
it is approximately 98%, indicating significant room for im-                   computation.
provement in the region proposal stage.
                                                                               4.5. Ablation study
4.3. Training data                                                                Table 4 shows an ablation study of the effects of differ-
                                                                               ent amounts of training data, fine-tuning, and bounding-
   For training data, we formed a set of images and boxes
                                                                               box regression. A first observation is that mAP on val2
that includes all selective search and ground-truth boxes
                                                                               matches mAP on test very closely. This gives us confi-
from val1 together with up to N ground-truth boxes per
                                                                               dence that mAP on val2 is a good indicator of test set per-
class from train (if a class has fewer than N ground-truth
                                                                               formance. The first result, 20.9%, is what R-CNN achieves
boxes in train, then we take all of them). We’ll call this
                                                                               using a CNN pre-trained on the ILSVRC2012 classifica-
dataset of images and boxes val1 +trainN . In an ablation
                                                                               tion dataset (no fine-tuning) and given access to the small
study, we show mAP on val2 for N ∈ {0, 500, 1000} (Sec-
                                                                               amount of training data in val1 (recall that half of the classes
tion 4.5).
                                                                               in val1 have between 15 and 55 examples). Expanding
   Training data is required for three procedures in R-CNN:                    the training set to val1 +trainN improves performance to
(1) CNN fine-tuning, (2) detector SVM training, and (3)                        24.1%, with essentially no difference between N = 500
bounding-box regressor training. CNN fine-tuning was run                       and N = 1000. Fine-tuning the CNN using examples from
for 50k SGD iteration on val1 +trainN using the exact same                     just val1 gives a modest improvement to 26.5%, however
settings as were used for PASCAL. Fine-tuning on a sin-                        there is likely significant overfitting due to the small number
gle NVIDIA Tesla K20 took 13 hours using Caffe. For                            of positive training examples. Expanding the fine-tuning
SVM training, all ground-truth boxes from val1 +trainN                         set to val1 +train1k , which adds up to 1000 positive exam-
were used as positive examples for their respective classes.                   ples per class from the train set, helps significantly, boosting
Hard negative mining was performed on a randomly se-                           mAP to 29.7%. Bounding-box regression improves results
lected subset of 5000 images from val1 . An initial experi-                    to 31.0%, which is a smaller relative gain that what was ob-
ment indicated that mining negatives from all of val1 , versus                 served in PASCAL.
a 5000 image subset (roughly half of it), resulted in only a
0.5 percentage point drop in mAP, while cutting SVM train-                     4.6. Relationship to OverFeat
ing time in half. No negative examples were taken from
                                                                                  There is an interesting relationship between R-CNN and
   2 Relative imbalance is measured as |a − b|/(a + b) where a and b are       OverFeat: OverFeat can be seen (roughly) as a special case
class counts in each half of the split.                                        of R-CNN. If one were to replace selective search region

                                                                           9
     test set       val2    val2           val2          val2          val2          val2          test          test
 SVM training set val1 val1 +train.5k val1 +train1k val1 +train1k val1 +train1k val1 +train1k val+train1k val+train1k
CNN fine-tuning set n/a      n/a            n/a          val1     val1 +train1k val1 +train1k val1 +train1k val1 +train1k
   bbox reg set      n/a     n/a            n/a           n/a           n/a          val1           n/a           val
CNN feature layer fc6        fc6            fc6           fc7           fc7           fc7           fc7           fc7
      mAP           20.9    24.1           24.1          26.5          29.7          31.0          30.2          31.4
   median AP        17.7    21.0           21.4          24.8          29.2          29.6          29.0          30.3
               Table 4: ILSVRC2013 ablation study of data usage choices, fine-tuning, and bounding-box regression.

proposals with a multi-scale pyramid of regular square re-          gion’s shape and computes CNN features directly on the
gions and change the per-class bounding-box regressors to           warped window, exactly as we did for detection. However,
a single bounding-box regressor, then the systems would             these features ignore the non-rectangular shape of the re-
be very similar (modulo some potentially significant differ-        gion. Two regions might have very similar bounding boxes
ences in how they are trained: CNN detection fine-tuning,           while having very little overlap. Therefore, the second strat-
using SVMs, etc.). It is worth noting that OverFeat has             egy (fg) computes CNN features only on a region’s fore-
a significant speed advantage over R-CNN: it is about 9x            ground mask. We replace the background with the mean
faster, based on a figure of 2 seconds per image quoted from        input so that background regions are zero after mean sub-
[34]. This speed comes from the fact that OverFeat’s slid-          traction. The third strategy (full+fg) simply concatenates
ing windows (i.e., region proposals) are not warped at the          the full and fg features; our experiments validate their com-
image level and therefore computation can be easily shared          plementarity.
between overlapping windows. Sharing is implemented by
running the entire network in a convolutional fashion over                       full R-CNN     fg R-CNN      full+fg R-CNN
arbitrary-sized inputs. Speeding up R-CNN should be pos-              O2 P [4]    fc6    fc7    fc6   fc7      fc6      fc7
sible in a variety of ways and remains as future work.                 46.4      43.0 42.5     43.7 42.1      47.9     45.8
                                                                    Table 5: Segmentation mean accuracy (%) on VOC 2011 vali-
5. Semantic segmentation                                            dation. Column 1 presents O2 P; 2-7 use our CNN pre-trained on
                                                                    ILSVRC 2012.
    Region classification is a standard technique for seman-
tic segmentation, allowing us to easily apply R-CNN to the
PASCAL VOC segmentation challenge. To facilitate a di-
rect comparison with the current leading semantic segmen-           Results on VOC 2011. Table 5 shows a summary of our
tation system (called O2 P for “second-order pooling”) [4],         results on the VOC 2011 validation set compared with O2 P.
we work within their open source framework. O2 P uses               (See Appendix E for complete per-category results.) Within
CPMC to generate 150 region proposals per image and then            each feature computation strategy, layer fc6 always outper-
predicts the quality of each region, for each class, using          forms fc7 and the following discussion refers to the fc6 fea-
support vector regression (SVR). The high performance of            tures. The fg strategy slightly outperforms full, indicating
their approach is due to the quality of the CPMC regions            that the masked region shape provides a stronger signal,
and the powerful second-order pooling of multiple feature           matching our intuition. However, full+fg achieves an aver-
types (enriched variants of SIFT and LBP). We also note             age accuracy of 47.9%, our best result by a margin of 4.2%
that Farabet et al. [16] recently demonstrated good results         (also modestly outperforming O2 P), indicating that the con-
on several dense scene labeling datasets (not including PAS-        text provided by the full features is highly informative even
CAL) using a CNN as a multi-scale per-pixel classifier.             given the fg features. Notably, training the 20 SVRs on our
    We follow [2, 4] and extend the PASCAL segmentation             full+fg features takes an hour on a single core, compared to
training set to include the extra annotations made available        10+ hours for training on O2 P features.
by Hariharan et al. [22]. Design decisions and hyperparam-              In Table 6 we present results on the VOC 2011 test
eters were cross-validated on the VOC 2011 validation set.          set, comparing our best-performing method, fc6 (full+fg),
Final test results were evaluated only once.                        against two strong baselines. Our method achieves the high-
                                                                    est segmentation accuracy for 11 out of 21 categories, and
CNN features for segmentation. We evaluate three strate-            the highest overall segmentation accuracy of 47.9%, aver-
gies for computing features on CPMC regions, all of which           aged across categories (but likely ties with the O2 P result
begin by warping the rectangular window around the re-              under any reasonable margin of error). Still better perfor-
gion to 227 × 227. The first strategy (full) ignores the re-        mance could likely be achieved by fine-tuning.

                                                               10
VOC 2011 test              bg aero bike bird boat bottle bus car cat chair cow table dog horse mbike person plant sheep sofa train tv mean
R&P [2]                   83.4 46.8 18.9 36.6 31.2 42.7 57.3 47.4 44.1 8.1 39.4 36.1 36.3 49.5 48.3   50.7 26.3 47.2 22.1 42.0 43.2 40.8
O2 P [4]                  85.4 69.7 22.3 45.2 44.4 46.9 66.7 57.8 56.2 13.5 46.1 32.3 41.2 59.1 55.3  51.0 36.2 50.4 27.8 46.9 44.6 47.6
ours (full+fg R-CNN fc6 ) 84.2 66.9 23.7 58.3 37.4 55.4 73.3 58.7 56.5 9.7 45.5 29.5 49.3 40.1 57.8   53.9 33.8 60.7 22.7 47.1 41.3 47.9

Table 6: Segmentation accuracy (%) on VOC 2011 test. We compare against two strong baselines: the “Regions and Parts” (R&P)
method of [2] and the second-order pooling (O2 P) method of [4]. Without any fine-tuning, our CNN achieves top segmentation perfor-
mance, outperforming R&P and roughly matching O2 P.

6. Conclusion
    In recent years, object detection performance had stag-
nated. The best performing systems were complex en-
sembles combining multiple low-level image features with
high-level context from object detectors and scene classi-
fiers. This paper presents a simple and scalable object de-
tection algorithm that gives a 30% relative improvement
over the best previous results on PASCAL VOC 2012.
    We achieved this performance through two insights. The
first is to apply high-capacity convolutional neural net-
works to bottom-up region proposals in order to localize                 (A)     (B)      (C)      (D)     (A)     (B)      (C)      (D)
and segment objects. The second is a paradigm for train-                Figure 7: Different object proposal transformations. (A) the
ing large CNNs when labeled training data is scarce. We                 original object proposal at its actual scale relative to the trans-
show that it is highly effective to pre-train the network—              formed CNN inputs; (B) tightest square with context; (C) tight-
with supervision—for a auxiliary task with abundant data                est square without context; (D) warp. Within each column and
(image classification) and then to fine-tune the network for            example proposal, the top row corresponds to p = 0 pixels of con-
the target task where data is scarce (detection). We conjec-            text padding while the bottom row has p = 16 pixels of context
ture that the “supervised pre-training/domain-specific fine-            padding.
tuning” paradigm will be highly effective for a variety of
data-scarce vision problems.
    We conclude by noting that it is significant that we
achieved these results by using a combination of classi-                then scales (isotropically) the image contained in that
cal tools from computer vision and deep learning (bottom-               square to the CNN input size. Figure 7 column (B) shows
up region proposals and convolutional neural networks).                 this transformation. A variant on this method (“tightest
Rather than opposing lines of scientific inquiry, the two are           square without context”) excludes the image content that
natural and inevitable partners.                                        surrounds the original object proposal. Figure 7 column
                                                                        (C) shows this transformation. The second method (“warp”)
Acknowledgments. This research was supported in part                    anisotropically scales each object proposal to the CNN in-
by DARPA Mind’s Eye and MSEE programs, by NSF                           put size. Figure 7 column (D) shows the warp transforma-
awards IIS-0905647, IIS-1134072, and IIS-1212798,                       tion.
MURI N000014-10-1-0933, and by support from Toyota.
The GPUs used in this research were generously donated                     For each of these transformations, we also consider in-
by the NVIDIA Corporation.                                              cluding additional image context around the original object
                                                                        proposal. The amount of context padding (p) is defined as a
                                                                        border size around the original object proposal in the trans-
Appendix                                                                formed input coordinate frame. Figure 7 shows p = 0 pix-
                                                                        els in the top row of each example and p = 16 pixels in
A. Object proposal transformations                                      the bottom row. In all methods, if the source rectangle ex-
                                                                        tends beyond the image, the missing data is replaced with
   The convolutional neural network used in this work re-               the image mean (which is then subtracted before inputing
quires a fixed-size input of 227 × 227 pixels. For detec-               the image into the CNN). A pilot set of experiments showed
tion, we consider object proposals that are arbitrary image             that warping with context padding (p = 16 pixels) outper-
rectangles. We evaluated two approaches for transforming                formed the alternatives by a large margin (3-5 mAP points).
object proposals into valid CNN inputs.                                 Obviously more alternatives are possible, including using
   The first method (“tightest square with context”) en-                replication instead of mean padding. Exhaustive evaluation
closes each object proposal inside the tightest square and              of these alternatives is left as future work.

                                                                   11
B. Positive vs. negative examples and softmax                           ter fine-tuning. We conjecture that with some additional
                                                                        tweaks to fine-tuning the remaining performance gap may
    Two design choices warrant further discussion. The first            be closed. If true, this would simplify and speed up R-CNN
is: Why are positive and negative examples defined differ-              training with no loss in detection performance.
ently for fine-tuning the CNN versus training the object de-
tection SVMs? To review the definitions briefly, for fine-
tuning we map each object proposal to the ground-truth in-              C. Bounding-box regression
stance with which it has maximum IoU overlap (if any) and
                                                                           We use a simple bounding-box regression stage to im-
label it as a positive for the matched ground-truth class if the
                                                                        prove localization performance. After scoring each selec-
IoU is at least 0.5. All other proposals are labeled “back-
                                                                        tive search proposal with a class-specific detection SVM,
ground” (i.e., negative examples for all classes). For train-
                                                                        we predict a new bounding box for the detection using a
ing SVMs, in contrast, we take only the ground-truth boxes
                                                                        class-specific bounding-box regressor. This is similar in
as positive examples for their respective classes and label
                                                                        spirit to the bounding-box regression used in deformable
proposals with less than 0.3 IoU overlap with all instances
                                                                        part models [17]. The primary difference between the two
of a class as a negative for that class. Proposals that fall
                                                                        approaches is that here we regress from features computed
into the grey zone (more than 0.3 IoU overlap, but are not
                                                                        by the CNN, rather than from geometric features computed
ground truth) are ignored.
                                                                        on the inferred DPM part locations.
    Historically speaking, we arrived at these definitions be-
                                                                           The input to our training algorithm is a set of N train-
cause we started by training SVMs on features computed
                                                                        ing pairs {(P i , Gi )}i=1,...,N , where P i = (Pxi , Pyi , Pwi , Phi )
by the ImageNet pre-trained CNN, and so fine-tuning was
not a consideration at that point in time. In that setup, we            specifies the pixel coordinates of the center of proposal P i ’s
found that our particular label definition for training SVMs            bounding box together with P i ’s width and height in pixels.
was optimal within the set of options we evaluated (which               Hence forth, we drop the superscript i unless it is needed.
included the setting we now use for fine-tuning). When we               Each ground-truth bounding box G is specified in the same
started using fine-tuning, we initially used the same positive          way: G = (Gx , Gy , Gw , Gh ). Our goal is to learn a trans-
and negative example definition as we were using for SVM                formation that maps a proposed box P to a ground-truth box
training. However, we found that results were much worse                G.
than those obtained using our current definition of positives              We parameterize the transformation in terms of four
and negatives.                                                          functions dx (P ), dy (P ), dw (P ), and dh (P ). The first
    Our hypothesis is that this difference in how positives             two specify a scale-invariant translation of the center of
and negatives are defined is not fundamentally important                P ’s bounding box, while the second two specify log-space
and arises from the fact that fine-tuning data is limited.              translations of the width and height of P ’s bounding box.
Our current scheme introduces many “jittered” examples                  After learning these functions, we can transform an input
(those proposals with overlap between 0.5 and 1, but not                proposal P into a predicted ground-truth box Ĝ by apply-
ground truth), which expands the number of positive exam-               ing the transformation
ples by approximately 30x. We conjecture that this large
set is needed when fine-tuning the entire network to avoid                                    Ĝx = Pw dx (P ) + Px                        (1)
overfitting. However, we also note that using these jittered
                                                                                              Ĝy = Ph dy (P ) + Py                        (2)
examples is likely suboptimal because the network is not
being fine-tuned for precise localization.                                                   Ĝw = Pw exp(dw (P ))                         (3)
    This leads to the second issue: Why, after fine-tuning,                                   Ĝh = Ph exp(dh (P )).                       (4)
train SVMs at all? It would be cleaner to simply apply the
last layer of the fine-tuned network, which is a 21-way soft-
max regression classifier, as the object detector. We tried                 Each function d? (P ) (where ? is one of x, y, h, w) is
this and found that performance on VOC 2007 dropped                     modeled as a linear function of the pool5 features of pro-
from 54.2% to 50.9% mAP. This performance drop likely                   posal P , denoted by φ5 (P ). (The dependence of φ5 (P )
arises from a combination of several factors including that             on the image data is implicitly assumed.) Thus we have
the definition of positive examples used in fine-tuning does            d? (P ) = wT? φ5 (P ), where w? is a vector of learnable
not emphasize precise localization and the softmax classi-              model parameters. We learn w? by optimizing the regu-
fier was trained on randomly sampled negative examples                  larized least squares objective (ridge regression):
rather than on the subset of “hard negatives” used for SVM
training.                                                                                    N
                                                                                             X                                   2
    This result shows that it’s possible to obtain close to                w? = argmin         (ti? − ŵ?T φ5 (P i ))2 + λ kŵ? k .        (5)
                                                                                      ŵ?
the same level of performance without training SVMs af-                                       i

                                                                   12
The regression targets t? for the training pair (P, G) are de-        F. Analysis of cross-dataset redundancy
fined as
                                                                          One concern when training on an auxiliary dataset is that
                                                                      there might be redundancy between it and the test set. Even
                    tx = (Gx − Px )/Pw                    (6)         though the tasks of object detection and whole-image clas-
                    ty = (Gy − Py )/Ph                    (7)         sification are substantially different, making such cross-set
                   tw = log(Gw /Pw )                      (8)         redundancy much less worrisome, we still conducted a thor-
                                                                      ough investigation that quantifies the extent to which PAS-
                    th = log(Gh /Ph ).                    (9)
                                                                      CAL test images are contained within the ILSVRC 2012
                                                                      training and validation sets. Our findings may be useful to
As a standard regularized least squares problem, this can be          researchers who are interested in using ILSVRC 2012 as
solved efficiently in closed form.                                    training data for the PASCAL image classification task.
    We found two subtle issues while implementing                         We performed two checks for duplicate (and near-
bounding-box regression. The first is that regularization             duplicate) images. The first test is based on exact matches
is important: we set λ = 1000 based on a validation set.              of flickr image IDs, which are included in the VOC 2007
The second issue is that care must be taken when selecting            test annotations (these IDs are intentionally kept secret for
which training pairs (P, G) to use. Intuitively, if P is far          subsequent PASCAL test sets). All PASCAL images, and
from all ground-truth boxes, then the task of transforming            about half of ILSVRC, were collected from flickr.com. This
P to a ground-truth box G does not make sense. Using ex-              check turned up 31 matches out of 4952 (0.63%).
amples like P would lead to a hopeless learning problem.                  The second check uses GIST [30] descriptor matching,
Therefore, we only learn from a proposal P if it is nearby            which was shown in [13] to have excellent performance at
at least one ground-truth box. We implement “nearness” by             near-duplicate image detection in large (> 1 million) image
assigning P to the ground-truth box G with which it has               collections. Following [13], we computed GIST descrip-
maximum IoU overlap (in case it overlaps more than one) if            tors on warped 32 × 32 pixel versions of all ILSVRC 2012
and only if the overlap is greater than a threshold (which we         trainval and PASCAL 2007 test images.
set to 0.6 using a validation set). All unassigned proposals              Euclidean distance nearest-neighbor matching of GIST
are discarded. We do this once for each object class in order         descriptors revealed 38 near-duplicate images (including all
to learn a set of class-specific bounding-box regressors.             31 found by flickr ID matching). The matches tend to vary
    At test time, we score each proposal and predict its new          slightly in JPEG compression level and resolution, and to a
detection window only once. In principle, we could iterate            lesser extent cropping. These findings show that the overlap
this procedure (i.e., re-score the newly predicted bounding           is small, less than 1%. For VOC 2012, because flickr IDs
box, and then predict a new bounding box from it, and so              are not available, we used the GIST matching method only.
on). However, we found that iterating does not improve                Based on GIST matches, 1.5% of VOC 2012 test images
results.                                                              are in ILSVRC 2012 trainval. The slightly higher rate for
                                                                      VOC 2012 is likely due to the fact that the two datasets
D. Additional feature visualizations                                  were collected closer together in time than VOC 2007 and
                                                                      ILSVRC 2012 were.
   Figure 12 shows additional visualizations for 20 pool5
units. For each unit, we show the 24 region proposals that            G. Document changelog
maximally activate that unit out of the full set of approxi-
                                                                         This document tracks the progress of R-CNN. To help
mately 10 million regions in all of VOC 2007 test.
                                                                      readers understand how it has changed over time, here’s a
   We label each unit by its (y, x, channel) position in the
                                                                      brief changelog describing the revisions.
6 × 6 × 256 dimensional pool5 feature map. Within each
channel, the CNN computes exactly the same function of                v1 Initial version.
the input region, with the (y, x) position changing only the
                                                                      v2 CVPR 2014 camera-ready revision. Includes substan-
receptive field.
                                                                      tial improvements in detection performance brought about
                                                                      by (1) starting fine-tuning from a higher learning rate (0.001
E. Per-category segmentation results                                  instead of 0.0001), (2) using context padding when prepar-
                                                                      ing CNN inputs, and (3) bounding-box regression to fix lo-
   In Table 7 we show the per-category segmentation ac-
                                                                      calization errors.
curacy on VOC 2011 val for each of our six segmentation
methods in addition to the O2 P method [4]. These results             v3 Results on the ILSVRC2013 detection dataset and com-
show which methods are strongest across each of the 20                parison with OverFeat were integrated into several sections
PASCAL classes, plus the background class.                            (primarily Section 2 and Section 4).

                                                                 13
VOC 2011 val         bg aero bike bird boat bottle bus car cat chair cow table dog horse mbike person plant sheep sofa train tv mean
O2 P [4]            84.0 69.0 21.7 47.7 42.2 42.4 64.7 65.8 57.4 12.9 37.4 20.5 43.7 35.7 52.7  51.0 35.8 51.0 28.4 59.8 49.7 46.4
full R-CNN fc6      81.3 56.2 23.9 42.9 40.7 38.8 59.2 56.5 53.2 11.4 34.6 16.7 48.1 37.0 51.4  46.0 31.5 44.0 24.3 53.7 51.1 43.0
full R-CNN fc7      81.0 52.8 25.1 43.8 40.5 42.7 55.4 57.7 51.3 8.7 32.5 11.5 48.1 37.0 50.5   46.4 30.2 42.1 21.2 57.7 56.0 42.5
fg R-CNN fc6        81.4 54.1 21.1 40.6 38.7 53.6 59.9 57.2 52.5 9.1 36.5 23.6 46.4 38.1 53.2   51.3 32.2 38.7 29.0 53.0 47.5 43.7
fg R-CNN fc7        80.9 50.1 20.0 40.2 34.1 40.9 59.7 59.8 52.7 7.3 32.1 14.3 48.8 42.9 54.0   48.6 28.9 42.6 24.9 52.2 48.8 42.1
full+fg R-CNN fc6   83.1 60.4 23.2 48.4 47.3 52.6 61.6 60.6 59.1 10.8 45.8 20.9 57.7 43.3 57.4  52.9 34.7 48.7 28.1 60.0 48.6 47.9
full+fg R-CNN fc7   82.3 56.7 20.6 49.9 44.2 43.6 59.3 61.3 57.8 7.7 38.4 15.1 53.4 43.7 50.8   52.0 34.1 47.8 24.7 60.1 55.2 45.7

                             Table 7: Per-category segmentation accuracy (%) on the VOC 2011 validation set.

v4 The softmax vs. SVM results in Appendix B contained                     [13] M. Douze, H. Jégou, H. Sandhawalia, L. Amsaleg, and
an error, which has been fixed. We thank Sergio Guadar-                         C. Schmid. Evaluation of gist descriptors for web-scale im-
rama for helping to identify this issue.                                        age search. In Proc. of the ACM International Conference on
                                                                                Image and Video Retrieval, 2009. 13
v5 Added results using the new 16-layer network architec-                  [14] I. Endres and D. Hoiem. Category independent object pro-
ture from Simonyan and Zisserman [43] to Section 3.3 and                        posals. In ECCV, 2010. 3
Table 3.                                                                   [15] M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn, and
                                                                                A. Zisserman. The PASCAL Visual Object Classes (VOC)
References                                                                      Challenge. IJCV, 2010. 1, 4
                                                                           [16] C. Farabet, C. Couprie, L. Najman, and Y. LeCun. Learning
 [1] B. Alexe, T. Deselaers, and V. Ferrari. Measuring the object-              hierarchical features for scene labeling. TPAMI, 2013. 10
     ness of image windows. TPAMI, 2012. 2                                 [17] P. Felzenszwalb, R. Girshick, D. McAllester, and D. Ra-
 [2] P. Arbeláez, B. Hariharan, C. Gu, S. Gupta, L. Bourdev, and               manan. Object detection with discriminatively trained part
     J. Malik. Semantic segmentation using regions and parts. In                based models. TPAMI, 2010. 2, 4, 7, 12
     CVPR, 2012. 10, 11                                                    [18] S. Fidler, R. Mottaghi, A. Yuille, and R. Urtasun. Bottom-up
 [3] P. Arbeláez, J. Pont-Tuset, J. Barron, F. Marques, and J. Ma-             segmentation for top-down detection. In CVPR, 2013. 4, 5
     lik. Multiscale combinatorial grouping. In CVPR, 2014. 3              [19] K. Fukushima. Neocognitron: A self-organizing neu-
 [4] J. Carreira, R. Caseiro, J. Batista, and C. Sminchisescu. Se-              ral network model for a mechanism of pattern recogni-
     mantic segmentation with second-order pooling. In ECCV,                    tion unaffected by shift in position. Biological cybernetics,
     2012. 4, 10, 11, 13, 14                                                    36(4):193–202, 1980. 1
 [5] J. Carreira and C. Sminchisescu. CPMC: Automatic ob-                  [20] R. Girshick, P. Felzenszwalb, and D. McAllester. Discrimi-
     ject segmentation using constrained parametric min-cuts.                   natively trained deformable part models, release 5. http:
     TPAMI, 2012. 2, 3                                                          //www.cs.berkeley.edu/˜rbg/latent-v5/. 2,
 [6] D. Cireşan, A. Giusti, L. Gambardella, and J. Schmidhu-                   5, 6, 7
     ber. Mitosis detection in breast cancer histology images with         [21] C. Gu, J. J. Lim, P. Arbeláez, and J. Malik. Recognition
     deep neural networks. In MICCAI, 2013. 3                                   using regions. In CVPR, 2009. 2
 [7] N. Dalal and B. Triggs. Histograms of oriented gradients for          [22] B. Hariharan, P. Arbeláez, L. Bourdev, S. Maji, and J. Malik.
     human detection. In CVPR, 2005. 1                                          Semantic contours from inverse detectors. In ICCV, 2011.
 [8] T. Dean, M. A. Ruzon, M. Segal, J. Shlens, S. Vijaya-                      10
     narasimhan, and J. Yagnik. Fast, accurate detection of                [23] D. Hoiem, Y. Chodpathumwan, and Q. Dai. Diagnosing error
     100,000 object classes on a single machine. In CVPR, 2013.                 in object detectors. In ECCV. 2012. 2, 7, 8
     3                                                                     [24] Y. Jia.     Caffe: An open source convolutional archi-
 [9] J. Deng, A. Berg, S. Satheesh, H. Su, A. Khosla, and L. Fei-               tecture for fast feature embedding. http://caffe.
     Fei. ImageNet Large Scale Visual Recognition Competition                   berkeleyvision.org/, 2013. 3
     2012 (ILSVRC2012). http://www.image-net.org/                          [25] A. Krizhevsky, I. Sutskever, and G. Hinton. ImageNet clas-
     challenges/LSVRC/2012/. 1                                                  sification with deep convolutional neural networks. In NIPS,
[10] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-                  2012. 1, 3, 4, 7
     Fei. ImageNet: A large-scale hierarchical image database.             [26] Y. LeCun, B. Boser, J. Denker, D. Henderson, R. Howard,
     In CVPR, 2009. 1                                                           W. Hubbard, and L. Jackel. Backpropagation applied to
[11] J. Deng, O. Russakovsky, J. Krause, M. Bernstein, A. C.                    handwritten zip code recognition. Neural Comp., 1989. 1
     Berg, and L. Fei-Fei. Scalable multi-label annotation. In             [27] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner. Gradient-
     CHI, 2014. 8                                                               based learning applied to document recognition. Proc. of the
[12] J. Donahue, Y. Jia, O. Vinyals, J. Hoffman, N. Zhang,                      IEEE, 1998. 1
     E. Tzeng, and T. Darrell. DeCAF: A Deep Convolutional                 [28] J. J. Lim, C. L. Zitnick, and P. Dollár. Sketch tokens: A
     Activation Feature for Generic Visual Recognition. In ICML,                learned mid-level representation for contour and object de-
     2014. 2                                                                    tection. In CVPR, 2013. 6, 7

                                                                      14
class         AP class               AP class                  AP class                   AP class             AP
accordion    50.8 centipede         30.4 hair spray           13.8 pencil box            11.4 snowplow        69.2
airplane     50.0 chain saw         14.1 hamburger            34.2 pencil sharpener       9.0 soap dispenser  16.8
ant          31.8 chair             19.5 hammer                9.9 perfume               32.8 soccer ball     43.7
antelope     53.8 chime             24.6 hamster              46.0 person                41.7 sofa            16.3
apple        30.9 cocktail shaker   46.2 harmonica            12.6 piano                 20.5 spatula          6.8
armadillo    54.0 coffee maker      21.5 harp                 50.4 pineapple             22.6 squirrel        31.3
artichoke    45.0 computer keyboard 39.6 hat with a wide brim 40.5 ping-pong ball        21.0 starfish        45.1
axe          11.8 computer mouse    21.2 head cabbage         17.4 pitcher               19.2 stethoscope     18.3
baby bed     42.0 corkscrew         24.2 helmet               33.4 pizza                 43.7 stove            8.1
backpack      2.8 cream             29.9 hippopotamus         38.0 plastic bag            6.4 strainer         9.9
bagel        37.5 croquet ball      30.0 horizontal bar        7.0 plate rack            15.2 strawberry      26.8
balance beam 32.6 crutch            23.7 horse                41.7 pomegranate           32.0 stretcher       13.2
banana       21.9 cucumber          22.8 hotdog               28.7 popsicle              21.2 sunglasses      18.8
band aid     17.4 cup or mug        34.0 iPod                 59.2 porcupine             37.2 swimming trunks 9.1
banjo        55.3 diaper            10.1 isopod               19.5 power drill            7.9 swine           45.3
baseball     41.8 digital clock     18.5 jellyfish            23.7 pretzel               24.8 syringe          5.7
basketball   65.3 dishwasher        19.9 koala bear           44.3 printer               21.3 table           21.7
bathing cap  37.2 dog               76.8 ladle                 3.0 puck                  14.1 tape player     21.4
beaker       11.3 domestic cat      44.1 ladybug              58.4 punching bag          29.4 tennis ball     59.1
bear         62.7 dragonfly         27.8 lamp                  9.1 purse                  8.0 tick            42.6
bee          52.9 drum              19.9 laptop               35.4 rabbit                71.0 tie             24.6
bell pepper  38.8 dumbbell          14.1 lemon                33.3 racket                16.2 tiger           61.8
bench        12.7 electric fan      35.0 lion                 51.3 ray                   41.1 toaster         29.2
bicycle      41.1 elephant          56.4 lipstick             23.1 red panda             61.1 traffic light   24.7
binder        6.2 face powder       22.1 lizard               38.9 refrigerator          14.0 train           60.8
bird         70.9 fig               44.5 lobster              32.4 remote control        41.6 trombone        13.8
bookshelf    19.3 filing cabinet    20.6 maillot              31.0 rubber eraser          2.5 trumpet         14.4
bow tie      38.8 flower pot        20.2 maraca               30.1 rugby ball            34.5 turtle          59.1
bow           9.0 flute              4.9 microphone            4.0 ruler                 11.5 tv or monitor   41.7
bowl         26.7 fox               59.3 microwave            40.1 salt or pepper shaker 24.6 unicycle        27.2
brassiere    31.2 french horn       24.2 milk can             33.3 saxophone             40.8 vacuum          19.5
burrito      25.7 frog              64.1 miniskirt            14.9 scorpion              57.3 violin          13.7
bus          57.5 frying pan        21.5 monkey               49.6 screwdriver           10.6 volleyball      59.7
butterfly    88.5 giant panda       42.5 motorcycle           42.2 seal                  20.9 waffle iron     24.0
camel        37.6 goldfish          28.6 mushroom             31.8 sheep                 48.9 washer          39.8
can opener   28.9 golf ball         51.3 nail                  4.5 ski                    9.0 water bottle     8.1
car          44.5 golfcart          47.9 neck brace           31.6 skunk                 57.9 watercraft      40.9
cart         48.0 guacamole         32.3 oboe                 27.5 snail                 36.2 whale           48.6
cattle       32.3 guitar            33.1 orange               38.8 snake                 33.8 wine bottle     31.2
cello        28.9 hair dryer        13.0 otter                22.2 snowmobile            58.8 zebra           49.6
                           Table 8: Per-class average precision (%) on the ILSVRC2013 detection test set.

[29] D. Lowe. Distinctive image features from scale-invariant              A holistic representation of the spatial envelope. IJCV, 2001.
     keypoints. IJCV, 2004. 1                                              13

[30] A. Oliva and A. Torralba. Modeling the shape of the scene:        [31] X. Ren and D. Ramanan. Histograms of sparse codes for

                                                                  15
                                                                                                                                                                                                                           cocktail shaker 0.56
                                                                                                                                                             person 0.88                                                                                                                                                                                                                  helmet 0.65
                                                                                                                                                                                                                                                                                                                                             dog 0.95                              dog 0.97
                                                                                                                                                                                        person 0.72
                                                                                                                                                                                                                                                                                                        dog 0.97
                                                                                                                                                                                                                                                                          dog 0.85       dog 0.57                                                       bird 0.63
                                                                                                                                                                                                                                                                                                                                        dog 0.64
                     lemon 0.79

                            lemon 0.70

           lemon 0.56
          lemon 0.50

                                                                                                              person 0.82
                                                                                                                                                                                                                                                                                                                                                     bird 0.96

                                                                                                                                                                                                                                                                               dog 0.66
                                                                                                                                                                                                                                                                             domestic cat 0.57
                                                                                                                                                                                                                                                                                     dog 0.61
                                                                    helmet
                                                                 person    0.52
                                                                        0.75

                        snowmobile 0.83           motorcycle 0.65
                        snowmobile 0.83                  person 0.58
                                                                                                                                bow tie 0.86                                                                                   bird 0.61

                                                                                                                                                                                                                                                                                                               ladybug 1.00                             person 0.87
                    sofa 0.71         dog 0.91

                                                            dog 0.77

                                                                                                                                                  dog 0.95

                                                                                                                                                                                                                                                                                            dog 0.55

                                                                                                                                                                                                                                                           pretzel 0.78

                                                                                       bird 0.98

         car 0.63car 0.96                                                                                                                                                                                                                                                                           person 0.52
                                    car 0.66                                                                                                                                                                                                                                                                                                                                 bird 0.91
                                                                                                                                                     watercraft 1.00                                                                                                                                                                     bird 0.99
                                                                                                                                                                                       person 0.65
                                                                                                                                                                                                                                                                                            car 0.96

                                                                                                                                                 watercraft 0.69                                                                                                                                person 0.52                                                                                 bird 0.75
                                                                                                                                                                                                                                                                                                                    person 0.58
                                                                                                                                                                                                                                                                                                                          person 0.65

                                                                                                                                                                                                                                                                                                                                                                 armadillo 0.56

                                                                                                                                                                                                                                              train 1.00
                                          flower pot 0.62                                     dog 0.97
                                                                                                dog 0.56                                                                                                                                              train 0.53                                                                                                  armadillo 1.00
                         dog 0.98

                                                                          dog 0.92
                                                                            swine 0.88

        bird 0.93                                                                                                                                                                                                                                    bird 1.00

                                                                                                                                                                                                                                                                                                          butterfly 0.96

                                                                                                                                                                                                 antelope 0.53                                                                                                                                        tv or monitor 0.82
    person 0.90                                                                                                                                                                                                                                                                                                                                                         tv or monitor 0.76
                                                                                                                                                                                                                                                                                                                                                                                      tv or monitor 0.54

                                                       snake 0.70                                                                                                                                     mushroom 0.93

                                                                                                                              bell pepper 0.54
                                                                                turtle 0.54
                                                              flower pot 0.62                              bell pepper 0.62
                                                                                                                                                                    bell pepper 0.81

                                                                                                           ruler 1.00

                                                                                                                                                                                                                                                                                 dog 0.97
                                                                                                                                                                                  person 0.58
                                                                                                                                                                                                               lipstick 0.61
                                                                                                                                                                                                           lipstick 0.80
                                                                                                                         bird 0.89

                                                                                                                                                                                                                                                                                                soccer ball 0.90

Figure 8: Example detections on the val2 set from the configuration that achieved 31.0% mAP on val2 . Each image was sampled randomly
(these are not curated). All detections at precision greater than 0.5 are shown. Each detection is labeled with the predicted class and the
precision value of that detection from the detector’s precision-recall curve. Viewing digitally with zoom is recommended.

                                                                                                                                                                                                                 16
                  helmet
                  baby bed
                         0.51
                            0.55                                                                                                                                                                                                                                                                                      watercraft 0.55
                      pitcher 0.57
                                                                                                                                                                                                                                                                                monkey 0.97

                                                                                                                                                    table 0.60   bird 0.52
                                                                                                             hat with a wide brim 0.78
                                                                                                       person 0.86
                                                                                            dog 0.98
                                                                                                                                                                                                                                                                                                                     table 0.68

                                 person 0.88

                                                                                                                                                                                                                                                                                                                      person 0.87

                                                                                                                                                                                                                                                                                                                                 sunglasses 0.51

                                                                                                                                                                                                                                                                                                                   person 0.51
                                                                                                                                                                                                                    car 0.61

                                                                                                                                                                                                                                                                                                 dog 0.97

                                                                                                                                                                                                                          swinemonkey
                                                                                                                                                                                                                                0.50 0.87
                                                                                                                                                                                                                            bird 0.52
                                                                                                                                                                                                                                                         monkey 0.81

                                                         dog 0.55       dog 0.94

                                                                                                                                                                                                                                                                                                                                  dog 0.97
              hat with a wide brim 0.96

                                                                                                                                                                                                                                                      person 0.77

                                                                                                                                                                                     snake 0.74
                                                                                                                                                                                                                                                                     dog 0.93

                   table 0.54                                                                                                                                                                                                           person 0.52

                                                                                                                person 0.85                                                                                                                                                          zebra 0.55      zebra 0.83
                                                                                                                                                                                                                                                                                                                    zebra 0.80
                                                                                                                     dog 0.71
                                                                                                                                                                                                                                                                                                                         zebra 0.52

                          pretzel 0.69                                                                                                                                                            ladybug 0.90

                                                           guacamole 0.64

                                                                                                                                                                                                                                                         person 0.58

                                                                                                                                                        person 0.85                                                                                                                                     dog 0.98
                            dog 0.98                                                                                person 0.73                                 hat with a wide brim 0.60
                                                                                           person 0.81                                                                                                            elephant 1.00
                                                                                                                                                                                                                                                                    bird 0.99

                                                                            computer keyboard 0.52                                       dog 0.97                             dog 0.92
                                                                                                                                                                                                                                                                                     bird 0.94

              cart 1.00
person 0.87                         person 0.91                                                                                                                                                                                   person 0.77
                                 person 0.57
                 chair
               chair    0.79
                     0.64                  person 0.52                                                                                                                                                                                                                                                                                   butterfly 0.98

                                                                                                                                                                                                  person 0.91         person 0.75
                          person 0.73
                                                                                                                                                                                                                                                                                                                                                          bird 0.83
                                                                                                                                                    bird 1.00

                                                                                                                                                                                                                 stethoscope 0.83

                                                                        person 0.61                                                                                      bird 0.78

                  Figure 9: More randomly selected examples. See Figure 8 caption for details. Viewing digitally with zoom is recommended.

                                                                                                                                                                                                          17
                                                                                                                                                                person 0.73
                                                                                                                                                                                                                                                                                                                                                                         lemon
                                                                                                                                                                                                                                                                                                                                                                         orange0.88
                                                                                                                                                                                                                                                                                                                                                                                0.73

                                                                                                                             person 0.51
                                                                                                                                                                                                            pineapple 1.00                                 bowl 0.63
                                                                                                                                                                                                                                                                     guacamole
                                                                                                                                                                                                                                                              tennis ball 0.60 1.00
                                                                                                                                                                                                                                                                                                                                                 orange 0.71
                                                                                                                                                                                                                                                                                                                                                  lemon 0.78
                  person 0.81                                                                            motorcycle 0.64
                                            person 0.57                                                                                                                                                                                                                                                                                                 lemon 0.80
                                                                                                                                                                                                                                                                                                                                                        orange 0.78                       lemon 0.86
                                        person 0.53
                                                                                                                                                                                                                       bagel 0.57

                                                                     lamp 0.61

                   soccer ball 0.67
                      golf ball 0.81
                                                                                                                  bee 0.85                                                                                                                                                                                                     person 0.52
                                                                                                                                                                                                 jellyfish 0.71                                                                                                                                         dumbbell 1.00
                    golf ball 0.51
                           golf ball 0.79                                                                                                                                                                                                                                  bowl 0.54
                  golf ball 0.89
                        golf ball 0.76 golf ball0.53
                                        lemon    0.60

                   golf ball 1.00                                                                                                                                                                                                                                          hamburger 0.78
                                     golf ball 0.60          table 0.59
                         golf ball 1.00

    person 0.85                                                                                                                                     goldfish 0.76
                                                                                 head cabbage 0.75                                                                                                                                                                                                                     microwave 0.60
                                                                                                                                                                                   person 0.57
                                                                                                                                                                                                                                                      guitar 1.00
                                                                                        head cabbage 0.83                                                                                                                                                                                                                                                                                           tick 0.64

                                                                                                                                                                                                                                    guitar 1.00

     microphone 1.00
                                                                                                                                                                                                                                           guitar 0.88
                                                                                                                                                                                                                                                                                                        table 0.53
                                                                                                                                                                                            dog 0.74
                                                                                                                                                                                                                                         table 0.63                                                              computer keyboard 0.78

                                                                                                                                                                                                    person 0.81
                                                                                                                                                                                                                                                                                         person 0.92
                                                                                                                                                                                                            dog 0.98
                                                                                                                               rabbit 1.00
               tennis ball 0.67
            lemon 0.80

                                                                                                                                                                                                                                                                                                                                          watercraft 0.86
                                                                                                                                                                                                                                                                                            sunglasses 0.52

                                                             milk can 1.00
                                         milk can 1.00                                                                                             person 0.87                                                                                                      antelope 0.74
                                                                                                                                                                                                                                                                       dog 0.87
                                                                                                                            bookshelf 0.50                                                                                                                          horse 0.78
                                                                                                                                                                                                                                                                        cattle 0.81

                                                                                                                                                                                                                                                                                                                                               pomegranate 1.00
                                                                                                                                                                              giant panda 0.61

                                                                                       chair 0.86

                       tv or monitor 0.52                                                                                                                                                                                                                                dog 0.88
                                                                                                                                                                         bird 0.94
                                                                                         antelope 0.68                                                                   snake 0.60

                          chair 0.86
                                                                                                                                                                                                                                                                                                                                             person 0.79
                                                                                                                                                                                                                                                             dog 0.98                                                                         snake 0.76

                                                                                           lamp 0.65lamp 0.86                                                                                                                                                                                                                    watercraft 0.91
                                                                                                                                                                                                                                                                         fox 0.81
                                                                                                                                                                                                                                             dog 0.88
                                                                                                                                                                                                                                       fox 1.00

                                                                                                                                                       monkey 1.00
                                                                                                                                                                              monkey 1.00

                                                                                       table 0.83                                                                       monkey 0.52
                                                                                                                                                                                            monkey 0.88

       tv or monitor tv
                     0.80
                        or monitor 0.54                                                                                                           monkey 0.90
                                       tv or monitor 0.58

      table 0.62
                                                                                                                                                                                                                                                                                                                               watercraft 0.56                                            person 0.88

                                                                                                                                                                       dragonfly 0.70                                                                                                                                                                electric fan 0.83

                                                                                                                bird 0.69
                                                                                                                                                                                                                                                                                       hamburger 0.60
                                                                                                                                                                                                                                                                                                              hamburger 0.72
                                                                                                                                                                                                  dragonfly 0.60
                                                                                                                                                                                                                                                                                                                                                                                  cup or mug 0.72
                                       isopod 0.56      bird 0.95

                                                                                                                                  starfish 0.67
                                            bird 0.78

                                                                                                                                                                                                                                                                                                                                                                     soccer ball 0.63
                                                                                                                                                                                                                                                                                                                                                  electric
                                                                                                                                                                                                                                                                                                                                                    helmetfan 0.78
                                                                                                                                                                                                                                                                                                                                                            0.64      electric fan 1.00

Figure 10: Curated examples. Each image was selected because we found it impressive, surprising, interesting, or amusing. Viewing
digitally with zoom is recommended.

                                                                                                                                                                                                   18
     object detection. In CVPR, 2013. 6, 7
[32] H. A. Rowley, S. Baluja, and T. Kanade. Neural network-
     based face detection. TPAMI, 1998. 2
[33] D. E. Rumelhart, G. E. Hinton, and R. J. Williams. Learn-
     ing internal representations by error propagation. Parallel
     Distributed Processing, 1:318–362, 1986. 1
[34] P. Sermanet, D. Eigen, X. Zhang, M. Mathieu, R. Fergus,
     and Y. LeCun. OverFeat: Integrated Recognition, Localiza-
     tion and Detection using Convolutional Networks. In ICLR,
     2014. 1, 2, 4, 10
[35] P. Sermanet, K. Kavukcuoglu, S. Chintala, and Y. LeCun.
     Pedestrian detection with unsupervised multi-stage feature
     learning. In CVPR, 2013. 2
[36] H. Su, J. Deng, and L. Fei-Fei. Crowdsourcing annotations
     for visual object detection. In AAAI Technical Report, 4th
     Human Computation Workshop, 2012. 8
[37] K. Sung and T. Poggio. Example-based learning for view-
     based human face detection. Technical Report A.I. Memo
     No. 1521, Massachussets Institute of Technology, 1994. 4
[38] C. Szegedy, A. Toshev, and D. Erhan. Deep neural networks
     for object detection. In NIPS, 2013. 2
[39] J. Uijlings, K. van de Sande, T. Gevers, and A. Smeulders.
     Selective search for object recognition. IJCV, 2013. 1, 2, 3,
     4, 5, 9
[40] R. Vaillant, C. Monrocq, and Y. LeCun. Original approach
     for the localisation of objects in images. IEE Proc on Vision,
     Image, and Signal Processing, 1994. 2
[41] X. Wang, M. Yang, S. Zhu, and Y. Lin. Regionlets for generic
     object detection. In ICCV, 2013. 3, 5
[42] M. Zeiler, G. Taylor, and R. Fergus. Adaptive deconvolu-
     tional networks for mid and high level feature learning. In
     CVPR, 2011. 4
[43] K. Simonyan and A. Zisserman. Very Deep Convolu-
     tional Networks for Large-Scale Image Recognition. arXiv
     preprint, arXiv:1409.1556, 2014. 6, 7, 14

                                                                      19
   person 0.82
                          snake 0.76                                                                                                                                                                                                                                                         person 0.94

                                                                                                                                                                                                                                                                                                                                                                         person 0.95                                person 0.60
                                                                                                                                                                                                                                                                                                                                                                                  person  0.92
                                                                                                                                                                                                                                                                                                                                                                                     person 0.67

                                                                                                                                                                                                              goldfish 0.76                                                                           stethoscope 0.56
                                                                                                                                                                                                                              bird 0.79
                                                                                                       frog 0.78                                                                                  goldfish 0.76            goldfish 0.58

                                                                                                                                                                                                                                                                                                                                        table 0.81

                                                                                     watercraft 0.55
                                                                                                                                                                            person 0.94       person 0.80
         jellyfish 0.67                                                                                                                                                                                                                                                  tv or monitor 0.82
                                                                                                                                                                         person 0.55                                                                                       person 0.68
lemon 0.52                                                                                                             person 0.78                                                                                                                                                 person 0.59
                                                                                                                                person 0.65
                                                                                                                                                                                                                       person 0.52                                                                                                                                                 lizard 0.58
                                                                                                                                                                                    person 0.61
                                                                                                                                                                                                             person 0.82                   dog 0.60                                              person 0.88
                                                                                                                                                                                                                                           person 0.79

                                                                                                                                                                                                                                                                                     computer keyboard 0.81

                                                                                                                                                                                           baseball 1.00

person 0.74
                                                                                                                                                                                                                                                                                                                                                                                                                                  person 0.69
                                                                                                                                                                                                                                                                                                                                                                                                                                      person 0.79
                                                                       person 0.94
                                                                                                                                                                                                                                      volleyball 0.70
                                                                                                                                                                                                                                                                                                                                                person person
                                                                                                                                                                                                                                                                                                                                                       0.80 0.58 person 0.79
                                                                                                                                                                                                                                                                                                        pineapple 1.00                                                      person 0.81 person 0.56                           person 0.80
                                                                                                                                                                                                                                                                                                                                                                             person 0.54
                                                                                                                              person 0.94                                                                                                                                                                                                                                   person 0.66
                                                                                                                                                                                                                           person 0.84            person 0.59                                                                                    person 0.94                                          person 0.94
                                                                                                                                                                    person 0.95
                                                                                                                                                                                                                                                                                                                                                                                  person 0.95
        table 0.82                                                                                                                                                                         person 0.69
                                                                                                                                                                                  person 0.81

                                                                                                                                                                                                                                                                                                                                                                                                          brassiere 0.71
                                       chair 0.50

                                                                                                                                                                                                                                                                                                                                                                                     swimming trunks 0.56

                                                                                                                                                                                           rugby ball 0.91

                                                                                                person 0.92
          baseball 0.86
                   person 0.75                                                                                                                                                                                                                                                                                                                       tiger 1.00
                                                                                                                                                                                                                                                                                                                                                                              tiger 0.59
                                                         helmet 0.74                                                                                                       dog 0.98
                                                                                                                vacuum 1.00
                                                                                                                                                          dog 0.93

                                                                                                                                                                                                                                                                                                                                              bird 0.55
                                                                                                                                                                                                                                                                                                               person 0.75
                                                                                                                                                                                                                                                                                                                                           tiger 0.67
                                                                                                                                                                                                                                                                                     person 0.94
                                                                                                                                                                                                                                                                                                                          person 0.65
                                                                                                   miniskirt 0.64

                                                                                                                                                                                                                                                        person 0.53
                                                                                                                                                                                                                                                                                                   ski 0.80
                                                                                                                                                                                                                                                                               ski 0.80

                                                                                                                                                                                       bowl 0.52

                                                                                                                           person 0.78
                                                                                                                                                              person 0.82

         bird 0.56                                                                                                                                                                                                       strawberry 0.79
  whale 1.00                                                                                                                                                                                               strawberry 0.70
                                                                                                                                                                                                                                                                              burrito 0.54
                                                                                                                   person 0.92
                                                                                                                                              person 0.92

                                                                                                  chair 0.53

                                                                                                                                                                                                                                                                                                                                                                                       croquet  croquet
                                                                                                                                                                                                                                                                                                                                                                                                ball 0.91ball 0.91
                                                                                                                                                                                                                                                                                                                                                                        croquetcroquet
                                                                                                                                                                                                                                                                                                                                                                        mushroomball0.57
                                                                                                                                                                                                                                                                                                                                                                                     0.91ball 0.91

                                                                                                        plastic bag 0.62                                                                                                                                        tv or monitor 0.57
                                             watercraft 0.87
                                                                                                                                       plastic bag 0.62

                                                                                                                                                                                                                                                                                      dog 0.94

                                                                                                                                                                                                                                                                                                                                                 cart 0.80 person 0.53
                                                                                                                                                                                                                                                                                                                                                person 0.79

                                                                                                                                                                                                                    whale 0.88
                                          watercraft 0.91
                                                                                                                                                                                                                                                                 car 0.70

                                        watercraft 0.58

                                                                                                                                                                                                                                                                                                                            antelope
                                                                                                                                                                                                                                                                                                                       antelope 1.00 0.63
                                                                                                                                                                                                                              bird 0.59                                                                                                                antelope 1.00
                                hat with
                               person    aperson
                                      0.54
                                                 0.880.89
                                           wide brim                                                                             traffic light 0.79
                                  person 0.79
                                                                                                                                                                                                                                                                                                                               antelope 0.63
                                                                                                                                                                                                                                                                                                                                                                                                   horizontal bar 1.00
                                                                                                                                                                                                                                                                                                                                                                                                    balance beam    0.50
         person 0.82                                                                                                                                                                                                                                                                                              antelope 0.73                                                                                 person 0.80

                                                                                                                                                                                                                                                                                                                                           fox 0.57
                                                    person 0.56                                                                                                                                                  cucumber 0.53

                                                                                                                                                                                                                                                                                                                                                          antelope 0.94
                                                                                                                                                                                                                              cucumber 0.52

                                                                                                                                                                                                      helmet 0.69
                                                                                                                                                                                                   person 0.82                                                                                                                  orange 0.56
   person 0.90                                                                             dog 0.97                                                                                                                                                             orange 0.66
                                                                                                                                                                                                                                                                                                                                                                         bird 0.96            bird 0.64
                                                                                                                                                                              horse 0.92
                                                                                                                                                                                                                                                                                                                                                                                       bird 0.89                               bird 0.53
                                                                                                       dog 0.98                                                                                                                                                                                                                                                                                              bird
                                                                                                                                                                                                                                                                                                                                                                                                              bird0.52
                                                                                                                                                                                                                                                                                                                                                                                                                   0.96
                          snake 0.64
                                                                                                                                                                                                                                                                                                                                                                  birdbird 0.97
                                                                                                                                                                                                                                                                                                                                                                        0.56
                                                                                                                                                                         person 0.72         horse 0.69                                                                                                                                                                                              bird 0.94
                                                                                                                                                                                                                                                                                                                         orange 0.66orange 0.79

                                                                                                                                                                                                                                                                              orange 0.59

                                                                                                                                                                                                                                                                                                                              orange 0.71

                                                                                                                                                                                                                                                              person 0.83                                                       elephant 0.60

                                       person 0.82
                                       guitar 1.00                                                                                                                                                                                                                                                            person 0.74
                                                                                                                                                                                                                           person 0.54

                                                                                                                                                      person 0.83                                                                                                                                person 0.80
                                                                                                                                                                                                               car 1.00               car 0.97
                                                                                                                                                                      person 0.90
                                                                                                                                                                                                                                              dog 0.85
                                                                                                                                  bicycle 0.92
                                                                                                                                                                                                                                          dog 0.86
                                                                                                                                                                                                                                  dog 0.50
                                                                                                                                                                                                                            dog 0.65                                            dog 0.98

              Figure 11: More curated examples. See Figure 10 caption for details. Viewing digitally with zoom is recommended.

                                                                                                                                                                                                              20
                pool5 feature: (3,3,1) (top 1 − 24)                                           pool5 feature: (3,3,2) (top 1 − 24)
    1.0   0.9    0.8   0.8   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7        1.0   0.9    0.9   0.9   0.9   0.8   0.8   0.7   0.7   0.7   0.7   0.7

    0.7   0.7    0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6        0.7   0.7    0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7

                pool5 feature: (3,3,3) (top 1 − 24)                                           pool5 feature: (3,3,4) (top 1 − 24)
    0.9   0.8    0.8   0.8   0.8   0.8   0.8   0.7   0.7   0.7   0.6   0.6        0.9   0.8    0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7

    0.6   0.6    0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6        0.7   0.7    0.7   0.7   0.7   0.7   0.7   0.6   0.6   0.6   0.6   0.6

                pool5 feature: (3,3,5) (top 1 − 24)                                           pool5 feature: (3,3,6) (top 1 − 24)
    0.9   0.8    0.8   0.8   0.8   0.8   0.8   0.8   0.7   0.7   0.7   0.7        0.9   0.8    0.8   0.8   0.8   0.7   0.7   0.7   0.7   0.7   0.7   0.7

    0.7   0.7    0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7        0.7   0.7    0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7

                pool5 feature: (3,3,7) (top 1 − 24)                                           pool5 feature: (3,3,8) (top 1 − 24)
    0.9   0.8    0.8   0.8   0.8   0.8   0.7   0.7   0.7   0.7   0.7   0.7        0.9   0.8    0.8   0.8   0.8   0.8   0.8   0.7   0.7   0.7   0.7   0.7

    0.7   0.7    0.7   0.7   0.7   0.7   0.7   0.7   0.6   0.6   0.6   0.6        0.7   0.7    0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7

                pool5 feature: (3,3,9) (top 1 − 24)                                           pool5 feature: (3,3,10) (top 1 − 24)
    0.8   0.8    0.8   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7        0.9   0.8    0.8   0.7   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6

    0.7   0.7    0.7   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6        0.6   0.6    0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.5   0.5

                pool5 feature: (3,3,11) (top 1 − 24)                                          pool5 feature: (3,3,12) (top 1 − 24)
    0.7   0.7    0.7   0.7   0.7   0.6   0.6   0.6   0.6   0.6   0.6   0.6        0.9   0.8    0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7

    0.6   0.6    0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6        0.7   0.6    0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6

                pool5 feature: (3,3,13) (top 1 − 24)                                          pool5 feature: (3,3,14) (top 1 − 24)
    0.9   0.9    0.8   0.8   0.8   0.8   0.8   0.8   0.8   0.8   0.8   0.8        0.9   0.9    0.9   0.8   0.8   0.8   0.8   0.8   0.8   0.8   0.8   0.8

    0.8   0.8    0.8   0.8   0.8   0.8   0.8   0.8   0.8   0.8   0.8   0.8        0.8   0.7    0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7

                pool5 feature: (3,3,15) (top 1 − 24)                                          pool5 feature: (3,3,16) (top 1 − 24)
    0.8   0.8    0.8   0.8   0.8   0.8   0.8   0.8   0.8   0.8   0.8   0.8        0.9   0.8    0.8   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7

    0.7   0.7    0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7        0.6   0.6    0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6

                pool5 feature: (3,3,17) (top 1 − 24)                                          pool5 feature: (3,3,18) (top 1 − 24)
    0.9   0.9    0.8   0.8   0.8   0.8   0.7   0.7   0.7   0.7   0.7   0.7        0.8   0.7    0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.6   0.6

    0.7   0.7    0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7   0.7        0.6   0.6    0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6

                pool5 feature: (3,3,19) (top 1 − 24)                                          pool5 feature: (3,3,20) (top 1 − 24)
    0.9   0.8    0.8   0.7   0.7   0.7   0.7   0.7   0.7   0.6   0.6   0.6        1.0   0.9    0.7   0.7   0.7   0.7   0.7   0.7   0.6   0.6   0.6   0.6

    0.6   0.6    0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6        0.6   0.6    0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6   0.6

Figure 12: We show the 24 region proposals, out of the approximately 10 million regions in VOC 2007 test, that most strongly
activate each of 20 units. Each montage is labeled by the unit’s (y, x, channel) position in the 6 × 6 × 256 dimensional pool5 feature map.
Each image region is drawn with an overlay of the unit’s receptive field in white. The activation value (which we normalize by dividing by
the max activation value over all units in a channel) is shown in the receptive field’s upper-left corner. Best viewed digitally with zoom.

                                                                             21
