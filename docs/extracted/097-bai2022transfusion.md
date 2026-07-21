---
source_id: 097
bibtex_key: bai2022transfusion
title: TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers
year: 2022
domain_theme: Deteksi 3D
verified_pdf: 97_TransFusion.pdf
char_count: 107910
---

TransFusion: Robust LiDAR-Camera Fusion for 3D Object Detection with Transformers

 Xuyang Bai1 Zeyu Hu1 Xinge Zhu2 Qingqiu Huang2 Yilun Chen2 Hongbo Fu3 Chiew-Lan Tai1
  1                                                              2                                 3
      Hong Kong University of Science and Technology                 ADS, IAS BU, Huawei               City University of Hong Kong

                         Abstract                                       datasets with sparser point clouds, such as nuScenes [1] and
                                                                        Waymo [43]. LiDAR-only methods are surely insufficient
    LiDAR and camera are two important sensors for 3D ob-               for robust 3D detection due to the sparsity of point clouds.
ject detection in autonomous driving. Despite the increas-              For example, small or distant objects are difficult to detect
ing popularity of sensor fusion in this field, the robustness           in LiDAR modality. In contrast, such objects are still clearly
against inferior image conditions, e.g., bad illumination               visible and distinguishable in high-resolution images. The
and sensor misalignment, is under-explored. Existing fu-                complementary roles of point clouds and images motivate
sion methods are easily affected by such conditions, mainly             researchers to design detectors utilizing the best of the two
due to a hard association of LiDAR points and image pixels,             worlds, i.e., multi-modal detectors.
established by calibration matrices.                                       Existing LiDAR-camera fusion methods roughly fall
    We propose TransFusion, a robust solution to LiDAR-                 into three categories: result-level, proposal-level, and point-
camera fusion with a soft-association mechanism to han-                 level. The result-level methods, including FPointNet [29]
dle inferior image conditions. Specifically, our TransFu-               and RoarNet [39], use off-the-shelf 2D detectors to seed
sion consists of convolutional backbones and a detection                3D proposals, followed by a PointNet [30] for object lo-
head based on a transformer decoder. The first layer of the             calization. The proposal-level fusion methods, including
decoder predicts initial bounding boxes from a LiDAR point              MV3D [5] and AVOD [12], perform fusion at the region
cloud using a sparse set of object queries, and its second              proposal level by applying RoIPool [31] in each modality
decoder layer adaptively fuses the object queries with use-             for shared proposals. These coarse-grained fusion meth-
ful image features, leveraging both spatial and contextual              ods show unsatisfactory results since rectangular regions
relationships. The attention mechanism of the transformer               of interest (RoI) usually contain lots of background noise.
enables our model to adaptively determine where and what                Recently, a majority of approaches have tried to do point-
information should be taken from the image, leading to a                level fusion and achieved promising results. They first find
robust and effective fusion strategy. We additionally design            a hard association between LiDAR points and image pix-
an image-guided query initialization strategy to deal with              els based on calibration matrices, and then augment LiDAR
objects that are difficult to detect in point clouds. TransFu-          features with the segmentation scores [47, 52] or CNN fea-
sion achieves state-of-the-art performance on large-scale               tures [10, 22, 40, 48, 63] of the associated pixels through
datasets. We provide extensive experiments to demonstrate               point-wise concatenation. Similarly, [16, 17, 51, 60] first
its robustness against degenerated image quality and cali-              project a point cloud onto the bird’s eye view (BEV) plane
bration errors. We also extend the proposed method to the               and then fuse the image features with the BEV pixels.
3D tracking task and achieve the 1st place in the leader-                  Despite the impressive improvements, these point-level
board of nuScenes tracking, showing its effectiveness and               fusion methods suffer from two major problems, as shown
generalization capability. [code release]                               in Fig. 1. First, they simply fuse the LiDAR features and
                                                                        image features through element-wise addition or concate-
                                                                        nation, and thus their performance degrades seriously with
1. Introduction                                                         low-quality image features, e.g., images in bad illumina-
   As one of the fundamental tasks in self-driving, 3D ob-              tion conditions. Second, finding the hard association be-
ject detection aims to localize a set of objects in 3D space            tween sparse LiDAR points and dense image pixels not only
and recognize their categories. Thanks to the accurate                  wastes many image features with rich semantic information,
depth information provided by LiDAR, early works such                   but also heavily relies on high-quality calibration between
as VoxelNet [68] and PointPillar [14] achieve reasonably                two sensors, which is usually hard to acquire due to the in-
good results using only point clouds as input. However,                 herent spatial-temporal misalignment [64].
these LiDAR-only methods are generally surpassed by the                    To address the shortcomings of the previous fusion ap-
methods using both LiDAR and camera data on large-scale                 proaches, we introduce an effective and robust multi-modal
                                                                        4. We achieve the state-of-the-art 3D detection per-
                                                                           formance on nuScenes and competitive results on
                                                                           Waymo. We also extend our model to the 3D track-
                                                                           ing task and achieve the 1st place in the leaderboard
                                                                           of the nuScenes tracking challenge.
Figure 1. Left: An example of bad illumination conditions. Right:
Due to the sparsity of point clouds, the hard-association based fu-
sion methods waste many image features and are sensitive to sen-       2. Related Work
sor calibration, since the projected points may fall outside objects
due to a small calibration error.
                                                                       LiDAR-only 3D Detection aims to predict 3D bounding
detection framework in this paper. Our key idea is to repo-            boxes of objects in given point clouds [3, 4, 27, 28, 38, 47,
sition the focus of the fusion process, from hard-association          54, 67, 69, 70]. Due to the unordered, irregular nature of
to soft-association, leading to the robustness against degen-          point clouds, many 3D detectors first project them onto a
erated image quality and sensor misalignment.                          regular grid such as 3D voxels [53, 68], pillars [14] or range
    Specifically, we design a sequential fusion method that            images [8, 44]. After that, standard 2D or 3D convolutions
uses two transformer decoder layers as the detection head.             are used to compute the features in the BEV plane, where
To our best knowledge, we are the first to use transformer             objects are naturally separated, with their physical sizes pre-
for LiDAR-camera 3D detection. Our first decoder layer                 served. Other works [36, 37, 55, 56] directly operate on raw
leverages a sparse set of object queries to produce ini-               point clouds without quantization. The mainstream of 3D
tial bounding boxes from LiDAR features. Unlike input-                 detection head is based on anchor boxes [14, 68] follow-
independent object queries in 2D [2, 45], we make the ob-              ing the 2D counterparts, while [49, 58] adopt a center-based
ject queries input-dependent and category-aware so that the            representation for 3D objects, largely simplifying the 3D
queries are enriched with better position and category infor-          detection pipeline. Despite the popularity of adopting the
mation. Next, the second transformer decoder layer adap-               transformer architecture as a detection head in 2D [2], 3D
tively fuses object queries with useful image features as-             detection models for outdoor scenarios mostly utilize the
sociated by spatial and contextual relationships. We lever-            transformer for feature extraction [21, 24, 35]. However,
age a locality inductive bias by spatially constraining the            the attention operation in each transformer layer requires
cross attention around the initial bounding boxes to help the          a computation complexity of O(N 2 ) for N points, requir-
network better visit the related positions. Our fusion mod-            ing a carefully designed memory reduction operation when
ule not only provides rich semantic information to object              handling LiDAR point clouds with millions of points per
queries, but also is more robust to inferior image conditions          frame. In contrast, our model retains an efficient convolu-
since the association between LiDAR points and image pix-              tion backbone for feature extraction and leverages a trans-
els are established in a soft and adaptive way. Finally, to            former decoder with a small set of object queries as the
handle objects that are difficult to detect in point clouds,           detection head, making the computation cost manageable.
we introduce an image-guided query initialization module               The concurrent works [19, 20, 23] adopt transformer as a
to involve image guidance on the query initialization stage.           detection head but focus on indoor scenarios and extending
Overall, the corporation of these components significantly             these methods to outdoor scenes is non-trivial.
improves the effectiveness and robustness of our LiDAR-                LiDAR-Camera 3D Detection has gained increasing atten-
camera 3D detector. To summarize, our contributions are                tion due to the complementary roles of point clouds and im-
fourfold:                                                              ages. Early works [5, 29, 39] adopt result-level or proposal-
  1. Our studies investigate the inherent difficulties of              level fusion, where the fusion granularity is too coarse to
      LiDAR-camera fusion and reveal a crucial aspect to               release the full potential of two modalities. Since Point-
      robust fusion, namely, the soft-association mechanism.           Painting [47] was proposed, the point-level fusion meth-
  2. We propose a novel transformer-based LiDAR-camera                 ods [10,40,48] have shown great advantages and promising
      fusion model for 3D detection, which performs fine-              results. However, such methods are easily affected by the
      grained fusion in an attentive manner and shows supe-            sensor misalignment due to the hard association between
      rior robustness against degenerated image quality and            points and pixels established by calibration matrices. More-
      sensor misalignment.                                             over, the simple point-wise concatenation ignores the qual-
  3. We introduce several simple yet effective adjustments             ity of real data and contextual relationships between two
      for object queries to boost the quality of initial bound-        modalities, and thus leads to degraded performance when
      ing box predictions for image fusion. An image-                  the image features are defective. In our work, we explore
      guided query initialization module is also designed to           a more robust and effective fusion mechanism to mitigate
      handle objects that are hard to detect in point clouds.          these limitations during LiDAR-camera fusion.
                           LiDAR                                                                                        as ), +                    Initial Prediction

                                                                      Query Initialization

                                                                                                                                  Prediction FFN
                                           3D Backbone
                                                                                                         as ,     Transformer
                                                                                                                 Decoder Layer

                                                         LiDAR BEV                           Object Queries
                                                         Features

                          Camera                                                                                                                       Final Output
                                                               Image Guidance

                                                                                                                                  Prediction FFN
                                           2D Backbone                                                as ), +     Transformer
                                                                                                                 Decoder Layer
                                                                                                                   with SMCA
                                                         Image Features
                                                                                                                LiDAR-Camera Fusion

Figure 2. Overall pipeline of TransFusion. Our model relies on standard 3D and 2D backbones to extract LiDAR BEV feature map and
image feature map. Our detection head consists of two transformer decoder layers sequentially: (1) The first layer produces initial 3D
bounding boxes using a sparse set of object queries, initialized in a input-dependent and category-aware manner. (2) The second layer
attentively associates and fuses the object queries (with initial predictions) from the first stage with the image features, producing rich
texture and color cues for better detection results. A spatially modulated cross attention (SMCA) mechanism is introduced to involve a
locality inductive bias and help the network better attend to the related image regions. We additionally propose an image-guided query
initialization strategy to involve image guidance on LiDAR BEV. This strategy helps produce object queries that are difficult to detect in
the sparse LiDAR point clouds.

3. Methodology                                                                                          3.2. Query Initialization
    In this section, we present the proposed method TransFu-                                            Input-dependent. The query positions in the seminal
sion for LiDAR-camera 3D object detection. As shown in                                                  works [2, 45, 71] are randomly generated or learned as net-
Fig. 2, given a LiDAR BEV feature map and an image fea-                                                 work parameters, regardless of the input data. Such input-
ture map from convolutional backbones, our transformer-                                                 independent query positions will take extra stages (decoder
based detection head first decodes object queries into ini-                                             layers) for their models [2, 71] to learn the moving process
tial bounding box predictions using the LiDAR information,                                              towards the real object centers. Recently, it has been ob-
and then performs LiDAR-camera fusion by attentively fus-                                               served in 2D object detection [57] that with a better ini-
ing object queries with useful image features. Below we                                                 tialization of object queries, the gap between 1-layer struc-
will first provide the preliminary knowledge about a trans-                                             ture and 6-layer structure could be bridged. Inspired by this
former architecture for detection and then present the detail                                           observation, we propose an input-dependent initialization
of TransFusion.                                                                                         strategy based on a center heatmap to achieve competitive
                                                                                                        performance using only one decoder layer.
3.1. Preliminary: Transformer for 2D Detection                                                              Specifically, given a d dimensional LiDAR BEV fea-
                                                                                                        ture map FL ∈ RX×Y ×d , we first predict a class-specific
   Transformer [46] has been widely used for 2D object de-
                                                                                                        heatmap Ŝ ∈ RX×Y ×K , where X × Y describes the size
tection [9, 45, 57, 71] since DETR [2] was proposed. DETR
                                                                                                        of the BEV feature map and K is the number of categories.
uses a CNN backbone to extract image features and a trans-
                                                                                                        Then we regard the heatmap as X × Y × K object candi-
former architecture to convert a small set of learned embed-
                                                                                                        dates and select the top-N candidates for all the categories
dings (called object queries) into a set of predictions. The
                                                                                                        as our initial object queries. To avoid spatially too closed
follow-up works [45,57,71] further equip the object queries
                                                                                                        queries, following [66], we select the local maximum ele-
with positional information 1 . The final predictions of boxes
                                                                                                        ments as our object queries, whose values are greater than
are the relative offsets w.r.t. the query positions to reduce
                                                                                                        or equal to their 8-connected neighbors. Otherwise, a large
optimization difficulty. We refer readers to the original pa-
                                                                                                        number of queries are needed to cover the BEV plane. The
pers [2, 71] for more details. In our work, each object query
                                                                                                        positions and features of the selected candidates are used to
contains a query position providing the localization of the
                                                                                                        initialize the query positions and query features. In this way,
object and a query feature encoding instance information,
                                                                                                        our initial object queries will locate at or close to the poten-
such as the box’s size, orientation, etc.
                                                                                                        tial object centers, eliminating the need of multiple decoder
   1 Slightly different concepts might be introduced, e.g., reference points                            layers [20, 23, 50] to refine the locations.
in Deformable-DETR [71] and proposal boxes in Sparse-RCNN [45].                                         Category-aware. Unlike their 2D projections on the image
                                                                          object query with predicted bounding box.   object query with predicted bounding box.

plane, the objects on the BEV plane are all in absolute scale
and has small scale variance among the same categories. To
leverage such properties for better multi-class detection, we
make the object queries category-aware by equipping each
query with a category embedding. Specifically, using the
category of each selected candidate (e.g. Ŝijk belonging to
the k-th category), we element-wisely sum the query feature
with a category embedding produced by linearly projecting
the one-hot category vector into a Rd vector. The category
embedding brings benefits in two aspects: on the one hand,
it serves as a useful side information when modelling the
object-object relations in the self-attention modules and the       Figure 3. The first row shows the input images and the predic-
object-context relations in the cross-attention modules. On         tions of object queries projected on the images, and the second
the other hand, during prediction, it could deliver valuable        row shows the cross-attention maps. Our fusion strategy is able
prior knowledge of the object, making the network focus             to dynamically choose relevant image pixels and is not limited by
                                                                    the number of LiDAR points. The two images are picked from
on intra-category variance and thus benefiting the property
                                                                    nuScenes and Waymo, respectively.
prediction.

3.3. Transformer Decoder and FFN                                    LiDAR points. When an object only contains a small num-
                                                                    ber of LiDAR points, it can fetch only the same number
The decoder layer follows the design of DETR [23] and               of image features, wasting the rich semantic information of
the detailed architecture is provided in the supplementary          high-resolution images. To mitigate this issue, we do not
Sec. A. The cross attention between object queries and the          fetch the multiview image features based on the hard asso-
feature maps (either from point clouds or images) aggre-            ciation between LiDAR points and image pixels. Instead,
gates relevant context onto the object candidates, while the        we retain all the image features FC ∈ RNv ×H×W ×d as our
self attention between object queries reasons pairwise rela-        memory bank, and use the cross-attention mechanism in the
tions between different object candidates. The query posi-          transformer decoder to perform feature fusion in a sparse-
tions are embedded into d-dimensional positional encoding           to-dense and adaptive manner, as shown in Fig. 2.
with a Multilayer Perceptron (MLP), and element-wisely              SMCA for Image Feature Fusion. Multi-head attention is
summed with the query features. This enables the network            a popular mechanism to perform information exchange and
to reason about both context and position jointly.                  build a soft association between two sets of inputs, and it has
    The N object queries containing rich instance informa-          been widely used for the feature matching task [34, 41]. To
tion are then independently decoded into boxes and class            mitigate the sensitivity towards sensor calibration and infe-
labels by a feed-forward network (FFN). Following Center-           rior image features brought by the hard-association strategy,
Point [58], our FFN predicts the center offset from the query       we leverage the cross-attention mechanism to build the soft
position as δx, δy, bounding box height as z, size l, w, h as       association between LiDAR and images, enabling the net-
log(l), log(w), log(h), yaw angle α as sin(α), cos(α) and           work to adaptively determine where and what information
the velocity (if available) as vx , vy . We also predict a per-     should be taken from the images.
class probability p̂ ∈ [0, 1]K for K semantic classes. Each            Specifically, we first identify the specific image in which
attribute is computed by a separate two-layer 1 × 1 convolu-        the object queries are located using previous predictions as
tion. By decoding each object query into prediction in par-         well as the calibration matrices, and then perform cross at-
allel, we get a set of predictions {b̂t , p̂t }N
                                               t as output, where   tention between the object queries and the corresponding
b̂t is the predicted bounding box for the i-th query. Fol-          image feature map. However, as the LiDAR features and
lowing [23], we adopt the auxiliary decoding mechanism,             image features are from completely different domains, the
which adds FFN and supervision after each decoder layer.            object queries might attend to visual regions unrelated to
Hence, we can have initial bounding box predictions from            the bounding box to be predicted, leading to a long train-
the first decoder layer. We leverage such initial predictions       ing time for the network to accurately identify the proper
in the LiDAR-camera fusion module to constrain the cross            regions on images. Inspired by [9], we design a spatially
attention, as explained in the next section.                        modulated cross attention (SMCA) module, which weighs
                                                                    the cross attention by a 2D circular Gaussian mask around
3.4. LiDAR-Camera Fusion                                            the projected 2D center of each query. The 2D Gaussian
Image Feature Fetching. Although impressive improve-                weight mask M is generated in a similar way as Center-
                                                                                                (i−cx )2 +(j−cy )2
ment has been brought by point-level fusion methods [47,            Net [66], Mij = exp(−              σr 2        ), where (i, j) is
48], their fusion quality is largely limited by the sparsity of     the spatial indices of the weight mask M, (cx , cy ) is the 2D
                                                                                                                                                             #
                                                                                                                                                                                                    Lidar BEV

                                                                                                                                                                                                                                     Query Initialization
                                                                                                                                                                                                     Features
center computed by projecting the query prediction onto the                                                                                                                                             as
                                                                                                                                                                 Collapse along                         $
image plane, r is the radius of the minimum circumscribed                                                                                                        height axis          #
                                                                                                                                                                                                    Multi-Head
circle of the projected corners of the 3D bounding box, and                                                                                     !                maxpool                  as !, #
                                                                                                                                                                                                     Attention
σ is the hyper-parameter to modulate the bandwidth of the                                                                                                "                        "

Gaussian distribution. Then this weight map is element-                                                                                         Image Features                                                  Fused BEV Features
wisely multiplied with the cross-attention map among all                                                                                       Figure 4. We first condense the image features along the vertical
the attention heads. In this way, each object query only at-                                                                                   dimension, and then project the features onto the BEV plane us-
tends to the related region around the projected 2D box, so                                                                                    ing cross attention with the LiDAR BEV features. Each image is
that the network can learn where to select image features                                                                                      processed by a separate multi-head attention layer, which captures
                                                                                                                                               the relation between image column and BEV locations.
based on the input LiDAR features better and faster. The
visualization of the attention map is shown in Fig. 3. The
                                                                                                                                               initialization strategy, which selects object queries leverag-
network typically tends to focus on the foreground pixels
                                                                                                                                               ing both the LiDAR and camera information.
close to the object center and ignore the irrelevant pixels,
                                                                                                                                                   Specifically, we generate a LiDAR-camera BEV feature
providing valuable semantic information for object classifi-
                                                                                                                                               map FLC by projecting the image features FC onto the BEV
cation and bounding box regression. After SMCA, we use
                                                                                                                                               plane through cross attention with LiDAR BEV features
another FFN to produce the final bound box predictions us-
                                                                                                                                               FL . Inspired by [32], we use the multiview image features
ing the object queries containing both LiDAR and image
                                                                                                                                               collapsed along the height axis as the key-value sequence of
information.
                                                                                                                                               the attention mechanism, as shown in Fig. 4. The collaps-
3.5. Label Assignment and Losses                                                                                                               ing operation is based on the observation that the relation
                                                                                                                                               between BEV locations and image columns can be estab-
Following DETR [23], we find the bipartite matching be-
                                                                                                                                               lished easily using camera geometry, and usually there is
tween the predictions and ground truth objects through the
                                                                                                                                               at most one object along each image column. Therefore,
Hungarian algorithm [13], where the matching cost is de-
                                                                                                                                               collapsing along the height axis can significantly reduce the
fined by a weighted sum of classification, regression, and
                                                                                                                                               computation without losing critical information. Although
IoU cost:
                                                                                                                                               some fine-grained image features might be lost during this
   C_{match} = \lambda _1 L_{cls}(p, \hat p) + \lambda _2 L_{reg}(b, \hat b) + \lambda _3 L_{iou}(b, \hat b), \label {eq:matching_cost}  (1)   process, it already meets our need as only a hint on poten-
                                                                                                                                               tial object positions is required. Afterward, similar to Sec.
where Lcls is the binary cross entropy loss, Lreg is the L1                                                                                    3.2, we use FLC to predict the heatmap, which is averaged
loss between the predicted BEV centers and the ground-                                                                                         with the LiDAR-only heatmap Ŝ as the final heatmap ŜLC .
truth centers (both normalized in [0, 1]), and Liou is the                                                                                     Using ŜLC to select and initialize the object queries, our
IoU loss [65] between the predicted boxes and ground-truth                                                                                     model is able to detect objects that are difficult to detect in
boxes. λ1 , λ2 , λ3 are the coefficients of the individual cost                                                                                LiDAR point clouds.
terms. We provide sensitivity analysis of these terms in the                                                                                       Note that proposing a novel method to project the image
supplementary Sec. C. Since the number of predictions is                                                                                       features onto the BEV plane is beyond the scope of this pa-
usually larger than that of GT boxes, the unmatched predic-                                                                                    per. We believe that our method could benefit from more
tions are considered as negative samples. Given all matched                                                                                    research progress [26, 32, 33] in this direction.
pairs, we compute a focal loss [18] for the classification
branch. The bounding box regression is supervised by an
                                                                                                                                               4. Implementation Details
L1 loss for only positive pairs. For the heatmap predic-
tion, we adopt a penalty-reduced focal loss following Cen-                                                                                     Training. We implement our network in PyTorch [25] us-
terPoint [58]. The total loss is the weighted sum of losses                                                                                    ing the open-sourced MMDetection3D [6]. For nuScenes,
for each component. We adopt the same label assignment                                                                                         we use the DLA34 [61] of the pretrained CenterNet as our
strategy and loss formulation for both decoder layers.                                                                                         2D backbone and keep its weights frozen during training,
                                                                                                                                               following [48]. We set the image size to 448 × 800, which
3.6. Image-Guided Query Initialization
                                                                                                                                               performs comparably with full resolution (896 × 1600).
   Since our object queries are currently selected using only                                                                                  VoxelNet [53, 68] is chosen as our 3D backbone. Our train-
LiDAR features, it potentially leads to sub-optimality in                                                                                      ing consists of two stages: 1) We first train the 3D backbone
terms of the detection recall. Empirically, our model al-                                                                                      with the first decoder layer and FFN for 20 epochs, which
ready achieves high recall and shows superior performance                                                                                      only needs the LiDAR point clouds as input and produces
over the baselines (Sec. 5). Nevertheless, to further lever-                                                                                   the initial 3D bounding box predictions. We adopt the same
age the ability of high-resolution images in detecting small                                                                                   data augmentation and training schedules as prior LiDAR-
objects and make our algorithm more robust against sparse                                                                                      only works [58, 69]. Note that we also find the copy-and-
LiDAR point clouds, we propose an image-guided query                                                                                           paste augmentation strategy [53] benefits the convergence
 Method                 Modality     Voxel Size (m)      mAP    NDS    Car     Truck   C.V.   Bus    Trailer   Barrier   Motor.   Bike   Ped.   T.C.
 PointPillar [14]          L          (0.2, 0.2, 8)      40.1   55.0   76.0     31.0   11.3   32.1    36.6      56.4      34.2    14.0   64.0   45.6
 CBGS [69]                 L         (0.1, 0.1, 0.2)     52.8   63.3   81.1     48.5   10.5   54.9    42.9      65.7      51.5    22.3   80.1   70.9
 CenterPoint [58]          L       (0.075, 0.075, 0.2)   60.3   67.3   85.2     53.5   20.0   63.6    56.0      71.1      59.5    30.7   84.6   78.4
 PointPainting [47]       LC          (0.2, 0.2, 8)      46.4   58.1   77.9     35.8   15.8   36.2    37.3      60.2      41.5    24.1   73.3   62.4
 3D-CVF [60]              LC        (0.05, 0.05, 0.2)    52.7   62.3   83.0     45.0   15.9   48.8    49.6      65.9      51.2    30.4   74.2   62.9
 PointAugmenting [48]     LC       (0.075, 0.075, 0.2)   66.8   71.0   87.5     57.3   28.0   65.2    60.7      72.6      74.3    50.9   87.9   83.6
 MVP [59]                 LC       (0.075, 0.075, 0.2)   66.4   70.5   86.8     58.5   26.1   67.4    57.3      74.8      70.0    49.3   89.1   85.0
 FusionPainting [52]      LC       (0.075, 0.075, 0.2)   68.1   71.6   87.1     60.8   30.0   68.5    61.7      71.8      74.7    53.5   88.3   85.0
 TransFusion-L             L       (0.075, 0.075, 0.2)   65.5   70.2   86.2     56.7   28.2   66.3    58.8      78.2      68.3    44.2   86.1   82.0
 TransFusion              LC       (0.075, 0.075, 0.2)   68.9   71.7   87.1     60.0   33.1   68.3    60.8      78.1      73.6    52.9   88.4   86.7
Table 1. Comparison with SOTA methods on the nuScenes test set. ‘C.V.’, ‘Ped.’, and ‘T.C.’ are short for construction vehicle, pedestrian,
and traffic cone, respectively. ‘L’ and ‘C’ represent LiDAR and Camera, respectively. The best results are in boldface (Best LiDAR-only
results are marked blue and best LC results are marked red). For FusionPainting [52], we report the results on the nuScenes website, which
are better than what they reported in their paper. Note that CenterPoint [58] and PointAugmenting [48] utilize double-flip testing while we
do not use any test time augmentation. Please find detailed results here.2

but could disturb the real data distribution, so we disable                   ing, consisting of 700, 150, and 150 scenes for train-
this augmentation for the last 5 epochs following [48] (they                  ing, validation, and testing, respectively. Each frame con-
called a fade strategy). 2) We then train the LiDAR-camera                    tains one point cloud and six calibrated images cover-
fusion and the image-guided query initialization module for                   ing the 360-degree horizontal FOV. For 3D detection, the
another 6 epochs. We find that this two-step training scheme                  main metrics are mean Average Precision (mAP) [7] and
performs better than joint training, since we can adopt more                  nuScenes detection score (NDS). The mAP is defined by
flexible augmentations for the first training stage. See sup-                 the BEV center distance instead of the 3D IoU, and the fi-
plementary Sec. B for the detailed hyper-parameters and                       nal mAP is computed by averaging over distance thresholds
settings on Waymo.                                                            of 0.5m, 1m, 2m, 4m across ten classes. NDS is a consol-
Testing. During inference, the final score is computed as the                 idated metric of mAP and other attribute metrics, includ-
geometric average of the heatmap score Ŝij and the classi-                   ing translation, scale, orientation, velocity, and other box
fication score p̂t . We use all the outputs as our final predic-              attributes. Following CenterPoint [58], we set the voxel size
tions without Non-maximum Suppression (NMS) (see the                          to (0.075m, 0.075m, 0.2m).
effect of NMS in supplementary Sec. D). It is noteworthy                      Waymo Open Dataset. This dataset consists of 798 scenes
that previous point-level fusion methods such as PointAug-                    for training and 202 scenes for validation. The official met-
menting [48] rely on two different models for camera FOV                      rics are mAP and mAPH (mAP weighted by heading accu-
and LiDAR-only regions if the cameras are not 360-degree                      racy). The mAP and mAPH are defined based on the 3D
cameras, because only points in the camera FOV could fetch                    IoU threshold of 0.7 for vehicles and 0.5 for pedestrians
the corresponding image features. In contrast, we use a sin-                  and cyclists. These metrics are further broken down into
gle model to deal with both camera FOV and LiDAR-only                         two difficulty levels: LEVEL1 for boxes with more than
regions, since object queries located outside camera FOV                      five LiDAR points and LEVEL2 for boxes with at least one
will directly ignore the fusion stage and the initial predic-                 LiDAR point. Unlike the 360-degree cameras in nuScenes,
tions from the first decoder layer will be a safeguard.                       the cameras in Waymo only cover around 250 degrees hor-
                                                                              izontally. The voxel size is set to (0.1m, 0.1m, 0.15m).
5. Experiments
                                                                              5.1. Main Results
   In this section, we first make comparisons with the state-
                                                                              nuScenes Results. We submitted our detection results to
of-the-art methods on nuScenes and Waymo. Then we con-
                                                                              the nuScenes evaluation server. Without any test time aug-
duct extensive ablation studies to demonstrate the impor-
                                                                              mentation or model ensemble, our TransFusion outperforms
tance of each key component of TransFusion. Moreover, we
                                                                              all competing non-ensembled methods on the nuScenes
design two experiments to show the robustness of our Trans-
                                                                              leaderboard at the time of submission. As shown in Table 1,
Fusion against inferior image conditions. Besides TransFu-
                                                                              our TransFusion-L already outperforms the state-of-the-
sion, we also include a model variant, which is based on
                                                                              art LiDAR-only methods by a significant margin (+5.2%
the first training stage, i.e., producing the initial bounding
                                                                              mAP, +2.9% NDS) and even surpasses some multi-modality
box predictions using only point clouds. We denote it as
                                                                              methods. We ascribe this performance gain to the rela-
TransFusion-L and believe that it can serve as a strong base-
                                                                              tion modeling power of the transformer decoder as well as
line for LiDAR-only detection. We provide the qualitative
                                                                              the proposed query initialization strategies, which are ab-
results in supplementary Sec. I.
                                                                              lated in Sec. 5.3. Once enabling the proposed fusion com-
nuScenes Dataset. The nuScenes dataset is a large-scale
                                                                              ponents, our TransFusion receives remarkable performance
autonomous-driving dataset for 3D detection and track-
                                                                              boost (+3.4% mAP, +1.5% NDS) and outperforms all the
   2 https://www.nuscenes.org/object-detection                                previous methods, including FusionPainting [52], which
                          Vehicle    Pedestrian   Cyclist   Overall                                 Nighttime     Daytime
   PointPillar [47]        62.5         50.2       59.9      57.6                TransFusion-L         49.2          60.3
   PVRCNN [36]             64.8         46.7        -         -
   LiDAR-RCNN [15]         64.2         51.7       64.4      60.1
                                                                                 CC                 49.4 (+0.2) 63.4 (+3.1)
   CenterPoint [58]        66.1         62.4       67.6      65.3                PA                 51.0 (+1.8) 64.3 (+4.0)
   PointAugmenting [48]    62.2         64.6       73.3      66.7                TransFusion        55.2 (+6.0) 65.7 (+5.4)
   TransFusion-L           65.1         63.7       65.9      64.9     Table 4. mAP breakdown over daytime and nighttime. We exclude
   TransFusion             65.1         64.0       67.4      65.5     categories that do no have any labeled samples.
Table 2. LEVEL 2 mAPH on Waymo validation set. For Center-
Point, we report the performance of single-frame one-stage model      test set only allows at most three submissions, all the ex-
trained in 36 epochs.                                                 periments are conducted on the validation set. For fast it-
                      AMOTA↑         TP↑     FP↓     FN↓      IDS↓    eration, we reduce the first stage training to 12 epochs and
   CenterPoint [58]     63.8        95877   18612   22928      760
   EagerMOT [11]        67.7        93484   17705   24925     1156
                                                                      remove the fade strategy. All the other parameters are the
   AlphaTrack [62]      69.3        95851   18421   22996      718    same as the main experiments. To avoid overstatement, we
   TransFusion-L        68.6        95235   17851   23437      893    additionally build two baseline LiDAR-camera detectors by
   TransFusion          71.8        96775   16232   21846      944    equipping our TransFusion-L with two representative fu-
Table 3. Comparison of the tracking results on nuScenes test set.
                                                                      sion methods on nuScenes: fusing LiDAR and image fea-
Please find detailed results here.3
                                                                      tures by point-wise concatenation (denoted as CC) and the
                                                                      fusion strategy of PointAugmenting (denoted as PA).
uses extra data to train their segmentation sub-networks.
                                                                      Nighttime. We first split the validation set into daytime
Moreover, thanks to our soft-association mechanism, Trans-
                                                                      and nighttime based on scene descriptions provided by
Fusion is robust to inferior image conditions including de-
                                                                      nuScenes and show the performance gain under different
generated image quality and sensor misalignment, as shown
                                                                      situations in Table 4. Our method brings a much larger per-
in the next section.
                                                                      formance gain during nighttime, where the worse lighting
Waymo Results. We report the performance of our model
                                                                      negatively affects the hard-association based fusion strate-
over all three classes on Waymo validation set in Table 2.
                                                                      gies CC and PA.
Our fusion strategy improves the mAPH of pedestrian and
                                                                      Degenerated Image Quality. In Table 5, we randomly drop
cyclist classes by 0.3 and 1.5x, respectively. We suspect two
                                                                      several images for each frame by setting the image features
reasons for the relatively small improvement brought by the
                                                                      of such images to zero during inference. Since both CC
image components. First, the semantic information of im-
                                                                      and PA fuse LiDAR and image features in a tightly-coupled
ages might have less impact on the coarse-grained catego-
                                                                      way, their performance drops significantly when some im-
rization of Waymo. Second, the initial bounding boxes from
                                                                      ages are not available during inference. In contrast, our
the first decoder layer are already with accurate locations
                                                                      TransFusion is able to maintain a high mAP under all cases.
since the point clouds in Waymo are denser than those in
                                                                      When all the six images are not available, CC and PA suf-
nuScenes (see more discussions in supplementary Sec. H).
                                                                      fer from 23.8% and 17.2% mAP degradation, respectively,
Note that CenterPoint achieves a better performance with
                                                                      while TransFusion still keeps the mAP at a competitive level
a multi-frame input and a second-stage refinement mod-
                                                                      of 61.7%. This advantage comes from the sequential design
ule. Such components are orthogonal to our method and we
                                                                      and the attentive fusion strategy, which first generates ini-
leave a more powerful TransFusion for Waymo as the future
                                                                      tial predictions based on LiDAR data and then only gathers
work. PointAugmenting achieves better performance than
                                                                      useful information from image features adaptively. More-
ours but relies on CenterPoint to get the predictions outside
                                                                      over, we could even directly disable the fusion module if
camera FOV for a full-region detection, making their sys-
                                                                      the camera malfunctioning is known, such that the whole
tem less flexible.
                                                                      system could still work seamlessly in a LiDAR-only mode.
Extend to Tracking. To further demonstrate the general-
ization capability, we evaluate our model in a 3D multi-               # Dropped Images     0          1              3             6
object tracking (MOT) task by performing tracking-by-                  CC                  63.3   59.8 (-3.5)   50.9 (-12.4)   39.5 (-23.8)
detection with the same tracking algorithms adopted by                 PA                  64.2   61.6 (-2.6)    55.4 (-8.8)   47.0 (-17.2)
                                                                       TransFusion         65.6   65.1 (-0.5)    63.9 (-1.7)   61.7 (-3.9)
CenterPoint. We refer readers to the original paper [58]
                                                                      Table 5. mAP under different numbers of dropped images. The
for details. As shown in Table 3, our model significantly
                                                                      number in each bracket is the mAP drop from the standard input.
outperforms CenterPoint and sets the new state-of-the-art
results on the leaderboard of nuScenes tracking.                      Sensor Misalignment. We evaluate different fusion meth-
                                                                      ods under a setting where LiDAR and images are not well-
5.2. Robustness against Inferior Image Conditions                     calibrated following RoarNet [39]. Specifically, we ran-
   We design three experiments to demonstrate the robust-             domly add a translation offset to the transformation matrix
ness of our proposed fusion module. Since the nuScenes                from camera to LiDAR sensor. As shown in Fig. 5, Trans-
                                                                      Fusion achieves better robustness against the calibration er-
  3 https://www.nuscenes.org/tracking                                 ror compared with other fusion methods. When two sensors
                66    65.60                    65.60                                                                                                                                               mAP     NDS      Params (M)      Latency (ms)
                                                                       65.58                   65.49
                                                                                                                       65.33

                65
                                                                                                                                               65.11
                                                                                                                                                                                  CenterPoint      57.4    65.2         8.54           117.2
                              64.22                    64.13
                                                                                                                                                                                  TransFusion-L    60.0    66.8         7.96           114.9
                64                                                             63.71                                                                                              CC               63.3    67.6     8.01 + 18.34       212.3
      mAP (%)

                                      63.32

                63
                                                               63.12                                   63.11                                                                      PA               64.2    68.7     13.9 + 18.34       288.2
                                                                                       62.56                                   62.53
                                                                                                                                                                                  w/o Fusion       61.6    67.4     9.08 + 18.34       215.0
                62                                                                                             61.86                                   61.89
                                                                                                                                                                                  w/o Guide        64.8    69.3     8.35 + 18.34       236.9
                61       TransFusion
                                                                                                                                       61.11                                      TransFusion      65.6    69.7     9.47 + 18.34       265.9
                         PA                                                                                                                                    60.48
                                                                                                                                                                               Table 7. Ablation of the proposed fusion components. 18.34 rep-
                         CC
                60            0.0                      0.2                 0.4         0.6                                     0.8                     1.0                     resents the parameter size of the 2D backbone. The latency is
                                                                           Discrepancy (m)
Figure 5. mAP under sensor misalignment cases. The X axis refers                                                                                                               measured on an Intel Core i7 CPU and a Titan V100 GPU. For
to the translational discrepancy between two sensors.                                                                                                                          CenterPoint, we use re-implementations in MMDetection3D.

                                                                                                                                                                               ule (denoted as w/o Fusion) and the image-guided query
are misaligned by 1m, the mAP of our model only drops by                                                                                                                       initialization (denoted as w/o Guide). As shown in Table 7,
0.49%, while the mAP of PA and CC degrades by 2.33%                                                                                                                            the image feature fusion and image-guided query initializa-
and 2.85%, respectively. In our method, the calibration ma-                                                                                                                    tion bring 4.8% and 1.6% mAP gain, respectively. The for-
trix is only used for projecting the object queries onto im-                                                                                                                   mer provides more distinctive instance features, which are
ages, and the fusion module is not strict with the projected                                                                                                                   particularly critical for classification on nuScenes, where
locations since the attention mechanism could adaptively                                                                                                                       some categories are challenging to distinguish, such as
find the relevant image features around based on the con-                                                                                                                      trailer and construction vehicle. The latter affects less, since
text information. The insensitivity towards sensor calibra-                                                                                                                    TransFusion-L already has enough recall. We believe the
tion also enables the possibility to pipelining the 2D and 3D                                                                                                                  latter will be more useful when point clouds are sparser.
backbones such that the LiDAR features are fused with the                                                                                                                      Compared with other fusion methods, our fusion strategy
features from the previous images [47].                                                                                                                                        brings a larger performance gain with a modestly increas-
                                                                                                                                                                               ing number of parameters and latency. To better understand
5.3. Ablation Studies                                                                                                                                                          where the improvements are from, we show the mAP break-
                                                                                                                                                                               down on different subsets based on the range in Table 8. Our
   We conduct ablation studies on the nuScenes validation
                                                                                                                                                                               fusion method gives larger performance boost for distant re-
set to study the effectiveness of the proposed components.
                                                                                                                                                                               gions where 3D objects are difficult to detect or classify in
                     C.A.                     I.D.                #Layers                      #Epochs                             mAP                     NDS                 LiDAR modality.
       a)             ✓                        ✓                     1                           12                                60.0                    66.8
       b)                                      ✓                     1                           12                                54.3                    63.9                                         <15m         15-30m          >30m
       c)             ✓                        ✓                     3                           12                                59.9                    67.1                      TransFusion-L       70.4          59.5           35.3
                                                                                                                                                                                     TransFusion      75.5 (+5.1)   66.9 (+7.4)    43.7 (+8.4)
       d)             ✓                                              1                           12                                24.0                    33.8
       e)             ✓                                              3                           12                                28.3                    43.4                Table 8. mAP breakdown over BEV distance between object cen-
       f)             ✓                                              3                           36                                46.9                    57.8                ter and ego vehicle in meters.
Table 6. Ablation of the query initialization module.                                                                                                                  C.A.:
category-aware; I.D.: input-dependent.                                                                                                                                         6. Conclusion
Query Initialization. In Table 6, we study how the query                                                                                                                          We have designed an effective and robust transformer-
initialization strategy affects the performance of the initial                                                                                                                 based LiDAR-camera 3D detection framework with a soft-
bounding box prediction. a) the first row is TransFusion-L.                                                                                                                    association mechanism to adaptively determine where and
b) when the category-embedding is removed, NDS drops                                                                                                                           what information should be taken from images. Our Trans-
to 63.9%. d)-f) shows the performance of the models                                                                                                                            Fusion sets the new state-of-the-art results on the nuScenes
trained without the input-dependent strategy. Specifically,                                                                                                                    detection and tracking leaderboards, and shows competi-
we make the query positions as a set of learnable parame-                                                                                                                      tive results on Waymo detection benchmark. The exten-
ters (N × 2) to capture the statistics of potential object lo-                                                                                                                 sive ablative experiments demonstrate the robustness of our
cations in the dataset. The model under this setting only                                                                                                                      method against inferior image conditions. We hope that our
achieves 33.8% NDS. Increasing the number of decoder                                                                                                                           work will inspire further investigation of LiDAR-camera fu-
layers or the number of training epochs boosts the perfor-                                                                                                                     sion for driving-scene perception, and the application of a
mance, but TransFusion-L still outperforms the model in (f)                                                                                                                    soft-association based fusion strategy to other tasks, such as
by 9.0% NDS. a), c): In contrast, with the proposed query                                                                                                                      3D segmentation.
initialization strategy, our TransFusion-L does not require                                                                                                                    Acknowledgements. This work is supported by Hong
more decoder layers.                                                                                                                                                           Kong RGC (GRF 16206819, 16203518, T22-603/15N),
Fusion Components. To study how the image informa-                                                                                                                             Guangzhou Okay Information Technology with the project
tion benefits the detection results, we ablate the proposed                                                                                                                    GZETDZ18EG05, and City University of Hong Kong (No.
fusion components by removing the feature fusion mod-                                                                                                                          7005729).
References                                                             [19] Zili Liu, Guodong Xu, Honghui Yang, Minghao Chen,
                                                                            Kuoliang Wu, Zheng Yang, Haifeng Liu, and Deng Cai.
 [1] Holger Caesar, Varun Bankiti, Alex H. Lang, Sourabh Vora,              Suppress-and-refine framework for end-to-end 3d object de-
     Venice Erin Liong, Qiang Xu, Anush Krishnan, Yu Pan, Gi-               tection. arXiv, 2021. 2
     ancarlo Baldan, and Oscar Beijbom. nuScenes: A multi-             [20] Ze Liu, Zheng Zhang, Yue Cao, Han Hu, and Xin Tong.
     modal dataset for autonomous driving. CVPR, 2020. 1                    Group-free 3d object detection via transformers. ICCV,
 [2] Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas             2021. 2, 3
     Usunier, Alexander Kirillov, and Sergey Zagoruyko. DETR:          [21] Jiageng Mao, Yujing Xue, Minzhe Niu, Haoyue Bai, Jiashi
     End-to-end object detection with transformers. ECCV, 2020.             Feng, Xiaodan Liang, Hang Xu, and Chunjing Xu. Voxel
     2, 3                                                                   transformer for 3d object detection. ICCV, 2021. 2
 [3] Qi Chen, Lin Sun, Ernest C. H. Cheung, and A. Yuille. Every       [22] Gregory P. Meyer, Jake Charland, Darshan Hegde,
     View Counts: Cross-view consistency in 3d object detection             Ankita Gajanan Laddha, and Carlos Vallespi-Gonzalez. Sen-
     with hybrid-cylindrical-spherical voxelization. NeurIPS,               sor fusion for joint 3d object detection and semantic segmen-
     2020. 2                                                                tation. CVPRW, 2019. 1
 [4] Qi Chen, Lin Sun, Zhixin Wang, K. Jia, and A. Yuille. Object      [23] Ishan Misra, Rohit Girdhar, and Armand Joulin. An End-
     as Hotspots: An anchor-free 3d object detection approach via           to-End Transformer Model for 3D Object Detection. ICCV,
     firing of hotspots. ECCV, 2020. 2                                      2021. 2, 3, 4, 5
 [5] Xiaozhi Chen, Huimin Ma, Jixiang Wan, B. Li, and Tian             [24] Xuran Pan, Zhuofan Xia, Shiji Song, L. Li, and Gao Huang.
     Xia. Multi-view 3d object detection network for autonomous             3d object detection with pointformer. CVPR, 2021. 2
     driving. CVPR, 2017. 1, 2                                         [25] Adam Paszke, Sam Gross, Soumith Chintala, Gregory
 [6] MMDetection3D Contributors. MMDetection3D: Open-                       Chanan, Edward Yang, Zachary DeVito, Zeming Lin, Al-
     MMLab next-generation platform for general 3D object                   ban Desmaison, Luca Antiga, and Adam Lerer. Automatic
     detection. https://github.com/open- mmlab/                             differentiation in pytorch. NeurIPS-W, 2017. 5
     mmdetection3d, 2020. 5, 2                                         [26] Jonah Philion and S. Fidler. Lift, Splat, Shoot: Encoding
 [7] M. Everingham, L. Gool, Christopher K. I. Williams, J.                 images from arbitrary camera rigs by implicitly unprojecting
     Winn, and Andrew Zisserman. The pascal visual object                   to 3d. ECCV, 2020. 5
     classes (voc) challenge. IJCV, 2009. 6                            [27] C. Qi, Xinlei Chen, O. Litany, and L. Guibas. ImVoteNet:
 [8] Lue Fan, Xuan Xiong, Feng Wang, Naiyan Wang, and                       Boosting 3d object detection in point clouds with image
     Zhaoxiang Zhang. RangeDet: In defense of range view for                votes. CVPR, 2020. 2
     lidar-based 3d object detection. ICCV, 2021. 2                    [28] C. Qi, O. Litany, Kaiming He, and L. Guibas. Deep hough
 [9] Peng Gao, Minghang Zheng, Xiaogang Wang, Jifeng Dai,                   voting for 3d object detection in point clouds. ICCV, 2019.
     and Hongsheng Li. Fast convergence of detr with spatially              2
     modulated co-attention. ICCV, 2021. 3, 4                          [29] C. Qi, W. Liu, Chenxia Wu, Hao Su, and L. Guibas. Frustum
[10] Tengteng Huang, Zhe Liu, Xiwu Chen, and X. Bai. EPNet:                 pointnets for 3d object detection from rgb-d data. CVPR,
     Enhancing point features with image semantics for 3d object            2018. 1, 2
     detection. ECCV, 2020. 1, 2                                       [30] C. Qi, Hao Su, Kaichun Mo, and L. Guibas. PointNet: Deep
[11] Aleksandr Kim, Aljosa Osep, and Laura Leal-Taixé. Ea-                 learning on point sets for 3d classification and segmentation.
     gerMOT: 3d multi-object tracking via sensor fusion. ICRA,              CVPR, 2017. 1
     2021. 7                                                           [31] Shaoqing Ren, Kaiming He, Ross B. Girshick, and J. Sun.
[12] Jason Ku, Melissa Mozifian, Jungwook Lee, Ali Harakeh,                 Faster R-CNN: Towards real-time object detection with re-
     and Steven L. Waslander. Joint 3d proposal generation and              gion proposal networks. TPAMI, 2015. 1, 2
     object detection from view aggregation. IROS, 2018. 1             [32] Thomas Roddick and R. Cipolla. Predicting semantic map
[13] H. Kuhn. The hungarian method for the assignment problem.              representations from images using pyramid occupancy net-
     Naval Research Logistics Quarterly, 1955. 5                            works. CVPR, 2020. 5
[14] Alex H. Lang, Sourabh Vora, Holger Caesar, Lubing Zhou,           [33] Thomas Roddick, Alex Kendall, and R. Cipolla. Ortho-
     Jiong Yang, and Oscar Beijbom. PointPillars: Fast encoders             graphic feature transform for monocular 3d object detection.
     for object detection from point clouds. CVPR, 2019. 1, 2, 6            BMVC, 2019. 5
[15] Zhichao Li, Feng Wang, and Naiyan Wang. LiDAR R-CNN:              [34] Paul-Edouard Sarlin, Daniel DeTone, Tomasz Malisiewicz,
     An efficient and universal 3d object detector. CVPR, 2021. 7           and Andrew Rabinovich. SuperGlue: Learning feature
[16] Ming Liang, Binh Yang, Yun Chen, Rui Hu, and R. Urta-                  matching with graph neural networks. CVPR, 2020. 4
     sun. Multi-task multi-sensor fusion for 3d object detection.      [35] Hualian Sheng, Sijia Cai, Yuan Liu, Bing Deng, Jianqiang
     CVPR, 2019. 1                                                          Huang, Xiansheng Hua, and Min-Jian Zhao. Improving 3d
[17] Ming Liang, Binh Yang, Shenlong Wang, and R. Urtasun.                  object detection with channel-wise transformer. ICCV, 2021.
     Deep continuous fusion for multi-sensor 3d object detection.           2
     ECCV, 2018. 1                                                     [36] Shaoshuai Shi, Chaoxu Guo, Li Jiang, Zhe Wang, Jianping
[18] Tsung-Yi Lin, Priya Goyal, Ross B. Girshick, Kaiming He,               Shi, Xiaogang Wang, and Hongsheng Li. PV-RCNN: Point-
     and Piotr Dollár. Focal loss for dense object detection. ICCV,        voxel feature set abstraction for 3d object detection. CVPR,
     2017. 5                                                                2020. 2, 7
[37] Shaoshuai Shi, Xiaogang Wang, and Hongsheng Li. PointR-              with adaptive attention for 3d object detection. ITSC, 2021.
     CNN: 3d object proposal generation and detection from                1, 6
     point cloud. CVPR, 2019. 2                                      [53] Yan Yan, Yuxing Mao, and B. Li. SECOND: Sparsely em-
[38] Shaoshuai Shi, Zhe Wang, Jianping Shi, Xiaogang Wang,                bedded convolutional detection. Sensors, 2018. 2, 5
     and Hongsheng Li. From Points to Parts: 3d object detec-        [54] Binh Yang, Wenjie Luo, and R. Urtasun. PIXOR: Real-time
     tion from point cloud with part-aware and part-aggregation           3d object detection from point clouds. CVPR, 2018. 2
     network. TPAMI, 2021. 2                                         [55] Zetong Yang, Y. Sun, Shu Liu, and Jiaya Jia. 3DSSD: Point-
[39] Kiwoo Shin, Y. Kwon, and M. Tomizuka. RoarNet: A ro-                 based 3d single stage object detector. CVPR, 2020. 2
     bust 3d object detection based on region approximation re-      [56] Zetong Yang, Y. Sun, Shu Liu, Xiaoyong Shen, and Jiaya
     finement. IV, 2019. 1, 2, 7                                          Jia. STD: Sparse-to-dense 3d object detector for point cloud.
[40] Vishwanath A. Sindagi, Yin Zhou, and Oncel Tuzel. MVX-               ICCV, 2019. 2
     Net: Multimodal voxelnet for 3d object detection. ICRA,         [57] Z. Yao, Jiangbo Ai, Boxun Li, and Chi Zhang. Efficient
     2019. 1, 2                                                           DETR: Improving end-to-end object detector with dense
[41] Jiaming Sun, Zehong Shen, Yuang Wang, Hujun Bao, and                 prior. arXiv, 2021. 3
     Xiaowei Zhou. LoFTR: Detector-free local feature matching       [58] Tianwei Yin, Xingyi Zhou, and Philipp Krähenbühl. Center-
     with transformers. CVPR, 2021. 4                                     based 3d object detection and tracking. CVPR, 2021. 2, 4, 5,
[42] Peize Sun, Yi Jiang, Enze Xie, Wenqi Shao, Zehuan Yuan,              6, 7
     Changhu Wang, and Ping Luo. OneNet: What makes for              [59] Tianwei Yin, Xingyi Zhou, and Philipp Krähenbühl. Multi-
     end-to-end object detection? In ICML, 2021. 3                        modal virtual point 3d detection. NeurIPS, 2021. 6
[43] Pei Sun, Henrik Kretzschmar, Xerxes Dotiwalla, Aurelien         [60] Jin Hyeok Yoo, Yeocheol Kim, Ji Song Kim, and J. Choi.
     Chouard, Vijaysai Patnaik, P. Tsui, James Guo, Yin Zhou,             3D-CVF: Generating joint camera and lidar features using
     Yuning Chai, Benjamin Caine, Vijay Vasudevan, Wei Han,               cross-view spatial feature fusion for 3d object detection.
     Jiquan Ngiam, Hang Zhao, Aleksei Timofeev, S. Ettinger,              ECCV, 2020. 1, 6
     Maxim Krivokon, A. Gao, Aditya Joshi, Y. Zhang, Jonathon        [61] F. Yu, Dequan Wang, and Trevor Darrell. Deep layer aggre-
     Shlens, Zhifeng Chen, and Dragomir Anguelov. Scalability             gation. CVPR, 2018. 5
     in perception for autonomous driving: Waymo open dataset.       [62] Yihan Zeng, Chao Ma, Ming Zhu, Zhiming Fan, and Xi-
     CVPR, 2020. 1                                                        aokang Yang. Cross-modal 3d object detection and tracking
[44] Pei Sun, Weiyue Wang, Yuning Chai, Gamaleldin F. Elsayed,            for auto-driving. IROS, 2021. 7
     Alex Bewley, Xiao Zhang, Cristian Sminchisescu, and Drago       [63] Wenwei Zhang, Zhe Wang, and Chen Change Loy. Multi-
     Anguelov. RSN: Range sparse net for efficient, accurate lidar        modality cut and paste for 3d object detection. arXiv, 2020.
     3d object detection. CVPR, 2021. 2                                   1
[45] Pei Sun, Rufeng Zhang, Yi Jiang, T. Kong, Chenfeng Xu,          [64] Lin Zhao, Hui Zhou, Xinge Zhu, Xiao Song, Hongsheng Li,
     W. Zhan, M. Tomizuka, L. Li, Zehuan Yuan, C. Wang, and               and Wenbing Tao. LIF-Seg: Lidar and camera image fusion
     Ping Luo. Sparse R-CNN: End-to-end object detection with             for 3d lidar semantic segmentation. arXiv, 2021. 1
     learnable proposals. CVPR, 2021. 2, 3
                                                                     [65] Dingfu Zhou, Jin Fang, Xibin Song, Chenye Guan, Junbo
[46] Ashish Vaswani, Noam M. Shazeer, Niki Parmar, Jakob                  Yin, Yuchao Dai, and Ruigang Yang. Iou loss for 2d/3d ob-
     Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and           ject detection. 3DV, 2019. 5
     Illia Polosukhin. Attention is all you need. NeurIPS, 2017.
                                                                     [66] Xingyi Zhou, Dequan Wang, and Philipp Krähenbühl. Ob-
     3, 2
                                                                          jects as points. arXiv, 2019. 3, 4
[47] Sourabh Vora, Alex H. Lang, Bassam Helou, and Oscar Bei-
                                                                     [67] Yin Zhou, Pei Sun, Y. Zhang, Dragomir Anguelov, J. Gao,
     jbom. PointPainting: Sequential fusion for 3d object detec-
                                                                          Tom Y. Ouyang, James Guo, Jiquan Ngiam, and Vijay Va-
     tion. CVPR, 2020. 1, 2, 4, 6, 7, 8
                                                                          sudevan. MVF: End-to-end multi-view fusion for 3d object
[48] Chunwei Wang, Chao Ma, Ming Zhu, and Xiaokang Yang.                  detection in lidar point clouds. CoRL, 2019. 2
     PointAugmenting: Cross-modal augmentation for 3d object
                                                                     [68] Yin Zhou and Oncel Tuzel. VoxelNet: End-to-end learning
     detection. CVPR, 2021. 1, 2, 4, 5, 6, 7
                                                                          for point cloud based 3d object detection. CVPR, 2018. 1, 2,
[49] Yue Wang, Alireza Fathi, Abhijit Kundu, David A. Ross,               5
     Caroline Pantofaru, Thomas A. Funkhouser, and Justin M.
                                                                     [69] Benjin Zhu, Zhengkai Jiang, Xiangxin Zhou, Zeming Li, and
     Solomon. Pillar-based object detection for autonomous driv-
                                                                          Gang Yu. Class-balanced grouping and sampling for point
     ing. In ECCV, 2020. 2
                                                                          cloud 3d object detection. arXiv, 2019. 2, 5, 6
[50] Yue Wang and Justin Solomon. Object DGCNN: 3d object
                                                                     [70] Xinge Zhu, Yuexin Ma, Tai Wang, Yan Xu, Jianping Shi, and
     detection using dynamic graphs. NeurIPS, 2021. 3
                                                                          Dahua Lin. SSN: Shape signature networks for multi-class
[51] Liang Xie, Chao Xiang, Zhengxu Yu, Guodong Xu, Zheng                 object detection from point clouds. ECCV, 2020. 2
     Yang, Deng Cai, and Xiaofei He. PI-RCNN: An efficient
                                                                     [71] Xizhou Zhu, Weijie Su, Lewei Lu, Bin Li, Xiaogang Wang,
     multi-sensor 3d object detector with point-based attentive
                                                                          and Jifeng Dai. Deformable DETR: Deformable transform-
     cont-conv fusion module. AAAI, 2020. 1
                                                                          ers for end-to-end object detection. ICLR, 2021. 3, 2
[52] Shaoqing Xu, Dingfu Zhou, Jin Fang, Junbo Yin, Bin Zhou,
     and Liangjun Zhang. FusionPainting: Multimodal fusion
                                                                                   output bounding boxes                              output bounding boxes
Supplementary Material
   The supplementary document is organized as follows:                                     FFN                                                FFN
                                                                                                           ×%                                                 ×%

  • Sec. A depicts the detailed network architectures of our                        Add & Norm                                         Add & Norm
    transformer decoder layers.                                                     Feed Forward                                       Feed Forward
  • Sec. B provides the implementation details of TransFu-
    sion and the training settings on nuScenes and Waymo.                           Add & Norm                                         Add & Norm

  • Sec. C reports our sensitivity analysis of the matching                             Multi-Head
                                                                                                                                            Spatial
                                                                                                                                           Modulated
    cost during label assignment.                               LiDAR BEV               Attention                   Image                  Attention
                                                                Features            V      K     Q                  Features           V      K     Q
  • Sec. D presents the effect of NMS on TransFusion and
    CenterPoint.                                                                    Add & Norm                                         Add & Norm
  • Sec. E provides the results of using PointPillars as our
                                                                                        Multi-Head                                         Multi-Head
    3D backbone.                                                                        Attention                                          Attention
  • Sec. F discusses the effect of 2D backbone in TransFu-                          V      K     Q                                     V      K     Q

    sion.
  • Sec. G shows the results with different number of ob-
    ject queries.                                                query positions    category-aware                query positions        query features
                                                                                     query features             projected on images    from LiDAR-only
  • Sec. H discusses the performance gain of image infor-
    mation on Waymo.                                             Figure 6. Left: Architecture of the transformer decoder layer for
  • Sec. I provides visualization results on the nuScenes        initial bounding box prediction. Right: Architecture of the trans-
    and Waymo datasets.                                          former decoder layer for image fusion.

A. Network Architectures
                                                                 avoid mistakenly suppress nearby instances for small ob-
    The detailed architectures of the respective transformer     jects, we do not check the local maximum for pedestrian
decoder layers for initial bounding box prediction and           and traffic cone on nuScenes and for pedestrian and cyclist
LiDAR-camera fusion are shown in Fig. 6. Following [20],         on Waymo. Following PointAugmenting [48], we adopt
we adopt the common practice of transformer except that          DLA34 of CenterNet pre-trained on monocular 3D detec-
we use the learned positional encoding instead of the fixed      tion task as our 2D backbone for nuScenes. Since there
sine positional encoding [46]. For the image-guided query        is no public available 2D backbone pre-trained on Waymo
initialization module, we use the LiDAR BEV features as          dataset, we train a Faster-RCNN [31] using the 2D labels
query sequence and collapsed image features as key-value         provided by Waymo and use its ResNet50 and FPN as our
sequence, and only perform cross attention to save the com-      2D backbone. We freeze the weight of image backbone dur-
putation cost. Our model can benefit from the efficient at-      ing training and set the image resolution to half of the full
tention mechanisms in recent works such as [71].                 resolution for both nuScenes and Waymo to speed up the
                                                                 training process.
B. Implementation Details
                                                                 nuScenes. Following the common practice, we transform
   Our implementation is based on the open-sourced code-         previous ten LiDAR sweeps into the current frame to pro-
base MMDetection3D [6], which provides many popu-                duce a denser point cloud input for both training and infer-
lar 3D detection methods, including PointPillar, VoxelNet,       ence. The detection range is set to [−51.2m, 51.2m] for
and CenterPoint. For our 3D backbone, we set its hyper-          X and Y axes, and [−5m, 3m] for Z axis. The maximum
parameters according to CenterPoint-Voxel’s official im-         numbers of non-empty voxels for training and inference
plementation. For the transformer-decoder-based detection        are set to 120,000 and 160,000, respectively. In terms of
head, the hidden dimension d is set to 256 and dropout is set    the data augmentation strategy, we adopt random flipping
to 0.1. We use N = 200 and 300 queries for nuScenes and          along both X and Y axes, global scaling with a random fac-
Waymo since the max numbers of objects in one frame are          tor from [0.9, 1.1], global rotation between [−π/8, π/8], as
142 and 185, respectively. Since our object queries are non-     well as the copy-and-paste augmentation [53]. We follow
parametric, we are able to modify the number of queries          CBGS [69] to perform class-balanced sampling and opti-
during inference. We provide the ablations on the number of      mize the network using the AdamW optimizer with one-
object queries in Sec. G. When selecting object queries from     cycle learning rate policy, with max learning rate 0.001,
the heatmap, we pick local maximum pixels whose values           weight decay 0.01, and momentum 0.85 to 0.95. We train
are greater than or equal to their 8-connected neighbors. To     the 3D backbone with the first decoder layer and FFN for
20 epochs, and the LiDAR-camera fusion components for                Matching strategy     λ1     λ2     λ3    mAP NDS        Ped.   T.C.
                                                                         Hungarian         2.0   0.25   0.25   Not Converge
6 epochs with batch size of 16 using 8 Tesla V100 GPUs.                  Hungarian         0.5   0.25   0.25   58.5   66.0    83.8   70.5
We use gradient clipping at an l2 norm of 0.1 to stabilize               Hungarian        0.25   0.25   0.25   59.2   66.1    85.2   71.6
the training process. The weighting coefficients of heatmap              Hungarian        0.15   0.25   0.25   60.0   66.8    86.1   72.1
                                                                         Hungarian         0.1   0.25   0.25   59.3   66.3    85.3   71.6
loss, classification loss, and regression loss are 1.0, 1.0              Hungarian        0.15   0.25   0.5    59.2   66.1    85.2   70.2
and 0.25, respectively. The coefficients of matching cost                Hungarian        0.15   0.25   0.15   59.5   66.3    85.2   71.8
λ1 , λ2 , λ3 are 0.15, 0.25, 0.25, respectively. The sensitivity         Hungarian        0.15   0.25   0.1    59.0   65.9    85.1   72.4
                                                                    Heuristic (w/o NMS)                        56.7   65.3    67.3   56.6
analysis of the matching cost coefficients is provided in the        Heuristic (w NMS)                         60.0   67.0    85.6   71.0
next section.
Waymo. For Waymo, we only use a single sweep as input              Table 9. Ablation study on the matching cost coefficients in Eq. 1.
and set the detection range to [−75.2m, 75.2m] for X and           ‘Ped.’, and ‘T.C.’ are short for pedestrian, and traffic cone, respec-
Y axes, and [−2m, 4m] for Z axis. The maximum number               tively.
of non-empty voxels is set to 150,000. We adopt the same
training strategies as nuScenes except: 1) The first stage         to-end detectors with non-end-to-end detectors, and claims
training last for 36 epochs with batch size of 16 under a          that the one-to-one positive sample assignment as well as
max learning rate of 0.001. 2) The weighting coefficient of        classification cost in the matching cost are the two key fac-
regression loss is changed to 2.0, following CenterPoint. 3)       tors in producing a large score gap between duplicate pre-
The matching cost coefficients are set to 0.075, 0.25, 0.25,       diction and building an end-to-end detection system with-
respectively.                                                      out NMS. We refer readers to the original paper [42] for
                                                                   more details. Following DETR’s label assignment strat-
C. Label Assignment Strategy                                       egy, our method naturally satisfies these two requirements
                                                                   and do not need NMS. As show in Table 10, our method
   Following DETR, we perform label assignment by find-
                                                                   still maintains a high mAP without NMS while CenterPoint
ing the bipartite matching between predictions and ground-
                                                                   drops about 12% mAP. This advantage eliminates the hand-
truth objects through the Hungarian algorithm. In Table 12,
                                                                   designed NMS post-processing step and makes TransFu-
we study the effect of the coefficient of each matching cost
                                                                   sion more practical and handy for deployment to new sce-
term on the detection performance of TransFusion-L. Since
                                                                   narios in the real applications. Besides, since the Heuristic
the matching results are only decided by the relative values
                                                                   strategy mentioned in Sec. C does not have classification
of individual matching cost terms, we keep λ2 = 0.25 and
                                                                   cost involved in the assignment stage, this strategy is un-
try different values for λ1 and λ3 . As shown in Table 12, we
                                                                   able to produce a large score gap between duplicate predic-
find the network suffers from a convergence issue when the
                                                                   tion. This is why it does not perform as well as the baseline
coefficient of the classification cost is too large, and the de-
                                                                   model on Pedestrian and Traffic cone.
tection performance is not sensitive to the coefficient within
a reasonable range. Since the weighting coefficients of the                      Method          with NMS       without NMS
matching cost need some tuning, we additionally propose                        CenterPoint         57.41            45.70
a heuristic label assignment strategy (denoted as Heuris-                     TransFusion-L        59.95            59.98
tic) to avoid hyper-parameter tuning. The Heuristic assign-                    TransFusion         65.58            65.60
ment strategy follows the simple rules: each GT box will
                                                                   Table 10. Effect of NMS. We report the mAP of CenterPoint and
only be assigned to the predicted box with the same cate-
                                                                   our TransFusion on nuScenes validation set. The results of Cen-
gory and the smallest center distance. If a conflict appears,
                                                                   terPoint are reproduced using MMDetection3D, which also uses a
the predicted box will be matched to the closer GT box.            resolution of (0.075m, 0.075m, 0.2m) without any test time aug-
In this way, we also find the one-to-one matching between          mentation.
prediction and GT but with some GT boxes unused. We
find Heuristic works quite well for uncrowded scenes but
for objects in a crowded scene, such as pedestrian or traffic      E. Pillar-based 3D Backbone
cone in nuScenes, it is unable to prevent duplicate predic-
tions, which will be further explained in Sec. D.                     To demonstrate our framework’s compatibility with
                                                                   other 3D backbones, we use PointPillars as our 3D back-
D. Effect of NMS                                                   bone to produce the BEV features, while keeping all the
                                                                   other settings the same as the main experiments. The voxel
   Recently, many works [2, 45, 71] in 2D detection have           size is set to (0.2m, 0.2m). As shown in Table 11, our
focused on removing the last non-differentiable compo-             model outperforms CenterPoint by a remarkable margin un-
nent, Non-Maximum Suppression (NMS), in the detection              der the same pillar-based backbone, showing its great gen-
pipeline. OneNet [42] systematically compares the end-             eralization ability.
                            PointPillars    VoxelNet
                            mAP NDS        mAP NDS                  G. Adapt Queries at Test Time
          CenterPoint       50.3 60.2      59.6 66.8
          TransFusion-L     54.5 62.7      65.1 70.1                   Unlike DETR, our object queries are non-parametric and
          TransFusion       58.3 64.5      67.5 71.3                input-dependent. These two characteristics allow us to use
          Table 11. Results on nuScenes validation set.             different numbers of queries during inference. It could be
                                                                    useful when we have some prior knowledge about a scene,
                                                                    such as its crowdedness. In Table 13, we provide the perfor-
F. Discussions of the 2D Network                                    mance evaluated under different object queries for the same
                                                                    model trained under N = 200 queries. Note that we use
   Current multi-modality detection models usually employ
                                                                    N = 200 to get all the numbers in the main text for its bet-
CNN features from 2D networks pre-trained on different
                                                                    ter performance-efficiency trade-off and use N = 300 for
tasks (i.e., segmentation or detection) and with different res-
                                                                    online submission for a slightly better performance.
olution (i.e., different levels from ResNet or DLA). There is
no existing work analyzing what kind of image features are                      #queries    100    200     300    500
most useful for a 3D detection model, and using improper                         mAP        64.2   65.6    65.9   66.0
image features might prevent the release of the potential for                    NDS        69.2   69.7    69.8   69.8
a multi-modality detection system. We believe that the se-
quential design of our method enables a flexible and off-the-       Table 13. Results with different numbers of queries. We keep the
shelf experiment base to explore the effects of different im-       model unchanged and only use different numbers of queries for
age features. Therefore, we explore this question by fixing         evaluation.
the 3D backbone with the first decoder layer and performing
the second stage training with different image features.
                                                                    H. Dicussions on Waymo
        Arch.                   Task            mAP       NDS          Our TransFusion brings smaller performance gain over
       DLA34              Monocular 3D Det.     65.6      69.7      TransFusion-L on Waymo compared with that on nuScenes.
   R50+FPN Level 0             2D Det.          66.4      70.1      We speculate that this is mainly due to the following two
   R50+FPN Level 0         2D Instance Seg.     66.6      70.1      reasons:
   R50+FPN Level 1         2D Instance Seg.     66.5      70.1
   R50+FPN Level 2         2D Instance Seg.     66.3      70.0       (i) As shown in Table 1, compared with TransFusion-
   R50+FPN Level 3         2D Instance Seg.     65.4      69.6           L, TransFusion brings the largest performance in-
                                                                         crease for bicycle (+8.7%), motorcycle (+5.4%), and
Table 12. mAP under different 2D backbones. ‘Det.’ and ‘Seg.’            construction vehicle (+4.9%) in terms of mAP on
are short for detection and segmentation, respectively. For DLA34        nuScenes. Due to the geometrical ambiguity, objects
on monocular 3D detection, we acquire the CenterNet pre-trained          from the above three categories are difficult to dis-
on nuScenes4 following PointAugmenting. For ResNet50 on in-              tinguish using LiDAR information only, and thus the
stance segmentation, we acquire the model pre-trained on nuIm-
                                                                         semantic information of images is extraordinarily im-
ages from MMDetection3D. For ResNet50 on 2D detection, we
                                                                         portant for more accurate classification. However, the
train the model by ourself using MMDetection3D since there is no
open-sourced model weights.                                              categorization of Waymo is rather coarse-gained (i.e.,
                                                                         vehicle, pedestrian, cyclist), which hides the improve-
                                                                         ment brought by the image information to some extent.
   From Table 12, we find image features of the 2D instance         (ii) The LiDAR point clouds in Waymo are much denser
segmentation model bring the largest performance boost                   than those in nuScenes (see Sec. I for visualizations).
compared with that of detection models. In terms of dif-                 Thus the bounding box predictions of TransFusion-L
ferent levels of the feature pyramid, the feature map of level           are already with accurate localization, which reduces
0 (stride 4) brings a slightly larger performance gain. We               the room for further improvement by image fusion.
suspect the image features at that level contain more fine-
grained information which is important to distinguish small         I. Qualitative Results
or distant objects. Image features from level 1 (stride 8) and
level 2 (stride 16) can bring a similar gain with a smaller            We first compare the detection results of TransFu-
resolution of feature maps, while image features from level         sion and TransFusion-L on the nuScenes dataset in Fig. 7.
3 (stride 32) yields a drop of 1.2% mAP in comparison with          The image information improves the performance of the
the level-0 counterpart due to the row resolution.                  LiDAR-only baseline through reducing the False Positive
                                                                    and False Negative. More visualization results on Waymo
                                                                    and nuScenes datasets are shown in Fig. 8 and Fig. 9, re-
  4 https://github.com/xingyizhou/CenterTrack                       spectively.
          LiDAR-only                   LiDAR-Camera                        Input Image (selected view)

          LiDAR-only                   LiDAR-Camera                       Input Image (selected view)

Figure 7. Qualitative comparison between TransFusion-L and TransFusion on the nuScenes dataset. Blue boxes and green boxes are the
predictions and ground-truth, respectively. Best viewed with color and zoom-in.
Figure 8. Visualization of detection results on the Waymo dataset. Our model predicts highly accurate bounding boxes for nearby vehicles
and pedestrians (note that cyclists are very rare in the dataset) and also handles objects with severe occlusion. Blue boxes and green boxes
are the predictions and ground-truth, respectively. Best viewed with color and zoom-in.

Figure 9. Visualization of detection results on the nuScenes dataset. Compared with Waymo, nuScenes has much sparser point clouds and
smaller objects such as traffic cones. Nevertheless, our model successfully detects such objects even with only few points observed. Blue
boxes and green boxes are the predictions and ground-truth, respectively. Best viewed with color and zoom-in.
