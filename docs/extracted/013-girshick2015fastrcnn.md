---
source_id: 013
bibtex_key: girshick2015fastrcnn
title: Fast R-CNN
year: 2015
domain_theme: Fondasi RGB
verified_pdf: 13_Fast R-CNN.pdf
char_count: 62622
---

Fast R-CNN

                                                                                                Ross Girshick
                                                                                              Microsoft Research
                                                                                              rbg@microsoft.com
arXiv:1504.08083v2 [cs.CV] 27 Sep 2015

                                                                  Abstract                                 while achieving top accuracy on PASCAL VOC 2012 [7]
                                                                                                           with a mAP of 66% (vs. 62% for R-CNN).1
                                            This paper proposes a Fast Region-based Convolutional
                                         Network method (Fast R-CNN) for object detection. Fast            1.1. R-CNN and SPPnet
                                         R-CNN builds on previous work to efficiently classify ob-            The Region-based Convolutional Network method (R-
                                         ject proposals using deep convolutional networks. Com-            CNN) [9] achieves excellent object detection accuracy by
                                         pared to previous work, Fast R-CNN employs several in-            using a deep ConvNet to classify object proposals. R-CNN,
                                         novations to improve training and testing speed while also        however, has notable drawbacks:
                                         increasing detection accuracy. Fast R-CNN trains the very
                                         deep VGG16 network 9× faster than R-CNN, is 213× faster            1. Training is a multi-stage pipeline. R-CNN first fine-
                                         at test-time, and achieves a higher mAP on PASCAL VOC                 tunes a ConvNet on object proposals using log loss.
                                         2012. Compared to SPPnet, Fast R-CNN trains VGG16 3×                  Then, it fits SVMs to ConvNet features. These SVMs
                                         faster, tests 10× faster, and is more accurate. Fast R-CNN            act as object detectors, replacing the softmax classi-
                                         is implemented in Python and C++ (using Caffe) and is                 fier learnt by fine-tuning. In the third training stage,
                                         available under the open-source MIT License at https:                 bounding-box regressors are learned.
                                         //github.com/rbgirshick/fast-rcnn.                                 2. Training is expensive in space and time. For SVM
                                                                                                               and bounding-box regressor training, features are ex-
                                                                                                               tracted from each object proposal in each image and
                                         1. Introduction                                                       written to disk. With very deep networks, such as
                                                                                                               VGG16, this process takes 2.5 GPU-days for the 5k
                                            Recently, deep ConvNets [14, 16] have significantly im-
                                                                                                               images of the VOC07 trainval set. These features re-
                                         proved image classification [14] and object detection [9, 19]
                                                                                                               quire hundreds of gigabytes of storage.
                                         accuracy. Compared to image classification, object detec-
                                         tion is a more challenging task that requires more com-            3. Object detection is slow. At test-time, features are
                                         plex methods to solve. Due to this complexity, current ap-            extracted from each object proposal in each test image.
                                         proaches (e.g., [9, 11, 19, 25]) train models in multi-stage          Detection with VGG16 takes 47s / image (on a GPU).
                                         pipelines that are slow and inelegant.
                                                                                                              R-CNN is slow because it performs a ConvNet forward
                                            Complexity arises because detection requires the ac-
                                                                                                           pass for each object proposal, without sharing computation.
                                         curate localization of objects, creating two primary chal-
                                                                                                           Spatial pyramid pooling networks (SPPnets) [11] were pro-
                                         lenges. First, numerous candidate object locations (often
                                                                                                           posed to speed up R-CNN by sharing computation. The
                                         called “proposals”) must be processed. Second, these can-
                                                                                                           SPPnet method computes a convolutional feature map for
                                         didates provide only rough localization that must be refined
                                                                                                           the entire input image and then classifies each object pro-
                                         to achieve precise localization. Solutions to these problems
                                                                                                           posal using a feature vector extracted from the shared fea-
                                         often compromise speed, accuracy, or simplicity.
                                                                                                           ture map. Features are extracted for a proposal by max-
                                            In this paper, we streamline the training process for state-
                                                                                                           pooling the portion of the feature map inside the proposal
                                         of-the-art ConvNet-based object detectors [9, 11]. We pro-
                                                                                                           into a fixed-size output (e.g., 6 × 6). Multiple output sizes
                                         pose a single-stage training algorithm that jointly learns to
                                                                                                           are pooled and then concatenated as in spatial pyramid pool-
                                         classify object proposals and refine their spatial locations.
                                                                                                           ing [15]. SPPnet accelerates R-CNN by 10 to 100× at test
                                            The resulting method can train a very deep detection
                                                                                                           time. Training time is also reduced by 3× due to faster pro-
                                         network (VGG16 [20]) 9× faster than R-CNN [9] and 3×
                                                                                                           posal feature extraction.
                                         faster than SPPnet [11]. At runtime, the detection network
                                         processes images in 0.3s (excluding object proposal time)           1 All timings use one Nvidia K40 GPU overclocked to 875 MHz.
   SPPnet also has notable drawbacks. Like R-CNN, train-
                                                                                                                      Outputs:
ing is a multi-stage pipeline that involves extracting fea-                                                                      bbox
                                                                                         Deep                          softmax regressor
tures, fine-tuning a network with log loss, training SVMs,                               ConvNet
                                                                                                           RoI                   FC    FC
and finally fitting bounding-box regressors. Features are                                                  pooling
also written to disk. But unlike R-CNN, the fine-tuning al-                                                layer      FCs
                                                                                         RoI
gorithm proposed in [11] cannot update the convolutional                                 projection
layers that precede the spatial pyramid pooling. Unsurpris-                                  Conv                    RoI feature
ingly, this limitation (fixed convolutional layers) limits the                               feature map               vector For each RoI
accuracy of very deep networks.
                                                                   Figure 1. Fast R-CNN architecture. An input image and multi-
1.2. Contributions                                                 ple regions of interest (RoIs) are input into a fully convolutional
                                                                   network. Each RoI is pooled into a fixed-size feature map and
   We propose a new training algorithm that fixes the disad-       then mapped to a feature vector by fully connected layers (FCs).
vantages of R-CNN and SPPnet, while improving on their             The network has two output vectors per RoI: softmax probabilities
speed and accuracy. We call this method Fast R-CNN be-             and per-class bounding-box regression offsets. The architecture is
cause it’s comparatively fast to train and test. The Fast R-       trained end-to-end with a multi-task loss.
CNN method has several advantages:
                                                                      RoI max pooling works by dividing the h × w RoI win-
  1. Higher detection quality (mAP) than R-CNN, SPPnet
                                                                   dow into an H × W grid of sub-windows of approximate
  2. Training is single-stage, using a multi-task loss             size h/H × w/W and then max-pooling the values in each
  3. Training can update all network layers                        sub-window into the corresponding output grid cell. Pool-
                                                                   ing is applied independently to each feature map channel,
  4. No disk storage is required for feature caching               as in standard max pooling. The RoI layer is simply the
   Fast R-CNN is written in Python and C++ (Caffe                  special-case of the spatial pyramid pooling layer used in
[13]) and is available under the open-source MIT Li-               SPPnets [11] in which there is only one pyramid level. We
cense at https://github.com/rbgirshick/                            use the pooling sub-window calculation given in [11].
fast-rcnn.                                                         2.2. Initializing from pre-trained networks
2. Fast R-CNN architecture and training                                We experiment with three pre-trained ImageNet [4] net-
                                                                   works, each with five max pooling layers and between five
    Fig. 1 illustrates the Fast R-CNN architecture. A Fast         and thirteen conv layers (see Section 4.1 for network de-
R-CNN network takes as input an entire image and a set             tails). When a pre-trained network initializes a Fast R-CNN
of object proposals. The network first processes the whole         network, it undergoes three transformations.
image with several convolutional (conv) and max pooling                First, the last max pooling layer is replaced by a RoI
layers to produce a conv feature map. Then, for each ob-           pooling layer that is configured by setting H and W to be
ject proposal a region of interest (RoI) pooling layer ex-         compatible with the net’s first fully connected layer (e.g.,
tracts a fixed-length feature vector from the feature map.         H = W = 7 for VGG16).
Each feature vector is fed into a sequence of fully connected          Second, the network’s last fully connected layer and soft-
(fc) layers that finally branch into two sibling output lay-       max (which were trained for 1000-way ImageNet classifi-
ers: one that produces softmax probability estimates over          cation) are replaced with the two sibling layers described
K object classes plus a catch-all “background” class and           earlier (a fully connected layer and softmax over K + 1 cat-
another layer that outputs four real-valued numbers for each       egories and category-specific bounding-box regressors).
of the K object classes. Each set of 4 values encodes refined          Third, the network is modified to take two data inputs: a
bounding-box positions for one of the K classes.                   list of images and a list of RoIs in those images.
2.1. The RoI pooling layer                                         2.3. Fine-tuning for detection
   The RoI pooling layer uses max pooling to convert the              Training all network weights with back-propagation is an
features inside any valid region of interest into a small fea-     important capability of Fast R-CNN. First, let’s elucidate
ture map with a fixed spatial extent of H × W (e.g., 7 × 7),       why SPPnet is unable to update weights below the spatial
where H and W are layer hyper-parameters that are inde-            pyramid pooling layer.
pendent of any particular RoI. In this paper, an RoI is a             The root cause is that back-propagation through the SPP
rectangular window into a conv feature map. Each RoI is            layer is highly inefficient when each training sample (i.e.
defined by a four-tuple (r, c, h, w) that specifies its top-left   RoI) comes from a different image, which is exactly how
corner (r, c) and its height and width (h, w).                     R-CNN and SPPnet networks are trained. The inefficiency
stems from the fact that each RoI may have a very large                      bounding box and hence Lloc is ignored. For bounding-box
receptive field, often spanning the entire input image. Since                regression, we use the loss
the forward pass must process the entire receptive field, the                                         X
training inputs are large (often the entire image).                                  Lloc (tu , v) =       smoothL1 (tui − vi ),   (2)
    We propose a more efficient training method that takes                                         i∈{x,y,w,h}
advantage of feature sharing during training. In Fast R-
                                                                             in which
CNN training, stochastic gradient descent (SGD) mini-                                                    (
batches are sampled hierarchically, first by sampling N im-                                                  0.5x2       if |x| < 1
ages and then by sampling R/N RoIs from each image.                                     smoothL1 (x) =                                  (3)
                                                                                                             |x| − 0.5   otherwise,
Critically, RoIs from the same image share computation
and memory in the forward and backward passes. Making                        is a robust L1 loss that is less sensitive to outliers than the
N small decreases mini-batch computation. For example,                       L2 loss used in R-CNN and SPPnet. When the regression
when using N = 2 and R = 128, the proposed training                          targets are unbounded, training with L2 loss can require
scheme is roughly 64× faster than sampling one RoI from                      careful tuning of learning rates in order to prevent exploding
128 different images (i.e., the R-CNN and SPPnet strategy).                  gradients. Eq. 3 eliminates this sensitivity.
    One concern over this strategy is it may cause slow train-                   The hyper-parameter λ in Eq. 1 controls the balance be-
ing convergence because RoIs from the same image are cor-                    tween the two task losses. We normalize the ground-truth
related. This concern does not appear to be a practical issue                regression targets vi to have zero mean and unit variance.
and we achieve good results with N = 2 and R = 128                           All experiments use λ = 1.
using fewer SGD iterations than R-CNN.                                           We note that [6] uses a related loss to train a class-
    In addition to hierarchical sampling, Fast R-CNN uses a                  agnostic object proposal network. Different from our ap-
streamlined training process with one fine-tuning stage that                 proach, [6] advocates for a two-network system that sepa-
jointly optimizes a softmax classifier and bounding-box re-                  rates localization and classification. OverFeat [19], R-CNN
gressors, rather than training a softmax classifier, SVMs,                   [9], and SPPnet [11] also train classifiers and bounding-box
and regressors in three separate stages [9, 11]. The compo-                  localizers, however these methods use stage-wise training,
nents of this procedure (the loss, mini-batch sampling strat-                which we show is suboptimal for Fast R-CNN (Section 5.1).
egy, back-propagation through RoI pooling layers, and SGD
hyper-parameters) are described below.                                       Mini-batch sampling. During fine-tuning, each SGD
                                                                             mini-batch is constructed from N = 2 images, chosen uni-
Multi-task loss. A Fast R-CNN network has two sibling                        formly at random (as is common practice, we actually iter-
output layers. The first outputs a discrete probability distri-              ate over permutations of the dataset). We use mini-batches
bution (per RoI), p = (p0 , . . . , pK ), over K + 1 categories.             of size R = 128, sampling 64 RoIs from each image. As
As usual, p is computed by a softmax over the K +1 outputs                   in [9], we take 25% of the RoIs from object proposals that
of a fully connected layer. The second sibling layer outputs
                                                                            have intersection over union (IoU) overlap with a ground-
bounding-box regression offsets, tk = tkx , tky , tkw , tkh , for            truth bounding box of at least 0.5. These RoIs comprise
each of the K object classes, indexed by k. We use the pa-                   the examples labeled with a foreground object class, i.e.
rameterization for tk given in [9], in which tk specifies a                  u ≥ 1. The remaining RoIs are sampled from object pro-
scale-invariant translation and log-space height/width shift                 posals that have a maximum IoU with ground truth in the in-
relative to an object proposal.                                              terval [0.1, 0.5), following [11]. These are the background
   Each training RoI is labeled with a ground-truth class u                  examples and are labeled with u = 0. The lower threshold
and a ground-truth bounding-box regression target v. We                      of 0.1 appears to act as a heuristic for hard example mining
use a multi-task loss L on each labeled RoI to jointly train                 [8]. During training, images are horizontally flipped with
for classification and bounding-box regression:                              probability 0.5. No other data augmentation is used.
    L(p, u, tu , v) = Lcls (p, u) + λ[u ≥ 1]Lloc (tu , v),            (1)
                                                                             Back-propagation through RoI pooling layers. Back-
in which Lcls (p, u) = − log pu is log loss for true class u.                propagation routes derivatives through the RoI pooling
   The second task loss, Lloc , is defined over a tuple of                   layer. For clarity, we assume only one image per mini-batch
true bounding-box regression targets for class u, v =                        (N = 1), though the extension to N > 1 is straightforward
(vx , vy , vw , vh ), and a predicted tuple tu = (tux , tuy , tuw , tuh ),   because the forward pass treats all images independently.
again for class u. The Iverson bracket indicator function                       Let xi ∈ R be the i-th activation input into the RoI pool-
[u ≥ 1] evaluates to 1 when u ≥ 1 and 0 otherwise. By                        ing layer and let yrj be the layer’s j-th output from the r-
convention the catch-all background class is labeled u = 0.                  th RoI. The RoI pooling layer computes yrj = xi∗ (r,j) , in
For background RoIs there is no notion of a ground-truth                     which i∗ (r, j) = argmaxi0 ∈R(r,j) xi0 . R(r, j) is the index
set of inputs in the sub-window over which the output unit         test-time, R is typically around 2000, although we will con-
yrj max pools. A single xi may be assigned to several dif-         sider cases in which it is larger (≈ 45k). When using an
ferent outputs yrj .                                               image pyramid, each RoI is assigned to the scale such that
   The RoI pooling layer’s backwards function computes             the scaled RoI is closest to 2242 pixels in area [11].
partial derivative of the loss function with respect to each          For each test RoI r, the forward pass outputs a class
input variable xi by following the argmax switches:                posterior probability distribution p and a set of predicted
                                                                   bounding-box offsets relative to r (each of the K classes
             ∂L    XX                   ∂L
                 =     [i = i∗ (r, j)]      .               (4)    gets its own refined bounding-box prediction). We assign a
             ∂xi   r j
                                       ∂yrj                        detection confidence to r for each object class k using the
                                                                                                                ∆
                                                                   estimated probability Pr(class = k | r) = pk . We then
In words, for each mini-batch RoI r and for each pooling
                                                                   perform non-maximum suppression independently for each
output unit yrj , the partial derivative ∂L/∂yrj is accumu-
                                                                   class using the algorithm and settings from R-CNN [9].
lated if i is the argmax selected for yrj by max pooling.
In back-propagation, the partial derivatives ∂L/∂yrj are al-       3.1. Truncated SVD for faster detection
ready computed by the backwards function of the layer
on top of the RoI pooling layer.                                       For whole-image classification, the time spent comput-
                                                                   ing the fully connected layers is small compared to the conv
                                                                   layers. On the contrary, for detection the number of RoIs
SGD hyper-parameters. The fully connected layers used
                                                                   to process is large and nearly half of the forward pass time
for softmax classification and bounding-box regression are
                                                                   is spent computing the fully connected layers (see Fig. 2).
initialized from zero-mean Gaussian distributions with stan-
                                                                   Large fully connected layers are easily accelerated by com-
dard deviations 0.01 and 0.001, respectively. Biases are ini-
                                                                   pressing them with truncated SVD [5, 23].
tialized to 0. All layers use a per-layer learning rate of 1 for
                                                                       In this technique, a layer parameterized by the u × v
weights and 2 for biases and a global learning rate of 0.001.
                                                                   weight matrix W is approximately factorized as
When training on VOC07 or VOC12 trainval we run SGD
for 30k mini-batch iterations, and then lower the learning                                W ≈ U Σt V T                         (5)
rate to 0.0001 and train for another 10k iterations. When
we train on larger datasets, we run SGD for more iterations,       using SVD. In this factorization, U is a u × t matrix com-
as described later. A momentum of 0.9 and parameter decay          prising the first t left-singular vectors of W , Σt is a t × t
of 0.0005 (on weights and biases) are used.                        diagonal matrix containing the top t singular values of W ,
                                                                   and V is v × t matrix comprising the first t right-singular
2.4. Scale invariance
                                                                   vectors of W . Truncated SVD reduces the parameter count
    We explore two ways of achieving scale invariant ob-           from uv to t(u + v), which can be significant if t is much
ject detection: (1) via “brute force” learning and (2) by us-      smaller than min(u, v). To compress a network, the single
ing image pyramids. These strategies follow the two ap-            fully connected layer corresponding to W is replaced by
proaches in [11]. In the brute-force approach, each image          two fully connected layers, without a non-linearity between
is processed at a pre-defined pixel size during both training      them. The first of these layers uses the weight matrix Σt V T
and testing. The network must directly learn scale-invariant       (and no biases) and the second uses U (with the original bi-
object detection from the training data.                           ases associated with W ). This simple compression method
    The multi-scale approach, in contrast, provides approx-        gives good speedups when the number of RoIs is large.
imate scale-invariance to the network through an image
pyramid. At test-time, the image pyramid is used to ap-            4. Main results
proximately scale-normalize each object proposal. During
                                                                      Three main results support this paper’s contributions:
multi-scale training, we randomly sample a pyramid scale
each time an image is sampled, following [11], as a form of         1. State-of-the-art mAP on VOC07, 2010, and 2012
data augmentation. We experiment with multi-scale train-
                                                                    2. Fast training and testing compared to R-CNN, SPPnet
ing for smaller networks only, due to GPU memory limits.
                                                                    3. Fine-tuning conv layers in VGG16 improves mAP
3. Fast R-CNN detection
                                                                   4.1. Experimental setup
   Once a Fast R-CNN network is fine-tuned, detection
                                                                       Our experiments use three pre-trained ImageNet models
amounts to little more than running a forward pass (assum-
                                                                   that are available online.2 The first is the CaffeNet (essen-
ing object proposals are pre-computed). The network takes
                                                                   tially AlexNet [14]) from R-CNN [9]. We alternatively refer
as input an image (or an image pyramid, encoded as a list
of images) and a list of R object proposals to score. At             2 https://github.com/BVLC/caffe/wiki/Model-Zoo
method            train set aero bike bird boat bottle bus car cat chair cow table dog horse mbike persn plant sheep sofa train tv mAP
              †
SPPnet BB [11]    07 \ diff 73.9 72.3 62.5 51.5 44.4 74.4 73.0 74.4 42.3 73.6 57.7 70.3 74.6 74.3 54.2 34.0 56.4 56.4 67.9 73.5 63.1
R-CNN BB [10]     07        73.4 77.0 63.4 45.4 44.6 75.1 78.1 79.8 40.5 73.7 62.2 79.4 78.1 73.1 64.2 35.6 66.8 67.2 70.4 71.1 66.0
FRCN [ours]       07        74.5 78.3 69.2 53.2 36.6 77.3 78.2 82.0 40.7 72.7 67.9 79.6 79.2   73.0   69.0   30.1   65.4   70.2 75.8 65.8 66.9
FRCN [ours]       07 \ diff 74.6 79.0 68.6 57.0 39.3 79.5 78.6 81.9 48.0 74.0 67.4 80.5 80.7   74.1   69.6   31.8   67.1   68.4 75.3 65.5 68.1
FRCN [ours]       07+12     77.0 78.1 69.3 59.4 38.3 81.6 78.6 86.7 42.8 78.8 68.9 84.7 82.0   76.6   69.9   31.8   70.1   74.8 80.4 70.4 70.0

Table 1. VOC 2007 test detection average precision (%). All methods use VGG16. Training set key: 07: VOC07 trainval, 07 \ diff: 07
without “difficult” examples, 07+12: union of 07 and VOC12 trainval. † SPPnet results were prepared by the authors of [11].

method            train set aero bike bird boat bottle bus car cat chair cow table dog horse mbike persn plant sheep sofa train tv        mAP
BabyLearning      Prop.     77.7 73.8 62.3 48.8 45.4 67.3 67.0 80.3 41.3 70.8 49.7 79.5 74.7 78.6 64.5 36.0 69.9 55.7 70.4 61.7           63.8
R-CNN BB [10]     12        79.3 72.4 63.1 44.0 44.4 64.6 66.3 84.9 38.8 67.3 48.4 82.3 75.0 76.7 65.7 35.8 66.2 54.8 69.1 58.8           62.9
SegDeepM          12+seg 82.3 75.2 67.1 50.7 49.8 71.1 69.6 88.2 42.5 71.2 50.0 85.7 76.6 81.8 69.3 41.5 71.9 62.2 73.2 64.6              67.2
FRCN [ours]       12       80.1 74.4 67.7 49.4 41.4 74.2 68.8 87.8 41.9 70.1 50.2 86.1 77.3    81.1   70.4   33.3   67.0   63.3 77.2 60.0 66.1
FRCN [ours]       07++12   82.0 77.8 71.6 55.3 42.4 77.3 71.7 89.3 44.5 72.1 53.7 87.7 80.0    82.5   72.7   36.6   68.7   65.4 81.1 62.7 68.8

Table 2. VOC 2010 test detection average precision (%). BabyLearning uses a network based on [17]. All other methods use VGG16.
Training set key: 12: VOC12 trainval, Prop.: proprietary dataset, 12+seg: 12 with segmentation annotations, 07++12: union of VOC07
trainval, VOC07 test, and VOC12 trainval.

method            train set aero bike bird boat bottle bus car cat chair cow table dog horse mbike persn plant sheep sofa train tv        mAP
BabyLearning  Prop.         78.0 74.2 61.3 45.7 42.7 68.2 66.8 80.2 40.6 70.0 49.8 79.0 74.5 77.9 64.0 35.3 67.9 55.7 68.7 62.6           63.2
NUS NIN c2000 Unk.          80.2 73.8 61.9 43.7 43.0 70.3 67.6 80.7 41.9 69.7 51.7 78.2 75.2 76.9 65.1 38.6 68.3 58.0 68.7 63.3           63.8
R-CNN BB [10] 12            79.6 72.7 61.9 41.2 41.9 65.9 66.4 84.6 38.5 67.2 46.7 82.0 74.8 76.0 65.2 35.6 65.4 54.2 67.4 60.3           62.4
FRCN [ours]       12       80.3 74.7 66.9 46.9 37.7 73.9 68.6 87.7 41.7 71.1 51.1 86.0 77.8    79.8   69.8   32.1   65.5   63.8 76.4 61.7 65.7
FRCN [ours]       07++12   82.3 78.4 70.8 52.3 38.7 77.8 71.6 89.3 44.2 73.0 55.0 87.5 80.5    80.8   72.0   35.1   68.3   65.7 80.4 64.2 68.4

Table 3. VOC 2012 test detection average precision (%). BabyLearning and NUS NIN c2000 use networks based on [17]. All other
methods use VGG16. Training set key: see Table 2, Unk.: unknown.

to this CaffeNet as model S, for “small.” The second net-              SegDeepM [25] achieves a higher mAP than Fast R-CNN
work is VGG CNN M 1024 from [3], which has the same                    (67.2% vs. 66.1%). SegDeepM is trained on VOC12 train-
depth as S, but is wider. We call this network model M,                val plus segmentation annotations; it is designed to boost
for “medium.” The final network is the very deep VGG16                 R-CNN accuracy by using a Markov random field to reason
model from [20]. Since this model is the largest, we call              over R-CNN detections and segmentations from the O2 P
it model L. In this section, all experiments use single-scale          [1] semantic-segmentation method. Fast R-CNN can be
training and testing (s = 600; see Section 5.2 for details).           swapped into SegDeepM in place of R-CNN, which may
                                                                       lead to better results. When using the enlarged 07++12
4.2. VOC 2010 and 2012 results                                         training set (see Table 2 caption), Fast R-CNN’s mAP in-
   On these datasets, we compare Fast R-CNN (FRCN, for                 creases to 68.8%, surpassing SegDeepM.
short) against the top methods on the comp4 (outside data)             4.3. VOC 2007 results
track from the public leaderboard (Table 2, Table 3).3 For
the NUS NIN c2000 and BabyLearning methods, there are                      On VOC07, we compare Fast R-CNN to R-CNN and
no associated publications at this time and we could not               SPPnet. All methods start from the same pre-trained
find exact information on the ConvNet architectures used;              VGG16 network and use bounding-box regression. The
they are variants of the Network-in-Network design [17].               VGG16 SPPnet results were computed by the authors of
All other methods are initialized from the same pre-trained            [11]. SPPnet uses five scales during both training and test-
VGG16 network.                                                         ing. The improvement of Fast R-CNN over SPPnet illus-
                                                                       trates that even though Fast R-CNN uses single-scale train-
   Fast R-CNN achieves the top result on VOC12 with a
                                                                       ing and testing, fine-tuning the conv layers provides a large
mAP of 65.7% (and 68.4% with extra data). It is also two
                                                                       improvement in mAP (from 63.1% to 66.9%). R-CNN
orders of magnitude faster than the other methods, which
                                                                       achieves a mAP of 66.0%. As a minor point, SPPnet was
are all based on the “slow” R-CNN pipeline. On VOC10,
                                                                       trained without examples marked as “difficult” in PASCAL.
   3 http://host.robots.ox.ac.uk:8080/leaderboard                      Removing these examples improves Fast R-CNN mAP to
(accessed April 18, 2015)                                              68.1%. All other experiments use “difficult” examples.
4.4. Training and testing time                                                     4.5. Which layers to fine-tune?
   Fast training and testing times are our second main re-                            For the less deep networks considered in the SPPnet pa-
sult. Table 4 compares training time (hours), testing rate                         per [11], fine-tuning only the fully connected layers ap-
(seconds per image), and mAP on VOC07 between Fast R-                              peared to be sufficient for good accuracy. We hypothesized
CNN, R-CNN, and SPPnet. For VGG16, Fast R-CNN pro-                                 that this result would not hold for very deep networks. To
cesses images 146× faster than R-CNN without truncated                             validate that fine-tuning the conv layers is important for
SVD and 213× faster with it. Training time is reduced by                           VGG16, we use Fast R-CNN to fine-tune, but freeze the
9×, from 84 hours to 9.5. Compared to SPPnet, Fast R-                              thirteen conv layers so that only the fully connected layers
CNN trains VGG16 2.7× faster (in 9.5 vs. 25.5 hours) and                           learn. This ablation emulates single-scale SPPnet training
tests 7× faster without truncated SVD or 10× faster with it.                       and decreases mAP from 66.9% to 61.4% (Table 5). This
Fast R-CNN also eliminates hundreds of gigabytes of disk                           experiment verifies our hypothesis: training through the RoI
storage, because it does not cache features.                                       pooling layer is important for very deep nets.

                         Fast R-CNN                  R-CNN               SPPnet                     layers that are fine-tuned in model L SPPnet L
                                                                            †
                         S      M           L       S M             L         L                     ≥ fc6 ≥ conv3 1            ≥ conv2 1     ≥ fc6
 train time (h)        1.2   2.0  9.5              22    28         84       25    VOC07 mAP          61.4         66.9              67.2     63.1
 train speedup      18.3× 14.0× 8.8×              1×    1×         1×     3.4×     test rate (s/im) 0.32           0.32              0.32      2.3
 test rate (s/im)     0.10      0.15      0.32    9.8 12.1 47.0             2.3
                                                                                   Table 5. Effect of restricting which layers are fine-tuned for
  B with SVD          0.06      0.08      0.22      -    -    -               -
                                                                                   VGG16. Fine-tuning ≥ fc6 emulates the SPPnet training algo-
 test speedup          98× 80× 146×               1×    1×         1×      20×     rithm [11], but using a single scale. SPPnet L results were ob-
  B with SVD          169× 150× 213×                -     -          -        -    tained using five scales, at a significant (7×) speed cost.
 VOC07 mAP            57.1      59.2      66.9 58.5 60.2 66.0              63.1
                                                                                      Does this mean that all conv layers should be fine-tuned?
 B with SVD           56.5      58.7      66.6    -    -    -                 -
                                                                                   In short, no. In the smaller networks (S and M) we find
Table 4. Runtime comparison between the same models in Fast R-                     that conv1 is generic and task independent (a well-known
CNN, R-CNN, and SPPnet. Fast R-CNN uses single-scale mode.                         fact [14]). Allowing conv1 to learn, or not, has no mean-
SPPnet uses the five scales specified in [11]. † Timing provided by                ingful effect on mAP. For VGG16, we found it only nec-
the authors of [11]. Times were measured on an Nvidia K40 GPU.                     essary to update layers from conv3 1 and up (9 of the 13
                                                                                   conv layers). This observation is pragmatic: (1) updating
Truncated SVD. Truncated SVD can reduce detection                                  from conv2 1 slows training by 1.3× (12.5 vs. 9.5 hours)
time by more than 30% with only a small (0.3 percent-                              compared to learning from conv3 1; and (2) updating from
age point) drop in mAP and without needing to perform                              conv1 1 over-runs GPU memory. The difference in mAP
additional fine-tuning after model compression. Fig. 2 il-                         when learning from conv2 1 up was only +0.3 points (Ta-
lustrates how using the top 1024 singular values from the                          ble 5, last column). All Fast R-CNN results in this paper
25088 × 4096 matrix in VGG16’s fc6 layer and the top 256                           using VGG16 fine-tune layers conv3 1 and up; all experi-
singular values from the 4096 × 4096 fc7 layer reduces run-                        ments with models S and M fine-tune layers conv2 and up.
time with little loss in mAP. Further speed-ups are possi-
ble with smaller drops in mAP if one fine-tunes again after                        5. Design evaluation
compression.
                                                                                      We conducted experiments to understand how Fast R-
   Forward pass timing                     Forward pass timing (SVD)               CNN compares to R-CNN and SPPnet, as well as to eval-
mAP 66.9% @ 320ms / image                 mAP 66.6% @ 223ms / image                uate design decisions. Following best practices, we per-
         fc6                                                 fc6                   formed these experiments on the PASCAL VOC07 dataset.
      38.7% (122ms)                                 17.5% (37ms) other
                             other                       5.1% (11ms)               5.1. Does multi-task training help?
                  3.5% (11ms) roi_pool5                                roi_pool5
                   5.4% (17ms)                             7.9% (17ms)
                                                            1.7% (4ms) fc7            Multi-task training is convenient because it avoids man-
                   6.2% (20ms) fc7
                                                                                   aging a pipeline of sequentially-trained tasks. But it also has
                                             67.8% (143ms)                         the potential to improve results because the tasks influence
      46.3% (146ms)
                                           conv                                    each other through a shared representation (the ConvNet)
       conv                                                                        [2]. Does multi-task training improve object detection ac-
Figure 2. Timing for VGG16 before and after truncated SVD. Be-                     curacy in Fast R-CNN?
fore SVD, fully connected layers fc6 and fc7 take 45% of the time.                    To test this question, we train baseline networks that
                                                                                   use only the classification loss, Lcls , in Eq. 1 (i.e., setting
                                                   S                                 M                               L
              multi-task training?            X                 X                X                X             X                  X
              stage-wise training?                       X                                 X                               X
              test-time bbox reg?                        X      X                          X      X                        X       X
              VOC07 mAP              52.2   53.3       54.6   57.1   54.7     55.5       56.6   59.2   62.6   63.4       64.0    66.9

         Table 6. Multi-task training (forth column per group) improves mAP over piecewise training (third column per group).

λ = 0). These baselines are printed for models S, M, and L                                       SPPnet ZF            S                 M             L
in the first column of each group in Table 6. Note that these                scales                 1    5        1          5      1          5      1
models do not have bounding-box regressors. Next (second                     test rate (s/im)    0.14 0.38     0.10       0.39   0.15       0.64   0.32
column per group), we take networks that were trained with                   VOC07 mAP           58.0 59.2     57.1       58.4   59.2       60.7   66.9
the multi-task loss (Eq. 1, λ = 1), but we disable bounding-
box regression at test time. This isolates the networks’ clas-              Table 7. Multi-scale vs. single scale. SPPnet ZF (similar to model
sification accuracy and allows an apples-to-apples compar-                  S) results are from [11]. Larger networks with a single-scale offer
                                                                            the best speed / accuracy tradeoff. (L cannot use multi-scale in our
ison with the baseline networks.
                                                                            implementation due to GPU memory constraints.)
    Across all three networks we observe that multi-task
training improves pure classification accuracy relative to
training for classification alone. The improvement ranges                   firm their result: deep ConvNets are adept at directly learn-
from +0.8 to +1.1 mAP points, showing a consistent posi-                    ing scale invariance. The multi-scale approach offers only
tive effect from multi-task learning.                                       a small increase in mAP at a large cost in compute time
    Finally, we take the baseline models (trained with only                 (Table 7). In the case of VGG16 (model L), we are lim-
the classification loss), tack on the bounding-box regression               ited to using a single scale by implementation details. Yet it
layer, and train them with Lloc while keeping all other net-                achieves a mAP of 66.9%, which is slightly higher than the
work parameters frozen. The third column in each group                      66.0% reported for R-CNN [10], even though R-CNN uses
shows the results of this stage-wise training scheme: mAP                   “infinite” scales in the sense that each proposal is warped to
improves over column one, but stage-wise training under-                    a canonical size.
performs multi-task training (forth column per group).                          Since single-scale processing offers the best tradeoff be-
                                                                            tween speed and accuracy, especially for very deep models,
5.2. Scale invariance: to brute force or finesse?                           all experiments outside of this sub-section use single-scale
                                                                            training and testing with s = 600 pixels.
    We compare two strategies for achieving scale-invariant
object detection: brute-force learning (single scale) and im-               5.3. Do we need more training data?
age pyramids (multi-scale). In either case, we define the
scale s of an image to be the length of its shortest side.                      A good object detector should improve when supplied
    All single-scale experiments use s = 600 pixels; s may                  with more training data. Zhu et al. [24] found that DPM [8]
be less than 600 for some images as we cap the longest im-                  mAP saturates after only a few hundred to thousand train-
age side at 1000 pixels and maintain the image’s aspect ra-                 ing examples. Here we augment the VOC07 trainval set
tio. These values were selected so that VGG16 fits in GPU                   with the VOC12 trainval set, roughly tripling the number
memory during fine-tuning. The smaller models are not                       of images to 16.5k, to evaluate Fast R-CNN. Enlarging the
memory bound and can benefit from larger values of s; how-                  training set improves mAP on VOC07 test from 66.9% to
ever, optimizing s for each model is not our main concern.                  70.0% (Table 1). When training on this dataset we use 60k
We note that PASCAL images are 384 × 473 pixels on av-                      mini-batch iterations instead of 40k.
erage and thus the single-scale setting typically upsamples                     We perform similar experiments for VOC10 and 2012,
images by a factor of 1.6. The average effective stride at the              for which we construct a dataset of 21.5k images from the
RoI pooling layer is thus ≈ 10 pixels.                                      union of VOC07 trainval, test, and VOC12 trainval. When
    In the multi-scale setting, we use the same five scales                 training on this dataset, we use 100k SGD iterations and
specified in [11] (s ∈ {480, 576, 688, 864, 1200}) to facili-               lower the learning rate by 0.1× each 40k iterations (instead
tate comparison with SPPnet. However, we cap the longest                    of each 30k). For VOC10 and 2012, mAP improves from
side at 2000 pixels to avoid exceeding GPU memory.                          66.1% to 68.8% and from 65.7% to 68.4%, respectively.
    Table 7 shows models S and M when trained and tested
                                                                            5.4. Do SVMs outperform softmax?
with either one or five scales. Perhaps the most surpris-
ing result in [11] was that single-scale detection performs                    Fast R-CNN uses the softmax classifier learnt during
almost as well as multi-scale detection. Our findings con-                  fine-tuning instead of training one-vs-rest linear SVMs
post-hoc, as was done in R-CNN and SPPnet. To under-                                      This result is difficult to predict without actually running
stand the impact of this choice, we implemented post-hoc                              the experiment. The state-of-the-art for measuring object
SVM training with hard negative mining in Fast R-CNN.                                 proposal quality is Average Recall (AR) [12]. AR correlates
We use the same training algorithm and hyper-parameters                               well with mAP for several proposal methods using R-CNN,
as in R-CNN.                                                                          when using a fixed number of proposals per image. Fig. 3
                                                                                      shows that AR (solid red line) does not correlate well with
           method          classifier       S        M        L                       mAP as the number of proposals per image is varied. AR
           R-CNN [9, 10]   SVM           58.5      60.2     66.0                      must be used with care; higher AR due to more proposals
           FRCN [ours]     SVM           56.3      58.7     66.8                      does not imply that mAP will increase. Fortunately, training
           FRCN [ours]     softmax       57.1      59.2     66.9                      and testing with model M takes less than 2.5 hours. Fast
                                                                                      R-CNN thus enables efficient, direct evaluation of object
Table 8. Fast R-CNN with softmax vs. SVM (VOC07 mAP).
                                                                                      proposal mAP, which is preferable to proxy metrics.
    Table 8 shows softmax slightly outperforming SVM for                                  We also investigate Fast R-CNN when using densely
all three networks, by +0.1 to +0.8 mAP points. This ef-                              generated boxes (over scale, position, and aspect ratio), at
fect is small, but it demonstrates that “one-shot” fine-tuning                        a rate of about 45k boxes / image. This dense set is rich
is sufficient compared to previous multi-stage training ap-                           enough that when each selective search box is replaced by
proaches. We note that softmax, unlike one-vs-rest SVMs,                              its closest (in IoU) dense box, mAP drops only 1 point (to
introduces competition between classes when scoring a RoI.                            57.7%, Fig. 3, blue triangle).
                                                                                          The statistics of the dense boxes differ from those of
5.5. Are more proposals always better?                                                selective search boxes. Starting with 2k selective search
                                                                                      boxes, we test mAP when adding a random sample of
   There are (broadly) two types of object detectors: those
                                                                                      1000 × {2, 4, 6, 8, 10, 32, 45} dense boxes. For each exper-
that use a sparse set of object proposals (e.g., selective
                                                                                      iment we re-train and re-test model M. When these dense
search [21]) and those that use a dense set (e.g., DPM [8]).
                                                                                      boxes are added, mAP falls more strongly than when adding
Classifying sparse proposals is a type of cascade [22] in
                                                                                      more selective search boxes, eventually reaching 53.0%.
which the proposal mechanism first rejects a vast number of
                                                                                          We also train and test Fast R-CNN using only dense
candidates leaving the classifier with a small set to evaluate.
                                                                                      boxes (45k / image). This setting yields a mAP of 52.9%
This cascade improves detection accuracy when applied to
                                                                                      (blue diamond). Finally, we check if SVMs with hard nega-
DPM detections [21]. We find evidence that the proposal-
                                                                                      tive mining are needed to cope with the dense box distribu-
classifier cascade also improves Fast R-CNN accuracy.
                                                                                      tion. SVMs do even worse: 49.3% (blue circle).
   Using selective search’s quality mode, we sweep from 1k
to 10k proposals per image, each time re-training and re-                             5.6. Preliminary MS COCO results
testing model M. If proposals serve a purely computational
                                                                                          We applied Fast R-CNN (with VGG16) to the MS
role, increasing the number of proposals per image should
                                                                                      COCO dataset [18] to establish a preliminary baseline. We
not harm mAP.
                                                                                      trained on the 80k image training set for 240k iterations and
      66                                                             66               evaluated on the “test-dev” set using the evaluation server.
                                              Sel. Search (SS)                        The PASCAL-style mAP is 35.9%; the new COCO-style
      63                                      SS (2k) + Rand Dense 63
                                              SS replace Dense                        AP, which also averages over IoU thresholds, is 19.7%.
      61                                      45k Dense Softmax 61
                                                                     Average Recall

                                              45k Dense SVM                           6. Conclusion
      58                                                             58
mAP

                                                      SS Avg. Recall                      This paper proposes Fast R-CNN, a clean and fast update
      56                                                             56
                                                                                      to R-CNN and SPPnet. In addition to reporting state-of-the-
      53                                                            53                art detection results, we present detailed experiments that
      51                                                            51                we hope provide new insights. Of particular note, sparse
                                                                                      object proposals appear to improve detector quality. This
      49 3                                                          49
        10                              104                                           issue was too costly (in time) to probe in the past, but be-
                     Number of object proposals                                       comes practical with Fast R-CNN. Of course, there may ex-
Figure 3. VOC07 test mAP and AR for various proposal schemes.                         ist yet undiscovered techniques that allow dense boxes to
                                                                                      perform as well as sparse proposals. Such methods, if de-
   We find that mAP rises and then falls slightly as the pro-                         veloped, may help further accelerate object detection.
posal count increases (Fig. 3, solid blue line). This exper-
iment shows that swamping the deep classifier with more                               Acknowledgements. I thank Kaiming He, Larry Zitnick,
proposals does not help, and even slightly hurts, accuracy.                           and Piotr Dollár for helpful discussions and encouragement.
References                                                            [19] P. Sermanet, D. Eigen, X. Zhang, M. Mathieu, R. Fergus,
                                                                           and Y. LeCun. OverFeat: Integrated Recognition, Localiza-
 [1] J. Carreira, R. Caseiro, J. Batista, and C. Sminchisescu. Se-         tion and Detection using Convolutional Networks. In ICLR,
     mantic segmentation with second-order pooling. In ECCV,               2014. 1, 3
     2012. 5                                                          [20] K. Simonyan and A. Zisserman. Very deep convolutional
 [2] R. Caruana. Multitask learning. Machine learning, 28(1),              networks for large-scale image recognition. In ICLR, 2015.
     1997. 6                                                               1, 5
 [3] K. Chatfield, K. Simonyan, A. Vedaldi, and A. Zisserman.         [21] J. Uijlings, K. van de Sande, T. Gevers, and A. Smeulders.
     Return of the devil in the details: Delving deep into convo-          Selective search for object recognition. IJCV, 2013. 8
     lutional nets. In BMVC, 2014. 5                                  [22] P. Viola and M. Jones. Rapid object detection using a boosted
 [4] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-             cascade of simple features. In CVPR, 2001. 8
     Fei. ImageNet: A large-scale hierarchical image database.        [23] J. Xue, J. Li, and Y. Gong. Restructuring of deep neural
     In CVPR, 2009. 2                                                      network acoustic models with singular value decomposition.
 [5] E. Denton, W. Zaremba, J. Bruna, Y. LeCun, and R. Fergus.             In Interspeech, 2013. 4
     Exploiting linear structure within convolutional networks for    [24] X. Zhu, C. Vondrick, D. Ramanan, and C. Fowlkes. Do we
     efficient evaluation. In NIPS, 2014. 4                                need more training data or better models for object detec-
 [6] D. Erhan, C. Szegedy, A. Toshev, and D. Anguelov. Scalable            tion? In BMVC, 2012. 7
     object detection using deep neural networks. In CVPR, 2014.      [25] Y. Zhu, R. Urtasun, R. Salakhutdinov, and S. Fidler.
     3                                                                     segDeepM: Exploiting segmentation and context in deep
 [7] M. Everingham, L. Van Gool, C. K. I. Williams, J. Winn, and           neural networks for object detection. In CVPR, 2015. 1,
     A. Zisserman. The PASCAL Visual Object Classes (VOC)                  5
     Challenge. IJCV, 2010. 1
 [8] P. Felzenszwalb, R. Girshick, D. McAllester, and D. Ra-
     manan. Object detection with discriminatively trained part
     based models. TPAMI, 2010. 3, 7, 8
 [9] R. Girshick, J. Donahue, T. Darrell, and J. Malik. Rich fea-
     ture hierarchies for accurate object detection and semantic
     segmentation. In CVPR, 2014. 1, 3, 4, 8
[10] R. Girshick, J. Donahue, T. Darrell, and J. Malik. Region-
     based convolutional networks for accurate object detection
     and segmentation. TPAMI, 2015. 5, 7, 8
[11] K. He, X. Zhang, S. Ren, and J. Sun. Spatial pyramid pooling
     in deep convolutional networks for visual recognition. In
     ECCV, 2014. 1, 2, 3, 4, 5, 6, 7
[12] J. H. Hosang, R. Benenson, P. Dollár, and B. Schiele. What
     makes for effective detection proposals? arXiv preprint
     arXiv:1502.05082, 2015. 8
[13] Y. Jia, E. Shelhamer, J. Donahue, S. Karayev, J. Long, R. Gir-
     shick, S. Guadarrama, and T. Darrell. Caffe: Convolutional
     architecture for fast feature embedding. In Proc. of the ACM
     International Conf. on Multimedia, 2014. 2
[14] A. Krizhevsky, I. Sutskever, and G. Hinton. ImageNet clas-
     sification with deep convolutional neural networks. In NIPS,
     2012. 1, 4, 6
[15] S. Lazebnik, C. Schmid, and J. Ponce. Beyond bags of
     features: Spatial pyramid matching for recognizing natural
     scene categories. In CVPR, 2006. 1
[16] Y. LeCun, B. Boser, J. Denker, D. Henderson, R. Howard,
     W. Hubbard, and L. Jackel. Backpropagation applied to
     handwritten zip code recognition. Neural Comp., 1989. 1
[17] M. Lin, Q. Chen, and S. Yan. Network in network. In ICLR,
     2014. 5
[18] T. Lin, M. Maire, S. Belongie, L. Bourdev, R. Girshick,
     J. Hays, P. Perona, D. Ramanan, P. Dollár, and C. L. Zit-
     nick. Microsoft COCO: common objects in context. arXiv
     e-prints, arXiv:1405.0312 [cs.CV], 2014. 8
