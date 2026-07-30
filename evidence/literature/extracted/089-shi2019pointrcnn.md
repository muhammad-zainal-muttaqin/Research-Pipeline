---
source_id: 089
bibtex_key: shi2019pointrcnn
title: PointRCNN: 3D Object Proposal Generation and Detection from Point Cloud
year: 2019
domain_theme: Deteksi 3D
verified_pdf: 89_PointRCNN.pdf
char_count: 79057
---

PointRCNN: 3D Object Proposal Generation and Detection from Point Cloud

                                                                        Shaoshuai Shi   Xiaogang Wang      Hongsheng Li
                                                                              The Chinese University of Hong Kong
                                                                                 {ssshi, xgwang, hsli}@ee.cuhk.edu.hk
arXiv:1812.04244v2 [cs.CV] 16 May 2019

                                                                                                                a: Aggregate View Object Detection (AVOD)
                                                                  Abstract                                      RGB image

                                                                                                                                                                                                            3D Box Predictions
                                                                                                                                                front view                      front view
                                            In this paper, we propose PointRCNN for 3D object de-                                          projection & pooling            projection & pooling
                                                                                                                        2D CNN
                                         tection from raw point cloud. The whole framework is                     3D
                                                                                                                                                                  fusion                          fusion
                                                                                                                anchors                                                    3D RoIs
                                         composed of two stages: stage-1 for the bottom-up 3D                                                   bird view                       bird view
                                         proposal generation and stage-2 for refining proposals in                                         projection & pooling            projection & pooling
                                                                                                                        2D CNN
                                         the canonical coordinates to obtain the final detection re-            Bird s view
                                                                                                                b: Frustum-Pointnet
                                         sults. Instead of generating proposals from RGB image

                                                                                                                                                                                                           3D Box Predictions
                                         or projecting point cloud to bird’s view or voxels as pre-                                                            region
                                                                                                                                                                                           3D box
                                         vious methods do, our stage-1 sub-network directly gen-                                                                 to
                                                                                                                                                                           point cloud    estimation
                                                                                                                               2D image           2D RoIs     frustum
                                         erates a small number of high-quality 3D proposals from                                detector                                   in frustum
                                         point cloud in a bottom-up manner via segmenting the point             RGB image
                                                                                                                                                             point cloud
                                         cloud of the whole scene into foreground points and back-
                                                                                                                c: Our approach (PointRCNN)
                                         ground. The stage-2 sub-network transforms the pooled                              point-wise

                                                                                                                                                                                                           3D Box Predictions
                                                                                                                                                       bottom-up 3D
                                         points of each proposal to canonical coordinates to learn                        feature vector
                                                                                                                                                    proposal generation
                                         better local spatial features, which is combined with global                                                   point cloud                     canonical 3D
                                                                                                                               point cloud             segmentation        point cloud box refinement
                                         semantic features of each point learned in stage-1 for ac-                                        ...                             RoI pooling
                                                                                                                                network
                                                                                                                                                        3D proposal
                                         curate box refinement and confidence prediction. Exten-                 Point cloud                             generation
                                         sive experiments on the 3D detection benchmark of KITTI
                                         dataset show that our proposed architecture outperforms               Figure 1. Comparison with state-of-the-art methods. Instead of
                                         state-of-the-art methods with remarkable margins by us-               generating proposals from fused feature maps of bird’s view and
                                         ing only point cloud as input. The code is available at               front view [14], or RGB images [25], our method directly gener-
                                         https://github.com/sshaoshuai/PointRCNN.                              ates 3D proposals from raw point cloud in a bottom-up manner.

                                                                                                               tection methods either leverage the mature 2D detection
                                         1. Introduction                                                       frameworks by projecting the point clouds into bird’s view
                                            Deep learning has achieved remarkable progress on 2D               [14, 42, 17] (see Fig. 1 (a)), to the frontal view [4, 38], or
                                         computer vision tasks, including object detection [8, 32, 16]         to the regular 3D voxels [34, 43], which are not optimal and
                                         and instance segmentation [6, 10, 20], etc. Beyond 2D                 suffer from information loss during the quantization.
                                         scene understanding, 3D object detection is crucial and in-               Instead of transforming point cloud to voxels or other
                                         dispensable for many real-world applications, such as au-             regular data structures for feature learning, Qi et al. [26, 28]
                                         tonomous driving and domestic robots. While recent devel-             proposed PointNet for learning 3D representations directly
                                         oped 2D detection algorithms are capable of handling large            from point cloud data for point cloud classification and seg-
                                         variations of viewpoints and background clutters in images,           mentation. As shown in Fig. 1 (b), their follow-up work [25]
                                         the detection of 3D objects with point clouds still faces great       applied PointNet in 3D object detection to estimate the 3D
                                         challenges from the irregular data format and large search            bounding boxes based on the cropped frustum point cloud
                                         space of 6 Degrees-of-Freedom (DoF) of 3D object.                     from the 2D RGB detection results. However, the perfor-
                                            In autonomous driving, the most commonly used 3D                   mance of the method heavily relies on the 2D detection per-
                                         sensors are the LiDAR sensors, which generate 3D point                formance and cannot take the advantages of 3D information
                                         clouds to capture the 3D structures of the scenes. The dif-           for generating robust bounding box proposals.
                                         ficulty of point cloud-based 3D object detection mainly lies              Unlike object detection from 2D images, 3D objects in
                                         in irregularity of the point clouds. State-of-the-art 3D de-          autonomous driving scenes are naturally and well separated

                                                                                                           1
by annotated 3D bounding boxes. In other words, the train-           [24, 15] leveraged the geometry constraints between 3D and
ing data for 3D object detection directly provides the se-           2D bounding box to recover the 3D object pose. [1, 44, 23]
mantic masks for 3D object segmentation. This is a key               exploited the similarity between 3D objects and the CAD
difference between 3D detection and 2D detection training            models. Chen et al. [2, 3] formulated the 3D geometric in-
data. In 2D object detection, the bounding boxes could only          formation of objects as an energy function to score the pre-
provide weak supervisions for semantic segmentation [5].             defined 3D boxes. These works can only generate coarse
    Based on this observation, we present a novel two-stage          3D detection results due to the lack of depth information
3D object detection framework, named PointRCNN, which                and can be substantially affected by appearance variations.
directly operates on 3D point clouds and achieves robust             3D object detection from point clouds. State-of-the-art
and accurate 3D detection performance (see Fig. 1 (c)). The          3D object detection methods proposed various ways to learn
proposed framework consists of two stages, the first stage           discriminative features from the sparse 3D point clouds.
aims at generating 3D bounding box proposal in a bottom-             [4, 14, 42, 17, 41] projected point cloud to bird’s view
up scheme. By utilizing 3D bounding boxes to generate                and utilized 2D CNN to learn the point cloud features for
ground-truth segmentation mask, the first stage segments             3D box generation. Song et al. [34] and Zhou et al. [43]
foreground points and generates a small number of bound-             grouped the points into voxels and used 3D CNN to learn
ing box proposals from the segmented points simultane-               the features of voxels to generate 3D boxes. However, the
ously. Such a strategy avoids using the large number of 3D           bird’s view projection and voxelization suffer from infor-
anchor boxes in the whole 3D space as previous methods               mation loss due to the data quantization, and the 3D CNN is
[43, 14, 4] do and saves much computation.                           both memory and computation inefficient. [25, 39] utilized
    The second stage of PointRCNN conducts canonical 3D              mature 2D detectors to generate 2D proposals from images
box refinement. After the 3D proposals are generated, a              and reduced the size of 3D points in each cropped image
point cloud region pooling operation is adopted to pool              regions. PointNet [26, 28] is then used to learn the point
learned point representations from stage-1. Unlike existing          cloud features for 3D box estimation. But the 2D image-
3D methods that directly estimate the global box coordi-             based proposal generation might fail on some challenging
nates, the pooled 3D points are transformed to the canoni-           cases that could only be well observed from 3D space. Such
cal coordinates and combined with the pooled point features          failures could not be recovered by the 3D box estimation
as well as the segmentation mask from stage-1 for learning           step. In contrast, our bottom-to-up 3D proposal generation
relative coordinate refinement. This strategy fully utilizes         method directly generates robust 3D proposals from point
all information provided by our robust stage-1 segmentation          clouds, which is both efficient and quantization free.
and proposal sub-network. To learn more effective coordi-
nate refinements, we also propose the full bin-based 3D box          Learning point cloud representations. Instead of repre-
regression loss for proposal generation and refinement, and          senting the point cloud as voxels [22, 33, 35] or multi-view
the ablation experiments show that it converges faster and           formats [27, 36, 37], Qi et al. [26] presented the PointNet
achieves higher recall than other 3D box regression loss.            architecture to directly learn point features from raw point
    Our contributions could be summarized into three-fold.           clouds, which greatly increases the speed and accuracies of
(1) We propose a novel bottom-up point cloud-based 3D                point cloud classification and segmentation. The follow-up
bounding box proposal generation algorithm, which gener-             works [28, 12] further improve the extracted feature qual-
ates a small number of high-quality 3D proposals via seg-            ity by considering the local structures in point clouds. Our
menting the point cloud into foreground objects and back-            work extends the point-based feature extractors to 3D point
ground. The learned point representation from segmenta-              cloud-based object detection, leading to a novel two-stage
tion is not only good at proposal generation but is also help-       3D detection framework, which directly generate 3D box
ful for the later box refinement. (2) The proposed canonical         proposals and detection results from raw point clouds.
3D bounding box refinement takes advantages of our high-
recall box proposals generated from stage-1 and learns to            3. PointRCNN for Point Cloud 3D Detection
predict box coordinates refinements in the canonical coor-               In this section, we present our proposed two-stage detec-
dinates with robust bin-based losses. (3) Our proposed 3D            tion framework, PointRCNN, for detecting 3D objects from
detection framework PointRCNN outperforms state-of-the-              irregular point cloud. The overall structure is illustrated in
art methods with remarkable margins and ranks first among            Fig. 2, which consists of the bottom-up 3D proposal genera-
all published works as of Nov. 16 2018 on the 3D detection           tion stage and the canonical bounding box refinement stage.
test board of KITTI by using only point clouds as input.
                                                                     3.1. Bottom-up 3D proposal generation via point
2. Related Work                                                            cloud segmentation
3D object detection from 2D images. There are exist-                    Existing 2D object detection methods could be classi-
ing works on estimating the 3D bounding box from images.             fied into one-stage and two-stage methods, where one-stage

                                                                 2
  a: Bottom-up 3D Proposal Generation
   Point cloud representation                                     Point-wise                                                                   Generate 3D proposal
         of input scene                                         feature vector                                                              from each foreground point

                                                                                   Bin-based 3D
                                                                                  Box Generation

                                    Point Cloud

                                                  Point Cloud
                                     Encoder

                                                   Decoder
                                                                     ...
                                                                                 Foreground Point
                                                                                  Segmentation

         Point Coords.            tures
                          tic Fea                          Foreground Mask
                    Seman                                                              3D RoIs
                                                                                                                                     b: Canonical 3D Box Refinement
                                                                                                                                         3D boxes of detected objects
                                 Semantic Features                         Merged Features
                                                  ...                              ...                               Bin-based 3D
                                                                                                                    Box Refinement

                                                                                                      Point Cloud
                                                                                                       Encoder
                                                                                 MLP

                                 Local Spatial Points                                                                 Confidence
                                                                              Canonical
                                                                                                                      Prediction
                                          ...                              Transformation
  Point Cloud Region Pooling

Figure 2. The PointRCNN architecture for 3D object detection from point cloud. The whole network consists of two parts: (a) for
generating 3D proposals from raw point cloud in a bottom-up manner. (b) for refining the 3D proposals in canonical coordinate.

methods [19, 21, 31, 30, 29] are generally faster but directly                                   inative point-wise features for describing the raw point
estimate object bounding boxes without refinement, while                                         clouds, we utilize the PointNet++ [28] with multi-scale
two-stage methods [10, 18, 32, 8] generate proposals firstly                                     grouping as our backbone network. There are several other
and further refine the proposals and confidences in a second                                     alternative point-cloud network structures, such as [26, 13]
stage. However, direct extension of the two-stage methods                                        or VoxelNet [43] with sparse convolutions [9], which could
from 2D to 3D is non-trivial due to the huge 3D search space                                     also be adopted as our backbone network.
and the irregular format of point clouds. AVOD [14] places                                       Foreground point segmentation. The foreground points
80-100k anchor boxes in the 3D space and pool features for                                       provide rich information on predicting their associated ob-
each anchor in multiple views for generating proposals. F-                                       jects’ locations and orientations. By learning to segment the
PointNet [25] generates 2D proposals from 2D images, and                                         foreground points, the point-cloud network is forced to cap-
estimate 3D boxes based on the 3D points cropped from the                                        ture contextual information for making accurate point-wise
2D regions, which might miss difficult objects that could                                        prediction, which is also beneficial for 3D box generation.
only be clearly observed from 3D space.                                                          We design the bottom-up 3D proposal generation method
   We propose an accurate and robust 3D proposal genera-                                         to generate 3D box proposals directly from the foreground
tion algorithm as our stage-1 sub-network based on whole-                                        points, i.e., the foreground segmentation and 3D box pro-
scene point cloud segmentation. We observe that objects in                                       posal generation are performed simultaneously.
3D scenes are naturally separated without overlapping each                                          Given the point-wise features encoded by the backbone
other. All 3D objects’ segmentation masks could be directly                                      point cloud network, we append one segmentation head
obtained by their 3D bounding box annotations, i.e., 3D                                          for estimating the foreground mask and one box regression
points inside 3D boxes are considered as foreground points.                                      head for generating 3D proposals. For point segmentation,
   We therefore propose to generate 3D proposals in a                                            the ground-truth segmentation mask is naturally provided
bottom-up manner. Specifically, we learn point-wise fea-                                         by the 3D ground-truth boxes. The number of foreground
tures to segment the raw point cloud and to generate 3D                                          points is generally much smaller than that of the background
proposals from the segmented foreground points simultane-                                        points for a large-scale outdoor scene. Thus we use the fo-
ously. Based on this bottom-up strategy, our method avoids                                       cal loss [19] to handle the class imbalance problem as
using a large set of predefined 3D boxes in the 3D space                                                   Lfocal (pt ) = −αt (1 − pt )γ log(pt ),         (1)
and significantly constrains the search space for 3D pro-                                                                 (
posal generation. The experiments show that our proposed                                                                    p      for forground point
                                                                                                           where pt =
3D box proposal method achieves significantly higher recall                                                                 1 − p otherwise
than 3D anchor-based proposal generation methods.                                                During training point cloud segmentation, we keep the de-
Learning point cloud representations. To learn discrim-                                          fault settings αt = 0.25 and γ = 2 as the original paper.

                                                                                          3
Bin-based 3D bounding box generation. As we men-
tioned above, a box regression head is also appended for si-
multaneously generating bottom-up 3D proposals with the
foreground point segmentation. During training, we only
require the box regression head to regress 3D bounding box
locations from foreground points. Note that although boxes
are not regressed from the background points, those points
also provide supporting information for generating boxes
because of the receptive field of the point-cloud network.
    A 3D bounding box is represented as (x, y, z, h, w, l, θ)
in the LiDAR coordinate system, where (x, y, z) is the ob-
ject center location, (h, w, l) is the object size, and θ is the
object orientation from the bird’s view. To constrain the                   Figure 3. Illustration of bin-based localization. The surrounding
generated 3D box proposals, we propose bin-based regres-                    area along X and Z axes of each foreground point is split into a
                                                                            series of bins to locate the object center.
sion losses for estimating 3D bounding boxes of objects.
    For estimating center location of an object, as shown in                   In the inference stage, for the bin-based predicted param-
Fig. 3, we split the surrounding area of each foreground                    eters, x, z, θ, we first choose the bin center with the high-
point into a series of discrete bins along the X and Z axes.                est predicted confidence and add the predicted residual to
Specifically, we set a search range S for each X and Z axis                 obtain the refined parameters. For other directly regressed
of the current foreground point, and each 1D search range is                parameters, including y, h, w, and l, we add the predicted
divided into bins of uniform length δ to represent different                residual to their initial values.
object centers (x, z) on the X-Z plane. We observe that us-                    The overall 3D bounding box regression loss Lreg with
ing bin-based classification with cross-entropy loss for the                different loss terms for training could then be formulated as
X and Z axes instead of direct regression with smooth L1                      (p)
                                                                                       X                  (p)                 (p)
                                                                            Lbin =                    c u , bin(p)
                                                                                               (Fcls (bin                  resu , res(p)
                                                                                                               u ) + Freg (c         u )),
loss results in more accurate and robust center localization.
                                                                                     u∈{x,z,θ}
    The localization loss for the X or Z axis consists of two
                                                                                                           (p)
                                                                                        X
terms, one term for bin classification along each X and Z                   L(p)
                                                                             res =                       resv , res(p)
                                                                                                   Freg (c         v ),                    (3)
axis, and the other term for residual regression within the                          v∈{y,h,w,l}
classified bin. For the center location y along the vertical Y                        1 X  (p)             
axis, we directly utilize smooth L1 loss for the regression                 Lreg =              Lbin + L(p)
                                                                                                        res
                                                                                     Npos p∈pos
since most objects’ y values are within a very small range.                                                                          (p)
Using the L1 loss is enough for obtaining accurate y values.                where Npos is the number of foreground points, binc u and
    The localization targets could therefore be formulated as                  (p)
                                                                            rc
                                                                             esu are the predicted bin assignments and residuals of the
                                                                                                                 (p)
               p
                x − x(p) + S
                                             p
                                               z − z (p) + S
                                                                           foreground point p, binu(p) and resu are the ground-truth
       (p)                             (p)
    binx =                       , binz =                       ,           targets calculated as above, Fcls denotes the cross-entropy
                      δ                                δ
                                                                        classification loss, and Freg denotes the smooth L1 loss.
              1                                      δ                          To remove the redundant proposals, we conduct non-
   res(p)
      u    =       up − u(p) + S − bin(p)  u ·δ+          , (2)
  u∈{x,z}     C                                      2                      maximum suppression (NMS) based on the oriented IoU
                                                                            from bird’s view to generate a small number of high-quality
   res(p) p
      y =y −y
              (p)
                                                                            proposals. For training, we use 0.85 as the bird’s view IoU
where (x(p) , y (p) , z (p) ) is the coordinates of a foreground            threshold and after NMS we keep top 300 proposals for
point of interest, (xp , y p , z p ) is the center coordinates of its       training the stage-2 sub-network. For inference, we use ori-
corresponding object , bin(p)                (p)                            ented NMS with IoU threshold 0.8, and only top 100 pro-
                                x and binz are ground-truth bin
                                               (p)       (p)                posals are kept for the refinement of stage-2 sub-network.
assignments along X and Z axis, resx and resz are the
ground-truth residual for further location refinement within                3.2. Point cloud region pooling
the assigned bin, and C is the bin length for normalization.
                                                                                 After obtaining 3D bounding box proposals, we aim at
   The targets of orientation θ and size (h, w, l) estimation
                                                                            refining the box locations and orientations based on the pre-
are similar to those in [25]. We divide the orientation 2π
                                                                 (p)        viously generated box proposals. To learn more specific lo-
into n bins, and calculate the bin classification target binθ               cal features of each proposal, we propose to pool 3D points
                                         (p)
and residual regression target resθ in the same way as x or                 and their corresponding point features from stage-1 accord-
z prediction. The object size (h, w, l) is directly regressed               ing to the location of each 3D proposal.
                                  (p)     (p)      (p)
by calculating residual (resh , resw , resl ) w.r.t. the aver-                   For each 3D box proposal, bi = (xi , yi , zi , hi , wi ,
age object size of each class in the entire training set.                   li , θi ), we slightly enlarge it to create a new 3D box

                                                                        4
             CCS-4             CCS-3                                 Z
                                                                                 Feature learning for box proposal refinement. As we
                                          Canonical Coordinate
                                               System 2                  X
                                                                                 mentioned in Sec. 3.2, the refinement sub-network com-
 CCS-5                                                                           bines both the transformed local spatial points (features) p̃
                                                                 Y
                          CCS-2
                                             Canonical                           as well as their global semantic features f (p) from stage-1
                                          Transformation
                                                                     Z
                   Z
                                                                                 for further box and confidence refinement.
                                          Canonical Coordinate
                                               System 5
                                                                                     Although the canonical transformation enables robust lo-
     CCS-1                  X
                       LiDAR Coordinate
                                                                         X       cal spatial features learning, it inevitably loses depth infor-
                           System                                Y
               Y
                                                                                 mation of each object. For instance, the far-away objects
                                                                                 generally have much fewer points than nearby objects be-
Figure 4. Illustration of canonical transformation. The pooled                   cause of the fixed angular scanning resolution of the Li-
points belonged to each proposal are transformed to the corre-
                                                                                 DAR sensors. To compensate for the lost depth informa-
sponding canonical coordinate system for better local spatial fea-                                                                             (p)
ture learning, where CCS denotes Canonical Coordinate System.                    p we include the distance to the sensor, i.e., d
                                                                                 tion,                                                              =
                                                                                        (p)  2         (p)  2         (p) 2
                                                                                    (x ) + (y ) + (z ) , into the features of point p.
bei = (xi , yi , zi , hi + η, wi + η, li + η, θi ) to encode the                     For each proposal, its associated points’ local spatial fea-
additional information from its context, where η is a con-                       tures p̃ and the extra features [r(p) , m(p) , d(p) ] are first con-
stant value for enlarging the size of box.                                       catenated and fed to several fully-connected layers to en-
   For each point p = (x(p) , y (p) , z (p) ), an inside/outside                 code their local features to the same dimension of the global
test is performed to determine whether the point p is inside                     features f (p) . Then the local features and global features are
the enlarged bounding box proposal bei . If so, the point                        concatenated and fed into a network following the structure
and its features would be kept for refining the box bi . The                     of [28] to obtain a discriminative feature vector for the fol-
features associated with the inside point p include its 3D                       lowing confidence classification and box refinement.
point coordinates (x(p) , y (p) , z (p) ) ∈ R3 , its laser reflection            Losses for box proposal refinement. We adopt the sim-
intensity r(p) ∈ R, its predicted segmentation mask m(p) ∈                       ilar bin-based regression losses for proposal refinement.
{0, 1} from stage-1, and the C-dimensional learned point                         A ground-truth box is assigned to a 3D box proposal for
feature representation f (p) ∈ RC from stage-1.                                  learning box refinement if their 3D IoU is greater than
   We include the segmentation mask m(p) to differentiate                        0.55. Both the 3D proposals and their corresponding 3D
the predicted foreground/background points within the en-                        ground-truth boxes are transformed into the canonical co-
larged box bei . The learned point feature f (p) encodes valu-                   ordinate systems, which means the 3D proposal bi =
able information via learning for segmentation and proposal                      (xi , yi , zi , hi , wi , li , θi ) and 3D ground-truth box bgti =
generation therefore are also included. We eliminate the                         (xgt     gt gt       gt    gt gt gt
                                                                                    i , yi , zi , hi , wi , li , θi ) would be transformed to
proposals that have no inside points in the following stage.                        b̃i = (0, 0, 0, hi , wi , li , 0),                             (4)
3.3. Canonical 3D bounding box refinement                                          b̃gt    gt        gt        gt        gt   gt gt gt
                                                                                     i = (xi − xi , yi − yi , zi − zi , hi , wi , li , θi − θi )

   As illustrated in Fig. 2 (b), the pooled points and their                        The training targets for the ith box proposal’s center lo-
associated features (see Sec. 3.2) for each proposal are fed                     cation, (bini∆x , bini∆z , resi∆x , resi∆z , resi∆y ), are set in the
to our stage-2 sub-network for refining the 3D box locations                     same way as Eq. (2) except that we use smaller search range
as well as the foreground object confidence.                                     S for refining the locations of 3D proposals. We still di-
Canonical transformation. To take advantages of our                              rectly regress size residual (resi∆h , resi∆w , resi∆l ) w.r.t. the
high-recall box proposals from stage-1 and to estimate only                      average object size of each class in the training set since
the residuals of the box parameters of proposals, we trans-                      the pooled sparse points usually could not provide enough
form the pooled points belonging to each proposal to the                         information of the proposal size (hi , wi , li ).
canonical coordinate system of the corresponding 3D pro-                            For refining the orientation, we assume that the angular
posal. As shown in Fig. 4, the canonical coordinate sys-                         difference w.r.t. the ground-truth orientation, θigt − θi , is
tem for one 3D proposal denotes that (1) the origin is lo-                       within the range [− π4 , π4 ], based on the fact that the 3D IoU
cated at the center of the box proposal; (2) the local X 0                       between a proposal and their ground-truth box is at least
and Z 0 axes are approximately parallel to the ground plane                      0.55. Therefore, we divide π2 into discrete bins with the bin
with X 0 pointing towards the head direction of proposal and                     size ω and predict the bin-based orientation targets as
                                                                                                $ gt               %
the other Z 0 axis perpendicular to X 0 ; (3) the Y 0 axis re-                             i       θi − θi + π4
mains the same as that of the LiDAR coordinate system.                                 bin∆θ =                        ,                            (5)
                                                                                                          ω
All pooled points’ coordinates p of the box proposal should
                                                                                                 2  gt             π                     ω 
be transformed to the canonical coordinate system as p̃ by                             resi∆θ =       θi − θi + − bini∆θ · ω +
proper rotation and translation. Using the proposed canon-                                       ω                  4                       2
ical coordinate system enables the box refinement stage to                       Therefore, the overall loss for the stage-2 sub-network can
learn better local spatial features for each proposal.                           be formulated as

                                                                             5
                                                                       side of object for robust segmentation since the 3D ground-
                      1 X                                              truth boxes may have small variations. For the bin-based
          Lrefine =           Fcls (probi , labeli )
                    ||B||                                              proposal generation, the hyper parameters are set as search
                          i∈B
                                                             (6)       range S = 3m, bin size δ = 0.5m and orientation bin num-
                           1     X         (i)
                    +                  (L̃bin + L̃(i)res )             ber n = 12.
                       ||Bpos ||
                                  i∈Bpos                                   To train the stage-2 sub-network, we randomly augment
where B is the set of 3D proposals from stage-1 and Bpos               the 3D proposals with small variations to increase the diver-
stores the positive proposals for regression, probi is the es-         sity of proposals. For training the box classification head,
                                                                       a proposal is considered as positive if its maximum 3D IoU
timated confidence of b̃i and labeli is the corresponding la-
                                                                       with ground-truth boxes is above 0.6, and is treated as neg-
bel, Fcls is the cross entropy loss to supervise the predicted
                (i)      (i)                (p)      (p)               ative if its maximum 3D IoU is below 0.45. We use 3D IoU
confidence, L̃bin and L̃res are similar to Lbin and Lres in Eq.        0.55 as the minimum threshold of proposals for the training
(3) with the new targets calculated by b̃i and b̃gt
                                                  i as above.          of box regression head. For the bin-based proposal refine-
   We finally apply oriented NMS with bird’s view IoU                  ment, search range is S = 1.5m, localization bin size is
threshold 0.01 to remove the overlapping bounding boxes                δ = 0.5m and orientation bin size is ω = 10◦ . The context
and generate the 3D bounding boxes for detected objects.               length of point cloud pooling is η = 1.0m.
                                                                           The two stage sub-networks of PointRCNN are trained
4. Experiments                                                         separately. The stage-1 sub-network is trained for 200
                                                                       epochs with batch size 16 and learning rate 0.002, while
   PointRCNN is evaluated on the challenging 3D object
                                                                       the stage-2 sub-network is trained for 50 epochs with batch
detection benchmark of KITTI dataset [7]. We first intro-
                                                                       size 256 and learning rate 0.002. During training, we con-
duce the implementation details of PointRCNN in Sec. 4.1.
                                                                       duct data augmentation of random flip, scaling with a scale
In Sec. 4.2, we perform a comparison with state-of-the-art
                                                                       factor sampled from [0.95, 1.05] and rotation around ver-
3D detection methods. Finally, we conduct extensive abla-
                                                                       tical Y axis between [-10, 10] degrees. Inspired by [40],
tion studies to analyze PointRCNN in Sec. 4.3.
                                                                       to simulate objects with various environments, we also put
4.1. Implementation Details                                            several new ground-truth boxes and their inside points from
                                                                       other scenes to the same locations of current training scene
Network Architecture. For each 3D point-cloud scene                    by randomly selecting non-overlapping boxes, and this aug-
in the training set, we subsample 16,384 points from each              mentation is denoted as GT-AUG in the following sections.
scene as the inputs. For scenes with the number of points
fewer than 16,384, we randomly repeat the points to obtain             4.2. 3D Object Detection on KITTI
16,384 points. For the stage-1 sub-network, we follow the                  The 3D object detection benchmark of KITTI contains
network structure of [28], where four set-abstraction layers           7481 training samples and 7518 testing samples (test split).
with multi-scale grouping are used to subsample points into            We follow the frequently used train/val split mentioned in
groups with sizes 4096, 1024, 256, 64. Four feature prop-              [4] to divide the training samples into train split (3712 sam-
agation layers are then used to obtain the per-point feature           ples) and val split (3769 samples). We compare PointR-
vectors for segmentation and proposal generation.                      CNN with state-of-the-art methods of 3D object detection
   For the box proposal refinement sub-network, we ran-                on both val split and test split of KITTI dataset. All the
domly sample 512 points from the pooled region of each                 models are trained on train split and evaluated on test split
proposal as the input of the refinement sub-network. Three             and val split.
set abstraction layers with single-scale grouping [28] (with           Evaluation of 3D object detection. We evaluate our
group sizes 128, 32, 1) are used to generate a single fea-             method on the 3D detection benchmark of the KITTI test
ture vector for object confidence classification and proposal          server, and the results are shown in Tab. 1. For the 3D
location refinement.                                                   detection of car and cyclist, our method outperforms pre-
The training scheme. Here we report the training details               vious state-of-the-art methods with remarkable margins on
of car category since it has the majority of samples in the            all three difficulties and ranks first on the KITTI test board
KITTI dataset, and the proposed method could be extended               among all published works at the time of submission. Al-
to other categories (like pedestrian and cyclist) easily with          though most of the previous methods use both RGB image
little modifications of hyper parameters.                              and point cloud as input, our method achieves better perfor-
    For stage-1 sub-network, all points inside the 3D ground-          mance with an efficient architecture by using only the point
truth boxes are considered as foreground points and others             cloud as input. For the pedestrian detection, compared with
points are treated as background points. During training,              previous LiDAR-only methods, our method achieves better
we ignore background points near the object boundaries                 or comparable results, but it performs slightly worse than
by enlarging the 3D ground-truth boxes by 0.2m on each                 the methods with multiple sensors. We consider it is due

                                                                   6
                                                       Car (IoU=0.7)              Pedestrian (IoU=0.5)                Cyclist (IoU=0.5)
          Method                Modality
                                                Easy     Moderate Hard          Easy Moderate Hard                Easy Moderate Hard
        MV3D [4]             RGB + LiDAR       71.09      62.35        55.12     -           -           -         -           -           -
  UberATG-ContFuse [17]      RGB + LiDAR       82.54      66.22        64.04     -           -           -         -           -           -
     AVOD-FPN [14]           RGB + LiDAR       81.94      71.88        66.38   50.80       42.81       40.88     64.00       52.18       46.61
      F-PointNet [25]        RGB + LiDAR       81.20      70.39        62.19   51.21       44.89       40.23     71.96       56.77       50.39
       VoxelNet [43]           LiDAR           77.47      65.11        57.73   39.48       33.69       31.51     61.22       48.36       44.37
      SECOND [40]              LiDAR           83.13      73.66        66.20   51.07       42.56       37.29     70.51       53.85       46.90
           Ours                LiDAR           85.94      75.76        68.32   49.43       41.78       38.63     73.93       59.60       53.59

Table 1. Performance comparison of 3D object detection with previous methods on KITTI test split by submitting to official test server.
The evaluation metric is Average Precision(AP) with IoU threshold 0.7 for car and 0.5 for pedestrian/cyclist.

                                     AP(IoU=0.7)                                             Recall(IoU=0.5)             Recall(IoU=0.7)
             Method                                                            RoIs #
                             Easy     Moderate Hard                                      MV3D AVOD Ours                       Ours
           MV3D [4]          71.29      62.68    56.56                          10         -       86.00   86.66              29.87
         VoxelNet [43]       81.98      65.46    62.85                          20         -         -     91.83              32.55
         SECOND [40]         87.43      76.48    69.10                          30         -         -     93.31              32.76
        AVOD-FPN [14]        84.41      74.44    68.65                          40         -         -     95.55              40.04
        F-PointNet [25]      83.76      70.92    63.65                          50         -       91.00   96.01              40.28
                                                                                100        -         -     96.79              74.81
       Ours (no GT-AUG)      88.45      77.67    76.30
                                                                                200        -         -     98.03              76.29
              Ours           88.88      78.63    77.38
                                                                                300      91.00       -     98.21              82.29
Table 2. Performance comparison of 3D object detection with pre-
                                                                        Table 3. Recall of proposal generation network with different num-
vious methods on the car class of KITTI val split set.
                                                                        ber of RoIs and 3D IoU threshold for the car class on the val split
to the fact that our method only uses sparse point cloud as             at moderate difficulty. Note that only MV3D [4] and AVOD [14]
                                                                        of previous methods reported the number of recall.
input but pedestrians have small size and image could cap-
ture more details of pedestrians than point cloud to help 3D
                                                                        the outstanding recall still suggests the robustness and ac-
detection.
                                                                        curacy of our bottom-up proposal generation network.
   For the most important car category, we also report the
performance of 3D detection result on the val split as shown            4.3. Ablation Study
in Tab. 2. Our method outperforms previous stage-of-the-art
                                                                            In this section, we conduct extensive ablation experi-
methods with large margins on the val split. Especially in
                                                                        ments to analyze the effectiveness of different components
the hard difficulty, our method has 8.28% AP improvement
                                                                        of PointRCNN. All experiments are trained on the train split
than the previous best AP, which demonstrates the effective-
                                                                        without GT-AUG and evaluated on the val split with the car
ness of the proposed PointRCNN.
                                                                        class1 .
Evaluation of 3D proposal generation. The perfor-
mance of our bottom-up proposal generation network is                   Different inputs for the refinement sub-network. As
evaluated by calculating the recall of 3D bounding box with             mentioned in Sec. 3.3, the inputs of the refinement sub-
various number of proposals and 3D IoU threshold. As                    network consist of the canonically transformed coordinates
shown in Tab. 3, our method (without GT-AUG) achieved                   and pooled features of each pooled point.
significantly higher recall than previous methods. With                     We analyze the effects of each type of features to the
only 50 proposals, our method obtains 96.01% recall at IoU              refinement sub-network by removing one and keeping all
threshold 0.5 on the moderate difficulty of car class, which            other parts unchanged. All experiments share the same
outperforms recall 91% of AVOD [14] by 5.01% at the same                fixed stage-1 sub-network for fair comparison. The results
number of proposals, note that the latter method uses both              are shown in Tab. 4. Without the proposed canonical trans-
2D image and point cloud for proposal generation while we               formation, the performance of the refinement sub-network
only use point cloud as input. When using 300 proposals,                dropped significantly, which shows the transformation into
our method further achieves 98.21% recall at IoU threshold              a canonical coordinate system greatly eliminates much ro-
0.5. It is meaningless to increase the number of proposals              tation and location variations and improve the efficiency of
since our method already obtained high recall at IoU thresh-            feature learning for the stage-2. We also see that remov-
old 0.5. In contrast, as shown in Tab. 3, we report the recall          ing the stage-1 features f (p) learned from point cloud seg-
of 3D bounding box at IoU threshold 0.7 for reference. With             mentation and proposal generation decreases the mAP by
300 proposals, our method achieves 82.29% recall at IoU                 2.71% on the moderate difficulty, which demonstrates the
threshold 0.7. Although the recall of proposals are loosely                1 The KITTI test server only allows 3 submissions in every 30 days. All

[11, 8] related to the final 3D object detection performance,           previous methods conducted ablation studies on the validation set.

                                                                   7
           RPN       camera     seg.                                             1.0
  CT                                     APE       APM      APH
         features     depth     mask
   ×        X          X         X       7.64      13.68    13.94                0.8
   X        ×          X         X       84.75     74.96    74.29
   X        X          ×         X       87.34     76.79    75.46
   X        X          X         ×       86.25     76.64    75.86                0.6

                                                                            recall
   X        X          X         X       88.45     77.67    76.30
                                                                                                                              RB-Loss(iou=0.5)
Table 4. Performance for different input combinations of refine-                 0.4                                          RCB-Loss(iou=0.5)
                                                                                                                              CN-loss(iou=0.5)
ment network. APE , APM , APH denote the average precision                                                                    PBB-loss(iou=0.5)
                                                                                                                              BB-loss(iou=0.5)
for easy, moderate, hard difficulty on KITTI val split, respectively.            0.2                                          RB-Loss(iou=0.7)
                                                                                                                              RCB-Loss(iou=0.7)
CT denotes canonical transformation.                                                                                          CN-loss(iou=0.7)
                                                                                                                              PBB-loss(iou=0.7)
                                                                                                                              BB-loss(iou=0.7)
           η (context width)    APE       APM      APH                           0.00   20   40    60    80 100 120 140 160 180 200
               no context       86.65     75.68    68.92                                                   epochs
                 0.5m           87.87     77.12    75.61
                 0.8m           88.27     77.40    76.07                     Figure 5. Recall curves of applying different bounding box regres-
                 1.0m           88.45     77.67    76.30                     sion loss function.
                 1.5m           86.82     76.87    75.88
                 2.0m           86.47     76.61    75.53                        The final recall (IoU thresholds 0.5 and 0.7) with 100
                                                                             proposals from stage-1 are used as the evaluation metric,
Table 5. Performance of adopting different context width η of                which are shown in Fig. 5. The plot reveals the effective-
context-aware point cloud pooling.                                           ness of our full bin-based 3D bounding box regression loss.
                                                                             Specifically, stage-1 sub-network with our full bin-based
advantages of learning for semantic segmentation in the first                loss function achieves higher recall and converges much
stage. Tab. 4 also shows that the camera depth information                   faster than all other loss functions, which benefits from con-
d(p) and segmentation mask m(p) for 3D points p contribute                   straining the targets, especially the localization, with prior
slightly to the final performance, since the camera depth                    knowledge. The partial-bin-based loss achieves similar re-
completes the distance information which is eliminated dur-                  call but the convergence speed is much slower than ours.
ing the canonical transformation and the segmentation mask                   Both full and partial bin-based loss have significantly higher
indicates the foreground points in the pooled regions.                       recall than other loss functions, especially at IoU threshold
Context-aware point cloud pooling. In Sec. 3.2, we in-                       0.7. The improved residual-cos-based loss also obtains bet-
troduce enlarging the proposal boxes bi by a margin η to                     ter recall than residual-based loss by improving the angle
create bei to pool more contextual points for each proposal’s                regression targets.
confidence estimation and location regression. Tab. 5 shows
the effects of different pooled context widths η. η = 1.0m                   4.4. Qualitative Results
results in the best performance in our proposed framework.
                                                                                Fig. 6 shows some qualitative results of our proposed
We notice that when no contextual information is pooled,
                                                                             PointRCNN on the test split of KITTI [7] dataset. Note that
the accuracies, especially those at the hard difficulty, drops
                                                                             the image is just for better visualization and our PointR-
significantly. The difficult cases often have fewer points in
                                                                             CNN takes only the point cloud as input to generation 3D
the proposals since the object might be occluded or far away
                                                                             detection results.
from the sensor, which needs more context information for
classification and proposal refinement. As shown in Tab. 5,
too large η also leads to performance drops since the pooled                 5. Conclusion
region of current proposals may include noisy foreground                        We have presented PointRCNN, a novel 3D object de-
points of other objects.                                                     tector for detecting 3D objects from raw point cloud. The
Losses of 3D bounding box regression.            In Sec. 3.1,                proposed stage-1 network directly generates 3D proposals
we propose the bin-based localization losses for generat-                    from point cloud in a bottom-up manner, which achieves
ing 3D box proposals. In this part, we evaluate the per-                     significantly higher recall than previous proposal generation
formances when using different types of 3D box regres-                       methods. The stage-2 network refines the proposals in the
sion loss for our stage-1 sub-network, which include the                     canonical coordinate by combining semantic features and
residual-based loss (RB-loss) [43], residual-cos-based loss                  local spatial features. Moreover, the newly proposed bin-
(RCB-loss), corner loss (CN-loss) [4, 14], partial-bin-based                 based loss has demonstrated its efficiency and effectiveness
loss (PBB-loss) [25], and our full bin-based loss (BB-loss).                 for 3D bounding box regression. The experiments show that
Here the residual-cos-based loss encodes ∆θ of residual-                     PointRCNN outperforms previous state-of-the-art methods
based loss by (cos(∆θ), sin(∆θ)) to eliminate the ambigu-                    with remarkable margins on the challenging 3D detection
ity of angle regression.                                                     benchmark of KITTI dataset.

                                                                        8
Figure 6. Qualitative results of PointRCNN on the KITTI test split. For each sample, the upper part is the image and the lower part is a
representative view of the corresponding point cloud. The detected objects are shown with green 3D bounding boxes, and the orientation
(driving direction) of each object is specified by a X in the upper part and a red tube in the lower part. (Best viewed with zoom-in.)

Acknowledgment                                                               national Conference on Computer Vision, pages 1635–1643,
                                                                             2015.
   This work is supported in part by SenseTime Group                     [6] Jifeng Dai, Kaiming He, and Jian Sun. Instance-aware se-
Limited, in part by the General Research Fund through                        mantic segmentation via multi-task network cascades. In
the Research Grants Council of Hong Kong under Grants                        Proceedings of the IEEE Conference on Computer Vision
CUHK14202217, CUHK14203118, CUHK14205615,                                    and Pattern Recognition, pages 3150–3158, 2016.
CUHK14207814, CUHK14213616, CUHK14208417,                                [7] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we
CUHK14239816, and in part by CUHK Direct Grant.                              ready for autonomous driving? the kitti vision benchmark
                                                                             suite. In Conference on Computer Vision and Pattern Recog-
References                                                                   nition (CVPR), 2012.
                                                                         [8] Ross Girshick. Fast r-cnn. In Proceedings of the IEEE inter-
 [1] Florian Chabot, Mohamed Chaouch, Jaonary Rabarisoa,                     national conference on computer vision, pages 1440–1448,
     Céline Teulière, and Thierry Chateau. Deep manta: A                   2015.
     coarse-to-fine many-task network for joint 2d and 3d vehicle        [9] Benjamin Graham, Martin Engelcke, and Laurens van der
     analysis from monocular image. In Proc. IEEE Conf. Com-                 Maaten. 3d semantic segmentation with submanifold sparse
     put. Vis. Pattern Recognit.(CVPR), pages 2040–2049, 2017.               convolutional networks. CVPR, 2018.
 [2] Xiaozhi Chen, Kaustav Kundu, Ziyu Zhang, Huimin Ma,                [10] Kaiming He, Georgia Gkioxari, Piotr Dollár, and Ross Gir-
     Sanja Fidler, and Raquel Urtasun. Monocular 3d object de-               shick. Mask r-cnn. In Computer Vision (ICCV), 2017 IEEE
     tection for autonomous driving. In Proceedings of the IEEE              International Conference on, pages 2980–2988. IEEE, 2017.
     Conference on Computer Vision and Pattern Recognition,             [11] Jan Hosang, Rodrigo Benenson, Piotr Dollár, and Bernt
     pages 2147–2156, 2016.                                                  Schiele. What makes for effective detection proposals? IEEE
 [3] Xiaozhi Chen, Kaustav Kundu, Yukun Zhu, Andrew G                        transactions on pattern analysis and machine intelligence,
     Berneshawi, Huimin Ma, Sanja Fidler, and Raquel Urtasun.                38(4):814–830, 2016.
     3d object proposals for accurate object class detection. In        [12] Qiangui Huang, Weiyue Wang, and Ulrich Neumann. Re-
     Advances in Neural Information Processing Systems, pages                current slice networks for 3d segmentation of point clouds.
     424–432, 2015.                                                          In Proceedings of the IEEE Conference on Computer Vision
 [4] Xiaozhi Chen, Huimin Ma, Ji Wan, Bo Li, and Tian Xia.                   and Pattern Recognition, pages 2626–2635, 2018.
     Multi-view 3d object detection network for autonomous              [13] Mingyang Jiang, Yiran Wu, and Cewu Lu. Pointsift: A sift-
     driving. In Proceedings of the IEEE Conference on Com-                  like network module for 3d point cloud semantic segmenta-
     puter Vision and Pattern Recognition, pages 1907–1915,                  tion. CoRR, abs/1807.00652, 2018.
     2017.                                                              [14] Jason Ku, Melissa Mozifian, Jungwook Lee, Ali Harakeh,
 [5] Jifeng Dai, Kaiming He, and Jian Sun. Boxsup: Exploit-                  and Steven Lake Waslander. Joint 3d proposal genera-
     ing bounding boxes to supervise convolutional networks for              tion and object detection from view aggregation. CoRR,
     semantic segmentation. In Proceedings of the IEEE Inter-                abs/1712.02294, 2017.

                                                                    9
[15] Buyu Li, Wanli Ouyang, Lu Sheng, Xingyu Zeng, and Xiao-                   tection. In Proceedings of the IEEE conference on computer
     gang Wang. Gs3d: An efficient 3d object detection frame-                  vision and pattern recognition, pages 779–788, 2016.
     work for autonomous driving. 2019.                                   [30] Joseph Redmon and Ali Farhadi. Yolo9000: better, faster,
[16] Hongyang Li, Bo Dai, Shaoshuai Shi, Wanli Ouyang, and                     stronger. In Proceedings of the IEEE conference on computer
     Xiaogang Wang. Feature Intertwiner for Object Detection.                  vision and pattern recognition, pages 7263–7271, 2017.
     In ICLR, 2019.                                                       [31] Joseph Redmon and Ali Farhadi. Yolov3: An incremental
[17] Ming Liang, Bin Yang, Shenlong Wang, and Raquel Urtasun.                  improvement. CoRR, abs/1804.02767, 2018.
     Deep continuous fusion for multi-sensor 3d object detection.         [32] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.
     In Proceedings of the European Conference on Computer Vi-                 Faster r-cnn: Towards real-time object detection with region
     sion (ECCV), pages 641–656, 2018.                                         proposal networks. In Advances in neural information pro-
[18] Tsung-Yi Lin, Piotr Dollár, Ross Girshick, Kaiming He,                   cessing systems, pages 91–99, 2015.
     Bharath Hariharan, and Serge Belongie. Feature pyramid               [33] Gernot Riegler, Ali Osman Ulusoy, and Andreas Geiger.
     networks for object detection. In Proceedings of the IEEE                 Octnet: Learning deep 3d representations at high resolutions.
     Conference on Computer Vision and Pattern Recognition,                    In Proceedings of the IEEE Conference on Computer Vision
     pages 2117–2125, 2017.                                                    and Pattern Recognition, volume 3, 2017.
[19] Tsung-Yi Lin, Priyal Goyal, Ross Girshick, Kaiming He, and           [34] Shuran Song and Jianxiong Xiao. Deep sliding shapes for
     Piotr Dollár. Focal loss for dense object detection. IEEE                amodal 3d object detection in rgb-d images. In Proceed-
     transactions on pattern analysis and machine intelligence,                ings of the IEEE Conference on Computer Vision and Pattern
     2018.                                                                     Recognition, pages 808–816, 2016.
[20] Shu Liu, Jiaya Jia, Sanja Fidler, and Raquel Urtasun. Sgn:           [35] Shuran Song, Fisher Yu, Andy Zeng, Angel X Chang, Mano-
     Sequential grouping networks for instance segmentation. In                lis Savva, and Thomas Funkhouser. Semantic scene comple-
     The IEEE International Conference on Computer Vision                      tion from a single depth image. In Computer Vision and Pat-
     (ICCV), 2017.                                                             tern Recognition (CVPR), 2017 IEEE Conference on, pages
[21] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian                      190–198. IEEE, 2017.
     Szegedy, Scott Reed, Cheng-Yang Fu, and Alexander C                  [36] Hang Su, Subhransu Maji, Evangelos Kalogerakis, and Erik
     Berg. Ssd: Single shot multibox detector. In European con-                Learned-Miller. Multi-view convolutional neural networks
     ference on computer vision, pages 21–37. Springer, 2016.                  for 3d shape recognition. In Proceedings of the IEEE in-
[22] Daniel Maturana and Sebastian Scherer. Voxnet: A 3d con-                  ternational conference on computer vision, pages 945–953,
     volutional neural network for real-time object recognition.               2015.
     In Intelligent Robots and Systems (IROS), 2015 IEEE/RSJ              [37] Hao Su, Fan Wang, Eric Yi, and Leonidas J Guibas. 3d-
     International Conference on, pages 922–928. IEEE, 2015.                   assisted feature synthesis for novel views of an object. In
[23] Roozbeh Mottaghi, Yu Xiang, and Silvio Savarese. A coarse-                Proceedings of the IEEE International Conference on Com-
     to-fine model for 3d pose estimation and sub-category recog-              puter Vision, pages 2677–2685, 2015.
     nition. In Proceedings of the IEEE Conference on Computer            [38] Bin Xu and Zhenzhong Chen. Multi-level fusion based 3d
     Vision and Pattern Recognition, pages 418–426, 2015.                      object detection from monocular images. In Proceedings
                                                                               of the IEEE Conference on Computer Vision and Pattern
[24] Arsalan Mousavian, Dragomir Anguelov, John Flynn, and
                                                                               Recognition, pages 2345–2353, 2018.
     Jana Košecká. 3d bounding box estimation using deep learn-
     ing and geometry. In Computer Vision and Pattern Recogni-            [39] Danfei Xu, Dragomir Anguelov, and Ashesh Jain. Pointfu-
     tion (CVPR), 2017 IEEE Conference on, pages 5632–5640.                    sion: Deep sensor fusion for 3d bounding box estimation.
     IEEE, 2017.                                                               CoRR, abs/1711.10871, 2017.
                                                                          [40] Yan Yan, Yuxing Mao, and Bo Li. Second: Sparsely embed-
[25] Charles Ruizhongtai Qi, Wei Liu, Chenxia Wu, Hao Su, and
                                                                               ded convolutional detection. Sensors, 18(10):3337, 2018.
     Leonidas J. Guibas. Frustum pointnets for 3d object detec-
     tion from RGB-D data. CoRR, abs/1711.08488, 2017.                    [41] Bin Yang, Ming Liang, and Raquel Urtasun. Hdnet: Exploit-
                                                                               ing hd maps for 3d object detection. In Conference on Robot
[26] Charles R Qi, Hao Su, Kaichun Mo, and Leonidas J Guibas.
                                                                               Learning, pages 146–155, 2018.
     Pointnet: Deep learning on point sets for 3d classifica-
                                                                          [42] Bin Yang, Wenjie Luo, and Raquel Urtasun. Pixor: Real-
     tion and segmentation. Proc. Computer Vision and Pattern
                                                                               time 3d object detection from point clouds. In Proceed-
     Recognition (CVPR), IEEE, 1(2):4, 2017.
                                                                               ings of the IEEE Conference on Computer Vision and Pattern
[27] Charles R Qi, Hao Su, Matthias Nießner, Angela Dai,
                                                                               Recognition, pages 7652–7660, 2018.
     Mengyuan Yan, and Leonidas J Guibas. Volumetric and
                                                                          [43] Yin Zhou and Oncel Tuzel. Voxelnet: End-to-end learn-
     multi-view cnns for object classification on 3d data. In Pro-
                                                                               ing for point cloud based 3d object detection. CoRR,
     ceedings of the IEEE conference on computer vision and pat-
                                                                               abs/1711.06396, 2017.
     tern recognition, pages 5648–5656, 2016.
                                                                          [44] Menglong Zhu, Konstantinos G Derpanis, Yinfei Yang,
[28] Charles Ruizhongtai Qi, Li Yi, Hao Su, and Leonidas J
                                                                               Samarth Brahmbhatt, Mabel Zhang, Cody Phillips, Matthieu
     Guibas. Pointnet++: Deep hierarchical feature learning on
                                                                               Lecce, and Kostas Daniilidis. Single image 3d object detec-
     point sets in a metric space. In Advances in Neural Informa-
                                                                               tion and pose estimation for grasping. In Robotics and Au-
     tion Processing Systems, pages 5099–5108, 2017.
                                                                               tomation (ICRA), 2014 IEEE International Conference on,
[29] Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali                    pages 3936–3943. IEEE, 2014.
     Farhadi. You only look once: Unified, real-time object de-

                                                                     10
