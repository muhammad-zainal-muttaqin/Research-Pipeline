---
source_id: 161
bibtex_key: sun2021sparsercnn
title: Sparse R-CNN: End-to-End Object Detection with Learnable Proposals
year: 2021
domain_theme: Fondasi RGB
verified_pdf: 161_Sparse R-CNN.pdf
char_count: 67359
---

Sparse R-CNN: End-to-End Object Detection with Learnable Proposals

                                               Peize Sun1∗ , Rufeng Zhang2∗ , Yi Jiang3∗ , Tao Kong3 , Chenfeng Xu4 , Wei Zhan4 ,
                                                    Masayoshi Tomizuka4 , Lei Li3 , Zehuan Yuan3 , Changhu Wang3 , Ping Luo1
                                                                                  1
                                                                                   The University of Hong Kong 2 Tongji University
                                                                             3
                                                                                 ByteDance AI Lab 4 University of California, Berkeley
arXiv:2011.12450v2 [cs.CV] 26 Apr 2021

                                                                                                         k anchor
                                                                                                          boxes
                                                                                                     W                     N predicted                                  N learned
                                                                                                                    …       proposals                                   proposals
                                                                                                                                                                  …
                                                                  k anchor                       H
                                                                                                           …
                                                                   boxes
                                                              W
                                                                                  class                                                class                                         class
                                                          H                                                                                                                          box
                                                                    …             box                                                  box

                                                      (a) Dense: RetinaNet                   (b) Dense-to-Sparse: Faster R-CNN                           (c) Sparse: Sparse R-CNN

                                          Figure 1 – Comparisons of different object detection pipelines. (a) In dense detectors, HW k object candidates enumerate on all image
                                          grids, e.g. RetinaNet [29]. (b) In dense-to-sparse detectors, they select a small set of N candidates from dense HW k object candidates,
                                          and then extract image features within corresponding regions by pooling operation, e.g. Faster R-CNN [37]. (c) Our proposed Sparse
                                          R-CNN, directly provides a small set of N learned object proposals. Here N  HW k.

                                                                                                                                  50
                                                                        Abstract
                                                                                                                                  45
                                             We present Sparse R-CNN, a purely sparse method for                                                                                    500 epochs
                                                                                                                                  40
                                         object detection in images. Existing works on object de-
                                                                                                                        COCO AP

                                         tection heavily rely on dense object candidates, such as                                 35
                                         k anchor boxes pre-defined on all grids of image feature                                 30                                          RetinaNet
                                         map of size H × W . In our method, however, a fixed
                                         sparse set of learned object proposals, total length of N ,                              25                                          Faster R-CNN
                                         are provided to object recognition head to perform classifi-                             20                                          DETR
                                                                                                                                                    3x schedule               Sparse R-CNN
                                         cation and location. By eliminating HW k (up to hundreds                                 15
                                         of thousands) hand-designed object candidates to N (e.g.                                      0       20   40     60     80    100         120      140
                                         100) learnable proposals, Sparse R-CNN completely avoids
                                                                                                                                                           Training Epochs
                                         all efforts related to object candidates design and many-to-
                                         one label assignment. More importantly, final predictions
                                                                                                                           Figure 2 – Convergence curves of RetinaNet, Faster R-CNN,
                                         are directly output without non-maximum suppression post-                         DETR and Sparse R-CNN on COCO val2017 [30]. Sparse
                                         procedure. Sparse R-CNN demonstrates accuracy, run-time                           R-CNN achieves competitive performance in terms of training
                                         and training convergence performance on par with the well-                        efficiency and detection quality.
                                         established detector baselines on the challenging COCO
                                         dataset, e.g., achieving 45.0 AP in standard 3× train-
                                         ing schedule and running at 22 fps using ResNet-50 FPN                         1. Introduction
                                         model. We hope our work could inspire re-thinking the con-
                                         vention of dense prior in object detectors. The code is avail-                    Object detection aims at localizing a set of objects and
                                         able at: https://github.com/PeizeSun/SparseR-CNN .                             recognizing their categories in an image. Dense prior has
                                                                                                                        always been cornerstone to success in detectors. In classic
                                                                                                                        computer vision, the sliding-window paradigm, in which a
                                            * Equal contribution.                                                       classifier is applied on a dense image grid, is leading de-
tection method for decades [8, 12, 48]. Modern mainstream        by RoIPool [13] or RoIAlign [18].
one-stage detectors pre-define marks on a dense feature map          The learnable proposal boxes are the statistics of poten-
grid, such as anchors boxes [29, 36], shown in Figure 1a, or     tial object location in the image. Whereas, the 4-d coor-
reference points [45, 61], and predict the relative scaling      dinate is merely a rough representation of object and lacks
and offsets to bounding boxes of objects, as well as the cor-    a lot of informative details such as pose and shape. Here
responding categories. Although two-stage pipelines work         we introduce another key concept termed proposal feature,
on a sparse set of proposal boxes, their proposal genera-        which is a high-dimension (e.g., 256) latent vector. Com-
tion algorithms are still built on dense candidates [14, 37],    pared with rough bounding box, it is expected to encode
shown in Figure 1b.                                              the rich instance characteristics. Specially, proposal feature
    These well-established methods are conceptually intu-        generates a series of customized parameters for its exclusive
itive and offer robust performance [11, 30], together with       object recognition head. We call this operation Dynamic In-
fast training and inference time [53]. Besides their great       stance Interactive Head, since it shares similarities with re-
success, it is important to note that dense-prior detectors      cent dynamic scheme [23, 44]. Compared to the shared 2-fc
suffer some limitations: 1) Such pipelines usually pro-          layers in [37], our head is more flexible and holds a signif-
duce redundant and near-duplicate results, thus making           icant lead in accuracy. We show in our experiment that the
non-maximum suppression (NMS) [1, 51] post-processing            formulation of head conditioned on unique proposal feature
a necessary component. 2) The many-to-one label assign-          instead of the fixed parameters is actually the key to Sparse
ment problem [2, 58, 60] in training makes the network sen-      R-CNN’s success. Both proposal boxes and proposal fea-
sitive to heuristic assign rules. 3) The final performance is    tures are randomly initialized and optimized together with
largely affected by sizes, aspect ratios and number of an-       other parameters in the whole network.
chor boxes [29, 36], density of reference points [24, 45, 61]        The most remarkable property in our Sparse R-CNN is
and proposal generation algorithm [14, 37].                      its sparse-in sparse-out paradigm in the whole time. The
    Despite the dense convention is widely recognized            initial input is a sparse set of proposal boxes and proposal
among object detectors, a natural question to ask is: Is         features, together with the one-to-one dynamic instance in-
it possible to design a sparse detector? Recently, DETR          teraction. Neither dense candidates [29, 37] nor interacting
proposes to reformulate object detection as a direct and         with global(dense) feature [3] exists in the pipeline. This
sparse set prediction problem [3], whose input is merely         pure sparsity makes Sparse R-CNN a brand new member in
100 learned object queries [47]. The final set of predic-        R-CNN family.
tions are output directly without any hand-designed post-            Sparse R-CNN demonstrates its accuracy, run-time and
processing. In spite of its simple and fantastic framework,      training convergence performance on par with the well-
DETR requires each object query to interact with global im-      established detectors [2, 37, 45] on the challenging COCO
age context. This dense property not only slows down its         dataset [30], e.g., achieving 45.0 AP in standard 3× train-
training convergence [63], but also blocks it establishing a     ing schedule and running at 22 fps using ResNet-50 FPN
thoroughly sparse pipeline for object detection.                 model. To our best knowledge, the proposed Sparse R-CNN
    We believe the sparse property should be in two aspects:     is the first work that demonstrates a considerably sparse de-
sparse boxes and sparse features. Sparse boxes mean that a       sign is qualified yet. We hope our work could inspire re-
small number of starting boxes (e.g. 100) is enough to pre-      thinking the necessary of dense prior in object detection and
dict all objects in an image. While sparse features indicate     exploring next generation of object detector.
the feature of each box does not need to interact with all
other features over the full image. From this perspective,       2. Related Work
DETR is not a pure sparse method since each object query
must interact with dense features over full images.              Dense method. Sliding-window paradigm has been popu-
    In this paper, we propose Sparse R-CNN, a purely sparse      lar for many years in object detection. Limited by classi-
method, without object positional candidates enumerating         cal feature extraction techniques [8, 48], the performance
on all(dense) image grids nor object queries interacting         has plateaued for decades and the application scenarios are
with global(dense) image feature. As shown in Figure 1c,         limited. Development of deep convolution neural networks
object candidates are given with a fixed small set of learn-     (CNNs) [19, 22, 25] cultivates general object detection
able bounding boxes represented by 4-d coordinate. For ex-       achieving significant improvement in performance [11, 30].
ample of COCO dataset [30], 100 boxes and 400 parameters         One of mainstream pipelines is one-stage detector, which
are needed in total, rather than the predicted ones from hun-    directly predicts the category and location of anchor boxes
dreds of thousands of candidates in Region Proposal Net-         densely covering spatial positions, scales, and aspect ratios
work (RPN) [37]. These sparse candidates are used as pro-        in a single-shot way, such as OverFeat [40], YOLO [36],
posal boxes to extract the feature of Region of Interest (RoI)   SSD [31] and RetinaNet [29]. Recently, anchor-free al-
gorithms [21, 26, 45, 61, 24] are proposed to make this
pipeline much simpler by replacing hand-crafted anchor
boxes with reference points. All of above methods are built
                                                                                               Dynamic Head k
on dense candidates and each candidate is directly classified
and regressed. These candidates are assigned to ground-                                                                     Cls
truth object boxes in training time based on a pre-defined                                                                  Reg
principle, e.g., whether the anchor has a higher intersection-
over-union (IoU) threshold with its corresponding ground                      k-th box                   k-th feature
truth, or whether the reference point falls in one of object
boxes. Moreover, NMS post-processing [1, 51] is needed to                        …                           …
remove redundant predictions during inference time.                 Proposal Boxes: N*4       Proposal Features: N*d
Dense-to-sparse method. Two-stage detector is another
mainstream pipeline and has dominated modern object de-           Figure 3 – An overview of Sparse R-CNN pipeline. The input
tection for years [2, 6, 13, 14, 37]. This paradigm can be        includes an image, a set of proposal boxes and proposal features,
viewed as an extension of dense detector. It first obtains a      where the latter two are learnable parameters. The backbone
sparse set of foreground proposal boxes from dense region         extracts feature map, each proposal box and proposal feature are
                                                                  fed into its exclusive dynamic head to generate object feature,
candidates, and then refines location of each proposal and
                                                                  and finally outputs classification and location.
predicts its specific category. The region proposal algorithm
plays an important role in the first stage in these two-stage
methods, such as Selective Search [46] in R-CNN and Re-
gion Proposal Networks (RPN) [37] in Faster R-CNN. Sim-          100). The pipeline is shown in Figure 3.
ilar to dense pipeline, it also needs NMS post-processing           Sparse R-CNN is a simple, unified network composed
and hand-crafted label assignment. There are only a few of       of a backbone network, a dynamic instance interactive head
foreground proposals from hundreds of thousands of can-          and two task-specific prediction layers. There are three in-
didates, thus these detectors can be concluded as dense-to-      puts in total, an image, a set of proposal boxes and proposal
sparse methods.                                                  features. The latter two are learnable and can be optimized
    Recently, DETR [3] is proposed to directly output the        together with other parameters in network. We will describe
predictions without any hand-crafted components, achiev-         each components in this section in details.
ing promising performance. DETR utilizes a sparse set of
object queries, to interact with global(dense) image feature,    Backbone. Feature Pyramid Network (FPN) based on
in this view, it can be seen as another dense-to-sparse for-     ResNet architecture [19, 28] is adopted as the backbone net-
mulation.                                                        work to produce multi-scale feature maps from input image.
                                                                 Following [28], we construct the pyramid with levels P2
Sparse method. Sparse object detection has the potential to      through P5 , where l indicates pyramid level and Pl has res-
eliminate efforts to design dense candidates, but usually has    olution 2l lower than the input. All pyramid levels have
trailed the accuracy of above dense detectors. G-CNN [34]        C = 256 channels. Please refer to [28] for more details.
can be viewed as a precursor to this group of algorithms.        Actually, Sparse R-CNN has the potential to benefit from
It starts with a multi-scale regular grid over the image and     more complex designs to further improve its performance,
iteratively updates the boxes to cover and classify objects.     such as stacked encoder layers [3] and deformable convo-
This hand-designed regular prior is obviously sub-optimal        lution network [7], on which a recent work Deformable-
and fails to achieve top performance. Instead, our Sparse        DETR [63] is built. However, we align the setting with
R-CNN applies learnable proposals and achieves better per-       Faster R-CNN [37, 28] to show the simplicity and effec-
formance. Concurrently, Deformable-DETR [63] is intro-           tiveness of our method.
duced to restrict each object query to attend to a small set
of key sampling points around the reference points, instead      Learnable proposal box. A fixed small set of learnable
of all points in feature map. We hope sparse methods could       proposal boxes (N ×4) are used as region proposals, instead
serve as solid baseline and help ease future research in ob-     of the predictions from Region Proposal Network (RPN).
ject detection community.                                        These proposal boxes are represented by 4-d parameters
                                                                 ranging from 0 to 1, denoting normalized center coordi-
3. Sparse R-CNN                                                  nates, height and width. The parameters of proposal boxes
                                                                 will be updated with the back-propagation algorithm during
  The key idea of Sparse R-CNN framework is to replace           training. Thanks to the learnable property, we find in our
hundreds of thousands of candidates from Region Proposal         experiment that the effect of initialization is minimal, thus
Network (RPN) with a small set of proposal boxes (e.g.,          making the framework much more flexible.
def dynamic instance interaction(pro feats, roi feats):                Figure 4 illustrates the dynamic instance interaction. In
    # pro feats: (N, C)                                            our design, proposal feature and proposal box are in one-
    # roi feats: (N, S∗S, C)
                                                                   to-one correspondence. For N proposal boxs, N proposal
   # parameters of two 1x1 convs: (N, 2 ∗ C ∗ C/4)                 features are employed. Each RoI feature fi (S × S, C) will
   dynamic params = linear1(pro features)
   # parameters of first conv: (N, C, C/4)
                                                                   interact with the corresponding proposal feature pi (C) to
   param1 = dynamic params[:, :C∗C/4].view(N, C, C/4)              filter out ineffective bins and outputs the final object feature
   # parameters of second conv: (N, C/4, C)                        (C). For light design, we carry out two consecutive 1 × 1
   param2 = dynamic params[:, C∗C/4:].view(N, C/4, C)
                                                                   convolutions with ReLU activation function, to implement
   # instance interaction for roi features: (N, S∗S, C)            the interaction process. The parameters of these two convo-
   roi feats = relu(norm(bmm(roi feats, param1)))
   roi feats = relu(norm(bmm(roi feats, param2)))                  lutions are generated by corresponding proposal feature.

   # roi feats are flattened: (N, S∗S∗C)
                                                                      The implementation details of interactive head is not cru-
   roi feats = roi feats.flatten(1)                                cial as long as parallel operation is supported for efficiency.
   # obj feats: (N, C)                                             The final regression prediction is computed by a 3-layer per-
   obj feats = linear2(roi feats)
   return obj feats                                                ception, and classification prediction is by a linear projec-
                                                                   tion layer.
 Figure 4 – Pseudo-code of dynamic instance interaction, the k-
                                                                       We also adopt the iteration structure [2] and self-
 th proposal feature generates dynamic parameters for the corre-
 sponding k-th RoI. bmm: batch matrix multiplication; linear:
                                                                   attention module [47] to further improve the performance.
 linear projection.                                                For iteration structure, the newly generated object boxes
                                                                   and object features will serve as the proposal boxes and pro-
                                                                   posal features of the next stage in iterative process. Thanks
                                                                   to the sparse property and light dynamic head, it introduces
    Conceptually, these learned proposal boxes are the statis-     only a marginal computation overhead. Before dynamic in-
tics of potential object location in the training set and can be   stance interaction, self-attention module is applied to the set
seen as an initial guess of the regions that are most likely to    of object features to reason about the relations between ob-
encompass the objects in the image, regardless of the input.       jects. We note that [20] also utilizes self-attention module.
Whereas, the proposals from RPN are strongly correlated            However, it demands geometry attributes and complex rank
to the current image and provide coarse object locations.          feature in addition to object feature. Our module is much
We rethink that the first-stage locating is luxurious in the       more simple and only takes object feature as input.
presence of later stages to refine the location of boxes. In-
stead, a reasonable statistic can already be qualified candi-      Set prediction loss. Sparse R-CNN applies set prediction
dates. In this view, Sparse R-CNN can be categorized as            loss [3, 42, 56] on the fixed-size set of predictions of clas-
the extension of object detector paradigm from thoroughly          sification and box coordinates. Set-based loss produces an
dense [29, 31, 35, 45] to dense-to-sparse [2, 6, 14, 37] to        optimal bipartite matching between predictions and ground
thoroughly sparse, shown in Figure 1.                              truth objects. The matching cost is defined as follows:

Learnable proposal feature. Though the 4-d proposal box
is a brief and explicit expression to describe objects, it pro-           L = λcls · Lcls + λL1 · LL1 + λgiou · Lgiou          (1)
vides a coarse localization of objects and a lot of informa-
tive details are lost, such as object pose and shape. Here we      Here Lcls is focal loss [29] of predicted classifications and
introduce another concept termed proposal feature (N × d),         ground truth category labels, LL1 and Lgiou are L1 loss and
it is a high-dimension (e.g., 256) latent vector and is ex-        generalized IoU loss [38] between normalized center coor-
pected to encode the rich instance characteristics. The num-       dinates and height and width of predicted boxes and ground
ber of proposal features is same as boxes, and we will dis-        truth box, respectively. λcls , λL1 and λgiou are coefficients
cuss how to use it next.                                           of each component. The training loss is the same as the
Dynamic instance interactive head.                                 matching cost except that only performed on matched pairs.
   Given N proposal boxes, Sparse R-CNN first utilizes the         The final loss is the sum of all pairs normalized by the num-
RoIAlign operation to extract features for each box. Then          ber of objects inside the training batch.
each box feature will be used to generate the final predic-           R-CNN families [2, 60] have always been puzzled by
tions using our prediction head. Motivated by dynamic al-          label assignment problem since many-to-one matching re-
gorithms [23, 44], we propose Dynamic Instance Interactive         mains. Here we provide new possibilities that directly by-
Head. Each RoI feature is fed into its own exclusive head          passing many-to-one matching and introducing one-to-one
for object location and classification, where each head is         matching with set-based loss. This is an attempt towards
conditioned on specific proposal feature.                          exploring end-to-end object detection.
      Method                                Feature           Epochs     AP      AP50     AP75      APs     APm      APl     FPS
      RetinaNet-R50 [53]                      FPN               36       38.7    58.0     41.5      23.3    42.3     50.3     24
      RetinaNet-R101 [53]                     FPN               36       40.4    60.2     43.2      24.0    44.3     52.2     18
      Faster R-CNN-R50 [53]                   FPN               36       40.2    61.0     43.8      24.2    43.5     52.0     26
      Faster R-CNN-R101 [53]                  FPN               36       42.0    62.5     45.9      25.2    45.6     54.6     20
      Cascade R-CNN-R50 [53]                  FPN               36       44.3    62.2     48.0      26.6    47.7     57.7     19
      DETR-R50 [3]                          Encoder            500       42.0    62.4     44.2      20.5    45.8     61.1     28
      DETR-R101 [3]                         Encoder            500       43.5    63.8     46.4      21.9    48.0     61.8     20
      DETR-DC5-R50 [3]                      Encoder            500       43.3    63.1     45.9      22.5    47.3     61.1     12
      DETR-DC5-R101 [3]                     Encoder            500       44.9    64.7     47.7      23.7    49.5     62.3     10
      Deformable DETR-R50 [63]           DeformEncoder          50       43.8    62.6     47.7      26.4    47.1     58.0     19
      Sparse R-CNN-R50                        FPN               36       42.8    61.2     45.7      26.7    44.6     57.6     23
      Sparse R-CNN-R101                       FPN               36       44.1    62.1     47.2      26.1    46.3     59.7     19
      Sparse R-CNN*-R50                       FPN               36       45.0    63.4     48.2      26.9    47.2     59.5     22
      Sparse R-CNN*-R101                      FPN               36       46.4    64.6     49.5      28.3    48.3     61.6     18
 Table 1 – Comparisons with different object detectors on COCO 2017 val set. The top section shows results from Detectron2 [53] or
 original papers [3, 63]. Here “∗” indicates that the model is with 300 learnable proposal boxes and random crop training augmentation,
 similar to Deformable DETR [63]. Run time is evaluated on NVIDIA Tesla V100 GPU.

          Method                       Backbone             TTA        AP       AP50      AP75      APs       APm       APl
          CornerNet [26]            Hourglass-104                      40.6     56.4      43.2      19.1      42.8      54.3
          CenterNet [61]            Hourglass-104                      42.1     61.1      45.9      24.1      45.5      52.8
          RepPoint [57]            ResNet-101-DCN                      45.0     66.1      49.0      26.6      48.6      57.5
          FCOS [45]               ResNeXt-101-DCN                      46.6     65.9      50.8      28.6      49.1      58.6
          ATSS [60]               ResNeXt-101-DCN            X         50.7     68.9      56.3      33.2      52.9      62.4
          YOLO [49]                CSPDarkNet-53                       47.5     66.2      51.7      28.2      51.2      59.8
          EfficientDet [43]         EfficientNet-B5                    51.5     70.5      56.1       -         -         -
          Sparse R-CNN               ResNeXt-101                       46.9     66.3      51.2      28.6      49.2      58.7
          Sparse R-CNN            ResNeXt-101-DCN                      48.9     68.3      53.4      29.9      50.9      62.4
          Sparse R-CNN            ResNeXt-101-DCN            X         51.5     71.1      57.1      34.2      53.4      64.1
 Table 2 – Comparisons with different object detectors on COCO 2017 test-dev set. The top section shows results from original papers.
 “TTA” indicates test-time augmentations, following the settings in [60].

4. Experiments                                                         pixels while the longest at most 1333. Following [3, 63],
                                                                       λcls = 2, λL1 = 5, λgiou = 2. The default number of
Dataset. Our experiments are conducted on the challeng-                proposal boxes, proposal features and iteration is 100, 100
ing MS COCO benchmark [30] using the standard met-                     and 6, respectively. To stabilize training, the gradients are
rics for object detection. All models are trained on the               blocked at proposal boxes in each stage of iterative archi-
COCO train2017 split (∼118k images) and evaluated                      tecture, except initial proposal boxes.
with val2017 (5k images).                                              Inference details. The inference process is quite simple
Training details. ResNet-50 [19] is used as the back-                  in Sparse R-CNN. Given an input image, Sparse R-CNN
bone network unless otherwise specified. The optimizer is              directly predicts 100 bounding boxes associated with their
AdamW [33] with weight decay 0.0001. The mini-batch is                 scores. The scores indicate the probability of boxes con-
16 images and all models are trained with 8 GPUs. Default              taining an object. For evaluation, we directly use these 100
training schedule is 36 epochs and the initial learning rate           boxes without any post-processing.
is set to 2.5 × 10−5 , divided by 10 at epoch 27 and 33, re-
                                                                       4.1. Main Result
spectively. The backbone is initialized with the pre-trained
weights on ImageNet [9] and other newly added layers are                  We provide two versions of Sparse R-CNN for fair com-
initialized with Xavier [15]. Data augmentation includes               parison with different detectors in Table 1. The first one
random horizontal, scale jitter of resizing the input images           adopts 100 learnable proposal boxes without random crop
such that the shortest side is at least 480 and at most 800            data augmentation, and is used to make comparison with
 Sparse     Iterative    Dynamic           AP              AP50           AP75            APs           APm              APl
    X                                 18.5             35.0           17.7            8.3            21.7           26.4
    X           X                     32.2 (+13.7)     47.5 (+12.5)   34.4 (+16.7)    18.2 (+9.9)    35.2 (+13.5)   41.7 (+15.3)
    X           X           X         42.3 (+10.1)     61.2 (+13.7)   45.7 (+11.3)    26.7 (+8.5)    44.6 (+9.4)    57.6 (+15.9)
 Table 3 – Ablation studies on each components in Sparse R-CNN. Starting from Faster R-CNN, we gradually add learnable proposal
 boxes, iterative architecture, and dynamic head in Sparse R-CNN. All models are trained with set prediction loss.

  Cascade      Feature reuse         AP         AP50     AP75         schedule (36 epochs vs. 50 epochs).
                                                                         The inference time of Sparse R-CNN is on par with other
                                18.5            35.0     17.7         detectors. We notice that the model with 100 proposals is
     X                          20.5(+2.0)      29.3     20.7         running at 23 FPS, while 300 proposals only decreases to
     X              X           32.2(+11.7)     47.5     34.4         22 FPS, thanks to the light design of the dynamic instance
 Table 4 – The effect of feature reuse in iterative architecture.     interactive head.
 Original cascading implementation makes no big difference.              Table 2 compares Sparse R-CNN with other methods in
 Concatenating object feature of previous stage to object feature     COCO test-dev set. Using ResNeXt-101 [55] as back-
 of current stage leads to a huge improvement.
                                                                      bone, Sparse R-CNN achieves 46.9 AP without bells and
                                                                      whistles, 48.9 AP with DCN [7]. With additional test-time
   Self-att.    Ins. interact       AP        AP50     AP75
                                                                      augmentations, Sparse R-CNN achieves 51.5 AP, on par
                                32.2           47.5    34.4           with state-of-the-art methods.
        X                       37.2(+5.0)     54.8    40.1
        X            X          42.3(+5.1)     61.2    45.7
                                                                      4.2. Module Analysis
 Table 5 – The effect of instance-interaction in dynamic head.          In this section, we analyze each component in Sparse R-
 Without instance interaction, dynamic head degenerates to self-      CNN. All models are based on ResNet50-FPN backbone,
 attention. The gain comes from both self-attention and instance-     100 proposals, 3x training schedule, unless otherwise noted.
 interaction.
                                                                      Learnable proposal box. Starting with Faster R-CNN, we
                                                                      naively replace RPN with a sparse set of learnable proposal
mainstream object detectors, e.g. Faster R-CNN and Reti-              boxes. The performance drops from 40.2 AP (Table 1 line
naNet [53]. The second one leverages 300 learnable pro-               3) to 18.5 (Table 3). We find that there is no noticeable
posal boxes with random crop data augmentations, and is               improvement even more fully-connected layers are stacked.
used to make comparison with DETR-series models [3, 63].
   As shown in Table 1, Sparse R-CNN outperforms well-                Iterative architecture. Iteratively updating the boxes is an
established mainstream detectors, such as RetinaNet and               intuitive idea to improve its performance. However, we find
Faster R-CNN, by a large margin. Surprisingly, Sparse R-              that a simple cascade architecture does not make a big dif-
CNN based on ResNet-50 achieves 42.8 AP, which has al-                ference, as shown in Table 4. We analyze the reason is that
ready competed with Faster R-CNN on ResNet-101 in ac-                 compared with refined proposal boxes in [2] which mainly
curacy.                                                               locating around the objects, the candidates in our case are
   We note that DETR and Deformable DETR usually em-                  much more coarse, making it hard to be optimized. We ob-
ploy stronger feature extracting method, such as stacked en-          serve that the target object for one proposal box is usually
coder layers and deformable convolution. The stronger im-             consistent in the whole iterative process. Therefore, the ob-
plementation of Sparse R-CNN is used to give a more fair              ject feature in previous stage can be reused to play a strong
comparison with these detectors. Sparse R-CNN exhibits                cue for the next stage, for example, the object feature en-
higher accuracy even using the simple FPN as feature ex-              codes rich information such as object pose and location. To
tracting method. Moreover, Sparse R-CNN gets much bet-                this end, we concatenate object feature of the previous stage
ter detection performance on small objects compared with              to the current stage. This minor change of feature reuse re-
DETR (26.7 AP vs. 22.5 AP).                                           sults in a huge gain of 11.7 AP on basis of original cascade
   The training convergence speed of Sparse R-CNN is 10×              architecture. Finally, the iterative architecture brings 13.7
faster over DETR, as shown in Figure 2. Since proposed,               AP improvement, as shown in second row of Table 3.
DETR has been suffering from slow convergence, which                  Dynamic head. The dynamic head uses object feature of
motivates the proposal of Deformable DETR. Compared                   previous stage in a different way with iterative architec-
with Deformable DETR, Sparse R-CNN exhibits better per-               ture discussed above. Instead of simply concatenating, the
formance in accuracy (45.0 AP vs. 43.8 AP) and shorter                object feature of previous stage is first processed by self-
running-time (22 FPS vs. 19 FPS), with shorter training               attention module, and then used as proposal feature to im-
    Init.       AP       AP50     AP75     APs     APm       APl         Method                          AP             AP50 AP75
  Center        41.5     59.6     45.0     25.6     43.9     56.1        Multi-head Attention [47] 35.7                 54.9     37.7
  Image         42.3     61.2     45.7     26.7     44.6     57.6        Dynamic head              42.3(+6.6)           61.2     45.7
   Grid         41.0     59.4     44.2     23.8     43.7     55.6       Table 9 – Dynamic head vs. Multi-head Attention. As object
 Random         42.1     60.3     45.3     24.5     44.6     57.9       recognition head, dynamic head outperforms multi-head atten-
 Table 6 – Effect of initialization of proposal boxes. Detec-           tion.
 tion performance is relatively robust to initialization of proposal
 boxes.
                                                                        Method              Pos. encoding AP              AP50 AP75
                                                                        DETR [3]                  X         40.6        61.6  -
   Proposals     AP      AP50     AP75    FPS     Training time
                                                                        DETR [3]                            32.8 (-7.8) 55.2  -
      100        42.3     61.2    45.7     23          19h              Sparse R-CNN              X         41.9        60.9 45.0
      300        43.9     62.3    47.4     22          24h              Sparse R-CNN                        42.3(+0.4) 61.2 45.7
      500        44.6     63.2    48.5     20          60h
                                                                        Table 10 – Proposal feature vs. Object query. Object query is
 Table 7 – Effect of number of proposals. Increasing number of          learned positional encoding, while proposal feature is irrelevant
 proposals leads to continuous improvement, while more propos-          to position.
 als take more training time.

  Stages       AP       AP50     AP75    FPS      Training time             distribution.

      1        21.7     36.7     22.3     35           12h             From Table 6 we show that the final performance of Sparse
      2        36.2     52.8     38.8     33           13h             R-CNN is relatively robust to the initialization of proposal
      3        39.9     56.8     43.2     29           15h             boxes.
      6        42.3     61.2     45.7     23           19h             Number of proposals. The number of proposals largely
     12        41.6     60.2     45.0     17           30h             effects both dense and sparse detectors. Original Faster
 Table 8 – Effect of number of stages. Gradually increasing the        R-CNN uses 300 proposals [37]. Later on it increases to
 number of stages, the performance is saturated at 6 stages.           2000 [53] and obtains better performance. We also study
                                                                       the effect of proposal numbers on Sparse R-CNN in Ta-
plement instance interaction of current stage. The self-               ble 7. Increasing proposal number from 100 to 500 leads
attention module is applied to the set of object features              to continuous improvement, indicating that our framework
for reasoning about the relation between objects. Table 5              is easily to be used in various circumstances. Whereas, 500
shows the benefit of self-attention and dynamic instance in-           proposals take much more training time, so we choose 100
teraction. Finally, Sparse R-CNN achieves accuracy perfor-             and 300 as the main configurations.
mance of 42.3 AP.
                                                                       Number of stages in iterative architecture. Iterative ar-
Initialization of proposal boxes. The dense detectors                  chitecture is a widely-used technique to improve object de-
always heavily depend on design of object candidates,                  tection performance [2, 3, 48], especially for Sparse R-
whereas, object candidates in Sparse R-CNN are learnable               CNN. Table 8 shows the effect of stage numbers in iterative
and thus, all efforts related to designing hand-crafted an-            architecture. Without iterative architecture, performance is
chors are avoided. However, one may concern that the ini-              merely 21.7 AP. Considering the input proposals of first
tialization of proposal boxes plays a key role in Sparse R-            stage is a guess of possible object positions, this result is not
CNN. Here we study the effect of different methods for ini-            surprising. Increasing to 2 stage brings in a gain of 14.5 AP,
tializing proposal boxes:                                              up to competitive 36.2 AP. Gradually increasing the num-
                                                                       ber of stages, the performance is saturated at 6 stages. We
   • “Center” means all proposal boxes are located in the
                                                                       choose 6 stages as the default configuration.
     center of image at beginning, height and width is set to
     0.1 of image size.                                                Dynamic head vs. Multi-head Attention. As discussed
                                                                       in Section 3, dynamic head uses proposal feature to filter
   • “Image” means all proposal boxes are initialized as the           RoI feature and finally outputs object feature. We find that
     whole image size.                                                 multi-head attention module [47] provides another possible
   • “Grid” means proposal boxes are initialized as regular            implementation for the instance interaction. We carry out
     grid in image, which is exactly the initial boxes in G-           the comparison experiments in Table 9, and its performance
     CNN [34].                                                         falls behind 6.6 AP. Compared with linear multi-head at-
                                                                       tention, our dynamic head is much more flexible, whose pa-
   • “Random” denotes the center, height and width of pro-             rameters are conditioned on its specific proposal feature and
     posal boxes are randomly initialized with Gaussian                more non-linear capacity can be easily introduced.
 Figure 5 – Visualization of predicted boxes of each stage in iterative architecture, including learned proposal boxes. Learned proposal
 boxes are drawn in white color, except those are shown in later stages. Predicted boxes of classification score above 0.3 are shown.
 The boxes from the same proposal are drawn in the same color. The learned proposal boxes are randomly distributed on the image and
 together cover the whole image. The iterative heads gradually refine box position and remove duplicate ones.

Proposal feature vs. Object query. Object query proposed               CNN presents robust performance in both rare and crowd
in DETR [3] shares a similar design as proposal feature.               scenarios. For object in rare scenario, its duplicate boxes
Here we make a comparison of object query [3] proposed                 are removed within a few of stages. Crowd scenarios con-
in DETR and our proposal feature. As discussed in [3],                 sume more stages to refine but finally each object is detected
object query is learned positional encoding, guiding the de-           precisely and uniquely.
coder interacting with the summation of image feature map
and spatial positional encoding. Using only image feature              5. Conclusion
map will lead to a significant drop. However, our proposal
feature can be seen as a feature filter, which is irrelevant to            We present Sparse R-CNN, a purely sparse method for
position. The comparisons are shown in Table 10, DETR                  object detection in images. A fixed sparse set of learned
drops 7.8 AP if the spatial positional encoding is removed.            object proposals are provided to perform classification and
On the contrary, positional encoding gives no gain in Sparse           location by dynamic heads. Final predictions are directly
                                                                       output without non-maximum suppression post-procedure.
R-CNN.
                                                                       Sparse R-CNN demonstrates its accuracy, run-time and
4.3. The Proposal Boxes Behavior                                       training convergence performance on par with the well-
                                                                       established detector. We hope our work could inspire re-
   Figure 5 shows the learned proposal boxes of a con-
                                                                       thinking the convention of dense prior and exploring next
verged model. These boxes are randomly distributed on the
                                                                       generation of object detector.
image to cover the whole image area. This guarantees the
recall performance on the condition of sparse candidates.
Further, each stage of cascading heads gradually refines box           Acknowledgements This work was supported by the Gen-
position and remove duplicate ones. This results in high               eral Research Fund of HK No.27208720.
precision performance. Figure 5 also shows that Sparse R-
                       Appendix                                   Method                 AP     AP50 AP75 APs APm APl
                                                                  Supervised [9] 45.0            63.4 48.2 26.9 47.2 59.5
A. Crowded Scene                                                  DetCo [54]        46.5(+1.5) 65.7 50.8 30.8 49.5 59.7
    One concern about Sparse R-CNN is its performance             SCRL [39]         46.7(+1.7) 65.7 51.1 -     -    -
on crowded scene. We conduct experiments on CrowdHu-              Table 12 – Comparisons of supervised and self-supervised pre-
man [41], a highly crowded human detection benchmark.             training weights on Sparse R-CNN. All models use ResNet-50
Following [59, 27, 62], we use evaluation metrics as AP,          as backbone.
mMR and Recall under IoU 50.
    On CrowdHuman, Sparse R-CNN is trained for 50
epochs, with learning rate divided by 10 at epoch 40. The         C. Backbone Architecture
proposal number is 500. The shortest side of input image is          The default backbone of Sparse R-CNN is ResNet-
at least 480 and at most 800, while longest side is at most       50, CNN-based architecture. Recently, Transformer-based
1500. Other details are the same as COCO dataset.                 architecture achieves great success in computer vision
                                                                  community [47, 52, 10]. We list Sparse R-CNN per-
  Method                      NMS     AP     mMR Recall           formance with two recently-proposed Transformer back-
  Faster R-CNN [37]            X      85.0    50.4    90.2        bone, PVT [50] and Swin Transformer [32], where PVT
  RetinaNet [29]               X      81.7    57.6    88.6        applies a progressive shrinking pyramid structure, Swin
  FCOS [45]                    X      86.1    55.2    94.3        Transformer constructs hierarchical representation com-
  DETR [3]                     ◦      66.1    80.6     -          puted with shifted window.
  Deformable DETR [63]         ◦      86.7    54.0    92.5           From Table 13, both Transformer-based backbones
                                                                  achieve better performance than CNN on Sparse R-CNN.
  Sparse R-CNN                  ◦     89.2    48.3    95.9
 Table 11 – Performance of different detectors on CrowdHuman       Method           AP        AP50 AP75 APs APm APl
 dataset. All models are trained on train split (∼15k images)
 and evaluated on val split (∼4k images).
                                                                   CNN [19] 45.0              63.4   48.2 26.9 47.2 59.5
                                                                   PVT [50] 45.7(+0.7)   -            -       -      -       -
   From Table 11, we are surprised to see that Sparse              Swin [32] 47.9(+2.9) 67.3         52.3     -      -       -
R-CNN achieves better performance than well-established           Table 13 – Comparisons of CNN and Transformer backbone on
mainstream detectors, such as Faster R-CNN, RetinaNet             Sparse R-CNN.
and FCOS. Meanwhile, Sparse R-CNN improves 23.1 and
2.5 AP than DETR and Deformable DETR, two recent end-
                                                                  References
to-end detectors.
   The experiments on CrowdHuman show that Sparse R-               [1] Navaneeth Bodla, Bharat Singh, Rama Chellappa, and
CNN is also applicable on crowded scene. We hope Sparse                Larry S. Davis. Soft-NMS – improving object detection with
R-CNN could serve as a solid baseline used in various de-              one line of code. In ICCV, 2017. 2, 3
tection scenarios.                                                 [2] Zhaowei Cai and Nuno Vasconcelos. Cascade R-CNN: Delv-
                                                                       ing into high quality object detection. In CVPR, 2018. 2, 3,
                                                                       4, 6, 7
B. Self-supervised Pre-training
                                                                   [3] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas
    Object detection has adopted ImageNet-supervised pre-              Usunier, Alexander Kirillov, and Sergey Zagoruyko. End-to-
training weight [9, 14] for past several years. Recently, self-        End object detection with transformers. In ECCV, 2020. 2,
supervised methods show promising benefits than the su-                3, 4, 5, 6, 7, 8, 9
pervised counterparts on well-established detectors [5, 17,        [4] Mathilde Caron, Ishan Misra, Julien Mairal, Priya Goyal, Pi-
                                                                       otr Bojanowski, and Armand Joulin. Unsupervised learning
16, 4]. Accordingly, we list experiment results of self-
                                                                       of visual features by contrasting cluster assignments. arXiv
supervised methods on Sparse R-CNN, such as DetCo [54],                preprint arXiv:2006.09882, 2020. 9
SCRL [39], where DetCo introduces contrastive learning
                                                                   [5] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Ge-
between global image and local patches, SCRL learns spa-               offrey Hinton. A simple framework for contrastive learning
tially consistent representations of randomly cropped local            of visual representations. arXiv preprint arXiv:2002.05709,
regions by geometric translations and zooming operations.              2020. 9
    In Table 12, Sparse R-CNN obtains consistent improve-          [6] Jifeng Dai, Yi Li, Kaiming He, and Jian Sun. R-FCN: Object
ment by replacing ImageNet-supervised pre-training weight              detection via region-based fully convolutional networks. In
to self-supervised ones.                                               NeurIPS, 2016. 3, 4
 [7] Jifeng Dai, Haozhi Qi, Yuwen Xiong, Yi Li, Guodong               [24] Tao Kong, Fuchun Sun, Huaping Liu, Yuning Jiang, Lei Li,
     Zhang, Han Hu, and Yichen Wei. Deformable convolutional               and Jianbo Shi. Foveabox: Beyound anchor-based object de-
     networks. In ICCV, 2017. 3, 6                                         tection. IEEE Transactions on Image Processing, 29:7389–
 [8] Navneet Dalal and Bill Triggs. Histograms of oriented gra-            7398, 2020. 2, 3
     dients for human detection. In CVPR, 2005. 2                     [25] Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton.
 [9] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li,                ImageNet classification with deep convolutional neural net-
     and Li Fei-Fei. ImageNet: A large-scale hierarchical image            works. In NeurIPS, 2012. 2
     database. In CVPR, 2009. 5, 9                                    [26] Hei Law and Jia Deng. CornerNet: Detecting objects as
[10] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,                paired keypoints. In ECCV, 2018. 3, 5
     Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,              [27] Matthieu Lin, Chuming Li, Xingyuan Bu, Ming Sun, Chen
     Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-              Lin, Junjie Yan, Wanli Ouyang, and Zhidong Deng. Detr
     vain Gelly, et al. An image is worth 16x16 words: Trans-              for pedestrian detection. arXiv preprint arXiv:2012.06785,
     formers for image recognition at scale. arXiv preprint                2020. 9
     arXiv:2010.11929, 2020. 9                                        [28] Tsung-Yi Lin, Piotr Dollar, Ross Girshick, Kaiming He,
[11] Mark Everingham, Luc. Van Gool, Christopher K. I.                     Bharath Hariharan, and Serge Belongie. Feature pyramid
     Williams, John Winn, and Andrew Zisserman. The pascal vi-             networks for object detection. In CVPR, 2017. 3
     sual object classes (VOC) challenge. IJCV, 88(2):303–338,        [29] Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, and
     2010. 2                                                               Piotr Dollar. Focal loss for dense object detection. In ICCV,
[12] Pedro Felzenszwalb, Ross Girshick, David McAllester, and              2017. 1, 2, 4, 9
     Deva Ramanan. Object detection with discriminatively             [30] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,
     trained part based models. T-PAMI, 32(9):1627–1645, 2010.             Pietro Perona, Deva Ramanan, Piotr Dollár, and C. Lawrence
     2                                                                     Zitnick. Microsoft COCO: Common objects in context. In
[13] Ross Girshick. Fast R-CNN. In ICCV, 2015. 2, 3                        ECCV, 2014. 1, 2, 5
[14] Ross Girshick, Jeff Donahue, Trevor Darrell, and Jitendra        [31] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian
     Malik. Rich feature hierarchies for accurate object detection         Szegedy, Scott Reed, Cheng-Yang Fu, and Alexander C.
     and semantic segmentation. In CVPR, 2014. 2, 3, 4, 9                  Berg. SSD: Single shot multibox detector. In ECCV, 2016.
[15] Xavier Glorot and Yoshua Bengio. Understanding the diffi-             2, 4
     culty of training deep feedforward neural networks. In Pro-      [32] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei,
     ceedings of the thirteenth international conference on artifi-        Zheng Zhang, Stephen Lin, and Baining Guo. Swin trans-
     cial intelligence and statistics, pages 249–256, 2010. 5              former: Hierarchical vision transformer using shifted win-
[16] Jean-Bastien Grill, Florian Strub, Florent Altché, Corentin          dows. arXiv preprint arXiv:2103.14030, 2021. 9
     Tallec, Pierre H Richemond, Elena Buchatskaya, Carl Do-          [33] Ilya Loshchilov and Frank Hutter. Decoupled weight de-
     ersch, Bernardo Avila Pires, Zhaohan Daniel Guo, Moham-               cay regularization. In International Conference on Learning
     mad Gheshlaghi Azar, et al. Bootstrap your own latent: A              Representations, 2018. 5
     new approach to self-supervised learning. arXiv preprint         [34] Mahyar Najibi, Mohammad Rastegari, and Larry S Davis.
     arXiv:2006.07733, 2020. 9                                             G-cnn: an iterative grid based object detector. In Proceed-
[17] Kaiming He, Haoqi Fan, Yuxin Wu, Saining Xie, and Ross                ings of the IEEE conference on computer vision and pattern
     Girshick. Momentum contrast for unsupervised visual rep-              recognition, pages 2369–2377, 2016. 3, 7
     resentation learning. In Proceedings of the IEEE/CVF Con-        [35] Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali
     ference on Computer Vision and Pattern Recognition, pages             Farhadi. You only look once: Unified, real-time object de-
     9729–9738, 2020. 9                                                    tection. In CVPR, 2016. 4
[18] Kaiming He, Georgia Gkioxari, Piotr Dollar, and Ross Gir-        [36] Joseph Redmon and Ali Farhadi. YOLO9000: Better, faster,
     shick. Mask R-CNN. In ICCV, 2017. 2                                   stronger. In CVPR, 2017. 2
[19] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun.           [37] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.
     Deep residual learning for image recognition. In CVPR,                Faster R-CNN: Towards real-time object detection with re-
     2016. 2, 3, 5, 9                                                      gion proposal networks. In NeurIPS, 2015. 1, 2, 3, 4, 7,
[20] Han Hu, Jiayuan Gu, Zheng Zhang, Jifeng Dai, and Yichen               9
     Wei. Relation networks for object detection. In CVPR, 2018.      [38] Hamid Rezatofighi, Nathan Tsoi, JunYoung Gwak, Amir
     4                                                                     Sadeghian, Ian Reid, and Silvio Savarese. Generalized in-
[21] Lichao Huang, Yi Yang, Yafeng Deng, and Yinan Yu. Dense-              tersection over union: A metric and a loss for bounding box
     Box: Unifying landmark localization with end to end object            regression. In CVPR, 2019. 4
     detection. arXiv preprint arXiv:1509.04874, 2015. 3              [39] Byungseok Roh, Wuhyun Shin, Ildoo Kim, and Sungwoong
[22] Sergey Ioffe and Christian Szegedy. Batch normalization:              Kim. Spatially consistent representation learning. arXiv
     Accelerating deep network training by reducing internal co-           preprint arXiv:2103.06122, 2021. 9
     variate shift. In ICML, 2015. 2                                  [40] Pierre Sermanet, David Eigen, Xiang Zhang, Michael Math-
[23] Xu Jia, Bert De Brabandere, Tinne Tuytelaars, and Luc V               ieu, Robert Fergus, and Yann Lecun. OverFeat: Integrated
     Gool. Dynamic filter networks. In NIPS, pages 667–675,                recognition, localization and detection using convolutional
     2016. 2, 4                                                            networks. In ICLR, 2014. 2
[41] Shuai Shao, Zijian Zhao, Boxun Li, Tete Xiao, Gang Yu,              computer vision and pattern recognition, pages 1492–1500,
     Xiangyu Zhang, and Jian Sun. Crowdhuman: A bench-                   2017. 6
     mark for detecting human in a crowd. arXiv preprint            [56] Bo Yang, Jianan Wang, Ronald Clark, Qingyong Hu, Sen
     arXiv:1805.00123, 2018. 9                                           Wang, Andrew Markham, and Niki Trigoni. Learning ob-
[42] Russell Stewart, Mykhaylo Andriluka, and Andrew Y Ng.               ject bounding boxes for 3d instance segmentation on point
     End-to-end people detection in crowded scenes. In Proceed-          clouds. In Advances in Neural Information Processing Sys-
     ings of the IEEE conference on computer vision and pattern          tems, pages 6740–6749, 2019. 4
     recognition, pages 2325–2333, 2016. 4                          [57] Ze Yang, Shaohui Liu, Han Hu, Liwei Wang, and Stephen
[43] Mingxing Tan, Ruoming Pang, and Quoc V. Le. EfficientDet:           Lin. RepPoints: Point set representation for object detection.
     Scalable and efficient object detection. In CVPR, 2020. 5           In ICCV, 2019. 5
[44] Zhi Tian, Chunhua Shen, and Hao Chen. Conditional              [58] Hongkai Zhang, Hong Chang, Bingpeng Ma, Naiyan Wang,
     convolutions for instance segmentation. arXiv preprint              and Xilin Chen. Dynamic R-CNN: Towards high quality ob-
     arXiv:2003.05664, 2020. 2, 4                                        ject detection via dynamic training. In ECCV, 2020. 2
[45] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. FCOS:           [59] Shanshan Zhang, Rodrigo Benenson, and Bernt Schiele.
     Fully convolutional one-stage object detection. In ICCV,            Citypersons: A diverse dataset for pedestrian detection. In
     2019. 2, 3, 4, 5, 9                                                 Proceedings of the IEEE Conference on Computer Vision
[46] Jasper RR Uijlings, Koen EA Van De Sande, Theo Gev-                 and Pattern Recognition, pages 3213–3221, 2017. 9
     ers, and Arnold WM Smeulders. Selective search for object      [60] Shifeng Zhang, Cheng Chi, Yongqiang Yao, Zhen Lei, and
     recognition. IJCV, 104(2):154–171, 2013. 3                          Stan Z. Li. Bridging the gap between anchor-based and
[47] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-             anchor-free detection via adaptive training sample selection.
     reit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and Illia          In CVPR, 2020. 2, 4, 5
     Polosukhin. Attention is all you need. In Advances in neural   [61] Xingyi Zhou, Dequan Wang, and Philipp Krähenbühl. Ob-
     information processing systems, pages 5998–6008, 2017. 2,           jects as points. arXiv preprint arXiv:1904.07850, 2019. 2, 3,
     4, 7, 9                                                             5
[48] Paul Viola and Michael Jones. Rapid object detection using     [62] Benjin Zhu*, Feng Wang*, Jianfeng Wang, Siwei Yang,
     a boosted cascade of simple features. In Proceedings of the         Jianhu Chen, and Zeming Li. cvpods: All-in-one toolbox
     2001 IEEE computer society conference on computer vision            for computer vision research, 2020. 9
     and pattern recognition. CVPR 2001, volume 1, pages I–I.       [63] Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang
     IEEE, 2001. 2, 7                                                    Wang, and Jifeng Dai. Deformable detr: Deformable trans-
[49] Chien-Yao Wang, Alexey Bochkovskiy, and Hong-                       formers for end-to-end object detection. arXiv preprint
     Yuan Mark Liao. Scaled-yolov4: Scaling cross stage partial          arXiv:2010.04159, 2020. 2, 3, 5, 6, 9
     network. arXiv preprint arXiv:2011.08036, 2020. 5
[50] Wenhai Wang, Enze Xie, Xiang Li, Deng-Ping Fan, Kaitao
     Song, Ding Liang, Tong Lu, Ping Luo, and Ling Shao.
     Pyramid vision transformer: A versatile backbone for
     dense prediction without convolutions. arXiv preprint
     arXiv:2102.12122, 2021. 9
[51] Xinlong Wang, Rufeng Zhang, Tao Kong, Lei Li, and Chun-
     hua Shen. Solov2: Dynamic and fast instance segmentation.
     In NIPS, 2020. 2, 3
[52] Bichen Wu, Chenfeng Xu, Xiaoliang Dai, Alvin Wan,
     Peizhao Zhang, Zhicheng Yan, Masayoshi Tomizuka, Joseph
     Gonzalez, Kurt Keutzer, and Peter Vajda. Visual transform-
     ers: Token-based image representation and processing for
     computer vision. arXiv preprint arXiv:2006.03677, 2020.
     9
[53] Yuxin Wu, Alexander Kirillov, Francisco Massa, Wan-Yen
     Lo, and Ross Girshick. Detectron2. https://github.
     com/facebookresearch/detectron2, 2019. 2, 5,
     6, 7
[54] Enze Xie, Jian Ding, Wenhai Wang, Xiaohang Zhan, Hang
     Xu, Zhenguo Li, and Ping Luo. Detco: Unsupervised
     contrastive learning for object detection. arXiv preprint
     arXiv:2102.04803, 2021. 9
[55] Saining Xie, Ross Girshick, Piotr Dollár, Zhuowen Tu, and
     Kaiming He. Aggregated residual transformations for deep
     neural networks. In Proceedings of the IEEE conference on
