---
source_id: 074
bibtex_key: wang2019densefusion
title: DenseFusion: 6D Object Pose Estimation by Iterative Dense Fusion
year: 2019
domain_theme: Pose 6D
verified_pdf: 74_DenseFusion.pdf
char_count: 70794
---

DenseFusion: 6D Object Pose Estimation by Iterative Dense Fusion

                                                         Chen Wang2            Danfei Xu1      Yuke Zhu1      Roberto Martı́n-Martı́n1
                                                                            Cewu Lu2     Li Fei-Fei1    Silvio Savarese1
                                                                     1
                                                                         Department of Computer Science, Stanford University
                                                             2
                                                                 Department of Computer Science, Shanghai Jiao Tong University
arXiv:1901.04780v1 [cs.CV] 15 Jan 2019

                                                                  Abstract
                                                                                                                                                  RGB-D
                                            A key technical challenge in performing 6D object pose
                                         estimation from RGB-D image is to fully leverage the two
                                         complementary data sources. Prior works either extract in-                         DenseFusion

                                         formation from the RGB image and depth separately or use
                                         costly post-processing steps, limiting their performances in
                                         highly cluttered scenes and real-time applications. In this
                                         work, we present DenseFusion, a generic framework for
                                         estimating 6D pose of a set of known objects from RGB-
                                         D images. DenseFusion is a heterogeneous architecture
                                         that processes the two data sources individually and uses a
                                         novel dense fusion network to extract pixel-wise dense fea-
                                         ture embedding, from which the pose is estimated. Further-
                                         more, we integrate an end-to-end iterative pose refinement
                                         procedure that further improves the pose estimation while          Figure 1. We develop an end-to-end deep network model for 6D
                                                                                                            pose estimation from RGB-D data, which performs fast and accu-
                                         achieving near real-time inference. Our experiments show
                                                                                                            rate predictions for real-time applications such as robot grasping
                                         that our method outperforms state-of-the-art approaches in         and manipulation.
                                         two datasets, YCB-Video and LineMOD. We also deploy our
                                         proposed method to a real robot to grasp and manipulate            data and perform correspondence grouping and hypothesis
                                         objects based on the estimated pose. Our code and video            verification [3, 12, 13, 15, 25, 32, 37]. However, the re-
                                         are available at https://sites.google.com/view/densefusion/.       liance on handcrafted features and fixed matching proce-
                                                                                                            dures have limited their empirical performances in presence
                                                                                                            of heavy occlusion and lighting variation. Recent success
                                                                                                            in visual recognition has inspired a family of data-driven
                                         1. Introduction                                                    methods that use deep networks for pose estimation from
                                             6D object pose estimation is the crux to many important        RGB-D inputs, such as PoseCNN [40] and MCN [16].
                                         real-world applications, such as robotic grasping and ma-              However, these methods require elaborate post-hoc re-
                                         nipulation [7, 34, 43], autonomous navigation [6, 11, 41],         finement steps to fully utilize the 3D information, such
                                         and augmented reality [18, 19]. Ideally, a solution should         as a highly customized Iterative Closest Point (ICP) [2]
                                         deal with objects of varying shape and texture, show robust-       procedure in PoseCNN and a multi-view hypothesis ver-
                                         ness towards heavy occlusion, sensor noise, and changing           ification scheme in MCN. These refinement steps cannot
                                         lighting conditions, while achieving the speed requirement         be optimized jointly with the final objective and are pro-
                                         of real-time tasks. The advent of cheap RGB-D sensors              hibitively slow for real-time applications. In the context of
                                         has enabled methods that infer poses of low-textured ob-           autonomous driving, a third family of solutions has been
                                         jects even in poorly-lighted environments more accurately          proposed to better exploit the complementary nature of
                                         than RGB-only methods. Nonetheless, it is difficult for ex-        color and depth information from RGB-D data with end-
                                         isting methods to satisfy the requirements of accurate pose        to-end deep models, such as Frustrum PointNet [22] and
                                         estimation and fast inference simultaneously.                      PointFusion [41]. These models have achieved good per-
                                             Classical approaches first extract features from RGB-D         formances in driving scenes and the capacity of real-time

                                                                                                        1
inference. However, as we demonstrate empirically, these              remains a challenge for the lack of depth information. Our
methods fall short under heavy occlusion, which is common             method leverages both image and 3D data to estimate object
in manipulation domains.                                              poses in 3D in an end-to-end architecture.
   In this work, we propose an end-to-end deep learning ap-           Pose from depth / point cloud. Recent studies have pro-
proach for estimating 6-DoF poses of known objects from               posed to directly tackle the 3D object detection problem in
RGB-D inputs. The core of our approach is to embed and                discretized 3D voxel spaces. For example, Song et al. [28,
fuse RGB values and point clouds at per-pixel level, as op-           29] generate 3D bounding box proposals and estimate the
posed to prior work which uses image crops to compute                 poses by featuring the voxelized input with 3D ConvNets.
global features [41] or 2D bounding boxes [22]. This per-             Although the voxel representation effectively encodes ge-
pixel fusion scheme enables our model to explicitly rea-              ometric information, these methods are often prohibitively
son about the local appearance and geometry information,              expensive: [29] takes nearly 20 seconds for each frame.
which is essential to handle heavy occlusion. Furthermore,                More recent 3D deep learning architectures have en-
we propose an iterative method which performs pose re-                abled methods that directly performs 6D pose estimation
finement within the end-to-end learning framework. This               on 3D point cloud data. As an example, both Frustrum
greatly enhances model performance while keeping the in-              PointNets [22] and VoxelNet [42] use a PointNet-like [23]
ference speed real-time.                                              structure and achieved state-of-the-art performances on the
   We evaluate our method in two popular benchmarks for               KITTI benchmark [11]. Our method also makes use of sim-
6D pose estimation, YCB-Video [40] and LineMOD [12].                  ilar architecture. However, unlike urban driving applica-
We show that our method outperforms the state-of-the-art              tions for which point cloud alone provides enough informa-
PoseCNN after ICP refinement [40] by 3.5% in pose ac-                 tion, generic object pose estimation tasks such as the YCB-
curacy while being 200x faster in inference time. In par-             Video dataset [40] demands reasoning over both geometric
ticular, we demonstrate its robustness in highly cluttered            and appearance information. We address such a challenge
scenes thanks to our novel dense fusion method. Last, we              by proposing a novel 2D-3D sensor fusion architecture.
also showcase its utility in a real robot task, where the robot
estimates the poses of objects and grasp them to clear up a           Pose from RGB-D data. Classical approaches extract 3D
table.                                                                features from the input RGB-D data and perform corre-
   In summary, the contributions of this work are two-fold:           spondence grouping and hypothesis verification [3, 12, 13,
First, we present a principled way to combine color and               15, 25, 32, 37]. However, these features are either hard-
depth information from the RGB-D input. We augment                    coded [12, 13, 25] or learned by optimizing surrogate ob-
the information of each 3D point with 2D information from             jectives [3, 32, 37] such as reconstruction [15] instead of
an embedding space learned for the task and use this new              the true objective of 6D pose estimation. Newer methods
color-depth space to estimate the 6D pose. Second, we in-             such as PoseCNN [40] directly estimates 6D poses from im-
tegrate an iterative refinement procedure within the neural           age data. Li et al. [16] further fuses the depth input as an
network architecture, removing the dependency of previous             additional channel to a CNN-based architecture. However,
methods of a post-processing ICP step.                                these approaches rely on expensive post-processing steps to
                                                                      make full use of 3D input. In comparison, our method fuses
2. Related Work                                                       3D data to 2D appearance feature while retaining the geo-
                                                                      metric structure of the input space, and we show that it out-
Pose from RGB images. Classical methods rely on detect-               performs [40] on the YCB-Video dataset [40] without the
ing and matching keypoints with known object models [1, 7,            post-processing step.
9, 26, 43]. Newer methods address the challenge by learn-                Our method is most related to PointFusion [41], in which
ing to predict the 2D keypoints [3, 21, 31, 33, 34] and solve         geometric and appearance information are fused in a het-
the poses by PnP [10]. Though prevail in speed-demanding              erogeneous architecture. We show that our novel local fea-
tasks, these methods become unreliable given low-texture              ture fusion scheme significantly outperforms PointFusion’s
or low-resolution inputs. Other methods propose to directly           naive fusion-by-concatenation method. In addition, we use
estimate objects pose from images using CNN-based archi-              a novel iterative refinement method to further improve the
tectures [27, 35]. Many such methods focus on orientation             pose estimation.
estimation: Xiang et al. [38, 39] learns a viewpoint-aware
pose estimator by clustering 3D features from object mod-             3. Model
els. Mousavian et al. [20] predicts 3D object parameters and
recovers poses by single-view geometry constraints. Sun-                 Our goal is to estimate the 6D pose of a set of known
dermeyer et al. [30] implicitly encode orientation in a latent        objects present in an RGB-D image of a cluttered scene.
space and in test time find the best match in a codebook as           Without loss of generality, we represent 6D poses as ho-
the orientation prediction. However, pose estimation in 3D            mogeneous transformation matrix, p ∈ SE(3). In other

                                                                  2
                                                                          image                       color
                                                                           crop                     embeddings             pixel-wise dense fusion

                                                                                                                           (x1,y1)              (xN,yN)
                                      object
                                                                                         CNN
                                   segmentation

                                                                                                             matching                    ...
                                                                                                              point
                                                                         masked
                                                                        point cloud
              6D pose estimation                                                        PointNet

                                                                                                     geometry
                                                                                                    embeddings
                                                                                                                        per-pixel
                                                                                                                         feature          MLP
                                          prediction per pixel
                                                                                                                                                average
                                                                                        pixel-wise feature                                      pooling
                                           pixel (xi,yi) i = 1...N
                                                                                                                 (x1,y1)
                                                  rotation       Ri     pose                                     (x2,y2)
                                                                      predictor                    ...                                   global
                                                  translation    ti                                                                     feature
                      argmax(c)                                                                                  (xN,yN)
                                                  confidence ci

Figure 2. Overview of our 6D pose estimation model. Our model generates object segmentation masks and bounding boxes from RGB
images. The RGB colors and point cloud from the depth map are encoded into embeddings and fused at each corresponding pixel. The
pose predictor produces a pose estimate for each pixel and the predictions are voted to generate the final 6D pose prediction of the object.
(The iterative procedure of our approach is not depicted here for simplicity)

words, a 6D pose is composed by a rotation R ∈ SO(3)                                 The second stage processes the results of the segmenta-
and a translation t ∈ R3 , p = [R|t]. Since we estimate the                       tion and estimates the object’s 6D pose. It comprises four
6D pose of the objects from camera images, the poses are                          components: a) a fully convolutional network that processes
defined with respect to the camera coordinate frame.                              the color information and maps each pixel in the image crop
    Estimating the pose of a known object in adversarial                          to a color feature embedding, b) a PointNet-based [23] net-
conditions (e.g. heavy occlusion, poor lighting, . . . ) is                       work that processes each point in the masked 3D point cloud
only possible by combining the information contained in                           to a geometric feature embedding, c) a pixel-wise fusion
the color and depth image channels. However, the two data                         network that combines both embeddings and outputs the es-
sources reside in different spaces. Extracting features from                      timation of the 6D pose of the object based on an unsuper-
heterogeneous data sources and fusing them appropriately                          vised confidence scoring, and d) an iterative self-refinement
is the key technical challenge in this domain.                                    methodology to train the network in a curriculum learning
    We address this challenge with (1) a heterogeneous ar-                        manner and refine the estimation result iteratively. Fig. 2
chitecture that processes color and depth information dif-                        depicts a), b) and c) and Fig. 3 illustrates d). The details
ferently, retaining the native structure of each data source                      our architecture are described below.
(Sec. 3.3), and (2) a dense pixel-wise fusion network that
performs color-depth fusion by exploiting the intrinsic map-                      3.2. Semantic Segmentation
ping between the data sources (Sec. 3.4). Finally, the pose                          The first step is to segment the objects of interest in the
estimation is further refined with a differentiable iterative                     image. Our semantic segmentation network is an encoder-
refinement module (Sec. 3.6). In contrast to the expensive                        decoder architecture that takes an image as input and gener-
post-hoc refinement steps used in [16, 40], our refinement                        ates an N +1-channelled semantic segmentation map. Each
module can be trained jointly with the main architecture and                      channel is a binary mask where active pixels depict objects
only takes a small fraction of the total inference time.                          of each of the N possible known classes. The focus of this
                                                                                  work is to develop a pose estimation algorithm. Thus we
3.1. Architecture Overview                                                        use an existing segmentation architecture proposed by [40].
   Fig. 2 illustrates the overall proposed architecture. The
                                                                                  3.3. Dense Feature Extraction
architecture contains two main stages. The first stage takes
color image as input and performs semantic segmentation                              The key technical challenge in this domain is the correct
for each known object category. Then, for each segmented                          extraction of information from the color and depth channels
object, we feed the masked depth pixels (converted to 3D                          and their synergistic fusion. Even though color and depth
point cloud) as well as an image patch cropped by the                             present a similar format in the RGB-D frame, their infor-
bounding box of the mask to the second stage.                                     mation resides in different spaces. Therefore, we process

                                                                          3
them separately to generate color and geometric features                     of global fusion so that we can make predictions based on
from embedding spaces that retain the intrinsic structure of                 each fused feature. In this way, we can potentially select
the data sources.                                                            the predictions based on the visible part of the object and
Dense 3D point cloud feature embedding: Previous ap-                         minimize the effects of occlusion and segmentation noise.
proaches have used CNN to process the depth image as an                      Concretely, our dense fusion procedure first associates the
additional image channel [16]. However, such method ne-                      geometric feature of each point to its corresponding image
glects the intrinsic 3D structure of the depth channel. In-                  feature pixel based on a projection onto the image plane us-
stead, we first convert the segmented depth pixels into a 3D                 ing the known camera intrinsic parameters. The obtain pairs
point cloud using the known camera intrinsics, and then use                  of features are then concatenated and fed to another network
a PointNet-like architecture to extract geometric features.                  to generate a fixed-size global feature vector using a sym-
   PointNet by Qi et al. [23] pioneered the use of a symmet-                 metric reduction function. While we refrained from using a
ric function (max-pooling) to achieve permutation invari-                    single global feature for the estimation, here we enrich each
ance in processing unordered point sets. The original archi-                 dense pixel-feature with the global densely-fused feature to
tecture takes as input a raw point cloud and learns to encode                provide a global context.
the information about the vicinity of each point and of the                      We feed each of the resulting per-pixel features into a
point cloud as a whole. The features are shown to be effec-                  final network that predicts the object’s 6D pose. In other
tive in shape classification and segmentation [23] and pose                  words, we will train this network to predict one pose from
estimation [22, 41]. We propose a geometric embedding                        each densely-fused feature. The result is a set of P pre-
network that generates a dense per-point feature by map-                     dicted poses, one per feature. This defines our first learning
ping each of the P segmented points to a dgeo -dimensional                   objective, as we will see in Sec. 3.5. We will now explain
feature space. We implement a variant of PointNet architec-                  our approach to learn to choose the best prediction in a self-
ture that uses average-pooling as opposed to the commonly                    supervised manner, inspired by the work by Xu et al. [41].
used max-pooling as the symmetric reduction function.                        Per-pixel self-supervised confidence: We would like to
Dense color image feature embedding: The goal of the                         train our pose estimation network to decide which pose es-
color embedding network is to extract per-pixel features                     timation is likely to be the best hypothesis based on the spe-
such that we can form dense correspondences between 3D                       cific context. To do so, we modify the network to output
point features and image features. The reason for form-                      a confidence score ci for each prediction in addition to the
ing these dense correspondences will be clear in the next                    pose estimation predictions. We will have to reflect this sec-
section. The image embedding network is a CNN-based                          ond learning objective in the overall learning objective, as
encoder-decoder architecture that maps an image of size                      we will see at the end of the next section.
H × W × 3 into a H × W × drgb embedding space. Each
pixel of the embedding is a drgb -dimensional vector repre-                  3.5. 6D Object Pose Estimation
senting the appearance information of the input image at the                    Having defined the overall network structure, we now
corresponding location.                                                      take a closer look at the learning objective. We define the
3.4. Pixel-wise Dense Fusion                                                 pose estimation loss as the distance between the points sam-
                                                                             pled on the objects model in ground truth pose and cor-
   So far we have obtained dense features from both the                      responding points on the same model transformed by the
image and the 3D point cloud inputs; now we need to fuse                     predicted pose. Specifically, the loss to minimize for the
the information. A naive approach would be to generate a                     prediction per dense-pixel is defined as
global feature from the dense color and depth features from
the segmented area. However, due to heavy occlusion and                                       1 X
                                                                                      Lpi =       ||(Rxj + t) − (R̂i xj + tˆi )||      (1)
segmentation errors, the set of features from previous step                                   M j
may contain features of points/pixels on other objects or
parts of the background. Therefore, blindly fusing color and                 where xj denotes the j th point of the M randomly selected
geometric features globally would degrade the performance                    3D points from the object’s 3D model, p = [R|t] is the
of the estimation. In the following we describe a novel                      ground truth pose, and pˆi = [R̂i |tˆi ] is the predicted pose
pixel-wise1 dense fusion network that effectively combines                   generated from the fused embedding of the ith dense-pixel.
the extracted features, especially for pose estimation under                    The above loss function is only well-defined for asym-
heavy occlusion and imperfect segmentation.                                  metric objects, where the object shape and/or texture deter-
Pixel-wise dense fusion: The key idea of our dense fu-                       mines a unique canonical frame. Symmetric objects have
sion network is to perform local per-pixel fusion instead                    more than one and possibly an infinite number of canoni-
   1 Since the mapping between pixels and 3D points is unique, we will       cal frames, which leads to ambiguous learning objectives.
use interchangeably pixel-fusion and point-fusion.                           Therefore, for symmetric objects, we instead minimize the

                                                                         4
  color
embeddings                                                                              this estimated canonical frame. This way, the transformed
                           global
                          feature                                                       point cloud implicitly encodes the estimated pose. We then
                                       pose
                                                                                        feed the transformed point cloud back into the network and
                                                         rotation residual   𝚫R
               Dense                 residual                                           predict a residual pose based on the previously estimated
               Fusion               estimator            translation residual 𝚫t
                                                                                        pose. This procedure can be applied iteratively and generate
                                                                                        potentially finer pose estimation each iteration.
                                                                    current input
                                                                     point cloud
                                                                                            The procedure is illustrated in Fig. 3. Concretely, we
             PointNet                                                                   train a dedicated pose residual estimator network to per-
 geometry                next iteration
embeddings                                transformed                                   form the refinement given the initial pose estimation from
                                           point cloud                                  the main network. At each iteration, we reuse the image fea-
Figure 3. Iterative Pose Refinement. We introduce an network                            ture embedding from the main network and perform dense
module that refines the pose estimation in an iterative procedure.                      fusion with the geometric features computed for the new
                                                                                        transformed point cloud. The pose residual estimator uses
                                                                                        as input a global feature from the set of fused pixel features.
distance between each point on the estimated model orien-
                                                                                        After K iterations, we obtain the final pose estimation as
tation and the closest point on the ground truth model. The
                                                                                        the concatenation of the per-iteration estimations:
loss function becomes:
           1 X                                                                                  p̂ = [RK |tK ] · [RK−1 |tK−1 ] · · · · · [R0 |t0 ]   (4)
    Lpi =          min ||(Rxj + t) − (R̂i xk + tˆi )|| (2)
          M j 0<k<M                                                                        The pose residual estimator can be trained jointly with
                                                                                        the main network. However, the pose estimation at the be-
   Optimizing over all predicted per dense-pixel poses                                  ginning of the training is too noisy for it to learn anything
would be to minimize    the sum of the per dense-pixels                                 meaningful. Thus in practice, the joint training starts after
losses: L = N1 i Lpi . However, as explained before,
                  P
                                                                                        the main network has converged.
we would like our network to learn to balance the confi-
dence among the per dense-pixel predictions. To do that we                              4. Experiments
weight the per dense-pixel loss with the dense-pixel confi-
dence, and add a second confidence regularization term:                                     In the experimental section, we would like to answer the
                                                                                        following questions: (1) How does the dense fusion net-
                        1 X p                                                           work compare to naive global fusion-by-concatenation? (2)
                L=          (Li ci − w log(ci )),                             (3)
                        N i                                                             Is the dense fusion and prediction scheme robust to heavy
                                                                                        occlusion and segmentation errors? (3) Does the iterative
where N is the number of randomly sampled dense-pixel                                   refinement module improve the final pose estimation? (4)
features from the P elements of the segment and w is a bal-                             Is our method robust and efficient enough for downstream
ancing hyperparameter. Intuitively, low confidence will re-                             tasks such as robotic grasping?
sult in low pose estimation loss but would incur high penalty                               To answer the first three questions, we evaluate our
from the second term, and vice versa. We use the pose esti-                             method on two challenging 6D object pose estimation
mation that has the highest confidence as the final output.                             datasets: YCB-Video Dataset [40] and LineMOD [12]. The
                                                                                        YCB-Video Dataset features objects of varying shapes and
3.6. Iterative Refinement                                                               texture levels under different occlusion conditions. Hence
    The iterative closest point algorithm (ICP) [2] is a pow-                           it’s an ideal testbed for our occlusion-resilient multi-modal
erful refinement approach used by many 6D pose estima-                                  fusion method. The LineMOD dataset is a widely-used
tion methods [14, 30, 40]. However, the best-performing                                 dataset that allows us to compare with a broader range of
ICP implementations are often not efficient enough for real-                            existing methods. We compare our method with state-of-
time applications. Here we propose a neural network-based                               the-art methods [14, 30] as well as model variants. To an-
iterative refinement module that can improve the final pose                             swer the last question, we deploy our model to a real robot
estimation result in a fast and robust manner.                                          platform and evaluate the performance of a robot grasping
    The goal is to enable the network to correct its own pose                           task that uses the predictions from our model.
estimation error in an iterative manner. The challenge here
                                                                                        4.1. Datasets
is training the network to refine the previous prediction as
opposed to making new predictions. To do so, we must                                    YCB-Video Dataset. The YCB-Video Dataset Xiang et
include the prediction made in a previous iteration as part of                          al. [40] features 21 YCB objects Calli et al. [5] of varying
the input to the next iteration. Our key idea is to consider the                        shape and texture. The dataset contains 92 RGB-D videos,
previously predicted pose as an estimate of canonical frame                             where each video shows a subset of the 21 objects in differ-
of the target object and transform the input point cloud into                           ent indoor scenes. The videos are annotated with 6D poses

                                                                                    5
      Table 1. Quantitative evaluation of 6D pose (ADD-S[40]) on YCB-Video Dataset. Objects with bold name are symmetric.
                                PointFusion [41] PoseCNN+ICP [40] Ours (single)          Ours (per-pixel) Ours (iterative)
                                AUC       <2cm      AUC      <2cm       AUC <2cm AUC              <2cm      AUC <2cm
     002 master chef can        90.9       99.8     95.8      100.0     93.9    100.0    95.2      100.0    96.4   100.0
     003 cracker box            80.5       62.6     92.7       91.6     90.8    98.4     92.5      99.3     95.5    99.5
     004 sugar box              90.4       95.4     98.2      100.0     94.4    99.2     95.1      100.0    97.5   100.0
     005 tomato soup can        91.9       96.9     94.5       96.9     92.9    96.7     93.7      96.9     94.6    96.9
     006 mustard bottle         88.5       84.0     98.6      100.0     91.2    97.8     95.9      100.0    97.2   100.0
     007 tuna fish can          93.8       99.8     97.1      100.0     94.9    100.0    94.9      100.0    96.6   100.0
     008 pudding box            87.5       96.7     97.9      100.0     88.3    97.2     94.7      100.0    96.5   100.0
     009 gelatin box            95.0      100.0     98.8      100.0     95.4    100.0    95.8      100.0    98.1   100.0
     010 potted meat can        86.4       88.5     92.7       93.6     87.3    91.4     90.1      93.1     91.3    93.1
     011 banana                 84.7       70.5     97.1       99.7     84.6    62.0     91.5      93.9     96.6   100.0
     019 pitcher base           85.5       79.8     97.8      100.0     86.9    80.9     94.6      100.0    97.1   100.0
     021 bleach cleanser        81.0       65.0     96.9       99.4     91.6    98.2     94.3      99.8     95.8   100.0
     024 bowl                   75.7       24.1     81.0       54.9     83.4    55.4     86.6      69.5     88.2    98.8
     025 mug                    94.2       99.8     95.0       99.8     90.3    94.7     95.5      100.0    97.1   100.0
     035 power drill            71.5       22.8     98.2       99.6     83.1    64.2     92.4      97.1     96.0    98.7
     036 wood block             68.1       18.2     87.6       80.2     81.7    76.0     85.5      93.4     89.7    94.6
     037 scissors               76.7       35.9     91.7       95.6     83.6    75.1     96.4      100.0    95.2   100.0
     040 large marker           87.9       80.4     97.2       99.7     91.2    88.6     94.7      99.2     97.5   100.0
     051 large clamp            65.9       50.0     75.2       74.9     70.5    77.1     71.6      78.5     72.9    79.2
     052 extra large clamp 60.4            20.1     64.4       48.8     66.4    50.2     69.0      69.5     69.8    76.3
     061 foam brick             91.8      100.0     97.2      100.0     92.1    100.0    92.4      100.0    92.5   100.0
     MEAN                       83.9       74.1     93.0       93.2     88.2    87.9     91.2      95.3     93.1    96.8

and segmentation masks. We follow prior work [40] and               the predictions under the minimum tolerance for robot ma-
split the dataset into 80 videos for training and 2,949 key         nipulation (2cm for most of the robot grippers).
frames chosen from the rest 12 videos for testing and in-              For the LineMOD dataset, we use the Average Distance
clude the same 80,000 synthetic images released by [40]             of Model Points (ADD) [13] for non-symmetric objects and
in our training set. In our experiments, we compare with            ADD-S for the two symmetric objects (eggbox and glue)
the result of [40] after depth refinement(ICP) and learning-        following prior works [13, 30, 33].
based depth method [41].
LineMOD Dataset. The LineMOD dataset Hinterstoisser                 4.3. Implementation Details
et al. [12] consists of 13 low-textured objects in 13 videos.
                                                                        The image embedding network consists of a Resnet-
It is widely adopted by both classical methods [4, 8, 36]
                                                                    18 encoder followed by 4 up-sampling layers as the de-
and recent learning-based approaches [17, 30, 33]. We use
                                                                    coder. The PointNet architecture is an MLP followed by
the same training and testing set as prior learning-based
                                                                    an average-pooling reduction function. Both color and geo-
works [17, 24, 33] without additional synthetic data and
                                                                    metric dense feature embedding are of dimension 128. We
compare with the best ICP-refined results of the state-of-
                                                                    choose w = 0.01 for Eq. 3 by empirical evaluation. The
the-art algorithms.
                                                                    iterative pose refinement module consists of a 4 fully con-
4.2. Metrics                                                        nected layers that directly output the pose residual from the
                                                                    global dense feature. We use the 2 refinement iterations for
    We use two metrics to report on the YCB-Video Dataset.
                                                                    all experiments.
The average closest point distance (ADD-S) [40] is an
ambiguity-invariant pose error metric which takes care of           4.4. Architectures
both symmetric and non-symmetric objects into an over-
all evaluation. Given the estimated pose [R̂|t̂] and ground            We compare four model variants that showcase the ef-
truth pose [R|t], ADD-S calculates the mean distance from           fectiveness of our design choices.
each 3D model point transformed by [R̂|t̂] to its closest            • PointFusion [41] uses a CNN to extract a fixed-size fea-
neighbour on the target model transformed by [R|t]. We              ture vector and fuse by directly concatenating the image fea-
report the area under the ADD-S curve (AUC) following               ture with the geometry feature. The rest of the network is
PoseCNN [40]. We follow prior work and set the maximum              similar to our architecture. The comparison to this baseline
threshold of AUC to be 0.1m. We also report the percent-            demonstrates the effectiveness of our dense fusion network.
age of ADD-S smaller than 2cm (<2cm), which measures                 • Ours (single) uses our dense fusion network, but instead

                                                                6
Figure 4. Qualitative results on the YCB-Video Dataset. All three methods shown here are tested with the same segmentation masks as
in PoseCNN. Each object point cloud in different color are transformed with the predicted pose and then projected to the 2D image frame.
The first two rows are former RGB-D methods and the last row is our approach with dense fusion and iterative refinement (2 iterations).

of performing per-point prediction, it only outputs a single           which suffer from orientation ambiguity.
prediction using the global feature vector.                            Robustness towards occlusion The main advantage of our
 • Ours (per-pixel) performs per-pixel prediction based on             dense fusion method is its robustness towards occlusions.
each densely fused feature.                                            To quantify the effect of occlusion on final performance,
 • Ours (iterative) is our complete model that uses the iter-          we calculate the visible surface ratio of each object instance
ative refinement (Sec. 3.6) on top of Ours (per-pixel).                (further detail available in supplementary material). Then
                                                                       we calculate how the accuracy (ADD-S<2cm percentage)
4.5. Evaluation on YCB-Video Dataset                                   changes with extent of occlusion. As shown in Fig. 5, the
    Table 1 shows the evaluation results for all the 21                performances of PointFusion and PoseCNN+ICP degrade
objects in the YCB-Video Dataset.            We report the             significantly as the occlusion increases. In contrast, none of
ADD-S AUC(<0.1m) and the ADD-S<2cm metrics on                          our methods experiences notable performance drop. In par-
PoseCNN [40] and our four model variants. To ensure a fair             ticular, the performance of both Ours (per-pixel) and Ours
comparison, all methods use the same segmentation masks                (iterative) only decrease by 2% overall.
as in PoseCNN [40]. Among our model variants, Ours                     Time efficiency We compare the time efficiency of our
(Iterative) achieves the best performance. Our method is               model with PoseCNN+ICP in Table 3. We can see
able to outperform PoseCNN + ICP[40] even without itera-               that our method is two order of magnitude faster than
tive refinement. In particular, Ours (Iterative) outperforms           PoseCNN+ICP. In particular, PoseCNN+ICP spends most
PoseCNN + ICP by 3.5% on the ADD-S<2cm metric.                         of time on the post processing ICP. In contrast, all of
Effect of dense fusion Both of our dense fusion baselines              our computation component, namely segmentation (Seg),
(Ours (single) and Ours (per-pixel)) outperform PointFu-               pose estimation (PE), and iterative refinement (Refine), are
sion by a large margin, which shows that dense fusion has              equally efficient, and the overall runtime is fast enough
a clear advantage over the global fusion-by-concatenation              for real-time application (16 FPS, about 5 objects in each
method used in PointFusion.                                            frame).
Effect of iterative refinement Table 1 shows that our iter-            Qualitative evaluation Fig. 4 visualizes some sample pre-
ative refinement improves the overall pose estimation per-             dictions made by PoseCNN+ICP, PointFusion, and our iter-
formance. In particular, it significantly improves the per-            ative refinement model. As we can see, PoseCNN+ICP and
formances for texture-less symmetric object, e.g., bowl                PointFusion fail to estimate the correct pose of the bowl in
(29%), banana (6%), and extra large clamp (6%)                         the leftmost column and the cracker box in the middle col-

                                                                   7
        Table 2. Quantitative evaluation of 6D pose (ADD[13]) on the LineMOD dataset. Objects with bold name are symmetric.
                                      RGB                                      RGB-D
                                          PoseCNN
                             BB8 [24]                  Implicit    SSD-6D    PointFusion       Ours        Ours
                                          +DeepIM
                               w ref.                 [30]+ICP     [14]+ICP      [41]       (per-pixel) (iterative)
                                           [17, 40]
                ape            40.4          77.0       20.6          65         70.4          79.5         92.3
                bench vi.      91.8          97.5       64.3          80         80.7          84.2         93.2
                camera         55.7          93.5       63.2          78         60.8          76.5         94.4
                can            64.1          96.5       76.1          86         61.1          86.6         93.1
                cat            62.6          82.1       72.0          70         79.1          88.8         96.5
                driller        74.4          95.0       41.6          73         47.3          77.7         87.0
                duck           44.3          77.7       32.4          66         63.0          76.3         92.3
                eggbox         57.8          97.1       98.6         100         99.9          99.9         99.8
                glue           41.2          99.4       96.4         100         99.3          99.4        100.0
                hole p.        67.2          52.8       49.9          49         71.8          79.0         92.1
                iron           84.7          98.3       63.1          78         83.2          92.1         97.0
                lamp           76.5          97.5       91.7          73         62.3          92.3         95.3
                phone          54.0          87.7       71.0          79         78.8          88.0         92.8
                MEAN           62.7          88.6       64.7          79         73.7          86.2         94.3

                                                                             input crop    initial   iteration 1   iteration 2   iteration 3

                                                                              ADD (m):     0.029       0.022         0.018         0.018

                                                                              ADD (m):     0.015       0.010         0.008         0.007
                                                                          Figure 6. Iterative refinement performance on LineMOD
                                                                          dataset We visualize how our iterative refinement procedure cor-
                                                                          rects initially sub-optimal pose estimation.
Figure 5. Model performance under increasing levels of occlu-
sion. Here the levels of occlusion is estimated by calculating the        4.6. Evaluation on LineMOD Dataset
invisible surface percentage of each object in the image frame. Our
methods work more robustly under heavy occlusion compared to                  Table 2 compares our method with previous RGB meth-
baseline methods.                                                         ods with depth refinement(ICP) (results from [30, 33]) on
                                                                          the ADD metric [13]. Even without the iterative refinement
                                                                          step, our method can outperform 7% over the state-of-the-
Table 3. Runtime breakdown (second per frame on YCB-                      art depth refinement method. After processing the itera-
Video Dataset). Our method is approximately 200x faster than              tive refinement approach, the final result has another 8%
PoseCNN+ICP. Seg means Segmentation, and PE means Pose Es-                improvement, which proves that our learning-based depth
timation.                                                                 method is superior to the sophisticated application of ICP in
      PoseCNN+ICP [40]                   Ours                             both accuracy and efficiency. We visualize the estimated 6D
  Seg     PE    ICP ALL Seg          PE     Refine ALL                    pose after each refinement iteration in Fig.6, where our pose
  0.03 0.17 10.4 10.6 0.03 0.02              0.01    0.06
                                                                          estimation improves by an average of 0.8 cm (ADD) after 2
                                                                          refinement iterations. The results of some other color-only
                                                                          methods are also listed in Table 2 for reference.
                                                                          4.7. Robotic Grasping Experiment
umn due to heavy occlusion, whereas our method remains
robust. Another challenging case is the clamp in the middle                  In our last experiment, we evaluate whether the poses
row due to poor segmentation (not shown in the figure). Our               estimated by our approach are accurate enough to enable
approach localizes the clamp from only the visible part of                robot grasping and manipulation. As shown in Fig. 1, we
the object and effectively reduces the dependency on accu-                place 5 YCB objects on a table and command the robot to
rate segmentation result.                                                 grasp them using the estimated pose. We follow a similar

                                                                      8
procedure to Tremblay et al. [34]: we place the five ob-                 [3]   E. Brachmann, A. Krull, F. Michel, S. Gumhold, J. Shot-
jects in four different random locations on the table, at three                ton, and C. Rother, “Learning 6d object pose estimation
random orientations, including configurations with partial                     using 3d object coordinates,” in European conference on
occlusions. Since the order of picking the objects is not op-                  computer vision, Springer, 2014, pp. 536–551.
timized, we do not allow configurations where objects lay                [4]   A. G. Buch, L. Kiforenko, and D. Kraft, “Rotational sub-
on top of each other. The robot attempts 12 grasps on each                     group voting and pose clustering for robust 3d object recog-
object, 60 attempts in total. The robot uses the estimated                     nition,” in Computer Vision (ICCV), 2017 IEEE Interna-
object orientation to compute an alignment of the gripper’s                    tional Conference on, IEEE, 2017, pp. 4137–4145.
fingers to the object narrower dimension.                                [5]   B. Calli, A. Singh, A. Walsman, S. S. Srinivasa, P. Abbeel,
    The robot succeeds on 73% of the grasps using our pro-                     and A. M. Dollar, “The ycb object and model set: Towards
posed approach to estimate the pose of the objects. The                        common benchmarks for manipulation research,” 2015
most difficult object to grasp is the banana (7 out of 12 suc-                 International Conference on Advanced Robotics (ICAR),
cessful attempts). One possible reason is that our banana                      pp. 510–517, 2015.
model is not exactly the same as in the dataset – ours is                [6]   X. Chen, H. Ma, J. Wan, B. Li, and T. Xia, “Multi-view 3d
plain yellow. This characteristic hinders the estimation, es-                  object detection network for autonomous driving,” in Pro-
pecially of the orientation, and leads to some failed grasp                    ceedings of the IEEE Computer Vision and Pattern Recog-
attempts along the longer axis of the object. In spite of this                 nition (CVPR), 2017.
less accurate case, our results indicate that our approach is            [7]   A. Collet, M. Martinez, and S. S. Srinivasa, “The moped
robust enough to be deployed in real-world robotic tasks                       framework: Object recognition and pose estimation for
without explicit domain adaptation, even with a different                      manipulation,” The International Journal of Robotics Re-
RGB-D sensor and in a different background than the ones                       search, vol. 30, no. 10, pp. 1284–1306, 2011.
in the training data.                                                    [8]   B. Drost, M. Ulrich, N. Navab, and S. Ilic, “Model globally,
                                                                               match locally: Efficient and robust 3d object recognition,”
5. Conclusion                                                                  in Computer Vision and Pattern Recognition (CVPR), 2010
                                                                               IEEE Conference on, Ieee, 2010, pp. 998–1005.
   We presented a novel approach to estimating 6D poses of               [9]   V. Ferrari, T. Tuytelaars, and L. Van Gool, “Simultaneous
known objects from RGB-D images. Our approach fuses a                          object recognition and segmentation from single or multi-
dense representation of features that include color and depth                  ple model views,” International Journal of Computer Vi-
information based on the confidence of their predictions.                      sion, vol. 67, no. 2, pp. 159–188, 2006.
With this dense fusion approach, our method outperforms                 [10]   M. A. Fischler and R. C. Bolles, “Random sample consen-
previous approaches in several datasets, and is significantly                  sus: A paradigm for model fitting with applications to im-
more robust against occlusions. Additionally, we demon-                        age analysis and automated cartography,” Communications
strated that a robot can use our proposed approach to grasp                    of the ACM, vol. 24, no. 6, pp. 381–395, 1981.
and manipulate objects.                                                 [11]   A. Geiger, P. Lenz, and R. Urtasun, “Are we ready for
                                                                               autonomous driving? the kitti vision benchmark suite,” in
Acknowledgement                                                                Proceedings of the IEEE Computer Vision and Pattern
                                                                               Recognition (CVPR), IEEE, 2012, pp. 3354–3361.
   This work has been partially supported by JD.com
American Technologies Corporation (“JD”) under the                      [12]   S. Hinterstoisser, S. Holzer, C. Cagniart, S. Ilic, K. Kono-
SAIL-JD AI Research Initiative and by an ONR MURI                              lige, N. Navab, and V. Lepetit, “Multimodal templates for
                                                                               real-time detection of texture-less objects in heavily clut-
award (1186514-1-TBCJE). This article solely reflects the
                                                                               tered scenes,” Proceedings of the IEEE International Con-
opinions and conclusions of its authors and not JD or any                      ference on Computer Vision (ICCV), pp. 858–865, 2011.
entity associated with JD.com.
                                                                        [13]   S. Hinterstoisser, V. Lepetit, S. Ilic, S. Holzer, G. Bradski,
                                                                               K. Konolige, and N. Navab, “Model based training, detec-
References                                                                     tion and pose estimation of texture-less 3d objects in heav-
 [1]   M. Aubry, D. Maturana, A. A. Efros, B. C. Russell, and J.               ily cluttered scenes,” in Asian conference on computer vi-
       Sivic, “Seeing 3d chairs: Exemplar part-based 2d-3d align-              sion, Springer, 2012, pp. 548–562.
       ment using a large dataset of cad models,” in Proceed-           [14]   W. Kehl, F. Manhardt, F. Tombari, S. Ilic, and N. Navab,
       ings of the IEEE Computer Vision and Pattern Recognition                “Ssd-6d: Making rgb-based 3d detection and 6d pose es-
       (CVPR), 2014, pp. 3762–3769.                                            timation great again,” in Proceedings of the IEEE Inter-
 [2]   P. J. Besl and N. D. McKay, “A method for registration of               national Conference on Computer Vision (ICCV), 2017,
       3-d shapes,” IEEE Trans. Pattern Anal. Mach. Intell., vol.              pp. 22–29.
       14, pp. 239–256, 1992.

                                                                    9
[15]   W. Kehl, F. Milletari, F. Tombari, S. Ilic, and N. Navab,           [30]   M. Sundermeyer, Z.-C. Marton, M. Durner, M. Brucker,
       “Deep learning of local rgb-d patches for 3d object detec-                 and R. Triebel, “Implicit 3d orientation learning for 6d ob-
       tion and 6d pose estimation,” in European Conference on                    ject detection from rgb images,” in European Conference
       Computer Vision, Springer, 2016, pp. 205–220.                              on Computer Vision, Springer, 2018, pp. 712–729.
[16]   C. Li, J. Bai, and G. D. Hager, “A unified framework                [31]   S. Suwajanakorn, N. Snavely, J. Tompson, and M. Norouzi,
       for multi-view multi-class object pose estimation,” ArXiv                  “Discovery of latent 3d keypoints via end-to-end geometric
       preprint arXiv:1803.08103, 2018.                                           reasoning,” ArXiv preprint arXiv:1807.03146, 2018.
[17]   Y. Li, G. Wang, X. Ji, Y. Xiang, and D. Fox, “Deepim: Deep          [32]   A. Tejani, D. Tang, R. Kouskouridas, and T.-K. Kim,
       iterative matching for 6d pose estimation,” ArXiv preprint                 “Latent-class hough forests for 3d object detection and pose
       arXiv:1804.00175, 2018.                                                    estimation,” in Proceedings of the European Conference on
[18]   E. Marchand, H. Uchiyama, and F. Spindler, “Pose esti-                     Computer Vision, Springer, 2014, pp. 462–477.
       mation for augmented reality: A hands-on survey,” IEEE              [33]   B. Tekin, S. N. Sinha, and P. Fua, “Real-Time Seam-
       transactions on visualization and computer graphics, vol.                  less Single Shot 6D Object Pose Prediction,” in Proceed-
       22, no. 12, pp. 2633–2651, 2016.                                           ings of the IEEE Computer Vision and Pattern Recognition
[19]   E. Marder-Eppstein, “Project tango,” in ACM SIGGRAPH                       (CVPR), 2018.
       2016 Real-Time Live!, ser. SIGGRAPH ’16, Anaheim, Cal-              [34]   J. Tremblay, T. To, B. Sundaralingam, Y. Xiang, D. Fox,
       ifornia: ACM, 2016, 40:25–40:25.                                           and S. Birchfield, “Deep object pose estimation for seman-
[20]   A. Mousavian, D. Anguelov, J. Flynn, and J. Kosecka, “3d                   tic robotic grasping of household objects,” ArXiv preprint
       bounding box estimation using deep learning and geome-                     arXiv:1809.10790, 2018.
       try,” in Proceedings of the IEEE Computer Vision and Pat-           [35]   S. Tulsiani and J. Malik, “Viewpoints and keypoints,” in
       tern Recognition (CVPR), 2017.                                             Proceedings of the IEEE Computer Vision and Pattern
[21]   G. Pavlakos, X. Zhou, A. Chan, K. G. Derpanis, and K.                      Recognition (CVPR), 2015, pp. 1510–1519.
       Daniilidis, “6-dof object pose from semantic keypoints,”            [36]   J. Vidal, C.-Y. Lin, and R. Martı́, “6d pose estimation using
       ArXiv preprint arXiv:1703.04670, 2017.                                     an improved method based on point pair features,” in 2018
[22]   C. R. Qi, W. Liu, C. Wu, H. Su, and L. J. Guibas, “Frustum                 4th International Conference on Control, Automation and
       pointnets for 3d object detection from rgb-d data,” ArXiv                  Robotics (ICCAR), IEEE, 2018, pp. 405–409.
       preprint arXiv:1711.08488, 2017.                                    [37]   P. Wohlhart and V. Lepetit, “Learning descriptors for object
[23]   C. R. Qi, H. Su, K. Mo, and L. J. Guibas, “Pointnet: Deep                  recognition and 3d pose estimation,” in Proceedings of the
       learning on point sets for 3d classification and segmenta-                 IEEE Computer Vision and Pattern Recognition (CVPR),
       tion,” ArXiv preprint arXiv:1612.00593, 2016.                              2015, pp. 3109–3118.
[24]   M. Rad and V. Lepetit, “Bb8: A scalable, accurate, robust           [38]   Y. Xiang, W. Choi, Y. Lin, and S. Savarese, “Data-driven 3d
       to partial occlusion method for predicting the 3d poses of                 voxel patterns for object category recognition,” in Proceed-
       challenging objects without using depth.”                                  ings of the IEEE Computer Vision and Pattern Recognition
[25]   R. Rios-Cabrera and T. Tuytelaars, “Discriminatively                       (CVPR), 2015, pp. 1903–1911.
       trained templates for 3d object detection: A real time scal-        [39]   ——, “Subcategory-aware convolutional neural networks
       able approach,” in Proceedings of the IEEE International                   for object proposals and detection,” in Applications of Com-
       Conference on Computer Vision (ICCV), 2013, pp. 2048–                      puter Vision (WACV), 2017 IEEE Winter Conference on,
       2055.                                                                      IEEE, 2017, pp. 924–933.
[26]   F. Rothganger, S. Lazebnik, C. Schmid, and J. Ponce, “3d            [40]   Y. Xiang, T. Schmidt, V. Narayanan, and D. Fox, “Posecnn:
       object modeling and recognition using local affine-invariant               A convolutional neural network for 6d object pose estima-
       image descriptors and multi-view spatial constraints,” In-                 tion in cluttered scenes,” ArXiv preprint arXiv:1711.00199,
       ternational Journal of Computer Vision, vol. 66, no. 3,                    2017.
       pp. 231–259, 2006.
                                                                           [41]   D. Xu, D. Anguelov, and A. Jain, “Pointfusion: Deep sen-
[27]   M. Schwarz, H. Schulz, and S. Behnke, “Rgb-d object                        sor fusion for 3d bounding box estimation,” ArXiv preprint
       recognition and pose estimation based on pre-trained con-                  arXiv:1711.10871, 2017.
       volutional neural network features,” in Robotics and Au-
                                                                           [42]   Y. Zhou and O. Tuzel, “Voxelnet: End-to-end learning
       tomation (ICRA), 2015 IEEE International Conference on,
                                                                                  for point cloud based 3d object detection,” ArXiv preprint
       IEEE, 2015, pp. 1329–1335.
                                                                                  arXiv:1711.06396, 2017.
[28]   S. Song and J. Xiao, “Sliding shapes for 3d object detection
       in depth images,” in European conference on computer vi-            [43]   M. Zhu, K. G. Derpanis, Y. Yang, S. Brahmbhatt, M.
       sion, Springer, 2014, pp. 634–651.                                         Zhang, C. Phillips, M. Lecce, and K. Daniilidis, “Single im-
                                                                                  age 3d object detection and pose estimation for grasping,”
[29]   ——, “Deep sliding shapes for amodal 3d object detection                    in Robotics and Automation (ICRA), 2014 IEEE Interna-
       in rgb-d images,” in Proceedings of the IEEE Computer Vi-                  tional Conference on, IEEE, 2014, pp. 3936–3943.
       sion and Pattern Recognition (CVPR), 2016, pp. 808–816.

                                                                      10
6. Supplementary Materials
6.1. Invisible surface percentage calculation
   The invisible surface percentage is a measurement that
quantifies how occluded an object is given the camera view-
point. The measurement is used in Sec.4.5 of the main
manuscript. Following are the details of how to compute
the invisible surface percentage.
   First, we transform the ground truth model of an object
to its target pose. Then, the 3D points on the surface of
the model are sampled and projected back to a 2D image
plane as depth pixels according to the camera intrinsic pa-
rameters. The projected depth pixels should be close to the
depth measured by a depth sensor if there is no occlusion.
In other words, if the distance between the measured depth
of a pixel and the model-projected depth is larger than a
margin, we consider the pixel as being occluded and thus
invisible. Concretely, suppose a projected depth pixel p has
                                                     ˆ
depth value d(p), and the measured depth of p is d(p).     p is
                                 ˆ
considered invisible if |d(p) − d(p)|  > h. The margin h is
set to be 20mm in the experiment. The invisible surface per-
centage is thus the percentage of the points that are invisible
out of all sampled points on the object model surface. Since
around half of the points on an object model are always in-
visible due to self-occlusion, Fig.5 in the main manuscript
shows results starting from 60 invisible surface percentage.
6.2. Details of the robotic grasping experiment
   The robot used in the experiment is a Toyota HSR
(Human Support Robot). The robot is equipped with
an Asus Xtion RGB-D sensor, a holonomic mobile
base, and a two-finger gripper. We deployed our pose
estimation model trained on YCB-Video dataset with-
out finetuning. Note that our camera (Asus Xtion) is
different from the one used to capture the YCB-Video
dataset (Kinect-v2). Our experiment shows that our
model is able to tolerate the difference in camera and
perform accurate pose estimation. The evaluation in-
cludes five YCB objects: 005 tomato soup can,
006 mustard bottle,              007 tuna fish can,
011 banana, and 021 bleach cleanser.

6.3. Additional iterative refinement examples
   See Fig. 7.                                                         Figure 7. Iterative refinement performance on LineMOD
                                                                       dataset The initial estimation is outputted by Ours (per-pixel).
                                                                       We first transform the object model with the estimated pose and
                                                                       ground truth pose into the 3D space. The ADD distance is the av-
                                                                       erage distance between each corresponding point pair on the two
                                                                       transformed model point clouds. Here we show our iterative re-
                                                                       finement performance in more situations includes blurring and low
                                                                       light conditions, where we can see clear improvement on accuracy
                                                                       by using our neural network based iterative refinement method.

                                                                  11
