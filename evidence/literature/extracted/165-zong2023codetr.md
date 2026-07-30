---
source_id: 165
bibtex_key: zong2023codetr
title: DETRs with Collaborative Hybrid Assignments Training
year: 2023
domain_theme: Fondasi RGB
verified_pdf: 165_Co-DETR.pdf
char_count: 96605
---

DETRs with Collaborative Hybrid Assignments Training

                                                                                Zhuofan Zong Guanglu Song                       Yu Liu*
                                                                                         SenseTime Research
                                                                                 {zongzhuofan,liuyuisanai}@gmail.com
                                                                                        songguanglu@sensetime.com
arXiv:2211.12860v6 [cs.CV] 10 Aug 2023

                                                                     Abstract                                                                          Co-DETR
                                                                                                                       54                              DINO-Deformable-DETR
                                                                                                                                                       H-Deformable-DETR
                                             In this paper, we provide the observation that too few                                                    Deformable-DETR
                                                                                                                                                       DAB-DETR
                                         queries assigned as positive samples in DETR with one-                        52                              DN-DETR
                                                                                                                                                       Faster-RCNN
                                         to-one set matching leads to sparse supervision on the en-                                                    HTC
                                         coder’s output which considerably hurt the discriminative                     50
                                         feature learning of the encoder and vice visa for attention

                                                                                                                  AP
                                         learning in the decoder. To alleviate this, we present a novel                48
                                         collaborative hybrid assignments training scheme, namely
                                                                                                                       46
                                         Co-DETR, to learn more efficient and effective DETR-based
                                         detectors from versatile label assignment manners. This
                                                                                                                       44
                                         new training scheme can easily enhance the encoder’s
                                         learning ability in end-to-end detectors by training the mul-
                                                                                                                       42
                                         tiple parallel auxiliary heads supervised by one-to-many la-                       0     20      40     60      80       100     120
                                         bel assignments such as ATSS and Faster RCNN. In addi-                                                Epoch
                                         tion, we conduct extra customized positive queries by ex-            Figure 1. Performance of models with ResNet-50 on COCO val.
                                         tracting the positive coordinates from these auxiliary heads         Co-DETR outperforms other counterparts by a large margin.
                                         to improve the training efficiency of positive samples in the
                                         decoder. In inference, these auxiliary heads are discarded
                                                                                                              a series of variants [31, 37, 44] such as ATSS [41], Reti-
                                         and thus our method introduces no additional parameters
                                                                                                              naNet [21], FCOS [32], and PAA [17] lead to the significant
                                         and computational cost to the original detector while re-
                                                                                                              breakthrough of object detection task. One-to-many label
                                         quiring no hand-crafted non-maximum suppression (NMS).
                                                                                                              assignment is the core scheme of them, where each ground-
                                         We conduct extensive experiments to evaluate the effective-
                                                                                                              truth box is assigned to multiple coordinates in the detec-
                                         ness of the proposed approach on DETR variants, including
                                                                                                              tor’s output as the supervised target cooperated with propos-
                                         DAB-DETR, Deformable-DETR, and DINO-Deformable-
                                                                                                              als [11, 27], anchors [21] or window centers [32]. Despite
                                         DETR. The state-of-the-art DINO-Deformable-DETR with
                                                                                                              their promising performance, these detectors heavily rely
                                         Swin-L can be improved from 58.5% to 59.5% AP on COCO
                                                                                                              on many hand-designed components like a non-maximum
                                         val. Surprisingly, incorporated with ViT-L backbone, we
                                                                                                              suppression procedure or anchor generation [1]. To con-
                                         achieve 66.0% AP on COCO test-dev and 67.9% AP on
                                                                                                              duct a more flexible end-to-end detector, DEtection TRans-
                                         LVIS val, outperforming previous methods by clear mar-
                                                                                                              former (DETR) [1] is proposed to view the object detection
                                         gins with much fewer model sizes. Codes are available at
                                                                                                              as a set prediction problem and introduce the one-to-one set
                                         https://github.com/Sense-X/Co-DETR.
                                                                                                              matching scheme based on a transformer encoder-decoder
                                                                                                              architecture. In this manner, each ground-truth box will
                                                                                                              only be assigned to one specific query, and multiple hand-
                                         1. Introduction                                                      designed components that encode prior knowledge are no
                                             Object detection is a fundamental task in computer vi-           longer needed. This approach introduces a flexible detec-
                                         sion, which requires us to localize the object and classify          tion pipeline and encourages many DETR variants to fur-
                                         its category. The seminal R-CNN families [11, 14, 27] and            ther improve it. However, the performance of the vanilla
                                                                                                              end-to-end object detector is still inferior to the traditional
                                           * Corresponding author.                                            detectors with one-to-many label assignments.

                                                                                                          1
      1.0                                                1.0                                                       Input Image       ATSS        Co-Deformable-DETR   Deformable-DETR
                              ATSS                                                 Deformable-DETR
                              Deformable-DETR                                      Group-DETR
      0.8                     Group-DETR                 0.8                       Co-Deformable-DETR
                              Co-Deformable-DETR
      0.6                                                0.6

                                                   IoF
IoF

      0.4                                                0.4
      0.2                                                0.2

            0.2   0.4          0.6     0.8     1.0         0.0   0.2   0.4         0.6      0.8     1.0
                        IoB                                                  IoB

Figure 2. IoF-IoB curves for the feature discriminability score in
                                                                                                              Figure 3. Visualizations of discriminability scores in the encoder.
the encoder and attention discriminability score in the decoder.

    In this paper, we try to make DETR-based detectors                                                        visions on the encoder’s output which forces it to be dis-
superior to conventional detectors while maintaining their                                                    criminative enough to support the training convergence of
end-to-end merit. To address this challenge, we focus on                                                      these heads. To further improve the training efficiency of
the intuitive drawback of one-to-one set matching that it ex-                                                 the decoder, we elaborately encode the coordinates of posi-
plores less positive queries. This will lead to severe ineffi-                                                tive samples in these auxiliary heads, including the positive
cient training issues. We detailedly analyze this from two                                                    anchors and positive proposals. They are sent to the origi-
aspects, the latent representation generated by the encoder                                                   nal decoder as multiple groups of positive queries to predict
and the attention learning in the decoder. We first compare                                                   the pre-assigned categories and bounding boxes. Positive
the discriminability score of the latent features between the                                                 coordinates in each auxiliary head serve as an independent
Deformable-DETR [43] and the one-to-many label assign-                                                        group that is isolated from the other groups. Versatile one-
ment method where we simply replace the decoder with                                                          to-many label assignments can introduce lavish (positive
the ATSS head. The feature l2 -norm in each spatial co-                                                       query, ground-truth) pairs to improve the decoder’s train-
ordinate is utilized to represent the discriminability score.                                                 ing efficiency. Note that, only the original decoder is used
Given the encoder’s output F ∈ RC×H×W , we can obtain                                                         during inference, thus the proposed training scheme only
the discriminability score map S ∈ R1×H×W . The object                                                        introduces extra overheads during training.
can be better detected when the scores in the correspond-                                                         We conduct extensive experiments to evaluate the effi-
ing area are higher. As shown in Figure 2, we demonstrate                                                     ciency and effectiveness of the proposed method. Illus-
the IoF-IoB curve (IoF: intersection over foreground, IoB:                                                    trated in Figure 3, Co-DETR greatly alleviates the poorly
intersection over background) by applying different thresh-                                                   encoder’s feature learning in one-to-one set matching. As a
olds on the discriminability scores (details in Section 3.4).                                                 plug-and-play approach, we easily combine it with different
The higher IoF-IoB curve in ATSS indicates that it’s eas-                                                     DETR variants, including DAB-DETR [23], Deformable-
ier to distinguish the foreground and background. We fur-                                                     DETR [43], and DINO-Deformable-DETR [39]. As shown
ther visualize the discriminability score map S in Figure 3.                                                  in Figure 1, Co-DETR achieves faster training convergence
It’s obvious that the features in some salient areas are fully                                                and even higher performance. Specifically, we improve the
activated in the one-to-many label assignment method but                                                      basic Deformable-DETR by 5.8% AP in 12-epoch train-
less explored in one-to-one set matching. For the explo-                                                      ing and 3.2% AP in 36-epoch training. The state-of-the-
ration of decoder training, we also demonstrate the IoF-IoB                                                   art DINO-Deformable-DETR with Swin-L [25] can still
curve of the cross-attention score in the decoder based on                                                    be improved from 58.5% to 59.5% AP on COCO val.
the Deformable-DETR and the Group-DETR [5] which in-                                                          Surprisingly, incorporated with ViT-L [8] backbone, we
troduces more positive queries into the decoder. The il-                                                      achieve 66.0% AP on COCO test-dev and 67.9% AP
lustration in Figure 2 shows that too few positive queries                                                    on LVIS val, establishing the new state-of-the-art detector
also influence attention learning and increasing more posi-                                                   with much fewer model sizes.
tive queries in the decoder can slightly alleviate this.
    This significant observation motivates us to present a                                                    2. Related Works
simple but effective method, a collaborative hybrid assign-
ment training scheme (Co-DETR). The key insight of Co-                                                        One-to-many label assignment. For one-to-many label as-
DETR is to use versatile one-to-many label assignments to                                                     signment in object detection, multiple box candidates can
improve the training efficiency and effectiveness of both the                                                 be assigned to the same ground-truth box as positive sam-
encoder and decoder. More specifically, we integrate the                                                      ples in the training phase. In classic anchor-based detectors,
auxiliary heads with the output of the transformer encoder.                                                   such as Faster-RCNN [27] and RetinaNet [21], the sam-
These heads can be supervised by versatile one-to-many la-                                                    ple selection is guided by the predefined IoU threshold and
bel assignments such as ATSS [41], FCOS [32], and Faster                                                      matching IoU between anchors and annotated boxes. The
RCNN [27]. Different label assignments enrich the super-                                                      anchor-free FCOS [32] leverages the center priors and as-

                                                                                                          2
                                                                              "
                                                      One-to-One Set Matching 𝓐                𝓐𝟏                                            𝓐𝒌
                                                                                                                  Training-only
                                                          Transformer Decoder        Transformer Decoder          ⋯⋯               Transformer Decoder

                                Transformer Encoder
                                                                                                             𝐐𝟏                   𝐐𝒌
                  Backbone

                                                                                                        {𝒑𝒐𝒔}                                     {𝒑𝒐𝒔}
                                                                                                       𝐁𝟏                                       𝐁𝒌

                                                          Multi-scale Adapter             Auxiliary Head 1
                                                                                                                  ⋯⋯
                                                                                                                  Training-only
                                                                                                                                       Auxiliary Head K

 Input Image
                                                          One-to-Many Label Assignments        𝓐𝟏                 ⋯⋯                        𝓐𝒌

  Figure 4. Framework of our Collaborative Hybrid Assignment Training. The auxiliary branches are discarded during evaluation.

signs spatial locations near the center of each bounding box           tive hybrid assignments training scheme and the customized
as positives. Moreover, the adaptive mechanism is incorpo-             positive queries generation. We will detailedly describe
rated into one-to-many label assignments to overcome the               these modules and give insights why they can work well.
limitation of fixed label assignments. ATSS [41] performs
adaptive anchor selection by the statistical dynamic IoU val-
ues of top-k closest anchors. PAA [17] adaptively separates            3.2. Collaborative Hybrid Assignments Training
anchors into positive and negative samples in a probabilis-                To alleviate the sparse supervision on the encoder’s out-
tic manner. In this paper, we propose a collaborative hybrid           put caused by the fewer positive queries in the decoder, we
assignment scheme to improve encoder representations via               incorporate versatile auxiliary heads with different one-to-
auxiliary heads with one-to-many label assignments.                    many label assignment paradigms, e.g., ATSS, and Faster
One-to-one set matching. The pioneering transformer-                   R-CNN. Different label assignments enrich the supervisions
based detector, DETR [1], incorporates the one-to-one set              on the encoder’s output which forces it to be discrimina-
matching scheme into object detection and performs fully               tive enough to support the training convergence of these
end-to-end object detection. The one-to-one set matching               heads. Specifically, given the encoder’s latent feature F,
strategy first calculates the global matching cost via Hun-            we firstly transform it to the feature pyramid {F1 , · · · , FJ }
garian matching and assigns only one positive sample with              via the multi-scale adapter where J indicates feature map
the minimum matching cost for each ground-truth box. DN-               with 22+J downsampling stride. Similar to ViTDet [20],
DETR [18] demonstrates the slow convergence results from               the feature pyramid is constructed by a single feature map
the instability of one-to-one set matching, thus introducing           in the single-scale encoder, while we use bilinear interpo-
denoising training to eliminate this issue. DINO [39] inher-           lation and 3 × 3 convolution for upsampling. For instance,
its the advanced query formulation of DAB-DETR [23] and                with the single-scale feature from the encoder, we succes-
incorporates an improved contrastive denoising technique               sively apply downsampling (3×3 convolution with stride 2)
to achieve state-of-the-art performance. Group-DETR [5]                or upsampling operations to produce a feature pyramid. As
constructs group-wise one-to-many label assignment to ex-              for the multi-scale encoder, we only downsample the coars-
ploit multiple positive object queries, which is similar to the        est feature in the multi-scale encoder features F to build
hybrid matching scheme in H-DETR [16]. In contrast with                the feature pyramid. Defined K collaborative heads with
the above follow-up works, we present a new perspective of             corresponding label assignment manners Ak , for the i-th
collaborative optimization for one-to-one set matching.                collaborative head, {F1 , · · · , FJ } is sent to it to obtain the
                                                                       predictions P̂i . At the i-th head, Ai is used to compute the
3. Method                                                              supervised targets for the positive and negative samples in
3.1. Overview                                                          Pi . Denoted G as the ground-truth set, this procedure can
                                                                       be formulated as:
    Following the standard DETR protocol, the input image
                                                                                      {pos}         {pos}         {neg}
is fed into the backbone and encoder to generate latent fea-                        Pi          , Bi         , Pi         = Ai (P̂i , G),                 (1)
tures. Multiple predefined object queries interact with them
in the decoder via cross-attention afterwards. We introduce            where {pos} and {neg} indicate the pair set of (j, positive
Co-DETR to improve the feature learning in the encoder                 coordinates or negative coordinates in Fj ) determined by
                                                                                                                              {pos}
and the attention learning in the decoder via the collabora-           Ai . j means the feature index in {F1 , · · · , FJ }. Bi     is

                                                                  3
                                                                               Assignment Ai
 Head i                    Loss Li                                                                                        {pos}
                                           {pos}, {neg} Generation                      Pi Generation                   Bi      Generation
                       cls: CE loss,     {pos}: IoU(proposal, gt)>0.5        {pos}: gt labels, offset(proposal, gt)     positive proposals
 Faster-RCNN [27]
                      reg: GIoU loss     {neg}: IoU(proposal, gt)<0.5                  {neg}: gt labels                  (x1 , y1 , x2 , y2 )
                      cls: Focal loss {pos}:IoU(anchor, gt)>(mean+std) {pos}: gt labels, offset(anchor, gt), centerness positive anchors
 ATSS [41]
                  reg: GIoU, BCE loss {neg}: IoU(anchor, gt)<(mean+std)                {neg}: gt labels                  (x1 , y1 , x2 , y2 )
                      cls: Focal loss     {pos}: IoU(anchor, gt)>0.5          {pos}: gt labels, offset(anchor, gt)       positive anchors
 RetinaNet [21]
                     reg: GIoU Loss       {neg}: IoU(anchor, gt)<0.4                   {neg}: gt labels                  (x1 , y1 , x2 , y2 )
                     cls: Focal Loss   {pos}: points inside gt center area {pos}: gt labels, ltrb distance, centerness FCOS point (cx, cy)
 FCOS [32]
                  reg: GIoU, BCE loss {neg}: points outside gt center area             {neg}: gt labels                 w = h = 8 × 22+j

Table 1. Detailed information of auxiliary heads. The auxiliary heads include Faster-RCNN [27], ATSS [41], RetinaNet [21], and
FCOS [32]. If not otherwise specified, we follow the original implementations, e.g., anchor generation.

                                                    {pos}             {neg}
the set of spatial positive coordinates. Pi     and Pi                            in the i-th auxiliary branch can be formulated as:
are the supervised targets in the corresponding coordinates,                                                         {pos}
including the categories and regressed offsets. To be spe-                                          Ldec
                                                                                                     i,l = L(Pi,l , Pi
                                                                                                           e e             ).                     (5)
cific, we describe the detailed information about each vari-
able in Table 1. The loss functions can be defined as:                            P
                                                                                  e i,l refers to the output predictions of the l-th decoder layer
                                                                                  in the i-th auxiliary branch. Finally, the training objective
                  {pos}      {pos}                {neg}      {neg}
  Lenc
   i   = Li (P̂i          , Pi       ) + Li (P̂i          , Pi       ), (2)       for Co-DETR is:
                                                                                                    L                   K
Note that the regression loss is discarded for negative sam-                            Lglobal =
                                                                                                    X
                                                                                                          (Ledec
                                                                                                                        X
                                                                                                                              Ldec       enc
                                                                                                             l   + λ1          i,l + λ2 L    ),   (6)
ples. The training objective of the optimization for K aux-                                         l=1                 i=1
iliary heads is formulated as follows:
                                                                                  where Ledec
                                                                                           l  stands for the loss in the original one-to-one set
                                     K
                                     X                                            matching branch [1], λ1 and λ2 are the coefficient balancing
                          Lenc =           Lenc
                                            i                           (3)
                                                                                  the losses.
                                     i=1
                                                                                  3.4. Why Co-DETR works
3.3. Customized Positive Queries Generation
                                                                                     Co-DETR leads to evident improvement to the DETR-
   In the one-to-one set matching paradigm, each ground-
                                                                                  based detectors. In the following, we try to investigate its
truth box will only be assigned to one specific query as the
                                                                                  effectiveness qualitatively and quantitatively. We conduct
supervised target. Too few positive queries lead to ineffi-
                                                                                  detailed analysis based on Deformable-DETR with ResNet-
cient cross-attention learning in the transformer decoder as
                                                                                  50 [15] backbone using the 36-epoch setting.
shown in Figure 2. To alleviate this, we elaborately generate
sufficient customized positive queries according to the label                     Enrich the encoder’s supervisions. Intuitively, too few
assignment Ai in each auxiliary head. Specifically, given                         positive queries lead to sparse supervisions as only one
                                {pos}                                             query is supervised by regression loss for each ground-truth.
the positive coordinates set Bi         ∈ RMi ×4 in the i-th
                                                                                  The positive samples in one-to-many label assignment man-
auxiliary head, where Mi is the number of positive sam-
                                                                                  ners receive more localization supervisions to help enhance
ples, the extra customized positive queries Qi ∈ RMi ×C
                                                                                  the latent feature learning. To further explore how the sparse
can be generated by:
                                                                                  supervisions impede the model training, we detailedly in-
 Qi = Linear(PE(Bi
                           {pos}
                             )) + Linear(E({F∗ }, {pos})).                        vestigate the latent features produced by the encoder. We
                                                             (4)                  introduce the IoF-IoB curve to quantize the discriminabil-
where PE(·) stands for positional encodings and we select                         ity score of the encoder’s output. Specifically, given the
the corresponding features from E(·) according to the index                       latent feature F of the encoder, inspired by the feature visu-
pair (j, positive coordinates or negative coordinates in Fj ).                    alization in Figure 3, we compute the IoF (intersection over
    As a result, there are K + 1 groups of queries that con-                      foreground) and IoB (intersection over background). Given
tribute to a single one-to-one set matching branch and K                          the encoder’s feature Fj ∈ RC×Hj ×Wj at level j, we first
branches with one-to-many label assignments during train-                         calculate the l2 -norm Fbj ∈ R1×Hj ×Wj and resize it to the
ing. The auxiliary one-to-many label assignment branches                          image size H × W . The discriminability score D(F) is
share the same parameters with L decoders layers in the                           computed by averaging the scores from all levels:
original main branch. All the queries in the auxiliary branch                                                     J
are regarded as positive queries, thus the matching process                                                    1X      Fbj
                                                                                                    D(F) =                     ,                  (7)
is discarded. To be specific, the loss of the l-th decoder layer                                               J j=1 max(Fbj )

                                                                              4
                                                                     process. Furthermore, in order to quantify how well cross-
                     12                                              attention is being optimized, we also calculate the IoF-IoB
                                                                     curve for attention score. Similar to the feature discrim-
                                                                     inability score computation, we set different thresholds for
   IS(Instability)

                                                                     attention score to get multiple IoF-IoB pairs. The compar-
                     11                                              isons between Deformable-DETR, Group-DETR, and Co-
                                                                     Deformable-DETR can be viewed in Figure 2. We find that
                                                                     the IoF-IoB curves of DETRs with more positive queries
                                                                     are generally above Deformable-DETR, which is consistent
                     10       Deformable-DETR                        with our motivation.
                              Co-Deformable-DETR
                          2      4       6       8   10   12         3.5. Comparison with other methods
                                          Epoch                      Differences between our method and other counter-
Figure 5. The instability (IS) [18] of Deformable-DETR and Co-
                                                                     parts. Group-DETR, H-DETR, and SQR [2] perform one-
Deformable-DETR on COCO dataset. These detectors are trained
                                                                     to-many assignments by one-to-one matching with dupli-
for 12 epochs with ResNet-50 backbones.
                                                                     cate groups and repeated ground-truth boxes. Co-DETR ex-
                                                                     plicitly assigns multiple spatial coordinates as positives for
where the resize operation is omitted. We visualize the              each ground truth. Accordingly, these dense supervision
discriminability scores of ATSS, Deformable-DETR, and                signals are directly applied to the latent feature map to en-
our Co-Deformable-DETR in Figure 3. Compared with                    able it more discriminative. By contrast, Group-DETR, H-
Deformable-DETR, both ATSS and Co-Deformable-DETR                    DETR, and SQR lack this mechanism. Although more pos-
own stronger ability to distinguish the areas of key objects,        itive queries are introduced in these counterparts, the one-
while Deformable-DETR is almost disturbed by the back-               to-many assignments implemented by Hungarian Matching
ground. Consequently, we define the indicators for fore-             still suffer from the instability issues of one-to-one match-
ground and background as 1(D(F) > S) ∈ RH×W and                      ing. Our method benefits from the stability of off-the-
1(D(F) < S) ∈ RH×W , respectively. S is a predefined                 shelf one-to-many assignments and inherits their specific
score thresh, 1(x) is 1 if x is true and 0 otherwise. As for         matching manner between positive queries and ground-truth
the mask of foreground Mf g ∈ RH×W , the element Mfh,w    g          boxes. Group-DETR and H-DETR fail to reveal the com-
is 1 if the point (h, w) is inside the foreground and 0 oth-         plementarities between one-to-one matching and traditional
erwise. The area of intersection over foreground (IoF) I f g         one-to-many assignment. To our best knowledge, we are the
can be computed as:                                                  first to give the quantitative and qualitative analysis on the
                                                                     detectors with the traditional one-to-many assignment and
                      w=1 (1(D(Fh,w ) > S) · Mh,w )
            PH PW                                fg
     fg       h=1                                                    one-to-one matching. This helps us better understand their
    I =                PH PW            fg
                                                      . (8)          differences and complementarities so that we can naturally
                         h=1     w=1 Mh,w
                                                                     improve the DETR’s learning ability by leveraging off-the-
Concretely, we compute the area of intersection over back-           shelf one-to-many assignment designs without requiring ad-
ground areas (IoB) in a similar way and plot the curve               ditional specialized one-to-many design experience.
IoF and IoB by varying S in Figure 2. Obviously, ATSS                No negative queries are introduced in the decoder. Du-
and Co-Deformable-DETR obtain higher IoF values than                 plicate object queries inevitably bring large amounts of neg-
both Deformable-DETR and Group-DETR under the same                   ative queries for the decoder and a significant increase in
IoB values, which demonstrates the encoder representations           GPU memory. However, our method only processes the
benefit from the one-to-many label assignment.                       positive coordinates in the decoder, thus consuming less
Improve the cross-attention learning by reducing the in-             memory as shown in Table 7.
stability of Hungarian matching. Hungarian matching is
the core scheme in one-to-one set matching. Cross-attention          4. Experiments
is an important operation to help the positive queries encode        4.1. Setup
abundant object information. It requires sufficient training
to achieve this. We observe that the Hungarian matching              Datasets and Evaluation Metrics. Our experiments are
introduces uncontrollable instability since the ground-truth         conducted on the MS COCO 2017 dataset [22] and LVIS
assigned to a specific positive query in the same image is           v1.0 dataset [12]. The COCO dataset consists of 115K
changing during the training process. Following [18], we             labeled images for training and 5K images for validation.
present the comparison of instability in Figure 5, where             We report the detection results by default on the val sub-
we find our approach contributes to a more stable matching           set. The results of our largest model evaluated on the

                                                                 5
   Method                      K     #epochs       AP                 Method                          K     #epochs      AP
   Conditional DETR-C5 [26]     0       36         39.4               Deformable-DETR++ [43]           0      12         47.1
   Conditional DETR-C5 [26]     1       36      41.5(+2.1)            Deformable-DETR++ [43]           1      12      48.7(+1.6)
   Conditional DETR-C5 [26]     2       36      41.8(+2.4)            Deformable-DETR++ [43]           2      12      49.5(+2.4)
   DAB-DETR-C5 [23]             0       36         41.2               DINO-Deformable-DETR† [39]       0      12         49.4
   DAB-DETR-C5 [23]             1       36      43.1(+1.9)            DINO-Deformable-DETR† [39]       1      12      51.0(+1.6)
   DAB-DETR-C5 [23]             2       36      43.5(+2.3)            DINO-Deformable-DETR† [39]       2      12      51.2(+1.8)
   Deformable-DETR [43]         0       12         37.1               Deformable-DETR++‡ [43]          0      12         55.2
   Deformable-DETR [43]         1       12      42.3(+5.2)            Deformable-DETR++‡ [43]          1      12      56.4(+1.2)
                                                                      Deformable-DETR++‡ [43]          2      12      56.9(+1.7)
   Deformable-DETR [43]         2       12      42.9(+5.8)
                                                                      DINO-Deformable-DETR†‡ [39]      0      36         58.5
   Deformable-DETR [43]         0       36         43.3
                                                                      DINO-Deformable-DETR†‡ [39]      1      36      59.3(+0.8)
   Deformable-DETR [43]         1       36      46.8(+3.5)
                                                                      DINO-Deformable-DETR†‡ [39]      2      36      59.5(+1.0)
   Deformable-DETR [43]         2       36      46.5(+3.2)
                                                                    Table 3. Results of strong baselines on COCO val. Methods with
       Table 2. Results of plain baselines on COCO val.
                                                                    † use 5 feature levels. ‡ refers to Swin-L backbone.

test-dev (20K images) are also reported. LVIS v1.0 is               DETR equipped with our method can achieve 51.2% AP,
a large-scale and long-tail dataset with 1203 categories for        which is +1.8% AP higher than the competitive baseline.
large vocabulary instance segmentation. To verify the scal-
                                                                       We further scale up the backbone capacity from ResNet-
ability of Co-DETR, we further apply it to a large-scale ob-
                                                                    50 to Swin-L [25] based on two state-of-the-art base-
ject detection benchmark, namely Objects365 [30]. There
                                                                    lines. As presented in Table 3, Co-DETR achieves 56.9%
are 1.7M labeled images used for training and 80K images
                                                                    AP and surpasses the Deformable-DETR++ baseline by
for validation in the Objects365 dataset. All results follow
                                                                    a large margin (+1.7% AP). The performance of DINO-
the standard mean Average Precision(AP) under IoU thresh-
                                                                    Deformable-DETR with Swin-L can still be boosted from
olds ranging from 0.5 to 0.95 at different object scales.
                                                                    58.5% to 59.5% AP.
Implementation Details. We incorporate our Co-DETR
into the current DETR-like pipelines and keep the train-            4.3. Comparisons with the state-of-the-art
ing setting consistent with the baselines. We adopt ATSS
                                                                        We apply our method with K = 2 to Deformable-
and Faster-RCNN as the auxiliary heads for K = 2 and
                                                                    DETR++ and DINO. Besides, the quality focal loss [19] and
only keep ATSS for K = 1. More details about our aux-
                                                                    NMS are adopted for our Co-DINO-Deformable-DETR.
iliary heads can be found in the supplementary materials.
                                                                    We report the comparisons on COCO val in Table 4. Com-
We choose the number of learnable object queries to 300
                                                                    pared with other competitive counterparts, our method con-
and set {λ1 , λ2 } to {1.0, 2.0} by default. For Co-DINO-
                                                                    verges much faster. For example, Co-DINO-Deformable-
Deformable-DETR++, we use large-scale jitter with copy-
                                                                    DETR readily achieves 52.1% AP when using only 12
paste [10].
                                                                    epochs with ResNet-50 backbone. Our method with Swin-
                                                                    L can obtain 58.9% AP for 1× scheduler, even surpass-
4.2. Main Results
                                                                    ing other state-of-the-art frameworks on 3× scheduler.
    In this section, we empirically analyze the effectiveness       More importantly, our best model Co-DINO-Deformable-
and generalization ability of Co-DETR on different DETR             DETR++ achieves 54.8% AP with ResNet-50 and 60.7%
variants in Table 2 and Table 3. All results are repro-             AP with Swin-L under 36-epoch training, outperforming all
duced using mmdetection [4]. We first apply the collabo-            existing detectors with the same backbone by clear margins.
rative hybrid assignments training to single-scale DETRs                To further explore the scalability of our method, we ex-
with C5 features. Surprisingly, both Conditional-DETR               tend the backbone capacity to 304 million parameters. This
and DAB-DETR obtain 2.4% and 2.3% AP gains over the                 large-scale backbone ViT-L [7] is pre-trained using a self-
baselines with a long training schedule. For Deformable-            supervised learning method (EVA-02 [8]). We first pre-train
DETR with multi-scale features, the detection performance           Co-DINO-Deformable-DETR with ViT-L on Objects365
is significantly boosted from 37.1% to 42.9% AP. The over-          for 26 epochs, then fine-tune it on the COCO dataset for
all improvements (+3.2% AP) still hold when the training            12 epochs. In the fine-tuning stage, the input resolution
time is increased to 36 epochs. Moreover, we conduct ex-            is randomly selected between 480×2400 and 1536×2400.
periments on the improved Deformable-DETR (denoted as               The detailed settings are available in supplementary materi-
Deformable-DETR++) following [16], where a +2.4% AP                 als. Our results are evaluated with test-time augmentation.
gain is observed. The state-of-the-art DINO-Deformable-             Table 5 presents the state-of-the-art comparisons on the

                                                                6
  Method                                       Backbone            Multi-scale       #query     #epochs      AP     AP50       AP75     APS           APM        APL
  Conditional-DETR [26]                        R50                        ✗           300        108        43.0     64.0      45.7       22.7          46.7     61.5
  Anchor-DETR [35]                             R50                        ✗           300         50        42.1     63.1      44.9       22.3          46.2     60.0
  DAB-DETR [23]                                R50                        ✗           900         50        45.7     66.2      49.0       26.1          49.4     63.1
  AdaMixer [9]                                 R50                        ✓           300         36        47.0     66.0      51.1       30.1          50.2     61.8
  Deformable-DETR [43]                         R50                        ✓           300         50        46.9     65.6      51.0       29.6          50.1     61.6
  DN-Deformable-DETR [18]                      R50                        ✓           300         50        48.6     67.4      52.7       31.0          52.0     63.7
  DINO-Deformable-DETR† [39]                   R50                        ✓           900         12        49.4     66.9      53.8       32.3          52.5     63.9
  DINO-Deformable-DETR† [39]                   R50                        ✓           900         36        51.2     69.0      55.8       35.0          54.3     65.3
  DINO-Deformable-DETR† [39]                   Swin-L (IN-22K)            ✓           900         36        58.5     77.0      64.1       41.5          62.3     74.0
  Group-DINO-Deformable-DETR [5]               Swin-L (IN-22K)            ✓           900         36        58.4      -         -         41.0          62.5     73.9
  H-Deformable-DETR [16]                       R50                        ✓           300         12        48.7     66.4      52.9       31.2          51.5     63.5
  H-Deformable-DETR [16]                       Swin-L (IN-22K)            ✓           900         36        57.9     76.8      63.6       42.4          61.9     73.4
  Co-Deformable-DETR                           R50                        ✓           300         12        49.5     67.6      54.3       32.4          52.7     63.7
  Co-Deformable-DETR                           Swin-L (IN-22K)            ✓           900         36        58.5     77.1      64.5       42.4          62.4     74.0
  Co-DINO-Deformable-DETR†                     R50                        ✓           900         12        52.1     69.4      57.1       35.4          55.4     65.9
  Co-DINO-Deformable-DETR†                     Swin-L (IN-22K)            ✓           900         12        58.9     76.9      64.8       42.6          62.7     75.1
  Co-DINO-Deformable-DETR†                     Swin-L (IN-22K)            ✓           900         24        59.8     77.7      65.5       43.6          63.5     75.5
  Co-DINO-Deformable-DETR†                     Swin-L (IN-22K)            ✓           900         36        60.0     77.7      66.1       44.6          63.9     75.7
  Co-DINO-Deformable-DETR++†                   R50                        ✓           900         12        52.1     69.3      57.3       35.4          55.5     67.2
  Co-DINO-Deformable-DETR++†                   R50                        ✓           900         36        54.8     72.5      60.1       38.3          58.4     69.6
  Co-DINO-Deformable-DETR++†                   Swin-L (IN-22K)            ✓           900         12        59.3     77.3      64.9       43.3          63.3     75.5
  Co-DINO-Deformable-DETR++†                   Swin-L (IN-22K)            ✓           900         24        60.4     78.3      66.4       44.6          64.2     76.5
  Co-DINO-Deformable-DETR++†                   Swin-L (IN-22K)            ✓           900         36        60.7     78.5      66.7       45.1          64.7     76.4
  †: 5 feature levels.
                                         Table 4. Comparison to the state-of-the-art DETR variants on COCO val.

                                                enc.      val    test-dev                                                        enc.            val       minival
 Method                      Backbone                                                  Method                 Backbone
                                              #params   APbox     APbox                                                         #params      APbox             APbox
 HTC++ [3]                SwinV2-G [24]        3.0B       62.5     63.1                H-DETR [16]           Swin-L [25]         218M            47.9            -
 DINO [39]                  Swin-L [25]        218M       63.2     63.3                ViTDet [20]            ViT-L [7]          307M            51.2            -
 BEIT3 [33]                  ViT-g [7]         1.9B        -       63.7
                                                                                       ViTDet [20]            ViT-H [7]          632M            53.4            -
 FD [36]                  SwinV2-G [24]        3.0B        -       64.2
                                                                                       GLIPv2 [40]           Swin-H [25]         637M             -            59.8
 DINO [39]                FocalNet-H [38]      746M       64.2     64.3
                                                                                       DINO [39]          InternImage-G [34]     3.0B            63.2          65.8
 Group DETRv2 [6]            ViT-H [7]         629M        -       64.5
 EVA-02 [8]                  ViT-L [7]         304M       64.1     64.5
                                                                                       EVA-02 [8]             ViT-L [7]          304M            65.2            -
 DINO [39]               InternImage-G [34]    3.0B       65.3     65.5                Co-DETR               Swin-L [25]         218M            56.9          62.3
 Co-DETR                     ViT-L [7]         304M       65.9     66.0                Co-DETR                ViT-L [7]         304M             67.9          71.9

Table 5. Comparison to the state-of-the-art frameworks on COCO.                       Table 6. Comparison to the state-of-the-art frameworks on LVIS.

COCO test-dev benchmark. With much fewer model                                       +3.5% and +2.5% AP, respectively. We further finetune
sizes (304M parameters), Co-DETR sets a new record of                                the Objects365 pretrained Co-DETR on this dataset. With-
66.0% AP on COCO test-dev, outperforming the previ-                                  out elaborate test-time augmentation, our approach achieves
ous best model InternImage-G [34] by +0.5% AP.                                       the best detection performance of 67.9% and 71.9% AP
                                                                                     on LVIS val and minival. Compared to the 3-billion
   We also demonstrate the best results of Co-DETR on
                                                                                     parameter InternImage-G with test-time augmentation, we
the long-tailed LVIS detection dataset. In particular, we
                                                                                     obtain +4.7% and +6.1% AP gains on LVIS val and
use the same Co-DINO-Deformable-DETR++ as the model
                                                                                     minival while reducing the model size to 1/10.
on COCO but choose FedLoss [42] as the classification
loss to remedy the impact of unbalanced data distribution.                           4.4. Ablation Studies
Here, we only apply bounding boxes supervision and re-
port the object detection results. The comparisons are avail-                           Unless stated otherwise, all experiments for ablations are
able in Table 6. Co-DETR with Swin-L yields 56.9% and                                conducted on Deformable-DETR with a ResNet-50 back-
62.3% AP on LVIS val and minival, surpassing ViT-                                    bone. We choose the number of auxiliary heads K to 1 by
Det with MAE-pretrained [13] ViT-H and GLIPv2 [40] by                                default and set the total batch size to 32. More ablations and

                                                                                 7
 Method                K
                                   Auxiliary          Memory   GPU
                                                                       AP                       0.02                                                      K=1
                                       head            (MB)    hours                                                                                      K=2
 Deformable-DETR++     0                -             12808     70     47.1
                                                                                                                                                          K=3
                                                                                                                                                          K=6
 H-Deformable-DETR     0                -             15307    104     48.4
 Deformable-DETR++     1               ATSS           13947     86     48.7

                                                                                     Distance
 Deformable-DETR++     2         ATSS + PAA           14629    124     49.0
                                                                                                0.01
 Deformable-DETR++     2    ATSS + Faster-RCNN        14387    120     49.5
                            ATSS + Faster-RCNN
 Deformable-DETR++     3                              15263    150     49.5
                                    + PAA
                            ATSS + Faster-RCNN
 Deformable-DETR++     6     + PAA + RetinaNet        19385    280     48.9
                                 + FCOS + GFL                                                   0.00
                                                                                                          ATSS Faster-RCNN PAA        GFL     FCOS RetinaNet
    Table 7. Experimental results of K varying from 1 to 6.                                         Figure 6. The distance when varying K from 1 to 6.

     Auxiliary head          #epochs           AP     AP50     AP75                  aux head             pos queries   #epochs          AP        AP50    AP75
     Baseline                     36           43.3    62.3     47.1                                                      12             37.1      55.5    40.0
                                                                                                ✗             ✗
     RetinaNet [21]               36           46.1    64.2     50.1                                                      36             43.3      62.3    47.1
     Faster-RCNN [27]             36           46.3    64.7     50.5                                                      12          41.6(+4.5)   59.8    45.6
                                                                                                ✓             ✗
     Mask-RCNN [14]               36           46.5    65.0     50.6                                                      36          46.2(+2.9)   64.7    50.9
     FCOS [32]                    36           46.5    64.8     50.7                                                      12          40.5(+3.4)   58.8    44.4
                                                                                                ✗             ✓
     PAA [17]                     36           46.5    64.6     50.7                                                      36          45.3(+2.0)   63.5    49.8
     GFL [19]                     36           46.5    65.0     51.0                                                      12          42.3(+5.2)   60.5    46.1
                                                                                                ✓             ✓
     ATSS [41]                    36           46.8    65.1     51.5                                                      36          46.8(+3.5)   65.1    51.5

Table 8. Performance of our approach with various auxiliary one-                   Table 9. “aux head” denotes training with an auxiliary head and
to-many heads on COCO val.                                                         “pos queries” means the customized positive queries generation.

                                                                                                                                 K
analyses can be found in the supplementary materials.                                                              1     X
                                                                                                           Si =            (Si,j + Sj,i ),                      (10)
Criteria for choosing auxiliary heads. We further delve                                                         2(K − 1)
                                                                                                                               j̸=i
into the criteria for choosing auxiliary heads in Table 7 and
8. The results in Table 8 reveal that any auxiliary head                           where KL, D, I, C refer to KL divergence, dataset, the input
with one-to-many label assignments consistently improves                           image, and class activation maps (CAM) [29]. As illustrated
the baseline and ATSS achieves the best performance. We                            in Figure 6, we compute the average distances among aux-
find the accuracy continues to increase as K increases when                        iliary heads for K > 1 and the distance between the DETR
choosing K smaller than 3. It is worth noting that perfor-                         head and the single auxiliary head for K = 1. We find the
mance degradation occurs when K = 6, and we speculate                              distance metric is insignificant for each auxiliary head when
the severe conflicts among auxiliary heads cause this. If the                      K = 1 and this observation is consistent with our results in
feature learning is inconsistent across the auxiliary heads,                       Table 8: the DETR head can be collaboratively improved
the continuous improvement as K becomes larger will be                             with any head when K = 1. When K is increased to 2, the
destroyed. We also analyze the optimization consistency of                         distance metrics increase slightly and our method achieves
multiple heads next and in the supplementary materials. In                         the best performance as shown in Table 7. The distance
summary, we can choose any head as the auxiliary head and                          surges when K is increased from 3 and 6, indicating severe
we regard ATSS and Faster-RCNN as the common practice                              optimization conflicts among these auxiliary heads lead to
to achieve the best performance when K ≤ 2. We do not                              a decrease in performance. However, the baseline with 6
use too many different heads, e.g., 6 different heads to avoid                     ATSS achieves 49.5% AP and can be decreased to 48.9%
optimization conflicts.                                                            AP by replacing ATSS with 6 various heads. Accordingly,
                                                                                   we speculate too many diverse auxiliary heads, e.g., more
Conflicts analysis. The conflicts emerge when the same
                                                                                   than 3 different heads, exacerbate the conflicts. In summary,
spatial coordinate is assigned to different foreground boxes
                                                                                   optimization conflicts are influenced by the number of vari-
or treated as background in different auxiliary heads and
                                                                                   ous auxiliary heads and the relations among these heads.
can confuse the training of the detector. We first define the
distance between head Hi and head Hj , and the average                             Should the added heads be different? Collaborative train-
distance of Hi to measure the optimization conflicts as:                           ing with two ATSS heads (49.2% AP) still improves the
                                                                                   model with one ATSS head (48.7% AP) as ATSS is comple-
                      1 X                                                          mentary to the DETR head in our analysis. Besides, intro-
          Si,j =          KL(C(Hi (I)), C(Hj (I)),                       (9)
                     |D|                                                           ducing a diverse and complementary auxiliary head rather
                           I∈D

                                                                               8
  Method                K     #epochs     GPU hours       AP                                            50%       Positive     Negative

  Deformable-DETR       1        36           288        46.8
  Deformable-DETR       0        50           333        44.5
  Deformable-DETR       0       100           667        46.0                                           25%
  Deformable-DETR       0       150          1000        45.9
    Table 10. Comparison to baselines with longer schedule.
                                                                                                        0%
                                                                                                               ATSS          Faster-RCNN
  Branch               NMS     K=0       K=1          K=2
                                                                       (a) Visualizations of queries.     (b) Normalized distances.
  Deformable-DETR++     ✗       47.1    48.7(+1.6)   49.5(+2.4)
  ATSS                  ✓       46.8    47.4(+0.6)   48.0(+1.2)          Figure 7. Distribution of original and customized queries.
  Faster-RCNN           ✓       45.9         -       46.7(+0.8)

Table 11. Collaborative training consistently improves perfor-        ter region of the instance and provide sufficient supervision
mances of all branches on Deformable-DETR++ with ResNet-50.           signals for the detector.
                                                                      Does distribution difference lead to instability? We com-
than the same one as the original head, e.g., Faster-RCNN,            pute the average distance between original and customized
can bring better gains (49.5% AP). Note that this is not con-         queries in Figure 7b. The average distance between original
tradictory to above conclusion; instead, we can obtain the            negative queries and customized positive queries is signif-
best performance with few different heads (K ≤ 2) as the              icantly larger than the distance between original and cus-
conflicts are insignificant, but we are faced with severe con-        tomized positive queries. As this distribution gap between
flicts when using many different heads (K > 3).                       original and customized queries is marginal, there is no in-
                                                                      stability encountered during training.
The effect of each component. We perform a component-
wise ablation to thoroughly analyze the effect of each com-           5. Conclusions
ponent in Table 9. Incorporating the auxiliary head yields
significant gains since the dense spatial supervision enables            In this paper, we present a novel collaborative hybrid
the encoder features more discriminative. Alternatively, in-          assignments training scheme, namely Co-DETR, to learn
troducing customized positive queries also contributes re-            more efficient and effective DETR-based detectors from
markably to the final results, while improving the training           versatile label assignment manners. This new training
efficiency of the one-to-one set matching. Both techniques            scheme can easily enhance the encoder’s learning ability
can accelerate convergence and improve performance. In                in end-to-end detectors by training the multiple parallel
summary, we observe the overall improvements stem from                auxiliary heads supervised by one-to-many label assign-
more discriminative features for the encoder and more effi-           ments. In addition, we conduct extra customized positive
cient attention learning for the decoder.                             queries by extracting the positive coordinates from these
Comparisons to the longer training schedule. As pre-                  auxiliary heads to improve the training efficiency of posi-
sented in Table 10, we find Deformable-DETR can not ben-              tive samples in decoder. Extensive experiments on COCO
efit from longer training as the performance saturates. On            dataset demonstrate the efficiency and effectiveness of Co-
the contrary, Co-DETR greatly accelerates the convergence             DETR. Surprisingly, incorporated with ViT-L backbone, we
as well as increasing the peak performance.                           achieve 66.0% AP on COCO test-dev and 67.9% AP
                                                                      on LVIS val, establishing the new state-of-the-art detector
Performance of auxiliary branches. Surprisingly, we ob-
                                                                      with much fewer model sizes.
serve Co-DETR also brings consistent gains for auxiliary
heads in Table 11. This implies our training paradigm
                                                                      References
contributes to more discriminative encoder representations,
which improves the performances of both decoder and aux-               [1] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nico-
iliary heads.                                                              las Usunier, Alexander Kirillov, and Sergey Zagoruyko.
                                                                           End-to-end object detection with transformers. ArXiv,
Difference in distribution of original and customized
                                                                           abs/2005.12872, 2020. 1, 3, 4
positive queries. We visualize the positions of original pos-
                                                                       [2] Fangyi Chen, Han Zhang, Kai Hu, Yu-kai Huang, Chenchen
itive queries and customized positive queries in Figure 7a.                Zhu, and Marios Savvides. Enhanced training of query-
We only show one object (green box) per image. Positive                    based object detection via selective query recollection. arXiv
queries assigned by Hungarian Matching in the decoder are                  preprint arXiv:2212.07593, 2022. 5
marked in red. We mark positive queries extracted from                 [3] Kai Chen, Jiangmiao Pang, Jiaqi Wang, Yu Xiong, Xiaox-
Faster-RCNN and ATSS in blue and orange, respectively.                     iao Li, Shuyang Sun, Wansen Feng, Ziwei Liu, Jianping
These customized queries are distributed around the cen-                   Shi, Wanli Ouyang, et al. Hybrid task cascade for instance

                                                                  9
     segmentation. In Proceedings of the IEEE/CVF Conference             [16] Ding Jia, Yuhui Yuan, Haodi He, Xiaopei Wu, Haojun Yu,
     on Computer Vision and Pattern Recognition, pages 4974–                  Weihong Lin, Lei Sun, Chao Zhang, and Han Hu. Detrs with
     4983, 2019. 7                                                            hybrid matching. arXiv preprint arXiv:2207.13080, 2022. 3,
 [4] Kai Chen, Jiaqi Wang, Jiangmiao Pang, Yuhang Cao, Yu                     6, 7, 12
     Xiong, Xiaoxiao Li, Shuyang Sun, Wansen Feng, Ziwei Liu,            [17] Kang Kim and Hee Seok Lee. Probabilistic anchor assign-
     Jiarui Xu, et al. Mmdetection: Open mmlab detection tool-                ment with iou prediction for object detection. In European
     box and benchmark. arXiv preprint arXiv:1906.07155, 2019.                Conference on Computer Vision, pages 355–371. Springer,
     6                                                                        2020. 1, 3, 8, 13
 [5] Qiang Chen, Xiaokang Chen, Gang Zeng, and Jingdong                  [18] Feng Li, Hao Zhang, Shilong Liu, Jian Guo, Lionel M Ni,
     Wang. Group detr: Fast training convergence with de-                     and Lei Zhang. Dn-detr: Accelerate detr training by intro-
     coupled one-to-many label assignment. arXiv preprint                     ducing query denoising. In Proceedings of the IEEE/CVF
     arXiv:2207.13085, 2022. 2, 3, 7                                          Conference on Computer Vision and Pattern Recognition,
 [6] Qiang Chen, Jian Wang, Chuchu Han, Shan Zhang, Zex-                      pages 13619–13627, 2022. 3, 5, 7
     ian Li, Xiaokang Chen, Jiahui Chen, Xiaodi Wang, Shum-              [19] Xiang Li, Wenhai Wang, Lijun Wu, Shuo Chen, Xiaolin Hu,
     ing Han, Gang Zhang, et al. Group detr v2: Strong object                 Jun Li, Jinhui Tang, and Jian Yang. Generalized focal loss:
     detector with encoder-decoder pretraining. arXiv preprint                Learning qualified and distributed bounding boxes for dense
     arXiv:2211.03594, 2022. 7                                                object detection. Advances in Neural Information Processing
 [7] Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov,                   Systems, 33:21002–21012, 2020. 6, 8, 13
     Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner,                 [20] Yanghao Li, Hanzi Mao, Ross Girshick, and Kaiming He.
     Mostafa Dehghani, Matthias Minderer, Georg Heigold, Syl-                 Exploring plain vision transformer backbones for object de-
     vain Gelly, Jakob Uszkoreit, and Neil Houlsby. An image is               tection. arXiv preprint arXiv:2203.16527, 2022. 3, 7
     worth 16x16 words: Transformers for image recognition at            [21] Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, and
     scale. ArXiv, abs/2010.11929, 2021. 6, 7                                 Piotr Dollár. Focal loss for dense object detection. In Pro-
                                                                              ceedings of the IEEE international conference on computer
 [8] Yuxin Fang, Quan Sun, Xinggang Wang, Tiejun Huang, Xin-
                                                                              vision, pages 2980–2988, 2017. 1, 2, 4, 8, 13
     long Wang, and Yue Cao. Eva-02: A visual representation
     for neon genesis. arXiv preprint arXiv:2303.11331, 2023. 2,         [22] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays,
     6, 7                                                                     Pietro Perona, Deva Ramanan, Piotr Dollár, and C Lawrence
                                                                              Zitnick. Microsoft coco: Common objects in context. In
 [9] Ziteng Gao, Limin Wang, Bing Han, and Sheng Guo.
                                                                              European conference on computer vision, pages 740–755.
     Adamixer: A fast-converging query-based object detector.
                                                                              Springer, 2014. 5
     In Proceedings of the IEEE/CVF Conference on Computer
                                                                         [23] Shilong Liu, Feng Li, Hao Zhang, Xiao Yang, Xianbiao Qi,
     Vision and Pattern Recognition, pages 5364–5373, 2022. 7
                                                                              Hang Su, Jun Zhu, and Lei Zhang. Dab-detr: Dynamic
[10] Golnaz Ghiasi, Yin Cui, Aravind Srinivas, Rui Qian, Tsung-
                                                                              anchor boxes are better queries for detr. arXiv preprint
     Yi Lin, Ekin D Cubuk, Quoc V Le, and Barret Zoph. Sim-
                                                                              arXiv:2201.12329, 2022. 2, 3, 6, 7
     ple copy-paste is a strong data augmentation method for in-
                                                                         [24] Ze Liu, Han Hu, Yutong Lin, Zhuliang Yao, Zhenda Xie,
     stance segmentation. In Proceedings of the IEEE/CVF con-
                                                                              Yixuan Wei, Jia Ning, Yue Cao, Zheng Zhang, Li Dong, et al.
     ference on computer vision and pattern recognition, pages
                                                                              Swin transformer v2: Scaling up capacity and resolution. In
     2918–2928, 2021. 6
                                                                              Proceedings of the IEEE/CVF Conference on Computer Vi-
[11] Ross Girshick. Fast r-cnn. In Proceedings of the IEEE inter-             sion and Pattern Recognition, pages 12009–12019, 2022. 7
     national conference on computer vision, pages 1440–1448,            [25] Ze Liu, Yutong Lin, Yue Cao, Han Hu, Yixuan Wei, Zheng
     2015. 1                                                                  Zhang, S. Lin, and B. Guo. Swin transformer: Hierar-
[12] Agrim Gupta, Piotr Dollar, and Ross Girshick. Lvis: A                    chical vision transformer using shifted windows. ArXiv,
     dataset for large vocabulary instance segmentation. In Pro-              abs/2103.14030, 2021. 2, 6, 7
     ceedings of the IEEE/CVF conference on computer vision              [26] Depu Meng, Xiaokang Chen, Zejia Fan, Gang Zeng,
     and pattern recognition, pages 5356–5364, 2019. 5                        Houqiang Li, Yuhui Yuan, Lei Sun, and Jingdong Wang.
[13] Kaiming He, Xinlei Chen, Saining Xie, Yanghao Li, Piotr                  Conditional detr for fast training convergence. In Proceed-
     Dollár, and Ross Girshick. Masked autoencoders are scalable             ings of the IEEE/CVF International Conference on Com-
     vision learners. In Proceedings of the IEEE/CVF conference               puter Vision, pages 3651–3660, 2021. 6, 7
     on computer vision and pattern recognition, pages 16000–            [27] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.
     16009, 2022. 7                                                           Faster r-cnn: Towards real-time object detection with region
[14] Kaiming He, Georgia Gkioxari, Piotr Dollár, and Ross Gir-               proposal networks. Advances in neural information process-
     shick. Mask r-cnn. In Proceedings of the IEEE international              ing systems, 28, 2015. 1, 2, 4, 8, 13
     conference on computer vision, pages 2961–2969, 2017. 1,            [28] Hamid Rezatofighi, Nathan Tsoi, JunYoung Gwak, Amir
     8, 13                                                                    Sadeghian, Ian Reid, and Silvio Savarese. Generalized in-
[15] Kaiming He, X. Zhang, Shaoqing Ren, and Jian Sun. Deep                   tersection over union: A metric and a loss for bounding
     residual learning for image recognition. 2016 IEEE Confer-               box regression. In Proceedings of the IEEE/CVF conference
     ence on Computer Vision and Pattern Recognition (CVPR),                  on computer vision and pattern recognition, pages 658–666,
     pages 770–778, 2016. 4                                                   2019. 13

                                                                    10
[29] Ramprasaath R Selvaraju, Michael Cogswell, Abhishek Das,                    sion and pattern recognition, pages 9759–9768, 2020. 1, 2,
     Ramakrishna Vedantam, Devi Parikh, and Dhruv Batra.                         3, 4, 8, 13
     Grad-cam: Visual explanations from deep networks via                   [42] Xingyi Zhou, Vladlen Koltun, and Philipp Krähenbühl.
     gradient-based localization. In Proceedings of the IEEE in-                 Probabilistic two-stage detection.           arXiv preprint
     ternational conference on computer vision, pages 618–626,                   arXiv:2103.07461, 2021. 7
     2017. 8, 13                                                            [43] Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang
[30] Shuai Shao, Zeming Li, Tianyuan Zhang, Chao Peng, Gang                      Wang, and Jifeng Dai. Deformable detr: Deformable trans-
     Yu, Xiangyu Zhang, Jing Li, and Jian Sun. Objects365: A                     formers for end-to-end object detection. arXiv preprint
     large-scale, high-quality dataset for object detection. In Pro-             arXiv:2010.04159, 2020. 2, 6, 7
     ceedings of the IEEE/CVF international conference on com-              [44] Zhuofan Zong, Qianggang Cao, and Biao Leng. Rcnet: Re-
     puter vision, pages 8430–8439, 2019. 6                                      verse feature pyramid and cross-scale shift network for ob-
[31] Guanglu Song, Yu Liu, and Xiaogang Wang. Revisit-                           ject detection. In Proceedings of the 29th ACM International
     ing the sibling head in object detector. In Proceedings of                  Conference on Multimedia, pages 5637–5645, 2021. 1
     the IEEE/CVF conference on computer vision and pattern
     recognition, pages 11563–11572, 2020. 1
[32] Zhi Tian, Chunhua Shen, Hao Chen, and Tong He. Fcos:
     Fully convolutional one-stage object detection. In Proceed-
     ings of the IEEE/CVF international conference on computer
     vision, pages 9627–9636, 2019. 1, 2, 4, 8, 13
[33] Wenhui Wang, Hangbo Bao, Li Dong, Johan Bjorck, Zhil-
     iang Peng, Qiang Liu, Kriti Aggarwal, Owais Khan Mo-
     hammed, Saksham Singhal, Subhojit Som, et al. Image as a
     foreign language: Beit pretraining for all vision and vision-
     language tasks. arXiv preprint arXiv:2208.10442, 2022. 7
[34] Wenhai Wang, Jifeng Dai, and Zhe Chen. Internimage:
     Exploring large-scale vision foundation models with de-
     formable convolutions. arXiv preprint arXiv:2211.05778,
     2022. 7
[35] Yingming Wang, Xiangyu Zhang, Tong Yang, and Jian Sun.
     Anchor detr: Query design for transformer-based detector.
     In Proceedings of the AAAI conference on artificial intelli-
     gence, volume 36, pages 2567–2575, 2022. 7
[36] Yixuan Wei, Han Hu, Zhenda Xie, Zheng Zhang, Yue Cao,
     Jianmin Bao, Dong Chen, and Baining Guo. Contrastive
     learning rivals masked image modeling in fine-tuning via
     feature distillation. arXiv preprint arXiv:2205.14141, 2022.
     7
[37] Zeyue Xue, Jianming Liang, Guanglu Song, Zhuofan Zong,
     Liang Chen, Yu Liu, and Ping Luo. Large-batch optimization
     for dense visual predictions. In Advances in Neural Informa-
     tion Processing Systems, 2022. 1
[38] Jianwei Yang, Chunyuan Li, and Jianfeng Gao. Focal mod-
     ulation networks. arXiv preprint arXiv:2203.11926, 2022.
     7
[39] Hao Zhang, Feng Li, Shilong Liu, Lei Zhang, Hang Su, Jun
     Zhu, Lionel M Ni, and Heung-Yeung Shum. Dino: Detr
     with improved denoising anchor boxes for end-to-end object
     detection. arXiv preprint arXiv:2203.03605, 2022. 2, 3, 6, 7
[40] Haotian Zhang, Pengchuan Zhang, Xiaowei Hu, Yen-Chun
     Chen, Liunian Li, Xiyang Dai, Lijuan Wang, Lu Yuan, Jenq-
     Neng Hwang, and Jianfeng Gao. Glipv2: Unifying localiza-
     tion and vision-language understanding. Advances in Neural
     Information Processing Systems, 35:36067–36080, 2022. 7
[41] Shifeng Zhang, Cheng Chi, Yongqiang Yao, Zhen Lei, and
     Stan Z Li. Bridging the gap between anchor-based and
     anchor-free detection via adaptive training sample selection.
     In Proceedings of the IEEE/CVF conference on computer vi-

                                                                       11
                          DETRs with Collaborative Hybrid Assignments Training
                                                       Supplementary Material
     #convs         0       1       2        3         4      5                                      CAM KL divergence
                                                                                                                                         0.014
       AP          41.8    42.3    41.9     42.1      42.3   42.0              DETR 0.0000 0.0062 0.0090 0.0129 0.0079 0.0069 0.0083
Table 12. Influence of number of convolutions in auxiliary head.                                                                         0.012
                                                                               ATSS 0.0066 0.0000 0.0097 0.0132 0.0077 0.0045 0.0083

     λ1       λ2      #epochs      AP      APS     APM       APL                                                                         0.010
                                                                          Faster-RCNN 0.0083 0.0087 0.0000 0.0091 0.0055 0.0095 0.0063
     0.25     2.0         36      46.2     28.3    49.7      60.4
                                                                                                                                         0.008
     0.5      2.0         36      46.6     29.0    50.5      61.2               PAA 0.0116 0.0116 0.0083 0.0000 0.0075 0.0125 0.0090
     1.0      2.0         36      46.8     28.1    50.6      61.3                                                                        0.006
     2.0      2.0         36      46.1     27.4    49.7      61.4               GFL 0.0073 0.0068 0.0056 0.0083 0.0000 0.0081 0.0054
     1.0      1.0         36      46.1     27.9    49.7      60.9                                                                        0.004
     1.0      2.0         36      46.8     28.1    50.6      61.3              FCOS 0.0075 0.0048 0.0107 0.0143 0.0092 0.0000 0.0092
     1.0      3.0         36      46.5     29.3    50.4      61.4                                                                        0.002
     1.0      4.0         36      46.3     29.0    50.1      61.0           RetinaNet 0.0078 0.0075 0.0066 0.0100 0.0055 0.0082 0.0000
                                                                                                                                         0.000
  Table 13. Results of hyper-parameter tuning for λ1 and λ2 .

                                                                                                             N
                                                                                             SS

                                                                                                                                    et
                                                                                                             A
                                                                                      TR

                                                                                                                     L

                                                                                                                          OS
                                                                                                      CN

                                                                                                                     GF
                                                                                                          PA

                                                                                                                                 aN
                                                                                            AT
                                                                                    DE

                                                                                                                          FC
                                                                                                    r-R

                                                                                                                               tin
                                                                                                    ste

                                                                                                                               Re
                           CAM KL divergence

                                                                                                  Fa
                                                                          Figure 9. Distances among 7 various heads in our model with
                                                             0.008        K = 6.
            DETR      0.0000      0.0078     0.0085
                                                             0.006        The number of customized positive queries. We compute
                                                                          the average ratio of positive samples in one-to-many label
            ATSS 0.0073           0.0000     0.0062
                                                             0.004        assignment to the ground-truth boxes. For instance, the ra-
                                                                          tio is 18.7 for Faster-RCNN and 8.8 for ATSS on COCO
                                                                          dataset, indicating more than 8× extra positive queries are
                                                             0.002
    Faster-RCNN 0.0079            0.0059     0.0000                       introduced when K = 1.
                                                                          Effectiveness of collaborative one-to-many label assign-
                                                             0.000        ments. To verify the effectiveness of our feature learning
                                                   N
                                   S
                          TR

                                                  CN
                                     S

                                                                          mechanism, we compare our approach with Group-DETR
                                  AT
                      DE

                                             r-R

                                                                          (3 groups) and H-DETR. First, we find Co-DETR performs
                                           ste
                                           Fa

                                                                          better than hybrid matching scheme [16] while training
Figure 8. The relation matrix for the DETR head, ATSS head,               faster and requiring less GPU memory in Table 6. As shown
and Faster-RCNN head. The detector is Co-Deformable-DETR
                                                                          in Table 8, our method (K = 1) achieves 46.2% AP, sur-
(K = 2) with ResNet-50.
                                                                          passing Group-DETR (44.6% AP) by a large margin even
                                                                          without the customized positive queries generation. More
                                                                          importantly, the IoF-IoB curve in Figure 2 demonstrates
A. More ablation studies                                                  Group-DETR fails to enhance the feature representations in
                                                                          the encoder, while our method alleviates the poorly feature
The number of stacked convolutions. Table 12 reveals
                                                                          learning.
our method is robust for the number of stacked convolu-
tions in the auxiliary head (trained for 12 epochs). Con-                 Conflicts analysis. We have defined the distance between
cretely, we simply choose only 1 shared convolution to en-                head Hi and head Hj , and the average distance of Hi to
able lightweight while achieving higher performance.                      measure the optimization conflicts in this study:
Loss weights of collaborative training. Experimental re-                                     1 X
                                                                                    Si,j =           KL(C(Hi (I)), C(Hj (I)),    (11)
sults related to weighting the coefficient λ1 and λ2 are pre-                              |D|
                                                                                                    I∈D
sented in Table 13. We find the proposed method is quite
insensitive to the variations of {λ1 , λ2 }, since the perfor-                                                   K
                                                                                                 1     X
mance slightly fluctuates when varying the loss coefficients.                            Si =            (Si,j + Sj,i ),                 (12)
                                                                                              2(K − 1)
In summary, the coefficients {λ1 , λ2 } are robust and we set                                                 j̸=i

{λ1 , λ2 } to {1.0, 2.0} by default.                                      where KL, D, I, C refer to KL divergence, dataset, the input

                                                                     12
image, and class activation maps (CAM) [29]. In our imple-           16 epochs, where the batch size is set to 64, and the initial
mentation, we choose the validation set COCO val as D                learning rate is set to 5 × 10−5 , which is reduced by a factor
and Grad-CAM as C. We use the output features of DETR                of 0.1 at the 9-th and 15-th epoch.
encoder to compute the CAM maps. More specifically, we
show the detailed distances when K = 2 and K = 6 in Fig-
ure 8 and Figure 9, respetively. The larger distance metric
of Si,j indicates Hi is less consistent to Hj and contributes
to the optimization inconsistency.

B. More implementation details
One-stage auxiliary heads. Based on the conventional
one-stage detectors, we experiment with various first-stage
designs [17, 19, 21, 32, 41] for the auxiliary heads. First,
we use the GIoU [28] loss for the one-stage heads. Then,
the number of stacked convolutions is reduced from 4 to
1. Such modification improves the training efficiency with-
out any accuracy drop. For anchor-free detectors, e.g.,
FCOS [32], we assign the width of 8 × 2j and height of
8 × 2j for the positive coordinates with stride 2j .
Two-stage auxiliary heads. We adopt the RPN and RCNN
as our two-stage auxiliary heads based on the popular
Faster-RCNN [27] and Mask-RCNN [14] detectors. To
make Co-DETR compatible with various detection heads,
we adopt the same multi-scale features (stride 8 to stride
128) as the one-stage paradigm for two-stage auxiliary
heads. Moreover, we adopt the GIoU loss for regression
in the RCNN stage.
System-level comparison on COCO. We first initialize
the ViT-L backbone with EVA-02 weights. Then we per-
form intermediate finetuning on the Objects365 dataset us-
ing Co-DINO-Deformable-DETR for 26 epochs and reduce
the learning rate by a factor of 0.1 at epoch 24. The ini-
tial learning rate is 2.5 × 10−4 and the batch size is 224.
We choose the maximum size of input images as 1280 and
randomly resize the shorter size to 480−1024. Moreover,
we use 1500 object queries and 1000 DN queries for this
model. Finally, we finetune Co-DETR on COCO for 12
epochs with an initial learning rate of 5 × 10−5 and drop
the learning rate at the 8-th epoch by multiplying 0.1. The
shorter size of input images is enlarged to 480−1536 and
the longer size is no more than 2400. We employ EMA and
train this model with a batch size of 64.
System-level comparison on LVIS. In contrast to the
COCO setting, we use Co-DINO-Deformable-DETR++ to
perform intermediate finetuning on the Objects365 dataset,
as we find LSJ augmentation works better on the LVIS
dataset. A batch size of 192, an initial learning rate of
2 × 10−4 , and an input image size of 1280×1280 are used.
We use 900 object queries and 1000 DN queries for this
model. During finetuning on LVIS, we arm it with an addi-
tional auxiliary mask branch and increase the input size to
1536×1536. Besides, we train the model without EMA for

                                                                13
