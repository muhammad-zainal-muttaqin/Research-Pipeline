---
source_id: 077
bibtex_key: chen2020g2lnet
title: G2L-Net: Global to Local Network for Real-Time 6D Pose Estimation with Embedding Vector Features
year: 2020
domain_theme: Pose 6D
verified_pdf: 77_G2L-Net.pdf
char_count: 70343
---

G2L-Net: Global to Local Network for Real-time 6D Pose Estimation with
                                                                   Embedding Vector Features

                                                 Wei Chen 1,2           Xi Jia1       Hyung Jin Chang1             Jinming Duan1                              Ales Leonardis1
                                                                    1
                                                                      School of Computer Science, University of Birmingham
arXiv:2003.11089v2 [cs.CV] 26 Mar 2020

                                                          2
                                                              School of Computer Science, National University of Defense Technology
                                                                { wxc795,X.Jia.1,h.j.chang,j.duan,a.leonardis}@cs.bham.ac.uk

                                                                 Abstract
                                                                                                                                                                         Rotation

                                                                                                                     Depth
                                                                                                                             +                                         localization
                                                                                                                                             3D                          with EVF
                                             In this paper, we propose a novel real-time 6D object                                      segmentation
                                                                                                                                        & Translation
                                         pose estimation framework, named G2L-Net. Our network                                           localization
                                                                                                                                                                        Rotation

                                                                                                                     RGB
                                                                                                                                 CNN                                     residual
                                         operates on point clouds from RGB-D detection in a divide-                                                                     estimator

                                         and-conquer fashion. Specifically, our network consists of         Global localization        Translation localization   Rotation localization
                                         three steps. First, we extract the coarse object point cloud
                                         from the RGB-D image by 2D detection. Second, we feed          Figure 1. Three steps of G2L-Net. We propose a novel real-time
                                         the coarse object point cloud to a translation localization    point cloud based network for 6D object pose estimation called
                                         network to perform 3D segmentation and object translation      G2L-Net. Our G2L-Net contains global localization, object trans-
                                                                                                        lation localization and rotation localization. For the rotation local-
                                         prediction. Third, via the predicted segmentation and trans-
                                                                                                        ization, we propose point-wise embedding vector features (EVF)
                                         lation, we transfer the fine object point cloud into a local   and rotation residual estimator to access accurate rotation.
                                         canonical coordinate, in which we train a rotation local-
                                         ization network to estimate initial object rotation. In the
                                         third step, we define point-wise embedding vector features         Deep learning methods have shown the state-of-the-art
                                         to capture viewpoint-aware information. To calculate more      performance in the pose estimation tasks, but many of them
                                         accurate rotation, we adopt a rotation residual estimator      [42, 32, 27, 19] cannot run in real-time. While there ex-
                                         to estimate the residual between initial rotation and ground   ist some real-time deep learning methods [28, 33, 38, 45]
                                         truth, which can boost initial pose estimation performance.    (> 20fps), they use only RGB information from an image.
                                         Our proposed G2L-Net is real-time despite the fact multi-      One major limitation of using RGB only is that features
                                         ple steps are stacked via the proposed coarse-to-fine frame-   learned from such information are sensitive to occlusion
                                         work. Extensive experiments on two benchmark datasets          and illumination changes, which precludes these methods
                                         show that G2L-Net achieves state-of-the-art performance in     from being applied to complicated scenes. Deep learning
                                         terms of both accuracy and speed. 1                            methods based on depth information [16, 19] are more suit-
                                                                                                        able for realistically complicated scenes, but they are usu-
                                                                                                        ally computation-intensive. One common issue for these
                                         1. Introduction                                                RGBD-based methods is that exploiting viewpoint infor-
                                                                                                        mation from depth information is not very effective, thus
                                            Real-time performance is important in many computer         reducing their pose estimation accuracy. To overcome this,
                                         vision tasks, such as, object detection [34, 21], semantic     these methods tend to use a post-refinement mechanism or
                                         segmentation [35, 9], object tracking [5, 10], and pose es-    a hypotheses generation/verification mechanism to enhance
                                         timation [28, 38, 15]. In this paper, we are interested in     pose estimation accuracy. This, however, reduces the infer-
                                         real-time 6D object pose estimation, which has significant     ence speed for pose estimation.
                                         impacts on augmented reality [23, 24], smart medical and           In this paper, to overcome the existing problems in
                                         robotic manipulation [47, 39].                                 depth-based methods, we propose a global to local real-
                                           1 Our code is available at https://github.com/DC1991/G2L_    Net.
time network (G2L-Net), with two added modules which             changes which result in pose estimation from RGB image
are point-wise embedding vector features extractor and ro-       more sensitive to illumination changes.
tation residual estimator. Built on [29], our method has         Pose estimation from RGB image with depth informa-
three major novelties: i) instead of locating the object point   tion: When depth information is available, previous ap-
cloud by a frustum, we locate the object point cloud by a        proaches [2, 37, 41, 12] learned features from the input
3D sphere, which can limit the 3D search range in a more         RGB-D data and adopted correspondence grouping and hy-
compact space (see Section 3.1 for details), ii) instead of      pothesis verification. However, some papers [44, 36] found
directly regressing the global point feature to estimate the     that the methods are sensitive to image variations and back-
pose, we propose the point-wise embedding vector features        ground clutter. Besides, correspondence grouping and hy-
to effectively capture the viewpoint information, and iii)       pothesis verification further increase the inference time pre-
we estimate the rotation residual between predicted rota-        senting real-time applications. Some methods [42, 15] em-
tion and the ground truth. The rotation residual estimator       ployed the depth information in a post-refinement procedure
further boosts the pose estimation accuracy. We evaluate         by highly customized Iterative Closest Point (ICP) [6, 1]
our method on two widely-used 6D object pose estimation          into deep learning frameworks, which would significantly
datasets, i.e. LINEMOD [11] and YCB-Video [42] dataset.          increase the running time of the algorithms. Recently, sev-
Experimental results show that G2L-Net outperforms state-        eral deep learning methods [16, 19] utilized the depth input
of-the-art depth-based methods in terms of both accuracy         as an extra channel along with the RGB channels. However,
and speed on the LINEMOD dataset, and that G2L-Net               combining depth and RGB information in this way cannot
achieves comparable accuracy while is the fastest method         make full use of geometric information in data and makes
on the YCB-Video dataset.                                        it difficult to integrate information across viewpoints [25].
    In summary, the main contributions of this paper are as      Instead, in this paper, we transfer depth maps to 3D point
follows:                                                         clouds and directly process the 3D point clouds by Point-
                                                                 Nets [30, 29] which extract 3D geometric features more ef-
  • We propose a novel real-time framework to estimate           ficiently than CNN-based architectures.
    6D object pose from RGB-D data in a global to lo-            Pose estimation from point cloud: PointNets [30, 29], Qi
    cal (G2L) way. Due to efficient feature extraction, the      et al. have shown that employing depth information in 3D
    framework runs at over 20fps on a GTX 1080 Ti GPU,           space via the point cloud representation could achieve better
    which is fast enough for many applications.                  performance than that in 2.5D space. Based on that, some
  • We propose orientation-based point-wise embedding            PointNet-based methods [29, 40, 46, 43, 4] presented to di-
    vector features (EVF) which better utilize viewpoint         rectly estimate 6D object pose. They adopted a PoinNet-
    information than the conventional global point fea-          like [30] architecture to access pose from point cloud. In
    tures.                                                       this work, we also make use of PointNet-like architecture
                                                                 but in a different way. Different from 2D methods [42, 19],
  • We propose a rotation residual estimator to estimate         we decouple 6D object pose estimation into three sub-tasks:
    the residual between predicted rotation and ground           global localization, translation localization, and rotation lo-
    truth, which further improves the accuracy of rotation       calization. For the first two sub-tasks, we use similar meth-
    prediction.                                                  ods in [29] but with some improvements described in Sec-
                                                                 tion 3. For the third sub-task, we propose point-wise em-
2. Related work                                                  bedding vector features that exploit the viewpoint informa-
                                                                 tion more effectively and we also propose a rotation resid-
Pose estimation from RGB image: Traditional methods              ual estimator that further improves the pose estimation ac-
[11, 18, 22] compute 6D object pose by matching RGB fea-         curacy. We show that with these improvements, the pro-
tures between a 3D model and test image. These methods           posed G2L-net achieves higher accuracy than state-of-the-
use handcrafted features that are not robust to background       art methods and runs at real-time speed.
clutter and image variations [44, 36, 28]. Learning-based
methods [32, 28, 33, 27, 14, 38] alleviate this problem by       3. Proposed method
training their model to predict 2D keypoints and compute
the object pose by the PnP algorithm [8, 26]. [42, 20, 19]          In Figure 2, we show the inference pipeline of our
decouple the pose estimation into two sub-tasks: translation     proposing G2L-Net which estimates the 6D object pose in
estimation and rotation estimation. More concretely, they        three steps: global localization, translation localization, and
regarded the translation and rotation estimation as a clas-      rotation localization. In the global localization step, we use
sification problem and trained neural networks to classify       a 3D sphere to fast locate the object position in 3D space. In
the image feature into a discretized pose space. However,        the translation localization step, we train a PointNet to per-
the RGB image features may be affected by illumination           form 3D segmentation and estimate object translation. In
                Depth
                                       bbox                                                                                                                                 segmented

                                                    Depth to PC

                                                                                                                                        Max pool
                                                                                                                                                                              points

                                                                                                                               1024
                                                                                                                       128

                                                                                                                                                         512
                                                                                                                                                               256
                                                                                                                                                                     128
                                        cpm

                                                                                                64

                                                                                                          64

                                                                                                                 64
                           CNN
                                       class                                                                                                                                                      residual

                                                                                                                                                                                 max pool
                                                                                                                                                                           128
                                                                                                                                                                           256
                                                                                                                                                                           512

                                                                                                                                                                                            256
                                                                                                                                                                                            128
                                                                                                                                                                                             3
                RGB

                                                                                                                                                                                                  prediction
                                       One-hot
                                     class vector

                             (a) Global localization                                                             (b) Translation localization

                                                                                   Max pool
                                    rotation

                                                                                                          1024
                                                                  128
                                                                        256

                                                                                              256
                                                                                                    512
                                    prediction

                                                                                                                             max pool

                                                                                                                                        1024

                                                                                                                                                   128

                                                                                                                                                          64

                                                                                                                                                                     64

                                                                                                                                                                            64
                                                                        Max pool
                                    rotation

                                                                                              128

                                                                                                      256
                                    residual
                                                                                                                          embedding vector feature extractor
                                                                                                          (c) Rotation localization

Figure 2. Inference pipeline of the proposed G2L-Net. (a) For RGB image, we use a 2D detector to detect the bounding box (bbox) of the
target object and the object label which is used as a one-hot feature for the following networks. Also, we additionally choose the maximum
probability location in class probability map (cpm) as the sphere center (we transfer this 2D location to 3D with known camera parameters
and corresponding depth value) which is used to further reduce the 3D search space. (b) Given the point clouds in the object sphere, we use
a translation localization network to perform 3D segmentation and translation residual prediction. Then we use the 3D segmentation mask
and the predicted translation to transfer the object point cloud into a local canonical coordinate. (c) In the rotation localization network, we
first use the point-wise embedding vector feature extractor to extract embedding vector features. Then we feed this feature into two-point
clouds decoders: the top decoder directly outputs the rotation of the input point cloud and the bottom one outputs the residual of the output
of the top one between the ground truth. k is the dimension of the output vector.“+00 denotes feature concatenation.

the third step, we estimate rotation with the proposed point-                                               3D sphere is the diameter of the detected object. We only
wise embedding vector features and rotation residual esti-                                                  choose points in this compact 3D sphere, which makes the
mator. Please note, this rotation residual estimator is differ-                                             learning task easier for the following steps.
ent from the post-refinement component in previous meth-
ods [42, 15], it outputs rotation residual with initial rotation                                            3.2. Translation localization
synchronously. In the following subsections, we describe                                                       Although the extracted point cloud is tight, there are still
each step in detail.                                                                                        two issues remained: 1) the point cloud in this 3D space
                                                                                                            contains both object points and non-object points, and 2) the
3.1. Global localization                                                                                    object points cannot be transferred to a local canonical coor-
    To fast locate the global position of the target object                                                 dinate due to unknown translation. To cope with the issues,
in the whole scene, we train a 2D CNN detector, YOLO-                                                       similar to [29], we train a two PointNets [30] to perform 3D
V3 [34], to detect the object bounding box in RGB image,                                                    segmentation and output the residual distance ||T − T̄ ||2
and output object label which is used as one-hot class vec-                                                 between the mean value T̄ of the segmented points and ob-
tor for better point cloud instance segmentation, translation                                               ject translation T . This residual can be used to calculate the
and rotation estimation. In [29], they use the 2D bounding                                                  translation of the object.
box to generate frustum proposals which only reduce the
                                                                                                            3.3. Rotation localization with embedding vector
3D search space of two axes (x,y). Differently, rather than
                                                                                                                 feature
only using a 2D bounding box, we propose to employ a 3D
sphere to further reduce the 3D search space in the third axis                                                 From the first two steps, we transfer the point cloud of
(z) (see Figure 3 for details). The center of the 3D sphere                                                 the object to a local canonical space where the viewpoint
is transferred from the 2D location which has the maximum                                                   information is more evident. Theoretically, we need at least
value in the class probability map with known camera pa-                                                    four different viewpoints to cover all points of an object (see
rameters and corresponding depth value. The radius of this                                                  Figure 4) in 3D space [?]. For the pose estimation task, we
                                                                                                                                                      A

                                                                                                                        512
                                                                                                                              256
                                                                                                                                     128
                                                                                                                                                128
                                                                                                             Max pool

                                                                                                                        Max pool
                                                                                                                                                      B

                                                                                                      1024

                                                                                                                         1024
                                                                                                128

                                                                                                                          512
                                                                                                                          256

                                                                                                                          256
                                                                                                                          128
                                                                            PC

                                                                                 64
                                                                                      64
                                                                                           64
                                                                            embedding vector feature extractor

                                                                                                                                           Max pool
                                                                                                                                                      C

                                                                                                                        256

                                                                                                                               128
                                                                         Figure 5. Architecture of the rotation localization network. In
                (a)                              (b)                     the training stage, there are three blocks in rotation localization
                                                                         network. We train block A to predict the unit vectors pointing to
Figure 3. Global 3D sphere. In the global localization step, we          the keypoints, the loss function of this block is the mean square
locate the object point clouds by bounding box as well as a 3D           error between the predicted and ground truth directional vectors.
sphere. (a) Locate the object point cloud only by bounding box.          By training this block, the network can learn how to extract point-
In this case, it can only locate the object in two-dimensional space,    wise embedding vector features from the input point cloud. Note
some points can still very far away from the object in the third axis.   that, block A is not deployed in the inference stage. Then we use
(b) Locate the object point cloud by both the bounding box and 3D        block B to integrate the point-wise embedding vector features to
sphere. All points lay in a more compact space.                          predict object rotation. The loss function of this block is the mean
                                                                         square error between the predicted rotation and ground truth. For
                                                                         rotation residual estimator block C, we use the Euclidean distance
                                                                         between the predicted 3D keypoints position (output of block B)
                                                                         and ground truth as ground truth. k is the dimension of the output
                                                                         rotation vector and v is the dimension of the output directional
                                                                         vector. “+00 denotes feature concatenation.

Figure 4. Different viewpoints. For a 3D object, we need at least
four viewpoints to cover all the points of the 3D object.
                                                                         Figure 6. Point-wise vectors. Here we show point-wise vectors
                                                                         pointing to one keypoint which is shown in green color, and other
usually have hundreds of different viewpoints for one ob-                keypoints are shown in black color. We train our network to pre-
ject during training. Then our goal is to use the viewpoint              dict such directional vectors
information adequately. In [29], they use PointNets [30, 31]
to extract the global feature from the whole point cloud.
However, in our experiments, we found global point fea-                  some pre-defined 3D points based on each 3D object model.
tures extracted from point clouds under similar viewpoints               Two aspects need to be decided for the keypoints: number
are highly correlated, which limit the generalization perfor-            and location. A simple way is to use the 8 corners of the
mance (see Figure 9 in the experiment section).                          3D bounding box of object model as keypoints which we
   To overcome the limitation of global point features, we               show in Figure 7 (a). This definition is widely used by many
propose point-wise embedding vector features. Specifically,              CNN based methods in 2D cases [32, 33, 27, 38]. Another
we design the rotation localization network architecture as              way is, as proposed in [28], to use the farthest point sam-
shown in Figure 5 to predict point-wise unit vectors point-              pling (FPS) algorithm to sample the keypoints in each ob-
ing to keypoints (illustrated in Figure 6). The keypoints are            ject model. Figure 7 shows examples of different keypoint
                                                                   our rotation residual estimator is ||P − P||
                                                                                                            e 2 . As the rotation
                                                                   network converging, it becomes harder to learn the resid-
                                                                   ual. If the rotation localization network can fully exploit the
                                                                   embedding vector feature, the role of rotation residual esti-
                                                                   mator can be ignored. However, when the rotation network
                                                                   cannot fully exploit the embedding vector feature, the rota-
                                                                   tion residual estimator will have a big impact on the final
                                                                   results, we show this property of rotation residual estimator
                                                                   in Figure 9 (b). Please note, our proposed rotation resid-
                                                                   ual estimator is different from the post-refinement module
                  (a)                         (b)                  in the previous state-of-the-art methods [42, 40, 20]. Our
                                                                   proposed rotation residual estimator outputs rotation resid-
Figure 7. Visualization of different keypoint selection schemes.   ual with estimated rotation synchronously, which saves the
The left image is a 3D object point cloud and its 3D bounding      running time.
box; the right image is the keypoint selected by FPS algorithm.
The keypoints are shown in red color.                              4. Experiments
                                                                      There are two parts in this experiments section. Firstly,
selection schemes. In Section 4.4, we show how the number          we do ablation studies on keypoints selection schemes and
and location of the keypoints influence the pose estimation        empirically validate the three innovations introduced in our
results.                                                           new frame: 3D sphere (“SP), point-wise embedding vector
   Similar to [4], our proposed rotation localization net-         features (“EVF) and rotation residual estimator (“RRE”).
work takes object point cloud in the local canonical space         Then we test our proposed G2L-Net on two benchmark
and outputs point-wise unit vectors pointing keypoints. The        datasets, i.e. LINEMOD and YCB-Video datasets. Our
loss function is defined as follows:                               method achieves state-of-the-art performance in real-time
                                                                   on both datasets.
                        K
              1 XX                           2
  `(θ) = min         ke
                      vk (Xi ; θ) − vk (Xi )k2 , (1)               4.1. Implementation details
          θ K |X |
                   i    k=1
                                                                       We implement our framework using Pytorch. We have
where K is the number of keypoints. θ is the network pa-           conducted all the experiments on an Intel i7-4930K 3.4GHz
rameters. vek (Xi ; θ) and vk (Xi ) are the predicted vectors      CPU with one GTX 1080 Ti GPU. First, we fine-tune the
                                             R
and the ground truth, respectively. X ∈ n×3 represents             YOLO-V3 [34] architecture which is pre-trained on the Im-
the object points in the local coordinate space. |X | is the       ageNet [7] to locate the 2D region of interest and access the
number of object points.                                           class probability map. Then we jointly train our proposed
   Different from other state-of-the-art methods [28, 42, 4],      translation localization and rotation localization networks
we adopt a multilayer perceptron (MLP) that takes point-           using PointNet [30] as our backbone network. The archi-
wise embedding vector features as input and outputs the            tectures of these networks are shown in Figure 2. Note that,
rotation of object as shown in Figure 5. Please note, dur-         other point-cloud network architectures [31, 46] can also be
ing inference, we use the rotation matrix to represent the         adopted as our backbone network. For point cloud segmen-
rotation which is computed from the keypoint positions us-         tation we use cross-entropy as the loss function. For trans-
ing the Kabsch algorithm. Over the training process, as per        lation residual prediction, we employ the mean square error
the definition of point-wise vectors, we used only the key-        and the unit in our experiment is mm. We train our rota-
point positions to represent rotation. In experiments, we          tion localization network as described in Figure 5. We use
have found that our proposed method can make faster and            Adam [17] to optimize the proposed G2L-Net. We set the
more accurate predictions than the methods [28, 42, 4].            initial learning rate as 0.001 and halve it every 50 epochs.
   Rotation residual estimator:         To better utilize the      The maximum epoch is 200.
viewpoint information in the point-wise embedding vector
                                                                   4.2. Datasets
features, we add an extra network branch (block C in Fig-
ure 5) to estimate the residual between estimated rotation         LINEMOD [11] is a widely used dataset for 6D object pose
(block B in Figure 5) and ground truth. However, we do not         estimation. There are 13 objects in this dataset. For each ob-
have ground truth for this residual estimator. To address this     ject, there are about 1100-1300 annotated images and each
problem we train this estimator in online fashion. Assuming        has only one annotated object. This dataset exhibits many
that the ground truth for block B of rotation localization net-    challenges for pose estimation: texture-less objects, clut-
work is P and the output of block B is P, e then the target of     tered scenes, and lighting condition variations.
                                                                      Table 1. Ablation studies of different novelties on LINEMOD
                                                                      dataset. The metric we used to measure performance is ADD(-S)
                                                                      metric. “SP” means 3D sphere, “EVF” means embedding vector
                                                                      feature, and “RRE” denotes rotation residual estimator.
                                                                         Method     SP    EVF     RRE        Acc      Speed(fps)
                                                                         EXP1       ×      ×       ×        93.4%        25
                                                                         EXP2       X      ×       ×        95.8%        25
         (a)                    (b)                     (c)              EXP3       X      X       ×        98.4%        23
Figure 8. Point cloud labeling. (a) The object model of cat in           EXP4       X      X       X        98.7%        23
LINEMOD dataset; (b) the point cloud from the depth images in
object region; (c) the transformed object model is overlapped on      Table 2. Ablation studies of different keypoints parameters on
the point cloud. We label each point according to the shortest dis-   LINEMOD dataset. The metric we used to measure performance
tance between the point and the corresponding transformed object      is ADD(-S) metric. BBX-8 means using the 8 corners of 3D
model.                                                                bounding box as keypoints. FPS-K denotes that we adopt K key-
                                                                      points generated by the FPS algorithm.
YCB-Video [42] contains 92 real video sequences for 21                     Method        BBX-8      FPS-4     FPS-8     FPS-12
YCB object instances [3]. This dataset is challenging due                    Acc         98.7%      98.5%     98.4%     98.6%
to the image noise and occlusions.                                        Speed (fps)      23         23        23        23
    However, both LINEMOD and YCB-Video datasets do
not contain the label for each point of the point cloud. To
train G2L-Net in a supervised fashion, we adopt an auto-              which is the area under the accuracy-threshold curve. The
matic way to label each point of the point cloud of [4]. As           maximum threshold is set to 10cm [42].
described in [4], we label each point in two steps First, for
the 3D model of an object, we transform it into the camera            4.4. Ablation studies
coordinate using the corresponding ground truth. We adopt                Compared to the baseline method [29], our proposed
the implementation provided by [13] for this process. Sec-            method has three novelties. First, we fast locate the ob-
ond, for each point on the point cloud in the target region,          ject point clouds by a 3D sphere which is different from
we compute its nearest distance to the transformed object             the frustum method in [29]. Second, we use the proposed
model. If the distance is less than a value  = 8mm, we               point-wise embedding vector features to estimate rotation
label the point as 1 (belonging to the object), otherwise 0.          of the point cloud which can better utilize the viewpoint in-
Figure 8 shows the labeling procedure.                                formation. Third, we propose a rotation residual estimator
                                                                      to estimate the rotation residual between ground truth and
4.3. Evaluation metrics
                                                                      predicted rotation. From Table 1, we can see that the pro-
  We employ the ADD metric [11] to evaluate our G2L-                  posed three improvements can boost performance.
Net on LINEMOD dataset:                                                  We also compare the different keypoints selection
                                                                      schemes in Table 2, however, it shows that different key-
            1 X
                k(R · x + T) − (R
                                e · x + T)k,
                                        e                      (2)    points selection schemes make little difference in the final
           |M|                                                        results. For simplicity, we use the 8 corners of 3D bounding
                  x∈M
                                                                      box as keypoints in our experiments.
where |M| is the number of points in the object model. x
represents the point in object 3D model. R and T are the              4.5. Generalization performance
ground truth pose, and Re and Te are the estimated pose. In
                                                                          In this section, we evaluate the generalization perfor-
this metric, the mean distance between the two transformed
                                                                      mance of our G2L-Net. We gradually reduce the size of
point sets is computed. When the average distance is less
                                                                      training data to see how the performance of the algorithm
than 10% of the 3D object model diameter, we consider that
                                                                      can be affected on LINEMOD dataset. From Figure 9 (a),
estimated 6D pose as correct. For symmetric objects, we
                                                                      we can see that even only 5% of the training data, which is
employ ADD-S metric [11], where the average distance is
                                                                      1/3 of the normal setting, is used for the network training,
calculated using the shortest point distance:
                                                                      the performance (88.5%) is still comparable.
     1 X
          min k(R · x1 + T) − (R
                               e · x2 + T)k.
                                        e                      (3)    4.6. Comparison with the state-of-the-art methods
    |M|  x2 ∈M
          x1 ∈M
                                                                      Object 6D pose estimation on LINEMOD: Same as
   When evaluating on YCB-Video dataset, same as [42,                 other state-of-the-art methods, we use 15% of each object
28, 19], we use the ADD-S AUC metric proposed in [42],                sequence to train and the rest of the sequence to test on
Table 3. 6D pose estimation accuracy on LINEMOD dataset. We use ADD metric to evaluate the methods. For symmetric objects
Egg Box and Glue, we use ADD-S metric. Note that, we summarize the pose estimation results reported in the original papers on
LINEMOD dataset.

                                    PoseCNN +
     Method          PVNet [28]                           DPOD [45]   Frustum-P [29]     Hinterstoisser [12]      DenseFusion [40]          Ours
                                  DeepIM [42, 19]
     Input              RGB            RGB                 RGB         RGB+Depth               Depth                RGB+Depth           RGB+Depth
     Refinement          ×              X                 X(×)             ×                     X                     X(×)                  ×
     Ape               43.6%          77.0%           87.7% (53.3%)      85.5%                 98.5%               92.3% (79.5%)          96.8%
     Bench Vise        99.9%          97.5%           98.5% (95.3%)      93.2%                 99.0 %              93.2%(84.2%)           96.1%
     Camera            86.9%           93.5           96.0% (90.4%)      90.0%                 99.3%               94.4%(76.5%)           98.2%
     Can               95.5%          96.5%           99.7% (94.1%)      91.4%                 98.7%               93.1%(86.6%)           98.0%
     Cat               79.3%          82.1%           94.7% (60.4%)      96.5%                 99.9%               96.5%(88.8%)           99.2%
     Driller           96.4%          95.0%           98.8% (97.7%)      96.8%                 93.4%               87.0%(77.7%)           99.8%
     Duck              52.6%          77.7%           86.3% (66.0%)      82.9%                 98.2%               92.3%(76.3%)           97.7%
     Egg Box           99.2%          97.1%           99.9% (99.7%)      99.9%                 98.8%               99.8%(99.9%)            100%
     Glue              95.7%          99.4%           96.8% (93.8%)      99.2%                 75.4%               100% (99.4%)            100%
     Hole Puncher      81.9%          52.8%           86.9% (65.8%)      92.2%                 98.1%               92.1%(79.0%)           99.0%
     Iron              98.9%          98.3%           100% (99.8%)       93.7%                 98.3%               97.0% (92.1%)           99.3%
     Lamp              99.3%          97.5%           96.8% (88.1%)      98.2%                 96.0%               95.3%(92.3%)           99.5%
     Phone             92.4%          87.7%           94.7% (74.2%)      94.2%                 98.6%               92.8%(88.0%)           98.9%
     Speed(FPS)          25             5                 33(40)           12                     8                    16(20)                23
     Average           86.3%          88.6%           95.2% (83.0%)      93.4%                 96.3 %              94.3 %(86.2%)          98.7 %

                                                                           Table 4. 6D Pose estimation accuracy on the YCB-V dataset. We
                                                                           use ADD-S AUC metric to evaluate the methods.

                                                                                                                                    DenseFusion [40]
                                                                            Method(RGB+Depth)       PoseCNN [42] + ICP   MCN [19]                      Ours
                                                                                                                                     (no refinement)
                                                                            002 master chef can           95.8%           96.2%           95.2%        94.0%
                                                                            003 cracker box               91.8%           90.9 %          92.5%        88.7%
                                                                            004 sugar box                 98.2%           95.3%           95.1%        96.0%
                                                                            005 tomato soup can           94.5%           97.5%           93.7%        86.4%
                                                                            006 mustard bottle            98.4%           97.0%           95.9%        95.9%
                                                                            007 tuna fish can             97.1%           95.1%           94.9%        96.0%
               (a)                                  (b)                     008 pudding box               97.9%           94.5%           94.7%        93.5%
                                                                            009 gelatin box               98.8%           96.0%           95.8%        96.8%
                                                                            010 potted meat can           92.8%           96.7%           90.1%        86.2%
Figure 9. Visualization of method performance on LINEMOD                    011 banana                    96.9%           94.4%           91.5%        96.3%
dataset. (a) Influence of training data size using the ADD metric.          019 pitcher base              97.8%           96.2%           94.6%         91.8%
                                                                            021 bleach cleanser           96.8%           95.4%           94.3%        92.0%
When using the same training size, compared to Frustum-P [29],              024 bowl                      78.3%           82.0%           86.6%         86.7%
our method improves the performance significantly. For simplic-             025 mug                       95.1%           96.8%           95.5%        95.4%
ity, here we provide ground truth 2D bounding box and randomly              035 power drill               98.0%           93.1%           92.4%        95.2%
                                                                            036 wood block                90.5%           93.6%           85.5%        86.2%
choose an object point as 3D sphere center for evaluation. (b) As           037 scissors                  92.2%           94.2%           96.4%        83.8%
the rotation localization network converging, the impacts of rota-          040 large marker              97.2%           95.4%           94.7%        96.8%
                                                                            051 large clamp               75.4%           93.3%           71.6%        94.4%
tion residual estimator (RRE) decreases.                                    052 extra large clamp         65.3%           90.9%           69.0%        92.3%
                                                                            061 foam brick                97.1%           95.9%           92.4%        94.7%
                                                                            Average                       93.0%           94.3 %         91.2 %        92.4 %
                                                                            Speed (fps)                   < 0.1            < 10             20           21
LINEMOD dataset. In Table 3, we compare our method
with state-of-the-art RGB and RGB-D methods. The num-
bers in brackets are the results without post-refinement.                  the fastest inference speed. In Figure 10, we provide a
We use Frustum-P [29] as our baseline. We re-implement                     visual comparison of predict pose versus ground truth pose.
Frustum-P to regress 3D bounding box corners of the
objects. From Table 3, we can see that our method outper-                  Object 6D pose estimation on YCB-Video:
forms the baseline by 5.4% in ADD accuracy and runs 2                          Different from LIMEMOD dataset, in YCB-Video
times faster than the baseline method. Comparing to the                    dataset, each frame may contain multiple target objects.
second-best method [12] that using depth information, our                  Our method can also estimate 6D pose for multiple objects
method outperforms it by 2.4% in ADD accuracy and runs                     in fast speed. Table 4 compares our method with other state-
about 3 times faster than it. Although DPOD and PVNet                      of-the-art methods [42, 19, 40] on YCB-Video dataset un-
are faster than our method, they only take RGB image as                    der ADD-S AUC metric. From Table 4, we can see that our
input. When using depth information, our method achieves                   method achieves a comparable accuracy (92.4%) and is the
Figure 10. Qualitative pose estimation results on LINEMOD dataset. Green 3D bounding boxes denote ground truth. Blue 3D bounding
boxes represent our results. Our results match ground truth well.

                                                                     embedding vector features. In the global localization, we
                                                                     use a 3D sphere to constrain the 3D search space into a more
                                                                     compact space than 3D frustum. Then we perform 3D seg-
                                                                     mentation and object translation estimation. We use the 3D
                                                                     segmentation mask and the estimated object translation to
                                                                     transfer the object points into local coordinate space. Since
                                                                     viewpoint information is more evident in this canonical
                                                                     space, our network can better capture the viewpoint infor-
Figure 11. Visualizing pose estimation results on YCB-Video.         mation with our proposed point-wise embedding vector fea-
White 3D bounding boxes are ground truth. Colorful 3D bounding       tures. In addition, to fully utilize the viewpoint information,
boxes represent our results. For different objects, our prediction
                                                                     we add the rotation estimation estimator, which learns the
matches ground truth well.
                                                                     residual between the estimated rotation and ground truth.
                                                                     In experiments, we demonstrate that our method achieves
fastest one (21fps) among all comparisons. In Figure 11,             state-of-the-art performance in real-time.
we also provide visualization results on this dataset.                  Although our G2L-Net achieves state-of-the-art per-
                                                                     formance, there are some limitations to our framework.
4.7. Running time                                                    First, our G2L-Net relies on a robust 2D detector to detect
   For a single object, given a 480 × 640 RGB-D image,               the region of interest. Second, while our network exploits
our method runs at 23fps on a PC environment (an Intel i7-           viewpoint information from the object point cloud, the
4930K 3.4GHz CPU and one GTX 1080 Ti GPU). Specif-                   texture information is not well adopted. In future work, we
ically, the 2D detector takes 11ms for object location, and          have a plan to overcome these limitations.
pose estimation part which includes translation localization
and rotation localization takes 32ms. The rotation residual          Acknowledgement We acknowledge MoD/Dstl and EP-
estimator takes less than 1ms.                                       SRC (EP/N019415/1) for providing the grant to support the
                                                                     UK academics involvement in MURI project.
5. Conclusion
   In this paper, we propose a novel real-time 6D object
pose estimation framework. Our G2L-Net decouples the
object pose estimation into three sub-tasks: global localiza-
tion, translation localization and rotation localization with
References                                                                [14] Yinlin Hu, Joachim Hugonot, Pascal Fua, and Mathieu
                                                                               Salzmann. Segmentation-driven 6d object pose estimation.
 [1] Paul J Besl and Neil D McKay. Method for registration of                  In The IEEE Conference on Computer Vision and Pattern
     3-d shapes. In Sensor Fusion IV: Control Paradigms and                    Recognition (CVPR), June 2019. 2
     Data Structures, volume 1611, pages 586–607. International           [15] Wadim Kehl, Fabian Manhardt, Federico Tombari, Slobodan
     Society for Optics and Photonics, 1992. 2                                 Ilic, and Nassir Navab. Ssd-6d: Making rgb-based 3d de-
 [2] Eric Brachmann, Alexander Krull, Frank Michel, Stefan                     tection and 6d pose estimation great again. In Proceedings
     Gumhold, Jamie Shotton, and Carsten Rother. Learning                      of the IEEE International Conference on Computer Vision,
     6d object pose estimation using 3d object coordinates. In                 pages 1521–1529, 2017. 1, 2, 3
     European conference on computer vision, pages 536–551.               [16] Wadim Kehl, Fausto Milletari, Federico Tombari, Slobodan
     Springer, 2014. 2                                                         Ilic, and Nassir Navab. Deep learning of local rgb-d patches
 [3] Berk Calli, Aaron Walsman, Arjun Singh, Siddhartha Srini-                 for 3d object detection and 6d pose estimation. In European
     vasa, Pieter Abbeel, and Aaron M Dollar. Benchmarking                     Conference on Computer Vision, pages 205–220. Springer,
     in manipulation research: The ycb object and model set and                2016. 1, 2
     benchmarking protocols. arXiv preprint arXiv:1502.03143,             [17] Diederik P Kingma and Jimmy Ba. Adam: A method for
     2015. 6                                                                   stochastic optimization. arXiv preprint arXiv:1412.6980,
 [4] Wei Chen, Jinming Duan, Hector Basevi, Hyung Jin Chang,                   2014. 5
     and Ales Leonardis. Ponitposenet: Point pose network for             [18] Vincent Lepetit, Pascal Fua, et al. Monocular model-
     robust 6d object pose estimation. In The IEEE Winter Con-                 based 3d tracking of rigid objects: A survey. Foundations
     ference on Applications of Computer Vision, pages 2824–                   and Trends R in Computer Graphics and Vision, 1(1):1–89,
     2833, 2020. 2, 5, 6                                                       2005. 2
 [5] Wei Chen, Xifeng Guo, Xinwang Liu, En Zhu, and Jian-                 [19] Chi Li, Jin Bai, and Gregory D. Hager. A unified framework
     ping Yin. Appearance changes detection during tracking. In                for multi-view multi-class object pose estimation. In The Eu-
     2016 23rd International Conference on Pattern Recognition                 ropean Conference on Computer Vision (ECCV), September
     (ICPR), pages 1821–1826. IEEE, 2016. 1                                    2018. 1, 2, 6, 7
 [6] Yang Chen and Gérard Medioni. Object modelling by regis-            [20] Yi Li, Gu Wang, Xiangyang Ji, Yu Xiang, and Dieter Fox.
     tration of multiple range images. Image and vision comput-                Deepim: Deep iterative matching for 6d pose estimation.
     ing, 10(3):145–155, 1992. 2                                               In The European Conference on Computer Vision (ECCV),
 [7] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li,                    September 2018. 2, 5
     and Li Fei-Fei. Imagenet: A large-scale hierarchical image           [21] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian
     database. In 2009 IEEE conference on computer vision and                  Szegedy, Scott Reed, Cheng-Yang Fu, and Alexander C
     pattern recognition, pages 248–255. Ieee, 2009. 5                         Berg. Ssd: Single shot multibox detector. In European con-
                                                                               ference on computer vision, pages 21–37. Springer, 2016. 1
 [8] Xiao-Shan Gao, Xiao-Rong Hou, Jianliang Tang, and
                                                                          [22] David G Lowe. Object recognition from local scale-invariant
     Hang-Fei Cheng. Complete solution classification for the
                                                                               features. In iccv, page 1150. IEEE, 1999. 2
     perspective-three-point problem. IEEE transactions on
                                                                          [23] Eric Marchand, Hideaki Uchiyama, and Fabien Spindler.
     pattern analysis and machine intelligence, 25(8):930–943,
                                                                               Pose estimation for augmented reality: a hands-on survey.
     2003. 2
                                                                               IEEE transactions on visualization and computer graphics,
 [9] Kaiming He, Georgia Gkioxari, Piotr Dollár, and Ross Gir-
                                                                               22(12):2633–2651, 2016. 1
     shick. Mask r-cnn. In Proceedings of the IEEE international
                                                                          [24] Eitan Marder-Eppstein. Project tango. In ACM SIGGRAPH
     conference on computer vision, pages 2961–2969, 2017. 1
                                                                               2016 Real-Time Live!, page 40. ACM, 2016. 1
[10] João F Henriques, Rui Caseiro, Pedro Martins, and Jorge             [25] Daniel Maturana and Sebastian Scherer. Voxnet: A 3d con-
     Batista. High-speed tracking with kernelized correlation fil-             volutional neural network for real-time object recognition.
     ters. IEEE transactions on pattern analysis and machine in-               In Intelligent Robots and Systems (IROS), 2015 IEEE/RSJ
     telligence, 37(3):583–596, 2014. 1                                        International Conference on, pages 922–928. IEEE, 2015. 2
[11] Stefan Hinterstoisser, Vincent Lepetit, Slobodan Ilic, Ste-          [26] Francesc Moreno-noguer. EPnP: An Accurate O(n) Solution
     fan Holzer, Gary Bradski, Kurt Konolige, and Nassir Navab.                to the PnP Problem. Iccv, 2007. 2
     Model based training, detection and pose estimation of               [27] Markus Oberweger, Mahdi Rad, and Vincent Lepetit. Mak-
     texture-less 3d objects in heavily cluttered scenes. In Asian             ing deep heatmaps robust to partial occlusions for 3d object
     conference on computer vision, pages 548–562. Springer,                   pose estimation. In Proceedings of the European Conference
     2012. 2, 5, 6                                                             on Computer Vision (ECCV), pages 119–134, 2018. 1, 2, 4
[12] Stefan Hinterstoisser, Vincent Lepetit, Naresh Rajkumar, and         [28] Sida Peng, Yuan Liu, Qixing Huang, Hujun Bao, and Xi-
     Kurt Konolige. Going further with point pair features. In                 aowei Zhou. Pvnet: Pixel-wise voting network for 6dof pose
     European Conference on Computer Vision, pages 834–848.                    estimation. arXiv preprint arXiv:1812.11788, 2018. 1, 2, 4,
     Springer, 2016. 2, 7                                                      5, 6, 7
[13] Tomáš Hodaň, Jiřı́ Matas, and Štěpán Obdržálek. On evalu-   [29] Charles R. Qi, Wei Liu, Chenxia Wu, Hao Su, and
     ation of 6d object pose estimation. In European Conference                Leonidas J. Guibas. Frustum pointnets for 3d object detec-
     on Computer Vision, pages 606–619. Springer, 2016. 6                      tion from rgb-d data. In The IEEE Conference on Computer
     Vision and Pattern Recognition (CVPR), June 2018. 2, 3, 4,       [43] Bin Yang, Wenjie Luo, and Raquel Urtasun. Pixor: Real-
     6, 7                                                                  time 3d object detection from point clouds. In Proceed-
[30] Charles R. Qi, Hao Su, Kaichun Mo, and Leonidas J. Guibas.            ings of the IEEE Conference on Computer Vision and Pattern
     Pointnet: Deep learning on point sets for 3d classification           Recognition, pages 7652–7660, 2018. 2
     and segmentation. In The IEEE Conference on Computer             [44] Yuan Yuan, Jia Wan, and Qi Wang. Congested scene classifi-
     Vision and Pattern Recognition (CVPR), July 2017. 2, 3, 4,            cation via efficient unsupervised feature learning and density
     5                                                                     estimation. Pattern Recognition, 56:159–169, 2016. 2
[31] Charles Ruizhongtai Qi, Li Yi, Hao Su, and Leonidas J            [45] Sergey Zakharov, Ivan Shugurov, and Slobodan Ilic. Dpod:
     Guibas. Pointnet++: Deep hierarchical feature learning on             6d pose object detector and refiner. In Proceedings of the
     point sets in a metric space. In Advances in Neural Informa-          IEEE International Conference on Computer Vision, pages
     tion Processing Systems, pages 5099–5108, 2017. 4, 5                  1941–1950, 2019. 1, 7
[32] Mahdi Rad and Vincent Lepetit. Bb8: a scalable, accurate,        [46] Yin Zhou and Oncel Tuzel. Voxelnet: End-to-end learning
     robust to partial occlusion method for predicting the 3d poses        for point cloud based 3d object detection. In Proceedings
     of challenging objects without using depth. In Proceedings            of the IEEE Conference on Computer Vision and Pattern
     of the IEEE International Conference on Computer Vision,              Recognition, pages 4490–4499, 2018. 2, 5
     pages 3828–3836, 2017. 1, 2, 4                                   [47] Menglong Zhu, Konstantinos G Derpanis, Yinfei Yang,
[33] Mahdi Rad, Markus Oberweger, and Vincent Lepetit. Fea-                Samarth Brahmbhatt, Mabel Zhang, Cody Phillips, Matthieu
     ture mapping for learning fast and accurate 3d pose inference         Lecce, and Kostas Daniilidis. Single image 3d object detec-
     from synthetic images. In Proceedings of the IEEE Con-                tion and pose estimation for grasping. In Robotics and Au-
     ference on Computer Vision and Pattern Recognition, pages             tomation (ICRA), 2014 IEEE International Conference on,
     4663–4672, 2018. 1, 2, 4                                              pages 3936–3943. IEEE, 2014. 1
[34] Joseph Redmon and Ali Farhadi. Yolov3: An incremental
     improvement. arXiv preprint arXiv:1804.02767, 2018. 1, 3,
     5
[35] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.
     Faster r-cnn: Towards real-time object detection with region
     proposal networks. In Advances in neural information pro-
     cessing systems, pages 91–99, 2015. 1
[36] Younghak Shin and Ilangko Balasingham. Comparison of
     hand-craft feature based svm and cnn based deep learning
     framework for automatic polyp classification. In 2017 39th
     Annual International Conference of the IEEE Engineering in
     Medicine and Biology Society (EMBC), pages 3277–3280.
     IEEE, 2017. 2
[37] Alykhan Tejani. Latent-Class Hough Forests for 3D Object
     Detection and Pose Estimation of Rigid Objects. (Novem-
     ber), 2014. 2
[38] Bugra Tekin, Sudipta N. Sinha, and Pascal Fua. Real-time
     seamless single shot 6d object pose prediction. In The IEEE
     Conference on Computer Vision and Pattern Recognition
     (CVPR), June 2018. 1, 2, 4
[39] Jonathan Tremblay, Thang To, Balakumar Sundaralingam,
     Yu Xiang, Dieter Fox, and Stan Birchfield. Deep object pose
     estimation for semantic robotic grasping of household ob-
     jects. arXiv preprint arXiv:1809.10790, 2018. 1
[40] Chen Wang, Danfei Xu, Yuke Zhu, Roberto Martı́n-Martı́n,
     Cewu Lu, Li Fei-Fei, and Silvio Savarese. Densefusion: 6d
     object pose estimation by iterative dense fusion. 2019. 2, 5,
     7
[41] Paul Wohlhart and Vincent Lepetit. Learning descriptors for
     object recognition and 3d pose estimation. In Proceedings
     of the IEEE Conference on Computer Vision and Pattern
     Recognition, pages 3109–3118, 2015. 2
[42] Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, and
     Dieter Fox. Posecnn: A convolutional neural network for
     6d object pose estimation in cluttered scenes. arXiv preprint
     arXiv:1711.00199, 2017. 1, 2, 3, 5, 6, 7
